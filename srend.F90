c #this file has been revised to include only the most important bits!

! HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
! hard-coded color table for renderer; read in once offset_cotab : where
! to start reading tables the table reading/forming ends with a
! '255 ...' entry.  These hardcoded entries below are working examples.
! These DATA entries and the arrays above holding SREND_COTAB_KEYS lines
! can be modified to suit, of course.
! --------------------------------------------------------------------

! -------- write alpha knots here -------
! LCSE original ------------------------------------------------------------------------------
      DATA alpha_knot(1)   /'  0 0.0   '/ , rgb_knot(1)  /'  0 0.0       0.0       0.0      '/
      DATA alpha_knot(2)   /'  5 0.0   '/ , rgb_knot(2)  /'  5 0.0       0.0       0.0      '/
      DATA alpha_knot(3)   /' 36 0.0627'/ , rgb_knot(3)  /' 36 0.0       0.0       0.2509804'/
      DATA                                  rgb_knot(4)  /' 71 0.0       0.1176471 0.3137255'/
      DATA alpha_knot(4)   /' 72 0.148 '/
      DATA alpha_knot(5)   /'105 0.536 '/ , rgb_knot(5)  /'105 0.0       0.7843137 1.0      '/
      DATA                                  rgb_knot(6)  /'131 1.0       1.0       1.0      '/
      DATA alpha_knot(6)   /'133 1.0   '/
      DATA alpha_knot(7)   /'158 1.0   '/ , rgb_knot(7)  /'158 1.0       1.0       0.0      '/
      DATA alpha_knot(8)   /'196 0.328 '/ , rgb_knot(8)  /'196 1.0       0.0       0.0      '/
      DATA alpha_knot(9)   /'236 0.302 '/
      DATA alpha_knot(10)  /'244 0.105 '/ , rgb_knot(9)  /'244 0.5019608 0.0       0.0      '/
      DATA alpha_knot(11)  /'250 0.0   '/
      DATA alpha_knot(12)  /'255 0.0   '/ , rgb_knot(10) /'255 0.5019608 0.0       0.0      '/

! linear blue-red ------------------------------------------------------
      DATA alpha_knot(24) /'  0 1.0'/ , rgb_knot(24) /'  0 0.0 0.0 1.0'/
      DATA alpha_knot(25) /'255 1.0'/ , rgb_knot(25) /'255 1.0 0.0 0.0'/

! upscale: for testing ---------------------------------------------------
      DATA alpha_knot(30) /'  0 0.0  '/ , rgb_knot(30) /'  0 1.0 0.0 0.0'/
      DATA alpha_knot(31) /'  1 0.001'/
      DATA alpha_knot(32) /'  2 0.01 '/
      DATA alpha_knot(33) /'  4 0.1  '/
      DATA alpha_knot(34) /'  8 0.2  '/
      DATA alpha_knot(35) /' 32 0.4  '/ , rgb_knot(31) /' 32 0.5 0.5 0.0'/
      DATA alpha_knot(36) /' 64 0.5  '/ , rgb_knot(32) /' 64 0.0 1.0 0.0'/
      DATA alpha_knot(37) /'128 0.6  '/ , rgb_knot(33) /'128 0.0 0.5 0.5'/
      DATA alpha_knot(38) /'192 0.7  '/ , rgb_knot(34) /'192 0.5 0.5 1.0'/
      DATA alpha_knot(39) /'224 0.8  '/
      DATA alpha_knot(40) /'255 1.0  '/ , rgb_knot(35) /'255 0.9 0.9 1.0'/

! red up, blue down ----------------------------------------------------
      DATA alpha_knot(80) /'  0 1.0'/ , rgb_knot(80) /'  0 0.5 0.5 1.0'/
      DATA alpha_knot(81) /' 32 0.2'/ , rgb_knot(81) /' 32 0.5 0.5 1.0'/
      DATA alpha_knot(82) /' 64 0.1'/ , rgb_knot(82) /' 64 0.2 0.2 1.0'/
      DATA alpha_knot(83) /'128 0.0'/ , rgb_knot(83) /'128 0.0 0.0 0.0'/
      DATA alpha_knot(84) /'192 0.1'/ , rgb_knot(84) /'192 1.0 0.2 0.2'/
      DATA alpha_knot(85) /'224 0.2'/
      DATA alpha_knot(86) /'255 1.0'/ , rgb_knot(85) /'255 1.0 0.5 0.5'/

! Woodward's Star AMR code lut: entropy ----------------------------------------------------------
      DATA alpha_knot(110) /'  0 0.0      '/ , rgb_knot(110) /'  0 0.0       0.0       0.0      '/
      DATA alpha_knot(111) /' 18 0.1058824'/ , rgb_knot(111) /' 18 0.0       0.0       0.2509804'/
      DATA alpha_knot(112) /' 97 0.1294118'/
      DATA alpha_knot(113) /'131 0.2588235'/
      DATA                                     rgb_knot(112) /'149 0.0       0.2352941 0.627451 '/
      DATA                                     rgb_knot(113) /'154 0.0       0.7843137 1.0      '/
      DATA alpha_knot(114) /'157 0.2156863'/
      DATA                                     rgb_knot(114) /'159 1.0       1.0       1.0      '/
      DATA alpha_knot(115) /'165 0.0      '/ , rgb_knot(115) /'165 1.0       1.0       0.0      '/
      DATA alpha_knot(116) /'171 0.3803922'/
      DATA                                     rgb_knot(116) /'175 1.0       0.0       0.0      '/
      DATA alpha_knot(117) /'184 0.5490196'/
      DATA alpha_knot(118) /'203 0.454902 '/
      DATA                                     rgb_knot(117) /'231 0.5019608 0.0       0.0      '/
      DATA alpha_knot(119) /'254 0.1686275'/
      DATA alpha_knot(120) /'255 0.1254902'/ , rgb_knot(118) /'255 0.5019608 0.0       0.0      '/

! Woodward's Star AMR code lut: NegDivU
      DATA alpha_knot(121) /'0 0.0'/
      DATA alpha_knot(122) /'7 0.254902'/
      DATA alpha_knot(123) /'61 0.3058824'/
      DATA alpha_knot(124) /'108 0.6078432'/
      DATA alpha_knot(125) /'135 0.4705882'/
      DATA alpha_knot(126) /'159 0.3098039'/
      DATA alpha_knot(127) /'192 0.1921569'/
      DATA alpha_knot(128) /'202 0.1333333'/
      DATA alpha_knot(129) /'254 0.09411765'/
      DATA alpha_knot(130) /'255 0.1254902'/
         DATA rgb_knot(121) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(122) /'12 0.03921569 0.0 0.0'/
         DATA rgb_knot(123) /'26 1.0 0.0 0.0'/
         DATA rgb_knot(124) /'41 1.0 0.2509804 0.0'/
         DATA rgb_knot(125) /'79 1.0 1.0 0.0'/
         DATA rgb_knot(126) /'106 1.0 1.0 0.5019608'/
         DATA rgb_knot(127) /'131 1.0 1.0 1.0'/
         DATA rgb_knot(128) /'181 0.5019608 0.5019608 1.0'/
         DATA rgb_knot(129) /'195 0.0 0.0 1.0'/
         DATA rgb_knot(130) /'212 0.0 0.0 0.5019608'/
         DATA rgb_knot(131) /'255 0.0 0.0 0.4'/
! Woodward's Star AMR code lut: FV demoSC08
      DATA alpha_knot(132) /'0 0.0'/
      DATA alpha_knot(133) /'18 0.1058824'/
      DATA alpha_knot(134) /'96 0.2745098'/
      DATA alpha_knot(135) /'115 0.7843137'/
      DATA alpha_knot(136) /'133 1.0'/
      DATA alpha_knot(137) /'158 1.0'/
      DATA alpha_knot(138) /'184 0.5490196'/
      DATA alpha_knot(139) /'203 0.454902'/
      DATA alpha_knot(140) /'254 0.1686275'/
      DATA alpha_knot(141) /'255 0.1254902'/
         DATA rgb_knot(132) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(133) /'18 0.0 0.0 0.2509804'/
         DATA rgb_knot(134) /'77 0.0 0.2352941 0.627451'/
         DATA rgb_knot(135) /'108 0.0 0.7843137 1.0'/
         DATA rgb_knot(136) /'131 1.0 1.0 1.0'/
         DATA rgb_knot(137) /'158 1.0 1.0 0.0'/
         DATA rgb_knot(138) /'196 1.0 0.0 0.0'/
         DATA rgb_knot(139) /'244 0.5019608 0.0 0.0'/
         DATA rgb_knot(140) /'255 0.5019608 0.0 0.0'/
! Woodward's Star AMR code lut: Ur
      DATA alpha_knot(142) /'0 1.0'/
      DATA alpha_knot(143) /'36 1.0'/
      DATA alpha_knot(144) /'70 0.372549'/
      DATA alpha_knot(145) /'107 0.254902'/
      DATA alpha_knot(146) /'128 0.05882353'/
      DATA alpha_knot(147) /'151 0.2705882'/
      DATA alpha_knot(148) /'194 0.5450981'/
      DATA alpha_knot(149) /'240 1.0'/
      DATA alpha_knot(150) /'255 1.0'/
         DATA rgb_knot(142) /'0 1.0 1.0 1.0'/
         DATA rgb_knot(143) /'76 0.0 1.0 1.0'/
         DATA rgb_knot(144) /'90 0.0 0.0 1.0'/
         DATA rgb_knot(145) /'103 0.0 0.0 0.5019608'/
         DATA rgb_knot(146) /'118 0.0 0.0 0.0'/
         DATA rgb_knot(147) /'128 0.25 0.25 0.25'/
         DATA rgb_knot(148) /'144 0.4156863 0.3568628 0.3568628'/
         DATA rgb_knot(149) /'163 1.0 0.0 0.0'/
         DATA rgb_knot(150) /'183 1.0 1.0 0.0'/
         DATA rgb_knot(151) /'208 1.0 1.0 0.0'/
         DATA rgb_knot(152) /'255 1.0 1.0 0.0'/
