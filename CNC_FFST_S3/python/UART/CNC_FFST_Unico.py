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
        b'c-riJd0<r4)%cwyD-TEjBTJN*kc0#$VP-;BgJiM?vW!Uxi};ZtnIxl0CeBP)Y+5tHVnA#O*b097brPi_6$P}4S`^SCTCh;tYF%2i'
        b'rd8{LOC^wy_dDm_`(|UQ{<go~f%nec&Rx$v_ndq0ynL)t=RdVQFaL8wNCZ4YlJKnx&whQuV;b~I(hLZ|Cze0SW-XDLAQ7fKqiR5;'
        b'g(n1_P<X=NX}3FVE8DCcV%~f)-ALw^7nRIyw6}NKJFFcp=iF6xyQ|G^X|g(2I=ebM?GD#mr=!t7xVg>ZY)xw<?KY>~FC*$*wa#T-'
        b'+0oUGVe?2Z(MpHa(zMdq+|+q-ly$AOu?vWyD(#kzCW`GH#M;qhxWVbNI9!JBQdL_=V_R2~)jz7sWot`o#f*$BBO}3>l@K7_AX2BL'
        b'smbwOJHqPhTxn~!v{+X*+a2u|7j#6SrLD26&Em2)iLKBSQoOd)+UWHKRR#K>#b)ntuC%YVI@&Cq1dy$H-AZpotWKxZNlfr|xWs0Q'
        b'tqn4=b%=>h9Xz>-O=5DQGi7`vv8;kBC8vmMEKae}(uT<_F40^l>enXfv)4k3R_Mnzs~9(5tXf=A@jV)tZgi#xM7LU?nN1d#g^qWk'
        b'I8U5EU(}PpB*u))mCd#eTVR`c1QL^^m8+c2m2?o0L6{fD;s2m&JP4|nM9c8co%%6*zw}T)7g^QS+-!Ax-;VJMc0kYC+o4c@Hnz33'
        b'@d!FM*_36N+?SW{fk~X{CSLd`n&fwfko*HZq+yQXnx8%e7=n99*6Ry!jz6FK`hxW9UtgfPp7~?pnF{Wve4*h}Ors|aH1{Yf7RZOv'
        b'>kG`Mg@!tKmcp|Fo(6cD;Aw^DG&~=|^AS9s!gB_mZ{Qh*C!7ck0z75lu7KyMsU-h&49VX<jpUmnN&X@5OHaP6#X3l2R3c_<+drXo'
        b'BT_!py8@mELP`FV26Y3pfVjXv74pN{L831@i5BYm3#e^AN~8v?^c_8tq{Z-wL?R7ZlGjJu59#ibl4<%Uh;+xWG!@)Y5I3(6<D@&X'
        b'G42aV%A;w*AkS7JEf|(aJ_yBd+O?{-o1q}6L-H)>XASG`1gLvaBFWbQ{s#K~PKcKl9D*!WV@0Q-Y)M0;7cWTp1rs6lRKhYlBW1c('
        b'aoePr8shGkPKOg~2#J|PtnX>!eo6!H!N4OPk1%eJ%6&I__Naz_tBHB;!XDMm-)nlGc+fLPyleW2K@ZtU$U!xPzN5)B5phs-_h9nW'
        b'$ZO7kUzoo0Tg{+Hm3UqwOt)Up7;cy1ZkJ5AONT^~qJdYk*1cBhi5JnY71V&@8_CXO66cZ(E@}3Y6HYm$!!Bw6fO)_vSwGXnIVFP='
        b'!pEI*NQXNh{Kn98QsP45-iW2T`+V=XTcz#~A-`;OetHz(95wZH|55f@r<24wGSo_jib!ICCN;7?_v*w_sCoT!F+0l;=f)UrlJ;nJ'
        b')@!V0&CVo^X{lt?V6Drv`g!wWwMm6nKV7TdP)&rQq*;P+=eOx$!j%0UwSLhyx0Tk!EPYua^@X3RkPcT!^CNeKA9_ml!2oeL&@R=u'
        b'SJKYkpb;Y7Ms&`P6sEiN=<0p#oG|6-Y;}Q$^uBaXnD%tGN{Hxw%lOj2d(xw}6p6xAAws`>eSVIp*Sn6tH2B)r-B0E3j`C!$kNG;('
        b'kd7UktuYumHgK%xcrM3j9H(-u<M=v`=Wv|DaWcoVIZk5Olqgk%qf6V9jzgKFHN{K4PrS&3qFB(ik}#RMVkL@)(uwtYa?P0vZF8e~'
        b'!+uGp{TA?E$@tQ_0#DD;$6yv@S_t&bwX~bA3UN=79?8DBe~Q!>v3=T(=>AF4mcA(Z7B{M_PiZ}#DJM6n`X@@eR9kjO_3RcORV6+P'
        b'q1w|B8VR8XqUG?RY~l`+gb1j}j&OH~)P0V+t~mq6og9PWns@*F=(iH^ur-}fUUrX-^^c7q&xTh-Zec7N?j9N2`Y@q^-Ji;Vao>*h'
        b'pT(4YYGEeS4O|=5)Z72nm{5gv{&GwXOpb7WG1e0w<^CMrBD^t+2%4jZ=SNcwd^E=W7`ZDV{s|)PjuMRGZVY@B1Gk3{oF4P+h#DN|'
        b'@$3+3d-~rSqpA13J9g@?V|#Z;?Ry*EUWx<Z18<HUdL9SpSuEy2<jLnT^4UmA)%Jr!yQAc^yTT8j!W@LVc?RJ$aNnzA?@idtl7;U('
        b'Ha2i{%$q?tCl7bOJT~z1m|RL<<h~z_3Eg{H&qNNqIJWOa+Fg-*`=V%&`!{3zpZFWiLe82M_RN^<ANcjyzF&K(_B}NwXU7WIH-@2m'
        b'141JP_KY2z=wTrdEM)f>^Y_}wpvUHZ1czRjDWttO;o!t0o-hm>#IVoQ@2Q1}Lic`;3d0_x=_U%-d<J0$$79fT47%nF@T`f%)r`f*'
        b'lc96!!Bu1n%4rB2STJ^Y!I&`4bNrAy(=YA5g0Vk%R7X5hL6}<SX<%ZjJ;~cdv4O|$yjnAmGq&GDhNf$JJt|);%nd{Ln4rFUAjgmr'
        b'm$*!O5S)oCweV`xzNbE+M!$8YcISHS{K&z>;Y0P>f!oFo-!|rXa_|(qAL@1AhV?iRDO4U*V}g93-C3`txwvg(dsN%Qv#0J*<wRR+'
        b'wR=<t)z)QztT$`vd>DFNq8Mrh65blB0f#VWC`3c+?I!zf8jG#i1NC(;$5Q62D%FFtNd8mejQGS!WKnu^%@@LqJ>#s=*b$inr2ob-'
        b'qlJx%QI#-IH72G<d-|eM++3za^owIgRU#X<vavJiDu~_XjrHv88hS&!%Pl6~>)DfNeN$`5AM4Mj3<Bbn&q7WAd=|2WF`CAx65U~A'
        b'R2V0o&<<o`uMC~g4jzsgdO&+n1?!nHE^O%M+T+s`@6x~;_#3U~6OCv8pl7i6ghm+ejze0{CzIW0F7z0qlie_p_3@%1am<}Kmg3eM'
        b'qwd<K6{aWFYiBzq?u#FTj(RR#7^i=3{m^o#t7kC8+J^X{tE{WEe7q4M*2k-oCPzM2m^3RoDSbMG3L5<fX1z#CKvfaa^{dPT+~>eO'
        b'3)Vp4YaZ~eM1tX!y!^T(&{9B0I10~dcs9ZVsX;dpF$HKX5-JFtOuLg_ghzwA7vR6aa~Aa-w7ME1Kz{<-Um-oHIQSoouzc4{lK(I~'
        b'Q)iI;DA3`i!h^aTOcD|f<p^RFc^CA;Z{XP;OY%XZBGi)0!h9BRGmzxTI@;c8Og}>%5%o1llP7}CHVWmp!7~Nig`hXy1J62my3Lw~'
        b'Jf=(iB8ux&R1cG+G1S>auD4Mg%1qrab2at_RF<#=E$E;RLs|1WNdxM!P<7N?i8K@Hn#J@h)V~C9e+q4gx`yP>0e$vicv|6E2hThR'
        b'yBlym;D6-2zThOZcj;Ss`QZ>&<|YkHA67$qFGwGOdmi;if&UBXb7<>cph<)$3m(#w1+}^X$~*>r^!o*cm>)cMu((6g9buqLW*v%p'
        b'=Jf?nK_6gWN_U_|Y=`Gn7{gG=_t=ZIpXKEv4-nE1y>jeDBA)q$H1o_aAkkiE`x9zl0o2*GbS#K!E95^2k1&bk?*^UtU;mP%70}*R'
        b'cwF!>8=UII4FkDvnIVs#!t<phEf|xeS0tvdf>nN+auX`l=b+#*YR&h6KKcdYu#cd;2HO4!gp$vM@W11rsK}u^F+7~S4EUuO%x6qO'
        b'{W}&ORBut?hSbQPBl(lnBy1er9T4+D=Z%7~Zh&zXpg*JFX#l_UwIqEA<)I!t3gaNn9F{7k1CK#|EzQl%<TTXxsh71=&>le=$Z##{'
        b'(oj*T^c_(D9;)Z#41v~y>^-Q~skf^1E&C^&N|6rFk@gRk4x~ss-y`?!AAc%YI-Ce0WgE@|xjRuBpqkQfGA`w<hi6GC(db%>D;b9E'
        b'Y89?I#8%Z-^!6Q&mEONrg5~q@bcsjwv52cNl&`>jf<TE63i^ZF#OGC~cSk*|+WQ<`!D&8g_f3$-r8lIjVAa&;QbCDjmQQ_Uhq~kj'
        b'VhEG6HAc;}+~WLq*F*TRR+CoJzo*JS9(D3Krhc_`Tzc+eRO8kbJaNcut^?)ST#GTwFrVyJK`UG}Fg(^!x8A&1<$*{hjay4&LRKA>'
        b'8uIVORNGfQMjFzi@*6SEwjExM))-WyTLq19mF45HEw$_O7poeIqRd5@q`Wn2T8QygNv}upvRyTg5pz+Lejd$w7v>mldT%VB7G-QD'
        b'G+_4EXS1<S&n46HQBT4e#wW)ly*j@8YcegLY#Z3JO}`~R3I!~!yy@5&HwIeeCUXDUqrk>6#((e-v)NT+A^NX@wOl909~>`wT#2V8'
        b'Zr_-m88bf7xJ&DP4%dNXtuS?|T2PxCx^gr1$?HYX%pZz>;)Xd%V)pt}&0~{~cp%5{L%$J)<%#DdkLR2CCkn+mQM2z?Z%8J>hNJ0('
        b'7(K_bV$??yi8<Sq^oDxFEUZ9m?UHo$QIKKx;G!-pw|*<NM>0>|@}2*dJZ6_LtD)f=eMVGFW`wW-D)e)zpp3^F3%6LmmcSVbi@Zm*'
        b'^D8Oqs+ofcVB}#EXdz3J_$8zfHXqdFO}CzrF#g9p{^SV}5-d#oLK4*1oPjoA1MU%)4}B&HLMqhbppdsb@iVDscQh!Y*s4K-t(yM('
        b'*ib=pvu49P63P16=A&OQeO^2wK3zNERL9t1``EzEWBUiUT6dF^>Cs<#2$(WCD$uCziM@Np?x9y{FVnS95Mu9vQU^W1*!d61y=sii'
        b'iH4Qd)6<12^UARvFnr=gp4I@m*DNv!>en;^R_f-3SZhLr8L^Rx!_euj=GQ)D+R>or*`4o8vU}aoX|G#?As&3>q`MruKo0!X&|jt4'
        b'h3+Cc)S8{&N{_0OHM`WpB<o~ouU-^gpq7<<h&F>ekE%S8?&}f9JQ?E2cj;Hx={<G&wmN;yVtw}FgKBpMMvD8z&PPPI5#0yX4ZjrK'
        b'bE!TO0%IHE)}cEqV;rQ?KP0-7(Oa4k0T#CwGz_Lh#=ac;WbB`Gp|NLUKiTlHgni(iIX3v%OllH<JwPo1>S>FVz5Q2%GIEG2Q?f$L'
        b'`_DaTY+%wDr{z|}#Ic~1)V8;NDGiNEvc3`*HYTph7e!f**`rCCq)mz!t~ujYVNF9XpeQ8hEJ3M=X~ZpE_rQc{el@dayQ`<i)%=$U'
        b'y~jQirU`G~^_=*i`e-PrnEuF)h~8r#L)iVH=cN^qkL-x-J@zkQ+PBGn-6FbV{=gvy43nc`@CnKN&kMdi2+-lg0x>ZR63xDULbhv<'
        b')_OtmJakBy?3uNm(~Cy2S2I3dE%fw7i+y76v9nt}s(26SN!bPy)u@>OBb)V{s{1RN-a?>^m_gJIht5fZCNg+Lw4y^L#2!@bQ75Y9'
        b'vbU>+sYwwL+gELU^}^FBDj~dwbq}rcbRk^av>sahpgKR_HJYs7wEok#;x%NyMs>WV`>VZkwq0{3H9Y2Ssc&O)M31p?^OPQ=Qy+f_'
        b'ECh|1y)9K!a#rg8D)d|4m+r?dBu$zqgx@tO(!J|K{E@NlbK=Hrso`>YmYo+0LP`A;?Trs#$jZ3hy%YQBhmr1w5x?)bAez7VBz^hc'
        b'58rXY@Zg0D+S8~1T`~U9k*I?jV6_J@&E`+`gt`A4U4ps<H{gjd2||93A@L<7H<67&+}#&?)#QO=?t3u8y_vp$O3A`|3oyEScq1Jz'
        b'3u#x238FYl6vZhZ=IV_hF+UE=FEE`hioT`j=FrlgQCq@&(}n&YUFhkG>WjGRYSWHr_ZrOXQI&f&&2-|vbr*zdE5@G)JM)C-c3@ba'
        b'YJ2qN*Y<?F?da?NYQtv|*%Q7l!hI{PO#6jRKki(6s4uLc>(K4ajbV!xZ}<>-(}J=2FN^voMbC0^PpG?*vC*Co_s!_qqu%*3$fVG>'
        b'=^WdmcCWxt>qkC0wbi4AcJz8g^Tzc(TR-SN|L(b-J3r8GnF995yJbTUNXO5g&_a)@H~-dMMTtLT#O@08Z5ZKW$)xVdgQBo-=Y10E'
        b'*SxP7#t{|{7hU+^k-6^)S=(VbJ2n5p;TtXt+;CyPCw}K*(z9hsOfsq8s6q`uIP(eaSREL@cej4;Cz><QAA076&rj}%-n5@Y<a@UC'
        b'Z(T%Y^kM%no~(Lr0$RDk476x7X#b|MAa3~TY1j?^$*#M=ZDH^*bJ(4PLH)5824XL8!9mTfi2i982BrlC#atMO2@0BgVc^5jz@VrL'
        b'15p<)5?9DWJHL^H$iy15N*y9-PB%xN8h7FSaTk85-g+c<PV>#0995;}pyq_8<!W_F5^0TpHtyAE_diA%?++pF9~~Va7mh_Ah=YY|'
        b'b#Ex$@L04X?w!%Sr@xs~^vQ>&=SGEzpcCakA4O-yo{8?aMk$-kNjIPVMws}?-}8?}<^S3n`#HwOeLBiFAoqk_W((5&3ML%NA*Vx$'
        b'`<>BU5u47t-yS`iJ^sk-*=5rXMlM=&_m0q0(%a|H-te_?_UxM@b5z;Wj-HdKeSO3eyWb-%8gTy!GntW|qXJ`lR*q%o6O!TgqmSOk'
        b'EZ=E8y@`V6-KEKD@iEiRKT5~%e@~+msFeB>FjiP=$d+_Hth+sK)6suZz6PllAFnF#kb|1iNs)=af?4h<SPv2^RZI6A_B}T`@Z9Lo'
        b'bJG0C`dgUf1q<e|2n=F<lw7y1Td3bO)~C8_P6XK0FG|9squ)xs5hP|8Nt#+cWB1lq#iM5-K=oK_(lNuK15wS-f85hE@49EN>w9b5'
        b'$-d|VGdA`9CHdLx-uR>$eZ8xaHhd*rxA8!D-_&R0HyTU6kUa$(YeGMj2;@`0{X7p-Z=4kRPiVtovP)f`OHf)Lm}J;8`b>IQ{1Xoz'
        b'#mQxTLh|H_F`tYbjMNEH1ETwG>^z;Y|Ba~E2Hbaz(w%^vPfCV6M}=^R?=2)dACf+u1GS0Su7-d_kCYVo@ZR0go`Ige$oTlAaeZR)'
        b'2S-tU3?3GvqQ#vaDdzlWa(w*<XOmUU>Z_C8N$SYtFClX1XVN2+qJ>HEg``AHl5g9i8oF0{Wb1o^I`mI`{#mDy!G}I_Ux)Q@TSxn+'
        b'jnefulo~vl7Ip6vWBNkzu5D#e`^3Q`QHeuPRtRp%O9!=k)I;H9zs1xWXBxERKQ{HCYVee5=mY72+mp2K7|f#wwMGqz(OiI$e^(0q'
        b'3Ue%YS^9_e<pSvG^wL?^0Kt){p}$G>ubn>_d1Qd>QMqrxia?`4;RK-woUv1lMHJ8?Vv0tw8mCk{-<4uEjr_d!tSNJ}Kucm?{`R0|'
        b'!w}j?&6>#U_+(>_DkVBpL%Kh@Yuotjn&g6<=oD45Dm(g`Gs19I_C)C1yB><TE*+G>-1tz?Rn;k~qhCpWdm-)wI-}x7h3i1<#*b3P'
        b'2iJSe32pr!$f;{b4_`YP`>TO#M|XlDdveO=2T#S09-clL`#h)`15-xb(-{ffS9wyb|A3r|9z7g0IxuN;zbDSBCIjO}k8eBTdCRS4'
        b'3EfenvdZGWCj-eo3wcii`k>YwK~qRf-wGQ&y*Ik&Cs&Dms=fP7J<p2+n$i8gyWl2tBoB@BwC0Dks?V5^0Mhqg80mhFN;A+JWf|u_'
        b'H$t_p%|`~#j>xJPlsxcn@I`sohW^h-y5GKt_A@W-(E!@5fwX@c>Hg#*+P`^e-wU99CxA99e*CF7M-IO^68pP>H%Gu4SdtKV>dzyG'
        b'-x!H~=jeG!n3|OU3XU*sNxVvk*peJYH9_EkA8JassY92L(peKu{eI-|??(nsj_e<}Iq_eT;q{UJ-;d;GWj(7di6ib4Bb)BrsJiP}'
        b'b!Z{*-oDpH-qW548+^M5wDt!h>vJdWdu3$c6&kqJq8j>Es*jv7x_aNUBLfF$;LyJ%A?C4L`d=Ke>>J6-(OO;@xuqprm6bDN-}58S'
        b'J=OB77~$IYLQaIjDvst;YA7AleUFTs7>5xDLyrzaOAY%*-21Uk*|&l-cV5;3b?CKZ-xDJPPta1VUr6<vLhHXBF>D{%x19!onEM=x'
        b'j(P69+cTnXIb^tZq$NAV@bHK}tH<*2$SqAR*-`rjpbA;Pq9vWsl>AlNceh-w<|ybBasNGHXdam}dv<#Cz8xb%%yUJh>FSa{OF}5f'
        b'2E)%r;#Q92-X(<IwO<YE!M?35#eS6#+R)(Ia9konOz7|UI601Jk9dHs37QpEBe*tSlcSE^d=M%+)GD>BQzMTrKfXA2y|Fp#nloEN'
        b'XY_hhAQQJ_gK_M7pgf<dq??cJJSIJ=ee7+dv%V@7gldhRkF%zP#JNU}ekp;hhup0dQvDp2F*GDroAuP=8?gK02UMY-fJ$@pBWgeQ'
        b'CS?6kz3Nz0w_0qD5+?OD9}*Yqk6#@#qy+=>4<1#+QSqQ^_b%&7seZXuFaBHK*CqDp^?mwrar$f%;9HDaH3aI@v+)p+4{q~7)v^a_'
        b'N8Yu@JVJmP1kj!^>x+^xAxnt7rEyhLmRA=W^bq$#Y<_>($iA?V`?o?n?|WX|>mmJQ<gf|?gc<k!MkS2f+b8ZjbY7S?`*~#CJ`sxh'
        b'bZYbRg#OHt0Zew^b5Z>nBlpLHNiaKC-LqZX(&Iw4S_t280oWe5V{y&-p*mX~AD?B5n=>oL67P9n&g^B;OXE^*#0~uvl{tAmOu1}J'
        b'dH<?cVp9g<!$QhbvlFHzhs}OceN;!{XJ;+7nBx!S8jUSkupp!mdL|HlFm#W`S_vImKPLio+I3){hwh26?v=`7^37A~cZRuNKVO>d'
        b'x;uSoXpX^f{Cxk3^SK#W&xRY0o!4jdWMz-*jnnjGzykkG{ol3Q`!_G!6Jq@wvJ>^%oZB{QKW(%wmmtZYCA`<79i7s5<90)`YDai>'
        b'%#8R&eYrU)s*N|^-F);7i44Y(4{-NFweYtGLv|jK>KBg2eRUqXdb>%8+@k+RnDLQY|Eq1D8xHl|M$)76(;J_es@Xp9>8ra;2Q`V='
        b'FoR>}M8fJGw|AH59y&j|@L<FV&7P1Qr`)^G!x(KpwdGMUF;Ds+POC3Er2o9<W7CFrq@G=%RY1*z9jB~jY5S?Z!@I&`HjV9?8k0K)'
        b'qNXzIz_DX-o1Wb@ZgclB;iEXuas8_kHvi%9>*wEu4iGjC9onsbbi%Ia2j1@S-23jPo|g^{K1@8v8+S!-JiO!7U-k|CxAfLN%ym)U'
        b'2GAvr#e%K@2Gwh9Ja1OVd%j5N|LSmppnf_-bwQotjvr9R{BhcC&zx_a-13Zi!*wvTAVwH}KqG*m*RI~%y6xmiS3`T$xSt(4EH)fj'
        b'za@G7XJD#teE%!Uc<WK=hw8rfQzM5@)h`U&`rEM`hfjn*ouc-<CjKEV{LB|3Oi-=$9USZBA;R=;Gt@gHrS~Ea^zU+?&?f#)`e7s<'
        b'O>5${GqNXd9(+1uYJ5Ug{1Gv}DGMC4)73}QN!&f>OG051CS>i>?)RLYvs<`EC+vNy$C?7U#=Jec%N?_j2;+ACRD$JQ7zc)333h&o'
        b'k&qz`Ou>j`H|U0uu<++&IIQ<DzlJtThktNhH*Sy0=sCS}gOodu>W>=t+Vj*p+WgvK7ewnH5{K@T;@Zy(njClNWU@bz^jaqD{gwFa'
        b'sl->LzV{ED`t<%8eRnV3a1}Z2jDBv-_OP(VDZ4^FJM=rkW~8sZs?%Xwlm6ibux59~fQl<<VCCMNne47New!M$%f0z_VVs~zyi>|?'
        b'*RT3I`|!83uCmmf&ko)EMt02RZ8a~)-lH~ZL$Z?ZVtRr4ghrUN^Y3h*E>2}QaZU)&*4!MvYL=?E3C;cf^7Dg}$(AkO?Cpxa@BS&<'
        b'C*PMDx^~v>JMMeBD1Ja&auu4l{igGf;J*7!_1RkJlLgq`6JdDU!95?{pfDX?>b@SGvBLhtOJ94)osOP&7Yb8nEZ*vAFuo+-_p^IT'
        b'RD>jJlGLH`1Js`F`SGERS}>tU`T6!{kkz2o{QVq|g7xT5KA$u>+&%kz(kwN+H%`h?_f6_Qel9NYyxFX+{~C8W<6Cufb2G^lcYaHJ'
        b'6b(sYAtx6{=Ld$ErkxKCx$2^jNx>lnPv9mg+o$F^a!<kIl7GTLy2-+w`Sh4NzI8GUi0XDh3UdvH)wD+O%pWFlD!Bq*oeK&n7`!OW'
        b'C&6h<{|pE*w(6jRsdpMpFv-w;PVS#cEadd!XnkOa;mvbGd2rYp=Sa~-312_wA2OI6+x?_|ca)iK#t*i}(o{3I@CxDf+t%b*{f;Q}'
        b'GS>K5p3Mu8jTn&eb3q~4bt!1SC#yv98`ebbXI;y#%Ct@^d5P+ueUp;a^@9;+b3)SOxiRZW(yWC^>9<(xaiEOJNpbg`%U`S#<-Plw'
        b')}(xs2^<Bjvsr&(nxCHQ3`|24B!l(F6ZD<)Tp~frhR-D;=h1WS<Ry~KIXWaIO|E`yebTIs=Jd@p?WDLLoHLuJYzas{i6*}~^lgc!'
        b'5ipJZ5^1J@8pPAIU>fr!(p(jKOir^B({x@UO-$&E67RqM%5%q8;g}&4Q9RA7|6}~X)5Gt6K*#htrX+7|y^ea5WN#Aa1a$mbr_zW?'
        b'a>OL6TH<~n<fGSX-yOso2PsK$^Uvj{M~i(?`fPfZVN2p?6TK;u;<C<(0dbQ;hv`^v2XS!RCRbEugbkzAu6S#BaA$tNHi<jwoDf0v'
        b'd1^<U6Svgun|1EY4i&pyu_J0<+_}BGqh!6GU9-66ocQwuJTux69T+k7oVWuc8UiA=hl@Jx;2sIgh0gfsEq>Ql!uy4DvR~e76<v>g'
        b';0`}G5Ppu5#)Y5r?lWu81=L;ie6#Z#y20%Jc6iX!6R;`GF1(x{mUpyE{>}Orl0p%*x_Z5<|LfrxwRZm#FZ$gh>5CZnVi>HS!GV0a'
        b'q`W!qs$n$M{y9wZ{f)->#2tE`GgP2roZqDvp#K}C-$`Wp&@Uxo^z`U=h#S6=_hbJ!Jn$yVO&AB26bDrSRUdpD`wJH0af6=UZ95du'
        b's@I0&kKj$7fuqABC{;Xea6soy9F}e0xZhyr$!am}D&{{hOz#-Q)eeIpnlyD{+;hX5x5qs@+<R<Hi0Db##{0kj@!^4A59{MqtgGXr'
        b'2Ewp0{1RS-kn0wFWjw^oNDX1<UAu<64?sw(wr1dTPcwFpO$)EJT46)O8q8pw*5nypGFg2z3;B4dR;W0%Sd2e%8jlRMLYANvW{9r!'
        b'HJ*@O&vbFo`agJX9rQGdE7psx>+=&t_f{<W(4V5k_rxO}HQjS;cHe`6?}Z9^+`ke17qr3zAyrtx!y<WDmC!D%z<tSPcgQe3zv?{s'
        b'Cgc^$)7?Hy4I*JKP(OedcbeTJXCcUR+i;v|m{xgq$XR+bvAfI6mOU-?3dLrAPciPs;T$!U5zxLFJ&U7g<Dii@kAwDAh;`e9=0A9B'
        b'*s!*3LRM;sdj&0Z@zG;4Z!8-YD!&44Vmv6-v}Wz@zhE`ob;H68h=AHvLZvbM4Gh<9a{uxy-GX-4P(EEWy#FymnS5NjA8T(1p1&6+'
        b'^%iyxOE2Yx_va69VLOiDhWuf-2?oE{kT;y7G0dmKtHJAMQ-(PQXyiLgIgFor#BX}G{QJJG;p6(c|8iH3>Y6jU-q0~N*LGfzX6K6H'
        b'{YSR!GkKox+4B4mFt4838rj=O9-X{nR!X`s6)mL|;df1%+UxP$HR<ZD9<ZD4+xn4^B1|0|IDPaRuw8AS3JE!(BP>tD6fCz)lfQ6E'
        b'(v<kkMM(*jY>~>wGdF17jCB2`BjxHxC*|Od;IQP@4%230ZK3&7dU~~=z6Epp`1%#$LLoRpzk%f^y4Q0iY1S(xpGrcXFnLe-(a)ty'
        b'4b(|Uhadt~so!>?GF)g}0n_aChJP~MY=tIkQnb<I$=a$uS_u>U3^+Da5<zSD_$&;d1_lsDY6cFI4Ts0@;aOn<1Phfy8z0t2K75&H'
        b'*)7^HB}gRx)Sx%+?|<j4J|nIt{gAMhX!3jX``mv$t51*aNssC?%s$XG@aMDp{(M%x;Refq`&IPiMAFuFzvfAg$}gnn<>97R&h}Dv'
        b'07X?TU$~@R_u;eP?|qoaH!}@K&*nrxD8GO<@YLDv-^pd<mx=DDu#9pnqbz*zG2$tTq9suOz~g7Zk497xFZao_d(`C-?mcu0?LO<?'
        b'&87}sgEF%6VC@&Clst)yZ`kGQG~PS0wAUW;^&0EU7z`E?O7`*jV*2UX-gv5HBoKY>l;gt(;&&OXzmu9Lt9Ndp3q<qO<fO^5rm1Ip'
        b'cfZKev2HLnk;FHo1CtV;l6Dz~K9GPHNOSV>K~K252MdW?jdfD{*XiuH7=9bpN$ppsFTZ62`7&bKO6c+)pM>bs#x<XX^*Sye-gH&a'
        b'#x<TbwVy3lBW|Q4sm||<GUcAl=a)i5f6sVc?D>YoM~lg#d&OD*wbEUC*5@{#P4>E%ogG+qmd^Jr@hV&>mYnr1A1Kr7&O&J5N^Cys'
        b'TZu6b-P!KjY5M&5Xw0HKD2tMdvJf@~tmW>DZkp{|ke2X=0{sJP^34Zs_{EatPtIBN)YPX7t(!7lfAAL5O!YZQ0R<FLKmi35P(T3%'
        b'6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%'
        b'6!`xJyUi*!{fnsigmkQSUi1Mmh$rMEp?{Xr?y}H7upShzB4^m&2k&fM$NutpKs@`q;e<4hW=o^X?pPO04<%b@nij{Zwo8=XOUNp4'
        b'{SR>hwWY-x5RZQg(I57%`@`+$7j1d_jTf&y@o>lT_mmM<Kmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35'
        b'P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35'
        b'P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$)=yTHex>ipz&S^1w6LL%THl7w%SNJ8>X$Eb+0?!>Q%A2c@_jOqHU)Fzw5wT@g2'
        b'Esj-f<O-nI=Njha8na}7b)!o(8bqVsm`VNf(&nWZuSCE7mdVD4!y~7))ZPF7UmO1VQfT__8-ID<aQe07lV19Fo0j}v2Fx%7o=|wg'
        b';296k9C*r&wWQryWNovoBXiqqE?1ki*-46P&FRL}+H_*fH0br|q}Ao>bmq>T+hTLIcCAWlw71X24k|NM%%w?5VO8PEl9Jjwu{K?-'
        b'GGx|di-i`4!)A4eHAY`w2)_EvQ(wBCo+MJRcWGAs1Bs;I(5R+BOeF<0J%stEyQ!q4rY^U*rsn4Hk=#?gh`VcxYirA^t8#0KYm4hJ'
        b'EHN!}p0nHG>P}2E=$-I3I!QuF2|ndjCDlk%vLsh-1GGC;pJqri=3;_^WyOffiYqFriPP#>ZFO`fLLN?}s;aIkET+j!i|fkflg2ii'
        b'wZr9$$537`NK;r@G@sBoj7~@(3D=Q?Qj#!>B$ShcDw432BtSW4l3*^cswD|f`?~U~QgE3nOf{8&p}o~LfD5ZDD@|2JwS*j-7LvDL'
        b'9g_EJcn-kxJUlPJa~PhN;dup~6Y#tN&wKC;!SfkBdSL%~8JStxIhIw8P1fdMhQF6+3l0^Mg4QC||5E^a;Q0u`bT?<^x5D!j__qV@'
        b'0UY&TS@}&6w;7%l;1)_r!ONUB82$iHG<RPIkIV|E{K9pCBn`5ohrU$}Du4fJb%WZ^FRXZVLE9oyAeKY@p)PNgk%D}vPl?54Y0DMM'
        b'JAi*XEiT)tHmlg=u)&Cm$%ONBuGnc`0|E99(P?dKPIXzGE-~3$U7I2{TWoFCrZ^bO#ip7%1AQCmJDtAgVfpRakUS?m>)^Qqp5+gR'
        b'<V_9>$xDPM2cAlJEbw%}vk{)Uw?gtRJQR|*fRtFRO=7FPt%($_YlNCPT^5In6tvkJZxx%YZC00+)Vl1QVw25jftr)zcB`Ys+R?ZU'
        b'QrbI-*<oL0#mGi`M~Ai1MJnwsy8|lS)h4^wSR5U;juuj3Yqz<aq8%FUur)!p5C{dX!lHOS80T_WR$JRx09h)w`{lPRz_&cW7m!jk'
        b'2Bro7@*qDe(2M<xuCv?QoK~01>hN>=C#W=+LT*h~94l<|Qn3x&Cbru;{N0ed*JoJ^?pAxdl_Oe1AJwt|s%3su%NW%%nQFNo)$#zU'
        b'<$hGl8P#%`s<zYC(FC0hZ|hpGud@ppM@(I7AzakU4ukA4%8qo|F;8}6$c{|ektI8_Wk-%TLtob3yba#W4c^=h-s}zD{0-g$4Biq9'
        b'-XaX%GK}6bjK2DN%P_JsEFG3MdyB8JKEENzZw&GW)6Wa?X9W2(gZx=A>`s@plPondyo@96UCt5rE`=H8z_f^#u{ZN9XK&`Ig|wZ('
        b'npAekKBs8ypfh!;>{#v%Sth$otQ-@~#^ek2@s`Ptn@o(GOaT*)P42>4uVbm#wan{U?sZkB`<(N9&J3S3)91|cvZ%eo>x8PpWV88&'
        b'n3q&~-A4bU#!DnN(&Uvkr;C)d+3ihqgzQ}|&I{-=cwI)XE8Xjw=XGUxU7222me-Z-b>;YS_AA6!iosWm!B>vKSCGM1lEGJ$!B>{S'
        b'SD3+9n$cI9(XUOu(gNp$uM_+N48Z}$;DC$rm=_$75gd>i9FRpSii^Y=`YxsK0{UJ;-<Bqa)ybBfKrhs;&<>KjQLM3oc$Pf{cDqYY'
        b'D$8rDNo93yIjJ?5i-i@77_QZGY~a|)aXRpW#o3CiTw5eIS{zOO&L&s^LBwNH2Q3R-<ux~g3R@`F7A|7A$V3)d*L7N&U|!LM3q!fH'
        b'W+|y#N@{B7WoL*rOXt=t^<&N(i_1k5eHYL-Ur^A=M0GtF3SE{qy3&hF8Cu5Ba)v6?IiAOH2FIBk%f^CxTu2`3FGoN>K)vNSU=83M'
        b'H6eMZr@sY$)YXRoqrUzXVAR=FAt8C;fF}V)8|PZUk*F&H9tSuNFzWT?fF}T64tOFePk^HUcK}BHsvGcBz?%S11AIT=>40|wo&oqd'
        b'z_D0Az}Eo&6JS)`PXoRd@V9_xqAd{`k|$z)0LK9q0mox~0M7!P4mbhp1vn9K8Q>(q^?+vsUIjQAunlkuU<Y8dNqz(v^}@}7Q4ib>'
        b'I2G_O0HYDG3$O|B(|}RId>L>d;1ht00RI_qG2p)eE&==z;8MU}0xko59&kBe4d`DBQC|eS2=G;aE3jWtPXn9`xC*cla5c6Auo-X('
        b';2Qy(0oPzZ0|r%`G@(9+{S0_9;I)A30rvu4g6#pk6!6ahFGE`g@N(>Tz&ByP16~36HNZCmejD(A0saK=N~||vRD>hLL5Bo99q=l&'
        b';{Z1THUMq{oCDYjI3I8`_B-Gfv{3<f0A2#v4)|ukomg+cw*kHdumkXIfSrKX0A7#d0r*a=Kj0q&egN<Wz)t|a3-C_BKLPwW;8wr~'
        b'0J{Lc2)GaMZvm$PejV^!Y!_fX;C}#~1o$(+w*wvl`~$RABSP}J0Z#z@L%>r3{|InA;5z`P0!BSQ8?YO2A>dxXRe-kuUIw@y+XZ+l'
        b';MIV);Wz-k7w}I3{|xX$fPW5nAK?3tp8#(M{2RbK03QW>Kj4#q{~PNK_yNEl0)7zi=YanQ@G#(CpdAw#lIKBw0z3dX2Jj%x3&0Pd'
        b'tpoUBz?pz|0yY8uCEyCckKnif-i7l5@S|u;0N#y!1Q<6j)&qVF@J|5mL3siAalj7)egek>@LuF2!21CI4)A`!?*e`j`x)?4fX4v;'
        b'8t_DrLr-J<06&BL1NZ>o0##_<vxvd}9P$s~=dphQ{|0a!;DgBbfM3A*3;0FAw*x)|_%6VQ(S`(k1nUX-CBXj!_+`Mq1pHg%7r;lc'
        b'-vPe@_yxenu-^f{3i$VcU&DR}{5!xO13nJ;YrrRvUjV<3^H>PU`#s=sfKLLR1{iJ01i)x(&IbGjre711_eY#B;QtfO55RxM`3(3?'
        b'90$N};Wz;P3t$W2x3PVI-vQhS_+6YAfZxM;0r;<gHvs+{jtk(^IKKhEkL?9qWp{y6XYXoh6<e*APO%yEs;c^0aaC7yv(*ttYQd%f'
        b'^UEo&aoAi|*~SD}j|+ubO(v<;ssy!KovBu9%G7G@a<w|7O|1_7ky;(LMXe4WRI4MNQmZ46s@3C?G#b*O(Wsu$u<fIjt1WF^R*qIW'
        b'tgbFchqZ}R)|P@)U7DR2HDxN%h7*CH5Kq?W=j9ibRha7t%0@lSL4&q=7{N{@caSi;#)~ey2sS3v8uFf<P&T`JcEZxx7~0iAEyzMk'
        b'7cQx};$rHD5{s!;+eC_(=?WHZs}-!;BD>weoy;U9=9YG`xTA?cL7;#_zrd<bm0YJ^kdx_=q_)j!?L>Pv&=M9?MKGT&4xQ*~wRSLF'
        b'A)wA>_IAvsky_af>up`21T=y92`UW_q^390IINDY4)GTIDkvU?3(BxUu)R%evv#z&T19(vGv*FegLc`Rt=PMM#_fNq$tBB_W7D9_'
        b'cCd9pOIruwU5%|`XPd=^{wA^W%9PBOX3PYoJJyMo7K^O|BCHPJz;@9BIbf1CHfTjcoq37aY;!nWahwt&T}&|&Er3=-u}x{0u5PE@'
        b'X`=~|vuQO`p;yxUH*c)dnZ85albOzgux2vTdl2rP%yb`w2PZTA2Vv)ArUM~7KAGu32+vMtx)8$A$xI(YczrU{i4fkO%=99JuO~Ad'
        b'24QqE)061_(-fvFA(*BxeTi;3O<_6{!p12~Z$kL>6t-p|{1M!fxqHG@A$e2yUe;`IU&X`Az#YTg4_AleUCrH1S795QNbE^c@agYK'
        b'f%c?tuS~_?YK}F2d$@$}<Em6_FBfr`k4Q$}3no%J6^Y{XGh=673;*b=_3DtkTi|Jfr{ikWUzU;O#B`}_7MwU<F+cLnhpx9z(&S$K'
        b'%#GQP{q~W}gIS>&KYOu0ea-P-8CG^i=%s($lxA+Tbaa5V%w(YGwA~JjXmP>>Y3gc3>6fr@K1gTP_{dVWDJL4z49((AvlC{Ez+|)O'
        b'Ch2U-aIMz1PP*$0f-5&6K}?t>CX|W^<zhmWn6P#}NIr0_o!@5bu!@i?!?hJ=F`-aQSSluzi3tVbkHk1}f!OGBw56`a%u>lsU|Uob'
        b'RTSqEn8SqbzUGqngw#TNlQmu!FLJ4k&cz)dxctJzBCE5}Ve7;>5s&-6lqiD7M$qIDMHZLEwXV}j9oUd|i!0(18AMdt;IXWQe8xwn'
        b'0*K@$s97$3*VdWpigSyq7uR+B`Axz8@~Upq-Q7**SIsqHPtn#CRu@6zZle3i%x%9FBCQUG-H{7rjgPFct^y;@D<9K{4%`7jWJSk{'
        b'j;d-XLo|u4XreI*XKzM%N2QU&-qr>qY;$^vL`yU7;Wf5eI$E%?u2zV2vX-Yo!3jhJPOz-CIomDHTd4;M1u5FW+%{LU&Dz$K8{iYy'
        b'w1RM!v%z3d&$m*Xv@TFF7b7V*gY`<ySAyF?*ea-rH5Xm5EHG?Y3m7{A7=i7<!|3Zs1hI9vtSwdtX>PMyTm&md*2<M24oj2GzN*XR'
        b'vUfO%t#kD}(rIxz*Vr9R-fT*1su!Da^r~y>a!ElQ3=5iufOKY(okgmOt1D}XAuWUG;VA*5X8sGH^ML%!{SD|gfc*v@2lggd%yUV3'
        b'N3$JjyoBxVf~%O0qezOZtGdvClewk<iY=?I#8I!SsKz>&YD~b@$QI<L(hLIxm69AI#^;jmOr2h*@5Zz>l%ggd`mZz#o@{uGdVCq+'
        b'l|x_X&B4f=Op-=Ja`2T6Sr#H)juBp&nedv2N#|kgymWYBvG9h#N_>E{5|UP?qbCzzP+BFVuB1saFg_z4UyxTF5le_zORm$AR2?zZ'
        b'70x#>q}P#>3R7(vDS;M};$m}6btSo}zPKhA<wzR2soD%pyvek*7T#6GOVC?fwYaiYS5rr@k94G}8i)$OK~e2|VlLE?ni3tUuGNu('
        b'A{{9PTxkYHs=`!PhUv`Zkf6Ary1GtBY9X?=7*f^L0a>A`N=I%gDX*zqVyY?5<p&K^YSosPR+%bjH9#k<t*fpvmEs7M)D#zsmBp3S'
        b'HOs(PR8x+XC;6nZ>~`5J!b4BFyaCV*@MC5L)ux&vz?G(@kZG}5tU-n$V%hDqRMX<6VmYz^=gOku+Cs=a-qdCR)d0m6PL0*jS=XUp'
        b'W5JcU<I^I?=u>?$K>{zHGT%knu+U57!Xkn)DFe9<+C-<V(U}Wg$gRB{^d2X=WtEu<MK07}xa*4Ri>vCe`4#1r<><&QBe@lf>oJ(i'
        b'^x`TMc*xZ-I=Q6EE-REMq*`oF5KkcPFw@Fv7!Vk<Dk=b&x5Tu#0_R7i+3p0igdtN6ePM8Eu7M#v=`KQd5xDY5IclsmT^%IX2nr|)'
        b'u!Z&(R7I_X_F^tWOdTeu8Rs$um!5o(?t*40p`rs`MRib_?vh%3!DGg-C56@Wje*sxu`ck`Ho~h69;~k!G0x@g@(%V&g}Rk2k=c=S'
        b'Clo?$Z-91#x?fXPTU1e3TwPKr-YAM@un&$!s0!YN=hLfH1;aB{1<4at1$9$Y1>FSqujjV6llJzxxLpm%X>I&3BWbd>__;8OrUVa}'
        b'!-3eE){1#z)k=_PHFb;4D=W&Yipkt|P*v&q@?0*_ooS7bRLq+XNeiKCnrt1Qk=Cw*4BMULqH|lKLzyPig5hInTG@zXE1O`s^+iyV'
        b'>yj~)gsQk*ohwmk2qp@M!~K4Cgd^Jpz~1e)Mu#2RZwIbTThRdvxvjmc9qgG-D}><rA}&mzXg9)?fC+$FJuHQw71$arZEfo?54v>W'
        b'@`P)u0aOuVT1FbKx^=DIqFP~512ue=RaT$GW{16<l5*Qgr1l?Xk%0?k2d-~v^w<G12YbT0wh@mWEuB!AwKmX1tWdgPo?g7Q?DjM?'
        b'P+>h5ovn7z_wjfV4<jw>SWakfb<$<r4)t+~P3t-=&~Ub*<B_5jbQ>!_vZS^fKN?9B>uIHo85!cOz~xSMq9GrdfVxrMfyaDo`KEPs'
        b'+FCj+ZB8+nS|reZ`<j%%WZvD}?~s;PL_Ysz#maPPVx`^b;&D!~%L%f<my?{BsWjLs8)oc;g428|QF-$v%7KmnMTsjVPD{HruwdW{'
        b'==!C|2T*2EC!kKmkAiF+on0<(Wdl+%v(7(3vJ;xlEO1#TbK(gMZu?^@%W5zaEvsy8HrG0+{}LS6h8lCFFEN*ofpu-bS~jAzLf!%9'
        b'txQMdymB6f^UkW(i%zgGA(d0Kp<>ufQ`U+%h(R$Oa>=u6EbWw|SYfmMOTl`GU7a)!>Ta^Hfk|S6Zp2iUw#F_rkogQqNY9x^lO|-O'
        b'=b#4IX{EJlTlb&1hFY>XKy>!<vo;(M8q<Ok5}Lf$>hv4#I@Dvmd;oTJTN}<vm{e^xNDY+*wUZgjFjp{lUt(HaS$R!JhdBpTwSiIz'
        b'VuG%Sz!@l?fTXdltBGX?63EqsOID{HTSCQ0Gxv&Ar|xjEN!m*HJD{$>lCT1a&aPFQ*yf#YB0XSShgJ4A)M;z)Y?C?4w<F-!XtTxP'
        b'L<7!+Vnl8-E!b)8v^ba~VG2K+3w~9mHKzOyJwVL?=uakXT49bgTVMk6wMk^B{Wx3>x|0UO0%Oxfc??DeDg{%vg5KL;vd#(9lrk1_'
        b'2+tL3P->*bmZpmqM<Zt2h+S@JZ0rIjwBCYkhx(u@51mfUp)|3;x&|gKS~)Oc>qM|jprx!J>@zD^v5hXVlWnb7IvTC=d_#_CY!$oE'
        b'=3`^QHsNTY9qW91Cs-*ei&?I&Rtp`&4zRW?GG{nhWFYhMIeKY<Cl8bV9TJ^bEwdB~Z=G07FO^^g*wzofK7t$$lH1FFyZ~K*xWGDc'
        b'0m{}j82aG)*}>RngWV3g)pwE1-UDYHkavN_<!HnPtg$)S-WSTQOJ~FP7cbc}us*ke>;O4n!;M5>7&CBmhs#D6TiIB|R8*?S>2Ol<'
        b'CbwC?OOMhj@=pEV>_Go!FoFMn*a&A}D*_5&)0?k9LHXm-@!d**ltE?4Gr(zYcCl7)LGGlRj;JA78e4HchRtp!)v2;UtqM9_m}&wm'
        b'p;*KA51g_zBXqU!O0V{IE6i9bZ(1#FE+-cYG*grsYfwV^=WLOCmaaln^K#f)TBz<XmZNxe*kDrA%SBX5v2rmX%vvYCJH|8eWdRx)'
        b'7&lG6#<%)yHT$)}zi2Df1#vauYMiCZWd|jUYk_#*qlt=KwlEjVYcRdCMRkHkZX5Zp$hv?Oay6g}P?R%41>Lr4otRLT#}o^Cx9SFO'
        b'W`0GQ+ED3%(5}E$U&m^VLW<ThsOEe*VNr}4LTQnxC|t4NhH8E{O~i@DT82xK1*<}(C*v#cmO8%_CpPfSeS3$<RdnypQ$w1(^Y65R'
        b'^v8~;S$fBhYvfcWulCam($L~$9f><jP#VhsDLSkzmY~$^A|I9Jm=r2ZCk}E(AkSg7L4G*eaT4J4fVNuro;xl`E~={3TCKNwbAy&N'
        b'-U`_@+bCZLWyrN{Dn#4pYRGbgCU=6FU=32{nI6B&>RMxkVWugZXeIbFt*qF4d#TB~3S@F4J)OYy(}i8{!bMMB=-D)){p@Qe$ZpmH'
        b'HdmU+hk+^#ct(Me!#jyOX1my_3C^R^taMy51ItOqVFS_8DXs!L?N)k9<bb@u0c(JtF-9BcV`O9%R6J28wBbnxEVCV=k@go`cX6K*'
        b'T8A1|7j8d5WPlk*DuD~oij&tU&?#{q@QKAQRDuvkHkZ?Mwsp1GI*^!~fd4zh7d0XwJwr^!l@PBS(%Prc8P^K3lnW9*HChm{1+m%I'
        b'(uI4lpxvjD3JdCPDByAf6sl6gT;tqy?|fv#L?<~2R&MtBw}43msuV*tD=b(R%azVnYRVv6m1gP0(rg{>5i%t#Co9eW0vV{mFjMgu'
        b'FEALb20lC;D7zX_zf5lGg4L6<Xi8vmZ-0Ep<d(JnIk~KjuW7XbkIFVI?G!)R<Fkm7b!)vwQzLYSgR!I&ivW&ZZEx#h!a`mt;yX}x'
        b'Y>St71gH>e78mHmINDo3!al}%fCbZ%I`IGwk|d<crUOn37&X)((EQ}}YGS94@LEST60k!sOg2KOq3GgfEHupmb*HDX;w|<T9~VG+'
        b'dA(j^ciigiw7^WHCooL(qc!Ah3{>q_uL#k}64)0mFG|=?Mb>7TDeYPsLA77LNO7Z<)3HT8jZ}5DufmJKURi}3?N&6~`4ltIO?>7w'
        b'W~UJoUtZ}YTo`D2*eMIe;7D%vT_zS(7sq8Io9$f=SF2arq9}r1Y+<L?R%W=hqo``P(t$*7fChBAFg32S-#K*&+DG3x^+Fg*ul!`T'
        b'9n}t;el-kA#TOIrnoc=8&Hu)7TPj{0q^HqsUARf*rNx@Gr<Hd!I;_ZzXuk5Oi!+$ZiE+geo4rdX%>s7~(}>xhYhY0afksud_I4ef'
        b'=*Vo@=-n6;Z%T#HU&-`Jov6Rrmj^W~<<*qs#n&xwgZxTncMiO=nT>V8t{SYSE}XJ04of>sb=<OP=|B=XMQzZ~Tx`1o)C9c3Xs2CI'
        b'Rc$Dyyr`m>8_$q0m6qNiwYnP9M3byev+Vp%)Nt32=0+!QTI3=t45Vyqu`EH4u!Bhf<=dI00>hIEQ#l!|x;_a6{f}9o;0Cs)nhbXK'
        b'tx#-J7nKgp^6wM4<&Mf%7qC6uz3@gN*P~#v$=Wv6pjj7Npy)P!N(hCtc}HCCU%4o>Ntlh?G#A>)lpHzm`-vo(-JI(>8bxz?5f%9K'
        b'7!SAr(lQgD)G-?bs>UTV+hW0uNj8t<dG#NYHbKr-t4~!xW=j(n<HiDvS*acZI&F-}v7;NohICk%nz>lsdEv%OC!Uk@-BlbxzER8e'
        b'qu_znk|{Hwps*VFie;09Rn<51aj3Y+WC~ZBSR|{UbbrCt<n2>mf1;|L%1t;duhn0T_T~<SSF`IdvP$Wcrwsny#@gXTuH@t6s{!34'
        b';X5!k{}F?U#pIgHj$K4GOsBj=qbk{CU2S9fGHn;1h3#~skZM+30n+;|(rgzDJChrsewj1%6^0q50Bwg)52LE2Q%p`s&oS!Q)*{+4'
        b'8R<DGoX-t(<I`cWIjJ7R_6cmwd?Ow;ZFbPjYXqTkQSuchjIl$<%R;+~Y6M<2N|p?iL8v*!Zw29X8)~9-Sl9Trlw^yGs*aUG>2nzu'
        b'(jw`7CZ@o7sdZFolS{;w(knvp4If(MrScW?#nOzNwDkX+zuz?gD*Y%~;ANtV8@c#9Rm$XDvi{%H%W`r4wA>=PgCkp?@}?afX)G$)'
        b'E52dDw1Wsr@ot&oH7~HnEseLzdKt0;7*aO6DdXKGWE|@2kN8WqA)f9;0C&^05bxEtbi6gthSGGsFW;t1Roo{^WWgJtK=?XA9tdB('
        b'u4DoG*BER<CmlUMJJ{P@{A%5IH-#^e^M5vo&2-fV264#3iCq_ACMUgq_n$M7)r6pds?5ygHUYQ5WMN`+@)391nX(&jU50aqm`oew'
        b'vUR4=-6{FN2(P{PYE+piuZKDtlWRc*(Y-5H8fPv3Q#84<lywVben)n3A$Ryy-EYd^7P>#@fB+8SF~40dzdbGAE*8~W`H=$jJ(Wc$'
        b'Yf96z)8@e<wvL}T$dV2fwg9FlMJN>b))74cWm^b7>kZ5T8jUMGTLCXe)Gi;&dbQKbq~kNeFCAM>K%ztba~-mt*o;?QWY(ptc1J4M'
        b'dcZAI*|s}y3M5z6*WzZim1=@6xu@^~oE>zhbvmk_I68p~+4APZ@v_qi?ErOQHQi8O>$^AQ^fSS6!caZ91!oNXUAIrUl=;GC_noCt'
        b'R&`pMtzhvojS})gjiL!>c95EfhS){9%K9X|FU#(Q{$I%T;<~26x(USkv<y56*E{J_?%j&$>SPCD@v`0!FE)2|G_u`yy4CKI=Mg<I'
        b'gnZXnY%Z^zbMYeX(;ew=f!N6q-&ORtLFw;io!<S!fXj_|v;kd#_Yj$2K?fGk55fEo%`UC5$V!zB5AwReuA^PHxULYgZl)CM+O?RB'
        b'>I#?R2}@Hhap{gK-Y&L%%D33W;#7K6ffg?l2c!Zs^E0NL?3x9;LF}Xw+1A9YI`6UFe;7M@3itni^n$i+cv<wqM5}LO#^Q2;#)}lb'
        b'A+0Dbs%2`u!`3MpE+1v|U8$y~C0#MFAGmpKcQC`e)R^rraY2#EUD1KJ=OBXagY#{0Jq?97K`jQd>w<|T{{qgR{Vuv0z_%a*E(TnF'
        b'qSAbVha`;@%18c|01MFG5wPJdXUxv6`2`1lIRNrzn=5o{fn7036Y;(ZKj-pYaIrMOs`4XaJ6~FCP<}&+Z7nqkaXD^~`O6!E3E8nZ'
        b'X9H?nHnV*%STg8MgqAK~24)vQh{Zw21b0wp*I2R7M6lx=ptk_a^8@(VxFbh<(_4@)lC{zX28_c-wNaU#YC*g-R>b$1>zGfaxpXcn'
        b'UY5&FeZLf-9d^l9qu&-c=1=_hs9B`VYqJn)y2_E685!vr{`9mrT`a_R5rT&@9t$2}Hm1qW6gl4SPKr|w^Sg%P1a5(~tPyW!kW$~}'
        b'iHpml2fOm=FFiMP^4$sDf4+~RlMgl9y!+ZPYdZNstB&t-IN0qH+@$ckiXazemh~FH(@CEs)D`gi>bSk4tH8((Di)kNs_-UpyVJ~X'
        b'XIOPh?2Z6Y$`k{ge7NP*$w%&T3a7UW+^&F%EGew!vq0y6*+R!|UV3kG=mPF_$c^>8{eithRhLwkJ+;NID_-lu)8;0!kV{#gHBDwA'
        b'=+pFiJu%@e3E4shJ(pcB>7dsdtlq(vkJ<xSK$bR)U%bIyk<Ww_)xf*FU$qF%D=0RA)q>&zSgzLZ)S3ULz6?cZU=U}nTHjf(my2+A'
        b'Gj)tIYrv0&WY0wm%)_aDVD)WgdV4hR01^<lXT0HoXKZ{12S#?v7K^Nm(nGS~!#M05`2_6Jr&a`})TNK4NF_b=ZpQ6Hwl&4KB6PkZ'
        b'Bc1P@=hA05yv>(B$st@-zx2V)rO#)4UsV7JiB|^Y!~ejKXat|Ih{<MiO^Uq9*=B9Qdp<RF-d)5?oOO6Ni`igvCMmMYzk~u+ln%Mg'
        b'B~LW@e8Rhr$+<XS>zXXpEz>QRN0Xgc5Q8zB9U|~)>VGm37~y{^5g6llA`z6A-)V%mD&Bo=AFBk%P?nTK*(Nzj<s6)9&?8*Dp?>jZ'
        b'IjQy2|78(N?=;Kvuf(^d%=8TsD8%`8Fs9JS*~_eo3;abJ-ps1d;bs`F7`Rw-4o}9-(@qzi*DUkOc`2mC?x4pNzyVZ+q(6V7BPmxm'
        b'VEZ@~Rp7v|@=JsjT_Q~0dM;->&Lq`;gVwi~>?eF@&EkpL{dSUhki~D`I4BkWG7bxD@|v@3=^?31uEQwu6s?yLSpl&Z$*arn(bDVc'
        b'@-_?=4_tNxZx!k;w|A(!!v39(pRQD929y)LLlqEtQPb)IHj08;7M!isCvY!{mzm_U`#-vi_f>R38z9)aOYb^de$V3ayA<B}gWC`&'
        b'Eb-?Ibm{h6%6wmR;p;=8yi&^nMf`|M{-tfu5B8YBOAJ&)=)$IRy?|-Ig#GR}*!pCaCZQ))v_m?$O|_Z|Z2W22<!n!agKyB`+eqK('
        b'AeEW*CRY(ZOTw)+-YI@TMmdOfK3~>b>~wz@1hBV5a8;!pP(t@>xZx`gGgn}IhL$t%yIMR@7H&Lw`z4YD{7Co;RQ?GF`|-6bC=1bk'
        b'=O<nAZQf=d2jb5u+w4x4j-_L>-|3Ztz#b_)itp~pQk#bc9Lsq>Z^RXD)<+pI`n6rF9I#@bD(uyvL73r{mS%c52?LK?*p)fisGjn)'
        b'PMIBL8h@)#cR4GKe(cL~33kJ9uXRMyv*+pcI)fp@2*{YON8h|meKw$stW028U5?QJ80r8FS84^mhCB)bZ;Se7m^?XTCJB)0{?dRi'
        b'?D7gCFOYNn7C}5<Z(-I4?N4vNGSirvduC?t!9tE21C_#L8AHn%GBL!VTV%hjUKYoGSA8mu{ib?2j{TlGA)ft~`p@y~chsZt?6=Z0'
        b'XR+T;rzNo8OP@$!zm<L^k^N5knk4oc>7ORC-$(x|iTyVE?%C{j(J#zqzljb>X1|9%p3Hs=otnaa2i>2-egpkw3j6)@Pv)@SJ}2tf'
        b'w`cCwv2V}(MaRB9la$K7J>y7a-=6t%D*N_KL>l|%OmiCh=FCHB?3**jx$K)W&&*}toOyjN`{vArx$K)WIz9X5%uRas&6$2Z`{v96'
        b'J^SWNrGb5O=Eny1&6#Hn?3**68Q3>xt~Ii6&RlO~-!55ZWZy1X4H&;=c`x8}{6-F7{P5oyz!^xF9+HP&04)NX#c?*^R=_!c9|fEX'
        b'_#MF4<2cL<$;$)081Q`jtvTQu0Ow}lHvyrZ8SI-kn=;rpZ}w-fZ^qzn>TlwB1;_Y}n5miU8!!tp**9Qr$z<Pr=?A<PzqOIczLgT5'
        b'#l9`_<1F?~5FC#e_;}O-L%jy!ivhop9g<fMxc2&xyd{9|0lXCOhk%y>&dP)O0PY5S6W~wgLwx|xydfm-X27L@djQ)3uLZmxa3A29'
        b'1tEDG0k;9(1o#Nxy8+kbhvfYP@NIzK2fPFD2Y}xO{2}0P0RIE<LKE-{F#L}IhXI~c0DJ|w2=Fw(D*;ajd^_MxfKLJb1>iG)2LNAH'
        b'7?Sre;1a;Q0CxaB2>2-A7XkmcC?xMB;6DMzd4|08DY!?A*gP621NSYjE|7nZUs0hd_~s^6z;F1GCZZVXQ_SYp)^e6tQZbvG4{T!e'
        b'GN?I?u9&3@{s=6V^GB1az;&aq91W+r;d{_%IZfU7pb6n+xxNQYDF5VZAE&`S*{$=n8EK|gstPvOs0wyfGP*EM_W-9MmndgxVIWO7'
        b'Z_gus<z&zCm4o&EV?iKI1TW`hPJ?~_mS34jQ?@jaCX(kpx5QUYaY+yjubUh;POeXBNZuVY8SgAA_0eEIuH6{O2Lh+5zXDBn5Y2c_'
        b'(^Pu-e(R|WtlI?M?ygc_dmi`eHyn$EWr2M#k>_={AI*>aXfVGyL3|y>`+CriW@FI!eB;;GD*hc<%<I|9)D3AqstByxBp&`|>7{v8'
        b'a|s@u%=`Q6(#!LxC#ak$Jg<pmm+$N2L40r(r-?7~@mq!;J@&P$D3B(G^G|~x%}dt>j*n+iAkEdBroHUD&(o=#=Ep$O%lYj=zq%n!'
        b'_M$-fHjUH#@_W!s=QJ;r`DEg~<$-)X<?cY<nZaq^DZBJspzT=}SWYY-$C1m>U_bT*&7W(y42dcal=1ZYFJVl#+8)H$*K)p&1sY@d'
        b'rRQlrr;&MQCa1}~0!>j6jmX<m!TSpN=)cMX`=D%LARol>a()2m{u#^4=`RoLgR-D<;yKNBNcT9en}_$ov(cfn4=RFaW^tOQuRvoC'
        b'qDkO1$FD$B7etfD%le@FyU*<;Ud{-oK|b0R)CWeta<GqQ%iq9Rc<H%Kzr|A=*w@KimgZc6=48;^PT?}UVxeztFJBn6mIReEhtvFg'
        b'p^pz9S{T@#UkCB%b-dk=@^q1W&f#}Oo>|EFdRow&({Y;T7k>A?PUSRz{2nxEoaXcIK{J=rgf05dG&1jG^L~q4<dX-#C=2YjmxKB('
        b'htpiY$S2=|X$}R^<Z_xD{mN+ock3eG7#|3txt`N>UZI@d1kvPi9_?Lpd46jP;+^@toO>7f*15`{b^BP*oV$Ui+jWI<jui*4jSD!<'
        b'ul>q-Wl<nse-u==e4Z||;_~G@RuV{K;_G&4g|D2OuM5-<PL>4LZ8={vmv9>F>&l>Y;g7rzHa9bxn>fv_SD<+-h-L++x#J2n?*`GV'
        b'<TTr^K=WY`O%tE1dx7TNlvfuZ&9REWbwOC}TN|;zIylXrAl(<7CU`v!rdi8rJ_4Gd??}_jX-0tN?02Nu&1s@4ee-8FxYH`x_wzM='
        b'G&rV6^Ax8sR{GlGFXL60pm~AQn7;>29sk~1N9Dz9mdtPS%6v2!hW0bs85=8o^7{VDKpL_rkVoq|&6j?C@L*6mO{Ib5Ea5a0sxGaI'
        b'A@AI~F>r1#<uun_fo6LU%`#3?b_JRTf@qd=n${}cJngOuY)?;VU?1Q<0?PG+Re^o|^{+$nWc?ug?!a<ZaGE!&F0b=N1<~BhX+FCG'
        b'jSxhGdl}e<u<Faps=gpuh5H_;yUeWi^?@PSJ`L&v+#^AGeI3x;ruONh_zkc(X7KMuZwi#(8#zthC1_+F_GA#vCeGKFD<_z*k>+kr'
        b'Q(5if>+QD$$=-#5_S{c+zujEz)5UN<<aH>+S<ULU$xkQ8wC{78wGcl%li3S6Pmu?ZhVF9~`1%_CA99+_R~Vl&LHh?ooJSwM0*x4?'
        b'zx{)kbJTB4|5_c$JC6me+qh4K{dVRG{kCgiVBK&}i+*p?9H_t1Z(82Z@a~{>dm5*id<B|c1<~MM8S-e7`SLvaX%LUj;O)sXe|O%&'
        b'y*SLf%CDS}lt7-`6I3_cx5K;|&EH+;!#%!`E6jyU)$Jd=4_1GVa{kF_wtf$qk2uZa--G63PIK&g&^*lh`UAhdK4T7)y$M0GY8Nl('
        b'<{N!;PUaoQjclGK1=$O~;pMEp(Qkj}#-MV7^u&Xl=J6YSy79pq1NTEV2kD8pFN-$N-*3FUJP->5<-ti#GjgME&PCJ&uJxOP=9~;h'
        b'NY_@u!Z2NypC9YHpeC@5FHZKAf#XwM6R7Vj^YbG=T55c{9=6x!7mxC2wVxl`+Uw^>on)h*ALV|(pC9efoqm2C(>;EEw84Mv=f^&J'
        b'*{^+QH=gAF>tvnL&yV)ryMBJO<^JyHM?38k?!WrJ5l!Tqv-0edG}oUvetbUv0<Pb;YLA(4=afBXz<oR5^M%ACltS1`EDiV}UC-|x'
        b'UiAMy-Z!e_#s#kiw-+&^<$+>f*fGvGhwku&eHS;GNH?#E2Th=S+*6aFQ_gs!RTI5Jk$4XAIu`KssEq*bS@8Y8_=_}{2ll&|f1Vbl'
        b')m)U!?_<I<fu%J;`-ti*lyGN<s$dH|O+;I;0-iQ_T=4j(sV%N4H&uwWbv4DNO3_qUS6*LC>WV9>itB;`mlPM&Ru?Y1D7>IzadBOB'
        b'bzNCdxY=QA#{*{kxT;T9;@>no4bL#I#~G~KPhjo?zIRMRpHA?Hs~{d8#2*p%U|f_+TX5M1;~x?@0v&cI^inv?=GS0gqb9Jjp|g5^'
        b';*%}>!)rmGpkt@_#M;r-Zl!mS@#g$08@<r)B>daE$-eLGruh9HSkBVY^}pDA7r-W~yMO#7X?lUGMGE5mfdRHype;x%3p7cS(nv3{'
        b'Nx3L4O`DWvrb%p4D9W@j)H+d1=U!3StV}1{+=fm!=j9!9Y@_qWHuYuuxs7eQG3PdPUJ!8of4=9OC(n~h3vPS&`@R3yz_*`szn}A*'
        b'^E}`4{q}{zA*y*yWkMy!0g5WF&Z-g0IJaAGBqSw{NMS9+GQeiGcx#ops(84L-ku)LupH_Rl2lCcU1D*0nyVL;SCCk;Ao(ms1Y%D}'
        b'51ojvO{x}?@{%MYqv{n+5uPNO97`H2O4R_mtLib050cHSN0yuyLnqjR-}$9N*6W$-)qpyYI6RQ21wKNAOgv3m1BqJ`VH{dhj2WoK'
        b'<6SaGq($rr^F^8@B`kTHP7O9w3zob|o)KuaK9Cq4@|yixx=k@ww2vjLqw;%j@khj?kW$o)aOA^mhVlVf(U^|am|a5RxGig`%G8p?'
        b'DJglQ)lnx?DHB;GIJ>0&4tMH>vr{I_{MZspWU1D!LjDFZjF8Yce$84z05&rvlzMlC9C-{R1oILLw@^TToY*%M)qxA@kr$*85W#0^'
        b'sp&dL-sC6$C0TO}1QY&{lnbaU1sgLdQr+mtnpPZ%B?aAPBq;f7xO^qSW~*2@+YhfyurHKg^0JTG1NEy|{c2W!8LRhrm}HDezg{gD'
        b'7A`eiD^QmvVHY*$eim+Bnihr%DSem}q3hADQmXLWGNr4x+fOW*{s8A>Qp46~4Xm=)Yrz}b2*|IEB_$CsZ$k?cHzTwgp*^Z52Ih6I'
        b'WP+29`*ZCG$;Fj3Zz-XO5Uwu9ook6jh&oZ1tM=YdIKTr*87Rzkp_)QavdCviieVOMtGEy|73PdhP38Enn=O28(S=apUxEMQ1*u?8'
        b'o370`V`?03%Q76x6cUgx<;T<Y3SCPJo-oP;ah=P?@ER`#IWX7uM0;cLOb^l$yDW?IiIYSSRkEWN$~h-X_4Gwm1;mNGRWay{M5(8Y'
        b'M{!T5gdY8+3cppx8k{TC?g|qJV5)3DCAba)520L*EbXBuB~OHi6WGB#E%@t^Qoc#HH*>6PTGrx7KB;7jb%y<G#cDwp-`4i{F_If5'
        b'nk~u$20Lvh>*8k1WuRBSDBoSd{IdqL<?xpbb~>x~!cKZ!178v6(idU>7S6D3Ul#U6!fe@V$hBCd{Z`mpkbdA^gPrzeTanNEIDa1='
        b'*6bfg`~y1wbKWsq^1m$J&HMoIBZX#5(QfR0=zI$Ml=IA%Rmh+AFRvi{dvI&`infP23cFQj{{Z%dI(y>*v!z65XT7j5FxdIo2<Ck#'
        b'PvMtD`Dei131VLo{!y5RKyTkK>^oro9?0^5EHBJ2gKocH*ndG`K?Bl$q?dSjaMs@?(l1zNw$y`SGQH(6M?i(J)7i_7a8Hx|-1~%o'
        b'5BzQf?Yd8t|1&Uu1+-n-zXtPjAjcO)`28^d22?HWufaSOXVNv&p1a;`ITz%X_USO62kMgcdYHGqi#CyVKkNz6Bhuan^LEr}SlaJ~'
        b'{d=H|(!Lkw=TZKd3k`NUN4D)W*bl>P=0(E(AnfnMzI&kvKT754Lz<PcJTTXS-jMcXF#ACR3q=1HqJ08n->KQx!hS@i-vIY3VbA%Z'
        b'uqR;efqih7Xx}dM+dA0y>=fyL3TEv#4!@AuPVz!@5*Qoh;~~k=%4Hv4N%9@TTr_j9xLw-I1*VZ?GP-y^R}<3M6<XVcz&$}B5i7uN'
        b'geETqi3Mh!vTQCbEvmc~DGx}9S&65~r_53&x}Z&$4(CZh_;M3X*PfAeuhf1tPjK$ech2QI-1S|dun=z~gjxOfR8>;|G*8NPmEvUO'
        b'E#+WeOk8QEyAL70`=-THUZ>@cBUKPjP)Y*ix5?<5zA8hvdfoyx)nv~ly%r`-7o`f<%u=*KD8N&pWtlE9Q2|M!Pb?Jd2qp!!2wA17'
        b'h!=TtqLa(A(3fdpQp}^sg07xQA+aff4TZuPew#HVy#CS(g&`SA$S-*nMJLcRHKJQ`^CyeOwJ&k;H=LzfFRBs6>LCg59oYWFwYxW+'
        b'or+$T8{Y=5=OV__@~VyYhDDok@fRslAZ2@HNasn<QWK9*hD~W^Nz|BSnPrjUZR2>>l42-D@QiaI##}R}ENfDCjN<Gg>4I7hh?`bQ'
        b'$;|rFRK-;d`kJWXRAu^daLT~EAQ{@KbW6yXkuoo@2thpKL>aH~<;AR&K2Rm3DDkU${o-I6ivK%$#;sRgo}s&Zp8n!NTCME<K=LFl'
        b'<WbQ*z;^7u#GL`YR(Yk!B9hJ{HF-z@TCVxcw5Xt0gFR{Q7Sz0(U|yjL!|<rWFob#*Q9_*I=P`K$mM$N3hNJ7}iPuoOuMzK_XKobl'
        b'd3S6SJhZ2MO7ORT<x}Dvf8n)4N0{YW!Qb9{t>Ab6&9#Ehz56=x-uRa51fTnlt`mIj?_MYP+%N1GeD0s<7kut{n*^Wx1)Bt)`@&6v'
        b'&)vI8@VWPI5`6Ao+$8wie+-mQ71I0@=b|-9@HI&#k-~2IOz}%`-b#aTqqT;QDH1?R!a{`%$dtuem$0hTp-166-%y8kitg5ghjWQu'
        b'^B5`4lBXDT>Z#e$Q)6u;bhQx7A>}ae-clvoigXb!7+NRglldcBnUeByrF8NX?Rsjbsv=)yv2<^2NP>(eawzR)yVBhoCm9boE(HBt'
        b'^?Q$kHAP&*PnXSV)6Up*s8olYLN}D=_9V3j`nk0BU_d9KDP5+YXfU;<I{XnTvnm-Mk9DpEPm{$b9-XKf$@9Zn7m4?h_?vilG)gK0'
        b')l0PMBg9Yo1m`i?mq}@MB$`uf7`Q%WH89^;pxX4>g=aJ`<!-Z9I8_ujEi#mVTx$K{cvMrW(TJ5rCr6atKJp`{Ue31cXSMp=UmYz$'
        b'v5u=lO8?RWMIkvpNp&5nyap+>j^7qm?;&fWO#ieM3Z8|WJo(h60tlgrqK)}xg-5h&CwJkkouAdp2%Eei$J+~&jo;djCZuQ%A@lMC'
        b'`@T!GyTRICHN-C>$^`Vjk*IRPk_&_^)(Gtn<Me#$3blu*YHN9~>xJ)X(or>?9P`x6Uh)acm(J9Q##$rEW>ol9D<QpaZOX6`s|juT'
        b'_#0SS(z)O$e}qe#OApNDdH97~4NNkA^3O;@6YkX|N5uv%^G`~P60&|sh;k?28>bEQWI|fK{Sig#Ra4iHaZAZ1W@(Z6gO#te=>=^G'
        b'#)5vW(Z#Zv9;higb`nC}M{4fWukz)9Xe6opf{U0*mI|Z2n>I5^5fPezY1vVk?Gh&i330JPB(F}2XjHg){1Rjz-xy~V&(k9Zwl=wz'
        b'U9>>R|Kj3b<k~<YDEVHwLOu4-D5Ujs%x2&_|48&iZNSy!h?=M9*+|MEq8%4@SoAO?iRY2IBr7SXwLjmUP>GUVEheVE)kq=*Y3JyT'
        b'XKT_AldXK6C^Bx1@Wowg?#$t|Y~g}=6{?1#Y+7Jdg&q7YwA}e?4?2AW{slr@9+bmFeZcWSPy0V@awi}3$vGv`Ql(POV?vb@-<Nd?'
        b'eNh>six*5C1za4o?jAGgG!TNLw9PT!8}thCqe5v^O4kUfMztOfUw!o#-Gu~MH*aF~@qO7UDO!&n%<4yhFqa^~_X$GS;5?o9-{b>{'
        b'#8jkJtvOX4LrS$W)jA|~GLWt{ZEe>dI&9wB#oCuEY8cs-bUNgcHB&tKENWa-p*B2USE#4Mp^ik_7F^+b@Z?rRuO?F`pKD&a3S)6#'
        b'ou_Jt)`og&OQ_!J$Wz4ym#I1`HmGk8c&pGcR(@*~qe~OwpYrk{DI1@Q)hF?gi7vDfwyE8*L{i*!Vtq9Ij3dM$Cq)(VkASQ;eXZho'
        b'$X6q+k>p0QGsLeJcVp_x^M_liGD@i%-8k<eg(UKHp|v3i(~Z*ymPkk(H}pfE67T2<ape@^g|DWkipr=S>1gA@i-NLo5fpOD@nen>'
        b'C25rWC5EnOy;52epU<JBbbS77Nu;}_@SSXyJb9bNndaP2i!;ropB87Dn?5bhG(Y^bIMW!nh%-&o7ICI|Xp1=0{Ar6g)6BkJoM~d$'
        b'i!;r)uNP;U!`F*5P4x}pOtawzai;mk4dP7m!VTg~^Q#-gndZ$K#F^%T8^xLClQ)XHyLa6v?(RN!qqw^}c|hFVtsW3}cW)mMcXuBi'
        b'5O;TfHz4lr7T+Z9?%Hn>cXw~SN!;E2;Z5T1?xCB+-Cgr%#NFMR&xpIb?Vk~Mcfa`=ad-FlXT;szqMOCt-TIrw-QC-67I$~|+$`?y'
        b'{`_WfclS>>i@Uoswu-yE79i<0?*&%Sd)=+#F7J1@io3jY#-qEuFK-ohdEeP8?($aMBJT3G-y-hv-gS$(%lqwH#9iJOfsMrP0&F6#'
        b'kz37{X1b3C^b#LE@B`v^0Is0-+rX8;Pv1)Vl+kWLp`^W1Dr;W=?Dl^$+CvzM5OPg}KCue>_{T9{2gy~28^0;fe5#Bx=JU66c_IiB'
        b'(qyocg^Nz}aiL*8u9eD%C_W)@SntvkT*sthL@{TXk4CajN)ho%0ja(oAAgo=4$*MHcQy0L;qL2+b<47<E*<f>bP0X(%49*M6MrQ5'
        b'0wM7YIK@#s^V1TGMsx|UM@!(K&3v8VXf!|`c!KznG7Nm3saAi$AEU|7-K8%HnqgFE-h{qB0UHEdEx<3JT|kF`UIFU_pd|8v!COtU'
        b'#c0(-3Drlp^iEn;f0B>q3kOM#i;us8^@&gM!cwW)D0ZB`Jy2c5dM1J~AD0fHdI<{`03!O5f2a46@@>?<Cx|`>c1L?Q(0Vke@r4~2'
        b')O5EW9Mp8T|9()@-M)UCrn~)bgPQL4ql236cH=fpcYEPBO?Ug$ZJO@(k8RU*w^wY_bhp=T({#7DY}0hNw{6pOw|8&Tbhlr-P1D_e'
        b'%Qj7S`#sw<-R%!;({#7*-6qyO`u%*Hrn~)(ZJO@(Bil6H?KwkY9pt>VLt-tY-=rb29`gHlLt;&&U-^(&7y12|A+a{{J4QodeWc$d'
        b'Lt>5Od{IMUo#g!ULt?Gu-=VgN^^$&FLt@S3{6s@y-K5{TA+dJS?^8o!{p9>uLt+i3-_1i}9i?CMkXTFk-Gd>qo^sy!A+e@%PQ4+q'
        b'uF~(yA+fe{e$XMYzS3{QkXU0mciE6wXX$t2kXUQ!ck7T?Z|S#VNUXW^dvHjsyYzcvNUXi|dv-{yzkD1Hi8Yw>YY&Nan2)z1u@-YS'
        b'tIvw{nBVLDtdOt3?@xYK$XMWa+deDgEbu!~pB1te==X!k&rN>hKMnThCqF;A?+Jsww78-;@sz>7q}W+p0$f(yT>K>Pvf|5%XFh4L'
        b'UtZi%Tn!8q2a5B7!Qx2qKH!Gp%^Ytj{tu4#7Jr4~qs9NpaisXC9DiB-dya1wALVGCa_SVqGp3v|Wf1vKn=)<6eZVuPOrP=?aK@Aw'
        b'Q{D!aO<6c)0OkDklwVItAp9sZ7)_(}E3@_XDXRP!SF_lmaM3aI(p=S-465t=W<?h|!&w#JN9l|2>D2dF6!PydTN1$YfMn<INAJ+x'
        b'^O&E?&%fiR27CU?2K%0u#COz$jI&%9r>%VaIO;v`4jIQ?&fFEuUCG=Fn0p~}U&P#tn7fL(tC{;^c#${!D-fUpAu1500%0l;r~;uX'
        b'5Uc{>DiN-d(m}Y&1<YB_oE6Mj$(%4RWX_A2a}je^vH5I%5a%`0prd2`a~N{$4InRQ0JH`aki3Fni3#8!`TxPd(F@!N+%Elh|6bJ3'
        b'`}<TLWGOV7`GTEsAMKi@dgO436zsyS%O9TC!GiJFf=Zv>k%c?sbC-5>uARG7Xfwt_uS{Q}l&2*yAK{RI7Meb?=|XEB9V90AL_V{W'
        b'Z22xZsqk9PY2o<^JTts586IKb9QgSnvGtWD<$ay<r_5JMvZXY)a?ZliQqn1%%{L=+aZXLIICdIW`n!_VTsofTETx(kQ<*(mDd`PG'
        b'60t;&FHxE;yp*#wOIeuS5)o{TeDr<*<*vNwBApMNS&}{#3#%4ZFIcp&N*BPNKz=enML7n#=7sH+pEv|n@2o9?jT8Ct(qQu-dP+3y'
        b'TJdHYj-^~V*~X1Zv?qoWWL#NFF=oXV&k8K&N2tY0ZM3JSH^vX6A>#N8kqBnxn)1F`ePs&${nV`Z1U4#v^X9R5OtB~nSd4eKED~HY'
        b'dWd8tGvSL?E1{zKgjb?;Ze=NzYW%qLZS6vZch*>qkXne$Y${4qE89deoO?*lc~I4;GOL&BCqe~+?Y(Ok^KWk=MYIGp0fi``9!0-$'
        b'W}?|jL!HOh>|5E=+|;nTlycTPFnTQ$O3b4gj5DJ|rX-7OvEu2)Mqgw~Im$QN9dxqqjgXRa+8$Cl&`U^-3!<j+9fLh3q1L3}=XeZ@'
        b'N=8qn)YQp85pwoKEr0$#cU?-uq$e#tE$Sj=q}&ors%6lZK$*LA{1VlL`h;q+bwT->pl6Jf@VBdP0wplL1g#bG^H)Nc%``J)hd5hW'
        b'd`->HCU0rhT*Rz6sRCgM@0^<@{6A2kPJQO_u_`rYBAMZ};BuI|<ktsPX7;*SUA^-_83FZQEs|?l$*f)sty#UL;|5PIa3>c$x!jE%'
        b'TrIU2g<^<PXe{z44$fy)w$N$|^4G_zVimDMQtOphYeYkdmXGc*4z9jXoL)YO6_vY`DJAhlPj5#;Nd}rzO3hH3eQ{`Uq%97@;lt;F'
        b'DPGE#c^G^Yfm?V7s1HYBO9aDV&DP^zkE9|bZc`T|!-a%xrbMFEM(3YqMF84J=p0gPT&sj;rP5;QOO~Eqk>FI!?d|k7Bhr!d;~)5X'
        b'WNdQKX1-WYMY3_6r-`$g&mJ|Q&TwzMOSRB4tD1v7eqD+pR%(I>l&k`M(G+K_qHmwOPl<f|!SbKa9<;r(?(IvjymFQQ;YQ0<X1DU`'
        b'$Nud2>}iJ&eeva&w|>+A%<iWHcfa`4pWV>++X=(xy!F&m4SXwC=aK3H#M|cSB&I~3<1aMYpPgg0KL*+XS_9ewih(Sk640Siqy2E1'
        b'(OzFB%)3Evlpr4LgTR>}23j-QXnzv49n=Mib!~|A*FrQ8JZ_h-uEFN1_tn~J>z$SE`qds^oz2z2=DQqq^QkYQ5#qI-?~lcNy)n8y'
        b'G9O!4Ule<fXpHuucz__Grq+fArh2RmCVcW!gpZV7@)y;tI~ou9!odhVsuxsdWI$J5!cl*K-i?SgVSc=)L+^~a6YoNf-Ix=)gt)bR'
        b'Ln7#l^mdcmLY5xMCqIMx<i`+>C=z;_K7**`KglA60-Y&dU49g*CzueA>{Or1ixy#+M?x5SnI5!*W1%Pp*IFt=Npg#swKU>O!2Gqb'
        b'P!#zQ_{7&L*69yp1dkCOBdY`9`Poc;7esEDhuB7SuJt9NzO~_KyFW}WB<MR7>%xx9?QC(m>wS&Qj@AaJuhF(@tPDg9Uq_;c&Nb53'
        b'9S!vInNM#YQ{ANa_cT{2O*If&7b1ov>_RK)Nv+z^t)vQJ5lbrr9=h}SQ7XP*ekjrr?hORF8@(~@@rA?lx|nLjGM4bk^mMYD%)0xW'
        b'*v5}J7-(>JtxpaF7<({!qTS*wM{8MFx?s0avMwOk`q?X-wGOAJ7Sqh<skgN_9i_8pXZLPuZjvENPn0`GN{^4el~C8l*9DTLhM5<K'
        b'2T)r&=|G!W7K;1U1v}6b!FY#Hd<tR27bhG#qZppi-kuI|e!!4+dfdL|<tHi;|D*OqPoje_lvFr0dX&CwVv6EO+>3$Q5$nZ687cSC'
        b'+lpnu1P&NMm!l+mtwXU6KI^2JR-9PJtN^30_DCZZ@V2x%$qh%G_?1is6YDgUgNAuu0;8KG-P6)k!k@P--df)(udTsX*W$d?x3Ii1'
        b'Yv$rzx~N<{+L5dv66JF~&RB7v_yP(_`KS*E{{Ho_p-s#;V_Uj?9UdeptxH3FMqQHs6bnL#YtceL&W{!i2WN~|Kvm032OBS0E;c<T'
        b'KI$rB-c6su#0n|bFWK1vT3dR8YK0tYjrQtmtE{b&D<jeM5te7b&q3QJjn|NPxZ+Wq0hov1+T)yItbV<nRDKHuX>6rG(a|N$6*?AV'
        b'y?eRd-QMD~E$3Q}d!(gFwej3t5i&ON*WgN^w>u_|W6Z@5ed6=Bc0(<NSyFr-EEDW{{8OPn5a^-Lk^I;~d&N+k(kcO!o-#pAGe%nu'
        b'G~Yj)tm9u;M906jXe((uCzKoNKBD#{zsd$gcIYReE^fURo|FmEa6)@EHnu7lrsx>Ksh2e=e}}3%o2x~V<v|(fVJNkmcK3>ON*S#a'
        b'3e#o>_4r~Y7{ev!11ahCv~X5|U|(V}%Hed^Rw(!_=E*9sR;F4Pq*@myt?pWd|Crk&4YqRCP@x(sRl@?+uuwHzq#72fhAP!itr{*)'
        b'CRnZ-DpW(IYFMBe7ODo3H1pV6gu%J0w$|3_agt$$&EaTa4R+@;?$zLIatK3hb8C}Vq3;wsA2eIO3VH<e6zGSb7eEI<zX81t`Wxst'
        b'$ow_4<y6oaAO%zkssw!;<N!5-R)Bn<F3?pVXL3=XzUhsKeHP~);0uUcD`1sAN+5MHVUB1oy-3g;w4hf8dm_QG&Z{;mRj?DYY0{Oe'
        b'cB1!I%KAVesk#+Ks&%)PkLz2(YWV<9s$*}b3uav9m?A#8@gYcR1NiU_2AC^Mib}$+h&Y;2{+<nS`YOnDZgoK{b55>Jq5%_?II4rv'
        b'N}moZl7-@`mOK2slvoNKeA8mza9OY?ic!g#Sm?(5I!vLp$UT{uEgV`Kp^wKRSGU848I_iy+g0blzEil0V6M9C;WSqY=WVbPk8{$D'
        b'Ngb*WiL7|dk|h$!N;j30QcGD)D8+$N>k1`w`6p8&CtW(yH)*epl{-l6d#pl0rGNzj77DmXz#;)v4k3^I9gNkSubVCBf#!oQ0kwgy'
        b'1?>Pm2RaBk1o}JZly8_V=YnQ}szFxJa?tm83Hk)gQPB0EJ3wCpeFrom!@QykOY|n}#@(1(yM=uY@Z#N?zYAtJXeH<qpdcs=ii55O'
        b'oigE+33jZz^eI2Mm@TF?jK8s1wO9aCHd^M^Hn+62y1h<^v^9BMO|5h#82bmlIc6maz206>=}Rc3N{lw&o%9HqyVPHivFo5cWKSX*'
        b'7n>rwavS$^Gkuew&mAO7<V3qyu~DZT6>$S_cD*k8Miq?HqXPR7vHJ+nD`3r$E+{uN*Dj|$8<*u#GKL@D;gwLb>Wff1nw2uWiv=xJ'
        b'SI3x|6G8}YtWR`6NDo_4Ue4ysnd59}X>I{3He#a0BTv2dz%OcH2Z{$&lIK`ukfvASqMG!^B1rEWk`De3&JM+5d^hY8x4S}d?4SIi'
        b'F?GLsNpAW^YDgt<zBAxVV`TZvBzhO+@nM1E`?wPHe4T5VkG6PTn`gOirNis<x*DC$tzMs}OyQ@<($si(BA1YAI$!x%9u=jGzD}KB'
        b'n9v`2=%zDbpSRX7ZjE?@*tDsKmslUKbQYg=wpc7I8OU&8pj$0HUX(>_{nEW%D45Qd%BLL;<W^ark6vrYmjTIB5<gd!IK3X9XSIhK'
        b's0HoSvdrl%_c<NQoIY2Rx5ejaZf&V`Di<pJG*iYm&fKG}!M4ojYOysc8x_tGQl{Wh;0<+L>5BK%^Jf?~VY6xD&JU(It(Nghma-E!'
        b'A&=ETXODF>T0BA2gf|A-?$X|1Z_q=hDbB?Xw=w(VDhkRwA|uk=rM-QP;-*l1r9UJj9VlZ2Y!FIXq%Z3gC|s4LN{P~H$5{7nhz0q|'
        b'QZ9NJHQ?d+JCBleQB1x$r5Iq-OAsU0D?HWfMyX+t2z`uGdiz{B_IT9qByb)h`jQhxpRPvlQ&XdzaI~{T;ptGhS+@MJFp;yq!jzXH'
        b'8ww#^5&H(x6+B-byObxFkp;$4W<>flm*Fa_xsFowMnyYjucYi1>L-0|GdiVJYrQ^fr8XpWD)Rc2C@G;Um2BzD20-c+y2NM-Vm5kc'
        b'<AkGT4|RP|oW3*CE!WcRqq!3IMrrhE-IL5M)=^K#*R*kg?$F9Jug??g_Q$%gvd`;l?8Ql-J{qRCNK5{~NNQDT1zQ-|#7r)sg7LsC'
        b'TXXXlf}+FHihrUm8?!VS^MS^bjHk9djSqP#uXK!@ba75{fb_W{T|xTF80iQ$tEadzx>6mavJn4@@wtu%c5s12OvIEopXz#|-8l0x'
        b'b%~PA=Jj8h7Es!jWyIk+g+d*kU?iY=#Cp~>MH8XU4VkNIMjYuv8S<V&cD+6E)C{wGh%{>XRf248VzEs1X%Vkf=@B~i0#8r7xca0;'
        b'3wMZ=NQ<vHS|qg2qpe@HI=LC&h1Aj&)fII7Msz$yOJaNmi0+hOI+9`dLtBK>J-;z7`^1aArAs&qg|u13hkey^$&wOmuBz(9Pbtl^'
        b'5Tguy85ZviElMRue4qM^7xVCP?srAT>|kO#&|u>lkb?n=(?Hid`M4KaqMJKi{6@}_ETa!plR3s|nOi*8DuyahF6z1$(7mRN^*M=?'
        b'oeBVRYouMU)l*-hiSZzB?&W=}t$_UD(-d5f<50AR^lDp>Y2`&)HrZC#>0?aG4;6urhNfU2U+!d4sfctu;3cf(JQ#e4@hbMI%VVwm'
        b'^7L1`S0sm`Sj~d*`d~O9BTqkJWGoSpK(J3f6f8=G<|3vkcjMJlU6L7wxjhsN@N@I!N_xyIsPNa8w>I#>GMmN<kEnGOjSgyXtlsOA'
        b'>p;fRI`(X&oh3HR{HcoFTn|@D>QhfaYB0V<jr%&Zpg0rJ4ONDPBhlLv5xq3Gf}Vyw>!_~kplBft>TI3pUA{_)y6Km?-f)IDUm{Zy'
        b'!nrskmU$bg0F<}KMZ;!>5$=4ksEhWf!<Rd@1c?)Y^412t$SI7YYI7v%N~#!1nJ*6VS^XKciih)C*N4`2A+%Z!KF1o}?EWl2UIv%S'
        b'N>76|IrdW*4wSpr-Kv(Ebdh3x6eaP{0U<e4Qrig+1mVC}73vQ0Wa1M!X=(5z1M#O8Z!O)z?hZvFnEX*1=ZtTBu#<PAWupOCgs%ad'
        b'IcuDe#g7oQ(0jXk6wkU2b*M0r7Fp?l%(n>K1;cvGTw?3EmwLW(Ib<s8BT0NarTS^7RIE(${L!<{E#AVZ7m{mL?Yx?ovoA(Bf08jg'
        b'{L&Y<QeVeqhN6v<hdfQJr9ns8>{-NMrr5KgN=6-Jv!5tGLz-;gZ1Kk`UtU@|>G91UGCkvmw42iEkS<s>CoP|xwDOwM%3@0M&pAQ+'
        b'<fOH&IW0adp!8)N=lDRV$KUM>;7@Yt4e+CU<}B$7`eXc$ufxw-6;6;0wsP1oh}4wX%7Rj{e=i{qot;utUrg{1Y&0A343&3Z`Dd(P'
        b'kG%UAC*{&ShM(Sf&&Z4oXa2sS^h7b~rcRP+HCZiw^(5M%bC3z@T=-|-i~zoNdJmQ9EJZ8me7aLTsMW+v65<`;4M|^aG9m~El{>TE'
        b'X><ELuFJCX5~TK(`tg`MgaVw!HPYMdBYRwPU7~mOG`KuopR>{JU0pI;{X|4pgvhs)M~eIWJw5&n$+t?W`7t#Tk3#PvgFRTrE)QKX'
        b'PYekZLhndB|E$&EuWQ7I0w10Z=u2O3A{35`FUB%HPW%;W!b_Em%$VR|Lf89LKcD#M5SOx~rHU9sQm(kQ%1Vk^l5@9zUk&S*bG;va'
        b'jQI2oa_(2d{$ri}V%VS2*%!n9tj_*%*q_tcNyX*!HAQ!*YsnI8(H+m%9PSeHwdjr|@PC2lpZpy>t&J38srQRKUR&+*`HmJ_BXi8B'
        b'_hlr1lAx)%$>(Ua`M6h$x0Zl-H1?S-IYo?3$k(MwZf?dV=4%Va#C?K?s&E?G!Yayh3fxTjscYKl6s}m4?ak%z%RG#_u(K%~>Y;b<'
        b'N`G~gJ`N(m_2E$ae6Ds`z86oK^sNyo#*52w;ofweeMa)Am(ZR0X<ORGPZnt#PRYJRuE}Gs*w*+GIAq7=n@wLge?f7wp?lO*s*Fdg'
        b'rl=3U&LAfXKmKtCUnCm2n!Zfw-*5ZYicJI4zvE6iig<z%FtRSG8ka51$+4GjGTJS`!~H;*^FeDs3aB3L-W*M)a~sUt;oj}`uMN@;'
        b'Vjg{kE-9Udh1e6kN}TRWNP;BUq8V>kk+)zF;~XYriy<NGTJX1LUPmm(D<ACX!GQ?Aix*Qqjlz5JV*1!#BAq3Z+nloGmlVxZ$`axD'
        b'n0!T&A45fI8h_X)Z;{XuKAXEwItl^J0satZ7vBqV23cD^s1Q^HDh5phodZ%pGeISwGEg~aA*dQ;0a-x~P(7#t<OX>`t3c`Ev%_$U'
        b'ffArT&_+-{XbWfnv=uZ6x*fC~v;#B@x(~Dq^dM+A=n>FkpeI3lKzl(hsiTeV4P8p|5Akb}=#l7^NWbyIY}rC(&*%CnnYg5vFH~G&'
        b'W$2g6taSSp^{(H*Nyank;_*A;CmAnC7mv~yJjr<Zx_E@QpJcouT|CNr`$@)Abn$3kw&Nt@S#|NaKA@9~*RP95`{MgfG9FpgcobmQ'
        b'$;LBk@#tRbgC`p=M~g>yV0WKvynHPl-IsmjWaAZS@#y*g*vZCIw0Lw6_sNruXVv1-o!vbr8?RrBNB4X8o@_kW)p#^k_nmY+V=^9v'
        b'efFf|<s{?LI<x<z<K-vg(S76>PdZ*vG9GO^4xDs6B^hsu?p$Ql=`GRou;$BgJVB1HLfP-9%Kj*l?R2^<f3Zw=^xycSvQ^6RU6h4i'
        b'ARY_J=W>#LoO7C!V76$F_Ptp3OyNLJy861Y%Sm(M%>F(ujU~;8bFtCgg*12moXvC=cOEi>ra56FlI9W#_R;QMa9u`YVv{xI?m%k^'
        b'ad%QZNF+bTb0!2|DDI2<BSD`Cq%tm*l<G6;i1pIuZ*B#PCc1FSNwVQqB$;Mu8&RV3rSH^g0VoM^Yp%05(ov?U`%py}UVa+Ty}ISR'
        b'9OR{O{iYU)O)nYmLm_|rS6lBSCUm-}<@Mp*(BgGEXd5k(oX%N0v~mhga$iVgrizPJ!Qn3w@FfeYiy)ipL&TsRu(;bB=Yx!I8`1rp'
        b'9gzf%aN-*=edOSbi*(zBv#2!J`WhQseQq0PA`llZN+@dla{3#IUQwFmWuG<#MCOzsF;-{IncfZXuPrlF{z<Xz=aNU|3BVtwflBg@'
        b'kwA=29a_!0xuf1e%_Po3Q91$>qeCOz8*w%J991VQZ8Z7jrJKCyYDg%`&O2W@_v~|KO`q|xnc*N!9OBWSYo5W#I4N>Id!DL47NTQS'
        b'T2$giXzz`y#|<$TMFcUsgOQG&4Y5R~kIpVv2!7VaDJR4^MM$PSfB7?Z;dB!v&Zh|RmQX*%LKT{aI5uqv(Z`Q?q9@YP9V@}v11+5B'
        b'DkFC9xl74NhyTt{U#1J)dnwIc6a*zgmI<tHanh~8lV$TU<>v>2>*h;Na;Z=1UL!w8bxGvM>0F$zV7KVpPFh2ejI$m1U|ReGupb8H'
        b'?=;%a*_rCMaA#&-dl6P+_)N}AWmbS#G-)B56_`GOH99V0o_bpa{UNHXT*%>~MFb0~x$UBgN)|jI<d<0ST>ZoWA=jiF=9LG8yb}e_'
        b'TK54V2jv`?mmLuDQHo)%Js{+!6j@oy>x_To_kTP7Kl?LiKa;_bXEGZMMx)VW%E>XCa!fg9rl`LX`Y9Q|fuhu3PVy%mZ2V`)@)Q1c'
        b'{xfFzk*~u3cl^$mdZ;gxx_<8<-Eg!QCHX3}zrzNx9MohGVb76q&P&6w+&*mhb3a7*7N@hxtB5zmO1!s2hz(@(xn`F*zg$N`g5xCe'
        b'Xl~Q8`SZAkWHg;CFW}4#hC9VO8}Xt|ecu*p@0c(2!Vn~)#3@HIc7ANM-}fV<{mY=7eMY+z_FB*zBSw1>@VRG<_KV^EAn<d~2)jz;'
        b'J{Em0&Hw3VGTqPLH+~vKYCh#Me0u)b(xAM~*X60tUmu>#mxG2t7Sy)~^f2hBu-7B}Uw<s{Y)NFk<2j?<{TD&^>&!%co&75?Klr>b'
        b'KLGr;G{61=*87tneY)xN=NAQT*>ALe@+ZQsQhM0({hImkuT%XTugY@2rnx<JX#Bj>^Y2Z||03zOPUd^5#HFto?Z=S+n%`-Dl>Z#G'
        b'Q&^Y(4`u%3UY_<#Uou@ybu1L=WKFgv7V$?|c}3-dg%>TVs=nCY-Vq3P>KttLT8Fcac`swj8og{*Mfv4(FD##Xv2E^U{<&9QF)PBI'
        b'G+QIx_m9le{blnxEY|&H51UN(gUn=q4P-T#?3-Y}4paha02P=`_FlLj$}!o0k|XRYk^5LgVfFUE=VZEHZWuoeA~m0|44<BVwlpZO'
        b'%XN9`^Vf$b^Bth)L48J({p+B=fKCN%LHG-E1g?}s<_Gdj_O22^kLt`sSLy7J!~A5vFn=5PBWXTbV6w9bCnkNm>0~%f;C~?8)f0tX'
        b'rSz~?U0V5PrTSfVp1=*~Yi=*i7(egy{I5^T-znV&WWIiho~b7LWaOVXSM#I%7o(lF=<@%S%%9v(ICmm+_d2nGHTj$VrB9dunFEO^'
        b'-Tb!ycRtE^M%~!^cZesMc-KSn>prFG^1bQ69S{F>hh@P7yI%U(yRM6uJn**TgVXM>{QMnTU&w#_@>#Xf2LmO!`zEmdgH;>8Z>v2c'
        b'Vt(||$39#4&igfgG&NT@R-Rk_e*OB*ms!3WzwVdKQ+h?Jhowxfner{vYJt|<1P**(;3to8?B6oaM!5g<4vt&?>kf{==bj@}e8YT?'
        b'e`sBO72(d?&*}zRU)xc>6F7L@-X~uME}Z?&m4&rxIoa@m>sKyZSIhP_t?mBaS8LglZEdfv`c18M>!W?=eq)Nm{ny{V{OVcD9YZfQ'
        b'=Du*a-|_Axzxk1I?xT)JKL7I#wSBKUT3Su^{uYci&_U32*v|*;^P22$fWExKWS`=}SOZ?QLfBOz_p#`zH2*KG$aFu}GJYCFYCeTB'
        b'e0u)b(xAM^{R=BH^Vf$ba}_WGnufYIfo=tT9rl?B|4ggE_gV#!xns4-UL6;d(3y$m>g*d}?!Qc!uL0gB&ELBmYuHJUKHagXX^qK#'
        b'_7x`=mgu%Xs{Ndhz@krTZr|!Y`Sd9N*=hM3rJHq)u%9RKw{0f-UC7_srTJ0*Z>>TdbotMeZAk7XTDRy`c#ir`Tz=rsQw>QMl@G_L'
        b'1vclJRYO|feC_RZ+L_KcF=wJV*Dx_@m^je{!$kf|8pO|>50{B~Fcqj?6UapkEPf`{Azwf;uly7I^6=ltAvZ5S&z!FvIAwsGe12FY'
        b'qls+XMHuw{IE=!d4EZpVvnl`oh2I3uKVd?@nOQE&LthlI32Y)OWT&uG*=hXU{Nta;Ug|EB{m-EKyG{0+V80Pm4)TH~-D9$U3hsx$'
        b'V6y-G3&O4vxsOE@R&UR}C)2&-?(x$gQu9g3@ag$yOM~+2(B-MmUmu>#_kdmo_3yx(1-%QJ3fhWtF8G2#pCmGW^Iq%+o)ENGXD0fT'
        b'&OQS3{++`74DeUdJn24@{fv_!eY#`O7ZC2s`%f+`(f@fc&Fvw9YaZ6z{{HC6r$_m(OUu7Sx(&)YL?l*x*<}Ac^542!^P~LjXs5Nh'
        b'{1dVb$^As@mb=;GBKg?0CwPDHKixm@1CxFC_e}h~<%>TzTXrusTY_hum{Pxj(K>DO)Vf^b<a8qc)K`PAyzmntig(YH8lf|OPYpY5'
        b'1mv=^Xa2(qvz2*{!93N*{yg6XcN?o{w=vH(Hn#XPHiWUUHD83^H*D<MC*eP0W5X{Y%x`V%>AxV{F&lde^<F%|&OTjaM>=*^e6F3X'
        b'`Iw#EUus91cD87don33Ovme>*NZ-B_#d)7(r-LFS3!mhP$Zw7$$M`tOaR-rn^`Fq4Y<edQ`XyBZ^nXY$59o8CJBjm5_Rk=-4(RWa'
        b'M})S=UnQCNB$Jrr1Cw4(lKD=%SeZA;8m3MohO(a$OPc&{N-a!skzbeJPN^J2@;%t!<@>EaN&7>x+z*hPc-qv0Hp}mr@5pqXkagSw'
        b'`Xlj7kc@xgC8O{CARo!RmgOf|$lFMUy);uhd8GMm8F!0}b2I2E*`6ix9U#3^J0jl!j>`JeCSbe#-uqYjzAC@@-Ynl4a=mIYF5x0s'
        b'o)=_aJR{qI+K%Mn*O44-P$%dMvMkhABv-mu#(A7{v&nXPjdT)#u8~ZNd9pt5kxXoQ2PoT@(jcCtV=~Q$WSMRudDe2TvO<36E|=vv'
        b'F4MhI_V-~~?kDAE^t)ucEt38AWzuUP+nC0~CrB1L=xmvOP>!qXWf|yu_%MAJk)Pmik?ndwPBI!haardIIev2Gc&4)cSo-e*jS!C-'
        b'=(n=WG@iH0vI~C9!)TUYRN+Xp0KJT%<Gzrwr;+sj8I0{kQ~VIcbexeR+mQO?x54={uDkGROWvB|1+%}j$@0`Qhp!&Ui%I)7OY;+c'
        b'^V$c0Su<^}!+UJ{A8YP@chgTN#{Vkq?^8D}r!Mv+F4lx)P}$xzTlzt8Z}$fTe=nD*4!7-~!8bJ-^IRVIYghw8N<j`M$M5lc&CjvV'
        b'1ik_HoC1wc?-97|`+a8EC;xzF3Ml6fVl9o6c7g<H#G5CSSYOV;7YbZ4rZ}`fHyy%xIQmi+>Y<ORp&lNG%c`9{Tj<4N6jb9+<Oz#U'
        b'OsPIRw%!9Lavv$)i3G#6U;e6@8NP_E>D{2)^O)h5JZ8KlpBej&%+P0I?cpoA3|-2X%ofF2*XnWl><!Daaz1mJSV;+2+{VB1hY}l5'
        b'FXC?|@o<(UN(tv$5c~+lZ!NyY$1g`FoEce}tBe;yFv%<P)oXPccVas!k>G+3grGH&lO+TQrx!>vLj>1m@scuFSXqp<SwRlaD$p8G'
        b'A7~?JJ7@>!G0>Bs1E5zxM?l9x)2?D|=YXm~7SJlt8c-jI3tnLK^_j~jB!iIM>T7g1Catcf6}ASK!)I$*mf<GUk7u~LE_3Qq^ZM$V'
        b'TbmpyE}m95DJ^$uu2O75Mq({+Xm0Xk=2F{Io8h*?+2V0EH)Xgt+G<k^<Z5zx>UFs{t?>BlHeD{{Kp_#(>p~irr3KDXEx3ADyPdv9'
        b'm#5L@t*uY-X>r;dJ}!wgJr!qDbL+BtpT}*hP0d~{e3Pv)yGOmPiSDwcX4BZb!pZwHt-#Bjt9{<)W?w^d)3Ou~&O1>@oHE(+NbO<0'
        b'PlK~*nYTWzI$Tx=Ptud(gD9=evGQ;6j?tV=&XsDHX7OF+^`P-;Te8)b{2b1){c7u$jpvoUI6SlLqgS@@_+v&&jp1EEwNCSF@;aNm'
        b'K8LHW4pmO^BLUaTc=oH^Uj6uPZE&X!TXNtxLa3?ju4O46$)0P*SmYwD^uCT(cY~`Iz3pqT*_{n3erO3N=8V&k#n0YiYpSjHk;s$g'
        b'Iv*^{wBj^-ZK>rW2dcV@szG(GL!RCgZ;!LVSxb#r*Q}N}#h<%SG1K~w$8EGVG$4gq8a63DEzJ!Lb{h$^$&8is%RcD&!-fele!}9b'
        b'ZStmilZ(&gNu5W+r^V@ZA~}c8-O{Y}M{TpirJo4eLeScTSPni&>?D3i8ww6vBPN!EuO<4(E^<z7XW=B|(55Wz!Xv$1SGww4sR?iw'
        b'bueeTN|v!~9?fodx`(SS)!x|bNXsd;#kms(M^jq*D?DlG=$3Vnj3>QPZkxxmvbiPAHT_}39aq|xJ5w7=I5)R8I7C-uR+kFttW8S@'
        b'XZAD~YQ$`Hq}IyjPD!KS&1u#1uEO%*!4Pj=nd;HvT;}q4TWl?9MR$uwQl_g%d%gpknpdXwzI4mzf9bB@3M7N3Y#O9%>U7W&O<h~1'
        b'hYJf}OOq`lf^(J2lTifSkaD=i2Bx*enc{}l%I2Kh&v?CBb2U0KQBs<KyQGfyRKJYINxBNDP?_#yBqE<CnI62Ob#qC2P(wGjtWI@C'
        b'm$WuIo6=HouBvrn!D#fhrn;w(f9{B(C5Ll*o|m>dThpe7-d*3xY8kP})6*=qqgBrq<n7Gn*UTSpzNU;6rAKSia&&%Es^2P#(Tu)o'
        b'a_Hs-_u@mUPQS5A*3{PG&>neNy;B`mG<)@HuE@DDz57Lr&;p(6?)IeGTb#8k@Tb9<HtVqE@w)0VCZlv#hb|h|*67I=ppFk5%71kh'
        b'Z%2KtyH*Ut^ygq|APha8M#efnX0X&%UkjGGF6iTDdt&H<w7BpXr-^E-tslF<d~qGSI!zwkq{L#7El^{FW6?MnxEJy5QhEsScunam'
        b';nbXVqDs1^&pY9v-!pnL(r;}_Za01P`X@`KcWu4Po#u^Ahc|Ub*L%Hbn?~+}gEYpC!_}gHoN=G@XB>B2+2X<!#y-rJ>R#u>$;VfZ'
        b'QK8#_aUXT?;xX0aNm=mpx#;H@cX!&B*<4N8!_pSAq1ltxY2F4;<^&?gT3eHt9iHX}9FnLpQ_fat;c8oG-{!+pc)8P?5lG+e)X2@X'
        b'%?;@FMpwh?jId(dsKv(KJhda$U?L}MUoj)Hj%Z#ut?ucgDVdIQtjJ!>IniQt1lE=$yVJqbc4A?m?Rmp$5?P($?Zp$c#l8#~Py(r0'
        b'sDV5l+JJkLtvg;gDLxTr3tMZ0*K?wvSZ>@+$;KWt_^OM_FGlC_ns`o_zYot7QStFB)ao8DfS3+r1aL2xMWH?YIEm1C-czscLdPq!'
        b'+p~PUFkY8BkTOfXvbmv-SLp=(qz`uzjjsmhEs0gzRkwQl{HZNYCfv9Ulgt%+y_2c!_yMwZA}u(c%!91v?BcDm46BOvM0R5tOAXIm'
        b'#&~{nzqAJ>rSHhhQhn*ul6KTg@e?~{PnxIpLhaHt9~2$a4-0c^Q*EY~+gI;s$>!{FHaXJVX~$Zdr5+?4RdZVD<1aFr)2f$rc6faC'
        b'INGH?LsPufx?m8EAHd;S=G3jUS;M&TY){?VHPSFoKMn{-vG*1)`qEF)Y8Vf8m0q!9IEf%xUz}tK*NUT&Ygv;sGqKhtSL3oquQ;QQ'
        b'nI%ra4URE=v0b+%J>}iSMQ@Am6JLJ7Y%v%ZtAX7}Jn%phupO8K>;syCw*Yg2_W<*Nj{@_7KL8d0e+8TXd<!@cIN=?$rI2)I0_kJg'
        b'0-yot02+a9Kof8sFb6mYGy}f`%mscQm<N0Xm=AmpSOA>#F7g4+0Zs&3frY@!fTsX^fu{m*1D*!_3a|+H1K=d!?|`QRM}d=pXTN8*'
        b'6ayClrvSacslYh!4B+j+X~2hoX9AxC(q+)sfd=3)pb=Pn1oZ({0&{>(K=bLu@`vzK82b#+0K6M$1U^pTfxn>ez;`J;u;_i%A6N!t'
        b'QyFUp8h}>-jlc-d1RMb70Ph2uf#0NfzylOdVeBx)qr1#U5f69{kUk1l0u4Y1xdSf)nt*X&4sa{b4BP?C1%4fv2mBr|ANVt10q|Ae'
        b'1mHWsiNL&L=m+4rz*8t6;Hf|t@HAjM@O0ocz{$W{fW^T3fm47_0jC0A1TFyn8MqLbbKGpX2zVAS0GtO50`0&~DnD>7up8I~{4_8G'
        b'yaV`2;BMfRz<t0l@Rz_lfPV#U2bw-GTkfRvf%E}$0nh++0*ydFkmRDQ2j&281Db(f0_Fn03(Nx^0OkY#3M>Gc|Bm(no(r4^tOOPU'
        b'8-S+(1He;(8-b?*?*!7FsYij6NLmc=bl~g2$&}tG+6#CNa0>9_z^QZ(3wQ>l2b>062RsvaEATAf7l0%H`!S#a_yW)fJPb6s>6>>h'
        b'mkF~FXa-&m%yrW@`dmvM@NQr}@IQeCZu(Z8YncEv8FDQXfhE8~U>%S?-gW^Ez-xd;;5MKM_!VFda39bN`~xr-m}^A57}g1(0ay++'
        b'0xtoYfIeUja6Qlr+y=}A?gr)o_W|>PuTVPun2(eWu*igTfYm?~@CslK@Ft)cxEq)Yd<mEbJOa!Io}QCyDFRjiCjs5S(}BIf$-vJ8'
        b'i-G%qQ-JRQrvlG4=UUDH)&Zvh*8<N34gk*rJ_tM;_!Hncz;}QZ6fZZ|QVDbd7XTB$g_IBQBH#~zi-4~KtAG>paxK-sG9WQ^Gy)C4'
        b'0NIDpZ)6AF4m1LHllyMQ_L4jBzsMc<H=qevl#g}+&H<W%PGBx@4KNRw0OkX?0_lVNJwOBSTR<c5C5jJxm*NA@DnPjXc%A?aKrhe;'
        b'>;syBcLQ^P-v^q3hk&`jQzsxlU>Wd3$+iE-gy;VYMB$Gi2|t@4{1c0_m;9cBH$tXtp$as$HqsWf7CX@97SDJ}jX3YTR6~>ys*U(}'
        b'=M;BeoaAt2I&&dKSwy;fmz8tD_YKY!&IY|G_cEotOwk19$9sfS_A+I5f*gb@ow-YSa)LV`L!6MV>}o>t?sHPKSW?(07oOi0jb6z$'
        b'Zgs?ZOEi~`_A(`uDR4hiq`xZH<%Kr|FUyZ&f+x7PT*}x}q`bhQr2M^pO&SH(%DmHfygXB$kVj)MN!ffxDQD1-5pR~{p;{*Su<9kR'
        b'6Y)@yQie+;pU!g5H#5nQbFS%QNYg;~6?VO8wv4hf4TYwHLc^5Yv(2*$DU<7xw;4u94N1apn##m{wYz~CHexKr{%Eo@+J<pI;`a%>'
        b'YO)irPtL28F%hZsrz(X>IfICV(8ZFkr}{OMop{M)Fg8{=;!UYchAZc8WmHe%VbR4usq!HXPwR+QzG;$=ErpMp{}Fzx#_$`fyu?3K'
        b'rYo0PUgE9Unsm2vcj_zRyP5qV>+ve$d@Na>)OzF}GTF}}=PAW0b)<UCgdg$U<(!%7M}v0@{74Q-&bh@W?7Niq7^m<4yThr!@_9zP'
        b'wasX6LmlY+L3K&Wxg!#+Z%auoU-istE3@vash&AfV+GaUEby@kwC}Z5Rs$dUHQ!{C*D)_m&SsMDROe?-^Xt_4<)-;{>HPB2{I=-A'
        b'7pD0|boT|)?+wIsZUt$6JvzS$X?_Wv-^4V(?Ygv1N%Ol?=Qk&t{8MB0d(s(lPqT!ZnPxwAjBurC_S41)H!sazr2DJ?r3*foG)A~|'
        b'e&h?r2<J$%my8k4`Txj0c6DqFOwQit*?yyv_jfdHEDY(~PSMSSQOQ4QO=)9o+>Gkv(Q0k0jh9iKoF%PIwQ(|<Hc$1ft<LGXI*(Us'
        b'|6J}|U9ouatUkweBkaKTi#9zvw5s{o)xY)bU1ONHs^7ZkcL%S3e(z!)fnGY&TPvYE(vX(sKlFQKFE8rx%Sj%nu`SsK|AI6Zt`TV('
        b'{)K6V*NC+-Tsl&d^qYb+fRouRwalJhE2q%YhUC~#7c0Gd;a!MN?<yL?I5We(W`)^8e9v#UXgsaERv9wnkYLLeo8OI)-QDx!!H!Q<'
        b'a#MFGLdck{HxZR8oIMVu!`~Aqt0$?ws(NSGf<6A8jxN%?ppd5SP-HE$&9(J~;%pU%veg1E6OOL65z=wEzAG3}Xg^rCJQ$4O&=3v#'
        b'k%>@A9*ro0D5+8;HQ#mNXf#mPNP^Nm*n*RIA0hv!Otl8E8|T{R%G@g(8P^_BRu>Egl&)wvP*%I417SFCXqm^~8BA>8iI>^AOj03U'
        b'vaFdi38M<}L^M|B^w3{-Pqdw@$iv1s!j)W=HAYD|7ncz%&FlR=q?NI(A=Dj8#JQ@h9yCyy&=9In^9tqc@iH&!h@ue-Dh1=3zQbG('
        b'-g>2zikpl~x}G*D@n~lPO-kvOHO;q`@xF+2Iq^y&nO2H(j2F3579F;PXc*=cEha#Ti^BQQABxl$9WSeoc9SL~w7t|HMO?C6$WWOl'
        b'm{7X?=;R3crYE$P^ngWinDDMg&RoEGFs{VA{G_lJ2L&Y*iS;JRM9q+RuRmPYEbFF-wxIg7#)G1I$u!E`Xd7NCYL6Zag?L#@uU4RV'
        b'M^7k5tsFt~prBo%$aFs8LP8m@x2~aOLts$vy}@A5`8TZhZ*){y7tY08q-T9h%smI}#795er_Dtw%T&70vPrnn^KaL!!c2QDdcS+<'
        b'4zq>kcE7~f9a{WHd<HxF|G_VhiF-o%^4^C3MDlt5hu3kpymK<%&-g#Ej%Ua^PLq4S)h7sV`X63L+Q)z61mP_eBQ^6+GVR26vt@Fc'
        b'Th8kS`%I7nG;GMR_p2`{igW|Tcw(7Z>OO_$&Wk8hrMxfoVMSvpl_NE3S}FZ!6|$36zvRBC&CtfW3~eXc)1}8d5uPpS97+268MNDi'
        b'NuA_lr<eZwC-!q6{XY7A^!w=d(eI<*N57ALAN@Z1ef0ZZ@ymX$NOiORq{_Ogu-X~`#Xws?_f4p_?ltAu_YNEFgSS;#`$6FiM*9}n'
        b'XMzsiW3=x8?SdN*XA<%Tis6>{ywSe!3r2fCXdmc}TdJ(=)+%c;XeMYOXccH9=swW1po6#4`)lzlpD6NAJYux#%YC?Jq~^$_BQ^c*'
        b'k(!MyBQ<Y$M{15YkJN;LuX;vm5|_&N)Hn$LkN%I}nqko%ga(O5i6)6T63r5GCFV)YmslWig2agu3niW+@l=VYNi32$N#f}eCrd1r'
        b'I7Q-AiDyWhCh<&(XGuI;;yDt}m3W@S^Cc=0r%Rk6@naHaN}MHew!{l0mPjm>I7i}z63Zmcl{io0e2L`}D<oD*Tp)3w#ET>@l2|3N'
        b'TH?hL7fbxOM2o~F5|>J(L45nQRo0K_e=iMS93()8CNb+3zcyQl)b~f1jI-X4=l9B=gbXZNThresJ@%G(fB&S!Jregy+$Zr_iTfqK'
        b'_?G%zAp85N^k)sN3FU)W8@6G7--+i0=vh$Le^gobJF$j;vC29Oirr<jzYRB5C)V^e693V6v#;EPw9uYAfDND=(2*}xS=Rs$-J?Bw'
        b'^gjo!F>)O)9?l-ddJ0NZu!IfYwv_F;pnxg&=CR!<>(<{_S$Bi>fsTWeKVUrp<>clQTOMn8r^;IYW|eg>p0%&Og|+x^cpievPr-Be'
        b'?JDc5Ft0ggvOjrhwY3fY{V*SaIreUqHSm`zYa8&fQ>uBHcEJ1yXz=aqWu)J%xYFqlg@b{`il$Vryl++?Q%YvVOIauU7ArGm#b+pC'
        b'`jj>+FoCpaELLX4Cj|RqJ;8W96pe7JdLN*<#aCPJtX<AxT$?eeMz2sT7Nv4gDXXbT=g#Z$hv!R~yGbTWawCpCQZ?)ghv#)MQp3o&'
        b'!qkFUF=WQY<sjESlrmO2fmHc*5;LAJ7LA4%D~(*ur_$XUPblrAS|zkL5)3Hq8<bhS_?rmE=ZzJID@Ii#wg(gIgTV;J@<#&t$Q?p2'
        b'dQ#IY|BkG5_#=^MLh16aL#9fkHyl>Du9+F*XjY|S%<Eu6iBBR*s&GrVh4YB=qHAuc0m>A9or6p3DCI@r?h2Jbt#hm=ihc;A2qJ-y'
        b'P&}(<p+$;!MSH^msx|q~VAHdN=W3E<R1udPl#~Q0^JF3-7PV=%1eQpFOev{Q`)g$(6_zs?#@RX^kPN&$N+&66p$1noq}HCncuH!L'
        b'<A&tj-@$cSk2zoxQGK7s!@h2ROsero1bgV)J0?uDN13a{gB?+fkZ^EaFs!tP5)?2LmszE^LMe%&;<B7h&?jnn^o=P;fY7iLimV-P'
        b'm}r4Ahf2~<Iq{&;7kvqdqN1omhwz1p1Q8NLI)F(_Yyo7{$Jdn@)z>_H-Jytn9LB<-gt9)A=u%W=NfavkfYdjZsz9mR-*YAE;E&5@'
        b'OBp;$tZPG@Gk%Cj7#0`k21RNX6rog$Dq>KtqN(`MN?@F>?b78K@9pT)mz0#8rX>@K_QumQr(kJg_XGt^%R<)}<L5E`BuAXkdn*T1'
        b'PpI3+S71J8R87{x6HD~kpirMC9Q^I^Xis~JFBM6|<x9Bidg^C=4%{yuB+eXPyf>8K+P}EJ3`M$D6G0IUg9&4dn`M|#Bp&QZ=v}0&'
        b'B(CFnF=`f0gt!vvc^!*q1(ZNA!5L%}KY!qrSNCCt6VnFGob2nhK8X~S;Y{;MD(nt*$HJ-ZlG&Vl_}imBiIP%fJq8WwcN67s*P<wl'
        b'Yf~bIBWB?m&jO07I&LY;XZ|?VGx^kJi}9ppvg9OQ4o_tDLIC~7(T&v|<jTLgqVa@J$n8V5)FdvHs=G+^oR*kA3KogAq-C7ckfnGC'
        b'U0tFNGTpIKCZfcO%C=+QQ}!pZ*XhEZ<wa02_A<2B*$VQ)yz9?ZR@&>l_y+b(Fw<V=G2n}bs;t}ptnF*my$+fC+#@yp*lW!^4e?H|'
        b'wjKbMPpP)<02NNf-l#}?dCf1z9&2iK=H6&hwRI4*k^Hc^E}L9!Z8)RaT7>wI6pQfHu+K!=`{5S`I*><UQMI)_x`DHU9G7M2N-IO)'
        b'{A%kP=byL?UFV51u=7*PFo1L#PRm|~J+cgI1B|qr3*~B(p=$b)6DTs&6s2+PYEmb((3F<NgR6{7$$_!Mmx?-<O!@b<`?F`rI!hha'
        b'i55|Yjnn?MW!QoAc266l4AVpzLf8wF{}EY+7ynIVI0W-yS%&UDG(t%z>g$dMg7Vr?Qg#Rli)tz5DiFsE;XsI!A10KYFUr;aWemAs'
        b'Kn}Vw;$#^@<An_P6MmmqlYCc4quq?Pc||)HpQp8R;7qg!C~=n7&aa$XZ9OtAdpqww8}4VPwsSSo3nNbWoNDVi=ccxEIsE$17VWH*'
        b'plqd#9g^j+p7-w?_ig8i{!VmZt!Neb_bLC{wPw8h2NjY3`cR}D8(*gC93M~DI3CSc1w!k%Hq3F=N%F%Wx!?qd{i3|(CD)=9H#|)e'
        b'>WJab8@kuwCT6uCxQbqKDX+Q8-*Iul)gSivgMy-$3Y6Ch%HJvALZs_Whx@I{?@dbeLhFKZ>rYJm3nrD%C|7<zxkzE}C7y@xANuO?'
        b'_l9yFf5gRpQc(1Bm-0tf`TH(wzso)7Y8!UNcAsQ%Mi99``C~!sCk5s27g%pBaNkkT_CP`G+oCup{5{9>|D{X$v#b0Am(}WWyIpN<'
        b'u2{^~-|re6bPW%?c8^z<=McF-`E$W;<o`i|b$NmN@`AQ23u4z4^xs@Ccz40@R||GOF-}>2I{62y{u$=gpG|i9{+akMPQLzg{|v+4'
        b'OOu_a<^B`#U!LqN_-Eq(*W@4M{WI}@GTHfe(?1p8eEk0+!=u&4jKfBDXtMbaX0DX_L;e<RqIZkev9=W>HN;PsxCv-wZTv$D{?uPT'
        b'Qd2*3q{a>ZL$jFuXN~Pe7K7PR)Wqo9620jh-7$NlX3MORn*DQ`ebr*4o%04_A>DDoNX@P};*Ns?KVp(an%A9EGE#E{>AeriSvgYk'
        b'HgF^8Fz5|XAC+Y$GrkIZdlFrJ;debiNcW(z?a9kWYId*W?=!jEgWPOH+8>M_zm0gOb6`F;TDWGUCVvh24ci#7>&B6qeJ*C-`U8{w'
        b'mE$J+@Wn=ZKFXW(aijfJqro0Pn0tLl8{r<jk>cgD!Y!zK`$$bSNC6!WqTKDoD>?dC{2Qfb#^9UGUi>-at6)z9zp{amnmvm+54SZO'
        b'M!asgffDORYE~U(_AZ1ya24EpkS-9<5`}760(WnS*$=_Z0&>L77JFRCi6}?gJsV{9#HS4QEl5X+Raq0!D(e8u;cpx4dmk~_UxfJp'
        b'=>LFz4vIZ&uopjMu;*1GJTqIiZy2e0^NVK7n)}R_3qXtS<FYB*qyqPT)QLV_#pGAc?}ALPjy_Ly{Wa)4enSQS_aU7U&M!(|%8raW'
        b'V6FxcUuL0F#EPy)f4WU={gf}v#h_^*@7c`y#%iPek_XI|%Roy&>@uT$0O7n>Fl!qq46@o!W7f0KB9H9NIf^h%yUdny&?=-+53+))'
        b'L2gRdZ?wmNiK}VcR#^`mENpuPbTjNXfd)Vie%WkM@|d;kk0yIP!dn9vqq)pV_ZW|0Pk=6T6A`m5wG+LzXJ_PE=u6^*R4-Q8Hr!Wb'
        b'9j5g9X>R;_bfcN^Zwu$3oR3Un))L?zpmNw`FFuo5tC82CcTDyjZ=38}fNr?$N8YT%Xn*4q^j&uJgIkc^ER5B+={p71kXKO0S3zDI'
        b'Yg+|c18M^WKwY3|ZN|25)KD1<+tBjLOrQglLpY0Bcc4yTlwk|#u(h!5IA{=g>;P>C9f%t3d;Vs!ccDyupETM(54Xa#M*D+Pa_k$s'
        b';K%FA{&SSyUmijK^M!TK=rF9x;d@5U$Jyn&syzp<%VVz^bL{)k2J|u9@sQba)q`e>2e=Z{2}*!k&N5rxK)Bt=XFt+jc+E&nIj9<B'
        b'1vx;6;C=wK2IiS)ivxC)_tV&$eA8@McrD6PgE%lxr#W4f%MMsaYVNy{zGc!wubMRs(DzK32lkXCD9xK`99Hcay)KuP?KN8-|AE=E'
        b'7I+-xjsx!ieR(hSag_ZOeyid}dpYvpA6AMPyBBV(f8Te%gD`%W-vh>g6`*F&ji99<3*tPv&usa_2>J~82I#vmH%`j6{1iA9bR4u`'
        b'Z_yKbuftpf?Z;fAZ}Rz@Mrt0}V6@j?W3(sGZ@bW6tKha8)CSrC`zYFY>CeoT{ueR!frpS^C-553{@bdoTY+bQUIx*3pnYvd`(c=y'
        b'5k4P8--X)H|IA(37Dk$D&g54J?Onjpd$^js-8ooOeu%K2e+lJ$iQ2@#!k@-EiSWCpVjjY6E9f%N?fJ|agP#TK#k0<l8j=}8@<U7@'
        b'k{j{{%C|c=$3A!$>i4qQaw}*7X#dBUwHA0SD1rDZfdNo;!f3xAc!<J)PP>4y^P4d7wj1q_ApIASzjA=j#ico@M?L1yZj^n{$;W7s'
        b'1!KM%WTCsrplZ-AjH6dDCf^2?!*3zYTZDfDeX{8ET+0m55tO0-OJ+;4DaXF*8M9^dHq7!u#*QywZLgHGw(Ab_wGU54mU9qw{WHQ_'
        b'(Q<qCF!ooN-vqq{dYjzKY3(dx4IJ6weykt$Fpt(89%Xy-7+~~Ovcmx>7#uv@MrJ8s*2mDE3o$R+`pNB7thjHEj-HR4e>Xb1XA8OI'
        b'v%SFYPo>rP@1qI6?u;I@PByZ<iTq2ZVm-*(icrTv)cbZ&8_c7B8yzi2y2m#m{P{;lNl8ottxbr(wzIR79n53f5q1ZKM?!;??t7!7'
        b'JFvER_Z!+?eAdu5*v8rpyII?AxE(=j=j|CC?ZV!mA4DY^y@yuD(d+QHKMc41Sd0phP7$b>*N2^cHU5+=8>z8_4nACEozsN18|LkA'
        b'nd}MR+e<OdFkcT>gYc|YFo$EXw_!eSd&F$1dDLu~{3!MR;nAWC#2wpbuQ1x1;r4~c&6a8CvyCus0i6r;Gr$X<pzpIa-~1WOlVE-a'
        b'c>1@@mP<i{pbrr5tH7h6@4#IBZL{Sz&?}(%kC`p|K(E66dh$DmS>wR{aQh?ZlJA%;LD*LSF9q%fJ_EFXehKq@;2O-Q;*IDF)MF{~'
        b'|M?yvlj;hXgP><&|Jx+S4m@qNE0`}YUc>K_^}hn#4|)u=wHxCf_#~(ZX<0#KplP5(a61lq5VRe%8*~TKeGBP60sJlK%qP(%aIXZ$'
        b';GUSs*jCsru=m2;3A_UC7op8|z<n2J7_<@Og8M7*F9EJQ1$}xtv%UlS>9D^F`&-|I`BbbDPoZuw*TY-{^In)=h50O)Ujvo^cOy<M'
        b'@b|#)Q8{3~1^7Y%WB0>cI05?z;Dd<!9NOqG%+CV{U_T#yZT?T}Pk?iQF}NMY+U$Y31?I0~PSn8s4d7>iF9Dapy#O>D^vK>S>xIA_'
        b'$Zr+$D?wXVWBpwPa)7KL3lW|#gP@}CVLX7Gpe9iMFRQEz;lBdrDNma%p8(zm3W5x<m&5OMm|p;OgN8t~Umz-HX8syM!5(=lo`FSp'
        b'c0C7t5j6U+*^&q9?BrYT?;F^jhGN(qpajT^K4<{#!5sMu>;s@-&?BH<P?*Wg8i4<gk>&wBv#r=GBrsS0Om^&P%7WNSy=$@`gS`Rn'
        b'lR<Mqc!JZ`ZqKOcF!4qmM{Ap&#5`@FeZ!u@HY=ze#6S(8RUkLW3&MOlGCKM_N+9nZ;(mC6jC9~RK1vsHZhI>FciJ7w8|rHqZN$rs'
        b'ZPREi!gg{C=K39=yOxRl;k}CwxRC%>U0U#J{ysYTqfvQ_4y(%OA3*Qpi12rQ`={T;Xczhd;=Ty_IcN*!&i21oS=XRn|4Qo!vc|MC'
        b'e5@X82k5QFk(&E~4}oS}g1y4KqoZEnV{pF(_&o4=7uF=;5#R%G+XeHBz#YK)<=Eqaeg+zXePY8%%_d+K@Kc}!%#Q#&fCqsqfYU&A'
        b'pd74mi$FJmT0!lgC@4HZ@Z$}`{3K{^F|+;<cmVXtiPhF$01ts)2fYFM9O_k%xz`55`Y?JJZUfEOAAw?^i$N<vkJX`mK+92+o&B1z'
        b'L~*tCP!aM19s!Xcn%fcP+3C!>UGRU5UetRv8+DJ=Typ71O$G7$y};Ohggpq#eIF0KV>ncyC#L^ubo7;vVIlwX=;#}mhkwDk^+C%>'
        b'&9^+5N1%JK${#?wSKT@~+5`JmPz-zNSFv|F4$8-~`Y_OhjrQ$ue;M>NXpxO=3LL+nI&V|Q@qzsQ&GG5&$M-1gCi}UE*&;tHG?q^K'
        b'Ufc2MpCHG_j?eh1VTSSJyYJ1}_@~_u7Y#q5z;)O08Md6^ojHf^nzZp3!(S~L{0g~lKmM>SXYdO-2XC6R@jHWe74_dqt^>z++H(4D'
        b'%h`DKkS%Bbz@*_ji~4U;HrsNhwy^%q<uGiYbg%RHU`b-IKhZy9k}{wSD!pvRq~U=gGMDsjt2y33!!QVIiGm_Bl>edX<I@*W`38>d'
        b'JbhLFCiC$2Nt?g%-Tu!M4GvJILl+ip{ORBwIfw5=dOEj<2e;?I;ozN<;5IjZ>KxWTr(CAFY5MWPvnX82`NO>ALtW=nt@3x?$ArV3'
        b'`J2u?zPaRrgZWIxv7L4N;ctvu?^Eu7A^&SR2(rqEKNlNc`)&SQvl?cS3=@1VfAcp+)j->g<pbrY6t%qZYdQD-n#Z8<W;Ohe^QngL'
        b'Eaw%t$r$`)zUU*{2gi2hOs&l=G_N+SJnNLgrN1;kXMT9teE)U%tI@DI2Opj^=R*8>{Nd?uA3ONOB;|>nzj^c6y>A`+rRnKmw)<PQ'
        b'SsU`_PWW=p{g>oDH=*#<uNi-7D7^CiYw}ABTPq7E-2Yo6m7N{L$oXKDO?{pHcGy(@Gvzr`;pM>%`4{ID&Yb%62Za+}`%T`?VZ)|h'
        b'9YcdG$$58%p>T5fj6HSO@lYA3zi`ZU;26ridBz!={S1c68PvX;+b3IVi|l>_cbU3r|FQlBMb-sW!^-xl)1NzLAI>i{O>}hT%$o5f'
        b'c7bW)^gYLB%$OE@dGw%>-Pm#J^e16Gr)ZKA{583pdw8?acyM4+|EB(-669sNv0(PWEt4)8xb(?m7;c}reqhymU1#6>__4CBPZ@(>'
        b'XIo$2X=IzeO=X_(^ntq9M%lpW%lamK&G_0E*$<D>;@rPLxq;Wg#uO!y*Zzr34<0L=LtQo?$H4%%VCdgjq*)6uN%eg^#rNJF$5On}'
        b'aH{=`_A55sE_2u}9k+8!G6!Kz<{*6^Pw~BX%dr&i!n0KC1?|2~8)XK&q~k7bNoF9d$qc0L<0-!PhL7pIhe{@>ISh48s6rh&jun=|'
        b'R`S^3400`fj9WJTd~imQW-WB3`hF+Hcbn%}ig)3es+GpQjosUDZ1ZpqdS&=7<*EF2H(&Skguujs3w9)Sqo;40QDWRVEw|I&P<Ye#'
        b'EXN+sFCM%}SvRnLMj;y-8U6Oqm79mppFZc<w@VuNpgfIDwD$LJJNTVRcisI^#j*W&0=KX3@6Q>$E2saa@**r%!>{&#MHyD!-qHTv'
        b'>*o6(8y()MOh1Q4AI9AcjP3mKL7FE#wW8_g9>dDQ(|joR_0gxFJ@7+3>S<jmJhrXy*yfVTd#4`D>zYARdNtNIT2;ifUcKG8^BdpY'
        b'T%f>pvkOZc1qr1D3Dv#J)7trT(Q8LXMO#e$E!#OGXH!0nWVi?49~~6y*x{qw4j<i|zwh3oNAnI%&zfJu1fHETR(3bME5<+4&HG*6'
        b'{eK(f>%pv}qqH7iZV%YqIY)=`mGbh$#v>Pma>^@gh11Hb%gf7i5M}D$Sn%*D74A1jQ8<#dQ*rR9d-BmDcHugfUllUn|CiAl-XAsD'
        b'*lTZ7IFo@@&N<7v`zRJCEIPxFD_=8idXeJh$~JuB=+M1v^8v%={4@J!ly7?MXkPmTG!jdOcCs_tXA0we?1J{`+_>$BN2}V;<3?V;'
        b'JF9cw8RhsxiKrpRy7xwr{$`_L>MmB8ztd>iY&X1iWOS#|h=;>#-<55>?XIKuK75oqx|G(0VZLl{4zaC6JBL~DsZp$%?~Kaz{{C=&'
        b'#jc}R!ppy?1S9!{`44^R=)GS$dgJL+X{t<Qn}-d9gNbK1Pzn=RKOTDh^yJvQ96o$3UBb5Aee~YDk8XC6b!ZMd`%WtAgl*g56u7@L'
        b'|7)h#Hs<qZ#cRR*B@?z@Rw&l%>4QfHj8pSRgROZb#s`KDO~2)6;j|K?QvKPvrXRjb^(;K=wPZPG;fQ_1(SiJ_B}_cf#CmuC(a{x;'
        b'qbSpE94h$#IC~ecsE)G%_}uowa?srcHwdJjJ=_-5c3DhVY;1Q|MDWr8Dx!&B0bL}fY1NQwQ`_uW5?BanxtIvnd_B8yBM`R%Oe1Re'
        b'!eT;<fiGh2skTH}?)N(eJ^#!(i<dV4^L+pRJUp{=X5N{3=bd-n%iQqHb3jh5ls!BeQVH#a-`^sGBEKHCwpak#(>6&t`*$*^@SE#&'
        b'OD8D#<kuj#5hZ0Tn<pLz<EBPIYgA_5N?H21a#L%s!H`ETc{dDWcT&1mHyKD0+NAuHRgjC)cS}|TXhW&>s$bKs7Esx=)!)Sa9l;C+'
        b'L)npW1Ff~ta+Ol#OqZsnLgKO;s1zq<&XCgVY<=pj$k+5FMn4@$D(NS5q|zmF?vtJljY+vxjh{HLnv{?@(0uMaO{gwwspny_Nxd{K'
        b'fN<gAd4O`X@1D~QIj{YM6lZVTlkICxf0NKH4|Jj0i<CCT!WbYQX0JtJ;vfU)aa~s68mzUOL#(ZxfDBLe6~-&A%L5DJ$>7TJrvr;G'
        b'WN$>o|Kdnh_C~Y#I=52X`VS5<d`=lYpyc(Gc|ufhg9ApE_&ca;AaCQhc+q^n-BFHFZF9U7ziWJy=la+j)d%m{9!&79|FBo?mXqFB'
        b'4*9ooe*gd4i@|T%a43}zgCI#mQAfdVa?<)e665VTGSHgf(*}r{gr|N#=SwqFbK3)a%jV{oiMe9|7zhEdNrN!ca|Slg%ClVhxAV-1'
        b'fGxBs1B0tdOOGBqE+GR<Nj~C1I6teUwbiB#zP#;K&?Cqs=DRt&XU-=5PlasnoLkVj%r|!{t_mc5%9DKf`NDiQ7gEe;9ItdF``!bA'
        b'F#!R-Eq*#dee=;ARhP$nG6&Fw(|~W^J!il4!|h+3yI<!YE-igEJ(=T49b9^JReI5#Yc~YIzt25bu;Fe&p^cd8xrV=Wmxm%0o5xEX'
        b'yv{3f@brC{bB1H=a}N8`d-(GsQ<DS}^xmrVq>}G58RVQ?nDant8~-u~rk9C8*Xu+_#$kG=NfDi(er@hbf<l9BFkK6E5D0S&c3HEP'
        b'iY8cETQJ3`|2*frB}EBDc(j4N#gxMA6xl6=?GKKAHyjg3BN6^68JdxhvMnJ_<V<~Ojuby7a^cyat^x?$By)+G7hw!mpAREh$#Z&9'
        b'+|g*5V1WsAm`G?aEkI^{qf<v9+ii~kG0JR&x#G_`q|J0>ymf{{nCD=Mewy@sEZUa_IzyFqC+4X+9f-Vf3o6U%t*kSF*$bh7I)QbV'
        b'`8qCgi0<M%kUb)8Mn#G?FI6)Ko6m%qwyl<8g00rZ9ruN4Pr$Uq|KU{GL(C37f6CjO6j9NG%;q^Oh|GRp;No>uOwwEwuD71p4eU!3'
        b'hBAq;2&p7}*@g-i0Z`<}0NBOkoP&O-Q--iWk+9EMY85O^dGp}WQDUw}App>*n6*3ytO^>Hu$9kIRUkq%pnyhlwmPq_7CJVdEL0&j'
        b'1sGHdz2F}mn3zqA4CoXgq-eV`IV*ZDBmIPjloq8sB7YAmjtVES4I84?X;jIg_($fgJ5;T}fnQ;BiC>rgwrFWX^e4Wywt>zJMe(-I'
        b'ZHlxH19zqaW5#iLkdE}%u_&;9NGv6^0yG9CBBou{-0d%pT9-J)t;F@Fk_wQTi)Zd>{<8Z{{JI^cf-$IjjQ=}p4GRD?u}kI}Si~BQ'
        b'o~`uPh57T8sS0WpBTZ7(H+Np~xumH~iaar<+Jdxb@VFDbD&IR*8%bQVGhP#)6j%O9(N0jIFh5hz&6>gkIthd%)+>$7=xkEPiB+Ue'
        b'RYp`8aAOlR()d;LEy>bEA7n+5rI9MFp?+H&)Ux~&->SCx&Sb^$gw6zo>4U%xN#Y3(Y4~K24);&<_RkOw`?peRGo{<OWE1cRU>~l`'
        b'nuz1707>d!?rYe<T!js96&kJtnkar%R6=Cc&y)2$U5nbKE}!2PFKt)>8y@)ghFjWTyRcCisWdn$fcoTR&Fh#ZIo--7Cl>&QN1AZp'
        b'qKtA7k1V9@?5zFpEbW6@eGtKCrhPDAl_1_YUUqQyL7zDbp&V2c>Jbs@zs_2*#zI+axdNzpN3pd$11VRa<r!%BQ;5}$78XOfLet7?'
        b'm>EUXnX~rSXTetkPnQK<@Tb`Z7D^d9RB;x=S}8=GK5IWZ3+!Mx!TquHAc>WZ7fcK1ZqUvOORfCGWuPY3;?8U&V#78ott5YHFPH@Y'
        b'=4X%scmc5N#aU}829PdiQA<sQV=bN@c-uh-!@0sv?(K)7PUla2wL1#nL%wA{Gz&0N13J)#5~Y9~l#!vz^u}AT`ll0nxWawc0dPog'
        b'>jWIXvR}`Fc>)byAE;fH2HPx_RfR!|;0H`8@~N$%Hwd;>*`EIousi?nu#`3rh@<ddb8IxFT8%&{4GfW7ZnI1k#2sW`+J$93K6|JF'
        b'ORPiU&SI?zNXRkpCC*3U;(irTv5h<x7q>cR3s!I($;rnON06LYOk9FkFG8E_v6;fN(u3?WP_SSKIS?~T23aGcO7t!q%0ZSW=s`l('
        b'!@4JtkV5cVa2Pqr`W>ohRxh7DsKiJtZZB4F7STo;#qWX~1~&W(X!z#`*%v^(^)rZ)_z1EBR8ms*qgjnlx^7<m`3(6GO>eR;#i$5k'
        b'Kdn7-=nAda&+{I=154}$+<TDChs_m$x-juo#A!luzQtNUK-3@3lzl&ArBe?0%|dosN&suvU{ma;<rd!aqjwPM=9x{tG%dH!&p^M6'
        b'zaDmwt%QAC4kD$8VzI<(5GjJ#9sn(*A7o+Y#G65)?T|kvZsbzmo*{$MzQC+Yq$@-zHaRJ>?98v*rbw4YmHlJp;M?yDjYIZXN`PJf'
        b'9mFp5LBOJ51*q+1*ol3}p)**)pTK7csJxZs4pht>d`PC+9#(b<P~w4_q98r?(~5&Gu62N?gFP;8Db2Exu~_RL5Ssn(xCX5CHwZB4'
        b'zvf!~LB0dh`4=E^5>#GL#2v8A9E{wkD*TcCqZx9!vyMyT-#k6={EWSE#u_PaVBwTwF3gl&n4yyhIv1gn5jq2>BjW(IRuZji5%q6o'
        b'gjuw=e>nUDPRy@zI4^R{i5apGq8kXX<hz+cw2pI3!wjfVojv2oUJJ-x0PotW%V%J|k~ntbEp^6B*%LD~z45?bXQ&?&1}jQOtrZ50'
        b'erhcpB`1Ruk8<QX@jjrZU!6JdD#R;FO0S1#sW*X=5Hoc#h&-lhnewO+@Y(t~r%s%ye+4AUTVLc-*Um88X25`@Es>HzV8C`^V8GaI'
        b'@)R&;m;B0p4aV$+2Php0$E=iAh|4*3>`Z+ktf=51r`CeVkEx#!Do2O?&<yG8Ji+NMdVm2S(H2%%6Ook6$u-hLuVDobb1~)_YpCW>'
        b'pa^&tfC7=-SYjZjre^HBU}fZTi1of1Qj})up+h58x(|2)CoTr$WH!tk$eIyoxk+}Hnrg+2uv#E~or7b1mTNr@iSNRl?{VTv5IrEB'
        b'Ap;$eCQ`x{=3Cgj^z&T@l4i;u!pOq?Rr1GX4*9P+$o}z=|Hc&$0e(na!j;q<n4LZtxoK|?CT{1{bJOI@06DRqLufIuf-b5jr)m0+'
        b's+JZwS9~}Gzz;6KyE*mHbYd|_2C9mX1Krcs$W4|4;>fv9o1%1^+_H@-X!NdoIj9KhZYwK|)URSXr&R}u2<67Ie@<JY*1}bTr`9sT'
        b'Gv%5ey%z=O=u0)`*HL+GI#yG0TG{D?h$Vm?$V{Q~5r&#6EdPjUo3;kNw!Zg&T0zh0+_g}LST)w3URS|9$9ypD&}?L#1hj)3lo<F`'
        b'Ajt|eU+-+|B$U~Vd`2T(SW8_r11w^ieItX2JicBZM&q*ial34$32!+`GG9(Ziwme28I;7hO9Umae@xx9Ex@|_5nZSrm>N-pdT?4t'
        b'|CCgg_<L<K1lUO{Wd-wIn*zvZ^&8VbMAP)D_n=x?DLY+kefx#td~zu%v()6Xmb|t~-9@XmDBq%|N-hD{zwLRuXBsX^4gyQtY3CBh'
        b'1v-XLa_XDYsehg(36lw-!|63L2MgKV{x4v<I)BX>Uz(;_&KhtuvNBkGZdy>hZR0sN*U{mjWH2d%qv(eq5o=e0)-g*|KF~Ai$~(G?'
        b'7Hw31y7hKU`*afqIO{2{CEzHGg=cc=H(^B%llb9L9m~OrZp8(POrN6;B7_Vs=ofHPH&5$ZRBIJ6xzjF87a9SmLE<_SqNB0&n~QbX'
        b'i(<}AC;8j(n8xYCqgd<9Nb-&9Ri;p6eUPv5iD}1f#1s||3?TiDq}}?^WICxO?kH9eij-rx71vs7v<?$mxD>OR@DqDX#G^X=Q6wQ0'
        b'i4BblklIf|S~<VrK-p0J9&5nTcpd2vnvVJFbaIPUFV|`(OV-9bH*MXrxFO6}^$B7>K5b$VPbQ~tNj{^a$%asw>H=ba70}iBOPKgZ'
        b'Qj7j-TmY%pX=9A>4e^fn@^~wW$6p0av|Kv#u~Ic3;P@cmb&O2<t!;6mto-A7gf!IEm7ObcT%NaGR7nFGLM4u{MbP9&5zs5u&5@X`'
        b'kdCHMc}~D;<Bz5tVe5emmF)X531yCHx7-xE+z}d`{Fy0qWz9v??!`Q?!V$W{%33T5RLxBuOi^u3GF9p})Ye!@>8W!erM1m9RtJWg'
        b'LZg93J~B@Rv+q^ZowNWkusgcCJSh!8mY+KJBM4Ux;K=2`(g#h|*(fjY`IC;_%d4|b?@Mw3ScezZ0bw`tuqz&fT~XbTbPzx`K*;0G'
        b'RSjT_$d~J?0OU#lNd_JHzVxk%+N0&WS6WS&#lX9q{>0f_sSfwmu9E9an4V6*C|0kU)+?dK?;o#hRU!7c=@9becbM5JNVLCkw$D_J'
        b'gN^ysUGTGxLp+~yNi8Sdu@aA*$gS=&1&P=1S!`TB&0L>q+-cq8pY$znJ}2W~_*&wxs#~Y*_%xKW8+lXCH#VMDotbT&hxRU|ot()I'
        b'Ika1D7f<Wnet`_u(sIB;o}Y6u4^8X*5%38>R268}l4)blRJIDCx2BMyy|~PCfs43>dA5Ri3B*|;Zq7PARsJPbzEoQ1vxAwQvPyf>'
        b'rBF~<1BkN0DPcp#x|Lx5dx~Ff+$!nC#0iM`ET;-W!_RUNmwmG%<o0i-8dyW87?|wL_ptl9JF`{d^*ItUNFYbn<kVhZoy8+r|Cpkl'
        b'Bn;aWDd`mOh*2^z+lXYnJXMWmM+AZj*6*f-O`-AtLTl4n{!C=QJ<@DbWb)f&0xoBN0Op0#2Vu7V0L=UBgD}QVrwp<3lvoPPFV$zm'
        b'#@ea0FipuLE({33$eUQfyPVoQWp_+1C_8)I6p4rbl~bRd(gBqh7OAohKzVc;2oOkw%BfAhpbO#;xSrjsVH08UtZh^2v#9eVXJs{o'
        b'G8KRV_KE$KDFBwu`ei3nK?fWm0Syyfux#S{urAiJ7uW0(gDSGa<T)y(ljU-X$t=@UlMK|5I09hog~0jtP@MP-_t0*?te;MiFGCa#'
        b'O|=ejWFnw->uGM6xZo}C8d2<2*|8~yCZxuv?6oQTYg6U9Ay$nZ8cIi}Y6Lsn`0A9fx}qUS-(VWB)#}yc61dqwtn}4}=dZ!&%U0@%'
        b'3P7*3{!gbCPeI`<f=i@l%fr;RscZ~6`&zU*V9L$_ib*1LnEeHSqf-S(!Lbfm372H_gl{a|5hQ@3Q6HJ2F{EVN{`)C&fENfZRUn`j'
        b'O<1@;w^CdH^#-DTdP;-wil<;$=ugbPDPE-o!}X#fJTm(Ubq-9iVsHU@P+GQUs@w+|EMmqc?YpLIha>cu{Yk*0h|`a6$Rs#Mi1iZ3'
        b'SMcy?S;ka@4^r}UlhnR_s$hz<r%!og9EgDSnWQNfCalpVjtT4UDO2TA<a9DzNkhthG38)OJ2p=puO+2q(Qk_u6`u#Sw)i67Hnwa;'
        b'f^9%kNhzQlEqUo05zvz9mjD&WInovvk7*g>s7(>`v#H_+@<ilcd`XN3MKrt~F2|A5lg6u;x1V|pyLwq$TDt1032}V9{n%re<722#'
        b'f@7D{;&G0|5+{T`#wKh9R*q`-HZ1Cho^mgrYH+N#M^AZP_c_+!*AX@4jsPi11<>AQBBtz-kYuwOIOMtRu&F4;!fIv>Osmc%A8zJ1'
        b'vTJhTr_KHF)OX9Knrr3m;3;p0O~?p@sde5YlH?0Fk=mvT>H^wXD?f+Uorihn_<9c4FP`#^&5T8XXx6TV>G815<iL-ru*9DsG14hL'
        b'uEUqEUT3(L57IB?8bwpu>!_hkex(gUf1K+ZyLubsrNgGTn^RJ@!a2MJ=Ins==yOSeTw<S_%-ouvvJGYV2@V^{U9S>lw{n>VxTLAC'
        b'%s!1|#>x%5Vct`4hwxx7+>l7hC2?{|mTR(fOTJ+nnwcO^Nq`{9xp7NHx{o=n78XycPCJdHB*?X^_^RRlpI&M#ob+zn=JM-6(#VM!'
        b'J*4TJhHoEEC5R!dQAK?0cVq%tYCtONr4_(RmwWfk^tr~5K_&79c)p9?@58Mh@q0~IStKPTFD(nvPEdx<ymr4PKQM2@J2|*W0@pXm'
        b'kXM@Dqa5sC!*6p;<0KNTu+VbW@*MC-n7>b2YUS+Rbup%4l4_tF8pQk~NhyE!J`2%hA?6OT{q$tR+no6`af=#>sh)i8S4cJ9gqasf'
        b'9HGc-3HYU;POGBxgd*B@xvEiCSET?Z^Ko18%k}JJbAp0j;>GITksDv1G$hOG1PW@}MW6;hNj2Us1`#=oNI=A2a>)%V_XJ8@m~)yl'
        b'e=N4YGD)+D`Cno$p5{y9td}7|nQv0zm&K!2(6HJz3G~8FTcxrSZg!eJ;Bp8b=Z9jK*z*riPJ?fRk|s*J(U!=sRk^TmmBd@03-dg@'
        b'5Vs$iTmjc4Y_bqv>RdiB09L|<@FJNvU%h{l$~I6Gv9M31Mc8P{1475uE5!=d)?Ai5Sz4{I)HYv@LYSP%(OLzG)%8PhcS+hzYp;CL'
        b'eCn~`b9@_8O0#gjB4*d5uqmcddfpSa9dzO5D|~;gN<`AT#HK9a_pPN?8Y}b>+jP|?xB{I9oB+Wt4?io8+2pOl(<m+-z)N2zm<^Na'
        b'q{&j7r88NPCPg;T8mweV_%@$37EMb+Qo7)x*?^2OPNvZE4Ynw$vq21u<x2~6_SB2jaj;I{@Ho$i>jv<;CZg=o$<CJ*mMROQo2>RZ'
        b'Zv&DqJqqzW?o-YpK>V3KGV|ZWVB|g!^ZeJAP1}Y2H_vHtOqdr#=ikIO<$Id)K;%e2TO}{gKpLf`7tp%K7!CH?%UCtWy4SI+hzXg5'
        b'3t%+>E9d)S5)%(`hz)C$c3w~<@*TGf;Febi08WVt%U@;f>lisK0Tl(@13oBoI>j+!*eIaqDbS{>R|Fd6x90gqZCG7>o-Gi$5Zd;2'
        b'2R7-(ChhoSgJaaW(Wg>cT7{NY#+<E!MI=xC%$AW}dFQpi;2Mnl6=)KmH#q^(`>PoC=<i~{qhQu}@dI4}C_;=zAyDfS_vOahRvMuO'
        b'aB3w1<``=cMF#%U`4>p>dNCl9cog!b^SJmx*91U#|0&9RLJah&R-0!q<bg?^nVB~vzAkDfns6{6%(V%A+r@lL?2<TL3uESdO`P@l'
        b'#F6h^VsqsKrG<hnjQJFn3qJ~GhPhT4BXfn={t;|5{MCPNaR2_i+meM=LE&b;$E9NXg$eVU3vDt@Fjakif{L~-><uxEFwM$7u0A_)'
        b'O5@AC!-F&kARu2mfNR$faY}hd-GsYt!d^GAVgT5z;j4U@GY~Y@H4)>Q=%f|YHVYMNafBlfzZZ#!AS^t}hxa8ARo)#FzbTv@3d3aF'
        b'=$MF30I|b_kriS|L|Yg0-xJq~Xj`=u^noz1BmiZBZIu&HYpk3A;*(0SR1;8cI+qiP9^R)uIzjp@>~z7oSvEnlgl%m}AVAEQ)?J*>'
        b'!A8SHqVPw&`(VW&9|hAE*t>s%$O|FqO9q*XFw)n-VjdgDFcZ84Vl3X@7vL|QgfjVj86o_=H!<dUK7vDw>O`8rH9*L!pPMMAdGiMn'
        b'+QIH&ehZ5gOh7-to;%@u2O_};tO1W7{Sij(znO49GeP>YZOxzokPwk3xBqIwz0aG**I}1TtRNd$Df29k2p`&ad(-yw9g;D>;q&;g'
        b'B*;9>sUMz*d14}U*95gz9<y^o{lvuTRa)&-=NpRX@P?BJd!gAtH&fIUvl|w1UPhU081YnMp5M!u1irTa5^8h$`W)CiVUi#v0iLHY'
        b'qke)6biq?l)&zvv&NCA#eOL1}8RR+1F>5D;13S`FMXUMWg)?aU2QO6aecnB|<IVLR+$qmR?7E3;KtnaG9$JC~ZwV48FwWQvIZ!Xm'
        b'k6@N+$sLGS9`h*wwR(zN+(AvaAD$Rm3>Ouc7``9c`@)~_>>e^vgPl_{zVIU^Xu=o-$5ewGghM?zBZe8qJL9C1g!+L_;Lm{>ku~rL'
        b'9F6j0pY0ucokBf5zWUzSdqF{%#$ye@0Xu*aDSYj;Hw(R6)7^BYZyd5rHxQsVaD)`4cS`(FWe2Bp8+?pNM>5il`>2t3a32NYPHxFs'
        b'd^JnH?ih{?<5<=bSi(ni0ztZP<IFfh$dN98a(@B*2ZU4OQlw2wW+nm;CI!n1Kt9KPV$jiXq}%@)^ws6aORwWnHTaM!kazs0F@Z)o'
        b'g#Z}&Dp0m}ob}%IJ95ium63jMK04fT=hqU?C5(Qfmpboo|7*NMHBQx9nW1rkz1?!pB56AYe#teYZ}=@qJ4SAXU%}=%2^kE_KP-iz'
        b'TB`0Cf7!0bG|G52orRlyr7zo^3J`dfN!6c>yHGw0rL$0vkJN>F7K0%CM^eD>pTV|(-`W9xz2OxY8U}E~W`e{>|6Q12OTJ4KeuQ(0'
        b'%+GVFjpL6&Mk^Afo*fr{-}V0f-TV8F_xFtO%QTFqHjMMUnR1U&frR+mc<SGND7|)kljsMMo#SNqzb6BB{~~39-JQO8>g%w=C{g55'
        b'KcIN_b1uTUpA&N&T+|E)pP1*@P*?tjUk8Ww&THfRF-sD&SP~*D1Jo7cN8sTBpacUcDgin&ch8*)B#AjVUUC%3Lwc>ir$C0OOq{x4'
        b'9JJt>kX&Wa7DtBR9ST@r|B{evT29uH!7j}FPhjqaBT`^Fh^3~rNaCp1SN+{MxfIwH%;E7UDaq4SI%@Rlm^^+so`oTlbqD!RJ`~O~'
        b'9Dq^vugCBDf+b1JGXnG;Mgt>ow_I4)<Y$>D7ELckJb#52PxvZy!N$A8K@^!^j^8`);hE=1Uy!!*{<I&7?c2vatM1xQ4~y+v#(~~)'
        b'E)xs(H1rk6%TmURt%c{Jna9V=9_ORW%6>6!e|-FSIT?8DykFVo@#8cIBF|w~7O_B6lMGC}?WIT3cv%uG6fdSqSCN4w-!R7UGShf5'
        b'O$J7uLrJMcFii!!w&YpnXI=!EHGF>;)^V*gs-v;;OQZ2vrH}Q}WEEX4tx<aBfcqF3q>6mQSFIbTV&&>XV^l2VxOm$<2|NmFq3$e%'
        b'N~3_00L+%|C0Ice(!$EMXDAoSJT?Z^M%Z{0;hEtY(JwC`>Sg291-aThMqQxjPj2hfsOqT19x~261QCLk%rY3UFCAz6VFaE=2!@er'
        b'1?le@<xU^3M!!6ds272`FIR6FqiQL~<=f@~j>O}RFVe)2{v`)#I)H8&q*mvz6p^Y7wMryA{j6O)4!F!Y!qIPYb`eBq7#{SnBjfGB'
        b'y<p}bqKQxlx=^@SHVm-MtktsGJb-iR_*lvXd8!_SRN5!E4+5M&$L%9yOg}7@;-r{yzMq3*OgD_UB+T#_ZycnL&!orBW~f)<s+VT%'
        b'J!8P)=;0Fo#Ub_^W5B-=G5>&Y;wcUQJUcD^66$S0yapDL+bQNK%zW9su^xyY3M0uT6ikY~1z%3!(U{N2>S%?Qw&++eFL|3JICdkQ'
        b'lRvgF?&fKcy>09Yt$?O`t;I7V66}~3Y;oB~W6jM(=X;9tH8$C`z@qFZS<S(=E!9|~(!2<PC*^vvua(t-r`AZmIv!RnJ@r4!st*@s'
        b'*Bp$JIa&g14yV6y`+Sw&C$i!*xQPFXtYDI>&Q0IR)nrHIS}z3_9c=ZUjSL?a+24XVMAv$7v2ZS%sTl({GO&Hy(IzYk_2i0dXilIA'
        b'uz=ZbVGfxIB!(TMLlJ8zN<~{p|5G}Y#EUPSkM*7}IzC2j;E(lKqk@G4nbxO*nODaa)?^m^xY9Aw*Rx4tSdOwMjljpPTV=dUpDs~q'
        b'@ffg?Md95drfBR+f?`8b6cHbg6!^8iQhG`A)hf~Y*CijFBT7G}t`j*V7U3tc9~mQ;hi{gcJ4G&$b9&+Y`aR3+@EExi+GcQdr(&hB'
        b'Cu2vfZh4Wy>ed#aWKw);a@LLmPcgqMD^i!Fk+vdrj=u;Ry;2-N!+Y{L((C`yBnt0SulwSAMC1#8;f?2BJjZ|)`~#V89*IclijaGL'
        b'Kw;Ml3j5<RsINmnO*mA-g4XVUsyJl~XkUGd)}5?3YC)-bJT+zvDB%=%r?`~r#lc@p(wHE{4Rop2#3m8)Eb0n@e5k&wyX)`jZY}ad'
        b'X#!q67NP*0s>gq-Lr`2&u?WF%l?B0?IW2-Cn7_8(|D_OI*?}tE%|}KlssbPh`(5x?1W7DIkpH(H!mfaBqRYm7P|(L6Oj>hiRBC)y'
        b'@`3RzrAUUWKK&kDI%ep^5fKZ7|3hPfr$L3X8jNm9ipN4QEp3fajzz~J)FjYghE9L&Bdi9W!$AikmswTTMJC{LzlgQQA*nuNNP^as'
        b'h9HJ@DO*{S63q}H36v=f)zFA`-A;P`jOAxH<FQf@C~*_!Z^A=OM65}))+F9ylI%7~pEdd9n`9Lx-#1L;8I#{d)1uEzi*K6b6DCFL'
        b'G9)MV2%-h$<seW}AfUA%&>28rN&!JyCJ3_kgW#YA1lCdzl(Qgk)PbPk3J6*{L2z{x1UHbFoAKlFn47w6IR!&Sn7KWyyFG00b$Css'
        b'#S+$eJuGV|?8Z>o?%QEqw_7<*^{Jn38EU*TD#?f4MPjwOUjpu1XIKk{KI11l!{*QEF>UXJUa9Syz%k4p!$UD5789+-#9J`QZcO?t'
        b'=97=fDlp$SF!BuMcM)6k8MgQ)CZE8({R8C@SRS3w(^_mouhZfadXtuz(5God6Z&kectU?rE1A$+wbBWFxz=Yw@6gI7^bK0y34M#!'
        b'Z$f`nyJ$jxL%VoFKdzNe=xDiC0YZgVIT04#9`<H?SmZ+g*y~~Hp)ki#Sm^Drldyl|YGnqKbU>d)t3{$OIC>c-!TJ$e4$R@F%6?}D'
        b'JbEKbv5v!X%MRPGs^vG-ih^;DG=N#S?mhGY9(<4i(HBOsEJTh{NQeJR?HJ08BK-3)R2QzjfgArgs-@+?%2!<_0JvTYr<_5Ua>lKr'
        b'1~A`<QeP7QNI%F0Cm3$}hfEkI4Tjj}<^jC9ooJ3NHU4_k5L=gouN3F{gZU@!15&lMhg<gvb{|eH5T^!+(^ZI5_5w~<{nvefp_vcj'
        b'wCg^cuHKJR18)4u{|%?)AH+%2f&n?u0_8x%f*g?R?x)>Fi02uI=VuVlpDy6}ng569Ff{%_JRiLe&(H41^9*hj{on9h_Jer7bQa=y'
        b'5#o8~E}pT--L(iZAS-b6lP!q90ZFiT#wt3uDOUfs5+j2JUE{(G3);rnBL)Vs-%hyReJPOnuMta|oVhdtlux6i?s)TwB2rcI(`S6x'
        b';}nCBuC6ZMhh(>M&K@j1hqKbWhp7oEeDRG^WWgr<e#9ni(?Fe3dAOvgQh$slDwB@ULpEE%94FXYsUHsen$|zELb7`a`N8`9Ffz;#'
        b'OZ}8S@&TZP7~Zyi=;kO%r1p*+7Ikh_v=s&?<g6McWvyYzr9*9x9WE@m#qHdiE8dGwxFjE=;eSQ7wem}7-0?2S?&oZAS^pR*yEd}V'
        b'Rv4eVF}q3ZBCF8w8A&Co+Ay#FVx+bpdf(o2ejT5WxIZ6x><RnlBhIB#_2(nen#gm$9iNT3KOK4OX^1IH1(cL`d^+O(WaP2mCr)t|'
        b'OF&6wN85<|qmjp6P8{RZpNvFD*I*kR(4YaHGwB(XsDh>oz87o;U_nB=dkh|5Z~L~S!QDK<FFL&sNxPEZZJ?N@5nU*fgD<XsZv-w&'
        b'&U5T)Y9-L0^^GHuXR!LSFx4{%Q`7g|QR(g&n}=N(F#ZO(HL~;#x7~FkO$4a37S<^i_HR^IG3Kq2vcHT#vsy&A%+oZmoz2}`+qWHW'
        b'j=0|(u~&{X*mKP?Y4!6>SopxgTJbKdt-J}Ilkes&w6-(ASo<FCzwk!3dhc+YZcP2^NY+auRJbMbQ8oP`teJcW;@!zTBTEk=I!Z^}'
        b'rJ(X+`wJsxLJBNP&p$bKAC-O{=_nd;7lW*d#91!<MPS9qPaR$3h>&P6QcWUrk7T7R{rK!3Fks`tCEx3iXsV#u>fbhD=?@_Q;xoy$'
        b'=#J+{+`j{L)F;B@;qYAj1jk<7o$`0eaFSwDhXrHSGs3MT#Gi74&j45Y!pA|6+WJc_x}OH*f)@FIjoh=XC=;cAVgz(02UECrjzGho'
        b'FwgTe0FAh}jl?xzAOvGaIEO%T`p!G5&^xKShMVwq5xlxL2oq(uA&kg{GwVn0-DT0HIkeeU61(;Ypsd(@1wfV*w~K+{+zzpAy8&=Y'
        b'^5PVKA5O-E5xB}rgeQw^SX(1-VHe?TLFR6WBO8G?5T6j0^7AMI8+^{QjmQZSd#{B6`azEQp3A`6zUYV@ajzP&uNrA!8S{Vy+Gbmb'
        b'h@j8lb79n~_tJ6_czf+T3F+I8x<uzta|R9w6_oz$9i19cZ2^uY;>_fHX)=JssZ|wPDznwYLB<AT&PkA&Q*kz$N`y|QIS%Lf1mK>2'
        b'1L+7HaR-jrRbZ?h@!XUM_Of{+Xj|`~k@S9~LpkDBj@bPGX6HTMN$R@sy1G@WPtcsTSoqfx;0nm=sd&^Z$8Bg_AmB-J25@$A){33C'
        b'FnBBJx^KI$^E#Gzi$AA3H!R$t41ZLlqmdJz0q}3IU9ysIJ8liTzaO?w4mYq*oBttk;m&RN4tW1^{erzqh5)-61K!ud_a^?k|L%7P'
        b'bc@Y*eHL;P|J}Rr-N2%7j*r9ZSP1`32y@>14Ln}(ZOul=VCN0*{i1tm8_nNw0&Re|L}wx46GFMW-{TA4paA^t=a@^wfKv<033cmm'
        b'6zW13u4~<e@$_)a`wKAt!^4=z{|(0J;h1+9VBP^RpgAa~qN#;_GH-h~Ip*{N+*<-1@Ie0q4orXG;f;9vBBYuB1=0i`75ZxID8Ih2'
        b'7;-&xeAp(f)Kt-xdRt(Xu1LweHeBQ&f%`^Et=W%Sv*WDUdZAou*)Zwv5}5(Qe}+Xj%Uq&od;$HLSK#M{4X0KCe`+7_r`-QL)L|NO'
        b'f!WS1g<0;)LmfXGs==CYC>yLWsYbXX;lfM&&9^vV!T@~3EAh_b3bw`q24=KYQR80}TNGM^yU-%knuR)NI1MWJtL!9ma|k;5>=g5x'
        b';k);!oMpIY>z%TvhrL(2k`d;qVFwGBDji9DiVs|@QRzA8SM3?L(3Wb<bBpt&-|=V(uOIkJSl=2M^D%4y$ycz|R1N0k4K)=LIc(fM'
        b'tkqfK-U*7C8v@=k2qVud>ew>u-U7J0$i8LR47~Oouogl88y_Dg;i{UAAeGwiiU_G+$EIO-5&$l1g&XSpL4|N75FHBD7I8=7u-gdo'
        b'{?a-KC2PpbU_Ads)EkG5al`GH3ohWMB_NCm)?f1NcaIHsJUU$e*l-K$bVgwOBD1%PP75HMxq=YfuJ!)D9kIji<)G&J#4kCs=}zYx'
        b'ikQ%0_6>`3l<RaTYTpPS<sR@oO)LtgKeZ~~xNI1<8iqtJS=13e><$N&T(mD8_WZZRDJD*ca)K6hsE6GYNd7R9w=2^4Gch{|qwjDh'
        b'@YKVqF<|$YySUW})r99JXU2j2k*QI@QE;)@guruYKf41%6y!ir=y`}>{JbM8?2q~m^Q(jWQW2d0GQighzI`{x5U?dMp!``r#5)<`'
        b'cp|VC<Lx2VVXQq#%aHl2V8lAp6#V9Xt|+E+Q2VHS@C-8z#~T1e1}!23DSf_Ho7WbbsjoPJN3SB6q^(7QX`KU!D{lrB$9y&jM@^I{'
        b'tYyw0WV*ejYj7dDQpViyCQ()+YiqXdL73~_6vwxZA%MN1=p(TxocRi-Yj6l#+pPX#sD_9ViM@BB;ZZH-Q@&uD(HqG&GM8bb?4zO0'
        b'qP<}usUO1Lk;JK!p`9-(c=ORFEmZ1*6M%IFQjRaA$bu6RC%p5GIe!nEl!WHm1SCO`jFU>(u<3J?U^_7g=~E@zVXP7#^VivPhw9%R'
        b's&)JUv$E)^3s`9pRd#x)K7QzUIT>{90=$A~qa?iwCU&SSb_lLN^4pI;0d2VkNm--xb^NzQ{+-2&VyjL1n&!@>V8o{QsPWt2+WHei'
        b'AsftQZkO!D^X88^XBT%J-ROR~9;n@Zu2K<q&d2#BN83?x2!bT3JBo)kR0UUco>XY7npwJe^#{jJ!ZVP^j$-1+5Ox00>qK<ehKt8S'
        b'FfoOwi-!(lzk8%4?vq!`_Y!H@2yG_R1w--SdMtTKaBMuLQOAp@gk}v2`X8M@VxCXAwpA{X$12G%CX3?vHCKfB)llbo#kaSL2gVn}'
        b'3ER7<<TrH<mPX&6zYxK-AFckUp|%;=cfoCO$FbIb0{@}lTVOMY;bf@)uc6KwMP04s1_n!BjYb+GkrRu~KKw|>FNfT}9I|H)HL%0s'
        b'`y^){4uz*zWYy}gQMRTTa7g{mp>J!;vqUXfVrC~CtxH*zsSXSYt_rSon2?Q!g6Y-|ITGKDL)vuk=QgPQlW<ct&5jMuFpm$eHrb@M'
        b'!1ekt<I98f{~Xv5D{P{DjDDjq|AM2asm-!9J9-KITJegc?H2!f0=$59aOc+FiLAhm*NhH{p}hqr+b$XSIUo@WccR1J=3-)pfXS@d'
        b'f>}e6$jZHy{`Fx)ZhEN0chKgq35~WDMp3rd5{+hURFY<G5oSKmrSB#>mJhk3h8pY!v50?)3kZ7|lHQASgbukwLAuT!GGyK%v0eg3'
        b'ex7v$l3s~)7AY=64*o_OTvgD^>0=XbaKM7dl`QB|^P8O6?PVEgbG33db)}*n8FF)j9lZm`D@p8_hA=k(nQ*?^Aw$}}?W|T@u7$^h'
        b'WM3UegXv(Kc*g4wF~-5vI|IeBDJFSzEb#tPV&x>ZdR5#zB=h`$ft?~n>l<-MCtw$)0VV$-$L^#`zO6<}j@J(lt`sq&gK(F5U~p%G'
        b'c-*@tZhi;Pi6+P(b1N?F9}GYkvt!|WHPbs7C0)2L)Ib^1Eb7hy4Q5l)c4E8!CnOdb5N-cvpdDl1lCw`V51|`7HvB#OJ7D@;3u;uf'
        b'6FV;eV>fRAE^VVg77BM`J|8^tEq^sexHetnBj`7SA@9Kd4qhW{5*KEZLM5_O`$h#cqN*{Q%&Jk8*xJRwj)yt83)f4UWO{!W1|Oy1'
        b'?=oBMqC#b2q$b#E$09X;@aB@kufzeZ*GD8)J5g9Z@$e{fb}&-2lzDfs&;j6p;2B`v87wUShPLDU#t73e$jcYnF6LF>qi}07n-;5G'
        b'gQ=$mlQ0c1G?}*`k>0yevJZF{@E?sKQT`fW)dT6yAJQ9?+5DTtHVrV?A+9o*OZsY*E*xZUOjs#XJ^wwVsm?B9L-W1o%z2xLISOme'
        b'dS!5z?6BB{9hP)Tkoo=+XBv%C2dT91!1U*k!&q7*k`@k(7PzY~Lawbo5zvIXBp}*WoP_JqxB$%l!k}J!mpr^3${<lj^=}6qZn+J!'
        b'X`o+m%Vw+$tW18dPqmh)%qZDWh4b!AC1$CnDt$VAko0fwR2!R6TaYaY!ar|AD~&}vth<4(Ym#Y{)ke@AxF&AT9xQ-+R}MQSoKMU`'
        b'lCU)xkg%#S-wZ<ag)AvR^`eZ#GS)^Z$notuUi$q4@R0_KQfL%_a=XRMHrRF5c`4`%9zMnUP!c*6rRj%HC?O>=<e`2a^{4$w==ugU'
        b'3N@}Bbm1DpdoD8lI6=;C*9T_!yYRGd6`)0$UAq0a%o<8qFU`NJL0w?vAkzF8tdu2+5%Qgl^<XUHVY5u^;7VEHaUatMTzcLeI5w(%'
        b'(}}miT=x76V4^xc&F>A`k<^GmI*Xvg5kN<phHbwhOOIZxF=i-p&8nP`jOSEKLNe%#@Dod_b?rn^SrZO$v6aEM14v1=k(6kHG7cVE'
        b'f*vl<wLX=qdUI*!_8aNzmgeq^dlwU%kquk6gWugqWoqf}8|jIGrF(9qcR!>ee6s09gDSOn@EKwkUTw4mSv5iF8q$VU8-+apRWwQZ'
        b'iZ>!Ord4I%&YB<4h&5jHR*R~Q%!~b+ptAga&5a_oO3{Q0e7d0$NY^V*Q77KbH8#m?DstHksrDIJ&zmw*R`+&33vZvGD}9;1fofxh'
        b'6wLp$a1?as6`5-F48Pp(@@evG7Z;UP*}pl^mo>)#NO-dsvz1lazdq2LHOol$1vY+t<xNHHTbE?jLF{SEsWYPbZw9tMhBjfrIR#xD'
        b'=?hAL8lxu)`Z+SN(zw4E9u#d{dOG*eqhb4Bx^b=7_IuEd2!K7mZGTSl`bX)GwgGqhfW3X7!SPHuBC$Q~&96*7zO6K;89r7)O39^7'
        b'QubU$W>LQ70(Hp<T;u^;po^@sLqNN#c%aEAwPB#$S0e&^p{q6y5!Z2^U<H>r#x)@Rh-3aXQ1Bt(XCO}sE($gWm_yD1F!s4va%yfw'
        b'rx-XJ>HCOW<6+goNV!Vlr`qCoINg?7cou8bAv-INfnP0hdR;ZpRJpR;R#4!;zW)8@-A`qu-xAx5HE6a5%Z?z@a}bjqh3h@l`o^qw'
        b'6u{ZgXJkcLs(p9vjqzsL;J#{OQkE^q@Z4^zMt&(3$bhe?%y%pJ%+t~L%}c#e6RJs5Ic`<QHi_YVqh1bqh7b>O)mRg8DG0!jph(G^'
        b'?UE)jm<7K5@H%tq{%y_A+lo@3k4^vl`}B3QtwWsg>4C&=K;KPvEb%Ky12;lvN!5D*5vXh$$&SDPu7JsoFV1Bk5frMz#fKvfN1l*W'
        b'KiV!TayJn`gxTCBL7r=3RqP@Fl)nBfmiQ>L^C%!r;wnTn<ttF<52D=HKwUNU$z{3qs%|1n(I0Qm+`GG);kmuU=H-<1ekmXcv+!hq'
        b'xSF|CW{pN0?Lb3heo18>Y6j`s<H9@E54hJ4*b@dC-gw1xUA#hS*}J<PS_~+2r4N8CwF8aK^GUmu{kUR3;FC7$YsQ9Md(RfwL{_<7'
        b'evnh#gVDCKeX;v&MP-l>B*_z5SIrEG44+dx!@#M~?gLCJX4!yvo`dYd->7@^JH(WwFfJXSv*dIb5E%wRWT-<2vej}87O8@SNRRfT'
        b')e4o>FE>3U)DrnFmKcj@sa5F*N!3ffDIk(fW~&v{vli-I%l^!*>F*Mhx!KD8d~c&^6A3zV0(NGT*hV<ia$ao$5`8NMAJ@f|LG6<A'
        b'D4-pzS@0f~RjqvQd<QY$77f_%^f#PbWNs7h&rG=XTTo%h?A}KC3KH(f+F*q%#I5}t5&|1|5q^h=;R_dsVIzkhYLbFMeMQ!`Zy&wA'
        b'0W0{5)4+6%Zb)<;CrOZt@jAz07xR1gKrbYI&;Js<69)ab779?W2`6RF%Ut-2+`?N5K;VA9aF#&b)K8jyx3xXDM&uH;!b^@WjQI*O'
        b'>Zw>C_#R9@?+)uO;?}q4EwS?Y`hIvSvG$Itcs`!+F3rL9wKpiH5B33i7jW(KCeqQ`?{4k4f7IW=9twX??2No))0KVDZz*mrJSVH6'
        b'X}hF^fJgK-G<193??2TrK>Cwd>m0N*XbdjJ8Q!7N9SCy{A_0tr5}9|c0N6}_@3(5u``*{6?|)#Q)^mru3u_Jm_Ls=PqTxTr&CBl8'
        b'&|Vy!-*e_4-Em~&G>hEdkF)pngE;})cF+j34MwV!B*uKucVD|(U~&z{H1+Wd8+@Z6y$KWc4eYP<Gn4nhyR-U*<!I--ci3o3SO>wv'
        b'U%#_Z-;4c%`&a`DF@wGJf9$tc_K}OJ&Z)>o?1mkoE;L_d4Wpk@%<~YGIn;lo54y%uQs#ZtNy>lTeF93#RC*CWf72f&kEfEg)aQ5<'
        b'vLZ#;Ac@)6uf6FnELN1f5tG{weNHj_pRqAHd>l3R`ye2YBI-T;8mt*X&?oyfay^x#MYBMb_q3I8HUy7Q5)m{BjKC)#dT@~tVRpi3'
        b';w`T|EHst=EN<M^&#!)@ZtI7;=ALn!zvQLI_)CPzm{UZo-$J+ukNi&LZZLp*oa474onn&udB9|xH;G`KZ_<l868hZ<{q}W$-<}J9'
        b'Rc!ouKfiKo9>N)8e`mSi23Ja5gw}hE$;07fV4GDP+t0uA_VB1$*I(dWI~CRw&9@$0PZXYe`r$ofEDODRuI<Ap^gs8>3;OsYYulP{'
        b'`w3&cz;hIv7cvXqtT?4#Qhs@2jj!YKbg8a_U7k;c%J~Hk>t**EUyClkoc-e~_^EiTZaGD1D2mD}SnyjY%X3s^p2bR)+CbKG!UF_w'
        b'{lLqQ3vDfYhfAd?Zl4`kW`|G8mp(i2lvbY|{2?4tj`aE?@8U?kKk_9GU-=*7<nSNVE)4P)xSao=4qxH&IHAtUgRl6M)Yz~}rG|#h'
        b'!$<!9y}gBR8=W4AR%03&Z#a=MuLQA4Rkl0TI%s3b?(kQodDxOlTVP2BpANkduZ>;*zkMN_Tqu}{alKGFp_{R4yom^=nU5i(Z;Z`J'
        b'8zzHYzRZVSz6bhLeX-AYv5%&MNIlPCWRUm51IB+EoBBc`g?kn8Sj>e!<9qy^!iDSbQMmeS9}j2og76=p29w=lxIfACc0NcYKX@R~'
        b'Slb5@jWvA>sYM;mOOlv3`^Yf95t1}`n`t7+Am&|&bt>Ce{&q7hLRRF1X`J<XpO&WRbw~(KV!$Z4j>j8oVpc33!rH~;@5!L3tmM=v'
        b'b(G?FXq7vPp;ML2o3IiGN>#euf9@+iE_aBK>p079g$LA)RJog~QpBra1$T=Zqhg{^K~%u%cl==WOexGSJJJV1svrpQA0UMg#Gcnj'
        b'7G1}ycr?jh{3n{sANzRCZ+{xpRTBfVs*FM=sMV)k+`#hh9OgkVod_eBXtiOsj_v-+T|`8z-!5sy7OC#yTpCMg(<;<E`*vWS_atOc'
        b'_}?Yr-*BGAoO*koal0^R2ew1X8@Kk|9TFl-)Vp683|`<6sgL(%-o3*k$e<O(U4BUJBjM%d41E7K{ss^{RGWlnCdhdiB#g1Kk5s`?'
        b'HuOC(_8~83KFBin^Tnf(FH9#5cN>ZoSRw;A+}9A6`s2Qo1bOPpKJO(Vj0ZWg%CJp-51Uj?U#5_a8^id16AyI9_+igNGfY6QSHXGr'
        b'iGBO--t`V~c;8<8q{rbjcoz`(=jnVHWgqFYaCV)M_fe%=>lgQpR-ycpQFT@FdcVH9TKRovqN}C#K7G_{Vek%CmEyq+qK~SA8JQ1c'
        b'R7$B8gu}(LRr39`!ut%NpwG%)>s|O>Sf{4)PTycAdhHXvd{Om8??P2&BfSscPO+2T_n4R)y$;s$pJ%)6p5BGS-HB5RZ(jA<#X{Aj'
        b'FUX`E=mSL@e}j0o*b!d``$<Lf1GRnDOSjwsx%Sh&)LRt`#T@n(4BNACj#T||udt^5<0ZoPhdk1l`b3ZAPfH>K7ppJ!mQ<=+daal4'
        b'kUo~E3U9y5F7(>}r&mj(LKkVdJ-vsud7tix@*!6<g?HO9{=N4IeAO|RNV9iZa$pCaBKWHeWI^U3Sm1Yr(bc=%ANo*`uLyEe^EQfZ'
        b'>Eu`N$vBcAgQ>iHa$86>wK4xH`?Q12p`OgAa`RUb=6}vNf1#kRQ{)OV7^Iu8&tDglkMVKmwfWlwxrkgzKFNQ3{t3T-K|ZtaeSQ8a'
        b'yZ_2pR0|8HItojCGfzHD{sfdc(c}jq{xNTSsaJivn@1~BG{fH-J@TAz;5>>DE|IQF5xPyN_w~kO{JVo`VNiWr_}P)R2LXNA<qNv8'
        b'iP~C0=3Hf;f<5?E1sS(eWWG92ZcF^%g*V}T)k|(3mm=+c00)5MGtSTEncQA77^H!e%>Yx72+FJ|W_}DQ4D92*a4IpGy$z=kp09ml'
        b'0Z+pliUJ>KwMW6kC>182l)tZ6wyn2RP(9KZqKDbm3y+PZ_D10#@ah~nlhV7Oc^2&SUkJQmp(ZV*Q^(4szP2OZ6vm?ukFKza?+E<r'
        b'yv;?frl{jBrS(Skf~E9Ai<L#rmdmWWksAN1(5P545Gv*;rG?5sE6WxtA1Y@@N$IijUNVXdbl5xLtuOMa#CeX47kkf6#6<P-;>EBb'
        b'AR>S+Nr(vB?0tX=cTU55iovnk;+ABrMj1~R=@Mr-Ca9P1CcovN)dpCs#NgKsyP+-rNh!G&M8uO^gulYdjz)xjlsL$dHqzfEZ5`$|'
        b';{Ycz79;^5rZc_b_GT%$`$;fmI)yjrvXCe7IHf|zvT@~D>n23Uj)F+RCd9-dF}Hib$l?6R@yzs0c;kG`To1VjB$AuSUkQoMcj3^z'
        b'-wlTj4Ik%XZuL-qj?wBG%Eo%MkEkuN&E#POH(0dw%w&%?RssASTTEo*9{WH~{Xh?Yd#}zW*Xk*z6Mn_Z_?{lQ%*M(MYkAo#HD2$r'
        b'@~ogIT)<k8-%~NnS3Tg{dJ^&45JXHtcf1cs^*RUkPkN4gve1ShiDE9pHj-f*Nm9pYgca0{l>fGW&;!2Vvw;cTcAxEbVaYzsMOdBj'
        b'{T}B19)5lRX42|}_F6q08Bp*JWcHY*o~tYYXmh2VTA-Nc<b2GzdlVBUz#H>qSYm^Bei+~E5zZOu!VvB1fVSC2x>{#$<8u5l&k0_*'
        b'<^*aY{6mb7bz5uS7vKaE==LDa&$vdV=UonzxXA$?Kyox~WHECL;;a4>96s#c#0x($uP%nTVE1tG9EXFK(k)!6(GY;lmV1)GMyOxt'
        b'p=@%s(?ba|pHLs^F}~E3jH!R$WBffodYHi`H$LBE@ILGew@i3j_%a7b;CY`jmvVP?;xj#Wbz<2sdjO>$&?n?h=EvQ4?*ly3^Q$}j'
        b'uuxi}6AV+V!mDbfF}iNb&f|xh{>FjkEgKZx<^{FQ{IVydR$)nygMqZ~>bYxB$f(zd=43_Z!XwQBugQ+Q11yHlWW|GtT_DjbV`TQt'
        b'J=Eufke+wt6#yx>+yl1Bj(n!I$w#j%t_WDj?4};-LkK@ByYcqF>Pi%yoZP~}yg69lYZ+CSXSgoEvPogM4pYAosu^ulfO?v3R7`9S'
        b'Uk{XicpbpFR&EgPXyY*}drWWf4@%-d%NuItrN?<Sh+E%&MaLerSmoLa@;V!(dmBC_VX@?ySPKw)F;vfbX{11%AN5$gMomm`Pa*%#'
        b'EU=gJ4EKbi0Jj9d$;DH`cDe>X@}hy3^UvwR@!O20>mKshxSSxYU>D-Je1}xBrhIiDuUN2@3}ZwXR*->6%$RsPET4;6?T96Zzq5@o'
        b'2tSdeA7yLQce=}Y(;*kj%*-pzp~@OOJPb^d9xIUWS(2O)^+b2sWVd#Yf@iwY9C_JTcPSWqZ<Rb4^Ak_mP`6hjW617%u)X)gs=w>@'
        b'Hn<01DSi~Wl8=HscZJY$*4N!kUl&ABY~Szk&Id8G(ZeUPXB>c@>>Jjr{DBBM2VvgvKz;QB4DD7A^Ktj<@Bs)7v?5frOntdqut*|}'
        b'kb}g`)h^36g;$J;V_xqDgyEkV1j^O=Hx6K*=`~by0v7Wlk>=u3yms-!qY*l+z{!zB;z^)a!de|%L;xm!i_3bs+v?y4O6=8gVgQyC'
        b'AQ$?^cg+1#xA+n_dS8O2yY-?lzIv(TCRWhFC4T9hzklL($>52;@b5V7I_onsQlfptkwb4~R(RaUx-Fqr%T}x9MMugnjm6ec4Vsch'
        b'byRg(eqwZqnlNTRqy_s@Gr6?z5%hIQT}yLmTXXsfQQ@PH*S<t9-L6MpC(qN-QIW?865FfSUwISt-I=-4NUBaff|6oiIy%B&H_CUT'
        b'?3+}rQ=4TZgSW578dzi>9etslxQ;X1J>G{*NsL$3yzSa#yb_DH6Qti22dce5F~1Oi*7$nu?|t3sZ@PGy6Z2Fz5NYbY-Mr-C$A{Oy'
        b'yzDulv}bqM@9u8Lz!)=Y7FrVSD*RVBe<fwB$9w(dm)-o6p!OZz%;P*CWOR4dDS)j>+0eQMqvZl+-`d^q$!#VH<~n<Cm)x?ab`MFe'
        b'i`zv_1Y`2tcMoE7_igcz=sE#g2%qE3&xyQugTia)@A~^{?^=)A)J=u5q<_5Na|nwhU?|r;<h|Ub{%JQA#>TAiXjics?8FTX9!y8!'
        b'IZBm!jR$0Cu#$$Qm?E~DeiNa>tkDWT60V_m%dX(d{uq`;;J(>uP}~<3AIw&-6iT1K0x`83g6XjnxQ<11+3?WGt1=kAgdppdB2v_E'
        b'^ow7kYPIL?!G1j!h{t0Z^qNuwWYUCQEmg=VMBDApuR%TJ5zfhIb*vuO`0JF2w$uN^00e-*y5Jah<35Tg_5L5<jEcz;b!XCYx&;^h'
        b'ALxhw6l>HVO6^A01tDs}bKh+O5|2lhVj3lhg9=qNqDw>8O>=;jF}J!NXj0pWgFGJW;ZdQ2u|Ch}1UtL<#Bav>yZBh!r(=UctmN_8'
        b'WqzaNV!u)0Uc(Lso>ecZuX5LPocr!ZmSQ|hsl{<!mcJGOp-PK_@F6V*-(E&asg|szSF?i3vw|;;T~*7=)g<lS|6#8fbdnrJbn@v~'
        b'l#E5&JV-1BD1_8|uV6H{$+Z^44~7PdL0Co;NP^V+x2Tt1RR@);gZ+Hq@FLd{(8f#u68rhlYL!m?5QX^D>Od{(PhtK#wZA4+i~H-d'
        b'k`81r@Swe|zS3RY(fA#Y-wm~5T&)DP0J^DNUAh(un2E{QMmkP6yTF?%19-|VA_UiNv&Nk4N{O|YF3QtbBy%@%7(Y~w?!Y(3u8*C_'
        b'6vmtC#7|ruLSE|Q{1%;foc<-&QQ0;76G=AS>v!vCao}got)D@phmdtW5ah4AWf&E!jbGOBryqp7ckjyLaWfur(RIAxB<5&|XI_NU'
        b'tmN`{M?4*W@YMgo^JIwU5|@5Z>cY(^VZ+OQ2Zei5#&xVz5VRRkg65I|?HD{X46m@~28Krx*Wrm<cw#ex01*sCmJ#l!J$%g1n-m^I'
        b'fEmn}^Mn%DZt!W#_+n0qaA$cs9>2+FDu|Ut!4Q|DoZ$~x<DL)#z7Yj{4jP3oYHmPC8L+Me*=1_k<o*8~uVNsC!s-SY;Hkz)OdFQ('
        b'J%`Avsx*3$_6(JN0@Y)i$+l;!>F_Revn-wthKI9u+<<#^*FLXSGHY(aoinA5man$y=^|yE{+b?(SMrW}wT^iNW?N}_rOsl>EUwaH'
        b'Rl2xyqDs2Bs7RL+=0g(emz?(9*4hVD5!{Y~zJ!TZMxkw=cSL*K(VqI{9{X~SCq|V0!KNeM!`DBG`J2*Vi!vs+>&T99k6Z1j5A(Ew'
        b'_V^c<7LnNY#ufZU=ygB<qOh;yTuMqF@>1wZS&kIG<(hG{<W<K9VV*RU3}C}5Tw+fplzze602qIYZ(X8yofFW)g`arRrmLhc+lq9@'
        b'^tcTx(lzQB?#A7-jew>{zIPGuwL1&MO^2<^ZVA(B^N=l}-Ah*M_!D<J(>izzx*UU`o<9h1327~I2$vt)9k^xzE&;%K{*1xJ>@-@b'
        b'T89FC<-*LvTuD&)Ueq@h6lm?`|7%LQYRN5^*qMkH%yRtyTp(1o@8Kix>(G)Q^Bym359d8^e67oUt;_y(SA%_-Cq$IvFEf7IWy<y^'
        b'2~&1}z!xsUoQE}l!5Xi|N?*3tD2tER*_w-st7zeIgd0V=Bk)yHt0{pG*Bz^ffGlJ><}Zi;iD3;|@;p0$vo6B<(jC~{e2ivM{v0gK'
        b'-U{YWn0YG(|CtCFXNc4JF86tWP?o)+%jqv_`=X<<%l$4$Fbn^AgbX5m49D|JOY@p!ZFAb=6>T*gbzSbi0f?s($2n4Jc)0=?r){&^'
        b'm-E}IJKpMYp8{F?3I@0*;nUwma2ci&EnG@=IJ?{|$jWQ&68J<7|LuTwT|RAIY+aX_EYg|fWUxzQ9^y!hHY-<p?@w;Vu3;TzUGCRF'
        b'S-ZWc3m&HN5osOP)1lhvmi0<snE7XrS>HOt(Qm(Xs=>G8l`eNNNO>o5f^%Hn>RBR!voHu=?6q!4d_|@TMXZ;%>ayiUSn@c$WDInk'
        b'$HVEem0taQcaEB$z<^Un;&GLzo`&DQ#<ZbS>B9fWO*Z}kgEY+Pav$hwcw?14tINz0Z4)#tFL8AIy3745kori$9G4R=*UUr!T=#Xk'
        b'_ky%X3nn?|9yC1~rPYM01^Is{`xbzxs<rL4_sjsoR%ZYag>q(KU^FX04KR{nM8!)dBt`7lIe>y_dJY;T8Rg7iIw*D!EeE5TK}qCD'
        b'0$O3}kwGIYJc(E2=73UGR%Ae!=>DIz_n>vY@B6?1N1s{u`@7!tuC>>tDebyF1@@72_lnllC&8uAO7x%IL)+=b?@;QpQa_*f=rDT0'
        b'NMVXhlR#;==9{u#E%Wz1$@;{)&@KKIRKV7LqdCTh1$+9Ol=yg(w%FsarW;1<c%Lmqqzlcmd+5X6DJ;F^R~zi3zg_wyv(NL*rWx1m'
        b'I%Gjte@18@?Jl3f!IIAdyL}lK;X6`^N}Bj7q5c0a;8oPFF|vXw)iM<>n&)Y!aw&~tMFtT^Gg#;vONs*0htaQ9>RGXZ&5YmK%s_y}'
        b'Y_(lp!Dxb*#FdmemwjXTb=TMt6|SXqJe(J?+?aYhUlUXExjfB<sc_ZUVXaAI#iFDwy65sMU*U?$>C7v<uzwpPQC7%#<#DbAbJiyQ'
        b'QTO7NM&>%_ab&^~_ajqHE4`{$ded$Bn(IS*U}^igUbnkmx81r{UGi4iHEEo>bOPPoyKkpgO&I6par8)7<5n6-JVNrQC|fFPv%nUR'
        b'OzB0s)g0-3bM3#TQ`*iu_pYsG8_zYhU9<mqt$Ob`+vRKBZPK;?N+{==u3fW#3tOdl?ugP#Kc$tc*X-9|t*ZZpha|MNp7J=?@r))+'
        b'c&q7aZGUhi$FYT<-Q&g<l<Wu|OYd4zyUc(zDyg7X%A~!+6H`FC+d_4a=K&K)!6mJP&zCmN;XF4ngwWdpmXXYTN=*z~#u!gu8`@Az'
        b'`ESrLpO@~I)CVdPl&PS>#2w(vngQaY8MFrNP+GI<f8hPp;{DR<nKSC0_jd|?b<Z{XC&;$l_TDwhkpC?ed&8k?_9|G@P0(6t8><b>'
        b'uWLGZ&3*uOUkLXKL9$4oBTR)%6DXAMdUh|zt~;_s*tk8zuLx|0vcT&kJ0RUPac!Vy@Mtd#x6<yNe6SZAy!%m<%R|h+I&hfJt$P??'
        b'GJ_%7Fd>0EkXOx3;!|?hIxAOa&GH$0mzIAiJ&B_UWh-2ad1CqLHQB;tlNf=%=Y>9wcH4B#zUf+ZX}WF2wKO~0O^+g7Xfj>18)3Ur'
        b'Y`4;2hMpmEXY?v*{;8(SYxY;*_;<=AUBFOg29N~wppWRm7|jIqpqY;o()dILlh#X61}*F4INs<(bo}uWcC)jwWMM$M%vIPVpCB;('
        b'1a`(B?C7Z09Y{Np+@?(XnIvv;#bEUc@8j-*j#C#{dJcnE={9=lgxcA0x&!WUKF;)p3m;6nd}RG}l9=!rUuqWir*{d%O8zexHcFex'
        b'(5RwO(ose8uya(Qr%22+nr?rVUgAp4n~_qtAB(xp8s2B+?fO&VzNN^Rrv+X)>6(4YwdxOs*?g{*9*~M1VB$4<2<(Q7*FbB$80&M&'
        b'#Hmb}O8TgK{`sbduGz=K*^}<{d!7wDHP7V{VvcEx162iHv#a5hgz*Ma879zENaGYRl&kbUV=q>`_)5bwId|yBjC+hAmHeSjV`D{0'
        b'<qvi<AjFLnc~e>&Nt`+i%w`$y^Mz}Yv`qsNm2}@`$^z4(m`B}d{KHw)^r=A2F|?#+9o@6%;jC%R@OueXMz{*Av|sonaotDT>tWW?'
        b'MWwv!iF%@0!t4(eNLK2@G9{<vrS|)^oi^+qL{3+MRnt>bsQEQQfn3;4-wJ1mG6kayy&&y5-e<yXAN^e+dq2^%YIf#t)t>TyN3Ev&'
        b'BFX|eHf;{w+Q_mX?IGUR&}Bd0WjoYWU2>*$2Y6q13m6|~4&%o9LEI9i%g#L+*La`r?wQmQYVUHJ-l6cW1bt&)m;F>%^}ZroNmuDV'
        b'&^I85qRnc%>?dHmTkIQ|OG&CAqq!6@ny-a==;9<6CfxUt<HIVPl%B_EQg|~1PU9imDcJ>iG2QJcN}l@gw?>Cq8H_Dy{R~)^@jWX1'
        b'Ju0mKgFsQm7?yRK9o-egC*iJj$_}4j1{0Rit)cfNN_}kokK!G4;8E+l>_uHwMP0U+x~M#{QEFmmHu|Q$<viz-AdLT1j%yVzLqab!'
        b'BP(vsqcfuHg>FbKU4{EmAc?_y=}ktI+Z*4Y2l{B|d!Jr(x6pa!XqzO$enwh$zS>%v$IMn3`y41mvm)-i$Gf{@b53K*VrKM9y?nI8'
        b'xMBY8FK-#XyQbQM>^@mNFCyQ=uZVLqO`qj&Hf&m&(V2HLb*U%kVp{5*x^&dmJ$ZD`dJR)@(qB`<m>K^fLtbsOqTzf^Q{Ibn_e4G$'
        b'xkvLeQ(}wf<{fuQUFws%baeS1<3*ah$+loiZfYDUIhovjaL{y~NsUVsmNY15{TH)evV1fXNq3W*rboCqL_WWLUf2DH1>B5tx*B&2'
        b'*VBlP)KJzv%o2%z<A?StP&$k0vd45)>AP(DF3oDGNj=)fOsdsB^zLc#JucyGuVmx2F5&SoX<9d9I>(sY7A7{3vU8=cO2O1#rR@{s'
        b'+Z&|qZwl?Qhjvwkb=e;4(qu@7_ER`72pYAT)urV+(iNeP)0}2Yj=9>#chTDv|HW+Ab_v3N*|6fNRX;c!rxaz8O`5JRzFc|q@@^mH'
        b'TBYsbuI{gx!B328nib)0YLYEnc*X4+O&3`$9=k@5DGc`9#ui+!b-a;laAdXp`)9AN---&lbK4#(8|(6eaFbjQ{l(O$zMb#h%h*PA'
        b'iEn2Wo)#{}T`AO*#6x&VOHzOT?WG1sjI4{E4AKf$sR{2g8t-&kR%{*<EG&c4ytAfehTeRdSn`FN=6xnzLMMzhtZkrk>(NpRbN>xE'
        b'5;EBkmch<C<Q;meQ&?;k{0W{gVT);@mL-AIbG4dOf9a;##i%ZJ3SZV|9r{H0B3}Q!a6j9ws}<~KPhX?eF|=LC>}GBVubI^S88g#k'
        b'=vu)18l%NA<Q6ejv<&hcVJvhAPeYk~sr{GqbdP&|&(JyRx=uRom!gtRb*8*_l_u}*7b|?>iP`8_zT*+$Bdu^>SGIS!k3Z*Cyv|&o'
        b'QJ4Ms@)}sLi*V<>mWRv4Wgf>;#mb!meJ1)27e4yZI&@DTvv7NLr~j^k{Ytt6S+f!S#G>#s7oPTBXZhB4ptIY=;I|aN|LoKVzuiX0'
        b'R@|9}-;z#^kukp6xxJ)Qe0B4^&h55N@q#DVnTLTX4ug%kPN1yKp9=han4?UwrQEo)(^0M{FWXwJ*}y=$DQDKaMT2I$9{4qf&K6h3'
        b'cJE|_#`eh~8K?AWZq~;N=h3tsPdTS^Wp`0QAE0H8n>vO1O-vdP3Yp(5D3&^N!{#GweJj6mqp%M^*fdLO>cH@?^YorW8{IdnR(aDw'
        b'`V*$HrRn8P`?}8RlD)R)JG&=IA#@+3wl8+t*TA+^<lH9JsE@T?+n03iw&WjaTHR@13AYdEU5|w}y0%h8*TTzUc8&FDTHa}23davI'
        b'xX_AGNim117`DqZbl2#|UO9)(%uOhXTZjnDjK?K;sv^aB=9b-CyysB!Az!T;MQ^9#weuh9**|~NU0$4Hy)yqbY0RG;6|Tpn<72wL'
        b'2e-NB-17NNa$H(sOUg^>_8NTJ-JEjFJ+DRG!hk{Q7phhA{mgjPz<iD^iy5z=@n?Rn#2D7S4{6B3)tY(Xg%h{5C!{m)QrfmIbyBax'
        b'qA)(u>D&t^zH#Sflyu(TlQ6DRSYaOe4u){5v7(jnw&TJ2@5ky9O`1--rn4%j)8^8td01);>=e4Rmd*myo%V5^Rq9URS<?G=@T_GL'
        b'zmq<=ch0+Ws#=ISk@d0t=E%8Ix|UJ#4q>~BpKyUQn|Mg3`qm-zRgrpnnWo{L_7R;`BRXw29Hl<e?icTfG5Y9#<2+qdB&Nq9j8L@0'
        b'uNAue+EgMQM`VS9Nd45pSHn^pKmWWVrj+(Ytt|M^pE%apyCx~7#tPqT<4!szE9Oj!X?MU5d`4Jz|2Tk(hPHn@x?g3S0j4WLe{kp~'
        b'QTMO_lKAYe1;VNLl%oQla1n^P(VX*(aB8r=n@>3`I+!CeA}m3>4$+Bik!;gder>%Qovy?)mXGsim(=^0J_CN?u+-BVA>4NzlZjl_'
        b'v0qV8ZZLl0K&Q+6L}@KEl+I$rt63dIirqVf4r-}4e}UfO(g9MaZ{tHxIfPGRV&Nqa&d&;WI~F_W1(<(k9yH5`ju7D-WgM%jaTM=-'
        b'P$z2Pyk;b8`-elbiZbB)PGSIk>d=zrKOK}50-XMxmUFHOmXs|xt%l4QtkyN-Qt%U+KU$alhqoHG`pby!)yyAlwQN;^qwJjjJn&!8'
        b'=Ycu@50R9vV3NO=B(IhlS388QUD<BNWe!KMV!ayv9G4VZ)ZD0T?k&^b4kn8%-s!&V%tuJmI){Coqbl2Bo8!>@Bynt3R4sC>H`9B8'
        b'x6+8+IJeDyDVuk@8k1;Mzv5OFMwhoX@0OKlnUYkd%=72zjvG@Q|5E0^EsRs2jD0f5hc<ng*FL|Hl1DuE`N(?84T*CotyeFjV^yAK'
        b'g~t&_^Egw(KsXo=-pcuUtW($BtZ(MaJj=$?=%r=8LhLnDKY4F2Jh%yWWjQN7PH2hg94nCgrh=h$x;TeD&QUenVH@p8>ypHbb<icl'
        b'(y7b?CULc+f)&_Aja&7X{@nqL$fb`<x^wA$2=m0V*z-AuC`Wcb!O(ca9QMhMswoZ|<LGXaJc#Yf2eIYcLVTtEj4o`)P?V*w^A)o0'
        b'nT#l##{7EKxqcifK37b9UgWf45n+wzo5nfp;~Z5=hwa;|-IpW@C;cmAX%8_a0iMRPb`^1K9?RB`cP;}7l0?367q%LC8@BaX3@>9D'
        b'RnOJ3lY-m68rq*qQi)@NqFimeM(Ojoth}V#lSU|3AUDRUuH|IP#kujytj0p)xvN{Y7{=%N+>$-Gp=)PH(#b6%C)3siPnqHD76FRT'
        b'8&@Yx;yi^82c{gsxUh7FlNP~<OKkKktQc<QWu9iD1ReUgOm*ri<SFs%1jjBKd$Q)F=4D=#?Tt-W1#XhZ8V@^lo<qF)dCGZPuG(9!'
        b'R<&HU*{*h<k~HpVx^mTi>1tK;)%xG~7@M<VHU5lB;Cm%%=dhq!+Cd4~Bt$8^!H`&7^SiDuUd<>`pJT%GiJa%m5s>R1bqg96W~{hc'
        b'GfKFG+AOOz*K+=bi937}NbN-BC!db0oKU-~+Q(W{TUlf%TuRW!^!PETho0o8XP-CSbjpMeDCM22yUpB~`?B_bj$M%*0vV~b#JKS4'
        b'@7~E=dDZ#&>j<VXtd!mwB0MI;rKy;qI}-gjh94f$wCk#U*Hzo%tJNR;SXwQazl4T^$l`%un%fAbS9{Oe!EOpA+aK--pUk?1IzKZy'
        b'Vij{{i$a<-*k@LW+SAEGp1#WYfhgwY>U3F+%dF|O$#ZjympuqX$Jn@G5PGc4@<SuVK%8{>SW5Rvd`6u~?Y-Q>MAn(thNXJHok9F9'
        b'ArZBaYaLH0R!&Npb`{lcPF*=E+%jQn7^c`i5~J>_woVwngO5lBIml6>P?j4&I}ib^9~ip7Ciz*;>9rSRsx$>^`@a;zJNRw3{wn|9'
        b'6b|-R`2U)J&U^VJcIJ5=C9glji|6juUnDn9Rk?L&ht67j?WIm}y(-?J-rYwU!@94bP6ZOur}`wMj;?S?b946d3YKHP_8J+yn=S3+'
        b'!%lirUsJUK&NC5>dOB})@ahSk59mO}cZk=9dKNc4=z#21ZoIQ2(K|hayF-ot?iiA3Y}Y!Fq3)X`^Lt4qM6I%RN4Rq|Pm(0+N%s}n'
        b'>~(IG<1~|qYI@&FoqzXbV(jjSaPylK>Bf0+Zkf5cuemug6pK8)jh6Og3k_a4o&=AP6{<bg6{Xs~=r}Ibd_}f@NwXL+Oq5`Tg>GwK'
        b'IbD!lI7#qMh@cvVv7PA943Km$y4<Sqr<a1JJ<NwTbco`^qQY>W>5}dq{^oN{KXllC?67^<QC+&bd$VNC$JC2HnCMSY`BT4~q>Z94'
        b'oH^y^Ug!5WA6BCIfv1<dbadFScG%wQsQ%!g?p#TztwX%Ayv@lWmDNg3Ff24bIW5w928Zq@{gzLkFrw*fhrOwzs;R@at)qK`By@X+'
        b'bGfP6Iljc~=@4#s5O&gd2w&}fH{Qky;#Pi%+Df+{bl;$p;Fvc$L`iPry_hW>Gd0eyunvvlIkga#HcT5vtN#Sqnp)vfdV<W~*ilC5'
        b'-7MQzL+O3L%<-I}e4%Y!hhw4QxXW|p-JcLNfyg4bQ3YT^E{3$+WJ6Y?IVHVgWl_N!xd)n^$)qXfYui`Sj3&u4>XJTN^n~{Vmz<83'
        b'3px5e!wQ+x@(smv!T?X_8%b`7qx$kaHTUk#U(+GTj47ENH$5M8l$k<teQx!Ll?fp+t#z=zmM5yI9md%m!ZcUdCN}HH@TS)~?CU$K'
        b'aymAZiJMvk0axp$46LOFS@2=u6M_bUc7zbdBUY%+*=}ib`9CI^A+?HoWTZk!F^2K7O_!+P_sh`UJ#~k$=*r2`j)B7HeF<fCqR1F}'
        b'y^TtZ!uz4aGU}I4WnDBRY3<u@FwRO?sCe#KvBEy{e=B)m?c%i#`XYg0{%AU8q^e!w&4$fy&lZ|%?+~j-rA-pV<%pA!bt*5h+lC7b'
        b'7|A;JC_)5=mHe^NT52eLhj61XK-LrClNfoB?t>_(Q1i#A&5~5Lx3+=v3VwolO7^^@{>P!Re$(!hA1X*<H39X}<=a|Hea;arR}s3e'
        b'O^5{jE!b;BlV6A3zoW{(!*;$sZN9`5FsiYpX-tQGbVt>g4!Xo+YTye4ICX%xY3ZooF$WSYzo}2sJB8mOB>~?47OS~7@5TKmLtEN~'
        b'd^zb<;+U#H7qjj$s2bZH^rba}W*gx=H?@juMlr{o`PA$oKDXQw)T0_NHVwAh@3vRnZMRjmcgIOEHdyKmlU__8l^H%}wX^(X3gf!A'
        b'a<f2^!Ebpq{nBplX|MXFedaAbX>DZP+iCZQkUYh1b7)07YAh*rs(JHUk8DlAaIl3K54PVQLIgU?Aos_R_>X9gOHBkErQ-g%ozTK|'
        b'=lE(N&PN~;1+uXS+sBGiA51?i!t|qX!YIF@!j+>Q*qepT30k+bGUqpKAIOXK?e_Zis?XbPFSU0^N>Z}h=?bc*(Am`UpK7D6{e}=u'
        b'5abpNvJa?0wC8*wl?V%z3yLR;T~BvdnRex#bA5WxAY!x;;qzTS`OnZ|ti^>sCnbM$ig0tjIJV${7$iIhBjcoD=V^la=?my`?K?sx'
        b'{byhgef>{PdZcpkKicj8Xs;@0w>{aO_J}0^P}7_3_O0zz+uG?j=+Gyfm5W+WIL8!Pg`0e23+M<lL-<uMFc`9g*?M8>f*@bE9zC=='
        b'zqIM~cKiDFs@L0Re#<`)k*2lp7KtPA4OgMTUm(Uw?PX$v?-OK({cd6xwgpk*K$9EF4QWdu4thEp*SDPtHJr@w=iGQhR-&0eh%4Bd'
        b'>vQ9GGX162q`Ld7WQ%G7^8-20@pQ+@7SxDX`ADUlGSKQef7^(5dS{t)(P!-Cn!4_Wd-wU1-s&5EczDy}?e=-?wt4MKj&}P>=J&OU'
        b'a|_KHQu<fk@`Y)FcM+TC`Lug@&HS*H-r+~)YS%}8@ph_{-q(xt{xhW+?K04N;UilEF>U%YG5*pPcS<P!EP>wjp!dBBoj~tm4=sHb'
        b'(rM}I_vt<6QkyU%T0y!O@oOh|CwV^QzHU@{#uo`Iy_fI$%i0N}d`4r))4sU)<lAeBe__13R=w2Ku}QJgtZJee$X+_Zym{C7tuI!%'
        b'raeoH=i4Gq3K<9&>OayAEO2VMbN*gpD4k1|f8^#Q*z7_4yiA0%ZX6r)@3yDdI=j5u?p<Q{jZ6tkk#!dka|$<NV17eP729rO+s7;N'
        b'7)OV)`>T8VrE_D`J;xuIqZv-p#|G(^l9=6X!hVW8X-s9Ccv9knHh~M5&O;iUr^^jK-Mz2rR-64+Th*;LTVb1qkqBoFdfJ3b*cOw}'
        b'AKUZ+<mTR#AKF0irPIj#n{AMprxD}#ZA~}ZR=C-3wxxXA_Jh>lgDYR`l6K?ne)<N?3Q_(-4Tq&N>KCNplYJvn<6~<%&+x+@s`j?I'
        b'N9mp*M1xvibXdxHE;`gZ_o(Vp+f3mMa8q-ey}8ZS+*WN{qZwd@wX)KFUiD?0mOX}m_bX+5iW-%Yi%Joy<V>6GOxt)xJDbOJS((y*'
        b'-9w1|Y-3B)7j5=0+H9u~-#E=L&QDHAXX2J_M)Dd<U!3IJOmhMoy)*-S_fLFDopfy~iA-I*c7>@sgyiovv4LS$X^2^A(gzOR*J4uA'
        b'?)_1l{o^*<hlqJ++7IlSJ#8FY<{CU!70Jw2<f*=1I##oQZ)cP1l|d7jGi*sPy;e{2-Cf}Xa65ZO24lC!J$itf^4hoCwBpIH#+@-c'
        b'+mfW?rHdsG^{CYny_#sl=Auh$9wTN`1xr6}uz|rDUzt<4Y}|Z!c$p;6bG-hztXoSq{m6G&35ep1^!NxWXZG=l>wjz7)@I+<X4}|S'
        b'z2{7K7b~t!$E<JDN;y|ShFdpEq7BPtRcnN%FO4LqzED%!YIjor**ukA$==;Z1=iH1q<b#mTvQotXI#qI<4l_0J)iY=v`m@m?OO`1'
        b'Dmx)@ooDx__so*l+&6#9mfqsc%qx=gB-Z86<bw=$Q!Gi3U}ru<K8R!MXOOou?w}lnR;ECx+iJCoS#id--R;vFP*E%Iv;KCr35hyf'
        b'$yyZm8+KDCpPkx37d~CqHy(EZjef%?PWZJcvCY01MSE_OH%4F1o%7%39-qHs-N(!s_u2-z&k`AY>L8<08FOw)_ZYGECf203yPk3R'
        b'^pgr!bCEwVha1s8;*9I@5lFj}Z+osu*JjtZRhI<Wo@gumip}{t*(^sUGid$0(5LE2<3;0yHna0l5Z{7^-1+LZ<WFi#G$d{IJzDpX'
        b'L-O_1LE$uoR#6k`V2PG_``q^~hxxfB8U?98#0Qxl{o2fKI>vKFyL{Q1WjwOSjj2(HwQ?l2?fWKmn_Y<#zUb0M87FEZ=Z0aOe62pP'
        b'zF7DQd0CnHxia&p0R?T~>v!?g%jj>epeZl1E;}E5s~Xm3m$%v2w(7l)rPZ;aeXY&`Xe_CaXxD<goPA@fDbF+Kc3xPXo^vZwJI_he'
        b'?@(@e`uk^kJuTWiuc82pHgZg)cKr0;FW?UOu}HR>(uX}{)?0jwyduZv1w{J(r^jvXWxh4;pB(9*>AdT`%+sPa>x(ArA5-QVyqhWV'
        b'<%SjMg+bdx{oq`nC`%}plC+e&r7Q0~7@mS!A%P3y(|ETT`n#gPH5Xg$=UY<`_GC8J)-{eyZj{%S)Fyl=jepLNyimSc#<?x8PL3QE'
        b'X04q%C2~fnU(4*bB4wecTlF8Fno}OB$&rL?k#jD`T`SyHOfinWBHRSAy{^?(*E&a?Szi0<D+L9~1-s-0<+WSN<7Skk`G=_Gv#NcX'
        b'j<(v5w%U%hR$G5e`zLFfN&M35uk-pkzmUoD73>PnNVO>XI_J3$=C%V@{&4-f(YMvPC(uaVl_W1Ejde}?TJ8H<ZDp<Vj+U0P@k>dN'
        b'ggyJ61e4vEy{(;lTYqkB4jpLG%?kOh>zfmS>BHpPTthf7Qy0l&HhbTiIhK&$TSU9~5RyJ@)ES0umUx9RzC#l<!{z3tkwmmDO1TpA'
        b'?flzo;JQO}wWKu1+?YSGX7f%z!*`Oi=Gx6i3gd-sy%jFT?^}f9ru8ZkYHa1kOpVZEJ~(@aE+lL7Xa&6};<Z-$x>nmdRL=U+B37?v'
        b'Ojc$sr1tFG@LeOCUT(E#w%Rh``fBMeHq3f&)}awiYg_FrTWv4EGAHeA)-QIpr<k1ct&kU5>Fj9I&^B@|G^2IS^c7O!Mq~1*lV)f?'
        b'NNTk&ZM7{%JiEKMv#5E<KW29G7)8@xTkX%c+7jUM9$kniV9lN$<~+|vi?OsNkF6K3FH>9j&DA5C7Pi_GT5Yr7b#Li5)+%H~l%rI$'
        b'TOs-us0}7H`M}o;(}+B_u|_qcb$4OeFhq2Je<wQVfN)>c6AYu$x6V7JPVrL3w2JRHgr#_^Q$`upl-$(zd13aX3Z`03)OAv0B(4AO'
        b'!XA2YsM}qUe#%%)*j;D;^;r1af}B&jg>p*33v=8I3+0RN-=XnHtFX{k7)P9AVG1!$q!Gg9{_i;}vA@w=rE0aQTF<4ByTiGMOBdV='
        b'8auq{;a2;@t+sKkOZ+si55>8C@)g@(uGlAC*<Dy(f@a)xj4sJkm0U3tWPMuA`F?VY;oR)+U8%M*`;O655|w79@MI<NS<F@$uZUL*'
        b'()UU7l-v7SY@?fZt1&JFf65kGNrB*3e2GMSUvFUO{@0YPS4uu0m`-*l|MtB5ahDQXQd;tF81wJ6*zdGdTkC9nE!{7&jipVuTkOBW'
        b';v@v`{p?~%!UtrrGrl$Jugo9S41tX9b6E1*YWL%=h^G6`G@5T)?B65QceZOSX@6%MKW_S_#r_Q}zNhm0es+aqv3M_KaYBgED<oOM'
        b'`4UeZG20+47?SA*@(_d9{d-xy@e=%&d14|u)r?tU`6LSqnXwX64D*&eI*$0Nnp$+a3(6w7PCPs8E9UY47A8V9zgee~Dr1=k!6KaP'
        b'@_!Ha3DVkG`~M%VoQ6w|Rs3(^5C}n?;Ue7pS*7!Q-2Yk+5$Xd3Y5Xw(@IGUHOVzfPycFZs7H(MH8vnAq82`Au`CLPuii^k#<+Q|C'
        b'N7S|nD*7S3ER`-$d*s}<?hmOIkLP+c>jk@sW6480Qf_lTHR@p--rPV3mm2rlqL51QK)Abb;Kt%EwrGL#;GFaAk(DhDHAFn)iWb|7'
        b'79`w|$4sDEP*}uhas~=4_aoZgcUdcL%ut#`9$d^v`^}$QxZQs|ZojDI!E141-%4o7`R>2D)6e*)7TsGh;+NccEw*_r!jPv_E+{Xd'
        b'dvuJeFVi!YaV?zhgYnxqqeT!`g2w#1eR_+qZ(+Z%iNGyA^4B5$Fs<dmLOi{<Mcu{uauQ`kuDC6UwuA0jWqiDMV_&t^az^@Tb%n&3'
        b'a9Ln#PcBPNjp1b6>_t95n?4H^J}wkwEv4DlR?sIonWC6H#yFGuUOy=_w$^W<CB{W~d*19Re3RQBH}ptswRS2urr;>8m+FkEPK$}P'
        b'|6wuj_ZIsbXze%HFEuxP-z+*D5v_i3Kl^)Q)8xxJKb<`)AF^pS*Qk5i<(1#=aERv}&4Q)J(Wl%iBX{I<(Dzgi*&Oh3T!=;ZrltS6'
        b'_X;&cRI?+f_au++9gbM*j|^gRMniWJG{*^%bR9f_@YX{LXB2VO>~O)ga(Ax!;09&8yZ~dyy8^k>I<O?E+OK#Vt*neiH|ROaR2~t6'
        b'(HOPb+B)I6TCMYL6tic}D>O&iWNUBo-(>|y<!93s$u9`&gS09$wA=eH*=JrZNdLXnp5`HQs+HgV<mK=u*qMJ3PWr`#gk(A0;yC&t'
        b'dj%ylOH7KXxwc3i5-D_J;jmzg^P&sUaQ|)Dr0oZ<cr1%gX9_0C;e(^Eo<=6E_Tap9OLuG!y!^C_kPMhsLAqQwQ#kAySIBZPs>`%|'
        b'anCJ|e==96mWNDYoCld{m1vW~4$}OMr|U3U#$zGGtoZn>_yplJqG%a<@e=hRR8w4tcr;Q78yD(v`S)gRsF}9jc;R#@wGrPaRyq9$'
        b'){0QW6{lH|K7rlz1o?P^E`1I=Gl=xhVe5lQ&~x;nH6dK+L`1K=A5=9@@_VBq^zbF8SxkoNgy)eJLXJ4`5(8TEy??CvP--1on=TJ|'
        b'LZ}F8jtEUTdntL6T=@N+t;_q)v#_dAx6AaMC{e%n(jRg*@jr65_0p#1`{9Z%(aSnZe`RPtPnsU**`=0Md%34dd`73ST>&mhY@I}s'
        b')YtAJJY~LCB1s6q*dFw`o9Q4=Ty+M+_RP#=GFnF#+6>|;QSSr^oA{Pg;6vH5$#3Lt-*?GikQS_yhnN||W`XYs?`$scNT*-WX@z7f'
        b'Ob1DFau#Me$;*Y>ptc$GXT^e43B$Rb-K5~g7<T2_-nt~j8(+j&*U1aS%PnGyE!#b>2)iw_vkJ`e?eZ%~&Y4!$lbbl#8vzDWOuOsm'
        b'ee9-j0?EgoU8vxE*UY>Wzb#j1W-`-<4&%lazqN*M7QS+1WMwXtuesX{$M{5{Y+1rB6)CryohM?Yf_YuvucG~L7c1BymjpFQ(8y6|'
        b'brLpzNzEk83;!wJR>sXPczfyb5od-~Fjtton4<ag#z*7bi*&!>=Yf{_j&el}b0ejEFYW&m3eszL|LC`_d5t+{(^t-Qv<y#Suc>7w'
        b'M5u3Gp`FbXBr|NCVQOG<@=$(mSWts&&TZnRD=64*FeKAqa^ujL=EDs;`-Xz^GaSi{ak(T!qdUszisY5z*gLbhCgw!5P??26uJkbd'
        b'v1Z-<r|#3~3PPNVv8LI1W}6bNK8URA?H4u1BNs&%eL9JA*9XcSQj-6YxS2ogod@@|Sv-Y7Zu7ve&O59;|EOv`o!<ZrW|{EPG3fKj'
        b'EKZiWHs)Q~It~4_JTrOO(&LgdE)`5+3MovH8V}GqG=1icaj1+DK6CHaCdbyUoFoi8^j+WkW7)+s((1Y-jAZX${BK4w@Be8e+j;Rn'
        b'MlwO320zZB1HLx7fbwH7V+bJ0qOc({Ut8hDIxBDeJwLWZU#@DuIAj%K?M=CKF+7T$xmbL?+u6}Ggw2AHwCiT5D%0go|I{3zN*R0E'
        b'=}k0?eAmqR)SYrXMfGI^wNK;{A00Vq%Q+tcp-9Zrfbe*_{lrC&$;p!#<Ta#RDfr)?t$SjJ@aDR5IurWwMFi2!5#KB?VY$$cE(#C4'
        b'Klfbx$2-6$LoiBJ-+zr=n;mwr*2$w6IC*ro;6HTLMg0NdWURt?QKs5+(RnqO@Zfod^1(ypT1%+9+4;(;MI8O^4*||Ngm+1`5jodH'
        b'vpOR}919j*baFZ-J(6`9Px@y+zr2WEk^Av@cBYnyp15X&svq;;)w0NRLSMT0prS>qkaT(Inu{S1tRfUHd(rkmi${IDICP#Q=*Tnv'
        b'p20{;Mb8>{mpI3!{tH9-5zN9EAanrHx$F{s%tO>)zf2F0i2BJFXa3AP%lo_FVI|}b=KFkIG!_&J-Itkp-5JmSPhkJw8&S2%snnF3'
        b'5mA5E$#cvY8*U_EXh^`&kipzoYNjKDd7xb;tWcWiF0efBLJ2!KoAZs&%e76Q#9~<n)^9BmSiitP@|MvqmF2Op@L(<I1k5TvNo1{c'
        b'VDrKg3d_zGE4Z;$eisW$bK}dIO0(Q4Eic<9TQo-Mu{hqaQ#g8Acz_fvlsku=oizdUW8iV#BoR)6EIVsfaKjMKnG1&fxjMwNP;M2y'
        b'F5BfRqj!%N>=f=1a;KM!ER+|#AuzaQ?&9S_#t$x3u+F%pN$h{}@}s=-?noyuHm84+EfW|qWstLdgx&O(^s^ViY3&CtoUO?PldZka'
        b'WYgbu+x(EsbjFzpQ;>W00nC!+B9Atuy9<_N`x_UWT-$}-+bySOhKG3Rq2Ke;szsLtc3Qz!I%gK<RM#7>W>yU3^anoGO0zWpZ{lQy'
        b'aso?s)$t4TX0KV7ow=jk){;@R`GV7&v3<$~=XFNDVo%Wuvxv}X7ly7`j7W98<`$+VVF7Z7<bO@iCZzYsf28-qgY?GSPftwfq07Hd'
        b'$TfofLpm9rIaIbY_gA<Sh?6Ed7@1$*zWKr#8I=bVmyb)F75TEzSli==DmLAC@4O*aZg_)n4rp|1KwP?U{RM+~@;W`u!W-Gk!mtO5'
        b'aE^L$tT?m@G+_3G04-i@R-&wGy4dJd6){v6H?uo;zZK~CmQN2<_#2rE^d<FVMwnkFUMM+0>$OlDBs>{bBpx?K$MGL}ep<8<c52g;'
        b'vL)J}N`aY|2*yIKR!pxjL+hNg#yp5K=llQnIOTtgQ~n^%7!sytN`#{$B}?hBzhBsDdETPte9yS&{7}%agHEx;dDnTt$)o6L_ky?`'
        b'Ic-z|*=egiDld3PNSQiY^ydzYqlRY-g$Y&7bdS@uwXv0riU-lq)#I9_LL_wuPawQ?r@|S<(n5B4^}!7VTXN}uwY0#jK;{iwghmy{'
        b'?dhxBJ&G`iE+~jCun0k>n^P-T*Nl+v8@xGHb^HA2jK`?QbKAF{cT&SS%Kic-tcnnCSy3;YAat_s@A!J*qJPo*3l~9DGk@WKC&wga'
        b'JKx^HymqX>Lq`d3wT)LQ1Hl5hVanaPWGr1;FpO8;UoRK^n#KnYJw_TV&<N}&{CD=Y)Jw)>L1c5U3cr}gI!VmkHt9muzlADwA6kSE'
        b'FQ}_KKXfS_!lw`m>&R6IOD<|HV=Fjs6?ncnLl^^mFR%UeEOp*G>Fgwh;73t4>(bOBVWX2k9ttHPdb5v|C>dGQFF*2p4^TUfkjQbe'
        b'C{9E4y$Yf;H-zhmjwEO0osP~(JRKbm40MF+V%x%XjX|fQPXQ6Zr=z2`oQ|HH6t1fT=rXGoss)(HMd&taPDc|WCzeNvKJJav(L8^Z'
        b'$KTxuq&u(>=AU>zJ`mwe;kr1eq$^xk>p(m`O!E1sQ{_D2`H4t(0T6gPT-SUK=_BmMXTx=Lb(rU)X=Cyi7KH2OAur3|kK1@U`UdiU'
        b'ScTln329pdH{|EkU&D3z3E{esXK6kSI%1$%AqM)7-$3>Jh9rc~L_8!gYc@ULmJD-o5G_LwUkrOK;>uDJ-Jg($MZjNx4L~sv_Xz5A'
        b'lvE#ryljji`dT1PPxNhoGz4`zp6IQM!*x9qi9QqgFhHL@f#{PTCwfCkxbDKBL~qE33V+uD4)L@huQk9an2%`@e=yNEpnZ@x#uw=s'
        b'VAqB?NF754bVTouG%JS5qW04KAn&d@gbbjZI_QZTArVlsP>v94MlBphn%+S~A3K4@jXM5kxX%AWw1p?pZCV6>5?Ry?s9Erz@f`Aw'
        b'c<%!KTF?UQt^>nZS=4Q)y?_*cAA)%h`X1mW;C2G_?nQKEUxn*#E)CbMqIC>}!ruU}A*yF&^k9!<3iM9_?*fUy^8i77=}=z;j`+!<'
        b'UW2*`*a6sp8;EB=)XK54s3_z)0(lI9>c0Xsiuw&iKC@|=VP71HdViAWlK}Il;kq)!ZAQJvpp47lFSo;QI_lM60sR@qpN?JyRKm}('
        b'KhyRn$*A&V;$V}9^q?Jb0Pf_uRF)h*B_)rBG9VNDjl};RJ`VA=0X%<?KZQ8<E(zE1JTpMZGMWrI1-Ao0GSX>;yEP7Nz6A9J@F#d)'
        b'3-jP?&<@PKb3jXTXuBIua8g-RJnR+#^8jC<Z7$sA5xov5{wvyQ^Xce(#2W~|EyrY0zNnKdv_TBa%iup5cpf+ae{s*CK7jaSwA0f>'
        b'?*{cI`bx%KiGJB2(dVNs<DpLm%KpjdGmbL)OyIy@8GSGOM*utTN%Tq7e`>f+xf*?BC3wI;7=0kz<Yv$c@)ZaDS)kx&^aa>ufp3(h'
        b'gzE}2!gZ6CjJ^_ixQ?`~f2H-kKGybE$}fn}Nk=GUQ3al|C^Pb33y=sxEKnIM&lk{gBEAFgUkRLrzr9IBe;8P`7->PpWG>1A`!cxK'
        b'K%EEPL{N4jmFvtYr=uq#{6?rDUa}}}zz>Lmng5k{vaFwY4t3au@V$T`h33%^J<mfH6$^dkG~^F)ECF(09!Nu<qGs^U2&n1l>CulM'
        b'&I@RR^mNPgNt3>eAz;F8$)}^49!g2I8whF8gDePxJe_H5Y)poKm_RG&xP+c4L;yl}0SIiCYNSi3AAZ9u{-=9<8RC-s%=3n~EhI?@'
        b'OP&F%Mc(i5L=Nu^L--#DdBU)Szb71LidG^FkuxL{=`2IO=K=rtdH}_xH%c0&^}>DhCrvf(m-jsRchB6Z3lMKS@D)GE^T)s8=Rtn}'
        b'<!c>zS{Fg%B8Sn3CZ7bRXO5Od)d+Sv-6{AfL!B>!|4P(*CFmqys6*FSl>NklO;oRpX{2pJWF+<^X!!)uTYzk;{~R<n3Vb$&(hSBP'
        b'AM|}%??5ry-vS(f{xIy1hr3JxKJtAucEKIhFx@}PCrsN5p1l#{!C)ZK`2rI)gx2v>fA^F;Ipw!EQCC)-JMuVoD@|WQ8o?JHP6aOm'
        b'<bVNXDJm)&<9<1S`i;4Xw4|`Vcm=csw|M9y040zKSSkO2dgCXe&!FZX!KZ&f8Ez82H`G&5GoWJV;)`B>`}IorIe>Tq(GMD^9@wf^'
        b'J@pg6AsRR_rEcvrNxy*~q@j(|Pe<Q|`x*E@2mH91=Y1KeJ_3Cy3Fbdx48H)C2R83V{(NOoGeM`nfPeb;$)d*cvZzrHgC_v7oGhvz'
        b'_P=~2i>h03I@%8W3H}$tt`_>#u_8ZCg53h>51^kffu8oqngg<^X-@vK6m~^GG2Dqiqi^(M^k#3O>x5m)Lns&e&bQE?KwNdK*oS|D'
        b'*^W4GBP||!`tJA0F|w$Kfqn4P096g7!OwW8*(lc(s4>7y;AtS0+5=fYJrE7QUqHPKTmya{BaRz^u%84(0D52!@Nc~=Dgo*u;E{jH'
        b'qEetP1I{5#E07NT-+(M&J@5*U3lsn`FUz9df*SM;>IG$c5Bdt=FwiiH(I0_&5~v57fm+}K;CBycqAl{#1~*`K8^P#r4hNqEj&Y3s'
        b'tUIHx1!_?D$AH7Yukd#lkfIzT03V>(o6*OjKHfnaTF_@6rey?<LH`KUP#_YR2E+n2b5LHWvw*q4Gr%I?d0-ik0jvVn051ct0tVm>'
        b'U<=@m_TC1ykODNb1uy}-V5U5f^1q{?hhiE(%r>YW0RIFkfscTrl%{}FKm*VSGy%I2PYG}d`WB!AxCYz+egJL(eZT-<2VLBOdJov;'
        b'5B?9h0V9D?z*s;9?9xtQCPEDZB7oVzGe8oM3@igOfK@;ykOjN~7=Sl`ZNPTmZQvci3VZ~d01l(xlkdo)&Ol#`{Io*74tx!K2iyTT'
        b'(7ZRLd*BgZGB6#eLI2nSwGpZV@Rc+AuVC%~z5{+ld>4Rz=<iW~Xnzm1aRXFusH1_gz~?Zlq4pq-Y|zjk)CHc5-i?>&LjZrE82vEn'
        b'VT{+XZ}Wm1Fp2hi4@Mse^;sYlNFGOJlyQc?L;o^x3UQwVUW48QYy!3cPoa<Ogjxi=2Uvkppb~!fLp=ag10MrNfjXLR;NQRnpygqj'
        b'&aeDcsMmpSfuDe0U>@=?02Qp)s$+@uF7y)E4Fg61o&ZCICZZ;zq4yg{$2V^>4r%}}9(auM2OtJGfIO7}djTu(E>H|efmuR%1%dyb'
        b'FgQZkTD9_Y^xz80`!n^akQJmaU@n0=By_NZ2$BT%5XdWTPzl^NLgi2L{CdP?0`h?UKp{{J>;*Omc}$s6LCqKs%7Bk4?Vv9Oc@T05'
        b'`Vfx@-3*u~!Q2V+Bhbe{?+JB2)Z*2kC)j5oy=6cI#?WJsAyga@WTN4K6nvI|2Q@4LFIXw^?2N^XzATQ>7oZFSiHzO?br5c$6OjL1'
        b'cO?C1B_#NcgbXZV^c>3L*dZmEt3e~shX7~)#^}er@%?-`^pk-IK)&j9bOF>_ApY-+e*QkBgSuJ<B!34f1#_)4jq|1zBWw<l>LD*Y'
        b'dGkfkAi{YAS->jb)I`L!4KgJ3J24;F2*1scG5t3)dZm%kPtIfX*>DS_em7wp@gn3H?6LsJEcylTV=*y$|1HS-YQzD56CXVt?Vkzy'
        b'L|nx{2+T^jX%TNe%oCyCjCc(2V}283Eb=gj`Dg*c9!CC8106s=;Qbb(p9nuA;CC;=X1#nmx_Qm%=%g&fx%PB)1N4o67Wyct-cZj%'
        b'y#VB|p)_QTo_6xFNXShQ2N1_;zya_8s-F0*5y#iLP*(uEfNJ18@G~%CE$9JQ1mpmFfChjEf?vdVgR;@_H~{)s=ygB?c!mpzz>K_J'
        b'05$?Gz%d}_FxmrZK41W9fC6AIa2VK0%LiNmvVm4$0Ab?)9<F-{`gv6tpMZI=lR`~Gddq-;w`Ec7a4-Iz=TD+;&Fj!V03GblH0Glo'
        b'8m8BFzaE$Qs30p(owozD3U>kw$=HOrK$3MM#b1DjA+Fj2loi+rKOE2oyHoXy-U@vg;wgZd`8eb~s0%{Sw;?wUo?-Nke}m4xLc5-2'
        b'^tvX{KHzqa(eH%6Vqjnw<RS}r3RD(|LpU?s^Wi4H4BA56>2Qw<h0F%KW*`FkEZE(IJ_9OUci8(4cqz<#fx|!+{4~R@7y2Hc7G?*`'
        b'JkSFuk7Mpsi+SkLa2*-sH;}=RnE=SR=NZo;S=6Bt<ORm5(CdKN&@YBM2kMJZ{{(dp)MucchZ+x6x*IeAH6H2`sH>o^hnfd92WmT1'
        b'Gt^(9z6sU$9rO#Rlc4T~8dMCPg>+M4egQ~?{!a=*njshOE1_*7*EK^{=133bBt08wy&%uon1v|Mz9Y(G6Oos9q30z%8_YkWUk*M_'
        b'n%@!T9N9H@(Ko@9EZ|dQkUn`MSIWN^`mPf3B)7ufM5NONbp=#6<mY9mu~3%-N+A!(5a@Xe%*m`&?+Jca34Mn<I4bn#ps%!{j|``g'
        b'vPgfV&JFd-p^kaD$q|R<UGPJMeGckVFt30*6@|z`Uj7FCZs0Uf54&Edzd)V%9xW3wtcLmzgz+9mNHDM$*(rqGS5S{by#n<vRHT{w'
        b'0`&U#X`YpGH_|h52I#~WWqtzua1HFEq3(t{2kL343!x4`{VUX9E96Y5iBMmMy3s1szq|%2kMg}XijX7F_duTyeHYXZq5cHBCg^XX'
        b'F6yAxj-qdgL3V{&0QDNwSE1ISepW;M1?Im(mHQCl4>bXJ9C|9Z9YZ-ALq+=ceFgmvplwOrq}eb7-mq(cA6m8xP`&raqS_u|^@9kz'
        b'6K=;IW%b#xI}dycGyr?uBXrixaNTvxr5fJCydM58><rgMK|eW@B=3AXT<3T%T<4w4CTAH)vM=H2+KQY`wlj$|ndj-Q2x;;L1J6sT'
        b'c_iUUvXn%b3EVdGTEWjjOn(P>U+CqqpA1AmA0@cCB76qnqX&4RlaS<fbp3^YUx{>BrEq29zhI^l>{A=}g7*Ud0=@#8frut5CqxfY'
        b'FG*j@qRs{oom<%H=!FX6%R#k{#az-LL7r<RgxurZO3~Ip1Q1_<JpO~{uTNq1Whl2!Ka%W)dZ0X9r$yL?SLoV?gp9-lkWfdumU&M?'
        b'<|1qkkO5=@v6!c3ycn*Nf;Mk%MgGA_b71yw1bw<@6Srw}b%0Cu2RI-Q@I`&@LRjVl&^Oc&q}Pb_zK8xYjT7bwK-oyk#}AIAYgQvs'
        b'OkTq897|Vx8QKn#ULlV?bjga!N<BO=@Z%i9I_Xt;R=6%1abzG4f;#s>S}TBXU;yDV;5LZ*qZerN;|L9PA{%zxdW;c(_CwG_Rk-d{'
        b'b+~RP!h8vw0E!W>7VfRkzXJK<seLq$cK${l>L4&e=MSJ4o#1(l8_J&d5jQa)-Z}8M4Y-~~+c>&bi8vPc5naT~pg*V={=(`L;r;?J'
        b'5pGt5Szw^+cqATG8()lkWWYWdhy!#$1ds&81C3vW>w18xWuSl1kq+u2AOxsv3fE=Aj~S@l7p_y5p=_{U1~dZ40Z6XNH$WxY076c}'
        b'oFgN;8u%*!xVwlOXuK1yTXHX4cNR1fQh|6dA0GI}oi}^Dy3Jp`e}`z%wi5w|j!SL>ZUQ%e0iYMq6{GJX5AtA)#ka$C6A@?GYvH<^'
        b'NUs;jg1HU+uo!+UKqcxR$&ZkH)Y*dT;ks<3-HX0@6VL^s4uJRI?*MH}gnxHG=G?$p{@>AypdOxqdhv0I%7eZZ>btaFQ8#AvYYgkU'
        b'vh|dHoD1|;bhFrST@B(o4FB9pR-c2s9qUHjWryqbB5!nk;pVHbgL~QQ@C$?>9y`n}z}G-84O@<R6%YzU1A|n62l37+7w7+U9(o=1'
        b'u>|Ha-~eEOxfrN~o(E!~j|1lZ6XO677=wC+s)YLR0dcJ(rvh>q^pQX&@F_4G$N*jfHUc~7oYxetqh;D#37&{BZ75qG)QvFbLm%=2'
        b'tKYc+ZH)S8K=~`7PJR`0_J=!!)ndbCl+zflivtb=@rW-3?xrf_|8K0m0d_Y)V^&I&u)qE)tJgto>_;1;oy!K`4#dJP4&V@;#kj!1'
        b'?bu87TL+s=3YcVm+#o-)maa8|@qleiti$|w1H$Y<deNt&W4D4Xz_SO3Md+@5hPh0=EXoVWaf{Fuz&;TATp*-D;ERW*LLU$O9k>ZU'
        b'lMzSM=a6FnGTJ4o88k7-|BUwkD!NP})m!0j9Nex#?E_9B?dhj6Zvw6(&P<rsKtJh}{OI9hpj8F>Eodzk@%kDd|K&n8g1!MaAb%VB'
        b'44{SnChABDH3|J}2@pm7e1W_|J^VBH$XCBadBd!OITk8|G27x#bRJM801L<g88943@!iDCgTD`emw<ae@_f{xaNQWV`4_VKSi}<t'
        b'IFPq_G=2EdVvLXj2DDW^{49VP54QyXJ<a?*<mB>r$RD{>9_H^XLHZd$7Epf>^Z#?07Xo2GGcX;f0*Z^lPu>mJ?S|g+PPonlHG}Gl'
        b'!gULweg=?yLY5$%yU<r(K)KJOPVJzJW5Sphvt$g?0vfi5>#8rxqJ986fx8#!Tori$=t$PP3;YswPG+KP=-*{3v^`KfB0^Vd3D?PQ'
        b'VXh80E#R#aWd`=LEb7m|LLdiaGXUAZN@@oF1~kL(5-aHY3TV1n7F7Uj1hRouKrvwW5VU!a=i6c-e*g~PFzkDQ$q45^3vCaKk%iI)'
        b'@sq?5UdwNAB^*o!jGzrZL}x|1dujdlNRoA^f8SP&M=eMnNO}|U2Cxis=)gDW_d}i1e2CRsPO<v4fb=s~9|0(<SbY-wWF2Pp4Cej>'
        b'em6pI1t5xSxCdmyJr?q<1@Si`z0VGnY|k^B&7=qNIOgIRuwMolI0CBjPsrbVhU^HOT{r;q$TpPe8_4K@Kd=hsd|*{O>IBeU#TW&I'
        b'0F!|TU^Y<PPW#<YkjZO7KOyMXj_Bp->FM+tSYNoiT@}}H^C2_TKvro3^3~`=z+~uGLB6*_&4Rn(ACSRNu14TFglj+<uA{!6hyDQc'
        b'M}ZXRvw*jON|<|o=6MtJZvnk1TNw=plsUlv9shH_o8h*g3p}?=%-=GotAN!&rqhnr%NpoM2GiA+k)-z{DhKz_Z^!pA3Pz_)|NGK?'
        b'o6kibYDnIy-BKTY=au*4y<*QtTdqOIq48X!{sU1b{y^;@A>O)WC~G{*ZiadjWpkbJSlz1M+{p{TahDe&pZV-Azd`vz<dvNI#W9!G'
        b'l9XS@EFbsC`R>bxM=nhS?bAH9AnuK5Ynn#no7W<!m_{dW5kh+OFMc}mYiI!dBwq&&1IgW>>u#~^v<?cO=g`iBUqg1NXZ4lyC3*wo'
        b'^4=S=s13b5PrsAX@74616#ee*`z^u&zTcrPzk3i*+;?J{r@qJ73(#-0bX}c(gP`mB7rqzgX7u|fRq01Y`c0dDr~2a7>@|WGf(X<N'
        b'%_C>iIr$0tEvW_i5R{jG*QVb|U{AyF;`fu=(exV%Pz(KubE-)ja;~sC0OoJu_U#EG%oF9cu1mZp1$|(P8v4!>_k)lJ^h`q%)DEN@'
        b'1pVvuBo-0Ad5QUi{ak>`33j;GLVfyIm|c-?`VH!z<>k}px2nw2n@>DhUK33yh+*!UQ~u=Aq321mn2wTuBh&x<?6ieptES2JY@PPW'
        b'>egwyi^d4wpPq?$Iof*i-6!JVH;MX(8DXYJl}Ah>#AkZ4zGQg*zfMf?T^kxrfO$tlCyn^7{iB74wnU_OJaLqML%Q~*kIpdibo5zZ'
        b'dhC>N0=VsY<1xd?+0!@PR!3*hcwr6;-4=-aO}`=Jt6&=1AoNd{XI1oPjSS7Xwc{`|{A_rN$H$){&Zmlsicq$==!rj5zlJA~CtB7R'
        b'0`vLPk3By5@ypeIKSeyj439sOXLgH17|dBVghtyYMrWwhlQuqkC47DDTM<XXjgfI3|C%~3ToKhY{Q0N;`r$jD%;?<{(GWCts?UlS'
        b'p4=OJC<@_`myxkN-wL^G+_d7Ch&k$d`0G4>3+C=<euD&U-*ZCIqP{k@q9FSF;V%cyeRY5I{HM-Z(}!0@|4ljXvokY3iRN=jVc_h#'
        b'=-~_L-^J+1SFM~Fd${Dp?z<fck9Jf<uil+?@K)ua=ruk8_v+Uii$3+e1;xbJj50+4^!pp=#X!G#W((z}*KP_EvU!!D2GA-v%?3mK'
        b'NkY&r+h9NGEamAJFC05oUR6{3vpBb$44S<OeH+{^Q2zCeL{H~+^gC@0WSS_<lOo{98)Md5U=~p0<q}2rm(X=ry4U1Su*(PNJ`pO@'
        b'EQ7ujIQyMMzW@;CT<`Nd-4jsuvqVpiThcu!QmEIFX7VkGe#<YIHv*nOGs5nnDi8#?qEYES6gqdL>nkC>7(d-zqSDhLqt6ib6`Z8s'
        b'w;579@21=(>fZ{Ns94|`U;|JH90&FTLvzs^NVgbrPaEKdvCjcFIzJ-f$71#-+}-vG=BLW>cXN**13cvoyLp&*$7j;{vxI(FkG4`i'
        b'N5^YhxNZ<?n5RqB(|{X5<sGu|bhH#0nxoM9Ng2XWdA+zvoGUmCkVBy+{VLHfL%2z(<5N)Se1v}UrE?KFx1sY9ItK~)O``u6?rQj>'
        b'dqSd4BON8?VmipF@c<py-+zhHLnWQx(Rp4R{2Bnd&qCN2gmK@uQj%-{2p|W%0S@p7lz<M90&dg~<N^BrNj2T;X(OB;_eE)<ihBe~'
        b'imK{g{r>qSb~z_8*7XaAHs#OL!~4f&6;jOt_^OclP15{THCLU!^c&498snjU&U4EaPGShl4WaiIg;w@YEw`F-^Bd#}WvM~aIESh)'
        b'YdBACq`kbqs=VL!&;IcY_m`flN@IEd@7^OX>)&41FYGUqYds5xHE7j_Ez$yWh*GP}`L@7J-;)*|ho*kt?>D>Ums#9`i`*=};YE_!'
        b'Ne}gyGd2yq)2%E~8Z9*L{IL#qqT1Qd4KHK4X=jFWe>U!*_MBTD>pVAVlKO|mko*YqTGxT#b5<g^D~}K7#-_dCSG?ZDkQ%8eR%+IN'
        b'c`7f~oQil&vEFGL{nS#a{vb0)&G~XtW!#QOo#!yCtqfwATUX(cw%o6HOAX6$rA9wBD>WTtwy3!=&ZE!|_2dkg^ir4G;+@xNgF|OQ'
        b'pJIKg-D8&bhpy_ENT-+rlqCMUMZOOuEL9d-mze?{UUY<Bf0SSyvB=lWwyZy4>BDIaD%cldO6jX3c{UF-acl9CPDzk9$jOBG1ZmE1'
        b'@w<1-U(`>|erI3Yk5**!Bt_@bR*&+TATuuPuM1G--7+rduMQYj67W!7N$G8sJ}_+6ZQX2X?M8)OqAiG(8)B9E>Dp>f7jAmUQ4mJu'
        b'lpXXab=pmD&Wj$WOSiByJ9w_NzJ(_d`Y?%d`BIOF61%SdxO)ZbkdV;m{>WRQ)A}PzT!!vBDzW+-pQP<jyv09XS*<h%3ym_YXyrC{'
        b'o3`KL-Z+~cQ+(IGY(?T0K94@^DTIqi9eg(Qv3|~6^;my}q|P?xUALF>%;y4TnHu;{9%5%cOujhZHJqGdrI+9Pn<GN8CHJgZVc23Y'
        b'rMj3{X_%D{_f6%7&#e<0_-VhV+<jW4<~cQNp5DCj%Q}<ZyENU;%;vl21#sW)vV=Fh*g2}dIklRV)_xYtxockMjGp~gtF&?|vt8a_'
        b'qBRu=rwmFmOq*B|cCy*!Yd+_fFufEF9(ItKsus^2?g&w4IcY7-N=Y+P6&c#Sbo_p1YgGjkso*@*#%rtrJ3{aD*#`Se0Vbs~E3=TX'
        b'3LB?QOHIzO^MCE*MyHOFQ`dCmnwx#83*~2AITvn>$(7WM&Py{d=iKu&9$O9jbDMtXGmVn#$`xmYedeZxa`Ud#8PX$D@)oAQGg7$g'
        b'1r@U;-=vj(k}>kQv_e+I)TJ<JtOkXJ@k?L(xi)>%J}!9eLOJKVrnN6>(4Y<}bmb5S=eFw@GtbSCSDTl%>zLGdwy%*zZ<=9tJuc1D'
        b'm`7L0@}`)V`=#eC6eIMHSo^tugJSdBCsfsaoU2+*)}~3<d4{f4OAy=IG?%q%Qs()JX04~&{wYW=J0WovDgBy#&Ha^yG-HTDo9dUI'
        b'cy8!^H)BoTAKsg@ebi_CsPA|0yH)k&+%Z=74ed=1E$!nx)Byq9Z}i!A5Bu)ErlP(IkJ5M5=G@ToK2=#?h`EGwH@rbl{_Rho8)o&#'
        b'-P20d!cm>Dy(Gl>=%%wBN&*S^McNe>oxR=t41=h&e))6M3{l5Q{|CO{lYl7`ng5SIogvF$QN#<6UKSoC1;P`T6%zd^2ANBbZ5z51'
        b'a#f#+Rh9$<R0jl(&QR2;C22=h(8ETvU4{9x*0X`Ft&^5oRP}d;?k0bg7CCesD2N!!YfaYQ_SJY9U#6D(CEQqJ)=(XVX7+&y!vYAZ'
        b'mOhq?GKDUobO-9(l|6=@$G<(%Z#U;#0MZS~3UYTj&Q>tp9onI@vka5=v)^%dTS_12Rr-+9KcDlMYcr<P_&E<QmR8B^`H@UyXk<+3'
        b'`)XAAQ+-WOp~}-XsWApD=sP~LYp+}T$cmAgU2ui{F*PTpm#Lx}N~P-b*jw|bfmDoh`?f#c_q1%aD|d){DDxZTEn8qo;LK|4X^%;t'
        b'jD5N!a29v$^RY9kzqoy7MCF;>x@B{M)`$PLx6Yju98p%dnNqw8Q@qcm$i?^JjL|fIndQplqsm(<&n}fhcni+kr1E;reYJ=F)b&Kk'
        b'Z`|Y(yYdy|itV#)kyVlQ$foXJmE6bMnLhjYzNYbgCAL8SJDhLw%SydwmPdNmsoswt8?Haq^MgcpBiEtJ@|nz7XBhNSGV764Ou9&%'
        b'jc%(SpYYjrk9CRr2D#z3F@48}*X<>mVXDwydTqb->H{9)M(LLZbibgodG)1jRfVx6#<MT%<hLPdxuJ4UZdky$3N|&CHkRsEZ-q>)'
        b'R)bX3bdx?Jzp>bvPOSXwk8<6ggnj&r>$`@=L1otcLC4tCyZx(PlXj-<Ua!F{+w3Xqb{{W9vp-V2Yr9N;MiMtQd}oy2T^YXY(ULm3'
        b'@t0myn_dmdRxU~%t*Y;>3v{hk2bQP<G=(Zr)4g0p2_x+SKU3IA7jvw)IuK12peay^n(j0eqA&%z&D&^*m8Wm~ipJbQW3KO^>6%#L'
        b'e_K`7yIDL~dW*Q}l*;W&;kpFj$r!bKdqZ!5S}r(L)ekuDrZ4n#58LAiDUt_$8&rZgelhOq-4{U5k(vjHJ3Yu*c)FGw3&N&{HK*>_'
        b'ykof8v#^Bh@}0Ula$L|r90F-hD1|zJ*b#cLH^eL#0#+eo==<TmiqIXs;g(AktnrYL-&;HhE$9sk@HJLaGwnlkR14h-JAdPWA-iwU'
        b'uk0ku<~^}dya~hj9(4+v?-CUd7Ng|6!eS<buIu$;XU9u^3w^&=PUgl3{Pr?gs8mcKq2Gn*u1nash$<zSFu$lbUU*BF=)Rl3t5>JH'
        b'PGS|JO=MNf&fW;SZjwCG&Mo64kqVP~W>A1CXwvc^FFA^ww}zXsSmokEIPaO?^9CceSV-@EFqovK6jyx;YgsdYV{d^$Dlb!*tNbR#'
        b'3*!YR<Hi=0?vU?hY_Io<<4^^YSC!VKDpRz}xQW&FiJGbE^yzOt)MLn{alS<FM|;9ZQeNy0v1WzE$P-+M#>AGSPzv;!;i|VXI(^7m'
        b'D@pi_cf6s9H~$~H-aW2~D{UN~%p@U%(I#9XH`~mFKtODhLFH1rg`g3Yb|Kb?u6=(d2%_6=Ev0I^>~3akLqOcc&?;ElCb3kYQUQBW'
        b'Tf2xhUKV$)_I?E<auEc@-cXqDb0*k!fA8o0=OpL$oaa2}InQ~XbIv@+ej!b%^5QO$;^5L8RmP&m^$p)F%u%&_v5ZAI;chpu?Yl2z'
        b'8AVv;GDYT|?KPQYu6Xpeh`!$58H`nX8&{vrcQ-6*xUld{zWbQE<Dgo*PhF?VsPuwPA@;wnw#@$-@s3d>La%mV4Q{od9D=@^m2neh'
        b'sA~PpphDV^bCZnm5*XI3X;=~N-@q5G4rhcYmZC}Bix+JTw?^D-d+=tXqx7N(lYg1%o?x@lKpO792?LZDHUaFC7d?R~lQKOM4d(Pb'
        b'`2^-3GR(gzxDoq~XM*lG2QAEEZt7R+$?YL2#l&WBPzDpPB11rt08Yu8d$ZKdn@`!j;`Ljjm$%17tNs8pC9?br=8PZK2a+VC^k=ts'
        b'=*xyLb)LD=k-mL+1#@UlM%p_mcem=pRpS^FzMws{0I6o0*4o<R!A$)BoQS#!ppB=xm%Mmj_E=qbaXs!^gn5)Vn=AL7;lAkJw@vU{'
        b'aiLMkemUNL@SbL;H&Wi(tne1do$He~RUE@j_hZS+4y56}H5hlM=Lh(cgK=K0B1*=+1|eSjbD98R*ST?|Nz`-k9GPqv_=t;=qetxR'
        b'eZWcfX0iMI+SWIe&`98$H*U4uE5<lCU$GbW-GgbX)fdH>=fZf~TjS?veBog~8Amfn0R7fDc{c!W5)D#S^+yrh^YYj#;73x<o%v}}'
        b'ZlBt2AKLB=AI$pM(EB>(I;;5HQ}K6YW7N@Iz#C`ThBp^}?m5FA+0~RE`x6=USsHqkV-fyY8s71~`slnCk#?`zc<OUsJ(4ELdk-AJ'
        b'9X>w!SVabIN`zitd`E|yI{EJX%C=qOT+qUd<_pbA;P>V?$Ye6c{(dbNEq|>1!h6aNCwdDy@37b*$53g<ucht(XX#dP=NtUGJ5g?p'
        b'+;ITVK-IVWTAlqrtG9_wqtoR#{aT*;Kg+j^O_u}w-y&kqA{tZw-?(AdczP%bXcQO?HRI`K6fh|0O*5psKm@Y?M5WWchU)PwD0R`W'
        b'W8Ce{0*$_E+-s9Dw%;2n#~E9m!3kl$5Sk6Pabw{<Sry|(8<pjNkQPEs*7Fc*g)lzrISA(np(^W92xnz+<M}(`&+IHagm-7HhA<}U'
        b'uMqxK2*a}e0%5oiDzeHUR0?5e)}J9P&$=JNKW9Ay;WI+`$E<A-K4zr3Jg{JFT-H{IK9aQs!j)Qs$gGLXnmgWBHojV%RXR?}jfIi^'
        b'5LH)(6z#?}T*6d)Lm4;0*#2aA9Qw4?@EC;K(v~r{&Hf@Bi0;`mZay^DAPzUAj@u4>;LXOEi@1@H^^}a~EmDx*qeio3MnYlE3SYNK'
        b'kt<z?5)`D^m=$5nQW>*m<>Y^qFupWv=?X~8mmBj*;|enCha0<Aj+4^NGIh5_x#@W{xhfiS$k>i%byH6J83h-EU%z(4UajW-fH#K!'
        b'7>zsr2XjVs$(BZWgRxC3W2!E!RB}tP_74@@Ib-E|?;_E$cROP+HgkN<Dtoo!#Dn7<z;1uQ+9TwTZL{xCkUJ3jt(2R^7%LxN&63MW'
        b'$(9}IowD#7ZvMwu{ZH)aSL4s*49Bv>c<V~#nxC9^d4Dfn`UL4;RTl=U%Y9OGfabOR$#jg5S;?JI#}pe+>Ea!@=|4Q%b%T8SBi(q9'
        b'cDzjsBz{OXDcSOmq6?dp?kyeNTb0k2xn{}9<c@l^Yn6OkBw4>_7H(RGmE3JnVU>4x&ctl)x=oL5`}0PbO-6QYEe%m`*n|5rvAQ{5'
        b'FD(rrH|)8qd!ur1ad)wD(;qucVy;*m)7AMf<~=9k&cwFK#y$ABe~ri^9&Za8H_9<{2nK_a33^%_=HDdpKfTcU?;B<}2J+V^6>oh3'
        b'm!@GY(uOGLhs~!hUOZ^{>4p(xGeItS5trs-W<m^qd=FzSM3I>H<)U4g&M&8KwD3PxYn`)U3}$mP&=@$;7(9fnS;a-jJxw<R3rsFO'
        b'3Vc<(cb@ZZD0ug#l~88QD(B+1Z*F)$L{qeKu{lECx>9XkgPUh!G0&SnT*Ez#tzIvE1AUV{flHhC6T5E+gNI9B=gBB(2fu0-?mNkE'
        b'o82{wdtBr$?m(1SU#gOyICI10Ztd8rF15&QGq9K~dy7jS!ZykrM|fjAzU$PD%*;iti<Dkzc+DcU%RRMcFXh>BqxD6lyWalM2RBB7'
        b'&x=8mkFMWUv@^PHS9L~9uvW&qq~TkmaOn}g&3>cRul(rk8{Jp!nWxmC-;mM%s%X`wVPlxgrIG?n;|iItg@<L}qk}h2G~E~>THjDN'
        b'IHN5Y!)8JaG+pwd-f-Xs8S_!YjT0WoZVB-_qM;qae{HJh1<>~}P#NgXACSR3Z`x@OLqskK>+#gzkp93=@A1^%0MQh(hTQ!SPU5Q;'
        b'tci~fvWc;Ul2xkTld?x;<g4Tx<ZN>0ma6$l>pP{Gt?R<Nb!8hKoM-<tm-h$GzQgM}eWB|4$7gI!7d<{R#JP80Rq<bDoK6@0W#-P{'
        b'O{-$)t{2OD_b`%r0y%K_%^T?CriP~YhvW!_Z3u<7Z8t{b-{6x(GKribcgKVMhr4y#?|c*4_T-J1iDdbfs(V1wwLh0twS$vkFiRm8'
        b'L)-21rsJYH^(0PbX9|8H3`IA{P>#U53bc9mbP1nqD%#XVQ(8+BuRp9t?+H%u$iwqAEi4F;vFDT((F7_>%E_0@rw+UzCPTqQbm16x'
        b'_JX~&?A_xt+Rwh)+FG`A<_~|wxwB2}xXAUd3pE{Or@=D$*Q*^JWiQYC;W6CxuckTl?wnh@qi%ILmCc9IR>X2Frr9^dgI=3V9v8tR'
        b'_=)dY6Zl>mYd?XWp)0z^tIka!A80x?>h3J&gu1G>s?8OQwTECa&enQ;O-)%1tqxcv+wJNy#~ok8>>ShqR(HcGQ|Yif_B@4qbT`1B'
        b'|KK`Oy5hkEyn*ZiP;T5<;E79PHpad!<f?C==hv%y8wrwZKe3tBB7pJHqtt8HJ<&I4T5w!R>|-eR^*cpkQIW^x@zJOk$^Y^~QY1=x'
        b'R9-z1^K8328NFv0j#4bmU<DaG#0>}9sAhu@8b%q0q{$;wS>hWmY92B>#1-|Qk-;%luEp3#*o_m|4c9VkQr3H7bGv(Ui-@zP`|EY>'
        b'?vJD2gQglT@f?+|+BA{><8?1JzfQ7e?@R6O&(BMbwb>ih4ZXbT*iT;3=l-~bs-&Ne2epWb26$D~kDk8k<+lP)1hLyt$Jxu*kzWHD'
        b'ayGM1_!L~cwQil@tG<+)w`9-C97)Wgr4rAl*V#X!^6xLm`sRB6SJ$25ItgIpvZk?Lqx5a!CJD4xdRkPv9%Da8NiHf4P;?bx+<Kw='
        b'r>?7BAMF-n(nCB(N(0ZYp}k~3&z`@|=`d9R;>BNl18Vzt_RRlEw@TYiT_+bJru`H(qKclueuDl~3tZmz!S#jJprz0#=^>H%MA{KC'
        b'm|y3GqUR=;FIw{A$ilB6<;_4!ka}5%`P3Bo`l<y_hAi@WhGN>!i=&&_P?Sx3hN9_q?^}?(%y_Jg#G{+(MVR(|UbRe2Q!TM?CCpQJ'
        b'yw@>2)1A4id?K@14{G_oW@BgXJM$upo%>>6Tryvh|I+m(p9C2X{dF1rgKY+T5CQI*(9Q~1eR(stm(Iq}6KlW}4c7&R^P^d5bU)no'
        b'_v^r%sGF~#4EGxK@K8}FKUdzBL54~{<g=#6JQde%afWUw=Gl1X&-Uv^_#?*5*_iZwkhRyLr+*jfFH>8FFm@;U4{%MwW@_6rDBmHF'
        b'N}gYM-69WWpGPsucHL;hsHad^MBU@{ew-W<-CXn*Rg{e)$0ZPXhc7zHtD=AGS$6%z#_R2F_cxLjk^c!D&@1{qV7E4)()aD2AuozU'
        b'`NKSQam=&sx{XGdLf9ff7(aU53<(kpXbgX%o8hm=d_6GVd>;cTB$(>dSlc7lJKZusb~QrJQYEu4Kx}K2qB&$ab<N+(t2SM;8m{*w'
        b'TtBhw`Zp55rv-h)y-nIstlQBJ_#6S+sgj008khj=(J=sn9GOVB?!Lz?!S=n#QrF4w{5Sz>4hBk95tg5FeW^rkRC{J!XAhzZs(AyH'
        b'XUvl_jUI_R{=v8Duao6~Sc-sH(v_^c1Q23ja?kU#_o8&KwZrmkpEconj?{AVa+d7+pJ`!+CI71hH(EPcd0+@s8ND%8kS61-Cs;{<'
        b'yL(6(w+M@QmRp9k1hK;i4WRHt@?&i+cu_5{l7Ghrg8*o8$|^ve+s21H=k@#pY%t%`eC9f_MfJ@I`E?kD$)FJ&4N${MT|0FG$^Qc|'
        b'K3|zVLz!7wYpC<$<2ZVO>s4Mg@x`)I+Y+orvbKMN@a$^az!<r(*~3l<B#?ieb!iOw2xm)Bocb7Tf6zFRr~A14kH&0Nr|@XPh6vm-'
        b'2ebB$6-Z-Nu9iaiKM3{lkJ$_8Pu9Q2*vn%j;`}pXF~u9jC9)<-ThADpfW_p(=;n<w_FGi!FLKL-6jEVIwxD?N8mrAS)b9N_x|obT'
        b'*5>sQ{#t(Dv$l_LoAl!rsrJ+RtDD!ou4a#*!ll`m_1svRG$bWmnkI%&Yzga1mpHzk!Zw*<)Xg7u=jD~HdKY&j@iE1YlRQmzAfAI3'
        b')>-YG6qLKTt#x5f#*G2U_5_3WeHCcxCM3AnV?qNSYO6em+-=Loe0}I$>n7YM=ok65V_CIhrCQ7u2j(h<jyx(Qm16A?)m-^Al8xeD'
        b'{H<4x87hGa1q2D)T`8_4iW=~_@{NM$YvHT|W8J8wkKAJ?{xn9)l7qKYD!peE%`M31pBy{a*uD(bMp%&C>&a#8K2(-{d~DZ?V@)zv'
        b'G3M1}HU;mhh2LaXN#?F~V-Tx>Sfr~YdDoLD_IHRyxk@5;J%(aC##|*)ciuwzi4W|7JIA~l;6xGIJF4zfU(`K8hWMY<lA%cACI;{{'
        b'd^PI%+n7<42C^r=eC%<#SBrtXA#p~N)*|gDFkw6H#I;e-_xy!gB#ok{j>|7<o@kVu$BR}1G<RIBZyeDM`q}R0(fix^T6W`@J4x*='
        b'`Q@CiWQ>+YR^Omyj~z6+WF52{OQ?^g-T0VGnN)uvQCUNG2+#46k(@D-v4shq-hUGImq;lndJ%J_nOgK_^oH;!j}yt&-czyco>3rL'
        b'Z1r*Jau0h7{bvaAYSC%~7Z<8usW-Ha9tqbwy-Zw~-I1kta)z9-#yChgFS2u=a8`-gD%Q@YPSlQmR0|~=<NPtyk?_tq_%|u-eGU6Y'
        b'T$D@+>G_mED<iJ%TA$-eeF1G@u&HRo{$&(q)C;Kby3ll&6Nj$s6&{9h3ZALj>PN}ofGd)wZGuCXfQw4uJ;Q=&7Z(M;xCxXQ)ML}`'
        b'ivr%F(MiN~oQ*~;LTg)5Ye+W@__cP`;kwWZ9JGjBeF<JjWz^15bpW=E{N=qZAYM13wnsiT#wok&m2E*|NzT1{UBMFJQ8-tQ2-1^u'
        b'2>UtH<A&-8pmj?2_Gpq*7pYDZSG!y?N%@!VdW9=TGVRmzhtWIFQ#d2l>YH}^%?c*S4$@M6bM_d0QH&1r7FaQAWK?)ARkuy8ezD6X'
        b'_-2Wzd12nZL?Q84H%^cpLr=s0?zgaO5NvuspQNieDhkonOgDkffIb;5M+%xVTJU6Q7fM#d%&e-SWg#(@cEQ(DWwhWw#PF|C=vp1o'
        b'D7?&qTu@dDZ*owW-Tq=l^xcNjqwLAi)Tj`HZ<OtXKRA10R2T*_+J|H8j8U(S?UsXrcuRPY8Q~d2hj3od5t2~6;b$Hlvj~1j^*2LO'
        b'vfdtr-zBwy2a=Hm(C{N4csGDOG^%!&Ic35D*PZ#&Jo+-OlT`=T2Yk-5`$p*;oPBw;PR6-6+i3+Us|dZD?i?dCNF8X~h(ML)SM6?b'
        b'E3F7PLrJU*Bz|dUv)r^|%&D|<!kJd3z&loqtr~5Vv9+VZ8@PAZybuu&Oty10J{@PPM>AbY_0f)ym#XSp>pN>`<bm$U8ZZh@I7ija'
        b'PJ7&29q%dB0navTgglBH1)E0wo}$AkvhNTYLK$?@-NJji!mv6;)U%^t3#grn%zEXtE1O?DiqV_y4!qH48->N2kw{2<Rv~W6$4FY8'
        b'qGlFLHb87SM*VTr@CV?cy3k6(N$Z$O4ZC`@J}fasaP$&ZK3FsDN-b<U;hFzm!ec-GHbLjyRWM3M2a*z<+I+Q_5XUqZJ*aLGH;nL3'
        b'f;=mfstFL)DMVa{{sR?aga0eB{EIt4oSNY@nh?hxt8R}y7atl#cTUBAscx+8`Q7M=2S>>n?XMx{YTBnLC&3&PT%6VEX$9lnJU!Rz'
        b'1VkeZ^G6}sFmF^p?cF9a;8e~qdZ!%YiMk^@Xx$yhXKA!V!niXbMlY67_lzC~McThFJitftQBY0k5|RHqo^}V`M5NYS^UNOQ=syAj'
        b'dSXXu_=97fm{F}gQ0HZwjU1(-fPc#p&sfe%sad05Tr@ZMz~TR)B1XGwl}wH}BfSp4kfO|}Ph0AJ4Rfcc=_q;nHgA-iE>O7N%pyb8'
        b'&3Y<i6x3{WibCD2bnjO;ZPRT`)ajxC-(W1UM3<PDqpMFWpzzVeIutYte$Pp~IO<2w#5J#6a^UbaYVz8J{ir>CMn@x#p15hIqvaqZ'
        b'p&9t2XVmI@v()u^YV2A~jnEXZS*^N$n@$c*MMG0^5}HbarZz!SSFb@+L)Va>ImCB8*En44l8BBIpabqX^8325`1EDMgTWW7l%6lI'
        b'U3`OYl-JaRS2cr$exV+1^sYOj<f7#loQe)%JGYZSTi}W=B}5-9?+6^`uaQ^JYrz{{iUR1gL_~%sq=`szX5gF)or8rcT(~%>B%JEJ'
        b'COioPq(qWDy#!5Es^i*)N@b0+LvS?>sWQjUcjQXh*Iw$aYcwuOIIN)Bub~a}G^a2QX-jKoj}?bbPzNDfl5qGsb?DlK?Mi)Ghf^S1'
        b'+R{Slk9W=s?PZkr8bGt*B3PF<9I<qlDDA~|_LXZFij`o;x%PK&Dsh@Bf*-IyzbMnGAfsCFOlOC^X?tE`tvX3zap75KN6ZKBVdBC;'
        b'W$;Qd?aX@^l{_y+!C2%Zk?w#sc-qGqmT6zam_)5<N=_wr9lWQ;sXz~uSmcZpGZ)KX&N25Nm$wi_Q+ETL2Jt<XvfI9XVSHkLX7`OG'
        b'Bq{_yY+$?9+&L@^oa5~}J_5iX-L7tv{yg0`!(-R7p1KC)We8E8cp~-aeTEW5WJZJ4IPK`3$aXu(Z0!UOWd!0Q(r<Sb*sH|uMm;7!'
        b'm#Ln(b3VWNTGqM%EXg#i)o5(e2pFC2X;5U*_Xt#A$h!YeSY%}E#IB7a0T<l|vlEigxol<P>@iRE2%6-p-A;w4Y6Rr=w9sB{`iW0S'
        b'LTg}Uy5oBu^Ke4Bji{XcH{~{(gm*Xd@4e>5#ibGnaI#f@ZR@ez3+Mr*j&0IzVQ;y>MPTk`@t$a%H&R~u1`o4kbF*Syy|PqB*6dZg'
        b'3gj(8{sEqhBtzUsw!{CMyy`hje;DoeXzfusQV`EMVlp&!o`}S!k8Fi?OK}a>RZb?+x0Y43t3fSMJ3A=FHE6XCud1XY<v^kXHmIq7'
        b'PhT|3-|@@sqD3qYtcqUmc4<T`aji{ytzO379*M1{b3`<OwTS2(2^&3vbRbc~t5E^nz!j<h)c2)BXQ^8w!t+gy!tAMHN~CiGzRH2K'
        b'+3!cbE_KO7dkzb}+tb*w5tt=TSzw+3x)q0i3``Gpc%*wer_k|}z<2Dx2pM8;RCl`dY!YgJmmd=9&jH+>@^@X2?D}@Z6%3%43vVP{'
        b'*sJt>G14gC+g!Ko-HoX(5KlQ`SAl{It9d2-$TEGs-f(sVaMr&k2&b1oIHhemE=$*?MW?4RaxA?hZ7)+InHwVP2O_$BIPxo9PK~sP'
        b'fGj6Q$lw53>Xkqi>cmJrm1uyUN>O4~(L+%IS^vQZjDl14%Qg&*4BdHsdKYf4jD2^6&UraNN9v1Vj^;?({*NrRP7z2e+C7sU876~W'
        b'B@YXC2HArn<u_b1tnH1F8d?v)(2!tklQ1NBLv6787}}s@Uq=aT`vFsS|A=rsq($Uc&k%HutbY!BULB$1kQr`xWki>9&`V0qapAg@'
        b'ZVBdGv5hV;ZlpIF8<{Ry;tD!0tO;F_X%uw_VXIRtD<_41Wva{a++`}Wh}t{Mh3+NsJtcCgX_%&$LfPp%b!_dhOP9OknHhCvukP^!'
        b'Q4&|l;|<ZufbM4>0pxRt{C&f!K5^F5BS!H))gxk~HXMwg9HKgolx`$!+OTdZcCe3>mO^?ER=2_#w{6kJxQ&Y%=XC`yU18LQRf?LF'
        b'P@_=^TI1#=h`^RvlV0tgK`nf;WaM#qPSAlD42BJ8o*D_XtuQPm!vlMlS$l?6jGT^(VpWJj!kz?L!?Qs~=4hN@OCo(uL6&fFsT<1)'
        b'Q@wDDi^JAAJFY~wa)1nSQM#n=A?KpXFoe}Ji=K)5-#9r%P)<6AoUd*RkEsw`ns%+)1|^|0LSo2P<ZwDXXOYwo!cwKXRhOgsVq!_X'
        b'v~E#-j&Fe98I0}>&~cH{PXp@>H3xO2Jyc9B9Bw@-R$Udb%ZEMs5s<y@Zq!_7sN6FbrUrZOh_LAgaaB3*NgM${XiQ>8JX!>Tixlq}'
        b'z&)A~HgOp2%FakROO5<`mn*1nHamZ~E|k;VTl1>eUMa4qCq2<43zGrztlyN&N*;a`r(wwfZ6#!c#9c|ax?P=6A8drx23?hTS*A;L'
        b'E?wmc)upGpkjr{qRF}EytI8zM;ExAe1}5jqOgH(;<s|N0lbD#elnk}#Zr867&RAjYWsMGZy59!`!RAUHM#|BR;m-YOfJGvTS>uO0'
        b'JqsZlZCk{l6zb-%A!wK`j-rbrDJTnyR`GIbY?ut8i*u>b;TD1}j-jp%mtMl@;(MqOC^}mRX=)fkjS$9BS0T(`6$m2f%^x04B&hyj'
        b'b75ru&@f&2IOT``vH1h=Ka4I6r!GS@A>R+t2paUD!Y9myETtUI?;TEj%3Sy`D0${XJiR2^yegPpv=^zJ13?fL70g88-BZ*%!`z`M'
        b'Gme37W)~dGnvH_%-`yxIdI^OM^-9lwhGR+S`p{M6m|COBKQLVWOr?a=aQSD4?X1{bsJT#}<baW*ktbYqorE)D=0&gA?PcaeqBR9%'
        b'a9&fbchO5;H=lp->VZ1ic{#5^U7v;aINjp0DkT_2<zIoRT$g2UR(p+@3(88~k7+|#JQ6y5t|<#)^}A4x5@XF8`w=xlEH%`brAop$'
        b'ImTs)ICqHfU&Jkb-zzz;XcLO$g<95NoaB9O@o}$61XU3YR)@On;_f2|;qs$3fzx;+raCu=l%rPiL+j3wk=3gkza)d*mD{`Pgo4MW'
        b'Z)X~T09?g@Vpq*D7u*VJzf-Ym=P<Xl6$;UAJ|R-+d48C7!>qvQMRjZi8c7yXG#algmW)BOJsM%w5=v`klX7&kOJlD#dbSJ;m%Qr8'
        b'C}h~73tY4&id(c#Wya`;k1A|4xu6JY^{_>UQ3WvGQJoR;>Vuv<G>6!H)CjHNxcyjyOhpF;lgriW@J_b~j5M#e3ibJZB^PgiB9;Mc'
        b'YiS6lSqcjSyLOl>HmoY0P0x~TwaxNsVnBMi4~Stxw;t1bRt~cT0v`%2Gk>N_OgI<m9;trD74cE0yKd`7QEu1qpcZju7P}rXM){yu'
        b'yw{oKS|4Uv6Xnw8w!7EY?3UE**j~BFax9Y5=DOVL?axc>iJ(#>K7weF9$G!L`G7D`8KJsp&b_{p@kYqW(3gYUuG$vlt<x1Q=301r'
        b'y<#)i4FT7%kBGU5Z+HE8)t<0@ryw}P#cHP#%r85wW|M|d$|GW0mKkK5MQih1Z}4hLypB`S;dcef(2v}OI`mwy*PY3#1EgC3#P@1*'
        b'-5v=d)*R8UNEk7dH#h^xi*D`U!mJnxM!7NJ2;qZ>Dh<UE!gP|iNryf1Vf6pi2wD?YUAp;QwbzXaqss-|5TGts>7-r_gVMCQKlUow'
        b'-H2+%6Ed$`gkb#u9KrS5!o1>FICll@w!3w;EjarWD#c#Bs>`YN(i%mZ`KssQ)c`^b!}9lG352Qb*v-4FVt+y?u()<kC_=eP>7v9i'
        b'uWFhVfjK43=Yhh$mq4z&*PC7eIp@_p3nD_b21DbXq(+<8do6fRLj@LCuiv~%y>*ol?>l%Yjj>#krx~sP9<tQVq{aIzjFS4-5Q860'
        b'D3lmJy2{uVlQ<ZfmAp^557@|j{UzhZ+G&yH57O5A)djTbZFGRus69?-U*pl+foIGgbzXgx*eO3wJWi0a>U5t)>FaV1{;_`f%kqu7'
        b'jX52wws%wm4}ASqS5vj5(yY2P(ZooH`13MYo5p$UfgsR?kIQzFb<5FnyJ%T!oO7ID4<T~-x_J!n&fh=O^%NrkBys5lo(!^S!_yd8'
        b'+3U<sO-c4MnrE^bQ@VoF&CK-LN!(dGH!>F0r0FDYjt^&OF=!{GY@4PayHZn`?KDFj8Ptgno34TM6Qe~tX*xRXJD2^(Rr=0(SUxwT'
        b'&Mfn4@7C*YA}YJfmPG5#+Sy1cLx&_HRjmjkzNA)MZR4)eIF7EH9T)->j^jo51t-hdZC8IeTQe-X3bv=^2m$ttWd*_haR_~#pqq{M'
        b'>15cxc53C2H*~Ek16^Bdd*Uhr^@0G3Xh=e!imv|V+lwDjj+#*e1H>nVG^j)7%F$_j!_R^J;}eezb$*R=WTYiW%sx2Oeu(Ej7kOo`'
        b'xyT6j4n2C=YEV)0lKvyhRj?RpYUa5f!d&F6?(TUt@9B|9ZC2au^W5%vy$^}FhY0UOckWW3_}!3a=~V#TNk)R;cF9HUa<C!FymI1e'
        b'5(F{KaXY7|aVgwhMQgi)dhn{f9=$1uy$8mGV%Nf}=nbwU5&Aepr@r%!SNc`2`vWqBoP8!Zq<LpZ!ak8R%60aq>P_cE?B};z%BQ*_'
        b'+54^vTMEMWADyEl{zFdGuH>ueiG^TYRFf!C*_fzHZvsWSiVeKe2Rd*3RZr;<ptDN@YnG}_b5%{xPp)neb<;}r$3dW95><yILu1<h'
        b'd2gsK<|-MSS}zH-wb$!~A$RJ@sx4ItdxzN0W~tU<txlld%?HL}>U}o@HpX37ow6hyDEiZH7wOBoY;4F?GRl=BVr5rP1Yd2GwUby<'
        b'GYm(J$R)>Gm#g*l9W^<%>K(QA=YZ5=E*E2#P1k4rgL!#nw#dGHuXB<9P0rLKVb-6ATJRFbHxl&763hUkDT92njtw1%kbC2?%(v7T'
        b'&Hiz|PD+Nn`@%iTQpix%+mjjT93f%|%<fczoemZxN!T^Djxqk&$#Z8p5<6x?j|09Z_>=~^K6!dD??RbvR^L8{d6s|E%7nL-`Ckp4'
        b'7Z*H@j#7Z#QLAP*wrVzcT--u@p==oDKUY2~XFnPurM4VwS?A;U>D`N$rKo0z@><J4wbG9Ac}H%>yxwq)-*tM(7%b{qWK4K6^@ZPM'
        b'of;y;m_?Z3<WL&%{!?TaH>;0XioL(Bf=OYPicP_odUr=nt-U=MX=t5R><eYl5Fb<gx$=z2bcJW%8e%|WAHPLLOTR<{i<EiVhq}|0'
        b'85v9%mJp`o&WM1=Awi#EhZKuu3YpGTbR?$o-lk<Z868i@{J;cTyf?f{ap_qei)YmFMs%IfyOfZA$kQ@{i6W4RpX5QCajOa6KZV3#'
        b'$*+k^C5~g$dll5*htlxdVTLV(oMyA(lfjC^L57+^y|b_~G%b|d&!-+ywZM!=OxJ{0?>$enyLr}uqB?x~qm#g$83e0nketWRPlTjo'
        b'rl_;F4aKAsh#A`xDlKW)I@IntlH7HyUB6$=noxBoQJnUyvli4bwA3#)+y0cldB|*gN(jsHpMdabA>2Yr%(ks&+qMFt`o#h<C&A3_'
        b'S*s%H{E{KB1oQuoqJSu#pQGE~C>AbVRCCm$gXFV1ba&lTFho{^{<ucKS4<LQxO(0+zN)&PIz#>B4CnUFuf@k_v`C<c=^Gv^cuMvB'
        b'Eg|QK7;;)>0RK1!d93Z>A<w)a)_}y9aOWEOn+YosraBpsl{u7Frn;mu<Dz{l^V5f*u7r%e(4q!8O@`^4^<JZh!SQ{y1_tF3X=R-r'
        b'U(9=C^so6igA<USH00g?E-FCI$gOUE@7H{S!6m9%F{yn(LaI1i5|WZyka7Xp{@nif3(d-^W;O=FmO0CEtKIL}kzh_L{|O7r1c{<g'
        b'(?b<|ih?mp9+1XI;663Rgc9%XH_RL&KeUAst1NRaG$_|Jk2Ncg5Z*8G5@<g*8G(^v)e~GOQGNxB$Xr*<+KUx7GZC_~SaOEJ#Rmz)'
        b'z(8l1|NVX5us*}B!9d?owO{ZS8*v<(+Sdou#)xH24yK9cq{Oe7n=Up5VUJ23U3{leEQN*C7>WbeSPCbB5Kz*hnKaxOggKUi2Fo)x'
        b'h?aFX&aB6ZG^9hgm7n&SYX78RaFASV{bq1AQSe%$6vk@bGE%&hAgkMj51`nu2GF=(<1w=aT?scAVwS~|o^J-pIsUuJ0>bk2ZIkex'
        b'8r3z((U|H8R@BRTX^j13@YgkqIyAu1f1-SY@i{nkVNh77Vh0k^f_D9Tkc>?DB82YzH|G|;Lkn**{$^k5^q^B#UFV9#5~9S;9LH^b'
        b'?l14uv2P93m9QOy)lGCs9`(<`z-NMWW?Gk5Z<Yq$IJO=cEdPlsPAmUB(PXC;Ed)sxhsvpj0h$g1?miPuaRX%V5z|g-9zK!BOn~qu'
        b'Gi+{A%^<9<;`o^R55~mL`BVJ;x!jrC-g7+N$y>N7)ltm*8phgD|B8MNpFI{P(|i+xiRNIRp1e>GOKKUBqXEg<{iX8Duft|w8kt6c'
        b'&)K3l7M7!VS?U-LWN2n!P*0D~Q7h%&%nVe80=_=}z{(m_;$zd8&<9V&pi6$$byieU6V9ET=~{NR!>M%9*uR|3&c@JsSsmRJsblJO'
        b'iD?aE;nVbf9M>DNNSuu5f|(jrsNS`0aPRXRFmwSK1#F1bdunKP)ovmftA4BMIU)y(SqT+DIm>LF$aCM+N>l;c-<mPt*)+KB9d*%q'
        b'm1pDNajCyhWwi{n;I{aOep!)h?y0%*4bd}fZocS@YJ&@>-3fPY-~o)%lX_dHJ~sEbv?Yjr6cH`UJV;86amrQUb2vQ5NaVmOn3*Xi'
        b'BbL-f8)+q{(dC5a%(E}*0A_eumic0>yI_0XYIWAKLGvPU^|{zwP|=a~E<v1G!qlaZvuZ3Iq%5zZwm@9|F39`M!mBK+#d}nudd7wa'
        b'yNKZOtu+>XUY_{E^U4D8ulcyk7+exs7xr5arH8(2{cjkdHeBW+WTl7x835w`UqECf#=7kP0`ewr|8F2hv)jI=aE&>ZJT5`#M<ZJ7'
        b'Tjms(da%t-b)^_Gq%9KmKmCwyqr=P^z$(wtK?d9R)N*lHX$!x(Ub#77%&x~)sc^F`%#4S7iEvWoejb(EUF#HEMT2?u%5`^&9f**5'
        b'jp6N`kwp`Cm0T>i^eafG_{kp!^miauidU&bt1sGcxtWkZ`S*c52k1ItHJH$G*smpUvr%rtlg&i30LKNhRRDBlprc;&U#J<AZJ}}I'
        b'u(<zf@6G<!JH-$*nf18=vpLRexr;i{Pt*5RmmU$HCvvO0@90zPd;N7K2fuJ`3+#l>mG3**DBoAbO3}#2G_x=E3t!AtZ#sgrPop#)'
        b'IyN^P8(>cjv}^KWb6aHWpHZ2_HFM?D`@&u~$yT7Wednn62Iz|-t}{;Os*6mN>vZgqfy5-8tUkJ{vq=`X7g`Gd=gOS4#mP6(rip;Q'
        b'<SFatI@gg)9~j$Gd6(hf03j1M$<om$CLkz)YdK?{0)r_()9c0w=!SqBA;Kun0I)~s1Z0w-nC{XYSw?p*Q0vR6mj>GQ!sKF&sQALS'
        b'9+hYAFKkGc9hbuz&;AZ2roI*1Ry%;iat4ZePkz{t3i&8u!N70i?T&%Kd!O3|NF0n*&Mn^JoNZtSh~QX2a*S322B5odQApgh8veM>'
        b'-VWem#bU|nkDwmy4{Sb@M=D$lo7{gy<kjV}g&;7&pm60RA3ftbqjxGRqnuP_qSH{BzGo=-xTpn3=Iy`lnmy*~oT#yv{g4*I&hCdA'
        b'oGfk6=L4P<1DrfOq3#o*8SlABHXAh~z0ObT&-u#-jGbazr&_f_%-+@S@`yOya(ks>Pvips=`b*ocYld@H!Ic6cJH~g?nO%YpSjrH'
        b'+(3x&Fgc;X<mg`Y$}kCrz6}!&ZoHkjfpW_hPZz^X-v{<a^YsJOws^WAaWP^Wb-#7$3c0jXo0n6#6MsOGC!HW?kKirATdL?VLUVj3'
        b'lJUn+f*nI-YeMQl&Fos=eN=huePTJroV=a5ShejIS{Wu#kNkVW!RBSZyV6<<R*)SNpKI5V$gsN`<+@I)yX%#C@`=4Kh6Q89QfwF2'
        b'572?-<aHads!IU-Kz)l#n}<&Q(ur)$*Du_oHmcDToELCkJeL1<KP|y5#$ZMwvYeC|Ci{_U?r-Gj@Hj#oN3Xn#n(QaC^=2Ad^|Y)#'
        b'F2NfYuPq2Jz?VEdGymunFOl3Hu@>!nDER{X-J+RZFUI~0;f8iRs>2KL{vw&zEn|HsjmE{Q8+bdB<JBlzTg64om0i!a$LSzel&;Kb'
        b'xYDUnTnt~=PUs=UU#grI|757|c0kV?=nvfWxYFP04o4ebzAK1*-B`mmWvrZS>Hn2?_4aU;4%1HZ?AQJJ!(b(2!uwu<^MO<SEjXQ%'
        b'%)WF5tY=6C+xV5=)TNI1H{#XN+Q0JD(f)Qi?e!QrIinN!%q`OXjb{&B@zQymE<<SA&ertbf!h@tIFC%DVfGzB$#V(m#Pt4oV?St4'
        b'j18k2`k6yKV@or<+22Ss+~%7I!>j!{#J(3AiJWC@J*u{paNOdVq`TSOD8|_Gy>!0i%c(o_T-A<ohj2S*haMJ9@WS~_es({afReq2'
        b'o&8yVyP|q#MyDqSNQCtKazrKS;VU*ecgYsAq|8e{4hwEcw5>4DtI6xCDk-}YJ+l7mKSNS%HT%RBVflaxK{ibuO+TJ!p(^`J@UGpq'
        b'xO+C@R7F3%{+^;6JRNZtDW_M&QEWe5c%ODk;Vo3Q5ZZR$YVU_71r~knp1Zo%=;Fv{(Z-i#uc}i-&ACF;xqEuU+P3wR$FwirWjQCK'
        b'<3Pe7ZHkTyS8<qGvey!UHb=FqRCFAvGNX<J1Ul!oS8YEcYm7W9YEmB2HKrY<nheK-J3aaqqLc_P$>yxV^(^}!>VR`sqo_&NsBDUC'
        b'q?&Y%hNd*=T^;LO!xg5oF);eMssi-wFuLQ|d%ZL}d}FrbLms1vt52HyF<Nt#<}QgkXk}7D=@~tz$*r4Ji8~YOL${??($6rak9k4<'
        b'ba?En1~nH;o@+yE@_aOGmWlD>@>sG(#KxjL&jbCiGK<)Ig}jU#zB9s|s7_j%M@+OQD=j;)hHrS<9bSWhO)!%?^quG5SCFY-p2<bu'
        b'Wti2!YsD2J+klovvjW{3h`y`$P3)pa)a_JUaDp6A0Dloi;1)3y05y<K7P;2kCG4rf;sG{J2nI3>Egzryk*5e@{n&y9X+PzYUA`Wk'
        b'`p_SS&!!^!^XLimNvdf17EE6BF`wM-5KQE`gz(-f@ZZ5u_KKg=El}kICKZQc)g@#IIvuu!0P7E2xignw9r)3VV<AQ8BaC-r7rwJ0'
        b'LXrH#h8Lsq_gq2m(?y7v6ort;&X_$GLpyHrG4$j3qc|Dll3-m+T_()*GoLKmb0jQz?}4b<3y&R$x+}TrKol<3V=+(1tVCzwmJNLA'
        b'VoW;Dt3I3B_3taL-~r1s!7eKnU;r0|6(`}+Ihe=ocP+-+lQ=TEwM}v$W_9M?T2;El6^B{A5brwdcO}lh-PHEk6*3py|Nj)#y}fMn'
        b'haH_=lN|@q1_E2{M_PjTjA-Av<y&1rSp3=f$Aj3XQK|#Su$G|iV8~YOy#;yiAFYn76L$^n+6RDB4}KwJdb2Sy$oCN+vo)kkI?7u<'
        b'8~2`l)$J~eed)mc;<Xd#Mx6<ZDK?$u{}L=cBkT*Dz}XN%#96a*`&1JOAeA+d$$EpaCNudZtW?N5H$_Ic=Wo}$%M5?Nl2z=t5q_`r'
        b'!S*<#$}-bNCASuBKQ3);Eo--?yQp;47nm{52*wF1$+Xm(v;E!^ica?n?e3S(ojZ1{1^4&yM$sE{<t<{%B8?5ll2@+UoeK8!?Fge0'
        b'GZTJQ#9cNjoueLHmnYU2DKiU{>sG3*JFl4YOY-t=Zg~E0Hlok6JIL%#H)p+(|MV4*LSzW2qklkj@;rCtIME3*Q-@-V<~}l*oB@q6'
        b'*14{%Qx~mF?&VZflwrP~(HK7qQy3nCKWU$Z1%dHTVBVs|VC7rJgS=FtY8h7a8UGM5H(=v&(97p*kIT^9g+98n`z*mk(WPMP1AbV0'
        b'O5=&{AgnZg*1mVG_xsza^mQv0q$=;7TCbaj430|Ab8P3b{btb{mbY)_>-}bJmP&imOZ0&mYx*|~gqi3gRqIyj&Dnjv?|D*|Y~rjL'
        b'8*0N`R5s(5r?2FSq+C%lSG3q=%`huV7%HRun!Z)s?N?ZHt{9~L)(_N(V(%#cIsJQz{5e-LOVC5tHF~i=MVVKu&=;#o0w_wRwh(y-'
        b'YHim0Z22W#tB$d18EZUaO=GN?j}m_&9*6N?$XM@XC|%5c$j@LH0;s3Aq=+fp&(LYr`>9A+o)#l|*%rH~WGej1kAt}HYl5L4?h5lg'
        b'LF7xWn6>%U5z@yAGo2IkG%mFg{ulY!Q__PxN9l73GP>fhh?Ki1eWzQ*oc$UtBJbBe5OQEg^4k4-QWA2<+ub#(QMhjzW(d8~c|vjQ'
        b'{T7_DCTN?3yjgElPXMro<i0w-p@t{JeY<(AloAu71PqJWqEKU-_ZlQuuvzC6ShVmdb&>*`0DY$D)%oZ<>UBegZ~R_O{=up<@^<&@'
        b'@9v}0q8n~T9H@=j^_k!ElOG0}Nz8XU)s2MVTR&$__7*;jkbWw)4)^J?+)MB)Ef<jlBm(V#oglpjuQ-f5{)*?WfSBn66!Wdcb2TWh'
        b'4aH0k<H^|&bA%JQVX2Y0X)eZ4S~AI<qUJ=W01mlb589e2!EnOQWt}3jvke~rA8EasoYr#+%k4FQ%SE>+jnLn((4VjE(3f?EnPkN7'
        b'1k5KTw053cBwfi1^K9R-W6@n8C;jdq%ie3n+F*bPq%*zCV-0`d$vEk9;4aP@zwq$Z{kZ7~Y++$)0`3bJ#jb$3F9D0qhPdM=jNHCe'
        b'^YrUmap?uDcnR)Xfn8Y@QgI-p=ovnCku-zHidT(u)V&s6uu7WBoW4cQ*6*yf>&q-BCtcLNobLzw%eA0XTRy+dxN(7<;z^yy>$j(<'
        b'f!*A@z1^wGXH(ec{bMQ0n%b<rwIoqrz~nfki!m&I&%D?7ycipnnovV#v*muopQlIDou;?ZC)L|i_u!6Cv8|fF#9mIFCEu!vi9MM*'
        b'3-^7_TV4m2x>waSNBaaH`<zc9e1RPX#eEhmxe%5456=M3mnRML`xwm<6*12EhGPd(kKiB?*=PN!pX1Wgynt!|Ps0{JyVkGY?KM;P'
        b'0+x)YJfpt8z?|bW#b66lwrZG#8laYR1WP`gIxA>l7;57k1c38k0SH2xv;{LP_mi^9TGI?{;R;AGwFu2bLLqh$>R|b$XJq<Rh1VT>'
        b'APo2Y4O3aL_}#c;KW|v*-?XQmKrpFfeThP~V1d@k$37zcVhXyqwiZ!i0S05|Sd8VOm^1}wQ;@6Ks)+?wgRyME7G8oT9W}fmybqdE'
        b'sct!T@>p&P!ea+-Ab}PSsj_?7bU#BSR}evl2oQ?-T~9%q(`1MN<hjC!r7NLD0=2k<->P{uSD^c|JP^myFtG0(=Ja>K29MU}0UNCN'
        b'=D*mW<ZFSdZS*t)wC?sI-%_cbXHz`l-}1m3W|@<--fKF^uPsCjTF4_VJJb7{K?zj!{LuGo3REPc($~0_IXwe?fX3%?sH^{`gABW{'
        b'qBieB*+pxnREMp-yj7F5_R9mn=NZ^q#P^Oe-l8JO?EsC8WKK7{EY;U-H}v+ovS<5V;~BSgt7b0aUYB|RH!+x@?lMC}#%pkCCU3af'
        b'2Ne)My6q`?_LDxQB-w$Si!*M7t|OIaz&g3mClq;wDTy>8PpXEBX$X${c*DeHGFr&~Szoo?@L?a9eYfg|9)C6;TP9sUMTWs-F>T}5'
        b'o=n}-AA5NNh!vVQT<Y6!2{);Emv3#o%v8>kS~HYNg7^<)bSzO*RSOX9HD#8;51G@i>-TO~eety;9P}EP=<LD1%_$w}B|bl&OrXJR'
        b'>?3uRh0<O=7exV?)58c8FJKbu_?kz3u|tOM3%=_I!}FKZ3RT-X3@<^yO~2=nc-VcH;cqBa^H0NzePo(%DG!_~{dvj;1GV6cp$37k'
        b'CDVY%4DVg`><rKX-DYE!>A2G$T7DW+`Nm=gHXOlySEtx*eH%W<9fMQsOMUj;UV#l<%XFq}<o=|t50;lk;y`ee;m>_-)qNaDL*%_G'
        b'r+nO<qOYk{xU9*BwU-h5t^n@)fNUmZ(3J;d2=>QQz%%S~eF3KFUZC7mJ65kWZ0vis-UX~YhsT)LuxSFEM+C6-k&C(P^*~waOFT6E'
        b's8nCCh87$P(M&U}=>zdhWY1?b4|`Ak^PMDx_t2W=6!b;2{@C_bec8Ul9&=w?VIPx}^DYtOkLP1wkd95ZLhGAyd~>EaU=W>TT}G`%'
        b'(}Q%Zc+Q<x0kid0Y-=M9Ov<@~x9V1cz;$fLUf+OAAIDx##eI)rsRw?41?H(|%0OS{G>cSc4m=Q4{iz^5yZ0-bQ^4-tl+r>7pO>m8'
        b'8a#%+^bF{@=l6YXq2s<ROb}J^3yIVN@gOqy971$4PSZuTB%~N7@x7RV?t5n3GzW>NJv&i}h0`Srv3<{Iq*^RDXRB^rZdwJ%yT4<('
        b'kqGO*VG9RP{3&eVnTlBl7Jgm<pf2(3+&;v2Gy9&2l+HrBliLP8H9e1Q)rE1VkG+$FJI?W}w6C-zPdYt!kbL@(xBO6V_)jlrW?fGi'
        b'`r-Fs)#W;b%B(x6{CpY6SUK)^1~dG4nM|u3CndgM7@HHl+$Efgl&vaZrmvVZyyiZDzPcnOtD>cbt1#!9#se}mRfhZCoPzNUjIQ*<'
        b'NyE;|=+V|NvHNxLX7sIQnd3UoPF!yL_A>N?oXwrSb)K-FujN7xmJhj|3h(LL9Zt3TQf>LyV=c%R2Kp9%`9Ud~J8iG_dgnacZe0dQ'
        b'JSuOemJLrBoY0k^;%r>{9nZ{32Yy+DM5Icy1NE)<@^s%iFOwyeVZL*)v?c+Jhsa2GTCET5|9G6eUTb`OMN-AA2R#+N<Q(spI46&O'
        b'*NHn~raW(5zDQ+r^303YG&DJuWlGV3pXbnJG6GWbgd`41Skrumd5mqkj8w{;Oc%rt@tDEd%UlvML}o%E?qGRS5b(Nxr)t&^?hsFr'
        b'F)bnfRjRINhiHleo;rHD)VdIL7TC(oV?{eusZefWQh!)YMi;GAbyXdg`yWB&zn?^XYq^{|H_$s$a?!d_`YMlUovH+=GcpOV3F!b@'
        b'qN`QD!AZj(fk+Q^g-QD-4SOyldi?crY2m|<N`1RvF6v>is)xk@%gqM0Q2H%E*LvM{fy1>(YkKN3kv-ScK8Yb!trn?h#aKm3Qf?vA'
        b'!2Soz-Hvpw3#giBcP~^3)HD=9HNE4tNx%X%au^!%ZNO5G;-*J2Slyy<)5%Fo{OhQi>DOwYXEJVnivouQ+q3dAvuTO1b`lz1i!?mn'
        b'U!dW2Yr_x@Pr~2C+;OD${SR6=0f$2Z4z|m`;;;yCSm4+`DWI@c11LyKu(c_upRWmp3w~2L9SWzLwh8@Qi&Rp_A5j}?1-)}Uwzd$p'
        b'v0JG2@NcTkfoi{VY?^MP7Paw5)J?}aZ0&w%$x%58YABfvI;h8Z8EXGpb@pXJA2mw<FiB=lQ#%sC-S4wZq6Jh)2!n)$4l}@KJlJ&F'
        b'Oh~)e@z5kJh|?)@NV!kC6cj{;41?JhOH5~oFT1P^k!_F~Coe*tM*oc(a7dQ_I=;7hFQO8RBYhItVvK-l?w$HKdpVSwB4s8G8Z=Ij'
        b'?zz^B>Gv|57W<MXEk9K5I@;q6KDuF3%x3pZ|Dq{(hFUd&wH@y9&M`J={C%pX6yI~V5!rs~o$mOzy`_aF$82a1S`WZ9e9=o}r#d20'
        b'+RZy@A46K2BMhaz(led*A4tn^%tUEd@02?SX%9GpCk?Cbr1&7^L8)Yt0n#H)kjXmb>FxP1>K}(9nWo#fF&C840L=_v-l_dguL})K'
        b'mha~6YL#gejX4=TUF{IyzQ}RyHniW;+uE%57UoEI+{UcudkK6&9`qdTyaYA8Kb2f2U2^+$k(j2JblE6xFBxIBEy;KHK6$E_*5+)c'
        b'6?9P!4XYg;L?2p{q_MP1b{*<P=LS{=*aE~S?aoRF1HA_;Qb%+rDVymFGz6aKdf`{yY;Twu(e<qMovF2P(z&-Ws<O9}V%q5(PfKt4'
        b'xHfYNR&lTGAupYyZ&rA1Ii;dg)q6lgCuuzctaUGFbR<E4IAwN=)bqFN)n$f1^)f`i>M5nlsI*ZT9CaUaXe!SFMsFsl#(5TX`KMs;'
        b'g7Iym(m*%VuT-zoi*0Z6_7o)~Lex;xYrVe*EM@&lWGO>pW}4Evu2(-_U6Uu)uT-u}QRD#)^GkvXao-%Qp?NC#In&fFjLPd}=zP^v'
        b';!@-)_4QSIe#dA;S|!+x^9_&mcGCInnjAWLwr6Xv`aQ*tt|Dft{D#}Br!_fh=vrZpVR>&Z4J#TV)`z@r@RrwI&MJC@vm({Gk^Hn?'
        b'Mw{;~%4as+ZOH5`)ja%+yeK51DHH&BwfSw<UV78)PWNLZzN48g%wfm6(OJY0=rD9nzP=ZI31iDK9pVj!Ub7~rzbMSQ3gqeH)Ys)j'
        b'uS~_h<vV{1sW8iWZLsVuP%zdds_jZce6KTwgTJ~^Ye-KEVT)gk?f^tP5^gh^9Q}MSZx<U(y)J4on4Rg0eTVf0PnU1e8^jj^)SRzw'
        b'Kg8?r*KdZ#vraM8V(S;(`bXl*$MaJ3W{Tmc#d#|fW-DW}F5OcSVvzT`H22vG?{is~8t(2jQ;YTU5hB$m4dPx>V$+z+g(jPI346L5'
        b'TI8%bsn3KMCVR}9bgnSnY|XKr=mv;3t7*x$5W|l>E=`85FvDdv8E!(EoF(6*iw<5*M#Bfvu4vz!NrK2QyxlF>|G?_FX~Av7#qNSa'
        b')hFV#r!e<kn;W?iO^YTaddv0)B%qwCvc(NMrjpl7x8KS?(9KXw%vKW+09rO%mxAuhdb(}Y63z-ZBJ4QpQb#w^QTZNd1m+VNhRr`I'
        b'9pMcZ5I*k~-Q(5h(E-!j2%jLpM{n5m8+<}<8+<)BO-||-B|)Scs(#IKgxuz+441ORo+mE9%2AoEM-_R0P}}ul7nN526|i-yz{;g>'
        b'^1$oB*_#8L{YB4{&v*aA*_#E<ezK`2z}YZHz}$$lttl6&6yWa*o5diRff+1YmHGR7oJGZv87~Kc8B|kKraBs?;=&46(g(Yfv=0Oc'
        b'7k@UVs`Jun^)zx7dl0AJd`GRdze7hBZJUZ+FI{lUl0Ac}=t&Drt&<SAo>+Vz_4gj;&36jS8S{V8#BV6ZefMLAzx5D=fiTXaJ<Ahb'
        b'R2m#Tz}-u1xZ`&i^?VOqXt1(9bbL-wFYYs9`FnfFuspNEGGBs}wt{G##rEbqn`}SC<EHtTtwpwpR<GEer!KRUlAz43+89igLJgfQ'
        b'o~FT!rPv;|MnQ&sZ8THK58$hwo<VKuAtPuSr#sJsFrl{hz+6zrEA+Hlbul=<u!q(zst%K$zv~MA*W_m%#c0B)#;;S4_82tX1b*MI'
        b'<Fo%(nyna&bRW;)v8ol<4MjbHeI~+qpW_7j)*)=nbRF4IbdK%NKi3I!6N(aeO7(ujnqLa1P^KQ=d;DYH=Yg0l%<=t`C&Nr%K)u&P'
        b'aZ}wC$lvnIdO-qH_xI4Ww3rU%sJUH{rdMv!ItfiHyFwi=-GaUw=Jk9wh&viFT9a(1=EjHO(tVh2r8!iZ;KzNgTfmR0-{X$EZ*BGC'
        b'QWr)La}C$N`?Wt$+zP{k(0>Jvi6(TR26Yc%41%FCANpGWH7W)~=3JUirb|RrWDm$|_kM}jnx&f1KznHs#bG)EPq)%NG#(49i^Ytw'
        b'1KoL%sGHP`9v3y2FsAEP)3k^%iYZyo!cR&<fi|mDxML?aYaEyUG~uOFwcBB)m>#%I;HgyqcWE}&Q)-$Hg1HLPA6@r~CJ7j~xdiZ^'
        b'h53;Bu{)pY0Vq&BApKy_31bE|yGIRCD-a@i*3(*!T1ZL(z=p_Z+HEupb|-+I^b%Ilj!Vlh+WotPG~D-B45}tP6-V`Ur-c?5#u`3>'
        b'@y=j0d6;@{+KN<H2!Nu3dekdHm?Z<#P@i|F{($>BF&aNO%Qh1z6RXh`=$M4<unyibT<FgKu$v|_&5~qNl}C4w61Alks?C+Gdqe{C'
        b'gxn5V1dEn>r5XUPdioDQ>Y!5G(T-6kyXnFOR7dwhZ5q9*7WbXQQs2gXhhfFhLsa@c{4t>P4>0Q8Zo?bhbm+ZISR5Ilhh~5}wXGTv'
        b'AZz&BcOYBQH_g^$s--&(FV5BgrGmzB$IBD>Pke`TfQaeQmyS*3>$?LKq`ci;cjFPR+0*b&Dq!q-4XfF$P$e$q@bxNL4yY*>!cdex'
        b'75kbmeFELe3MKF$B0I>m6{+#GRs@`9D&uJ_p|W8lo;bhADzi~@bru~I#0ZmE`Z(zFb5%`W>7wYuWXEG@jzE0>w`pNrCxMd)i5NJ='
        b'u?5nhUYaE>j39y>6Fk+>ofj$y*-%V#()U-$U-A_0aPWpr-Hav`BhJCd`#1o;kajQH(~kS9_)<*{^-6a_1?adF1aWWP+iFZb)FSm)'
        b'MI3<qrI<f?D*2QzXaW)c25wq4K_z}i5DSDeD?}Jy(*)GXYfuwe4>wdq5Tb{n{s9K}wSg>OV7nxOsM!=po3u7)_0VLyuM<}Oy!X(O'
        b'pa0c&?S;z%b4Oajqm*skt2o^Ez(oGm?mU}f)o!^zZfc>}*Z(t6&a7GT&Pv?z(&Rn~L8Kaj0&{Z?nwz^PgGv_~7Istke<A1KCdd%4'
        b'TLifI|MDB$st|7GOCmCqUK|H$^kOZQ+zn%2QJ6&F_mUx)eh4{Ddp6=g3U2z_q?uk)9bx**B;+v{g&t+c(b-zVJ>B^acLUm{fAc^)'
        b'v(Q;U4Zy*icycLl=`zT*Eson9=;M9DxF%j;f-%N;(DXYV%m4ISgzz0UGg&6`cYilcktO`Xm8-(GEqosFbR4#D{;Dusx}48H`|Tah'
        b'oWtO2w_r1UK^PNyulY?L@u&ITazFe^#X_0~LyMXDUNQpx8rMqi2V3^203d9Fl%RVnXhF8GP(o?Y0H^gj^SwSjZ#eY7%57euw6*Y1'
        b'R0;;SVc)mYHt}U#s^ty)|5x#KQ2Y&4+%(9O64Lat#B6<lj6N<YzrAjYI;42R3Xn_LVK{Y>dH@s6c{v2zd$Q(bbmPutePGu=z9o!Q'
        b'UQ}R=m0c0i*^|`C@6fHu^`>ZKi>flQHJ-e+dg$)UGP?8jqq2~#maP-jQJ`lTj(i8Bo4ua;?mIJ$mEXvt^&sD;<#gM348Gp-)J*CS'
        b'{E4-Mg;Fi>=Wfg4a1aX>MNd*q-!XJ>u?9D-#EMgJhZQRhTWhHPmeEMjdBOy6%DexMwRewe>Pi=e_bnkLTf0LbAfnxShj59g$&LzI'
        b'ZIgfzQQIUIytF+p0YQ5^2hoaS=`@L*h!)R4oYqV2nGj38w2Y8WtF7Z(z!s^3B69HpN_CiadK+tP)u`ls)(+a4^PTUX@BMy1eqpb*'
        b'*M8Po&wB3bc9pO?FheQyS%04nm4+n|j5MZR1@%6QwCK6*AV&1uE0@yBK}4fTbsY}+=uh_yHJ9zLU*;b)Y3pSWzX2kRd-by52ay>I'
        b'g2m4_gRp`o={2nF5egkb@Y~BahZ3w2(L~8mmn)l^F4ylIQ}7K_a{V5?);j?hrEcrx;o!Z1bB^@$FyPU9EKFyE%itj<)ULYx47u)i'
        b'aSCJRk})bGn<TjE!=jSS2K0H4gt4Jw<*rhVG>%m!YKRFKmxmD{FWRAQU@sNnpF!`+$qC?9E@s#LZXAFqP-gazb^kkbGCQKkBA~=`'
        b'6TugY0)2ZRY}f?vP51S=N&0RW<3ULJu4%uzm+_?c+AYM~pj%!dtVhH1)+hjV-2BUcJ@3b1?vcwpZ%cDv#0hCAY?yRuX>muKckgWn'
        b'48bsAHQq+(r7qo{Lnqpn+)G<yeJ5<sy39?!3?@+#Ar~YQ_elzkde^^GK;O=jm-Kpy1><}bn(ZrcW~A(@c)AV5_R3v^^bl51Y)H$e'
        b')sEKh21#4r#)4P$eCrjqcw52WrY2oUO=N&6p<Fkp#iZ0kWUuij{z})=yMirGv-R7CU1QX`uhg1pw8c5*GV1_5#Vg7y&W;%>S9)5O'
        b'lG5oL)|2xv1z*&5w=DxJ(#})A8wGWD{FG!#eUq@RMg~plbwc_dBX-&4)zEuwZiR=C-o8ajX4p>*J`fe&1-DK9(D2X3$f?KlhkpOs'
        b'mDA%t0vPkLQZ>;w4@*fQq|e+=Eth+rx((35j#ze^_U#Rp*Pp(Z)Z_Ibyc_xk0~$qv4)Z#01EP6eQe9NvdGG19ZCh>)$-&KO`~H?;'
        b'_>x`zE3F!?Tq@ebE?rC$E8~c^-I#})0;EC5zfCBX7H;2WOWnq%GrV)^i_vN!dAR*v(v7x?Tl|SIvPhO=T=ylONJGd9u)KNc@QZ-2'
        b'9&Ym>-;FznEcNej9$(70hS<Wjzs#Uh^P`79yEpqa?@DMZ_t_<So{yjBJaj23Z)?=Ls;P=4OBVA$$3sh$dv_)SZi6jL87xsHePa1j'
        b';(rbNl5;Ud1z;P<vaKWB+Ol-{)2g``TKUIqA9V22j<`0}?a2D!!-*Z^y~ppi`V#^zCbx4CE!KJW5|CQzOB#~M0<%r+!MG11)TXoh'
        b'FOlY07$4^smkLD#)c)2bI_S{OOMOEgY+>jv+QKpF<!#)Xm*~0W(C*Eb0>^)$kGw5ex4BS}zhv>hmBz;m{Z851VgmNrQcdP!RtAQo'
        b'bo;|9X*Bc(-bH%T-D29Z6+IH!@C&l{(Drfg5@mOGw=k})E>ea?UXly3(Z1G(f6@IE0S~aH8tYfUlO3wIbN6WLE7EnFcqD&$m1HbQ'
        b'Oh>RK*<uY5lp!W|e16yZ8hk?%Pqc}byYSqUQqZ1r!kqIGZ3TH^fAZ4oWv@s9(AhXrG97pyzJV`63~wK4Gr~996TgFYRj-G)3?^^;'
        b'C9IJ=K@wwGOs<h=;J58I=#j@SWi3{(xlp=|u&xRZ*WX)2c)z`g0^ZIk(iKRMa8rH72|ni|FGd$R1#1+A?4Bt=-EA1<G+v_PcSvhW'
        b'nhR6Wxm3LKk%2gnF4ZyCJ0$O%g6NR&{ut)Ts*V`GIDr!`34BJWYN9~AA5{!}pUM3^a9?^vYyazB#viO5P&s&RI_*b1(KZ{|UTKRX'
        b'e#GWm9Dm8df#96ReKp{4PW@HxymZH&bcvT#sk`k03b`1I4vruR!-79*VpG_ngZEI(g=dPmsVL^ci!qmjmm$Z)Wi>*M!14z*AmmXX'
        b'M)X+W6%_MvkATh<Kb%uG6BYAt=0cVN&05H#K#cSDAQ-VOma;{Xodb~cagV`s5jWG6u4FZ+F6XsD{e75%pWyAQpe}XyWarhvEOm;C'
        b'@YZA6|GY;}^H!to2X3Xt5#F7s^W_=|p9;N~=H2414hp<1MHN-@`n`;Iq@J4~xhm_IkWnRD?q%die|ysdys};iyuw`={MAOBatBNV'
        b'Yx_-3b}6-rkha~lpBZ#+A6P7zVY7xz60uDDEsaDl5#n>~Eu+L}BE@IrEfX<`R?`HQau&u{B{5XTcoXlK@JWzS9n%(nhb5m!@-Xhs'
        b'@l`TjJMSY4;f=Wi?nZHxl$2405yNWHz2c}SOe#L--9z0QXRI3@ME7T?%y}B~0;73hw)u(0=0)yp1BmZ0584k5F2)yS<4+jzg&KT;'
        b'3eR&CN$i0^?))Gru`IS=qy;zO3+!_S!6mf+*Px>)+WyucqYODDNh%AWv5-a!rG5#o-8*P|HdLt874o`5qwc{gu4a%YCaML3`)si8'
        b'(?JzM*mP*U7Zgwtr1(Ip2uggQqKcOqUK_NpA5@VFjbtHrc#u^B53wvKSCJ;9t|il0;9rZBVZrIpX|iWTy2IdkNKYIxLSK-okm!P%'
        b'8ED;V8R{nVZa=}jIEXBoVmatid)*)yvFY{4ixu1|5Rdb?x1nPSZuj7(Vwt@ddOiibUhsrX`19+SC<m{oj%({saDN!IYX+8;qn$~L'
        b')HMoj*&rf<{~RPO60Tq{evJ$qP{Wo%GFyg1ahnGtt`yH@1A~IC$t@bBNs^e##S91!xQZdHy0EwLjsP0*C&HSAsLg>NSaO!IPKW1x'
        b'cIkj{EE%n+ov}<K;QJk=y8CHIF(LSIp<t=u`o)OdB9Id@rG&Nhra>44OYnFJVNJ&9`10a;sV~j6Pabs785AT*q$CUMn2zk)NrPZ{'
        b'dL$DVMknA0RwoXsbEAY~dIY?Jj3O{xZis{4OtMcLbgKsGc~HnFnV^zQD%;Dh+mfWHs3=g9l58?Jy+T!@kxhrOfoD%UlB&>1yL1qN'
        b'nht#ygUpVSf_t-9v^D%9Xyz3h`=vhrUeYw{fnPufzP=Idcgy!2TPPkGqmf~xgcOdkAUqL-Obv;_qx51JQ{TQFsR$&k^sgXSZw)y0'
        b'sIP_Kk{9PLT`cT*G&3%7iSapMk1q2K!fU~VJ=5T!Z3-p?E@Zy3!tm_?6p#Ozu;yUg!HeL^h$Dg6t8MB{o=h^_7yvV_!(zWWAQ~b%'
        b'u4lk-X}~UnaZdl$m_0RMPz?%2Ix9FKdmN~SRBVY+5ccF|#@P(r1GA^6EneaytR+P1hlKaHSkhcbd1G)$SyQo6cyj=wrP9|%;Pa<5'
        b'<0QhK4ViDW3Gcr%YdRfIOZ6)^7V6hJKO7LOO@g%%fqf%R^n?YKH1jIa_V7)^p9W}YQFf#A(14JV8?|N@_wq%JbcRg`=|vGEz55GS'
        b'KcKPbxLE@z5K@|pDHA#W05n%+NzVk)*BeHwAsfAC!)kuSx)X*%?YM5;{!7v@YU?l9Z0(X5qOCWawy}UX=)gbY{dboTK(IHt^9YG)'
        b'1UsF{gc4hR@hDdnakD@RRDRodm;uSnPD1O=Ko3O1l%hob|4kXZH1IFVAn)S;tPEZpc%TeG6KpRU%e_Cq^H`+O-e-Q{Rt?OSiqW_k'
        b'*+k|_2_gL}UdV)07DHhy{0arCO0IB#CswEfIQPr|6jKosHAE(+1P}UQ76X|zgS2FFO9l)J&|CW(17!9@5CUZO!yo}7>@W3(g}PTW'
        b'VZ5V=)DO@ic%kmMMScw7jT#aD<eJ6P@t}mu{a9JeTF~k~r_d2&-FL@OIZ&q@NTT&0u<qGNj;Xgy;bsrm3kF&Nb_dgu)E35}R!(x!'
        b'!O!3QJIuDL6vp%#UaBRmKjIxP@w|uCO8D&A+|L*6Q|=o8OcYPf?ucpg+y<-8@aKz>up(N9VDy5^Ugv_QN-yC;ox6z3hG%bI*qR>('
        b'`BLypPZ5gX8;hJ%V7MK>4!2ED=^tThSjxc}VYqo^qY;IiJe*)-smc$Bcyyf%WK_NcW7c&)^}^3!^T4n+-_LLyybLfJ#iWDFf*k(f'
        b'V?ek71pI!NnD5~pK_wed7@#ao>Eq_WSUcWB;cwte2hfRVc0h~l-(9pBl{Q3dkJ(!;h;%g*lBO)B{cjh6sGu(W{i+2p6kHVd*Nf`h'
        b'=S3r(D?fO&3`B~B1A}n4g^L=n4_;hPR9-LR_2u_x!&aZW=t#|VICHAwq_^$`xtvzNKG4E=oR7PYTz~<ye}0i3$4kC#Z3y#bfsae}'
        b'aF6r$1a9rc0P!);<@nP#)&v+{sV@6O*~~MIJR1ZOKcI}9tH|5c>a6EEVjv5u)$@7*d}J_YgrZ^mUJ@mJ`e!f@vtc;6Ll;HseHt30'
        b'6s&FB9Uk9Tj_(KEfcE}s>achdW<)!HS9%!j$X$z{ZCm&=TKH$QUJG-3FGl@LNK>!?Kcjw<1e_%6<zIlRF#R_|(ZT`^=Dl?bX*1o$'
        b'QEi6rbG~)a(K>r5Uui3Ft=@W3Xw|DE6v$}@zJFFG2z$@xdg1fgkO9Jc){HF`*(8P869wrCq*HPd)n}RV)+BU0!#YhAQU1C3SV~F>'
        b'MhG!Xh#`SSW9xsqn-MG3{ERkBtDqs)FGb^A=ghuflZG$?MX03)Y;<;{@WJdz;qx%eMpqdHbXcKmEM>|{*~-H;WniFAg?e0KMvd$K'
        b'cDZ$oYbDTWR{6oy!U_i9c!1DKm97e=umZ^;bQnklP|%#RXO)F3SywYv{$AJzRMw#^D`i$MzSs=Vnkk!@1VUS#dI56KoJ%QVYFDma'
        b'c(J*Sttq7RrOL7nrm%x;wXbS!zR}!jrqzWV`sQY;)oFCjyI7u*n|hOwzJl4yE;jx4qOF3di@8`{nwvzA+H12fMhqD+aMX!EIHXC{'
        b'z4p9|q%<p{qDX6&^X_@ujL`0@2IEB@(90`z8Vx~2G(jOBBFQY41&b+*n{?4uqFV!oOX3Anvd-oSx#D$&(hw7s2WnN1EXi@)zg@g<'
        b'*vhpR?`9->n{S{4$Vs$#_JI)z24%51ubwp)<9T2^g5kxc$Vv0#ra-9VVIzq@?*D`>6xZ9j$0Bx!tW_@JOu>UAjUOVf0h9#DX^$v1'
        b'?kfq$!8_vo*3==9d&Qi~5%vb10dhf98>zqwz~l~bKG%j+#UrR>Lm0*il4UcH+5ou#0;f=9au_uG*B5}*(cO4RQauLB1Cl1K(*DVL'
        b'P#chMAG#3H9QylJgW9kqhQKzCpg#2qQK$?VE?&@(St4d-fLX`^v|`$jiCgZLUIYfQWrg&-4x>VRtKNp^MaIGcPXB&Arh`0`VI;G0'
        b'(B9zcy+1<7BSzg+=i>yl(Y2zkY(2YuQ&h>ZyBX7@MK?Tsc)5)A9sGSw1yi2OmP?ZgqT~f6ZTR?t<8wXm;qt|#1P8bnl_=JwB5<&d'
        b'nYhG=U0fnHqDIL>qg4Z4ptjskL1`E?MyX?C^3WYqBpN#CHTcNf;DtbOmW_w!QJ%AQhq=xRkb{YYWsM7Sy%&Dn!U0TqA}keG+tQic'
        b'oKSu|T=C3U_a85iQsZds%xVPRy&!(1?Nr!Mb%CA%S^|9Qr3#WXsz?@<$TkYc?iLh`NRJ~pyNlg57mS2KLkI|hQOEE)qs5@H2;6Tj'
        b'IEWP;angUtG=u?EGrUm|4{I!_EIdOIb@6Mpt_$41Ul2pAIwn>}T4ty$nbzo$w2k0ndG9{3YT9nx;NH2glt9z;S_T|LYyJ&q>Uokh'
        b'*whjKSD_&Vv?&_=un%r>%PxTBu-oWfb>V(c&_F`9=t1Bd@N&iOVlvV!3^nUt-sfF#96Sw*Mj#M93KrH|c@K$m>z#XG6Nc^~)txG_'
        b'G9&0AMIs$L0zSW0au)-4+~E{nlz`lqP8`875FgSc_zxOjb;Sjwv5IoNju9*?>P5nG?4;@0ZH1<_)ob-WG?!a2bGJF;LQ-|`vz$On'
        b'tozD2v`J2qAy7HIc?voKSH>r+`4}miObJT0<KU|`5&ft^x`_MX{85T+WkJE!CsEajZR`!92e%}fma66xxtc8FvY7e&OhG#S2F4@%'
        b'HYb=mFJ-(;eFx`H{_+byU2%ktqlrfC#-jvx{am2Ml;#^EFliLDU2EfhIJYl9ty~OGRlikdy^ut^KS9m&a2YpO&E!VTJNU<Uf4(rj'
        b';*AVYPTl-G%>PX*zbMGh?dn?V_usJIq%iKA^8wyoeZZlc=)QU$37jH3_x?Fr<{%R2ct!r(GTZiz&qVvU$&+O@soU6mX44ylbRCwq'
        b'EGZg#UBfe*d_>z?jJtY%p97TmFm|`>fF5*qkelN7ul3=d1)LWC<Vb_8X74t3{kF1QjL-RKIXC%kbXpY4#+JsUb6-Fcu#$Use4GWO'
        b'j30FSEHyG@xT(m*m_g}v+rSxwZ=j^%f1l_1xehL!FP@QpM*Wh+!%aonOiwj_p!9GS;oxQcOb~j=(hVN`)GyjqKJHOuTEW<)D_x^w'
        b'v+DSj@eLC959cBqj9)?j_kUUa+);`98H5L(%dqb`zobaYy?;KfC_Rola9-dhgC|<0BIoK;5{NbpmgS%oXpUd=wu0TUt%hBD2yihC'
        b')4#sarC)n!8_{M!VG<7t69w@7X)!`8Gc#+yZ}^G3`#m5`0I48PvSuQQl24M9N<wf;&w;;TBSIMdJV}!47%g|^{5~=wERdRL3c0J!'
        b'iF=GA;s%KikW$>n^Q2`a=RWU2ZJeo+Q5X&;K?$lN8jC6-q#B&taNZ}rCFfIC9$j0lVFhj~pn^@I*y$U=zm~omb~qn(I4!S8r0;}z'
        b'=c7D464tsf>IbhO)#VuP$I^|%+oh4|Mrp*v;HH9}V)cOW%P<C@r;w-e$p0_~4si_b^T(<sMaWbZl&g3Y8AFEg2MlYY&~goy60Kq|'
        b'Od9jiRBz=6$o9-<1Wo{aK?bP8$~9mZ>&4f?!GCz}TgLZuF1tj_SX|Iy5pzDh593k42%|=$6b`<M%4=B%x>e<of7Xu?<%l$67BZS6'
        b'$`K%lrnb3IRE1z?+aEq}8@00^v)||!-72IRO=(K|xbx7_ntxS}tp0{O{=9v#f8|xekv4N#Eh(F2mz~G_yL{Trz2lZP-RTdMWCA7%'
        b'PEx>8+Oc<moo1h}O7Jgdx9=dlU07{ze;t3`lkV|XG3r|ecXz)hZIODPK#%EmX1h=IqfL|T)4REBdVJ$iePiR=$k8zlZuahaA2)kp'
        b'g8k;X?S~2J8SJC;MB7Dd_VALKgtuRuYx$XIOT+B{IJYz|r39I{_Wpk8OTkaF!(TdDvKkj}J1Vgco(pI*>#4i;i|6)Bv=!2QU#j!4'
        b'`t^5berf1Cw@)HyY)hACEzXR4%J6x=pqZ&Q5<r#?@eWR)Kp`4iqEgzgp948%t77dv=RD2~Veb0|e}7%uIfrJEdaf`e!KxFjz1Pw1'
        b'T|c6C_cZh?1hC9qg!DKz{McP+Z067C_;JH$0BLfNd>?8!6sJ9x&|bT5skVMh^*5+8^8KaDmc|KlWy1W(K`S7Y0#38N@SMBpoDlaA'
        b'+P|6qkboRBquxeUUeybX4csHn1f)>ed+q+fRepHiT@r@wyGxZXb=`mc!p~p=HH#@Q!%!p@3@{s-niGH_!0hK)fDRPs&xel@H`q{_'
        b'SK+y4nbPI}X_p1IGw={Ek{>HBO5z*B@PPdJ>CmD%V2>fcPIT!<-9PTJ8quY9iAiLbE$;V346_aAfc9MfN_&Tj)Ldad&okBCfSmT)'
        b'bK`>1*uG_;L+s_}cy6+x^jx>r#urarSf2VeA>D}e2hob$g+-|o2&o&R3Enw@Q=ZGRq&WoVc;1=BEkDQe%Ic!D7@jBLWnIC!?#@Ht'
        b'MuD8@(rj$i>Dg{J*z&?~c}ziGQhoZ}r>A*CKmK2c43@o70phG<1O$+v1zN+&Y;5>(X+SG!iSA!{MZ%fRwem9&MaZ!FHDkOjBXzg>'
        b'_H9VXQ~1(ns>gMDoY~eH;RZ>`t~>4tz$!D<hlv0;*(b*uBtGW?bPo)qxCI^swmm^vJO5lOmr>Kf*6Pl+Ix{@;-`6JGwWfp-VTStA'
        b'Id<vcZeXdbO%op8G-uwz+)Wb*>*R1yo9F1oF~y01L~Cjcm3*#}riJVK?s!v>y!1rg%1*ck`sneZDKv?eK~e1R+4|2^)(K%xFW#-q'
        b'Y}L*S%CrGl^6=*>`v)KuRCSsC?g3P-H8zaVagMyN1PxPns6Y4)Vy=?&66y3XX85`<t5|)u)5m3O`a1zRhCBUBx21q}CWO&Cx=;Ji'
        b'l7O9zO%?JvGsG~X0@LrZf7LIPWLeY0hQIY^ky(qScft!jKn32p_(GrbRcJU`kN0mehQWS-lBOcfRB4PHv~`BWCVJkyW@-|>)Nzym'
        b'Lupx^dwZXFo&d(1V+$&tfpQUYM+LczdF8QOUw?owl_>A1w_pNc;*R$VmJCB%zx_A;JedK)0SqjlB7QErWW9+y36cb8EMA{Qv1wGQ'
        b'Y8>!xxftOn6G;Od=9&LcgQ6r?!Zr5?Vy19_FndD4k&IeBMA|>;M+<9s6|Y?7<7NpFk1EK3n_KoWQYPS01rOdsftU)0tpI)FLNhc-'
        b'+2|t~Yih(mOeFQfPw*eq4Jc61IFJEE3_yVE8}AnZW_O9^3?vaLqnua4Z-yigG@FWevs`5MG9(a?FIF!4Vvvl4@XAGB%qQv^=;i9)'
        b'A>|U`_cBr4tX|p|Q8#6xx>@~7{{wYXcAw>sUwMp|Fx4^jNmA}N{Q@`F!_5<yds%&4u7jH|6wNX`)#oX)3L2}gXr`lRs{1?|IW{Ps'
        b'$wi`tP0#nEMNpCeKcnO~B+?Qka;~%=^yTt?p@;<g%OheG^!LY%OVr;Hghm2eqx$<-d`2?v<5NrlKJ)(xpZWia&ryYbAD{UmKJ(d#'
        b'?ncP`zfs>)`+rs6RNud-@AUrvuD+eKBN}{fG1rvRUzga=D^_ICe4Z_Ma#i5OlkN+>=!`a<`=`E$4Y{&N!6o%Oh$QZzeuqUSE+bKM'
        b'@%`QSXC$F-vGrq(yY~4Ii7vhaB!6fX*TnSKQT<5^gD2BY9B{WGc<98A%YBg(JBDr0`HakG6`T~nPT)d)4ofst^i`3HBl_tr4q_tr'
        b'GvvwL-F>3Y&scr8Z+nT%k($8$qt8*KN{e#%(@>~-I|{2yzrh^-BuKVRMoBONN_}WMtNkB+wO9Mn@&!p%D>sE!c-|k{;-TY(`D+^#'
        b'LdVFU!nJpszJFtSbk`Q<&<+CZNyF8?*7TSxvbmj_`6IYOFNB&0lzt=Ag(8LO?mBnsQNlZbd+L6>Ng%8VWYX8*Ie6C*sfP)x4@b4m'
        b'A|mnr)daGmml53QzN{Z-65LCDJb`~#?%{H(6Qs|R_VzyRFMWc)eHJhD;ts88y=ob;6r8E@BHU3#%oG3{H?I)VL!{wopTl3oYaU1a'
        b'D<aXl^B9@KZ&?yUcn^{#=`jyh+y}UQeO(9Oe@T2yM`9a)1Dqn74(cYnexQE-9Ud)DpGy*oZlX-|p(c0_-UT^c5)(67uD<Z6qw>0s'
        b'`i7sl<9@4;B$BISWVU|EDv3iYbrj>9RvGPY_Idsk&O)ck&6EsJW6;qt&!fRHywMl*yOwUN>+dsE^(E1t1Rcecdp;U+`{uqZ$&xim'
        b'?x%aj&kV2k1^HBmYD$1lF}%{}Se!h3o3g(Oh32h!*zM|z6ms_kNR#2EzCd<{VODQYg^qn0ZVEw;KvL?fWYed8b+7id`eWUCREgoa'
        b'z6U40)PF}8Y{7y&I_jnV0?n=HGw6C-d8S)c7$o!oUa5^8!xi@lTt*rZSsE#QWkg(`gQAHx7ghPKLyRW6UPoLN;ruF~RU=!4j3?l`'
        b'D$#fXzN->Tyo93KRScxSc#4FyQTeHm5s7MxA6Od250JqGrjKYEL_Pwx_kn33o-ztjHNZUrk_Uw%^OY{10gV&{NxEDaXbAfu>0krz'
        b'g&SF_RpfksK2vAt0}0YB3R9Gn_Cm6odkmff+)UGCBvbr0sxG}xpRe?b02fM7Xp3hGVz#Z1q7%!?Vjait*>oEnN;MP!zrW@UhTX~f'
        b'?CO+ELTVl1$-lXFGU)CH=z^HvW*Tw$C!!fHCnoq)GGoyCI4&9yvz~Wl5ldqPXM7f)CODi4f^!`2OboU>P4CiXDWv1U2lJPrxrHE>'
        b'YJ5uYKaJ*N;==aF`glJM2LAB)JBD9+*Gq)6IG>$S75AHC0C>H2>GURR-*2ui`)TvpB)Wlc-xLK@JT37r+2#N;Y3eyj2%3fTC)<mO'
        b'Hav{(S`qwZsGd4_*Z`GS?~Z^07w{|Urzrw0FO<aHX)*u}G4SlZDng6n&h^ryA1z56&v)bHT+*^u2R8xK`ER;~R{b&!&rS4h$N1EF'
        b'bd=CKLdR{5(*F+m$Q9cZeCv1Mdsb{CyjMm7_)_R^NxH)DSuc+-b&#=Wt-%18dhz940)H&QQ7kPlj&gA01TJwIKU2_ROk2;0-PPm6'
        b'KLd-3mrQU-CbH=aS|<EKuSXKS``qqeX3;oRR5mG@j$C4FOnE=fN9EAJLpIC29574hICyk$Q&7C-yI%E6Sg?g@Ahb^s4kAZgA9K8z'
        b'kj}^I!L8vEpdo@Y2`YCu$D>v_CkjN4!#N?dc!T@zy#a2b>oDta=9L5thSDBz%Wawvi=hPqDE_6#4FA~+4tzi}oitBWne&GKXfQne'
        b'--|JrT!T+E^!KuCqRlAIN-~63gHE|JSbJ1tGQ*%-?Ga<YYA{Uc4HQo<IY2c%(Ob8;xBkb6pzUaka*6u4B|MRnS(M0S^{DVfkV_b@'
        b'Gx^bn+DZe*_6CY355G$_nS1Nz_G*84sBUF%q=US_oz=OP5i?_c#dFEjJ80S9h7r^ZZzo#z*VqfKV@WZ5c|OcwiQfLOSozcSCZg?I'
        b'Wae^<dqpYz|3=pbr1Qg^vL_h8czz*!geh2ni)2;l&gwyCcuOS^U5QL#e-q$fK;re^hqy<3%e5E~84!5udM%LHW<+9X(|@B$H@4YF'
        b'&~8{GnmC+-ryA{oUqC$e;)qIOAftsq3j^&}NrV<z@0FGpNVA5FHg=z=M48bO{hzR;IhmB0#N@-Ic|0jG!!v14sw?f)ZY88ojbP<<'
        b'd4@AR6`)V%;^lP<Du4&`M|jmk^<GI(I}IuruDs))#SSbtOzds>N6!_Fp<6Spsh}4{0MAXEBX1y*EcKaWD$x795p9d|pZ0u3^+xu5'
        b'l^j%dBuYKk1^hD${+V7w=^H5!rcaZuBRH5KCIi*Tvt>ry6r|An@DaRD*V`CmTm9JZr4WbrcFKeNTzW#FZb8YFkd^uehNkypCZKuL'
        b'rQku|LcE=ZLlS&vG`$}~v?Y(AxpL^sWIU^m8}7+cl@qyH#_KW3JP$)Rg`NnWH=9lkeZ>a$;DfRb%^)$E6u2B(vgtX!eQQs^zv6Jd'
        b'phfYDR_B6l=b|glh1Z>V^}h#!yTHReex1v^!Y%CP7Cl3|+F8#*%=LT5^}cebif#Q<xVfG2cd(v@a9M-W)xr4RXX~}3`&duish%LX'
        b'8S<IIRg;?%darQ0kMZlec}-;RKG~TaJ+0!bA!&{tK0`nifjzm0WqZdH-XHIk=jIMX?W;Q)Rq`s`u_4G!32^d~7imubE8l~=D%i5J'
        b'8=InHYv1bu<=`2YTm~9IR3rSd<V`En+{=1u-{}!nQJ`>K<w|~Ba^O!$hm@f+f|CnCKBP$+$YD3dz10(lNtX6tXxRji+@He2o@v(i'
        b'!f0uO53O%aHAVqm+ulX%^!GfC^6KH`25$gyN7}ejK7;q0K$&t+oCOn!ClX3|g-T)}qo<(*=w3csld3GoW6R1`fbURlj;;H=2RN)='
        b'PH>ey0&nj)i}vYkI2+lo(e}Z;at*HCt@LL$d;GY=kLj0gWTq>@sI;#>Yg>xK2@Yq*-gv^g{~j1LSp>JPM<{x{t^Qu!!JaZBIOz;D'
        b'0zBY)iU9XlNVluc-gap4;Ww53>CO7`ZD^;=znv{BqnHY%ekM~U8UcI3t9;|0VQCNV%n>wphXykg_Be_km)6_^0pRFKiz(&RJRU0?'
        b'bRqNE918+>A*qk}i^yr1&6ZIp^mm2TFlFUz<yo-tuZ{XlM$r#LF}sTUaleXR<9?%l*so!~QLpQM*snqi`&HZz`&HZz`ypQ~Yc%o)'
        b'pZtID!!$kr-4FYv`(OO9@jd_ShuM>QBCZ%I$r7{+Q;P__zVJGyJLBwW`P<pLCwgY$rlAlT+8emk0(gr^D~6LdE$ab2L7JzS0^q7I'
        b'a7UjNXEdkSW`#_o97d_h-m@{<hy<BL*l0FjESgK?TNo(s9_bbf8&F}5d?P*u6in0H9wtGqF(+#z;@U9t0!AqZb>jXB6-E=1i6NGg'
        b'llbE*iMeT3kH$P+gBzd?7$FB4k705&Gx;?t4A1~FqmqLp?QX4X`QWU|oOG11{&{40`lu`fxi~!OPIaR6>h}U3>p18_tJBS~;2b1L'
        b'#9g9lL7CtPV0B}AY@-C2P(Oe-5cR`ETlj8?L1LhKxR=fbH5h^x^N=<bpm|S!-?ZZ_d!FhfA-7~HA^j-~W@rvgIGj`FNXj|=Glcga'
        b'pb5AQ-Qa)lF}r-dIGaqB@%m=b=|j90JsYH#+CsTEc9W7BfwXxbN&v$_XCB6WGbG1?T%P~YSbd-wknDeXWBL5qAYw9OVxcgfHXob-'
        b'bY}Lkv+m!V6(?L~`MB8*k&4q9R~ZF_4Bjs?a(jW6ZHN*DM9Uun84ZaUDD_gr0gj{|*uY|n=ca-K%-Sd(9N>JQS;hvL-~iiz3?KE2'
        b'IY7l?=Bx0GVu(vn@C*nUNEk&$M4uTQC7UijBM*6whcnxn#Q<Ula%k;kXPbF6L2rvB=XN)v6(5g@Va}PRFO<!#qKCZdEL!x@!LS`H'
        b'_s&_-JZiPCs;?t>Vs^lp(-GtS!(C3_-9Sd}c&dBltlNn2()OQseOyk;IKsQ@Zd1zHx=Cm2S3cz3j$9`ThmPU$+@IGriSyd7E-HBN'
        b'9`OCOK{T;#Ie4dwM@t1v@C@wVp){2NirC7vkkM74eBlO&<ibL#xl{=mg*;m%Vy)1IR!jlb3Pr2kWfI+n9MnS->fWP~eR&QL0`uWR'
        b')@Bl8205cs;*bNpZvn&=Ag}<z0_<Ny74AgI8lE+4&VndF&wk1R$T|S-0ZWoIOz$YoH_kXTbKw<c`UWyhrW?nLavG>%d+56h+}CH4'
        b'7SM@2Z*i9*<h-vl$j_$h(n!m4Y*}JQ(SFiOpd<XUECn0G`z--ZZ;ksNdwROVsh8djcWdU+NnKrQk4hRSYcz7a_I;^dE*{~D-*J;?'
        b'4Y#_}Zl&+(=;ro!qw7^-s0wg_{oiTtQTz7r{^Ha`!ulA-eR;;hKVJRW5QX-a?Xf@|+rPs+e7ySW5g#{;SFW<4C{E1~)ffZ>8HbLr'
        b'rY@@T5{$<XIvP#rI>G`0RR&=!&{d*G*qSn`vK+<&Qe{Wj7p}v97!e>}7?i>zEc;+A(B3W}K?@KuAiM~OI0t>?<FZUgSPM9EDN2)g'
        b'WvS&)C`bbo97*!rBNh<F4ke0(i$F{@6#rfrg>ZHv2<A__YmOi?wTYh;agUj|oq-SG*^~kW*v7w5XtVb*5b2MBh<3RsH1q(3o8@t4'
        b'fcmfjQ=yahpdu4HM1d4(<>mmV@toPi2~e`RnPOQAFyV7fwTLTaK(lzbM_Zi+-kD`;rl89;CJNXuWmbBvzngxz>Nc(LwSQLg>Bh#I'
        b'wFC1Nha3O6vEzJ`1&xhwJXN!uQqP~@{_UCTX=?RjV?D}M;+il(cjftOTa`6$F|N&Q<&mM?O31Bwi>+Mm+RStvf)xA0ZFt-4RYHLv'
        b'VD>Q6_y)SA&I7VxGvog=DuUeNw-_*cYCNcz>n&yQPhlttU4@cmhm~lB&SpTp0SXsxR{GuxM{0z@0PD^6v9k8LZm{8MkUO3MWlWou'
        b'wU3?wlkR@8nR+Nw)QxTtIm`y_s}PDG!X|BTxz@fd2a693Juvq^N}~~#d5gb8=Y#me54!m+TY0hZ2L`CB@<`VuwsDXFdTQ=uD_?Hx'
        b'K#W~h$-Z!>v4TM~w32OnN$EIv*;c@m<+Er%a6SX1W17p>08N1KOJ-WRDaeBZ9$q-g<c@}LH;gM{azoi7#N>r@l_2&aZ;QArv(RmO'
        b'7x6QgN9L$Ah*#m&KE%n#iwJ2}xNd6q?AF{+>K~L`sEg-cQF|~nIY3~b56~S_<A}B?VeY4{x^riEo}pidH}y`cEj=6%JNb#&$qW8S'
        b'CqIEs`X6+1ga1J%Lw>Q7frFQ!pZ-z?O%xTd0W?cA+R4DdSN%Dthc%$Ol3B1sT`!<;1auDxJdje)jLJFaDs=2YKkc{AAlde=(tNrL'
        b'lC5ahnApkpk(BD@W<pYb6rljTiKa_ki=rFR-t-&n6B~EOdfKnJZf~ppqxndeCHa+VbnzZtzl^m1{R~Z6=2p>?WkyGK^fDEA=$7oi'
        b'R@Vmtm?b;b{m~f|4WKO985UKt<4>3^hjD0>mc_}tOK56ooF!XtDSl}FS&KwgbnqXAIgDkl%v{?=r#g}sg4(OzTf|LXT2SO)u{7@4'
        b'>5d-UAu&ajXp53<bO~Ci{CNoM+9GfSS8XgTP!_3@Js_7$(Ww=V#pnQX_w#2QOCM5KU_t+i2F37kvfzrO>G+ud8LLf~cPs}&oP8a`'
        b'pswx1e6ZyO`jh%p`R)z&PtTxp+EFm05jDSh`B4e|i547&&{$et^1Z^op({XUIJ6UnBv_K%{mPlhX~Zw1|IV#lj+FT7&x3xPjtXex'
        b'?4gZN%Kq<N0sn|Y@^QKUo~?kg?cF&1ThU=Z!Bm&?$qOsW3GW|A(q_=;{B!BsNSMFLV_y3;I?ub~TePnR=UzLbA*OMko?)@X$WkH}'
        b'ox_N{?Y7A`+J=7UP<f~PY>m5#?prjirDdC9&9#%x==Ez`qivb=bb9_#S+^fo?A)r@{xrXR@xw#=l?OZr>d|%}Ikt6-2uiM!Q(F}n'
        b'z5v^Lwj-e+`W_v_rs;v9(3$Kw{x-qocm1aBI-kqMo|*3s5+8Gi&n&Cu3GCT3<s5s+Gq#)K=%kwcEbzW~Zw#Jh!PAFIl+UHB@Msd3'
        b'ts$_X*OV$Vo&M#PbkeNA;uDJrjKt~Zim@4qi>2_W*s>ARCT61r4RrdC9w&pnmiV`LB_<1D8$*~rgb^W(3t>#Ctgev0{x{uh?x8Ll'
        b'5prSABUH@CSP>^)6Q)P2(Uo)zhPEH58RB_5M9aK525EX0z221u2t0d~{98PJG&+esQRj22uRCM2%`uD3%3`x>jX92G*SfzsEuKiL'
        b'zRtyF<1veIWihT=gU7{RA=(~8tySS;7+c~{z0zOjTAW9vULm}5z-*>Td<<qubf4%N%2DRkW#>^r*~fq#sDw@eBNY$?K-F8mhw9%Z'
        b'ljxd{(M_D?ewq6es<6UCc&CCvJw}5oSX_=)iP~M{TrBDeVI9q<A>aK$7x&}oJTuSd0&J*(%)#g+0EEcskKqUkqUkFzxYqxTTukV?'
        b'j$UPLM$c&J8Hb^*GYoAR-6?n^%;L{WKMX^XK0%+8euOr4EkH1WKowqeXBT?4h2CL32+w7a4LP5Nu_Ym>z$9*(k+z00YslLi&iay+'
        b'Vk#07=MxF(sW66zyd7blW3qlE3G`;P)=u<B+7U)H)+*k@7iiI2oU!gB2p7<u`dZS0C%tgamBS>ZxpLU19bFbPpixg#^J`0vjcs}D'
        b'v<8p$4B*|ecj#Q!wzh$KTefa<s-kLBK0B1FENao`eUz82qOkD?NCn2k=r#?a!)Q<}X8|_n8kTs0q?O?HkmlIoO?ncK6_?WJ412qd'
        b';sTigHIZgaFi+G@Aq@pxbdDuk&SxvM%g6Bk6(v)~lq^G+RR%Ol_5h>a5{0e|)hM~L(@R#!J$y{vwJsW6)xC0s+ybfZyXcoed<OV&'
        b'=vcMfwE;Wp&td0D#FxWepgAZ^gb<@%fxEACp%dlrk~F%E3vKB;E3U8Mm35DH(MbK2OddnWKzpn=!<e?=mUSR<-gE6^r)gPW+?nmq'
        b'DS?bxS0P))xNezTu0l`y!;`8S(aqFp2~}wdqdsk;c<!?svp?MBkl57uiRwLZHdk`Wdcyi7M$3GDQn3?>i{ODh=rn2t<~-1a&Vp5o'
        b'D;m-0;^V8T$9<I6pOQv+=V93drXgW`ah6In5(H_+L4cvnf@T8kVlgHf&7_gS^pqGYd>msniHDW@IMOWDm@$=^GMXjs#ivDI6=<EZ'
        b'=|ZNMJSbsMS#bBF)8b+$sS3x?CMZ15h)YNdVYFaq2_}U{7Erb=MD+(bf?*Q(DFL#|jJY30p90w##ZUDBlS42ucUI&DksW~<n}^_A'
        b'2p~EYG@l|OFui%GOpqi08D{z@ObvXRhdw=Q*vBE5n#c>>D84YMA~11iDxF<-?$q1ly3KPG#?1Wb&daArd8%zjNL)3XGPF_Y3c6gc'
        b'xl{^_lu;TP;vXdU3>PEIkTFe2vj7X67@Ba+NKqy+;0hf5KOvDgE&A{x62-;^IXu9T2#t46MbL=4475(=SsM_qQ<8{Ik+y`P?T0z&'
        b'YJkH>`})JFNMF%6vrw1r<L~Rp3qm8l0K`fUhDk~q0cAZFet@=LVO>1+-^XGUZ@rNh_=B;KHlh0uYF|I)t~ebyk6#&grfJ)$Zuu<w'
        b'HPa6aFSA+X?+7xQ&g<%;Y>$L&lR~xyp-%a_YJ=jyUPmsb3RU03Vncfu%k50pP)NBvta=C|qf;?lzWdVNo`=ZXBuy^sX}|0HVhHg;'
        b'Ar{i)CXu<UH54vXhTyddo^OVOtJvVGBy^fV<o<}2r_crLac6+L%=Xinr4Q3{SHF0QCSQ~&@|QRy!ive|D-tZ9-Bpwpw28L>(AM%^'
        b'Tv58xVemw~vvTPyxAHV8Nwp<}s`u1_mhqyyB2+R=j7KMvISG-lem$WNte6aN9G?#r{Bo!5J5;}W@hO`uq+Wcl_9FUlR~2Y+Xg9h_'
        b'1Dnx;n<t;P#9|gFSDlQ+hPc;N!`V+a;Le$+97O%_Y?23Y+5@IuQnCpJ;gYx)PFpyRCo<;O^5%)$BdBw)Na-Bj$=YH<bb=yhC|SwY'
        b'y0BOiwy!SmY=V!|%sY=}d7B<NO-7~q6cbSL_gHPlDO-9dqJ*uRvDyz$i%DH;i;dmwLf2hPIt2pWm!9ZxPF9&ShN3ZD?fx%nC!Rvn'
        b'9;oOf4>wtbXCTFLI;_E2UyBW6^K|JTIW%T=^jIAxbe-cc%A^;slxJ^jyYA%5j}H|*`LmloMaKYk#JL^9`)SzXOi^#7NNGvalcz@)'
        b'($796Ds>JhzcF2@TSrDcgyA}swDiHDJu2zS2-Cx}E=5Jqpbao~7w=5r)o+&jSFjmWk-vmpx$#=Qa(sS~Grfr89L{7~;&Ac~r`FMy'
        b'20D8(c#f$}-=7M!n6%5ry04w88}4kCy;J-7DOv(m7x}5{oJLWKNln+vYNJ-Jre&UICkI<>Fr=>cT%;UZIY4;LSPD--yRWyHwj6{X'
        b'G7sBw5Z(n_^iU|M!y<=q12%omNv%#D;M7ftJcMTeN})#{w0db$E2l#%LlXf|q3ic9j|_9=v%W9x7QA`WJ=Ez*o3c9##uUD0TUmgO'
        b'j5rYn)ZUhi1vs`utzW(U)KPpt4*hY=Q<NMf=v>b{dHvsM?f<4*YEE6}QbQfBPPUXMq)%h+rp`bbQgH$MOn=Q<|Gu@Qv4oYww#rMB'
        b'qbhIdtMvXV=4iC_VW8)xNvCa!kab<SDgE^I78~%e?vFq--ZkhPcc-Svne1%{mx^cz0vg`49u?Qd=eqW>>$Xe<Ex#mfXos@3MZfDW'
        b'2tx|2=8vwXEuETZ3?u?eJ`aNneTT1s{^ndmmWJ4Xn#0Uix$9-N>=;9jryrunG~d}~y123HH1n75Y7XfAdzgTeUnKoYqIuaV50|Rn'
        b'$!y8VO>Q79PHp84eU83tEkh^QEZA1NuJb76OHT&u133etTb(>TKiE=8PpBM0cgUo-Kcd)qT=MYtB}s^E$C<Fsy5>{*=6t5+bn|tN'
        b'r)AB*-{x`h!IO90kDl^zydzif{`pppz0PT?GJIT$>-Wtrcj2b}iQH42bpxk(K8C&nx<4XCwJ(!a2`K+Fw0kNHLOQyzJ570QJ+u3('
        b'+9x_o<I`Kym36|YqftO0Lp0F+q^2{c0_j4@CsI05tGi`$O)J>(SLp;m>5`QSM|w=%XTYN9KDdRFB~fGTkD|spv@t<{6!K*r>7*5_'
        b'eh&DFAt@qF=?W~M6-}8{V9I0_9sqAz<A0a&``1<<C_-P!>Kac$S!dKKXjxH8OhM@lhgMlP_7vDJ60D?-wx@JDRh>(J4ye08G(a8<'
        b'wRa&#^Q-rraxOllaJb_;Z7VlAIG}_ykCUaXAV%~5*XrG;fKxWCC!>H)(^kiI0*?k-Y+H7*K^6wumzr4a$I;O*6?J80Yk@(;8y$cf'
        b'fGxJT_qV(8PForhIO{NZ<*l;y`m%h+W?QSmS&Ye3nc0GMw|A4~a0jihBqujW!7N)OwK#d_PaQ^_wWUP%hbq*+1CYr@?csu~UiBUc'
        b'NR>(HjTR+$xg(D^|GfjGmMu22W$;nwcOAfvmXu_A5*?2nI@Uk}O!xrG49!=zB%I1KGl;@%`aLX}6RUk9tiG^^hvEwH&gq~ytFPS='
        b'HhkELmceDqL45F}jh)K!*)}@H``QQ{V+{gpq<)1CItS#_Z%O?Td+;d1*-llzF3$LW*zxOKANCJBSp8a0+!>1>+rDZ8)Lj3N@gv>p'
        b'fIn>ekljks^q{<BhtEH<eb+OSW!`8kYL%`(Q9Ef@<4z^I!H6IgF`}qdsG@OFp%hn{%V>g*l}fM%dVGh=Z4RDftv`gLuF~Uqy}?|N'
        b'9d01o2n_Akd8cmpW?22)i0CZ#;sMDl`<@QJpYmwcN5xx8v}pl9wl@J?w=CW}zE*#L`O7y!Z8EK*WpwP@<fgaA&fXwi0FRDJ(68MZ'
        b'y_dXEEn7tH-S)Rpx~u}>!|vUv6|@mdl9=J0j-!;Inb$y|1#Jl~v<A2kfTKGsTNJ07q^BAvZDzROle-xgtmj7Wr@GNV>@8lQ-)|mW'
        b'G)$@UByLBi&rbna3kg(>5#4kxET!CII?+;^)g7f<l8(wf8m4Y>XJn~XiHTH)aJK{{3oeYfzeNvqUv~<c7<v*k1r>ReoN&!h+2NiI'
        b'xw&V)?gX!nPP%_5Bsxj?OR+t*^E!Oz@j&!GPxO9&6&r}&>x+ID9%`!C+R2?R*V;g|%`=|{8S9yEyMO2Itd6?gPEYzOpdNU!cSo|D'
        b'?+nOxrS6jW#+_OD_c$NeQAFyvF&>%CwVA1@YNp4z(ziwKUz*cVd%V-PD$$+aQQHO&xwW6e?|kt$ul6(eop=APquSO^TD~<p=ucSp'
        b'dTe`i>Tbm~G^vetHKa|rHvYiLoiri67okh{$DMVDI;&)S9<ENqe!b7BF4$Rl%aezL8mW?1Cp@@M*+WECtRk!_@F1((-<cHc$-_2%'
        b'Otk5++P$4!?aC7$A6BTpjZRr#{7cnhMHL|8qqP4x@o~38LZ@}S9aK;q3p_+L5GB2!v8vdUN6?cxww~D88coqNn?K(82~S5Kl~3X)'
        b'9oh78Mk^s1ztc6KY$c>!9c=4Uxb$`yE3Imz2|kaIlE@DuqUi(x!Y?PdO`T~(b&Po55!67>uMxo?mDAA(*yUZVt+agnPJm*)6Rx}t'
        b'{q<fCNA6wYHgwWt8X?&6MZ`12Ut+ohC2MRRGAf-fb<%`z?61!m(TjivN9XLEs3KDm7OKCdJnbVc-A2!`zh=If=~3d9S8X;*U&Yv}'
        b'*vhje6Ll>|2`Lk#K48U3CcU^y%EhjARl%Rq#j_Kx&5@z|Sr^H@--n-(Tfd8piJ_nqY{p#j{b^m(lqO@d8|c@l6pr29Vzjj1ts>P+'
        b'vB<4_(6o8meu&V=f=-iZ?G9OKdb)dl=MEVyOG%&8wHb`s=GyE|bRfazs$6t!q<H(#R(V?#^nLXGBma;0bb@-roycvV0DCKu6ipMG'
        b'X3||dl<p~=yQ+4`YQ)?5X4GK~<nTRoUXaOjqp)!8R(Xex7A9Qt$))t740%n%#+AAsF4QG01iiA^-R+Eazk3p~9N)>CqkMAAlx80P'
        b'aWD_#&Czx0PEOsq6Q?`qamYY5Q-WD$G0V$~F!xUMQI-2#ZRwhaX-BtN!keW{F`cb`oT+2A*TRAyTX@B<*@mt#SNGi%WEAaDZ<7l$'
        b'$@^=dC~uZP35H{@Wh?XMf@wb9Xj*SBw<s(YdJ+!~Lcxgl+b}PaUYmhLSheu-4874Tn8&<jq+f#!i&-j|CG?HVKND@o!$oHL{lFp|'
        b'2m>FJDG<`ZFl#U);Wyn?q{0gIYom&Y!Ys3pGj=>bKBw*H@Ep8DN~^C~M(gHL-PvO;*$+)JM(XYeLkpq$>MJj&uo~_u9@-4Gc-z9)'
        b'Qj|~efZfQQpf)mO_>T_Ie6}Y;XswSb(I)6@MIlC?2iBV2qGP0awvrHL&MPEzj09yer1(qai5Kz#jKga@?_!NRm`&p(Ktm-5!tPdt'
        b'+!Wp8NcjCgsFzbHF#0{wktc>cuwe;Ny<zxu!h0KW3!;zVIAS1_R?Npp=M^PXsa&qu(gbGs39|aYzT)=9X$OKNy3LsT?j#?B6?pFO'
        b'{t@Z-AT!<g)+pYoeuYFFkhNBDvO|K>;#Bd@@fMDqrA1me8Ql5=T|OxRgEwJwi_7&AX$D6nzR1bAcO$K7e&=Ms857_VO$+qTC{T>*'
        b'O_c5auao=FxL((LoN*pbwMa3mYM;#G<lMhUFI%~oL5X{7hq(Aw6>ui$^7kP>A?Tdo_M+VOGlP`-cOBxqu{z+KI4f%(8FW7Eel_xS'
        b'Qa3lDh|{}Y87;B@OI_MN;^QCP6)2;dd$^UG=w2rR`f{>-j^f;p0WK!U#k$K;-Xi%kihXB-TwEtHNV;D{S)KAhMFVwI;$C&XK;#3l'
        b'L`ekDxgQZI@k4jvgO7-#r2A<xMGZ>ojZ@vrJH%abe^V3Emoe_~4)8B*#ON+G@5`7X<uBbBabk3pzyegbWnRabc^#4G$?^a<w($|x'
        b'J@;Q~u!tzliGUX3$L_uQG<WC(&(Bv263aVSkegsKvH>nhSTfc<t3%wM@o>N?3ji8sh#%D&5<70ST;Z5@;MpMHoKw$KK8p@L1+`tK'
        b'QwHM43JqZ}CD;ROV98h&&Twl^Ft}VrjD~vJa!{-d>`8PWj&&+`<)j85D;^1=gThDU5AHy6?>_+*){jiF=|Wi1H|meZ@bP1p6j=l='
        b'9!AQ-sfIL4U6w9cMPfi-!okZJo(K?3jUf^r8-cG)n+g^zigjQ*_*l;~<UEXDG8UV0Vc(ag4?;#W<E}X&UMMzJ@KZcDUSZ6P(F4t9'
        b'#_FIFsKL>~=;rE{0_mwF7@OvTs)8H?RiPHT#cx+&1;)GF`V%VX2NB}FI?3S6p+nqrC-j^S^^B2o`%W$*={P0^d`L~?;4-xQ4NpLh'
        b'lR19n8(P5Q(Wv@kVPviudQL(YY^u=s6c}zS<(T)i@MLM*#xO<)=LHF`9au;+KF59Pq}X&Oz$FKrO81GA5sv8QVgt^EpmSV+V}hL0'
        b'ef*@T7T#90a$~x=IAFgZH_qeK`kX25=941fYrzo`X+(B3+Wj%gb00y!V9t*M6h9)(sqR1Dht_^Z1cs^@1=jFC0NWdBV@%K)OX8^r'
        b'X?~Qm|4h&scOP^Tkez$CSnJy-#ijgQ`<eZO2!0|EAn&K#e-K~45vhTHo7gW~w>ixN1IDK&O!RPUY63J+HRMrlc`w+)Y<V5r_(;SD'
        b'occM}0-Wk-)Nn%>1XgMyA$>PIK3^ILgKskylU&eevk`KE?v->+fo2ArV<1`o-4qR;h>mND(HZf04L$}6uqw0%-Tfb^A&?1$As-`w'
        b'b`vALWbx&wmn$Fi65Yavq4;|eZTd5sig3UG1?o%j$=btT*m6U*aUpP~Ot{?rj}zcDMfR=RWTC}UteC(w6qYT)Ono8K=ONQj$n@us'
        b'DG*w0mKK|%RA!aNOl6xTD75}oSR=)^QTQGSo=xB=%sxvj-x@OYgiN1=O#4F`v)pKo*=CmQF-K>c6-X)U2rtI5VjPuM;VL5@1H7`>'
        b'Oc$HS&@#r9So_FH+p>^J^87l+I)F0VGfvu;hHR90)|U~39MBp#)Sqo;jAl$@#!I$`0a!N9s1tGbkrNmb5(7r!Ui`N3glmjRUORl^'
        b'+-lp-P)&}m-Feu)&usc@X!Dl<MC_0f+6d6<|1%6gY#T!7n%e7vTy%hwL9sRFhqPP6#b}a7S$p;bTOhaX57~BwpymEImaoAdsvUc>'
        b'>Pu!>Xd9X)iq$_W$F_%{X8_9o=5prQP+`6t9Rns2J8&Y5L`!A}qe5GwtjEIcO<!R4kZo0{@X0)P^$9dKVo$A~htI7ZZR&97pBuW^'
        b'JXZS};Bf3{Ll4)Yb`GO<)_b6xG&Bk1SeaFhaJw&rZ43GTu-vvK1nqZUJ;BU}hK_-Tx}c#x)KCC5+Rz+1G$b<ZW39j6P)VrmZP2$Z'
        b'7)g<bpR6lBL7FM||3c*C)PC^_mHX%Yb<f(t(T-XnA)}&5v&8xE7tcE5M^jRB`w22iCOXYJnnD8j^C_w*iX@3hynp{{@iZTxQPQk%'
        b'6A1436(B4R*O~T&hWmgu(2N1g=*TE)bWESbR_!IDa1}{RDh0WoS867{uuThzQ(K9aR7KPZnF^N_Dnlx>Bz}cVgG&o}phT$=m%y|6'
        b'W;?5rqw=_%G|R{+sUErW<21O;h|3s0QLopTf+48goq}4kf2Ad6EO?bUti>_b{B=8tN8Jwr5N!hTH}jdzwU&dfvV5hYR6S!18ATXz'
        b'YR4foS4PS;QPEM)N{msI9!q4IJT{2Bsxo8R7sBcd@{$%pJxlJ38C&_aYbWD#jP(&zAb^>6vOWvti(&lm;9z{vr)LQ-hmkm;!evL%'
        b'B67q6#PG_nS|{CcDE?U#)kEC%7ouZ>+lks;unPc;r4vOE2yRWy3ILj-CcMcQNn%F{1Olrs4kP1zk<?ok7AHU{4IXur0FfdN2~qD1'
        b'7wr0R!Zr5-1XQj2*?Kpuf$_sJRa7*zgvit260s<19V<=?mHb<{K=-p0IYdwnN<&d2E@g=2qm@EQy;ySisc^w_H@xVCN)H!JMv<O&'
        b'97{lhk7n;^k2AXdBOn19kpPQG0Hjak&<&tMz%pPLBNJ7T-moangVh&=)!*Cz+yxrK?#g!mPDTYIwvz>!0H_oL8bAgVLx6x)93|j$'
        b'5tZ7-;ev0jN<WYIOrDsrzWv{#1v2l(f)7rTQ$3Ec9?e|Rf_aLf-A}cHSQW3ro+X^cQ&(lUH@3I@_=P7e58aU~?yZA|;YDHhNIOz4'
        b'4PjQts2v1Ncmdb$nO_8DAFE%#=YFaE%wOTFTsld-p{ii{UHbZjYr{5NJ?mbEync~<xJFS@qOgL!?!?k@_c!gLaUDJUHn9(<6(#i%'
        b'|GEyF=`O5V3(mr`_;0wG&dsZZ*s=7u8Y5d+_)<9+D?B-NXa+iTE=uxX0vBBD9Th+ZrQ-<cWQ;VEhuukZ1ITr`n`;**ljKJ!G8=1<'
        b')SJWVPh?fjp;G104rSHqU2p6(!vp-YKew`q`^)+WSkX#c3lM$pAKv97&G^n*G+~V6zSyziyXUJoI#E%znL`x$<k*6=_<e4)G{Y@H'
        b'^%;I@rwI#*rT#&|lepl=^}HTUb+VL{LZ|FxV@Ih5$#52;mxwC?1SnCNN$Hue_!4cAnGr5HaZ^0DScBuLC=$3C^g~3wL5n;GM-Z1i'
        b'IhMq67{EyHjA8YKkZ(`!cHiQ2$t~B8?^^+g{WMy=<+hKa=!rE==Ak3{%E87)>e_qCu8$f25q95-U=Fq8K>L&DoBm#hu9c;zuj~A^'
        b'=5tL$JM}d+)U}<;t_w`f+pI5#a$h_SWNS-^C?whF4vni}U(~qjF9ONZmb1rq96)i>Xv`P5K;q<fUp$(CM2ja#Rt&$@HXkRWNf1}Q'
        b's03(pjh_OPiUK2oNwM$R)UbN_4^_3*xd2%`^Xu+pqBU6(q$sGPBp6+g_?5Q_@KXD?c3*U~`q{sFI4Ph2#?ix3ySAgd%VmHKWW3~J'
        b'RjbiJ+jnh8%SocKNT!wx7lekae&l;$GjYSN;}$znPA1S)`SB6KPn1pD=(eDde1)7t0gcwLAzqZv+a;kjlgSC!?7u%Q#O>Nt{E*@B'
        b'@s`vt1Wg_cCyLjZUuv(dI!;UIT+=j`9<Qhx+NV4aKoir^$(zj>uG?w&m_usg@hPpzllR}KGW$3($PvdA73iYF_v-xlENCC!7ekiM'
        b'?iPG~$K23vp<*rB8Rq{wUeWt9Eqz7mNfxSiwBx{(k#iEzwa5R5vA2P1>bxGuZ*Fd0NUoXy1|-@gHw2=^4zLxpc9TE>U)n)bMAvQ-'
        b'4N})`N^P;uZpo#ENa?p2TY0J7a?_?Dm6Zf}2jxX0wYaHmZEM?=TBFu(D^;r&f&9+739Z|{pa1{+`Q&r+yq@Pg=Xsv<oO7PH2x`|y'
        b'z_`)5ipqWFxI;;@`pl}=DOz2tMDbCdg~mouMh#?H9Kq<rxvN9`3cX%H(sD+h*(3)~<ym?f6Pt8W(mU-`lZJmgdx6S33XaVFfFm|Z'
        b'_3=%%fU=Dr#}z6UQC&y+&IKG!q1P#L33Il-y0^N5%sh)J`vXJt3r&*RB==$3o>r4|Qr0VdRz}Zhl0wg@5rC$XQ=xRtn!e}vLsg9m'
        b'Yoo?4aOF?W913&@nn)-^FA3PwRI;z=aNHicQNhg}V)P1Y2alACaDN9p<&y2(asJLc!uAn5;_EJ9Vx0n?#F#@kbn{%gyK4to-F$~G'
        b'!Js_wUhS9c#u-`X<yd|15Fib}Xwsz51a?aX%NY?7{%-{Fs%fU!q|Zno1jJyNMy|g`_<tqHRUBt#?kh2q{*Q$~9NwgchSdlvF^MYM'
        b'5kM#r6m76FXm4d!QQ}LXHQBUpj`s>#il{W;cyA&t5rX+LRZM`TWV;RkYet)#hRu-a@0DAACijQS@i92GcYSeOW4-Q(m{C4Ugkx<5'
        b'=@Jro%LUA;8UBb{u6ZJ0E2{N`rkS$*GAy)L;sH{#bi39$WO5QF6Z{0ZU;3Dtr`MY0+LOo4B%QZfq}nGfxa<>(l>A1C-_WL~6%Q1D'
        b'AYdem3$FN5%*D)Ek|Cq>9AZ~o6m*>fO500AK_j<ny~wr+-CV&C6Bq8~-|JwU0W5p-a|a%v%w!HN->?zq46`vuA2msn?sI~IfBEtj'
        b'&oIU%LQ-0;x<1Y?F!;XZ7t5~U?CNq-maoIunftUCeO5-1XB2P;kF#+KFK=GwiiV)e>(dE;X;@{9o4VzSy9@iYb9?1-my>WyZmEt^'
        b'O+xps$@#JeD3@fhIZj2(p`(q6iM;o20&rU=_7X<_a2iZ_j3UcHmfcP0DL^mnxX&1ys5*3wR?{L)>s~ag6GReweAiW0NL!giR+s}A'
        b'*;WoQ={YMpU}!s_-_;7L4rtf{QEgghf&Qt<nzZ>cdu~U;17Ue%H`Vs`nsf6hwAmB;O}0cVxo|l}%PgOT0S$cohNn+2@QpG{TXcNa'
        b'HE5PzYQuuW#Ke2)8%;u>oJBb4P7!#XJI>jU`~N_f;lt5d*5_idL2P$p6KK~TXUL9t7<DHD31>1-hWeT<euxfpWKSP<Eg|>lhM4SW'
        b'^Py|(`N>fK;p6nHeJ+>0*7<tcNQJV|K5AE5**<nCkzGc_cYiov#?LosPYWN@&K#mCqj9?SSH8r=?K#YtHhgF#UAdguAOKl+#R3v0'
        b'-**!US%26NQFWzfBeCe*Ng+r=i8{><W`$&<RQvgH)ZU4C9>EZ?^vbt?IzC^1#u->LT@Ll!?tM4#;of`u2KwX)3121~iM&pV8J=8%'
        b'kGE@Zb`i^&g!lND+=;Xok23?4AmswA%*z4d#p(OEkG|o$vl7o?C9Kx%56RdS1dckc^f+DPT;`H9OViUv?o}?w_hS<m^(7A`0?_J?'
        b'y4R?wx+Z+BacOLC`GBJPuQZXim(e9}Y;-LNqvb4UK+*Dquc~V(TFNd5bmWcR<$}!bgLylI2_JNM9dd$RzIN7c6I#_TtgRI}<O23x'
        b'l9u(#PRjl%qhFza@`OzF4t3_8Qy<=U-#@xf?bqy|rT*8YR!Q3v)RN_8(}+Di$B!?%KC)kV;+@f9<+<U}x3P<<?Jz$6(bOatj|Uv@'
        b'ocT;#^?B)NcVcs|BJcLZ@N#+{+B!7$zIP}PM1-^~^LAkNPVpGeH}ZvM=frx`RS}_f7ys>p(Z6Xnmx~5O0@pEM_@BvNls_teO-@(S'
        b'cc~ts%)_TPr`)rlLsO|X9TTigiK?6?uN~=7R=fa|-D2;ZJ|H91jlS!F-f4OB1L|7-9`%9YGqkwxx1}SWC7wE~$ZMJyzJI<P+A8<G'
        b'V}$fv@L`Xq71Q4g(-wx^le^=1@EXH}57zz}7rQm{`h*#ToS7>`7Lfag<9F8v6X5X}LiO0h1EWvxmgfE<lr8gHlo|1+DMHOSiKi8D'
        b'ytRR_T%9irZW1D5w09q8odj<iLL(pJ6cC0%-maUr`8Z?^YHbXE+6<@Q?)kwt2aG2K@{CGq7}#=NsX$*PaL&`Hypy(uV>zuF`>iGO'
        b'@NCG9fd8k09KA->Na+6@Mu%(Wh2*)i>j8e9B<+=B?<OafYI3NtoY=7lkeX52Ar*q<j-l~#M<N>2=z9RuUKw}Hhr5ghj`5oq(7Fb4'
        b'CObH;!JF}j6i3)n?bw{r7sGu23_KvsycO(cT<URJP7m8&JI3EH1RR47TO?f+y~waAby4=B{N6C*+n>{SeHON)W%g4pk|>yeoc_g@'
        b'odXhLbXc)}<;XM2x@wT*9PgZ}t5Y+1T@zxOAg-S9E&Zcn>(=d0&|81I_gS$@MHQcTFXZXTEIx5C<UUyD{OjI>OAOhm`I-e91K!+f'
        b'FyJQ|KT`P2mtKqz@S<$o-CJ+mPxt&XPW`aD`?YDlF9Ss33cL~d#tKr*5QV?ITzulqlhd~Twe(r~<TU4BOZ!SRs+5W91*dAIzN>+O'
        b'hKEl)GvKt9Ea?MW^6GCFH@v*Fwl-h<j{x{5rft1lI=XecyjCR{quZ-fUaie8^Fz$RJjwT}k8kbBE*SNlI=<?J?<!54oK_emAIg7X'
        b'T3=se-{#Vj;uC+X?je022WnHxJ__UozN>CUd8O7M{vbf)&G@dmg)BQ0sEy7%9onb(cOQ*{fqfQy8p6tBrdP~W+pX4n8Bz)%yJt<U'
        b'U4HO?OgH?0OgG@8g8}#n+tcg2!_#?(XDWR=q;CrA2#bF;yklAACm`=u?8arQ3PwuJ8CBaI??e`+eom9XNBHz_{g6JnW7)w^Mhwad'
        b'7SdbiSzU~9L=Fn0P<!?$J&OsigL#jZYIg6nPIdSn;2oh!U^u*tQtL~r_SFcPNFp_C*Evn8Qj_?;b%Dk{%eg>dwNc2Q7ibdfR#uTv'
        b'QC~A{*A)oItx-A+)WEQ;VG)WDk%We!U|a!L#{SOw=&%=M$@7T#y{nSvQL6W-k-5q$#>%hMCjH*$h#=sb@>SfyWV^6D{3ovZzWOj('
        b'e~Hf}mC|ze&u7@$j{^5LfM`1x)ls{U7HSNAbhIY56lHjIt?NW&;iA{*(D`qyN1^YGQ|gK!PIW2r)Y1Vb*>^(Wa0>cf-Mj1kpeD4m'
        b'QBl>X(LU;Pts)voRz@wgD^PG-PNh{G%}WrSvMW-GQrXD5wMA+Dt9>q+lwRRqID?Hq>pmWVsl$6FFvlt)mF%0RbP1`)Z&`!Z{&b3g'
        b'jAkiUe$@6q$3pAPL{`z|ej`G%B+pQtm;g|Yw?7Aok%#d3Ek;N|8!_pWcogZDyU<s#`Dla4p{g^+2sPI2Fw-twrl7;~q%)QpO4H{1'
        b'fbeW2;eGq|2!H1Vo+MsPsJ@)W$f$Vpa)u(<w=W^Y3_`p4sEgq>2My(lBtS_E;<*~cW~cLd{5hG^MKMm2j&>SKoh~IbA=~hC$m?`r'
        b'B7?{qN%TkfT%@$QEyEHwqo>gUDeC*IyA?F)atf@j(&h?0PvWe_lRE5bXls#Gb6umS?4rlNH%ak`VHJNIkjbVP6;GR`M{QY18z^k;'
        b'dC4w6Ue>-EeTjEmah9w}UJcZvrAygTt7bbs)MtpH8#H#sd|_dYr0NxlHdg6Mfeso?hNI!<PAF%J6fpX6jC^^FokgS+MFFpe)>=no'
        b'U6wLVMbM4yqSXL#@bzh%?I^>{1|0@EvF{e<{fq>n&ljr-72m#pj3zr~wB1i;{)|{^jdTo6&{0+Kr7)B@#nHIbCmiQUc9wM8M@P3p'
        b'gRYZ~ysP};=&`O!9K8SIkW$InQvUJWq$9_6eV80UY^_y*qJe@;t!7sXuAA55B_2zSc&;r&si{>gt<`)ib!1cPQXk8Xo1-n9k56SX'
        b'(Ly>x41(|{--ilZ4Fzg^=b__6T=0l<zL1&6&gPw4SZ)2Wq}PuzTQaq89-||fEi1I{W3-6bvRwNHgl1_mF54i~tj0$fhm%jmmR7P|'
        b'!z07W6Mr4pNT|CzXTU^Tc(*92?pX4cWk@e5C;1J+cVTL*RRCpZ%IuWd(+}1(EZAT|W!Ba)=!g)q(RH*Ob)s3;&b{+R^=g?xh&yuT'
        b'a?lgh8Oei@h4&7Hcwf?C(C}7NW*0J|;DB-Iu*ce-J!Y*?SgqId8YUe&cI`74=vlzUoE!z+AwK3TqeJaC6NC-iXY}N;w7S7}lXFC4'
        b'xvvjK2#Fm17(ab$T(NOWJt%0{&JN;g4ouYoLJ>ap!(L37wv9(eQXCY&hWvn3{7tBSE@oC`qpj;GF1I)d);!C_#DJdWHr{lZW2SJ='
        b'J7!przsks{vu36Xsp&du20_RosA(Vxgm!o;#+X=jL<Vhk67jF-7#$h^ifF@|8cU|kuquB6%gla=q{HZ#@>jAd!<Ma@Gdf>nV$^os'
        b'+8U}!tk00?$Z0~7#%*MZ7$G@*0Xc(E$b=M~C|Dlc21}4*LL>bUi7y!pWM1Ll$)R;p8e@s*2tJEKDGQ}1#KLU)At^m8LP`sz)8<R@'
        b'<bU>iMBRI=VYc}1*!OMPV+QF|{q8zuh!`KxrVl2RnZo7kga)B;Kyc~};G%sajqtU?*R~ufdmut}LTq#r#x1ksXUaXwW1RAsZ6#7K'
        b'JAx+TBOkU+Kh{fH8#Dt>gY6N_p;aGcV`t|Z4W@OCbG!1S5`)lt^zl;;7zBMIwaR(5@ELG!H@zMGnY7#+XNZ`)V6JZNDj2GB)9LUz'
        b'qw#I8u+Hy|&Q0;D0{V@mOy68#=7)i%uuAFrgN<(-kUufa>gsbozIV$T2h?i&z%b}5+i|U4e?DN)ArxJM&afc9?q6k>vEJG*k2Wy&'
        b'<nkDWek4%CG?>`Av+HXGyG^^9;2xAujv7)!bg_MO)L^iu#@CP_%Z9?V?;W)>HOW9nEjd^|OJEoZ?k};Ogn1ZJXIq&*oQO;319hR#'
        b'vf;Fl3{M(5y7{t*C0CXd#js2?@Kn~Igzh@RpPWLoc6t~Hy^e5N@>o2hlM~_Rw67lxUeJo~Ug(YnpIXG-x8xY#hY7;|x{g#bK$z&5'
        b'tgoVi_D1L@+Lw<K(dSU1<MZ<2y$}v!D&Uj!`cdee_66nPKTG@bQILW`r9uJyyTFuy4#^kdlP;t}Xq*;=sxwXlO0qg3jHLLQVeKnN'
        b'BaBi2le&P84!&}UkI~K<RS4$sZ>%m92y%BH9dJILeIG4vqHN~|prW%YSG2f}uC&#oC;!RW^tw%^2t_YxS}o7t>pH4gx7{RUOc^ut'
        b'TTGi`@?SS?nq}LMNzIXTZqs1YMKZVKXpv~g%*Sj+`uzKz*|W}*TRrd?_nC-3PK)W4I~{0FoE9q|CIs^a3L?)GM4<K%KA-JR+*!l+'
        b'YYv3%tf>jxd8n$cZ$KM)MjN48#8iE;;VXGV1`&3`J3n@$@yP=jkjGIF9?WkW#PZpG#m)}MaX|h>{!u!{p$#WyFC`i|r*pe^IstIb'
        b'hRt!ls&PC_I14prPL32GAJ3z2ZhPoxv4kkjh%Am(sgBD#)(R!m$P3B}uA!p;v4Q4pXnjRj4<S3z@h-pfT4`$-;0@pkTmcJ@vHfO1'
        b'C=uou#uUN3dI|{Jg~0|1ZZ^d`dn549-dBS;BBq*+6z3DJO;M~?sS_wFm<W>4t{c!O`Llk(d-_e#e-R3E2b7Bcgi@AG9EggbqJ$Fu'
        b'z)coelR-=7OG;|VvNA%uc;K1W9n8vSTFRgK#g0u0F(nn*#b*RA$(+rypYOWqEJ@t3S)tlD!*>6`h7H?``xQCTvAli!D)YkmpoB|o'
        b'zs2%EyZY@Q)Dc;V5L$R^p~k$L#+z>R0at<Iz;$#w0|hq*4_wF*j{zJylSmx1=?5ZsssP)U7lL}}((8G~AF&`U+_rXLiuXqZdH(`I'
        b'c#!==o8Z}pi?>aYv@k;{vFu9vVo;b7UbG-tN2aLAD9azUGX`L2%{?m2P-G?%yS{hUCRV+wDBB(2qyx|eYUMj?4uoZv2ZR|>{M{?U'
        b'ECGMCO;RX|kPx6hZYW4wQIdHyP%v-MES9QN*Q&oKeJ271!-JqU^5#2K8#8^FS4gb&lbL@HL;!^a^Tc@GD)*cIf+K@4wb6t0gHYh&'
        b'9ROA*mMq?;AlE}9ntkKRgX0ldgnUh&e<G=UF!;jt(}YYr(hr!6Q5j0|4o*EG{N#cRMRFt!(|i1To0h(z(YFV*^@GsJLQ)#qTXPSA'
        b'<D60mGp5FQ#x%$RV>{(bjY%siN?T{j-<EoMU2%T@W5#u4Q9=F}i^5aCeawv4H|16h8XlZ`AF|j7-7f}^R}=h_T!cF;&?N9b7fAYU'
        b'0Q;40j38r@7%ZE=lWJZ>S~&KHne&CDAVLtX{dxe10PO}m4k`)>ph<CS!I%9we;nw?Qyo)td1iG0D(ibCfV}2ZX#XcW;Bq!J+V}i!'
        b'utC}peITp>xOV5P19NvT;(7X>!a?qdLBk^Z-16iZz@IgY*2%JlFmTQp1ziLE3@c}Rw}bFpPQrg8%$7gsFp!QSkv+A17U}+DfQR)1'
        b'_eLpb)gZt7B8*?(n<mT-^B)MP<`Mqekd`wI(g%A<TM>3jP{0t+tik+-_*bMg9du+$E$~a4Vv1zRMRLoVfyx-mtw7RC{q`?a`IGT8'
        b'DO!d$^EW0K-E=?)WT3KZybhO^HBggLwOga|g1j<hWj8WTna2L)r%$G?uC9q=B4_aDl*`WxJ61PjxNiX>Fhgh-Y@|(^1y5GjP=?hh'
        b';UBG(?ao-V+V*Q6wW~Z_TD}Cgb^i`YZreGqYmAkC%^Def!wvg-Zr;Fdvwi2|x2<+jUyYItpB~bUOw%2*PFhXNs@^K~HU(ajLHO22'
        b'CGI7DE3ly!FF*<=3(k>A5A?fq_kq-B?a~#>N#A_J@$L<JHa$%%9jyAa^i<V$JDJx>oO$=!sr{u@A8S-!2`gB%kV;&nr1C^Uc6pt_'
        b't4rc02HY9flX3@WsVn_TlCgg`nW|%r5_~(J%zKierQ!&JpzF$R1RU?$0Pt(mhMzt2?kxbS3KOU<Psr`NNg6;WXG?rn1H-rC-hEe{'
        b'x`?b`UD=Ydf8o7KuF3M2uN|Z$A)Ss+sckxil_qyRnHZ`M8LH2x1FVoxr4ndQv2jScye*XN@BP8k6D5}~0!4p=!K^D#pZbw4cEBOM'
        b'uz!)gVfdEkuLJZFG-p;}ysGPVFWDrty^kI`ybLs5+l#@B+VYBnXeY(~Gt}>ZB5DP!RFIb{@IMt$og-|Q`?%qL)}Wy8<^^k<;}7@q'
        b'D=gtE@~*UzKCWPZi4CW5<>*nF>fCHTPMILyz$jqijCxV5Dc{ScQ=7vhT|&Z=G0`N^3#Cl#oF*~kctVo1b$gS<qLo)>GO<rUNRD+o'
        b'Glbh^+n5>5&<z+3beN{Dv`Vx6pcx;*6+vNK#y~GF+Z0ygI`3?i_M^Vd)nsNCVMwN9AjC2BO)tp~{iCX@)H<(JbGHVv<(bBVn5nMn'
        b'(!70Kbw2>|@_m24Ox49Ch-hifdIcTTB+aSc3raY?832PdR=pedG}{F$MG&1+UdpBuv}@Q85%Wb5QND#Tr4zHm^Tf-sehVi6WBqp$'
        b'Q|ufN&__f>o;N#KF^1nD&o2OH&PKS9dGi*z_CTM@Ni&QPH-tVqK#R>rY8(G=Cd?qR#4a>vA(91K0AXc<oF`j?Bv=<ZdMi*l4CFz;'
        b'syaL_2vwUiz=RV{M)9dJ8Hn|Le=jad&KWf%&z6<>p#ugpOU&T_kyi5%J>T`aVv{YULQB&%{ks8L=DvDed@(@K;xbPl>pYpc0CSlm'
        b'DE95ot%V9UVg`CwQN`&3Q@YHQt|@q~|5A~NRmHNaW&j~*DVur8qMtBB-Nl&I6+t;0sNpN-*hQ85AgFS=IW{F2g;4Q19z_tOSy-zo'
        b'jI<PmxzdF$VXZqLqhl;3H!SxD{6%5@Hv^uue(u43{l8@HO*d$nrRawK<fQH6K3rRgk(-4zX5V)p8?-H)4b)gEM!Uu9l+#k$B=$cj'
        b'&3(9U_Lltnpj{+pxu*l`jC*;X6dpHAU9m~Hw6>A_(2Q$rZavv<CiPo{m&~Ml^>^Iuey2+T?AQG}DXuh)TxWzD$@z!;y_2e)6r-bz'
        b'I+4lw^4dClWwXAO^d%Bz=bp{ry^pAGBgF>rR-tz>LGO!SNM<gEfT0b{Mt|pI-p+AcIri5FOhOH9)T~kD=_CAIlMl&Mjp44h1MW39'
        b'iq;o9Up1%<$t5q7nU4}#?YL~kI%~_p`zvtNfkXUL!lvqD4Kb>G5Q~xd-c9&dg{iK5?Q&Z6o22?@!ayDT;JVusmKPJ~m6@S)e9#AN'
        b';AAwJAat0Wj?FPiX6N3`F{JoxK+X8x515_%Hpdt?FP>+1R&S1hZ_S3rK042tSz2~7@D`IfjJAV;8<{5paz^}4U`ed+cmT91kV9s_'
        b'j2lm2ddNH$pk26ok9EEVSOQ_n50T<~!2752NHn$5kxSPkW)j3(jL{hue=pX|=p0(gY;-pQ3G%u|fq9ADyCnNRu>G2E=B}B$#w-~('
        b'7#Xypj1kVxOP0b2N}mla5@kk~;65<<qD*x{miu{MTKf@3lu+z+8s8_)&ghaFyq>_}<f@}daSCB;KEi%PveKBSqII@x1fI8(qGxGr'
        b'o2u-IRx8>pcYR!ix1nl$)3BmtX9I+q5q|*H_2D^psGs<Ks9)y$0lfO4?C$|OV<{y51mbM>BEZcRe{nkjoxFLsOriwM((P*_Bb&(G'
        b'0{@a5+QuVxf#G~*a+4H~${8>@;~bBdk?voG8DS8S@h?OD1XFwi7aFDk9jO>eQKM}(CLcbr>z0N`b=OyDzqUmM%e*W;AK0_^h+}Sy'
        b'>ie7gdb{tlfXdNsid|UjR6_rU$-)1QEVtqaR0<eS{(YMIy%4MtxBA|n<mD6#7f4F)J6K^OdAx+=L$dK?)oOy_1o2dac1IsW5|u7('
        b'8T?<!V+eoccmF%eb4J+{R+@A;1y;viN4lu+N{mg{zbCdIt$9TRvy5Q!h1!RYFw8>afh&%%LQ<9gJ<NT1w{EdQk;*{m*#HjBI;rjR'
        b'BiI4XMFx#-DOcnyqwv`KI340>n|FjYtV}5){cf@4l|XP$J&_jPm$dMRi>fK?nnsgMMvbLQhFg{h!lmPx@D)5HOgHK~W!lUm^obxZ'
        b'W~jRT1HgD{Bs6K#&EYoyc<e`*j5<!*$LJJ@>ear2YkjnY7MYCHGh}flQEU<hMUX-nK0Qzj{Vj&{{Sq8Rv6%=a*tWP2lAE%w*bee_'
        b'IWb(UQ*hUgc%9Y}36c3tAc$4@mPnUV>3>_M)gEy<6@ZlQWB!8DZx5To>(*Lk1(RLcqM*-Nnq=DOBeT~Vl6@$%THYFWZqcab3Gn{g'
        b'w`5u+0GI}G@8DTg=HYFx^=)0FD0yY6OUEzj3v6{rJQLNiR+hj3nOw>s?D{QI7<X4CnLW5HPwVSt+R4K%rv!09-2}4K9h_-mR<5-~'
        b';H)<)(cXY~66608m?E#_%6Z#1tf|Rq%V|_pj+v+$+8h7MFy9t<Al&>OY59l5tdg3X(zRlp`Ha9UUM;y86U+~JQnpOz-a2B^DZI|5'
        b'&<y&s0T)%9x8+N3_-W=10&iixeSv$q&-Mz|!&em`X4jY0MQ?lWaB+OP>i9+5-;cO-Mz8b=(zhDM&xso#Rfbt#Ev>R{-$4%VaGbbS'
        b'^+KsCS~Yx=CB>Bu_0iH|qqwXR>*z9y^?wU|8iR9YBt=JPbQJV#-Xy<++*xeOl7Q^C?bs1Xk%aDGv#$6AcmQlX9~zjABveH+ip4};'
        b'NrL||?7{96f#K!F6p?pxY}+3Xn=%B&@hej<k>cWjd#AW;D?ShHj0Hg(#n4~&>GxlA0Tk!_^12rKg#IO&?N5j4ovZ=ZF~pZ4@gtqp'
        b'H7Z-}Vb*YW<wx8vu=bE4_=KJ<5^2tIT5F?1wVXm}Grznxg(aoq(Yw=Z(=gV-30N&vEz`Or7hre-_O`OaRs0z~){y4Px}a*fhGm@u'
        b'IiN;76ksJ+=vmeSr4XN2L9jy~fm^lnTP~?j|1zSg>KZi}#hLwB{+=ffyChd?=I%}d-eXT=jnr<uqpGliEW4jbkk0;o>+Zev29PTP'
        b'2{q+)q&ShNH{1_0c+7?bdwI;`4%Z~>6qGC?bDq~&t0<I@zn)SHNY*u3(m|HR2Gr%dp$%MFk}_@Jk&g11Sl0PR1g0aFbd=Y1L9VFF'
        b'hgg!@wP<Q@O=b*1<VnULhTa_nR(2r}^wlWxp1DP@pl9O+W&2C}Y8AUaLt9KOcWSEOyx-h#=-8?~qP}+$cRh1z7?%tBhBN~v5-&Xg'
        b'F!4oX*{J}QxDMB5j1<z2P?aB+mpl{fEybh+hQDfaF94#W0Mypn#9lICKmE{or}R{<vRE!T9`$(1k|>}>)NG(d)ZOZC2+Yfx%)E@('
        b'E<w$rHb7;oFWKHZ^84SHSASj{PL7mlicO^NI#y+5ha#_j{M0Q49Wz?L*Xg8oeK^{v+-g@igLU|3Y*)$FsTyHFg8Uzr*A@fP`PLFe'
        b'v61qf4?q}gC<kd5LQ}TxP|(@d5>4i<0AN);9lB?e*iwAWlu3w}!JM=6F!YjQPFo_IvF%2$%NbT2PvTg+86fy{;_pyD#s0r2V5tk>'
        b'%K8<;|Mp~_EMWT$=8dbk6tZ)=k0d7EJG_A3@FCe4RwH$U5e_54AIn`~_uUHF)f27P_q=-K=9kmBzTTDTD_6SCk@Snh`S{8$W-N;E'
        b'h7ob^PCNc;xHm@np`1!a5b9d1EzS2`z-uI?ba7jAFCE5J9C75^`D2lM*jv3^8B8QeQ%i3UW(RfR@(qJb>*!^eBF$V8NYewFcq%h='
        b'Ml|hDy}3J&u(3%^xc-3uWbi+@JFjx15rS~5Q|L@H9ui9~ApE0&gaNNWz$_=!jr!4mS3vSk%QxT@@=o`^__HjCSK*O3<J~t*QMSj9'
        b'#4(Jm;K+^S*|uLFi3?ZR9yubW2-}7uajcBC$ESutKw<G^G!ol>c_hyJ-R$pe>yK22|I>Fpw6BN6JrC~Qi4g3h#Yb|&dHacA9z^JS'
        b'_=wP+wavXvBvgf8!w5@Bm4cgFhWvxCl%;cGs$P)xkzP}5l1doGWgG!c?IMZf*d(G+r*EIYL(M-wV&dr_!n3j9<nB45vO_8olK2lz'
        b'K=@R=JsDgL26qbva>++b&RwSEgozBZB^;@=B)DO!H!T<BC!1!9Q!J84?lWZrKMMMzERvNE-r>&z|FJ2*1N@K4O?pM;nw2vlP;KYa'
        b'Yz7#jJMyfBJg?m0F9E;*4u3hM*Wclf2fyV9zg`K@*YMC0?`#6M;AIP-Mo1GT<j7AJiX^#Vy*V?3mbRZx)jdC%RySCHaQ=Fv8h8CL'
        b'xWQpahX00QuTx-o6C)TP;J*&@+ZX4I0;z$BZYNK#uR=K*!h`?Z#lw&oH>p4yX-pdJ-w)#|i;=*in@+<2X;}Tef;ppkhlHw9p)LF{'
        b'E0rC*B@_|#{lRl_mOoGQ%9=>q(O$gF;ar%!vHp<E^Vh==)Q3UpjLd%p@ZPkF=jr<!q?y-nygy17_<FQQ5998!P(kLi0{z)wS^uE+'
        b'e`&kf3ni(dMYg)bP+IVPMS4ZBOtFY)yElau&&kS90?5|qtu6!Mbqd}4g1B&4u;p|Jm$wj?*Fv~l4B;XKk?^_0^ok&0@s(iTM}_ZX'
        b'n6|OU_E9g419{`fJSCd5S5_|PEp7jVFD<3R3B!B**nl!YSk}KZ;q20IRflbCFMlpDIBp(4jC+dEC_2yU#G@eYN<LlLVcQN&2fS`-'
        b'9MzcZj3b?>G3}0UY!o*nJ4niES9(u;1Dx35#C<VD9ZV>i4&&}8E8lwIbz2c%kZ{hZH(iR12JM47!mA@4LxN_zvQ}8p-9%c(0wJDa'
        b'_tLXyx%Jh(jx?f)Y>$rchDSS`JF2=Bs&@&`=EElimWM=)0EQ~c328*;c!1w$&;9c7nSRCj{zN)^QSM1{S;4w(kJ+Bt^Re<P!EWt*'
        b'+3c4R(&fX2G_=`@j@PEOzbz^MDVf-!d2M=Et>c|>d)PxVhm>fd92wBv)fstVffwcc_AS1zX|^Y=?E&%`b;<sxCr)P^_B?plc|zlI'
        b'3N5z+z&BE_(Q=n_6K|h@IzS_~^&omD1hxlz_@kfuuk?~OJ(9wce7K47KcaqCMyqJiaC;MF+t@qBq&<m;n<Tcgm`8O^q+Q&@%{}a3'
        b'l5h(;lf=zC9CQFXb`%i$-%ivBLNPz#V<d!XH+r|$Yrv}-6tEC=7fwx0;$kLA|C<Sz&p7pA1|X7zX9kG5gk?4ElN&8mI(G*3J$|03'
        b'5jGe)=GqSRggObq@5OcBq@Iv93Eh+T&>}iA@xi?Zl+M@tmM-0XKs#4ZtfGnvcdp6H3luWH(#m@{GE|QKIyGNLuV@n4%CMeK$W&dj'
        b'*JJ<zWKOC)#b_|+F@e*!dV59m$|kYxdrUO4Mw#?o?|ku=HSw=(fj~6|(!wRCr8+#1UYLA9d##(h0@GMh8H|(Ba*zzHBX*^W5e6L<'
        b'6;0CJxwUETs(?MWChgO)%2gfF4a)jgqpS_M(bZ8v=|AS9DwppLQ?FT3t1ij>B;aBQMZX66g+5;7T)uY&llggo7Ma7T&G$)oJjH(x'
        b'j6Sc-;md%p8MG`YtguO}uLyj)zH*gawL@7_GtJ}cJt^4mrpC=681<U6e+7VkefWyJ)$IIribG73WsyKtFGCJEXEh0Ihp~o_l1+lw'
        b'1he<EGGe@_SI|VU%Lx4uIWwS8HI8fBy1AC#WQJ#n`rtqJc5jf#9W&_|zn@=Vh#OLPhyL8$yuE!1xdE@GAk?+$#>^1kNOE^`Z}b{<'
        b'NziSLq_lE7I9&r$yeN+(!0pe*i7?IHYXb3z0yf+b4lc_tuj6!PuDr$Sl9s-K(m;bb2!sJC{|~((xx+>%JQ_T2-W$+=ADH49N%n5;'
        b'g;1FdCiu@=4-*Kf&%2IAJ^n*cE=CMa_fmce4VD9QY`6m4+>YM*%Ore*QG9Zikzh<QAM?<iG1)GRc%rxReY`(`B7&PE_4o7B%Bo&K'
        b'IW*sd@Y~SM72b&-qLtbE0}4UB^eO)vUU|L8FH7P3A>feHduIZBF~&d4$3M)+XWxmVoyRewcYkyPyC=K1TDCBF*8_dG|6VMphP4@c'
        b'%XdfoNbq97%#wXQM00I#s1Cf47ObH^VWMm_)XsNza|`~nPRjovwSO*8k$D*W14^1+)#cE=6G5o%cud9eIf1D$66_{FM?5&<zi0^~'
        b'sPT16?8IqRuSeB;QU*Ly|7L){PT(c#0ond8t*DzD?E%h&k{FZ3AFqOdU^nI$$bvk`v0rM7>^@1^^QZ2rfViaZx;Vj9tw_XU4t7^='
        b'q9=%l_y*3|Y5(X_eMv%p_Nyn7&i3GNHU+qI=y2x-8p4NTxNm!Cxj!eso$djVg73T_V{rfMfiV>n_bk!8toKz98ym!N>K`N@)p{bB'
        b'3uTuhJ(*McWYYc`D%TP@k<`H#w>-f0@CYmqmir!*YgrcHTK=uv(?6E$SMcS&`~O=m_hY%Nkf=#!hm=iZdF>2)gt`Xi)feow5fv@|'
        b'=K>*_7Ur;I=VXclw`nB3(dE+pbVNp|P6(2r#l1cI$tF@CHgWoYdOXcNCuQ_ve?@?w&4Tr+=`zPI?pe6xHZI0Qb|a^f9b8@?F4uJR'
        b'H8)?!&LT#n)UW%gi6DMzcaSCU;x!3v#P8QEAYLSyi0Egjc(Y{3;MOPa-MW1s*V<LEwI?n*TGeqEp6Tf(3RB6l_X$Ry#2fYJjDm}M'
        b'sRx`c9fmsJuv#X^@w)pLdcX?~Rwqaph_9KU&FVpsiD@8NJ@zk`j@;U=@m~uxq+4FT2c($7d8GIO;>O}Rs(Dmg%*q`LXfi%(O)<d#'
        b'V-L)Y4GX}TDJSBVN8VUYmZcJObxGaFSp3sHc%v=4e%HhIci#4f86U@tcoL4=(gS{kvZ@!CLU(Lb-IVQkQdKX*WJNsujlmS$f~llW'
        b'2LFpAq9vQBVY=L&;c)ms7^7dTa(vSuY<$B#1T&~=z03$Lc0J6<(}g0o<@NMRK-AbAlrU5>2~--FYovtcP#>#b+(bg#fbZ^DyiE~t'
        b'Pwxp{Z{^a77?8i83W(1JF#KnHo#dI{2k>4h_MW_RH;Q#)l|+CT-G3+MP@kypFmz#0=HCKFlBm2eg%AE?LnlLBz9h?D3aHNGBa|wZ'
        b'FFFB>K!+L~VtWuFL(gtJa?>CLPvaZ<FR)d$bdQ4v1rkj}v|Ui;pc*2o%J+KpNfnLW0>b_G@eToQ?A0d)xl~O=!ccjw0$M)pcy~pH'
        b'E0zeheuJ)8qJKXyg;&D@7(d{-1J#CfaJh@`v3xv!XXvWR<^P^8d!y<C(InJwyJvU{gf(ouBhICh{5RY|a5<fn|Gj^MJBXc^qugis'
        b'&U>XByyBh!flX{VJ+6JL8~TkT0LXK--9OgLwx@gKWo4Zm6bGOS9%|%!wZ#W4tvl3>7W9()EBwL$-&@=iFq%#P<|hNb`N$)<wr(Gu'
        b'4++uPeS)X+yWOllsN&Z|u+D_?TBWT7i>k6)e<%xS=syxD<`ZH;kVVxv4J{>8LFst9`B(Q8F2}p%+ScRRP+<&Nwv13UDsj9mCkhvn'
        b'zU4n=Sfy%=2zC2l6H0Jk!>HERQ4ir@$(u)TySt}`MI?5&7rRx@5k`to#lon^C}S`y(qH^v^#6}GnMz0pTgBZqerNbpv*<g=%kl$6'
        b'O}hM<ws^YuopD;d^{rCp*6o#>IkvlO0O-frx>a*W;}+pn%-kQl%kX-{xSi{7R4C)tGjUt+QUgTxneI$65m&JixJL|`**_H~;Q7Ti'
        b'#2%U*-CMhXE286f-99{ngU%<q#W(q|$Gd&kdB<<M@dhh&ZRr+|26m*!WszmgeAMRdvZmmCUlVB$FRvA`v1Cfk47+#u77T;LL5;?%'
        b'aW@3_orI>*yycUbw|~sjOP&-?<)a!XzdP{b9NZA@uclOWRNh`HDXNous5><AhNB?zCK54C+x>%_NTNXT#&}Rv2#G9AFb8*|D>y#`'
        b'<m_<O_CT7jvq>1V#xyV??f#oCm^Q>WLib~&l5ILN^I>9TB`wEmGQvCYDDsUCZhi<07fIp#{~C|RCtW{?UHN3;OgYLivEAVF(S(Vl'
        b'Olcr?JyZF-N7H>$K+7P!NC`<)XTuw8PYA$Ei|oqsR$L#B)01K&q+XzUP!2`-4H96zb+UhxhTZ$Hmbpi|%sMociHRa|gLP(sth=Jn'
        b'C5GBBz#Vx%Mm?u55dCjaxkNWO?V_5QY(cnPpMM`)5NRh(1v9PeOwcME1rb&ojKpwAY9a+|EmEx2^{zW*OarM|MrlX8mNUHcz91wU'
        b')^&wsvSJ=>7)WA;s+<6y%csEMCYFL*Uonnz(f@RT8+1Snj}wC1z5g1x%|4B|D`4gUhza!?Uq^u8PIrkLL-OU`4(@E%f64Uznrqk|'
        b'C0#!d%#7+o>G=O5I+u2#;9lCri}F}GYiT6c*A-`&&K>T$kt*f7yW*lrZY?HgU?JY=&hU3nVsZx$ptWnCf#818_1`+d6Flhbt|>7b'
        b'Avf}n>v_m-9`aHia&Zu{zHRacq5aQYHz9j!*MF%L>$+efxKpR_KZP~pe%AG$a<FYt$DWtESi?%Il^TxT^I{k0=&F_Nsq6wzWf%8S'
        b'mtzaD=Y_631F@%~%l2Ydtu$!2O?#lj6^pXj!5FkqmUp3HS$E%!1**6RT{16A!B}Csf`bN+C@s(yru$Kfw05D4g0A0pL7eYe0Nu}Y'
        b'0gpk)jxJy5oFB+~<6|$%dZk=qSET_o{b<Xr!0;JcY6ojrsLBV0pzDWw0KHDEujNLdDp)VClSKb_Kl=Ij2PoEgU*(uBzN15C&p#<_'
        b'_ToAYEuAk7*>ynvoGY+g6Fwv}ISF$lWsDVXSYyq*H=w^NbZ*h`_JKci@{(oVmN1$$s;De4>03w?73STT6l(}#lvQeiN`9PB^P`fl'
        b'wKyj2+E2S`1jCOt*j*>aZ_HC*u>KPW2IXF&&R9{RW>^(fp4@E^>}L#xmFFE!D=kLz!@_%m=7*0udntM);P5fxFp{AxxTkBrXnjWf'
        b'%UKY3yCX=CXJzv#{$}XWGUbLTgTsapF0Sb4>WWA#x>jj<4+^hQ{!o0O_yXD%fFW;a(^$0B3dV;^U!z8)Cc_G)!53-;4v(Viq;Pqo'
        b'{wI{02|gtNwDU~w0v2d_SE_Am=jg7W>Te5lf`dhCqM!*+6+_sb-5sD(;Y&BOC@#<$^%coYVtu%Mok9I7*rwVy+PT}EAu#{!<i78;'
        b'O94tUuajZ->Y9ptsskJ@X^tgp9K)ac5eyH<(awE6mGqNNj_L$-z#BZ}j2U*^QLc?hDr@IPI)PVcG^jl`@d{iTGVopj8YhRtVCLwN'
        b'apj%-Zd+t!!Zb=>FB1x=UbLp_)5ra}D7zq&E9m@Tz;VNvgYVvaIght<zD|IJ>XR-cB?b)>ZjCHh#&7?v48QY-GW<)%-7BWb$iAbD'
        b'mOIMe2<^@ehRjj1q&BymYYGtozPQ3ad5y*kmE5mPA`MbPG{}9UlNJINC}Mvo%)3HpA8Ds|8ki703GL6?n?yzi8EV|#S@fZ-hzxok'
        b'__^xN%@H%2gzjtC)QuoSV9?8*IIHG#29p=;LWemHy8=E+Ato?(Rw!1zpz!r_zzoSMBnq~5as?gPVhEts5Q`X2NA&4PaOS48r&_WW'
        b'kiG|rq_B2l#A(SU(*J2d|3$$4VIb|>b`$lS>VxSy8#d$=DmL6$x?#fxlkX?R0Q<>Kv+w744~c}>vZ*1i*`g$5C$?<t@ZlcS#qD?}'
        b'k*O0B+Qm<x5dr6&Z#%$`4ohdyQS2nPW@)l!F0Cv<o95*Xly&16TY4wJ`bav!By|j`s{vpw_s*V=ZMIkh`;l#=M7eX@fvk~f#L%7*'
        b'nyBHP4TCXPm^`Q{yw}51)U6&*5_O)G^$O{Eme(es)?ZX~-~~?fizhMOUn8~58h4&R!=KAZ>R-hq+&dk?c1yb2#^`3N9DY0#^>QHh'
        b'o3<t@^?4xHj+h5zs?BoS`|UMrP10sMyZm{)yk*ySRcjJ+el1e9hMAxmcX#3>vlg8C2wrSx?g*N2gQnXdF|BqK$k1eqxCaA4JP0E='
        b'Q71S%WDQxh9H={d92#_^u^%=F!HIJ65oAs5UTR+vT6_70JJ(*y6zqsJKkY)EeI4LP6;_s}UPVi_2(VXY_(}s+zfP)J)5q@t!gGod'
        b'*xmhaO495d9%bjFvL?#51BuLi+3vj0mAD{nq*S>$mA?bCFL6zu(~Za0-J<bcO!+%Zx&L(!)d`;8pr=Xb7mho-G%)MiHe&!z|DgGd'
        b'cOY3C+g-v)i|-m1Sv(2yI(HMpbAQuj7DX4vO*ac=+(<`W9Kn5#;RWAz@a6!QPUt$Jv`pf?+^kT_ecS<aDECnZZwAP%%*K9$F=5>M'
        b'9mCP^0Uw{y9`VRnoIygzIPHn9p-1&&2!Su^C$!A}^|hk)W|cU;Fr1d@!4tzB?@&S6KFlA4Qk2fU*P&V{;Lf1Wo*ox12lB@mNNfZE'
        b'rHkMWcf_eku9x=;bGQ>7`^DT4`YgTIkVyKwCY$imO#AEmYYJ0IaR$+rja%&sqe*c(!S#0(8qh$2o2$=X19hK!t3$F$iQX@G?}3h}'
        b'3nbTo5RJl1s?`M79&{(DE=-HsB;pQ*yj%-pB*hDeG^*VkIitK##CdqEsJkjNxwm;|<cw+vZbG-|1AOx--Xb?f&Zq}42Y4{LoQBo@'
        b'OSe65cAS*a^W2Y3LSUM?!=+2ireK74I6hoogyFcG@WX4V>ysnI@f%}+pl7eS=20LWAb^@601GDMuC)g_-s}rm(b^?Pxw4L|XcE*b'
        b'Gz;{DjQNL-GF;Q)p6w_b3;pv8=G-3<De=3Zwd!lF8s~OXY?Ax4+ox~0d#qT*V#}|2@h~<ic-s?quH6`$6kOO{m?lWN*a|>GD#;(v'
        b';s5wHx+mL1260_bf8<WIhvYe#|2*Z{-tmO2NnmSj1CYPes?HKd=qQ^ckC^c~*M9NJ3#Ru-qmeL*Vxl&YWxo)pjoQvu#~A?|wp3Ci'
        b'ene870i&%r{B+7@@gt2c^h9lzxSZL%(-F2f<uUOi%N)EXye{i8@yc1er?L$?WYk6R%1kqQ&Ez|hLaEuA2tMOcfmz2&3dN5s<m2Lt'
        b'Ai@-kh`%H;J68s?%#@}SiWAy`p74F;7a`f&sr-h@r_IjfpfAA(|FqbgAwU`kg0%3zH10o+1WJ3peM%8%cpY38-)(SC1;M{wB-J0g'
        b'GtB001!qH%e-J~tr!hY`Ecab|Lgvyv4Dzi<)A1})bwe9}C**8DA=UTaX0@|noJeiI#Ly)TY?_!3`@M}VnC&Q-<DZl`v~wUueJ5FV'
        b'i*PszM>gU4bvs(71(3w{a2tOi<ZN7J3+n*b%lH6hrDv>t^JUWWeLI9b$cKfWmK4c60!);~2k5dqlkKV+iq$RaY4A*7%EiG5)><#J'
        b'?h}pFDn}cYRgD_!^CD}b#?p2hI2&rFNtmpcf(-ZY8D>gL0Q5f*!n{!V<vV1aD;N-m0j8PKwHCSOQak3>Vn~)n=DC3JccE`H_`X12'
        b'44+!ZUV?zXV}Oc>M@APKWS&njARGg3Li9)In;t~?50y2Z56~||f8NamLvb7)MO)<QYR_{elt9^k<I5&7-g6R@23o;c{*=sf0)6A?'
        b')4Q)$)_IPj{}%e;-`2`sCgS9*$uc5gAbzh1@5f(GY*Vy037Gh#U9HI2<67w$MyEy-)2+7T_>jud)(%c|w1ynXACle(X_LV6w+T!n'
        b'z@Sj#RB?)^7(Cot?RX=*FgXpPep{F>^VB0c?;{$iV$bgOxCK)D>PU|rBmRmJ$?;ncrh7J`{{;FI8`CVW-tNV|=0m@y8lwh-N&mgv'
        b'<oIc-1tb>y5*F-=pN6Q)2q%E3zKzINgpf~->e-9w$}wF-R4A}oH7LN)Qa-dAoc_IhHtSTKrz#k~|4B^vdp=?Oe?+FJN_jBb`Ph{I'
        b'h+P}Z`ddD7?Y~DR$IDgk@p(4~D<B8A`vo3{O(7g;IUS?FD5KTD)Z}izjF!VhFW38J56JMCisgbVr%Yol)mSSu{Hu~Gsh9<TYuaH5'
        b'V*i4o#4y_QWw(Pv%^V*b@=YRe`Jcn_Zi){o%}qjZxl3<@Gno$(5-@_%8D?Q`-+{NS_7E*&3~GL6Soz`I#$uyD{Fh13s<x2>%C5!+'
        b'nYz{`BV4!_MLa&~32TpwCp}VZ$6Rd3%;i&iLYUY87$2dd<xN8UYS1;8nD#HWG*3Js8$K~a^-_I<eN7^F$>e<ToYAF+@X|4N_@r~5'
        b'rtEg;d=JXzIl?Dos`X<3!HK*v5s2M6Lg#u-+S)^T1A<~uqa)ivRBaN1Q~&gB6kiM4g1UGzzfUSpPjKto(5s4;Y>Y(3`&VtM=LwUD'
        b'P(joq7&Tms3pl_xrgRIu>tNj>P?24F2D{s0O{FXC{zKeYTX6cKDK>&g)m3EVtqKH_JRrl38X#ABT6vvW)hKdAfWBRwdQYkjSXEtP'
        b'-g}d$zita^wV+tqbU4@_0F^f7<)45`n~C|b^r4864&|wjlwDothToB^?RdDyrNfI7Eh{FI2Pr&PPE)1`V(q=sR9&7ffS263bb?c>'
        b'm3VJkqt%~1sm>7JoO-V*K3EUk5A_H;#GUwG>!G`|9)JA*sz>)7_4u~+-|7+hf2c?1|E(VBch&<c;l4~7orFmyaLp61&&XRIa9<)H'
        b'#hnb4ZFOsKCqsp}S4PWNk)V9>J^7YAec<$-w&8I2@c4=m-(#3`zIaPU{L6PYiEWn;h48JJ*;k>g*!@xTYvQ4>;YW7MS9FUN#L(>H'
        b'a~7?r1<41^1uYtP{UkF$WsU;wq){ZuN|y4)_^@(%L7!0xX_hux_3lYE1GvjG)Qx4I;2LN$NgUkxB00P6k=w~I36xTvt!+)Dr7H|{'
        b'mN81(+rlt&4tnv-To|aH&KAzn_QRSiw-NgaXKo8^6j8K+B>%5K$hhSg{Bu>+_UgrC^8!UOKO!#$JnPy}xjq!8Y9v6*iqU^IfoJh7'
        b'?~~96yhuU8Nz(t#L|)zP)Qy!b4H2p>fs>?HC=ibYwAL1GMX0FEi->ztQL85l%CxORVrf?$;vQ`ChUfSnpGX*DmlLehRl#_}2_{_N'
        b'IsqEIve~QAmrQ7X+tMTq)`45!8d^^d+2aa`q*bk+d)r`q+cJ2d8(V^xkKs0_pSJ0roPeAmp>g@YWyW_S@>_zh2qqa@J@IX>Tms=F'
        b'BOI@Q;B;;74HK+0!7C83xY^PF>k0M@$x5R=F>RomcxJWP42SMq?M}Y40D!-1%&)s<SpR^GVU#M9l%5B1hE+nD5d5?ZkHEuJn$q&9'
        b'3|0TIHng}}z^T87m(A{KH8UaE>?v@$6L>i+6y(xN!D+dh=gLgT{wm~+2=x7EQQ={5(?b|BI#Du|NyhIL;PVcE8$Ap%JPHfREl9SR'
        b'EiChls)O=eZdLSa_yd>?%H~F;P2R$baU@1>p*&x-o)qAjOet}Cq!r)GOQ31eM&ekQE3gX;5P};#^;4sv*{-z05d2_*)#CQU-2#3g'
        b'z;mYcBo=`WVgfGQ-&$#5uV9fte?ZhANQp^31qJ`p%kNQ2iOKAhC2t|P<E@r@(P>|6hk&kZB5i&wVG(I3YXsG)atM%46?qD;i?g~6'
        b'0vJO69g}uaZQo6bzYFxrxQ<r+>!RRZ0-8MC+WJrOB-u;SF_tEnB2Rn4uNlz5<atnbx;YftM7rOSo&F2&qt#8MzY+J=aYWKPUOJi8'
        b'tya~Dcq^SMMudi?H&9Zt=ep`2uV@6nMTyF2N1FE4L+WnGyn3Po%~lrp*K#$7{HrFk9~|mX!T?@1(Sf!yziEPV9=g-$9OPNtORadd'
        b'ppME57w9!qUKgP~;N@Ppqr+i;e#4v0B&b$N`A2#V2%OIAJ&Vyo#J1wz1N$N9)lEXnf(hu+s#ghq(5V|O$rC^HVD?bR;H4C(RtYid'
        b'c0TJ)$V%cQ`cud&tbCQv3WL;r&yRVZoXX22fb<yZX+fKLjd%8PyWt1hv+ZTC=hv<LMH$gHGq$sRZ0d;`K7L&*x6RAE70}ofj(O?Y'
        b'Wi3^86vISpsKp(K^sI}dfDY5{YpJTDa%z>3h?$4G=jj+cjJbDYu3%4JOYo{3EKe)Q{gs!dT>30yfx?(;$f_g7a|vV-8z`rZa{ejO'
        b'm1{5;DA|GtM?pB3i7jaR2V#|5((;hZEV@L`%qdLVuwi@dVsBm>QGDVS>lAD)+N&y@UU&%Adb3lJ)kgXZL}4tM`4DmA-nHC)t*ZB>'
        b'g^{HA=Y+Xm<5|+uB=$cpap+grh1>3Lt$K|*bwCi@^uAk|H&?k$=Vkjf#ZmjVZlzQy(OgWcxDfc;d98wuJYNuQEQmN?pv?RzP?&+Z'
        b'7e3d>-Gyjw6Sfr0X~h$_@ruIe4UU=n+8<lbX5z8M;wXySerW9_sTtI?nXRg)Zz3E1G(Z$yz}J7wPHWaeb==XMxc5ol*+9Xlw_%_A'
        b';@C-<N7<T5<ME@o>qfJS*bG(pTLAb-8E#5p#e^z)jMXZ|7Xt+sybW*48!casc_t6>_5#ZU?rr7950&8sI^69;W#<D$!hLy!dFH<Q'
        b'LRG<sUYEE=b&k-FU^&+hW%BR$aMuo%;a!&8)kAoEjsJfi{@v}jStnXPogJmlI!%M{RJUO3PDOKx<{4pmEm`IbJS*)LXNrlDa;25C'
        b'THmo+U$6>kX@rzem*CwE%Lzw;+FKCgj|TNp?bXKAr@SY22bv_bnuXAVS6OWgUI`#2Myi#N!PT#*tBY7h2x0CkSz(7XmYEV3v%R~m'
        b'$HTQ9g65HICdD;q(bzWg5TIt4fGi+IHV##cD%5elL-=gDbliV>3{4_UE%5!~u*Y>zBJ?-+sj*<n_`+HK1GiO+f7Y<G@{0a%W1h|+'
        b'0dpsKa}$yBw32H@NJW4va2GMbn=ITP3XA8-om+5W-86IGv$7P+qq)~xSd}<m6n~i%Un2a4`0AXeJ_v5*1fQ*bt;7^3Xqf3gZLkcD'
        b'<=R_L%6df*y&R+2IOYBwbPTe4ng4GFi*GC#Ystpg+&_4rpe#Qr-cIa!(c_vM1ti5&S^c(qTlgm+)y|yluCz_AxoT5EG{l_ODm@Q*'
        b'N34`)NNG|Uni~~;jhbEm=sSidQCMxnd2RS;hjQ0P)?r0+kEXf#ea-(UtuJWUTm!AP+R~c&!-C$o{|FhYfR9%|yIZ}K^DiQ2H>9R^'
        b'^>CTq)7uV>bSwMpie|g!%pC0O-WcjpDIn86ZI$C=(lJZA_Nzz;9*Ch_Z-3tBqnd~DIDTKgChMyx+d{AF?Qd|*L{rXV3hQ%J9~AV6'
        b'rX8Yw>fK}Y2BWGVs+`K<qgZWpPSy3{Xw?DQ147Hf7NCO7fE?nyHrkeS2ufB>7u0_>!z<X-B(;1tj&!NeR2~2pm(!~8|9u>MCLOWw'
        b'dE)p}zc&fRDVC?O3$DBE)e%5I=wxTVzAI-H<*eGSdP-z+E|YwvIR5+a{0L_=m6Ib{tCpCYkMTS9SGuFViUd%{pNcT)1Wpf?lN*fQ'
        b'5{zz*|0+CRc>F2M>!5N>qP4Ri@;7{>D_v}I5}c$3eAu{RY~0O$(zls#2&t9Qd|}=@QP$^yBbl7La#ky5FQRL5cH{AQyKr9-MbFH-'
        b'Oy;ar^gXZ47e4-d)f$C$jV3|5PMBj?&@(?x-9teKxeMwA-2iIjbZ&R%mo`7I1Z?p#I6k>)Bf$zO`jzrlYB<uAPUZTW0f)8F!B!F`'
        b'p~x<*d}_~lOSPR8XA&VK&e63wb$fGfwm8y7Ir$35u|8T#&#cNXwIUv_zXY5-<aI(;t1xjy)$^rnfr1r^ekeqgEzF~)r%_%bbt!NA'
        b'%st;V8|Ug(&k;cT;EHdyF!yZp*-eYNf8uaW`-{g&iSjO_(iC?U1I+s5cokWu7SJ-=84us<6)ujb4-?t`ieA-r0i#!V&Np)hJZL8Q'
        b'teMe8s2C!&{!?(#<BD4-76tV4ac~0X>uV9m2Y}>adUn;CJ~}LC|K6&c?P4p4{%;=vVop^kujrDz){#yDtIHR%Zy&L)QLGb!N4^Fs'
        b'Rptw13r&9s<YXw83Bf~@Z(`CM&Bn-ml1*e;Gr=9?EAzFNRvTjpd@-FujIxE*o0Qy}eB2R_i;DEGxXK4_-t<7)?>r3|ma;L=pIdnT'
        b'Aw?F@uv-88SlaKsz!oTao?nb%`6`!Q=q^Q8LAjiyTf_$n&CceuM$g(Zk%_vb5=r-1o40P=4qYP1Gi;A}Jryla$Y4y^)_M5nWpX#R'
        b'z(|p7p0PETT6zB?i*w%EoBL>sD_gjBGhIBFE!iwyxwiO0LcIp&UP+;N<!0U!RVZ0`*8Cu0Iwmkvmnz$ege4axk7R~IoCG+a3^ac0'
        b'h$u^xKK*L$a&ND!N#uWhoZEsmZ^G*tiiEjEEo;R|xeqp*XUYzi6(oANr7bvfs;KHqB=@tH;Jw*q@D|ElGiA6PYWo;pQ;9{98|wi^'
        b'U=salcqVsW3m+P9F>SlcV@ql_N$9**!fYtY&4m&kFga(KB{}``TQ*n}YgJ^w*6Uf>0(3(b@GY)L!e}u?pN_IbxFk82-;Q~H;>G>7'
        b'q<(aqhnr$i<*J)aqUb{XG!rG`)Gbh^x+Pe{63a|uY>q2d<lZvoN#PsL{f}V2w0m2!L=U;N;rhqMJjr~N|H?Su+F9H0JFhgDv`Vu!'
        b'V%LSG4=ZvqG^2USU1v9BC|GSc_?9kxUz4u{N5b>a#R`v#xRqXh?SQzs=_hG0Y@GrZ^&Cw(AKcqS`ORY<b+CX7!2;SZkiOVJ+9%Df'
        b'*occV(x(l?$?kJ+81sbl$t>qFS?26Olc<-{-+OiBd8MOYQL+1gRK3Rknz;VHi{f7d@Gye!c7PMNh_45bZ{b4StU%gFZ$mGyh5}Rp'
        b'TIPS~>O(U9_aYnZIUVpuNE3zA2+yRK5Zv8A;T2NUo(b>M#63DW!M{_gHyUz^=<L;5`_$QC^)IW64Y@Q$tNuxCy}0+;>0ey)o}W&X'
        b'+?4{U%!b_T)wJYA$ufG|KfQG1hUfN1JVXdr5C_88Ea*J-7s<?<lV%wBau4@bGtALt*Cw$=2gmoE_d<&nhY=+))3-JzZrGgYT)N%7'
        b'3@;Mj_Nlj5I^e9?TCah$w#&`DVLL{3ZVUo@rA-pspWen@pJLy|00@6y34NC)gLaFA{KUk2%N=B90ui5jPoa?%Yl$1CusEhLF8OyT'
        b'|Iap*hyP*r4oFg_Aqq`jYhQYsIU`6m-tW5^U|kn6JQlJ>Ck&M*|8+@pe8*F)>(AwmLGANzCmRoy{R<LZM)+EyJo#zX^;Nl}LHmaw'
        b'h_~?$7VYnYo@n2f0qu^UdzNn`pnWRnR{K5+Xp4jHCI64FcY$xJ${NMbE2n9CfILd*3(Yxc+O(jPq+kQ0(}a?iiZgA2P*7*uKue40'
        b'hu8tsdM7z(8*2H6rYdde<0Nfp`hvD90@ATmr&g>pfR9ne2Le?@aTt|X5zc?@la`r#zx%(xpO&5dSbOcg*Is+Ab@pCs<dn$%S2*21'
        b'@^_Kl7)~dQd?<R#_NN+o|I^i+#g2^}7un))S<lG(BI^pLdq<9m?C-<reIxHkzUv;_&vV8_`C99w{^?n@Ur1B(pWv44I7$Bjy&-?U'
        b'$@H_OK;c}B*DmU_^devPd@Ks;h!U%*se0MrdS9S=mOeAv_y1Gx{{0MLDR}vIT+W5?n~5>;+bxmrN)BS(X*$c&cc;ov+}X#-`3Dbq'
        b'O#6MG;AbN5JM!O56qD1pNB1L$vBz{<Y7(QmI)0bHrtK%?$&+rKuxVIa2KJ`EuR*tKSNY%!e)M!ryzjw7Q@YUX{WWctm=m0!h*+z%'
        b'2s5M+-^UQ>q1d&sUnVvQri$Rz@<sXUOXF*mlUUX%tt!7`KcBJ;gddYv$CoV&>tD6<sc{ThalfPQ|ELk}SKJ3Z4agVv?V_|Pm`|AD'
        b'|7O20=U~>O(+1?TE3Sd0hTah89Gto{^3%SG3$S23vCy=O3OheKQf8{9Do$ORa)xBGP(Bd7($K?X)SG=_@paLBbzgv3Xwgr4!Y3tV'
        b'cH;-I7PoD7p3nBxJn0M1K^ZJI6KnEq2kcHSQ2FEwD-H_{O49<JC41qNui@kSCdVgORWLX>R{zKNYTucvvkT_ndjJ1z4nY5?T27eU'
        b'iM2=e`98(@r5Uq8B43OuEzOvuk=oa$;9QdWsyOu@V4%FecOS?rv8MX%?oRyZ>3-jwWkcaGB9AVs(hw#O1v%z}`!;!TQ`p1oqsy2{'
        b'A4|0@Q?QSRVL$!9!}h<t&*Y|%SE|%y8*hXkpo8oTlfJ8A(uHsB+x;->g=zTYly6uzg?H7yife(`6DF?-nt;%KTjB=wX!Qxe3s(42'
        b'2tWEgA|Qqsl9bh>HTz5fsA}r#!oxYHG|J!8-<M_*((wOn0#P52PvO5QybitM|6GUSsXBd=YxU*-tn;um&X9_aZIs3d{SNFCO@7MV'
        b'r3(M#S2z0C!Az&Goj#DtZ+%8SoVpYgw4oR3HXTIGhJhDI3IkMR<XLN{L9O-AL_jSj9xCM?R2}8_Lp{@cDqIiwK~6)!O;Q_6s)LE@'
        b'jhZA+MDI)Y@f^>-xL*g-uVt)&P20C%K=OMDW%hjmDBHPT*9B$29Im+5KWCpwQf+kgDpt0ipR){_u`lmOo1&J2^yvnio!=kcBk=Qh'
        b'8jkvXbXoY39@+!(`;Mak&GV%FKl`?A$TRal^Y6Hw&kyf;_|vLGO1|gIYQE}_oZp}B=G|2bl%A6PZZ4qH+fMVURO2O1H5nJ!U!6-%'
        b'RH^Sxwnp;)6;<ja1d0#DSE=vg1O6)CKiOIP!$A$%YrUBJ0-ygdGT&kB<z9<xfyHH}e-halQ&s*Mu2ML1QDh^hGB1QPiz?4gzHis{'
        b'*WS_36;LUw8)7Esj?pyz7>;$YX<zt-C3;S~8l}6q3~nfj)0xWAvr}a6`ncCZ#FS`efNuOgkwBWdl+IKvV2`n=qwH<REN`6wHlO~g'
        b'%p&M5`B8bF_0A<X8+cQ?a!g~%|2-*-&=A?-*i587+kO(azUHE4FTl%GPJLwQ<^xW`u>j+_2i=cSzzNoGl?Mz<Ex^dP*A;q|<}3SL'
        b'>PFBHO(jZqrH;>UL^aDOM!t1x#Ad@%X6B~n>wM})sG8p^<~Ard!RFe5>g7{+l&W&?QCc$Zun_Os_kWp@rnK1KHGkP>R~O`Ku!^5D'
        b'mgwyH1$Oo7+%yv^%wH|-g!>4_;Z;SItpCKJArtka!HetIR7`%V|8ISyjm!v4Xl#V%qh9F(94Q6Fd_aQ}Td-N4clt8=C&CYn(Z#JX'
        b'R41_3V0r7b^T34TZIQXBY_s{yJ{PylRHAdamQ@}VB|iq`Niq7SZH%SFID<Xd$Hee<jD4yXgn%%evHSP&c17hi5j{A4jo<`T)`qXy'
        b'&V4Xl^yHmXlTbeXIJL-L)9BgI%McQk9-6ejbD)j3^>KOV4xhz_7k>m0=G8Q^g}pqE@%F(fJ32%78&I`D9BPf9Bo^7V3-JJsvrbeI'
        b'>(cY~BZl{gfA0xbFS~D_-N@@Qm7G92+i~8wfD>?c;&z?8yylZD%cIz=-UXYBzoPG=W?y0~^exE_y#O~{k$G&r0|5+98xqI*8kCD3'
        b'8atHm!s}`#VbAMo{eXZ;0VD+B=e{mgbt8Z5wEKBmymyONMlMzO-aS2XMf|^(MWV9X@5zk4K$!W7rEGDZWyJ|oA*C}Y^A_yWeoXU;'
        b'rLO%~-OtI8+dbLB!muZdB@6TS|1%dTVa18O)qR%e6KlAp{D`%h-Di~piRyq5WB6GdNK_>>24N5CdzqOQE|wuo`P=W4K`(stiQEDi'
        b'G)L;97i1Qd$*KcTF!C5Az^pjoT5_MET(rm*x>lU1I8X>3Em?@XV8fgsKM?0+!E>@==|9i)9+($~AhWZ>e8Z}q8%VBGu(Do`<8^l<'
        b'e@btC=o92H-Bk;s3}49t$L4mVq1S0T9fcmNK%1izJ-vi)u7eZiA6Za4-UH12lEkG??!S3_ic1g71vaiSnUOVU*MD&0;O5Aw^U<U3'
        b'14iMC!T9~+F0ZNfTn}^;HUOdH&Z_kMwZ~GhI{06alXtK`>p{LE93Vv&$ok*usW{_{Z-mZu;e+>~MlO-xx>*Grc^D*y24rGFv;R=z'
        b'`pwZi)U;4sw^*2lEY4^KA8H&giv)_`5*>ZrQq(8pDH)wteFza=z>%Z~$M%$@Shj3D{^ocjJ$0__1d>gzCo1p6ymFua5fp~~e$3~8'
        b'Xt$N9?8W9Tty)kvSCeif9Q9bqLBdgoC6HBV3roBN{T#;dRhFodQWT?*A?O(x#`pjfDmar||2^yPF~f?SBm!!A#g8V=Byh^g7%ah('
        b'9J8v*LM5o_D<VI7h9RyPiIMG+ox&${?XD+As<5gB4=g%~VAX*p5I5HaNrxYs`(twbONO^)jQUEB-eE!(;zef}b$ZP3GIeqcL4P5#'
        b'&-HLz7NcPly0*Hz6v&g{x5x*Xe+3%jPONHxpf|!Cy_y^Y)bVF%BuW20VV5P2FOYwsK-}(_1~d<IU>?2#d@8E}pNBdB4g_N>AT)>b'
        b'Z$s(NM9%L;Fy0gme?sJy+=wC!1q6J2BO&Oi%H=4$yuTXN{R1RkKy_agi)#o*eIS*n{JY4YxEkoYXCMM~v;{hvZSkK;hv7Z}4bDM>'
        b'%8<zZ77%<+mqgJAL@p2m;6|RrxIio#vtMMhpmf8?CJD@&yTdpxxYrkGMd^)@)^UM&gu@DGRE=<`6WN75ARcgS$O+;|Cgl6k6lXx<'
        b'2(S-J;G3$nI7{GbSoq39%n~@B4y|4m*}I@CzS0Fb-&VasIDDeV*u#H9_~f%k>?jnJp@-KSwZ^m3Yal@=XEcJouF@;Acl0m{XqvuR'
        b'W_XAY+Nrw~^ma7xUc#`35K^ehKT58<W+M1Hy=>$e<Y2LY5IBl{3iQ4iQoc^c#0i|KvRw2idU&HzTmM-=x(*IKVPuA&t3`nW9}_VT'
        b'DHVrKNmgZqM~q;st1J=OU%JCu3Q$cc;c$uU*N}k+h>VIK0Wx~^%KnV1a6}vv15^~Ms|0vV-1u){&C)jzl`BQ|yKaPxfvU_$I2ZpH'
        b'h>i?_;IEb3N}cQW8J}Tdb{Xr?)e+2d8h)>&Z-}1HA;If--Kw%E!$tzO=9N?ee!2nY4Cwb`0J~1dQX`8*&j(O7R@?bkX>Maiz7suv'
        b'?UvH<(%pW~d#Dd>=NM;1{LWztpK}($knSUBGnSloA86+z2GGuDCUH-dScs83F@`Lzm6=kN(#}uNr%OtD!jtG<7L@fb*)}v47UEvV'
        b'Wf3jC55=NMPK%p6%8*r-;YFI{SGHOLt?9nk*oJNk@oMFFQ0+WwuE)}0U)_nQBHg!}tqsH3?*JwJzr*Pm2Po+;gwwGOP}05Obi4zU'
        b'^ykCrMGjEX`Ea`3@uA56F`Q0toDj_w-Klzu|LKLCg}}z2lL0duc@O4nYq&~J<*3M(hts{4e-YUy!s&gL!^r3QqR}dtma|y$L85X#'
        b'mSBZnBX3~I*5xIDd=D^5MY45P2~Sk+#h4e8-yj@SSc!|EUzX%-23aIVf>2$_d{X86j$H%mv<wK%aZM~4ARHZ7LQIwKLv}?sr(W&&'
        b'Nh}#A9M1zxU9$C8yf72lJoZU^Cj^;VgvbF5nMeX`7DAFE+Q+xbbg4@8!D=otos7H&eMQeLs8SR3mm+(AxK;vi8*Hu@wQs}b)<Yq('
        b'X{3h>GaMg@y#FiI*BfY*v;}18l?c`Vz<PMmHPmb`Bxf!<4=o+<imXu@g`OHg{;*3<5{@9YEC!Vgi!9rX<VYjs?xc=)sX#mzIGwwl'
        b'LVvrdp)QsCd6e$+szwSh=tx4k6`;@M{c8Y3WxvQOyO~s;Tjs7Eci&CH?(0;#(E*@iazIhu#p&oyK-i6JJv9K~1vJ)nktMqaVJ{vT'
        b'pG$D)MYO)MRmAu}I~vz6fS<+t$5CHZkdEj5=TKk3lrDEMacD5V0<26UKJ<++5P|BsArXhhv{Pii?~-Qf4#%)mK8RqxfF_y`96@lN'
        b'6WOy}2uiYy=0!g6Cc@1NHIF0Qo)y{8!T=6cJ`HsDX%|nt%OGcFBU{8v^(uyQdu#~`A*9r$DF0)aAThY%7jP|I<wj`tUKdBi&>KY0'
        b'Xjkp2F3$L%F9p~dwe=}QAf|Es28v0An(MC<jv|qdY3w*p(7zX%Yyd$&BC>CUF^Hqri0r{GPW|%8Dx~|2c7@Ma_7%u05CTf}VlS`8'
        b'Dt?3+r^`fkAM`m&KPY;-yJ`og`edoC*NKrV)XUcMMCB5ZF;<R?Y+DzwX=FgTk5Ri*w^#leaBk@en^a)9pAhuDqMNh9@Hi#l>Qz?0'
        b'BeE~Sy!}SU$>@2a$JZ4w{)US=A+*UhUPGk9q3O`+ejb^NaD73V;v~wE0xUpEvy>wVSU?vdmSoVSWk7DHyCjNxjv5(){{NR$&p<g6'
        b'ME033<7P*k$UY_IrBIGpBD)2Kt)OR$?33a7nO(V5WH(6_5@qxZk$tQSQPp5&ndo`6tM>hFK#w;rW8!ql)UJ9Z69rVmr0(jjgFgLl'
        b'cQZ?26@@)@kc0(<Au`qO!`pX8p?KKrLlT}T2uZhBMmL}_IideA=*yEfQvVCR2{lZV=h?1Fw-WbwFh(A7?ZA<08<+dQ(LsEHtvKd7'
        b'iBn^17^C!vO@reY{^%A=5!(FA1xAiS(_y?ihKU8L3cFbyyJpVnVqzsfN^`IsZ)vSJ7iH7PABWl2#bi%8o&U4rJCG?*AEb@qKx|f_'
        b'ev;!}mU@5+{>pz%-f`d1YcB0&#s;Zg(zCu>y5~~U<)sRuvlDlat2ImYdC6TiSMS5jpbXui`yHxsA5=jZy_9Dr8lMShJDMSN^Q7n#'
        b'Q};xiF0y#KXujEn44E3Lqcpj={Ay2J_?NF++!Z!)E~l8o<4?-Wmac#>&7vpK9gnPDD_N7)OZ?kEgh@voIm29AWKXx=Q+uPcVt_|x'
        b'PaQJ2C`~M-^Xe*2nK%kDDKCmTWJ;qp{s_g$9}cpSy({?!zu4*9KWdS`yDJSjIRr5{``yaxVV~Y}di%#aeR8a+jFeO414*QuBp<kg'
        b'loR9wT2hXa4@~FhEUV>uk)`p`WuEUlea6RY-eqR<#y<@E-$wCY<^PUN(rGf4TkNCBXC?D3dbm(LhOfHtFP<2+?7v|`4i85`<3Pdc'
        b'(0#^FJ9`QHM}$3E?lU}Kny0jhJ)YrCdo*U6r(>wBSh?LeH)F9WBa5;W6cl&M4YOq06_~~Fz`t!ko&%jyNb1=j0J%-Iys*t=qN>!H'
        b'$yOCFtgBM%dExOYbxK$-<psV<E#n2D%6F0dvBz0=i~YH0<eG@mAKYXw^o(2<*&lkGnw#wTo{=9#$Z;<Jh5fn*)J8Z*J$pKpex0Rs'
        b'ou!Dh6cGzl3-I7QSO5JkwU-E<z9sNO{95$%B+&Lp$p@GR@<D4ZqBwyM-V_l%HWKu2u?|Z-Cp-@6k^4X*-v)`wUn6h9$#F{;<s-NG'
        b'ucEAnFeImgTwMr>uH?qEY)vP}8MT3%K;a<X5ttDN0S`f4^UfU3yt%WFQ>E%jJ2sMpq;D28Ki1i2S7mH>YvhdNzU;}o^3Gg?6p{m5'
        b'9}abZqT7c$kyo096Q1961%{2lgStZXsQ?#CIcDNgF<)ats&6<N-5agfMB?uSOsZ6FSO@h^b5J$a=;bs^@p=Uoa}2dmrJ_cjMrgN#'
        b'^KHO#(#XY(;o|lFHC_JSbrsK(fyOi<8u31hie1vVkR$EWDkntqvpq&U>@3ave9vjSDklw+Fd}j>Zoan@jcfV{+V%Cg+1lB+RF$(>'
        b'L(M3}CZvI-*>qi8JNjVAM^j7=>;{xvK~<dLsaz~JL&tfffMvO8xEWoNjfMggV8Q^q8HS2mBcF<9u9MT8*nNfohG)d*aFf$1`R_Ex'
        b'PnEs=pJg~bCh6(?aMQ!z_7YWx;`yG_$l|AwtawDF8S^lm0pkLP7M5fXFaBIalo+?Q!y1RkGcF6r7I-5f*tj`<rZar|hZkP0iYw!V'
        b'KUc;5ffu@}8qaz0+KJE{FGwEMJ3{gi0`ua1^(xQhP@^|Aiij=z`(NnyCm?cr@&5aIP|ih^bKdhSw8ZpfF<k8%$Ry=x_J9H^{|ULZ'
        b'XKzC{0w)FVwO`!Mi5dA?Ot#KR@K&kUBwM4L`IkL^4+V_b^jBg6$YZ}vIEaL@zloj`kh`uD`8(tN)m3U+vQ^FdooF6LMbEKN=%94B'
        b'NHS|KKxR!z=<>WB3dB6@pfS%dG*^Rk>v<Crs!HUO*fR))g_z=0|KB^2<3Hpw)pHQ?iln0=?EB`(NiUydm0ig;mc*oo2yZ}WbNAF+'
        b'II84H<nQ&sc4FiXtYj^UEr}kRA`f9n1s@+Mh)ODzCvAH_{GOWUsHAPVSG=(nE;6a$o&%-EQ2zM7TZ4)aX{f!nQvo_VQ<oldce?e?'
        b'q<V&VCB1&c=nJSZ8pq&Y0t;4O10E70>6@b2AM$+JZ6OauoNf2|M!pe~w$EXF$r_^aOA##tdg~na0~N|g5s*T+NF0-%$x3&(Ft#=X'
        b';#P#~r04x^$0t&(!w);PE*wxSDOCnIdGYkrn!_Q&80cz~Vie52Wb}myI_w9K<wF+kapx<NQ`O)t*lp7=%)&j1KHQO*U6>^-)MYh('
        b'Wh)7B+!kgwu=2ra((}2y6v4nP?a5#46dd2_FaBkcw?7CfAvVTaU({-3)^_b%l=V3fh%`&`qp9SXj!Vz0)_6~Q!+)&v_|fmH(;g$3'
        b'Sphwk{}-_^Nq41M<JHuhH;}1!MbtcP)Js7h?vh*H8mn39+<X&tqUA+Pw7h3|{R&VG89FNMxL%c-QlP$zHW}-5n{@ys7ZS-zCwEKx'
        b'mtXQJ{K(9q=T+S3C2urCr+POFxX~E3@;<sIV3iwDT&VkKT{@i1{OF~cB~Hz)k#SMG_&WPcx0P5*EM3c}E58cM0-#2P&yqiM^G5m9'
        b'dG-}%HisT0c>Uv?fFJR~nO`4*vSrx}(P2$pwsAlZdvVX=(Bumx4%$;_e{uRhFte9!1evSt^+~r|VYy(CJiw_=Jkovik?#ISy8XZF'
        b'4ht2YSs^%5n^qqWs8UmpbE-gF5}d6FL|5S7XR8$NLUrQ7?xXqL{rTPg-*kI^gId?hLww5PPAkq!&I0(w*dS@RE;0&4565{`s`t28'
        b'HPDviOWA@z9zNJho{q$v6F2E_JQsk=j3yscow&dI=>6UO_jmiP-5#riS5$~M&a5dNB*TxqJr_G}<JonoOT{516PQ6VaEkc%yY<`f'
        b'QoE1N?e3r3?N99XBuel;N9{lBOkmIx63^uh^zMlmB!gEcu?3nxKA=i{<I)={-na$99{2|#-D`DTxEYq)zQUw=XGnBw`W%8_v0>(S'
        b'Iuf3-=*t7hzF7{`tus-kjB@SUbl(1s{%PGn+qprVrxR88d<_ylAA|8L3xal>H&{@lKM&=Tje_`ueB_@3#pROpnE>i787<C`Dg`Mw'
        b'{~whO1C>w4qFgeX_f1#9^QUFlELRjG>y^c?49>b#61<%3QY!m(fRo|02ni-G_@$WclKU@oq1VHw#G1EluXOk;JM4*fR!DcvKkmw2'
        b'*VC>`q(Fw^DeMu#y}YhzWkGw*Oyqf`ye2q6Vg9E(`uYly%Zzo-7jKU5{%4qOt2%lKnA@=irh5G1<ZMb)2(#6O9tS%Q-;!i5<Uh06'
        b'dFxpec(Pd`3=h>LGDHf+zTO49Ri3Y=R#_)~F>0_&1*+<mr&q$CkOlr(({)hsdPAA>C(3J?`|cWVC}wx#9kqOiFJ)fS>X3Yp*})<|'
        b'-fT@ZFiWe)hW14bl|mUUYq-xgGep5i&0l&W0QE-{!tNnP{!312iL>$+Ec?(A9bZKFitu;w;*k{O+hG)UR$q_z(*F<#BX_V+GXA!d'
        b'|GgsKyID(ZJ$UD(ZK~?6r?<kN&^_?arY<*N_tI(S2frBad72x`d{$QZjfj;|h#N}hL#cZ1Usk=G!^j?!RRSl>eNA$u_-2asX~L7&'
        b';WEx^(uRmZ<T^$gfW@Oi19+bTVIN83k11+4#IG#gNOjDA>#nfzct9PKFKo+wL#cg+2>Z5VqQ<`!8G3!(XGVOz`tQbp_3D!V0R;<q'
        b'Od%2Q`;-K2@=etHB)ZKW{92rp6V1QsNU>S;tW%E%SPF;+#6=-TH#Wf#4gw3=pygc(Z7R%}(Z*=<hnujO8Q60F>O3o6uzc(zD{fu8'
        b'0C$q2LvpUVStGaNrBuQ4sPyC8Rn^be%Nb&QEa6DRkeu=IboOQkPt4|68E6ac^t$6us-9kHoT=p^Hb<j@t%@jHbOS|X>X>>w<h3zz'
        b'g{4Eu>#5M&LfbrH?{IuqF#g)J=;L5shxBNtH^TE<l&Up%bsY#r#=lWy>gsqSJw!8+z8q|oZ;6qX{HncyD#gEsJ~19d$(kn_8Kc!X'
        b'w~sB+x_+YH5uYXL<02NK4@EW<d2~or>!j<8oH;i-Bk7+--Cu^{#|8;cJSuQpkm9h?U5xx>B;G6k`@$JxMsL}eq*^x1k)CrfcIcSu'
        b'*c+qq@m;#Hp`jPHhu<H-Uid|Pkhn{6B-N5iI^U9c)k)i)yyBgcl>O9|f++L9Iu979!7+g>`|6}ptNCIlBQvHsIfZqtb2%uQbR?9#'
        b'f-LX}RcX^pyq~k}dy#GQE~=8il0q|?vv72Ph#=7mte*DRbr7rAJ$spGWTr=oqe)j@c~xXzmf9twFyU<7UJGYLhwD2a-;=k^$RiiU'
        b'ONjM?#O+O!{^<&N<FaBD@f_%tRhF+ncpa1#`%<*WZjGD(>?*H|Q@*AQ|C;g<ZnQIpn3&`RO3(Y97?I)D)lP*6VbnUKN&2Rnkx>pT'
        b'npmm|ekAsE6|9;2UaxGth3te=IUCP<Io_*k%C^1PIrlBbF-Z2xJcFH*`t0nAoPEjEM>*e+UQwJ7wW+u_C(3)p8ntarFO6L2#zl;k'
        b'nasBM68fSz_wB3(JgO^xD=1*`nZp#wK0|-5>+378d2e9s!<~x0|E_cQl{@F$YU<h4K9sa@CY-<r_aeGEmhq}C@DAw_P{01B&S3?H'
        b'-a#pd;Vf(*3lC%wJ_>WLzV6E+N6v~5Mlg2(GkBjy5p+BsA_&ekmjiYTQJBOV9wChOTymmhGcn@8uJEP<E~3(gz9bDFl@A<cdZ`ri'
        b'IC<?Z#rF%nOOmXQT*<!E8ADmw1N!Ji_7M_bl<>$o1wVX+Ar2VPY9|%Q4-{ncqgSpNFEM1OcmZx_iS))_hyLJvn(hUPLr-u52HAix'
        b'*RX@M3pl!e)b58}KAAgSMOs**BW(b=;Kjxhsj%}dWZ5v>xavH1!>USuwU3_}!)V+dTlikXSSb^mv7=7wy}l?1HM5`rAU3i9AHRAv'
        b'z0qq`Wu+nM({WXVxh&o*Su{$jW7(@gNzzpM(>h^lJv&heW6|dPgptQG`X+j1!LzsMlOhJKR-rOXam;aDoSZv2K+GvDdsoLG-YZK{'
        b'6%U9HD#ng2$}joDy)4^lvvzVtD7015@ZDS@RpPoEa6*$x8m?VEk~6^Krnit2i{Ljvp*<JIitWe7n6(-D?Xxe%r=eh;-0<}SmcPGn'
        b'6xx{Dbj9CY)i(ZOeC`1EHp4lth~DRttnw?_hNKu`BoV96^uAb9hT=yYD5IIiL2~zD{2(hi?r>NodH=Hm1&<|_Zb;hpf#K61fMIUe'
        b'>e0ru;(1p>tLh^1{u<0T+`0Nmi#|g8*45zWw*~~<d@AHj#Rf=>k>xK&H5-CZ+}B4TKO@kTn!6&a4h4wGdWC>}XL;+x18a%Ozlq~{'
        b'SLnZj4wacynsH^@^nw?yY*M!EKta|58GTwzs{b_;tePLqJdb>%jftTb2T4ykn%t33M9?c@2;hR&7Yo?@<(T6`NRc>BF2*WPh$hoK'
        b'%M#4-w{YoVYy_0ggDPo|+Ug(gQjGM8=Iz1!k8q1#ACM(5@yK6Qx8%F^<Ip1ntl`%|Y2{%zoI|Ouw)ieySj%WS4&n?645`B!YoV~3'
        b'y8ib<P&*ePCE2_l+&d+Y!ddlPkkij|=40$zA#UwF<J!;c?9oullPTNTp-@U4`qPH~ykaX1BCnW<5r)C5g9`tVkY^zRGd^Ervx3g*'
        b'Y59qd*Q_kiGf#tPkT5Y`B#zr|pl8&@`8R@pxg``*!9V{{%-=Np=_X06>%~bMN!kd~1_^BZjw``;U^7b&+uy_(MR5?@y&*>Er$B^c'
        b'5<qGLCfRpHC%mCcPyk)#tq*PfkQkVWRb1{{X&RU%9~SVw*OUQadazH-Pc&-BG0B0Q&{xhRFxAET#es-8NKFLyL2>NZYXkd4CZVtI'
        b'=Y$QxUeQw)Dk#;yM%KTiO~F9)ssBUG>Ooratyxe^Ul)t#-zYwGD_?)7&<Bj?u_!5afkQj~qjZT$hS8we@`-%DfV<br+?6trDKC|%'
        b'+$Fl)66DG1eHpXC&>;@e@5>Sv2KS1tlemx0*eQ!Blkv0U?(Nh-;&ULV_Ps)(cqF<-r;6Lf+LBP-=X;s-2HW^oWWBB9bz)>LwmESr'
        b'b8pjndm^8)RhHq9VeuK*R{v0@DkDqR_o~jWZrr^8%T1X|dwwI6uq<x8RUF`!J@M<ko1RfRvt-!>zaOj33uSnfyJH-l--a@>ZCTc5'
        b'ZI^>2u_`wjS!y(dnTf|TE|A0md;Y^H)br~f!1maJEn}kXjze|=d%_m-+!5N8sar}IQ5cN?eQ10M!Rha`#e}$Z5q7<em51yuj9mz{'
        b'WZMO2We3QcAw~RF^fG-Z_Dn<NG10ESleACz3?-hpTS6q=kDfb8cFegUCK7q)$_{`3x21-T8beGJvfXwdDmN#FP>{LB*pUhLjrIVC'
        b'UIXR57<^2DJiy3)2xqKsR3Vd*LFM#HW+a1JTYxhJ3L=cc`z*#huLURf04gRix4YaqdV}MX{uhD+0d%{c4%;?uf%ZV+Gw5AwWXMSB'
        b'x`sHx+%fR`a2|_?I!OeOknF`g#Xb>4@CX{<{ZfzcR8vAH_5B6Iwtt!r1bGE!A?KRB$Z0@R$diO{NIE<%>6B{h7#!^*I5HO*14-(C'
        b'Asc|>=G2|d?>a2mQ}6xGcW_g0|9pfFjyp!4UZ%3RX!E9apMc-CtoPNcctRJx0*G#2*mcr;0!}1BX$YCQxLt`Ua`ni5h%)VHW;6sv'
        b'67&{qff9Rk3wAF<hD$8@gt@Riphsi25@8UX7UNs!Od+#BfY};U+zxtzKPvgx9##|nKX-s|w-Al;wjXA1-~r2L1?cwE3gf`h%=Q5R'
        b'JrqW_(c#PtJ8`zJa3a|_e5S(y&FUZ!s1)*b&K9K%b?-pPk~F1p(3mQ2fQ#S-3-2T{{1Y0OqV?_J_`OPE0y7-*G<WE*RP(x^2FFkg'
        b'S=|MwrqliG<^%5MY?%C*4pYEDJZn&^f}~ETGl=CSwg(Jow4F&)vCVgOc%Q5}?=xb_4W#i&DfT-^|8s%Ec^c3NJD=2UxRs(n>Y0Q$'
        b'HL)6BlxW&St)KTRW+wElMA)-U<Js!$#EcATYcw(PFqS=>(Ld2kSWhAcZ;Gi82DZ%|1=K1v<t&a$q5K;=m?+?t9(ho*bP}UDpnH+}'
        b'9C#FHiHi)7)$!V%Ks3=$1hKeNFgi~%8cW{W?NF3!nCMhV7xtx@qo};E+ccCcY&b6ZOFN2%dk^MS7Z`I3sjV-|O|?{R9<?f#%a_Z6'
        b'Kq|g2T&di&QkS1CF9>7|O#mX2lT`FVnkYKZ4xscfHl;#`qKe03$_ZwsV+M%iP%-#Dh!9Xsd+MJf@52d-#;UOqy+pxDDRi?0W`HIF'
        b'EFOIBss<+>QDFFlvulFHv7)!z5W1OEAn6%s14{wro%5jF(E~I5|AICC$J?;93vb*;Pzqf=GV-yQ9T>%>F;E!YF1=rl3iw|r){8n*'
        b'IVXtPr*S6A@R<=y(+g=sz%=4asdYMCA?)x;dy*}x1LO1|>d4bpg|+U8#+|P}JzupZ?NS>2$&+;)NB^eB#aZIyRcEK0|JX*7^T?bC'
        b'l1w9W<j9WqH<2MN>#+2IEd0^Ie0{HlgrApAyHvV++yE!<r@gu~H@b~F-)$weYj4{Awbw#b)cj<jOn_LjCc=`at<f0L{+W6YR8LKV'
        b'stf0Xs#x{S^e5J~krDIA#Svsg8o5~R9?+k@S9LfowGt{GPJ^>1)eE&BNIUL@Ce<rB*@`jV7<AedjG9}rVvt-m){A?7+XmD6L|z*+'
        b'lZ%L9$S6)XfBRje)x7btX&z<blok~|#Hn)AlsdgG@5weUkLC>bJBbKJ?RjS}msw$)x8qgq8QMY_D|nq=X=S-g<M(OMDuFIstE{(a'
        b'_sWd16$gw2C|Rd1DvmN1a!M1YgKEphKmwK9i*V1~2nmbf*Nj@b_9AQz`c)C}2sn6_tk9-@k3unGy?8jV>zeNzr$tU!mokq&BU&PL'
        b'Ti3Q&W)%fy6*38fv~Z-(w6SjJ4du{1N)+iU&ELoAOctFb)9Ac#ZRE4?p4AYMz-}=70Z^P!T<bew&&Fv8g;JRco63-4$W=@f*fHV4'
        b'ny#9+vpLJ#V%A}WF#ky!$E^A33x5WF>&~E7mEMbyr!)lJ|4=)$1o;N@UzpsNwzjZG#oRdPMuE8-S6Qio{M>@IHJLm|<Q5FA-rTg#'
        b'$eAodl0IVoB@pK4uz9T(^lj2k=&bgLbw5q|07l<G_vTYr(oBLjV0k5b3uFa`q?Htq@$5?==Vl`Rau18zQ@30c_Qdb@o_4A>th}@m'
        b'{v2PaTC=LK?`KPKv_u^eZ6LB}OOe3>5JHFB^H*fIbS<F@xX+${`W5qodke^4iu1k*93m|Sz9_Z5FimGE=0U_9d&{4*ciEV3K<7D%'
        b'+QjR*Obi52`U?@$zIIjmhTvbk*YhD7J}t!z!gzg&KE{0SUWV|ICaghU)gZT!70DWcP2UT+6UoMFwP|~Ok=X9gKTjJ~)!ZdcReSf|'
        b'YVJ6vN=-2mTK=YX`AxT1KUFA|Jis+_l~ZSpCvh()-15mQYGOILDST$?j+e8u_xjK~|K!-Dqp^DjBe%S8M^wY<9jZnz?2SfbXLSek'
        b')ipKET)kY^r4w{N!)Yw%eDqW-F-F0}f37h7WBaFEhepejx~%g`o}1PYqwqWz;N>w<UU&C)UQKWOW$5ta+gd)KhLcWc)V;3352kr;'
        b'1rOz0<P};CJxpL0xd|K7!>&$m%7@c;Xo1QXa|fBNCW(lFQq{&AeGN)egYMJwz5>YA)N{@*%=r{%wOdHt*0Xwx+*ol;KyF5i+6Iat'
        b'&}M?HL%YJ;DccC+?*Dy&N$|xN-ly2LsLlta7YE{tj!R(sdg>}ZFf~ZKqRWroQe+#gp@_4u8SO?jN8qbm-HaLqR6=tnlrsbfPwe|a'
        b'n83Rtn-;L|2ANnR!4tS(9Af0U9oyZAOG4dvPUi-0id`|v*kMphE2Q|KlYV2QlH~d*&ygT6uSkv|*u%l8Z_fvyGS)N@#i2X(UWr@P'
        b'_63ilPggt$V7l_8f~fxfpuaz8I4%m4JQ>zH6ofKfj*X4#s%*|}NS83&5E;VL76fLEh@gR&o0vGvt51#rLB6;RT2tXS1`WXgfsN&$'
        b'SBW=7=)Od)^3(;HNUz*$<VSC~Q?`ehKkx|9l)`q|yqch0hG{9$C16i@gM|(qFT<)1eC3UB*)U#?^ERAMj^3dfzb@{ilHwwI>EZ@a'
        b'aF=5tJ#QnJ*!XJqi`#uRd6FX9^K`KP>7Y+;LN~A*^nhViEdIdjhs@AWq4sQsIR?}ryU;u2ez9(6ByWo}y@DL80qfiRPJ#2(mH3j%'
        b'FT-)8xTvt1-()Hm^d@s@kcoq{1voZC>K1OleZRpctOM4<bNKG)XrPGnZ>O8<+c4^sBxa>zs#Npmeu)`Ax<wfcREcg~D5HQR(ftf1'
        b'0cUG{XycE&>ZqYkl}|1wvvHmD6lbZ`mo3lGO-#veUUjzheM;Mg4GW_~Z>?q8Ok+<DnaZ>3R6ZkNF)DVwNSV^8^ag@X#z;ASP>v)A'
        b'Z2YolRa;17#MxNSBZ#ADb0R&B0p>Z2T#<pUJt!Pn%sL>+OA#CXVNMEWlUX1yos*@IHeC=o`~iL82x`e|h?;FklprYp>{Zt``A1_;'
        b'#ugsLFQR}et3~bM>%$r()KH#3NnIVjwoKuXzS)=u{noQJX_5;NquQuOfn*H77w=POpT6Qi@wGt?X$o0SHm%K8!>kV^;#0B+oK+|Q'
        b'JZ3$kC2wS_dx?X{bu9gDcpn9HzEm9eqs~noKd9m(jl=t|hWW(71^iMY$W4;{uIP6G6jOB8jLkIee0{oCZ4$~&Pf)O25f`ksKlo>r'
        b'sq;$xM{@#aW)=;|<)0&}E)YSK3%pM)jX|bA<lX&F4CA2vfMU{V{eYUzdQ>)R17Ta|kNB3LlQ3u-@n{mP$F5pxYwT?Qa)0e3{xfk!'
        b'!$y49r@CIE0Uyr?u=RLDOoJRqCgW8dEY+})l-A1d4-t;Di!wOY#+Kw|`p?WP%s4Rtq9UvU@>u*^u|QpMo|DN<Cdw@_rHT(OZB+q9'
        b'ZUX+aM4q5nD)amXO?NM4cpc|xOndTYhM?hahc2Km08$Vb|4>BEX&uKVZGB5|&&Pgb-im>KlTwu@1?+a0#ovoN749j1Bh`IRs;iai'
        b'sy~;7tM(GXZ^g$HV^1^m<hOt)@PMb%Z=W?IBU|a5C-bU#xiR_t0}*SNM4VsZwbbrz-{n=7c&B@2`bk1AJpute=>hE$(ypf8Id?ZE'
        b'JJrty>=6Wd8L|ZR3HXnHe8ssCM={p1S*3>nc;3Q5F6im2X4njVd!kB9U7Hj~D?b;pv6*=l?E?{n|JnB953XoaukgaCJJX$!@pIN|'
        b'QHB?PU@jQ$B1cYwI6WZUPF}y^gyW((IZngqwVn;08GhcVtf?QxKbK7gH1K>OM68WI8B;jSV&OTOj5dj3Cu536CT)OTb;2|lFsLra'
        b'KT+o9{@ipi_aj}nI!svccd#cnUgk(+E~n%c8&Pu~&{EmmdG82JT)tshR`G?Se-lubh7U#0en0Tn<LER}RQw@#@-#x9Pf!JW5oUNz'
        b'gyqn7UH7Ura!k7T(M_L~d|TbquInqelNH)^r0oqMFRk5q1LOsS+pJRheX3VB{-x;sz@m?bt*|s^shpwg+47A)XEZ3`^y)>PdlM9%'
        b'!+uG_M`r`q&cR_jfN{oIeqB2-O(9Gi=sgTw_GDQaNf8<fFJjx5YFuk$$;FYNM!MAWW<R#6M5nPwXs8HRKFw1&lSSHTja|NJo6=b|'
        b'4HOHV#182+jLCMF=%5ld|J1>G`D?L^Hqezw&)Wjh#Hs~7Mdi+)FcEW@nb@iia&xIm#j1Q#SMlktmCC}Ex_V0~wd*CS&_(SkQC56g'
        b'SV)EQOR0*d3QMWuC90|48?P6ZQA7X!4STO}BZYY`>?%>^=B|Uh{KdK*dMxHt=_}9;iIZED4=K6S{)2wL2><unrWPTrBx8XKUKP{='
        b'm8oW?5E|-Ct7I^s=8D%4jpozY+X2lCJ9Ro!g)$cFY@f8**Tyl_0{dOkB-YF<+&1)7nx3NjTm3o~1YQ#0Loc4^Q5OJL59;Q^3G}|I'
        b'?Lz;{{=yCJvgN4!SqTLYh5Z)*fzHLwQ@HKdLT=&&hORWJY;U$<+EegTr%J_a7wl^((4s?&LE#tn4q>UM(3K~EvJpYCz1G$#p%v};'
        b'G<+wG6D%L$7BVAZ?QH-4wv8Vf4qUbEYqL<9g=xx!BqX|KW+E+2Grr`ixwB2k(ZNB^C|ry2;zxeaR!`$oW!glAFEOSnR&w&Q7$>P&'
        b'E^1lBT5_?>wV1L~arVWS9Z2{&{iSSGb>{I*RZg09twlp;t(|Ux-LO_35L!IDk<6P{+cvi{TV}o>WYO{HHeDHRClyRmVW!T$SW#5d'
        b'W~)Z(ZW+ZSmJF<0iqdus#b{yP3o}jj#e`MHQ2B42&P}Y#<J&B6T}zQMYEvSL^N00}GBm<YLAeyzj!EpC=Pnoh)M|_K2a@ivQ*)7r'
        b'rgmLmF-CtN0>!U&Tosqr**3H>H1f)jnHb)8p2rccjAHy9(Q~eqQSe6O%+hnCl{p-aMeQkSt6hhXlOi#MW#OC-!dUyNz(*>o6pD(&'
        b'0*a=m2tJB?oNcwvHYP`^4S&3o7c$VE%giFm%pC$pDw3%v`~Djlh@mKoOL2Bd+tD{$10bwW)-Jn!?z=w@qG!zJ{jE$&{s%ZOTLJvn'
        b'c^>2K4$qNRIO8W#w6)n5BD{7`lKCxh*7+z%7%3)4y3xSPY$Tb7A`s+jWSDe;^vimpK;3|^R@HL_mIijUx!OZ!WBrMstLKAYMcNfX'
        b'{S|HX4e6m7k`WKL1_U}BG2U}$8*6Cu$Dtm%Qe;x&6p75zT^zcn#^ofkn*=7c(-$BVyA`t-MKA~F2}MN%icDQ5nc@)RMOBShKtOkO'
        b'9O3WC0Zyj9fO}e7fqiT1u}{>a_5lLjEt38X<$q2FgHy4}*1J;Ki2wkx5Q*t)XND7Yfdc6WrR|BRUh&Uj*oeq1PA4wr<p`WikxWjj'
        b'cm)n$ZVB?jVaUVT^8r|bFo29SWw^ENhk$t;fnQ46e%tE$5O>iT5hZ9HT|{E?*MA64GgDdU)fKH1NXnV3MJ8nbSEvndPsI8z^!5E5'
        b'{89Aew-#*^0>(RBv_yqM`T96rQ2{hr6>d^=ED)fvaQ$)9MM#gQ{166Tv8B+fgk2d1=~|L7*?kEyGAf4Cv%a2z7McvtBaJS_dtM8W'
        b')N-F3x5KH@slU{y5*pmck-IZDtg7AaAmuW<oa*li_+JmW1gh*MAT-iGBS>A*#@%rAPp-GRRk|*o0eWIV6x$k*%)E&@jtbMTxj9fk'
        b'Cci{DwqPX#MCA@FAtE{baofLIuUKYk^QWhf>_1ykJY0f(F<{#r7+H%Y*}p|^GZteZl8Lq)`vp`WQ{r~pc<X&c(LF*q>U?gRDr^Qp'
        b'KUYwkAJ?TSogBtx)^|W(4`FOftMQ~ZUyBT;tFWXqtX*&?&s&2YYplacPPW<o+p}Z@orl?`w=x^D=b;NJW34WM=p|h1B8&Hl&ZqCN'
        b'JrT&JlA~qZTC8|A%w5tM0zF^ZfQFb&u-gL3FB0^};`pCMbiuFWM`GkX(H_9E)F|RP$k&er*xv^#e}&!%tqFjPig3+NOrcXqE|cIg'
        b'6)7*Kw0nvI>`GL!g9wjo)fs|5DzblV@xRi_!Tx^XDdcb7aYV$NAN>%#ctzNt)8_mDC~=gc;+swAdZz+f=4aByb3rCtw$-(S(=zK_'
        b'=mQ-)*b?B7b(T+xc^0^oT5@;?KM>1Op=2t}j}m+l$^&j2&h&1m$9LB&4ZmRQuL8DvCE_ONCh5H`|9u#sXI@}a*HFj7Nc1h~Wn%LC'
        b'fG<(S3#O{bKJ<NHd+UIpoBTe2anNTR$ElF>$=ViDfl05k=WN01M<nr|3t-7FQS8jXYGN*tLLwI*Wv#2mWp?$9-RqRL8L$u~uP#K~'
        b'UQMl9XATI;;ul5d1ZEfTrGcWTfQ<@B$3g<NlnmE$?f<ec6Kzs^J~gsY%-#&OAY*+r;V2WsRp!!gtW;isr9vU(fR<;uWC1}Q{7_6s'
        b'2_*<;9WJG3V+#|<8y6spdjK0hDegvv?&6bSKN!mt9YmDp97vK_M+`B3T=bmr_Y(gHA78SHxYwNBV)-C^(EiG1X|+&_beRH#hcu-n'
        b'Q(=h0&G{_>J#t!PKJFLVC@b0dV#!&Vp#d?naF>Sn#PzOdHX9Zd)q_f`uC>#LTvp6FgXr2k>^G7n154SsRy&a}HjjDEZcnfs@#m$q'
        b'1Ss5PScWasU($m{;Xcl(bcyZ&M?W#6bt|xm1(*?qd5X9|1W#XN2retZ5iL37JM(}<(Mw8B9$-U$G;hFH)}`7G`SU`4#(`)<X1mo='
        b'_F}kb*12CJGB!-|YnsF`TS7}95#gJ@Vbt8{4+uk?9@BLxoojw%FSS?*MQ{*EOK!0%41*&5wipKF+JEDT8_km|Xiv2N9k)|9G9u6Q'
        b'Hg&p0Rp@eSXiR!S@h7jnK7R*Zy4mXjO#_6l2GtI>%$#E*GqL_>{A5IaFAnUi_|RqN#8vteu}Iz0vk<gOU!*as>^EEza6|=QdZ|ri'
        b'>T)0NQa#W$Ftf0$J=h?6E;e%%1{^uej+5i22PkY{=EH_hzlVh3WO$y8_b{k^<tQTK`okPSosPtWfGOfa07&~PtjnK7_8-l#WDF00'
        b'(7=zKp=%|2TPAn&%9_$(O*pzO5)m%fcDJy<@$YB|^Kvdyk*tt`pkVkG<PAeNnyFxybm2*&*A(-2E$my(0rH!kI6i=xm-x{(27VP1'
        b'nQB8w^!r;76N#U^ugG%?Bo<&8y~vZ_XwUyb|A^$7B+l94Qh55CrwBdSHPiD^i!Xo$<liuIVMkprGRGU*#I3GGCeCmi^LSdASYI~b'
        b'lOv~5k~K`>(fe!XBNFkIV(Bg_L193~RfK1<>wY%gZzb6BmXf#PECL*yir}BF7zQ!JjVt}W7XQmF#dgACC(JYbAu`w`4iF7B|6q4E'
        b'`)2?TRELpg`&&5T8?8lzU0B>GO7R>3w&9m6=HIn|gfu`l=yVi_N7^?q_K(eeY_e(5O~IaoC4G25CuC$<5=vf0?`08@YN+HhMCG55'
        b'lf#$9kz9$~&&424^x~H=*Qp}=STlOWIvWx4Phws{Geg)v!nwr>9F-9PY<dM2(9Gc4r8UioF7CN#T*HB$=OQW}#MsY;@Yx)3K6X+D'
        b'i0xn1;y)+s3g6PVCmPZSp0fGK+^SCr+J-%Vt`b-CBxnM%ys+`8@?I21VX?yVxllBQ;O(Hpu#(Rcl?JSTaZ4{Tem8-3hD7=~APY-U'
        b'n^Lk8Wn#8Lfs`%Jr!d$7`F2M>h4&v2u;=yCRYzpm&djGMl9J`y=N7C3?KR(}L<fB3<;jhHE;gJHa;b_>F0E9#Gm+D-@RrmnsPHV>'
        b'jLjgIqV#e}&(X_P)Z2BKB9z}icsJL(I@Jx_4$EzG7-^S-R?aBUhiud+X_8lrd<P2(YoSIQAYVhV)0^KJR}|1ma0*Z>W}S<$bF*Qq'
        b'!H$%;-(=sB&A<ks`_8&B0wZ3u5A*&A5*&)hbjhVkEdix)!^%*xw)(W^n<kfWS;rNE{-c;LqawzMkqXfjN3W-3vx<q4r$oDPS!rBG'
        b'7B#d&Wv7iBuZ0I}cNj0(RjG-#ase6D6Gt~>cOik3!sy3DMxD~e77OMLXn__Gm46P?WwMJfd@P3fKl=zO1Ntu#k~PGL8OvKGz&^Fh'
        b'aKny^oB{)4s+@~qnfgoRs+?rhg(2jsX*9-hgb|UG0lSo_G6$P;kmcS*COp8U8nh+ySta>Q)WG5d?S_cb!-tT|&VzWwhWm>?Z90>r'
        b'thtr58-%&WmyW*H6e?q;ot}>6WFgfHX5wgH(|~{(zPM#46PTH3fQu8dzpj}lO)umnuQS+2n}9LqCz2@2P(u?k+RZFv2t&3A^lv;@'
        b'W0AO?#I`^|OJDah6D>HlYu~<=eHdUwY&d7DY3d~gq6;g^$1_FPo?+ExMB+E*xk5+-YuMCi`>$p%I<S4w)Hh|a+GJsO4DHR9Ofl9p'
        b'=k}YE-|{&@CzMME>c4%{%odsnqr4`vVbcFioDjZuE|hz)=6~NKH>(6M`PumtvX}I7pUHiM%%c=$mB}r74A#OkUDy#vM`2h(j_2_v'
        b'Xw{=&<U1CoD0Y(d*0I$)ayqS*{}Ojb)<-5cT=dj5OKRV3970^p8W;xpeUR{9ZDr<q74`Dh8`zU_%12PUn`3-(8BfUEJ500AGw(!F'
        b'>`$#JaiKWix}k;6xSJ!B@wIsZtJ&tc*jg`7kvDMRG4~QpYTJ2GF0(<styx#N#*~{|{(W({@6+h{K`0s+#vobU1q(4&9lw&Nu&Vjz'
        b'pg|%W4~%S5R{~D<&3CM}88Hq{#i-rSQ_{6ZX>N|U>U8B+l2IJd43iimuY~1{_r7!R&eQd(>W0&YRP~y}4Fi!>@}BbtBd^Rk>s?x7'
        b'4KI$q@<;LZJlNiBHJQqL31eap>EvYWolTvIJU8EexOGP~&sot&f68{S)$W>)%<5WR<P-|+0M`F%>u@{c5%(ZZuvC+RRW(_oEw1?-'
        b'G(q2;QYiR8k<pC&OJvBYSmZo1(5KgH(6JW7kUA^6Q9AolFB$ygJJ5$=Ih=9gq|c9R0(sMV(PSrNv(Ba3uJ7?BZmf!B2MEgamTurZ'
        b'RX{iihc*1<5;wk2N*O0m&r^PZcrMESSd-*!U9By^!Y<u;PE%u*oRxde)MSVK!okc+=c>_nJ1(B*Dbx_A_d&&H7M5t{h;vRmrJYAv'
        b'{CGNbZ{>8%{Lvmxf7camet<k^_(pt0q1|xPn+j@F%&f^9B!;}lT1{O;jHcr?LTAz4Md}0!RIjjoIvjOd3co7#SAf>iXH++>zT(n&'
        b'e&2c;L_8yic<8E@WX1!Qdvh}0=7X)e-16-08HqY=JO0FfHx;dH<sw>E`83SK1430V?b+Ql>DU~AYh?_h82?dpDsK6gwHg&A_D!~q'
        b'Jp;n4!@|15uX_H3mXAxkx5kcqGZ3Jc9OC!8-RKMTA>(#9K-bOZ^wW{Y$waI1mGFF_YGi3(ZR{-9Oygp1o!R&Sw{9V)r@3`$oSxv;'
        b'{mPietuq<hxOM5qI&R%PZ1o=d{#zV(Pq-x$C$W>#{HzvFHA0mW+<<uQz;@<gz<#}iy}I&mqVX&fhaLj4vs<%?q|Dd-39W;~uuxzZ'
        b'C{GbWd?^Sed-9jx&2caQbiok?1&h_L`NfDlKRUjW-Vo$rt=Y2V7o%CSwPvj`5%f$}Y)P5PsL@><=kgg(TyNRxBhhq)=I<mQBb!O*'
        b'(+ce;w+1-O_VAu3#FmnHV&oxA`^L1AIRw1~E4df>o&`CGrw(mBPmHXV9*%x3dcJA#3AjsMx~oLz$}a7Vc(`Ve@T4O=x5<)sGeu`x'
        b'yffF=Q$?p+%4WI}e>L`U(dRA6yYbSQu64i4dw5UHTB|I;Nrs?rTl{bCv8=OL60K4=k$bhvvG7wUi(zh!237e-OA6`ut9Ve6y)b#t'
        b'Tw~5sOHE?-!j#PH93!>WH_e#oN{%xUg@x1@VU#uCo(Iva*5gdfgOR<+jX*D9=n}P0Ut(zbFOnmSkrs;))2{u|N@_Jfq7$PC3-*c!'
        b'aqYr?S?&Iz7Rx$w@W8cRBKVegpTc?JpWdGbL3&(=K6MX@*rpEMID&`y5412*hF7mK@+ytY{LLPoY;v0@$EzaL2!=#$HRj*nf`Wnd'
        b'Ut=P7Yc%FB_P{(^$fn(z2u5SFnoPT>`yw47u{R<Z6tx>}Fj4;YmXQkxNA1fO`~hf;d;W?>Q@J<%oynp@-&r*pCLZ?q_-Wv5H5>XH'
        b'TY#y&Ax_%AhXrObcmavl!(Z2eUO1swPzzKHG2SjF$I&6ya6?31XsAj5W&-jXsSDKwN2L&_DDOUk*W&>a$K=O&64PG8ZSOZS@zTY@'
        b'IgA`T_`&!PW!1yc*Gm+uE&`m4zKQWc$}usy&)K#;w{Olhg**d|wQo1_pWp#`f-gl6f_@~haY??UC*yN&Xkj!KJ7z9xLEofFbKM@;'
        b'r_$v<ntiR&&T%NrI@$c$2e#HmKKfH_0nT%JDR|)w#N&PpM1MMnY?>U$O3V$xT-m})7XxA<J<D6_M<wScQ{Sb9MhoZAZb!jfk%uA@'
        b'PVW|Ec+P2I<QemH?owTRK{L&dUUR=xw=;66LFL{tge2eXp;vcAuci#d#m-lE%9xkzZ!cO^|AGHLXf~*LU(WPy*~!MAZ)W(>tL~P%'
        b'<2zKlyhF#msu#S~FYH+OZR)$Hc1{l*v)U{z{&_76D6_fcT@wC0%q)mn5YI$;UTQ?EW^7qB20wi0hsV=s<jtuqZcv<vQ|z8*_YT{n'
        b')3~ITOWCR&B%rlavje>?p5*Cwv~Z=G$@>wya_w*gyRMPvq7g7n3v<Uo`DhHxY$%?YHq<z@>x=Ejca@)rZb9<RgV;Nb*|l<%4#kb8'
        b'bjlAbQq+IzOQCnw*>)d6D~5E^Qmh^&L$R;Np??D@kx8ldqi?d2lwU+gczrCH6V)K+I1O_3ey#bSqG^xkS~H_2<xxI4P)Mq-LB|lj'
        b'Y>a$>Nl{GNW$I%`zLor${?N>n))VN{oKf#N-|YXP`JjAQSTx|GJ+sl2kObkikoHKDpmuBqK^<1Pq7#{8mrCYXjQy+`#G~8qzu8mG'
        b'ObXP28b{9e|D!qNS~TW~LV)UBp5x6V0m7LV;1Hmm?6CMhXlAUWodP)M8eul7*O|}0GYJy1X%wsPo}-xgLL*3w5g_?C<F+@Oi;gsV'
        b'-e@)=-KSJ-j7ff(sN9VkDJL-<8OA{odkQOl<8mjZtzO5)G3#B-pu+#xJxq^h9Cg9=H<wcR1O~!><z~$DOXFsFM#MLS<1s85#Q#UJ'
        b'iu3N5ls-E~($n)UH27ESSseiMNL$qEuRM1m06eK+k~eKr=H^VK(KARqN`p_=R;4bd8B9NsVOW!ww}(m2T{7{MI)ji@uV$DXg(-JU'
        b'MsT9|4t?iI&lUtGDaT->O7$EUQ@B=Uv{Y=>B~pc)&P5`A0doDO5~VIl2Qo5S)f~3vx?sYeL#ytCDc)7?Y;YDm-ON7S{0UV+8wqmS'
        b'jFcx*4D3_Qq)n#5Wh5ahI^2Naak)to4Ief9g|yM=n;S;BifEFUt|4ZSHe8S6j8=!wVN!R}SoH^bV%m;c&*RM+8>zR+HH0G9IN|AR'
        b'SWYk`5p`a@7?){m)ccV;aJ`LqmM*!2p#O%YO`C4Aq-uY-E9rj1@fnt@j5DFT4+Pzd>2X;aj$<-~NgcP`Htl2)12d__6_WeE2AG58'
        b'_%scUqmOB_iT5L#>5KFyN7Ha@F;3{x6lpdrgOt?XFELYM++v(kQt0Q%7Z_%n82M5hZ@xV8yvRgswqql8BIZeN-X`BR>nVBQo#^)}'
        b'56T0_emVYz>QLOk=r2`TV#I=Z9VD$j9#VC#575zMRwPN!2xOVaEID9>$xrb`5@LH1Vx3!a6%&D^7$DEiZvshiP^0tpfHo?yDmFmR'
        b'3}oFCD)Az#Tp(*+ASrf-rL%)k1WIB9C2{^cnmsQe5T1t`I`es#atDV9CRK7IBD{pI6a%N$S}Bs423v)+gR+t8+kX|gmjI%3Fnkj2'
        b'uA<z#%K5DMJq??+jDLG$)i?5iB(>*{2yVcob`*#^qmbjC&`9xhu5%z9#DY)KGI8$4I$zd&Iu|nXZZ_r0!k+{QjGfTi6&m|Ax=?&d'
        b'oo1h&T>2>d!psvPN@JUzW@8rH6o#Fbb2m(sQiU`k<|koxT&i5;zHxdQ&Md|iTd)n7Ar7mW$l%v(w@+8fAKijw!Zu-&fxe$oGga6s'
        b'MB|1_oQuFZPi_LC1y*J;!VUTe6e$ePT@Dm6h99`jlK>8Y0%-b6C^unoox{vM8CWW5pHZeBxd-J*UFDTGX7D+faU%Em2{)IDF3V!M'
        b'o6wjtP0F|oRjS55L&}Wl9L8jG80{A2pL5aW!|55yH5&VLI#C1+_4XNnqTW7TXUfTFn=pLMbq-g~mOk(#InIi}=cYkj(#|+yL{C8@'
        b'rkuzvoha1&e}ugaTvONiIDT?-6OwS%1TbR2F84wpAan%V@>08zh~cH$0j&sVHxe5}S~sP%T4%T1U_%l?lFM6y_PZo46_`v&U&I$S'
        b'pe<U3@07M1wRWR+tkl}hQneIc?(du%)NbE>{{PR1Pq_Eo^YWZ?p7WgNIp=vPQ)<gV#2kcfBplF1chmEO>8p6WEY!4S6Hfq<JWGy{'
        b'{G*|JI37Na<3R+Uc0pW6ST5AFDL^t7V$Eh@Ey~4ZwLHE#cuJGSn)fKO-kf{S2kYrXR0mc`^E|;T=WrhX<q+cjQ@)8INOoYw!Us?v'
        b';35G^I`JOZ;HkM<9<DT$m5Uw)@;NyFkgp5p;W0dsG+O~EiKh=%pDoD>%zfd54P?DKM^C$hZSZ*_m~$)y);<l}arX(MSg?sFlnN0Z'
        b'jXVPC#b1QgM?<`Ylq&6?A-3&C(S!20M8@RE>IG}uazsj3f$C)WsSN&tCGwDk{cHUcA1pub{rw=wJP(_M6Y!o7_6*_#eFn7}6N16+'
        b'KysRe<)8BP2;l&lx^6+-fNL-Y3kTTp=cUUlakw0fiG=*E(4FV`y6|cf0V{x6CxrlJ?RpM^vwH_5n#NTUq^Pfj0#zbx3ZnMZuP9g('
        b'D8IBb73M5&8}yhU?iGtge!gT$)h;3;t6S+`CDCkh-#L(%reYxeGYR}9Vv*Vu+VJUw1GPL15=5m9qAsY_Vkv6H$Vaz<duz4N?A#%('
        b'_&hWQ3sr)|7%U9_A{~Dr1VcZ{8cN(-#0A2+kuz-NCH`vBmJeYEkUxzW3|qwmAmqF<Rsyli(}%j`pMynXw2=N0bS)a6?ZN{EWpn%x'
        b'0H+EFkn_|IBh`<?wOSpz2E2CZRG7ODb}WWlQgGgOz$v&Nj7Je`LbkmqE&g1x3X}3N8L>>6l|Q~(P23lHVU<pL_BXZFs}okO7M%NP'
        b'|IP&m(=dGum|jLKIrvA>L^2V7aDYdofhAeM;{zdCUa!kzf_uOVZ}L~;KzP3EK?v@9ErsXz7l6c_NI`z*5^i6YydVgFbdk}>=M>;D'
        b'eZ*~J6tTHN=KI<M89+4UDi5dJu&^-P4apPdwI~YR=?Bl9B-WP^MPIG9egywpFR}p6E1^@yN$VLRObJQKDv9s_n}C}hz9zhNYhKp%'
        b'qhYdmcayi<>LdcPe?LWq-Z>YF_ozj8c+o@q)x-5V3VR5hAAjgZ79#@6%UW-+s*G#$OqP-?=HdaPa}vA<8HwkFiQsMv8Fy!HQ!-v}'
        b'8Q{}TqsB%dFBR1tMOp9g;hKN8X;(u8!l-ajJT3^vopPOU6X=SWT8am~yDQ`I0xG5G@NWxjQYR9~xeLouyzoj}Fq`c`n1v`M@|9h+'
        b'h{;x|>vh4%)~VqlGTEI%N#&_?$hI4``CeNz9&9oP6H;DIN741W|7<fBwfW37*yP|3oBZHjld=Eaq`YW8nl`LBnva^)aZPe<9%@Va'
        b'zinFnv(30*Ke<pMKWy}^dyU5Z_kO~Plm4SkvayX2F;o(nzu&2@otI-AT-pny{s(C<acRFHb@$SC&rPkkY%5FVt~*gYb9Ir03PV0m'
        b'@5Kf)o#m4c?MHUTBJZ7YL*;Fj!@!>eT$=sfekqg(dzmKlQJL3SgS_P1q|7sbSZZdPfL-QOxtXLj^9~W7Sz|hLV;&wun}zy~JQDMf'
        b'`vYEV>g0D8Y7vT&{uFmc^qb)Czr#W(rrw#Iw^b%2s(a6hsXzZ9{q8edRZxEGI6v!6RNmpkQM~NISwb>3I*Tj`rzU0zBJj#@2M;Mt'
        b'uiq&*>;*8%@8zok!J<D%!=`%wBMlbqID9v)-e~bF2}d0k4$I5m2h`i_$_dE5_}{)|dgk)HD~pFdMYgf2Cz>GjulLJe0u~>i@`~yN'
        b'2?W-|hX4)fDXreL?s6(mpDY>umZsZ~cahZx-&{a>L*XZir{^kyyn68zinR&x!*u)xXLyTVk?cK<$`qb%htC57(}FP5Q<wc(eQ`Uo'
        b'*W{asu;SCVVfDo^H}2X|5z(BU-Ss>6-~_?FUkko}3gi~R`1lsDs0~viw-pjq|BcI;q^OP9rKXU<7LQP<j@-C#n#AuU1wH2=$3`&s'
        b'%301MIm%{wcve5la^uDLc!aGDi-012QeInRLR|*zWDJoQAE_kLQRyUOd}K<JKi>T>^4m5)2E33*EV-?R42q&-@CNxstKTc0SEBh@'
        b'kk|qJH*B<IBp9FIQ*;tx`tyx|mj@qIX|s3zP@A%O^XIY#K)TWDvxMPh7rvx&H9gtZ!|P91*;Nb=BO<}lEMW67*q+W|PP*G;@!A{~'
        b'W;jJX-X%(i>`YK+bg2{4eb?IHVxW85=Fij_-5&k?-5c!kt$R4yar4e|55MC?@Yw(~2U>&I+OFr?Rz?QI?zrO*dA(OxsyAP{Kdov3'
        b'ZE58~K0HB8ggm`0S{-sJ@=*24^twwj&F)sB#2<bxq)Nz$iTW*fMxBYN)VMuq_OJCfSo+yk*Zppb`Y|W6)?A=!m`R$J=ieH+iU!Fa'
        b'gJN>h@$R5YSoz$oqzV1kEa#t$z{hxx_UR0~sr#-HRE{D6IhaljItJ^wkK*%i<jP#CC^WSesOF%+^gIv(b9*vw=g*I=JRF1Qf{u&k'
        b'*wOQyyw-N)pxgA;cc|YG7f*aQa+6gJf7inwnd5ZE%39$t`qdiM*WdZQIK2^#r*nQk)3y?Jzj_Ukeo(x)L42K((vP+JR<v2vQe<N('
        b'x{Gm$#^knIC`;W=8H%kc<_<MP?f({Il)Fz@GZP;fy)iXDa`_s#{@UCN=}b7#m?ct_GmVkAJj<?-54Fy_#>Li8|BL+I180@g+)X<&'
        b'{V{pXqrb+T8!T<*f}Dra39Y_wJQg*Ii%Nx^TVf0)V_SV+dH$n)hzlQo$zZ&V>h!WYkIWJiCeOuaMXT>0^JOg<Z;dYAEu~^)^?owE'
        b')%SPLzsFdGZ7yu}o%h@eBRhfE2vyAuTb10#C49&UUH7%Zg0@QExMwsH{@jU6sRi2GEpT$ESW8`XLU9vNjou-cRP4IZA_CK+vxccC'
        b'IQ#Nlw_zGAS-k5uk*dEQ^t)4EZSmFmA^pN+#W84+ncO#ecmsSBnC;=CIYv|e%#BnpfP11hrl|)T`5ui`1+|zqqPZn!TZl4s>Roz4'
        b'*ouuTkvR2-Tl6<AM7|AOi!@*y`+@KYQeiotH^A%RPkqRaR`v5*mxGQCvv=1rY)<|x52D=E`|M~p{QNW+lfVVIj>}^4Mw%%p1h;tR'
        b'HryTtu#T<Y^<Z~+n@2FEvZkIP54ON*B#M?)rqYG2u=xv@&{py;3rA*j7i_ra+hoas?o=<E#z+Ya9d6S(C?Awj6(4XDqp59$B&}F<'
        b'+vLARCvh|I#}=hu$@PZe6ZJ1x_yuOWv~KAiRZq;w9XE)6LSb3uHvR6F@L$3ED96-2TAcp_x}0dbcK2D)arN%AWa?XXo|fDlgO0a<'
        b'I0mZK|9uQhPyS#G=rx|Z_P}JGhgiy;V20W%M7(8Ju23>3@>*IWyuq#2U$ywvT>P-yR__~##bF}xXKoH2mkoNPkQ+b=CG*MN<M{C5'
        b'-#Y*6rw%-D_)p$$S+7Ux?LwdYC3kImAg?J82nm68F|dUVnq*bB+;sUKoDqqL{DWe#UyZJp*Gf*5F*r!d-=5!caH)ccUxDoI!>YD)'
        b'3YmBfeD*Ez7~zBPZs2rZghv;T!ed9R(_tXzL4W-wHKmn$av0})-xnap94WSc$I_vmPEou9C!*k-%=<a$!S?ng7)&>&Z3c=b8a+md'
        b'c%uQ$>X!8Ic^{p?5Z@A2qKnhKD9F<iQELU!2R7b%S)$zE<aE~5zsC%}?Y*RQe%UnXthwA(eUe9=M3zESHYg78`>wcA=xw`!{zD5o'
        b'TsB-jzoB!g6i%OYnvEL{XNI|O&?^OJDJh%{SSTtxY6lepgrBof*+@fR<;Oh&+S<ZJ>8Q`7@<CKS`H_1ka>`K%^Gz4V|782l_~OrR'
        b'tF>v&W8{*SYAW&2k@_b>vseDLIvY?_BHe^a7rd$D%pvQag3?De(7nT}_Od&|FzX0QJ5UC>gh$)ZL$!}jSavut;UG(3XxHcwPzIjq'
        b'__y&2Os|5w#>i3DR;XSw=$5rJ{o)>h$3VY;3c3yT?bC%(Uw=_JGQp`^w)n*&N+hV)ExCkQ?+4S`wEF~UmoQ;6;GB^wmH4QUP-G?6'
        b'%8fT|S}K8;=9bf&TR4Af9I%X+Z43K7a!gAbP%;yzNv+U$4BTh80cNPs1Pva^BhAQqGAwA9gpGX2!oAHj@U8sPRe3Y7h{V@iOk0fU'
        b'_ae)J0UUTQnF2RZz3{atP6OZ9hcAXz6QLb(a6^-?n=Go(jBqa7pTr@ZTQg(b&91qq|8>wFf<E2S!wYamXC}UiZfIsikwi&cLMY@j'
        b'pePk&H0rR$WKD|&+f#qaH`zjnAj3iLZ@Cwr*W7H0Y^|#lAmg$>T%$XiE$RsFQq}JRw5#QgjY8q`&BQyqNAhbsMFCYTketq{Hlwqb'
        b'H=5BgUWo3Un?>(VZf^ctaGlX0L7P#y#gLU%Q{b(6>jB~X21EX;Ih-dfz=HDV7Xv&~%niBXHi7)J*F`LyWMq?_vUZo(XXcCXa0#G>'
        b'c__SV9&S0stDr9Md4g~r4nQL1<>|aY%F9PW`kzQtrv%x$fY`TDECS@$@F5@QD{X-rh|VB_qzp20e4Yq?L>|dRZDF#>qq1Xtu(j||'
        b'(CrJ)$D?e_d%OzuKl~&fAO&Ms*5uqLeABmg=pp@CbMRhSL$*}pqw5AsjBNe%B8{%u_jXHaOxQrsHr~Q_$47og{}ttqn=@JXg5p^L'
        b'!}n0D-0>dFvdY7FBjDV`XUOPKH*$>RbOj??AkRoq{^9F{*t@?L#YTlP&MJY$2fTZmdPGyYTNeI-(cDzNyW(}X=BLe&lBC9<D@Q$)'
        b'-KkX`>*V}By^ja?#yV^%is1YU)|;s;J`bjTa*O`9*)Q_c??OG|cq#h+W++tz_2!XujbzU0HZ}hcMSkAKY1$Uou%x6pc+X;?(mR8<'
        b'QQ>)rJJ$RiWep=Q+{+5?WQ_s3O~7J|4&Ih%{?bN<H|zM|06y+TG0T19ZNpyP*#Q)eQ+pOlZYy%!A=*E;<>ETy3eJ906VXDg`kef-'
        b'Db*_qY8|Cjh3m$V|K2oQf|OiOH?Il3=L^tum8A#U<`qBDTz%IR9o*>War{_YN^gxt4df+Y-pAl@lSLg8d^Mf9qq9!;wL$Di5RJa?'
        b'>w+*wB75OCn^5*cu=e_rd1Iv@pVQgaH`EM8CDs43n%CMad@S`;#AK69<7u9>$($?9jy-%nFC1>-;hgD^Yyj)Q`MGfKGf^|%)Y_C_'
        b'WFu~^aQ^#59W!&9rZyc3T(;&sey%JpJeSOi(KfbOaBQ+fR`$5%R0LlD(4CzfvdhS4@@i1{n>LF898lB8np`wwTs56yVi}UP5V8gk'
        b'pKOYnDK495@L)}l#fCMQYt6y05F*pk8TqAK6s*Ol-QK3@Y$BGW#%Mb6u>}N*fhGKgMR)o^xy}cAcpZDMT4W1}rBHb3;aLh7s{X|u'
        b'I8Fbu$+ojXozTOZnqlkDcWk*fRdcoPg=XK2&8icutGq3EJDLYvKW~G-$mX}S&9}bI5(-@F+Ym&j&1Soq578%-$6tebY4$)O0365o'
        b'k3uO=wP=P|%Be(}y*0wm*?Cx|ELSNAOLz*U)U0l!3KtgfF>QMD<V&)mcOxd($;h9yl|8{1@EjJ%;bE||9g-P&=7PdiO%~Of&nqib'
        b'zqlsPCrnjW`yOld6*ZgsSn|2%z~YU5EJ>Am$$yybi2E`i0jKiE7ngUIO|{(&sMe5OP0Hia;*UjsKBfx!lHy~U__j&TLobG`g`_|d'
        b'lu-CO(7~S(E`_oaA9BoX$fdEr-3`ea>=!}`5Xta)|2Gx0e#E*(osk~Qt+u5jB|eB<U15`M8N>iI{d?ftw==L2h`szgV7m29asIca'
        b'qHFT=ypAWY_C+=Ol+9DGvgEB+-*>G63ZT&Ie1ylTIJ!M<3Z-yJBzP%k@2mNN-7`JgI>5IfA~~;aM5i`eL=jM6pl4bk7gt|Re%*?g'
        b'ih18R^xv9-9M_UB2wKq;oq1=?xh}Q_#26#mbENdjnf?AVocCtr(7D@oN^Da@p4&V+XqvmEzsk{_zJE3OK4|UmupJi>Pi#8E(!wUB'
        b'E03_aewhA(@r}XtDkYZR(J$liG$XA^v*~>Ks&MTeThkxUeS#3BHDmfbpn1EsKNSjsOl;wM46&o~xe9q`HJq6xS>So!wrw@qz9x(J'
        b'eg-dawn^KTU?VF5{UsCkkc?5U*xu8+W2wk@sI|Is1ycox5Mrru<W^5ec~{d`i7(J<%m+Oo7Q<r35Yh45o4&UhW8$)&5Xk*m$i;?('
        b't#I|Bkg|HfkP%x$c0>}k=bT%Vp|-cuv2B}`+nZa<%W-24Fzj#L{(4i7a3G|^!9pA&LZ>cXf-?+J2TiUOu7MtI*UJSqp<8Y-NNsVI'
        b'4>2fceVEY@-tqWVqiiAL<soI2!i5lz4ffXfof->XU^d5A>{JJaQv6;CqX!*5bGbvdb2@`G_fv~OrZa>gaq12Ba$+>+vk>wEdH@^#'
        b'55#iu^Q2Ic*9n3A0kM$}iXe_w$f~q(IfdiWGA$pMYPYmj?THZqDF)GXeHnV>Jh-e$g|)4aWfo>Wz!ylv`9Z5m0<JxrzY0u^e<RPF'
        b'or=F^T5;94qiG<72siCwQ+1zfwlltUO;n6D@G4SKni{-Hh(`XxRy`H22W3wT@F10iq;BeezbQWdz5Xnl{#->&e-F=eh(*4mk-y^A'
        b't&;(nYb|rkfz)`#p~2CkA8HyF6~u4U_72NVdo+bixOfpVA4hjd$;@yx#7L*x94_YF)sdx!Bhf-uhhsr6{uq$X9qSIy=k}2yz>Ta('
        b'<(`9$KYW+)K&nF~v>LrUxH9C`=zvJ|KkQbChHNE&)C%`Kq##_B4~LD=@e#?s_m1fI!d4xmys_GRhL*MJVl|y2j(#I++tCW-i^U3e'
        b'Cq%ra{`igj{B1a013WZUItR@c5s;>31Jl4a+Jy`e%E!e=xAV0ipvAXJjwq6f1mMWxIQnKw;R=RWR-}S;k1arM$Gmt!nT*yp`DF{u'
        b'-O_??rN3|?L`2h<to*H60!<gz(KZvOKygv}%9~-^zhGg*u$nun(glkVnJbE2Q}DO|j<j45!pB9h>9g<3xYA9iwDr$yfRE81GG~@^'
        b'qneKCM0+Sm4A9Gw54Ix*VaI&Fhnsq{l^K*ScMpAyK>~aTL(Fjk{FD!JU#90-dEj5<w97ZjAmzj5NbCO?WSMcvJO$JORnIqa#a9qS'
        b'2nE_XEM_h1g6RlSq~U|GK@Ww2QxuUn`1asb;F5m&j$Y5W%TGN9S&YjH3zc!;ly6BB{XPPNKIYne)V9;?k<y>JM(vDoEmQe0cL?9x'
        b'0$<Q?<-@MSP`Ch>&l3uN9`I9ZT)vhrvFrCxj7?#TYg`A=TNiv=%v7ehyy)#USZp!f(&82si*GR0R*#7Gw^)o@gK-jlKy$!Fq~<;w'
        b'nteT1q21Gxiyw$3T`dr`>W9f8SM;vn$p+lbwdNKb4&+z)+T*UF+@_*fjh1eKl+_pubo@wSukM}OS^nCNpCPk!j9AtqoS*qbnRb|g'
        b'GoRHhRdO>=KG$MsWO}dxVTYE5+xvp6h1D&5zSu9|tmjX&(L`{dP0zzw#gk@)lkE2MO|U?S=_jmCfYCiJP6?im1J2@H0&!9ovnFem'
        b'K#q&~d=4+NWzj^|sFFkE?K2gMe&n9DBNG*eO-()_D=VTIZps9x65Try+jAIL6{<KV97pRWxFW+>15}A>AEYJUsXn_3_p^4)dYn~#'
        b'{jJZ)3<ymRvf7-M^k<<At9{Ou`u6Q;Rqg}Pij<BfWWU}A@rHj7Z#wL7P0d&k4D)#7+I|Obmfpdevq3-SnJqybtc>~pKVpJsyyWxD'
        b'l4*?0aLvp4OCgqq1MKu&9}_UG9Htehi|(ePz4N!sypOM1Ez<h6BWKXmAWgNv<U}<(CGn84uDT3@EMP3Bl-$Zw2lZp=HH<}Fz!yPD'
        b'NWxW!(sCHh;|$!b3&N3-g>?Q)a9_`2EE7CRlmxKzck}<^zqgP5uzj3sKLxhG=7;T*-#Ss$7d8Ha`drtVA(}~&#nE3UEr|Xd<m(Rp'
        b'gg06O_ZY<O)eVFXpZe3_V9m*&VrNmf5D?W3#jU90!fW&AaIS|DJWjtKGI=Yslds4!k?(Kf6|a9#SzD{Q(CqbI?Ou_}2gLrg<3jQi'
        b'bgTmUK5Fiz%rJ|&d(heKhx6)vwMO-mIr;fpa2ra|nALp!wRu@N=D+uMq!}hF)n*FaK8oY}1>{LoHOG=mOc}7M+eo9AG^?@TjR>ks'
        b'I$syj9;^*=uJhFe?o}6m3@6`!b)mDv2j=7oHdqfu0pa{P{?z(Q^exv9!MazGcfKMx5sX(%`kZwcLNo`CJ2-I01;uEKNF>kY(T&bv'
        b'Y?8DI5n06qmFa%q<AiQ#*0`K^J6XV=i%-w6469*-^j4SCX6{tezj5|5vUVF3?E6n4x&DvNV9WsIr30;$l1o9iP;gP8D<UX%e}{NA'
        b'PQ4NY;knn5PMNved<8`p8dQ3(`cLzMneW0g_=CLZGDj`!v*xL0*lmP+F%U|kDgJes<b<FOAYT<zS2#Ibt8-}@Tz)*s!jCxUUU|mC'
        b'F)f`U`ez7w*bxYRKusX{_aXQ#c#@7E0eg|-j(U{Kyds>B!7hw^!4B{`qUMUbZ&;^TFqtaL)IfH{Iy>)2=qkC|N$Z*u_@RjiQuEdL'
        b'^!uZykwbo*{7JJKqaSI80^zJ%6z^HYL}CX$Vid?`73YNCmOg^cK3xwrNADaECySo9{AhS-NvQ2)X2kH)(t|4(B40s!)sc{nckxGN'
        b'SmwQ10z)2X@Awm>W1E#JS3_52WucY{EGIoj=e;lO0Rj1=W{5q8`<iowPvSlJ%}hGl$x&R$Wc}3dmBM+V70#dsuS4e(Bm|aPh9zXi'
        b'H!t&70De9eRA4WW#J32F6j<8gFQ1fjW?H{uyB-|*jwQuTf*&*wCBi@qI!Cd78^qISE*#o9F0R`eK=h-SUT<)3N}##jgj^aIVfvNe'
        b'y77?;3L9w$*Hf2izC-Eq;RV5miZD$003d&Ykak1^DpE0FGpNvE)@GndcfkzE5C{1;)_VY9i%*wT7_kusR8*fKWiAUQ64n92jbe>8'
        b'feL1nBwXsSI9O#Hu<qsJ!eQ3^AU^#uE{L492|g~b@MHQ0fI`XHph&$kfx;s0cx<Zc!Ysqdls`Jr21KWY3ju)ww~g39TmZ9v%#v3j'
        b'c?;J=Au~D`r8{7CifA>e`6ZzFQ)6^G7d;uXo?*E~7F~&Qy##Y%LJRT^yXq1pL8hVBr-1dBT=Yy-ScpQm{W2OsC`6If^wDS_^=9}O'
        b'8IAg;|22s2M6pedvE=(s3d<Ef0W_~PMxWxEYl@ygZT^8JN1aqyED8>@28<K~kYqzMu>)Km#`Mnu|L~_%gDgaO#P7hC(bVaiVH?k^'
        b'EI~c6!pG#5Txh-*!OC0|bnSO6-S5;GoRm5ZZY!`c8_KCa#lrmxX}_(k48pl`Ckmmmk0oDf)U0z_C=1NGeijq{k)<ePkRhM>8sapN'
        b'oVOljSE9a+?17D`S90^V3sRm;)PY(kVmJD!9Js<DF3694iOf9z5CIp!$_WHu9SY(%QVX~UdLz{=S=HD%PG)eKFHIw-rcX7&HiASB'
        b'!cN*DC=bCcPk4YOtxg-dVIuc9A)hoq+myFE(I$il{u?-^qRWiN?i6lf0r_kAD%Rg%$(>FMCg$v+$>*KwFza=etbzaIs1L~OM&aWq'
        b'eVbFQE7sja9yQ6W9Co1a2UD?^)QX^jJA8?OFDPW3305Z&LNqeM1|-7IU`7>n$tE$IaqEY${F6>wz)a)Tah5EDk7!pROVE_oUBrYF'
        b'tneayf5OSfQbsnT;GFke;!AL$iS<P{5$?op|LF;cT)t(E@#)k&3BTFcZi5tjVdKA3@W&d_2{xvBnYI3!JDdIq1iZjjq}Q?JN;qZ('
        b'WO8F?iMkq@h_s_<m@vyjPR-xp<fOrjaB|f}C?J%cC1V=Z)o3Fn1x+?A$~N)}%8NH@K4=VL!RA@ax)Nalkyz~i`$z^$-rT1doBz0D'
        b'7Slh7KFViC35E4}mOk4^iHHkD<fr>IU+!b5N)ltxo@B@L%UNQ^A}Y|3PP0Xd(jqb8|FBjSYVYkv3sxX}i6z;6He)cVDHmr#wUdP-'
        b'vhnJR5<*T0a+o}wgqKxZyH<eQ%ZuuoA0)^3CGd+vz{Z*QmaLUC)G&LcNTyt8Hb6dqoveJFxnIx|LRX>Tx{%qqc&eA};s<S!)(VvR'
        b'S~%6k%uVt%Q-Y0zK{);hAINu^23(C1O9^5t;p|LNZfWvXNad|JZP<GEeFGtn`aQh&Wc0d5&UE9HY_y$^iQ)dxAk=@$s{LE>k(+GE'
        b'gL2aiuIWcnw&L@*I~POrhTL_qUm3iPDpm)3HuH!izIh!b;jO$TpTS`#LqgYGQOW36m@;Y-`4#NPw#B0Zr-Ha9Ivv$jA6DFb>rf{7'
        b'GNZ;08T&E#jZO{rPfgVaI(b~Y7$FaU(LG3(P^Vh2A<vcc+&-8o`r^UV>5VglAU;AsT9_gVY<DoZAzSfe{PMWpn?%$5IEz4e;>`j6'
        b'qke)<m!rB%u~efZtvQa`jP@VCPK<oRS7Pg136zTtLwV$xx3^+yKXM3_@R~Kq`_Uky5bk%>+iZ~mhr8|dY7ym)e@lf4cY}&mn2-V2'
        b'A5X4`!A70}Z>_*ac7Td-On5&apJ6I7<PP<<=m~9q;TYb-pA<r<5XG(7gy|1}>+shBDxUqI<G>Yvq0sBCiPp(aFC{lH%BQ69a?H96'
        b'?Cm4kr_8L}@c^HP0q>=$-(P|K>RwSPiF+Q!!X!eT46(s!ww(H&keIt_z2=(H+->$Id4EdURZNeL1Vnysc*ky5-u`1)ML(+Kn`~y='
        b'WX&hMF#&9{qZ8I>^s<{FX&YztIRGrViboF%SHrfW6{;85(Xym!s}`x3@-QM4!SK%aPfFyD+wfg20p*vJ6@yeFUSTXGmZa4rhHQ=>'
        b';6-P4JjWh5uNL&LPK<+tUGa1-;>f=GW<Y{Gnk|@1mK3+oQYu&~V?fv==rDdiAn_>}(|NWpztOjpnfizoW&mKC`o4JATtSDj<F_&1'
        b'T}rg&0R+K6z8Sg9qQC_4OSYo&s^?-L$<6AW^NAVNU)a8kMxTi3_>i@R1E2|EC~tI1wlu9-OD^4)N(oPFLR~XG%^o@rK~0>hVh`n`'
        b'&Qt?$J4C#6#ev5m%s_bwvKZHO67J}<AJhMp1xZFuQ@|UY^VBssvP8aWGb_LJ6|6<E<mxh52jrz8d{7kVFtPHo%cQ1J87n=6!S*su'
        b'PqFgMFJYbl34(c4PqT8xCD;qd?e+7J97k6p%=Pw`dyh+dZ)ElMmIux#QJjaqIqMNNdU(lIY~*h&YOdoKu>OCNXBr@+6qR=%6;=sh'
        b'mn)`xiyP@PsG5;!mORlg?@&YfxwU}>n)ZF#`}R@ci?S#s_4pz^x|4~&idna^9G--!%2;{#c?e@QhQpaHFSsfX5fgEn_h7=`un-p&'
        b'suI}WzrhR)CIH(mRTlzc$>ogAAN&l?{Zr8}N2aQnJ&*`9M706)r7JsR+qRo6>w$CIRSPDRt3Rx}ioqRgZ=c^AX?h%X{{xscS_G@w'
        b'w(aT;$e*lXgVB>AJms$`RfTZO<`C+mws_^wD-kzb?d8F0^x7cMkyDRB<o+|v1Y3alk|abPtjyfrv?Bo%rnA<cu^<<VUKKr@6;rEk'
        b'WTSP$ee-847K|sK7C;uux7&rZwPi|EfQ5;gUp7G6KALO6Ft~5~o<koY)rDV*`(Z2CTk3^@Fut$G1wv6+2-RWu39Cq#!VCv0QFXsU'
        b'B|3Vzdm9VnDUj<rDh!IFr}eXU{qJc@T?GX-xp)P>QTvpu5+7~#dtarC8aT7qQ}~H`!`234+>h&viO@Aw=qlgq?!=*NQ$C`k(;GP3'
        b'SYmX5U*2t|A7}_N)oPrti!IVMt8s!)M9hcdys}4@Z*#42LGfa5uEXA*U8zPFkla~;ON~`vv1GRE6n5YMUD#kz|G2&cwzmsakI}{Z'
        b'I3**_vgZn7S6rD~HELK5bxO_I8=!jPU2ZH+EWLt!z`9ah+!c^oz3d8kKWspM3+Ybu-RC0eZBSTa;OrgZ5n`vZrY>oTE6f#T>k?ma'
        b'%j}^JyDKJGwktAtrz>-*1+6;1M(k4aZ!(nvZItUuoU97%Dv7b3RB^XREg*!URDxhLMIZpx=u5USmbZnUF5rUAD}OA2z#G1Is)aq+'
        b'<#q$hJ;)U|+!7l<x4X_GwFwWpGxLPWIIY;nh2lz<^xz}cSuR6nokxZ;MC1vxVwH5*y&NcRU0$knj?MFP_S%4wG}nizEMHU#eh4EW'
        b'q;XVe3#I>n)0w*9RAW(8@SNhkdLqL@ts!)f_cABc-o59z=w#qtn1@_x0Qz#h>m#RMy|zp2`ozgpt~LGR&V68!7rByzo2QBoimNaS'
        b'4i21B+6K2u%%<9Mb4^rs@$@ar@c5ngV$m%mq(UBN-rjeNpY#VJidf)>gd-7WFy7}L(ei+4j+13)PG7JPV6<^`OV0xH?`!pQ?4fk#'
        b'^!OtSoDbKgIBP~d=I%l7{@Na~{QH|xRMhCmS13NZ^$Ob~;*=~Qj$bj#QYw^Zi)H06A(OoAhn-c(nMIbf#!;vJy%WmAx>ztQIyKoO'
        b'v*Cz$PXM+(?Y4jjJ8}Z~)wGECC;PFH7|?rS(Dp=cZ;eOx9xrHZjbdZTt3rYmbG7E~an$uErm9o&pj?^uaHvJCA;ORJ^B%#H`L<n}'
        b'M;nw%JjEtea$3mc>jo2cwKtz#C!-{|PK;HVCM#t5x~d&ew2a6Clus9*ltoE(3Mne}09PtTNtH?0N|4jO+~(qUu0j@xv*&g~KF%$I'
        b'*q73;JiAxc%b6b@v-Q<D5iak|hy6L#!ygk&ekQYt>zHVp{gQ25g#Gp5FxbB%>BQONgX%okIqtsL?J2h33fg1S;L5NpWmNeUes+zl'
        b'R5tj;AOyDoJG~Ba=qL_Zk#Qk-nV+gk0>Z466jw?LP6#(c*5eUS_=IySzgh(*OJ$uQ2P2Un)>#)=2+F$0CD>n&V<Wl1FX10KhFSHX'
        b'ay@LnM{L)4w8IAMqCtQl5rVA}o5rm@MNSvWs}^<c`uq|md>9O751!4Ioz9-jmW?k2`Tl^n_t-IFF<6!b*7+tv&#qIJhQel^<VV4V'
        b'P9AyrSNW^+DG2=Ca#v-L?A`C2yQ=fPk^eJ44h}w8pst(DkY!S^9ED-0WJ)+1IS_^~3cn|vT}T;6T{m5rAWX%<EJ-Z{xx7r4`q`<;'
        b'SeZ7;NyrmpLs#i^Z=^m3kO$JJb=FDNkG&W0vVPsEBZ}0CA0K$+N{5U%P<E_`zy1W~fA@NCx7quN*?CmiBN`K+Zljh=pRu#BuWqeP'
        b'6SXdivO?LEkne0O{`^b*7eQQB7Sw3jM)Fo8l0UJ62h5c3kaC4Nl@HWvc>s5dinrj5TI3fC53YEG5r?E@q<LQ%<SYh}mMN#FgN{AQ'
        b'=-Is%b=ZMQA_|0Of#bf^SX0Vz>FCp0gL7Q$nq^mP?qc^Gfd%oa@M5EOvJsi^e~8)eM32r_lkd@qk)D`4@<dmqs6zfwzs(;iJov!<'
        b'fzXhght=L!2UA{GqBg~VzQ8pWS)}@F&W8lxpC1sScCb6`bl$jQ`%j;2yyBO+MS~WZm&4$0oA2#L?nDnZm0~mdMW-OKDG<!rG7d$a'
        b'5}#z2P1uJQU?(#dk1yaKd}PreBnRFaSo^#;4v5Jaw|38r+?=ofaHF!frc*@!p^@>S<G^FKcAG^6X;9V&O82e<Urb9X?o-S<E-u18'
        b'PY;_}#IO4)G1)m7>;|f@v%R?L*8G|~(1?6Xw?+PFa)qo@6yF}!X{$dUkbwHVncaQ~uiN8v*1+DWZzqfI(o|RDn7}5=>aF2|WN><e'
        b'I^VN74D#0#{{W%$Rio!*?(PB(GJLT<4|6=1!(84@H)?;rmx}*OQS2t=3hDar^N?vPcszwF1e6vtdO?V(oUYvK`*q`hkWz2xxJVIE'
        b'W0D@E0V1!$ZSC?%-0dJM8<ZaD%`E|iG+BJ`X<2{baQw$79~KYCUm(JcoZuykA*msjQjpb_XMqGC@;FT>57aVR-T-oo992<Js4XwA'
        b'DHeQBmN%w8wMmW1!>;*#&y7HS(ooV^_|RS|u3M)nhY;q3n+PmxRZ0RcK^F4VW3+a!uc#5S4%O-nQxlZ;v@+m@w0bfGoKU#i4}G*V'
        b'F%aiJk`@<;du7MN%AF1(YTL6BFUUYx7WlO<We0>~+lks2Ljzg>ArXTpDod+H@mgZ%$VVDeP305?{Jv^=>Sg2_;V{|@4G%O@aW6wi'
        b'Na<c3WylHNJr56M;AL&Y<x7Ng^j=>wf~g1&*q`sgBmnY!e4_otEg}-N-|vHqgGlP#-2}(&1sM?%9Jx3@8o9Vv;J7t}yeQhX4X@S$'
        b'2sp8A7kokkw%{I^@63|_a`=7ErWy^TtWk{>8<D-JfoLrJ!a>D-2BD->#`q@8YG!p_peqDAEvAe~fzKhvb@YtGCuoG2564dRE*0?d'
        b'AgFL^;n+Fc?I-g39Yf#L51x@;KD0A&JnrMarp1iMUD)x+GGZCpNM1z4x9vi0ZvYQydE;mRUtEBOFk4A#;l5EE_@4Y~U#iKd#{9mT'
        b';_)x7znIr!Nm@gMBFl!a97vV>pZk*54De`nFS_^}bGSa+ce#wbxR0saKvkBJpYEe7H*&uv<RtuE&;6E?e}}(6hX_fCoYWw(RB5kG'
        b'zUy~1X)mFmAFfBj_%7F}eKzrEWtSMOvj(x-U2JE&+#{UMs|{m()dbd-zL4@gTNfZ0-*XW8>yAcoI$Fo~5g4O>Hh$?9M%~Ss`*W8N'
        b'^qcz_^&xrJEk^y>e0+5aEFJbxe0r$GS6vsTnAi95)zpP0T71u;IOJ9bMQzfH09gwk%IR14S=29^DJi;vA%6>#3`h}uH+(SCFT-zt'
        b'5pp&aDB5x|I(p0?z92+x%rdgZVOhnqP-`JiWmyH;?{+hdV*1%q?BNX<r&oYct9WFU1Lbj`fO5fv3NFEVr%)X}^35GNVfY*3Xb(n&'
        b')g9##NN2h(L&<mnvx?^`aWEh881dojwlK4~28gnpW>>Ib&KJw+X+m^8^K&Sc--&CZ{q?>9$fR?6UO3P^xHpx*U;aAe*E4t-veZI6'
        b'RV&e$_Q5q{jOi|-%FDB*<?Ez6BYgc#M{O!HmKRaRJBgcgG0zqmjidk2#T+VrVgYH|hmczi>DT+14!6jkx~+SMg;-|LI($X@kSA?7'
        b'RTQ@YA}}%s;zE#~xK!DG;x)IUGtv1g+^FRlWBi*lR~TbnIrvaAA@@_|2#c*gWVI|Yzt-ezituZJM^@RwUBja=p`qCo_{&f#g=BDm'
        b'XVij@f3n4wZgr{#c&5wjR!MOpd?qFirk^nxC@AzEIBy9nA(omQ(gC6QXp<$Z6p|Hlx753(c8d&cwl-DtKR3HyCgfXWNZ13q_xU=!'
        b'LXOXbX2Y)dsC@&tVS&R`4{0py3rA)l&BzqE+leSRNC@6DKKXn2W+Kn#D3sI}*rYe7jg;|8(PkpNGI2cS<G(%>+Pgs+h`F%&IA$(U'
        b'2B=L11$gfXX^~b$5X9o%jkQHu@!meTOi|zJ^<6C3ePi%=N;#xN1YD-3zs;f>6m-x3Du>%wR>-neDSNQK?;4T?XZOhDQ^G9w;8~9>'
        b'--EP@_797X4d?TUJU>?+Ft>FG233O)hk`jmNAo?WhheVae5`$c$<ksK@NeP$Tj|}`ib^+RaeHz;=L>Fcz<cbNO&1CBb-EHjA?**C'
        b'C!a^<W5_Op2E=_^cvm*bCap@l;S>Cle}iuOXAMZ{?(=X=-wvj(vP?+HCxZ5Fe@@95zXu=ScYMq0LQ3;tLaEJg_IcS^x6E8RSiS?X'
        b'oM(5)d_xV6byYhc*EzXER(5Px{_y@M1I<tNo_PGIO#ZR5KUV(hSVB<kWuvkK_{kkn=uX0%hnPMGVivRV&DCBI@N(fTPacWJ^m~Bz'
        b'ctcz`rajhR_MpBxxV|3CTYmN}S^4q7v&Uss$0yIoPM<&HIWv0tbbEVV@_VF5L*PfXP)?EON&Fag@C|Gv4lo!$=O|{41^wEr!J5ha'
        b'vc8sv_Wfl?haWxF&pUKuBEdU4I5=2SFo`sM4=lUVE+c-|?IA)x{}UECef^lH{S!COZXiODTp<QFL-Y$#>vA%(-P*}6nX9&;+vE36'
        b'!u$$^SjT*w;@)m$m$<K?K^_a>ub;#$1|gk?s5DZxJbq<B(n->*9h@3Fg9+rNp?*vVK@~2CpoTzDN7MifFW2q9s)k_C_wPCiq5lt<'
        b'w@ub;`~QMD>K@EF8EfuV>RUHoY5RW#{TB`O5q&?0kn<7bih0O84kO4lv^)rT)DE{SDmy0wv%bQfjgysAgJ&t3=BEu+Mx<-CiHb|7'
        b'DwdyBqpM)}!NJ{K)>7(ps&aX*j0lIjeN5A`D^Q$J{VznevVsql2;0i03w!Xfg%ICHA--)u__hJvbwsTj*~Uig(C<L&-TU|P!_oPx'
        b'&rVpPU+T`@eS1Lg{N4rmV;8f*uF;EYK<K*AY$8PetNC-3D>_+9jq+@cY}+2RLJabTU1*UMdHY|+9C2k-5d$g&VdsFI5crcf6cs`K'
        b'4zBt5cKJ3=DA|SZGha{P{ZM+KPz03Z4LxEH?<3h52DxbNczi-8m)x=_q@Pb;@O%5qtlc($B#7$vmjLSwi{!LVzp$0citgXofDu@H'
        b'3ues$hL8pni8BZJk{iheMZ%IRJ7p<5lxO2*+qe;PU9R6nO^(aXf8<^!e{Zq>{te86WAe<!a`9p)77>fOcnM^vhq`|Q<YdRhJtF&d'
        b'kLIJoFSOqq5L6hLH6%-H+j|zdH4}x?+7re=nDp~6HK)i<YVw3^=)?MBCx(}&oP-kIau8UqId~k&)<F)vpXdGkAYx<w)YSWXB@rc0'
        b'07u%J2(j{LZQFiy3EI|<SyKT6E8K$VQvh@S#t9jU-rOUy7($TKFek1&DjV8ihgpKgEliQrwq0H&Mzatc)taF<>LIDvwR`tf-TI9c'
        b'ksFF%!Bd4L>znY<bw&CTv^N$BONGbS(M?6dGGRZ9-Zu!}g8u^;ezr#mn_>+7V2?YJsaeCccB0U&v2EA?8Rkh9macC)imEErUuH)?'
        b'OBI%_Z|XwtWt`$vs&K>lCJ%bwp#KNEdxpw}(?0Sk;up4JMRF-wUth2R-wAhg<+>EaX0G$8tx6JCu2ahE7TN05!uUu`p9$0>avj9h'
        b'9$_#<mScgfZl^UPZrgSob#7-M1Uvhj%qYYQ>bPTw<7GC(^YxsP<gj=0^eJNL?zss9sgWJ^^&U$(dtB--+2}9XU=tlB;?#n;^vB>p'
        b'$Rl`ksZAFFEE5<LDawMwSt8QCJ!Lt3s}2v-y*)#m%ITN%@J(NlaQl=WyBTb(tOT6_6bDr4XiutEJvS@74B6M#obUxYZ(B}y6t`7D'
        b'ZcL-I5vo+k5bzb8WxWFKU7AO1!4%ZmDuw<kyR&Ts*|7*e=FaLKv=Icge8b7GpIVl0B$g!;=Hw=3d5O|olT0|1oBYeyE1mGso7|-I'
        b')=<k!m19kV${M6l(WyjQi|tC}NH{^c?8?hn4;Hj$Lu=I{E0v{`D9^qmE8zCCGMg)r8?Vxxi$~Yb+h8!>W6l<HwFk&g-nJO{9&+kB'
        b'`yy`BxXF;Jk8j4V6?k}Vp2Y*|j*PiNZQFWlED0NW1Td#6l(K11kP}Y6ZIBd8M3AN+n@?Do9dgfg)hAhtdIKy{(4j;HME_o3bXRfR'
        b'Efhlp0QW9uvoy!^bstuLir1NVdVe4x<w)jzOoHZMMr1FykOm|@BAaYXh^~#wZW3W5e`W(BJXo^{qbwxfdY$b|48+2M%a~YLaLNBI'
        b'c={STJiJ?O>NW|>ja;9XncuI2<IAW^P^>NC0H2eDf1nSoJ%hemV%OK(h%mT=1)4aQd+UF2_#3QesICXH>7`?MN^i~Xnffh|9M4PD'
        b'!S6?d?fjfTG%xENW&Be7KikU1QgNOR7i6t4kFFvF$%189a#J-Y_U7?b53=&pw>z;<&+HwS2!<s*BD7-%a$C6TmMH_p`cd4<O(i6G'
        b't8#T+{Jh6=F$*p@7#V5{BckjvDn9Ga7Flp!{e+q#LK9X%nl!~jX?e9=#1{@e?_Qfo-YM$D+_r;DG3$>ZgDxea+!pg*yw{fEbm3@?'
        b'*?dl$lH2wm31P(8P}AP_{X`V9GCJ-<n`77D*>0rxGYRqZklCM@elS$_X=R<C5615=mn#Hkf3NiavV5K&u_JxEdb35nye?Gc`$e54'
        b'hQ}lt;v&<W$CZI9LnlRCjBo!b#RqgroiYWdBHMR=F&{Flq`l+Jcigz`p6l&SIomBoeC_Vp-u@KlaVZLjU~?Czf2;qR1;qHl)N@mZ'
        b'Nw4{;+;-Eox(-$tSXxr=M<LHjON1yeP0$Lgmy%MYB_q?^`Nu{y9=1E<p^y9j9}h~5-5r9VwR;^XY<lAI?n7{V!qE6oiRtm7(sL>_'
        b'8dS3JghUAkW2-SZ7-qXUI2x3Cd3>mhj;c%L^C<Nu`Qtn#9F59N9VcLaxy~wKXTM>0f7|<dit@M=3O%r^wrj{0IkNdq-J8y@Z$hHa'
        b'yv?8{ajzxjS$QN2$&sZ=E4ST_4o?e{#=nl~<3WWH?OMcVY0Nl*p`(mYHQb=J3+sG8+N%sGRik8T>|J4o4<M$U7uee6HbG}15;zJi'
        b'F(Pv#Zqf3lJS4Fc5>M3Ck9_o(R{3dSII@HY9Xu@^JlX^WkU(T<Z?}|K?%m(yk@<OmQJ2dvg*snWGL_}FCQjBtr$(Vv9ENV-P{j1;'
        b'6=`9jRR0%gVJK|%4*{IA`o41vV5(sR-<aecc$d&wkQ?tzl=dl25$uV4-+NXfGLTq4%mWBEx3AZ(EUpJZgR5Sf)KbN@9yHfL{t!`6'
        b'L(myB!0V8+#d9}8sS2!d<PaNBm-h}xd%K$4wNN~RLYhZ5GRE$nJ9|FG`LYy6-{#g)eKmc-;TDaG6GZjT(tmcSMWa}Ti2j>{5`p4z'
        b'9_8gxxqv=vCC449>L2;eJ5r5+oN!Q;KQcMLo2M0b=s^C8;>W=}9nfixIr8`&S8oUDz<Z8)IuNBw3(|q9+1rmuPB?OPgaVR*qPt|E'
        b'{**1udrWEB#OoNo9i#&XM7C5lWnYo-EE+e}5KPANYEh`@sc%{9XTf``HyuHrzJ4Wr&5CS3F$#kNObwq4b+`^YMyX`+p=n1fG6fkv'
        b'r%bO^e{^7`2cs{cyrJC(n--4o2XIt6ybc|JWU9v@h6Z)$QR*bhx4e6eK>M=e;G5y}R`mX)WVCzt%%Bn^Ae#6j&(Q3EG`svQC7oLr'
        b'G-jf6(1Qt?F0Yq`AbV8wE~oGke~~Ku@?rw{$0@~&UInH6A}lFds2=8`4dDqfT(A{LC3+B*7XU&?EcO;RaoIPwk66EB=UWzXcK4c{'
        b'j<uMYKk6rL5DNM<YNd;>=GUicwmCAWzO9ZPoc<evnLrlkL4Dr7N(UT)kGRxG0`sa-NY?o|MQ2T@-$ho=W$JGd%80Op%wV~-7`eg0'
        b'#WBu+GY^tx;=_exsY4C->K>d6R$rXSYKk1{_YVYM11?kr+)}yGJ#OV9&)tH<JIf~XtuuG%d5(jNQSA}gAbVh|yyw5!2Oy(!kv&jW'
        b'*}Yxs*dbq-rAHBD<ympT2!h)ma=?|a?TC_o4b@%Tjc;G!AR-gm@(vc|ByE4tL4^S1Vit1XxRr`~0>x!t;h-v>sQ(9<3W2V#9uo}U'
        b'TnN;8A!RK(&l%yg?N_2BvFFifZk5OrQG`Hx9JSKJr#GVi-LHjq`z0Xh`!<DmAf!h~pFyegrI(;^OI3&|^%J@ZNs&J3g}>|wTgZh~'
        b'-JuZn@Jt&QbdB^aa=>a{Km{&1wud^11PG~<gOtP^JI61a+%m2oXZwUG+poC3mEGRXa}asR%J~|b9D)pZ*Gly7v3GpC;PlCtf}W|d'
        b'1PS?#-QvX<EU8YsNIhPxW9iR1&@nv#36gmm(SGE~NFIt0ePiz-==~^z4eR^L?(Q6ubc)}L>I(IXlKhW~{bHPXn(u#9WSg*Ka6w{>'
        b'C~3(SO#azzcc)t{f8lm==-u@<X1(WAy9b-Pz}72L^ONRLY(70eg-{geecj@xuup_zg8bvEPbKw|-N)|uuK7RTJ5K(W?`M>qRLXIS'
        b'>ir*n8yd6+yey$G4NJ6tv?oitV&#eu&469azga|{u<yPBk#a8@Cma95DLB8!?c8d)AUXGzedsN_?=4uohW?|C8!Xz4a(41}-=G61'
        b'pDmU=Xt(9MtBHK4Z8+h9Jj`yPe~-Qp3%VjY`C|(P7SLVxJ2saV3NQzOdC!}0U?BDoSer=vXm`icBoTSnpHL4*zHC4FE&62=L5e*k'
        b'UZhYa#Kd6{w8!4pW+y#%vt8Qzx>RXX*6j~LbBoksQ}(<WI0$<CrNgg6QRd|S%g$rXDVfb_4}ZpmwUo8n?2>tXCC<;vX3~arcXna-'
        b'e1A|1i<&650YAm3%dMQrtim=iTG?40#BTIDJ-X9REu~AW^Io1|xl{hm6>xy*N72aap0(fMDcz5!8Wk7B=YDA)`lY?^S9ag8?DR8e'
        b'6m6SEJI`&k4{fpcJ!7|i&*r`|`s%r-?L#JeUzHt#=xn}N-*v9iK4h@>RoWr5VBT}FzVlp#eQ2Y-ufh&lp3Y~p94Kj%eW=9Vx5*Ag'
        b'I_C83?pZhmp*HhuR+2dA8n*6O=(&ydp`Y3NHrn-nXKhWR{pZT;Lyy|~%Ix}&A(!>`p$U7c?R~i#w-`ep-GDTDYKHYwiomecG{dG+'
        b'iq6+>mYw^Veds6lzMt9k|I4DNmos}f?~455%$vbjh`V(o82~_<`X&0(Rb8BT1Ikd|tk}^fazD#5M?g@u_Mv2ZUzXiEz#e!)XIz^5'
        b't;Ngc^efJ-v=7DG`&QcZM_BsfV8u&|=WaoQb0Ax1jMBwO{}RhP_n>`fnZ54;`$!K9EXF7}Y6qUu8KZSEGRrHsbNXfHerz9FZ120@'
        b'ZtY;T*Y`lS3VmOuiwR4AHs|%Qa|!mL1@=C*9hvG|jLU@ILk=v%lED!C41cOIbl6KE$GyWV>GKE#Vw8JJq5r}GG@OgnNa**`OHgFs'
        b';>=ruNL;r<b}rmL6pmJz@4Ait7STsrD*Sm(5qfSBYB=EIK>=@mJ=%sLjWIi$FO;UVX%C3ch1iEe?0q7;?{gdd4^$Sch;gh)F*g%p'
        b'LSgQzl{$F7p*`Le(v);%#_+xSx{~T#e$l(L1h)Qxq=Hw6L%Zo&gk8%Mk(EO1U;#A@m+QAE339T^brx^-U_thvZWEaIi{ge1nc7||'
        b'D>)bc5GKq4?ib49<Bww2Y%uy@k6=U#PQ2~rCkxtI)BD5SG41=?jwEke4y)aCBrR@R!k~KveC$0k*f}(Y9Xm>IM1x}+O5BlXvkxiP'
        b'4GO<zlLc<Pt@TI!5$;%2T7D#L!8XsJG69uxKOp>u-FAGim)d0GbwXjU?!h#7ne)iS%QxB{Om<o>nwh~_#l+B8Vz}NlV<7{=$wk0M'
        b'x;4df!p<S3da%8_Yp8uk;yU36ER`sVe@J#NU>oYU1-wuDT5L3f#&NpLCJVjaLG7X@+b&LCgnxtTUCxt(%C9#;IMm(kU&E(~2h@r!'
        b'_<Ipw#15b{jMo$k&iQRaufd9*M;dfMF8LRlH~-;7!F%8#pfiYdF?bMNUhw5<w+xvAY_2OSzd4U4@SQ7i6k(Ngj(kDoOo5}hysCL~'
        b'I;J}WjKh^%`ivxA{+e>?N93dJZD~(>cMKA1nIY*kzq9WnnTK~PWDE;%?#zo5@lGvWhvv?u+v9yL#n~;j(OudTJIkBj^dAJ?E@WtV'
        b'q&*?4W6*oLx%^o3k(JB(ifoWW@7oD~m7CjzyDtSf22V`6N0y(L_2!_36qg@QF&~!}Z}?7G91|z_*g{5@7c`sKZL*NW#TfADtj*Wi'
        b'S1PmfcCnub#;}f0*kZ>Gij1`R1|$W;gJqp`7@Fp)SGhAJWb0sVhLW<y0Lrf`iG|!57&i44d)N2Qx%IZ8^)~6J^D#cBZnA&L2g@DB'
        b'BA(^&?K*`B^6ki1nUuU68^QoAudx1iMRm;)efc)Zi_u3>lho?@@DbxwRC%^6>XV^Wwyz{vpD0m_rtjER#qD!hHt(x%4lT0zSA(y3'
        b'XFq_Skh7L+Y-`y~Z|s|?ek_d%QOgn*qj^pB^U|0@UT<^PV&NA-U6M|WsC^Qn5)~P;)FEjGZ=!lOVj3Tl1Wrr+rz@vMVXsDy_3#7l'
        b';vIk_!sq!$l2>F{QbZ}H@sgLS4RWI)(sKCF`k!DU-+{`A^$%eq*Fe#5WsyM!Io8$HLrOm>dx2LfyCp;eJRsacZ*i$kvel=bXpn4P'
        b'5<)ETZf+{pXO_x}hGI*3#G>g4Sb$gyvo4x?hlO=4d0AL=`U!7aQ^Dq@@=|G$A-q9S{9u~#@S)9$MJ29Ey4*Ba{tHd{y1{~92qsOk'
        b's+y>EJ3|Tz@X2+u7x-n_xj3QD3)c-vtDdUVmo;yRA%qq~#FiDiXBop%?Ug!WO$nYGvG?`ebEO8IA;e;c>PX{T$fzPR9JVet8p67U'
        b'){2S@i+5jV4ALH0IBIG}Swu>!DMk0XB7>C3D;i4j$Vzz=J7!3T+Yo*Zt*83gPb9FS0}kEcLpjSZ;bB1Fx>a)FVn9Ub3=v3cx^rki'
        b'Fzm%)o#O_DDuv%Q)Y(VBi`KHYIHj}?mL4Y+e=&vV4ubNh-ps0y>N-G9>q0pExhqOc1=$yg#aSQLo;{0?uaf7kkY~pa@Zlnb)tPp('
        b'u&_Lnr=BtAH!BmH<0CM=6Ofl{Arrxn^7<}axWt^;oJDP-O2J>!DGI)3Ht(KBa`sDr5DE7{qKnSZqE!D-8X>1ZMom0#B&Ai|2L~|W'
        b'7;8KT3Yy<6_elL6fY1|5&>;*7w#bY_>McBGejFbCehec*O`XAkC@%ZgPG9BF<|UYLfb9%a_7Q6WLn$3fepdi?uCq^C!83iLEMJ!b'
        b'o3W5#Ro#^ahFrX5Q|0!q6<eO&eZ6#*<#7qKYRQ(N7x4yst6*)2bw9*pNRLAX#0b!6G;du)Q5AkN6wTv=60UKWbnvYVxWh9;Y7Z|!'
        b'N?(vo?1HczyN+Ok*%&zT{}Y6eAr<mVa~x_RSG6djlDx7HGH~TJZ#vtg#qZ$^83rj_+e3I%1;h-7jO_1oKApmlOWLgJN<QrO7VV>3'
        b'wiNnFm642vl@AX|Cxw8kytV4@m3_tMMQepG;%h}CPy+YA3J!WQ{bU%}5wok^>AcDq!d%Phe9P*b%_#79TdT-mt}V}23a8jO+yxuX'
        b'YH!}0VJqJu%g;gRV|)#4hU5MTyR96r_KJ*##c-yo4ZP~1$Z7+C&`do4gL#19z^<7Z5oW*+j{KPwZeU%kwY(;!EkqHQhzUPpvvxI?'
        b'w>P&PLD34ehT1H>a^!t>_f_jS3mO)noAL?~rvDY2lZuUOWi1mo_0OPldUEMBe<D10wULbYi2p^nZW9(K$3|AO-z=@`Q`Gqsb;GZY'
        b'b(|s~p+F~Gi1r}6hb=XwPZ{5dL`uC!mGUy+KYV*+VUQ~onQ3j^n=33a;M0&gi$P!uKPRcP8!SUoyNnjq-ICaOV?rpkVF}u)x7g+F'
        b'yC<U7)rsHu!NvvY>Wmj$Jj~7*c;E9rnJ3k%H`qHqD7F6q!&L7)4AvmyYvVwOLPz~k>pFUs^~X?)i2a*m<>zny#~zvID|Kzfbg`g*'
        b'HT4QhtpjT7_P<*bHc@e6YEwwx`&Pt8{+$yUpXfVl?GezQpqDPXdv%5435x(EU5t<XYXeR!?K@@d5qX9zhEV!_P8{p&d&k<XhOEt5'
        b'^!k;=JtSA)6^UsuBazgDebGn%2Kh;K4^8)7R)l&ke7{^L{0u^+rYoqPzCT&VFxc92wVb`i_tpz+l;@IVWQwH(KyD1Nkdke&Zx&U8'
        b'3hI~J&NsuYh<ZD+ZkdAavX*}$8`^1AUR0X7O-HD5vM)+nGx31;#|0fqy4Qjv1X4^a^3K-U=xO@S^t@_4_lgzH4~qXT+@dWloH~FC'
        b'c7x)oe_8lTiYIRD{yaHk*_CHbBBfI(-@~;TS`iqE++yf3uv;a5G6K2W3W1`$K>oadNGLbsb{g{c=-76`7Z{Qr<=v8eB>PG*7Gz2)'
        b'Ee5g5$l6?&+e1s%Cq_)ZB>R7Sy?a~}SK2r}nOqH{O}GRKsFOe-pmqb;a@o2Iks@gALaGtiwo5<|sMZkf5K1N}1hwxgXcbtyn?zHA'
        b'N;Oy&v9w80iV9u8wq90R#nPhH7B96{h54N`1E_t!pWi=_IhW@==Q+=LF6Z)`214l&Y}uU5Gn}5>l2v_!L^@&sTmbX~KISc|ooJgi'
        b'%?D;A0jQ+DuXT5VxDv5@3QDV8fRyqS2^v$XS<+<kO+NGy9RAid0K<i|#)vg9VY0eVvHNvy5VeYt7@d}81@@-E^e{U5UbLyj9vz)#'
        b'IYTN=&W~Q6F=S#{fGSiY7ll{u3HzCt3qZTkY*mpBX4Q=c^nUDebM$IEyi^bGm&AmMg?&rgn4Eb)!m)H?4;I%nz0~1;!T-{K&mUWK'
        b'EIe2<Y?lv1%hDni^v~}6{9+Pui~vJ&A;};XTq?d~G^hmwVbClE&a$`V6zN>RZePGZ(^}SQ|8c~AX2jlVKh&C`8@uwO-4RvY5!2$|'
        b'!l-3kcOT}oq1H6=n}<|<N`Onrx$MIjf8DWHG+FjURmKK(UtAlzdNzWTbk|K94BgSYxwGnl<8-&7ba&HBBYv}&{WeeA{qm5Xi_?$a'
        b'#Vcjp>5gbaYhyC6lg5~Btq`j2M{UNOk&Nd6gr5!Di}BKKpiS@iJvS7{t@p!h4a9hb{m^kiT5-mwD@NSVI=AYypM~3h#>@V__3-W`'
        b'FO>=t82vn82i+o7Hy#?#mBp4BYtI?)0tCU2yPWeRGU7J}2ttJ#>E{7bOQXr2dnA~zJ>OCDl_60tkO;K~VSz*~lhhS;u`rfI9b`}k'
        b'FJiT^+tmw43-EUF!p^4Vu>Hr24W{kbN^j#uU?)1o3&xlev%vWEW!I};utoucG0-CRCoVu|*tA-1b2l^tJ@CSz)nK?KU`DKHQL6nd'
        b'YQK@*k|CfH#1VME-2CNceV@S8Cs6gx(zosuZ4n+_95ndtX2-Xi&6dsWdtW2|1#Q3|JfSXb;Eajt)&5(vT#7$%q2#Ci6JhiT`;`+y'
        b'0KT&sfDFp5O*M#vC1RN&^*Mw1Wl8Fs+9ruO$RL(TQU$e_B;qCQXBWcK#-LV%dWl5rN7y$9-H7BjdZz^EM3pYT*m?boPwXPhsg5wH'
        b'Uv{d4oa$hwTGlnI`UKz~Gm6bV)`W8Y0VaHqMZ6@fLkL;{{qLXi@C1x5Cw^g<x2NdgW6>ufmstBgVRWlq0yJN%u+?Hr?dUWBsNQoT'
        b'_y)Di;Qd^KH=whjNst_DPzM>CvZG3t%W^@h?P`BxYsaOrGnU{v0LgZ>1dt8%?vB_W5NS^o=;3(l&YCC~Y{(#%)pWuOIOF@QqOxBN'
        b'W=4%S%K4f!Z`lkm+us1+)wO>mj2^awUSAm&Ub+BZb7`9ma2`=Fx}#o5_`=B&$qyAr0PF$iJK}{Y!I7y-u`E>lvNClJprlf~WL&>9'
        b'vT6L`&QNhsP_CY|1ENNeDXk;oMM-&^OP2%cVq71Yp7d+<&WVz!gO%zCpIFe%JL;e%bHv%3H*j^oe!z``PP{nC)Vj0dg)OaVtwP|j'
        b'w9i3$=e7TrX+Oa@)QJP60bK!hL+XV9L7JvR;)S50U1f~3KdYjC^ce<xW;(R<*pkC>jU>kB>?5DZu+q990)z4^Fr0<)djz04ci?Gh'
        b'WOmG`2QDYk$OsbV{&tJ4`N~d-pI#__<^b_?xy)GCkCt_`%_43>l5Fe5+%SpBZ!f&lFn2t-xaa!Rxr$ziT)xxZozaY*W;}2mbHBjq'
        b';%7b}`&wm^a90lI9UjWSf~Vqdb}%c@1q+T!iY<ZOvMqss77hk&b_8v1H~q_eeG~B`)JC%0Y`+U(x#=!hc)$prW$$&91*iQ$$6AC7'
        b'36D29=7I{Ao;zgUmcAnZP#05rVUpfO`!$92AZ*O-0yBp)1mJs5zmU5wA)?#~$-x8E0lpp>7?i#b4)50Jep<<C<G#l&83Z=cF?Uf%'
        b'^|8gmLH1?`8#Hpxd~y@vfLL`Dm9=7={U@}8$Yuw*sonGyJf_#~haB6PZSiC5k4Se)yoVO@FI_s{u|_{^e-Ne_&M-CGI~@J9TMyQX'
        b'FA9m(dMJj4Msc%Shu<Y5$ZT*NYRv~y_)=rXM~#jazky==u_i$;W0(z%l3MZTP0}dti&Cxoy^RYA7~tYEII_v{9ccb`^#!;*mB4Jy'
        b'&G9oej{s;bZlG(>zVTxK`?d`Q-iA|<0z@J<JM%Vl+8#EC!8L8^+o;j4B`nog>juWe43G3A*rb7YiCe?#Wn~-CmHhPzqpdhHR-C18'
        b'_QPcYlSLjx5LRkQD+XH$Y*(nlGk*s#jke2Y>U**q>xND~u3+toV1Ndgz-qGoMyjG%@kD|j7#Gbxd%&_gcchGZ6T{$efB0~W-CWlQ'
        b'q~_2UkNY{8ORcTZocZIV(biz@yD>bgpGSeeOS%+`f`LI*{WCeWHq5X{km#@Qe&$qgSA<@Nka#DrjdxrAN_lMJs*%K4JH}3_OCcKE'
        b'mPNj#`>hnnD2fumAwLiFwaQxr=$5>kI@9<A5DqUPgV~!L?`<+C0J8QHad5O(lxo)6>-SD>&&nvvT6UDJJoz9oD+6$s8e6G!c#Sbr'
        b'7#D%-3aw|LMXdjwe3QRzx#7$zRlJ~C4YUoBx`|o?H5ujlgKWzsw!M{+mW!JgY^rsbvhZfV9JT2~IgtcQ0gI$1ra7#OjlG(ggkseX'
        b'+{TzKVJ%51j2z(%>X}~y)Qt|+a(*)CSYP3aloTR4OsSrgtxikaxngzG>J+!6a($vvkY<$Yey#OO3FCZDs#3YxOO3>`qwlO}NXxeC'
        b'erq&W&q0s|;<rXtLtSyB5_{ePmt7i#EsPc4O!cPGR_m~SIq8zsV0#?Z#@&7z2iDH$GSuj(;5V4l9@uyPwd-b}eyv@*cT$s;u?5mc'
        b'd-4JJxuUxId#Fs`<iou_VE+TXI`tmY2GqANQ3?-kD@_d0CgH4v_iSw#+v1Q}AI=xuKqLYDq=lPQDBNEHE~7TUyQD^w7gPKq%K0nO'
        b'VQypjtiHlTRA)FHwl)|oQWeZ`I%EL1HjY(6s+O}&Ww=4;T663Gfow`UFLeB;YQ!N2Mk*)*IdXLJn@fmptfpy!Pq9XG51#fg?K@I$'
        b'K~4I5yPLen21Rd8UT`EZCYX>X+c=|ZNKq7Z4a#s~Qq}NSl>WHGLAShRvRynIzCFN1V6bN`$_en~$WXY~i<CHtE`4ILpvE(Zcvw~9'
        b')E5gtLe1{)#)d>6Pb4rdjKBukozW1dBvO?7IPM2>tX(t*=2@QPjsA@kop}@o?Goru4AXM}SKty8W5{1r@9$~w_d4I`qxAPk9ad#?'
        b'ub!;3ovJc_TjjLGXWn&Lzr5NFaWNX!dbRsMzkPFzPYOKhw$^jYRwEA@%t~|3=1z&fM{uLW-&<zD8%G+MN`DdNX7Kl1<5i%S#=u)?'
        b'3uGwb6^-mQ<E?@|N`_1Py?l%=62n?g$yzVYJyPlKZSjA;_ejI$fj5NPhe!0AGn6J|XsrjZ)eUP!phaRC9BSL~s$sOB)y9&3N3Ll?'
        b'tG^^cyUMj9nL$Z|0`@J&ul`|5rvM&Uad>o`TnUtos*D2!0!s=5r>HvF*vhR{W6UmoiyyT1fkVNvoXocFoy2@TKuvTA;YKhO_3c%M'
        b'^aVFBDEz&RJ3sVtZ}9UmV(!sK+@*0#qrP?oI1aUbSZqQV#?#$PSX%pfLPkRV-0?+x&g9fxZooHi-E53BrQ(-U+r=y(H>7ow@RiNk'
        b'aOtKA?RgP_oNn;LfI+dWWEC(;fx%0>Qw6Nj`XH|UXWVDg*26W&(ds}1^Qr}QnR_i`g4GW!Y3Wk(@+E98NEwTPy#T57Ot<bL4^S&Z'
        b'-sNxd;d2%SAT-rLqR*MGjdpRsG|k*O2?ISSPBMo4o;&{u+A~Z7LD(+g_U^Ozxe=Z4sfc(5Kv|I?h*tv8iVR_Vx+23hGjmcF6XT^1'
        b'x+d$6mf%6%abHgH*fnw`KfODe1D{d88d5bRW;tH1vi+&b{A!irASwOQMUl?xIZndZ<|(%1?q!8bl5Gv=fQ6n~n|wHXf1)v88R+`y'
        b'E0(>JiLb|)vNC{EP;=z@<eJ92%5*QN(X2Pf<nGI@>hqOps|6|D*|r=anYg^U*;dU&l8a$@PDK1mCB7O@>88bdb~o{JrCuf2b_BFy'
        b'yjxOS?1fg#ki7Tb9XqGV66DmWRK5V?n_nOJOxgYNg~PpjQ=nJj@^cp;@u(lUty9(=bE%T*Ch+zEHPVjanX4z25^saw?Bvb0W`J4p'
        b'wG;<%GeL#Zr0UY+4mBud)lMGZ1NpV4sq5;`h6`#3R%N?oFwd&e{c7!UQDz8ws2%ELGbpS2m6fc{Hm6+6xtrXrc7nbE{6P!Zg~@jl'
        b'v+T(PP#wzd=m&SluH`^&JQs{0n+o<I;tRD04-|W&)nAhoeJ%ibFcCKd%vgTA!(G`+D%I@Kyh&pc0Ow<DD6CCNuG2cRcQ<H!T1|;*'
        b'rqzPPU!xNf(+sEPD^KAmgUOECt0^(bb=WfF;F!AR#gr?_!t2*k?s9--Y+?YzZ$ymM!WDLQ;;<dc`!;Uv?RvGqx^dEYyIw3%-MBfX'
        b'rV9-7Afo}CHUQcBi_hu{N#|eeOjcjKn{urhKGq4mX#lTYjp!fXz@wsi1&UMPGIL29T<1?6SJ(U#Nbb1*k|Sc4sS_3j(0Rk$eiZs&'
        b'*^?svBxe_i=tfhnUBAmYNG6{%61l5W&L!VXGupwAyP)g2v0$hOFjUp~)ZAn+;=2P2o?CX0rTZ0(MUu7>IM@l@9o-n;^AQ?14<Tm1'
        b'8-GrJLXdoTzYje0^v0|3f{YZ-3FBU%bv$a#DGno=><XM=rCMl|B!?ypD%EZVwJU&_ju_7+A6^p?4n}Qev{r$kVH*w}sA=-Cy=}Of'
        b'W4Lh5VKkUG8?1X=s0H@XPf6hEP<)Hcbvjm2(F13byE-T7Pq;qcNA5Z^k&FhgKLE|B1wdUUuF6k2C%cvuT^Y1jb`IkQ9hP+`oJ*7l'
        b'k``1ZLbmO>0c|?txecs6*5%m&9>NX0EU7TLJKfL4vk*<o&d*)DzI9g*u!4Nox2{{vs@cVE<3KDFewgRI5NdgX1q4Xu%E^^*v7(ES'
        b'!?3<Oxqqif;U_dQmPO1_`njgYF6-droU6SXH%`(!6xQpcs_apE#_XP-VEftKo<9f&R~j5E4YrjA^CUq$hSqH0{Rm_Cv9XwvbM+G6'
        b')OG7q*F}b?8I@^9!KcQ=ui^PX01Zs6Psv?d7+@;4>Z2tB&?gj(B1MpEP{~1Tvk#Y?TX*be&bhdoWcK0WqxPJ08+d^D42rh!vPcKH'
        b'Yx#unTyex0wH6WsocQMz!bGLoTcP#>qAy+Tle{zA52$vZtRFm7=@}@-ie80-E~lG-q0TTIBy;L=9O=QX$B9~Vtxa^Fm)`RrXK*xZ'
        b'Qq;+Va~;gX4Zvt2mFX<i_spx~#E>7uHcpr^gLD5|(sy0r_`s$)#ZZ_S(W~)9)d*-p_5Sbej#X_;rP@QG7FjpW2il?Y0WcI5@L*26'
        b'Besp1t`;iQuA>{~uLH*B8szFF;)0v)5@ALG)U~4}KvQ!P5o9I5=PNS1tojmQ@N@?blw5ZgttM2#_YIC$Ym<m^;*Qw6Hb$dQ(;NM2'
        b'LkwcC5%Kf2V&W&FUF_4(F9ljeH_?Vl)Nbi&cj?_pRnwiJZm+i4Luy~^+WA9b-^*JJOi#xZ!f=6OH!|$Kcozrq?O#dN!(ZsfX)TTj'
        b';_nr3NzjAQ?tB@1O4rSAcgn#JYu5a9XFO0nj)>9B`NpgD2jHWfPDcdgs$8`uf%dp`=4HO4ml$$Hv^%K1u1Em?I`|EG^9qn9*9{Wy'
        b'__~hlL!XT7aT)xaaC}afbBXr-uM+F@)ZvQ;w^}#QxrDHIv!=w}$ke{hPgsiewQ-0SA!?V|CC*Ui%h^MvcN9*!Y$V4m$ghn}>x&hK'
        b'DS;(=c*AhUH!)VO&)g9mhpSkV)fKcIY7oky#fa7pCOE96Bw&`6eB)rRLv@K&&-9$&*2e@kWZdF3nj7+m*|iL+Y@<zjk=(^+X2&Ea'
        b'VP1x%o;evQ`EAU0CvHugkGZ|a(o|LHH3i%Dn-=eon+moC=NMAz;oa|*eCql<v}bHaV#tIDD1uyMjJ`(p@tdhvc3u)Q27VBxt3?X6'
        b'r&8^n`ZM4pj5D;4;oL_W_9OKlBAB;Q?6GDZS{;L^ibM*gNagMgEEa{rjgPT0PFjKeXdqf`M?Q^9)7%>pi=1M2V8n87F{wSsaq>Oj'
        b'nxvocRo!<H85iCDGXcG0TNGi=A)Na^9!+$Cn(F-@L?}msB>VXkVIrT^X~no^^@ysF3rCHa0=MQAfU{M(kR$H`h`Y*gppZ*y5Kgp4'
        b'Q&-&iT3!Hg)gR0k)Vvyib#!s1D_mx9Vbi!s$H))Zrd`lN12{F-pYh$U+5w-WUoDDQFz7*;mw~EhySUb6GgYzYU{x3h#sOOW=E1z`'
        b'4EVg0*dv}D9eX4?@m}Jgedqt_3P|A-t9YHS5PNKmRj56B+Q~2eiG$S3tic6@V*%i<Yvw^c@gHc3y1<ef_`r76uNLfn|4h5sBRZOu'
        b'?9;(Mo{{XKSn8RQ&$&f{$}0EkeftOJ5)L0wf1L9Rsrh1R`_@`9xgb^d)qDJ9Z0MZmzK6D81F7J8ioP1fWIag;qVPiiVV!<Vg_?I^'
        b'DHt!CLh5?D?xOj$L-Z9(aq>aJpu!QGkQDPskFoEFMI&N&Fzpj!QbJP1DZ&&6B$z}E7{k?ibn-p^8t-|EGrpK8T2+-8U7-5vJ7w>x'
        b'#JDQaJ#L(ij4uQx8<@aAy}}9nwhnrgPI(s_&ff*|70#EtSa1dhgQ*-3r)bdplB<RT2yjinSLs!dQNe%QG&Pr{9-zIOxsLOCFoh{Q'
        b'Y62weX@%{3L>E?RGzF^j=M`sGf#0fS=c#+5z^a0S#3fBz@NHB{5ys|x1!Wmvle+Azv~?rfdInGG9ld(nX+38T$jLUBhLt#TmS%gD'
        b'-bt2r@pIf${INcZGv1)~BBFHEE`nFO*fZG@&q=r%FG{#A^7wu0EA5VmHlWYEM!n{Pe9;YVGMn=|iLB(ty-XS$IFOU=dO*+Gn6xQ5'
        b'nWn#2D<mv>K;c?Of><{}zu%QYNX?*Msx6lcrpe-nU|_f#OWT87ExniZM2u(wa)^lO$Z`4SmfAxdBZrLk2Et^_*d2k!NlD<9mSu6o'
        b'<VqfAHL%+jViZEea5=!aUF-?aI_AEhUhEF0Fqp`?ha5I=3ukFQv3~K-e`v~fuG<~cB5iqbYa`&ibPsg*KS#8uaPXtvW6tiQXxv%S'
        b'!k#ZGyR$vZp1vCG=fdqQ06ufoB<yeM#C!ZW3yG{d_L)l-$WLc;vH}igTV1kptZ+Z${69YgO%%Um@|nqfKile)RSnNo6O0mzx~E*J'
        b'_E)XJvH{}hYCPMm3#ce@x<d{G>;c$?5wZUrhhUi1&!k5G2=sq;mCaE&1nnm^FbqFqeqZZC3}iA16ReOWO?Eot>8T;TJplwolS_O|'
        b'UYuT`#^aNe4uL`~RsiYBSA4~>$1<F!G+k^>EFRkJh0Pmsl(eA=^}JB^{LF*ooBUljxC=4LsV8b7><`!&6F>-6`zuaq0-j%op`l`b'
        b'?5}U4@_+28c1Mt{`@@@9C0x!~Xt!8@o2T+74O~u^*H6YT*71G-s;1#sbMx-b%MIs^#>U?azz^X97MFmQE-yEJQTK_iiwo3P?H53A'
        b'q{0)(!H?**i;&xu4;+!gh`|xDcu0&p#CqGUN;9sHWLPKoK=ik<M#twR50*Ikf=hw8kFcoj&hBD4p}w$&O)j{E`Mk+A{hK}T_Z{26'
        b'7F6(6b8+2ucwK5G4D)tq;sfB-x`J+6oN{U9L>E`Nm;5xU!D&8Mxjl7f3&S>4IhJ%G#=+K`Ir<59=6!y%)5g+A4jpP0M2@sLHBmde'
        b'xZy|8_VbS;Vk~>fP_=JFQmA?^#@z403)xYb_P$UaiQfTskJ@|0gbq2<oDL1`&xWeK?x>#!#!_Yj`2l~IH$Th!Z=qt}g;=N>4;9a)'
        b'NMElG2vv)TpmJ)xIiOzcA9n)G*sX`#SeaMnfgby%gjtxJtYATV_d<A=@ya~aazvZqlF}W)?D>=&GBE%pqCbHQ0bmWOrPg5JH|x$V'
        b'XvKUmOdcgLo!wzK6#&>nVyWuz*n%4U;T^zTzubGdb?|JZ<7}m^uhN`ZNu)!Q{mogNCh`Mj+znDUR`Wgzbh*)~*Y8v{&!Q<fnmeK0'
        b'OCD%7I_s(`^<_IL(sfnZh)VO(N_d<obA(@aq%zsL9eABijGZ!+GLjslRO87>O0^h}evKzDB(5^8MktQ}^l=Ym1SajS3_ZuOhcN&R'
        b'6T@(dhKazOr3`{QYL8HO!o^d%33BY2%hMb?Tt;zh+-g9qfkSD473wD7srFwvxzxiqd`>oP4=^wm=Hc6ixmX;D1PN;?W7c6FO0|#0'
        b'kv)2Po~V`4j>?f(zvvYi(TCEI6MoQ;+BQL3IZj7*JD9Gh)NNALIjLo=Q=NAM^lo=#gBD#T7vz3ZhF~6PYpPUVKURr2qHAnNS*2}B'
        b'<?WX%N2rq{=Hg1}ARo+G00sg+GNFoksAMctr&KDx=Ga#=;9+w$u5`ph`Zxq|JWm1sNrbxZ1i35sHy?PzIv@&-J4g2Pk-E_}O)!vM'
        b'x<lZ&{q8V-q^E>3Ei*r!*wuRPj#vWPREqsT<LCd){_%bIZtRc$X0Q1G<%kirXJwwK(y^-2ys8qY5#S%DFfzXY?r$O(+02y_Dn5#_'
        b'm1<x3XKvDKmFaNnb)K@PM5&&SEdp#Ecac;|uo1CGV(QKzvAbhwr8$;{giNqUoqVHH{Sx#@Fiy@;&Pc5@eJ{Dr<0JK%chg|RM4URo'
        b'1qV<L$6`Gk3(mi&y92ZXL%Asj$X&sVZ4Zr3j1L%ZzZa*A4@iA&`h1rId2k09YvVhQ)YQ(NE(BjwnmbN>_pU=yX#f`B@Vg@t;gCdN'
        b'o?kisaHsS*pnvq#64U(&mG?x0(}q<V?;L6r=(p@_bk>>QO*0BxhFV6p8}XJw=tI(`t3i!P?*nJ__qZQP%m;A6f61Qjp^pZ}lb&*;'
        b'4HK6i8d#onKfFtu`T&CBq!;Z?0o#|6Ae7#j#+^WveppOh`7$<}-r=4yab}SqeOqocT+E33o#Yl?QFQabTp#^6nClbE3KJ}TZViW('
        b'7KXtMg&boPZg0R78*!zddn2Pkn(P4@ts8x}MF{?5i$KdPxTBF0l6iwPcJH|%E-c55cx^X)uQ&NHaLSWvW3XBa7+ebq^_Y0L3^xim'
        b'zfGM}o>DHqk_HKXCBNP&+m_tStJ&evGE3s;E<^jYaLwyQD6gR5{Q>Vie$Rapj0-Tj0o|Z09;(Jhf0)=6#Wc0T;|w)TE>0&M#Qoce'
        b'%a;^iF@a`ETZ^Z)3QZs4Ed-=Dm7P+T`5ifP=OBToKs`qjBqk(1!#%y5C&`!{bXSt$meRfA9IU`;<65tPY5GkW6Iz9QKpe$ha#=%='
        b'ZX~`tDWbfKnHY;Fbi;kAJ0!fL1ABEDMwAvcJ)|R0WA2KjocR3-%*g!!gewecRg?L-k!a)9))BFgKP7=a#=8COT*<-9)Fzz74UJjy'
        b'Zkj|Gt-uo)F<+LNEO>M)9`owE7`sIrEy1xRfc^lr6k$*dAauz3SENJm>WTNKs<QiwSQrZono(M_I4_y42=o@cKU<mM*2Ze@j>cn;'
        b'fDx8TCf4jk<6cBCH0~QXAiFbRJSg1X8UWCH1-1_w-=FCUx;R-j_`<uOj{_3W&7LuGaPGT~TNMLC_(-=5OiIvk>4pi=-EX!$=;;Ko'
        b'jNRNZesZ_xsKO@}-lrVj34<Bb3L89z+|VtJhFM5*P};E2aDkaPj0094d){%O0-ikK08p9P6W@40UXUs}^=J{Fv!68hxi@%GLF}m5'
        b'a7I~u;M|%>9dWTt57`*5E;sKZHkHD&%o%Q~*4sKobt9?p!w8~Od2mu6iz_lPjHSpB0y5zE&iH*PdxH)uGX#nZR}nf6`Z=_Bav(MX'
        b'^mg#K3P9KqKR3q_*gI<A{{aWS=~mAsa{Zm^DiT@W&M}bd6+L>ATC-|HyO`4FCa5KCzKg-%yNlo3Vex;SsDucCZ^>GZ2BWc~i!lHu'
        b'lQBcG*3+<7RKL~>&bt4Z1hrDRL~EH?_-^f0P&&xmP+~NSpL^G!78v|}f@}u0(BSVYb^!^l2LHJ&bq2K?ajYW9fi00ZB4~DI1r0Xd'
        b'HmG^hb};@oQ!O!~VSYa!W{e&JDVL)xYIn@l=|~jVfQchfdyF2KfFbOxlaJ|lS%Eh|t#N_=OdVxqOqiDAsxodD-?tCUU(AhI0sHeN'
        b'E7E3h$VT6oSHTxOWLung<{Q8|dk#1zZES1CyvwN}4HbYjA{h@x#)d99ZSPl@f2tT=$Io__c%=Q6of{T;C(;=qO?SQ=nl22Lcx%%I'
        b'$yE{U%5<;9u#wPo4~!X_E(%TeTtr<w1qDL=c=C{#@E1|e-;j{g73$Y2Le*}eCLYx2j`&Dn$fk;`PSD;2cX)c|2)J0TnX4vzRxjc2'
        b'YJE<WItP#P%VMIOa3msT@OVX}AtGtSA&;!@=TN0HV<tdB@7ZGxOmt=7S4;oo60Yeb==AsHUXkCEf4E~$>h1Ij$AJo4dWHF;iYr&{'
        b'SyTDz_f`iY7jEy_Fe33e|Jj_|sTB@ug)OzhY^?xR`A|C0$bvl|j7WUXe<r;BdWFMOVN+I^O%-uetiYjk-yyLOR-Owhuc&Y|RoIqS'
        b'n42nq<{C<$3p#$`>R8o}bLZTSt#G_wVOv^Ze!n8_Dw#bPksmH{yZx7nTeBT?6}BZ6=DG@a*#Q_3PC2c4GGCf7Md6~<Q7DE+$d$~V'
        b'kKmp7g9l)EXqsmM^+xMRRTFQR57?sJAp>NnpV-yJHAU@&qHPCUUyZk<g$WZFrr0A{{(l|BD;(px5l8&MIh-m#x(Jj9wsHJc8~CW1'
        b'P@Q2m<PnEUEe9{w)P_(xjC_2v%o4+~B%#k+h-*4*u09M{Vt^6jF(w5A4CQDw8NrCOY@_y}viu*kA0z=Tj~=ToO@iTsu%(-TxiGoa'
        b'LAUxp@NCceR%)vsdFd*HGJXRU>VVNrq(!|DSK?p_c&9rwPSc)Y{uu`h4?DUEu=}nv2;I2~{<0mM^%iQQdB|jPni>WM^>&9I7$=EV'
        b'Txx)2`Ole}b}oDV0!VA)SpPJy!Mc*)Xs$mvx!V=3UV>P}0mS(dXh%zZ_8&*%3J{V1?1ocjVMQ0y)F?>XD>OCY<_~q?Z{w+Yv2Wwo'
        b'_2RkpnR6h3dX%#esTU@i|E)`Fgyp)JjSTqhgx^Er08<N&VJ+ge*{6l4L+aHpw5u06)$$?rpNLM_<kgCjdhrWaiUr$?aZ@o~8k6T%'
        b'F(m$zyb;$l;!d&rVp5|zC$9o)7cc57sN1YdD;L5uR|NJZ#_eao4zWw?GB=XNP4JGb%p7C|Qub340iKLE+H;%)s4ROP?Xi<RN8#@-'
        b'=I$_t&tYs<&(|cr)2i8b1Rnm4M23Wks(r}$9bAccVcY>Q7+FEf>vrqlIl?TR;3~cyZqb6atS%F~&ioD=1`;AOb3*m-LAzL37X<la'
        b'w+qU-0?i$E=H<t#+~4XQGE2-0mLyT5RrJX%&PSwZ6H_6@wEL0hokxmiEzCQv101P|6(};Xn7`?qrtK|Xw~R)I;TE+Nn@f*1@F}fo'
        b'Qk8lq!W?PUT??;Ad%hu|Qj?(7Uy-^;0Hd#gtW(|ij$(X(l=Q6$`28(qib0ICN%(#b(8F;>B#`!n)VW2<=D?u<MI#BI6n1qYrZYQ-'
        b'S=5FAIx%BQ(B--yUjkz~RLvWG1J0BGW1p;=cpNqK6;mOZYaeDrXJr5rC2bgYh;*i5{1%%k^4nv$w>=Wr<YGD49mjxXgvqpX>Yh!#'
        b'WG;O{2N<-sIMMck^@??oEa^Mb_i!u{KFG|(=83!+gWGhDZ93aFotdK}n9!a|`vHGq2#;=j>YQw|1?aO`^DgrT4LXNGXEW%`56X%A'
        b'&_bbAL*`m?`u%sh4Jij`0LEaE&QYSXmFUd3%847WI5Yz03>NAfg*sc2j((iP^MUZG9Rz79MK@}FDs55}HCg?LoW@}kfjFpjj%=MR'
        b'TW3CBPJ9i4KE3~tKRMM`s{F)UP=2+}@s`f^md<>(oH+f*^4XJ9XB=s~tq<oyyyJC_*LAknb>`2@iBDmbhHlU6E`wa1<8L}!BE)-r'
        b'>#j|_<a5Tuo~3A_F~8=M6%^H0O{%=P>GTF=4&0!;1&u4f4Ji|<E$r-T3FmV5CLC7ZEQ#+<qihgBJir}^rvTAGcQF)iUE1S<EbI7T'
        b'$b>pg2!*8et;t=T42)y&o4u@~pLV&ajPw}6=-SC|QYW7s-=C>Ic<LMhI$MCw{6FQyR@evGx#{tw%Z>g-m7A?|%+uNC>CBtT34$IY'
        b'*<sHTR>V2EBp=@QAZU3SAeED<U^K!qWZDDd<E6nf4k(Eu8B+NKm{U!26vEd+_mbf|XVZ+cE0<jVFzzu4<zihie8^AY1MCOO!OP3S'
        b'E(2XgJqF4PP4^0QWOp$$$q7~J<AvB(U`oUjY*;?sk)~w)L-jQ$>1?^vWCZ;N0-5T!QY}eW`(^qAe11=7%vbfW4Z_#dZ<YYp1Xy-}'
        b'un7)@IG|2jo-i0wTn@YyP$=4n#~d%m*lDlqfCrl>Ez)RCvDIFUysc0RLe;{|`DFC~i9ib=9x$Kpgy_a^aeaV8q299YcnstRkS^1@'
        b'3(6L%pi=E0s+L-PNF$@xqVgWsJ%Ucv_Q#^8`#qo1XV0kl^Yz?4{K1}bM^Cw}r`#+nCjua`6>1cCTc%6+RtNN(GJSw#WSce}$&#f`'
        b'i-%C7p_XB+uN4X$IPLajx=uXKjrX&>jwT$A4{O<*(2e;+SHc2Z2@8h{26-^D90(7`tnz_NI1s#aHR&ghziFcO;MSj++OLQ~oMs;8'
        b'(#9e#6aj3K_g=PQ65GGaC9%lXeZ+1!46?nLw~r)fFRYi|jc0lAF$u`F1(jFdCxO?abeprLL1bah7j;gg_2BK@JU~3&gzC~`fS=P1'
        b'9cFEXdo{Ml3%2OKUSm9_bVGesD_=)-qieiB@A;9WY|YH|(>!b@%CT9?8X0rPo2m>v1pg!km&tK_F+8LaEJO91V(=4k_|&X^F%^i^'
        b'$UEd8qnF5i8hdV2aWJ&yGTzjERJpuB*SXEmE}6Hj8?^B{Nnb&(nmaD~Gq5PENu;WC(vm)pl0&d=M!7Ac+#*AW6xegKy1YGj-l*c4'
        b'H-kdnC|CH+YhxNW#TP^y4H&ByRirblcgaw{dB*&NP<^YRMFMZ<!m@t@W#OqiVz7vc7630te+hqvtSE2IEOGP6T6fI-<pn;ihmPcT'
        b'b~ZDQyAcOUsk_J}Owkuu8%j7~X`faii3ZSxikkRD2*j=(Mbr`H?PmuM#Z`gvZQ~LPU@{dt|JzwB`F)q#*u>i~DS|17H@D1xD(_+u'
        b'!w^sf|7LJJbKxV1+WV!{nNL%!9rKE=*|BB0HWmQE_%L>}mW7BsNt>h`Fvx$3=(iBGeh6^Lh&}K#%Nqk+%O&Q(W&r)6b40jMXuzkR'
        b'5%9%<U)A4|NU0lVcxsOfE-kO0Wq}VySZ|SCd^5Kkdu^EEG!<BPOugTZ0%7_S8N(>=;`aleMOsS|e=U0xwc|(&4`}9KmQh&GK(KkW'
        b'%nf|Q=}G-NRadG7cB9a+lob$!0T<o0A@K-sY@|jKdu=QDEC8Qy0keh-SkA;)@VKJx4m<%wzsE63b}`<BhgrqaGS~=u^M=9ni#}FR'
        b'&tT~uL>uMXjRJYBz<jw32$B&KW5podf+2>LX(Xu{FkS<Sd0;I3l^xMDaTMT<FC^(dWidl#TP6LhE))z;FPY~;wZi?un+fk!tNY4q'
        b'r_0(nL=i>g8ywq7_@#wkm%aO8gm-9$o}wD!e&~Hh!s2Z+Q0wv^7g6zj7zP$nZ$cy)(EvF~?<9<*z{USnr9H>62MHz1SOKy*LuS?`'
        b'NEnJmibw!Mgg#irjQfrR>X2??^t0(E(710&>Ny^G9@F%)#l#>M!=c1Ofib=3%+^kGQ&~R~c$dV*QfgGT!B`R$lT6(&S0h*-9k0|;'
        b'NZq6#{gMpXR@TMG=26sZV`jcX8UT48a>raiZXe(TkQPqP#2_*gW$?w{ZrrMvu`kTJvUVpXts^B8hQY)zN$eOOZ?1Y$r+~`;-<e4Z'
        b'(>B6104I}p0w))y0o@Cdr4>)w1Tdq|8O-TrxDz+LlGc6-la@@|PcY++vVQdJk<2_g&5Rh(v^~khJB0?>s%;nAU{Ky|xowQhzs$0v'
        b'KW|QgZH&GRWDQ{~nvRL!KrE*167_824M-NaAhd<6JhN7r>x;dj%$=(=ZNON{<t559+1PBw@-$`ce1)k1^H3~bugt~IE+5K$erS32'
        b'(As(0GwYQnOSHKXEKr;4m*UtkTWiuPnaIr}&4bboG9<KY%rVS?aW`Nz_%u@e4mD65Q5jG)#9D|C+yTM7iaq4@rsCc2iw#y(pM?`q'
        b'f9Q-g1a`(Jj59{oo7B7Czem&;f^t0%NjlQ}Xc=iqXH?&$?6er~vMy#kXyFPAN%ATSmAs~4Bl1YrGPebzUq4#HKM-Y*yoRy#wJgIc'
        b'h+fYcmkD)Wx0_%Hcj@^@8~A;xZA|NbAI%-N@ynVygsqUewltCWiJ)18pTG~Tz^#`aaqd#{HWUS1)#qluUkYq+>!&1Ko><NaWw4fI'
        b'yah#VKCB$_bLpG>Y`6VKJ&jED{ZgOSbq!KtvVfAZM&^O+6t`w30MzFu{=T#eB`y_CEiEDljLAjBL;tG!9*Mjx33AI}>h6jETiSDn'
        b'^o@nFH$Z<y^$hd*(sn1X>E{w6NMTDhj2eN>jJKIu`ujH-(q9T0d^DFj>v%JYxKaS<yr+Yr^Pc5x45`nomOAXUA%{N@S1=+8P(Ad!'
        b'-Jh3+uAL`3%z=@(_Ti&HOm0hs2PHEvPSPpXQDAqnLplo_pOp^zy%y40I&hISv=kW_fC7g#J}k6;^eE(Hfl1HO$b<$zgQAU$Ho|Zc'
        b'h77}=sF1c&8MDtR{-!`7nV-N6`M5MReLnS8VOy#BvqItoqzQ+%!;@M{Wo%VC+uU4gJ;qtd&*BRQKP+{8SlVv!H-A`4j8j6wiMN|b'
        b'xMpPFn4<8$&OuYD<6odi5IjW-S*Ds}2xcw<<fvIZyFt-ptoejv-NXq3{5V?7S;AK}P0)&omZ2_fE<}Cl%-iToPy=(e1jY15A?!l$'
        b'Z`kt~st?*hY=LD$nR9SFExePVyE8SXEhdCs3!J)}aMe)SJ7?Rgw45@x6%R8^76FhXQSGN0gbo%|c~2S{!7?gF70}~FrP~b6%x%kw'
        b'qEh<t3nn!#iHQYpsjr`P;1r=LrNY-3dB9H98>D^BduoaG(`|CI*#nL8?b{3VL=233N34T6)eoj)->faI`>+t|58kW%?GhY@_2Cg|'
        b'rS<y|Dp7ZHI#K-h(z-VwlNnKL{&piwtVOBMx;3TPYd}fWsY<64WwVG?rFw~gXeiW6a6$<)f@V<=O;hlwQs$QnroLfj^DN0h1aB2!'
        b'p?E7yY=MalJoD00Q=`CQ)|(n}DojsZbSYKZ_Se$E;R1LMe@W?~Cp9{F=BQHp2?6+d95&OzA2<OskMpTo>&xw}g6Xo&JV#h5jJ36O'
        b'3ILBvv@Iwdo^yyU#<K;Nnq{Rk0C-c?c|<^|IiPg96(isFNdcxiL{o-u7MI%oR6wO4G76|9Vs2^s!S5&#)1c|b(1Pi2vq!1Tqjb8K'
        b'&AoIQ9NmDh6s8KENu6b0S<v;IiB6eCrvR!_--aB(fH?%4Vx9Te3&V4|o^zVGFb#oex6ok}dk)h9AqdkRL4gCl=iUNoU9(}*{gNl~'
        b'bbz5W2bRWsV9q#I_ysy?3cycP+Fzb7_QNzx@IiwmuEM0cp%U|z5(-@tO`lnH=Ss{Y`OhYuDluOydN%2JiTT7ID*mU$d}KO_ro*(q'
        b'sdciPrpN6j%5eNFAL24M67}8I#RandEV%)Q!@ktM)xK4sS>bcX>p4D9u}9(CBX-EQ7wk!h-cqI47i{ab1|lu21D9YuX%M2|utH7O'
        b'!`(SzTM3NH4SEmv96lp~Qya=*`?A76X@fU+BxVNZ2GG_po)e6<;2&OrruPbTD4r$2T=iLYe6_sKQ#8u5_#<HM0vD!>(b_C^lB!ge'
        b'9RF2rEX0j+xl!&SmPf>Z|GA;{OrW?5^tE<S-Lk_3P>V2cFS(p4+K+(Ra5;!8osWe2hhzNQjP$kPGwVPbP;EfC3{4Q1NrGY|rai#{'
        b'K_MkE7#iB+8^n-s*zt@&|L0|#z+)%}M<fB^M&Q`k%e308a14#}h1fYw@X8DqsCQrlKV-*?w-sR9s5A3kNW5D#?yl0Z%*h4IqGDuB'
        b'Vtt8iL&+Ay*5aBIJmT#Vy+L0S#nniFH+AnOYW<jONh%dyKG_gbI!orZqA|Ew#%K%yo*rXs80RuPp#Ap}Fc@Nn#Dr|u-@~2<0`@&r'
        b'mZUe>5u-3#ma%7Zvk*qlX(ey*MO#?d>^u9Az$JpVIim;21|c464{mG}a(*N)eb&tGbuo(Vt@0N3p5_75&daF-PWyOYMjP*9-gWiw'
        b'L?(tjAjZ@e@>UG@{7mZZ#9gKBPRt#{<R`1__JTK2)nyKTvPz}n7+vc!^Cf1qCNiaieTy}W0X=yUlB0=5?Qj6SnRy+2KW?H9w(zZ2'
        b';0DMU1JftjV^6QeFWks%H(eQKEyOwxZ)vseB`-HA{K6F{aYaUWs9$*a5mY=EbR6&v3Y_Fc{J6&?twRckaqX1B)`?gXxbT(P%;nr|'
        b'{F!)4v@+<sGbk)^2upl_G7C$Hh0qQdP2g^88k|$&z)BXvNIuj4>0w;u${1vqIA)c!n*z=35(0<C_qYMb@!V~#gJ_8ZEm?R1Y6@sX'
        b'_{^ok+rb$`+qP;%X+}jSS=KrdxKq|&NmDMaG&4l4OpM#t4QRo!{!YHhtmcElc;Y>S7&r-x#NAcflkLcAp?q})Jn=mGKja7ezD{7A'
        b'aIE)9-LKFpG<D*Mr|>pTqcHOh7|m2k+pNt0B@@H!)z|5<d3hGb3k(tx|1GATMwg+w2VkD)|Chape(QHkaUrx<(&5^SS}V{NC2eyL'
        b'7TX4k`%z*D8VLq7%FXp9zN7&d(fT%$(oNeX0!lX-Ovn^0b9b?=8`eAdR6YAlJqt2b5C3DmBgM8Ou-;KvZwV@aHG{>6i!m=53SU|='
        b'nwwGIJK+*<D6U$?9~TFQT?rFP%n)D@lO9*`HZ4?umvEy%yhV#Q3iP#<bh{LH7p^y$_Y~Xqz&1Xh*0^8`@{kXTb&r5=riJ`M?3zXt'
        b'OQ7&<W73#PvJoOjOGV^cMB5YQ+G1NRgtg@<SX*dV|Da%1&A_VtKd@BK!YV4Z6+u|VPr)jtVZBPh(oDnB9iM?En1Z$RSy&mxwhRbs'
        b'?NhMU(y$^aSZ~h2D*ZpO<j=q&Ru%jHZsfJ09X$Fq52HCSNCXM`Pi*!;Ki+Oeh}Vjzyhz6)iuPyiMuB62);>e~vvKz*+Ak@#ErEFb'
        b'<te=WLgVE|;T1l^Bxd9pf&u%A|7;(Fi*3OW)`A&W$sr49SO_c$-_?~6vSJGbsew0b2T>oEHWFAz)HmTh)8@zIGsFOG-pYHX&Dq7a'
        b'*|5zyPvJj@Zu1%}NpNRine>0e|I)Lt9v0ai76Dj~ik`rFR7AlVpkUoAnuc|-@{f3Z@hq$#i)=qaSYr^D?vd#uxha~ZTFkni5uNly'
        b'k;LiS#wJcsK(9ccMqd4aN+VA$_Yamq1Hg5Am=La)L_ka<T|wc4c{5%Wn1s{s3z_?iZ2d*RS)doiD5OJTzAS1#NCjQ9z)B&#MaHnK'
        b'2(JDorv5!vZCD$N_$N&74Qpn0p`-as8fzNf@gm!C3SMW?w4j&`RFwEwkwt=x7BMm2qUp6k^T$QDk6|AV7Cn(EZAHEhjl6~#&OA^R'
        b'7!2*Z+90}SNNpaZT#DQ%2&u`FO9XlY#g8d*zmb8#(C({^e2)pdMf1B<!5m;5nJe;4GX-<1r_Z?%^+j+V7=aLlW6<ybL8G_hb#!!P'
        b'Xf?_NbsO>k6+yZlw{d=-s%O?0+4NK&35YnnCJ1qV5fF@<5h`sX+gP3%VVS2%aaj?TAVU==eU0dqSmAa*!SeV6lw06F#X|0sfXn=l'
        b'q~7d9fZFDOA8-KOb%*7&S?69o6?ZxwRZ19%i*b>gM@V*&I=e`|Sdf+}NDISNcipH5BiO_n5F_plcw3H0F1nH-+>({exy%`StH|+I'
        b'k@+7*?dBCkHuSuq2l!7?v>ZnEEM$~O+L+uQ(Vhi})J&S=i)`^l{Y)YO0xOYVubND(FKW>00Ax=q@k&v9x37_R<pkilP9vn7mz|!6'
        b'UY<XqaZ+Sk6fh}|lO>^TOwn&VYZqCf0Kb0ZNl%j<$~LBSh%5pBMC*9c3#6_i@6Sd0YC&;>YhGwkT`wFmBRnJuJI;k4oV>6ijZu*2'
        b'mZzajT8>ZH%c6B|XpfVG#Ix3uoO6(NqKCf`^NQ*z+!_IHx)V(_c83}T)#pjj@NSZGiOf7sa;Saz(UT;-L2vzvj2kAw5cd2;$Hf7h'
        b'C~9X#hJ;{6zC1X4YZ*aeg_@yMvxsjsfFxp8kumhigb0Q2<erBawpoD7nF0qs8i5+j?7mcE(l#&f<H`Fz=G%p~+l7GV?-Wk+{9@wg'
        b'LP{(&pp;+6%?R*CryV~`rmqrEF5;dN%uPP!BTnhp^><)g=U++PH90LsW>wGd==nn1`9jE}7hpq*gQO`|9t|YOD(3yAp}>R*@be7_'
        b'lLWZAWWEn~_P3KzG)T9C-_k~s^O(%sLehJKnL9|%LlRK{TWpFC&Gtf@9rl4*RGgA?jzUV#?Sf<=It!<DWYGW7k?(1qk#lW@wl)as'
        b'<ELPKOv9?8VC|oVrMvil^jg_7um&W;C`m{wRo+jAZgXO@o71USpdS`Y#{xC`<OR5Lvm`vRrLdU_u3-LGVL<4w7(YufPW%fZA#N(f'
        b'TMf`}fom;I5EnL)Mz!R%A`IFr5oY3jsuiP*CquK`q3vRjgzBp(Uo$-vlz&|_r9VMRy(CokKu)b+&z!LvFbL&Fecii-FoJij-XKHv'
        b'cr|D19uZ{_Rr=Jt^Z~v0baW|NEk{&$T=Gf^C1$3PE8_9R1%*IFLsK*gwq)emw1o{`&5-q@Y7M>a18`&JP^=(tLm{;iV2>4QP6(oD'
        b'{~s#McwW{^Z>jS&X|XUV0VcHvFV>xmJ|V!|>2mG4i=!IrPrDDmVC9rosbd0}l$f|U@rjomF)JoLuMLe3gDIgo2;rfbS$|e9%1?_G'
        b'P~fSshEVVPPS3F*bp=zk*A4NAMq<q&uM|d$V}g>RESOJV6skFf_p^q%L|h>iv^f0|Y5q$g=8A=_>)a3$UD(gfc57xv_~i&A#b-lW'
        b'7#kRoF_Hj8<-|f36<Yj|zB8xuMmI8g^FH;K7BX6xp?-)lN#0SY4-;<Li_Hs<V!)t*n)CRf&-BD1Y618R9ts+f7KV4ulEtjZT37$E'
        b'#KZ_SG1PdW;xf7HC>ke2vfS2SoHh==w+ev2$cS-=jKLx<Z3F=FgoV9%CEOBjfa{!f^(ZGA36P*Ye?=rF7@;{maIvlz-|i0N9KBv-'
        b'Shu*1<y3QtGq7@RUb~nhzXo^yF~0OFkZLfl4-%r$WVyl+DoeQVki?fHaUZfq$lU^Yl%eMgndKKBa=Rei4^eR#qiGD)azt_v@XKf>'
        b'!;*o3K10%;G=qNI%`u?sroDPh1pCgxW_KPXekq`63)+JBOEK4guz7)QUYG=P3s~kp_<e!n`vUX#1?}b&#4xnH<bLop;pkbChH3)T'
        b'TrLEFP5S`UWiwDO(NN=TB!Wq*?c^d(+~>5+xF4H?u`v-&T|!cwVyjOTKvw369<aoY0_t=TQ3I)A<mh@jyc&2{J`!H35_Yym84tAz'
        b'ufTT?x71R0UUam3TB9JEQaSb6FbZ^60Uaf{Xyep+I+W!TGyW?ZUqv-~gnfT$vU)#kH=ZN<gcY-wYL`Xiz<M%H8_Ve0fP$u?j8hYc'
        b'Ht<8dHS#BGbrKm8QlynnTWu--k2d?#fgGbOBCP~bd6Ix~N(nRDHC~eWHiEgm$4#uNx*y9}!UfiuTwb8M`#7|R)S708hxde37HIvD'
        b'%QcSL0t|+|Hqwjap}?O!^RSDXc^Pe&u+qN4``K+Q>sfLMUzPfM^e1@cZIVOBV4vRniY`!n!nt3So%A+EXSS$;EnZhZZHyC(C_1yT'
        b'SN?zL+{R3N%Dj$9`g~*J6wR50dWz!S8~<N6CBT7$XYPQHBEG~sT7|~VNAeON8p&J{o164X0VPo}it5}eJA@^u%r&a<3Vg^Ih_6GC'
        b'@LOsq9CTWsvIb&>`1F8N$jErQPok#=0DeZqcy0tLcq%D^h@`M%6L;Q$*m0g38#R*mVgV*v6AoX8#60g;F)*$s3x}BQVroqceBF-6'
        b'9PzvYBk)t12V_*lH7hy6xy2dg_5<@OhXL443c<sy(FPJif2!|l%63o)jINj`#?mj_5v?zXkf<7-161gF8Oc^CBnV)I`*Eng1joGY'
        b'OBonXUyO6t!2`eM8~L^y`TZ>7C%Cwv`^~gp4(u+~85d)EiBhJmWdOr8NGM%~5cl(Cyvt4p0(b;&3X-rqaXY_-X8?SX%L6v~ar6SC'
        b'pWDU6_||a}{>%K9?B~EA(l1CDHU|8tC&dH#S5^sACCRAzV!o~&mkQR^yQ&BB^RhNVx^gr$MLCe|rHFbkzuknUNd)Rc?*LObjh++i'
        b'(bq`vNPe%d9YwI&Q76EB`kY!`oU-!)LFl+7YUF;^l5`V8X+mfzaC20AGXDvs+1CFdC)l^x!<>GW?okS)^x1rx(rl@Ld}fZR5tS?J'
        b'{?flB9nJ^UEmB0pXJW4K#C;IM+UsLvcQ9l;qgOxc>Dg=m=w1M9Jut9%bT_qk_|%;BjmH+$xCR7vKnvFP(Z&FSH)afsh-kMU0in;`'
        b'R|v2bz;0ORa$kbl4!;8ft+$)>0m@%(ZX1s(f3bbAF(CcA#QD1~4|Bmgs(_luF4&g6Q{(zoV1(GVbz?yNS>RP4tv`iz*tTt~aqY70'
        b'*eG${!+3bd4q$frdfEOC3hxh$;7Oe01~XE9i}aO&wrgB>NSwC}`;fTnr0<yRJ5bdS81b5KgROjH4Nx@0WMD*qZ#Ml^eUW_CrKTMP'
        b')~;^}Ko2DKd_~#{K}%!R-;=(*w$gl<_8-z_cn9>fx}U^c;PIM;5!hB(|1^Lm!&YQD(ViX>TW}xzKS?h1TId2Y<AAvhko(qmRu>OH'
        b'URC`WxiI-vn8Ep!wEeFZG~08WT$oKa%Q;5c-0}_1i`Xpv@g3ENr)V5xupql#@xaJJUtWOL>%L)uVTQc%ki0xVUgGcXK+Z8x<RzAE'
        b'yr2FH(fLl?LlQeo{AFXf>(#(8H*5!>QMl_j#Nv&CVFScpH&)*vv2(;v8^T?k#LFAQLq7%i0qsW#_B#^iFBlWA+QGR&BEAn`_r*wH'
        b'M5J#9@d5z0GcZi(yA+d!yKZ@v7Z|n~P`c+k(zl9`Z49T#3(yD$UAsgQ3-Tq-(YTxB!iXBzm4OjH3!h)egQrHnB7J#*$5GA@`Eop_'
        b'kQ=J1|3fZ({Z$^U-%k?pT3G)KxiABQ0%^S@(WjL-FM`p+Wb)b_J>8_Q5i`K|h9Hf`0wd=7HWGI2?)C*(Bk^4RZdX6w(%r7}0z!R='
        b'E^QneS(rlbLF(+l$T<rmi4JXGBucRJA<Y)%5GcsG3*Y8^3Kk=uhBc{u8rI1vSifs$V0})(x~H9jbzA!c*24V2!-Bzatz%qk9@qN%'
        b'(Ebh)1x0MkEv=3^$Fh3^G*E76gI`y&5!L%tpoTke0VbPY0q^jfCQTnwZVk5$9sLz%l<+t3sWZvnlDY?`X1Rvm|KSAtDNiw!3WSir'
        b'27pYd-0)=og~p{{>loCU`?bDjiBBk8JSkkxXeqO-0G20uwZX<v9^w)P)NE)xqN;*%Kd#dly$LYNwA0O|(ao|!?oF7R4A7!tgnUJs'
        b'tQ5u^0-3_(%?;DO#KQ8x6LSVX(mD=l%^zurdJ2pCFgvMPOX;}RH&A*~`XdAy&tJl)7OejRd@;)ChQ^_cNky*0X_uEt{IG#mUQ0L3'
        b'?6neC;cxM7E%j=`UnnBKuT?O`mt$jgYUADEnVR2#A)_!cGDk_pQZey0-7XQjVfszwqXxA41?Wj|79m7G1+Pjw<v|2dv?8=-g$Ax5'
        b'xkDu{lk3A6^m<x-wwz8emuW$YJd(2Xsl-s3ysikY4@NSeE5O(uCV28ur_nxLkj{HjFIW4=l%#jIhfTpI_D%JGv0=)acuH0S-ErUG'
        b'cHd86o~O0V(*lh-UrViea6lpI{abJCm7T&SV*}6Zr`2`nYX$ooT+QBE+o285Y(&zVgg#ohMD%F=^p@Gpu=|Q5*aCR{auT>{;y-JL'
        b'nOh_s5@>S~JZi-ftsW(hDz;-j@F>8ylObW+0qApfgi>V|!!p#_1P3Dho*a^}oD#GHZFU_PWJ&LlErg2yLWFBNipZl20z_!_5kz_N'
        b'@e<C_S5Q+FGzdknzaENW7&p?aL}we#nA-<j{f?@{{3=Z;uJTkaFT`q#ThN|Y7)E8S&49{k>-u_(HvLOGM6V;E;#sPUL}C>rTb>K#'
        b'7%pL35BC`bS`7NBp+R!fl&>a_P;jrIJxxgCRpL9ipx1CU<iB}@eIsx%;30}2xs9pSQ&Yo|Bd1g7-Qk%}+kLoV(-H$0E@GxOZ|M))'
        b'?Yw8}Jp;yeBkzwXLmOsb1AP3c@#hi*#NB)?ui<JWU)2*(kK$wLz1qgBrw2#W7~!*lS{w!CN~m(@^R^biCjjBet`4rz44vH&_&a1U'
        b'f4x3iIB-Ic_BL!J2c~9+09O`%z=fu4E^<VebUII0k*E?JS`7=O!1QD;7LfMzr|z4y)q<yT<DShuI-T2&22m-8(pUpo!hzL-v`ngH'
        b'Zo}2y!7;}HALU8emDR$M`qWg|JlpnBo<_4%Q!G4`B>*-lEXv-x3ce;t=lgP}Q?+O?m0~#fxkke>6$|xGYET(=JL`~6=sftHy+@$w'
        b'gBhpUvN|e@kgmrytV6|&r|Kw9;v&g&Mw_~Jqdv?jZ!}!F!b)qjnBHYjRjw}Cxc&W@?P2ySKL|8G0|vc^Gzzc83PI*|w!9Hv-U<zK'
        b'K5>j1f_L%=clbj_%pF&n9vg|oFahQv-(0nX7Z(rXrcx|O1a35E<>_ewK(PSDmjd(O*3WP!ooIdw@=;_G6e&q2TE5U9=H$FT)PAO('
        b'GVhNmksD@UhcvG5$%H~Vf~{t61f5BvAp<f|-3j8yoh9Mi>?em%k<*pmc-5(%ebGU@yMCJEF27C9m<0s`fZ?cf7&ODRh~aN>`#}V7'
        b'xIUL6F-*!9n-}Lj;Wof}rYwPeH6u~=gnc|`c+HdgoZ&V4bB5QZa*sZnTRolIJ4kV!-Tpm%vwpqV;hDGoq5YH~jphZqsS6HR7LH=F'
        b'@X!X~;B$EcUklQPVTp@$Dg`SYrJ<*#vFuqw6JX<~QBZ%i-qxs@PO_k0RKun;R&*BQ&`epbi2p5>p&ow+enY-WW&pMWk~}fYnXCl^'
        b'0RAgce0igMwIRMfZM6kBeu=AN62t7{VZ!m%48V2r7pc7rYSD?C^u0zN%K*GZFFZwZ<Ng898K6N#PZ|l_??|HOEmCPlQ;427$f<qd'
        b'X#2gyfqNKwe|dPI?@O3So(_G~z+DRnr)FytwQNi;8S?<3?fMtT8-!aL?Tx}Og1E$K%^!WqC;PAEn*aCyE3h9XATFX#c1WiNC|kHr'
        b'{2F8%;+^R#bw@Nn$Kcenn_FsSyk<zj29&Z1rk24`qD@ox*4xzDL(G%a&ln==?U~h23ZKD!8pl43d7tLxw~39=T7hea60}Ex9Q8xv'
        b'#PFTZD5Lsc8o1<`r8fk?<yMgwC!|ROv=`9}p+!k38$$|zXLA}v5uAZqKos?Yx8X_eu(V7;T`<HXIe+`i=)#jK2^knP8x$El;wY@U'
        b'1Q=J__7bj7FeILXzpEcZf=r!byD!n+_uDwG5Jtr&m1y9DzpEqI3V_pLR!AYlDJqn(yiLzHCV{|T@$6)G8EfDbVJh`Nu!4G^Evez{'
        b'MA{i;5xZcimHam5wv)u2T-Z8`UY{U-fnS`*BwWaTNX7TY_?XuR{OE?N`+kh~`1)F0uP;zFu<lFZ#_NUVRT_Dto_aM^-#n|{j2>vB'
        b'uKl~$Ce_A_UhyVggBS+Onq4o%^d^<Uz&ot8qj>Ay%oWH7eEPwh`X|0G#>G4~aHBI}TW@l~oabhuarxBn<RQtc)PL3}Pfe~lipITz'
        b'B!z1R(uKLJo7v-9VP-s87ov%(p<ZKcV2gry#0wgEu|7AO`1=%TIK*+-wWL4|RDFfb+%B}AIoi%>22ENIGi2P7SR*h#C?jh=;vJ1h'
        b'&GM<$`1u3D!q!mC<w}?^Dnj%3stR`991R>^ro5N|Mp#3SFtgsDo%H|F_U>^_U0K8MIVV@b(Ix@H)iya83{+bPDhbtjNJIpxGe9*0'
        b'UYZ0G!p#d~>*b++azY0Z#2Li4g0(Xzu_=L(M~JpXE%Oqz)KYjxY^SzXr<7@0Z=F(Fty=Ybd!G~3&b+_({k}iGf0A?d*?aBF+I#J_'
        b'*4}Hah|TH`?q$3cXZef{Ol(Sk+Nm$03a682=(<riHM9sp(#}_9w4<+wcM*(o94=I$yQh*-*`z+pqaM=P2wPfygfA?ssJOE!wOt}l'
        b'7q{$Xv^+3Xg^CxT5AtuHPcdOUnV5IU!q<Vkzqu8L;wu))cc6Q|-SnWj!eZ|0FxPfrLF-;)iKO+<bjvnz!8Z7Dhj4r3I?m>zy)W>X'
        b'vbh@oNfU2Fr;BDK)~{er=!8Yx^kzVo2yxc*X)j&L+$HShXGp`yHI<>bOk^=LvF@_^ZPu1khwR2~ByPSz)J(!N30+_l9FT1FY?wuM'
        b'kgMq5bVdXEYbUQ%PS5XL_~hi`(p;fK1v}n4I|2FwCETI2lMM;v7oiq#nmy!GmG|}Rq^6QxTg3gfmDaV1fvSdIbiPdl7rEvkeGp-O'
        b'Y6HOCoA8nJGQaLk^F*D(kuIp*stn0lpg=b#9-5hua;7Hf{j(*-E1Oi9osh6+T3~K3y>@o&<xPQ?H@RQl<fn4T0!E-{g|G{jly#z`'
        b'Fl0kNN={aQlzbv9eZcU;-H>e4w8<$PQ9+8?CTyX28T)xHdzQ|L{nn|vU!R#k`ng8a(r&(YKZ*;jaoCU?iC=}s+WX|5;d=$g>Z!K9'
        b'Eo;P$uhhUe7W>eSXTrMqmRHbyWxSD6s5nZByGck9!Ne4P+U^ireUh=7O@W$C?v0?iKeN0h?gU>9!n<?KQH^E8shM0DcRGClur9@W'
        b'8Hev#JzD|Lm$`UUL1`-3xcHapb;6-<LTzNuYkr_th<3wEVZE`NJQPkAZ(`yX%dT+ok$x^YUctP!3404S$>rIT9<--j-1}lB)ee{{'
        b'E^<%;UcvL&(oOBc(=)#0SG|s3aN$y1l;x?XsI4QJ1D^UrrR^#g69fe53+thH9qAW+Lh8?{-!$=hdY8^Q@z)h$ZOIMa(}-(!yDEp3'
        b'-SIehl-}hg7i_vOQ{GQYn@$TLd3*E+krMZg-mGWD%U;2TzD95!9%)=!Uqnr2Wo=!}!3-~Hirh%SGvel@vQIKz^<+5r$Z`><TPDot'
        b'D4QjF1JymcY0IOVvU2Rp-kGVJwQ0*N_8A-c2+>pbmemXK*&{ssE3j!>F)T-i)P03tUnY&I`#6CI|4!l0Et5*>juug~mPx~k4%1b7'
        b'{GF`T^}X+H^iV>Q%g~!b*?Fm32&OmrpKw64u5z+gaG{+;H=3ubrS6dpFj>20TRk8DW^=vVwPnlq8}a3B0z+q55)aGCNAQ>POu1V~'
        b'SB1xoP;ZD`<O^XQ6W*um76d;5D7=ulnaZ9#j_SVI=tHx*#6T|TL|34L3a(!vsJq+E^?m{!-~?p82u~z}=QcLM_+`FGoNLGwcMFu8'
        b'P$${=2G;O2;xsjOVGVgm{5I?Rf3oscyU%YV+&pqQY@n}@+z?u9xP|{7?TJOUhrQoaJl-Lpd}$q0tl?24SGO6U_~qIp9&huOrQ2Tl'
        b'%V}NTmhP~Ny!J86|Ilq?vf<m#Fni%r&~%>n9BBHM!HtIDaKN3WhpKoQRzbK?Ah0?aU~NiY>;=)-v5kRa8{PlC(NA@d8z4{HCu%u?'
        b'_VlH_Bi-XGHQc_}mYj10M(hB9-=kjuV^Xj=dvYJ@_H5jaQjC@J4)lf4m=yd?-Yu}aN6XHC?-b;GPRD2aN^{<&5ir^f1Mv7GxDM4T'
        b'_{&nTp?7JIiN8)Tbe!%Mc-Nv}fKsrAcjzHzt>=+LKhcf<!1(D%LKAr%1|XHi{gBX%hm#W6ALpKmOjn#O(&?@!b*0FSTb;d=&r8g4'
        b'h%5i1$n)PQ#mF>u-)y#u&Fc^|z|Au7-fQ3ZS)_R-GRiHWwt7psPM!P3jpH^+Wfv~1eHnBdo@rU#9iZOX2tIdUo4j@<QumXwJQYY{'
        b'6{1(q0%^A3J!qXnZh>5ts<4}vhp8fS3zH+2!}L340x-^1@Qb@_Bl$PjYO^9nmc(-wy7)N8Z=`D}VQncQdlMN{g!l77E0jgtePuJi'
        b'8jNDr;5t|sbccE#bsIL?xNJWvxD6lENZo~jZDP=%9;=*xfd)05gCmi18PfWk&CGpTd`1PsevHmw{O6pUwv~}dXQ~OrlZa3hFZC)X'
        b'bul+1F0yyYM){yT_yiMZl}cp8&8E%Y$m|v!HdgDRfeq@z@H|I6bUgX4)AKkA4OJIx3@q5_mT&ZXc9Z8I`*B)|hdE0-4s4WF@LeTj'
        b'4}&EPk8{T0VfOv?E%vQ#7?{`@SI~EbzA!wTaxWbfS@c|xC#<y?aSH7%yzx%Sp4g3D?RNLlx=VmRu{%j0ywdCn11%y$Eo!e|cDtO9'
        b'X;*wskbYexv)$?z=8Q92-e2j^-B0i2^u10J-$>+6>(7|UqY!Qk>APwm%rrg}MRGZ$0QPl^vk{LuJ)?CVIxsx&ekRyuvhFxqUK_|7'
        b'@z~o3vMxJPn<bM!yf=AMp5^kS{!uc%<h@j<WdEP+FUixc*9@F|50Cswi{ji%oTlb0mz!QX9igYteZK-J!_KCcE^}NFoimQjBEJju'
        b'W;y&<aWoMOo`TnDa-xReF&JGPc>;bWFEP95cnxG7Y%hp>eDW)pvh8@dCkcVEb{VxG`B_cf&nZry(1ns!jH2hGntnk_1<3vx{BAm1'
        b'gU?8@LK%slcBW=@MoK!PdQAJDntt}Vgp)Q>lalV^kZWQ2v=1P_L?4D@<Z77UMDZCuA#;ynWi_i$1iUl07{en2ftrgP{AW)<tX$0R'
        b'=92mFJ9)GQU)1F2WQ|(?Z2PyQH<_fvHQ#sEz%+MnjTTLz6Mlb@Gx#QS1WtZa4l*RgMUNe-2^^|%AFA<Fza^hy<O*)i1dTjRSR;O9'
        b'aqDnnH;5QkUFdLgtSLA?gAFrfxk~RA-M?!V%D4Zae6vE411~+CPkxmnpU3r33Etgst|W~32MfvH!cqytmR)qSL$Rv{k72|z)*g-B'
        b'eK0ju){o)U-Q0MBEQi@MTK_qH=ZE~S8ax&<bh)hF7>*pyvqs2kI94ePSiBt;@V|lJDP$IW94SqTB*L>7^Ps?38~O<2J!xwg1JFC('
        b'3pBiZyh6nPj%H(zC@N}jkqRR>)i5@pytGfs0kaGZl~2Zzm#Ucn(yBRek}+dVzzD`O&uy$Bzh)S_II@gUDX*=;G3}mYk~G#Z5}YR>'
        b'C)dMA_`qnrJ#S`FM?8UNYQ}bzQwJU7->cb61S|S6m}k{==9R4S*77|~u7HnJrW__eJ^ei&KDhNY0bLD%H@2Mt_8|)ljN%HIM?ale'
        b'$3BS3zr$J4k9sIdvxQs)Q|Ii*$J8}}xu8GK@js-IZj{Vm>bt^mP?Y_+$KK^gJt>!;m6J!Rne>SJ_V*OR@_kf_9G;;nn29lX{cX)G'
        b'cwz*|m%OdMMZR_9Z0qp#x3xmg@OPA|URL{vVr})Fu4?AO55j0Jkv*%biNjEr)D~uUq*9*Lme$ljQMDo(F6mEkxl>*@W%s9^VGVKc'
        b'fCZNB!|l7|y>0N(g+o1bID85xUx6v7p~&+A{P{GT8caPi0!w}n&RpbaAyTP7KV+d(cXirkhD@*C^K&(m_zOuZVgLR6s@JRcTrB^^'
        b'4R6Kw)q51>jQP^Ex`DN2swtngZBiOxyq7%_)%X?i%j$;H^uy~UR=I{Aq++|VMZ3sOX7&HQdeLo0iIQ;OzMazf>R%Y8+#$NLwO7g4'
        b'VSdHO)d{yk^|SSnXR3eEZo-Cmp8<3ol=+!#Vaj~)Z)M)A=1)OA4}M&^>Yn0Mbzra>pM^gTXzj^rmgXK}h}&PPyMc6kmO=qf!L%1&'
        b'Jj#J5P~@ATe0`z+gVodLJUv%AJ^fs_zdE=Z%$peHa+<ozp}M&V&5Qn%tcKYVn!I^5OS`+O0|%?ygwB|Dg)5EhsK#f&7d(EKyB&rW'
        b'ApZpO?{bq)w(`M_Gk7?7Z3rc|h5qZAR-mlD5&XXz`hTH%`W);_M0tx&Ypqsu5LrE{+f%KkkfPa$Zg;g-U9hBHOW^5wdaYEWZ%+5s'
        b'j&l%l7c464;-!(*o<Mdk*nRXSiP|Jhd$F2*L9`OmT+OVuY;x!HgDF(=+R*>j(El2SYc%5`^7-jDA!(bd!JhrwYDNcRh~qKVAV6GY'
        b'fw0@dIuWF5xs0;dS{=x$9@}oE-ttgh2RU5D(v!u|f`rsnvq9dU3H|>H{s%A9xkWO-ZP$)-k>&BA9W_<#=lP**%R~R^OqGT3_d<$F'
        b'ikBuy`FLd#f#Uh(3YhAhAF@qW<X5NVS7-Pm+54P|-0CKRq45qq=oXvUCT%PMTnnV5gEt#k+gG+fmcJpEM#M{?il?dx3~8RST#aeY'
        b'Cv#x4+=r}|K?E>c!9{5BFz0}1EWJ9AUhQ|w-Rae=oT5-ydk93f6CqOgBU0~qZqSD{pC6l79Y_ZGe#K{khg%Xk?v!fsNoE8VaFkDQ'
        b'6mzQ6RMj#OI+j!&cnsvsX}Cg%+IJ_z|06*mmNr^Vp~3GVX(DvY-6d2gmv4QSz_Dah@nuyvnk*r|u42)7FZ3UT{|affgF@L6@O~1<'
        b'r)fmNfvZx@z-h&p>(QvtLv66zx3Yx8!B&Bx>?e>epH3$+*zlphhxV$u%b~1BCRm|<;3}tJ9and|3Pz262`u$@PeLo3H)E}(JZlsN'
        b'Y6km=H+JMXYb6ghgLUHfMyz#b6nPysb#)wW%(jE>CUcqZ-uG#+qcOc;_h!S<aFB47QM<CgAHZLk2>Pb|Q!IJ0O2?_PcZta`Yas?6'
        b'<XQRlWeean5M5POVO16T+MqymA6MC%1{&u>!AxhZ%I^X{9Y;6y{<R7)p05EC7~Bt9{af8g72t7Ns@T)wzlQ$*@Ss6?D4v}s!MS-l'
        b'-N`DoPOdj$;$FB_%ObeJg@8l>#ApkXw*&)_nFZ_XU0Bu{iRJv2ZWsaM5!@TA>#17SgaP)q0orN7Bj&xa*2+Kf$LZjc$aD-Ra#xi@'
        b'h!{SFL)Opn$`N;WmG}3tA%8&&k!jofwAZR|{&o%?C4XmN1;1zMUM9q5@Ml`*23@i2ik%ZJ^l|$6<@>{CO?nd1ex9t94&I`HAnb}|'
        b'bg7`OeN~L9Fynvym8wCC2fYq#wSYwM;I&Vm-S_^X%Ke8bb~x_eiQZi$zsw1~6e}?E+`FnQFU3ZKho-7vee4`_xZ7FPIDvuRpd&WJ'
        b'EOa+ki6wHSBX${h{vCX_kg=;l{`#t*J(i)@8YyY7svArt#A*Lk)#PYQ&vd_71(rqdMTn#qW8HOC$`>I+=EJ~$+Kwt{`2GS+@DOOQ'
        b'F1DMatYbbC;6K!E#g-~Y^H_|n;G`zX%@hhR0ynq|oMLM(HWZKCD2_^sNlQ}wIzHWca>D&wRd5?q7D?(`lXTi>b$+d|Rq1S1jEf3)'
        b'IsDJ%HXw+5ZI$IY&@S-fF0JxzjqT<Jx5m1QtAf9c&AA5F-Rdgc>QE^ITMC-qBkq+|Obi#02u<S=#i}azD&~-YK$M#yz|FB_Q59nk'
        b'{f&+1E~pA_jCKE}3P_I7*Ie(f0gj9iN8u1h?x(Bddbzh6^xaYu>&~kZ7s`WGv9$rCdkL5v%Bt8(uO|iZixAlw)KVGi)>Q>7Vk_V9'
        b'#eqNfe^e<eVxP8J-~O!VJ+c0jc-t$d$t-4(9p@WP@(3a_sR$d2M%<}Y@?MU`8tZ<tDrf<9dBI~^mBkVZz63YK!lezKpQw`iIl(f}'
        b'2jzxX_uMM^5snhRS;}JF$yM^B9Hkk)nPZ_(Piuq_z_*&Qp>L*TKL-&xcjq2ORbyt@9(mQcPtw)i7S^7)=h3S6^brj?tID-RB~314'
        b'<_gGbElz>v<amrLf{d=hMXp4U*qQ#dQ?e(jYFs5rX;+0MCnm+nleQ<%nzY)4ASZ_p$K1Mol>E4oxuMwr{Rb*URh<#ZONJoLRtT$-'
        b'mq7b86XKNO2`<#B??+t{ry9^qmm)chM60Ix3znBkyIa`<mBnBi2eM=8GjgyG<d2IGYH59ZI*@qk|0$b|cnf1$xn~`;q`Q&0Q1N{w'
        b'd#ST;1C;%)Rrb_N_B-)#yy^L-$8v=iHk?V99ETQlnc8lwgfovzc5h(njX&|U6L2}58(96&&~27x+=u&l2(E{L`|1B3?!I5Z-TN<a'
        b'ZzMjc8>$Rh743!}$v|aKx}+%`4|7n$=beDUbhM)FoTs6A(Mubq@2%kcx;ub9<CE{gaR&b<;QtH!w6`i%9CG^xMpD@wF7xAU(o5LB'
        b'6VRRHJMFx0j$=dfk?rQ@IlkJ?ZNAzaqAgvOKK-`+(4kKQobh;c&Od3Nddo)3O=9y-@#e#FS(m_rJrZ5HVf^3#9@&wOuHd)y4U9f='
        b'QIK_Fz=gIeE=#6N9Ma9`IM6o5CCSaSH&Yg7{s$iWQ#$%OziHdf9a?OMl;I{@VKX)QZoaCBY+;&?0Uivre;0fi`hvdwD?H|#baXd='
        b'=Z>A*bH1l_85;^0Zpgz*qz&KG&F{PatFrgS%27V)2=)8Fm{W##=}~_7%>J;PY2CP2gammAv=3%!uVP!J$IbZ^yY_7$XG8CEmG0*%'
        b'&zcbVlzf7ck&+FJTpjMiE`VHU1B?vg-dO1kLkwN_LcZq6s!G<s0&DI8>j+-Gr?6IPFsC#%a{!lSWMZH``-uVh;{#+g1W6qnAfK(o'
        b'W5Jl=VLilv#|Fq+WeYJt*ig%_<EHl+MR6q<nPPS{0RL?WJ>mG{<jRMhi>6OD;NDbNsryZ3prEq1u<~0DK4a1GWNz>b^v^2d7G_rh'
        b'4xh*BIDH&4pFJHp)aB$Aipv=p#K$QJ*#t6Im}2YRDhS<aiVcq5!#P^+w7%$anJf_@Gb>$Ko-~x!Cv{?Y0urBv9B|j&X3k#|TDnrt'
        b'ye2u`F7FbLw@VmTBMG5HW5x9{`Gd;Zwky7ve&3Emp(@!1r8s9uC#9&=N<%sXJSO3mFJugxkqmE*I4UE^jxzPh1m<84((s5qvP$S$'
        b';^u~s$O9$W-k~zsmlPTFhH$E^XWBT^Q7Oy$j$L;?tQA0+HsFZu<yM9+KgGgYr|S%3>tuZK_l96X1G~dzsSm^aiG`_@AOnO%o?<5m'
        b'bQ-t8NA9QH=PSH3LusHFsRZ}}5369zObm!oCVVD74`1sCviF~C%#4Grg3O~6-E*PBy%cm*JU1-VTeKD9FrQjlxbk)h<rF{oz-2zT'
        b'Unv9M#J~8)0{fuC-E4i39h-(@Y)Ahs@BgZJkdaMNoU_3?onm=A`ir~@aRp=TlgZ#v;jdtAYkMoYF{cn3q03argFA~3LI9{KST}QG'
        b'#AGKVA*o&B)UE+Mf=aBPo`Y{xBv0$1R$vNug$Bd15zeeh*2j<cXIi!&@%@%O0E>4KntJ|C<{TUPwuhuTw+x>3y<CyY9pN(W8@ZO7'
        b'v@C_|+uDzkEv#y`4c+f_VQmtp6#Pru6i%YW`CAv!mgZE01a+IvsR#f1wnAqS_%CWRInChTocmJF6{aq^Uk>@Xn>3-o?)#=x_vuMf'
        b'8Fgadoj&o{wu->E3iq~(x$)$$A%{;s2W#%EW#_%3x<ZAGfTCbP3@Vi6GkvwqJN<)^WHrpGa<KEvgowAugL9FAE(zrx5XT|Gd5Abo'
        b'PMw#(&Y8!-BkOLSo3F*WyVB=z&%M0rj9!uguLS%&KXtxt0L-_v0dWL^<Ll5G{M>=1<*nFIIx<#L5m;5>r*<?*03&CU_US9V9j}S|'
        b'%s!&ywXhO>agmFtTvbvOpG^#kVK~5IP7)7|C*rf!C&fcSx-U5?+!p`!H-5>Oz9OIpkjmYQE67OL&GB85<IofK_rI!my6?<F$?X%B'
        b'2XDs1=*!+)aW}*J9=|0zmU1(!FZNdE?GxY6uQ-<9JHMjo564O!LJ1yztn!^0*|D9Ka7V@YnF}iFYi7oew0<DwpP^gJvB7fA*>dD^'
        b'wDK~2Df&~v>5R5HFr;Q$Y{e+g$yqEs6f>4s5qK0d=*6M)G}3#!eBh8A6ta9u56<CSNQqA$9GN|5@7H5-6@e&_t0`xU_SN-sKgb}X'
        b';h5KmPG`uP?q;2m7rZ4W8_duYZ|Dxr9TFhE`lp|fH6i|!F(emey%0(MY%3O42um8^u*{zG@`YKGPEHBOwRigL8^)uN8|tCW&2yqu'
        b'L%ktNlm&j@3R{*4#i}h=ZN&mZ6u<XO`P_W+5gSv#tdif4;Ui=@tXuI<n|5Jd4q@dLS^23)2cW{>E10kI`H}|Najt(TlKc|BD=yiX'
        b'`zkwNDGd<lv<(%4c|3BfnOS+Z1<T&VGTuzKEd~GOiHhRi<$Os4rUY!Kzk_Q9?r?;goAWb!c0V*l*G<8*Q+S?>jdDD0>|H-OX4^An'
        b'yCl3Ah6@}2$n&^)Lt#+s*YUV=DjA*ZvUmJBVZbSA+U-+~H%YqS6ma+3o_02MS-xWqV&a_ujSPFp%>Mx!`4^kqIiNUUv)3zBSUi!U'
        b'3i&2^0Zm@5c*|zP2CNdJVn8fKUPpWVHn8J|kqX$O-d-Dd*!H@p$2kDX#^;_nCHZ--e6|i!Sth@t)3z8@VS^(#RnlDtlR1hvZOIX?'
        b'#@2EHDS-gS4%+Z$M!E7R+_#;LZQH<73a=Yk_LQu$LbbX(tfIWQeD(gKw$)(wmd{qqnk<(3u%}j0hr|P`#GQaU>F`R%_Syn_ZGOt^'
        b'-fJUQL1wD)MC_-;xs>p+KiC4h!IupUH|f=2XXZhbZTyK{1pgblPgES|OtEF+VXiq98OH=A(WO`Ka%y<H!`qj&EnB7yOW@(L<!?RH'
        b'FcbOov2(uC(~o>}=qeujO*h~vaM}Al6z3b;#Vsvcuig5ld;a^rw4VNfp0@_<)dR=kJ`*MI%9U8o8M=6m3o9XtGb*GdYL}oQ8Z2bl'
        b'u_@26IOhWzd0!<yvvFYejJ9RF==k>bWzfk9DE}=ExKzkHnQVAmKSo;N)asB*#@5>c>urAbR`+@v84vrZSZni8&=nxLj?FV;ti%>r'
        b'1@b%(@B1POgRLL!Mw3y}V0%FO{S>3L;IKRzpz{T`Jq0#Azg<ZB%lG`o)@nn@<0eQdSJ*m*fb|k7f4YB;b<`S?tHFLc3+XA9Qz`PE'
        b'r{uaNHp6v<>@@A^G`YB~8&HNA2W5yYvY1=`RPdcwvDKMh7+1+<OYeE3kV}y_xyFsCaScj+qMN*-JM%aB<PG`c>jOOo-T2o!T()m9'
        b'G>IC2Z@@S*@O1*uaP7A2*zIGHy(zX%t}osh{z(^ae;bf`8?`Xs@bK`^tM8&s4m@g(2E}>vgnJrIWP_<IJ#&GJ+a8%CMB2kYh)>ys'
        b'NB*=B(^E+1ug)Y5WX{JU=PX2VZbAA$R{8+Ek{6tT44t8o7TW+mt6YPfrI3NrfitTHzK-G<uHTXk-Kq#LiQnG}%E8mM;q-Z7ne!R3'
        b'm+^DQwLxiu!yM<)<&H$8H4*O7&3(#mX|l|;$82(O+9QBGai^R)&m`ZlYNYnp9H~#HrE2Z=U4FoQ>`TW0eo|B^j{^h&Mi!6hNXHx$'
        b'(&HZhEN+k!Iz#Nnnx(;;^nE`w7BMTkv1e6jUzMvk&WMy0JfcI5;+&=v$J5zzy76*Q|L5h5W*j`SdU!?&uN9J?luyfmx=&!fv2sQu'
        b'UY_<bn^gsw6%B_Rxt~v&es8g8UO4$dd5G^GDu2LtgEiYJOpdvKF9&*lv|NQ=a?s!pwB^ZrR6d+L<neNbQC=4g_yhS%17mNM;|Y!P'
        b'Q5-MWJ222baC(Mnmc1FUCXI_gUjWc9Un&7#Gr?<*-`;b?Zkd7yP>}Dt!P+PnQQ{0~w1>cyburMDGMDtg8Qq+zlJXg6J8-P1a-Xod'
        b'3!lN9CF(5GeIob6bRch%Pu)*byi)GOnpJST@i=lmOz*@DSMI^947Wo*OucvM3nIWiSXKaX9bAWWqTX9H8|jbLEB&tAd-ow9+G&n*'
        b'`Jmhf2ww0<8s{EJfvRb5b&QWQiuH57KhO}eB^UBIUL(SIsbu-xpXkNdJkf<K%ImZ@2f7Th<RKSQMmhN7c%1TOlyLJ5`B2e1YqFce'
        b'L~57C-D5TtWH5ybW|zf{0%$|i@|648a_{YjVydh3IA3;FP!aG`^fAdXbSfa82&7)*FK_O~EN>v|M203_@5=IoVQ-~ug-9mim555>'
        b'5^#SYW>*(^7}E8k?C2s?T$CMCgw89<jw?dv7G=j4M>O;DqKYFbB1^c%oV<t;ULGemu?UsMXXhp621>K@0z(tDO3ECfGxTGj0?XCo'
        b'0y9O)xZ+yV{342;qIxE%GcZVA93A)1i-P5IK_k1l!TpFq6y6#TJ1BdT%TM)m3+Li-CxA%4%?MBFM00UZU^BTDzQA}tn>~S4a`W_C'
        b'Dm>1snSK+)SU?riZv`-?6}}Bp@=#VYd_9YbThR#o-n&zyGk5ttftXg4_N+-WVag;0CMI^4_N+oPp~$?D;=p3gwaxHgaUEKL1B>l)'
        b'HYO*kq(hT*ZsgEuxYq~7m1if=BZFXjMSJe@c3p%fG;bn=V!i|QHxYzsK0m<DYaezf&M9h(I}p<zb0FCj<|M+MF2cJ?HUxO@b}Z*M'
        b'?UM3uvw1y(n&2IpAVjiSu6po}J`tImFUenWX1)YaJ1EJiQ<un>NyGK04tY*x2MghCRQbUH#ow)zM<?%cC^D@;tRxN}0?(e|J6#7Y'
        b'g|g{6;wLcApg8Me=!#W2g{%YfvAGoIs4cOxCiU-Wy17s(dYv}EmyOpyU(ZeEn}@iXrLuG(jwJ{183aWqOOit~3s2~u0Ve*7fbBBu'
        b'<n{Jj6NZ&bWnk8x$16k?_h(iNoLOdlv>BCHWeXgrsvmRcV*u`-iU9*03R<p&R}`&o2O%-q<Yu$Pj7n93N`gN@Ya$xHfR4n@(TH9t'
        b'Ar9ZmBE&G7D<L;MZX_%cLK&mC#6ojYpAkllC**`Brob!L>a>MgllOnX0%_h4`UmD_&JaKv$OFCO{*Cr1xU!~6jVL$n0GQPWBDGwN'
        b'DLh?kvMiG2+@$k#U=?c%b0CrMSYjJOa<GTsOncT>n$QO{;h}U(*+c0*HM|`Vw4kB8G+-qzl!fR)fqg#o`FRRj>;oQgMB`I?YaS~5'
        b'zxl3Q`OtT;!%JNRX|ih7E^K58d1Au@UZEQcJ~>@aTB(&tL=0-Ica_ycse&o81Er+FnjGg6C8s23Cg&%YCRZl!Om0fv-^o$2J}^}J'
        b'1GPTFDRQb9(^*mvmrip&Smn29B;*s=#_8tRlE(Q66IkmG{es94$M0PP>acld%W6c>ig=j2L$o7qNB)k|9hEzF?r7Sve@EAjD?4u2'
        b'R*GvYW3?$Shyaxbaw+up_X)jQbl`16DOXd}%&Cab@^Ow<rqNdvjc_XT8gqQQ)(r1gm<fTb;ZDY@F~+y$p1}m=qcQ3vq?@ma!1?1G'
        b'B<CuP*peWPG`=Z!n2_Kw-OX1%CUc_v$p=2G$uFLT=k%0#1=Le^XnqZ)T<;{<m*?!)1J;X^j4H2!t?f>w57me?dja4+l)9iB#lQ-;'
        b'z@YXQhTC3pqRnBhWY9`gdyHnQ>!lHnYpe6+c&F>-S(83g)<lD%5uj)&?m;LX))jh%sPHF?ET3O2#rX%6&IQZb!puvh{k*3=-iVlD'
        b'C75$Xvk_;c%))g=$!y#bVX?WJ8@{T<to#e0nHH%mxAxsPin*XEMM`X(2k~?MS>{Oe!WA$g{oEiPqvCdRRnl>caVp@_=X^_-6oDTk'
        b'cXrMsy^h-u@{``p2~HpyVx8#FNsTn&17~8Rc6PifIq@kK<NX9kA$mR1lumGPd#R+LNM4d2@)^@RXz@^XC0|Bm$|0in-&2OiI0&>^'
        b'sEu)Pz|@RzVp{2lP>VSU`zi?-6e3H$6+loWmZZlM$%*`L8G8zD@H|33W*j_>+PlO~?9ld4Re0FGSqbCEB**)Ra6Che_dV6qr|Wo)'
        b'JM1@{K;qknexjW*{Ok06pRj5Ik)<<H()5X_g&Wh&Q6jR%T!x$?)Akdgyt!B{MaxccaiMMYI$^gEkFUGiC`%k~lk9(aFbvN)5Pmif'
        b'Ul%^o6z>ExeOtoy?r@oshECuS^K8^`92$UdmG`1SyKhCU;LDUh^Ka7gxH;4QSn6)7^@v`N7U{8CJ;z13)GocN$Yplb_VW+O@H?JC'
        b'A^EY9(Nj6}(GaR$*f8zyfKzv~?y?pPo0b4eTHmUVbWJ$SkEqRJ&tSIl$7r=Va(eAQ?N4a-9HvRDW!e`mi8$4Dw>#Pv*IjN`ccTf~'
        b'=UqHUewb$%bsWA27J^gXjk+WbEYhJ90%oUki-(Bp11o&)3}^8u>mM3mO$}jnPB;c*>TcnV=N+7O;nPk&dp75sXr*2l<<#A7)Fv>6'
        b'+eH2kvwED8wu-qk>?iEwVGqIZ6Eg=X49@q-Xv6TmwkhX?H4Jr4wMymj&iMA$BDrfKWD^Y9eLlQxUncH2EpE1{^sKu+#S<22AOpU)'
        b'smXa3YZzCnf8Y-g)E}VMYeap7=C@#lEf$4p2GpzWrpGLHO}M5UW)2v);6)lvc6fd=Rd=g9ETb(^Gf_mnSdd=UK9!$aG#Ha{G>!>%'
        b'$Fp3I9w~LARuwOAiV?Z9!A5{HZX=n!GcX&F)gNi|U<`}_!|CQ*rlJ8?)y2ytlV)QL^AI*xpZA~9hLo^w)Z2yBDp37kHdy%E;<V7l'
        b'^Bm(e0miS3)=TB#+4>^6UaE)({|dux9v*3%%6Jv}xyYQKJCSh|8r#6-3)cL{v>wIs_lEDtn3D`E7j*O61C}e%ZGme$oupMIZ~$;l'
        b'N0HniRfKPg2TzKIA8Bi(gmnQFJQppCyS+}-0H`Anj#@ql#Z37;8q#xWI20q<^0(-mi!{Q9RDrQCuF<lTpK`vZwG+_eKNy45)U9o5'
        b'EvZJ0I9NLsZtWg3x?!>K><8jAPt~{Vs;>yx>tSS^3o*w(JF~0)qHx4%b36HF>V?L)d8WT?Xm||qO`V>gG{5ywFH(ofI>$VR(XLaw'
        b'XM8(jVAtM)t9!o@&UTVrKB~X|z@KmK=@)*>8|8MRmSMV|Gl~Lqdf%lNi#iq_!DDez!G0K*y8TPrSosl8d_5d}&tQzJH~49Ejp#yt'
        b'8){9S3%yr>P4{mg1xyi+Rt=4>U?{&9#6JgpCr--TxSyZ_4|DsjrWYQSB4-8YnQr-6(<8w^^jXCt&7~dzmf6+W>m)rC-4Vm{2$078'
        b'XAdmE@9cU9@Dd;+xqUrYL7#qaIR3M95A2ceK%D2)Uq*&K0#4)pj^)Ih*V7svL6+|V0N!~y-7nyDytc;~cn89o)wsXmTqI#5nUeNb'
        b'#a-<qTHBWf{!dP~Y4ZlHu;DBuE*&p_rgCfH;XTBI(YST<=B;2o)SA$WX-=P)HLx|cXDb_SGDwe<_60!KKc+)5%X8IrM^fjDalx*1'
        b'T(-GUp4w1vPu&U@z_z_Y{V6PKVg0s<S<J%L0IHx#ALX4t0oK-v>4D<{8Hxjl(O_U@KL_;NI~ct}WT?DnRzz8othOmDA5)tjF@pte'
        b'H5bX_)6LY2<$K3$>bh^X$uNE`g7aZX7_jRvuwYz#Ehw1rRK*0C9h!-Zw=w>s2vhxbhOVSbwr9ZjE~%L(#s$cME}X-E7C{V#+h(w0'
        b'Kn;q9ujzPe#;ct<-_e>t-$W88Q>}=C(R_JYU9d0OAd2dn7zM0}(g&XJXeIyyF`>~}69sCpR?^i)ay0-1{uM)C(1@9ssis~`U09|z'
        b'#W)VrY6@PyE>Fk!X$aHbZl3o@wBh_Cpv@zzaarBXoMglr%`7g<Uuc8q1|X84t<18r{CBkB_K&rS89)Y6Rw5nI5@rpapbh(f*v-LZ'
        b'4RHukJD5GnfdQ%n-bUIGH`Om1gfGG012)Qorr|Q>{^)n(%&2-dr}Cq7eX4#TXht{BVTwCziVb!}I}~we6|sh4zDE(2l!6WAAYjLW'
        b'2ga%O@{D&xo8Mv9?@<~QPj48Z5vvdz`aSHH+7vm6rl~2~kEW_ksFs~P1!n^qIB(*-0kFORaKn{xzap~nDJ+MCzTA3f+4(QD>J_4f'
        b'7ia`bBdfTsJ_BHNC#{*PrC!K*2g}(;hXzXNjyB}qWoE@}Hog(u240Ug9RG(|!2^O=uo&r(&16Vr7i}m7h~a-n1CC!N<H0e3yPf5E'
        b'+AuusL7^bvbwwXK9$#O%cVD0K!7#L%VlDgOFtmbUD80c91AB4ZONU!4(}yn8@y>=Ry6*PS7|o3TLAqfN4P&ReG1(G9)=>%0)tkj&'
        b'Q$0qkL+ftnsfg!a;+mI+#jnZ*oNey>xii4N$OT*#&M`F2R4b4q4mOmG^wyWD!Or4Af;*!Yi)8sT3YN;v=P@vIfpAruf}HgrwR1S5'
        b'oa0Bqw0%L;d>iNHsR2*2BWj(1jZ?jwvt4Kv2)4&03FbOZa~ow#>OdCgN%8q8jk@mCvIt?u{7U`do6GiY0{uBfuM-V1%<Fbll7P3%'
        b'IW$Eh+cil7{)bM6sRjFH<Eww(a$&9hV{BU_)^LI512U#o2*hp}5ThePpgugQMRP9E8dOi+)v7fTtzL}^Gmbv0)<-r>&~;xei+IJ#'
        b'!GMre2UdE+-)JyM=+H-WVNqGmS$d%x$(?flx-5yiFgHDko2(}uDWYCj_7>c!2AN1kfb4q7XhS7xBa@O6Y*Wi#6@zg{p;O4`!OUTz'
        b'PsVRp!RJrWVz7I0!HlYlHtf82`XBwM=VZ2JHErm+EAEBIQ<fdH;mRE|iaDqk^R4BYx8t+RkDlu1jxvWl+oK_OuG~h;D(?Xd<D!O3'
        b'43E%<HUB37`eHORlnn8Dnj&{%*`YFx+HrWYExj>T;U_pBdV>EM&CHS=(S5A|5}3fPxCoGjR@g=+K~{Q~e}|1fh{($3fNJ$-L5ahA'
        b'i~g{-TcEr}o5W>xw^uKGWYQ}stvvIl#Mm`3-X(dutM{(iTN1TfbSUNNrV>%O<#pk!4QO|m!z5`niGwD(RUr<ywtleEp^yNv-%Riw'
        b'X1>h8a}3>SRUwlu$^N!8E=h}X02*mFye`})i}QRi+4{jD7J%g$8WaRDSO=m;-+&2FPLIym<uENa8@t5j!-tHl#P72dMcK?USwiVb'
        b'oDWT~6o}6Z1<}f`;9qIOPNB~XNRP40uC&q3!+qv%LFEaHExJJh;I<NoLxIb7#I<z7$k}Y&UQ4L%YsY=Mj=nigvybQtt8~V9T?=o+'
        b'jtSdifFu;wCIxb6m`mD8n1@!zXAh0jZL!c{pDW%K)*f?A2pg^@FvAf<Z4LtqGRW*q9s&jRSe}J3KbmiUdE7j9+}wNIyl5_Yf;o=S'
        b'6-yy{Is<h-{6evX&lnAdyU_FWNS7_3Mx~YM+Cak%I*IeR2CHirL?s!Z=c$MzkyGBr)kF;4rYFz{KPsN0=(7PJC3ttyVD|!fe<zFJ'
        b'+tOFdpgmx*wC-!?g7UT~K=4Zd4Z059YI}>L!Jj~Bhz1kqJSg>JpA?k;9~!zSqYU-sQKG^>m`h8`qp$`bZ*qdGXhX^r%VMpB(@o$l'
        b'idGeMa}9%&?*B431Zd>prVLU#*bxV)4uif#L0iw$K;mzBhekYL9lk{`|J~{Y7~rrNbPV*0f0l-AJYF0%^fL|6hgF`)`2({KMlq;N'
        b'wEPB8EyB$^aN8_WDk{wvp6@l7J(O7ac+?7zjyCV?=LLVhH;<n;ZSyVn%LgeglqibepzrbzQeyHq@X<dQgEy1Q&C_xQJkuJa(7M~?'
        b'GB#%dPA-K{Px<i#QvXmsc$VD1_JK|!E#KUmYlbJ#VNff2Arp@y{|e<+P`*<*veT1@cyVM}hY0d#nHg)My=&k-U`(;ttindXnk9d~'
        b'h6U=xmc@LhBKV=ZL52u)Y=Jqj!0cXV_EYubz<S0y=D>uL@L?`a@HXAN(;3&S@k!a6*{{O3K~I{nj)&R_O)hOrog)0bLstqP1<im~'
        b'6I)=KJHd>{w27Lv&M?Pm)P?1VTtITrMz+sp%iuhg#>4iD%^_p`GWZ4V$5ZqHQE#}pEyWq$(H7MnPCmDmy=7doCUjS2cX*$w<F%XZ'
        b'Dj<3=@ltyJEGIc|RGU+Lq7f#Js#DY`<@!<p?tO6~J6$l*uF?4H1H(*!m7h$EHsD$u{xlflV{4hWk$n6V!^4G-O_~5-6i$9;VjTFb'
        b'5MKE4&|Z9)d>l4Hw)3twPQyzU&Es4%UpuNz>Eyw)%r@>mX-e*FAXI20aV`+v!7ipzE!%rDS;ZFs?5K!_A85^NkbO2I3>(Vss%9^1'
        b'`<$>aQPZAc#+o@3McrpjI7a$l<)$;HT>hL$Y^V_48U6?+^`@+u2y8zar~^_6EE#TOW|W~+TB~?0?Kf)`r%ag{YSUvW+tzWn?G=Do'
        b'o&zsn&jqZQCs0gYE`>)Q@0waAbLH|M=d?oxPI27CJfDS%;bKq`b4rHCFA|ZpYZ>UW%Afc2n*3;KTiCI<c2TP$8c%4?Y*oax=eMG3'
        b'+EZE;vszlXt@%nktTkV?=hCx`hh033@+dFdzV=zGUJ13G8$5%N<V6Va4!6X=4pX0$ufX`9(1J?d024EYa_e$_ppoX!-TO?f3K`Wd'
        b'c0abZqkRyMZTKhMcC_7}d=&a^MxZad_cU*H^T=-@O4e~2ex|`j3A)z|Tb_UqAAv7FtYL@d%AFFx20ls#;9_#`G?7K7>GKa5l)!EZ'
        b'*iCNI<fkghpVvW>svbEA=Km+tb56I>R0Os0<PsC}^}-VHtYe>LOYUm*nj=~@U@o25>KJZY#J;vTrxZRV?rRhK2$|@v|70YY$xNR7'
        b'J51hx!ns>mVsi4DKXn{Nn_4d<H`O;^f|Uiopk-b68kh~%Lq(FmhX^Aop=UsCTyiFkCFkd*SbhXs19LYrL`VL-=E3@eefqU2@N1KM'
        b'xykQNBZpw0RQhR}!%DBgpP=IRyz(v$eMpe6tqGaggFF{`7qGD`Qy|OaehL6MO}-5Q`1B4pmXY~r>0XDMyDwALr}kk4raXRRWNI|L'
        b'pGz(@F;>@%g_k19<Z$y<*qr^}jdICUQz!xuq>bE*JlH;!De$<-JsW_(O#TsqKdlD@J!4Ts>0S>2zbO1P06%<^Of)@2S3_lEO@T*E'
        b'?kG_9XYvpKhq97~%8qhDpTbQ6iOJ13`8_j95*BP@3Tox~^`Ky*HYUq{^nxnYeiUkxeXxVakC6OnD9qS?D;Q<kaMKt-Ozt0ze$Nx+'
        b'MhI#<11ck(1(osmmamOYY`ehY=5K3z)Th44?@D*CSeLr_$DK#1gJN<PoQfm)D*jF)nIDSPv>WT^K-gaz16Pdhi$=fukK}50=m|LV'
        b'kCpBv;Lt}CLZwf5L4R6vkvDu2aF^tH<NY=wiua9xMIqe$ef$3@{$4&2-~vW~*DX}SDFe93J_+MI>zfh?7$xt(O#pDuFg_+=GzhMT'
        b';9TT*??pb)qm!qND=-{e)<<}Meao5IIA5&E$73^{jYns`j^)71jYwuT9=l94*&^S1e~;jj^7V|5Y9rXYZjT)^296os$Bb(~Cy8|r'
        b'<|^qo*8S`gl1GgXrF9!YO0RKxjiwzo&PmKC|J%r1LQPfc)E_NE(j{aUOh{D^q^4d6Y+hG7`KFQClt?f9&vNKMYUA-)Bn4l=b4Pj{'
        b's}oK8a($*cH8l;&3FLnGwc#hgm5^=lF)g+<BkmK5`WWew0IDcYkuyHy@9U?7{{$i#Li*M-&Kjo2C^*TUP2qiwtzpWOQK8YpeRKLG'
        b'WA(;Bz0qB7^dB51{{hLLwJ4Hwz{(cgOc-p8`^cUmhI9|PQ4~SG0MjpAaqlpuq!1Vab<)cJ6(u`=Z_*)2QB4vOV(<cx9H!q8EQ_M{'
        b'Q1X@hf6&Z1+DIn342+-0j3}y%vL?hkD05H<rP|B3FQFg03nVSmGX~l;mKo=cXfQmSpip>Iy#-DULMJ42VqBkWB8wS)tP~egj(Ueq'
        b'OqMcd9s9dcLYKsTbU$P4M@a+I^8JcJBOoX%;mgRdGeT3;m@Y~qjIN?&4#Up6xjC%f(!I>+MUaQijdP9oNG>OBnGp~7oaB-lOBmkA'
        b's8zd&yikY|R)>55TXZW!i%-@|GM#CQjZNte4)(zJyPlZmr`{Ol9`^&Bo`*mVh{hHg0}GArg<w&sNJogNcoTk8JYnpJMDr8bJCpsG'
        b'hZ^vk5HhudA&3q)x>(eQ9_ZSWYz!nD!Ja1Q*eA6%&SHEFl`>YYD6D$CQ8Mgw3Y)jbZyUNn$2Ypd$XUkmeL!5Xd#E?GLh7JB37bRS'
        b'En!Yv-(W5W@k<y*H&HgPsO*W_vL_p5M|bcU@A&u~Je+(2euhN;e!QKFyl?qQoX3(PlJJ`u8pYd*ky98l_ZFZI`~EaDbANbyYZ&rV'
        b'EZ6eG^r<(r+P=&BWg;s}m=j}sCJYt?c=p@V_UpUB;+~_5P)t7C2A=lyg(<#!7K&I76{|~jQ2*hfkU5%&N$5ezuK4oVCc=ZENLQlr'
        b'4jt01!#Pz1E2zN~e}5L|s<7RnWVG(5dED2z_^b))jk!R!UbYvou7&5G9iJ~LO)uuiUg4^h^D;C`;t%$RQT_FIUc2%ZXc^xnX;*xf'
        b'c3C%N;*l5}VyC1{@oCy6-Oa)am8l*e1T`KJroL(Sh>)N5^D{a)FL37Z;<NeFK0=_P;07(Pl~a{+oM_(P&+-19R#``C*E*5~byE#8'
        b'M8g-9t?n0jlAgH88|98;fULYaEYSI%#W6q{^B`^B<9pUaWwp5E&o@2g4?~d?iPrEZCTk@r+jcr@g-BhnV4Juo>B-t$q$n3v=fZM}'
        b'o@FT3D6b!a%(+6x6Hm2+^o1~8^}KB2r(C{Z!wgVsKL=#M2OB<zyfw^whgLp;szf>G7+i6@m*^TMw)hy`Ec>Jj!S`yhy4ws+ow5<l'
        b'+WMTIX~0&RrA!~#gH=ez;mrr8dhq-M9Xh}I2MfzG0%7fc2$nMmf@)wvJ@Q~U7;<<YPH6sdEMKs2g75!(n->0mY?Jpqy@KiANxC`m'
        b'lbtLqK$@LfAt3%8TE!KZ7gNXOp4m^pySB@pohJeV`432Q*+rlAEL`-6;1X{4a}VsolUtl}#}a4(_BqUybBzx1)A%B=(AE}1?>{#k'
        b'OHjuWj6Z!pgo%-{j){eSoNkW#mp=V&x=%cTc?Rf{@(E^WhQQD;ooTqv;!1f2z!+)56Q_$pc<;~-WthQ+fZ>J8h<||rin1`+xJm#='
        b'AN~uBZmxHj?uZg3B(k?~V4!=iT<HhQ8a#;c_R>x-GgLn??VC9YVS`x(V8erWc;N;<Uz?r-?}73Dmo{3uX~*nvLvg5$aKytw6PW>r'
        b'p({hNK-uzve{bKw|E7Ju>GpNd&iDRbw+|PA@p8sN{R=Ld$9>>CN2Gk4b~Zt6)C2a0&3}}3?gTXHf&Bt5vK*nEnGgn>9-?iyDA-Fo'
        b'QlePk52sstKzj5q)0BrnT8z7QJ?PKF>0U5aDXRO;V9Or@X$k)hH`oQzXFZe}YO|#iq(AyE_4z>BW53J`{iRjtb`)CPq#X+JC7la('
        b'q$J)fge#NTx*wG9b*^_i*AG%i(EW?J-IjX~V*E0GvC{18&#<vN(q3GT$G}Tw9JyvM<IoQJFTOdakJ(<y?dwyV4k2<QcM_CqxyosI'
        b'otx6G*u4IXi;2PE-n71XuU42B)6qHxjpI6n?J=R4al0`^<@%)J$Q!mOMfv(9O}L_Jz2o$qRtm8v?`2|(S=J|QzpgN^e|!6PiZbx+'
        b'CVx66C?2|3U%UDN4=8hRoY=b>pY%YAGv>zjCvFtyC21BW<u39Ns3imO5zSYem|qw+c|yXxDi<Pt3cqh}iMtxLAA2=2XhDo1!QDs>'
        b'bD1%iE`y#NlnZ2#tz!K%;lflV=;DR#@}~L=s<sF%2Ct3W*fH})NnVmRGAZv#GIKrPxbR)1X8pbsd2qL1yURNd>699FBBXjfV|(Ro'
        b'Kn!1Ta3Lg}e##bn9DJ6E?ggJhSQ{cgwbh#f(}wSOS0eCMIZPY3B*V0(pOu@DobPBqC(J`(N)_TUV}`h&yD`gm^w8H#{IA&c2QVkr'
        b'eA*e4R6PHNEj&pRo0O|y@tm|>{r2``w|KqP`7Iva5Qg}q!8(K;U+_2|VGcg<c%M}HYXoq!AP>MAe7C4%tSkz-3paAVjvL$Y8^upP'
        b'r~`MoZ>?+8{@{~(tq9X!0NC=}gF2psbpZJJA)40DabH{a3uyBgXpe=U1zBj8vis1Kn;2*S);weg!V2cV4P#*dDLlVUrWTqBMD~eb'
        b'J0WWn6!F8By_Et+=bwNq8RGb?gAwl!@GX<qk9K1~x&_ZWxf)E*5iUlH2*gZagS@asRo(o7=k4S<1DI;X*xC<4TDO4w*uZF}R=+&E'
        b'8&h6}v~E~~_45ZgVc;EBvK(IR6eFza3MqZH^q?aQT50w;QyqCo=|1oVxRLl(6!Q+XKdh|H-cM3=t!qBsCTiZ%meQ<MUS@fw0OEdQ'
        b'oootBbD58mOUPDoV8e@qVajXtwI<M=ar#=E6DvJBC}efP7cz6Pesqv41aDu_Bc+U%{__3%jU?b*6@OSKyUOWCkLken(Wk=`x>4^K'
        b'j0wpQ*KSmK72eFrALaM+K!2`-myw<Q0+0@s0o^Dx@;%MUG31Nu`Z-SFFX#=qa~-s~xlf;=hll1P<a6uraK`*~+Lq9XE$7<{R^~fh'
        b'Sb=q5Ss!n^G=AF->ATAE`Kj>w4X2>XZXA-6IdIhVrv~zuR;DkXSwtb`!vn?*;_>I@hW8P}DLyV7k|Ov_usdBwgDVjS5xcAQ5^4an'
        b'D#l@sc9>(Qh-g4y@R&(g{axYN!2}q2p*yS{RT_~tbhilfEX;)}3y@$T;zVVAx8cgQ#+(KlgvT7c`5pO$39+m|E};-##9)H))IjBt'
        b'QV%INu%?5skAsvA`VuFfHawtB(`iimL;FuFg#sxn%LOS3V+KCT9r2~Q>PL!!yvWRX5p#_N${6qjfk0bUD9<=0Sx&j#_uQF0iARUn'
        b'sp}pc>d<lQK3$gcIfss$Wxwvw@v@vchmNn;30mwc2dV8I9kytzePp0<K5vlHfQMcgz>D`M=uvGa-VA4v_Zzt1cO@*}1x281t3uI3'
        b'{;#-E-N(%rtNu^8;R*nuyN?^?Q=mTy58)=xVNRGL;=q{T!b#U&4-pU1qZ)-ly)8M&ZV^c77r0PBt1TLcn$rww5P%ynh~Ogt5kgNo'
        b'Ko4{0fEZLw<EL*`$jbqPi>(YU{;}#|{IF?%hiP~$<Ne=Zj$bSc;fgg718o`Q&WYrDS^WI}ftTL3V5#1G2roevFLQAQFAWdjr47@f'
        b'i@7ZY8}yVtb4Q=FAbS88;j(=h7!YEPTX$d;((?V$8Sg~45k7VN4(5xQLb|Lw2(y{<?t*3MX`aD?KD4xJluK@gfNiMbq&?r-w4eg5'
        b'rR+G*eAsR*6K~Fuj~q4B3vdBH3c&?Kw`k>KpyL_(L9yW$*F!9@?$mjt)$J1RV@R8%)jS`MZ8c|15%a-D88*3pZyyTsd@Hycc6P8}'
        b'l<!SOUI55kkabk<jYYiih-}X7c>*xmV_8ESYwRgJ415Q0`ng^iB#g$B0~(YVEHECi7kKRCQU;fwhj2O0;BE6mxcnuqEZ<J!3JycA'
        b')K4HSyOn3UB$Q8nrd^V?TWN2X_lzpfyd<$V%c;}P4eAhT;QF8r_2@X%X<du&IggIp0`bXf1$gu6>}}7Td0Nt{6WUv@x9Y+ix^R0N'
        b'i)5TZ@(h6FK^^AM&D852>9KDZq$WK&eydKTr#4OFdNagz##-j?(+bfwQ3B4a!3oC2p?^?J5DOOJNosUC4v-$U>V7C6*8T~keX-`g'
        b'i_s8W<$@lQpRRd8Um$<<(Z9U^b<M-~S)0{>DS7juc)O4px)T|)g$Z3UxH<i<d@0gH$%CKX3cb%21;=kG>+j#6lehfnaNFyq8e^mJ'
        b')_v+o&j+ar|0;VID({jn-(|VQ1XLubvVH2b-uVVanxW^Ir{{={vCf-xO6;8j6!oKLIMx4Qs{I6tbV+);<e=!<@EkBP93G@@YM-Xx'
        b'on)YxVm<aBDW8Wrs2fj_ba^HrJ_pGEC?0=YVt09t`zIfl$lD=6`|orBrsH&KOUsV{rrn9QevsPKWp9_Xbb)zdhc)aPI!CknVF|j9'
        b'Z~AzR@g>jZ&0Fmo28<?Mlhs(Ii?>#!E$6=tSPBZc;Q-6XzWQy9uR_S-HSSZZn(9-_<c-IT<oj#fr`Oo)?TyEum7U^&>}tyXwu3jR'
        b'L)27Oszc{6p{dz}viFca^rB!C?8=tUBXI%Fd!4sT$z#Lv3@Xsg=j6t><=t3&q2;s4w!-*TnbsG=7@@eI3w20-h(yz$*R-LecU5IY'
        b'x#lsjH;0jj7+mw=ohV_B6v(dpbqM$!x=aIlX>zZrw2{=B^1chQSMK)yX-zkej4oyE`!etP6-dE*a&ps3kWc|AuuJi_`q<kJZ0HP('
        b'vf_Sa4L(A>QPwFb?Xq_bl1*zmbzs#A$-OHX{k^+!%^-#QDa2Js{vIYd3uUu;Z4$;Q*4T?BEdxih4nYV1)PopzK4Gt7l{N-C$ofT4'
        b'dwf+W)PRj~;iW=)n^xXWaaXO8y~ii3){Iq@Fu)4{<O2|L%LB-5!rt&zJ?-Lwha=GT-dI_T_WUAc>&lXt>68Q6Y}#N+&jT}Yj}7Y<'
        b'D!B;NBsYkz_UT3i-I%M;aw;<Tm&js8n<Rc!iNaafl0C3L-Ivy;ctN;M*wKj%_0ZjXFc2$OF$0m)#LBB{A(;wd(|nPh3NNBW%xSjw'
        b't%&CQ@a&Q7JVw_E@RAP45HPk2zeEZ(Yvg7*G!#(r3=;x;q#ql0lM7%5Xp`BElIoR=rZriT?C$3!U>~}ZdxOx<WlPGMkt+<N2H%>m'
        b'_;|{_Q8-7-(+Zdc>*M(Ys^EnPp8)(@E=1tDxY;M@7mi{slfxuV-r{YI0>Y$^$0U)-d%Sz1d_1o^%DQqjUYD2lfew7)T3VtM;x+z2'
        b'st?1XmA{Y54fOLTUy|fIsay#ez9!$vgfrayAdq3Mu<o19p}>Pap5-4AK4@w-5rM-HNrW3q%7!;)@ajDD0|^jg7~THu(uZVu6S9IM'
        b'`(b9YBiC%mhTe5_i0+5dWqWxVX$}uTbl-z#zJ_4V7<B&xFQ`V{kK%D&Wt2WKR`AtKeFT5sS3*ysjJyQl>i6;uU!er}G{Gc(1rt3A'
        b'MBFR45K(#xX^<n+q%aI|B;qSX&Az^RMzF8DN#!1NMDVxS!upoL(?3|Y@1q0pj+5Dq@sJZH$4Xh34IlXvrOh99L-!2i2y;AFCWVfm'
        b'(h%Yq{)5_2F||)WSW*!m3K|lOjbiqEFc$BWGN|`{_ds4Ris0LqCKeR@m|?+keuWfHJyVb^w`V67N9dp7e;p+(N)&$`h2=;P+YuR`'
        b'iwlb}7e>DMj6GYNmGxuuN>5_c&?5-aR}Z}|f^P8<t0>ip9qKcm{s$gw%&X7J+B&kqar%lqufBOh35JV?76RTXg1?-bMaV(x`RQP&'
        b'!KlvJFf%tIt7{<lqvmXVq8L6M>8q!P<!2cq%W*DZj^JBGcrKRk=`zhyvbl6w@qg%EUTMr0<NS&U+Y-=b&|-5L^8SW!tB9v35W{T5'
        b'Qx?_tQ3)oix~V^zy(}KAL9&h+Q&Hzf4Uq_FM2;Mk8j>K0ZHbJ3BbQT95Lp4FYGd|5<14818CPOX7=jcZ?5n@X9p!h!%l%)+J@Qcd'
        b'>uxt-fGeW12fmIx*YG|&urOX+B6mcCV?(o$=31wDL<6XG96}bCHp02q0OlHL0MB5qG0r;3XTS@lCOD40eA)Ip0Bar!wcLwz0Nh@h'
        b'2`0(DOALmeE@f^?^m8m<(cs%W(J#JcKbU>q+mWmt-^hgGk&<40sSgV-jDmi35OP6i7F?g!$K&D0uw&9=gu00DH^=IW1jqEpijJA_'
        b'X3yYSGWi*JD55S+cDP!>pUXq0mAd@!XK;G&?tQWpkf+qB>31MF!FEZRb`dgiR_Oyi;$Oc-KlCm9<m7V6Ftqj`&OVbZ>Bju0wvw^z'
        b'`aKW_S}D@Tec07W44$%)oM#?7zdKh9XuajWZLPbaghWaoe0N()*mIEScT)*@^Wpb(CFJ#o-h+2(jk!63FF|y-OVs9tc^*76&#X3Q'
        b'sLc?M9HdjqkmF7Q5Mc19_DM%M_|ulFw2v6&;=6)ZXrCIN>!+m3D|DVY$l6Jo5EiY$@klWA@*=sSv)G4eDn}v!%bp9?_NOV?c#dke'
        b'GcqRvD%RAkd_x3R_j!qDusBbxHph~m!8Qh`Xdl{-dM`xc&00)LXr)@cwn%FRR0g7}zX<xsKC7Kjo26>7WWs?UV+(hFa`U!|+pNyz'
        b'^1q?sjbG(ux|2IkWEj2|{FZ@-pR}Bd)bd!rwO48K5Ui{BFC|KG6iYjNOv3S!;LIq{KZYl+;b>-$JcDx@x?po<{EV_FP0j(1hFc`#'
        b'<H=gI<rVQYZB8VD0EPr!wwV;D57V+McN_i)c#7>pP0TK*3+2Q4j|&RDC5r{JvU_cB_B9lIR0g-p@i4H~Fn$ZtHoI#Zl|Ddq4s^~o'
        b'{6FlyeOwb)_CG$EBtu9>C5R~!+RcoBfnpni3PEfkV0ciw5G8=ETP79+R(C6Xuv)vDM2!J$i%}uab{m4>NvT48z^84XHdTuKfZe**'
        b'YL~hTwQk$BR=cg=YQE=A0^+lFKfB-0=k@#jliZoP_uO;Nz4zR6?%emC+RN_Ko~$h1>&{mH>HhQmiN`UZ7SCC0$>WxD;>Qvkq`c{T'
        b'$;vBT5&}HGGZ9V1nsvB22K(Y|+#P|HZ8j{0%P_1%b6mH*#nmi6*D5~IViDW_!f!bxZR%Y@CA8R=KGV1;_5d;%%aGtbQA8k^In5z)'
        b'Gi98NbnK82?OT2iE=arG06vC8N1UNR+Zf{9_$(^(weVzjhX$^mL|336^|s$9#Re#K1o^HCC*}d);x9GJbQRwimb$(qmPLHcReZCc'
        b'i8wO)0RKzMxCZ$EO%Z3Pm$?1FB}j4h?3aXDg1w+=jN={G{rT-^#qSnm?UX(JzRdU{%It{1JBX)ST+8=0N9-Yf5<)}cg}XglmlKbo'
        b'1A%7ezr>B(i!Vvm_AWiz`)AV`Q1uZ$=y@~*RiJ6}6s#$1dCt?ZuBVr~mWAnd|6OB2o^2in^vehRjw|PoLdn3DlL<%o<Q9k{rXj(k'
        b'o7N>rTNJgfqY?bm5x64))Rgt(g0n9*?xX+N_zSe(zb3{whn0pnKrC-*2DS!TJ+_$rC)~l<pC6VWMrvZvJ3^KfTg+fc82F$^#-Nfv'
        b'QpQwN_6Mpd!WMJRtBIG!TxxL?VNch%$dH~rNY0uVXA_V-8PyTCJof3oyS@y2I>)6OebJnYVtENMi>m;8ts_=^=l!e-8<Xr79N;b%'
        b'0ynz^v++s7rg_@NMJ+j5ilD4lV@|%iep*iDruNEB6a*Ljwc?hVew8?(roTo^j;-Dl7Be}A9Iu$tu85-yD_#BZ;)>Y*mGFbkD4F6S'
        b'1&Z>O(*@^NiWTt&<M}+eYlt-rMDYfqdB%U_ndF!xoo|uk+C(-Yoo9Kz=S#N$!(dzn@^pKzXh;lOvl(~eSl(dnW&*5_$t=W3o}0kP'
        b'acjbO`6ftN2G@jf=KJTH)`X357lN~XA;aWefR&rfdMy2Wu!%`e#u!$$uRoSovC6QP%Cfjx1up32c`ny#F<e2~u*y|wYd8Edrq%{x'
        b'Ce^rH8Delr!2l;&T<JJGP7f@{D>u5*>6$?MW>+(vxMR&`e`!rkpy|*-@RE*MFcEu^SdOO$Chkmg`b)t;s}HgdS79RdA~7Q{oeq62'
        b'%{eo#4E)}*JiRn$@Ht!q<DRcRcqU(;LFXyc)zX~)r^NZn(%5)z?gX587*pi9@|Dub5%oNkTJs<luO)d>boQw>qs%-JJGR3=uS~>}'
        b'6XjHeV~AW~zCKT>J{SzQl^L{dlV7@8lv<UFWvDg57`Y=uovzh4{#rCQUt5|AGkp>?^T+Eu=T>gKrkV4_S?m{L$Z^#h!?O3z&6?Yu'
        b'l}i~`yZZCQ6*=fY%N$pZIBTwpgr>=QYUO-FUAHI`I7wHdkJrR1CtxaN_$Y78oo?2=?(t!LH~1Z!$$|Nr^oQ87hA)!`R9l0fDZy%>'
        b'#hU3?jxFbSk!!Q?NZurW0$eKy0#!UWiBW}l7BLwjvjot``$>OU?MiuD4Zo2NjO5V^f?^hH>CISNFlk2S52#1-sNZM%aG~H{k>R;K'
        b'9L&=x&dg30VDnE;hj=#Hh?R_9RRT{ZPZ-iCRG-OP(Ira_03Q(CBKqC5NN!{b#0PW0$;*z*%Xet)hAfLLPi&e)<j=|DG;^C%Uf&6F'
        b'q3;(WLhH@~DIj49AOmF<8Ds-rNybw1&VfyM;@gdHM<jk=oQ(1}bK(OnoINmZ(#5Jk)KWN12+(Cju^G53uqhDbmP2m2FE>4$o345a'
        b'%LruMCvW~h72QOKJ_Gqf*BV28`IW=@l_)>$%O4E+X_c}`O#=OJ@&jXlFTZv;zn1McZVvWAs)+4%Hf`vkN=1<F8D8C#xs|_+v8&oc'
        b'k1M87Nhz-W$<XZmDd;Cw99I*eY+RI3V{dM+d^E=1NGV!e{R!fhdiY6bLB}4|xRmzL%9R`9m4jnPlkbG~^vULiex_{vH6g?LzRo2_'
        b'hjzDx&J8_zzHzZ;Du()ShPsHCWz+ts7G-2;lk7n+lR6=<cU61Rwiv@|%HHJio>9}}{dswG<3>86rWY9aC1M~c)78IOoY?}IDtrvQ'
        b'Ji2n-hII8Cf`}mh?A~0|Z)ezewfpucJCqI5wVDSo><t0f0vK>gmAa^YPP+C>wREydtEdcmS*TO-wr^-xyc&asO}VQdeNd~v9R1XY'
        b'UnZ+JgkM^<9SqB(F_qPnLgnh;fD9+Ho~|0SpME-NNZ6oQDT`O9D<j5|@VNF3n}1s5D`pH!lbeTPwea}@_Vc1AJ;j03aaV-6fOe%%'
        b'DCYLl;!@i6lsHM_Lcc{WSCQC~QmUuyxiCWK(dn^rT$CD>nm4CGo|YvG(gpIULvym;jFGKw2W?f_T>a?dR|sQ@j`dlyNoH+aRJ%zQ'
        b'*<Sf-jBFxhpk3&r)pGc$pk1_hVhu-{YK+jWFVD?*regJq^K16tn%&r};@qaZ&h|O&b&HSI{pNJzBFB4spRZ6GDuX78ekyUv9kNZy'
        b'{gL8Yy5H*knKY`}_KUM}m(@}E&*c6$#g}UOe}o^T6WaC0DA{WpDkEi4sZxvkVX*(3a)^h}X41!a+vV*BU_P9xw7RY(NLJe-PRO@g'
        b'+hzYis_y^N)&B?a*_!?@;m1qX^}0+}i|EQyT_TGa0)V#Fb7ti^>K1p^{pM)nB13=BnsA%7Zn5qauo$;ilC|zPYc@rg8W&ZpmH|84'
        b'ke=+ICx<vH3VvFUo@8>Dscx~%wgLJL^=NMRey%Lc<UGJFpbd;NS08~%ita0(<7iw|+Hz=R@qJ{lVO>gN)%fBsI{tZlP4A#<dy#9Q'
        b'L$+A(1&tHg7zE@d2J2!t19q;7!VZZS3nXU)-QRhNmx33~=EWU$%x-^{9RCH)A^p$zRaQP*St^q}gjJRXR7D3E+=_@$6xH^==8{BU'
        b'+uv|Cack+?7F%pHx0PGNIV>L7<*~%tIEPTDlmw3&lnVw0elL^I4Iw<YJyVfdYdcoM7wz0`2(s2K(&Y(_Q|D}lA@>@ZFYH6}MYHz@'
        b'l-MZ6VF)`Kf8CN}SlyllIoD8jiwlNiMFl%J(WILLT3VE4+h87tWf_8?C3H<ZqijyrJ23`lyWL4`-|On%BHr85zt{WYsQb<CP4f1}'
        b'MSEGI?;xVvfoO-=u+{*-+bxD6vWv5tHZ(T#YMucv*k0}`f2K&n%ljvYqn#)S-^|UT4cRAj>VrI((Mnd%o1668m@F+-kmKqt6ldvN'
        b'Fr#_r(HC>_7x>Pu%3$)Blo*$-ABtkbAM&)*`037oqn(QLc7ftuSu6gf_!G{LR3Xe*-u->5?4eS|S{=KGa@{;jX-{xrl&5{da9N(L'
        b'OV-NumUV{ne6eT;cilAbT0Ja6%(z}Re3py_B^#}{c`_Dn-TzT~EXj@A7-IIv683e7z*9;`EBUKYrUN{k$TKt6V(o}8`fESj{XM!H'
        b'Zw1o7MhgJwszb}Bm$7Lpn|_{6pJvm~u<7%Xwd}h0Z_!md9l$<X<h_{YdsghdOkkfCq6;M*xbCC&3A8Um0ZZyA`+Ppjh<@F7@ecOb'
        b'&~|z%l9v6t$y6gp&xDmR;Yaw#Ho~mG7Hxe2FWBS|n6e2KN0m$p)&y}xt00C_X8WDC8<ci?|K|oppCNP%TK_Mn%Ck>1(xXhsc_wsV'
        b'1vV(;u~gR0m2*h0Qa!xigQI08c&jqT>R2Sgu?^rdtc?_|xa1zHFp?9ADjdrZt)#bkXtqL{tx(oyAph$K531x}Q>F7cR3)OrUpMEP'
        b'D%rELHu#|(C1@ecak;7+Gff!RVlgckr$I{+;4`fM@v%xv0Qd_-YZAEcJ0N3;HN_$*O->?7@R4dRqs-qt26w#qy&J#KyN3;zePyrK'
        b'HBfcgik6K=89(=tXX`V5|CnRJxJuSPxmtz=MP44-*n;}p-`SUvQ3>{WGTla=!=7byKZfG0!UWwV?1->WpsN$;o_NtHL;+!jFe4-*'
        b'DkC8yGh<#xX+}%N-i+>y6B%bSE~!fc)TLr|X`s4vtU5C^qqZwNfxMsHLO=!i-Y-RpBgT!1R_7{(i@9w@S>zgmhx|Cnz}r{QUVJ;I'
        b'NyM;8gcZl6=Dp1hA+}iXbV~rl3em?F)(EZWa~}_ykaH8gYheu!t{*flIzMr>ED@hL9@j)-v;foF|588)JYilKh!YbrtAG>AHyy(J'
        b'9{pucNZ<a)vJP}*O**}YB1Ms$&^ITER(wz1*LAp;{KNZy4C*@k&ijw@yAB@)->mEKo9{n5rR#8W?$(E^9>i_bMAiK=h{HscyH~Dz'
        b'{0!#+@%}@jW#Og+eo@ihSo{D1?7*b<cTbUMluaB>NBU11)w6?ufM;EZOjhvvv+G2ncyMyLnC{~Dq|<!DqkHaqa<%!m@4N`_RwU5Y'
        b'*H_mqjjM9lRV=i(H2kX(_kVZwzVobSc#o5b3W%igW8{1rl_$uWvZ02f`5cp?Eq&xTLq0mwaNT>_L!Xi%S<Nf$S<mXiuShzQNxroH'
        b'YyOHKPx14`XijM5cD|fr5@OPXiv8zBSckax1M%LTw(^|reV6vNi?BW7wlza((Z225pWU?<C*H$4SLXEZ6Yt&MA+n1wvR1PnYqyu~'
        b'4vtwfZPcs}b_a*G+lzPGqTGAYo}Jw`+}r_)<&e<qg2a;D!2+~yM_LF!ELz~^qkTL=j>*1g&1=GFuHuyJ!31I}hJ^|Yr)2JC%yj4-'
        b'gW=i4<uKu|Nr<Q`%t1SAD=Y%L083kpyFbNp7vsb!j5rN+;D+WDruhpN;qQ;!w>9|!O${bmy{j14JcQNdjwst}5=*V}u+Y^r9nE1C'
        b'=EiV8d61jkia#-&8?BBElk@Vz=FxQ5PjZ|b7b%$Jzv4%Y8OsY}3%;1M!X(QHSnF&K3pGJ$nlBGRi|n~HH`;Wy><>+NM<5wK$-h~!'
        b'Cm6~<e`B>gc@T8Mo77q8tFr`Hy8BXmZz=cVH<lsfL2R&alTuTBbv^d8<eM=p-y@hMY(>S37P}>2ZO5Ll(2CtrJPRtgCW;qrF+GJ_'
        b'cuiqoCJ+74B<Ki+nkvkwq?85+(c)Jm2<oyMNKvcbC)r;z#&>2z$3Mdy&$e(xf2g#~(TLbQ!M;2-$!xBjL%D3pqHp?Nfi@?F%>oOj'
        b'-!iA1LxjLwjRa~3MO4h}It+?<KguV|#3-L0fF-XUKno(xDD3p1Ug*@wuJ->?eD?3>z7bb^!;Y-iZKgxLYxbVefGLAZxPYFyCINzY'
        b'^Z)TQiOG&NA-E>WW1+NMY@(c4H-+>kq#kqxcb08s4aXdTA$LAEk1r1s<@DOb-xn6vz3u&Sb{^l($6ln*(E)3<`C+-y(7+J+PK@S!'
        b'$tt_HYFORP{(Hu2?z@M)B!<nrHs2>B@*%PPk+3i0q3fb&uXr{36>ylO7CC1PjcY#g<i*&iaz0p_-bk@Z5EXI%IdWWtKW?7rF+b!X'
        b'!y)Mo^O#j0j4VWH%461eNIoQqUwAax9&!pKHK88!;~sJbDmUJvDe_FE2%6dKpf)R+1~uc*GOz2IH_Dhlgg5#%2_4Ma#!A$xCaS@~'
        b'Y@>q-WoN)r{X_EfudGmHmdKbsmpw+Uq1nGVqvx!N+Dvw>_%TvoW!}=%iZCVBFbj{IqwNe(*8R;Wn!R2)o5T~Qthk_LUZ$B>Y33E0'
        b'sZukkG*eA8jV7kW%4|_GcAD8mGrMV~m1f##W+%<OMKf<|I8aZsm2oI32U1Hc&BfNK>8?+8v`0-jk|ww$fqX4x*LMbF@YU3-k>jFL'
        b')y%7E>J{xVTnfoo23HA9lzpwm#Mm`{SeGNr+8NLef>E2h4;Q{6SQkRf6KU%%%*)m?c0Ki$tjM5;nz>j{pgUazGLZiC$2iGb@q=2e'
        b'l`f#EH%&~vmDxJm-^$dn!x<}Mnn|9XYL=Sy1Vk9kdZy`#mcFpLq%ArldJ8*c>6xuvRFl4^f8k!7ctp@&BraWCOxOtw*cf=#&k@CO'
        b'FguM(q;v<<1~;9rz)f6FwK<qpiR6;x?2mdOCNcl0-;9}eVET{oGD54X{vq1Wt;R@+=4}k>Cv9Z}rhmV8VFyk;C<3*SLTSkx0u;zM'
        b'mA&74u0`C^2sxxhruTc-?D--(ea(I7m3p*aV<YYk7L`%eqL!sCf?jkIF<L_^bEGeS?x^F5E=R#K&iRiyU-Lswb-#Cj8(!&Y66%>|'
        b'2eZ{dy{QRB_E9e`Ei?yXWgp}16GK9On)zC&WnuJWsk@7*wk`~*mh;Odjt6b+mh+<1O$$TH!fmGT+TJ2@#nQ6(f3o<M7Mhr?<pg>)'
        b'hI#Yrhx2Rn3q$nbwzBZr<wbh;PsIc%(@Jf1FmE0!KT}y*0F6OvG`~ekiQZkN(VAcPpvHI}8UtElx5STx67^;^>PRMk4q2l=)VmPk'
        b'?JtB5s`<fEQV0=I%NDRDNI^{|q@eagy}Lm{8P&nKdyQ8?=3b#sL4K@)%*3tr^E;14_!7}hy@`$i@#*G1%=9tdB@YR`JacPk`NByL'
        b'OOG98svX54jgfql9Lf5ABriI{S{!16=$X|`E!gRwEP~QPPz>}7l$FrS$D>IS<<;nmkzPQL6-X}@V#W6b#dAQ^cIHj!lJ0pP3_DHL'
        b'_y0zGw&+}uxVs1*>HRS2QqYQ?YJx0X?%wx1KGjoOHMt(W-Jp2@D}zo$oTi%k-Qv<kP^jy}-qJ-~RP$*l*VDx`zeJv9n&9U99iLP`'
        b'fSWTs(KrOn=5nDZf(+6;;vvn%D5Ph-y|~ODTUafW)>vUcI4~G`vj~W-pk+`ewJ(BaCTJxXmd#-NLJ1R9R{-uaQ|FHML=#rHs*%A6'
        b'(?oi-RQ3MNxsEZtwAj%Zz(UFh)KAbywjFs#9kaeB_a>h|$vJTn8ln}?;B<e8&g1jYLa6Oc%`d<ny(wLgTQ39xY9J8i9*>zi1L)&;'
        b'866V(!_2hMmAUe%($yxWTCERBn?TSstK+2;c+n|JeF#mxuB86Zn<Gx}T5GT$^YSD4GTF1xDr^Zplz;}jwg8(Ocm<x7CpdJ9fj)tw'
        b'5JpSl<XAoPrjn_r8RuerIzAsKQvE>UP<|FGvzDsUQ`NZxxLJwq-?7j!8W;!r78MbX=LNdKEIaamhl*qn9V9-$&ETB>g!8rkiBGx@'
        b'L!hhk#0&F6)YO|qC&r4NvantR6u^{4g}bGgPj)38vSRg%v01SJp+BsBCUo^eP=Og#P^J%A8txM)E}R#=@~Q@kSPlGuxPbagOH@R@'
        b'#NCM9y2NmH%^#q>K&-UF2+7|bSm+Q9Nn~Dx4U5Byftu5wSd20+9KbaXWBZ?4=omGWU1`OL(mTkn@hEFCbHR<WgD-MTyXS_k91>cq'
        b'56Qh%yL+YnDIWL9Y>1uUF2UFmw{CY}6tRHBs2;$<x!S*Kq!>76zC$w(s60v`rXKFUAc%0d5y$^`$e~c6{(C1mfDXtz3ETgymw$Ey'
        b'#^b;~27?cV;9k^jC)su*Susw0*8L&yKMA@a>V)^qz8^5dZY#J0|A>V<u^*2so{Uj5Z&rn4?%(<=6a{1;$y2B|WMvhAAW1o{=ws>='
        b'xIR@&oPsDwPr=Zujw|}r{=elqf`DCMGfJKg{a4MjXqheUS(w(52Q4_y*JdF3G0xY-iDTVvHky3EgARaoi(n1|nV01@i-t7jP5|;C'
        b'^f4T!1W78-OP^JT1-AuyeIWN_%<9O4{Ix#%=TC6H7M?iK-HoVcaGb#&xiCJ2W?GcY7IP%4*k^L<gNE$dRZ3<G11-^?u%mp{i?K=U'
        b'C|?k|Dp#J$8all`WMSCQm<_vTlzZ*m54J!H4wQf%O|>YgEk3KK8fO+Ff996u*}_+KR>r)Uyf;%%ZP8LK)St3q`m>WX0Y~st+*bYp'
        b'o^c=>9G<T#hObYf>xPiv&fjJBy_D&oTH2{C#?R2rW0^SG<I+X79Hq9jk_Sc^k7cu`5ePJ+ecdVgBQUP(UD-;iX;v9{jByTr@*lI2'
        b'cT3gL+kOwx6iJZrTBc6VIKhW=e+l%cpqW-`OEoS8t%H4LNyM~gs}Tt$<4AMxjoY$KjKk_BQ4>JMlDHB%fOS`m_a}T9s7>^?zsQ~q'
        b'm=!p&IvaVuALEJOzSYqwSz7xG^uafuSS6dWlD6ZrBAJP*SEpp_frNd*8pkie+iO3>F+P*cI)4t`2_AUXv$!w{&<o~#f@l|DG*usg'
        b'Kcc4U$+44!NfTDW<g>1wet*w=p={2|EZMVPbs;Cm=|*j1s;jIpI*^PG_D!Iba#$HB!NW*B+@+a%@TnmIQYeAHI!rb}Ml;)KYKxL;'
        b'Ifiqn|H@QTTcSUfg(<X5J9w{%a{H{HwEJ)(3;gG~-JPx619;&Jew{&?eT%b=`)2~<o#M<sapoi;Iy9V>q$hz4QZt)ORFl@uBtMy*'
        b'8;mFaDqBm{13RMCokV8eli6tBk%{TBGJA|$5RvI3dz8%hlvfdr#s%5zM;=d!T5+_QxDI7GO*LAnJ!hW+=T4fh&wvo6L(A-#B%Cf<'
        b'EQk<<cAm@V`$vWdyb8Fz$2cdOjbb{Wh_2;_&NCT(DQu<2$Iyd8=xBe-=zGL_YX-Wd6Y^-P(NCYCWh#}tF^PP%(ya#dSBhwwsnkPn'
        b'mwcmibF_99*w5T5T*(tE)fj>FtX5-E8gx5}Kd&f}M>9KQQ(ebaUQtpzP@od)QZkLiBy3h8YQ;x#?-R_*As@=E=15cZj--NYgUOMl'
        b'WpJxwt|8lyFNRK0o1M?O%saw8g@=F6hmJApx!h_A^ku(+0N}?&ISjN5;wK{5+s3nsGV>Q!N9e)Fa`&DzceZBqZOuR}Wem*rp8Y9F'
        b'(zu{W)YPWToK9y(pVRx;k8Q3?ATbPPsag$^tI?W$A{VO3Ret6Et7q0TG_@(NnpRTv6DI_$_$ZDRsj0>^2d;SnbLYS;*Q9;#ik4||'
        b'bFf(p;;L~?G8oe)ky5+uFIl>Pf~04a%%)kAg`0T)Cp9VQSs1SR<G5NA7ro=yN=#|z$YNb;`y{Y1`cL3?JZX({Ftj5sD$;m7tIWQ@'
        b'jn*lr^9(8NV9k@%R9331f37$)=Uk3BYmQ5#*S@FFYOuJ8pP)h9bwzzpp>(LUjyPzLgoJtXP>`ku$!K*7#E-MNxyp0w+@W^FwRZ+&'
        b'J~->X2kE8b{1b6nqsn}c?&2!nRY=vK1KN=mMJcI9Ss3VfHyAdiesBT=nRR|o385qFscoe>TBaU6S9*&_CWmMjQz&IhW;@B9&z;02'
        b';!(TQL339scuBFchQM)>IfRzlrneW(Qzk%cS`VH$nh)NE@P3<>s+Yzm)F|ymRv4K~lO_mL+ZRG5$b2#NYNn}F?>BJ2c{C7hR8rgE'
        b'p`ylMWuFWNhRaG^dN&7Ld=2W0T6+<cK`jEpLw#g0RD}XpnBq2LS@{7ZH*Q?=eC}YN4D9E`%@HQ5HHmhq1)O!Oq!ww8iD@N3WwCB#'
        b'>+K#Z)v5+}e&fdwkS5Fk`&E!?s#wL++peeD!5a2RG}S!N|Ima=5}FM>?}VB=h-+fNkIQwCLvyMe2iM~kb6p09{oF(I6}eD9>_33}'
        b'E*jy!-{`+jxo7{~+Xrs%zRPhX^_B`(JQ|}4bnn7g7a?sBH_NcClXD%yA#pUThJ^u_-~{Uo3EitO>_*<}Z{)oRH&<a-*}s+l<KrK='
        b'm*eyD2@B$7;UG>Zz&FcfeKVhGkzlvgZTQCjF}hW1F?Ruyq#CsP@V#~t=Nhjd?gws&@yz4@vvR00_d~<%vmCJO5BZC%r--@*!N#b_'
        b'M+Wv^9Bu~_uwR_pgxUeBj*3L>;B`rE&OhJF|I!J3r9JEh{@d9;^7uXVafnFWVgE<ZMxjMAa869#DD(_YOvd*AX(1bbv%H~z4h7&2'
        b'M;=tvGSoDma=sRw__X_j4EBWNfyGxwgrPUap`o{qLldsXp~GY0E+SE)5iP~tITj_}7>Y&1C7U4@6%IvZ?qA;|6xA&9g`%i;K07jo'
        b'3&b=fw~yhR^RFmFF!z(#zbzJ3C@#2*?-;`cV&*4@V^QLIIdDu9cY8U)v#&rb3PB)tLo5e!+#p8Wy~lFkOSz}sMJ#Hb#I6UBR|8QP'
        b'W4Db%3uj!pE)Erqh(m8=e#$+!!QI87Bwz1!6N&<0Y>~KTI*!)0M%ugh+t@qQBG94Yy~6nHT}tlNh5&o#jW4~jEWBzjP^fkXdl!!b'
        b'1M~7!UVFh7xScG(p#B7&h?cC%G~l4UK+<KJY^LZjS&hsDS9~jqv38lj`{3fJ-&OD5n0wWJ$Z;AXlc+n`kH{<NMTEmGyJ3#He(YSo'
        b'es_D@=(Fv>LL}cUxU+GDj9?nQwwPVMV?(ir9h5`XC2O~1#?kBxe8#D#oIN4txnNBlBu|k5?ml>C&c!_UFVRZ^$WQW(32AIzaLk;G'
        b'`P2DCCVn%6tBJ+-AM`H!4I5lw_4fLb4B1=r`u~i*H7~t8duv|owYC!_2S-|4FswIPTlXTbo%)&fmiQ0YTaD^2>@7HDBkk?nd$hNg'
        b'E_?0m_14xr{<a3|rY!yJbw83%2D-;`?$zFYbD1?!=6`tpP4<@f#B&$+*8E={EL%NW%j|-PoOyIMvPVPX%l&i4SO4Yz@%~H%>(7Wr'
        b'_%k<KTVHgmwRPyWcN$>5mtlY*XX1aiKXdT%b^gp<%W;dj<v-}pbX@));?HDFkV$Bqrt19kp`dva)db!LxCDuWUY%u9XQQ=F_I1`Z'
        b'jt}i!{2~3yG+H(DrWGbr|A;a)GV2hSiOrOiA|oZFAj!PJko0WNvnHzEpxGdKN)i$HxV5e_q(*)CsUliHq@#E5YRVxBgE?AJ$Wh3`'
        b'Oq4?rn@o2p6jNncbCT(FENg*GS9O{0>Ltg@7HlYxJu5jq4w&@&64&Hl>VsDjaXJ-KgP)O&om@>?<CH<{RL@bqt5DbdRjK}KW|Vsd'
        b'hN1WSb!w)O-i)d1E@URlA_7>L8B{-AIA7HH@T|VRR8eXx_W&P=8RKTL>yC|%ZiUq1NX1M{qeRKKQmtfgnLnm`4pZCx<0f-n=Bu}H'
        b'GSf)HYUd<Xtz6@;K&xuiQ6PquYHO!<Rw9T^<zbl#XuhLiX}0Q_Mzw&mFo=iVowjxc%<6lat=GuUL<^WZzb7}w?ZDl~J;eQ(_3%?x'
        b'#z9jKHMI*ZU^*1C$x&f6jv+-&M*2w#=O~o2thve1oI3SoA^^rjo#877Xdxl<=}MmZ;8W}plVfWM&D7I%mFg3mM1BaZP5mp~wE!rZ'
        b'xlo`oAl9IK_bD}6xN^{S7eFmh6v<DbU3v;RJ5Y2w-#i+vpEUJI+~;w&pK|nS1IdN{O8TSMqJcD8S9dOEL3oq=*=1}H9PIaWVm>hm'
        b')K?E&sZZdQRddult(DonZZdkkyd4ZX8J3hDpk~@7t1v6I-Fg`J-d5XJvG;fA=K5Qyt*5E&{TZ%M|G}U{g2Ikc_Vy0~x)x*B#hg7I'
        b'%bFV2$hsVpy<0;<daTTz!WRiEwP#(3`v~r+``c-l8{SeMJm+BSz=r7r-bLA8Xj;3qqeHs1bNkG+$hWMNeOXh+_`Ruz{WCfs8xVw?'
        b'U5>EsZZFls=ZSS8n!UKX?r)%gOtd8h2A%p7yo{%nEagFYheKaRz1m_d_a}oZmM+`z!shbv@V|L*jbJT^Y6tUxd1<=34PK(*O9)96'
        b'=H85(>Mj_J21Ju;my8E>+1nijYU<U!h?=~@w=D)rOH<3otC?5IPT+&9{8_T>n7@v$^VclhS4Ps^5%DGZE;FduL~X51zk5|Wi@d5N'
        b'Uc93!e|1-?bTXhy^TKOXN!5o6DvMl$l0=OR?GFHTb_eVs%R`%YXEZjf8p)E0>2S^`OjHN7hYq*a{p~0OU2o{!=Rg_2UD;=NJ7rIA'
        b'T>DznZfR<pYUV;YNNmq&ED3HY+9N304cQu2-4Fcub`pK)%tQR7Aby}pGm%nJXN3sq1YW#*&EM3(oxD*?*<s|BmPqMxe$BX&-I0xh'
        b'Ccm{gTE<SC<6N)*IjsI4!j*Lw6fp+PG7gwnwY_jn817!m>D-ypw=>1}hD?IqjObd%PysVRagqLHU{q1$czI*VZYhnbxOF3k&qkG)'
        b'$N4HjyRfKD$OzE__Dus$baSlKHkx`>PuXi}w0nzs#YDXg0uVJ4nt28BU!({A1?aPji1Y^r^g@ejaHg^RU*Qas2D+hqQP^Oh(!7HM'
        b'zRmjq+7eFLQzGS4!iJT>BU)!5h0rCe(AWJ9xGgQEyUsxcpnj-8{VBe-7-TeloEg8l-2a6g(%6aNJKYmGYHCwM5bn;v*w<I~NFJ+$'
        b'psP9%tc3w!H~V2|3z&9j3z+LYL-=$;SNfd3?m_`$(6jPesYbB&vPfA$77sdC7A;dA$6+8zx)_?;28_tGvdG{}I`VCKy%p)AMi5y)'
        b'Xd>34bMjgG`eFKRLwFp}|1BCsltD>tI`&ua4hm#tvQWN8h`#HRe_#2ojE06)*C-&C&_ykx*}fDNseJd`OTM6ceRXDfLyezhmo#-P'
        b'9T)zN>b{Ct)ll)_!7=bK=&u-xgT|sBR3h`=sKPS>(R)eMl8xpx=uC|UbxK3f^wOtFb{98V*`6saD)-MAU(z^e7J9o3lIOZTbKy}S'
        b'j~?Vf*4a)H1*vnA)UHs$V9+%4FR<&zT}fku`GIT4U3df<ce;dM4UIZ51S3aXv3JxJwLOuUCT|CAmo#Psx1{b7WU!;oEFCfG3MoR@'
        b'l0Rb1!Ndbi7ZnD#8jEoA9E_NUtxFNbqIW<rcZzb*tHD+fR!{9TQEesudg@iMu+W1+Ew2C-DI{Mh`ve~}i=fA|T^qeb9Tp*=$1pIS'
        b'(9P3A$4Ihxt)c_zvcv$>yR66s^LxR<lm^Lku;WnA^5@H#SIekZBK@UHOU9SMfLY_msurk@&`W?=<_scqXJ=hCX04>((?xTDT&RD+'
        b'LNIFa!~+;Iw4htBp>1Xjt@K($8y<iRt!`dA=ri+=V9?sHwXyq~kd5VME{uGewXr4RTZ#_*mvpov8#}TKIz@!;QVMkB%p!L5wdw^}'
        b'DV_D(n5-gKRl`}uZ(|gYkes!$y(?3tpcg>z)>4h&H$oHm6+H$`r=+&&scouYCDO&)rLjupRVDRGjX(;iSD-fzt`xExGYNsOpP7aS'
        b'&LKk~m(ZP<X05wWx!&MyTA-da*&s`CK~0J&uB6zMhOx<7>QxiF|1(lBZ-UoAse+|6YnudK>VDVv;epG1UDQ<8lLMnb;<DH|KpTd>'
        b'EZn7_U7`HJz!>vdc5mnV0r}&X?NDuQSUG;Ac7EjRLX=($RZwcUsfpT}an(fajvT+7js!B0ZEz)Seikv*{ejm~4qV{tGAF@sRl;xu'
        b'&Dh<Gz_GN)!*tQOHcVP1jU|Hy!v)~a_?^McvoP;iRhMu~B^Y#EP$h`guyWkhfpOUR58zMksJqZYDXF(n8{p6eYHHh18)O6ywZU4N'
        b'HNIC>-+gG{?|fZC7-+thg0}6Hs{2CJ-l;};&|~~v2Kx;W9+WNn7zg$1Ckk1QwNd+?2e?hI%|S@pd>H&|=|MAsh5&g`)UbIP0C^t('
        b'H!+GLV4@Bs2FE_^z8~2_y`Ez#6sZe^*O|l9z>l<ywP(v;1amma4<aP(NqqgBjC5xWZrKUuuq-ZOzbX*S;m!=_B)^7L6QNSDFWpDn'
        b'pL;Ox#G5g$oL{nA)!497=<N^Phs`HE4o6x`4AReTJ+)gE2zmm^hV;a0X>g_ATIf*TF*{OGg`e<sEn=jo^;R@>)J;4cs-(86sqI?o'
        b't)vNaqH<v7)G}{L&I`<PjD3H&)kJL%<ryMegMp7|E_jeBatAC!R(Ge$Ik?h0RlB|O$W@!;JPPe8Qr7(qSX1N}z+pgL4s>t~k9QXD'
        b'l*TR@lQA)@4SJx;85vwkFB3%WgnmYx^o;EIuEU1#5BZY47d7KCk_&<<Dd$%yL&Jb@Ubtp%?0&EC13vmv)@a0eJLQCX-f7bKPCEMF'
        b'Gq|I+3m66>ZbjzsYWF)d@IK$n!`OWZ&UH0#>wv$p9hFg14QlEwdMvTxJ6Qxzma;+3yk#DR^ztTp1=gUasuwol=D%NXe|5o1y$P4n'
        b'Jqw$0%|jQ>4_{PM^$;nNfe}1h^UP104L{M;TfXnbZ%St|I*NB?#!u3R&iiCA<E!cHVfE;s6yrxIeJlZ6@k2Ss!dZux`wrZPd@{96'
        b'+1M8T8jrSPX%lesT+Gz;m|?D=ceQw)rPl&K{dr==WY;{4LP@RfPED{Vn>Hj&uAI}Zcr+#}hsug|!L8<Z;8v`oa$|ealQESSsVt96'
        b'5tp1`>3>vw>AT8mDyzl?$plZoN?f~P2)s;=?e~Z)H@fEIm2*~}yWq;_=)057&DoF<vi59=IB9!OKBXOv&1y}5<j<SNXBPK}dLBN4'
        b'_bf}?d4!u5&N+g2YecCqcxGu9ZsKRAYor)<oXX?8@WA%@E6;r_o_ET1O8iO85dq29U|4C-@fayOZs0^wACs<k|8%0Lm{=PAMRrO0'
        b'%#&F!wJ)EarKNg*AM<pMtM@r^R<0{+zAG!$bu0*bG4+LqL`!>f#qcO|h8Y3ge_Xiv$IMxs`RRGTaUC?JKUOTxoHZ{s<5#CY4E;ia'
        b'zF(ETJpL>h7#D^PnTiy8KQw{P#<8Xum!yw4E9aFo<8MY>8)<Ygz!^R}=O>Txess%;Vd0lOzB8gbu|fl{jY+p>vIoKZjyGMHtxrFB'
        b'iJG6D{A7AFPDP=g$J3km8Q}OBgVg8{8@~Gl*1`Wu)WkOisJ$Oh&?Tb-NA|Yj#<8f5W`55lbZ(dN_vpSZ^Rnhc41Ijrg)X&REYUG>'
        b'6Rv!hQwB*l-5HdvNncp4lrCtSk$wt4!fz#<(fq*>-0i|%$Tq!yd6xwz{)jCvDkHGO!G-tX?!DN9u_%Va+EnSXqq3~`*ze&*vSr@J'
        b'inI0Z%e%m0wm~xb&!w??F1ECakjAd~k-)L&-Q@VCRh-(`vd#zE9!%HUF`D5l<6Op1cgjxTU7d6**UFIk>;QfCnD8*ZtrMNV@(0Wz'
        b'4rmvPT@_-x#pMu>>9-)z@D}m*y)N|I;&Qc!8F6}xrP5-`C-Sn(SIvucfOLnm$EH`;J}lkPHafl49|>2}Iq(2bZ3u~J%5Lwz{QcU<'
        b'mKujYmiT3L2p3JU55~HMSR2=?2yS>NzahlWmTf(Jc~^OmoQPi)DWSekQ{mLXG?J^ri5IYZNnUpJ@p-YJ*EO4vls{-d$~`7Kr+O2o'
        b'B35h1+P+QGW{b7i0ov>_AS~RuR^IZ?{A}kqz6C_}&s)WOkye`H_Q&+%fHII+Coafw=|SQgbiBqw@zc+{&@T(_FU>LJnDQ^=Ws}6b'
        b'*y#7y&NZWbE*ul++lJZ~5?1@{YTM)1&fvC>(jvt*Y`r0<-cVF;_-Lp#A_3QEuy*lia<AyM%E}AXdvT2#6h2B+3s<}HarYybRZQ+$'
        b'hMN;H(+q6SxaRPhDVFStl^O{;lA~o-Mx%`<jWyV0<W`v5TDdiy#y#jAktNxYP1-u+Y*Dj5I!P!~1!SyhGC4t&S~8dQ$(5;L<lCyv'
        b'<XF`XQ074|4#jT2V4Z<APa!8Lv&CTFvjddbW8iVNRe(i*7guw?5;~4OtyK^yR*g`ji6IL)AdOWV-~hF$#FeowE2u3N5(ZbT*xu|y'
        b'zcns||Bp2&3wiO`+V?^e;v-;~w|km`2DW(OS5d!*wv}J-p3J^rC6$?0;yr_Fz~w=>*@K?&PVeCTZ^TYMl6E6@G9m3Mb}~NgCfG@R'
        b'+W#}`WNO;a$4*X7`~R_%|9h~LPd|D$*vX<t|94|2t(yODV<#PI^e*3roh%&7b3|bXJel+;yHvl~!EBRQFnMv0vQ^;pT%x|30nzfr'
        b'8h@JFEN8b+Vbqs1lyGYU1W=nTa<tmb!>9poHUVU#X)et;+8wD78g75v;IMPTPmh5}hL(@_J3X2XCaO;h9CC^AlNl@^(?O3X;`Dqv'
        b'lBYY$ZKoV)&G`y03E@H|?5Uok!S$~8p6z)A6#>fX&Hx9sY5NYtii?FO$3U>6*)Kx7$SFstLm5oSCIl2&Q)ruC)ln{6tEl>~Y?TMt'
        b'DiH=N70U13<2*j*DE0bj>W%Z%AG)Y|Z|&h<;|}I6cO#;>;zB!%2vsww+2%)*S3g4H3DZVELaS-UMl+3G+yILQ-8ljex@#B@s->E>'
        b'XzzOc^>|S9qG*CkLL(d~#8pw(ta$rJqBU>rb!*<&u30(;O#W!i@>d8Dnw4$vB0{5zh5(`Fnb!eAbv{6-a|jU1p7VNhJm`lrZiNR;'
        b'x(*Ne4VT4(?lQjh$W=V(*W5edL3LO0pziDOpc>V^;z92hl~K0q@u0I1-m&0%yyJlBUhtr{|1cg@cT+s5^9DSq`Qp9dK|dDy6f^=4'
        b'dJFwLJpvEPYK92D4h^bAXiysq@$@svy?X@ifCu#gLize(?C7oVpw4UXpw5waQ0Ko15Bkd8;Xw)EP4S@a>+zr%HUbgqmV306ZU3s='
        b't9Ue;#nZ8P&?k;MvTlY4b>{sHJgDtIfd|zM<3XJ?)8K;?X>P!S+7KQz_7-^1Cw!Y7vTm~3A!8U1+VwN`t=R5)--@Q`?)I(R0TcSf'
        b'$bBnWcYz7LjSdFlufv4idH<^Ip7yW)H)29>BSvBL&%lJ*{==BiCr0jF$+~v$ip+EGdsl4#{d-r2F`?#{Zi5Nc5uXiVLT$IfgwDpa'
        b'jwgJW(5xFVq2c0NV?w75VL}P%tudifFstJU-<II48!@5bqLG-;s3A<K<R+L<8qKA*K!s{pbH}1Oua5P9H!gH?q7N7Pm^x-&%1B)3'
        b'lPTBYLZ3+S;X;3y*7wh8zPH|aDL2K1W~JN&7phxdoZ`cU)+1bKQ3~?hZ@`5%fGg+4g}#z_JuXxSJo<2<^#~W5o8rY&jl_jISzKtt'
        b'EpVY(*Wg0u-UJuwRHx(&;X-HmaG_tTy?cgrwLFCK8-WYm2@!%b0-vU)oVS97T9L2Q0Q0O56bb^?gQo(0vEB;zy_nDjnsKt2&<2p;'
        b'=9tjT#M@#*^SqeQ@IP}qU!B%>Ms19njxeF?ruD6x=Ea15qaMbDR{1cYf)s=a^-IxGPGCp0y3;tV?}T~;CNyIDFedabY9A)_Gxar?'
        b'(9r33feHQfw7$}5!<f(y)z@G`7fkE>BU`EQu-b<SeR5jg9`7xe`rn8Nt@mO=&0b8X^LCifyc;p01CK&vRewDuwBCyeHG46k_19xU'
        b'<<t5mPGdozFRMplLaWqNRc217Y+9ep``DzuBPJBX5Gu4Pu6hE(gNl`ubK(RaD%AZrrWt_>MLXqKSg1Ma23Tm-&0(PnFmkLc))oDy'
        b'Ye1m|UQp;9^}h}Zg+T4U2@~oZfeCf`Frm&{VL~-Sm{8}fFrm(CF`>?3OsMk)OsMmgm{8}nm{8|cOsMk)OsMl3OsE=RLMgOW51Y6-'
        b'{6<u$n*;hXUjqs~<^zQ~eV|b12v8_t8vzQ{kp!{P3ktR64&ubkL7_LD?7Vot!q@K!?-zT|KD^oIz~92}8;O^j&1F%cn%%d;gsvWz'
        b'#fJ&a`da8-eKSnx=9^+dtFf!>-z6rr+=mG@-vSeQ8`V0^KLZnLyL-INJz_!`FV?pD*7(-j$TG0(XUp=R!-YOE5*M0v4K8$G@z218'
        b'-VOgh7Z*z3fD5(V78m-24@Z%8BaR}x;Ai7P<9}W}O88DFx<#40#ZlZ4j}GA|*!H~%j^cLl=r6C_GmgUcZ^BV{qfvym+URY|p=i_{'
        b'hhcY!M^mocJC5RB<I#TwM{%22)ERf>=f<LUi2?Z+aG|!F;X-c_1R|3+5OwdkP}{#57dqF63(a9hCtZUJ-RZ@JA}M!VhYGFNJa~KS'
        b'Q5ediLhCiuP3F;C<3jJjwgVG)iwmv41{bPhW3h)FRJ{)uYI&3mSsL_IgAW&4@56<Hch+zf7g|s9jXUDK7*Z`fxH&Eq8C<vW7Pz(B'
        b'*<1hH<3jIr9-QqS&x0dgxGPNPZ*H;n=f20azrZ`L{e}O?V%7@&owin!a5tFHn5&pI#f_M?_}h!&{EEe_J@jw2wf`zE^mg{P|9V{L'
        b'-7a0;?HcSo;6l$nqGfg>T<8~%AbT`CzG8pI`1<Hy!-d-ZU*SS;>CfB>7kWE?rt9+m7=PwYxX|1AGrKPT@AYR|?hO|j`*YUTZ#N$A'
        b'3Ku%pq|Uh`E>y?jLY;Sk3w7QO7g~>Sq4h(!(E6W;3$6dzxX^kQ7ur0%Z|2k?Txh+qZTi263$15yp}Vf)LhFsH_?zNFE2j5Nn#$rr'
        b'e?RT!xX^l<s#jAx(IRI3Ra|KOJ>WvYk*P<xQ0I-f(E4j}q3E<h78hDSj0;814ip`U3;pgUxKJI!g*vU^7+s4Ctsj94b&kM=>i%uG'
        b'P{%MXw7}1c3+=rlm{B|ZPGClMkIv(M>q0aKZiWlh4dFtI?gbahZoSd@p}j1PH^qfM_49C{h^{k>rMv!mT&VdvT<CP<q~B4O&Y3=4'
        b'zH~=jVt1uWrv~Y=^jcu3(+3QlhVUjg$AvnEaiMBIFD^9yj=0cI6K{hHb$D^1(}5kc=61MHrw<oee^XrOcbx0>AJ6JPW(XI$d;~7^'
        b'1y1L~Q~DmB;(J3@nTSUIi7`}r;yvI(+0LUxm6(G^;zFyg!G#|AnYd7gGn(a}gWre?oowEH11>aVMC%O5QQLmUxh*pE`NXTRtG6|B'
        b'4%p%<A2jso#G67x{a9$I_u~L8`o-Zzh7M4EI^pvpkfBw#M2711w?l^V*2>MqFfP>L!-a<W>7t$<!i84d0T=31K(L?g>`if@s>D0s'
        b'LJ@(1AV1xu5x7t=|BWCpf`%e=*vB}6hGq;yLlZ_oL+h_XLr35jz0e|u7Z*AP<XLdfxX|Ho7cN5MPIu{!xX>%pZi5T;j=Dm^Pggqc'
        b'8eC}o-Qq%b-7_xK;lqVqA#@>gM&Ls0{}o)QV;C3uBcW@V{WEc)!*(|OB8v+R$+#^pv~k*PaG_pW&U1urZ|dFPLhG;MLaXiy7Ybcb'
        b'8e1b!GOs{aM3}p)-|R3A51d1W!ZU=fHgN<lw0;CGv}y<!I^)*3Q1vk!**+h2?7DvJJPrE32{yE9BsTQrn_@$~8Y=t@_`3r(boR7c'
        b'V?&=Gfem#yKOuD8*I+|`a~o{vY%eynK4W~jKXhG?3Mumwd<Y!sm9X$ngs$RF;83l%?8o>u_)v!z_Sj44mS4q(Ziwx(#$LsTexGnN'
        b'd}#gM;X_$>s2ljZJA9~5<L?7MH^qm3mv9gG(E2;!Ly@fv)Kj~?#_~FdsDOot`mn|$l;u1?+#N==U0|Mg14cCACK%D18H(`Tgf7zu'
        b'5KYLr2|jdN!o;whH{e50c}8}A*I|RRose9*s0kUuhc<jQVHh7;cj1~DvirS(Z3M!HjzQ?q1}{3alrhF9c)_8>rV9ug+M{Plnf<Sy'
        b'FSZhrgez_?<Y`!kzAJP9H%2C~7||Q{s?!PVUiG<Xqj}rFw<HTUev1zF!ALi3urhD4@2p1vNo@<8aLuU;=Fhx9QX2~-HUHwGTXqq}'
        b'XU-ugsk!JUv)KnFMOe@bPQF;r;6@D9d7N`b`~!6WKf-llmxsSSh@(#ue}X>$m#r~P7_Vg#O^nJk){pczWv5wITA2tFBe&G+ndv4b'
        b'%49c$<T>8UGcmM@2`^(F31nn}OqlVK3g{oD5>Hdp&r^@I+YLu}A^XtbZ$HfzR-MJ*Mk^k&udx50E6&^18)&g+mS7Do0G$|U89j$^'
        b'P*W%IjGw8zz)6Ig{1ZysGi8zr%oIiF<XGVk|1|ch)@<O%2N4L<_#vAPLjkI>2hyDQ$smX!eS*PoA?{2{+8F_9E5`}6wmz{qvg4!I'
        b'Me27`)1>HA%<m%FBroG5^;p8R?NdW)fO-xA*JIODGPvk#&=v#xNoMr~p6)3Q%H%LWCX)kO6Xd6OTh@v@pZEcNxH*Zp?oT8hIYB;0'
        b'CM$?s;0Ay1zSEraIT;huQ%HQ`#y~GeON;$y;oh%2uQ>1h&hvacJw>i2$utK}Jc5Z*`!|Y@z8h3KsqDR=+G-2l<S(@tO1su1EdJW>'
        b'GHDq#^ORxxg@S!1gW+QLz5<JByZvH|rD^o`?HBC!3zsf!-{$&Zw83@p-1dtgy<x4(zCC8I#c(bLo?;fUy-C(QdgeEOZr^F~Uzd)y'
        b'@`zHchkvS$<7do3K7++ya_EZYCl7{!a9K`SVJ4?4gwVS=?e7IC-wh&3o9H;V(te@WaG|@!(BkUty;y0u*lTgwD`RRc2G>wE7FoGy'
        b'X6(#;aqUO?!^BY&<MDM1*o{L_AKmrSL{uMYuXtSYE~@VcF^TlzVmZr<@y3^MB_oNiF8MqoIX|1GB2Ru4Dl{sU2*_I9Q`@&!bwt>1'
        b'KTG@(Q-!FaR6<oke02x+^|i%g$+4Iu35%^Ok*Xeix=}W89*eIgi4yLy0gN20!l~KHEIJ@E+l^res~Mk7y)spy4w$%6uBPNvqpCPL'
        b'l9$||n$K0F1{9>qdV+}aIPpDN_@G`>nW!i;iKQp!Wp|RwK9RDOhZa8qwai%KBGipec55j)V^xuXkTa5B($*8KIg3*pRFMMB865eE'
        b'fk&ya=R0`;pUZ%^!W>R>og&Qn`q7wjm6aOHRH!Or0}AHIlv_CoG|5#{fl4OW9e|~a<(z0f_;{O@nd;)?B&Q1tNx~ZH(wsp_Nd=Cs'
        b'KrAQ;OR2+zNd@-x_RTV*1#uIzR7D2Q7Ve!Rg5eq5*&oyQtO{{#Tpf$Hu$8I$%2dXcY<h{RZ;8tIJCsHrI-f5xCLju(i&cG#RmSD9'
        b'Lp#$@>F2z;wm&X2D%ebiWBLxqG&5N{Wl2zVB)WI3mea&|lSg=`_(nNOt;@7AqM90p49a6d7pR&0a$_Hg(W!c8h%;lmCSXS=a2!-%'
        b'J2loA%#!HFL^&jp&*+)^G%%J(fr+^<UM!p75?M)ZO`obWu35-#r6PH%&Wyf1ri#xg?jr^Bic0#ljM&5kxOteZQ_he)S&d7kD5&XF'
        b'G68BvocB3tCCBC}pKB;2wD0|t|2fGm{ybvpV}qJtQc(VFL`2Mr^W^wQW8{*WZ$m+K68Cs4@AHTm5>is~ZA4DgiXTY-a%1_DP}&O5'
        b'0x>c$@>`2>FgTGMUt_FUGRYrq6QeM&1#ml^Ap<K?r5iKgi7avsOrmiA^SsYjTu^<RVaxy`T1J9CL|<$ySu%;ps|M3Ej!cC+(tUfz'
        b'ol6z#4+eFNTiAZC)i3-2*4)-}sZWUdeqBr5rFi4+$)G8DwWZCrq#P&zMg~^zK$vt{Y=GpuSUJ-W__RzmxmPJJW~iUy6X=4;6xyds'
        b'(rF7Gr7p#Tx(}I-TS4Ut#bo18Xtk|5c~3T}gwWP+!MH=jaS602w5#zF8hBEAws5{k5ksvlGGiEXHeR>#a#M0gHrv8qq0;UkupbOb'
        b'OM>}^q=KZZ$-RZ*?9Wg=r8$TA$HzfUNvV`^Q0c2F`;&N*Ks&hno(ed`KN`-VyEw+bpr?ujvZQ2cZH{j8m30~i!)s^wR_Z=U36C9o'
        b'lVbYbiErg0&R$0K9y^Q2FWI`G*f=P`iC2Mz&ajxicjHlaRUYyfyNBwN(&<Js`<>NzCVdGQe<Lb=DEWA{u@mL#yf3D2SG;jQN>e-I'
        b'zZUMLW#?tOFn(u1OkX?5!E2}Zrx_{Dgc^4!+5MT)Q}~h54(9%LCdBw#?|S9^Rw@J@G=$)Uh7;2sb7ZvQsG?PHz~87x8LC2lNfdz<'
        b'4C~d3sj7I}xAW*j`0+qV4O#b3MO$_}&_56KZSh|E=c&*mqtE?CX0)LSi`yJbP-$vAGfvHn@5pXSrrjLlW8QbH_Zw%&`vz)LGB9df'
        b'tMu~IMFp7-DUMR(Od1R|p)rZ&WACE6PZe#8<JtBzpuCU~av9^<$K4O;sqqu5aCZXM*{A6HEr=h~PK{fP8=q%&)uZSujR$Uk7uGH;'
        b'8Pc-m6VHJ$#>MC|ug#kwGaT`13`2w$3yl-5^4XECcPosHx2%2!291=HYh_H7sPk<_-)LW@NpgcRS2?1PF({thH;rqueO%WyDcbP('
        b'M85H{Yx40~Su!z=KQ@UcQtNqGuH+)|EC)kRJ6}`usp5_5A<o?&d%$N4R8nIjlU3O;bWg`~(5BCHtcn{*Js96RS)4$lZQ?cSX-WcP'
        b'&L}E5ro{>(WmR2Rd|P^Q>4LoMl4Ok#i(jH!spwp(=nDf01Rd**k;<W-#tNUlWIFFy%R}xzVuy^!*ZW496g@G18s}Bg3G|PiN+%dY'
        b'hGc@AFy(;8g3ujx3QR_E8=pi^jAN9({A?5V#Iaj`BhU@Dc@Cl*y4u-(gMseJoZ_~$Dsdtof*}otV6*W|;wBAtRYjj^d6+aun~G^7'
        b'VZ3x^EBgKsHyt<r5QAENwxVyA0^Bh)1-!+Qt@zIU3y$Sm$sxk_`Cz1!rh?b$>CLfGu`t@?;=~2$GbmJmywfcL&1k6rQA%1kku<{v'
        b'78?B8023uHIOyuOsF?s0BPMzAOXQu$QZN>AZ>2~rHA+!qNXQ|jt$sC~`F+l6Y`PHnS1ir=Z)H!$$Z}lA-UIVr@MKH@B*$?qodw#I'
        b'EQ<?b_wvpx+EvnLr2-@wJS{b5>&1p3*#YhmUaMbWBX+3nfY6?Rreo(utfOweu+`7`TP(j0*h+G{UiW^Nxr+klUWlgb%`niw^WZ=_'
        b'{8boS;@QH6;GhG-BLXPrz-*t-7LxqI$SELr@#m0=m|#gJ`MI`GW__G3yV@MYlufQCM(1@F_epc4MfsgDS=l*2hYXR(ImM~diV$M*'
        b'sU}G@;d}|RH@IwlEzNd&>g#)>344*NK{qDU4R?z>Tj-Xel1?)Zi_iqM5|&O!cW8^n)>qzXrwuI-MU5)%Y><dL>W&bI?Ru=a&eGQq'
        b'Jn8_?aESFi9LS+YHZ_vlRF||vHn0Udwj3{JI_gA4<S24$t6vEdz5ufrZQnN6l`mPh=K$Axdw>D$n<zj1Ax}ZE?AS4$?ehjz`pM%5'
        b'c&7y96Y%^=Ffs>(O?3ke&;g}Le<W`@C|<JSd={;UWaMqA*;UMRo`orHOB^S)NF$&dmNO)uFk`lFdzKZq&G*-!7oH7)qreN5bs>(!'
        b'QL8KJWs)3j`veY5hqJIr!k)c-X>l+eI?igQU4eF*z-xb(?CQb$d&D2K7&kqPeEZM?IJEQzOx~8)R=mWLT$&@L4F+C*U!-w9x4d(@'
        b'&}M9^6V)8x)g*_fc}(4k<|R#a2lyuDerGKV#3S4T&{LdmKy6J4wr|0n_O!rre87fm>l;Eu9r9Y45a6ieb1?pLW91fEM<+bp-XiO%'
        b'O{}R7p4}kHb&tZTc41AQcXSq%%C;BDzWTmlyc)Vymz~2>2rtJD@St}At59?>g!ff~Uon+fwJ>;0@e-3e1|pq?@#EpzCbT3cR_W6*'
        b'jRHZ!ZONt#%p8YVDS`g52W)(CU$taOM;&S|<N<4-?NRywztt~plmEaBY`zf24-YGxfqZ=XJejv)3sXVC7NgWsZZz-pU=B(M-6DJ{'
        b'1nDABiZlW!SL$81CDjdq9d)Pps7QD+&|Zu~B#)7NuP9I>$WpihWNEH*n!Tcge0A3E%s8-%wzh>efyIopsDw$B=rb_4KbB}ihKCU8'
        b'tpv7a{3&TU)I;#FM1OEH3L<3sE{}=8s)N5ntuQbJdws#W)p6qpBuw}e>;M;<W-{8puVTC-)ENs^63A}Im1;~Huku$?QCnjpxo$r!'
        b'xoN7FipprC8mF!s=N4TixESS}ss~@aZJmVhyDV>G&sJ*12j2I~-ZEt|H=cil=y{vHCUHUn+V0Vkm?Q@)d+%M{eV)V<1uI-{2pc!W'
        b'X}<Ry@jF1&aEwmW=WLv>Lh`uFa~yoEx;B`xO=-m~gf!f+(q%AFrl+uhE<Y4&&5Uj0>gN4KeBoj1J>or&`=9KW*dgwvYNoRPHr!Y}'
        b'wQ^gGp}f7K++c{YTU>R@srC-j_8M1J30Aj$DsqrpYU(Pdwpi-IrhaanYHxPfw<NpvitYPc%@c-?!?D-6>h5PBI?==CvGy&le)e_^'
        b'cl`rXr!`g9w%gx{sjaQFQb4?SkGS$RSKEtID_dOKI~>gmw*Oah+p?*3%cgGMZ>re0{b;hi)zSY3s%mdbWp%RgIX36UWJ8Uk57HZx'
        b'D{EbKPfxX%I}FV(dtGuxi}5#8?M=ysaz~{#xxdC?cr|&i1xi+0T)nm8mYUug`03vx-dh8A`p<|fzIpJQ-p?GpyOVoggPX1&#g}Tn'
        b'^*sDw&AA$f^f=Hs@BFdy4Hr4-i+4CH7VkaPzhB(Fum1!1aqSbg>?1>WP2!Mb_r9*Wm^J(T9B+NtVj;ws-4%55_0G{sSGU78klg>F'
        b'_-s%ASLmllOg`{_?Jqh7?4vJ6JaYAjT`ey10g|+TwZU{~+F48aGp44E75hlRo;jbS)WnvroW%8=>twQ@tDt>pYVuULl;i9Tbgj7d'
        b'I^Fu!T!%ft_~Jvz2eI~CIwI_oPpy+rZMPR0-$B!DMo30fhEQF~O}APmuRCM0_NRy~@tNsOypwy)0xUX|oC%)n{Zmo-$?4Yg$-2##'
        b'NugPY$%T<Tb`_YEVq=rAnRSmJ1OXv$Aj&JLy{rPt5RGI;CJe9tAbwI2Ke;3L;Z3dM0Y4SS*RJxDk+AMNxix)k|0;31vLaQ^i{z?!'
        b'KADSC$dLATg9=*aJYO-vA~IB7NUA}r74vG6ET+n=i}Ngotc#VEXqlkaQZAagPx2lweL`A<s$*;`F5Tz+#xq;UR{Z6Zy1^;!_MOI;'
        b'P{oH*K6u+}+8y1b@d3mj`)$e#p6R@q5&g6{YC?XXv`D{zhgt%ik#=Ir+D$NMD&LGT7%Avbq=+2P`v2!@#L|6hBL4}a?F$cE)rV8+'
        b'K7gt|H0n`RCG#NG%OtDP8sw$VEcVNcHQ9wn3G9gAfbi&%-d4PvBP}ZY)??wsRehm6_(MXR8^gB5&L$S~$VLqxOESAERvrcRQ0^ms'
        b'z~eU_X;E&(;8i`ZkBO0)WDu)WTlk;{+8(fe+Z0ICT>^teyuQ_&=D8sKeQdRb_aNPG5m(tD2s6CGkM=i2uJraF3*L$wD#Kp?lEfz-'
        b'e}asx7Wf;C$>l;aP%{=Ym>@OD-yHyT8n$1U<li$5njsVlJgdvc*s78Zm6O>t&#(&8L2Md_f_`TRAS9*NrI!oQnMBdvGmpRr!<~Qf'
        b'>dZK$?srq#>ynJ)kj}_p)x7ddRzlEyaY|llZUZr&JDry`L-s;SajIoPX>P~Z+$N56Un^eN>m~8@l)B#liTOqzB4O<g>fb5eyJwO='
        b'DL{ThIX;u#t^9$0H>iK9SbZ=ET%+Zt(x)Oh<>C^`9S*)@5GK*_e&8JO2Th(CbDZoqTqv-ZdY`_~-+!^-8`E-2l%==#;)%};{TI)k'
        b'Ivmq0Lu+E#DY4;Y+3}c}p7K!^@ywnzkG@MU!n%Su5|StPH@zG5l0P|0AB>&9kK-yb$z&HU6`eSSEf#<6CyS8%U-sTTzKJUDA3rlm'
        b'rfD+RNt1@s6q!j|(w0`!luKIy)3l}+a5n^Lp^xm-RN4Y7E{i|~;UNi<rnP7rm0l>C1Pg7~uC!i2khOF%0$X;ax~Qxuq9FRHi>$8L'
        b'h35A;lk~z(z;&N}p4a#HPdk}8m(Tg!&zUptlW>bVk|?>A>{i>M<;CiSvSaEQ&KVW#o8OkF9ZU$Bkv*f)$yL5cQt$dP-=uT4MTB(y'
        b';X=GrsrJtc@+TANO^W7H+oVa-IT&YV?g0@_uUIb|*Xy4q(Hl7B{*bw@FYbz#*j6O-mRKMmfM47sj~e*(TiY%z+?^LSFL9n^UdBS#'
        b'-0{7qy1X!@J$1_8HlC*DOBP9JiqBmk+J`KNfP7a3Y(MQ^E7>c6eoFWGmrlWR?B<EBqJs8|hednw^H2P3qD2zNIX~~rK#ux3++ksE'
        b')-HMeU8>~^V<@~XakflWF&=E^AaUvi{}KsEjTU!=?iC*(DmRTja$%z9`-#Oqw#)OL?Qu-yD-xA+MtfoW-*?QJjR)H}Hw$<SSKT|Z'
        b'i{?J}n<RQiZ#OM@SBzA8bll_aVB11l#WS3U*1O$xGa3uiK5h%G`Fz512${KXKQ9#D`$k&PL9R0H6|}tQPo{X?bQ&76z{<Z^c%o6J'
        b'?!l{-P2Q$d@1YC2-(T1zX%N(_Bx}ys-yx<W@!@~lb)R6AM5qUug&^*Nf4=1XV|yi_-rM}WO-Bw*#A&4tauzx~A%9+xBMEy_<)+nW'
        b'zL2Kw7EBZEQegD2t)R$9UgHbvJ$okF%y`IWvJYhS{a%4pc0dLWYf(o3H-`?Zfl-16;oMQRJH9blzscBR-P3I{;pNjE+7y_pWH_zb'
        b'lpQ;;U)<qjXShK9kI%?X4t-<VK}w9A!Wr3C_L~eft4#qb<_m*vLSfd)Rsm0vL%*B&9%Mq&ulW6H%Gv(U0_w)Eq2H6DbuuaICT2LN'
        b'iBCr=tkz=dBPnXPyiz@??zY>ISYNB{gdB%L_5)u;f1dJolFLn0CW`Cq$@p1qU2-VTtA`9FJ=hvouQb1LAy<?{b_nBM@VnLB2?E-i'
        b'QZ#Y9dIH_$?&?NTy`HVpy0D8Yd|9;Yjq_>^@*ax73zyG&;3>=28D)s33ttwR-#C9j<URDQ_DOal{p#W*(!H!3h3LE4I$Zii54(ru'
        b'vL>>dgKg<vzo3pm_|bD7C<YC&)vV9&PZm!L4d!pOs<axisP`rAL+p{liJmzVyS7Sf|BX|#l-nnoQW?`dExnWQ6cX8<NwTK0>BOs#'
        b'%<$yNPPO}UWz9`a!mTaFK{L&xPi2urZ?)E?o2v-mZk{=fpyO$UHus72l03sSp-+H1h|=x;G{Sp`O*hl>bVGB5?l*@s=Cse5I(r`F'
        b'-rC(30(>?6=8yU95WDjYZB%Raj#OF8Gk$k!cX|j<^Nh|8GVXK#62aY)Y0?gAzH~1U_nCh!>C9PZe26G^b}s~-zz~0nop`ptEi$Cr'
        b'No350#1H;k|I*FR@ud@afY52ufRBlO$WxNk`E9Bu{ubMX)HfkO#$)s;nD6hqH|fYfQq?_vn*fK=g1&)ZEnZio>#ZBO)@+p%LXHbm'
        b'xLsClZ*K!`<${*wfluC^{tYbz8^YI>y7PneTs?|-gLVT~sgBXKs<qne=HH))mn9~&l1QL;gEWDmIu9K_rD+`Yj2lS|`&I=3*?!<c'
        b'ytsE+W%{=?iJxFZO&n|J4wADZ9Te`XO4Zt#y@D-*%A~381MI8!?{jP4SU-B-grp;<Q*C|NL+-FM>gNyb03}&~)X$Ni+=))^MCt({'
        b'+sJThQmbpKgzPJ9V3?C_gxxCy>$T6K)E1<+2n`ms*%DJ?iCt!ivsEVHb(p?XwcA})M~kbD*e&5}&f8~&*xgpV1w@qyf1+ro-4fj<'
        b'Ynx?DO6A{oMFm&u1bd0nDw5CP`F=VC&`mm_vj~T~c!2NXl~f(>;-uS3i*ZYQPoICZ=6uEx`cH?2dx;JbdOc}T^;x3MS)$_}A%pg8'
        b'LHk;h*9z$BB_S|tQdJ&$rAvy|irssdf;|IC?^HBOTo8~|6C8M!k+id-Q3$^$IPU*@`G#>*sq!%-1kVyNTIT+6X&G~GWrdP-#2}ZL'
        b'h!#z7t{E^raFV7M5vGBj4mx@hJ-YAUoAlG~{4S#J;A`(pruq&Z#8^;$2cLOoa!TL9w!)4Ho4z2n->Gsx(@oR0Z>+Dm{|wRdy#Jls'
        b'r0y2`;gI$Yu$na&fB==#@rA#PrjugQ$qu^rZGL-}asqO@i<_6%(9*PYY)l2Oe@D0Yj{6Jl`i|b<`-^`#XF4tdp5UG7XZ^!|?XZr='
        b'$2~4QEPyO)`2HKi_v5}Cy#LeTGal7liO<-l8^&jRQ+E}7#_6g5Hhe}l^~d8ghNu4j_>BK|@EOGuZUmokAo2e;KH~$r{}=HYEoiMU'
        b'H@4=*+>kti7Us#82q_VMp*Y%@fpUplxRXmPR6LrUM<`DZG{n@uOd4a6S56t8wdPdg5BVEr&lT*-+HqI+*?F?2Ii_bsMe|fonr3l}'
        b'8*Ar0xP5U7o&?w`@m#Do%5e+Ym33Iy#@Vv4vOqIkzgf4Vo#}F0ceJzK*;E5(6eB#Xu&u{6wn*Mj+?55t9^j{g`}0V=w;rL!ta-EZ'
        b'8})O#8wK-Xwovsi6I-ZVvR1+2&_>SIfMa(9mm5=?-JKVcD`<K$SJNmcex$ofQ?Tot@qk|~r)CQE{KgO%s3u`FziR^fa*@um+0JcN'
        b'Tbk98l)=(uwmey4d1{$ulWreVQIZ&+`-R!dHP4jVX7h7PZgX2`TV8Lwool9h62xHae+toYn`e><vr9a+W*)#Xs*ENxCaw9V#J6As'
        b'd}FP_lC8GX=`e_+Ta9sWy!gZ@%hU7863eq{t_jBkm0Cxlnk?P#|56a+w{uNaUAHnOfY;cNaVcJ7I^K(3GPD=HVFX?y-W=E5#ceMA'
        b'$X^p>+!|u=d=lJ{*kI?L&VZETY3Qa`?${K9x4^we($q5VL|R;um9e^U&EHEbjVi-5k=?RoiP&zbcUhhZ;3qG$G|`lSYf?R8w=@}q'
        b'=p#=G9ZEMP%}na>@sGDG+kfKT-&E`&jg=J6?*Hqd5O)Z&)u-4kZbys=h>Ck_fX8m!YP*xy28$PNo;m_INf+n!T0F}4zE`$?Z;&8m'
        b'_V<Qokz*$s-07cDpuzBs*@#w9T_A`iy51g&3<uuK*-09ghN$vr$(E24t7YxmhoA|CNR_?pz?&7Xe43O~5lQ;~6vS@)MaVL)4nq@4'
        b'-)xuRZ`XdqZ%f<9Ec0qtulbV3-w$!m^mz5FFg6}}%Ia^GY!P`aTR=a2W6_&gvOZwv-M%sC<UYpy0qKnkkN(Gu>gdXx36oVXc3JA|'
        b'rQwwt${Z)dL2bK6n3S`uG~CQRxs2QNX0~kg9P{fJ=8Dci8$UN&w#*Y^j5=IHWQdait8s;FLut5yd(zBpD#|wOzmN;L<rV|CWq#<<'
        b'{h#Xf#qf*HHZH}?N!p3olbzvf@FOgo<sg}N6e5?U(U^_d#6vh@HoZbR5<|RP(}euXAsjKEMnE`H8-jdN+#H`uAHX<{!VZxydWc7k'
        b'K^}Dhk9e5NoTN#r{XLdCS7~^C{2-44IF~$+>^zUEF^`-99#si>-R3I<S%k}9#v-S1%{Tho*#=AFd<keOHOJq@HJ+Fu+ns$DngiQu'
        b'G+;1Ccx2xXapa?A+!lw~Z*W^3x1uhtX>I6<O4;g%4Ex_a3!1wea}w$_8Kn3jU*m%}6eMNzCkZOHlGGn5=@eS&y8|1k!M$)9<U{om'
        b'{AE#-!HXOenu&$#!q4ts77EWo@E12Yu0;!7T)iHD;8kx-@+S%H@C)NO*8Af9!0lI8R%{*hW-9)`G9z6lz?gUVdkC*KKfljA5m-GE'
        b'%L7A76=KZ0WDyKP6<5(BfvO;=j5|O#K~9GE$&%Rc=<_oQqSsf%PgYghEp_Gv;e|1jE|%weIsc8?f^Z%8q=DOnC6=oD{e@h?n^R;N'
        b')A9uRz&EeBh6ri^<1ekimj)_9#D)(DUAC1L>OLS1Ss9KRh+6g0!objA#0IXe@H5h=L$AJ^vy}lV@rP0w3k46!c?{F8z!+x)$2j5}'
        b'QnEvED%ZbI@=z2E@+}x-4nIg3T*g#mGy;-!$4PTc_!`H<bBgESk4INTJ96UFv6HG>c3*hKcuE(;kF{{TFlmGNK1{lq*Rdj?{yZiD'
        b'@A>}OBH=29aS!%mxRMAe!EkY%M-2Ck7%pGI*vTUR*XJx;`y7?Cl^ztB&l>ntgqIf&YxAYVXyb{d2PH#!5N|`e_sL~3;XLNRhMZQC'
        b'dIIqzm)sX#9v1?=2fiVU6DHktIn5Vf&<h3mcT*cM4drJ@$8G4<f}CN!DR}}p7G7I#Fi%@j{UuF^`p-*gGe%v7Hqe_P!UlPHb-ES`'
        b'c$;4&w3fyA$`M~9$Vglv`w~W8z*PPsz{mPCJWR;Skz@E_-N$1n)%Z(>bU){E-T!CDP+W|4|9WEpA;DOahG+*>%9y@T0LG8b1!(^{'
        b'=)s2s+z*U_hp@o{P=Qh>i>P7R4N!F=_{#ta-U!-LZ<KaBuNS$Cu)n-gk1iv9p`dtO$|emmwuy?1i)jTdD4zJl(xt_~eQiZ|(w`wM'
        b'a3l(`bg=E7A&n{M)v^(~o+dC}$2XOZ@~26bh>YVPuPM!Gxn)p3X#z)3&(t6zb$H;L+no4G{5Z`e;rutZvJv0hhO4<Jb-aHHen$Id'
        b'tSm7(oeW}#g!7*Z%Z5J}4werVR&!4$2<|4?+fx$c#+R;Ux6~t7+AZ9}R1evPqv|R&gWcAnVX{Mjijm*`UY%~LYS3=Am+Cw)MvSiG'
        b'@6QkXZ{ewWb^wPeV82vgEc7K~`GKLZU2N%p|L++~7LP*})NkGrdHpU448RyfEe(vLLl7|H(hskoA1p8<El7U=OLPSNsn?_5dkOuC'
        b'JpDhUS0nX%K4tvs!cP}-TaF9_Vy?08UmSC(-8U9<sU263xzyESuJy8*>%Mx-b=`c-edJm(SB@Oz*NIoJ4wOV8>KFf-m|I-@jj!yw'
        b'@d~J%KWwv?j{#!t<R2bG+>QZ=xm5DMY7EPLlWrj9I+BKLH5hQgQmzwkpB?yj$6GoCj8gX-zqXNq?4K4oOeD_u3o7`51dY=u{$az6'
        b'YZx9!#jshzIDm(S<0JF^N!QEwPX_b-g?zq0eUTvGFMl}QUntOV^>nO0m4)F?73nPXbx$Yj-X+ahX=e9Bbci`C9e*@EhBV-@<qVH4'
        b'?FYuzA;6<6tp<mBiHt^!4P4F$8BMxT8Knt$Pm>;)LtaO<(gawEJ|t<8IXlC^HI5gKJuIZ99Rl0&B>n@RoF>vSkJPqzdtrKANa7RH'
        b'MvdneG8$<iHJiMe1E#<MZ_C*lHqrrO9Kav;zpH}&*Z1rV``;-)%KtiQ0^WB>cdy}p9rkPZU)ztK^EiIWIgk9hbDq)#y#Kw~Igcp7'
        b'%ZfOW*&X|X{@0j(1O68hr6K=&`<4E8%60tjT;BiQ_Am3lH#Fy=LuduX5jX3DOK0-F%kfwLb$#%poA$xfG5>Y#8)$qJO4a>3$%Q`^'
        b'ueb9C>Vuihrpm3ij5JUm@2X0?+Qq*NjA0Qm!ddMlTkZ_nrvv9lm6zM6`8cVI!}gh4oXSLh|LB9!j>?27ss<O>XDM%=fpxDb<1sc>'
        b'>EM{0m)K|ZV~fPAB8|HdUnK;p1Te5JsWVi;xP!;EuFqKn_E|aXcKQ5ha4f-5P*$F3dWdM89}WB1@39Oj+eioGN0{Uvw9f#|7fxb1'
        b'R6j;xAes8|&jR*Y$?G;x257#q{D*m3nuzVwH~%u)qOL+)!sKDXu3?|fLER2=66}+@a!q1*AVop@^vw_OvHr6_el&6n0%V;0!()iM'
        b'72BsT=_bc;4IRI749ls>*ByfZ_y1~HKnK7gGw$Tm3VVR=g+TGU#FygB(xdQzY2J#4)H$%CH70N%%SgH>-6-8%yiPp2NbDPmy;rYL'
        b'G?*YQoy<1B1^GqDeUU&eWECKYsUk=%3|Z-PjFw+EH3X8VY{mfBZVZWJb|b!Mqd6;MeCT*HHtc%c^Xs%u1_Cj(Nk`J5+J+};waa@S'
        b'gkrU6Pbg<A#w%u;xo68_DJl!^Zxd)MiDG?h@qL-nNrwH};)U$e2Qv*>XsLrO5Dyskzey_t$XZIF97qWH1Vg6iULTk$ghEsfLho17'
        b'Pn4%Bz?GHww7NeNC0QSrcxt1{jCb<-WOx?QVjcIaK9BJsv_!I2y6>~ZBQ-G{)ZP%gWxMShejy@F^&ZlCvoHph%Bd8J%$$c-c}1wV'
        b'kbbIs60tYL{5(-qM2FJRri1Hu(%Q<VWIN~W;<j2-yAO-;0jJw+YvcG2wmdFwn^{cMR<X(r7*pMKkZ@T%`+5_P{A#Gr?)U)SR>7x#'
        b'hxT709q;)a3giW<+jWN)m^pW`eq#Pz1|iS|gDhT<sm~#b7qCm0XD&6e1#e%3c_a)`XK9Qo)A<&>zuaUJnk|hr-v%<ncL{UW#|BHI'
        b'&Uc@Sdlu3uZDTinEdjZYQaC+;7iQq0td5a7Lq@Vl=O)a2a|SmurC3Y2Mrf$`p4lbuk|k6|4W*g`e55r?S1~mq6Xt-7OWcnXFJuao'
        b'5*N3{RMmYtk~GGl=v(@{v7di^%zw`Ej4uphe>8l3KC!2l`F_;NB}C6+X=D4gDs>O{Oc%G=%QXWZPFh-8ZW{nToa9;xKA+UZ<D%?-'
        b'#eU#ym!$!e*!vf<p&gnzuv^vm=-$fPp8M#N#Hz7}oS%)V+U;5_fkNA=Ztd~Lp2J`7<2DcdsU=~cAV0;<w^WT^&jp&XOEQ!VLTJk6'
        b'&FI14Z;y9zk2N(nj-tn?_B1&g$5!orrTz4yA&(yKvo!d4XpfUajsCGTcA%htLZDGA#<6cuR^rBbytzDT%43IYRio&5RbzEU)!1d0'
        b'$6c1kPFG!{t(I{E1sR%UJPOoO49L<j{xs>+Ak4`{-KUkLFBV0Qa(QEqd77FqgaJCqHFW)fIe5!^w{|U*E?X$sR>=h#I~)pX*Jo)d'
        b'jT!)*>jNIPb6(FUz>W6jOMGX&mWDwjm4+d(s;3gmlRI2o14dHWU3M_EWT6zwZL1tN0%!@h9TzcBa45QjCv&kAsKn-*-F;d?`eIOY'
        b'sNEae<f*Ra>FW#7H>z=LSGlyLT(ZqENS_#F3?!B^SjIqNLHp=Sz_c2G)MX!H`W9{n`gW?y_AN=wN$9Y14H!gcclJTCp`52Lh@uma'
        b'ajA5mKq4PT(P=Pn4WP5>LLK+`BE=y5g&m`|V5pFHF=h)4`O$PL1Pz07;kHgu0|kq3(eVHs+B>Y^UNoPKF5$M=xu;D9vx}V2pxyGc'
        b'@^2x=Sj0;xuX~%~gJ|(GZ)~+^^=hLOc@HsF^0rqNwLO};%@G|OH@5LO0uQ>NT0GqP{<ENZuJ_4KUE;#FR|KuEsLFEU_vXplv-6;V'
        b'ZH^5A<c~lj-G{BGE?iVfzB9_O4(wy*lWNZ=v@mhH!Sa|66w7oTiW`O$Ykyq-Mdjj)J`u*YP=*tOh!}iZuUq5JU$k?ZUEI@`fKxn;'
        b'_esEPN%d4t3u)Yb-q?0N@Vf>7{^GpxtMeFhvJpHxtr#yLjg<qAtpjTA>EJ%C24Qq{(o9N%oG~+Yy%MuCk#fp;oWaUO;$VzZuq$Ra'
        b'J{xYA81GBk@QPT~Snquc@AaS4D2x{c_BnQtWdh-vbCe3%6%;;!!^t$fZNG=onwD$X<xWNO_YI%aw~lfOrOqm$ITtw<lo;(5#)(N~'
        b'(*X4~q?M>OyFu8TSihT*wslF6X0y0WsB%^*j1;mjV9eP@`~Gb6eq+_!^MrI79nttr)hF{5{2s+!Z#DnJ{`>4o9!o--fSqy-Lz4+_'
        b'RmnAxl=E*@0!oD9vy#LK0=O$50=XE(e$cP5ClDKj$pYmYqG=(%QRuL+gRJ6gr#Wb<m7+uQ+uNvCLjU{jM&(}WpzPFnf4<tu9gx+u'
        b'uU@XL=(bk$;OX%+I#;=inliEbumI?I2Um6~AELC*?u?36RF!hAD4E}9D%=>dmQa^JM3cJm2My(G&E-o=%71MyU#2d9KwZ8@UA|mh'
        b'{;;}ywYq$zx_p&Ev(~Ozs}mxXQ>*{RQ22qpd~L77aVVtD8ADe$;X}OLWsI^+XxBWL7P(D6+NF8WV~<G-r5`m2P<}pypPi4$9AEmo'
        b'G!J?;55;}ySMI*(`^<09tb`h>Y(x3V+(=cbG&?UcT}*xDPntaiyu;7XG!nYKn<^<^anAj#lkVkS_hLGs%e|z>{W!m+9iH}S)|$mg'
        b'b-b^9ZJ&F=J5Q0u3Zif?=@^G*=2kvM!qm1fEiI`PU(STf@T9CMaQPsDF5v%UWNZwXDz1EqG}ebqZ7575jiqR28ZNyaIb0$4;!EE{'
        b'P*Fbf0KWS(H1j<CH!eZcqao<tU6p)ecK3a7;iy3OIx8bc$0H%Wa`YXPDj*8)oV*<_^r$dH(dS<H4&SHUy$CmJCaBdRJD<WwXcz7w'
        b'jlV*D?)#yDZ#<%whoDcP+GJEXU1@hO#Xa5!)gHvX<PygFLtyOghw!hvq1I|V><MsZ1@umphESOV=FN~OfK6$k(p<9ufgo}s6vlg@'
        b'en1qZZ(~tV`Va)=RH?aR(nEEcl^}>Qs#M<{BC}?NehzCcUr`f5{X8UE==1vZrinEXz8N8qn7s2;$OI>-f<uDn2r2?0{hJeO#`>~D'
        b'`ou)xmQel~y}@@2qVIByLVQKXw2<0tma6mPpUOXf>_`vkzK4PPQ$p;T<-PCr?K{hiMH`9m^5yfy^CHb|t0|i`ZUEDKLr5BL3+dCW'
        b'II&T7%z4%+vmbb~dV{@ug>S9DM&Zze0If-a!c>WL60J0pub>|C0}mdGE=dp@#UXSAwBtC7`2R+{Z^-OLa5?K#e6-kHzQ*x&;1TsT'
        b'FlKE>h}o?_)gy)*UKm0I6|6W@1b=9e@e8P5_fEXo%ffG0`I=~v@ifX=KvI+ZX3YarAg@eB&p8UW-f|*UR`L#!F}YQMKXpYto?Ts@'
        b'?!I@3)xEoSLdL$se>Z6y3;DXC(2L93p=?^KfIr))M6(QL(vzd@fm2?}AJCOAo1zw}HNVD-dTL>kK@HZbS*p`4I}rqUZzWyt5JmIa'
        b'L>Mdc+Qoxq)tZ&+d_+yaTN*zhjX-fh;Z_=`FaQ-3TLnhp74)_Q=*8sXf@UZ<35FIqlGw?^#D+lc{Cx9T<N|Ms3fcnL``4w{4$h(o'
        b'B@2Cj832kPd3VI4=cvN15}+hw8jv9vWN?t$reSJFdEX&$u?(JCWKY&bpPR8TdVQffRTT#=uVjfXc~p4}rAto1Q=3YD&2))Qr`DFJ'
        b'@dm@icy`k&C{nkPcp?PF=a0fC1tg~cwYaoFy+o&u)9T`M!`w}f_}=oP(Vz_p=()*-TSpD^_HtTJJr1<`qIp_FgX5vb{8Mz|96d;9'
        b'2++yP;i{CHH7iZGr_7TiL{Y8&K{^Mu_A)w4H~h48nn71@lunR;mBhHtU-zBH0d;KOY3M3@`5IUGY9Ic%an?BvjV;*@zXgbngNEw9'
        b'(tvT&E#~so^d#_a&N15}L&`t7hsV(h`oBlO{|!)x0{^#C)#xf;3FTVHNZZ@SY>T2G^y9sqfub!oe@&F*TM-oK`~zoCKy-~)jCQnJ'
        b'y%O|B^=oBur15LAY!XRr5JpS%R$&?V;<*HPrQS*O7+3iU_dSfVA*Enav|aN6C~yVnMJ9S~eC5^vBXb3m@KXJKz<;-7Nx(mpRC*=B'
        b'QpPcmKLWqMnUNlCuZ&Gq<r=`;mgunY@akBv4l*xbY|enO<&t0m)zx`o%x@@u_b6<iL4FTaiPh?2b;0tz3gc^{nG%~vgU_gw^hQx%'
        b'kuJ^hHlcltKs|=kq$RIeR9pLv<`vTSDSq&%x;6Afm&{&nvyF?v`H#j1bw1+jgsSJ^|6a}V_)t{?-bHTD6DL!yBEd#M66H%q&y@}G'
        b'A#Ios9RkdWxL^3ENtTE<itZLUVz95Q^h$#zlZDjxe$0%&^UN4OS+%ev$c!t;b_qMu$Sz>Vqv>L-N|+x@uF8+`THScvAnrGnEZj)l'
        b'P4Nd{(-gj(M)kN647jI!UCWn(9?d!!^BYa1@qVl%AY*R=a`h6BNJ0wUHPhMyA+~*2bf4y7>7G}j+vu`sBClrg`24Y6Pb;+ID!2By'
        b'#a(W+wB2gU#$0!4tkB{~Piv3I3L1DkG*D{wSBKu%D`+_*@RmOe&!JSAgrt5ha<{O(i@mcEPhpql;WeLcSIzFxtZeFaX&&w=Us;w8'
        b'bS)mA7vj>akb<tSxbW0-FIu1IuJv%zmv`<a%QJ565JUSXUY6N@tA_qJN}%oDDBrKhri?b>*)rLL)WaeNfewcnfd#Zz^I${N=`rzp'
        b'B|uz&4W&Q#14Y1z=BS!zW1`6VLidgouKa~D%?lu#hkgq_`-1BCw+d~Wa0fM#HepSKvHYS>Dp0NvE)hf40)^5dbH(*rqqU9Q8D-FP'
        b'#>8~7br%HM6{UH8W&6eV$NS_sHG#sW)b66}qO$bJJTVyXVr;;^*%w_y7Ir6k&RD-Spf3vrj^Q92^k-@QC6f811KXInK4@c5Zp>he'
        b'$c<iK4?Zmce3}9Kw4AH?Gz0jwMp<xqx=Fo=#7bqrI+YV62A$&f!Vf#OVWnC~_A06Gg<j1H+Z*G9R%ZN8s0NFn4B-NGIH{SaS+me;'
        b'{YJBk^nC#7HMTM_SeebJ4(!c-PdI2_@DMKJ#i~b6WXtjm_IZLuLZ1erdVMfNrr{~bC8h;3D~$*1nom+=c?Jxcpl{5N9Dkai$(0^@'
        b'qvOX$brLK^vjU_{NADGs-tJGvo~BvYJYJ_+F=h9ty^>bSCJpKe1rvr6&8oy~RT)efO3GLH;sscz<{|U*e#lbY&obWfiY;QLGp(RV'
        b'HSA}n|B#=Jiv&MAKj3H0m-^Wf-p@|Hx}Pn-hM$GdS?##GpDn+JpDh)FpUnwsz~VLM?d7YC#k^pJB>`tUd0apZ(mo2hS(^{f?UYd$'
        b'LF{c}^<3;;RgU;jj2cstM<t6u{!0W&BI>pu@~x#}kiJ<{u_WMJukfvy0pIcrh?}gMYrfpKmS4lS@}Xwfx6Z#R4~AnqK2srC$kTui'
        b'U(tD9#n%~AXc|1qse0^K!K?a|czOvEZ56AU!KWTN3@&w7q^cd9X=EFCj)%+Az@OefK7X{=v*QwH`gL5unV$6Q81$q;H>!Psje8RN'
        b'(SQ^6T@>`@g9iml?bv@F4&B~BIwqrYas)ma>d-Z`^j!J6)$O+Tahsms#hufvYnAkQT2CgXb$NaVZSUT>`uO3n6EN$M;zpxFyq@2!'
        b'ZU=&Q@AOL17svWM*1$%8k5$^ZdQa1%U1HS3XBg0aAGpxJ4fJW&LDhm+E*d$YV`Y;Q{I@;mzwZbCZ3q7ildBajO~r*p6H;GYUL0`Z'
        b'FYVkdD%?#{A*h4Ge*7hwZ7Rp3NI`STqGP-lpCjwhRDctwX>j6)F;5#JPmdW5{R6kb&Bpz002p3VRMTwS4FbdVwdhm3rlKa&c<~>_'
        b'FLc{yBU-+rlhdcISM5>85QTffys_x)9+{2ff-c>qS%q_{Rn*u2K%ia9r-Z&xJRyY%CQR_9*<jkL#=OWWV-ij)!U6-|D{lGk0ig2z'
        b'A}FVeM+O1X=U8FBT5!*W-Z8%C1u!jbN~P+FtNZrcD}8&*v4LT`uD`^tujSiB0pC^`IQQ&w-<Au$J&(_;gTC#`e0A8h@pf$&BuQ+u'
        b';)0&tXBF6ala3UqBf+E-?9cx_;M%E$0zQF)d;y#GpV)wJFA-ebxWTlOD9V7Y=i6Hj4Pf7n^YszF-SN-)_8S~OcI|glFxi6Sxj`ju'
        b'Y*eY58l{jbtDf*?A!~Yfb5D6{6r>a#;=PpZ36{?`fJajV8K9(~nbSfCvy@lcf{8|qdp8@%G)^5DfHb2ys`80(lnk={a5_|<uzsU}'
        b'WtZdpJ=7&ZP4%u&RPg<G)|l?zaNjrqEw*PNRaed1<$I)%eyn7Jx~kKxf~cZOP0ZGnuY#yTJxL%wX~%AOMYISqc@t#rt?30ThBJ36'
        b'3v{pY+PZhDYv3o%-C<r|U3GK0`<o=hl&;u-?p3cjr-qpF2NK)!h!j2{kiw^bcxnEAI~&N~m5VRntbGys!Svk-A!g-ph%t@~F*|lz'
        b'<Gcfd`Md9bL;j9q3<WU;U*j0#`wtY%;Y(9S<nRxZ|8x#NJN9}xd}-39Is7lk-XaJ;c-js5yZ8Bl+Jo%&%_Nn8ymAz%*uo0jhuA=s'
        b'SMwp5P!ixbgp#Gb*4pQ+KxiPC1WMz0@>npQK%Ij0i^lN?^?@%v4l$+gYIA}O5Kv-=X9c42KtLIs7_^QXoERvpj|Ha%hw*{o5KF*L'
        b'U5Ui$F}DsGDsVOKv4Oyppk{GRv?C5fOMp)}(m%FA3Kn{-5&lg1OoYSCs!w4qu%O>O8^N?85MyRPq1w|tseF&DRftgo_IPa0al?kI'
        b'N(Gzs74|D%7p9yZ3o!;SVrI`BlNTzTV}KaroHr&XGVXLlSb&(lp`{xzE$>G`Il4MG)GS2WIaad>Z5Qo__)-nct)#O15x?xn1gu@T'
        b'Andt<N`7GsPYw8Wyi4=P<pWCsUUo$OxR76Ga`ApPFM53?_}Ta?{cQcEe%3iShp2`*1YTzf`q@F}aJ319vS2mDm|ZcvohzeO+xfXe'
        b'Ai_)>KQwpv6EQNtOu;-<?p`)BygUNo1<xB632}H4Iy574<}32XQwsu-<&vB^ZOFgf{Fu`O)%JAp)nZHiRbz{Ai4Z&e;-J$vDz6!5'
        b'a#Ew3mz~YVaYktS{#IUjl}+UkWvEM{%yaJrqfFS~bhf30SC%5Y;PbPwd{EiZXa#lca*KC{K1PSSpo7$I)eAX$M%8#>n)1=D!D)(G'
        b'vob>s`l&8o$*X9x$no3nA!$omB%Mo(3ts{2S&_8De(*h*v(TZl?uv1h|Ch^SZK~&&lPjh+V^SpMP*gZIZff=RNu+NAnkv~IVaCaw'
        b'8YS)C{uDl2Jn0zze>*bfqI;|1(s3Iq%(%t-`fG0Y^1m;}#})Z9k=Je6{u1f96E4aMGe{!~7Z2fg5;4e_0sP(h34UkXrCD9D2YJ1y'
        b'&n<Rmvwh{Oz3uC^f0AN;ZXH-cjnj-XPSqTs*R1(3{QtjjZ1ZYXpWQ9<C}Vc-?%IsH%2#_7G45=}C&%w{HLE>L%-OxN-R<5c<Skzf'
        b'UC`A#+gDP5_ro)~{hjt-8vo`;6$=)4pI_(r+V9<lVE)$SMLV0!-VQ&s<847eOSFWqTw$JpRC~J0EBZ7K&K)bAGjHs+h!9m{<0y=P'
        b'&^74tu)oO(`kUT%pxXR8o){Lq{(0qsM6(BcU`0`3<x4X20YA9OE)l|OfKvy|<rVPIg&!6+l12p)O?U5S3ci>M*((s+#k+31X3gq7'
        b'J$E4x@_b3*f?pdn4>V8C;S(^3&l%~CeF*%8aUYKPIlN84JSZc>u^&R|vgq$;q($3v62_^Xbd6ZcHy%WlUXpqP@$22x>m%2}|A-$M'
        b'djpS*hw#2J$UG7e^!ptC<^($Efexm&^7+SQYxSoR2L|(x9RA$`Ji)8A{JVt_^rT)&4_?l`bg@2raIs$f4v}ww)a<f%3zb(}t2gH('
        b'p9jBIa0JM8<nZr823NnY@-F1mxXb7r`7Y!~(F-!k&%052i;!;xLi%o@@_mtk_xm+U#|)krlA6sY%s~R!00Df`=DP<6gK48G2lI^>'
        b'Ej0%Po;ixHe1>n0{)9B9qRbq%S+fT83bbqW9#F2Fr$jBEV$hpYe;@;px)6Sp4zhCOa{N`~TuKiN=b4xD%>{hx=Toc1R8_0@Qohw+'
        b'$~Wf-zExMXi7)3{{nhxECz%%oks`pc=D+7`9egR^5L}uM6F?=NhX6lEyf@JCY>kO_<|Itv*$RBp#8bf~qiFk-OLM;=(L(N*Kcg+M'
        b'ADpiejF3~}N0tv3o+klMoJ{eKSm&`CG!+?Bz=@S;R%$197o}#Dm6Wga8PD4_tCaB+_<Hpis=UPHh`@QJX1VeS(1%rJ!X%o6xg@xn'
        b'69$M_xdN3MCK2!B32&NUo}fgt+@KVsQ90@l`PCboEGHo4F~as1E`sM~YR&S3k^vwR8Z8j~W6d{)@>OchszFSfU2k=e>fdK;Hfy`w'
        b'R$BtD)tj;AoFg2m-PVMU)dFMNTk8CEYQbIJLu=Lfgj$fT&PQzmNP2QVK6{VM^g3&c;dt05$lCK4@0A=D7H?y1FXDTP1PO1=`<Nz!'
        b'm_cO%k}{*3Wphh<Cv}i<`@f#$XA7Sc<%Z+&&AJHJRIZv|M4r_TKZso2UV@HlX{F4uV?s{dVpdS~r^Mb^rR^Jjo-nxA!s?8%-$UVq'
        b'<IJ?2Gg37aKDnU&jKvs%rYvOjFS4wcZSj1q1m7?U8?}O3vjVC?owiu-0t$Z9cbS|l{BC$#Yg+D9Xtm3gZNi36>f@953OmS_Fa6JD'
        b'@U7mWR`BPh010nn61*H@I@y+|Dc$pahYF#1p;Vn9G#gO7LZwbn@O6Ghg(0}W8$4K6*ql+nTgLD4n6f!k<!lpHDI65~flVI0eZzh3'
        b'#C^6BdkIFymex~4c%QcCSRQNWu%P9$0Cww7hcomldnL}$E_N7a=w<dQI75@Ue;dwFB=_TSh9unok2Cat2WO~>y%C(DTK4}o&QKZq'
        b'|02#%CMZe=xmVCTw@T3=hVJ$I*_H>tw!6Vol2wX;j}xga&33LCZ~C=t9s=K~amFt!FrW@`+%LZ7%E!65MonXgnrn^^hs=VzZ=4Qp'
        b'JRyO4&Um|}5$2cNe~u`mQ(GFlyjtBpX7>wTH*rc&*||n_Jn#D>c|RPlwB0j~$Mb1~h&`o57@t?*6?Acpc+2Vh@1Oe|I=K9ht-Nvk'
        b'AzNC*KE}({?tXF2x21PbX3NvYZ}EmIDDRHaMN(`GQ|8K2H-v2J6YyP1>p$lEOXvIB2XhoHuKr5P6snJV@+9}vIc`%Aw>i*v=|2ds'
        b'<!Rpu9&ni)gbu1xTU=Lw2B|%@T>-cub;ccQzESsJupxsbn+F(rR?Tg`0#C@mZPx3$m9s@9T!VcdlSdi2$J3RAutFv8k{I#ivD1%8'
        b'@FrEfpEdA-e{i2FChycqe@ztibP!NTUuF#;3Tg5F;Q*wNZ{r9^p)?FBG(7+*)N~o7kdHviESoW&&}RIp&t{A#^vt+x;R&r9i6`{b'
        b'IE*L6@pwW%>kr}yJvnX|PiSWU4d4k)zYI@k^9Vd4$MT!P6Pg#YjB{NbCuic-aB}R!ctV?R1W(BIZ@?3p?rXpbGYlux<iK!3n@7M2'
        b'`ECpGa+@dQd)?^9@Pxu{j!&n4brX0(u74SxP!q-z+RWn#HI2j*Y6{{BZN3_w(B>=fgf?UA+RWn#ZN3su=-@D((B@0<gf?G-C$#wz'
        b'JfY3k#S?N}3r}bw{=P8nN_>fyxi^U?<och$6PoUL<O)0?*LATCCgN{v)2{rswlx1o;t9F_eRx6>f8@8du4{iRcG;J;jtv1Cei%>a'
        b'YI?(empbVt@q}FeK0Kjojp0=MP2vf;{^#+8CXW2JHf_WQd~suM7*A-@jnY06-{1zmtqtM{bzB=yNF%fdOc!)4<(k+x*YZuLZut>-'
        b'Lau)io)C{F<a_ZN-^8!K(r)42rFcTltKtbcHlbm%uS&&bRP*gz7f<M#{{H)c|1CVlctXXOd>enW`te0zEVrUdInD1{xMC!!H^=65'
        b'60d3g(^x_iM_>u1jldF$`{?Gdgsv-xt6>S<sBX`vjDNlG6UN)Oek7KV>wg+c$hYn)@%F~BgdDD$jkk|nJKhds30*VZ{_ZBRgk1k('
        b'EFoX=HL--Q8E-pBU<nOHTPo_x5lp#3){YFe&^x+;aQkCoZRxgwe|N0C0!!#;B+mA)jwN(0!#ve^b67&I{{bwaEh-*MXlf8kXd1>6'
        b'8ciDT*sh8tbmiCrSVD0%H-{zUx&f@0AB`n6-M}>sV+kFK8p0AX2e5>ij3ypS=sp#{h|xp~shQ-}95BwBu8AddP5=AwAePY9f3g2{'
        b'JbGjP*I^5I--nw|=WHFqns8Wuin-2Dha+??zg1dxlQ=>*>wAAf9HDE*kD{Bz5pw;@aD>=v;Rs#Z|NiXeaD-g{G900(K^!4IJNf|}'
        b'p@|qTChaOXLYad&LPu^GM<^ZRuefd+N9Yx7o29&M@@rn#!V!8tfFcC8S;^ZbKNiQjp>g~u3?bJ~j3IPQekR={hLG##@OOSn454d{'
        b'p_IKz3?bM5EQZj;5g0-v&GMAuCNYFu|DzZ}Qw>?uu8$$qWX_s?0~kV07(+-PAHopwO}jY^q5ZNThEVn}hLGV0FoZIAUym__L>NOT'
        b'm%$JQJc!V{kw?s9Frbg^WaJ10A=Mn^Jwg}fp(DMa$n`wY)I>{bcRjI1+FM9(F294=7*ZJ;SJ<RB^YB5Y)b7I~NI<g3@Gr$Yw8$Px'
        b'6h;d1Dzj(bYmrAX0$seQ#0Py9o~P@}cap{r{rJ268;1*W1mS|30&qc(@Nhv*%_5%t+CjXara`=*CLS-S=^A)J(}(ebng;QLnnvIS'
        b'O}{o?(9zIgyr9@i@Peo?9xliq$-@PGHum7|VX&aaA+VrQ-5^-dvB}p33;OLxUqlXq1vR!`iWSrtz>!HFD9G1c1uJO!AXd=yo52d='
        b'8~tNk{6Il}($%nnX5Iu=P@t{Sn1O<f_<tHJsBr{VP~5FUSV8LRVFhi8ygpVC|8_ERpy1HhOR$2PZU!r;aRgRSoMH$oDDrw(K`SDE'
        b'2rDQc<G8Sa0*T^ste~cJ;Ua~OdyGHerAd|AlntaCERX9f_;u{*^&wE|(TP3^%cEpS9==iu$RkY04>ThUbX@b9QpasEa8H|N&o0W='
        b'agQ4;Pb=TTXh9_)B4hV9#fJf~pt{wo98$c-F%m9F6&yN-3u+Paa6v_(&^jNlV9=nBuD_6-8Ii+iLBG2SS`bg$;TANYjQS4yg{xo%'
        b'%{!0KAX*S#e1FTui^}|q{2G#)d%V|03vdc&dCVugY|L^0xTus2T;)CfeWUr;@_PJIy)(`LKCclNp&k>27s`49c;TS&o*$S(@c={A'
        b'*7H=$dHyGlFLdU-@$>W8zcvN%g~X)MI^bv?!WXijJYt@##6sG#a9{5dXJqF&yiqIen~Ou|%8_<CwdTEAh!(Sq_Lwnd%T&81-7XKI'
        b'L+!J2oa<ed@penRb8CrZn%$CUcUz<8dS9Pwx2WxwxMh~<;TAUB5^I|_nm+?@>Pc?eIc|EF+j>|SwFmEAyLh)`)8`0obdXVd;!^&)'
        b'=A7H`gj!~tDXt{NLvTP|ZgR5F#^FW+m`0xUN?TO$C;xk$(l&a;?=CmO+v*T<C$dB5FS`A-Sd&iMdPY~P?Ifb@tdj|zamxK}^mEHQ'
        b'e>YnHENlB6Zl}2k0>99<2Vd75>)bUOe(d6ZNcatdcwgIw(N3}bT|zC6=i9KIQwI0Bo$4PvqujP;^j?8ed|YIYPydoSEbM)f9=mV*'
        b'=)FP;?_VRKe3?W{3-c(0yE=~?KFiPcVW6!qMfili(tixKw{Y~ARIt6kX@C6QM*fV<0y&ySBnz9f*PLt?sf9>A8^K>%Kr7gZPw;0x'
        b'+kkJQ*NPHS@`(8Y+IhFAL<k8@`=)cDXg+E6GX<{=B>lN?lcWTgGj2jGe>&nzg`0%%dqV8}-{e$sQ-wK7lFC5_5}Dl}nzEUDHxw#x'
        b'tS=#nWo|~@LuQtap0#vz!GEI6cOqszFna0ZDaXZ!L-6^VRkH6hZGXk%dRNxQ1@767D)8~Wv(9JIl8xjRNwS2F?(^aE6sHT9i~|4A'
        b'=X)(0euzta2Ls<r_xYZ|H%dx;Z57+@-PA9vzhmakMq%qLO-A;+v*=sc4sGpUv~RYv?l0EY{NfC^roa5Q<TJ9`dOQ1D`*FIdiQR5z'
        b'HQx4Zi3!Eeq?Bh6^r*x|i?<|8I_SW8z-#(T__G*~`^zNEnUo}T8j*0z7E!YB{TF;RY7S#f_#F^wGOVvHE>0HdH+AO{&Ck|Iq-jnf'
        b'T}%lPDyaV}y`9?YFBtt-x{})CpB6Y9cJO@0mQVe`b2dSqrI;Uw1;>SZ$+*)a?*HfT{gzJ#?}Pm0qZ2aoh>Zfe>TWTXUVQt?Wg%!I'
        b'SzEyr>>NmXw=y8T(Lw3$svMTyhH<>~9NAcUcK3%?ke;(rK^hHMdeNc@YSYhCJc}bb7e#>5iSlH&U-81>?v}nQ^DKzyyf5Og$hHm>'
        b')|N6Tt~LI{5?U1$nP|x<yzk+MWL6lE*~FPSjlwgWW_tD+uJ&y$`&%rr<FxxP>uctpN$Cg+$m}UzW>Sz@i=B-dA+zIjP-fDA%sRq&'
        b'nHd8z%M8eD&ABaPKxQG=mf0C1{T5zk5ohTZ>NS7CQ-7s5fb1@lS?QS(vN<0yB%4zsWp-}(e(9+Z_a9as7dgfH?r-ezY5eKZgEpIq'
        b'^!jf$3Yurz-Ts_iQk}axom_LCKY|_7Oga)fC&c?{PqQ+CVA~mY{RY=TTl6oTME!&XNApNict2OKG^zVpLc&!l;U^+ytVG3|T1Cos'
        b'k?nCMj#r*qB?{HM-JRRTd0dTBPM~0ghleWMzAaMHS&577sO@ZWuKC{GrnOcx4iU21mD_iP3ouO*K_=pfvsEaoh<G9xLu@OQb*q)&'
        b'OFPKUGG%3(rfwztl|a)B5k=vTUYJhy)G6fdR*a8k#wU#_XePTjqLpZ&2!{milEKvif=9K(*QFxD6xCl$^c(qa%All|Lp^Syw1hB8'
        b'`t@x85KjuP%@gw=PYgpt{Ke4*k+NE3GbtSk;K__3p5$;jBX}}-s6z75R@7;@f+rO4WE${<8R7}nL0TN(2tJoLimhC+=6km3g{}j('
        b'=+Ad18jkKk_5*gBw7Q<aXa0GTl)rJZiHv80(yeBr7o$i$vU_$W#@G^-NUFD5I}@GJ%XaXmL|d(O{I*vU*^g@RNqW{sd+@Aj=*12l'
        b'EZR#}CQLaRNpRsxb^=o-o?;7ELfC|K$RkrCF&?BwqOOzU>ss74#8|b~s%G$lMcElKZW>8~jK%UKlyy`<o;2NgE~2t6u8shSiUSh$'
        b'g`>Sh+(G1aE5=93#wXtT#cnJ%kWgGM0qTK&#C?W9R`|VQK&DuHMk265IUvwer%^!4&~I%(p0<x8>i#<-&~J3-+kC$tM-24~o@Fo5'
        b'vJcToXWM1n?F=35?(N<s!)@gaYsN5N7H=Ud6GwB0BQ~8u+@B&~@T|2{{k-3**4C<-V4k4g&zk;>ci`_8l#U-d8`^@f%_k7)vX<${'
        b'_C|y$vEM0%$%)hJM%K3VZtHT8y__Hla)k_1p{lnEb_uxc5hh)~mYA>-Ma8ZCs`J^1q{u4Cj^D7hUDz!^6ArvrT<`9W0hjP1zSr_N'
        b'5knwl{{_8zkoS03DegBeAKBU>k|j>@cyV;x<HY-mTZvPT5jFj-vQqe09ar&Hk~%@cZH)-ft9=0vLTw?^iPE{q))WB@36M-n0u&d_'
        b'4F@G>2%g*qSqwq2q-rISbE_hF%?G+MB8cNoAd*`i0izqdeFxMFKA(*Ao_;|l8RsAb1gT6M#Vw8)G@ThM8GKew>5{MPZqB|Kacd(S'
        b'6YzL(`SrMbK@$b!+xe=Wi@@q_{AC941t^I;wdkwP0-kFfQrj<irb+tocMEX~zv4_00)nu+)u0Q|HiN)EmC(XE%t7wH2+$=U5j1%v'
        b'n$G<q!Z-?XSrJ%o5YV0E<p?0+)N0&a^D$7*z*R;|$yZ77RT3^ef)68Hb_BE#)FTVx8H!GQB(UY+_Ag~8D8LsDC?Nbul8fh=h^dMw'
        b'o&Qy5?2z!&`Ef+`>$(2H+z#5c#YgDbV!fI*H8AY$qJ7gMYSk>rP%~BGW{bfoXr1^zSh4mkR`cqp!@}btTN-Z4X9hY`BZ|~exz}(i'
        b'jd1)7(YKp!OF64%+-F#=Uvw5843w#HoG;Un#=8*ypcCmoV|#D)MWQzv=hrtRd!i#cqa&aYbtm$SiRg@qfTGk?a2OGtV<O7JNh%$A'
        b'Zi(oOhyalz4;|4t3YT`IB2Q>UrxcfVXp!f?6`kKIptK_ydCn+0KUEkfpf?)i9u(1uB94xgcrGeBi3n;u^k3`jwmy<F^<ZVf*rRih'
        b'>-qil@#6x<XKTS(M$3F6E{T9h>^ZCG{93`EJ@0u-(b=aMA09GZE&IZ5R3Pp>#odw}X6;@PB}4npDUO^|*uKHF@tN<QlZwud75H1Q'
        b'eP1Y!e4(&?iJ$B{t~m06!uC17#@~;7-cxiQQy2;4IjZP<Pciab_s-udY=2U)e_^zHm@i3s%+7d%4y7Y$$&TtLYMt!%ccr%16z{}~'
        b'c6N+)Oh=$xrWjDVME#C_P;z+0M|CO<<g-J;KF#dhf>#ebdlYZJk<!y^+x{41O_udMZwFPA_MTPCPKSTDLz8mudAqvDHl;eu`lu{9'
        b'3_nw!b;^!D<nMmG8^?u>p6`;Rwr3R9uNeIIG1mLMojul##^SHOx2vU{jS3()r2+o3Y;QOJ4IwnJsR{LF;P0!@*=m`zcSmb?!I}Yg'
        b'^$RH*74N6j-Y%-!uD~d<jq#yADK0NnS8n|dn%=ICQ1`5>^%C4;io|$ON;Z+@b2v7!8<99P)yA_yUzJ&*U}G8WL}rRtbT^qSm?pHj'
        b'6k0<!Sb{0FKc_WBtCl$KfV!EFDKyWfXD)@mEL6$~7r_${0k>QMWpm{CAdy+WR+!@YeYc~`^@@CTerlkRnc4h#_d?q`#gzC7O1Z=~'
        b'A1=aYtx*{E+fAZ=l$wati8z0=t%6&xR;#OnHMNE)+X{tV02VpUYG<kla8t#Ce#RitqC`d=#R`jx5rma|7{4`@vE?dE_w`%VR+G7('
        b'Tc{`&^_!OUFD3Jf<xx=HMC3zZJzvE{<%76e+ye0EN+H2bQPgG=Y^*hb!1;hWanP6BQ0DE5S+^^+3z#heAXPbe&a5;Ao6W2xbK>ao'
        b'xKLVD=r!SV8Ck|FxHyH0>eoC;QZoooo}wj%@QuU4(w3trkB_$*73Hn-yzWiKl_}QhZU|+??oO;7)t>T(Ot)J|$GPWpJ4PWo&Nfa_'
        b'x#>2KOu;b<aG%hkV=|HB4KoS)kB+&U8<2yCqjUs1n&3Cdas2h&Mj)FADn-JRqo3t_NX1^#CRGI7uTcYovc)PY8ztDmk%?3cz7eAU'
        b'C#H2;3(lZ5=UJ!r=t5NbxPbbbAGs`omKegughOSIN&(T_?X<#doQ|^YUcbY-ydkAGO<%qK)ySitfzObG@z~DF1AQGGoyFavNX#~6'
        b'v%L!tiZWu}jE^9V6ajqq2?=(cNLsP9h3!3tBds7RV0qNreh;B2PsHapb4Zb+4m-N&Ypzeur!|SxcVLef<T+l^=`o)fU-NT+kZ1lw'
        b'j#I?*at1}=i*Mz4XiSkQ7GG!nU5>aS#3Vu=+&MX;PSggjKay+1aT%1-&ua5iGf^&~S2GDjDnv(ZkyaMvz~4F{%kShG$0+W!{C=m&'
        b'(62{{dVN3lyj)+N0<!0RBQNpU*jTo@%=UpifuPBpR)y`joDR=vrE`hIGH!=FF*^_LXTB#tVV6~B3xtqpAkP*#qm>{oswz{EDbT+F'
        b'IfTgO#e9n)L=asVLt@=4@>XJpn#jr|a%BQSP@B!<aqdjc^M*W?Al=!l$0wgn5bfER!Tm@WrH?7f0vr6j9Io$!Xm9A}UX!DkB9kaF'
        b'b00r$rNmUyU#!pP_Q)ZBforrNA4b5+5|Ob#`12+C@bwGB*U*JFE8isSFOJA(vL#uWsFkSAX97KI1x1L6f((NJ?vVM2?bpZTLsk?|'
        b')EXF*qF*mB;=FQTHP8ey;@ntXz)9{Ixiga?^Q+Zz5^>ESKM7JEvTT-D+f9@Ek*Qy6&d(AfeVl|*OQ5}lMD2J6WXps{B@lX96edbh'
        b'#4u6PIb5E6=^Pfs+Iv^#Ou1=dKet#8?pzB3m1RL{Bm=^tW`ku+m+RvaO-w#(k=)0N+{tWHByj8Gm0kfwA*5-zn_CNvMOfH`guN>Y'
        b'3Bl*+Ih~w;uftV9$<UOQa<Df19jT^aEO4C_Mj_&tE72HkDIOamNCZ|GXJY+HnJuTu%B^{`V&vA!lr#b+4q)#lYiEYjs##$fE7$ed'
        b'kU(F&v~$h5rF<HnKomO}wR^P5$!gWSmu5SU#v+z2<~>pr_`DRIJT+68g$DrsI-LL#Qp|ETHVWKA$}D;2ED&mxo=wC*O`!i+atNkD'
        b'vH8f{kM1b~!#8F1r{u{^z{UHpPNd|@<(UH0Y<QZVVw8hEqPzNoKeOb+*Aa3k4?hF#n8?K9(kL)m{mcEfbKwE~l@kK6ekMFW<&*GQ'
        b'JJ^#DL<IDJJV0`gaJD<GQ&LRg{?qbNFysCb`wA%J^ZUUy56uT{C?PXGGqW$;_D(ohT2A~Z0U_ji!Ub6<K~DVw*>08R#4n$9t9*^v'
        b'n$3ViwnfY3gm7DU3a65TI)WG~pS*<|BhMVeiv)awqMu=-U^a)MVzMCRj1puK#{031xLcrxBv^x%XO0TgknlAmYx)OkNT7!AKaq`+'
        b'<Gmbd$jb>^j-Xk8!OqbX(LaljyWHa-?6FM#tn=Z>(}Zt+7mhLx!A(X`#L5$a0=>O|dqPy#A^(X#$U46bcRh~|?b#)*eUjNZMu<}y'
        b'q|ZsQ)~~32vYURieuAh<Kt&=n>(g+sD`=02DVlXE+;kTv3Yr8@iWso4e1?qDTl;an?C$8soP<zd6oS|g3i0}QI9!3X=mkZYe+ft7'
        b'QDBQ;l*O`s7AmrMa4`ae8|0aCv?sJ!-48b%YGkVbR|Yc;A<Wp|5j09mC>+Z4Z=~3tUtQf>TSHj0yRm**o3J+(AIkiFI834uiF=t<'
        b'5Kd2HQ6kbeA;lqRUY<$7PhbZm@GMT|C6MRS$p$xp-hS)rm%>lFNywWS4_i749W@XF0fG@iuL1$VUl4A0ad3UqHX}TNfPhrj9?s>3'
        b'gFb`#S0+gD`~^ZqU6Zm=40g;t7;XZKC;K^Xc-=M_Jb(RkI3xxpGCy#^n)10V;Ruq1!1d-4*Nwy1tSAv0#G?TZ7gto7AYx$}D@I&Z'
        b'cwJpM%q=Pt#C83$+6Jr3g0QWof>*%mh9I^L>UE|-ZJEP4!Ve2i7-jkDcygJgKy5Ke<J1<j*)qGtGHXo_Ez~4Q480d;B<T%X^;w*m'
        b'Gub(_D)vpata^poau0hyB;Vb%sBS=p<y#bQ3hm$2gZj7voCGGvlZZTY((OJGCyV+j@iu`0spb@Jf7i~<cEQbfSyW?U0xg0$RUbF!'
        b'M7^wOOH3$|i;=1Vd@){}_~<j)M$&XkKi;}$wja1q(e~#PD`cyGEy#g}W~lo(Q(?!k6WOv8^JOR9XU(r)i2BN4nM*%X^i^?o_esmV'
        b'wWAD{!V@{N{7i^;2KU+gx{aapLyS_CnHO$;-4ANPGKnY?YeZ&RIQ~f#fr1zoq7!!oD$Q_$J)VyE<6a7Ui_7vKJ(hb*e}gjb2#45+'
        b'RgFlLXBOeK?frqw$)KG@*Z^^}MK10?dboRW<HAEo7PU>8BHeCwpN*PxqFvVBvP;s(71ArvDE$s=XLUBtx}6^Dqus@Gx~n8eq_>(n'
        b'eG>G(QCbKCJ23~?SM-ayBGX(ByLvS1BN_M^2K|y2!Q9v}9#JGZ9f9A>Vw~7GTB^$KkoLL#Cq0NB2icA@w0C#2*!oy^Rp`brJOi?B'
        b'#FrA)o*9iD;))3$Y*XGoUMU(sUg-!$(n=SQ*@!<0uWAt2)-Hf7SX$WyWH@C}d#WGB_wH#Fm&L^%c}!*+)ek<kxq2`4W(Nz*0dABw'
        b'q5vOY)W8ATLo)EN2&VZki%&w*`i@W<FJ|{agS%x>$9M1DC6%`CaIz;k)2HocY8GM$@kW@h7`S=#7{mSxa}~-z5A<=fL645*fUu*!'
        b'QWfU^tf>NKYJJ??6Hm!bas^Et?Z0i6>=mM@LmgsyHUdwC7e!8jS{;)e`yfV&Qb!?GJ2;uHKV0bJ%-cIYZmN^#VJ*ro+`iMe(vPH#'
        b'n9~WoqQ;XYzVphi0la}k&D{f$qPwfxZYgSc6xn_&gZ$i-*3Sxld7={Xp`w*2jeA)JJi~!HJdtU%TC1#H_gTa>x!xd9_@NW4WLmB$'
        b's(tn9N6V19DFN)XDIp}VfURz_+N|n@Q<v7Wo(x&>%Pi=aAhReApFi{;(9x1m=z)*-SODWe0Exd&oDfe+%b;PdK?eDRJO@u1A+0*P'
        b'?c!SCt>-BjCBd*$?R#P<lqyB)9s&kl;uC_sXp%`y>q#)ZL{4r{NGnv%O>dwR<+8;VU>Qw1{_a1?%{o0j^z^Of=YHqY^Y0jEjfW}x'
        b'bX2m>1nfy1zl2;H>fjJu+xM9g;~`^`HbO)?dT^j7BH$u@I{b}ziOjptw0N<cf|(~g$Mdb^(4!>-&=C}5`sG=mCki?oJQJR0LHRBy'
        b'|4S&Z!sRt>Uj*ADe78bfxSvW9(h4mnfe;>JL|U0dZX`;47fz2pxg->)ObBR6B?)O+u#AB(V<6N$7fz2q2@wrw?gN^W2WdW?@I?%v'
        b'kP{KTD<H_ovj_)xd38U8qrgwTds5HF2G(tCN0_=48Sm;Lp8+3>7j$h+%J>kxR+J%QLHdS7$P2m2GCYys^0`U)g3;x36J;o-KX|Ph'
        b'zJ5QJ)5;(YXo-9X7kVb2-zUp`#^9*HCISH*CDX<hfkVVX7UEK1S8|-w^05b;y_!R|cBXEeY>=)gxKLeFK^~>vPgw12!Mk{Mt>x!v'
        b'uf*eFz_FGoNNN$<MR=ZNY}*<9+J&G>@fizYvdXsGk9I-wgrgmfy_qPbnSrbhX1*z6nO=^QCy1yic81}XsG&pX4W=p#mzYAz>IN9#'
        b'0y{eqm%qqBEYzpu2QHYb{FDm}n%Ez_?jLb|e#G^6!RwU2F*qa4%nw{J3-VLWF?b#jxIR1L`l}JwjkqtQ#0dq`_M1{L$5=tWUX+hO'
        b'88V5=wmIPLV+cqG3CQNPsfjT0k!O<nu73U2e%pPR9Wcu=<@fW`7nJfaBPU2iMbWW%S?0DB@a-@?qZMo{q{N3H0^pYy5ip@t%*^~1'
        b'lP23G^Zbm_$1u=r0%!X<ZV&TM2Z>IU8|F@U4#nNcz|1IyAOkbS;_&=pCLa;~c*a$n5Ay*d0Wu(B0%GRZM0Cuoml$m}vqX^7a>uM3'
        b'CMWKe!Y9YlqiGRa_{7~JWdw1UJTAb?ytZuIr}0_Pqlrw)L}r_k^u2(%6nyRIM6;fSy0_uKEu=9A?c2&6*~;+sCgXbhXy%A7%+?eJ'
        b'*W02<V+#V?=a-M;640zh1}|(uO~*Jis~#HC;}tSnJYVx-*pZ!KbcijE|J5IMB#F6OGGEHKJ&p;krtvRlUkl^cw5CZN8no}PVMp4-'
        b'mbnSrXujSTVMn%w4b_ufQm=EU-WW9NA?QAP--)mz&0)00Cgv-@A9kd1xN<dr@13wCt}vTFY^WjAORVkb!Itns3BSts$FR;)hMr<;'
        b'80rJRv;A&}s}+Nkv=Oh!Y!C8H7cobQ_%Ygk#s8km9GT15KEW*n*B}@1_wQkj+{4&D7;&H1vwbG!h>5YiJL3L){{Bqn$V|r8H{yOF'
        b'e?ONwlFQh7@qH)JAhRA|Yu{sSCjMC#b0mw|DA~eus)}fo+4A}OcQQxrWNh6d+T!(N-yO`6I~d#U5%;I__opyNrZBb_N8C^2@24_H'
        b'QW@KCc{buz<5VU{1?Gvhm92e+wQb{{0>^9<@YAx82%h7ZeeOZF`WTo9aLg<<^Jax?b@u8N2SVN*9pE}&bJL)pT7_M)gv~Wr@94{j'
        b'TN=hM(@qlwHZ)AmL>o!&mtk5LGc9!Ron|KD%EMs3og!s2)a>oSv#M+*VOIX-4F3*1tnR)r@RoFVWgDq>5AN;Y5W~L<KT;T$kjZXj'
        b'tUEV!{lON!=s@PqHj?6ya;|g>-Tl1CW)3_04`JQ6VUWOBYna`Q@=#>0Ew)y%b*3<DRc0+r1^ybwv=g<xO!ooyU}nt!$KKt?HF4z&'
        b'z@JQB2$KQxg2<cONe~Q(yF;)gaqVrAQUtB{qODZjb}wkL=yvy7>uqh9wwchvfVhj$T@z}z36>hz(jxW+U${+h%c2b};7e^+?^0J<'
        b'tG1<T)uJ%ZIg<omwtMg1=Xw78eLrF{GiPSboH^&rIrA2YjFC`&hCo#X{$C<?`fM_zZNRDa_?T8(RXh>8KvzvKc5t?8+E{VTQODN1'
        b'aIV2qI(Bxr8GPY#%k5LDch5#$P=cVu>tNiWDY!}L(@{iG#@IhtPpF@wpCTT-T$1>L7;oy7>OIk+OLSE%L3n3Q*-?|J-#;bXZP8?M'
        b'fhp)XQ=Lk?B=z{p*B4@w1uay+d<yE2IjUcn%Qt%_s@rt>m?_!OQ_x(fE;CAIO8>Q2MZA`v&fYbpo|mw0HA<Np3F<sP+P1^@(=BgI'
        b';U;2pTc_%U*vVOx$@(2r#Mk=j?bjEil<Qx`Luxf@W)r<pMD`!1IQtSq3$1rCZhUG~zio=xNyhbX=+ZIXm&ICw*0z&ee=N#Ai>TuV'
        b')fy&EPQ)*e3{!;Sdm&v%j_Ac(d1OQxMa-6k^8mhv(i40AexK0wuaPm~hWmZm$+B@Fl4qWsf>PQ@qW{Eer)6^pXU~AaNPqU!l!i=V'
        b'c*xOr?As@&(8)9Jl+dcN;K9AY<acJr))k`oj3g2@R24oM*|#it-_d&sI@!P1zk69%l4|enr0PVeyP$@0`S4X)aa|)>gfo+fH_M06'
        b';!CG=8e`7%e_JwzPW*VDgpMBDyT=_&d?!mzN9Uu)kZak|R@9I_XXz@~O`$$O!vUfAOQOLjb5qTI?8u!2zG!-MIf37)r6JtQBJb2%'
        b'GzD$1b0sly2Z=AAhSQ{MLg@4;adOQLZ6_|%bX=}>nv*25no&P7A%?5M=|*ck_DZXD15QyC&Z$?L^w9=`r26-<UDHs?T@&gS6sF=U'
        b'2%TvXw7|5hLj2Qct~Js^T}Dp$ooP0rGgZ=Tkd%Ed#5WN%UvoQMUMR1bdi_48E}c)?a#;wTxpWWBOZ#Q~GJHSv_4^-&NrFqpRR>xH'
        b'-o(!ZZW<oM-_Hu|WV%$2zP4oH5iPUA^@jT9eK|5AlwB3V_f1jZbZPlYxHVm9ycsF~I9;qikS_CoAA`0ZZDPwc!Rb*P&-59-QW&Wd'
        b'a-*|fhB6(B|7J?Ohm0e743Y-D1_k%O&bSvJu(f<IY^Gd``)sctToYZG`1{8t2EBUj>XP+-T1T&5cSq$jQj3LFR%wZfleBVX<K472'
        b'!-8+(Y}TuH{64XBCSH)UROVhha#7%IuEl7NWZ>hV&*0RnjTAn37}t+SeWeK9rE)zksJ(ZDK}Q7?!FIA`L<oNBGoUC_{W9Z9G2CRm'
        b'9N&yKj)*@<m=`o3WJltOc4_Zbl<wTwn8|zXxOZc{Z^t$$W%0|2W+PGd)|qf2L({T5V)bvtI;FDLd7reU^UQ4O_*k<?$$b(d?&Dz6'
        b'$cTX7dYnp>?K)FT3C$~sR&AtAdSiEbW1ZridQQ76?X@!v9to}V)KsFONIrMr71vpO$`;?5@VItz<h@Y2_L6iWtt_gkbT~Hrk}N)^'
        b'U~4LiH!6x}$eX=Px1`N$C@nCR7Ph>7O3%k$YjaAHP5Rt@1)ZMZEIMg#yPWI9(d-$NbnYK+SG2r;>iF7bJgsw3qHc3=6|v$*)FtUR'
        b'#!eqCdLO4}$!kp7{!_Cl1<G*-FPZ<n5Q^ve*va(L{}*i}x&Oc;S|jCzTZsq5dGz0J`2OGx-<Mzio?Q}KKvrC3w=<zRho9HfZg<U9'
        b'x!rS%3*}vz$5n&NVgt)#y~|@eoAulZ9LAmL(>{6?m5PSU^9%S6w|bP<;Gwl>XiHJ7c&5Ooq~p?JKW~?E|AuF&dl>ENb)j8N%c{`E'
        b'pmi6JX6>f?E3Ou`Fx=hZ$}2Us&zoJU9E<Ck&Q)+cde9mhu*G`kqIIv}eu{%w3TPclPm8$FU1*^{!wYSfm0du4ik9YI371bZ+9><}'
        b'xOUk_X}ONe!om5wE51aBVp`rVTb|=wCF6{EtWWzuQqIWjUv$1H;CnLlc--jkHT<--ZjW2j#G?%>FF^k-FR1tqe=KX4aY?bEiiDeo'
        b'SB}yy?Sc?)HvIj%W5VnHB(m;Qyzc18y6;H)ab(@(53GBoF$Mj<q&!7j`;zkMX!T<;;nk-^R)03MdQ>-97B5>&OX;LVQf5JA(cDUQ'
        b'4r9?2@6R%k%5se-M@`RRA8x!;QLa7yTHtI<rzeXW#S5Wlv`VZw%recnwFWObXfD$%m#mIY4xGe6@Ovyj$DvAcn1`tNgX6r$S&H^v'
        b'p*}v(P#}wc)xhh`+VTQA3T4#X-;=%7gi%&;b<;{bV?UnJ9M`VEuN^g*8<KM@4ctLI(kR)sBx8nIQb^Kd#@+MIXWXa%Af|kAMx{lu'
        b'?e^t!P$hK_8o5;88^bRylxMuKTxncvCiU;dWTc`Qa(a&lfxR*FHqlAkdw6lrQ1L6KdtZ;KxXN|lVXigCXe_p?yqz&m8Cz$1+hQ`J'
        b'd{jp6$X`af$%Q*wNQrM+iV7vFA@h8Pfx%zao}V4XZHw`lliOO&s0qt?@PdM?+oQMujlQkyQPavb*)_Iu8=dr8v4p1Zb$iy;=y^(A'
        b'd|6g^AF4493PwF0{|u>0XIA4UUdWRFkh8`{X0^Kb^NYp1bPgk9O|4{@4R!0+nHyPlL-Bpz3~q`EY>M$ZP-4HsIq^EnHHs5Lpc0Kp'
        b'X+}Mv>KL)r5}!F`Q%^fxakZyZ!99t`@!5T)<;vot%0i`gV+?Ow^Kgc&Ca(4VU&{Dw-!ilr%i3w~S2$$+7Yc6~PMkI3e57q<3@)h8'
        b'`^?P;CC%khoB<yeYpLEiyov**+|R|3`F*91?dsqPM-F4jzmr0T3T}nCz{d%+e_Qqo<$B&$ke$pg%qv7mvq;hVuCP&)|5pL!)D1Y*'
        b'dd~<O^^2l@8I`{W6;A602IUg7B)$^oT<#Y*L|qvw(rd(Tb5K$KFCqTjkK3ct-Vu5qL~}etqAb~a9(^--<-McgCz)Ryst>!-L~`50'
        b'KB?+;f15hE=a??NTbH8z*sO?uNP!DvdVd+6x%$KfUS(crRPqT%?Wjvre4o6w#)E%H0q=HWLY9;b<$&^p(1?_qMl=``^)qAGHVxxe'
        b'ds^}M=JLb?zxd?WG@1Xo&>nL_S@nfLC!z23k1pLSp<`>s^4ov{UWp!d$SR&4FlvUsQ8QoTdB2QC|DBGm=w!ZDqg~+m4IWv8NAijK'
        b'7;!Z`?ggL`t%+45q3y)a0g&-!3ZvZqzOtO;WOx@;Tt#X89Zol+*83OLXoJSHUCqa5y3O~9^~Y+R87;)j>j!8iNA1bMi?rZc#mHx8'
        b'(xENP;JI&U@$l0w+h^zghQH%hm%-!6#6itUz5j-}m3VGt_P)s6%BpV!f;)=mQk)Ohy{K3uyiBpKN~^EZ<7Tc|n3~3Or|C`YvXNbq'
        b'eoB0T`<x2RF?g5`-}Q=GXG3&#Qw%E1gJPb!AT)c)aN8}dQxa}RcnMRf0@Zvb4`Gp{wM*`#>f)?(SJ`@LdK!vNfvj-xB2=5u%9oYQ'
        b'*2;28bz)TRYciv(y5Zk!-84>N*|{FuJ1DgE9{<avb!%n4bwlu??Oocs)W3)<nqO%x+7RDDxE5Et$*47?{&o71RD9Rb;G1;dP1@T*'
        b'cY2m_Zm}*PB?hge!AoSWMn(FOR#Ly6rWG!U+eSxkj%KPWw<i3Wx8?et=#n{A5<{}Y(W0+4sLmUDel+@%U2EHzH2n_40}g*)$$`eN'
        b'qEAHk;s-dAjZA%B21k?iGb@?;4ap~hYesp$V{2vIQ^~*iB0l*mB^|?a)o&i9V@{WLs)%vPupI5V<kgDLP{Zw0<IL?}I1c&IL2!2T'
        b'!n~?(A=FNweKWf>gHAf&q&vNG@3VBMtPMCd`e*4{gNx*~_^v6ZEw_sv{52ieh=M8dzY_>lWjE#E9WE97i{ewys5v6DdaPS2&Zoam'
        b'(OP1v6%|KAkHF-qT~Yc+X<Eu;sB@c@DnkYDFfhr6efD41)Yt5CRO)N1`pI?~t*X(xHQXv31zz8Yf5MSzE<lZXmxeL=iwt*Xy4_LC'
        b'Qa`F%H-A1=it{2LmFfPq(P7-xAI+rd+fkOuOvelPM8Yk>i|HiAh1iK>5|r1|?#|?E@Df}a#W#XjN3=^@z7Z;}q`!}<YaC<VtKx|`'
        b'{OR$jIlCAY1x>d3S`~cM3N*Kv@3#C4O)I;jn>~l0sMYjE&)lXQKvl*jW5V>&WPX!de>>fKO+d%o`c=fhDx&19l*^$P=g^<!(2ghA'
        b'Gb5adUL*O!Y}=`&`z7u2(2H2p#s!z{*y7WrKFN-0$GJ?D6>Dp0mE+yU4#$Qa@iXER$iZ|vkd89i)82HNo51CyUBO9c2d!%!AzCG<'
        b'1}vXSQzcI~R&R|N{1F{UMqz)gxQGhhde6io@2Uoq=s-LgSAn)ZdG(s91E1^E4DSDzql0tQMj86HekHMP72!B5HOglu(1TOxz!WsY'
        b'A9_y;gmJ3MkTLbRNk5{>kgto(TK~Cj4QeVc@dz{D{&G-G2c#(ctG!3Xb{tK5CG<{`?kBmgade~B#-cJ#j<`?JKgFHpS574x<|R}&'
        b'9HaN7m7JkfBY!wW&n^3R^eqj2qegy?zO}r3icU(y-$u5bqBC0_Lf^{Jw*?~);;Ap4qF0pRZ)xb;+LoW;sZFQor_=B^yrSB&6?iK8'
        b')-<vl&*3^nx2554BU?{J`tr;MRB?EZs&;;?>X&l+LvdBKOY3^dUOJVWgW}jYjKikAa;oZTsNSXTrB%&6O3qK=deK!w(nhCUnPRNb'
        b'hMy05U&Xzzy5aetfQsw6VR!_e8NlZOCIqnzW$#l3?KFk!Gn6SWe8DVOg(^T9*M;Z7oeYoI$vC&sT2pz>$n8`uIM}6hCGf`G5>>F9'
        b'YDZl$XDL~xJzd;()oSo7&Y^lzQgv3`5BfHhfh2-<t`skf+kyYrFHvo4(!WWiC&lSosr1ZP{VS^Uxk~+O)anJK{^iMg64R~;TcTC^'
        b'ttyY(zoS#W#jQenZl_!2X||!J<qne$b)N#iQ_WWHFr}bql8%hZ>7&C=O-Bz~TZ1yl0p%t`6{<4ug{D2b(THOze<%CybO|ac27F||'
        b'X{n+!xffL8!RGi1?pYO`*ib-}T@<)V%F*U`dSxDCV>sPVi<%puc0R50`1~VNPNR-seW>s9q$=F05BJeGsIvbPx8i)He!a@`>f2(E'
        b'omR32wY5RRy!EyxgXw5s=%o7EN=N;MJ5|90+**~x$#(FJqp7m4P=7y_eP8G}V=GgITjC5}2`V0r&9ZEinCKu~>7Y^FB_8p(Bs_Ka'
        b'taSJ*Szv`~<{ze?kaoUG+&h-G?(=PDK3j%*OsbvBR6U-@xMeuxSLEOl6$<bm)q6>Z<O@2%c{jl=R?*SCl2-=J;z=E!a%K|Utds?l'
        b'n(rofBkCr-tjr$|?c4dNL~--Q+JNNp!=LwvyZA1Zk>t@~FNi880yW6doY!!@m;EoQP|xlh&b<0N@DlC_&uI>S&cUCypQwy7BN=Q)'
        b'2j;&~;mqqKWx>-vlKTk`fj(#BPlJIhwojB<B=#AEU8an`UxH>iDwd74T$-5edhn3-tkk+l*6ewh(~B89$=ck=-G;xSMiSm0+ccHf'
        b'dU+p*UOYvG8p7rB;&?hmg_;1#IAE(h_$dnT9u6S(NeCjKR;^r%n&}eL0_6v1PAIw+^A@x$`}~*GHtI7<HAty;QYhJva${nI+RCPn'
        b'=)b4v=>dhRI|gm5BD~Gt;mKw>uj}a3ID-D+pr$t1PSVr;K@F|qCPGu`JD2I`<c{|>MPi5*!H%E?&3lQuVHxQ2l=vy*ekZPytU4lO'
        b'#Ose!rhFxu_?K{?v!O+n>pFThCF0`N260`B>w_ayXdhMLFt#AIOcs0}r70KMZ2W5b;7abVl$hzeCGBL|aRK$gKE?04*%%5#DlQ51'
        b'2PoP4@o@1Ov0eRGIN8uKz$HVOZGnuB&Y+fO9>3DOhG_N>+y^+o4()U_U!VB3fu)lbGGcSI%UE0^v>JPHY3@Yz<vyy#_C<V><g>lh'
        b';9hEHC)MN4;Jo7UB}APz?Wlm_vNW{)`G<tiGZy++(01WI>LNUW`#ps+c^68Gg_GOGwc@YclC+P6;6a?1LsR5cR|GM>PPFiZvH^UK'
        b'=wCt$7aN$kZWt42ZRFnIm#M`sQw!{yNm@JqZG7_H)<l)QL@g+wr_O&zLd%N`Ow`FK`mL1hcT}cv=36r3<MBf=%PL>Hoy@<TC|IR$'
        b'q{<&3$kSxbsLR*?mSSc&P8x~2qv`QaJ@x{Xp04C#@yZ`_P(xB>gH+b8%&MbR1>4=4p;F>YJvTQx^gOG6XhDoi^Ci`=Ahto8{#4TP'
        b'%)%9$seQXkmNLaHSB+A`0@|39QDBhHs52Qn(u{J0G_7vEv7EjeHKa4jQ*<<$`=XTASzKtt9$QUS{S9qv=`X2eWY>K~#Y5;{@-K$p'
        b'(X8F;->X^qdg3FqV!f*=&mTKG-pls9rtfI-7rBQT3TUHN@ws@usOqawTDi2`V$@8lcE@r{C`XQiTS4V^;bdYMS)>jPozq4wlN-)y'
        b'Z&{458}QM^8->WZPrNJhG(|-ltam$D-ao%F*|vZ(c_g@-^e~|>pn_BN^YL63d@{->o$JCqnCOK$RTo2XX&DnZE45`F73oN1L|d&J'
        b'=mh;ds(1#W|0y0{6Mp6upIW|vAF55eEbP34>c{V_xk%8;nJzikiqm}9rD<w(MF%a(ykblUpKC1}CAe7>zWlKr#c)R>sx`Vo@z{;x'
        b'p$H$-xl{^OH)8LO;Ph03CklNxq3`iH25u!cm7){HZ)M*^&g*jtsISk~G)CfQ%9GKN^NT(^O*=D_@LAf)^UaZGchl{OmzGfJT3Nb5'
        b'B92RU#;oqVNZa$T2?TBGMOk@CRruUqLywbArm6ZrR(d=e&VAbO=5tLAXy9e)TvBt-Iy8<xw^_AgpW4||f|>{&vzT{`WPJv+nRMWN'
        b'Nhjb#1zt{MA4cL38NT&%Gnw@iO;%g-vI@7FNyQ8zrDkh_soJ7n-G%RQPKmCzDCqCECfqiCG$nCs!W}6YTU{4uCvF<0v~EpE-)jE3'
        b'v+uJ@1%IWrRhNVY&kI`<E~2^Tq50HVUvBL><m~(SQbB;Wqe_Tq@I1fO^)`JTwOG)1erv+p)t1->Pu13h#0F3G)`VldBWMx7*_t44'
        b'@cdRWBG9I)&ji|#KOAm{eS#mUMjcB+E8ZIAxOn~g9&N0<kgiLjbtXIEv`c6yz9|ZQ$0H<8J4yv78c?E1COg@CRXqNr*h6WvIda@o'
        b'x$1d!vO#g}<}^e{Rw?>ZIt>2Meob)Zi3uB?h8kQ>)KtJzC&T~HIHQ(Nh%AHGCG$19(E5$*`Nt>6lb4KgUWz74C$D>;`E&+S=2XhA'
        b'FAs;KdFcQy0U3$cgX3uxE{8#_GT@dZQ&V|8jhacKK`J5IQVDlzeXXBPL4A&W_&)iqO>zV3%HB=fke=bTZ6yD=I`LHugGUlyNDN1#'
        b'9DYOHfzxkh!jD~ix<!7eFllvSx~qUD8xD-UQ<&&e8hvfs#j60lB$2-S)H}<S>1*WaPyGeWZ7fJ%a@#vg==6qYdRMNNrpey#1)~e4'
        b'UGHW5sU^?>$mlYXsAq$(8}%HzWJdK?RyYluJ(n&S(Xc#{CU#ou>=WKG-%_{zZ)L$~x_NxX`S7;ik_Ju#ami?KO7X+}IFFLDYPZg%'
        b'b#5n6wpo2eX*BqBXiHmDjj413>I0h_LqAJ{=QX@a+*Bt-mi>2e)c){vXT#4OF6N0Et%|R0Zl?Njn-mUq177}}qgCNDf9v*5t}Fa`'
        b'>vl~J<DX>>=jU6)-nuLoNhhR7N4vDB`R{hrI~&8-fLvsklvci*nA)d3rlYk3ulw&*dQ6S&(g8R6R&Q$b@Ab1y>JDdP{p5QP7-woS'
        b'PbbmQs1cr-!7wi_G=$=ytZlB{<)XS&3;7N=>!w!wzKX=dhuZbkO;cRj%~Y_4H_%!~LuI{VLnz~-=|Q}0xmwhcMeSc&+Z(x7=QJd_'
        b'c&A~iqsBki>@>vJ=bWtGmBhYaL&p%OA(7TL@%YCr4PLX7$zjleAe<gNiOLpvy=?K#4L!!XWj<wfqr5d5kAGRYnL<_g59~`~U1*>G'
        b'qq=u8|AqI5!4M~gw}gjTgCt!?y?%FkswO=r35}zr?8zdQA;jZG4!g35K;O}UgHBa^FVGjlBQA-*8A2LSS=flGg>Y?I6S~Ie)4Isv'
        b'TFqSE*%yb;WYmb~@@RAQ`Dt{*@k})2%$VbF#HA-hr5k0dQ5(3RMm(@oh58`49-FKOZ^>^DqLjKd-|$kGuI`vSq3+9?Xx^aWYtSwx'
        b'++_Y$p+*}y7W3LVr6qyaqR1+1bUbO%29*}lY)H<r7$%ov@)>!GH%@l^ZYsZqp14RIU^1Go&tojOHLZD_D;34Zh~ks@599Msgh4SS'
        b'YqT|!@rw+js^J4e%CRSSshh;v`JYV#hS}ik!N1-_C!!;I1Ad0d(DPSRf!9{n8yQdd8RAmH>3ODNEZ1DX*3V(**hbx&;T#QZp4&+z'
        b'S_z-G;);i7eZRm1d0r2%wiYnWhPc9C6iT`b1ytt;Ou_y1qJ9ax*D)+3>N07m#T33@eg3XTS9+eEf5&Q7p7kvootryjrS(Od)iY<<'
        b'tr>08G&K-OR-)S5x2EEfql)$OYCPP6*1^=QnXi+VJnSfW*!D;=gMaMG$(N(G)<|3wZ*VPl_Az*!9bFD|+z39c%IjA2ej!wh;T6+V'
        b'r0zo7)i1+a7LR7_G8n0j9F1we)o9O(>Dc86Uqu$*tMbfdl*w`}DeMdzzM-7wl`K1FG)F^7tqyhz%f?w`k+Q3;OE8s7emGnGll$c#'
        b'm)X$aHB$fGT2DHA%IWB!bNVR0bYLfv4b=@7d&A3g_H6iv)9M<Wp5a<2$^g|3lItNR>#+vUa8m<1;8N9YHEp2_P;=C|^7cEG;(GB#'
        b'i2?#OhOdZa)$TdAz>d01(ZsSD<#APV!Z}s(jxomhyQp+!RJ(jwN_Y&+lK0D1tB>9>Q6MYcFdm9Kn(rAB&sjwg;;g;+Mp|)ZwKy}?'
        b'Enl~Txp964o_|Jo{-DVyi|>?gCTA-fNEDrRX|I$>ZhO~F6~8@EgMSk)e+tn_5ydY}1lPD_v!n6Ll#*SYO5#LxyR?TQ{`^v0-AgJr'
        b'Ej1Mq_>Q|1s!wG2-v8vb&C$ij$MY|S+WPeL(3OLcE5c-*fR4@&ez`S4k=#g2t0cs%MyFIl>u6Q8mw2L9v8Ts$FOj^LPGZ~qs@?Gk'
        b'a@3&CI`rTP1xakC^9dsB*vqQg&gO+gPc)IdJ2!>;IOWI1^CrX}xbBIToD6P{e`CBl>*M6pv)qn-{x4pa(8*71QY7=WJ<azLz26Gm'
        b'(X&-zc}h{%=y{Ts^W}ZAc5=C7xn_Cx2}w7;8^x%h%kj&A<g3f&MoGr?K7=*hk1|zxI8*&l+eMFW>#o<2vFsRQTH9e8W2Ixm)-kJe'
        b'ZAbQ4$$euCvz8^s*pe}J-54WZYhAgPy?cz=u$ExgGWlyuW{xq^wd*#l_3OtvG-HH%ZAtFfC^<HaUnTH#<edzto#-X&R=S+{-67GD'
        b'a_7Y3@JThJHbW}r`BI{vv`7jy_?pzCD*nNF7f_czH-XI0B#iVi$rY`c9DPN@>&99=ZJNRd@tJk{M*}At@d1Z=^n(9u4Qo&jhpr$|'
        b'-LiAD(U+5%TGN|;gU7>ut;U0EwV7==d?pHt!)1=SjrWR|wThR>#EWtXw2pP-Wi*7Z(j`><jdiO-BZ7CLJggv09?x8S8OvqtVDImI'
        b')8DaM&F;nX>^6!e3?2V;kxN<PAX-FdeaiU$tK!8#ZAZO0XQ#SeoU^lBn}1pm`<rO{_hs@c=3Pab|87Etk?Pa(<mfgHpK#D^T!13G'
        b'dqop}932=uP2ouFzG2;X(VgKX(qz8ajtI4<qZjfGeb-#k#TGFWG$cxz458_4!}<E(X5-5>zm>Cwp-f}seBv#~<4Y!r=IQ0(J^-z}'
        b'<h+!k#BB$BFI1jpZr*0;d{?;M@F`iBzo`Lr)p1uE%|FLMln8=wH6`>(+~pU9Ec~4igc<l#B4GH@c@j;YAP5P;qVY!b$KdJD5oj?='
        b'V&gpr?plZbns><OeS!Xtqd)abLgYZ>OVD2t`dgk!5PvoiL;?D~&2-?d7tx;!{newtEE`?oD<MmiR=T7d{helslG6-PvH`7!!0Y-e'
        b'iUC8Qn2FV-TDXjcl?1_yalb4)AKHfJ&>spZd=p2|CH3OCZ-f^^)9yllABi8|h}(5R5Z=R|*YJlLg-4r7SW(z}(O=1vxz=TRv(@3t'
        b'wf61IwN`ZITDPIU8Gp>RD&NSpo_iwK%C@6FmDyT=hBrKY;4VT<5OIIYwZ8gkuC@Hv2kv^6GFyXx&9xF}+{0-2b+nymTZocf@_B3D'
        b'lFu7JpDy&b6aCHGm1~`MAlG_&5Y3CyXBql?e`e^tG^mv;EucQw*%K$RWLxwWjj5CvnK`kD^0o?_b}plOrb^OgPW+PcUJw?d!IC@%'
        b'jTuRsc!=^g3+kPWGm|Jn;}Rq-GbTKFOm19MXfYOvIs4vd7IhA#a@KLb!%<S8w{~pUDwA8S_ggzk3N$8<!|K_Pi$^?c^^~|I_5KaH'
        b'(enEGhwJ?%cF&;&3k^NzhUaOl2Is*X8;^SSy-hCETv?DaT%(z5LQB+tBn&Umpp4v>m&xN_KIiRkDi-9>=j|SKZkICI(8R0qisyvy'
        b'zar=#pNOTW(8uZIX3sCVR|I@Q@Lz5m)r3dc77L4)2>7bCtaOP`l!FVhMP~a~fnom>eO)GV<VZ@Es*6I`vSs3^(gHMf0~+he(L^TL'
        b'@`T0rgqG9XOrYg(cENLfCbM$!U4s1$JmH4R;x1H`Sl#MSmE;bM`SuRsvpa-Qw|e--v4c56AV(NLRaJN_#|q+vBDdOeW5630w<QAy'
        b'>54AetM-H{Fnq^=FWTCsX4}Mj1)|02qkGlE*Qa+y5A0R@ZwRmKmX5ZmheLCOR+94E4Kbl(=|%K|I6?EpG+xv#O?i%v?T^8uY+@Qm'
        b'35%7Xv_adySRqU%noRiOJXv)gN>f^jGFoRq-7d4(MkdB{o5-rUgvCZDaoKngq5tos=*)DT%Cvu?*&|uvA=sA2PS3;KEJ3{Ad*|f|'
        b'?{^cljx!44%{?7IW4LtuwQWZ$_vBm&Ep3<VS;`s2<%$2(Q@)yVVoLuMoF7WLcyUxLecOrH{@Cs*Xw-@vP9u(#(|6F*zLKAi_ba-i'
        b'a9AB4Jx-la^ees!jr!ip#p02zTexWadBxke<%E2*eDvc+e|2N^W-9lm-S0Nac&>Wx+wBrgCN7ua#wPH65IVwaOV^QA`vtFmg0Ab9'
        b'w0u3jjT-!~iNJdk-uEUtJ>POyaKQ5t;wy@NhJLhLievF59!LLbT#B;wgP~C)c$D|;30k_0>I@{HM75M!7LR;6UM_ox>WN259M>)z'
        b'IX&)aVRDnCcv`{YOEc8wQk1Ugarmv~m&Dr_ye$*Bra*fHR~0skq-A6r)e_!`Zi!e+w456EyecjNP2+8j`VEhi%N?lX*OzojI@k?Q'
        b'{zBf-@o)z#7Hu~w!nVeV;q4k!jOVtYBD{bfZqqFO?L-?-UrdocQK_iDU7DQN#Cz)|QuZ&Sx+Q28sA?+v@9{bcEno6_L3Y)|Pkq+5'
        b'RjtxleD?DbR(@5Dbfi<TIVW0WK51H~kj+iBO0yjk^rG`pqCW=hNU@ZAaDrrSoS<XTXp~bQ4UK*YkFH+-GuwuViqm4&bcD-(_G1$?'
        b'F0zGE+kZ^lG{yGlEyHVW8D1S8uEfJNvaRRI{1*t@%8A96iAe4j12XgE%tASv$7DY^5%n;s*o2R%1=7XKCyMgap;c#1EM69xiMwwi'
        b'GM`wH{CPcD<s@uNCaj^cN^z{cUATGp&F9dtZQ;b^DB0q|39j(wWi8H+42R}geD_VmvWk|Qg6}v_Dt<-Sa?q+7oAky-&z`9Ge6sSK'
        b'GeJ}0=#ualZUIj1EkBvC{Y2cRXzs_6*hh;Cw#~Y6YYLRv#tAl*65{fsZE2Bsg~H#ssnNFEZdq8$#Ld$aZ<!u{%XHo3^ew`;{ms9M'
        b'V{e=#`q7Iw4cab^M~1Uy6Cb19Jc|%-da2l84K)R&p_`trjYpb>q2Y^@!`WYr+ddl?XR?MGlhW)j#%<?s9;N?goR*5$NAzEfS6m2R'
        b'DG6nkkH*oFxc6~^unnTvFgNV_X5!{ybmYxp@+$;e5J$VW9<_SJwb0L_^;8`S_Z7V-$LZ*Ps?#HXV$)QfnwbzEbfNBi)3yxp!I)(C'
        b'!Zv(Y-8BKVT=T>IPw&z3w9iIvcsJ;waa_3$jfbxY<8h&j;#)o(f6XZ8KEzYR%S7=Tg|thjT2vF<K|HSN3T~@*oRxNT%bXsG!9#Qy'
        b'E16D4zkeKc*(yf1^x%|nMiUOlhIq3O3Wz(^9W|Bhq@#;zd0_<6?-@6cL|u<}_juX4@wx?ECtf(MqF0P0Pi&(;dux2~t??euuXnyR'
        b'&b=eX^=<rr-B?-XL|xlwZ;lVXjwU<vFAMl4$~W+|_#{b-aUy;X@mcHmU<;aB)BBAua@vn7?;Y2-lOz64(Ph*I%OZ%59Q6*|JD*MU'
        b'ejiS2Yu)Ysr5Ybuw2VpNS>8|MTXwrB{N9{8Z^icxH`^ihO5D_}#=)GU186ri;SiRArRqWJ5!3!SbdW9z9i%P(JbYRQ7nZ`gbMcK8'
        b'ILDYNmKX05oZL4qGPJ5>G`24quWFOGV$9LT`rFij+C!oCK%Qp)zSzNOM*|5*y$MG<Jr!vt$p_o<<*`=(pVWij9l?1o39la&&pal)'
        b'-lVw}920T9(c$$*-+ZmG?5uz{I!}YP+w-aeZ8)7UA03mGMsm;670U)1HQe_{ni?ES)ixzw32#9wvGQsZ5Z^;>!S@22a2yM1EiM{4'
        b'Vn4HPPI}z*>7zXPK@JXp?_K0|`r<>V!;Isg%fBMrGL1pg7)9is@0%xXIWeTplhpHSYiJX6;d9kA?khHDB;r%PW^btdW?GXN?nj|?'
        b'JuSAYShJr_z+rfNqU)wKNa-8R(YQ!!fuGIu(>i=3S&p};2wzbwh^~7fTwGD`iYu&{MTHa>Fw|bB>pDI7c7U~q@Oy}gHgMa9(sfGC'
        b'Ka`$IayyUIXe}hK-O@3nfAdIDk*xTFM!ZCsCH554ZGSvcFV;4O^7PP{fu$Pj&0}oakK8)umA@Oa?bb2&H*p!xz-u#xmlz(fzaiWh'
        b'@aFk+Vud4)(1|0|VtrY(gb{C4SBDq=DiH}4iNF&>w~WD6+$~`qKXU7s{KGenF_mY9`mToZ#86K<yL>Wzw4pJ>OEv7xW3o$*(1o{-'
        b'd+-R6_jdswICA5dW@AdlF1Afw)E2t;H$@C}TYWe}w}~eoQdqaTXnAPkQ^Jdxe<X4nab&@F-!cX#T?W2{Zj><0#qg0LG#pA=nhb4a'
        b'{(d2JzT8L_H%Av0%}Ce%B)*bJPhF6nvv%YxP79MUU9Uf4T`FO6)J6A&Vv=sP+0Ykz`OHvy;V_9u*4-RN3}EcNB!mNKk9d9{Kt|Qq'
        b'p<@jWLLC|SfgqW^BSO0F-(IgwPyN;EoH{YARxd-@Ij;Vu;94>GG{vVvILwv9C=B}pVd4~nkuak;OwkX7nX2fEggK4Ftowm5@rw6^'
        b'aQbce_;7Hgc$O$Dbe6R|Q86B=L(p{Z?L)^;iu-hyCwzWsmN=Lm8N@&DuD#**aBXCQw)cu~eL3BO!Sj(B)sYz^GpNHej7{#>bEeQr'
        b'^;3tKo7StNoski`Th@FVZI4X4E&qmfA2)=TMP6Ul^;tvrhq+KVmX#fE7O(uI>;E)p&B6Dcv*u8pn2swvahg{D`@_sl)3o99%=qTv'
        b';F?HcMlx$?`8XcIhEVwxAG{5f0eluJeDD4VX@EOiJc9^04tu%7CqKBtISyaHcQUBUe&(>D=UPQ?-4b3~(xncnP@Q^h(-KFJJt6b^'
        b'W#V~kqn1fmXQrWW;{AvCUb)8(i*>#IPgg2FV2k29^3>aI_x|#5r$@$><K@%R@Woj)*zl)|Te~!YM-F=*Ih?YPE5Xwhmj$9{|21cp'
        b'q~XnRhXWnCn0lAm?vYsCOb4%ar`SEuIU4lc^6IyyS+7`ATCHwB5p8wUZ^@FUyj0|7t$Y0)KhrcVMODy>CHAyw!NY@#4+j>b7<}Vh'
        b'e0XFxQJ9r6@4%dj5BJ`?>G*J-dj53P;Jt?fg($#xs2KK?O)Id|Q;B3Nal|{2hcB!Y+V?c$OFO^wE?Ys*sQ(?a@Im*A+7}Ke3lkK<'
        b'aC$QJahu7yPrP#v(+jyD9}eHhpJB)_x$Vt8aXmxPZYoRl#3q@ceA+^OVO#aKuTj$|+}4|MxYls}nb)+dLLlSt&f5+%cE-QovFEMX'
        b')X160y)f~O>CQK=nf6QZ`wYJs$n7F~e@}FJXs747j$M!Enn?viIIdb#+8lEykD)4l5AR1w<@US%DXF<`Qc+9z+x!HDUp$;8WqEdC'
        b'D{h!HS6uKV;pR*wzJ^tNMVjo!o1Noz+3R!E@fUu?)|aprHG9FD@;&SJFAOy$c-`@3gA<1W!l6!2ulLHKmhD7`Q%^@L&Ik^+1ohw?'
        b'Xw?@SmHv)aO>LXF9#iJDcwN#lUBySE<LY<cQw@H5DDdr}PVam9-w3C3`ci{$41Rqm@HJZCq24n>@b$s34h7Dlp~LxK2w%=S@Z+Af'
        b'(`IhV9R5;s<|Lg`@bhqEZ_H84qIOQr&x5CNw6}Td+gO*~)2eQ@M}4IlJaH&+0<Ghz{G)>N1NEl;)$fs2cM%mIIzPB}kni|!|JciW'
        b'k8Sb|pHP3Cq#8VQC~z1BPE~v$Ec{E;iOVRD3?2%6ghr+3_X@`n1_t8lPcWY((7W*r7S-UvLxDe|sm9*_5?s3a`nZnW%x;}4fu2?W'
        b'2X&jf;lMRtVoh{M8`GNTOP~|$n;3Tj3ik(f(>65C5=~pgQNwNO2G4UlECxb_-{?$7ckI@*?ZwyjI)`RWJNMAw9}WdxK?(7VqD815'
        b'v!?v9ey?8)x+P21(Z;5{RR5Ac|Ge;tF~eMQr}G!ny6h+qptLyV9oWmDF34_slL22q^m+Lu_*wTQyso0hVNhpg@uc{WTn%Z|Rh-7}'
        b'o74H{F}S4C(yB=P9DitrbN`hFqom#=i$6mQ{^n5NH-|d6KkNPVp|a<Rp*OD$xYeKL%(WEg=rq)$D%ABQ)JSO^JCCs>JWxq0<`BFx'
        b'=o@q%3RI$`dMN)};dDaO*D-^RLxE?}h@UI)eRBi<tu}d{8)(pvQy=e|#*U*B&Wa^`0F`iA$}3hk%L@Jiv)LH@(_q=5KpD;@RsW6V'
        b'3~nD>btq7Z^GVgGLdScWroDwZDD5mW_H^23O`GpxO~05nvoUk{-%-Ut$KiB&%Uf~5wX|awTfbMmdui}2ahsL6=pD^ruh`kU)E0ZN'
        b'dvL{}zzP((1-<VJM8$q~oBE7<q1&B+8XQfon#8_@ia%{SW_?io>Fo=0Py~t&1s0>wYxDP@Y!LM&sYoM&Zx1dy6j+GH{;Kyafv|pw'
        b'DzoQ?@%DXzYOsmP8f;js!Ct{NnBZTQQ;-@z@@@QE=f&+<J_lDrX?r@C%$oK<BWp+7@#6nwI~Hy`<F42riuKEL-8IqXgo*=b0Ht(&'
        b'r+(|MMD}}>nOHG1)z@!n_9S+Cn2y~n+ve|R((G~L-fM#?V_I<6;KWd1VhH8HUQQq^IG^QI{OPB6qK0-ZDkEb<fy-#(cU4ad&Nb7_'
        b'b~+K~wn8szmZO4iv9}p;z3TRMEvbKraW4tiX%CTgyMiy``<z-n5pcCxe2B2V#T2zLBOQYH6z<UeE2pPd^wO%5XVq)BzZ<79{7G73'
        b'P?x^>(abyKsP^mVe0+FRR`=JzFNXpbhB~+Z(R*|#?PtWhxn%EMMB5{-_=-M9hI(N&!#mzJlTlx$cBA80+8@!v<HxRaOV|Br71#X{'
        b'z9UxJE-xDt#Oy=_dk0Sp1x^g%-FX)0uXhLkG8Fg(4gU(&Lj>B3j8i`o?Zfld6rYv%i!UGFk`<Nm$~qqJ!-6|p=_rrx8w%`0X>uqZ'
        b'|1w{&b#Tv6plb-%Wk-cVi+e`LziDdo@HzN<*3X#s$X2%D;b{-JGl%~}v$hQFTU4{X=&iWS7uRoP9d5O|IQV5~-xl06`Xsw<gZim^'
        b'7XBuaujr|njv5GUyfLBTFn(caf^mAqsZW&n>vVp)!!N6QeXxBf@CJ%}m7+^P6)&$ge4w7$MOHmXw7s-9V~pSQ<)}g3!TV?aNHzH4'
        b'P~b%rG&R3nFeWlgoWse~B+{K|rfQRF@V7&Ox*=TGwFt)P^b9n;qm$V^-Iquwc-~Z>X=^@s&6wn-P=h)nsUWf9Q_rjF(LA-IjX5);'
        b'H4(KH;+LG^wNa<ZDgzP!>Y33ixIm0L^(W}dZzWiT$;2E*iK!U!B$lAmJmD`l6&T_bXX6i_?daCj?p-66i1a;gubegQk%nwkA|7~g'
        b'*6<>fjI?&+{h^obi?>XyLzUY7!7KQ!ZbM$<Jp-%Rl9lR}WwM2}V>sCoQL@#d6m%<%i4}bee#ho>j%Iyz=QIW#w%VA;VKQY~7Ul7='
        b'Owiv^r)lHy<C`xSjMIY6gL8)hb8&&lUnyi{EVsB#4dv5}_n>+=#Yz--Q6dZnH5vCDT#8Eq@AWNp)G{?oXG^Q@2|bsgtky;wdaf9?'
        b';@T(gr=okp_lSk>mGs%mo)I?f-!V^NG-bB!m>27vhgSM1cL`_Pmek2}MD5a+$={_ZK1mGb3<YwAymN-|35ZN$q)hNEVA95fwpW`E'
        b'#_iZ858Ys8+JBDS#h_-&$df|zN?H8V6SS<5Oj{**w)<PP7E^2J@siMeV0CjVu9iJJ9=ZRPtV?RyG9J1wAkpa|Sn(N};?q*5rm~pF'
        b'KZMb8P4L;frD+?4JE?7LEu#Xj_4xeFD<x^?LtlAAtG0TNq}335y9b+!pEseUll_7Qj|9I!Ahh5FDO$t1uFm~e+R3u7g?6&#lF%+K'
        b'JBt?8=4;iCoI_u_rTDAQ-tr=z{#~T)gwx~vVBq|qcXY7Rb1E&7I4(u?3~q8=L~#qZOVN^XJWdPv|51V6&a{jO4^em%`ekWv<BfRQ'
        b'r(Mz3s%@8!{0*(Gz<{=)RXZPV0b1SHLhrdyTR0_1tMKyxi|{^*Z;;~!o<(UfQX=de8f5n~Wrf1ByIVdJJWHJgrnGwnm$v?Szqq)f'
        b'Hh&>H1hneh(rs^XqaPMswBk1rI<_q7yUp>!cE<~Phob~Hc2dQknhE8Ry2JcE$-J{n#+N1YHD%LB`K9P{DW8_xb<UF3`#tU#Si;w;'
        b'>$C<#=(jySBMgB&dK-Rfj7$AUY@zpfOr0J=?PW~1MJC(7a?|l>?zO>TkH+zvsSGdiG}};dPNA7jrupDFw|x*z_neh_+GVD|qHZbu'
        b'I`;=WihF4=<1>BJps7@y@omkZDKLj7J5%w34LuSr6$e?Ev)X>PUDDzl3;hmNv*#SWk5;vLIRdY=({q`Aeb3HzDOZa_x0GEeUMtW3'
        b'=EG9<!@299yo1!gFgSNk?j5(=UKpGwHQCOg7@9mAt^YdJWc!NA!|^nE&RN@-q?{g)x^q8?Vr%!D<DSF|OUlbW@nPwYKAd}d?j7Xf'
        b'#|N|j6GhY%jI%v9Xehm1zhN+YJ^FHo!E>3>I}D|{`gMc$(i}snS^pm>;2cBgT!W`iZE!3pwXE-%VfPRw&!5Z5b_G{1CdYlN`sE9}'
        b'-HM_dKbQU?8nYrV{%&HS;mL+i7T9RAU1G>1(jFhX;l2U1D^FYwm)-EYZZ2NF>0LJ?!<QrP$B>SE8VQTC|6e2HQGP~QuI$?z=d<4D'
        b'wB|G$JVdchf)1)>AEO!T)^^Ley9OuUXHiyo4ed;nCr7S@9z~dp7e~;tZdppOU1Bed;+pW5&}OHNbOustvYnn+oQo-*?3VBeq2IjW'
        b'AKRHZNNe|Wb=WJd9UIQga?ENxKGggs;i&)4<5S!6KScd?g4fj7UqtyAzl{hLJA+r*i|=zp>r&x0b)q#n#5E;E)<iG6Wktcc#>eoj'
        b')0Ft`1zgrpzT(#7xtyLqPX-o$JPU8*^)PG1B^R>n2D+TBX*824uvv#6@IhVL@I7pt=EDYq1SKU(&}ui?^8A&^y{H_)ZRyYLiXHrR'
        b'AaH)bdw!tP^SiRc0$zB#gj<4_ZP8>&O=y{93UAgqZPIT1avikn@H^u<PMrU<fxxK&?@2Vjw`?FXzdba+$#d-H1&DDA&%eddU-Z1A'
        b'dUx#Lk%7RG0q-DMM0;9L=<%fBlbjMR8!x0#L(i};rV7X<Hc3HT$_q<uQj1<(kSx5<U5|@z1ABj<E)o4#L!tj}dcM!t5VcZgWn@vS'
        b'(o{KhE0gm=zr!>uuOzi6*-&C|TI8(3f3K9yTV*w@LUYC2Cwjx@0r0#Us{_qD70p|aEWYD^R^Gj&Mb69+!y1L&@Us_e{dZ1Jxxp*1'
        b'cE@n<^`oAx>5!jRvc}3AkAbCx_z2cgBG|@D=)zHyg;4z`jg%L>jK1(PUL5$lW$-Jv`1*GmKdN`B+sStmmFQ5?;F(%&nG&cS*jYO;'
        b')J&v3FK#+LJ5W8avw9#u^sIt`Oh~Drl{0sfP7g`j8S#e^@H>xI(n%eTi!|xT#7~O{TlEzKnMS6ma&~mxQ#6?&)&KTG6cV*|+q|vP'
        b'&^ejYc9xY5J1(XhpS@(B7Qa#H<v(1VVB>x@K=0+1LrNLlr_d1T1v&2&-0S5&T)ixvdj##;vv?Xh0-j^L8dK`Blx$yP_AmO`uNfa{'
        b'q>Sgo_h@ntp`gFOK~YQ}y&e?r5Uv<a6IX$X#=iWo1a9%bJaJe$uP^_i!2Rn0{Zl+BPcc`G3izInP<C9-aewF+A3?O<ZL`}X_5f3;'
        b'FQ8D?EQsrtpo}zm{~vpZ!8NQ0@1ko$Bo9d>&yYqfty*c&84N#Kw}V+(Iu*rtrB^YVdL&62B!lwlqdgvLr$@jAvr=4F)JgqRBh@cA'
        b'4xzF)6tJQhdi3fOR9luWYQ@9M>QzR{|Dxa6X|3{iOBzb!ouzRoNP|AUM;|wvs^96r$J_%!To35uO7i>*me%GhQYcOdI6l9`@u3VT'
        b'KBaMVG_5UaXsk!Oj|yhsINwX7n6%@CawTG16esm@MhZp3*xWDgmZ9~WpqlmS6*E44dYxgFb-my7s=q%9wKu#&rBk`r@k)L1w5o4U'
        b'yJDEeaT?N3Egt)xM{!d-januTMY&zEU?~dsbj~6Ybu>`EE->&9)3W&qbLeEBiG8cGCm=)9=Qruhn)&xpW`oaUejKH?R7`DyH)>`Q'
        b's*i+rnRxAxXjg{bPvj-GJQL(9f}uU<-r_7(azDWvLGxlA%G6}v+l6X6ADN|e+Tx8=x5TIwGmnq!+M=qZ6L*;L4bUC_lC9fh6`xdF'
        b'RNMi43~rU~*5UOkdd25+LUlCWUDHBY!|7R#Yg@EDr%{5&oZHh);YysF5}ED}Pv`MZ{00y5+IG^F;51I{ioU77DgCH_WjZl4UfGQE'
        b'2OeA6`cb!hV{yA|IEp~6(v1rA8GOMQkD}c!&%Y#C*WDj{VBVE`qaHBFTG!<TA4$2g-ord#mZU`S>G;|1b$=F*Nhk~QU7^E9@!T=~'
        b'4sjg*eMQaW?<*GXxpF;Tg?L2UWj=r1Qop#Xp3ckvOuUZd)W)FLt?o;smCnUdr^m6y`B9C;NAemYh2J&!+(!n()Owz&(V#sx`3^4e'
        b'cZQ1pMhtHJDDc!r-lsn5^gf#QnBX)>`ca}K(#beo_MmDl(ZR{;dDc03Tnil!cR$AM6Y~~%{eZ~hV#p_SOT>fjY^p{U`OP$Sfa&zy'
        b'j++lxh2u>N1N6^OQ~9b8Ji|*25}AY7I2;!l6vas0*)N@kLZp2!gzrhm^=!+8@PqYizf@e>rAQw`EcZ&W+_&r#uJ6mp_-wS`y*G>x'
        b'{P?4tKmG_+x46|ko0xpIJaP}E8SN_bF7ap=JZMHcgx8r;r*<jvky%G8J(ai<5ab))7;9>(udICiijOo?<{UJcUr*~;v{mb`??(J{'
        b'&`z(Sx{1Pl0={eVhcrWRDM0HgcuPDW1`ihCb;a3d;C0CeIu5Ptd2wAXw66LlNB#4a`;0zxyey#XGh`@;c|9Fx&0#F-ugB7iqG9qX'
        b'a+@f#wp$k7jQ>B@C;#E~8UN??O(sNV27&8=WVDV=H?3n+<-T$sc|y)p{W6{pJw$oadX|anx#xdcPbqOjc}8ujo8F}m<U8LO+tY>y'
        b'>RfnZc#7XB7Cy8IJ~8Xgrh;uw3Bj8EPA`60(`3K0TZRIcUw`hTlt{jtmRs*@OumPn>LbgkmFcm=3SwVUxwc=jGCi?dj-sU?j(_Tt'
        b'cuF>SJhF3p%<H38O{q9#%~4y{mz2s-6;{&Rh!>Y0*IkaP)$%)v-e%A|syqeiKN?c<OCDaun|-Ek1zK&o)Qt`v#dE%I_C_hri_gJn'
        b'V^9~jZ&-W-!{*7>K<GI$uR<(4y#1G?v+o*BUNX+XRlRtOJXgz0ik2}CB<T70Zi??Jc?~Btim*aVM{|5#lX(}NEDoYxo6e9rwbO{-'
        b'@Puj*6Rrz$n`Rp0>12aJ6&g9Y<l-~e$|WYRvZ&Z!l-j63$L`{TSF0}H(5`wp+$MVH!@p}21(tufbNPq&#-Q?i@uspL2$y}w^R^qy'
        b'e&k#P%YN73=|Q_|YopR-r^mM9yAQ(8V}!~vN8FITah{M7i>Po5xAuc@4zY%FNb?(GZFy*5TY)Y2!#bVqjt_k#Zn&ZYMnN2!6ECXZ'
        b')y_bQxW&OXyCj93<F}*SGNVzfBX6iP?xcceaK0@N^Q}xAgUc3sy=*l#qM{XFE(=Fz^#@|Tnw|7vw*)u2QE;;k&1YWUPKJv?sIVoV'
        b'k*G4clL}QQvPg9j`pw;cu59}z%Xa+fNCfh61hQln4T{8AzuhMG9MHC#QYChe<OgEXX_Wp?<?;VZTvBg{%dvkhF693lmz$6Ew^Tu>'
        b'3g1*2k6N9fwM#?00`*rc`Yd^NSO1c51PV2{dnT^_|5i8QHaBi?cd1hny{~_;^R@o0&07<cc=FEX{**<iEkuXg(D?5A|4aMu*unpM'
        b'`*6m={}=5;RJZhuzGH|Te6l~VvERF~ztdA(_SJ-VQj8RzF~B`&-2UUn4{W)1z-R9a7;8B9ma=P+PGvh@uTz2!C!;P+ldHi-4)dC<'
        b'=mwh<H3WIe_HchgfZ-F|*{Ilwm9o*El2F|++sL`LFucvtDsj{@-em_pyqaj$F!kTnH!<G(4>HUKk6VozJE$>%TAMzO)^ba5n~%%v'
        b'r=x3YLyw3CyFA9m;7X6r){5hay85AK&%F5AeJLu|7Ov%6p<5biQ#wOYP02!0BYilYCNY*q$`oKM*#?8e)FwxnLcJ5$gTc8536mic'
        b'>nCw}GPJxxuH~G7&sgB){VK9N8OqJ5`+}BQn2nZd%jicfQ(JtvqOs4wy_w?&of0NJL78q$XqDp5Zi=i>S|ByrXU0i!pAN4lB`$v~'
        b'{GN?)n{HZvAfex@Mf+vz$f1e<wN3W}_2-@&>QBSX&kl=qcz?JKzj8pV!##i3H<n1swOgJ(u;Tgk={h>O+9E++uJj*?$3xWDdRgpi'
        b'MF(#eUvv}B!<<pfjAXyOoa&a9A6@r_*w<2o`&y6s$Q94KDE}#c3BSs<8@26Ar=Bd0vzGgZqY0GhU#9vM?b0(l8%pE2UmXzpT2t5N'
        b'IB;*PK_9nBng6#?U!fdVKk+NmarL7hikoEJRF5YG?U|JZf{VgY;O;ztN_<xIeAH^MvFK5zEYzf=q9HmJ7k)*z#H<sKjG?-0S)6G`'
        b'sMLqs1-QQJ^bqzLDzU~ZrW7|<dBtOs>ntF-GdQkW^aq?CCf9<xCa5_rwP>;uaxD_nEkX@ynRwC&cfgLX^^paXbB3lkL2~_=GAF#|'
        b'0@R}HdtSV&aRNWI_;>MGaBDo~%5lF4MZ=CZy-$pX(06k@oSx(2(6Mk#P>0I;D)SHHGULX$ym&)gP`+WlGkLyY4d{4p^2!-=rFfkB'
        b'N9Qw8-Ldsx3MD?0u(K?9({m8?+?xjvMh3I)MY-skKKwrV>Vq#!Xx9_Gx+{928{fjG@`s*sn0&_-J~5>liN?>{(hF&7geK~ipf5>f'
        b'bm&>_79D|KA?zVqqQo$>XsU(6VP?@uX%w2BMAJrMh{*e%=_GC*?h&D|`2Nzl_<Oubf&!s_3}?oJTy9W2_18|0d@qQF7Qeq{%ft^p'
        b'R~jjAXnE;6m3VWPJUxd@`^^NG9&GTOV|c%n54{%FrK~_{F!^xE<b1&kgVTe7=|S)G;Dajsiu1+^Zd#Br`mF}dY8{n5(T8tM#1}nP'
        b'jcm3}l|$5M966|W#W-@9$o)f{Du@<!eWq{mOs17_(?|coOp&-V1=3^#L0Z{DDa&jja=b?`s8B`28W@HxVRG<Y8-&ivFk6^H9SUpc'
        b'xs5gX*#i8IIi^q=-y9WnQaSBp;>?qC6{&>jz-Xa#xo%DBQ#nkjP3^EME(@mq$#JIlFPf#M{lhg<x2`pHcMj8RV^El{1r&0qe>6HK'
        b'aeBsV%blhG3O3ZQHtipX%vp1{`@YsyyB{BQSed`sSckP2zheZ=hN47ht+W;$A5a8Qq-Zi`l-9<e-7{*?BpcWQ>E)A@DhCZ*UU`{i'
        b'=ipmgOd8g}G0a6Y2P>6kk&|0Q8)C%$swYaV2a7(JE+R_O)IT*a;w$y;`AUe96^UO_x|vD#iwkBgtJawftVU-xu`-?6&eA&b5|+`K'
        b'SF(DYc|B{;nVoE^4lQ-vzx>TYvTCVC%W9++11pnSOe`(6*jYwuS;Fe2mX)kQYFW>wN-fS9@!3&Y%AP94>72?ir|@dUvWUjZtfBF9'
        b'7$%2hLz6<ic%n#6{I90#xBq9;?^_-!GK^mOeE!}?E-t!#;mB*R8S;OexVN<->cCS100000000000000000000000000000000000'
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
        b'000000000000000004mhhdnqD000000P=rr1XWd4RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40753mj000000LcHf5mZ%GRaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RoH_A0RR91'
        b'03iR@Mo?8%RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RcQ|n2><{900jMi?F|C}0000000000000000000000000000000000000000000000000000000'
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
        b'00000000000000000000000000000000000000000000000000000000000000000001x$I$Zly'
    )
    _firmware_identity = {'protocol': 1, 'firmware': 'CNC_FFST-S3-0.1.2', 'app_image_sha256': '21a3759a96a55d5022f0f6e647bb67f44d354be5a6a622462e19bba99207c979', 'application_file_sha256': 'de89cac6d39c44c369074fe86d013b07d503985283dadf4e995f7ee3a035c1e4'}
    """CNC_FFST HMAC v1, shared key carried inside the bundled BIN. No unsigned-motion fallback."""
    import argparse
    import hashlib
    import hmac
    import json
    import os
    from pathlib import Path
    import queue
    import re
    import secrets
    import threading
    import time

    SAFE_REALTIME = {0x18, ord('?'), ord('!'), 0x84, 0x85}


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


    def verify_firmware(port, identity_path=None, writer=None):
        path = Path(identity_path) if identity_path is not None else None
        try:
            identity = json.loads(path.read_text(encoding="utf-8")) if path else _firmware_identity
            expected = identity['app_image_sha256']
            version = identity['firmware']
        except (OSError, ValueError, KeyError) as exc:
            raise RuntimeError('Manifesto do firmware ausente/inválido. Use o pacote Python completo.') from exc
        lines = exchange(port, '$FFINFO', writer=writer)
        if '[FFFW:' + version + ':' + expected + ']' not in lines:
            raise RuntimeError('A placa não está com o BIN CNC_FFST esperado por este programa.')
        return expected


    def mac(key, message):
        return hmac.new(key, message.encode('ascii'), hashlib.sha256).hexdigest()


    def exchange(port, command, timeout=8, writer=None):
        (writer or port.write)(command.encode('ascii') + b'\n')
        lines = []
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            line = port.readline().decode('ascii', 'replace').strip()
            if not line:
                continue
            lines.append(line)
            if line.startswith('error:'):
                if '[FFUNPAIRED]' in lines:
                    raise RuntimeError('Firmware não corresponde à edição de chave fixa.')
                stage = command.split('=', 1)[0]
                raise RuntimeError(f'A placa recusou a autenticação: etapa {stage}, resposta {line}. '
                                   'Confira se o BIN CNC_FFST-S3-0.1.2 correspondente está gravado.')
            if line == 'ok':
                return lines
        stage = command.split('=', 1)[0]
        raise TimeoutError(f'A placa não respondeu na etapa {stage}. '
                           'Confira o BIN CNC_FFST-S3-0.1.2, a porta e 115200 baud.')


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
            status_only = bool(data) and all(c == ord('?') for c in data)
            if not self._raw_tx.acquire(blocking=not status_only):
                return len(data)  # A later poll will request fresh status.
            try:
                return self.raw.write(data)
            finally:
                self._raw_tx.release()

        def _authenticate(self):
            image_hash = verify_firmware(self.raw, self._identity_path, writer=self._write_raw)
            lines = exchange(self.raw, '$FFHELLO', writer=self._write_raw)
            matches = [re.fullmatch(r'\[FFNONCE:([0-9a-f]{64}):([0-9a-f]{64})\]', s)
                       for s in lines]
            match = next((m for m in matches if m), None)
            if not match:
                raise RuntimeError('Resposta de autenticação inválida.')
            self.nonce = match[1]
            if not hmac.compare_digest(mac(self.key, 'server|' + self.nonce + '|' + image_hash), match[2]):
                raise RuntimeError('A placa não corresponde à chave local.')
            reply = exchange(self.raw, '$FFAUTH=' + mac(self.key, 'client|' + self.nonce + '|' + image_hash), writer=self._write_raw)
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
                    response = self.raw.readline()
                    if not response:
                        continue
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
                    if text == b'ok' or text.startswith(b'error:'):
                        kind, self._kind = self._kind, None
                        if text == b'error:78':
                            self._responses.put(response)
                            self._recover_session()
                            continue
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

        def _signed(self, command, kind):
            generation = self._generation
            if self._recovering:
                raise RuntimeError('Autenticação sendo renovada; comando não enviado.')
            encoded = command.encode('ascii')
            if not 1 <= len(encoded) <= 200 or any(c < 32 or c > 126 for c in encoded):
                raise ValueError('Cada comando deve ter 1–200 caracteres ASCII, em uma única linha.')
            payload = encoded.hex()
            with self._tx:
                deadline = time.monotonic() + 120
                while not self._ready.wait(.1):
                    if not self.is_open:
                        raise OSError('Conexão fechada.')
                    if time.monotonic() >= deadline:
                        # Never retry an uncertain motion automatically.
                        self.failure = TimeoutError('Sem confirmação da placa. Pare e reconecte; comando não será repetido.')
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

        def write(self, data):
            data = bytes(data)
            if not self.is_open:
                raise OSError('Conexão fechada.')
            if data and all(c in SAFE_REALTIME for c in data):
                # Stop/status/reset bypass HMAC and the pending-command queue.
                if self._recovering and all(c == ord('?') for c in data):
                    return len(data)
                result = self._write_raw(data)
                # Firmware reports session reset; reader renews it without resending moves.
                return result
            if len(data) == 1 and (data[0] >= 0x80 or data == b'~'):
                self._signed_realtime(data[0])
                return 1
            if not data.endswith(b'\n'):
                raise ValueError('Envie comandos terminados por newline.')
            for line in data.decode('ascii').splitlines():
                if line.strip():
                    self._signed(line, 'line')
            return len(data)

        def _signed_realtime(self, command):
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


APP_VERSION = 'S3 0.1.2 — Controlador PCB autenticado'
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
        self.running = False
        self.paused = False
        self.m0_waiting = False
        self.m0_stopped = threading.Event()
        self.cancel = False
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
        self.simulation = False
        self.port = open_authenticated(name, baud)
        self.inflight = []
        self.work_offset = None
        self.work_position = None
        self.modal = None
        self.probe_state = None
        self.status_time = 0.0
        self.settings.clear()
        self.reader = threading.Thread(target=self.read_loop, daemon=True)
        self.reader.start()
        threading.Thread(target=self.query_settings, args=(self.port,), daemon=True).start()
        self.emit('log', f'Conectado e autenticado: {name} @ {baud}')

    def query_settings(self, port):
        time.sleep(1.5)
        if self.port is not port or not port.is_open or self.running:
            return
        try:
            with self.lock:
                port.write(b'$$\n')
                self.inflight.append((None, 3))
        except (serial.SerialException, OSError):
            pass

    def disconnect(self):
        self.cancel = True
        self.running = False
        if self.port:
            try:
                self.port.close()
            except Exception:
                pass
        self.port = None
        self.inflight = []
        self.simulation = False

    def read_loop(self):
        port = self.port
        while self.port is port and port.is_open:
            try:
                response = port.readline().decode('utf-8', 'replace').strip()
            except (serial.SerialException, OSError):
                break
            if not response:
                continue
            if not response.startswith('<'):
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
            if low.startswith('grbl'):
                self.work_offset = None
                self.modal = None
                self.work_position = None
                self.cancel = True if self.probing else self.cancel
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
                        self.cancel = True
                        self.emit('error', number, response)
                    else:
                        self.emit('ack', number)
                    # Sempre notificar a thread que enviou o comando.
                    self.command_ack_event.set()
            if low.startswith('alarm:'):
                self.cancel = True
                self.command_ack_event.set()
                self.probe_received_event.set()
                self.emit('fault', response)
        if self.port is port:
            try: port.close()
            except Exception: pass
            self.cancel = True
            self.emit('fault', 'Conexão serial encerrada.')

    def sync_command(self, command, timeout=10):
        """Aguarda evento de ACK; para G38 aguarda também o PRB da mesma sondagem.

        Uma única thread continua responsável por ler a serial. Nenhuma consulta de
        status, dwell ou novo comando de movimento é acrescentado na sondagem.
        """
        if self.cancel:
            raise RuntimeError('Operação cancelada.')
        is_probe = bool(re.search(r'\bG38\.[2345]\b', command.upper()))
        with self.lock:
            if self.inflight:
                raise RuntimeError('Aguarde os comandos anteriores.')
            self.command_ack_event.clear()
            if is_probe:
                self.probe_result = None
                self.probe_received_event.clear()
            # Guardar na fila antes que a thread leitora possa receber o ok.
            self.inflight.append((None, len(command) + 1))
            try:
                self.port.write((command + '\n').encode('ascii'))
            except Exception:
                self.inflight.pop()
                raise
        self.emit('log', '> ' + command)
        deadline = time.monotonic() + timeout
        while True:
            if self.cancel:
                raise RuntimeError('Operação cancelada ou erro da controladora.')
            with self.lock:
                pending = bool(self.inflight)
            if not pending:
                break
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                self.cancel = True
                self.realtime(b'!')
                raise RuntimeError('Tempo de resposta excedido; feed hold enviado. Pare/reset antes de continuar.')
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
        version=self.status_version
        self.realtime(b'?')
        end=time.monotonic()+timeout
        while self.status_version==version:
            if self.cancel or time.monotonic()>end: raise RuntimeError('Sem resposta de status da controladora.')
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
        threading.Thread(target=self.z_zero_loop,args=(feed,),daemon=True).start()

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
        threading.Thread(target=self.mark_zero_three_loop, args=(params,), daemon=True).start()

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
        threading.Thread(target=self.probe_loop,args=(params,test),daemon=True).start()

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

    def send_manual(self, command):
        if self.running:
            raise RuntimeError('Pare ou conclua o arquivo antes de executar macros.')
        if self.simulation:
            for raw in command.splitlines():
                if clean(raw):
                    self.emit('log', '[Simulação] > ' + clean(raw))
            self.running = True
            self.cancel = False
            self.paused = False
            threading.Thread(target=self.simulate, args=(command.splitlines(), True), daemon=True).start()
            return
        if not self.port or not self.port.is_open:
            raise RuntimeError('Conecte a controladora primeiro.')
        if any(re.search(r'(?<![A-Z])M0+(?:\.0+)?(?![\d.])', clean(raw), re.I)
               for raw in command.splitlines()):
            self.running = True
            self.cancel = False
            threading.Thread(target=self.manual_sequence, args=(command,), daemon=True).start()
            return
        for raw in command.splitlines():
            line = clean(raw)
            if line:
                with self.lock:
                    self.port.write((line + '\n').encode('ascii'))
                    self.inflight.append((None, len(line) + 1))
                self.emit('log', '> ' + line)

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
                with self.lock:
                    self.port.write((line + '\n').encode('ascii'))
                    self.inflight.append(('macro_m0' if is_m0 else None, len(line) + 1))
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
            threading.Thread(target=self.simulate, args=(lines, False), daemon=True).start()
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
        # A resposta ao G4 chega após o esvaziamento do planejador de movimentos.
        # Assim o fim do arquivo significa que a máquina terminou, não só que recebeu as linhas.
        commands.append((-1, 'G4 P0.01'))
        self.limit = limit
        self.running = True
        self.cancel = False
        self.paused = False
        # A escolha ocorre para CADA arquivo iniciado, inclusive na fila.
        grbl_mode = grbl_mode_from_z(lines)
        threading.Thread(target=self.stream_loop, args=(commands, grbl_mode), daemon=True).start()

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
                if re.search(r'(?<![A-Z])M0+(?:\.0+)?(?![\d.])', line, re.I):
                    while not self.cancel:
                        with self.lock:
                            outstanding = bool(self.inflight)
                        if not outstanding and not self.paused:
                            break
                        time.sleep(.015)
                    if self.cancel:
                        break
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
                with self.lock:
                    self.port.write(payload)
                    self.inflight.append((number, len(payload)))
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

        ttk.Label(top, textvariable=self.connection_label, style='Muted.TLabel').grid(row=1,column=0,columnspan=9,sticky='w',pady=(6,0))

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

    def disconnect(self):
        self.finish_timer()
        self.stream.disconnect()
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
                raise RuntimeError('Informe um buffer entre 16 e 4096 bytes. GRBL clássico usa 128.')
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

    def resume(self):
        if self.stream.running:
            try:
                self.stream.realtime(b'~')
                self.stream.paused = False
                self.stream.m0_waiting = False
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
            if self.stream.running:
                raise RuntimeError('Pare ou conclua o arquivo antes de movimentar manualmente.')

            step = self.jog_step_value(axis) * direction
            feed = self.jog_feed_value(axis)
            self.prepare_manual_simulation()

            if self.stream.simulation:
                # Na simulação usamos G91/G90 para o visualizador acompanhar X/Y.
                command = f'G91\nG1 {axis}{step:.4f} F{feed:g}\nG90'
            else:
                # $J não altera permanentemente o estado modal G90/G91 do programa.
                command = f'$J=G91 {axis}{step:.4f} F{feed:g}'

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
        available = self.active_file is None and not self.awaiting_idle and not self.stream.running
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
            with DIAGNOSTIC_LOG.open('a', encoding='utf-8') as diagnostic:
                diagnostic.write(time.strftime('%Y-%m-%d %H:%M:%S') + ' ' + record + '\n')
        except OSError as exc:
            if not self.diagnostic_error_shown:
                self.diagnostic_error_shown = True
                messagebox.showwarning('Diagnóstico GRBL',
                                       f'Falha ao gravar log em:\n{DIAGNOSTIC_LOG}\n\n{exc}',
                                       parent=self.root)

    def poll(self):
        try:
            while True:
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
                    self.status.set(f'Pausa M0: {event[1]}')
                    if messagebox.showinfo('Pausa M0', 'Programa pausado em M0.\n\nClique OK para continuar.', parent=self.root) == 'ok' and not self.stream.cancel:
                        try:
                            if not self.stream.simulation:
                                self.stream.realtime(b'~')
                            self.stream.m0_waiting = False
                            self.status.set('Enviando')
                        except Exception as exc:
                            messagebox.showerror('Retomar', str(exc))
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
