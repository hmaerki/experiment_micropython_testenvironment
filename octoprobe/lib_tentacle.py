from collections.abc import Iterator
import dataclasses
import io
from typing import Optional

import pyhubctl

from .util_constants import DIRECTORY_DOWNLOADS

from .util_baseclasses import TentacleType


from .util_programmers import programmer_factory, DutProgrammer

from .lib_mpremote import MpRemote
from .util_rp2 import (
    UDEV_FILTER_RP2_BOOT_MODE,
    UDEV_FILTER_RP2_APPLICATION_MODE,
    UdevApplicationModeEvent,
    rp2_flash_micropython,
)
from .util_pyudev import UdevEventBase, UdevPoller


@dataclasses.dataclass
class Tentacle:
    infra_rp2_unique_id: str
    tentacle_type: TentacleType
    plug_infra: Optional["UsbPlug"] = None
    plug_dut: Optional["UsbPlug"] = None
    mp_remote_infra: Optional[MpRemote] = None
    mp_remote_dut: Optional[MpRemote] = None
    programmer_dut: Optional[DutProgrammer] = None

    @property
    def description_short(self) -> str:
        assert self.plug_infra is not None
        assert self.plug_dut is not None

        f = io.StringIO()
        f.write(f"Label {self.tentacle_type.label}\n")
        f.write(f"  infra unique id {self.infra_rp2_unique_id}\n")

        f.write(f"  plug_infra: {self.plug_infra.description_short}\n")
        f.write(f"  plug_dut: {self.plug_dut.description_short}\n")

        return f.getvalue()

    def infra_relay(self, number: int, close: bool):
        assert self.mp_remote_infra is not None

        gpio = {
            1: "GPIO1",
            2: "GPIO2",
            3: "GPIO3",
            4: "GPIO4",
            5: "GPIO8",
        }[number]
        cmd_relay = f"""
from machine import Pin

pin_relay1 = Pin('{gpio}', Pin.OUT)
pin_relay1.value({int(close)})
"""
        self.mp_remote_infra.exec_raw(cmd=cmd_relay)

    def flash_dut(self, udev: "UdevPoller") -> None:
        if self.plug_dut is None:
            return

        self.programmer_dut = programmer_factory(tags=self.tentacle_type.tags)
        if self.programmer_dut is None:
            return

        tty = self.programmer_dut.flash(tentacle=self, udev=udev, plug=self.plug_dut)

        assert self.mp_remote_dut is None
        self.mp_remote_dut = MpRemote(tty=tty)

        hallo = self.mp_remote_dut.exec_raw("print('Hallo')").strip()
        assert hallo == "Hallo"

    def all_plugs_power_off(self) -> None:
        for plug in (self.plug_infra, self.plug_dut):
            if plug is not None:
                plug.power = False

    def reset_infa_dut(self) -> None:
        self.all_plugs_power_off()

    def rp2_get_unique_id(self, event: UdevEventBase) -> str:
        assert isinstance(event, UdevApplicationModeEvent)

        assert self.mp_remote_infra is None
        self.mp_remote_infra = MpRemote(tty=event.tty)
        print(f"Event: {event!r}")
        mp_program = """
import machine
import ubinascii

def get_unique_id():
    return ubinascii.hexlify(machine.unique_id()).decode('ascii').upper()
"""
        self.mp_remote_infra.exec_raw(mp_program)
        unique_id = self.mp_remote_infra.exec_raw("print(get_unique_id())")
        return unique_id.strip()

    def setup_infra(self, udev: UdevPoller) -> None:
        if self.plug_infra is None:
            return

        with udev.guard as guard:
            self.plug_infra.power = True

            event = guard.expect_event(UDEV_FILTER_RP2_BOOT_MODE, timeout_s=2.0)

        with udev.guard as guard:
            rp2_flash_micropython(event, DIRECTORY_DOWNLOADS / "firmware.uf2")

            event = udev.expect_event(UDEV_FILTER_RP2_APPLICATION_MODE, timeout_s=3.0)

        unique_id = self.rp2_get_unique_id(event)
        assert unique_id == self.infra_rp2_unique_id


@dataclasses.dataclass
class Tentacles:
    tentacles: list[Tentacle]

    @property
    def plugs_infra(self) -> Iterator["UsbPlug"]:
        for tentacle in self.tentacles:
            if tentacle.plug_infra is None:
                continue
            yield tentacle.plug_infra

    @property
    def plugs_dut(self) -> Iterator["UsbPlug"]:
        for tentacle in self.tentacles:
            if tentacle.plug_dut is None:
                continue
            yield tentacle.plug_dut


@dataclasses.dataclass
class UsbHub:
    label: str
    model: pyhubctl.Hub
    connected_hub: None | pyhubctl.DualConnectedHub = None

    def get_plug(self, plug_number: int) -> "UsbPlug":
        assert 1 <= plug_number <= self.model.plug_count
        return UsbPlug(usb_hub=self, plug_number=plug_number)

    def setup(self) -> None:
        connected_hubs = self.model.find_connected_dualhubs()
        self.connected_hub = connected_hubs.get_one()

    def teardown(self) -> None:
        pass

    @property
    def description_short(self) -> str:
        f = io.StringIO()
        f.write(f"Label {self.label}\n")
        f.write(f"  Model {self.model.model}\n")
        return f.getvalue()


@dataclasses.dataclass
class UsbPlug:
    usb_hub: UsbHub
    plug_number: int

    @property
    def description_short(self) -> str:
        return f"plug {self.plug_number} on '{self.usb_hub.label}' ({self.usb_hub.model.model})"

    @property
    def power(self) -> bool:
        raise NotImplementedError()

    @power.setter
    def power(self, on: bool) -> None:
        self.usb_hub.connected_hub.get_plug(plug_number=self.plug_number).power(on=on)