! Woodward's Star AMR code lut: Vort
      DATA alpha_knot(153) /'0 0.0'/
      DATA alpha_knot(154) /'8 0.03137255'/
      DATA alpha_knot(155) /'20 0.0627451'/
      DATA alpha_knot(156) /'32 0.7843137'/
      DATA alpha_knot(157) /'133 1.0'/
      DATA alpha_knot(158) /'153 0.8941177'/
      DATA alpha_knot(159) /'197 0.2431373'/
      DATA alpha_knot(160) /'241 0.2588235'/
      DATA alpha_knot(161) /'255 0.0'/
         DATA rgb_knot(153) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(154) /'24 0.0 0.0 0.3921569'/
         DATA rgb_knot(155) /'41 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(156) /'81 0.0 1.0 1.0'/
         DATA rgb_knot(157) /'115 1.0 1.0 1.0'/
         DATA rgb_knot(158) /'153 1.0 1.0 0.0'/
         DATA rgb_knot(159) /'197 1.0 0.0 0.0'/
         DATA rgb_knot(160) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(161) /'255 0.0 0.0 0.0'/
! all white blue
      DATA alpha_knot(170) /  '0 1.0'/
      DATA alpha_knot(171) /'255 1.0'/
         DATA rgb_knot(170) /  '0 1. 1. 1.'/
         DATA rgb_knot(171) /'255 1. 1. 1.'/
! Woodward C64-FV-6a-for-Vort-slice.lut
      DATA alpha_knot(201) /'0 0.0'/
      DATA alpha_knot(202) /'8 0.03137255'/
      DATA alpha_knot(203) /'20 0.0627451'/
      DATA alpha_knot(204) /'32 0.7843137'/
      DATA alpha_knot(205) /'133 1.0'/
      DATA alpha_knot(206) /'153 0.8941177'/
      DATA alpha_knot(207) /'197 0.2431373'/
      DATA alpha_knot(208) /'241 0.2588235'/
      DATA alpha_knot(209) /'255 0.0'/
         DATA rgb_knot(201) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(202) /'24 0.0 0.0 0.3921569'/
         DATA rgb_knot(203) /'41 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(204) /'81 0.0 1.0 1.0'/
         DATA rgb_knot(205) /'115 1.0 1.0 1.0'/
         DATA rgb_knot(206) /'153 1.0 1.0 0.0'/
         DATA rgb_knot(207) /'197 1.0 0.0 0.0'/
         DATA rgb_knot(208) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(209) /'255 0.0 0.0 0.0'/
! Woodward demoSC08-FV-good-colors-for-tp3-density7.lut
      DATA alpha_knot(211) /'0 0.0'/
      DATA alpha_knot(212) /'18 0.1058824'/
      DATA alpha_knot(213) /'97 0.1294118'/
      DATA alpha_knot(214) /'130 0.1058824'/
      DATA alpha_knot(215) /'158 0.2156863'/
      DATA alpha_knot(216) /'171 0.3803922'/
      DATA alpha_knot(217) /'184 0.5490196'/
      DATA alpha_knot(218) /'203 0.454902'/
      DATA alpha_knot(219) /'254 0.1686275'/
      DATA alpha_knot(220) /'255 0.1254902'/
         DATA rgb_knot(211) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(212) /'18 0.0 0.0 0.2509804'/
         DATA rgb_knot(213) /'137 0.0 0.2352941 0.627451'/
         DATA rgb_knot(214) /'148 0.0 0.7843137 1.0'/
         DATA rgb_knot(215) /'159 1.0 1.0 1.0'/
         DATA rgb_knot(216) /'179 1.0 1.0 0.0'/
         DATA rgb_knot(217) /'207 1.0 0.0 0.0'/
         DATA rgb_knot(218) /'231 0.5019608 0.0 0.0'/
         DATA rgb_knot(219) /'255 0.5019608 0.0 0.0'/
! Woodward demoSC08-FV-good-colors-for-tp3-density7-for-vort2.lut
      DATA alpha_knot(221) /'0 0.0'/
      DATA alpha_knot(222) /'18 0.1058824'/
      DATA alpha_knot(223) /'97 0.1294118'/
      DATA alpha_knot(224) /'130 0.1058824'/
      DATA alpha_knot(225) /'158 0.2156863'/
      DATA alpha_knot(226) /'171 0.3803922'/
      DATA alpha_knot(227) /'184 0.5490196'/
      DATA alpha_knot(228) /'203 0.454902'/
      DATA alpha_knot(229) /'254 0.1686275'/
      DATA alpha_knot(230) /'255 0.1254902'/
         DATA rgb_knot(221) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(222) /'129 0.0 0.0 0.2509804'/
         DATA rgb_knot(223) /'137 0.0 0.2352941 0.627451'/
         DATA rgb_knot(224) /'148 0.0 0.7843137 1.0'/
         DATA rgb_knot(225) /'159 1.0 1.0 1.0'/
         DATA rgb_knot(226) /'170 1.0 1.0 0.0'/
         DATA rgb_knot(227) /'207 1.0 0.0 0.0'/
         DATA rgb_knot(228) /'231 0.5019608 0.0 0.0'/
         DATA rgb_knot(229) /'255 0.5019608 0.0 0.0'/
! Woodward demoSC08-FV-good-colors-for-tp3-density9.lut
      DATA alpha_knot(231) /'0 0.0'/
      DATA alpha_knot(232) /'18 0.1058824'/
      DATA alpha_knot(233) /'97 0.1294118'/
      DATA alpha_knot(234) /'130 0.1058824'/
      DATA alpha_knot(235) /'158 0.2156863'/
      DATA alpha_knot(236) /'171 0.3803922'/
      DATA alpha_knot(237) /'184 0.5490196'/
      DATA alpha_knot(238) /'203 0.454902'/
      DATA alpha_knot(239) /'254 0.1686275'/
      DATA alpha_knot(240) /'255 0.1254902'/
         DATA rgb_knot(231) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(232) /'18 0.0 0.0 0.2509804'/
         DATA rgb_knot(233) /'137 0.0 0.2352941 0.627451'/
         DATA rgb_knot(234) /'148 0.0 0.7843137 1.0'/
         DATA rgb_knot(235) /'159 1.0 1.0 1.0'/
         DATA rgb_knot(236) /'170 1.0 1.0 0.0'/
         DATA rgb_knot(237) /'231 1.0 0.0 0.0'/
         DATA rgb_knot(238) /'243 0.5019608 0.0 0.0'/
         DATA rgb_knot(239) /'255 0.5019608 0.0 0.0'/
! Woodward demoSC08-FV-good-colors-for-tp3-density12.lut
      DATA alpha_knot(241) /'0 0.0'/
      DATA alpha_knot(242) /'18 0.1058824'/
      DATA alpha_knot(243) /'97 0.1294118'/
      DATA alpha_knot(244) /'130 0.1058824'/
      DATA alpha_knot(245) /'210 0.2156863'/
      DATA alpha_knot(246) /'225 0.3803922'/
      DATA alpha_knot(247) /'236 0.5490196'/
      DATA alpha_knot(248) /'246 0.454902'/
      DATA alpha_knot(249) /'253 0.2235294'/
      DATA alpha_knot(250) /'255 0.1254902'/
         DATA rgb_knot(241) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(242) /'18 0.0 0.0 0.2509804'/
         DATA rgb_knot(243) /'137 0.0 0.2352941 0.627451'/
         DATA rgb_knot(244) /'193 0.0 0.7843137 1.0'/
         DATA rgb_knot(245) /'212 1.0 1.0 1.0'/
         DATA rgb_knot(246) /'228 1.0 1.0 0.0'/
         DATA rgb_knot(247) /'241 1.0 0.0 0.0'/
         DATA rgb_knot(248) /'250 0.3921569 0.0 0.0'/
         DATA rgb_knot(249) /'255 0.5019608 0.0 0.0'/
! Woodward LogFV.lut
      DATA alpha_knot(251) /'0 0.0'/
      DATA alpha_knot(252) /'18 0.1058824'/
      DATA alpha_knot(253) /'96 0.2745098'/
      DATA alpha_knot(254) /'115 0.7843137'/
      DATA alpha_knot(255) /'133 1.0'/
      DATA alpha_knot(256) /'158 1.0'/
      DATA alpha_knot(257) /'184 0.5490196'/
      DATA alpha_knot(258) /'203 0.454902'/
      DATA alpha_knot(259) /'254 0.1686275'/
      DATA alpha_knot(260) /'255 0.1254902'/
         DATA rgb_knot(251) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(252) /'18 0.0 0.0 0.2509804'/
         DATA rgb_knot(253) /'77 0.0 0.2352941 0.627451'/
         DATA rgb_knot(254) /'108 0.0 0.7843137 1.0'/
         DATA rgb_knot(255) /'131 1.0 1.0 1.0'/
         DATA rgb_knot(256) /'158 1.0 1.0 0.0'/
         DATA rgb_knot(257) /'196 1.0 0.0 0.0'/
         DATA rgb_knot(258) /'244 0.5019608 0.0 0.0'/
         DATA rgb_knot(259) /'255 0.5019608 0.0 0.0'/
