# Errors on v0.3

* TODO: Verify bom
  * https://jlcpcb.com/parts/bom-tool/
  * `Do not place` these parts:
```text
prototype_GND
octoprobe_breakout_PB
BP1301_168,BP1301_167,BP1301_166,BP1301_165,BP1301_164,BP1301_163,BP1301_162,BP1301_161,BP1301_160,BP1301_159,BP1301_158,BP1301_157,BP1301_156,BP1301_155,BP1301_154,BP1301_153,BP1301_152,BP1301_151,BP1301_150,BP1301_149,BP1301_148,BP1301_147,BP1301_146,BP1301_145,BP1301_144,BP1301_143,BP1301_142,BP1301_141,BP1301_140,BP1301_139,BP1301_138,BP1301_137,BP1301_136,BP1301_135,BP1301_134,BP1301_133,BP1301_132,BP1301_131,BP1301_130,BP1301_129,BP1301_128,BP1301_127,BP1301_126,BP1301_125,BP1301_124,BP1301_123,BP1301_122,BP1301_121,BP1301_120,BP1301_119,BP1301_118,BP1301_117,BP1301_116,BP1301_115,BP1301_114,BP1301_113,BP1301_112,BP1301_111,BP1301_110,BP1301_109,BP1301_108,BP1301_107,BP1301_106,BP1301_105,BP1301_104,BP1301_103,BP1301_102,BP1301_101,BP1301_100,BP1301_99,BP1301_98,BP1301_97,BP1301_96,BP1301_95,BP1301_94,BP1301_93,BP1301_92,BP1301_91,BP1301_90,BP1301_89,BP1301_88,BP1301_87,BP1301_86,BP1301_85,BP1301_84,BP1301_83,BP1301_82,BP1301_81,BP1301_80,BP1301_79,BP1301_78,BP1301_77,BP1301_76,BP1301_75,BP1301_74,BP1301_73,BP1301_72,BP1301_71,BP1301_70,BP1301_69,BP1301_68,BP1301_67,BP1301_66,BP1301_65,BP1301_64,BP1301_63,BP1301_62,BP1301_61,BP1301_60,BP1301_59,BP1301_58,BP1301_57,BP1301_56,BP1301_55,BP1301_54,BP1301_53,BP1301_52,BP1301_51,BP1301_50,BP1301_49,BP1301_48,BP1301_47,BP1301_46,BP1301_45,BP1301_44,BP1301_43,BP1301_42,BP1301_41,BP1301_40,BP1301_39,BP1301_38,BP1301_37,BP1301_36,BP1301_35,BP1301_34,BP1301_33,BP1301_32,BP1301_31,BP1301_30,BP1301_29,BP1301_28,BP1301_27,BP1301_26,BP1301_25,BP1301_24,BP1301_23,BP1301_22,BP1301_21,BP1301_20,BP1301_19,BP1301_18,BP1301_17,BP1301_16,BP1301_15,BP1301_14,BP1301_13,BP1301_12,BP1301_11,BP1301_10,BP1301_9,BP1301_8,BP1301_7,BP1301_6,BP1301_5,BP1301_4,BP1301_3,BP1301_2,BP1301
No matches found
prototype_NC
octoprobe_breakout_PB_NC
BP1302_352,BP1302_351,BP1302_350,BP1302_349,BP1302_348,BP1302_347,BP1302_346,BP1302_345,BP1302_344,BP1302_343,BP1302_342,BP1302_341,BP1302_340,BP1302_339,BP1302_338,BP1302_337,BP1302_336,BP1302_335,BP1302_334,BP1302_333,BP1302_332,BP1302_331,BP1302_330,BP1302_329,BP1302_328,BP1302_327,BP1302_326,BP1302_325,BP1302_324,BP1302_323,BP1302_322,BP1302_321,BP1302_320,BP1302_319,BP1302_318,BP1302_317,BP1302_316,BP1302_315,BP1302_314,BP1302_313,BP1302_312,BP1302_311,BP1302_310,BP1302_309,BP1302_308,BP1302_307,BP1302_306,BP1302_305,BP1302_304,BP1302_303,BP1302_302,BP1302_301,BP1302_300,BP1302_299,BP1302_298,BP1302_297,BP1302_296,BP1302_295,BP1302_294,BP1302_293,BP1302_292,BP1302_291,BP1302_290,BP1302_289,BP1302_288,BP1302_287,BP1302_286,BP1302_285,BP1302_284,BP1302_283,BP1302_282,BP1302_281,BP1302_280,BP1302_279,BP1302_278,BP1302_277,BP1302_276,BP1302_275,BP1302_274,BP1302_273,BP1302_272,BP1302_271,BP1302_270,BP1302_269,BP1302_268,BP1302_267,BP1302_266,BP1302_265,BP1302_264,BP1302_263,BP1302_262,BP1302_261,BP1302_260,BP1302_259,BP1302_258,BP1302_257,BP1302_256,BP1302_255,BP1302_254,BP1302_253,BP1302_252,BP1302_251,BP1302_250,BP1302_249,BP1302_248,BP1302_247,BP1302_246,BP1302_245,BP1302_244,BP1302_243,BP1302_242,BP1302_241,BP1302_240,BP1302_239,BP1302_238,BP1302_237,BP1302_236,BP1302_235,BP1302_234,BP1302_233,BP1302_232,BP1302_231,BP1302_230,BP1302_229,BP1302_228,BP1302_227,BP1302_226,BP1302_225,BP1302_224,BP1302_223,BP1302_222,BP1302_221,BP1302_220,BP1302_219,BP1302_218,BP1302_217,BP1302_216,BP1302_215,BP1302_214,BP1302_213,BP1302_212,BP1302_211,BP1302_210,BP1302_209,BP1302_208,BP1302_207,BP1302_206,BP1302_205,BP1302_204,BP1302_203,BP1302_202,BP1302_201,BP1302_200,BP1302_199,BP1302_198,BP1302_197,BP1302_196,BP1302_195,BP1302_194,BP1302_193,BP1302_192,BP1302_191,BP1302_190,BP1302_189,BP1302_188,BP1302_187,BP1302_186,BP1302_185,BP1302_184,BP1302_183,BP1302_182,BP1302_181,BP1302_180,BP1302_179,BP1302_178,BP1302_177,BP1302_176,BP1302_175,BP1302_174,BP1302_173,BP1302_172,BP1302_171,BP1302_170,BP1302_169,BP1302_168,BP1302_167,BP1302_166,BP1302_165,BP1302_164,BP1302_163,BP1302_162,BP1302_161,BP1302_160,BP1302_159,BP1302_158,BP1302_157,BP1302_156,BP1302_155,BP1302_154,BP1302_153
No matches found
prototype_NC
octoprobe_breakout_PB_NC
BP1302_152,BP1302_151,BP1302_150,BP1302_149,BP1302_148,BP1302_147,BP1302_146,BP1302_145,BP1302_144,BP1302_143,BP1302_142,BP1302_141,BP1302_140,BP1302_139,BP1302_138,BP1302_137,BP1302_136,BP1302_135,BP1302_134,BP1302_133,BP1302_132,BP1302_131,BP1302_130,BP1302_129,BP1302_128,BP1302_127,BP1302_126,BP1302_125,BP1302_124,BP1302_123,BP1302_122,BP1302_121,BP1302_120,BP1302_119,BP1302_118,BP1302_117,BP1302_116,BP1302_115,BP1302_114,BP1302_113,BP1302_112,BP1302_111,BP1302_110,BP1302_109,BP1302_108,BP1302_107,BP1302_106,BP1302_105,BP1302_104,BP1302_103,BP1302_102,BP1302_101,BP1302_100,BP1302_99,BP1302_98,BP1302_97,BP1302_96,BP1302_95,BP1302_94,BP1302_93,BP1302_92,BP1302_91,BP1302_90,BP1302_89,BP1302_88,BP1302_87,BP1302_86,BP1302_85,BP1302_84,BP1302_83,BP1302_82,BP1302_81,BP1302_80,BP1302_79,BP1302_78,BP1302_77,BP1302_76,BP1302_75,BP1302_74,BP1302_73,BP1302_72,BP1302_71,BP1302_70,BP1302_69,BP1302_68,BP1302_67,BP1302_66,BP1302_65,BP1302_64,BP1302_63,BP1302_62,BP1302_61,BP1302_60,BP1302_59,BP1302_58,BP1302_57,BP1302_56,BP1302_55,BP1302_54,BP1302_53,BP1302_52,BP1302_51,BP1302_50,BP1302_49,BP1302_48,BP1302_47,BP1302_46,BP1302_45,BP1302_44,BP1302_43,BP1302_42,BP1302_41,BP1302_40,BP1302_39,BP1302_38,BP1302_37,BP1302_36,BP1302_35,BP1302_34,BP1302_33,BP1302_32,BP1302_31,BP1302_30,BP1302_29,BP1302_28,BP1302_27,BP1302_26,BP1302_25,BP1302_24,BP1302_23,BP1302_22,BP1302_21,BP1302_20,BP1302_19,BP1302_18,BP1302_17,BP1302_16,BP1302_15,BP1302_14,BP1302_13,BP1302_12,BP1302_11,BP1302_10,BP1302_9,BP1302_8,BP1302_7,BP1302_6,BP1302_5,BP1302_4,BP1302_3,BP1302_2,BP1302
No matches found
GPIO9
octoprobe_breakout_label
BP201
No matches found
GPIO10
octoprobe_breakout_label
BP202
No matches found
GPIO11
octoprobe_breakout_label
BP203
No matches found
GPIO12
octoprobe_breakout_label
BP204
No matches found
GPIO13
octoprobe_breakout_label
BP205
No matches found
GPIO14
octoprobe_breakout_label
BP206
No matches found
GPIO15
octoprobe_breakout_label
BP207
No matches found
octoprobe_MountingHole
MountingHole_3.2mm_M3_DIN965_Pad
H1305,H1306,H1307,H1308
No matches found
```
