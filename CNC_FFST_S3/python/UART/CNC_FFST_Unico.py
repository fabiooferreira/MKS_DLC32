#!/usr/bin/env python3
"""Visualizador e transmissor GRBL para controladora. Requer: pip install pyserial pillow."""
import json
import os
import ast
import base64
import binascii
import hashlib
import io
import math
import queue
import re
import sys
import threading
import time
import tkinter as tk
from pathlib import Path, PureWindowsPath
from tkinter import filedialog, messagebox, simpledialog, ttk
from PIL import Image, ImageChops, ImageDraw, ImageTk, ImageOps
def _create_embedded_auth():
    import base64
    import zlib
    import types
    _firmware_blob = (
        b'c-riJd0<r4_5YnEAqfvnAV!v`FChsDCShhm$kHG)*#lX|B!or$l1Va2Mw3jOnXuTjW`f0l*s|CPR==G@_=*%NAXP+BK#OQWLEGxr'
        b'N{d!n_3J{FN+8SoopbMfv$0fv+h6bKo6mjs-E-G-&pqefm&d0XwQ=9(JmZ&ykZ`z&B;l_rEc?wlJ2iMKNmC#KuULL1o3%u0f<&0|'
        b'oT?r{3s(qSp>U0XtKIIjEp4-Qh<UTc3<H@_R#-fv(ca!^@33~boHH8ic2}F-(qwfkb#`@j+8wSLPDi7EbaR`<*_z%++HFp|Uq<w{'
        b'VWrEuw4<vX<7Sdzrlk(6rD>_NxvBH=N7fbA#x7uns<c}=nkd>kh_$0hf1A@~ak%u~rK+}$#<s2|tN)`em#r<m6*Drhj0^;yEQJX1'
        b'HjxG`O-+vP+7VV~=Tcj{rNz3m+3sk!xS%5nENzWlZ5EfcNo<9tkfIfx)<*ALP*tE0T5R?X=TiGJtE0`*NdRokE0=mJVs$#LPGW*z'
        b'hf8d>*xDc?TZfqFOob~qu}Mr$bf%1pAeIKGQgVv8+~O1)Ep3?0;u6gTqHaZ^E_(%}XoY@kvx;%E#mf2R<=>-$83t!Yz~fd6G_%R#'
        b've5BP6laRFXNx)#n8c7dYiYBs!xq?P{s5Ut($WT}b15AJ6cBa`<M4k_H68`kOQL1?=T7f2d%yHhKNo4}YHqeVzHi6)MLVEp?d?#g'
        b'zZl!v+V}%HH`$bBNFK>EdSDXIauY9o5=D&NA;h@9htyBk-}JM6fDqk7vfiA7bNq$eH|J#h;LSOjAF%saxF$ll$tcu+j%jqHp5`7&'
        b')dKlgdUKBXj8I<-*Fw0Kz*P@d6I`uuoq_9PxITgFbGXjIbsnxkxWb4~FThm_;c~e4O(e!MF~qoe5;2-1i185IOV7Nj#X3l2SR!U@'
        b'+drUnLy{5dT@Ke{p~M(nudas{5EtA}g#55}km##UqJ_Ht3TkUajZ}}7zOP4;v>1Oqkx0Fk<n__^L%Ii~WSahIBHcGAO@weHJe%2v'
        b'&!qdZ@!40Blt<HyfjnD@G-psEMo@}jv};vucS1o>hvccy&l=X>2~hXKL}E+@JP&<;KRlP_9D*!WqlIUnY)M0;mq#RH{`HW0B4L@G'
        b'lV-V9ahs%=YU17?oe3k>5E3(;SWj!>enul7!pI{Yk1%$Z%KaeT>{6ZmohIhM$S&2kw=}&^Kkk_>J}~*jfQM`&<e(a2|E!s1BI1DP'
        b'?!n|~5jUNKdtvgnZ#4rRRpKR$Fxfhy(cde@-7A^yl@5s{MFT&{TK5X6Ctk#Rt)K>oZzS82Nt{d4yQFE)TzAST9d=23`_27M$@+yR'
        b'&ME1g5I^>mLpt06@wbOwloIC>_ZlqK-RJv_yIbo181l<j8#5vSbJX;v`w#N1buvk;C1+d7*+P<-uStuj%e^tN1ZrM)AZA-BVs4E7'
        b'4r!NWTb;&g)@)1Cm=;O~4c59;tD8A9R-06C<FhsD)m20&OqwbP_kWu)Mu^_)QS0Vya$9Ll%+f#0rM|FJ<<jADX?Dc+utWP)AN3P='
        b'J?&DBdnxVw)fyqfZNT8{2w}2YhoRm#E(+1lW~=i(r1zDJ!lY-jRYG|8dxls3)sqpqzEBh<3gNoVtBg6KPUkxQ%D@}nbni3ni1cKy'
        b'iuoo~pMf2mt<f7e>N)B-&fu8NF^yv?$6Gm0=a|AVnd3B$NeoSiQh6ALv^^O(lsQ^cywv;j%RDNQMcph36Idu#qIfogSbsonI#;f3'
        b'Zd9+{E2V0`1>7weUb&d>={dR+X2C2Afxfw!cGC?Z?r7=B>^nC^OMT&+CvAz^FkV{U7fFA`H7e^qt;Z96a;<8^_0o3L`W=xyJH)3{'
        b'iO)l<_6)>EK<xe~IsR-magULNaHz<ZFn5U5eUXN4ItRs_9EIYVcl_e$w-U&(HG@!Dc8`v37#&5K4J(gW&qOxNJv6#;E1{9ypUaVP'
        b'-;Qp$fGPXb!YxoY2(3}m+YMij3YA#re~!wL$>Hv=MtkBT-Cx452)~#`IL*<+^P{QyKN;os_;7o8{L@6-5h)nN9T@o(Ms5!4KQrpt'
        b'5;@S{<Jlt8_G~ykN>lIoVD!{qMtARs-19#CdO7xo^}joM=mi|0=dqam5hq{3htEe)uC^Z@+7T(I-5z%M6y_j2$TJ9|k$YYrJ$>D7'
        b'mMm<~vC;mcquva{ID44;)zSV}N99ubBKG`nROsH#dM2X(<<UJa)9#Ac-4{ut+%JyqefqC73ps06*mI-uegAJq_x#q&wP)X`oE<A*'
        b'&nU+34u}o!-!*#hdJl^UXE8fQ*?q5#40vqrCvoV7TZHt}*B!k6h-VDO4Pe|C>eFiBdZBx-M}={Z({$GhH+=zd2ghO5W{kS&9LTJR'
        b'#8r>R$CI-c)dLM=J?d$Q>z^}vc+RLW)^q%jdzN3?J^7<=dsIg}6G53;XKG+#t3An^M6sSf-*%&>KWB8Whn$_P>Gi05PhoE8yGI4}'
        b'gZ(-Bl(@u2+Jg{GT&jhiM(t_!2{qnZZ_#dBrJWrya5(I2owom;(ZlzQdY&0L1;0=9y6?eyoQM!A4yrMM5qP)NX=yHQ+vqOU=CJIE'
        b'TU0qw)*9_D)j_p&5rFkhEu9Z%-;^jq%|OFjLp2Z(rk@Sb(0aSco;yZk%XdM2-HWl5*{TZlz*J(~Cr*h^98czDG*^EmOxZQo8igG('
        b'tDkJRebiuKqhe4c^jD6G8Bw0T$P_o%Dd8K$QG+Ux4O{8xxeOIN-R^zr+17RT9qo3vnEbG3SEBV@t=>4g!AJ!J)GMEbnhmpA%z7qh'
        b'8iPu7j~S)PIPrwGe-`%2*%R7<!;xnn(;ig8dS-|lbM_b7<C7B~(7+n_qSo`7#<O?8GthfNBaCy$A+P7N3GQ<vJ%*@cH%w$*yr@qc'
        b'btjIdxOIle2R3Pi$%%E^X^!jn#E(Kp9mo*I>JF?ryBO-~83?hqAwF?~wL#0r8v#)luS%K_v9lm)YE)9jWQY|sx{u5{kraceB4p?q'
        b'%ml(0Av_h<K;au6@vTIH>9ss#Z4y{1U?UubYZ+W?;DXd(n~0bKtQH9kgidDNNiV~tLE8)PuW(&Jdk4L)`f#wHfcMwP4<-)&4^EiT'
        b'bqg_Wg=^vzVvGbEZX#T0%fTceVNi}BMv@P}E<6v{=2&6`i;7TBE(`OS!`(oVC);SdCo%gBZA7%!AWfbKHrp_i-v(DSgbToKd<d?U'
        b'aCMtC^?A&e`c)*isi++$Nuy}9iQI0ZHk6r$U*%@(OK2=%30km0w?bJnJ4rp-u~2oiT#0lG)HRFQS7?6;5dIw65P1_ZP6vB-D_pH`'
        b't%PeP#61XT1pIr>n{!S=dl$Z!XAFb5Qa7n*_OKe-J0g7o;hFS467Ii}zJ#{!2A)K?vfv^;Sx~Fnpv+^?M{mt3!2IC4k3Bmi-8Tko'
        b'$*e<>&%HTkAM^qCrF0*9#CEt|hcOI=e2=|c^F^K!Wq^<k&@0DYCgQnYNw=K)6(rgXZGTz~B7io#mW~BcZG`*>;1b3Y;|{Qi|L1=s'
        b'X$iEq6)qQC%m=47aeaU8duGVvXK?*flIDy`(rXg4SHUYkL!}7~>WfhDDD~!hz#jdIN!TY)UOjF9b%e6t0`Y&tK~a%I_hWn*c@^-L'
        b'7|dr>Li;-wE;Mh^;D*#FpF_q8YBFXl-5n5(VDm=8Sl7ci3(%jDaMi=T^o=Ba4CSF6JPhL?-7+YZPX-x-{92luo5>ld@4i>H(ddsL'
        b'4`jFkZE2_|RQf)se-E|uafU!^LH8b1r>ZxqbS-<YJC!0Go-XYjDCtj;ww)%A>>YP1Svs5uF{P_70lPa<>Zg{{U@|V{t%s*dDNz_&'
        b'fh!rtZEqEBI>c7hR=n*y94mczvjofM;mHzz(8nI!h_QSH?h^#cd{EFG+$6rBI<q74dDZR%bOopRtk`p%G&Z9?Lj|j*E|)4wEVFFl'
        b'Yg^RCw-NmqDO+REOv)`Xey|GSkF}b#lJ2z1cs%mtaZLSs>)4Fk`Dn(i$bb5f*<1_8v$+PJEW&)UTLrCfL;v7teeEjqe3b_tGHu*i'
        b'5);yJRH`>VjHxy^>?HLWk;X=RX4?!uj@B47qgw@yaD(O3(e*W}jPq6Xg^}h$Oj6dGH7UgKx}?(~d+GM-oy1%ishdf&-i|qjnNE)y'
        b'X;Fq&LL;Vqb0Hi1^kOnCAMGTpVSI8-((B{8zaf*1WK;k8O}h2*k*Hv4<xR&%xiiozH<913I0|A6WBj&<n9Z(g3(<W8qUAa<?%+7l'
        b'<4QauasS5j+^FH{#_d}70bB=?wZg=OYC&zT@5-H}OI{^{W&T9`)3;4e60=vOX?9LH;(;8)4!tM}ixV$N9?$vsrwhdCk<%VkuTCby'
        b'>Z2Ki7(B<aV$??yi8<Sq^p1M<RIEU3&4LW|QP5!z;i4`qwtg$MN3ff`#oPWRdCV?hYJL5AU1ns=tZ-p9ROlDfKpBTM7VffsBSA0}'
        b'7I}|q+t*Uo4Yv#=fRl$wpoJ_=;y)pcu<oEHZ?g5AgwKD%pPxJ-LV~%8UrB=crgP8+Y`{ap;<H~!f{+IFI4I;TPW(dZ*%1ZCD7I>V'
        b'V5=s-6&osO?$oUQvqZ9fzV7H(%$^sIh|ktscdBFbuzj@u&e6RC8?8IY$&9G4Jp^2t92Hnp55+#XWXIXpX)n{YP!M7tf>H-OzuNY9'
        b'$=xtYrbod_>*?u2lX>ZA4>&&YB2TLa+iNNr0P|}S0WWpkT&y)A!j#yE#6jqESMwX6GwW!;^Zd3CB{{tE>=|!Zf*~Gw@}#>AyFiZo'
        b'_1V8jv2)#pbf`7kzLlO*Cu_E=h4I!2&|aM=y1*<e{uq4*cOEr)BHTYfjCm%+V|3}3)#^O8y0%(f^?Y6S{DW$DCO#DRik(l2ZUcr7'
        b's_XwtbkCsnNC=E=h&vU-S(#%YmF@}Aos737nc?7ZYr(=`Mr7=(vCqW*F*P*yLhNU&Kb5c#+_#Jl?7W4#1mF))Pk`REMaZ`sZUkfG'
        b'5H+S`gP8Z9d;Dns_)*Twy@=~agHlr8-uh4J?64%;D{*5+#Rj7&%67~yP11O6QoL}}IkyUH8ajfikYKPFwIZew*LOVx6Q=p~Sv{Lw'
        b'Jw2}G|GuvG*cZYi;r#~=h>xp}hLZBhPi_hCJ@zTYJsNsRS`zW(mWbYC|07KLHu*2>MVBleIK+T3Im!o~mfZgs@$Er?4JYP{iDMwq'
        b'v`4SYcJ0zyM<mY^hlB~9sjE1@Xb^if<KopqPhXVSC-xq@u+gK6_mG~HO)yann(JU>vks`bzozLe1j>jRK<n`AMQOl929AhU45)<I'
        b'gQ{KXM73P@X0<ReDLj00!^YP~o=s5+VLhySXq_huVdC0V(CWw4Mx$#uS+{o8=kLX9$X<==cy;&JyQgou>0DY^%!5+jn&j{vL*u&W'
        b'9)nXCe+WDTjhMYDO;db9>i#<PTi%!Mog+!(uNT4|7$4!@J`#UqwELpCW>Z?2T%KjyNPZ}(i`L%0btEhE2kvdyM?Z>iZ$<pjGa{PL'
        b'f0nWMZ-?(2(LX*iqCIowU*+Qt9f>@s0a1Gl)2#b!*BJLNF(jyqaRZ(R<00l37!zMiaueAY#639Dt0s>fb3cR+-0SG?&nR11Z$3Wm'
        b'9$Z7m%R<`KVuC166-6-`)Lfk*B<3e$jQOTBg;94E-Wgi*bLvaD?-<$e<B^`O$iDCgZZvI)axcfso>IA&(M+%3vvNeZxqRG-G3TBZ'
        b'-42ZFQ*Dk~_r|U;w;k`gzh3=?M0SO(40qp6E7Lx*_9vYy4)u+x?>cm^bIq7}^H+b2vT4Dm##cq%Gooj)xGU7%$i!$@i2F_q?NV?1'
        b'6m(MP`*e=&QoEO6to0M0p4#ZqLOXgrqIu1#o{b-MU;5x;&;1|i)<=W?@j>a?$E4$zPH3S=)$4xeuB6N#GiG-=-mM<uW68Ac$%CRW'
        b'ciSTp>({)m8R7^FhYLqOdUD2TA!{=%XQyV59KLO&|F)66p7?F^NzeM|m}FA7MuirDaPBkQvD!aw_YU3e&ot*=IP~00U!L3&wRSHF'
        b'H+t4@*f@_&>BIhEGFf^0I`nddDd^E=(*8|nQQYy>(YV|ElifPPePOs^?yx%vqc+5j^v8~H#X;Sz@C}nj`X>cN#f<dF1Vv34>Hl~*'
        b'Fe-ASKXT+Ub%ipt?YtyJBvz9Kb%>xj(;Rhb?8t{>M}DN<cqDdu^PQR;RfXoD=7gr@Ms;x#X^nqA?)515--ns(pGDj-Jls!4jz#T{'
        b'gN18ZZz$dHn71YF&%?XVoS$C!*~g{>!@~7o6B%EKq_bkz_3rnEshCaAFrPUuT>shMjK?C4zx6)-5}(F>KFl{Dca6Eq7Nq+%On5ej'
        b'oCziFKM!vYUwg^@{_utDaYv?2E1h&OV&3uxw}hUO-oJF=wr>p6rrjBlqspFi^rA%l>m#1ny&h>^zx$7v$&`#76*${db1d7Qmh^88'
        b'KXniDd?)qvCJLGl7AC93ou+Mnkd8lkT9YbJE%iqbtTC-2>oat)?)JD%NB>3T8njw`yei*A4r)rqM<o6lX1OPS6=<k5E!}h2b6~jt'
        b'!0_1v((H)3yO`z$59Y840%CoN+`6e-s9QVQr+Q#|IQY~rOTzf0-%7pVBxXBFnpibu$Hv#iqZc4TwX-$pnEufI$mSP5?dh3$>+`qv'
        b'y*Kt`U)267YkU7Y`T6YL_@pU)y$wmLzm{%Yvp=kF;`8xq48>o`H~DL-LqC@Y<Wsl#5|2}_86Wx&Xv1N$U0s(;P+RXGuU|j>T*jFA'
        b'ryoCxlgs+F<jECdJ{vt4kt#&?i|z-p^HPPq??k@Q?|xvI?gVUmM$+FuEQG=H-U71i3F-6cP@9;|YKTbmNJ$Y}ckhVu^!M~d#K$L%'
        b'?GuwfI*R&Z;IJ4OC2sRbF_(su<Lf@UkgRG}-<a%9Qb#2J6CR%Zx%A}tC}Dhj0V!6K<a>6h&OR(Xx$(514*esaf7VH4;E7M%w_-iq'
        b'*5M74hUxknN*$hA7Ip8_qq+j|flZ~6d&Gewk%?!atPtFimkw%osn3Ryy%tk%oN2&f+&S@}YT%UW>_^gL_a<rotTzuI)EYD-Ml%8<'
        b'|A7?xHRhQAs`Pj5tNGB=86{J10)``zXa6eIy>aPa#F2ioOXa=|D*}xIgA<e@NX9lb7LiYjh$$S#YMfGS`#_3WJM@d13#M7a`C1b5'
        b'>bD0qtIwj3)U1ifj!!n^s8XUrHKhBK2R4n%u1?O+iAqr=tFohRIwuTfWnT}S`@j?7w`PD5m>VAowyHWsb@Xe=Z!g51Kxb6kuy8A='
        b'-S}Z@_~3f4Iian4o1D6N`0&lcvA^!Wd3YN*vL~b0J$@>7`0(W6*cZUm=#L(DPi8E1U*#FG?jv$4YWQ%>aR2z>y`DI$n)HtyKECOQ'
        b'=RLQYC3Hs)%O;Eeo(v@WBIL9N>_M$NoTiYNy)|a|%<ib3pWYz$sdn!*^}HbVYlip!e#A}aNFEyMX*G^%Ri85<1Ek+DGSq#5YBR7J'
        b'WgX|fI7F?kbw~Oy49TV!l-&O>xQq0z4I923>VE$+-Y>koM+0~_2J-%OsQa_ac>n6<JsrUN=K$WU_;IJ+9XkB(Q0(vf-yH&PU_nB}'
        b'sXq-JerG85&qpsw!o;iuFmQxP3*uEm`1<5XY6*f2{76%>NgcX?luW(u)LTP`-x}&aIkdO`&cy$b^luJrcxxy(E9-f6aU5}<7+QP('
        b'8r1{Ot3wMw_V&CnbXt32%)t9SV6{IUQI~uDp4W!@U!##5EvmEMN_7#}4KLgC{80aX8hQ3#k`S}=t_?2_S@sNN<!CK04c*m}t;))o'
        b'vgd`N1N&Nj9V6U)I^;wstm5cCrG?T#-SgzoiLv<LVCd07XsLeBkb5uIDf?~+=FZI8uMWML?0I^q|7lu^^((1vZD`%ML;B4_dp6T3'
        b'P;*~G(J==uxjjR=mP7i7hgz~j^jn8?Sv{7mLw7Z`WJm7lhbm<KnwE4zQ~Vcc&x3NgnxkM(#Qkze-#j#Z+O&+QJzIu^m;;3+8S3Ic'
        b'NkS;-2K~>6;+78OJ|KiXuvZQ1!JdsQ#a@*VT3_#4eOw|!Oz7|VI601Jk9a_=3Az=PL%25Il%tMacMvLiwpD6Zr$roJe0+ZFDnoPD'
        b'P3Ja-PU-ciKqs!x2ItuISecQUr0b4tJ0?A)-T6N9Sznj(L$wCar&-Y<ajv1G|CB)2L+;jcscyQ;5E>Gz&D!^y)!2RU{i@K<z@$0)'
        b'3H6_Q6S97!Za5a%trnXjh4DSjhs621<2S~f)q;chwntTeR6MBKvE8~<s#~npiT~2|b%}jCU7v1joG#l0c$Z<LhCqFK)*J%%flVH$'
        b'T6TZU&<EC-Ckb$a0@^jk`m$t5$Pyy%YHVoA^4ekp9^#&h&EGI)XwR6TM>j${A9+FD>meJ+&|wus2vZ(;Q6-Gs-6!rjbV-;r?FAIv'
        b'J`sxhd}8zBgblNX`Z3uf2O>9Q4m}zVF2S^1b<bvTeUA&xY9Va(2#7sy$KsmvBXzbqK0eD9H+^b~CEoMc^l6Kt7RIIAjvM+ZDs%EG'
        b'm~z>cvJDNd#isPfj|nMNO-q=RJZ9Q6>Z7S7ep=Q-i#h&KuEEff1q(t7p=SbN2SayhtQF9qb<@Mard<gRdg!ij>u#wu#%PYN+cw7i'
        b'=B1Ks*Mk`gLv!@{<Civ^xRjfj^?aEA*d<+NPgeHW-Z)K9CM@vh>;9(QykXs<T_M&lAv;m0&ADft_VY&TVhNHASi*WO+TrNF+c)cz'
        b'Ra?TcW2VH<>&wkaQLVZC!RDjyNMs<6e1y9fs=2>A7_#k%R5y1x?(0j?)tgO1#CqL%Vag|N-LE%!ZadU>56Or!W;8xGQM0-K^VheV'
        b'4r&s!VFt%ckAT%ZZufT4efHAu+=JmKG`m8!oO18D1Y@-M)cU8y#60PvIIXVmknYQ#Pfe@;EcI*$s{(2!Y&m5$OPf#i9o`-mvvzd*'
        b'#F*SsP&E}<`;Q%qTl@U>vFo~z37^Dyj_Y2(Zr$65-@NoLbbzq-?4cdHr>@%`_1OD8o`*kJ+w;nyfvv=Iym5Qfn!{U8{r8@;zm(qF'
        b'gSpP@TMf3vu~@J*z@d7Bjpv=}c+XcU8@@iAAgG_sRE?-p-0}VDm_JOq=ebL*6Iz~Auf7##7CaHg?bit4=(VeNw{ALl(pBFcIrisA'
        b'4vY0iR;^E7^#!=<Yd-wiGR}Hb`jNWt!?cLOQ+0F4Z2aBmmcu8)o=s7E-Voo83p@9f2oqFm{WFgB;t*l-x0&i~5z^_1{TsHsPiPZ='
        b'Fa0P2kES*8+9}x+)(t$HIWayVEB=TW-;@P`X&LIH86@tZOU0ou2@|rmYxjE2Oy42glq&4r*JDkATw~rJ-tLZ>ON6o8ekQ^4E{p}o'
        b't{6MN*g(ix4NSrCWH;D`5wP$ZF&@@?m|thtNr!)UDRt~FmBDjn+iEFyCbb_m?iH7)ceL(}!!CHNdqO;WzZBPgNzmlDLnn~EiKN$Z'
        b'-R@tD&!0+sP3rq_|EbR(oznN<{M9#*GtQ_3%Quf1(-^%y)U!pmWz3X}6*qJ`Ov^JqUJc&t_82g61r4m+>t-dp>kQwfjoI#Acdsy3'
        b'&?Me3<+$q_zR5oP?bI7AwU@F(*S(V+vu;!MtFaHM4cd^b<Oi5tpgy4yrf>Tj+oy|D=}%k~!m>4YhBZu8^){iqzoG2Xzyz{>{rTNp'
        b'QI9+ty?MeTvqD!)y?4ta&lbk_Ym09{_jZHn5+r!!QBz&E7W!lkw)eyseA~f28^d5Q9bV}E0S04*y@waR@q{}AZ$6kSOq?=*qo>~R'
        b'iulOSA1+oAlB`KmhsO6)f41i*ht_Dpg&yYT+v`AAgH`jli@*xrqdWOh(u6Sgv`a}-)$qG!e2%(r{D$Kf;}S2K&Dy$eaF;W_HI;5|'
        b'CYj<ct&fkSF-a`u<oqaOV2o+frQnzwE{ho-9FzYvZj!QnYMvv%$^VVypD>Vbf^ff)9#hA+PM{Hy-7ZLBuEx0P)<~ZDRwAd8EAaKj'
        b'pqTuD%hG%noW}HzfEYt-Ds(WtokSCi*LPo(`)53hIWs>>7Z{^|_o7f19QV#eQg~UyH!u3f3?#>PKcm|bX{MX;1Ff+%)h+9Jg>d_A'
        b'V{)u+OQd-bYkVxv<|W8R49NIEPz-im3i|KKDp5Son#k{2*Roe-S|=61LhaAK@yY7CfpD`qA!)*lm{lZc>fEG^yR3CMP=@5BxJND;'
        b'=c`0{@4mV<$!Ib`Ais4Q>n}|6vx}X9X=s9E@ZNZWzKfnKBuH8Pr9|XBdM=*4LXzo6&q_%Xs&=kQn%dEvv5ux4ANRwHW^?rVfaK$8'
        b'@*6|nmv|Zh)99{{CK}8jo~8xUn6HrLhR|bjnx&Yg^9pHVLSL46|81zac)S6}426i|B(MFC&-<Sp{NN)xrnfR9d1LFX^fpPpO#+*M'
        b'j$i9U`e3~LU_3P~aX%39(do1w4B#6FDM@j&FB&tV#J)&fHa*L*CGoR~-jwliSr^5CXX8T$=~!<Db#UA!S5y{+)x*@UcyDlEn=xRU'
        b'#GQ0e2&eWu^`kC|>udK+y?AbmioIR2C2~*P#oaq1WxJofW^vO+@fQhrX0#<L@WI53;ud^RAMjvvn3$>^*d>9x&>0`K-tV=QunodR'
        b'`Ci^@6<s?&a)({)54%WN<H9a__nEa91L`h%&Tl(UH<;bu4i0#F0yd@D3on-j<sI$ff3ZG>q)-H{u1@FL@XcV1TD$k@m;K%&=?m}w'
        b'Y7o4ifqtW0Qr>iT<siCh{}`nCzNj%geV>l!3>7FJ>-W+N@c)(aZzD2)=szW5@bu`mh^xPr_hbJs*#9oeO&AN66bDoRRUh~b_7^O~'
        b'V+TCH-*hOTRc{Q&AHg?y`i~BZU{vvE1O2J)#6j8jje8L@PgaZRH?aHtgY+GvxSBz5M3W|7A9rAI-R8LG2YZi=3gJB|n|S|k_|0Jd'
        b'ZwGbpD%REUk^N(^G5jUGa3R+%_{w;Kmys62&bzh`cJGInR&90vnVx3s9-9_^R%nIQ^~*7Xm0FW$aKQxi(JYkXg<7Hf(0noe$Qe8`'
        b')CyUGR+u8XR#kgKdOefHd8^*`+&$oF7MH9NTUQwqME6E4`p_Sv#M9ytkDBf|HoG6f$kU-h9=~6M_aj>2Iw4J1!s8-%T&2)1EWv%r'
        b'W_QRSJ-_Na`7Y!Y%G2FDNF5?!25>)yFYYwEhb};r>7Kzj(;%(#w2%w*&BX35Gh6nw^j0V`^Y;|vZXe81Qyl^Ao6<8sk~R(+dFNPY'
        b'U%6PjNoaoCW5b5EZ4$E5LflJesq>E>lVxMkpiuEOSQF#GsHQb*cmFq5!(BTlOo0bby9%f@#=nE{scYT;b%Aa{yQ`_3&KumjlTaZa'
        b'o8c$gn?dFuhDp7iox{?X^1?P42iLP5$1uHd&~1Xj@73oGrfBrD>F{ds^|R<fE&&?(9i|*6Pd(!Kp7sBFWMkOazV82iAV+o6xzyg!'
        b'Q8w4MjY!jSMe)%i>-U&EFZ8T`;Rv`_&uxt8Z6r@k*fKRGLzsx3(vq+T#!u|^cpeyk<3<noO^<B+L`V@P4)mWndLDdN8<;{uPUsNJ'
        b'Qy-1xmTHW1qm!cJ*A*ruRIo)V8_(RJc~dfUYmbzvpBkToJA#9fTRTXbiM561NB8t<KYtJA_VHCq!h`|{gr0}xC#u(TE@|p(#h*(;'
        b'pD<xp*wHVg3Jugr$bcvURjJ!FQV}LJE`e!wX7xXqZMH;{H9pGV@nmgOAFY51ehvbwD~O=ge|iB1Py+)9BQ*tw$%ezD|M-G%9YhNi'
        b'LK`2}Mm~JAF0i*~|0zKt@n?FSVef`NU(jX7^<*3pRuGM`N4LlQmkYX#sGf|-KK-=)P5pnmu;)(~<Tu=48F0UjcR3NXwcT%cG9rxy'
        b'^t?RG^xB19Dh^<%s^u3h>8<<l1-S3sO5`^)^+zw{ghMQU0j+=Eh3?<WWf)6E_dYD649h4D8`w!ag^{!bdf)$>3viE4R3R_-nG3tr'
        b'W#R5!bPDab;NHQe4!#CuVCBKuFGLqVgMzQ$?&~z(JF&Fap78Y=>&zI877~j0@cCl;*@fPCYGfo3U2gR8!Ts^u4c6aF%@fqy*3$)|'
        b'd17+XgjmzW3%xsDX6aZr7@A1pJJSB~iTkAOhO-|@APb~9`S^e*%-w^9#4W=*sr~D8;aiNq2kWHvtJ6QfWdr#tB5fsfd5=#+^l9Uo'
        b'FTi>oXM|t6Drn;xFPPddl&KLL=}4-LeUYZz3r7A@Xy{u^=Ea`#BtA+^7TrrO_^*}jnhU<L`9iWcyy!yzq6>7sua8&ZLb2e2Z}~u-'
        b'UV8yz16N}61>Z`Hd8A(GzL%yq#z$cmWkFdKUzUZiCSWahU-qWio;m3WZ|CbCTW&P(zwK8G7C$q6-oA;?7FgG2zWMlFrd!k(C504H'
        b'NFjw3Qb-|%6jDebg%naqA%zrDNFjw3Qb-|%6jDebg%naqA%zrDNFjw3Qb-|%6jDebg%naqA%zrDNFjw3Qb-|%6jDebg%naqA%zrD'
        b'NFjw3Qb-|%6jJE_8|^Tw)bw9OH4@UX%z4=d#Nat0Ckg#$DeW!`{Rh^Ao~y_?_V0stwytFV@_E2>_V0!hQcs#KjV`-mWiUUKY@umd'
        b'91U$(D8HAG1_=EpaRRrc#TxJ&|1Cs++P(7adoRsf|Nc8K-+W?g$Kun<2rHzJLJBFQkU|P6q>w@iDWs4>3Mr(JLJBFQkU|P6q>w@i'
        b'DWs4>3Mr(JLJBFQkU|P6q>w@iDWs4>3Mr(JLJBFQkU|P6q>w@iDWs4>3Mr(JLJBFQkU|P6q>w@iDWs4>3Mr(JLJBFQkU|P6q>w@i'
        b'DWs4>3Mr(JLJBFQkU|P6q>w@iDWs4>3Mr(JLJBFQkU|P6q>w@iDfC_F(@?c>=E^MNmxPdTxQHa-uSz5#dE$*KVyHdwYvM<Gi$15x'
        b'(2&+-bGTNL%c;fD&_=F7hKyXjE>|~8zOQO@i3YuB&>2|N%=DS*hHLQu=C66n@)kUsbldh*_pW?Sm%n)Y{@%>I2`^3Q*=l;@%)lSW'
        b'|7Fs`6#`c%Tw~xG2iJ7C$_zE6-C1aDv#caD+H5XYo3+_VifYUmhP0XtVwk1Z=`u*G%hl=3oiU@u=4$O~NN=>a&%h2UHI>hxNl8Iv'
        b'!P4U5np&|YL#))#s?HV*EDndw>JY09zP=EA^_i)@ay?Hbk^FrNvy8_RN&ZYplW$HV`52!KasKJ<C@!w9%`K{~zH?jzzp0wX!!<=U'
        b'HDy(mxz$BAMYR~0m_BQ!v)ke7PE6P9obYRKl7!-7yi5i2W|PD&Vrjg)JJIR?e_)iksIsuEvIMgSmRw{lt1Pa<`{D(;a`U0f(sb$i'
        b'^o(2r<-)T9lQ|dC>#-KVlE0`3p|q&Hyoxxjj%8K{FAUOFR#g@h(VR{5YfER7#x|R^!{vL9vAmIxrl6v5Hc3bz3Ad7j5|S{LB$Sba'
        b'N|LaUBtZ6Nl3*^YtRV@|1GP|Z2${-F)fIryXI0gJ1yvOlrpm$^7?#N)dEcr-@-D(P43`9#S`(5N0#_JZW8sQ|>qfZZ;7Wl@50_4F'
        b'$e5WqD=Rz4($LssZ4RC^VH$1z%wm%NK`|S{KEUV_lD`Bn`_3$*3$A3i-wJph;$r_J%lKXqq=j%RgnP;$T?yk2rnljW;^AB2lEvwi'
        b'UwmpHOT8TEp}(qnmH+)2b-mi}zG=zpbIw$d{D<d}d>7QE9B?1hr`Y1MwB?Fr9WVzvEiPL_n^kOb*kB;VWWwh}uGnc`4iWYa(P?dK'
        b'PIFnEE-~3$Rg)q%TWoFCrZ^bF`KIbxJ^eM%-wgUY6U*PD4as{Bu7hyB0@r_T4ar+DCM3@W*N@=Z0M|CSo`>rMTo1n&l4pW6b4an('
        b'+9bBx+nPwh%0{S}(`9kENPe5W@ourn+GcfGNsY_iDK^=h7N|KXYPULCtR0OjA*H>Om>u>8D?V(rcXU`AU8KV9vOA#CU2SrBxy8|8'
        b'>u4e6wsxD#DcYgo4qFps3z1M@0~W>e!DlXqWtp{&MUaJJyI+2b0`3+E+y$f*4S{LlesRz}E6|JnMc3NxZBDDpWp(%k{S#D}OCYx<'
        b'D~=Vmd7;>bZ4=vV9sXg+-Fs(Q0pV7AyOjg2p^s}(0M{Zvu0@P%k<7K&k85!N*J3}e#f)pQ%vIBA>u7?`hF|Ln?_FmXG>(|MRzSR{'
        b'lLLA=V2}eDa$u$$$dm)K<Up1j$d&^+-VA+Nd-K+NGuL}_*L$<qd-K<O3($K@(0hx}d&@9*%P{!r?=8c?%CK};+Uza9#`^B{LHCBB'
        b'`(XZ=LHC(K_p^fTvtZbrE^8-QXkfUA1HWC&f!{8K8RfvV2#eS+yIIVB*-Z_k?F7-Jx<kHmiq;M~Qy0pC#om}ja>&HWG0|*HzF41Z'
        b'nf#>5#H7g-FyYwbE~xPa7J5UAyrIS3P(_9>IMWx*^aW@6f>~Y>wRd=fP*s?0HoqA2f(mcg;GfiRg~SG$yu#*mk>WPHy@`&Hz01XA'
        b'0YiFk$lwiSctbP2p-gXRmN%5;4P|>nIli3z3h|Yq_Z6e}m816+r1zDi_Z6l0m8JI;ruUU*@RerpYm=|E!1>_o1iuJ<aD*W^;<7wu'
        b'21jHDN6ZS2$Rg!Mg<>`REup{p^mhUMwKO@bPPXg>-a_pP?4Y?D#cC_4XZa@IZg=TOMOjT1si>+cBQ@qSu>h7~iZwcpdX5H;86Xc9'
        b'XDf<wO`+ImaWwe{n_vY56^}_Bv@8sjRo@O~aDiA;FppuOiOjRE?6fq&yrK&i#`0kGLQ=bsRM*VR&J?Q`&Zu4JC!Dtzm5C<$n@@lF'
        b'f`UP&s_Ven=(4oYm0n!PU=f4G3@S1>&g7WMaTdocZlnBeY)Bs3FQFk|s{uv=Y5-4HhvcEH9}D+r@23Ew%|8ne?fxRbFu*!M^phF@'
        b'BLF)A$D-{6h`zx?fY$;3C*bvfTLB{h_X47QbqH`G;G2Mx0RI9w8SqQMDS)GZu~@&*ki44!Cjp}Qp8$9>U@qV-fO7#wtPfxu+FgM0'
        b'SRcTtfXe|BuwH<Pfa?I003QXM2KZlq$$+~6Qvja@M8D<;Alii|0nrZp05A>kZ-D4Xd=6*=yab2_W*FE}1!y}076MKNECQSgSd6wL'
        b'U<qI*U@72jfMtLsfO7%Ofb#$s0hVLG0#*RF0agMo1FXV!0Ga{U0^SbzFkm(IGa#7aWIJFj_A}soz!w4Q0FMGL!1e$x1biQG5#Yyw'
        b'i?QDU@4$WsTmpDqSV-QTfHwpF2VgqjQmi*18p4%;7Qp`iYyj*4Yy|8AYy$idpcU|bz-H`sz!tzwfE|Fp1hfP819oD)0q;S-7SI9s'
        b'TR<n^3xKO|JOJ;<`UCz1&27NdfZqT<0Qf23PXWIMYy}(!bOCC@L-P92rw2?291l1H+XbjY9~N*t`tyMI0?q;aAz&$BH()j3j{uhd'
        b'{ur<s@IJtM0MX9x26O{H0N4w-5pX@=<A58mU4R<_4*+h$aR7W6@EyRP1O5Z>7l8i)d<5kQa5GNOh>*N32!M|QMg#s5>karAU^3w2'
        b'xQ_t%pMZIQzXB`<^q@Qe_5&^k9Kd-2_ynLGa4X=wfZG6n0{CBm>j9s{aRJ<p^8)ZG^d$gypd10>2FPoGJJEjv+=coA@Hc>;06vZ5'
        b'0k|9G2yhSJ^`K|=0*ZjoU_S%y1I!2fEnp4cvsgdC=TLqC_XGB-Li3&nTn+aJP<{Yk!2Sh%5pXl$L6m#ImvH_9z6|&h;32@@10Du^'
        b'5AX=q6Yv$lj{si<{0#7SC@+9VvEKn-LqAXm$vcMq4){9Y1i&}2-vNIQm<D(pFbnVm$_wC|IFA9}!hIaTlYn;uqA%GBh`#3CfbU@X'
        b'6(M=JInx36f5iC#_$QptfbZfs0KSLg0Qld4+W_Ck_5uDGa3A0YI4=NC<GcX;3*Z}of5mYDJcIKa@I!1bV5Qv!MxDK@rB!UTS~|sM'
        b'u&XNTYQ%=F=4PuSj?{op1MZhoT<);Btg?>@9xlqET202Q)v5%wT0Kjx)|9H%+Qn*hNSj(6`eU_v%zCvtY(T9J-=|hb9965wCTTRJ'
        b'L!(hWr_s`NX6Z6ZTbGr?Qis*m<>;_Bk&2oU(5efw^CF`s5^Wd}2rBX9RNYKtVQIO!mY{Cb(Hu1Bn~x#bspLK~hOY6V%PxYC3AKj2'
        b'rzMn5>z<ada2m#Tbx;qoz|w_FYOXk+-b0B+)T(VFh0JvY54Y6{UTvY>?%+Y@k`i-EyI9oGM4%urK%rk?)u%?T(=W=&>_}46X0>*r'
        b'KO5)?i)kXb&lX3j=xVigFk2y@&ZYKt%%+ig*$(SHU0?(>f%^$24UeR*H}W{Fj;;>zE_(wM55omzSRvZpCbn5ST3oH7y}224hpIul'
        b'Y|d8fT|ejc-__)bWy(*}q0Dyhb-_wo3GrQxtzu`J#fA4xV&}CvnJ>+R2}*aY6fG?lTL(O_IzR&3MGNGBNtWB76$!QG1!A+!;dI4u'
        b'PI%~IhLLCiSO&#5rC+(aopz^<CPc}m)l7q4N%!Bpd1^AVcW8J5vw4tSn855Fq_-w8+Xv~x3C#XM`g8)bfsnqQ!0aHTkqOKeqUt)D'
        b'*+WR<qnS;Flo-wIBBZQnX2T#EqnVwAWRGUH64FninZ1OxHJaH>NGGD1-Gp>8nypz#6K@E~o4~`>5RT@1S$9MD1|Gi-!ZAGjNmWSR'
        b'jXb>l25e&!S^qZ4uZL^J+rGUr75`Op)cEZK6TTO$QnCGD#4$c58NL@?Px(|NlJnmZd&|x6AN|>RBdjrS?S^abjcC6tB8!RXO4-ag'
        b'alCwX#Jf-Yz&>7+d*gGrXYc&old}$Hg=YTz<+_aJ$A7I~+8M5s{(eWgxy{ni0p2pxfuhrPF9@Q=2@|BLs}Z$d!ra*~N~&=YC2Uhp'
        b')Tis4#XF`YOcO!KrqNB(X;k1^t!<rj=NJ@MZbE{XFjY(_5fjS9gi0}C#ca@g5Lz+2&DLQRAy<Yq<z_LVKulODCX|W^`QneoIB|~H'
        b'=yJ5Bt-#FE$Q|HYR2G&O<r0{~gzmoPlK6zQ0(+A+J~dwCS{sA&J3w*y#fgPhXQRW`iE|<zw|gm5IDZ;WlZO{tTo%{LPAd&yL)tB_'
        b'@GE2xUSWgFvI6oM7m)@ek~^Sgx%9WD)>K=RTUa%}w%hOC6ntM+*-g5;yUFaz87Ay0+M0r@LTKC_bU&Ge?RUdNtHWV;<U(2FBC4$o'
        b';KX_LV>(HNa6lAU(y^qYvI@!&O=2s$XiUS|n^E6UZRD`GwZRD6oL(l;(u{j}jjfiB7Hq7m6&^ZS%hRFY1R{bYSXS7a?H1?V^actA'
        b'E!x4tHdnLF+SZgCa3?Nr1?4PfgVCanZ>2bCU7%tv#!_Ym@0Gf*1h<2*RZtUaE{0%PU}#wZh@Aj}!1mx_^ixSVv30ntEmj9<ZnIll'
        b'1S>{X$dw=tOOwss(B*R3JDkMUxojrsv^bs1?T#jIHYL?n^UXMVRn@h*B)=Ah1zkgcR5QuWB9%o|6*WYko=J3Y6@ydrqnAJrO#%D('
        b'MbIyReglsKdj~A$xumS4*$y>c!1i|`R7A&7B!$+7F1)|PT%8ZamR42ZsMnTPVI54>CXi|r3vx$ErXHe7NR9!Y=aTMOsk&5MH>Rzo'
        b'9MwkXzmhDtvf(o5@JA0nIrIl_bMRr#ERs%Ra_}b`vMfNp90UB!ngu^IG3iWvIx_=)uvqwo$O^oGwE~h>WZ=y#{DIOcAaw;zl8MhV'
        b'Gw=uUswHAE5o^e;sU$6xm}(1V>lx@$NpZQUrj!&z3rSItxw@)?+)-Clor`)To!n7nh9=%&T37?Wl|>8iwy1J`MNMjTEx|rYC6!gc'
        b'ln((4HM5DiAeB@Xr;@6gRFYqqN{Rq0%wR~Bn`%ojow*DW6y;Y{)uxgfcvw>esj6#%t-w^7O718wtFBmJsxHdq2Mttf)s&S~n#yT4'
        b'z$UDzt*SPa;0P607Zr&WMHN-mi{P%Xx(q8%jHIIUUinspi=LEuBcK^@kD29HnW_r`D@+R^(;~B2jRHf&(tByCruhrSG86$Wm4!t$'
        b'1(1Ebsm%hW0jevU8q1)wZbik$qAPI6r$v6EOY=PmQh4!H_%6$a#a<y7_8=&eQqb#QO?28Cow;xexwW^0-Q&ctY%)`&$dwulcWqH!'
        b'QDrSQzr3uX3<J5PB)6PNJw|h#UQ~$+52YGLCzn*(WrGrxREy0C>Iu{xW?E4N0|H}KNfiLQEjG<B$N5oVwmSh9FfdiqAB--^)icnM'
        b'?m`R~LMV@vp~YI=)j@I%V1S|mn`>`DQ`AamFXl2}<}g9aIF}i?^yGtd=Ql$M<sI--SPPZuF0R2JxXc*0prDHWVr11atP5N<jqp<n'
        b'7uMH|h;zBStb_feLEVZM$l^%46AGZVw?VtX+^;UJDJ-uosw%D!Zx=-~_y>7{D&GuO{X|uMTf8d&u_#sku^3f;H^Keu8SU+)y?q95'
        b'R|7b$jsIaFP1Y8_5I&+Q;f74-L~Knf#5}QbDQL9n+WF?C<z<ycWJWufs`QL{2G{7$^hQW3=FNtr1<*B3whpjJYgR&r?M`yp0WL{J'
        b'ohI{w<6~)B+K6mRn_#*1J)kbv6`xQRYT|ZvE=8jum?_{H?)S4J9N8}b@ou*@I_%JXJ4kK%k`7qNZS7s{;LmhgAqLMEabW^OyAh@Y'
        b'OaQd%VJQTwz}9GKYg>tV(4`BPCtOqYV2T*hGt+U^t!?!d)e4ImnBfgp*?bb49rkw0%6%u1`hS>3CN7j6xW1*+V+Y6_{0ZxdMm&17'
        b'bV6lT*uWC8Lh1UMI`Qt(d(+WDh4ol;w%Wno$Ky#njI^v|IibJRNtbau)W;<@t?aNs!`X_CM~YUkZLIvrlKO7^Xe3>%qm?pbW{P)%'
        b'lsnmphJ0iK=0;fu9`mu~o7UB7Yw57GImKk^kwE+H%TofAd3STaLt0)D`TUm^EAyp`6?UhKKXZy*PS6d$oaDsJq`_9%Fk>eaobEG;'
        b'%9^iG4s;9{O57-MTH39F1%p&T*DpjlfHH$R0c|3F6lCk@>~eW48<2{*b^ZyGozQgVfy*|T6Hj1p+aFU|mVujSX|T1~Tq~je3vgWP'
        b'tIZX@#9TiH*0mmM*@)T-We0?}A_I-{ikTSCJF7+~I>Ez)R8G-`hG8>JStH&i20iJJOP*G3X{Qp!3Y+F%3f4pH>ZEzlaFcyGOcEP('
        b'Bc`&nHFlwc%x6GCM$Sx{G$Au12Q9!(E3H-A%6}&{)RV;lqO+Huwc&u!CoMQ3p~)+(PQT%<MLX6j2jEw?wc(tEN!4b9)KFP4JDH;l'
        b'a|LtvC8pJtjn{+>m~&878yJ<KCg_R?l7adOSQ^{9npk$Afm~g<WOdrHB~*Ph^IMVH)EzE1Nn7cD2h<fr5>_D5+10?AZQl7N(gVho'
        b'SY>ZRowoMQHd&&4I|6=<Hd`D{bl_a5M&u^bf}Pe*i-TzrX7IDQ;8$f@V=C{^1JoUW{$$#w73Ns81tuV0n?!cnkHh7lJ83X1Fg9IO'
        b'#$a@yQZQx9>3bVY*EwODQo%wA;kjZBN({8vk_^$}XvAzAvCA!uja?9g)?2XcP#-kqq0^~5lrH95m&2q*F9$|!r3ju0w3HQueP#tO'
        b'w$UYavaJ<MN267qZzvIstzsAYd~7V(CLAraW2JBJ1S>^#G0WA}YN2D;0p6BHmJBC*7%04aj$T>e$;0IT4oRw5C5sd)?^LmfzEpx0'
        b'U|T=@^%0bC(A-}6;{~J!s0*wkSD<WNgP{+upB<ciHrVZ8TYVSJ>^*Q!1@<oRxEzhxfaNwP+xtS@b>(dM{^AvT2G-{`&>f%$Y`BpK'
        b'0%Hb=?r_=YVk<j~n2Kr@IUP<a-sCpxcj-}DMc%3Zn;q!i45sk^4;$eOY(+o;Y<lzcCn$ehI=)*8kTR$Yc?LM`%`VmouE?Eq(-AEs'
        b'OJghU$FSMWv^q65s8>O!3o}h%B^0aK{()20W`wR5UhUQ1ZiN|3^-Zg#&E@23fo6(YV>xO_|C}vy&(c+hT3!xYOAEFA#WGZ{4jW8r'
        b'`f?G~QmkA|2(#8n-yP!_`LY0u44j)LU*lW-wwnFg;9s<r+Jd;6a5K)*<+6hj#;rhn-=m4DT(&S5$!jouWsBMbjodf#Uy)M-QpnYS'
        b'E<jbz6cuz^!%8usG>;h;^xdl4yqWnGX=+2G2V%PdSN&90YgAISmO(Y=%L#kLxFMDniH5>83$Cx?@1}`3(OAoHNwQ#7sP<%X<=s-}'
        b'FU5)Vd~@I4A#xMlyYp0^F7Nz1t)Ts}<7t-O@#7Xb)yd2J?1FUkI9W&H&JvWyGC+<FYl|f)HG7edYI95q6{ZshB_mMgu-c$M9PKy>'
        b'aC$&nEqu=%7bF)oRcfr(yS=$VOB(Nn?3!&<u7fh<);3k5ZFDtcIYN^=!A-CR8S~7JZ?L+STVa@K3MYCA{z5Ao_TFA<vNnKDZltFZ'
        b'xPH2@>s`3$$qPN3Mzo)O?F8M;dcfvN7x^$yg8|PdP;+=EQO7hFJ2k<1RFai}OJ-m>$vAAFIy%J$@YC+5r$i3O3j(kP_&H;=fj&V-'
        b'Q9;8KbwV4SWWX}pAsT3Zv2_>sDWP>}VRhm513V0H<46Ta0eW%r8U;2b&I3NN_zRVw#8J%UG@Wf-Ew&D1<}Tp>4)bM=NXW<(lW`@)'
        b'R}N|IQ|OFq1zpM&37;A*2y8)YwzYKO9xPb*>7?9(wi_zA+yH~BL_fnYBf~o%*)Y*b4vLk#ef}+A8i5+cP|b1+mc??Vvz59sC{`s|'
        b'sbWcXD((?7BP=H?-TwtLFoR*H;xS%eG<pqucsfvbHKKi)+|&iDCl%3@z~tWk_>RdfEB<|Q*&1KoY6BUSeOTHle!9o!5u@nVc%7z3'
        b'=nMxFNhcNo61~jc*2R>Cyi&w>pzYWeFYgFYCDts?NfqO0Z~Yki80P^NOiSv-12{;MkS4nhI4xk*(1t+wlh><>oj$_PN@|gSAA)hR'
        b'6G9zD7k6W!X%?tEJ&hIbvbXr80Mg6r^>Vx8ZfB<jW+FX-VX7a!A#Y=#YIl28NUE%Xeev?5g#A=#ZKj#huB8vC^~)D2?$mNVwy39*'
        b'%C7bXd=c2It8k;;if%ifVtTrX&w_^RbYkMmD}4zU2AUpr%1SZ#A$R+(@)S%L$5kIT+q)dDR<E{2RRq1*!cMKN%yDZ+Rn=~#1BucA'
        b'4d`-VYFuT%bLwLBkG^y2xiFMo{mFbgY8^QJY8aG?FDBkKol17P{~OC~Y53wGJ&kVb!c8hKFV>_zy{x0rVMS>~_mw}oJcAjW8CNW^'
        b'*}HVoEO6H_otXWl1{QTtXw*b&Z%@S&9a$_Jy&Hq#9ceK7OPO7nD(dd^<w4y_c{OEu@pa4FAit8?I|p9f%*HxkR}EHE7f#t0hov2+'
        b'I&RstbRY|zqBdw~F1FnPW&*y#Xs2CIO>HQqtgyU@JI|0W)t25NwYnP9MU!k!v+Vp%)Nt32=0+!Qdc-^{45aLAu`I!ku!Bnh<=dI2'
        b'0>_goQ#l!|x;_mA{f}9o;s&v%mJD|G-B4^(7u62U^4}+L&mE1gE)aXVd*OYEQjdzsCR^Lof@WQ8fuh^^DIpZn<{fdlf90akCt*Hv'
        b'(+p@MGjim}@28SvadWQhXcWz5g;e3wV?2-oNXuM&Qp<c0s2bPIY>NdqCfPia=heSW+5|aUtv*u$g)Lp2j~fdxW+gg^=(I5*$Bu3U'
        b'AJSoAX6Af(=Y=~jop?^pcUN%)`9>|<kAe$UOJ>Y~fx>FwE0#?bR#o53$D!gXlNns;Vxeq;()|TnlebTO{fVY_8h7EayjFiR+M7ER'
        b'Ud3LAkxfdcJZ13jZLA$mluAB6z8cU?621dt^B*yoSWK_E?AS%r!gR_@G@6o4)@3$kFVlAMS=dfD3aMqq4IrK0BF%Qeurs+6>X$h)'
        b'UtyS03($7>>@aFdI>qFKj2uHM+gd~)CNm=^h0D2~ZhSf{HYc@%*gk=+nQz3SrOghyd5s`eE=qpI37^=Z<7K5?Ni71e86|55Dj?LI'
        b';%^1v>o(Ly>98*MZ7Inf7d0I#g3{+QDWpZx_nDXh=jBeNMw?tBwv@giB){Q9i@Z|4qERf#%t_Dq_xbz120*nRWea?n=<-I+|4x-M'
        b'd6%sJH}$eyo<A+OknZ5f-lx22M@JfqO7^O6STOCNf>OL&rudo{c;lAFyJfo!MFAWs8{L%g?h-Ny_4P;mmD&(bcOpQ#X<B&hwYE}u'
        b'YoHA!89HCSO;@V8PnF1uH^6}Kb%Hz)zIt8D1NN^m_=HY6dVYSex4ZbOb>H0;zCzCb-XS*ARUZVzAuA{Lx(IVQ>Fam@J`>qY2pXu0'
        b'S-IRN;2xN)Ol(d*;!Zm=b^~6Q;nE={(+0V0ohfv8N<J{c*Is-zs+c9Ohp9HE*MbV7dsnP9E?WFg(d5cf(JheW9mU0k(&1NizbS)T'
        b'=>C!e3OGo{{C2tg_OyJvSk!LiM+(sQR2QMHDapuAp9zcDN`B%XYdSR80)(CvqEg^nNAv`gZ6Wx)H*gE+V_fOk3V1c9cKJ}&Yn@&t'
        b'9iIt)>DY1t8XfYV;gIdbW_;B}7G1h(ccg)@2hu`~ZMy@fKyqbW4Q^IjsU_%=dkSBGvxDulGL_mVj!uw5w!ArUyzF#BJHT96MmN+~'
        b'_}-gx`nljZVW=J4f-{ExZMe_4l;y%@_noCtQFU6Ht>E!8ixToei=qi<c95Bej@V_n%Jw9EUzWWW`hOwU%j=pB>n1Sk(lhZST<4@q'
        b'xpym~tCJms#mja>yx82;(a3h+=~lZ-o=5b=5b|AavAMi{&gF}^&vvAL3&c)__^zVA4@&=T*6H0p40yQ_k2aty@I6GPSTKOa^FuKI'
        b'L$fOzEV5B$!-Kpo@at%o&95zhteYtZd+l0GMstPh@q~pbS9s};8s09peag4k#G*8MRDm8ZQwO9RGxKw%oa{9V_6D(&YGhjz^Xk0E'
        b'cK>GV=qcR)|IrKDw&7*b7baSL8#5M{3oKsb@C|8sQDF@;>m9aEQGfME2Hz{y)U~852KEDYuk8-zn3ou`{WUHaGPz4S@a;KxK=;A<'
        b'Hn@()!Y@H92D0mdi6#F9oWJ;8_GSRzf(Upq;OY~V<`X<5>7+nD^0x$dfcB1n4R<+Xc5cmIaNsWoK;CR~g>EgdR}9icd|!p1bNOCy'
        b'u{6P|@?%3gUs`NXetofR1$7B=Ij)!G%Nv6U*|9kn1L|BhvwbgEGU%HKEnOfC%rAl%i-V2{?x0Sqwql=&;Kw<@ZUK?!2k_HyM~?QU'
        b'w;<m`)=C>VFb*5FMrD3#1@Y2Y5#M93V?Gt;k{M`tS*|+u{ZfE+*d=?7ep}p_Kk?tAW)E#%pM_A@Rem@tGczO8pP%-oi^cd}gy6AE'
        b'#)3zfjcKwoMSkx0PKr~G^Lq`&3DN><StGugK}vitPh4IeJ=m2`f9biYlkZNX{`>b)QsqO<Ht)VR%$iPq(3;A3IUMZm65OQldlf-0'
        b'%q-hAey5W@O_-X`-&e=&mDF;4*g@5TGnE>=N!;%=^S3jssSE6m09DEigH-u&%b6-4xyvb>-ZF5z0xGhgpo-6eRR5PPQrVlA-Zwc?'
        b'1K#V98|(M>2lfs%UD90kv=)16(FzxyHaC&ET+8~rX)+Z_m#)+4hzZ}4kUeCubJ@!!9rU#Zt9P*FqxL`%khKky7jLvz<ufHkE$}Yy'
        b'S1p3`3VIqKYC+EeM6Sl~)S3THeJQHYz$h+UHNLZ6uN2|zX66_b)_^}6l5Z{(U>;BX1FLT{)7ztg2ao{VpYg^Ap0V*69Qd$P_E=<N'
        b'lpc}=AI4$l$R}V|KD8n+rLKG=MJni_cQbAuvaKn;6_M&YGD`KG^IZ81hqw94Cpm<h>Q_Fvx$^mp@2d)+A@P+#`S3sRBO1XcEMl_R'
        b'T%96sa<*Ap@I9aETJJ9670x=mo5gIfxsViE<-ddiQ<M(5%_UDX`Fz5=kIAJtVC$MJOkI?^SRPGwVnOtVY<7sir>XzRMBoGeQ;EPQ'
        b'ekT$^dHJ12c&p;w=k|$8@DnPMaxB{<Cuv-Q)ATx|%Qw_7-z+CJe)hktV(B~0^873IZ7DN*g9IvZz8#DyQswMrQN;!RvJG$MRixr('
        b'7_Jz&SaS(a#?8}C7oFEE^NN`%q}cAD#}yy})P$se{zgYqu5Q5gaT=PyfpKM5h%3B8oV@j1#&(=Zn*Ro^Z!g(T`A(h66Se#8B=abX'
        b'-@b8BD*k007TM%=XW7z2(wJU{QRFFFucER7o?fP}uD(Z0Ussp6VW@iGx+8e2F!gGChpE@tzf0w(D;2W>$_d_~3V3)~(`o}Yih^1e'
        b'oUPTTa4&l<3&~aYe^M{sS4j=p0KwK>dDr3UdlpyUrSQ%l+=f79iGR*Omu|nM%=bkXzCIMlE43U^$d9<>zqAedgFWW(5<RsLy0Gco'
        b'E@0L#VSo1<?0qs%lhBhY+94g>r&>l8HvVbZ)qGEagRf7;UjzNk0IkftH@S-VSrYE8@lNrJGRRT1^ZBygVyFANpn$y{f~zX+fMU8|'
        b'!yR9Fn7IMtbF`d+-__!gvU20e+pmx$;E#l_!R4QTus^<*6=ebX@BE}oew(-1CxQ6qlx=pWE0v{Vv)}2}f*>9#{1M;XleIRF4LFwb'
        b'e%^>1+^ml>Vf1Ud8XT}<pegLNp+TA9D=p3Ra1sU{x3DX6ve7){X`Qk-$~^vFU+UGoH2SeG%N4{8<GtPy$;h6m)1~V5nFatuh7Rv$'
        b'&eCNAWM<6*kxk7p=mDV)AaEsCkZZ`JAn<Kb-wcx{hb$xkTHRk8@P%DoLF5H;hTkHH2kb4(`=I^l?N{a+Q+LnI+&x&x(PE%lm@Hzj'
        b'n1P7_r$Zw9+v>;T*xyy(5YPUmIxn96J#}k5`&;VCQ`z598>h0rm2RBM{(jn#!2Vu3Dv|xI^w=c!chZ(5_BYb+B(cAbo-vL6ZS-5y'
        b'*xyB~liA-ymnE~mhmK5Pe+zw23i~_gKc=w1fzF)H{{H#x>FjTxZK>?rGjFA`Z_nJ6#=bpsR~q~F%(H3i+cT5X*|%pZ(%Cm>cBHd!'
        b'&io^teRF2n4ED{Lp&9I(Gvjsan=>XI`{qoij(v0HS3361nLp~-H)n=*?3*(i^z556uj|=2XGZkwn=^U?`{qo8fqir4J_Gx9$>Rq0'
        b'?UDn4_&v<`05k9#IT;~&_~E~qfSJe#h+h%y1I*%>4Y(692k;BPT>KmBnIU;Uz;OV~1Ka{Q8~@fE@HW67XW};jp`MxSn>TM}vTxpe'
        b'o5{WzgMU+h2gfBG@f$HqX0dO;teVBX0rQ(#?3*ut1YCjN+L*<@l~SI?zAf^47W*a$j>k)UJZeFpuFDR|n-6$nPDoxI;3Gc>$y)$;'
        b'3UDD{a$ZQ@BETO4E(SaVcn4tmZBQS;M!-7(9|Y_Hd<Jj@;J1K%fQ#pZ<gEeR4Y(HnmfaYV_aNYAz@GyC7VtyB(|{iV-fRlV`xr1A'
        b'@b7>>1)Kr`e*|z0U|l}Q6<{CWB)}&CCj-6&xEAn+f{?sl0nP;M2V4ZW6>u%!cEG)W2LU4rL-Jk*d>!y4;H07u93FzQrGv1sh|Qz3'
        b'rO;1zzdlF)d;CL{s{GdfPzC%AKk`&S`a6r*-1<`)%j>QpHaE|&W&AR!IZr1qQycUL_E=77p(_8A8ecgY&eQunc(j~n^Y`Eh;brar'
        b'9z3D^v$4lH5BAA{R9~BsXI&MfpRdY~H8Z|3obL?hAy+8pcu^ov7;n%2_?1&S-B%9QyEKR=oR<?;%y_WxV~c%dBF~G919>8N-p*oQ'
        b'IctJ>csX+1Se~xCBqZ;ZTbS(pti;EI{djUspd1LC=h18M{2_>E9Ov0ya`k>YUlmxl>v+4LFY&eKCBJ^dvDkb^U>{u1^LopV=cj%='
        b'm|t&@Tu1W0{<|N~mZ0%z^(#lkzXOYTja;Q}$g?C!cE<DgDWzAIQOy-(bOP`1tkSE?Xmn6H(LAr3(yRBiu{f}=Z{R%5r9OFE>Bo<K'
        b'{Yel{440p+emw8o8aO`Dm4Q4ra-Kb<-+i7=<UFqf&rvRKANth|d3II=>bFUp=d<s@Gnw<K%X~WVy|O^LZhJ6LcBXKiTgt9H7ifEy'
        b'1eO!a$8pY8c(5Pe3z|PSaUD`y7O3Ot_g}^^+v;49T;I&)x*m9zm0fwBZst6)?A*e6?!5-jV?jJ3Z_j$(S13mVWr2P0VtJq(#PM=o'
        b'hIF^y#LD?&SzsS{g35{KJRd;1uX)`*=6!H6DwOuY)*zm#oafRtc(w=eBygU{xmV}e8N`#w%SxL2-RE`^FJ}(tK{<Lis1Mfqm4kge'
        b'jrVoq+$+y*EXP$6*w@Kim;UG)JcU6#DO_i-pX;03|2a2kEeYb8&UxOS>yv|j%nfYMxS;uSD{uD~JY58zbNF46p}9=1?+M~b<vh~&'
        b'=<77jGjZN`=Sk;0hVQ{MgY(S$4m`5#Wb=Nr&hzPmzm*2|TWnAt<Zzz*=K1tnFwevwo?OoJbH8%7LU`vq-xx;*@%(`E?7K!e(Lp?U'
        b'Tt<)1ySluc36h=Jyqx#u`PR8RgVt^F!N56p8&CK7HOk2=4O|=NaGr~P<%}&4l<Os>fps(TboZ8Dy&SPDkjKQ=?FY+!<+R@#Xde`o'
        b'1=ejbUo(Hnd9bfH1g#6Ha$nmR&mElS>1*)lf_Rp2o>#8HGc$;1Dd&0j8a#PHJWYJAo(G=KQ(m7#?d^)db)m;^ZN&cS;5?Hcoy2*9'
        b'*VAC06`Us(c>eVrd3rg|9N-x<{k!q(;5@YzzWH-EgdG*^`}rC_9voBT*~fX7`L)Mi$E&Wu^AhKI_<Qiw^6#zft+;&6lI3mtTptg{'
        b'q5q72#)%4_zWz%^AdjmeP)6%GPiCdB4?YYk=e@GPau#r&>dGtIVkkSGuL+#n3ptPd8a(HMcouP<b=TlIAH=hm^X#nj&C^4bf$cdT'
        b'G*59K0rk47DzL9Jo(;*9?SuLtUA2Vs+*oyWo3Ay9=T6R}zXnfJ5D)HUU>oLDU0qiV2kAH5_dwgFvC7v6reObcZeSna9trAeJMg@u'
        b'_SvKO4X_(y*}9$ZV4(h9!+CnHz$4qR$w548xm;hZoM5>|o(DP4hAN+2pSvqa_f`b@b3f(%)?ekb#c)4lJe2WV6|37vel|I#{gCs#'
        b'2+#9G<}ctpMHxUIET_%S-^TloInT*!j89W>U|*l*GWx|ecpeV&&Hm2Ii7@-dG~OI2JKCUi8~3TO-)5Sx-fyu%`T+N|(622t2ikA+'
        b'o0h-ic14hkPU1WZuEC=T;=#Q#l+nA)SC`THAQ_#)+tXwI?y`e>ahUf;zjDR~*&!i8b;Er-%<D<>cenX)k1ymJbKy#L`#bN01K*>Z'
        b'e{h~ZeGi^bIM3JLgXdGuBi#PodA9PtPP*OK*E4Sq)V-U7bk%lVPXFz`IVa1`v$wN(`r{zEevy}Rz^|MW!R3?$%FaQ~^Y!gM+gMc{'
        b'xF14->W2HW=mSlwzPdhmI7lCy<UDh#eRHm&I&iHgL32)~WsvSnC5yv!KlHoD`mU-DY@;UHR|byHrs_a@=W)M#l*et=K3fmlyUXu6'
        b'>Z1dG_t@5>e)njTobbCxz5hqQd-O*?^}EM0{iokO`rsG+?y--;YJBZOzcHHM-zwXTe)s6_iGKI!%T4pUM?Wo{-{1JikS5~Ysd@JC'
        b'njf4vetb47vB~dSwa37mFD+o#ISAhic&UJRgc68*g{6UeNZ0fGt@HlhKlhF5*s;N@!M%mdX?d*37k7-y&7u2zao;6OuBV&V#Dgx7'
        b'5%<(2=#+Eb$ExeSN|AUD@jB-7^r+ncd**!qFa9DA=7Ie#8ZXhJw3^G3`F%|I77%Go&_1I28YK*Ns`9n>sPf-aYx7USbq20a;POvX'
        b'Q&e4MDi>>NtBXt(qN$*^tgeXE7L`{P)doc_D9W#?Dwua!e17@-qS~se+R~tSv%}Vo2h8|!RiCcJf77fMt~L#;M-$-5^&sznVJdcg'
        b'4ENn|?}7_)3BT~!{Tl86V((o5qpGgG@jb63gs4G+qM{xsV1faX@JOTsnVDolM)DXl69FHcOfnNPC7GGdOdwdQ0a2r3h3HqYrEQ>C'
        b'X|<IqR$6UKy|jha2U=~p_iE)@ZPD5mTeJw+{C{ijede5bBw*Xy@4NroftBChYrmgo?{oHE%Q0esNs++QsIUztQb@trPtmZ2XN$B^'
        b'S;sbMbBh$bmL`Hue8p$MaBokLpFyUR^X(yipg+!}?A>Bb&TfhBKCl|4zqc>c9ioy))kCOsaDak}tFvl=QhwU4Hyn}@N2IV8Ix@hf'
        b'ws>olnW}iWj^0>|A6O3c1W76;xh}N2Jk3?}%gRYCS&&>7ApjjuNcWwHtVpUBlk$?}K}OXnk|I1w9&#*hEH6<#=&q_qwR4bcYCV$V'
        b'XEAhwE%=>Z%4EI%P`&C=ClZHy^0dH3h>(e=Noyc+Yr;>hRuv<9YVmj%&Jc0Y@r2nTPLdLqyiKQio2q$B-XzcPG+pmW^bUE=eg)m8'
        b'7%AAtlEqQadvNhbbVea1s~P^th1m^d1G1n|-BDw9C5hv<uAm}QP0~q8c{W<@buyMxkyL^om(<_kPQ7q;R{qqFEwqLgY4s}PZ_t4e'
        b'5*o*^Su60srl$B(@2(J&hd@LyFSK$CdGyEW_=ch~xS$?+K?)w>eX16lu5si|esW)!HN`+M;SWi<fVy0;5u+m2jkQ_hiX*b5pxcZH'
        b'<@p*eUr8LZRjmBj4=+rxFO*>NvX9yV^~+fOa#nv0tM_=AJQ$OHy;@EzTxz<Op)O6rE=tbbtlYXN%@1W#x-cn1*Q1-IRN=X$N>^`>'
        b'pN?Sq1N<bD>bE|tXZ3i!=DooUkNnzLQW634HncEtGeWx&8dEhfFt2+l6DR4oJJ*hooLu?gEhQ8d!qr8;b1k$AQ77tj)!rNG4scIW'
        b'1`2asuEr3QN940a#W0GrSzL&j>gETVn#%BBH(L1IqVu7^y&V5X^HR>7c3qwEgQ;=w7H2R^6%vpy<;T<Y3SCW$Ghvhn!a5g^;51qc'
        b'vSY4@MS7$0Ob605yEqH`^ijf#D%nx<<(!eFc>1iW0^&s4su*-eqSRCRqqwJ2OppE&h2JV;4bH38=IW*sfT^+pmEbCLJos`ovb2Yu'
        b'lsplllfbpi(}KSqDdn4Fd$Zc5O^aJ<lTRvHW1Zdp6=Jrai*GApe)Qx`V=dNuzh-dIa`KM2#rh?X`>SG2Fa-1YjTUPF?zC6`4(z1Y'
        b'_0Yp&Upg^iv7W#l_N9k}eGlwrV~%yVw7&@Z=Mev)uNWL$Z^qXRj)mBN2XyvT2;Z<nvtRd~#k%$(@or{Juf_UkfyKJvQG<h)qouGf'
        b'zr<pF2I<rK#SQ--2XF7g+8SmN?7MY#JM24k_PY*QtXp;VTDWhWXK?U+D$E5Yi?x5J$bTp7Uk4?23irog{spK@+7H8QS!J>A`kKry'
        b'%ol?4b_)9?Fjs+2Jt*u}m`#YkR@P4=>>ELEJSgJ38|Ftr{jk&CYahy&1OKJc{o8Q+8EDdjBLC09{0C5hw7(1UxYZWxo(F{gBABOv'
        b'9+vhJn6Jj3^q{m~3A-P(Puhbpw}W1h_Kh$<^FH>pUlsNTC~i=(v_D0DQ3plR{u=C-K8y9J44(({xyb*P`348=BVR&0&joKwrLZgT'
        b'w-ENJmBN1w%zjXTY>yz!w}INE{Z5!40G*mA+P@$5vy<#QH2XuacUOt{_k#Zj?0pXi`w`f`4ZHavQNORC-M$O^T$$e=!mQoK;TJO7'
        b'NnVIf0%N0mJR}daa@of#Nxow@7tP!&ZkP6QfoUX}j4qzf)Pyv4g;sRIb1Wz%Vg>k((B!2cF~Q7I7SE)qMU}TA<pBvXEAce>lv(mb'
        b'7qscp;VdZ#UoN8Q+B1^wmD-PHiIcmtoiq6gcXd~&TZlIj!mR##imE99nkD7BN^!FCmU6H!Dy}rs-G>lgebeMAuha6!kt&EMC?x^%'
        b'+hlZ2UzMR-HEWI<YqI5%PIHr{d8xuRvt%t03h-EHTBb`(ltGf{6AcABf=NLwLRP6N;ziz^=;X32^m&?_6!R#OpsS}+NNkE=L!oen'
        b'-)2qmufMcHen^HA(o0@N(FycS4d|Aq`IA}W+LyTa8-Ao(FRBsQijjo(4lIA-+TEMZPDL-vjV}XNa}ncdY1Kq}yG5OG@fRslAZ2}J'
        b'NasmUQWK9*ibZK=PSlX4nR$`oZR2>>l42-DoEhgrjJak`nb)N57{%E~(gn2^5I3!q;;Ho|sfw!_^d(Wnsml0e=aim#Ml!Tj>86ko'
        b'17%)b5rTL|2{Kyc%ZphlZJ<g>QR1KK^^1*ZDE`lA8Mj_}d4}%tS^A3yX{B=b1IeAVkVi%L0Nb(p5_bmpT;-J_i%2?;)Z`%rXt`!L'
        b')1-n{4aU;mEvRWX!F;tU48x-e!w~9OL=LfspT*=2Sh{@B*&SIuOT30U_G$6%xofR>&wF^SI793Cj5y!^htG(2{O%itj<Eh4#rgK{'
        b'+$hewPrFH+bN|*&;=S<;H;HrZWBbK9_XYjpoO`5SoO9paFV49yStri9uUse2x%aIT=iIlf6X)FbtrO?mf4fecb3c2%#VVgFr1>Y#'
        b'MQf7aYm!PLh28Rz;+NvQl?K71xrX;C5<p7ALWK;-l*w8bv8vP|rtp<-s6*RD_h`byxkRs7j1*_dU5q;P)a2-?u_7G0K?vrMau|4P'
        b'sgi9)yzmzct&;M|{9!FmNqM<aI(dqAJ+)C)k*_jax;Hi?K}Hifly<XS>FJG=j0bENf_|?0J*Hqz5!dk3WwY9~JvMDB)o!QI4W*f}'
        b'r1n5Rm)0H(=p;0y%k&c!rq)!4KTLU6CFA3<&b8oaviQWK6GbC=ewgdR@m>;t6Yq&cNJXG}iB^4t_(`AOEGFABDb0>VbBYB6*T<}S'
        b'<_ilHn_j!{gl47OZPqfUio&Kzh9Zztt-m`S(UfX5VrJ3F5v8|}e9Nhqvn|_MEk1WwdrMHv<7$`Ezw|&>NRCfZU56^KK?<$ow}sVv'
        b'$XYMcKW&AAXCWs~K6NPrLTI9>W4>770Ug@TT{vs|XSFcGCU3~``odu2xAr3mDVjsbygbdi?@H}%u(nnW@r#Hu0=;WEqFlD{G9imK'
        b'OzXoqJ)gQl?I9}K3f}5^;k%l2R81$xEcLRNe8TdnGj*V`)^M^K6@Jx9Nbg&b(yhd7LW@5B29~CDE;z~`=91>pJ#%>;ej!%_gN*O|'
        b'GosLhdv(cPv4+e1lhUGutRE7h+{xF*X&pTokydVhSdn_w)H!6-Tylw7T44TQ<uh%1Mq7f>pkJ$WF>R)MYKn{;g;4jAnmV<sd^sR0'
        b'Nh-hKB4(1gLT~S(#Y|E}geG8GHdJQ4#7RLyT+9&3tCJ!aWo{O~1lh+I##zPl#AL_T2G`<wbA<daF8)Q%4J3k+ua(QyZ4dQAnm<RZ'
        b'2EOtSM^0A<TuqKBd5WHmq#Pnzabbl;4?~i89-c|El7d?O^W_QUDB09vVCrj)BvO!ej^22-D*Y(Q%GZe^;npyp+_mb?>`sg4&Y4xN'
        b'YB<WK1y)tq!QVp5mB03&(+A*RAjIWC**(+;9PjkB{?i6`@<E>*Qz9-^D%C6|R4MUwS*Oq!mC?I+#?)TG#X;-tF_TUMAvj7~9P_n7'
        b'uMj^flt!gAjgV?o<MHs>SAWr6NRV~&Dpnug*DRBw_2|K@eiZ2D5+wLKK?ob1r4#>~d?1mSinO9Nr>bK}DORRhhonvh(zT||?fOlJ'
        b'-CMIj`*KAUBb$<Thg`B|iX$IIjq}UZis$nRwRCr=BayZQSNIw{xfIc>$<)c`nw74?SZr8lsoJ5nuAW*Gs<YbjRB^$js*Z{^>e~Ze'
        b'E3}Q3-x@{l(uDY@ynIN?#^+-7Njzkt3$=u0YELwg6nC9i9ZBEg2yw_sQHA^?Agf8At9Tmn)kteNxsdD(@vFr>7`k%*;g+h5Qp!d*'
        b'&bvq<iQHXibx6W=<Me?g91`0NeV3=mJ7OWOoI<?t)$~+R9@Q-!Ej)NukT))ZLJm2;%~2vGjgr5_&}FSxN^9cdIh2%+&z~)cbe{gx'
        b'`oZ;LPg8WW*wgrL7JHiibF<jfJbSa))8uaudz!ipVox);LF{SX+aUHdvu_c5nor&$_B6Y15qp}Gw}?H>+*`$-X6>zFPxHN7#h&KR'
        b'w~9T@_}j#uX3A}1Pc!c}v8P#io7mHQ^EPpJ_gA-xySw8C#NFMc1LE%P+5vHQ_t1d2yZiotxVwAV?c(n4vfIVo-CJ)LcXwaBUEJNx'
        b'zeC*JExkkB-F4j|?(W`vhq$}@)jP!9-M`!+?(W*|6nA&McZ$2a8}Af%cYl7TxVvlKDDLiFyiwfUoxM@q-R;~c?(X&jNw4{LfaUaF'
        b'ccZw=Yr0F^<)u9y-Q~UTE^(Llio3*J-cR2p?(%;1E^(LlS9giKyeIDxcX=m%)?#g>^De+9(nk+$rn9_2FP()3eh9n|cs0G>1}+8u'
        b'<g=tt8TAGfO4=)=vi3Q^9{(pJF~U%okZT(BiCNgkKaTl2NUkz?{H8qfsWQr#&)?4FiNH%plfh0FE;`M}g@*aKRw^HY_=Lb=Jtr1i'
        b'#iU|HF=m;Mda_SS5%Ea@slJ$xKT9=6q&widf%#;2_r;<;GOsG9BOaHW&?i?WGb&m9k>Cr2#5dp+rg-M3MHUI`B3_M}z($+-I=ds0'
        b'06E|Z;!Daf@O7qI{Q-ZJ20!OZR}wVCDAT+OeSHGf2)IFjUqHKn4gtLaRtZ2(<O74(nr4gAtcM(`k8bIlw5skTAJ5kvBsnfV{tDJ7'
        b'KE(@5g=(YFasKu|<%s!Acw;^;9YS>y7A^opv?c#e?<3{gD19u5HVF1aVrytV+N_-mo3vTe-9B}*rn`N{W=(hdlbbc&?UkD~-R+Au'
        b'Yr5O(Hfy@u-J3Pt?bmG9bhoeAtm$s=-K^<uziqRoyZv*UHQntyHfy@uzqMJ@-Tw4uO?UeXn>F3-zuv6rZhvpHrn^0FP|SP$9^jy+'
        b'yS;2s)7@?z)O5Gk4~lt^eocd7F68I^2gQ6yzu=&l6X};26!RkeZXOhKBmF)zDCS4{eRfdHk@UN7P|TC``_iD8EBSY*&0@Z!-@}7q'
        b'&ZOUCgJRyK-**Sa+)2M54vP7cpHLeVb140u9~AQ_{q7kQb1D5kKPcu?etvdP%&GiL=%AQa>G#N>m|OXI&_OZ3^7EX7VveQXzCkh1'
        b'((h-3Vy>m%i-TgmrQhK}G3V0n=%AQ)={Gzm=3ahp_#QF;@_u-an1lJ<xqHMs%=_CtVlJki>mD&5^E(mu2>A;9oYy@<#sdAK_Xs%)'
        b'^jmk2khMU+AB}%@eDMzrj_1ZdH~yXP85|`=<wZw+U~nufau#g`E-q>=D%)#tTvK#S(U$KU9M=|g6g><K6a|Xb0)s{2A}jo@DO%6*'
        b'uA<Lz+*b5;j*l08pW}g|7dgIK^c#-v7M<W|nQ-<5!t*DbKf#RnCQiUV-~|&VPbdXWnJ{HS7qE1~+zF?UkJl!=HsJ{D!^~hb4b!jG'
        b'-rJ|B@?%`hVuiv*$IMFOsxKK-?(Ako=R1R~3h<-&#rJfQ8-hup;XaEs0c;17oxdNwPdfv=adzr?{=%0Hj<tsjj=6`#chrOobGI%`'
        b'v~2V+>OJoVWf*rEbC)xB1#{0~?zzl8kGbbFcO`RIG4~a4B4@al!$UcIl*3Co{FK8}IeeAFTRHqyz+VN$1Ai5Bn6r#I%bBx+Iboj5'
        b'ob#A-K66&G*=%+Y`!&*_qdWSy$7FWw1?>l&qBDh{L-MTPVTnh8W;5L1GH~1vJPKZcS-4MqOO$W_k<>HDQfM^u1v}$DS~W}c$lW1Q'
        b'unS(7zk5~(3&x{!Dtvk->+X!tT-4FIV&)>D%@`BCGI^m=mKMQm_(KGmZ~Dll^Q}2_keJ-lxlB{CrMvKq{A($v`R6<EO#ixQc!0Sx'
        b';N}ZQS6395^>xahGFvIm7Sqg%8FNcYNT+l**Nnu)J~h4ISZS>EcO{FtXf(%ZN)^whGJU#I+#3ofqKTL<QIgHSl(RKWnVVh{VJwY&'
        b'^nL*Ou9!DZ=R$jyq)YkS%DGi@=FhFvdGIHYp7c;&hK{Z|VY%g}6N0L9)*8XWiQIT@uy_zHC8~CXcry)V30F?GcC8YLMX`g7D~l+^'
        b'wD^K)fdzaEwLqzf#A3Zsz8MYCiN6quU{*d|);F!MRH470nHJAy!}2$47K=v}t1^d0d2`Dwfs@ffBrBN-SJYZDWz8p?5+yS$N+?&O'
        b'hox_8mn*!nMyiC=Ok^fgUXohaCX(SCBRS_mRinzZUMipP6$rNXu2{goy@?o66I2D{qnKJ0?aB`mO;;M~Jicb%(w63?hUF!cvYx@{'
        b'wM-~6i%Kxch!TmCEV2cPrxy!-ktn4o-)wi#&b~KHO3rC{Ncli3AvP|En)-JX_LPWPlY*b)QA{csEtyhMC;vpqk0)yB^Y^){QYt1r'
        b'YVm1N7bqj<mS9pXgFXk!%tfQ;s4mneREw<&%GU(35n{sMuD*PVU~(~PE9&R3gfN<EWXJ|_wzT+~nw?GFlB}tSQE^5Y!W7;)GmHPf'
        b'p+KGb#N#6sYQ#t~{cGN3H+RXe530=URnxk9XMr+2>c3hf=d$8yz35ugdP_$2o}A#$%zJXW8`-;>Ytaiu7boAC<WKLNkE(3G)f(il'
        b'k5$DgVuqyJE349ox)MzvJ>A&2`a*Gf`6Omk&M8%j<B3>rM?y(@no&a4P?CLeXsJz`90cQ|r-30}!l!u{d=!9Ncmt>pM`23@ySp`8'
        b'%)c5@g-P6|&PxV|gl(n-qS;30o@RvyT1e;^DK@TELbFnCG4&;LPp?R@E9UlgdYcjMNV@S4d@&iC7~04e^Qnk7j{P*9tmdOfji|G`'
        b'H{PXMXqr{c!I)ncqX?B6Av`6EKwmV)9;NV!i}x$xk3U@Y@6$KgUs-kRs+B93`5$exe#+ujZr=0z+I!A9dgLp=_{GM@{6E|Ebl?jw'
        b'z4-H6`(Do<n)IjdeXoHp<?1|AU4VGoj7_7{AlAr<nMQ{VR0=8t9V|6Ej)UF+?E-BDT?Y!xHaeb~CCpPnZI>e)cxK?18Ae9}bg<ay'
        b'C@V2K3P7*G9PL^Y=dXom9C+L=UtNRUQ}3&>*VH>J-1W;nzB;?Bfz5W+*3G82h=l2^?QDNE>g$ct?UC77y80qmdqkqN4#fim5jC|o'
        b'G%(d+MKIx$pCWvu^pd}*W<8O3$k!bV)1!J$MMeU2<)u5~574_2F(=H9$2#<EjGcHFQtZK)&_%?p?Q0T2U%0o2cyn2LAfNmU?vo!w'
        b'I3i1EY5EMJ=Kl<{6bf{vICc4vsaP-}9@(ib74zn!n}<W_dYKNif@7fwI@b!yLveD6nKd`!OTg?E(NF~G5%|Q{D%R=mMh_mrKYCUN'
        b'{PVq;`Ywog7>8I!b*}IwBEA*fk#>JKaY)d2DB6V;m)qIma@YGBn`>JeoW4f;vXK%HA$%Q)80~AMttS%b<s+ZoKBn@d`1drfl%^U8'
        b'tqReBB&<R!=t-^G(X6BjVLnUC10K4w`Bo}EXLcyu(cK#eavr@gjrqE}XLT{vh-ob0lkw?fH(7M|IkAi%u`^KT?pmGf2r$Obdm=qz'
        b'FGq7(x8z{8QM@W3=lbbaJ8Np4o*E1@pQqm5;;b#1K0Uj0Q*)E_QF6M}(NkhR`c^_s8($Sj<{D<69qvJ`=_G>|wJa3(tqOLaDuVG2'
        b'pZFBQ=v<s&bVkrUBfYT>v4239c6!{t<|U`g5&xsML@d$4CrZj3Dm_A9HZer8CGJH>?TGf`p^TXO=xxQ~U;-PApsThxd#OXw4nFFn'
        b'nP!}5$Fu;Wul9%|8t}HXI*ErZPJAVk-o!jj`Jiszmq70(N%u5074zq9i?_zN%xiD()wMXU^35%4%$m4(mo5qyk8~sph)DUEk26*j'
        b'D7uWiQab9xfxmw}YG@PV&DfT1Uxf!rO6^itpHi1Re~Jkq#I<O_BR`K8=?+dAErY6-nGQBuv|Ma@RD9G`#JHP0g^3wb&R?>z12nh9'
        b'f@*>Ggp7{b8!K(C;g#XY>M+YS;8#n_Che>to#Bc{um@lseru1P3}f}H9i;MGC`e;V{fUk)VJ_DlLDuuj^n6E))4qgjIgUw7lWOCs'
        b'yTW8_<gdY%KyOb}Y{!_3Z~DaNZS96y%3(?IeXvv<*W;fG{eeJ?K1cFx3#}DHaf+)LRB~3n8fTQ29H_p(H`>~NU>0ltu~}P6%Q>Ok'
        b'Q1=lvmi#Ik5XqsPgu1xZntxIzMBNGX)!5jopqrv$#7VuZQTaPm)!AGvlFSeCKo3Ky-L$7y#8bj(o=})JI;h1LFmW(ko_ruBy`C0+'
        b'R3O-wSb%&u-8JP3ehYZC3ak~W);X!xxk;<LM&Uo^_DF-hOf{6Nh6>d%M>Wh<4f9mPeAQ5?8md&o70C$8R71IHs89`aRKr}=Afjd-'
        b'dy6nQm(|qRTRl!PTy3wdZD9=#=VI>E;B2ZDhMMNqCa*%@DSq>?#rj9kaggB~7Hd9eJZKVV8fX@%5@Z9pKrNtaK><(?Xcg!t&;V#N'
        b'=<}ejfF1@t4ss?Z1!|k#uvlmD(*t}0k#hyC(nSfRPA052(n~KAG=}DNWiS>FcI%vKB2ooA9X3sJxoRhRZ>6jbB$BFIk);}UYuTu-'
        b'<*bHx@T5BScDi83RgNj*lN;}Xq&9$e-(Y~bx=B$<w<|2RW|Y2XO`N_8G99ljh-uErwMjH!pwfxzptRDb!}4UNxT@t2KhGtm!dkv)'
        b'ajdx}7>l4+@<S|iV}2Ee&<doUjLhC0S`ns?$0AjCtsNsOEkU=dt`_S~!4=+Ib=m!CT=M5_aL^g&q#1)cR38#a@scHTB%+l(^(3Vh'
        b'vl>wfgJSCnC3NX0V<VO>9_gC2*F?)|N$h*HTtJ0@IRfSim?vPqfXZ4SkNt{oTCDY;c2FGjS<nv9)1bqkagSK6Q$eL52k0u0AJhd}'
        b'3)%p>8<hJsLEB+|40HhWpP+X^AA-)>CES%=nqQ)Mu-AdEmHaU9Gde$a!F(_13!v?wuYq=fo&bFxbXNXZ`3}sx^eI2MfGwaojK8s1'
        b'wm<+=)>>!QG`F<0y1mX?X>0Pjnp){fFxC%zam<Ppdc8fT!k17=lqfB}JLwTJbCJJ1W7R=x$XFs07mFggavS$^Gkuew&mDA*<8-T6'
        b'u~4TK6`cm)$Mw4C8&xn)j|!|q#OfnJuYffsT~Kalu318BHZIGfcmy}T!Yig|)fb_(H7j9yjukakSI3x|5_||}%ulpINcUS_R>o$`'
        b'nBi<`X>I{3b~;3fN1l4^fnU_Z3KS2h<e6jjfHb`l7saGE7D0O7kYxBf_;Dx}<*Q+rxZM?sWBue8m8pKimgJ`UfreBPdpiU6Ge(xj'
        b'Orm9x7at}!zJ@DCtJk>}`)GORwR@KMmezWGURR^Dxz+3Qlq!4&S&|wKPvc@zOXn*a$)UW2(U+;ybP@U^H{7&8?DN(*#ElVe5DPYS'
        b';}Y%T1<vBK${vk&%fn;XEYOXXm=}2w%f57H7c!=ErTl3d1G!8V=%ZH}@<l*$hs5_(#ZIrs=UMKd3Ti=pwJdge%Y4q-#ZI5A$=l-d'
        b'G`F_YIF-v4zLP2Ci)QXn*I-}lbG6tTm9+{#4N|J$G2jh#taQa=_5AsT1=w_2wDV0VcB-YkkR|N&Rmeki(7t08^%PGKCE=BUy1S}3'
        b'*c<fFPKuvk2XDkS`4oBO4UrLO=Az!dMsZ6hzSJKQQVx_6JT?dgEz*_s3KU#rky5O*I?&I(Yob9utCWcrMhUn-{=TDlRRjZXMhQCD'
        b'<YI(~_6kS!s!^&RL_#0pl-@oUwmcs78wuDW1YdZ%;FHzheQIp93XXIZD?A>`H_MhDCM9C)3ruM#vZCPA6?Uv4J;Af}p-Xsl8A+fY'
        b'Wd@|rav5A%%vBVlHzMjWdm&}3P&?^Mo6#t(TJ7~=8MP*<Pm!0WSV{3+p=66+Rsdoz*F{D{5TnsUizaL{W7PCPvGdM|w@iz-kH$*e'
        b'8=>B(HBU0NXh%J5UDNsnnnTOatUgb$#~<y&tUjx+u@}35`bamuL0b4X22zVsBaVcTO^oDX${6>|vQ;;K87LYoE&HcyvJrEWF&?Nt'
        b'$#81TQ~!_`@=8WXNf+h}J4l}^+!drRjNy)8v$}&Dp()i)Dl_qq=%1^&=UOg|h>4K$)>B<9(u4gTQ>Q3dZC?M%G>_7@I3o<#Clu=N'
        b'1j7N<AsSoN6iI|S*JRGB8DS)c667s~<a%TA)C99Th&XEaHG*tBF<GX%w20TK^ave!f~TilTz%4_hC4(|q`_BgD-v4c(Xy{f9o&qs'
        b'Kx*iE>eaOMMsPeui=%u5h~|`jI+A|)LtFULJ-^W}`@~DVMGN`y32C#6kNT?P!iB|HSXI`EpHh-#B1RtgG%Vg3T9pd)_&)U+FUH}u'
        b'-0k{|(ZR%Upw7m%9|r>zrh%?@@_sKgL^pT3_-&kpS$ZF+I<t?{G`C=+Sqw#>RMdGdpnF9b?Q_y8cFF+Et>JcYq@LOmRg4FDb1!dO'
        b'Z3g5IpQhkyY=t5*(y47lq80PBWU|e$lSdeqA1MIu4Nbv5KHbTzQWj}zz;jr`&tLE^#*5gePLDN?YtvurUZ3oWVm1rL>x10^8F=z('
        b'17nH^2ZDX_p<q?YHI5jjoX3l&a*_#lb9*Ql;Ctq4mGqF;Q|50hYi;12Wjgg09#Cs4>K#<!n7vme=Yfo=b>z`VD@!bx`BN3ExfoYS'
        b'>Qi?>syDtwjr%$@uh<XK?No+|BhecRi&mOhPEW(wDk`hmDOyN-I$I@Lm(LQSZ2GCLw>!g`Pmw7RVNV<q)4ZM3|H+%<qGB`s2tJ=I'
        b'>LM|<`*LPWkWL{`+FFMfDRpC;+8j=DNev?@^2H`Tt2?7w@$j?O^`RAA@U7;9kFiEKdmzh?=fR~Oqo>ZA?E9$`2l8FxZdLP4dPp%p'
        b'ikx_8gOD64sr7^hf?)7jg_=V=nfO3XS{gh_PyDIHYfCq=yF=kH27iS5IpYf-tmNIO*+{?@=5qi)m^Dhz;#&xs=)FBL#j~nI?J7*f'
        b'MONAz^Cbf3pj(faN^})>QukM`S{aM_ND|*oseIZF6*H6Ef5cX~#Tz*FGIEWonOAdi_C@K|PcnpuU-;ryYU{X6P}EU!lc$NaH0UUs'
        b'J&Op;6ni#Q$*7}j_S2<jNR#WEE&NFN%T0?XJ-p>3#%KJ9c2imz(uIne)6y}g<=2vy7gL(M`84%oPODo>T6mg3>8m*Q@qtjx-{TA5'
        b'Pjc!F@U492DCr9Nqx_Gr!_SW?oF*D9<*;B7u_@D)IVEEKUQ7-;JH@EJnBX7RXf)y(D(}7WPgud2y!RI;#nL>4pWb&*$qWrPf8S7Y'
        b'x{!2BCwX8sSuB3-B+{W{$Ov^D{>eAPgRh<5L1nU~SOuL+PpSjens`Y<=LUF1(pQ^|0D_^O%&d3X-9C@&n(XHYQrk-XaLgH@06*Ru'
        b'?(OlBJ+5&V>baf<m&faKHoCpbi>Irfhv<3`xt8!iai2dH^RG$1RZ2~dseyP9dJh?lVH&$Obp0&RC6Ea{lUDv&i@{&lh>rw5JRQ)M'
        b'zTQNrJ1)K!%kbFom#YykQZf=_;`|bt-lw|x#0Q7Clp`(G!x)k>#ch=~Qp%DXyZ!sCS-%|X{cvM+M&BUEeiiIL)!DCr{bxG+0@$C?'
        b'**^~ZvpPGew|uU;@IG}eS!gS~@44!uUGn_@eGB3KJWoIQJA6(XDaBIn7J0n(nkBPqTkMUjb~e2)BiWM#P0dZd+D5yNJGFRg2<R@-'
        b'ev8#y$XI@!7Nw1NZpOyuX%ohh{o?#o!9>)BP2{H$JX2okoYq4AiZr?2Tvvun!>IGyN&Zj{J-;jc)m3^w2nSbphuUXzmCN#-c*>w}'
        b'4NDPTT!ssGrmO5zl3TrmZqHB4(k{NUNLz5qqf5k1ZhOVD#+Se*J1*aB`g-^aiZk^cQ+KH{9L<`dJp3wy94vhM#~HqGBzyyXmD0c4'
        b'_N@?$2Bv?%on(q|;t*hXRZ=Z3+nHl_?6}$J*aZv_g4Ti#g6;)91^)gVO`h{hFc)kvI(ppx6+v1-%%U&Q#U-;a5qpB461%%%k{(I6'
        b'NX8phq%97I@zW(_iy|VdTJSeEt0Nlag%8GJ*bu>W!2(LBQ8+JHKp)zRC0ibFn^BtlilUiHSfV>V;+Z0O7DGj<8h^J>-XNhZd^WyM'
        b'GKFyF0DlOyi*E(yO{^^sQ~)Xj6@ey#CV>>tR8TRf6jTP93#tNHK{ik=s2<b+a)Z2}WuSD?+1=npK?zVFXf3E8v;i~#+6dYNx)-zs'
        b'v=uZ2+5y@LdKk0|v>UVs^b}|>XdlQW^|R5Pp{wYA8GbDiJrcbV={K664I3!$d0aOo6BqRIgnCQN4E<7(m2Tal-t!wc!*E7jIDUWX'
        b'48xgq;V6zxXBaL|7mn*rIKyy-x^P^_;TeWgbm3@Sw)G6d*>vG(ejPf)aQ(V)v@YIphT+Jnh9eI<&orD-3&(XHooP6;7LM+}?mE+O'
        b'd0IHSE4%wl!xd`b==s0rOv5Q!IJ$%T)R~5}Y2oO;?%p#E*RO@6yS@9)G#u<|IO?nW&p4bh8IJrubH?G!$#68!96aN2dC72e7x|?#'
        b'4p*2AN6U^wXB<vRhMS<<7a4UrOZ4Yg^JG8Hm;I|iw)@$#Jql$#oh$QSB;y_aC;ljJ6*7PGvYZu&M?><toIE<tPnnZYwn$9-UaUH%'
        b'oIX!-eLYy^q_Oxxe;=2`lIFrsu+hDRG(LaMX0pY7hfJ?&EG$IQIN@L)t?tE%%Sco#vPN7TXf+}3O{yD-<i~h^0KpfE`{Mp^&?h{p'
        b'hn9*<^a*uDduj1Evz$c|UD)L$kKmRk56sdsqFCoj->KCMP!!_ETxV~%qf}AXp^DDG{4}6@b<59jkdt=eH#JLaa`9*%3i;c=ntCT4'
        b'K&MMuULW=iEna6WEu%%0llid@EuZ2Pxi6$1q>77L!R9X<@Fg>=3m~iOBZQz8u(;P7=bel%8`1oo9pMDFaN-*=edOSW7U`x5Kc3QD'
        b'<7;ee^||f*5P`UKQA|PO*V5l`<oc2<FZ;AEAQGnp=}>jnl<D07|JpJ|Jv%9u{aos(+yVHzsiTstV?+?8U58e(9?sM=)I{Pe6rn9J'
        b'9du}<J0q@UUv1@Sa~ny%dFdf1x)u_OuuCpgF1~2ew8>LGHnlrQ1BcFN&=t>Mc$66V8G9b9KN_NKRa#Iwi_qR1SGOBtEQ$bPbO*y7'
        b'u{F^|ri;!lX9&L6#x5tsPl}K{d;aog<jm;?N}LZ7I$J{R6b+SY4r1H1CPW`U;)z(eqbFL7y$5PI(N#)Ey=N{WBW?aWLw%VXy7N+!'
        b'JuC1^gd`J~-{PcKfk(?`W5~}A1Xs<Lr^v-KWXo5Kd>{3SM82yZgZ&lkyL7xW{T-8G3U(MB%8u0V4X_75YeAdR+;;BBOsfh!?XYKZ'
        b'Tq@H7bUc$LvT1?I`K+;a9`n@O%jpkMMa5hW^X3!Gsp7VI<rVCKLqc|m4bRmt9TGB4%3!|lkdSqv;90xrkdT2g3Fg}l3E3z`FyDMg'
        b'$V@4;v6R;tf6MRxcKE;dXV88ogCW;sF&K<Sqse48TTEt?*}@d{S4=-8<2O*4`ZFhgl40jRLzbU#ckrJv%a2?Y_P^tIsnkJzjnwmd'
        b'ALwyfi;{dWTHj%TSO#h`2)~nLm`l=dB;H5$fAL4~-{N#Oc@^=7Sc&&`2$6woHrMJB=NIcpKyaMI9nEZ7JbM;*kcUiX%F8!1gWa9t'
        b'osD?WroL|rwRg-GI$;PB5jrV{-`md^9TR_QbX*MT1APbfCqQkW4Iuk-M#ne6SAb)l6Lyt|KN5{ebD#fQCjXwFjvfb*n$8aCKRx|y'
        b'aZp<K=+e}uulG;p=Rr9?!@Lgq4QM*bTnBvWS)-%lS%G&;BJ<dTM#sLRf-caRiC%tQGhYHX<pp8B2za?Pf8s^V_h&%*c+<)MOM%DX'
        b'?^iz;c9qio?$E^*cs<o^&u?VDf2;Aze>ZyC>FK|fmj2fy?`@gxk0d_&E2ATV^bfwNxl#IGLY*DfrN2O?PyDj9U;32kYN}(Qa3^cB'
        b'H?gok%*x6u=FFWpzq0BIe|twD*r{XK9W}MiI_ABGEpGI(Y2{_t&b+*A<`wpt*Z61NaQ(C}XKA)Zy6YdFrTfcfb6BAJ%ckd;9A1;j'
        b'u^hA;^q$4!_%moLXfNn9xhBV3;9m!H<_fz?#2<;AY3{MyO#btx(c>Ue(>W~tr>CDS4od5JU7Gsz_5R5`)@*V(K<|L2puFv%^)Met'
        b'y?i-G;LjwH`J#N2<CPhLN_1wTH^*q^S#T>GE6kSzKQ7JT0+S<g2BeQSoqER!%s<QI_`_Mku2Q<+-MYBePD*uqP7(O~$r{f!ZS=I$'
        b')BhkX{qGbA-YJ>x%MyPw(d4)d=^wdNbEEXXi8?#3OTR^?PyEx4oiN?IPOM=~{-%HE6DC0BKq5l7z8(Lak20Q657z!2;z=gn^^okk'
        b'&!~EQZ$EV3qc3i?&UtX>%O88+b;ZI5kJWy7&I1)+yl><4dEdQuT218PKyl9geAa)sa?QWlYt9c_9)En#J$3JWQ2myvxvH_^;<69w'
        b'SFgXu`h)mQuQpHUmD1g$Jg=$pE!1*>wz~xm{F}f}9_QG<VV0fn;JF<fH~jKGj=^W2B~*Mve2sr(RedGl_Ioev0ovZ&TDBdy>5_d<'
        b'{Q@|5`g<!2YSetPp+mPUox7@r?QdGq^TUT~*uu?iZ!G(-8r#Ol`!0TDLaqCcum9qW3zyUmzTBAe{L%i}_pkh~pBQI8Uc38?|GuWC'
        b'@9o+jFEu%idC}KE-d2<2|G<6^$O>u$UA)}nxE=gc%P=mN3A;+fABo7X-hS@#On#(w^f-vrbo!<L^z^gEL1{&FY3kG0`zP~5pw~eg'
        b'uQoZJ1{qQ2DZnkrXZ13HD<zTnm)Dvc5BCZ>qB9e1)7gIy^RerM`Hw);^};;w6PUx!fb{W>L{G!t-M%yPOJrJ+YTvX{;D&CEHzRuH'
        b'@lpDpPfLH5<n5Ma7?gN*hskj^(%=0_&5hFUL_OWDOMi>3L*k!q-lA9GX7!!8{J@{98j>9K9F9@*Y{{{xhBVK4+S}{2J)Lo^d8{SJ'
        b'Fg9rzJJtllSpG{I#Ltok&e&X-#;8vD#8EwqpGjrp2}q`ucbZ=={u?>u<mTmC^0W=7^kB~8n?*93$i_Lspm)b+6z*imgPGW-y#E(|'
        b'`TYEZ3GHTKIV=}#F^1){v8;fd#m;8u@OSgGhOn0UqRHV0Jq7yk%O=N3&<@ak&@J0cj(5Qi02{XnyGq0#i5k<~Z`hW}|K%4)kAp}}'
        b'=ZN&5o_@ACD6L=W($uG~_fO{WUotta1RVp-KzTn2x&vkg{|^oc{P~a|GGDd>>w)hHs?wQ>-u;SZUI@3^2ZXsA*dooheAVQ*^9)EI'
        b'??`m+gC@so51yG{qUJ}^c#jD@xLf1J_MCZql>Xak>Hqkvf@hZe*JW8Ac*x|q2I;fMG&f5B+o-eu)TMt!)*<mvH*dL{JuZ@sU2~fE'
        b'7yr}U5B<dCn7Yrz-&+>_hsAnqk;VG83r|m}U%_aewtH$^u2E7toqOu5!B?JtL5ShqJE2<Wi{D$#&N%>b+1SrMXM@?sJSSm3&(3~7'
        b'+YY{+mABiO=hJq!;0`<d*x7Yof!iZ?cH>iUKVWA=FT>C4cJ}li;P0fJ{R!n>kndnO7djA+gB4xuVAp-j!5%1aAWjFHKi|P_v^v;N'
        b'91g_q*pBRcKr)m;VUoQ}dPU_oN0MQDie%1{>|c`mOfsHH_C4rTDhB93NhS};*9YBC@2F+_Y@*r${Z*b3q2=*IB<G!ETa#>HlFbi#'
        b'f>yCIZIUxgjYbE`UZf*w^1CV3Fv&!ITYfvGd<@F>V1JeGw|*z>-;()$kYr`kqLyUE%kP-)$#|ZWW!wOIi_T1tj9d`Ob>0o~fo_!f'
        b'CppNQLBEh@swa;$ACqA>$S`-3%w}1i#qu2>y;D0b-vJKG^3x(<i~QdENBX`hzxm!N-x<>P*B%*`aK6mX^Rg{|ChLLfj%4E3foMa}'
        b'NwTeFUZ}1}rgX0i^IejSFYD<|(zi-7_~jwRTv?vKkRDxn2Po^8;-E82CuN-9l6krdbiG`wTrIzIm&tsblJTyT?R`|{`ziSu{qwTk'
        b'=F4{b8p#lsbxi%?6D0crbdiidDErkdG7t1Ue2C8Y$xrZi$$C8`2O0I9xGZzI>_0iOKT}?RD&2R24uI(3)ax?O)SoxXyo>XgM^P>R'
        b'QHd?l9JDgJj{9=Po<`IMr!ck;Rq<nFv-W(mtV3#(*MqaC+;sU3*4*og=1l+UI_vj-cJzjU+^Do~wl+WMx2$;h)#`~eYrQ8Yzg7K('
        b'_t(8RHvUIx|A3lt2{o}NafK!*gMNRqSogkbv4Y?34~X-<#4ZK@5cmh*)#S_b(+o#22ZHV$Yv!~E=33wuU>m4!taeVX_$}<a-pce_'
        b'_BPfv;P<^H=F&K6CP<Jryjenl^|c&)p}_Scib4zY&?cPwqc3Hl7=26)#dsJlr*`^up%aUdSM7Wvk63(SN_F9(^$ysP`$*|dIM_|='
        b'<%cZH@D(ggzW};7ml^KLWyZVmn6cl;41Ffn-o28`&!u$9Y*n0ftsbY((Xb@z$!9JPD=FQI+xS=hP+|?rMdzDIG@NyzQp`^+i1P?^'
        b'-dcQ(k6(*K_+eyarZSojaY$a7tzN6sPA9gL0tqhUKnPhQ8CgPjaC(O1VTj<0EKXAX3M-AWHXEoGv<!3|s1LLjv<0*kv<LJQ=n&`?'
        b'&~eZy(8N!%wn?BWkQKBHbRDP<#Dy*}`ufae6Ouv5ZS^%e8<SR7)7AC{SFO+9vN(e$RF7wHUDr5uv3Y%U&8<zfDI8C$n-rEiHLet!'
        b'kP%r67|l(d%v5SxYBG3NJ6k-i=B5mOqrE0IL#`&5r(TzO)72iI!>&t(7~~Tky)MLYO`7K{#RAv6-0k!=x;%|`Z%uuQON-N9>*G>L'
        b'(_?WqHMcIV_j%m*n$+ag%s1H^vpdw=o9HfEYBG(@S37xore%1EbGgsk-0W*;Zd#n;z|T(9(Mg$XX{5HW-lf6WwAfppRva!Tgh%N~'
        b'aY2w)=Sb<dct@ztCg)PMNwc^v^LkKuH7(gnOK!E!k=<(Q7LVqXJv%(H?7dgk@aTO;N{r!6L8VS}Z1OsryuMmjT^)*?;zq))7xUzo'
        b'yS@7U-P+(z?Y6|=H$teY9j?VG4#}2lMqlLOtn{w6t?mX_4O-jRV0SnhQru7zPK+66Z5B62i@m9)-bW%&n(KV9EY`Bq?6s%nj~G;R'
        b'7ZrobT!%EhDb5~egR_Pzv94Loaf&<VP&U)rkB4ovH#8uI8tOJFE-lRs4GudAvdIjUbj#l9`NM_@5q`qrt7-D4Iupm|@}!O<;nL!C'
        b'I}u&2&)w3jwMR{JtxG=;w27d#3889vCvlMI9jz<W+8Z&jYWZBE59}g#YCQ{<kU^U=xeJH%dR^+ObEQVWIcjIl<jNys*&LeP?sNxN'
        b'U8=pYxi&4O)Eeh3bdIL9_^<Y)#iN_nMKqrDLb>f8&(h|WG;aFChBKGimpD@^OR$?;8)`*UWEPh)>8weM2z&N44pm~dGE!}2<5Seg'
        b'cyn6uyvr~>c+kb0m!>+jI2XG--WGdHTGrj-k(9~xXwP?GQ}fc))|b4D_LqG9QXuIyWzitHsl!2wG<9y34lYc9Elu`}0M2DDPevAW'
        b'U8>eC7BH<X&J-SMD;qnxp7DCM>S}aiprlj*=cM-cRJV-ENpgi$s7(F{k;tb>rUP$i-B^+iRME{X%Tw8ClGa9NQ(7#}Wi?Jr7>(Z6'
        b'RDOE@=S*}h*`3qVysFjNnl?1_e0?LUdBh}7PqWm9RvlZAwlkYsGk?7KnlfUP4y{c~(D+TMZp$b{Guo=DRyQuV6Yo-W`h``pr1q9t'
        b'?U9$&IhA>JvsXXoij*7En_tujP0*=)w<p!!;;gwEe;S-=qYg_Rud6O&FiN)Cby2zYMo%^mb-d$H`pdI8*Vfm#YeY9pe-5U4Lf7MQ'
        b'WX$s;dP|-4HE)^of<An<Cx*^Tiwlo&8mRV~`jIotC)bgS)8x?&N=ydXJT*4d&L1TK_k6xwO7|fiuPJRMSj}lWsw6jk+zAK$n$eRH'
        b'e``~6x#_FdKUp%JYwBI@G-oV2ys0C)-s??UG;$6$(&#s}t`_~{jJu>i<2Z9^iwi>->o9vNzs`xBkFOrRLbm|pE^6n+W2(uMGU4e{'
        b'(T_3CciI=*T}|2j(h{<v*^}02-Ud(R03v3My-AD?Pjdq{NmQ9Bd#f~mH7&Gm^WiDH#OclOq_20X<mQ^@2DEykt6_PDU(s*WY-4Sn'
        b'+K{R@krI}#7!g@}G|!w?_VnJAjK?`rU@yj;s4?0CYg3ZLS<B;gVq&1>dBbuNSDoSP#S^r}u^0(Z1gS}=o;)5}fP0g*JDNW!J`sBh'
        b'duxN&b2_h>Zrn}D${x}CvUz1!pz(M~Jf}_Hhv$hX_~->{b&uvj42KasxR=PR(3*afNN7LrsaIE_qvhG{Su&a*uS@MnnYmut+)&4h'
        b'beeY3`#XcmSH1I^#H{VATRwXFR2OIBZ`6uOri!)RnUr>P4_O<LCLB-ZMpk3Hc&#kPtfD=U-I&Hw{d3L;&u{LQ_MoKrYcrEnU;4D9'
        b'Z8cNe#ERLI=BT|;yDH5ES;z3h#N66clj-F4)z`LUV|$!UwP}1>vDRcM2MI^jSWA8UMMiU4@sjLXkFOqEyVPfBinCf4bfVEc)VdZs'
        b'bu(>NKW;qRQ<rv))Xmek1A-~m-r_}H`Yu}a<H4%ZD^?6=;3eyelPvyPu{ClnZgOTu*4pH1T-@jtd(;t=#4fm@c0^Y!*X>D1d3SNu'
        b'G4Xxk_YYdE1_NU^!EOY87H9%)2bzI<fEM7hz#QOfz+B*az&xPkJ&Sb=@DgA?umU(1cqOm^_z56=Op5~zzzskna0qAuej8{89t2u|'
        b'zX9d|P46Qe;3Qxkuo5^1coi@o_(|YcU_Y<`_<7)2z{i1S1D^+;1AH4;2(<jgVjTzk81P(RHE=xeT3``y6>tLZUf_Aa$AISpUjj}9'
        b'z6-nnc-C>0=Um2S01d#81C2m0&;*PD&A`tBEx@mn{|Su!l>7t#ll%iukbmHXAHY9wKF|Vm19O1gKz1HucLNQ;F9MCgZvsug{S*%P'
        b'289FunZf}lo<KN-u`-|mSOYWyuOogL@<)8&2I2!h4>SQE1Db))04=~*fH}ZF0CRzclV}Ivc;Fb|RA4@E9&jvhF|Yu5J@70_2Y5E{'
        b'cHlX{?Z9(^PXfmSp9K~H-vmwoeh54dSaix_odcW+oC~Z4&I4Wp3;@HxAaFgflkyK-0sIEA3;1uq5b&44PXdnuR|4}sv{<`=7X$AD'
        b'&IWD))&TFP_<{5RGY&KWZvh&C+khk&<q4pfq_hAnz~2CKfWyFC;KaY8et@%qV}MRzKJa?rSYQlT0Ne;X3%CP#Ht;FnIlzAh(w(XI'
        b'fa8E?52L<-Gl1hMJ|Nw%x(+x2_-WvIbPo%7KE(%|2>dqi0+KcZyb$;+APK-e4m7yw8+VS?=%(+(IaZUKzE|gPnJ@{U1^5ME4)AGU'
        b'uA9yi<XH3E^j$y4ItDn+kYmjU)&R!>yMP72TY>cPb|=sPd=h8`z5p}<-v*lL2DcIE051dP0PBGCvHuf51276S0`CBtfL{ihflp94'
        b';0qKEcodim%rhZ>z)3**;QVo*0q6!Afqg&|@QXk*@Bq*PJPOPKPB0@LU==VA*a9pBehN4axCwYJ@NwXH;H$tQV4fw%IssS-JP&w1'
        b'@O<E{z=^;IffoSx11|)=1H1@0E+@x22{;c}PT_zRz*~TGfV+WnDIMTEpd~lQIv+R#SP5JLtO9le=}^aAKm%|G*@w_>WCy+kGy;zj'
        b'e-~rsJn(_%1C78rKoignGy^{gv;c1b<^Z<>bAh{odBA6Y^g;eLiU;^U#RHr$2H}D8ffnF3Kz0z%6QBWjFVG0w12h5ull%is`S1@c'
        b'2Ic^pfVseK;75{a|F;Rw{|AV{A3+L!HX-<@7iBNcdy2CWGG;3kpsBTymY_9Qfi|~zMpJ0S&(2E~L<ynRh<|rZ;rrqwhbxoKg%o8G'
        b'>F!-z#s%LuIIng#=ta4gDrKdLCNMu96H?hrmFWp$2sJu07xC!C>3|GzLb|-G5y`vHNzr0SVV_)hepe*2l55-Qi1rq1oR0QVC6p;}'
        b'KU1W?D%a)tcg0zjpG3u(;F>ZiV^5Lt0t=J!_xd$y6qq}6&*9;6O}RoIjlm>k^BJX_K|@BkY4Qx!VtEd$UY>QLGgPFI;YxW<X9+(y'
        b'GtOYX*z_^PX`uTGN8YtqhuH;&0@IiR!-SlREYk}pk(-jY8HR@qNy2ZUdWiW3cLOu5MPGX3cP0m;Wf*s(^FD`uV{*`0AM?~A3`ENP'
        b'*-AlD&L9H8cac2T^YCv?4mwLFy|Iz}(b<%Wq`xxGD<zpLM@$Yy7ygX$hcG;@DlLB#<vF&LbKLxoa9cKl+erDP^E0Koe5v`Rvo#x&'
        b'e48j6ouzu)<e2^u%dre$K9<Z+YB|=z?LuO=rk0V)u?22)?#{eC)r~suak!Bj67%(^Z@ZNG7^Ut0yZx!Z9c4zx?slW&C6s~oA5@m4'
        b'oI4_M^lcHz<*S`qWn;Ge)wNR(RJ%b#cM9B7j&<jal{N$K`qhsydDbyEP0ptJ3+UV|X>Of5x12P$E}dI$n%f4Q|AI8Pu<pJ<`n`du'
        b'jyERFEv9qJPjgG?+{UK4ZPCSbR+`)WI=30w<ewU|-;>Uedz!`H)HM6qBls&xv!649zgcPaLfv2eFJ17#xDouNpGUrI1b?+@_Tmxz'
        b'IsYHI$FBB`f$`bfJlk(rp8Xw8>kETA-dVbFFf7lH+EVIR>o>zXd9+&HYW-zcCud2kQ>~v2r;Ss6ZL4FtuFm6?nm?B~mzOVCFs-ll'
        b'rUUHImU-(QA6(Xa@`l&F`>r$0TGnry|LeoIJhyKF4?r&+>8+K}8)-<3^Kbg?-p8|=cOA(CHMS+|;2#jDO~z^X2gccVotPWfmK>-~'
        b'x=p}%t!Iv1PUcwaltbugL$YtEla*e+@E(MxcNLquv1g|9y;obTbndyzqn&A;bgdyn4hfcQ(b+xl+0!#S9_;u;1vmAC!i0?3dlM0<'
        b'zS&c&bogU|(t48GtEzT}Eg191I=V>nf<julL*W(7KGWV8inC=LN|y_`Mlf9~!ld7DbyqN~(0Z_RNiZ12rXkYpM<PNUc_gd^BBVx<'
        b'RD9QUM<RjJMiP|n!4jOr`w00*rK&Z6)i~EYSL$Bc$hh{1(z;+UpmasL1En=<I^c(&4K4NfJA;WeJn~Wpmq{wbOO`hCL&7LRJQ0bO'
        b'Iz9B)9gDPc^>|nqhq;2Q(#8l0=i)MgrFpeKMj9DQ8$vyyM4YS1ilKr^g?3Pds#hpxkC%E;Mr4hSpprMP<-42fz+0_!Qg)MpN!QaF'
        b'B_8Qaph_v;(x%z=Qr;GEE+<||B;!h9M|qYjWY%Fzh>BrOQDXv>xX7Fz?V(6r(ecvyNDpa3LfuRKQFKa{3mGc)1QSY+AB`MF+r&aE'
        b'NC#L1n+fk~q|61J2jfb-%TLN`u~AS$;b?E7RFn*n_xig_n`PM)Q5RI6)_719FBwOv8+F5TMfDLwSBRIk^lBN3cf>+bs^u`M2N~@W'
        b'S*HC77ZS>NxpfsSD*~Om>UM*}{7;zgk9S}#G!tWy?y5w^*z>|p=jh+))5ap@<vdz<t`|Id{=M^AVWzbfz27a}VzJWL-glqC-S=tX'
        b'i`xwj_Wy%lE)(~J^5ne@|LNrO{0}eVE_vr<w4d>RU>VPsWt=G2e9KSc-}FDcjI@q_<TU;p$`4e}KEt^8V62Z%<Mq8`aBKnX0Tr3e'
        b'j(+teMWL>v7*8)VOI@eX*m(nas*v}kKB{P}vWf%MYFsJpXA`oMRk!52sLjyEx(scnThpb7I~`smX_6#;`3%}^!K6O&k>gAM{T=JM'
        b'fBpXT``7PZzkmJy_50WFU%!9-{`LFU?|;QF`@SNT*YHB6El^Npi-OjIHi35KSJ|p^%#NzB7#&;huC#3g9sab@aeTYcu?6G>6@n(M'
        b'H9ELIsTXKqo6&LP%SOk}A*16M$O`-MyDDu3pRKehpfZpR6aWo?c7YCo-uW!OzZO61SdspbZyO!@d^6jD>b#Z%)tlT0sy6~pc@I<<'
        b'z`PcC%yXc6!&UM<HN5_h{*PbRkf;wrgG8f5lSH#bi^Lp>xf1gvj**xzaje7wiDyYXTjDtq3nh+|c&^0p5{o2Gka(WN^CeD{c!9(V'
        b'C0-<PlEjN8ULx^QiHgL@5~oP~n8c|Pr%9YH@iK|U5=$h`ka)SoQi(Gq&XPD=VwuEpi4_v(NSrHip2YbQD<xJ*yh7pvi656}mAFvi'
        b'B8k+Ahi<I2{fqwh(!J;h{h%Y`nC*+NS*%3r`=cvIneRt)oAi#5fkks``un8ge-iKSPf28d7HF23C$T_cp~Rv;tKS8(zn@Bf*6=ec'
        b'n=p1aql{m`a{^@BYIGz%hv$p)Kz09DDs2yg-T;r?hdHQD%<0_{|JHZ2N4|{t4)wVcxC~SXGK0E6$G)sRd-Ojy%>i;AR)(_sv7Ln+'
        b'jakTs?q0<9UN(j)+j7}n<aNt$Ds4}JUIOL)7IO{A3Nq*9(Xl+X?7d2x_uWd{K|E`Z{t0vCpYc2dS<k|A_*kXwD9i^xG&%O4U1jTr'
        b'`!Sf!=ivGLex)t?he}&FaNk)~JWo4e-V54#EPEd5H!ZGo`a|8pzyd{6s#n%Gt&b_i)8Zwp6K)HXDbwOply3TzHZ71(S~M0Y)8hHT'
        b'zGy5MkB1^*ZdLCCG`IL_>YX)9Sd?osCe`TWiq)!A%r9Zp)#<16y8PX<rOe&rAxh%Wi9J#^?Cb8H)x}5+BjXBF$4rYNF)l6#srDh4'
        b'(UN>p<=07v@qE!pq<ewV$klu*J-zXS(oU*XLMy_-fYQE3nbwQHiC}!zNMX2QR5f6GFtIuq3{xn7IG_*QA@rgrHO=zx$V!Jl9F8QE'
        b'F8?Yds)T#HyA`f$X38j<RVf>@I+#%6lZcQi++uFwXGD3{HD0QRQiWgV;L<uucvd)Hp**N%j>aNrhi+s+L=X~+XVoOMK=H0fZ+C!7'
        b'P3}|J<ShQVnj{%ige8WO5&<Qij6{T@I?WcrLMf0bB^IiGEia_PatcE~Tg5$+f#*l*BxNmB;c9|Z+fx{iNsV$;pS<}yxK8U4J4_;?'
        b'Z}WJ!ug4#iYJ3vG7=3%kfQiJEnMyp^5kU{>4z3DzEA62Kc?`v6Qt7o&LZYa+ET_}7iJBjMWy&5PH0*@JD@N-kny1XJl5|r}-)Zz&'
        b'Ur3^;D5%gOe7Pb)_(YcuV9?UB05a;s>vD|ZYYx7iP*~p&qurr|vO1LLQdDJ0<SToJ)K`|OK&i(cTZuCG<FeXPI*$_VS`+67KSUsO'
        b'i_3JKA~gvLP@)ADA*fYRRlI8@&`(!%=~9gMc68};N=i=Cq6tNM<LQZ$x3s={nvA9;p{tD1)0ljQJx=Jom7OUT>hbXzn2#A%leKWf'
        b'6ulxS)TarCzdas_wWqjJmPA-Sh0CU=cGjoB-Qqzynd6K1h7w%+7k8JwNY`p2DEy%_p^tI1^b-olgRz93BV{FV9oGv`vhGBPE0Lbn'
        b'v0z$22?P`TfQ;hj54^IfK8$cWv_T^$`+TjBB1L65(_E4YyF)$E?o_@!Y|b70?U7ibxI|fvPDA?LL_XX#$O_}yl<2?_vvQ4R0Yz0E'
        b'w}|C2f1Jvhd}^}=cv3T&a}qCyC$f4WfPSOs#_9=j<zHQqc)};-_Mup66qifYT_k!=i%cH`lf(+rGEQp9QXGV?F3|>=e9V-I2pvUb'
        b'JFxDl`kh$oB(P>V3{tSJp|#EyP#es<e_v^%wa(#pux^5x);jxuhmTa+cKlvj*Qje9{;mOg|4mqHmBH`fbE|A`0Id_MY&$^{&%@fN'
        b'P<(kUD#9A;ysC_~QNg$>+g8v3xnXf#HNMKW?EEU*B!u5vB>dOHUWT||fm<KYjWi|}R@vGkYxr@Hf~!Ox5@~seURq^4e(CA+khnzT'
        b'q2SWgJlu<TmYtJ556{RvtOzjDZZ4Fo$pclB7oJ9up{6K}Ygdyxp@pWjEDl^{TuKVaP>U$@+zJ1@dOvi&EVI;My+P(-VB$YE4?7Xx'
        b'QxiwX!$gsX5Z1zcPvjAKIQ&n_!!ejo$vpJ*p%RKi5noRv5R})BlCnccSX4_1SAjU9k6QRR^KL@P`668HUq+V;24trjAxxGoG@8$V'
        b'KjHU@ImvfJB+|oJ)GO*)xkRhy=mn?`Q2&KmJs-Ka%4WVGdp$pO5ysd>sr6io`1%m0Z&H=5_~O)hw!&@WMWUXSV&ts^dt{l9hD-i='
        b'{l5DW(cXzJ#`;=C`Wuvg>|8Ti`dbx|{_0S;9SdKk>Kq?U*Ek-{p9+Llac!8Rs*~iKLE>Nsi1nhp<t68$6ds-?3AM-Y=MCNKD5S$`'
        b'KXMhm>{8xzmA&WUf~!C3??+<_Uml~pIi~ErF<gjrz3FJbP5F&UshVq>Q)YX?)IVoj*_1NnH{%Nx_LszSaQ$sxJ^tQW#={?Qu@}Y^'
        b'{<}+g%T@M)%hvC5Z*sK_xuUzyFgphjc#QJanCJ^*%03ulyKRj7zA<eNj)^`YvUA$svpoG*UCQrWWgoh1HkaG&YHM>vqptpb*QQOb'
        b'p&{3<(em;v0*_ICKV}!w|8R_L$r$&wW7<}ZiGF%a|D9ttePPVdLt}P5IZ9q$9DmF5zvuAk&&ONZ{+{qJjdy<T?>Vsd@_0*O&fgLK'
        b'7vnAYe^2;dj=v@E?+O3Hc+0Tq?+X8;Q~wtaJlgEcIAml;#{cNI7Os@~BmU;Eqj!rpvFOzYs_8u4Gq(e6tc`z2!Jna94pc9jdZ4-u'
        b'?h~go$Ilzv3#|r=b%UGHw<W}|clhDy2deL#hH$f(;~A^b!OsR_B7OL>1J#FSh&vAMnZP{$9qOji;se!JEj>`(0&;_{1DQb^DG$I?'
        b'zyUH(WyWK`W8>)h3%~CHLfnUqZAI4|sLor)-)VB5nVXG>|HI+vAf2B!!+df$0Do=Qk=u}c8F24y2db?N$jg3{!#!+r6d}KBL46C2'
        b'j%5~u<0<(0z=ya8kf#9(m%{=Z4pi@K$Fl>}2l93z{~dH*a`=z<H%!kB^D*WaxDV+nC@b7HAne>L_&ILdzHWr;0T1-dD$ptBcm;mT'
        b'V&H=|eG2Iq5E7-_3jY3;%wYrnUhoIv7VE8XAuFN`^=Ip1jw3f29Iqgr(rBfvKY}$r%!j{Ya8x~EaFnjbdLA?fR1SJ$x4|*+n89&='
        b'1)l%RVm-R%K=r&G7V8jbCFsT-Ts}pcRN~%`GSTO&sQl9T1CZ&B;peEVuYvx;Z>iwFa>Ie@Dt=~^zLp&y_QG5bqO+L=N+Iil`&zfD'
        b'Z4-EXFn5EZAn!%Y)^?rI@!1D0)-Qq9ffBH9fj{r{a07LNY>so7?LySZ?tSJ(J1y2hPy)0IaSVaBfHr}4f;M&-9s7aL+(3P|(st-@'
        b'LE9^!U&H=ipu?b}U$a=1TxJ{koyqYO{O|5WKh1&tPP8@p7@E*cL<erEo=~WLw)1nW^fmD*Di<qgd$_OCb{ugH^waowZFsGP@$U<h'
        b'kk8!{nXMSO7kKZV(626Fwuh0{b;nJP!oQdt$3brJY6C_`B4~89`RUv2@P}_AzG-x0U|Xf_2<8z5`78!`?W}DX=sHjvC;;jLO>8r^'
        b'JyK11ENDZ`D^r2BAT!}KX4{G~bt4ZOKu2u_ZKps-kj62p15iWE=$QMy$?*#4oo=J!J@EQNMu#%d>^S;KqvIeiEBpR1zr%b0?awFI'
        b'y~9JWDo4LOd?{l`Z>rpT_@-R8%wl#NL><rv@quqytdBozvEB##0_f|YJ)qBBXtB1zU*4zD4v2drZ~(Lkv<0*kbR7I6pxrP}MO_?m'
        b'pj~gSv~7CKV%>Nn+NK(P2j<B%rYm#U5!-?4UANKqOnUHDv1J4FO%vvUy~WQ^oOe<`tlT?%Qx5CiXR)66k;VET@D%d>81R>%xAsvR'
        b'N7%VPwpgF(H9BlagMVBpV(h=*pY`wm!3XfO4dzPFF3_hycY}Tcx)IcXFsJrgte5@NVx4-xVl4#?gYFuaV?7tVt6{bR=j<zda#H_+'
        b'>istzs6L3XMBnAx)*YxWUTbtb^%?XBwA)U!*DmnB1=<7J3i~kX_{N`Gtb1RwSfjw>Nbjq_Cqb{=U1@s;xD<3A-054875%yl=DR`l'
        b'Ao@1chW2Ofg0_8#^STT8H9|)haQMqyRo*T$$vAk~Vto}9f0^pU!1mpYc@qA2oyTnb;5`HSJm}s$X4?-pE9Q$=oCm5&ZV1T`F@Z>S'
        b'$SLG+>KL=b{6(Xq{udVObD%ir;K!KlX5jZh&mjDLz#X86R~a2|0*ilXu@-{Pxs0((o6w@j_ddk`64Gxw#K+<yGs^K4#?UV0eaOlC'
        b'XrUE-z6x|N+ItIV6KD_m(JSba$3SIpn+w_n|E1^VSXY7CL2k_F`@U+i4xnFd`5D^mZjAB*<bMvzRmR$GI?Ct1b@ch}Fv{wLe;aCU'
        b'?_S0h!|VcG32GpI8O@!Atbrpt+K>689_Hcdqr+@(E&~j|L3S_@gQ1rDTg$9tm~9X0b0fxITR-v6#*F*!@bINb`Pak4dp8g-kL?5g'
        b'+j%q_|8+RQ=bhn`w(&-mJC=XVRBVS?TOrCggmUiywZT06=i%W2#CvKT{9k%}m=wh{(A<RZD>^$n+2LHa6Mi2i|A=T4#rv1x;jNfk'
        b'yax?!FFj*u+tkL|j=EXfF7S?{wsZFm4|idG&<~=V4S$(t#^Iarx4#>_gP4p85Kkefh?j?*djpNm#dywx-g&grwx9`X378AsGdVT@'
        b'&FC+CF<#jfn49pdRxpP5!`_YY{K9UF^`^%yR?p+q{zr!kFBA7{ZEZ%!-QfM|yB6z2wAoWI?*m;7^Vo0Wnf4@oqpf~yJj_?YJP+6c'
        b'+6+1fS_t0nfD4|mSU*4<eZc2IllEAw5m4TDFqYxxM{ui}#B7fN3&AS^-2r+4_Rj$~1CIj7!tYv`F9t<G*I_($uSI!LjvL{2!4HL8'
        b'sxQL)0H^@=KaWFu{0L(e<u6^!@00b<T}$%;<~k6I8XX0|B2X7-3upr<3bKK`AT#JF(#Qk;67g0b-jl#7Pg$(XL9f6q2Hdq5&&{!n'
        b'y#f1L*n46AD)5Wo&qJLZqxwf2$AK?_ZU=wT_bk>f;HtCGrsp!-JlI=ce*^Xk;JIfrW(V&AnCoG7!)zvZn6H8PO<))BD0nvmr&Aq('
        b'cEkKEc+Zbv>`j;p^3lV;Z?V4f1MpEtWiUSn+z<PuXlp0z3xGYqUErO-+<XtrgD`&+W8x;59|8Ux_%iS_;JZMbpuPJlZ7YGVAiZTs'
        b'uL^a&3G?qR&{ohE(7i->z8nF$k-rZ>w}3tiDtfijwh`{1gSqu-tW|(-fF1zZVIP3o4B$DSZ-DnAh}H{4Wz51~B`8=YAH*}zi)Yuk'
        b'N6}wFH83v$c6RdR_rDp~-iBqc4}kW79!4AN0L{f1ses>Sz<UF99CQiniSf+#6x{PMJ{s`M-hegHZkT71eTC661UiK^$H!sc2=ah>'
        b'KzM@F(r)jt=_s9#Iz<wfp29e7pmoFEf;Jnd9>hQmpk*L8$P2=FIzBx7Ly92x%X9+bc{0+b=hQG=#<}}@k-yUFP~K9%j?qHA%-A-O'
        b'<{~U7@5NYu5cKuMVtu%6!67#yz^qFXUiDvxhkr6GZ_;5_8U8Kk18fui%5MPmn;5M^Uqje8KyQJL?=w1f{I$|{9olsm_G3sI!_F|L'
        b'9%BS##60sj@Q0v^D^Z{C4-W@``x_5be-ZdA;ICX5KfpZLp8)NF`3>O1z-3F&KR~|*ZHN7$h6B}`fs286fi}Rr4;Tj?1$F|9L05x{'
        b'kaivDK2Q)81KkAb%NJ+zcES7%XkQVt{Q`Idv}$aX?QP(3&<W5f&;uw}J;q)e$UrOZX5<Mp7t{}OfmVR_*J0fR+;z(2V6UONimGhK'
        b'3Xu-bJfX@)!f1BD&oh&;#t>&fhUfL(z|OhqK=m~sJDvG^p0QWp{~b`y2YBe6#HI=@G5J@+!>@b{6Z!9lhu^_C`~%6`^Bk!DF{lgl'
        b'Wz6!25bvixJ3PD|_N}1)R@5WbE~h|wcvc?;ny}E`0se15FM{UV*}9HXmsRDiYd<xR*S|hK*?(%U!ftn5e3Z@ivjStuxF7mXO}?I('
        b'drnPx(J;mM@m<@@Yk#-v(ZZo86>xW+nqoH(Z8snN{J6FMG4xR3rmqus%c)20=1pHRAHIFu+V5=od}06n#2q-b-EQu`+r0LMLA&|j'
        b'z__9N3;S<Z*4xeJwXpv6WiV_Rx2^WnrsBk={zU(jams+QN$F)%#tjV=lDW8d^P*GzQw*D6Emn|4hWvl4^3>#cl)r(K+s|Frzs@qW'
        b'W!(Ble$anM;idsfbnx=RwJ&bE&wTWL#HZsux@n6UjKlYj18-*Dc{5o5j4~PLI^|Tsh2*dJ(jlJn!LCcGRC(KXFu}M#Z{4I*>x(Zt'
        b'oX2Ds`vs>SePr0SLz#9k?;B=#S!TqaD~!Qk=gqXJehQ_ZH=oU0|H!cFX^XLJpbUkgnm2yKJnb+KLH^CE|DWbj3E^1A3vj#f%~$h8'
        b'8`)2t+-W|qCa1u%+_3b*vkDfyYI)Z3=#XVvf8KIbtoiVx<7QlrKi_?H@}Ey0esY}h<o5qMdUD&lCto!^J;Zi>+y20syqWo5Gf!KR'
        b'`)q!}+21g}YA9GaZEaq$VPi!>{<L2kDevqsdd`Q#?7X+x>qDlppDWLr3a))~P2Lsef~n^{{b50V@b%p7Lxy#)o<xN#G`~N^P%yr1'
        b'%HBGxcqosPpF3&)<w@jw{gm_9`xy)sQ>cE|w~x2g6gvC{&N*-0^C$b~6x!xc2`k#qoBYg4$538@X>4t$dD@h(vdc_kC;#B&lqnN~'
        b'zZgDjWVdykJ^4vkCl!uUg0B(h;-l-0#=`^S`q%Xj79%awZDXb%-Z1XUfvcW8iSBmCEd$H`(sj|c@0={%_&wvB-((x#-fm>;zD;?a'
        b'^7Ns)H;384xr_VqzhMmSU_U-VlXL$Z<yKw>J5!WIZu=+JJ#?~Q1~u7$><0tfg06pmp=K?(GS&6FDX!bTa5BXi6{p(IZ@+%sJu-zY'
        b'lDUOjk|_vlG6m`S-4xetH=j&#F1S#&Ue@kg_i35HPRZQKEy)CgHJN~P{ceiuwv{J!&V$AIY6^p0`IRU``^kb5*oyaTnnK)?J>0VP'
        b'-#1Mu)T{-rRM+pMxNdGanc`e<foi3GZ)e+<oLoO-Mym{cUin_$sylCbIzKRW;IgfWU1;gsrxY8vPt56bG!)$a!;hbQG_PpW?aHcw'
        b')l&-C;DO;M23M{hx^!~M$tQ{%d8a&wjkWdnZ$A8;ai9Ofx5`c)ydSt_d4Ioo)920ox0e-Ssv3Hu|Le+-a%^k+U*5JnuxEH^yE6GA'
        b'>V4>Uw=%Z<r-x~r@Yo6`PdbU2g~$1=oVSOce&*1R@u;VHW$ek#V^6LxuGlu=WNz0K8q&)#x6!O3hV}9-#_f;%VEq^c-1RO@apWbG'
        b';w4n~K96hr(}i!I7#4ML-s^1p6!W@V>dD{-KN#L5=CMDX*!;&6>+|++``|?Gk;z%pYslxxDI+C!>-(brBi`I!=RWY~VLl&BJ26c2'
        b'0mk-#!)-n>n5UGLCDtClEMzV#w--z-t12riGb6}(e`dj>!<4zhCy+Ukw^RPw3HSIDh3xWGEUz+TdEgJjw|+2eva>gjkw24xRm`~1'
        b'w(A5YCrmm+-&MY0T=#Pdn<MM+yC(*>vGs=x>+>$?pHjB&i4(c)mr+kF9^B5(Z=WiRJJ@CIleuy8k4{v!U&4*NeD_!7yf@78#}ZLO'
        b'j&*+-M*QoIhVyo^g1qfU(|U*D&Evz{jYd2i-u!{A>&^F{*!Hax)X*g~Ck*jvdwqy)9Na#{g5Mi1$baCyVL9JV>&YvB@C2stvacv_'
        b'hVu&YzV*O~Z4aEd?cDQdsElO=6E|&2Tzxz5Hu<c-Ke74CC(!H2x`eGC;`}SwdKcUFg%d~@1`0QWU35QXIDhl!zzRIjnfDFTn``rA'
        b'nr{a47UpmK|2TUSu&A!H0r+mSFkEzIz!3qPJC|)B+Rh9b2Aec9BO<u8fQo41S3n2RG_4vFZED)NLjr@6mc>LMroA&d5r`y!iEC&X'
        b'Oo%b?Rm^T<O4MQBcMN*}bM75n+WgP+{r~guoH_TL_nh;d_q^v_&c<d^klX4%-?n2aDQDRr(O@S^y3~hmlYttHGL$aHn<rp@$so&p'
        b'e1WU|@@>0Rr9lM6CdfV4Z7%IRz$Y-j#K$wk0eQ7pws0t<4B8F9zfA^3em!7ovI6uc?2;1peKIKjo9lE_J1F_|*C6*SO3GMvuXqHE'
        b'pBnXyb5zFO#j><(a&vQ+(YTkKcRCDXH&gm%HyKD0+Qi)CC6Jrawn`QSXhW%$s^8MhR#4f5&EL$vk6=clvG~A<k=9yixk@Q=rAbqM'
        b'35m?EqLN*dC0$ChQ+2<(9r?O}#OP-NNhST1o>bO|Tsx&FLv_ErU5Ot(uNsq(IM9IZZ4IbCbAe}}*sNX<8$i_H;d=q)Xy0uo>$6|~'
        b'87a<My)DbvlJ*v%e>AWL)n25uIxF)F$d6ge5#3VA2nJlA8TbU&+`%EX=5|1ar@Qmxl(t6$^W(_ivXW;44_?Sxjfnrvk*ciK7V&j%'
        b'vAFqP9Af;OGJZ(O>nO{pDDMUbj4ko^Q0G7%M{e^X`a%1n1fyD}d1-#n2r0?&u{$gG+_yoP1-JjpZn;-Z`an74Kg#+3|7%Z&-nQdV'
        b'I`0QTqK2XlgWsgYmD?nyAEwDbTf9#TAZ8+-GCl1}Go#ZR1AL1or<vjDBLNr)0kBzvFk{n3cCU?RxwLCDOuv9Fv@HXJ%ZrK*AE}U#'
        b'0p>&>aUYzgmD1`;^D1B72FvRdWE1o6X~)fJyY#;mv*WwzS>4Ngb+6*`K+>lq(TBIOn6~MVgM3CsnKQ}vJ_w8n2=Hz3(+TRGkEW^G'
        b'z04=m09`l@`1b!X?P&h-_TAGD>i+#jMX#kLaXhJmiw-YIE4cgZ4FT}f^uq;f?-dl<(7iQX|4v6qC_=G&dFg}KdPNVOwi9zra?IbR'
        b'osI?f@#jaTDiJ0ayj2@WCEsT<$Tc=Q=YjM#l~04|WhT&-deMOqnBHzyM8~TSPhW{wXs}i0Z$q5~!n_8%tXWS*6D+OG8|T!oPW!G)'
        b'RsvBTZDemVe}>t~vfBvT6C8ay91}+)5&kF{njW9LAwE{*O39rj#XCebcowMZWeD6Ls}VCc7=zU_Fp`-tZ4kvCj)n<;gb8$*NN6xM'
        b'KxRAEt|yR<_N73aGKnx({5glTm=BCJPjU$J9857xkiL&c`_e#ns8a9hwomIp<k)SfG%MG$u6V`*p@3R}b!_G9xX2;;i!(s>h_vaY'
        b'$=bas;nT4B|ACqI_11#~Td9q$@P%ocU|Pc8IaO9avysmq_ckX*RCFJ+dfEmeQ$OU@@VZKuFdc;(Y)7{OJJXDzOgt<?DoJ0qzO;q_'
        b'DDq<f>|>v4Cq2JihOj`Pu+Lko6)a78^WZU3bh=6*0MMwIwLTB53mTQMWzSRPAVSomfJSn*a&K)lbZ|gfAcU-T1sGH-J?kg!9-2yx'
        b'3}_c2q-diuDN{3@o_5qjN(<7Qk$(UcM}?Evs#Q@dG^!*~+|n7_CRH<V<QLg%#BWMpC|FP*{i(0LrMEp@ad1QX21V*eft%BSQRBSa'
        b'M@RbWSrk}7B$gan3L1kF5z{Vd?C=*ytw`wS7UKqUVJS$>!85ise%Wz1Zp9{Z-Z0cXrcbAAVF7?94$*Wyi`b&kGiCnzFn^vh<w4D2'
        b'q(Q3s=I*OLmo#OGkw=GB>yRc59(%M)<$Je$HHm9B$7$jcV@p0Q*bFKZ=4Z<3DRX#0JAshIN~MVzm`Y4Px`gy8Pmc-%?rgk98n<Mo'
        b'DM^~(gDfhro~4Sas22_fH9h*NZ+Xj1dy=9ezCB)H{xEP=qIi@;>ObwH!~Ije{WFHc{w<c;&1rTn$qYOL*oXg}G7}Z507**O0}UIQ'
        b'E3o19Lc?W16U8lwijORRGReTxwV+j6<MYD71@((y!@d96a8nCx7d9#*l}2YNP@lZ4c@xtlrP;Woq&&dzNCRGjd4@QMM<!DI{*>eS'
        b'DcT3M`5=PtO#5KKIzhZ~y!dxh5BtuU2<4=rP>+aEzd2>Y&gRQvN)$lNI}h4Q(vcDcT9S^2??7x0H2)x!D>SYA7PFv;ddrmKjVbU|'
        b'&(mdA7Zgs_vrx*=p^7sY)=VMlbyJR#DPRx73GR=j1xajloM2kGwt{vRS*ztoF9S8P9Cu|Q5vw-XXeIe`$IDXy!164T2QLE_+oo)x'
        b'7(lv&MXgn(&gFPo;2kF&4Ce|vw!H_6I=w&f)z&D05BWBr0KiE70>I8#s1%TcGBQ+|cJ?-`{+WbME`R5B02~tBJPOCJ_%~Bvo<PIb'
        b'2WpoE!FH>4Nq*2A_yJQ2e5$MHRZ?DV7H9o`fKC6u!&2J4KpchtmSdwS)iMN1X<&%taBF3%AZ`!)$`&kh?bN<fETI;OJ%csJBOyn?'
        b'mpB)Rjr~nT=?3ydZ0xe^by!{nlAVhs3?kVvn79zJU4%B-<CFPkq<h#$K*79zWcSae$RJx}RH2~;hjNf5@;Z@_m9XwHBqSgF=IuxJ'
        b'uzveW8`V)$dz2W7#cs#)&LG-IllU~qVPM0rf`*^m!~O}xn?Hjni4P!)KqZC6AyXQkH2sXaZIYZ%(`#%CFe-xBMQac2yFx2=@w`WG'
        b'!V<aw_wHeHVRLz)E=+tCahZ|qYgqG#h`MRAczV)CC-3&1g6y<_04A}~uGmG(t-J?FZz9wUlWTlwTJE?#3H>krs@NX34EFI+5GmRh'
        b'gC$ggNCCulH)tVk4+}ddUJDZK`}{HSSuW+|BpH<Y1!kKkT_j4j%Sn-Sb8hVhMVd6K_?yW+@BTw*9J0>>0`vmtAa=G70v36TKy8O$'
        b'Cw3zHPGNa}2A_qX@@AIXT{O98zD%_-thgCa;-Q+NAU$@`iaj-4b1zQ^M{Mi@nq?znu;!N#n*D2RJ=Xj?1Q_*SbItxB-wEmbOAt8@'
        b'D$gt6cE2>aCvvqa|0j-*Cdo%#wOj)K{^{<0laAAqwn%wB3#S}&ZnF5?B%MgmIS8GE(CIiG84IYjm}p*(sDCpl%%bf*1K}TXVt%#5'
        b'b&+E#Cdqt=ZXm#t?`AsDJi;-xlb}ZRuP2>Z%K_Q*;JsUQ(Im`Q5=U;lt==$MoIXj@t9QRSN&S>C+E6-bxiDb#j^%WeoD5Dl%#ka^'
        b'JAs}qo!ngt@rshtD<N9yBv2A!rnZB~<Eo}{j~W4=&7X7X<&$-XK%%_)WiG`y$)rw#0ZW}HC4<0#ZNb2Ru^Z&cV9YN075@f|*`FSw'
        b'bR-<JB3dCX;ndp6y5+E<ygi(HF^K$>`Wc~ewmF`kBz;{+IsHWsFaRXl{8C#2lAJO2gmmBQSl&WTw{_AMs@WGP0-gn+Kx7A&5Xh+)'
        b'PCA}~m64A^taBzwQL4F<4vkdlKjaCVFc*-MNu1pM>q&u@Yh?GRsh%?_tQv^l<lq>e;hHNT@oR9`2b{PJM0blO$v|hMnUt{kxmI>>'
        b'+WA|%6DCXMV`ToWa{1$v`~08S!~Suf|LR5a0Y4<n;|i;Gk5BB0T(i9s6Ss2ei3#!$Ku&Dn5LyhZpo{9^37Y<+s;LRi6(0@(@ZGcU'
        b'Zcg1Zk#LYB162jc?wb>~$TikH;=s9fyP{}=+`56vJL_Hla#9httu|H~X;{KspHS@~B9yC(|21KYS`Jqab}VNWOqOVV@<9}!qc3$f'
        b'x0c%5qGvUwCzb6!h*$#Xad#qLxs>_IWPZuV%qJ7Jz}HuH{k<9VoX%Meb%;%4>+Gt@o8cJugj2JcbrH}Ga#CX8SAirO(0pA}&0|nz'
        b'Gjk?2v;MA$oCFpz%^pi9A}dxJ!f0GJGvbg=HsDRiN#^qjXmJ4*BZHC{uMt7X>#wVsum{+-F4cz`fT<Bh021iwpOeZ$f3Ho306S^1'
        b'EN{kZQvms_W+#A%rs*XgK((@1cJiR@-9H`7B^Qt~YgI05-P=;8zi87I<XR0>;U(8N*Ycv{<^)`t>;smz%fTg#2y_e|<J8|zq!dn&'
        b'gxQSH;q((SCkxr#aUGbhuHSMd+XT&Wwt&NtWx?t*6N2Jx8Ogr6f({QQgGm`2MLz_ISiS_bj#;B}fu2cI-ql~UYNK+~Y<F~@PBdVE'
        b'vvzPz0f%8MJcCmohZQ-^;)O$cmV*`Djtvx<KS!NJ2pOE$BjBd~`-GuMwOpaIOw?fd&<H>c64#p%J&mQ^oU6~8qdPN^=x@h$rzi3c'
        b'W6g(<q#Kn>%%RB2AYW7ZgmWum4hshckl{w+RzqkKo!At67|RPqN-*4pYpqpUry0#(fZ5FW(QRhpF+Khm5+91hgvJI)9ZpCq*Ebv}'
        b'8*12Q3s?}RC;dUwx;H11nzRPFRy$U>T=(3BZQb1ZFkjWDh@))6%p#r)&d`)}N>7vZp)%D4#8C?9>iRWIJeJsGxEdQk8uVJ7DXu=w'
        b'8CMc#Bk{PapoykSr#?}tW&)fa2E2)pi7(jao|Tn+GJ}xD+S=lC1<uPe_KPZMKz*ph88!!+{P2wN4b{y-T`HubIaHn<u*?)Z;S5^|'
        b'WT<54Pe~|q%v<H=&_|u2(Mg|~Ll;+FG;f{D11p@Ni)^gb8c$W-<iQk`wnTH8epPjqjg+1^7gAK+SY>l!xH&W$XygMkWH9?dY3*?<'
        b'5CdDID@zhn0c6REb3cJ_B>;|m6j=J8saiYb1wMb=x%JV?tdlzvodDM9g>^#M)jaH?hhZ00)+g=(ko6F<qOrUlj1hULwj4k%29RXX'
        b'fgg(AF0DRXvURb|j9HDm%jr*?$&u=DU+ogP-i#UOw2NZ3e!`%H7QcU-vRQ>VmQI9_hu&i*#v#$(;q0HO&i0+nt-J+4YdOU8PcE_P'
        b'=zBI|>Cv3ZTjn6~%58H^Q4`Fy@w1z4+x!!+@#b?94u-EO?yCCYxC5Pla&|Ru%K65`(W+BZ%`?#6rL<#{St0wj${oan{@p*3!CG1l'
        b'Sjh7vr<*sS_ea1d08y2qnf?<d&v=#!q1PvqqV2fMbAgMvjd|9Cc?rZ>K5ogZ8ZY@0D_J1T_u0gZjoYN1X;LUCYym`Z&$zHLV_Q!!'
        b'Z;bQHj_V~|m^dD>oZ(bKX!sc};<9g6gxvAfcs*-u7Xy=>nTFlZ*_@>kugsQ^K>|54N5;1U>nsk*{AQebnlNrqB&SipBSy)DEEAGx'
        b'AFo8SA_74LE4Na@=1@rhp|xwRe<8Bo9c;8KGWhK>0hcpB0`sS$hhaAU2+Tj&hha>u<Hi_yatsCLm+G?tQ{{MSn5J-P4F&{Y<V`H^'
        b'G^frQcd+BL%Fgl5IEjb<jZ;^T>w(G(i&WWqp*%VX1PCO;>*H&DK^Mdya-Cb3!6w4wnW^JxQ>g1WXJa+_G8KRV_KD-rH~`CH{j%cA'
        b'p#zSPfQAV*ux!FVU|p<rJFeLx232H*$+J~T7t3WIBr~5JZ;*i+5(WW`;}zh1dnitPikrXHFViqi9)c)5Ki=HWkqLm-%_q4n;=H%L'
        b'Yed@d;@8HVnvg1=;=|*P!{a46AvTQx8cHSORe~LEDjgSAS2P6a8%zVXTDFXw2R9vv#lG6`+$S*lvW<GG6wvF8|1&A}aVVTcaEbIx'
        b'NtilsJPSk4ydJGqj641WC?<)}V~&>qjxH4(1?LK6F<g={5WX>RXOIAjM*ZSAjUk02j^B@40=z(QsR9ALXu!h#xy9l<s5cPxj&Tjf'
        b'E1tXop+CBuabBeb!}X#9JTmJk^){Gd!{9=4pR_n@yu=6TD_{o398Zng_eU5o$7aByh|7;}$SgQUi0u-`SFmuXIBmS%2Pu4}LF(8r'
        b'o;S`p){lE+9EgDSnS}8gOjx5!7#7yye>q+vMNTHcl{BPy&A5{-YFj;CQB6w8f)@(r96S$dZSqB~oo!l;1lxh8l2Sl9TKA@DL_kZX'
        b'T>?}fr%8Kk9HwPVLw1Gk@$rN8<k84Cd`XN3MKrt~F2Rwa<EE>ZH=cMLyLwq$RJ7!(8F7BH@yO$t^Ao5~f@2<~#UmVvC5#GtjSbi$'
        b'tOV6=ub<PV8FxpG*E?4_G~=E(eU8-owMCA*!$3-69<+CvuyIE?B-xY(4tb879*<JYu4Y!jw8|WEVI#kxU6lhr?e5_5?-!0YR?FQB'
        b'#=RMKAwvaIYrRP%$ro-QwGE}z1+=|deh#fY5A)9P_3W?n8~2ULh(Up9)-HqTaj?y#z>mwZgkK;!@wfrk;|rFpFn*g0(l6zh@Nw;R'
        b')Yu}w(gLAB$?=U@wgK|ee)GGH$;s>C99{==Ho<xfIV3^Ob4-q9tj|r}fU^7qhmGW{REe^hxeOy*(lnH1okTKX<i@QqZwK5d+>--0'
        b'CK7W<oSc{W_E^!nT;m2bBVL{y4?&W0Vi$<?pKw|&ES^}IdJ;*Fmur{sRl|KigVglOn0Na&hhGPhMvhJzAWf$=eEV=JK@4e)D&iBr'
        b'1Ea_SBU0)pDg{=$+`E5f$T58kDv{5^^Ii0Q?{EH?-*dXkBFV{nQ!^3mC}nKl+v?Zg2j*>fI|mm@;QA&R@@nG;l#~5i_#KWpJ%&Up'
        b'thAi9J`em6=G2(ATF%~E7h`J2sCvq&K`cL!6!GWqGZB3zVrdgQs>kZz<t(3xo79Nzt+CgCgH+-Tm}QQ{8H&6fk6#LEw<+3>Dx&R|'
        b'%g@Sc%N4+6uCO0GRQK1h#&`w4#EaFwCpWz@W=xXT3KZ0|ia-s1l1jW)3?gzEk${N5<dPd!?g^CCV6F+y@`>1SXpCkN%fH25JS~^R'
        b'nFSD`jJK%p%i<v$Xjq*$2K2&adzrEwZhD$O<gy7L*GJ+SvFBf)oCaSFB~6rcwLO7ftE$1mRT6J~HJE4NY~1nu*dn+lVV8yYQs;7k'
        b'0k9Y@gcr!X`Rd<}QCUWcB4+oAv<Mqbc|hpAdgY*kwKo=Lj}=uatksQIqY!4>*if~C#A<t>xVt26q_tN*Z9MV#z&XARDW#b`XQ6v)'
        b'OxPULC_NvDTlUo8mMeUJZAwJaHP5ar<oB<oHX6(K5!>~ZX1D^K3Y-AJE)PE=)~)hZ;W;ZV>cxxRB$&i8b;4MY-P)d{NR=Y1Xbo04'
        b'FMNYfDvPEjBFVSlqFJwud2%e7mano$NnQ0~U@TvnrL(6_tX>N11P+hul(@DRuWcZTmyER^QdrBajCQQj=e!+AzO*RB^DCbc76IbV'
        b';*nY25rdKYP|WjROBU@A_TM}w#X8!Hq3a#7UHO5gBoH~!!<NfS(vh>$q6=v4S)B%Z{Sa1(vF;TtD`JAi-~w0`z{>RxF^P%$ImC{g'
        b'm9}3{B=8-#_Ttu82>?!s@=IQ09V?hQumn^Ta4&d|%;gg62-ql~=LyiJs!IeK<+tehM(tQ_-Clbjav`+k>o#P}jf^?av3lo_Yqd|A'
        b'w5S{{D$|`Qheaeieqm2fE4%yp8@L7|e*>BX=#7j*^!_G>J$hdZcofVUFMgma07Zz=00e3t=e}Hh$3`PmFHS8cz#L<(qR7DSTyH>%'
        b'*NFj<#6yrTT@~WpH%0-%yG~G+qhg>>wc5Q#<6bbyGcxw}i?54Xi3S`D2y<<e-*&Ma5!XmuHM3*pdR?4(b@adwHDXKIL#2g+H5k(h'
        b'%Y`2XGs99XjFF{O?Dz<_8UEUTHn?lo-aC@nRzcyv^F1ySJI;+--kNQbxd2nuXGf`M+w9&Da~h`E*k7sNA3dS*W$Jm5S^)&)YkP6+'
        b'6GW_1-uBL@`<+q8JEMzwfz2Ae#D}Sapeb*U>fRo0rxnx&D-~mPh9eNamx+iVEIi7G_azY3-n(XgXE-YqhDo@I9gU6$vHgVUuR<)5'
        b'Xt~849lcIO+bgA@4}@hg0VoS>tL%Vk)9a%^d{Xh&N&?DF*P}#&hxe&VMoFL9oh~>x|1wImgnfBoAVAEQ)?b{-#)iU0qVT2OeK0%7'
        b'N5QlO_HH3WUI<BFGRRVZk-knA^Vl)wPoum9V*cp;eF^^3i73PHWrXne-bCGgK7vDw>S(IKH9*L!pBp_$^X3mEw3FS&?1jbhMxh_z'
        b'$R2gQ2a))bz#8xv(g7HCJUi-sW|Z`0TN*(FAR!`E?$|l%&he)4bvQ($i^zIb%IxM5;X_BJH|@84hh)sNd>$Vb23ZC;b?~Te(`d?5'
        b'qttS_E`3zJX>{2Vt#-Wqm?Ap7{y4&3Xf)D|6gAFd!XmEAD3bvro-)ky2N`4LYkOL#&E@N}d-bSUf)oaLc3`H*M#;b$cpAzUk1!i}'
        b'W<sT>HD8lKp5q*28Wj%iNKX_j<9}z*qVXTRP`Uqk?*NZC*L#4cBnNS5N3#G8AA!|FOOW6#K>`KF8JjK#>V*k`S*m$=Azpi#CH&X2'
        b'adK|kPe$Frqy2N?q5|_Xz8^n*AY9C|d(dbVc23Fozz<#Es3{PRsRlO+hkI~_fElKl5mHG){Xoa_=fO<K6YwY;jq+ok<sEyyLOnLJ'
        b'?Ect$K|z?xV-3IoJAe|&eC@P13%ys<y>zB?1hPyA5TG}3gcPN<OZ-q}8>e&|eN0GO64HVDsFC+@9|hu0YRa5@HB-Lg2#yTkSmr!f'
        b'!bfxzL2luu@ezcOBe(p?U3u`I5sr>XkrpkPkpMiHWGpiP`5gDrp#vjGhySzaYmXwYyopQI;6tiF-t(900!?xX0Wk6<plrto>%I4P'
        b';I_*qBmLlfbh_oPuO*&K7=5gZI`4E}A8GR+p{i|6?})(OZn<ZUv=sxt<P)TC_-#omMy`cl!Io(W84SxWl)_LgRsVD3ki&p!lyPc0'
        b'6Sw$E4>?>45O^Musy`X2LHR6{&O|*v(i+q=7X;xykphNqgKYu7^`G$98~!g0jlH;WEkR<W{}#-+F1JP$et@eHSzhE)PLDhe8LdE+'
        b'^8SeM`=0mrl=rvZ`&%dcGPNTqwIe)lCf{dNAR$hUq@4V*^vaPnq8~{<HbRE~XEI>-FOp~3-Q|m?ya6kW5=9>N1Bz!CS3|gVabk{x'
        b'i<;r!6Z8BQ>dN2o>)_DdIXuE2w<IyEH9oQ|KwUg?03IFyN-&V3;-MpR@BFDi65Xzm!oxrw(#r)t1u{%!=F~5bfEGNXlB+D*<V-id'
        b'M*$1$-xBhPrsK6_a1Cbp4w!r4h!j{3VySsKk}%};RrigM3xHk0yf6|aC3(6^hfH1_vxgs!-7ti*ZWsT_hr)S=-@&N*HzW6a!NNr5'
        b'83B4569FS|w_I4)<Y$>D22DGNc>V@0p715;tc`b<gD5gvM(&^Y@XT<eFGx#&FzqK|$A%Hll6&^kLa`%d1n4c-BVxgxhQ8uR@h?XX'
        b'+VamuGiyhR*YeRvir0)d){az^kby_e`xUPqsh~j+c@DF&h!vWeWMIM_FFg`QiW6X=I5AbUgbXbFhIw+N*f?^KCIchSp`_F*n5KeV'
        b'TlgIFxEDd@=X`%>*Kut$s;9A%OG9y3nUC$#SUFuOtx|fXf%_O4q>4P|tJaQCF>>|u!&D6Aym-el20RLCw(d-XN~M620L+$-d01W)'
        b'(!|QOr>Gi~SvCyS20hY1cqX~C=$97|^}-SAf?U0In7TmGpWe}{QPp9IBWQ$~2N8mn%t9D(%pYMCFal2_EP#<p1?le@;!ajnqF<gz'
        b')Fhbua&^iuRZTfB-?8*^BpzEaN24SC3-{1;0NvC_Ez4ajB30>Xl}L8-IR`NUxXd-k(eH8&93nIT4|+K64z~jLf|-PfCO{!rgTlqK'
        b'0f22rwU*WH1vsY+4JTiar#uEiD)rMldjQU#<BtAerVExzc2Ud_-_M?5<`#_9NSMB1-Z)4bnM{kBN>?w&Rj*7rJj1}^=;RXq%^{BV'
        b'Vc_40m~SAQc$@<O&rOKGgnAngubxHZ4vHy(nTOn~>wx&7Fp_LQ!KCP(_2mQ})m<H~r4?G*s%OEx<ZY7RnALQ4?(pomTP8$~%fnY_'
        b'1vK5Ot)5AdV8=9JbBjM3ZfqplKTw>nvdg{=EXazIRqbh6SBaffTIL||q+A#FwX!ns#1oRQD#9wIC;t9O<^F=Ksy$IMXH#I+{<LFv'
        b'&X*f}B1=Dmi}<g~^2WHzoV3kcRaR7v?NVUDo@VbE$?yS@qYB~>UG2fe!uf3G#4xatf$iIhHegYxCr4yQvjatd1uTBEbI3v<y1x$7'
        b'p@=OMrJ}8*{|P-x;s-CBkMW)_DjOzO@yB{>QNhB&OxuoNrgV6AO=i}Q`|~jA>scc)K8mu(O~A*kU1GXNpIf37`!KMPMd2MHCV%)!'
        b'ykb>i6cHDY82GiJOnOQ4)e_OlHzgmRBZ@wut`pfL7U3sxyf{og8opLyX&2RqTobeB*za3rFAS3lplt?McS;uvdom8h=9U*IY;J7<'
        b'N+!moBxP>ey@UCEae=xpm9!VAv;9TT=#}CC8s3@5kuLvN#!z^#`jyXrKt#R>vI5?G?!vQ;Sl+*oiN?W*<XaJP&yOhVIzeH7G7R-~'
        b'2&f5%N?6d^ZBP~eau{e|gHG#CGMKcWR2`o3vtgiwli}UsBB~1qf4YQWL5dscBCVNCB;=XY6$1H4eNT7S-P7G#<j2wkym%}`0XS8M'
        b'|6GrtxTJIrg5fGFf;Dnl1V=D`ZJqxsA-J*)Rk|Aw3{g}mKoa&l?{5f_P>dk|Z#{%v0o_Cw4*Q^>kDHj(#`dU`xXh&8BbiE(3|Ia0'
        b'2Xy|hu^mT5ED-+lh6PW93S~7I-IN%Ig<x9Rrjrjx#~{=g&|t=Pf9+CMgHPk21Cfu|RJJ*0;B&u>HOC?;l3^rXYfeQF<BH_<tXYYs'
        b'i;#HAoQi5_M7v@$J#)(Xi<@y+5eSsH8S^*ep=Kh+ELv_BuQN-wnx)T~eR9pRQnT+dGkMDFchNlOGxOY=X8EXD(fkOK9diKDg7R_@'
        b'C@B!oS`g@sATTF`AT<L7S-U{6#|i>l5eQ0H5IAc=P=5skP3<7KIs}3ni0)?Gh+KD5pCzYYs0g#PhIO=tZNCn$t29}|+OLOY_J`f*'
        b'58HYt?AD!Tj#K^9PyYyN`rjc*F6=H6qt*W!aNi2!axnDiKieEObIO2eyG9L4ZTBdSVg48%iV-oGXgMZche@_#(&sRrTufGq`5wc_'
        b'Q<&dHY|dxc+?$wu6!Z2Elt*BBbksm=u~CCwi;o)2T4L0YsuhhIvb5q+!yc_<)L_#}M-3%fpHYKTD;qV`YkfxzO<KQE!&U8^QNs=G'
        b'+)=}bRz9ky<yr*@6<XzJSa@sLTdiS{v;AYQhpGF+oc&>;cfyXt{*9=W=}h8oLnf^jiN4_IM=%N2gV1td4(}-by#w&*jZDP~4$CRt'
        b'@3^X#-%u;^MmW+4X5oqt(1&>NVFpBB8p1LWIZ7dI{;#xR=%0oV{wW#i7OuU4n+^<VX*sa+RaXfBZqULhXB4KKDRsyQ<{MGuYX$&m'
        b'd${0u<4ymNQRA4=7}MC;i#N6sjWI>0-wYXJY7_Cr;v9c4|HR!usy26WD?Y^@z^Mu1R1a~w3USJq#p$a5iVrdLe;&r^sRwYn`XEmA'
        b'xM}hK4X2eqij$}b19G4V%7OY>IUv_RNV|&=&r=Z3&mf+0vv_{y|Is-NjeQu;B@f{F*@JkV!cF-94bO!?isvh5Af6W?o~Q2N8H3zg'
        b'iy#9sRYRYyL;Q_MyrVrv(Y`^k?1eIn3>I`v4Q8CxHm*)FFo^v&!}ab<fy~o`))qO_JP4G}SxIe0<Iw_ARrvE~eb@?$L5G%Amh42b'
        b'nmJb|mX^)gXx_urgyg?`tO%L438x3`(iRQW8D;wm3(5>fXre6f2;FbD=S_2hy_M25;A>vFbdhB1Jo3YpxnX3OF^2j%ec(et2{F8N'
        b'J^$tqNu+cP?iaPMSG42@$7e4YB4y2C$fbQPkMGaVyUlIho+I9lkJd;&LBs!sYOCd!(AbJwlC96%V>7=QEWS3l)1DufvpTCmTtk+l'
        b';ggawRJCeG{n=o3Ui8lG=lt5P4!W-nKK_*B>Y!_ZRDE?YS`&HBx2<i^-8%UAGZ0gj3MedTYaMidGWhr(62>{JHK4Gp?ed`eqrt}y'
        b'B@A=wPX?o-tFYBhXwU%9ne+@vR6!GYKL|Dhuppt`Jq(Ypw_Gc%cmI8mUvz4Kq+Lw#HjwVZpgt7I#^=_ZAB4-2GaS2&S`74O-RZ%|'
        b'Q&`>mFxArsQ`2_dRq5}V{ytEH0pqWidqS4B>W=%J!3F}<SqbYD3;Q>!s~A%?SX@2`&1w<dG(*$CcD8hIE!WzP54w*JI$j^FcjQ=P'
        b'(#jVbu<+j5wc;&UOGyJfC*Q$aXf3CJvGxPpf8mX6^|pan{jj=pFf(_M3b#f+rlvoFHIwrp-tFA8va}$g?azbmKZD8-I$j#I5K>@S'
        b'dcNb>omAR+q%D8YZ3kJU2~%A7%fO0}pE&%4GeV-hNHvHoosz|}w2G;hFks`tCEx3iXsV#8$`=~2wD|~t_)PL`bld(x_dZZZT>?BF'
        b'4$sw(a_q&e$?sFf;}r9&0l}E{404MJ@jp4iXMihx;Ul0&Ej@)7-8%rephf=l;C<VQGE?eJgP<$fn8KYt2n~P2GQ-mVG~!-27+a5l'
        b'5R4t+>IcbboA0VZ@1{I8(15p!K*N?km?*mgVMH}Jvtsc6ofd7XQ=4TYv2T|G%8D&l0A%68RxvP~KZV$~+yFQwcyWq-04I}q5U%nP'
        b';YlJp)^ZlOuygR1AWMhDnT3ERT~CRM_<59$^*!&|Kx7Arz1Knj{UFEuz@=j?U$p54-TFa?ez2ZpEWHwFo2?@vf<A*!hfzyDNX?Gt'
        b'?X~YEq;D%)BRYp#(s4kjptR@i>eYy99dIlWR|e-xlK~`7Eh*Jf8O<IJGBzM{cD&4zg0s<70(3epu{h5s0Qa;TNSkWVtr~O$fU#QY'
        b'xhWCsWy@;Nw!ujwX+21re9$c)boc_y&U?O>)OO&twM$f=qS?!_@UJDn6_D3aai~R(+tJuSz>}7A;Ot~C7rSm_@OIL5-&SAObu8gF'
        b'e@=IDz<WRQF_E4|j(!HfzrnW13a_<I4Y;QV93unu>@${sNosJ{27D6+hH>Sry-S7wyBP!C*X;Ki{=4VicL;QgE%$sDat;68HTzx9'
        b'qHvCnz-w6u|4j&U-un$aUhr+pLdam(4evdp`)R8!-*W<OfVV_vBH^P#xqIIuv)`Zq{O;kH<^jN|`6Yz<!+|KY2A#dObq~hV$uSMH'
        b'Fdy(RmXZH}ad|lAy;+!g00WwXaw?jd-6!+5cavkPXW^;@IN*W)7aW-Wz{4B#_C-ju{2QbRJ}UIp*dcy>!4GmhQ#N3imTAiAGJ`#^'
        b'TwkDM4i6MKN#MSbQd`zzwyaoNmO&_&@|OY9zeZ#M2)_!8u9ek@p7jOvXAZ&7RjW=c0shoZ;7_?*`rDrDuK}~2nGdtvm-^d&-d}|^'
        b';7~SLVN#WFN1_HV^tasRgb4%i4KKsnD->*%6%5Q!wW7+uAf_O+0Ixv{P+KPIn&dR7;IFb{%=i7!$!EuzX9w=xqjDAFp7nQ&cMN#%'
        b'btNIp_5mjgmnxl!e2NcTtWg;_=vQS8SZQk|=DE#z((Zb+gx3$;0_%H1#(WGLKynpqB~^uac|%R<!Us$n2DEx>?0Z4F$$sE1gD~>c'
        b'oVJt!cM9O{0!PY#1$gZnVJ(9GH?18Y;i{UQAeGwi(g>+v+o}O~0st;<h8ybqL4|N75FHBDI&oY4fcr_1_eOIcl&m3#z<B<dsC#n2'
        b'v~-{qtAPu+sqqM7g!LC*`+nI#+meC0WdlvD%N2p~i_G3Gx~zb3mQq4+yH@)9w&@1kQK06!gfBUZ`EL6$g-$)d9<#cJxOS(a`dIi7'
        b'_mJ;tW>GNxsU^9lg#)nFFeGx`oVL&bcPOajqGSGm=dTi%m^doR4w}>U$bkDNAo-&N-mXaH&%|sZOg;ncz*7&a#DLvnxy3DuuOvJ-'
        b'ISUTtk4(+=lm2kA*^Iz*X}`D&LlopdQRtaZFuvZA74}Dc2Kd!MeyIq~e;MHGS>L{cV=&kf7*PH!AL5;ia6IqAaWwtV&pJ)j$7vZd'
        b'a}|tOd#Zxp+|Lo|zU$LICht4Nj6pa66d5#!45SRXTJ7GJm<&VdQ9ODHIWKiN5=`rzNNh<Xs94w52S-hmAgpE1>|t(sOIP7Sbg_(S'
        b'_a;#`6Kij@Z9|xUc~hL%9!CIsL(xZKQ8@DjOxNHLwz^UMS$`D~B@%n@M8l(6Oe<e7)#Qz2nV3s3Qv6Z>TG95fkd%wCcO-G*cxd~}'
        b'3f_FQOY@b6;CNu2fs~5b6j^Y5!l-w?F=y{%lN{ez9goB-l5kQ98#aG#7HlU5A$`h4n@r{6BmR0vc7I(>f3@=^%*LW8E?`9kRB?5G'
        b'U2K0v2^n<c0=$A~rzBkpM%Q1g>xb)){PyF|KwEG3k+QSWH}Mw={M!#I4%+O}*EM%91tWIF$7invSJzeahpe(#xGl1yFIqm~T(`LE'
        b'=xX<&I-quYxH3iTIUm=T9PL2GAqbMFZnO8VDi1DiKd#W0H?nl&vJa0Ohi4#<9LB_tBWkAqO(HsM)x{$rn3zJ;_Wu3Y@0S+Fe)?L;'
        b'b|N(kp)G{^<^H&E1C}%|I3^C$sN+Obe4_>h{f~|(G0#7_mL)YJk4=(pN)pBKYpw{hv%mek;@a(ly(4qsgzcJB_`BMA>sjB<H;CZs'
        b'kC%OCtZoGMU2scm1=jo>@E`K70h>V#Cqv!S{q0qX+G^_!43@kajnqdXN9UYbxU_9czk5r+<A3_=*@5t#k~0fK;pr7wrTS}>t!e}u'
        b'QkUL;t-2&r)RZY^(&1=b$}CH9Vn}d#aJAEntlk$)H-E&D_*xv&rj0+hLG2oYo2sb}tZ$N8+qcYYm)ZkY8p2EkeRcopT@@p2qJ4sX'
        b'qp<vvqp0z<vQ!6p3H@5}s-)#M|B3><fV5}x`rnIez>e1p^^2js1t!}T8Ti>P5es*t!{6m}x_)3XtJYz*P$aT!dzpV7-S4LQ+kE=$'
        b'{+iHedwvvUk15n>mPaLOmKR`_^IY0iqAjZ59ob*+Fp5R|lUzX9%aF7#q)pxLR)ciCBdFi9Nn*PMjQqW}RY+PH(q5pr3_184X>fU7'
        b'7iWk`xWNGnB1bZ-OD%747PpsWpv~3H+0|u=y1RYuJAG{(y%l97c0@y1>VZr+U+I(~E!WyB6_=~wF(KJk6=*OWY!^>@{UPSbzLc5X'
        b'gE7fwd2|f${*q(lB(`ix?0Y1$uh+<qlcJSpaY!d%7o`Fv{}IP-rV6iBqJ<T8eSM2X%s?O9W$y0V94{X6u8CXT!?U9aGRV@53;PG%'
        b'5XR!1Jzvdq^hHT$?+eva##F2NyIu`uSJDn*qv2;H78wxj_^P)RW8apuPc`<VtJ_w+AO1ZseZCDkt7s)QUjWALo?f`LjRILH+>N=~'
        b'ci<X-HAc8TUEm|=H=}Xy?v}o93A>~QvrC~8*{nTQ3XP~r%r3KO6ovLyF|gxd4qk&BBn>iye+>p7r{M20+Z>{NWkRGT*yg|@HGc5s'
        b'lGCry39Z+q5}Sj_FBx4p#Jt}Zsae3h*O%`Ea6s_%GWC7=CEw5voZlE>YWsNkLOaB~3VaN1O=i(z_1k?ZuD(P}0}M^33KHpq8-+W8'
        b'cLD$D7!u{L0aiVb?))LWKAGLWL2TCmgB{{3gSn)yMp=V{?A7s$WvUl{fHc)RL~LlT_nbLz6EP*Q=FCHVTV(siHQ0Vhy9Al(DRiaM'
        b'D7A-54G&Cv9@&qjMk1-<z-WQH`Xc1pWk&-V&>9Jdwj4~v4QOlt=6I>kAihT)-VSAuD3f|`pVKY3V|ESnD{k9OWr1Z$A9Smh6J_az'
        b'o62$Cohietl~kEeyAP6f?QW&10ksF&6CwPIcC^e?u*tR+=(+}(Mp<bB-GOW3j*PxMxOe4rV8Z#tOe7I|0s|6O73P~xsJ@UT2B=<^'
        b'ky!fjC<QsPQO`@iHGq#aSd>De0F>J*X4b*3tIkV7U-0m8-iMOVp(sr+JgS70#E|(tKI)d9M09068ikrneKoj-@SclIt02g!jfTK<'
        b'{~A0sTm@*6>X2@%kl8{B+ohS)8ngzC97LKQgT=B0F+#q#x(<wGENqt1^(~g=SNNDe<kI%ug=3@IIgxM&%w^BN0Vb-734U+Tfuw}>'
        b'(U}AtjsQB+G;I4-Sz7d5jVWE3V^L*?q(85k7m`k=haa6+sc$6;iW_i%i@g}WAwWthO{7E<l)h)*Jam6aj%`PZ>a7JC8*ikoSdg<h'
        b'_B1B8Agk7G1ixF6vXr8&H_{RUi?-cJ>zJ=1e6r{{eJVB4_bjmmuQb_%Y?`1n4Qa<JO~M|4Dw-sH#j6n-)2g!WWZv%8h&5jHmWe7&'
        b'4AY|tDz^4$ZWN&9iUw5R(^X|ax?b5q9X*|6YLMAg<Rdqv+Gk~*Z^=km?Yp@wynTW$_GLPID^2NAF#l7-QP7=NWvXS9{BnPdPlI2p'
        b'xS+V)@y+h;%xMNd!kfLAy|~Qr_3p0BDMqq0@a)%D-cnS*eMwds#GbUCI3=q4s(0h#Xag3Uop*~PeL)FOWAtcV4@U-;nRXq72Sv{='
        b'IGMBWv9MjQ-1xT3{s+*G2!Oq~VOMtJ%E#!o%f0STdmW$l);pgKM<n)Vy!mA*6&s4O8{wlBq?BCHAZ5>$W)$RFFHo0Ez(wx02iB0~'
        b'4hZN_9qeuJNvZ8^_0@;~U+61M{ls;gCs^Jkj(NLR{4vLz?9KZK@H3Dnc^3tn1I(dgy<qHfu%winh;}h>Hqv$yIi~%pJ&|&i#80)('
        b'Z-1ISCI1Z8tVcGN9Ra^u<m8G<ps8|XInAKJ?wp=omaRK7({79HrYbZ`gJne!Y1xR`fx`8kO2gUARusV5(Pw1^nW~+4?~n0XS>Mh|'
        b'Q(~q)$oTwLn?`;q1;~J}sEpI4eCEmM2j->0qzToes+_kgV;aQpzEKy4JWGiCxJs;nxD*6nNKmBktyW2c7|a5n9(bKOW!Hwr7wrWp'
        b'FUF*O{zKY|spfvpw4*oS8_;*N155Y{(!h<-nNoEYAOe*|BUup`z!flA#oQbQ5<#KLpSwR|f8<d~<zua)0(S!eM3~)O807g@tcsZf'
        b'fYMf;!4e)rHXjDWNmzoY#(f3qyd=tb9n@7-msFfnr|KXw=k~-oGPZB6WO!~bw0k)vtw#z-!puGyAg*LC72BfGvksskGQOlT_BDd^'
        b'jj`cvD|+24dL8E8`eUzpu8S8*t=qS@LW==q{<j-|EN}pg&GSjCl>MZ17vPf?>TAZ1efxnuuz@Uh*Z4tBarZ^ri+9HCv=<aZLXad+'
        b'WPK&mFEV~k@eBi}LaPrjshEYm;u#LI3xA{TvF{OcrouG8m(G;aVL)UU1(Bgv_hzZ(8Z1%;36U1<N2?Von_o^^a;P=(G?oy9XsIP>'
        b'dq~wQzR4hxMP{iL)N@wqv~^d;`n1yoWofjrPi{YJUPFS;RKU)x5!(r;TF$FYK%#46@Nr#S7St*!i2~ZemI?1++0@Dp&bMK`ZoJnq'
        b'(^G$Zj-^GsD<l5f7eIv}Q`^tV7m;vBHV;;~NZj1RAtA5<8~hFt!xt|0!$$VcZ;*mPeO1=7b0@vA9?ScR)4+6%zF%}5CrOZt@jA!p'
        b'5c7NZKrbZx!2c4w69)abCJIom0Vidy%Ut-&-0WKlK;V8pdzL_bp@+2iZfJS_2~mxx8D4U%!I&=~qn?QI0nw{HygRJFh}+(svBt>j'
        b'-tB>>607g34$j08-laLXzIKdaI$<B6cLCQvZz63U_P9UnaeUNM&+ZHVK<tXVYu6Vy^;i!!=AV;Q(X>NSNWdfd8XCGi4Lv97dr5y1'
        b'Yo3O7293d`IOBU%niFBpKqP>%P$=`R6#$#*RF6%AKJdQAyFCx>(|Yc5_h2m{!2S|BSv35oxaE<%RkRmJ*AJZKCwHA$IL#st_T&8r'
        b'`oUDdww*M>tb>tCC5bUj-4C>z0+XvS=0Z2Wu)#M9(i<>g-@tLGhZ%VQ-u>$yVL94$`Yszy3F{zO_?vfU>$CL;?&Aqqi0SUCJJ92J'
        b'y_=j%wU0-h#cntd>O$jH);RP}irEiAndf^BbVJuzO3J*iJ4yM^drv`0nb*AtpwIS1$>XRbE%iAbg)B-IHb`_iJ=&Z8!eT|?F<o{K'
        b'^f|@w|HtaK@o{u(j}HO@DWcBm(O``Tf^P27$PHAY7X3BI@}9O5&W7L-N+N<Lff2X~q6ZfV5hfi*6K;F$VWFwC=Wx@y9)9&BWnB;4'
        b'HTR6*{3R~~#$O^#!dxO^<vOB<@W}5*ZUqCl%{6id(n*)l!viMayh#M>e2bpbX6|vDdmPIFzdaxRn%MM255ID2>BpHTd)i9`H@Hk%'
        b'LukFnm^>U#2DaGLx*q<$w}nG$ZBL$e?NnG#wA_ApJyCe}>Bskwu}t*dxwem@(Er{if4Q4KvbLe|j-N2rvph$!dqbw+n-wPv^GYs{'
        b'KH=-UJW-@CWgpF@LgoB|hwZZa316!|w}k!UtN4jHtoBig(oht&H*eN&p{&nSWqYkQs>lwqo);b<fa?cdew=M<_B&iEO?LZi!ZO-?'
        b'lE3uXgeN!qY~l~$kaDEUA32R9b^gegIQ)+R!<-!cv)b7~{sNct|KH&&TplabS+?g@pTa6TR;JX@uzC2{-+#6@`)#Mw0?|rLBjXJx'
        b'Qs$K)cB#sKw^9#nEZJTDsx%K<SY{6_Oy|>~H{!Li>sq=)*3_V2CNAxQ(g|IQRpJdqFwJ}n8GUt3cIp5bT;t1J^zuE>r)qb%$=yxU'
        b'L8O7_Ffzz{;Q`}6O&7XDB87VuahUF0x9L1Tr*Ppqd=##Jznh1%dO`RPP=ncFH9nYRem57Sk{>>lXsYZ6iKY|Xv#AAbu1gZ#@oqAV'
        b'Z-gX`-ewv|GKhH(Vx98W?vi&KX%Vt07fj>KH@dYnMXx|Ya1sMX!F4>&RHa)qw;yX2lYbzCqB4_GqSR4}-=pR3D27f^GRI*hPLwKh'
        b'yI<`ts*pQH$aS1$*TVzqCaT0ul`G=Zu!4KVO;NfiR1g)g`b|GtJ@aRnU;JV>1Sy9g#D9Uj0zn*my2*m;csY+I`OE)ClR41MYktQL'
        b'P*;@>W|f<SOi-&&tGJ%!-#gp`!So`GoTt@>+1obyE4L64F@9U55$mM-i_@trp-nASr+06{JReBNpz!x4;ooqcxtw}Kw`qegXuCH+'
        b'%9~QV?+po&iFfT127?zkM9SLkjC*%@1R1o5xW^AGyGeMtIUV1%fxiI+57j2(8S!#n1_@*QWH+gTqx_5RhsHkS<&1|}=0Uz#0{Oyx'
        b'+<31coxl?5xbcC8u#`pJ$?@`(N4ve3gfJfDz!KvI`F(6sBDyn#Y}`ci{U#pjj_G3OY%`3q%d6nL`@}xo_wIU!IK6MMebVW48NCY#'
        b'{4;evjJ%ulnLWGC%;~0z*4O!U50#_*lTo$h@;cw{+G_a&XQC^mb&_uC^)Pq`t6cGL2G&iL!;FlFGRmaXBEnh2vE}kzw8Hxwp`g!-'
        b'4|mOe&#qHbdr#hAhPxcYU3^jXaMx^A#r<6m;ZCt*-uIZ8_AV!D{qM8gj+<Sxhr1KTXWzW)au7n*q%X*%oajSEobNz9n;eL*ll`=`'
        b'@uAw<y6C36AlFgdMZH}*Tg>TL#Qe2$_8h7D<1S%M`=|4S?~6Rrn7X3V`saBOfpgXFuEH{PW0&pHUDC%IRqE|`@wqO?2VGhk6}m{v'
        b'9qT(;yZ7miC?9ee^UA$8OsBdIz}Fpfh*U?rH5+zt2f<%uAoDWz!2-W0OmBB>^oKqa<ST+))3|}6o7(vmd@`0K$Y5%3F1aD3l3Ja6'
        b'm3_v^W>Zh+QaQPc3CnjgjbA9J>lC?&3<l|z>oeEI<l}tY_3g|Zf}BGxCZFcNJ>S9aUy{$xeqW!t%I>=I71hLosgA-D-^`E;$)ABT'
        b'M;rVg#J^@txn1h24j!#Y(IkIs^uY7Nf%7OrxJ0@lS?D&Q&gqK7`1c1>!=U=M^0Om#8v^>W#TRsA4Yj_M%)ZL*fIaw4DH*$1WVt#+'
        b'Zb<mw**D>Kc9CmGq)4kDzyaX+tn0HGCcBFa25BH=Ex;5cf-;K^GK(OEfqiU&Q;GSXuKJS*&)2>&fT!UNMS%~r+QVRC6bTbg%HP*3'
        b'Ue{G5s2-^f>txn-!DC~;>Waca;MF;D=9gWwnrGHdUnB5_l^U}ajUOqI`q~eClOKmJ99m=(-xc`Pb%%>wMo|?_MRg|jg0<*ElZ{2r'
        b'l*nvbkt+Z4(5M(P5Gv-UrTNN08_VV^=a;ZUr1VHh7a2tcIvwrs))%=WVTL2)#NM+Ly2vhGyckynL<G=<@eyHby$?{~t_gTgF*rth'
        b'uqg?vQpV8*`h+Qt3GCv#$!|GmwE<Qe(f75}VQk5LT1qYl5%Cxo;jgf<LlL1LC-iZoo%FAfHV<%XaexyU1CoFb)1Fp(XRVan`ZSm_'
        b'?ZO*$naI<4tWu$8+1L`Sc@3gxhd?B64Ps^y-4C5$<ZyoEcxHMw{OpWwvXh(x63MmXZ-hkGX*hHZ9dPK-@DWZo)k*zDr`6XN4|Zyo'
        b's;x1N<bDJ<TD5h|NT)VN0sI}iF7oU)M|WpkcPD>)uhuTt8Yt#F_!TGPdwSq98zVO^=Vh<d^si1E&k6>j23QO7`znU{q7!`Ejw4<h'
        b'g3!I(5$6L^z0QH-lg<O5&bDDpq?k*vjU?DcqSSd3VFh&~<-Z+Go!}cj8yN3xcXvk(mgK{@VRfd4PNt!gpC5pkw0fbvW)DXO<h=)('
        b'U3a1LDoX&`Txq3dDdssoqdRk-V!{MCHbaIb)O+WL>3FAb&PX4IXqN@FOr51G^_CVc+aL2B<%Mf@peDjU#I&r#R{akFP9TAP8{+zm'
        b'JFE1Z=0J&?9N+;YThl@wWL|^#ste)pVfQCq_|X})9pZxB$Hh|t2k)01!j&2g0my8<FA3~~`lU|FE>}A}lpym7^^2XR+|DFS{rgVS'
        b'@A=WgjCQ$cf2Yy=z%$%3;cel|93X+`ADpF#yQdSM>Aa^Ci??(FN<XAe$j!{6j(hh3p6UF}U4B?7Ezu5!DMsN{wNjn7gL3fr;pTTZ'
        b'(7bh(!rQ!{wwW!R$<+#Lyc`Uq<EhSj28E1zooGx_w9h`)EbyA_z<a=AXiri+oOlZ)dS#5vvAUD`oDkCYUU?Nj%B}Z-?Xm-(Y3=f%'
        b'>xwG^7BYvillln4Pswh)`|sL9MLQ?AaxiZi7Wi65)$TQ3mtR?<FkXkL-w4$VwJ1P6jdn_>>*VW!(hsi%7+1@U!X0f~_h_g2ZT>+?'
        b'9B6rCwY;c;SA)3i-B<PO9;;2Ry&$i(Q~Gz|QxaC|UNdV2Vo&#z&Xv+gfjS|bR<BW`ThN)$zc&l)<-NxH!cl<p2XJ!nxUikB!4JG_'
        b'q~-jxx^Vo~VrlyM9y^yEgyn5PoR{yCO4gjK?&K8<mYi;i2*dKy5s3v8Z-nJ@Fq;FhX7hKpG3IUuZ+?87rBTmxl<=lQ4wjLzw<wz`'
        b'uJ!ORFiCnOPr_$OvIo_}9mOLZ+HDG+>58)D#e*G1VC=nB@?gwjPjPRDS0iJ{*88v>55lVd-QjI;8^BWh7;+^S1$pjbq2<gkJD84J'
        b'5J9oyw;u0&5Hm?0K8Zc$1oUK&*{<>jBIs;{srNvA^%4vnRuA)W$D8m02o1C%RJ2TesY9?xB2AEk#LPc$SvM%WVoa=iqXQ6ze`XLU'
        b'SKB)rz&^uksAdPu<wqj5hD-L^#S4cb^jMyYBZ-9LK(B-~JGqDeO#C*NS<qo~@&hIIYB@0g%MOqWed9ak&g~Fi;)Whb_+v-&MPYmm'
        b'Qprs$uZ>Ii(mQ|u%x#gu6Mf;|bJ`WQXJw>ByVRLYuV<n??$<i3p*HJ!oAqU9@~=$?Z9^I~IhAUA{g(A-rW#QL#{3r2f_<ftT#&yM'
        b'eN$4~)L7Kgn6^li|JbjpUm+K4G@x&i=jrIE$Rh-aZ8sRMyoLI1&RA?BRVS9Bq}Z2^jxah*@~tTQ7FF%iW}3+0jmxll7THNhUuY$+'
        b'<IDz+_aRdf<5e|pyEd4v#GtJN>37A6YA;aC8Ug4DU$6b0)1m(A7B6#j+dF_rQ(HQC$-|EiuYY;jb5!Zb=%~x=XvM%7Ge4hgNw}-<'
        b'bO(PWCDr4-{<5Wme-hNOv4dI5^Fdlid#wW4nv@-_tv6XOP>$4&`cLmL2{6~yb*J#Q<5wO1lI!ADQ3JskJrCT2Slw|)+%LLLz!t)%'
        b'Im`1R@7<vA>Y01~zS_Iiqc(O>p)BbiC-@w~A_*AE74yB9yVP+VR2ZxKxktN%)nG?&Xz*Y<3eQ%m)Iaxt3=LLTzW`I{I_S3$D$EwG'
        b'@FU?GinnYuUv?2Ji@<%elc2aSDBhQ)epD!Z6br=Ek3cX3b`;mMh&~G*I(bb7!&eYw#R5c%`VD>YTU7ms=ib470~UzKVH)&XrA9|}'
        b'jvCZbg`7gP9sc|p)I5)HPDZO|4Y<Z%uSB%%{vQP(00h<r$G8LcQADYC{q$y(E)(y_pyhNEF8puMkG>OY)F4W2MOFkMYRvP%Z2}UH'
        b'Ll<BgC5eLyRWzbcMOI93fR?(cTMsp<ZO1_#54Lbfs9?C$Gc?Lh%{}_N;jUYJtmU7>JwmMTS5uGp4Uu#GhJ<?!n;3Xjy`Zk#UDbB('
        b'`x}{xkxZo)$Mu>1S_FhDEegW<S`5Cuj1*B#nG3FF29;z6UmCuumY1kW+P&+eE-~mNIfUrt6EP?mgI@L^F%+N>Qs=#b(byu_T8%#%'
        b'8m&fQ8BHJwQs>{KUT{?%RH6>{^MS*QTt`3~ul!r==SQnmdi8t?@u$^+TGXGy{Pk*oO^O!xH)JO6PG{gjdwX4(yRz-<_dI?#)QS<c'
        b'64V0drhfaDzKH^6ViLBRj@3`i@@8@`p1g$!!L=J~I_ItA7_0fBJe5T<wj%rSeI@87e09vqn9&Sjys38l=+%DYm2S>&&e31dzs7(F'
        b'nfjR|3-9u~{fk)e^Th36K&1PT6`c^|Z~8|tDn=XkNL%5L!ri}j^+%8UPabm4b-eyK=4^^%Y;c+tUjF_?Pum|nb${?Y9pbsfrR|Z{'
        b';1-my<Hh@+a8FFXjui=lHXTaP95SF4gNKIU751FK@JQl1JaG$8Y(@|uf`P~*gnNgFkNJ6%!h;AfgZXlvP~zJgeA**?F&9O+f9+{o'
        b'bCb_h5Q~YtelA-%$se%BJs|{qBMSH&GzwqTT!oM_U|kEc%iOd^I0x!_4Fe$*RyW81PbEfT+OS;jIYeGnrP6b>r>L}}r~z9`wmer!'
        b'hu=ci%Hrr?csOg*4Y*hL?dO$B=I1xz&Y4nA%a_>=bb&I~@T~!hQ}T{_rJjj_**02Urng!%4wf6Ra((PMQ5k)(pg^A;=0g%I=biN3'
        b'(A*7F5!{Y~zJ!@pMxiaAw`n|Xji)Zk<B0NjbfT;e*Btl(zW#BLzbPFyCw*+Ao@@*CxF7M<(Vk||9{=Lf91`1jb`gIOdIb=GDD3M9'
        b'mz=y8c_nnQEL#fSa!o&6_?q*>Fi$E<2C!kJHDXU0lzzb*02qIYZ$*N4ofFWa20!|=U0+6DwioD+7;rmQpg*f;?%cR{wh_?uzz;P9'
        b'eC^H(anoZfvYNuQ+P%oS(2jY_^!$lCy?F&Z23>+dP|r&OTzqPi9Kz*>b_6~#3l|Un<H=tzxR{+vD^)8{ps#8$%K%px6uuqxjR6Ik'
        b'yZHZ}Qlgr7yGHCvK=Y<J{(mnJD*F%c5%?8oVUT5;7q*l0o;SXB%YE&Z<I7w1jz>HpqHKSe>FZnOEPs+PX9Wm+QA1evV)bCKMk=wQ'
        b'L$)gA!HQaY<H3XFwD35>jRO4v_$sN*9M6X<j+90~7BV04m&5<a@B~`;BHN3zHH7PxyRf^t7|o*mIarvz9?YRI%X$p{QxP!E5T~=Z'
        b'+-CtonU309E`L$W7j36+x!(f`7U4gTkU^x6u_CvqXm5k8Wm;QN+EUf_&Mo&z0I?%sgd?TKL#4ntZJE*@%5AA^tGeZOfvlZ*z1-9A'
        b'>F)x#3{!^YFCg2F-E#jGWbJLfCGd$Fv9YLjMJ{cbYg>_!B+^^tWN?kh($A3?ZBZ`v-k)5HeT%jI<(B&}DC=<K--3r}d_-EO?PRDn'
        b'x@o1-7iPW+GV7WrIr`nVPt^Oi9lGVVgOv9YMmgu@^`3bmI17W|#a`R0gjZ#%P{ek5y*^7`fF+H<OU6Lwc|4pxOX=0$_vWbODGWGu'
        b'BpzFa8ff_a|4{ZV08v%j-}{`I0feK@03r(JFfcHh7N9m@6vK#$k8Vgl(7ZQ5K{UIeQBs$327C;PHKHjP)eMRvS5nXnQ*I0zVc|`D'
        b'qC6bXNi!=_BrNoNzkSZ2b-(-n9_Vk@KKuPxd+oK)*^j@op@B+s|9!dBV%}zH9WK6Rd-Yn?&hgfluBGzQ#ycvNJinxA`8C@z*iKk?'
        b'k55y}HNOTUuj$upsjz!$T{mC4n3+48Q3XhS>PXX~YqpnQA4ylQXk2{~Tna2i|K$U;oo>_?r7kn&tC?d5&;v#al4a@y%DdIq%YH4K'
        b'wdZNpC)R~7@voo?w&uF}7#|+u>2qA-<4Ia$YhX<mjMni!8;Hmk>ctPxhaJf*J>^#u;-kM;`ZTl0^WCON*KE%s3%dGKLi=d8`xNw*'
        b'd==#IWn6^sNF@Q%xt|l-|NjPAMeQ0RE0|IZQ{kfiEA3P+rE#n%AmV5S3tVGKQDE8t`n5_mHCC{h{0E!K2r!?mvdJqLbucq`85PcD'
        b'*9(8$K73GxYiS)1=XoqQtlq{~$CP{}Pjz7`T-7#MtLL&}QBvnUaQT(5aK+?w$|YV{zm1V7GxV&ohAY9GwTU0=UcAi6U*$ZGj6ULi'
        b'WMa-Tuc~F<bXmUoTK^hY+J3TYHrX|6*VU?$_fxM*<5Z=i>FVA+TfM5oIWLc+N5UI7(m>)ClCh$0sjSU}SU@tR=jl>&q~rK6>6Etd'
        b'&b4c=u#IP$E?>3Xx>~hsr1kt&N2|0okTS}drjDz&>#$Xd`;I8D^iW=DyK3uzbwK?c9-7d~dMe{wM=|Pf;m)S-G(91a9LE-X`G6a4'
        b'F4+<?oSwC$a+wTmR8m2Ylu7-7Cpm#>ZgW(@p8ImZ3NEQ7e7>}CI_J5LA%vb5u$W}*QL1CuGRFAT)&2#=RQ?7J@Ok}yNqvwqL74&`'
        b'oVx{bS=~!~)P0uVElNvf{g1q#N<3d$HDz+W^ZZVsuUfC#K1H@|*5a#FApct`_J+!<w*9cCi=Z{qR#p>~U)NM|)m9F>uZ44kpjjl)'
        b'5vD?>4iZXuEvuVjR~=a>EZm;#R|GLbMc_4(6`1BacV&=g$WSi~w^GMeKE#U+*)bO7@(}Z{3L4;Z`vC@+j1Z_cOlZ&+<W+r(_>|nY'
        b'OwH9<GJS^Mr{!NncjBnS*a{cpda?ZUm~7#&NsK^0@IoI)yREruTXVIlG|jr?YN`$Grbm&^H5snjR>O9g*lwjE4BbQI&gcWA`6rtG'
        b'e$}=Lj;~T7=>mZ=C6FYb2YpI6#;8Z52TggBkjAGfnAC29GH6(*#PLQSqT`R3u$rBXC36DPWUj&@`2<1eC$N+MWJgCeM-c5ua;q}+'
        b'7czH)D+a4Kc^`Kdbey`N(lZ#mN;lC%CsfXk;|P4f`8d-XD10#K^pW+@Nn*m6e5pxTpWZ19EBSXYY?L;W{!vA(q@#-ZG3Tg4cafNc'
        b'3&Q+adWb81UXPR<ek|rXD|nw}_v%lG>y{#8o)ctc*j3xOt5v%PSiP^7?vsigVDwen6R;a79s{lRVk`@kb0;$40n)MV`DdH_uG&K2'
        b'>`7Pp{gn+rG1KL7Vv1>v16Qf8+LUlg#CQX(3=`-Hq;UcS$`yK^u@@^Ie5K}@?BD6aj0cRMmHeqrV`D{4<xh5#p~MXqWm9S^nLBX+'
        b'gw0~!=WEwQX{#D6DskLn%7Rj(n6d6O{(&rN`b3cW7+O-jimuu7aMrYX;DZDUBOHZQ+9Q0DxaOnj_AqJaOQpPPbM-{Mkl7m~u&mUF'
        b'WlB!SOKlHpJ9WSVsGP2XsHVH7Q1dH<0=cm3z8CfqWeATl^n%m{ywB)+KKlDY_I{>mRd3DTs5#;Pfl5W!MU(|`Z0dBnw2@`O+WoSx'
        b'zSGv!X|3$6DmhiU1+vd^8G?^9g>%FGpl%7%W#^iVtGv(62RSMUwRgEk&rtYKg1%AOX{+n3+EZk;be6t{z5zWHZT7EDTMcY?h<zht'
        b'5lInrG?yYq{hd$`ot&hQ(fU4KGoZrB>3NJgnKv<zG#<j4lAX{O)7+k+?5WqjKQ!FJU~Eb4VIZ=M#Z>tlE4=>)gQAKtEbG);92LYT'
        b';l5?U7N0wP35)5{(1#kOKDPcR@eDf1sH{%g_Rh-foz~YnsXnnrn!`?M^i6%=xz8m*82_mr*CHH-gkESuR@|IhXGGl#-H=+k3g@Fh'
        b'6NC5CTa2i;H?E}{`e^6-m>zUD$GPWdlO)1+N?LZd%2JxgOj8)|*injRMci4B4|l|7pTv~K#ON1!`Dg}k1N`0J*f4NMb(II%alC3~'
        b'M81b#5$BdOX{x`;ux?R$N8a(2MV_2X&LZ!WMMF03%%f}8tC^DH{_1MR#P}B(@@ktE4QH#H@?M*<GxCMVo$6nh5^Fp+v&JQ5kx$B^'
        b'q2)V`XKC^|*4Z0!Q{qU;@g&FozMQj6O59xGl?Iip|6=w^mJDSg>1y(vNf9n~QO<9k-udui0XJh@XX6gxcpCAN8Y;R66h`9TsQ$GI'
        b'l+U6&ZPA^Tx=yREQ~ioGM>W*PM5<Ii^z3QzUM}H|uOwqsr*MgwG}Xc6oMCd@=FDv%WoJtNA%#%;2W_8V-|k>dPt%i~wkJC)Lp!Zw'
        b'I@RgY{`C~j1A>OU!s=3U?P-dzu{5Vyl4GvckWPA<;=h>9!JUHgUpAn4V&xBZ`w2x^WK&@0*WWBVdU1!3a;4Jh-|6_4>HEy6q*)Qp'
        b'rY2d!fmhu2q4Xtdp~v>2!wNz?H?ihxwf42S276}fzkgA5{#Imm<hDLhHr(Y$;Uu{(`irSgeH-uC#aOvc@%F5Olft36%Y>SecnEiC'
        b'N$MZoy;N_Hk#y3XK^oyGHQ|0n<Gqf;rR#@<2(LkD-r1aHhMs&nx8!R#^~X$_giaW%S!++n#-pW$%)`6jNa%P&cse`vpm$hThw!pl'
        b'@F#e}ge|6-T9yP+&s8c?^^Kc)I}>oWL-?{j_26g17xDTZg!9?9Ua4T$d-@tbviC0+GP#)=wAJGrUoulX`i}+7uQqP8_q#<57cGN*'
        b'2N}(F;c6(8FSY-M?(T7~@9N)YUE4v&{Zdp?T}Sd;S7`F?ezC$Ao|qi_k}Z!5A8Cd2y0W~rKK`6n@hVe&dR^96OR8bLD#D%fTB4PS'
        b'uX*f?6w9^>{5jWmpzzU`)}edausNF#bog&K?^V(j$m%udCxr?>Q^85^RfXSM%R3x741P=TySGCv{5p(`bw@`kek~npBV)|(*lg(#'
        b'Z{IBL*!*#ac)%0vOamYk2f)TuCvevK&jtBDz+R@<P;M;fu$L>!%QjZ2S2NIV%9#~gXwWRzeZOYY+2XQT$5uvYY@bY$enPL}rXE%}'
        b'x2A1*#yOoUyN?Rmjg~d8=@9C7Zep)c$oyu36xNv<)*oT(Tli&bgmnPIqFGX12Z4W$r{^46>AG1}fHxhaKVup%H)VF%Uhk+X*=2pP'
        b'!!b?@rTZAQUD08C6}F|K<jx5ga#-WFc|pgH!u%smFL&6|;kKKe^;lq~?^cTFyYRA@?ZZ8qQafzPaQp;=3$2&{DdsR01GamHZ6Er?'
        b'n`h9OxzQzYa}Z&fu||>?P^1{e+_rg(=Nzg(;j03M(9@}S&8!h!duOe?&x>=cH)p*qjhSz+aIKM!ig9@NZF0}P?em+YMp|M`%u9B7'
        b'^*!fqN<QYEcUg6rfq>M{Q3c5NGNS@|XK`#<%qRtoKjSMU#xTboq#=h?YvzR;PTW$Tl1{l#dE2tc$-VYMg>ig`b1j^B%blB%>3Fy%'
        b'VMK@UhPnSc7{UekidM#7?T_C79##!%3hb~2c2ov+Sfw56$D~G8htQ=pbQYlOu#M=bRCWm0lRi9yXC*WDru5OdbDkX&RYJ^jSs!b!'
        b'J^T04l}x~WyRclvPdLDtoqJFgaNRESRgrtTnI?}88`n|Eby&Z%m-<K@ul+8@=%fFQ^K=OyF+bUb5sG&Bl|r{)nL@<vh(sue)K4XR'
        b'H7vFAvzqKNJ856k$U+YOg=3w)Yn)<Ytnke??znxtV*0q47CY=9XN33ehXbi<Xl=AR{=ql{Oj3mXVAqYK?%{!C?hC(~g<bK<M+7<H'
        b'A~18KDf^DFYp~wICs&CMrik>2!r<)(>BP23w(bhQvfhnOSK^t%!}-%n>itWfhrF;C*3%Oq+_xW-iBi?RS79zU7(cb6(`9_7w3Hc2'
        b'r!wNvto9<sj;%rmEvz?vjo#wY4pyjd<->#(9rV4r@Z}83`Dx*7#~pTh0OpI#qh{G>4;A)N#<2m1?ZsOk)rm^juNlc&H`&$8sQ`ZH'
        b'BnHr@^uN;FYp1Lb==ATjjJqOOQnBE)>VHmWHLmFwLY`9p*}CjMyj8PR-$XcGVg78ZVJqLYm!0vS3Hb~D+&BIIA(GOiOwtdMq*tWI'
        b'm+ivRt}HiWirpTfcuNI;_6v#)DsIRo_sf&Eg^+oL-f6z<l*dWa>vr4g_R2Tx);PQRXNi5iqH>P?EfYN#cq5J2jdNS?m%M(5t8p%^'
        b'>NnlW!s+X+^*dxG8m1(LDf9d##(ra>{a?!bZNfP9+3=@>eQ48{dF}BFEqUB?kB_XY+%R`K<@Kt?bgatrtnfI(sGnr287K#%AX_<K'
        b'k5#I=TlLL+nP=H>8ojj4SBSlO;%6W2f(JL@tSo1xPZ3&T62}TGzs}tMo^FcWHpN~!)ovYPPwkY%_}b|!!_tY&BO%e&Ucm}tqS~$M'
        b'8-GV2BTDHSi6fVuhcHvzi#^NTF6xnvrx+S<sNEKBuN-H$@>d+Kl1H(fd=y*uZNyjV&*;Lp^ha6x4qqX2OkqUbH0JIV=lkO@@!DeI'
        b'^BSiKj|gu(+cd&%8)2_}%x=AY#c@HBaNNH_mO6qd3G_6Uwgo)6vVJ&QKg#(UNYEtmg|o0#$lHL8FJO2X&IJ5)rR=!iwx^o*r;-$6'
        b'AFU`?Svx3y*2v0B9G)~nu>!ea7F8`LQ_jzgS7tUA7*Ai>u)#1Y*XOqE(Ft7z?TN=Xh>}cG7cyb8vs(lz!oIsQdK~8|bT|m*2*!n_'
        b'Gn~{2MtsFa_ri+drd;G{CQ8tuYh(d+SD;UcUne+r-tgnq$JKA}qHb^e_KF})@>pY))8yGNtN%(RZ}Syf^OefxE7p&%I8I0!cQ#$T'
        b'Vmo)G^1_w+-}so1ofWJ0X95JdSE6zb3jxXPl#z3UD1|#1<`!4~q3erBGfGrvm~j1E&U4Bj=yhY=f(L{f|9Pc)h;RtCNmgsB<@^m}'
        b'w)iBF+A+${J|A*mbnW&kA4^f~fg(e}B7!!i+mFFLbSFRE`@HU!Qzv}HDMeRyn7CmNb?yHgyR_{B8>uwJ_`;Px+>@DpMVtwz4q_U^'
        b'OX;a0!eugCY5>!JMxy^3?V&+U?_aUKf5kfQO4aV4N~<KZ7SM1|Sv(L-eGkF(D(|UV*mYrKvwypGJnItX{LE;NRZO2IDrwRXpQ$A('
        b'Pp1f(afR~(Q_RTK=`tG^TheNiX5<zxeiVp~v2g>S^jMfB2M3FRIO&q%l<yPy^tv3C_mV;;vd*+JJjHukI`J<Iji`-WX@5$wY+Q2G'
        b'6;!_|W!X4w;pmOwm}37#jL%-t)Ct3P$PuZa2iZ#$%5npE2P%MNx54op$<K67uf3pCr7BR{|63uvL$<N?SNQ)@IM`p}|M&cJ-b==@'
        b'Q_k`zdHpF~+;^|~I;nADfJ?ikf3L-NUaDl-74Zyp$6eAG?zoCN6<A20;**dvw8ACT&DqZ@SdRV9YjDU8wzPu}KkiL^P1FQB_e3=6'
        b'>Acm>t44c1;)8(u?c%Yap2ZE1Iv}~ijdFG*dZvePcBrwjy<exXcC;fyj$0(-2T2B0t=(;Qt#dR_l+4u=$0geAb#7GRG?R!bdfrN%'
        b'zvCh?UTu$X^BWiG#(8mW8M(P{yV=tf^E|zc+uD)}Y4CzkBxIPZK;^lrD8<^)UL#e1OE#aRS&SGUYA^%BHnuIBB<L=jBxEa8P&LC?'
        b'YueSlB+ZMyZdLo!LqSs?<HPFPMfG7`f!1e|#L>myTF~@EyX{uHbzgf`=?=$w$%;eNi#~+tPf-0+zl5X?p*Ng4_2+Kq_ctF_qW+Pm'
        b'hr6`4+uGW##qCwQM>ujNVIQ}PCziK5C8V-SsSbgK`e&y_YFA(X*`(j|X`=@<{kz@vZF}Xn?beO$j@6Q|_u8GWo0^^DON_N$IN?E9'
        b'N#h}Wwfn<(8!M<=`6Vg~U4G!WK_|g6x$UARx8^~NseOvt`4!f#RxD5nQE9?8;k5d{ARALETuQ$nvvS(YD8HLzd#WkF@0HmXD9Yzp'
        b'UvIb1QPj9BD0h5D&;+80;D(qXgj@`%xk-l1MpN?Q_GLxpwYmG6oynvsW(Bt`qZv(<rPn2XIqxa&M=o!*FPp>B`x%zXoR(`93xoll'
        b'&NmX><_@`=@2P(9VAiYcg3g%y_x4+!k2=Z}p}0P`yTr<bl9<}kS6|DMfQWYE)OKN-D=ZV6dSqbJKiX|s?Uiq}uPYN5wFnBX#!VSi'
        b'OCMw*hlEcEYAD(fLKu%&p*p9zrOx30oMgJxBCe5<3L(W9M#<J)po-s}{<V9`cHyNfCrdpB4x{HKl+}qUV_0V^)f$ESLkFbSFPX@?'
        b's7d0=ZEG24CCpJQctNbNFa6(7no~P}rJdeLV3;+8ju|N`mw1z5{kCaBbM5LE)u^;_g1Q`WJhCo8A$D7>(14MweWxN+5Liivm6lRN'
        b'=?8=xf&sFg2%p5rqjVodL6w?6M{Sa%sJt}|oL9(G%rmmTO6q^=FRP=?sXtVZxm5(*M_=F8Qtoq(Xt|28(pDi7^tTYNK~2NjZNu9u'
        b'hqqgs+EQmpasr1mRyPf8w+(5p9NJD_@#Hk{1%aF@&^u?*kdR^f<`({@I!@0NexH;CdixhzOtpEh?L8jW+$QA9$)^(gL<PE-Wv3zF'
        b'>oz;RY0aSCL^#iNE#f<)n4`{os&^8f+inS}A&uvoervP+-d6d0n{|JiBTj;`p|H*{?zOZb8QNj5ILlwAFuvYeZW35B<b98(U)pRx'
        b'wN?JoHsv;-xH7VCTk69hBu}x!6!y<H)L3H5MAQ2BAK#dO;a~$XR<u1FLIgfbClAMv_)lq$OLGV$O2xx{J7MNF=lEJkoR>h%7TBgx'
        b'SUy&q@@V=|C`>;JMi22TDp)q;k-bS+oS<<_EpvX;_JO{5qRn=qt@6t@>uYU}NJ;V=ZS)PQy1?1gvz~6Ht-V$VCn$2W``AZZAlh@j'
        b'&`N|Cl(UP+i(OB5NSS)+f%E<J&OXFwCBo;seDa^6#aN3Ae2z>0>=fbVym4&yBQ;345JtvH!_U$L^^<1P*R>xAmGqy1J@oZIJNc37'
        b'#hcn}o7yVhZL>zUr9LjnKiHJtX3J}<+}K9HL5D>;D;Kq%aE2+c2q*c-X44U7vhb^#Z7^gCv-N_M*}=YSJ$h(WerZ#7n=PxYGP`Zc'
        b'_xvLjDXMLU$Q*Omx(W^cGBJj=m5B|$N6;Dex`|!b8bp}`O>QVRq%MLw=;>@+pEj!0a5BS-x$%a~xh4W7&b%?#=f)p&`g1Lbbr0W?'
        b'&8rT|58^yW(G@2fP$OdHBb9P0K&$Hfty~*Dv&{L@XZXeHI!D8Uhw@2p@zow0*fh4yHoeU{y=~!9hp%MTomO#fp<Y2sU*ZeD&Kd1p'
        b'#O8TE=dP`u6~4?{dt`>@t;nypr8xQhEs@`UraYrr41O<od}9!%O)nDTFRgJWgyK&X_+1Zv-=)wA{4Vy;(ifnemcH|l-($|T3Nxam'
        b'#4(RwIodnX^BMP5L(<Z}PFUu>Wc%M%jvnGO6hofowfV=ltt9>h@v2(YB3Ju5#WGXCw=@G;i$<H)Zy&YswF=kN7l^T`HR8CC0j*H~'
        b'k!}!y6U&|R_Yy<t46@`?Hz&hp_2K6YBJ6eJ*qFxFXV^NMyvpWXV)Knm4o{Xj%*2$;4eFiM5K~FotfXy}B9F1RD;?iH*ejh8o8~!c'
        b'-*ojrk~Tb8w}`|PwhHSh@}x1Jw2C_=cC`vpxO67c;5=P!@M-RMo4Q(UU9FW}tyXiZnvn>54t{DC4q=;5!fv(d1Ievj$v?D$<4d0<'
        b'vu?IRXMUC#zi(~2*}BxtcC$74dh3r;e-EyFzDw$j`+MmfFiS=K3pE^`!l+)BYRCIVq{PS8a-P~l9sw<_Gmg?VL5K#mKJSo}^PG3E'
        b'd&bd#bFEW^J-|&DT5T6vtruFWtSi*LtnjX^w1*Ek*{WfWA>hMG8I=sB(~*lx5vt^yR_iydqZDmy9@A-IO8@l$A@;J3mzx?|Z4Ir~'
        b'I>a|peaHF93F(a4;9w+gv-HME&MjwpP@|W+mv{Wkm()pDrjW>#`74*^I6_JOt{gTf+#(G%DRcBe{pYphC~5aT*lIh}YTbvJx2FEc'
        b'uCTUpY?*7w@PJ5Wnj$aYyG6s*v-vhQsa_d8nmNUmgwSL4)Hm-7JAm8RQ!+d{JRZ;u+*H<XZPkc7zZ$p36tpHvM@i>PMs%rE61|FO'
        b'!e^jMtDhjIoC=nH++c%3(!VvOY*@4Y(7-ZDp64iijm)7T>we-pEd)$)N?J3B>X~=>xo`c}w6WE;vDKQ>TD9|(qmvciO~+)lYNVX2'
        b'pu?>iBGH6ru>r3NO<x*GP<>&B)>qtf0?GP`^hkEcU8=CAEFz8>gmVc<Ydz&s#?~;Yeh+-!`d!161#G*m&;(>9%w6T_`22xM^0xc>'
        b'&)L%3yoq^Jl9tH2yhwJZv+H6>S_C`gd9pi>t)EP`rT>m{6j&IuP`6bo7n9<YYn$8W)!?EQ-si1*Svg45?n+joxYyZr9eh?w1AX!7'
        b'@>XMw3wZQ8KX>%6O|x5V^H8(}>%1}ga_*e}CinRKEvpVQr`&5B<UR{!@Tr52Ms>^?C5~ZY?Tx8UX>&d0^7&^Ktol5^Z#p-qZO|##'
        b'nn6grgKu5X^lYn5*IHE)Y#rZP`YoINU6M(TOs3QNccE9+lg9H#O{>XyDTuGRA$OLtHR-e35;aMk_JG!XWWRnru}|1dp;1(a*;%4t'
        b'ww?LG<q$ukM6Dq82l-&r*zZj2x??<7wB47TQpO{D+^}keSSv?TT7PI#w%Q&;314$*rGgW+k$uCkO1@GbR9`H7g}kWD_)3{^)PRCE'
        b'@b%ky>SgHlOK8gTtjpF%->O_&ZG&2^q_t|-6RCA<*qs*V05qIbNHi<KUe3O;F(=P6`(9pno}P0nQaSfY)9+AjdHRQYdOZs@d0s_<'
        b'g__7=k(yDH{`dm7-%p`rV@}$D5hi`1Z;@BzsJy^P-~aTu$-T_C+WoU5JyV=#y_b0ws!aN#(R+uL`G)LZihQ{NMS5Y-_E0_A7bxly'
        b'%0(nK`F`oL`;UgFpcZK0!uT}GZL<Ep=x@c@7F$zG%Kom5#@f2Z!AXts+LGFYPo(h+3`uk3ugEyJB~?k0L&7b!6DLGY4jXoP+WV2R'
        b'u&-M5pPZOp9;wcjgl>>?E;X(dZc8T^hg=d)g4kT!Vy$hNuF5E{{l}YTbCP+x++1F}p*(JKNveOSN<Ov9r|C$G?MRFD^Oh>hPpSW8'
        b'bEXi#wEAnjzRoXnynHFU)H6~gs=m&7?xVSF&!s;d|8DeYajpq8k`E<Gi%4T#Q)!E>w8gr+W#-Y+QZ{}O36`*@Z%Q!PjVWpAC~5iS'
        b'WOG>0W!==!o1NFc2ud3u-{cy~dF6DHJZ8Q3?J2_v`J+X&iw_}b1BRSp=wgXC8DkMm&;*xT>jo3iwkY{h%=feIt$^!h(X}wSIp)T!'
        b'-WBV&`WbFYPMd1iA1R0zmi1P+7{9+PY&WeBAYrRpxM33`^q3D$+oB82Tt8Gn4~qCli|zFm>+7hTw@Qmxy^6`PFe{<8XXR?Q4{FM6'
        b'vHiWp`ggegqjWnPZh0{E;Gm|A7F&9Ybtx>fQ@62xvC}-o<eYbfEN!8)qjCMq$hokzmg$q0N`(`R$yg`P(0(wt#g^P+oridKI5xAW'
        b'dFVeTcKt9#(_dR`FSc0Y;qnoE5n*Oco*t$=&&ERI&dYghy>NV)%EGU&8r1Yci!HvzIvHMfm2P4!LPkVADqw00R9~~okfS2IeZ4S^'
        b'$YUF;117cXC@33%h#s!*L<j8^&Z~NgVFGk5Gmoi~y#k_J#QPh<lf6~RLyStwZYtZ%a9d&pQ>7xRI;l}h>t9>YMGp>jyD#!j8LJMz'
        b'@9e)Ga~90bKB1c<rwlwN+s!aXKL6nv8lzf-7i|S`#5oow6XR$aAzU8*p0N;HZgb_x7VF5CGs)!sK<=^9*$;w;4{Y*pvH7=HN3<;T'
        b'Q@_(6=jQNB)`gdBVV8Ckl$W3xw;!XgWGXF}4Cc(wt2p1!jxn5@t@u)vh1qkA?vglQQVLgA5})~O<?2h~(Sr1Tl04<+JD08A%{x>W'
        b'7eYQ~3oOJe_!Vy=5%1UQ?LYrDIqy=*Zi4BgBk8xly4SdrSQAr|e#4l5@3QUQ<tj^^_0DC-Yiwg_)329pcVTfHiuYc2z9eBcneU8m'
        b'Mb@QRp3P9m=sJgmzrEsK<BDh;FVbkPU$%XZP&cg|ms4M58xJ=*F54Wi_<`#0d)cLu`Qo{h#R;KCuh1k3=Sw_w#AJoCU`V11$U_ZY'
        b'56@+}?j`sw^Tb4Sq6xFa@^OVMbjAaiVwg7M(Q(8#;M>bO-8p5ETqo`w_7(H^e+m;3@O-mQCsoEWkAg)w+vWcp?o*_-wf6r%Tp10Q'
        b'6s!2Zg+m|&b%u*@^JkUL{c-=-dWcZ%BS_=V2|)H4H(ajVcsVcGn0J{Qkhj9WEHB1CE^ijskQcy3<b`n>;;SPn>*xUbA-pVwzM%HV'
        b'zGvARS}ShP^=Q@$c4LN<5js+CbzU{<VfAQkpo2@bdu>tZ0dYgPyRhM=&|Pd%vvcE|^X`%K%XSr1JmZqf)+Lvba6=w5nr1;!C`Oar'
        b'Yc6~k(dIiBHR8eyr785$!F;se%)iX-`15xAIhP;Z7AN+t_{-Th|I3+v#+jFO@5hK=a;IOmPQNS+c}nH%@)Ej6$N2I^y2o<LWzP4}'
        b'_-&kYSx{GkhyA)a=CZJEVXv@=z%4EE*M9jBb@|bYczSM&s+05OB+7_faaj^=2i*(G_;~NeyH%FLQ_|0?DkR4Ei-J&ldT~-p3@78J'
        b'&GY#s=gT1B<AOPJ5zW4)f?mnV6vgB*##rk6t#KK#wSIF7V_by0=S`l%H@UrW{g=d6X(n>R%tvXxRHaXJT8ydv4~v<9wAkA~YrnyE'
        b'uDR*^X3^n@X!WD}=|4U;g<s76`SekFzfH5LTGiDiKk)q)ySU%cBv^VJea8Jj<d*DqdY|e+s~tXSgjj@cTKZpZU!o5YRqP<@J<;O_'
        b'yFJ$O6N8wX(a@Cy&2d5`o%_E)c*{YBGm5w>cA(&TU`MWM|7vBM+>9~fLxJ6C9TX-8v|REydf-4Tx<S`b=D-ml7>!Y*sjU;PtJOHq'
        b'MlpG2ze#hXNwRb&y(%*wm7h*iB)u%WAEZ^8uG!pu!4`Yboc2d6Yjgi|iiO`Cc~ScmJLPY}PQSR&&`hUW97jK7FQtrD7?W&ht}T*>'
        b'Mhe|n*en?1Jm^AvczCyL;^vA=9*g7C81pzed~o#E)5yeEJUB1iqAi<M7oT$xl7Y}Nr^$6wgw39D1uPdc@**u?+=BV>Pv`1X^3ZXN'
        b'b0agY5=~<Gewx2g^gWD*@t6ZOD?UCmK0(-xC|ZV{y+C~k)f5*hZjBVe#)S>I_{V2W*gD#JqlDe1)JD9cIKb&guvUb<bIJLvNE^+r'
        b'dx{($txKEEP6;MG)7knE61;#Ov?hcL8;$6d4}%8Gl>G5g5mt4<`79<wO~Uoa3L!_Fc!&Y5`R+g0d>FM3t4))KJ|$EHeU1oA{`ZBX'
        b'adP4J54J8JJNLo{gt=U#_e6>2k_&&z*_i*xS>A<p%@4zEzd#S`Ed7<C{XB6}oM)#>R^{cMBJmlT%6102B(il9N#fl$7vU=Nl@dup'
        b'AjbCKuiSF>^TbtWFl^4qNFqaZWRBG!?h^G*kg#*#mkM$yD>i9u?&i`927}bRN*-!r4C@8CC)~3++aryBL8ldxrO4S&l9Dnp%Sl=y'
        b')CRRpr$0+)r$`vi_4GOgH_Wg-*Sh6`5N~`DV_79Pi-%jp78h=oUlLYZW@Va9^38)TAvtGSnNP3dTyF##a$?$C*Y9E1jTBfu_VgSD'
        b'=er{ILj0y&or%dv>)(tUTm1ft`^~~vj`YloIr0_1H^VW0u28m2;gpKxUz?pfVx_|Ks=L2B?ax=R{VoYAlAxBO&gvv={=({Um>2$2'
        b'JgtnIX5O}_X3(ht70e|jFQ#Y~J@L`_`+2%v@T;K0S@v>8HFG1md>8Hiqs?ixJAU$8)x5$Kv+i5xd$e><VXbN56sS<w-=v)_Cs=0K'
        b'I60?*$<9OhxdFiquG#m9o6c<BY%nCzVRB9XnC8O`IK5WE`5BJn#z-#+(ddpcx+3`jaqOK^Tpd%>EL3Jeuq)k6|9P|S;Z^r(^bJCs'
        b'i}7%?bI&$qT758C)!ic+jEB#QF8VYQ=dKTu+odG`b#XC&>IaX`Yb*2=2D$aUzdFyb^87Q^csjoU8cZ_brepBu)0vzsV`a>TvQ=vO'
        b'X?aT0;zc!*Q!W)uK{6>wmKw`x9p-%Ljd7@q5k7P8)g;B%E*mEdJM>=Phhy3KQ_`xsM2ut~p8qc+nfL!Rk`<i)kC9B!ry-BC>42|E'
        b'GE;dBVGIQ%NmMpO;cGRYue0!$Kgwh4GZ!mc&i7k|TDp_Zo!3UOQ|61ecRM?Jy0BO<l6KwnfCFiAr+@k!5s>VA(dkWm7Uiyq^Qk*w'
        b'e}<aNdTXD`B|bWG+?sth6iShpr(WUmbX(1NkMT+4800myTq*e9o27edi*V<<auO4E=sbexri*u$m#|#e!Slie?+X^hAKn5v8H!P='
        b'>fvqdnym2swN4p5+bN^71pi^n&g=IPr(hMvi?RUgdFRnw!iDGQ%10NKYYM}Z&CXj+3&qjz;Sk`AL%5ez6OnyYd{(7Lh-1N=^G->}'
        b'q(!nWqe#!Rzb+}FN8}zJ#ZJ)>(UW^KLe&rZZ?!B6ov_!=KdNZaDl|<V_Uif2M^+IEmtAQ4;Q2!i&kvg^2|n_?zh?-N3ZQ$99VO1O'
        b'>CU<S{0Ps&7$9^2(Rud;dYOl4?z~7hkBH{*^HYA|o#p*Q@bD7yr{{-qU3@eb2;G;Na?Kgf|4(55KR%*rlTzqYN_s^7X{XFFVQjdO'
        b'fT1A)Lqj@qW08rD45r>Tnec|vL|1|3c^637zG<9qd|s|qLz$&;F+{(mND%#k0LfcSyHuvfoPzze;1dX|_(V~()<Mh*S12q#U98}S'
        b'R}MRGF3pWEXAYR;PHlPdCfU4UQjhuZhONTZ%YuExJV)*vcD7ar(vN{Pe2zre39|UKNx=<3Jl~u%?9J67o;h-h=ymaSUl~1n+`Lsd'
        b'N64KXGBQVQUMmQ=#qQ$aLdIR^Dp+US(nR(@W%*Iwd3K~z7Ms$pXUPOXOa<gLA7M3pVcO~QkhHe)bEm6wA!KVG3fZ&|-PVtg<(zV6'
        b'A}83rY9D6Fa#2R-q`3>0WOMF0r_^?#=XT5Kp5cC3dhn03v~tcxL7Y~w2b?ntQ;O>iR}(7+a{7auYN6Tcg*S1sLM1_AR^`!i^klEe'
        b'7oEAI-L^2ja_u?ibNc4+bI#+8e8rxk5oQr#PoL{QW-%hg^{QLAii8Ks?UMg%dLIkvjrx!DmOe_)=V5wcLVg$jn2>7(`=@l$J+rB9'
        b'XX>eNF^iKXIvAPW*u3`KDH+uV24Ad^I4klEp|LjqrN3g+jK7~X#L5k88RvjTmj=Y88MDqA#GTh^sfE0eToi^qaD;Qzi(|#1P2d5O'
        b'ClqM$V6zfs<+tY>y(*vTFN>SWoqN~{bbQOF8!G&b{8@UFdJ-edFK3@C*+=WOKocxn8CE22H$}(s@4tRpv=LTn)19&<n&1P1FfS1v'
        b'3p5%ry@GU&bIuz5D9-F3{@>%2|2a<iqc~$oxQZzewvLo6qQm}PVX5WWLKWwG%02r>bHf%o#S-UTX9XvZqUYSraa*!msRpvuT6<J('
        b'{y<2XIv48C>>EiRUMLVIRMnF_PS)1O9%xiNiiW;Du3jWWQn&vLgtu%}IHOopzz(e1zuLSZmkwBq%q9ggZ`dF-sxWR(TJG*qgh{m7'
        b'9BVEVf=n`{RIsk;p^h88DJ9_7vqRILpdQa`e)p`C8_rPi7dU!(gm}t|YSCz+lR0kk^}<2_qW7ie!BkW3@PE)_=4LtX-od<fxFAD^'
        b'2zRxOQYwQW0=WUo9l2yUeYId1rF{6lT=bhWDy081(hz}1U_bi5*;|t?82=`yZ0?m4&gZdC7IU|TovUmVs?@#zC4_iDUF})4G$Hyv'
        b'Unx;CvZy;h@q8ChJCcyMN6Mn2)I{H{AiAv$S{>1mq{h6H(OGj(MkfK%D_UKAt5(+<d@}kR5EpVXdh3Rh(GiJS-64R!8XW^#3`B4d'
        b'x~=My(S*oJ!&suXtUVdc^H+HM-H$-JZitWnndg&&PDbl;w7Nu4u2ZXPv?HD_Ch6>RDRQ3hd=&gG20~A2b=S^lb+HI*dO@qBZ*+M+'
        b'nl=F6JX@<<h`eM{ziUoL-$4Ek1t9lwLhSR9XXNMfOIn>dL8}}80?nsEM+`J8#6bV?tErh^osRGZ#6yBIr_oJm8F=0oOv}*4?}Pmq'
        b'#FeQcy1yU~^MJnrtAS!5>v7cSP^o@A^3pqr=*Pzr{V^bZGR&bwA2gcicg@%8l&FhL<YNuYWw0|pN%Z+8T3sA3(dTDrbyC=Q19HS;'
        b'M_!Ks-J^*9mWJr7Lx{c??Ss5AaY*j~>^M+T$B^Yn(+vDFKo+$N`AJ0HU9$=4MLFYPCT@hpfv!P0bo3duph23k!N?END};UMKeal|'
        b'C&-H@(Y4P*eM)3eAA+ud|I7tiT^HiL4~)^AjGhJiZrBfCWl;$*OM!*J2t3aQB|snCy}!`v^1aX=-=ba?X?5AOj)5@vi$eUXqq+u1'
        b'_jO4o;5i;)W&&=&G~gN7>3}5Q1t1-`?<b4;7&HUO0yYCXfpQ=bVGe@U0$&4X0Xy&$(2F#ugLV%`x+q^P$`cBzS*q3ff}Tcuj7Pal'
        b'G=Fewj0Dd<P4p&U>*wH^MDRM=X)W@c34gimev{A+hF#!S^Qe>2*?=4TcrT><LXyx#NyN@3^_#(KL<)DZAcZA|PDshvFa~Uezrpz5'
        b'#pfelrBoKh^AC7`#BpGuR>$*9FCmL*GQ<sTUGS5Ebb{dSJ%i{MgC+s|7d&4)o#-=W68%Cvr#}bYn@Rb^@I^ermBDTwunWil;{Sp+'
        b'2Mz(<FP)68U4JsV81bgV@9-Lw5AC%U=40?%4SWhnO(&y|%>s`D3zJYE@!(U?Ui7P0@KN&v@DS?q1kC3E|4$fwYYn5n1}IY)eLDQ_'
        b'd!Fds7^%Jy?inds-I!OjI>R!pjw@jFg>Xwp8p}bC0kQBe?I!w}kUx!(F^7^NSJKgERE$0-f#|!0v}s+x6?^X`DqD!qp%av{sB@mO'
        b's7B;pDw9Q#2trz6W-L5!q3wh;q)BKiz}rg}<@+MhYXCct4(xhW7S)RI1nzyHiI8K7s2?Jg>+H$s3kcr|nu)N9z)QeZJoCTuPVx3L'
        b'&w-!DBm7LDIhp3s5N-B=oPfFeSy|K##Bm5Xhv((#L|;swQBE^xT3TB4tBCU)+8`~haMHMO-^36I>?Fj+bWtv<T}?=X9xOo^<mpsn'
        b'W8*IP#}oJjot)4eg9t$ASAIbxQ-jn({qU=&@;^V|3DTAP!t;i0g``*rOP+^VM&5tti5%V;hVVc2@q}Rs|3KKT6rF|iiJT!BNaq;B'
        b'?*iWYt{26nCq^2cor&k6pEXsxU)=fhtDd<N3u(Oo-|~GtUvr%|!z@J^TLz!hnQ2_)5c<#f<G`dtLuFBNp`LU)fA~3sIxmBNH_CJ1'
        b'lWT&TYb?tC#lCgatc(dVQ7R+VUxJTqkb`xQk<@&W=$nV2pVKfYXlKN&qZHVO_AdjZF!%b%qH44*6M#>B$Hvb7Jz#+DpXH;U-39r+'
        b'24hEG5YhPpW7LG!@iVV_N}itZ+q<YMi!KFeuiQw}myl-2gf|f1>p(hi0_hbM6%BL07)brb#KLYNFyyi<$_%$Mn9V>I&;T4jeojz7'
        b'w~4+M)cY5V8C~cnKSTBa5kM<|VU90)W7|7!i%v#&A)Z3?10~E-V52_ZnV<R9(ZClI>Q+AA*hloU(@sXe2+V@J!dDjM1N^j}hn$h>'
        b'V`*PP90eHfePKTd_+~Hi2f6`#s`ZyeExap>TENSq=065AVB%y^6JbB@Fl5BClhMO~0{Ab2Jobfo_i#}z7sIX)W+nQ$1!meG`}WDA'
        b'a-6bd5A50iIovZJWAr+}<V|$yVX~;lkWLW#&RCcwkaaE+u@8^Kvkd7xgY+lCOz-u60W<~ZMw%SbOM`hY=qsSdP_8#Y*8&@W&A@JI'
        b'4^#v0@Rth=0{nmwV8U>5Y)J=Q1!M#3fOi4UNwTPIpdSD)|4SBC3R(vE03(5NpbDr4{sq(kUjgTUwQtCxE`ct49^)d))(P`3KrbDK'
        b'd>Q?HP*<eu4)_C7TA#p+50EC>q7iK{2G7}YMxO)}4rcVBK<q$9KOT^y?!5sHcpCm<fH)ulSOCa}qJB{yS5UWIkYg#djDR<I_*Kx?'
        b'fwzGizy$P7M|n}t8)1GA*aCb2Sb;KNA8-Kp6!;wY0yqJj1pZCOX6Oe^pcg2>GyewaffhVd8A#<H4}P%I`0?xjy$SpbbOZMQp4J2M'
        b';0ADj92f$$BcAVo;V?f2sDKb)3=jr91w;Z-fDF774XOuPfXTp2;00hl@HZe8*shttWPrW_WCNRkEkH4_3n&Bj0SACXKs8VUoB&P&'
        b'O~85JGH?aB2HXQABhbdEcgydxC<V;lgHK0-YJkze6F@W&4<rKVz^gzOupStL{_$^69q4Qz-;>dMp$%2Q6F@l1=L<}PSx@^7+W&b_'
        b'C1@h(i@@K2k$6r6U5q$xfqybU8@w5PHs~(E49G_^`U6Ug*RYTGf!h#9zY1aU!C!BKZU=S)yGBy|WTfFB%%21Ph}#da!CVh~4Kx97'
        b'qmML$wgH{MHQ;-|4Ss*5d<gUazX3epf_OQ=lgcCDF(I8_`9M$&FcugGL;z+wM*$#uEjktg7UrqIb3g(x7htHuL{#KOm|voPi8omU'
        b'x&(LySV`pruojRaPXy>&iZKDW3v>eufsH~wgvr4JVQ_?^bpn28(=a4MzZ<&3!k00|qYeojETMuNfSU>WN)l}cxV3`v$9eu=h^rnr'
        b'1^ftH0PMgG;JA>-<jKE)9>RD~4g3c4F38Sc4?>26MtMZ&@<7MoSq=Is5CijE&{?4NSHMp&*CM@RKrF`4W6&W2I3nmovj8dNEP)K-'
        b'643@uncey#qxYY|=%uVwzkEKU=Rjv8-!Y?6#_hjLdQMA7$nO%ed;z0h414<)DY^D4WD(3JAa(_#AG!92S?Mt617;w7Ip$!XzMv=I'
        b'{{9~HA=FhFkaQDT3g%^}8fQK$hg%oYgTC-|(i@C^EBr498fiG-+!*Lv?=kuYm@Sw)^uq5o=$Pg__|0YXWg8j&X}Dzr5wJ6P5fYlu'
        b'=x@LtI*Yymez>)a-VD3Nubhm&1%FXv(KZ?2MT~=TK!@inxQ$1=1kY<=UXOTAz)zo<(KjOxv!Qd`K-ga7e<18tz(l~bozYw1Cn1CO'
        b'Md-C}U=FnsV|pgy1XTh-fC1RL0%Zf$0Aqk_D<}_HqMtqfL?ra4h%Ur2a0U7?FbP1_lb2SA<Li5%6+jEn0}Ne>@d`))RskOXwZL_N'
        b'dkx`%mx0A78y%0Az&sn~cz~nhDwx2IypCA~{savN^#-~QGx~FQz6LY{a@gGf?E^TNZ_)CBh5@Hx9tXPoGe*DgRjuw6o@)<cd;)3_'
        b'PZnr8(#r&*wj;mrTl@phA4lEVVNL?pY(sx&%tt*mOsaLf6K5DJ=*kn#ThOoIo=D-;u?ca3ChJDzrx^Wg*h@E~tUxQwi-GY##7Rcq'
        b'3tEkMZh#t|M4702DB2Efm~k3mn;`3esI!dz5a53f@(#EKf89V-A@m|(D)Kx9upnF?+^^C6USjlX5O+D;XNF-OorU@U;$W_ZT`bJ|'
        b'D8(4)dlTa`p8F7v16>0@{zV8!{R5}*9E9gdz<6LxjaIj?7IV_0;KM$CHR&6i0f3FWo}UZ%UrR8q<MADs*8tOC{t$FJ=x3mR0lg0T'
        b'Jm}CJ7*{~!Kxcz)1ziYw0Q4=;Q=r+P0Uv;eL7xVF7jz-$R?t<TJ3yBeLuMh}-FV(l?O^_kf{<qD#XpqLHj(R^p(}Hw3v-gL)wEua'
        b'=Pb-Zl-|XnK9+$zbs#J+=~~@)2mP||N#b8D%sH~g5LWLGnN$clMf&KKHge^fABDcFL_A3&;V%Q}1cO$9&IJ7&)CBrZV6l(~WC;BH'
        b'Z#<uqO7)(Qcik|zyF;SF?DHY?3acz?-aym?%Od^3IyclShdQ1Fx7mneDJUnC>OTTC;<*BJA_{Q>d8vZA9T@l#>H>BVpm#tsKB8qJ'
        b'hDy-02;)6~kPu)OvU34;--0q9L-zxX0Y#cgFT=d<W145B+>LY%o=o`!Wqu0s@Ke}FgSLZC2OVgUMa=<?0(}YeWzaOx9iZ=kHduuE'
        b'm-m5ALi%qHA>=;H<6+K+IT-X4&~YgH5SVYFE?husVfP*E&VZf+y$bpTXdUXO67&w9cY?}&Fy{o_20RHf)!WEU^tUjP|1;i1zXE7m'
        b'Qn!WR>BYcu*fqlsE!#EFM1+Zdg4OFlZ^11zl+_=DdFU=#)B{is^niPWZeNC0*M+&%x%VOG;m^KRtBZqqd<IFfY}4v)eWcZSC$UMH'
        b'29o4UIQm{iPAA(LM4H6&bk&12X|;jprSy3);YpH|M41TO*7F*{&wfmQdwE}&<**+QM8F&+xVa*HI^m;xd7{Huw~D@d;XhU)9abqE'
        b'iTE!((+T#82IO}_sVs^Gya0b7tBL9f(S6iQ;Wx6V(}9>fhM$a{qaeQipqAlyHb{`?S_vT!_?ZZk3uFWFX5{fbo==PbZ@vYYq9089'
        b'Q2y$2tu6v#m2c5^8xk@Y6F@>8>3h!y67n9x)&l#0LqII%shO{7byDzV??&VwlGKFfg^d_LT(gMVv-Ir%m*fv{KoH=I`fNei$-BYd'
        b'fDY*eA-yMI_5)_)ISxo_q~+uL2GjRdgHcRg!fzc;-wrdh9V9b_Ja*C7Ra95%;)#JDX&2t9Uh&V=>M{^V8R8(Q^96{v0{90Ik8oLV'
        b'i#h{dKnw6A2@Umy33iL&mIRFd1Uylx)t#==>Y5Q|FmwqCP=<I7a32YC4Pe|u^JwF{^Rzm7P=rnc5OVShp2xVM?D`mS6Eos{7yg=n'
        b'u1wm-(Y0BKW40gB#lE4{T?36vX7xMZz8_cvw*v?>+d$vpk$6;Xd>Qgl3;Sxo0u%yf>JKObn!nZR`ha)Jpx=Ry)_{HhWCF*Uw7LfP'
        b'u>*~Jw7M~6S{;XZcNyH|pbP-bHR%SpL=#AeE1t7uM0W!IiUHsIh#P4BU8_rfpw+d4N1`gUIwj`Az3=`0ZkLzC^zFyL6AjvS3}DxB'
        b'Nv*&w;0DkObOX9#$Ts9b9s-$o4}69=550}C2kAus20X_@9(Kb|7f_2jNc1D55OtPx4P`>wWGDJ5`fGd;^a`K{{*J+)4&gh1&A@5?'
        b'-_aj{o|ud=aHvbvDOx_zyYRaYb+Z-y8pFDd{Dbn3^JTsT-7FUMgt&TXUY4_Z6Y|#J(CV_Yw7LVx8-2gf`wxUI2k*b5)tvxB5swVd'
        b'j{&2B2p}Fv2VMtqfj+9hgL&UA7w7+U9(oP+VZrk)pbIF(b1|(am?!-c{R-wd;60ezfuI=l9fVVYrtA~nb<|cs4}<w_;1KWt*aYkY'
        b'jsOk7MW8GPb%rwCIDqh<Ab+p0`bf|QJQJ9A0hZN}d#I0Ql-~_BA9(DscHvEN{zbI6QLCE`)B+0;p9${um5@U#Sp7NJb%V!xDNn*a'
        b'@f}uQNaN~38>5{M^}-z}hMfiQMR*qDf-l?}UZ>wh*d$_RlK7E*{NP&pt`UL<Vq<w7+Hf`c0oq&_4Lxq-$>?2>*=|5!J;oB?1;FGM'
        b'p(}>nVwjHu84ZG5JopyOW?(<i3qP@lBl|0~EuaHG_yT?WFKGX7qy1f^dOQ5R1h<jE1i;^LGCKDp=8!-T(15&Df{r^OKU#YX{Xju<'
        b'=fG>T5pM?kk~N@4%tL@Apl}oV3}Aq{7j={cnuvb35ZDTH+}FrEX!kF&sAs;t6Ez#pg?L^A%3#bc^d~wGPzk^SazF+Q1d@H%G5PTK'
        b'9q=je;3uAsJE+wSgPVCPt1m`87N84x+XXrX<3l<S59Fh*$os553A7Au`vAII`3LC9<?)0x=2Cr_|9v6SPX{sqcks&Sv(N<~Ggkt>'
        b'Fz15)0+ba)R(`0}U50tr2U=YnwWH=Dt?qqL8T^ubLJlFFXJEd44s8V5WdmOv6UMxlg~N~*aBj0!cl$i%-WOz10l+gC==>jf0O&|Y'
        b'3L!61=kh5i8~XR50JJ?&HYh^Z2)Fp#&<Wrc0R-tpok4#QvJiM5IES(|1E+y<JRbu-0dBx=x&`^U1amWF2yg<Z2KE81fZ-GH=6;^P'
        b'6$?Ed=mNT7KOSK+fiY7tZUVz(Vf2OgabnQc@~d45hbIF@&;}o(>qWYKw0^rJNi$LZi7k*BfG@E4UFaJ?2IkPA@6vCLI%VIdte*Rd'
        b')yD!^z&>E>K~}#Qer_CQ^$h0z9Q^je?EM+5hbprA0gw&%Sm?LSh&Kp)`Q^cq&3Pu1iF6UN9CPt9njUoEEKucNkiS_B*%CCZAfgqz'
        b'JTU$S`29NS64;05MqpnX>I6u?B8yrMWB{2!7LW(Dw$Xm~Gj#G=@J}fEwLN-CT3Q;t<~0%SaaY9mxcSf-s-dg20{JSmIWQjP<<Rdf'
        b'pqX&be-C{g<!T0YAe<6q=tg~i2(uJsFTe`(A>abwhUczdc)kwi^FTMsc7xj6(VhV5_@DFb3%9ME7<W6x{OtnW2UGwDoOZNcDq$WR'
        b'Lf^IwCgTrNJ-Ca0XMTWDFgkhCtBdxmKNEehA!(y#Lw)q`Z+;x_6?-<i`Kl~x0C3<c^&f;f@ds-A2=Ue}Mp@%gb`xkH%H}%xiMr*#'
        b'xs#WH8kd(Npa1eczgqcn<fZKT`7sw(lH@zXmW+J-tmC5L@e5JleVV7?h}Vp^rfEdJdo_ZpX>{_IC8S6H;wK@$hA8lj<r>Bez~TU3'
        b'JH)cnIyepUOtf<p5O<Q*2hEn~4baQSe=mz#-Ocm#n>zirO}|OeZ}f?<&jJ!}qAqVfipO+QOjCLb_5TCn0-w?M>hv1~eXs9*OPrh0'
        b'@1K;?4~+EtH~mia_3ddZ1S1p?(ACX@r_nk27xY`wWtep+FZ~8izmve8hT+BUC-<W1Hx!^2<}c0!j9Z<3iPZsk{vK}Me?f$KqP*61'
        b'q4&7p-PWl7?<}Stg*>2V8WKU<k!~=|@6erAMEK?<<`eca0IDb0;9d**+^=|cMZW1bsDGB1KTE$=Wt84}>gn?8XhJ~@Ggh4NCl?O>'
        b'l~}}dl=K^!{+Ab?ofE$NS=r8w&wlnw%d<O*h6&%Fo{xAV+H(BEr_AtMNd4m(VJ1bDM~uU4a#E7MWMKZkzL?;<GAx<^GmnOi8+5bn'
        b'(>Vt>L?nAWb(DTXy84Ze&M+9V4VV-=K}!I)ook;k44yV=%{^6g8I2du;bEJCkiSWqpJ=|!&!P>&{&I0@MNj77u<YAg4lx5yYm+?='
        b'e~vhxDJm*L+2W#?|3dv5o<^Q%Sz~l~K6~<sC&xc|vC8k~h^Lr=@kjDZZczw>Im_y>XzQ5h^Z?bkH7{J!zE%5v#1XAAGOqn!6Gv(l'
        b'QB4E?`piq8eDK-i?wt`0!NVu|EPeUuT_Fdf5FU9M9Lw`9(91?XTl_jPMP1Xr!}GWC?1<)9OVIXRUnnlCu1>5lNB=PJji4F-*c(0T'
        b'nbVfEftAsJSI+$M)a1{i`CL*EG_5Xr;2ipQKKjY!%f`eWD*0l^{q}^h?G@3l?8w}I`@q5I6+VFv>Q@|#KJh~#iiz<WWy%8R_c!p1'
        b'fqwI>7RpVJ)f6UVGY^0pz^jlns}1qTF;~@>Y=Zqb4df3wf9}|^^2%y*Tbx_Qf@jCTJRWXifW(^;J)PIl@3beN)5Kw(6bC=E;in2%'
        b'5A=GuMA5Y<^t~%xm+~&`8Uebdgz7ZAV0HkpKT7lsw<LOD&h;_R)Aa!U-4Z?BPD$6RNI|2J<~i7XeFyphkO24sS1IkrSPtrnMx|?3'
        b'=-iRMU&(-dzPn3QS{jDh$-<g~<MjJBLuzM^QMg16@^pz>1Nt8D1#kwq4}1^w&qZ}ew+wpE4Zw}QltCCeKO*ACVm21;-g|`SXUg%{'
        b'yHn5so>9VXCg$Do8Fc<Ep&!<x4<HZm@V~|i{S$O0;@SknQ9$2Ggxx}*e~v=uC)Ef;_4TqQajtO706i46@t#D#3*lZv9ZLZ^AEDoT'
        b'>0E@)ZRmW2&OvtdN%W)Oo&wPIBXK8@S0(0RI_RnK03Fvqex35e0Xn~<^E?y$)&g{m1zkf#<s}{aeGf>I3;+S-fH%Ma{(utD0aCz?'
        b'`hiYB?-IX2*K=A4=f{2Rcq@Q=9As@kWmS)Veu+)aNsNbkgpHZ<ztRo*HL?n6Y8HG|Nd3m8<_64Ar7gOi`k~smr-$?0uz`~p!gE9E'
        b'*+gNxdM1`za&q$<=)&M#>c;7m?oe}{++f>BJ(VBzSU>I=#c+S?x}r3G)bocs$BTP57xxHj$mAN&f&mR0m0^R_YzkFsl-b{#P4v!a'
        b';R0ytcT11SEx)YLEu_e;&{ta|nU*-B%ap#Z|1NH2iPD%)<IW#$cP9a+9&TV6%RPH)AorqiJ+<fD@>u8I&>X3McnrypFs*d$4LM^W'
        b'a+|VdAUC}9J-_0&au`xA&54zo^xvGwi#4Sn-kezP(lS4lRI1<4OjmKfoKzXNWvp|rWtD|N3^VE~JW4nE6>q3!InGh)r(&f!`<V?Y'
        b'ZkThs^N6nO-W<Ku<(_!1b!uP#e$QuEpDOp57kk2zdL+^bIe|(Ne{-Jih=fJT0?Xo@z{lntp+_7gSO(4Wb+ab+BrJNY^i}}u3oxzp'
        b')sZ}_hl#jd_L5FWkT%H4==cO__HXe!w#=H*Lr&kcJ=cR)Wb-6NXG=E^@fj^MPV1=)ROa0_#`RPMjw}frkyqjvq0$G1FTbaoCaqng'
        b'&`UJtSh*oqsh^~&@^s-Qg&qZC9GI|$ZkH~V58=G%mbtV-c1k<XmDXS8NrXOJqFl1bBcjAMzNf~$g0)LX*tnj^+hO57ktHtuXBm}P'
        b'{Ebi2b|~K9pRcS^8vTSu8Bnxrle^Wwr_jA|8r_Qcp?lfVxf}RAdU>Z1E+VDxg)mhQXR1{7R7mQq!#;F-BhPduaB5Bi|Jew3%46i~'
        b'vz-IU8CH7nqrclD6dQ6+n-qo(hMW|a999}`;kCXg+`t)iLIbbxd&b@8veY!an$6RjmVHx~qxW`f@H4Ub?s<XS_uC7#4X<?!=xI)='
        b'Vx_fT#&YhdC7jWv$6}Eln8<9F_LOLH%)(BBlJuN)ED1l}?D8F-eJ5NmMT3X$XC|t|eT7>>m6=Xn3%5|#j0}hjQ=3NZWj0n;Fp&z*'
        b'v-CN&C2&jF&v&g|cXI-Bl*-JE0>&aNj?P(>;|x3Nhr8U+lp%8Jnx<S~znd~ge#(_|;fCe7lIo#(siq~Id!E{3qhW7uQ^(z$A#z>0'
        b';<T`qJZFyFv^{0A^vHy~IcXmZ7S3})#casW(MUf_A6z4?kQFg?$qX8+K~c!~rLFu*leTUT7qW7Wobz4r?cJz8gDSMZl|vky+xBD3'
        b'OgBSbZC>j3V^ZUZyNxV*(`1utjWkbf8d@RCn_ybvmzFn2jL<(~<yZa<iuK#R2-tm>b5*Ix%2eqp&#;v$31VBB>atQr$~@mxuk>`='
        b'I|1osCCr^l9PX00-QS!;GlnQMDSl~l&-9<+X54r8Pj|{$_ue(`z59nd+)D3e|8CrUw}1U{SkYb1Llqdv{YI~5_prTtw`tSe3J-@('
        b'Wy%fv=x#vq-B42r=WbX_clYg0po?PlHSVP+Rl;_h@LeR-d9kLm9ZG^oIK7pYMQ3kwKgA%bnSS}xRSZ$ZO8*DB;FAEgn9Rz(t21O8'
        b'3Kj9f#g+y8iCMVDvO=Oi!60*Kv90~*J|^AGVU;C;fmMM)L(>&?DoN>;0GMHu`e^{>&>GJMwzf{{I2KU<d;j_4uhJriy$lW_hVt4R'
        b'%Wr$Cy^PDK<z5Ll+?d{9M`4Taf(gR|396P}h>J3X#Z$fmcW%!bMlYinG1hMf=W7P*hGqu4yVS51j9N0Pe}62)ln(K)aktL7%Xv9s'
        b'l>Ygg#|*1+0ga#Y;9_Z&Oq&(SM21DiIF74O<zaW5!cgU<<tmH;ad&G5ckXg)8(c9s^(b6nZ&z_rdSEK5!J$#5#onG34puQn-`yN|'
        b'_c_@suG~RxM8<XHZEH|T(3C36Nsn=#4S%jAXexK?tKpNYzP@*A(1BCAb&ID5zoq?cSDiaCA5m7g<s^F*BzvDpmWy}58OPE5Wt1zE'
        b'jw){lcy<OTg!|sSa{|2Hc7Me~f8yF)$#2~F5}Wc(<I>I3tdW(Gw#X*6e*kxQ^WARSh`UWA?v_}C{D0?slipD3)l)svI!|;Teqx~h'
        b'MAwfJ-HlwkF4Jc`W0`EwOUcy7Q!w!&aaOu?epJGj*F09u-P6Ynv<|#mGq7$KNgW#ycD>try;~nRf*Yb=6sR@_SY7Xy?hgoONsP<g'
        b'@Z;Zyrsjr8!MWjqBP-aHSlU<t-*s2WR4Nr%MMW3lBk~*bo$18NPyZy>{Y6--Kfk`Se;ib1J{)w6Uv_Uk-kqbFV!hpMFv-??3M<-2'
        b'3DNA06wlKx)1Q*WP1J6U(z`3Qi^rDK$&J^$QEhq^I9oX{WoW?X-E~2(RjQy8RbcAj0MVe%51@>ZdXAqWtfq@O&|MXTrV30w6d)SZ'
        b'8v+nTPLSKoHHKJu+L~`^%x7rK^<6aG9G3Xs3n=bhFK!;aP26-!<z}UDB!X})j7q-wShrav7aS_<d!6Uc7kIjd@3e;&$%DTSE<qf3'
        b'j2pZ61k$~tre5MsH)|H0tmTG-vFV1)iCflh8EEn>C?VT@C$5hi8QdF(K&e-iLLETu2;12mYLW{9E0HnueXXw|Y<;)3@InP^+#}@o'
        b'Hc!IVbcYA}8h6oW+K1?<7PcC8{zgl`-S_BMHWF_29@8kEc3~`_PT{j$q5{KXl$=+1%;>O}yS><H@si)dwsgzMjQGIc-XL?7iqRzO'
        b'W~lC(gpG@+RFcuNHg(4f_vI4Z%~>0}b-HULRw3F%R>qjRBW${H@<<!En3F^*a#T}-0|SD`EeZCLqsVzHxXJSaTwDm}J>>`9V5Amv'
        b'=-Cd29BEFnt3H`6Trn%F+iZ}^%M_+czj5)xc)`iI;pWmU@*RwIWw$sERWNy#r7o&6MVpKpQ)L^I`ZrbDq<2UBFS@=yu8AXke6yQ`'
        b'5LQh9BX8R5hCo1UlSSpF_6`CfD)u1Oh@S1&1VOaz)l%w9kKSdMHU^}37+M8u+awkRDivt2RjWP3Hno=CS-rd3UV8;3D#$z5S`_y8'
        b'%m&-u@B8`wGs(<6^UO2PJoC)+%*@V=*vb*kXVD#Ki&@OF`KI1g%A_kyQmpVW?y(>VR4olKx<qM4eTfS*eav^gsLXZPE+i{e9^5HX'
        b'99^ERO3iH8<P$xVt!ndNshQcKE*FUH`!A;(!N^~sNZVgtomT3MLGOp?>ueo?Se2(?-KTl3`b^)=CFk;7C)Mpo)rIZqT2*R=2W$$l'
        b'_A|A4(T_-Wj3N<wnG5rMq!x@ruy@n%zX>B$wP|KR0c}`vlZ^Bb7}lim?FjX4=IfsiWrQe}s7X42*S{KS3B1{wc(cJ?a#4iIzfN;a'
        b'ut}&R4G-Le4$2Lg0CCBUn81|rY3>Q%_LN-t1m@~D#N8CG3j2;{0v<F4EJ=^Ksb8Zf%Yzb&h;5#LR3=7627w^~l9Eo{EOGIsk8B?C'
        b'rX3M0+oB^>zlD(!R`wNh&Ij`YNs{6EPs`i&r305b&W*LFln<<Cj?GU^elKxei#}8}jxnK&+k*3vX{KqZsW~0U#5{Ip#!WzN{HSZ$'
        b'D@W#z)P@$-;oeNlExFlLaqt}XRoB6t!rc@X8kFqc#@mkG*W~bo$y=Hfo_x7uQ^MBWC-JNYv4j;zl5y{Pj62tT3;twdoCn(-F5}*W'
        b'5HI>MSwOM(!*OIu)NwH!nP3y-hzpmahw5#;AW60+vFlV#%UepQ#Q$9zw@&U6W1NfMeE|2~hZVM{FN!huN8_yx<Dbv?%FTW{jz*Ax'
        b'x?!B02gn;meN<)L3554^c~m9HBPr+3-JX=&rpj&o<&Mz4^dAj9hcV};ip%cZe^NGtpV$ks@hR)Oxa6|?9D96kV_wv4GW^SA^zud~'
        b'{$(=WeoB2}VY8_4L$&dv%icPqO%e_qIgZ=Ce8S1ysd!c#wEE(EIy|d`?>eMxeQ}%%Sd!Xwp-Bny-t-okKt|e5)o>B=C(15-plo-b'
        b'_nvd#5!>Y$f`0C2Xxsk@-6HOIi{E%J%B`2%j{q5{_|~6`v;SxDR&mzwH2h;f!*l;9e49AyieLVlMeJ$BV`}xd;l=TkU=+|OFdAMM'
        b'Pcfl@K|xQlA;k$QkbMV1r+5su@pOQ?X!zr}%aaZk{U63XRvBacjp6xm#+qvY%h#GGgeHS|+*oj5`tQe$Rx15D2x%eIr0;@ID}*uW'
        b'J0YAegsSvB2<N14AJ1dq&)oD<2<N4*f-o|@1j0WEVMzMZ5QYk&B7GZ#N+AqRe+t5~^amjPefpCS?h?Ys)1QFw2_wzrf(K*e(jSND'
        b'Bk5ZqTvND4WYUDCQ{%10<LkufMdPI0SP-Vwt2$GqXhqKV1Ex9<%(w`~`a6RK+O)&45yG9xD;VoGZ6yv&cRx06IyU0dg&O9MTaSI{'
        b'$-tP4xRH=`Zy3+bRFL1JN;70eLSae|-I%G!k#0l@3Q}xLpKVN68Pn%v=Y0`5zC3;TYDmkI8}mrxYBIflZ13`MQkqt(?lLR4zK90b'
        b'?uKkKs=Z0wnB8_x!A0VuJ!7^iHTPS*A@qj`-2NEm2=A0F5BCIOTh~NZURa~#mSb%nE4cH<icOwO(aHBaA~AO1`1-ZBD#e+^@pcfm'
        b'-(qdE<xlLi?NN|>koc{Uo5UD9HMWi=SCW$Ldr~@Np<^!ohbaAR_LDba&Seiou|JHptWmDN?U?2Hjd=M}q;G9)2+S@INYN&m$NIah'
        b'lYHbF?wmTZ$oP>i#*SzGooCy}$iI9MHQpUQ-Wm=pUL~89Z2xoNg{?~0_V%tF%I8X*bL3<~d!5?3R=zWgtlK{a&su>M&oisAig_I~'
        b'F{`U~>k~VFzeQ%1k)1nAg4CP$<K8r^cK$cZOM=MF`)74+Q64DjDpGEJydz7@6^SD|J08Y7=SAGPsMfn<?ptHpKZ@M9$6D`<8ReKM'
        b'2!l>Z13N7m)BahcJ+Q>mF=ldMpnr{0@s5{qX)@L<tq+HGSiS0^rG18hF(c?^f?W0rF3rJAgc$yKAI6%ALNV{nK`S#IUr&uS^FLH+'
        b'9dn@%=5jMoA2?7Stisl><z~y>uZ;;Fm|S`S<f`bvLdQG+oVRriz^q^ESlar<nCD|OL@Sn>X3JaFs7>o}(@ZS#MbpRYxrecJo1|}{'
        b'@2)3sX(NB8a!lwvTzZ%%!=>%~+BvxQEWdMZ=N#@yk*la3abi=6N`B_lnA6qLzC&GNmRo0Fk=qXxm8`<H$n3{?V+_9c_*hz6W=p2h'
        b'BMq(2R6AW$`wvj=KaRD$qIA{SzGxd84E$USmV89r-ul*v+Pzh&&4F4O@05n_2*;(z`PS007N7Eq#<8v&wzQAbVBe4t+G7!_tpmmo'
        b'nNuYNoW|8MZ!-_mz!$EuGp~&e5-o43eMckAsRJfL4Ln`;ir(<*7#aCR-PoB|AiFt8`&I<hL->ZK>W_oHhk?mJcich_^TO$ic^D#W'
        b'SxC40r7`I(etM1Pr7=)VLF>tVt8fxuyLf#}M1WO{Es?BM{f3l1DkI+@-y-LdGq+bRir>^B#jKqdHf}84{Og6b-*dUY<!pOA&QC5>'
        b'zWC&f9VwzGX9hVA9IPyQe#R#$qUUG66u5P5B;EN+S<ik(Qb(Xm8h-K4Il0yMdCV#~BH;-{LhBP_gYs|jNg{znFCmCy!T-Zuy7GJ9'
        b'J+>B(y+$O+w^!Z=magrE^vXS)41-Y$u}IoxTR0sT&95VIIwMWE`@yhoj11-otTVr`^uA8vvrI*+x}J_P$MgDk)W}Vn;L$D4)4W)L'
        b'2pM@nxjTYDu%w)Pt!(PZ%VIJZTtp|1ai3nWwUoYpdPdu)Z?v?OzBKdJ<2d(eV;e4Ves-a{z4R0COg?*~y}k6cnYW(6ou4(%r}t&w'
        b'*%yAN-JxuH2Q5Xc#3Gx#{XE#U3FK)J41(Ky=X(D)*;v~d^weD85U)Bvh3+}isZn$1FlW@2HI=Q-K&&kYi*&Tq>8q<tt7*00D=D|B'
        b'OYQgW6K3y24Pc|j95R&-yXVhSxI1bL{Q0&~WOPN0xx>bgKLEy!3-do?Y0SXbMj<zJ3_Y=4)zd(bWZRi-Y&b#~6ERHHj=E=#(X?<m'
        b'C2^3UULL&%qCg-|%3~r>D-u5QKoW_P9+g*3L_XK%N<eSc$xw>93A`YK`-f3GTC8U8jH0S#7}6$>Or_r*by5qF+acav_azw^S?OGg'
        b'eQ|U2%*|2f3T#r=b7otcYg@C3v!rN0)U~<(5%B?3Rey=+s1()KiM$)59%@moWdDIz+gz7Fm!533HK^-*c-6_<9?@m(@+GSH+ouD-'
        b'Ub)VzDt~Za9xc1$e+Gzs0yUid5)osSp$laW3ZHw6chqha?xQcE7B1VrCR-Ajxm@BtKg#|Of<Lu5{fp7OzmGb^wGyDnX-Q@;p!A*M'
        b'MhVnc@`<Qq6UKI;Bqx;&BsvQ*Zj;db<D;s>!(C!bdW^?NssD*J^j@})XU~jsI!u+1Wbvo_|Fpe4d+L9svjMHgN695fX#a^SQLUfB'
        b'{saA~N)@E3wRN<^mFzjAU}vLL;~9nNO!jdxxL}_N;FXgrGuOU6xa8lE;uccQ2dG!Hn?9N%53gPPw8`CXJ)>A}4$6#d`&`^CVZ{ih'
        b'&GRmIMzLZkiJv?UUUVkr`+!%i5Ytp^)Vr|@74BC?F+9zcwzq5|tw|52`N1Y*N6&i;XB#^XM!m9ZktFX=qs#soU_ADR74$9Z47Lg3'
        b'?3~a(7^*sOGpC2nz`W0)`G7q%DhQnqjm(_hR&EsJlPm*D4~z<OWj+~Ud0Y@4sb6>^e@`cT2Km23`K#or6%lQR%79eU3JhHoTiD90'
        b'BEqA{$jr7wTh3cfzSk`Fweza}ITrJ%@Mtf4V+6^-+R@hhQQ^%WkLNZNZ)(ViVm}tLtfSvbK))O<W;c%3$~fxE?z$+`8Aa=3qaM$@'
        b'P4ykFboK)Tn74lPq69O!M9tERmTT-kP@3n^x{K5`)hi^hw8?yC^=MR3v&6So2Q{oynmq5W&%fxoedgiOb)rdpQ2h1fHZU+{zCWXU'
        b')1j30`KKiiJqq-a?EODWsp?h`J0C@hWjj=ORssg#R(Jo_;?q*Vew5EUI^te3TB0?eyK%LKW*mO0l+k;C(XSYOjY3?EO2c0uwW$GO'
        b'_fl#2mBNsBCyc^hwD^Z-y#fN;8a)cFch%e26vT397;3_Oqv|nrTCe)+f1xHw>&tane?!1?N0FQ^K#=Hh(+HyQFuy=9yv6$nkEL@X'
        b'Zq=wY+R!D%+=C<2e}YGi@JEc9GO(<bJk~mE6#6$xK(Rt??#KN9K`^|7XaKd!P=2UiKGLs_m{$b)W0Y@X9Zun+>+r(3`#gta2|*D}'
        b'^{1%9l_+vr9MM#GfG>Ov<l~3#zm1&vaiq=V`c@3%#<xS)=J^Qe7=`u~UKRg+n|s285+a(k`*~{3h<kX%N+VJs1Wp3UJtHu@fn<++'
        b'0{%oa!C&`(M*KPxnqfZ+go25vDjaF;9wDoM-m6GF%qwJ;<7o8+9RA$gQuDJzg)aj=LzZ_(x*JE%d^z&17>EKokYq{=f2Z5ihUj}0'
        b'Sg1OA!(BfDs{KKP2+4wU$G&;snjd_DJv2gw<{d_OjoBC}UM|TyGqPNwHmTipBkcVMUiHswlxD=;j!4XM@U4Fx5eC^AfvAY9c{Ku2'
        b'5=4|r>tjy|vTX60xAx}!Wn`zseC<l!o{`_v!UGU!_?awM**}d4J)ny3iQEclQno^<DYd&~DHgfDWCaGg<Y|-y^48|L{k$BFPtMY-'
        b'-2w9bAGUVHNp(16;2cYL@<F?u?mzE7foDC-Z?lQbx4$`4JJROvpOg&ZLKktCYlV;MPD>FtDtXn!*Yp_$jK<T_oTw&`(LKTbYZxt8'
        b'KApaT`aIw?-YltSc^DxajK$Q;&l$N)kWo;KkK!Ay?gpbd2Wu@D>2MKEZ?ZOl=>C7YA4bgWMQHMVgSbIU(2RM|lecQbN?jFNzIiro'
        b'&%mDEGGdCwOdpHZ1-R2k{57jCe!;F3ltR{sr5HHIW{gDc*d^I1ZIngs;N1PYq^*S`m7B;Vz^4KP_`KYFo`i@FMPk<D_6M-GLn&m`'
        b'$#)+-?0c3!xYhU%!YEE@7HhwGu<Agwm|chfOENHb^hnz=o;`u8Wwj$e&8w$gNT;VM%@%Kdd49TKq=f1K-tQ8FGB*;Kd%=j|{*j!h'
        b'lgE(_P>ISLVnK2s=AJdezKIgjQ$~`-L5V5iWC?^4bHPXH%8?YYy>JSv)Y3RccXR<$V&B81L42em>nMmhP5H7;3-?gF`?qC+PYn)2'
        b'^p4t)r*{v7an}}W(4JC(x0m$=!1!BR;-+@U1IU-ri2e+{*W8GE1sgT*)^Pf*;Sw!ojmE$#Lfd8)k_xf*xN3oXmt>3hr+fJah7AM5'
        b'#o~N|lmUpif+(!V7s$5=H>3;uWf(gP)%3-zkuzTmld^=s?G;MTIYm=5x*JlCoo{Gc0rnLbHLgwM3N}d4`xl1yibon{>@&k2U0P${'
        b'UVOx(OK=va?L9jTF&<LGoW%)y|AAtY5DRw}hwc44icJhVi^K1|nRA=>@1y)M?9pJV2obw<Slyw%sC$YG@;$93gRA1vn^%6AUk$s5'
        b'hK-tJP#<|WhM$ysv>50+5@$5Ypo<AiSkgU{Hw-?5uRx2mVZ_vF`9;lB4U*6C!Zm=+6<y;UN4z`pEkN<;o%TE}dwJLuul5xGv{(G)'
        b'Ff9wK8lz=T95p&+?X(Mvt&5;t_=r;(Uw0u+SxvVK&o+`_oH2~Ch6pbL+!od-NhvrBvlmFywCHW|&7n`9CK9SVA4RbfL%_7Cs?*Yy'
        b'ZZ;Ol4nv67iPjmo=wSUCy&+`yc&OgtVWLB9_H@02GrT|C5Df{Ri)`FKIg7+(5o;GwXKoFBack&!XhXCwk~$vR5e@$)r9E$A---(p'
        b'C?P$M5_o0A)t#HNok=gFWia+Is_-)-dYys&0TEIgoZ@ug(3Ath140hr2D8??Lu8=;%9_TV!o@-Ut4xJ=FY~9bLdpN>I!T$~&%@K#'
        b'T={PmN4r_makc{02(^8UYD4~w|Ne7lEv^f`z(I}ZN;u)RS{XGmr1s;Mkw3l52F&Y1+;;C89^sT-b;{Q5!|{#-2b_Tt;qgFcwg}SW'
        b'b%^@;)BT3Z2&i>R_HlsLg{kAjRZgc&Quej0PT|a!OyB)lIDGFJ6Gxa@ebZ*Uxtj^Ffx1@ToI65a6r&B{#TJa(Ff2T)tJ|qoztZUx'
        b'?(m7MetF@+I3e-p>%Jg6lAgx>@Go&!Bi!^MK3=!`geXW?JzWLbN6Z{9L%xP1Lb&nPCP40voLN~(%Yq^+Y{H#f6%hby!3?Rx(6m~j'
        b'L3qIjT~%5kyxl@!Hrp$^Bjy<v53|g0Qh1PI(J*U(KRBx&7P^6q@ZuP|ZOEfzyX4?x+z}q`Ms!BfL7WF{%y<;9|B**qb;5nM`kO(C'
        b'>CwaRyR63lkT&un>wn<=?@O@rhSjc8hfLTcy*FOMhhM{WvZ}y3|J}rF&@i2iv*a+CgRX5hT0zQo2hXEBM#xlB2Ob+@P(|4dn@ik6'
        b'D_nkwsqiO$ZDZ42v|_}ev~j||XoVm<7L5IIs6oc!!@^t1^QvE-9RoskcPJ(WXYUN9IhE=Y?Ln_r*0t1iRMY6D!sF|~u{`s`klN8<'
        b'i+;EL1BKdu1JZgSj~X2UzgYc&qTL~~?GY+M8Fc(S;oW7STOA^*ZwUNJwL_6sr<}g>=%<_K=&keoZ#jN3q&BJ<iG;-G6yRBT7)h%W'
        b')yz`KW{9oCsIP|%=Z744ZEywQpmj`zhCMe_7ZR5!+-Ve2)>l1!<zC2i!mj@>;fWuAnV@s*{bY!Y@F&GNw0UX|A&zV+{IwdUg+bmy'
        b'ke>=r)qbWrgoyLl-=RQM;D05SeRU6sLo<*}6XK|oRc%q{V}b+dj;W}x)eSY>%|mD29wKM7y@@X2(>_Bv2<E786<)2LRxqw@(__6>'
        b'AT-SI<`5(s4h{K}>EbZ|<%6!FdvJ_9{GRThb@wjFOQt0f#+3#!dZ~o^)6i*f#C!)s{c^Nx2&`keSmgVTr(OQHGpW;q?y4b<ejEhQ'
        b'y=RDqKVXAb4ry)vGOyw6?jg!Cq}P|moil$brR+l<T(ltY$UBcwFAR0nD4A?=YDz7BAyJuHm%QBbCgw_1)8X=zot|(xov(1colXX;'
        b'oAlIkL*S;V6BX(vrR$Koai?xeoK6=G^af&a#k#n-Y+YSkKK1laTrCP3g!}PHyeRw!_m&}#Tyo@{A?k^t3x`mB`qcIY96g29L`TR$'
        b'NkTR7N6)C$_ou7t^wj@=m<d&ZnANE3cIxC%RRmNeC!wl%sA?-zwH{TqZV25+h~zGJh{MHBiRd%|#?1cXzo`w0Nm(I0EPbI;>0Ul`'
        b'@h!eVUR@np*~Agpg*voZu<@Ldi;!P%DB6WBfer#~qbNF+5PhPo-G3lty}W8+GhY8{IAEtGA~G~KSwxD{{ClNnFEv=<#Ki%{p_E}r'
        b'csdAJi8OgiF&e1U149=ol+})Q;YxBymDzv1r&mh9@lcu}8W+XBqoAlEv<Z{!5c(l`dClCBqTmTC60#++?~GFOhAxyV^~voHfo;jl'
        b'3#32X+jF*+QcBdjR$K)0^5)~_u41LF$i~hXx=^I#beQu{*VbZ3*6zTEY%gY}ITU1gGoI#Xw>6gM#?`3f6=o-%o-k-SdLI)V3MPX`'
        b'ifL!w$Ef7Fi3-LnCy5k0%)!%l;bCdEOeRazlC0!Za_7<esvQdSkd0Z+NHJ5948|Pu;Awd?Q8+aZ@YIX%Gnd}=UK9E!>PMCzh>cSS'
        b'_w|AAUwv=G*}oUOS3L;GAl;^JmHs&0Hp9OM(|ZPiy$m7B6;C9cc);-GATXKHVAT#AI%`yJ1D&m%-~mQpK4N{jBi~jjb~WfR`S~>U'
        b'#Jw{f=LXaN?#CsW#&vEG`X-rx-sze~MHYUKQ2D#8>;J?>hDA;6?Hur5<$g3HHXiNmSH#T)M{fWP@^vnU!aX<udV5-Fugkj4$Ht>M'
        b'up-6&J&(D40^Ak^cjXswTe5`rS@T{S^x)zWi3B9s^2XqflQ|dALtE`TrCq}QM81>2TutKr5jszpyyPt&M$5J)#l|{iiHxj1pmyfV'
        b'n*)5;c`}R)avd*+|2KKn3z+^Lv}UNag=b4aJ!gx_;G~5j5})4o7v`-$4#K?3$t3!g(%o%pFiX^qcIuCVP-`t-SwV-%fkj8GP*VMY'
        b'zHpeocYnK+7O_tcf_d*O#+(`vTQb=C>|mXYeS9#giq00%1lBB~vnA~F1IPvv)xQz$w+)=Z3LyPp3N)75Iw(Bz)gX+XN~T!4z<;Mb'
        b'NH)7^@S75+Otk+U;g0`g_J0OplsIJmaRTJ-e&+}O@L+#C*fpI~V81QM9lLgr46-$-J6wA9B~<_3M<Ai@Jm7sv{=V~(y{iVDfq;6Y'
        b'@Rrtv14?)HV1xWXQ|*fPw<I}1J!OlX`3f?m`t{J`EA(}GL-HWdtp7kzPOpM;O5S=}mZD3JNJ(boSW0p70j5~8AV^qKMtoWL3%(={'
        b'Hj98Q`av?#&z3qRu!YhO)=_Z=_^A-Zr5COW_v`uvgU|~O*-uM(&@*($==4hN0vQ`KNN2z1=OeXbfTKB*w*5I>tyB2Z3ir)qa|g&k'
        b'XYs?rxl=ZBux!jJ!&)N-t7$zTLtTQg{}8$audfMookWY=Z0I0bU=IdLS>>Q`#Hd;1Q_m1=j&yp!J!6oLMynJCa!{9e)I&;5(V@D;'
        b'E(zvXy_3#2ZlSjr8<<X6+-f>Hq!AsnY7lh=VCxdiYbJ$urKwAEU8O3Mh?=~?1s@>s{l#*M9H8mt06Tpylf8ArsmocmYeucfqkHm5'
        b'xWrlfWPOCvZ~F}m0P)#G9)CmCD^BknFp3YV9uXV0q2L5%6IIcqbPHkChIC1>qrIfG1kwYr+SQKeotayrw`4Xf><nDK+Ncew5H%{H'
        b'M1vBn#%;?GgUxd$J=))cS@`t72A-5>2ON3XVE88*r{Md-KpYU0q5k#n^obiPMoveEvo9d-2}@mQ4$lA`nXPezEDQ5C2AD&|B`z#G'
        b'MD_9=E*jhDXulfP!T~YpD%)kXs~njXA&9D7nY*I@H%$%^z)45YCA~XCBX<i|-*&Fu36RhjAu(tNx|lpPJ5%ZdWvSBLsm)e>HL<Kt'
        b'TANvy?Y+*w6o}59(9vPifBEMd>Hum=Td<gV<3`H~vFe71efx&{^#RbmZ7x(@N3h)e>HrzU9vl!Bjv=lp<K6oQ01@hw$^mx`LcxWJ'
        b'_g}}|dk5I68{k)Vgvr@I5Bz){FrZ*ATYIB6nA6=~{f5|9A>Lg_x*Y>c5&-jyzko~s^NmMw8m1huR(1`LxHBGCx2a?60*x@+pyO7r'
        b'$#ij!<!hb6x|Ad*dfGr2-f8OmcSSr{@TUXK*C!XqvTpJfD@ok3J}xe9IT>u$-K|?M?9;>8OMh&j!*vP>1fT2AH;{3(aiHT+GEh;4'
        b'VwQ><9quKNjh1wGqZG<IVAy(tE()iM!YF_RL#t>d^%!u3F3O=E9cU)#qDX4PK*=SXF1nBU?EqagR|sipJ%kz|jHcE>n94qbFp{3U'
        b'^#gGPwPwIn5SEueKo>kot%m<md1m+@LKlQmc@T}wTMg0KG}u7}Pnil>s`N%)?m*l#rh<pT$TJ<|>17e7wSjcz0c3Vw4}h>Re<u1r'
        b'F-d6$xMNc$90S|TCR{*lG748j??YkXt0=6mQ@S4-h$5lss}Nb7Mw6!+DBD#b;WS)c(twQ>n+h}+@|7G2as;|D868RDjF>6&b(^i!'
        b'bWF59pA5`xtnp;N>T&UTvu+%zr5#st>(zDXXpPk+9;sA<Q&jeEaFuJ*ZB1&A5px2p<WyuUqT-R@f%A>&h^k)&bCeis(%6ox5n)Ne'
        b'j&xN##>p`*UBtP9g#RLL=_!xow4zl2$qhEI$2iF;Zs}={NCZVuyVnJ~Y~rrth~Tml)&3J5Moe{nJ}F1F<OSEBC&Q}NHGEA5x+==M'
        b'Y6ZZP(<gk5zyNOdb;aJP8(d%unEejL-a9wA<t+e2yZG2JrF;Aa?SfH((V4aE_lRXIq-ZoASri$GMtcOJtT~w0%q8XMbfCsoWpwx6'
        b'5Dp5~lHtg)Lx%uqO*of%P-VjC*<b9o&g24SQ=i;0>oCfDgDwc~m@Th5>i!UoA@;AR5?aG?hp<?giVg@QSE|*a9WD_#X&z4{YV(6i'
        b'F2(>L=Ihvwk|0jA93}?#{0*+iu(o6_Jx8{~I>)1l1nuQIB8CCoa#HU;dxP}~awv$*qM1%H;mFiIQnkxD`-=`&?T#&?oX*n$&Ekr5'
        b'_LF{qE9>)!4>;1Dn?lU%!=2ikHrJ-=eUj=u<rSIclVO}T$LZQ+dr@MG1Ct`|5yXR(;Hv&@M}&?_4c0|)u1yt;XSSRSel5V|tZ7DX'
        b'!8k+3Tr+R0Q)~mj!GDGDBVum$fA$vLu*H_YBq+{MvD%>o_sd4BL3f~(N5r%&Ex<a5*5*3j;?<ORBd4T8XZd01M`oc0y%6YerLlkV'
        b'vu-gk-=ocOxh05M^F@2@&|@l3U@EW|o&3UuQ85^Zaw9_#!AB8S>WgLz!%5y+dc(c*2KxWTY+4gtRkH1Uwa0}Cy~_oR30POEbW)Fo'
        b'L225YA9|Fm7}Z@gA@jII2-hu;2=1CS#3O#4bM2;GHkYoZ8E5~6c*~~U&}CP7XpN%vFa7Sc8-9Z72jr(<3WT9;-^V*GVqa`9h`4rs'
        b'Fe159>7>LkuBw|9{xK!Z<AKB8S3$44Hf6mIdd{PH4pf9{J%;){UQNol%mZe;yM8z3pRecMpy(Tn_~6k?$&C4uJlSY5^qXsD(&B?='
        b'MoHb@&)_Fw3nYeL-(ajuNgN!_3f?Q6DQ#fB`I>QIZM4YzTWQOK>U>)D7qki5pgm1!-{jF7ljlrd=x;nqyd*zOJV}sqYIR?R>ua-*'
        b'K3=!-HTf3ZmhASm<?U4<1K<3+v$0B2VNzY1Xk?`Q{O2;5o5p$Up#ZRiPs?5+YgeLYnbEY?F#j~c&P7c1cJUa{ohR+@e1?$#k+}2%'
        b'PX<`Ep~(!)?6oF`rZ{7lW>-c-VrO8AiJ6`|iF<SB7RIca%sR`PVnP{O4Au!L+o{RVsL)hoI80DR24!MGrb{6E#Awz|W}TS6W0{@o'
        b'r|<2l=K1>6X{8?RJiY!V;<BrBS%luCor{bz38wl;q^c2N#Me|uf9ps;jpOLZq8#=3X}s`(zyvvawg0F6S;L8b@IB4P3Gipks|ogR'
        b'edr4p-CVRzC&Lc5QOEl{!5dVm=;&kXxBUp!4}Ay~Q6G;`UF!eE_dA6sqGr?}05S1F_3EGna&)4j{zw1%@tODgI=;a<GR&MUW<7mv'
        b'$9V3t$Rm5xNzQid(W4j8`V`f#>c9A?A3TQY>V?i#n3J5-)wQtt13glyO=_EMq06<fXO)OsMR-=-JCA?H-RFM4A5eFYVW7C3a#5Qc'
        b'e27wyocM+WMGRxy#wn_u3YSOG(x#xA`)zgT?Mdtda3&OcoBGjPZSf-Xfssyq@4dGp{T|ncWDq&`TwqYsOF^**MUHUir?;!Neja4|'
        b'yxd$i)fvXV)-Nn62;UHO43qe+?C`w@`q5Jyfx7TUQJk_NPM6XMhIA$Cf6ozY-k1B`|Lg;D_U`RJQmbm++pne<B~&$wx@aZ49&t9F'
        b's>P9`G421v_qSH`lYvQf5`SF>JRazBhn}q5Ua7FPi*0PWY6I5d0RG*4Xe6@Ed(-b@Jm2q-#p}S(pMK*?U)pJ9clDFu&TJ98z5mRP'
        b'{svhaiN!ZTcSMSua;#;gT3^>*on52eQ)7DpSS{vqFlNPcc{aN*H@DOp)_d?U7v|gQNID*3+1%fZ7u&y;pvSmi1RzTp^poYW{v)&H'
        b'o)|3cU3F@cZ=A1{l0omkeBX*hGFbJO$<!2%5HSR1b11=22M>}YY?>PT2!HbI`A<0#J84CaNPZyPJq~<*I=(OWLaB95??Jn1j&JLl'
        b'*uN<AmiK=y&VLqdrGU7jT1_r&?OgJ-xS9A$SwFyERz50cf89??t=ZU$jwkU?_AOnJsG1?lZ7BuQN;}Nw9={oRxPFM=yQtq7DC*2K'
        b'#y*|&@~_gFelmo~#0-Z1Wa88_WC%B>msyUT+PRxaWR{Dw0x|Wz_Uam2TOhK~IxN^%%EEp=vgoq%oG9xm&(i%2SnT6>$O!4zNMVsO'
        b'x4OS8S(%#3gkZ5DO75HpWE>LosWwP4Yo?IvTuFyvD$iY7hLaI7bmT22(CiuWEXSpv@>mR`jxnMmsh;J8^kbfu5llFNT>N-9T8vvq'
        b'c>gLS21<TTTrRPnoL;M-?)D|)cS8(cUFS6049R`F-w7~`U)MVdDuR=PxkG%?aaA*n`0MEV5WMQZ=R})}XZui8hfjaF<Ue<XaGkqO'
        b'E@bGZf)djb)#+FJA`|n)jP)s%mNfYK+T6zzI#0Ig52@KkRNO%nB|qn=0dovZ^-E3G-{t+M&t!c@2ut(6h45J++)heN)*UA6&U~Wk'
        b'm3%RW&K}HJ8%F2-tIs3Be2*#eiK0c>x<d_O;owdcN3~xkpVOi5AKczPvI^|S(*nI>k|0CX3#aK-)!yz1_K`Cj<sILMPtRzU07%xi'
        b'JeL2A>cu-k&T%p1G|vF}vG?&<>#07sr;mLD4L{-BKD77kJ_g5BXJ@Cs-IrXdx}-AUqJwMlj`TrU2^n>vSq*xc4AD2~Jw_3O;|FUD'
        b'E|f<kmv*?lkspu|Kj-5NPC$NbpXbo~2!NcCQ`Pjr&-ny{OH?&tQu~mERB^Z@C^0EN@dEPwxkE7*nv|7IYz4wCbCl*(xjwKV#T;LD'
        b'8w*JTjiOK1LlIk|f-y=SlE%!&y=sgJCQcnPl=YDxTZ4(U=J^-umFt^Env};0&)0Y{)E||A&`7bW2`-o@yNb<D+gQZfiWF885wxaA'
        b'a*n~pM+w8q>m4D!QwKdEy@oB*Z9~O=qFZdlaj5EGFAN(ami~BOvUq-C%<2Ux;;aDdQK`L??=Xs`Fp(OAagZ8w!6YyOAkCUd!^S=s'
        b'V~MD<+>iC4Y2Af0o3KI+X&1iiNPbgwXwtB@k6db5*|(0!f3rafeRXgJDPB&HRc*pYbnLHC*Jlm!m`Q^^D=-yc=B1PFm3`!V-#jv('
        b'Fh6@YOL%vWO6}ulOm!S9?BP8$#%A>WJZDkC*E#xk)WW`)Y@GU4pD<5FU5`x;*t?{U42%6Li0=3s=Mud~3vYM+VqI!cpF>tv>kPwU'
        b'!^Mtl`(1v)PwyGBbFSAGv-kH^HPXeo)Pg?$r>3<gT9;dAlKS7mw#4+6-R6pt%Pz-d*=R*GL6Swma!PicrUO8_&qYwaYh>W@te2#@'
        b'_(U!<0m_$5wYo&reK5O<V<I0s8W}VHcQFs<aOduN&hvB!Z|0^{Cos>O7(0acQut%&+>sEO=G!1lG#~rd*$Z_rrIr%e8qlm=Un{@<'
        b'CS(Stk!ck8{OyX9A=#SOr1k-ShGqr^<@ES`wNn1=On*@T@b>aY)>I>ie`JjaZE$~o-6_A}{8Ut39m;(=)4AeCyF=-uvCkY$j)vem'
        b'SuNcdreo@Kamn=~q0{_+64x8jNt~SB2_rS2K)v_s^#d<*Akg__IEW!u=dPyJmHUW5tm@s$7l>>uat#y!<1DRZBG+|OD^dA<f6Hsv'
        b'+?TI!d{14tN#*|X`e~`JKxH{`tr@q*tomt2vbv@g$TvsKu)6rdbE?fwoOZ?DJH-h&O3v!79r~!8)6(Vu_A|t^bWkr6W3+N@=zI>('
        b'HWJw|3#O%s$=S<lBaF0?)9A88vlrSj+d&v!lcl{<<H|43U8hbze%+KQt~wu;11381-ixmRvSOw-k(^U)ZYO2AyKC~rW$%N&-zL1?'
        b'vrfEUC8}erc%YLAEZb3S*5~GmFTAMC7yq1(JB@+G!L=d3L{W0=yO#gP5p2a}PC{04?5}<#uK$HZR&1=z_%9@H^S1v+Vl=sI>kHPK'
        b'qR7({M7{&@;@}F0xWtWZbEqrCkRffBuncOJl@2j!fT~=3I~i!(U&BRXCC&V{I^{OMGrI{}tHMpz5ECBiAwo%&>qP{&uf`#^Jas*{'
        b'PPy?O*pb;Xk1@2ZBdl;@R`JFBOFyG@h@URJuD^$|LcCTbT6fWk%T0v*>B(!kcCdBCYH*>Wv7aGulTmKP6HG*cfX4}=RY3H}_4Yc^'
        b'f01TPum(q)LZbhxKIOHRdteBg%rbt>WQsPKXHn7DX!?PwlH=mfiJZ!=d-fDN?^<o~(XSjk{VSmh<Ok0-$PZSsTM&yPo7me|g|9BF'
        b'wjRe>7fREiZF7U}I?G&d)8t0wG|SlkAegxI3*^)5!X6jN_M^0e=c%~s^hFWZ5v_C9hQ-NsIyUBdT)a+J7tz_#DD$5!t^tG#WDeTw'
        b';2Y_z3BSGM{_-l<v5{Q<(8%_RS%!$~giPEhOF^G0fuaDZ<&3!s42Jwnj|(TD8CMW(gb1T%T?g?9o`6g;7}H(4r_1P$#cF*i6?nZ>'
        b'b{!nYClUCPcOR9f9V)0#k)4*q9M2v_iAnE9wTiAIwcLQBp0gj<CqX_+c=OsX^zDz={O`hEy+-2Tq;f9tcE?=9@HHYZ3Wyw`l|TX5'
        b'?%Nd-7p;ar&QI_9X|Z5Y<n)Jh?N|Ma&*bslPKN#S)#D<ME{FXB6ec(n&g_H}=bY#C4rN8SgQ|#g7%Ecs_XnO9HRH&={oAa$BhHSA'
        b'YFp{8<RI2|6-scj<o%bgyU$$X<e{;({}ih6oDX9UqiUq1{Iva?cjB6{Lu~C(t5%EIlB-U)h|{gKRVem{E%tp90#5S2uko%XrMk)H'
        b'IiK8>sf7P&OKnZ{gcuKz6ADa@&gQQPkznZiLSf^^(~;wcTd{N+49oi7zc!lp`n4)+44ogh6p2mwRg2{+xx7Q0n_ch{{*WYBIzi4I'
        b'#G3=RSJEMb=JZUY<4>OjKZeNA1l56=*}19fg!1GmVkO3$y&Jbwwet>|83euL+aC%(FKfKoQUhL)4HKVl(~-!rV^MpZXVqPG%3S%x'
        b'fmcETF=9Ekx8N#Z2a%K4Zow)q0q!Gp%}#AD+Vx8zGBEEo;ViyUjgH{FjC*6SJQy+(%xnx~BqH-!nc?wk$Tasg@N{T2A&#ck%%UE@'
        b'Mr7zsG`99xSzC0hCpt!(ADE9Xdv<1C)Kw3W&^CJmTK7=$`S|;VGd&)RO+l2S6_2XWeEeFW%;S==3sD-4i&bNI8<FkNC|g>@g)5bv'
        b'&$UJCAXb>7OqX5l&?qj3Zfqm;km4&*POE=1*n8J+=b8QT=zio{hbt5<e8nLyfFD!8QyC>^BYz>gdRwSUhiNBycEvUQJK!Z_!aH#O'
        b'{Q(B%9y&XLo$`VA45{E7lfRVv`PUlostD~Lcq;Z<8=ZVOQclk306BAsw14DT`Be{{%jr^us%`Al)q8k5gZ=xF$ux|<*$CkRLOL<M'
        b'ey+L(mJ?&esE}*SF`ls|8=|f?5cPNYM#3=TS~hX;<pv^q1si~hEhp@EcqV=xD@HNKn&+YO%wJF48|SJvj5~(gI2*LEaDo^1XY$&v'
        b'q5&v5V7PNNy~n58HKW6w4J<--{&zmKKHciG(mBhvlf|VT`bn5@izBQBxgJe!XJv8ez3A~x-~1kuqN>=7K4JQR0s&S{E=@lfXQqC*'
        b'T8ww@vqs;y1*g8hN^iQaaEzyC&m!gY>S${CDqZk^c1qzXP&O0VHr_G>!VwCSzIOkt&h@%z@;S8dB{`t#5K({f(R9xKo{-k7SILvw'
        b'S7w>d%jjs(FvyysqeE33W|AB*&qj-*+O;Y=npBxkL;MPzbJ;4(kINduPKX+n$8`<KC#Xil>A()RzL_W?LW?svOJE(#dQbx#dmBWJ'
        b'vIb>iSOe9lYcMn>L+ff;$9k?HiTwlgevT?1eSeOQQ1*<LWQ1<Xuz$>BG;!nU_Ny4Jxj}Q6MD4UPKDOkXp3~&i&Z)p1v30>alPc(4'
        b'Ox8bmLI1S7ZLA$t7e$_LMRW2YBogL{@ze4svRTCb5#_nxx(YM1h&?FerH*;e31^}@XlX7n(Uzbz@4@Q7<!M)FH3mMxOzzls?uV`-'
        b'SHU!si<o72@#^09d_;x;O^qf6IyDe6tLJU(qFdDEP+V|;9#DXM5k`;}F#v!WNGFJ#>t_jTsxWzgj}wG}&O*~iiVxj3BFrD#u>kGA'
        b'_yni7o2PWX5PU9Gel?e#K%X^>R&K}Sh5z6a+U$ahynqni<pudW8q6*S-Yr&T`v(<=V^zgu5ZWEK27&0CuihI=Fc17-!m*%2^dZmt'
        b'QA^(2JX?`)Yx67Nc~W#x)HGYXtT2c~e#YF9NZNjrkEEZ(AH~T4rv&R<?##lne&iEm`;Uht95@m_cge{k;j<DdkA&k=Jr?<F<QlXW'
        b'Zr;q7EXAbbyz0xTy-Th-1FxHR1v)Jl+w2p*h`@^Cap`=_P57Kkv9@@QjA&_<9En_)cA!R;B5_7z=C8ziRX%6jqPvZ)ORthS=o^wu'
        b')PlP!wtd{*(K*?E6fGdI!@bB#5T6qrJil^>GXRVEbkXSm_A*Mf;~3T)&=m;Tssnc*@6?H^=vr}S-(J4g8JBeQD<RX9fsp~;FZjqE'
        b'L7mcJ-u&gb=hHV_uF|Mik31;eFo90gWnqy;S)cOH2TIQg>jGzRc9%~$3!RbEtC~;%t1NL$`df@8fypaoONG4iQ{-&dqH?{f)Nt3A'
        b'{%Nn3@Odo1Zi_am%rmW2LQ7%!X=zJKX`3a*Nu{X1!i>>Ia85``nz_c5;q#nPbhut_bG>^0{K=EexUZKtir!ivZx)*~HC7x;ShIFt'
        b'68O`1XB&-}iSVgr&$3b}9QEssxng~xGA&=ZagEw?$7jkb&dt5K`Ncn4iC*)*0Fx`ll>S!U6(49JG6>Ak4-uc-W4_Zw2k6W_D8^_W'
        b'AOp!6PzhsM;7tGMqJ_!1lB5bZ)b=tO<Ch@{Lks*#{xT#0oPPrI6fOlX-#i}Rq2g34u);6-Rm1|nkH<kPU#vMTLt_`(=*;Lf2NH#s'
        b'0xhmyn0rcM2=o;~%$$SoTVC&Nqf$1mQIM+K_i8*Y9x^y8CD&fgW%x{@x6FUJnOD<m(x$7lH$6lzxUs@#1ty}GRBc?NH)ZsCzvoF='
        b'LKbI9-CPsmq%s(nJY@}6DCG(hxWc7QOR7m(%uuOiL;4nRmrr4N&u7@u+w!3raqI&H5U2k@kyqzSD@G5ZSL?<4L}hM~LSLjN3E(K1'
        b')J)_asj*rfu;vweEIP)bWh^m_C7H3LJxV-JJPG~3gt6SuP`b!Nke|vh1aMDpP83sxy$qdPb%?V2JoHk;FY8h#l|XU6ANp|bHv~gJ'
        b'+!^A1ipYD$XVT_X&6Yk%nCR?)XK|^8@V&xEeIz}~bCf=ZAR~6aBO>KaO5foUF`s^eCXrJ$4+S0Bld$2?{>0dv@itd=QaJ8iff;PR'
        b'jx&mrr<!rb602<r@T9+0H37(0$-T9FeKk*pdiU{I2_+^(u^1M)U7^Od9WXrO!{(e<U=hOS`0)yC0_>T>Hx{99@i+DxR{A`eyrY%p'
        b'<ZZ6Q?;oU+BkFI?K2j6Dcd5@^<b#f8;__S$bpv6@@o|;}Pr<{8=x35@ajzcBxdgw`G7(8YBJd8x3DUdq-S6P`Kj1m5A(r(aig`ES'
        b'IU1DLiegz0;|UoMvxgEnAxU9))&h*7v}C+1QO$`y0z7279;`J{tl<G4m;Movkzq*iwNYA+CcEXl!hCl<&~niwN+$FVD)gV%wChVd'
        b'L$YMVzF5pFCA2o4%#^O-g>iQ9<jIIm(33t_fcd~skv0%80_(Eg=dt?dc`{nM5~Pc>#4LGd$00oHDQrnWQY`Kb6-BLvxHlGy%7D22'
        b'Hb$23&^&v12QIyU6)nTPtFfzVgLWSYD%{0KWlB?dtZ3~xN8NAM1*)V;%qMrqx%!uCZ2D63*-0mLKj*z=d#whHYV+m0j0+dUDTdU!'
        b'6+T;{8pO@D&(oEpd@hk4?;S~0R@bB-s3D2Ed?wo=U5a5b`xhSG|4LLyQfxJu!S?qe`TS%!#gX+F^jUs+(th0jFKmbA`KT*NbL2ZT'
        b'kx^%p=HTATy!kMQ)cvZ)`P!%Ws298n;Vb?S0QZ`)gaQQfcb);7uS^<huP~ZrDq@`R4n$o~I*x-zWUu!oUB;!K@B*oRIt{(O?D<~('
        b'K97mIAE;#9WvO*_`KD|~RwTA0afgOkq5*D62eE{AlI8>~2|;zdhY)aX%#T4xlQv_96TPIYq9$twwq!M=WHk%bgaHuSh8kFQX_ri&'
        b'r0}?+j)dUeKVm8~7PAkxAL0#7y<7L!5eO%hpf6Ua7BALX_^3yuUrj;tHq;<)EXJVk>`Sp66q6<bZ}M|AJ2X)sYS5R>*pf?7rM;Rr'
        b'?6?9|sZ@9DFY#DTBBEmtZ+HrLu}YQE!yf5nsD#}_fT0|eVqWJnQ0FuoDu8&d;9=<+sF6T5?%{W69?cQ>{u~d?G1p%|_#X4gcOV9j'
        b'*5ra1tp4`D#Gv>afvc_6y?%@>`#k7=vLyF&iSCkL%D{SNg@d!)pLLesP=ExqfJahxuICq>;xFjl)caf_6ePn_);m`?+~!^&<FXve'
        b'>c4F#LoTeY$-Pi|(UK<BVH>XO(8O=}`UuE*Dz*X1y}gt-t4OjOu#sWRC-tvM^|j@O++JtKT<@Da<Ff3~EMQz4laAn73}(2~!w_LH'
        b'8eE#j8`kwg0VIzuTcV!L=w*r%?C6qu#)ZhWC-Dq;C%^KG?CVT%SQfgG*U&$W!Ttbmc=QSxA!PrkuPiqt_Hr5XRJXc)8GKZ!bkh_W'
        b'0)r)MC%@rr(*A2vS2lxMp?O1k@8(N*mYR2ZH`K|p%6L+10;qV1-y$QTi0aB3z-X&3HTQkYd~#TSpj`FUH}+7lYha+W5xv_I+f$0Y'
        b'K0bj!ovG?2brl8D9zF*}ftXJQ5G4wrB+C8`kJ@5`4DVNb=Pkqap5y{mdAlJH+MV?q9;t_YvkW~bRr6N^Oj^m_<vd8L^v5YHbkyQ='
        b'hN&xnzJ^Q&88ghg;=Xf5Xe>I-#;nkBpL}e-J)-iCL|xx}9QWRsVy|A=d>Oa*O|gN!wtXH!44f-;SsCaG9ceF2FAc<zz;Hv~mDY(X'
        b'9B4yy16p?3xGPa#U88VX5)6OsLE^g_r0+wriIhQ89+Dy4|Cj=qVaKlcg{Et<a%;^<ozn2-mFMc5Aj<Q3jCm8AX29o&0T-^2OSz0q'
        b'z**_5JXHLsR9~lt8thBZNHd(f0_vH_Sj1=^_MH9ed+`d-vGq-f=&N}B$?_I`>A`p0?N?gAxWdF|zfT1CV)&?+r6ZFqQ2W+w@BAqa'
        b'1Vks<m|A1jbR!!phI1wFhSB;4wxa<DA>~|wJ9KM6;o8fw!<%vGli1-T-1{h&bmTWzVVt_B3@`R@noQNXBM${s{Y%iEU5AuSiQso{'
        b'O>8FoAF55%yWhByk_ruXpT6P}8tzTU1XUHYgh)CP11fX>F~paaX}+kI1r@;{z8^DGU)eRDH6N*`{VySirfCR6<&|9;sTRx0-l1EV'
        b'le`=B-Jh_WFhunqu_f10{26S?x!rS)EV;ZJP+j8LSFa$sE4#8QOgabIPA)67H0wodhc1Ns<m7wVxcxlOmR>0-&XrD&9i*Q==FPY2'
        b'3=DLqvGW<j3iy3kb)^=O^5Q*GHeUfYR*c(sVTQshWOBtgDe(qE-$eItmvAmjwzim=K4Mb;rt1j$YL}F(jgT7F!I*0t_v_Fk8SZ_1'
        b'3i{XIyV8#*4R?Fci_Rfp*J1HC^sR5HeUxX5ue9c%c93(qPwsq9*gmh}f{vE;yBrG7CwJQ&YS*QjvTsJ3(S0iDK8KY@rD*K5;ys@E'
        b'54TxX01=PM+o%--6NVezj3%Hc1DAfsGxJkGUe+TOsnYC0ZOgsaHvJW{xFW=R9;ViKz_E%9b0yb!(fW`3Mz_Zj6SF&h_ncq5`@6~c'
        b'p09CE9`U{dw?|I7=_?nh3{IYQ(UOb?$BHy5+VFGFy+Y20)LbEn0|-m9_Z=Q%=UhQ1Wp<hq;>UQ*@KHB&NyHFou?4uD<+B1n)_pIj'
        b'=Jexs@e~=^9OPT8>Wr|9rZ|wP*efNLC8)6=RxTbZ+@neYxQR*qJ8CkbaE+?7^0eId2!j89616SzO3ng*>qyB(%M$4uJf?N1Vxi37'
        b'B;Y2b*U=PRrSkSo8vX`MTGbgMy*6o(AeCVl=qV|9_))2MFN{S!OjdO;8DKdXU=~XM1K715mramxEwY-rdx(q$S#6UTGSzC3iB^Q|'
        b'PK?hfKo;0zSWY>zxh|k$?jO6MfWM^S5){+h-<$+0P$lm`CEm?g(g{54Q4D6ca6Iemq&em=D%SXOF|ack7r$MB!-VZV+rw;K=B=58'
        b'iZ>t&&-*-7ym3PaqTy-y8<#VV?7qj)#0fMU6KJ^5^D_-?K*M5t`J_O?1`UuPEygw^qISM10DFG{d<1|~vUUpX+<;6{`{SsN4T9ad'
        b'3ENPB>ewd~JN1iVbx`bA_N~)()Sx;ZN6oZv#5Np)n(P&mV1|+zV1v3_V6N5vTy#&5V2>K5znvsArnzkgbPsyXlV}1J5?DxBVmASP'
        b'#*Iy<l|kD5_EnQGAx@|4gp>!Q%fUco$PgHPQN(mcNsrUQ5E%xkaq=SMY4qQ!frbS6&;7fl=OTh&>?xDT7h?ocbMBS5_HZaSQOZmj'
        b'?5Lk0-Myg)(;r~AF7+l%nr~I?jq3IUp4hxKa+~X>FLTP3s#Z;4t*UO%d}E`=*Q;tw^uBNxv8||Qy5Tt>e_8gqP#@Ip$7xswEl9G5'
        b'p)~8gG$W)X+e1*AXu590Ly(qgpNZ1e-GfVpw1@10lZJEmpcX>PuceYn23U_QK_>kp_tNhF;{JR9Nz1x>7jpuP26$%3zK1Wm$B8;7'
        b'-Fx$Hl`3l(^*I?aU2HDUo@pPt3-w3#v^1$b1=-R)cQMO@Jp{fu7g~;1UIOY*O(m2{m)-rOP)yUyI<1tVhn#J)F3X$Q^EA^#YqPh}'
        b'3c4_xhS`n|ppUJO*O=QRd*}9`eFF;vVgc%tcBRLLfZc-?s%Lk_E1T#GGz9LkZunI<+3IJ`?tD)B-qeO@>4Li$^+R_D#kA4c?#Q09'
        b'ac$ZZ%;FyFDi58lZ&G-y*(IWns`i70PSSb?MC*RA=tzS8c*^7wsTY;&)uo1Sx*6h{>KUcVsI*e49Q6QmY%13bPH!5R#<^y7*}uTy'
        b'1?SsJC4+6KU!&fr7hB)vZHY=qgs5Sv+wyuBc*^=U$Ww;Iv}C2_Z{7Mu>grsvevNWtq9PY~m{%N7fP3d-^-WU=FJw*K!Ke?r89Gn('
        b'jJO0{w|jW){$DW~kyZ(Q<03;xcL$x<rpcxg=DK~|>JJoqIt!VpvN4xOPiwN((6oYV!-?)38fG-atdDtb-yM&ujD4m{*eg<<AIv-4'
        b'&1myHg?Y@@d4{*UOEeGfk{1TeZVUzl9&KLh-@ECpb30s5kocY^x*(ffjY>-U!G@u;^Iq>pU&2_kvySnGH@Z!l>}!P~mXAT7E=@Wt'
        b'FMNF}>Rs>WcaRBlyxR)X-eLt~S*9vi8eZ;pBy#Xq7i{@mS2JOaS&Gg8MA&2RGMa4tB5-e)8s6=8QcJ<@Oi>(sN1y*}*>=4_e8JDn'
        b'Me4R=y#7J`HmE%PBZgXPS<<C{B)V)oH&Jh*7>-(+yINtgFjmX*{l!6so!w5&1J;5EoR;N=s%{gtRKExjQgzl)(oIUNnk-X6mesP1'
        b'jqidQIZJlZt{}tX(3%vkAjM?KwnRg>Ewx&*mhB8O6aubPYeA~hl4Y=>7BBlA9dz($QtLmIc1C#TPZC6`A*@UA|3TF8ti^W?i@Nd)'
        b'RR0twKZCgrSY7BU+T;jQqBoa6Bmv`8l_9R*GnKGOT7D-_-o;SMOqMKQ0Mu-<EC<_}6?a*wWt;_QMAUJX<@PRQqdwUUmB4r+L$F0>'
        b'rGvcTSBReX3-9x2^k{?WFNmH1phs`G`Q6X-1m86*?6zvMleQ}fBE>NHbCx~mE=Q$0mBqGPaoG)yN^3cx$o;L_rWZS@<g$N*ShonG'
        b'T=F&#vJR5H%`e%@x}U!O-A|IeO_1!T=S)jB^brU*l59)jMJf^G`@%LcXl4)w^A2U6vfEKu6qfp00JuTb)upNvAu28;e+_-KD_;9h'
        b'fN=0<Tar3AxkgW;>xPfw^xN;LwYK-@u)>{FQJbWT@0c@YP~UeY2Pf4^2wYDreSo^##k~DqzA1IlEltekBHa5RW*F=u2m@hUNV`|Y'
        b'zM?eT>;matX2tEl!l>~sy1-x=?xJI|1A1_;5zCWxlOee#g?W(#8EyFyI<xid_qJMZ#o$?sFl)1HE3IB#o~tf3mylr0t=$qxb#;*;'
        b'I%^C~gBwc?cd0cBGUOYhiAs0~U;FF~>T(x3o2GHP<8x3Z)F^akf;vW_r`4*9fq7qa(b~+a5b5W$uHt`4c+Osg28?Qal=`g8VE>N5'
        b'ANaX{4&6z%7J-xQ<rzFmwR+TW$uDQ|gz*9U8T73~$Vk>G@}uZ%>#@IX6vifi5_n?OA;Y<!fD@^AySyLpPkf&XYPKNT`&XU}$@&V)'
        b'9S+8`YNtT|mR->c8klPAqG@Rn9n4V+I>WMFzeDRJG_C9mw!eA@+HUZ4ec6ZG8!%dvV4@bp1mn_!m~M?JSQ_iYz0Nxzk4fL-_IY=9'
        b'_;9HcBZvitykE%MQ+Gn}0Q6shW1<ONu;EW#gfRfR#&qnDe$uE47<&t7I)N@0QT8s-*RDenk0o6-p@I66XBUO&2t377-9_V3FuRyd'
        b'7;Emz4MWYOeh<TW0bxwht)poXVH8u_yO#X3I2d@dR)yPN!sd+Q(%TarI!Rj&BPHvhy9Ay@t@tk4s(MCE(*ZD6LHncQUJ)b#{kDJr'
        b'`7<*gQ-xi5f9?V-0Pfd*(CLIRmD<y#hNuM?kuc|3Ek`XOrGQ{_SOo1d8rF8jf}Qj#w!00NmSVK)SFy>s_YW8pjeRDX$_4o?Du^;<'
        b'bP;$eqshh82a;DOIfDQd^=y}V4Jfk&5E?40E9n;Q?Z9aK=p5@z;7pW8m#<@D%V8e8WB659USbzbq?sfMq$-zgCnaig4HR1-+4zVA'
        b'_zAh~v<N0G^%^xGT>I>Afz<&exV;Ud3@{27Q}=f*(I(StYjE#*Ea@+}_Z^sV^bnPvf<Fe7{vk$byA0u7bnyL5NHjTH57hv7YFacR'
        b'AlA_HAJDDnn`TP_71@=H7iDOGQvu_+{k4g_i~m73!0hSXmyS&2z44u&gOsAn<7zn0HM#5GO9G0WZ(`N^6sox89KJ~<%LX&WOc)AN'
        b'rlQ{Trc9tyS-}JzKx71D?LcNctrdafWtH-@mQYzS5|3L{Xpvc|1v;}105Kv<EPWDe`30)Rf9t~Of&}{$XpBJo(0`IcI?sY65fU*-'
        b'ihVnzL%C#gatJ{L*e7@@q$@XAP_n_8=B)P*kiYC1+-~O$m%n2)Nf>b+dfv+c@+Gt@bAKD|t>jBI*%a9oyBloW34*vk_b+Np-QO(r'
        b'Rn9&F`O7h1!c@XX-hc_j{4qRh?F3czAA(pc>{%hkcpE36Om4lJNPoC~_iRG+FqA*S;NDiy<%_MCL=ZJ)MblYYE7W>yvd!B8Gk@*}'
        b'Xv)u9@m*WN3jf%V7V{|O>UV27-22c(p6|O{t77dwxi5NZiP(GXN8p@Ev+TV!`2S<=-NTx?(#7F@NkT}rbcaAdMBRIbaEYkNjtW|B'
        b'lYkLXJ4q~vww*&j&|c;{h*X@GPLtS)XmJK`I$o+XNi6l!QZb!r?Zp|u7O4j1Cf-1)Ez>!@jdiS-DCGC99kes&obR9S_dO3!*lX>z'
        b'-?i4e-ut?FULV~fCdn-QGnWP4oQ8Pw_oGpj^Yw?Wux0<&IFCC-$^Bj&+BWjizqD;DYMZ?er((H<DUio4)Udm+z}Rmt)sn;vN{;Ei'
        b'Zh4DodLe$lfv~(hYUdW!#amt)g?D_f(4(9bE=Qx^cE$Gb6==5QbQo}F7di_~18~3->)yY@mFC0Sl7%T1kv`58#x<jxkH&cO+m=Vd'
        b'm~F1m;QM4|DGb@fSH>~2C_KMlg>vKkUn81M!RF6ip(G?r!nVu@lsSzjp4@=NbVOl%><s%mVML$y88svDUm_Cnd>B$@_8C+>`fq+x'
        b'@-X<a$pQdnh!Uf9D@Y+bmn)z&Sb*bpoqa}!F07CJALS~RD@vNfP*egAw>~^H?h}7ONHk%+<bM<|hT?Cb;+FpkQ)0@pS8R7IppuS>'
        b'Ywi_qVC3a%mV;c%Q4(w~y8y$d?UiG@kJs--EAAQ{3mUEuk!IF9F*3%AV7z4VD67AMR!y$9Bq3i^WyDtbtWWBoyL+Wv`@N^6^6J9s'
        b'P~AkZv-GJ~V03d<v&*j7IjrWomD7QIAD7cpukgg`!u2uiWOzs}RK~KC;9*MPyKx{EHkYkq6Mz_^%hiOX04p~T9tT#gd{Y09Azm#('
        b'^9doKl=r_NEOt!)*$}Al`*f(#e;C0?OWGHp-sh2K9V-T<sAGqR(knqkqe*ow4*KYwQT^Cu+nvkYgC^a*4C2>Mq_f{$=Di>?<3O-@'
        b'xmFNX&?KFju|6z9hY);w*=kpSH6oZOnW{>~k*Qajc1<Y!nl8ION>zC#1EcuvULFaI`W*`-pN0XCp5tLE2V4d>F}Y#j@>Ar7U&qT0'
        b'St}+ei5!w(>y8RaHV4q>`6!GHmnwFbt0nP_B1uh5#@Kv}2zk&Bb^WHH68sbBT_rggyvpUwhF?zvFolY&b1|+#82OxtB8z|$&fWxH'
        b'EDH4Pp|Ji(cyGL~&yA8d!x#rbvhkYctI^EIJ=bm{<_6vJJYhK&UbJ2gsAJ#14A}F05M~cv<~VD*9V1RkLSg-HhKfpq@t*y6>@Wl)'
        b'gvD?Np?A&D{W)}^W5sCtddnMO+nbl!*Dr%fR6@vj@stDNVuQ~4|A>IT9rG^hbRq_f^R;NUuf&m=y1V+x4iMXGb`z5KvBFY)dI6=f'
        b'w|_fCS_d{2zNF*YuQH|E3;#AV`D$7c4NM8;dO<BFrzIhKjXU`z)kN(Mv^~i*Z69$?P-(wXsb^7U$BUO4JK!lnURm8YVYpJ^ZYv@s'
        b'vtQUqF2dwoNyoj8Osqt+NcCnE)E)e1vN`Sdgk>EvXwt3|lK&jDZMeJ+dauc=b`z32w@L9F+w`FaqQbM}j?o($`Oy$LIh*>k*ITt_'
        b'cEWoAV=-2)B03gfsi}nIsXJ+vGS3rt06N$aEALQ^`va9tXGW9zJ&g$O`nf}XwY*S^dF*!p(HtkPD{1N)eX^=!>+N9~xH%o)-PSL^'
        b'Y}@z~t?I3pOZG8E%PC?_JkhZSbF(vmG^m8VguJMD$98Mlb|!=795a6rt>RNgI!BXlbX4EwPKJ?1vI=93mpLLGA<NHjrlOHw0KWR!'
        b'ZwI+v+)iYxevNZ@5!W7KimPtUq0$PXM?M*y|B7b~w3X#AQ;Qn8MGnp7<os<>8)|3DSFBjh0UZyoQ0(880=Nyd713CdQu4D^PYD0j'
        b'@JlYl<kf&}Aj^(mxV^1t)sxDF7+U$qh6e4NBpBbJyc1bJd^9OI$#ddfyEoC_W^{crh!*R_T?SH1dtOZv*<iM*+!)JV7N|{Yi@8ji'
        b';$VCnS(l3i1Jo9MnF`o7i_%_`1=?t8tEPB@YE=g-x=bysgm&K=@}Ia#eY97+VN0>RV8!yEmnXyy|60-BW(4-xT1Vz#78-`6e8*I!'
        b'BpP}H?;^eFZ8L7&h8~F=_yyVf{*H<85@mPww$aXQPEv|RUXn|(@xC^MZ)*P;0S~YxYRgx^lR;(2`BBR9l4QeX4#{6mDUKnD*$B2c'
        b'N2no!GQ`C8Pw!b?fp19SXC1-?K^!}y9JJ?xFneZ*vVc6XwGYi-`H}<x^~ICo*}(ho4SWe=c*j_W0lwLh^ewcjZX>*<F<HmWuv+{x'
        b'l89k2nOdxd-;O(=M?N0PUaneyv3xsWSsNZ{8eK+szPW`0-i{fP)ku)AGaE}28yye-BD%!ETcSkB?wJA9-GPZ5z9A}Mr=-5DwKxr('
        b'OT{@J9*hU+QWtBvOLC4Ghz<$Q4`Gh14aRb%iL7^s=Q7KcQ+VR-s8Z<rT()TNzVwLJ{9!cnca|Vj4xXD<^BzZZ%ty9Y`tpb$vE?>f'
        b'KV)Y?aL!`$2knlTKgpfv@7lHwapGE4uZ>3`7emS6F(hFa@JEeIDpPWJ6vbRPx`dsHVlJEzb2)qka@=fo3*_(&cUTQV9tC0qj}=})'
        b'u}1b`(7D2g3o7QKVs6${%!oj<7IP>N<5)8UMy!(&StCi^AS4^vN8!1IoomccFltnn<L5)V`!IPg!P(YAU8>&c4%<++Dpg5%nlR08'
        b'MyXkzI@Ept?X-BpvkP^;QZ44vp!bse+pG<+CrwpGmAyKe`G&-O3nW)f(+V=GZ0l%duH;v@+`uav6~HTO-q24r;*7gsB3L?au^Wcc'
        b'Y6(flE!(3*j?ks$;yG4J$S4-dB-~buc_Se_$K5uF4MtLUR@^oc(<l{1V5xmDzDlvaF4mKD*N9JpjJnv4gu4v+ERu)ucTcR9a+*c&'
        b'nF&wqU2r!_qa>tMR2(s^mW`H1MPU-*Ie!#&Z=%7sd<fmaqBP~JO-l@>r8%abEjKN5-MobOe%X*MacDWdEC>IY0bi=dmniXkdx_Xa'
        b'53!4eNU?dj86(ZO5np0^dk|bg8#QDviMB-#(Tb2=oUAkxYBOmti&W3!4e>+Pr$faGZ84`UHfSHbV#fwKVv33<SboSieMm_VRxMiZ'
        b'1qGA@DLjx$LL@whqDqVO*9UEX8&r~VwRkC;I>ab|hZu&HDM=$z*Wy_W@UK}yGvIV+)j4w_-J$V(q$l1tKwprm5NiYKIcVK#AL=Ib'
        b'?jXTl8blUNsSI?f?V%wsVl$dfl*-uw5RZ#kIdn|U%7!+VN^L!Zq<98+z2FHO@n<*CQFcyV7vB+-v&4|ib7^HI+L<IzTQ6r%3?d@9'
        b'H%OYr>?eZ>>!sj;>TeH{IZ_mgyEPbbr8qVR7!+(x_M<_HB#D{q^OyJsTtyQWZP?Rtmj{jbPr{OosLhTaTG2;XX2bIV+tZi$<0)uG'
        b'?VOcr9zSR=*WORtO9|eK^MytFf=dy*g(oLxNeD~(ExmUTEWs0Hge3)|5-Lj<r9D5__WGdftwCO#Op3F?jtS;8>>32i(=DD%(^?)s'
        b'w61ngl^4Yy*CF85WE6qnGW{m#%`{uxpvyH#ErLRg;>k+sw2J-AhONo+>gqxTDb6ADGOCqjYUykk8+dkiBB=_Ev{elvP_v=WLXg>B'
        b'RyaC;bw~3}UcIRB_|2w*(d1c{LpMPPzPbtRcPnroUn(3Kqn2W%nB<Q$AUqL-EH#P2qvTQ;Q{A}}sR$&k<V%pN<%5ntpuQG^OJ15+'
        b'w4C4fNLGB(3d1w}K5f=(gvX5W`)0vI#|(`3U(9-KwSFZkp70}K$;H^%OW?`~BZ1hfW9BW6OxBkSf*BVy+iZh^A);l?gZia|whb`O'
        b'89y1b^9S{=LB2$50Viai9o3MAtuXNXzPzk>tKK*`e|Gxv6^(?Yj7a-4;rSJoybw~JSR7K8G^`xn9KtAx<dre_{K>3%F~9GHtk*jD'
        b'x8ImIn@XT0x;2}MbyW`aAa6OsTUrp<*Wv|Fm{&@&z92fL-qI%zQj(IK7Kdh#PtA*3Kaah9Q7xHc<wH6_#7OSlWR-(zvz9%02?avR'
        b'^Dspc8#4&aRhl!hK=hprqt%ctp1!b(8?)?!p-|bcTXx(`9zkuriOtunh$TAChSN6{5{K>hC!F`*3IYiB7P|-`F`Zy$(^*hr>rJ;}'
        b'Z3#OMv_Q=_Ek|jP+{`qz-VF3WBuptt<p1B4!55eQO&K&_{NI(qrArT#0ce69B{6K$Aje^mMth#R$qrnaFA<_~b8?8RHDW^YC0<O2'
        b'lxBT#9Q^Wy${P0cC5~9F^5g8OOHfQnOi>eAm;yZLsSE}(YYu77Vn4m4{{X$Uk-#leKnRdIQ$Yem*k9ra^S+m}V7#M<w0F@Wc;5G`'
        b'5-*1ECK}`4an9qY1W>}2UaX?N3bcBogAc}94&2p$eaZLorDRI?F5^0MNjTej27Bm|?UPIG06RzrlRLsV)XJ{CXy+F1`88(UT@GV<'
        b'4KLRamLKro^Bm`9G-57iK3jCrw&&7)ffL1%^MkP+?mJ-B>D8AaVMVkI!QcUx-RFd+N-pEP&sD<az_Vu{Y$*tXd?~!yUxFg|h7!jN'
        b'7;gJd!)?`xbPqH2jL6O!V7NI&ivfk4+$?WpL^XdN=FpWykWuqIj9K^n)N?<A%>%>QdOyQ{_zJ*i5t4Q`8*;eAj{@NW5b*n*LcW`Q'
        b'7?o^BVStKsMI*Za#@hZC3V#D%+JR04vjbXWTXo55P*@SMJ!(t2DA3hhNE)*hw#P34Q9)h0`&IK`C^$u|{gNv0S;0tWD-R#50Fh#5'
        b'!64jY29a%Ba%m$`bG?GoRo<TsTW7gsPs_7Aa_izHw?_kPZo5|}9N+txYsy7*Jg(sqHIWm4)7~8BOgtB#;$|P?Y>Dg_7yZNs9GmOS'
        b'*i`SQIfbg?Lq#h`w{T1VNc@l@a;_q0Q>n6_Wh*XaL$x|i$Agay#tdIFf{!MPBv1Yb24W5j2dlXxSnspY7^Pwz6Yp~PflB-!=mxa+'
        b'SM9?RjF<uK0AAy!HDmY8UZ!K|k7(ha!E!Ck#$Ss1k&vWfer`_FG%+|ymMb@bsxaNxe96*6HRic}8)>s$7ss_3e!vlZ$=*JHxIkeo'
        b'bgsL5k#E;2#UhZ?cKqPHED-kYPj&pK^C1I-`Mfz>t8+*ZW=rBFtC3F0O;YvImF>yshK~*ED5COH;jx^Q5Hug6=@3l<jm9<o^Im40'
        b'MExV$EUkowSUwkwbFJge3sy-8BT$4|qQ}N(M~WZJjubx&!)$O?h=2~O6)oj-MLAP*w7voi)R|C^Q^=@y-rp{_fp)F|I?b*;oK{>-'
        b'0~|LHTDihmO&3=qIfM=asRjyKQ1P^)cn#xh6;-|!ZUia|Dk{q9b!``00a~lbDkOo>)@{82IcUzMoHlkU)_r)fwS%cI7U{|r6+yZ<'
        b'$h6zmwzl4AZ8uS>;-IdzRn+b<IR1RGGBq#l79n{Fvt7P;<lBqZYTD<#SXrKzOpV)Xhb~4888C2EN#ENg$#rLKM=z3+?1+jYE!mF$'
        b'xL}<V+Vh3pcaa11atf_lO%M@HP|Sr$GMiz*V#;P=B+Inx!Ekx$f-yyFb%&e@+G0tFj>-qMsza9KL^gQwzF{lVT)LN;;%U8s4zMTD'
        b';@JmABp8&Xru-(xP>Sb+?Ffb!lPV)kj~V@;vZ)3Vf6V(KQ!K2vb*;Mq&5x{AE@6#<!(%OfMqUFb36RrnL2BGr686J)h54<S!vgmT'
        b'Iaea=4LSqlf}l3ifE9qr?ZSMn6{(7cQOV{oj1?p+<{-5JasdQRvB2aoXtqM6C(!+hNK!ot$^(){jlwqh0;mnhw>@?-qB(T;s|K}U'
        b'O$vc+96^2BRiaoC(l5TKCbI?1N&&Nw18BuGAtSrWRdo><#F`z_aav3i;@WjqJU=oPW^nos>M$+jp$r3=gM;=4SMTjHDgiO-W?v)A'
        b'qm8cBzKV^^j?GbJ$M0p%l9b$V58#zjrt$D^>#OO?Jf>2TTo@%QBq@E`Mf;~Z;KNnRNihy^F;S9Gmy*E2I;P{3B6e|^#DE$l3yoI|'
        b'bb;D(KLw>>&}fC0iOo0qLQNzZI_Nd{$n27f{?cqK2hZa?XXy>I4_|~FOdu>ve3;F-_|p~+V9JwWiLlz1%IanL$`j%0r(#?afKm<P'
        b'u``PSeD}hHv5wPW{ml#19MBTrTNlYm(x4<6R3gW~AHP>vI3_uP;Or@Nja@JhdNsi#2nH?9X$@w*+RU?GU9c0YgYlAoNY#WMR5QF$'
        b'5>wS?R2H70h^q9JhVL)1gBOGltCo(_lIA%|bCxA~EPWIBSe|<iteTD+H`v&VMFg6r*U;b?S_*DBww@<Ry;T+Qf8}bDN1LL-4}13('
        b'd*T9E4tor)feZJ8f_f6FMGrjN3NKghDJ3J#!cepR?fuaU_QPjD(eMPKN8ZeMYDSSbx7-~Cn=mwrRCk)#LXV+`RIwyx419iz_#OuC'
        b'xZT13LJV?WGGz?IKzvA&;Xi1Abt4y$#wyA4*vGK!s9zA~<EM;IZ!b1h)m7;l(Ohof+&!k<7n17&pXB=6;#>>QqfK(+OkR}BnP#99'
        b'aHU*|ii?#nDI#8>vLAlAKB6DhNEfkBUN|OV+8I!AP06CVqz>i=-;bM9j77@DM4md^urhWrH<y=8x`A=XzReA!ElQmvRo%t8Q#WsN'
        b'v*jOA@f6Xb*>sFx3(ou7jOmTT1SW}swri}c?fij)^hzN-Rrk8@PZyFY*JRW@H=B8D?OgV`3wG|YJ)bU3sD3RIlv6La2=jj3&MgaY'
        b'3%k3kyxtp@TOy1ty5Q$*b%*TQDK48Ja7t|KL+2@}ok*k-<OO@B)*YLkif&}5PnXuGZD$JT&94!X4Osfh<Y?%1Jx6bDBs!`v)^_25'
        b'9hCS8cCX@)4s>>ao#FLXHR7N69cJ#-ShKW#|8{2M_KMwfqvMfEcKW^O^eBdjE04`!v!DrB+34Ly)(ld{3%Y%t3K=r&Ok`rr5$Uws'
        b'!5M^aprk(Y0>>@1vl(3JoQxjT^I|tU6KOM@sO4RSn>F)?ujuB2&_kAP;P79)f?d_fK7vdu7@G`*b9`*pp13-xS?sc%k8Cg=K8Lmr'
        b'eO~v>F|n&w7-Kfmrns=8M8YOrNH58VXA>{*>~!!%Yn9|eU1}oHp~kZ9lpM|RtM|&8o!je~s`mjGvoPJOo1D6;_qP)rdK4ycqcD*l'
        b'KbRiNx6^a84>pec?A}2)2opdm$dl~3NTL*wq(~_y*pJSEzhNap82&6tk{f6Z`{;!OWJFjXHE|^5`sSRl$2cNxkoW*8#r|-fG|y%K'
        b'ao&yEI9DkZVK|rsWvGg1EUJW%sB!l1=NpB$<YJM9L)V|H8J?X9s9;h>%<N6zUrXK$+Z~VC9p;zBk~hMf;}H%X35zd``oXD5RVBuG'
        b'u?)k=4oPIXQ4%pR*qNZG7#(2z3XB2hDded<{J)HWT^NJ={IPaL2{M&=#aa$U#*ktBF3ng)Xt@R>60Bk{Oj-)iRBz3@$o4Ftd6ox!'
        b'K?bP8n)P59>x9?*;eWXATgLZut~dqDSXj_u7IOZ2AI2kI0Y<%A!5@AZmDezKbTiMx|EeD&$`NVCY-BV?lp{b8Ol?!KpbEjxwrx9a'
        b'9k;U|wXHZOxK&6q8q*cF&F7(`_5ZFM8Ql%nug}|z=hl2d*wg2(Y#^ocY#YvF-rbFwto;*<j{N+bzbp$dQFuxO9Hoi52kbQeLT#dV'
        b'6|-X};pxU2vd{VI&$~0+-db99Tko2E&YiwYb%3WP^g41}`g3U0WasQ&Hiw$ja!l9KQWZHm#?H>))6~e$Uz%tuJHO*7A?d;1yFheY'
        b'!sd^xm`ixh33Dw!5*_K7?Wyxc@u_9V#I?;k2Yo60r}XIO_O|Sn<=c;mZA;GkHCaufd$z^r4~jL_k^`Ts^0B6k_vU`C&pm%Y%&V<M'
        b'tFo78#Xq4>KgX-*stg2>rCqqk6)2F8##Sg5wql^wOlvJ;GoN=mGWmsX>&bJzS?BHQWvYezuo$aLvYfq+cJIa@c69j>)$@KVYd0Y|'
        b'fsH(R4;q{GBRYOu&m*c2kZ(f`@5gJ-Cw4X*DAF`dsQVgKM!sFNvM8QkDCHMN4q5@J<ad~CXU@5%p6BBqLi;xh9^#Q>X3$whHDBm>'
        b'+6wLwYXnlLIeYE?z}5WuzPrQ^-*=a4p6|Z@`ney$1ZovhV1}VcDi~l^G&RQqLx9=OF#sJX&|3f>BW|#wGB3k({Yr(^4$>|gY-ivh'
        b'P9Q%<Sd_#yhv5PF^RuBv3&0*jex2abkGp^DqxFJI?-Y{AFne#n9Wl)Qehz5Q`R}y%eu;`bKEQEwT`wS~v*G;2Ks0t>CFl^_@Hvj1'
        b'uJ1qBtFdyWGnZDT?Ik3euyX;lB6n#?+GIlF!YG1sOlF<uvd!ss-Z6=DB(t68I8ISlk{-)(B)s%}a;~@QeQ={dPIRj`wQF@uFB52c'
        b'Zlp4{Fh98|<KC0AJfR={FGL2z+^7a|790Zs#A|@oa54uQc}(Khh})hUSaVg(zH_dfn~NwyiZ!jD;AtE4Juz_Lh17g`W5!(7#4fiZ'
        b'$1*3}EH2x9*X0~=r_WU#CH(C4Mj6&DZgea`H(No9UE-EwI}#NQ@1JXDGwXv)!_IT<j!gIBw>63PEU95cm}?P9c4UNmfu*uHPoBDY'
        b'!J?&kn<o>N>EVDT-+mUy<R|@Njj<(E_Nh{m9&Q@A>q$lO(j9p#J?VOMfSM$jLenTI6vdAAHGQJAOb)xx;=P)zcFm%IRO6SXjC`uJ'
        b'aUd0xzTE?^d{nI^E{sv}_WZASHSN=!3%r4ttL%bUGCPdvmkeZ=s`|Pb+04!VML>@J>2pQfQ^7jp!)P5HH-MG|?4qs8P@^ML2s6qt'
        b'-ELdKIle60k`dNFelDBLUM{&CUg`!a@GQiaHcDQGhNJa(KabTfIR{YEm83~j9xDTFohh~oo;RnSnM@Vgj}c%ft@OD<XNB_wFwPWL'
        b'Sp5`~i;z1i$Yw68jAL`p`3Ym0;;w2d#uG+%_Br01sh@Su_V)pf%mm>81{P2ew~$$}(a6pPNdh#Mpvx99>7q2{MBv>@A;M81kOn%;'
        b'v*4j-d0C#AopH_|JA-A<`E7}QdkSjxFlkFahZfdwN=~u1k)6j!JgNW<Zf?bkNSS~~6*xSK0x{JzQw{pYiDqb!ve88{*4GPxm`Lim'
        b'f5LxIH=sa4<3I)wF#rLsZ@FItnB6IuGmu22jB;KEzZsH1&`cWQ%}RmUE091yzF4K;i$O9H!mAW~u|`4HKrh$*a{%}u!tWJ=x>@(p'
        b'*@(KS5Y)}OZw4Nyn~M7^f8y$+oS3eQZAzA~Uk&i=LN~ieSng$MWb^FoV!mXa{x4_UB^F+7X)Kv*FPZ6DG=L5S2?%F$k!WGlg#ok('
        b'O6=$6l>L%KTB1zG_78x*>>S`rNU*=$0!Bf9e?U70{T)GQB(OEEzkkAKB;!6lg%sek;9u}r@bCB>SLpZgSs>uEfQjgCgv|dN^}ToC'
        b'C-uGN?7yk+9RvSeeLLnyH2D5f_Q>xBe6<6de03(p<y!-%*7{FA?plC|p3=G;0}&f?O^KY{I$$S~*_Q_FW~s1@M8*DkpcnsyBy??m'
        b'8Ngb0A814*y8JGX{QGO!BflE(RSqOC4V+3pdB~N4;Gq*cmJLKs>=>~^=QFdOma|m=b~3vbz(zwwUzI4?iUDe?otVOwLY~ZJ91wJV'
        b'=DKGFc9co&X^HGp1NIVSdX(LpjzZNtP*`2^HD>oFL$YH!N`etk-iWrd+MXI{unnXa@Z#Ebb_OMPzdgLwO(pP)tD5C}aBN8K+`nCS'
        b'Zc|2d_g4D-odnpEdfPyIMr=0O+9{g*1GqxZg<1y{UIX2YB8946pDXPc;Tgo;zF%$T2}>fG{CDsiJR69#qlBdqN43r)BJuup1hS)7'
        b'66}J3>>uV5?3ZUb0{^zs&F0o6N}eTca|T%L0PpRb$MI)zyT-UtxsoUXXR5LUx0euedBDc4tAylzQa^3L?k(ZekD>mRkZ9d`tkmu`'
        b'uZSf)hsm;x*as`_{j6%B`w;vuONb37b#OPpDWa%=cJix-nik*X(DL+!Bq8r5Dg+;DvghzUkmF^svD0O$i|-th`BDZ(es<RtJwOsE'
        b'wNf%iw_>f>u94VF@y%-uHqn6lop3ffRc@|$WEPE%j=6xwRZk8Cyw0NSzJ&w&n`e`$4+Hj6k?ZY#6b8L@He0-6eX{GX{laJZJ7)u2'
        b'nq4`=&!y_WIcr~@GIB>``wj{%T0hnG{n<#Nf1LG`M*SCO{W+QXz5M|tI`(DcNC<LxQl$EVJTiU2_ubicZ=7p8sziVO?1PhDn!cq9'
        b'w_*Vf9re<5kz#w#>bLc`b9Aq=I6&z9oI(>ff$cfVvzh5cWND=2r7>ZB4vHpPouZm=>_Rlr`6}Y72<O)Vts0nGWIO@i)e6QF@LjD?'
        b';&~L+uB9Ob##1Dujmpo2j7U^l_`uvEe1HrlFnt8mAo3BgeIu9#!YQL5RsHP4AbC(IvOwYFXwXOjkff^={^qb3l6J=bR=9-`wF{i@'
        b'EuejWJPQ(}RS>2q`E)-dd)Y_f+0V{3PDe7uYZdu+oYfU5yaK?bVielq=)&0T8>6VCii$Y<iBYR|lU<>L0^s-8zeY2=m`0l_HH(l~'
        b'#yIkC&RsOR`vJNj<aZdy?A|G8hRcER-qfsEv_6ilJ`2RG<DA(<Q7rFB$mY^{yCaczOynF%fwm{9-I{E<WD@vb-f}dz5Wvz5Pw?I+'
        b'(R@sN*w%cO^WtFOk4(C&Uww9?nD4{6oXpzzUmgd*8#P6<kNoNEFTYs%&n<n)R5Rf!69iNOCHAh^ZU-`n>pw>D>ZR0&J4%TTJdEyI'
        b';k^~89v?is0F_woje!B@_sW}Q$^C85mBrsZ@<*T{8lGJ?0a`q3IZKgVv?Og3*Na!O$t&CK>|{{qzwG7Pbt}~zJH@jD<I)yUQGELt'
        b'6~8S?_iN-MS8tbd?caj$S-qX`Tpjb{MbO`}47r{^%i%?KG7haZ7z9%<p^{DHjwjknC6%R7c6K7qCavV=@*0fp=pVCv(btH70u~h~'
        b'o@^ISVKQj6Oqf0E7Dw+nzbBAYGEo_oLyBi3ml&H+c@F2Ia;aY<n`Kchm?cy^JlfeAC|<Mbtm=6z&_*{Cn#Tz{k*jKoJyA+X7Gq7|'
        b'*071t5Z;jtmD?SYP%9i$cp}&Cn4DGmf@{TDKRd;FlyN)q%lvx%XMNz7Th$>3Lkk2@{7Z-F@AZQN?^n+zO;ePn{E<KE^?&{E#b`{X'
        b'#;52Po@JOMt3jBRqzR82opPl=*ry~@Xj*IZg%D%EtOq9dmrgG`Bsy}e-`CdP^ut5Yb~HwLMAKd|N91OeB(bmeDe)wbOBk*-deMiP'
        b'8a?~let*gIkvBz04)^=s?bm$&kne1Nq=THdlhHa?5_4mJ!gJZoyJ*?q3uCAmo-VZPZ^~I{9YYG?%L`!|OY)ox3za|FWF$JiL1r%7'
        b')-Oou|2MimBv~A0tNH?djN_IvAJK(NaDl99T(9>bGrX+^h^|a3w~2s3Fd*@!??UX`{goOFhztn4eWM0QYzrc>^x3~uXBawcV`w+5'
        b'0Zkmvz|#yi-peB%`^A`2tS6&+e;W<$SBm+z4gFW!o+C|aGTP94vIb>FPw{@pkfsz;Y!s4HNz)`!Y=URfl<e#8*K8vsPmE!ezI?s0'
        b'zZ&$(LcG$qq#AgzV2o2f)Z`HdG_%m<lQnm}^O(U^`nvwMr~0p|^}Xs@M?UFC5y11a7RZ{3WOGv%nFjQ}XiU?l_?JCj&-X|6e3czm'
        b'1d}B0>pcF68UIA57U^0<AWWYmogd*~f*AFp7LKVf;KqOm%@2Qs`*!xX1ekU&HgY+{{%3!eEWj<KCi{I$%C3eiqJLm$dOvnDnnx`H'
        b'5BfIZ?Q|TH;5(z~{aB(SWem-gLtm!j**<o8f3~uc$jdfdk4@n?7`hqM6!5&64AJmcjDH_KBn_&Ei0LHH=2GI#&**IT`uyJ2M+<lj'
        b'idVEdmh?K7U3DzI?#OTYEePBtZuYV3Z2nbtX)n9%DazT&xDR8_-_p*v6~nbm`#a&*PTCt}+|A*NW`#3Id*5c7G^9)4@0;Hr05?N6'
        b'H?Vg45l{bBR{H^dUAySWy8Z*w9!Y<@Fl$JfqDOiNsKUQ5@2GVDB*OE<Xk}jBVAKKMv8b|_so)C%c7~somHmQp`?1P>xU-t6sJO8?'
        b'Dz0H-KPU(H#FPrq0D>CfR;FxTlkV#5Yl!XV*NQ;lI4c$0#1#KKNQYFQGlEkJK|Z95o5>NEh>h;|$EHa7F|=#~Nba35zi*c1tuR{J'
        b'(1_NzrWv9DuN`lqb^80BM0ri{@&%6{aYy>ZaxRne8bO(|fnG3?I3lr}lPkq$GI|y|fbPY<`ZPr)9#>JZ8hnRJQ=HGx4;<DcBiOI|'
        b'c+M8=L;G}wdL#QaI^G?vRO6aG3U5}c+l$-1n679OJzD`rrLDi$T7<$0c1Py^1j2G~6bzbdu&es`lE*rlMtzg}D-7VI)6fX;fSW`F'
        b'xW9acP1SeDuEs}xukg-p)m3gsJ7wB>D=I{EwL&+St`LlX{oqx;HmdLF;~crX+GbZ{`qO>((#ItAqaXlU`_f~}ITeS;@rRwrd^W{_'
        b'z+Fn}BK{(B8s;+<A{6?&%BbmzN~Wd{Z2W8EK9fQ4!%)nw`hMK6`lq<xxF7aY*l*nHx*ztd7Q%kj_rreG_rre3SIZuc{J|&xAN;U}'
        b'zW?rrt?d0bKWt0izxrXet$h(!j1*_{nx$zagicp{oz?c7>1%tu&v&eEE^ZtSp`pEjOU!_`h_s?v*^v`{peIPv45J@h^(C(7dW9Ly'
        b'8P<6rBPoMXI`Y@PP0<D<$i)06lOAKxTq4&-LwT1YQdo})t7V(;8K7W}yxT`7%G9P5wOCjiW?DikWS~x5g{Ux^kW30Otc=7TQ;JPT'
        b'4)m!_lhn8#+JF%<kntEMLo<_0P+@=ukZGk1Bx!GZO&beMO+H3g{xmi+dt4TRTpXEpw=PNY#dka&XFu#jtJ6(!;2b22g<Ya5UXf_`'
        b'W4@X`>o@@>HVxv<MAHb-5x!TZ7waqg*e`nnY79Y(eMplA&^%|pJ0j_0E{M8F$So@(B>xP98JbHGcE^kb;!0Nc6yf;?XaaVq2mB8%'
        b'c6Z}hoJkQ?aJp8(=|j90Js+f($}DpIt%nrP@ux2WQ34naIPx*(>tPudVDr6?#OeI4fMoBBn<^L22N9DM8wZ8C^u^!=pfj`eeXg&1'
        b'g$b8=jqH58K*brfvqA)f4Bjs?a?b)STM;Glh?f5hWHc;fpw#mb2RM>?U;_&&j-3e(Fk=;Q-~bl@&C*uL1P9m(WcY|z$N?%AGGB&g'
        b'6hmBrf@eU;K*A_0BKXYcDA^3*8F|PH+^oskDg+RN$f31e?rr7J1idwqJkZmMR(w1vggNILKU1`}3m)=7FIw~wq?sVY#`X#3QM+wz'
        b'laJtt`F=-kFxK<Cd+hd}W-@Zelkb~emk;5k<2Uyj+1%8LglG4?BfsnQ?dok>^N?o;a-Ga9I)=-Ae_q=t%xgQlMS;Vk!1vdN(8RX+'
        b'@ZD|>Efp}rGq8V9VXOcYF*Q|?(Os>0?gohD;$l&2xdJkZIi^IwTCo+am;$U73s$?+D7X!|sE0<>y+<PZ^6Vf47Q=^()hNUaa>u8{'
        b'AqRNh42Ua4U;%;|*uP#>ybC4kImXn`3!(r$dqrkI)*)~Y7?PZ0d_!Sc(PLLHgjbmHYsfSjZ=5K}Z5EB#Lf>9wm-Hkrp^`Yx?CM9z'
        b'd0VUB*qfnEC(Wy{l}W*pgQSH(NBCu%3pa%in*FTK68|0c<ZQb`C%G5yRWG8FySuB7iJL{1XykYu_*}J0IKmUZ>sr^VFYisiov|<2'
        b'%O>`s>s4Y!)!+hqztxP24(#K+rD;io<xz~y?J;wY)qOH7Li@}1nW2sy-(qeqLG|~sMs^;jSZhX6ocdu=O8^jL82*Scc8h8*!*~p%'
        b'qtW>8j~F1JngEOix=QpTroKW{Qwd`Msfv%7=dQzl7!e>}7?k3V80NuPpuJr{f@UCMKzIodaW49(k<B)K#F)X6OH~+!D@)DqpdbxU'
        b'a3smG51T<0+Z8AlE&wssi@3MKD1@^MK`>44t^Wv-sa5!-gniU>vl~8yXJaZ9U|K#Fq0QdML8LzlBHHN`p`iyL>^!$46V!(lm<pY|'
        b'2NfBaVG&4?c6I@98poR4EDt4HTSW{b0!%bIW}1bSGN4)9>?7?CJ?F?awu+$3^+pk}U+TP!hL~PzYV93L-q`s`{a-h=)K?8ImLF~T'
        b'<EG$+BS(7B?KqP}^*cnW#gkp1cVACesUD4SE7l5Y!T{Yh7p`qn)W1$Uw=gvy4ewDvZvE>_%|_=Iy8C@dG0)wBx2+xp6bJxjkJ2r#'
        b'p<C+QARD&O-anxt$Sr=I2D7K$jfy#6R|MV(LrLf=l&m<aKr3{%0P6KnxOj`A@vU&AMi>mR-mD)e8qW8C4Ofrc@k}UV+@fgkb%RNF'
        b'zt~(Il<Dq4w}>2N0=BgX#SdZAwmO|vdu3qpfuRTH-h1g3qB2kEx9EHjZ}>qszhP=FwR}$lRn>gdeVJ()qJf@TyO^36TY`wOD{7eM'
        b'?zU9Zh=$fMEzc|Lhp$)*>52jd?FTNPfpm-unR=iJ5Pm6iJ39k;aKOV$$C=#T9PWj2MNF=*ScaIqc%cHsUgT{Fn{D#;Sl>ka4CayP'
        b'nQp|Z@ah2K<P#-?Bs=We+cUpCFO>E>1^ZMt$GxO-V`y@Kz(60MJESHO9W%mgVYkoH!*MkAD!gfOh&nRDexZ{e3Z1;@jdb!u=%n{S'
        b'CtvVB=w!$%bkcwL3iQ)kPNRvULdK6~iN-tWKm4*c7xl0nR96ZEmZ<YN6pn!IA%O={>Zx%#2VI4ZJ?N)xO%IZ7Zz@cDHzeE9t}&sL'
        b'Z!1hCJ-zH)Na~Iu6o5Bz#MHekx&`e`zrp-$)1EkY=T+yO?R9@NP3bnLyi|uS-lLjUlC~8+l*qiWmJ+Wt*mI&+D#1fH=X_b$<o9Fd'
        b'oH$oX4~hne%sH86Ws3bB%$iHv)e7_Sls#pXs3_i?qcfL2w7AbKmX;j;M{zD~UMMx)I76k`Q<j3-tJ`0~PA@7f@vbh4e|omPAGeE*'
        b'QDvHv6f0GRRw{oQ0=u>Z9Kp4liVGDb$`m)q<#Kdtg?%|XfZTPl+g|jLsu~M;S2xQ?PLPFH#YblM_{lg;hAg-W2yy;(41>CMjBtUr'
        b'=co^x(qwyHuubnl=d`0>#uU{2x>d)-)Q1{y7(y|Wtn53vZRm`j%(QDJ4~wy6nd_VG$Z5p?h5kFPow27T)O{N8;#8DhEo0u_1f^^}'
        b'XZ+qVyZD1j@2Is<WZl1M<X3{jev+=M<WiPaR}!8-j-}6`(D~<*y-1k<p2Ix0YgE2x=Qn6y4bEQgRui+>={*dV6j@5dpmP|Jx7{)Q'
        b'M#u2?L8WKLkCymb=)Of`6(!vqXKL8pt<zPtM_aR~+0^1=(q1nv-?dG?<4JDE@~OiI6^Go1n$UJ28MbYL07|BmiMGixd<nL#FPK;u'
        b'Jxawg={jI2bS68F?<LryXMX9s&gHS2x)-|w#0P9@&&mdlz@F}@WSRHfF}*BHCD$KhfcJ%aWAJn{o-tgecqT)MN0Yd8J%J6sqEMQs'
        b'jL)}bkR~~nkW@-wBu+h3ip@z{E`dk+)=iiuDF-cRpfY}NJ80~cq`xI7Flh+e6vA{Nj0j<D2%|$4zGCY7-?a1D$}?6X<iwsus920K'
        b'0!}<eOovvZE2vluZ9h=a#Isb0l6r6q($qX^qca^4*msQlTLOM8I+;4@YjmitJK}OovCB=0Qj>DMDV|}fT+7Y~C(^2}vvE0i>~dUD'
        b'iYwRS@d;Onjz>{zmG}hOnl#*`@cNv~^F?V_3C{vBn<)~XfSHqAbGwIg75ToLd{IF90bmCzp_0K!1q1<5)z<Hz`n_Z_RsR9HiL=rx'
        b'b?H%s)o#Kw6AbDJYFy6XGPFw6<|G$lQCA7ecs>RBF0Pw>{7k-y<MIGD)IjE9R5AcUWc0^y1O?I5RTx~$UyzFlUDr};Ev@JoEj?o~'
        b'v~`B2%;P%+KMFJWvywlDAxWL2&P(1yo4S@D7y+OP54y7pz1m9cv>b-#ipYkXzlO0DA*jG8Y?_g@hcQdY(;CkHoRnZn5)<YV3CZa&'
        b'hKD@CFvrr_Kad1^GhS;KdLs#j5skGAxA6JfbY@4KYYM^zbf>9-G~>z7op<Ka$?48q=7^-*YyvduDAD4Evg0vrU!7LtaqdC9SNaB('
        b'$5^YHMSG<iwxr2xHy1F&d5V%YUH*IdIZ6>W=@2Q$=veLMA#@lGisdZ97F@%UE|Qc2ydKgNH?mnr;&H-K8m&IQ`xwrXnNSmH!g$jZ'
        b'%?wii=@}~5oFn6M<eF6zIPdDR857D@qRT4%Y6WwMR&9+!SB9z;Y~Se>t7UF3*7x&n3SHH`X0^-=sVBOr7eRdbxryjlwY)07jq&C('
        b'i^Rgq<=vn;M3?{}R<#;;S&>v3xkpmyGA^{GuTNNC!zp}kpP`WYDVsiliiP%AZiO*T^KHvu<h<tw|7l9<pV+hG83m9r<1A)sY3FUD'
        b'(^>59oI0(x1>H=Yo>-eMH|Wwg3Fkh$Fxzj=*u_>=L6T};yw#bKx{<Ivj#1J^FDc)J#6{rHK6Dzj9CIXgqqAUD!iq*Ty7;8px{2?l'
        b'pG!?AJd3a#0#lPPzBnUFG7to5!a;zc&4MNZ?P4(`8BC->gy}>=tne|6Q70W$9AHV4L~X*9CXvA;cD;96@Ku4<MOJOd7@H3z^hz`C'
        b'YB?<|c9JM@3~hqK^9{I|G!q6hhL&K8@W=wnj-{yn087wx(g6iPR+=!E4}A(`XAnNs0ZbOb#9XgOUJyAEm~r_CzL@}`Q$q7aL<FWM'
        b'AC(EP<iEnK8;7ZePxH~INA(9-1k)3Ffg6MuMr8yh4o#(Ud=H=AOK#Y*KyJt?nC&p1CS_^XIU!-yaO&_Tg)`uEzT#BMF;Xg0OA-Gd'
        b'xu?GrS%!?ML+T}%|K#xGYX*_XC<I)AqyIM~mYo)Scmat*;{q)1XGw&{pO2#vbs1<~ly7N9ye<+)bc&=c3~fKkLRbAPKHgW`cwf;s'
        b'^H7)W<8R40{?x(?K&<3&m=sAOpe)D35771#tVjOGSd8N>dmL{M#zJxg-G9*VeV6NRr~Mc3s}p;U-0bR=&7)p1eou2!t6BC2FQusb'
        b'?rxFw;gEG&$hsudCEHM^mmk`1&%>0Vx=}1Hw12tG_Nz0)A;qe&@*#|jPQ!57p3D3DA0qRT)p?A&^Iqd;!-x-xv5-11napD>p>VMx'
        b'1h19wd@CGS%LLXYqtgr`_eY%ULKm>d_W*a9T2E({Po);F>+Yh+Ux?)eE9_!^_4LZsiRMr4$;%5ngj)b8OXXQyUcSbzcSpUkrf8na'
        b'd72cbSrbEb`x=VQ413UB5lSg0#G_Nl+{8#&zlqTKS5F5x_D_ckZ{F?r7S->1ugfY8sg{p6EJh#ht_3X)?M7E=U~}4V)1K4jILz!|'
        b'>r#-|5cayN*}tA{#vOaQ>_pSZe3Aok+7G5)a*7cJ;gZ>lr_C(O5t)k{IMWpN52$l5NvK@T!B}HMRH8h0I7PuUII%b*cEIO<I<b*e'
        b'FS>wcd5;`CO-7|P$|s}bZ?T5oc3Cq*5hZNdf;Fhm2uW>wo0Zw)MAu#XrV9joV@8tOF<oiO9FE4c4F^AKaCM<+4^(uTo1L!2Gm&CB'
        b'6ISC)W1AIY^0gTtIn*X*{8$}2be&}}kx?gHDbL*4e%--Vo)|8C{72V+c2Ti_9bs;V@ccDwcBHB{iAYJ=k@nN$3+eyZB`9?kD8D5`'
        b'q1`}6J%r&}rKJ49p*>2;nh4Xwvo=*pP@oMkW;f?Z<y60~^sZ(yMJ3)cX3eH+1&T=pC60^|mbE)lD6!qa*&P~tM>^>2>EJo09eLuk'
        b'zs;yw83Qcm%j;^FzR@u2G$n?rOT41%tXf`<NsQMj8lu*$qonSqrw7`sFr?16oTLm}Ge~$$SSm+AyRWwyw;qNcG9TM|7~TcibWkXu'
        b'#Uh7s12!8S)7l+cz^Q9Zmk^H21e8LL+-UXEw02gDR)!`4pkn85oo*@SEMOWxyI1)8TdtfgclwMy*)XQ?HPg-jY-Gd<FrfC16wJ>u'
        b'Wh&h|$?0SGK^*#HUnDO(Mo@X~MY5*<qBMV@+QMDe*|bow-NBS|gyc!g71!lYM=H*5o9nHw@*b!vk0UHBwoO)^5><0sSF7{Z(#N7L'
        b'Q-Pk3>^g0ghb$YyM|PaP-ev_J*8UM_#<L!s<L*$GI8r>#;c@{D0YJlBmSe)&_&nzUX2aH*pygMj5ARg8x9N6&j4&j}>i_6G@?B6J'
        b'je$g9$Y)`2q3`fD(BFb<$kGrRP=A!(CUd^XR2-+NNz_Bsgx0&;jh8lcpP@hgw*HXLyN~uexMh-$lT4jmZZ=J~i{6@>m(om{9h#aO'
        b'x?EjF6-}koFWKI3A$UyGn2`e52XY2Pw>vm$aiFc3np`u6?vTmod|1Bggm~(X70HNfCmOLXU+ZaIYXMz<ru90@QPS4mZg)Glz^Qw#'
        b'=B`GTv**d*zR=Dx*I7+%W+R*G{B5h#RlNCN68o2+FaI>h#Zq@c_q!G&VX1kMw1`3Z_fW1sz#wFx3%k=5*EZ67zG?^r%M&u%GZa2='
        b'*Rd!dkYNhwe%g^oPx~|YvJWLxl16*m>YP=$^GnHOK<SD#a(hOsk3SvoqWj>MidRI%*nC0XjMH{aY``0Ze3?H4Df!wT{a#{Nf=E-c'
        b'8uM!eQ)VrgGTFt4z?)Wk-=w|Xs=7lZ=qssj%4sO;*w6(nD@lzlEWcsbD10?tV84j5G9P8z5_D_`7X9c~b%SVtJQ!-vQjFr(sZKlE'
        b'y5x4(3qk9eO?DP2A>Hj@C<}<ug8x`2I}M!j!bUO*=rn!Z#vt&hzs<UJHxpoBpc~VYD!n*5`lZ@eQBeg9BHZWz+yHE`)pfAbwK`}`'
        b'M*?R9Cabw!u~Ao1KwGU<N}R#ye5Hvg+;C?PX)1y4np0AmC192<lb9WxqcCW|8Ea}}f2dsbYXF&2(itwyKC9X%2B|VFqs6RX&B1)m'
        b'v@{4(%NiHiGWdw&XVAnY=F}8w8kK;(f4rFlnD7CV8D6Yt^K|8#Xhh*w-9CoQjnn)rth%_5gW_`G&gp<KtFPG^)~9r#WpFt%5FZ?A'
        b'Wo9y5j+Kh_yfQ|`S^~ftX<wm(&H?$<>k@Co9y~^{f9a}wRhaQl4E}W2hb=M4=&IcDJ!UVqW9<u2bJIhH_q6N$-mvx0%r=suhGfB='
        b'joz^xyPuja^+aP)YqjT+G}Css>{6f`j0jR5D~MXTG8!l43SpJGlp?4&i5P39CIy`?Q{WV1`92)=1vQD&=}m<>;byXfz|d};H+&<v'
        b'!m4M+1ZVLq?ibIqNrGOl$gNQw6K*Ndr2D<t{zP=$vT*NsmF^Jz@z()O3Z<l^RNP*2^XoD5Ul1;UM@J>-s<uV%CvVhAmy!Fo|81Nu'
        b'YeD!h`!{KLO$3u9rjG)K<<*Ot3ACUs(TUao7Xxr~hh^I@yN*<KHH$P^;ldB^WnQ$LAHSdKMl-R$bhYlFX?)SJNR=;kwFMi!A|Pu%'
        b'QB-e0H(m2ZBG-!uzxw`D<y(`F$=qt%*A|Q{)haWRsu1p4kCKHK$6PCsoc0xV@#<J=8Z-qJd4!yNO@HN->#ZQK&g&`c0<VrrzJDhq'
        b'I!XC+p*;<UPBmV@{m}>9(FeV?j6ZsRWAvNwP+!Y5><K!ZRsLwJdocwv*1gzz|IXdLr+gslGu8t2z>EDmQ(O%}zjSxnZgJzpo;Cj!'
        b'-w1XTkv4IHTWWP~q3df~sfo^v?UDPJyr&vwcQvj}aveR@Fbf{?8VvBeSoqCv;Nf@C{kx7DbX}BeTXevixZ%~f&gir~@@r^P8|`XH'
        b'pL}i7p;NmkLNXemOIKQ#Pt#Q^<??Y=I`-3jPCllq=C(T@cTI(tb%_t|Q+5+k)oTe$Dm+Mi30=w2?tE<X2SkS!Yl!da?o^!o;HX^n'
        b'O?2wU(wnu*<+Xr__tO9K<OjWSF_j+N8<2~FOWZ^>5GA#wrMA?aPf*i>+fMFkj}}pLTR+(JAxA|YlTG8MeYE+5%yvRNX_s?Q(N0LZ'
        b'gG~Dqxa3Y4E3a*#2ri$HkjM`sqNzjx!mT3MAA{*cU95255!65}t{1=`lTpzK*p=Pw?UZcNE`VaW8?Lzy{q<ZANA6u?{~n~sbb`0x'
        b'%ZR6lk7K)e1!HI(HYgll1Sx_){^c_U^un*k(K$OOYsu8arK-P++?``i?I!o}FSCB1<yPP|Us$aoT`g^`Wor72M$xrg1*D9SdY2I<'
        b'nRLP`DJN6qtc5>?lVc`dTOdXEvo4c)z6(DkvwRyF6a6Pauo?5nw`X<FQWy=bK;_UF{`kGE26N}VT2fVnMQ-JTrY+k3eS|(f2pWx5'
        b'JEi3r8Lsz(JEfE~HDf{d7BFgC8;%6gfdpG>^U$@C!tF!bWF1k^_wn}!|HpeOQT4*z$ZenidmE7)O%a>tQr$Zhu06rswL7Kt!tH!>'
        b'd{{F%GK$U%G8%6b7gueQ1+^4E`C6k)LM_Xb)i-Ziqy7G(FL^2Gl`XDbN3<*Y6k@shAZLndlwrnn)1(gq`50%4_Pr8hUkUEQsUS5G'
        b'8K@=^Z<3l#vdR+7b?+p)m&$d%p?v*R%HC@db0*0VXRzIi(>_LXEzEndrB}V`?dS?~)xa%YDx%z~?J`~}etSI><xFBIL9@)Y97X;@'
        b'FwG|!j2lgrX1Uo+P2<2pC>-;A6Xv9nYjcnYtK(msqcfOz(}dRz)GLr-Hc5Dsn7WbmC!*s-xWq)g?O%oiVc-+8ctSE1X7nZ`{AN2#'
        b'lvuH@DyoDi&NlJ6F_XASxg9@-7vMn&rMhMwubV@4=fs$E9-3x|)Ex{%3!(bDt1qT9YW4{Z+6=XLI>Ogd6;E)0-N>DwRx+d?It7}~'
        b'`gjPf^-(5Sd9Af1MC<awTGN@ev?SkJ7Q#&V#e|j?qfD9<ent7hg?s?x=z8~?Sj$d&^F%SwP}!ldONT}zRr?qce%}+SRU#A^{f-Fc'
        b'3n33|L`>AZF!Czlxr4X`(Z@(UF&IiO<zgj^N)l_8PG?+sB0cgmvhL7<($3}ShXN$J&6s`S6c>vXy6<w{G0ArzGhO($D9)jJi9{Tb'
        b'UBx??VP0W&C^^R@Gt11=AT68%ZhfM*fE0tlo4BRT>3p6vfuoX8;-FnJB(+V-Q+`LRpG`6@(LE(cF)9(tc1<{Su*dnT&h3bIv&v=i'
        b'd9??mZU^fcMSW{$V~519yQhT3w@SYwSzB-b`3V8XWY-Op+u1WDa{cp^FmJ5#JEqLbK0pQ>Q(fOhzE19CCzr4~*Ei!O4t}mpKR|r&'
        b'gKGq3^s-ai*(t6s1wfxqmo1Q=|H0432G}^)Fv?pddrE$wC&0#c5ksWw63Xh54au8D$HcCI`voE&2qpR=fX@GbKnWkZPCxjFI7Yfo'
        b'3MtW$xXCcn)p<(TCHFTKA$bvFKRyNig_RiJh30t?lc#>%ixDTsR|$N83b+0FRL`GJMV_b2{A^6i!;I_Qf2*MdrCfmsXg(ok{})fP'
        b'NhdjOv5FU)-@pRwWTS!cv&sC57}tSQ!v2h@euvZ#Xm~^Ts6k(Q>UP^zmhJ?e4FJwr)m+8X=+IM8+Z9@cKOu&14udJd9Af+{Vw5<|'
        b'4tz%AG9@t{>gmWuu{N+L(SbOYnXL7c8jlf<1kpm_W3mT#Ah{?c8k)vtShXRn<ZIP?6S#z!6(we#O@NUyv&vz$LYu8kQIZ(Y7k~H)'
        b'h9?08V@rs{V<PZ1=`+ECMX?S{3m@w^np}i&D`K!Y7Y}@Hd^cn;(XM}fCR`{M!+S*>J4tTHiq!$lX2oft5~#u6Mr#*pi-7c$VvI?5'
        b'LRA5lhN@5tzZAY*jTIX1v6ntmLO+NQTX2fTS3!r^uFrI=7WIslv8q$cNGhI=1s_r!Ik*fhf5Q`z<77%$^O^?mcr2>vco>;$dh;ph'
        b'f>jxslnTR*r5^XZ5}q#U*c8U7z@h-*u>lLIC*`{4pAwo*``MI$L*dFE=ZIc5&hJPJI41g8I>0Jivrh?XVXwTMozTn11N#NoiEf9c'
        b'(UIz!5g~jHI6?xANRLIk(gYgGK)+zlj{_7wB28&7?mo269swAtVjS3{{{>ilq>ZrwM;wW#A*96!bkq}Y#NP*<3}ok$3AM^k2}}9e'
        b'&YpvW0DcM(Am<gi2;nsuse#)|9F%U@lJ159<I)nRxLGDG5gMo*b}P2N6=<Wkz6x%9B;o^3{eo+LR(ULHq&W-%D=mqTycwQUAn}L6'
        b'w~4{T7j-#Igj}F|W!*ENnSRFvNH%>tLyae)<C<c%20THHPk;i9674~E4I$cuOehTb7zwnS6zL^{uR^^%d-8rS(JgEkioYjQ#y_E{'
        b'2-ic1Y+OAj8zy~b%?nv4hQOIJ;xgA$C&6io>|3`=L(3&tDS@d)SdJJo4up)KhK$1@<DWuCe`vW$Qfi7)nv`mjD90p5q4n3pY6-qw'
        b'gzppMIRuWv?DK^3?IB}-$oOH%crc_k$qc60?I!6yQ*@3=j+DaA@Nyh0#Zh@Bt~B7Wz$?p5RH<nKC8do?4F^wJSB8w@XE)H6L6qTo'
        b'<D|7HWEBZ#eHk#w0j+^U{W&JuV8YZUylh7pfaTz{DhYRGoW$sm5HJ$<;&+56U!#q(hUF*Eue0t7)#qwE9Y<{kOvW!mTRsOMLWdO4'
        b'Mu67zn=k;ez7RTpq|+B*qy4NDimf+2q}diOMUym&2GdEVP-Z<CvhEH+%e}9yT8}@}P;;{Ob9!ZHJDMhn(>*Q2c7&j30LuIORrJ%L'
        b';sO~u223n;;A9wymaGsa3T=zB91pv`?!;^%>)KH9<N2<TFg8L@EuV(ZuN!abNa$Z1y4)0_c?ED7Gv3gn4XB+XsGUu2XeR|tawVLs'
        b'u*eW@4}`GoA@A>2S+|Cu{Vv-{dNDL~0yNYK4Q)gX1yJJ+&6PnzBGW#Wruz*QhdTCxzHP%u5qb1+U(aWxN#ttpM6;u{oiB;<{&djy'
        b'v<)2XsMTUJDvC6T9q!Jj9SP$piD}MBGD<2q&00!?1n{Rblu;s*BqH(tgX@ITe1JwtliXE?;7(c%!t$ukxGyv^0IY##3>aEVMv2D9'
        b'^l@zMeliMIlEk!fkn8#7rm{}!tdKCZm1ItnN3E7BadELCq%?^WR!h~mq?iLrlo)U^JeyW^GD;aLkIP7tl#G(-kUKw7jY|!<l;)Cj'
        b'I;}Afg4$hMP-_mZF~`P$SDDM0?J=e$og^N0KLkK@@W|gRptm%b4?8Og6!LP_oC#zUVZcQ@-$!$0q)Z(Z9rd)>5GB%KNerFO1W;F%'
        b'CQS2OSoMOetc_63lQqW1)coDKi*B^XG!i1eA2aS^8qK1{SlSB@cDfPz^fcjNF%l<~xbzrWM2=X17+DimX(c<~Pk0(d^$>S`OaxzW'
        b'ok8s`+zkL?s3ZXdf?Hp|8i1y%2u}(|lGrf<fxwzd!^n7FCh_>f!UU*DjYl0LK%@vmLNqzTg}Z;4e9iR%0;<yfXt@_w!}#HtGAbHc'
        b'LgcG)u}~DXjuEDX%6=X$)cz<z4iS`t(oocZOK4)%c%@KMCzKp{B3$^)4G%h@(#=MbQKY*Q#}d)tquD#k?TBuA4@iJQB)}jN0O=Ds'
        b'bOWdmungG6$RuT?Hw=pNU`>T#)z>!wcmC$E>&gl5E?NmAwu=Fo0H_oK8bAgjng9VSKSsdk0xC7j!-ZdeA^9}oGr4198V`Ph7RbCA'
        b'2R=AS&UD*j-0Fp-8FQCJyZ&+l#Hw%=_B_51Pg|Sm`rC=N|M<+Eo{#Rx753J_!^pC*>p6rqw6sY}tLy|tcmUU~1Dyfs2dY;`UFT2q'
        b'*x{=@Dp|Ops&Lgk>iXnsBUW5BZ!}ZZv`jWqFE1;TTfkm-U>Ufps8cYmqeu1<2XIPW))euteb`)Aacvbi3s2*}Wam1ztmETisEPFk'
        b'rnva|N;ZyvJZ5+fI&>~d{9pnXT<o3IKnCR#3CVPfG?7PL$y77Qb(!mx6T)PY?3jqm!J5TQrm*TmX{}?pTrs>;QM+#UYr9PF0RL>y'
        b'tf^%`-WUNZScz2tvGMJryBkRpzN-OE7~^<jT#WGU*;<xLlGkow5k)>8Q<$D`z=f7(xYnZj^d+4XVJ5M(-^n===e@X&)1j$OMkEoT'
        b'Q+9H&W1?p9NH(IEh${gEC{~(CNl#dKiMGhh2^XHcB^+C<#&Km73EcdD7<(76rmk#p{N$XI2gy+rz<{8g<b*)9&;hi9*4~jv0Uzx^'
        b')QC<yBher_?OaQ3wT``$gcc&DGZ<TW)XtofHWjIiB+45UP=i{Ws%>rSv{PzLwe~TzTD1t|x7JCp&dmM(|NDLUPWE%{wbx#I?X}l_'
        b'!T1my-T))}fpP3*%O_JJ5j0@1cC!QO3nR|g^J<*SK8)*IHqfvR2zw+<UHPMvrkQ)HJsCq?$=g3^Zl;IdQl05ga$TB+b>3{cw(-RB'
        b'k33)U_^d2VU*Wl(86SFv>XNIg>ESxnnG4G5*EG&-+V)=qz_$6(!2wAYI-&7-z$u+pb<!0l>6<%H+lY43Fv97&K#8atXA~|#;^qlT'
        b'BbeWI>ISGV3dEID8VxvCb2N}t5Ewy93U${f1k|g)b?mIl1IX%mSI)(e{c&P1O+y(LZ<s0Oa=8cSvUB+fXIPke!zH^`0wjQTv}@`5'
        b'8hpE42Gl_1C691Ci49#)UxV98!iZp?UK=ot4CQb*_af$rQpS9l1!O4|&CsO-<Eb3EX-=7~8C&u>>OmTK)cq9sggm!i%;=J+8N&tN'
        b'`%<UYSFD|q5<AfM%869nVrWjZ*JWH9*!h)@5i@xU=V+K%g=45e)#$>7>9DvR8H8w7T}p=*hmA+>>yJy?cioZU)KXq8IS`}3hYsK3'
        b'xfL21eViwUGLMa#uH4RuJ&{RAW@aU3hz7R2|9eLAoWvfNT2*^O1f4Q?PXa!B96@jY5Ck_mm(c|u`<yD$uFt7{on~U|RH#1cbJ5rc'
        b'lTia%9#63PaDL4RVTE2VA{hm%&uLPCr|LX2iH%D+E$x|frb#2bojqIa9R^2EU%(lcqW<Wny@<ALM7lU#L`^;EyAW`4l$R5`sQgW@'
        b'?y9LIbIxPRz9&vFFE&Z*Qrw3bM@DVRX?c(AIXN?<Nd}xzD}tF$ex=GaZSu}92dW#D)<%s(<SLw;b0W|#Y9gTwy)@v+P|Lq$!f|`('
        b'S|wjI!0MIOb^$3D;r;<+%4J*LfN*CXVaq{BLj7e-tW)BX7&8c`Zk9`TZ{1P5F3G7&G^qByTlcwr?UdY$3aq~71RxE-7}BWE0dY$P'
        b'%NY_A{(p)R)RT;HDW8x)2#CQjjY5Bo@c&v=@RX08x_gV6^nXMFaRieZ8df9d<P^GmYXG4{(2T*#qP>+}MoTV-)?_n&J<vnhX`;%2'
        b'{k@5_M2M2)>X?9?mT%t&q8V*+8hf@}KSyEtFNHr`fsetVy(@n}W4-Q-m{KuKjD2kh>7oeJViCJ+ia+9(YnB+qih4DnX{If|3JdL('
        b'c#zaA+^n5^!pIRuBm6`KIe_-rm1c!@!GM`$Ov}aU-Lj%3K1!?-HcI@KF+QVwu=ITqE1h5TurJMA%AO}#GTP*nxZ<OLb@r)jV*^1W'
        b'w|ceMb`IVAI|FQdxL0_ugXIEP_WI}dJxH6$d`7WmEsh!H%zS;+I77NGh>8k)rukDc<C7sNqflQT6&4tL-wBIl*Kl-oakS;DF#FWq'
        b'+C@Gqt2AYb_?Q8EywWR}*ZK1U!1DSm!e16v72~FFx#I6Zp5``JEp~B)TY5`<jBcXb+sBjS57I8_d~>{-Q2?V2NeI)sHvzaU0kLNF'
        b'k7S%2SjZ}Kon-mFgq{ZUGG_TQ<C4{ft}(HUSktl#&FTb^@||z{_jZc0vdMNTA270Y4zOAIOWL7pJAv=&MAiE=_9AgzMn{qU>G9f('
        b'B)OxYz39O()5y(OM_cWMBpPk@#2%yV&ps%*crne$EuVw|4Sd3er;jfQjWSL9fp7aYXqFy&&Ftjl<T=cZCJHELp~l^5BG30e{)W&0'
        b'KTJ739If>qcd^(YwmPhg_N0#`+Y_MIoem_P%Q+q5HQOr#Oqero@}O%0xpU_Ln>Q&5SYzi)1AU1D%&WaFm!gh)J!7a+)#w;@sI2y0'
        b'`-x=xA|j#dgCw~y-k?1#d_-F|z|fhQleK-vlan{+vm;vTz)+TIF}p?ty6%$MBn-Z9Clm6%EdxaL)$X;#ybGr((1en8nj7pA=~|ig'
        b';Q^ez6SF-3JwPnH`W-Wnq&UX~7ED$^JvV#b4t%g{PH%s&A~Esv)J($EL9>J73-IxF4UR4n1)KP;@RB=`aoflCkAs#AuyU>hh?ges'
        b'**yG)>+VWCkCm`mH$N=5FCnnk@!$EFT5gd`!7j|o7@DJ6jPJ)L&+AP+nhZc|+UsAVC+eE`mByv9O~yvrbG3=I-8>F1MPs9DK^UX3'
        b'!we`|k@#gzEzQX6ivb-)qj#|==f_~)b}I4xPOnozFpF1C`(0v7?29Yw#7>3C{x-?Td*r9(-^iI)n4di%SD&QMojmiw{r7*}b!Lxd'
        b'&$QTYFSkfrpP&~kE}ul~oHZ~o@A}Xl)v1%igQ^RI!v~PXVja*wzHVw#NJazBljlB>RDW7F+?Cwiqcq(f8(hrHLR*K%(R-2xMTBDH'
        b'IkyATw@F3>xlu@&xv|y8@5Mx{yY!v+hu_hxuMqc(MXuu@@IO(!q<Bp6nu4ie?omHVn+MOVPrGkTyQV7EcwDqHEvjmgqHd^NRrw-N'
        b'cB7+ba=)C2ZS-9a^h`1(1!C)jd(`^}&oPqT-<1u0l6>a8($q9I_&|~Z+NxmgaYA+>_^`(_%E@nrX^X?|EBL|}yv8u`{gr>g#cs{4'
        b'UMibVurnzX0R><C?yU<Zz~eE5dc)X*!_VxH74(F%<$Q-aBi=Mc#IhXmj51!ZHV~HYlc?Y(AtFXw=d*K!U>iasAIpgd!%@MmoAJI6'
        b'vIb{utZ>>4hv2TH;F|-Pr$mbEDtZvavZ+j@uNHB$G-~g-O>sQGMdP@&U>2SYxe@UHT$HcZs2d6WU&5Gh&8(0<SAIPptdnHiI`(#I'
        b'a+xNd9?6dzi2$t`wH;C^TI@VATH#DaV;XZGVA><+XZvuMk^Z=_i2<!^pl8~Tj%x5`JR;2*wop4VWB8>o-#38=WjVKke8#`&V-(Dw'
        b'jW{mcF9Z^U37aRI7d_7~FMVF#yuzNa%mbe?_k0qz;NbM9T_jQTs*m~Q#%=vlVt7!wXX((hs`?tx<eVqZ)Yr$drp_@5LlEDe@-6&>'
        b'a?_^GPcWN)x9d5HT1}UpdN<_h&M7^$KjhwD&i!rI{so4-^g_*SjR9|NH5l*{jUO3&l4M^*hy+zO{@zVD9$>nE6(9RZY}ad(e4hu1'
        b';w5+^@{J{=ge8i9b*1#wo2Msj`dis^%;`zo-^zNoXw+$AHM7su$$Z}j`WqfO^=v<9+p?e+a53$@UE1*Swz|4P$=3n!k4@TiyKH#V'
        b'W<{M^I>NNoq`g{~SMG<H{U+&;>W^-1%`5t~@65omQ@-yR;`F5AD8-4wCnojwM)s~RJ1sf&PE9xI`zTPCUjAXg6!@X01@)CWgXH}H'
        b'VVd$o%|WvKT%ayG=WJ-7;!+=jih*Mqd>X<kVkTG4jCEM8b68RaAv>l`tX*dPAJfhMKc-9eF~I=*gzdc7cb6yOF3&`IJ*006YY$6!'
        b'HN1UM)!#wit=xgjR+X%bo-rKjaGs1TPXCl4L5>LNr`<`P+P-N2--isUN;{;t&a%2#YDfVSMoK&H7&DCxuZMAuk!g19vQ9Ak9e76='
        b'5(JK*qey)jVqY!AMiS{^+b?L!RGQ@Xtg|(aY20k3)kdRyo~=oASnbNh%DuIdwqJ#C+#03RKn)Cw8s?!25lLuR8u}GTW#sqa<4o8~'
        b'^3+*G!meehvuO3Z^w3OIHER`CYE!;E?u;PdoAzb={!|B55&kpR-rl`o@;(?KWim$L{>2nq%rTJO22gEh;&jwOF_gy8%S3C^%TR}p'
        b't#h4<ES~oo6FUEm^?2|2IZoz^AkK6uO|i0mj_f_9baJBJS9fiHFE|rg*r=>-)M(#6?pj7Pkajt}(4j=dZ84qk%~4aL_>4oDR+4Uy'
        b'tY2A@(bs?6C6_Tv{Bx(+Bhb2!M_}slo(ascj7TSYXQ^Bi{rD|w(Au9xvyjm&<F6jIjUEfFHxs!fSNfU}k|lMD`qUVJavt~;G)4i!'
        b'<F{CfhBjieXvr|rt>BI0MW>E7h@I;C%os{z-3%k`!bM6Z+$5W_&`_4~>Tw{vJ(BPqxIHA?d4VU1mlNvGC$Vxm!MvEI3HyP|2r-+`'
        b'o;vDcg_(nfc102}Nekk+9MooxyPj}C&beroBbjK<P{z4b(1iAeUqD{Yg^3JeZzR!YJMJQ7&8^v%_$l3uPDru0*SbT=kS<PSb(J+&'
        b';&~FT4o~XXmqS~Nt(xl^J?#)b{-aTbM+~cl<A7`)&8h|3ynfWyg0z9cR$i2D_v2;l%h8v7*A-`}n$+b$Jw~?BUS`#7#)tY0F-(KT'
        b'p-iHRYo*n%&`f5vt_<j)(PTRte!)RG6QqFNkA0-zxP2OtRuToW9$IS^k$XkPa>}3^+eKRj#KG66ZI_O+>~xsJ02BLeVct(jAbOHS'
        b'U99{r^EgAcPicLC%=s^3p*7NZVvLEZPAG$}#6NX3KK%*j1=2oE_GIp{P0*mLWJ7POK1)5`S%sbVk4_n#nkN$;&rL}>zWsyL2x3#6'
        b'5+)j`$kb`JAH;R@I=sYVVJ4ny%T{UXlnd)LAIY3~^s4j?dGRx}#Yy;7CL2vL5fV^@|NdjBz_z2C92(z6V0?%R9&s+D*je`Jf^(x?'
        b'JN0;q>NvYGM;m#ZiDWk}(MB9+#O%h!+HeTX)nZ(pfzm9;M;QlG&%~8g**gb^234p2*1wjB?dq5U18woW;uP8O)QyXfUQkZz8-(xD'
        b'L|?mgj3F7?%*h;C`)eC!uQB3e))srz89~{j>lp>kiKbaQb|s1T#>x#8?#P+R11H30ryh+go^v83`%<(p!&_37SImlo9mb_Yj<tPt'
        b'%v!0mTCbZL#+^F*%4aVz(?E)GJPquS5Obc@;p{gDlnvZx^x3hDvHrJH^Ti_tlA{q6k*^;ShHs54E`Fg06%E_Gqqv#_L$!!dhL7CY'
        b'iwVPa=CPqPCoQZYKPZ#@GgLnpJFTkGW<XBG7j(_jTx<-?)7+UiUFMhx+>aeI%r0D($;ReR&7$bZI(iC0$Rp@Upb3O_cq&KOxY&qn'
        b'#>^23ujp7Ened8u&6^raj@+=UaJHSD{xHdeF)<ad<W_|(S~g=iNo-_e9lDjZbdyA%E!UBgD3ZZ#WXc$doIIPHLMY`F%_NH!2e-iz'
        b'<Or3?JWS$C2K_l#g?Dloos7X)B056IqEyL4=?Mvy$2=@!rbWmYN;WA;hA02?-X-eawHu~O{(-!2`_nOlY@&Wu#|#mp{n|JC6U&X^'
        b'idB?>%Ip`Nc>|<q?@%Lrt?;!q^`l)nLVZe-$q|_wrzcERc>ZvV|HCm`C(=AGf*}(kAF*ve)<aqwH2s{xb_8>1E05aarWa-!jH?=F'
        b'cA8{T1LZyT_!%d3g5IGz)vP-B^mChy2ckcbRe0kK5i@7c)XiK5U3F#_6Fy@&q4gCz_hTlvE+JjSys?n&ok`_<5NHaklC9p~_{KiP'
        b'6O*j2UheT-8{gO$8|&yFg!#&5T&ve#3>b6>Mc1G+%ucBPw)_g#TU&6ffpw%-#3=Pcfm*h~XrDQKZ=Gm|aR(dRgR<zDAw5JFTh1|q'
        b'!I7R&OM)&N3e#pBbFj6kKu4{mzhauma3Z+B#P$G;!;m`9%J$+wT$TjX1)jBsGZYz~GWXc}D`GpjbW2H$os9;WYB#8WU5A8|Q)t%C'
        b'3InCr8O}&IB(ORK5q?3dIu^X372mzsc{KRcBJRE=M+6=w2*>L>QpEycqGNKuj0)NtflsvLF(Uc`PUwWZLU<2^gPIEXq^OPocRFTQ'
        b'g#TB@q+_53!;}gY^dABf3OXd8i%+_cN-A?w5UMV75>V2vqo5}x)DCK?V-cA$0FyqOi4MMUiI36F7*>jA32&^<6^RON9_{BI&%2*d'
        b'G|{#PkrAd>Ejj2qw$vs^PvKM3nN{nI5y~FYxLi@V%XLh%YO|4IjoDKR4;t6S6uxd;H_aC4gQVt2rXcoc)E8ud|7eML>(mXl5`E$Q'
        b'&+c61DH!S7z<(lU1{evmbej{+iId_KgM?^Se^KPQq6nNlgeTeilDE~``!xH)w$;{#Z97z5-`lT^Jg1FN&tt1UTl1x&A)5$0<xPqk'
        b'YJ6&6Hso;@g$MK7;t^GQpK@C}<k+Y9%y*QDacaYf=?jTQp5r!qCldhYeAo=`RgLozf-BaXJ3Ul7Flu6MKG}7&R7#X)N0!E^)dPz5'
        b'm6VhodQnx$H&pfw_BD4w>nl6E3Hhn^w}qY8Dx0ETFn}v@1uQ(q_P0JtO640yl)<}tiU^zWXoD0to8q0l5qM|sc%P6XVxrkdNg?4{'
        b'7iHI~bRuOX8$lA<?mmr5IO`X@r{4(ti%{6RpnUW1P|EX&eNho~6eSf7+~ktA*^D$vx}}aRFDJCG^*#H#lU@4k!HQ>pxpiG)%$CZ$'
        b'(sLr0bjEu5FSg(0wj{4vuT<}zV*7L7nl+nC`;_^z5z}sAm3eLwOv0tMvsfO?u0HOEI-*FSpoKRTYs||Tyy-?Ca1|-{T}LMuC|Y-P'
        b'-=%!X2*6=-h~yEQqc1|B3W$A0F-$LAdc7d{BW7oW+dBIuWPe0Z_RkiD2gN_M37&oU;<ho8p|Vv{%l4FC9;LFwOJ=9)$TT$>W%+})'
        b'v=6%0%wtrxGAD)D{v%hHT>YxDd`E!)Z6B~eonl+<zObB%0F@mj+`U5OiiD$W(qeIhlz{o;nxc#)TXK#Cifa4K5}8_kt>#D4cPdac'
        b'|0qlw1@j$F8*_Y^mm*gB$((-#B7nl8SrR;NRbcEZN;(Qd8*`L-2nw9P6~O8w()mv+$<@$^X5VP)(b0%pLb1Z+A4}064Zd*w3?bKM'
        b'A?6aC45es}PCOy})a-0!Y9s^0d&0Zx7QUg;w*|CQk3u6;q%5?z<~{=ZIjy9!C;EBzB*+4NJMD9gQ7bOVSY<4HGX3nT(!#zCnXAZ>'
        b'qQcMSg{ObF!Hm~86^!>A9-4VSir9zTF9lFm6T*^QggY$IB=SEWNLkyDe5D&9$e5Jse%#lCcT&xY$OuP%n3_b9q6ksAc2z$R0on~@'
        b'98?q%K$GIuf*fp5Ez^gmIwr>QoSFbs*7r&PWzCt;{?G6FTwFt=W9KLR4YKy=ePInCwL7Nmo4I42Ak%lg*U$gG-!RWHvm$j0$Y%|!'
        b'<?MDt7&vDP!(0RXtX;wSZU^DHIKqD_%;xKN8c1h}*pXf_jdcGZAi%mKy-^G5>lb!kgbC|=lc>Bf|Gt2F7U91QY5CrMW`7T9JCBus'
        b'2^iwp(qGt+@QSRqorz4V19{2NY>7OzL}7U|P!(gj6-fEM*YUZ!a6Dlu&B)Pa{>B)qn+)iH4pe?kn8RhX_SI%r@6f2dps$>;+Sjt2'
        b'T;q7^<EPS>*VM+dkyC_o$`u!>_T>%P?puHej1ZdHYZ;?v_ER;rv|)K#_=ij7JF@33x1APH`(A*{C>G$h?sL6ZuPc4qN9?k%?3t{-'
        b';f7;1U)Q(8?AZ4BZL34vTdT5%PY%tEjFX-64knh7SHD%}Z3?_5hwx2}D%?x_R$xsXUVs!#791l}xL%j;e$e`?ow{NL=}RJ<Z{J|1'
        b'Gn2H>^jCjecBXo>gEVyz=ia_{W=~o5M;i5)RHYp)q*50ttvZ#MS5a^9>QeaM_PevMryS{HWUj2MDem4KWV+6tDaE(rNz+p_Ba=iB'
        b'1XEvrBj9}727q6iH2B=Pw{HPZb(lzfWlZ7NK{5b3HBajMJ}`JI{_VG8)8~<uc2}OX{9C+N$u(Ya@GB=NP0V7V)9RYeV5Q0JPbG)y'
        b'Lx$?JxZh3@>U09_DYhv{P18o&_HbYD^u(4cUjRk_h7`5C0(;Xxv^o2nvP*mBIT{9Uc^33D3(%Z7j`8Zw+dX6xWecE(2``74uI+X('
        b'qqd@QKiWx=f6^d7VX70^Wg=6$$p3UeeSxqo>E-A5*$qnOUO}<OF+QnJSYZiQllNp~_44oZv2o!Ht{gokS6`Se#HkV`Ygi==oKY`H'
        b'G!?t-S@inwNEby|vd5aFdP>H|&1jN9jwht~n>IH|Em}oY4jcCbgydT{vnO!7Y%4p3J#hni0~4mHFRRvU-fzZ7aK%s<@9pcsWt-v}'
        b'T<4vx);`d?zJ|=nB@C%d41_pO{IiF&pZL1Ev&=fHOmnXWvYCvdLCn<O>oTVH@?yl=EAW1jT;0hgiWyn{Y9$lZB+K8s3nt<CW&m{7'
        b'xY!-Ir`aJ|Du(F%iZXi^!MFzf5RoK?h>DH0F^iZUZjvm<`pq2!jP*ZAjd3$TK_3zmCU0J_Vyv)1URVImnT~KF^ZJbnEz|4b7?!1Q'
        b'L+IOmjKrKtKPmj12{WiHadXYNh-A@+y=<H+Q6Z2mQ5viZ6TJzj90vLzU{w<yAB3ts+{cC!9IN~|GZl!nzOM%tC1(s9Qm4zy{lI|1'
        b'%u;hWKxASCh@Q25uDDc78KvKGP5*X)k-NXYF8LxrFp_dlAon7fGaGZ6BWU}9Pp!pDd&Cs<E~87cM8+(+F-ueQeedNGv0WW!Up55@'
        b'!N}}6mo54+Gt^yzSzQq{*FX<mHOI}X+6_Tfi_LLq!6<}^&+#aOAk9>rx;WBO66VUHTvVMqAZKDMTW(k$2>46F{BH(42YUH~z4~wE'
        b'?sYd9xuxWW{`9yl7umTuMq#FE&AuN%H)x$Z9jLKXf_977Y0gsCB=J8aEASkdzOnFrXcwtj;fcpO<6hpUr~$Lg6_<ibYir35%(%wp'
        b'){|{!QooV9Y$n~yf8aOtaV{l@U-y5@aHVPJI!kG!7a#WbjH|cNtd7pqiH+RLE9>!<&Alz8FPSiNJJ*BveqwJcDKUVz8ol!gW_Q9|'
        b'GG{&noLIxI^>>V$wvFP-v43yCNNJc%%?hPSAK~vDe^{<=40jy}xL4dLSzXG#YET<ex4cZ|JVxZU;j)#TtE&L-ufb6d4$036+p|aP'
        b'h8T4rsKqFJ?<M@p!qiv4a&cDuI+_02FqjU$f8A{iGsOgY<Yr)wtX^mXj@9IV(qZPD>tj;P+^+R8q~v@cmi4_CFmt=t#~9YnpJnE1'
        b'*2loNc1>e1W8!kk%1;O0Vsi%3cF=z#=Ttz!N=^nA#Q6pSFq;BBWctgv@dSp4oZ|t;g}e9c+-ra(5T@b~DY*~4f3Ao`Q!5j>a7A(s'
        b'LA=Fga$yN`ux6RuiG}Q1cO#I%)Hw{oOXA)x-SfWf^bu_4&Z*l+EZH|$IkcjjrKX!wWzd7NrbCNFnNcLT_l>_KSD%s>JlvZRbA%Nq'
        b'mU3L?d!(6*-cpO#6F51(CYqF_5w?gU_76$BEGDXCm8}(lo3_!+G>vUtwIkVTMVsaJkE-!DRE=*ER<!(lfQV%!??ZKcc+MT_CwUL*'
        b'm-Ai#uRbXMM}Wy*2#Nm=aW)qMTwnQDHwWmLX5BK16EzDruZ)arB6o=V3vOs99dU>Z7pqd6WO!6=HzsGf(F8f^{&iR;bRsh0WvHKM'
        b'LT=zf!z7?19V0Div{hpA!Bg9BX#`Zae~I>M+Y7-muShNicHTJboEfA3@usle?)xO5cD5Pg=9Y3Q;C~n#{3qoF-yDWYfdDGJU$b`?'
        b'1gj-2zW2rjJ;lNYQoKj@SK2lScv0lT^3hcFa)RYW33P<^iz6&aRJpX*;s26}CHz%C{O>5w7`C6XGNh9eS)IF_S>ocWF}9t(JDt5~'
        b'%_||;MFd+&X+4Kob}q`mzaF+zq`L4&82e1OZrLfZ+Cb>-0qmOfGTXxf16+s<8r{;aD(tM%bK?lV6T@vU9kv^mrj?L>x5V;FAh@TV'
        b'$gmwrsXOeVYl}N4F(jK^Yw48ZmL-C4=>#Es6%PqBjrtC`cHd#<R8SVPbp4)w5InU~hBWGC2pa%AUma$%>-lGnusS88x~8|NsF#s4'
        b'Vq+%#ELoaElp3j^3Q{b`rw2-b-(pDLufRc+nu%b7CmW7Ha%1jQTZ~YbQ-h^CC0}&J%UOq{M9x10L98k^M!Gna|A1Wk{9zZT1f+Z)'
        b'2^W+uKWq%IUul^ZOm=yrlDS}Ml52l|c=~EXst<Km%Uh$|MvZ!w2=BjrORn7v0471)Nj$5{KJuiZchd^xmRA<Kbi$&($R<PKX{6g%'
        b'$`e^2lS>tZy?3Jw`rY@^oNio}XY_mJ+9CiYMO<)h0$J+!Pc^bjS6U)))Eky+S3x|9@qZ0WkXL&3qV3beSO90sZ&X%|80lKZoAAn@'
        b'&=z<g-25(S`C4jL%Z!|Cr9@{wCo)TxOTUN-=7&6K8z=MAju>@HFSihyL4Q8rqU%f>Klg^8W#1t17S`LBc(T_<VLg1+0b=^zE%nh)'
        b'&OKb3kfk2@!nX8?OPA@DT}ArVK>s;)1GLI8>#Jqe*3DbV!L80y*Q#GEQ%9=@Z`w&oRm0wBS!t%Eyb9~+%9QBe349!bV`e1HL}+w0'
        b'aJFEQ-%4&PHReh|cYAX75ow8(X}9NI^@;ER*k~a%usxDcmrN;@5T-4O{td{%?o)xm#icZ1x;gUX#U5j}s5D_|+GSEw8gOrulyAc4'
        b'p}9Cvv{4N`c|^bGnhT(CNfq@6nN#{d$!(&;%r?6L*D)klAn~IeHMMHnXph}+Z`Fr<53&<v2tJ`_vm?#zyw=*NR4=Ac+bpc8OS6-*'
        b'(dZo+w%=o{lNZ^wbd6l=l3s%D3E11d?5P&c@YxL+uG~xNhHF^XY0v{|B_{%Q=~ZT$bzd38n<@$Wi4Vc8-u4~;mm~U@5mj~PurX7T'
        b'(}(5nJm2GzUag(EBLifQBg39a@4!2%iYv+T2Z%)3^dC3v*tORHdPN|ywxXVtBoliL4}cCHvnJ6|5%ajyHE!obTjr7ZFKDdQH0sA+'
        b'O-u_&yK8()J6RqVh^^QGZQ#n4mTLo#wpYZ&*||R;Fdea=y`sJoaz$M^WGCtE^CtGz<irq!Njd^C%#I+i@=JlBuU2V#_7<~*nT{8f'
        b'?J4W6Q*QqRZ83HHnTdi;zrEqq*{gSodru~BfA-8EE*JEk(DWNgyz~UXB$SZlX98H_DqNe%q>*-ny5g{6%d<glDJ7-Q{nhJx01y)e'
        b'pf=Sd_mGKun1?TNvNLt6QiXIN>hUcLqJS1r(}5OI_r`WXpec7e=L%lC1T~9V1C_10Y|A+E``=g8d|Db#4sFqt8cE-Etjf?<rD^Zz'
        b'nOjOGW_a%|j-$7KFx;rx<WO?KI{b5F`<6`;H9|gu{2x@*l>*X*)-B4?Oxkxb0AY-w0<>KSP203p$>dqLXmV}^0IQnGz@AMKOX)RZ'
        b'4k1|tW6qTx;F3~ayG1_b$yGfrF03?x#J+YjKnUq1Kj8cn`F~!(QXjyT^{a&cz_>{suziGi<0~(R?3@utl9T5Q&K5R&NY{qd%A8?@'
        b'Gm{XG<t}mfZiVdX$=2&T!;akid=jtgS(>$Usp|sCyfj#duiRqBk_c}Y5&!n2fmg%5F|rR7bSi>~t+U!Pd_M%dnZ(3g+!oQpgz>iy'
        b'I}07cu}C3oau0tU29lJCr8fw3z;xou4TD_!LpRHoXl9B*o9@>n&^e(qq8Xx|f-8sZaVbr>{(%2v@ISaauWD^31mRYv(3xgDB$ir4'
        b'_=f|D{a%rXT};F_>W2ef5h*w={{$x`INje0XIT)h_YTKr-h0CsW&7Z8Jj>eNIea5^y6yDg_;9uD)L{ut*#34n-Y#bx3F%=FP+WQi'
        b'jl{N-hvU6JO#jh#;&4s)H@@qkeLW=Zd2siPg<z*N9L^6H>?fjG5TWlDB0_uCPIWhtP!(YfBP=al25!C$<%duyOUKwmy&&z8Zev`E'
        b'nu_ARhe1-iNFp^Zg=p02+s5!vbJJm?KnF3NjRhya=djuVsYpoTKQsp66Y-8za5Wg*2QiT64jZ}c#>Iq@471fAuCgS$ZMBDui$#U0'
        b'#;KAti}ca^jd>uCg8nFrbm>EP`E$X4e8TSp{|1FoudG_JbSebKI)pUq0fzXlJS!p3D|h*~fZu<YzXH<h@A4;r-*U&VR{``D0(8VX'
        b'kH9T>c_OG0(u55;3R5YuwBYgX{HZ}p+s`NJUYN?nHdugg{=G;w-h3F`;4q}Ze?zI46ItHG2o?zV=wV^|;*4P+H4xFw3G`YS%Fz%W'
        b'{O6Y+hQzo@1=>hs)M%F;##NR~0*`KTg#Y8Py>mn}hE0bkbs1%|_Sj|e{kJGF!8{N=7iam)SdYAkw54Ka)n5oxH10hl_bfOJLHA)$'
        b'Y<AAK0lYV@@&)FB23gKE?C+0}MKim#sfTg*Sg0WLd6E8nu&l4?J)hewSduzgY?B>^(t__RGE0JGO2kC#oHV;+Ms8sWK(@YMbr}dR'
        b'N4a+gahZYzTh4}XnTEJ1Lb!Yp!i55r@cSNSNf5B)YLNGF!go4MJE_~2(*ylL(Ks|qh34#~Rf`2n+c)rKWK1|=cvt8fP$nqL`ag|v'
        b'of>|;$JW#>oC^&0n+pg+FpAFda(EQPT_vQu-eY?m(}Ap;=ts3?2kXotYK=Q0oNFZwsZNr%I#k|M{{%_w<ZxdMQ4a%(rag1VQ&n%h'
        b'__}SEP!Kg^*qbFoL4)=|9pTlH&J&_$hpLXM>}nz{BY}`iad??&jKccrE@uYOM7Bjoc*CQe+}7$YrTT5c^M221k>z1AD}t_ydO`+~'
        b'Ga3-~+4CoR&h;rT_9ZiU^9oLri;7k~xxx1A&W}`Iigsv|<kSC@n57sjW}wZMw7)i~?SQo6=VbCh&1;i8>zpS?9bpg4oid_{c4h;+'
        b'$7Y+t0xv0q?OOt`X*Q>Hb^-Y^b*cVm#?E?sJO_KYQyLdXS#AYDZlqsh6fSO^V4r|GKqF4WTDwk(Yz<w)(a$|sdq`V8270)jCffgK'
        b'>~nHP&4>rvnrPeE?g=67`EyT`)Rv8Y^#!r^wJyG<$H}JP7IZd+uk8ssKpZ=Z2>tKIYDJ-#mxLH8q27VsO?x%qRUZ}EA*u@5sYz1G'
        b'rs#h=2ICpOqlX2EB;k1u206mA9QVl$7pu5!!TFvrPSjEjhW42@c7jO=VK1)xCjErGiE@wM$B3E8<cD_cQ*p2NE?l^IpLV9GR85x@'
        b'Z(Ct91&Y~UYk$|pZwi&8zfLE~nI%nP+jRu@gk0Sze@zY$K<A_@(lQNZ6B{^N+|wgwmNrRj>k;3f6{?iAJxP*{D-vGW2!T5=CqpeT'
        b'F4W<9^y1WgT2mKah$WOmKN+q7&A>Y3P`Owt=%}o0lI<v{%Wzi*90j!*ACFWmYmaVF?R_=M+JGBfokg_%BO$74@s6<A6-(-3x8(di'
        b';9?17p9c6spCINI?^?p<d>UZH=5Tub{Zau>$v*<aFR1c`GT>{5Sr!yl+$7Og20mV0walU3s@hUJ$ukESb<LX^H;Z6mSCoGn0Q&Xf'
        b'EAmz|_nS1Qgdxi#fvR4X?B}L6iEN2j?Z?O_(QBgVd+c&zw4_JWMB5h;`XdUqU#V^!)lTc;wLPh<AQJV#e||=Y$n8^^7{6awV2D4V'
        b'^q%-jbMxl51>_pMmV$__i*3va$&D0Q7a!h}sY?O2%_L=2o5AVom*GWuBmr)J9u9;VH@c0W9?>9%8^Xb5`PFqC&dgP}?7EbNZ=g2N'
        b'U=9LdLCgQTJEV8m2&G4Z=goTp`X2)mG9%@yPX5R4VDbhd{F_$807B|b*RiMzcZzbc5^%Z~3PWhH92jH6mEh*T=-zvUgl{lPNN#7P'
        b'7&9cqbln}3=fa4;cUQfK_b1RqaC4;o0by9_>jsoV<4p*^qn-SFcjJd>9qPV=LJ%)~+W&^vvF?E@GWdP~I2`W2JAtDV<GY3UZXv$)'
        b'ZX6u~j^6G)(GB*Ut=%>9xxu?0n0x(mu%KGIt+~5mN5oGAF9pmjdDlZU|5JCU4uX;vtf4<~tb91s&VTIW`G2p|AO4Nh{+R+rYBBf@'
        b'N`LHDUkTki5rpbaz*Kf2CkQoGifr-=#Do9cf6x+oP~+>CxUsX(cYB`iJ}n0ssedydTqp1+`a$`gPHjmi|Lbm$OsI*mDZ=q82ne#V'
        b'us{}+LC!rg+m_DLw4-q1t_p}tDeUC`d!kk(;xPl+mH%xB56KN2von6#ss5Y<e)h+XrDS(wcQyw2Jao7V0uAAVG5l}38HGPT!2hBf'
        b'R0@H4LC4^K)eU_rsP0*!1zm4tw>>V1<HSE`KI+v(Fc<1BN!>XU`(!dwLgiW_$5P^j;uZ(^Spou!gXLyGxt2u%Ui&ZQ{^F-{{Ys(S'
        b'dH=uVPWh=^J4Mu{+E1vO$cnltj)>S=7*}6()J0St^gka6>9jD0rE=qGPTZ!EBJFhPem*28)TczL(BhizJ!BK94;wo>+U2<i8jYFn'
        b'uM7yIS+HKWJIrzOyXP*rjf*i`I#E)|_b=WXuF!P$HaA~KW|1ILv9J5-u^@i2?x08z)N2yjNZ7AgM7%_@5z)`l31;cmqnn<ZvuSgG'
        b'!RH-C|LBU3j#jtdgJ*iWh~jjz{5^uzrwB&<8N=Y>$GX7j(qSm~hSf4Yir3x$*acp2*ma`B{)E~o+LkU<nb-!>u1EfI>BvoO8vnIG'
        b'Lzd;``#_5+o<&L?ByP-~p`Jy@$1L4Cn;{dTR+Iw#Z@OS?Y?uws90d`-IP%6~vOJw&YPQsWgvDR#!W(VT^+}h&?}F_OGhV=qcoL5P'
        b'unYVMWmyj{g>GG|zA4}OlzOimlbsjfuMMW)`H7@Y1^-JUqNVF6VY(w-gW>RjFjhZb?fhp0)%b?{1dO2S)$&YevFl-(0$ph0$zxqT'
        b'QcyMC4{8`{xfCjm%QZ4WbEwy@pWj46+ko%hIJ`{}arbluueWmP#4PCFPX{FD0~o$vsFNb+#{k|-WxvmK;YO)WqLzvfqkVT{4)uxp'
        b'0Yl&D%6TV{NfK3;Ch)<3Z0J;|%jabIp91QO_z0!iE)-plMWAB`IwX!DLc6<m;E|gK3OtQ(=s&|&)o$x@3ZOuviHLTHs-1L0M0Le3'
        b'uRf)+(OX2g|1sJw!i~N9l%SNVjYvFEQKy8K&$z#<GTRkL1Y5sB*CW-x7ns1SVK($1@Z5!JLl(H)rT1Ar8ofJoS=HiyO_#S;eTitI'
        b'^iSS5xDmn{*4`E8(n<dl?on`Y9PNMiU*H}^=H+SkIe~c#k$ENE0Ro%Yau&yT;2UWGkmsdcKh?_?=p1@kRqud_1JDHzH40p9@qtL2'
        b'V58YR<eo}D6%e?^O@p9G0APMH;7dXo!N+y^@O(&!&hAqJo#%Dg^}#8AZG@dmtf*7j{8&`A!+NJIq@n*vpj1eR1wj^d<0Q0{Oax`&'
        b'>E>VGSG*YSl51U!YeU5`WceaO-KfI;wwNfMPx==Blwp~=F(SnF!6uYq$A(_5ucsfz&SIKH@Haarx<w?i+wD&E^F$_1sN<m5V^n4^'
        b'E7D)`AN2pXHknAs1Y5=3IeK^aM6>8SM#~EWL~WMh+13Q6^yDZLyXmbmZqw$f_55&Wc|XvP|7WLq=5YKxyo#Csrn4NcM~vUL`bMQH'
        b'el;7v5id1BWG{E-NQn5#r64_G$eg~3Fp(fHK1J-I+0p%vPLPV|_@vW^XK>K@_fE-8A?!k@@4Ddls1t9nLf40#lHtJCtoU5Ayjh5P'
        b'zq7n4INsMrI>IaJ#P&Ect#*pTJ9rDaLGn?J#;b8R1oxeUhEdbv@toT~<>?_$Qxo~<2HNiq{4@qPg!^k~bv<p`MW<|Q=es&X18+Dg'
        b'B5xuQGyc?hM^7YCp?G67s49e17B-lJU)LENp8;}SxO#ISqqx0^3R+_t*wF0$u}&B^BsW6$W2BR<Ix^=GVrdnlz-uy|ZpWj@tJ?Wj'
        b'Ls+;-8pr?F1T+?P-ch>>$>OOB)MK2T;PWwrk)(|opmsf5^@8V*ou@^N9KuUfkVJhxyutQ_2)vBgp{i)X_2GCuDanM?v(*nNpa{P~'
        b'3Zl1O{x90FdpFjyAgR-=LsOZAC?VHarxtDPtSoj(p!TzIN8V3S&+Chx`ro1oeun@Y;@YY9qHu@4@P2zyq=PgTO|{ym!mPqs6k)YN'
        b'PYj2oMpCrWBEwplJMY#p4Wwoft^IZ9Vph=JXNPn{S!YNmD;3a&jwDg4D+utpd`j$Y5*fJlm7_Qojdp+==71O;Pl4OL=Nh=pK8>U^'
        b'U={#Kh}adr_5i{EqEpfs(l2kc@!6gKq0{?ouVH)mJMIw7jMIm*(f>tt{;mTR_wPCcRURv6EsNyu>x?%{<`X+_q|5l3o$=8me;gAu'
        b'*dd;CXZyRxF}YI!pzGXiAo!k+|C|&2T>#zMF`<Sd<Y)o%Q~`2?0Qs*1<kBEyee3ugrF~N8P00Rc$A3&I20CCMxO-0Fe;RAX@9+3`'
        b'J=nIVZRc2r-LTYZr3a&T-tORu&N}(dkq+>Tbns&x&W*&*A3ID2V&|<6+wG1zS<r5q!L_;KP&eBjgBHpkI?%AJyZ^>)b$o;_RnVoN'
        b'uT*ygI}ILDnyoF)@}m~{Z3pTo==!n);(XTv=)T+mG6o%AbofH&{6N<m9eGLKBjf+vQDuOcezfIQVDOyn)i%3fuDTE=1RZzo0rYZM'
        b'U(1a^b+BGujzs?tKlz3D2WdNZf7OVsvaMb2C_GIydxc#(vLso^t^@k#Op)ap^|0K?5#~rbGfuK*h1E1Cp#PrYHfjX>z}M}9W@*|O'
        b'#*mq6I@e43<`N~vrW@lD4M7asRhr-=Kc3S3G|AUmoZ}Ad$DOsJ!3_-#*QwDPvy>RD|2qW3<X#$^y<|%)Ygf}1sa*!q9@bD?b<xRL'
        b'83~#n=FSP4A96Z+Xl5zkkc(9x%2pNa=|~c<&Q5qa7Xml52kG&gJc$-=h8`|gt(h=5tO?=bijJ<SjKrerRF-$4@LJWK;)^Ah(6#^q'
        b'c}=UvqNSIxK3w`5&Qxi#txy_#p;qAV{7=VeYH_3fXLKwZd`bXl=h@x?BGB@-OgpWO-_{YF`rDpBhaIhnq9#053}HKOwZW7MU%Ht_'
        b'^G|d{eM$0<V|{qKBRIbbwy9Ry#&4Ja^Q#VieTPE^P*R0C8M2pQBJxrjI9#%POYSI!f8Txwi~#3{R({n)(nTG7X*-|;-ry-`%<#oe'
        b'8RpuElrLNPM>;@OXf!x`Y!W7L87RPeL};8G41<xQTh9N`F6_2NQATCZ`n_^WME9UIRi8ELFF@S|h1@&scRCzDA8RSFw@}VIt^Ax0'
        b'fQ8d1T}Vp|8YbKtd9aL+|D_B+cc%>hf>HO9i85O6Dnol$89brA(#DecYCEYt)XK+(hyY();UB-o;Dt)=SH_VB?hp+M!aEoWus{|2'
        b'1Il!j&>m@Jwi(zEJqaz}+9b|oQJ}`}n#LT;jmTzpgP#|7tdE$|M7ghBi){oY0)xm7990ju2a^|FMTa>aSpgrVkPsMK5sHnSUHp0l'
        b'V1{I+h@wy1`FGm#BoM&FLM&pqy&Zj#;4G+bO}FIECVdYPDUY{iMx2$dBmEx-^q&RX9|SViv>EB=)$dQvU$Z8^Sh?oL!ZmBw7=1r0'
        b'1=ydpn|;5)dq||j#&r$x%@!3QKecgfyASuMzSfF&67{x2LWkrDG$P=*^BeS|<K2*>lp{9fYI3J8tlEM$O;bDSy78>d(+;pcl=ZVI'
        b'?MGv40AL+|a_2`jTLpss&^EM1we87$xkHnP6FY|(qLzOy4EkJg>QPPc9FIUzckF1&Q|+haJrpy`^4d7m`m<YYc!3l1(rJwM*UBu@'
        b'M!8dH_;Ycj{#8uEr-j-rWkoBio33{H@l4dqfdXS|6P^A75Nm79gL3tHg)OtKcBN6)%;Z(PfS0#y|Dk$Ca{h0`>XtAgRHLpP2bq=N'
        b')JF(v!#(Xm6K>FSdqTp*I*a6JvPIm3fuJ6Q5&Tn_uwCAeTgSt6M~Fj%ZaH#p0|idhlatVA-$m~(L2IwDaOc`Z8-t9<2*WPqp%IC6'
        b's;Vsgd$d%G0sGi&Us<5~H!0OCdWAhecuvuV?CyV4nsKAe^N04w<W02gbtE!h(8k^GN}ioDRHmArF5H3Ho4lfzbK|jfw|KM%Q+|Re'
        b'_q^^YZ3oXs=xL(-)F{`ffl=S~J_g|M4>O;QSWHTEn~RFH_^x4*rQ@Kl^A-#*_*;uv99<kg*-Xj#N7_yC1phFG7yYJPFbBAFl<Snr'
        b'GLH9h+bJ2J+YVzWpVKaw0Sc<}kZ&+1jL&QzjD`>Rgp7`eM@QlfQYMCTB)d*LrXN8FLQy|s<o>U&m8>?aB?-mhj9d?%82<itHIzLE'
        b'^9P}nWbqm8>bW9*A^IFy@zDw(f4qUjMgUN{2tKhrUQP1%3SKIoPjBBN;pd{y(sK=oq`zmp2`|lbyuPQlIGvPa6Rml;)vh?2lw=Y7'
        b'&)bU)XrRE&)fcb9bf2HrE?uWW?`MKHsy*rw$*U1!CUsf8oZ$6AccS{zq^Nabo(*|<Eo3Amvx$tSTFsGDDvHJY&jhUKd#ZBy8G<u%'
        b'N(}_ZqTBdBzWJ13QDjC=*$ZHz1Teb%hUNatw>^>2cbHl34dW1)ai-0sOU|RAhj^w4;rbE`$K8Y<TuWb_8X-wo8v_JAf6X<E2JHX='
        b'NP++?n2;}O3rf7{mvW=E3y$&E+j65xm|me-pbvD+uiMITO^5%gt$ZZ(FD#hz-(W_`+o82;Q;UY%Y>Z2Be{%cmhBnW)ZD_W#{6<g@'
        b'<5GgRJ@I*MnQ<w>h26OsqLf7~03<Xe`5GPmk8Y#;@lYUqh4~|&-WJm5<o=7a=VIFv@+OgOs0Bd&N~=CkWCEkClRj$3>s<RJOD`GU'
        b'B{MULOmR%qI<owiqS#FB^cLqikv(jov_$f#v@{!fTWR>&wDpol8(rv$S}%2Rd4kg!Ha~5H<k3Y=!4qDeyFs#an&7Ew1%{0JLb5c+'
        b'j9xQ&Qd%rCbIIV#JSH;h?9yV%qjQD0gc67_1|t$KOU>NUV3w(}v|>qOYtR$EyW$H-wsIoBq3Rhkmm2gX`rx0Dn6pJl15uC`{y&ZS'
        b'2arG+*IFkg0u8T&%i_BY&WRxS*NbKP<9CPIWG&!qDDfY~Q2r9;2Z!bUYfs2sx<^32_588zIi%`~EyA6U)BS`@-*?-toeup(W;=<Y'
        b'3mWVh5+>~THha-@XVDD*xYVhg0V(!&kma`sCr3E*2+!$Ov`mX2iLJXuxDawWuCi@u1K68|0CuUTq;35b(z71J4hmu6XQd@_&wpdU'
        b'0U<z_>v_CQT}#__i@F;;zr~1#V1(VeS8Uxa9;#CfH>#=|HP#oz)<%t`^)^U0oSFUwll9P$VULhus%#5@{uM%~4V7Q9RqiRofR{1A'
        b'I90aNqVTL}!`y$ukX(!0W5oC>^sNWqFVW`^QtRxOAz&#6JTJf_ql*o4&ms)4V!%y^&OzVyAj1DsRqM$@|5o&yZYCN^<MAlkJddHx'
        b'<VxHEWj`pCy$Rzz4`9+K&{^@c+>?&Jjp)<6zptwI+>icZ^uzz9L&9Yu9B)mP6N&u^yTo`u{$k?Erw%oV*n|{700jGvLre^-i$xPt'
        b'acgQqXvz}T22OP7LXOlANN<F!No09v3=@ekD3mx|k|r(%4?nF9Z)B%ZGa%}B#aVLCR758e(MgwhZnnnHmf=@NdTz8r!~%>+P1v+Q'
        b'%X1d}>F7^x%&@$Ay9aq~j!<DS!bk}w{nv6+6DFx=lUVRrD_Z0eCLyYFf&&mWw-NbUtwH3|qq=utx*srILsTfRMtxL-q2CFiHQ@B`'
        b'60&_8%66xM345NxgkK5?6aFnSO<g8{xhTY@{aftHVAhX?$d&&ZnVO(bzboW@KUe_;xZN)bIGhXNz$lm){TFg37KEC@?UyqO80Zyx'
        b'zx+Wt9#gSglINFetYsQ&rAByFQZ19%0pQVA=z_>!P?Q9Eo4)*Zu&bF9f?d8z3@-ok*x!u_!AWxy1ul2lZE&UvK@<T!7@c7j`|Z2%'
        b'wv8TS<g6i97#Ws+aBpU5rbzPFaZg{%&^}dXV}m@l&Lt;YxEDn-I_}xh8lOOVp1~$Qf-IS{cw$co`}!XeB6N(RiPA5Jx#j}np81yM'
        b'u_xq%r%up4bnnsLCb4_Vc#>qs@WMlQ>6klwoSUU7za2W?gSvS>^@Lo#TH@b7W*QNL+MQ2vt2G&&2TlE=QkX{DTR~NAqQI$t<~FLY'
        b'@3aKx;;F(uDU+VyPqd&{9W7lOi4*U^7WE5+QB0^I>J&x|mf`}=Us~?WE%2^`?t?HzcIjDUxA~eXSH_<Y@+Gao;ftZ|5k$JKGTXE)'
        b'5KQu*95-r!UiGsUVa}{>6gwkezFm`kU%C!NRehuB-SM-lT7$D%m{{6&V!{VuN}Klb&tOV>2<e8UpNJT0SDpD#)!BJr@T4Nvfroos'
        b'I=m>+vSd8<D2?aJ8QK^@tehiD*O_zyyyV8E6P;PE!h72qt^U06*lfwoiT9c+gZ0qesmJ37`Sky_9=f~h@y((Ck9y3!s~*4k*Lv9h'
        b'5B13Tzttn_?s`Ba+*im<jxfqau33`R*`~z-_hs@i+{r-O`VR$nGE_=><c!=d7FEo@uh3%B2hIjs2E*Ya;449VXCuBzl8xC3FW=iF'
        b'v6&|Dt)1FisjA%ZVf1T~6Jdjo?ocf0k|>E2(+6hETT%y_51I=OYTSFr*?u}_7;q;u#iHC)nNW-mE2kIrW~v~~!bYp!Js!&f?uzW#'
        b'#`3@88fYp>>|gs5IlcbT+o>=Jl+m7lv^0^H&M=s>jL=%mL6)7d--~DF!eHu29pv9_xw9tApGBPcGcBQwBLC9@n*6tcka5d-^e@%b'
        b'n``Ei&9jxMLXW&0@C>xz<oZyUx{-icR*e3WF+7WBd5;7h@FE38r%C@m$4vFN)7MrVY=}^A44fvtlt?lX(0=aaJ3>X}e1W*9oIm7g'
        b'fii8+AH>6r{RjDjE#B~a|KnqcC+v#}JLjroz2O8KE^?iM8N905tI=;6)1LJ<QNcR!Ck}<ylSB5nA|j>lkjK>m{oD560#Khfc=;G^'
        b'b9${s|I`@d3@MH6|B@Nsjp*_QUlB}cKID0&#Z^EcoW~H3S48kTTik2L>|CN(B(mdXNB?ie?B__kEZXB}fw_sNqQ$oR;N7d;+}#BL'
        b'{Ou!t-8IAN2jwiQQX6H=EQm8KqvRC$895$-hoQ9I`<NW3{##nm;%Wh>{ysrBt2$(6L%P}1;BqGldRQpPrI&%za<3qj*^vE}5{wAU'
        b'187kZVDQ^R7_mBWDwIhk>=NPg4uBgo2s%6}3$J*QY+Jo{_E~j1?J>0|`!vD<%m!6+qssO>ub{?}7`>79{Icb=2+w57h_jEh;Cp$A'
        b'3`5#BA@k1^IYb5s!400f4u*O|vqNQtF8KbKU5ncfcZh_A0MEjf(^v#PhzYpx54JE=k7%AqzfasCN{dN90|n=Mg*{4XF*!Z*)Qtpx'
        b'e~V?W`0SjPb`ew6MB0{Nk@H9gSu3hZS3tls6GfiE>*A~~g9y5if9tq|jCJfFB|iju<a~UK{&jJ1F9AcI)wO&>o+f)pCdSePL*!Wv'
        b'_%;0+7(DmO&)yS?Y$Dxn$<Iy~d`xT;>2Jinbv%)h=w(vvy5;Ixv0$ZB$B5Ce6pq5*QQ+G9cx5B_Eh?Ohwr6O=4#jps=H+AUXtuJz'
        b'zm}IA@-G|HW*ur*K?hzo){eF^zj2J8eCTeYb5LgSV~6l+K^<)h7wI*$sguw$UjE0s7!LVa>P=-6)yrhUBR%^>9Cy8YK3a%|58>W}'
        b'8wY`_n<&fdG2m$RtAx<$VjC@~V|O@s_+ZH3r4p%^QJD3jko5{=C2<h_Ipn3PUKO%JCw1TVQ{K-e^0JAbJ%%_fXfwa<nZDRzxMO>^'
        b'-Sl`)9}+Igh_)T~;KfHH6Hn9#@dJnW_dM)d0gXfHoRy_*_g2@_EE}<=4tF3j)4m`@OqiBFSY1u$*Qp>8I}3NuGckA=bJx&J(a!r0'
        b'2CvG&^0cCYJ`Y2?^tqWu%FF^oZapcPNuY>WLvuEo`*WnLz+f&?*^45aMd3UQpd?{ijoeq@_dYB)i!U=%^NW+$tl3=fn#a^il%Bd}'
        b'=R})IcBzXe7aziDy_r+ywvs*rQ5;9+JWSk}vyy-PkorAYaU?1E1!3;fcpAM;693~;r+$fpdUD^P>euKq`$WM_?>i{dOx2U+9($jr'
        b'G-~&zO|&{Kns*$M6oY)bs8uqN7mLC(iy|%-sd7FH6lWvu#m_hLRfy)3rQV_!58;X11Z8pb8t2sAZ5vkGbMV+=X%x+0Jh<|*%nZ}C'
        b'vP0@;ZlW0eI6xF%!q<PyoHciDZ2YnO`1eTP`9RTcybZhEUyPiVd;V}Jhr#1V@z*oWE@C}Y;hg};k#gLWVwVu==n=bCCHW#yw9MP^'
        b'rlQgE`H1K7LxR1)GKPCw`HhFl@d6!w!=dtvff8!Bi7-#yy|-9hl;d?tYSkAA{ScO8K9nQ8-@_LjD#yDl`89{|_?qzl9{ju8ZreGu'
        b'd~)q&T)n1&I@2ZEv`yK(Me{6GQAd`01JB8NBsmgds6u7st=5xP>x)*3kwwUe*e!T>!(zf&6zeUD@khh-GS;h&*_-yR#2sjoGO>0D'
        b'-T%E^8-rH@$cUjD6=ZPrDeLPa77-MTeOs0|AdO|J)Q;KSe)4A?KJE}Sk90jLsYQ#%lVt}1HHQ>*0U3&MsA5#Hj-P|A;+Bp2&yJu;'
        b'B=#VDKht_#_ay_rxzCIQQzjHo^Y6Q@p8sDB+p4bW-x={F1PNF$CYYOuv}aVj4k48Qt{`0`gkZ98e?XPaQg9n_Vcj@&_jB?z%VP!R'
        b'gLbu~P@Hgulw2nK#rW!+XKE1K(lH_1-jz~gyr^NS|E$4sVx-`P_q4o64AF}*+8(dkvz3WKaWD73W3c!}g0Yr7j4k-A84AkvlakHE'
        b'&f#X)%qSo!p33U8xxB&?kg;6;W>>~K*UVUBQ8dI{)T%t)o*^r(IiWJD49$(o-bT&#uX~T<Nff&_;-WTuxLvjVL+hZjxm(lR{GR5I'
        b'D(j0Hdx3$8wc0Y8g~Nj01Al;w)gZ?!q1~-sn)|Dm>w?tu_HMq#bN17NLtUy~hqBqBIX45D-5WzcCIe*JCM|P*L^`L*R(=@?!Tm9`'
        b'>%gbIKDv1jkK^|iYI47fvbjC31OLQ66HRl+mDcC!UMT2MO&di0*|YOoPcW()qAKWoA<C|e&ab{c7_HvNc=`_VZ+L+Uwq+={E^4D~'
        b'e>n&xt0#;0emTV}TGu4Ad@_o3snk^M0}+?sqVfM@6nsV<vHJyL;OXBRDM^~;X=K4wx4k+72nbAe{;PZPm(g7HX7$rzBezKUrE=i+'
        b';e`=gGo7C=UKuMjavOvl`%B$XUq%9`fu|#kIuYlg^9zE}8-vj;315a6QUgz8UMHPz6tA2Hk-rrpU0D(%NAOR3!H12z0ULL{pY*LK'
        b'oD{uOR!EsnMp<6~iDcxq=Py@IpU2eZ@4(~n4r+G^%}mX`Lguej_P(Ghq#pmVdWF)uLX#+4Mddq`%+!z5cdiEpxd-Y6YydUlxXoN)'
        b'S@R1jz!ooq6OtR(5_XDaUa4rI2P2JHbU_~Cuo4(-DPg3<4yx+uof{9<I7mqj5kleuQ<q=AtH5&5nI+CIR639MGBRdrbzzwm@o@b$'
        b'zzL97QFg7;$P?8sl-Y}vc1nDw5OE%5q9<pRdNS$Drp;4#7B*+j)T^H-fcC)^-#n^dUi0~N^Z8$4cg>gq3B{&M=?u-U!2q*9H9<|5'
        b'$BG!aZJ|ftdZmje_J)aV3(%|HEMoOa&qK|8ln2cu3!7P8gqkHn>pw-yJ+An<5^+GEgq;&4-+c!q2>~FvgqdEwqL&HF-?OVaf3w62'
        b's{er_K+K5>nMy7z>YQ0Lh`K_`e&C38g>n@I9>of%RJkvZM;ZSb$j??TqQFB`tYb5NIFK2+Te^-cZzlK{p)#wyOl)QxfiI@hh*2I@'
        b'vrffF3UNsu7ai$e^1Tqee%*r^|7dQ=wv>-}CLI*yhYUqP!*cx#BN<<MKrGPAEWZT93e_$><t{@}LAyB8EfxYPGuNCE?O9naHqw{X'
        b'V%g5m4{X}B8CW7HGi)DtJh!}0$e~Zzo^KYOmnk^wg`Of^KV?$^z4U=c=jXq*tKe;~E00>ao++Ja-?Cn^bY<y7MC=L}d!@yarRxPx'
        b'RIzmFdGkYr@wmuLU#@B`p|*S>eKaQ&!V%zrGSK*~Bcd!(`mFB@+C4q;Cb9qZQT{`m8a3hd3?)>-dGAU|N<qT`^Hll%@}j>q^MCc?'
        b'$f>4lE|a`4iNZ7g;4N0Trpj?U)aDVPrc#TtU{^B;0;BlPgH!p}y+UY$#rWh)&9;{h7^RG<g)kdR3XVVt4;r~CW@&!ktKKyh<w`Z#'
        b'_a~31(+hM%5%3+ZNJ4KhMxTwcM7X5+mfwwdUh?4nT2eneD!@&%s0;q*fKeP>te<40<@^pWl)1wjtl<{R)XcbiSDe_ram3^H3ikM~'
        b'gZVOC-dyp+E^WAe!-$6yqWo7!h1Sm9eE&t2!KhW4wGrDdEqp|opRE}-skWbAldZIC!@;+3;d`1w6*v-K02V7gCgwXm!rB3GbKTD}'
        b'mNy$Yk&Awwp}B{4HPL?ah-XKzfJ?yw+Afj4xIo6@W>;Lq7jn|44aCducdr@oScPPki<s>H@%1k7O;yR`_<iLzO)ro~34NitH%*%s'
        b'aFY~lK-_IYNgv>DTObtF@3w)Kg6JY5pw{mu7j09lyEH{<OCL$v&@{BrRzzOiEugVt{mMgkk=3=LRYXyiRo-xab8cGP-{b%Pe6*aL'
        b'Gv_sD&YYRK=gioWgdWKNrJH$W<Yk5DsC;Wpmo#z7Xbasr>udUV0(y)Pz9slJ^wU2Hh;N|}b@77bAw=anpaZqQ$VMNz@`y}#L*jbA'
        b'_tca9Dye~-fc35I$M9)KpXetks_u#Yjo1U)7)*>)s<Y|~Dwy2GIj<+?Mt5#kuh$nc6r;XGt^2zE#fe{(_Me}KZMrWLpd9+b+{H}P'
        b't5JE((~tHuu_Z6ns~*9~1z1-!p993x`88p?cGm$L|G8dYd@r2QRsX(=R`mGox`KXK(e=^Tri6*>LWYu625;5|M;>w{{&ar-fb^KR'
        b'VO^&NU|sfJ(XgGMK6eu`2c$hwE_^S#^+|`n7C`v>mJEM$H)6M#UTiSTto9JL=~$}yfpRNBv)I+5=oGFz#q<Xx|0n6ImH(Zz89=Hu'
        b'Sb5QR?3F#-Y20LeD11%e{a>T}WT+Z9eW=>>KXc<!4?N5J+p0as*$aD2)_qk!0MG^0K8sbGHuC;&t35&Xi%1iDkq;L3pOGJN;V%XD'
        b'ACYu?ctl{&M$(Dl&jj}4NP2GgoWP!rq&vcY7uXLY>7?*Sf@^qBx}Ntvzm+ptvG7TO9g387hd&V5cOvPY@CkuE7D?|3zbpE#JGqDF'
        b'^mB{U<}v-#b!d+_L(ZSYO}Po8{)2oB?J*dBG8N10^YFUedrdva*F7JPf;ytaGHM)dcLeUA2+p_HxNYzM2b^yYLzs$RzZaLY1%5Me'
        b'27Zev`aRJ>tTRJn%6o6T{M4WJGE)ALgRc5Lp0oJ*=!cK|iHTwIdv|KCfEas1v#~ZgCe-;~N$l%;NNMVrTPJJ+mXL-0)z{mo*|u%N'
        b'z$AWXq&Cs>$iZ=4$hoJs-4u6<^U9)D$W7i!;*1|=2=q|wdc-diTLY*fc%^i1(W;8Xx@X2lSuZy$d|i9^w1pu27~C3u^}>k$RrkdB'
        b'JO<6UZ{Obk10vF|V-NJyFP+o7jZ&v!9`7WdeXl3~K+Y2r`lVAVuY;t9-Vo;>7{4=O-&1)J7K|t67`9On=SN3Y8|tXabC<`RAsI}R'
        b'2Sl$7^e`FqW}Q=ZLohDi<0s~rv}2y|Nl}?ydj{6xp3Tnnn?1G9cp^Ah4U5gh8$4TJbR)AB9_gIQL*7QYVYbGUJ7?V2aK`xjyk-SV'
        b'4vy9TYkqa<<1pI*2dn!2UpN5$qk0ixa3<H?zsK_l&gW%K0f~Gb0?Nx8qmjC}@pdkYeN~?Ok7l5}Pre7_m3TwL7H1cJ^tXMUX$uD<'
        b'VMLx-Sgj%qE(&stiF?+$aYMwz>=O%_F&|5H_;}kVBW*wbzqjqX(PMB@$SYO)!nL;|570q&2BdFm9CP7YXX*p2mt^2$C||R1eB2j%'
        b'DzE$FPZ`_>r~*RwJ&7CCqh+UHT(H8IgZR<qh&&i#P*hfr{@7#i1E`@lghz4=8I&)fuQ$Ws&A|UR1fo7p^^A>wU1S}4g#UXThQ?uf'
        b'$JXle{~PA7;yi;2KE6quC-mFDM=<y(XGjtG$uDd2z1zb`GgnOPPv<wiAU&3z2MXHYEA{IRplZi}7l;Z205Z~?6%znz)eBJo#Uuhy'
        b'!2!k5%X<LMFpG-7AwS3&sBwc>$CPekVtQi6$P>|fcMs3;EU{Mu(ywW_n0>uxcE9NN63PNSeki-OM-zgw+lMNz_x-8IAgVT+1_ire'
        b'4?k@oRAZ^VXj9ZtkREBo+4kPZ9)X`HGjP=J6AL4c^w1vo@1Bz=K=Vv-|4+SV8***_&;0xD<@3jOKK4oVK{?<3`BuLApp@U6>ExZ&'
        b'v*oUj_Bc7eMr#@273uoRoMJ34uy1Ptd9zyiP^vka_bskgrl6*He`2-rVczen_Wa1cyeAUWkbSfVb6(_&9z*6kj4kdlIcA$2M*80Z'
        b'`{FoAQ3RwUd`Vz8jb}a*$t<n9F!sLvPrY@uy<9PswyZI340nvG`AQ_#!I_@O3rqBz_6SOcxGZikhSL}}pl7GZ-Zi_&M8uV=CV_7J'
        b'0g*%+LUMaL=C{U~lrh%!6Q<+mfz4;`lbF0(Q&CLeZ+fPa>vg;#Q$DOR75$!+M5&0}NNgt3nrl6co8NR$Q)lC=6?ScO#rpkr!ZsV@'
        b'xksE&P{0XRZIb$Rc_v`wTk1>Pa^uQ94rLSQhlX;wvr5AkH6h5=6eHcVDQdkgkD0vg<$8~@2|$Z_gn~x-I@nw_2(E~_uR>Aqpxl&w'
        b'pNV+Sy7%*}47thrp7D`htFpLAg;oALYre)>RBTl)E66aQ!lGs3PI#DLY;HwN`Kq%v6`8Chb#7e4reo4`eGm7N7Bb6!Q)MAs<{t3^'
        b'94Q9GT%f{<jo1{|tlq4?n~{gc=;GF|5R89?&UAdlzW=7}ZGm}k^?GB$9tXG3P_A(}7FHb<L_Y=_QsT7Dn;BENeiEC~%f#_kjQzA5'
        b'gn$U0u~YZ(R$0|`0X;Z<li<9HoHbvwQ}zJ5=&?Jg2JeQ^r>MEs+9uZr-3%d8>A^AkI|tgRqL(W~clb;eyzFCWVP<U;d%T;+G2S{b'
        b'ZbxSbUlalxzyWIXG%?qzo`d^woIQvDv5=Ox9?`u|{IVzB>1LDmSoORnTh4h&dk4<zXLDZMnY=~g+)#V=>Y^An)IEEB*%$N-YU*Xi'
        b'MBf$d(6e#fRf(&kyWfw&X+z>zZ=-zfqr(T2UU^H&B<*}lsqOb-VgL!R_ov>FVrvtBV#N8fCDFanEg|z{p7%z=SB3v)Su`rU_nz#P'
        b'ZXnE}<O=r8Uen@Jh7wAnlNWaOsQ*Uu$rX;h*PJg&klQ`UoRWwqjQMkl_WoD^l(6_z;k$cHv8R@E%|%fwR6D+u_a`g;-Z<S)LVvO%'
        b'sVM+^u&SGxY~tb>!ces3VF~oY$DS%EmOyo+F1kTxQ5eh`XbNT?hXk0#ryTPi)@=|>k~xmWrz-cCKu7cEATQW}6XXZtD@ouhNtyVc'
        b'>#=UY3qz2(xe>l$R!;Y)*2~z6ZjR$M4<LU^$3OCTrGW10*)h5=B>ofAJ2TMhG>wKrk5!<~(Z{=c2+wpI=bd$Ac3o~aF!#$Mmp;As'
        b'&dG5u-9H`JxWZsW)}U?w!HEOwqsPxjmvb*L3Qruy?-jPW4Rtx)&`rbugpND2+-2-G6)y|?A$sf%_HVk8uLv7Rk;Rg}^zO>@p2Q~T'
        b'ToXBXA8q22`AzE;z>$xE#L$RLObGjrHmzD8%LAl|;&uxq8OY*{F!*TG=;~;o2rk*yyIYL<gghmq^GbyV!h3NfDZ;TmE-9{FIGT88'
        b'G@2ei*IosZO>H2m?#J9xkMD65hW*!=$M@(CGf~xpP0y>Iy?VMT(@fYJu<`?htsYAvt25@5y9xRwjNz+IG36B~Mj=DclQ4|&KvSsT'
        b'd}_n@EY)p<6**1#mD0*92F~E+<W+H4k|{NAX|;(;Qqorie&{?yT-6idEux*m;|=X-Ai~vH_3Q<6PouW#K@&)r?trAthfTkd+VGn0'
        b'Z3&~iny<APkcD{emy9wq?$|<QY8*lTQ((W@&2c%5ijisB>u1Q2C&6!#4>I3kG{;x5>VAS=3pm=B8VA(z7pNpk|GOhDOKkr{{)PMr'
        b'JK`D<9;N{vzJT#mZH4hX#`$Vc8=GK2(>UK|l>SuUd~VdnUj^Nt5qYIHp$J2MFFv}K@M@{5MJT+yZ!3a*780)@*nL7-Ex{=FrxR6w'
        b'7Z?;*1AX`ON1={3LPt|gzVn$d-KU|#S5ToUD6su7z?U>B6un>I{Bh7+_!*4z$D=v>1U3YvYr^ZqX8yV(GRD~tdHiiCy%y3M&Yy_J'
        b'uox<BMPsNJ*p}TO9&qi*31T=K@_h)!S&%pa?8D^$raB|R<o_BLzN!Q>`A=p-t=9#18+652IUwiT>Ng0RM{vEen?Fl<q*KFI6bj0{'
        b'o7d{q`Y*-TKwj?#M&;GkSGfh&wVRPa)y(x0-J^uJgPI|ux1fpl5W3}rH;t<Lqv*P8GiqO>m4shF4i<|EFGtbOf!?=X%-2Ym1TSZ('
        b'+90@|+|BFt>V{AK;&pK72_v(-nmQCX@JRu4m5ar}bD~uljU&#hudgZ>*x&DtXemH76@<+puz8Sy`-!Z|E6_4}^~x?qARLjv!~qor'
        b'>#LwWCSmk<ux6QSh^i$5`&)4^I;yG&jk)X(AUZMxYJY|3Rw`$=NB;s7w@qJ<u8v@?dGLD)eM@j<L4w!tnx(5_bZZINnpe{a`00c('
        b'XF<QSq1lxhmI}`mTn_?hyt?auMBK)OzY|=>2%ZzgyZx>QP#@~9VNQ?uoy`zA=S*H*riY-7SZc<@pq+<xpq)=n;hrlu5#jqWhAgX-'
        b'7}Dk9&QH>2ib{IYGw5Fyl=aV98ll2OJY@S>KuhmIv1n2=5~dF^WVPwoTvh5Dn@s+;OwXI_?U0GsSM?o$T|m{fSSIYN`w>-SdUmis'
        b'g~WFD+CWMFS0o*0110^3NIKpIO8R$^bfOKE^b3*nTpK9qqmgun?IVFbA4w<KP6@`(L+M(R@A)~LiNHo*k^nOczYjP&7Xj(68WPyQ'
        b'N76l2?+ENik@TLbW60<F+@Wef%a>T{0itRamSl!s;lo&}c~LnGz8jdNEY&=voF}SwVazM3hY4FXR_-9^*F`y-K^BQ{0KnzU*=o;s'
        b'>_CX)76PH!t_$V;gsl@ximUc~#J&~cl*?@Y7RrwiwwIwzO{)1<ymvCPdF&DSP7pHHXdwGBWFqmiAv8#i=osB3(WJ}K2dnAGbP|3O'
        b'`ih-iT&*PN&jr>Ofl2~ygH3m%`t8{C1}H=}jiyLpmhEGK_kDr-I*evXn?ROcg4*hbwjP^%9aY-}$;opsKuz0w0{e<M3oR8!{;<nW'
        b'6Se@hFb<U+6WEtRNRHG~&MxX?NCD!xm(w^qDD-zXH5gJjUq<O(w<27OK}X`C+o1L7yl*))QPn4~&xDwCo?Gaw8+ATF!S3slJJA84'
        b'Ve&yy-o|O@E*P*A*?MZBg;&sAI|Q~oGyr??$mn!}LocGWRc!*s`#aFQwn6(jyl)isRSoGx-uD&i3z$-Ih)F<``4x=H5cZ&Ng#IW5'
        b'=Y&K8n$xQS`@0CH?z0^e%Lh=KuOLM8{v)WJmju=(q9j#9^8)YxD;k>{AWx#Py(qB1i8OGq>Up5Mxgnl-k3r7N!W)Il4GM;Hx-3aD'
        b'Z&0pDlmEvwL1J*iFW_35s<lw>fe=T;(Q5?Pv{2o{Ax{5@Ck@ydwdpyTKdx!j8j48=$W=E8TdBauHFaJf=-&%WE;K<uF0l7SMvy=+'
        b'7uZCgw%5Z;k?u1s6ggvAHRKh0{c_NacqLYO1u#yp7FY%JIYd7qxF&|`G~<1;)TSFmI0yBz=>kzTUtsiAqXJ8ZfK4L<%EOG(nZBj!'
        b'H!x;A6fvp5bk7p>LxPjD!1OpdjMXi#dRJhtcX8ZrHJpT=DY$;_^6P)g#hvoDOV(aTq{1O|Xf!{Cr=zj{(1lQ(LfO)Q1&C>uvZVkE'
        b'=t9Jj3c9oe$ZaGfQrt^aco6#kLWI*%wj_c5XP17xEkR&E74y<4+Z2KQq>EF^=*a^6w=NMsQ>*d>_KXOSETJa}?8z=fRRdM41=s&{'
        b')jhNuhR5p{G6|YgYFmSxi2<r%(zordhdzC#-Ao>=qIYLKBw+zzip*B$p)Ie*pm^BqU&L{yp+P#`61ox1=^*s~Px|LE8>#O`cTz1A'
        b';~ME2b1U(n3uB}~M-7ft+k}DzM+flPma@1TBu))4XY}GDHWiLz_!Ap3S#bUBi;NV7ro(t;91{;z6>+mVeBBu8V&X+VO4G2K<7)Gr'
        b'xw$m*$6@T~Vsgiw&i}>s9mo`@57I($AT}#dKdA|?i#-5<uj*f8cihi*8~@hL3=dE}r0e65c+aIa<fe*abCYYxWvV=F;npt8$?nIP'
        b'0SUT8H;h0Y1`w3dL%BAi`5Az=V;NF2Q;a?_eow^iAj>8S#<d}2$W&3C6{%$#u5~9wetC8a+ae~;MHF*r^cjiqwJyJRf=NrFJ05R#'
        b'o5|XY9^x1O5C#o(<UDhIt~JyAVBLRpRrd49?5RNp7rB9@G;U4hIRi%_Cgny^hYT6i+AC0u{NW%Q*?XdI@PaPS-XW9py=@uD$svfr'
        b'x$jloi1_qw?C#6$@<_4f)ufan7o?C<l3Z{fDJ94SYEp`m3nuc@7S?U+MwZ4W7P@}d<<UP?`yMlu*FSsA_cn_EdhgB%`(T&Bu)$;<'
        b'O8rta-=c>LWyAQ=i~r(@A=BPl2ITN?2s929tPb60oZHnySU)DLu~Lt2fnlcH@?^J5*JX{x3^O$hl@l+u>ZfPTGi2pZrsCqV-BR5Y'
        b'iFz?+(k=MK2IPwG5<^l?1p&xusN=nx4F;-OnVo7@@ZOcxN-ghws#=*A(Mx$RU#*nzUT?MM5?j)3ufNMWy2IB6ls<EZE$$BgEU=Gt'
        b'+f{d1dw2K>u-0z-qTB4^ZcrQH9Ch6d%6%GB#Y$5tX(}aVD`w+?2e19|F13dUjNJ9|gZv8g^u*u(N6`nE3-Up0E~PjxAGjkRdTb)-'
        b'-(j7mM9%vZq{9z`M7|jkRlh;rf>RUn<`yBh`TJ1TqZpFYL9Q-=L@2fCOZLYg$LZDnJ3!$e-VvA{2LTVYy8PW~oblseFQ-V?l2$C7'
        b'f~0R2GoB3gS`}GaoGK|Jx-WaC@bAF_ofwh>TNMd)fTG*SAc`)SbJI1@<v*qe9ux{Tq(i${+6e=fj(M6I(>=#x(Y?_IRW$y--=Ik6'
        b'j%fgHgagoYy_-|z;SDk@?gXl#NJo`iO;E3f^Q^)0Gst<2?$V9Ep)TKWSJ_MnXiQ;2kN27sY%n;7BdrsvZVJZlcI)wovozzscaK;V'
        b'`5BOe8IkjFV`~u2YhoDf`Uc#%GuWG_$e*X8CY4|}#ffED{@lfNpbv(8EXCx*Za~S!RONY|D!}5iG@MHeSXO|hyQfRE(NHi1Kp2c}'
        b'lCJV@_!GhSa*$J<+Hsx$hNs7;abxHd{dXGwd%W!R|187lVNp-#k2OE`Z4Xg>Fp=*bK^8xiXvHI{jF{^WLBD>sO$|#jfR}wHAWBTw'
        b')M-vY<e88IWDC3z5p2RV-yedJ+dsT_Uv<K2-usv8glBngsJiJZH(vL6aGDz=kF7O9X_&y=cyEKkRUB+`2Zs=`MSd?vzt4im?Z*3d'
        b'??yQVDCdI96GYBhe-<KO`H)FU5%z!rs(ysrI@`V0^}tD?`8vzJoVf7ULaKRMlDk^DJk=ayFZ$Uv2PTzEe<37+JodY!14t<QP;kwJ'
        b'+?7?x-x=@QTCKFCnw7lIj_@!fxMl={2gJKYqFHk`GHZ%Lmn${sk9*8UV=f(3SAulw;vk`@LOzLI8YnEmWas+kcOl1r$YrW45%NmK'
        b'qaxz_=E!L`pJJ9=&DEF3Wd;ei-`no&ZZL6F`7_Ah>;5f7_&%(B1&S?+9-AT$VJXFb+g}`$QXx&*{6XYBHP2Bgn+vYG<4s(2O7VmH'
        b'EA+vl(LHwuWI<9_cl}iv=<G~=X50gr=KE6`80L-4hOpk_S7J1d!M_9+*m@m!NRXuO2u3RCdSthWJQ($5huahWMo8H*jq#+ah^o&8'
        b'v<&F2bHoo+un0v!3f?7gOnfFQ-rd63pE^O@igKKGJ+#|)R*ZFM?NU2%7-D&a+|NnNCZ^XO3KDvMs9lUvF!i$D6C~(}A3%1r)5JYx'
        b'e?xSt8n_F)Z32dwxM$FZI})>cr+DXRa+<!dyw}Nb8=0xV$_FNh&*x^y0{*+|)3>b@9N(GS-x=fWkAO;u4fE#hYL&#?p*~KTUjl(h'
        b'HNPm9N}X)G{IX)Xd&C|2W1h(meZMv1NrIW;*J4HQ2qh_+t6NoWRqX{GnLZ<`_IbTl4EiubYC1k#yTrc!4(deB3#M3U_o9Zypc*oC'
        b'OvXvAB0a5GIfFLn>ow~&&`JR$Qss8;uKJzZMHGHy^5Dw~Zs@W*mZ8(#>%F*MAG73Py4G)&>QP*%hiOeFoXq^t<=Xjn)!p!@pq_Vw'
        b'{WfGK@`$_@jI!#Bh%5kFSL7`DGQ{hp<LB8Im~ngOBLuH~iu2+}+;HaK>V&d|xeU>1PG7jT-z)Usu3epDFO)c_|0}e=IPJ5{)P-w7'
        b'=4yXy%<Wc0E*K#9bBa^%hmO7<>U%%r8xBQ;3fJ?UaHKXbJLy-Xr=R2${`M3&TTv4s|1W2&81F)H>Tu}jV5n~}<U0~_9YMA0p6KM$'
        b'p0b;9UUU|~&%*{t-3@_}A$mB;E7IL3-HQJ96i?bl)a0Q9J>*C<X1{rdj>L0;cA25n1Bz4Kp`+cQzV483SID(X9M@Bwynb?R#Q+(3'
        b'<n1c>Wt^eQAq9s9nZyi`{&U1H@7C|N*AP0|6zXdV`8*+)M{F+()&I0Bi9t_DT*U}+a59pCYh$AYnm^gENI!h}u!7fbL~Zx~gAnhv'
        b'+ArRT$ZcO>BHkGi-I~rpEto8rF}*YC1(SAzAK5oI0Cj5&lp$+_`fa*U+1d9(2xz+?pm8w>+_e}ad_E52mlOxAIIlCINPjNMBN+nm'
        b'3HiuB2a3yO@iPIy%^xbu5`hAglm8E(LqO$Yu_)&c6)p)CzdRzrrZ{34NslCPNnpz5^1#oj4!OKf17p&S2#{bB0-p<+4yms=gkBGy'
        b'6KdbKs5^b%?y@G|Un$--&kp6T?C#JcQy@d}6!tjbTvXq@q`0GYGV;8#p*GM@VZP6H_4bw^ml-SV+wY9-_%TAa7kBj#fZO3lX6xvs'
        b'F>Hz`1Z)8j0s;@+6=g2uKeNn!_eB(VvPI@SHdvd?5NQ;v3&C!c7AdKv<}qK4D(rHxV(XHTCGaO`f`68W4#?hWTy6h1<u*-!Z@D`d'
        b'x1;I4y3t*pw3*Gzg3<w|hDCn7+1jnZEX}U92-~$(8l^Wa=RRG}5XIrzcY2~==#R_1I|do)?fi;zd(~Z7_Q4|>zLfBk;_u;Q;WXsi'
        b'VF<Txy^-jq{~-)S*RW7B`nH(=y)4naUQKN}aR24aimjVQHo>3ZgYeI~kP}At+KBzkZT*AKbHmv$N~*pQu+<dehT{29p`8BC(%17D'
        b'$&->Q;DiNlimnv@nx=l9aP8aW(9djE2Z;gXI!2s;$u$>E-~$STeI$)PDXU$RxTI_?)j8|<jEM2LUl~{A-CS^3u6}`t__kzXM!yvp'
        b'dR4-wdVH1g@B02#%G1yS3KsCBOeEkBD6zG%H&Gvu=r()cYhg@IG<tTWSxj2iuEqT<1w;elqBmbNe3Kz;1QxVF%^5OvI^axiVN^xO'
        b'nz6}Q*dpJuLNi{xX!v6@ZeB4Px08ZRbgsHyB{ky}RPmyi%#&LbTVHOFGQ_HQ!j_C7Ipg(-EN~8DD#uDdTX1I9pL|B~{1W|SH5au$'
        b'7ENqv)atpnP(-F(<Bx~j7AB#jVlZ_T6@1&<KGVDFSYjxUc>P86ad6)*@zG9Cl&c@5>e{+O`-9Pmhf7<#IuB<CX(rl}k1h4g*VCe3'
        b'wKRm>MD(u3l_C<#GmL~$YwTNw=c^t6rr#A_B<Yg^7NieGH<r5oghaJ2x}nsbf2%8+{z=fhGnhC$K)7m9f$gFghjl|2BRw6B_elRf'
        b'XVS3Vy?R(wEnB2W&p8l3ctUaF@K9o6NHaV*_{x^Z`vceuw}nTD8L}hkrgYMNT;f)yY<}jdds<5Fb61OFjKA;Nub%+N1hVWaQ!32H'
        b'N4pq_KEuw*%q#4RK+&Y5q2vu@flsQ=m{{)qjE&lbY@;)%DgsLhPG-J@qXR?)kzQc+)F*C$SjFBAFtNx?j}%9PW<%9AfxQtx^-@uo'
        b'aQ14z#OcxD`Yy=#<UKQT_>yoLv0jk4-5KIPp`be<Cr*~gfnHf{`T~U40ZExBO?~2S_!Nw;>V`1xYfAU8aUbD&D|3*EOPwuuJ=BE}'
        b'Sx!yecz6&-snHw6Z@O7o8-PU<d5XZtLU*Wm`SkaDB%`fl7o5tuc+TsIZbfshWk%QZ<BV;9?2)*pb&2Y;Jrq6lvZ0r<9~NIxoD$UO'
        b'xH~__ebpSZd3g_wT<9i54X-vBEs5pyC1Lv8IgNNsC~*@gV2RnsD3E;y|5D%EyP@{|{^5^amG%Cq-r2jsKJ9LE_qvY3lsS{(1WrW6'
        b'm3Sg+pT_?#>6(c8^~t)9$uRT|N=6*Z!TNJ>e-7cHF#EC_o*Xj#rSM1;b008+4`>uY$7Mw=*q8t8w_=FGMBeZ?p|=*0H_O)(VH<Xp'
        b'H|%#1RTlIm>DW<e|52ugN;8g<*JsGSpW~jNVt)K;?)~;S%FOQ9#?G~dNob>-N6snuV^<kszaFi2O0jf*aV|e}^{W0dLk7!c<5rf)'
        b'Z2C>`S^M*J4^SL>g5%do`n}V2HKf&xqx(l4KG@}Bxueyji6uHS`jHD>Y&4mQIPXH14c)D4_7k_vip+hz{Ny-B<#bsh_Zo&PnE0%k'
        b'dbRt;+<a8cgeHL4$ZUM{+O^Ckw^@;sfuv8{H34ur6c8;M<y+&~<pELBl>2-^K&|T*Dq&3O{C{KQiLBn6J(9qecj?mt2DJ{MGE8>D'
        b'c0(A$9ULIWG?v}DYXI+&q$$e!g-2w=C*~HFKl>2-=b&X*kSj%@tx}FXz$H`Vjt5{&2&ts*`n4nZ{VZ-cj+|Hoz5xpDzBpWFJu%Fz'
        b'$kJ|^dO0xz1@q*N-PmvX`zuGGj-g#s_T4pg({24r`?<Fn&URIBzm#H@Ud`2|#1Y|StRdUIy?ix_AF+Qm%`^>=I}YIoSkZBZ%`D3M'
        b'pYAVyGNoco%H}h=PksP~xkar-8`F#zt_&`%k18|<igfocd&Z=VQXjt-`0Q@K7dPex?de!Qi7}F*c?j}$2Nd`AQpnE;RHddb&Z$QM'
        b'VshRfVBeXJf3$xEQT3rPT6mTIAJCz)Q!28qZk|}Y-OQ%sTJ{&`%$Cq2LQ2DLm_YTcSmtHq8*Nw!ZXY0BZ3wyHvjXT9aRhKd^Y&u4'
        b'Xc1=n2vQ`Dlk>2uQ-Z-T(=;EmeHba7hlN4;JfILKsor{JhAiAG7{Bf)`WQE9wSGwwlZgCP?G}BvW(OZ9U=8ykD-XLN2c<&oi6P#*'
        b'f>CuIz!?%4Ql~lIL}9h{eY1lA{TBoy+Pn@2#^q5stG?;rv@`8R7;6l2D`x6fd}?KX6-;|3Z43KAFs&Z_X-9wFupI9|UNMuSbOYB0'
        b'WWMyEs|+<WI!j<f9rmpgijtqIT~e%No(It&>E>vuFlxDlo>7+--3q*O*IPmb{_;Z^e@FM{J0!8P2PZ8gX(31pB(Tx@t_I$P%`7@>'
        b'|0~AG$^zJqHF4fP3PeaI38Xe)lD$VX-ou(C8PH|n$DQjxBKjv|l|T0`G4xN79`oY8Z_54NiGg0BC|R!_#Y6{o-rfyN60@~zuh1Wr'
        b'0I8dSJy0A!{AT|ifl2D^{V8cpphs~1y|cJN{U+J)nmP>w(Wl|r+GPW@=v%Y6jJ_e1&AL@~@NSXzes3=@o+o3(*abHA=oRr2lLVtd'
        b'v*nZdA}{V-C2>|sK&HH0u5gxX3d)fus}Cg18eOL_Kz|@fniJS1I8NgpI_p(Q)M^PoMe5u_^(Vgsf@<#@6pBZpnR~9RL#X?xvv9#K'
        b'CbQ8p`UTlw>3oX_Psi3L=P?g8ud*idS(_wTHVKxPg>CW;W-GFCG`;&YR%O%ry`QhkmRpOOn52aXqisSzxA5tnz`7UY_8dtr!SBWD'
        b'{@R)4mhXtOxduA3axFRL7cDCSB(bz07FlXkgpo<avM!RuY-`bDDAe;?XJC75#1=BKR@*@<fjzyq(^cEKE?bjF=usFAKYeg?KEY}4'
        b'w^Vg<E2FGh3%jw?>cH4wC%3|~4bI9=kT-*}#7*dBdLH&dW7P@4s=c4Ij`<8Fo^BQglIcUwokTlkQzsLRymRG7zW-YqI*-2I$;2Sr'
        b'?PNr7Mo%XSGB*!9a+AHU!_T4DK!s%BNg470Bl#hcv8qXdOh!6|-7T7tbV_wG&JZYwFbeN84|8e9_W&v;F{g8bedrd)$$d9E`u*s3'
        b'KOM1cS|lC*<QLGp)=iyyQWF~FyvEM{-$(M;KXi7Hs6j%s7xNT5(t+9|XlU<t0~)82@^(?*U({{>(U=_IWtfSaZg3-~0nI_z_73E@'
        b'?$CskbBf^;aI}YUWG>SCQ<VQgHUQh5@jIK#I!(Fb@BQqZ-1yr+521nMj*(`rR+t>L@l3nNi{G=X_ckbaLKC?Hh;Ck3H6lJ?Oe8_6'
        b'2#Im1U5?2Lw8(ylGOY+RDuN;jdLuSljy<svdx#+;C8i?6c)Z=OMRPV2ktVuK`s3(KA#=|FwgzPPf}Y?{i2k*YDGA^7P7v;bXqNZ<'
        b'FuVN=OrI8`+fR%2{YN|7`@QI)FuIKnXJ*8Svvsi@$;Od09VTdWbpU~iAz!C$luJ<eHZ)k0rc^c>QzZ0rQM}j0+legSO%<T%M0+HD'
        b'ubjAv=}x#}IyG3j@pOj@$50Ge%|!syXnu0?e&<UTOnO3t$zUR`0aU9vrOR#)V1?D~ejS=^SIT&7^IN;z&(vP<=&{sBQvZw?`yHhJ'
        b'>A>M!QHYkho>8y4n<hi*nK*9h<}!S4vSA&yYUZz)$<VhPjh<~D%~j?mXJt{FVu|o$Snjc`zMDOS`80CyCL8}?U>Vs}Of6MX_Oh5X'
        b'%6D!T69c@`wXs9AbP_{24EGZC8Sp6366fk5tMkpB{#c@KT?dwM4rb@tisn+7(E&vTx|>}J@xs1{If^RGYgbW{h~c<&W(SIe`yl34'
        b'7V8U2s7<d+4RusOA+<D~E0RiqKq|j3St4JzL{pS2E%s*(-h_dOPEyeeX`)ou0ZnOPZgQChMHNrP<Tshgwn-q817P5L5Fr3eeeTEb'
        b'2XKO-xvDHg4^ezt4Bad?(@ztA77x61O@$MW%P{<=J#>@AvC`CbG~8^;pYj6Kfu(@*u9;A7>jn(}|Ft#x$9rw5=iItCKrwW6IQ%yu'
        b'*FS`dbD%J~Lwvs+<M+K%rWG`X4V+g{KaVppx=;03hSr-g2uvfvkY2CRl)w%jvnN@e+l6u3Aa&$<v&>w7MCB~fj?7Xl&$yfce+r-3'
        b'brSuXnUG*gkXC;=(RkiZk~7KtD3Z(|^QFj+_o2X$rj=NxUlRG~U|hA!M8eO@BMyb;K_|3RSh`D-;Y7DlXF1KJdc_^f?{}G~%G!UM'
        b'C<6>ERTX7QR@bU@89$~!2;k`%06J$DsEXC!Onf@*C!=PP^P<S8404{-*{>aWNO345y$S#iWx!dJ?gr=u87JLPW$O}7vUr%+2kcfE'
        b'qvYl<9v~ME_u#I6WV3pDpP!k`Ma3~>45yj3Wd><BuKn3ClQM8}lY$=P6a^V_jaF0mH$PWMbGl#Ki6}<tnzf6|uGG)0*{42Fn<#xH'
        b'uhGiQESIhSJ_Bkc(IqS74Hoq-i9Wt^zn%akYs94BD18YhH*gvNTR037sMK1DyXw#&OuFANO7)6Mur=s?0^$*H@XTMVPX8W-V#Ipz'
        b'NMP6H-`Pe4&bu;gCVgHoMQb*#Xf;hK^-n2bk_Kq+k$S`0`oY8U!3X6i(pQGBm(v(b8dJ93e(`$v)5xAx5z)YIFnj?hPAIPR{jg^f'
        b'RD?_}PlrvVOVbs|ZWdcH@5SYz+P8B#)7wJMA(?m9Gc=Bwi!$f@1pL;SMJ=s(2qVv_2)ggRcBl#R4d%Nzwl6#U5s!)m3DAuUb2cqC'
        b'Q^iFE#VcyFd5$P39$dD*d8M8+m<C0C#Q1xEgrCFaHJi}4Nh_f-TccL~d&~zg`u-UxqOg?71g*mgKME8}ighVVC?MmhmqE_WM*ig<'
        b'6V&JKIw<Vv;lPMpv1ZBTCGh9u62<bRCA~kH%3?+85NQLEMSGeA7J%?}I$cIITE~2<nEUkQ=ie|M4iuBO%L*<2gQQ8vmo~JQWN1uf'
        b'JcyXX$9)F^3x_rR8dox^lc?pgF%UrMe+roT&1>Q}1YcjkWkqa>7GnlsytZ5$XY2|vgoiX>joRu)sfnyiRS|3;0AnXo_1Eis0Z%lx'
        b'BlzQpUa^(C%qi-c16#S1oFY9<PpJ7j>P2^)ZtZxXSh9d?;;P2a8kZ-)dGC6pm9_Dl)DSr{H77T)uLL~koquY4%F*h;K=j5}?u%(0'
        b'sZlh!VQ(}cJFC;L-CA4Q!Zk=WA&pn_6P(6U&O?vK5@Tdc;%73$Kel|rb*j`nsmZw@=eY@;aWdC8K3*CZ<96=e!Yk>uw+9c6y{+Yo'
        b'XgKM-O`5k<_<;=9+Q7jgleAK;qK^@nNov4`wXmx*n~UJ|9h|N3#N9{cDoG-$ze2J0R&S%+(5U(3f~OdARSldygxR0N%vKYr+4QB>'
        b'B-K}*@FF)OdUYek5NI<&*1>I&?UbvBdG{UjF-e}pl80s6=GJ?l^iqFf=}EEK-tPL!GloWSSA=}%Ek&;09E|$%O}$mG<OqDJV>hEj'
        b'0hJK$yc-w-geUePguofm&9m9e028k#cmnt82N|iRW{VSXNq|k{G)~~A*j2rRHGo=LDaHpK^BW_Uq&CF3(gVD-GBu81^?~tk&&dFc'
        b'HTTDG=uW*`<W_a}1x}(*S3C${nhhz%F@5(3eD?=*Ck5{qPlmNt2cV3XV#7n4YKwg{(j|1a1cq=a0>G>h5j65r1CxNcwW)C+$d|Q4'
        b'Z7TA{AS&P|u;G04D)E*8-IpsBE<C_QyQOYDKXl8Pwk5*+fk%L*6tT+|-t4eSFf}DOyx7xMJ4$RCUV>Hc|H2*Ruwc9t=Pfv&8e5|n'
        b'y&=3xr6ff4&}EH+*SP@;YIzI6#3ycbZr|duNK<67t_vM~7dkvr1G<6TsD%+$$Kwm$I%tH7GNo&zgNcWsLw1RK(7C<-)o9)lZFmDY'
        b'Rs+_z{@r5xxvPogRi8)VMsYC_Grz&G!K*bG|JK1Iz}W&En;|uGw%ohl;PI{m*1~i6j@VeBh|F&%8tHb7Iwy)*>6jwjnB^0h;S(F>'
        b'u|SpR)`dI<ND|%8kP~pWHU!sR*;Y>tb}2kkDVd9F#HToUW>2m(OLKEvese2x%^y(ecI=pUXz=(7rrj|7%%EXIPQAjTCro<Tw(XQ5'
        b'gUW0q=v0i9;s>Nia==D^7R*W$sgL?H-u1o@X~g-_u4q5=l1VDdLf0N-HZ^AM7v-g>HUBVf@5m){KwkPvl15to)PWrSfWDB9coDB6'
        b'YBwWMf~25fx3W&~4#l00FFAl;LIGEn3F<>Pj;WAPL%HsVT^+i<Q09t5b&VRI`ODf2(FKTJsaK*vGP>Uj56jfgU$vq5+8~EC2hFFO'
        b'SL7-I>;1|2xGVx^6$${4na``qTe->};sA0TOMe^LM}Cbb9S8oXaZ)D_DEMgovAx$KeB!`tK2HyFlW4yy{lJG}icXodp2qEOO>`>_'
        b'-VKJQDOj$ki)PDN@08Wb!uP#L5BkneF71~}KSNYqEPyEI|A5MiL#99E-Ti(H<Dh=OY|LqWzmm>*LNa9yVR_dZ^({fCU{E*ei4<6m'
        b'ZFSV9_^H1A-nv2W`GnGAdVJd_njWGNA1#7r8}P=sMk$a?);<j^)iFIOu9fZ|0vu<TByg+^&oAuso}XNjb?PRFim(dEWAX2VVrAt8'
        b'P9ilJD5uDjD$iWrqyUOs2mEQiG)a~xaUDUJ@1b;W;T(;rPyfUaG#u{G1@r}t6#GX%5|DFR+let-UmottMs=7t=r<)@e%g!O>$2>7'
        b';Z>P)oZpDBvqf072&?=|5&`WY0^bTx%7&k3=&^4BPp|X2zV%wCOv=iY+h<DLN?xi@y|5r^#r&uX^WCO8Nyj#~yxcv}wb@G&Qt=T8'
        b'=t&FI^GU0ce)p>fFv+>TKl`jv1bP_~^dfhz`!u6}yK0|<qZsShl!}AUcwx|20DAh;Nfx))nygS$*T=-ss?P*$cyi&z_Wmfs_g#D0'
        b'nXBsbtGsu}neEKV`YGql7~S?Cn2Wj@WcW0Q)BWP@<W*}<*)9oV^VAJp?_T3t@8$LK+J+(gGs##$1DC}cwIcR(T*)yOi{NN1+9ZaZ'
        b'jw=n1*#O<jqzN!#P+d-*l@}EJ)O@MnV@(7c5LWgb?8&u1bELk2lXLU*sJaJeY4rnz>0TzGNVhPj?BY?A7j>!oNO0Zf1O9pvokp_C'
        b'XA8zoBlP(M0a!~h-J1d|hdOk_tyD=d@#4pB`b*KbRY$v~cY~FzRIem0_jwC_?e<$BFQBnash~fgdL*Nt3+^)}Z6a)iytq6mLs@gB'
        b'Yk$gWl*8%OgFN>p$y|D$sNtitVOu)~hiyN`>8JSqgg&x+BgBE;!_cdrS)D;rgo?sT|J<IZa;%6a=S71W=}^+^eb~BkjmjFOqM{r{'
        b'G*9774r!%TR_VIUa(ndzP%JbeJESu(Cf8Z60U&JFxdStcR$y7}pevECR73=Ym)f)xRWR$Oftbcj#+IHbD4;HvDT+u<<tN*g$V--J'
        b'8cY?`w%4c<2eqwSUiocF2^Gn&pemm$si01lE5?7Xy-~878vNxq?7fn;6z00Ptz1!1uoCi$=4ooQSlqdaH=r95CpXF;m2>HRDL%dw'
        b'|K)8H?u{tPnE#?%0Z^ba)lT*X2fH$=7!0Vn@=ZjeMRe{K7-p808p&3mjCmT1t=+mJfuUwwXNX9wom{ec@VN{vMfXkcX;=_=NoXH>'
        b'ab0MGE}&g4sGD<cqW4wp7yBq*$r|VCMW}oPl_OEucM%5AHP3zyxA@x%l5b+@N|VAeqa9P9gP$5jI%c_OT|t2s9h?UWzjxOlmVORh'
        b'd4g6xM6Fn~?Oo!qVr`#9?xelkX8IU6ky%kIruwF~ul<{D|20ceyNSv!$&e?dAkj5D8);#x(fQYmQ`)`x8aT)qnPVPa_V^F#trPfk'
        b'i8@*4Nsg<I7oGgf!%1q2gId_Qf}AID%%iMSf^{Bd1rmNqdpTFJHTz_?B0s~t!la^eR!lU(Zdf7pds|%+Q56^b)2nhN#%10dIuYHb'
        b'Ta8;u8Iw|yt+CFNmEQDQuKVGPT1_#@<^3!3km_qyQH&b!UXpFF&LhkchAKKfQjlC<c-e0{emzaXC=JOd&L7r2#L#GTGRh&tYQ{!q'
        b'|LW&bdmHc<f69GUYC7`J)S>au!{{>tQ2YwpH6gFwa@Nn#$SXs3a%A7RK1GKfBO85JaOJcyGG33IS-SqKjX4yFMeX{~Uw0Y}RE)$B'
        b'k%jX+34NW`%SX$qWwOdcUKCAF7I*@8z3s1i+t1{S(D27Sb|C}px$GQbwNdTmNLeZsW8Hfz3o#T~Sq09%;Xlf?`9WBr%pt3F`g>Of'
        b'&@*PEvW-bAI)n3)#lU~<7ckyxbKTztXZ+X@_xdeCG_D#-G`}TJxex;hJ;mgUHyU_}g(M461cD-!1QRcie%?S7D;x1;iUzLO)W|L~'
        b'Zgr8lSf2-U^&$|gNUJQMy{g`NOMGaCWW=d$elHz~81H)3&(`~WZqy@JflO+gESbsM#-V#^Tz)e9c^i}7<?$1;9kMBmERc`$gsid='
        b'MW$XYn&J@SMWA}j??rcYY?1HCeomskh`We3VBhKn?5uLg+E1XnMdH7~qR+@cU_4gYDn~k7fd*hAk~3FKjwGyJ3Zx^Hwk9LEvY&*A'
        b'5s{gfNn9#C*v3g@spN#pH{kH)<|8j0x<Z__`(X(p4P<4=BegA$`HhQE^LeDDzt!;(?x3@x%F#MHh~(6-pN*iIsVZ@6N>8_ul)XTW'
        b'Ovt|9p*p-Z8SA~++xt`Cir{*)we;&Yzy3Z4EmEO(!>R;LX&9<3jZ`T$`~5T)fgd$og7j$G50U08H<q~Nuqz`?I_4*hbze?|hlEIa'
        b'%GZ<7LX#0Z(&$pWOY0}8MII?`g;S+Vd$~#BZFHVQ?#`UBs#dFwluE2psxQv()A=1<YV~VCXry&gfV!$qxMk}bTkmIE#p~i(peGi`'
        b'uoJ|!CXzKA6`^5cjK7#neT}ef#LD}Lsv0aQDmC*dOG(>R(`0qg#59tHZ9`eD1WWiW5`TCFmSX)Dz0H`11xY5>bmBIsK!)Tkmc?xk'
        b'6Qvz(k*M<p8H$J*1pQo0aXws=F1K?Sm)+0_eLae?FSP1UtBcggV7e4bInP?X&eWO9(PNF3So!I8t8Yt=grEyC%hRpQn%tS_LdrvJ'
        b'4lmI|I95iN?GfzH-)H&UmrJF_O1KqR*)qUg%6S4kUpec8PIC$NYhUVig8rK@`WFFR@GHMUgx?peek@0cBA$bM{SP1efv@UU=#9{j'
        b'uXGqy<8qVJ=roecCb(=_+V->#*M~m#I4Y?jA~Rcho}iBktg+R{wsEk(UwIDso3|YiF#E?p1TJ0muF<ITe}Exzl&tcbb?ADh3~Cl-'
        b'(`C~^CS175F`rX2s~qS99jj^ebI3Z&r^LMoTuLcAyn`QzWhqcHo#uxKz7*vFw~b`F*EHZe8sxg$7~A5rbfLlJ5p=Wo-j@G9(xA)l'
        b'TNfJaJP?h(CB06JeIM{7D|oM=I=UBqANW^mzgIK%eE{R2&jgNBAm@`mwU9DQe4RaQBi0ZW#edF^rM^b7TYSri=|mbSy7*{aIx4X$'
        b'C+%1%x4Z}oQNC{u;`T~v=}M#DD=*tF*l%K1FP`Twea>fD?-P%OBr1=LKsok)UXqPAskMj-uN89F0~BPeiY08Tg$T%W8jh8!tFTlk'
        b'gdEWF6o<s`l?FZ%GEqVf!da(7?)tEWN#OOfk;UDQjh+^Eph9Qa>4+bUg|bc}##Q9w^;l;dF?v#P75I9H|AUXuUrIb=+}&b26FF#q'
        b'W%0F|C|RaN2Es#z+>|ZT#o)#_Tl`w&w8;2tpSPVdlU>`(zm(`25hIIqse4~o<%nf>xA-{(2SDtfTf02SWyO^9h^~zWpPnr5&tq#^'
        b'twhrBOy(u4HOZ3hE39qtQ@BI75SydDtObq2d6H9TlAV5ze)_*#HvyZNjp<RCr>KiWVB``*a5+h~SkWQh`2`|H&o4i{pH(9qTY;~v'
        b'Ot+-^3e`TwhG;`#d9ro&_DIo`uYQBbSU1M6X%fRMe{At5qw!|088S+Je(xZs#WW$gefbsk_pK&E78n51lA5eC-GD&9Ekqh}?7j8$'
        b'f3=LQpf%b0cic)@$f!cc+tf(8qQv1;(U|yz;?HhtLs1Q0vEJ<fO#_6lMnw&~+L&)4v$4K!y<}8T4-V|C?BLJ#o7d>GLg}+D-E%;z'
        b'^hE1(R{xeu0gfnxkzQ_B7(&jIA;p4F|KyTTN1zcFvW25C;K&hnoSHDvPhtI&AJcvEJtTCeBY4t3$e{XFLx_wU4sirE5{-HNhNz2v'
        b'Anj|gE`Ju-U!x^scxVVs{KR>>PNcVmQYSC3tq9acqT3=7;pe)9R`!UurZK|HxoBCcOag*}?pu&Ibh{Cz0wM9jlSr>=#$~N+N{gTT'
        b'raOW6W5zeUXd45+3JT0tT~P2%YDG*WaqPY#&&?KDfNtm#Pky7maGSn@<e3!C-szCJV($@ps$;TiUaQBC`K8}5Qg2Ot4>HH=+J#My'
        b'WF|p(5_4T{Vd6cxghz^;Mv2xinXArQ*X~7ZpaRQuP)RZ!GOnU=raFGj)_BbX`(;b{@dT3>4o+F%&sTK=nC{lqKCIP8wU${4la(-T'
        b'@dn92v(Qg8*8YRN-0XW1hOdkap1r@7Bfe3a1lWaTO@bKD0ovBxzH0oS1tg??vQeX<Ks-_(#@O@CzNf~jmOkONreG-_{hIS;<(QJn'
        b'_o4T)h)7jb>UpB-&&bK)YeKj{B=@i45GUIHIp8{7U{5xqN32s3A^%$_JlxC>){k*+UJ^%TMFE>$jQLfQxDIhm^JB}pFX@+apyxS='
        b'sz)$(fj4qCM_q^?lL6xU-f8g_dACJw>06U^83a#RJY+%jCj@Q57ND!dTX_;R0ZC!RcvSTe3ZpPj=33w_orBt|p(AajULdM;SYKaD'
        b'4>9@xfp&&S`uQLWi&C3hv=U`wmT6v6vZ#o{U<VXgZABE`m+Zw}){0jhk!3r(h@wbJQe>T8yb`q6B8MCu@KryLZS=3=BMEN-ReARE'
        b'5`{AxIqiyUNwtiMVA1kQGsvYVy-3t^w35XQRt+W#7Bv#?^$m_LWg}N(x@Qg}ty0j+85#PJjVh&#@rv+wu%NIOO2h$*R22Jk^Sh(6'
        b'Vmbv*0c!D-ucEBnRM={;BSr2v*7w?GV1v+oSAApvVK>@`pht2N6p!h$Ly=w%O5vI%!7}yM5m$b*L%*=|Dnb8ID3VZ7qeQq;a3s*H'
        b'D9MyEBK(|S)i10_$jYGx7b~o^e(m+hgsnFHWve1R*>b)O8P$`A*5rnez)4~BlLDhmYiG~28P6ioWHwRtmk3>^Itbn0gb4p<-$!LY'
        b'{~xxcs)(==D|`opWXvkTbv2hb83x2uH66pUwU;+2@>5Y4x}c-BNuR(GdPGh->~gZg7~7JMEcXsFX#tn6Q<qDplov5E{qvI4YoaO+'
        b'9YiiW58zR2eqB1Z`Fx7J_HO<T5aya*I~vy<T+K`vnTX}*Ak_;naa7gZ@5OZgylW+sn8|2@^OADEuAM2O7xGe9>MYZmfiV^(lPJp2'
        b'?VZSIH@So%bh!f1zy7OQlgRZ%wgn1W=E|R#Sg&o1`t7^9hoFt9HD6hN+}T6)$CgxX7|j-7dqz~3u*h$WO>IFHtYLGL<)6)NbYOd8'
        b'sc%+G>RxNx5l6doMN^D9!@lLt*th&`Z5r<e@j(5>H_a<;ErecL8{IhO|Hj=Gxp(f};9AlA%RO@AAKTpIrx()59@5QyD)kT&*MGN7'
        b'SuHhbF<1*%Wm`=G9fM&>`L0ttp;otyk=D#flf6ndn1`3u<ae2?{w2H`-4LDHc*%9MSycP(jUmX@E{AEL-v<a^SsOFmEo+dz)ySTf'
        b'QXYcZ(Gus8N_axztT9Zvz`Pqxv88Qk3Bd&5y1_a2ggfD}_}V;y)oyk@+SVXVlQwdZIrk9FN{bzo%Un=zYgd*mHxv|X_`WRC_Xv7^'
        b'5R3(eF+gq&!9omgO<clLSoN&0ph7Yn4~%3?R{~D<&3Ej}&4_Vu3P$OCnG&x(in#f8n?|$2Ofs?~s$(R^NULBu6W#9~xPPQUv9)pJ'
        b'prS!_sIfnqO5J(kK=jpVU%K;Z&5^~?R$US9;lVPa&0yHjL+F#cNjoQD`JG+KJU7dyZ>x#rIWzj`Pgzphtd3d8tghw-P9{_LV|`rP'
        b'u@1)NKzI*Q%`$ewPIIiuF^hvL=(|%I1^*{As_?%Ah8&MY&LabTW`hbHYjF&zF{2x$Q!n?BfwSL%J`BrYPY}j@e&iC!o7Q%Nm5@yN'
        b'D&6wfPEYdM>Ug%FpbW<~{qHOM-qUbc!%r@G?FXcoaSHW3?iYyXVtgleir&_h>S8S7(w*m2wPw*-x%+%=Zp1GfU{*X=^`3ii@m$}a'
        b'ih$lnWS^SYb<G^{mEB6IXHq5~o=H7aH4!tKcXHYpSGie!@__Ce;c=OI%^i0-s8MlK#%_@43jfh+2n{l-&Nm5-Ni&1gcqvf5BKGM>'
        b')NL{Rs@Pw+6*}|imCehpI#jL?T1P;{(}ReIu4;*9JYczZ#^P-rZq*cQ$la2atWkI1Pv6;Ddc2j3YF+A4F^~0ot9xjdq<PG-IW(@8'
        b'FpO;UieQ)B^&M)}%gU|mEV7;b-hIcsD-Z2+U1>sZK$0J-wIbgP1n4CP`Mpjj`a*qBzXcA^m9seQMC5TY*{pvff-eL{R`^%MPjO7v'
        b'&*N4a^=G)1b2u%{t<2!G1h?{6`V4NRLEp};%+%L&D<5PpHCgxG<+ukUHJJpFom3R%w7RY%Jab+r47{L!3-cI^{^OnETimJ-1^t&y'
        b'0(uC<zS5dYq-4M4+uAxn9P<`iy_D;1H1Irv{d-f<q6at*CV(zDqM%^$>gBif$X%)J3-Jv>;Zv=-lGN?7?9;8aEA+{rXR=SWrcGv)'
        b'=q`?Z(WIwWwQll|2wlNhuaZxaEu{T<nfmPAeh#zzwdv_6TgwxP@S~Xe@PzVd1U(-se+c=W1v!YP4sN<YgqMjAN52+aOIkf%+##*l'
        b'R<3d6R`f(YRy#nrn$S2mOHy|*rG>5T$*UTu(%-hOp6p2e)$r@33tCfm;1!b{D}Pn^*QVMPW{IB@4M9s=ecVpdN|PzsEQS+#NWBP)'
        b'JcTmprq`+vNM36iY5O1HfGl@T>dxu<{5(@_a_*e8?A&}kwaGI<pY2FZ&=Vyk)G(o!G~%wq2&)Y^6Zc4T4{{^WL+C<+`uWQYO}`^L'
        b'!kF1=(qrlsSIneZbp@RmrC6XxIDo6?{L5_hJ<w`eX$<VY-a`bA3lGce7k_mBGyu}$O7y9FK)}{@YDQ6em@m1NiP7!5&Pc0O5~F=5'
        b'Pc}OZlx?2?5P_he-irCAwxVEQeb<@j9V(Uak)41?6WP2&6~(9wW`kiH^>DN;DD*@H0)l$YEhfgNYz<#TV^qI>(I<z>xN9z=@Ty&r'
        b'?@T5Q`p&9SF^RCpM@N9O)voE2wgOW*ER5N|k9nD~;05JqJ$yLYZUg8Q)NBPqjCKgA33QOv-4c)&8fwhHnHTwu)CB7TLt=<il=m>f'
        b'YjHn`W6~2miK(yS7DE%0C|)d_#z?UPXGRApvlfoN9->Tf3EIi(y*WBS*=~;Qb5^<Y-p#q@plfndU1}457WYe&JZV}G^rL}|i}EEs'
        b'7N7HM3!^ewG2`D`&^Kw)NbH1tDqilR*|;Vv$DuImWXq>#EJPC@`-!?3=Q*tyyl@iYaaa7Yp9~<ICdaWNb3<(&Z{fv@0ddi;qb&_X'
        b'qVtpS@6u$GiL<G<pkS`ZLlFt5cMCE+A828uSu-`x3Qb~h3(XH*cfMBtYV=^E!dWwjB;PH;eKoPmC>?RBYu~F9<~8fvbC))p@$H6c'
        b'1F{dKOwYzw*~AMi3_o<u*;;?HMzPI3c+#zS#l7{FnmOO5zjyA{iT)F2i?_w+Z<$RQ+gjcu;m>2t?3me!OpNP#BU-iBTjmbKkDt*G'
        b'*H?{t-q_IM1jUIs$40j}Yb;|<<F>b4&Q;WqFswXP4SHKV#?xzCxC+(S{Rqtl^|2`S-A0~^MUA;ynEMV$hvERU!9-@lVAJ5Xe{MOs'
        b'ZNn+P1<5y$VDC2N)@?-TV8T#ZmvsMJS;M!UG<sXTWycY;Vn`>gz#33882?rR`q!Tpos#}*^i4LJ@;!;_HpG+pF^y7=Qz2LH<t+zf'
        b'%{yJ?EsT<s#(1PaA?cb%4MTWxF>(QuCL6QMG{lF$75$k$*1}XY5a`pKUhA^A_#SIHAU)=t+wY)VPJ|MYAlxR>8ch;Z&3X{jVU;Vp'
        b'kU2I_G{<6WKCDK~z4za2ZVQtJFaUAnLSJ4>&@p$|^%QET!QuLK3rT=*=7x3%P)}-1K1&N@Can~-gRT+oMsQt4?5wdSA)7|A`W`%r'
        b'8J9JI#25vVZwqdj(Ndb;;!11LBi*M$sgFy2ov7M@>nS@i5gEoo5ql0RJN$DOrQW)dOJG(xm;sq@?oOuLwFvE0_WqU%s))cq*sofT'
        b'xz;qTmu5wML)f0gQbGKG0;{~>d`<4LVkAAW@R3H}v8H8y7#?YfS@wmCM`Pqk8I!thv%DbxW(GZp#A8(WM0IugBAUUpH?wrhf$=h_'
        b'1@mt{r_3Tm)vE=tBQq2%&kEcuyHDG78VC*DU(MI)sR}K}#g(j(=uMTIG|5y6r*V*oUw~Y{u3WB3(SVH1{@fg~<vIZ2SCHW50TgfB'
        b'U~jaSUT9`7G@qr4X+1$sn3VQ(nvVUZnY2h$xP&AmrBfR*JfR@vX5+_=?~oQ6eRIPIM=4Db6IH|{(t>MooKb7=X-xX7G`97OmY7ge'
        b'=lZl+Wg)c|sfv&l=x@51#zh1}5-}H)^KgmELVXZjgKI6si*)&Y1pOhFF=3*?l&=0^M#`@V+oxE8Ji&nOJ`i*dro|;0IF3nV24%t`'
        b'%Y@UV3}8}@%S88o2nUPs2`U^%AJZf^KZt6fFVSa@X5iR7oX}**GAvjYDXP7nV}|5}c{nAf(9iHcG0bu^{JAjN@^koQfr(mg#lrOh'
        b'<_a`#mTsQ%oYenr?E6&*r2Z4PPaakrOz0oFU9Bd<Cd_RkY30eFqHC3(jwN%VNqUk$$3W&tVN{s(9A7F9ELx<)O$D->{**W%&#rI$'
        b'DG314^_E{9<6j!@rziV!{ug2I0@lQpHjbanOhOVyO#mYX>}Cc60ijE<EtlF|5@|rHU7!^a+bxL=qFujLq-tHe%>)}Jh>#1HfcD!Y'
        b'l?tq^kZvnp*ah06wYZD)Ms2%GZE4louBB)xUgmes1hu>0KL7vo@PwH&=klI&-t(UKJ?FhV&|b!(Q#pUmeg3$G_SBApq|{%w&|jwX'
        b')$V7eJ%|GQ#nVw}HOcHWLYPF}k%+eusT4y>tw<+uYz|y1xE=}{iLS#xAomgw=?tVbPGqSjERITR&i#j4DioyeyO!#&#DTal<~*v`'
        b'ZwfOMb9+OP<DT{*^N(~#AQ;5L8mAzYmR7eb=YCN>OelC}f4(qyC5QoPCPps}*Uu4^a?gb=(a()9e+Iq*?MyonuA93=M=sMz)qAhz'
        b'Z=5M7N<|2nx5Cje$@7u>#<@!b<T8PD8`uccN>DwMWi6@F&y|Uv*#@%VG9lw3em@sRR)f_D$JJM869zg)H$$cc&df3d8*IaGl&W`M'
        b'^&3g`w{*uStPWNRs}}teeoq0)jzRK)ERcxn=WPfZdH|*IO%<GP$+G4F%}oA_GZs1#Da(TV&8Sb=DKcf2JTY89k57#37zDz_q+*-w'
        b'FZoFMaBh~YBwRmN6w5&fWAyVNh%x%Ps+7E}muJ*p(j9}gMf?R%oZ)j0(z!V>FRmvIksLGB0%SA!<uj$>B`RGBh?s%U4TS@y|4w>d'
        b'FnyUokcFDot`i6$l4mIpl7BRC7st1Gf;b*T@C#0e>j=w51}+6i&xF{rIarHoeo2)8w**gVvN+3bW!7smZ~I_9?TG5YDw(G}!7Jx*'
        b'0sc}5dG9IT*Z?Fuuwv1Ds1I<F02Sl83pRLqrb<Alj3uSwM}T4m&OhYq!UaT(KrG8v0$SSA1FO%LW(8(0`d|ZD2WFT@X4}98Vwm$x'
        b'2(0}AY{%0hisHaJfk-Aocr^47sFhp{tBr<u3n^9Fmm%yHllXqc>ta)KWW}5n9t9$$%Roi4;#3AcXMrMQZtqGzjf2JKynpNmnde}W'
        b'a01@;!Ja{!VD3e&#)M$7JCK}aVR@%~T_QMu=8l^XH{cqK!NLKyc$;i-IRTfWDUnpX9=hWkt`Dy;lduAqbzB5s){bW(IJ>q(qG?(t'
        b'MT+`5C{QKBrXXrh{Fa6_fznGmQen>0=KdBl#JwVk*pEvWY}`pkWOb_i%cR<&=GzDIvQ!Mje=dc;WGqsfLK{BQyst`tL4v4aA?kuE'
        b'9hRa|4t;bBcs5n|EROB6vadp8uuv69jKRX-FVgWBK`;!%obh<`21&kXX6PNR{1X1Kc*Fa!1IV9742CTe01$Fc6)S~U*3yHz<ez~>'
        b'V|0-Ik<6FPNSnBFUw+999s=N00U>gp+Ge7A3Ak1(LRWxSE}aVV^uUhA@JkBL+jckw_kz(Vaz)7I=Ve7-Nta<V9FvoaR9ShW4{OMK'
        b'LO)rimyP_ss^Z~<We*F_uHCm|&cQUy5CbkOA{QL|i+C)Vj6c{XAk)BtEYRWuAz5Cpv&9VefahMrA0~k4T*v(o+_xJGa`)wf#2rXM'
        b'e#ZiSUza{741Z*v$%OL?aF`+DmMMx{UnciG(E=GjH05p&uiP-VU|TaJPrTQnD0HVEJa>}XUP2W8VU6u0_}_M(18`nRy(&&t>mtKc'
        b'kfbb=iuQ8}g!#d%qMJ8oWnCGn)9T$t8Jnx6LMm<_O^4n-7i#oq#J71-<vz_|t)9jnK<CHV9%L~hq`jQ&I;YOKs>tMM>3lvOFghn8'
        b'x{#50PM8?(wvcgm<hqlIT5BK9{0+^?Fyy78I-_XYZ9ZJPyjj-{5eTEh#qoqN7<bCK*h8W#W_lqJ^zN>TC-Ui(!ox4*voZ$~$oUJ)'
        b'HAKN<&B1K!{V)r;hRjoSR3Ro?t*O-qBU`72iz!EQ3N2Hl&LG=v)Miq1G!bkv2NTg=UPsY6_dnZ=MQ#4(Dr~a<r%k5aZ8G-Xn^Y9e'
        b'M$?8BN8_kTJ>MkX=Dg;l|J&ww&HvG6T(F;fD3PBwy6|qJasR!au;QfuXp@?3BE>E`iRx{2XsTxAm~Z&B=cqsbB<%v9_Is-PZrZMy'
        b'i6xiWl4Sn66U8&v6k6#p<n#1yY%uc(P911PcE)1w?Q#QeG+7S=e-d#1q1D?fgYsav%WXL-_c|((mwZ;{`VAl#T3l{mm-`x;T}dlu'
        b'9U}Z@h54Q9v+%sxWTk(vh{SyLtpP7Kaq<T%JrBi5f0{od`hD>C-(ew@6K_t>+A5P$_1$OX#NU6Ce&-pkDk#6TotyS1s&4b)C|-8|'
        b'G%1}Jo<^306JygP8F=}H{zEGBtGCMydI3!GdvSFjSo9}p*hKe#q`{(Xhwr4-nyh{mSyPRL!}5xE0sRKIbPRGY{x@!#e{*@(mBj;}'
        b'A=}v06K+WTYyFBBfz^l8UU9WBfyBCS2+)9m))~yJE~g3%$<pEPnJ=1<caet=zBY&UhQd#@z`$1odG(?R6l)XWhxzz*-tZQ^BH23}'
        b't;K@$R`}c}G|ve$KYiJ+GZeKVdrjO-h83N@1*<QLxqiovij3y<?5^Fm2PaAX{c7<2GoY{nmk+mk#m$%oxvh|@d#_*4q@HOacWP*4'
        b'uq7as>Lb@bIZds<ofPz(gB%;d+)Jl<kK`zu`N3(!G{=vZ%O@b&W-J1V_({u~BNM7KU?*e9#P~=RnT|>)nc^c;lKk<We?c1N$AA~|'
        b'h{d-IkU>$l^<Sq}H2J-fStXjjW}esq!*^V?bSM~~;4^d*VgCE|fL8z?)M?Xq{7{>-1+(X}C^jEjebz9-;v^Q7Kg>MZ+$HEuSKHMt'
        b'0Y*lGg;{|0xv<^sgS>RN+v;U&tggWn&1i=>A+kL|lhL6`NcXL4hKqr@r+M~F-KF1cn7w<0UA}o2N84`Pe(u8CP6VHgK+81-ueF_D'
        b'G%bw`NIY@JAMkpomTJ~tx;Jg(9A=`C5BcyoITrHFqG(OXrN~1SOVg__$+iD%B#ZswXG1oMToST&!|hRb#guDBEot^|4c9s5gGT56'
        b'W~=5=2eQ_jqux82bU~4Kb7%?;l0OE;<YXF~gDzneGdGjQ4Bv9Re=?FdBY31oZxl@2Gey!l$^_(KIyLARtnD5e7ZAvmxlCDbsxe<Z'
        b'0|lmSKm;tU$%GxB9a}{>2GIo_7tL_P=h_8Lt;j*Q`Sl-AzacK3_+jV<ryl&F3m=-{b;kM{;V}9&TJ^U-_`L*k8ezX<c0W7NNZS3H'
        b'6=eEB$^5;NYqX5%Y4rJ;tQr}zu@v9II7DOq*l4A#)jQ-Uw(55NP-9!mzr`5k?-N!`#z#g!ks2Slcm-U4&7Qf;OK_kuYos{m0!BU4'
        b'vgiuc(m3lH7h8SdU)1^*IIC2{owOqtKBm^S7_Rc?2D=*hAm^b>ZKLn07OMuuMWw^eE--~s)s4Qj|Jgpog^#~>VS*<#=_S=Ia%)VO'
        b'A{S$xZ}b(;mbGGn75aFOjE<4l`l)S=zLhQi9%B`@xuwyU+j2LItO0dZU3s0|s9^boW&9Zq(+CT)<-V+z;Yj#%J1(UT=!}hUa_CrV'
        b'bwxsv8>okG6HGdG)o>w+8PHk7L=>ET#m-wW4VEn0d5cUnTnqZ$sjaa3s{D|CVe+CFw8+e!>s^9A+zh6>a5Tqg>VI=R)eGRB=#6oA'
        b'VM9Nnu_~kIGb3njskMz{i6-?9y&%~l6GtXa{OKn1cq5s|qHB@87|(tne1cS1feZQsUHHWN-0;R;LDOQ;ws!i?T87OjwhAE1O}xtu'
        b'cf!xlfHP9K09Wx@tlmfqErZ||P2PgrLm$?*>4z@tHgEF~rczbbx+p1{MzU~0c`EbQM%er(m(W)776(UWcqeSQ>-%Ks{?1e{m*$d@'
        b'7&_c$UPJkyjH-N(pBU|ABP3}>;#+3_O{SF>d#Og1U&Z&vg_E_<S@C>}T~@vDFY3o96*bq%UQ%gY<}v@_rs!Y6`>2|UyR<m(Cv-W{'
        b'eD%(=vTf?lvvlHnZkCqZ8H2VremVx~hyVK+n4kQ~7%;~?ckF?wBOY=ge}WmxmWc(6u3Vwz4&=48QgoePtD_Bm4Ie-3NTc`9h{bV5'
        b'62H08e_Y<*B7@ujN+_O9_8un&55M5}ub<k8z~R4oJLTOiGH(a^<S)Ks+XHz`ML<LfZSw&e)^C<?WOLIMy9t+AOy(VwNc<Xfy}VL-'
        b'qQpgjq`WO%4F?x0UGYnh-F?``4ecUVycRzDUi6sYgXm7+bf49uk4NFLqgLrLkaNGkcAbXS{oa$~a?JMqcb)+6Ijijlj(N`0E{<0c'
        b'WE7l}Sw9C|*q)vQqx!=OtdSOohmX->!Eiv^-jE(X>!TAGYZ{`8^>Nzgh0Aqh)JkFW{wHp}BvtKmI~<j@Z@UKH@Lp0mzIKm0Dld0b'
        b'oD|R}k);rw4T=JI&#yfw^tRo|L?gUnjhD}@ZJ$^Jr_XkQiyI7g4f5fjmkLK{8JrDRC@MQ@I~@W<UvW{{NJC)h$6Z3^Vgnzgqc)Sy'
        b'15tTYj%NpQ%25FGT_}kE#g-lMMPJ?0=+az|Qac+e=)^-uY99~HUix80HlXQ5Mu3{me@(@kL)JbGrH^c&e^XH5<+g`mwjqw0M%62%'
        b'0_GZesPN&Wb$bma>gPxd?HXM|+9)s||2|%c8Psss7&^+a1)2r@9(k*)SJEYHF*0AFf*xaS>xF`-Z!Z=Mp;)6#Y@=Tyrp3Zq{enxF'
        b'?Ot#}mv)aZ?Gh$R2D~$Jm5LZPk;<&ZDuw9=tD_SHX&wdhegp4sjR)4{<(k9(h#b>0e@Dr#IBjZ~w#CSQ_84J?GHuY{ky17w>&dX7'
        b'T@p6*J_q+UbKm!hOH+ylK_Nw~IG;8jGweZ@1$_kYUNQ%+qk7?MVVoAeuMVFNt0qI+;^2m+ST$Z)rXAv4wm(TgI=5odwu@VF-tfDi'
        b'Jp_~9*d++?MrUSR&0KN2#F1oiTtX=1GoUCHWHhR=`PAnPR&00eDc_@wq!=<BjHK~yeBRI9*2t#nav?G<`_ok>w85&0;4fAEKEQAd'
        b'w`~*(K5~<9?i$LgY8MC8u|Rq{tHOfLUKXGn9U=NRZxp^YzP{lf!F9%f1YJhK24hxMWxlua_4`D#8w@q-4i|{>v7kJ9u}@%*xvo&&'
        b'B9VXg>WGEoF8O%7yw&OTS#SvvE(P?U0EKs5PFPO~%IHsUfiPS^0FX#~1$r-#3G$GT{#OdsDMhv}AodLuivamGe82~KPBy>|L~j&B'
        b'QU)10Tp)%Ykw-FdbC`VmsQg$DY%M$#bo#>ch$z<ewxCS&g`Xk<l<*9eH9qqxZvOr@J!A?Rg7?Z=M?+a2x^A$>$X8#Or)_ilw2i4T'
        b'VSPc{cq{ISkNkmo80C(eF<WtA(X`Nox6sQx@hzBjS&PdX0p}(@L(V+cj2t65oWY0|$TL!ufAAV9@$Rcau~DInvrK690q-7nmv};d'
        b'(~9pO&P~NVWv_a)emA5fsWIrv(Ew$4dRdEYeD<E+CxClnHMS5%aDIyOW~z$Lfr($-WK0cyaZBw^)FYmkVw`R$RRs0sk#vn@&Z1@w'
        b'eu$=4HS?ObMU@=2$sN3BvC`@7!P}_t<%m1hu0&bGsJy#b*WJz<1N7^F)f64PEzxE-Q`_8n9PB4Xy(nh6FROXbD;ViR;W%}_XtvTz'
        b'ay%irhnjN<y=e(=zp1r0(96D}9(AXB#X+s3w2k5VQRKfjjgTTG*Yt)Jp?7@&nx{DC-sV}wPc&C0?&#n~Ka1m<=9KPAs|F~F!K{x#'
        b'wcDx*3BH=&xvjI#{Hz&bM}m0xUEcx-V<fT{j&!5!N?3bs@vN~@kk3&x_x!v8ic0FgaoUJxD~_d}iWqmxwc>_xR_<70so9O=f^fKr'
        b'hx4XG@;<DKz;of=XQn5;sZ}Y#$VU8H;r;iC+a_nUf@VDhoIkji<GJ$X;knfE7~Rb#D}jv{%S#@!o{GSQ0NvTyA-jxxCO-@cE;m_)'
        b'V84c0<aYiGGOpTo3AqT#S_oMKh)*_0O%|2RGI+2i$YR49ELE1^R|t`L;iTfyO&Zo>(*3hZ8|o$(rN(I6i8FIZ6a!229f$7pgL0h@'
        b'bP3w_Oj+e~$%RmO=@M8A=Boe2?LW<&b+J3jGzndTiAk>ZT-%1L6O~gvU%7o>yVWN+=ii!wx1-B}bGQlqBAefnO}@99tf9d9Ruh8g'
        b'w8dh#;1GR61^5coOG^tR0-)v?{s@%v)bl3Eg}h3n#ak)*ikpRH!a7AmSi)0imG;#px?pZ0j_D4%$6u5ez7;XPN=_YWDtR0i3Tmv7'
        b'!^2=_+oY3<%sB<GxUA|GUzL}spSr5ZBh4G9dQP}~{cdv)M}6)N%zwg<C8<*{`44k#abE|d;8fn|{L=Q4iRK#t^$Ln~tB%WxJ{J3N'
        b'Odawyjbqxzrg7dwFNUmzWI!5}P;fnH!zV=xq3nbMrnU*WH1@Z8AX$U`LP!B3UAW-?red~_IFGnJvIX;K*mR`C2eGRoY}_M<7=WgK'
        b'H=O%c7i<J#FTNa@Z+=&l_r1CBs^XlW?a8SgyW3aio;bikVcKVI3eW(BUN3VYR|N#RJ$8rE1SArI6twqM{>1K?DQoJ(Swtjf)r}ah'
        b'+bWKL0s~Xp1i84{3hId_#8k}szF}6ngB;g_izM^BD?0P`nseqi1tgeDy!*(SEAQ;{zr%ZPMh=}j*;5i$19@)CaKCxxl3|LcJ3UXj'
        b'efp-h7Ow3);)%^iIA((j>B=K4t{r4nxO@-7^(rG5-_|b^2(<S#B~7Q}ie=%tq^9)8avvwfX$_cRInZjGdQ+hw=!z{!a*^B1pDj~_'
        b'R=}BAkOj8+HgB%fsoYlYy)Gi((JX6TfDJ7L%%iTj2jnizk}Xk9+ZT#`%BG6)C9aKt3?UbqhHiF+ly<l`Nqwp&Qy%CFu^Q*Qj1g@w'
        b'-0;P@Oo@xSLLm2NrRE#wqt%B(${K)+ir5sgJ(6Ufb!<?DvahFOo7bzhU`?f^geeCYB~4o>cbBLyq^*X7I7Eg{oWBHT7@`iETpL^i'
        b'UHq<>3s{jyVKvIwxbg>FC}@3{$r#@D*px{=*X0!;WtD=t5RZ*NG{*1HT8Vs%CAMsbCNPlV_exy`(AG7RJHVdR8)dnlS&eeNF${@Q'
        b'f95VHM)N)kAunJ6u;KqeEGNEP1|@mD2q^B8m~c=CakNanQ3sb(I3X+1;e<^0VdKW#F=8OYAiAzDL65u#mldh7wk7h+g3SAHp)4E^'
        b'T1}F0?GgAgFfsa_B6E5o{;GM&lyAb-7ea=ccXFxvue9$ueQ&tv7+K%|Qc;@dpCZLWA8;F=4mW_3$NL13%0f~%@we}a&i!Z@;nJTi'
        b'i|OqWm=AHtcQo=>{A%NPK<?~z9;-oWypqu1=rL`sL2-Wk6T0p}`RNwzpPk{7dB}Vm-6bWv2BRTHIy{zeiQtZoEIk;B7P2NB3wrU#'
        b'fNbViXLugJj|>2QWW{RF3~c<tJA?;P9jdv}<Q2e`p{PIyMC$+LHc7Shjnv*oxbGna;leyPY@{AXB>V0=qTjn3^^o$$>bjiF3yu0%'
        b'ZM&GK-^ki_xD5GXvBBL55wD5Ae5W{f3r<&`08N#?hQY-oq-oi}-1nVsi<1n+3CYndxDEt##3tzxWm2IK9GM@-Y-}uOa*~S*)v)d}'
        b'bCBCHFOgp&XAZmk^0}5yS$?O=UoaOUqWNo1@%l80rVDFpo{UqXxF|h;gCh3CQygp<R&!fbI)6SQbA_=h@*fkzkyZ#pa6$~59(ha7'
        b'mv*Dlw!d=$9AmOw?=0p=H67E7chis<pqC@>Z9xvgj`@5YuI_AA2CdKC&8$O2irVNTXLtdA!Uwr8^EOTq_!sqv)0gQ&%7=@Q*8efc'
        b'G858S3aA6>uJ07eZy<;e3bb=rEjp7ErXxs^h7ZC90~7{M(PU!(8~qc3ONI-#^?L4i`sqg@i*Z?Lr8D-Q^1bL{bO;P)k#pBkc88@!'
        b'#u%K#c9&_TtNcO!5dNM<_=0}RA9OB)!Uec|j#T=W13$gOIj^xp;#}D1*QB^iE1XjFwgA4(ca^6&=c2a=SZqFnH+sZHlIt#dQ;V39'
        b'HCj!Zf^iakK+8GE)ZDG1+1Fx~y2*xIVt*{fH9*v=9i(EN(K~}D8*n$*ecPZXfMN>Q-Qyg1-BlQ?)%~jhQdUze(BqNh9{roQviwzT'
        b'zd~l|7`doRG&}Q&a$O3V`K(Tvil2EX9T;yqyRbe{n~sCq`<$tQ@dg~1_=UXn{An(l3=Xt;8=O@lX;L)KZOMgL(HCO=1*aEcjLgX^'
        b'!Q%wrEzYG7C-pHavX%)IgapTVyvUYElUc(m9+9_9mMMFYd)Bs0R2()n{<yrPkh$tWQzk@}=--Uk^12gNg(}VoC(ybHuE_9*0jfk@'
        b'2WiO<>d&X(e%6ZFj&tg7zxRze`$XpZIo)dw>06-;s~dBqzHuvBoqJ!jGNsLp?ALoB-r#rfrp*r5)T9-`FpD?N_Z+i$v+y?Fj0F9h'
        b'w>JcJunx}tuX6^^c&RU(3oc;P{@Zds>x6tSz)s)sF#*&52GjC2g?CcX-uaDl*2h<s4r%?`kuzwzpK&z6<U|cRC266m9n~2m^%tl0'
        b'l!{+@nxK9xbIfVg<l|x}2}$`1`FO}q?SK>R*7@N`$wD^!CAhEu$!Q%E(BdS3ox79&%ztlx^H1Af&$s`-u>BQ3ZJ#P~pr|hz;wSYv'
        b'*EK*ilO{`|zfGDG{Rha`9sGr0xESs+h})~~3m-i7*Z%&>lfT49P`D5f)d|I|sN<rmv*&Qm4g`<G?}tp@65aUA@=WCWn|#^p?^jh-'
        b'Y4aMq-l@(dsW>3_r5zVhS!lRHPfkNOZGl-Vo&AnZKb%+ZflBo+W)$ac!fhx;Yti6_tFyAQ^S}4^KGa{8#zLdpM@f9IkV-^V^DMd4'
        b'oB^x4g*198iv|nch@iTDKU){s8mtX+uCvvt?p7CnjGz|4y3pC-eKQIr7p#Y-foS#|e`56|=9zy3>uyDJXDfme;qpo-0?vd8%|Xp='
        b'9LR7&G1@8?D{=+QWPLC;N!pm08gmAf>3-tlgt_k4PSxM(WIjF<pPpeI)W8OrPaF=`(yn1XtM7KnTUjXB_nty>J>>|-3_xBw&`K%3'
        b'6m$y(7X`W^f@1d%h*#s)D?t#RyB%qlTRJUQP;{Ywm3PX2S`f^92cCO>k~dvmQw9619d*NQBixIDP?GNWSLNE1^$^rP<f~%h3NMH2'
        b'dK}v84nL7(#Ul=SmcC=<nU;1j6F|_zjzI7O8WO?(T|E*-i6lK90eg|-iF$<3yd)gQU>Alia(#lfsF|Y9>$V9FjHk*owUAx0P0#uf'
        b'nxfk4nQnIi9-4?CwM@mQ-y3}aIpim(Lv9Vm{Lu{s!fB5<zGa>(5<A!;L4j<R@lN>J^dWTi={(?$-q9yX7H_luY;a+5D0?z9VsPP_'
        b'gG=WkUqO2`k&upe;6sy~>+NY0Lmp^v`x9hbZdJ-u=(4OV)G~?Xr03|p_oUq?r1rWY_84p3xuPeDF5*Te^FlpOaUqlSOTSkJ=ZSf~'
        b'KIp;g(76ODiKUic37PQ?i~MB(&%=TW?8VafMq!~6OPl}olhXD~+c#Xt{X;)+)NkrZJZK(DhJhG#j$->hh^NtfIJC2TT(=c~>_suX'
        b'{>;Crfc7_T<kGkhGb{zyOb?aO*ib9Dmbyr5M(K*dIl+grFidnGpbj}8(hg}sSt=%K0A+g2)&R7xIA8{3h=cqa8(IL##;426OxTbM'
        b'lvTV#z2LB7Vo^09Jt)?g8<e?*shti@SRAaf8QAvlap5rAJ`kV&C?7=5=7x`p%lw#OFF>K>Sn7WqOA}};;<m@8>JH30m`wYl6ImcW'
        b'Et(5R6u51O1#tn)_Ay79AbATnKp`_a7p2$0>XgwMRP&2KOV>xI^U;$r+dCY;$fC<pt`}i0Ok_pgVV7N^rN}hY_B62l4<9`f6&9h;'
        b'ZT}OEAQYj<YKCYukOm8UjEqKoGyD!jx1-o5$2dyops`%h<3KB_k3PjW=Z+pjZT^X)G97eSED8>@0t^)aki?>y*bc4@Vur22Kls^1'
        b'KL=4B@jI|(G<Ajs*v4;`7NZ{6;A8SqJ~ZF+U}-K2y7mW-iF0U2>S;|H+*V*?EXrv(#ligwX}>Kk55l>02MVE5$59vRv~Sj1X)DaS'
        b'dKwe`g`;U?kfE6T7UDFJp0ge0mZH85?S_qMmh$tq6H=Z`)PX9F8msfuIn<x)AucG6eT~dK{}cfiz|t`UU^NQjH&g}q2zo;m9CfCy'
        b'eH1Q7l=;#H<kWQ31=|P`IS4!T0|ey(xaEoVbJSEli*A^x$$H2q&CWLM?M!4v5Wz3k)0p_OOZ!8;XdMTri||!qxXw{u)>|<NZx2m<'
        b'QLhQJUE`?p@P8cr9(Axz^cYJ2N4-X0q`!eYYEmE9BkVxo4<=$SX_P?)clZ(mUr@-ncVTr>5kw<6qVVB!m{Cn%Vx<-fVS68zf2W=e'
        b'SQx@K%2B7_BidD{p?Wx_)#owM7$-Up-v{e)EM;gt3eI`YC0t5~%$%>rMS2oD{inwua``NE@#*v|34f-(m4y_1OWnUy@SZw!f{m$P'
        b';%vX;&!!JS!1LKcgPx;0;h5!9j=J_@O$9O$X+_a6VU`2++DGgCbQ;VECs$L50zw%$%2ubTKpQEw)x}~_?9j_7@A^9JvRN!xKaJUz'
        b'A}k;ii~Ro_%HXJ{>a<H|KW?AK4ELjtipgP8Y1_szzpSUl<R^txcAfUoIu~6|ZFZtP$&MKobL6B|oUg5~w^(H;EfN#`FK1Ju_EO=v'
        b'=8Im0%d?I(1*4ksaVFF|I5;9tOg%3p6{Il7wOlV1WEEAd6e9QX;_8O`sr%~^@WK%A#AJM9*3wCOkh@YSSFN%bA)miWUb@QCE9?qk'
        b'#?WwmlG#3gqMPf$gSJR3g(^c8oa!Ri4JzGLj17fBIFjH4wZyfT&|u_3lH5c(+EY{;+}<*oqUi>Ut@hm07xIX|Mew$qd83Xu-8dy5'
        b'ZpASP+#mLe4BvAa|0ZJS23LH)!hD@?`Y6g)bnaIBe2CtVyAJj%L(sO7)5D%kJ|vBASVc<(ORp*>3E0Vy&{bE|az^edp~sP5!Cq{0'
        b'JUVd7k8?Axpt@?qiaKu|%A`VF8tjm%7lYpzZ?JzFx;D@*;N!)J1ON>0MzVw^)piwmu4JA>nWE1hOug{LBq@xK5K>p1g*4bQ?aU3?'
        b'L?jcJNB!O;=8L_&MW7<_Mj!r&pTwCxsMs1T)g(=8h@;n|{Rh`ekZ<^MY;_ZfaxoT^N0E7J6Q=PahfoQx*n+$t12PKWen-E-6&eY+'
        b'+g_^>)86>k)tG1(C|ib!T;SSc$z?Iv(9_`cCD_n*P!^7f?gi92XE}!4p}rD5rt2*@Lv-QeA_x_txMk}w!+vlL{?>r9t?#w%zv3?t'
        b'dA*g<dd2C5)Z0$g)3SI4W?KaI^pLF+7EV!fA1=Uv_tL~4ufTqFE-9DBZ9}mz$&e>QSUAnrQ$LbYOGlO0QaPNv+3r^Krld__26QAK'
        b'_ItzIc5#Z<pTjD8Q6=96oSVlhKNXx2!Y13=VT~p)w;qzVQO=M9z=A0vdQkK*Y&%-1evTV1Nvg2vkb0>ABSR4kZ~pkCR8eyazH6kQ'
        b'^pdKqpH3voOa<hEw93Sg_3?dz=*+ffx&7xf!rq4y<KSSIJ(G(#vTwfYlOm61b7qpIMXl4c8kWlF6LksOOh5KXeXP@bj_c{I^Hn=1'
        b'KH@|f0GKC!EZRAf-==DNA;!B?g|<9^Ao$|Dq01Z!Oc1|d6DqHMHU^U1tnL}#cBlFSuIFH#Z=192ea;pRfc9A@?Tt>!mZdf5s9k$g'
        b'Y0-&wsB7kDxI^b4sEHFBxkGuVGZnzw3K1_|x&JW;Gf-WEEXFmxls`J{#S9;EAj!mQ3V5S)p1ul4mdsPH=M<N|fwd?XOf7<SKwcWc'
        b'2StH4Gp8uIO#Puw6)QW0!S*uEPjiaQuVJ151%i3h&u|LmCD;qd?ez+f9LJ0!%=LDcdXLMxuV;04mj>QZp*RmcGqxjK^x%RiZ0H{x'
        b'YOd`mSpS#Qy?Y^~G`)O(Dy$O1u24?+s_K{wgv&!0IO=D6XB}$DzOwD*fL2ncWA@VF^Rj3a{n$JMx|4~Y!fcy39#6v5C7h!39E7m~'
        b'BjC)I=1(a?BxKzB-I(b29K=PXx)}ENA25Rp6N1f`DhdF(;Bv<L_kIQE{^@9#BU4?(?N5XmqMCu_(v|J<&08$i)xfcN%8H2;n)j=x'
        b'Ft}sw>G69b&5yzEzX!8Mi(yrpH&1Pc{K*O~7(E%nQ~HWZT>!^y2BAJ`OHjH^g}C7guK-qK&;@~xoOl!>_upYA*aFO#Bqf)_$}Fw!'
        b'?FpDDowNOl1G!lAvgpCAm?}d(7p)i7&7Q4TF@fTO5VBalOAe&1EmxTX98A=nt%bCGIM<3{aNqWQjy^)F3%?Zg!d9@?HFE=DxbM6J'
        b'grcwz>cj98R+cV<8TOZ>>OMs!+Pe6A8!O}~kn1`+42q+t4byl0@99oD^7AWmi8A5|-Ke9S7;f@=4=}IQ@@BE8h!eHOky=yS&ufdw'
        b'&=nieRle8LPC(hFbV$YQtL1HD$>Bb{w9~>g*9Mtt4T0-p3-t{eg2c&)*>Id!cFXfv=P?HqFZSft*juy9HRuA8KPzx(ure%`3OG(-'
        b'`}Z?{uC;1@URw;?+li{jm^b(GN=Ce8&lSY3INSMZG_V@_l!muAK=m{_JXoAWb_Mx>b$T8A6_7@==nAzTHek4kbSHXh9b_#Fg*6wP'
        b'y+Z<0;!ssqCoOPV98qkC<cddb53R8~ox!plk-<CN7aSU4lOES@cWCe%u5zKy?zj>s--vdV#MpMas8g&FlA=&LLAahK5r7)>CEFA$'
        b'*np=C`C#*^p9>-I#`O-3s0+K?YTU#>D3sSdQWnqctZtF9qJy5y<)UPQVfXT(xRRw^#LzX4&yZQ&B1ah_mW#4tRgC3s4ivX;d8%!O'
        b'TkhxWwE-<{s0~wFFO~~`3L`0EDo~*fwBbEoXDSa4NfaGCr%0+LGpzIqQV)4AOG4G1dyagE3+{!>kt+?r{HoTO<M3-%c1WC$I9%l`'
        b'&0pNU4=nT|SCVk^RO6s%BW5MQ{!=Qpf0NW=t}3-uMr9XWxM>|6z5QM!zKMiX$m7h~`<}s*{zOKRbNrBSBoZ!6@KuX=alkyo%d(TF'
        b'Ke3WvxPEv;*Br|qs|+*Tp>)^j(TC<Z9;`}nR1UXTI{Ur*s=6eKA8$m_QNu&up!n#vD_obDSF(gSe#InDDN~IU$xB~ECV5*HIW{6^'
        b'7FmwUnrhubB-ra?!JzomxLeK=h<8r_?Cw@JAjXcIKz=o?V*F$;HWUN8PxP~ocXwB|$ln$Ot*udPEXBr<V8wi`xw~tsdlOSNDa)Z;'
        b'nf73)Rih=tkMs&2!jf@zr}kK_N=2lwG8M0dT)L`1VP|W@$SOH4CG-+(qj|hco~Pfq9g3C_S%CKG<CC&znO-SFrS9WP#i-~K*-9yL'
        b'+Lzl<^yU;~k$8LVddSCl#1Q*ZdQ~HP<lVga;W4)7d_BVDJ$bM{r@HVn!tu}Ltfbl%&Dt-qqhjpC2g6|hj--<#$NM$QVdwb!Voytv'
        b'{btY}n*mn_<tf9eZ-|i<@-_1Q$NM3;d$H52Acv0PkQJKdf|u}AbrKL|rKC7hQV3GC9<m+}fr7#MO?ZVGjIWWmha8MVf>?WXU@j=>'
        b'9F<}p9><1qfnSOrIfmH`pnNrKze{4*w&(_p*m<K6K_UX1q^#DXJ4Ib6P;8vnzVoX~nCL;!pWQ!_EkB(-o-H4p3-bH{Z}+id<b1Fw'
        b'3#{^ug^sLJtqFzAJc&oahE5)N>9=_g=g|=OJLRV2knHWRpPABo|D5+LKLHNjpRcJN&yZ)*upEtHr{pR)8aWV#iv>SYjt-=Zqp7}7'
        b'kRVDWz%)hA1-XJuj{eoD@mRUeUQa3#V?&qe^?y!%6d(_zQLAj@oF98T;N|@KQ%97kV?W>j(3LhhxxeIC7ry!g=6~y2cc;bssl{<r'
        b')g?Y7MBPR$nLp>IVP8EuRvWb{inc-7lvM0!F8b<g!^I#jtMV&#o9d}&(2);|<=<zaeTP&_EU7rqXcPg$BQDxNxHMwFM09Y;LoP{3'
        b'T1J}p<$m5`5NVn6dOGOXql8(z$Epe2Urt7W@GNlLml|tMIW8N1CaZsjk6p9q3hOEI%#c_RzY6l}b&u8~6aM!xmPl;T`zrHV^b({e'
        b'=7~JfQ7$f1JkZPfLq!MgyEhOTlJlU(d!Rq%RTXMe0+?U&jYSr!Kg@Zb1o*i=5o!m!-A?=U+qVDA{q<M;a*w#*D);gj+{ya1JO<am'
        b'rczjoUwjG@n|$F6n{g=el;osq(U^U34t6qg{^%V1;6wBJAvy3?!rEuOaX?JYxVdX`=*DdQi|SR~mF;3Cy58k;SjPm%*jCmmhBPSa'
        b'J(XwY{)-o+W%nqjYtGNZzDf_9oQGHck{oaE4|W69*WOyR@#gHBlhz~O(#?@S8($)C7st1TwX?P70#Z=BC$rNp6?C>Z9F?$lnp??|'
        b'J2aK6J0oPpS>2U<kPKdLQ19EC<3j#=;_oB%z6$i5%->zWL5453Z7|2PIj+lF{#B<NsG;LOD2!dFS|VE=ehxBi`H!X01%TFJCNBsv'
        b'moo3v_%7D<iD=E*w(~R@bw=8SG(Z#^3AR-cNqB0g4{B8{vKt!$N?Eex;4|{x#KHKFPd+FajQ@lTJ90vhEP<qkTu4J!Tag74e8}T8'
        b'soG!V(h2&ITjZ#+`~qERX=Rb{N9u2NsZX!dV2ZG-e&4f0ke@UT)fKeV&~cr5bt!}}C)`Y8S<6xq1PStxrypew)cE@AAnQ<}SvxUC'
        b'drzwZUP!CQL%<28r}fZBI}!tN{v&B|fw-5qKd9PKLq=`h8u6SQgk^!>`BJt+I5wZCdOkFu0}v7kh@!J}Iux%Zc82<6U8=d1rh(sA'
        b'p-8=qTq7Jtd!f-^N5{PcA)&U`=xJk4_^w%aXrmx&Goe@@VqU26?L#mX!U6mHU6_PGkw=WRp14UyqV{`zaB+}H-Midy+@6z@A;FQ0'
        b'^P`cAdl`<~-jL_Tn>P~`IsgGDH}8Z`Xu#&&1@p~ms<6iI+nQ=JQZLkLup$$(7d7szD_8-C>~jbutv1EGF`I?cdx5?H=yjMXCIvo+'
        b'm{u{XYJ6MkAm+odQ@=$AyaEU+oLV?`HJ;WJ%X@1Eo~rGCM|Szpj>OTpk3UR{8IAj7`$LP!MQ9^=9u42-PpY~DL_jAPMFaT!95jU4'
        b'DoO|UjiSJh)LJ-%CJpBIRThnYZF_1~k0ogZ8Hy|$@@tSP_v3X*EBXY?rakE5FQvv=P<Oe6%CB>kucgaNs9)95<xlXx#nhwlcQyaJ'
        b'hFS@Ke+?0m6g%jCa-qszm3+tVXwn{1$#kIlYIiyxsADC=<sA~V&h|<?o+3Nf;Ths}URliLt01xF^trTeYjuEh`JRQyUwt%+*U?I-'
        b'BQcj|Yy841E=?zI?$2LBFfny5%^^j{O_%2L+4$;KSUT*1`1DY#ucA6kIjisEtE>)7wECV!amX*)X?mSO45%;RLn#whXVtu9p=Ia>'
        b'hB^<Ej7SmvpYXxNgu-thh<KX{6m2;f9X)1{7fErmYZ3LK-MUO*rB_0p%DN1)->nt~#q?uS?BRPcUatV7mkFpdc9f?E1(XXWyv--r'
        b'ZWpR1hQ7NkCk%c^9__-&u<D}%66s7=XQ*6W;94ed9=E$b61XIXud!hkOC=CzIV{d#!@Mt+(-%nbwal-eSbjUMjqc*!KFFl=dR_$3'
        b'9;ivh_bFb5{Cb8UL!Medr0S&FclW|IV~Xi4q)SV)Wu>cRdJ}y8Tu-knG?f<8rrU|@^f6ltO{U>5^f8Bu9-l+KyB8t10@AN{F+E{b'
        b'Jbg?5CI_+1c);%K--|qHd+5TrwGe@kIS?O$^u(p|))TLIYT6SWza>mMfhoqnK68mF=H-JAB$En1U5c>S=0jG?Qp+oDhdaWr11<9M'
        b'M*bQeg$WJKE+bxoQYj>ZeFBpXw0+4HUAoz>?h}|VbDN|^iSU^mJDC2C*+@g7cmFwSSTVWKQX}gVS&q7`VQU~+v2@D38>%+Q(Pqo4'
        b'qrY75d5KhPkRxFa=-<WlM45t^49$jJ@j3SP5ys7Sb1kH?urEBBg)}2m=xHUR;2<G*-|;ElCf1Y7*_whKd-7S?jSD8)^rUz_8D5?^'
        b'8uRgo4}^BFRRv-`S$`a}6srRCy8L{i`-H4eCnia9e)khqg*wTe9=J?V-)apV9N2Ze|9DC%q(mfKrsjW4qZ<@-&wqf&?JG;<S<6&i'
        b'SdV#cvT$U#TrnZa^7N0i$n#o|R?)se$+5vaL1D|URr@W?ZNh$aKg6M6j?m$}meYeU*I*vjy03U)ksA0n2>z|~uB(M>)@Jd0avtvs'
        b'Zco5_>=>($1bKRWF`$w52h5Wvpz|<fm%#w?o(+O4>*V7$mEHI$aml|{zolR=Qo8#p95b|ni7Cz%Qv9i~wbP$dd<O3#`tY{zIeo~Q'
        b'JeaVCHI8hPk9g#kHT|XA5z9HUUGDq&-kMb#w?nRTe7n5l*v`DceNP4&p6ovH*ipISV^wdg;&-v6u)@nlWe13p+oRB(gk?Em`f3of'
        b'n3ZR#@PdGs4{v$$NHk{H4Ri^6<H9kWX0N3M^|glY>#^mFM_!kg9`7GHF5h^3{2lq}bMLggGkp4VYwPmlx2YB_NgUNdIYqHt>c_By'
        b'f5wL5fD6NOj$*c0(5uVpuN>be@4@%B?khPu_{gbV!J+G83EtuU{{G7Rair<Hf6<jzIr)dq7Bcj!zhZ&Y*N(Nce(Dj}jbtd2D<pt5'
        b'Mn4y|Dkme`qZ{v#JHM;#Z1H=?VSXh-tYf}*Nq48JL(+4-RuK!}ub;xKMiFzwj$G9rP^ph!>65lo%&T@@jopO_6>CEMm<WO@S`0xA'
        b'fuIg)02*Gt+dX5o!JhBic@#qbA24qouiX6q1#{G0m~%2#+^N*}#%!gn{}uEzwY3pF!w_;DLC(%X-gX#4u4Q%yA&=Vbkw<0cWMH<J'
        b'xsf<|DcwIp%e7s#8%;>pY8@SyPM0kn(V(kf_@RcsyR4!$>2&$xTsavIcl#LkqAO6GQ2z}gTS@-=Duit%7Ye$FGjk!n4MTiei|}nN'
        b'y6cEqHME(F+HTm6*1PwgqlcsO9v&I9M!(pZz3Wz=aNC|ad1uaNgPp_YSAft}q1j}J;kUErC|C6IluFe|j(qcOv_g!#Yj>hWQt0h{'
        b'39E@Kp$lE0Oc-`{9ZL%R$!iM>A%6$ge0-~7GcT0vMEIF!pov~6J<uouO7hw+NsHhk`56py(fslFm|P*fX;sR;y6}nL+goDmWc`sK'
        b's?%Q#Y?B<4(>`0lu8|ks`@~+1#Nrz<TMjTjTZ<xb<{)2kL)oBERD5NJJY~CTBwoImA2DZ1?M`}pRDSLw&mzU!^Zoa(b<H`Z$egc`'
        b'%!gtTIj=*IK!vu@_pXJU>={Xy*uJGj`%%F~-H%2D6$Yk_$x?Pp*F2AQtl)y~geedv`|4}$DXN_wKOrAjR(tHk;Np~%P{Lab0*kc='
        b'k0aSS$f5TNynpORY|LNX-G5Y(QHlg`q}5GIR7b0t_n}MB=2py>3S6+l4VWPXxbA&oOpc;AcZsdW5acw>L8y+(2fk!smY{Kqt5C*n'
        b'QEZf;SqP45<p5m^NyW}xyQcK3pD2r5Tl6xKDk@&>CPG&g8j8{0SSVT}I>rsJD-@N8dO7sIR`fdjAHax_E){IbWyFI$ZcC=8jTdxd'
        b'1s*NC#qf8SCsnj&wfiWlYK`GCH~e|3sARRf1HG5<ic_hgwX5AN=zXo>3vSmWoeigb=rhDGY{Ci^GHPZ|{#s%O+|gC5QV^TD%BQiZ'
        b'C_=SLrKq0AR%=A@k(eP9XoeJeh^<|sV2G@mIc)U~TSnaGEd=V^jz9=D@~qq>BJ!*GV~FD=tnrIIyprUgcl`7za^bF-F%qef9rbk|'
        b'OBp#X^A|tiFJ8-vkCJg3VO;v7a3B;B0_H@uJ_1<BFju5F3l3+oSpUX^_3+JVB253rBzY>QSK5V}zoFpvsW^5c*jPz1Is+&QsMFD&'
        b'RH1%$T67t*uT44ObM)TkobV`qtAgB^wyl~}r$UARSMrwiO1O7vz16`K)Y>woVT#+)JcR66L?82Kb)IUHq!+I}8TL!-;wQ*O$)qLO'
        b'?OI%{vQ#FMj%2rg@oJR=K6;bgDsLsdc#Z0eyI)m_6e`+PNNcfGg&YYds1{v$3G2dw)@*34TIFlxDaERh7v=f<epbRdJ^XmB*)e~3'
        b'^{fqs%X`exXsKucij%jjM!bcZxW+wCuv!llvhm{^u`7iw0*}Dj0;-RkasE&B=I%;s!rCq&%&88gSuF~3!ppaNrA1OPq$$Ye6INyy'
        b'FsAB?lbltv78c2GQ=tOle=jh+v#9zeiXj4kXQ!h<mecZW&*nX+1nr5Z_XQGCj%42BO3)t6i0tMUQlGR-%*xM*(6v#?4Ki%#?_5Ak'
        b'1Zy^9w3Whb*SPk?KrAe{$Q26<F8IF%PhUlchj+?N+@fH)p=+};^8?jzd|jGi6l+V=hx3x~PxPU6_oDCC*wwWx83uQ-fSY%@xB4fC'
        b'zrlK9tGghZzUB;((p|Z0vUUR`$Fov(@OyNyonMoP=4HL9ieE_lXIr^gDk0Dl!mK5h;bo*SS-9v*ZmKqM&vIOSKc_f-s~!6+W6!8m'
        b'I4Bj6p>5ld+rphU%^4`xkMd@2Dk)vQELY!wFMli-vl7CCk)doD8D)=A<D5TRY$XJ>V;Y(aO;`eH(u4q|EwADuzVPtP-NT9%?c#RK'
        b'!ya6S*?tZgbQu}tv0C;J-E4}(NuV{x`W&o^-}WF0aY?WN!JgKAWE8S8I_^W8V@Ll;CsO<whj@C(;!jLJ7%Knl9h)BqqxY67l){le'
        b's{H>`I?IpPk-lB6#j06c9V+(?+N?1GSE4a4GR<*Z71(HOr^)m2t-qvkz#O-!QV2S-b=Sq&kYUBGZSVZRkK3-9?#`5vP8s5BcTIQq'
        b'rZ|qvP(TFMQ<VO_;ad)nqX$#ZP8_DZmMH~$!`W_w6$Ta-*ZNV&vo*yc6qqJx1=dZ==rzSd7x?p!(=~8B*xTb_i2MH^4_boV8G?c1'
        b'H8m(~dg9{FLvVb;(D=}a>G7emvn(17I@xqWs)B>D$rKz6i`^0&4O+7}K2*;9-j<3BXw5psV*(W%jq-JECt!d1&Z=N%zvFg&-~DQe'
        b'>bMLFJ+Q0nRpg2s*?fCz((zhk8g$!cQ0u9&#%xtYa*!NZ-8uz(D>^(aOcwttW{3x6CbVmjpQpJ-Nemrjglgaht=nSr?X6J-RO(?W'
        b'HTI4$g9C_Z=Y(vlf)%zWB7vj88Y8yU6IPvIqJ<(CLgI<K`jL-$)TTI14n`J}q5Y?2{YTwU00~5{>F$(~i@p2YEpopAxHP4TOQDXJ'
        b'RIc(;*3HX0=+r2bj>FIm9EzA8y(BG6oa(=r7KXxB{}jMno6lU+hp7h<d}pM0!MlXcf;>cfqO3<{j^Iw@`I2m8WFWD0Pyi5Y9$&Xz'
        b'Ra6Ut23Osz%({_pJ!r0h{2`*ChM+yBPtc~|ie|2d(q&lv&>=3MDedl)b$7TuRZu*GLRyP_=nS`OX5?Io<0To2zRj<r+6pGG#v>k<'
        b'B#3LbG7r^g#KTyIm|0Oni$T$-fc6ULT)-@`QCT&qnxFY{Yf?>sGStxJKQlXin57lB=|J9+qQ}529nfnvHOuj~saruhkXAEG2cpzz'
        b'K{_xoed{6ViJDwJsf1*p@D3TMJ;jE3kEyKd1Z{)2f^=ZNm`&Bt_9Y2h(YUDxU^2113WbWE_@1+U9=x}TsR{b@^{bd-8?yPtXbcW8'
        b'J$N>>#<{3wm`;`)x=<5~OhE?Es?w`8AMKy)!kCpPZ)oR1_uMmhAAw3UD5W-2GYT;@s6&rZm!Z_fohyX8(3*p<g)<{B!uKbo!=1Y('
        b'`&A$T(ZnYOMyv+X?9$g&%vM{_n2C7}J(!W{@@jcVmynr4?+ThI_7|$dFV82Df1EW$;Q_D)FT|3fMVdiA+7OWt!v|Y|RH6$}c_AQ0'
        b'<a}?Do6o+!b;$MuH`}s^x4YMVX<vzH@L@lBom4XE)#%0$*Wk6O+JD$H=$?=5T?DfNwM`-m^q@X(&j)rC=bTTCBr&fBg=C$bQ*_pZ'
        b'`u*CAyvx+zCzOz337NriD>3SAJ0Hh51I|21nv4$@Q77#hxL0=(e6aeWOitTx*Sxzw02`P>RlqHkAKe7L|9Lmz@J@5dxNY(_J%7#4'
        b'$Ea=*vyeSt%kTPc_5sM~oagqJly`19Y~QY!n`J-|WEEL)!3cs|4%p#J*nC9AM4-BhI*BblI~keKy!>EcPSTc_?Q{r0E@mMIzWzlz'
        b'?r{{C-DjuE9<Tj^@<O0%E6xb}2tEYrtdO!2o#zbk+V)G)k=Pfg-c3?PB8m{m+(g~!!kNFK|DCUdcKW3t>BnZJq%WjP#AKkn%*q#`'
        b'a7&j-XwBpLGHIb9>A4TKht1`~s%}?`x&-DY=5!48Ja329e1)p{q-M)=b}|7%>fj-zHrscMesXfds9}`rsYKa6McIl<Zf*Ikom`Hr'
        b'oUd}pA;^GtrPS~?ciXoM!6d#I^h}K<NU5jnRxjqllBy;1G^0g&j#*{nuPO}yBuHm%M0=4ZBSk1N@RYraWQI^_7VBAS_q3mpwoBfQ'
        b'>In6Vll+fJ{1U?T4DNqK%#PVHxF9i?IBCHKO!4_GPrFB=c<xqm=$-ZVpzW?t?JjKM6RuX7nwK<-VzcQ1I)tV{_p4SvjeROQBg{Ll'
        b'{!Cgc-F57?@0$Pfz3t?G`TmZoolZG!RlobwZv*$*1740)ng^x2Bzv;7BUYgd(Jr=Y@Ee6xqJ7tOh?L*%Mm@zpIR)o8!OpLiPo!sK'
        b'?E|rPUo0$M$t1D-U@@PgobC9o>x_z*gJY@rb~e{jLFPHw!G!ykV|FXE5Pc!%bVRh{XXf<HVHVhL+gw^{;5rB_yI+F?1F?t1n#Gbw'
        b'I@_M1$jCeXgt{;))PC}N^y^9lDfX0ju~L-~6Ng1GA@&}joeHsA?6U4xWhz!xy)OjKEmDh3+5KAJAn5Lu4IY4^%*lP19mg6{G8@t!'
        b'{G1PKDQ{)%(ph~a-p|T<ip4tHJFvUHKWL>@Ll&{XPvgwrUgS+?mF(DXd3yzO`u6LE;T?W@VGuKB{bii;w=aPM%=`(B%&uwsZJyHe'
        b'SgJ|+iRA1j?7$~%&!?>KQ<gc0C=t7Exc%(M?7)X?&pFoiBbWQ~@PV@*u><e2J!32c(a~_ew&Uyv?7-jIo)1{aELe7*uWdj39y@TF'
        b'?Rk%dEKmE^tQwSbmK_*kd(N^@q;s8~-Zc%UAe6OCXC+C3u3@W>g`Pdl4)n1-r&+^4Io3Vgd-fDNaFp#i#Tq__T-F<h#_Xx=y9y0q'
        b'HHARB0crHaB<H7<fkByhl1rtP?XTV_Iorn$9AbO=Si|2q6!mh|Zr-~hUX*zw7z=TiekcO~NK+q0Upgv^60buU%9|BC{CMu?S(XS0'
        b'>S1<ZAKUXM*4D@Ee_U@`nESoe%jNVc&vvo{jciXRYdFF&zX(>muxREcBslxC^`<C&jO>G0!P%GDfjw-GpB?JrfYlTQM{WPpdQ-GM'
        b'Ms9uiR!*<{>`UxG72C6)wY71&HM=2Og}yJ+$AqPC&3QHKY%@FXJGQ5ZMW*^z(<0H2kORxGX1GW^!=Gvj9rTjOaqr+#<{<<EIn2MM'
        b'Fc~~RgSkkJgn0nH1Vsiu&b&2<#MMjWXBl>YVIdOuo@N;%KgX%?=M`n>+2>Ki0iOU0c(dz~9fUN-;%N9}O-i$FzvS$*?7*{Z&o<V#'
        b'ie(B>S+FFgW=V>rfs~L+OGlNgM&OIx?Oh^ENmpeI-o39YuE@m;-<l?|)%PXk9~cbnWXjMQU7U!l6k_}H=|Q+$jVK9nvZ_^9Z+3rv'
        b'cE5fdnDvX|fee|(zD8brHvR!jlmk4^mBhy%#cbJN`2H^8kPe)9!-FRao14;m!#y#r`<jm=Z(a<mU3VlcZgWDvX9;}lKGNSla0WYe'
        b'l=&-iPR0%-Zck+G1FBX1qHnomp@(R0`dM#;Cl-}f97&tAxusu~fJ%Ap6Me^RKHlF=uVV%6P}r-!Kh0C(ICB2-_2&DN9oF*}SO2tf'
        b'Y~UM-oodmZ3F#A!&jT#w(H6~!+6Ppc{?^Wpf!6Jbt3>Z{bfP%^0r^=KI}iuw;29szG60R^g%VaCdT$NAlOAtAKYkwm^=o!IPWG$5'
        b'T?gUNbhdsApT_RfC^ryqM_i2ULuVMTDCeA&u>%pXqHRcn4k)DmLi6T7d?<JiJOK1Yi9Uu1qRVr><+=?6<^Y%L%*tz6&XB~8B{|Bl'
        b'awbPHr+hNMrlE9W!}@ege+ZZc%Qy6xD5CTg)x^)JM_QZHp7d_-Cs(=#WEb%Eo{!`$f}0^{umJDQyeN@q*D+U7C!B3n-d9o_oidi`'
        b'(4E*(+VGnHAn<k|L(3zr30ZCZ-qQ`G#~O|-UDVTG4LS6lFX69heXD5Kr69-95>whD&s(1LTECT&lpas99G4ZX{Xta}6DR!GN=26D'
        b'H&|A!vr^>w81Tq6>uc{>Bex57a-Ry%U~QjrMK#xHDw6f}N%IH$OWK)d(KK&7z@H%@TL()6l$5PTP<l;8&gIX*u!(QDJHB_$zEwT&'
        b'R<-Q2*%+S_H@FY-z~Y)BvA}xxR<%+L`F7;1Oh(;_4PgY<mpT7i;_8Nop5AKOi!opDZtotR4IeQ|N0nyFqdpzzss2Wq^{EQAX#Rm~'
        b'Qr<fIr)uwk*9M-i_CE~15sbVCKOtu=SGlH=8{XL0QvFz(D?}qtn2+W))h|eM9rAh`I_8Tm26ai=F|z7Oj80T$$WsSo8G^Bj>4*!&'
        b'8EN3O%zwIkVi@*n_*fSnc#CKQ6d69tH&TK^<AOq3d4VW?vBIb@86&NS53T+MHuM81k68TxHgpvf4we@h<&a~2xMD!%r{vEG*2r&)'
        b'&;a*|HZU8U>XTf>>Bsj<*DnYm7kJmZiwv1-<b?yVYXs!H3lXpYxe{ibH}NJ1>sauTsPOdT-e!0HdUxp>S)nm}ue9j?G}GZj>y`70'
        b'o#jlaxxe%&ZRx81{HKKDX8Fd-s8u^c^7D!DRr2TXlI&c9)GQCz56Ct?U2Z68*bqaCtj359OLk4Wj0<(Yt|nI$6S)z4Ufngb#;7-j'
        b'SdCF_X}Fb&Dx|_;>k^YOtYcuMxX?I%*EN?>)&&bkO-!l^DOm-r>|9l7l#$B|2a;OkYXoE4Cn<>A5Plx5CwjS0rLdy?HTuJcau#8t'
        b'!+<38%M_ydfQ--^Baqf~`#_&?&`ZENM~zB#3f?i$-oq?G%fMTdvZe=?9;K8Ym_zgjLFv=4WtGYFZ6K#<E*$>cCB^3a?DOROtoN%%'
        b'Mu^d6irgiN?D#$$E>c*Xc?SmzD>4O|NlRXXDzPCx0y8)OwYCZ}5iUwm+o2DaS`r(w=ymiO@Ig9F!`IA)T^Ep?{URX6qTP__qBFE8'
        b'^%p7=<P@l=v27+wwz2bIA0|4(nGS;dhSy44Wd1fl8ps9c5QYL9<fZ}527zmK93J`c3`T~U+k*p9RPwJKzVd<f3oub1*B&VEAy)(j'
        b'Qrc8_M*w!Ny+>9iFn_8lU6lfxu~K0hJIjqOYW{|G<y$(IY}mT%+L~q7$E2=h3pNZqPwXW&30H>L_CZXB^f;tXf&h(1^VTsCRpzHc'
        b'(L9c+;2MWX2Vc*CJG^T^(;^5^vghPuJ0Wbxt|8c9HWwWE{|!RuqLhkDGdyY`SG6djlA^o^GH|7puQ{4!MQ;->DhyJ%<_CzVGKd*2'
        b'Dzdl7@l1+~TF`9Ml;g198+4Cs*ihi7)FvtxRz5f&8y5k-@}`adEbl2gCtfLfo>(a!f)cp@065r^>8HZL_L!Zm4#$+s80Oq#^X;)Y'
        b'8c^Wx<|eW6U)IuWm1u&CBb>0|tk#D08Eolxd0q}eAJZ#fJskH>xy_|Sg;#7c&WAHqVH8vhL{=C9gl25pPv!xF1G{FfN0<RSIP`Z;'
        b'w3c&jvXxe*G>0hT5;4(7T-MHp($<FNBPd#-Zp4~pPz}Ay?V7TUa$xTqbW>g?#tgsZa#FFOO`LV?hT%8poSs^E0Ury`eb_`re1u;N'
        b'*RR9k6xh(i+;`Qs9@ge#ZG#8Sw4EX$p+F~Gi1r}6hYgi$o;JN1iIjSesuU%_fB4qW+#pvfwlKQt*Opjgz-Q0etVSUles+h=ZnO@_'
        b'>~dzC?WWW&I3t2m8<wD(c>VwJ_2qF*UD@L=FRS5c6TpCg`Vt5P)J_OaSw^RjB7)X_A=L;>7XpGnU05YR(7a$FsGTpMRiO4ed9kTL'
        b'Wi)X^ES)4+YAwtF)^(s&EG;_PTD0!)e)qnBOTXXG?;ps!%em*Cd+u58axOKmNq5nARrRzZ&nYe-SI11q@Ih)!!+6LTniSR2Bh*w3'
        b'%9!8bFmh-ThbouhYot-|g-iXut1O4`9UZVmX#PE-M3<lZPDdt?DRt{nWdO2ciDVxoS%t`|@>f&^XGj94Niw+Bm?~&S(u)nPE3JR7'
        b'YGV`2;YSP6x+KeIrGbsi9}e=q@Bs^(WqqZpjo0WfXxxYxSj1?xDymv#z_j@@{Jh0)aEN?ZSs~$|AU3}Zy>2CL8sMgsW7K-n$E|Vj'
        b';XEbh8o)|MWJ%hr3#xii(AqTveP82Y)ga~Dc*D>=LP^+&D4lB%^Ya3Zs<M$R$%eekyMQW^ba_|L_948g(uRbNAK%A^aXqbcIMQ0G'
        b'g1<Y8Wi$OD(Sj2m5F*g9*h{7dl}2Kem>M4Us(xV=7$5llJ0~Y5C23?Ytk{aEbAK@~z0?;U>wa3moqc=VSMbm&@bAIgbjz|iymK@b'
        b'4Yi(c7JI^wTU_AEvqhWOSa6!2RYL&#9xmHnByA4C3C1}8lJFM0*JYGs8#L3T>6EeVW|Ld;>JZN>?+Y6Ul|!)Y{bZiu>xpeyRW~T4'
        b'JqEx9KtJYVKBAiOwrNv*Kq3i1CH0)sjRkWhV$T%RrFH>QsxK+fm`cNvCR1<op^xAQu&f3c&Yw0)tbPTP)hWcD*SW#;Dn?>-TABse'
        b'n*!6L=;*uArWSj2bej1Lr93q^dRfMRiDd?=P=j0&Ub!pmWnyjs?MBj~rW#1~jR&s%*kxq&Dm%PX5AT=6D8#~^*V>qzIY7d(bfXUz'
        b'RyV!U?s+lb^1m+}UvNA;ByY$rAA**pSuE(C-tmu1NrVpphU8+BK`gjja@lCm2>QaHSqhwGAM=-#a~|6^kAJ4MtkwS0u>H)iz14oG'
        b'HA6Rg<tMwN`Th2omVg#U4ePq+5T^~bq*3P|(eWt(F50u%hcW)z<4f|g?1}1(_3WOwHg?r?1krZYtuq+9qW5s8)dR=rPDAOQrdNjj'
        b'r!T!fr=V-mfWMp5pWn$VWsG%2w4pUInb#>}%#KzFRrgat#*E>NmjHyf47DYAX&2C@WBxA<1aa&AG3#Uf?F##$6N0pojL(-3d!Tj1'
        b'`)NN5Yk$Ve{<i(_p2e?}3KJN;JYWaiqSQAY8PAr*mKkf#8t(uE!H+wf3luW!KLZFtr3UHc0a8n&sqVWJn6KU6)AN-f(ae(w3k<>{'
        b'iAE-=+tkUzSQ1UJK@+lo)yB4I=8qKNHu3z9rslByCrS*aT5N@n@e;5To#J_;%<*Yp{CcwMH7{GDfWa7K76%Y<&_On>l3Oc@W}pXN'
        b'KC}u9w*<_H<t-{rfLY@|d|EpIRDw7H@0F8_-q-gCOg#d1&oq7OF3~pOv4z3?ufOkj{e4pKzHQ$d1O{ENAHAS1Zs3fH>NNq|v)oEP'
        b'cBAE|{fIF7r2WcCApqae3_u3w)}$K5Ari67kouBAyhxHdqozqB4mOA-l2k#>Wr=vP?VI_qv@y8Vpjj*t`x7s}AABQ{-{_MPk`q<B'
        b'>{7?|GrqA4FsCNMpjqV91Uoe$PK~T{TGdIwKO~AxKi-6L-USmr*eqV0)-D9Cfd2Q+cytm*mlMCd+s8}v=!xiv$Sv0Xi7>j=E&-aa'
        b'RoH4arnYw&092nD5qyJ2X7G8b!3WUU&?HC>F=&E~P1#Y}WwKn*s!bDMY;C_hdd3_w10ZSBNC4SD@5aOdfJl3zKo4)X?y8Q0!G;WC'
        b'S#<}zfOGp3i>T~31IeiNK{@9r^1)Vs+5QIjuCD!CVf2t4^!mz>@bX3YnoHYsfb+0s!I)+~u|*FMkK`-F5deDtdQ3b&B_uLcC6+0~'
        b'i&UvI03}u8#kcjlBAaeM+NBT&2j}W3J0NNlmC`yaUXb+t*3xBwx)|42rl<THeR85Cnh=#H!Z#Llb4(Mwc!v1=*7aQ7Zy$5xpc5|+'
        b'Hnr|*e|cMLTB{IvEVdcQ={dH4GwmlChdOY8G@vWMZa_01An2m$fOtM=Xm=Uoo1fKDKlu&;J~JKKb$s#RxJC-&b3UP-$*|J8U;=~k'
        b'D=3_W@w)|}IZxne<;m=rQ4d^BqLC3S%)Nh$o%gMs7C)z<_?ZF3&tRFct`{w9Z<|J>Liw?y1M|QnCjWi#PQ&cmAtl|{C(l)!mdNG1'
        b'>|Ghn=+}$~?xUU;S)KgM2UJh1OcL(S!F<9M3@l_a{$@L~0-ZPSn54uU<RjY_^e18eo~@2OTWzNQAy;oDRzVL(mYeN=F)TOTEej7E'
        b'#<T3FJ!BziKe}Qq!i9v~t&Z)Wg1LK)>e<$F6aeaEN-s{hcF}%IVLb>N^|;8)p$!4}-qSDC?#qZMcU*Gt0DXY38wLh--3NzvYjpov'
        b'!D-`uz}5Bx8|k>GsJ-g=LScX5R!1Rd<SeP!O8fz0)xN2$731tbS<t^>t7ARL`W7D3v-u;(cV(OX8T%vBof4mc`TWb5FSM`L57{4t'
        b'<qc(+n(gh5-s!CeYs8m?MEe#fhJ{9Pvq!uCWh2OJa2#qa1XB2NWBX@~ju!vE68rHc!D+@28yY1w;*pz_QQQ-yUi+|(3kewL=GLFM'
        b')v*FJ|7+DnxIC4>Y|hQ`H#H9fXe}O~YtX*&X8`-Q4F%qYQ;-5gA~rqqSLn1oY7T>I+S2z>qen|vs<Flcj0p*k^dwlNLAchV;mxwL'
        b'_2>%zI;GKC5*aK0dP}oEE)$r{@?e7SpqI2_uob{|g(^JrA%JPL4xXv+&Tgz5IQ680wL5|V8ejse$#S1kN3r6G1b;9td7sz=myV4|'
        b'8TBTH!QuJn(I~sQt`SJhfv=wQaxk|VYa^NY(}dC5K=#}in%2vs!QY|WN<<;RpsM<rnp_)Zm?cQ`w|FmeGPo<^T8EJMB(I70Shl1*'
        b'HgV-}Vyqowr_`ko4IWD)U(ww!1u}}J1aQbN0DZ0Y5dpd-FQd;i{s@G_D@gzOO2^|$@_41qbecE<?U&`Hd28(T`zC6$GRm@+9%HLc'
        b'JxI*T0Nka)R;V1_qs$b>CE&V3>ltVf%fBby=I>Z$II~h6FKE^PZ9|-{q}M=AM!EhV+kBaAZ)K$A;$&lGjl-0MH~Z&kOrOeKYem2!'
        b'X^CkL>ttiEXC|Ro)dP=FW=mL0QVJtS_!RZba{zUtL%ocj3_8|RygVg^NDfnJre$l=5_c_M)wC+bBk2ZwBOuKv*Zo%GpAyFT2c=Hs'
        b'X1``6mLA)%ydf>yuDjnzR?R?=2I77rtD&x>QH9Mi!)2F7VGCpV`N`fiT5BAZe@?h%HCUfSwQ*~|#(}jnvJ^EsD)<d#+5`KZS37S8'
        b'>DSl`_D$qvWo(1=DLC~2{9ImD^#fF<Z}Z_^AF%&{UY&f8X+7%KlPHA;w^b$vXp@k_$&g~j*k*^!@@TH;1|kXMCpA^7QMkVZT*iVx'
        b'A8mDBeoV<9QO>JKJK4taU3G<tsLycPt!*$`q&kG-bjSd1Z5)e|QZHkh%5a0wz54h8Vnb!x1)*bc<*-8zj8sqra^%Rw`OAoIw7O}Y'
        b'Z%JO>U3l8V^vThBGiuV`-P7bV+An%%;-VvgG0ucM*~S@JO^KrDYfy%Z6Y7R1qVy;24p+<DCT!yA@a+L60)sslpqxN2jtqr+y@=LH'
        b'%+n{92&%n;iR?<PQ(qzg3DtYP9~}_=eLR72aTqpWb4Ej)k|<H`leizLQJZK6%rigB8~HCvbmnm!v`e5rG31&9xDuC`7y|*K`T#FO'
        b'fcJ$)Usb@&)FE{?_o|}O8dgcZUg<Q)XWnsJx2(zoaWfj$c-sPI)xIC&n*xuzt?}Bn-N=Imvx=;Kze5r*Go(=x;3G5Ojl+#hRe%Wd'
        b'Fa&t5_Ab&(W8kf{c`_97jz;#8c&ng?mf?~BZ(pOE#IVLovc{Wpmr@1zm;+{=KHBhp-&?}kp<(^|87dPpux2K()eUPzphcn;zFJ@n'
        b'svJUlS#2!o_tfepwCbM}XjipHBr~X7pn!dg@vDBE)G2@mmLDFuO|1aRMqS1M0)Zukfm75SY;48$%28$~zr`O~`@o@KnNMX~_Dx{E'
        b'AEPE$2;oLB74^2tL;9kd7nK1%#$BI!dp7v{8ZpmkBktC?tx;by3>=3Ve=Ig34CCqUCcIYjW<o|n;q2QB_?(H!yWD_p;JVo;WlF^d'
        b'Q*B}vkQ>sv3HZw9bhvcWgm(WCft+se$ACexRJ#(Gq`=@M1`WU}tq<nvf5v^cZa-Xo0<8){Fz*^*mwDDO##z0<l9s+k4PM4(gOt%2'
        b'*b9*An(3C^)B$>B$fx{mK77u?0EDInNc0&~wb4!vn5LP#CSafk<tfI1|4SE+pxr|h5QH`f_w*-be-C0dBzn9OpsdUg#H#>kWri?5'
        b'U76vYnK>bgiK*HWd`;FBEy07k;{G|wW7nt^{PeD94tz%W>fa0lVwR)BVEx!Yb{LcgDd|7ml<BPQ6BLYXo?=bzT3Wm~+1hXxSm>!W'
        b'$%nJ|CmIV?LGGU~G4Gp5d^5(Bl>wZB>Z7xgs~hjA(!HTZv)rJPy9Qe|OSYt~5~OrxTXTqHV(|TDYZVhoE`i}W5%Jqw@Ktz9mrJ~7'
        b'cM)%G(W?bJj)GQ<ceEuX-e{E!$$wBWdNwahkW;5t`vHt^o;&b`s%z23!>9M9K(E5>=T1Q45r1k&hpa0mehb}A;Ozlwq#eUES52rS'
        b'J_i5k$?w;Y0JG$4DGuOff(l<#>dQ~sHK3TKVB!ED$gkB+omby7T+}$q4A#FG$P$C@H%q6RDnrms?@%X`pse~gR<b6WOu3eGC%H=_'
        b'2YmzhgBG%jlkX&E*^>#NI#gZJ5AKX!%YoW>HW)!R9qd8G7Zw~mP~wADoug>_Tm<r9JZ=D(v3#4uQ+1kBY1kwA6UHO}&ezybT$7Ys'
        b'SK!Rv(~#%eYD!Eqtr8^u7M+-wX83Zh>PtMOKiN@pH6<pw4qIyMAJtU<G383K@cOlsI~-scn;5|G8x~_VaD|<nIAn+NzKvV+YrRHb'
        b'**IbRwO%Yx-?%xdaTOTiK}G{Otp~F87vEJElP>(RBUy9lPRg|^_*f_KrUATq4WfU51CNUC6(~-F%gm)*;5z=(es%RnKyt_Zn;I6g'
        b'OdYT&fX*A@_M*`L%AOGMCpfz)L^qOh?fM<gK`QyIk;q+@ayI!+n$Zq^+yPzBjRiwRfT5}?q~|7s5#JS5^wQG1EZuKlERwEl1`c*Y'
        b'S9=%6_j-)R%|VE~iukkolY->K`+eb|r?*~*7i5eTaNT4d&^j|~$P|YWO?C&)uu3B|N|F@`{VI)zLE{b}rX$9)$%j`*go9CgI$A5i'
        b'(69{$4^%h#S}ze-FAx{6IqnhU9m2BLjb30M`J4it4$ZgNY^P%-9X)V5wYy`&^$FMKd#K%K#*@)N_Q#+ZjR2_2#Fd39XJyxt{=PYQ'
        b'pX@Bg4?ZmGN;sP+5hOKkPK0dReFNHb#<S~Ldo9bd17`}?^RlGE<gRpoH?LweExRyx&AQgz-M|X+Ti3dFA**^fyNv^}Q2JwDcSGsr'
        b'2^J6_nJXq%z{QGAMh?UB`o#WSBBj63$XFUNL*?(D8oRWelXJG_PTXzEwL@XKPN~Ztr)Ny>{ts+FyUXiGVgE_Oagwl}B*=9HkqiB#'
        b'pnDO<uH&OI+Ozc%ztpwsQrAX?YBp|8GYUR8CZ2=m0|7KJu|B7EZ)1R|=&g^I2tc1uFp4xmu0bUSvCTfLJ-hb!v7EDUH>vEyCCBVJ'
        b'XV>!p@fkF2;boC_YWK2n<JppkQF<*T1~~Dvl)^-n#z(2~2BI%r<D0xI+aIWQ->e^Js?#%2j1|2S2VG7#0YjZ(I7sEx<v7wq+)ofS'
        b'WQ|pHkC)#4Ag6yMY(mt*gL56s!}Y*up;YNC^$*Oe?+^q24C^}tSw=Ybza!o37RLuR&6f<Ni4naDPgD<sCe$B3v^iF`F;$wGN{z^}'
        b'aW2pf9S?w^sDuY|Y>wDAX1YeG(zuVTpSu<qo2!wl@x(<BYdk^b0jO(6v_MmH5)ottzx!J%yR7OmVDNMY4wPJ1r%O$!L+%+Iuh%3I'
        b'?+{~RpPHCFeVX3rUlVE&dk>3e)rg4{!Y20Z<(C32q8o2RB^r-(ji>a^gt}>Lpv${$`hdpIvS#jp*l%!~f$8OVgD_m=*o_SPX}psI'
        b'`Sw*x{pc6h<FsZ+1o4FqE(y+L*qn>Nr*!RHn^O*cShD7(JL7@saYT${&NW`GKL8)?bUGqvSLLcD3AD#`We)NkuMh){2%Cf6>xu;M'
        b'uY=#9H%ovlxo(j7#MiZFA38F;*R6j6;aEVB7xlLNuM_9C(1$M?JZd~Z=Muu=$vmySky-F2KjAg3r;S52K-31=TBpLfD0`rEOzD)%'
        b'hI2fE{oB|seX;y7EwDt7ZWzw^CC1A2nLDH7a5Zb9s={T58iaCaF`_m72@Xps1(;<8-`IcJp}x$jXL^lu>tli%GH!7i$%euqb`66r'
        b'+h~<uqIUC{*)hpUn783IubhmO!ZxPOiCYrqVjdr`@+vF!c||++n-=brn~HXX<QP)w;oa{QeERx4v}dgM^aCbDKojH=W8@90hu=)U'
        b'vh#|V(f6Y;T_aLzyi^*`)Sm$-VVr?a7|u^9!+xaxQv~x-iD#~!gI2{L>P;dgQ>6Cv0Tzo=>A}a?7$>dBek=&BvLm0zrRCin5R05*'
        b'PhiAyZ!zgT$lKHhz%@xf<EOsoCNeJgwM7rTV{5aXyr6gP|NBUy8`M-E{wP8@5+vE*cM~S^U6odX=dBu67jxmLF;n2yoDy)hIu~-}'
        b'9RP8684eV(wi@9?=jGLvbi9$jOMkUqKj4p&T>z}3lPg{B_7oSk3m54q^)cJD8(L@pr^fm-ezoeI@JaerqKJ9@m3s0hsQOJO*Ru3!'
        b'RqQ2L6$XNFfL6~xm{XMjpLY_^jAuv39*s`Cn|SDx3m>@yQuxLy-{dRBGq=YoH8Z<y)K?$jAa#({->7#q0`9s-zN#k{Lk4q$CD-$T'
        b'?W$iT*z@5Tn|Nk)G%MM+oqZxBd8YC;uarX0EecdtdtUF^-@je&r~&nFbAF-nzM9;=wNy;ZOVxe*0e>kQIw!gxpe@)yDY;&vZ$~g$'
        b'cM^gq{SiP|r$1Av;az+UjF(j@b^p5V68W`5^eszy>On%k(h-}G6qBRJ*kfYRu-Fq!`-GU3&=hfsFogjLCeZ-KaJL+r_<+CKXO8lW'
        b'A0~=cS0+XmslWYRb$VrDT&3tPH%>>z7Xy<GOkkj1;ROC?IrJ)>@=i9Kzw_oQor^kIa0Z8fsT>cdXz*O^Rl@-UxF+DM^eV`x;6G`a'
        b'oXgUgpuL;9jwO09g=sr#93<>*h3(IbF0RbWD^g#$pggk@{8lf$K;IJuRuvp1E@j$=@1RSHFgE8~D9Zqw)MaO-tsUOc-LKF)UeQ~_'
        b'^_;yRCz~t{(>ilr%br;}mMrb$=Xj<BU_EAMyg}nld|XcNB6z2Zy^_uGoP?|KqJ&>XGaqhWVsk{a0e$8@;yoASi*9g}*_?+IvVt48'
        b'h%z{EASZD>pl3}?+N7LJ)8DNT5&}J-a1A3ttQ&W|-<3j0NzgC#w#x?7L`g&lFx-u$wqSSj=|MdaBbtXCB4XNe+&<b?bEtjzkkQ^i'
        b'n2Z^FBG5P~1-#O-ERL93!Q-p~cH4Z6Mu>=pINQWt0IlPm^XkQ(U<!kYtb4>^1GjKm-Vw`JAHADbwrlO4m=<ZvAGbFG&P$((?)hlA'
        b';7c6*sGm7w&oMOa8_LX{D=HhS&9bMjLVLMzI}3o%TsZ;zn>zjhKh8`cYma~7mId<D*_^Dv!`T+MtQ-s6&$#f>r=W?FS4_T7b3e?s'
        b'_-0kXbJYYxYt{spt26=X)mSz_JY9oldvpR7B~Ew9fq;Dpc41f?Fy;^pv3i;G=pTjt&+f7rN{7I9Di4O?XUy$sosWS`Cc%UivZTpQ'
        b'XS{1_NPis%f}+VSJ|_Rj7NrJ{Pf|GqN{v_vq$^+fEyo_qaDJKB$<B+#6<yxgoB@Zn4OMF9C^U034^nUQci-U7$7rXXxCukce9Xp}'
        b'0D?jjp!_l~aMoH3Rfq$ySKmhE@9wPfM3C+K!<$%IF6SF)w^;7aQTtE^E+@<TKgO@t@_q!Wrr~&V^PY~uh6_ex<9!40L%4v&C7`9j'
        b'WyY`SB)U#6P-8V;0lkq5PauapcCB56zPsgtBT^XAKP(mxh;he%Z?XPm3;EYAkqpZ?ABg@o*2wKS$^BYKPe>^c_Yr3Go#~w{C)5{~'
        b'u!(t>G2geDroXZK{<5?7oS=fQo{j6S!|PHjV3@Z<;~xXB)*W=y?37EljCXQX`>4;O8k}UzmfF-^Eevb)meHh(F^<A5WYLy!cIG{P'
        b'v(s9zC34_Us~~c?#hDkitCJgk6t!J=5)otGM=3OZ5lIToY>c^oCNGq+CGA6@JQ5!Rc8|tq*n|!^(wvSwmp`k}c#mmj0b?n%f%=%g'
        b'+lQa!^Ir<F-+WA=!4=}!H0kR#feMY7*ilBWHwV^h0^&}B8N2;(8!Pkb9MEI`lrS@slNBPcb<Kx&8L!MyFGC74+)}zCnBAXK111Kb'
        b'MD!8J5CGPIMrsKGezWfEyjIK?!{ku{(>FWqrXm1)KrB@s9-UXMKfDvT>w~8UTl*uoI3l-LqqdM|Hxqr(WPf`ar-}NQ8Fz!yjaGk%'
        b'0$px&>h-(S&C^^I9LXIo*hd{`H9G5l-K;O$MU!sc7V9sY$$%~JI8o*>zs`S4va=R=olcCMGLSNy9HY|U$w?}W7?6Io7ccb4=Co>|'
        b'JOa?iQ^5#IVsBBL<=Dd*fQE@-I8DPuV9wG8!I);I0-kX3l5T|@duDKoW20Rh8@CD&tM5=6V1>GIc&hz3PA>iM4WE<kvIiI#3!CZJ'
        b'gSnX<i9|ZArHWaL%~WZ8&5rDmujhzb88%do#QH}s&xk&hhMe?=hSZL6mzCpmWZS@WMWr4S>W+y5##;3S4?u65BOA2nHZd>vd>Mkx'
        b'Oj}*4KKDc|;)t%X9iyAApKboNb@MQNa)cb&EbZrmISar*z(>c`QIAxNrJAoctIl!ks~GUGxdvA`;vsz;0yv&u0{%&ay6+^lJNLdX'
        b'ykQ*}g~pwwx_c<y$m%8-$S&O>aJ;*Dh(Fw|rA^DszmM;3y*nnBfHqZPf6(}azp;P%5WXAx)8E*uKSnuXMDzaU{H>cE&dsEAGf*SI'
        b'KTKg{eg)j$L@=_ME5_A)6l1G2e(=xiq|Y~}!>!jjs&1`HGZ$L`*gEbKrIKL7;+cu5y9UIb4(n#p=7NNbvqzkKqf_$<^hhvH&Opv^'
        b'jWc~8wRYxbnuyJ5Fk&K3pWuQ6D2HS5uTpq-;(zG711<-Kc2f>eyF(Z|9vPh&A28m2Z%!v4kowxx`7Q_YU<?>*w|5<_u9-en2)?E?'
        b'`!=y+v!iyi0a$>`HxEmM0}=uG!RFhKc1ceF`bSSLG2I(i`;0d@t!0~yV}}|A`fa-!opmn(q=hX5EyJ}&yrm!dkS^2Jpuwc~fHV3q'
        b'?k5WK1zhlNs{04%qk-{sO}UYV@xez1mRH@%%`Q_PKv16Yc6n34_GKgprDIdL6Nt(mi=oPvve~X3?nx788U@mK<VM5AjJSssxA=;('
        b'iwEZV$lt(RA75IWVD|TDIIJ==3?3-t7^ASZ0Z(kiRsNohj0S1)OwefEo10sN;6Jtiw9JA#8Y!WfHz;G*-W%d;Ww;Tq>4NX|CLab)'
        b'c~VUbR$~T(Yeu0S6Tc4f1)Ten=aeUv%WsrH!e7C!cgl7oH}k4@&TN?`@%NOWJq2*hYag6Q(D444_W{5A9tFk)7~Ozw&=pr`u#q3f'
        b'cSkWzt?)QQb(5RZ=?dch-T2^T<+n_rnbOwaX{|!jr+5ni=}l*+)Mb88J-u^~KvbY!BMA}{lAht2-o=w-Ob@;z$?!<&T7DK*;Iwfq'
        b'SHLtqU&e%1As-M&xsO`f5Ud-H?@Ic#tdp4-izjr!eW@`D-qC@*8iWz0MNN-f5vVaw<!hYy{Rzy-{Q!hJ3~E)K`41z}#;d6#_Cx-Z'
        b'1o;~4_S?9UgM;)YoWui-`K%&MB8*nz35=M~Qj-~vZpC9dDlm47I9h^Zivj%sYAM3t7(nRIbxWiJ@al=r=jyV13s@Kn44P3|y)ZwS'
        b'tqk%JeK=i};nBvjbw%T`N5Ke7CF84ip>cmiFf{Hw9FRSkFdh^hU<m~1ErIQW#`kBsgD$Qs>)%@e`q(D{-RvHv`nOj&{!-C5fDd=c'
        b'z@!8nm#!ZN-95kUL3am$W$faP@{_x~MwGs>@IK}3T`-tIjj&<nfCsv*(J&234o({q8ZI&uhj75kqq7`w74YN<2Y|}V9zXB%WL~Q1'
        b'%f}1&oc)x+-?PD+4q`{ghBM0QgJxGp>WHOfddS9bb-DQy;wLRU%bek%Zv9oKtZJl`{uuFtR&{VfAB!t9FpQ<l5CSsb_^$X*QuYNO'
        b'R%Hm38SWzVHt6TTzKOor4A9&D%nCr*VSf*YKkOYn@bAKbZ@SgJm0CAeRY@W1Y#al%PT8%e=ryZ0w38`)X`Eit=DQgJd^-83+sy&9'
        b'h+&8j_?E1h*<dubcQX3GWHM$*)_57#i0apP!&&#&2~aDQOL&)ww^Y<z1*L<@2CdO3uBb3*1cm_LV5>nRGz9pGOF@FWAz*e(ok8P4'
        b'NGpOJ*kXwz!o|+4;Qq#64H}-*2FCwpsyRk9#P8+9jFCeiWiZOD@x<JnjzobKm^c#6%#j1*Fod0D;)&~BR^ScLYh0i|lSf$@<ECY}'
        b'x{TY&_v-=k7xN(g4*T;qE7EFq$VT3pQ^6NKVw;_K=3BrzdkHuuZEQ=%oWayk4rGl;#)IL}fs0Nnvw}>i7+K5Dc4}v)y~@rFiyVt|'
        b'Mo810ixlZXg~X>IU65QEVN<1hCx#6x(r02!MY>3l?zMovcnS(A{CV=wnD9TMoc}^X!z(nO>l7Lfg^33>x+6YP7&@lADhKV2bBCsO'
        b'j)05hp1E?|chzG4?$(z?sWb2>|12iT2}dGg`hzMW4G~Gh4tZpKFNZFj88Z$F`b-~nV4^F1znOa{7IRInK&QVa_lo?k{L`I#Q-AH#'
        b'IeaRteL8Yh#g!{}Evfu<`>KMFi@)w&KP>UR@WqT@PwN~W71q-_(xU=c<pb$JBMbI^JS_3M@P+VKht4sh!fMx%Gb-ZfSb+oSegk45'
        b'tUMc5KB05)Dy;1~l2-vV*FgGg(D92`M=O7tJ>yrK&cUp(T6H9|BJL`c-5*gHF7o*GfbQ0G2c@%qrXwjGyzBrB2&deoc`{!aH$~y1'
        b')Db9#hN%_I?$6+z_=5*vcxV^T0_u&_QR*h%5FfCG%^?G1s2|_m#5G0jf}(9FTwjehr-ca<7^c{xSpl#1|5fLBM>p(<?>mdr<wq8P'
        b'^1wEZ-);pT)#K_j%!YhITxvdesk$bV)?w6>n`P!0jyVaPWhRnz*lc|mu*3i(#$!wx1{lhbDk_2zY2HEaLuCa#upOiTE{~t6FHeBs'
        b'gs`Psfw?fT-QjBWukdWox>kCtA9>{}gEoGHl$yYit&~|aA6MaE3izZu@|>o<L;N!i7#?<HD`5BCXAoECD)>uxa@LvYjphN9$!Tin'
        b'>(|>IdSIL+T5zcWmgT=>YTC7Q)<uxk#<BciPJ?9yzmcpzII+haty+wj#eqZ=oDcO<-~A`hxFSRpFumbRa*M8$X=)Ut?Gu_Bane%<'
        b'{x*JDFZOFZS1+DjpE&~ps7E>Tk$PbwIbE052+MUc8yWCh4!;M)fu<H5!&<~`)4vve9a^t>*``_G)W`=ke;{VVCa+#8sTaR|r9@C$'
        b'f}2Y4(wKZgHz59lyb;f9#GPXKrKCnpPJRVu6EEl~s=HI3RxX5Rt_bXHjN8kA9b%W(Wp1QOn&2H<85wK=QucES0iKKx+I@los4Sg@'
        b'cH61$WAJw;b59t<_b@iC`y7SuvgCbo6dwMKL<WS3>Q9ghJGm0^{I~;PFtUP|)v<N(9O1X+f~$Bf+@b|-S=`2VpLqxy1`;AOb6oxC'
        b'flVx|+oJ`1vd0bOT!H2eJ9F@fI`@9PLuQV7*_<S5w1|$};(SJlwlbActYAM9z3XVnwE6i#I>3>6u>xf#7SmboG}X48YZ-|S!_68g'
        b'HrqAUz^AlmD0S*s1Q}`3T??;AyU$ZlsY%ePZz<hlfYCW1>(n>Crx_n0C4FZcet$=sVi4nO3clY1^l;oJ3P}56`rIOIbKp>bqLBnp'
        b'3cEWH)0tgEEP6u#9e-*|xXN`xz68d!Lc<$*3(k}OWuL4Ze-btDEmJ9(Z69JpXJr5rC2a_IY%Mnp;kVdyk^4{J-u7@%lbiWqR~!SH'
        b'5hl~F$$K{SlG&~cI>4a4#fi2Tty8XzWJxzn-NP|U_#iVAn<MgJ^gk+hJSw+7DkqD|iF{~JrTvIMGlWMrK6g&G*$njAv^j(P{@dk_'
        b'+vV2V<z!Ylu?ALhsfNro)YSX$t~R6`paB^DKa@LuEVuqxPX48wNQT9s5iq0wTDjv|x%G!~*W)B!4}{O{AV^DTy3y-XX%nKTiK@rc'
        b'6b>T@#Nl7%j`QW#^X24{a^f`z^!fdV!imYg(&fizgYsSFj-GOBPdOP`PK5uyeD=iT8Ali1mPfN8-p9%vj&iG`oLo>&gup5dU0&DS'
        b'`isjQo#oaqAl~a*cW>n-pEVx#Dn%2Gh1Exv(^OkIq4wdXyEZ6u;0EO_Xj}nqNEugeV`pDWIGeLC;jkuE8{d^i+aQ2=fIAYu1Vjhj'
        b'#ZbKUwQe_LY5R`@Ce&#{Xe2G~OziGpU>t-0^rh{+E|;6mNRJVWteH5UI`QK8{!I7b{c^{ya_g>g@<|!-5E_%Rvs2^gDmU^Ux?Fj='
        b'V@J7lM>#oGM*LDrkCE)KmzEWARxT-o_dN)gJPnk}DRl@MVIDB;1@iH7{}~6A#E}fCd>qWFrWs1%8;X5Y_^#<L#@U@qt$P&rgo1MM'
        b'?k4z<pTrl~59Wh|OTz|%E~6g<<tfs=6^`sqW+pYRPJJ>T+YU^Lcp@8?Pj{rL81Jgjagrjzv^Ii%1A$EUTcwetYy2|<06q`X8FSU$'
        b'Y=iI(%{L{$H360#AZ&s|DGsc=QkKvkGg1b;6;LSJh{pt#W9+mgJK@15T8lK2Db|{+k-sW60)<AHIhU&HqY!8T!~^E@8yDTUAJ+po'
        b'6zVO@&L=>A0O>NNyP#~L3#v2$3XRm_OBoq8X0^|4-DBuf)jkn5-Ru6`b@q&&Kj&ue<@YZvcPuQoE-WW^ml3-lv6UJWcw45+_;v^M'
        b'n=*ZYWMrGR9?g=aPKgJF(NM!M*4GFH4&3GTWx9_)$&L3nzlkOsjt^_um(Ya;Kv%*HTnRIW3kJD=e;E)Sj*_yz%Qz6cu4>XFPtG^d'
        b'dvNQ{Ozv02AWo8pxwWx~KS7cw?;EsW66^GGNi4Gc6T%78Wcx55UrF#jSTDT`&zi}{Bp}<mr>yE81-u@W$BfktA~SQYsAD{>8@F}w'
        b'0P%R^>dQ|6eohZ`h_xN=)mWd*+on6W+IU>$f%>jey@~2ZR{Q*;`zMOFH8a;u@i6&I88&TcBV+dMrb+`3!H>k?GC7Vfgoji@WT<{?'
        b'41Q7$pPJP#qyv!}d4~dG^b)ymWB0Fg9E>YvGT!8URJpuJ*RjK3lg!!C1=@I%a$P~LoPAsLCty)nk|=e@ggJc<Er(#;{xWNSnOTMq'
        b'TVc=1f0fxn=8Py`crz&UOqtSuP8-v>HNGg?Xuw!Cs4|^lxkD-Z=NJnU6#7;}iv-@zg=ITIS$OJ>Sh$If7630thr*wsC(2qgwI04%'
        b'Yma*_n&;bk=xAX_M>F$;2jNpn-$m9kMPFfUC?SQVeOrkm#Wa9URMf;L-hzoX6w!QIX8Wf9P+TP#-!?9xhRJm3{O_i%;P+f^V-uHP'
        b'QUp^DZ*Gwvmvyp;<uIj!e={VWIsY+4jaf>c`837aG4JT=o!gcb!~!4~AI5GjU?Cze%350n7-aD#*INh${s?f$2nr&U<%0pP<q|rW'
        b'2j~x-BchZ>13vwXfG@hcRo_uasRw6ha*qryEw7tqh7U$qZc&|lvbYR;V~F826<KypzTb`lVfr5`W@A|=zZdu{(i)0rD}5Wa<46k+'
        b'Xyy=>QCQDFusJo%^?bwE6Z#F6SE>YdqtNggD=-)XF1l%b;!)t(NR1Ts#&+;o1U}&cW;GSKjES+}aYfx2JOSi-k7I=DWV{Uzvx;|?'
        b'!bZ@WHw>m<^s$0^221xK+9<Cz3goc@a#<M=B*P}g@_ttfh8R|+k)mtBcnv5v6Jy~^c1AyqqX2JwAxVqNVxr5oOL|$IC>Wm8RDLPl'
        b'3in4JCcIOvi7K;(m$h+-A0SmlH#k-W{JH|a27P*Agm-9$en~gP{nY1-gvHxopx5Ou71Qy37zP$nZ$cy)(EvHg=?NG~fs6l7Wx-j7'
        b'Jy<AN$_kXt7$8}fAz^41*+c;tBJ{xmX59A_P=~H2M!uM80*(8QqMze|=P^x-%q9k5hC_)ffHA%I%=QkFSJuk}-X*b=?h0?mHo&el'
        b'lT6+(*C1GrD_&_pF@2MM<eyaNqtZ@3HixEO8#8kQWdP)T#2s}5xjldrKw3EUGzJm*ODTNuw+pu@pV}AXjZ&Kvlh#oZ3BzDwm?U<L'
        b'k2hC7t20dJ|M$~L3)6;R8i12YJcDx)rUBgxlBE^T+5|A8&l<?SQrw9fmZaIf#H89O`w3>8DeXnSIhvX8N+S^inzlEY=r1zJR_?gi'
        b'27~hM$Zca}{&|`?eHQr-*v80vK-LiVil<^CI1sa`R-&0s{G$lo7zn{d+qkMTYgD;@*b-IlY?Wy}#!@ZQs?KC%)0NB8RJn7NrXp;n'
        b'a@jgnF8<B3f!tXG%d!X7%qcjtPIXFKkSoE03Ud8Z9P6hSm<m)(<mS=lerY=uYAPLd3~^xG4HykRjnWKi;XrXjWkAso0}vm$1A=*%'
        b'%#_!gO7?sxHds)77EXNpyUtibVP|~9IHOd(Nwep}yTorrpj`JO$`xsTq>M7BGpcUVc3O<Fw38VRTDZbOlB!A-k~frWL>|dn>M?KR'
        b'+~dXk15pOa8yHJp!!j&E^m^89nNWAmW`ZHyr57Hr=l7(xF)jaoJo~m)TiVPa<`&b}mc|p02%1IsN&L`q+;aIb=MFt@6)51U9uIO&'
        b'DX_sUpHpyoVi`xlU@gsf2a4MBkiemDmA=i-_Sk>S%gEHMDfMk#+aM)0MYNPPG7n^@cr-HspdJsgs<aa&*u|4eiwFW^auLT$p!~W^'
        b'A&Vrz9yv_iU2#Hb_Za0D3uAA9{)*}u<PtE<z^0!~Y=smyXTzuwWlzVOq?i8wMuq;V6f*coE`8SVW)$%nr1Rc(n$CNdwK1f=(^~4V'
        b'HwGL5KwQCyBtZ4J-tAscs#r5ebeIDpaeac1{5Y{A6&{q#yfooTv5Ww_lN~y{$T7ck!2gX<S!v%T*1&5>Ump}WtlL9E%V&>6gNjUg'
        b'R-Q~~@HZ&isAwY$Ct=7i?2QWbEtN5QoZ`qLrDSdbGt{qCkv^AxtI)TUoL@`?!@h7_c6gFksf?{oXOp5*%W=*MeimQY?^){bEVY>f'
        b'NY7H@9Y`-QcWfpKt{E9PrYO9pqkl%J0|P~Z;VD|kGF2Qy2y+1-NA<$#4az2C^%0I`D<>H6<46f-F<;#@?ov!H8S2*NMj)k6-$q}I'
        b'8ko~1D5f_GVHZx{$7W%uK6oeb06N18<_sK93-4g)#wO>q*@O^d+R2DAfN!qe)}EfR<8_yuB7IAS7$&m-NRlYq*9_tYEU5OGFfu}9'
        b'bc`yX$A8f7Ff=oFEF*r<x*oq^(&LhtSOk~)dRYg)B)-$q;cJXMV5jO0(w^qMHN@qqHo4jCzD9X%ZIPacfpPDMb1<js!Bp&<0d1XU'
        b'G1MQt*ZH*)9ESDb5&zWIe}d47x|>sp;;*%JXCRXqQEYCl5hm84^k?0dTI>y=r0Py-rxIn;2&Yyr5fGeWy#y!hFe7*x4be0Sk1j?2'
        b't#I-iW;Rcg97OO|0j9uPVPXqRY~Ybrt*KF9CiSL9oDS1d_jfH_+S;b=f4vCa!~aZs=vj?+9@(t5pA>+fCtx$}{JxVg^8}x+wXWRW'
        b'DwrzU%yW=h7;9_$Bmf?rXl>LE%{b&L#<MnP$=%wg0C<ztdBiR)xl23Miji;iFT!+(T$JIH|E;yw7t-m6i~>4|*sir5{GJ9e1=`hE'
        b'X5rK~S*f*FYNu*h4caMit_HSfVd~}=Qm2uJ3Oipixl*RNQUF!yZ$l1Xz#O8GW}Ug%%R@6dUviqbFl_@&yM+#+*h`oW2tk;ZLzjCA'
        b'n|%wUbxwy#YqZbe=>S7%1}u&F!kl;L!Y{j$CIO_-X@7pc*vcuG;KK!$_%E1L7p*1VpnE#a<f6~Cx)?3Fr0~V0FfF-s(~C(#S~B=|'
        b'6&Gts|EVMw9j5%v0w>F9dSWxthNHL;;xaoD_1n?O1+xAdYCRB#J*hpb{3;b$;j?eob9|v<kHTvscFJpu_9jGctJLd@cAT~ZAuX%}'
        b'mtj3=FrwtJ6sGIpo*eO9EsV+ydJp#;zMz0ptKhKxSm8(7;LRNg$>7`o+8V}lg0U6?!Yk19(*hleX9+NOeU=?xCGYVPjj+rC2$;LT'
        b'h3RCpHcOq9I+Z2If0G-Faid&rl)H)L5i#I@uA-g^6jzbH#ty2RcbWid5#&V4V5Vq40&2tMAg**Sq6i4b__-PBYr>zd1Fc630>fo!'
        b'g1Af)93wI94G9bm)y80`qT4T+A>pv&89@QFWSpSmC<jL*f#F8r*x1Vo3bMj6G|mrV=QP19GhCqFff4+O9WUNdgzccu%zGp89?`g`'
        b'x`0J?7cPy8kuizOCDwnJY%^>xsXoagE|usF`syfdo&<PPcW<JWzf&zqrNY5e4WXseWFE^KLrP?f#!%qtF}8<s2H^qiuS>vSh#3+S'
        b'Qmem<%>n}U15}ozH`o!QFj|(e_x)xejGog<-QtV3v9Rf5pCCbt1#L4%4p0q3Jk}o4*eK-uL|y)(nSI*LD7LrCTiAP>`%JqAQ~R9u'
        b'+dUa=yi57lH4lkQ40%9|YA)t4AL{;@(v8Jkb=jSmCx*#SRod-EZ=>o#4t}aqt>YNo>rNL)NVGaKrJa3?HG}~@c?puEiAC>l0KJ)c'
        b'9eh7&q7Sz4Emz<M$Qc9EH+kmX(`Ns0BhzNOGQ^sXbsXN-YS~8(HYxqXm8WoJM!3R1Jp3ps-VQnr_yz?|@&bO`6UwDSiikH0CJnX@'
        b'#FD^;ugqpH<L=-;ji=;N20df_TS^>TO8ovqZYd#}pza(=;O=PZ*OfTRO6J2zK2!ebVO;Ib=r1gBl$6*^L1bYG@mE-UuLpn}&)w15'
        b'pI73@E17>1Y6@sX_`>x)A_LAKmu;&-R3s`o#j?~<z@4)EMwxPP70D2_GBIvX7oY{l@{oF)S;Ys1@x;3ZF>n$XiF+z*lkLbVp?p;a'
        b'Jn=m8SL$PaPX{ngIF@^q?l))^nmX{rFYz``qcC#}jAp8&ZCd7kQ;A{rs_U+?Su_pf1qBO<gcAB`bQ!990OpDQzu601Z~cxcFDgz;'
        b'+TEK`O9k4Za@pLkmRMgc=|zcXXe1a&l$+~EEOG%bqV;VQt($5k0$Mj2OvofGGPJ}R3hODJtM~HLdS+y@9{&4!{v}p_ST6w9TZ~Fz'
        b'%@DD;1oM`m@TC<a*^K&)g-d*(xM~&qm4t*{2@^_42r!uG8dvcz`A`8~#*G5;t$e&ups%5&+vT`BaJ_-#mst6*4L8_^0=6Izbt}<5'
        b'2EN(3d>9LkHH9daK;zlQbYUvVMu?t#IwIc!mpwt=-(<bN3BY===^3mCn`l^08rH9yreM|lFIXpDg!RKF>kkmt$aAnpT(Az(u)dpu'
        b'r91HymS7Urr!T_l-(>BFum+xkHQ<7^mxlGtQ&^?{3)apTU=hwueh-bjHng4Rdd<T~1_g^CK|jK#_x0j75+OdH@**9zH0{5!8wHNP'
        b'=G&jr{+qbFH0?jzWc>`{b>KO?4!H2zMB`<d!mFM{ULY8-uhzfV$A(ST1_-P1DXiqsMi;CMSQ5UgD<O7oGSiS6cvE%|{b6pSfOSNF'
        b'6UL`){+)V(7@*C>7uzh~WG#nn>Yl@2=V~*K#=rO}ER+8C_%D7DR`w=qHiVV)9IPA{tS}l@`cqg3xBMQjkQZUC+GJe?VbLo}y2qx^'
        b'<fdqrdLipxMs(83O%kVH8=IIz1APMmHS+2YY%%iW@_-N-GyvRd!-R0XBm!a@=?)6J=RftTz$Bb{Ux@tEChMOz0cU|&^c3mPm_?gx'
        b'2kD?|Y*;Dul}*O5tO&0DKTQ1xteUVk7BP_r(ocsqGdt0dLZ%CA7rdZN)*u?5Y}1sWm=08wSh~q9K}I$)G2ViywL#KvlhqIQarUNX'
        b'GR1e3-y<Wh;VEYxs0<2$_FYY|t7hoUJV?0|xls^$BTp_7=nXVKro`Q+f<mC(R}=XG6L^c{Rk~mfFpkJ8d8VfYbE>A!xey3F4~#&F'
        b'!ZB!gfS}Q}c%3V{GPD|Hg1WvuKt+(Q$E}=)ll91-i>*Hw!#@53RRz2z2yy=-AQ(48A#J1DSY8=nnO{@l(PAt?hAL0_8PO}T!did9'
        b'viJkETi`j#LY}mM%lwq0-|Rzx+U9^CZ~#4ZhvhD_&a-MV?sPn=k}wh%;v$ckq34S==ZobF1!<Xrv@l$K$Af+_f=!%(7;$gF+j2yA'
        b'@s$kWwybQ<Ag8~l*wIr=_7>a7<-~cYyr2j85hYp%BYPGzw30R^_b0S_9wH?v@>sF;SaC0tI1YhnCD`jG6YHyLv?>tU+e#cRwsrX#'
        b'c~?#Xp6f6|x_R4O^U&MtCp1oq?1%y;<q1lwXk&`*^DLc|RtbLn#FKtawX52g(g8{f{)yJ|q!%e&dwxr?zDiKi;GS<Pt_z2<#t09I'
        b'!j5y{2PdB_&NB+~H|6EIOj?d_*dozd5477!LE>5JDb86)JJF;2#E#;68n;G(o9<+j3%f&&f~pG?Xm}6BxlCoApg8ot{KzTFwLx$B'
        b'mWmsqzz}x-#}yX`aH7b@iVO`cEB52T*;~U17ArLjm4-#cK*kpr6dM)KCWHdMlN$vytR=-}2~*&}M<P%I$?i!tChhPBKc2nsL%v&V'
        b'eYY6!d|L4o&o3n2DyGFk14{d4+>Ag!bjtC=Wco@0?IP~gVjl8IA8}H@t{a1KoqwZr*W@lKGOg+<k1i>;E}?le4mPAbNSR{g(LjQ%'
        b'WZrvC0Zf=cf4{&mNuY;Y=7(@+zm|fcLAo9MmNrtHCsgJ(%C$F`xs&2Nq7Wsp#U}ZXe7V^AGVH@2il523KNQn)?%_r#l4QkGIx_fw'
        b'>B!p~UyyUY#a3Sk%kMc@elA!)(y(Su!O~s&UwUom1z3F&VU#4)n=bD!Lw7i_>CNeMEKtv)saT-ow!A=hZkB{678Ezr!4*iXI8gB$'
        b'#?MmTCNPMEm{*Lq8lc|-*IIZG7dFvFx8%J%4B9LaB*COxG0J!{G|Lm(E(VE0UrGC#=?YN(*v3iy2~z4M3f%)ay?*`lj9s5WC^zcs'
        b'ZWh4^-ZgrI4B6}5oUMCIjMBateQI9%z_s>t>@~DXj;P1n@_#InkW3?2#N&&Hi-3rRrs&78B_r2*rKrKX8M1y<jp4LsAKaKZ6f4O8'
        b'cM-i3V2>5%ofJg7{C}u0<9S)HyrVh4F)bD*CBP(G$U@zz=#v7>(^bxvyD+M;{%g-Z7_6N3Ds@aClM)jbCO-4BBc{dl<+Y*FVK7CJ'
        b'gAm${PuHI{9~Gp<3TW_jSVO3H9=hgOu%?2k-sgeLj7DO~(8ER1;+Wv1C^P086ouv;$9q{rT;fO(9ke+8GDRLJ!rZa2wH@n2|6bI~'
        b'&Gu+!M)>ClBgNl@wlLN+B4Z?hh}wyTepF=kM|#eDoj<aXaXSBVA89e8g{kmIj7jqLVttr!+dgbgcoYK$4a~cMANoR1d_*q*pTQNN'
        b'k)1{19n)kn%d^(j|6O8YC`=5^UyGE3)Y4;UoD9kGSdDSoIQYIw0R9pq#!v(pgGDTc-Ob-pbUI(l)p7&fXRNJ9InhX<1nqtmk(gkF'
        b'=JcS2y3=^ACy;Zl^&-RCg>5XShD$7fl~3o}#2ooGxbu(krB{JegK>S3(C;^9xx)}Di@ETS#6Kxw4ZW7CDUwGSy3bHq{_&yj7Nz?m'
        b'Y7S#0jiFwKNDcyi8OdarGZ4^cNZL~*=(nAW0bMuk(_<pocMdka;~4R_i?*OGc)t{L4-A_V<l&7;Fpt2cp8cvKhpLEF71_v>#B%6y'
        b'$^GGJ!jW$%7gQ6V<}x7wZ2AO1UHTMiybEfal|nE{m7Q9^iTj63X55R-!PuAxr!OI?zhrB|XjbNk9<aoJD56gn5jQqKPUh&k+r1lj'
        b'S3VP7sT6j!Mi~#a3a`L-54Y9Oc3yO}XIi5mnpQdW*)R(9ydqbW;7c1O*VCaaAAjn<vhkI4qet2IUQ5=@gzd(2L`PULLb_cR(F5zr'
        b'IBhJWdjkrZiZV`4AeVt3TC-99Y^_crLqdPZmrq%3pZ_0i_M`(jMq5M$5=8Aq0m`W)%xw2~N#=V9=J5eHv9j`BEMqYjSZ8v1k^0UP'
        b'MK@JonjRkB9eS&<z#kc`cHA$-VA$(>h4do10{D|>9(8gv2T_}Zm3AKQWw)^`-%yMB>ePqPNAS#FDUK@!`_$%FbdmZ9=U!!Y(xpO3'
        b'XSS$;Ek0LBZ;TVQG@aSllK(HA+n9;Znb#3XFK<koq&buLSD}mI6&wC9n-bu_!83QlM-gA)9jip+<|6sWAsWeC5u2NIxR92p8)>R@'
        b'uj~|RQJH&G;}!UjF%VyeAmO)F(>Uk~fXeEN72;C^P9r1Z>5fEC4gma&h$-6uRPba{1hJpSj!mqhvEw{9HX0;<Um+%19S&cI#JuiR'
        b'GB9pl77j7p%`7l6@U=UiaKt+bjlfT39+1%y*DTaH=N4y(+Y8LA90p*woe(_C8fl;)^ym7np=}4H!03*7VJ!X9ozeQD2#LDkB|wGl'
        b'MM$<%DM0`$+>1l?S{(DfCuLwfeF@H83lIE~$%WSB!d@1U0vpiXH|>`LyGwn>&6uuL$qH&1z%UIKN|z$UnnD?G(COF!cm!?=u7~A`'
        b'cMDs12EZq|JYbWbKrb?Sxt&amZ@Epuf0^G=y&U*M`V|Gk#(*F7l=#nuS5^vBCCR8}X`#-BO9gA|-8FwM%s;mQ(v_3vq9_Nly%f>B'
        b'T4*z&X%d0PV*@aC(_C|cJ@N)6PAohvw4n$#J?bQwPYY-jHfiSrg1F+6XpnoAi_=XEl?ic4ftw>@#dDNqTmDLovv0A7IK3?0;}l5g'
        b'$Vp1Gr3UJSIi^9>?yP&S{W(bt*~%<MM0_UZ4o}<%Gc2cljqG-YjA!)jWj#Ne4FKJXfUW!b7LM$p_YR+%vwrc|ylVHrpmu1%T4!wx'
        b'H27e~poj>Y83|OpbWbV3mIJ$CzS}(sY87pOf!1v%eW2<$t6{@2)h|}Jje+UcCC-O_Jj@MmuLNoyyJ&4)U+w;FP=wg}a6@4IH^8et'
        b'R{tf|Zhf?&+P%}t*eG${#dvu8PGENWd0W2#h4%+V@FdRL1`?^dMfu4<+tuznCC*!hPms9ll;5az#l~uPLr}yUeht>^8>)e#8KQzB'
        b'0{yaGUsac=*WIdZD6n?@v;aMj)cq}Gy|zK(9Ig6+@;hz)sQ{+^i?WWa2R*Ior7$;myk>p`wjI|08bFg_%d?zlcQ=L2y9fTCqUL+g'
        b'cLSMmz}yDNedjl=lZT(EtonkQpZq$^;CxP5$MZq6-6yE|*{)_e$0;jOU~pc-rs+@YtU5eN<6wgs+2f7}MFP7zu)zDCVV>bBdE+5@'
        b'd4Rmc7waMC7-;emM>pI{|Ah$N5ci0}4ig79gu7o23iH5r0vd(8pC`;4g2MWUwhdKd6n2()V|}>0lW5%#uJ|0}2ilGi+3O|FUoa+K'
        b'xs!8)Li`@U?u(J2h)BN-VlM!;D=19p_ZlV(ci;9pFDUGNK<V!9DZff$_l9tqya0`G(6!4H(O4jHj>O%h=0{Y!uLz3poj+?n51tzR'
        b'mh$5Toj^GQ)S`GyDK}JB{fnCa=IcCIzn3D8<-_`CsQDQX6i7Qw5m5ltB`{i;OkT6IyNmKOVg~r$5Twy)P{eG%M&jjyJ+^sRBT-SX'
        b'$KBtrbdUR-K!q<cuON<%%ugY-Aa#0B<c#@|L|{QsBuW$(K$^|ZA@V@Z9r!lqbFel}!dmwNEX5?Owa;KJpkbv?!Fu;OSn~^m4h#C<'
        b'DR8_~K)zGp=SwVs{tnTy9{i2@OM#9)$MR?$G*FTYLf%xd5%q_3poTHH0F%wHfOmMlrc9sGZVk5$9r+DrX!+~;^qJ)EDBS~7vpmnW'
        b'|HBFKSAEG)DG{O$HUMPG@VaOFFD_jERN#2Efc#T|-#3JW#-)nJC8B^f%Pzq3#480MMg<RX3j=Ca5s#=VVcd`FE{xs=7-iaB&8E4U'
        b'WrN(CFgF>XMaKyFmNHprj5)-{NlfhPrhJL{<v}NB^v^1A%qbve6%YuGMJ6nkBr2eF+_81Eo|OIsfyVO}^XUcae*s^NHoBp4C}Yx*'
        b't8kag%OqB<cPXz=*FD{9B@$tpm|Z}>nn2P-W)>)!;=$M$v>@ISo~gMH3>l?~kvT#sUlS9t>s|W!!*x?{DjzeTRWCzNg0lc27SZs2'
        b'&7brjcF?r?C7(RB5w0M4LM1Pg>%$nX^|bnIxhsVn%?By+NZQh;6BROf-4D=bk7PhsfKeMJc=l2EUH<b0U3t&yUCjS|%0JfEhE2jI'
        b'JSKavX5FMW@tmv%y5pX~<DS2O+>vkHkq<QH2l@1>2L}|Q-@i5HU)d#WGB)tYx_n)`zDBUW!JRbbTj#ESVI$JDNm!E)mx$h3H??JU'
        b'Gwh!7C^ipXznlPWnz$u@h`CMDE`c_eYfTea%_Gz?Wi93lj{<x*5lZIwL7%f-L6<SZGW6L52O|A}8j!G@60{v{cJJ$FN$*lEgqr_y'
        b'gnK%Q$fJt_MQGJgM0M)PV$QK8s3{5>grYa!RG=8fjU-j*bR&s*e9YDFtV}Gd%qzv!UaDoqSWQU_+P#EfRMl7wsH~>0r`u@Nzp_*G'
        b'CZZ5eQ)eU+U65?~rTKtkxP&MCsN0;6K|fUyEH_R1YVrsr_Zr&Wgfw0yRzRE^u7)P$6EANB4hB3#5iGan=j-XIVa}1eQe3;kPd}||'
        b';25{Wz=eyL$<15WhxOh37wf$M#+sb}`;_SQPhkUmcG5G4OZ@O2JO!AP-*7dOukH@4NAc10(*=!JzwRH_V8pg{^x`Ne_iwt~lKkyO'
        b'@Cm>&=<{-oBy@H|;qTD?^Y7`ig?%RlY45>Ca$st9C~#%r2V7{%<|0RhN#XgribS>G&?;Cc1*Ru+vB0$FKXvERRtcWVje9Zo*i^0!'
        b'4W?5LrLp?5gng?7X_<7(+=i>C`$ruId{w7pS5^tN^{J__dA4;{eqP?Lyb|G|ECH}dVNv$>mGCt|SH2&2DzyL&p;HV8|B;u+GL;DR'
        b'&uY*ac022kPUt-Ny}etI*8?-YX3Og6EW-F6p2s>=!g#KZ@)RzTykxX$?r+eCIpvLpD_2-)jb_tk23_UqXB%oijHwN?U-?mx_cLJ7'
        b'yGWz(N~{oMUT4c2@nx;hFy|A2a4^WhJfZ}Sg^ZYeTV;A;Boe~}*i8BRm5X_C@i1;G&4R>-8^~|-^ezEFvjEMP0@C*0Q|@#nl09%4'
        b'H!=x|lq8c&zPLWf?!4dCexaT{@AoPD*FA+D%3If+359Y5TT{3JbSBLO8IXzYPB1_28w$?NUTOdpIo<h<SDl*ammI{c_og`R)%WNb'
        b'Gq0!*FdW=+X?8JOix~bE+YTat!}Yl|iD6Q<m^9}-<2Jy0rYwPe6(dpojD5VG@|qX@`IOgOpHF#hGWXbvxm8oSr~7Hnv)g}wZ`Q9P'
        b'9q;F@du0DokmlkAS5p@quq+(KWZ|Lp!v2c9zH@@KAz0#)E0u<oj=G?yrLpW;LK9%)=TXoo*IBuFQ%Ppjn{L>Y#){5j9C})oE8>4g'
        b'XK3DmjztROt7HaXJ0Qsu!<@+lU;w~>6^buwl&><x*Qc#A1II6MRZL=-{dSn}_9_P8I{6>zy$pKMiJPR#lgBauZ@CtpBDrzz!gB^_'
        b'Fwvbx0rxwS=zfP%k!T9h{T4O3FC1;Zo7i_3L+>pM5Au5j6Uoz|j~cXl9wE=$-b61OyOxZ308p*|kGC6y+ZyeS!mon4M0noseaUD0'
        b'uh%#J-}|q?ei(<ih&tGzvOJ({;X1K37b@GqsVa5;c|gbD^s}4WYGk}-NWlh_wh1Pe!BN6Dug;N6uRX*(Tm6h7KF)o*`bp!{@1Eyy'
        b'&m-OQ7QIIdLH!BW4kc)}1Ucr9#);uOpHW5)mIs#{v-E~QxZL{xXnXg7rmn1U^qi9?;iyS~@N}9S3<jz#1S^5o8ImFb)fu1~0c8xq'
        b'KnUQ2vGws`e>tH83F3T!Z3U_`C$TAk$_Qu`A9P4mYAMW!?evM?Fm}?`M_Wp(^?mN%=LEGgzk7f8{&D|F&e>=0wI6HmwbxpEueD?m'
        b'{3PKfuzQgya6YFI43A-lkj?xynTCJf0S2Yy4;FaSJK10ox9o;3DfnIU1MI?^D%qttWE*s)LQ)CgECI|_(*g2@hb<&);B)<5I3R(0'
        b'Y&VFS8?hUwbdt1;ye~JxfWNCWJRNA$VQ$hF8=*E=O-cgmjYF2g@>#rsP!;$5Qb`dLAXvu)Xv-5+=CZ;lm*m0xD?~k<rZeO!rgko?'
        b'pCI$$8~-j171_5L|K7L=kJv9tZ>zfzi|!U#9dfI6i@uF}gUFm}l{kGH6Wgs!)Kse{sMU!b>|o6PLmhbzt$#9#JOx{rpz=sR(VolO'
        b'4ju1s4M*kO2Tac)`$cTPoYsf3FD}5tss-sLSXZ$Cta*V6%lsXKp3O+X%95^)`DgF1K8j^-K=Rxh&l@F{RUY0{jl`5ixBO{iS_2b}'
        b'wT&l>7n1unCT_J_%;boL9U49v1E2C<-3Yh77d(PNY>eaYM?IiQ_hD2e*p^`j%m>3{J%&W3BT8ptKpX$q`2<O~8V{aKmZWJmt*P6|'
        b'YpLA`(aTBPiUJI8Vlm8VoyW@~H>%&epYnE;=~LR9yD<i8r+x#~mt8!4_l?@=;b#yeDXTK29o-+?O)$!FxKM@85DTNSNnFRH9?{td'
        b'o11@xFD$F5uz<mq$dkp*dl)SbOjV)cr_hJ_w=JTWFrG}zyLjP#An$K#g`xNgg!1iZ%bJZ3n=35f?uWUy33FTb7z!n=Z_&+L#kpJI'
        b'$L+#xp~aj{`FnQqn6g>x0Z9{YMQ4hp$JVW2PUwXBJ@h6(mI!hB%xUii3v-vSho2%1BHyV9#APB+!YBScR=>^Ka%z#?*p1jtH;C#f'
        b'cqXBJl3DH<>Ul7W>;PBs_{Q@Z&|fQAXqlPcZ$U72E-uXy+ElRPt@C1_KTyIMI6GM%L;gC@0#1{Q{A0xfJv;e&1-rJ02Wu-SVj~0f'
        b'Rrp0K+emPcYc5g-5!O$w2e=Dm4p%~$-#Hr>in@fO-5|fcA|Pjh0zI5)Xl6pzF*QjaoGmFh8&#N<kg#W3U~VtHc3~Xb=*2cVv5oyy'
        b'CixB{P#_R??z5#`=ok#yFo=@RLqIu1dh(F|hkF6p=H>>wa8v~;W}C2?;-z%(np>96kNn22dQhK{KnA&nlBGR-cL$0K%c8JhITF1J'
        b'kF*ZRT_g8%kJnLcdz#mX8(yu3aV++tozDmL@J+9xdrNtvMNn}R7j=`6B7#fP_&KXhT;`FCf4;%{`3C32hJNY}*~-WmcJM_nyf@z%'
        b')=)Z<n8t;1r;~>O>r$|XarmCzy9EG!g^P#f7A1m>i+`Ce77l+EXd`o8^8>v?v>RRu>ucEHqHuC}0~5bkc7=<N4syw7E11_dVc%ai'
        b'$mJPRF0{8@-1kid)ee{{E^<HuUcvMD;SKG=bF==r#j+otaNts0l<umds4b&uL$11mMeQmF69fbq2<oMHoyiwHLh7x=uNry1eM{$`'
        b'{M(A4w)pz*X~Z$FU6sko?sybDO7C`(2R1yADIcW$X(r8!WVh%JAcfBDed*7Om%WM&e~I8cJk+qXE}xo8Pv5edgXv$^<U5hv=fzD+'
        b'Wgn%y=1Q@*$g&W-QzlI5ES)QR1JyQd*xa-sJ=41E*lg{t4V!nd&)Dz>h>p6ytWJo}8|C5u0-JUjhGlAz+JE8Kmq{aPKaAnQzccs?'
        b'%cPRpBl*<aWzwMhLv*DMKbF3_t}hvkr;x0HZSBgFeI|9jxS{qA`9Cm3W%^Z4`U)<zbLc^{wKddz@-j?L-MqDqkAJnPPVU&edEEwl'
        b'd7D7r6%@zAGIJ38mF$wN&Ez$+%ZX5Lh#ln4AXf=KpzRU(KLRM6NZUkZOr1crt2TJh^lmYbOS;e%s87M|R|snF^>E!EK?gWqnJ2^*'
        b'ir`rdjWB+hClu%E)5JXj<wn#_HoSq=KZn>$8oIIiY$SSX*}H!#<E?gPZ6KUH@(^sGCy%@kSZuh7f0lMdBHM!AZ7i7Vlu(|ePAOLZ'
        b'3nWXs3846unm8VB)8?gHUw!ACc3^W)&_!PRxaqHS+qi7xwmrz2w-hv;=l&QpeRJXl{YWt2PG1XDaU51bI8h+5+8JPNN>Aj3Xng(#'
        b'@B9tU7%=}k$qR7L91u01M0*F4j!9cQMf%(K+u}11!-yRK@L75%7?a#h8B=>vr+C9Qlwz!$x1&1)W0L!Kd5^$!mX>|?y<L#`IUSwh'
        b'Dat%WBVe@ahv4ytzZlgi_{$Qo;ZwA$gkLNeK0)^g+-p%VKnYm=F?yI;>)GV+Pjtf<7(W?_X(S6^7i3XC#5Cc-<QDj1Z>dOgM43bF'
        b'&Wa*Og50ph-Z%B4#2AG*axRKoe?}=rrm6jEQ<>OUj2HoKmVx)aZ>v8IHLgU)xVh98cM;dFbzZBUG)pYqxUA+C&~bRCRp#sj_0B`^'
        b'1w&iqH7k+YpA6-RKoYAEy><aev$<!Xbq@It$W^KGdU)BGDl{uEK2$kEA1f7rasCv3agJA$8rV>yB0?6&v*$VZIL2?FYbaq&5h8mN'
        b'@hO4_`JffbeD2=TSzrx@F>COBSQvDNdJ%P=sWx-jepGPlKctb`iJ`4x(4gKjIe&r%H7$i0&Abe0edZ?SJ}o}0f?+?#W-<PAPS4oN'
        b'$fUE?1mcQCD2kVOm6N!Hn-Ue;*H<m~$^B0-fmW$lHr#BItD4y@L}pg&@+NH10ETDVqM_r-Q+C(mC^S?(Q0+ZX?fgS^ziT(S6waD+'
        b'Qas3B)VXhitb*?-B!9u|VHh4|kHCYh9d*stEo~T>*eO@gQ$kM=9!xoxj)_b<F31zqT7cMv)@I&hm!zeky1U)#Tw41z;7_b}(gUwF'
        b'JAy!q{#DMlNWkuPnIF=Q=uAJoUnDc%>Jes6GF#r?=)m1i_teb2PI5;zku{?~v%+pEUaSu2yUs(HNn4;UD2qeB0Q)+=xf+i+H>-6a'
        b'Iy5r$ZW`ES((l@uUmr>zby?eo(l6T*n<P^|oSnKUPj|Qy|0tP!_H3eE((xzj%kres>Y>wT@z9@AQJniVr?KhE<;IuKh3F`B?=L~h'
        b'h`sUU%N$2Y*R11n$=?RX_YiD>ilYf(@Z`TvleyIlkHP5b$X~#0q`sQD-Bk@)2lGymhfn6il&vR%U2zDEwfh?;!!m%n1iMG*K*>)b'
        b'N?NqlgMx$#kbN2aUXoso&q^qRG7>-Om(^pl5|SC!W70F#gY0u5Cn>EuA=$$rM_~D+6bLZZgW(u?7ADwHe3nPZ+@tVSvid~8J7Y^Q'
        b'Jk<MS^+gVT$K@3(m+*VI<N*9m64m%KjkYe<s5Q#`A4y?M(%kCr!>eJM^RenwG=Yx!!$pqoP3Q=m%z?ub7ZpApRqc(cc1BhAQ@<m-'
        b'An&t;n|X;wo+HXaeq?cLb7D7$2vS<j+@|4_CE)lhHq4aiD!p6u;I3I9pYV}<a|4kBzkW2I{3=Jjkn5si+`Hjii5czp<&pn{3_{F^'
        b'X&2pOQ{1Y;BN(xawMS!jA52Y^4q|v!4>y`1{|>XKw0=8t=ZE~J3Xg;gT^6f1h9igb%0lGToH8j4So|d{(EkR4Cy;-JkE2C#p+s=T'
        b'5*`#7Cj%d0yr<48#sKuLdxD0Sk5`EJ-_dOB5yi(<xJZSO7poYXP+n4MIbfEdq4Mb{QeVXckXFr)l8pbg%KO)<ek$Af*D7))BOpbQ'
        b'<BUpqqzcDUTjELbuT_i$=km(QQTPZS-e(@(Os5XJyxywuZ_B6yHgb6tdx>DhAO`cCp2_TE)!wG>Y4Rj|q|)Rt`S{HD0Y+2QTjf1e'
        b'1>lW;&Hzhgfq_w60rT|EWIn_`h)FG+6@#dYqBNVyZkRg110ScVyd9uFFYw=|ksg$EGxc5J*eJ?+!e#BYC7zbcFUUy+n;!DO{+>cu'
        b'zK=?f!!y+XhR-(N^`n}(@Wcp^FL_&CvwX|wh1QYlM^lBak?$x~ovdb#Vx+PqqKdijgD{#)q~&xaaR};?+JdaMM9P)e+?wbes#N?Q'
        b'=K2Je+vT;>*8arvtRW8W{h$(RBysC5c^@BUao|u79Som>Ne)ao2SuLu;Lj()lrQo8C@lG2FmsWonMkDGdc;Df_Ueqy4C$<Fsi<NS'
        b'e<o?gbUe7PT3Xezy!>Z3ycO%JT3#+=%$H`=4XiEG`LY??CZz$!duhq7!mp6Osj5FmKe|pLm1}4p71@J5vx^L8*#6~J&)jB|C^7pU'
        b'*ePXI{mdxkF42Rny-Ehd{0d!F%&kEEY<=V}tA5sQ!i>0|2Xq~jxkKKE6h@KqA7zrO_|s6&gP%~Yy01`Ic@wMfx%lIN)+Vu&k&I#{'
        b'`GTq*ARS+zP{30#?Zuajao`CQt0f2jae;rygL9tVtDN3Ju2Wv+-wozXgmO7eUFA?c+?b|k{)_w!HYldiolUc}JEF=fscIA2Bia>?'
        b'Br>cDp9Np==v~fs7+Qdw1;Orek~b=u%6*;Z@nG=!V<nr+4}AU}zJvLEE%48+V*jsJ&YXk&6H(rxlaMMk2a(mGTDnqAA^GzV?VZY0'
        b'b?&ousRW*!txJ_^bWO>gnn?~q-hxGC-MpmlDqY@;EU^3NN+jwMY0|Yy_613mkmoCz)s{hiJ@fFlKnq3!|Ca*)?=f7X5f`yKdS+oI'
        b'{ZA#>v;WEJVDwQu#u@~Ot1J+9dngt`s&<so*MC^){d48`=O*fH7v;8*no5?QEP)mz<e^G7$h$Z2e-QrrFVk81GQe%uOmdOs(V!il'
        b'TiDO8K(-Tse<xGrU*PXVf=Y@P#Yy?NC5}Mx9P%VgbuS9oCMyOilLjhN`a{|KoQk8BjRZsEZ932`HnC0GPzbmdNJo7)>si}Zwm+u7'
        b'Bc=w#O`wXdN&-WgrcGBPnsUe^uvyMIWhNg2m@WS^sQ(aWpJ?1!>2+52JLOJiCHW)6mQa;00+H=Nhy?zq)cqOP@4=cr8-KmhyBFm9'
        b'C7%f%Zi?kN+bYTZ%m_TiQ9i*@yjq#`TBS^cj=xgr-3@YP)?c9m?Yo=O|06*mrZ!qlq5kh7X(F`D-6d2gmv1>m;8;AW_)TRG8ZRMN'
        b'2GCg*_<x>RVAe_-g|Z{y{wRu1(}-d-BwK0*PAkS-k4A+qYQ5FEg(Vy|wh9boKY?`lOggy<0v-OJz+SarIh57N|7C*ufvcR{Vy@O)'
        b'38Tio43_$-)6mN1&B(GMURf9hY6km=J96}eG7AqjgLUHfMr7HJFtQXvT^)rRGOVDx@m%J+`&}CBXiP8Iy;*-G7$g)jvw{6(G@UXL'
        b'^iBJxNb<Q#?PiO$TTE7&@-~47d3ug@*;DWui1t%U-lrD!wO)Z}b(Pk}p@v0JFw=f$$>|0^okuqIEvW>I=j(t3`a3|Yf2U2Wgcsy3'
        b'>}m0mO7{Pr<w1k8Q9L7Cf^)OA+N4UgR<0|-#C>q9mW6QrivfuOh)K<h-|Y87W)`fk1PG%n6wCY@T|WxO!@nm|`-{qDjTm5m>!F<%'
        b'JYwDxS!Veof0Fh;iOj@sB5zr2LPY-w9I`=<TaGxRE8TyH4EPILjLg{PCk0jF{B0aOOnz)=1;2Oc9wx-5{|>F41G-|`6*)g#=-~|V'
        b'%R7SRPPt;yL7uFL_TQp`Anb@_bg7^&M)4Z(zs{-jQ9S5%;N$fm5j?o9GiUdG_bkqP7Iruu+=;$pkzeNcUyc+QdCprF)60?J;Nhml'
        b'Ul%#w80@@ZX}E-eU%xFf#VB-Mw}>Tjr7dz9c>V!Co5;x3ApiFkzcrGf*BUALt)<qNNQjfZu{7EmlGB{mEMQsqUxG+_DbjhxqI?N5'
        b'WF8FsCw*mshVMIJf{Q@?wUIp>Wi9iW0RMq@EB;|&G>-+?3Ql6I+(@DDB5=Jk*Dfy0!iJ-f8wFu;5lL~XUq>gGoxbG!!s6e`lttnO'
        b'*2JANl-a*jd}Psn#3(~C=ilLf7PlTjoFf*~3!q)#$9c};-V)iv^>2xE4qN=ci_E+R*4<f)_H3Zk8MYKOy+@or3lqZyBtp}8L~+{U'
        b'Jk1;u5QuUU1h^@Z9I`O>&|jH(&UY;S4Ux`43y>V4uerWc79VARINAVl<UDSX>*Ve#(05aHr1O|XoG15JM%H)@&OQsyS5`(^+^z(q'
        b'Uxdikpe9SC^N__~5ovkD69xX9Jr-p}<a1?ZM?cL!E7qM6Z+-O~`Dch>*$KY>G>;%c<MOfLaK!mXi@c9xDvNaPxA;w<E;o4mlf`6;'
        b'1Yi8?BjM5p&-*O$evZEs^g+2k(%E5=ALc0Go2fL?xz{2;!ciLGn=uml^ehVz0{CS{Z1}4g+0RCVF4)oX-<F27pq4*aCOwkw_O_t*'
        b'*p?<sd-AA;++}e*tCGf-GIIswEh|WX=Hz&UBZU0D1s6GDL1I_(mv%`@on=xbNoZFE#mB})$m6!f&z&kW3qei}AC7t1wlPv?VQy&F'
        b'L;rz_ZI-T(_-BV9%~rf<iGLQ_r<EXfDIViM?YcqKA+f6g&2%W@lgN#h8UBLhrIIQwy--;Uws9akCO$6*`#{d52%(nNMJEG^r|w(X'
        b'Jj9(B$;v&&(30*(>|(__3wx<E8lthK$kJOU>9FI$c;kzWk7Wrb)}K$7oPZW}X{kL}A!i|%6t8FMjXwFD9dJ4LdR9L)e4C{i58!48'
        b';PM!_ng3_Fw@V*|d!zK{aBsvusa<3VSQSmdkK~h<-egH*G9F~3gfH3wh3RZX+d0oc^P;axXYQ@w{Mx&KJ>!!J3_<0S@$i2qKPlFt'
        b';*g)0GLp*fU|B!jCjA=QdlI^nJl4+p>I62t2-#+An(wLU+Ulv<F4`Pn@#wa8K!-j*!Y<+AncvbL_2!B7H;GL<#G4MuW!(Z7HYeP&'
        b'e)7N&9@?3VuHZKh42{jXC`dm!<UrdMmnG9B9C8k$<3QUKUrTN#y_v8$?N@l@Ps!+he&g01+f%XaQihvEU^6wk9=<A{ykEg^lz;~V'
        b'?Y{+IhW|m|{v{sqRWiDpzhnE3ZJFQG+K$q^_R?&uP+I>z-Sn>Wn~J_`6=QsIs)FtJH_R!+DSC|GGkY*7b4EAr79oBf0_}rY+N<za'
        b'xSX6%uxsCVyGr}MsBnH!aiIi}Ps=Y+GIC2PBUcA|unCLHiPpo&FwThzcMziQz8~;4M}Att`d47hJzyRFtM?TjR%kH0G%;-mm!_m)'
        b'pg!x#A^GD&<PHduIxs|zRp60e%<!OIV#s9%WUZo^7$VH5>DN&+`;20^0*uTsI~suhJ`;Gt@yAKuBhN!KCmV2Y`b&j&u)_OJMc-d4'
        b'zTx1ro;eZE^`D3SSw-Bu{tCe1^H?3HheHl9M>3*=-F9ByOJ$4<;^E{5Yyz1pOp&#3=LYUHMf%6?<D69PjJ{}jsVo*DJrxctTN+3k'
        b'klHak28m8b_Bm^BGv}`{&E1LTUzeO{mv@UN+a-*vk(j`tv7(?<{;;yPZ3^AY`!*a3Rq<vh#n}TossFA>l?HSOctp%CPrw*9B_7@y'
        b'u~|Y$QK|ZL40A9CX?RG>%N5YIMA`a)$O9$WzW7qumjoH~hA_Xhcg8r=W|3un$F4gM)(W7^7;r@P)l>v7KSjb?XX*@M>tuZKhX!Cm'
        b'13PJH;-fHsVqq#J$PgisCs+vrox!bt&V#fEe1&^<APw{)kpN%dVHJ#-i2*UH1fPvB#Mkx%*?X3mnQ^dHka@JDEjbm=Bc-6b3xWc@'
        b'MO!fr^QpO+D{q%jcJadxT;_xGrV)G-|LhwJETzJE+w?FyHUr1dj{Zm9g%uAovPp`iW>}|PEN@4DmRIqTnX&dsV{oXDSFpCVkAXRE'
        b'7eXU+nF@J$XVFFo05t{cW`2a242Kgnv0I$jJ%oo)v2`<ZP+Ac`qla37DdvDBhhw9hxl^o<ANL(v)`56_M~YzaZbDPXzsa0qL*Mq0'
        b'RKI0}XMI>j7I&1(xNqc|Zql*@u4l_2O5SG_=vW)tVRv9{61x=qOWPE7qS^jC2ho;fSAzs~o7S!a|GKt3dp`KjZ!57I!M`!<<;*Kg'
        b'UGjc8<mYbEgaUiun^HZXBhMJAlS9V_#N&Rm*Kc<E%?qN*Q;@?azkoG&)v)tk@tIkLje??JK=dk<<ug4sO*{I1q2y;Ur^?38vl2wS'
        b'S?*te40TH==a4uG@h?QgNpk8l`F_qq4jx*2^W#OSICod_Lhi?}tU9lgB)}^HcNQfs(hh<7mNX;|L2$ent;Rpzx3s(!8%{>X-!*$r'
        b'oBOHl^%B6ynWY0di@Wo6@qp1obiN)`s4K{K5SCSi`Oz7KPYlBW7I5NtXfzR>p*}4h_R|CLalz*3FTd)SjQ5(oy#P|V^DQ%JgWa6m'
        b'B{=~-VSj(n{M^9##gf}6EeCE!!|2QITTwTI2OhsAI-YPdXdv=d+U=9yyUfRP`dsG5|2|%16H4&l<CbF)vg11}a7V@YX-`$uRnLwd'
        b'ZGBJ7KTo%oW4?0Eg>vL_xbianb@(TOb17}}VMxuS2J;xt&RHTn7%|>r_BMeAy)^t8jr5tzhYrd?A=4+cZ$4)tAv)PNI&c1-FURd>'
        b'Zym_hm^n^+Y6rRRrI5deV_q#fmm+JtmwrZ``?j3CTmnt;hVSCsVFBW)d+vEzBhr65f~<jACql^zbAhlzSXd8-W#0T(Cgx7rIfWd@'
        b'o|&_67>`D-uY)!>FNhNLb^0(-I{1A%Xjv>2t2P&!3k3Qwe%~+47vzvT%bEIR7XBcHkCG#>ZpB)2>f-E7qKubc#!oyl1QiDP%q)7b'
        b'uwHh8+dmvi{)Q2r^=9V2$^<N>0RmlWeT85lkNmiVS$XECmc5Ckycus^3jWJu6$QV~{3i{V60n{A0M`oK;Rq);^A3A<KRiv>PQ$ZP'
        b'c%F-maa>O9R6qGEbIY&HUkfh=;lhSL@?1{da1hk`bv~|~jz_1ut(|Yh4A~`(yFIGOMoBlE0?x<H&)FNhP2VvGG0}E_Mut6P=Km9B'
        b'a)DWHA5z4dt#t|&7EL6m0=`LhqVcO0v1T(iR3<SfhQv~2KiVfZgB?GJd>Qtr?=dqu*SufUYaaq-qqEMRk=$7zpQnXXmdUROH!nd|'
        b'm~Zr^O1kSnJVy~~jt_A(w3Z9VEfB!C#EdsF%9SR#Z`&K%wt}S;Tsyk#X_=)$wYn#$qP(Ddbw_^NYOs6D=PBk+6-YhU)2pb1;-OXI'
        b'F2J31x+UYN*^7c%WOSlt@-$?o8cs%jLVTPMJbtg-d#AjgT3>&YUJZ8U-<3hvi6?gv{IBQ%Q9+bF!JLK%Ip$ZS92XRZ7hS!_spjnt'
        b'ZeP~6Y*}hh3=fYifBX6R*~ll4ee5YZH|MK^SMkWNdH_#>%ii^%IN#7NZf@Rk?bcU4i{AAl^$rg8zCC2E8af{JsVIh5uEa9W(*^S#'
        b'SRql6QXwr=I|LQsU?IznPrF9MneWlayDIVd4MV$UwJqC4N4K{xgHBFB`EPK*r9$56Z{>K@AVz)&r(~y8GCo@F9WC#7ZgGy5lMdKV'
        b'#Ynk}g029`_t`wN#@{XXo(6edg!g?B#hLO!v<Hnx$us2-X@5V(C@nZFj|S-cJLN6!l;b(=LQ-DdGFaYfM##AkJ><#qE+JsOM9QBY'
        b'oMRDX0l6CNr*o0sA~}^H?|oXX?JL(`M@YP+1ut=MTi2ruG4{(4b7%p#{AvHO*Ra)T|1hkQ%a-1Ehaq2w-sBoKpoTRl^^tb!hW7m5'
        b'<x@B0Q~QT{_1eiVwYY5W5@-@Nd3MM!I`m}>Pk-&U?D*~Dp?z)TU0hGJJ@}(;UPl{{dK*$<zLAlU;nz-~jW#@Nz6Qm43xzFL4CG})'
        b'cXHZO4sLsBrVwclelI#<BOdzGVoXONX}>%lH<Y#r51qdl#ksl3L+Qyw@JgP47BYOEMw-n-_}p?0c7Z~MiiXaw8u~Jfr@wwnHhilh'
        b'xG=h-6_kUgYa_`EgVGi;VlU(8uBIGH6Puaiyy|jWEYcba_voep<u^1rY-l-aaB$i~fIML-XU;Q8X_-c9echJ$WKv?P)w-)6a36b<'
        b'F@T>0Rl?%{L4c9PBRZ2Y8-?`t4*?d}&k39%_Fzp?|4sUVpBa;wmEFiyOzrvQDvmuQApsBRRHHbj@#KkQww(6Y<)HrTaz--_9$7v7'
        b'b5IGNDkL+?XJkNa2F&-Xaz-Owo}^>5svxtX;gD$$@+p(=FA*&aCR54-eD|XAhkQ3!vt7dYhzIv_pyx-^Rp=!L_5VPdp1e=xz_~-J'
        b'${9wvI2iB;@|TCkW6SZFhD9ij=k6IAY9Bf`OEuTp1Xz=XXFy*7&~8s60bkR=Yj3}`_psG84G*9o-*<zxQO>8tDbjEkfhlVvpetn{'
        b'XTllXl%|sM8D~3itY(*cgiYP}Eaoin(E6D^kwTab<V~{cL7IY7ZpWHbaJ=y-(goAIF#VPL@G8UYfDcpmJ$ga}*ay=JK(778NEhn9'
        b'MYECqSiRB@W$t^A_|Q(8DwF%<9zgK?KhijNUjkH3yQ?BRoH1;W>;8d;kWE>T$8j4F#!Ds3@BTzD!4`@pt|+h5?o8-1$drvtB#d$J'
        b'$MGoTD=6XQ>2si>b?#IThl$iKi@MKjDu^$E3uc$ei2`WDGxC&ktjvA;k(lZ#9nP0s5L9^kDf+nNI6CbWU-Bki<S%dP!Ax%;#Ugzp'
        b'ug_N&Gvc<$R)}OGUZJQkDhBWOM(pY)=faIFKO;OJ73XI}<f9AoGotd*1^F3~1tCqm?6886iqJxC0Vg|Tl$XuPip@u*(HYsXS>B?I'
        b'Z13<TS|w!;(HZ)&Sb=5faDkDcWL$Ag$)bFUo~C*)QRiWhyeK;A+lzwb3qT`#xc&}AFA8q;ifxp&(a}%!_6Qf?Q756tt99^{PP71b'
        b'c{h<C!xtFuXOqjDNPaN$mI#mY&d<DwVJx80nYUb+^F8?HqvV0CXW{DwRNRV&;P+2WkImlI@A5{pmZV-N(OfD?BVRBuv9nSyC^VN8'
        b'X%h)HEaKy~SuQN9GgV;2BD?Jk@v$oD@D!aDI(!c9^<J^%!X@;u5AEwmd++gfU4$kyZz6<Zkqzx{B#4qld@nn%J=no0yQnQ{UqpMv'
        b'zIaEFod~u&2=^-4FyOu0vCP}FL(0F+=5_fr{<}0mh-5WfwePMj7MWTk$$9qtA_<^&P?A$8J}X})4c47G=sJ_(&x5y7<p+io%gZR2'
        b'R^Dw>cuYX7Bn}+}&#sZX-3Ls0vY9#3Phc*eIQ>KDid8v{6odKLRD^TXrpUQdy0e-dE>wzMr;TSb@VXc4xbb}BFjuowmMp}vcrQMS'
        b'py+r>d|+nbF@v+f#D58}UHToozQ@7LQZAK&S^F7YA*y&Vv+CgjHtNESsH9Bxlnqr4Vm4g_!2Qz^V1NTb%a!noVwuxMNDOAV(I_#Z'
        b'QkB<2@GsGtkotc>M`9n-h)yXX4&6^D#4wsGAusvEI>IC&lo2{pBs3=tH^8Xzgq$!%<htdl+SI(%68B%h0%__1{R49|a~L2E<bmFC'
        b'|4zFUTv_9kMwAt`56tR)p{ZO=NpNy%iRl?x=1n?V3s!MzUM3_GE>mQEKn`{hoEgvh$`bS;O?V{TRQgD|M-6WW_)TcwE)7_Ti)8_N'
        b'kZWB8eSV&S7W;rl9MyQ#?&?R%{%^i3S3dF`?C??tLH^B@s&-(b&yw-$AMy%4nE%O{dXmnWh*(6g#`;d1T$IY6Alp|&o-xHoIYjXZ'
        b'@oDin@kQ~L_#N?$@f}?p73%{-rQ28IA?zZ%iZPufd*RY)$^onV7L5da0-HHK9CO?xA7KJ(-KBSm^ill2ZcvBWJx^9Gf>y*M-0h<6'
        b'QQLF27j3s}-?6=Md&l<f?N_$nuCa(~ERm@RJ4JxX1GyCX`}>IAE!uZfU&PhqH*qRLQu#P1Ri@EZ<d1SHbQ)uHa;g#DuP_n<S^eFV'
        b'*CGr@<t|^0@)r^6IHZTK3Bmc393=B9jhN#gjWoO|x0N9N5xR%3d`xCX`BM*lR+Bo|9~&iJ0rixfnqNaH*F6RH<@p^tz<P1wQRP*z'
        b'wcWLNP>o2l2LK*GsR`{E23EKU2DP6UX?xj@HU&B2K`T}55t=QImq$5{E%sNU?T%OGPI*vSBMpj%fTDr82Z4B4SLhX@Jd;V5!!MBH'
        b'{C!IMQ_I?dj7z11yysl*kca{$m~;8_5PPW1#C3$p%-lj@fw6}hysFTsd<W1>lT?;fbLx!(E@(==5}V{f{A8_TjzlM}fDsww`tb-A'
        b'w}-2ePGXEx0f#R08@ezb{2*ELGN<TbZhgQ{dJo5c3DFS6qJyV3(wO(`u??y7qE+#+PpcU3CqN3(>5#@`f`eO&B)R$W!sLL@n7%}S'
        b'XRDGgqtfIM(H-}d!4WnBZ4#zNI5=QxhS;%G>8LOjvlG@;5-=!4x_k?Opo%R_jwa$``QI@16kPvj2)TQm?+|M37Td9d+dfg@L3`)M'
        b'Odgk<7$Ac26g58Zbnk$+^L6e>zy2f=-9G#iZI9qzryux)RTGFTnTe97i$zV`h#rm-kuBje<P@2)p9tj5!fGg5c7}@!&GU+dJwiOX'
        b'_FjW5cCt;<@ro}9PuUlIAsa6a9&L=agPFcH=6X-COi4p0@Q869sy_h@K)A~L;h^2O!dCEQ$~*j<^g?dtj6aszn`#}R)1mn~tVYLi'
        b'5Dv9N=g4;$9W{geeKP#6%O@mt21ZY1(}hE*I$`~czXML~&DzVUVAxU#u%vaZx=_a@n{kfXD0cZWls|^6jiEDZ|GEB{Cf6aF{BZq@'
        b'FI*C_t7~s}wk@f>+^+6HV^Uvq@N79jt`XFB=ss8oc3ltZkl3(Ln^p*zovzI;B6I+(@CCE%1!Js#Xn-{}gw=J)=8LGkh1*`VaoUB?'
        b'+4=0*oc&TOwR4P9d%GbuhAG@8>VH4I*Dh(RSTM_a(mEOR2#kJWwvWQ#e4h%}kKAvYwqGg>LLJksQhBsJy1g}D?zj}N2?p){EVylN'
        b'8g4r$ZZfNMth+wNzV*;R27GT*ldrEY3*x5g9{K|W^?NzL)rbZN&F{bpTOtb745(M_O_x#Zxa63&8989w{1<6B+2Q%gbnUI4pp>>)'
        b'&82+mrQGDw_UW9gd|yP$ktinA9nW+<e6+}pmZ^Bz(~QWS0X71haU03(o!)tXto}$FeGxDQ45x>0nhpnCRW~n-jGKqmFGSc_eeQ3='
        b'^$9^esJk1fQJ^|s23Yu8qf()b=f{lG1Q@?ATql(WXXx_fI;kQW{44agd3dOKI^{L!=OS%U)}@pq(AWkpU$Evsq;)8kvnP0a%KUg('
        b'xuA#N?loNrZ}VQ;VJFK}0viBlx8=)iQbq9AXz-+{|B)^Wm9Q>={2zzQqHY(9>H&2G!cp^kftV?uheLW!jRayOoBkf2d67ogkSZ|t'
        b'#Wh-%@KfgZbm}GO@gIyqV&axIbt<Vw4LDdk70%QaBf5Tx@WOlI^H0|`@2actTI*nBoQa4NpPt`UcTqTMH#_ZoBek>PD6eF}`ufKZ'
        b'&-A%Vl;(FX>Lu!6Y1g>x5ZZla_pEPb4ei>Kdv(uO!g+SG+d~c3?R)EH%b@TZ-WazBHI2}NoG}!j(|w9wBI;ax7>~q7xg9Vrb^AZf'
        b'<K>54(RFb2UA_oMpZ}BaYSBba8(J2>0D7+go9^F13Ya3CR5didf}#AHk^cGUu_!5X<Ngv2c$nMwG=1=>6uBTk&-chLl+5va!!Ic2'
        b'G!?l7SXy^ipPh73bY}$5B|sWFF6?^>zq{)g;3Yst^2=hdf<F0Pf8vh41@_3ZFUoc1ozW4OfYZ>?xty54KdF8WvV0c+aO{=jegUWR'
        b'^%lGL7=$&qp`-reP{K?yC9SWCyW2-o&HvQ%f3iDE{--omSbqT$m(Eu{RXJ1P;XTBI!LVi1rY&GS)RdqVGn_szeP~N!?-n-Pq@Nxw'
        b'8t{Uye@F*nmS?GJ4<{}X<APnuxNK8{Jh8scnz#ilfUSFkx-(e%;<~LNbD4#$0aQVgJjVO%Bv@N3W(JN6WGD_GMn3P#K@RA*+ZVn<'
        b'q_^BRD#FU*%FNScd`xYeV+0Gl%$P5aPBv06mG2oht82g7D#Q3S2+oHkVZg3;V8N*98c;Ch>55BWc4#i89L4y*K$z;cF?1zavMmM1'
        b'cS%e;IVnK)b>kfVIt0<{ZyUji0W~P<zoetfQeNxI{EpUm2QI~N($tDD7|oZLs`U?q>qTJ$m&O2VqV$00yP8XYfw-j6mc<IxV67yp'
        b'^W|y)2>dIC|3M>0Vz!!kDRFVBx+KDOh*neZ@^yJK#!o_+{`T<Phr{)s%>iv5U5(3XZ)V0LW#P=?GQC6VMK=JE1Z`!OmFdsn`rAL&'
        b'C}sf}L}@`f!zIibJW1<2e%Q^yW%W@AQsc`Q<G=t_0(S$gkD4A7`QVHH4}gtwp-H$**%5v!%806Wb1WZxJfIpBf@bvaY$Z__N+SK;'
        b';WkCo1x2KOgzr*>#U)_FnF!di;DK>sojm23Xwxxf{T`t~@#OkZ8YvTE!+(I?QkR7K&?GfQ_oIpG5;T>aJh>OV8aQvF++MK00C4@4'
        b'$$mv>!_!zM34OWs(z4I~k*Z!Hs^3W?U>cQ)YwJ<~R(H^v=^AQh$}uc+D;*dpr88WgbB~!7^Vs-Ca2wbku0QdGQNaU(n7;t&l+9*H'
        b'WjC!a0*K*%M+1&uCgZ^|fxDgQMOr^H=|Z6(;C6%`JP}=I*|T>*`EVFoOCn7ja2Q&_FcjTjhJn4f?xuswEXl){>1ccXG+ldpc${X&'
        b'{{UUzLc`dpPE7W!ApM90=jx1Nu&Ev=iqYB|Ix6JFm$}BJLD8$S0B4)EXu&M7FLD7_g>&?cv(*YDj)M)yBYoc+)nI3FA^sg<OGL7q'
        b'S-DH)#?LS?bAfPGlYm@sAvN<kW1JI5z_i^dYPyYcv(<nn*&bFbVB=Kp=4=y|2?X0B;sgt9=eP~BXKO(g=t=R#FpawQ%(4(+$|8&I'
        b'(9LCgHiG_~p^HVs4D-586(`{BvJX$w$Tm%!fd9UoVQRs?+3?z1n}4-d_aU}56sw=0`GAb66#}sn2E^zL5vUJMrJ|W%(;8Gq-Ah$#'
        b'B&j+zDoi=@3$-q^{t{jLuVo>xmT@p3WYvO|UjKI*3=%s00i8Ew%)CG^b|P8R&Qr!X?&7TEIBvX-n3GTKT=q8HseDW%BS3cDWVqgf'
        b'n#s7h81wY9*Ti7lQRo!%MKE)i=#$awSMd4Mv>5DOTri_*!}UAvpZj7Eb)C*It)}(e_r!hhc*?Y$)?c}6L@^unQchX9=4f<A`H?e&'
        b'+%e{mXInVr&XrqfndLsfFfOY9n&A-!u%`b4Kwk=nhLQnZPm}L#F&-?{sBMR)+L9Y075xO~eV6~g!kJmJJ$#@QKmrrE6&C^0&<fkg'
        b'B*=>H@$a(n2N7B6d{C{<C@8eKZ_)49^azx<=#rO=wYOI<o-^f^6j{!{DKT^pO?FG3>+Y*Gx(ma0iw-6{*H|bDHtiR_R*&`s*-9j>'
        b'C1QUG-Kr1=m$kmP(x#9AvENAWZAQLK&$A8RZB-#t4oOGbd55IgJ_L<4>-P)y%A#EFO|`yvkOg3Ro(2U04Az0D!825nYXlO%q1#sS'
        b'R*9ioY&>+(z)JicQ+}A)D3iq$t;G4z1WSQ<j8G7@bo>8C>vsq}MnHND-BzWUZW<Xd_6RH|P3G`=34q&5AT|Xq+aA^21tVv(b-PW0'
        b'y04w^Xgdey+l?M#Ajo2m?!Fe>h8-8SM*vAEs7(sw&>)Aji!ctajLsOIq}w8)!#+o}Bd9&%xDYm6O<?-Nh}swg7NnoqnOp=4>M^Z@'
        b'F+ZAa|5IfgR~h?M#%C6g@lYqF(H2M{db+%|Km1Iwh0hubhP%*<^k}!)t45`k<Wz6{4LXkVxCX1O_o0#$(DOvZ7RxDb<7z^NZ_}61'
        b'kbYD=P0<&;KuU1$qQUM3^8Q{H!Z#<cmO*>K0%`4+_NU6*!T`Z91T^S6bgS(y2nT-xr9K=?oX<e19|xqM{9kG4qKwklm4}J)?v)f3'
        b'm4{*VK;Go|SJC=}X_m!W38$ODogc2s@8RlwQ_gQn>b*4bXj6QY7Iwr2s>7f!QP9@UXdv;|AEOZ$Sch-Z%YVN*1_n4R038Fp;$NU)'
        b'8&4F34d0;w`Y_AM%>QQA!59XWiKgEGszo??`)(UWO2sE76EF6iDREI^<>O&1KswsAW02>+bAKT}d&cHl-Y@r2TqsctL3Pcpejg<!'
        b'2jOGCF9L5OPn68a8SqTYN1?U1$+y{@F*tb`K0V!!$B?~`<b!9)kFR~GlSmpU={s5iPoRUKR&*i_k0O^qxfPV}5{~Y0#UgGTnb9GF'
        b'{C_TCtch+E!F#}%;;j-DHVW1(`F#-!)Q&BS_)bOe19yY;A?Wyl67PW$=Nl#cR2})mZyD>DeV6Qn2Xk=zx9O%G_NXR}N6OyJ=EAl?'
        b'PnrNE`bayW$>sY@og)0~!7F)9pc&9=;zO9`Y%IYe+C)vM_8{9i)PZG-96)kN4Q-#tmce-}jfd@jsU%>mKMcRX{dk(*C+gc?(w1Nk'
        b'?raNd4<^4@!`?DJRTQ|ZvO9P{)%p6(b`=mkn0P6@Z^_Bcj1D}(BN}DmsM<vhQm!Wf;NBAzu+s$-?HY~G+c&}lSTU6_+JI|O_;X;4'
        b'=dWenMsx5p3=bDP{@W737X_2WC5!{V6~c)h5AMN7$UneF$adUIjneSqMGHCCjMt8&CUo)OS!Nq|uQVZR9uO*0Lvbz;-oY-WQ7zkZ'
        b'GhW3P0PLuU`X6Y`Jdk}JBMj?H@2Tc3Yx|rqF;UaHU_bfHnJDT^FTpWV1}iW5Wl0u)ekeAa2k#7PnZwE5MVGwWE_iE!6aq_bU&qWS'
        b'eUY?A@mSK}8il$fEk#}OSi;s~?$$j5Fv~OH1?&ZY6?1tD$mOsPiiDC@$pX3j$NBA$fm5hTnCA;nF<byDQo)Mw=x0Ra<QfLL%yOsY'
        b'v66nYs4eJtRJ*8E5st^Sr?n~~+H+dbHSGzlin-0r+}0c=9@LtnYSFJ_JnZ5@luJ2r``V|iIwjP0u6OxD$>-o`-{lte7h~$v@)a2W'
        b'BU)hL4KXoeD5o~_2O4Sm+{r6xRmiAzv2*vD&UPOjS^q8FcBH*O{s{Ejj6h#@XEks4@W?f=eZ`#mJ2coRLHBM$-9ZdKau~jpu#E@X'
        b'Wg%b#e?dM8hsyc2fgCc-oPWTe1m7CG-x{3X8Tu&;Spnq~je7I|nEx4T0&`9~VaSKtc(TvHe4Tg}JRf48WzXJA)oBi=ssVFp$5uyh'
        b'+d}rXMcJkBDRyt0*h9!f_xewVk{)LA<lJTQehcSr-n#}nujv!pA+)h|BEGS%>1$Y-{~xrh`+hyM!MdnW^7}$~!_NXe1ExmBr{P$9'
        b'PIiLnN3b<8cOwIIBy!Ee^$GiQ%HTa^aGo&qJCn#ouum%849#JsSN~5?@%x$b9u0j+kU?t#X7(V@McxE9{%3>t&jx1~0C0|+2LX6='
        b'HYb*n_KTuDHYay)nruMr!3a!w;_&G7Snwd1e8a$4T{9M5idPIaCtrol@Az(vOa9RihyVm>BljW?w(m8Ax82}u1>i4}I0S!A2MBt~'
        b'Ga*HLTmbwt!RG+@k<(<0;SstTDBEE0HW{3CpzIy;-rE2Bvj6LmvSVD(r|kys|1vnY82Vka$?ssnHl|>zJf{v6Y)Fkrw;q{LC0dU_'
        b'ZL$Y;@Wf$q%M27|Y`+nVF>NR_csCfFMgZywasq<d#(+vmW<jMqzImm=j%^dTocyhAzwoFp^1G9rC)Xx!`f<k*>VTNs1!?bSj*7p7'
        b'i021lHSNX*IS}@54Bi5R^EuGJKaywHGDA<mp?|Ds4*`choDeEK!U^3u%|+hGX~12QSr6NYD4sF^7KL!~_jY_M{$75`%LR-8uScka'
        b'QwDI60}{r0Rt}t29+b4eh5+sv#>WJV2Ela^oQoXy{m_ScbaJs_1%_kG1_<}BZ`sot7Kt@Ecx0Nr;mGX$SSGyOh@@rUk;^nw&GIb|'
        b'_6RQdhhoM@wE^s1x5wujyz>pt`G&Qhlg*FpC8XR?d&eUr3Bx04(FTz6*n>5iG}kacHiwKcFqcph)mrrj&mhSXG6E(fs)rI2uLCx('
        b'JDChMFq;w?0{_!(T9DdsVlFuwzJlk@<S14rn)I9Brl}JXlc1bH3YppY6W~fnK7357Eli2}h@w73x+Q=r$`j;_&-e%WY5%uCBtuBq'
        b'Zy9F|Gh^hRV$Y`Vfri!~<>|1%=;5CE1CsIY*LlBR=lp(M|A7%Q4|cvRKa`w;#ORruF}{YV53C7dNcWH%`61+0m_BjE`PI6F1Oh{#'
        b'PFnewFxhAKr)-i0)f6Eid=o%&n0Z66bc$-B<SY4K(9Aj7Xd3zUI*-t0L=>N{lQkl4pUg%flxh##zL-JiE|5JV48-+QjIUcTs=@GJ'
        b'f<oa<^&bi##nB20tr*wEmypBjn6BbN%2sF7ipg`#Sw}|?N@(NQk52EpL6khhw7f&{mvw-k_~6Uvh&@D;-;gXyYF_8akLNJ#tdpC`'
        b'>MfmbuX7{FBj?6P*WsgCoTRtc;lZxcTyngC;eFPnsvSgjAVdkPL*9oyb1NkkpQ@9j*^}N{*O+YMU=Mx2>xhN@)Ei^m6a4_ES#X~3'
        b'6OF&I&ilqX=Ns$#ohouFz*GdmZ;E~EIz!Q%SoY53Am*Zm`b!XUPXR*^ZBBHFXaL>U-LiL`ckeo|rwKauO3NDNLbl~pA!Fr=!m1}5'
        b'BqMgauxVTL*5Mm;bb}*^+_i3UFA!I(F6xa`A$7nShs`Hdh0KZT8_eaPiULN_O_VOoFMXn>^vMR<k?nlOJ3f9F4<=jSXGr89#M`;Z'
        b'`-UIKc`Pm@4!@bAQ5=m8oyL#_w*Yn6`={Ay9l`CbLC8;$T+<ITr{2(N`yT6;i5x3nPK@!{Fjx@a*>BI-ukQwnd%h|}@!NH6;A!tb'
        b'kfL}U6tQe7R+ns}e&wQ&`I?X^=t0S<_|3XT!iAwocdYU*9nh`AIrTQIpc+#wUx#y5*ltlgTKm&N?tU&l_Y(ES0w7y2+XGnFyrt_V'
        b'7fFhe3plb@xoYLY6wR~I2L^+v!MeMzUwIp}jPH=ND?UxSter05k(=On*(Gg?Pm;dY-pre@B)WhQ)Nojs_@>n*LVoJtr*v|5au)KU'
        b'Gx#$;LZG7H1}(3VQx-W+G<6Je-2X$X%0_F}+TsPZ)Ace$!xxmU9u&Fap18;x<4$6Lth_cN(8|~07$A+u;L>i9t#eW7%?|mCjZgOn'
        b'p~%VDvfwACY9t9;ci3x$NUcA2t2jUI$(k%AKMPf7!E)WdWhmAdZxDjayh2A4Pq%~gHyA$qMcJjFviO4avp}tb9FPI`)qf6oYnb;g'
        b't$YGii84QCaK&+dO;<Cq#mDI;*+<<7z9$u{z0Kg%E*sUXt;@Va1GdsAW%|G#tU@vlZ$2>9gXbUU!1>h|EG*L~gw^o~EPEUTRnLN&'
        b'^KdvAa`*sFVE%DT|6t+x-~G=vE&l)5CiiFb3Z{Rj>88++cCfGjX|`{HfcST56<1(fLY<Ji<~;%L+Mf9BLJ=6qJUEc-qW|-6;i5+b'
        b'U*pz(?!H}ke6w9{dlp)NWy4IF*XRI0jXwhx+Fw>f?>{$f&!V<xG5*Z`5GF=OF%t{@1l<(&Z+-gxOrLlH<1El8<rB=%41=LzI#Yk0'
        b'#g+0rfHB&L$IcXm@Q%?oWsu&CfZ>J8h<}3tin1`+xJm#=@BbT&9<F<Y?hF&e#Im<=V4!=qT-gtpHFyx??xXE)W~hE(+BbU)!UnSn'
        b'z=j9$@WKszzBV%l&Vup&w>Fx3XxqGCeL<j&aKwW_6PW>rp(_KiK-u!%|7_pT|E7JOnf7(k_Ot)5+lPz5c-f<%{sk8;<UaJBBT^ov'
        b'?Tt_y^^m<`^B<w@I{;03Xup7qOowTE8ic{72WT5E^7qlUgfJHPqv@tzkRJZ?H02?X7U6vCx1c|drn|vdC8!=WgDrm$q{aLvTz@x6'
        b'pZiE^pv|T(kp7E*tIq?{9{YJ-=r658yFJhJCT&xQzt%cXTSDy3Jh(EMt@~m5z8l5P8^t~f@jHJOx7&38VT@nKFILjG#pl^r9ZA=U'
        b'@d$Xyj3d|VVI0~)|HU`w4=~#+`DJl}-6lkCWKDr`%~v_i`?(42ivKA-?_gqZI4>4A?MW48M|8H1L*uwEVS7X%X54N}@kw!9LFf&0'
        b'nBwonahhPor^U8&cUvjM8o!5$E%rfi+_vkA^TkKEeWw@)-){0}VuIp<d-Z?UKjZ;rHjW)TrSVAjCD<cwY<uEHL3W&Gaa`6jE&?^B'
        b'AReOWiXH1022GumFt5tRNI!)?u(!k=4XGcxH8N;Hj3EBqNG5Zc(Vr}Xo*a}<$sk+B`e(w0iA>PNiEZ-6x(QWVNGb-ejojEi`$l1Q'
        b'Txw`s_LHQi7;s$pF7nOdy(hEbZohVydm+*#)$c$^s+h68a@QmJe{pajB%S?~+5b5BEEC=LKaH?9ME%qjcLGcsx$9nuz+2@oZPFAE'
        b'(;Dw6HzAqd(fynt7lkQRh|7rSqwe%zrtj$CFPZpX4aNH~JJxj09uZft=!Q8sP7@iIrC{+Kw@rO?TfFn7;xhX;cyN6X;*t7m5q5mR'
        b'<06DP_`st*Qsu7^z|Dd@0Bi8wq>{0+DC91j8y?hgV;g>>;K_$|;0|YbaYO149;v$wVfqUIn_hTW$CI!Q06!-{(*`-tqMt)s$Uu86'
        b'0PT4enyK^wH04GH8i2JB8HTX@nQ+5c>_zgjie+k{kw9c03APck20=bQXxZBdV069(WJw>zXB~{Ve}Hdkyg{@F1JW&c-oe#iI*xD&'
        b'nol4`0`u{Lo~i8N54~t5)8JGqz}CJG(s~4Bik{I-t$t-*52m~fY2Anh8|3>qLEs%$vK(IR6eFza3MqQ6=zuK<T50y$6K&Z@(O&Qd'
        b'xRK~p6!Q+XKdh|H-cM3Q6gQn{6E$sbOK3_}US@eFFXEII%cj9Jmw7l@glr`THauS#q`XF7YXseyq_0KUv7#eBA*&0XNXx<oQ6E<b'
        b'-u^|87BO1-%Mb21l7M$r+*>QV%IQImYr*z0pv7Z)Q1>{D3CR%G9#nZ1-pt7v;}7ycf3Aa<(H(;VkPejrJt#EtJ;%y1<h8Yf9J}ym'
        b'^oIO;Ews6LK%b$9ho-~i7i;lg#{6~0me7tZ=Ua1E=GYxrZrRYX0p2!g^w#atQ_Av1iSYUjC%4;b7?zV=t6;>WGebE`Ey>Gg=TnIB'
        b'(2!xhc=AQL{#`_WhK~z}r3gM7>`s?a|4PJ0MDD8j8r1_@6=5@m+l-OZL^vQYc*K;W?w;_1F9t?l=m}~^l?J2@-7Nw=3v!^!T*RM;'
        b'*iqTQZMbsFBF=#g!etEKbWDD!1Tn2ZzD6Ow2w#lh%#h`9k&CQb#hMPnKKdv#^d(OIdDTPOG?T`(Kd}F_QYetJ(jAbJFlOLm+)+=W'
        b'qi(bS$cxOJ7ctjZpo{@e5D2t+h4Q>zl5Uq<JujTkmbkQtmAdZIqBbqZ>d~g#U$AMp>DKEuEic`!wQ2b}t)SVu(noD`X|ZRvSVxB%'
        b'7V&(P20Zk=4DjOq33^o9fj7Zf<o*io_uVnecR>;8H>(2CL;jDrQ9Zzo?*9=tTmc|-4{)P=8uTaT5!^)Cj4{(h6c`g+IOW*mBBCLB'
        b'RAVrxw<#0ZEdnWn0tX6cwMhd}bB;j`0&oKc5qtz70_aHw=wa?05I)rmexg?eyc{sN*uvl<^Jn;B)3gkJA{p=hHe>V>VE|XGff#7Z'
        b'7<Yas*UjSR{|~%82Jqs)`3PS8EM6Ai3|=m;e2AAeEEQeCZO&b<qpWG$2c)?fL%0Z+?M=ae5ObnzJ60hr?+8yh7TQL5)Y03SFGdRK'
        b'F56BRjhs_YElW;v`Em!)qV6#+`2hrMMs269Ic1GcRiHJL73UcbSq-J)O_}o1Bl<c4F5rhDxM27et$Yl0JVoad>u+&g#8YKEv@U5?'
        b'yTtt%(k5v&F2W;QjVaT_BCt^gO?B)UKtY~w1owh2_;Sbi?s#M;K;~2FN968E#2t;u=HFf@0FynEHN+{4Jc9>;?*Psq*DZsD(QtZ5'
        b'gA%@6!(nT#%Sw7+Q-?nf;Bu0|8`J!mbC;jt%Jj_)uHZ0aN&5+;dAIU>w}kS@&$mm`cPp*!^4>A!`IjZuCOLKP1)mn7hOYaxs7uSC'
        b'&S{%HFSxYaW{6K-E5MsaYi)bs{Bx34t<c(hy;U1z(*|4HSR~^Nl4k)V`?Q!%J6orn(`#Mtqo!P1eydibqc+aqdK1L8dku5<X@%&T'
        b'C<bTN;3dYzVZTpI5KldW$EnffI6!*U$_Jr*So<fCwqnf#7o!2X$^|_pGuJ$%FOWad{@eSKHILqBZBhfK<jqIo?LubgZfL+3CUD8%'
        b'=FGeD<xm$T_kVIL@V-FgpS-24dvJeF-u$D@X|0`Zhz!SD_o_o(?<Fb}tE}Cqyj#9}m+2N0P?4ZY_o|cnT&om+TGe~p)q7aWSm#aI'
        b'CDyJXiu%ztlGy)#qV*(-bW3`><)G-=;7l+vY%ZjBdaq{C`N}GaDb{QKk@C2x1KP<1Nw;eX;&X`XSv~o<#OiRJ=%0FAB5#KPt-sd-'
        b'n6`6?&CNdom{vR5`d(sVx3yi;+zsZ571pq8_+y&g4-3&^eu-|4;bqsRO<Sz%hYTg!#xg^tHoB}LX*vHWU@0i%h7Bwu>*}KzUxkpG'
        b'HBR-a#=68(dBX_<`P3Tc;x*PfYr~0kvNJr8T}@e!+IUl1L`|h9+O)P3G%>>`JBtjU7X@QrS2lefiVJYwe%>-Aj}6P?Q=pqZmK%=B'
        b'd$9IA)2E?rdC{xV%60}ZLh&FM>X76Ri6xP1+E6lNm8GIw^BCBhgUBcb*L-*<N|-4HvMawB0l&kSX+SSa=B%-p$=Pel2PR~%-s_vS'
        b'riVxVzL2%=OS{*vKyuH@$qUbegbF}`9g3ss<40}S@Oc<z#mQNNk5X@xc1eo5t=&HIW>J?GtU4ii<9SAZ@4Q~*qwszTapaNT!z6p2'
        b'Y#y&o!Z^hmzgEyZbR_*Cbns6-jB)1?_BF3ejeriaeiqdJzg7l94VW1hUMi&To97>-I6p0to#m6C7L9*gzyQw$koQ5z%?}~B3Hx@e'
        b'>}?khJsN?w&$O}t?fqHG$Ill=%%tqgVAB!{dmoyKyUbXRP{~E8M!8;ebwE2N=)oL$rZb`bcR~vkZIb9!g$jFKbH-3dvL~rcu~S$q'
        b'?CipZd+8oN7zp1=W*{;fS$TCWBvXEDhA+}l!TFSkIn8#z9nzE&oH3e_&FDG-US5M^2pHSN|3vcMERq}L&`?0d(_a$cql4IplWc<-'
        b'piO2EO1}C$qiKzo#5)IhG1&Xg_&z_hbJ^ThG<t<$)Zkmw6%S9jCk*GL@=^uNg7xtFy(<4ih(`eaO%ow_7H;$i28Cmoqr_Gsj^FHV'
        b'4FkfYhsPw5@h$F_Fb~h|3@cl?8n4YxdQS^JaZSx(ikFJ|y@?(S4_E#nEXzB{pL$u6W2dqt<o2Q*I}^@u)5Ac9S;E?{HU$C?dU&QU'
        b'LOjsa>{190LnIMSEG`4yn8B;E(f1@kjA3;9=AuVr`4VIWNA|<)CR>(Kp8>t=Xc28m(Xu@}jWm;oAlh}{nXe(3GY0Ki@Pca8gD4*5'
        b'R)*<fBL)AOtqbAr{g==cD<ky~u5J%s|1XpPpDr<p`7qI?K*W7=6A`APka{^XLkfcsTP(gp)Z`hcV+8x!n^e{TTL^!vIcVTnc=`v+'
        b'4t%gL+IBjlAsTYR<gbcYmkl5E$4Z;t?}6?a$TXNnluDr^s3e4Vp8v3RHB<Y{gDDa5pr9fC$S`Kl2V<cuVo>k??xDP%AHugTjm^#d'
        b'F~x*s{u0Ss^?YuI+?o+v5TbjY|7DmkKUVx@7?vqP%!g%sE-oy<92gn&yfs6dp8jLgN>^;y@EimgsDoY?LAUrwnJCeY9UL&8`vQ+N'
        b'WY?vqZy8;0J9ovJUDvd}5W_{oive#H!e7o!C*+{@{A4iHU{vR?pPdzw-aVA{K~sh<Rt%pG57bd3@(YZS<s=s|hVaWocor7($uiAS'
        b'@^;~}f?sK|m4*y4&aVhDKMUFnT5K#u-d!JDCgSM`L_ZI4m4*#`P>9JYZ|Y8GEQ=PvV1$rv;i9e&>O&FGh)g*sH7r38^RqJkjVw-X'
        b'ZfFINstp-K4X>j1=N++`K?qWCV4&_IcZ}ZyFZX{LHRqA`*WRwj09Qn141F2;as9jOz`}TOvD{G&jt$R6nriIEQ4OHhQ3yF)*Z}8R'
        b'J(z3c8So6|8sn^k^nw>mO>k^`__A$x0oGg;YPuh41GxQqHkc%Pzh*FeypXvmF~~9fiw55oihlOBzwp8AbKeeS?f6D7DRvh0^%i<C'
        b'|Kc#{R|g>v6tc76`iwpv4?d0^mmVk7`TTxkq%L1@Tz5SGxDju1`PPz6`S4JLDvY-|TEU;gMgFPK(GP!oGkbU6{z5>W62oTRf#3w&'
        b'C1u)0$jDuV5BZ3H|MvSwz6GD2S}qxZ*8U?I=QAWdSpS(VWW)c(-n+*&aitCXlSwj!WU2%)MMAro5in4!A!s3pEkq0iwHty2u=QOg'
        b'3IeO$mR{_|?wdp#1G+7Z3W066AsB9z3e*eUb^~prQtg7>y4LD0bqj6Xwrj2S;#Tu}&Lkk-wfpY=-uLtS{R5MkGv}P=Ip;j*dCr{g'
        b'Od&gdUx|QP3RMyBwzbl|Z<m@&^kbgi%_#s|Up&gzHvGB3{7B)Y>kaQ0n14C;_a6()C1ZcTTVP&1=J(JAU$SxC1VW6Zmli6G_i0^Z'
        b'nAWH?CMk`m9l2O*C~J;eX)wU>PuUWBh)d2b{=2V*KExx}4xRF~D9QLPXK3^(pVm0!=Oh`-->gG}VW4`MUPj$n(1ItIADjR#dlroC'
        b'qj4FeMjmAg(@a1MYf3v|n7~Wd7P@*1v`VFMk~tIAap;V%g|nCAJ|0G{Q{gIF6{=FJ^eQ7*8Pr@dq!-m;)k&o>R0%^y1c6Mc$aduW'
        b'^K#xgWfqV4)Q5KbMt|;W<xLeD`YsNA$>vACRs82L72p5f+Q0kE5vZ)r_`>LriGJH5VNb{lhsI3=`B<NLIX5}#U@pnEwxQ}uh@{06'
        b'lQpk!lX-dxLB^^$)f+>;P-((23>*@)+2(YRa*I!L>Voxm;8Q#;NDg0XtK<-<|C2#E6AEVqNfuvpG<92b?=MEv<zO(3HJqr%98qm6'
        b'oQWQ1tEV-}P=CRD(x=n$UU9bv&k9}?Ogw}^ZpoarwgPS?CwT(FLCTxOm#n(jD<Q!1`z)q~ShEhdCSaewiF;$PicO{!@G}bQ)*Ll-'
        b'w0T;^r`yHH+H7LyU-@k(q%HlAQ7LWC6^}PBOWcbL#;52h)4@0*6wI7vzqpk$*XE#cCLy|B|8H<Xx|}BPF<b`XGYYhgp_-ddqI<p+'
        b'9`Ebcj64Vf{iwJ6cUoeI(m;@Jsc>Q;)LZ<y<{3lPSEd!7&xvPZzT_&tTHHb$8n>7KIb}YFe1Mji&#33QgHTJ5;?$|n39AHqTGO1w'
        b'J8JmzoAHWYFV=07J-Sck5A9qrcsKEAo9EfxtuZ@^ABE7+c<~P3=4Xiq&<lZf7d+2R+J!&1DW`wM;r>5cJ_A)B;)9;YK~M#nw$8v>'
        b'qMprrG|}_uvz}+73_Jd=u_4d4fCKvFgMKGga!8?M=;HB|Lwxdeh$C8&VA752QlxE)de7k){>d2J6$5J0{jm7d^Ub^I@0x#x_WRc*'
        b'n0r`hh`q$KZLLtPp?04mVb3vdIQHjh5>%181oVuMt%@UII3fys&_m<Voj*|KE_CnrR7;E_;j~{9&yPRf<|@G+t@Dr(2X`Vl>k`~8'
        b'kmd2X?x<%IAN{-M^QcGjJce=StobOGmk{%~3b5A(V&ymf&#JI7$qvC@?s6g2X1icMK2_MVP~W_)El;Ni)4h~%{H>Q;7gTTTs@_OJ'
        b'a4}dfZmSzqiBswZ>%`=Q+Ko{Ot_9>I#f&aR5@lND8B7*eB@V8FKj<ALGd!d~QMqcC;Pfi7BH3gvDuA=5MAJ|lZz!H;UQ}R_W0EYs'
        b'O_J{rIfyKt?Wu#Gdj%K<<1&<I*mY4uV%VBZxEIF?hVwTOV0|oBAx84N1V&C=6U8gEz>#fuO%!KQaG_;Q)Oc?(IO}J%7Vl!L(qc7Y'
        b'S>J+9O#4NGX?54j83k3VO=~Hg&C@RMKrb)wcwP|0FE}=>_EbB%Og~SkcYv5_bsmpa3@#}c;53^j3x~^Dp_O>`22U1U7wX*PX{A%Q'
        b'uGthUt*Z;Q?0*})q$4&=#QsRF#Ir(Ew`ID6rC^}dZ?hLyV<PrPsx~x>j(jrHJ-46&{N9QJqcm^$Nn8Wtp09rUvqGbmE>LEvrFnx('
        b'#D&W8#AI&%WSp3WDe^ppO6l~NMxIKoxd%(ulRPPU_o-f6VV!~<*&19>A!4%=<<&%ED7)f9V}Vlrb~v0?YH7p9pe(g0qb38>sx{#l'
        b'xmByq(i@w9DOymdFVBFPJ`I}rgO{f*sNQf{GZ%_=>=$CliM1P|a^wqi3%Ydql<5V}V1c+Q553Sb&yy$CE%1=gG`c0L77^-(W!X@Z'
        b'EH(OgO`>u#rcy@V;g7kqteRJR0oHeY(2=<un6JrTh#l+rGI>a?Jq(%>tOi=FnRW5Vvm8IUHV=>GO${c%wSpi}#q*LF^?trhOh(9T'
        b'A@tEfGFVo>O5Rz=Z>B?IdGzA2gpYFQO;}PmX+`D_a*yRvCv^cX6x=H^I-iGwc{;(F+rt7j-}$=5^U+4EE$C4t)am#!Q`Y3#&k9!d'
        b'$}&R02L!i>ek(JU8#^1~gIsX(a@_faF1^#Fv&jm?mRzDRw}8{iZJqtfHjoQ4+Ke(<cM7tCENmfUsLUpVWZ)~w*xdYcU<;o5X7igd'
        b'sqdOyD19p@In>743F9V9tO`Xfg~NmZT}G6s#Z{p#p(wQ+Qr84h)1#^BnkASvly#r{=|fd?3my45q>o%{t_q}Aj;2?l^mHJ7IHadl'
        b'$`&;V`A3uQntvTguOCgXXZwwpgT0#}VtbuKAGyC;5oUOt*U*?-{qqE;sw?uSVg{8q+cP*FntgCK`jaS5s*6!JFH5O&wsuuNkl<{l'
        b'6m6ct6meT4{7Gp;uRW^sD4mhjtJWtghbN39{}6d_;Kkg?zbKo3NyxB)hw{mBk$s(2xsk`uG%wfOhoL^KRhRH|4*d^mkyfiubB6tf'
        b'GzfY9tGm*+B$!^HoGl*zJ8D||e||Hrc>|qN*AEr=IjTTfwr6mYIJ*rJRRt>Wn{n0a)@P|-6~u%E=iHx<`t2MCuYUJVWw)|Px>j>H'
        b'hP^5PTL1%2sZy6T=4R<XS4*d>^or`R-v|vVUdQ?_#Y+ij*i?E3(Fe5#E76}i@o&i5_0i{7cYtAeAfdXJQm8zG>yhC^*3(mm_S4TI'
        b'O)2XYt7OUQEM?3D5-!)j>Ilw^ebI_xnR4q$tQNgUz<yrzxUV#H7Ve1=7tx-q$)(&uT3k+hmWb0d9`v`w<0%o_W|teOarrPp7t&dY'
        b'a$J-Vmr;=0B+t~z!VIB2>b_jvYYDO!x<Fgi4$mO^_!VMI(QAFyY?RrXm(_2S#dcM{lpvcznP?CCXtf;vRM8$<Jf)5!%`k7sd-*$q'
        b'_VKD0R-Re26W8p(=9T8R6!ge)yBd}sZg}Km^D@^vyPm32o2tX6iheBf$X&9H>4UN2dV0|A|1<TDTF1{$$vt*g^>^umuZhps4gLUs'
        b'kWOgNt9QtLyS_SB7MCHld8dK>-<U_-i#C%!$m@`InV|B~RJGl6d4^=IBj%XA!`>zP2U7Lm=bpjeiBHuHehz>9*?L})$?8$QvJ8*N'
        b'W`zKt^BeuV0$0QG-iAjGH!m{{hOLQq*c+A`UgS|<>aVLLd&47ZHpW<*msPzWgX(NSdUArET;jMm_|t~;B$InA4a;SY_0Vsqc0=?Y'
        b't}M#p-pehbO^nlEjKL%&cb4Y5nwOQg?O#=TCmC*9H@mrJQt7AN-yL1kKkVr!@ho-8mJ2?maUutUfZW1hy$ol_$+b|}e(`dF<W#8l'
        b'8(--P@S@qYxXXz-ollUHKBYNi@Ml5Q)lXEH%Ov+=)#V{I@gXL!A|?_=wf(>KNMf*#S3ND<db+;Nk=V*@=hkr!h=;cOY>5uee$*)?'
        b';dczn1;c`%-;mG^Av||HUX@YrI8w(KZR;?F*&CJ_3WVlO`VJU!zeV$fb7a0~_5T4SHcN3B!mj3Dw&j^#=+Z&THI&olfgxE{#STt1'
        b'>E?l!mgyYptrIbwDGXY|(84pnsMq}=!Q}38x~Yy`p263}yV?eK`Tw{Y9@()`-qpNp7n|uHP^KM_X}8$4)&ze$Y^ITHm+M;AH@EWY'
        b'9tSVjS?Q^KyhOq)_zuL;PZ30K;_7HqPL@IaHV<aBvQ-Ngr2Q&Er>BbYJpILDoxuY$ntvXBF0XKL;N4YPrtq;c^D{4xM6uEL`nqWR'
        b'WKYQ99>p1_K=GEW9sgYXA?F9G7-lU0{ytUC$X#ZEf!#y7ZlSIGV0dwyuWRz?y*yd3texw>*B#9Z#G>8Ybu+<h^|6GQ*_Su^E}3u9'
        b'VY3~#PREk%d*07VB)Lf&BCNq!%I<CvcuHAlCI1_gXfMwo^36@O*}IcV{x%3_zeHz~?U3~^(E<Sa)vafbKV^^Y?C~e;@k#dhWA^xr'
        b'WG%byeFFXJqC?nA$NWEL2Cg0P|4d=8y^nq<>CkoWcTJ`P3EpF~I?P^wm#v6#-8acD_O+p1^nFNL_Uk71nK?!#s)C6=#6PkDX8pBj'
        b'>kD|n7MH-1L#Q~abW*S;j3ZhNF_bbV=%mx6bUFt=HYo;7k>k<&e<f9!bCQuBW+KiokwYu7VIhyrW!(ZfhvX{Nqx(HLdS<e}D04#|'
        b'OClUu4=%&nSmDa^-jM=hIkBj~2^`TXdW(-{3#8csWdkPikB4|rB>%D^-A|$-Q9k^2xtA5mzAI~e5ZY0K7Q$Q?YWgtC<cV!I%i@U|'
        b'v?KvO!^;mpSZxade_>=z0uOu#WCF3KR0MaEQ%Mqhq`C_zan6Hq#-HB5@e4hBSbrgK@1?SaYA)E(ve6ypj6n8mdFH|gU5h7Hv;N7Y'
        b'dsry)!pO!J)aMG>hmvtA&V@3=2A<2QGsixN;;iBn!+GqGaNw!DhNto#e$M<f3JA4AZG<*Xo1)FuF4UH5+qAp1ecEH%Q`+<D@(^{o'
        b'SX~~fE}x*zj?~uoMyHT>v0DhJu)y=BSaHn6@$u?>rEod7^G`n~*AP79$4Q3XyomPVJ26cvhD{~xI3~63YIO;*<$_1sLLgR%KeDt='
        b'Xh)y>xW|H=oA~WZ>v-_{9?P;bQ(lmz;!`H!nplh$U`FR(i|CMttxH33VhUy#a3cAZ{rJEe4<3vd_}PQHy}i1rCwEe$D3%lX+EmfX'
        b'Z^=7*5A>72+xPph-UENw_W-~5zya{hdJnv|?|~V;2U_ztPpi2HcTiJQcgY|Q6IJh6weF$MID3hG_l}cATlNOU#rtFNy#!PTCbhr&'
        b'N<?=!#PM`&@YFjFZY3b#Sr;Lb6}|GrI*}+DoLnwuIQK2-wjT2tp8S@4!Fn|Cz6k$TB+%BEm)0%KXBM!lSZHr)^cQ2!e{t!&`;>2V'
        b'kCTN8iKPk?<a`HJAkfWNU&qmWj7ia!K60X|5WUlI-8=gIACVEd)>Tg36Nc!ElJ0bpFKzsizw(C@{6aCB6WX~w|6E`ZV$zhVJ!eE%'
        b'x48dZ@veiN-!16deSUYB2-_*{JU4PI+TGFd#P+o~@ebDW^@73O;$3^XMNSb$)@$})UC#0y;R$PI-ZAgp9pO=3&e9!@IPWgBXJ>~4'
        b'w|2w9vv8o<4hN6z2p6DrJJLo3VetYlAMN82axBheYkn(?=PFLf?nxmwV_2lXbVBBB#Vq^(U@|?C`YcTNYf@qw-d})r)>hdBP63v='
        b'9QS^N<uAvH6Buz4@_`eY6PV_&SWIv*a^Kbz3N&??=!Na2xaMB0;hiz}_FKeKyF4oLg}JWQs48o7bdWsE%WlP=63vZQ$41F{1yKuW'
        b'y7xypPEL#!ObuT7gT{&#M6owMm$%X)%L`fSZjFkxz}+-o9)=d#^J#9p<<h<1x8U8OWc1YFR>972xc{lEi{;6~pc7uB%;G?qWl*JC'
        b'zl-m`%lpvP_Ym?hHdwgET{8k@J@}L4n=>lk{g^FkWz};wr!8b{_s*!usvU7W8@h2#953ExS%TYmEm2@5_kZ6a=njXHs;uZvDGd&y'
        b'EvQ5g*6TEpqV}K<b3SLx^nB>}pD{;sY#h<=s%^O%5t}AFkftu3O%*<p%8@SmYVbv9b5htUuyF=$xs@Cu0_JKYP!}koYHsfVP{h8t'
        b'fGktu0(yWd`Sk!=5NYnfPVVoAPL1s9;P1t!{(kx^an)Ds$a=+L+26lr*Jm0qW$+VzK+jy00ztg>pS~6`*}WzL*Tng3l%9)CkrV4?'
        b'kimr1hhD+0bF8Z4SYt5c&gU2K<x!%%euwzm;^GF%|K;ogzLSqVN1vuc*6ItR^5da_A@ZFP&-t8Hc74sLx?6*HPSV_Y8)-=ln|pb>'
        b'567fKVh1B(e}hM^i=V&prT7=YVUpV9oHaDAdEZx%;Gin`U~T$i#VSEu%w4C+i7~;rb&Ah=uaAs|LvNJNs`6oEF*>GvR*jG3!y)lA'
        b'pC-pg&VWNrq|f@0kDP<<o8;4!`0k?!n%U%{HYu4VHRIAVuNawEE12I!HwU!{UCf*2Z|0#Oo@#P2Tj+2?*%PwDc&|L`3p?C0Ph{Sn'
        b'%f3dfsWrG&d+?Nn+C=uQ{2^9gXWr1%i!deCG!Ku>)%S!b8$K~VGVkT(^GG~p#>%rw<~KC+63x6wGc{@^gJx=JrrE-@*_qdsjFV=z'
        b')65Q<X{VV^n%PD(Z_vzZ8V;1xYG+(Z%7xUDNOQ4uYP$C$1MO2&uC&P>Nhn`WIgLFbTE3ckDRyF9hMIXvO}(f;f=l7>#o^UL3*}sE'
        b'voKCg5Z3F8viF2^fne08z5~Ut3f4ss3q|^dvkP<djMGTHAuBN%p=2(0Fw~nR0vX6)`U9Ngt^8iC)=L-D)N2-|(avn1A8cnD*x`&-'
        b'Fs&rdNVQ6>Mgk&?RwL8$aNB@AmvqEy<6mc|EF-hImufK{99+5!C+-&vmWa!jml93_gK7-D6y%EIxR`C`jY#P(rV~!OUxbsmk?M3Y'
        b'?Gnj($*CWVLQG=)!MF*tZpDlr;1z`4Q2Tv+kXMb763v?!lutS;2+X*ze`z;P+#>?DkwR(Ns{$0rw^Z!wKiwv7Ylalk63f2+H9J3z'
        b'&suXQdZZp7)ZC1F!$lQTt*C89o1h=Pi5RURRk*UAee$sD;a*qKGn_LYaK7Y6oalRJFE_f{*CI4BtuAJ>i+W8HiR`0MTwZJq$0|O+'
        b'yQV}${y6uyk+!Ar)1}^Crq;eRqE^nYm@)~pwL{K}&$29ysEBr0qU-xh#8oRQ_WfuJDlfJ$n=1+QXbkhGH;$&)7?(yEqa78|_0N_V'
        b'y+4)`piDcp*~Pqer1G=s>LO?iQlt45QcC=e3XR_SiVro$Q_vXD5<4V8B;3(xRiln%3FeS>#{K<EA>RH}=%QNhDJO*x5w*Pzwgf4t'
        b'#ex*nwZDG{C`elyj(gYm6=dxf1{4&;D#%J)Uq8S0*@Vv%UDRvnH6Q`q+=*E}z<cEpkr(D}j;vfdb(-|ZVW!qq8qplfx5$yK`(k<V'
        b'T6<}P1)^tGH}znrf3yk8i$O8aFHlm#D4&ETNt9M&EJb<&Jys#T*oc+i7M13Ls9nr!&?UVKeHeC<Y8-q-e5&MhiMX!>E*XO`=?c(_'
        b'k!pb?z25$P-5(jL&6<3l(P`4$ja5LWAx=^)gI;m@GPtStz5eoLy;SQ-xbI*u)A~Gll4*gH`?^1@y&Jb`eepO1&DKhxD25Ev-0vf;'
        b'#2rY_MrUb7Ft)T-D6O-@fN)_j^yU!|TS3d9PU>6+*DTOVFf3ca_(c*Hs-XznXQsg$?~5nw@T*P+BTN(P(^Iv3Hs!m<_tRomPY8>Y'
        b'5vZS_k8HaN4!h=kN$yHNbDVSRI5b2%uI2Q-hu+8MqlHk~Ynq>dJ$g;LIKNQ{8K@zHDDNc9(i1`-#VhED$nWQ7My|@2-zR;+!qlpb'
        b'5t)+-nr3ypVlpp&w$d0uQ?Dqg-}UE-Q~cH%?8m~wSiVg51hfi!2OsW$2E6<RHZ{~0>a0A*p=X=uV>k+7^dwGBFfy+xnMRs%FUM!$'
        b'i*O<%2qcc=>sXofRD+SK%^$+8N^H;8rLJ*Maj<W3G0AvAs29w#s{rayl@6kV#Cy3~&Y2H6Uj`rhu<rl_x&~jeupmNBy+-t4tmw0s'
        b'Hi{qzFlBMkUMUukT}el*eBrr7U1CV&_iG=Id|@f5zzQm;Fh;D14hWPK&5K`kNdqOU2EIqNfbz@BR79b~+l*cRj?v_r-$8qUSeeB!'
        b'l27hl>Jp7eWL<`hio=S5nlqSKjuI~&!Zp*dJxi9l?ifj~v|~j1P2|`3l=Yak=xW))7rCt6^CMS{2(33p<X^Ad{Zjv!j0a>kB~JF1'
        b'VeB2(Z+ECDssa+Db_fUOYR~GiV&ItdCe1jc@+pOwdbIz7Ai~i`ob*2-heCn+@6F_Zd_dl**q$f+^=C(5G7i<pVDP~Z+=bfhINNR{'
        b'E5@<E^t}i5p9<X&b;8@Oeh^fK-Bxgu`lBk`toq5g;ui^O=Czt=%=@cgg`$WIC3y<<dY!Ha1WC*D#2--~!;Kkw;siuNMhb>rZBog9'
        b'?fE3%6$aIXYR1X4p#Q3wHa+vYcOIs96+jCv473?YeuVQSaqLK+myIUx_MsQRdPOjYfy~e3w~9tI=1qa@LFgkmObL<<o<Dz99X8w%'
        b'>i2=X(=ofN0Mge7@;`Ho^QG|EvA#Z(yO!e)_sNCH5j4}LWL~$%vWk5?zcFmYu3gH>N@1WS`a^b<uYN8ujUDBSBUk6kGgw1sG)63q'
        b'8X2=umyL42o%`MqYQrHX$d9Jll+^11tEZZ16(WD;y7#j;U(#6x^IG~{*+%MhJ=I33bqNpVq-jD9;U~E5{JlJLE?VaJqH6TF4*hP5'
        b'2=Dn=J20qqQEgq+>*jgr<dJL~?Q!X)+745%x08GCFlXejZzB+B#s#`l{QF>BU%od-Nwv(Y0FN=r#ZQmVLEbIZKyUePh^9z_Ox80E'
        b'M#c?3ocD9ck6M*&r(Uncg`jn?&ukV6vK%$aLdm!?U3~LhITprc_h(TTLMD>95;=ekmyGv^d>E)L^p?NMo(P#2I;A!TdA=Xuso=gf'
        b'(6e=V=hO7tuRXk4HfI&>#APKi3)QHeonwS7oQv1Eeh%JV*M5%qV;$@KxeUj6;91Y(!YDuwm<tJ_OMuZ-V+?-3nrb8`Ockb0UImlS'
        b'x-NR(&P765?kb(^i7$GQljHWHwy`u+SD9T%Mi=`e&`!DRjGN$Lq!G^2Oe6TzZ~#&$p?(dRY_g1II%w*3CDnEW=TP@&tEt!HKafQ!'
        b'^h_6cuPEoPd10A%;)D+T=LLN|?cBY1@zX&)E3^Y2>CAC+q2fJHXa}CqP8Fh;hO?3!Od-S6%ti~<qIWXshjjVjc=|z|o@#{Zh+gO^'
        b'(+(Wcp?yadrrXZ!G*3dA%n~`{Wah(uMKqfSbnHhSPl(!aw3&E3N^+8Fwo^M#Edl3FT4>Zlh|;ZRwoVn!5-k_R2qJrOwF7#s2)qh7'
        b'z0=&IW22aExW&-+ea~F&Kqp(Mc@MfU3>_^~JFwY*>P>XYAmq_hbC5Ab&r~aU<5T%)rCSZ^uNKiXQ*DIaF8NC7<>;L%u%G!gxRNJS'
        b'sxboTS*^yTH0X9Je_=@~k7l;Y?(-a3bx}!eMS)79N69o3Q?Yr)s1@(ezf&+TkGwa(mLttDy3&erOcs|;&){~~0#lBuPz;@-KBtg#'
        b'fp>^|0+0Tf4;^FPlliq0=*vMvAy6L+<ucJ8h@XgXe;dy$$u3-48)F0?%iDk43h~gucr9uvvq|TF_opOH<AEkoQya7MdIZ`5f&cQ8'
        b'Y;&CliD58H)oPGjjn?c_xll~L@(b_ZeDfZssf|gsw32F^GC5@B`$@D&O*Ln_aLvP*HxFjH7X3RH^-PPGgUwr<REulU!I-v)l=>}y'
        b')fqyH(w<N<8|O)uZsh$lBQ5O-7_P>nxLT7GzxBu}OzGsv5<P0?RIo6{58-q&X-{%7v@0nt)~wN0I2U`-I^`^$X?7P_^E5T3%kT^?'
        b'5NGF|&J*i$JtCw29fe+lB~AGd4dUL5>bDh2mrCzSf(A)RS-21dX=;#+R?mj`aXvR+d77O&)UKqio{;Q&=G}P@y<%c;Do$%u+4s=B'
        b'T;*E|sTy=ZyE5Y_CDkm80zK~l!^SiYPlh0~A!vyZI<k@4Ql6)08o_g=U-!x65ba_LrA*0mklaPwsazr%wMzpuceR3-mMCiqohZpA'
        b'^wbukvt*$%1!B`i@Wj!4@D_ykTkKS$G&!YC=`69s$YfeHVVK&v6beD+i)mCdE#=0bp}VZ(Ak$_gwFNFJ>P&X_%5Z43tjuHda=^vc'
        b'puVVgmcTuzML>8cj|_*RP~Zwv+$Ky{7(#NBCZ;dq4u{IXeoomGW1-s9XpdUJS+`nhljd2Nb^=tE=tZ{P>9bSqYH;T_d;kGy${es?'
        b'MH!Z=)ogwpMyd;};X#R}mIwMDnNUeWv!3UlQ1gdzO#=9F`7Ux~PL<=}dR%9&({k9)J+xkw3yq`x1Gw*^G4A`-{`-vE_TT+|;KuH|'
        b'99L3rsBpyt393-<c8qlqGKX=i4BI?C-z6LoN3(iV7;p)WvCfdtyBfo;u6yIvb#K9~HQ1%<U(f#u)E{au#}^h7HdL3T!#JS;-z=Z?'
        b'%>t@Lg56NJ(Hs8P=vJx6yhTWoTF~mW+wCOoHGV<7cV89bSttEx<xpeZdq=C!)_|@4h`-2sil|!<Y>bM0WT^ggqwQdU>X+uXpmu<w'
        b'<6==e_+64~*PrjN|BA_cr8DZP`ggH?<e}T@;}DU0qyA}RqtFr=I42f=6#5xXOvm>8X(=0jvvorO9SXo*t^z2iZKP>F;(RGO_EF!v'
        b'TJ{aeL(4CY2}7@rLnE&rho)SLLr2HLEkvS3Gg^wfc`Qo2IueUUOEy6)DjbQ*yuZ9gD5_Z&2t`rvd}3@27m8`hZXCn87hP0FVBTL~'
        b'|F&3Ep*ZU;y=e>=idla#8jBKF%7J5=q#Mf-opTXlQ3wLDt718j<0>(dZa<a-U&?#mEySYMsqA_Hc_|QuF?Pc^w0O?NE8<Ymm^k$6'
        b'%Fnp%Hn_Dol;j)zZbC^2j4cw^%)-&S)>wO&d;@!jS_C>&vR{~hy_=nXsUg7L`QuB!EK4uh3lyr|#NH+2P=SR7D!;v8Z@7^xP(kA{'
        b'JQXcjRUilLX_Btc<S>7lFRPPT;1}PHVyx{J@IJUW>UXt!HsoKjA99?A$RzG2_9ONpdJy6A%C4HDt{gj8uHW6*HU?}vR3Vn{72Mo7'
        b'LP9W&ep}2g-?5?CG#BNP^~$=On0e)VHe7KVDfht$>jJQ*E|RB60e2rfGxu_y_vh##0i-AS=2tarT5!zV%lWhTL^ggcgR4oz_Pp(1'
        b'_8T?0P}LjjOEO|_tuOy)?5%aht=U`aa=*2mB6)kPwFSd^wYBvw^V_MPXm5%CfW6hIZo%GyQ#RJ#F1Ss5d;Wso-d<^Kt&?tOu&!C9'
        b'pS<oz^2t!|1kUZ++pjLLCd&E`-@nP;5+C|*!QNW`=)-b4=INR35Ro(O^N>9n8DHL?GQI{c{IB<CVpxAhG{&E~*4p~A>#eOrx4qc_'
        b'>%Ra43^^13xBZ#7FI?fz+_D_knOpvY{!I6U|0Vv6Zn8{5<22O}WQ+vOTc{TBKENeNC5&pFMV*7zI@!lrmpMMPfANP5s?g}w%xiX-'
        b'OoL-8(8z2+FcX_dH(N$ZNI{x)y(#U9gHKqfMw4c}WQimu^dWmgbwr)|z>*SLKxCn3?`p~=ih?;>QOr@uqAZk4k(f^RDirt0bh+tt'
        b'7N%P)Gt^w5d;7@=vc>C*WKT#=PJ~JZeU5ALF!kFPQ*k;2Q-hz8gB^c?v?nRU*r}eQd`qEj_?uGwx9m9Y91KIx_Z!qqGrb8@H=NB*'
        b'm&Jszm>Cp5OSnkX^XlAz=^3JocJ5w2WM+2HW!D{>U406v&6R;!m}ZHRZ>QSH@QPr}@Fb>o1}9DD{D!aI!pY7g3A>Y%R<mkNumY{B'
        b')y9DscB-?B+E$Gao9Y8H3*<Rf!{*s;WSZ3i&eAX*dUo30^Xs_-61H6P<65+Ux$RqWL(*2<d(=nVh1m}*u`@23a;d59XaUoukWG(^'
        b'qHzo<YC6(SS~N$Yl<5|vLvtF`7l;rT6Ah*>T%d)N>_@A4>bIA$OH8iKWi-=BH&m;SaZ>pav_9i+bnjxw(aMDzszVY@%D0xN(ZZFB'
        b'Za52SiK9q<8tpMs$k~BgXYsA$(E3TsL5cSa&h}G|QEei*&|k@5^jI{MM(gVC<t&6ZHJDw-2EoC8&mtBPQ$c-=P%HH@yt*b=&C}bN'
        b'j&;+~<K+%8>||70R*0JElB~w;REPZl?mw+|u4d0~H7p3WQ=3mx9fMj=WbklUDnVg~DQDNaA-&5n`*P0C?q^z>*2sEY)BRgRA`aS_'
        b'oyE@)c53Ik2=5`>)$qwlm>b?uzkS-pIH4MrV|Xv+e7a@r=I(Ckik`dYX2!l@r<~8UXeaH;I1sGuhGdW-r0jJ?_4WC4Eq;nv7opjO'
        b's~bK61!SWwDKO~NAL11}y<`Os?svJ271T>@=E`6)ylTZWTc6%kISKx68eSt<3!*x~JYfDjJ$)vBrqPcPk~qw}3AZ$yHJME)PpV5Y'
        b'3Do86auunmmv*7t<W+%fF>tpuqjHj(d9mUcKD;`Z&6XYWSLEydC7bVyWAoh_^Evu1GpN`?ZLZF`byd1c{Hi3LyQwM<X5We`-3+MG'
        b'y7V$tQjL*<>JrbeBvm6r`vX9oeIYx^%E;Co+UBO!W2<Cgy4{Ni3)KznVZiMTpB#pu>s6!oG$;dVSMe9Ti*jZ)ul;Sy4rxYbbM{g>'
        b'NbJ-$mxZ^L>=cykfMiXp?}GXSb`rhkE<p8}jp_qUnvIl-Ix9p-$MDh}Yd%p!?c~jR$_XQ{yi7`0^6Ms+?TBq2wgj!s(=$%uH0MhF'
        b'=d$|07gsi%RV0`+&v3xRs-4AaqHymDPEYvkf$-UZCuFO$(a3KbPyIR@6c-yzhQ^h|PLem5?U2%_i0e0U^n6r^bz-0pv<r*ch>Q>|'
        b'V4pPLL?6daZK0``jFhvUM!UDD7cJDAAOKM(p_vy^{Y#8ce*yaJBFg$*6MCRUHMuj{`d{RXW)1m9@<ma@p-Ssk4)`|vLiA;viX|fD'
        b'5@FM-@G-43G@CG_tTZ-!0<|qKr+ZIB0ib>;K>ZQEwiIME&(2QXR2lsAR%zmt=xyF995uDEDGc{&F=|$}8g#&8br5z*2ZFUQ0G!q!'
        b'3~d3^k8A<+ykm-<MHtGTG&Y<qVoXL>emm6+)?OAXE7I|xbLnWA@+b}iNz%*E)E20SOfQQK&!%JFlsDRuF6soajl&jVEqYHro4;{1'
        b'f3GPz3G)9H8bp*yNo_pxH}DRMWEHYVzD9_?>r!}U<#ugT)9T9<kVqKfmeFiqii=ggb^7^0(ETz$JFBTK$hKXYv6fDX{)6hyszlYu'
        b'?W2QZXd39R6mAEN#oePs=D%5mYeUg<Nz{_f)=cP3%_jBirm$J%OUibXHrv^rDJ`iC)=nyG9<~boT?WZ>#h$t7IFQE(@*wN%B#EMo'
        b'+%&Z(QZO7g)A}>)ig8!g++@A`@^Kd(gT|d9<-bNo9T<YKqps9H>PkBMw3+fQ&~{m~HoPrkr$Eb&I;(Wds4J!jLtEjPF$WV5G+kU2'
        b'oN6w?t+^Pn5L-7}l!%@I!Q3gzLyrdAL0BWT%|dmS1skcCz`{Zg2DQ8hxk%yg#flH{VXFvwJlnO=L)1|bLJpdSCJ}~(dgvHwHosML'
        b'AzhZ4V0xF8cwl}nS~|N)G7IcDl=JLU70gQ&)Qhpf(iLTsDqz5@31U?XxsK6Gh*;(hBMhhJT{33vWYD7}xsY9CaM4mQYRSai7&5e='
        b'Tfd=gWeu(Lazh&(f()%;VHW5!`}bhbx-Pe|ds>i<eO$XV_D$BtmQ89aIS^dd-GyxI*e>W65r*@#p(AIPu%oZtD8R~T-LDdKC7zn5'
        b'Q;J_DDBwVH%Fgz#Y?Xpu482=VHG|&>O%PP_AT*tl+G3=(sKS*<7jKp)Dw&s*)QfcjDIC2By>WPzklmO`2m<}gGCFYfn~J%F;n+-j'
        b'!`bSWP5!2Z+;!7Uve_OeNioBdmN>g<Lb{%M$-?gcj1?@L>^D%Va4F5&CV@Zqpey_E&;`CB?mpI&1EWCVvcz1-8-~6t+M}R7k^JG%'
        b'1nXLMZ|A;{!b#6;Rc&foHEFDNe&8D-lzt0URBpPaiHgu(GEqBXCp}BYLN<_WcolAa0#&H*UB9IqI?Fd?Ple&Cgy9OBae9}5W9dwW'
        b'>7sdUl(a;eNQMnZ3&5WV`V6<u!~A1aUB<DLVbF0wl^|Nvs)?5d#sT*~pnh^!!`U`UNxg~M0EaeEQ(H#bKpQ&J25V{7_+C<d-~OS$'
        b'^9?Ccp!s?V+P3G{=>yNF`==V^+dlIbS?o7NcyMpU2RNwTI7P^Mtj+p&d{Eo0`aDG17Q*0POAlKS8UopaqDIZr5XgHsxQTHT0TXp3'
        b'F+5?K_by}$jYf{8Sfnl%USSSTLVctatUY`7IWUJ)gCIiEAID$r$;xuq;kIpH4l9yk_NYR^9B$LPrv^2xo&tq}ed#;o{n&^3CtmHu'
        b'N`Bc6RddrSp}#-$9k3qrxm=lT2}nOXjMNTQDCh|!8_^T1rQuaUYoSB=$Lv@|6@SP#w26_TUbdsDqhZR)NF}vdO?Bw0H_|5O#^u4x'
        b'sb}7hoDo>%82kKivxVx2<e6eT!=d+U&iark@`gNvtnN0Idw7+9s`mQlkxMqmeHhwPq-^*Es;0;@fy02h9O&Q(p6o8&CQW?o`K&2X'
        b'ozMeS?%42h`WZp&Ht1)>ao^aE?>S(KevdENbxt!0Be@`$l5&4Bdt?|8?z5N8jeYMFzspBo${L4i-bK0LoPU}$Peok-y0XS`7Q;Zq'
        b'&Bz>H>VEr&_VKMejNO;uURMXF_6D0}=pH52q^91WClD*Yk;U+2v)8McH>`Icy}X7Vfi)Sa+NCYH_3vlBU!1j5ufb30&ZVum=H7GG'
        b'Y3I~bBSea1Xbcb6JpQ9*{f{*DM&Nt#+$@&SQM@HHXJ(DO?~}pI7c$wG)uR`snA6dPBPrO*?<+Yr&N{p@@WOpaCsWIm&7IM|<<U+o'
        b'b24sSfLU4|G%YaozaU;{>$kz5!2+>jx@VzHp`>0;&PcH-Th^ycug>jKJdmKvqjZTLIMw<GIF;zC-q4lyi-hWPl+Nc-B&Da=1|JZg'
        b'|E9W@($#t3FvT~h64$REftSe%gFbQf2G1hAI(OCSvz|hZu`lg(?s{#++EZoXw2rVsN<R*p*PeC%pEpj*E<GqZIPDOA@R`(Yhq#&1'
        b'oI`k@Mw9`AXP##1M(_<ZQVcsv6>y%uyJOL+(;tWzp75Lyf0%GcK=L&hR(|kkf)u@O;8@APA2W^KACHxk5-XxV&G~cY+~d0EyPjR7'
        b'(^LKbo$zR$r~gT@F5jbD<k4k#j)Y;)WjuYaXhna%7%pYcu_EC8hozf-$e!1;FSFng&)b%)2TR4-^A=`k|Lf#?k)KM?_p7p=O+H12'
        b'CPkr_OvMWQADTe##=$bpf6W~8uACn==Hp|2o2$`}A<pQ#bAI%h*P>Hy42!<t3%nz`2P-!5I{%pI%w}H%^K0HLVNQSM@$=NXndyfz'
        b'TXD*P{v60`;cLP1F<a8nOKkYwV^}x;3sDQ-{Off82NZUup%;$qYRAoHR7NZR;Cb}kF7ub@ydnF7<~<C3eEIL_r=E+Yx~6Qzm2Yt>'
        b';LuC=gyn3_Tw1G?F7A9Y^8|i~-%hyW`NI*o*MmKsW7&6MyA3CPk3CybL13xFOYg+JyRdr_Q4EK5HfPEX%XIIs-@}V#?|Bm|%`ti}'
        b'YzK?k35W52E>ARau@yChG;!q*1dhe;ASbP;;nXKq^xWN9muYljG{bp@a{)iuBRhfj_R#HIJ3|_CLX0`%qoeqa9`pv5-(fCsNS9db'
        b'sS-PF9+!ChpbbI8uZuf&dC=cBkEcz{{C8%Xt=eWOBnomWS1(L-fpiCQ%$c?I)1>P=S7x>cBjM_LhVF)3n<5fga=Q91e7iQbt<DvU'
        b'rG8!;!9`Q-J&9f+*7=xU5!~oVep5t{BgcN=!uHBAIgz|NRzfYwRN<5|ljN#!;%Tf<QjimWbYUXsb<IX3<@Xwpa;L?~solt_O4K{C'
        b'&R=BebHw_b5Pi;g5Ejl{E^lQ|VUBwu-v*)v7p!LTGRyP4!I)7TQUMYh#6@`?BS@TwUazrK{OD62^p}PE%kxZmmcp|IIV7<#F@E3L'
        b'1y;1rg<}DIJ5c+=f!#U3*71<NC%iK~Gge&3mK%Y}jYQ=}kAqTUQgDq1>k^M6cZq&mU46E87p_r*!tW5(!>{dyxc7d{E+)4>gIiNE'
        b'%N%Uy#MbD#8Md6NRT>F;B}dylZL@<XO*A=V<Yt)L+PQT-<|(Kj+R|M)q@yRv5jXGs<AgFpKqjiDlao~$WeZrJT$vF?zNy+oPEc(H'
        b'Wxnm_P@K-Q_BmMV405tEM-28oCq$Vu9xmtD1z7wyNp*KAq2r9pY!}3eRb$j>VaQ?*NMjd=xIk?xado1{4r)t;1Cys->}>U*zjYqO'
        b'|0kN1#k}Mk{X3B<$uTg@yL>HSL$CXiS5seVRJi=C|IO@+S5e)XGXFcchCDvR&A#o6?(q-a|3P+gv*v1cvPE-=oov!vgPrWx{J+Ld'
        b'c4>Y(JGn{o|Fe_-ci74I@4ppx^1%K7x7kTd^Z#vj(xpbv@&oK-@dTbL4ny!{<NfSX{U#T)MPkF`r3aPm0=MrxwQvqZ%TwxtX=;<4'
        b'-9m*?`E!(TYCQx{n{0Bl+RekLTz@hFB%^6A&A7T;84wzFylHYdIngJ_LnK4XCk34xM~4%&Cj~CK#GE;Y1u|XqBqGVkr(=1B!`v>)'
        b'h1Q%e;*tn16vDpMa~!zdwf=W|&P2CB&gz~J7qzitt7+xA;^X5XSkdeep<U#ZE7GM5CuEaDO6;>~M^MdSE?cUo_HS&F_pn7G1}g*Z'
        b'-?h_ybo^oJm6Oz~XQ<!xQjPx7qrb#m%p2Zjl;g^?T`Uo*W-@X<pOyaEED}$dIR*)>r5Oj!H2b*$mIvK7h6mj~%7f~uRz2Fg-gqSs'
        b'iXIeA_DE>NfkIprciD<}a4cH$)?cyaefgTDYseCe)-3-E0in7alb;BUD;WVot#hvcLJa{R)I9=(vhR7lHV>LQ=XyM7+7&$LS6r3{'
        b'-EJ1&e~AbEl6x~A)NqLh^<K$?YE-w&gWe^opd457pz{##Sac=tIApmU9@Oz4=0OeD<U!q6@u1dox5tBiAPgvI3=eu8{X9B`2W2%w'
        b'gkM2}DiICpU=hzCi`>6Q;3hn%9|+|eN7>Qq@u2R@cu@CP9@PDB;z3`$H6D}@UXus)Ude-E*cc+zEBEOs$DY;smv}Uq<>^=+^x?xU'
        b'-L-g7cfn8KK^^}I9@H?(gSu&^DS#AduHr!*hzCu)4iEZpV6%hn8k-%oqdaKuPuREOxb1x_nwDGJw{jCE^x?7lR&=+(gx)|0L&;Y#'
        b'p*P>Z>bR}_tN(*c=ncduj{gZvsN+A(gg!iW?~3m7y(==`?eAT2{Lk-Q8D&DP&)<LvH4uLpVL}}@U_$3(de_4NCRBGd6B;ePJ`*}~'
        b'gb5|2*Jna!V0PETfi1zhtC`Sf(O4!lZiESyT!RUv(Oh~RDpbRoJC^FaG}iy!Txjjg02jI^Jz>9kEEjr6eK{A}rw(wT56v7{I5Y6n'
        b'+pE4N7y5hkHMmg2%SY4!F0>JGp?^{%&;2Scv<X}}KNoso=9OHi0qPjwLK_hm`i|PqQ;p?9-7FW{bR8~KcNrJD;2K=0TRl5(gbSS)'
        b';6fi#`}YhR>UoIr8^eWeg9yPLgU?h`?(1QpcI4|c!8{v)LP5Yr@Km5LHrnC5p9yWE88^#>Hh~1!W<qz)yde`>;AcXk|IF<<lQLjX'
        b'o87613H?XPz&}#_Oz6YvQ6{t|z=S@fMoj3FYCYwK>WE(G`6Oi^OFf1O-H<xUgw9t7n9zCZ%b3ur)LURe-%A-dlrqYMrm8PvLcJ*i'
        b'@ob^yBz1rZ?M)e&;y-n-`rpWeHu{-RtDgyV--rn<xS9zadH^D;#w(f7Mn4m3^)sQ3S2Ce%QwFM1Sm^Vg>0_DD8Z}juo!7G}Wnh*6'
        b'^6B)OGNBlTsL-0E+R2Cq6)P$Cl*s`q)cX*o8AFAlopLM|YE8Qe3$3{}7P=TCC&&^#@qfAu3N7+Op*`vUIur_l+W!y}>K?;{x&ut8'
        b'`+7{MW`qfKUyliOU(STON10IfRZOV+x=g71awgP$i3xRI#e}*qV?x!438m0hJ#5OR=&PwvF9-Bxy$lLH5`aS80Vvcx1_~t{W1vt2'
        b'Ne~<SP^cq+7$>d`g<f;A^YebiuiO^zmw4Mgyfxs!U&rqo%gfE@vQ(&M$Mu-d7e-|XFrm6Hh29sg#e{CUCKFnVU8?>qGNF|LCe(Tz'
        b'CiDiXbz6S|6Y98i-sU!$P{z;N)?S})y@4!4&-`Rr{&QUD!(+Kn-DO<p(DI+ah2Bd2e<~MBU&VzwZpei`9N;K)S9286ML(GfP5x=|'
        b'C=qx=(RJ>*RgU7ScyxrLVB7Z^9L0^|(Vt(uZH~h6Z{jHY(I}#=Hu&3eBpUT5Vc1RL(b*SopQE_lc=TW4C~gpox|1&c)L8Tu8IXU0'
        b'3w2zJ3%yPdh)mv4-0gFrj(;;3x*))X<}oWDxQq+k=I26@lv}T$LK`*r+}L^)N3v9CqlUW1JbHaD^fqieRN_{-(8kNSPy-u_O><F='
        b'0WS1g|Kfd<k!lKXp^X796uh&hOI&Cp$v5Ab>}N>zaN*iqC^EQS<#o8V8`<078*`yIdmo(RHs1$FJbg<{=p)xz`}5xB+F$5R*Z!h^'
        b'V41a|f2Xb0q}&P<nsA9(Q(VogCEr*K_ZKX)cJIH{*8Zzp=#A{{;FVnHtu9^O>Kg2AaG?eF>zQqc3(dP9*`v|%mG~3J*Zcn(7wY(b'
        b'iwnK3KXW}U^hW+n?}h(0{>;s|&>Q(P+b{gz^=H~{j|)xwDQoLD8jrWcg)XqD^KQz88dxsWeG6Qu`$k-7BjQ3EN4U_&pT>nY{$wt+'
        b'k>x_~oHg*qj1exh(fqSn{~{OK$a10EFL9xb=H{epa-rX+4ph%zxzI0DuFZuu(p00G+J+V}8!vI8jkm#tf+N$2xKQ`iTxjFvTqt_m'
        b'Aj^d|j&h;M*@0Wfa-rW`g9|kvF4S!Y$LMk{v~dg<>K?;|8vbousB4r9Eei5;q5U_789k{tgBjU9Iu8Y{i_q-778hz5;X+GphYMx5'
        b'-WY<=UY6!-a-mCp8W)Q4b?exCU%rwHwO+x6&O%Q5O?By>8_?zRH`V1Mx1>wA2I;c=axl~#07GXY-sIX`sB4r9RR{UG(88N?q1x0N'
        b'aG@?g7di{7W7XV<3v~y$(8g<Wq2F+>)PFLo|AY}P^w}|7=+m4Y`}6_(^uQCci!;&4KQ^9{rQQY?%61+lD#RK-mJ6-9j0-*V6S+{A'
        b'JD#mS2fvyNoo?N66&D&YrgetosBORD+>i|YWacI8>P?ND1Gcy(fQJ5M<~7mKAQlbve;k0NUtE4NbchNv2%j25hSpq{3^f{WM27O#'
        b'%B{pG7wQUdp^-s`xJO60(3+cYp#cSi2N_OXlM8L0c@r)aWiS*LWH>*D3kCDv3<4uG6wzTH;0O)Xj-sI{W6;pXOK9jAe$kH>x%^z{'
        b'c#voDZF8Zc<1Si+#+~8(O}WrzGjG6!`bS+c5o9P|co`Skc&l9K_S@z{T>&oiB4LQg9m9n-{wrLlYm^K9fiSeq|A}1asGW^I$8w<&'
        b'+8c7A6KCFl3-#yaK1~>QW!wrE+IWczt+^#G6uP1`u}+|5UWBfQn7d2g?68auoc*Ta&j>?(>KHDxaSRt)Gs1<=xjq-FK7u3L7swsE'
        b'q940Yg1)c8hSrQ_Lw|EkHq@`7;=e%sZo-D{PPslC`qUUU)aCw=F!Wu<hCXrwHgvw94Q<p;stks%3sNCveu$62p?(RA|3nz7ZU%?y'
        b'{r7%=U&e>J{MchZVR-fuANs9w;GFUjAG##vT6}2Zt?{9(JJbjDyEQ&Epz(cBpKJ1=Ov-KWp^Z1=Ly@fvHBvkL#_|e8RKOyl0oHho'
        b'vfO)#TVq7K1lB26F`_BgU_`HFD57@|hU@?!nv!=7KJ>1XDN)<5;zLjP#&&+s0h7CnkeolKi5THSo4%Ml%7-?by=;c;duM11f%wqz'
        b'hz@P?)1l>zxk=@RLy3)N5gU5Y$Yx~?zH+|UOh{5LdbyCMX&w5m&|chJt6~|^tM;l_tJuBj3(!XM&Y`bK7B_x_4i8|Y>(|?vH`r&^'
        b'V?a{J(iU8E;;i*Aevs6`f~3};o%71hq4>-_f|6QGezaNxC@Eq=wVXn+k-^Q6pfZngJ`;aW?Zppq-PncEZx7<=lf)mQ&;R9UER!ec'
        b'nN$m-vP=jfgDp9kwpDf}#=^*LjYejcg^9B`O%VmIcM2>FZDFD-nEOK+Stt`_E=BntrczH*v(8ZWcR5XmcoDnN%in&SFRVF*!HIS}'
        b'Vt4W2cPr00)$3`oW}aXTE&!dFXc?VLxTyQ4^33y8esB_TlWKJA%$7;2FiRX^kYmN)e`mg5wPrm(IgCI|V=8+bg#uJ_3LJBir-LA-'
        b'tjQ+R*`&{AXMQFi9hEqN*4C$##&*B|ib(xdMy3>fia7!0P4cwwt0xeaEgzXOLe#kg{GO0CTgydXgSMI2Pco|~^9)NkD3Qwqi7YN`'
        b'O<0iPO<6nce)xOz;pQ~nx<8S4>|}YaOjZ=T*bDyNohLb2x!TEDvq^l)hERWvR+I+M!~I`*UU|m<o##b()@-?&Br{z&aX%)?7~CK}'
        b'{8m`~)QWe)>T7LyOR&^tD(_vBvi!@S3#9FixhG5=XNz`QOr~>vyNhg=4(GWxTg$kPj<ZhZ+4JW+ws^iDXY!mo-Ej`2H?8$JI}&!;'
        b'Os5mzDrOTqTV$={=6?0(u5Gs9by;XDk0`@_;K$k|zIG1s8EnCl{TDSq`Y;TH)465E*_@gP!sz96y%VN<D~u!^qNChu=h=SK*}gVY'
        b'o2S43T(#+3zs=*UPN=t;JR`-}WR;@1iF0=+bsZXv630zR#@8)oHx5C0bnlN-P<g1ml5xpfsJuhORMOAIa-K0Ko1e#(j3l|X>|<?u'
        b'VGd2j9)CYlXx^BBK-SuW^#gL%Az_#E6!CjZ6`_h#2~{b{wcXrT)|O5nCt#8^EU}?Xs=DXVX4%jgEV-5>%D6{{Fmi$lr#cdJbVzKD'
        b'7sC*%nVduYI76WhnX*ByrsUK_RcU%GFFj1Ph^xp5Daw!?3?t6q#J6bSg9=tzs5mQ$Wu+J7^!zGe;E{xO9$Nee)iV>!$Ix?*<9&Kc'
        b'&R{As6jH|W%Q_E+Yfj-5M-?m3e1;=GG4wDs;Y<%N<YO7stvHX<+MtMXzj8R?yJR~xf%!hUIx(auSEk&|Nuf!unhI4i;ocA|ODyNa'
        b'^TEg4q|8>Arl+|*SVS7u)R5^8OG_(q^@d_$Y1r%rOqf>WeA&54X8sn{CSfR<44*IDl`Deb8QwEHVc=vks<HVSCECI^m^?6;Z2p=('
        b'{%i8UUz5#Wpkwr*^F<<a3(BGAqvU~)lFgqfM|P&6yZ`1-)$x$b{5v*Le8NC{LMx-&CQE~&YtgwQ^_&*Qe|U&@f^V)tN9(d3jHs@T'
        b'A;Suo$i-^r&iurC6W&hlpCisr?467qp3HGkp<UDjvz5)F4-@5)L?L5j?$p3oA_W%a&SbG{vPWbmxpf1oo}^YGyOoOMsd}^n1xyW}'
        b'Q#wEj7M7F^=oztv3GwnUM~|E#d9pf>Oi@(VqhvzVjJV)q(oRmuS3cQPOz7YFvG8M(Tl#U#eGd+6!bw5p*D)~(E6<RVV$HFS)qNca'
        b's*`vpVFe$@%#o0ivae(E;#Pi723MLZAB&{za4i%gLu0?TnTNwu$w_tQy2qvl!)f9U3~T|M&SJ>WstoA{EnJbs=E5Wj=RYp^c;#8u'
        b'*IKg{GSM><^db6EbJ=54iGo@%Jrl_cI3wM?bK>a?vGMJ&?ukpgPPYd|@5Nd>51t=*IvM(YLt8^>vN?J>Xi8pd>vTL;iIbm@p|x8P'
        b'lP*gPk$jUVXPQDEmC2^}E5)S@Ri2ze7fq+oK2?&=T>Jo4nhfgRZ#ilQl`9m}&E-hzt?4^+NF{`}L5nBuCyq*>MWJ2IrKruN^nBqW'
        b'ks^UwTVlm9rXbm{>OxC;cMjXa3(?))Ft8sCNlU`{rnI6o-Sqxqan3wcPI=yb{?Un0Qd$OOUZ4z=l#`iE5@-ik(2|h-{KL^4x|d^~'
        b'kFF{f%hJ-RwRwi=7uRWA46lpf+o?MxWjuE9RVxOjLRUsL`zKl>JaP(8er)slQuD9`CtiXo^sG?~B(R-bx!-3_9w|>sXPK?+cUF^`'
        b'tjECk{{!8<KmBNqc^W$oo>dG)C7a{WF*P~)OW`hBc1C81;`cnR7?6P+ye^7=l9AF(q?uN-`!l5{@I&KV%w1hfg!zPjz49(Q6#*BT'
        b'B5*>(NuUxAjZ+*}v<vnIoBL6MnuwnhC13@k`t@Rpm+bg@A-x|z8Y-zH8x|@$|BwXvpMm^|WPko=sK`U(PXASACQyN;oh~M<Jfn-5'
        b'sAeX0=d`5LUXFQB68ntxF7xiBz(8$Dhl-kiNbuLEmkP7&R~)7$S~M7HLh~DJJ$5Z?xL?uvQ4-sJU!k;+5K@_&*vox)8>vZCYH)7~'
        b')-zo(a3aY?g>_LAm*eJ7P}-hpih-j^P#dTVYZv~S5YV#bL*L%<=8w?Nf=+*e>}XV1vmIr;TxfpzQa!tKj9!KLkN$g&b1-P6ynH)j'
        b'p+r3r#lXryp=olH`JIF@H<>L-?7nGSlM|?QgGkZ&Xi_TQyyvoXkF&C5W13)WDo>;~^00i#IpPTphOYKpoHo#$WbPQLx%UGf_-vs{'
        b'YC>$fDhGz{$z%@N^qGa#a6_rOr2gsR6dG+4uX~xMBrxX8qOv1;tSDAi(~Bi{W~G-eF32fM*9fuX#|*0!J;T!m>>z=l`(<-&!bneJ'
        b'h0l6y7Vk*gz24tr`^`sR4vex&bj7R<C@G8Wn{ZV+*=!q;2~xt80~)iSGwRte86|D_1-fE>J|U2vZQ_(9cFS)JI>9!N5}h#A&kq_7'
        b'^-kxMc4pRyQ~3}KX)uJ%CNrrUHP|H;{YB5iq<Q)bOcM*^rDyB3fkjEPaB~UU@*UF#woC(e3{3%%Y_?V3cz?#ReJ$BfI6fYZmC{uB'
        b'IwQR)F)k5Cn_Qf_7<~qX3X%7CMW7iy6(X9Q8BL_k@qmQ}zc$1|iHqL$^x4!*h=mc8yyVB^Jx69^EOBqANIi9jqRy0(M@rj+>Us(X'
        b'+_l&&A@Z--Jd?kc{USk@=Q;8YnE#?*Box8nM2@YeNIzR=^FZug*`uR9Wdn99M55*Csqvf7HHFFcau4y^gNmE6{SAAC&J;8qyEkCn'
        b'4U2^BLGE8+g$+=xG_U6s|96>tDRAzEXv*FM0}VV64jf0n1cOUFU)U5LwpVya0Qb2t$H()9B!4(|1_)mIF&xEAwxyH&d`BeXyU&qR'
        b'YYk%t6Kjca1wEw$(mZKNVGm4JP7dTlMo8qG(u|oUh?rc`B8ey5&tuLek7J;%)#=Q5Wmi1mEb%lM#z%VLY-vv$-Bwc8W94Bnny_}l'
        b'*5m4nY_mBADtnx?sSTp2J4$<+B%<zyLj<aJBi7nr8)yo@V=vFNpY=Ul$e~6yHJ01bkhWDe^g4FrS-h0#ZV;7_caWRggUXob#hA_P'
        b'_`0>B^09S0_j3KGhZxYlg$gq6_Z5}OjvV1RK5kNF9Y4C4cS1lu4A*}FMrN<DrD3QEI-nHkkL1k)#Y<M6(b0-nM&5~<UB%4e*_hJK'
        b')QM7?GzPk1B}4KFE9Ut6;4`J2i-I-ifoD_b9pHt^dQpv|QL8H&Ws*E@*JKV%hx4$h!h^d8w%rHQq3e`p=0#|y$-J(&$lina;6d@b'
        b'ZRYRqMZSIHUL0C_Jtprg=q!EAmR_DGrA;PY;Xtf;5x25ume65tX%N-z<<+G}XZkFCiq^+k8us!n%w6t!7>I|sd!eVeUxm_IQXF4{'
        b'Jw4b4*YP0-vaPQQQSOk|&O|_sx<3ZvFE>}eF6-`rs~v5!gY~I(wc+!dB>CPuu$t{y%g5b4Mdh-N64@8uHce7Px9W9r*c_rOvAsO#'
        b'T~JlHbvT0eMM_X9m0Ghje0=F+7H<MXI!%)%!EcAqmY!N;%)&GZgoHcNEn3W)gxM*9@qiC(eCa@~<gxAs)Lh5|)<D~%<GuX$prnn#'
        b'Lvyf2LKr_htauLc@tq50{)R2i00rC3Qd_0jy32>TC?Rx<==&f@7lBfwF_3e$(c^fmwkfo`;RGMu5}gitFUKL0$4I_k6etm7DP9S('
        b'v^Kb{eo-R6I2H8SM6ipF&ZTvsrHr(sj7gOkwU{>;OLZW_Lx_xa0$VfbgtQXMA$VA7FgO`SF*0MX&q83e;oqQE7@C2-vUuGKNfQYq'
        b'O!N$FFBh6-I@-UlV*Df2od`t|$Zp7$YD}7}3RY5an-gQX-XJVpa-W`x({@r5?^`#~E4n~%F>1nnM)1`;*GY(=3-V6(-Ae8F(7vFY'
        b'Ni&vnllg~;gKx6GNt}>?wh!t_Op=FHyz`dfPG9P=qLrRkh0Pn2G~fCT1??s3IOYk{pwBrtUqlpepUrdevD*4@hM3Wg+X!j2X_d!h'
        b'p)5<Vq23@AYt2n;;TjhHNPOyJ%RS_OANP0cm)IfhrGoBb|2uFq|Gw%i38u=fs!Ee7!D;g}IA=J!Egf~9nlh}xHv>7yZFLP7XSCTG'
        b'>@z;b?sK-foUf;Qc8Q(4J*|^RUx(wY^E9lTfiAky#nuVV*FA&m={oMq>t@VssjlyG{vn~hzS>Sf=KVXx)xY(0em<kR&C}8CYF*s%'
        b'$MnumXEb~|qhpVyYIn!sbZ5J3@KsdQuD0shbo1ZXlpE4bb*=$8-jH5h?`inU3}>aw)ar3Iq*t|>kI!(nq?;;T)%NtkI+y9C^j$W%'
        b'v)bnAuNSw~_1D3l!JXn=b#P|zGjY{d_k7j=7gzs|^#0$%NzV`B^L1Y@pLS2(={lG6DCBX*{X_Mu9&+lZf8eZKzU#!`9&z99!FS=0'
        b'XScX*HyOEoDu*QdcK0?Utl1OfdgHw|8zIJ=p0MMu^sG$q^tn7k>4WcyPaPcm0{uBCChy)?|FfQ_*h`;|x#T%0_OyA(yGhdd#d^#B'
        b'nWt=(k6T(cRP81OJ99srU6)w7YAQGIUMGw5bQK*qrd%`NryOTbpx?i{{CAf9iv=!ci1{y5kq=@&c>a)Zpk_ux&5SN*iFqoTZnY8G'
        b'IIU1!&dsvhrmy?VW*?j_wk2n0weXJbvI?;HNOCTCvTJ9c`=@8wv!)w1T_A;4Ato2b^4L{iQi@GT!{#<T^fm|xX-z1tr2c{ma)xLm'
        b'J2qu>{Rh=21J!5OnEF)AXsCetRGEV>)kmAM?i;y1Yr^1aah9?wL(Yrks(1mJOJ|c2U2laIwdFolHQ6RIRi90(L#q`F>(XqNYTdbo'
        b'Hk0mLbv0ThsJB&$=I)lf!^@hS8Kdf+(2h%YyT9_y7qSKC&uCZx1#dI|U4eX?+3&vTH|?%I(riW*WWP;$);EhcH)fC)$4xE_m6jM6'
        b'^H58mccf*_Si2DhP4#ODCNl*ciWHHPSpWZYomjeiP3(6t+CKHMMWxPYP(e}enfp;uWeXwJ%O-0wo8;w>FAvI2v^a%_3G9$yuki4p'
        b'{&u{QBP}WZ+Gpb=)qJXa`}>q6FNVFIIG<R~BbzmREY0ev`hVDa_xL8Nynp=6B$=kkU~_9IZIPMjC2eUnO}Vrc*fg!_1=tNiTIeG_'
        b'O{Eu5c6kt}u&^dU(zJrMQRxNHBv@#xU1`+?LDo_+3S0Jp>Y~evA_}69y6B=}7n<MaOwtQC0oUDqp4a#HPkS<RE}!$cpEGCPv$hY&'
        b'!?h2E0F7VzqsoioPY?6C{%I{^XJD<?;1mHLIJc~R>_jMYJz}d<ULO@G3%jAbAg#eE9M7F_$~QK`BFy@zC^^)cxHh0aPO^iv*2QlA'
        b'lqNOr-c2Vqh(oQmtQrZeFe;JN4yBY(pA5#d?l_kc+It6xAsQMiE1ZY;p|Y%X6Zo>w`Y@DLe3^uXA!jJ)D2iL3S0llgM9BfnBgnzX'
        b'mbU{u`|AYH=M%a-dfQseGdd!pxTb)gA@II3du~qAHfp|Ls?c;N^I&#mjx%Oa(Jp0CD-pG)gDg87=;Hkep7)@O`L?CF3)ex_iI?QN'
        b'Urq_7#W-)MA*XXYb?3R)R41zBhW#o?jaJzgEl4D4<O^9}9ORBFq%IVmCk}-IC(nevOP{cwD{<NnFFAMO#5W~h+E+P~oQDs8bL@TV'
        b'iElnTejxQQgZISHak+H^^KR;Nf6XYTe0p#7&tBv1M?ES+O$!r3?XRiUgwmr*Bhc5QiSBYc!<_3cKXw!?mVXh##50Mva1li5tz<W6'
        b'hn^R4mGWcUbm#Oc=I}Qa=?4-+rsqs=a<bJglGM9?%s1(rZQ&tZf4Gn!RdfD%LH=YRy-BsX%(iucbPmRunfs;)r&o-ZiR<-GmFNwu'
        b'dVk1V*XMUeOKk5Z^OjgBA%I_xP4LtKzkX|r$NZWXIWK9RWL{>aYi@k+sV*-pX-}Q<x5d-ce91xyP4T%aMEj5h;gIi&fbFOKYb1LG'
        b'FizP%|B}ggjlFq7tEjO3;vvyqeE(yAn`oiL@wK0KW*|rX9QKefFMF4=;LfOJl`$0FmpEH4uZjoTIY69x!M|7nQlrHkp?k$|64e_='
        b'A6YcPQ!$~$$8>rAY`chq;meXJ=k)fXgl~7unT;pgG&dV~45jWJImL6Idp4Qg(c4W+-W8)LJv#1jcQ9?Ct>WoUMC;w|`sqzY=^wR)'
        b'uK#TOG6<P@a6La1UpptQ>L6Dd_X=8G^ruj~ZaNK(*<j_LSDt8+b3J&svf105<~?{p_u7SBl14#8lw|e!hC9S`1pfHncHPGqB@x;|'
        b'W+8~X;GZvf@7P`msP{I1Z}XA#2{^6PLC!)e5)0-PJCd;{Rc~B{<_l?RreLaQmkOhQZ3RU>lEPQkdlDzuy783H<h+^P_nHc;?0_5`'
        b'*22vGa|aJ`z$ihZaPFwO9p_BebD4Xrd%8^~ynVVun+j`{Os7?wx?>0Si#wdmbQh@q@##4!p>Iq*K#7r4I6cS8oXg}GZ7NtXUm0{0'
        b'Dl<-|26&PZ`rU*-Lnb8sl0UDep6&lMpl<vgdXHA?l%;-=mg$@-J{_U5T1%`Cr*dv(H8-k$a|#mc>$IJa<50-{=I7C$rA|(Exryo|'
        b'as5}x_+DLoN+{2(2Mwh?*cw-@Fu!pjPn1k{2;*MxySeT}0qsqFGi^IJp6+sYbt9=>&(v#O*u@q7PPFum^PC2G4~FB7%V#`rmtpFS'
        b'azxWbzZ06@IRB=|d+;0W6U+wsl|{*<ducZc(RVZTxb}-4W)H)5rZJm>ed%7mz{MbZ>p2fpgN~S5#^?8^h^K}I^EW!GtQNAU_ayFv'
        b'%#qjAJg=p7ZI#&OVbP>+!6#KsceV6R#7jtIBa^LZOa}4F!_z(a@>A{pJo)BkC*jtX;GmiA(Wfy;qPJS>Gt4yva5vwaPS6RoN}Kn1'
        b'Mrpobs?aAu9Yoo7e>&kk$YhvlWrksMxbE3QnRD9bOqo58a&PT!3jw|wp8aD%JH+k+LmSnavm;I3^0eQb)}0Z;(>%SigN*ykzgRF+'
        b'GF93^&6n;a;y(4SA)UFE#s`TKXLlv&1cvxq<ixA}Z4n{eP9k$IB!2MU`j>8gjlVLD2MC=i4fvSo2R*Nk@4PonlW>b|QQBb$kO>%l'
        b'3fBAkULAjAVH(%txBV9mqlJ9~!B)JkNY`4|v8_2#P6#<JP~moYt-ZYsxRnQ5mJdF8d&W6h2sVVv)w=V8?OZ*o1cP=RTg}C2S~;yY'
        b'XY*?(668sVtt1lY-5^b1sLn$xCO416o^b<-Vc%*XAlu)(kRa||TAlF?P2xKkQ4_}+x`Sl*k3S&X_nl5_m+cj75mYBnalgsDa{s<t'
        b'v~R2(z3<WSNA60q>G2$P*k#=F2X}yyEI{0IBq(>1ll^(xn?j~Z#(t)&U0)+)US<N*oMa>HULjboeHO)85N8n@ES%XAQ)-D_YKgOb'
        b'HXiT8=+ij2yQZEN*Br516synMXNB0^R(u2`Dhd8X(oVZ2x=r3T%hs&ppLazDck2XuiLx4!&*AxTIs`CG2BEVEhle=A51~oZ;UP}C'
        b't+W{T#E<mZhpW$L9-;sHkZ>>2LBgmfEm3`z$geHYaSxM0d$yo`>XbDCx^{60teT>#55C+bMQg<FJ+i_*1Ih1HHA!3$kfX*s@G2vD'
        b'XH}CBevfzD|82#(aZ{*@F(d@fQZZWU{$NSD?C$C+HR*^!E-?`;8t+^^VEW}rnqEkl26{T^=#BK~z5|Epr{4K}c;A6n-<d@99XNoo'
        b'p!yCx{m!J+z5{JV9pg8CPHg{Kl>6y!ny!0e?fU!A5IxWP-?>fdZm}N<Y3~55S$zQrh;lkU_m|Uja!dx<LHEARAJ0;cM{ak?=4I<?'
        b'X?g}Wroz|1qg#B({e^daN3Zk!#Xp=g9Tx#l@X7SE{$am%hmOa`JuW;XfGlhH`o!VuabFBx|LO1<b97hYGwOB2_>9wZSHWj|PWNxa'
        b'XM9xm<MA1-y8j=a@&67!<9$gtg3oA4`oE3O_+IM&i};Kdv__a0yZ*(zkbHs`=F1lgDG`34INF$r@`yaRl1Egk9?8ik)Taj;V;X)('
        b'8e@@HNg1B8=GNjD`5R}?73|91acB40dGh8trl&>4^P-+G&0-fd)y;We`=V652(W#F*A~5zj$6>K>_fsf*0wDXKVVW)UC%zWqg~eJ'
        b'w(e+WytAoB)+k1JSz-GMx7Z?iFKJgc{CbaH4(`t<@!5KWnzHB3E@;xv>24Cti`hao{EpZ{?UJ_&4uv+cHVVh?Mm8^|E~h&`CQs1('
        b'M4qNeQ1Wnhjizwd*Ty&foRXR$)bj^JV4|AD(fp|i?8`+u%O*R!iL-3xA}E8U*=%{D)biv~%SPQkSygFLLf+?QFS~h$)V7abTe6$l'
        b'Lfi6t+wJUTx+hT##{S<SI(E|xGI4gPr_Rg+I7XJ!Wah-x=SqDGM!+}L87w)RrCx_Y9Niqo!SUiRMp>SkPnKGq;n-#z6QVdBiPmT9'
        b'Ui(X7jNi^STXo&)m;hd5W9FrJjT!hXdg;(v^u`f*jreff<}P+q*@yo1k;bhd2G7UA1Bs1x_Nh!rIi7-HdX<iiA@~T~pGlfp>YYG~'
        b'OS3aqHLd=()Y24Xm@2Ycwk#IgEe$Tq(*gYCrIu!zGO*2258Exx1|j+|ER_zWo0DfGclh|*TbAxWard)Tdq`t7g|qwLJQ(5*K{ipU'
        b'-Qsq{h=8cLw+49Z#;rCluMHM2Ts(CIE|M<R>$P~)fBs(G{=Gqh)H&Z9o<WYCXz-+eW}ybdH|8K(MRkE7n&}36C^EcxICm#$ToMwM'
        b'PfNChoLD7q-#!FQC`3^?OW!<P_3|glxm6LQ@4tiCjrW8sW$Q6Cq4aRO9KXBvEPpI*pKPgDyK40pG=6`GeY(f1Ux~5t$WvB-t7MDF'
        b'YuN(&;Tww%XUqG5oilx7(8+x=^ZTSXP7(e0>9x_-x#K5Az1U@`x0flZHIz9{j)U5EjW9WPX_>;zKCzVDcsNJCYL5B!3v)$ZLm$5|'
        b'Tei#-VvIW6LS%@O1FLa^97CDHz&>GSHx}m@_Fu?@+;WS7-7-J)=>AXi`V#m>=NOk@<|OaL?8(XWHTn@2&N7h9J1UXO(qzoRY~mpt'
        b'F`Hf{9Z4Zxwt0NP<q(dTPa_~4sdYg<scw!>WxvEYj=~O+FM5bajzJ!E0grf?%iQFNQTux=^{z5SL&6}B0yvjEkL)~;YB7(T0Up%|'
        b'dEMq41X+aZU&bP*aP>KT-fV-VX}$zBm73%4Vw+A(m+#Iw3*CY3G#N0MBiyp@hdA=#Qg(~O>^Hcrj$2U|+q@?9M74a?gNFTw&w}PI'
        b'!<>XR%?2sH$+vj_4HZcl{mFu=tt9nFN;;WV`|iL-YH(LBg?y+%g5NA^Hh7VPLNl;XUHIPpOGDva2!7)R$F*poi*3;37rYvb$^K-a'
        b'9e!aP#|B@5AGrO>imI)n4yWN4EHg870*rZw--qyO3kv$Y6M)qtu{<!OR1wC!OA)~&qT;GrB+wKDm3ar~CdkR~9$6Zzh(15PFnVoO'
        b'!lbBbyQSW|Kv5J!>0)`lSMcwsEl}v#Ck*UHEU`4*YZvkahbPN3r{)Xvfp=bU3lX#c#$VciuMJd!hz;)(x*RJl)V)s{vNIj)A!;>5'
        b'3j<Sw85`L8qEAVq4!!cb+^sU862B;wSt)o>$zzyy1?D(CIL8t1kdhsOQ+fVM$%BzF$+uvVx%?zya+y<%(FjP^9Vg8(iq(!^&ncOM'
        b'Umjf^?Z{2Yz)q@u>Ai}ocuE(;&$TFCn7qz>FDBj0>sT>Re;$*7&wT%Up>U<jxCi?&+(-nCV7j=?!-jiDOqXw9?Bo%E8*(exJV)hj'
        b'r3VG(vj$!j;pN4{+I%4~+IXVrLCH`a#M_YWJ#uM`g2x<Km)lBGk0YMs(t8yZaUn2z;2pv^Ve*}q(|iFYT`4G-Nv*>)RGc9lx1m=G'
        b'bBFb&^l{{<ytdw8p0=d<OPdk(pO?~RjJyhMpf^K=4f68pbX5v?n_nojmdE%i5Z@xmNZcUj5=LIYRNfQdW5XF9CS=9PIsCBh<2jUR'
        b'{G~&>pL@CP|D$s#DZ#pby*Yr8V6MqSw1X;TPOB7v@uRN;wEqJ1-~$4#2j;*-*kA!ffl{Z4sA1X-&~yU$%K!@A2-?$bly*C>7kLY@'
        b'zr0e9E+f5CQ1VdfMh!ByiAqXJXca9eneh0MB_+UpZB=*jpCB!8Bnh!}u<f29jj8CB@)5e8E-+rlH<gX@r%M)#jN>4$Da&oSWl%op'
        b'0!L8KIFJ#i2)uKfn=p}|r@2(YzjG@e@y@M+W1rCR{weqx?crE?Qc4CH#1K*NuM5kEUl$J64_4;brxFD-N#^#{M5XbitJy8}@RfE8'
        b'*D%#Xw&AF`3e8}*4QQC`5TIh@yT4bbo2nVKTkWMf4~!9`>-hWg1OHoi%FPboPzCIl3e1JRWG+826{d?R`=9?kbIIm$sDk><TOzOD'
        b'rGW_;gQ%r}d2|Q@MqKv674(AzW~K+}4`7Lopg-+;^m{L%KZ&RRhxBTse$S_jUtaj>Vs6Wkfk4bP_WhG%F17o{VlK7g>M@tPTFkXx'
        b'7IWQKkGZa!kGT(DE9NSZqvAU8>Xm`gNJQQ9&xyGuCFgwQ*Ns;|<@{lry?hQ3b0_`q9O8BiK+L65{#kQa=9_o}G1rkiWUIk|3zl-7'
        b'c>B!2zdPR2Az+lcXZ_kH8D#&o&|xBR#$Q;)Pb6rZM)40DW?bX&JgSDx66OIsG#nq9?@zp5zJD^9?^p8q{<MXHfWQ3VbiY!dV;ksL'
        b'eHsJPpCZy(8tUm3-MgeYJKgMlkPb0tXW*Bn$B+g*x7^{mrT@U(Is|xjWwqc?FOkuRxq-_WA)|>mDx-7(?`bjuYsl-UR=NNy(FY_g'
        b'GUsF(*rs^l*h4~E+99w_Pv&3n$!#Vb^GI!bw-=VzMI`=0+LAbaBcq8HQnSgcIbaGL@V4BoVIv(d#sU0c|GP5ie|^u~u>YO>qx`R9'
        b'eZcz;>FzcBufu)~|7-ivYaYi>x#m$`cg<6_fcL*QyXFxEcv%%EGP`4c(El1UZovOSqBP`xZ@<$2PQH%+oy+^*+x}_(_lDLybO^1Y'
        b'SmI`VaM=vrcRBv*zpf9Sc+)<ZI_AHweFKe$p;r9|<6Zbw@di6@pgvgHY^>gT%SZ$D@vf@Wt6g+oU=9n35zcBa+48fXeL8S{RDHR9'
        b'nvavZIBcJ3C26wg?;m*}+EJZ2IjYeG_F2Z;XJFrJay-VSDjS@W^Ah{4eRQFCWrT4z;+up(lK=+RC2fWp7<cfP)(yD}!9J^p-7cRW'
        b'4bCMv3(Cq9O%D-`^P^!O`#qLHbsOn`{0Ni$gZ3Gq`NByohuTLe3?$P~@oB(5t9jk#$pFnaR{Ste%aX8t`sQCoTjW(}OPn-J*fs3a'
        b'IjGw~PJ(?>SMEs+Poy|#pT7A4J~n(B$d5+OL4b^tes~UXw_^MBCEw&6uA$>s&S4of>AG_e;PGE659k0`WaiKKw89>syAmjVm-s?_'
        b'S$d=hnC7i$NSy;aT4MqqWEn~K#2cl%i`R)q7K(jCvG?i?iU$*<C6k!VZ$W+$a&H8X3t0sSVu}b-3qy7W9i!#9O$~u0Do193vKvDp'
        b'ncax5+GNhoj1P@BW5aIHJ^zr_DT6=^ebNzhsJ8L(I_<LF2cTMA`s3=^s(955Gy6<=EJbDG^KAlcHBq9EEx9*KI?=FSTT;m^c_7P>'
        b'jg~l=Lh*oM|6y7kK-N+Vl|Vws#~3n2_xivTAylGr5qhthe!L=01+J{rr`7$5D9!$;)KeE(Zu}XqPljg@E!MHm=<{VhgceKINcR;b'
        b'9r-KQLG2B(TejOu@Uv8Dn)jgAn~gEBqMT}>$jo}^D6a_h7ST^uOeFS(n4c$#i|J50+H_#;PFh>toMLCaUF=qCTK6F_{=n%r+yBJ!'
        b'FKl^S>^8HQsH<Vr>oBIe>j2@hc=lx`9qAhy^R|Ql-d5o!-$MT{k&Zw69V+Ans@ru37noUhiGD)CodzM$1(PgUkfqNhN)|9nmSrt5'
        b'GKFtngmolLQD<q2EZ6xKytm9`5}GYd>%R$PhVK&Q?2inVCY|qI7yAsPQ`)9({8$2VAGL5=058nILs=aob%x9ok<Lw+`R)vEWJ<M`'
        b'vQ5xY$z8Kc-z7__%=J{%9N;6ZS+Y{LK4knHka4N|;gU*Op<3c%x0q_WPe+i(I23(LpEvfiua5b@wmj_%!`L5<UzI2I^vb>;b#gJ$'
        b'vq;+1zO9DqVV~||H+k93z=xBTmX_NFfDb3xmcq{_cJa6<yI;1ydA7^a2ukez3)$EX-MqOws_Buv)wezOp*g8$>_O+JqiS}$7D=Ge'
        b'wwhaeys=;7xA$?M2miYzaiFju)z0@+iyzMgy0J?#)r~^v%H_@M!QgL?b+L~&Z*CezkBQpT>}(oav-{=t(~pEaa=g#d=;NV1P7ZbY'
        b'$FkUg!v67rPOTWnzENF`JL~c0@u(?}9<<erq7$N;YO89-F10-7vOIda<{Evqj2kG-)GXyupq5}jmd5zgq)&q|Cl_{~R+GM16g|r2'
        b'jXmaRZpIJ>=p@_N^#|F3TmF1&SEY1mrDR(*8|ds%D5zbZrKK!#0CcVoc-YQ*Js$%%+Mh4=o%LE82a!}7hrp@?Nfjv_F18UPsq8L4'
        b'5L#L(g?ihn$Bh75!hOeu4-_7ZF6GHw<OC|Q`Q~(=R*}9K6dh{!#x{FuYkB(m0`!e)8rxMNEv=Aja}3fa1{nj1Wil*dAhEE0^d(?g'
        b'jX>(s4={a|+kw8FQRVyol9-#=VP_jLh|cbu17br3PhSv4Cm`c8=|G`GIgFyyXkZ&bXETI4_OXSkLHG+hMs2}RA@5?$7MSuQ8B_=w'
        b'2IaziouUQ`7u}-c0XnpISi!w$J|11lZn3jZnF?nYJE23n<tg>wLX5G9mr#E9Hr4yl;-%i$TF<IgMk(?hl+`HPUS8PtNZK|>ba39-'
        b'#^VS)>B3s^aPRxig6g^6BRk!Rm2EEzT3?PT&rR5yuWZlBhYq$m)&-D10-bapvYxtdQ7!q-D91XmPd1<AJRj4-q-h4rqdHJ5(|M?F'
        b'7*eeLas3z7i!S;^7~4XvAO;aJ_`Y7Z#+|=tXE(Xnr!E1fcnY7BfYnmelesOVar=2=+xfun7X173^TsdFW6a4W@a(iIUO*bF2OL`m'
        b'IQFUFIju%vbZznsN`jm*(|5fbvoncuDtVm2>LlVoj8m{HW;gye+%7Rbm$dF>aa2=-_bq(Ze@>GyK@>RW*g=*HgsZ=%qL5uh;V*DF'
        b'WsPs!@1nG(Wm;yLQ?>c~#*Z6XM>&O3XN}ODhny-(jP?rS#H6};fcgs3O4ORuDBPUXuv;c=>yjYNCUKiE%2}f_QpmnQX3jC%_ve`R'
        b'8*AR4C#2Kq@TPM$AJ0?qXB2n6wfXP%*K(?PEQzOhryL`r$;7v6l$r?2`L`MYB|-_=$>Kx-TvZN%Tnu7A=$G3Qi4DROf%*;6)DYh&'
        b'bV%4i*08pG7P@Ms=+J`pHma4-zt-KP-b)>jpE~a^;GFE6^7ZYjmT9ZHtyMjEc|4WQQ}3cCPv|}*06H>pW2gE-O6%;-tXfIcsMm;6'
        b'_;aSh4Iyg?uHr$O)KxrSs90mJSW;T?U-pWnT*WWBiq%}jGOps+T*WG`Vg*;R(x6#m*R0VAQIu1wKW8X<-(In%SLHYuQvWSS*EZvi'
        b'c)QDG>T;o7^FVsUHsxrS<^j)HE<Kcf#2`Qg1rUCAJ}h^9;qTHs;MF`B_k~}*`=aktzd^GCT14d-Dpur0M5Re{@*^_D)R+F`*^|LL'
        b'{2WasVc3~eX~pud-M>2NUgmW#q7%E^i+kLU@kiR>Zl7k2S&X8N_f@Rvb1!)3NzzzF6zwG)<Is$}>L*E9+7_j!C%59_3@9p+vnNCG'
        b'0R%(9|4GQ$6f#9z{Ss+x2$|AYlujDU(2R6kdo6OfLhi;z--FOlIpa-y_2+2DdH8Q!jHpLK(A~SL`OfU_d!gW{LU%i>!%4@(A-)Rq'
        b'9n>l$ihed}I~4S&C{xwvu6&0d)9zk~yEPNks*s&e;!kK7?IDf7LVfQ0p@J_SQOiQmC(vvXDw?LYyO-b*?}cU$;8F4j<NYBpclU$%'
        b'*Gy=&3Qv1HTv-mIQ)MAk7J+#)Bnn_tdZ;wdEI=TL+;ElgZfGA6McLa}6qG&$LA|K7yfGP}I?W0Y#F(fw-yI^eX1RV2W3E`fKAieR'
        b'NVL%B_3KR&)`$D1hd^TT&XXbIouCR138KTPaD?=SC#)aq%L(Zd6GdA>`Fr#_-z|u~(=iJ14INWM>T(#W-j9E(|MZa~Bc%H-8C;(n'
        b'V%IF|eYbDlS=m^$flyQ|n<t(ZVRl<hIgD`~nC2To(s)})pJw@q4f12ovrf7F&BL|p>=ny>Yy9g~4owKqnk*<vlSn7hYD2|x>Onv7'
        b';KAt9M6ppELWe^?j<bmWZ^Y+@%w7b=S+f(O#pa6Dj;{i@sIP!AYdS*AZvCkqF<kJ%6vC-s!x<v@LyL@`L;LzW6U<%)e!D7GM~jT7'
        b'QSJhgn&>xcemNQP$|UrhqiE|bC(`7l?+}@jS_Sx3SJdO#)#d5#dxu!nyL%^O>^uB3N#j_^*9}EpT-OeD(_01nw~b0QOJOBFDcT<R'
        b'%1gyBbrnk|b0SXjUwBiG6DAutuvX0yoo4BYAi#So>3WAKp4TSASee(Z9<0l0R&WJ~8jp`OeoPvH;=-b>G*DpxDkiiFjKVAEZ3)ne'
        b'$;B1TP;nwmEn+0GlZJ^6fzkQ(=C#NL-V_(M1+e$8ORpWAMKMYd`u;Ki6hZRtNI=g~MO!66N#;}_LomqTAhpfI)Q<ALL*QzeJhjN4'
        b'qKp1|dS&$5A}%c|4qRU8VqMCpiWo|ll8To$)%>36Vx5lDmU23vcM)FQv<iy3HWDv{p!)n#_)7sPsX#5RZQvH`xHzpYPB+ZmM2YV$'
        b'KN=0%kcgg}RJ3)}FmErX_0(fPt1p_TH8eOMYRo@GC(hA>bcO((yd17dsadnabbIPNNn#|`>K~+YP-`!vvuxc@OQ#uh^+xFg`PWE{'
        b'5BclMG!AHEE7Q<5_KMZ6id8=Ra^tKL4UH|?4!;G6j)RWs@792E(k<qSRrEygZ_Y8>B0?%YzKh4v3i`i?!T$|Vhywq&BC5$%u>$I~'
        b'j*+&vjoB7SLFmV4I|Ef)Z2t9;j&DRzp)-TECn9>iSB!SFTfGwWM(wNRaisApvV0;*trJE|^j2Xx_~N+)c%|Nn^cYvga`#;_bz^Gb'
        b'#Av(bm!QB^pch%_x%ld>0Y>HtDB-30`%C{!$>M;2D6RHNg0+leAb$jYpPQZ$ZLf|^i^?;Axh>XV<Kfk@feSJ(U~JBSvE`9q0=2dI'
        b'V$5%-K64bd&mg~tn#5{#vASUWUX}4x(F}<#OoP8sC+Ur(z9e0mWo<(H7y&ni)TF1ZURYOmPV+M9`vl*3gli2w(IvN6*lZg(od0NS'
        b'(B?zFO(-`H|MzN^C4@#b;#1`Id~pipDi&-IBvZZ=^j!HMAJT{U&>_H_h`Yx>RkB#LK{Qk3h{3+H+A9s#Oc7Gw`!O@V<(UybDXOwG'
        b'$c!uJb_qMu$u3~WBN<|>N|+yuugZ^jtu9_Si2F^Y2scnODgFc4G=+;(sUA0i3HMYy)bfR(NAnQO`Hg1Mct2JWkg+!rxq1mmBq0Uw'
        b'nqlpM5Zk^hx=-_K>7JLP+vxJCBClpqe8E_+rxki}Rakr6;x0E@(r&eN#pAQ88Y}d8($m`Gv4RF34-M2>_2t1g_6l0g2)q@)hWk*f'
        b'TtZU65V>2J-bLQoh^Mei^Xt{0ZI7DWqgm11>(czXr(#8U2GF%AK0m~zSuO=#Uw+}q=U%iv-d*QmrN7&`o2<yZwL=X3pZJ~J7L7%?'
        b'K>~gEM*4n5HfOd8&z8%_ryUYG2y`ga2rQtzng<#qPmf91D*@sHY$*GMA1DG&Y>r$XZA=nbU+CVE%2vEEX7d8b=3(5zPd}&n{jEZq'
        b'5D&0k(k5IVZmhWIlM2+!g^R_IwLqoxh&*w_)@W^0cV;<sojD;xY~2Ncc6nL8U)_H3y?CDzrzTL@l-6CGQ(T@AkuL@VUW5(UH~XS%'
        b'$ijYxo-;OV4d_dyz%d+zgZ?btzgRM#bYL4ZHw0}A>WvwU5qZ&T8^EU}f=@GGpO$+ypJo7`)+7&ZPd9T5Nvu=`tW&u$V$do6Ec~!j'
        b'8&;}HvR6%gFZ61b+a|^bt<3nHkOPaM3<?3KAT<*-t1GS6bDCYG?|n$Gv6YFz%4{#PfwS3v77p4M+=OC+IO^dOIr0L7eV$;U(5Hc@'
        b'-Vh9t>39ipiD`k%$`Zi3=9AP|o&kd<=o|AR=btWUc4dU#==`x!odiqKEC(sm(R&4DxBFADr`asr9Iw+XpS*k2UP&uuTge7=g@Oe`'
        b'sb*zTPE<K88A>Zw`Vs_Kr{*E^^M1%u-OtFp6;)frYG-<3an!J%o%Tb1HZB7E?EHYAHDBsyOL;##>FR#A;u?MyLT9bx>VCH38h*A+'
        b'2!8gZxPS&MT7BMLvC>$=3szVfaJG}i1=Jw@!=RhBO~5=+M_vT6w~4vA*u6$M5<)R*OldxqA_Dm@79@+P+kVKmmWe_7W=+-NfOEaV'
        b'w_*l-!!samQq)}Y<-WDz8oreeHN(Dj{#AJ}9NY0X6;gye4fx|LI?pS(oH?1M!K0jNz>XEXs!xrVmmtwranxq;sRs{%OWhR_)eg=y'
        b'q76L9uglZHpWYu|Fxu<cafvhi&$xgyJ?Yso=t+ZaRQm!G_XPH%0VnFaDCjK!4+@mpvHv_2y1kKfOhR8P5%_3mL$9Z$UspV|s@+zA'
        b'`}8EoeXV(@Rnq5aJ(-l=<@r7Iy?f`X<A=gdz^X@zJB<wSdVasE9SGjN(<?=vAM5j20|)&*R%z3!J<X4FiBS)qVL<<V;6nd4(5HC_'
        b'nijr%(Z~WFE1I3)zwJT)eLwhbJNR!{TrGELsxB-XpZ3bKl7JI`Y3FWH(Qc9oK^+wK<1fi=?F^411>LEOkMUl7j=V=x1x}o%!HFNj'
        b'JZ+3PJ!UkF58MVf8~3*XVEFpt^_z{mL15Uv7Jg#aRIQINUi^E>3*GkFh*s|CWcBH5qxPs{h@w4V-dJ>YkKFbc6Lje=%}Sh0t)#yC'
        b'I|A)eKPmKu;sq%zFkyi&%>mPnYRZq8JSOq9Dl9PZz2cVt82~EZD~5Wy1Y{5(eXbSOtA%%6=pEyGUI5F|<}|8-xVmr8yVAF}92*$6'
        b'>xN70`dYqC6!2};f$yGO?%VRfx99VDb<nq6nXeAJHr}r7f@F#9)!3kC_gMvY-lQW0Tm+bOqW$@A1FoH_6z~ZY<O|rer!oQGUMje{'
        b'af4|mQ<MQ+&$qW69KgOE=j$VUyW=18?Ke1o?Am8iu-Jm+xiL!G)D#uf+$4omIqGq5HnL`PZ|<o`i-eS-L%f%=5e%Pg0FNdMGC@f}'
        b'GpB|QW+|_<1rv=J_iiSTX`Fg<0Md-jk=2inqvVk7E9g*t;@S-YhFOO5_fVGvH8;3IQQ`OBS!23;6~1u-T5QioQC;ibuGk}m^yA}k'
        b'L0#2pRzg&XN=wSoRjh=lLOnqsK555pczLu4GI<kZ?yVVx%ZD>}DjRgK`r5j8s%zjU&D~*LUt4o?x%*)fVhR(~z1r1Za}ZPhKw^6y'
        b'k-{eiQuvGyF3sP!j0@!N>O~iD*1iz^VES%^5VK-9#2810m>oN<ao&N!{N4AzA%Dj)hJqM_%Q(jP{sRSb__EXyIsC85e>jKV7jwNF'
        b'zAX9D9R41%w-~|?UUozN?tOls?f|oW6G<f^uM!0swlD(sK_<}Tl>!JRlmz$<p=3#~weC495E=+3f!a8pJQ|EA(55isqA?z!KJcZ-'
        b'A*S?QZB4Ka0!r-gsz6i`2q=RK1NFGUg@L;ESa4Zz2!AjfVhPx(D~UKg=GGxY1+K<DIuKYAtY5S~+7XALCBP>fsT|uV1q(ga1b-%f'
        b'D#BrA<tMNfSkP~tjbPajh%vJtkJ__&V#OYLs}Q3G?D5#Xy>-}dqtd`;eMSB1*M+HfjfEJ4H!*YOj>!*|&M`oYan2i)8xeOpJS;%W'
        b'-q5mjn3ne<p&nhE7itzF?HsFFgtm+JLwu=)?p9Da{fOUolm)C^y&&wl!fJkF3@;7%eY{Ka$7KVH173DS{#eQHGr4#_n;*Tl8vJa+'
        b'm43G2Qa|e)Ttn2t8UpV#1^w)xbGX_9LS48DVoZDtZ|CaBRd#;u5Qs1n;)m7_|4obxFfEve>fK96hL?vSyx?`iLLm+>LWgEV&U{7Q'
        b'cxpi)vRslgrw{qJo1b&Kpw^xtzFKT)xN2+>E*4^^UlMfsM)fu0Om14_=A~zIaGVj^DsJVKSKV9zQHHuC$~^byV3Y|PT+X(X^2$<-'
        b'H+)`+=7Y+PCM&3Gms`9u^iew01p}mYN4=1{XViKxEK`0FR85N0tjOd*Ke>t(yo#oX9KZb@lD6c9(z&#_=w+~;<;lzK2mTCe7CLm+'
        b'3!JOsH!hF0xq;tKu9~tLlOi#PqM|8rQ);(QBz@!26v_5*GfwU}l)QWUlla@>$;a^j+mSI3-CYYs$8D%6^A_*xue#mKzFmYrSLDk='
        b'UbkiYOQhpxP$)0TB#jId9>mWiVvsQt_`CCC{LHvZv#M|p@_JF9TkOtZ`YKj=+aKEgajN;bhrklnJIy%bjG6=Vnl-<{|9^vHn^&{y'
        b'>~6W|VQ%;Cu1%<`VwK0vxpQPbC4QExS>^c+cXqFQce}S4c`H`I5OnR%_7&8(ez-@szteu7@o#=qwP1nw`G*`|`Mui^tlzr4XlJw8'
        b'+u?_Pye$Z5iI(t<tIX3;)Sj-2sy@vFbH_^O%p1EcJS3{AX%t34=o)l+*x%#^{Y`H>P;Gu4FANJ`|EzjJlGy`3u&TJI`X#yfO+UEF'
        b'E)l|efKvv{6;*K4g>M!$kwz5}O?U5?6@ESivR5Fsi+A02&FWQqdhSFZ<oS}K1^;Ex{BrZ8Ts{GV_?(&H*oVMh8290rpUc|>tb;N$'
        b'9s41aE{*<vdU~`yH*s9l6Rr_^`NjjN+DlSzAb!7_dVS<R_#g2tV{hP=@gP1o2AM|^f^nb2@0`E@JutwORzCl@Y_I-Q(!gN;k;^|@'
        b'fIE1%mVdS|f}XTX>A~CCmu}YQ3~ttQ?+^tBNX;&LworYwy?S#2@_F!M1xJ8fM=t*?WN`QUD$hbrjk}EAk<UVY6ulsmg8Un$w;1`B'
        b'Bc$&Zs^1eCc)!11?U>FJLsGN(ggHn66Ci+3+I)B6U@&!5^<cgcqowAcz&%ItmG|(a(I1n>G?eucYu2m=y#no8wFi_d_eoL9Cm8hR'
        b')E~$Iq%MRXwS%l4xgCEMIhWA`!+GZAd~*Tc`uWr<DJ`nidnw-<F6EnZ1m9|F+QgUht>J2X%a_cHgh&zK*ye9@w+=oOa0o8VhY6q('
        b'uS0;JBc2=Rc(%qwJ985!^K1n^X%eX5mQl2Q@};@okZ2+IE12FEI1kP@2}a1t2_x$VE6<aFCr+VwN38Q$4VtRV$>79FH7m3ex{K2?'
        b'%S$U(_>AZ6nw9DV3Vb~`hN>tvIl^&Xsad9e9Q0vjxiFa~VJ!)+=7a$vR-Pb=gGEFE-h)XO%oCJqmKoH7bSjtofZx5r$#No6A0up8'
        b'xC&mIahhd?r2{}DbXq9*`|5Lsij|yZ<shcbuD3c!?zJ4vCT*A7YHQ$EfSIemb|?_%wkCeW35;!TaRm=?f;+tj*Kh>{C&=LnP@4df'
        b'p1hCF-X%A^&e-Z19`*^c_JT!wC5MD1+ZY>%$6qK&d~4oEG#SJUDi@HH8LeMBx3qU+2N}2jt67Vgq9;Uo3Ov7A_d%J;<M>VFS(WgE'
        b'$kXj5=*X5<${af;<kT%@71eM`?2T31O7Vb0XDzJG82eomPB_j?%{?RKpz_HD4QDLIa5TA+(Z9$rUZ%zKl^T4*C~VX!YV~qx25s76'
        b'y$dM#P2Xv9GVr_cZLMjUQ>E1|Q@05lKW<1!*(>ZITfXo=m&x~f3#a10n*t;lFbQ53$vT;qrzqX?en%8S2|_8CC^Q>Tf+~tjRPk+o'
        b'PK6;T-~%2EBix+Xuv^Zb@tC|RG|Jf~tWh~A^aF=Hdi#dQjKgEL5_<`moGELdhVVXZkqnPDbV$(hX#l(Rr^6XaVy?s)if4v#hGLnk'
        b';0!&({M&Gb9L$f$8G4ZU|8a)?@8ArHnH#|w8W{I~8)xY4asMyk3}u0$bdY-my>n|+9by<>zn^J&;48ZuJSAD93ivn?XW49LH{(OU'
        b'mQ6$8JL{bZm4yb>A&$G}EA~&fy4WU7QwYayPEbH*!5+C)2NxcfKs#rG-O>c>OZL!+N;=Nc)aBLc_Q`g?;B^zH^pu@#;u3h@AHn<K'
        b'1huW_Rvyo%2_p97Qei@Vp;yqwHsK?u^S^)YGZ^6Vk8JI{mH)_=*04|JW$SjoxcZy2J1Dc|DdRWzKo!(?N9rOdCPr57%H|qFHueel'
        b'A*Br;@#Agh$J+;M6fJK4a?50@kA31K`{dW`#vXQ4VC=HL6JE<xz7ss)GC2qxRL@ylSAYg_p1Q68+z^*}$Le!j4+a}DSaNuPp=UUD'
        b'(-n9^26mHP*R7r{DrFn(`(*i)fqg7PJqRmQ`YwqPPaZw}umm4c#phWAFZc(~sbca@o%FAdq@D@_3hB$O0Yo7!K0h3Q6!L8t0V$M@'
        b'A%&&|AcdMQgB0=+XsKlr#uM6vU-j99@q|W=yB40%LnHBo1miHC5X<8U{k%VjCq#}L#uJ*+e*<_z(=Njk+B5=B$g%9E@Py`tEM;9+'
        b'$H|#+HJlv#FrLt+8^IHD{TuLvruiDN!VJR+H9Ihz(54Y^LcZHVyzHj&1ztD0F+8ELo8!}|U)=<rkn5j@C)AAbgf{VbLd_%bgqnkR'
        b'LYuCJC$#AbJfTh4x;F86LYuC{6FM-AC$#AjJfTgO;0bNI1W#zwb@7B;*TNH;fZs1nzY<@fW$sPl3Az3ictX=04_|>N<hm}l!36wn'
        b'ZTgk()|M6gNIW6ezYkAn!jF8n)^+Wd#V&iZ*0C-?!w=&LT}^NJ_fjX`B%YA#--jo3tvQ@ZxJf)A*S{W5Xu`;MYtu)(z!x|6hVg_Z'
        b'-YD%O@eOX^-P$0YP{+0Lgfv2Xz;r>!Qm=`9b1mO=>XsjYC*=Ak;R*3*LcSNT@lO2OEA1ApU5Y2<yegiMV<Q?S`>Ir2Mm68hb@7C*'
        b'>F>WE_}{`)j3-ob$-D74s~?{S=5i~#l+*mFg)3%~c5`gbAn~5&Ka3?bVFZ>?`UotcxDRg*OX#|CxEhwwjq3J%%J|m{KViIm>qlY<'
        b'x&GByLcWKt5^rw|OUU86*?9Z#wd3tDme4ih?eA|AOUU(4#uD<SToX&^n(?-C1eVZHw51}ioWbN9WbMdc3!|eO2)92b)|PD>_;<(J'
        b'E3kxqPU39;>R3Y8GR#v=H-{zU`WIjcNuziyp(#Nup{W>4Xf$cSbGs^*(3NuwU<t*ozd0-+*9~C3{AetpX$H1=7)vNUatKSv9KaH4'
        b'Hkx=Wp(By}CPp(Yq-Ky;bHF%jx+a#;HU00e2eE{<{*(Q$<B=QlzYbf#`~G_K>D;YDSQ8HGPqEhd>2QRu<+sYpZxTo7W_|BZh$D2('
        b'_)&b5I6|&}8jcWiEgYe1``@469FCCdpN1neW)Me+&yIcoM`!}Zi%Gu<j!@Phj?j@C#u3WE_$#iP#u0iM+h!SWoBW>FwQz)<51<Hv'
        b'ZC3NP$<M{{(9k@76o!!NC&m!ECO?yJ5<|#!bND+yC5F(o=1|7mB!-adUyC6$VFZTINV7bpx=9Qn*S{1)Xo?|w>h&>%n$6kMZU955'
        b'8Dj_ultUOozNt5dA+%o}#1P6E#t<_60ESQ|@9Qy!kO*T4<;gIF0S_W%j5yLAfdPGNric*;LQ!+ncL`mrhmP=uBG>aob2BZi+x7Ss'
        b'X>Sp|sp1Y|Lr8UKTv0P;=HY`(Y2AlJkbrbW@DIg2w8$Px6h#Q}F0*G}O2m=Yz!01of9R{|Jl#;SlQe$d$M5amI9!k;2p7~GfD3w<'
        b'hYM=nEaKU(9mET29>fc3=JA4>uYngdZ5S`8c@QtCc?4e2v}@x99St4E3yQr2FNg}`;er-N@Nhw&jy<q@7%Zr12rQ^fHwYGVY|?eX'
        b'f`0p9al{~4P*eM*SV2tz9GR4X!UEk@u!5!yVg*gR8LS|_(?7-~3>5Y!Ukxj0#!X-a1^OzB87Rz5_=mBAnnqv+#oaoD6~tW+D@Yn~'
        b'eXJn<>14z};lZ(&U<Ebb3|3In2&|wu)eu%t#PzU(J{tW)SU~|9$At|PN>rC)1vO^~7pipZqx=V6nxoR1bAWV%<uRQFKaM@UHUw%t'
        b'GQme-d6W*x!&fE&d4%csiDssQj%z+u>)0&@_9@fs*~K|J_A!IyDfL?zEvOVkWbEFi`XB%nRKIGaLyGq}M#2R}1*eYTf?9+;Tu^Z+'
        b'^v=gCm^7%P>n~(y>*!&$px<8wEr_S>PzxGRM}CL>!d0+>=AB1q5G{zWzQ5(-MRmbNeh-ObAM16|0-VBG9`y+?n{(XXFRCR2S9y+q'
        b'M9n{z*W-ukopA>6c}>6wZcGqfDEo2Xg@eXteqag30}N4H&r>bu`JX(#(3$hb&(352+8n?a5|c*jfMfFzzK{jw6Z7Py7Sh&<$9k7I'
        b'BR|jLgIaOtE)IQHj<hSO)qk#oXfexZj~QdOOtD)s?8*>2)IKZMxz=Tgw_6gNTT3ld?Up3F+Zs97`}$nFg|l1YmRhDMER4buYkOAB'
        b'e*<vJNp|Yj?6fYo^^h=f4?eqgai(PBX9zBIkdb@hQvbU8Yq#NXPHvnbt|rApa6n#mQi{;_815v1Y2^7T+~y4a<bQt=Zd*6vcb6OC'
        b'V|56*lbE6JFS`A-Sd&59w4-Y|JBesJ<CF!zampr-er{Q3@@V}tj4gRI^s~7c0>99fh|BAbb;gf|AMyMT34dS^pKJS@+9|fbOK{=@'
        b'z7Jc8I(W|QRR7>N%59&i_X?ci<05-P#uwBfVeb?4*nQ!n_X;U|evO3s<q|P1%%=?Q+I({OTYk2gfxf;F;V<-+{e7svqv|iHV1I$H'
        b'{qbiT`EO(vD$!ITMYuU<^~ud5PKdbK2>#LnTE$Fwod4#t4fv*BBT7uoC*})i=S)$l5E7d9jbDeN`J~k^D|~ez`A<a~C8fZeapPn8'
        b'uOq%xv{4AZ$H(4(F1MPUBFt5jR4y`*$n5^Wlq0))U6BgM`cjfu>XvamWY$~iS?{Y0{}W~189wVh^^(U@kBbk5;O}qN$iL6B&F2+O'
        b'-o^&5*>Y6)^S!gqXVH=k<Q7SagpTg>;qNI<6D}SF{-MwJYBc;1m--F_-k0w4J&iAvmipSNw%xt4U)XTRjGaxw)>)d&oOfr@w=f;r'
        b'y1!@-w=?d~*RH?k47<9&;<l7C^122)^IQ9Iy1ALzZf7*!_H9XtB~PbTWD@kKq=k#Nq)0mG!1sVx_m}eDVm$6Im&nefCUfaT;w@W5'
        b'DZ=+&@X=^<7-PcEfJl>JZCy!8ib%h)JCE4>%zBA5-AQDKDIr3I4S%J#Q+xe|qyI`*Q+xbV1K)-n{61sLC;s4fHbI_mg~R+0362Z*'
        b'l5wX;Tt75?z2)P<>mWayIx#Ds*dU;5W{R=&653ZR4M7{ox++=W&Vl52s{_&-9hBa#>S5`v8^=q}k%OgYcYk07={c)aq|tz-7cCmk'
        b'nSPP#c~{l>jtZ1clrOg(S7PC?Go|m!J$<UqBdS9p+ZULyw$wp!t@a<1&{08=i58E-=N^7YW<>#+O_-6}Bs{}vrsbSr>)zHfzr_+e'
        b'PP_lIcK!S_sU2YfnLWwNObRk<u`_WaWOkem%1j!NSw|QzGh;wzSpk`?{(1`;kXgvJWp;+hxP_Nl_*uGzdevX}<X`D^AiK+CR(58D'
        b'Y|4jab84i_N`|kOof>id)9~XWr&!;8&YqCYe_eXeX0wo9e{O?d^K84@pSw${bJu2&tIzYFV23o5j=;_d@qXGPQ6~~iyUg9N&UL^R'
        b'eV>zP7{B0XK50_)vm&*L>t_fF`%O6fM8xzJsAOZSNZl^7UF7knJOkk<RPT0oZWrgX{ozUi1si-i)Zq4Q5t7btaJ3zEoz2eG-@Dti'
        b')>@fEgluQSx9?I2FijFc7UGGsoeHlZ5{O_7v3(R?e<mD!X$RT)c6fE0rv792D}k<ML?ne@dXaT9r%oYvw<<nb7N0z(a5LG(60JlF'
        b'MK~mAmmEq92p-iAm&-(iDYCzW=r{83ltE1|i+bEdSt((X^y``aA)dS*eodZqhX<#)V`z%^9BmY-Yelx-hdWfjlb45hlFPm{f+x=m'
        b'HAp$yiaK{(!4nF2@+|N~HpCOGgS0rn5&T`=NTz!E>hGE67rNfGMSr$4$#8TJvcGAkNvrE|{LMd4bNI7PCQ0UL3U_l%^dc0YM|RK7'
        b'q!?RcIFjnE*3Kkn^wJ&tSE8-fdj8m}iR?#p_)B`$CVTK((=du123WY4tWKPKG=gBQ;mmkhxp=b88V+F-(jm`7;Yf@psgZE?He9a5'
        b'eM5}pv{p`rH!RA}h;i3Q5@alv=dZ%+mj&cW)14(C%eeYq!C!GeqCN%MOT-;OZnr8vQXZdl>*u?%*g!&Yc?75j{t@>n0$JhbiUFBo'
        b'@fnH00p)-|Pn|{qDZ{vR0eRYHh1bsujvL)+;K!XcJT7>ay+q4CL?@qZmv^_z=xBFu_bxf^D}PushWWB+3t62sn!O`@;~B(G#gk{O'
        b'o!s+&E2pjFWWhW^zn?Mv37^2<D=3Q}`Zlx$VVh4RGUP4OkZoePDXHHnhQ*1~>qgeLwQlP&kiC*13iE_A6oqQuD%>St!^2Iwel0P6'
        b'1&WMY^JS+ZJUOC9vg29C7LVNmbm72f#r5v~7;p(3zSi;>5knw#{{=la$a{RM6ptHMfNZ0~QzTAtyf`}UG2*>Nt;DHEiS_-h@-p~W'
        b'8&~yZGM6Y}<>3K(wJ+dFa26tiD4UCH;&5O{fMi+{ptx|Z0+d`v@Z>hiV+evFqgEg#`-zIze4ra6f;fH#M6xGUFuTFacR;(~{Ygmg'
        b'=@(>?aSlR2km{sS?7ON#)0w_PhQF0lw)jiCo3$@O?Ek17<MDiP{k6D$VKW8f+xe!SiNNY@d@&RF0+d9YTKHw>eii0ght&3GoEN|('
        b'@Ouk!m0z;IR|yEh?&d%jpl=xh`&2^@4`B|nM^vCoKq6@J3N(%FRT)Piwo`@m1_9m4UX}nNPOZYjZ9WF-87O78lzy3<P$OZttN1X&'
        b'cB!C;pdMKe&ro#gLxJrj-2bKQ1O@oK5e0-FL9!cpCSt0>%jSRC=~4{}e>*>q$bLQBKbYG=zqXAkJyW9R7*nH+xm~pHSydg!fDAQL'
        b'RBomOoPySguY(n9-(obcj5;JdF0yUIUHQyFr$<%HLE~P-sdU2eb41^6x-IoACv%@+w0_Z9xG_-9;W%HeBaL?={6Z(vf6DaU>We^c'
        b'G|g{lO!3sJI%`!>iTWAxRI56jDyT|L0f(XLtX7pPNGbz)R;xPKszBt(vr5(ZYh2rrhCEfO&Xu^fLyJ7~RGs(Y+Kv?DDO7dNQ5nah'
        b'HyV|mU#dEPsX97V;<-=N`70F_598N4yR8qWPB~DWIQHlq<a&O8L&CU#@!6DkUM=&9xMTt%vF9FD=YOjBZ_j(ORGoTNydor?lYeeE'
        b'st}v2nkm^~*6tNia<s2Rb)-aPE5)txH{U%bRp%@feiv+CvFb>%%Jv`l&c5lYBQsRCxjgT{-+6LXop~xFfjl{?&Ro^V@49!Us%%qL'
        b'%wJ^MJ+d!Idd$uQf)1r4XvvP+$LpNT_IIVW6xBNkqMaRM9n%mfmnjC6E=j+mACw$!@ll;h2l?EpVxE%i+=6!xJc+8qZ>0A0+O|I`'
        b'v!=*<p0|UlNqf(7^3#g%c4$(+e%{XY*e2J8Ss#(7gyDPKS*QHygZ}Qvx^Z0C;Q20DY8$1peksF$A7#AH+nHnCXe@r~dpjrX3{e5O'
        b'sTBNWnBH#w9YW|}V>9Z_#P3(3v$b+*?~c~)!qo%r+80v)u6!@O?sidqxC*1hHYJ4mq`1D6tKRw@biJJm=XxHh^AhX@Wl{ntC6mPP'
        b'IUJMJjYu4t>JpfsugW^5WMXC739`vv(M&Q$FjZ(nDy^X#EWwo4pW7Ou<s^<fpl#L#rRJH8toPwB1C4SOBDe!0U{5NcZmtr4NMzOr'
        b'N>g0F?{<{+m9l^<NDFi_BZvRqz0mfBa&p3WwNhgH0~8dqK2sX@+fAZ=l$M0JB%Ht5K7mWG)N-}KmRduk?IWdL02VpUYM0dz;HF9h'
        b'{W60@i;`qqBqJ;?K@e67VE)!LneBH<)4lyx&T2CEvqzOBqJGoT{v~8Vi82!En}`Catmm7Ur~(joi(3F5T`eTo7G+%y!Ngh<37ijb'
        b'NrS%JhO)LOXKhhx7s$2<fK>IQIkUDYnH<>~GB=K{hzq4fMP3t5myzWOCHuJ2MD=T)AgSquXQ#3ymGF(j!P54UvLYeD_M)<)b)MI~'
        b'v7|cHTH6hwti;`kwWHQk(U|3S3+XuboNmV`M90}SD62Q#=6OiT{zeJz6MA$^B67W9CPDwvF*DiwmEhqh9f6J}`b|n4e|@(R$o2p<'
        b'ihw&uKP~VqQSK#eE0qEFYt+D`Y%XPWlLR|BGKq@87wVPZ#I#Op;Tg30Jmb_Jtwd#y38=sMk;@`zi6LyikwarojS`}{+i8W>I2~!-'
        b'y>^FnSz~H%y1sVpD-lOO1)re=<FVZn9P8-lY<9IWDaVw<^e#Xs(ujEzA5I!60{HF|63jy)Y1NVzruP_*w1UWh<xy|@J-<>`B;oHj'
        b'v%gg4a$!doe#PpQd|H!4eFyfqNSW&uogVY4@l`*Yq0CyS#3^FAQidXN;a;qTjI7uci_2LHl!z@xvLqOTEm6w2ByFJl3#C?p>!8$r'
        b'Mq7}Uh4KhJCrc#KAUbM`wem;@e%A?El9d|ADE2Pp{Z5miUyqXX`hIq-QeTk@vS-IAOMNybmZ>eb%}^#1G@09~vQ1agiriK@k4P$K'
        b'Zv_VA!}Y9O<q5mIHb)?YL<4!GN|{!I*vOhJL6$)O0^|@Pn+)?Uh7dt?kr|TeHOf|E2S;RQ5qWX}A*jod<+JWA)-zF=Mv(3t#xp@V'
        b'n;_bAFoXM%Fj5~=oDDXZs)X{r5bX{9Y>E=a6q`gzS-11^R!dB!{U!PWHc<)r3zX4<0+<0KPeR82;LjN4aG4!0!w}l+0+X=6B)mYD'
        b'BgxJ}twddcEHJWGP>hI3$S`EU9kKv1{rZ>!$chq(I)lul>enlaS(y@84K#s_*juo?fRpSfr87%L7SwV|60s7Hp9HB7T0)hzcGIMO'
        b'Wa`(N3$n#XA19G<66mjzsEe0@Y-NhbL_#l*#6+ozWwJ==9CoK-$s7j6+Iwf#ZiQ(=Kl`o%+_@G6D$j=0NDhQW&IZePPN9!WGRX=U'
        b'i{xHj<WAW(RU-R^qS`B<D1<bPGui)9Kus)cLc-h`iG<*D^sHOKKi6STLCw(Aj}>5T_&rih<5=K2BaB4EeJjuy_I(A;QUpoB3gZl{'
        b'KdJi^G+Dhhe^$N1TAi9sz`_CS-DK^|bXqmbEsrR4JvJoJmn`XA{q+()jZY*>oHEWm+T>)k9Pg!>&ZDu2VM=(96bU{r)vZX&5@zEG'
        b'fWOWlfP~a;1rr+yZXxwmMb@hdMjokWlJL*pD-eq%hhP~LTY${{=&oWgd{cIR>Q03TxOgwtiPYaIlvx7PY`9yH`l15#5#8Az{Mo4('
        b'F0WNUefSyZ$3!NTltqHk>VMa7D^UdWS4jxK`ellORI{Sa4)!Dj5dl3Q50D%rob68Q<W!Tm|Fm)xthm3xz5*)w{C;rFL+e2sO3X^g'
        b'%F-)rcPhZrauY@g2qCLg2(nS4lDY@k)+=%omd#qPSS_~Z$iN}nY9S#OZd0VPH40Ei5JUA7x3JZUtZH5);2Tu^GA0sMb0{(<8&b|l'
        b'K{jE$AIpec4J{<W7ONClzYesJ@GT^(`v+S{poQ;0k!_g*pXEqLURKz01kK7<zzj^`{j+|haJk1p*kfb`v&t2)F2onh6e#l`T$Bll'
        b'8D$bspttvLPmJt3=s)oXdFQ<f*YoJ$o?X(qCuBRv2yse-^tq|lhUIlnbkmPCj2G1is0f5+%~60|L4UHC;#sp5raLiF&?R_MBm)a8'
        b'kdcvkYd>z6(;eNEn-~g=LJ%85Azn{cKnbixFDTB+S0F_s*diEZiM*eIh76uui~!*dd8Qog2`%CJ;i7{>wo~%lR?JvfvB53ql$KC9'
        b'l<D6{wLibAwzqCQVa@5r`ekj#-c)=rD^&rDXhh;sX6={LQyG+m^vy_h5V}`p5%3e(0SP>VlX(f``E-iGO`x~m`YJ|o(oI6%Eb}mB'
        b'qtH<UArK&#A&e>z5PX4fyGw%mqqdjji39|s`UnNPQx5tJ=3kvC#p@Rc74^;PCNbDC`=Q(f7EkuGGDW=#CeN2?1tbP0vLH}kOa-h|'
        b'fgni;ltV|9Lx#(YC<!{mvjGnmS6rPaVqh67M(lU;dcPdj7S)O3`bv3Sqt#_W*jCfPD`0g)5ZeazI!nM==CJ4FhlD4L@&Yb_Txu!g'
        b'EGB6jXEB>Cvr8?rR`<|CO|rz$dvSWQ-mq1l&6-)0oi#_r9_Hk=%Q?$k%>9sjchjQ!`{h`^#R;a+{*67Tk1fPWU`hgs$b%={?h|qH'
        b'$S;#_6Btm`oTBaT+S%DIxR@Z1Y)VR`MX;voW9OV`kT-9M2}MdVimC!%j5jAfERt^^O}F&pqkCrin-{9u{&ZrweARyma-pN?Tpw#H'
        b'>Ns{HM}A_y{G|J=`SlBtUm7fP>4%HIEXnCUX_>cXl)+MTB3E9J1<}snK3h<~A#{F-QHrv5%FVC)K`j_r63W6Fk+n^Ze-g!@AcjhG'
        b';?6*$=}xf6)8T*IOM!23S^lHPa(CIYD635lu@S2pk)+Hj#%bGo16j|=l|(T%K-_Jyi~Wxt_HNv{@F0>$Zd0d9x0~H(Bj=oGm$$d<'
        b'lJv1f^l~&xzr)&Dn}f4%r^ot8cgdXY8VM5Vt)@<&1ifdJ7Qw_$%mMZl-!oTan#*EWk7oTs4t_?4?xRJpHg?1#ibSWw@snAM6B|cM'
        b'qjEZ=eQy6r52D9Gw&M)#-Mv|CeYCqKbVC?k0a-WTq9kh1^rjAR)%f?fsc(;0i{j(ej!-16b^)19_?7UQMsZ!;0?2};)m=b_Qy#ge'
        b'_7QyTt|oDLT<nnxGSjGj@Tr??_fm&D7+?-?qpS%9_yDs84%kl1z{4U~=EEvJ8A%&DLTS92-3J}+mPa1ny?2*X+P=fdoMcU(w4YgD'
        b'i6O+BV7+2s=h0&f`!CE@ssA+4$Ib>lI+hE<j{GvJsNm<#Rj^X)W9OcDQht&xZ0>0PZL4Ij5JevB5G!*Kcp|(hauU?)nEcrLF;bK^'
        b'3PrVplj-`yg+A82z2l?idSyP=qMV}bJB=&+NZN!soyaR{0$J)iukISa2S_;fE{GJ}UEOv|amypf7A=ST+?3wW2<|&k4f#;<3Y5;q'
        b'%7JG%P%DyTO;&4-)$2Zs*k;!o1X3J4u~M#OizC}tt$L&!am|Tfr_G5Wfemb~*=n<Ll~a~9FrHRf$?q7@F+o;w9RB{$f51SCLtz9y'
        b'-eUp8g8-8LD`|WJDJ_SNSxOH1gfbT|86mAYy6xf`;H^g>rz9A5s(nukh0>&m>mgv`r9L6pizbECw4MahOJbD<m9#3#x$zBjqC&pN'
        b'0xY9R$G85I?5xw%LQmgne(v`^J^zexRy-`>r=ik)CSXre{9<xVsDnjNw(m0~B|yd`ZGwn&^uWOS@PLc->F_(^rE>2+)1pO63Ra$Q'
        b'AFsDkLXVaXz(7z@*00P4JyFp(MB;T8)bE1&_d)$ATwl}nd9XjicPq4o>uD4rt<tg*2;nhCq?JpQMxxYr;q>T}i$ihBgn*Vbl8}}M'
        b'>lpYt27>Fka60}ZL^Pne4`@yqr1^B>=P`szNrd+<hajWOCLG}9xqb*ofuH>Fq@IZl?AzFWCaZs1#=CmRXTZne4P9HaIw1t_6}8G3'
        b'kiH=a@<R3*8D2=R1?*N_km(9ouMEZX2g~l^@_VuDQ!<DHTA~2Lg<e*`pOa;aWH>4?Nk9O*Os0)328W1+EX1|Iu9P^Z<zo*xdyYl6'
        b'2wD9G*&tn$ai#j^!hDL`Pgw0t;k$Tut>qVJuf!831IJpfBB_OF7vWLJY~eEe*oC0V@HZCL$g10JKiUP!6OMK`_GY0}i43wjSox-|'
        b'km;2;d4h<VdNxePZ&Aa5Fd8gXWNcFE5?THIm<!D8BwYVK8N@<;YC)hN%PvS=BtsMWgXPK*<?<2bvS2yYBEuPBRzaX3TTqZ%BE#!|'
        b'K>3~#<-13eL-1HgjS~u_?Kh=jjxmA)y{G_zGGr0eZF9ig#}JSX5|GVn(~@A}qs$`pUH$s4{k9`vzz$gDm<sy&<qJyvG)zg5h>E0R'
        b'@wUuuso>jTc}A<4SV)NvLIl7MFT!C#shW{>JS<(lOYV6kOdlhIZWCGCUfdt%pAHh8NH?sV@EVHk2!oYT3_%7~iY1DI5?KKv`tgdZ'
        b'qyW|fMgn9&#0135?}@m>X2r;~IkLrq+?G3Ly%d%kcT3R|W9iYfh$(t}rbr!593qbk@HVfl3y*1h2K2}qmg)`LrY3zaAogioc66dy'
        b'3R!O4ZTN2sY0O3Y<gz1j8Q<<1+-~2hup<+~Y+_vA7D*ag5ZFGyeH@pFW`)S`#ul`6j6<_T(2*YRkl8l!E$<6E5*J2?*dFJ9RfZjD'
        b'4x1^NFXj8*5Ek4`;~&nZgz<Y?Q>6|K+BZM!NJQ9DH(^`Hw<``iq8e`Z&?W804YeDCW}OBe<m~%-*bzw>t+B1(8yAEf2^nsDp1=10'
        b'vG?wAO<Z{c_hfP*nGBE%A~)Mf5DbXBL$D=r?XyWrDQNpF+Dg^!?gLsZb=zHQeR^BkW<m>t;x0mWO{je~p``{^wurr;mTkZ-MH?(Z'
        b'Yi(C|sVl9uwxw#-qA>3{lLXQ2K9~1>|NMPFVrI_$`a8cf=ggVg;zL9{_t4dVN?vC;IvNswP$E9%TNuCdP&}Q_DW>AUYql4sN_8|E'
        b'K$~Q@mit5udLTYDAV$X>7w`MyL;dmGQhXhG2Kk|A-WMP0i|6i`W-hj~-ap5O{v6L0PBVW`G~W{++7r*&rkTGZn!gbrdLy1&fUkLp'
        b'Tk9NP8a`sUKZ|xd<3l^+H&ZW)B~>T!Xt{3Dydyr;5zqZ#T3BNH=xvJ+wZ(I$Y34gb^VaxKYdmM1X8ww3?u!rk;<+@j6!24HUo;iC'
        b'Oq_nEVK>7ih_<N2I1j#B6Ej0Baa??H(PHh_poze5<CiqV4?U)Rvf#=89EdqOGhFJTPg%5_{j#pv5{`)aJMso$_*<O#nD!QVctgX@'
        b'c49MW_$ZET)ZC(qu4&o{!v}F_zMcC-`~oBM!^pR)xS=?wxHu!OfyZqL#UW`)>uTFbqc^&@!|=;^aV<RbPF$9q*{pHC`CQj~T-pNz'
        b'_BY!|g@H(1u6~gYyej7caYru8wycgv3XHQ}v&W-X5zdA(XC1TU&vDK=djpyZ{48G6E@=pA0t3u`d%8r%NT>iqAW?z;mxz--yUb)C'
        b'a%sGNrp;cHNQ4*YYUw3T&R$EKs;)Te*#@@;wHj>GxwF&5;DyUAFU8gFo`<HO1VM@GV4OW3tCW5{MU-TX|BHCS^OWDliG!D0l2{b$'
        b'+Y(p1M-^V8t6>Sk_q(|5b=ij8_{g+Ho6Y?&9*r}#>9kwYfLFdg6IB)zsNvl>G$C`=KDU5x@lMvZ>kYq-%Y7^k`9iYHB$*@q_kK0;'
        b'N|Gkm5Z}N{SdRvkOq~Qx9v^Jq?*Gx2w0Q2pxcs&mhKH_tQKlMZ#EZxJ8ak($$_=`Bbf?iEHJj*<A#&+>*FbVO&;~c-!H-4_RJ=Gz'
        b'#&S5kbd2k=R7cRd4wCy(9BMvyQpXNxv`mJaNL(Ztp$NryLZ+S^HHcezWJCo;%#%gh0A533<F4-a39o;RjtkTF`*e^M6GF7joQXpv'
        b'Z6eWs;@WA&e8SZ?WHiyAd=}T3O^ggX2abL-8b_zjxkW;&$Abs<22<ad7gt}5(leS&)KN9~VdTK_)VGe@LC~pzy@B1!yHnJAcc;`Q'
        b'OFcz(l-rM2WyQEga|l;9k!X<*qu}3<>oUcj9{lED9G(2(LJ6%J-@C^XOnxIrPOA!$GUQ%<qzx(3XRO^tyD2mWXxuN9eoi!+WFD$z'
        b'fE~Ssz>B6wRuK41EiK_$9z9cQZyd_6YZWniGl`c^BV|%CDRg<2xVYwp^NIU3osh4a=^}}o7Bo*xisjD7;<t2kUPrafwgHzYa_2HA'
        b'%?6dxD5?E@T=z^=a#w`<MaAiO1)(cLf&$FAEF?aOd_5p7)@S8K&P=ltUFnh*qom?HA+edD`MR6v%3^uljH~;Yy7hit>qQ}W`oe8A'
        b'FCCQe%kh5dtNR~DNP?@w^@yUtS^QMsp2N5J`U|0h%#_N}Wor&LXq_988&6+bm!p$H#bqI~Z|d<#xwL*MTwg9U&PLk5E|))jPr2Ow'
        b'`&g8Jl*QI7g3GHomhCrwsW4H;<tEpl3^h8G{>_xQhm0fojFLu!7C8^>U_49q+graAHdF2;1NI#U9#9o0|Naq)(V$tdrfhwH*3)a&'
        b'-CX^Y)M}-bH9Df|1g)IYbStgPvf@pgEe6f@-zRs?!2!9-Wu7IY=LO#GUV>^Q3y*_-qsyQ%QF!n$t)GbbQW4&zay2bT-}`_;qXJ4`'
        b'2iZC*1V8p0QIe@anQ4{iZb~jEwxG-ri3bSFqLu^fXd=-e?Z1r5om&w*wbzczi1Ve#H7aF^D~J{oQSsX8NGC&fxi`ca(&AiF*$&<>'
        b'ZS6Wek2*Hq;#G3D$BK0vOc@;&@Tte?M8&StrIgUJifGeC`(%9F&iFW&xKq#NkY&7by3s44mEO8)bQf*s3LJ60)vs*zpN^PykfU#h'
        b'`?ZgxlWAp1UA5D>;UTj0sDiDlE`3~4I$Pf2V|pa*K4W>2xxBdb^^=ARu~*t%l2o%H|E;1f???`vvbRIdF*uohAxYQ1kq$-cJ138='
        b'ZNYY3A&I8l$(;^oqCUm&Y3!`Al6P=<mc7Dc>^nJ+QlJ)R^pS<%3E^~(TrDp{4s9a2<Jh1r+E2J4d>d(_gVU}LOuK&f>UHkH*dns('
        b'GW!w}_BrybcH>L#1!|9HL20qPJNuYA)F0dXZmjR!*sc}>H-O!Evi-UTFQZ=3n0<B;-|5ke@mhSh7Ts<6bFBEJz^|keGU7h%ka9iP'
        b'OZ|PQs{cldNvCBsC^IPTBGRJUba&O|l2(S>DMntc-T17<t<JN$ujt)H$5f#|#rD1$>+_?yS8{FGiM5E<qw?G?2D%Fcx*rGHA*(ot'
        b'YKoQ?UW)Wj3(AyZUqXlMacQNVYsSv`TdO`tLoqGykgdpbt(I}W$EJSWJt=vkH+|Ois(|-o{uY~!{a(w@T<h_Aw9P!qSY;9VZ$(kn'
        b'xA<pyhm7N6!-9ls$C0D5%Qz=Q)P{eK``3}UKZ?ekj^lnT8u!f^KZwS??t9{1WlBT;FRe@yV_#Z13q@ZUjecV^`Y*!KBiUeGvU~|G'
        b'rBm*dGK;E97F4tI8LPH*UyhknR%*R@8hSo^U(+p$O5L$ndRN4Dd2_g*i_&Ozo5YsKEZ3e{YxJQ(bGdefWKCjfZwYpS&#}B4yDH0L'
        b'enur8nBcXpa#VZ8hQtD6ku33LBX6+iDvRhC)KK$(PxjXmCRx?xO{=iSA7PJ{gboEhcGPHTOwF@4au#f8l5AU=HQOR7CTTM3)`e%Y'
        b'?lM?oE0<(dTNT@GS}`99soRj@GQ<2>eo3)B>$w$5(-I45m=~Lsjy&Y`e<1W`#V*`Lr*QLda8FT*D`)vqVyiB5H{g42W~|9n>QMWb'
        b'*e6VFb9_m$SuuVpD}VH_qdnx}?X9H5KQm2@3e}i>w$sSqi?wIx#c))t-;&ziW<e?}7l#81uIY&3eu#^DRiB1dK9E~yue8%Cuart?'
        b'3a{I<?k4XOn$nB1`n!<CI3Sn|bmCK_I+Iz0-*_R*ekEs3P0Sii>8IyQcj=ub#+F{qFdOREud_6<?1s|2z7Bmy_kKtFzM{LlZ*XHc'
        b'rb?~ixX}9zGDvGdGof#3QEN%ej^EVRL04VwD_3x%*o@B|D6dqO9#Ix6eV@|2{ek<kWOWH`cRwWKbN$OvHkNnL+%fDj@iT?*5c0}>'
        b'DEcGqLp1KF&-yJb2P7?(QrrNCu~lDx0*+#TITsXN77mm<U(y6uI`bH7;Vl#zD!2hLz()vFzpeX(N&{~%%1z}L7ZjtSxl_^qrtrA7'
        b'@b3a@sVCHUH^gb-al@T455*MjL7mgKfkCarB1x>qEtmTUyQr@~UHU`uYCh`9e-;wo{IDY?;|-zzUgYB`5;e*Gv*^m`llPB_zhq%)'
        b'SRVEuOLE)d0jYXNpj{K(b5x(%qfb+QXi+5oOo2OO=3oV#z2^8iUTs-yQu0YA-I!ZjdY61-ofm&c0av>zDM!kNTR>$}*dXm1gGN)b'
        b';deCKu4OzLZyPpmsZ8Ggi;sRylZBrO9kIuiHJ=G|3c99mxNwJrj@u~q-$vx{l4`^$t9p9Kq#gNM!+eGPey&3Qol;eGF<)s=6*zx`'
        b'4ePKWpKSQG7!8kS0mz^&xn?w+Py8MLnOLDP$sO+~D@krWu7aw|sEk+RE0fMwtR8FBdSBA;iP;{@ZKC{Gqqm?yEWF|0XeLkN&BH-j'
        b'u~aefxo&khhgm%LAGA39bjaRva7*wt*1C*dXEt_fQ5t?Q&9@T!R_12Y5#P$1uLXiDz`hh`BeEBDi=-DR)?ID$S9?9o6)RKMbmkPj'
        b'sY5opOEO4_Z*Z@~wH<QMkzKDyJG0TX&9SI6{}_kWe@<xekrCZ3qe~LeBYcFpT!AE?*-Ka@86A>asQLukg4Oo<G(8igrbt%2<W3|_'
        b'XyuDaW@~k&q&7Jw{}q`@R@?X!`&=5Au<T5qeKvA!yDjh{Y1>-eVA~KpZ_l7@%K~?jCAU}GN;V|667D6n9x~<u(vU*mpN@AOg=W#c'
        b'vuNK9s6#I2VnkU$N{l*5qmRg5gSzznZKOd<(+ao5W2aS{RZMO5)}&wa_I&@N-7=S2Voa4dTMZkH>a)ha8^(UPYi&D|Vc2fG#~COn'
        b'+u!u1>bR;Ozrc}dVj2pvIGSvjQ_VDNNIf2WV2lqqw^r9bk@}m@5>vla(y=^O`|1%o_EdS7nwXG`$WhIuu2Fn~6t|B}b6)z)c_@Ge'
        b'!Fj611vNcFSWlq+bGo&mF?H{ly2~f`ol%GT+K@|YIHTTZbd$Ue@0xPi^SkNL=jz^1kuyc%w*rAgc5@!CaH%+76yJJA>WIwdwQZ?7'
        b'oB0k!>xdaP)E$j|0#l%I#~40V(^4i&li#9L8>@Jykx4ba<@j}7L)|WCwP9n;AlV_K)pZ7smJ8t|@P;n@2}h=-2r2b$En^Cl7;nw?'
        b'cw(4k0VG;Ce>y{o+ae#6?fJFIY1%cYV$uyAsL5n!;y^x<Z~+`l7bynfAdX6S!%)Vp*?b)i!L3z%Er>FrL)!YaP<1Ku9VD)Cig}-!'
        b'Clc_l*RSC^#iS@`vfbaN;A2)I-(tJlvO`TPdsHpn!;fy%4yfjAQw|}KvB{J)Yb=%D<T1RY?!O|SF}GngF|?W}`$Ee3)JuHoPkd_U'
        b'qwMKX&Z~Yv@|nfH)2SYmbjZU8v1UvNZu`+Cr^@}3?K6*YZZ$n~<3?KTe6y+3xnX<a?8GE8^t`(Fd3BffN#FBo?m?Wk4h8oswUgGj'
        b'j1p}UBmpaD&{WxzO|@HNL-p$3I^_1(iu0)Rt@lpe|E4;`t9zeCW>qNnscRmXG4!ck!{GUUB^sP#9+#o3^{a?=s|n{9Qj>g65*>O<'
        b'-TM^s@L&BW1i~~!ZOoc+%xt(zoh4rv_1f^M{sE*aFZBv@UjIDwh`RS-<o@OUBcdKhlfGZ6cdk<plH9#GxiM?wP#-5pJtyfO;mPtJ'
        b'PNo_cCe=0`rT1i%ou<{J|8<gHQ1Kt=Dg#|nqd!MituLOWQ!?<?=(dw|cI(g3RRy|QG<q+#ec>d%vI1XapsTg5KgG7qC+R0M@D+||'
        b'W5r5ri>{hSS70CRlXQCqz8c+nGCG%MHXy;_D^TyeO+6^(a>Hp=bV%#_Dqc95nupTZG=kk`{NZHH<*?kP@1WH!eM;^J6qbwbI+8ZI'
        b'9Lh9Poi6fzP@bC0Q%`$8=!a^KopwKppA6vV0F#2)hjO#kK?hA?d4?M0xzCtItC0Ydahcc;o@98%NyeGSZFSXWOx%s?MF+Z-?j+u{'
        b'TcQs3P#tJ0<|-#Ebf-$&FWZa(#Tg_gB{g4&^<YR+8%ZMQ;NHiH<!0a@4FPIfvtbsMnUY|bNo8io8DiC$3zUWgYRw|jpq|>3m~lne'
        b'@)%{1tG%AU_AdFB7&WT7oiS=}iyf(!+s%43ed?8}=P9?F(@-)=XIAyBu@RTHvya_ahZ@L!<tAed5*c`*Y0qwCa8w=WV&9x4K|RHY'
        b'M+RJ$YC4-cM~Q>Yv6b8zicW4UA}Y=c+&3y`d%)$Bc}-1`azh$5cNewu6y@~?M&nPRiC{x`?lMY6CiRgy`UxucANUcMpEQh6-j`n&'
        b'XY90+HEL{)TIRLay;)3WBSWV&Y^-)RY`8@o+|M1QoG!MLXPnK|^~HuhRc>#1pS%4K716|hgCjxR!?{_OiwYAB($!8H$u4ok<9KX4'
        b'@`ZHdOIhy#HRr!(9hY{!Ox!V^vF_7tr$6bZLjBaveyY#=FxQV=eo2M`6moDc)qg>VwhKDRbt}QWjTA^;$t!~v@u7}iIVXi~QObfT'
        b'Ew>W92~Cq;R2EKz>-KdDO?F<#;i2ExBEP%vuc3o7kvtmqf=DnCNFhf)uVA^CyMqeP>{g1-UdAE39P#-|<hKR?+FzthG7}kWK?Cy='
        b'D$;meq%3&KPjW9}1N8d>{xurOQpaS4RpOXUIAqGiyCuj=f!H_Ja!q2hWAXpCFQm3RWi8(OxZjGFDYlj-ZZp0_N)pbG{W(h1Uh=Tn'
        b'lBX!72v^EW6X`THQUU6)VVgYoF>)|ZjMgVU$m@NYTD2Cb=@RoI<$I@(D|!?Q7qu?`^dV{+^~vK@=y7W2<EYq=aFt@5?G>{|4fj*@'
        b'tlkY&Pb|vohDe@Q<6n!M*LMzRox#9JP`feMLDI7VK`o6WZrGN-Wx1YC?R-aDBDz=^><ns=-}|PAfqs{YzcNlLMoHFuAY>&P7E$Ix'
        b'C9*7zI9d@7vQppKuPqaUTN}i(7R!TMBX#tR3RlDeYPl@<4l2{HRbsaB(e}Yr+@0Y@-y`WDGmZ&p4)!rV>*mw28&YvWpx;Bq_9N`7'
        b'^t7l~|2=FcL1Tbhh8o)<8L!HsR%9Q$)baq);w3mMcD!9T3;DZQyliCYRE3P#ta6)5>x4E_Kkm(4NM2@Bt@h6nQzV~cQK2kqCqwo5'
        b'vbcD$S|mihF5`%R(y~t_=D+Ze5PrwP5R3AK=cs$J1t+6WBkx8<v3n|C+)Nxqk0j%LA$S0{<*<#s=8_<$*M$O4su;r0h<1bn7Zpq_'
        b'8^#4%7u_4Irk1FwMUKrRt-Jko{P5ncq{>y)q9S_6?QckEd5MvUIT3G=Q+6qpZJP6%%=Ad&aP0ExS8gH;Zz76T8zfZaBSQt+?Ai5&'
        b'h6xoj+j+u7)E~)AeB$AAs?1C!SA`>g_$$@0RM{w%btrS{X?4*{9_?^B@wtIJuL{4<Y8YM=>(+iwH7<&4lx9AWvLd^9<!0)w-DS&|'
        b'($>o+sc{i)%F8M;N@v%bjb3S1rBRwuzur_y--;CJtjaV!P3Au@rS(=f%Gkq)RW<)Wc`g5|YB||`S4rtG`j`5PkvFt!_XhTASM5l?'
        b'e{P)bu*&<#uFkh}y{{NLn*$}D;l?7`q*Ht<J};{IGF(<}9rw11*429AxPZ!;=j8UQ^1E>{F^nuKL&MLsk!CXOnf8`|I3ZD$J}yL`'
        b'eR6N%FI1J3Y_Q$xWck4DO{w<XDzjIDr%Cq_hBsBg8HP8oFDrf+<(DpS;~9)<abC^&a9Uc&1@2YVmOrYZ6NxO9&9;F~GW=0hI-4-G'
        b'WAnPmJFocB@;UrcZN^1mXRB%upILLBpp|pna&9Ir^AWeUxyh{xT2pz&xDa{PS}{g&%__Y7@e)em_9i4Xy2I(%jnbirjOkpX3W*zW'
        b'c1Lgxszz@Nx;CTh=Wq%<O72+|oh)8ed>wtR&(*4E6<gO7O`o|yMn|77`W-aw%1*&gX{VkyN8jDebR=I`N@eO~nMR3dmg$OJ({-M9'
        b'6kZVs+T4$t^3s~fv%SVX7oAE|4S%fmdN-W;xbf9znj6v0i`1EvmcDh!j6Snjz5OkXtFH{H2%U48H%w$h7PFaj;<}`h@KAxniPm8>'
        b'4bl7Se>amkPtatowIHW>tA$j|CerG*CYfukhBe)Ik8_%;)~cYt+nRLatg*D@tw}ehWo>nzqg_}vN^9Gil)2UNbJxHp7mEH)>uN3t'
        b'jo#<BCY?vV7b1U}oX@v*A94+Rc%i75b|4`{G<u)i>VBO*i!>H=&2LS5z1AAn=&jkBl-%g8-I{c?e-s7ro2^OmM(=MGqXKQN`9z?N'
        b'g(DF?>?8b2HJVrwI&o{1^ZeEIJ=#=%E>oXE>&*_r<&e-)yeSG@V*`oHfl9%JZj{K%>>&Fui{nq4BV0C{qvNL9-N0*7jfyMRmLVEh'
        b'rRY!TGzP-;n&c`F3pQeh6fPH16|n7;`|mR|>G-5*7`#4}uhWO)H?8L%nKCCYnB=?^SxTqYJ&-@Wk(9ZVva8`?cQh{@!aX1>`Kohl'
        b'SLJpZHEJW)B$>MEt7X(e5{*&`(Vk9t(i=7g=rlCvcnj~7-`XrUqN(hy#I*8^=(f@J<L<(%7)Gxov6vW9p%y+(cHr`xlk@{OpJ|m}'
        b'C{9_Eoarv2$;SQTZxko{l_r1tOX4a(KS^Y+IQhm3W#$9&%qRYee4C0gm)`isQaZCyMeoYj(KOlronUgKvg^Nye{}>JfJ|-^iDou<'
        b'-Kg)-1q+f}Igv7O^<B7NLih4$nK)>jYe0Cza-D4ZpZbEye64xa*+|~6D+8C2xL`86r1<52+(t=Rtw-<Hxn3ervsrUVX)^ltD5q`d'
        b'rgS<9&4DdV;m^`wzs8q|Yh*$+?0-t5?)&XsjX!s~nMdn%YJOu&3pJ46tZ=d$aQL^3)kOOI_4%8MEAo4NzNYT+XIUfd`Fgk4hvg>e'
        b'q)e5{twZX+$JyX&imU;-$!;mFd^0(HKzCG6>xOm&Zc%#8O&!u954vhFHwE?v*k(<qtEpk?90bOdp32iHv<fNV*;x$p{9<D`4a$uz'
        b'8+W;>ZuMfm)5ChGHU2N7>F^`HzP35ut=mim>v$urb2e5tI5&hFF0v2eyyfeVCX4i6TGt<4t8*Ds+`P*;!&w(tU~w4}8}d%n?n+^w'
        b'v!gM@WlW}Z%{>0NrO{_mGI<Od2qNXdlc;ZzSNj&<(%5IJU+!1dHp$ym*!)H1W(tY$@2N{-UAWHwmF%5rf06ny8WTkK*2q0;lw|6u'
        b'9k*ttYcumwkQpsyPn56>A&wh)?5Yw1U88}6PFH*<(B~os7sPLdkS5d@9!Fv!A}#B}Ym9!Kn;hAwUBJ5r67Z9ZI`LT^ZK*vwlTJF8'
        b'jqY4o^PSFw%%qr1lWYyrfs5+Ifu$xq2f=b|N)BGv-tI*ub$z?xrEY!wQBP9+=XEOHsOIZX6%!t^@Ul>+i;l&-u3l+P;&mvo$~rwy'
        b'T6ICCm9!XB^Q^|HaLj%aPw}RyiQhH-*Vva3l>ugx<*FZ3(e-7`>)q)nJtmZ%<bRo-|AiZrQnF50H<iBVJrWJ?8PkqF%1b>YZqEPP'
        b'GGLeuu0H(rCOR37=#BUtCS%{<kpSOV-C$z8k#~s8377Y&s_}eF5!*1Ioo^rWXh-t2v}HjTk!&OUzN$-Jp7s9%-xT<~yvA0<v=|eL'
        b'e^D&yHWpD`?=eMp({~O^*uBmX8Bw22OReU}e)ZdTJ-EvI^zApVQ5V==v(x$cvsc-kx7)n)M?BiGc5QPbkzylieFG0vU2xX00bYae'
        b'TTvWL-2=Dl<z@Fd%kHz^pDKRr%EecrSnDKiiZ{AfxCR&;XJ@w)jT^xy)df9@{?CM}aU3yCMP(Pt*PsmNED?F_Hkzo;Jgs@3&E&|5'
        b'?cC*ztRjo&sywwBHL`qb8avyLH<a_dl4a+Q<!K42&B<<I*#xUB+IMyJN#;t)_cyEmWxf3CJ{ulhqw?>1IqB-Fq*X!JtTDWF;2=_s'
        b'wT<WdBVoGwHvCJw`bL*`WTOi;fZ9gMRToootkFBt+=vETs@9{St#lDmM_sFKx<x6*ix(w|2&4>O68oyddvuWlO_@~0^4XOMHFCl='
        b'L-B?w*7duXOl3@md_+okjm*+_D%ER_+&oz%E8Q>=PCN4V6p4M-P=x5UA8(`;J!?eIRF8b!c4oSN1@=EX;y-9M$r8Kdo5^{~MiM2b'
        b'L)tGTQrqA3P^GU=*5Pl$6~+@?6jA!ZWbgrxY@P}qrj+XLQWD2i9nwCEc=v^b`WMt5T52vP@Q%CV>W^f2?|*9hW>x92iNf<?U7wy6'
        b'UO5=OBuvQ!G&<k=`PL*wY7;H3kq~p6Tv7?Gr`0V!;?a$YJ$>doh}6Aw3fmq~?@mmTBZWHW(7neMB(a$;B#4}&FRC|owJaw3R7C3T'
        b'{50yrv>%i%oD@HB-KUbA2)>l~r-|B}4^vOg^*G-Oe6~YEr#`w#k;-rEYq^8y|3>Ih%~Om0DNR{t;7MA}R}RQJ$Q6<m+7-FSB|UgI'
        b'ib+dX;=_RCYbxa?N!Halge^0G8dYVaQGK88V!+$F8w}$tJI<KbcG|~T>G+6k+$LSynLA!~*EqwhWr=aNY@A&;&dAr=R;^`k9cMPI'
        b'CD^r0;o7n}<BW9ex(#ashVf4AIH6fvmOnm5j*sA@1fGnZ$$<1kA6dW3?ZRh=sG|MOh0X9oHIpt&Dz^D@Vvw{-inVx6>OnPs@4|Cv'
        b'N}r!Z7G@JB`l#fR&O(m;LCfpM+q~`C;(PIvb^3;(6HR!)p&mRJ_)5zfH6!5_B&tVtW*)jYk*zbo8Zdgj>{l9myH=Ooj@@S?r`TQg'
        b'xW{ydxU5yWR3<LUCDD4;gTrWytkNY_{e$&r!Un-xP#abdX0LYvUdD2pI@!CsUJZ2a*06iApWP<0hoSLLA6?24Z&488_>_r*m&L_E'
        b'U1x*nvrE$;`s}LI6`m5r`6kN$TiN`|g_lwG-%QFfQ3E=j9NVVllMZ-Hi%?>BuWaUzp@G5M97)9PX>sGAyCNadWTB`>g!O6FV!m<U'
        b'id$7`6&pcgvZUD<wr3m9HvBdhFW3B5&KifaP0{Cx*Nw*)%oNSjD<X3MT6w{BAx(*O2fP=mK)aw|v-Ea%L~i(%tUJ)$h^FdzDvkWl'
        b'cM@fSAY4uh{}MkA2tp3NCIn$N{*?$A{OUZ3tS1RVLa@l(g#H+8{|teGQ4;)Z`+w|2f1hrbFP!U_FJ#c4W)30JfXvsSzcTc<BAX!I'
        b'H6wY0u6LOC|M+F}=SP2D^p|6&%lu_znbJm=RieLBEKzofA<8zOcnBQV-%$z}0;Nn8lN#Y7x>pheFQ)yX@N75_&!9i#QusQ7pvxLW'
        b'v#*8c!*)MLfA5PwUyJ!VCkSuj-z)e>gWRKR5;o-a4)pinWBIoG3>I6xKi_tEXTFW^%D4H^AN$9ATf(36ZI>R+w=L{Ie`<^EZgd}f'
        b'a{rGB4M8yf$hUQVoNo*KdjF3*DU0ps-}7xWGJ6Z%zlHLN@<Mob$rrZ2hRO*29YxpQpueJB`L?3{`L^?+eB0xwd@9l3J9EP4(jYBY'
        b'T136KvoAqn&9xe=T5~xuI%o1u%GV}r+PR$Sn<2@VGx-qZJ0~ngw`BzkG8xU7{2AqI5i~m)S2j_C%#tLnvnRa;OnyR4I2fzMl6!}W'
        b'MUz9RoORyqbe0tvY@Hjn%H%fN-L}rMBCXl$w0Sq=V}tu_-ZHnOA+RA|C2wfBuOU$8@E%&U*w}YwWTDn(bREdE^Jr$@-|R-}%A&lH'
        b'I_&~83eoVsFtSLC8ghF<Hjlr2&O2UJEXt$LI=q_vZe^;mnO7H-&X4TBBIq9+kE7%1V{~eZ_aW{N0)8O)Z_|yMv5|d=uw<!#SFL5`'
        b'ONEj=+>xy^`@ahe`=97?xy+d-DO;u~39n_#M5FQ|WV->Gdh@hV3wwdE<hF1)EiD8JhjR$ttDY>%B|jD%f5H~imc`vjl-N9)ut@TR'
        b'O}@EV_~d3`%%d5ZZW_uHdh>)KB&s5&94m+xB_54;y2EL~ZOOt;x>Y56HQulQ!w;+cDqFjTZ5Q_ns6_j*y_%7$_T8$Xy_&!@_sSmW'
        b'Si5E<>?0gW+B4HqLdVf}()Z#5EfmZ6&K_ynGj!ZwEH<)>WgH_cQHIL~<$sAnm?|`x@Yz|i<}OsGv=lY8u3k-t%xWK<oXBq`YZeez'
        b'JDtMi;vmBR-$K#ZnR>N(-(-tdveZkktxa9t`?$G+xZiu{#Yx|{leC^Q3F79S&Yv<|CcbRn-o`z)KtfA9Bzu-|Mln3`e>(ol_~Y?|'
        b'@wh#dbBUr+9DU>QxWTxdcx1FPkJE~Va{6X^=9lv0@<ByU40fx>#uL<W#h~KLu+euuE)E;EZQ)e-_mXd5%W?T;`Phd|f!e0p%~bx6'
        b'dfsf3@m%eK*E=MfObnOe#wYPU2t8r3XX?qCeS$AAN!RyCTECjuMuq-7+57gS@9oJh?>F2f?C`9F_>!WZq95#$;#7Q&&FEiFNKv!C'
        b'H*7SDjeM_9($eKrS8oz3RBO3)$>`@3m9n2veTk@u6FOw0rzX6uOn!<K+Z8RjFk53ON9CHCfKN5QAZ}mqwN7G5focSc3cFR(Iy!-*'
        b'gm1D(B1(zYlM~*T#UPL!Z+A9qxW7{FL_NQutXtB_Zg}h$^3KltI$5!6dr%j)H%*Sbq($9$K|AWgi};at?ULV4w)6D)H0h(&irSl`'
        b'sRhlvuYNLZ-*T!)f}%j8sp4-F^%M$UvZE-sX7WdVTl?xZ>0Cbd*-0C}x=uRUCD>h)Z8E<!qf5x;CflUB&Pn>tvr=L(7FDF!%e}Zj'
        b'avz_h<B&0GsSk#YU%<w->wjwBFj;j<Y?{tU-_Lz`lEz)OSZe>(<TW<-2d}$-;JW)Yk^5?VUnkpomMnaZu&<h2Vx5e(e$gSbP|hrt'
        b'vjt4<y^}Hbk%~=tOf8ZwSut5spb1BvGr44W*b{fxWYnK1NZwsf*0>1!(n(v`R4JM|I)rQQUwsDM+ZRtx8OfFuPjbcAhP9+HdLQ<+'
        b'<koBMWmT=$INyGjRQ!^#=b@+>yL5Wc^Cqi4of4k&CuvGFE{m9Oi*RXg`QfDfhhm;o+z+CuSBU}J=T6T}kuujb$%acp3}0o>h^8y-'
        b'etK3__8YGYEN${y`{e8F6R)$^PuXt~CLFK+T{NBUMfKqMYi{iqCZhMbvdIroHP0o)O)pg&Y++SU8s7ADWg@B?hVRc$-RFKeVgF=8'
        b'^kfSwlhWMJChTXgH8OlXK}*H;5yO`gRp%lrCE>>M{sbC{`yUYqdkCe5nO5~J#I^Tm<jrFWs|0%xC%eA^X+2^r^s^|QnnRJfqVL26'
        b'ts11dyz)mk&ETmyNr^!>n$9<G%MxFVN%bsl$GhsT2uO1+jLbiMM<y~p8J%`E=%EQLT!$wjE5g_;yePiq;KVB?Id>4-h|5HYj|&+W'
        b'PPVEixdYg&<`ULbJHL>2_Q+gbiP1}RnyQ&D#;|V!P1&kOxAftXaj6KWb3>v<2s^}+>dw0A4$|4pv_3bAFzlHyl0<!<Z}&vSnTh&E'
        b'To(?UR?{m-Qzy4kpS(5^dTpZ5`|F*rO>l3BX?-34Uq4=vJz3xW$*U8g9mv{Mcu~NcDF1}*5>q6trpd%T#3yYNp;lyD*Z;N9`j-F_'
        b'-rKL{lOz5K&Bc7%{CP-^6NgE04&)~BhUGd@lb85@bI2RnGKg2iOi3TEzc_@gH{}iGX+<~MowprX;1Sy#o~@g-oq3w=c&0y(>i;fM'
        b'Z?^iI0?V|1vSc}v#<P5Y#@m0pDSQS`y|3y!r-$tnXE+{eZc`}t$PlX1X6(W`v`iEFw-3zw63~EO5+3lafdc%92zR{V1q<*d4cz)H'
        b'6w8Y{4yWqbO@^aNMWzEP9MvXY)wr{r4YX@|`9opdqCk85TXCToM|u;F_!5tFd8;zalJ{Q1OKoj|zi2||KEUlb1;>xNdI1xOH)Vkp'
        b'r$mfb6^U1M?Yd*d7Xr?7ffnW4`?3>doKCtOjqgemxo6qR<wH$c?&1f{jm~8ny8=hTTTvu7UV|Ls{n%E#uh@*!SWN41H_H>}to8FV'
        b'6K2gC<H`5(umijglGhvVK7=OUI1T#3OTu+_Hy}Gk5#2w2t>u=FhcyL~23}(eXF(r%?oH!)XG>Nxetc~4g>^ym1Idv&87kLPqK?K|'
        b'0(25~!{di$*OWopz*wHvP1=eAY(aq5<4tLKzLFBWI$5Nue=gGXk@Koctc67#9(PvM_UQU9FWy>Ec?h3rRI-8d3}@<<+@FUt(@E~t'
        b'59)MQlGknN7&df#P*Nf*Jtwxn${evBX4>06Xb>fru`)AkGPF!<yVk_+``~($7yrqm`Faz_t5_an;n+-(5F<B^KMB(vUh7XU3NO(>'
        b'FB)h>*;}%d5jVYSB7wh5L|sJ_@W}9WCRkiv=jP!Lt~V(-Jl(`xnG>D|8!MB;v+~?EQ{|%zn~W^eve%mA{`>>F_<FOI9}orq<Z#&s'
        b'(@k1TX;r(}c1=lpcpq_^=<3FXNP=z@A7rGl9!<%LaOTq@!QA#ibW3tHVEc6@xahJ(;Ui&~^N~>}d><}anhfW%aGwx<_HH6eTT~?_'
        b'vorNSOspm{(-&pttsVUWmxbAsX}IwN+cF80rzyEBoRUnN-Ht9Cm2<-7h26~jVBNKDL<gq+3qr(!<^%8dILNB`Dm-psC&~|ozQ;*+'
        b'|EQ3u|H+Q(%=BNb$*ULL>I@`m&It|IIM<2JXDU7xB5p1mMsC>eag(43McsUb-IRQfn;D9MsGCo*n|0sgCQ<RW5GlVc9~=&@5}!Eb'
        b'grC?}CMzbQG6dQC@`jI{5bJcVH}b4%u6Uany~Ur3*G=1Mu8Uge`Y#Dr!`TxGo{f6cL_J15Xd)iQr|R{LIUK1$Kg?Vcuby^A4fNN='
        b'd?W3MTHRPUE$(B+NLa+xu&#Oy?=^EHcPuMA)*`MVWg7ZIwmiI#owbBzVkQ=NqMgq0{9)!AJ6+_NHQtCEd>~qw(Z(7MAEzVO81BE~'
        b'OT6JefS+hZ-UB!;?S1BO>1?9+>BGKf4xf1M68H4stNSp6`rKb1Huhbq>aSnQ>&m({K{b-8S2itm2HE4XKtLuw6F2FYOigwMawqO('
        b'#QW}kby$@3j=x;0dXFth=q%7|yUF*9!(Cn(w+4q#OCt-t=(h1M=eKridn*q6Dh{VD=6;Ut6&D4fZ{HPHj->I`38xc{Tug&o<M2vs'
        b'9;TDmc+wo+XPk|O9(nC+Gi{e_X>B%7fKb_-4O?>LX)ly`Sliw}=TEiG%a90Kxzv#{Gk7@klf%6~K`Hp!_mjh;yNTkQtcCmMR~_7Y'
        b'$EIT=1)AGusY8nn_uh^ie2cnaU&YKK2R(yGwGkiqh6?Z^O|fH73tlGrop1R{dUnI_n8o*cR&IQ5zp^+<5sZ{4(~z*4tpCVoIZQ9+'
        b'at=pc3dk~MnLUn{zJ$JEm50hvKe|a~tem-+U))~1?JJ~aMf67F;f=<t@6Tpj7JBC#-Z|?q<6r{&oO@oIM~$A2?yE^`%5=SY#k^07'
        b'&qh2ml;2JE|DNdb(k|~aox2{%w~z{ka9*~hwL2F~jiG9O4<A59<q3EKY3cbMQn8T;v<C<ZA7Y#%WqEdS8&*tOs?PaSusTzX*TYIL'
        b'NmD&I+j%~>qaja|c<u(ap^UX^*mJhD?^sV@aafh$^~aWnt{m!}IMn6s_gy&D`V!IUGSDi;X~D^sq1m7lMSad$9q4S+ZfqChF=x+A'
        b')TbQPSG_+rp?ULdb?ECuy<Z>d^1WU7wQwqLAU*h}(3wNMXHbBL`cDhN9icA{^?r`-4i|nVe7<o15Bk>5oU<)^<a6!m6Leb9&m+p-'
        b'xN{?m^qjh%2T$Q-Z}T;@vu=mCP1ELx`BEMF>!IGiqBx!?JR-Q>(`?#T`!-qgW1{My>%A)n_|Crt#$Vifbd!JNxaPwYbtrVGcNjTN'
        b'SG*@I{%iB`i>Qsff2em58D$ps3rCZNh7uZ%Gan_<yRiqWIy7*o_Z?(w>i@Ig);BaHbna$$>)lE8+=l<sw0j!&U-2i`sXE)4wq$=2'
        b'o!rpOc#@F2|I##XLv~gbZ5541+BJ>dXSQ37gc_d?O{+S0YuoqYb;7RUxiioFEVS)V?~AA)zE-pf4db@7KQ`<Qh)%cUs5{%)v=<s)'
        b'2o#<bJ~Cxl>TYrUVrI7kwE<KXM}0$k88n^Q?PxaQ#Yn%8Uy9$GU&`yN`kY2hb`DR9FWl9UCVkZ@e0H5au#mw$m6p~-<#Xbp*{*$;'
        b'8cmW0uPpI25vo7bTYsqQrKf#Q9IAMh7=HE2kVo@z-U4fpp3XqCvts=~Qk|66vkMt((mmCrVm`qugZ_~7P%npy>Su-D2&a-_zKRV!'
        b'eW<qz8T?#<_uvivO=I>xGt_99pg!C+lbt|4oE3Zc5bEKwv_IH9EGq<xEEZGnFQL_kdROCCQu8<DGx$=d{7~<I;C52;vC#Rpws~)H'
        b'9x6NQ>^)tMxifEfv*usSoYRy&@*hYr&<VI)Uh`F*b1&=M#Ww8K>|Pf9g1FH}ocE38v6md|k2O|DuqU+qQ15b-xJCW%2t?IBcAMt3'
        b'XR*hVgcOcucU|&8Qq^BJ9kt!7`S_+qc_;z@eyH~+$o1O7J*XMPd`>Ddh~Vp?#fN%}k?Ak{UlR!1=SY}6GlKK?8IoX=Qxa@Mlwg0r'
        b'5=;mz&nrq#9Q`KowX<SAR?Np@C}U68(z!G5X<{8HAJ6|^^09c^X;0O@aH?Ni;HgttlB)Kj8&uK_U52f@lG*Q2V`9a|)X=b{#hcva'
        b'Wjc4WY<r-yS-Z!BXTpu<teL@Gp)13^SB6mw?B@i+irZOU)n9&e3sSW6Q6IT9-1{xE{I=#v!S%pQi-S(at*zLH)N<7Et&Vmhma86L'
        b'_tJ(J7|+s(O#2yGzbp7W-ZRzuk$}Z!=^?`Q8dK8BjCKm*8@<E(E}fcH)laL-p4O~=>CFVK@h{Rcqo#bv`*UuVBk9-K^~lJWtp4wz'
        b'&xU)y8SZ-NkG{jh89yc7%qRPQOtjzcPOKVmW@#4JGQ9Im3mNlydJh`EGX97HPaMD0BVG5G)!g3q@$On_hrA*rh|P%z_J{sD-22yI'
        b'T%BLw_Vs4yqv75U(fu!x93oIHGA_d$REKA6X?`0Y5Dzlnk`t5mhjl!z!=jtrnW&BK8SdSK%H&WX{>oplEz~{S`^GSqWk-Z!t7mrS'
        b'PqZ5g@bmoJ*3X`K|5mo~zM1!UvPXWUU0Z?b7D=|}eN`9v(uS?9)1&c}20stiZP9IGkFo1EXr8!j@o%#Es=m5eNI_`lO-WUU@!_XQ'
        b'rdd@dKT_h$S^O+#Kvusa^vB`e9VqcNif#c3US4B-Pcx^RthtwHe_?OdIKS!hF{7rF56rni9cmozZA4Df3p)f;GQ%V|T})jv-Gw~W'
        b'n$@Ar!@V1av8-zqOta|O$iB0S**(jjOec9?)tqi`IdH|4;-Qd2ot09QT=lW{WzATD#@WuCp52y=bcMvFr+Hn>DYC{$B))ul>=Nz}'
        b'V=lvS`r>OzHesqT$53G^hP}yUs5FlUD$Pa4M8y}0hrj6T(Qe%PfY>84_q@Jp?#%leb5W1D=lQuKccNmXb&ua2KDb}pez6V-wY!6t'
        b'@Ck9lKGSVOYuK_?npG9D#T&<Qu_dEo+lWfgqckN~4KVn;&S#u0hT5)~3>voDndmT?wk?P9`dKCz=&aYa^Y~TJ=ZvPA!IqF^xYvR^'
        b'MByqSD{F<-V{WXRX}S%`-836f<U@rp64Ykhc3>Iq3B1q0%(;=NTQ*Nxb6fZw4`r=RW$e3T(uuK8?aiY5BKyrE`!4;Cil>B4`?fDs'
        b'n9SMj+ZV?97NAHU<j&(}+nPT0ys1OlI`xg4(i21|cepoq*k>Nb4<NFM(F(!4h{+fi+Fx!tkg$E1JiJ-UyzdOVi$QA2=wm|5Dp}%_'
        b'leDau%vddWUkbG8tmd}xt196=W%UcHE>}D~5#7s6)~B>?nF#MONOpM%R(v0)^pupTt1jj7M>Sfn2!2P8G-HEs3$?Aibxh!OUVorv'
        b'l_cYA_>woa>1y{#+Kl0oLfCZt?g}lPnin*BCHOFcaKK4Y6vLVBu6>s}$cnFo4zl%v&>^k(0tMCXZ_|yQK^HwzeCc<zK9B9cjp|Og'
        b'JjO!3V<F#Hp)T*qjAY`N6v-K^a-BzMi|C~&WSovu0{(wYU|(WdM}?nJI17WajMs4{p7iThwzugzq@({pu@xCn9@=!b;~b#qz7qP+'
        b'gmvMxAg#vl7A(efl-MZ80e*qXVzf-yITT{|F%`wa@>^R!5xmP>Mdpk<1h=l?*?<^aNqe9e4FPR>k96B>+*b!n&fD;*hR!WZ2X1se'
        b'_mcBDgVR}tm7R3)vo+y1Qh%7gEtPjw$oPs>zOG`{7{3htF5@%uyU$oN`oF{T0&8U5yIyBBhQAZ?31RFlpts>S&^W{UqK4k*HFtRl'
        b'jgK+g?=;*0olC{W+{>X6uh#jS84NG+w%Ad3PNSJFrsco{=L;cw?-x>Uhs@l2XOEQL!EM7voF|m^iNPH*mus@VsSBBV=hI|YIu6*_'
        b'C*cg($>O{<jxRbSt*-I#H?3N{XXv+Rb-Rz7Jc!>^^j@TQ?Ah5N<#_D6wc=9gT6yl52g~OjT(JJJn@K};Xu<san{TpLhZaiB_A@Aj'
        b'X7A&+f1hEtf5{Z!beg?qZ0$@+UY}RfwU0!pb$HKk|A_-jDaifn!Sd9D3vSB4nOyR4DEASRP;)TB{;QC&{3gTtQ0_W(akJ5Tkuf-p'
        b'<@ttRh8*R2#&V0{A>?qrv3!BiJD@Q-mzG=C_sw>A3A6XzO0q-2tr3gkuGNF`MZO+INnU`Pjq|dyAn{gWvGK9Sj~3Z!vO{7lATk~q'
        b'pSA}9Rps%Ek-i%_H|PAtYtGFX9l01iYePEvanvnp{(p~}qxOuNT*Wuj{n_qv+45S9UZPYlL4#_=hsb07+8#M~OK9qBjEdqbs4`KT'
        b'9K8~Ltzjx%96`%^WNE<;iK9G*bK{)Q7MGoL^`_P3y1ajIEuna_N5UtCzn{ZDywen-b$hxy9o4qZ4QJ*$=QbT1Zh4h(Hhk;#YwQIF'
        b'(R`iYwG9pDQTxRw8=-Dz^eOxCo=Fs!8pqUyVtQJPDJdEgz5Kd}f(uL!<89cKc#Z?^Yp7ju>##4E_uVPS;)l3!9<RE&UktgJWjD~3'
        b'Y+aLuM2;<b{IU?5(nj{faq$NmjS^Ips6cByWb3n+qWfAog8R*2es^5x>!IGUA>Y_gm-lxShXovXhlDG^VOzC1QZovZOyezjmtER}'
        b'59&c-N6w$;o)-Q8eW>@ukZ%O}_f-r<{oBI+&EBKe1|X&_;(yCigC);8Yj?+m4h{7l8uGo5g6PNy3Vq%*{E$<^{SXIItfgl=mQY3H'
        b'QoE!mA?>-PcB$1M1|*Brx%(0EWU+li^~vbJItu-F&AWo8#+X%l8zYNZouSUFUzJ)A{-)F1g0l3!RAZUZWtFqWz#USyV71M-8u?0e'
        b'O!h~f17N>en-lq+f&3Pwir)*ETW|+yl{2$Nw<e)K@*W4<@U6>RY4pi!J+WNRAez~l4+Ur?YpR|;29^`z>s-r-U^_3Ni^otCLh?@<'
        b'?Jqctfk+sQL;n;8ziP`XgF7?dZ*Xfm$TyRfXeep)&ZxD<_wqwK`Jv$!BI8*x>-4<d=Z1DZH&hsY@4-kWrPa~OIlD=hm!utx_>l#C'
        b'e$pyBrPFzyCY{;%&GTTJ;mM(F6VqHhPgVZ}O=d|An-3zFNZW1qwMoOzWKKC)RyN{1pJ{sff@Nmn<4Rx6!8J*C?!h5?FRvU{%IE=w'
        b'mdGs1d!y(M-!li-EYIXBP}P2c?a&B#hV5=jtItug15LRP46<J_e$qsl&PMioaz8~*e}SE%ls<UXDXtLiZe%A$fx5<9g<lHXPlgtX'
        b'_tJ#}h35tCjv@L-_*R}~sTmXS{*iEVT)}bM2F2GIZMWJTc8Q~xDK->QsA(1@^hi)cn%Yaq9%8VB_2MeJB1GGeMDi4A($VTwM!nH^'
        b'!@BLvs`42qy{mkRdDQ(W(jXa>&l>CV+Pb^~?wFhySIh~+3==gdHw~k{H{5GO9{LQL<5YW&KW629%$n6ED)4;3)Mcv)^hg@Z6J6yA'
        b'$VsCivCoh&k80TI#AEKeK`aLh31tO=Mawqk-KkKV6mWVT!s(%mC_Uu~w2Ic1G&VJ$>Z5{LIL&v^C?y>@Q10hqS`;S?2__09!qhS-'
        b'?~$Q+j#DiL&C1yyKe^7h+O|I6eK{}~gY*sGaQO_b9Y^X<q}2m^Ius)`PSdbqM(Ox>JW89!WzsPPD9Ig)Maz)8C-d$k(L@8a>mnn6'
        b'A1%8*X+E9mH?yx*_w~w<{q4<qi}v=rD2vf=wmgDLTPl{e(HAo(1<50!Lnf|65*^C$Sw}u%%acLwiD0<qJX>7lN^Ty`1kH;wl&Q<T'
        b'qZ>&&KbfO+*%M7vkHn-C8;_ss-lE<}CvUgl&D5QNvaQ=>RUg$_)!e&y;BS-e*5h~;{o=bmVHu69Yeu+fxV&qyv_;{$OcG>rW={`='
        b'g*X=*wf98qdHk*4-~nFOLAsM%rWxI;YvfJ&;NYrEVosv61-B1uTE6}L9{J;?9kP)a0%@g>E6{K7Ia4A^c89$1f?!*BckrHtm+pwU'
        b'#}a2-R}j2E?b3QLbB{%m7Q<)a_r%w|D~?I13G&_HVWV`xIDfNfhQHOQo%&W|>7Gkh(^ZTO+As2j>y`z?s(P}Z@Dp(z$)$@$sarFU'
        b'K`UKLq%N;>i}U?DiJ#=PCJLWh_|*GG<BSHLsnenwn>x=+{AN+<KZwwy@Ap3TzVEU3yL=C3JS@13l0j5x$#g0%mpw?VB|AA;1JAmq'
        b'#<lQxxcgylkJz@zs{<mByCI*{BM}GPc~qS&`u#OcFVp3{39Ap6g=5W&d+DDdRr#_IJk3jt5}A|NI-Tbkl*Fj)9F#6ZE;7CoBKzC1'
        b'oNb*HzE{o;O2yDFMCTY{zgLR=zV$8PYF$Rnb5X#1r<wQWyuUN&eI#zN);*7ydQUyNAJc-W%Cbuw?Scm^s6u$XIekXA5|7M!TIsFE'
        b'lYk)K_^0va=7#F(9hdy1g|g%!YkobgXHl-!U#-SuECYOs+GYyR3Ha`*k8+07QiS3vdQBV<g9nOmTnUcZI4&7MC!n~V72|TFxEh+B'
        b'4bN7;W%8r(vWRlbmLVsW^>l(QkFl=5no0{whS{gcZ>B7|9$6$C|9`|M|Ni()|9yN@1<{p7U^$SA;@EUe9Gj}&s`Qh`<vcYg<N5Fl'
        b'nb*X#T#V<o|1O?#Vp@MjI@LAjG6eaqKaKBcM>q9uoEe_t9~V0x%7R~Py7Q=DyGuf_mVnEL4}O}OSN6z|<I1b=u#^+2x6*RkT}`RC'
        b'(KGyHCABIuZbU)6l~So2l&s23?vbNpDTreq`z7A84PLM8%pS}7nAP!BCvABe>-w^C84_V-EloJM%!HmwBvvbLE_t0ne$)jDG=DUv'
        b'6_(w%nz#7PJqi?UrqqK5kJ9<ywfJHbXT^8wbg^iPJ1`=i=CFB68wkI%=2M7$hj%<gx(2S$<OS1wEb7HE^2|nFQnH-6C&|Dk_E3Cx'
        b'*(<o9QGyj>Ia(6yn=QNORPh$g+VsZs8C@oPS`?BXW-JTyo9CDk=~Sap9X6Z_x%BjvN{QL0EGZ3?q&F$h*j;+ya?QnQdew^&o#>|r'
        b'|4Aq6z31T0dk)?ai~95VYx;g~r0+YQwNLN+(Pt4X`)#AQ4^`LJCZ*d!k8j1h4<he&g!?f^Ol#h_O~{BlsfdQlzZYpCwnz(U`O|oN'
        b'0lL{%WWVWPz1}|mpr6EwD;hA05|B?ERME>_y=h{OgY6DU8aqGWK&@qVlPDvn$&6d5;Az}$i^O&-6HRd6Vz2hC<|fp&5-Vkq<lOh3'
        b'C|7fn4)#c}%8i^`^vIuOeFquo2I0<@gba}|xrGXg6IoQ8gumbWzw6unslJ_fDw==-oPZpeRf`gFY0zO8XAUUu=5&d}EBT(3beW|8'
        b'U4Q)lk`}|Xv>f^0rG@<O({k-tf1L<IB79SIBGNj;u}i{Lf#xe#LykQ6jlrdn1QcuW^h}KY|0bKT&W#oBZcSRUul>E9FAwHy-kPMu'
        b');qm}X?G%Bh>qyccqjk=ML#@p;Qy{48V~%x&<~Mp=^J~)7#I4_!QMv)eUA=yc}pw4oD?65k>dLbcm|F2KW=>gmhbla9bLVqI?l7D'
        b';!1Q<`9~bDOM-@zF}Jqa-DoFAcx{fV(Jn=bAWzv>4L0^Ne3B;@bvscgn;dCLwT<&koO=ty+nsF^=SId?dcezTh&C<L@NGjg<6C-w'
        b'VK#U@8l>zXWddoNeva00C0OU<OoOy)<HqporonEnsVTV1>$kVzbfT$#_&qisJ_kUGy0w*S{YL1KhILA3IH_qlC~2f0r_(H^(nOhi'
        b'8EdZ5C^5IoQKQi8#BwmWz$js|WTJc$!;_)#in-P^0)AqF!+S6qo(#2SG<`v#7U!Z+?Q;f^W@=B22pY$1JexUoz$IZala!gJq&6v@'
        b'?54?zrA1PcV@`q;&*^YHX$ghnkuy6YI^B%H-o!zl2Gz^f(L<B}qfYld@^jBL`DwiNJ!Daa4@PA8h5e!o_x{t|SR$#^ZFy|}%4gSS'
        b'>gm*4s{~ECGH(#aLp0ZVQJib3f;WkW=0w^smnk+za!_7L^~frZtouxyYbhdgtq1+&%4gkF;AEhTU+vzFbo=rdC(09Sm4Oizfg1gb'
        b')S#k6dU|JLc>?#~esQifV{M)j&$b#333n<B{}G-mRATXyxGEEi9|cj`EbF2AylJRrRv8ISj+4MG*pGUAj_P)#wbxk<s8JSc)6&r$'
        b'osK)dqDNxUiz8!LmMu>(&kpzch+cr@U6+?|%vOsMuar_;EAmRmr{XLkxl=f;TW;9z@-q2WG&Mo$wA8B2Ny@iM(6k6C)H3m*5uSh@'
        b'Tk9u_DA#OlX_DmXm@+>Sa}m-g2c8voNKWDxApa>Hi>^<{0y&-+p=3Bv*89bDTp74F9WL)N@$P6OC1^rrdztx{X_-AeEzeI&3u-sa'
        b'w`T9xtPzd(W}lp~REy)(zj~g5WXJCgq*3DQ4Ler{uX(3}UU2R0f#_|{9jFz3Ie^c$f9}AG659PJujy7T#v3;M>OlC7iK+9l@PjG!'
        b's0zQkOE0FWQJSb<iY`(r=<s{rt$G3<N9-k9V?;M|X{wdNZsyV{85HtPBD>L8B6@Z-ox&}^Ga}>`?^U(n>qN5zIYRRo?q+<;-4qlb'
        b'{dJI|-w9%;#b@Dcnf%^&RHOY3g_o&Ui<`UTnR#T!Zzj3f!A9>Hh7Z{I@Da0aWfdxesTWPA`~}a2QiHvzL0@X{UNt^0y=ju05oAmO'
        b'n^C()Pvu@2z*`gXqNlov&9$rZh&rt^56!L^XC4#XKg6kmD5$HRzQ&%+s}g37{R>agv@=E0R3ky!*kUQmY$5V|N6x8{pka*+!<I35'
        b'c-ID@w=v8XrdW^M8vAZ!%>lLupI65eOA}jSVooS$o=Bc^Vu2!^Fz+8Lmafo0kp4s-Q*PHdZHkM6d2q_i{LXoc)Vyz`PU_LOrSHyT'
        b'TI>vR^Ob;H4iAp0Vv}cO&9mNO?nTaq2Q}t>Ls6e~w|eesTfO^{F{h3Bhn;oW`tf-s$Qw!$p|jCCG(MmNqD0YT>=><!Mb$HA)TSEQ'
        b'BI(5wlsXUHTwHaLW#{9qEoLoi<QV2W^1(`_IpkE1Xk)BcuLh$0-wu>~D!r2^%h3GD$cV@D-S(vrD=QH%QMp-2_Oo*q9jnn>jI35~'
        b'F|#tg#lg~g%TkunTUN0Ky=6UX)LUF^x*mnP?%)1lC0UKss$;cMtC5vSt!9>%S{*DSwJv21QtK+#D7CI<)1_8dtoR-(EoD!Z<8n@C'
        b'n3FhKu`eQXnJsKSpJDP?Hf$B1#S<kO;(x^Y*3%jPx%e-N{D*(mzBO%h_45x=$14}jeE*Bz?9ZIRTt1y700000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002M|HB>}'
        b'2mk;8008;FHiD|Es;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80stS8>AOHXW0089w+6bzus;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80sw(WkfdBvi005BxYa^(ts;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
        b's;aaH2P6Oh004sizwSq<00000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000002=}QJLhf'
    )
    _firmware_identity = {'protocol': 1, 'receipt_recovery': 'ACK1', 'firmware': 'CNC_FFST-S3-0.1.3', 'app_image_sha256': 'bc7e25754bc40637715daa971ce563946d0add684a17cfeb8ec9261520fbea18', 'application_file_sha256': '43deabf36a3365e83c1126cb811f4eb71be5278c360f4dc7082aef394929bd70'}
    """CNC_FFST HMAC v1, shared key carried inside the bundled BIN. No unsigned-motion fallback."""
    import argparse
    import hashlib
    import hmac
    import json
    import math
    import os
    from pathlib import Path
    import queue
    import re
    import secrets
    import threading
    import time

    SAFE_REALTIME = {0x18, ord('?'), ord('!'), 0x80, 0x82, 0x84, 0x85, 0x87}
    REALTIME_WIRE = bytes.maketrans(b'?!', b'\x80\x82')


    KEY_PREFIX = b'FFST_SHAREDKEY1:'
    KEY_SUFFIX = b':FFST_KEY_END'


    def load_key(path=None):
        # The matching firmware BIN is bundled as EXE data, so there is no external key file.
        path = Path(path) if path is not None else None
        try:
            data = path.read_bytes() if path else zlib.decompress(base64.b85decode(_firmware_blob))
            index = data.find(KEY_PREFIX)
            if index < 0 or data.find(KEY_PREFIX,index+1) >= 0:
                raise ValueError('record')
            start = index+len(KEY_PREFIX)
            key = data[start:start+32]
            if len(key)!=32 or data[start+32:start+32+len(KEY_SUFFIX)]!=KEY_SUFFIX:
                raise ValueError('record')
            return key
        except (OSError, ValueError) as exc:
            raise RuntimeError('BIN correspondente ausente/inválido. Use o pacote Python completo.') from exc


    def verify_firmware(port, identity_path=None, writer=None, reader=None):
        path = Path(identity_path) if identity_path is not None else None
        try:
            identity = json.loads(path.read_text(encoding="utf-8")) if path else _firmware_identity
            expected = identity['app_image_sha256']
            version = identity['firmware']
        except (OSError, ValueError, KeyError) as exc:
            raise RuntimeError('Manifesto do firmware ausente/inválido. Use o pacote Python completo.') from exc
        lines = exchange(port, '$FFINFO', writer=writer, reader=reader)
        if '[FFFW:' + version + ':' + expected + ']' not in lines:
            raise RuntimeError('A placa não está com o BIN CNC_FFST esperado por este programa.')
        return expected


    def mac(key, message):
        return hmac.new(key, message.encode('ascii'), hashlib.sha256).hexdigest()


    def exchange(port, command, timeout=8, writer=None, reader=None):
        wire = command.encode('ascii') + b'\n'
        if (writer or port.write)(wire) != len(wire):
            raise OSError('Escrita incompleta na autenticação: ' + command.split('=', 1)[0])
        lines = []
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            line = (reader or port.readline)().decode('ascii', 'replace').strip()
            if not line:
                continue
            lines.append(line)
            if line.startswith('error:'):
                if '[FFUNPAIRED]' in lines:
                    raise RuntimeError('Firmware não corresponde à edição de chave fixa.')
                stage = command.split('=', 1)[0]
                raise RuntimeError(f'A placa recusou a autenticação: etapa {stage}, resposta {line}. '
                                   'Confira se o BIN CNC_FFST-S3-0.1.3 correspondente está gravado.')
            if line == 'ok':
                return lines
        stage = command.split('=', 1)[0]
        raise TimeoutError(f'A placa não respondeu na etapa {stage}. '
                           'Confira o BIN CNC_FFST-S3-0.1.3, a porta e 115200 baud.')


    class SessionChanged(RuntimeError):
        pass


    class SignedPort:
        """Serial-compatible wrapper. A separate pump keeps ACK handling independent of GUI locks.

        Commands are signed individually, not unlocked globally. One envelope at a time
        prevents the ASCII HMAC overhead from overrunning the GRBL RX buffer.
        """
        def __init__(self, raw, key, boot_wait=3, identity_path=None):
            self.raw = raw
            self.key = key
            self.seq = 0
            self.rtseq = 0
            self._rt_tx = threading.Lock()
            self._wire = threading.Lock()
            self._raw_tx = threading.Lock()
            self.nonce = None
            self.failure = None
            self._closed = False
            self._responses = queue.Queue()
            self._ready = threading.Event()
            self._ready.set()
            self._tx = threading.Lock()
            self._kind = None
            self._rx_fragment = bytearray()
            self._last_line = ''
            self._pending_command = None
            self._pending_since = None
            self._pending_sequence = self._pending_tag = None
            self._receipt_query = None
            self._last_probe_at = 0
            self._ack_probe_after = 3.0
            self._ack_timeout = 120.0
            self._pending_timeout = self._ack_timeout
            self.recovered_receipts = 0
            self.last_motion_progress = 0
            self._last_status_at = 0
            self._last_machine_state = ''
            self._last_reported_position = None
            self._identity_path = identity_path
            self._recovering = False
            self._generation = 0
            try:
                time.sleep(boot_wait)
                raw.reset_input_buffer()
                self._authenticate()
            except Exception:
                raw.close()
                raise
            self._reader = threading.Thread(target=self._pump, daemon=True)
            self._reader.start()

        def _write_raw(self, data):
            # Windows pyserial uses one overlapped-write structure per port.
            # Never let status polling race a command/handshake write.
            status_only = bool(data) and all(c in (ord('?'), 0x80, 0x87) for c in data)
            if not self._raw_tx.acquire(blocking=not status_only):
                return len(data)  # A later poll will request fresh status.
            try:
                return self.raw.write(data)
            finally:
                self._raw_tx.release()

        def _read_line(self):
            # pyserial.readline() can return a fragment when its 100 ms timeout expires.
            # A fragment or empty read must never be interpreted as a complete ACK.
            if b'\n' not in self._rx_fragment:
                chunk = self.raw.readline()
                if chunk:
                    self._rx_fragment.extend(chunk)
            if len(self._rx_fragment) > 65536:
                raise OSError('Resposta serial sem terminador excedeu 64 KiB; conexão interrompida.')
            if b'\n' not in self._rx_fragment:
                return b''
            end = self._rx_fragment.index(b'\n') + 1
            line = bytes(self._rx_fragment[:end])
            del self._rx_fragment[:end]
            self._last_line = line.decode('ascii', 'replace').strip()
            return line

        def communication_diagnostics(self):
            elapsed = time.monotonic() - self._pending_since if self._pending_since else 0
            return (f'Comando pendente: {self._pending_command or "—"}; '
                    f'espera: {elapsed:.1f}s; sequência: {self.seq}; '
                    f'última linha: {self._last_line[:180] or "—"}; '
                    f'fragmento RX: {len(self._rx_fragment)} bytes; '
                    f'confirmações recuperadas: {self.recovered_receipts}; '
                    f'consulta ativa: {self._receipt_query is not None}')

        def _track_status(self, response):
            if not (response.startswith(b'<') and response.rstrip().endswith(b'>')):
                return
            fields = response.decode('ascii', 'replace').strip()[1:-1].split('|')
            self._last_machine_state = fields[0].split(':', 1)[0].lower()
            self._last_status_at = time.monotonic()
            for field in fields[1:]:
                if field.startswith(('MPos:', 'WPos:')):
                    try:
                        name, values = field.split(':', 1)
                        position = tuple(float(value) for value in values.split(','))
                        if not position or not all(math.isfinite(value) for value in position):
                            return
                        previous = self._last_reported_position
                        if (previous is not None and previous[0] == name and previous[1] != position and
                                self._last_machine_state in ('run', 'jog', 'home', 'homing')):
                            self.last_motion_progress = self._last_status_at
                        self._last_reported_position = (name, position)
                    except ValueError:
                        pass
                    break

        def acknowledgement_wait_is_paused(self):
            return (self._last_machine_state in ('hold', 'door') and
                    time.monotonic() - self._last_status_at < 3)

        def _ack_expired(self):
            if self.acknowledgement_wait_is_paused():
                return False
            budget = self._ack_timeout if math.isinf(self._pending_timeout) else self._pending_timeout
            activity = max(self._pending_since or 0, self.last_motion_progress)
            return time.monotonic() - activity >= budget

        def _maybe_receipt_probe(self):
            if self._recovering or not self._pending_command or not self._pending_since:
                return
            elapsed = time.monotonic() - self._pending_since
            if self._ack_expired():
                raise TimeoutError('Sem confirmação da placa. ' + self.communication_diagnostics() +
                                   '. Pare e reconecte; comando não será repetido.')
            interval = min(self._ack_probe_after, self._pending_timeout / 3)
            if self._receipt_query or self._rx_fragment or elapsed < interval:
                return
            if time.monotonic() - self._last_probe_at < interval:
                return
            challenge = secrets.token_hex(16)
            self._receipt_query = {'sequence': self._pending_sequence, 'tag': self._pending_tag,
                                   'nonce': self.nonce, 'generation': self._generation,
                                   'challenge': challenge, 'status': None}
            self._last_probe_at = time.monotonic()
            wire = ('$FFACK=' + self._pending_sequence + ',' + challenge + '\n').encode('ascii')
            if self._write_raw(wire) != len(wire):
                raise OSError('Escrita incompleta da consulta de confirmação; comando não repetido.')

        def _consume_receipt(self, response):
            text = response.decode('ascii', 'replace').strip()
            query = self._receipt_query
            if text.startswith('[FFACK:'):
                if query is None:
                    raise RuntimeError('Confirmação recebida fora de uma consulta; conexão bloqueada.')
                match = re.fullmatch(r'\[FFACK:([0-9]+):([0-9a-f]{32}):(PENDING|[0-9]+):([0-9a-f]{64})\]', text)
                if (not match or match[1] != query['sequence'] or match[2] != query['challenge'] or
                        query['nonce'] != self.nonce or query['generation'] != self._generation):
                    raise RuntimeError('Identidade da confirmação inválida; comando não repetido.')
                status = match[3]
                message = 'ack|' + query['nonce'] + '|' + query['challenge'] + '|' + query['sequence'] + '|'
                message += 'PENDING' if status == 'PENDING' else query['tag'] + '|' + status
                if not hmac.compare_digest(mac(self.key, message), match[4]):
                    raise RuntimeError('Prova da confirmação inválida; conexão bloqueada.')
                query['status'] = status
                return True
            if query is None or not (text == 'ok' or text.startswith('error:')):
                return False
            # During a receipt query, a bare OK could be the command's ACK OR the
            # query terminator. Quarantine it until the authenticated proof arrives.
            if query['status'] is None:
                if text.startswith('error:'):
                    raise RuntimeError('Consulta de confirmação recusada: ' + text)
                return True
            if text != 'ok':
                raise RuntimeError('Consulta de confirmação não foi concluída: ' + text)
            self._receipt_query = None
            self._last_probe_at = time.monotonic()
            status = query['status']
            if status == 'PENDING':
                return True
            if (query['sequence'] != self._pending_sequence or query['tag'] != self._pending_tag or
                    not self._pending_command):
                raise RuntimeError('Confirmação não corresponde ao comando pendente.')
            self._kind = None
            self._pending_command = self._pending_since = None
            self._pending_sequence = self._pending_tag = None
            self.recovered_receipts += 1
            self._responses.put(b'[MSG:Confirmacao recuperada sem reenviar comando.]\n')
            self._responses.put(b'ok\n' if int(status) == 0 else ('error:' + status + '\n').encode('ascii'))
            self._ready.set()
            return True

        def _authenticate(self):
            image_hash = verify_firmware(self.raw, self._identity_path, writer=self._write_raw, reader=self._read_line)
            lines = exchange(self.raw, '$FFHELLO', writer=self._write_raw, reader=self._read_line)
            matches = [re.fullmatch(r'\[FFNONCE:([0-9a-f]{64}):([0-9a-f]{64})\]', s)
                       for s in lines]
            match = next((m for m in matches if m), None)
            if not match:
                raise RuntimeError('Resposta de autenticação inválida.')
            self.nonce = match[1]
            if not hmac.compare_digest(mac(self.key, 'server|' + self.nonce + '|' + image_hash), match[2]):
                raise RuntimeError('A placa não corresponde à chave local.')
            reply = exchange(self.raw, '$FFAUTH=' + mac(self.key, 'client|' + self.nonce + '|' + image_hash), writer=self._write_raw, reader=self._read_line)
            if '[FFAUTH:OK]' not in reply:
                raise RuntimeError('Autenticação não confirmada.')
            self.seq = self.rtseq = 0

        @property
        def authenticated(self):
            return self.is_open and self.nonce is not None and not self._recovering and self.failure is None

        def _recover_session(self):
            self._recovering = True
            self._ready.clear()
            self._generation += 1
            pending, self._kind = self._kind, None
            try:
                with self._wire:
                    time.sleep(.2)
                    self.raw.reset_input_buffer()
                    self._rx_fragment.clear()
                    self._pending_command = self._pending_since = None
                    self._pending_sequence = self._pending_tag = None
                    self._receipt_query = None
                    self._authenticate()
                self.failure = None
                if pending is not None:
                    # Stop the application's outstanding operation. Never repeat an uncertain move.
                    self._responses.put(b'[MSG:Comando anterior sem confirmacao; nao repetido.]\n')
                    self._responses.put(b'error:9\n')
                self._responses.put(b'[MSG:Sessao autenticada renovada na mesma porta.]\n')
            except Exception as exc:
                self.failure = RuntimeError('Falha ao renovar autenticação: ' + str(exc))
                raise
            finally:
                self._recovering = False
                self._ready.set()

        @property
        def port(self):
            # Preserve the pyserial interface consumed by App.update_indicators().
            return getattr(self.raw, 'port', getattr(self.raw, 'name', 'USB'))

        @property
        def name(self):
            return self.port

        @property
        def is_open(self):
            return not self._closed and self.raw.is_open

        def _pump(self):
            try:
                while self.is_open:
                    self._maybe_receipt_probe()
                    response = self._read_line()
                    if not response:
                        continue
                    self._track_status(response)
                    text = response.strip().lower()
                    if text == b'[ffrt:ok]':
                        continue
                    if text == b'[ffrt:err]':
                        self.failure = RuntimeError('Retomada/override não autenticado. Pare e reconecte.')
                        self._responses.put(b'error:110\n')
                        self._ready.set()
                        continue
                    if text.startswith(b'grbl') or text == b'[ffsession:reset]':
                        self._responses.put(response)
                        self._recover_session()
                        continue
                    if self._consume_receipt(response):
                        continue
                    if text == b'ok' or text.startswith(b'error:'):
                        kind, self._kind = self._kind, None
                        if text == b'error:78':
                            self._responses.put(response)
                            self._recover_session()
                            continue
                        # Clear metadata before waking the next sender.
                        self._pending_command = self._pending_since = None
                        self._pending_sequence = self._pending_tag = None
                        # G-code, alarm and limit errors reject that operation, not authentication.
                        self._ready.set()
                        if kind == 'rt':
                            # Realtime API has no GRBL line in the application's inflight queue.
                            continue
                    self._responses.put(response)
            except Exception as exc:
                self.failure = RuntimeError('Conexão/autenticação interrompida: ' + str(exc))
                self._ready.set()
            finally:
                self._responses.put(None)

        def readline(self):
            try:
                value = self._responses.get(timeout=.1)
                if value is None:
                    if self.is_open:
                        raise OSError('Leitura da conexão interrompida.')
                    return b''
                return value
            except queue.Empty:
                return b''

        def _signed(self, command, kind, ack_timeout=None):
            limit = self._ack_timeout if ack_timeout is None else float(ack_timeout)
            if ack_timeout is None and re.search(r'G0*4(?![\d.])', command, re.I):
                dwell = re.search(r'P([0-9]+(?:\.[0-9]*)?|\.[0-9]+)', command, re.I)
                if dwell and math.isfinite(float(dwell[1])):
                    limit = max(limit, float(dwell[1]) + 30)
            native_pause = re.fullmatch(r'(?:N\d+\s*)?M0+(?:\.0+)?', command.strip(), re.I) is not None
            if math.isnan(limit) or limit <= 0 or (math.isinf(limit) and not native_pause):
                raise ValueError('Prazo de confirmação inválido para este comando.')
            generation = self._generation
            if self._recovering:
                raise RuntimeError('Autenticação sendo renovada; comando não enviado.')
            encoded = command.encode('ascii')
            if not 1 <= len(encoded) <= 200 or any(c < 32 or c > 126 for c in encoded):
                raise ValueError('Cada comando deve ter 1–200 caracteres ASCII, em uma única linha.')
            payload = encoded.hex()
            with self._tx:
                deadline = time.monotonic() + limit
                while not self._ready.wait(.1):
                    if not self.is_open:
                        raise OSError('Conexão fechada.')
                    if time.monotonic() >= deadline:
                        if self._pending_command and not self._ack_expired():
                            deadline = time.monotonic() + 1
                            continue
                        # Never retry an uncertain motion automatically.
                        self.failure = TimeoutError('Sem confirmação da placa. ' + self.communication_diagnostics() + '. Pare e reconecte; comando não será repetido.')
                        raise self.failure
                if self.failure:
                    raise self.failure
                if not self.is_open or self.seq >= 0xffffffff:
                    raise RuntimeError('Reconecte para uma nova sessão.')
                seq = str(self.seq)
                tag = mac(self.key, self.nonce + '|' + seq + '|' + payload)
                wire = ('$FFCMD=' + seq + ',' + tag + ',' + payload + '\n').encode('ascii')
                self._kind = kind
                self._ready.clear()
                try:
                    with self._wire:
                        if generation != self._generation or self._recovering:
                            self._kind = None
                            raise SessionChanged('Sessão renovada; comando não enviado. Confirme o estado antes de tentar novamente.')
                        self._pending_command = command
                        self._pending_timeout = limit
                        self._pending_sequence = seq
                        self._pending_tag = tag
                        self._pending_since = time.monotonic()
                        if self._write_raw(wire) != len(wire):
                            raise OSError('Escrita incompleta; não repetir movimento.')
                        self.seq += 1
                except SessionChanged:
                    self._ready.set()
                    raise
                except Exception as exc:
                    self.failure = OSError('Falha de envio: ' + str(exc) + '. Reconecte; comando não será repetido.')
                    self._ready.set()
                    raise

        def write_with_timeout(self, data, ack_timeout):
            return self.write(data, ack_timeout=ack_timeout)

        def write(self, data, ack_timeout=None):
            data = bytes(data)
            if not self.is_open:
                raise OSError('Conexão fechada.')
            if data and all(c in SAFE_REALTIME for c in data):
                # Stop/status/reset bypass HMAC and the pending-command queue.
                if self._recovering and all(c in (ord('?'), 0x80, 0x87) for c in data):
                    return len(data)
                # Canonical extended status/hold bypass the legacy $39 setting.
                result = self._write_raw(data.translate(REALTIME_WIRE))
                if result != len(data):
                    raise OSError('Escrita realtime incompleta; confira o estado da máquina.')
                # Firmware reports session reset; reader renews it without resending moves.
                return result
            if len(data) == 1 and (data[0] >= 0x80 or data == b'~'):
                self._signed_realtime(data[0])
                return 1
            if not data.endswith(b'\n'):
                raise ValueError('Envie comandos terminados por newline.')
            for line in data.decode('ascii').splitlines():
                if line.strip():
                    self._signed(line, 'line', ack_timeout=ack_timeout)
            return len(data)

        def _signed_realtime(self, command):
            if command == ord('~'):
                command = 0x81  # Canonical cycle start remains signed, independent of $39.
            # A resume must not wait for the ACK of a held G38.x command.
            with self._rt_tx:
                generation = self._generation
                if self._recovering:
                    raise RuntimeError('Autenticação sendo renovada; aguarde antes de retomar.')
                if self.failure:
                    raise self.failure
                if self.rtseq >= 0xffffffff:
                    raise RuntimeError('Reconecte para uma nova sessão.')
                seq, value = str(self.rtseq), bytes([command]).hex()
                tag = mac(self.key, self.nonce + '|rt|' + seq + '|' + value)
                wire = b'\xf8' + (seq + ',' + tag + ',' + value + '\n').encode('ascii')
                with self._wire:
                    if generation != self._generation or self._recovering:
                        raise RuntimeError('Sessão renovada; retomada não enviada.')
                    if self._write_raw(wire) != len(wire):
                        self.failure = OSError('Falha de envio realtime; não repetir automaticamente.')
                        raise self.failure
                    self.rtseq += 1

        def close(self):
            self._closed = True
            try:
                with self._wire:
                    if self.raw.is_open:self._write_raw(b'$FFBYE\n')
            except Exception:
                pass
            self._ready.set()
            self.raw.close()


    def open_authenticated(name, baud=115200, path=None):
        import serial
        key = load_key(path)
        # Existing GUI is USB-first. socket:// is supported for a future TCP client,
        # but TCP/Wi-Fi must be validated on hardware before relying on it.
        raw = serial.serial_for_url(name, baudrate=baud, timeout=.1, write_timeout=2)
        return SignedPort(raw, key)



    return types.SimpleNamespace(open_authenticated=open_authenticated, SignedPort=SignedPort,
        SAFE_REALTIME=SAFE_REALTIME, load_key=load_key, verify_firmware=verify_firmware,
        mac=mac, exchange=exchange)
_ffst_auth = _create_embedded_auth()
open_authenticated = _ffst_auth.open_authenticated
SAFE_REALTIME = _ffst_auth.SAFE_REALTIME


try:
    import serial
    from serial.tools import list_ports
except ImportError:
    serial = None
    list_ports = None

RESOURCE_DIR = (Path(sys.executable).resolve().parent if getattr(sys, 'frozen', False)
                else Path(__file__).resolve().parent)
# Montador extracts source into a temporary directory but provides a persistent config path.
PROJECT_DIR = Path(os.environ.get('CNC_PCBS_CONFIG_DIR', str(RESOURCE_DIR))).expanduser()
PROJECT_DIR.mkdir(parents=True, exist_ok=True)
CONFIG = PROJECT_DIR / 'config_controlador_pcb.json'
ATIVAR_LOG = True  # True = grava diagnóstico; False = desativa totalmente o log
DIAGNOSTIC_LOG = PROJECT_DIR / 'CNC_PCB_diagnostico_GRBL.log'


def icon_path(saved_path):
    """Usa o ícone original ou o correspondente na pasta do projeto."""
    original = Path(saved_path)
    if original.is_file():
        return original
    filename = PureWindowsPath(saved_path).name
    for base in dict.fromkeys((PROJECT_DIR, RESOURCE_DIR)):
        candidate = base / filename
        if candidate.is_file():
            return candidate
        for directory in base.iterdir():
            if directory.is_dir():
                candidate = directory / filename
                if candidate.is_file():
                    return candidate
    return RESOURCE_DIR / filename


APP_VERSION = 'S3 0.1.3 — Controlador PCB autenticado — M0 XYZ'
DEFAULT = {'baud': 115200, 'buffer': 128, 'macros': [
    {'name': 'Laser OFF', 'command': 'M5'},
    {'name': 'Ir X0 Y0', 'command': 'G90\nG0 X0 Y0'}], 'sim_speed': '1.0'}
WORD = re.compile(r'([A-Z])\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][+-]?\d+)?)')
PAREN = re.compile(r'\([^)]*\)')
BRACKET = re.compile(r'\[([^\[\]]+)\]')
SETTING = re.compile(r'\$(\d+)')


def expand_macro(command, bounds, settings):
    """Substitui limites XY e contas aritméticas entre colchetes."""
    def evaluate(match):
        expression = match.group(1).strip().lower()
        def setting_value(found):
            number = found.group(1)
            if number not in settings:
                raise ValueError(f'Parâmetro ${number} não recebido da controladora. Aguarde a leitura de $$ ou conecte novamente.')
            return str(settings[number])
        expression = SETTING.sub(setting_value, expression)
        values = dict(bounds)
        def calc(node):
            if isinstance(node, ast.Constant) and type(node.value) in (int, float):
                return float(node.value)
            if isinstance(node, ast.Name) and node.id in values:
                return float(values[node.id])
            if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
                value = calc(node.operand)
                return value if isinstance(node.op, ast.UAdd) else -value
            if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
                a, b = calc(node.left), calc(node.right)
                if isinstance(node.op, ast.Add): return a + b
                if isinstance(node.op, ast.Sub): return a - b
                if isinstance(node.op, ast.Mult): return a * b
                return a / b
            raise ValueError(f'Expressão não permitida: [{match.group(1)}]')
        try:
            result = calc(ast.parse(expression, mode='eval').body)
        except (SyntaxError, ZeroDivisionError, OverflowError) as exc:
            raise ValueError(f'Expressão inválida: [{match.group(1)}]') from exc
        if not math.isfinite(result):
            raise ValueError('Resultado da macro não é finito.')
        return f'{result:.6f}'.rstrip('0').rstrip('.') if result else '0'
    return BRACKET.sub(evaluate, command)


def export_macros(macros):
    exported = []
    for macro in macros:
        item = {'name': macro['name'], 'command': macro['command']}
        if macro.get('icon'):
            try:
                with Image.open(icon_path(macro['icon'])) as source:
                    icon = source.convert('RGBA')
                    icon.thumbnail((256, 256), Image.Resampling.LANCZOS)
                    data = io.BytesIO()
                    icon.save(data, format='PNG')
                item['icon_png_base64'] = base64.b64encode(data.getvalue()).decode('ascii')
            except (OSError, ValueError) as exc:
                raise ValueError(f"Não foi possível incluir o ícone de '{macro['name']}': {exc}") from exc
        exported.append(item)
    return {'format': 'CONTROLADORA_MACROS_V1', 'macros': exported}


def import_macros(data):
    if not isinstance(data, dict) or data.get('format') not in ('DLC32_MACROS_V1', 'CONTROLADORA_MACROS_V1'):
        raise ValueError('Arquivo de macros incompatível.')
    items = data.get('macros')
    if not isinstance(items, list) or len(items) > 100:
        raise ValueError('Lista de macros inválida (máximo de 100 botões).')
    result = []
    icons = []
    for item in items:
        if not isinstance(item, dict):
            raise ValueError('Entrada de macro inválida.')
        name, command = item.get('name'), item.get('command')
        if not isinstance(name, str) or not name.strip() or len(name) > 100:
            raise ValueError('Nome de macro inválido.')
        if not isinstance(command, str) or not command.strip() or len(command) > 10000:
            raise ValueError(f'Comando inválido na macro {name}.')
        macro = {'name': name, 'command': command}
        encoded = item.get('icon_png_base64')
        if encoded is not None:
            if not isinstance(encoded, str) or len(encoded) > 4_000_000:
                raise ValueError(f'Ícone inválido na macro {name}.')
            try:
                raw = base64.b64decode(encoded, validate=True)
                with Image.open(io.BytesIO(raw)) as im:
                    if im.width > 2048 or im.height > 2048:
                        raise ValueError('Imagem muito grande.')
                    im.verify()
            except (OSError, ValueError, binascii.Error) as exc:
                raise ValueError(f'Ícone inválido na macro {name}.') from exc
            icons.append((macro, raw))
        result.append(macro)
    if icons:
        folder = PROJECT_DIR / '.controladora_macro_icons'
        folder.mkdir(exist_ok=True)
        for macro, raw in icons:
            filename = hashlib.sha256(raw).hexdigest()[:24] + '.png'
            path = folder / filename
            if not path.exists():
                path.write_bytes(raw)
            macro['icon'] = str(path)
    return result


def clean(line):
    # Remova comentários entre parênteses antes de tratar o ponto e vírgula.
    line = PAREN.sub('', line).split(';', 1)[0].strip().upper()
    return line



def grbl_mode_from_z(lines):
    """$32=0 se houver qualquer palavra Z diferente de zero; caso contrário $32=1.

    Ignora comentários e não confunde Z0, Z0.0 ou texto comentado com movimento Z.
    """
    for raw in lines:
        line = clean(raw)
        for match in WORD.finditer(line):
            if match.group(1) == 'Z' and abs(float(match.group(2))) > 1e-9:
                return 0
    return 1


def _preview_mode(lines):
    """Classifica o arquivo pelo movimento real, evitando confundir spindle de furação com laser."""
    x = y = z = 0.0
    absolute = True
    scale = 1.0
    motion = 0
    eps = 1e-9
    laser_signal = False
    plunges = 0
    cutting_xy = 0

    for raw in lines:
        line = clean(raw)
        if not line or line.startswith(('$', '%')):
            continue
        words = [(m.group(1), float(m.group(2))) for m in WORD.finditer(line)]
        if any(key == 'S' for key, _ in words) or any(key == 'M' and int(value) in (3, 4) for key, value in words):
            laser_signal = True

        g = [n for key, n in words if key == 'G']
        if any(abs(n - 20) < 0.001 for n in g):
            scale = 25.4
        if any(abs(n - 21) < 0.001 for n in g):
            scale = 1.0
        if any(abs(n - 90) < 0.001 for n in g):
            absolute = True
        if any(abs(n - 91) < 0.001 for n in g):
            absolute = False
        for n in g:
            if int(n) in (0, 1, 2, 3) and n == int(n):
                motion = int(n)
        if any(int(n) == 92 for n in g):
            continue

        coords = {key: value * scale for key, value in words if key in 'XYZ'}
        nx = (coords['X'] if absolute else x + coords['X']) if 'X' in coords else x
        ny = (coords['Y'] if absolute else y + coords['Y']) if 'Y' in coords else y
        nz = (coords['Z'] if absolute else z + coords['Z']) if 'Z' in coords else z

        moved_xy = abs(nx - x) > eps or abs(ny - y) > eps or (motion in (2,3) and any(k in 'IJR' for k,v in words))
        moved_z = abs(nz - z) > eps
        if moved_z and nz < z - eps and nz < -eps:
            plunges += 1
        if moved_xy and motion != 0 and (z < -eps or nz < -eps):
            cutting_xy += 1
        x, y, z = nx, ny, nz

    # Laser típico não mergulha o eixo Z. M3/S em arquivo de furação é spindle, não laser.
    if laser_signal and plunges == 0 and cutting_xy == 0:
        return 'laser'
    # Furação típica: vários mergulhos Z e nenhum corte XY enquanto a ferramenta está abaixo de Z0.
    if plunges > 0 and cutting_xy == 0:
        return 'drill'
    # Fresagem/contorno: há mergulho em Z e deslocamentos XY com a ferramenta abaixo de Z0.
    if plunges > 0 and cutting_xy > 0:
        return 'milling'
    return 'generic'


def preview_arc(x,y,nx,ny,words,scale,motion):
    vals={k:v*scale for k,v in words if k in 'IJR'}
    if 'R' in vals:
        radius=abs(vals['R']);dx,dy=nx-x,ny-y;chord=math.hypot(dx,dy)
        if chord<1e-9 or chord>2*radius+1e-6:raise ValueError('Arco R inválido.')
        h=math.sqrt(max(0,radius*radius-chord*chord/4))
        sign=(1 if motion==3 else -1)*(1 if vals['R']>=0 else -1)
        cx,cy=(x+nx)/2-sign*dy*h/chord,(y+ny)/2+sign*dx*h/chord
    else:
        if 'I' not in vals and 'J' not in vals:raise ValueError('Arco sem I/J ou R.')
        cx,cy=x+vals.get('I',0),y+vals.get('J',0);radius=math.hypot(x-cx,y-cy)
        if radius<1e-9 or abs(math.hypot(nx-cx,ny-cy)-radius)>.01:raise ValueError('Raio inconsistente.')
    a=math.atan2(y-cy,x-cx);b=math.atan2(ny-cy,nx-cx)
    sweep=(b-a)%(2*math.pi) if motion==3 else -((a-b)%(2*math.pi))
    if abs(sweep)<1e-10:sweep=2*math.pi*(1 if motion==3 else -1)
    n=max(8,math.ceil(abs(sweep)/.025),math.ceil(abs(sweep)*radius/.5))
    if n>200000:raise ValueError('Arco muito grande.')
    # Inclui os extremos exatos para a área do mapa não perder pontos nas curvas.
    fractions={i/n for i in range(n+1)}
    for angle in (0,math.pi/2,math.pi,3*math.pi/2):
        travel=(angle-a)%(2*math.pi) if motion==3 else (a-angle)%(2*math.pi)
        if travel<=abs(sweep)+1e-9:fractions.add(min(1,travel/abs(sweep)))
    points=[(cx+radius*math.cos(a+sweep*t),cy+radius*math.sin(a+sweep*t)) for t in sorted(fractions)]
    points[0]=(x,y);points[-1]=(nx,ny)
    return points


def analyze_preview(lines):
    """Analisa o G-code para o preview e classifica segmentos e furos."""
    x = y = z = 0.0
    absolute = True
    scale = 1.0
    motion = 0
    spindle = False
    power = 0.0
    eps = 1e-9
    mode = _preview_mode(lines)
    laser_file = mode == 'laser'
    drill_file = mode == 'drill'
    has_spindle_command = any(re.search(r'\bM\s*[345]\b', clean(raw)) for raw in lines)
    segments = []
    holes = []
    warnings = set()

    for raw in lines:
        line = clean(raw)
        if not line or line.startswith(('$', '%')):
            continue
        words = [(m.group(1), float(m.group(2))) for m in WORD.finditer(line)]
        for key, value in words:
            if key == 'M' and int(value) in (3, 4):
                spindle = True
            elif key == 'M' and int(value) == 5:
                spindle = False
            elif key == 'S':
                power = value

        g = [n for key, n in words if key == 'G']
        if any(abs(n - 20) < 0.001 for n in g):
            scale = 25.4
        if any(abs(n - 21) < 0.001 for n in g):
            scale = 1.0
        if any(abs(n - 90) < 0.001 for n in g):
            absolute = True
        if any(abs(n - 91) < 0.001 for n in g):
            absolute = False
        for n in g:
            if int(n) in (0, 1, 2, 3) and n == int(n):
                motion = int(n)
        if any(int(n) == 92 for n in g):
            warnings.add('G92 altera a origem; confira o zero na máquina.')
            continue

        coords = {key: value * scale for key, value in words if key in 'XYZ'}
        if not coords and not (motion in (2,3) and any(key in 'IJR' for key,_ in words)):
            continue

        nx = (coords['X'] if absolute else x + coords['X']) if 'X' in coords else x
        ny = (coords['Y'] if absolute else y + coords['Y']) if 'Y' in coords else y
        nz = (coords['Z'] if absolute else z + coords['Z']) if 'Z' in coords else z

        arc_path=None
        if motion in (2,3):
            try:arc_path=preview_arc(x,y,nx,ny,words,scale,motion)
            except ValueError as exc:
                warnings.add(str(exc)+' Confira este arco no arquivo.')

        moved_xy = abs(nx - x) > eps or abs(ny - y) > eps or (motion in (2,3) and any(k in 'IJR' for k,v in words))
        moved_z = abs(nz - z) > eps
        laser_active = motion != 0 and (power > 0 and (spindle or not has_spindle_command) if laser_file else False)
        cutting_xy = motion != 0 and (z < -eps or nz < -eps)

        if moved_xy:
            if laser_file:
                kind = 'laser_active' if laser_active else 'laser_travel'
            elif drill_file:
                # Todo deslocamento XY de um arquivo de furação é o trajeto entre furos.
                kind = 'drill_travel'
            elif cutting_xy:
                kind = 'cut'
            else:
                kind = 'travel'
            if arc_path:
                segments.extend((a[0],a[1],b[0],b[1],kind) for a,b in zip(arc_path,arc_path[1:]))
            else:segments.append((x, y, nx, ny, kind))

        # Um mergulho em Z negativo marca a posição do furo, mesmo que exista M3/S para o spindle.
        if drill_file and moved_z and nz < z - eps and nz < -eps:
            # Evita duplicar o mesmo ponto caso o pós-processador faça mais de um mergulho no mesmo furo.
            if not holes or abs(holes[-1][0] - nx) > 1e-7 or abs(holes[-1][1] - ny) > 1e-7:
                holes.append((nx, ny, len(segments)))

        x, y, z = nx, ny, nz

    return {
        'segments': segments,
        'holes': holes,
        'warnings': sorted(warnings),
        'mode': mode,
    }


def moves(lines):
    """Compatibilidade com versões anteriores."""
    preview = analyze_preview(lines)
    legacy_segments = []
    for x1, y1, x2, y2, kind in preview['segments']:
        legacy_segments.append((x1, y1, x2, y2, kind in ('laser_active', 'cut')))
    return legacy_segments, preview['warnings']



def estimated_seconds(lines, initial=(0.0, 0.0, 0.0), settings=None):
    """Nominal time: feeds, XYZ, arcs and dwell; acceleration is not included."""
    settings = settings or {}
    pos = list(initial); absolute = True; scale = 1.0; feed = 300.0; motion = 0
    total = 0.0
    for raw in lines:
        line = clean(raw)
        if not line or line.startswith('$'): continue
        words = [(m.group(1), float(m.group(2))) for m in WORD.finditer(line)]
        gs = [v for k,v in words if k == 'G']; values = dict(words)
        if 20 in gs: scale = 25.4
        if 21 in gs: scale = 1.0
        if 90 in gs: absolute = True
        if 91 in gs: absolute = False
        if 'F' in values: feed = values['F'] * scale
        if 4 in gs:
            total += max(0, values.get('P', 0)); continue
        if any(g in gs for g in (10,28,30,38.2,38.3,92)): continue
        for g in gs:
            if g in (0,1,2,3): motion = int(g)
        if not any(k in values for k in 'XYZIJR'): continue
        target = [((values[k]*scale if absolute else pos[i]+values[k]*scale) if k in values else pos[i]) for i,k in enumerate('XYZ')]
        distance = math.dist(pos,target)
        if motion in (2,3):
            try:
                arc = preview_arc(pos[0],pos[1],target[0],target[1],words,scale,motion)
                length = sum(math.dist(a,b) for a,b in zip(arc,arc[1:]))
                distance = math.hypot(length,target[2]-pos[2])
            except ValueError: pass
        if motion == 0:
            total += max((60*abs(target[i]-pos[i])/max(1,settings.get(str(110+i),3000 if i<2 else 500)) for i in range(3)),default=0)
        elif feed > 0: total += 60*distance/feed
        pos = target
    return total


def estimate_corners(xs, ys, zs, measured):
    """Extrapolate each original corner using its displaced sample and neighbors."""
    original = [row[:] for row in zs]
    for i,j in ((0,0),(len(xs)-1,0),(0,len(ys)-1),(len(xs)-1,len(ys)-1)):
        ni = 1 if i == 0 else i-1; nj = 1 if j == 0 else j-1
        x,y = measured[j,i]; ax,ay = measured[j,ni]; bx,by = measured[nj,i]
        dx,dy = ax-x,ay-y; ex,ey = bx-x,by-y
        det = dx*ey-dy*ex
        if abs(det)<1e-9: raise ValueError('Malha insuficiente para estimar os cantos com deslocamento de 1 mm.')
        za = original[j][ni]-original[j][i]; zb = original[nj][i]-original[j][i]
        slope_x = (za*ey-zb*dy)/det; slope_y = (dx*zb-ex*za)/det
        zs[j][i] = original[j][i]+slope_x*(xs[i]-x)+slope_y*(ys[j]-y)
    return zs


class HeightMap:
    """Mapa em coordenadas de trabalho, alturas absolutas; nunca altera o .nc."""
    def __init__(self, xs, ys, zs, wco, wcs):
        self.xs, self.ys, self.zs = xs, ys, zs
        self.wco, self.wcs = tuple(wco), wcs
        if len(self.wco)!=3 or wcs not in ('G54','G55','G56','G57','G58','G59'):
            raise ValueError('Referência do mapa inválida.')
        if len(xs) < 2 or len(ys) < 2 or any(b <= a for a,b in zip(xs,xs[1:])) or any(b <= a for a,b in zip(ys,ys[1:])):
            raise ValueError('Malha inválida.')
        if len(zs) != len(ys) or any(len(row) != len(xs) for row in zs):
            raise ValueError('Mapa incompleto.')
        if not all(math.isfinite(v) for v in xs+ys+[v for row in zs for v in row]+list(wco)):
            raise ValueError('Alturas inválidas.')

    def height(self, x, y):
        if x < self.xs[0]-1e-5 or x > self.xs[-1]+1e-5 or y < self.ys[0]-1e-5 or y > self.ys[-1]+1e-5:
            raise ValueError(f'Fresagem fora do mapa: X{x:.3f} Y{y:.3f}.')
        ix = min(len(self.xs)-2, max(0, next((i-1 for i,v in enumerate(self.xs) if v >= x), len(self.xs)-2)))
        iy = min(len(self.ys)-2, max(0, next((i-1 for i,v in enumerate(self.ys) if v >= y), len(self.ys)-2)))
        u=(x-self.xs[ix])/(self.xs[ix+1]-self.xs[ix]); v=(y-self.ys[iy])/(self.ys[iy+1]-self.ys[iy])
        a,b=self.zs[iy][ix:ix+2]; c,d=self.zs[iy+1][ix:ix+2]
        return (1-v)*((1-u)*a+u*b)+v*((1-u)*c+u*d)

    def compensate(self, lines, initial):
        # Preservar todas as amostras do mapa. A nova fresa tem seu proprio Z0
        # fisico, marcado no centro X0 Y0. Aplicar APENAS o relevo relativo
        # a essa origem; nunca reutilizar as alturas absolutas da fresa antiga.
        # G21/G90/G17/G94 são exigidos; outros sistemas/offsets são rejeitados.
        reference_height = self.height(0.0, 0.0)
        x,y,z = initial
        try: z -= self.height(x,y) - reference_height
        except ValueError: z -= max(v for row in self.zs for v in row) - reference_height
        motion=0; ready_units=ready_absolute=False
        out=['G21 G90 G17 G94']
        step=min(1.0, min(b-a for a,b in zip(self.xs,self.xs[1:]))/4,
                 min(b-a for a,b in zip(self.ys,self.ys[1:]))/4)
        allowed={0,1,2,3,4,17,21,90,94,40,49,int(self.wcs[1:])}
        for number, raw in enumerate(lines,1):
            line=clean(raw)
            if not line or line=='%': continue
            words=re.findall(r'([A-Z])([+-]?(?:\d+(?:\.\d*)?|\.\d+))',line)
            if re.sub(r'[A-Z][+-]?(?:\d+(?:\.\d*)?|\.\d+)','',line).strip():
                raise ValueError(f'Linha {number}: sintaxe não suportada pelo mapa.')
            gs=[float(v) for k,v in words if k=='G']
            if any(g not in allowed for g in gs) or any(k not in 'NGMXYZIJRFSPT' for k,v in words):
                raise ValueError(f'Linha {number}: mapa aceita G21/G90/G17, G0/G1 e arcos XY G2/G3; offsets e ciclos não são permitidos.')
            if any(k=='M' and float(v) not in (0,1,2,3,4,5,8,9,30) for k,v in words):
                raise ValueError(f'Linha {number}: comando M não suportado com mapa.')
            if 21 in gs: ready_units=True
            if 90 in gs: ready_absolute=True
            if any(g in (0,1,2,3) for g in gs): motion=int(next(g for g in gs if g in (0,1,2,3)))
            vals={k:float(v) for k,v in words}
            if not any(k in vals for k in 'XYZIJR'):
                out.append(line); continue
            if not ready_units or not ready_absolute:
                raise ValueError(f'Linha {number}: inclua G21 e G90 antes dos movimentos.')
            if 4 in gs: raise ValueError('G4 com palavras de eixo não suportado.')
            nx,ny,nz=vals.get('X',x),vals.get('Y',y),vals.get('Z',z)
            path=[]
            if motion in (2,3):
                if 'R' in vals:
                    if 'I' in vals or 'J' in vals: raise ValueError('Arco mistura R e I/J.')
                    dx,dy=nx-x,ny-y; chord=math.hypot(dx,dy); radius=abs(vals['R'])
                    if chord < 1e-9 or chord > 2*radius+1e-7: raise ValueError('Arco R inválido.')
                    h=math.sqrt(max(0,radius*radius-chord*chord/4))
                    sign=(1 if motion==3 else -1)*(1 if vals['R']>=0 else -1)
                    cx,cy=(x+nx)/2-sign*dy*h/chord,(y+ny)/2+sign*dx*h/chord
                else:
                    if 'I' not in vals and 'J' not in vals: raise ValueError('Arco requer I/J ou R.')
                    cx,cy=x+vals.get('I',0),y+vals.get('J',0); radius=math.hypot(x-cx,y-cy)
                    if radius<1e-9 or abs(math.hypot(nx-cx,ny-cy)-radius)>0.01: raise ValueError('Raio do arco inconsistente.')
                a=math.atan2(y-cy,x-cx); b=math.atan2(ny-cy,nx-cx)
                sweep=(b-a)%(2*math.pi) if motion==3 else -((a-b)%(2*math.pi))
                if abs(sweep)<1e-10: sweep=2*math.pi*(1 if motion==3 else -1)
                n=max(1,math.ceil(abs(sweep)*radius/step),math.ceil(abs(sweep)/0.05))
                for j in range(1,n+1):
                    t=j/n; angle=a+sweep*t
                    path.append((cx+radius*math.cos(angle),cy+radius*math.sin(angle),z+(nz-z)*t))
                path[-1]=(nx,ny,nz)
            else:
                n=max(1, math.ceil(math.hypot(nx-x,ny-y)/step))
                path=[(x+(nx-x)*j/n,y+(ny-y)*j/n,z+(nz-z)*j/n) for j in range(1,n+1)]
            extras=' '.join(k+v for k,v in words if k in 'MFST')
            for j,(px,py,pz) in enumerate(path):
                try: h=self.height(px,py)
                except ValueError:
                    if motion!=0 or pz<=0: raise
                    h=max(v for row in self.zs for v in row)
                # Converter altura absoluta registrada em desvio relativo ao Z0.
                out.append(f'G{0 if motion==0 else 1} X{px:.4f} Y{py:.4f} Z{pz+h-reference_height:.4f}'+(' '+extras if j==0 and extras else ''))
                if len(out)>2000000: raise ValueError('Arquivo compensado excede dois milhões de linhas.')
            x,y,z=nx,ny,nz
        return out


class Streamer:
    def __init__(self, events):
        self.events = events
        self.port = None
        self.lock = threading.Lock()
        self._send_lock = threading.Lock()
        self._display_lock = threading.Lock()
        self.latest_command = self.latest_response = ''
        self._worker_lock = threading.Lock()
        self._workers = []
        self.running = False
        self.paused = False
        self.m0_waiting = False
        self.m0_stopped = threading.Event()
        self.m0_alignment_ready = False
        self._m0_managed = False
        self._m0_editing = False
        self._m0_lock = threading.Lock()
        self._m0_resume = threading.Event()
        self._m0_anchor = None
        self._m0_modal = []
        self.cancel = False
        self.cancel_reason = ''
        self.limit = 128
        self.inflight = []
        # Eventos: a thread serial acorda a sondagem sem polling de 20 ms.
        self.command_ack_event = threading.Event()
        self.probe_received_event = threading.Event()
        self.reader = None
        self.last_status = 0.0
        self.work_offset = None
        self.simulation = False
        self.sim_speed = 1.0
        self.sim_position = (0.0, 0.0)
        self.sim_absolute = True
        self.sim_scale = 1.0
        self.sim_motion = 0
        self.sim_feed = 3000.0
        self.sim_laser = False
        self.sim_power = 0.0
        self.settings = {}
        self.probing = False
        self.probe_result = None
        self.probe_state = None
        self.machine_state = ''
        self.work_position = None
        self.modal = None
        self.status_time = 0.0
        self.status_version = 0

    def emit(self, *event):
        self.events.put(event)

    def connect(self, name, baud):
        self.disconnect()
        if self.running:
            raise RuntimeError('A operação anterior ainda está encerrando. Aguarde e conecte novamente.')
        self.simulation = False
        self.port = open_authenticated(name, baud)
        self.cancel = False
        self.cancel_reason = ''
        self._m0_resume.clear()
        self.command_ack_event.clear()
        self.probe_received_event.clear()
        self.inflight = []
        self.work_offset = None
        self.work_position = None
        self.modal = None
        self.probe_state = None
        self.status_time = 0.0
        self.settings.clear()
        self.reader = self.start_worker(self.read_loop)
        self.start_worker(self.query_settings, (self.port,))
        self.emit('log', f'Conectado e autenticado: {name} @ {baud}')

    def query_settings(self, port):
        time.sleep(1.5)
        if self.port is not port or not port.is_open or self.running:
            return
        try:
            self.send_payload(b'$$\n')
        except (serial.SerialException, OSError):
            pass

    def start_worker(self, target, args=()):
        with self._worker_lock:
            self._workers = [w for w in self._workers if w.is_alive()]
            worker = threading.Thread(target=target, args=args, daemon=True)
            self._workers.append(worker)
            worker.start()
        return worker

    def disconnect(self):
        self.cancel = True
        self.m0_alignment_ready = False
        self.m0_waiting = False
        self._m0_resume.set()
        self.command_ack_event.set()
        self.probe_received_event.set()
        port, self.port = self.port, None
        if port:
            try: port.close()
            except Exception: pass
        # Do not attach a fresh port to a still-running operation from the old session.
        with self._worker_lock:
            workers = list(self._workers)
        deadline = time.monotonic() + 2
        for worker in workers:
            if worker is not threading.current_thread():
                worker.join(max(0, deadline - time.monotonic()))
        with self._worker_lock:
            self._workers = [w for w in self._workers if w.is_alive()]
            pending = bool(self._workers)
        self.running = pending
        self.paused = False
        self._m0_managed = False
        self._m0_editing = False
        self._m0_anchor = None
        self._m0_modal = []
        with self.lock:
            self.inflight.clear()
        self.simulation = False
        self.probing = False
        self.probe_result = None
        self.probe_state = None
        self.modal = None
        self.work_offset = None
        self.work_position = None
        self.machine_state = ''
        self.status_time = self.status_version = self.last_status = 0
        self.settings.clear()
        with self._display_lock:
            self.latest_command = self.latest_response = ''

    def read_loop(self):
        port = self.port
        while self.port is port and port.is_open:
            try:
                response = port.readline().decode('utf-8', 'replace').strip()
            except (serial.SerialException, OSError) as exc:
                self.cancel_reason = str(getattr(port, 'failure', None) or exc)
                break
            if not response:
                continue
            if not response.startswith('<'):
                with self._display_lock:
                    self.latest_response = response
                self.emit('log', '< ' + response)
            low = response.lower()
            if response.startswith('[GC:'):
                self.modal = response[4:-1].split()
            if response.startswith('[PRB:'):
                try:
                    coords, success = response[5:-1].rsplit(':', 1)
                    self.probe_result = (tuple(float(v) for v in coords.split(',')[:3]), success == '1')
                    self.probe_received_event.set()
                except ValueError:
                    self.cancel = True
            if response == '[FFSESSION:RESET]' and self.m0_waiting:
                self.cancel = True
                self.m0_alignment_ready = False
            if low.startswith('grbl'):
                self.work_offset = None
                self.modal = None
                self.work_position = None
                self.cancel = True if self.probing or self.m0_waiting else self.cancel
                self.command_ack_event.set()
                self.probe_received_event.set()
                self.emit('map_invalid', 'Reset da controladora')
            match_setting = re.match(r'^\$(\d+)=([+-]?(?:\d+(?:\.\d*)?|\.\d+))', response)
            if match_setting:
                self.settings[match_setting.group(1)] = float(match_setting.group(2))
            if response.startswith('<') and response.endswith('>'):
                # Diagnóstico somente durante sondagem: registrar estado real do GRBL.
                if self.probing:
                    self.emit('log', '< ' + response)
                fields = response[1:-1].split('|')
                self.machine_state = fields[0]
                if self.m0_waiting and self._m0_managed:
                    allowed = ('idle', 'run', 'jog') if self._m0_editing else ('idle',)
                    if fields[0].lower() not in allowed:
                        self.cancel = True
                        self.cancel_reason = 'Estado ' + fields[0] + ' durante a conferência'
                        self.m0_alignment_ready = False
                self.status_time = time.monotonic()
                if self.m0_waiting and fields[0].lower() == 'hold:0':
                    self.m0_stopped.set()
                values = {}
                for field in fields[1:]:
                    if ':' in field:
                        key, value = field.split(':', 1)
                        values[key] = value
                self.probe_state = 'P' in values.get('Pn', '')
                self.emit('probe_state', self.probe_state)
                try:
                    if 'WCO' in values:
                        self.work_offset = [float(v) for v in values['WCO'].split(',')[:3]]
                    elif 'MPos' in values and 'WPos' in values:
                        mpos = [float(v) for v in values['MPos'].split(',')[:3]]
                        wpos = [float(v) for v in values['WPos'].split(',')[:3]]
                        if len(mpos)==3 and len(wpos)==3:
                            self.work_offset = [mpos[k]-wpos[k] for k in range(3)]
                    if 'WPos' in values:
                        xy = [float(v) for v in values['WPos'].split(',')[:3]]
                    elif 'MPos' in values and self.work_offset is not None:
                        machine = [float(v) for v in values['MPos'].split(',')[:3]]
                        xy = [machine[i] - self.work_offset[i] for i in range(3)]
                    else:
                        xy = None
                    if xy is not None:
                        if self._m0_editing and self._m0_anchor is not None:
                            self.work_position = self._m0_anchor
                        else:
                            self.work_position = tuple(xy)
                            self.emit('position', xy[0], xy[1], fields[0])
                except (ValueError, IndexError):
                    pass
                self.status_version += 1
                continue
            if low == 'ok' or low.startswith('error:'):
                with self.lock:
                    item = self.inflight.pop(0) if self.inflight else None
                if item is not None:
                    number, _ = item
                    if low.startswith('error:'):
                        self.cancel_reason = response + ' após ' + (self.latest_command or 'comando pendente')
                        self.cancel = True
                        self.emit('error', number, response)
                    else:
                        self.emit('ack', number)
                    # Sempre notificar a thread que enviou o comando.
                    self.command_ack_event.set()
            if low.startswith('alarm:'):
                self.cancel_reason = response
                self.cancel = True
                self.command_ack_event.set()
                self.probe_received_event.set()
                self.emit('fault', response)
        if self.port is port:
            # Best-effort hold before closing a transport that lost its confirmations.
            try: port.write(b'!')
            except Exception: pass
            try: port.close()
            except Exception: pass
            self.cancel = True
            self.emit('fault', 'Conexão serial encerrada. ' + self.cancel_reason)

    def send_payload(self, payload, number=None, exclusive=False, probe=False, ack_timeout=None):
        # Preserve send order without holding the lock used by the reader for ACKs.
        with self._send_lock:
            item = (number, len(payload))
            with self.lock:
                if exclusive:
                    if self.inflight:
                        raise RuntimeError('Aguarde os comandos anteriores.')
                    self.command_ack_event.clear()
                    if probe:
                        self.probe_result = None
                        self.probe_received_event.clear()
                self.inflight.append(item)
            try:
                timed_write = getattr(self.port, 'write_with_timeout', None)
                if ack_timeout is not None and timed_write:
                    timed_write(payload, ack_timeout)
                else:
                    self.port.write(payload)
                with self._display_lock:
                    self.latest_command = payload.decode('ascii').strip()
                self.emit('command', payload.decode('ascii').strip())
            except Exception:
                with self.lock:
                    for index, pending in enumerate(self.inflight):
                        if pending is item:
                            self.inflight.pop(index)
                            break
                raise

    def sync_command(self, command, timeout=10):
        """Aguarda evento de ACK; para G38 aguarda também o PRB da mesma sondagem.

        Uma única thread continua responsável por ler a serial. Nenhuma consulta de
        status, dwell ou novo comando de movimento é acrescentado na sondagem.
        """
        if self.cancel:
            raise RuntimeError('Operação cancelada.')
        is_probe = bool(re.search(r'\bG38\.[2345]\b', command.upper()))
        self.send_payload((command + '\n').encode('ascii'), exclusive=True, probe=is_probe, ack_timeout=timeout)
        self.emit('log', '> ' + command)
        deadline = time.monotonic() + timeout
        barrier = command.replace(' ', '').upper() == 'G4P0.01'
        last_progress = getattr(self.port, 'last_motion_progress', 0)
        while True:
            progress = getattr(self.port, 'last_motion_progress', 0)
            paused = getattr(self.port, 'acknowledgement_wait_is_paused', None)
            if (barrier and progress > last_progress) or (paused and paused()):
                deadline = time.monotonic() + timeout
            last_progress = progress
            if self.cancel:
                raise RuntimeError('Operação cancelada ou erro da controladora. ' + self.cancel_reason)
            with self.lock:
                pending = bool(self.inflight)
            if not pending:
                break
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                self.cancel = True
                try: self.realtime(b'!')
                except Exception: pass
                raise RuntimeError('Tempo de resposta excedido; tentativa de feed hold enviada. Pare/reset antes de continuar.')
            # Acorda imediatamente no ACK; intervalo apenas para detectar desconexão/cancelamento.
            self.command_ack_event.wait(min(remaining, 0.10))
        if is_probe:
            # PRB geralmente precede o ok, mas aguardar ambos evita corrida de threads.
            # Não há espera adicional quando PRB já foi recebido.
            if not self.probe_received_event.is_set():
                self.probe_received_event.wait(0.75)
            if self.cancel:
                raise RuntimeError('Sondagem interrompida pela controladora.')
            if not self.probe_received_event.is_set() or self.probe_result is None:
                raise RuntimeError('G38 concluído sem resposta [PRB:] válida; retração automática não autorizada.')

    def fresh_status(self, timeout=3):
        version = self.status_version
        deadline = time.monotonic() + timeout
        next_poll = 0
        while self.status_version == version:
            now = time.monotonic()
            if self.cancel or now >= deadline:
                raise RuntimeError('Sem resposta de status da controladora. ' + self.cancel_reason)
            if now >= next_poll:
                # Status is read-only; retry a coalesced/lost poll, never a motion command.
                self.realtime(b'?')
                next_poll = now + .25
            time.sleep(.02)

    def wait_idle(self, timeout=4):
        """Request current status; tolerate the last pending movement, never resume Hold."""
        deadline = time.monotonic()+timeout
        while True:
            self.fresh_status()
            state = self.machine_state.lower()
            if state == 'idle': return
            if state != 'run' or time.monotonic() >= deadline:
                raise RuntimeError(f'A máquina está em {self.machine_state or "estado desconhecido"}. Aguarde a parada; se estiver pausada, use Continuar ou Cancelar.')
            time.sleep(.05)

    def begin_z_zero(self, feed):
        if self.running or self.inflight: raise RuntimeError('Aguarde os comandos anteriores.')
        if not self.port or not self.port.is_open or self.simulation:
            raise RuntimeError('Conecte a controladora primeiro.')
        if not math.isfinite(feed) or feed <= 0: raise ValueError('Avanço Z inválido.')
        self.running=True; self.probing=True; self.cancel=False
        self.start_worker(self.z_zero_loop, (feed,))

    def z_zero_loop(self, feed):
        original=None
        try:
            self.wait_idle()
            if self.settings.get('13',0)!=0: raise RuntimeError('Configure $13=0 para relatórios em mm.')
            self.modal=None; self.sync_command('$G')
            original=list(self.modal or [])
            self.sync_command('G49')
            self.sync_command('G21 G90 G94')
            self.fresh_status()
            if not self.work_position: raise RuntimeError('Posição XYZ não disponível.')
            z=self.work_position[2]
            if not math.isfinite(z): raise RuntimeError('Posição Z inválida.')
            if self.probe_state:
                self.sync_command('G10 L20 P0 Z0')
                self.emit('z_zero_done','Probe acionado: novo Z0 definido na posição atual')
            elif abs(z)<0.00005:
                self.emit('z_zero_done','Eixo Z já está em Z0')
            elif z>0:
                self.sync_command('M5')
                self.probe_result=None
                # G38.3 termina sem alarme se chegar ao limite sem contato.
                self.sync_command(f'G90 G38.3 Z0 F{feed:g}',max(10,60*abs(z)/feed+10))
                self.sync_command('G4 P0.01')
                if not self.probe_result: raise RuntimeError('Controladora não informou o resultado do probe.')
                if self.probe_result[1]:
                    self.sync_command('G10 L20 P0 Z0')
                    self.emit('z_zero_done','Contato detectado: novo Z0 definido')
                else:
                    self.emit('z_zero_done','Chegou ao Z0 sem contato do probe')
            else:
                self.sync_command(f'G1 Z0 F{feed:g}',max(10,60*abs(z)/feed+10))
                self.sync_command('G4 P0.01')
                self.emit('z_zero_done','Eixo Z elevado até Z0')
            self.fresh_status()
        except Exception as exc:
            self.cancel=True
            if self.port and self.port.is_open:
                try: self.realtime(b'!')
                except Exception: pass
            self.emit('fault',str(exc))
        finally:
            if original and not self.cancel and self.port and self.port.is_open:
                try:
                    restore=[v for v in original if v in ('G0','G1','G17','G18','G19','G20','G21','G90','G91','G93','G94') or v.startswith('F')]
                    if restore:self.sync_command(' '.join(restore))
                except Exception: pass
            self.probing=False; self.running=False
            self.emit('probe_finished')

    def begin_mark_zero_three(self, params):
        """Três medições independentes no mesmo referencial Z, sem zeros temporários.

        Conserva o ciclo comprovado do Testar probe: G91 G38.2, G4,
        leitura [PRB:], retração G91 G0, G90, G4. Zero aplicado só no fim.
        """
        if self.running or self.inflight:
            raise RuntimeError('Aguarde os comandos anteriores.')
        if not self.port or not self.port.is_open or self.simulation:
            raise RuntimeError('Conecte a controladora; a sondagem não é simulada.')
        self.running = True
        self.probing = True
        self.cancel = False
        self.start_worker(self.mark_zero_three_loop, (params,))

    def mark_zero_three_loop(self, p):
        original = None
        try:
            self.wait_idle()
            if self.probe_state:
                raise RuntimeError('Abra o contato elétrico antes de marcar zero.')
            if self.settings.get('13', 0) != 0:
                raise RuntimeError('Configure $13=0 (milímetros).')
            self.modal = None
            self.sync_command('$G')
            original = list(self.modal or [])
            if 'G21' not in original:
                raise RuntimeError('Configure G21 (mm) antes da sondagem.')
            self.sync_command('M5')
            self.sync_command('G49')
            self.sync_command('G21 G90 G94')
            # O operador posicionou manualmente o centro do furo: somente XY vira zero.
            self.sync_command('G10 L20 P0 X0 Y0')
            self.work_offset = None
            self.fresh_status()
            deadline = time.monotonic() + 3
            while self.work_offset is None and time.monotonic() < deadline:
                if self.cancel: raise RuntimeError('Sondagem cancelada.')
                self.fresh_status()
            if self.work_offset is None or len(self.work_offset) != 3:
                raise RuntimeError('Offset WCO não recebido da controladora.')
            wco_z = self.work_offset[2]
            # Três posições fora do furo de origem; o plano permite extrapolar o centro.
            positions = [(-1.0,-1.0), (1.0,-1.0), (-1.0,1.0)]
            heights = []
            # Elevação inicial relativa evita uma descida inesperada devido ao Z antigo.
            self.sync_command(f'G91 G0 Z{p["retract"]:.4f}')
            self.sync_command('G90')
            self.sync_command('G4 P0.01')
            for i, (x, y) in enumerate(positions, 1):
                self.sync_command(f'G90 G0 X{x:.4f} Y{y:.4f}')
                self.sync_command('G4 P0.01')
                self.fresh_status()
                if self.probe_state:
                    raise RuntimeError(f'Probe ainda acionado antes do ponto {i}.')
                self.probe_result = None
                self.sync_command(f'G91 G38.2 Z{-p["depth"]:.4f} F{p["feed"]:g}',
                                  max(10, 60*p['depth']/p['feed']+10))
                # Registrar o PRB e iniciar imediatamente a retração: sem G4,
                # consulta de status ou atualização de interface entre os dois.
                result = self.probe_result
                if not result or not result[1]:
                    raise RuntimeError(f'Sem confirmação do contato no ponto {i}.')
                z_machine = result[0][2]
                heights.append(z_machine)
                self.sync_command(f'G91 G0 Z{p["retract"]:.4f}')
                self.sync_command('G90')
                self.sync_command('G4 P0.01')
                self.emit('probe_progress', i, 3, x, y, z_machine-wco_z)
                # O estado Pn:P pode chegar atrasado após o G4.
                # Reconsultar sem nenhum movimento extra antes de diagnosticar
                # um contato realmente preso. Mantém o probe parado em Z retraído.
                for _ in range(4):
                    self.fresh_status()
                    if not self.probe_state:
                        break
                    time.sleep(.05)
                if self.probe_state:
                    raise RuntimeError(f'Probe ainda acionado após a retração do ponto {i}.')
            # Superfície no centro (0,0) do plano pelos pontos ±1 mm.
            z_center_machine = (heights[1]+heights[2])/2.0
            # Elevar sem depender do antigo zero Z; retornar XY em altura livre.
            self.sync_command('G90 G0 X0 Y0')
            self.sync_command('G4 P0.01')
            self.fresh_status()
            if self.work_position is None or self.work_offset is None:
                raise RuntimeError('Posição atual não disponível para definir Z0.')
            # G10 L20 P0 Z<valor> fixa nova origem sem mover o eixo.
            # Com WPos atual na referência antiga, Z novo = Z antigo - altura-centro antiga.
            new_z = self.work_position[2] - (z_center_machine - wco_z)
            # MPos = WPos + WCO. Recalcular o WCO Z da nova ferramenta
            # a partir da posição física ANTES de executar G10; não depender
            # da atualização periódica de WCO do relatório '?' do GRBL.
            machine_z_now = self.work_position[2] + self.work_offset[2]
            new_wco = (self.work_offset[0], self.work_offset[1], machine_z_now - new_z)
            self.sync_command(f'G10 L20 P0 Z{new_z:.5f}')
            self.sync_command(f'G90 G0 Z{p["safe"]:.4f}')
            self.sync_command('G4 P0.01')
            self.emit('mark_zero_done', z_center_machine-wco_z,
                      [v-wco_z for v in heights], new_wco)
        except Exception as exc:
            self.cancel = True
            self.emit('fault', 'Marcar Zero: '+str(exc))
        finally:
            if original and not self.cancel and self.port and self.port.is_open:
                try:
                    restore = [v for v in original if v in ('G0','G1','G17','G18','G19','G20','G21','G90','G91','G93','G94') or v.startswith('F')]
                    if restore: self.sync_command(' '.join(restore))
                except Exception: pass
            self.probing = False
            self.running = False
            self.emit('probe_finished')

    def begin_probe(self, params, test=False):
        if self.running or self.inflight: raise RuntimeError('Aguarde os comandos anteriores.')
        if not self.port or not self.port.is_open or self.simulation: raise RuntimeError('Conecte a máquina; probing não é simulado.')
        self.running=True; self.probing=True; self.cancel=False
        self.start_worker(self.probe_loop, (params, test))

    def probe_loop(self, p, test):
        original=None
        try:
            self.wait_idle()
            if self.probe_state: raise RuntimeError('Probe já acionado: abra o contato antes de medir.')
            self.modal=None; self.sync_command('$G')
            original=list(self.modal or [])
            if 'G21' not in original: raise RuntimeError('Configure G21 (mm) antes de mapear.')
            if not test:
                # Marcar Zero já estabeleceu a referência XY. Não alterar sua origem.
                self.emit('log', 'Mapa: preservando X0 Y0 Z0 definidos pelo Marcar Zero.')
            # O $G do GRBL não informa G43.1/G49: envie o cancelamento e aguarde ok.
            self.sync_command('G49')
            # Não apague o WCO válido do Marcar Zero: GRBL envia WCO
            # periodicamente, não em toda resposta a '?'.
            # Pedir status novo atualiza WCO quando vier, preservando o cache.
            self.fresh_status()
            if self.work_offset is None:
                # Sem offset confiável, tentar obter o relatório periódico sem
                # forçar mudanças em $10 e sem mover nenhum eixo.
                deadline=time.monotonic()+4
                while self.work_offset is None and time.monotonic()<deadline:
                    if self.cancel: raise RuntimeError('Operação cancelada.')
                    self.fresh_status()
                    time.sleep(.04)
            if self.work_offset is None or len(self.work_offset)!=3 or self.work_position is None:
                raise RuntimeError('Mapa: não há WCO/posição disponíveis. Reconecte a controladora e verifique o relatório de status GRBL; nenhum movimento foi iniciado.')
            if self.settings.get('13',0)!=0: raise RuntimeError('Configure $13=0 para relatórios em mm.')
            wco=tuple(self.work_offset); wcs=next((g for g in original if g in ('G54','G55','G56','G57','G58','G59')),None)
            if not wcs: raise RuntimeError('Sistema de coordenadas não informado.')
            self.sync_command('M5'); self.sync_command('G21 G90 G94')
            xs=p['xs']; ys=p['ys']; zs=[[None]*len(xs) for _ in ys]; measured_xy={}
            points=[(None,None,self.work_position[0],self.work_position[1])] if test else [(i,j,xs[i],ys[j]) for j in range(len(ys)) for i in (range(len(xs)) if j%2==0 else reversed(range(len(xs))))]
            if not test:
                # O Marcar Zero terminou em X0 Y0 e no Z seguro absoluto.
                # Usar essa MESMA referencia, sem G92, G10 nem subir novamente no inicio.
                self.fresh_status()
                if self.work_position is None:
                    raise RuntimeError('Mapa: posicao XYZ atual nao disponivel.')
                start_x, start_y, start_z = self.work_position
                if abs(start_z - p['safe']) > 0.15:
                    raise RuntimeError(
                        f'Mapa: a posicao atual Z{start_z:.3f} nao e o Z seguro '
                        f'configurado ({p["safe"]:.3f}). Marque Zero antes de mapear; '
                        'nenhum movimento foi enviado.')
                self.emit('log', f'Mapa: partindo de X{start_x:.3f} Y{start_y:.3f} '
                                 f'Z{start_z:.3f}, sem redefinir origem.')
            # Na malha, o primeiro ponto começa em Z seguro; os demais
            # começam na altura alcançada pela retração do contato anterior.
            # Não mover novamente a Z seguro entre pontos.
            probe_start_z = p['safe'] if not test else None
            for count,(i,j,x,y) in enumerate(points,1):
                if not test:
                    # XY apenas depois de o GRBL confirmar a retração anterior.
                    # O G38.2 seguinte é enfileirado após o XY pelo GRBL.
                    # Sem G4/status aqui: não criar uma segunda parada no ponto alto.
                    self.sync_command(f'G90 G0 X{x:.4f} Y{y:.4f}')
                self.probe_result=None
                # G38.2 é relativo: recalcular o curso até o limite ABSOLUTO
                # usando o Z real de partida (após a retração anterior).
                # Sem isso, o segundo ponto poderia descer além do limite.
                travel = p['depth'] if test else probe_start_z - p['bottom']
                if not math.isfinite(travel) or travel <= 0:
                    raise RuntimeError(f'Mapa ponto {count}: Z de partida não está acima do limite de sondagem.')
                self.sync_command(f'G91 G38.2 Z{-travel:.4f} F{p["feed"]:g}',
                                  max(10, 60*travel/p['feed']+10))
                # Salvar a posição PRB e retrair imediatamente, sem esperar
                # G4/status nem executar cálculos antes do movimento de subida.
                result = self.probe_result
                if not result or not result[1]:
                    raise RuntimeError(f'Probe não confirmou contato no ponto {count}; mapa descartado.')
                measured = tuple(result[0])
                # UMA ÚNICA SUBIDA após o contato. O próximo comando XY já inclui G90;
                # não enviar qualquer Z seguro antes do próximo ponto.
                self.sync_command(f'G91 G0 Z{p["retract"]:.4f}')
                if test:
                    self.sync_command('G4 P0.01')
                # Sem G4 entre a retracao e o XY seguinte: o GRBL ordena os blocos.
                # O probe seguinte (G38.2) sincroniza o planejador internamente.
                work=tuple(measured[k]-wco[k] for k in range(3))
                if not test:
                    # O próximo XY parte do Z alcançado após a retração relativa.
                    probe_start_z = work[2] + p['retract']
                    if probe_start_z <= work[2]:
                        raise RuntimeError('Retração insuficiente para liberar o contato.')
                if not test:
                    # O [PRB] informa MPos, que pode divergir ligeiramente em XY
                    # por arredondamento/aceleração. Registrar, sem rejeitar Z válido.
                    dx,dy=work[0]-x,work[1]-y
                    if abs(dx)>.05 or abs(dy)>.05:
                        self.emit('log',f'Mapa ponto {count}: PRB XY diferente do alvo (dx={dx:.3f}, dy={dy:.3f}); confira offsets.')
                if test:
                    # Ja retraiu: definir Z da posicao atual igual a retração
                    # para manter o zero da superficie no contato medido.
                    self.sync_command(f'G10 L20 P0 Z{p["retract"]:.4f}')
                    self.work_offset=None
                    self.fresh_status()
                    deadline=time.monotonic()+3
                    while self.work_offset is None and time.monotonic()<deadline:
                        if self.cancel:raise RuntimeError('Operação cancelada.')
                        self.fresh_status()
                        time.sleep(.02)
                    if self.work_offset is None:raise RuntimeError('Sem confirmação do novo zero Z.')
                    wco=tuple(self.work_offset)
                    work=(work[0],work[1],0.0)
                # Sem consulta '?' aqui: ela adicionava espera em cada ponto.
                # O estado de abertura sera validado pelo GRBL antes do proximo G38.2.
                if test:
                    self.fresh_status()
                    if self.probe_state: raise RuntimeError('Probe permanece acionado depois da retração.')
                if self.cancel: raise RuntimeError('Sondagem interrompida.')
                if not test:
                    if work[2] >= p['safe']-.1: raise RuntimeError('Z seguro muito baixo para a superfície medida.')
                    zs[j][i]=work[2]
                    self.emit('probe_progress',count,len(points),x,y,work[2])
            if not test:
                # Somente ao concluir TODAS as medições: subir ao Z seguro,
                # confirmar a parada e só então retornar X0 Y0.
                self.sync_command(f'G90 G0 Z{p["safe"]:.4f}')
                self.sync_command('G4 P0.01')
                self.sync_command('G90 G0 X0 Y0')
                self.sync_command('G4 P0.01')
                self.emit('log', 'Mapa concluído: Z seguro e retorno a X0 Y0.')
                self.emit('log','Mapa: todos os cantos medidos diretamente, 1 mm fora dos limites da placa.')
                self.emit('heightmap',HeightMap(xs,ys,zs,wco,wcs))
            else: self.emit('probe_test',work[2])
        except Exception as exc:
            # Retorno após falha apenas se a controladora ainda responder e
            # confirmar Idle, sem alarme/reset ou contato de probe ativo.
            # Um ALARM ou perda de comunicação exige intervenção do operador:
            # jamais enviar G0 automaticamente nessas condições.
            if not test and not self.cancel and self.port and self.port.is_open:
                try:
                    self.fresh_status(timeout=2)
                    if (not self.cancel and self.machine_state.lower() == 'idle'
                            and self.probe_state is False
                            and self.work_offset is not None
                            and self.work_position is not None):
                        self.emit('log', 'Falha de mapa: controladora Idle e probe aberto; retornando por Z seguro.')
                        self.sync_command(f'G90 G0 Z{p["safe"]:.4f}')
                        self.sync_command('G4 P0.01')
                        self.sync_command('G90 G0 X0 Y0')
                        self.sync_command('G4 P0.01')
                        self.emit('log', 'Retorno seguro concluído: Z seguro, X0 Y0.')
                    else:
                        self.emit('log', 'Retorno automático bloqueado: estado GRBL/probe não seguro. Não mover manualmente sem verificar a máquina.')
                except Exception as recovery_exc:
                    self.emit('log', f'Retorno automático não realizado: {recovery_exc}')
            elif not test:
                self.emit('log', 'Retorno automático bloqueado por alarme, reset, cancelamento ou desconexão.')
            self.cancel=True
            if self.port and self.port.is_open:
                try: self.realtime(b'!')
                except Exception: pass
            self.emit('map_invalid','Medição interrompida')
            self.emit('fault',str(exc))
        finally:
            if original and not self.cancel and self.port and self.port.is_open:
                try:
                    restore=[v for v in original if v in ('G0','G1','G17','G18','G19','G20','G21','G90','G91','G93','G94') or v.startswith('F')]
                    self.sync_command(' '.join(restore))
                except Exception: pass
            self.probing=False; self.running=False
            self.emit('probe_finished')

    def realtime(self, code):
        if self.simulation:
            return
        if not self.port or not self.port.is_open:
            raise RuntimeError('Conecte a controladora primeiro.')
        # Ctrl+X representa reset do GRBL; distinguir reset enviado pelo programa
        # de um reset inesperado ao encostar a ferramenta.
        if b'\x18' in code:
            self.emit('log', '>>> RESET GRBL (Ctrl+X) ENVIADO PELO PROGRAMA')
        # Stops/reset/status must not wait behind a signed command holding the stream lock.
        if code and all(c in SAFE_REALTIME for c in code):
            self.port.write(code)
            return
        # Signed realtime has its own sequence and bounded transmit lock.
        self.port.write(code)

    def wait_m0_complete(self, number):
        """Mostra M0 quando a máquina informa Hold:0, sem esperar um ok tardio."""
        while not self.cancel and self.m0_waiting:
            if self.m0_stopped.is_set():
                self.emit('m0', number)
                break
            time.sleep(.015)
        while self.m0_waiting and not self.cancel:
            time.sleep(.015)

    def prepare_m0(self, number):
        self.m0_stopped.clear()
        self.m0_waiting = True

    @staticmethod
    def m0_macro_lines(command):
        lines = [clean(line) for line in command.splitlines() if clean(line)]
        if not lines:
            raise ValueError('Macro sem movimentos.')
        word = re.compile(r'([A-Z])([+-]?(?:\d+(?:\.\d*)?|\.\d+))')
        for line in lines:
            text = line[3:] if line.startswith('$J=') else line
            words = word.findall(text)
            if not words or word.sub('', text).strip():
                raise ValueError('Em M0 use somente movimentos XYZ, G0/G1, G90/G91, G20/G21 e F.')
            for letter, value in words:
                number = float(value)
                if not math.isfinite(number) or letter not in 'GXYZFM':
                    raise ValueError('Macro M0: comando não permitido; nenhuma linha foi enviada.')
                if letter == 'G' and number not in (0, 1, 20, 21, 90, 91, 94):
                    raise ValueError('Macro M0: sondagem, arcos, homing e alteração de origem não são permitidos.')
                if letter == 'M' and number != 5:
                    raise ValueError('Macro de ajuste: somente M5 é permitido; ferramenta deve ficar desligada.')
                if letter == 'F' and number <= 0:
                    raise ValueError('Macro M0: avanço deve ser positivo.')
        return lines

    def m0_restore_modes(self):
        # Restore the file's modes and feed without re-arming its spindle/laser.
        allowed = {'G0', 'G1', 'G2', 'G3', 'G17', 'G18', 'G19', 'G20', 'G21',
                   'G90', 'G91', 'G93', 'G94', 'G54', 'G55', 'G56', 'G57', 'G58', 'G59'}
        words = [v for v in self._m0_modal if v in allowed or v.startswith('F')]
        if words:
            self.sync_command(' '.join(words))

    def pause_m0_alignment(self, number):
        # Host-managed M0: drain actual motion, then remain Idle with M5.
        paused_port = self.port
        while not self.cancel:
            with self.lock:
                pending = bool(self.inflight)
            if not pending:
                break
            time.sleep(.01)
        if self.cancel:
            raise RuntimeError('M0 cancelado antes da parada.')
        self.sync_command('G4 P0.01', 120)
        self.wait_idle()
        self.modal = None
        self.sync_command('$G')
        self._m0_modal = list(self.modal or [])
        if not self._m0_modal:
            raise RuntimeError('M0: estado modal não confirmado.')
        self.sync_command('M5')
        self.sync_command('$$')
        if self.settings.get('13') != 0:
            raise RuntimeError('M0: configure $13=0 para coordenadas em mm.')
        self.fresh_status()
        if not self.work_position or not all(math.isfinite(v) for v in self.work_position):
            raise RuntimeError('M0: posição XYZ não confirmada.')
        self._m0_anchor = tuple(self.work_position)
        with self._m0_lock:
            self.m0_waiting = True
            self._m0_managed = True
            self.m0_alignment_ready = True
            self._m0_resume.clear()
        self.emit('log', f'M0 linha {number}: parado, M5; ajuste XYZ por movimentos/macros e clique Retornar.')
        self.emit('m0_alignment', number)
        while not self.cancel and not self._m0_resume.wait(.05):
            if self.port is not paused_port or not self.port or not self.port.is_open or getattr(self.port, 'failure', None):
                self.cancel = True
        with self._m0_lock:
            self.m0_alignment_ready = False
            self.m0_waiting = False
            self._m0_managed = False
        if self.cancel or self.port is not paused_port:
            self.cancel = True
            raise RuntimeError('M0 interrompido; trabalho não retomado.')
        self.wait_idle()
        self.m0_restore_modes()
        # Only the explicit Retornar action can restore the file's tool state.
        spindle = next((v for v in self._m0_modal if v in ('M3', 'M4', 'M5')), 'M5')
        speed = next((v for v in self._m0_modal if v.startswith('S')), 'S0')
        self.sync_command(spindle + ' ' + speed)
        self.emit('log', 'M0: retomada manual, alinhamento XYZ preservado por G92.')

    def resume_m0_alignment(self):
        with self._m0_lock:
            if not self.m0_alignment_ready or self._m0_editing or self.cancel:
                raise RuntimeError('M0: aguarde o término do ajuste antes de retornar.')
            self.m0_alignment_ready = False
            self._m0_resume.set()

    def start_m0_alignment(self, command):
        lines = self.m0_macro_lines(command)  # Validate the whole macro before any motion.
        self.validate_serial_lines(enumerate(lines, 1))
        with self._m0_lock:
            if not self.m0_alignment_ready or self._m0_editing or self.cancel:
                raise RuntimeError('M0: ajuste indisponível ou outro ajuste em execução.')
            self._m0_editing = True
        self.emit('m0_busy')
        self.start_worker(self.m0_alignment_loop, (lines,))

    def wait_m0_adjustment_idle(self, timeout=120):
        # $J ACK means accepted, not finished. Ordinary G-code is rejected in Jog.
        deadline = time.monotonic() + timeout
        while True:
            self.fresh_status()
            state = self.machine_state.lower()
            if state == 'idle':
                return
            if state not in ('run', 'jog') or self.cancel:
                raise RuntimeError('Ajuste interrompido no estado ' + self.machine_state)
            if time.monotonic() >= deadline:
                raise TimeoutError('Jog não confirmou parada em Idle; ajuste não repetido.')
            time.sleep(.05)

    def m0_alignment_loop(self, lines):
        try:
            self.wait_idle()
            self.sync_command('M5')
            self.sync_command('G94')
            for line in lines:
                self.sync_command(line, 120)
                if line.startswith('$J='):
                    self.wait_m0_adjustment_idle()
            self.wait_m0_adjustment_idle()
            self.sync_command('G4 P0.01', 120)
            self.wait_idle()
            self.sync_command('G21 G90 G94')
            x, y, z = self._m0_anchor
            self.sync_command(f'G92 X{x:.6f} Y{y:.6f} Z{z:.6f}')
            self.m0_restore_modes()
            self.fresh_status()
            self.emit('log', 'M0: ajuste XYZ concluído; coordenadas de trabalho preservadas.')
        except Exception as exc:
            self.cancel = True
            self.m0_alignment_ready = False
            try: self.realtime(b'!')
            except Exception: pass
            self.emit('fault', 'Ajuste M0 interrompido: ' + str(exc) + '. Confira a posição antes de novo trabalho.')
        finally:
            with self._m0_lock:
                self._m0_editing = False
            self.emit('m0_adjusted')

    @staticmethod
    def validate_serial_lines(commands, limit=None):
        for number, line in commands:
            try:
                payload = line.encode('ascii')
            except UnicodeEncodeError as exc:
                raise ValueError(f'Linha {number}: comandos GRBL devem conter apenas ASCII.') from exc
            if not 1 <= len(payload) <= 200:
                raise ValueError(f'Linha {number}: comando excede o limite de 200 caracteres.')
            if limit is not None and len(payload) + 1 > limit:
                raise ValueError(f'Linha {number}: comando excede o buffer configurado.')

    def send_manual(self, command):
        if self.m0_alignment_ready and not self.simulation:
            self.start_m0_alignment(command)
            return
        if self.running:
            raise RuntimeError('Pare ou conclua o arquivo antes de executar macros.')
        if self.simulation:
            for raw in command.splitlines():
                if clean(raw):
                    self.emit('log', '[Simulação] > ' + clean(raw))
            self.running = True
            self.cancel = False
            self.paused = False
            self.start_worker(self.simulate, (command.splitlines(), True))
            return
        if not self.port or not self.port.is_open:
            raise RuntimeError('Conecte a controladora primeiro.')
        lines = [clean(line) for line in command.splitlines() if clean(line)]
        self.validate_serial_lines(enumerate(lines, 1))
        if not lines:
            return
        self.running = True
        self.cancel = False
        self.cancel_reason = ''
        self.start_worker(self.manual_sequence, ('\n'.join(lines),))

    def manual_sequence(self, command):
        succeeded = False
        try:
            for raw in command.splitlines():
                if self.cancel:
                    break
                line = clean(raw)
                if not line:
                    continue
                if re.search(r'(?<![A-Z])M0+(?:\.0+)?(?![\d.])', line, re.I):
                    while not self.cancel:
                        with self.lock:
                            outstanding = bool(self.inflight)
                        if not outstanding:
                            break
                        time.sleep(.015)
                if self.cancel:
                    break
                is_m0 = bool(re.search(r'(?<![A-Z])M0+(?:\.0+)?(?![\d.])', line, re.I))
                if is_m0:
                    self.prepare_m0('macro_m0')
                native_pause = re.fullmatch(r'(?:N\d+\s*)?M0+(?:\.0+)?', line) is not None
                self.send_payload((line + '\n').encode('ascii'), 'macro_m0' if is_m0 else None,
                                  ack_timeout=math.inf if native_pause else None)
                self.emit('log', '> ' + line)
                if is_m0:
                    self.wait_m0_complete('macro_m0')
            while not self.cancel:
                with self.lock:
                    if not self.inflight:
                        break
                time.sleep(.015)
            succeeded = not self.cancel
        except Exception as exc:
            self.emit('fault', str(exc))
        finally:
            self.running = False
            if succeeded:
                self.emit('macro_done', 'Macro enviada')

    def start(self, lines, limit, segments=None):
        if self.simulation:
            if self.running:
                raise RuntimeError('Já existe uma simulação em execução.')
            self.running = True
            self.paused = False
            self.cancel = False
            self.start_worker(self.simulate, (lines, False))
            return
        if not self.port or not self.port.is_open:
            raise RuntimeError('Conecte a controladora primeiro.')
        if self.running:
            raise RuntimeError('Já existe um arquivo em execução.')
        with self.lock:
            if self.inflight:
                raise RuntimeError('Aguarde a resposta dos comandos manuais.')
        commands = [(i, clean(s)) for i, s in enumerate(lines, 1) if clean(s)]
        if not commands:
            raise RuntimeError('Arquivo sem comandos.')
        self.validate_serial_lines(commands, limit)
        for number, line in commands:
            if re.search(r'(?<![A-Z])M0+(?:\.0+)?(?![\d.])', line) and not re.fullmatch(r'(?:N\d+\s*)?M0+(?:\.0+)?', line):
                raise RuntimeError(f'Linha {number}: coloque M0 sozinho em uma linha para permitir ajuste XYZ.')
        after_pause = False
        for number, line in commands:
            if re.fullmatch(r'(?:N\d+\s*)?M0+(?:\.0+)?', line):
                after_pause = True
            elif after_pause and (re.search(r'G(?:10|92)(?:\.\d+)?(?![\d.])', line) or line.startswith('$H')):
                raise RuntimeError(f'Linha {number}: alteração de origem/homing após a pausa pode desfazer o ajuste fino. Revise o arquivo.')
        # A resposta ao G4 chega após o esvaziamento do planejador de movimentos.
        # Assim o fim do arquivo significa que a máquina terminou, não só que recebeu as linhas.
        commands.append((-1, 'G4 P0.01'))
        self.limit = limit
        self.running = True
        self.cancel = False
        self.paused = False
        # A escolha ocorre para CADA arquivo iniciado, inclusive na fila.
        grbl_mode = grbl_mode_from_z(lines)
        self.start_worker(self.stream_loop, (commands, grbl_mode))

    def simulate(self, lines, macro=False):
        """Executa movimentos G-code no preview respeitando F e o fator de velocidade."""
        total = len(lines)
        try:
            if not total:
                raise RuntimeError('Não há comandos para simular.')
            last_report = 0.0
            for index, raw in enumerate(lines, 1):
                if self.cancel:
                    break
                line = clean(raw)
                if not line:
                    continue
                if re.search(r'(?<![A-Z])M0+(?:\.0+)?(?![\d.])', line, re.I):
                    self.m0_waiting = True
                    self.emit('m0', index)
                    while self.m0_waiting and not self.cancel:
                        time.sleep(.015)
                    if self.cancel:
                        break
                if line.startswith('$H'):
                    self.sim_position = (0.0, 0.0)
                    self.emit('position', 0.0, 0.0, 'Simulação: home')
                    continue
                words = [(m.group(1), float(m.group(2))) for m in WORD.finditer(line)]
                gs = [n for key, n in words if key == 'G']
                if 20 in gs:
                    self.sim_scale = 25.4
                if 21 in gs:
                    self.sim_scale = 1.0
                if 90 in gs:
                    self.sim_absolute = True
                if 91 in gs:
                    self.sim_absolute = False
                for g in gs:
                    if g in (0, 1, 2, 3):
                        self.sim_motion = int(g)
                for key, value in words:
                    if key == 'F' and value > 0:
                        self.sim_feed = value * self.sim_scale
                    elif key == 'S':
                        self.sim_power = value
                    elif key == 'M' and int(value) in (3, 4):
                        self.sim_laser = True
                    elif key == 'M' and int(value) == 5:
                        self.sim_laser = False
                coords = {key: value * self.sim_scale for key, value in words if key in 'XY'}
                x1, y1 = self.sim_position
                if 92 in gs or (10 in gs and any(key == 'L' and value == 20 for key, value in words)):
                    self.sim_position = (coords.get('X', x1), coords.get('Y', y1))
                    self.emit('position', *self.sim_position, 'Simulação: zero definido')
                    continue
                if not coords:
                    if any(key in ('M', 'S') for key, _ in words):
                        state = 'laser ligado' if self.sim_laser and self.sim_power > 0 else 'laser desligado'
                        self.emit('position', x1, y1, 'Simulação: ' + state)
                    continue
                x2 = (coords['X'] if self.sim_absolute else x1 + coords['X']) if 'X' in coords else x1
                y2 = (coords['Y'] if self.sim_absolute else y1 + coords['Y']) if 'Y' in coords else y1
                distance = math.hypot(x2-x1, y2-y1)
                if not distance:
                    continue
                feed = 10000.0 if self.sim_motion == 0 else self.sim_feed
                duration = distance * 60.0 / max(feed * self.sim_speed, 1.0)
                active = self.sim_motion != 0 and self.sim_laser and self.sim_power > 0
                if macro:
                    self.emit('macro_segment', x1, y1, x2, y2, active)
                steps = max(1, math.ceil(duration / .05))
                for step in range(1, steps+1):
                    while self.paused and not self.cancel:
                        time.sleep(.03)
                    if self.cancel:
                        break
                    time.sleep(duration / steps)
                    now = time.monotonic()
                    if now-last_report >= .05 or step == steps:
                        t = step / steps
                        self.sim_position = (x1+(x2-x1)*t, y1+(y2-y1)*t)
                        self.emit('position', *self.sim_position, 'Simulação: macro' if macro else 'Simulação')
                        if not macro:
                            self.emit('progress', index, total)
                        last_report = now
            self.running = False
            self.emit('macro_done' if macro else 'done',
                      'Simulação interrompida' if self.cancel else ('Macro simulada' if macro else 'Simulação concluída'))
        except Exception as exc:
            self.emit('fault', str(exc))
        finally:
            self.running = False

    def stream_loop(self, commands, grbl_mode):
        count = len(commands) - 1  # exclui o sincronizador interno
        sent = 0
        try:
            # Configuração GRBL deve ser confirmada por 'ok' ANTES do primeiro movimento.
            # $32=0: CNC/spindle; $32=1: laser.
            self.sync_command(f'$32={grbl_mode}')
            self.settings['32'] = float(grbl_mode)
            self.emit('log', 'Modo automático: ' + ('LASER ($32=1)' if grbl_mode else 'SPINDLE/FRESA ($32=0)'))
            for number, line in commands:
                if re.fullmatch(r'(?:N\d+\s*)?M0+(?:\.0+)?', line):
                    self.pause_m0_alignment(number)
                    if self.cancel:
                        break
                    self.emit('progress', sent + 1, count)
                    sent += 1
                    continue
                payload = (line + '\n').encode('ascii')
                if len(payload) > self.limit:
                    raise RuntimeError(f'Linha {number} excede o buffer configurado.')
                while not self.cancel:
                    with self.lock:
                        used = sum(size for _, size in self.inflight)
                    if not self.paused and used + len(payload) <= self.limit:
                        break
                    time.sleep(.015)
                if self.cancel:
                    break
                is_m0 = bool(re.search(r'(?<![A-Z])M0+(?:\.0+)?(?![\d.])', line, re.I))
                if is_m0:
                    self.prepare_m0(number)
                self.send_payload(payload, number)
                if number != -1:
                    sent += 1
                    self.emit('progress', sent, count)
                if is_m0:
                    self.wait_m0_complete(number)
            while not self.cancel:
                with self.lock:
                    outstanding = bool(self.inflight)
                if not outstanding:
                    break
                time.sleep(.03)
            self.running = False
            self.emit('done', 'Interrompido' if self.cancel else 'Arquivo confirmado pela controladora')
        except Exception as exc:
            self.cancel = True
            # Best effort only: a USB write failure cannot guarantee a physical stop.
            try: self.realtime(b'!')
            except Exception: pass
            self.emit('fault', 'Envio do arquivo interrompido: ' + str(exc) +
                      ' Nenhum comando sera repetido. Confira a parada da maquina.')
        finally:
            self.m0_alignment_ready = False
            self._m0_managed = False
            self.m0_waiting = False
            self.running = False


class App:
    def __init__(self, root):
        self.root = root
        root.title(f'Controlador PCB — grblHAL / ESP32-S3 N16R8 — {APP_VERSION}')
        root.geometry('1280x840')
        root.minsize(1040, 700)
        try:
            self.config = {**DEFAULT, **json.loads(CONFIG.read_text(encoding='utf-8'))}
        except (OSError, ValueError):
            self.config = dict(DEFAULT)
        self.events = queue.Queue()
        # Criar o log imediatamente na pasta do .py/.exe, sem depender de eventos.
        self.diagnostic_error_shown = False
        try:
            if ATIVAR_LOG:
                with DIAGNOSTIC_LOG.open('a', encoding='utf-8') as diagnostic:
                    diagnostic.write(time.strftime('%Y-%m-%d %H:%M:%S') + ' INICIO DO PROGRAMA\n')
        except OSError as exc:
            self.diagnostic_error_shown = True
            messagebox.showwarning('Diagnóstico GRBL',
                                   f'Não foi possível gravar o log em:\n{DIAGNOSTIC_LOG}\n\n{exc}',
                                   parent=self.root)
        self._mark_zero_in_progress = False
        self._map_enabled_before_zero = False
        self._mark_zero_succeeded = False
        self.stream = Streamer(self.events)
        self.height_map = None
        self.height_enabled = tk.BooleanVar(value=False)
        self.height_status = tk.StringVar(value='Nenhum mapa medido')
        self.probe_label = tk.StringVar(value='PROBE: aguardando status')
        self.height_window = None
        self.height_canvas = None
        self.height_fields = {}
        self.lines = []
        self.segments = []
        self.holes = []
        self.path = None
        self.files = []  # fila de arquivos .nc na ordem de execução
        self.active_file = None
        self.awaiting_idle = False
        self.position = None
        self.controller_state = ''
        self.preview_image = None
        self.preview_transform = None
        self.preview_bitmap = None
        self.processed_index = 0
        self.tracking_started = False
        self.macro_segments = []
        self.port = tk.StringVar(value=str(self.config.get('port', '')))
        self.baud = tk.StringVar(value=str(self.config['baud']))
        self.buffer = tk.StringVar(value=str(self.config['buffer']))
        self.sim_speed = tk.StringVar(value=str(self.config.get('sim_speed', '1.0')))
        self.jog_step = tk.StringVar(value=str(self.config.get('jog_step', '1.0')))
        self.jog_step_z = tk.StringVar(value=str(self.config.get('jog_step_z', self.config.get('jog_step', '1.0'))))
        self.jog_feed_xy = tk.StringVar(value=str(self.config.get('jog_feed_xy', '1000')))
        self.jog_feed_z = tk.StringVar(value=str(self.config.get('jog_feed_z', '300')))
        self.status = tk.StringVar(value='Desconectado')
        self.coordinates = tk.StringVar(value='Posição: aguardando controladora ou simulação')
        self.connection_label = tk.StringVar(value='Serial: desconectada')
        self.last_command = tk.StringVar(value='Comando: —')
        self.last_response = tk.StringVar(value='Resposta: —')
        self.time_label = tk.StringVar(value='Total estimado: --:--:--   |   Tempo corrido: 00:00:00')
        self.job_started = None; self.job_elapsed = 0.0; self.job_estimate = None
        self.camera_index = tk.StringVar(value=str(self.config.get('camera_index', '0')))
        self.camera_status = tk.StringVar(value='Câmera desligada')
        self.camera_flip_x = tk.BooleanVar(value=self.config.get('camera_flip_x', True))
        self.camera_capture = None
        self.camera_thread = None
        self.camera_stop = threading.Event()
        self.camera_lock = threading.Lock()
        self.camera_frame = None
        self.camera_photo = None
        self.camera_active = False
        self.camera_zoom = 1.0
        self.camera_center = (0.5, 0.5)
        self.preview_zoom = 1.0
        self.preview_anchor = None
        self.preview_drag_last = None
        self.camera_drag_last = None
        self.build()
        root.bind('<KeyPress>', self.shortcut, add='+')
        self.refresh_ports()
        self.port.trace_add('write', lambda *_: self.save())
        root.after(50, self.poll)
        root.protocol('WM_DELETE_WINDOW', self.close)

    def shortcut(self, event):
        if event.widget.winfo_toplevel() != self.root: return
        if event.state & 0x0c: return
        if event.widget.winfo_class() in ('Entry','TEntry','Text','TCombobox','Spinbox','TSpinbox'): return
        action = {'i':self.start,'p':self.pause,'r':self.resume,'c':self.stop}.get(event.keysym.lower())
        if action:
            action(); return 'break'

    def finish_timer(self):
        if self.job_started is not None:
            self.job_elapsed = time.monotonic()-self.job_started
            self.job_started = None

    def update_indicators(self):
        port = self.stream.port
        if self.stream.simulation: connection = 'Serial: simulação (sem conexão)'
        elif port and port.is_open and getattr(port, '_recovering', False):
            connection = f'Serial: {port.port} — renovando autenticação, movimento bloqueado'
        elif port and port.is_open and not getattr(port, 'authenticated', True):
            connection = f'Serial: {port.port} — autenticação inválida; reconecte'
        elif port and port.is_open:
            age = time.monotonic()-self.stream.status_time
            state = self.stream.machine_state or 'aguardando status'
            connection = f'Serial: conectada — {port.port} — {state}'
            if age > 3: connection += ' — aguardando resposta'
        else: connection = 'Serial: desconectada'
        self.connection_label.set(connection)
        with self.stream._display_lock:
            command = self.stream.latest_command
            response = self.stream.latest_response
        self.last_command.set('Comando: ' + (command or '—'))
        self.last_response.set('Resposta: ' + (response or '—'))
        elapsed = time.monotonic()-self.job_started if self.job_started is not None else self.job_elapsed
        def clock(seconds):
            seconds = max(0,int(seconds)); return f'{seconds//3600:02d}:{seconds//60%60:02d}:{seconds%60:02d}'
        estimate = self.job_estimate
        if self.active_file is None and self.job_started is None:
            pending = next((item for item in self.files if not item.get('completed')),None)
            if pending and not self.job_elapsed: estimate = estimated_seconds(pending['lines'], self.stream.work_position or (0,0,0),self.stream.settings)
        self.time_label.set(f'Total estimado: {clock(estimate) if estimate is not None else "--:--:--"}   |   Tempo corrido: {clock(elapsed)} (inclui pausas)')

    def build(self):
        style = ttk.Style(self.root)
        if 'clam' in style.theme_names():
            style.theme_use('clam')
        bg, card, ink, muted = '#edf2f7', '#ffffff', '#243247', '#617087'
        self.root.configure(background=bg)
        style.configure('.', font=('Segoe UI', 10), background=bg, foreground=ink)
        style.configure('TFrame', background=bg)
        style.configure('TLabel', background=bg)
        style.configure('TLabelframe', background=bg, bordercolor='#cbd5e1')
        style.configure('TLabelframe.Label', font=('Segoe UI', 10, 'bold'), foreground=ink)
        style.configure('TButton', padding=(10, 6), background=card, bordercolor='#cbd5e1')
        style.map('TButton', background=[('active', '#e2e8f0')])
        style.configure('Start.TButton', background='#157347', foreground='white', font=('Segoe UI', 10, 'bold'))
        style.map('Start.TButton', background=[('active', '#105c38')])
        style.configure('Stop.TButton', background='#b93838', foreground='white')
        style.map('Stop.TButton', background=[('active', '#962b2b')])
        style.configure('Title.TLabel', font=('Segoe UI', 18, 'bold'))
        style.configure('Muted.TLabel', foreground=muted, font=('Segoe UI', 9))
        style.configure('TNotebook', background=bg, borderwidth=0)
        style.configure('TNotebook.Tab', padding=(14, 7))
        style.configure('Horizontal.TProgressbar', background='#157347', troughcolor='#dbe4ef')

        shell = ttk.Frame(self.root, padding=12)
        shell.pack(fill='both', expand=True)
        header = ttk.Frame(shell)
        header.pack(fill='x', pady=(0, 10))
        ttk.Label(header, text='Controlador PCB', style='Title.TLabel').pack(side='left')
        ttk.Label(header, text='grblHAL / ESP32-S3 N16R8  •  Laser e fresa', style='Muted.TLabel').pack(side='left', padx=16)

        top = ttk.LabelFrame(shell, text='Conexão', padding=8)
        top.pack(fill='x', pady=(0, 10))
        for col in (1, 4, 6):
            top.columnconfigure(col, weight=1)
        ttk.Label(top, text='Porta serial').grid(row=0, column=0, padx=(0, 6))
        self.ports = ttk.Combobox(top, textvariable=self.port, width=16)
        self.ports.grid(row=0, column=1, sticky='ew')
        ttk.Button(top, text='Atualizar', command=self.refresh_ports).grid(row=0, column=2, padx=6)
        ttk.Label(top, text='Baud').grid(row=0, column=3, padx=(8, 6))
        ttk.Entry(top, textvariable=self.baud, width=9).grid(row=0, column=4, sticky='ew')
        ttk.Label(top, text='Buffer RX').grid(row=0, column=5, padx=(12, 6))
        ttk.Entry(top, textvariable=self.buffer, width=5).grid(row=0, column=6, sticky='ew')
        ttk.Button(top, text='Conectar', command=self.connect).grid(row=0, column=7, padx=(12, 6))
        ttk.Button(top, text='Desconectar', command=self.disconnect).grid(row=0, column=8)

        serial_line = ttk.Frame(top)
        serial_line.grid(row=1, column=0, columnspan=9, sticky='ew', pady=(6, 0))
        ttk.Label(serial_line, textvariable=self.connection_label, style='Muted.TLabel').pack(side='left')
        exchange_line = ttk.Frame(serial_line)
        exchange_line.pack(side='right', fill='x', expand=True, padx=(16, 0))
        exchange_line.columnconfigure(0, weight=1)
        exchange_line.columnconfigure(1, weight=1)
        ttk.Label(exchange_line, textvariable=self.last_command, style='Muted.TLabel',
                  anchor='e', width=1).grid(row=0, column=0, sticky='ew', padx=(0, 16))
        ttk.Label(exchange_line, textvariable=self.last_response, style='Muted.TLabel',
                  anchor='e', width=1).grid(row=0, column=1, sticky='ew')

        bar = ttk.Frame(shell)
        bar.pack(fill='x', pady=(0, 10))
        for label, action, button_style in [('Iniciar (I)', self.start, 'Start.TButton'), ('Pausar (P)', self.pause, 'TButton'), ('Retornar (R)', self.resume, 'TButton'), ('Cancelar (C)', self.stop, 'Stop.TButton')]:
            ttk.Button(bar, text=label, command=action, style=button_style).pack(side='left', padx=(0, 6))
        ttk.Button(bar, text='Mapa de altura PCB', command=self.open_heightmap).pack(side='left', padx=(8, 6))
        ttk.Spinbox(bar, from_=0.1, to=10.0, increment=0.1, textvariable=self.sim_speed, width=5).pack(side='right')
        ttk.Label(bar, text='Simulação ×', style='Muted.TLabel').pack(side='right', padx=6)

        footer = ttk.Frame(shell, padding=(0, 10, 0, 0))
        footer.pack(side='bottom', fill='x')
        ttk.Label(footer, textvariable=self.coordinates, style='Muted.TLabel').pack(anchor='w', pady=(0, 6))
        ttk.Label(footer,textvariable=self.time_label,style='Muted.TLabel').pack(anchor='w',pady=(0,6))
        self.progress = ttk.Progressbar(footer, maximum=100)
        self.progress.pack(side='left', fill='x', expand=True, padx=(0, 12))
        ttk.Label(footer, textvariable=self.status, width=22, anchor='e').pack(side='right')

        pane = ttk.Panedwindow(shell, orient='horizontal')
        pane.pack(fill='both', expand=True)
        left = ttk.Frame(pane)
        right = ttk.Frame(pane, padding=(10, 0, 0, 0))
        pane.add(left, weight=3)
        pane.add(right, weight=2)

        files_bar = ttk.LabelFrame(left, text='Fila de arquivos • execução na ordem da lista', padding=8)
        files_bar.pack(fill='x', pady=(0, 10))
        files_actions = ttk.Frame(files_bar)
        files_actions.pack(fill='x', pady=(0, 6))
        ttk.Button(files_actions, text='Adicionar .nc', command=self.open_files).pack(side='left')
        ttk.Button(files_actions, text='Limpar', command=self.clear_files).pack(side='right')
        ttk.Button(files_actions, text='Remover', command=self.remove_file).pack(side='right', padx=4)
        ttk.Button(files_actions, text='↓', width=3, command=lambda: self.move_file(1)).pack(side='right')
        ttk.Button(files_actions, text='↑', width=3, command=lambda: self.move_file(-1)).pack(side='right', padx=4)
        files_list_frame = ttk.Frame(files_bar)
        files_list_frame.pack(fill='x')
        self.file_list = tk.Listbox(files_list_frame, height=3, exportselection=False,
                                   font=('Segoe UI', 10), background=card, foreground=ink,
                                   selectbackground='#dbeafe', selectforeground=ink,
                                   relief='flat', highlightthickness=1, highlightbackground='#cbd5e1')
        file_scroll = ttk.Scrollbar(files_list_frame, orient='vertical', command=self.file_list.yview)
        self.file_list.configure(yscrollcommand=file_scroll.set)
        self.file_list.pack(side='left', fill='x', expand=True)
        file_scroll.pack(side='right', fill='y')
        preview_box = ttk.LabelFrame(left, text='Visualização do percurso', padding=2)
        preview_box.pack(fill='both', expand=True)
        self.canvas = tk.Canvas(preview_box, background='#151922', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.bind('<Configure>', lambda _: self.draw())
        self.canvas.bind('<MouseWheel>', self.zoom_preview)
        self.canvas.bind('<Button-4>', self.zoom_preview)
        self.canvas.bind('<Button-5>', self.zoom_preview)
        self.canvas.bind('<Double-Button-1>', self.reset_preview_zoom)
        self.canvas.bind('<ButtonPress-3>', self.begin_preview_pan)
        self.canvas.bind('<B3-Motion>', self.pan_preview)
        self.canvas.bind('<ButtonRelease-3>', self.end_preview_pan)

        notebook = ttk.Notebook(right)
        notebook.pack(fill='both', expand=True)
        controls = ttk.Frame(notebook, padding=8)
        terminal = ttk.Frame(notebook, padding=8)
        camera = ttk.Frame(notebook, padding=8)
        notebook.add(controls, text='Movimentos e macros')
        notebook.add(terminal, text='Terminal / Log')
        notebook.add(camera, text='Câmera')
        self.build_camera_tab(camera)
        jog_box = ttk.LabelFrame(controls, text='Movimento manual • distâncias em mm', padding=8)
        jog_box.pack(fill='x', pady=(0, 10))
        jog_top = ttk.Frame(jog_box)
        jog_top.pack(fill='x', pady=(0, 4))
        ttk.Label(jog_top, text='XY mm:').pack(side='left')
        ttk.Spinbox(jog_top, from_=0.001, to=1000.0, increment=0.1,
                    textvariable=self.jog_step, width=8).pack(side='left', padx=(5, 8))
        ttk.Label(jog_top, text='F XY:').pack(side='left')
        ttk.Entry(jog_top, textvariable=self.jog_feed_xy, width=7).pack(side='left', padx=(3, 7))
        jog_z = ttk.Frame(jog_box)
        jog_z.pack(fill='x', pady=(0, 4))
        ttk.Label(jog_z, text='Z mm:').pack(side='left')
        ttk.Spinbox(jog_z, from_=0.001, to=1000.0, increment=0.1,
                    textvariable=self.jog_step_z, width=8).pack(side='left', padx=(5, 8))
        ttk.Label(jog_z, text='F Z:').pack(side='left')
        ttk.Entry(jog_z, textvariable=self.jog_feed_z, width=7).pack(side='left', padx=(3, 7))

        jog_grid = ttk.Frame(jog_box)
        jog_grid.pack(fill='x')
        for col in range(5):
            jog_grid.columnconfigure(col, weight=1)

        # Disposição tipo controle: Y+ em cima; X-/X+ nas laterais; Y- embaixo.
        ttk.Button(jog_grid, text='Y +', command=lambda: self.jog('Y', 1)).grid(
            row=0, column=1, sticky='nsew', padx=2, pady=2)
        ttk.Button(jog_grid, text='X −', command=lambda: self.jog('X', -1)).grid(
            row=1, column=0, sticky='nsew', padx=2, pady=2)
        ttk.Label(jog_grid, text='XY', anchor='center').grid(
            row=1, column=1, sticky='nsew', padx=2, pady=2)
        ttk.Button(jog_grid, text='X +', command=lambda: self.jog('X', 1)).grid(
            row=1, column=2, sticky='nsew', padx=2, pady=2)
        ttk.Button(jog_grid, text='Y −', command=lambda: self.jog('Y', -1)).grid(
            row=2, column=1, sticky='nsew', padx=2, pady=2)

        ttk.Separator(jog_grid, orient='vertical').grid(
            row=0, column=3, rowspan=3, sticky='ns', padx=5)
        ttk.Button(jog_grid, text='Z +', command=lambda: self.jog('Z', 1)).grid(
            row=0, column=4, sticky='nsew', padx=2, pady=2)
        ttk.Label(jog_grid, text='Z', anchor='center').grid(
            row=1, column=4, sticky='nsew', padx=2, pady=2)
        ttk.Button(jog_grid, text='Z −', command=lambda: self.jog('Z', -1)).grid(
            row=2, column=4, sticky='nsew', padx=2, pady=2)

        macro_box = ttk.LabelFrame(controls, text='Macros', padding=6)
        macro_box.pack(fill='both', expand=True)
        controls_macros = ttk.Frame(macro_box)
        controls_macros.pack(fill='x', pady=(0, 6))
        for col, (label, action) in enumerate([('Adicionar', self.add_macro), ('Editar / remover', self.edit_macro), ('Salvar', self.save_macro_file), ('Carregar', self.load_macro_file)]):
            controls_macros.columnconfigure(col % 2, weight=1)
            ttk.Button(controls_macros, text=label, command=action).grid(row=col // 2, column=col % 2, sticky='ew', padx=3, pady=3)
        self.macros = ttk.Frame(macro_box)
        self.macros.pack(fill='both', expand=True)
        self.make_macros()

        ttk.Label(terminal, text='Comando manual', style='Muted.TLabel').pack(anchor='w', pady=(0, 6))
        command_row = ttk.Frame(terminal)
        command_row.pack(fill='x', pady=(0, 10))
        self.command = ttk.Entry(command_row)
        self.command.pack(side='left', fill='x', expand=True)
        self.command.bind('<Return>', lambda _: self.manual())
        ttk.Button(command_row, text='Enviar', command=self.manual).pack(side='right', padx=(6, 0))
        log_frame = ttk.Frame(terminal)
        log_frame.pack(fill='both', expand=True)
        self.log = tk.Text(log_frame, height=6, width=32, state='disabled', wrap='none',
                           font=('Consolas', 10), background='#151922', foreground='#dbe4ef',
                           relief='flat', padx=8, pady=8)
        log_scroll = ttk.Scrollbar(log_frame, orient='vertical', command=self.log.yview)
        log_x = ttk.Scrollbar(terminal, orient='horizontal', command=self.log.xview)
        self.log.configure(yscrollcommand=log_scroll.set, xscrollcommand=log_x.set)
        self.log.pack(side='left', fill='both', expand=True)
        log_scroll.pack(side='right', fill='y')
        log_x.pack(fill='x')

    def open_heightmap(self):
        if self.height_window and self.height_window.winfo_exists():
            self.height_window.lift(); return
        w=tk.Toplevel(self.root); self.height_window=w
        w.title('Mapa de altura PCB — fresagem'); w.geometry('850x740')
        ttk.Label(w,text='Fixe a placa e use a mesma fresa para medir e fresar.\nMantenha os zeros e a fixação após medir. Retire o cabo da fresa antes de ligar o spindle.',padding=10).pack(fill='x')
        frame=ttk.Frame(w,padding=10); frame.pack(fill='x')
        defaults={'xmin':('X mínimo (mm)','0'),'xmax':('X máximo (mm)','100'),
                  'ymin':('Y mínimo (mm)','0'),'ymax':('Y máximo (mm)','80'),
                  'sx':('Quantidade de pontos X','6'),'sy':('Quantidade de pontos Y','6'),
                  'safe':('Z seguro absoluto (mm)','3'),'bottom':('Z limite absoluto (mm)','-2'),
                  'feed':('Probe F (mm/min)','60'),'retract':('Retração (mm)','2'),
                  'depth':('Descida máx. teste (mm)','5')}
        for n,(key,(label,value)) in enumerate(defaults.items()):
            if key not in self.height_fields: self.height_fields[key]=tk.StringVar(value=str(self.config.get('probe',{}).get(key,value)))
            row,col=divmod(n,2)
            ttk.Label(frame,text=label).grid(row=row,column=col*2,sticky='w',padx=5,pady=3)
            ttk.Entry(frame,textvariable=self.height_fields[key],width=10).grid(row=row,column=col*2+1,padx=5,pady=3)
        buttons=ttk.Frame(w,padding=10); buttons.pack(fill='x')
        for label,action in [('Área do arquivo',self.height_area),('Marcar Zero',lambda:self.measure_height(True)),('Mapear PCB',lambda:self.measure_height(False)),('Limpar mapa',self.clear_heightmap),('Cancelar (C)',self.stop)]:
            ttk.Button(buttons,text=label,command=action).pack(side='left',padx=2)
        archive=ttk.Frame(w,padding=(10,0));archive.pack(fill='x')
        for label,action in [('Salvar mapa',self.save_heightmap),('Carregar mapa',self.load_heightmap),('Exportar .nc compensado',self.export_compensated)]:
            ttk.Button(archive,text=label,command=action).pack(side='left',padx=3)
        ttk.Checkbutton(w,text='Compensar Z em arquivos de fresagem',variable=self.height_enabled).pack(anchor='w',padx=12)
        ttk.Label(w,textvariable=self.probe_label).pack(anchor='w',padx=12,pady=5)
        ttk.Label(w,textvariable=self.height_status,wraplength=720).pack(anchor='w',padx=12)
        ttk.Label(w,text='G-code compensado: G21/G90, G0/G1 e arcos XY G2/G3.\nLaser e furação usam o envio original. Alturas exibidas no zero de trabalho atual.',padding=10).pack(anchor='w')
        self.height_canvas=tk.Canvas(w,bg='#151922',height=270,highlightthickness=0)
        self.height_canvas.pack(fill='both',expand=True,padx=10,pady=10)
        self.height_canvas.bind('<Configure>',lambda e:self.draw_heightmap())
        self.height_area()
        self.draw_heightmap()

    def height_area(self):
        index=next((i for i,f in enumerate(self.files) if not f.get('completed')),None)
        if index is None: return
        all_segs=self.files[index]['segments']
        segs=[s for s in all_segs if s[4]=='cut'] or all_segs
        if not segs: return
        xs=[v for s in segs for v in (s[0],s[2])]; ys=[v for s in segs for v in (s[1],s[3])]
        for key,value in [('xmin',math.floor(min(xs)*1000)/1000),('xmax',math.ceil(max(xs)*1000)/1000),('ymin',math.floor(min(ys)*1000)/1000),('ymax',math.ceil(max(ys)*1000)/1000)]: self.height_fields[key].set(f'{value:.3f}')

    def machine_command(self,command):
        try:self.stream.send_manual(command)
        except Exception as exc:messagebox.showerror('Controladora',str(exc))

    def go_z_zero(self):
        try:
            if self.stream.running or self.awaiting_idle:
                raise RuntimeError('Aguarde a operação terminar antes de ir para Z0.')
            if not self.stream.port or not self.stream.port.is_open or self.stream.simulation:
                raise RuntimeError('Conecte a controladora primeiro.')
            with self.stream.lock:
                if self.stream.inflight:raise RuntimeError('Aguarde os comandos anteriores.')
            feed=self.jog_feed_value('Z')
            self.stream.begin_z_zero(feed)
            self.status.set('Movendo para Z0 com detecção do probe')
        except Exception as exc:
            messagebox.showerror('Ir para Z0',str(exc))

    def zero_axis(self,axis):
        try:
            if self.stream.running:raise RuntimeError('Aguarde a operação terminar.')
            if not self.stream.port or self.stream.machine_state.lower()!='idle':raise RuntimeError('Conecte a máquina e aguarde Idle.')
            self.stream.send_manual(f'G10 L20 P0 {axis}0')
        except Exception as exc:messagebox.showerror('Zero de trabalho',str(exc))

    def save_heightmap(self):
        try:
            if self.height_map is None:raise ValueError('Meça ou carregue um mapa primeiro.')
            m=self.height_map
            filename=filedialog.asksaveasfilename(title='Salvar mapa de altura',defaultextension='.json',initialfile='mapa_altura.json',filetypes=[('Mapa de altura','*.json')])
            if not filename:return
            data={'format':'ControladorPCB-heightmap','version':1,'units':'mm','xs':m.xs,'ys':m.ys,'zs':m.zs,'wco':list(m.wco),'wcs':m.wcs}
            Path(filename).write_text(json.dumps(data,indent=2,allow_nan=False),encoding='utf-8')
            self.height_status.set('Mapa salvo: '+Path(filename).name)
        except Exception as exc:messagebox.showerror('Salvar mapa',str(exc))

    def load_heightmap(self):
        try:
            if self.stream.running:raise RuntimeError('Aguarde a operação terminar.')
            filename=filedialog.askopenfilename(title='Carregar mapa de altura',filetypes=[('Mapa de altura','*.json')])
            if not filename:return
            data=json.loads(Path(filename).read_text(encoding='utf-8'))
            if data.get('format')!='ControladorPCB-heightmap' or data.get('version')!=1 or data.get('units')!='mm':raise ValueError('Formato de mapa incompatível.')
            m=HeightMap(data['xs'],data['ys'],data['zs'],data['wco'],data['wcs'])
            self.height_map=m;self.height_enabled.set(True)
            self.height_status.set('Mapa carregado e compensação ativada; posicionamento manual dos zeros.')
            self.draw_heightmap()
        except Exception as exc:messagebox.showerror('Carregar mapa',str(exc))

    def export_compensated(self):
        try:
            if self.stream.running:raise RuntimeError('Aguarde a operação terminar.')
            index=next((i for i,item in enumerate(self.files) if not item.get('completed')),None)
            if index is None:raise ValueError('Carregue um arquivo .nc.')
            item=self.files[index];m=self.height_map
            if m is None:raise ValueError('Meça ou carregue o mapa de altura.')
            if not self.stream.port or not self.stream.port.is_open:raise ValueError('Conecte a mesma máquina para validar os zeros e a posição inicial.')
            if self.stream.inflight:raise ValueError('Aguarde as respostas dos comandos anteriores.')
            self.stream.cancel=False;self.stream.fresh_status()
            self.stream.modal=None;self.stream.sync_command('$G')
            self.stream.wait_idle()
            result=m.compensate(item['lines'],self.stream.work_position)
            filename=filedialog.asksaveasfilename(title='Salvar .nc compensado',defaultextension='.nc',initialfile=Path(item['path']).stem+'_compensado.nc',filetypes=[('G-code','*.nc')])
            if not filename:return
            if Path(filename).resolve()==Path(item['path']).resolve():raise ValueError('Escolha outro nome para preservar o original.')
            header='(Z compensado: desative o mapa ao executar este arquivo)\n'
            Path(filename).write_text(header+'\n'.join(result)+'\n',encoding='ascii')
            self.height_status.set('Arquivo compensado salvo. Execute com a compensação DESATIVADA e os mesmos zeros.')
        except Exception as exc:messagebox.showerror('Exportar compensação',str(exc))

    def clear_heightmap(self):
        self.height_map=None; self.height_enabled.set(False)
        self.height_status.set('Nenhum mapa medido'); self.draw_heightmap()

    def measure_height(self,test):
        try:
            raw={k:v.get().replace(',','.') for k,v in self.height_fields.items()}
            common=('safe','bottom','feed','retract','depth')
            p={k:float(raw[k]) for k in common}
            if not all(math.isfinite(v) for v in p.values()):
                raise ValueError('Use números finitos.')
            if p['feed']<=0 or p['retract']<=0 or p['depth']<=0:
                raise ValueError('Avanço, retração e descida devem ser positivos.')
            if p['safe']<=0:
                raise ValueError('Z seguro deve ser positivo.')
            if test:
                title='Marcar Zero (3 pontos)'
                message=('Ligue o sensor de probe e posicione manualmente a fresa no centro do furo X0 Y0.\n'
                         'Serão medidos X-1 Y-1, X+1 Y-1 e X-1 Y+1.\n'
                         'A origem Z será calculada somente após os três contatos.\n'
                         'Confira curso livre em Z e XY. Iniciar?')
            else:
                area={k:float(raw[k]) for k in ('xmin','xmax','ymin','ymax')}
                if not all(math.isfinite(v) for v in area.values()):
                    raise ValueError('Área inválida.')
                p.update(area)
                if p['xmax']<=p['xmin'] or p['ymax']<=p['ymin']:
                    raise ValueError('Limites da área inválidos.')
                if p['safe']<=p['bottom']:
                    raise ValueError('Z seguro deve ficar acima do limite de sondagem.')
                for axis in ('x','y'):
                    count=float(raw['s'+axis])
                    if not math.isfinite(count) or count!=int(count) or count<2 or count>501:
                        raise ValueError('Quantidade de pontos deve ser inteira entre 2 e 501.')
                    count=int(count)
                    lo=p[axis+'min']-1.0
                    hi=p[axis+'max']+1.0
                    p[axis+'s']=[lo+(hi-lo)*i/(count-1) for i in range(count)]
                if len(p['xs'])*len(p['ys'])>10000:
                    raise ValueError('Máximo de 10.000 pontos por mapa.')
                title='Mapear PCB'
                message=(f"Serão medidos {len(p['xs'])*len(p['ys'])} pontos.\n"
                         f"X de {p['xs'][0]:.3f} até {p['xs'][-1]:.3f}; "
                         f"Y de {p['ys'][0]:.3f} até {p['ys'][-1]:.3f}.\n"
                         'Margem de 1 mm para fora dos quatro limites informados.\n'
                         'A malha começa da posição final X0 Y0 e Z seguro deixada pelo Marcar Zero.\n'
                         'Confirme que TODOS os pontos externos são condutivos.\n'
                         'O limite Z do mapa é absoluto. Iniciar?')
            if not messagebox.askokcancel(title,message,parent=self.height_window):
                return
            self.config['probe']={k:v.get() for k,v in self.height_fields.items()}
            self.save()
            if test:
                # Manter os dados do mapa mesmo se a marcação de zero falhar.
                # Bloquear a compensação até confirmar o NOVO referencial Z0.
                self.stream.begin_mark_zero_three(p)
                self._mark_zero_in_progress = True
                self._mark_zero_succeeded = False
                self._map_enabled_before_zero = self.height_enabled.get()
                if self.height_map is not None:
                    self.height_enabled.set(False)
            else:
                self.stream.begin_probe(p,False)
                self.clear_heightmap()
            self.height_status.set('Marcando Zero (3 pontos); mapa preservado...' if test else 'Medindo mapa...')
            self.update_macro_availability()
        except Exception as exc:
            messagebox.showerror('Mapa de altura',str(exc))

    def draw_heightmap(self):
        c=self.height_canvas
        if not c or not c.winfo_exists(): return
        c.delete('all'); m=self.height_map
        if not m: return
        width,height=max(100,c.winfo_width()),max(100,c.winfo_height())
        low=min(v for row in m.zs for v in row); high=max(v for row in m.zs for v in row)
        nx,ny=len(m.xs),len(m.ys)
        for j,row in enumerate(m.zs):
            for i,z in enumerate(row):
                t=(z-low)/(high-low) if high>low else .5
                color=f'#{int(40+210*t):02x}{int(180-100*t):02x}{int(240-200*t):02x}'
                x0=40+i*(width-60)/nx; y0=20+(ny-1-j)*(height-65)/ny
                c.create_rectangle(x0,y0,x0+(width-60)/nx,y0+(height-65)/ny,fill=color,outline='')
                if nx<=12 and ny<=12: c.create_text(x0+(width-60)/nx/2,y0+(height-65)/ny/2,text=f'{z:.3f}',fill='white')
        c.create_text(width/2,height-20,text=f'X {m.xs[0]:g} → {m.xs[-1]:g} mm | Y {m.ys[0]:g} → {m.ys[-1]:g} mm (baixo → cima) | Z {low:.4f} → {high:.4f} mm',fill='white')

    def open_terminal(self):
        window = tk.Toplevel(self.root)
        window.title('Terminal / Log GRBL')
        window.geometry('620x520')
        window.transient(self.root)

        manual_box = ttk.Frame(window, padding=10)
        manual_box.pack(fill='x')
        ttk.Label(manual_box, text='Comando manual').pack(anchor='w')
        entry = ttk.Entry(manual_box)
        entry.pack(fill='x', pady=(4, 4))

        def send_from_popup(_event=None):
            command = entry.get().strip()
            if not command:
                return
            try:
                self.prepare_manual_simulation()
                self.stream.send_manual(self.resolve_command(command))
                entry.delete(0, 'end')
            except Exception as exc:
                messagebox.showerror('Comando', str(exc), parent=window)

        entry.bind('<Return>', send_from_popup)
        ttk.Button(manual_box, text='Enviar comando', command=send_from_popup).pack(anchor='e')

        ttk.Label(window, text='Log serial', padding=(10, 4, 10, 0)).pack(anchor='w')
        log_frame = ttk.Frame(window, padding=(10, 0, 10, 10))
        log_frame.pack(fill='both', expand=True)
        popup_log = tk.Text(log_frame, state='disabled', wrap='none')
        yscroll = ttk.Scrollbar(log_frame, orient='vertical', command=popup_log.yview)
        xscroll = ttk.Scrollbar(log_frame, orient='horizontal', command=popup_log.xview)
        popup_log.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        popup_log.grid(row=0, column=0, sticky='nsew')
        yscroll.grid(row=0, column=1, sticky='ns')
        xscroll.grid(row=1, column=0, sticky='ew')
        log_frame.rowconfigure(0, weight=1)
        log_frame.columnconfigure(0, weight=1)

        # Copia o log atual e mantém esta janela sincronizada enquanto aberta.
        try:
            current = self.log.get('1.0', 'end-1c')
        except Exception:
            current = ''
        popup_log.configure(state='normal')
        if current:
            popup_log.insert('end', current)
        popup_log.configure(state='disabled')
        popup_log.see('end')

        def sync_log():
            if not window.winfo_exists():
                return
            try:
                current_text = self.log.get('1.0', 'end-1c')
                popup_text = popup_log.get('1.0', 'end-1c')
                if current_text != popup_text:
                    popup_log.configure(state='normal')
                    popup_log.delete('1.0', 'end')
                    popup_log.insert('end', current_text)
                    popup_log.configure(state='disabled')
                    popup_log.see('end')
            except tk.TclError:
                return
            window.after(250, sync_log)

        sync_log()
        entry.focus_set()

    def refresh_ports(self):
        ports = [p.device for p in list_ports.comports()] if list_ports else []
        self.ports['values'] = ports
        # Deixe em branco para permitir a simulação mesmo com portas disponíveis.

    def open_file(self):
        # Compatibilidade com versões anteriores.
        self.open_files()

    def open_files(self):
        if self.stream.running or self.awaiting_idle:
            messagebox.showwarning('Fila', 'Aguarde o arquivo atual terminar antes de alterar a fila.')
            return
        paths = filedialog.askopenfilenames(
            title='Adicionar arquivos G-code',
            filetypes=[('G-code', '*.nc *.gcode *.ncb *.txt'), ('Todos', '*.*')])
        if not paths:
            return
        try:
            added = 0
            for path in paths:
                lines = Path(path).read_text(encoding='utf-8-sig', errors='replace').splitlines()
                preview = analyze_preview(lines)
                self.files.append({
                    'path': path,
                    'lines': lines,
                    'segments': preview['segments'],
                    'holes': preview['holes'],
                    'warnings': preview['warnings'],
                    'mode': preview['mode'],
                })
                added += 1
            self.rebuild_job()
            self.status.set(f'{added} arquivo(s) adicionado(s) — {len(self.files)} na fila')
        except Exception as exc:
            messagebox.showerror('Arquivo', str(exc))

    def rebuild_job(self):
        self.active_file = None
        self.awaiting_idle = False
        self.lines = []
        self.segments = []
        self.holes = []
        warnings = []
        segment_offset = 0
        for item in self.files:
            # Cada arquivo entra integralmente e na ordem exibida na lista.
            self.lines.extend(item['lines'])
            self.segments.extend(item['segments'])
            for hx, hy, index in item.get('holes', []):
                self.holes.append((hx, hy, index + segment_offset))
            warnings.extend(item.get('warnings', []))
            segment_offset += len(item['segments'])
        self.path = self.files[0]['path'] if self.files else None
        self.macro_segments = []
        self.processed_index = 0
        self.tracking_started = False
        self.progress['value'] = 0
        self.refresh_file_list()
        self.draw()
        if warnings:
            unique = list(dict.fromkeys(warnings))
            messagebox.showwarning('Avisos do preview', '\n'.join(unique))

    def refresh_file_list(self):
        if not hasattr(self, 'file_list'):
            return
        self.file_list.delete(0, 'end')
        total = len(self.files)
        laser_no = 0
        laser_names = ('PRETO 100%', 'CINZA ESCURO 75%', 'CINZA CLARO 50%', 'CINZA 25%')
        for i, item in enumerate(self.files, 1):
            layer = '  [BASE]' if i == 1 and total > 1 else ('  [TOPO]' if i == total and total > 1 else '')
            extra = ''
            if item.get('mode') == 'laser':
                laser_no += 1
                color_name = laser_names[min(laser_no - 1, len(laser_names) - 1)]
                extra = f'  [LASER {laser_no}: {color_name}]'
            self.file_list.insert('end', f'{i:02d}  {Path(item["path"]).name}{extra}{layer}')
            if item.get('completed'):
                self.file_list.itemconfig(i-1, background='#237a36', foreground='white', selectbackground='#237a36')
            elif i-1 == next((n for n, f in enumerate(self.files) if not f.get('completed')), -1):
                self.file_list.itemconfig(i-1, background='#ffe066', foreground='#202020', selectbackground='#e5bf40')

    def move_file(self, direction):
        if self.stream.running or self.awaiting_idle:
            return
        selection = self.file_list.curselection()
        if not selection:
            return
        index = selection[0]
        target = index + direction
        if not 0 <= target < len(self.files):
            return
        self.files[index], self.files[target] = self.files[target], self.files[index]
        self.rebuild_job()
        self.file_list.selection_set(target)
        self.file_list.activate(target)
        self.file_list.see(target)

    def remove_file(self):
        if self.stream.running or self.awaiting_idle:
            return
        selection = self.file_list.curselection()
        if not selection:
            return
        del self.files[selection[0]]
        self.rebuild_job()
        self.status.set(f'{len(self.files)} arquivo(s) na fila')

    def clear_files(self):
        if self.stream.running or self.awaiting_idle:
            return
        self.files.clear()
        self.rebuild_job()
        self.status.set('Fila de arquivos vazia')

    def load_file(self, path):
        # Mantido apenas para compatibilidade com chamadas antigas.
        try:
            lines = Path(path).read_text(encoding='utf-8-sig', errors='replace').splitlines()
            preview = analyze_preview(lines)
            self.events.put(('loaded', path, lines, preview['segments'], preview['holes'], preview['warnings']))
        except Exception as exc:
            self.events.put(('fault', str(exc)))

    def zoom_preview(self, event):
        if self.preview_transform is None:
            return
        direction = (1 if event.num == 4 else -1) if getattr(event, 'num', None) in (4, 5) else (1 if event.delta > 0 else -1)
        old = self.preview_zoom
        self.preview_zoom = max(0.2, min(30.0, old * (1.2 if direction > 0 else 1 / 1.2)))
        if self.preview_zoom == old:
            return 'break'
        xmin, ymin, scale, ox, oy, h = self.preview_transform
        # Mantém o ponto do percurso debaixo do cursor durante o zoom.
        wx = xmin + (event.x - ox) / scale
        wy = ymin + (h - oy - event.y) / scale
        self.preview_anchor = (wx, wy, event.x, event.y)
        self.draw()
        return 'break'

    def begin_preview_pan(self, event):
        if self.preview_transform is not None:
            self.preview_drag_last = (event.x, event.y)
            self.canvas.configure(cursor='fleur')
        return 'break'

    def pan_preview(self, event):
        if self.preview_drag_last is None or self.preview_transform is None:
            return 'break'
        dx = event.x - self.preview_drag_last[0]
        dy = event.y - self.preview_drag_last[1]
        self.preview_drag_last = (event.x, event.y)
        if dx or dy:
            xmin, ymin, scale, ox, oy, h = self.preview_transform
            # Fixa um ponto conhecido do percurso e desloca sua posição na tela.
            wx = xmin + (event.x - dx - ox) / scale
            wy = ymin + (h - oy - (event.y - dy)) / scale
            self.preview_anchor = (wx, wy, event.x, event.y)
            self.draw()
        return 'break'

    def end_preview_pan(self, event=None):
        self.preview_drag_last = None
        self.canvas.configure(cursor='')
        return 'break'

    def reset_preview_zoom(self, event=None):
        self.preview_zoom = 1.0
        self.preview_anchor = None
        self.preview_drag_last = None
        self.draw()
        return 'break'

    def draw(self):
        """Desenha o preview em camadas transparentes."""
        canvas = self.canvas
        canvas.delete('all')
        self.preview_transform = None

        visible = list(self.segments) or list(self.macro_segments)
        if not visible and self.position is not None:
            visible = [(0.0, 0.0, self.position[0], self.position[1], 'travel')]
        if not visible and not self.holes:
            canvas.create_text(20, 20, anchor='nw', fill='#5b6472',
                               text='Abra um arquivo .nc para visualizar o percurso XY')
            return

        xs = []
        ys = []
        for x1, y1, x2, y2, _ in visible:
            xs.extend((x1, x2))
            ys.extend((y1, y2))
        for hx, hy, _ in self.holes:
            xs.append(hx)
            ys.append(hy)
        if self.position is not None:
            xs.append(self.position[0])
            ys.append(self.position[1])

        xmin, xmax, ymin, ymax = min(xs), max(xs), min(ys), max(ys)
        w, h = max(canvas.winfo_width(), 100), max(canvas.winfo_height(), 100)
        margin = 82
        scale = min((w - margin) / max(xmax - xmin, 1),
                    (h - margin) / max(ymax - ymin, 1))
        scale *= self.preview_zoom
        ox = (w - (xmax - xmin) * scale) / 2
        oy = (h - (ymax - ymin) * scale) / 2
        if self.preview_anchor is not None:
            wx, wy, px, py = self.preview_anchor
            ox = px - (wx - xmin) * scale
            oy = h - py - (wy - ymin) * scale

        def pt(x, y):
            return ox + (x - xmin) * scale, h - oy - (y - ymin) * scale

        aa = 3
        size = (w * aa, h * aa)
        base = Image.new('RGBA', size, (255, 255, 255, 255))
        black_union = Image.new('L', size, 0)

        def hp(x, y):
            px, py = pt(x, y)
            return int(round(px * aa)), int(round(py * aa))

        def hole_radius():
            return max(3, min(8, int(round(scale * 0.18 + 2))))

        def width_for(kind):
            if kind in ('laser_active', 'cut'):
                return max(2, 2 * aa)
            return max(1, aa)

        def layer_alpha(index, total):
            if total <= 1:
                return 255
            topness = index / max(total - 1, 1)
            return int(round(220 - 80 * topness))

        def paste_color(img, mask, color):
            if mask.getbbox() is not None:
                img.paste(color, (0, 0), mask)

        def draw_masked_line(mask, x1, y1, x2, y2, width):
            d = ImageDraw.Draw(mask)
            d.line((*hp(x1, y1), *hp(x2, y2)), fill=255, width=width)

        def draw_hole(draw, x, y, fill, outline=None, radius=None):
            # A camada é renderizada em resolução AA (supersampling), então
            # posição e raio do furo também precisam ser multiplicados por aa.
            radius = hole_radius() if radius is None else radius
            px, py = hp(x, y)
            r = max(2 * aa, int(round(radius * aa)))
            draw.ellipse((px-r, py-r, px+r, py+r), fill=fill, outline=outline, width=max(1, aa))

        axis = ImageDraw.Draw(base)
        x0, y0 = pt(0, 0)
        if 0 <= x0 < w:
            axis.line((int(x0 * aa), 0, int(x0 * aa), h * aa), fill=(228, 231, 235, 255), width=aa)
        if 0 <= y0 < h:
            axis.line((0, int(y0 * aa), w * aa, int(y0 * aa)), fill=(228, 231, 235, 255), width=aa)

        # As cores das camadas de laser dependem apenas da ordem dos arquivos LASER.
        # Arquivos de borda/furação não interferem nessa numeração.
        laser_items = [item for item in self.files if item.get('mode') == 'laser']
        laser_order = {id(item): i for i, item in enumerate(laser_items)}
        laser_colors = [
            (0, 0, 0, 255),         # 1º laser: preto sólido, 100% opaco
            (70, 70, 70, 191),      # 2º laser: cinza escuro, 75% de opacidade
            (160, 160, 160, 128),   # 3º laser: cinza claro, 50% de opacidade
            (205, 205, 205, 64),    # 4º laser: cinza, 25% de opacidade
        ]

        total_files = len(self.files)
        for file_index, item in enumerate(self.files):
            mode = item.get('mode', 'generic')
            alpha = layer_alpha(file_index, total_files)
            layer = Image.new('RGBA', size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(layer)

            if mode == 'laser':
                laser_index = laser_order[id(item)]
                # 1º = preto 100%; 2º = cinza escuro 75%; 3º = cinza claro 50%;
                # 4º e seguintes = cinza 25%.
                laser_color = laser_colors[min(laser_index, len(laser_colors) - 1)]
                for x1, y1, x2, y2, kind in item.get('segments', []):
                    if kind != 'laser_active':
                        if not any(seg[4]=='laser_active' for seg in item.get('segments',[])):
                            draw.line((*hp(x1,y1),*hp(x2,y2)),fill=(0,102,255,255),width=aa)
                        continue
                    draw.line((*hp(x1, y1), *hp(x2, y2)),
                              fill=laser_color, width=width_for(kind))
            else:
                for x1, y1, x2, y2, kind in item.get('segments', []):
                    if kind == 'cut':
                        if mode in ('drill', 'milling'):
                            # Furação/fresagem: qualquer movimento XY com ferramenta abaixo de Z0
                            # é mostrado em vermelho para não se confundir com as camadas de laser.
                            color = (255, 0, 0, 255)
                            draw.line((*hp(x1, y1), *hp(x2, y2)), fill=color, width=width_for(kind))
                        else:
                            draw.line((*hp(x1, y1), *hp(x2, y2)),
                                      fill=(0, 0, 0, alpha), width=width_for(kind))
                        continue
                    if kind == 'drill_travel':
                        # Arquivo de furação: deslocamento XY entre furos em azul.
                        color = (0, 102, 255, 255)
                    elif kind == 'travel':
                        # Deslocamentos de fresagem permanecem azuis; cortes ficam vermelhos.
                        color = (0, 102, 255, 255 if mode == 'milling' else alpha)
                    elif kind == 'laser_travel':
                        continue
                    else:
                        color = (0, 102, 255, alpha)
                    draw.line((*hp(x1, y1), *hp(x2, y2)), fill=color, width=width_for(kind))
                for hx, hy, _ in item.get('holes', []):
                    # Posições efetivas de furação em vermelho vivo.
                    draw_hole(draw, hx, hy, fill=(255, 0, 0, 255), outline=(150, 0, 0, 255))

            base.alpha_composite(layer)

        picture = base.resize((w, h), Image.Resampling.LANCZOS).convert('RGB')
        self.preview_image = ImageTk.PhotoImage(picture)
        self.preview_bitmap = picture.copy()
        canvas.create_image(0, 0, anchor='nw', image=self.preview_image)
        self.preview_transform = (xmin, ymin, scale, ox, oy, h)

        if self.processed_index:
            self.paint_processed(0, self.processed_index)

        canvas.create_text(
            12, 10, anchor='nw', fill='#101418',
            text=(f'X {xmin:.2f}…{xmax:.2f} mm   Y {ymin:.2f}…{ymax:.2f} mm\n'
                  'Azul: trajeto de furação/deslocamento   Vermelho: furos   '
                  'Laser 1: preto 100%   Laser 2: cinza escuro 75%   '
                  'Laser 3: cinza claro 50%   Laser 4: cinza 25%   Verde: executado'))

        x0, y0 = pt(0, 0)
        canvas.create_oval(x0-4, y0-4, x0+4, y0+4, fill='#ffbb55', outline='#7a4d00', width=1)

        for segment in self.macro_segments:
            self.draw_macro_segment(segment)
        self.draw_position()

    def draw_macro_segment(self, segment):
        if self.preview_transform is None:
            return
        x1, y1, x2, y2, active = segment
        xmin, ymin, scale, ox, oy, h = self.preview_transform
        self.canvas.create_line(ox+(x1-xmin)*scale, h-oy-(y1-ymin)*scale,
                                ox+(x2-xmin)*scale, h-oy-(y2-ymin)*scale,
                                fill='#ff4444' if active else '#36c6ed', width=2,
                                tags='macro_path')
        self.canvas.tag_raise('position')

    def draw_position(self):
        c = self.canvas
        c.delete('position')
        if self.preview_transform is None:
            return
        if self.position is not None:
            xmin, ymin, scale, ox, oy, h = self.preview_transform
            px = ox + (self.position[0] - xmin) * scale
            py = h - oy - (self.position[1] - ymin) * scale
            c.create_line(px-12, py, px+12, py, fill='#ff3434', width=2, tags='position')
            c.create_line(px, py-12, px, py+12, fill='#ff3434', width=2, tags='position')
            c.create_oval(px-4, py-4, px+4, py+4, outline='#ff3434', width=2, tags='position')

    def paint_processed(self, start, end):
        """Pinta de verde o que já foi executado."""
        if self.preview_bitmap is None or self.preview_transform is None:
            return
        xmin, ymin, scale, ox, oy, h = self.preview_transform
        pen = ImageDraw.Draw(self.preview_bitmap)

        def line_points(x1, y1, x2, y2):
            return (ox + (x1-xmin)*scale, h-oy-(y1-ymin)*scale,
                    ox + (x2-xmin)*scale, h-oy-(y2-ymin)*scale)

        def hole_radius():
            return max(3, min(8, int(round(scale * 0.18 + 2))))

        for x1, y1, x2, y2, kind in self.segments[start:end]:
            width = 4 if kind in ('laser_active', 'cut') else 3
            pen.line(line_points(x1, y1, x2, y2), fill='#00aa32', width=width)

        for hx, hy, index in self.holes:
            if start <= index < end:
                px = ox + (hx-xmin)*scale
                py = h-oy-(hy-ymin)*scale
                r = hole_radius()
                pen.ellipse((px-r, py-r, px+r, py+r), fill='#00aa32', outline='#007a24')

        self.preview_image.paste(self.preview_bitmap)

    def track_position(self):
        if not self.tracking_started or not self.segments or self.position is None:
            return
        px, py = self.position
        start = self.processed_index
        file_end = (sum(len(f['segments']) for f in self.files[:self.active_file+1])
                    if self.active_file is not None else len(self.segments))
        end = min(start + 3000, file_end)
        best = start
        best_distance = float('inf')
        for i in range(start, end):
            x1, y1, x2, y2, _ = self.segments[i]
            dx, dy = x2-x1, y2-y1
            length2 = dx*dx + dy*dy
            t = max(0.0, min(1.0, ((px-x1)*dx + (py-y1)*dy)/length2)) if length2 else 0.0
            distance = (px-x1-t*dx)**2 + (py-y1-t*dy)**2
            if distance < best_distance:
                best_distance, best = distance, i
        if best > start and best_distance <= 1.0:
            self.processed_index = best
            self.paint_processed(start, best)

    def complete_active_file(self):
        index = self.active_file
        if index is None:
            return
        end = sum(len(item['segments']) for item in self.files[:index+1])
        self.paint_processed(self.processed_index, end)
        self.processed_index = end
        self.files[index]['completed'] = True
        self.events.put(('log', f'=== CONCLUÍDO {index+1}/{len(self.files)}: '
                                 f'{Path(self.files[index]["path"]).name}; próximo aguarda Iniciar ==='))
        self.finish_timer()
        self.active_file = None
        self.awaiting_idle = False
        self.tracking_started = False
        self.progress['value'] = 100
        self.refresh_file_list()
        self.update_macro_availability()
        next_index = next((i for i, item in enumerate(self.files) if not item.get('completed')), None)
        if next_index is None:
            self.status.set('Todos os arquivos concluídos')
        else:
            name = Path(self.files[next_index]['path']).name
            self.status.set(f'Concluído. Próximo: {name} — clique Iniciar')

    def connect(self):
        try:
            self.stream.disconnect()
            self.reset_execution_view()
            self.clear_heightmap()
            self.write_diagnostic('CONECTAR: início da tentativa')
            if not self.port.get().strip():
                self.stream.disconnect()
                self.stream.simulation = True
                self.status.set('Modo simulação — sem porta serial')
                self.connection_label.set('SIMULAÇÃO: selecione a porta COM para conectar à placa')
                messagebox.showinfo('Conexão', 'Nenhuma porta selecionada. O programa está em simulação.\n'
                                    'Para conectar à placa, clique Atualizar e escolha a porta COM.',
                                    parent=self.root.winfo_toplevel())
                for button in getattr(self, 'macro_buttons', []):
                    button.configure(state='normal')
                return
            if serial is None:
                raise RuntimeError('Instale pyserial: pip install pyserial pillow')
            self.status.set('Abrindo porta e autenticando...')
            self.connection_label.set(f'Conectando: {self.port.get()} — aguarde a autenticação')
            self.root.update_idletasks()
            self.stream.connect(self.port.get(), int(self.baud.get()))
            self.write_diagnostic('CONECTAR: conexão autenticada')
            self.status.set('Conectado / autenticado')
            for button in getattr(self, 'macro_buttons', []):
                button.configure(state='normal')
        except Exception as exc:
            self.status.set('Falha na conexão')
            self.connection_label.set('Falha: ' + str(exc))
            self.write_diagnostic('CONECTAR: ' + type(exc).__name__ + ': ' + str(exc))
            messagebox.showerror('Conexão', str(exc), parent=self.root.winfo_toplevel())

    def reset_execution_view(self):
        self.close_m0_notice()
        self.active_file = None
        self.awaiting_idle = False
        self.tracking_started = False
        self.processed_index = 0
        self.job_started = None
        self.job_elapsed = 0.0
        self.job_estimate = None
        self.position = None
        self.controller_state = ''
        self.progress['value'] = 0
        self.last_command.set('Comando: —')
        self.last_response.set('Resposta: —')
        self.coordinates.set('Posição: aguardando controladora ou simulação')
        for item in self.files:
            item['completed'] = False
        # Drop old execution events after workers have stopped; retain the visible log.
        try:
            while True: self.events.get_nowait()
        except queue.Empty:
            pass
        self.refresh_file_list()
        self.draw()
        self.update_macro_availability()

    def disconnect(self):
        self.stream.disconnect()
        self.reset_execution_view()
        self.clear_heightmap()
        self.status.set('Desconectado')

    def laser_countdown(self):
        """Keep Tk responsive while delaying all streaming for five seconds."""
        window = tk.Toplevel(self.root)
        self.laser_warning = window
        window.title('Atenção — início do laser')
        window.configure(bg='#c00000')
        window.resizable(False, False)
        window.transient(self.root)
        window.grab_set()
        result = {'ready': False}
        deadline = time.monotonic() + 5.0
        tk.Label(window, text='ATENÇÃO: LASER', bg='#c00000', fg='white',
                 font=('Segoe UI', 22, 'bold')).pack(padx=40, pady=(24, 10))
        label = tk.Label(window, bg='#c00000', fg='white', font=('Segoe UI', 36, 'bold'))
        label.pack(padx=40, pady=8)
        tk.Label(window, text='O trabalho começará ao terminar a contagem.',
                 bg='#c00000', fg='white', font=('Segoe UI', 11)).pack(padx=24, pady=8)
        def cancel(_event=None):
            result['ready'] = False
            window.destroy()
            return 'break'
        tk.Button(window, text='Cancelar (C / Esc)', command=cancel,
                  font=('Segoe UI', 12, 'bold')).pack(pady=(10, 24))
        window.protocol('WM_DELETE_WINDOW', cancel)
        window.bind('<Escape>', cancel)
        window.bind('<KeyPress-c>', cancel)
        window.bind('<KeyPress-C>', cancel)
        window.update_idletasks()
        x = self.root.winfo_rootx() + (self.root.winfo_width()-window.winfo_width())//2
        y = self.root.winfo_rooty() + (self.root.winfo_height()-window.winfo_height())//2
        window.geometry(f'+{max(0,x)}+{max(0,y)}')
        last = [None]
        def tick():
            if not window.winfo_exists(): return
            remaining = max(0, math.ceil(deadline-time.monotonic()))
            if remaining == 0:
                result['ready'] = True
                window.destroy()
                return
            if last[0] != remaining:
                last[0] = remaining
                label.configure(text=str(remaining))
                self.status.set(f'Laser: início em {remaining} s')
                try:
                    import winsound
                    winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS | winsound.SND_ASYNC)
                except (ImportError, RuntimeError):
                    self.root.bell()
            window.after(50, tick)
        window.focus_set()
        tick()
        try:
            self.root.wait_window(window)
        finally:
            self.laser_warning = None
        if not result['ready']: self.status.set('Início do laser cancelado')
        return result['ready']

    def start(self):
        try:
            if getattr(self, 'laser_warning', None) is not None: return
            if self.stream.running or self.awaiting_idle:
                raise RuntimeError('Aguarde o arquivo atual terminar.')
            index = next((i for i, item in enumerate(self.files) if not item.get('completed')), None)
            if index is None:
                raise RuntimeError('Não há arquivos pendentes. Adicione arquivos à fila.')
            item = self.files[index]
            if not item['lines']:
                raise RuntimeError(f'O arquivo {Path(item["path"]).name} não possui comandos.')
            limit = int(self.buffer.get())
            if not 16 <= limit <= 4096:
                raise RuntimeError('Informe um buffer entre 16 e 4096 bytes. Cada comando pode ter até 200 caracteres.')
            simulated = not self.port.get().strip() or self.stream.simulation
            if simulated:
                if self.stream.port:
                    self.stream.disconnect()
                    self.clear_heightmap()
                self.stream.simulation = True
                self.stream.sim_speed = self.simulation_factor()
            elif not messagebox.askokcancel('Iniciar usinagem', f'Modo detectado: {"LASER ($32=1)" if grbl_mode_from_z(item["lines"]) == 1 else "FRESA / SPINDLE ($32=0)"}\n\nConfirme o zero, a fixação e o laser/spindle.\n\nIniciar {Path(item["path"]).name} ({index+1}/{len(self.files)}) em {self.port.get()}?'):
                return
            if grbl_mode_from_z(item['lines']) == 1 and not self.laser_countdown():
                return
            send_lines=item['lines']
            if self.height_enabled.get() and item.get('mode',_preview_mode(item['lines']))=='milling':
                m=self.height_map
                if m is None: raise RuntimeError('Meça o mapa antes de ativar a compensação.')
                if simulated: raise RuntimeError('Compensação requer posição real da máquina; desligue-a para simular.')
                with self.stream.lock:
                    if self.stream.inflight: raise RuntimeError('Aguarde os comandos manuais antes de fresar.')
                self.stream.cancel=False
                self.stream.wait_idle()
                self.stream.modal=None; self.stream.sync_command('$G')
                if not self.stream.work_position: raise RuntimeError('Posição XYZ não disponível.')
                send_lines=m.compensate(item['lines'],self.stream.work_position)
                self.events.put(('log',f'Mapa aplicado: {len(send_lines)} linhas compensadas.'))
            if not simulated:
                self.stream.cancel=False
                self.stream.wait_idle()
            self.job_estimate=estimated_seconds(send_lines,self.stream.work_position or (0,0,0),self.stream.settings)
            self.stream.start(send_lines, limit, item['segments'])
            self.job_elapsed=0.0; self.job_started=time.monotonic()
            self.events.put(('log', f'=== INÍCIO MANUAL {index+1}/{len(self.files)}: '
                                     f'{Path(item["path"]).name} ({len(item["lines"])} linhas) ==='))
            self.active_file = index
            self.update_macro_availability()
            self.processed_index = sum(len(f['segments']) for f in self.files[:index])
            self.tracking_started = True
            self.refresh_file_list()
            self.draw()
            self.status.set('Simulando' if simulated else 'Enviando')
        except Exception as exc:
            messagebox.showerror('Envio', str(exc))

    def pause(self):
        if self.stream.running:
            try:
                self.stream.paused = True
                self.stream.realtime(b'!')
                self.status.set('Pausado (feed hold)')
            except Exception as exc:
                messagebox.showerror('Pausa', str(exc))

    def close_m0_notice(self):
        window = getattr(self, '_m0_notice', None)
        if window is not None:
            try: window.destroy()
            except tk.TclError: pass
        self._m0_notice = None

    def show_m0_notice(self):
        self.close_m0_notice()
        window = tk.Toplevel(self.root)
        self._m0_notice = window
        window.title('Pausa para Conferência de Posicionamento e Ajuste Fino')
        window.transient(self.root.winfo_toplevel())
        window.resizable(False, False)
        ttk.Label(window, text='Pausa para Conferência de Posicionamento e Ajuste Fino', font=('Segoe UI', 12, 'bold'), wraplength=510).pack(padx=20, pady=(18, 10))
        text = ('A máquina está parada.\n'
                'Comandos de posição e macros estão ativos para ajuste fino de X, Y e Z.\n'
                'Os ajustes preservam as coordenadas de trabalho.\n'
                'Laser/spindle permanecem desligados durante o ajuste.\n\n'
                if self.stream._m0_managed else 'A execução está pausada.\n\n')
        text += 'Pressione Retornar na janela principal para continuar o trabalho.'
        ttk.Label(window, text=text, justify='left', wraplength=510).pack(padx=20, pady=(0, 14))
        ttk.Button(window, text='Fechar aviso (manter pausa)', command=self.close_m0_notice).pack(pady=(0, 18))
        # Modeless: no grab/wait_window; movement and macro buttons remain accessible.
        window.protocol('WM_DELETE_WINDOW', self.close_m0_notice)

    def resume(self):
        if self.stream._m0_managed and not self.stream.simulation:
            try:
                self.stream.resume_m0_alignment()
                self.close_m0_notice()
                self.update_macro_availability()
                self.status.set('Retomando após ajuste M0...')
            except Exception as exc:
                messagebox.showerror('Retomar', str(exc))
            return
        if self.stream.running:
            try:
                self.stream.realtime(b'~')
                self.stream.paused = False
                self.stream.m0_waiting = False
                self.close_m0_notice()
                self.status.set('Enviando')
            except Exception as exc:
                messagebox.showerror('Retomar', str(exc))

    def stop(self):
        if getattr(self, 'laser_warning', None) is not None:
            self.laser_warning.destroy()
            return
        self.awaiting_idle = False
        if self.stream.simulation:
            self.stream.cancel = True
            self.stream.paused = False
            self.finish_timer()
            self.status.set('Simulação cancelada')
            return
        if self.stream.port and messagebox.askyesno('Cancelar', 'Enviar feed hold e reset GRBL? Isso cancela o trabalho e pode desligar saídas.'):
            self.finish_timer()
            self.stream.cancel = True
            self.stream.paused = False
            self.close_m0_notice()
            try:
                self.stream.realtime(b'!\x18')
                # O reset descarta a fila GRBL; respostas tardias não pertencem ao próximo arquivo.
                with self.stream.lock:
                    self.stream.inflight.clear()
                self.clear_heightmap()
                self.status.set('Cancelado; confira posição e estado da controladora')
            except Exception as exc:
                messagebox.showerror('Parada', str(exc))

    def jog_step_value(self, axis):
        """Retorna o passo de jog em mm, validando o campo informado."""
        raw = (self.jog_step_z if axis == 'Z' else self.jog_step).get().strip().replace(',', '.')
        try:
            value = float(raw)
        except ValueError as exc:
            raise ValueError('Informe um passo válido em mm.') from exc
        if not 0.001 <= value <= 1000.0:
            raise ValueError('O passo deve ficar entre 0,001 mm e 1000 mm.')
        return value

    def jog_feed_value(self, axis):
        raw = (self.jog_feed_z if axis == 'Z' else self.jog_feed_xy).get().strip().replace(',', '.')
        try:
            value = float(raw)
        except ValueError as exc:
            raise ValueError('Informe uma velocidade F válida em mm/min.') from exc
        if not math.isfinite(value) or value <= 0:
            raise ValueError('A velocidade F deve ser maior que zero.')
        return value

    def jog(self, axis, direction):
        """Move X/Y/Z pelo passo escolhido usando JOG do GRBL."""
        try:
            axis = axis.upper()
            if axis not in ('X', 'Y', 'Z') or direction not in (-1, 1):
                raise ValueError('Comando de movimento inválido.')
            if self.stream.running and not self.stream.m0_alignment_ready:
                raise RuntimeError('Movimento manual permitido apenas em M0 pronto para ajuste.')

            step = self.jog_step_value(axis) * direction
            feed = self.jog_feed_value(axis)
            self.prepare_manual_simulation()

            if self.stream.simulation:
                # Na simulação usamos G91/G90 para o visualizador acompanhar X/Y.
                command = f'G91\nG1 {axis}{step:.4f} F{feed:g}\nG90'
            else:
                # $J não altera permanentemente o estado modal G90/G91 do programa.
                command = f'$J=G21 G91 {axis}{step:.4f} F{feed:g}'

            self.stream.send_manual(command)
            self.status.set(f'Jog {axis}: {step:+.4f} mm')
        except Exception as exc:
            messagebox.showerror('Movimento manual', str(exc))

    def manual(self):
        try:
            self.prepare_manual_simulation()
            self.stream.send_manual(self.resolve_command(self.command.get()))
            self.command.delete(0, 'end')
        except Exception as exc:
            messagebox.showerror('Comando', str(exc))

    def simulation_factor(self):
        value = float(self.sim_speed.get().replace(',', '.'))
        if not .1 <= value <= 10:
            raise ValueError('Velocidade de simulação: use de 0,1× a 10×.')
        return value

    def prepare_manual_simulation(self):
        if not self.port.get().strip() and not self.stream.port:
            self.stream.simulation = True
        if self.stream.simulation:
            self.stream.sim_speed = self.simulation_factor()

    def resolve_command(self, command):
        if '[' not in command:
            return command
        if re.search(r'\[(?:\s*(?:left|right|top|bottom)\b)', command, re.I) and not self.segments:
            raise ValueError('Abra um arquivo .nc antes de usar [left], [right], [top] ou [bottom].')
        xs = [v for x1, _, x2, _, _ in self.segments for v in (x1, x2)] + [hx for hx, _, _ in self.holes]
        ys = [v for _, y1, _, y2, _ in self.segments for v in (y1, y2)] + [hy for _, hy, _ in self.holes]
        bounds = {'left': min(xs), 'right': max(xs), 'bottom': min(ys), 'top': max(ys)} if xs else {}
        settings = dict(self.stream.settings)
        if self.stream.simulation:
            settings = {'30': 1000.0, **settings}
        return expand_macro(command, bounds, settings)

    def make_macros(self):
        for child in self.macros.winfo_children():
            child.destroy()

        # Remove pesos antigos para a grade se reajustar após adicionar/remover macros.
        for col in range(10):
            self.macros.columnconfigure(col, weight=0)
        for row in range(100):
            self.macros.rowconfigure(row, weight=0)

        macros = self.config['macros']
        self.macro_images = []
        self.macro_buttons = []
        if not macros:
            self.macros.columnconfigure(0, weight=1)
            self.macros.rowconfigure(0, weight=1)
            ttk.Label(self.macros, text='Nenhuma macro cadastrada', anchor='center').grid(
                row=0, column=0, sticky='nsew', padx=4, pady=4)
            return

        count = len(macros)
        # Distribui na ordem de leitura, com botões largos o suficiente para o texto.
        if count <= 5:
            columns = 1
        elif count <= 18:
            columns = 2
        elif count <= 36:
            columns = 3
        else:
            columns = 4

        rows = math.ceil(count / columns)
        for col in range(columns):
            self.macros.columnconfigure(col, weight=1, uniform='macro_col')
        for row in range(rows):
            self.macros.rowconfigure(row, weight=1, uniform='macro_row')

        for index, macro in enumerate(macros):
            icon = None
            if macro.get('icon'):
                try:
                    with Image.open(icon_path(macro['icon'])) as source:
                        picture = source.convert('RGBA')
                        picture.thumbnail((48, 48), Image.Resampling.LANCZOS)
                    icon = ImageTk.PhotoImage(picture)
                    self.macro_images.append(icon)
                except (OSError, ValueError):
                    pass

            row, col = divmod(index, columns)
            button = ttk.Button(
                self.macros, text=macro['name'], image=icon, compound='left',
                padding=(5, 5), command=lambda m=macro: self.run_macro(m)
            )
            button.grid(row=row, column=col, sticky='nsew', padx=4, pady=4)
            self.macro_buttons.append(button)
        self.update_macro_availability()

    def update_macro_availability(self):
        # active_file is selection/progress metadata and can outlive a cancelled job.
        available = (not self.awaiting_idle and not self.stream.running and not self.stream._m0_editing) or (self.stream.m0_alignment_ready and not self.stream._m0_editing and not self.stream.cancel)
        for button in getattr(self, 'macro_buttons', []):
            button.configure(state='normal' if available else 'disabled')

    def choose_macro_icon(self, parent):
        return filedialog.askopenfilename(parent=parent, title='Escolher ícone da macro',
            filetypes=[('Imagens', '*.png *.jpg *.jpeg *.gif *.bmp *.webp'), ('Todos', '*.*')])

    def run_macro(self, macro):
        try:
            self.prepare_manual_simulation()
            command = self.resolve_command(macro['command'])
            self.stream.send_manual(command)
            self.update_macro_availability()
        except Exception as exc:
            messagebox.showerror('Macro', str(exc))

    def add_macro(self):
        name = simpledialog.askstring('Nova macro', 'Nome do botão:', parent=self.root)
        if not name:
            return
        command = simpledialog.askstring('Nova macro', 'Comandos GRBL (múltiplas linhas permitidas):', parent=self.root)
        if not command:
            return
        icon = self.choose_macro_icon(self.root)
        macro = {'name': name, 'command': command}
        if icon:
            macro['icon'] = icon
        self.config['macros'].append(macro)
        self.save()
        self.make_macros()

    def edit_macro(self):
        window = tk.Toplevel(self.root)
        window.title('Gerenciar botões de macro')
        window.geometry('410x350')
        window.transient(self.root)
        window.grab_set()
        ttk.Label(window, text='Selecione o botão que deseja editar ou remover:', padding=10).pack(anchor='w')
        choices_frame = ttk.Frame(window)
        choices_frame.pack(fill='both', expand=True, padx=10)
        choices = tk.Listbox(choices_frame, exportselection=False)
        choices_scroll = ttk.Scrollbar(choices_frame, orient='vertical', command=choices.yview)
        choices.configure(yscrollcommand=choices_scroll.set)
        choices.pack(side='left', fill='both', expand=True)
        choices_scroll.pack(side='right', fill='y')

        def refresh(selected=0):
            choices.delete(0, 'end')
            for macro in self.config['macros']:
                choices.insert('end', macro['name'])
            if self.config['macros']:
                choices.selection_set(min(selected, len(self.config['macros'])-1))

        def selected_index():
            selection = choices.curselection()
            if not selection:
                messagebox.showinfo('Macros', 'Selecione um botão na lista.', parent=window)
                return None
            return selection[0]

        def update_selected():
            index = selected_index()
            if index is None:
                return
            macro = self.config['macros'][index]
            name = simpledialog.askstring('Editar botão', 'Nome do botão:', initialvalue=macro['name'], parent=window)
            if name is None:
                return
            command = simpledialog.askstring('Editar botão', 'Comando GRBL:', initialvalue=macro['command'], parent=window)
            if command is None:
                return
            if not name.strip() or not command.strip():
                messagebox.showerror('Macro', 'Informe nome e comando. Use Remover para excluir.', parent=window)
                return
            macro.update(name=name.strip(), command=command.strip())
            self.save()
            self.make_macros()
            refresh(index)

        def remove_selected():
            index = selected_index()
            if index is None:
                return
            name = self.config['macros'][index]['name']
            if not messagebox.askyesno('Remover macro', f'Remover o botão "{name}"?', parent=window):
                return
            del self.config['macros'][index]
            self.save()
            self.make_macros()
            refresh(index)

        def change_icon():
            index = selected_index()
            if index is None:
                return
            icon = self.choose_macro_icon(window)
            if icon:
                self.config['macros'][index]['icon'] = icon
                self.save()
                self.make_macros()

        def remove_icon():
            index = selected_index()
            if index is None:
                return
            self.config['macros'][index].pop('icon', None)
            self.save()
            self.make_macros()

        def move_selected(direction):
            index = selected_index()
            if index is None:
                return
            target = index + direction
            macros = self.config['macros']
            if not 0 <= target < len(macros):
                return
            macros[index], macros[target] = macros[target], macros[index]
            self.save()
            self.make_macros()
            refresh(target)
            choices.activate(target)
            choices.see(target)

        refresh()
        buttons = ttk.Frame(window, padding=10)
        buttons.pack(fill='x')
        ttk.Button(buttons, text='Editar selecionado', command=update_selected).pack(side='left')
        ttk.Button(buttons, text='Remover selecionado', command=remove_selected).pack(side='left', padx=5)
        ttk.Button(buttons, text='Fechar', command=window.destroy).pack(side='right')
        icons = ttk.Frame(window, padding=(10, 0, 10, 10))
        icons.pack(fill='x')
        ttk.Button(icons, text='Escolher ícone', command=change_icon).pack(side='left')
        ttk.Button(icons, text='Retirar ícone', command=remove_icon).pack(side='left', padx=5)
        order = ttk.Frame(window, padding=(10, 0, 10, 10))
        order.pack(fill='x')
        ttk.Button(order, text='↑ Subir', command=lambda: move_selected(-1)).pack(side='left')
        ttk.Button(order, text='↓ Descer', command=lambda: move_selected(1)).pack(side='left', padx=5)

    def save_macro_file(self):
        path = filedialog.asksaveasfilename(title='Salvar botões de macro',
            defaultextension='.json', initialfile='macros_controladora.json',
            filetypes=[('Configuração de macros', '*.json')])
        if not path:
            return
        try:
            content = export_macros(self.config['macros'])
            Path(path).write_text(json.dumps(content, ensure_ascii=False, indent=2), encoding='utf-8')
            self.status.set(f'Macros salvas: {Path(path).name}')
        except (OSError, ValueError) as exc:
            messagebox.showerror('Salvar macros', str(exc))

    def load_macro_file(self):
        path = filedialog.askopenfilename(title='Carregar botões de macro',
            filetypes=[('Configuração de macros', '*.json'), ('Todos', '*.*')])
        if not path:
            return
        try:
            content = json.loads(Path(path).read_text(encoding='utf-8'))
            macros = import_macros(content)
            self.config['macros'] = macros
            self.save()
            self.make_macros()
            self.status.set(f'{len(macros)} macros carregadas: {Path(path).name}')
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            messagebox.showerror('Carregar macros', str(exc))

    def save(self):
        self.config['port'] = self.port.get().strip()
        self.config['baud'] = self.baud.get()
        self.config['buffer'] = self.buffer.get()
        self.config['sim_speed'] = self.sim_speed.get()
        self.config['jog_step'] = self.jog_step.get()
        self.config['jog_step_z'] = self.jog_step_z.get()
        self.config['jog_feed_xy'] = self.jog_feed_xy.get()
        self.config['jog_feed_z'] = self.jog_feed_z.get()
        self.config['camera_flip_x'] = self.camera_flip_x.get()
        try:
            CONFIG.write_text(json.dumps(self.config, ensure_ascii=False, indent=2), encoding='utf-8')
        except OSError as exc:
            messagebox.showerror('Configuração', str(exc))

    def write_diagnostic(self, record):
        if not ATIVAR_LOG:
            return
        try:
            if DIAGNOSTIC_LOG.exists() and DIAGNOSTIC_LOG.stat().st_size > 10 * 1024 * 1024:
                DIAGNOSTIC_LOG.replace(DIAGNOSTIC_LOG.with_suffix('.log.1'))
            with DIAGNOSTIC_LOG.open('a', encoding='utf-8') as diagnostic:
                diagnostic.write(time.strftime('%Y-%m-%d %H:%M:%S') + ' ' + record + '\n')
        except OSError as exc:
            if not self.diagnostic_error_shown:
                self.diagnostic_error_shown = True
                messagebox.showwarning('Diagnóstico GRBL',
                                       f'Falha ao gravar log em:\n{DIAGNOSTIC_LOG}\n\n{exc}',
                                       parent=self.root)

    def poll(self):
        # Yield to Tk regularly, even when a fast sender keeps producing log events.
        deadline = time.monotonic() + .012
        try:
            for _ in range(100):
                if time.monotonic() >= deadline:
                    break
                event = self.events.get_nowait()
                kind = event[0]
                if kind == 'heightmap':
                    self.height_map=event[1]; self.height_enabled.set(True)
                    m=self.height_map; values=[v for row in m.zs for v in row]
                    self.height_status.set(f'Mapa pronto: {len(m.xs)} × {len(m.ys)} pontos; variação {max(values)-min(values):.4f} mm')
                    self.draw_heightmap()
                elif kind == 'probe_state':
                    self.probe_label.set('PROBE: ACIONADO' if event[1] else 'PROBE: ABERTO')
                elif kind == 'map_invalid':
                    if self._mark_zero_in_progress and self.height_map is not None:
                        # Reset no meio da troca de fresa: não apagar as amostras.
                        # O mapa fica DESATIVADO até uma nova marcação bem-sucedida.
                        self.height_enabled.set(False)
                        self.height_status.set(event[1] + '; mapa guardado, compensação suspensa. Refaça Marcar Zero.')
                    else:
                        self.clear_heightmap(); self.height_status.set(event[1]+'; meça novamente')
                elif kind == 'probe_progress':
                    self.height_status.set(f'Medindo {event[1]}/{event[2]}: X{event[3]:.3f} Y{event[4]:.3f} Z{event[5]:.4f}')
                elif kind == 'z_zero_done':
                    self.status.set(event[1])
                elif kind == 'mark_zero_done':
                    self._mark_zero_succeeded = True
                    preserved = self.height_map is not None
                    if preserved:
                        # Preservar amostras e WCO originais do mapa. A compensacao
                        # usa H(X,Y)-H(0,0) no Z0 fisico da fresa atual.
                        self.height_enabled.set(self._map_enabled_before_zero)
                        self.draw_heightmap()
                        self.events.put(('log', 'Marcar Zero concluido: mapa original preservado; compensacao relativa ao novo Z0.'))
                    self.height_status.set(f'Z0 no centro: {event[1]:.4f} mm; '
                                           + ('mapa preservado; compensacao relativa ao novo Z0.' if preserved else '3 contatos concluidos.'))
                    messagebox.showinfo('Marcar Zero',
                                        'Z0 definido a partir de tres pontos.\n'
                                        + ('Mapa anterior preservado, sem alterar as leituras.\n' if preserved else '')
                                        + 'Remova o sensor do probe antes de fresar.')
                elif kind == 'probe_test':
                    self.height_status.set('Teste concluído: novo Z0 definido no contato; retração confirmada')
                elif kind == 'probe_finished':
                    if self._mark_zero_in_progress:
                        if not self._mark_zero_succeeded and self.height_map is not None:
                            self.height_enabled.set(False)
                            self.height_status.set('Marcar Zero interrompido; mapa guardado, compensação desativada até redefinir Z0.')
                        self._mark_zero_in_progress = False
                    self.update_macro_availability()
                elif kind in ('m0_alignment', 'm0_busy', 'm0_adjusted'):
                    if kind == 'm0_alignment':
                        self.show_m0_notice()
                    if self.stream.cancel:
                        self.close_m0_notice()
                    self.update_macro_availability()
                    self.status.set('Conferência de posicionamento: ajustando XYZ...' if self.stream._m0_editing else
                                    ('Conferência de posicionamento: movimentos/macros ativos; pressione Retornar para continuar' if self.stream.m0_alignment_ready else 'Conferência de posicionamento encerrada'))
                elif kind == 'command':
                    self.write_diagnostic('TX ' + event[1])
                elif kind == 'log':
                    # Registro persistente para identificar ALARM:3, PRB e resets
                    # após a falha, sem modificar a sequência de movimento.
                    self.write_diagnostic(event[1])
                    self.log.configure(state='normal')
                    self.log.insert('end', event[1] + '\n')
                    if int(self.log.index('end-1c').split('.')[0]) > 1000:
                        self.log.delete('1.0', '200.0')
                    self.log.see('end')
                    self.log.configure(state='disabled')
                elif kind == 'progress':
                    self.progress['value'] = 100 * event[1] / event[2]
                    if self.stream.simulation:
                        self.status.set(f'Simulação: linha {event[1]}/{event[2]}  ({self.sim_speed.get()}×)')
                    else:
                        self.status.set(f'Enviadas {event[1]}/{event[2]} linhas; aguardando confirmações')
                elif kind == 'm0':
                    self.status.set('Pausa para Conferência de Posicionamento e Ajuste Fino')
                    self.show_m0_notice()
                elif kind == 'error':
                    self.write_diagnostic('ERRO ' + repr(event))
                    self.status.set(f'Erro GRBL na linha {event[1]}: {event[2]}')
                elif kind == 'position':
                    self.position = (event[1], event[2])
                    self.controller_state = event[3]
                    self.coordinates.set(f'X {event[1]:.3f}   Y {event[2]:.3f}   Z {(self.stream.work_position or (0,0,0))[2]:.3f} mm   {event[3]}')
                    if self.preview_transform is None:
                        self.draw()
                    self.track_position()
                    if event[3].lower() == 'idle' and self.awaiting_idle and not self.stream.cancel:
                        self.complete_active_file()
                    self.draw_position()
                elif kind == 'macro_segment':
                    segment = event[1:]
                    self.macro_segments.append(segment)
                    if len(self.macro_segments) > 2000:
                        self.macro_segments.pop(0)
                    if self.segments:
                        self.draw_macro_segment(segment)
                    else:
                        self.draw()
                elif kind == 'loaded':
                    if event[1] == self.path:
                        self.lines, self.segments = event[2], event[3]
                        self.files = [{'path': event[1], 'lines': event[2], 'segments': event[3], 'warnings': event[4]}]
                        self.refresh_file_list()
                        self.status.set(f'{Path(self.path).name}: {len(self.lines)} linhas')
                        self.draw()
                        if event[4]:
                            messagebox.showwarning('Avisos do preview', '\n'.join(event[4]))
                elif kind == 'fault':
                    self.close_m0_notice()
                    diagnostics = getattr(self.stream.port, 'communication_diagnostics', None)
                    if diagnostics:
                        self.write_diagnostic(diagnostics())
                    self.write_diagnostic('FALHA ' + repr(event))
                    self.finish_timer()
                    self.status.set(event[1])
                    self.update_macro_availability()
                    messagebox.showerror('Controladora', event[1])
                elif kind == 'done':
                    self.finish_timer()
                    self.status.set(event[1])
                    if self.active_file is not None and not self.stream.cancel:
                        self.complete_active_file()
                elif kind == 'camera_info':
                    self.camera_status.set(event[1])
                elif kind == 'macro_done':
                    self.status.set(event[1])
                    self.update_macro_availability()
        except queue.Empty:
            pass
        if self.stream.port and self.stream.port.is_open and time.monotonic() - self.stream.last_status > .25:
            self.stream.last_status = time.monotonic()
            try:
                self.stream.realtime(b'?')
            except Exception:
                pass
        self.update_indicators()
        self.update_macro_availability()
        self.root.after(50, self.poll)

    def build_camera_tab(self, parent):
        """Visualização USB local; não altera os controles da CNC."""
        bar = ttk.Frame(parent)
        bar.pack(fill='x', pady=(0, 8))
        ttk.Label(bar, text='Câmera nº:').pack(side='left')
        camera_select = ttk.Combobox(bar, width=5, textvariable=self.camera_index,
                                     values=[str(i) for i in range(8)])
        camera_select.pack(side='left', padx=5)
        ttk.Button(bar, text='Iniciar', command=self.start_camera).pack(side='left', padx=3)
        ttk.Button(bar, text='Parar', command=self.stop_camera).pack(side='left', padx=3)
        ttk.Button(bar, text='Foto', command=self.camera_snapshot).pack(side='left', padx=3)
        zoom_bar = ttk.Frame(parent)
        zoom_bar.pack(fill='x', pady=(0, 5))
        ttk.Label(zoom_bar, text='Zoom:').pack(side='left')
        ttk.Button(zoom_bar, text='−', width=3, command=lambda: self.change_camera_zoom(-1)).pack(side='left', padx=3)
        self.camera_zoom_label = ttk.Label(zoom_bar, text='1.00×', width=7, anchor='center')
        self.camera_zoom_label.pack(side='left')
        ttk.Button(zoom_bar, text='+', width=3, command=lambda: self.change_camera_zoom(1)).pack(side='left', padx=3)
        ttk.Button(zoom_bar, text='Ajustar', command=self.reset_camera_zoom).pack(side='left', padx=5)
        ttk.Label(zoom_bar, text='Roda = zoom  |  Direito + arrastar = mover').pack(side='right')
        ttk.Checkbutton(parent, text='Inverter X (espelhar horizontalmente)',
                        variable=self.camera_flip_x, command=self.save).pack(anchor='w', pady=(0, 6))
        self.camera_view = tk.Label(parent, text='Câmera desligada', bg='#151922',
                                    fg='#dce6f2', font=('Segoe UI', 12), anchor='center')
        self.camera_view.pack(fill='both', expand=True)
        self.camera_view.bind('<MouseWheel>', self.zoom_camera_wheel)
        self.camera_view.bind('<Button-4>', self.zoom_camera_wheel)
        self.camera_view.bind('<Button-5>', self.zoom_camera_wheel)
        self.camera_view.bind('<Double-Button-1>', self.reset_camera_zoom)
        self.camera_view.bind('<ButtonPress-3>', self.begin_camera_pan)
        self.camera_view.bind('<B3-Motion>', self.pan_camera)
        self.camera_view.bind('<ButtonRelease-3>', self.end_camera_pan)
        ttk.Label(parent, textvariable=self.camera_status, style='Muted.TLabel').pack(
            fill='x', pady=(8, 0))
        self.root.after(100, self.update_camera_view)

    def change_camera_zoom(self, direction, event=None):
        old = self.camera_zoom
        new = max(1.0, min(20.0, old * (1.2 if direction > 0 else 1 / 1.2)))
        if abs(new - 1.0) < 0.02:
            new = 1.0
        if event is not None and new != old:
            vw, vh = max(1, self.camera_view.winfo_width()), max(1, self.camera_view.winfo_height())
            # Coordenadas relativas ao retângulo exibido, com limites seguros.
            ax = max(0.0, min(1.0, event.x / vw))
            ay = max(0.0, min(1.0, event.y / vh))
            cx, cy = self.camera_center
            self.camera_center = (max(0.0, min(1.0, cx + (ax - 0.5) * (1 / old - 1 / new))),
                                  max(0.0, min(1.0, cy + (ay - 0.5) * (1 / old - 1 / new))))
        self.camera_zoom = new
        self.camera_zoom_label.configure(text=f'{new:.2f}×')

    def zoom_camera_wheel(self, event):
        direction = (1 if event.num == 4 else -1) if getattr(event, 'num', None) in (4, 5) else (1 if event.delta > 0 else -1)
        self.change_camera_zoom(direction, event)
        return 'break'

    def reset_camera_zoom(self, event=None):
        self.camera_zoom = 1.0
        self.camera_center = (0.5, 0.5)
        self.camera_drag_last = None
        self.camera_zoom_label.configure(text='1.00×')
        return 'break'

    def begin_camera_pan(self, event):
        if self.camera_zoom > 1.0 and self.camera_frame is not None:
            self.camera_drag_last = (event.x, event.y)
            self.camera_view.configure(cursor='fleur')
        return 'break'

    def pan_camera(self, event):
        if self.camera_drag_last is None:
            return 'break'
        dx = event.x - self.camera_drag_last[0]
        dy = event.y - self.camera_drag_last[1]
        self.camera_drag_last = (event.x, event.y)
        if self.camera_zoom > 1.0 and (dx or dy):
            vw = max(1, self.camera_view.winfo_width())
            vh = max(1, self.camera_view.winfo_height())
            with self.camera_lock:
                frame = self.camera_frame
                size = frame.size if frame is not None else None
            if size:
                fw, fh = size
                cw = max(1, round(fw / self.camera_zoom))
                ch = max(1, round(fh / self.camera_zoom))
                # thumbnail centralizado: a distância arrastada corresponde ao tamanho renderizado.
                factor = min(vw / cw, vh / ch)
                rendered_w, rendered_h = max(1, cw * factor), max(1, ch * factor)
                cx, cy = self.camera_center
                # Sentido natural: arrastar a imagem para a direita mostra a área à esquerda.
                cx -= dx / rendered_w * cw / fw
                cy -= dy / rendered_h * ch / fh
                self.camera_center = (
                    max(cw / (2 * fw), min(1 - cw / (2 * fw), cx)),
                    max(ch / (2 * fh), min(1 - ch / (2 * fh), cy))
                )
        return 'break'

    def end_camera_pan(self, event=None):
        self.camera_drag_last = None
        self.camera_view.configure(cursor='')
        return 'break'

    def start_camera(self):
        if self.camera_active:
            return
        try:
            import cv2
        except ImportError:
            messagebox.showerror('Câmera', 'OpenCV não instalado. Execute: pip install opencv-python')
            return
        try:
            index = int(self.camera_index.get())
            if index < 0 or index > 99:
                raise ValueError
        except ValueError:
            messagebox.showerror('Câmera', 'Informe o número da câmera (0, 1, 2...).')
            return
        self.camera_stop.clear()
        self.camera_active = True
        self.camera_status.set(f'Conectando à câmera {index}...')
        self.config['camera_index'] = str(index)
        self.camera_thread = threading.Thread(target=self.camera_worker, args=(cv2, index), daemon=True)
        self.camera_thread.start()

    def camera_worker(self, cv2, index):
        capture = None
        try:
            # DirectShow reduz atrasos em webcams no Windows.
            backend = cv2.CAP_DSHOW if sys.platform == 'win32' else cv2.CAP_ANY
            capture = cv2.VideoCapture(index, backend)
            if not capture.isOpened():
                raise RuntimeError(f'Não foi possível abrir a câmera {index}.')
            capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
            capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            self.events.put(('camera_info', f'Câmera {index} conectada'))
            while not self.camera_stop.is_set():
                ok, frame = capture.read()
                if not ok:
                    raise RuntimeError('A câmera parou de fornecer imagens.')
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                with self.camera_lock:
                    self.camera_frame = Image.fromarray(frame)
        except Exception as exc:
            if not self.camera_stop.is_set():
                self.events.put(('camera_info', f'Erro: {exc}'))
        finally:
            if capture is not None:
                capture.release()
            self.camera_active = False

    def update_camera_view(self):
        if not self.root.winfo_exists():
            return
        with self.camera_lock:
            frame = self.camera_frame
        if frame is not None and self.camera_view.winfo_width() > 1 and self.camera_view.winfo_height() > 1:
            w, h = self.camera_view.winfo_width(), self.camera_view.winfo_height()
            preview = ImageOps.mirror(frame) if self.camera_flip_x.get() else frame.copy()
            if self.camera_zoom > 1.0:
                fw, fh = preview.size
                cw = max(1, round(fw / self.camera_zoom))
                ch = max(1, round(fh / self.camera_zoom))
                cx, cy = self.camera_center
                left = max(0, min(fw - cw, round(cx * fw - cw / 2)))
                top = max(0, min(fh - ch, round(cy * fh - ch / 2)))
                preview = preview.crop((left, top, left + cw, top + ch))
            preview.thumbnail((w, h), Image.Resampling.BILINEAR)
            self.camera_photo = ImageTk.PhotoImage(preview)
            self.camera_view.configure(image=self.camera_photo, text='')
        self.root.after(100, self.update_camera_view)

    def stop_camera(self):
        self.camera_stop.set()
        with self.camera_lock:
            self.camera_frame = None
        self.camera_photo = None
        self.camera_view.configure(image='', text='Câmera desligada')
        self.camera_status.set('Câmera desligada')

    def camera_snapshot(self):
        with self.camera_lock:
            frame = self.camera_frame.copy() if self.camera_frame is not None else None
        if frame is None:
            messagebox.showinfo('Câmera', 'Inicie a câmera antes de capturar uma foto.')
            return
        filename = filedialog.asksaveasfilename(title='Salvar foto da câmera',
                     defaultextension='.png', filetypes=[('Imagem PNG', '*.png'), ('JPEG', '*.jpg')],
                     initialfile='camera_cnc.png')
        if filename:
            try:
                if self.camera_flip_x.get():
                    frame = ImageOps.mirror(frame)
                frame.save(filename)
                self.camera_status.set(f'Foto salva: {Path(filename).name}')
            except OSError as exc:
                messagebox.showerror('Câmera', str(exc))

    def close(self):
        self.camera_stop.set()
        self.save()
        self.stream.disconnect()
        self.root.destroy()


if __name__ == '__main__':
    App(tk.Tk()).root.mainloop()