! Woodward LowZAGB-NegDivU-1.lut
      DATA alpha_knot(261) /'0 0.0'/
      DATA alpha_knot(262) /'7 0.254902'/
      DATA alpha_knot(263) /'61 0.3058824'/
      DATA alpha_knot(264) /'108 0.6078432'/
      DATA alpha_knot(265) /'135 0.4705882'/
      DATA alpha_knot(266) /'159 0.3098039'/
      DATA alpha_knot(267) /'192 0.1921569'/
      DATA alpha_knot(268) /'202 0.1333333'/
      DATA alpha_knot(269) /'254 0.09411765'/
      DATA alpha_knot(270) /'255 0.1254902'/
         DATA rgb_knot(261) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(262) /'12 0.03921569 0.0 0.0'/
         DATA rgb_knot(263) /'26 1.0 0.0 0.0'/
         DATA rgb_knot(264) /'41 1.0 0.2509804 0.0'/
         DATA rgb_knot(265) /'79 1.0 1.0 0.0'/
         DATA rgb_knot(266) /'106 1.0 1.0 0.5019608'/
         DATA rgb_knot(267) /'131 1.0 1.0 1.0'/
         DATA rgb_knot(268) /'181 0.5019608 0.5019608 1.0'/
         DATA rgb_knot(269) /'195 0.0 0.0 1.0'/
         DATA rgb_knot(270) /'212 0.0 0.0 0.5019608'/
         DATA rgb_knot(271) /'255 0.0 0.0 0.4'/
! Woodward LowZAGB-Ur-00.lut
      DATA alpha_knot(272) /'0 1.0'/
      DATA alpha_knot(273) /'36 1.0'/
      DATA alpha_knot(274) /'70 0.372549'/
      DATA alpha_knot(275) /'107 0.254902'/
      DATA alpha_knot(276) /'128 0.05882353'/
      DATA alpha_knot(277) /'151 0.2705882'/
      DATA alpha_knot(278) /'194 0.5450981'/
      DATA alpha_knot(279) /'240 1.0'/
      DATA alpha_knot(280) /'255 1.0'/
         DATA rgb_knot(272) /'0 1.0 1.0 1.0'/
         DATA rgb_knot(273) /'103 0.0 1.0 1.0'/
         DATA rgb_knot(274) /'112 0.0 0.0 1.0'/
         DATA rgb_knot(275) /'119 0.0 0.0 0.5019608'/
         DATA rgb_knot(276) /'124 0.0 0.0 0.0'/
         DATA rgb_knot(277) /'128 0.25 0.25 0.25'/
         DATA rgb_knot(278) /'133 0.4156863 0.3568628 0.3568628'/
         DATA rgb_knot(279) /'139 1.0 0.0 0.0'/
         DATA rgb_knot(280) /'143 1.0 1.0 0.0'/
         DATA rgb_knot(281) /'255 1.0 1.0 0.0'/
! Woodward LowZAGB-Ur-5.lut
      DATA alpha_knot(282) /'0 1.0'/
      DATA alpha_knot(283) /'36 1.0'/
      DATA alpha_knot(284) /'64 0.3372549'/
      DATA alpha_knot(285) /'91 0.1137255'/
      DATA alpha_knot(286) /'128 0.05882353'/
      DATA alpha_knot(287) /'173 0.1372549'/
      DATA alpha_knot(288) /'220 0.5450981'/
      DATA alpha_knot(289) /'240 1.0'/
      DATA alpha_knot(290) /'255 1.0'/
         DATA rgb_knot(282) /'0 1.0 1.0 1.0'/
         DATA rgb_knot(283) /'35 0.0 1.0 1.0'/
         DATA rgb_knot(284) /'63 0.0 0.0 1.0'/
         DATA rgb_knot(285) /'92 0.0 0.0 0.5019608'/
         DATA rgb_knot(286) /'118 0.0 0.0 0.0'/
         DATA rgb_knot(287) /'128 0.3764706 0.3764706 0.3764706'/
         DATA rgb_knot(288) /'144 0.4156863 0.3568628 0.3568628'/
         DATA rgb_knot(289) /'174 1.0 0.0 0.0'/
         DATA rgb_knot(290) /'219 1.0 1.0 0.0'/
         DATA rgb_knot(291) /'255 1.0 1.0 0.0'/
! Woodward LowZAGB-Entropy-1.lut
      DATA alpha_knot(292) /'0 0.0'/
      DATA alpha_knot(293) /'18 0.1058824'/
      DATA alpha_knot(294) /'97 0.1294118'/
      DATA alpha_knot(295) /'131 0.2588235'/
      DATA alpha_knot(296) /'157 0.2156863'/
      DATA alpha_knot(297) /'165 0.0'/
      DATA alpha_knot(298) /'171 0.3803922'/
      DATA alpha_knot(299) /'184 0.5490196'/
      DATA alpha_knot(300) /'203 0.454902'/
      DATA alpha_knot(301) /'255 0.1686275'/
         DATA rgb_knot(292) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(293) /'18 0.0 0.0 0.2509804'/
         DATA rgb_knot(294) /'149 0.0 0.2352941 0.627451'/
         DATA rgb_knot(295) /'154 0.0 0.7843137 1.0'/
         DATA rgb_knot(296) /'159 1.0 1.0 1.0'/
         DATA rgb_knot(297) /'165 1.0 1.0 0.0'/
         DATA rgb_knot(298) /'175 1.0 0.0 0.0'/
         DATA rgb_knot(299) /'231 0.5019608 0.0 0.0'/
         DATA rgb_knot(300) /'255 0.5019608 0.0 0.0'/
! Woodward LowZAGB-Entropy-2.lut
      DATA alpha_knot(302) /'0 0.0'/
      DATA alpha_knot(303) /'18 0.1058824'/
      DATA alpha_knot(304) /'97 0.1294118'/
      DATA alpha_knot(305) /'131 0.2588235'/
      DATA alpha_knot(306) /'157 0.2156863'/
      DATA alpha_knot(307) /'165 0.0'/
      DATA alpha_knot(308) /'171 0.3803922'/
      DATA alpha_knot(309) /'184 0.5490196'/
      DATA alpha_knot(310) /'203 0.454902'/
      DATA alpha_knot(311) /'255 0.1686275'/
         DATA rgb_knot(302) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(303) /'18 0.0 0.0 0.2509804'/
         DATA rgb_knot(304) /'151 0.0 0.2352941 0.627451'/
         DATA rgb_knot(305) /'155 0.0 0.7843137 1.0'/
         DATA rgb_knot(306) /'159 1.0 1.0 1.0'/
         DATA rgb_knot(307) /'162 1.0 1.0 0.0'/
         DATA rgb_knot(308) /'166 1.0 0.0 0.0'/
         DATA rgb_knot(309) /'231 0.5019608 0.0 0.0'/
         DATA rgb_knot(310) /'255 0.5019608 0.0 0.0'/
! Woodward PS2-jelly-fish-2.lut
      DATA alpha_knot(312) /'0 0.0'/
      DATA alpha_knot(313) /'36 0.121568600'/
      DATA alpha_knot(314) /'72 0.274509800'/
      DATA alpha_knot(315) /'105 0.784313700'/
      DATA alpha_knot(316) /'133 1.0'/
      DATA alpha_knot(317) /'158 1.0'/
      DATA alpha_knot(318) /'196 0.5490196'/
      DATA alpha_knot(319) /'236 0.5137255'/
      DATA alpha_knot(320) /'244 0.2'/
      DATA alpha_knot(321) /'250 0.0'/
      DATA alpha_knot(322) /'255 0.0'/
         DATA rgb_knot(312) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(313) /'36 0.0 0.0 0.2509804'/
         DATA rgb_knot(314) /'71 0.0 0.1176471 0.3137255'/
         DATA rgb_knot(315) /'105 0.0 0.7843137 1.0'/
         DATA rgb_knot(316) /'131 1.0 1.0 1.0'/
         DATA rgb_knot(317) /'158 1.0 1.0 0.0'/
         DATA rgb_knot(318) /'196 1.0 0.0 0.0'/
         DATA rgb_knot(319) /'244 0.5019608 0.0 0.0'/
         DATA rgb_knot(320) /'255 0.5019608 0.0 0.0'/
! Woodward Sakurai-vort-3.lut
      DATA alpha_knot(323) /'0 0.0'/
      DATA alpha_knot(324) /'18 0.1058824'/
      DATA alpha_knot(325) /'65 0.2745098'/
      DATA alpha_knot(326) /'115 0.7843137'/
      DATA alpha_knot(327) /'144 1.0'/
      DATA alpha_knot(328) /'188 1.0'/
      DATA alpha_knot(329) /'210 0.5490196'/
      DATA alpha_knot(330) /'232 0.454902'/
      DATA alpha_knot(331) /'255 0.1686275'/
         DATA rgb_knot(323) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(324) /'103 0.0 0.0 0.2509804'/
         DATA rgb_knot(325) /'132 0.0 0.2352941 0.627451'/
         DATA rgb_knot(326) /'155 0.0 0.7843137 1.0'/
         DATA rgb_knot(327) /'171 1.0 1.0 1.0'/
         DATA rgb_knot(328) /'179 1.0 1.0 0.0'/
         DATA rgb_knot(329) /'187 1.0 0.0 0.0'/
         DATA rgb_knot(330) /'248 0.5019608 0.0 0.0'/
         DATA rgb_knot(331) /'255 0.5019608 0.0 0.0'/
! Woodward LogFV.lut for srend
      DATA alpha_knot(341) /'0 0.0'/
      DATA alpha_knot(342) /'15 0.00558824'/
      DATA alpha_knot(343) /'96 0.3745098'/
      DATA alpha_knot(344) /'115 0.5843137'/
      DATA alpha_knot(345) /'133 0.7'/
      DATA alpha_knot(346) /'158 0.7'/
      DATA alpha_knot(347) /'184 0.5490196'/
      DATA alpha_knot(348) /'203 0.454902'/
      DATA alpha_knot(349) /'254 0.1686275'/
      DATA alpha_knot(350) /'255 0.1254902'/
         DATA rgb_knot(341) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(342) /'18 0.0 0.0 0.2509804'/
         DATA rgb_knot(343) /'77 0.0 0.2352941 0.627451'/
         DATA rgb_knot(344) /'108 0.0 0.7843137 1.0'/
         DATA rgb_knot(345) /'131 1.0 1.0 1.0'/
         DATA rgb_knot(346) /'158 1.0 1.0 0.0'/
         DATA rgb_knot(347) /'196 1.0 0.0 0.0'/
         DATA rgb_knot(348) /'244 0.5019608 0.0 0.0'/
         DATA rgb_knot(349) /'255 0.5019608 0.0 0.0'/
! Woodward BW-1536-Enuc-4.lut
      DATA alpha_knot(351) /'0 0.0'/
      DATA alpha_knot(352) /'18 0.02745098'/
      DATA alpha_knot(353) /'34 0.1294118'/
      DATA alpha_knot(354) /'54 0.1058824'/
      DATA alpha_knot(355) /'66 0.2156863'/
      DATA alpha_knot(356) /'75 0.2627451'/
      DATA alpha_knot(357) /'86 0.5490196'/
      DATA alpha_knot(358) /'203 0.454902'/
      DATA alpha_knot(359) /'254 0.1686275'/
      DATA alpha_knot(360) /'255 0.1254902'/
         DATA rgb_knot(351) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(352) /'14 0.0 0.0 0.2509804'/
         DATA rgb_knot(353) /'22 0.3137255 0.0 0.627451'/
         DATA rgb_knot(354) /'35 1.0 0.0 0.0'/
         DATA rgb_knot(355) /'61 1.0 1.0 0.0'/
         DATA rgb_knot(356) /'74 1.0 1.0 1.0'/
         DATA rgb_knot(357) /'89 0.7529412 0.2509804 0.2509804'/
         DATA rgb_knot(358) /'108 0.3921569 0.0 0.0'/
         DATA rgb_knot(359) /'255 0.5019608 0.0 0.0'/
! Woodward grayscale.lut
      DATA alpha_knot(361) /'0 0.0'/
      DATA alpha_knot(362) /'255 1.0'/
         DATA rgb_knot(361) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(362) /'255 1.0 1.0 1.0'/
! Woodward signed-for-testing.lut
      DATA alpha_knot(371) /'0 1.0'/
      DATA alpha_knot(372) /'36 1.0'/
      DATA alpha_knot(373) /'64 0.3372549'/
      DATA alpha_knot(374) /'91 0.1137255'/
      DATA alpha_knot(375) /'128 0.05882353'/
      DATA alpha_knot(376) /'173 0.1372549'/
      DATA alpha_knot(377) /'220 0.5450981'/
      DATA alpha_knot(378) /'240 1.0'/
      DATA alpha_knot(379) /'255 1.0'/
         DATA rgb_knot(371) /'0 1.0 1.0 1.0'/
         DATA rgb_knot(372) /'35 0.0 1.0 1.0'/
         DATA rgb_knot(373) /'63 0.0 0.0 1.0'/
         DATA rgb_knot(374) /'92 0.0 0.0 0.5019608'/
         DATA rgb_knot(375) /'128 0.0 0.0 0.0'/
         DATA rgb_knot(376) /'144 0.4156863 0.3568628 0.3568628'/
         DATA rgb_knot(377) /'174 1.0 0.0 0.0'/
         DATA rgb_knot(378) /'219 1.0 0.9 0.0'/
         DATA rgb_knot(379) /'250 1.0 0.99 0.0'/
         DATA rgb_knot(380) /'255 1.0 1.0 0.0'/
! Woodward posdef-for-testing.lut    classic Vort colors.
      DATA alpha_knot(381) /'0 0.0'/
      DATA alpha_knot(382) /'8 0.03137255'/
      DATA alpha_knot(383) /'20 0.0627451'/
      DATA alpha_knot(384) /'32 0.7843137'/
      DATA alpha_knot(385) /'133 1.0'/
      DATA alpha_knot(386) /'153 0.8941177'/
      DATA alpha_knot(387) /'197 0.2431373'/
      DATA alpha_knot(388) /'250 0.2588235'/
      DATA alpha_knot(389) /'255 0.0'/
         DATA rgb_knot(381) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(382) /'24 0.0 0.0 0.3921569'/
         DATA rgb_knot(383) /'41 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(384) /'81 0.0 1.0 1.0'/
         DATA rgb_knot(385) /'115 1.0 1.0 1.0'/
         DATA rgb_knot(386) /'153 1.0 1.0 0.0'/
         DATA rgb_knot(387) /'197 1.0 0.0 0.0'/
         DATA rgb_knot(388) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(389) /'255 0.1 0.0 0.0'/
! Woodward inverted-signed-for-testing.lut
      DATA alpha_knot(391) /'0 1.0'/
      DATA alpha_knot(392) /'36 1.0'/
      DATA alpha_knot(393) /'64 0.3372549'/
      DATA alpha_knot(394) /'91 0.1137255'/
      DATA alpha_knot(395) /'128 0.05882353'/
      DATA alpha_knot(396) /'173 0.1372549'/
      DATA alpha_knot(397) /'220 0.5450981'/
      DATA alpha_knot(398) /'240 1.0'/
      DATA alpha_knot(399) /'255 1.0'/
         DATA rgb_knot(391) /'0 1.0 1.0 0.0'/
         DATA rgb_knot(392) /'35 1.0 0.9 0.0'/
         DATA rgb_knot(393) /'63 1.0 0.0 0.0'/
         DATA rgb_knot(394) /'92 0.4156863 0.3568628 0.3568628'/
         DATA rgb_knot(395) /'128 0.0 0.0 0.0'/
         DATA rgb_knot(396) /'144 0.0 0.0 0.5019608'/
         DATA rgb_knot(397) /'174 0.0 0.0 1.0'/
         DATA rgb_knot(398) /'219 0.0 1.0 1.0'/
         DATA rgb_knot(399) /'250 0.99 1.0 1.0'/
         DATA rgb_knot(400) /'255 1.0 1.0 1.0'/
! Woodward posdef-for-testing.lut  classic Vort w colors squeezed up.
      DATA alpha_knot(401) /'0 0.0'/
      DATA alpha_knot(402) /'8 0.03137255'/
      DATA alpha_knot(403) /'30 0.0627451'/
      DATA alpha_knot(404) /'160 0.7843137'/
      DATA alpha_knot(405) /'180 1.0'/
      DATA alpha_knot(406) /'200 0.8941177'/
      DATA alpha_knot(407) /'228 0.2431373'/
      DATA alpha_knot(408) /'250 0.2588235'/
      DATA alpha_knot(409) /'255 0.0'/
         DATA rgb_knot(401) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(402) /'40 0.0 0.0 0.3921569'/
         DATA rgb_knot(403) /'80 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(404) /'160 0.0 1.0 1.0'/
         DATA rgb_knot(405) /'180 1.0 1.0 1.0'/
         DATA rgb_knot(406) /'200 1.0 1.0 0.0'/
         DATA rgb_knot(407) /'228 1.0 0.0 0.0'/
         DATA rgb_knot(408) /'248 0.2509804 0.0 0.0'/
         DATA rgb_knot(409) /'255 0.1 0.0 0.0'/
! Woodward posdef-for-testing.lut  classic Vort w colors ssqueezed up.
      DATA alpha_knot(411) /'0 0.0'/
      DATA alpha_knot(412) /'8 0.03137255'/
      DATA alpha_knot(413) /'100 0.0627451'/
      DATA alpha_knot(414) /'180 0.7843137'/
      DATA alpha_knot(415) /'210 1.0'/
      DATA alpha_knot(416) /'230 0.8941177'/
      DATA alpha_knot(417) /'240 0.2431373'/
      DATA alpha_knot(418) /'250 0.2588235'/
      DATA alpha_knot(419) /'255 0.0'/
         DATA rgb_knot(411) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(412) /'100 0.0 0.0 0.3921569'/
         DATA rgb_knot(413) /'160 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(414) /'180 0.0 1.0 1.0'/
         DATA rgb_knot(415) /'210 1.0 1.0 1.0'/
         DATA rgb_knot(416) /'230 1.0 1.0 0.0'/
         DATA rgb_knot(417) /'240 1.0 0.0 0.0'/
         DATA rgb_knot(418) /'250 0.2509804 0.0 0.0'/
         DATA rgb_knot(419) /'255 0.1 0.0 0.0'/
! Woodward posdef-for-testing.lut  classic Vort w colors squeezed down.
      DATA alpha_knot(421) /'0 0.0'/
      DATA alpha_knot(422) /'4 0.03137255'/
      DATA alpha_knot(423) /'10 0.0627451'/
      DATA alpha_knot(424) /'16 0.7843137'/
      DATA alpha_knot(425) /'80 1.0'/
      DATA alpha_knot(426) /'100 0.8941177'/
      DATA alpha_knot(427) /'197 0.2431373'/
      DATA alpha_knot(428) /'250 0.2588235'/
      DATA alpha_knot(429) /'255 0.0'/
         DATA rgb_knot(421) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(422) /'12 0.0 0.0 0.3921569'/
         DATA rgb_knot(423) /'21 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(424) /'41 0.0 1.0 1.0'/
         DATA rgb_knot(425) /'65 1.0 1.0 1.0'/
         DATA rgb_knot(426) /'100 1.0 1.0 0.0'/
         DATA rgb_knot(427) /'197 1.0 0.0 0.0'/
         DATA rgb_knot(428) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(429) /'255 0.1 0.0 0.0'/
! Woodward LogFV-revd.lut ------------------------------------------------------------------------
      DATA alpha_knot(431) /'  0 0.0      '/ , rgb_knot(431) /'  0 0.0       0.0       0.0      '/
      DATA alpha_knot(432) /' 18 0.1058824'/
      DATA                                     rgb_knot(432) /' 38 0.0       0.0       0.2509804'/
      DATA alpha_knot(433) /' 56 0.2745098'/
      DATA                                     rgb_knot(433) /' 60 0.0       0.2352941 0.627451 '/
      DATA                                     rgb_knot(434) /' 78 0.0       0.7843137 1.0      '/
      DATA alpha_knot(434) /' 95 0.7843137'/
      DATA                                     rgb_knot(435) /'101 1.0       1.0       1.0      '/
      DATA alpha_knot(435) /'123 1.0      '/
      DATA                                     rgb_knot(436) /'128 1.0       1.0       0.0      '/
      DATA alpha_knot(436) /'158 1.0      '/
      DATA alpha_knot(437) /'184 0.5490196'/
      DATA                                     rgb_knot(437) /'196 1.0       0.0       0.0      '/
      DATA alpha_knot(438) /'203 0.454902 '/
      DATA                                     rgb_knot(438) /'244 0.5019608 0.0       0.0      '/
      DATA alpha_knot(439) /'255 0.1254902'/ , rgb_knot(439) /'255 0.5019608 0.0       0.0      '/

! Woodward LogFV-revd2.lut -----------------------------------------------------------------------
      DATA alpha_knot(441) /'  0 0.0      '/ , rgb_knot(441) /'  0 0.0       0.0       0.0      '/
      DATA alpha_knot(442) /' 18 0.1058824'/
      DATA                                     rgb_knot(442) /' 48 0.0       0.0       0.2509804'/
      DATA alpha_knot(443) /' 56 0.2745098'/ , rgb_knot(443) /' 56 0.0       0.2352941 0.627451 '/
      DATA                                     rgb_knot(444) /' 65 0.0       0.7843137 1.0      '/
      DATA alpha_knot(444) /' 75 0.7843137'/ , rgb_knot(445) /' 75 1.0       1.0       1.0      '/
      DATA                                     rgb_knot(446) /'100 1.0       1.0       0.0      '/
      DATA alpha_knot(445) /'123 1.0      '/
      DATA alpha_knot(446) /'158 1.0      '/
      DATA alpha_knot(447) /'184 0.5490196'/
      DATA                                     rgb_knot(447) /'186 1.0       0.0       0.0      '/
      DATA alpha_knot(448) /'203 0.454902 '/
      DATA                                     rgb_knot(448) /'244 0.5019608 0.0       0.0      '/
      DATA alpha_knot(449) /'255 0.1254902'/ , rgb_knot(449) /'255 0.5019608 0.0       0.0      '/

! Wetherbee : mid2high spike -----------------------------------------------
      DATA alpha_knot(450) /'  0 0.0  '/ , rgb_knot(450) /'  0 1.0 0.0 0.0'/
      DATA alpha_knot(451) /'128 0.001'/ , rgb_knot(451) /'128 0.0 0.1 0.0'/
      DATA alpha_knot(452) /'200 0.02 '/
      DATA alpha_knot(453) /'230 0.04 '/
      DATA alpha_knot(454) /'255 1.0  '/ , rgb_knot(452) /'255 0.5 0.5 1.0'/

! wetherbee : binvox fluid in solid & fluid mixed rendering test -----------
      DATA alpha_knot(460)  /'  0 0.0'/  , rgb_knot(460) /'  0 1.0 1.0 1.0'/
      DATA alpha_knot(461)  /'255 1.0'/  , rgb_knot(461) /'255 1.0 1.0 1.0'/

! wetherbee : binvox fluid in solid & fluid mixed rendering test, reddish fluid
      DATA alpha_knot(462)  /'  0 0.0'/  , rgb_knot(462) /'  0 1.0 0.1 0.1'/
      DATA alpha_knot(463)  /'255 1.0'/  , rgb_knot(463) /'255 1.0 0.2 0.2'/

! wetherbee : FM nice for vorticity
      DATA alpha_knot(470) /'  0 0.0  '/ , rgb_knot(470) /'  0 0.0 0.0 0.0'/
      DATA alpha_knot(471) /' 32 0.0  '/ , rgb_knot(471) /' 32 0.0 0.0 0.0'/
      DATA alpha_knot(472) /' 40 0.0  '/ , rgb_knot(472) /' 40 1.0 0.3 0.3'/
      DATA alpha_knot(473) /' 48 0.0  '/ , rgb_knot(473) /' 48 0.0 0.0 0.0'/
      DATA alpha_knot(474) /' 92 0.03  '/ , rgb_knot(474) /' 92 1.0 0.0 0.0'/
      DATA alpha_knot(475) /'100 0.6  '/ , rgb_knot(475) /'100 1.0 1.0 1.0'/
      DATA alpha_knot(476) /'108 0.03  '/ , rgb_knot(476) /'108 0.0 0.0 1.0'/
      DATA alpha_knot(477) /'182 0.0  '/ , rgb_knot(477) /'182 0.0 0.0 0.0'/
      DATA alpha_knot(478) /'210 0.0  '/ , rgb_knot(478) /'210 0.3 1.0 0.3'/
      DATA alpha_knot(479) /'238 0.0  '/ , rgb_knot(479) /'238 0.0 0.0 0.0'/
      DATA alpha_knot(480) /'255 0.0  '/ , rgb_knot(480) /'255 0.0 0.0 0.0'/

! wetherbee : FM rho
      DATA alpha_knot(490) /'  0 0.0  '/ , rgb_knot(490) /'  0 0.0 0.0 0.0'/
      DATA alpha_knot(491) /' 28 0.0  '/ , rgb_knot(491) /' 28 0.0 0.0 0.0'/
      DATA alpha_knot(492) /' 32 0.9  '/ , rgb_knot(492) /' 32 1.0 0.0 0.0'/
      DATA alpha_knot(493) /' 36 0.0  '/ , rgb_knot(493) /' 36 0.0 0.0 0.0'/
      DATA alpha_knot(494) /' 60 0.0  '/ , rgb_knot(494) /' 60 0.0 0.0 0.0'/
      DATA alpha_knot(495) /' 64 0.9  '/ , rgb_knot(495) /' 64 0.0 1.0 0.0'/
      DATA alpha_knot(496) /' 68 0.0  '/ , rgb_knot(496) /' 68 0.0 0.0 0.0'/
      DATA alpha_knot(497) /' 92 0.0  '/ , rgb_knot(497) /' 92 0.0 0.0 0.0'/
      DATA alpha_knot(498) /' 96 0.9  '/ , rgb_knot(498) /' 96 0.0 0.0 1.0'/
      DATA alpha_knot(499) /'100 0.0  '/ , rgb_knot(499) /'100 0.0 0.0 0.0'/
      DATA alpha_knot(500) /'124 0.0  '/ , rgb_knot(500) /'124 0.0 0.0 0.0'/
      DATA alpha_knot(501) /'128 0.9  '/ , rgb_knot(501) /'128 1.0 1.0 0.0'/
      DATA alpha_knot(502) /'132 0.0  '/ , rgb_knot(502) /'132 0.0 0.0 0.0'/
      DATA alpha_knot(503) /'156 0.0  '/ , rgb_knot(503) /'156 0.0 0.0 0.0'/
      DATA alpha_knot(504) /'160 0.9  '/ , rgb_knot(504) /'160 1.0 0.0 1.0'/
      DATA alpha_knot(505) /'164 0.0  '/ , rgb_knot(505) /'164 0.0 0.0 0.0'/
      DATA alpha_knot(506) /'188 0.0  '/ , rgb_knot(506) /'188 0.0 0.0 0.0'/
      DATA alpha_knot(507) /'192 0.9  '/ , rgb_knot(507) /'192 0.0 1.0 1.0'/
      DATA alpha_knot(508) /'196 0.0  '/ , rgb_knot(508) /'196 0.0 0.0 0.0'/
      DATA alpha_knot(509) /'220 0.0  '/ , rgb_knot(509) /'220 0.0 0.0 0.0'/
      DATA alpha_knot(510) /'224 0.9  '/ , rgb_knot(510) /'224 1.0 0.3 0.3'/
      DATA alpha_knot(511) /'228 0.0  '/ , rgb_knot(511) /'228 0.0 0.0 0.0'/
      DATA alpha_knot(512) /'236 0.0  '/ , rgb_knot(512) /'236 0.0 0.0 0.0'/
      DATA alpha_knot(513) /'240 0.9  '/ , rgb_knot(513) /'240 0.3 0.3 1.0'/
      DATA alpha_knot(514) /'244 0.0  '/ , rgb_knot(514) /'244 0.0 0.0 0.0'/
      DATA alpha_knot(515) /'255 0.0  '/ , rgb_knot(515) /'255 0.0 0.0 0.0'/

!wetherbee : FM rho continuous explore surface
      DATA alpha_knot(520) /'  0 0.3  '/ , rgb_knot(520) /'  0 0.1 0.1 0.1'/
      DATA alpha_knot(521) /' 28 0.5  '/ , rgb_knot(521) /' 28 0.2 0.2 0.2'/
      DATA alpha_knot(522) /' 32 0.9  '/ , rgb_knot(522) /' 32 1.0 0.0 0.0'/
      DATA alpha_knot(523) /' 36 0.5  '/ , rgb_knot(523) /' 36 0.5 0.0 0.0'/
      DATA alpha_knot(524) /' 60 0.5  '/ , rgb_knot(524) /' 60 0.0 0.5 0.0'/
      DATA alpha_knot(525) /' 64 0.9  '/ , rgb_knot(525) /' 64 0.0 1.0 0.0'/
      DATA alpha_knot(526) /' 68 0.5  '/ , rgb_knot(526) /' 68 0.0 0.5 0.0'/
      DATA alpha_knot(527) /' 92 0.5  '/ , rgb_knot(527) /' 92 0.0 0.0 0.5'/
      DATA alpha_knot(528) /' 96 0.9  '/ , rgb_knot(528) /' 96 0.0 0.0 1.0'/
      DATA alpha_knot(529) /'100 0.5  '/ , rgb_knot(529) /'100 0.0 0.0 0.5'/
      DATA alpha_knot(530) /'124 0.5  '/ , rgb_knot(530) /'124 0.5 0.5 0.0'/
      DATA alpha_knot(531) /'128 0.9  '/ , rgb_knot(531) /'128 1.0 1.0 0.0'/
      DATA alpha_knot(532) /'132 0.5  '/ , rgb_knot(532) /'132 0.5 0.5 0.0'/
      DATA alpha_knot(533) /'156 0.5  '/ , rgb_knot(533) /'156 0.5 0.0 0.5'/
      DATA alpha_knot(534) /'160 0.9  '/ , rgb_knot(534) /'160 1.0 0.0 1.0'/
      DATA alpha_knot(535) /'164 0.5  '/ , rgb_knot(535) /'164 0.5 0.0 0.5'/
      DATA alpha_knot(536) /'188 0.5  '/ , rgb_knot(536) /'188 0.0 0.5 0.5'/
      DATA alpha_knot(537) /'192 0.9  '/ , rgb_knot(537) /'192 0.0 1.0 1.0'/
      DATA alpha_knot(538) /'196 0.5  '/ , rgb_knot(538) /'196 0.0 0.5 0.5'/
      DATA alpha_knot(539) /'220 0.5  '/ , rgb_knot(539) /'220 0.5 0.1 0.1'/
      DATA alpha_knot(540) /'224 0.9  '/ , rgb_knot(540) /'224 1.0 0.3 0.3'/
      DATA alpha_knot(541) /'228 0.5  '/ , rgb_knot(541) /'228 0.5 0.1 0.1'/
      DATA alpha_knot(542) /'236 0.5  '/ , rgb_knot(542) /'236 0.1 0.1 0.5'/
      DATA alpha_knot(543) /'240 0.9  '/ , rgb_knot(543) /'240 0.3 0.3 1.0'/
      DATA alpha_knot(544) /'244 0.5  '/ , rgb_knot(544) /'244 0.5 0.5 0.5'/
      DATA alpha_knot(545) /'255 0.5  '/ , rgb_knot(545) /'255 1.0 1.0 1.0'/
! Woodward posdef-for-testing.lut    classic Vort colors.
! This is a revision that brings the red colors into play earlier and
! that reduces the opacity of the white and aqua colors somewhat.
! This revision was made for the H core conv w rotation at 1.0 x.
      DATA alpha_knot(551) /'0 0.0'/
      DATA alpha_knot(552) /'8 0.03137255'/
      DATA alpha_knot(553) /'20 0.0627451'/
      DATA alpha_knot(554) /'62 0.7843137'/
      DATA alpha_knot(555) /'133 1.0'/
      DATA alpha_knot(556) /'153 0.8941177'/
      DATA alpha_knot(557) /'197 0.2431373'/
      DATA alpha_knot(558) /'250 0.2588235'/
      DATA alpha_knot(559) /'255 0.0'/
         DATA rgb_knot(551) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(552) /'50 0.0 0.0 0.3921569'/
         DATA rgb_knot(553) /'81 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(554) /'121 0.0 1.0 1.0'/
         DATA rgb_knot(555) /'137 1.0 1.0 1.0'/
         DATA rgb_knot(556) /'145 1.0 1.0 0.0'/
         DATA rgb_knot(557) /'152 1.0 0.0 0.0'/
         DATA rgb_knot(558) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(559) /'255 0.1 0.0 0.0'/
! Woodward posdef-for-testing.lut    classic Vort colors.
! This is a revision that brings the red colors into play earlier and
! that reduces the opacity of the white and aqua colors somewhat.
! This revision was made for the H core conv w rotation at 1.0 x.
      DATA alpha_knot(561) /'0 0.0'/
      DATA alpha_knot(562) /'8 0.03137255'/
      DATA alpha_knot(563) /'20 0.0627451'/
      DATA alpha_knot(564) /'62 0.7843137'/
      DATA alpha_knot(565) /'133 1.0'/
      DATA alpha_knot(566) /'153 0.8941177'/
      DATA alpha_knot(567) /'197 0.2431373'/
      DATA alpha_knot(568) /'250 0.2588235'/
      DATA alpha_knot(569) /'255 0.0'/
         DATA rgb_knot(561) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(562) /'60 0.0 0.0 0.3921569'/
         DATA rgb_knot(563) /'81 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(564) /'101 0.0 1.0 1.0'/
         DATA rgb_knot(565) /'130 1.0 1.0 1.0'/
         DATA rgb_knot(566) /'134 1.0 1.0 0.0'/
         DATA rgb_knot(567) /'138 1.0 0.0 0.0'/
         DATA rgb_knot(568) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(569) /'255 0.1 0.0 0.0'/
! Woodward posdef-for-testing.lut    classic Vort colors.
! This is a revision that brings the red colors into play earlier and
! that reduces the opacity of the white and aqua colors somewhat.
! This revision was made for the H core conv w rotation at 1.0 x.
      DATA alpha_knot(571) /'0 0.0'/
      DATA alpha_knot(572) /'8 0.03137255'/
      DATA alpha_knot(573) /'20 0.0627451'/
      DATA alpha_knot(574) /'62 0.7843137'/
      DATA alpha_knot(575) /'133 1.0'/
      DATA alpha_knot(576) /'153 0.4941177'/
      DATA alpha_knot(577) /'167 0.8931373'/
      DATA alpha_knot(578) /'250 0.2588235'/
      DATA alpha_knot(579) /'255 0.0'/
         DATA rgb_knot(571) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(572) /'60 0.0 0.0 0.3921569'/
         DATA rgb_knot(573) /'81 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(574) /'101 0.0 1.0 1.0'/
         DATA rgb_knot(575) /'133 1.0 1.0 1.0'/
         DATA rgb_knot(576) /'135 1.0 1.0 0.0'/
         DATA rgb_knot(577) /'136 1.0 0.0 0.0'/
         DATA rgb_knot(578) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(579) /'255 0.1 0.0 0.0'/
! Woodward posdef-for-testing.lut  classic Vort w colors squeezed down.
      DATA alpha_knot(581) /'0 0.0'/
      DATA alpha_knot(582) /'4 0.03137255'/
      DATA alpha_knot(583) /'10 0.0627451'/
      DATA alpha_knot(584) /'16 0.4843137'/
      DATA alpha_knot(585) /'80 0.6'/
      DATA alpha_knot(586) /'100 0.4941177'/
      DATA alpha_knot(587) /'120 0.2431373'/
      DATA alpha_knot(588) /'250 0.2588235'/
      DATA alpha_knot(589) /'255 0.0'/
         DATA rgb_knot(581) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(582) /'12 0.0 0.0 0.3921569'/
         DATA rgb_knot(583) /'21 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(584) /'41 0.0 1.0 1.0'/
         DATA rgb_knot(585) /'65 1.0 1.0 1.0'/
         DATA rgb_knot(586) /'100 1.0 1.0 0.0'/
         DATA rgb_knot(587) /'120 1.0 0.0 0.0'/
         DATA rgb_knot(588) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(589) /'255 0.1 0.0 0.0'/
! Woodward posdef-for-testing.lut  classic Vort, red squeezed down more.
      DATA alpha_knot(591) /'0 0.0'/
      DATA alpha_knot(592) /'4 0.03137255'/
      DATA alpha_knot(593) /'10 0.0627451'/
      DATA alpha_knot(594) /'16 0.4843137'/
      DATA alpha_knot(595) /'80 0.6'/
      DATA alpha_knot(596) /'100 0.4941177'/
      DATA alpha_knot(597) /'120 0.2431373'/
      DATA alpha_knot(598) /'250 0.2588235'/
      DATA alpha_knot(599) /'255 0.0'/
         DATA rgb_knot(591) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(592) /'12 0.0 0.0 0.3921569'/
         DATA rgb_knot(593) /'21 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(594) /'41 0.0 1.0 1.0'/
         DATA rgb_knot(595) /'65 1.0 1.0 1.0'/
         DATA rgb_knot(596) /'100 1.0 1.0 0.0'/
         DATA rgb_knot(597) /'110 1.0 0.0 0.0'/
         DATA rgb_knot(598) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(599) /'255 0.1 0.0 0.0'/
! Woodward posdef-for-testing.lut  classic Vort  squeezed way down.
! for big Frontera run 10/2019 Vort at early times.
      DATA alpha_knot(601) /'0 0.0'/
      DATA alpha_knot(602) /'2 0.03137255'/
      DATA alpha_knot(603) /'5 0.0627451'/
      DATA alpha_knot(604) /'8 0.4843137'/
      DATA alpha_knot(605) /'40 0.6'/
      DATA alpha_knot(606) /'50 0.4941177'/
      DATA alpha_knot(607) /'60 0.2431373'/
      DATA alpha_knot(608) /'250 0.2588235'/
      DATA alpha_knot(609) /'255 0.0'/
         DATA rgb_knot(601) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(602) /'6 0.0 0.0 0.3921569'/
         DATA rgb_knot(603) /'11 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(604) /'21 0.0 1.0 1.0'/
         DATA rgb_knot(605) /'35 1.0 1.0 1.0'/
         DATA rgb_knot(606) /'50 1.0 1.0 0.0'/
         DATA rgb_knot(607) /'60 1.0 0.0 0.0'/
         DATA rgb_knot(608) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(609) /'255 0.1 0.0 0.0'/
! Woodward posdef-for-testing.lut  classic Vort  squeezed way way down.
! for big Frontera run 10/2019 Vort at early times.
      DATA alpha_knot(611) /'0 0.0'/
      DATA alpha_knot(612) /'2 0.03137255'/
      DATA alpha_knot(613) /'5 0.0627451'/
      DATA alpha_knot(614) /'8 0.4843137'/
      DATA alpha_knot(615) /'40 0.6'/
      DATA alpha_knot(616) /'50 0.4941177'/
      DATA alpha_knot(617) /'60 0.2431373'/
      DATA alpha_knot(618) /'250 0.2588235'/
      DATA alpha_knot(619) /'255 0.0'/
         DATA rgb_knot(611) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(612) /'6 0.0 0.0 0.3921569'/
         DATA rgb_knot(613) /'11 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(614) /'21 0.0 1.0 1.0'/
         DATA rgb_knot(615) /'31 1.0 1.0 1.0'/
         DATA rgb_knot(616) /'40 1.0 1.0 0.0'/
         DATA rgb_knot(617) /'46 1.0 0.0 0.0'/
         DATA rgb_knot(618) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(619) /'255 0.1 0.0 0.0'/

! Woodward LogFV-revd3.lut ------- opacity of dark blue reduced ----------------------------------
      DATA alpha_knot(621) /'  0 0.0      '/ , rgb_knot(621) /'  0 0.0       0.0       0.0      '/
      DATA alpha_knot(622) /' 18 0.0808824'/
      DATA                                     rgb_knot(622) /' 48 0.0       0.0       0.2509804'/
      DATA alpha_knot(623) /' 56 0.2145098'/ , rgb_knot(623) /' 56 0.0       0.2352941 0.627451 '/
      DATA                                     rgb_knot(624) /' 65 0.0       0.7843137 1.0      '/
      DATA alpha_knot(624) /' 75 0.7843137'/ , rgb_knot(625) /' 75 1.0       1.0       1.0      '/
      DATA                                     rgb_knot(626) /'100 1.0       1.0       0.0      '/
      DATA alpha_knot(625) /'123 1.0      '/
      DATA alpha_knot(626) /'158 1.0      '/
      DATA alpha_knot(627) /'184 0.5490196'/
      DATA                                     rgb_knot(627) /'186 1.0       0.0       0.0      '/
      DATA alpha_knot(628) /'203 0.454902 '/
      DATA                                     rgb_knot(628) /'244 0.5019608 0.0       0.0      '/
      DATA alpha_knot(629) /'255 0.1254902'/ , rgb_knot(629) /'255 0.5019608 0.0       0.0      '/

! Woodward LogFV-revd3.lut ------- opacity of dark blue reduced ----------------------------------
      DATA alpha_knot(631) /'  0 0.0      '/ , rgb_knot(631) /'  0 0.0       0.0       0.0      '/
      DATA alpha_knot(632) /' 18 0.10     '/
      DATA                                     rgb_knot(632) /' 48 0.0       0.0       0.2509804'/
      DATA alpha_knot(633) /' 56 0.27     '/ , rgb_knot(633) /' 56 0.0       0.2352941 0.627451 '/
      DATA                                     rgb_knot(634) /' 65 0.0       0.7843137 1.0      '/
      DATA alpha_knot(634) /' 75 0.7843137'/ , rgb_knot(635) /' 75 1.0       1.0       1.0      '/
      DATA                                     rgb_knot(636) /'100 1.0       1.0       0.0      '/
      DATA alpha_knot(635) /'123 1.0      '/
      DATA alpha_knot(636) /'158 1.0      '/
      DATA alpha_knot(637) /'184 0.7490196'/
      DATA                                     rgb_knot(637) /'186 1.0       0.0       0.0      '/
      DATA alpha_knot(638) /'203 0.454902 '/
      DATA                                     rgb_knot(638) /'244 0.5019608 0.0       0.0      '/
      DATA alpha_knot(639) /'255 0.1254902'/ , rgb_knot(639) /'255 0.5019608 0.0       0.0      '/
! Woodward posdef-for-testing.lut  classic Vort colors squeezd down less
      DATA alpha_knot(641) /'0 0.0'/
      DATA alpha_knot(642) /'4 0.03137255'/
      DATA alpha_knot(643) /'10 0.0627451'/
      DATA alpha_knot(644) /'16 0.7843137'/
      DATA alpha_knot(645) /'80 1.0'/
      DATA alpha_knot(646) /'100 0.8941177'/
      DATA alpha_knot(647) /'197 0.2431373'/
      DATA alpha_knot(648) /'250 0.2588235'/
      DATA alpha_knot(649) /'255 0.0'/
         DATA rgb_knot(641) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(642) /'12 0.0 0.0 0.3921569'/
         DATA rgb_knot(643) /'36 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(644) /'61 0.0 1.0 1.0'/
         DATA rgb_knot(645) /'85 1.0 1.0 1.0'/
         DATA rgb_knot(646) /'120 1.0 1.0 0.0'/
         DATA rgb_knot(647) /'187 1.0 0.0 0.0'/
         DATA rgb_knot(648) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(649) /'255 0.1 0.0 0.0'/
! Woodward posdef-for-testing.lut  classic Vort colors squeezd down less
      DATA alpha_knot(651) /'0 0.0'/
      DATA alpha_knot(652) /'4 0.03137255'/
      DATA alpha_knot(653) /'10 0.0627451'/
      DATA alpha_knot(654) /'16 0.7843137'/
      DATA alpha_knot(655) /'70 0.7843137'/
      DATA alpha_knot(656) /'80 1.0'/
      DATA alpha_knot(657) /'100 0.8941177'/
      DATA alpha_knot(658) /'197 0.2431373'/
      DATA alpha_knot(659) /'250 0.2588235'/
      DATA alpha_knot(660) /'255 0.0'/
         DATA rgb_knot(651) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(652) /'12 0.0 0.0 0.3921569'/
         DATA rgb_knot(653) /'55 0.0 0.0 0.4921569'/
         DATA rgb_knot(654) /'65 0.0 0.8019608 0.8019608'/
         DATA rgb_knot(655) /'70 0.0 1.0 1.0'/
         DATA rgb_knot(656) /'85 1.0 1.0 1.0'/
         DATA rgb_knot(657) /'120 1.0 1.0 0.0'/
         DATA rgb_knot(658) /'137 1.0 0.0 0.0'/
         DATA rgb_knot(659) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(660) /'255 0.1 0.0 0.0'/
!
! BEGIN 10 TWEAKING COLOR TABLES.  701-799 ARE RESERVED ARRAY ELEMENTS:
! Woodward posdef-for-testing.lut  classic Vort  squeezed way down.
! for big Frontera run 10/2019 Vort at early times.
      DATA alpha_knot(701) /'0 0.0'/
      DATA alpha_knot(702) /'2 0.03137255'/
      DATA alpha_knot(703) /'5 0.0627451'/
      DATA alpha_knot(704) /'8 0.4843137'/
      DATA alpha_knot(705) /'40 0.6'/
      DATA alpha_knot(706) /'50 0.4941177'/
      DATA alpha_knot(707) /'60 0.2431373'/
      DATA alpha_knot(708) /'250 0.2588235'/
      DATA alpha_knot(709) /'255 0.0'/
         DATA rgb_knot(701) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(702) /'6 0.0 0.0 0.3921569'/
         DATA rgb_knot(703) /'11 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(704) /'21 0.0 1.0 1.0'/
         DATA rgb_knot(705) /'35 1.0 1.0 1.0'/
         DATA rgb_knot(706) /'50 1.0 1.0 0.0'/
         DATA rgb_knot(707) /'60 1.0 0.0 0.0'/
         DATA rgb_knot(708) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(709) /'255 0.1 0.0 0.0'/
! Woodward posdef-for-testing.lut  classic Vort w colors squeezed down.
      DATA alpha_knot(711) /'0 0.0'/
      DATA alpha_knot(712) /'4 0.03137255'/
      DATA alpha_knot(713) /'10 0.0627451'/
      DATA alpha_knot(714) /'16 0.7843137'/
      DATA alpha_knot(715) /'80 1.0'/
      DATA alpha_knot(716) /'100 0.8941177'/
      DATA alpha_knot(717) /'197 0.2431373'/
      DATA alpha_knot(718) /'250 0.2588235'/
      DATA alpha_knot(719) /'255 0.0'/
         DATA rgb_knot(711) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(712) /'12 0.0 0.0 0.3921569'/
         DATA rgb_knot(713) /'21 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(714) /'41 0.0 1.0 1.0'/
         DATA rgb_knot(715) /'65 1.0 1.0 1.0'/
         DATA rgb_knot(716) /'100 1.0 1.0 0.0'/
         DATA rgb_knot(717) /'197 1.0 0.0 0.0'/
         DATA rgb_knot(718) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(719) /'255 0.1 0.0 0.0'/
! Woodward C64-FV-6a-for-Vort-slice.lut
      DATA alpha_knot(721) /'0 0.0'/
      DATA alpha_knot(722) /'8 0.03137255'/
      DATA alpha_knot(723) /'20 0.0627451'/
      DATA alpha_knot(724) /'32 0.7843137'/
      DATA alpha_knot(725) /'133 1.0'/
      DATA alpha_knot(726) /'153 0.8941177'/
      DATA alpha_knot(727) /'197 0.2431373'/
      DATA alpha_knot(728) /'241 0.2588235'/
      DATA alpha_knot(729) /'255 0.0'/
         DATA rgb_knot(721) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(722) /'24 0.0 0.0 0.3921569'/
         DATA rgb_knot(723) /'41 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(724) /'81 0.0 1.0 1.0'/
         DATA rgb_knot(725) /'115 1.0 1.0 1.0'/
         DATA rgb_knot(726) /'153 1.0 1.0 0.0'/
         DATA rgb_knot(727) /'197 1.0 0.0 0.0'/
         DATA rgb_knot(728) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(729) /'255 0.0 0.0 0.0'/
! Woodward posdef-for-testing.lut    classic Vort colors.
! This is a revision that brings the red colors into play earlier and
! that reduces the opacity of the white and aqua colors somewhat.
! This revision was made for the H core conv w rotation at 1.0 x.
      DATA alpha_knot(731) /'0 0.0'/
      DATA alpha_knot(732) /'8 0.03137255'/
      DATA alpha_knot(733) /'20 0.0627451'/
      DATA alpha_knot(734) /'62 0.7843137'/
      DATA alpha_knot(735) /'133 1.0'/
      DATA alpha_knot(736) /'153 0.8941177'/
      DATA alpha_knot(737) /'197 0.2431373'/
      DATA alpha_knot(738) /'250 0.2588235'/
      DATA alpha_knot(739) /'255 0.0'/
         DATA rgb_knot(731) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(732) /'60 0.0 0.0 0.3921569'/
         DATA rgb_knot(733) /'81 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(734) /'101 0.0 1.0 1.0'/
         DATA rgb_knot(735) /'130 1.0 1.0 1.0'/
         DATA rgb_knot(736) /'134 1.0 1.0 0.0'/
         DATA rgb_knot(737) /'138 1.0 0.0 0.0'/
         DATA rgb_knot(738) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(739) /'255 0.1 0.0 0.0'/
! Woodward posdef-for-testing.lut    classic Vort colors.
! This is a revision that brings the red colors into play earlier and
! that reduces the opacity of the white and aqua colors somewhat.
! This revision was made for the H core conv w rotation at 1.0 x.
      DATA alpha_knot(741) /'0 0.0'/
      DATA alpha_knot(742) /'8 0.03137255'/
      DATA alpha_knot(743) /'20 0.0627451'/
      DATA alpha_knot(744) /'62 0.7843137'/
      DATA alpha_knot(745) /'133 1.0'/
      DATA alpha_knot(746) /'153 0.4941177'/
      DATA alpha_knot(747) /'167 0.8931373'/
      DATA alpha_knot(748) /'250 0.2588235'/
      DATA alpha_knot(749) /'255 0.0'/
         DATA rgb_knot(741) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(742) /'60 0.0 0.0 0.3921569'/
         DATA rgb_knot(743) /'81 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(744) /'101 0.0 1.0 1.0'/
         DATA rgb_knot(745) /'133 1.0 1.0 1.0'/
         DATA rgb_knot(746) /'135 1.0 1.0 0.0'/
         DATA rgb_knot(747) /'136 1.0 0.0 0.0'/
         DATA rgb_knot(748) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(749) /'255 0.1 0.0 0.0'/
! Woodward posdef-for-testing.lut    classic Vort colors.
! This is a revision that brings the red colors into play earlier and
! that reduces the opacity of the white and aqua colors somewhat.
! This revision was made for the H core conv w rotation at 1.0 x.
      DATA alpha_knot(751) /'0 0.0'/
      DATA alpha_knot(752) /'8 0.03137255'/
      DATA alpha_knot(753) /'20 0.0627451'/
      DATA alpha_knot(754) /'62 0.7843137'/
      DATA alpha_knot(755) /'133 1.0'/
      DATA alpha_knot(756) /'153 0.8941177'/
      DATA alpha_knot(757) /'197 0.2431373'/
      DATA alpha_knot(758) /'250 0.2588235'/
      DATA alpha_knot(759) /'255 0.0'/
         DATA rgb_knot(751) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(752) /'50 0.0 0.0 0.3921569'/
         DATA rgb_knot(753) /'81 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(754) /'121 0.0 1.0 1.0'/
         DATA rgb_knot(755) /'137 1.0 1.0 1.0'/
         DATA rgb_knot(756) /'145 1.0 1.0 0.0'/
         DATA rgb_knot(757) /'152 1.0 0.0 0.0'/
         DATA rgb_knot(758) /'238 0.2509804 0.0 0.0'/
         DATA rgb_knot(759) /'255 0.1 0.0 0.0'/
! Woodward demoSC08-FV-good-colors-for-tp3-density7-for-vort2.lut
      DATA alpha_knot(761) /'0 0.0'/
      DATA alpha_knot(762) /'18 0.1058824'/
      DATA alpha_knot(763) /'97 0.1294118'/
      DATA alpha_knot(764) /'130 0.1058824'/
      DATA alpha_knot(765) /'158 0.2156863'/
      DATA alpha_knot(766) /'171 0.3803922'/
      DATA alpha_knot(767) /'184 0.5490196'/
      DATA alpha_knot(768) /'203 0.454902'/
      DATA alpha_knot(769) /'254 0.1686275'/
      DATA alpha_knot(770) /'255 0.1254902'/
         DATA rgb_knot(761) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(762) /'129 0.0 0.0 0.2509804'/
         DATA rgb_knot(763) /'137 0.0 0.2352941 0.627451'/
         DATA rgb_knot(764) /'148 0.0 0.7843137 1.0'/
         DATA rgb_knot(765) /'159 1.0 1.0 1.0'/
         DATA rgb_knot(766) /'170 1.0 1.0 0.0'/
         DATA rgb_knot(767) /'207 1.0 0.0 0.0'/
         DATA rgb_knot(768) /'231 0.5019608 0.0 0.0'/
         DATA rgb_knot(769) /'255 0.5019608 0.0 0.0'/
! Woodward Sakurai-vort-3.lut
      DATA alpha_knot(771) /'0 0.0'/
      DATA alpha_knot(772) /'18 0.1058824'/
      DATA alpha_knot(773) /'65 0.2745098'/
      DATA alpha_knot(774) /'115 0.7843137'/
      DATA alpha_knot(775) /'144 1.0'/
      DATA alpha_knot(776) /'188 1.0'/
      DATA alpha_knot(777) /'210 0.5490196'/
      DATA alpha_knot(778) /'232 0.454902'/
      DATA alpha_knot(779) /'255 0.1686275'/
         DATA rgb_knot(771) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(772) /'103 0.0 0.0 0.2509804'/
         DATA rgb_knot(773) /'132 0.0 0.2352941 0.627451'/
         DATA rgb_knot(774) /'155 0.0 0.7843137 1.0'/
         DATA rgb_knot(775) /'171 1.0 1.0 1.0'/
         DATA rgb_knot(776) /'179 1.0 1.0 0.0'/
         DATA rgb_knot(777) /'187 1.0 0.0 0.0'/
         DATA rgb_knot(778) /'248 0.5019608 0.0 0.0'/
         DATA rgb_knot(779) /'255 0.5019608 0.0 0.0'/
! Woodward posdef-for-testing.lut  classic Vort w colors squeezed up.
      DATA alpha_knot(781) /'0 0.0'/
      DATA alpha_knot(782) /'8 0.03137255'/
      DATA alpha_knot(783) /'30 0.0627451'/
      DATA alpha_knot(784) /'160 0.7843137'/
      DATA alpha_knot(785) /'180 1.0'/
      DATA alpha_knot(786) /'200 0.8941177'/
      DATA alpha_knot(787) /'228 0.2431373'/
      DATA alpha_knot(788) /'250 0.2588235'/
      DATA alpha_knot(789) /'255 0.0'/
         DATA rgb_knot(781) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(782) /'40 0.0 0.0 0.3921569'/
         DATA rgb_knot(783) /'80 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(784) /'160 0.0 1.0 1.0'/
         DATA rgb_knot(785) /'180 1.0 1.0 1.0'/
         DATA rgb_knot(786) /'200 1.0 1.0 0.0'/
         DATA rgb_knot(787) /'228 1.0 0.0 0.0'/
         DATA rgb_knot(788) /'248 0.2509804 0.0 0.0'/
         DATA rgb_knot(789) /'255 0.1 0.0 0.0'/
! Woodward posdef-for-testing.lut  classic Vort w colors ssqueezed up.
      DATA alpha_knot(791) /'0 0.0'/
      DATA alpha_knot(792) /'8 0.03137255'/
      DATA alpha_knot(793) /'100 0.0627451'/
      DATA alpha_knot(794) /'180 0.7843137'/
      DATA alpha_knot(795) /'210 1.0'/
      DATA alpha_knot(796) /'230 0.8941177'/
      DATA alpha_knot(797) /'240 0.2431373'/
      DATA alpha_knot(798) /'250 0.2588235'/
      DATA alpha_knot(799) /'255 0.0'/
         DATA rgb_knot(791) /'0 0.0 0.0 0.0'/
         DATA rgb_knot(792) /'100 0.0 0.0 0.3921569'/
         DATA rgb_knot(793) /'160 0.0 0.5019608 0.5019608'/
         DATA rgb_knot(794) /'180 0.0 1.0 1.0'/
         DATA rgb_knot(795) /'210 1.0 1.0 1.0'/
         DATA rgb_knot(796) /'230 1.0 1.0 0.0'/
         DATA rgb_knot(797) /'240 1.0 0.0 0.0'/
         DATA rgb_knot(798) /'250 0.2509804 0.0 0.0'/
         DATA rgb_knot(799) /'255 0.1 0.0 0.0'/
! END 10 TWEAKING COLOR TABLES.  701-799 ARE RESERVED ARRAY ELEMENTS:
!
! ---- end: hardcoded section ----------------------------------------
