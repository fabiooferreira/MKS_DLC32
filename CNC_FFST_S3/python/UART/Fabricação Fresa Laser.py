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
        b'c-riJd0<r4)%cwyAqfvi03%C~mym=6Ct+qn$YPM0?13y}62j_7CdnijO)_z2BH)+SOt2UbTb8zhpMIT0s7RqKQpJS|XenB-pl!7('
        b'Ew$3BpH-?>0ttD)bMC!wHo)p{`|BNe@7(R&_1tsMx%bY?M;f*1(6&6&r-YD5c!(t7TNRQ0`usf_^h(lH2*4+fKPeV1k(wY8ro5=C'
        b'N2G-(44!a!M#0nWaM@S3**e6$d18i<%q}Y|p55qZ?{sw7I^3?=4GxF9&0%e_Iaj*6Iy)Us_iUH5F)+Bf&FX4RZzSz@mm?q}>TOu#'
        b'wyo^wYR9lSB$Q~S(`Id2>1uB3yf(_V+Sb?w#88!XYey5sjt*k$XfoXHa$B8l!#Am_y`!<MtH~A^)#bLgrMF^6MwXG0V9ZJg5N{W$'
        b')7sSJ{H7gYb9Jt?w_96mE1Mn8cB>mYqQKhL*wtor+nU5yXbLG>-Dzv|`9i7!eb8cebhuVJ?zK7Ftepgqy?M<_Uqx&#m(4}Y@OHYz'
        b'W~;poGO~AwNiH2cxk*i8N|GyeOcb#;K$TKb#Z^|9*l2CTWLCFmDG>Fmll0lEAw?_nW1CHkpC?u>Dlh*Q4a_jQGJ>L8t<cOStJ_M)'
        b'J4u`)&YLIdNpKQl=G>Ld_6~b+n|TBhljM~RF4syr2*@DJ3*+#AP&FO|)k~&j1m;ftn0-KcsGplObTv2IoZq%%0)m~;vyOHsG?0z$'
        b'ZEZY)&P_ID877b9nY=KG=X!__K8zuz?l59H+(YVT8K(W<5MT)IAz81_$2tB&?(6e2ZhL*c<~HV!gJ%-Bn@mFeCzwW0>S^xLR4kAW'
        b'q}S(L&I|Rm@GOC61w8feG{Msf&v|%0fagPaK7r>VJYT{y2u}nN>IHa8!Cel|p-IGaK9-oaO(rHw6fqqIzx4DgTC9Uah9zRbw*4Ji'
        b'Hzb*$-sSK-7EVkP>(%wp0^$b$B*+hI2Z=uGBwDEJPoTCYlt}eh>HB*mNsHm*h(zkOB(IOQAJRQ2rO@>Ih;;v;Gzr|%5I3g}<D~nu'
        b'G43--%A;vUL7uHdnm;HJ69~l!+O?{-JE0(`L&^;3XASG`M5udV5;5rje+hm60K`l4k3yEJk;3y(wxl7_OIIaR{y0cIiLlHrN^?D`'
        b'_^ncGHSuhg&PNbi7>S)lZ09ubKcImRW8iVGR~Wrl<#`A_dsP>HrHOt1>R#2(-)egIJ?@<)J~-v{fS2qf<cJzV-_^`D6LCQF^kDL|'
        b'sA(6$FHG6_m1e-JO1h#Err54(4EIU#_etjaq@yB9)xax7>sc-JB#7wO3Ti+JjbvvEiFZo|w>0zVv1eV<F}HNE-_q}rZ2!>2yCj1P'
        b'!bhKVO2;}N{EqO;QqltAS&yZ9`uy+syQS_AAir$2DI*$ij+%P9e<yowQ%F)RxzI{36q2NTO<Gi4?#)RhQ1iOyV|SJ!&W$xJm-cFQ'
        b')@f`O&CX<vd5L7yV698F`Z;srw8;fGKU1S#S4D)v<QanSz*iZggoy{eYW>2k9viKRMfzvC)E9BKTsl@R&5PO<arBVt{eI%9r(LS?'
        b'tfZa4P9sEljOd&fB~0<?(bfCfWntno+3I{R>3#XKF!`Bml@Qtew(;eE^<+eEDinoDLZp7%T2qdw*Sk->Jn-5V-G@xOqrKT{W4{PD'
        b'WMBtpYYaw?4IJw^p3QMO$7vkvIKGwRSsbTwoWk);j*}TSCrRZI=+gFN;85mh%?VQPzL$7VGz+>#5+*QLoJ8@33}U;DOuJaFZEjSr'
        b'J1FV2Ujg1P8DGAf@9jCU2WG)sD}lbbg?7_TVV;T7li7D}o+$N2ZkxP4X7hMyQ(rWFi|bXkLt3wQ;+YMq&Euq9s!hA2dv=RYsgj<9'
        b'Q0;jLje^j_F>?5YY~mRu36W5d?Gc_Zsrxc@O}hxiof(1Rns@*B#8(pVuq}g7UiOTPY#tdwo{cDv+Qe8k!ZS3oWe1^w-Ji&T@n4N>'
        b'zJw|J)WUSA8@Sf1sdw||BSIzC`JW?lU`nLtvyq;JXwRqc7U7LqMA96+JU^PM|HBdP$H-lg3Hyk+J6bS`yD{)74BQsce}2TfJ$j(O'
        b'$Gcsm?b&>8gr+|5-pJWMjqKkYec&B<`zQ`a^uIN7^aUKC=dhT=QD<Jj$mgOcRoj0a-5o8b-4$`{Eao6Q#50JXfd^h4IX8AcOBQk9'
        b'<VgRC5nl!ooIJww%1Hk!BXTKyQ3w8WMCjhndM2v>rI7<K(e8@c-xp1TJTHzM-1ldig`71j?Aa07-~Wq|1HbT59XK>1XU7USFoL1`'
        b'gF++w_l_JH=Vc+0EM)fx^Y_}xfY<JM5{F)xE~K9udt}^k?<fo#z_5R)&#8rRLia(h3d0_!>Bb4u{sCb}#$eDk44QTkc-Bnft49(N'
        b'$c4-5fd;Y(<uru#&mTE9e?%DVJ$2MGHz4hS{E;`js^i{CAWUs@G%&H%-juDPSkL2k-mK}*89C@B7p7=>y()h!%nd{Lh@gI`KgW<7'
        b'pR`na1e{4LweV`xo>QMzqu(}NyK}8}Uev&`hzoVv{(DA_-815Sdf+U)pXl}6gY`HaB~%<yV*(S<?yS?&Ts-!Xy{c^y*^{=ba$;;X'
        b'+P$hHYTHskwmY?SK3sTRq8Mrh65bZB0f#W_LYRiu+d~d4ABij93-$FZ!&2s{D%1lri0P0xH6dv{S(wpW{h2Uz?`T^LcEsF%viXh?'
        b'qm_+{QI*(VIU;7nc>AJLJzS<lZWc$3sw6gSr6U(JR1mw%7wg^Gb>U6zE{~Y<L+{=s+gn<LX=JmBG6;xQJ_|LQ=dqAYjL|ekmFO8Y'
        b'LWObCX>I>p?3D|rwFAeZFFd9_qJs6z7(eR5kF}?!Bt58sHSk5P_hXIs;DC3a_q0YB<B3OF@5d877q9jhV^TaYk@X3pA!)>uG?MDk'
        b'8>1iGsuiXr)oEus#~nx*fsT4ULl~`pe(i;2P*?9jn5_-*6F1o!w0yh~A=W3Tk|#v%DM+3XlbkUHLIsWfeT!Zs#h|JP8Ttkb0rzEa'
        b'&ww>h_<{#~C6Q40b)Km<8MGA85l+B!FFfnvfz+Uzh?oMj76}!EPNv;SFTtZh-3#!a;kktR4q9FHk)S^T?az=NR2=*dMwrPxotSpO'
        b'GifR@MS~7E2_DqtV3LpsC`S;Z$$Ov|ehJUEIAQ{gicm`~3-g)J%|MbT>uCEYGyM#8MAX+HO`Zrk+c1>h2G2xr7l7XQFg$DE>9%O<'
        b'^O!F6lW49}Q9VqOMo?!Hx!y)~C<}GJ!qwPcqOyb~Xh8?v0cFkUB=xArLe)`oCDL@LYZlY5Q2!FZ{Ry-odKxj!0)2J|JgxAofoBec'
        b'Jp|YU_-{F{&p!k0UGjFGDFVVuJ*1xL!)j>nRp~=;&!PTk@P8(K3T@pFG)eGe!9#kopjNj-nJ1x-emlPa^MmJp7I##-e-!AFSx2Lv'
        b'eSQ8R=mYFa>3+0`9q_ygV;Bzko_wk1A9*I^0YWxIubg~|h!=k%O~3dPNVFf?zE2G-fI7RDjs;O|f&2&H5ylhKZqSMU=YJ$=1+=#n'
        b'9ydJ92B$i4eShxT7RciV@cdJf=8s6yuO+6hf>nN=auX`lm!aShYR&h6KKdEsun(cUdfNW6gpyB(@W0}qsL0U=Fg$|10{G=v%x6SG'
        b'{W}gGRBut?hSbQPL#7F8GHNv49S}{R^G3s1*TXmq(4W!p)PrC8LXtj!@=y;RhH;Rl4@%`zfX5)emgeSWavth?=oRfmv`3HzGF*+i'
        b'G*lESeLvK{hwAw_L!h-FdylAf>MbgL%fYc{Q>A0Gq=N$`{i)K<bL5eOW6q{X$C4nVblnvo_asUER8tyE!KJ+Q*bFH(23@OhCBv{?'
        b't-`dUY*lSVZ{M*v=`XiPuzVhyBJqem7I8C%@)fvG5Ge5xL4Rbc_=4*E?&#-K`=6&PIL&AEfw9u)jQR`}teW~<Dk!ncvPr+*t}ecv'
        b'7)D9i8lz@%ZjtG|wGe)?)vT5D=TxRs(PvI!>Q`GwXXGwIHEwnOzM~dPEhx{H8jM+r`DC{WTH&Vt!IApfwU$LHFGMnF+*%SF)^I|q'
        b'H~kP(ZEM&=>NBEEjTmR&1}|r8EUMA1f=0N>`q9Xynzg1ys`|ocOCcsHYt5P*W_(rB>yf;4SM?rZDU8<7p;_<393#x<MohFQV=JKn'
        b'Grzc$jeUAKg_e(c64o#wB{uohG2LH~$tJS3f74d|ri5q|u(a~#lOx<1XqB7D{i{y^8^ajC;UyM}yV^?hUjS>lPmeh=M)bOq&P&|B'
        b'F+V$E+}F5E>v<m6ffTJUX^C1;Tk5-V=jv0|ilCW4k+ARfS;=Dd+BD6c3CF#VW5m%HMPXUe70K)UGGSkVI4gSQqv~}jL|AtsgAk+l'
        b'WLB*DL=v%NyOZBkubY7th^twgp*{gJ>|tEgg=My{r1mK0$y>JbUy|427G~7ff2q%mj-4ARtb+>um?|h^u*Sk&wl5@bhQlK7Rqgy-'
        b'%DQR#Kq44<m;_qL(j@&8(g+)mX!54mE=m~xJsyANv<L|nBz-0c>S-6D4cLH(g=H81Aqhen)Z>Vdw=C%&QqS%fP)4y;0|Z+&<+pL+'
        b'g62-mx_2d#^`ng^K4bd4cwBs@X6)IHkz<aL{yRqw4s5aQCTB8YKKBwZWpY%YQ9T^@(2Cs`UZuTE*Fr&vdl*U`@cv}y-y~1N2$>ZF'
        b'E3LPu3svToBRydFB#1n%0d%h!WB}B!$poy_jSH~Wga}jPqLK!o)7{OleZsV(0q=7=|02omH5bnN+!74&z>{Y@W!MFB;Lk4nNs3$G'
        b'DWpTK+4+_9lsZMTOD&AIO@Q|5MbQmvS@8#GGkEf-$`j?e4RP$#VP2D4e{ZecTdQxY)mJalXD>RU_GDtDcu?$oQuG+neMDXVQ_(Y<'
        b'>LXz=wqYI}y0bDzLn{3fq9+BtC7F?6ace=tU`k}%D{)W9{azOycPZ}UbstIC2cGF81AC@ZlK|`iY6(zJTa@hGd^0E`N2xL;E5yA2'
        b'JmW|D$B%GYZbgh62}wz9d)q&y3&WDEuf&fU5gSaRDC;qMHOb?($qB-=iyjr$H2f-xLW0g>l!}-}+|>0jOqk|Z=k{!K_w=}%|2Vey'
        b'<UfST!aEN>FFvk55l+gdJh?rx_vA+q_GtJOX+_kN+oO6<{*N&EtCT-&65TR?;1C0b$x%MAPxAczs(%jxbT~0zOd17=W<EML+r3w7'
        b'yDE8~I4Vr=&REOoMWfiO8IzzEdir9-KC$=Yr7d1nf|vB9ZiR_z)Qp9Z&3azd{W(o<B~V7}0BVO9E=vPuGH_h9p+hCa9Z~I7C#mJK'
        b'x2c6m$&r!U8n(Q8^_f(a5YfZBht_$D5Fu_@3$1=!Z8EusQ}i3we)4vLh8)zWPE~h*zJJ!%X&2KXVjq(F)~7`F7#lZE>@m9Z2}i*~'
        b'(1_Vv(=^4Gr0&ndzv6xA*>g2{{5T=v!SPX^T~`y1k91!a*KbXWkjt~~yqX_Q>LzOM*l{&0^ES^;?4$2Qd3GTFi}$K%`SRn8Wq&<('
        b'|5d}|SFdW%pZ{0+n4`y|k7$6^9>X*nKi)ga^Izx^)Wx^~PlWLh@?#81C?>f{Yz*Qby4tHIkDc^9j1iuV^!)=$7SWrJ(cOdV>3CU5'
        b'yIM>X#TlX~P6RPmXAFz|-Y8SP`Fvr_U4?gsm;8v@5}xH(H-GnPPgitb<byYxx5s!^VP;RMJonN}#~oO6Rk)>m%;`}V_lX`ShV`ko'
        b'#cX_SZ-mEzzV6T0{X-&qBi2NE?xvM#zq;XjovV-bjjHcDdY^0ksD+ExeSo}a#aPoTqW)>oyG-00?rCIfv^UIiC%X2kcYXviDf}He'
        b'$M&i{D=^gdp<hmI@oJ$Ry<X9>er?Z|_q(sWce&?*_w}15g8lJc>4nFnQ&&!Fp-0slf90v9#2+wXPdWP54e_yLQuoXeQCP6^5sCF{'
        b'-scSC2n)vwufG4}>~liaHdxNi&bxZ-_N)E3Up?qe*tv-GY?>IGLh9D5Py-MyevCU-hsW&St>6E#=Hd%SpZ(>hXST;|I7lK*-c6gg'
        b'EF@F=uzwg&R-PM+R<1A=E!s@lzv(Q98@_rPc6(s5Td#6k7(C1z_9SD_=D4f<aaXzEpypQO=E+z4Cx-;ZUhR(!37T-V|AXP+py;dp'
        b'(O0h#SI9#<zm$Ziq-xTj4ihxzn`6$7zWSHZSHGj)ay)KU^PQR;RfXn==Cr2eW_58gX-#-8{?!=I--a3QUqHNhc(|WjJsER29u}^9'
        b'd&B95$HMLL?+))j|K+U0k3TR!KP-#`oyhb;G@TWD$9di!rffDV!*c#hVcf@mHJyw${lXXfDaOWsGR!w1_l~;37NqCbnD9alIUi0u'
        b'?+)*Z+;GM7&hVw|F~?`lES-ELYT>GfwuhgU-nnw=_AiVxXWki=qspFq;<7~T>*L<IgI;N2zvuUu$<&M-6&Twya;!V|NrvAJKXnhY'
        b'd?)wxCJCDNmZYe~J?5RilTJN)PNNg3l=?j|)~MF7O&NMvcY8eM6aS)o4N@&3L6z?%M>Hklqmq6Gv)r4%79>=fmhL$mcz(G5`QZ!C'
        b'OY@@Y?qZS`ESO^=Fo^9ba_iP^p>D%SpX$L`kziB5BnjhBd?ocplGt4&c~aHX-CJH2Ph5fk)t=VmlZK;*qnls&sHbPnt<T-s_x9*B'
        b'eKCipZs`4E%5&Mh3CUCYdK;40eJ<U){%}O!q~{XW8;d`aJ^Aaa!#|M-<Wslp3J+7SA0PgAXu~nGOI?>sP+A`zZ`d^aY{saBeUG2O'
        b'$z|Iod2_|sk4KI~>4fNh(en^?o=!OUX7p?Qo(G5NPQcEmCBp;5LIlM37Lc7!NT1At+Qe>CLqL*ON{-sGe|L<xzo#!MAt8BmpP2Ig'
        b'36viL$HeFuai>>`y)vAVQ1||&6jihO<`hq|Ix6L#5P9K8(v#z3gz*Ulq*zT-?%Aul@I&dzE$0Mv`0x4rvrQ%gPkiXP73<-#4R4-2'
        b'OxNFVYVgdps(bg1=nKRLx0Xg95C@J&CtZND!f;DoI-=dHz7RnUTFt%j<^ii|&!i)&fwQU$?@N!}m#lr)U>QE5HEKw#<|>T*ds6u4'
        b'm}CAc(%-bN<U>zql+2h01jnN<{8_4d?aGm;<Nai>%5ytb1R4bjCkRF0jGbyMBA*r!TR4o>IIG(Eo)o)b=*Kme%yWnHwIueHua0Qe'
        b'T|gVDSre6=kYdbHrN)G7NcV>iZXJ_dosypuld4KlWyegrC=6z0kAu#A@QKJ<Ge8N<O$Y~FRh_Cj@wpVR7vf2zGb(;qxD~{1!Z1~Q'
        b'aJ|=@*4Dj2&fYS7?3UrUpY`7|yb}!BGZQyHel~9S*p%V87eLkMpE&H9!bs@8%F|-q`{ZoQ@Uht8{_(>Hz410R=^s6OYU^?D+a5Jb'
        b'=!qVdRhGa#8A$ezuyY#F2eqC^nnGgw)~Mn0`(t{(f0Nj!+JDg8^Mcr~89w-%s~$o}^5{@ct7%lL`l1;LApPd6L*36)X$D%OEaN<v'
        b'hp5)I@p%8GAzAf;lKcM!zG&atu=&%W?su-C{fCeCL=f$kVA?+qb$@&f?Vo+L=YnY84Wi9T7<2Zmp<{0i#r>xLts$@m7AHoX{ln0)'
        b'H;3ZhJ#j@6CS@gpf+I{`oS+gSH>E^VO%QnCJDQTM>hQ&+WX9ODza2XE+oAq5LkIisO!^<m@cPi^-wx$wWj&`ZjwhbeLmM7guX^w~'
        b'b$9{r-htPK&S_7N8hED%wD!lN>T<^&`1Mf#uW8^GtLnm6QeD*8;d>7}H`ITa2447=B*gByYx7G()&oOXIa=#4hwf_0R%PW(J@CTN'
        b'^M_h~7AxFxF6?wTtm0@srG?W$J@Dkv>CqT*B>co6wA655$a4_ulzlfibLV6oR)^n04(uE1-$zTaeJ0gy2(SBU$gpkbz&08LV(wEY'
        b'I`;W19`BI8<*4C@LoL~1h8;uttRCx*p}U$|vZD|5Llv@qMoT)aDgKjm;32tO%?Z#a;{R*N&^$D2=FE(k1KWp$*yjsNGStO?kc4oM'
        b'4Tc{L#jhO7eNYI0@Sqyjg9BSwii0X4yuRMO?vzA?*zn)*adIBl9`^!U6ErI-hj4A4mZOf_cmyhXp;c;Er$wDwc4|@FT4Qt8w2NE9'
        b'r}lbPAQLxbgK_MBtjt7J(v2r~o|K-_?s*64Y_CfB;aa2jqpXQx@$R7$|CB)1L+-Y6scx3a7#<d<%{uh+b=Z9g{i^VfL8UqIA+?`-'
        b'6SKafZa5j;trnZ3h4DSjN5w_@Q#Z$6(1L;ahF4X8LOi0{z00;zs#~Vji~rL1b%}j?eV=}Gygu6u_%7oX4T1XftUn6m16#dNwe0?y'
        b'q4#XDPZFR80kn6N?Ip>Wm?cEr)!5LK<<rFmyu`Bro4<L~(1B4yk8Xi>KJtRP*Go2&p<^lt5T-uzqDmOOzfU}H^olTf<_pNUeIgY1'
        b'$)x6GiJRvR^<%O}o{!#~IrL}(m;^I()jiw9O+9W@tA&VlSAp$uI~LcR@2IoY2?<&D_*pYjtqI=8X3bn0vm`$C4&2aBRasKj!j#Ll'
        b'mThkMbzEwH!l<xP)y%}nDWhgStv;b62{W^nSS<-hbB)H9ELady2|W{tI1;{BW2=A;t(z4II_(-T(8Kpe+V)GOu_nvJx}BpuuU{$2'
        b'c0ZJ{Bs|ApICW+7=_|RJS<ginPF~Sx_GD#`?v2;<WWoafW!+!3+cs}px;M=BDP$+=wK?}})PB-vTP8u00c%9BRXaSf?~ZMT6xH^K'
        b'?AWOZ3;S|&QdR5kc&Pcrn-Up_C-39#g=)dCj)d(zF4Zj<j{p1$boDl~5VcAFr7-nFkN#&{y|*9jyN6`Nm@*olout{;|H-Sn%ttgy'
        b'*)W4+XGOv49>0H==(%uZc)^j#)0(|u+s}G-Ux6{&c6QTKVp5*;e!Ny+cvSys&qwBU?@B$pK&yb73ER)wEYh~KeaCi1#BLbbH7PcC'
        b'1Vl|m*5Q*U<2O9FYxKtMlfsAb-c$Nl$8LP%*y~r`f({TiTsXR0|J2xBF^|2|<Ne`#8+u+oI<SLyPc`m}S$}N%**_k*@L$r~2Qb%#'
        b'ed|D%I2i}J1{hSYvGKf9o#6c}b@S)P5(V`$nX0SmR8K;`I`(&y?|Jr0>x7nP)$4ABnFTSzn8O+Y483;s{?@H$&baH_qeuVf_%X5m'
        b'_}Wb=YySbJ`ue|oZXIJgA$>>P_m{M&!LxM>Ms4}k$o6BWBc4fBdtVdZh>y7VnFte9YkL>RdRdq-<*Q8f&M4_z)Zxv$Jg2ouzmdKZ'
        b'g-6qx1nt!92^$BV$()psn3Zr`OlZmi$IJ}%i3}3|@Rj0ln1qR0yR-+r=V$E}rs;(Jhk9(OkZbHa!@E4O3y3g!=MN-U-i6U%*cD^v'
        b'7aIw=pn)kEnc@N6FbWoa6NbZj5A*B7M(NmpUeS%-t1^1e?_4M4&Y}9F#<ThgwT?EvcFYaY`X|H-4@mLtR|HLtCwu}qm_&N5WB30|'
        b'eC}-0ucf}f96tNWqf`4HTD0yaa^4m5{HkrEMm0{{74F@x-#%(;#_F3oo#s^;AFKmwc2_K@xPk^&?u~O(Jaxve(njs_Y`jkxEohP+'
        b'ka9eA4PRs*`)bBb*4iuC;Tzw~j@`Jm`jxnc)kbYtR?34+FHoP>2(xznmF?5Ts|=?v3lZ6xJ0luqsCt{w+}~VwWnco?wCT(JT``Y5'
        b'I&s^CN9KmFo^jvyN1iE6=+_qCgy!vL^A$+&$fM@EY%TQ3d~EOOQFz<IGY{RMFdbXsxec9h!og!pUVFlmfu8pk2$QBR+TyJ@zAQfS'
        b'qaPNl2uaZ-tHTresXg2Cy`$^3U_uY`^X-iwt3j*z>t!GX>(P^PC3!-GXXcgU8ESa1AD^S{8^8I~<@ls47K^s-3*6;QXw}ip&17@@'
        b'l}!oJG$fgYoLLlO3Jx((z7iU8(={RELqqcS;U+2Dr{+0wPyWxPz=Xkc6NCp$^q4xKbpj2D?sh{8OErd7w?^~KcMv(1T!GIohlJ!0'
        b'T$ASG&@|@12Zb10b<n}oJDDaJZ|J@(_s@71a(+>aJ~+hi)@7kAH0;gGr0|-AuU`%f8Ayriep<gf+Cn$u2U_E3s_C0}g>d_AOG=!6'
        b'd$eUKYkVBf=9iF-7?knzAtBgxsc65as6_Eg)<o`SUCXY@v`#L5nd+Z?<5Sdi1CbU>V)BI9v1>{4j0MRVciHN2po}TW@sC_KEmDc{'
        b'-hFjzvdL@)M}F%})?b+B2bVj8)6fJdV7>7KeV4u0NszkkQ;EoV^jto3og}kPT#%9{RP9-tJfovIV<SyFKK?&1TPzbd1tlL(liwWv'
        b'j>OXlm_~n{G!sD$;%QnijpaINZVEpsr&)<<I<J!^HvA=t_uuA<%cmM}%#evFp6t{AF~0wq!S~*$V|pu7lDD+pO1;UlHyLySI)1H_'
        b'XvBCqVmwtXaX%39(d)JE4d9J~)a3YimrWTlVqdgAo1SIZllj?1Z|eB?tjl6h-1zW8I@a4j9GtSt6_pub-7vK)-X0v-X$smV@g!ds'
        b'BB?%4?WoJ*rrHBDE??ZPVz(={M<0m4ynlDJtoO5P7Sk?^KTgCmqwO)l5tA;9+cBa(C}LZLsM8MYmB3u+Oo-VOaBU@Gvv67V%X_V&'
        b'd(Zoxh|B#Emnms{#AV+;v-WaO-9_)0JHMnG%$~0X2fRH&o6_vU%auWSN4xl6tdAin6hW)2*Sj}=F&L}X9^Cg*z&(<_$o|g;!TK5K'
        b'H_0XC&GJ+ZqN(=xL7MN28sonE^*m>&K>6r^OD{nGXG*`5$n@d=l!(#Wqu(yB`&{0S{oP>yTP!zWG*nU?Pz6<e;OE$1un><P@cw4&'
        b'(V$knHkfc6Z}Rk?7!*ON;&B80I#1G|Z2QK)h?%FT#q^t)|L`EaV-#OA2!?3#q;c`j4{qER|J-2j$q^y4Cv_|D|II%i?El4}K0(F0'
        b'Iw87$6gGxm!iyAgJ%YcCCwLiYVeGtX*I@Ty2x-+;_n+@+#_q9e;k8;TtgByz8LZKoy@QJ<s83`eA1~1g<wqBZ3CGXlk)c+|612ip'
        b'(Y?0X8`kTcA}(C}hWG9PZ?m{!t=PKOlqh<(V9`f^A0wU<k9*a0&#~F_Fb19r7xK7&J^HU|g|R}Ku!4t0@vusvU08wplFgp5L3)1G'
        b'dFCz1E1ajhZ;%>9!fc>^3@`39dxkDSkolg$c=I5w^31SH^k!mrmxV2RTIv;wEc~8g{2hZiYAPe3eN%fDMbpMXBkvpy?JE~+w+hW~'
        b'c<tD*wyi=|T9{`AEp^d}lQM5C9TX})2W?^uDAlxP?VdkkH9WP0!c>TW+EqZMG5k#o*KP3p^b*~I_Eb|oT{w7f51~vxIwOF!w*k-p'
        b'5GM5|b`DD~<wa~Z4Q^sPju8gapvMe@-)qPlOw}0X(c#tL^|OhCoC7rS9i|+{Pd(z7J)8dZ$d-uFecgY2Fh@1*qOLc5gw3^`SEZS`'
        b'qWI|XO$W^07kW0ma2(95XSYQ4Hj<|%Y@d;uAxuI`X+^|?<0ticy$_DRd5ah9rbo7XD5MIL2KvvR_!4YaJE%fJPWTYZ(=ZXsE!CJ7'
        b'OiZ4bu(2>Xv4Sm9*?8s#&6}E`-*CK4{nYpz+z}j<Jla9pOsp+5e_~Is_LH|^Zl7AaB0?wtNBEbp{KWKnFDB3Ub@3;X&?ijT8*$=O'
        b'sX_yF5;7o&Kvn9tUag1_8dtzHJHPJlOgCGh$r>MH^m?<ls83YD1iuK5brnR=8a}!N1E_%kgprzx!(_+dF??`I7z@Edh0w-_wUH0s'
        b'+)L~h?LQ?*B>uplHy+&l?j?O@d{4$vVKvd1dh`c8f4Zd4i0R3Q?la6h+|>VvO9%dNNxtC*%Yf%q^yNg+)^@+<&4@M?(DU*L^RF-U'
        b'Qg#4ERV`n*q+ZXlOW^O_LFAj6h7*@^A|aGtK<htrsrxr_8KzRva|p{Q!!k-E2KEqdVKgm)`ul%=3H)e874mYQzO+|e7U|hbr_k<8'
        b'p51Kf;58^CD-YIwVPf&q$oPg`{!Zh)6GwaP34gD#&Wy!iA+h)XpD*SgT<T4rN=72l=T1B|csOB~(e@jud4hW9Cb~d0PfAIi5NDor'
        b'sdx8FEFJ3xV-rbwQ#w38>5#O`c;S5sc!4yhoEq>(czUpq_<ONV>cBc(`U=DE!8)k}>h#aA*g(F5n6?tSyvHvg`n2)Qmteh)H^G~('
        b'3flO_OXl`VWopEYbR^ZLzG!pqB@@3C8va|x^J34JBq2sj5j`s|1+JBznoEAS<x+~zz4TK5(o1x{Z%R<%Lb3RgfB8U}UV8~bgI8k9'
        b'CI3o{dFU>6-$&D%5@IlmvXCr_ugOAKAGDTxuDNM;V19by8~OUjR+%h^Z~w{SWlzsqcxciy1-1>DuRng5dAj<tq<{hnD4>7>3Mim}'
        b'0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}'
        b'0t)<pgWVRDn*K#p6CoY<x~}<v7{n8DhR{Dt>2O==A6O5GSCNbC?}K-?u3>-qJSd+1-EczcNwc-l?QpIMrH7KOG);@Mq3t^5_Y%?o'
        b'uKy-3ptiQyg5vRSAqK+!HE-N^W#OiG-hAnn(>pqrol{0w0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FL'
        b'Kmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FL'
        b'Kmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`5cZvr2Mt4*J*&N6*U2#JJ;ND{tPA_>bo8ml74+S5NH0g%~bZEUm}(wgi}_Zo67'
        b'v^X2u$k%`|BiE3VtIv@ARgG@ZsE7Z?xzs-=eNMXZYv^ZRY=5|IW81UO&3|9J^CyQI&xLun{^!4bzC8O_)Gyi}zH2)9zYJP<!r%#q'
        b'XB0eR;F$$anX!hny9#Y>)-_~yo89ehvo*U&QH>?Tm{yZPjB^coXk@F~-Ra7mJ-fy3ZtZGFZ*;WJ#tteqm(Qk2NkL`7%HrahTCpZW'
        b'tTfE6&K3)-PN&`G6swK?z7YKNnWMgbJvSwj{5?yuOdFF(e&MhtKRS)%W4Io|0@E!oF0QW4Evl}*b4(QXR4qhzQu^FEu5PEhJ1O0u'
        b'cfs4}B8kPt_>@%^S7F-X#kq2Qp^a(!bVIr!7Za2gm6ul$m(6*v&Dos<#4b!;Syfq3MB~kiYD?#l#x}dH!|jj9P+mBsDX1u%M`#>I'
        b'Cnl1_TS;OGNt{6v%Sd7+NnAn_p&ScIw3JoWki?pz+S;<p5^$Nz&D9lvp;1-UfD5WBD$JFIHDu4^u)IgqVR?_j^Ef<Sc%Fdgr|>)l'
        b'&mMRV!gCm&<M6x&&l~XQ4aST)nRBzUbF2-GO}6Gxrk+H!`Go}}|C0jN$J+oW7Lxonz!z6!nRIt%nX<vZ0<aeF?*M<8Px7N7Ui^<N'
        b')23pQUs}j$L*Wg0Vz~QOc;w+e8xXDwCaISlJ@l=rR|WddtLxPP{!`0eoqurw$=^{*@^w&`6@XuX`V?E;*0x-+tOIzo)9SW2wAsWa'
        b'ryT}VOd*_SbHz@_DhP0Nh%Q@ObDG=ca*HXJs+v@>*=ldIHO0eFE;3iw8tB_d-x>5h2g|=h8<w{io;%@bgeP}LSl*@Zu)N4oVR_Tw'
        b'F~Cy<&r*2W;hFPxSl+oO!t&;mVw<f=Y<09Xk%BdiP&1d?>U2YgI~wm6n`~`1w~f@e9i3v6-DQQElcIK;v&GiYxCT->I*G;UXs}^q'
        b'qobq4*61b`4!6SzmF{Yj-K(t54tqxnDYv)V-7e7q4R_j`AX^B80voU>o)5;koz{D8Z7hH+5!(auTN>nB7UT;`DH?;*f`3_vpB3oC'
        b'fkoFk9BnR}+ii0OI0F+@SV|zbCL4|wwt0!zhHVqu?Hz$`$ld3&t_F9jqus_4t)ZW4X%N-Y0IH>oYN<@MEP!fR5Y@5(s%4C7nM_sF'
        b'Y42!)&W5*bwa?et1&t%-uGJ7O>Sc#Pb{J(xhU}OlJ2GX*T-lK&JF;a*jxR%h*1o(AzRV52+zr0$4Zi#hz5)!s5)8f~48AgqzA}vd'
        b'`uoZ-vNEh4);33rzp;M5A;fPC@rTmS3Gru!_~(ZBvtZa=Zd)f=Vq|zJN8G!NBko-SGs=l+5iMnJ=2^zx%u@qtJApN+?2vsf(bhp{'
        b'>Jr(p%onm$c9~f@W}1!JAL{2Va{xD)88?}OCLEjG1vNg$5}#|S&$Z0ws>tv==lGqOe&<}jGt0-Kjt-v_stS|M9uQ(#T;X#Y1CtuB'
        b'lh{a;SJ+){QrzZnG|>@qbh$Y%pv&NM8GWt{pKFfKmFaWM^|`Wqu56zx$DeaRA^uVf{$dRNat!{04E~Y~{-O;2vJC#h4F1xL{?d#A'
        b'ZSt2EJRkg>5D;Jp4KRiVT$9I~(16U)fVrUoS){zEP^_l!68g@k@5S_OZF1UNY}pC+LhTA1Ah{dGY8!}W*^}>Zxb>u>tfq=oRMnJ`'
        b'8cUg2P`;4i8a>Abj*T2=06$n=t;otXg<_-C*%at(f)x-%JSKJ0vd~pleFvzi1!7IXLWT>?WT9<Mr?m;@6<xS6lsl`JklH1rx@Jyx'
        b'rdYjXcI}b?=Dee*Of=JXK7I2A1)WS(*MTw6Wo@G?y|{#-r3@`&s3L>oIUHwlJeT7vuA|sShvlLE@>9?cP;c1}SOa)Xbyyzi;xB?9'
        b'_3>8$qfY(@z^IpB02~4ME5K;SsKdhYq5ww&9t~IojJkUo;IV*j2RsgNA>e4h)qqjIss}s?a0lSYfWHfP3gGVpo(lNC0mote08az_'
        b'9AH$>Ujcjz;CBF{5%Mu$5$gju9_<Lwa}uyVfM)={8E_)j3vd$Zbbylq=K`JyxEOE>;0nO0fa?IG-O&IT^}<fTs0VffP6NCaFe>^R'
        b'0h<9o3K$j4U4RP!9{^kk_<6uZfL{h&jQSwp62QL)TnhM4fXe{?9q<Cc7XdE>d>L>#_ABUR6=;$Gt^^zlxC+|=*n+kZ;5*Px0bGs!'
        b'47dhxDd1Y{XTXa9uK-*JxEb(bY!BcifbT>75AXwkmtnsHUXJ|^cm?2}1HKdRF9H7t;MW1K#CiipMfg*|R=^{G8vu`u09_OCO@NyK'
        b'PXlZNoCvrX`yFr#;0(YWfNulr0Bi=_iS-7258z6`PQZ%*yU>mTycWj;@B>(Xz~4h18}K^7TLC`^cs=0n1Kt9-74Tz#-GH9}+z0q6'
        b'!0CVw0-lZS0;~u88sPD$_XEBU@Sg$yC*ThOcLV+$@OJ<Y1O6`Br;%ZK_oIyf81?)(z#hOe0r#Ta4R{mad4M-#y8v$iybSPG90$NZ'
        b'1ndI*Bft*={xRSm0e%Ge3Gg<+UclP{?*{xR;6s4_3+oN|F~BDQKaO?`;Qt2v9^jt<{u^K~@)O{Gz*hhd;Jk<en+)(cz&ij>0lX7%'
        b'65yYr{R;R=92da5a9#j@3T+9%yOECo;|4_w;5~qyfcFCa4&a{y?gP9J#{=+w<Ricb0Ph2Q5b#mJPh&p=J_PuEz`p?e1>k3}ejtyY'
        b'Mg9SN7;u6rJnuQc$>4t;`3LX|*uQ{Z1e^`{2=YDPU*h}){1V{*0DKhi-GGk)UJdv-))Vl{fO`SI0(b-9Um?E$K7suX_}7330H4Hu'
        b'2mC7Frvbl){SNpyfKLNH1^6w%r;%R(zmD@5@NWTs2KWr%tANp#j1a)q1w0z?n}FY46_)oqoG;-2J<bonf57<+_$?d<z;EL?0RAK3'
        b'BEaup`vAWSxEAnxI4=O7!+8PtPk`?N{AU~&z~^y(1O5xP7jUJ+4N9G(tEE+JwOKpGX3(oD>uSV?uI6T&GoI9dO#|kaOI+o&yKS<K'
        b'2^KCc6lygYuU4xP)oS%zwOUiER%@53)nRRFb@+GH>QS52>WBfgI`WWO9d$yj9-XYwkPeMT^{hrq*O`^~THCs89IbTP++EHNTNA0M'
        b'DFLavBs(v9B3StmL?9@{Q*`<{roz&4OD#d!sHZt-&^8}Muv5wXWE5TFMYlr)8xv{`dCyENo!LDzamh>!?dqTwWP!B{m(*Nw5%oif'
        b'MO3S8B8AL!1q-*;23BpM!{OvkW|9(1OS@Rq(L|siP(YzyVAZEet}7tO#q>y0(`K`EqCFdI35#hWn9o+HPIR~0I+(5yROeDhJ7&{J'
        b't!$_5o-R-Vn!x-7m4*jW(;I1=HfL9dc$cFAiihEXGHej+XcOCP9WCxw(b3$DxkJ^UU3OP1_HKZ2`|oOU-7@9abSSeOY+caO)<Aey'
        b'W2@NNW_6>#N$mW3N@hzlW`fe4YeZ{{)!qRSHYadkyJ&?RFv%)Av?8(AvRG`kJ6-O0P6?52rWlD<K=(qiP3hOKZl}X#rwNg>X*JWJ'
        b'SJDGFZ_1`HeTTXyFrA0)(@kJ{4}xO?(|r&;6PW&kuzmv5fe^M#V0sY3;}e)Jgs^)8(}xfaPGC9_!mlPUy$Ip02~3Bf+eH(Yo`f)N'
        b'BGZ)+k|r{J388Qz)0q(3Co;VWVf#e3W+5B~_XO_#9NZK6Ue@TF!t!pC_p!ho%iRxDh2`DM-K95S8=Hvtw<Nz4p1$Au_sUfKt>#!0'
        b'uun_)Uad;S_G=N3@)ODETfsO=ry|juetO*WTi_pkmER093?2(S)i<O5vXm?%=IdoM|MaQyc~NgYahqejCimuN@5tWst0(6k$qLW>'
        b'(Mxq1t4{sQu(C5!Fa2$Kx~0w9(E-*nlYyekejhNR)ddrzsjCsCU*dv!gqT!gqDt7NoM=clG>gk;Ce9Rr$!5|$(wUUuT5WBebe9(d'
        b'S8igWm^edBED;mS#KcN5arHcqeBfF=ug%_J6CqcIYsxKRVu6^rL`*Cd6Z6IIit*xnvC-{pOIwYZrIF=eTT~X77v&O|!-Q_W=8}ZO'
        b'v;s$yEkTzca;c5ZMI9ix0>Z>Xo2$`j@5DKgfZM*5D3ZrU(&UkaR=3r?rqf0p*pPOsJMuaiL{`}0v95-E#zdt7h-5j`ESJ7(YR$Dp'
        b'xrJ4WYP$pc=1_lGWjE>W?k4jpXPdF7Xln|p3ZZe!>2@-6JMM-^o73rV=0aIxqN;5TV8r?4V>;1+J1B^(=vdKFSp{W?X0a7bG$!F3'
        b'%_#4vG;%uH+F*q3E+3I-ZN@#k##U=b3pUo>3Xv|>@^mOTk%+(v*41`byVZ3!^+2H@MLU?=?ryf*+M05MeB!EB5YBQo7%b}fR*H+('
        b'1uEudBxM$`Ua9#?a61TF1vRndq6?M<hOMgsV<!M3uq}8PeI1D;_71nL#pWc<Z4RrOV8zI4xe~-_ZL&KWy4-F@hl|)d@0~+BtuEIp'
        b'hqK9-O-XgtA`6aQRdsDH$*+ZBLDLYB&O)-YNM%t~MGY~eXA(U;#bDG-`z7dfAU~(P2)Y~KfPu$>T@H(RE-CA1c0i36v;AFg7141N'
        b'NujNw3;oM2)%j3tX;lS|dTn_X*1=qD2Chc7Aj?ZK4G>g9a*P<COS<Rk^g4YvrmdzF)h6h_k}P<#;W6s*Wq?->eW5o8BXj2BD+gcM'
        b'kY523<rv{L7bE6ix;Yp-Cj(wsCcGiA0w2h!0+Lo_pl2?=pr{H+T|tv%Vti%>z96q!A{G;|hTN(nX*y!AEtqFuNUtNs<>s1FQVh)_'
        b'MMakCstU5auBbW}g-AMCUS)yyEjKTzfp=xmV)PbOE~==}Ro4>iARVc!0-}6yP*gLISPFEcx>!f5YIG#OP)CXYS6D!cDmT}bVmeD1'
        b'Bq++Ss;bqI8i=eZf>hPDKvrO`)RE=IWz`jn&DBM@{FH%;teUctN^?1_1}KCzwN=&T5*(i5>Y^gCqNt*(dMWq{tIM$R#6&7e?~}bE'
        b'JT+ximA-fpngM>yEWgTJT?n|syaX~WvWV5lEkrE6kCtj)v_ve!@#idASX5I0*(aFWte_X5tipM5FLc(eDAibS1#b7W$T9jfe@uw9'
        b'OQ4*0O*Sm_I=QfjkW5NJsDmoeX>WApf){dYZwIBvg>G42rV^1$G#KvMqPn8WT5NuKSw$H-a!W~WIb(SY<^sK_5~UroG>lFzsdUKN'
        b'Buc0jy9;C!$U4llq6!8C#;lUge&#JUFDl2$QDJeo04-+7TuomXT#{>GNKd*8(On3xJW_`0YIRo!$u)xZiPCF<qXqR)8=<|J%MjCr'
        b'397}pOuMDW9;7?J8A>ScfLCEHRHnPQ24C=4Fl=!_6@6o1)xB63cxoEqRSFN**Mb-)a(7t=d!<3$iWkf5NV*dXptiR|yU&p7(wf5Z'
        b'+M=rB3h@q6w190;9;wQ&ho|!<Retw$RsNo_s{FSnfScgn_3ZX`(%wEBx2gfTY>oe6Bu%!K02fBll;9z=I1qc&YB5i&TnW;wx^|Ie'
        b'WqDa;5t-c%YAQWHp3SAXE4>ktih1)OX#w<1lf479(V8`oVY`c5b5=`qD9>bCFnX*_D;tq)WfLs5{s?MrT{ni3Q1!N}b0sPap+rG('
        b'xYy5)Z)BSQxVzon=yX8)9l*5dD>`5ix3_n-gDul(gAhDh#6<~|>_(Uo!2hVx!!igOfxXe%*0u)opvx96O}L&KKn*dbXQtzdTifa@'
        b'sudPAP{A8)vg#x@J00zml-o@rwf!)QOk5;8aBWMcM-GrV*b=tYjd<*6?S#s#wu2U8gVGIi^y1y6_obt83Tv_GYIT6Fk4KYu5NTb*'
        b'azb0HlP=*7sE=E0TGL^LhO^Zij}vX6*Vy=RCAHi5u}HdDM=NE_%oOhiCU>#Z4EeYORE@F@JmO<ZH?6D7-qK-hbBQU`8iDpZR;30f'
        b'^X=q*gS5ON^4TvdR;EiAD;zF2k8_D#E)Wg=oaDqzoxxVwF=H1LobFeL%9^iJ4s;ACNn9auS=(*F1p`+=*DpanfHFfm0req%3}o-<'
        b'>~i}m8<dKfbb$#{T+no8earfo3r}Bg%O6u&?*$Xl+F)<9yVpSd7vs3rS6eFliMe<Tu4_HkvJr(9@(wU>MFuM76>~70cUFyFbb)mV'
        b'sa&ERmBMD4vPQgJ42kKGOP*P6ZKoW?3Y!^N3f4pH>ZEy4cavikOcFbEBc`&pHFlwK%x6GiM$R0XG%+(H2erRW8?9B_nt#VN)QZIc'
        b'qO+Huv*Ccym=>In(B#!NSHN)Bq7Lih1F)&v+Hg+7q-wK6YN#xzoXkjuxq`X-6VvL-ifdv9%sHs49TZ9s6LdiY&OrGDB#mudO)NW*'
        b'K<+MFu{s^t5-L8LxmTq6bcdTw(pI|H0d)nIgat@+bv1BeyKlaU^l)(vR@v83m%Y8SP39>7Za_ezEmo%sjW;)n5xL2<V3)1a>SU6H'
        b'Df?_L1XP*UnDRUH05t`mKbf>?g*n!2g$c-)CXt==<8V3YE*cCAj7=BiF&G`F6inH2dS`>lIu}e+%2>!DJXfqiiIEmtk|A21jhJmC'
        b'cDc2&u?w8gdMmaa>Vs-LbUHPK(#3q+Dwwor;lPNk5y2{fma>Ad&un19HoC=5wyk3AXtc@m4LPE*RqR50kBtS}fTM+Wtnu%gV5O)m'
        b'X1Tgst#k}Kz|ykHoZ(`T!OY9&==BAjJWPT2M|5J9%u*=4bz%{{P=Xa;+dlm22y!?`ZXf^g0(3#*0_(^HC|lQH=tJx007IV*b~~t6'
        b'-$XL|4x4pA-UZf{vk@Dx%I;$OUMRb+pAFwzyl&6H`rHPx1LS}mHxYqhEWptnZaZCUWkV5DQK=%Q!%4-P+-CbGJxZ&{JN19F0|T4E'
        b'1pfbFBV56)2r7V0Z@&J7<c~|oH!A^BhLj=C0GFfL&04_)xr=T%qK0H`Y{k78HoKWrr^*I3D(G}!stK%wVl~@4aLLk)(AB~xz1rJt'
        b'Fk`8_X|=YwU0f{COi^mALJ1j|vsLa{x(ZRv%V}?Ep{l=FhT_#}he=H@7Evk1%Eg2*YhCo-7|+O`1!!bo+cfzb-x{#Z9MFcqqHR<c'
        b'#MOkWan>%k1C%hX1>#+gCMt5-!dxV;!SuQo)d?E8X%x63>w;3q)qpNQQO*PvbX&t3F|jm{DHilz)$P8_0*W-Zq0$4PUBRoqj@254'
        b'6s=`Q&G~Y|q8K%V(jrk&_}YT&tN6V%5hogJ87@gytO}K$jIVs#>HI>RSkE{19UUT9(S5s4_384izsm;FA3L6A=^H<;kyDv`Z-8Eq'
        b'js_>|NZeI|(pUya(P3+`hNNbf_^33;q)=fxagZ~Dc@C=$^26DVlK`g&wAIS@+i^j1Q&pwLX1m*$8?>bHZpg0LPWd_{L#}O8A=*Y)'
        b'LzW{nxf9F;TZl5x^!NswdzB4_nWk`|l@Q3ZvSRP+r6yYg$mB+PGJ)%-8@t|(i=MpDvuQ;8+22l(-K+=f?sSn4163ICd;%qhZxVIP'
        b'bh8r^oJS>D8MtHymy?3S2BM==Yydm$ZhAuGguK83Ye0Z8MjPm7WMmaoJW(dJ;VA|zvmK(5_7_`sagP#OhZ<HF?mj?dkQqlRfD6!y'
        b'lh-KFDRCa~iN!Bdf)GbGm(z5%b+y<#keHi*|2xFjG$Ju0Q%u2?5U(53+NaVP*9x+f3lcsxS`e`XvDx0zh5N6d-KUdsE9!12;Btc$'
        b'suII&<LnIId}PB!CpidKZuSMXfJp?Z6hk%3tymVzmCjab${<^nWa-3`Y#r_oG9@f0D?RY?7^uN8Q}GBdI2f%4K0F;LyBblyOlj(Z'
        b')swPlYH)I2e|*E_*46($xvY(^YPAE8$~G+RlmOY|w}_E-YkWpiBXow7v7`%&0FJ)b(bmO;g}hQEbfE6omLTs4P$AYV&ew_Yw70&C'
        b'eT?$}3#KJ?;^7-4NlcSX2b>l#YN$h?`N`|m#7-XJwT5aWV25CsY=lrl(ap_RXqpx3PETURyBsZkE`ap%dcDfwyxY}jg_%fCUzq4e'
        b'Ysl9asM_5=5u%eNus>X0l(3%)ZOt@O+O;%-YQKDu;zli}V~ct^sqAWRz)QeBS%sVIHZ<G$6f@8beC9M}rxP<@Ug-r~7-)LXDGSBW'
        b'NN)DsAQn^?=M5v99bHa$t54dZD1u&WVJFr$X1KMZsA{*-fkbYA26VYGHLkMXICU}FN8dR00vJl4{A9Kr)ec+%H4I6`7Zcx_PB}Y0'
        b'@V0VW8eSTtC(&(PxJl)s#hSFImvuBcZODyizVfJRGnmbZam5mweM=|J0(TA5i6xM0U{MEwMpd--b{(GP$ZXl@+ZYs=r@`p2WO}7e'
        b')ZgjPgPN7{YRdBB>z1!U0VT8h20q!$#yV(M4OUY(PT3ZxwH>B9ZrQYSAPJqKc4%lWw%rM80$yKq(5|PdHWX7<SYE`9XULaIOW%;%'
        b'+>Pm?Syrc6b^)hpxa&uAqZ2qiYM~7VQZ}|&mY_#Cz@&ik9ZXVz;Yo$5oD5c7zXXE*$1G5A16xx~20Qz1D7LAKN{43ow+Y;GN9C&v'
        b'*q-iQ_#%<(Q83wMZJTP)tc$HsbQ?b*ghJYUBQE!^Tol?Q%tmgS4Q*sfjvV;yM3T&It~DKvqNS{m3VeEm2V4MYnTbzonGFI}<C2+e'
        b'vEaren@94z`nO4&AZMG+uPPw3rHhMjV*$pjL=OR-cE;q`(T!k3I;~92TqN(jaO0&D&&c`iDvluEsAc<6@W5)xlo?P^SPlHevdO}#'
        b'>Yw>IR9s{-g)3bwlvPl=zhH0j^{Kx<QPoc4CLEU68mLD5a)-jJ*i{%=rF6+t27hZ~>u@1g^6~N4fNqlT9T<Dyh{42Sa?S0)E}|Ny'
        b'OJ1T;m29%zYiIg0Z5N+~?R2A%YF1nU(g!TkY!?hWlN+G{nKShjh8d**ZHHeEqpGA!Oi9ehG3waXBHA#S89Aw(&kc0r(`mK4s2;@j'
        b'3GB^$BOWzvcF4_Z1fg<K^7ST+aX`n*Lc5Y`1U@xNmJF0Zs5!-N1mRU1YNB-5R{6J-WQ&Wcjuj#4a~T)XBI#Wwroj2AbyR7SOT?Da'
        b'>p}AE9$Mt}@)b>DNoG!Z#=p-$;0gehev~ZuBGI*tT=b19W%eyu|8MGLy*7VZZXw;lk*!a8(~gcb7M0=?->_ghKm?`wwoLJg7g*!g'
        b'#=B*`3|RpTDLdVi@$C{a4)ym(!u8saKzAa5yJ=d8_i0-?-Wq5_Nrv8^Z`1WE?iVGp;0;nB{GA{Vguh;2X8{M+7;Hip9lZcM*w<bB'
        b'THQA{g|CzIzc+|2bkzq2amvDpT@_&_C%t<2?=z9rgph%%n48OO0&aoH!o=?4BkpoAWjE-m4Cf9pg*M1-?@Xn;Q}TfkUU~7?sA8_X'
        b'9_s8&u7wmt_pVrJoVEDR(B#Te)-90v9ofZ=+!0XqfGLAp=z*LA0yu=n0(Q9q_O$%FSX6K2M+(sQR2HGEDapuAp97278h+v+OFC58'
        b'f|#BZqEO&lNAv`gZ6WxrH!urmG_Le)1-ubayL>3?(@t-Yj?aXEbZj{Ri4OVCcFKBUGv0KOS(mQb9cf_e0k=?P+u_71kWyJ!gPYYh'
        b'stLN~p2Ev-4$z&}=%{|;>;x`k%bN?w%Rwi!6V!!!>4y4h|D7pUfC-KhhU&pBIAiGVw*AVb%olEl|16ENs>|AJ1B;hwl#mx{6iqm@'
        b'L)1Jp#IDIz)+gy*S#~G%|3a?U)-@g0O(52%XW~h?-bI&k-&RCdCp!pBkoATHvAL_Gk?p?It#-FOkLZaZ<h#mhcl+#|YZr09?nr+J'
        b'#7>6zu414KN`Eu!^6ei6U2Mdo4d@EIgUAF6I<R<t2o`u~c726KR;uiHkk<uv9qqD3wFQuMGo@fxuEi8oSGXKcT#|a73wKoUcC+nM'
        b'zQraMrO~4bw0M~~Amx}@fHCD_*DToWVHcIi_9kZ4`Ht=W&DhaXxc~p77qV@`%c2)1TKyX{R<|28UZn63X?am$4O8o#_D<1o<0zy5'
        b'IyE&d>575<z|CuilNshE#_T|e3yMtciVnOv2N851oNt5cX(+r2YB7*q7fdYq*KdLBcg@WJz6B9<G2q4%mF5#VB<Z9;KJvE)S%8j?'
        b'pbd99V|H%MFF5ea0gyM_T%lVF?219Ui1$_aIhX%}i?s<>mG2tc`O;#C^6QK3tEowd%W=KTU%n7b$d1i98&Ko2neBVQl0k1Gv~&S8'
        b'FuMpstWG*6xPv;g+J=25f*t1sy#-jFAHdJV9XZ;YzJmObtd({!V4QZUjmq>?3*x1*BEH33$9yU*C9_fSvfgm&2c!V)uuHZY1Gcy^'
        b'e-gMy%_8kSn}tx*RgRpSnVFFpNKbpy%|iSaA$Ta`vCt7_W18YhmE!~Mq`2g;fNLl&;1*cR8u4ZZDe+&PxVAicuq&Vb(sNT6-<{C?'
        b'`}-(5`B1aXx33MerjsAE>i8~)lie=CO^Sf42y$T-S+5B=o%BmWT|U37j@v7`a*XVtV!@@O3U4yEJ1zWnhE2EF;S3U`Ofk^Ohg&Y4'
        b'eB>^taQVu>?Fy*K;({tZ3v_{(Ep+VSrSB$(F6dr|+}MEIAJ{uobxCtO(pnt4qSbCZZEhk9xRmu<(_{vMK3%WZ6EohDkS%1;bJ^vR'
        b'4tlM@<{NDJs6ChkWNE|r#TV=o`AkSr4ZO?uMT^k9LSlnhEhH|8<!S;>o%!$SOHqUd2XW@A@t^hjxCm!AQ^zQ?2K``2_FTijJe=AG'
        b'HveX(uSbIqAOUfE#upxZ#>QuGaAc=!vB=6OJtPY~jKj{6Pr$B!YDHj5UH?dmRM123X52nxTT^^1Lgzm+()rJMu78HZ+kE|#9Ku!g'
        b'>mS@)|9r;(MFo(Mcx6yN{15(sM(7EPm}0S1r^=h0ZMGJ?=Tlwl+eN(2S%+`4m<={(l0uvOD=1J!>5$vq@<fx*Cw%*uoQs3DuE`SJ'
        b'Qr$9nG}(y-F&MMiAp)PKfhQBe5rL-?!7%|R5+Qj7oJRPn;@ju;vr1?TWl1@dZIY8T&cSI0J;Jpc>ep_TlbQhiUly_SO0zuwiv3&4'
        b'Oy3~ELY!|0V+x&|z09h(z+bcB&8!L?ZieBCfr~Zg@D$uU?R3+5%`&f;lS+ymPI_Dc96(h_`qMW$l5%x}wvW?L1r81?yG~f)b;9JW'
        b'=Q6hAOws~3X#IQ10m66244$YxU?-UeSp)WsLsIdt;;_IbpE=8x9+Jl7I*cMu(Ru@s6%>1oyt?roExoNSZ^KaWz-341R-x`jdxyHO'
        b'*}v2A)0K+3LFI(*Pz6O^)3n;4jiQj2g=TB>3*2ksWhS}d{*Uh3eHC5E1_-w9`nwJ{-m|#zE`@LY;5GybOZ+thUAhC7GXK|H`1(*F'
        b'uheotAwS}he`Oo;V?Ac@5(Cu`y0Gb7FJRg)VZZqewLY1pN$5!x?T`*`Q{77iHvX*aMz$xx!8hpeZKUrEkjl(@ldFiIB;nQ?@05Tb'
        b'qZ~v#pD*hz4!XY!0@&9fxT?|)D5m>0-0+o$nJX}UL(3KXO)VZM3pbv;{W?j4ejxlcRDlTy`{A`LC=1Yj=O<nAZQf=-2jWjD+Z-;p'
        b'j-_L>-{q5nz#geQitp~pQk#bc9n1MXZNwFB)<>Bz`ZZk*PFOKe753@SAk6SeOEW#3gn`E`?24RhR8M(Ym&}ebO`z4MyOEVfKlEk2'
        b'4!dEv&pIL**>m)IoxzZ41Z2$6qi@b!eKw%XthvClx*VecFw_AUuEYj>4S5s<-xl@HFnMywOcEs31Em39*yR;OULa=&EP{Bz-omU8'
        b'+Mm9DWu`GT_bklZgM}P51}cTgQihf>WM+uN3X%P;Iwzj}ruslU`#tsB@$9$M+64AH>Sq$zZ>Zl(V84@=64-C2$0oAhO7Bf%zmtA4'
        b'iTy_UY7+Z>v?H1QHu^Wo?03<3&t$)e{_mOW_s|z+vfo1QNnyW(9+S#`1AR{_`~CCTRQB8Fj#=z?&tW?D-I=>}?7K71>DYH?!qeDy'
        b'XR6cKcW0hSW8a<mD2;t@rZ}B_Z)R;e``*m>+3b5WkIZJ@oB8={_Pv>Nv)T7%1U>uS%x!x1y_tLT?0YlY^z3^xX$JPa8JmH9Z)UrJ'
        b'eQ)Npfqidg#K68cGu6nxTasgB-z}*FjNhts1ICYg4gkiF{+$7wiFAPR3!jM@VR=~`XX9_Z0q5Xv*#YMQegW`pI1YgG@Oz_k!t&+;'
        b'wgbK$zYmg$-vfktX0q?y+?C0`ce5pveJ=)oPrsbw6&&ODVFokV_g|*ZW#4~UFqeJr<sQJR0snX|`%cP-bJ=%AY+3AkAUGbs<l|8b'
        b'47D4=7Xf}cJ1nmbaK>$6d5ZzJ16~676~IdY-<${a0lWh6a=@?6gZcoL0N)9C=Ivp5J%FnKuLisYa3A2W0IvsJK0hpP1K<I`4*{NI'
        b'3d{RG;5z{S1@Icc?*o1w@CSf@2l#J*XPJRtfZ_iG@F>8a1D*spF(3E}@O;2i051c)0q_C9KLLCOa6jOG0p0;PxgacW7vM_3M*#m6'
        b'@JoPgg<*MT0RI9o&NJk#Q{aBDkj*1cX;|KicfC4a{w@BQg{u73%T+<Y-$$B{ApPY+Hn*H*EU)k)HaAynVDvJmIgL=n(rH6}T#w}}'
        b'F{|<iE&g&eoaUBqL8Ij~bG`*l7%!{#ThN5_Pr9~p8tjw1bpAFY&12=N{OD>`zOI7NjpB6OoQ7PdocHpBX(D)g9t<dFFx6iU)_X|^'
        b'O(ZX82dBZlKO9gd(wtfxOcTZP9#`xyC#g7uhL<CUjppelmB9R*&Uok65<d<0WA^%BJ`gy~+^?a@3!xdqX$nhj+;7^7;JS_F?Os&k'
        b'Z%@Z8f4(>tyOsp^!8o4R-2pVW2hd=CABWT}n)h{Y08QDf;PF`<P>za!0~YhzeuKIpO<M@>jOXFcmRz4lHP_+M3B14GEV(g{CWe$V'
        b'k>~Z<*YvfeAh@q@;xy_~Kfm2n>ZixP9t@$0<@{p`pjmrs@c1My45qo6(^Qmx^LaXn)7XHff%DsU0_uh|FD?j{Z<9IAx^F=<h12|Z'
        b'sb40#%Yym(cOf!yDyMm&^!jswwr6Q@IdOa(-@O41_M<6;N2hTaa<Md6#?x=VjAFXgl90OH!ufg_(v2^>{yZg|M&_OAoF=yH#x&Xx'
        b'8j-h0$NLKT==QSUJ~&kt%m?wjoaK=2WE?B!p0eORhzKbsfzzypbl>N7>*0N{Jtmy?fe=D7gVX%@YiOcFXc9Tip0A;q7($c8%Q{~6'
        b'&F6M9FXvrOgM8!)>4VSL`^&*Tp2_=KD!cyN#&RAg4DRa`E=wmbxG_y_2u&)N*}4V(xt+TpWGxAynZ;@DUEt?~wF`pV(-p#_xAJzc'
        b'=jo#OoWpO5JhFiC^&dlMbe!hD7JT!*PUAF(z6DJ>r+NKb(9GsEfByzFGVf%|>*GSdJh;C!xZfTK>4O|jGj*X~zJ=2CgwW)28bd%i'
        b'CUBQ7^pElC5SrUKjpb{~=?<aE<2>51@W%XhF@$&K@p9Y?{p;MAkafE+WX|2r)AfB#IpsycYvX)Q^P_-ro?IBr*KI|?bu;mFvE?@|'
        b'M_(LFW9IAj%yNG@({2sc4{D2p>$Z%qnOU3$`#LRTUHBpIgXm^Pvz*f`{2H2VAv7yE&C0K#c`SrxC8u$H4b6@ankGJ1Hv!FKpzk8h'
        b'uJYh@VN<}`i2c>UX?_9e_Hmlf^)!@bHK#cVG&{c`O)sZ;7igaShBUi5&Bb#6{25gdmN&M7eLG(hK!an7G>16N_zHh}0%g4FIyArJ'
        b'H2QBrQ_H`#R#|cFnkDnw;SxU$hN1n8c80yeFR$;b2&Q>pK`@WjahkIg{yz9lNI4%C2bZ&$(|lTSeO(NBr*?ht++M<IMpxdLW=ROm'
        b'QcjcdH8d+iXqIuB(n|k4T~Qg_9&Jf*AK*R$%Js)9gZui;Uxek!`oYN%S+#=GJY9KXo$pKt&7GX)^w-dw3ZcQh3~a;SD{m~Tgb-PU'
        b'`yQyfNCAED&rtg`qz`b91m*SUs<6B|wO=2_?|&Vd%GT|T8-nHcdQKB}9U57O-4sHzf%El^$_eFbq<M(bq*eL(ddXcOvUfqSJ@<Xy'
        b'Z}Y1Bx)|<<?1M6Ds#x6?1nA_L_Ai`f3B<oWo!JXGPmu?Z2FvLVu(#3w0jFuJy7Bn93xfOl0_V~7UqiDa#5VgIFXyLK{xSV!RWR?g'
        b'g{<4SPlf$<=4<**7a|XEPYdnZ^Hst68@k_ol;OKVcyuzS`QmG6?hc{By)vrHTW-vwogq9rmA5C(^38b%_u??`^nh|+NDb!6_K>>a'
        b'z8&UOVEN`cAMWvmea&3BUfur2`=IVyl=F8^<NOvhA99-Se+!zAIL)qaL9>JR_3?ndK4S@%y}Lqmv0c2Jd3X5doXk7bcd&W-w-CO5'
        b'k(X0<hrb;A9U<iu2J_AlPV@ac{JQbucLeW;M2FN3_hr!rdijnU%Yz*u^56`odG`+gocrjG;I%$FWX{PjzB(-L;zAaN>2412V|}Mr'
        b'2e<Kw3H~y0d}db%>pM9Ce&k1UwO`l6_Lc?2qdck$@MBvW0{p0x*aQ41_wNbtqdoe)06&iD!vTJ@!G9Fs$3EH-&_1*q_jCWPvd$Rb'
        b'M|<zZ06*GtF9-P1PJ4~}Z+>J*6ZO`NJjZy=ZKqG2n#W3P3iwX#Nl@oY3)piJ-1h;#Qb4>y3531O(tsb*_55bX!vFX2{!tx0I&?L-'
        b'uaFrnj}`gDPIA6EdcQyHo4Cn1x_M2!XabpVPfdbOx#){ljq?db;yudin9tLrHUhY3{<r_yFVbKh*zcn03N1>jxh7e_hlHmCOKU>*'
        b'5!GK)LPUoue<C~|N}Bxh@LYsv5T3v^HAU5B=5n#7wz|k%A({(n%j$|qZBcn;QEf=z;-dVTs)B{rgy)wpDyprjsx1u(w>a(Xc)*Mw'
        b'R`ttD{Cj3i@N~n2emCIr55wFCJZVHjpD)3`5&RFpgSd@9823X?cU{0gB5)i!>;dSdh*9{54M4DrWo1KWX}|B6E&Ri4A)laQr})Iy'
        b'(baCFcaZVse1n}{=ywtR-Q5)bH+EA4eh(~XY3*8VZ?j{|JO3AZZv)t5b@q*)Bu!gN)glE^QE!k!tEIFBX=Q;XX;PZekJzMqC@xLg'
        b'lxDU`Y*HwWX<?|SxRuUL{Mamr8{71eIo+7z#vGe;>c*Tpwz)^<WOJL_(4iur{r|3W&Yk<tM+<Iy_P)>mHE{KJzQ50PpL5^mT$g$X'
        b'l@1P2RB?4yjZn-_yY+^GQsRgd)<Q=H*o-D`wK7{357*Y))58xe2fG6#6q9@xT3nvS%K4>bB$g~dK8p~6jwd9Cj)hmn)rv`ZN%A10'
        b'>J?59o+J-B7S@*)sR49X)g#(DNH(JuS@N?OI>8qF&My_RR)45o4X6`|!vlGm;3GuHM3ba7khnDw#-TOEsDYY1-i4QlwCH%k9FZnT'
        b'35(yRQ-jUWg2iu=rv#d*4<ts1yk@_OZc~gF?c#WK)bk!({1Kf|NGNJbIPzgOL+K`2(TMJ-G5a`);<l`!DpO0+NlAG&S{-#Vm12=q'
        b'j31ZO-{DTYaCSz{jEfgqLW{I^74kRezz7MA<JYVe1Yk1~LaBFG$dSiDLNG71a0><WN9p*6qB?LvJ@SGS0wVYfEj3-|$eaA+zc6i%'
        b'?SYs-DCGj`O2I}=inKO5(xw$fVsSaQDGAE+HC(=uIA*I@_^}^enLuAK#^hxmwFhdKv)UD`_DWXk@i2KXCi!}`WGq}_x>lf0O~5W{'
        b'&iyRhx+p0O6;k>zDM8nx<5H^Z++wA(x7$xgF#YZPB$FDpHf><_c)b?9&W(Wl+E`o?0rS>1F>y0OyAj%>YGGhr_cA6<(s6&T86nPG'
        b'`Qa@k7!rcj#kg}Vv<OirD!Xd!4R*EjKvD(@b6u*Y5RgaY(<H?(i!?4S#7uSZgG~*k_^+ESoVVygDDW@C|FMFUF{e$}X8d4k6mE-C'
        b'9E%kajxS}$)Ab5nON%pMlnLTG7mwmKRtj=puIdT*Mxv=6qy=_y8s}3di6E+EM=g}|k~G!R7gZGyC-PQBpfeJqo-iK8J)J^&^cN}o'
        b'RvD{vE>*j$i%tM0$_7*dt1<8p%2m&j9(q#pM37DbJD8^le?3yjH;MLUj%5vtn;h{cm29z&F8?aQE$HIgsvbW^a_M-pWye<xc3Mu('
        b'jG8SAKrQ!+HGu`@Z`GMCG5FJ7y%~1W>H7ND#J==V*zds}_O+eD?u{WWL#Ab)w1;4ykMv(3GT3QdmiJYI{nyxk$8`2th`(~1W<Pn<'
        b'Y}ve1yqkFd@tbnZmOCCc*l9VsANF@HFk4<m{<MB+LHJ+7?ZDTxHO#MJ->0+x7WUmb`|N|LgU)^k{tuQL?ED=K%nzYF0}qJu8+*-`'
        b'8qmfEgnuK<J)k~mUkCFx(B7}e^1}RW(3A&+{c)II0Od;i!CpGsW43r@`}_&^!qsNW(H$baOJQyR4Zu!&uNP3iuOhrf`ZvLE6{vWJ'
        b'DE}v6z7;f8+HZ&XA<+KqBK$6xe*oGe?LUI~oxDuTA!+{u?C*nKkaoiwv*iQW-;nk~*t^~_Tk7r?b{p(oP^Gjlhq(`Rm?7<-f_)o^'
        b'N&60%zlHMeoNKVtKJqp6^8vW+oG0w1$mdtE&zmR0zXJ37psBJy41H$H#h{3^&w|+o%AG6ve*o>{Ap3UBz8Lm(mx=TbAipKBZ`v;G'
        b'$6#-QJ%6WY-#5^2OJR4&`d$sQb{mIZ$ZREfAvy_+_44r$KhVl$A74ZA9lN+_=3a5Tw3iD^BgtfR@qD%>q_H!&suO{G0zx8IJHHVc'
        b'zZ4`GOo_61HnA2}-ink5B*d&lljKvTDHC1Lrb~w<QVzacMANlrWZf$@AC-ucyK|hg`3iSUXRu3%Hxk0E{%5MHDgP;va$Ti3S$Ru2'
        b'&=(O`n(6LCkgvXpdCKdw{BfiT;t5Defc!QYUDH=(=vJ1@Ra1@kT-<A3+;mx@aLqJDYY(>bRERCpB_=8$N%V;X18sr0pcWykR2A_e'
        b'Z%%Y@Sr+;-&5Mh96j{*KQz;}iL9n4vHp6eTCWO~tTA?r`LkaoCucGJ#dL~A6%hUYvqH)bjT>K3`Qmq%&h+_4Sg!eWqf1=vmn~n}e'
        b'FUyTD1J`g7<4Ji{hkLt3n{n|M2~r?sd!<O{NzPIek5G(7X=+K-n8m4Ok>YKmc-E3qC`FtZ=R%CRR!&*gxZW7W*+<d^wH^>Rt(3wU'
        b'wMB_atLpSMQN^js^yT1`fq6kvG*#(X$f%K0FRuteJYz%|tMTQ<tb{&LC8Q|PYkU1-V;YS9Cwj)MS6rT=x4cAu@gS*Ic7J<(CoSYr'
        b'(LKOctiHsZ0nV$uQe+WH=aGs$qyR0~oJL|Q=+!_^(z^vU?*^Ecs=_clsxS<pokf%od-xJ2Z@|*!gO0B7niBav_EX~BbH+OP-DjOR'
        b'L;Lr2;(Yt9pBC@<-}to94>t9BalXCzdU4+U2iJ>p?)5i__r~2fh;!~=y+NFFf9VEs&V78pIOo2oUz~IQW4}1(p0!?_bI)Hd&biN9'
        b'FV4BQtQY6pKeJw(bN@O}K2=ETPn3(+B*E7tl|%}=<uk=E#d#}r!i{(hA5$cNl!S!}8ITFgT9>e@)S*Y=E8k$7wu|o8goks9UL}l_'
        b'X31TQI`!1-=&7+P6ueFd=8$q2cyFnaZAH2W7YMGF^2z)mtxR!wxl%fLf@VFnQ&o|#vRJw|HY7nt6FHQ0vt8-#jgpK9Y!?E4uJ*l0'
        b'0Z$Rv@RMb;+O$13Z7S7ar_c?h**$U1fqpKnJ<zU`(3C9GPc)d?Qf>Yam06XHkH<RKfTzjg6OT?*jpX@(*M*|JB>pDa9S)OvK=l%>'
        b'`UvrpF2NEe`!X)gjzn{c1q0W`tOn)_3sjq4yYP%k67Du@g;Pag6O*9?B&+pzMZ=m>je2kvog7hm`^dMPdO6#&pVjJfe|5A31Rqz2'
        b'l>Vg$ib8UH;_5n7c@0u%9ltHC-b2<#nf_@jlsgMKdGe`C1rS0LMH}<Q3Xf>lcJ9Jk+dr$75jJ^4j<**k8^5(5j!DrRLgwWu)_ot>'
        b'?gndX)gZr!C=<~8hQi9Mg|mb#))1`^qx5|047LWTYO8p!>xJ)X(or>?93|>yFZqP!tTS<<vF1>`85MrjN=WZpl`yOXH=#uze*;S_'
        b'oePfghq$D<<iK2>hhNCmz$D{4|CA&&;a;6`RIKGP|D?1iA?t^PD0lF+aneAKC#2QeA5x@FHI;{qSxPQ3ON-1Oten#(7qlr53HY@}'
        b'7i=>*P(yh1B!s$;#N4T0<;wxlNK*L)7cmnr6-IkEEoR~(A~XThvZGSlB}xhsqJl%juTF|+RJam;39^qbjMIwe>5&6ln_P=8n=9mh'
        b'aq%ybH;@QQzE&<%w>>lpiGPmT41DDu3ZJSCxSAYM^8`H`aXCb^;=&4x9)=|GJT#kRB?Ywh=gSi+QM{|g#MHMMNu(g{9KF$WP5NQ7'
        b'm9G;;#?2wl+_mOT9Zrkq%`GWYH5{eW0IMqO;BTSj%3piX=_Bwj5aRNn93JWejt_cT|7nvu{-BS~DUp^cm8ygZRZ4ta)*<vorHn3K'
        b'Fm)7ganQPZ%%sym2#(Sg$9!$jE5wfqrBMl8BcvKtdpw-`>Myzr39@e9#OmYw%H>kD9zB@Vj{;p>f&^bD2w{UII`O~p2NH>?NUB<6'
        b'qB@3zYNe`mi0fn^Rcjh=*Kay(-s%O~mn&)**_E_A<dQWLJozlDpI@dnJm)La(_O)~Ske+);cM{tQbeyJQzxIRBw2m2*szwUnxVC!'
        b'p4bwqw>t7valyr^j*7MF+XLPzw2hVD8pY_+g!m`Ce2B}&=VJ9qJY=jBt%PN2cO(`UcO6?3PTu1PamaB|h5RERt4`)sJP-M5q&XB{'
        b'NOlDI)#7eUUAg~oOI1b*b)y^SourUN?k==8Bw@Ny`oIzjitUDe$W!8NJwdLVLcH+R^i)w9)h!(@Ja|!1HZFofPC35KQNkpRlE1{z'
        b'6|GlFYvS`c7?+OEpDnRuH~pvet_@;OvulIc)4aby>}kqABla}G&xk$ES3V>5G_QU}>}g6iiapJijbcyp%to=N$-GhQY1}u8J<Xjr'
        b'iapJN8^xYx%1vTVv*ISPr}^AXVo&q%O=3^;y_>|I=I1wwJx$ilVo&q&o5kJT>uwfzcOSZ0+}-`h&EoFvluhF9ZfujdyF0i^+}-`*'
        b'CUJN7=q7P@cls^j?r!K7ad-DCw}`vD`)?6<cMsnp?(SZ6tGK&szg67b{rs)s?(WOCio3f<ZWVWT3vUy5cf+@dySqcTiMzYsy-nQR'
        b'edacCch|UC+})iDB%S8Xz%qKTyII`jy>GL)%S(Gay370R&EhWai<`w=-g9mjcX{o%i@Utn-7fC(-g&#Y%ljy>p3b`f8-TwDHqzY^'
        b'pqK6meb#JwA2=7dl-_RxmjT;8OS+WNZa|@+y<944p9}2ve=^)d7z`0|O@ltcg?;?vn6HiGD#MN6lxIFwMj7+@Te&<D1PN*~*vZ00'
        b'r}?<hFdx@S<wF#o5IC%N=?Sc6QZb^Kv&=^$*(arl_@sbTUyqMJOErgZSG(^z=99zS*AwZMWmR3;qEYD*{Ny$9f=Va;Nbt1>#W&yt'
        b'NAb*0N-P}GCA<bLfsHovb##Tp?c{+ch%YX~z}Jyz^|$*YH2Jx^^d&(vj0(-0(AOtmt$^zU_yx2IXcN#YV6_00L_RQht7*0faXpk!'
        b'eRNCjxK;Hh`FOsr0LgLj@mH`u@hM(d%2gZ1j`Ft$s*B)fA{g^==@6=yuy6q&qA&S(dLJp?M(uk7=z~CaxMwZ#qXF$)*zN&MZ~NW>'
        b'O>g^;2Q<Cy%eH8G+kY{j>23e@fTp+o)d5X!`x^tA-u8C}G`;PnEt=l;30pM1?H6y+^tP98(e$=kw`h9X>$hln+dr{Ir?-8Jrnmiu'
        b'Et=l;En76b?K`#zzDK|BZqf9%Kf6WK+kSA1rnmjIErJiy@6THVFQng_TLeGk{C!aHM1EgmQ1C^5j%rZwMt)9rQ1C~7{%%n4Ncznk'
        b'6nv83DH;^Kl7ENVBKRfO9X}{|CjA-*1>fZN2L=W2<mcN51^?uy?FI!8<!65f1s~=2sRjivrQiHP!B6>pp+Uh@>E{>}e3gDn1_f{B'
        b'=RpSrf8}=r1_h6$U(2B2v-DdvD0nUXLW6?e(r?|M;JNhMJSg}s{q7kQyqA6t4hsIu$Kjyh!Swslpy0!NybTIo%+GNT3Vuw#e+&xw'
        b'3jFtZA!C7`oBX_xv%v3seqP90;Au{LZer#44ECQ+{OQD#j~nbo`DOXX_89C7^PTw*0vG2u=3AdM*ssjLGJoe22K!a{ZTWkE?fLEb'
        b'n}LD+P<|c4t<B%S@%H>La@>~xb&ikae~;sE{_`AvoBs!nZ{{E8Xr6TDB*JqhoiiyP=}nn5Wl|yV+)2|WS%A|gO`p^UES@xPQZCB*'
        b'%A{8&9fN&@8H}b8`W4%H`xI4vjH^+sP`K!rk|bC4C4=fZr%};`PH|QR_)+@edpezW22*(bi)Kp<_yLgY{Qc;i+8JQWoW%3|%JT;M'
        b'<`)fi$BW`SYD~ttR2N4n9XpPC&%0X2ahEc88FQC2_gv<l$K01O_k8BAVD3uhz8qfU4gWF(C_{)c1Svz9G6X6^s4@gAL%4E;E2nf2'
        b'u6!<YmNI7<bCxqF%=4J@GUlAmoE2;in-jo(jWp=!j{fau8TJF9gP>ePhW!xmb$M3sh{R*SeE8-5(ZKQGA5b6QRD<xJ_XknGgNGB('
        b'AWNaq%opg0`e@ZG)gyNWNx?4MI{jTGZ7dLt%q{on9a&dLboQdQj#aZ432nw;^vbk_N@-F8a}W**XrbvNn=Z8G(MDo&Pvujfq|0~V'
        b'X@%EvP72R=;Hlwt$?ypCE`gsf6j@VVSlZVif65%CFkMQs%P*N%R75(Z)A^=kF7~O(6~{{B8h>ZJnv2HrEKn+WF_oD!mBQX&C>DwJ'
        b'_+mxr!b>?@1<JhSmIz^K<fHckD0lf~m+5?H&l2}3n^!Tfa_;<j6}kZa81j<=%1SZNH7_i;{B%N4^-kL&SU8a%FAWwCqNhaDt`cvi'
        b';aJ3#ldW5)gnJ^`K}MBD6r&)zprCyL-$E@=s>3}!y%D|{4bq9fAc<gBK2_RR&{wR`-%l4rbJ&Rdm6Wh(M6oDyS%i1DED~H&dWd8t'
        b'GvSL?E2N_NgjcL+c6kw%YV5f5ZS7Kpch+c)kXVS+Y|4rfE89RaoO?*lc|g^uQqW8F6QSAzt-Y%j@NaJ-MYIGp0fi`}9!0<M!$dQc'
        b'x*CtK(YLIrv7v575#_9RVDwrh7%QO~j4`7`rX-7Of#T`KLSJM`Im$QNZM3uR4Uv*_S{_n4&`U^-3!<j+9f3U|q2{>Y=V$~>C8Z}5'
        b'YU<>l2>J0uEr0$#cXdL;BquFCE$Skrq}&vUt7XuaK$*R0>=M-k`-Ez-)dBgMpl6hn@VB!shZ2}ph}Meu`70sJW||qYL!3=bzJ^9;'
        b'gSRMcE@D=kR)N66J7%W||4&q?L!Wtcv`USdNNRX3xE$s#`Sn4SnZ3H8v$q745>WruBF@VS3wklM3VMsi3?652rx!fV?nV!;mRgKL'
        b'F~lh}nEa`O^I4THwAzCF^|7j0MQ})Jz0yjJXebf;=<dSC)fbG?%O}B6xl6H97>)Jxw#Afqpi7FV8H&;~hbBi7a}W+6J`YUsBF^Sv'
        b'@KFSA;T@np9EB|w=<3pJJ^nRFDn#NobwN^GNZ4jVB;qzY|0F8{&_Y7zkYM9lB{VCQ7OXE`dU{2IT`{+}(%XzsTilO-;OmjG$w8a>'
        b'f}e_Hqu5W=$!b1()Py>^dZV4Hh1jfW4)pkSDT-K$2_jIu3iL%&?9cMPbHRQk^sxs^e>HQ!_VVhZS6p+=a{nXsmTS#!<ukkg>iGOw'
        b'M_#}GrI$8;%m2)-r`qp%;rU<O)c0!6(A2k{e6o%&<!U@qU4VGoj7_7{AlAqmFEQHPAPYzV9V#-~vw=r}dqEF^x<IjFqy5=Sg?Sz*'
        b'QiynP%Lne9WwdVu9V#%|tuu}Gsh~Gtj&!b#^4CH%4?J#{ucprCsr6Ocs%xF)?%EX|UyaRG$L6>kHFKyh!XY|qJI5c1_<AFBdt?rl'
        b'uD&qV9^nYBL-7DXLJiGzbxieG6^QxdrwAV@z2q;dS$8-Z^mPS7^r)U&o{|AwdFcxK+v(ki;0bf0J#Bht%$;Z_a_q*O&?UsJt!rZe'
        b'U#Pd6+~%?5NIv-)+$TSVa72;N)ASicE&pj2DcIhT;MM6zp?U%_@yJf}DZgw!hIuH6p_l4GD>xPmV{omaG8D#_m}yHRz68u!6$yrs'
        b'AAwJNtzsSiE{xz&!eeB$Aw1uksqccw4f7DosE$>>SlG9!E8ObuA{P?$9gK8h#pQN3x!kqB`bI}{ozquuTRvI_B8IOm)<gRmY3mNR'
        b'_wt!fZyyugr1<wFS1C=kJ-9kZ2a>P~EvF~7YDc${DunqgsSJ4N&f#0B=-fHMP+M1Tdw{#q8`B<NS64|VQ;lF_F`rCNC%eh4yU&Sb'
        b'{HTM026yM0_&|WM2csw4E%tK6%etfsRvU$@+a<4`xzt(haC)jS&3v9(Ta(jKG;?Np?}o+(8KUS^xnrdC_~=^+b!~KYd%V;z^WyLT'
        b'YD>o*Xi>|8QQzu78=4{zZS#pwA&kz&35Sj_hG)39r%mi1Fr=Lxx36)@sY=BEs6EjWYvYWP3Wr7y)0a(5QEZ8OF;Lqgy?7`i<vw~_'
        b'u{aRJ1|#5d6sE6rFw(|noir22iL@28Gx}<eG$QTZre-I(VT%*JhRI-pPg6N)nD@mnx=GSKv8F=)ylwJU`<8ocb-tP==M}zrrS)ku'
        b'7w^(V<)Y!Xcm<ItpYu`1^4s%gQBcZ9eK_#<uSX0mV!jz$lI^SUAW3Ll8tT();^$An5Q1Eb76S6~XyLBF^sx%4YME(cV<pSQrbom_'
        b'T}8~hY15hDkdlAN&Tc2((i2cCw7<h>Kl$kjYjfzDP<Ty<Wf|~u(6UK8Ye;9fqG9X-n1|om<0r#d?HW6&{1yt**fM{tty7rGbVrc&'
        b'?xlKndy~_)gljqOk(LJ4#&dUt$XL%`gDdU5-4U@JV=lhw6Q8%W8)^xMCB^r_VsTuLe=791xA)NJNWN{MwPG+zX%&Ks&d5>IjL?z;'
        b'&G)Y+>-aYo(edvs+A><s3FU^mkElKIud?kTJM@!K7q><WPs)U7IHA4j>zfq}Q*?|tsh2h>f19d0o2x~V<v|(fVJNkmcK3>OiWu<;'
        b'g=w>cdVB#B2gBvb2U61OY2rr(0)4RsD2LNsU8dl-fG4ZKTApZ~n`oUEx4Nqp{$p;BG}ua2Lz!wQR}FJj!#ve+nQEA?8Y)ynrE0i5'
        b'o?xkJC{qpPs$s5bn5P;<(#&IP5(ek;>S|lF$4Q2zHix5$)!ChkxmTUD!66LQjm-^Sg}zg4c+hOQ4Ri<SOQ5fS9tQ0O{Q&e6&@VtQ'
        b'gARlK26`979x_|TfzAe<51Ij*4Vn+C0@Z@906F7Kf%>L5B-UB{^Z;idl2^bgeU$b@X2KldUV4$BIcPzz3G{>lT{^GouvEcLhfU+I'
        b'T(uLuw^G)$$KtA6QKV{jbLp7AWvrSH@VGkmR=QxuRgNj*lN%p`q&9#L-#|Nab&;ZyE>}ow%_x7*+9-V$WIDH+0N9+9Ym=zMM5Pne'
        b'0coXAhh_0XaaGH0eqKtjLI+>8*w<be=m}#~@<S|iV}3QJ&?@8}Pt4X8Tos~^$0Ap^!-g4^l%d;I<G{L8xQbw|n)Kl`R|@B?v(p*p'
        b'xEYf=SQ`{s@tVa;B$AbG>Pbp1Wi_D$2TH9o7}Mn+PmP>(=}6zWy*g6rAhGX}G6CfR<_ef6;4%U81yneMJoXncR$l{s06Ocx%$7?)'
        b'R?sIv>p%~I_Ja0<{u}gH(EFf_hs~BLAO&<O=>DC87Qx&I3V_ytZU@~3`kD;0M;Dgp=diyDdRMyV>@r)<-KF^#!CVTe04)MJL3JPx'
        b'=t|HTIcMb9!FTCXeqaGxKs=1Uu~@!908`dkW>+^hH8s1vPKUHLcwG(6bR`(;2fjFFg$ljio?GsVDMd<z7T+E82${XeUzW1!pfzMq'
        b'EF2Y!BD!)L^>Z_Qlc3KX^o{aVt5>m5rxg{Q2H?l_I_Vo#AWDx4tV6`=qn%y>YmRh5xvsH#39Z?<ERVub{P+s5kdjqjgwocmi0NG{'
        b'XsMbS#?+h;LU@Be(FP$oY*}e3yX2BfoJ~!QO+dv)hbZyLQ?EVni&|KL;sF&ubF3bardQ&kn)JpZK<^vk4*oWN9EwHwYS<-icLk$Z'
        b'Klw#t>VCD7-1MEzkVs;GXTYAu$g-J9^e)Qd1B2u1xI*-Njcc)wmUv#9XNhl_!|U_9>Ya_vUZ1B};k(G9#CUij7m{i^U+HKbWkrm>'
        b'PMu<y&>y+!rafYxx7sdljd%lCw5gkyNFT3s8lTm+NTf?1Aj5`%ZngAyQ5LcEOZIl5U^-tapSC%WOJ#vRdaWT}2E=zsd|y@Q^m=@r'
        b'6&`A!CbU=6VyCy%=X5M~`dkg(CZDIVxvAQzT&nQhOfg?LbB~%j+hU)q$yTqdQ}~IHVg-)^Z?NqeSG1>=Kf|yHn@J0IzA?pawU}43'
        b'h@H9#d8{_td#t9>;t8N8yfM&rSM&yY10LE<@l)(@8?{farJ%ecQX<V>)Z14tZVE-0`GZ2zfig<KI-#UR`m$bu!c|$M6e`VjjCJqY'
        b'NPu&eQqjYx0T0LDc@(Y=WAa^6gaJ0K5HTXX!c)C&lo$qy(8oBXx6g%bk4ODZ0_RbpFFaNBX=?O7H8olZhdT-to(`3prOOYDiJbKn'
        b'ro0r{PzdP?+1HY;;5qu(MLfBbEHI8zBhsh26jxcz)s&()EZQ-BC1tNrKj~|m(kaba>-AwNwKlF(k=LhCNeEr8q)T5m08%g0B}P*a'
        b'v(ZBfCu}u)sOtk__nne%sg`aZ&6TJ(OruZho_KDNwp!Z0CXEYphgP1FK2M<AAL#^VFX^lA#ZI6$+(mDZ7XFiw)T&gAV_{?yGr5oo'
        b'#sjl-&COp3iVjOE{;9fb)Y7EP2O3W@p4##>KIEmmqET|v#W~FZ(&q|w2Iwnes4dW_?&3!2N_CLRLi{_%=V~6<!37dA5mVlLs_6-L'
        b'W6#G_7A2d_>%S%`ptLPciNkdY1=~D<P`m08=~>+njs-i`rgGJkIMRhO<UNJ#dV8XY8K(CTX;ky81nJxavrP1960cP05jr}9r>9+1'
        b'ebS<Z+eAvF#aC=CVp`|X(yvmT+>Eb6s_BaAQrdnaI-a715k3P%cgiqr@i6?MEkfy@-x!yD;>F&gh5QJGv{}T5ebsZ}!a^*rDr&?}'
        b'DN4hLQ3lS2#d|}GQjQVdr#|DwJiLngU7a#Jn3xVU*tiDdKs&{$qwAe~+zTzyjU6t2BWGcn(FdwZ9pl927L3NlPzB0G<$LYA*OZYy'
        b'C!J)c0>IoHY8A)osV~vQc#t>t^1jtLAb<EY1lC|X6z(Ct+7@J5ewmg{Iu1K+lxg{)BJk1B5a{FVP8OAlNZSKm!fJj7gAXxY#Xgli'
        b'R@<*iezkjbd?*TT7Kqjcy4q#rX{U?~77=O>^vQ>UMJdx<#5Cn@yn3ojJi{(-4+h%#zWFL8Ip)<=`0GoX>-b=qNn?da)VhjB2Q@gj'
        b'_v$zwNMWs`&qi8VV!_Oxs#wkSaHXU^br+-t<4e@2uT2YzJrUhdWndh!-ky-?rP*clH0)VTbyWvN6KPOqt3~f}E+OisXLY?@Dc+n#'
        b'CM1M?aZs>%8>s-4x5q`priKyjoLSU_d(`2}9h(Al5`ps82E53r3tQF3P~4SNF_JQ0Y~<7WGintNKW|+dT-AxtYB~5Et9P>p()@TC'
        b'T<TGJ8m#fLpU5~+?rL|lT4vHk3jQcc;-L*fe5NF}6CMb{fpZn=4)J8-6FF|F^TY%3rxtH59b<O~Lm^E5FpYD@7d}|YyV0`Yc2|h='
        b'0Dd@YjFH8+5X9)c-93tDb(=a=m`IDPv_a-e1nz=iJ!&qI)!a+nU%4DI74?xMzMWG2v|TDVliYvwtagjHaO#ERYE?V0=H={*(9NHC'
        b'3=hBb#jVuWQJJA=qxdFI6KiSEQ964XF_;PVbf}V1N9pXR%FmD_+c#bO(aM*VlumMd^M_2&_#y44q&g%E7R^Y?CnKr6=A^QilKeAH'
        b'(LNbTZEH@7PYjg4jAI|)9_;aV``Ym*&U)MVRz7u>bO!tp{>Rtm=SLMzkqnk{STKmxl$pxhBC&oiBoCdPQdD0|@DFS>8}SU4cVGEu'
        b'tU!;v`xhnU(maNr-g!??jSXl1zM<$;G3lmG{LpH=TKwusxJ~CE6V$oz&%P-Ee692zD%DwvR?zu$Cwfq;iI*gFc7Qh|eYr`AARN@w'
        b'nYB)v+vjmznf@$6Vqd8rkGVszogZ-x^>+Kn9@ShI>Rml`E|1setap1?6wXvX5z!SP@-5<#qCS65kAH3atx{rsOpU~&(7VV$57^jM'
        b'!K+KekU$~yj<oVmTMhoYMtmsn;pu?B^!3JqT~YDHSjNYWzf4Vdk&==b6K9yv^*+_lCq6nvr7UTwBE}GxD{if@l46$l-0k0A#rox3'
        b'?}s0wbNU83_bXxliOzmG?9b@z3t)d%Xa5-N&*|)>;_|0ed3UP3WT7?h&YxBt>6G%h?_3D~pYi<Tze8uWkYX(Lev!v(t6nn4(PXP<'
        b'jyd$cjO0%eG&DB&9Q8II_iFN16Oc@{r_Gj(JjQaebxD$&o3ZiP8pHU@)8Y(O?i93zRg~wia5H5m^0c=oT)rmTn||-fJdC=qnfnnA'
        b'_0YR_CcnB$9tWYonyz5$9Ikd*z86oJ^vxkD#*52w;ofweeR_PW7t`(eX<6FIcNR$tPI-KZT;tnbv8?gMu*r_fH=Dk0{(|CkL-(k='
        b'R2h%Brl=3U&LAfX-~Mq2Unm^9j=oIk-*5X?iA4j`zvGTOig@B6U}$w*H7?t2%CJA$Z?x|P#t1>1L5Dy)K+nScph=VI{2I(t*BkBK'
        b'ZvUzPtsqM1D|BH|2^g^_aIM(g6_Nx=vV~LLup)19K#ZR-AzK6qVby}aJtb|C2(Nsgrw1D%_%2vL`P2*V1q<k7d!clehukhHj(<tf'
        b'Ohqi#6&>|lkvxx~A~lV_%O`J<&=x+OyH7d_0nP3FA<!zm7i0{umTXWiC=ZkmngW^%Qb036g`i?kDQF(35@Z2cK@LzYs1D=?c|prT'
        b'$>OuS;1&VJKz*QfpnlLs&?eAk&;aNT&{ojBpdru>&`!{Upk1IxLAybFKzl*^KrX4HjqVLyK{D3yYm(@Z=#@ynvBGTJNM+CF`YD;X'
        b'q?avJT!J(7OJ!ENb&Gn}Z_{bUGwR||8k<iuUWP6n*Yk3k@v?RC2=6$}czL>bl=s%tjHl@0as98S8PBSVNBni@G~@N_;?cTz$7#kR'
        b's~V32>^$9gMlBxQYklx^<7H^^=nm|z(~Xy{#pC+-PB&hj7LT6)yH7WsqQ#?oxO+}Fo>hxScXs!lZoGai9^LQVce?RlSL4xG-GAEg'
        b'jPZCB_Sw^pml2OgeCEJu$IFh#qx;A&oOZmtcsyEm96arKN<7{q-M+}E(_5lH!<sF}agH2cxw7BSl>Lz>+v#js{(PD4$baxhWh<BE'
        b'yDZIlfoLQspUd&%<NTyK31$oTXy1!f&x8}`aaUhARyj#d{II`|OJhm$;iuT>?n06~f6k^li#rdgL6e-Y5J_?g1^Q@pFHT*CBVv&?'
        b'>gqsi32}E)-AKeg#`8l6zF^cB^@jpJ5lB6_R9K|Xs4db<i@(`rEF9~^E+>8rw=8~WmX;BPI$!!utrmci5Vz(!dP8l+in<O}bm8Tv'
        b'0o|)xewKs0v{S!{MPkzm$NEsn-~LtCI_VHPUDWdWuy1JcIvuo(7D-OyM?17~ij(BNpn8}pDq01bzfij`URYfO*<2qY2Caa_-QFl4'
        b'WPI6(?(b*|#ju4F--ziW2S2z-w@vsFmBwmceSNdfZR3Xs#Knt3iW<F&{)WO=7o~aGrwsv-Ib}!(tJCI8?*{nSmg(yGNwMtbl1JqZ'
        b'z~4m!mE;{Gfe7t7w3>BuN4<lZNt6Y{v<0Sv4)t_z#MS6?RGhN3;rN@EZt|k5A;B=a@FL}c^QRU}n||?(t^iFOI-^0?JOiOIQsn3C'
        b'd8+<MkhWDxQRyr~Yj0HDZiu-kB8b@?2(|UBjl@!Ybau%h_+A^koFG3bLNe|7%b(E;r<*8IK1Jwk3H4JXSf+W1ZPVHyef)^VdO~g8'
        b'kwWY}(896KVmj_Udl4CF^WPEdOLd`pFGcB#f}ljmG6wz@CEW@<SvCh#eolK}^&EMUT<Q%QGV*=Y8xrYPmx=uq?0a=?r~Av;CgMy5'
        b'mTpUozY_KsXftRi$#3_z)VylprXBc<&r7ACosMV{BP(d1mc!~DmoZPRt&IK<m6y-saM^r<xs}{@Sy?%A9u)FRtaz?2Iw<6tl)_wb'
        b'P{=z`@T@I8DCD3_g?ZLNAs;0l=8F#sxhZ*8mhd{`pZWctj{mRz4BF3RFl3p`27}RPG?_9o%%%)ehM6hquaJI9%5PI%;x8lqlMXii'
        b'Go<+me>?vf)BMO+VgGOZE|Pkvuavre?<8Gsv=${fDzv`C0<jd-U=U%a$~YG$;b?9jHv9!2B7Bq6+2B>g8)7Be+a|;YvN>F{OO#)('
        b'BO$?25_vScVey<2?jaAF&XyN&W(T@D#5)`DqD_6@7Hn;sBlN-$#KLq^jx@y$8|{Tp8|||}n?S>`KMjh2?f_l!jM4ri+)IJyJ|pZZ'
        b'k^5+LZjyh^GpX+PKRtFDL~1^d%J9kgr%QwKx?h*4K7W09GQR?vydQiW^bTk~>bw;A>`#pL=uZURCyC7GKWDVR@K-@aIy2GXXEk#P'
        b'{7Qc+%$EW`Ce5Lrf#077>C;W7YhMtUeZXk{+W}!$DLL$;y0l`iB>L_Dy)5@@nw#zQvGY#O|GlLAzxy-cc3kHBqQs|uW3=CZ{13gV'
        b'`BDD=g*H2)%m3pte{wHP`X#eWS3?a8hB{b-t$~I7Ay!&eK6l<_^D8PZ_qVpS2Rd{PHhZ<hS;M?nvc>gYR!~-Y)$B`4XJ2lceWic)'
        b'bypXJxRYk9r~Ce)65U@mhr<HhUpC)lvbQsnJqX$dGQ(~HJ!mx94}fmZFxlUOdl#@dL)cX!_tB_1$$vves{1Q!>@<kfe2&QQ$@!;C'
        b'gYtSsm#02|eRwjTZ!p=LKqo=vsBaHw5aw)zf7m4OHzq-3zBJ2Ze`A)Q%XMa=w=*^KBKTReh52K^CDMHTIFo(jX^=kMWV-Q8f#>Cz'
        b'>>uO^yGqGn_vzBwd~TxOe_tT*{R=g>71PJgJ30Sx;}i2A9w*##b3~ZKGXGyrGTHA${>P?jew6?B&}P{eX=%60{K@^4b0<W1uVZUj'
        b'gTLY5`h;mGb9*dIH^1%wlaDf<Q8(89ZQ@BL-u00Dx=*XRd~Z2;=OfSGYnl7ioiASej_dM;Up?x0|EvefzjWv3pJhLORY7(5!S=$;'
        b'{W+}vP{rCG+N#e9nIC&>_vdTgey{3JrpC(p@(W7et6j6<O3U}7H~hA7Qm;t$h?MCyL%xMtA<+6cft!9P@RP?l_HQh)5gs_ZjpN2&'
        b'-pMiW+;fDAPwXdNUtL>4xc!dvx`Eci_m*x44qUiz&r860GvB@@w^}VH8#;L7vU#hk+5U!A-9Pw7HCwo)<+bI%tF~@_tnY${Cpp}I'
        b'fAyu;&RgObe6c?BXGi)S?|l4sPa9`H=6Li=zgk<}_h-jTUXwke31bb^4tfCg`$2V}2x#_Fll?BZ=K|ku7Iu}$eKex5di(UHsqQy4'
        b'jhzOOn$Lg?pPYZXG$^kdbb0FY*M}$b6QH+1_j*kB=Rs$q&gH<JC}(4{z)wjc^B<R+?0b3y9n+bKzNxdn4|B$q!aTCVWS=O_&a1$~'
        b'PJ{I6jz-TT+<hxgFD%i-_C)(or@%Xcn%jcz(@&4`|9VpXH%YgBvJTrNcC?u67b5?Ct295#e>K|aK3)DhWgC+FsrVMX3eQmAiOUcC'
        b'S*juKqMpMsYJts}X4Q}sI9q#rowTPjj?Wlx&NPgV8^(_}!7!fx;s)_EXTxQD7EI$*uN-nw1B;(Yb;uT==@>r6FAM*T95S=Av&`Ar'
        b'hEoQ}$mW|xGMdQ7U4%jJkIg9j$$%#^_cvw#-|)-f=O;|)H#5s*S?G&#EQgI}x$F#fCOeD2n_u)LtflTY*{=mX3pxY#@t{ZVHQ5h>'
        b'zVKy}-Efb|9s^$eWnou|+()CUll*V}a;p0u?;bl1A~m05cZ=}J`KL>R@*?+Jznq%CK0KK(23`ruKwTGrt^?f-dmh4n=Su>A|0O|W'
        b'uGoh4z~h2yb!H-i&R!3*ce^k*0$Zi|3-_Ds_nZdl(;bbb?=ac_zT@=568RoXa@!^F&^I-=4Ue6EdX)e1r2JpHU%2H<_qSwS9@}ZM'
        b'e-ioU?b7@x{~r&T?0?bae{4t~xu1$}xf?w$l8;?|iuV`)+x=hPXR^=xfzXZq=&#I{fkkGE>%3D_;#V-@(>71F%QZ$$r}9sHHTd$+'
        b'elA4u?wwR6bjI(kVrLD5TvqnX7p*W`ndbz|lWpv;b8K+8v9eYh^L)z27Tjt>7#mx8Kl~oHvFrE1f7r%`UPPEzZS1MPA>0WYdkghm'
        b'kYi_`$+IIJJIlYo&Q@M*XAczFk*1x^pKoW^TkPy<yB+D<x6`>Q(ziwOgh3>4-66j@k{sicq`#76Qj;8e(Ay+imGqNRH9)^1xjdjR'
        b'fbOD`XR?0=sC7Ue$TK3eJpKmgzd=usd|;3t^c`Bo%DhR|Fm)OoD0`mHkIC<*)WRee`Oos(DV1YTz6bk2zTf(bw0~2U`>VvOX)KUD'
        b'1^FHGZJEv!vW^=`mnof@07XcTER7eC4|KgOKgmMgLi)_4ncB%C%|~V2jWW({peJQ}7Rq;k7jap&;vL|KtUoORw#x6lf2Z%O@|*8%'
        b'@|_`lf9;lW3Fpi5{7m-6GqN41?MN<u4Tv@b9iT7EvQS%*T<KmJ=W)=}vYif-Y;DqeDi0}U$@;uYdf(_Bpln}CgU&3SkZFEXmg#nq'
        b'g)P@AOXYX&Qdy3ZGTm!re;<+M-XlMw-!0p1zU;TJk$ivI#xx#2L1zg;=gag1a$Mag%Rt}5hv<x-`~-iyY}bQwlF`_S$~u?H@slaX'
        b'GnMrx(tjstm}F~{EOl9C8qb?$*~NLxBWRXiS71vt7rl(3<Gz%!r;zl4>5T0|Q~VgkbexkR+mQO?)xezTH(Yw1C2M8=+?iilZ+Y^W'
        b'BiC)pib(qwOXCxM^Qs4bTQz02!+T=dpQ`S8XZ`czqkot7_oy3}P#1e*mutc@sLpSiEiE9pxBA<~`Ccwl9d3P~$eWssd44M4FnAzn'
        b'M|K9M{V;ohJAo0<rflt;UgaOK@A^Y(SnD6Lu7UfeKL}nLCG7+;(uh|glvrQI!53`5dQ@>}?cKBq=i%r}S+IvbrUrX>94@PN=1id%'
        b'i&0SRd?HU+d}2!U;j#4|*pd54@lGhvMeF5nn3>^zEKTnL-I2u%w`Vcq?b*!OZ)Ao(6Kn0dhRe{Ue93H4oHflJr_WxuB<;y(E)y#*'
        b';fmY%SN>pZE$T(*n@K#JWua2YPc4Y^2z1_Be2tG@g-rNiWM#H8RtRxOUYVm_tJ6*=wvrMFF6clAS|d4GLV$2`f#hL`z^XJ}QU(hv'
        b'j<6Oh$N^doS_$d{tpjZZ-3!_c+5<WWdKq*KbP_b>TGlcZR0*<xmV;J;`aoRp0;8|bTs|QggzQ#dy|X@Ubu}!t)wvu#ThrncH=%w!'
        b'#npACQ<s|8SJT+s;7D-sG`mS@xl?nMViQslYl1^#gC{kY>Za-xx24V|kE^jE#l7BEome1OgUeH^%e`T#$7i?cav=u_iGW@g(zr4y'
        b'aGGkt)w{y&^wqmO^)_#HZGume)8_DTNu<fCI2#(97uWhcZd-L?_G;l9Z1w3qYHba4mn|`y`o^VB-k(VYUgBKg^ENj6>KYpsCwTC)'
        b'6E$>FCS4whJ*@Ysb2cpY)+SYl%L?I1dJ=pPrP(=J{!QLdnzO;VOzqM%zRSHHG+uR6y4sST!#TQNb<N_jywVqkXO@2S$`&4b%t)y*'
        b'yep{INuCW}XM@-0aMjeH$_aiX;CeC7eudksAK%S&?!;kB4*W(4HMQNfIKd;{bB!2_T%?uW*U{{*b5*0aeRVdwvo668E#btRaXQlY'
        b'*_&())wMnndD2+pgJrQ+oJOxLv3%q}Rd-P}sLnOW)0^P!an?DjsS#@$)e<N8a~CRRQvdO|^|rb?q)<)6Cc&qvv98W;BVjhFvEqK|'
        b'2R(n-Fd@cISbWtD-b8P5@wq&S^GNtKIo(bq=kU3k8nynYZgjZx6G3AH%?*g<;Df|Y;&-&6;IP$WVmUZ3(MNWXb7DISCn1M6fw>Eh'
        b'<aS-=s&OSIz+KeAoa!o%jHUBvbi0#1Ts4XI`bI}mPKhnfoiI2WlG0!5NlHh@)<rU&<Vv}19?!DIrX<(ohYfdJW?SM+Y%Jm2*j(oj'
        b'U6EQ{Dx|YIDIx6HlU%3~)76n$E1f$fje<8ORnNN|?7@Q}-ncB$qsh70<?%Mznv#m{7LTM<SC9652R1Y=OYD8=meT*yUB48F2TfQs'
        b'NY}*ape35fTcw8!46v!emJ-3a+~r9rf^JAT++qRK+~iDfLu;jTj<09DUah(6otP*IO~73e$9tk*O5?;`g;c0i_fZm&Pm@#+-qE_b'
        b'Bt5918=F=nI-^UP>zxfrsW_KcJHasOz0Ha4$>X0pVra?XoSf$s&CceesiAk*cd}YWFnM~KC3dvx*@V2E>HHe`<IUHQlA`ozZdiiO'
        b'Z%Fi8PB9wMR}Bu`yx?AZNY&^UR`HtJnjG3AFRgc?<I+a2p6803>yx`*v<NZiM0d9*(ca{&UWz|;&ZJp~C6CutlQJ2lvpRIqxVCyv'
        b'x&SqN;86Z6(s(;+tKHRN7$!dl69ZxB@ibES{HVbaxxN-Gl`rVyr+Z@Pf;74C7^jJ9tF9frz?`{`UY!PyZc>67qzhDE=a@f62JZQM'
        b'xs)72JYEy}N;owp?Wp3e$@5Nl=+}&%l=Pb$;>%56t^Uc9>RnyyawmCX(cw*;(Y0Q0(xQ>OU?Yuj<8U?UA7|Vr`5DI@mo>RCg|QB^'
        b'CA!x*vGeiOVpQlBVBAL?ym(ACcoG<%J{SEQ<L*w|Vw<ZWeOOvT)-`&PI?Y?>Nu5CCSZ!+%v%}L^hfNYSX2RYoDO`0Et=oKf3NLYb'
        b'Qv&JRof^5Zy0H$uUhk?~krGyn8@1S2n<sXp8cgJb<tt`H+7ZnQr`0`qG{w_#juzRAIVW0-w!j)ovO66-Z6_E5Ezj##kjUy3Z!eyp'
        b'P4>mefD%Z|LJj2c&;r~WZ{4xNN%4u;TiBZGyq;491-o%K#2b6m;L9&7y&Rp#YvMU&{yscUM8(IhP_uii0Af0f62QGg7KPUIV<bZR'
        b'c~7mn3LUG=ZqJgj!gyWkKuRt3vc|d^UZqp?lRn&OG`<>~w<Nf>t7gU6`BPh*PPj1}CY~$SdZ$y{u>+*-L}ECe)Qzm>?BcDm7+ghr'
        b'BD=xH62o(sQJ&x2FX=%^={r)hRA2fuC2chm{KSgcljNzrP`e_@2Svy917mJ(s802A`)VCc>6|^z21k-Rtyrtm)PsbhYEH|1{6$7%'
        b'QuX4_4v()ETf4+(Xo9y|7Yw4Y12|lZojOjNHjEq3_Qa)KJq`2Z?SOC;Yj5$QFL@WOhVfuk=@l!6(+HCG#YviQ&Da{b7B@Ik6Kig8'
        b')i191iaqM6Sz;Gl=NQ!&%XM4aQ{G*id{lg&xaF&6i-FF)!)^qY08KzUFax+8Xa;rzGl4e%vw&X!W&<Apjst!Vm;-zsI3D<CU@qy-'
        b'q<khYHt}ub1DpXg0<Az3a49eY7y+7rHvuz&_XD$ldw|)%UjoMg-vs6WbKXHdKn0i!TmU=+*bF=q7zUmNycL)Sd;mBB_(R~?z*m41'
        b'fhU0Zz{&5LEt7!rfRlk9;5on;a0+k>@Lb?SK)MY26QBY38=w(*6lemTeGK&hmH^Gbj|1sr*C&An;HQ8_;N3tI@No(ce2KyXj{q})'
        b'x$hy~WX9$I4Zwv!Bd`Hz0(Js3fE$5k;OBvvz}*y2VeA0K1OA@k0Z)>9Dav;o?!Xy9BX9xG1oQwifL%Z{a2+rc_*q~Ua2qfi_$}Z#'
        b';67ju@I~Nw;2(jx!1sY?P(CNn55OYeSwK7RY~WSEiNJ1PKJZ51B;c2TlYx%{=K`Mt&I7&%ybO38*bY4Nq}dVxP6u{S`GKo|^}tSG'
        b'8!!l51N<a#0C){>C$J0nB=An)&wyKjzX#q$=>zEl=EV2WKEMK?5oiOFT$E+N3}6^&2HphB1l|YC0`3N8lN1-=IN)Jm4)A^8c;ML|'
        b'pnZVFz%zgj;F-Xcz_WmBfpll;3&07${{o&(QfGh@DLo+FuQ~~w1U!EP?M3&nfag$pz$w6`z;l5i;CaC7fg}KXE6@OZ7-$3@0Gfb*'
        b'9}zNP@>!<E?51zznU+j9ogv7yWVz`(Y^EjKP2aIIE#usDP9W2g<EC%KnU?XuY(u6c7dR70A8%`c2H;gdBk)?F33w|o1Gp1t20jhU'
        b'1pa~IMZhO09x%^{c)&}5CSVmX1Go%m23`xy1P%bRfIETNz&$|v;QSk)0eFPc0ZuU?9pFM>1~3RT0|$Vaz{h}Dz=ObS;9I~v;Dn4!'
        b'%LHI4@N8f+a3b*2z<l6N;3VKLfs=vn1J41@G-q0-02c$#1$F|@18xSM5Bw%@D)2>M8N~yZ0}C=UEpvfh;5^C)cp2~k;C$dufEB>M'
        b'04ssHS*Y&-W3zz<po8o~=r^(hV?ZNtfZTU6wu9V(-ywJ4FMuZC5n#qHk`sh>0Tuu=ffisE&<o54b^+;w{0%?@@QXkr@G)Qp@Fj{5'
        b'JWk;b;CV6*;ehjiM&NRw3HT{s2Jn8M8Mq&q3H%!{3z(aeY57oc?f*I9`Tqt{_@hX|PbUcf)Z*;rc~5aRLZ)n?3N$p=(-O2AE6~O!'
        b'&sa*0_}O`>hA1Xf8}aYX3GTiq$>B<M=0b|nh;;WZF6Dyn>zqrSb$U_m#Y$<hq6y58_6Vu$#mdYWIS5rcvlsE?#OZ((aYDMXs|m@w'
        b'&vDUWabcfacz$O%d=1yQ)fVY3)LhzHi<Mxi!2MK_{;FJ;pS>y0vOFCTXM(FsrHnmA$_vbk%irtQq){+-R@PZOUY03K$fGfsq-;K;'
        b'lrv~ZiB}-cP%W0{uxjO5Cptq#N*O*b&*?1T=Vm4tGA=M(j5G~&Ut!amX3GdW*N|%(mur}mdA@mOE@g5<{5HeLh#^k+O;HaqU+1o4'
        b'hIJTAM_)JD87;%OAD#Dk{r4t2o%PAsHxUz&N`I!38<#VPNC=%T&-Lti&19#uWHJ~VEgYRqDUXLM<!;3!ljN|;uIS>QR{0Qzr*%*('
        b'-xPU{E#VwD|0DdCkK#94dFlL2v94TddFgD;=D53+yHj7$xtp0EvL2m?b8);piS^hFzw^lX?Zi4#J$Ay6&fR6am*_`>HygQ-9FmOp'
        b'Pu+J3?J-8*{ZEHee~->K+V}a4_SaB9+J8`8;&SeY#L>4!B$w~x#g$fO-CuR`;^8VbW4J2&Hi5g#7<>8C6;=Zu`c>az@~mT4lAKNT'
        b'*RJz3C;4^g{4$gLI(2?oNq!r3;d7JxLc03`$@c~#I=692emy$BoFu=P&To8@-&S2(XC(RErSrQao%~Z{`g_tTa!=EQn~`KcbChsJ'
        b'N%pfw30IP2&(r<Y|B?kCOc*6x@_FQ0ql9xL*$YPr=ls9q9=kd=Hcd?5=jnbU^6c+O(pVVOxt*b#2P5+Qs5PODwQ)0|lSiwytu|gp'
        b'baIxoHr2+-NYXsjx3)T`Yic}Rsr_?_b4A&L1qFSM8;04zt(UETY;bwwiR)hV?ptXnS>A7*|NBEX{&e309)Vsu(pxK`JJOJp=0Ej&'
        b'bRRG3-m6F+sIev92LFaMkI6I*|Hd>+R|?)(Tr^x2_nU+@xRcrU+L?W`T~48=4Dqp{GAq4&;ZDS-cNN85*fY~JYpK~n=bm3^($2IN'
        b'FE^yfA;FR@GN&6MySwK^18tuu=cevph!9)p-dI?waP~NqHh)ihaV<&hRn<Gg7U=Q!v~`l^1%)(q2SclvZMLm17-h>j6t56)rEqku'
        b'3XzV(HJyQwLhHfeC4oQ$n}%?gADIZ1<l&Ig9wt?aq~^P(D;#bwt|vk19xTC0ypNE7RIFOtu^Q*v=Zf9S>KWG_QCt%Uv@4zAuJ+>U'
        b'wQUH)&xRIz{2hVVTAp~Zoy#N@;w6h4`5|FcAsP!uik%+%>+T7+aus=47>Br$tK#}F3FqQ6f~9$lzlXFk7S{#4gRv-AmDPg=Di#_-'
        b'6>46goIP6XMIBKzI)X~UxTfzet_N?8(m}<IM<!iQYn5oYBZelWbc-A2*ot{yM7f-JB^FOB!8yW<TrP_aTTC<zbBY!dphQLC{OAuw'
        b'>WhvR*M_@E6B629>W`vRvRueeu_q8yy8Y<n5c;MkxQg_Eg|V6Nu0hURz<D65L_7VYuofEyB^ZkI#)?JFka(}ZtGH3tO%ZKD^=Xa<'
        b'MD^ln6uZ$jyj0X4Js1kn;-+4$K+(3IV1!yZgyum(J4KOcf5L@?GG1?8L(7K1psu~iV9)pu@cUhD71pE0n2RL0BqHWs#_ZuLI!E8%'
        b'r_Dtw%Vb)wuNQ9g{M+<dVWzbfz2Dt`r`bYtyG5e=PAz_=&tPZ&Klo)aaZe~)-rMk>N<Pp3@;dI4cTUFo8UGj7@f=ylDRRxX;uPUc'
        b'|I6!0>-dLH5&mT9aMhgCOxwHFY?+wkw&_m>`%ch)&<sO{y<dGvk*6Cd##778Qr9UockU<~t}2)Jr9P}^tV4*arj^itRv|lC^^32I'
        b'S`00$)6jCNHC=MNQ{nlNrb^P+&!F8FjO!#HJ-y`Lzp$SB==ag@qu)orkA5HhKKgz1`{?)4@1x)U6TkHPibS`JpI2C?=2lt@LGwVh'
        b'pw1kiDZ^enWVCxfS7CL4j`SJr*|6`t&uDK4DWKxDMmrBD^#X1EveAC*UZZ{YmyGrdnCn2hZm+QJ104jt4mt*!`q>Jr71RkD0PXlJ'
        b'y}uT}qd6k~W8X5`_2u4GHC(m(is34&d$`KdG+gzdcerX#<8W0maEE8OYTgy{JvBDM|EvGwrwobqAT&rcN;FB#kZ6{eDKSf8w#0D~'
        b'b0m(Jm@DxNiDybYOJbhH2@=niI8kE0#7Pn-OFT#76p80bJWt~J5~oVMK;nfGFOsN8oF;L)#ET`)kXRsbro>qi3ndmwyhP%q5{o6y'
        b'mRKTjj>J-lWfIFJ&XqV%;$;%&ORSJsDe-cN3nYF_qDA6DiHjuCAYOibh4mx)f0ycL{D5Acz^n^jF<Xe#_eUQegWr$kx92ZH1{U$w'
        b'<o8Ki-xBZd@0B<tafig65+9VfOX8z%sow?Czn@Be)(}rPif75o1K{~v@tgp;@4|EBi+Bz=hpQ^@udud*j>2s>-1a&JPoG*N@SlA*'
        b'J9HnOL7)~;9%%oUE3A7!3d|4Qr#*Z0zieuM>349HFxE3rqHzn^(B~Ghy|czKWm^`DpsemcR9Iu6&7i%Y*FZ->8JXGHT+z_m;J<HH'
        b'SU2HWyYsCI>j9AU9|%Lw;iDDSoiHCdZnF2ES!taCzl;+m`yQC*y#v1XH}F2-x-%+ynOb1(19^|8FC+a5qDqH9*cE7BplC|<O8W}>'
        b'm{M2}En*$;TcAuYh)!3!=u=ujdk$&QSfCU{a{_&lo<KAj42QT?y${gX<g2cARxe=@uFaTKqn9Zbi&8$nh*ec3pU&&_cg>M9cjJdB'
        b'$&F6zk*Z-|S64|VBQ=bSD@+|%5J6^KTn=*WLn$LgIi$+3gAU{QBH?h?0;Qg-`Bb`lqcNqGRI3D6g#ztL>sqCt7k^`cXvt`CxMEZ_'
        b'Vrw9_CJ+cwEPtq7AGuBFMUQKm<=>H&Hh(A-jwzk~)yPx{^>%eBT-VI>F*K`EF-qE)P~sB{lPcUoZsBJ{dC@hu!~n$#zs|v>brkWU'
        b'aCe2upw>Ck6GlIDp$H;@pin%kW}!ujc7}Vq+Nsv$Kb=iW6P~L{l2Juma!?Wypv>cmh*;F7=@M8d1u`Y1LhY}Wg;ZEhXBcOzc|bDo'
        b'@+cjotc4m}&5&AqI^!v+NsbwkcYhn#X+7$IiG}rj9_{jV`y*0~Pb|<w-`+7{!ad4tB^qc8V}x`CRtLJ2)?kbR2BR{o<W?vmQB+)('
        b'(<%ByEswr2<p>ZOc7mZ*V+|86Q0h>L`zfa$H2R`1BvDipRp=1DRFNP;Vo0}R($cX2GV0^&N{s4j9=`5iNIwoEUBQ^LCK&5fRAosN'
        b'D*b@eH<qeEsoURk4eH>J%4SO#JW8Z<ZImDU5Rot}X6Xh+VipvkNQ)|BP_Lq?_|S@BoUZEB<rwX4>(rN&l$<6d6Abr8lQXAaNn`gE'
        b'1x?CA*BE2xG3_)*oX~qK2UAb5+s8RDpEIf^YvBnNy(%EorwIptYc$-`n&3-C5^*^Tmt9Z&tj~e_MFVs)#~1Al#<=z`?k_`;uGLsT'
        b'gu`IM7~^IcCK!qadSZGPDJzNVxL$yob;W{QiF8TZf`WFXJrLsuWE4Mt;FVVPVTRM84VpRW`L#ZY1eM`T^NB0$4t7Vn65ZutbME19'
        b'4fn(fi<C7OG^F26l*3((qA;#ai4Ghw3)gtouBfWx7O`yRk5WD3Pi?jUPiiJhPU7Y8L{={Z&~FUgSlt1x{Hrq@jroM!K2%Fh;!>%)'
        b'i$u?9iRq(&Nvt9*<D`Zx!9(ck5`B>B4o(>h(@|8m@{bkPBYzfaonow6wt^0VXszQ0PQkjS>#r47TI+0m1M4Q3X|1ykxb^i4>&m}s'
        b'>l$^fL*`2NaFrEnt=B2u*_GCN&qA8{mDZL?mDU3w@h#fGo}Gv_*5t~Rwb8!3N~?E5rPWG)SX>`L8hPhbT3<jKefc8%N%*~vFn1u0'
        b'Qut>hj{~6A@LGNxWREOE@mYywD7>iBy6d7-m!bGVQHFgNCYGTN>ExZ2z6={>8CJD3(rzx4tH}dZ(-xjWk)ft2jcZqvI-!N8v@{-E'
        b'Wn4lISo>cg>ikCjf3DpJ&XIMNI;`h4i85HH{CmsLg7jijMk&J-QHCJa!sNeOmSO9Es0<In?@?KX?mjd^VKD6L4z~y7wWGM~5E2&E'
        b'RK!&vjvB&&5T`#(C_7)6tNlwEa)EX^=thZ?W(bWHvfUr^`vgz&T^9~_Gp2Y&J0HA2Yv;mq(H@}6^R#vzg8!Z=>DxJWKIYhYiS2w6'
        b';Y*38R$32DO>F0*aCe+9+F2<?*^00SmgUH}@IN>1XIv=yJJ!iqVYA5JqWpV#%~<(+6_Nj%V5k)fU#99DA4}Ib9?jRb2Ul}#m}9Dw'
        b'<eNcq!444XMS06h@}dMcJWXQih~dv0y4Mk*!)iZr<-O=q4!cU<c5%VgANKd7ad|I}Qx1<SeR~`iB3)}b(r;D%U{WgQS?88oe{SlZ'
        b'JE3%Xsq%-3c?x?s_EY%&v9A_?Zz|>Shh6OF<MMvxQvT#Bea~g>cew{#EkmxzuG1{eFd~mr{xmM~^Kqr`jkDf7&VA>&mamSBd`A@L'
        b'l)vYA{=ao8e|43<@3LB5ZnvwY#TALT`ukl21FoSV*RHY3@*E<MQ~o+`7xI69oOQ`K_f_Lst{E5k)VTiJ#tqyvZs;51c0DmhS)QM0'
        b'ZvIyeul{1<jaU6E@n4wuqb>i+fxQ<e-Z(z<Ux@$G#2d~3O8j3=G-v!P@qa$?#^a`cDZcaA|G@)~RvR-88QJR-oxeA8rPLqtH-A07'
        b'TfBiOONXoIJl(uofL7MRKcwJK_Km|;*)xW#^5B24fZ2ah-<oGJm@RkIGy1lK6!wm+oH<<OC>XBVJDb^GzT9Z%X9K}VSI)w-{StA<'
        b'ArF3ZNET_{unTED2znX*yMg;akAf_qN-D<;X50ZhI)Sde@OvI0q<P5LvhJ$ks>m|_E|a@;akCNWzCY6cIXX9;0rQEGXAy4yRpd8h'
        b'+Y2nbdAO?1#q4=MGTB>Bn(Q-B&ds1r3yk(oqrpC7<#3hXhqMu{>t>3V$)5cT>fJhAb<96pbqKU4FkJQBRyrp+@^}0jq31>Zo6NrT'
        b'4&<v~Jp;ct5Z5uEpWn6?cOf3=4bZ&RsPB8s{szKsy%z4EV-e(IKupx~LAW36WcHnKKMD64QL|-wRLF=ZMZ38J%zkX0!R|mhuZ1hD'
        b'm7rRfk9^x;uYJ^DzXRs2pnE`ffsTF?`Rp>-pDr7&QkdDYeC=@6&+j)|EIZ7WEYNv7xLk@Bsl2@(b)wH!5&4Dl`ykV6BR{3Oz5;re'
        b'-%i2*O-Sc;epZyek{uh#C`UbDr!$$kN*+4^|8;ItixuvNV15B~5ad0dStBcq_DjBMwk!Z$0NMz9Ey8)PX4V!^7szTqi&@V@i#)n7'
        b'<JSmNveRtI15LRO;}FC^$B<qg@ZJ`qy%ac)-0?g+cqq5!WzZ7XU7%Xf=C7G8N*1&3dfjAy7UB1`VSHvXE8St-jr9P!&`m@KZK<7T'
        b'nQ>@xriH#Dc9qjO$ZcuwtFX2ptxf$jFJ2j0XJ-7n!c>&=(J9PY2;2+Y@pqFw|6FF>gS@)lHrbV<CVMu}4L7gfXy4dsv`0Qc-(*ML'
        b'uSa?X7^}PK9Xa^N9@KFk$ZKOQ%RwtaEueN#CumBGvE|_^Dr0U7T3(p}bbvAl3z+p@)Ts+)*a$je&22deawCtGpyh;Nquucjll=|Q'
        b'$)M4GHQWX|(0-FL?5xvh@8@-8-y7j~mxs~+oT=^|8G=<ga^J{BSnu3WvG>poSqPqCKY%u%58*SuX|`PPpxH7PSOKa5c|r5fGg~4E'
        b'7omKR_EF#w>O1PIPhkxR+6niqps6s=KwE6J4_CE(rovkKEwkn5r@>Dap?_eWMsvC%lWnyQS9RV@-!bWdSIP1=(YH*PH|;H)M`_Z%'
        b')c%USBR6ES+<j)t-9Iv076VVB+#cW>&@KC@kHhQ{_`Td?v>!np{G&=fW9#9@`uBhTE`+hc{7ax4H~};Vv<h?~=p^FYyWebidKi5M'
        b'd=_*c%(EwCS{?zu1N+Osx%={-*m%QmRVnBI<`R96-`@`&x7KKX_Bx|IhJM?L{+hCWxawSx0=gIW5w!7zzc5=`UclG~?yMTFssUaF'
        b'y5n;d)-K??&zmjZ2GTd6I*jWBFwa5w*Mam+s0IDc+_^2qNOR@6{Q9816F71oSCO|X13cv`2><C9&6bHTQkxi9G5B2}!ta{QtP0$^'
        b'Knp;3WHW2&XK3AwwW@QtisXfm><|-(WQIJ5^3BW4u;<@xw7-t<p_h;*=)lFydNJ@5pm~U20d#=&M2+?vf%`$bKxfTj?4kxN9Z~KW'
        b'(tiQ@vx9stF3LbXp2a-cg|fTFx2!x1#(X8{<gKuy&yN8+F^*owm^=z9h2K0-3&KB(KAC)Wro{-_jWV=+#cbJ%aas9{*)sAu%<^2U'
        b'+2^vBmrGg84M#ZdTTe$i4xz3OA-okWw|6gN55xRT&?BHn$-R_#XCABL$d2@bf7HS}Qgvj6?ag9<k=Mu$2c%$d@NnyxWgN5aMtdFw'
        b'4{PZsw==<U-y9ja2s!_LWMuC~a?57>fIpl}-1vi$80R}9C#(~VENeXfim6x+v6ej4(M|jl)B^L!KSoB5Al;Me5&oiMBcvdvj(8K|'
        b'uj=UNV285Ua)ez;;gQe)rTgy42>57=_kf}0g=Y;d11+rOh?}+Sg4;2)cGljJkxr}&`ax8(k^6`<j@*F1{atW70A`enbn-y?yguyg'
        b'>+t7w?6ZuEhpToxQepjbJ$N_FQ{OV#=K&wZ{3*nI-Bk&mfM>OWIb2FS0Q33UN6nUt9y441@hJ8Gk&(Pv;(o3BYNLG)+^>He&jR$>'
        b'N|@V07r^`t;P@x#+icahz6JA}2=gNFEl}CF!G}P<h1+ewUxV(VG`?fDgh6{iXYIxu1MP!*08}}ZSv|mAa2p0)@?EpV3Hy9t8E^pj'
        b'4d7JJlQ5qJT#5Pg0_xxeU5K)Lcdw8~wGd_}=t0>3F#+X%%4k1?`rq*>evhpGUf=+z50ux9@ef=FIsjtpuyz0*Bwh*H1L^`T2Sq?@'
        b'knZzH_a5L=p!YxyxSzcTd<*We@#ufpr^4O~a}97I+%Kc{gL@~a1!Msg!F><>vw^G6K%bt?tS`d;*7wbp*I<7hc=nl${SI#5g}D~y'
        b'BQWnEf0&QMd>EMhB-#gQTnzj%a2v=Ab2sp3;~2XU=G+{{b^<pe?sI6P12F#-*a`bZ=<CC<F94qLJ=6nk$HAND!dwpXe_>8s1oOkd'
        b'DDXw#1#tfp%$dNxeHGU6z;(!PIr4iQZGG(e;i@U%!5JV1ItlwpJYU?vBM5ib56qSVPzmVSmn*DC;XWVcw?T_Q8$nLc??6Z3_Y>g5'
        b'pn6abh}H{4rOeD<At+cMci|a$<Po#wA>gB+S781lu%m-7yMJh4d+UzEJ_GJvP(Jz~7v#Vk`6=w3pnlLDpvOV6iOf0!{$I!Qa3!AE'
        b'3au3|N1h{lyV1T2l>3g!{u|hf;r<Wc88nCX5=%R4?}+ILor^k&UNh~%JguX3!`|E$E2tL4Ky{$yAUDVh!hAY5GV%jTAnQIl`S3F`'
        b'(q`x62wlSY+>_xCXmu!Wr>|tR5HB^hOd(!`<)j01eHrM=#bSN9ZNWh|5&+jFhFA5$$jH+p@&+Ba%E%u<?_qoJ0l)dvZ(_6x{T$-n'
        b'0lEv6jk&Y(g9__P^y|a0AEo^X9$deNS*ZnY2A>H4uLZs80`GZeWF-INm|JkK2Ywd#S-1}YcLP_!trO-ufGdedEy0=*^m$Md?9Tvg'
        b'z;}TQ>+p<&IR?BKI0T#wJP6DL?gPC8THG*PH3>8wGzU~F&*HVfybiQ4pIL7LZUvQ$ue9C`+zI+R=s{33>Qalj*8&267}*84+D5GT'
        b'DJ|f8z;l3o;IHk#z3-Xq>=mqr@+++m<{>ZO9uNtk@gmH#)0lO+IQubjS?_i1`|jbYoGXT_-UO23sXGvM2PpGBJoHXrQ-z+G_TM8T'
        b'FJBBs{@0O_H!u(X2EO%V({R;l59Sf*K5+SiNcY;$j*OJUUI!}0TKYAtT~30s@vJ@qG-09bh5Hvl8$k1IY<=M5tjetQ?I$;7_iu<!'
        b'Ydg7DVYk>XIKt-pS+22Y!Vml>r}@Zn_sQwc8>SmSwrg9)y1(ptByZ>m1+F_!PPb(YZO=Gz_k?x79{NV!z}Lxj>&ZuK83SL=ICRT|'
        b'b>AJhJFovPa@}-tyDg*ta~bQd8?<E{*fe42uDt$Rlnu6w$xW<(Ln#bfCv2-ZIZzlI=#TYJpP+0~29#bleZtVDJTe#dZn2*1pKcg{'
        b'wNOD38Os07%TG?Lpz>`xvHk4j{p-y`TPJLI`1}30<_&D3Ob0K`Tlf6Hof${&LV7y4M+UZLz~Rtc6W}&Gd-5f$|B_Of=KAR;bI+r2'
        b'g%=I+k`H!XM77G^zJm#eyRz3`cydGGtV7vM#<87$@{xx}tUHu~XR{y5K#=7|{JGp1cqMzbSq*cx40Cumd&9#cYM`yg(oLnP6t%qZ'
        b'p^So;c?=4lsfPb?Hq{WGrMv>S7!Us{TlA6bgA+S5CRb<XnpYT>op(m=qTiaIGe0t9E?Aen0u7sS=#dGRT#7%BKQis@6NjFdpgght'
        b'cW<58_Ky?4H9a-Nc75CSKyUW!oUdgREY5l^C-=;UjK4MHUQ^JQU1-=`o|{wfijm6B4q@cHKf)&enY}t>D*c7>oGJIJ!@b#;XXMV9'
        b'{M7roIf4Jq+CF4h|H=t8$ij?wrW<l6mQLSWgB1^zaoT|swqKn<xi?HdXM>-?P(Gd7cSGw$YjvL8Z{RMI*Z=%P|J*$5T&iJt>*Q%a'
        b'Jz*cp&NYp9bYv7v{|cLB8b9p^C#FxI5_oCkkdfWocILDvVV#;cK?%G<E*BixU^E`uG@*Ze|6n2VGTl6G=An%fKECOSCr@Cw-FoAu'
        b'<?nW$zwL<=#hafr9{xJp{O9dPwthF2dHPcaYYvaFO=mCe%X!Ec7-By@PRzM~u5uHvgN-RlEUWbs>mNFidkJ;fCOHl^aSMk2U3r={'
        b'_v4Aak0<zU`_hR7Z#0~0Kd1HT^<R)VY?Y2%xh0;1u*P$czK<vPZoBbBf_LtDs&!VYZ~dob20NwWPHu^3Agu8Wr0?SizT3J_=)4CD'
        b'bJQFLJ98>fhxQY>MX(j_9+*z9MZ39W-LD3w=V{hlSEBEC6MVOLPb7Hfo~v4E+}qf;`V$+5GSDkScPme3ufFYur*hiIZ<=*)Y!`a^'
        b'mg$AY?Nc&4>~*=f{9xgUN3!z=Zc$cmS~ESD4GxcdXYiU0Ll;fE^u%`x>-nHOi;cJT_is7$-3fQ!^Ud-T2kruHUD4m4F>rTA|1G6?'
        b'U{yn}^?zL%QjXr+`tG0259}Tp+OAByfJPt2-A#;b|H&bmCp@*hX&0UVXW?mnGxN_QPd$6^$9U8eUpeE%mNQOlC@kN0&WWtf=`^KR'
        b'fVUA>5z~6bR^#@EzrSIe0@n>Lus8}5Ob8OJd55R9{i(de$45k4On#MZpPsRP9F1hS2i_YQ5Pa;-<6GW5z9D=6wiCy*UZ0jWzq%Zr'
        b'oibW>H@zdqKhn+mebxj27~%Y&;P?pf1I+DBc6Y|{!EB|pG`8;8tYAiInJsrpX=Q0?X$GQ9{s#*j8KJ_xdK`r#IXh*)JMNx%Jda(v'
        b'nq^l6%@6!-<fivVOg47-D1|c_SotOAS$7==a{|*DdR%$Pxc)_on<?9H&+)-+Y{NmrhU|0ur<bn(?(wYFSu_$02e-3xT4xC34mPWG'
        b'8aHlv`gld_h1|&NcUNWR+anx*ED<&2So7`((%)b-Oy0?Iv$q>f8|;R|$40grjd(a5{=RJME%zMX_O0X8(M7})hB({a5M-MNw-2$v'
        b'lOwq~54=4h`F%k!dtuJzD{}=8o%WUEn~amQM;=(7RcQR`;Oo=wKb||K(5O^?ezxhy?@-<a9of_FI}VnwY*!Ai%HHy&<GIB5H@Mig'
        b'dygYy7-;(CoPQS;IA_aNxU@gen*EURa9_5}^MMm1>py>dQ}*OSCLT_LcNM%lvh;DbVQ9+DgX1thz;kBjTySLSR(ketI-Yyptb>2s'
        b'@Kk?)f9#!2S%X85<(_x*ul_&I-UY0wBW(aaw_FGZO#-F}c6)Ll5U6fLuqC*4H;IU#^(#<~XzQ+kLA2XlwY0TecQ+@r5GdW{Vk=m?'
        b'dlF3rYFfZ<y_H>pEwvWD743bsOO<fH$z6+{f99OvWw-zHeE<JEJd-&y@65dO&O7gAZd|5YIzh>&z6QA`P*TRS`QkA!25Qtg#!*}H'
        b'm&hy!<mT31qcNXc@IfTTZld(9UNV#<bSVXCOCd*CawLmGbP?1l)o<ul8>no`9&Bd+hG0gcv3&2Ck=EI0xk@RrTBPY&u;c7%D$Px4'
        b'GNm*-)3D`6^cw~eqn{2XmGqN(Qt1&{cSw&$#BIJ&gC9Jl`dmWdK#O^|Hlg~gh3@;sX7$2^5W<7|o&^-A1GgS+%zfjhq&R!c*6cv5'
        b'<qbmrV5kSxouPDbHfAm4sq7U<TrwO?1Fp{sU5>SObN1FwK!vCJiV~If2SbYz$?&R*r$b9lXRkq$|ILxA>^0Wp%iI#N_!4)SXeZ<i'
        b'lyzKGc$EXjlK2YL8IVVnH+T_yxBXCoQEk_GX?)v=sK^U&xN3Iau_2h48~<f@+%6}*s~qwl<--5}wHK$j;lQDE-2;LYEk*4Ezo{v!'
        b'wn|KafH&<)0d0VgDR_FojX;{gZ)^w&ESKD1&>Q<hFc1P@vld~98%8$Y&a<24+gawOfGxBQL&K}f%J%I)AR$A{DFNa^IL~UNbv5SI'
        b'fxHb>*dxdmX5_ka{JKN>--^{ae0@%LGCj8|t_~#wDpCS?8;SY;`l1p(<3N=wHSi7yj0p(vZShkO>Wwe1Q}y}GH`f8Wa0>A4|MR-@'
        b'%O7vQ<NDpYdrw)}>y}iGCv|w)zNMDpTbHf~fM>4XTd?_dL7|Pf53V=9+g%ZXP;5RgJ@9(J=)f&IF!waaym#H@TzCh6eq?G>V1mJ4'
        b'wSiRfeI~=)6LT^KNMBR!buhKe1iDHu+B*i*JI#vNB=zCz=aUp#Y_<7Pgo{8JH|(-@9TiKkw61WHQ@?dR@QE}f5XG@Z_6GA8n4KoO'
        b'fw2AIu^(tKaV!!QjFJ(VNonho5=8Fw%Il<fyU2rQgSz%X;3k<z%v8V_tiBvZvNEq5L<#$1VZxta0v#z58q5fh*$;K<31oxgVcj8$'
        b'*#vXNpL0l?dGA>3G>0$+FvT!M20j`aNCVlg%D5Hx!gW1}9J&FOUd=kzoy0r`p@3R|bv(=0afU<mXJ&!i5$Q53({%ai3D;rszk!*K'
        b'b+!_Mt<fbM2!v_dVOsLvIaT%$vyIQ6^fxC(RP-S8<aIlU%=}R3;dM=%<$4Tmupi6;cA^<WnRT!TsU!p0#!3$XP~^t|*tg-=UG#mO'
        b'GK2*Rfql+ar(kKyp9hbB24AmL2mmxHW^K;_>wrcjY}IpAHHZ+6D4>y?t;w&igANKP3nY-up#Xzwqv!mbUD)-E=#WkkLW(vhQ?m@$'
        b'Gc5;wq_o)LivAs_I7UNat5?UY)T&ZNi4V`(H>z5JBfi+-5x*sUzIb6{>}P?Fwt>z}MalZk^@@y-LpND~QQ|r`NJj_jSrk|?B$gIY'
        b'2^xda5YsJf?hY2mtV|x_mf!|+X(dR_!?$d0{<8a4;>wNY!fQ}pnJ&-RBSQd9oC~fuvWPtvJzf>8j|}E1QytbSMw+CmZ*IL7a8_HD'
        b'5`FNR>ItMpizgiHRR!LvUPI#AO^MpXl!S`UiZ_7@h54C&cE+p;=_C-6Sfw;Ew`Ni@4=yDGsxxCEfjgR{l_oBoZAq0T2Ox`!Z6~O*'
        b'TI%_du$Biu3#@LN?Mzi1Na{>dm_G_#ogyCRkjBpjX-#m3zkfyz?B5cp!)$SIsb*l=!#;dBV<rx$LL}*RcQtHeI$^`>godkt7D`+i'
        b'lN4S3i&O(o*Wz}mC*b*#g^i10!vp`>a7!C(7d9#*l}1-3P@TN2c?;8~TI^hEY9U~FqzMO#dz6ECWFh4r&p3-_=m69nfC#=X9e@Gr'
        b'0`bT3a%SdU-!}^ZW<m_=6A^09j2$~sB#W<502S{lu~%dw6$-Q>6V+@->`t_(1j-efR$juaD5C!DjPsot@YTrEWlk3yoM~jCl%XRO'
        b'$1$vxLe$n7r)vh-vv7h3W0o+9olX?Y3U>}@XR)nLe()Sn6Dx3cHWIaZy`5H)KXdMz0RYx#kV1Hgue@T$9)SU*D_GQ4Tj^SXTS9NT'
        b'=x{h!*okfZP}J#ziLY{E06ye9&R1ptM(RR<ov~CYAO~e+gwk^22CV++<Q}eQ$7KM#D7<wXj$irS88A<v;Tiz7%ffJn&9<~CY##i8'
        b'Da8SGwe)H!FE`6~|9^nZ`@h3dx_lsxtiR#dSW2}Ffl}IoTl2WJGF2G2n|)<7mbH22g-R^B9!WTkwI(5p_Jc2R0g{mL>!`~0<dKAg'
        b'Ww}pag$Iz_0xWq1$&JUvrHK6uw8tKuE;=sV%{~AM77ii1elbIa*`s4h4IUiIL6#`&K^Coobx$CRiokE-9%MHg^g?B`I&o&V5+kvM'
        b'ZCK%PL>Fxme*khA*zjwh;a}`#{|Mr(7a>aGy~tuvNoo1w8Et??KdZhvP2NY-kJ%SuR1~q3*6n@aJgwNt^B%nsOYQ~SyPGY5%@u;W'
        b'F!2S%ZANmx#acf?)Spk62LQH7+Z8?o*=ZpG94Vtiv6GhDcn^-=NT~lg{a7GP%bhYf-i7=Xuib1F?BjzVQuabTmRtiO#Sq(Fpasir'
        b'7Isd&79=`e2*$)Gxb(kIlVKTOVD<&l#iBHaoD|tM71Xa+SfnxKebc+&`-jjtWS@lu=mpS0>|7rNED9Hc+Fpg7*nzxo3@iK-_$&pL'
        b'x3b(W*YxiDWU393<zE6y+*4Bwq{mKLvD?G74)AnvCL}DRSvEQzYyCY!vwulw#9Dug05kM!t~D6syC9wa2Sg5o$_tCRU4Ne59lb_X'
        b'^b_Y7)8vEhdM=rNw{%zWw6k^E9xZQV;gn-Ooi6`$noc3;JcLd~=uDiBP5{(eLbR?x)PI;3X3@6(Va-RJm|v}MpW&FgX|f2S8w#-G'
        b'yO~L}j&V%$G^kO%Yuc5)0+78B-j`Lg(=cC2?7#AkdfRmQj%k`+v&%D0{gg1;Q95RYFktld6?BZ83{T$2kt@YJfSx`yz3ULfD@IDM'
        b'f@rCq1SKJ6>M9U<RMj%+QzPKB^>a?We!AgJkSK3`nM==@X0}d)0n1n*CBwjgZN|WWvFqh&V9d@2mG1>(_Q!iD9Sz5<j8=#%IJJ4Y'
        b'VLhy<a5ty^1&I8VdWcZDI-IXelY#Dooc@dt7yuGoQKdZ@N!v29T>8QrSmFI#+_Tg62<;1@BH&d33Pg8f$)TM3p=sySurl&Ni1nUn'
        b'Qj}rtp(CPI`j2=5C(j4uWHP6B{dQWQ<zuqj)KpW`g4Zv8i-Ti)oNGM*iSNPPA9CU<5Z!g(G#ToOHj@&zsKCbNTTXTDvP@Uphml1)'
        b'tL2YQzYx59H~WVdg4Zm*5AZ|s0<N@nmjrOcW7~Q#aXY7$PLr<!<irLJp~b)oI-|xxlYdaPw7|I%z##zshbce2ms8J9C6{nysHzy*'
        b'H92LEe#}-#>^<4(P?W8g+tyQsC;aPIE-K2NV`rt&hNaBNlxjB-rCd`!G-Z!j0lok2E0~z+3hhrmi~)2Eq)rsnQ~7OrR$F;g*%^R{'
        b'C4e6Dri+vhGe4a!s`!NY*OWc<ja9vWZv{Q4^Hx9|V%OSxdOd}+9CLBXrCr0i31|noC~-I7nTu0)p!s@dS|^~)W_~iQo%2^si>84^'
        b'OtXhFiRc5X43RW0n;mn8PB-B#he@Vu3R+x1#mJx}#yuh^d4uErG35xc=RB;BFaT2{hEU&_($ha9m8HRcn+ySV(h^zWtly>p@>$(D'
        b'1w=GWFZ~dzl_j#HCHD9JSW-YPBxSbR0@jw_R;52<*A*Ao3{>e^;KH}P<Q$)ZON)cR(snz!<S~Jcnh8#QZ7TgQQzT(FBeaHIE(4A~'
        b'sM9$FOjq}BIMco<n&s>v`=YDD)t^iWinnbn_v%Vo6G4WPGB}Ds2okkoDQF$D#S{QNV^QAHpRws;3M}@UasQfX!T@J&=UPJc!I)+X'
        b'r+yz+<T8uzAJwxQtmsBUsL1>|>LM1A;f4JIZtDM?GPI~xDB@n2@?iRiC_oJo*P9VNjajbF*Jsa*`(!F5*n!8jP8IFLT3<y{uhc9x'
        b'M<A=h0!=%nTseq2QUeSi!<CdALqsZ_(vq+bD~v!YFx-yoY_&R<87*3f+0FRDt!Cm8J^l!i6oJG?B!ozvjgVIEZ#Ymk!m!mIvM^Ck'
        b'27{*KJX5JHI)hxNn<!loS1@INVt!*}pz1TkSu<s35#JWh(2{ygPm_%iGSz9sc?i(e{VSMwD5b@4At8h`=yh?X#KuHdVnw2z#1k)o'
        b'CR)xO`&6l#4RL)G@)ky>Jnxu)LRRtVEJ7OV>&s6TyUxuz&ZwjzjS&)8<UDBdqX_7g>gq^bHl(9DLY^D4%(P_66}bw?P|1#;l2GQD'
        b'bL8fT2VD`dsTa)=OKQ)UbLR8F3RlEpJ8QEgQMFfjFhz|$#ayLdT~})-rAJOKDywU*wYxCf91#mN^4?i8oc*w}{;&;*ft=Wyij)ih'
        b'S#jj#Pas?cfFmCSmOf~z-a+|+PaSsUJXn)`bVrH{z`FdfE(p7Zhh2Ox?Bbfnl-&Tb5keklu5JWlM7~;I4Iq~QNHT2i4`uIE*6pjv'
        b'Sz<S1HY4wH1{25gq<TD1w^Xh-V+PuCMyxhZ8I;iC4^C9Jsu1VOsYT?g?=xaJ?ULW+92Zq522T{!bivPh4)OhyOKCayzMXjZU|vm^'
        b'IZV82>wHt<6f-z^Vv~JqaLTv5`J9S_;cH2}p#EagshEOtb`5XJ1;!`Rs$(;)v(Vn9bQ9Cri(bf)J42@Q@BNVs*U@soLcU*cahfT8'
        b'FakaSh^i9JikLD@PG+kRdR-bR+J?(~r@5#bm~S1Jmq45q;nu9vlNDcL6$_<B0UH@&$}a7(NTHyxhY;mACWVa^`#OU0O!CWy>m<FH'
        b'I0>;H=Tu>+<~SF1E-*Vv?(CUtWR0C-V6rm-u={zNvQ^?$xe_u=AV(H9wGCKjiAYx8B=r<wT(3y8P{1Qb$>eMkl67FR2F;EN1r@By'
        b'p@hwyiV#BQ(AoY>WWP7k>`-jsx4Q&fj{gYEAIt8A+3+JU|6uQhF<qWC#>>;<DKNiO7l%zJCNm<nr4M^BAONGUVuc@Y>ikJ({p6go'
        b'bN+pj#5I5A)Tbu(K;=b7tLy_%9vuY&1QOxx$;Sdg7sMZNJvqx@6Or<)t&^4+)P0z<v)Uq=3P1t-#QEkV0Lx~BvXiQz1CEe@hRGgS'
        b'Hu)d0F4ndU*KQVrDzYQxxhkcb<#J2Ntn|qy8K@z71i(072hO*T;>5?e`*MP^R!@?zLKI$^Y#rjrWI*fIquge3;XD2{BJ*Uqd(x#{'
        b'R2xu!c+z=zvLbJhU2A}bl54V7u)|G<CWX}%EkOo`(}1m(Eh87eO#@;{piWb;9HY<KsV6G|y^aSzonAEwg|i4Qj~=gxRKGEqjUmV1'
        b'h*d{SI{yqPCW+Ex&es5rZWSB_*GgmwT#_*mf$?x>j{u5BT{1~yNa>ifc+wi;2ZBo#2<Sx<rU~Yjhzp_KK-4czYB65%6b=jhiQ6;D'
        b'tF&;qUQ~=nXFmx>3Q`<HfYm=JE#Ey^5r7O9GsvX#=}E_)C<Er)0az4q2k{M=1;+@npXK-p?jJ4Boooz1N}q0$I<1q1lbmzwq)*0y'
        b'2xy<NOnNY3jV}3`u#W!A$qFfQG!?F-A>~g^y4bRgCnpcoky5hw`Qmvcr$DVOfylQfTGk-p4xp)|6i|+~e2Z2Dw4~)MpaOZFbR;BV'
        b'I>t2WP{chpS<*-zjD9na#Ar}N%j@9^94R|&x^Qm8kw>u$=X7OdOD~ua*QXoyKZ?0Nh595s{y|zi#*tX^xUg5)ge}G@P~Eo1c^!sH'
        b'Z{lR5Yn9V5>3b_+e`8Qb!lZX8NJ%M#_Aaw@()lnX*^Cwrd7f848Kan6&8&rKHF@Oy&HRRRZ65q|cpsene#vBWo!lEU>CbQo8Bs8`'
        b'-k(I0eBmZi*HlTJMmy`|C(-&-Fz+N^&z^?+Cj;ZR#G^no>z2XvMA&9(=qJ@!^3Rbt)uaK};|rIqG+rtI>1Xpy!IQensIg6cz70Zu'
        b'nim+qY(3<qJ?8hC)6&+#Is637*$C?~<dFoqz$uyBvaTR)J<9SE95#}-N+rr}<+d2%lBS_5`zW#{UT(~RdE4Pm-|jpWT*%EMadJV{'
        b'>4~x@3XJQ~ElKjUBnXn4m#|Qz|CH0|VDXfijH5_el3cfxuNv;-8KkDyC;Z#5dHgz%G<tm60BL$%%eN1w62y?!s-iv(+B=RcG$NJG'
        b'vPxj3%l-RbhCI_(pc45UJl{qC_ny{I_&uWwERvR%pOJ;=#wlZGetS?;5SX``P7W@T!1YaX(QC~gQZDwdnwuQcI)TJ0Y_y!UJqP>|'
        b'=FEhxPR`z57h{?ys7A`AMXW!Ol=0{1vk-k2V(kz+Pfaww$5}6mThvJ02NQ4n8mYmXFzY;tD*|~V2|pXwX;*X}RKz;YRiBX6S1W+Y'
        b'e85riYQwt|%}EM=i5IJXUv7G5!k8+r7bvK07l9grBsF-u7)0bSA_0+L$yqO~+!reGVD2f-`l;CY<^;_m)_;rrcv{bjv#KFNTi&KL'
        b'=ftCS(6IWA37{7?IjWSMaMRNK5tmB@xIY$q#J+!la$0;1lr%BYHI8I{t;&OGR1$xE9?W<DT-^D}#A3K6;gBr~q)rw917HbU2rriT'
        b'^VNTtpt6k=Ma=C>=@2%S@`2EG;e3gLbu^bhKT%eru+=qRh(VbAiP1U*iPiT*ad%eQOzX~n)_mmA;gftDQc62_P9pAU*dbt7Yn8qa'
        b'#cjJixb-~WU%L{K^e%8HOZok0sh!4(0>ln|jTx>$X8<Qau*)^a#c`YbRrpSb%LeeWw+JS4LT#BSbJ#jl6&X@wHLb-;7iiW8WUy#P'
        b'3X;|Z7tID_%;OVjw0yNAM(S=917rE@9G!g)V)e=iVGqrHOk6*J*EbR6NfVu~Ds0s@#yC+EaLNHBpCtzIJswcOB0&6EeKPC2VlZ+a'
        b'iFy8O%ch;eo}KTgI8N`!(EYC1q5M!=5sK{XXRGBEnaBxg*=e-?M4T3T<5jE%W4$X`R>Z_kzy+{cfR+0nViFS%afkyuA?-Y^Naj0k'
        b'8^CR^5dfSL6;-^>I#)73fhC}#fP1;SWp1}PE(A6T=y?RRsp=JhM)@svzEKBO-;nPJMNUVwecd6S@X9Bgiit+osC!L7m9(rHEvt$<'
        b'UJZ*#w*TCbX{oyP#+$enBYzE=1n6NrdVdwe9{o)WcofVUKYpMq07Zz=t#JU<I>~*x=BAxSr~#Z>LV!8O+C<Tz-?`s}6mJj%B8f*K'
        b'U%C&7ca4n$gm)gHtOvzFpXzk^Mq@sh<Xg7n4~Z{}+KDC{3<%Rd&TqR|_lrFew`Xq5+;51pu8i;f!6UX--BVg9=)suFu$*Qem>JeO'
        b'VT`PmV&@mIP0j27+2GEd`8OqVt%Ab;3kzGz#LiF0t#8k@$$SP=)n~`4So_@G5Yr0N?Cj&}kH?Q_1DO^cq*(v~`MLpIx12~&$~*o('
        b'?*03?^Y7z}2Y}70SsK82A!z#P@wn6DowR~lZ=>REE)4?ldzpv|!!$7gyf1;M@^1mZ2iipuFigcw_2aQgAhw4vy(`30h_)`~==fzK'
        b')=?t`eITq$2tZk2Tjhq-ncf};;*(0U)eul_x*sHxeY{WY8YcthcDmr){OdT)5{?z6p#ZT!T7PCX7aP@xM4E^F`(RZd9|hAE*t-WI'
        b'@<K=kl3~_jj0|+Kn9qSRe;(&05c4Ph?`!avPC=P+zKjqS`xE0Fd<2IU)xivbYk-hd7mSzCy!itO?P9kwFT-Mm<IoRqK0oe$A0qK*'
        b'fi>VUqEZ-j{(jv1yKyp*ZEFS%fP|<Fx$~uQ?;d{|Ux#zS_+qk=l`;&E2p>9k`P2TucSy$kp3mdM(lF~Vr+#oeZu@xp)8o_%d0gJO'
        b'di(gYr8?bY=OIO`rtvVso^CeM%@j4s?1Dwy=TK%RjQFZB-|u8h24CB+h1%SK0lS_YH%pMx5Z`vplsry`df;g$dlJG}d1gYTA85ZO'
        b'!+eK1CVgBucq2Vhyo~>yJ4?oY@IvLz=j{VH{#^e7oQgceX&lc6G<*nF4=q80w*(0k7-wvz9H<v&G0ajexCQabXOj4@Ws~Imj-QTu'
        b'9~>W=4;K}fU-13-`CZ|1p50@|Yq66`W+D8D(~g_8a7?whQ8=7~Ga)d;M2?e666yy!i9gR}LYBj$Y&6P`eYSt>^$ImHzU<D}`$0jN'
        b'!D9`;0Xu*aX?*RpKMTEG)9rL-dJM8mHxQs#aD)_DIwe7<vV&84jR7X4BNge!1Jua-cz^=&rnY3wzmO$gxgSS{aV%>AED<0&h#+0K'
        b'Ni>cSa-=Jm+*t_!i6A~MMcQ=amSo_;q+wYh$me)K9C~XE=?;Ddef>e?mA7!I8hl6<$os+4xKNXvLI8|>DJVNN#`^E;?Y-f)%g7)&'
        b'A6;I#`)i5sEJh#drB1oLLt`D9F{;ka{4gf4w^#0)CvC^TFS(oy)ZCD?W8_-+6>hyQA;V$$`=u~cOV$4#d(~;cw8}&^orPNirLQ{O'
        b'3J~}nkgC5K^PqedN@t<I0I3J{%?E+zCsM%h-@~?m-}-O(>kq$!p>Y5=t|dr}4Bm_xpD6H%G<!LZ$odkO-a7UuWVB*Y`p09!???XM'
        b'GydNe|F2j0Wtzv*o5y(GOuNIVKtg;tmj2<7rJopkO!Onk$Hqv_e<lNV{~~RU-Q9tB`a7_~7*X`TAfR}5avs9HlM{0sT-4NnPt5ll'
        b's4IWVuY*H-=kOSRT$03WwxsB)5Vdn`FFZT|lwc@DB|%5#_W4nPByqN}(tSW4(klc$1u{%!=G6Pf;7Ocu$psc|ab+6cr+@|aZwa})'
        b'<#0V2?!m0z0dr4-NP*=bmYP=}$)kQ>wP=i72<!@`a4bg3AK@vMj+*>B#?B8114Ah5Z2Tu53g;RA2&3w~W4C?5(iG-*0`ykq5g38H'
        b'<-)oqKg)dasHFt){S{g~nx*KRjdzQKC^FBC-8t{!o8`zrkd}9M+E2tz>zHrpZTsndu`_E7=q>jHV!@t<zT#N<FULykMJHpK&12=8'
        b'`RD`XPmMV@j~%EWL-(HwDt~h901blZlbD@FY|zvsLz8d%>0ucwx4=S)VybK@8Cv=c^Y~bK+E@uqhDM)6NvTaRO$EEQ^jYRHKZ48}'
        b'zQ1$pxON)V(^$pX(L}5&z<ze3ny!)7Dt*_1`xqUjiar#mHjYv8a`h|MsCdeC=B9N5cofuJ-B}2gK>;HHm@VB4u)-Lmg_Y}$Q67|8'
        b'eGRG&{a6#>o90fSU!F$POU9_va`m&<sM8ev*-gC~Rqc~FW5*Z`L<m|kOJKwqJ;tbE1fE8Sfsq;o8SES7jvlB%zdVJg7lFAiS7%+L'
        b'>L}N_o7Mr2#1jt8)5ej(rMqc5gl-w6mK7`!k*Z9!N+dh_tTSW`aG86Aqu=A4!4RQgc+kT+Z>$}-7mNfpkqm{P2Zf7e!vNbYbvjm;'
        b'4{%OL#?ns9)03~Iou)EAySW?S{5kHtd5xKY-Ai**48r4l;~FyoQ#=x8_8M;-SjMI;@iUp~CAjL98Rz6RU~%+t$^YgM=jb)y--wt#'
        b'2q&K80Kl_T;xD1z2E=P*5xJ9MTrl%h@0tc6ekhD2n@}(*`sRE&fk)%6T&t%QI@+dZ!Mx;clJNL7bZ)`5xpB8niJaeFJ5MX1>0W2^'
        b'O^XCOrUjc{{>8QCW}@>$#i?3{>{4iPc8sicciR&+*a@X|9s*C-^<rNuYeJ7Kmwa^~vPOF3?+?`MDbB9l9V2tKgx2n{9J+a`+7J+3'
        b'c@Zw+za}f3;A-+Lo4DHSm^}O0(Bj>#{xgo6VUhDB#38oMhl_>t)y(m0z(xkPZ#&wA#h|`Ckps;Q6#*8o2F=YOD}ltldyS4j>=7sx'
        b'Ya@e?=ur|cIejYLf4->Z8o8Q3)?<$e7Y<h1w}&%_uFb8<%=vMDxkd*19+Ma!MA^e8;N#XWHQlC9mngmJ8nBT?nr;!Z|JwN^#p;w8'
        b'A~7T-^lL+v^sM%)rJ_}DNj^DAlzmEFCUQwEDoElixkf&ySu3%2iaa9s)Z97rJC<4DHF6=e&EV=z<q}~}#);Uy@?wSEt1Cvyl*IJZ'
        b'tc|<2GcT4Gt4lLTN3l9LSOkq;DGs3FU3VPm4Sr<;h4-RG-~51x0uf{-yt&+q=NhrXe<4%NBT;ExQF7mpDC`D7VSjoJ>gz?ICLAhZ'
        b'L2GwFRs73qK>Hfvbly~hNe4<b;OW1(29$6byc=9b_2S?!&T>tV;zqhmXJ%6fc@}k^Kt5LA*4+)ab+-=ru`~fM9t%+jPBq{^(*xT;'
        b'QaKO7aFq?gnmHYUBUrGmA^4R=xUvIPdYku-QdA{C685|BuLzP{jv)VUJ%n8W-9(pM3qV01H!>N`oiXW&S*g3mvXmkjuKMQ>X!JE>'
        b'Cyt0%ApAAg1W$vCV6_<Cl9Grm!gRDfj=B~bk5CgpgBd%6bq}*z{5lRg5dDB%WuIpTKKIL5YXXvf-!&vjXU;$n<I1#ktXYX>ijXAA'
        b'oPla-M7MGiJ$uad^Q(zi83>fP84EV!5oRLZELvd}KVg>Sn5EB}0}9NtN^{^LGkMG$bjCdIqIv#RvwYmFXng?5jo*vtKzTU`loSYP'
        b'9SHPB5SY_Ikg){>**ih7+Xe!A83-y^5V-0=(0CpMEuA2^FbaYzNZi%LF?rloeYTu}p(4`S9@*U<x$QE%Zqj0l?7SSAH57SeC^F|}'
        b'WY^7Bj#K?JNdEw8`fgNG0K1FC>-4_@+_%!W0t|iTLz^OJj~Oss@3=v!>l?>0EEvNhFd`lkt-!=jV3Hh6`YaYufXOPcz(W{$3=2Ag'
        b'&AW)rzlzDnF@OI+c?6b6#|^X&8#m~6__)EWBgPFGI?=cxTPGej?AA%f4R)P$+)$wl7&o|dvT;MBE^yq?q6-=~T+q!MH(b%pA2*EY'
        b'<l}l;u2X<ep;L}WYT6^;ZjX$f>mPeLQau#u8j6g#8F?7?Z%nPsWKwn+vS_tP^aV#hfJv}^gq8zyczgMaPQasAvJ@*hEU$cz^MYD_'
        b'MXe|t<47ZXapFVt9v-}x0nyh+u`EQ6Qt*Y1b`1UVD8fGhLv`W0E4Zn2R7cB!m9M%$0C0m2PC276<xJV5Mlj!qvOqHcu<Yi-lZ;n`'
        b'7mXVyjK=up<^jC9ooJ3PGwmHU#@DCdOT>A>VE&2wfK+Ym;Z}Zz-Gx&N#HkVDbOGYDa}K8q!7D$)(BIsP)6;k1bm4BC8gbL|{~Jyl'
        b'eiSEB3kKvs3zP$mb8<kgzngYvAfCq{o);mWsdIQ<4F32ehOW97&!oHXym&XB$8b~d{|(P2KZ@ro$043)AfCr=;~9_KUW*_@vZ6*m'
        b'djbhIB1z89ctz)W#j@wCFfv@wH6F}3r)}IlVqg#lZG!9FXG57^kJ#Ge%$FlT`J9l{A80;UOsYzM_DleKfMOJ*%W5iiAla>)y9cx6'
        b'a(0^cFtv+{UOrTY%-MtiqYi1C7V3<uJ*CA}hW#{Am9n26aySaFbAr8<{`qjAdDX*<B{>Vok5&~#l99%E>Sy%cj{qga@YeKwS4T-A'
        b'eQIQnsB@j7ttdPxcj+i8YmG$CzR>pQo}$7V+@@`L;%)f2NAfAE`75fclb=Ns4s=O!o^vE*^^KJGkL++1CFZTkZW4RQYE&~VsX|q&'
        b'XVq6n>I!3bY&#j$ab?7NW#rK(omWQO3#IBSBeB}(lYt%Ik9aSSJo+@ml%+ySD>^QZc)uBW^moaVoXr+eTGjFGi1&+;M_*08#;Ly<'
        b'iH)tr*0`WS13YKaH!4wuO%?ti*bKmegm(8ecyzt(+tNnw|BmpBPVJDiO9<Wuiu-ItAA#iJ^Bc~Mz-7r<j$KAA0s6C{btL*2*6=Y*'
        b'^$o&Q%Z^(r{Vmh~4tp?Q{0(r+WtP=9y?-BRB0!xdV4Y%N|3-BIV@{5g*N#B5T12<Z(loH0t=(MPw;k_~c;6p!zCF_D%(Kd*H7_+`'
        b'nt{2s;>}oF1*i<ybn_Nk+c99Q{Q&o0cq3c={BVN)n)=X4R^<q#u|+?kray)?llMWqJGp0MmN25@FC*T+fXYjpuZ>s<DX=Vk-*M~?'
        b'%5n<n*gxW}0$G*GGo0pSV8zIf>|5@NlIYG*O(JWL1l}2#`8@_~T)5<W84^tuHdFI_6K1&&0T34@mts2{Bi<rVM?*3^9uCjdk8|vq'
        b'oV34D#={izt6{;I^^I^#2=PBT!DoOgeVQ@QqqhFiGu{^gxu8Y<>ybOQ6=kN>+ebiGaxsNBZv-0tgmspu0cgaVGm_AVfe?%x;T{6X'
        b'mQA-*5x3Hx9&W<hMWA8pAWW3qgfJox&a5A~b0<ZY;nHQ>N$k?YfU;uic>q~j(k=#u^S>arZC3zJ7C%m_?!w8GF#=b42~DcVfwi3g'
        b'F6=zKEzH_2ab+W*N%xbYGJYOqVuR25))Tp5V*gbVKtISaKX92?+ZP?C5wCf~X&z~08S8)q+GbA>QDGP1lV8-*4>NL;czf-82^rXq'
        b'dPFBtYbFi|6=r$%mR^mho&b&|;@-jq(qssUQ%fs#)RtBs2N@fXIX6jWO~=_-Dj7PR)&!jA6M(zr3epiZ;*A<{MuM?=*mqST*vr;6'
        b'plySTMlAhE2Q}iQMx5aQvs1qBCH38Sef?6^XK3yUO!Kt_xB~J9DiO8HaR-_Z3V70*37nnW6=L@d4Bjrf9M~S{zKkW`;LqtwM*R0H'
        b'9}($k<lsdB{tdQSR{Cv+bi^Al;>18JPh0;b@!;<D_(lv2<ElA(ms|wwW(;^=bKj5g-~G407eTk!dfR6qALGA!=e`?R6wdK6c&!TI'
        b'zX@T^`@ez53%>2y2pR6a;=d<!CvA=OdrqJY@RsN-L^CdwyZt>j_YDfb?|zQ?au{%GQ3av?d^iU6pmW!*Zo~L`IHr9Lrj3WOj{OIW'
        b'+s82<&B3$)7|<M)Q?b<CKAFG0s~mG`4(_A?2RzXKf&<eZcz7fJz6fd7e}go^M}@u`JIb#w+z+{)sTp=itF+a0mBA5OtuIzGhlh(@'
        b'ByitIsXhA<dv=07+aQ!n|LZUr>=9W3!f(N%Yh@nMGl78q%$x9Y_39%_fj_ka_*33XLmlZu9x&UPXqe^wdZ=UVP%YMkL)lOUlWK)K'
        b'5+1xX*m{E#CJew=Q-yaPP_VT&FfgNairV1f_~M9S+=CXQ_AJyr&1q4=Uu7qlYeUe<XD6B858u8+<u1p4>u#05IBe%v@9n7w^TM!;'
        b'g-eyL6h0*YF4m|F9Q3Pp58G&44d%PS`7F15I>PS<J_GApE@Qre4Il*ywuY+3{Jf#2;vOD0S%-CcTf+Ncagt%+ErT%n*u0LcVQ<!O'
        b'BU|ju8nyzjeH*Mr(Ep~*!z5f)a}cCbr>TsR26b#2_F4dNc`Mvd=MO4qlt6SSR8NRI)(v|f2YGL{4noPg=v6SDe<B(lA2zKVZpS=u'
        b'0XHKFVbWmzrQd$PdblHLxMB5h3+r}AVf-Sqzl&}gAe^<55Zta+!GRs7VQ(U+xgq&W&T78Zc}Ni#H_RTgxktH9m!j^FW|X_f_cXI8'
        b'nEuq#0@IRV*lHvay<lEP{IEA3RC2}{J?#67#4RQcigLr|bv!ie{V7QPIGMLAGWatw8wu0G;ZESGN7i7#?y+`p%aUpc-&M|v1NkFU'
        b'&j%a@7n{upJeT(KTQEdH4itsH`v@l7KeEF9=)z%sb&y{wg7aSn_<GK_@8%dKYzYh~f0hsNPewSN^I$Eez+u*9syj@}kl71h#5yw+'
        b'{N{e1C~kOA_lSJ(7(+lf02CcIj|`;@1v*`RTl^M7<v~1lDY+nH1rko{T}VPjGpIQ3`$0HrqGVw$b9Of~F(j0(#f9h+88hlnqU<Kt'
        b'(QMy}Fa!P+*SC)%fW4vUBe58q@xgR04q@w>)mMjVi5QXCf2SE9)nYF51v5<kNVbXj8b->$7+NdZ7P%<>;t(iH5=Rb4biS<M%}0l{'
        b'NNEU90@fKwIWU(Z3r|WO_s=)x>>X^<lA7z1kR(MaPAXx;=FiQ7?ZhBtK(%P2sam{0Snqs(sG(`7&h>lD&Z0+7V`aru`Kh6XRYM0V'
        b'$gusV;q^lYCFxZ#rlE4v5L|!cw;vw@ZJiz@WhbO>;m;Qbca|th><;N0+FNJC5r^WF6W@l{HPj6)T5Yv*n`H-IvVO|BySU5f8t<zO'
        b'K<)N(Rf>d@0q!q3+KGx6AxMh4qiSe%b$E5>VTG=`nWdYTeYF2DJOjCZA0~bjQI`+BMZ`v~KC^!jCZ-T|)zBX7#fM81K6|}l8<CNX'
        b'&{jgdZzxe?z)}~4$0uT1b)tw$YSyBl|FKCV=KCktw$vl?*(I5#R8b<o=87;c4RxMUe0!s0U~E2|u)Xt2e_P*ZI}zCPCJ|ou$+GW^'
        b'b<M!O3vWv}fVF-H{D;DCfz2R>lcC|)L!GsX`a0Vc43@kQi!??f2j?BX|KW~jhP=-VIe#<M$PR0ENRHnh0Z*^UYSdq&Y;7~(kcPaW'
        b'Z|f?uL@iljCJ&C**{rH`7lwpahu68x$eI_z>DG@q5?_l$+H~;eHmIEwa8otIi49IOn+KPf9a2Z=Dnq2Hdaz+=V0FB(iS{Y_jl%jr'
        b'97Rp8m1Q{5v*_1~*CcH>_*W3%1*F}Z*1agQ13O+jIwXen7MN_CW#DI*L@eBG*1X5XnTCMLta<{oM<CHv+p2;a^g~|VP{+bSN3b>`'
        b')=?BgIpRyT+7&S=+7-o^^%Q5xAvzL=ya_{%PNP`FKdA+Ty$rGRA{}u<-Z+r1cg7A`H%jbhfsvnYUyWF*kj`SoImp4^NW-fOdpSdV'
        b'@)ZtP5P6b0U21)svwHn318uHW&Y`YSG|U_F1`Tyg4IHQ<vHe=Y+6ZLAsT!9IY5TUbMscnV9uty%bpQ>g!yV#jzdyu0KA27pmc*x-'
        b'<+1U=`%8<Lli0GQ3Gb6k@qm$?Bt@%E;E+zhF3JE({$q~aM3sJ9gO(m>m>paqVr~t>UFPe9o07z1{xxyy`*?0FL55jdabf@9I)t&h'
        b'=FV3$Q-d+mx%)zmlrh7m9v;wQ4khg*HW(fvvFMOkXU{-8#=awGpKKmN*L1A@o9269`dkV-p=c*Iod(9PeE=?Pqd*o4cVn&$?){d('
        b'8Y5hPE)Ed%o6(rR>(byQ!Xfcs4k=V3n{<aNp%GPsIb?RNqSVnY26jBm!9BP^(j+qkdocL81b_e8?i3X%lcTlab|)6C4T3k9TtTHS'
        b'XuUoxu{(*Pit+nLnU4pfwF{Y#28&z(4hWtBre(0G;v3qD^BW^f^B^x@Xs4K0fseqg$!uDzK0TQJx4{%l3k*%>BqY*@S4wvP?*jg_'
        b'FeD~e3#@t|-T6a$gEB{Olh~mJ20O%626M?kt<r;o>@`VCWU7~bfHc)RMQlWY|C~8*6EQAWbJm-Kn`L{%9&C@KQ-aL)m%1}(l-f;Y'
        b'XhJQ|A$zclXe2`ej25`7FG4OYI~dZ0dL$s)R+54n(1Z}o`P!gCe49MH9m*gvCiTmMF0b5yIkeEPxZyBWg;u40*r!@SRArWKtj2kF'
        b'rV6vwP*nk)0f^<>TQ#O8)Dh-Lf$%Rm&?-~$Mtcs>bxks@vc?3u1J}fzI|mEl-j&OV3Fi~DkQ8h=1|+O1GBA@+eIZK;QN1i9vCI`Q'
        b'3UX|No|k@40Y1`VF$%2$P%cNz<iM`0PDw#uaLpv|LrLfel&0@LsDzZnko)=r)Zg`|psO0u7}S(L=)tvw|6HWy071@dFob3Xd+-d6'
        b'3eY0MDcx{DW{)83XJ<dqq8>1E5NUo4mdKLD2>Je+1~8VZV6%*AaEYwwK!Eup&XRu%j*V)^RPs$Qmwo>Rn5Yg+@q2?#Bz@^1okh?Z'
        b'1kjPDVcW0CEV1*orc7m?Rh7Fa^EuUmMVWM_=HP-FeLGQH-h=~O9Odv008&z8A|=|e%-t_6K=)MS*|(>w-d?z6!xhWQg?XD2KET9Q'
        b'Wc3ppz;6yxm0p%}#gZIaw)Kjo`#u#BkWJ4URH;J-pCLBmH6}-xT^nZ6k`AoKB<umGVo5Skyau5$ohtigmTXWf*80&~CaN(pmHpbV'
        b'@``@#m14A7(S!<oy1EKT*Yn${gCFFXnq&?Y`M?#a?ipFn+cHvC|6TzLZ=aw`0-5Q78dIhe%>N7x3cB-}Otoy9U+(t=GzGPbi_5E>'
        b'-|Xtky3PPdc(WIClvg>w-qo8m!$@|7p7{Fw+lsn(&dO@S*rT>1$3zW10~;Pio3QZQ!Y+;s1SLR?vEzmP92r_=+F1e*ik?__H1CB+'
        b'B6q%W<x;QXcc2{+0DEcu&fMlzkI)_84tW1H;QZG>qw5(BB5^$J&#y{9u)Zv}89q8eO38&yQubu!mf`~2Y3i&AxX1&JP!Cz{gn&*}'
        b'$v{&;dh<YgpjHI<LSJJVA}-@R!3xiE%;^E~Cmi$PK;g%LpMg9nJR{f~U=AG{0ArtrrKaaab&7$rVc9|Cnf9o5N6S@`Ak`B=dn}Ih'
        b'qT^Vr9@$j2AN=Z&qbqBGrplA$wSoe>_Vn+x=4{Wh+z>lVwP>~$%Z?%}xro_`!u6gS!-=eR6u>#qXJo}$svWoPjPY98;EozoN|qzc'
        b'_*{-%D?ghKWWZO{mJcfV%%ib)%}awx8==imxo*_NH;LhWqh1bqh7b>OHCPjIHVnX!ph)T4?UE)jm<0>_;dSQpo$H%laulb(6mR+b'
        b'2g}Nt)*;UH;z05@pzmfUmi!f@ffu2(r0U&(2vjzWWJh5DSHNTk=I1ex2ntov{5?^7q7O=H9%&a9dz%O#!W`bxFyAGyDt;aSvaC9e'
        b'B|m~}+6Rb}ycAJQ1`5>qy(sSuP*-h3YI$CRs+-7qpg+;MWm`@S!*hG7!_O&}ekmXcGxubGxQ01fZjVJzIDv-P@+Gz9g=UbxAwkoz'
        b'e!#naz?m`7c<43XW$|LEZCg$|v=~t4yFLK2&<Qj)&nN9t_S4FpfKS?}uNen+=|e|o6It!`1VK*m4#qmlcf{{-6qiFnkR(rJeGM}t'
        b'GJa0+3<IY^djK%0m?Z<^Sq`!bf1~b^?-6sB!W2C~XUXYEATo@C$WX@(WUJ*`ELsH#VTlc*)e4n8D9@4>VT=9%OO8i$)KbfCQuRt;'
        b'8i-_**=hy#td07>wsXrm%LfEyZML(&*mlDF7zsL42Rrka*g?3|a$ao$5`8NMAD6{dVeOKN7@!^OS@0f~U9J4^REKiF8$9472O1C0'
        b'v$lzMZb`cIJg9Kd%(fHq#U$L3eFIjwSlrsrA&X!G74UnJxV4)@_P|E=+}9)pgZi4RZO0CJLnBuB6{m&iTK$mdGER~p7vpt~%PHpf'
        b'@PS@P{(=7`cqa_{aV->}UK38r+~+vW%iP>s3P9j~K6jQt{aHV04P4*$+;Wje)Cw;-dN9TZ8TCkf0Ek}c=iOob8QlKftSw&N@Q;3Y'
        b'DzWaCs$@2i@Gs55^|eD3GY$Iyy$iVZc@^pSyx;qIzw?X!M)n2Ghhlg1Er-7RLcgt~x#*;<mZqJOQUV^)*V54KY41PMI6wxISnG9Y'
        b'XV4g2iZi}XSzHM72}A-I3#BsuS^=<`&h*>0=w0t?{G<P#eOliw?l!D-5wO2RE*91N6t_NbtCsfT=>CDT{^XV`8>d<1?tXlHS3j6K'
        b'*tUyCm>d|XQIZ&Qq3^DCvtV*9#(dVtFKqCQg7hX#*f(&#+0S78ci_Fh?H87#-5=ayV<}-B1k=2AYp%YEe!+b_4(nrn=xr$NcfQ?6'
        b'&ZjyjqfcO0oCtNg`2uSk{U^mZASm-n|K2|68cRu;|8*uQ|9Sf<Cn@u`A7S+O{W0=HDpf~)j>jO2(}WF@xIO*4tHHuzMd_iq=lh}0'
        b'DTe>|H7=izqtEsSARv$;>fQZXtQkSj9sOFlflAS#zXe(T(^kUS5IjmrMA0NL0=Gl-;36Ty<iTk24Zl4sG-Y`fH|6y6s~_n({czXZ'
        b'H-__<ybKtBi7*v&i-=WE5FWxOzZIPW25_r;>?WjBoTZ-!OvQPV2-f*FJ+C99-<#3zd;;*>bDG!1rnUY2%B^(>XCCkGtPtGbDyfIi'
        b'`HwOAIGhY^v#U-0{CjQpkE)IRh5ofuVLj1$<KFc|;n}7i-$TZ-(A($QK8`{Ed!Kw?AAe+Ree=yAVXWtPj$-o{&A>M+ju;kHoEu*r'
        b'=sGu5rmtilETAIf{DO!5oOgMkO<z#K{^2$JNFrAMAVp~@ipnpX^IIs}b5vEn%}$j$K-P1@0|apWz|W6!ZOwgaq|!8Rz(#CKM?l(_'
        b'0UPnO)_{%tAskYU^adjz;7CI-@+FRR1dFb5a`;bX=LY!;T+aVrhOcmWf>3AG?$-iJYaLjXQcJ_;;bVRO+1}i@gSLdCHJDb$8&0Im'
        b'FF_nqmE%^89@<#4Tl`gN9=5c~5n7tbr$cYVZ(}!H>Ra@f2L&^6WiOOY=vu4>Zz95J<}1kPYvOY=hRJYGAal{r_duVjJNir=eKZ|L'
        b'8h8#P!~7Q>F#gl@S>K{);a)`|7WZkN=^Q_&aN#<946gpTkB77QLHG|)gV|{_-koHAuK=WyAKjB^I?)FbO~?D@Qj0s>XC-m(_mPo&'
        b'BP40`H`7FtVa!Jm>-2Z~D&A|RMabd;Fpaa`>C@2^y%Jf3lNc}xF5`)&+PKB@hp=`r`8zT!CMz{PMjfMg5v}&dFm$?-c^_8dLa8dR'
        b'_pQFN19F!Lxs0>yI(R_cL{)gHYDJ<NR&cwxDJCuk6+{KBe&df;&-?}EmzVTGkZK4*{1?dU5X5QkBa1KN)jXQy|NJ+aOlcpl`JFF<'
        b'x@zNKR<%jU1hodViyK+~y+S(#(~B^2fle3c=-3df+)PBp2W^%{Jt5Vfxt_rix{OM7Uf)K{_o0Lg)BH`M`G)h&=hW6dlT{eBT~<hW'
        b'Q+D6&AtADYdv^+h!3!KBeRJQI+jn>b8MK(V%?}&;NO-w96W_U>zX1df)u!NElH|M$62|!PK2ilo`G5NE8T&;qZ@HIc?&gam$QS0r'
        b'#@h{<1eVCejdwMKr9ax2mLyOAS)c!s5XOV-U20q}zk^NsBYj(hY}};h`%T=_9n;00xn>x;*RSCG`@{?TZr}A@<nq6v_Dzq=ZS*f7'
        b'@XyQzFjOBIFn4yH`AHvDwyxp+zR_xwe=@4RTHX-eS6?T;>r8ZwwBf!!>WxTv2di3fZ-%mus)iX`?#ZZ<Qi}<fhhwYdJ86agIYB|6'
        b'l^^b%`<`2;rt*(oVbDG&+Q%1FqkVH#mEY{W2X~5{@W02zjP|-%+kc<!c8>SX9qvw^oO|=C*BR0)9Q6(anUo8?r-<uah-Zrv33Rca'
        b'RW{#K+xNY6%Po-WJk?9RQ#n`6<y_3X+cS5LRQ*-2u%`Xf1;Y159%)Qn*JJzBf~e5>>W<#hD)sqZ``KG$fGwud-|zBId!22)IvN$a'
        b'NXwmDdsv76>5iBHavAgb?KVtjdiTQD8S{t?XQwR}c5pkvUu7T*x4ZxgyhxZ%_ihM=J{06Df_$ubJw>;4@+<gc0!fhJRDJ=ueo+mz'
        b'rr-kmw2RH9o+_a73YHMo?`E67P*9gCaxobW(yf<gFN?`X`MCSi>`j84M=l|s;=g_0!SDYepPBo<JbQuNdHyS^g#}X`g(be3CGRI6'
        b'0%Z<11wn{^&6+BE)u+38w4z1R{H@Ww&j|<4V+i3A>B=;r+k|>gZz9IOAD9sd)whkG9T{5@(3j1Dpc{`->nh3I3+#5-gI`yY2}?xQ'
        b'3$x_<<o}&}6Yiy6a_yKDX%7N8034rjUz}y0?<K=Q8c10SFa?RA%;FN}QAlB6A3q1D67!qh#-j+&*MaeXr{N7nfe&=LePCjg2@_As'
        b'-`6Y8=`9mfk2Fr%!{qeBV`IPSjln_S*Ew?Lm%VeEXU<N4O5hC}HDN28++QILbnN}6C=tDXbg^B0OW;@cO)h#FMIC4<YcR2=ZDprh'
        b'>@0G;LT1lFYJ;mIV&chAsF<IU7AZsREL)_!uYw&VrTZ&-$rv)!<?MvFzR2y#vmBWy_Me@IOX%gri*a>GR0v&~6cxGF{{R*4o`Uxj'
        b'!{c=&EvZ<oGLbIUC(m$<wwLcFzvZCQh1l%G;MXpvv8~`KDY*hf#1mXpu)@xcMn!y*Jjjs_GT0++9p={J04FjYBmp0$(^7eJt(44p'
        b'3QU<!;SIVh<S9HssnD}*LIu|P7@}uKL8S08#LOabfpFw-e&l#&dPZ|%Hcrw@&I5_$TJqOIqWc3lbnV@6=upiV7boqd{v4;%H<oif'
        b'x`)-a_-1ksf*WnR1_tZZ#Vdfn<A{qsvDJCKr{Q`Je|xXqA=eowW*B}Y%J`n{J;%n&jVpNBD>V)D*m+hk5FTJH$nU5a#@7SB?S~P+'
        b'4MD{1>rM;+seb3c`AyH>&*s`Nrclh+u#HsMMvByR6k!E*BjvxH7ka=qd^Rx2-!9Yb!BPX54p^P3y@zS<;pYcnCY@eruhqwqA%*Wl'
        b'W{>-<=K@Or+MI8v<|yVnJRA2(&uxkc6X4J+8JXPZpC6|8dxUdF`bb2#ETnDb1YM)IwsE<^nC~DjTysOUQNfE$tGn%W{}A8=66m)g'
        b'?u*<BrSAg{l(@<P9zb%nZDa}KhWM%v_JHBT?o2$*!C7?`#09&9i|+s&ykB+;S8B8bAhYd`BybSw*Lo<2T>ZX}5@bH1F6l8<_M~F!'
        b';vQ2mKYEzaAvZaCjQ$6j;g$(+3!mcv34H(HtYzG7o%p+++d8rQnI1std-MspiFvg9_I-fg_5Au4KP;4v=mf(Qukfo{X`Hc}a`O1$'
        b'=65;Jylu6@-@Kr<nP+;^>J+vlIT%Ri(>=Eh3K{hV(VVL2oO^6p;5FIa_kqRGnX0%qu?r;nWsJ=EWDoT@A*AP@e+@v&ZFhhjvb`5|'
        b'4*BS1#d!e>nKP}2`WV8`$gaHi@A^_jCnvXYFz-4n@U@Jp&o^F{pMOkYybM#n5vmz&Q-FG!9aNmDhpz`pKfE4bTqidQceL@ipY@pE'
        b';UAR5ftEMc$;%G#Y7n=-_nMyFZL`aDr{(nyO8*{wO2TH#H?uY%_Tqlpvq~B*P-k(E&2QAi#q<>M@5KUpIp26kI0|qP08TER6t>f~'
        b'_}-U|w48qy7mnXr%%Z=~=iqX~u)@uV>)b6;$(jq))4XEA(lSj^kyv3SBC%rP4X}J3W_KdCT>j2B#?0d<lJt{ot(xqq;7x}-Y|EDX'
        b'vRtaX*~i1cB<cP_37;j&9Z{n_<yenytAb~`vRrvN*Ifq2-d`mT#w_=h|IqE%$QY7y2X^XiSoKJ^zrn2lOYtMf`2rN=d7VPbS>4^t'
        b'Ocz8@?EHhzKOe-*MjxNV9&-VDvWM&!_yZAiF2c0<puTzyhR!k{^Huj-@Bs)dv?5frO#OAYV39<dAP0$=@4Ia46@D=$j(evY5Qcwd'
        b'5GYssyBxrNi{DVq4Vll6M23e;^V`Muk4EXSLN`Ye$%lbniEMRoQ6ZT49WJZ7+wS5AO6=EiVgQyKA{Y9`cg$PaEk4VQ-j(pD?$$HH'
        b'_!^{=t5{(Nm;9xF{{D&EEQ2TdG~aW&mG)<3q(t|yE0<o!Ec1EY-L?q3ZJpirvMcRZrV{(87EQ~bI%>LX51BloCXD$5qy_s*Gr6$n'
        b'Ve~CYeM@s$TeD@csOXW$>s}!jZZM#4k*Da`nCSfkiET3&&cBTYZrZZMM5>NFjFRF&IyTDaG|6*N_HC-pt;;fz;Tx7=jV!W*jy>H@'
        b'T*euz&;O7qiSeqMw_Te|=i||Kf($zELUpGp<|zSad7$6^-qWq_>EdNh+zZ`6q^Y0l<|Pk5KD_?rWzRvSb7yzMuI_dWj4`ujt|j5F'
        b'!mqpeD=FDN|Miz=y7?zTo!h#Z%{(9Ec6Zh*fUQY6(E3J`?KI`g?r!|-CS!rQ?%tcFH=Muf9+F%Zw~LwxCe3%(J%}f}Z;FRRmkHQ{'
        b'<~nD6PUOEEq^X;|?eDAoYdz|;ZYqK$gA)axLs%pML%H%k|K%=qYBv?h#;x(`ma<yx;1w+%PRHQ6N|kzz4`gVu(#D0D!qiQ_jZl&H'
        b'SVa&C*HHXrm+@sEg=G=AZ*~+E4+O;rv(-NnN*}~RG4(?b%zz!l^(>;#hKEjGm%;EA1X;Ndk)lDPU;GADKjgc8u-|}%;)$3Ry`<E}'
        b'Q9a`ZwNxRe5M6gLzXql83Fl;Vde(qzgY`;8*BShA2m(N0U2u%M@c>1Pdgo8C#>8a>cW<HPbPF#0PtT9P6KmBVO64Fc!w|L7ch_wK'
        b'5>G@IVp=7Mg9=qNqR&89PH}*iangI6)OF$@j|aPdRH)$Ev~P5rotb~|x7TL6_*mONuiX%0rH{`%5Hw284;mHjHEd+yS@q(EYHw}F'
        b'$?vaZDaNvtIvm$$1?vzHs&ps_@6%!M-DRYVYROu7AuFsREBx%W3u<|VnxwruKkgNSPLiXDUOp9%lJV%bJ|vz36ha#OS1_8}<T{)2'
        b'M?<5{C@iB1BtaU2Tht3LsKYAM;Xwg#c#+EpXycWCi-Uq_wMwtPk3xcJb*K&vrm$eWI#`>o!-EZ3DZ4Tmc+lR_Q01-ZIPpD?-xalD'
        b'Osxd90J^D9cj;RwU?!$wYv=_1%p7l~4d7{;iAA_>y*;k6D=pq;J|oXyku5pM9{hz0bR)hdepUSV7Gb=pPW<47A>@@lE@<At$LU{T'
        b'9dCEdJS54+dxLKLJOTVHzwvX3^boSL2ZH=n{{TkC>k=R6IQXM*ckW&N$>;sEkDPZIZ#;~-S`wKGIL%7WeP811c-7bNs_&^qzO$TV'
        b'x734MQNn?j7eV2kl6e^`69jE0l%RQJNIM1(4Z|z!d7+wU;xasO3r}oD5g>wr$ODA;MIRpv@+WD+2rz^Ba=r-S(iJ}K0lt`<BD}x#'
        b'b^P)wpQ#|05QRfru5y|`V2%405%7&D;B(L@d{J{XLdt-3Eyyl&%VWYhQ1|N?2%)gLLWcNiFcQ;67WmI0@~SF>o~JuTSq`EGY%SUL'
        b'Yz?jHLf6U?>2P>BYvUETS9j_28YQ#lD%?3!>S_5hhk-6uCKxUmutX*AsMqM36)@XQ%d7M@+m@1Q16Hk1I4P>4ONxv2xsd@Rv1-B5'
        b'!1b+tKo!C5DCkR=X=M!B_IZcF=Qa2m5`E4@pD#|7{n2B4e}J!ll<+sDBj;sKY|xV(@jmZEz6QOo6|~2{xHON%Hk??@UxZ!>1Rx6g'
        b'I>x1?<s+{|ERp3(;ajem`$}JTeH7`-K*<m`veF~=RYB<&z8-+_r}$PT``0-EEj;+aryTk!`kbR!zu$m6uwwlQJri{G_Sr^2)4e}<'
        b'2>9Ba4dSN9R%W+E>U8<Y6A|4Dmg)HucY5<mcnrD%gP^|O3vfvpEpiA~5YZjFd=4%N{>PF(V{kD$gI20mqCj7HFzYZ^8m8HX2F8N|'
        b't-btzKdDeHxZx4IlhMK%j{n~Ygv#+lnwzq&L`%c0Tm7&-od3LWf0wtv%h}!4=zPGpNR%5aGxc_vvx7;(oE;+Yg@>@_V~t?2#%i##'
        b'SM9aRk^}XQ=8}?XT6i4cO0j+~e3jI0PU6Fr`zxa$3z_!^%i(`iSdNyy#17!Bhj71g3wE~vqgj+c2Me>;fjJauU5CMc3IfI%;&isl'
        b'dln#+<!tV92aDRi=xFWoegqP%!haAU!^i;Rfr7HK{3co3b=`r=w%U%rcX>Yq5ZjZ-I8thSwGtSoZ8N%83)*TrPIh_!2C{Y(4scJw'
        b'r@xEgGE5a(w2<sL*5!Q{WaYPZ34EeP>@2EVSwLIo+gB#1iu6`F8SW8Thd2_Wt;!|-`;%+2OIXKWyS#@%S*LS<7d%W8Akw+)M<aBx'
        b'EvuA)F!L>t+0Z)8(eJ%;q%pAL%`R^hNO?bboO7L9=UX6xvoH)^?6t2>eodx|K<ww%>9gg<Sn3$OWDInk&&TPrm45wwdyZP4#DG&r'
        b';t5r#frj6|!E_N++1&rRO*Q=<gEY+V^8T@_@z7G|Z@a7<(Kb%g@={mF-Y)M;AobzG>s+ozuAPnoxbErlJ_phsDV*TkTTx3aN~;M~'
        b'3)1mym-n|IJrSN>(MnVq;tCcqe|!s!-Ty<`w*W*{t!=NpX9h;t<_sXBV$KW<jHU%>4j9ESBI2b&6Ge}m1{6fIbI>?RMmYnfgVH&O'
        b'reJoOK}qCD3R+@nGH8T_C-I7M8&Jy13JnMo-T$-p9<<K)egF6W=riknd)Hd;de_?PVi>bUWynbWV%GRU^n#IsB$;*&ZM#+9mi}5e'
        b'd(Ts>Z;Tt=;$Kb$Y~8ooV|-Y!m+wi5uNP^KISy;OVYG(#-AKfCp<QwxeYi7;rMLX*f_;s5N}gi&c>TTMh3k&zkOf2S8KHi3+kFfA'
        b'i@yl$^kdwF??}aJ>AX(~?f-uUucCJK5#>yYjwyH3zDPTjTS*)%GKe^u!2<UfQWTInh<>foOp6h0rvA=mDgrEED;<h*MjOP;TTYpC'
        b'>9>WyZXfYTxqC?s59j$TH@w!tS49_pp-6FK%H6dNSZn98Vo_4&-*@|!FL%e}H1-NF?BB*nlo4`Xb(|~4oV9@;@3C{aWyp2T^T^mE'
        b'9!Dl;FZZro?nAfbYp)ONfu;2~^txl{bvwCUS^RFwHEEotWGvm?yJxF+RT$^(dGttF{U#bnJVG*Flr2@&8DI-YrsN{sYL0YzuKm|^'
        b'N?Lf=-nCcQ`g0B6Uvu<dtK2=>-g&LFS=t;x8_KzcTh|=F!d4}oJECo+m$sE3uQ_hPT3!1K4@qcME#-0UV;F6i@aEDty58Ujj$;cx'
        b'zt4@xFWwS7g5I^HahnQhR8mf_lu3DyC)ok1@&rwg*S>5t1-F!9K2KUdgY#O?5JGPYSVGeGsI<{+DPy^OZD2z&<-b9LeE)W@xHeEV'
        b'N0p2=IByI1vbK--YWr<LTU54;+8_Cm8u5N<P3+WK*ZrMBU#+<2_#D}G*!Nwd4Ef(uu{SubIZnWuZi3cHn^|38UQNUCYmQH0_oZ;J'
        b'5G0E^bc89FX#<54UeE02*wsfC2^+Vkjw}M3p)Bw^$qYz!pSLQ|D|nbUhFfXpRzBF94c;*x<?<BsuL&IFd;2~HnDk(XHcUw17W#z9'
        b'P2yX8&o(W`V9W3wagUaNF+GW+4Q0#SEZfEM(`&MY%O)`b{lE)-9QC&Knq%v=%92$3>T4+u)SD4Sy3mk+&G8S|E*I;qB$%ORh&&jh'
        b'TAFvN;jL?q4RHJ`Ws+`SD6s)#4tmhX^k9s3EP7Dv6NJ=HDrZu<3Cf^jT^z>;eTa@f-okEnHijewq{`fdP4aUDray<B`Ug8Ys&xj^'
        b'j-;@wQf`rX8{IKjz0Ui3xS`|J1eTn`;8pSty>vq3>NuSN_c>ozdV_@zCLO-AUOGvf^EqE)751lh2*XO=FBmpT8p*(@qE*pRMf<30'
        b'RH3Ixtil6d{w%%3m6|sorOuHo<~l2R-{p5|Pl@}MBBGxacxCi8$CPW89}cnyUMtxr6+6J>YmR4NH(0y|TI<c&7OLh=X2R6c@g8~S'
        b'8y>sn(8Jk_?(}<+4Ldc<?J;7FZjM8%3cKbAfm0&J8%SlCKtD<9p9Di`qxTtmv*N{9TAs<eOE+fRX9TI_4>XO55hayB*iD5HH$>!3'
        b'Da~Zw<UwFIOL*Te-4mtFS~O8f=N+arFeQ>1??K}q%!1OV0=36bliJmE&z`4?(%QlI=hztGDy))T;giI5UtPDSRYw<<a<9)b673>p'
        b'Z=ld*rM@gvd`eN`ctGuxLH8kYx(lqDo|*#XR|*AkW7mHtoFz&Zj573sl!d(S*gL+)dqVbprfF4e&D*3q<^P^WL-$3L26Al547#<E'
        b'Wzn<;c;BTCM|+3e(NS4^req6vU*}aYKF%7(jTi}WOPDUZ_GDb+eZRk-t&vcBw>$I>h4&@s8y|N#&UIAoDY75vDESBa2INrG*}pp+'
        b'XJETS>>KHeNwOfLxfL<mZv;AYaFRks@Aug8LFKNNp37*Hcq;==<0;%J*#UVmRsJ+>o<{w<!@_I~#+H;`1}w|6uY=Czh4p_lP>>kI'
        b'vO&A0vz++Oxo3NFi|;S}bC%Gpp${ZVV@&N&;vID0QPvK}o{ow=9rm0KDo?DFX0x&Nekt#|&biDH#(yfuH3^p?p%+?_6}ju^j3|4d'
        b'8&XSm@rfhjRCq7B$%t}${oC|FAMJb}(2MR8TxX8nk%T+WNK4OG+DdYn=}L>F9i?bg#+~<ke@9H#X-rwHjB&BIuWk@G$lv3&je~bo'
        b'ReF*gCo5-#=Xs7S;^f&=rukdV>ldfB=blVn?8UidFZM}ZJap5pT)JnyiYY$nudQONjDL|ix4KbTcfP72_tlxZB3_8trM<-z+vB-e'
        b'$K8?_`z9|QR<_G>%}Hkl_PHB#lH*A6NmJ+k{_OKia@;&&NrQ6M&zQZErNfvAx|=+EO1PU-<nx;sc071kKyFFwsNW%6Pa{53Ls|Er'
        b'!U+5uGq6{IwzKCu9M5-D#CO=^JG8Gzvo*tft)x=pOYfc*-_;V{=rUPmbqJ4uNmDwR>~l=EJYilPDLq&6h7?Tg4O%}ze%(R3-iD|S'
        b'M^s0Jp~D{8p-qzx?5A*D5H$1^){v6pOjU+HO>>$lIp%KHchK7uKVvpe>JWtg(m^{XSKM_vPbo_y8YXmn`PK5Hmv{K8R;ldcIy%2*'
        b'`VU(|XjX)~sY#}A;T5-i7+qv7^xQsdctNn&J8b^-YUkTIW@kq8zi+8Kek;oF%xQkSbcEZF!cB5r^cPc~+7`ZZH)HpwSt%GxUvQ(E'
        b'<pQN7p2AyLlG^rx?`)Tx(cT^OWROm{N=<lQ(K4u`aM_08!NM{q%{!aj$k3Zl=M{e`*M7jHO6Y{KinY6SY&u#}$UJz<jf6}zho!O8'
        b'4*G<W4q>rb@F#e}gf03;J3apuNIh3-Naa^@?RG|etzG!CKJDOP;fr|f55oOyAGVdV8@&81A2|oM3t8pXI(^lI&d-@x&w*<J^QtT#'
        b'ItSdsM~Id|evepePT^@Ns~@%hik|NAsO=g!XMMJvj{7Ab(z*7eyf&J=$H*Ar3r}=`bLp1HgpahseO;M8dS8Fed*^CvZCXv{7fY*P'
        b'y*k{3^Ioc#iOW3B#mePdh4wkmZ?N#uS9o+Rb$G(&>URI_`FmA#2eNh@`bnX3q_yC*&+5YO?4P!GW;6IL!S9iFt?=7vVeDn?Dfm6m'
        b'uC*|ho$Z?sw2QB2?rYz?zg@iG33k>&V2XoaW33Td)`m|7{yxZAs@zy+DQ<U`Da%SXRchBVkZ#JDmAh!rO!s}iX3^Q=@|e!8j8NIW'
        b'86@qLQNvC9MCm%3w&iKpbguLs2=pOp*0Qx-pzplIKB16#je=5GW3Ah8gspAjm#-7{0SKFBNmUIP{&k+-b7-ggW;JRbI!GU8>aRAe'
        b'Yj?ceURk``{&IWg1Sy2>W7O8t?pO=k5|MLftA~D~^WMC?eMe#5k%l+g9hq?ZklyuJV5e&<MRYB^G<y38&xXIXJ66K+BMdH-Fls60'
        b'Fy(``dxdTv_W0}P(3!ch#c>IUu+(x~lB+IKj$v*)e8hVWwIA`7>Y?;@Dqc5xRM+0w>+kX69P9PjZ%U(=Im_LTOUFca`t-l!k#*bm'
        b'H_35nu{|+2snfgvSr2Q{F^}A<nyU;Lq%lFGR_tZQsQYGfY-#iuC5=D*3l+w&&OJy&0j}1_3oo3=Qzl7c@6onxTkLAR&O)Unrros{'
        b'PJE?KZc(;B*po26U07ir_zs3}YMp3hac_UP{`-mMk%kHFjtT7*6Wi@R?b=7BmaulAOY7(?Af(+fzP%!(U3gyf!5uuSn0enzAKp8s'
        b'X`ieSVxGtP+U4jUC94?q;C5lV%1Ge?XLjB}nfh0!&{xIQ)6F!DY<Kv#SNONvdz~e|(#}`!iZS{cf8)H|)Fk@8Qy8IWhhHUh`&G$A'
        b'JdUUk3L+h;5xyFh*!kJ*&gg@*FY08$2cP3uSMQpjoE#&3vyD6HoT!{JA^Ha=?7(M)b@xvKsAy<!c6PqOxB^U3hTe4=CQ$dV05b1|'
        b'U-N}i@kyrzKH(-b=6Y+^FT$z8+D<;HMs%=-r-c^=Z9hmSwneh_ZTzZQIi0S=GliezO)swXFL@sP!dX~LZ-nsJeoQ8ERp(x1ewo?w'
        b'xf7i({jkbbYA%_^h*z^Zi<CRI3LUht*7_xSi(4z2LTxi2dd?|)8WRgIfpC6SxZAPJNiV?s6Z5cIjyXewbChwcy4JaK>qDAog!7sa'
        b'to?nbb_Hd?51hmR#^iw|%_C0Q6arlSU6zS$f+b}OE~^1^8mn_pyA(W0`$y~2|L|7DR(=)U`3mz#TOC{RPiN^l|5@O_XrKFL{69oe'
        b'vWzkPAThlnwY=dJwsvL8EvuZ)VC5PO{5dZvH)^<{?|59DvMrd*FZ4<EV`Cp94R1RgZ#yg2JMD>1?avbD24zKxbB&eW3%rR&Ea&7K'
        b'Mka08;ciK#q<&pq8b+75HtdiU>zLwXrqt`!Z0C*1&d*eN+k|oI@Q9~^d}-B}dhZz-Qv8_L9$#5knR(s}+SV(V(6K7ltK9PlqkV#@'
        b'Vjvuh0dM8}JXdRKZq_#PrCy~YX!O!jKOy$2$%p^B8y@7sU0E)o&l7553dagfetrJHI^8^{W1h2OzSFLCrgTW6bxyiuSTdP;$RvJj'
        b'EoTKbQ6;bZ%D*#!5xMknNoNkd4`G&g7JK#xrzl5uPGV@h2B*X5teE1o4{>%jOCH8{<zZ}Dw-H~7KVt~nG7x3STYR~!GnNr$(`cE~'
        b'wSF8bK08c&U*&XR;bHaX8^${w<DC_cJMF)=bzYLpIq6?6OBux!2Y6Wyx2PX+ZWzJVj&Usm36eyfa2K`)c^kCp1q?4E81?<O(vyPQ'
        b'o+{d(ij#?Rtg=jFzeU^Uaamb$rx%S-Bp^53rm5y+ss%ams*L&qi?eOxM)Q~)-`lc>H*^)ZCZ60Vaxz^_@RL(r-6B94+S@jE0_P=k'
        b'I56dK#*L*joRn}zTw<eVVa0H<mwB3rVsz-^GWEGO$W!9i367mV;$+oH?Q6U!+gsY&1a6YcT54Q6uK`~DBIUd{+8j69DsHsd_qTPP'
        b'lGN{N__ob)y{+P#w%XtL=>2W33mW_xwZQj^HLhVny|R@y<ZK~I;SGj)JF9-z^~I|hC7N?gm~kHG75fO}y7BU$L1C7oZB;{sOQ@}~'
        b'YHKy;ZyvYBcMho@r#k%U&;w(uw^#bwimDG3nF|&Z)G<ANjMhU>^3$`=>u<Vb!iOzoZ`%$lH~fLD{hwpkv{s=RX>`Q0xb1iEWM;OB'
        b'GvSm+nEJ31dTWUAm<*SqW(Mv^^k1hx^hiTVo1>)7zO=3K!=FkjC9{{)a1dEM5lnjr!HgQ8X<OL!p=9&8R{ccQE!6dy(HWzhF<lhW'
        b'q`|(^iZxy?7V@VyZX_DT%p8Luqkf4kwc0c@XXlcKf#?_;HwZ$Hjahndh!}{IE*(MJeIlP$ldbVtTF6AySXYH5`)o@i{)Hjo)e)<l'
        b'la$LRB+Y6A`K`&zC+G{uZVJN``zK;~u1!}X4Bx>=q=FpeELN(@%xF6h0c;<dJHH`$8LsKIH)N_5C8+&h3gHvHjje6t|C_?W{tEwJ'
        b'^UwJ#oxsMP=TY+7GrV~2Uh}1?ezMxPRX1?f;u~*G($F^X4)x9+QXkfN4Kx*+kTKbJPV%sFw-mXnpO>>7`;GUI;2ms9J0Et^hx(eV'
        b'3viu@s5jDitCQD^^?KM2)Pvi^YeT(u);;WiiZ*VHt0U1nJ%qbMEzPY1GL8LKD>Br1lcfJ3Nr$NQNsCkO8qE_W^NghP3a$1UIpsKw'
        b'B)pQ|w^HNZd6`&#X$_Z;oDd=Byg7M#PR^ThXPR=pmyhMc7E>V&UND9P50@2ayjB+_+Z$VtOSNB<%~x8fm@r6`U<QT0*Rp(yAiHpq'
        b';H?lrwG3lF)2i(wsor$CRqIbL1x<OB553eXiVyP(^uALhon8FRg$;LG9sRBLW381XJ32Q=R-U3>jKRcsiprnHr6gr2ec{X{KX<#n'
        b'zxlEf?T<XY+~sDg<HuI}zShbQM|I{%Lie|dH<mZMIHamlr45FK_GgzxN>~5D-K5{~sbe2$Xl-@0wN|vX+TUyKTq_Cvpw+e9)aV*t'
        b'qAOa38y<w6G@im&yWfqsF@m_2SFEwo?FXGV=p;CLORFf!t-Bvx*cz*KeT8*ul?ydORJt%-7$yG+vMIUTt>grmUC>%e+q+e^r;4`s'
        b'y)x%QWm$s#?N(=k^0?c=vd+T<RUonmZfHK3kefLr$7If^w<cw@E-%V|J7-^`E14AK>`5)lX+{%eX*G$T&!6P;&}C!m@&t~)&#+A9'
        b'vV2>)P#ECpd?QglZ)i`Rm-hbs*=t(`nK9|D)|*}rJ4&ojT;JPWA~7K(rZn}}R`Wz1*J_#HDok^QZDP}o3~t!e>aey}Y;0X$DsE~K'
        b'1YDh56<AFTvfx9)Cj>17?QkKCXN*A3>GG7B{2!A{liI{RGEyO=7{eIZ`b$*s`(<G7UP!C3=*r1bj-iFo`w~iPM3FJ{b~BY4h4(`T'
        b'rPVH-%(`hw;;L<LGcF<|C>OpU66|yTcTEY^3syPliv;G`S~_MVYuw_k<_+7X3)QuIfK`KN69jQN{A5IpTHPviTfI<$5v+5UGDKil'
        b'rcYG15_8FWgd2(hvX%&+#K^;RA4Wlinm<Nul_YC?bak9}@FeDG*^83ep9ad>)8djJ%E`P+g4RcuZ>wqRbB$;@%FvISg-Fofg1sMU'
        b'7}M$)+gdTU)!yEcGFy@zFtom^A-L6{ZLJ7yrAs{7b$meprwQ=MUOY5-_`Z3CziCd=JB8mR#Q{G4g*Iz-?yGxGhTdoq^5tr$66a(k'
        b'x|nU3S$(y|NnctsYu_Q9*ZL-L%_#aSS3b47i0^Ir9L>=Biwz#F4$syK&sO`1md-c{#)iTg^MqGZho<X?zv3!?snYUxbD33WlELqK'
        b'HZZM@`z;krYwT@4aaBakwv-1$NUm~+HS}l;D3+K!*}CD~$2QHuaIleBj<-A*LWFjfMjnhI@gLJ1mt+%gl=27Xc0z3}uJN^yxE_I6'
        b'A~c&qVf)z5<cHIbLSgz*Fm~w3qJrf^AKF`m%?UbrN~!CcwlCzx3oVWdEfp7A>^Uu+5t5|!Ep!D{Ti~kd*)yAIZNDvq69l=r{p`b5'
        b'Alh?&kV=FF%DFoyie1leNR@KszH5DYS3hF36XEk+9{JDEVyrt0d{0XL=oBt@y*M`ap%^4Q2qWX9VdrUr#wl~@a_xHpk^VEVr?K{D'
        b'S9_##@%t@~_ggCd*<zpGlJb}&?_k5u7DrJ_#d|IE8+7P&7jZ%LIp>%Hn{bnlY%U#PrV78Bxn^^QFk3H3o*U%H)}n`2=9M($wK%LT'
        b'6?rYO-|-Jcq**OH#Ktl2ZFix<UnZ95mQu08_Xsk>Ub)zX?GtI^K$V-z%qfc@4tlvNH>iaQHJr@+r<{0m#yl&55SPCx$M?qXWcuq('
        b'i8T*a$>vuD<^^(IW9W{Pji87~e56uF8E9pVzumuu-dW~a^ciuvs;0B<{saDGwE5`|4Q_b4#j&u(zOZG{(M~_fY)Okax6rO6B`@)X'
        b'UuKW>DPnWIp7qdI%??}cqdziJw<hAtZON|ozD8{CJZ&?&C1~#jk8KLXwCPX8!nDMl5{f@fXzxa}_uWc^(B8!!TJi#<(~`FywD;)i'
        b'&BBam8R?wQuNv!<==HS6>Y=G=U(Q+Xvvm8PSB)L&I}Agf?$re+x2+=n1@W3{&0=@wdgXGfx{YQabMaW~hV5fEy;|;`@&d86H;11T'
        b'GN2deA0Y<|oLuIbzZaWJW|E~J%UumNvmZaN5#g*G$3{0dKh4%S6qOF2VuxQuQdp9#GoM(KxJUYC*F{$-TI`CJG0I%V*{bUN`u<+&'
        b'%$QWKG5cm{2b0thL59U7y0lr?PmwE){;XL%DRHP-;KC)dkOt@Fc7sp#=xHD=4$@LVTI{xFEh7=m9NcdfE@4|hLi?MI0p#ZHq`S>%'
        b'@g>iY*}pYIW`2fP?ld?2*1Sya_^mnV*XAFk{+?Xf0=JYK_x92^V3vvU7bqN-%xGSg>L>bzC&$NBb6)yGp6VZ(XC9?{f)EX;KL3!E'
        b'^O}FKd*)H~_2yXN3~<9Y&5m!H?cX$4+E;4(SYfTKq?cD;Y1XmF5byy}#w2M#lpGL6AW2iRy{UPOvW3lMI&4hIXZI0eFI#`Lp|RP~'
        b'*la(C_(p4gaeZ<^I^#BWGLko0`r;%f&z=!j@2&0QJAdYjYox1^NksC3Rm-wFLrC84Y&I~=CJnKwvW<ZQ_qAlJX!kzZ>^RkIKZcmM'
        b'ru@jRtZ3%gQup8y>Ii1KGFSc0;t|@pd<$!;RRxV@&alP7^jbab_xFSoz%A?<8H}Bt_vry{%4>Hw>%@~^^;@Hhn-isDqzfdYx-=Sz'
        b'QA2cLGts5Bj}vQlIZHoouz|s8Ut5zmuG?^EaH%BMYmD)@tW!tU|HOCL2pYv1>G4OXoY}+ATk~7Pd(Dpbn(YP6mAlS#cCg~wbhNcu'
        b'C*|A)8E*AZi7qUYRj(DQz9fQxe4+WxuXtn!kPVaRmF%58RA5bBOgd*0&Q1MV^BK2N_BfL=^1knyyE>*+z3sMAr_P)+Z?#wFr}wRr'
        b'H$66d%9h;bt<39^)I`?pPvpZic6|&<4QFGYCm+VKwNuHqw7V!rfsM%*Xj`dqvntQHx5z)OLMv+Geb?N{%toS4cd`n_{gz$d&Sxgq'
        b'(S=X9HTB2c&_=)I=Z*cfVM()NDT=mmy$?oT&V%!R$0I&(%j!><Gal7-3g1OC_%uL9qcY~q;?ChB^~O~tx455i`}A-*tG&qYo54NO'
        b'^2izY<BuTicD{LG!*k7!_~y#uAbU)6$=7VwHzunBnM|YfccV|$llqI6@Mf#)Q4qiUx}4b|&8EZE#afaw{XV6A#DIJ~xnDR<p;K0c'
        b'I$5G)ww?RI?GQh+SgRzp2l*iD_;0N2`eQs-wB3)5E#;9tZg`baq{@-x<{uhDnjMd$gs-|aQ^pBuWZf{YR;)4x*6tL(LS9y-f1yf0'
        b'YDPip_}c9}^)l?+E2zqgtlQRy->QZ+J05MeE1D~JKb}&<hDw@U1JDRkF43(*^K$i#P1(6#S$A^7a*dq4NaH#uO}|6QbBzzq^m-NQ'
        b'a=nWJ3Uv{~BXnb?{C)v<z)zuMQ+Dd0QC4H2Uy*mjnB0H}zyI|3jz_6qmB-;Dy|J#l-b=j-HCAKM*uBF`{epKeMSk3%BBL;9dukq@'
        b'3lwDu)nby8bgyLjy@$io#3o4K!uT{sKGk?n^tbX_lcT*Ud4E@WeRWO!5L3OPy107IN7DF(W>bRV6&WXAT4{<H8fL4W{A9$`&@or1'
        b'zZ)S7z1(E{=+um|2yK=mWTS#}JMLaCU-qO$dqubjV)NN1``M-$n)I^jH(t-rH|1|v<d;=%EQ_03oZ=s%QB14!Z8+WJINfCbvZ>Pc'
        b'Q_8>C>{v1~we~u1tQi?HQL&6&<`tn4MPJuE_u<^u?dl({f42lRx%LEF$omr0Vp3nz@Ntvl<0ktjO|y=cl(6xONsxp+`@IB{-RR1u'
        b'_R6MPO^u;$O@?V9-*<d_A~1E3;vM%8&O5t<<T4w4ZpV%w<o6a)ZoY)14jOufp_?UMXDoYZf>yZPTt9?}wna%-qQ9GcXC++iqHAGN'
        b'WAu&LeJeL?9clhva@JbC;YdNeu&uY;&2s0eaNM+3O+x?C#0{SuZp3_W`W8b-#)e@^dQrrtCdb=N_P0TtH6=x?QNv{0m{pM4GjsIY'
        b'A8A<E<an#e{uW%{DA~@2+3rs}_(+4f$&uM)e;t-tDcjhQG1I-o<Xmrsyxv4-M-v9Nk#nK1HO-i^Oe)-HOvby~4DAQ0O^%gK_N9nt'
        b'N9Sf1l!yFdWj730HoVg0c)7`Lg3CYYLPS1m_42gldes+N4qnY=YlZ8}G&X)i<s%J?n;fPldjh=fE_sKw2^kUPDE0g%h`#w6bGC+j'
        b'=;w`TL@rxjrGBAlM?vWzMD$>PCpu`Ka9`CVhEc~i%{rz@@>W0JB);DemgJ*J8fpol%}wK&73N4RXDT&BQzNxZqx9DobkU1L<@dz)'
        b'Q_5<??z#G}XTrj{S*HvM3fh1ZvgGCj#exTSXhbv#3vC5)#5EQs5zAy6AzU8(p0g3hmd1)Fn(R+Bol7G326K;=%)K8pVsOK_CdarY'
        b'`}n3sBeic0#JSmc#lGT-Bl^mYg0f;%<Mv~8Nv7h!6?1;Zr<I)F;bROZckH`TX=C;rqo*VeSXIK4mBe=eTk(%8;?;umeUe<&W=WGh'
        b'sBwn|<3jMKY=MpB3x36yNW}N``UdWQO)9!l{2{?~veWe2iyp__itULhrr$8;4{CA@0vT)UlBUjA+4_<O_a=u77AGNi?`0QA=6pyN'
        b'xZ+!By)rwn5ds<A=dkFvS3HipBbv@X(P)0X>bP^Y()PXm*4321vh|-d^jvlHz~Togzwc$2NfwCrQtq4+V(|_!NjN{^Wgu2NgaxyS'
        b'ZXgdadq23B<y&vTZ>bk1qLZzdC6-MnWFa#iz!bx}F_(@be(JWX2Ezqak-{LJ9rhFR_<su%u70V}V34X}n1{i_UG?&R5BE9J+FJep'
        b'AFhgqGsP(Xw{QrApssM?a(`CkIv@AH(ji>4k06adCIH@N*>Sbvy{oxNmZGcNpxl-IrMc1mak;a(x?D9Eo*T;Ph@XLI>|@pRLwIR2'
        b'U7+^Nx?|fLQY{|O^=vc>cH>5nQ3g_GcRe-gX&>2GM+cWGkLse31LA>j58=Q~p@&$b`L2U=uD3@ruR1jl@hq#a+E-si!gaaKSegZ8'
        b'p%_h8Uw+|(h&D?ab>hYhl{Mty#eB5iEW66>_~UW=l&cS4ixc~n>1x*Z|IM9#mPJ<$??#JXau;5;FT5%Yc`DW1vSPYN$MVKydd70z'
        b'RnG6>_-%RNsvxce4gYoX?5o1Qg}uTi0(ol0uLJyH*42j#@$}vnO$X=4NmSuE;<hAO4~7?1@$o+OJ(ae?Gty5h%Ow`mWr3+ZwZxPh'
        b'&B?gw^L=k+e;z1&T*%K@OtY^mr%!S+MbWv8WiIu-W<q*Q^~i+6XgA^Qd8?Q3O>S@8z$3Ahy2;$|{G*gEm1&b*7UQb_!(!I&E%w$?'
        b'>eo50H#Xd96djI;RzG^2{k^flcsc9mvqu#JHjUOQO;?NJz;|1m;(14_VCi}EX^#UDTe4c|d#VTRPWU)3#3FptGTve-Igf-_vX4;j'
        b'iJm_=oiVnb7{ug?hVCS2j1wa1*na}yZ3mUEDB>#F!Gi079XXo)YgH|Ze2f|I3(cL<pfFMW!xhh?2M)xb8+09I4jd7J(HM2Q>Kfs>'
        b'TAk}|6suR(>oi9?ldaqIS6Tj1#o1J)>1APkkdiV@w^@4GG52zQ>hG;88VAhDHh%N;%lb)d?4N~`esLio87{Xtj(*5qMjKjTbW(m}'
        b'b&(<@Lg>cAVZmtEMHiys!P~Nln~z`dToRwk<WEq*2S;B$jYxdOlk+w#-m*FD^0RJ2GGJQysR~1^aM&}hfaRi}xJ=6zw{SuHQ#l5W'
        b'B4h&NI><~(qDu_hPxCj1uEXdU&jg5B@$nh)bA;1~qGjl{OVo!zrnnICXrvG}E_C?i-<x%z+pbW9aJrP*h;J0DU48^>W$53pxXjAb'
        b'vF!Ru<dd<6)ER7S5b2%4)&`THh4i8|AzbKWM6Y@fR6R@bd!sV6=90@SCPQ_?^T<jeN1S+x0i}HRA1NP7twXC*6(N%ZLQr#fXj1DX'
        b'(*%X^`#W2=4_s$q)uFzZ={r%PzVgx^ayITia#nO{edB|0doIz-I!k_KXg^P!66e*SkyUzoBujjUrLY|VZi#G-M3UIk;wC(0zDgpQ'
        b'6M(Tj=nHxFexA4+%;wGM=_WGFKoaa`@sy~~90@z`U8%r_GGk0{=WPD?lG!ZHU#$qSGUg2e-xJ>1oa>oNzo1isWGb`w6O$<evmDb>'
        b'fg02{js7f~n=D~C_p|Gj+;H>u9Q&?ILcH-sjBT|dU%cERW@q7M)fHj4WoAacRk8WeD@e|jR>o87Irkd@=IrPe_YHg4^`nI*A9FTA'
        b'$@#6Ednx{%9D|ifPaQan8?*D>m4mMcUpdk;(i0RbJ+Htqex6Xa4B?iFB=;+>6R}dkyt?OC(SFdSa(2LFj)u(9DnPRu37fa5Y69kk'
        b'{}OL2<EH0tTYUVHGlR;RD@<;5(QJC-qs8+Q-7ok>VBu_MnX-zxkyN&u_W!Z@snt7v8o9c0r8Ro}*RFN6G%sPVX<;lxsBd4Voh>^^'
        b'X5KV4yN=1qMftfwL3Qp~cZl4OpTF5`Hql{n-N2aU%MCjFwvroZK9Updb4iHCaFj6=DGrEZZ|u&h=rfH1F$;p+>0$aW8x0Shx=*Dm'
        b'2yt$f+D6xzZQ5v!L1cAzuc)!qT@+o6sU*(B7^rYcN#5VY&HO3vJ-n~2&`TKPHuU}Ky2HxrkE+hg^$pN$l?g8$qkTS=!O7BBMZYgw'
        b't)-uqV@*pIAD5hQD`yIlNI{a+^65poR`R(I#-UP1_{_amXNsv_K0z3E=)1lT#<GiNq?I*^7|F^n{x>6;&;K-%6<_?1kxY=M!H=`('
        b'fUh&<Q+^C)3<1O>3L7Hxwc9S%*m&FT`LX@k%N0Ld9Iy(pbthfFsE=f07l^NSyE=NBuvsvIcHK1ffmDUdKQ)J|lXRC|-bAy=cdeXn'
        b'%_-;8RA1UxJt>Fy8pug|*7*<!MPi=%gvZkzXD)h9G)-WT*N`%m;D2wXVbT`i&2`ljCiK)r1ToAI-z+a?xzLjrg$LdjE{y+V3;1LR'
        b'MybjNud(Yg!}eFZc=TKskIoeQhpxG3+(%rDRTwWy)fE?AS91vuo~NlEK2)wN3=L^?y>eP8j(!h@09PEsyQI4CtZSlKlNK(H1t}L@'
        b'oQ_G2VBN-$-svwcEuvTCelmuQ)e+Ith(?5}9sb`@S!6n)ITs%iTC@sDRfMj+81m36T<NwObsw}~=qC$8XGwyNJn!!njHJ}`tZ`?t'
        b'YiyD|$d6za#sHxMh|Zr}qK|oq`rDW3;So`9ycm0nca`^d!NZElAIuN<x@gQV5V|iDd)*b!|4(55-y1<%Q!+Irr-j#^b@3c4#)cbn'
        b'Ff`1;(2&O5SZt*ugSD?kCah3e=`OHbp8^TnKb`Z7&&{!i)5cP`1gzgyB(Q#gf#fcsT`I#fp<sVC+6kCde4@x&Yry7(Clr>P-Kpe8'
        b'RE)WpUy>7F#vHIJT+;HAcVzR2OFb9Fo3{!_FAMgO`~-z-*x6bYKtBc^=d&fkNsuLHtx9eX;%T~I-kW1UJP8V$=yl0<KN-DyJb$Zj'
        b'kB|qwWF$e6|F*#3mUxJl3t0|bC}&-9OB31u<mE?s*WHmWUTjVMHd7`rV#*+=`wF}13scWt1gCX;df{wU4w!89116jLzI?+dS@s!M'
        b'CbEM(D)(WQtPpv0cB+S9Nj7h};NseD^xkd-Ju^JOOAr2@msX@)7T9Syd%!ibuqM0TaJRBzAeTSzsV17OK6n!+E0hxyW>$Q4f!^$u'
        b'aM_hR+HDKdD&D=|GN)~hx!}6a$WQDkI$;(O`s{^)YZk+k-LJ{RG$brQ;gtNZ>FpQNi};W9UVoUL?m>EDLXTbkeM0Wx>>tue^U9*K'
        b'owc{zEnl28(ZR_2+U9pJoRLv^VD#nV5*Hy~6Dn)-p9ct=Y8iaN9HTJ5&A0|Mx-}p!)ncW#)SQ}9$XgVbg<%gZ!Zqr}vEtAsv;nIZ'
        b'1ZeSMvtm_6+r@hCir9g&$gLjSgIb{DTOK`7;cppofxe_}VubnSk_*NAC|wJ5LBf+^MdEQ&bR7SI=ch#*VW&1dDO;=yIv_CfV!>FT'
        b'(~0R7r0HC9*5@C_nf1f}dz^|t#;JH1XEX`ZFvY^rk>bU4*xxH`wLD*_;rz~cWc`?5w}noz#Cg|w!O64eS&#g<Em_S}0@-S>KB~xn'
        b'Pe_?M7aGs)8%+%_6bKWlswtkQtE*!U)GHrGLsyTh77LNo>_36<wyjE66pIVk!Ik^h=5NfQ1J>evs}h+vZxkw37`Laa@bE0cBsxDo'
        b'CcjV!GR2x)&bp_Cbl%{t$!hlt!_pq79?xyIop-f{bCmrBj9n2f-m;=uJXYvro!|4d!bSh0_t!6?QN{kk|4xpXm+5+Y2lLty0uLQ3'
        b'ywx^Fr3wTK<OZpB<d6|`X~8^3^<ceR^qV~<c;GS8V4;n`e(Zl|Z%@Bu`HLX3c~nfjn9I7Fn1?<3LPfJcQjdW}2=Ritv*!mcr9=26'
        b'Qph@Ul){pWM#tFydEO@Qd`+4#2KZfG_3K&cylKMO2};3_vLfNq<RW3Clh8br2PP=?6hQPE?@@clH7*$Po~%w#ma<^u{?-t>H&9p+'
        b'p%tEI&$?rNxWMw*mWJp{XN#0O=n_a(#MuNz!*dtIPWqs><AvHLM$T7CRE#Y0m!EjP3#cAV$cWLh$o@cL>{b%PtUA4c7>H?N?&&Dq'
        b'ywgz%;8?5PAaB+i@`6rBtpoaiez=Du>J9q<x`Z1Dbt};28E%Nto{l0!L9FA6QU3PnD4uWQ@pmsA=~gAc{4>uh0uhe|@j^Y-t~ac6'
        b'BAzbBbpF|71y6YXCj9vz?HkC?&U1Q048odU&>QH=GtWoShQgnnt2c1Lr=tSluRaHUk^e(#<X%BY<9xj#4*9XZ1kBMJ#=SuEX*Liu'
        b'%?dHofBagi=hylnd<fzpff>{3;W-t|i-Kqwy7)yje#DibA%^FWhxx#tfwjO+Ap9}Vbg0xg4tbGB6Jrce515Rg=M%(ueGD<~T%b2N'
        b'#}VTS<Rc6Ew6Vk(54V_Ny&<t*VvNbu8&1LB1wf8?8j;sS6fp185o2aBF;;1b5qV?eNG~0B^@xMiFeJ-Bj5c8NAX(&Y<VTLYyJr#7'
        b'hjJ3=i5z;+aw5vn1r^jG;Yd>&M2r&=M;z>Llp%lRpqCdh#LfrZC9+5v)QJe+hx~RS-h04qn5%$8z$su5D~mh^wHa|7fVz*?!)ItG'
        b'-o&utYrWyXV$hw^78nJ;&A{5ot|3wVT@p3)V}NYH2voz*OsI)~0Z0a31~P&5Kq=h+4t47YS!5*gS%-XuKy{|+4cC!=INT!_BJBub'
        b'^m&RH`zI6QtWQB}lw%g?tVNjub*H0pT1QR+9nFi--V9?-M~ws0;V0`)w7!W6BsLKzYZ}mliev@c$--oo96BW><3kxV3;Yei|1N$U'
        b';;jaF{yx7BailHM8+e}SBV-9phLplBA5bBkJh%tOq3)p80sIM`-#3jI&C`kT6wH}3;5MDsv-w09!YCG@E&vW_gu7`bF|Gqn0gGNj'
        b'|J;DGAzryu7WwHhS)?E6kpbFkVGcwX6)*}|0e|(+p`AVt+L-hP#j{8U{o(*{6K&zfU9`t#dcy_iuLI-$#TajX${4$Wke3)^Cj1|p'
        b'MT~y;CB|mB>ykn96?#MXa=pR-AB?dSZfB837SwuRF8ur4BE~~jw4seiKS^(xi+ZXW%@`*l52eV1=_N|<H8DvqQT{-LPWcn~P==Q*'
        b'as~3g8zA9?WI<(YJRgs8UPl@$;6EKW1b@0jVhjhmfK0&fS6O5h?9<@B6RLs>H&m}jI#PupF6ngCO@xnu>f<eo?1MWG^qY|Wue^&z'
        b'{mgTq;Z7PqU`V2QG)IMa$|9xE=RYHhj7ORLfk>FMQixGX&ESQ7h&wekHEIarzJNMNO)Z=<VZv9@1WdOMaWP%AB~`D5$%tk_806_p'
        b'eSLil{KJH{f{se)=|lt|bVq@}R;fm6pnmwZ)A*n7^J&Ph<QC7Hw-u5|AuM?wtQC2`%M%5>GYsK>>gNf=68^q$G%CtTX{}&LI?@S5'
        b'zB%9@-}Irl^ma<~Glvl8u)_^i9+!7L^;fT)$>E51BJefe&-2H><wKxffpRttIc?|@>g^Ev(8QC#l)1yuM@`huU|0t~D?sx&_)iBt'
        b'GSE(D2{d$%LD^6E(7GV1=)4V7m65s{wB^r;(f<VcE7jMc9*4>z7a>d<Q0j|*4>cWFg!)e$L)+5ns6yBu*SkFleC#(qX6{|}Aj7}P'
        b'#y+zfJbE4YKgKeHA23c!D2<=~tC!@dCx81pXk{~eiL|e7r0GjYKKMc_;%foU0!vVqqN1YV9+v~C-{^g?I|Y1vMHU$XH$^h)8D=LC'
        b'0=<dy52!1CCg>CB+dqNt|A>BalNbwuIN&CLp^7hhZQEPv@RN^tO3@FjG#s$WsDAoqer*(R;>ns-&o|#eUrRY1brLuN_X_y`1o&wK'
        b'&+jBsV?X*%B+QSauT(+31}xo+{Q1cu$D*BH7>PFBEsOl^zAUnLlq~WNpyOnbmtlYYWANK$r=u)D82m@T&J2C*2$2s*!Y&;85cG2c'
        b'^t3+~?vq7oT>NDk?A`=aa9=l)F~$Q{A7c0%c1Mv;Ao|W3=yxNoJ*?P=&%<1TIIkkDYtYj-#D9Ux4wpsd!OuRZZoqW-84NWMX%2^~'
        b'1;zrQKrFC`x&dWC0Q`Og^(gQKaB;XeX2@Yb4DbhnfXAsnqbza~)TaQ?&t#EPp~eB9Aj}D12J~})MBvZBi@;JK15m#vi+mlb+w-!>'
        b'xhPvU^qYY~VAfE^_&(G<KpAih*bP(xckdxh)Wr&37FiE--eAU<4wQ0?(E!Z#V2m+9CTO1pWB^U@*ACnOZUesoDj&wE1wFDJMgGuk'
        b'S<p}pWI;a!>QG=5paFD1;S5>ieyEQDPXH5ur+{c64wwbR0|~%F;3Z%QunhPf>3o1O{x8tK3cQ9k^A{i$$b^~lK+6B#Lwk6W#t(Bg'
        b')D1u$uo>6}>;&vU39uI^2P%QL5YKwxF!V=(6Tm6pH1KcQHi1jP72rcED?n`nGW}(d9Z<gmx`1BbF2KTmyY5M5FjQ|~I4~9n0V05C'
        b'U@9;jcovuqBmfJ6Bp?;|3$O}U4P*fpU>jfqwt^mpyJ$bup2|5;KL@@5z5<$oAAue~hPKZELunrXBGEryh8hob39xerV>|%!3E(T>'
        b'JmNb7T!y|4$V2_#gldJ_1GNvh3v7T{g1XN@9Q|lNW~hxy#+V275MTpT{*1AD6vk`Vo4n!X#Tb1MW+&R$2&fZ*DS%-#l~G2U<Ds7q'
        b'tV7&6z@MRC3@ioy0*pc*`5V+Vz*@iptOwHJcO%qyfGxmwng*~7*bD3jJ_e3HO4Iq3uZH?L@Fj2-xCo3x9<D$I>$MqJVrzx|I`BR4'
        b'Gw=(*P@#!vNFVh5)GzTN1mUEB2QUQi1vJ14<S7kU0+@gofknWnG{{Cmc?ALgzA!jK*c!JSbD3q7_oo|;kQGkBd;>Hjbg+a7;s<jV'
        b'#_~G&sfIoV;7{`WLd2B}ECX_ZRkTk6>wuR=(>x|keFy3ij0b7JHrjSn;6a{*d;)#9N4P-?^8}b3FndBD4gGECXG6_;MHblvy$<OG'
        b'0{xgn9fJ&^=7=B@{Yc9XK1;xZO6P+YEEjq9%|ymHE)Mn0ON?3b7^6SbV{p5LJdo{oCB0`QB>1j`WX)%c^{{ttk&^BejIoZE6PWuK'
        b'#yI-zA7-D0z8mNR&c1v)DjqNc7vLVc2fPEciUCaDLrTHi>P-EtXH;;5XkvuC@KpM%jIp2k2PUq-m<X&JcRFfo9^^;p6EP2v!|zVW'
        b'n6~wdakrT<R#_QiINYuyOdRa2-jE=28DpQ7#!HNi@Z+D&7;UhthrhYNO~l!ceE1<Q70?B<liEYJRKR=_`VEN3l#c%Rcf<+zW0-%&'
        b'!+tBm?FBvqE&+vG(I?+wj6XrIL)eM0L9SSNI?68taYD5MdB6>zKOJR*nh$IRX04=c$QJd?$;TrgH-+aRy}dv+&<23?<Zik+zCN}R'
        b'JP23~6aWW-2H+>adzCCw4=e(5fKs3haDP=6=`$WOCdNq#^it>vP!68qhDH#Fylw?zfE_><Kn^j+NT{;_1CR;C151DmU@k2mPy~bn'
        b'@6m7w<MUU&;YsMv9>DknoIMD-LG?p=fk5LnS>*e0-}wX2p9F2=R-=Ewtb+ZS`aIB~Zc26MTX7-d1zCCWxGm^caIXdiWNbp*Aj!&!'
        b'>PyCW4EDBslog0UT=g_=Ag&ht3+6P$6Av}y3A7uiJ|XDakQ>cs7~_(EgVzDG&N9YRz_<qRJ76ySEdm<1W6UpvoPoS`0CI%m&cQ$2'
        b'wqC;A198W~y&rLw!mbeLgMKdT_CX&9m98`BzGaL%VO|1c024zo?}ghT=nnv9n5$uK1I_~1kLe9Q)q2AX%r{9tzn1h5Ne9r3yPm%d'
        b'_btWfLokjg!k7+Bhdu)845%+aeGY04)aRidgc=X^I@GyPLw2BjK%E734b){&v!EV_YK3|k>ffRELEQ?~`#o9Y4ybNB!LyLA5$2h|'
        b'B<P=064D5{ctbI*6NRA>vNA`yFem9+OX-3<XJQtjI`Ez-k8#Muo6z%;uC?4P^vnJyNY#77oFg;x9{MMEQX%*h>8H=<C{$a&7y7OW'
        b'@tBUnABS{mXk1WlK%ECQ5c!%05Fro95Zd!{n6EQZqZjyHKJ={~;Hc17LZ5HPcr}=i-8@Zyh(Qjza-eY=+`8Z<dmr*1D>Y7rItp=4'
        b'hdP<Ac_1&(LB9sr3)I5y0@Poia{r`dBIakI{uN<-1`!er>_&E0!R~9Q??b%;wFN5DG`$SH<^!5%l|oLshD>EBA5y3$fgjF>eH7F+'
        b'P-j5h3pIhRK|y^9s=E#H2GmJV--5ctCeU9|2(=AmcylNrMbMvxJ`egDs2@T78g>=X-{k0fWZ*AD>HB`N$a7HBp<aXfC#W@`&$Cc}'
        b'fjJ7Q!k3VKgbjoK3FxWZwiD&d3l-acV<!3?K<kpaoud5^xBxpV{Lr#(h1!iUrpH)gGt{}SgRhKdjfuO!!+;$?DUgP-ZArS`P>Q)!'
        b'-n*FB!(ZW6^aJQ8rV~@*Hoal@KhZx-tSQ4xOn!u;Yby#m*-j@?6VKBf7E;q%GtWz@c?jW&NlGHE1a2F6o#1CbroVkW_`XR2`-wm}'
        b'^pS#_JHn?CKB|u=1_=pVP1j%e4^&8pRSDNGeg-q0V4qsD8@w0zC$Jx=0{j}NoDkJdy@Y>-ItU<!I+Q&@N&M=e+D2e5X_g?*)e=JP'
        b'^EVJ?bP2)%@%hN(KX^XvN!FM~>0=y1mOxD}11~^W>+5uFLqdjN0!XMMUAw$5A&(*KA|Q^&0mNXQI__1yL5j9{U=#9BXVWnEBR~Ie'
        b'&m{6^=;{Dx@&`B|5by&%S0ijYuovh;dU;6iE9egc(lGEg*pYf#KE8hlU9%d3V)7Dx>j=8S%g}m|91`-_MVG9otklI5Ge6oXtc$i?'
        b'Kps?xCk}BC(7YG%PX7>dET9VEbZ~11{pe-f{AfZ$od}0rJ>2Smo8@Q|6?%iUQg6sWn12Bu0HzGk2ku9qUjX@H)E=5g2fr^@Z>S3h'
        b'H#h-8PM_d;j2o)14-hvoAl|X?_X<#&LF+iG+KD*kj>LTbZ+gRZsEL1Ojg#O$6SxUC6T-|j({(%&57Ne)kPqD&j9q{nAV44d`9W0x'
        b'`Csb|hky~KkPpy~R8aMR0?2648$#eG4p_Gb=>es%j{)`p?*ourO*ha=bOD6yf;me@3|Xam!(8BOKjOZpH{{<%y!Z8nt!N|N`=G~s'
        b'xbGi#|K8=@Y5n?xyF`b&9S1lKoT(YO3ETksfNsFB69u994aS&oM{nptyer<+8|snX1t1)0n7|Jg!A~NP4jLqmL>SP_@4DU)iL|TG'
        b'R}TOrkgj=S4gh~EXk8-wn|o!E<AJmMzoYa}Gp3%7+UM&QxeR(6)EC##aZzuWg?^1;-H^71wjbAmybawfMsLVOTwCEke;I2uAaCYQ'
        b'@PbUeAq{z>>k9|o&>MEbeZ^aPLlzK%c<eBL3e*A@fSZ7{OctpGMg#p+fJfsUTPDu`={)p0=n)CC703e$VcrSkL*E9(KpzJ@_AiVB'
        b'Kwvays)nk9djDVITF0Vt$YF?UI1mr)0LB1uKmxD?coi^Zqt1}0bq6pPL>SX@)_4)>5||ax9|98Bg07&473EKd+6_GVXsfVV9CI1<'
        b'ZPpt&3+My*AigfRCs$xz^cU8c2fKY}V<y@rfwVVRBY6XDvKRjPP{+VNKngoKa2Ebqj0<OBXZ{=gw!xZ6K4aoX_wz%l=~^Qg57-7*'
        b'gZS4%4%&ryo;e*Q-2_<)JiB^OxZ&jIn9I~++<<D3ha2X?UJCPKKv5^~#e*ZD4*{MB4!}=0;_&|hGz6Sz4^==ve+%{hb<{YC)M$o3'
        b'9ykG91lA$#fYX>a0jCgW2+XsgpKwZXG!t@DvyvDtpsh)xAiu#aEeEO@<pb(~_;=7}fE&;sK$)FT6VcBW0sYY5KwMo=x89OPKK=DC'
        b'k=-y83uM<XF_*-cUFc5?o=_zK3n%~?Fc?VkThEMxzx6-@aQ`RJ?V#Q;9B#JFtWk=1<bVx%<Dk~Vj~qO?3u+ANN>RWX{iq5zAAp{W'
        b'{sD4wSv(;VbErJb-(7_C(|`=%!~K{KpMwk!cmY*F0I(S_?F6rUUvF3g{i65uhGeL5R9^)79BK(b@(A%qIxWx_TtFS22QPG>T^tj}'
        b'yy!*4krt4*S#Kz~2>Bdv04>1o(Z~ZpN3yEz;9sD5HTt#<SfNJU1Exp94eJWgPC!d87PN)ig(y*G=(r?{eCo0+@<|{PWitTbzzmod'
        b'0nc5g{SUm=hJJDdeX>y&nGP%g5`kGj7GVAeG~UniJ7XXx05)JN>@NU52-l2s&jQ0`p>#p~Br)r&`L*tZgUO5$w9c0pOh|VLrEizS'
        b'BnAEZu0o~(ssR7LL*4*%T)5%JJM?>@LB$<pjsB-t<6OWB90PVAfF1nw!HvP({}lYn53$BT0HVm+`@lrF$3VW#Yyy8ldY>OG-kfW-'
        b'T1ginD=-(2gZ&c7z<y9w&mn)a8L}mCdO;)1KLZ!Og?t3`e}nQjgWmzOS`Y@1w}Hlh0`LL+fH6Q;3+;D5Lng0A`w2n6c1A5tO--dw'
        b'%J#KFj&2p#aq}QER6$m02J$rML%>AnS3thELCt`B%s)UI+J8Wg$%xyEGVBJupN4(~^lt#s(9Z>41JYscy2bO!(EknSM%k=TOKDgq'
        b'_`mai&UY2uCU$_wc8K|lfjSF#7KnG*QM$~Aen>D~Z5cu?d`#uwF8ZzbK1vsrH07_0_iQ*9b+FE~Nw={!>h9|w#Cyk_kIK9T8HdJm'
        b'jrtD+P5goCenNZ<OHkH$l-&w-AIj!F_3@e&zj=_Cf#Ys3M?C-eJ$|j~<%la;wF{yzts+Uk3|~6>vGbjm&5vEW3I8-tpCax!)HO{b'
        b';_uhOshCD5Z+=30^e=u2@@t-jc4N4Xz6uyR(XKnivQrwQLw^(X+zcevvc`$CB}Oyk@(VX)k!!mlSb3s7g4fY+QuI4}AME|UlSTFc'
        b'itiuBqx)V=bN3IB!2$YBmaePQZxD1{|IiQO+>Czvq$>T$NWWpz?^Ivjp1xAhLJ)zvwsFXGIwwCtza?FTz6<50-?8a;64=u)y!id('
        b'P89uy0#rkP;+%TI+N>+A0f6~CxP5nm2=hcmwfiEU2|*v)BL}{-=zbLPfSzeigxZR9gP?zlp6VjPH!m@tu%8J~Il%$<YN*ft3bQ-%'
        b'O}|0?tE}u9`mHLx<mRNO%BrFW1u@TDdCH$$I`|?ni0P>4H!|a`7oJH7Tk(u+*QRF<ztZ%~j-uhh_owH>UyHJxe1B31{DxEiFeA*A'
        b'$g=PWg!oP|8H)$!eRkqWzg3}81ekR+biyOww|ty%aASCq=cJ?b8`8C}d=2Iy;6cEYm?!lFknei?ar2PrQ`X(lM8(l~VGav@ClL9Y'
        b'QYYjq{~6Rl=yR8+mG@>03C+5_<q$LYtUk%}lTQ)n(?vx^C|g_<cZ>QpKZQKevPL_*&@WCu{=~#5E?18HIeZc`IQ~ekRUU~jn6s=6'
        b'jk1r6N>ghltb5^#eoghe;YakAh`83zCXd!DBO3<4`1DI3y?1zO_pb1|pb?XOm%aSd?%;!w2#>rBiQ)Ms$YrCS+4(nOjl8aZi|22{'
        b'+!@8Mm7wmsPAIQxu1zk_kNRQoYk@Q0*c&zb>9e-f!4*+|QO)}N%+$kCd=4oHoL&<(ID!6MjCx|l@^LYTicjpg*E(l>YkAZwJ2Lj)'
        b'K5#H<rEkFf+LgzmPW@1bVq#1{8T}{%X&Y0R={L_rq1^NePhmnf>i}8<+A28BT66qKLQpU7z<xqL<>?nM96MH4QDwU&&MmvqX6vEf'
        b'3Ae34+P4xTo!8Otv{{g82<9k#@Y4-Hb8gEbgMmVCw@A95gs!{Ny(N#sZUsR1g;1F$2Ku*wx!+5Sjo(R(!kp^^o~L^P#@&(_>CsKP'
        b'=R^v1H`2TgyXC)N-U!@AxGEqA`YON;a7U%meJ6D8NY_^s=%?d6+#*v`QR`EMeFZ1!_ict$&#G6rMSi4oiwp#w0A2!C0q+C3z`$Iz'
        b'6zQ74yKQt_!q`_0H#$Ee;>TikAKdFd6wFVT;qSmMK?Zob5q7gM?~YHW^JfYDupVVX9;)C!(yliggX-nw7C9ccfjFtWQw_UQz`z`Z'
        b'&QH=1hRW-v263*i8?tK`!Z-Iyj4=r74I1x;O6Mc=n=hS<(76qrkI*^Dp*s@eX}GiSNB4q|(|`(dF$3h(cz}-UAN-BBhXZteN9TDu'
        b'_%#7^pM|gw2;;ur0g1^B5I_O=036^Cr~m^X1?1EZ<N^9-`M>DCQ9I#Aa$j~nujU?uvQS-7)9asC>`-tLOKq=k095fJy$ImAtX!J%'
        b'EPRzqM@~pdRL|6;F8(%UmDX~&m-E`Vk&~Fiazf}GNTG*%Czsi>bMorw2ISYZ^)smYS1sqo4RL(bTk%n^eShy5hWm3@o67Q0@9*9='
        b'-`Bf&U$3xNO`-ED7*wazm^VuEtsyF%D(ky^D}9?<cxamX-PLQA=am-9gNx*ae)=NG^u$qJ*0l8lZ+@$aRhFGJ?z|CB527yY<p!6s'
        b'+%snebAPgIr}msYmvx;%&6fIyMU%X6>niuY;Bz*jaHx(C=0=n(8M$*!HbbhU*)dY9@vBq0G1g?nn;qj*^5#g5RBGJM%+PRtoKzLJ'
        b'WxVT5XQhon3^QxWJxfd@cW$g=Ij(cfNDV8^-p_2*aKl~4sz-HY^<^8SZg<4{vs3y9&XqpR`c`^GzuX&|-YbzlnH``a@!!w)8#QOK'
        b's=&4+JK)jzN9a{bb8L^y_mkVxdgm;Dw8Wu?eF3JFeg=|j_p}oERd4B&bEI_&GB$pWH0!tc9b0Dqsh6Dn-tl5DYLU&A6rC?g9qKz)'
        b'W?9f%6QIhyZAt8{3>aM;Fe<mW^S0U;7`Eb$VY;+>ozf`L<;N(@F)HH}U8R>BHznjK8peSqx6otRC7nK;H$9q{TFAz>@?1&nRi1<!'
        b'!z8Mui#@}O9WlMfJ<3_9goIA%jkq0Z?2RaP8@My6*yeAEqV=$Iqko>NQe}BesFXoP%ir;^kLxY;sGm-cJihNyx@_J?K9@ccDufG9'
        b'?tdXPte3M^g!Pt7YV5<`m%o;4Jr^)7yN*9Rij94ge0jcOFgeFcFaPr|&T!?%oU>M?d80Wy*)5xuhS_+%Uotm%W{pt6u_K@M@VzRv'
        b'&ZuH@jn?H~)npreI$s)TW%E381Gw+D7wYR?Z6Ds-m|V$9t3Qw7JW^J37T;c*O?qH5v)QM&SeKnIoLDGM%U;itu#=5$-|$(#gc+r%'
        b'@UZ>NWQ}-!aZ89Q!`0TpY_w@cs3StPFOJ#EY^o?{B9xq0iAHM+*b>V3*hz18K(<PikzT;qgiYAli?dx}XW#ANh9wVGP}fw|%C4T|'
        b'1jQM5&W#(M?M|wO<)&Ddavr%_&rRmNISsdZvWF@RWy-U{p7rbmg>`%KROyi?a}!eE8zS5r1Hx>~%hpK`rwutSEteHBHAxIAt4>+S'
        b'j7(kig)Vjd9xixQf`ao~+13-;Z`OnqxO0eulW#x9%#xdPt8-JfACp=x^whKHO;fGz$ECSi>#%ZJ?vvJ~BU5t|#0dSvSAF4Mr`)jZ'
        b'g!+>n&RwG+t5T$^y+T)MB#3QQirXp;DfN0?yUI(x_erFeIcMH9(%Hto>G663%^0H4C67#<cW&UWILon~KfGOMKhk44((}8w;y&)l'
        b'x@-BQXJDUm=-wXAQxg!t{YIaF_jLTTr{Vpca?j3f8f#AIM?LC&Jt5X&&cpmRJw>>84&8ifJnm8QPmOTwCu}zfaXsMas)yo00)A0)'
        b'jzwp0@i@aED)q>`85)LYVx<2AU+|s78f|3umL7vS!(6D07aq_o*iZ6>=Q7JB##0P3mm1SNaKB`FPd2M64hX0W2ppECtkFnH4ymDs'
        b'P0B_!=Fd8>I<~q-+PPU>dw1ZT^R=|dp>OnL2M}{vb++xdJyqV8HPmvigd1VW9H3EXMh_ZcSO5WO>BGAyQ>Y1{ve7!XXAY;2Ufdox'
        b'atG&^kER=v5#-@^oGoXxjk<wzxC~SB{mA1U_LLsZyVF<YpT~L5v|E<b_&HB5hLU9Z><A_zG$OjQPy>=j_cTO<<Rxo07y}Y}jt}YB'
        b'EpHi8J|ra{uCV`D!%6AItRO?@J#}i#?b${&70dHIn<w-<D|^MAJIIYn|5kO|9#|Y0TWLG(IpOe#XNv=;amT(GF}3o`J7*p_a3-f_'
        b'$&8>i`rmffc#!-fs&aXDl6OIp&$%Rp_|}|d3e8`7naXrjbzAM#p;ij-%K2ogz2EeB#nX7|`aH>R+{9vs>UGPq&C~4>6%mez2JI~s'
        b'_sM2ik7ImK!}y+Jd!YYa&d>Ck%BY>@nc8ux`;*598&7rpC^6i~aT+pwCo;CFW}}o$dn_4~E)r*_TlB}w`TV-)>Un$mxxw~PJ;w*v'
        b'>?SF!I`r3W`>)-`fKl8~<Kh5qirPM`r(~Tvj3v>&Jz*!m3rWcd^+C%G3m9F_CdbgqQulV3%QPAdnu>;Q_($Y77P!)hQJnorVR%kB'
        b'6R@DRV_+OqWjq*kEEl^spYP7r#oE~(vsJdiOV~L-Mu=u_gm`avsqu^?ZnA!Bq|rmAUoyV9Mq&B28)P$T(6UwYlZUCl?5+uPuhaw<'
        b'YXVX>sYQ)8NlhC@$^|}F*hv>%-CY@ostQQSRf`(!OKL=s9Vnl*&K#piUH3JOxr4@B+eOpOW{LkD^}g;6;vv=BL~c;2HmiiI7lh|$'
        b'G>Xmj-T4}Y;80Q9=ep;<z{?|SmoubD5%gV9G2-~e@?Q6z0D30X+DAO-q0oZU)!Ya)Y<lo>@|F!-23x%fiph4r$r~a@2ld4vP)e0b'
        b'paH~=(1YC}R)r9-0vSW!*ZV0$w|DCcFO{>F!$N*<^CWa@cUXX*<q$Q~K14^g(0{<r-*RBU?mP4=2MM$LjH?%K)vy#(r?A;>kpW@R'
        b'D$YABdTi($-QMi<c*$>}ySf!*W_-YJuaN|max4k`KE!Zc!p4PHsL0sa?{~)w@A4AE_p{&YHW;px7^P?vQ4w9(9quqpP((PmC7dKe'
        b'nXQQp3Qz}4SQ_N5K#_A-a#I(m-P{Q06Z->iwor=%dWVELTbiBZZcJheSI)L}=bNR9Ql+(G<b-%(yx?Tqi2RZ*iXDtSyIUNG%9-4X'
        b'k|uSjvPH&?t8|P@nV?CX^7m0)<{TR5-{@UylPv#-u5XWP;>sSM%p@U%Q4=1Kmu+T3ARxBMpz^5QB|#%9?Lw>(t=+E)g6Otei_}M#'
        b'?j}PU1Esqds)E&R5{m*#1>DwG?IO0Rb#d2fcem~K0Z2p;<Yiwd%<tR@w%y<N^Zn;0_sqTLo_p@O=bm%t&bgRn`yH*jl+nvfVyy6Y'
        b'xYvRtP_ZP);1*;Wv?XrL^a0oPvOL#myOJhXcyX6Nc5GR;B4csG2LHbnWh>geSjOV)aJL)8_T+1Ng8<81F3a3kUY%L$ibwa9XzOep'
        b'!B~~IVa-Q*?)t_4j}~3bbDvSRA5#|YQPwIlD!gD*2-R+-dBG1zb_@amx&aLH*C~195bRz3FYdq$Rcx3UR6y%;?vOEF0>heA{+w|C'
        b'My}oz&hS|*MU}cAuip}GiMrF8b*I5ma#esyKhJbe*q5S#)cx`f3{Y;^1c*y+^aLhP%JfY5SET1kCouPbF8vN4lI&}a33|j7v`D}3'
        b'j&_xnEDuR3BDQ#gGMIP;83Kj`NQz!}r^L;f-nV&$8@5NUXp4(hJP9);vg|YFq94`=k|d+FAC<RjO9!uYTpVjpFCSdV9G{z!_D;$J'
        b'E!uF!IL3r8YzxgtrkSdxrsiBQ6aVY;bM63Y!~0!J_Z*osQX5`Whx-;|o`^e56$dV|pLHGB!N<V3(jd2gHQsjY!6v6SQrgla^X5yP'
        b'8<IEgI)fV@!IGCBNyB|>G4^8jx9}$$W4+j}C<*%}q<GN}X*`PEe;-GdL>(K?lF2q+j@T$EER8l>FG!NDN$7sJrsb#{8VP(q$F7lj'
        b'g&6DRcJ0S~4`PKcE3XPM&nM%pr^YYO_{?MfY#hxX9`&hl@&Q2JDCnmu>rNxQm!+|lAdjS!z4-m4)HYRa8z^^%_v?Sq^&G}rAIU!T'
        b'?E0g;A?oyQkd2S*{v(S%^<1={+TEBJ`#l-;?=*D7$71~7X?Xj)%G2|k1%)+A!~385>X0@`-hbp2?(lKRXLe=a#zg4#)ps<wv4iV6'
        b'ByZg_&IT>YXu8rQ2YGKgN+y#rws&jTXz9~sSI)}Yo#<Za+!I2F6hoyee=2SJKTEd=JC1Ve?`PSyQpXV>166<Fr|S0qvwEx0I6Phc'
        b'w?CC<|IhMmLgV#-{5K2iml2Ptf^prR@$^uX&?qtJUK>w0p@cz6Pns^>1uD>f0hLbo>Z-@}Q0l7gPvdT{9xVDlj(e>V#`-JWtK*C{'
        b'S62mT9-o?YMdOBo2lcOv8?2PR5>lE^Rr(4@)qEPScS1UsPZfF#q_g#o@x0yeXO8|QNFUHY1!;_)h4lA)8m6~H8qTLOy$w=1pN8uH'
        b'0BM>2myrHW|01M2`SdsXGDx2`&}=SvFjiLoJIFqve*w}}g-HUFDpIc-Z{0DzMyTI5PD%|0k!q2mGeeAa<NTeNVt**(CK&5)b<aVc'
        b'w(GV)x+85lW8I?u9~_wO`R%yr_=tZpO!vsR_4s?<ER4B|8wg4F)8n~|W#l)g(JYC9keT%1>le#%#Oo12MhXr32!mc>(9h1!`*`m7'
        b'GX1iZ0Lzma@<_u<Qa>@ad(Aj0&MZ}SndO^bMw4q-LpB-P-lS~IZo4RBWAM?jF<X_AeG+d7|1KJL{2FscbxM{+d4sXdt70mztdg_K'
        b'u(l6m>?K3R2Jd3QnUftcn0@j1+SRry+4-#Tb`ZBGv9<{5(>rXh$jDca_^pzfgqVHi_!>L8f)s6gCA~uuKIZ1Wi`9N_|L~3Yi`j#*'
        b'_Mq{WRr0mpJ7;-+C0zC_>0ezN2CK`%V)O#dYyGY93>UMCy{L>SGQ6*eci_f<aP})><l7%7k9Q}Iw<ZFMACpXqw*9H_%4WHHTYJ}b'
        b'`3t44*-|pOy-w*`E!`1G*6o{(8<%6n5118L#RDBPF{`_F^V2(iw@G4^ke%C0LX;c#;l50)cJ3F;N<zqu`(|}*lJ76-Dw1#hO@~p)'
        b'771fIJ08cpmjvv^*j94fBOX^jA@E4XTSLYTQp^;B!JuS<ofe0wHwe_vF0x!5Gr2L)zXq{z`)jy34Qm$HM?pWVK4sC8e%-w>1L$Ug'
        b'T)GDr=U^s62!DK!W6eaNkn`oBU73#0r^cGO@2b?!IWPuu*coUHoM;Rl!`7~5Bcz_@G2R1{icf=F744tzd;khQuz3}fS-aY~q_um@'
        b'`vIDw6-!JJ(w0?9(^}j#6N`D-^ub#8acs>7@lo`B_XI9(<j(IO;|C8HALhs?aXYtqHtxH??U>U!n|(&$E^0@d*ifR7p6?uUxm((|'
        b'D@)8$>kKSr+y0`G$FNNj$0^PbkMF)XmYKP@WwG2V4zFIUbh)SY?Wa6{8f)1jch}iI?id>izAOYwKDusqy(7AIcU4Anuv)^o#Npec'
        b'aPcXw^`)^Ezx?CVV_mmwneQvXz9FO4FGVXh4;sQGE`=Cy8dget%^WNPAGeI1Zyp;WT8=9H_Goj)povfdPnYh|>W+?)F&{UMov(+-'
        b'%^_-AG_*tbZ%@^~3icibCIj8^EpnLWPX_>Eh{&a3-JXME;%~X>J)VPOpqfI~l6xP+NqqIfweitGRw1@Xv|8~iQu369e1kkn&LL-R'
        b't6Y$@p+k&WJFl!?U%K&^^KHLlbDv~wuXtS_Ua5TfnHk&D1<%Y3aqd4*S@hzJ57PxN&U`g^^XeG7b5B{%K1NhWpkNR`yHB0m?Dxh$'
        b'CPgHaAre~4#)hO{;*&%&iEdo@EFSzn+^s3U|9xfa^J52zWa+lb2f@;{y`-;vg_U41OCc9S+idfv^Mbi`Bu-~#@-ZfKo5sjcmcTmm'
        b'3zt3E$$$PSYgN{Nr#2^X+7n9TrcH1tTJ$t8)*?biUXt&MCQw;YN**kmI`W#33<Vd_g=6eTS8Oe%C(q4j`{<39meN;ee)}7o{iv}G'
        b'7r6d*rMkWJL-0)g_C|Yq>A{)bK8?Hn);O2mn|*h0)ZKQcyy*nmidccgH2DTNuxpdaa{`zI-*cU71K)mQZRgRIc7?Y&#ic0}Pfepl'
        b'-JQ*xS60?kwz`6`wh%1F*;1#it}d;nl>x7$+@>sb+>cvqe;9SZo;>E1C^Xo8f1biE$zvMv0TXp{)Ekd3ByBst#jZs~pOVH$^9}-*'
        b'{5LNElM(PSY1QX3FC_o1ImoU-d2=Pk&^k}lnC};uJ$ekq;Fe(E)hf15=_1Em)O<dK_O80m$l#bt*JAABu(9*uW3J`cq@?HkmNxg6'
        b'W&vwS_wUoRxj%_M3(XXM%CS_sqH;nXGUlZg)C%|QKiKB}^s?woYqO-Vk5deM?-hLNrxz*Ket#|q{N^D}appUZV65ye`kr5f+5a?('
        b'`uW``x+@4g(k-P2wg-sVv!0JX&QkMJYgeTSV^Y$Ep7BvTi^{*7sv8^CkBmBrTCm*HU6wTaD1zq`jY4S8^nt)sfZ2x-$VH_Ag{}=4'
        b'Tfq1IKck9&4}&>qJkDWcP~iGCbf3ZiXYUzhHJBnF$<L3m0sS{Q`<MR<ZV|VBHcBo+f;NB}QAE$M_oF{mykxds8(mZdmPI-OJti=n'
        b'Pdg<9m#LdCdTDaS;-!0r7X1ex7XpwV<??pZ`%~oM)eD~sS?u);#I#)&MmO0L(PP>(5KXsv{{rCUhBK`s9^FJQ#{BJ^V!4o}nq&Wx'
        b'Fkj|5If~(#?#$g~6PZm~Fr^PP89I92nIB>3I1syM=>kz+%jnX71{se3emVWEb%wniA?}<|M}#XrzmwBLXJP1yH4L+#Mi1hn{b(i`'
        b'+>f^&8Z~6`^QjFzaIaMk4yZrm=1Ds<$WZYIoIYaIb70gOr|S}99^3stwW9|3Bg9NunD||;b<ZgD)XTF%n)ioM^YUQ(4wR#QKWeaI'
        b')SpmVNImHFev%v#-BkD&sxS*>&WWO%)aN)gbTs;h?oFfTUmk69yT24Q3;fS&fFIFkL7Ywj7rtxr40ur<%Aet=(GgGCsFg;PK-w%q'
        b'6zv=}0YHQS58+RA6a4i&J4(|i5G-_1+zC=(5Mhd!##)~p?Qlzg;L=fkzDO*2NHh&%3|30>OCyCRIYrWlC1<pI$>{mQ(Jw_nQ#1Nd'
        b'dxyBNNb^b?Q1>42M=>zuSvp#F*Z%JjK!bvnh_~;3&?LeR?6EHzCByT6$z#pNz}P9o@*W>uCQ=%do<~OQmrw=8oqp=CBc8{nNhEQ{'
        b'Uaob;C|L%CJ<bz0(5Fx0Q3w%XiaR&#%MjdaX*Xxwuoy<O#pb{G^{Ua|(fo}MpaO7%rNbT{7zV|}^_WV4Nm$EyJH-p(=RKr^U5v%N'
        b'z%Iu?T}TlSxcrzDW-{)t15MUtj~n$;%}&WKFth%^g}mhT{0V#`Um2IVUTFT;SLfBEFcOnNLpU0w!d03!>OAOWe>10$erfUyWa{;6'
        b'smsE1IJ&m59`wL}mX}zUV$Gs;eH;0!Ra=EHr<y$Wh`_A)O#j^oiUV$UAeK<WXj_8Dkq>=<%^MuCQXTxo2pc1CaWZC^9LX2QtXd<6'
        b'@;iAJcKp*mi2msNM(k4~#lpPak(i=Q!eU9IsP*0mnq)=fqUfeg68jIR*o#tgMi4+@+WigXi`EueJp*mtPoj&+*fXtOA5plUJMe<_'
        b'W85nKq*?6$=Oa~3>kljKpP<4eS(wE?k|qvGNf)OHAr+dhT}~G{?oDBvO)%=F54v)5OIM%79Xc+i$Z-M0ji%a-pCIJ}t*p1$STPu0'
        b'aocO<&*?`1ZCiq_{;UG5Xk$M&-GqnQE)630S^?IJuBmRsQJ5N}qw?Mw(Z4lPqQ<Oo;7VfXbwq`zLRf!NF;BWvv`P45T=h3cbZ-JD'
        b'@(B_oyh2z(_}|3mNjLEku2IbIvm@tU9U&#j!P_e2-ixxPW)#v-id|}GTMo+=Nw&E+c-=z#Nkosma%6YQNTbC5@Q7EF*%-Y0E%;4#'
        b'6=&}L!wBS#LN3x(oV@#wDAx$NC|7ah?h2GUJmM;jn%>*3|DFr%OCK8Xsz8ql?1B+xhw`fCSu(``oSF<p8Z|LMpKfB<vwy^(N(0@J'
        b'w{PSbsaFjX0cHoIN^2H_PUpAC&d(SD8_Zvzb}v_&qo>YEud1GH5M9O#R{=J6T#auW*-PgupcIGh*UnShUm9^IDZRx%zI!Vlp(T-3'
        b'W3=SyV+NO`opxghb<wmNA92Z(>aHZptLb+Bx;-+IHAFJjFg}v|_xzp@DF)*!VxBltjqZfr82;QjBDu=@eyshSVPINp)j9DBkNrCO'
        b'&k({jf;BoeE>ycptNX|Bsc@~+%fyA*9D1#j)fJ31!~x*4z{dWQwTMg>p?U#zzHRv9HYnK;=Z~RIg?Gfkze#b=o7k7a!eokv=TSVb'
        b'47jp$L$)jRHMFf@H=z;xn}MHACs5<Hq3JFs4qe&LU;N_aBTu!S8YY7Sp+*{a@Bv=}At?F#3iGGqMdbe&22i4VWMn!#Q6L&LdOI+k'
        b'w=X~~LTh_bYsg*<#I1JK;+oJaEVPJ1dGS$3CDgHDWdOH?{P8|5U|tvEwnsfO!pghq<gN5bl5_ulSFnh`^v#tm0C<uHQ9pNj+)y1J'
        b'wMK5A4W%`a%0yw6%Ow$&eeSN4xw1vmF+1fW_phIDMk<weY_>bQm>?TyO68q7BlJ}vdcn5Pf>DwY{yJ364yAHWr;Crh5>x%!`~!(R'
        b'@TV|M@HmE^#yv6oGu+h(H+_gp((F1d2+>qeH-X;Ej0~3{`^y>4$K|l`C3nTltgNIZAu$y;K9*8NG#?*CcVig3R!cPSH?N=&lNJ1('
        b'8x&@<?b#LmfUalQ{?%}5REVy7*#0H_!R=oR^TR+!`*1KKhrJqmmlQKM-Q_P_Ms&u|A*>f{fFzW!|A9lVKKMAJ+B+dB`YXfmyR;^7'
        b'0Wz}6>%Zdy_X5~24J+NHP6_|g>Hd8AVE7=ekyHiO1!BtDPY%=Bxc$^{t%P-NvC%S8vMclfx?_aQAT?kCBL-EJ-LkobEwn5U>?E-w'
        b'0Q}r$*Sl%ih*NH3`S(l}yzE#od;M^O#QxSWf5+_u)vrawgOD{0$EV}=Bg2_4x$<;-$m^ALEp;8$G>R~HYAqP*=MN1logKEgzqFr~'
        b'DFcyf*7DD&gTvrwD9_5;odVk{d_(8~o%8^IUoJnaP64%N80>SUQ<hmLpAJ>?W5h6e^8<l9_+A`_g_{wHNPKnyZp_0-TA89`mWVb&'
        b'ZUsg;hIQM9op^0%1>vMMOohr`I$Rf)n8F8g2`lTbo(`23HVxSM{{f!<;pYI2bNAL^GCBZCbgJ`|UP2htRQO9}v#@@Ma}wl7e5vXH'
        b'Q=NRqb^IStAvXBGfMuWEN8(fsrqP5j_Doe<?4|h7Ai85J_H$)JP4}AN^J|C68EtQ(;A!ful#^hN@gdA=wX}?JZ<(I!wLGDby4+y^'
        b'>wYz?osM1;83-DeGkm`s<B7VjJ7~@Qz-DQ*NW{1^AxAF}Q5nPMz)<!d2oK1SdKgSkx>(@<nxox;I}fRyw>@dYEd3i0Ku_v04S#UV'
        b'vv62#3)DG?+f#<A`5?cgi5JZui795-iwoujA35=BN;}+DBWJRO8R@n7l@xhKUD`75o0vOANk>W3cX*?ubiT~}mYxh%HfgE&VKAeW'
        b'DKce~+<i#dxI?okQKN|hdV{gVVohRVwx%vIpPDnASc{SdKCU^57e#&Ni5T`uMMqBDrXq*09764BGuj()bcIb59W4bV3C+MCEu&OE'
        b'q*vBysSpq|z9|s18fD!MjTD-ShNh$>G?fHRZHA`As43AfiX(^Q?%r({7rI1(a|GCb`%e9;HY`4UIe#JWl}fqio7-29at+ez>hQ`Y'
        b'@S3mGq0QIz7v*fU^omo~&Tp}H5NKOk)+vYV(`D^}7wl`LRr8zi`q!fXJ1r8B;R$I1QkWTd_k`X}h00vGFsL}3`tmk^<qNP9Y4Y@9'
        b'G*PMl+`dvFuXeWcp`-ySar|&!uath_rT%f7#svu{WYp!`Xj41Q$&W+YvYI&~MWGYahwxaGaAK6Ybo)xVT$|SJ<k^<CtU&zT{dah_'
        b'QtI4oz-Gk-ur6;rW$r4L+lp-V)3>h_$-z%^9qQU#>@@BQe$@8z;!LNEjB3U+o$a>9^4!E4Ws=P7!u2<YOvfH%;=;jX@QN|@%m*2T'
        b'G&e=Yn586<?tnFTI))jRX<N(~1ubcERv~pAd$8ImLl=;krHmLe6-i*uF^`;+g6lu^0N|+?K4>nz=j-FgC-w*X*`b6)86Rg2e6#BN'
        b'FYp5I)^>j}1jqnxQ?`ol$86H=x~>1?ZD21$2y%rJsiz;-l_MrIDy-URLuWV2ZJ@K&6C9M`nU7ds?##DU3f&D_OnNC(IdT7;dFgHa'
        b'?*h0))3{2}*rX9KI$hJK$ii<Bs=$zS{hzqV$k>V9&Y?gE?qgXAN$6c^MdF+h&(R??$=A4@GEd_W=<R8xy~g-Gmym?kz>0LoHyq~i'
        b'@Z~n4a&P>s+$JM`uV&t|+g@B)A`*clTUOlOekSJ%x*(~2hq#O1@6C4+n7c{1FIwY`l$IRjV76>&lC7_kmq^I!{YqE9v^fa;bTX0*'
        b'ai1!O|93dWOPKZq+JjNsqO!%Hp0kByXzF|ciBG>q<=3sbw_#mnB_eH0>8>^<m?cVQJ2m$<v|5W-R?v}BV9^mP)Ks3;77law<8HfX'
        b'fqf2$D!QH9r4ra5xZO(Ku9Mhj-;S-KvjsGPH4Er$kv)9~*+7E&H=+Wzfh$x7q#sC!&Qglo{Pj!?{OqY@ipBE+vB*KP?Xufnl(-~<'
        b'eJA+X>}mFp+b~O<lE6Fxa(A8hE-*dpLASf6pA<O0=jF~$+$KY84ayF;*1in2zZ(NU-6g>Ls`RAmiQPX8xq<=p3jPkHEBoc1J3|f9'
        b'{Y|yYPi{(efqKdoy7FaYSoNR7Pc7HhX?49rK(qENubf^7<&?JhoFrY77M-5PNU`+dwEax6XkG}vM~C>*HS`l-z8-2809(EoB7*~L'
        b'sgna+s4s@<s6-w7R0tCFg^xuAbp2;TFbYn|kJ~ITGIYo2^v>8kiT&yjoqaICN9y}QmS#!X_9wkkBMZO^_s+DF(2%S6asC{i{llTM'
        b'F_#2u^$k_iT0n+|1hc=-4+&mh6YM^NHVy6P5uo)wpw#}}5PxI?Jb2{{-saGMHRw4rM8_c)Tz7g%lXA>UicN9hnv^aP=3Kdh&NpnL'
        b'HyIk3PD$cQIxegc9b0J-bOm8+Qp~F+`F>?8OLN_&3X_03J;;XcC-Hs7QtIL$O)rD8)92jmZG$dN&eEMTYE53vGe@FCuHt9vqvZkH'
        b'@AV-dKAXrpJE-Ut>Z^wg!UKvYga&muI6>J&RU9eaL|D~fU1IE5FDWhoco0^*(iyj7@us*<iyP*51}|G_P={3r8s$)<K@L{qmZgZn'
        b'=Gl{8_3ywee6D=x8EJOVk=JxO7R^%wfwmL|g=9E?&l;wGXHdaN>9{C6gE++RN1!!43v^_*${Dsa($^Sd4i}cVvFtF#Yj@c=Y`wGn'
        b'Mq~>M#GnwQOKTr<F0KeeRP9{6Gwy%W<P<<T@dyg8x+6Sh7ay{;bM+1=37z4AA!t)@XL$Bvu^*JBLUXq^Tk+Y%(mHYN;<{|#P43lT'
        b'^d6s%ixmGWu-;Hc)RneSA@$^7%W0wFmcYJw(6eF)bZ?s*HP;a;^<)o`A%R&kX9V(!GS0Jj2oRw$Svcg$L@3xu;l7)==NCiv>_PA='
        b'J0hj_MMFQGuL>%dV}D|>Hk8#oRQ-m~Rw3L~M|u_vElLK=%+Jc{R}4Od)3D@#wGux>;;tlI*``dW3pT)NgO0BplxPy2%T~KWHR-7?'
        b'6p~&O)oJSdPel?~@aKZfHz(&wjCZ(-6(sIlo0yomj0`nv?$xd3-+RK`(@Tds-0uQ`;B&1QM8?sKp^igoKt(pnS(XfTcoxB9v}KWn'
        b'Ak?fOUHl+j6h#+BQcxBQt)dlF2ylch%Auq~%>-Q(Lj@0&T*K+22Pw%AT{MSJX(|X(6`#gYVn{RW4<n4EH!o-?k)ZG)Q$b{&XoxO&'
        b'hQi=~Y#sss!{~x=YHH9_kdTK#Hi8B_sNh*sft}J0=1mSJZZ#D=4o05oI7csyHmwe(7w<=A=glBU3-f29|LQ5~<3aZLlnKYcHnZ`8'
        b'V@(D=wC`S&7QT+s`Z~F1U@(@1t_LHsSd}WTW3X&zg@{$LdA)-+yU<jix{@zvL6D<Sq+4{vgEe5L#ecThN=?TFYxBwA+{PO3;@7=y'
        b'F7I!*j?~i5>$&yHIz8G0bqhx-<=_;R{Rdp-TD`4F=`~<3C@Xq5rWH}~MCjn9Mm?hH7ojXA#F|vLQ%XcwYN%7MNWxet#_9#EJB0r)'
        b'V3)k>6`hl{@<nn(&1*4M^e(&PoL3-#s;J*<LftlD*C|AB+3D)Q8*&4txHOlPqE_-kYcG+JRcjhPCxhJ;<z2OW!86k*CJn#<cGpeW'
        b'?xTZja0{6IPTB5;L3UXS6r$Z+LZsZ|9;DqcD=>O-t=)@QW(SB$<(0&eF=)0&Bg&dXY1JH3icVXpY*hx&?m_<GRV^8X96NNVidIFj'
        b'iw`JF7#;EPF6&G-D1s^-G;1(w>mXea)e#}BI_CKennU)dQ6sd9We;Hq5(OO;Os-HW!#mspaMHZqO4R2^<ZQeSikNR=+e<=N)iPKZ'
        b'?Ar&~BHikeIrMDFcI#}fDh9Nd`-l)Gbjum7XUm{{D=&w<$Sj!Y5)#hEnkTAux*|UAaMy0%B*^JJ7t}1Q(A&#zLAkPiuW-Lp@7fS%'
        b'UK{07=d`&uRPPm4zfxYY*nB3ERp+?e8*DF&Y>8k}BtC(7kRDn!u;mCpP#K|`Xx6=<g7HR3$<TvAZdXk+ipJ>*7qZQqtxmQD{Dwg2'
        b'*C&K*#8<mR2W<)EukwmBT&Q%)!Tqw)O8b&Q1bIS8OEQD3vuSm%>nNwBgzH&39X=~ihJIoe>d;HUUU#PbkpSx!0`tA<9Jfb=m^D|h'
        b'I|W8e;SJ6J_M($CI6o_fg3;5Ma76Gi#FhG@2!1+ATd6^hdJz48BZ5}NRh4Wxsr0%restNOF&^s*g+}aEF$kv4`L0K9Z$n%wnvi(i'
        b'0)*>ZkO;QV8s-)LnRV}?-8Q$TrWv<aqf+*vTbk@DFRhZbK6lGAbSpqm{h;(+SOQ^cJN9xei_o7C3L>ta8;VG-l)ES)%&Y1qSzu0y'
        b'^ElwJ?{(1Y?hVF2gP!xMUH}!LSc{=?Pg0@{>-}cDyM7lISg$|2Mg8LzBRp{IS{h@%CQUO~h6c<vGil)gGb5)41{nNwLV-v(c#E+v'
        b'A#rdtD>xs2Mz4YS;&aB0wb26elj4>~l=-ycZS;bwL4A%;zsaGy0WX?9{_@sS#H-SC#4`jryH@k>C~a-_vES6KI4Iqu*_7SBy1cy#'
        b'WZ;YcbT(FrDol!N6OD{`fV(V#wP~Eg9t{FZ_?+ZbvUUZ!P8Tg}4Rg;C_DhIezAg>}y7M{)I=3<+AQBf};m9DXIy{YmmA%&FR266K'
        b'RPD@aNa+ktH!;&|Cvku6+{Bm_lg102DL$N`g<zeKk{zo2tO`{{meT}vBv2<lY`O-rPYh=Dr1A80Y+QTOE&BfZt~}3xGPBgHen6|e'
        b'gShN2T^g-5splZ0OoS=k7bt2381Xsv+gq&%Z_zl8j)3_FfP`~+;lshnQhUv<AK#tn3U7h$X+A}OKVx1=*eeIn7Xz9(XrE4k9cZIU'
        b'2fU%{6dC9!S!?Ajgz5y3il|RQsBE`>_B})x$|xBn2ta&NNWC&-o)o<yum2&ie|&!HK*tw2OGcWrh4x<$v>oTzPX%7dn=UfK{fZXd'
        b'T-7hDeqH<VbGN`_sIH#xdJJ=sv%9+HSD)1)mD;4V+2*_5^Lri>u#XYm$L^nRKL6B!XTvQ(-9biz;&w>|ZBp<dO1)Cz3lbDD%yAnl'
        b't9HrUURg_<j9PokR)_8k#Lj{<A=|zB7P@0ANq|1s&?xWU)AhtHulqeRgq(9RIHc*-kc0yQXO!!s@2fUn4zXP>H<wLyM%tI(;<ps|'
        b'Z!$WDN&MUFsNG9%p(_-EHBpU%M0rD^CcP01=}LRx9zL*n^|w5`2Y{U2zkoGM(fW&9N_s(ZRkNUrmfIDGvq@AfjvS3?|L0!=tqX6F'
        b'!KrnkKwJC0UKnzxmaN=XDYLZ;ZFaq49oFIm{@r<WB&N=HC*Wfw-EvBjG+^jY-%X?~?X=qCZ;?^1Y=K>M>wMg;21y%<B{jit#0Xqc'
        b'tYw8#Ti0HlU88)Z#`Y4hTFB;L%<}2_cHuy7ZmBi0_rPH`(!bf6dMeBkeybTTc6=#9mngvuK$bG-Crik!BN0+>JeK(vWk!>KoU0X+'
        b'AtzsZaCr(Ds(5=cBb_A#41w94a`4l^gCq%?s>U(Gow;!7BbLO@SkdKwXZe`Xz}M$)^ygkFwa)H6;4sbhZ(fz~wmk3Kfy=`D=g}(^'
        b'5O>t7$&Ia^L!J{h6Q9ZJ2f0t>Pf6{A1EkoRjV<qZ2LEvHlI1Ci8G_uFQZTL5!(8sEJ28jrZ*#kQ1`NT1&c%j==Tcw$h5qXSGK^V_'
        b'>Ao6BBi`LghOx7InPu3!J9aTC%rc=d7*p<TudcDR1tSZs!-9P#FC5@viawQJ6c}%C_J0g8V6l(iC8NckBZWmuJeLQ$(&QN#Oc<6B'
        b'CTA}SK*j-}&9DK)teQfub0r;#DZKY+2~I}G(=p#N!DjE6cNs4Jh{NI;WxN3$@$)Vt#2;|9gkYiw<l-lJ&}Q5k!uMAm7%ch;xJ=|Y'
        b'Grd<qH4dcV_ri30`dQT$-JSkjCxUdx`?b!3iqN!B_7InPO3@56z8{^p$E)^VCfeMby&h#X`1FS$fpaVf*Gv86e1?8DBqcLNsjnG`'
        b'Ny!&7)@K!JQs)|I^PEcVJkzE<q_h{J>Q164?FDBIm}6+EUt+TUHt&@IlXWYfmgZGL`aGX*BSj|bc9V5SK2fzNU&x9ulY92+NII{4'
        b'z$?Q1zn0|_MGLYuhZ@josUfOZs;r-UL4(edd$tacRbW5v<mnZX1R1WJKTWTq_WO=dKRLr$-tmR-+>B-s6fu6uVfkAXFW=>#oD#y5'
        b'<{2PAj(!en-8A6&)qp(*O+Wq|H1zjLScx#jg$VtV18Jp-YYG!CIIt@3i2<l9B4e*KD?v|_VcI6G*C1eU{6LNFG4zZ`EA8<3V$PD$'
        b'KRw48oPg&`2E2z(q5|ZMoT{d?KRqWHT%@QGlIllAq=LmoAt|Z(DOZs1&mM}u(j>2JvM)rqCC<{ED)(6%Qp`zZ-(z8!pi#7GTBu@6'
        b'kue6*qvH4o+^58tP~zP~y2JtU18XR;+C2A4y?kxcNR#{&;r$#hhW2BV5gIX8HNl1wWjC;h%=JZfTanCaB0^Rbi7qm@@ED;B>hB2i'
        b'zk9$N)~i!Y_YGD1k#3;@$DyeMy)bPIm_BkKO*l6te&xJ$p)m-1O6=(5It)TFETo1|9HhovFbRx+l4jMUZU&lTDQK`fAp>YxcjL?k'
        b'tWZTd_>=N!Zz>K=>VyO263h4fYl!?e8^kbH2bPn<WdvE(#($J#pSX#}^)`pjsF*(BOa+*E$)xA|esZq=0WzO3KY!22-<L-9^|Lgl'
        b'IE5AVa9$d-kM#evW>J5?$<n{2y8Gj^aq3n-zfQ&8Oh^mb-QQ0}CVUn`cl@1o3*MpmI~RYpFV)lUlvLHaBC&)hp)=cYkDK@7J#_YK'
        b'H*1US|LL!4q>FQ@&-(+P?$w%TO>Uh@9Js^Sa;?AYd$uU8?9)V}jg~bNBv}+HrQW|u(?KBJ7o#c9O)~hD@l|myK9S2zfbu0XtZqSd'
        b'Kdi38_?SnI#l+A3ZTurS?8STDOB~(7nb|4DY0Ud3W`7;^ukeTPIU`{b)t4cdU@rEr3s>r3Ni8L^RiIhBK9_&~Mc52XB~i)nx!YuC'
        b'!m?Ed#g4(i1Jw)+>S^)0O1bpQnSrWMz}L$iSyhcnd}18o`{42RyQH^V9|@|f!`Y8!x|ZK+cgkHf_BUsfvmvxjQcE{RYM44rVp{!3'
        b'_%y$t!L>R)iIWkXFjIpHl)G#C_rJ`7K<ATDAck0-r<zt)?j?e;s=rjeL}X(ztDpiHXPGS%x$Zk^ks{#xTh`q4yxhP39cAGLh3BRI'
        b'b7Fsi!t(shX51S8*pDlc)jc&&x-oi&)y)-NRBUwNv^(McsW`w<azShD(8lJR6E_FhcOa(epXnz>hB*1^@VP9WZ6LB?70k>Ok`YU5'
        b'qYbp2RcW%rv*+6uw}UVolw|Iyap#xku2Jd>`%R05RhMFOz(hyhdmNI?Vx~5QoLy~hCndSNYVw6;CqdtD;cs18BiyGD)G<~(*hK`F'
        b'ZLc<Kb904PUY6$ze|nC)48g^rwP8O;QF8q2mjA{PYQ-fkLQ-=4uK^_P|Aj<SY^crpFC=eqw*N+AFu84O3)Y%q$#Wt^{sP2{1IwMl'
        b'5)Zb;sjLvf197v+e!CCgRyxe20;+Ny?PRcRUkw|Fl{9l(>f~Dj&g=$kwE{O;!%TR%mk1{n?w3)yy){muCAL4ePQLzru_F-@uOYmx'
        b'BeHN}R`J#RYd@iM3ZDz@*WSliAzZBxths8%r6xl9T;t7L2iQ77CAiRW*iR*JlR;|5lTAc2kH-bGl}9A#Z?6;l7iorMYiOJ)EbhPB'
        b'yWH1uzZk+MvAl89WQsGHXHi{!H2rW@$tmGwBB!$JzCC6Cysx(S*k{fift}EK(gPP7qz5YPYBcgOP4>U^@n5l3Z9WCw7J_NeYjfQ{'
        b'Z`!}U*`~^k&1sg{_oFh2Yv)O)_l3P~(ta4h4qT%Cb(6j-U_0V8uG+{%sYU}jB{4}Osf+IHXp{ubYSsY4c@igWc5;ohaUx(Zd20ID'
        b'j`ifSM@P0*%+h^$laL4-CF$t14^R{!wX7jmhQXAd>2>1-bc3gj5Mb21H$gl?C*UC&ifOLh*JX6aLZ!Bpdgo^A+c3H8Pod(A{_>PG'
        b'^H4#3y5yV`)_D6G1Wf%)Z0lP$ky>7bvfc|H)ThF81jxJjGktsbX5c>0nwumJPAcmbZgbAj9k@vZ#{!Wfv>Ye^+kKl%<ffJI$Mw;@'
        b'04)|QmYn`DsjM%s`AnYL<znnB`c4VFnjHJ@L1BVJ;mS@vebIGM>y%eSIjM?7r>-J>-$3v=K{Jlr+rQ76Gvex)sJ4}Un-*eU)CV<K'
        b'N!q?oZ+d=vla+=i)c%ui#(OE!Zbi+AN4aVHIj`uZp+jixP%2gm?GN?2JOWm;!d4;M7rD^?VHh~cdq2m!n&iqRoA**$*J3&R&s<__'
        b'swaean3RxVQgqgNRhS4v-)r$NZoC~ifpW{2Oc%q9-%OtuT5+?=8c*jZE<s}R%RbATK5|)yIybxERs2y=u6Tl+GlVw>Z>yxk2-Ufn'
        b'NXMVM0DcUSr3$G7GqZC;*J=5gcZn4kbKzd%62*?YXk~~%BjMi{4nD7a>PAZqctJKyc&SZ8BFFAg)L+*HWmla%S30qOPgpQUEW>s`'
        b'*az4_<fOHmu*z$I`$%20OP!0}`lS<Dn6HmN+iXyxBRH?&zIZI}N*^u4%!Xh_Brso)=pt_-)7;;{(cy7~Fpgd|i;BESWNA$_w)%NV'
        b'TU>%SE?%7<oR2SkerDdMH@rl0Tf{oF?;+>%@sou!y<W_I1JQ<dJgUO;@xDTd*DbMkBN&Yf6=QfCk?mE<TUvyLE99Low8d#4SC}r>'
        b'zkj1cCA%8FzKzfV#9tzxR{vzE?_R*pBLed15!~!>hog-z{|zL*ZmfQXJXUJI*!Pp{YHi^P4W^#t?BDfiPk@(<@%MKH-Vc1;*NoHI'
        b'$@Vihz<UNL_{OJyR+sv;uK}-$R{x%(KIv<t(+<Z-$r&9WXKsP|51ie1!%OF~nhd^aoBe3teY~Baf%lPVG|avZ1fEBTC#Lt$FZ6-s'
        b'#8@$^y^lH0G1fHQM|}-M{XMRc(4FbaCJwyTKx8iu=%QtW<1WV}Jz#G|ImVjjrSr_6Pu-vAiZ+Zrj@wup^ssP(<KNHZ{kjiLK+%3('
        b'L!bW7HxxT(ba=9XMaa&79dU_z=7yEdS-OoZF7?vSz=B&GZ7s<4s&YFki%aikPi^?(cL0j5vj6c0zkEQ2Agd~urk_bPQ*ZVa<DGl0'
        b'aSv|7DQ_RW;laW&j*gf`O6iqx)PX*_;9>QY%v&IDCe&@5<@G*TQee?n@0-=RRuf0QfHuBF`xPAmYWWSC&e_)!)>_j?o>A|aWxgb#'
        b'<3Ph8Yl@BwSFo5#wBH<oHb>Q~6?7b_FrkhF6gum+RhFNUG(?^jG|EqD8q!Wvjk<He9Ug5nQ9^_lXR(&xI=lVXr~}U34T45VgS;`a'
        b'fojw==o-_YceQrsTDBn7o&lquqsT|!^P=;OJ)<RA;hVA?A8;5=+<NYrK8#k~qS<SLc3Pg4P;ybrs&Z;)SK!Wsy3ie|74%NV_zB1B'
        b'pLUPUZa~e&l9yW1nw*P<%{(!FP8v%#3+#`eXP*2%SeXU(W&E>@G2cc0OjHLg&Lt+=lI7-Cu=+1K+8thvfln}#J^r<){|0guOf%W&'
        b'Svsa~cgYPRONW+5lMJ02h@RE+7IxJm=yJ-gI6)7{K)whANQ)2(fEh?93tVew@q4PUcz}-+f`QIL%f~l<6up68Kek~(>VI*`E?+lC'
        b'_4>o`Ih3|9m!3eMi3(P1!=#0uaLH{B-bJ2A@b{^L{2dFmi-30v71@DF#o}01F&Tp14qHP&^obwm608H?nQ$zm5PcYNGIr5B8zW@N'
        b'-)`I!mDhFyomY<#E-efpk)JVVB!+g};bQ1#@TYJx$R)x$m${6X@dqwhvhP$_^8O=Ha~7RB5;ZHi@<<de)?zWw$E-r{!p$4Gk|mgU'
        b'oKyUJYIpw)SMW{q&R~}Xvp;!*Kdp`xCE?<^nCGv4*AlEPi6x_3T17`<)@1IlQKXApahUlt;qI$`SK@+ujjdxh$eb-ll=e|n_uld?'
        b'AGCLLPPQLI8wmEJeq<#GFA5G^TCv>~gvEcf;9QXXH3W6w7}gxr6%3CR`|rZDcTZQv)e1ZNcb^5ssmDI!A9}MeGRXHa7qdO2Q#{O>'
        b'|2^*g=nc2KH1_o)j|kUIpc8dQET+i#5%*%S_#(eAa2~fO@G8!dmD8)3kO8YKiH!azV@YQ6itRN2?9vn&;a*U#b(iWIZ|Gn4TM56{'
        b'^2@e3gTg%1N+q`xmY);1w3N14(p^-#;xo(;X8`Af6lI!gOj&;Kd0B`1wKn(bmoA+-(~SFjIfLNnJZZDgyjW$$vE)^&_ojkBeJ{db'
        b'z)XZ+5i!e3rL)v8*XIhgh4RdN`TA8#OT!IQUU6>josBR5!AkU+_Xe5V=_dWryy_dEg~$*vM_)jE^1N~59MJ(fb1BL(s)xy7at1WQ'
        b'SmwF(?_aerIoDGaQMxDmjLPuuFq!UY_>=bUupn^$3Cvr#1iXCnc#xM$R4m5||IIx{%nSH<EcEi_nsX8~ccG82tX^|4QFtxbvd#}{'
        b'Pf0w{6@-<<&pvR{vew^5rLSKlBNe&t)Og(-JYcExTt_*Z<u?hAn%};Y_bb0ityie;c!^$cV~u}@fiMxhq+<OlttqS5_YFr%l8vk-'
        b'V`EL2i^^i$()3kqp_na9W($|NEEy(wF+*jP-PX1UyZkas!3~|--}0UkaqO%Nh|`{x<r!~e7Nd)-tF=OHiafVSrY%yE1aOp0Z6<P$'
        b')L1PKTl0#&77b%jGnRP9lEzpvpCVo)o`LaS#8@6;C{4^Ec%H#91aMDlP7zX+pP|#L4pAwvJS{=|vMzB^$<)I)zU#+*Ul0uacxRaJ'
        b'St3t)!=%ouiV#0TnCR@F=W(%x@bBSb-xnX_SW25ikkPwN2uP`m(ssB7%tv3KMdaO@M?;RhlDzKFzLbQV@iupLY838Uj_Kyz=r}Js'
        b'^KLWFSQ6AtL0<jQstG{$nABIx)mL+5xNk3ql~6)Lkbq$^+hj^?%YL2m1~&VW42$MJZ%&e76JXC2zOev(+q`~2_r2e%$~#thQQGD{'
        b'eDVO57F~ZQ;z&)@?lHe7>;?=plbGjrDjNvh4}R8?>@9d45xq6F7WZkfoNMqaE)$Rh0D*TPP5|%5cb&i;zsGY{LeBUe%K6seIV$w5'
        b'73GYN<H=c&bA%H)VX2Y0aURA{YBI^4qGSc{10J$m3)Y$-LHC89)xS?<W$8WxIZ}I7*)5l3=6h>_maA?-8lineroCL#t}X2hGfIfP'
        b'37AhzsBIj%SiFkk=h=ZXXQDenPx{?K=KZ&e)WLueSZ6%RVf8O^WSn>fNEd5~Uvy&oA>8;Zwx}RA0r!OqVpl@mmw?4)LEiB_MwV|^'
        b'J%4yRF1~^lEyaB+u^X#Hb{z>R+{wi*7H4o+(du!QddRE^R)|xX5ATw5w6E6Kw58??lP>BZ*7vRLU=0}6=1=c2Zk!jVcv9mz=eMOO'
        b'LEPMXy<MsD7gFqQ|453wx<<dhh9v6pnQW(c35Lb*n}2xUp4hO|glaO&zR!>3^TXkEr}1s{sZ@FDKHTvyY`f~k*z2jYrQ208u@_Qj'
        b'<GxQh^I;IFhZK!-)z5OVFZpErSJ7cm+-Js;3s9MVa179VeNy*CFQZzjAjTQrVC>D*Q#fcu`yPMlr?~h-jwdxhr*603zTL0g>orji'
        b'0hNrWETgV2-<0h%#$bz5wyT&$D&UrQ2unVZIy-1l7;57kgn;#60Sr7$+>Ggp{G_C!#yA68v=Si3X1<w7C}jU1)WNcAJ0;pwnb#eA'
        b'Bn<cc0aKW<_`SH}5T{%1-@LDmKsc#nZLv(TaG~15#XceaYzn%!t_E>qAqHdTSc2uCoHzw|lb@s7u8IXwgRyMJ7F~lT9o3vJr5Bn~'
        b'DDFC5<*=L-M8_+fZZ7cRF-2C79h4%Kyo(6ZX+bIGb#8?=r`fO&h-V8P7q5aA3Dn{%+;-JdIXvHA;D9;i`kM#dVLtpC#Ner#To8km'
        b'U;dXE6o0{Uwe`_y0chFlMe&|eJujqq9{jlstYwxvS<6Gl3*5Q_B%lQxlCq0EKO2-lMUUM7LJCwQqte&9mODL!AISJr3U#$#wv%C3'
        b'R@UTRDZOgR6l<_`*SD*Z)_r~i<U9jghveQ-%9#};Sq|99Nan-(gJNxMxo)!8l{LrrCdarf+g0-z_xjW$xRJqhC$BR^WV{L&XL35R'
        b'A1WYublXz2_K{wuIN5;$elu=Ft|OIWz&p9s%NO}GQyghT(M@%Sr!hDl=5$fLWHkTy2W@4!uB(^LdO-1Qw?B)EEfsH=BEw*^7<X{%'
        b'E~M`3i@m-P)C$e%Zuf4yh8vZf%eSshVl3lGwFyckLH=7ZI+m!etO1O+>QZz62h4|uwfoBzpMBv72fGF)y8Xl6Eh+8k#XdimOrXKM'
        b'&`WA63dB8J4$1;C9}Xf)&H*K{jxRXW7aKhAea3Zut9$c$T7jaxUH48e8EO0#ht$K~S-L+XsOqn}mR>T=w~PZx75^}0g@IalQFj!f'
        b'uOZVw#&n-w_cR1}fljkA%QftWADF)%QTRq;Z*Dw=`)*CyYkD_+iaYwJ?C<p2_Ii0Sa4pvuvrtHq6TPs!G!RFEqjY<FTaWazpbb$('
        b'sqC_GcZ#;UM&`04>wb3~iSJ5~zW2x`QUYChRDy7SG6gbYf1@`bG+hhjn`=hu<hqx7U#N3|D9`0E=1pvx0hbX2UhE~8uvr^`v*On|'
        b'X!t3ywoVBxI2NIqrhC2@)H9K_fKff}z3|s}l4RcFYnxKgSH{{i<t^IM11CJs^tS%Kmr2S#Nd)=hx!BjlBa<!A`sQrk+$k0WL?c?C'
        b'QDathBO5E8b*Jru+4=^yy#WUyW!=HsHLF13I?A!b8*%Y7*x^*%_Y{_T<X1Ofo_eNq`s=J}vEt&9M}w;V#cR*5L-M8+@VhssG!y*i'
        b'q>71pPfl-o26WuBx!28i+^5HQRTaO8NIen{Ds$g)#FwY0`Jz}FQUsIuAx!sZ@6K`KT%?}%y^2b#o-UzF?cJ#otFfHy?V9;HX}dt*'
        b'{SnKFL{$F)TXYlUw_=Mf?wWmM(Wkor)iutZ-HYTdv3F;rcs8<~+*atR@nvkgCXD^?%sbh*;}U15dP|CP#nW>K>8B4k^S5=n+dW{J'
        b'b#B#(VOSqmT(3o>F!xCb?*%qij5~H>x=;|kig8lp3x=`j>S3?pY@}p$F*AL{r2b9!5%g6hDOw#Z)`?-xHI4^#XsQJFy)^~n8yH>j'
        b'2a~#n>*!L}FroXfa0~htv(z!l*&}*ef4C0)Am^|j-n~rNF4wRj$I1rWPMP<^d+ko8`&v!e7bDFmJ_Y(de#J2{nmeuU^?2t#-ey@2'
        b'L_8&Jqm~a&=#D^_f{L<m@z)$PHyz|<EmDyR)hnoPlh>#F_T_c5xFXDV36|C*!0{Lv=}xQhq5U7vkshxlK7LoyuGzoz9PT0KdOycm'
        b'Y4k}a?ueQ4{NwsnDvOn7UbUp5$+0|Bj9&P8E?p-h0Gi8#SSVph^PS)@`}^0CNtvDLg8Xp~)7g5MYXXMIOenw|cFq_CvhIIXF?#@a'
        b'2&c%H<`DmCMQ5}_FvWsQeR93TvIun+#LCTKg|8@5q1?oz_Jop*E?lMPtUM?6KY_}BGl}|k@p{g@K<`M=Rm&pr8yu!~DiWa1&?Mj{'
        b'#5d6rU8V5#PwFaxNso1giTfsXZPyV$>aLd*JpPo}w;Sf778a{ISPZb7EHDejUjcTt*KOk^T#c-zKVB!Y<{8^2F=VRMAQP<!+m(`('
        b'Q-Cb6Ut>At$mY6&s(Ie-feL||IvZ5eI^LWFDo`UQpb_6jEcG;Qd<uirEebbYm^8;9M%4;`ss?r@<L0)>a9FTCTdp&km-=cZq2YDN'
        b'!t=cd4X<AphG=*W{wC&(BfIa{XyF7Jj`K9Uc>O0D{s(AS=qR7$Nm!=>62!&Wx)jvUH~GR_e^&SjD4cHG!S{0=GD#i3L2az#?amF@'
        b'x&qY3UcTC<pH(wLwO=?kPq$Hn+V~CXrei&}?hv%(sF(yZl*|Gf)brGJsQpvbwClV*Y7jp;NoGxRI|a}^;xkX81(XLo1b{^j6X0h&'
        b'*fcB=U=KMSn}h{%8lncs!{TLNATnea%)VG+`oV+OT^5GO(uoa|SK*mT`=t_SNS6LIzKZKtQ3=M8K8buWh9@=We*IZ6PvL2bn3>cW'
        b'&^Q6y6MP-h?q@bH@g+~1zpdE)X}34{^v2CGTikd2i>KTfO2q`$dbQg-*U+f)_bM7wd@tQYYzw<S-SHoKN(zjQInW-o9>A%)(?evX'
        b'IwBEl)_vG8z|tIH2zIV}8a4p14983a6W=fA2iT*I;7MKSG=;iufc#P{nq+|W$P#4q?|TG2|Hb`Jp-86j-aX6(WmLd3-8c7Zf866j'
        b'1EcrdxmTqy4x=$Aqo=D~0@@clZr_9UFZQ%FDZK^R;#clrmYY2UzAzVhj&@#x>ffD8E)_4m_hF%srk8eFsdGJKgvq)z?`+R=U-!`J'
        b'>@Bp6F3hH3wWEXR<7<;t<~GspOFihlfrSCF0QE_`^$B5M_h5y}h^{1g6Mcn-#PdcE{3@Gl^)n+nUr@g@wJuIP?;b|I+0#KWZFIKh'
        b'Vo%w)I&%tEaj*3;FP*Jzl6kG!C4%>>_JM^?(pm;Y>mjh{NP_-g%H$R(7nEz2rMik9hUimll`9N#E0w`g4>QN7a?RlMW`b#)YgU&1'
        b'3mjf>zO7Um*oN9w%Jo{I^)1epA_pL3bw_(FYrDZy)~-UHG5|Bv<d)y{Xcs7}bA{Sf^7SdQT;O3|aZmy7n~T*qO(nl%oVtrqzv*G<'
        b'JjGUF2?}3&c=f(tFe-ss4u0bT-LpL%bY7b(n@*nNarG$A%3kR#WTwi-++HoM%2q<x3bJ)YJvlV2Xoy)KaK8S#UU!-O;cot2k>b)&'
        b'-pU?Eo#!pgV>Umad$OlQ_4rO{VMs({C?N2v^IFS#=*@FF+)tDED@}AkwtW_=DINeDhR)7g(SyE(v1S{ObGn=!lPbHfFw9Z{`gBR^'
        b'VQJx?r(*x&yL=a!Foiu<SoRjm7|T*cxm>63ai*~FR}*SU>TV{i@k`JdfM`d;Jw}zST>$Rw5}l>TMJ)lhGhKGzgf{>AvTa(O@JfK2'
        b'3zTigIqf6bEzr3BeTG_M`Myj0L|oZ;Zi?1KF)Xztccsi^VXT&A`-($!>K>QsVQay|F3U1qdXI@(qFsOpsk)$hu!j^`RYp^R(P~+0'
        b'ztIIPvX<=BogunN=uJ9XkZ!VMTe`Xcqt#+ux+6pv3b-<?1sN`jQ8x?qc<DFjpo3SHQU9K}Guk(Ik{~j4pLFs5KZrVRTzF46+Ld3R'
        b'_@^*!E9TyBb)(RpY0;!eYc79OgyLyr3F}{(O5PwYznkalVyLAiixC(AEt@RMz;?E`cUh^WtOaO9)UlRjjxJ=QM)yD?FrUaUY{3Qb'
        b'5U0D<4fLEWe9)`Xq8ChWBYJ{>9<8qBXY_>L({*=SRoSWA<OGqfYy9bvBjg@SWw_+Uwp?M^Etbk`IW5b5Qfbo)T~u1xe?Y8Tcu_8S'
        b'ivw8)$=(u>>^t4hz1j7nWN+am`?>eK1CkA61j3CZ+mdpXN&)%4vPB4*8HB;SU7q(|x3jP)GUH$nxIxv`rHa#G3N|c%6@9ELN&RRL'
        b'fAD8ZsxmjNMoXjct;cZst#_1a+dFh*;f|@;4dR7&%~>-jZ+BW~YORRCwZxK#sm5;Rt#|TG84JEu#cwRaeUD(e{oMqiBMkFt&x(XS'
        b'a-F9eq<g6qcl-jQ+}(76&T^oej?WJ2!F>iS@9l0fEY~D6FAyQ4Ek9agw!ZbwX6v`{xN!kyZI*1Nl`G40m8Iqq5{$Xkn}VrVp@zm9'
        b'Pt)MWQU|(~Dj6B}g~3E6KZ>t@eg^e&HyJ_GINfm>lnM3cZkP+oc$t<~Dy|0S{l1%4FRls`U!HXX|9$ccjv_Q+6yu}Rj&7Zyi@+cL'
        b'X?zadO|uq(lkVdfJXW!CRA=iB>@yLDhaKn9w+>+=#!=))(b?AHe_hYdO(;s>DOHDb&;M9Bg|c+}&T>zGlM8CLAlvs>jtnz?2K5ey'
        b';>Ox3(7$EZwY&zV%-u9CE}}zOYF=lg@y~Z@jfke@ouQ7`??T^ozv}*XKkjJ2XjQU_nin66iw|I$Ri;pJf*<#}?t(m~euFz6xVznt'
        b'i(ME&%+t;InY=xFHw+I#|7AEPn9zjk9_c0wK`=C?<9`T{MlA%DIgh53>0$wu(hd6BeMscB=oJ$xXfG|IC`?1(>6S;kX*?EI7qbbo'
        b'6WzIysGF3g+eOVI4C$IRG%X+uLQ2)W=%2-*z?;<y-0><ldmI;kKjEcQ)#Wf#jE~+U@Kj3Nm1b3JRnl}2%vI3-=(txjNx-<xBS8Ml'
        b'%m-9xciy6Izyies+7AYuFl10^-Ac$>fDy^FpI5WgB2o+pHbzF%Zi7zPod9;y>)5U~TwIFL?q4LN;lAHvP&Hv|95vaM7Ftvgs~dsw'
        b'&R|rzm~wyG%2ZbfprYt*<tk8S$sjb;cvtGTxUU1F@nf^CGl4U)DowtINhpVP@UHGwS6){aO=Oxx$)qBeZYM=ba}89RCtCl62>1z4'
        b'+i3wTTFO;QK)Cw(CxO*LCAgyvqrU2*3l>uU=~|>tqgU79zDro@+qmxptT<Z8ir<AlIs|_Yqpo)8d|h<tLrhp48KH${fIBrUDgh9y'
        b'`}5bJThTYomSpN;R~lZFr2<X`jpL4k6M2998rc95)1xmQnaEqw72qIsuFLCgIK?)3>fcEPid}DF)q7=%#APhLK_SToGsR5k3e%@z'
        b'-}I$Vpi^0)1Rg|W1sS&^GoDrpK=O>G9IYl4R*b|G7Zh3~R%)Kctbu|UVHAp=0b72aqVYePD7qlo@idwvkU#WQT3F`=kR(DR1W9ph'
        b'131)6GpB_SM37^GquRT2LwO||im5L6eh<%=Zp9rAPWN&bqe{hyOEB_27LYHZ-HZ3N;l4_)M3qgQ?n>ANHtqyLJe2#k5>pN|i~W@m'
        b'N8tG~%%41!{Jt+}0x^FKH?E$bvcD#Xh5S1!#28=W1k}l`R}%Wi>vu&Eg2$o$5eE0Qf-YZZy(WOH$rwi))mCWr_+*=}16KarvuMfB'
        b'`}XU$g5`m^BQE9;q^4^%i~Am($a8h&T4k&EO8s$Di-f+uAAoZv)zWuX;f~iQ4~PgNRTuv?KR4&1xw&^TsAQ3Dbr(hb7jX`Df(-Gx'
        b'1wfns#h=kuiD)xj6Of_wk~o0TOVrfTE*Se=1xW<{5E+7L2U?CQ>tBdCl7bumFlnNfRz(<JoP=l0RlY}Aadehim(i8CsSC(9{+$Ef'
        b'nfT5EX@Cyq#B&=!N|(b^>yo%Ffj&OWk89!;CKzK3$Be(=u)J@+LImFzGoyJTul4I`jx6OCty&$nW6{e<rsJ?h3s#5W;uT!p&9ClD'
        b'=3E9}w+)-=3&NPthfHsANIp#umHFXUEaYJx3@v7+hsX%@Ygi|K1bo>~c?4k-qzIi`K?|~Nr5s9w1vqWjnI7_KIo;p?SGg@K<<@2n'
        b'ii*ME)}8%o+9$q_i`AU2<9`)j55<q7;>LcC6p_Y*B9rA&GWwjT?B4oq%8;UsD?u-1h2hjy>QPKE_h1ON|3dXabmGosd35(%Ul9f>'
        b'H!3j3^3DkHoJs1duhFT=4aR8Xiz+g)wVvE{TIlXU3Egq;DM`q7^Y)3VD6q41*S?0)&Duasd~Kq!vawuR3;KOpPj`OJ;2X?aXHu8o'
        b'PpmmCl)4Ci9x$H>2eq)P@Hy)JuNgYHNQE0$VMQsp!-5rst<xR-icyKt`-BOQl#|zSqY2Z!41Lz#mqWR3TYw`i3D;qH&maui|Hs<9'
        b'$2E1O3&Z=C5R$F#5D189_ue5~B5Jauf>zrkU_{h5i3Kmy&Pzbh-sT`uaaub~LMNidGZ3farS_c=OGR5oNM~AG$1{K}S_MT!Pz0s6'
        b'%%#(ItYf`IA@8$x(9WFieE)p!_xte+d#%0pv(|dnb6+<u2x3If?Yojz4k8*&s_SsjN5302ym!_9?p6L_lNzsr_ze(g+}^8#A4Fy>'
        b'2o^uz3c?DSq}Q;vM=5j&!Jex&hZ3w2(L~8mmn&O3uQu$NQ1CTVa$}UP@J<Crsc*bG5*!UU7fL@110KD{!*n*d3?5=?UDefR$W6bD'
        b'Qy4Q>PEZlqB*E1j5tVE<pwD|Wj13nn_m*m;ajY^?LrlfEJd6l=(GGRP<5!CCPoa0^<W%q~SFoFYIT^qdC^P#fy0<|mvm=Tu0!lo~'
        b'5PY#H(6@)eh5)=bJ<#VS>APW!2O;UZuKmks##7$wcMx-fZh48Y9t$ttr~uS)Yp(+KydQ_Tf~!1lOLJhvDQPHd$h)$txHHas;I0FP'
        b'V1%$5?;`YSt~{7SCpuP+rfsyo6Sl9o3X%#;q9Q^rNTxMP3XOW#&nTd8=bx|W^%M)n`Fb?lSLDn{*<1N^2Z-%;dkN`BSV6HNEuU69'
        b'+P@hhZGBY*uj={sYi#k(f<Mnnx|W*A08>J_9#D%(sfoy5<4=7>H_&^7ZBMfeJ4aj-)VjZ@HM41pGwmwt06fJj$}7)L7%o?O+E$U$'
        b'IWKP}7h?*(sN;S|23Dk9tbR8N>hAn!k|p&wgmnWlXi{$w(*GE<Yp!m9-fMF!J%se`9a1va{<oorqQblMuE`%7`N0@DiJ1O_-(RtA'
        b'PW*=eV+mHOCOQ^lDJg{XnY*dwa_>*>0(7t=R^O$42ZH4dXGfEIy*`9@!w*9NjiNw@c^!8F(L67yDQf5%eY&D!`<-DqxH%o)-Z5ZT'
        b'?b;t{)i8RcXg|AZ1x>7rBRckB9&RR(1|9!4p;%S8Yo{%BC!5aj&RH);tA*r|lcPyDJ1Xz+r^3i0S%Y!kUg3!}gscF|n^%pz2>9yd'
        b'8i)8E+(Bfie~I(>D!x6$7FOJvOQ+^Xk9<11;C1ghXe)R13cc9JFLw4^Ny^(1wW)fRV&%#eJkas*O67q)$$;Bn+bRZ2R7sy)^AqvE'
        b'27bv!n4%J}4P@ET8E$V|wdQHnA`Gqk<31d6@Y2q>4%OYr`r#vqom0Fg?zj6B0&OO@YX~jYX}bcXmim&0B(lJ4Q+qJ(OoZBW_M=xw'
        b'b1aOH^Q$X`q5*3E@CqGtXcwoxDG#<W^mc9G1ofH@uH_27s2tk;&XvH4TlCSlC7ZStD)LvZ_-Sc;%<wOj?QJGtpY1hdE@ow5NJ@7-'
        b'qLM~KZ{S^|H$82p?K{vTkqy5fdq3JW8D667uAVl=wZlcqu*get88+V6y6`RCKO^7)wp3&N3-Dy8s^j7)ZGBa`X)BN9FRzkJB#Ai)'
        b'wj^7uA%Zf*#E#GITVIE7NaD#3@xm3Jn^_9lb77d<a)q{nJhA`Bl?AI`l>(siainAp@IHJ4UxFCkHP&H-Z+0bq1MRBW3~w1s-f=6e'
        b'kvvHf6Io2Ik!awz<1XltXRl<fP;VS4-AP#2hesMlmlNK<-$ns%=S=BZBuKbfzTyO*^U)Whi=2Wrib8hJOrY)#jB-A4g^u4Xtu1LS'
        b'OhxBX@y<sF<3PI9#8~f<ymKa^L&E!gm?x_{WBB3(Zuu2~&nQ(*6NvYtilOiGxY(fw(j!{?zeh8EZS920!E@7TKjevy1<3YFTM_Xi'
        b'w%y?tUU6_BIA?RxA%}C;k8<awd-lvLyrf#)V;4}!#aMKB3`rOk{81B|!WJDKMKKqiDdJ|Km<un)Tn=A_91oY(3^@YJAJ%}7M}Zj8'
        b'V}(~x%*Q<nI#>K~Vc9%X%)^-rSqe03A&&wv&e$tp#JX6@7D;|H2uUCJI6N0|^GxYVR)gwtDz4}sz!dxhZ(k2}se5KP$A+@hDJsI-'
        b'fNB48l%DOaLER7BNsS}Cdr;@gH4;7*dN0kp!;K9Iyevf(Rr1DY#ye8aZIE1B8dj1~CEG_ca-_ew?EzldtOQ=+ei-`EMx1#MOa$x6'
        b'+aRb@s|jhxZTmMv&JPDyNaotCA(KQb6Msh|5ln>m9DBzoF`7v6S$W4qOsCZ}fu)>>@l{C-H8I}AdnSB3WYolT#NT7d=aD>&yLV!}'
        b'jMpyy&_Z})?t!~e93>@XRAI!hT0UAF6@^K~=e$wWy~)OU><YTmLS@d=n3o#O%d*W+t}rim2L}<~hlcE*4XwbJXX8&A@nsr(sS3|?'
        b'6iMvIhPazUq{Onqf{_;7gfF$P8UmNl{_&8bDBAwv5Tgt^BuOd@p|Oxg3#EPuuWKK&JsT=i>I!*Xp;7nn75Cl{PfSw_1b20)eqcyN'
        b'5H=lJ?*#=^1Svj{DuNOpsHoyqhTjg^cMhpYg+{WBJ3quKfrnU@ldDJ*QrD8%Eby;I%CO*c=rq}LBi&)}JftT+GD2UFs*vb{nz?A*'
        b'>aS2Yp?3!fu6hVrG{thzrS?A#ff1YDaH3ejRe^Y1%pHM_DY%b@wie6mzkr_41g{r7VH5uRCML?kD{A68Iu+dEA-iR8bvfFZq)6SU'
        b';3|d?5gZ&MEfQ|SQ2a(2IG~1xAu?NrLUHd5MO-PK%LWDoTa#NqM3W>ji!%%g54nmVth%tb`JMn8@t=e>3sIW`KeX~ZVVwidjdtyz'
        b'a6B2UsGYl7Bj5)erMd@cM=>GzaiL(9K{*()TLf}yrj)R@-!?2C0!#2j31Lmf==k#D#i=jNv*!-ER}Bf0BvO(Ec1&k>oplH-Pmg3O'
        b'!{`M3(1tlf>f9*dxE=woB%=rnmmBoZo9Xs>L++VF^kOLFlT1~~rk5RHH*HT+R8|%!Nl7-Dn_j6Z(a7e&*ub;rB$BGoNIN%#K+S<Z'
        b'i$P{bNx|rXwH-~j1kK`t<F^{}N0Vk-58VPG_(m1l@0Ra5zDztaMkB*W2`L<BL3knvnHmy<N9pA-roMYOQV~d6=~p0ERYT6DsIP_K'
        b'k{9Q$S|RLzEHf@~rSUmozb^Al!fU~V{j=erV<sj91~T7VYmlPi@jnpO98hzY!Icq50<l-etlK=9WSBGrW?ZMmJ~k*CB0BCLgND0<'
        b'b`6Yk`j5u!-v$jchlC=X6`YX$4pc)bw$dmF`*SnnY=&<K7tBdpvC>CaONi7z5Z+&4NsA!mjlm&hO~p##%^{4IN?#v?&!5hWlL-4?'
        b'&U~{&c>kUGbLe<ls$W-CsIPE#4+_>6!P<<#z8NQa!h%Yg`6bcu$Zf;tgS50LyV=<@D5T^@ZJf{Ty{wVWwFx1;C}O1dZ*i@I8jFt0'
        b'A4GwW(p*fL$Q>Po=Bg~|nIQTugwblqX7Bm1njf?7fuT@4ZdiBSN*Y0Jy@f5%u8bi%E`-yn3W&oF{8Qe4e<c9~dz-sC2uMsL*f~rl'
        b'l-PdDqg-Fa%?B;8<?qc$7?9lTbhO?K^gtv`DN5x3-;_b^;J+z@XD|QH%Ak7ip)vqXu&ZbycVdv|u}Gu6&)njw1{X-hXx!XvB6FRD'
        b'kbZ?1G9i`4P#6opLV;=v_sSqotW^haZu1}%QxVfNL?)&L5Bd=n1DQ3Kv}AJSgN9P{*4{iwW={hlKxRJz5+K6<Qg2wOe=QTnJBmpC'
        b'04;(S>VHw>#}MAAG2wTv`8*vDO1RvQmDN^&R`)rD&KPUsJ;ScS`i#LOTK@s-UWw$GdizXn<)D4TU^~F>WIB^N!Z_5*C0};%OZNQ|'
        b'v+XT~F};qLY6<K2c;`zz?_sqPK6?Qdd)dBZ@PWXI;>iV_F&&<}VAUDUUXFwn(J}<17hLvw7c^CR1sCewMO-#Kd;7xH{4mIuf?K^s'
        b'D1vV+a?XU|cKkTpHa(?(l&xhc2WN!g=9SGx6ms%#f{mrN{9%|!SG+*RmX~16x*w!o_yKGl7}nMY8IHqO0Y<Z!bZ}Xa!ykSe2p52W'
        b'-|rIhJ=~+HWD^Pll%*+s+(H;@$9pLJ4SeYUIuXqdXpuc?&}LNH5V1XOA080tY91s_SxP%T2t);S=^s=rfT7@`xbS6l?(?FN&XpfN'
        b'Rt6%)!hu1!4}J&jcP?)xw%jP=_2my{!#4c$vLiLu;moOtlinE(ayjjOeV~o;IG=D248VZdhcDBUdCA|~o5H+V;Ny}#+!MS#f&10v'
        b'0P!);<@nR9Y6A?fRF{3CY~`6|o(%$tA5uonRpjkzb=LFT)WIyMR?q7N@R7lo5sF6e(IiUx^bcSlX2WoBJ(or6eKs1S6s%+NJsxi?'
        b'#}9&TKzn~R^;o<KGol^9>pYBh?7qd%b}ah=E&MZDuZOwz%TYfN(iAMf&uy440Vm0N^%hVSrvF+fT2`RJym#&(ZMNw0xHiKZogZFy'
        b'v@aOWSK10(8yYVQ?Ru4j0y*u#56;g7Vek1&FMPHDGC-KmpS!&>o1`#%q99$1bV^R5`aDzKo`h~p*rbUf%0CkyOGzog2qA_EF(lAv'
        b'Y{NhAXT(Z1KcLOhDrkuH3(+{&Ig18t(hx?V2({FJjn9r0KAasXd>)3`=qjUt4l9+-rA%2VyX8o285pRupdOc)QR{lJU2YTOS_gER'
        b'Rem_Nu#y2d9w4+*rK^%DtVD7M9R^Yf6tuAHS!Llm*40XtzZdoam31o1N|_BmyW9%US}B{D1VY<j9e^A(=Tgd;PAWI7yWHBr))rFw'
        b'Qe{~uQ`pJ2+t;_Y-fV3*)9S)beQPV#?ld}!E|;g|rrsu`uVVH$F1PHtY^!AIXIw5X%}t`m?X{JcBZdqZIO@dj9MYtk3-*%Bq%<p{'
        b'qDX6&bIO2iZfM_^h9@rbfL>my(`X1Hq6rH55J_gSELcogob|G;M7I$Pmw5xGWSz|ua>eTkr6DFN57eq2S(1~vpI?4p*vhq+?`I@?'
        b'TW_KR#!0kz_Ms6824%51uYold<9T2^g5kxc$Vu}Pra-9V5hIB|;s1m!6xZ9jXCQWntW_@JOu@rr&3`~%11JfQ(;iW3JWvvj!}rAb'
        b'ty#k&_lh}JBkT=21LT6JHd28VfXN-=e69_tibqk&rZ9{ZB+KR^wE=Pg1WuvI<S=M<66pzaUmcQEkAw1nq)Dr^U%CWp1M=<n1|ph6'
        b'|DbA68@9v{*v1jmr(Popl_A5e0S%cYVpay2g&aUDrVW|6HE!-QFo-QHq~~=Q72@0VHassf78Y>&59%=;<e>~BnT><?23PO>F*+VG'
        b'>ehN6C!me4mGxzt*<D+sN{-*pm@O^3>FLAEWvuV;uWBoq@?5rDnp6-aFCb|{?||boJ@Db06{G|QxEPfv)}<nFu#TCy#E4y7A~m8$'
        b'$wT8+16`oDJV-%l7&JzyV`K76^`Qn54IT6vd}Qv<K%h9w#>4YC&slrI++PPE2NMa)8W-lS5B#`=1DNtuSSqfzr89dtq5MR+@|lV5'
        b'PX<V-aXfZrHG=P65I@#&CT!S0K+gp&0lxJr1xXrJB#TO98-?Td3kt@hClH){#qRe8jD$f$2nd2v$M8C%#h|eW+^+{5#M;g{=|5x|'
        b'!T_on-l&L2G!|4Ao}q}k`1QKC2DohlVu)48#Og@PT$Lr$8a<X)1wNMd{zI##<K|87PXnt6G)=E%z%jJu-*j3pk)*+<j`+U{4Jn{a'
        b'(cp)DaGR?b0Lx*Y(Oot0ASh@cp<47Ha4*8kwfl<6NV721tbco7GT=CT78H#@AbJ!mtar;O66e-?qhJ$;Mv>}Hl~|cE^pGNvP8<WD'
        b'-zvF}fjjPS3NK1P?n|eQVHk)HX%hSg4Y0vCfHYQ7uGcY!WktP6SdO1IJ-f5eR8do*_o2Dmf_eMQiwBZwf}iFD+G5@KCA3LSk|9tz'
        b'ym=-%0awN+tN9oyn@kBxwd3$>wGsWOLAr>G9yms^?JOv`h9s&cv4g!S^x~Fe(<;>xB3F}TTphE7pC?GC+{Acf-{u5U7pF{-sqf+Z'
        b'>07t>If|on98EN9tBw(z@=~D9l;#^IFliLDU2EeeTx!fuD;L94HE-2B2a;&_rHg2@50`O!{XA~+fP;Tx-)GC>E8olj<<!G3#{6Hm'
        b'^UH($qVDbrzyGH7HidDLfdFr>IpokybC03EIg0Gu>5H_?K_t-eiu|`_wp~@vMEkfIGi0@?JK20@>zjmh6PC6*DH?iR%QIVjL`Mb2'
        b'ja_PVfD#|U?w1|XgU$|eGyVPwAO2~;Y2i<gHOXoZ>|{6ZEZfWYoR5`rGww&HMX_vbX-qoz)ujNBm5ko=aTbs=e$egn)yR<HW+4+}'
        b'E~VG)1ZNPwfs%$xmw0}WgG=X&=cb=iza;T+vye8^Q_UYJJ)A{2d{sXWgdVbVgNOg*7wsw^_ZTv*U~JNruJN&1f8yGdCW(8(rN{>3'
        b'eF$*}zo>ccn8dwV9AhrS{$H0?7D>4im(q&T<G9Z*3ET|uM5|TgB7I5%(V@Yz9JB(>@oU~zu)BBGvK1czE@or;H>zCvijQ^@9R?I8'
        b'@t`nK06&-(BeXN~vJU!2p1gn11HuH53i2dt9+D{eBuS|x1Xp<x{0$os!tm!wlH9~-xo<8tk`ZBn)I>|jec+<F$2cNxkoW*8#r^L~'
        b'q-7qr?~(_#ah^&>VK|rsC8&yMEUJi*YH;q&OFr=}xrDOv=qhOqD{!*_6>JK{&Zz?bTKaC-;e5>Dw7e>jz7yu1kMZzGSnI>6AH0TC'
        b'mt(viOE-?}l18Q*r4bW@n+1A`)dR+_!We*_LY~T_|HBwK#4&ilAL~~ZAyZjUuIEu?3>n5BFszM2%QaX^w2HwnY0gJey<0v&wr4&g'
        b'a01{9GC&n>*$9TQUVJSa{)gv*W&9xLs!Ozt#RVM}G3QSYU_9m*Vbp4r!r|9Yc`fTex28P$ulg~f9Fb<sLPm2$IRXUH)HWB2su1jK'
        b'`}|9`aXb5QyXvCoRw2!3N>kcrUxJR-{=0Hy^*7zZCHwvUbzc&Ww0W!RNZEY5<`U-L>(gc)n7pbb@nWDP6EIP5ngWi}PP`B7wBS;8'
        b'f`1LWYd7KT#_DeN*Dt)}N%#1x8TB25`}=-R+H!THKu_p#X1l-bN1G;3&gtQ@=_$>}^v%r`k)vZA+=6`#K5oIX1bfV-T}KG%Iqbtr'
        b'M8{=p!N|&agtuRuYx#lbNW<*%ORM5iN|1?bzts<YDfp-C$QO>btmYLvk4fxzE(Wxj4b*-6t&0aG+Dd8T7wSB$Ve|cYUl_i>*eDS+'
        b'wpDAgR%FKg#PC(WpqZyO5<r#?@m@@zKp`4isZ!b}0Ig=&s#*I#E_$39!lL&Lf9kLQ;-W*dT)jvbmS8oB)(bb#?%kt^-rY9zD+I92'
        b'y@d1xHuCs=Xl&*W==gEN)r$Z=NWKp>d=#g>m~gVLah0}VLe1BxGV=XZt5?Mdi)6x*$U!S0l>$z){gsRE&Wl3aB(#4sf0BS4Go#){'
        b'ZTV6!Fg9?HI1`Y<mJ8P(4BVDKJaCtU;Ro*0mY2F8ynf*aFo9ad6qsQsk_rZx4Nc7nzz|^e^DICI3iRj0$A}wjsLX5dT)SFnbAYtV'
        b'0^1pQh!@F^6&EG(O<{OI{`?$h(L%7tkY6Xd^yBUy_js-7(!0bYGR(^RJrTp~&5J;Lu79V!kBZdXYyCXW)bs#yPS#zV9E`>qSA!0*'
        b'@3_cwGYsyFJz5)IJZo8b>f4003hNJ|6}iibQl}D9H%1e@b1Ii{G0T$X5S&wZXA<|)MV?pI6s5)RJP9xBH(c!L`Uu=8kQ3dSs&<{8'
        b'?O}s$FN~DO6yzl}q~Cvfwm0<s|Aok4*_)Lh&N|0H00~;4HJr@GMxKxcw34>8{&m+R+)pmH^Yaiz$gqZu6TEF>_3{0UFQ?=weChMl'
        b'le;|5Z0p=`lcZ$tJ@*1&m3itTM1Y&&lVeR1pK~d?0|rvuQjY@Lm7uI!d$FC%sO@Cy7F}$2W_XsouT8jbO$j5yj6)>Zksj^=mde^X'
        b'^^vU$7ca}*I+d`_2nV%!jte-ZI2Dj+P0gW_&s5U1a6{icZwiu^p2%C-DfhiTdWvWYO{Zm06gzUh;Zv1$YS?oD@6l$qYZnJ)+JG#1'
        b'<TI81On;z6RbSBWzTJ<`>4^<vbetpaFM@`t@97V|gP5!2l0-Tuj2WW(vx?Q{yL?>6*1r*uV^CjQwKD~*Ga-!D(Ov07O9J*VHdV;y'
        b'%n-wj3QWJ(PFxg9vaIQ01AZ}!%vvG67hdK8D)27Cm-(cxLBr8{yr0Gx?(_qcG!<#4N@L`pturJx(evgtvy$jlj$;HEN~`PLANGmo'
        b'31GZAwxIGEC>J4jRFKP9Tpr7P-ya}MCCYp1?U+EAxNH4_CByJVzx~(!JedK)0SqjlB7PCOa<hs1Ge{Dkv3PwJ#imiIs>#5+<zj@R'
        b'Oe76-m}mZ^CPhiEguC1yh?&U&!t4nFM>1;lFloQgj~3SODqgwX$ITZa9#xP5H@EB+q)fo03LYLsftX5$tpt7JLNhc-+2|t~8*9Zt'
        b'OeFQfKjA;98&II2aUcVT7=QrRH$Nx>%<dA+8Au{hMmev6-wa70Xf_q`X1U1hWk?_(U#wj8#UL38;gyTNm`~I-(8~?}e&B})zn6*X'
        b'W<zCPMBS8$>Sn|4{)g(O>;cQ4xb`?NVQOL;lBC?P`vq>1hg&Qz_p<u9TnD#AD4K70xzAH%6*N{~(L6`dEcXv+<k+BiCKrhoHhKHe'
        b'A}C3KpIh>C5^0GNIp^*Nefd(qP(*_L<q<Io`uk(XCF<`8LL-5#asB-xJ|h_q@F}JMpZWiS&-{PK=eR<DfX{pppZRP=cOzu}->C1r'
        b'{vXx1rtja>cTWF*SKrPB5e<Hzm}@cj*U#za6>BqSKF=0By*_a2DfitA=!`a<dt!gYhFn*q;4=FiL=va#cUWZNG7>c>^!MPOl7znP'
        b'`F^Z<Z=(;9=!$zl@*l0|TBi5cKhmGHEO<KY)FJl>f`?A*2=zry>=>~@=QA>&Rd5`Doyx@l*l4KeFGVVDYCpZ*K}_Qq$dkLj?Gtr='
        b'#)kO*T_rL{Y62(kcND48q8$D-6sq2Z!s^nmF^4}1k{vTp5{!USAKK1pm-p9=^`+$tlInJDCav(iKfK*T#|uj;niN9k*pR|?V5h#n'
        b'Dm}V;JM+<Q0_;h{SYLa3OcvRClA8BDxI!<4S_hSWBh!r{h3cMqcj__1JBWMgf3Z~{tO;b&U%_+mZX!~T5LO?KYMoC+;{6*4WJj+i'
        b'xUc)NzMn^MwS7E+e^c(^a%vK!&y)5q`?&r-!GCf-FI>PKTGM9LYGM^QQ{_dtqllO%05)!4BcvaZhKqd;e-W>F0`;$mMC;CDWDdV&'
        b'WenjxOqQg_JX~=f;EwloAA<iS@iCo=9sEsjifB5hoBGC~h9&oSv^;$gNho@VGSP>c>OFiP<akL;%nZ4D;CIL5_2>FVp1cPlk0g?-'
        b'Wn{K~<$8%jD|Hm(Th|-yEq$Kfg|pD9a`Pl3vl(=Bj28`#p}8;Ucdgo4f1}T^zb}dYB<Lun-0RVh+u!NSlC0dA<bLIX_?h9|z966K'
        b'P|XbRDTdvBjupuxcPaZ`D71LvBks5QB8B$#1xS;jwl9#KVOV`3s6xlSjI@LxM<6Nnmt@O8U;W;`c7Lq<NmPm9mwgXUdTIEEF4&F*'
        b'd34lE!vM{_)@N99p`B-XRE0r8AK;bR*a_S(`UEZ`jfgCbl)gG9uFpZyM4OA+@^^<AO?171xGKW=)j+F8wi+2vz<1T6@dSKVEtYr*'
        b'MYXFLNP+Pb32CG9vmhf9)fPXnG>ab~g9%I@(KLvB1Z?jE(?C3B6r^f^dlV!O3Pt8CT|5ICDF~8ujWW;__CwOa2Hp!dvsAmt`Tl&S'
        b'epw$#kXBKcqNMf$Bzw5W;W@y~GtEFU#c!kPbNcl8O1}tjnFNKlc%~p`=jJFnv8*iCabnb_t8ysSPyqb?+BX??59_n5Q!)vub&Mzf'
        b'?ApViyC0wnVt$8d%;BGgX1JV~;7`enLF?nVWJJt*-jzkHiV>XgS$vw{a3%=O$-FZ$*!DENSDU4fP5~dxUy9}yf>^5YCxZWJG#?We'
        b'wy){q{Wuu-BUA1flzp2e!g-v}&Zv(2`EdZeS-WaZi?i?NU#|Y=w)07J6XA|Qgh$8I693Ab4j_~6-eZKISw?@dtC;A(!|1LR!C!{z'
        b'sfUM`p%Ux;F)-i)enrD<MWF44lDK;<%YcR$cy^D8;x3N+=LMSdqa|rm_#V8ROIqFT;HH8)|9Owlu3xR;xoO^A7@xYBjuP6(=(rtG'
        b'`d=a+xpJq1Z~q2-&&r*I_u5zhUj_XwNmm%IUf}Un4l)+4H5dd_FTR{h;EyLbilybnQ4Vghz$LEc=LuSj>F6D^|F+kMe+m{AFPZ9)'
        b'Ok>j-v`qNS1&<_p-^G2w%%aJvsBBU)2f4)9gz|ozkIJEciENg|IbfF1aq#HiW}<jaRG<1KEZD|05!$B+2a%(0h&fSANS9y@;MQ;n'
        b'&=A3y1eH6SQ&20M(*z>N;hdUT{IZ+s3vkn1M_7+DuOwhF{IVC^a+@Z^VrYQ?iht=b!@&#Szy~yQNb@w6Id9~*2E!}=y%>YZHTX2c'
        b'jSDQBXfuklk__S1pi{04CA}&#nPJdP^N6uuGXRSQif5D@qFSE2Q2(<F4c||Kwxco1B^utA@I+2#Q6jgpSA{2nT*7dj$&WtNZZU9='
        b'UI-M;7<rd!dHO<q;RWq?lj=PeA|2%YCt00qH8C&dM?9Czx`&nxzC4DS;q5}p{!U+j*0H1*zPuD>utaZvSgic%1{2ZocVy;rKf54G'
        b'>HjynJ|tZd=JdV60LJsn*rQCrQd}gfE$)@Q$P91W0z_9LQ`lPo4hAIN@NI}&eW6^70g(ZLw{O-0iETq9mNw_-nsj4_eGKh}HKK{b'
        b'nRu$vF8Bq+V=s=WBnC2C2(&TKew9RM(_FaL_5x|vkkQ7TQ(I7G^fdn`ENM<AB_=WX2x*=|O3d&~nv?3?7qmMF=}*S6^7=f(H@%gh'
        b'PZr_j^-C*(2lK~x)uaZmB&eMY6^v}T=bz6Gt})EJ&?didO=IZM%x>9m0Yv~W&R!^QB9bf(nPe)^`{FTeoAO`weDN0|d%j8zD?1aV'
        b'o*M%GsRjR3uc7qK6bRF&N!L*vOc0ZSYUbH8BW?;(Xny!8Uccx<bC7NKV<T5WT+)Rud5~X3PYu*BEx8u5Qvblv^nT1#G>^IpJm@=!'
        b'x6^P)g71u`_hX2T<S{f?4t<${XVr7qg)CJ$k(*__5tGdGFmyBNY2bOY>D2IF*uZ{#NY<$tB4&^RmqSaoKBu=g_6GcGkK_wl6t8G^'
        b'F70tHzvf(a!<pCcD-gI#J=_yFxV&rJvL0^vGqmd@>p6_Me#N-nR}NRR?Y|4Ro@D%;tfwhl)}(ZGGXD431}*8n(p&$x-XORc@_E7a'
        b'Gg^!nu5r4L@f*6uEz>SE%Fcbz+b+%;lIG}<a|Bco*q?huc3=wO{eHAOH+L|qvHn<8$!m1y%Rz2tfRmTJNP7ZU`F`A0$(EJf+!_^I'
        b'*U<~g!819z3^ahKM)=jqTi2zzD|+kx)GMr~K;gK`mHg!7!0(U_DMM!jCl`QxNRu>?BW{ZOus0BsEbYb6vI!u$--U(!v#sxi(b5JV'
        b'THl&#i~_uNyo=W9?|&NQHNeZ4y#d4>X_HI&4Bl@7Wy<~RJeWv4kx<GjR1ymrJsTZB_saR&RAo6HTUNFfe1~##Z2fRAa9D$!;CA&2'
        b'yuI^0+NZPUd}O~y#|NY38eF?i>CbHS_;H6H)32&x<|x6awAY@utwP}hhcn|qJYhXJ3I<IU!PWH&MNf1zjMks(Ei;0X&Ojr;18$%Q'
        b'aDRn#yZZcHhXx<{jnY4-RbRdn?UZ@-d|4UAR4VoJm@?4_H~?Pdo1=z}y}UC=(AXUs3`Clv_z7w4C<uTTd(&b{c{Pv63Wr_Dd^X2|'
        b'z+Fb_BmN?C8Wyl+6bk)aV>L`!IlJXN*!b7SeI}#mhoP8V<%76i<&SZ{aX;+Gu-~}X^&sq5DTe(jAB6oXAB6poua-3)`GZgXKlovf'
        b'_5OE1Ebjcj`C)T=|J4t(XZA*1F;bExXqTlH5qf>$4NiA%OK%(ATmM||Jlr%KLPL8Kms$XC5oyJ6@|KET&=aJ2rYQif`cik=d2vQ_'
        b'rfq)6M9N{5T3+a_iZ&uaCK0O428=~>iF_La<=s;wg$<~%MqY)_1O?Ml*vllyHRfcEL|hwYUdkxtpibN|s4$w4OboG{oW!3{Nz5(z'
        b'y&Cfr4Q_xoV1yiGJch~9%w!ZQ4A1~FqmqLp?P=fAcILdwoOFz^{(fv^&bTZDxi~WYUQMF(%Wnld)^XT{R;Qa|!8u5hh`U79f-=Do'
        b'!0OX`ZQ}%(&@hNM5e*|mNBDk;L1K8Mm#aM=)L;l&%p`3pK=Ypcw&jEK>?Nv;gxr!<g!G?bFhg@_!r`2`P*Tq6pCP>e08PN{=>h+P'
        b'kJ;<HfV0U|8Lw{@oj$~C(F;I&sV$T{&_hb*2GSOTC;<!yop~7h^{^ZZa(Vv8V)cPmK(haps`4cZK*VIm#6n>{Z3#F5=*;XZ=iR?P'
        b'FHX43_i+mxA{D1It}+S;8N6R)<X!+;wjoLs5H0@!$Y@y1K&h7^4say(&;}M$JU0s*VAe+Q-~i_X%`!H~1P9m#WcZk0%mFGEGhc&e'
        b'6hmBzf@eU;K*A_0BKpkeDA{!J8F|PHJ)GIrDh3cckwa^L<9sWRCg^RE<l3HAwBqA&G0Zv7^trONUG$Kv&Z9*ioebN_a(_B6nn&&S'
        b'^$qm|Pb>&Hb2?+ZzrN2s+0#Tu?s%%-ect^9!b``0-uH1iDU%8B-uo@)^YzyA4eKU(cOlow!l7fhJP+ozP2#+^tD6cQ9tFO?K7=N='
        b'Er;)Q^JuAn37&!dJC&v~KoPs80y4TQl`q@`kz80vwU#O&qmXBdM64Cs(26O*TA^sQyG)|nkb`<?Lfv~TvM<j8LSPAe$l6R|%phlc'
        b'N*r>4_bq_90t6NySb+U&slq)dS<AEL$IgQ&K+k^40?0Z9?g2}Zb4~9k&8i-UW)Zx?OkYE$$#nBXQBD&zVh?>Yz(w^WEu|BA-r{y6'
        b'<h-vlXwRqX(n!l1Y;|I1(LvHmpd<XUECp5JgO&iNx5j;oJw3<a)JyM&do+vbr0(vDW0EGy8jT#U#xK-s#3MZMd+urH4XX2LchdKF'
        b'_Hdu}pzBp)s7i2w{oiOusmA@hzc@9Kus)7)SdWE&qUO_K3hgi3Z-F{?eS>-Uc=cb$eB69qx!!`JIJLu6a}W?@96rjLx~VN!U_6G='
        b'(P%>VQ5FbjOAy8aT_t*ytu3Rrl*3p+s_ZEH!VUNjBLd_LgHm{uWgm_O+S>&rXaOPygcku3=b(>#T$br5YXL_tMQIYREVcX&1!;hS'
        b'BT1fn)B>W|p+vE85s0al;@=CS5Y8S1!937YdlZqWP5h*Yd)yp62Oq+-DFq6!&3~lOX7A%5(jNyA?Q&6Q=m7{f-{Z^x^<e|1LMQJ*'
        b'MJ9Hb0x8nYEd);EIkSfopk!++#j+G&!snc25m(B9X7O;3wL1;GGt1OUL6>Vy6tG{){Pen`J@g~hcWH(1<fpZNs%oyS7+j(_()`=1'
        b'&Py%Npt12yp=x(g>LpX%Z=bu7rdB^b(W6{1t_cHlZ@F}RhqCr9#<h*za&&l~5^`(bVz+E|ZDYDWf)xA0U3lB-RYHLvVD<>p{3g1k'
        b'&I7Vx8{_{yDuUeNw-_*cYCWi!>n&yQcVQ?AU4@cmN0exV&Ne{30SXsxQ~KTuM{0z@0PD^6v9j)$Jz&GtB6mCk%9yq(>z+9WCf$Q#'
        b'^Yl>W)gE+<$PqSZUyo2c37fv%<*ImF4i+C6dSLE-m_{Qi^A>-D&Ij>_A9nNa?3T;T-!VW{TaI>LVVj2-pr_U@cFQZxortl^wy-bU'
        b'Yp!Gv4XtCFUs5^_U$qr5W%(@H51h{c>6jL=wLlXf{F0e=ZYJ{JfQOfjGr6NF+ymo^nA}jd95H#}A|;5u$lD?=%e=hD_AcUQFptbB'
        b'=Mb;Lt474hCyEGZR=7T|XF+>zDD~G$Zt^*ve^u?l(BuGtfj&TYNKGa>W`?<#bM^m(w+#ITylHS!9qHkK*vU`CP7e4Zo%{qk>3`VC'
        b'm;Dbr8S;yr3>>}+{q&bIXricq4WL<~@lFN~zvj<DJ*)-QmCS-A>Usf%BcOXo;DMBSW?areSD|AM`)QBuL9*>#rTM#VNVcP0V`3-Y'
        b'SDGjF^l<YasXvBL0NzB)X!r8yX0$i`Ci`U7zF5!6Yp%OHYkq4U=(Z%kT7xd$qZ?L}cB+S_EQ_jX$!en`J9@PWJakL;S2YcR0A|UK'
        b'b)P$jq5+g8JHw(%cKi;r<uDG7(y}6XUkOdEinC<vEya_ToVQ41MTh@Un8R2W$;{2&bgCnH8K}LQ14Z17RRu-<wX5Quo#W`m9THPi'
        b'iMA-&Mwg(K%AbY6t}OybaD7!_fwD-I>;bu4icYO?tUw2lyS?Wet0t){v7mo#lVaoqS#V9#a_wAzjMb*gJJ$dqF1UeVP}i;zKG^mG'
        b'{YgWreBaCVfph4bb`;DwjhbJx=9q;3L<<f>Xd*2y`Bq`y(;Xl)9NMYF5-dsX-hD1|8u4$?f9Lz%j+FSC&w_rOjtXex>_=5l%D$sJ'
        b';2(2HJ}&o<+6pM!fvS;Thz|QHrly=vURGI7cz-*VHkU@{pG)6H!u&Tp=Cxm^^SrzNj`r2y+;7imh}qo0ITlNdEG1&mIgH5L?wE12'
        b'WB9vHm3QV3*0|f~zC}|7E!!GvuCt!g>nqx$ZJG2OddV?aj~`d;*`e6=G{0-bBf|%khdhTG&~_j>wqt?_O0JSqI}{kc6x(sWGoc`Q'
        b'l#XH3^uSQ)Om-Z9o8T(Ce_nrs&*f&FTjCB9A9Lr=t*+w<?AdeW9Q%=HVh_jBNwo)A;C=Dl7(C5_rw^AXpG#Na(IhV0NMOUSD^+GX'
        b'{fq7Cq*;N*Cl(VJiPO&&V{;Q%Na0bjy$aJNW}^iSbo%!mCxgA7_~&>fCJSLzAxs~_h!DnwFeX%1Ur68hvu*)5v)e|5T-fsn6-zKy'
        b'#EI90>CtL*B^`sI?FVXxc%BZ?GB1unnx0Q@cBKIV&mSZI9FHH1PNGlM`<&_<&e&{o%nGxz*sR)Uj$_#hcXYRSBCYxc7n_a8tiYAU'
        b'xN0LF7k`cDcpSA>g->8?iNg&_f4yr(9+i5H@Gb<inI`cGm?hCY(mkA`%&X7Nqk^)J0Xt9$odiZIAP9h}w|@)OzfC65wI8FKILrMq'
        b'_qS)E!b%U}odpK<1P!iWaXDHgYIl)~u&8T<bv&PjeD|4dj_J-b^L#GAh8oBmj7|bTh>U(4j-Vi#z6OJ9{V(KVLf3WldTT3sMoZ5)'
        b'3~ilZXv_Fc!J}aoe_r~BFeK?y^hN21Xj9ix1S1Gk;YD|Lp;z1K-PXhKTo&1o^QSPjG6WTv#7#5O_Aq7*d0WF-UyxEvMPlN7A|X8!'
        b'#_*80Gt6^L*7qcV-i+7Uh2BUz!-&S(#as9SZF-9{);)l50o`e+BQ1E+3m08EOj4RFhi&<w+hPVZ>S=08UCHr@ZTrt^@L10v-XnX5'
        b'&Sh;CP1M`6P1{lx)m!t~;ap`=n?CQuylfSPO*up=FeXN~bqF0sgJL;Lv4z*M!~v34g4aWuV@I~?Njz3uN~1HhcOSzAG6QNN&6r@G'
        b'rkzO|HgwZDmTWnnt<bKS!28#h%$!iN8eLWy&?wnMjCy+%x-wLw<bHK_<yyIikEvIjqtR8}>(<IGkdmFFUjgwM;3uPF)p9EWcGjQ6'
        b'E|!Qdv2&m~C`^P9qh5=<M-lyv+$U*t85i2pcV1jy!z=4ochgAyl+2hw$3T0mx5JpW>5g?Ua^7>@PtVe_z~pngo>KxDv#vt6nsMDR'
        b'xm<;wlaEZVZbmm#rzKRUDUABGD)HQBH)fyT?U2~i`HAZNaW+?S%4Wj)6h_N@ep0aqiHqQ&{pd7m1?K#$8=VEK7FRT)(Z#1!*G&E}'
        b'tv@A=@Gi!(2~0!6_~I;;Xe0>IjDr9}n+44T+Qni_G@3~xh3P3VR`>+QY7&nq8#&S})tE7rnKGIs?((yuuL`tI*>oXOOdgals4Teq'
        b'g|p&fC#ed@&?YE6&xlJ%3t_ZiXbC2TM;1_aEJO7NIf7vl8<hZAWyajkpihD9jN+$yfXN}4n0sa91(6+r8JmaTTL>UJ6*QkBA~3yq'
        b's7#O}{}pELI7|(Enuk6;Vrb+LOiSbiZWLdbR1ugsG?mV-zkTLya?`ej3S(ye9Ou{>Ql4s?8xmIyrwmsqT|t-Yb(czkkupjnL;Qo}'
        b'p5bz288W5`X_jJvQ^QlQ8!5^p23&!o|0g7JXGI@gM55TZAcqGy5}`419F3^UK<iYVwF&V$C5h-1X<HcDeuRUr1~`1YuM@`mioThT'
        b'y7T~lQRDd2h%W%K(!*hrl14yTkB1+k?MGOlGyi=o#_@JD@&bQ27Sa}U|3TfMGj8A6z$N_J<Z~^-Gd=S8^y{YY7+z+x$lnoUG@aMo'
        b'P1zm|*`|kVOG91qO*IC^p#zRwOckmb#bQGTR><wsyN5%{HDT2xjEqjjaQVI~2YM%wxk;K_)^qZ{@AF~A2ZdNjlbb~5ver<zP#J>P'
        b'DtNvf4z6c|>yyxF29f(Cyl2n_>~ZISyUZ_~%`AO{UbLa+3{Ac$QRJ_5NQAXB%GV}XKE1CfE$9$$0idnr7jQ-CI)}j%_0GCg^W7O|'
        b'NlB_LAyl)!PSQQ>MR!H0WSAI_P9}2_B4PaoLLXQ=1K>D58!otYuj3n3zq|a5O%_tG7_GZ?7Czit4O$%9jjqzb=C<MH+_RQg%;Mx~'
        b'l9AXD_quAh7tS`}&Q)g|M8n7ek_U0x3#MLDvIzy@lDMsBEgZ)a8B6MT^E7S^>fEbRI)`_%wwMr|pvW0cR<d<2EY^fI)(4(V@Nt^O'
        b'm(VP4OTk$(D%Gc$iju#=>Xx3drH3L)*t!j?>pm+cb?t37cApDfcae7n1iUXj(c_$<GG`1&W4gM7pVuusgQh)D(diy;h6>L>isfur'
        b'gR{Oi8^-48(m`@)%<TBFI!x#W$6=I7FJ39n-rRY^$(5fNE_mt(_w+M#3}8o`+abJv3R|2h>MDwqmbCoG+3|(+KRF{Rbq*-MIbEsS'
        b'L`F@*aGgq8`tZ;mm2_Q%>ET(Iq9SO}1{k}Scc$>_-<12;vKds7zl2>^bv<7>CBMj-Uc_+@XEH5uIC+Ot>*z=Wojn6Q$J7?t*+82~'
        b'yLzHqakid1(=L0bZukr>fvSuA)D2FfD8;0v>t%IO>o(9b&$BavZ8jKE*LyBfj;$Lcyk;zgC!pOo+DzLI!w;E<Z9fd}f^B*z6x3mn'
        b'!?*#PKIimyrw(xH)`&cWX8=l}M;^3#X?i=SLn}iQ0Z^gqS1ykXbLF$X&+ixf=C(WB<w={lFAK&LzGmB5fQ^he5eC%Wk&Fd6wnVMp'
        b'5Il1XKZrwr9E%kt#|S#tvsm8nH(L8&blZDpZg8og&UPnT$`jJ3F?V-YAPuRwfPJ37w!+_7Q5s8FIc$f#G&yR^9euUlU(Fngwmt&%'
        b'++sazQ-rLW!Yw&xZ?xHfhjqUNn(=N#=eRpHMb2bzQ@B(_LlDsLp7ofxHa^$Y$Zpy`3$*;owBg;#_BQ?AKOzh%u-f0cS`Kz;qA`#N'
        b'EcrYPF7zF~2Krlg9a$P;18R>jJLIlc*s|jcJ%ye`PiVcj({#D2`z-UvZ)y+e{rj1KlV2|VW1_j@jE76r?_sv*<R&+f7N>U0O?{5O'
        b'tb(DFYnSe<d$a2p<x5Wn>;pLiqT8K3y(HLHNKf4|hVGC_Kl!L)&k4yRyH+M4vYl+gy6Ric=v(ud+Ow@UIG&cZ{%WVk$p=s0cdtI<'
        b'<9J7|;{8kQ9D9S)R%iIQ6xXj>UGBoI2NSuMyFhvHd<=aLbiex+8ffh+q*VgS{~YbkgF#3~7j~y9uWx4d{iW__U8V8q?di(;<!6pX'
        b'0f7wDK=;#IzBv;}7fL>n(urE#9h+-*!S1i5Qvszb*C`z7G4)r0MbUk5%OoqKCfc9rs=s{3p^XXpqmVDNri)gr{~_QfhNXx!rE9T('
        b'Ry1YSgDI0$cnG{{jsIQ7@2{viRD`~g)t^2CWu5#PXjxH8OhM^QhgMmieg^Cp306{1+ZS~?g|1aU1k~Li8Xymb+Pe&+`3=X<IDd9V'
        b';c(CGvaPFfa6k!Z9w$p%L5$}AuMHoa0Zw^&GZ_VRnzmtf7w~AH&9;3n8)RXieW{7%ejFYBQdwVCRsjqm-sk|_0Bo_{eek54?XsmI'
        b'fwKvdZ@E*pSzngV*lZOloW+<tm6<Krbax+Vo(A2uBqujX!7N)YwK#caOqUU7Z7Grcp$hdc0c3K~$#6l|1@(RjNR{d7%@!p$)|tnf'
        b'WnCb(Y_X9ogO52C(8Q&dlw^839glr<yom&u@Bx$=UZQL>p2;&ah{A39{VbUit9>%89@x)AafNv2bWoht*X|A*y1URaxNJFy51zEK'
        b'vsgacM#p$xAERTeL12y4zo3K80r~V>Qh&rAJVtQOpQ(96obm7N{PC_2dv7PJukgg3v-q)H>tBYN8zvb))NKg(!?r)LJ4l)yl6UU*'
        b'`NwwceP)Kt8;wP+*YziAr|)gvqeM3t5u_qU6txOfG)^j%;wp0)P0+DY3D!hU>2$fx!PBhuyKvN(^b}riFc)Npo5&6VL%Vg}sUNu='
        b'RzEi;I*S+ZfMmYCz0>cfJX-ZJ@s<*8TELGTNI=&ui}#LK=npY}{5q&jrd70zj(wZl`qsn+FN+tzqoWe^6+5C2kT+{&%gF;f|2$5Y'
        b')gXM>165i<8^I)r8IE@zqXf<3CIT&JOK_nzz=Z%D-C^05a;Akl(?n@A!v&w*&ls>?9KWCHW)pFsc&+}Rd3@0@rOuPMU+nVvDIjYh'
        b'fvPp4o34dblsml(Ev2dLEZv@TOzzPz^*`&1EY&J8k?Iic=1{U=V9YH=>|0Ns5i~LMbZ81H@)$Ywy5X%(_sT9olY5Rl1701S^x#fN'
        b'bdvHHVteXJJAIe%Ky;%g`k=p>4MZRCMZXIVwbg80ZkNkd5s0>Vme3$$Jxgp4?%ZA7S%1CDlfE9P2VNZ5o$OxN6_D*s-7E1;KDX{~'
        b'aXzr4h}6jwJTjYW8&g}|N>6sB?~L5P^mJ$4wJzWKM0Z7J-52nXTQ>~9OT^#2x~uTJ_`zLAbwgdWd`EQ9pRnnT*ptzz`xMvFq&C{s'
        b'kT&)DltZWY(1dg}LYMB|uKJ#?Y8ju0tJAO_?{li}>e_P0lZU%I;bl$2!~2vyL{#N^!kPjPvieWElA=9%*w&AU4joq4-qn3ldFtaM'
        b'3iaQkQ#Kdhs$QX}21I<A_8+G{?omkSw9dDK3aWFdhlmEEq?a~V7klyudV1%MQ+wK@DSBS($5o&3bo4R#bbk8LtsiH!6Ot)=T!YGX'
        b'LfYNQw*Lf|-VI}=)y*`)=Mhp8`C&vfod7`iH3S#vN+W7w#QTn*26{=Y2>zIyjz++)?rm?U<x}<m6zje4mK)Gt?~QQe-Zk#cE}Bdu'
        b'1UtT*c!v06Ot+w9jjh8*rL(q+CWPZ(J!eEO0va5hvvaDNOi5U#{ww7<Ip)$;d5(XT`I}6S65sNr%|_{~8Cx~G<-Ey6UC&WM$^@wo'
        b'SaFg`FRqeuu@$ar_*1%gcIx$oGIT%da=G{0@H2AjH<2+hZ0G`;F_(OQcK2+h$=K=!`ZX$r<M+24Ehq0+lj>Di<W@dt+TxwxMd+in'
        b'%Vet9Eh|k=cdzZ*Eu&>A=?lBJfl=F9_tP$PAi=ikTy$-uc>B-}c}EoVef)jF|KmNKpnmyY<Tg-%y@N=Krircd=<eN0_mZx?)w^Z2'
        b';_ZBM>#-(sWE7njWHQ|>EUefe@6^%4)ayRElwO`8uWhPYr~7W8K4}@~m2K`GXSDmX(}?93cJbyYpByu#nWual%)@wdbiJXAGj#32'
        b'=}vkwGEmKwV3t|T^710geFS|}?Y>x7y73X((PNhIW@*ceu694p)U(>_VZo0ryXM#IL|2%r`)&&|iuR~?$_1I^{f$tRH%p)d!?D-1'
        b'm3fQ6G@oKLZ8n!%6c!6Tod*Y@V9fjXFfWr{pNm9Tjqu7`z0oX~C%k2(Uxy5fSt^(%^v%rQ6CEeQMP~Z_z;YZ21D}v75YnMAYcM0>'
        b'H^)_^!V2{jQAI>ymRZP|IE9~*)A2)iA>Jva)z>ZKb@Qn1?1`4_Nz;vyx;w+rLa4sx+AArnhWiN*ZH8LB9pURK%AfFn-N>DwHZo+`'
        b'-U*t|_EZS1^-(3-1f8uY#OU+DTGLx}j5N<y62i=Rg@lfgpiG7of2ln2LOy_TWTWR@ta&%Hb+QC#sN_)CeFY&mMfU^}e%}%5H53Yr'
        b'eoJ)bi6IYcL_*ZOJn{zNy^FX7(Z@&}F&IiK=3}IbixR3;E>~=60yFX?S#zkd_~eSTLqQVVX3Rx(@-bL}=N|7LlYR>_(~a+l;+^VO'
        b'NyGtJ6@rr;7L*pJig!-2aO`|7(!$B$)+gxlNeLLd3ESFSu9rwNI4bc)PR9Ka(wgQ!oenr-0$ieLss0%Sicz(oZ1=~f51w<qq4zlB'
        b'Je+E|Vt#d_%;V(ThtSJ*E@nvLZtN5n->L%6Bwc<Z@)Ls2sqT7|d-B{6<@R@q^Tz6cbK3l@Ml$Gp#JxB2by5#EwTRQZcaN7i_=PU5'
        b'k@)y~w-06XaF4We)7*6;pf6^~7b-4(AK+qwT&#Ns%3CgfM$vdK$i;OLL!`SJWp&Ai6iw7IiM#4Sfyf7930DNr#qSX)@k9434?iM~'
        b'k?u+{MGZ+BjI-P?b&9*>{;VdXuVCD>o#0>Ci1A%$-d8Y1${%|$;?(#mfl^est*G-{QD@|NhCIMcY<`q=7yerf&xk1fUlGtk{KNxa'
        b'KF#%=;`t?NL1K9a3vyFUMmE4D2`eYM^E<`;8IJ^<vH+mLE`C&JnA3Tu?Hb3N1fC57&N=lw<+JF}Q&8JwI%Ob!qR<ouQ-VFj23Af~'
        b';SA?H#o%%kF&^sa$U(6-uqV-hIM!L*=xGf;Q9Kev2ZfKxAKroFK6wf%Y#5tq(}l32uhkz;;NvH*EV2k(JdBiuQw?jBx-4C?io}4v'
        b'gu_=cJP{z6nnNT$F#=zkHVZ6R6zjlr@Ufm}$i*1Haw0Z&pz#aS2O*=GaUVV<UMMzE@KZcDMPba0(F4t9#_FIFsKL?3=oaZ#0qLnE'
        b'7@OvTs)8H?RiPI8#c$VQ1;+c_u2U-L2NB|kP6l5C9pbi~(sMf0Ge*uGKfRo!<CqxmAvKYM%h2*SJOMdQ=J<7QY5|YOq8g5ek-290'
        b'$7$$-O%<Aw0>h1^9QVE+o+0h13S)F|aggxZfrT_va@>DAEjFDAaLGZZ(mirI!Vx`OY`~cibWRR%OpsH$ubmdv!rO{=ZbA<i2kaN*'
        b'CVQM(pEJdM`Lsy*T5yC!8j&4~cK4z@cOUu%bABA4_z`JNb)S6z?c_NT7^-3%*vbC^SbL<6F+pc6iKil@9Yr|@&jp=v4?rgY*||Rw'
        b'YZcW2&v7Tu9VA5X(|`bZKjl6wzHW}xz`so#lx^CU=79m@Qxm3nI5sr_8mJofD7U{CY-6^+0d9OG;sZ|o!s`J}bu4P6DGUNDHIb0M'
        b'8=jIc4TQnBnTSaS^x15LT%da;-7}$?0p|orHheQvgD0ZnnqqWDJYIuOfC8)v?Ll{MM-72YC=B@+3ACFS=_QM=LA~@m>?OK|4MXww'
        b'B--?QG!@}K{W<E(FHYC>e{RbS*(Qg;nKI#WxBN6XO_6=;Hd$ze6e}h$4TWV(FjHU1^jXL>95VerWD0~<n5D($D3w{IF;m%Q2@0*h'
        b'71l`cofN)bf@c#r3bW4_%eRM2y&=;lA=AN-#w<6QV|JQl`_0kWW(86TyTdDRtQbe-Rk+HC#{jRaFw@263ABtcCDs+3wyh4CB+qYR'
        b'tb-`SZ9i>W6|zy{SzksBazJa~P=B_WF`6-r886ut24LAZqfW%#eWx%cBnFJcz4#sBsn;2kybe2kaf5A7s5VD;(s{(*Xf}Nn+V%wi'
        b'5j&)WHUhMU{|o~V+smPgEhp=PTy%hwL9vbIN!lIZVl+vkto!a1TOhX`4B7UEpymEI*KEWm)uo@V{(@N@+KHx#V)f6;v0WkP8G!Qt'
        b'W)1Ufs4!oSjscU19XJ(6q9rqgQK21C*5hIKyPsqBkZpaa@Tolafm3K~#GYC|3t!wY-qexMzczG*d7}1pz~RL4h90Ry?HobvZ16xk'
        b'X=sxB(^F+uIl^sY2-_L*|9XvWdkEU^9y`S>frd_ihPt4kKGaYEHQvx1IW#0P?PG0t&`?RJ<89ElZ5T<BN1m$x#VOKExqpGk$(i%{'
        b't5ojq57s|x2S+<<t%Qt<BFz%#W1m0kj2}-)&0n4(qhzAftfMI;fIpk5ilRu8h{XF3ZV*rN0U9OE3O9$~PFV}W@<_dDe`ur+SOd)%'
        b'u#Aq3qQ=McDQx`#G749b#Pm{->v^SS?sMDhkT|uKXh~H>t(B>8Nue^NGE3su$~3sNkOxYX8gU6co7JDQDmf~T%Sp40jFRe+J3m>2'
        b'%Z#{;;S=?GohcZC+TDv#YYwin#7qRQGKaM|CYqx@C-JBUApoL7K>lVvv#ri@*j1LVRFtacP9UQQBTnu92+fs|a!pip)Uy&}6s5-!'
        b'StgGSqOPjUnD&LR`ek`Z8=;;r_r*-y@>ka$#^;#mBd9<CGwor07RndH_~F69_@GbE5?&4?aYBX5j-f^5hy{p|bz!wmy8EN}XHirS'
        b'an~P-&X?V<qIMVT1ppK2L=gmnTU)ypfTpMkZ!$)b*f9cuz#59f$ar5a_11^Q2~bLdM;#+Tq=-X8G&sWrd%vH0-MtP0RqKAR-VbYF'
        b'{BTSa6%8#R@-(<aEQ(skiqk?RKMfb?evl%E2+BceC~Cx|46$asQYfhxOOE^`T=3jYFFK*p!$p%(q~|1#C7{7avv;(|8Qt(9kN}NH'
        b'fJGz#(kF8022dej8L*3yiK<9%SQO{M8VbVduWthG0!?A}TPOW{7!{1z9u{N*pi&HI02xpW0RmQWjDXKYRBBg*3%>qR`dP$h^2AK^'
        b'9sE05AoFf4_~0Zt%j1~n(JUe@n5QV({qji=tKwDI^M&(x>iP_K;A9(p%9ECd?#LDQ*1^Nb@~}G*VGS*9(lKfWK@(oUwfm{hgR+m+'
        b'Z;ZNseezuRb5B|>oh05+Rj}qhePinN5gV?aKbj$LSS}x_Rg{z{tYEJ@v2@%m{aiGzqetE*8gW`t(h%{l>#=$6!s-fe7M{g_&dqaf'
        b'+aSbFq$k%J*}}q?%DGtKsfojL(V=rul7|zx;9~Et1TrX{Oh{*7q?tV8PNJJYuFKt~lj3BO{1`=MV@;9<b6EX}tlBwTsvO>}tlqHq'
        b'%{^v#fPePq)>U(V+#CTbT8R|^(f9t5y*|>6@2Nu*#yIYaohZJ0zM7*G71i4~M3GNTEJ%xQbfcvi?qpP-VdCdBVIi^9Un_VL7yP)M'
        b'*Q2RUmXcEFl$~ts7}X>h$wKrJaV3BNB`Py1Jr@>VqAfCW!v&{qi^mpga9kBd0yl$xh^RMck>~Ij;<BeEk~j_n80noctR4vY_UG>M'
        b't+<%nHtA&JT0rcdqSf2)`Y4K?R@-78KC0g`)Z9#6e^1%{G2=hVHm(ikP`eMEeCkrm-|Eq|vJ~~#dVihyV$1LzeQhmueUGwxfT?|('
        b'_2p3R&<P-0TS7!3$;NkRd>QsdO|JPokSuMxabou&6eo?we1QQHCwKYc(F7z~JVCNz_^s~h2{M`lapj9jfHv3qDL|<xFd~=~`>st5'
        b'tJi#2U00I}kk#}4+LKJQCrg491$C4JqYD!M;%x!E)Zw4|qNCN%e&yk$fC3mt4@d3Yh3+nw0XC5Fl8aSuKm%>xy9+HRiN+$CS}t4='
        b'8n*h8?}g374IiJd*oks7fu_n&j0t|CY<89Vr)VT!B^OdaqYWF07v+ohN@&dta_V*a?@kDDd$$%(GW4HlvwSXS@?bboyv|&EvhKhM'
        b'T0-ZVX0!AZMfGr_@=yRxOh+egGh?`JkKtnusf{OQwkOXxc(dB<<H#UKoJdrliw@tb_vf>qeSDt}TRy#C@Yj3hlP4`ytR*|ceC$N!'
        b'g;!|lt5Q$0P_z3a4on$2Cjni1tfIDD1i_6SS5WrdCwxl6qqWxVr|2nrl*oM4{vXEP2Ck{|dK|yGxp^VEXaX1za7%6oM2j6@D`@R1'
        b'fdamCgQyW*yGb-iUAwPRTdlKO5?Y9qZWvnys%viA6r?gukQaH8Hw|cURomLuwi~sLTDP^VTD1t=-#Is-b=&vz|9?N9d~TlC^PJ~A'
        b'=Q+=L&hwUw#zvTo>dEp%g3(2=;ivc&dYyoz<%}+;Ne-T>3v@V>ka|Ya9e%b+&A**JPvsj0M@}E-Oh{FIbjw~u*<z3`PB*cyj`UyT'
        b'oGziyC2|Y%H@~`PUnQAy0aNzHo}yoDlGLVpj?<3Jn$$D0Zs~I}dRCJZIHN`YGoAcOrF-VI-Ft_s8x__@wL{=8oR%}hwF{a^C_^XV'
        b'9GNQFmvjVf4_&WdvxgX+!rIOw<t9Aef=sz$yE(|;nMc@epd+d73MSSn@JWnWgi|}mt-Ysqz^<L^)F$hd2j8vz+`fK#?j<=^|I82|'
        b'4Zvv9sLKIyO9sms5fOo}1xc!KV?yeuBoG2(Fib7iT_*y+6cqeqkeRV}o0$xJBn0B{CN(syMp7xMRQYxep+r)&-pZi8m03ZFuY}fQ'
        b'Gi5{FLOVrN>9M~zk(NloT$w7Cvs1F22SGHWO-^mkmg(-3TYf4JM9A?mIJ9?-52~#<oRQNjW{R+{EhF7R!n9Ptte75%yzQPN0<of6'
        b'OQ?@fmS2R0_DVcRsuyq7bPgF^gwY5;K>-P9pIdE~YpxEON!qkhq}nSjk_-w(N`9lnuW92miU&*I7ci2AMPY;K=2GSY$&fK7r`Vks'
        b'4XkreX=@w`8o5<#MYi9go839YBu4o7_c|CChh=Yk{@{a@naro<>(=9#VK(IJq9<w6b5T$fK4@Av-H@09Nol$2#yG#g;QtrDSauyp'
        b'SGS9@{5{M*W3NUuXk`>8gMb|zv?nTjym_518v>TsWf6h0u&P)Ob=#fzBjjn<)~cm$7vYiIR-K@lgr1#~b7c=wZplJ(qKcLSqm76O'
        b')4R6-xa~dU5=Qs4%x8ucGm2a%S$+?pqX50k%YH*bit6ZfI*t~pTlSz?ogh*V4DS5KE~KqYid~ow7}+)sF<JS`+M#PZf$wSs)d$t~'
        b'B2jJTu_E2mlQo%hWsZXOq6foFW4GcQZ8aC?QfRX$_8V=>vE<^V6fLuS8U{4*^BbN%`GRkhnVPb}o!6mRx~X;ZQc_axqi;3|fpQk%'
        b'q$geAeQl6^eK7Dlx*Q*l*06pzgAHQK!6wi=J;;#lNzm)gaLMO$&V+c)W*DNwoO#oR-HXWGKOJK7!sh~O>|Qw3_t7BzYOmWZuXVki'
        b'IZ~-?bc{NbR(r2~D8;^nNb3Axu8bdV(4H1Crb!v1DT85}<~e^#%GP{lOfz?ABulxJStkHpciB7=2H&?+2w7jk5K(=tYdx{x;u#@m'
        b'LMdAHO=g*7y;L(ch_iQMjyHaYSbXhY#|G!h&%3xq)8tUkt-iOp5BA*G+utisPX0X2K$wnE%<$wQe7s$aql;M1B)`kQ<W6KZ3^M(b'
        b'pydLroU0u1(zN|sN8fPYU5V$h5?1ThM`ZS81ok@iPlI%gYl&OVEY8Xtxlg$i-;YgM(3>`p0zmh**Bzjy>YDs_wOef)@&iTpUuz<5'
        b'&FGRhHo6yu(Q-S?fMVpyU+$}+XsLZEpd)YeEfwT^7tGr(On$$^=adul($zD6liU*b;_6zFQ!cQ-P13S%*%{eCW%MibkDrvOPEqGi'
        b'o&Dhc`~T5-cE5W6%($<vv`AW?q!ukL4<~kiFgUp2#>jr<=~JV_%8SFJhmpnN9MC`h(bOatk8{pb=RXx!|E+AaGv!FP!gOb1cqu&x'
        b'Z5?Vy?<oot5g{$hxx>Zp5RdV4qflseO{_J3BO>BFrSH5y`i^>Ig{WU7aGwN$|Ec^X`D5|}a(W;ABh{mndHC$c^n2H}tE=LSCk3n1'
        b'qpQN@wIl7y$`^sMn;hNK`ej61qyGli9d4S-#ntlnsP_+_r^UU$DI57T<?IE8scB;Pfw^*MtAcM%64HyohdrKAOnWm-Qyg}0!Jfh3'
        b'HHOLWuYL^|yVY}gh1rChnJq*SP*6K~Pi-&(9*-eZk54=}`phnA!KP5QoPVLth&N3Uag2+2Mv=%{8wkrcbA`c8LPV@4XVC5<c-s&f'
        b'`52dg&=2r--Awx+WDU;R82+>w4#AysgKrKPP7CDORn#zuWmB0zS1oYOQLB8Dw!xG6Eo#T@MRV|M$W1Qr6G6UCt!gB6uZ7VO>Nz2O'
        b'uKWhauajgRJ^6N8N|`#J8p}@@iv+D1wH;C+Sn3=auW+WIF^#?#FzuGHBYxav^w~*%69Zb;K+m)fjH~fxJR;p0wpcSZYxJcs|3A40'
        b'r8&2Qe8#RAq~-LmtqXJ6ehw0Y4qG5y5VJtPAY(z^g2L`F!{NWtKl(ImQFHv$Zjva<8>D}}X-B_=7#&vZUq14zvTh$}a?Vp{>+0ed'
        b'Q^$muCWvoN`xpOSv3c{>C+W?<+4G!OrJ_ntzZ>#&<&>U26mlObcl~A0p+)+<j6(H1wH|M7)$8#SgC8k;=1MO|3V2mE@t(~$AE3K_'
        b'kr?;0xXuIN{?9q0cp2V^d~+EoW{BcnTrEBQ=9%!#e<^#8J`?WxOIhzWwJLpL-@LQ6QvWwxf5XpCKiluJZClg}xR~nils3G)qqeqC'
        b'{0|QN6XBchl#OoQDz8;Z#^|<v>95x2l?Nc^kV*2L>Z9A+^NQqyX9riD_J2bYXTpo4<wJ!}hWGYH^=>RXBR>7kzAn=L5m%d0{vl`L'
        b'zTMY?`bw={{60sRrhmJynJhog)yCwU3++?<&QGIa;Ft-YhOmm*X_d3%99HXn3@L?>T{EZFE=T{5>8|`A(|zivg8}#n+x?;cF3)>+'
        b'd8X2zhxAQh?O{o;Mzk-f`WW=x%3Zi@Rmn)HS)*|d=c%aTjK9$&$Pqrh|NHc5?Mn`QJfc@t+9ADlj@8WwN8~VJ6l%UbLC<6&>R{ZX'
        b'rRrUKtWymCJ-i;81cAfrC`bL7K7Wmni6Sz>c3xDMDb*?OS?8%8GhOo(RvU%#d7e7iVYMrgE9+~*cV2^V+#01-Lk;vx8Wx}m5k;sO'
        b'3i=gDW#sn*emd+WS=t;TY0rwZIh5*MYGk&unz8aLwW)jk&PW2j>0c%uN^=M+B7W?y@2wA$^*Q}+sg#y`9-3~uZ~~;a9#q@eI30Be'
        b'X`x!*OUI})%20=ot974_Dqe7a4xRtTdf5EuT~c=>akfKYij(%c$llWmr%TZL>YknN1!qEw8x_@!YRz`Pdj-)z+GW&YhXNJ1rBvp@'
        b'6Q*R*S%)IMB*Pw6x4I;=?|=MmnUr1@m_OYfiPn8Q0#k?gOkj=`L<ZSAN9h()Pu#W!t^HXP0~yUy_RSNvgC|4l%|vd=)xO6Nk|k}r'
        b'>huJFavuI0XpB6BCvG!B3fhRtqQs*}w}JwHQTd4mkyBM?h!v`>TVbSKyhK4qn55Ge>&r6p{6Khn6yZC3XN14=0#6dJBvhY=Gcqd4'
        b'yp*8``{64HF`LkopKvq$%t1}LqX?L!1@T-7YO~9ABk7{d<)#=HNyoVKWiGc8n$X_x5ae~aF_B*6iz52&^}9*wk=ATW;`FXYC#0zF'
        b'weC{Tq}wI1y33AK;&~EREuPe|uY|T1S=BexI?5q>;ya@hj~G_-#{ro<ic#^j`PB)V8EFHBt-d7L8NkchSE4WFt}D*c)M+b$dbD)0'
        b'z09iKiVyYaW9bI9LoruaTqCJ|g`y4B+A^SnTAl4|c*q6iOpyY5KlYKyllGZJdPy|MdT6aRMDA57<5C3O*e;rffH?U2w9R#bVd7y9'
        b'15E6{jd?#Mf#`F^s$#{zzCKBl?bBNyAaj07EVf2DhbHLg>ZCI0O6*TgBxXG6yhz$-O1E4;u^Ae4jdbK~<!668*-?d^_YY1fm6j*v'
        b'AJ0v_cyi|lX_3U{S_MorP?4!s?`+0(^IE*bW3d6xwPh>SwTi{H>W`$(JZeqG<9Ug*G{tlAsZ1tDNJol65&rnQP=QZDfolIHV0?%R'
        b'9&s)dGIQ+lymOOX(|<Dc_(^6{j;8M<9mQ-~rs+LNi<nJIH9ZiTtHHQDy->XpA7va)JDX5eW$zds8CIVDOaFQzuJhP*7-);{5v8`A'
        b'Oxv^s=>_Gay+QcDnCfdDpbSl!T~bHZp_+zy>x?*=wS6$)j1<~q>S#I6iDp`l?U^g8kCW+zxFcsa3!D&_oi-3veBV$=_N9IbGrVP0'
        b'dBuz<*kRmS<XBtHNo%FTYQ14<m~?9GtDpUXo(WRS#ZtfyNwF6gEzW*(K-s{3Mt?Y&d2HbAw0zN6LH|IckjU4K@x!;;oshWLi;9Nr'
        b'+W}n7fuUMJC?dwb--`*uw&BD`x|8D9kROzazYf*U&CIN7w7q`<ms?zf-8|FH#KJtyW4Pru$4=qC<)nUI;R*v2mpda%NKMmH(+NTr'
        b'Nri(Z5Zd9X7-JIRBC~0;i%5D!%V^1@S48XHR9kXn`W1!q>`eS4BppV_R=kp16}Du>tkJn5BNOM)uCAe)#JX&mmJAn?G;SkP#0tr2'
        b'^T_FhLMEi>6v5KqHdulj6B_78NPNklKj#|%P7bY=(ils`MDke_N?9m9Ar|J*k4Wj6ky2VH4WBE;lmB_|5_Rv|_3`4rBJbN4ozzRG'
        b'>bKyeK61QYV;)E@H%7?U2=zikzu@c}AVqse8sTe&ukCT9?7>LYX|cgY7&gTx&5(POPqN7;Z5xq#d66`k6!kOP?33N3wL#tQ(%XKE'
        b'IW+T6*c0Ll4SM66#@QVvsYEaIop|D`6FNcfNUd^CEqwZ2TaAZfK9yGZ67`X@=grp6UIATob`~8mYc#3#6}#&@gKI-lhJb!!G1EI+'
        b'nDYVG6jmi&d#Le^gYqZCt?pje6MHtjaWF2<(LW6Hm94l|ue-$QwFpJqpw-Vys{5+^D%M*wd7^=Fq*cT!bR%31(_pmEj<2s3>@x0R'
        b'f_qSIp3rB6=wiEmLa%pZB-N0h%Z9=<U!8C;HEBRcjb@-?ra(Uw++Sk53ga-O&a*PTI1rc31?mFN+9PNo8Ik(=iH%o9c5?Z)l2|(v'
        b'12WaFR|30^@F%Cxteq7GO0P45mOP%sXyru2Ma}UO!3$dP-HV@|2tKulyKl)co`(s-@w%2&GC-J^*xWCpgZ4(?6V2fhM9f8;(D8Zs'
        b'@NNhPH5KqlJ$?eX(=o3i;-{G%CqN5^DHST{-*Qt5IwYTuPr8r_p&>j7Rci<bO4_wT=t)U6!<r)}A`MailQEBu3BGcPkI~K=RS4$r'
        b'Z>-K22nyaf(eHX9?|xd|MA^RUhl<8mEo*k4SZ?#9r|_wGdd&u7q@tTNu9O$<ai37H*=iIr#_Sn|&BhI}g|8bo%(Qi4QgaktFf<T-'
        b'nJjRgC=qR+@wlx-S9t%kyVrONTKgYoKNZn~w3uGL!-?j^@C5lVA(+!&6m`BR5@!z)bM1X8J8JBG>VsiBYHGrE9IdYF?bk$|*F>ro'
        b'Fx8)}`%>PJO@y8H%}p3-eCl8}<Z%{71oPW2Vfpqx#g2B!aZvu*Qzz(HrzV1kUraQzF4tDyGy>pU2%F`4Rqgy4;VM?2KQmG~IBueE'
        b'Z7DfXDj`a<qe>H0szG`CYN3Q0c~M!(HdOXG`j2!%>nl3C2-)fOxA~pdO50#RZva=|3Rpy}t+HPz5$5a16v4ZCiU=Dw&>+Fhrg&#>'
        b'B;MKE5zG-e)oi4=kZ^B^wriAHfufR$Bni#-ezlT6>leJI-w6DRP?)=*9Q;ox<$1)x=twGBDB%y><dQYnv}CSiTP;~$PH5KjKl{3q'
        b'S^jKu#j`)(z9BhwTV-D9d4XFpYoqL;owr=uQr2x$sP;~`t?gg8Zfj|uB40XY+RLvp&z}pEaEa|DEDvT^y9S_+C{l#b!kdfL=9M(w'
        b'bfe?kMT&zr(COlelqU{;kuM$tICKt?GG@!}kL0NWVqabi(@VEb#|!?*d6^NmXZojPe`HYh&l5xh#XqzOo_)A{#~4Kmvy~Fd&eZV%'
        b'VRl5xyfiJDt|Fr?zt`N`4_#~a31PM(CzaUwovSvb`c*~wE{;v=2NtN6@2EK#mQ%qAv!nUDSA@9&{%D(|SQIHCVE(wSD0A7ioD*Ep'
        b'!vkiqRHeGU?>o|enk%|80Mka^e23G<96#n25~~Ab&R@Amps-+$7|&Z3OzSVYH~>Q%JwQJU1uonUV6|e&!YvANEi|IpKb|%)9+^wX'
        b'SD6A6spkiRFI+!E$TVCZU@peVQ0ke1sV9V=nwPCei=tt8PkML5;y2W~Hcrz&0F5jprJ=nw_Y&C8DTOe5s-I_vLl)@U>7T2O8c|8+'
        b'8e`#>jB{&B3;P~7tRYK^3O`#Ak@2s`&3JuN!CM3RhiBi9BKBd=OB~8-f?tx0^n`Iug23}!s$u~7N;^i7v8fMY+5DYUb0RY%kRN8u'
        b'6_SETL4-y;07QUx0~rSug#^%~xV3=9_S6jZ;i-<Pu{>uV2bJ}|!lA4=8`}SQpx^CkXmsqZ9B7cX#~ci60I7X!=E2#!7Vt8Cw{3uR'
        b'4Cog)W>=(52l=dKG%mYc9|q1@qcGP%KVz3O{yRZ<ZWj?a9cFuKz^NylB_c;g#Z1!kdya?oz4S&c=r;rW?u#&feJ@;?7Zy0kspb%Y'
        b'JCK%ra)3V6P1?$^5-<TnJk0}z4N0#^Yuf3k^jeUYG{uz2(n{o(H@T`<%WW?8&wY;1RfUsDGbmbyHuE<o80|Db2XvtF>--!p)7)Q^'
        b'UA;@K@`1iGWVNqnTr#!esZXBDSh=qzk%^klpHr^5By3;VknOn*h`<P;p0}Phs^>kmuZGgEOpo|*xolVVf|a%%JZj(YaB2A>+}8bv'
        b'KCIU({X56((!bjcjIQCPV=en||1Ps*#}jv~4pDE7(jGA_G&eF%bIOj<akQ-ZtukK|cR&W=n;Vt5m-sDiT`gXK6igNzBU2ykb8GJh'
        b't<Tz_EtZr1xrFoWn{+%KuF(!ue^Pd~daHvp9V5=aef{kIvg(i2sxO6=cC?U6+@z%HbaGxro!+NSWn%_(58p_AqMw$!v#zBU_3a`v'
        b'w0468-;O6uPf@f~97zy#UHMJU`L+!J9|#|Q?)=-g0jMfWpt?FCckCi*0G*a6@qfb&-%fn{?YN8uWToAmCn^65?^SY7Ry6<JNlKEl'
        b'=$Q1{rn6XSa_3Viq56=a`rPWb3kg*Qf%X(zH<He@2}ZlV;OU8NS1$uaD>2ya=IS#(v^~`Clzy>)fumvgw)e|^dJ&p44`IBj<4!l('
        b'B(!~v9y+2NX1cb6!Hk-U%0p-;MgIA`&k04;3hYvWDMJu=np0gQY?40qN}pY?pzq-oYaHW0>f={fB2?#RWpcgj&VD8#g2t7j$7HI;'
        b'cs@><EMCVbVBm~?Nvy8eW6z>CMnt)Vge7~TNum=<nS@zQV#x8NB!BbPCW%EOugYN(o`jHm>sDq6x68IN)0v^0&>QG5bzNDtdg~!G'
        b'K7uQP!q{K+cjK~6@jhJVjaO-I^={lp=HwFkG&&YSoI_uCllGy1RCknF=ai}MQA0M9aXg5b>Kkq5xn9=S2Y`G$@6VN~I+$b;EzMu6'
        b'prf0l`Sp8X5{_>MKxa*e+l70Y9fIW|h|aGlvu6>sdpH0Qb43tQv57Kf5%Ccw@lvec{0YEV_pQX3Fbfp)5fNeX<pnFo@Ehd$1>l@`'
        b'gbSHBZjx(;dfhIXVT2?6cuI@S25JlcZzjy3vLwtm=OU6tF95>IWI0c^WJ$0tbj)U;av11?fYrW;#2{47ultz@!o?^)F{A;pqWZgW'
        b'QF7L(J}q8W9smXmW|o*E03sd7L-Z>8-3e)yGNI*dj+O<!x#7Re5ww^;t3l*mB6H?pE^{PhKm0dqvBDlX9la~4(ky{7OJ>Yc7roYZ'
        b'r9@;`CD>O?2SU(Nd(IV$Zo&+87h_g;B;{(LhOe0u7F6wppsJ<jg!Et(LdEBJ6hV+?VXdk-%2E>M&JwzXwH{7J$6B`Cv^>BCO2Ptf'
        b'a^6S#*mZrnuVkJLH))xr<fiV-r0v^YTw95in}s!I|F@tUw9bzQYAhF{-Qso1WhrYC2OgFdJlPw+sqlVi7l~Q!eYX$ljC*;X5)PWB'
        b'?u1laT3b(kV8%5zkB)3Jle$g9D`wKO@>^Eb?{X_Z{CfUJiYrYcHyEK>a_Nyk_oQkE#b_ymR%CR&yt)ow*{p9N{V9amwR<CY?<eY8'
        b'NwFTh)#zPF(0h~SlQ|0^U}zn)K5%T(v|}7sjsx|aQK+U3>QxGpE;7(D`3Ur<2=`&mv+8Ea+EUl6dX+wH+skCmV?=HnE?e1MwH4s~'
        b'B{=H9A^r(ryT8}2k5v_dT8zT?9wM+JOm*$=ZkJWJL8^N;45owc-|!g2OtD<I%nZyi+6!&qV$?aHbeLVvjj^d_*Pe~Br1%0C$N1ml'
        b'%&xr~WAz&s&M~|8ZH$F)&AP^3+T_Y9D?h`%#pDd5?V$f=&S_50h);2g68wW4%%(sOiGLY4p1|;sbCRRoxO>m;IsjM#VJeQ2;(NjS'
        b'r-~>vwbD_GSEb|-#9NHP6_#`#*394<TFk8XGy(}s9it$;#Gaj!{qNg;%Qth!jGbea?3;`XT2aOb<4tK&=s{WW&?3=h6bYV#lP}3s'
        b'r)33Wy_pw!7*TSm%Vl_vG`nK9)!_96P8Yi`h7_k0ws(5$ACh)yY;?&Q+Xe(~+CkAX)wT`QjufjEZI(Mfs>a(;)&6j-X!!+>h-1X>'
        b'Lv{Ul&K>F}eh=!G^B#v+AC&)<qq7%7;*TNDmX828R{q)J0(4AsZW~3(>cv}EM@2P}y99wnH#Mhv90L8Ns<b949+k_+<cw=PNk)2p'
        b'8D@Y^L?*oq^%G3V4P0ml2Rc%*l9EPS1|}aqz4Nx3M|J0yXur123zm6Re2Lrb>v7JGReg7hUvKw+%Bh@f#)SE$E+z0k3=V-)vVwy>'
        b'P$>{Vh4-uL_du{p+~R+4lGjr#ESLJr-b0nPAMtnz$wy@4X{wb3!wQn9NX?#Jh9s)o8W#S)Ffl}+>f8Sv<yoWl(^i^vx&&6|9%q)Q'
        b'_*$&(r+vF0>O*T@3BfEOm_niE$sUH8k1}vmk6lQr3crJ~&vg5?T_{rN37wt8u30Cw-RVIFxEK{Qx}{%}+Zl!T^<MU;h@)*uk6ph!'
        b'y@U*S#FkgM;GTLSb8c_ysvb90Q``|wlT3Dvr9*~WmI%VF<%RGyJS0pv>W;}YmLB?aP!=;(-Tr<MJT(%UG-_w@8vwlZJxq2TtL<g9'
        b'3Pd%$uV`8yEulq51NAIfnnRQtg+UdhScXpzlmfrSlKx+SgD5o<!30}Y^+IxE?ls#GUzgLvrCJ3$t=H$Wj!1}{uel&r6`P{mE@j}b'
        b'OtZMh?NR_z{*U+zN)<iEh`QC5nZaaNHYw<fmL{1dy(fOHKFyChtL3e6*Cw@UjsWk!eM_cE0RZ6;cM8v{GC$kW-n)5~V%sZ=-CBN8'
        b'UtnuN;u)#-)v{y;$mCWAVb^bxLcjY)lGBCD^0cmArkMqxB!~;nO(09%p&3SI`D#lfj(VdK%?yYqG5*io6nQ1rF4<nfni^fU{6<C9'
        b'n31ZXeMzqj^KF3#!p-lJmVZdhDyh*WT`ks{&kM}rm6FS`!TgXXebY47-(%D&e6GdN47v-Po2oT!`rH?Bj(LN?TUhUW!5;3l9l?6|'
        b't2rXRep_A4mT!)iCS|DxFWbKBacd1e={2P9KIlKEZ-Q1CW_`7++PZZ+IlSF@`g-+?WvUp}@GUzju4<@{k(L_7<yBZmw?V9Xhx;TJ'
        b'$IK{-j#O(Y;B4L`zn$DsYRr{@?zUy5M^Yl8+wHm6`~o}xHeLt~Y>y&TCDTjAglSuH;Bn+&&uMOWX(>gRZjEjE({W?ApfqWD`V~@K'
        b'%6WE(%Qxfm(5?hfv{4Oxrq{Fox*MRl=2p}-)2DTRl-atE(>v^XT*nY!g~X2@+gGEqwI8?Z@2UEb-GsG=48bS#Y$-@{JFBraDpX4;'
        b')HVw%YSZncbUbEPrfoLHI$42TL+z7k+>$S#djj@0&+%&h44++}>CXK^)o>llIs>Xejd+N&ORmu~tq02>-c(80hdu<iYRA9W<-MMl'
        b'5mi;ksL>$K>BI7OJCD01*J@_($^_Zt$g~@%U3f=TaV1&)0Ff+>|8DcHJ@tCfE4bvEiaJu9Le%RY03AGbU9zJh_6etZ((V#$TR`T&'
        b'pte?1s2~4*YFa?r-ILqe$?^m)u3{Iofjd`HuHhbSuZT^syMB+rw8WzJin<QS6@B%nouqaynA%&D6H5>#$r!}YyMn;Vzu<zt8incE'
        b'+w?Lz9xo`{U)Ecz*!d~iVrtp5Qw5uTebcG6SML_}o=VyI?Ac*lF6bRn_ZvyP^aQ{pm5}9UIV^DvuFV)Iq#dEEI4<AzY>-<@NeOg+'
        b')y8fBL`MUt&9y1rWb%IckxMS=*;-|(TrwE_#I{AzK#S;jphfgOah(uo%AL%)iq|ed&7#*qW%pgNebw{Z-&XAVTWJJ2vQ1rTB>gwA'
        b'DkIw!ruy--w-t2kX#F0Si`x0YXrpqoL*WY6;p?%T+cr<t2>A%|e^60d3P=}Pw<$^ul>ZV3VYI#iv|R{I-@IKx=UKO@b8d5h)xK%K'
        b'o}f*YUN`0t;w3QV>^%-#Qp#$!$)<0aaop_+D@`J?uifGZKAremoS!29FW@Y79ImWiBLasfO)}0_fq4@vuY~NJy*()@_YKeEH+)Fe'
        b'ht)`(VT98_@W*nOIsCUncJ&nNjoqz1w>}SN|JJ=cYx#2bMUsALxDa2t#f&A9zAz&3?eM`@BYd&a59CxDf{3fN+A{s$ay|nwH5a$N'
        b'(@lr5o*rkRgFhC@hn?<bSr|xCr<UFz%mLGht2gyBjklX&O4PGOpiTFylc=1~8PUw{?t)i(><Ot&xc-3uWbi+@JFjZJ0fKO=Q|L@H'
        b'9ui9{A_Ajaa=%X?V3rbbjk;0JCm?yJ<!f*Xd8g+q{wxdPW$Q^a+;h_yZF{~akzs5*dv2!1+jjIMMyPDtdc+iA`)yC6T}C^SGQuFB'
        b'xb!L-iEYpHB>KLM|IYSw&%TI%`fr5x^^myd!P7kvf(-*?egtnn5zK)IT^An_+Ot;P-9$oF_%)2M^b9Gu*$pT^_)1xhO-$7b(*CyF'
        b'n2@RxMzg=_0ZHv9iL``NqEV}Bo4`ZOYkQ159YlCG7M$#o9+d-9k&q;CbOOSs;vH$=YS4R{F_3+v$LQK=TuK<pFk5a<l_l9@d$`BA'
        b'R8W{^oFPuPNFKf4m<RGG=#REYmOp%#KNtKbr~FRvKQ1@w6jiI1&w#)<2cKpmz!2S)XEo$`<u3m=@CWYlS3r8*UH&BSTfX<}lmLAd'
        b'4;}H&BXA2|o&aiuG+{!H!Ze{sQlRh7pAodQ{bZ`{g=utLg9Qi|s7I=?(|f=T4t*N@H<bEZ0?V5i!2kindid>&vqpi`Ktzv=rxz8<'
        b'(GU^*X9Ycw7&oav8>x+I&3DIfmBm2d(M=Z-_#~|UKEbR}(@~+SOlX^X+%A<Jx-AqD^aH_jahBI6x@AqI?Qh+9nZv~}d1L)infJ@%'
        b'5cDwy#bxJw#o@hal`qf_G)Qx<V}E~)EDCgK{&pO9kA(^{Ul8an1k3sdwf}Ql1eT<V5!qUfLutYH73pQcGQ}dI^}ckwcvfy<DnPcr'
        b'V0G&WpG)Z38^omx3$~mK;o?VJ+C#Wp4&fpMmGHIW^s*pe@wFiD<Am=_nC4WM?Rq!#19{`f93`5wmsc(2Ep7jVFD<1b2>rW!-+(ef'
        b'S=Rk=!quT>-#TtP(9NF<4ECFf<G7~?jiPgWE<6h2sp8YI$8CEs9mu+=epF+2FwQKZ#<(lexnA6m<|HYrL+LyHHArHo3-`qkbugf)'
        b'+YP&(s(S0i*KK8dLBd(1zAPyU8nh2;37?j94hfDpl(oXj&L+|_#)V{x!$;4g<<?jCI5UYRvMnak7ZKxhZLjWBsNN>L_Ty&+mPbU4'
        b'0J<vb37JIBILGg^XP-HKzE5$fFNMxqP;iD^QnY5v<F;paf290UuuC&n7XQcOEctLT4Q;lp{XlrzVM)bL$dqRFfoUDJ&Qs%#ut#K0'
        b'DbYkZvw_{?vQ1&!OLBhu7SC(yt*Os+0r?Etw7@eH=YDnEyY9H_wA$?wT5fY7H!`l%a<^*(Z=ZlVKqJ22h3K6Y*fw<WM?d#p>n3fB'
        b'krduXjyF+(N8_H8(JERr+}1?de%C!Eq`k|IH%V;YU>?;)k!DR7n|<8Lq~aEICY62oc+dgj*jYsAelt-c2*oVqV<d!X7kW3>tHG-p'
        b'5ZEDV0S-+~;!-A6_v;B5&)E6L8GuL<-Z?PH5tfy>Pj0kW>Dm#T@A2bAjj%!AKHGM-E5sxOzZchYi+WPlB=k()ON;2Jl!x~mRJva8'
        b'UA%bfLCtJIsfsEo-m%JL;)<DHYUXsYvqI(QZcuY&^s*+Ajm3ICDN}XG4#)rk=$uqVx<PL?G2FSx<J}^9d6U={h4_xFQl=`7&lPW4'
        b'mGsIc2%L{OY2hN{VlAFWFHSqCiRfZQSVB4UlhF#$46Gv#rJE539hH?$(p?3$nVxFSQBafl$yn8j_Lv4`{j1T|2HfcCETVKD@ljPv'
        b'cZJ2RT2>pkE$3s-%@B${HSmQlN#t6(XBm_8H;xvWBdCq{OL#oRf8|DBQ0DVxz}F13EGVqFNvx~nK3Q9}!lBx(+*T9r{jB?pVBMQ)'
        b'4})OhR+WFn0sVUM6?v=K^{aHJm?q1kfT})*?03y<64*Y%8a_rg2@VM2_uFN}cuBXQiLx&tbUkvWU!iIo*Sz1!{-ryO;YFe@_|Km1'
        b'4idS21|1s+@CyuyLki!}Ye$Z3ZCgaH!)qysxZ1eJoRHi|J<-YbbQ`p(z_tcbTD29N?tUp=lt&Wa4&>oLnE86Q5!53J#Bf6dxGcZ8'
        b'fy0@(>b6~*y7&#$1{%ykAPi{vwcR1T!$v5)YCLb=&FQ}5resEHeJA^7sLTc<{F~Oo07B|aH?XLR?~8IXVsLsE^FwH`92jFG6yRp}'
        b'bk|=c;Tw$NliL{y#=OMGl-wPY=f(&}ch!4%e*#4WH%ICo;D?ppbOXwv@g{`d?>kxB-S{C|Mcv<{5X4KD{=eb1rF-zI6uut-4!`cc'
        b'JAtDV;~(eaALrxO-;JY#$MIL)`(qmHyVrN`lg$s_^+4YfxDN}evD+T&uGkg%1HnrHGfUo$5X~2Lhw8v9X~7x>k|)YXL+!k@ll|F$'
        b')+zZvNFA8XQ{-U`{vM?Vx>Z+0_f7<%dXg}eozDqEjgcUmJcM|#asNe2=s}IITM{PDrFMH$yU)l#M(W<=`0E7zNIfXq-=Rt9WaZr;'
        b'nNSmBQu*Um5D;Wzet|3~gPi-Nwt1arC`aMcT@?_Q8r8|hPt}S<JZ2%gvN0h%#5Zxw&XjkmJ|}^n1920n|LVf-Y~<K)(cvlJ8X|^c'
        b'S-P8+2l6@gA6=kQ@XQN31}p7`J{45=EHS*UM|Im1f;dk7gXW`JO9XSF?sBm!XKJ5J=07`v<yxX9Qs3o^TgtH?@CYmomitu~Ew?P;'
        b'*uVT+x&P?;zTAL<FZXiS|6jRXKa^`15;bY|A!QR;Q9Ioc8CL`2>Whxr$jaux^IS-$g)uD6HJR?jZ5pWq9d7MUMr4HQv>**y{7lz='
        b'vWe7%O`JQ}<$b&BjEr6wsO0$3ELg9$4s*i7uKA1Z;9^W_CrT>Wp{4Z^a&<@Vks~*dS;UA`-0J~qB8Xp{Cnyql^_qk>;`eJ75igNU'
        b'WXy9^l3B8SVDnS=ZQj~n@LEUFi(QE^F{<_-;hCOJqBw&re~(~vsk~8t)+o5x#x8KWwHWGp!)lov$LsFj>;f-1>{>x`e^SkKjkya|'
        b'CZ>V3>yW?PT5@xnI&ht9$g;eAFK98vb4c-n#Lb1XRCB1r*yY>j(PUEes#1Vo*9Bu^!#r^2$ce<IQ8$;8<rxIMZ(H3*Sp4oTywMh2'
        b'm0di)^R_q4Sb-VwBpmxf7x)p%if&vA-M(IROSb(fRlN+8mGSV`2UD;=n@ajr@V_)NMzS#+(>>8O904B)V{{8u&aWGUjc<5{U<6gI'
        b'l^LMLZiE?lx=_THEnVFbP&Mp94MQc9K&5fHMoOrU_S$s|n@DII@ZFPuw<#j-zw8QLZ{^mC7|_3;=EN5`3}3_7NuKi^hxbz1?=@Y#'
        b'S*jJQBm%_9bT{TupXhHfw4f{J9nL@!RbNcuga6pjX;7EX$?`vPs!R9?rOM71or^`FV?H{>jvzu=UAyqeO@k0Tjc@2a!&cQKbvb!Z'
        b'pwUFeI0V&Bsv)wvVvkRkTG{9;B0PT`Zx`UkUR`QXO4URr4^`AEpye|!byjA(6Nq5zH)y*hy7#y#yc*^~{{hcks5WGQ%Ts!<<)iVt'
        b'LswKS{r7Zv>s4P6O+ww4dxtkcSi}0e;@n!vf5ROBm&-*3-u*YY1IWBA<vGtYuLzk}+{F>t#Flg88h<D7jf4Z_*`u95)XR3LbL3@Z'
        b'odYHgKo>mJ$aA&D4<fBI#76VF$^Df9A;)uzhXO(K9smoFoPRFL2=-j3AJ2z`=<GSo)A@3zT^F3<*F@S~$rZIqn-hzwc38hJ3uzeW'
        b';Y#_0SP*1UHHM?5WGW~NPdESa-r}Wrmt5;wTpKEmCCir(szxRDx1~h!LejtVhYTxJjgcX?4>q9$J2v!cT^;oZb{5kdf_<ZNs#`=M'
        b'yESyGo+k_xp-O;Wk5PtTR;0i9zv%xTZ8DXR4z`M?WBl&$sb<j~8!s>9h?*?<v#m*V>8Wu#Zu47ZuFYGkHnImg%lm<T?EX&G?9s#p'
        b'coj2S*IAC&BPQ-xd$UrRxRy!WgqIp1vM+b$h>66?<sdy`$(+8aFaa+wst|i<c67hk2~rUqm7RV(gM&^-r}!2hR?+Fd!8^)3@dhh&'
        b'z0fHh<+f)f=91+{_$Yg4c~fw_uZeO*RMd*>31oWBbcb*FHgtoO0kztv_A~_dorH!_)6&VDJ3r*<CeH|`@=*;`z{CA81~)_m_ED-j'
        b'%Cv_{oqvoi=?o3L5vYi~iA2m?)cL)hNTNdV#&}Rw2&pVgFbAvb435tLIWI!BmCIy~H3@^(m<A>^yO(vsupzz~x*sEhY}JxEKO>e`'
        b'(Q>>dBlQ>_MV@ht%?n}SCMg{M5AbN*?D$^oDkO_%$Wf1Zs1tmCnlO@-F%#6TXRBWDKG1naK+7P!L<vb$7a|&LPYS?GiyX>|7F-`r'
        b')RAHXq@JgGSPn%5^b!!gb+UichCO?+mIW6(%vv;+iHQ<&opnZ$uCub(Er#09!yS1)L_M!7QvYvJ1#z9=bckwZ*oz_@y2AVIMNtmY'
        b'STw_Gp8>N9XHlfp20bwXk{U_DYKs(WHNEq09aB%Lmrxpc=Te5(-sgpM!<LSaPFBjJ4IN3WP*o7%bNdz8-NaIG>ng`_EIQZ$ZkPjN'
        b'c%l&8p8eOsZT73h9h{j5ASU8g`P(^y{YQtmF{EGm+Sz|~{FhE2sJV{q;q3UHU}l^?l#Tx{s`H;ZP;viL2d~Ow<*a2<?8hC6`f2P('
        b'9XB(i?1hfR7?Lf;1PykGcX_e{os*c{$pbjsu~$#9n>zk`PT=4{ukV;r!x8dH9&$eqxtE9h3m$T55VEdy@_VJdqvIB2U(xYjQ;Mw}'
        b'Fc925rwBZaHDlLw{HGplD{SB0*kRW%w_2&;nB5H>Y*R<AY<GPJc<MXY#t!EuV)vUJCOxs+(_w4qsFeoowwaH%yAx11I~0o+N_Phu'
        b'mbLfaoTo~R)TZ&e6!et`JA$1Ck0{O46lVoci+r^Mbrf{%?SMG{bq?JxcYusR$DR&<=$s$udgEg+$-1TNvW_Y}%=BX{x4Gf-w$<%+'
        b'{d`p+Ob9x@zX#Cg!uncna@E0l`CKIWzx~0_$3IBfUH4aw*>c+3Wsbr#!XrLh$DyTjr6Icx=%2F%mg~YtWJVWZj-m_+;&rR6ru#VE'
        b'H$vAYHE$oNJ;rO6rcGfqX;4wQKGHv*C@D7GoD{1GV$`lw2PgT7LiG=me2v99>Ck-AQ6m_Byusl<J$`eJ0)urQLoiJ4C2`ryw#6}a'
        b'6;+YesTb^L^u<+|oGvRZM)Sk``-0|&>&Ln&dO6^5192G1Ru(Pkm@8VFo%C`p1gee&>G7OwF2&yrJzB0@H)U{G7sACI6SJ=}3X85)'
        b'THb}iYn0y?Uo8FtZ3`ff*R`rG8fqEi$EB}PgHoMsh0@>)wE~Cto{lrZrH#5DQ*li2DFL9JcXkJeK+D@w&HHU^Qb%y=Z;M5T9j%Fi'
        b'COlOPVY}aGhba}lbTgA;V>_b1B-xqRl&tqyaDEkRQ_VmdtC|8M?O>xi98!Ri#?Q%+z1}|-imYx2hg+I&$sNb=*M0!Q!|}GU;wd;c'
        b'kFh^K2Izn{c*+?w?76F48<Fa1WA7XTS)o?r?6HZTz-6KU?-rnOaySe|jxHJNKF061MNuZqq;&N%p@8Z}YpO15JWznT3ktcN$G-1y'
        b'>=n$xvo~MPi*4*@#{d>ipR^$@F=&|ZsAa)2cKur!0oV6s1Qv~ZmQ9th{;o3qa#tBFp?Rg9A@fysQnR^@9SYG4zPQ3ad7Z`!l{~LZ'
        b'A`Ofo8Wi*#qlJJ4s@NY0P1gv`Z`<e{dL~3qLi1Q#lgPlJKuz2;lRlaonN9BnKkGZTF>-p7&~yEITq7tE7<Bj;j;g;t7EE5W4;|)2'
        b'WCeVbLQG)neWBR6dBv|+0A@&5AyHIyjNRFuCx!qz4q_3**@!+J1<nFfTZScf9_fFWNY%F)BF{-SkbzG)-DjNV11^(pH&V~5-k+Ag'
        b'Ze4z{V%^Qf>(;F^`hQ#su>Ww(?0*RFA(0T9HZ&w2u_y`I=}qg~{kTVUO&i`x^yD!}=ny}NMg$ypX!N7Q8gi7nh|Rg`+!>3jwxLZ^'
        b'cno#jM8@{ZV*u+zX+M+NJ`lGL0M@dnc7J5EWg*xPZ6n*1JGLCm9SJ9fc8}0R4f|Xe^ts}+0d?_xUY??!xbal=u`{x6Aw9=(U=nKm'
        b'nWr5uaH3y2gYkhHsb%K4>ogkv+%8i0DkfpSXb-kqs<MsI#;cqGJQMXYS1_%uiOP5Zh_yZTL78f!-1c=_&1$3c2%T5)0$$#-^V{lG'
        b'Dfzz=sanE}P>q~pILNF9r!JCL8{TdYns9@r+aWO>=PZ(;$rf=B27-DJMzHE*;B1#Q<kqq<-QnZVpgRxwut5k;)RQl^Ba`o;_LiWv'
        b'mtVMZ@1cxAMx^;+7xH-9!I2@XD$Do=E!85xJ}%o|##R3+wR%-AzXu4<Dc+0h9(Yrd`FguI`PgH!Cd#%4iOf#6x$bwT%*z}pQ!dQl'
        b'@4)O$S=H<E;IVa&XuKO!R$|KiuX}%d3_RuNX%Ys6<E{=hjQTb^2H@}yGoNTICiP^STNq{WU&kU#CqZ9lBQU(6vehh#DNdYb7RuN='
        b'?WRP69c#y}gY+@p9N^Xp-KUk7NxYZaE|ju2+F=Z3uebANfP$(#<Qt3$W4~@6j)4#O_>7LoN5>NN5<1r9NO2E6rW->Dd{IB9Wr4q6'
        b'FIj6=iIa*WXqgT?vFxRG6_ouM<_|(C$zs21SIrl&|3sf7D=|h6<WJO-*a!eh8_9muo~R<(4|%UJpAEF{7qg$E&(eJziKP3{WD{PR'
        b'>3DsAO>qV(&L&#(aI0N$3@Oec*iYJv^=P2L&DEE#!*rkZw@WrC(fb+iJ<%Th1<4K|M1$~(Y9+y*54w|8UxY_*5V7xsyzE~fBPpIo'
        b'Wd69#95ub7Si}zVSW!Q!%3)9Q&Zz18Ab1Gf#`p2frzDHq5H-CXz?|U0X!9FZ2Cm%k_O+jp(Q`bHPeNekbM0<zN*)D0#M{M(>q;;j'
        b'cN2baJ!5TJq&R7PED-d<b@v<!v;zdt90Xv&gzU8Tpu~&+A~!~}=mg8Q=f;pQy+X4<ALy91?d7<p!`8HykA?pE1#`9zGm761tyM>~'
        b's$E-+38|h>@0?S$dtb#O7FvGAtA`1x!P}nLZ`%wBslkQa`I&-LQ7ZrmO-X9e5%}m1x@U$0;mgk-*+5%JpOXbHQQkkcKPhVx*v_^B'
        b'$X{qw7YG9|$_B}!X1va|PrUpK<GZB6Ko~@^(HqF}p9|s)nh#r?=LPn##gY>7qmt5W=xwDD=h8QdA8mA_CwimA?aJew&aj2)kBc8&'
        b';^aLMb-9m=m(S!qRjt5~(U--`bIj;9lcyxbQnM=se1;POv(_#t7C$<lk4q|n2xBlJ>59bcS{}?YLz-SJPHqi)BKB5XhGeU!^6RUf'
        b'F}u=&zGOfA(_(YB0BIly(jxH3@xUMwDAUz8H4$id9b6Xw9dJ$s!M{!<)t$UM%yyy$oDC&`0Ssk#V}5X0?!W$|%&q+y=(pYn+Mh$J'
        b'{<f9B6EZ$PNOgU8?3#G!CsNxp7`mvzo++loervNA#XE~;1tuj<%`8Y!e~c`@O*mbIGmr4@XhX}i0Fu}qZ{;t9jK@{Bgm!?vfe&Do'
        b'duOz7yh?hbFl-$k7I98eBJ;*$z@vPCHrG3|T~$NbwM)7hyfGNDDi~q6){CrrMI*J!(MDx;quTm{$l9p3wB7;9hBMRUn5>(E3`_V7'
        b'Go;%9v=kvc94fzJyUZ)XfJ_W9&XBIQ$h~Ac=3ay$xfYq1YlHX&=-UXsarE8Kr`Fo9K)`nxkjld&V~X`M?@bJtivhPF`a1e%2NC{V'
        b'RgHHP{W|oUZYAqW6Y(h80`L26CU^2SDEnF)mOTsOy;m`5EIKQmmU#o{i$<T$^G#Kq_Y(Re(GUNw7XC637i&$E5y|~Ydqj9Y{!(Jg'
        b'Pg<G;Oj7F378L9cx6rYSHV#cpk!@*7p()EbbfV*I$dUE|>5G&$2`ukSU?Kqqg%W3o(?zA=Vf}4*BfBsy6QX`ooF()2BRXFr8X02m'
        b'8*Pd6r1;g6-q$hWON>ZM+I%R>`#bap(4W$nX?gWdH}cwN==b_C>aW41|6XodQn+d!i3K-e!S1ARL{&z(0K~pKh`c9+d`5KF9!%%P'
        b'bPds=z<sI#0fzpG58VgOz#cx^t5bEJs$kOor!e7OK4H>-M5e3CcrbtDW7Gd5c6Bi8E<SSgzelDe$yM+2dF{ap$ieM-k;mcpAslEq'
        b'9jm)6qvJrR$vpuXEr)?#t_#Q>l;JTI%NMfza<#QgZLL)EuS%+<Vmkob+y-3``3s5?LvPcS-wAd#b5gL&H;KR%cpm$^F)27{ZW4ma'
        b'Q+5ZOX?&27fF6v_FpK@pU3lBtkJ2(mAIFaj%RjisP-+l}|2*maP3y=(Wk+L!EUwlqBiy(bMLa&~O=wF@BE4E{$0x8IbCyo+31MFU'
        b'eNv>BmNyA?D`Bp=$hd!@<;cX7vf<N1R5#T-(Ay;PY@3`bo;AAoC|)||iI{ZFQJ3Edo$o>2JYV>vOtn@VI5c4z6M@>DFLbR{XFhY('
        b')GsK7Y4lIpKviuLf>Za*9aLX;wg%_oY5YDZla64YZbh#uMzTH%C*IGts$L+BB0>dG+c0Xl6c=znZcNQB@UDaHM`4QW)-lL#3)NNb'
        b'%(X|^8KL2ertFbKhPE=>w1NvJc~FKMH9)T#ZsF(5sz#AB66V|cGVaaLf~cx%G`%}{PTUrp)xyNm_EYS`55kl-{pBCSl(q=-Vd+DW'
        b'BkjtwA1XUKE)JiP$2stDk6ViuC0dqErVUVduAHWfk;Llzq#0V1mcvVK+*-lel}fy~t<f6Dn~cjA-<o=_DJNJD?f3Q2A7ulr|64t@'
        b'ch{rt|EnGsT7Req{qObo$^W4qIsdnMWZhj4sD$S#X>bunnZP|qyf)jkl=EC6AH$stl<j|7f;$;1#oaPmW)}%67T#NEG3mH-hgydt'
        b';KSo9Mtnyw>0I%q?4+0PX%gFnQ~1`*=&e*%?)ot1fOsfu_|aYRWu0OLF%&;IYr(Qw(0tHb(5&{<Pcr>f&M4qc8bpHJG$~(<A1kL5'
        b'^cs|qW^toc=b4OS0C#zITx0pixCWX=5{K5mM8?-WdM6DAfilYbVrvs==?H^4%NV8kq?uu69rEFsxiFY|_B6BB*6-J3+20|J+2>kA'
        b'8%6GE1x@}dE@a$t4!l-fy>;J0^2j_z8s8(YaNe!0IJrI=rfMW$mKCe}bOO)fS>7Xo2Yg6D!5K2}^@OSJPR9DG=7vbsChiRB6AHv*'
        b'oaVJ=wm4K&&Sk_swXDT!hB9qikK*CR-yCJvwfZ9R15ZpO580Ozc9*-7@kJ0!gus0oX7I`*KDBP!gyyB@CSkA+?9(lw_2iH}u82te'
        b'O^f&Et<b-1zv6+~n}e5+;WnqGt-7ZsAZJKvwESCUd^ciSbMO_x)W=%9hE{h0fp8u{I6eWv{<PJzZo=+L_6Y=b-0T?m)r9>#X_v-$'
        b'?{9^<iTA!%Th`ILSGym%y8wW{b1a~}u3!70jA4{2qm-TlarzZPnGpQ643EIWP-<#^OomhcgjTe;TEMBhm)Fe}w3wNYZuT^|JjuKs'
        b'77B9fq~NsN!%Jl*WPcU%Mg;l+w5aef*x4bB7_BG`$|RHa2=I9az>OXT9Uhg1f@UP!ea&{}Syemb6}Bq+)cgU=2IY}PrEN|#uf~xW'
        b'y@~RUx115+nM^5h?oJE7mzPY_q-_>5|7?Lnpob9L;JNr{s5cyOD6P;1-=DB+aQopd0lyI7{b$P=ECL_I1YFo_Ewr#(ut1<YC~6R-'
        b'$7Y;`g6U>{k5YPUPPZ&=6Tx0;vDAyseb&-0psSil8-YbGART0lU|)tD0<=>_p2h3ptZuykx=>*Iq=Sre>>|bAa@{ia-4@;JqTpTv'
        b'nml*5<)7pkvYVu1Eln^)o;w46b-x-0&qK0vZ-*kANY7icbEkM89oIw#8gXwOOQc@)(P?(=N>z=Bx6-L%MQB*+K~2d~;I4n7vJw0i'
        b'B~C`$Gc~P8<2oVp%87O~TUp>=!!{octeDV@9&J}b2VODJj<&LZaf0nUdbiOzD6`nc7Q9+eOPL}BIyGhLAT&ch_RYH(4*7Y&m&PQk'
        b'R!I3rdJYO)t{Yto(L!{f1@|7jeiXR6Nobij0UWJ*mEb#FT%#pz;(HE0a5QA_QVLWngqZb@eAZVWD~W^XPav<b>Qz1~bW+c~Kji(x'
        b'R9+?-w8s#q1#RYSzWAjM{r9$KTeHu*qlLdHBgSU);l)Q|Q%}_J@mpKiY9I3!r*<fubFwrWnyc$5hKXEPi#rhMnU_fc9j5U%S65T{'
        b'wMt0D%)#CBbSxgm+%qy;u>0fY;8i(To<>mcoR6m5x?Dq%!cd^kts}*=2^10QD3^_L{VB>_pf?vO?M0E!q6oGKThJy&?kjLMKO!@W'
        b'uFx~`i&NIE+gh;3XKE!%Pv5q?1e;6tsEVf*AH`|C*`>&BCH;D$IDyQ0gt&R%YBs+`^`5jiiWEOYnETY;)y+-fz!MUuZka>4#ne)L'
        b'fI53n5Zv^>OK6&{++y(A`_!e;dpB>UROvD7{Vn2RkZ+eX3OediQG}r=@=}p9=R>YI8*wjwzL8ykXm0sYb5TYMp14g?6vwP{&e+@b'
        b'_*#1o9$PGprr19oU42DrhG|+#i|UzMD26}bh~h8s^&hj#nma!(@kD;&d!+vYS0rz4*z37Gc1Gq+ZpoqX_)+2wgV{}NgettlfgCBv'
        b'O(}LUp^6!^Yn0;4ToLDMcvIeJ`FzYfvxT=8SSE09D;wQXju+^#s+RIgT#0b6i7?ODTVJdy`o`xL*QhQMx)CgAdP@%feh)jXr5x|F'
        b'WW!tV_!|HJ9{hXS?$}*u`E<3Hx$4vn!n2)%%{vrFwyB>LR@9Q^KJGbbw>U>kj8rJCtkrtTYJJfvq@|HkB5oVr-LRB!7RC9BVgoTS'
        b'y^Ql|V(Zi26??cQ2_0vL&_mzYHL-XlfRq^7r-TgdK1E$!<Pt&%W8b!A4oG8}A+ck&x3_%kWzQXj=8<e9#WiTr*phM-P;*E?7m%VD'
        b'hbl%FYuV3^;<M$_@xZw;G>Hr~!}qgKz3zKcfZsf4$AT%7if0B6-cc?5X~T}HYr1#Fyzd?530N?}o12LAXO!$&gj52!f^-oRyvf4z'
        b'fv|Lr+_ec8){QgvJ||1JJXSFMs9hy46eV3H#aD<xF}^zI?GJ)mKEY?JUo9~v3L0hv&gm^fV+F4_pOJNoAbKfA+Y^=hx6`pG?qz{@'
        b'^cMeEFxHZXu>}XbP*84w6mKPVAM(0qM*~UmR92tu=gs^Rka4d3t?tYX?%8q1q8Ny|q)~cHd?Qv$J)|@$^+y^Ny^ZRf|L8r5CsFL0'
        b'$V-}t(RSs|53R$BBVFnvN8VHaL1}$aZ7<N%aaLRA5&p2C@9^&-V>QU}N@#bhk8=H4<m!af)Xpxp$ak*l=t!rs*P%G#P@kWL%<hY&'
        b'9+LtxZQ(1NACb<P($!x^L2!R8<v#qkUO#nY7?0!k7OHc<jJ6f{+=su$J`+Q^PAaU=Q@v2oqv|$@TI$>VsxKH-4N(<TJ|AV*#N=1s'
        b'7>-dLq`jcD6f^@BY*{F`E@@(H%a20Is%e7yFQ@wi8=9n+PsfoimFlX4AmZ{{)PcW_gU_fX_P#(2KK)yxP@Hag8d-479iNr}0s@m='
        b'`1_CYS5U6%t*WO*M%NO_mx{sPMifT6j!^meqSbK{qw8^g$Nq9p^p{ZpYVheuqgLSZQuzhJ=uN@smZUEu3WbADV_qkfZxpSb36a0%'
        b'Bi&hIql;jfX7FL->acM)21x%#!YQPdOACdjQ_<EJKq47kJM&j6;up|0`MdCVyhFIRgraBUUM2HaD|%m077CyEu6mWix=NiaT_enQ'
        b'DCilVWbD=ggZv2U1#AE{a=Es;3d@eXpag93GB`fDaXn!dQuHeoE!1$7F^ejo5Qo*kV9N=kP~;F+J-s{n=spK2&LKibT%>FB>-H2x'
        b'9Cc=i@(UHtlfAT*o>5&`W<@;Qf96~~<TXOOMqy-$>KDrFMGCu6^nD?sJfVr2mic3!fx2SaI%9W~*DzbBdY%B<2UmRagazLoxv*g&'
        b'E5$ySdCF^`M5Zq?Xo?NT0JAPFNkx{&322$^pI)Bp6>gTO4-?tGM6YVAfYB+u0xx^Qi)NDXBaAju#So$OpCW<Joj6}C;&gMdbAsgi'
        b'xLKUU0m;R5eD$hcIxK(xp6dLqVk@ZrhkJmSQx!6mT#?s0vnUXCg+lw`9_uQ_8X<V(tDsWlelAaF{4<xItym%i4^gp!$@CsEMD3Mq'
        b'Aj^*s>>$dXOmQ<EXGkFM#dHcW$`kI}pk({_xQkvl6%|<a4IjL5!-JWX-iB;T`Ixt(nU^0@6aft@buWx%?)8CKpy)XPF@_bY+&ZDB'
        b'3`GUyc99+tA1E}tj%1$nt}YiDsVgdxboXmVHgDbvED@9$w&#6bPxF&9=o7ZBUjBKRg5NbmPmye#zPW%}{=lOP^WWN2u)W!xCtSUe'
        b'E}d=Pwo$x%b?L)I+$tD*CB@?98+lK3v1IuL^TUMkq`*vFscJ0|Zo4dbG$$0|BESJ<pz&KvL|dYDS>F^`eBH7pQQ-A)_64kY6JF0y'
        b'A}lCtUM)^7*l@%=Lw2aVXqlJ&MKg|^Dr(;ql3mjryf@nn-eS3Xh77kuZ5`ulDzPXE9`b@9FpB;(JcG?|=0lS##w`oHw)`VT32ka2'
        b'%=(goC!mA}jjritNq%2m^E!)SwTkRp<nwN92D+gL_!q87LT@p~oQt+Zx+VFR-;8+|`fz_OsT&>V;ig+u1q+WDMKQ&?a3dvS=Ql%{'
        b'^P7V;+-8|!NXU05h&-Fdyhgs^JpTyh%lvtBuILfBCPMf4nD-GrDsXL_Z|&Tz_g_-#jT)s{6S?z?#XnQzXRAj|%AFV1Wh?BO2=Fal'
        b'{GPf{36A6!fW?YWh}exje(iv`wc*E^gxBa2xT)u9%JuM`CMsYa^Ue<z@I|nIwl7G30+)I7h&v(jvW)a=xJ23go^@m1xqLFqB}|qR'
        b'&ozm<DcybFjJ%+9_9-fN9hAnc3LFsE-+x*Ba}Ez9`0sG6rdfQ0L%D?ubu+olTZe(m_dx+FybR)zZyu59z7yG!yys$@Bc&<AaKbyY'
        b'nGoF57t<`HsNFHm&k*-&<plpusm`F!FQM~R=I)Kl3#)%wRjMzbDO&YUYV+ki&rSPmTJxo8#I_%$Ln^brAa5ltc}cQ_-Xd+Lqt-pY'
        b'C-M<OxQsX$X3quYslQC-+?q5)$4~UK{v$9(mtUX679AMhJ>i2EEe#{K#ZKGYn6hqTifi#!^AfyBe9J9gx3u3?v$<XkX>CF;Z`h7i'
        b'T^xhJZfTRm)_oXveTw~;IZ*z-6#B1B2JIHfg()fbRXE9<WFjf!-eLnO)(|(1VTnv}V%q<p{vWTei1=Onc1TjLCW?)J*Zlb~b6${U'
        b'c))*)v%4>2cmiaNNgk?5`^%!3r1q!n?$;`u1DZDurx}ixe+7xIB76-|k@k$;{bhx-L31Do;xOL9qNxjdV*H<Tnteg{O#cX{c{%8g'
        b'^MA@|b_d;y{1-XRAA;^T{2y?d7lZD2|9hOxad?j2&hDsW(hP+EET?%s7<b5jhSU5%zP<&lsVi&rymAQPsCi)IWt($CAfR@Vpe0&6'
        b'Ljne*b_P%*I_>{M6a;JgTWi&}%$?-eLa=x%p{;;`C&5Snqd=`yD;>m^Qisl{ZKti%POX;K+S)o!>jNL>u6+V_?)~q*-`C>KeyqLr'
        b'-fOSD);fEy<%y)jLnlP`e?-#zhTfHY*VXOkIph2yt#w@g^laQOWGMMha7$i-r2l~4@Z^4z=_gCE!kLZNFYB>{k*|9`9tCwoiRIKp'
        b'z15L=|3LK~?lI5r`G3@VbU#B_ieJ4OmvcG%X5viz7EAPdl7m=xhR(9^y@~Qu^LiLL|L|eY@AmsX!OulMc=UfVF-(5XPTds{V^8Qd'
        b')+NVub^J#XTeP2)r;fXI!X{w}S=gWaJx#jp+c)%2;fK%GCHfvdJfREC-(S~mi95v!il~)Ji!enR@q-M39*SL$_+?@jz*G^uT0XyM'
        b'bwy(Rug0-#P+C>~vi*G8A`pH|UL9Y#D58JWr%sGxz>51zd;X6ak$&&l4?XqC=k;u-v}u@6nBpgTeEElRADh%CpI&txBsKJgIRDVZ'
        b'oe}l^s*A8-JTcF-or*X=I$CL}r>f3eo^Xa_vQRz{y)w|lWYn8|UfB)Ntlb|V=2`UPp72RYnO*w<ti@fMo#*Dhx~F`RIjDriX5vl0'
        b'Er8wGxhkK0UeytyNoks^v*gX2@HPD7zVY!1Ruv2mj@AD*zWT2x>THKOi0%8o%>n2iHH!(8JGuVv`+T3`{KBkhAdzRIN(-~bX{7$c'
        b'2{@OfzN*gr8yG0>9oYx+O1!CYi@Os)cC*(vW6?k)jL2h)YBYq&LqU%D<9+MAxGCac_OV6GxR0g!{t4J8Be0+S-(mY--)C}D$SYO)'
        b'qO~_8570q&hDqPvH15K;{)=9i^^y#He9G4>n!tO{zN+hi_){jY37UY=eOKZJ^=SDizzbIRatJ>bg~)>;1|((mSoc0t0IHgLy6{Mj'
        b'DTDIA+uM_25;E}rZ30mr+a~Z|7g>j}_}|yz`H4C`<7@TBf3NeLG|rHUk8hU73H|o%6HR`~-KC2B<d--5x4=wiuAJPL&To27KA64`'
        b'6tsaC8`d2{%?5!NND2c~WaPOkCqb>%&qYBkCJ`zX98w)?-4FFlbErr?<Oewe0XIo)Ea?s=CLA+Po`~Kn_VFCg?%%Hi>DMw+%ogpN'
        b'+b8+GgtF3o0VoUY*L6YJts_;}d-M01B-KXOsA6^d`5B9#8QZ%bZHjsd(r24+wxBn%N8snl3>@|Q*rLcIJ+uer?K_DAG|!gy|Ma`I'
        b'A<yi8&%ftxK0mngkxy$5EBU=&Y~^bX%lZA8Zr)upSLyNWcXI)q-gcH(r5i7Es`0qM{;dV%SdIFDRBJTvUs9t^L7@0RVvYJiKH#tM'
        b'{m5GOM}iu%)AnKRi+s@|$b5&fvHL8pxfYk1{+Gz6PgI#4sZug@No12JGNU7zrPUY4-?u-|TR*p#E2h$xH^q(59iwTv5{Y%NZC~Vt'
        b'C3;S~8Kt|pEN&o%)0sA)XQ#;C^>f%l#FcBNfNuOgkwluhl+JW4V2`t?W9;oGEXU6Qo6kHTvj}=iQB2{@@Jw>Ofj4C;M>LkA|0HEm'
        b'8X_+en~AjN*-zuv*Im@~xp<|@sgJH$f6z%d=3+eeu=_CzIKk>o@_=EX1sM63h7zyRtlIBVH-mm?Dp$Izb$n4Xs#!@f@=cqf)*BWw'
        b'Q`f!F;8Qn4)uOOi(4<@ko2wSpE28eHP!-&-wB+1lA>Om^{~{|xX|ca&9_z8Ii;FZ^)xWY9=<G$scJ=at3==9WS}yH`2MNaERmGIA'
        b'{=}gnll7#*i|g2QOn#>KVh?E}vjSrp8{zpWEM0&jrGS_ZX>ejAHqCRcC#!cX^3WJv-1-jH39K|&j-PcN9CN%aGWS=mH{agp;ue|8'
        b'buQPU>SLnh$6!NBoW5l<V<|UIVL#|$;&?m8Hikh6h|n2(Vjpi;R9_d-gVWauPEh5p`I>!uA50fLekau=Y#4olns2Xb_SA+MLZZ^c'
        b'<MwwBw9&VExI%P?&tk*NJ^~1{>zdg=hIt(0?fnyWbcXOBK-Kzjs5N?;m~Yq4!vi?ZK8-43U3%Vr)bMBGmp$PLv+wP*8+l!hk`qYh'
        b'Zk#vH<pkWFyhZ2UQ1{8z#W8Goc<%bLFX>s-^vjHez9ZS8=i-K|GEYgkFMz>mL*iIZlXCv=M-C^w_=cKE+WCfB-zQ*F00}|(si#Y|'
        b'wV6M0*8PGl(Yw(rBNr-s@0}gGD*j)~qEXr1_hh+YAk3oV3fA3YS#ru$Lg@_3!X^8(f1~;23fKN??&oF5?VfC2NyHPzf_X*ze=Gn>'
        b'SaPaxLysl))C#VpC~Bo<$9ZL6vN|Bd8GaJ`l2u8~LD+-#Ff-M{#WRGdXv>2#=!K6xRZuL0=15)ig3O{aS#<ykMjnR*m?fuN3m!CV'
        b'5G}HKt|h0c4wgVi3+5p&*f1x^55!lp;8(IT=|4|g80Li`$h^D=->|A@22vXoY;u_6c-?)-pVILUeS#dOyJl{T;Y(TI#LSKi^g2za'
        b'qtIg&Xmcz+9434-9h@-d=-hfL49xwq#HCN~zkPCoOZUwLHm)+6ku_-hzj5N=`sj)C(KD+D7=<qm<M)f(y{39H4BbQwK<K!$Dm|C>'
        b'T8ftk|0{a@4))Ex$XA2|q{w1f@7H^)&iN9Xp>tj2;Qf6wm&|WkuL6!d2oggRGBKgq|9$i7^|3tEv`}2PSdxJ(&S(aI-#l6w4HUs8'
        b'J9@gMs87gKGCHsRx)+kXfFnr}j_nCav2xL9;_cCBdg5H$1|*x>NL1g8dF4L;qbLmfuQ8wh_dBdabr_quux4)MOiiYha5Q4&hX_Xl'
        b'mPFQM%q#a2^z#_Q*H~i8D^QF=hM=cl7~=y_sNh^`<M-^qUNfx7X(FJOS6wl2CV^8{$6-m9)VO6e7Ai?iUlsY`a}06SNDOU}>=Zts'
        b'Yeyq7RD;#beQ5q^1gilwfrObZNILx3%qyvluNdBzG3u-NdWQ*Fi07YY)R}REi`1!c1pN<@ZQsjrxr~NU=-L}*DUc_@Z;=l&{}MFD'
        b'ZCFhoL9c~5I*=L%)bSQHlBEB=5tk*7e<1%tfrK4#O=uowz&v~j_*8ENd>-NawFt&0KxhW%-;C0qiJaeyVEjomyoAUrwHZYi3JCb<'
        b'T0+oM)r(PhdH+^a_i0GHi0U2?%jyV5eK4J<{#ayCTn+TyGZ2M3+6Wy@xA@Ox!f>C2246vg>X67j0SG>?OQGn4A{U4Qa6?aFTp%8e'
        b'*)Ou?P`YMlodo7jJ0dvFeZUvkh0<#wt>XfT2!|!mXe+{@L1dTj1@VAuM@|rjav<N2rZ@`{M}d7<0^ihRBv=Ap!@^gWV3xqiOlbA0'
        b'$S#7e_-YsAd|UGx;qZx`+`arKgik(w$c{om<?QA4My>I@^cqMIHZU4N-%#xp*$4MB3TT?SUS{|`A?&7RDd;U|;9<hBf)LWE>OV@Z'
        b'yJjQ!I=yV@IZ&&E#e~37^fRFM-6!SiWK4p<nW{I4p0vHZ(Wq_wEFfJ6hn_GpOVHJ$z=4m8n1_>!LuVwbGQuNHFg8?|i)`ZFh?W9W'
        b'Q$aXfA}fOoJV0bsT>;4G)hnw(RX8Gni32JMHB<vUCSmk<ux6QSi0Y*xtB{Z}P}M~U=d%9-(UBn#{FRbhDRQsR_#6|r-PnMxj$j_K'
        b'+h<%#-xNK!Ai?W+-LlFU!&(Bi=GAlpe!2nYEa>;=ZjM`}W2vF}qUQ=!jn{VmMVi~Vq3=Y`rEV#mDBbP%T!ixHw4EcI5%D{RDRRzP'
        b'1Vg5epv_on#)F`p4;er^pPIrwQ*I%K?!_3gtX^hHS4ulSNuMbx=}Awae_2r0zhDQuk+MrX;P_cYOYcLmXi_s0W)3rCjb(7YCiS&V'
        b'mcXt|-|Ot5ZVPds`a7t00X5fSnXs?!MO2aL+rjok;OuvRk{*tv;~b!*cSX|i4p7oNBI!g2DCxT+>G=*&(*2S2ZpVir+ZIVDIZlb@'
        b'o!#kri~reqoQ1$fpO*nM8~QWM*{hK%d#i^<wjq)ZSHB~&+au|H)q}|A`uyP<n3nTc>LH?f4whtvUqf$Vsn*5ifc#!yl8RL8v~r%P'
        b'-h(kOroKryYOrz_LBA@=*$lEs3<aUOlKG^@_Z|BTtkWVOG{<$ZypM2nU`cT`z7N@_x;gc7$G^n#LBjC@z|^H$f5i(^k<DYD#CJlF'
        b'sYQq!#E^+3z?LH<Ib!$dCYdf>i9T4(M5dFW*P*Z2nZ-3~g8o8eAC1&X0&auN^rH6d*vv*KL^cg)q%h0zk;wbMM18%9MoC*hmR^cr'
        b'^#QC$=3ht6_CRv#{0q?1@t(-$N~6$IL&zU?`Dwxt#1_S&vO$r}>PB*;k#cuZC%aT2o(r7Ly_-URyQzULmHP#h?(wRIiZSR&LV6cK'
        b'pUL}I0Ep^dk^NOSlg@LC-1VdG`zY9bok}-40CY?~D9YP89o-2CyOFJ@4j{aU#=2W%x$b`0i$_Oi5*&IFt*_oCVtimX8rOD!pUeA4'
        b'QC~HXPUQVxp}v4A#db3ZXfVG5tV}~b^o=kOh3dH>k$}duO=M#tGj)$+P%7_7FkeIy%?FMmIM0hLAx%lDjOIl?@F#?u7iykFxcxz7'
        b'Z+1xl4p%=5ba%arC*EU_Gqa(M;^jsa!?``SB!v)C>e7_|HcXHh-0%yymacj&w7b~F5pnby(eq7L{f#cp_^>Yx*c!Fz8ATwjdG#8K'
        b'Nr#%NZxD`Bk&kQcxIobVDKdEgf__wF&qOdtpjU|O$6cKI)uClb_xYwPa>lZ!A+J~nC|UVFUX4{<ff=VOMfQE@bC`Zu^qlCb|7@a9'
        b'mfCcK7|KPxY`Q>HFAy1H^{B`Wb^)7429yUGwL5)F^=|;@{;r5g1%~?xK|dh6IU5X*Qv$ADW%auvd!UQseyihT^lZ`7+Z8bWmWw+j'
        b'w9D3BN2J1`>CowZ8k&i4?dn2PoI*L$fCWftmU5&33+O_`k_x)C49M+lmqc;TQ$qvLf2&l_Ksk~`wz<o=-jN`(jZ$73<(MY2ufVVs'
        b'^i+}cMdoLE^+J(-Nve=6qo;^$T^FLN{_0B6v$d=KLN}nt8y7JNx>Ra=qmqdMs$tT%cQ-(v{x7<jg|Ldk&IU-r0>TiPt?naRw#A@$'
        b'*zB_so@oe4w^v3tp)oxT{r`jhdE7?o-xE%%V`4llUE^*g?)PAfJmjjyk!qVz@X)b-e6Fo5?goidBP$rA^oUJ^;~4(fMobY}f9oP6'
        b'N1^F3ULD88164)btd3kamv=Gok{_iRSnYAG_4fQc8u{Zemvk|C6He#fa(o9e1?q#eQ5=ZPD%4ME!mCmbP{CjQ&+$9%FNDoo!pulN'
        b'6(&7=w{*{?uFFdm$L1y1lFKy<^@WZu+aJP@F#R%ghwd3v<w2-|GQyN+HX5G^Xgii6b+e`D6BGADoG!9#vS^O$Mutoc)lrdJw&B{|'
        b'gvc*nx41oG;#^EIM@FBLnG3rD!X%5HM0Y$~VJlge5hi}|4`I?#N6#_W=i4)__tz(MRrT@6?5RTr7o~}%bY5N6852h#Cgnv@hfEpN'
        b'+AC0u{NW%Q*?W?2aHh+*f7l{_Z+ixEatLB@-h0(IB0jwx;a;lCC&yYUNjXJ6ltRi$@}YZ3IYB<8CFMBz&}4qbqWTBJ$kO=OB2P@0'
        b'&-g^$d(3p+`1GLvZ503Y?wt|#N~g)R!D1gyJujJW(ZhwZ5q#OjfAYkzW&ceRa(Fll8V3qihwd|8?+g?6j|h9L+-G>mG+Sv)2z$Ql'
        b'w8vtm**b>GjhEYvGqbWyS-F&@xVWraZkQ(1F2O8@hkmgEc|PitLQ+o$0myBt=Y`EC6IG+mNwunYVO5P<&kIk~sM8{PDKGFfY8fvG'
        b'HNH#iq_DH$4m%}0bX`R04{o!v@X*g98y$9PZnI=~=n6<jVdvsoEFK265zbN1kxr#wXQ^0aDJ3nX#9Y-}Jb3@LU*4sLiQw5g0zbg7'
        b'L{Cow?SGVffO#MvwB}NZ6Zqh55z%8aLH`cxuq1NA6ObNy5G3-=kf{C*@)n$$uyB46a+`kuW&IvQayrP>C6MS!Z9dO-cXFIj8@LS='
        b'4&ohw8F3Ks5Y!d#&fv`Tojsf?T~FGvp%f&2vzWQAv&XK=+Tzy88OeRwQ-uwk1qLZ32evvA>HtNzf438PrI|P8sq6|28i5COg&NZV'
        b'E|zw}#HC}t=B9MtU@W>f+Ng=f{~R!>(z!t$)H};T)pVnm(=5ar6<FK})Iybx8hM(bT`lKZgXL$C*^J@Rjozob{Lgfi&6a`2G$b1F'
        b'9*c@y)j5wN?USm<M04X_BOY;<W)}9IwX5<oAPFNPvvKo^PBgB`Lul7G;^t+YJquO&*&1p}2{tATEW`Fd7q=UIFyvz?CLeYKN-m+Q'
        b'&hb<M7N4c#JW{~20yNy;cS$xH3Q&Lv1MH?4s_qPZDw=JboaWSya|AFvBR+#0pH9htr+MB)*{lCvhSMXGp3V=pJo0Urs5zX-?>&nw'
        b'ej3S&M^u|J&y3E1ajruPOVW>*eJ&zOOxV<6O+e(CkPBoByb%#>!VLe6&dBW_UN}&bP{|8#)g(O43tctMUwQHR_|6$#kUX~5hU7y8'
        b'=EZv&Ri4<+W^ZU15nJT968-)JL~bwMTf7(LFevAO=eKBy>7T_&H5xKWIhsA7fa)J1x1P8Q-3Xi%z}MdnP2|K4eJ!S1XC!%R)GJc0'
        b'G0vi&Jy$~kV;=pbm<00J?~)E7q3o}s=Q8B3sz(0Kc>mTKwJp`E=KW4I55uD8+fe9`bhk({YtBVxO-bnToDT)!9&yl^=Syg=2I<!G'
        b'4@ju0kxydJXHZyzDbDm>=|qnIkjqrh$B<Vl9TgGZH%Cu<`4p?{YM!w?E;B@U146rdZ=;2y%AZ31UJq^|hVH@2SEAUG=&>pC5SCK>'
        b'w}ZtoDHZaR&F@FvQ}Y~^vbo@@H{QZUrxf3Ru)-KB8r^rNUlAe=_1Cv4KxbzfGUM*cwBDQ2$S|*EHVzqm0X0VB82n3M!L8SUhlEJ_'
        b'wrCy*dB(ae<l(6EyS=`lZ^V=>GZ<g0hN%8RM9YBQI!F9Kg^ExFq|hA_$E0Vn(%mhL?FoUn73DhZxzO$SM2dCzW2e@I1B&Gp$^a)X'
        b'o19*EBt#ekUF}kgg6Wryz7Ro2`~b54kcE4~`I_WZHFyVh+awILa8IERcO+&PrU~<Oxy@hNUI=mAMrJy&^8QKE^SN1yVBn7S^esCD'
        b'$9Lw-?~L>Ihe0L8MtJMXT8+%QTYH?cJ`VzsW<gObl{(dN`32Pq?^$o;k99Ub{QcI9#|dUyK#vu@BbKD-u5Q(MHFXyZWcsYAx@V1g'
        b'Dd@v2x#jps-BRcJ+o%&QFIr;ddlxq@0o9P9V=_+aRq1KP>RGhO*q~dl11JTMNL4zyJKA?{6;b%nsRJ*lxZ%s*ScXpbt`~5lF=pw5'
        b'bX~wIH=?*u57N3!IGOq3%XJH!nma?IqBi>m=uB2(A+c~JqptokA`7s-?#NlPy_+}6C(g4kF>^uaVS?8`!3p?LFP!;rgrICu9z%3k'
        b'(-*Dn6T~p?afQZTC~?sKUbMeB{nO0!MQcIkYJX$g?N&rC=qC?ys#BZ0k8SSm-Q4YeraK~3c<v9uk=nBSWI&akev(rK+Ed_cMIgEY'
        b'znra7ybIN-itb~NclSQt?XT?iRHD}PsUbe?38xk3C1(MAHr7uXZitKm(ZfkzmF_+1RrR%}_|i5akVg)M$+OXzbL=)9iRS`vnc>t!'
        b's#D9mk1g-+UEb|q-0fK`;gufZjZ^C?`pL*6Zx8beo?Vx_R2)JwiRmW;XNX_kt>1;Wp!-;EcW-XD|2N&9-$?LobwK;iI+Gamgv1kz'
        b'CJs(UGI(tqTcG)qeX8^~FTbhcjT;f{zP}UFy;kSN+Y!0#OH7(~hD5ifNd&=S!^~fIBt2)*ZwMg!<_4f{oryAKZP30=7yhNA*VqlT'
        b'T@ciHhC2`vcsHZq<1l_{anO$Q1`CSx=b?PEVGy5?kNh*BxLlS#6F|KM!(~}gr6A?z|E<yypz`rplnaIniSFVT&dRW9t{6rZmL)C?'
        b'PP<$l{5jR7RQBosC&O705==ty3o+9r_shD`>)|tE-P^X)9sXd4J^9`$>8|-dyYg1;-K|TeK!)Ne>`}tKxS?ff@$R~*$n(mEx?mrA'
        b'S=rIkQ-WM(ta845dvwQ-5xU*e5hh@6N1B+eqnE~KQ<_4Ut#<S{*m>lRBy%DEnPtv9e?WmJTNT3KKwUCJq*0(c!ETiosi|ewabJuY'
        b'>~gVc>(aAJ;ZMi{|E%abq<EvL()lmSYnl1p3U4TGNAo@P{tjQ-?3U#rc|TLjB0t`2-Bw_hR?j17aq6fv%4k`^eYTz<iihgn2}c3y'
        b'k1B*61C0Duenq*n`VK7nz)>AvO883g_wcfzH00Z17<X>Hk?5uWF7`*)vQRSmwv_+9BGJ2EOKm!I@8!*^t((qnf<K}A;h%L~Zoux9'
        b'v(6808Sj6V8_D^Dtoj=ftE3P&l+K3=^~`scy_(O+9+y=ECoFhfa;5mEH0`s5XI+QOIJ-p~BKnc*7-;|&&rCFc_bCweku?6eqHay%'
        b'(z3Nw$DHG{BF5uBbzG6Kx!_Hu_BkTr+meYH{Z?e?)d`;&@zv^&jeV=trvU;A7Vx-2BH;Ha3EKFZsP{>9n?3loI4&oef7_8}v*=l;'
        b'9uKe-5DkcnLcVTfj3FEZ7P3LhSqg1B%$d=~Xo?0~u&G(tV*m0&D_*>K<RdF?T{#zblA=R$uDV_$x8fC4@#2`wlUr0<Uucvw#Oip$'
        b'k&GcZ<JHM*T!<&8bF2)s1$Sn{$){A$E;UZoa#8DJ(ZH5PRnET|COmZ=6OV_yHYTB@Vjy)j6?$7}pDpYeOza9KUjGC7IJmAudbAUc'
        b'@;rf3^^3Z?4u+x=-z<HotK-eg5Y0sU^08&U1x8x(tM)fkDe-mmiSYxJtb2-)F<PB-%g6$)>tFP{;vY!*q=<#+!_iHpo(GVq)=4*('
        b'I`eOKM$<oux_1T=NBRlR{iwikQHsOLb}{nP(Rf(?@w_P`MsMYaq*}Jhk)CrXe&B@a#GAv3iCwypfq@sdMBX33UbrPbOw3XoO}C_z'
        b'&f_w#I%V@ySG_Y*@}9X`9Ajp>4jL!HF@Y@m>XZtrS>DCSj2TW&VO{B542mWl4JEH33w%;d#^iGE=j`!4$Tm8QswS|M&{XC;933Dc'
        b'Nb~}$r#*24#47g49wru<>5<}S(ru`|CbF+f?NU*gaJFxcg)^eV^<9wf$-8Fcp-bXr#Ck#E_GU=`bcMVLxp9g_4)n?z%a<U$_RGqA'
        b'Y1$KahE4%?)i=ZmUsHyEPWT8n+L^;lT<Tn<=Rzk&WVv<q6X8J^wa#dgzUgLVZ2%TcEK~(Q68Cl$ubBDguxzxA?1WP}56^uy(W`37'
        b'vz_Ujd7N?dlVO?XlTJx}c6LQizijHEoNr36C{BsmbljUC<GpH)*}Ni5BNw^}Q6rTmvn{clz9i0kJGTjs=}O!L3Rq&!AO*6|z*`MH'
        b'Jsax&+&A*!Hbu|>Y;gB%aL%~XvUlC?fs}bu;ROD852BkBSqF51cS+Bis9*mZor4Mty@OH^gSl8=E*{7wd=%zfe#4hb4xJYtj$-Zs'
        b'X7E0ZBItN7BM8nFKL_j>qA-a!JW3et1>{)ydSb|dUFA&&T|~7FeMuTTCht4OgsC+1D0zLB;`@2t1u51?ujbwBjH9gVL4E9e`w$5*'
        b'%6a6Rf*-uf5C@HDwNr}a2aEIg;j34Tml-ltHW#<EL}v4ELQgxNrNcmR=m}21AnOxm8fr<qfTR0IyZx}s$8$$(NDE7JWb`2yyx3?m'
        b'6>;8$EE|TK*PJJAT2+|`dibevjK=M;Mea3>R50;bwGCSDjrsYgnFS31v5~p>=(TH^&0ec2Hv>tZj%y;!<@0+ai$?j@cvibdk~Ee6'
        b'-*&>(dOA@FW6|dS3nNct^^ApO!Si?M(;^0~Hli|2al&y!9G^QlK+I_@o7d5ghh=H1vOe))#mI^IMdeRFz|QZqE$-w>QE01_!TY#m'
        b's@!!S;DjcXG+e)SG{29<O~;WFi{Ljvp?fcml-W;=Fe|h4Tc%%5%s|0BxxpI;Eg!#l4BD95b!FdO(>C8SK7WvVo8cT+Mep+|R{7OD'
        b'LrNSml#Dgzcwa8BMDZgIR?<v!Ke^)weu$MEcQ~w)y#Lw3;>S}e)}(Cy!0_o0z%aLH^=M;S@j_MSvWBR_OTi+;z004n=%cj9uLVE9'
        b'(<k8OpF_@ctdGPPSy48sc_;|QJv|iiGXhPinM-mTP=J`+*9h2mmg65DTuD^_RU9q6O8*6PsGO9FtgD+R7r$&}Q}S#Fi*x77=(A!<'
        b'<8PQ?&74@~1>_rTL=3&$PkLTLlRNZ@2zo^v0bJ1faxq)97;}6GDH6xYY^?f}Xfn;VEWjLpjg)3%L!f*fQb~i<ZoM)~G1McP1Hqz?'
        b'aEo3akR>sR$X`{r<h%8sp+^Z=Ls?|yVK<N{)zzNZ#S1GLO~)aeA%P)vSmP}eR@cz`bqH!dhU!Q*uZler@+h2D?LkgI+gXIM{|Ip_'
        b'XB$_3W@kSOr9G9lh5dUdtpWXMM}J<k{V|BVVkSo!`mgmX{2zxrOA(mSIU-vgbZ(tgl>9{9(qcXHEQkh4W22?wsO=_tMqO5PGx*LO'
        b'p@a&)^+Oqd+wjtDl2{eSNgGMp2+{@#Z1kS1!FORZOAg!rgfWV;Ahu&ooX|^w2+1UY)CNql=crD2Q<tOwx-8^F>pvv=reak;_bfH_'
        b'O_L7_c+cy~fG|1OBNinawWFBiz)tAdz$7tS%l3<XQ3;S53+{vB_>tH9_K8eVPtQ+DYl30X^L(hdLi;+|_=+|S1JS4P>AL0pwB%c}'
        b'xQxCbmd&|YcKA+_{$8O67|-J|QtSeUcJzvLiAjdhpxN@te35{=SIgYhGLR`Rm#f_6x`J}#$?AO>v&PUN_S5gnlI8{Xh_2JPkIvdA'
        b'i>j3I)8y_gRA2J*AgK1dMxl5ly7_0yc8m3%P~r7GOlFg9^h>hQ*6{{0G!t8&ypVaIWwkw-&)Ou*a>%g6ENqj1AV-yztLr(Sv#Xoe'
        b'@Bd<5j?!M#%p@&J7~LiIaf_Z@v1i?LN@uPtkKp%X^=m^}UgeHBhi6SFE6<i|{ew-pha{F2#3D<LhA=aUSk^_7m}@V31ciEj;{(_p'
        b'8?i-9tle?gPGC<y67tLqt;^9ZB#bDGMu0v%x`5#H_u4W-+^Q(M-p1-fb{EDj1zNIghqJN+<js&GaT9u(z7Tt^srrOy*WXLp$9;wp'
        b'PcD=Y$@HV=PLdrnH^f9E?_7D2@Bg+1p<~%0CI;DV2ZPAJ;cr4H$Xqsdbc{W-JHVmWK!y8*k1LP|7}*bzjMdF5WHK_SoL<R{WKe61'
        b'afU!agi&~(Y|L{qIKBr^F^Rd|8=S*8IZo-{6YLA1+x>LJwrM-IJCOVwde@p9GLpKk0ZuS?^!;Zfk4*}7k_aFn*^7CKtqUS}1P$<R'
        b'H6lFKl+a0if6=h{NAsy5ufQziOp_Nm4QL5@><EXHBa>3js76k}(LRJDbCEHSqW&kc0XS|?+}Wf<mb{7geq@N7c>Cugba31;^2|z='
        b'#YLN6+U*nYyO#ByMio!!B3A&>%?rCunoq!qBq$9bGe5sui75*7$bN`2?Pz8+1Vs|`Mr^JUdu${207FJfEJcL*kGlhUG-fLi0nuqO'
        b'9!F;infC$AR=?tI&=dSI$-nlXn(%+x0m9u<G|Ibvn7x6AET0vl+fPf3eaBYr?i0{MVRRcE&di7tXZsQ-l8qy0It<V}D+mNCg?yc{'
        b'Q7J>+I}oxYO=%o7rb_7JqIki=JBcj+m<Fb(dUqs#uaX$U3@1E?I&@gN`Hw*jj-eQ`x{FXvr~Apx2i(uwF!>1`rhtKXo<XgOQ#zf_'
        b'AXb>YJ77Sg?M#`7Z650IK2>+YXT(yQNaIsd?01m<X99=w96%%Nd`i3KPMQL#XA<7j*m8V+vS}T)diJlFsnE9)Vb8XV=Be|Nv$Cj7'
        b'vBc0LSl(b(?^u|yo<<Jd6cZl|Y}-1Dsby-)Sr(H<`D;3u7~qv2eNeJ=62my4dx`oScob-f^9_*I@%qj{EYUkXh$WnX(RmzbEQMd}'
        b'hN1$)Sf@(5urJLVMHR|+YbaU7a9nzJH;RROKju{z8w*OPO|QyL^;AJ2wJe@1lFNZWs=h8+s$92JSCl6&4rC3C0V0x<RP;icC_RNh'
        b'>0xY2g$_j(PsEgC%v8q|5Xqrp@Ouy;pqlo~k3;Xn35v$5u@PaS__P$dSpw5X69E<vK7UPv6OSq|e9YN3M&elM`F4bE4i!jw4%)y{'
        b'KzZkED0l3I8UFvl8vWy4SlW3v?;<FLt{xito0u0E#-%Y(7`<D1zZ?_rzgVUhb*2rRAZnk*nHa-oMl3@wWDEe)NHC>0=yWBp!^iDO'
        b'wv-Nx(}$>|&sr7MhNBvHk^bx))rySE8Stl2*Krd4o0*VcNs!l^pKNYxC&}4leiTV&koj_C$NQ_ukd{?gW<VDC=wOcRu#oWc@>!Qk'
        b'cfT9p6i)8YWw_C8)H!Y|sa<*7#&lSys=9w!C=(!-s)@2BYwI+Ij33kQhwAAWP<7rMP!(&wnfxT*PDafpv!lqU3^H5p?$e)rKy@S|'
        b'y&5VW$$+ya-3zrJ$~ftTCR>+svLz$DG3c}_7&W(GNk6%0B#e8WXoqQia$P$!m5YjF$QVvHXUi<oYF_)ZX*Olzlok~|z^Mu{lsdhx'
        b'(AUlt(wyPfP9lm?d(Q3Qa;l88YY%A8(H6>B#q0D+E6e2=zt4bHNp#6dWur~IM`nz#I%p(7$vSIMag?!yQ<^v(R9iFx5~$o>ihCYL'
        b'NLUQNVbt1{mtbqq2Smgp;NV%XM4SFS3dM+p@kn6T72i3|ikz@2Z8m*Qv_$JRt!%SQD-BF5VUqf3;b?<tZNtEu%7OcpDAHGkzlYPA'
        b'EILb$(RuOu&}Wf7t0AI+-C+1bpg5tp*7w4mP0$bur7|5hl_AYgpcpH*W5UH1U3G8gahA8m+#?EM&QmmwS&K5~{RI5hokcCHcmN~M'
        b'Xb8G@<8EjP@(t#{IKD4S+9Mtn3lg9k1?FyEW~GXY3W`_O<?tL)P&}}Feak8%XR-`P`iMEPJ;Kjn^I9$F+oYY)S?y7){x$9c7=8cT'
        b'Q$%4YQwiFD6?*m*%Zd#tODQ1Z>6byy%|ZU<9uc)??zkxI$!GSQb*k1Zy}T6uoLs6}v8<%$CreqZL>&@sAhKvrlfeQILWkRP3E3@O'
        b'3#el5vlpIy&0Mjkn7mb1csp>Iv>5o(1-nZ!be1w6M9h)n{<1xbMs$5T&so$aQP1UIAb`^U5HaoR*Q9R<{{PtH`4J7DmSP5ByuMr?'
        b'XLjyk2p?&}n)EeIatm3Nsv+2-J%BrrYP??m+daN$Y)9zFvqsfc?lPyUU$|#0cal@3rx^(?e_Olww%e<pD3nSb;+nbYiL=J@n?0Ox'
        b'$0x6<i|6E~$eF1-xq-Fr@u7GAsqrbtX7A~b-uU7@F->P{Rn1=58_meh>JI3)*44FgjdER=PSE`Xr?H&#(G#)67zLB~xx)1KEuV57'
        b'8ZA%iaxW-(Zc;~_!qXn$<#91yclQ=vO|QK*aAf>#Enh^#NhdVx-q7HOGCc8n4i{PERay-_NMIJZ2^-PFuFh;Jg41_kuF4m851FSX'
        b'iKxB`)!LgqO-fUf?$ZmtV#w7ra?UQy`3z>YTS(oe^LmTiSam``ZbppSCW;}@W`eB4+aud4&j{o0{T~4)$(LC2pkn*{1|O7O>Psv='
        b'DS_?T+fem^sY%)uU4HbIBF|_IMV)`$Xg8`k0$=9pX4EL45}G?<14DrD#9j!(1kQ?Xnah3^Wa5nkPvC-afRXEJx403Pgu02G&JElY'
        b'yK0oNp9eXjN{SCU?l(p%No|brd>rKERjF|V`%!S>+w&=?jJ5Q|aOh6GSK?One-55RpRRZiz;qi@ieq|5g8q@9;iM>x^JG}-<3T9n'
        b'<=DuuuEyrvjC2XZO_3oyZv}x_BO++x<t8Qp^XgOMK#(tMht^c&jlqFnfWSub(W}IpB6MG_R(bXXnP{)vYvhM-y3@8qm_P6c(3B!}'
        b'*}{&XU505X(IsF{wg*cbI$nm=9Q@K7<+5SC9OrE~pBh`M8oeQIqf!#0!gN`aD7ZIZAw6#+nE1r4?w7atZ1NOEtml<r?<+x{+=Omm'
        b'H|YVxnt1%7Hx8Sjp+fE126GIkLw1RG!2NQ=wrJiKZF&tkRs+_z{@r5dnX8HA)n7#7MsYC_Gr!5SLC~AbTY^jioGrky8B#ZI%ia48'
        b'K4BHG7M{a*#Kr<eWPUr@{8~Fkosq<>bWD|QzU7yg;bR+>u|SpR)`c<#ND|%8P!e#qHip(-+1@}6bgF!EIhlv+q^CFwt-d^YmTqi9'
        b'e)FpHtnX9Wc5F}>9yq>|X*Z2LHDKD1+o19p35!v&{bkCOL1i`(bSg&5@k4SXIbfqdi&nLTG)A3|_dJ6*iZ(ym^Ll`J-Xd3Ip=%Ec'
        b'hZeK;N%B(En!lTE!8|e-<fX4<X{7CeAaeKv`ohPkC9fgsHX~7jqyVs2UH_(kIPP?O$szm_3b?Xd)E>Dps6j#v<&i$rXpdZ9r0~3h'
        b'lIG9+*7J24k_!-{+Nef>WDNf)KB&+>d)0yBYl9rp60)9dS(&GXS?^26Cu9*gt55)V%z92s-po^ni9^VBEd6a{9|d&2bR77j&P|;>'
        b'q~fEEgZr;V_{5>P{6ZthO_Ket^qByPDLQS+dK!1WG1;p&2^&mLQm|Z67p=CJ{nIMdg*E<TWr1^3OZ(*V&k<D@iy+Dc-lrDEA=4l7'
        b'?tU+ZanQa`G48a!Pfh1OCY!c~ux;^2eM`_O7_^OgECtqMdp)%&e!73XzrM<UE}?YLh;RQ?7bcqU(INobh&RPG$$@0D4(MR1292b&'
        b'R))WeaGYI|!Lc^7pm3%C+|-h+Q)3`1!YUw-#lI7a)m0ZbncQTe+!9l&`rz^=6;R|l;7<$WNs5IsPbHe}FlBfH=V(lO`X`2<;c$m8'
        b'pf3PY92osjM9yg)C&q1k3vtgCKQeE{LBA>K%F_aNx688c#cc}r1iz8$ek0Y@N_Ewr%OX|7MDSbjamC293_boW;K`(bC+N3No065M'
        b'bk3G})x6x8df}m{l?$RSEbv<D`*v^lD$Bi-J+u8JA(tM3fS&Y_b^&Qu)9-$DA0|7~J3nBLBGAi_Rj5zEfAnuxo%3)SDY(-r4g>JQ'
        b'rGWy_)0a)L<@oK%DlK(=TpX?bT*OAE7Vg;H7e)9Rcb9!|Rhxd57lz$A?yRhza$k=zy!-=m(J+e~It}7<pL9EU^_o+TOXB!A4a3*>'
        b'uJPRG=Z(s`#$o((*?2$$&ut-UW$fv=l0g=W%+YwXNenw3S2{Fq1N5qsCc%I~bvgNovY_CnmP-X6=_1u(!pgpbJ-PO0jx-i<N-o=o'
        b'n)`s3D(@@&T3`~242yEhE*|?qKwTO>6g?;Wz+X?I(@0VEbiw#(gg&333ieXW@VW@gq3yciRcqv!bn&B`J}>#UD%`E>*<dHDw5v$l'
        b'8KLmEyPY>dUO>1_tDxVf!m`mXMDGU{eIjgyg>ehz3}w%gul*^jNeQP{7<ukZQg}Y{OBy~p8y?)v!C~8namH!>2X+I~6e7fd-owz9'
        b'PgQ1+6rrK;()qg=YFsPh$?RxQBVB5Gy&qdwuG83~G*pzUh~_Dr$tCTy#x7sCS?R2q1d4@DVuy4F#^kxnbx;YLbLP<OqLo-yJLpQJ'
        b'=e&S4u}(oxQ3Z3xOvDUkDz@x{f&%JtnW~7?ReidBsj_6LuF+CKZGVL-aZ%gLl~v!Clu(iU3aaXvk_zf%xoYC~+8ZU6)W9#lVegf!'
        b'r7+LM?d7V1f>n@Ll&!1PV{vCHUW0B(oZP7Vy^>4s{lL$c;=jCY>K7tPG8VY#RY5IKnd+trp@GhfY6b&pu6iBOXc3*a1<=g0Q)hEj'
        b'C?i{E`&YYtWdcLZwa=0!v2JR~=7DE2^c3BD#IIvP;3WY*^y1l#x&XL(P&em|q4!no7khjCC2QQ3i&1%tgaU}d{)>P>XSVYUZu<|R'
        b'AbAW!SDI9|Gwqo64E)ro(lOgb`$`J5=ukE&{KB3AEd30+@&r&`L{Mxe+dCz+VjZ7G?xfiS%SX6{%!*n$-G8Ee?cWRsui4&fw@^7H'
        b'8Oo#-B)aD0AT3NYy5O4m?RFtw2M0N$aAo6VkN%+DI*Cu0X_FPc<hYu6$;nSPPEylc)S{-9WVXzeP1&ggdp2eV5`JEPIZw4U=VXp5'
        b'Kf}7xqM>tFPPV{qSSb$(ZJs_P^A_%HpIMzJGt2zBbRxP<SBcw61(Q;eqqAo#N;}$ZL8R_hQcQAr->QWuZP!qY7UsPq$7IhYtTKiw'
        b'I)1hwxuLMN-E#bTnv7AKl2M#LZ0|5bBkUBEOM%snW9R(p=Tfy`o8u3p++(L^A`eZwb%AV*{y+qZU+K6eE^M&9(9Y1vD??6lWZ!ve'
        b'5w474^j*<I3XFm`B4?JK1c5mciAC+HYOntzLQaar5RrxRI|yU_Uj;r|QKL{)9T8A8Jw@;_-1B66{gdrXzEm6jc*iefpgot9OH`T%'
        b'1&&mtQZe@ZH?t5!QIu8SY)SjEf9wi?utHh8?Dm=OUFk>9n9YCL#iSK|fb+5?z<-?=Fy8L){CyXk@#82y(r#Od@T#RG^IP(?3o(!|'
        b'QcS*dqk)&%NU{(`ASlwvFzEv67mY-*x(Q#dYUGM7P3&^>Ru7qn_5KEQ^&$|gNV_7azpCAOQ+jBIWW-N*1q3=0G2Sz;oy}_Z&p|zM'
        b'709H<DUz9m+c|VkjmuAFUlf@1PG5jf>`+W&6v2F)ClpmpC^B`WWQs$K7gaT40Ri3BaYVi&2RNDbBJO!>7qD+_Bld}U*xpB=yG7E!'
        b'p`y>pU~nQ<*=kohI~5^dA(As!PK_k&0tM0$O52lBy|SOgh!K&=&Ll1smI<6pkxEXgdJPU=ZUOSbVJO5|vK^Kn0w60x8EI{cZZ~5H'
        b'{6f<9#4gu|xQot;Do5++B9c?TemXMEOm&G@SNcbRq?`p>WJ31e3ZN2uGS+jkr{|~O718tLuF?h}V7$jgOH?RqSe>9NeF~Z^i!>=6'
        b'4FqT`Qh(HR3DTo!KSaP+Z7lIBVOK^#x)vmjcVA8n4U3WVw6CY2g(f5ONTW;fo|6HRTI`eKb~sf!^_QDfLX-O>a(Cv2Rkhn4q+Di~'
        b'Q@!s5{HFshfvS832#vH)2~t<J2{#?R<LhnSC0!TK0zI)fhCLFH%)H4uj*8H*`B0#kOnrrLY{bg@i0WD_DJnJd2^%9^wM^9(O->_O'
        b'g@EGW672qftuHXN5=*gvi{55rV<D1>wVb#GDv&98iwzSVBuWc~NYwd)3{}Jof_^TcI6tmSS2{V2%W3R@zJ8CfnY)aqwMANFFkObF'
        b'oMY{RJ9YL7^jKpRR(`tO?%$FtBj`fRHftBNCT}*nkn+tgmq3IG*Q)5UeWLT(du(-qJSsI-#;wH4mc!hooFmZll^4(u^9Z&fkoqz~'
        b'|4kfyOGFp^%C8VZe-`ZlELV*po`Zbt4Y1D!s(*#v2t6GD85QB0mz+kYkz5YJ<tWl#PTTFN3b5-?Ni7i>*|Kv4eN1F8wfX<Di-Z0B'
        b';xowKyyK{dIY0U#c<HLJMyJjH0Z`&7Mb$U!(DhCQv@FV@%VvU1xM-7W0jFhFyU+(Z_OrGChpe-FO57iSOQ|J?cklzTEEP(o)BG^O'
        b'm!dr2wvkNlnnrv_qtb8-WAg(xCqix^LAOZnZTasb06o78tm_)+I24V(CA~_Fe;@EAt9Zdw6WxQp547#-6LjO>2QUu$OyD>baz5G9'
        b'Mk+Arb@q&nSmTf+{&N8=^%aUW1(p*ti8K<q_;`NTvQe2`J!Qu#r7ay6qWr)-#O>A8vQ_4Qpe%b?bdF(m0bdv>O$pfU4M@jA619+w'
        b')N<|rq9g}xQhO0Kv{uYp549j;bu8hi6eCq;(r~O)UxlSYA>@FTr@3SSK_2{2%tQ$#2xlEGrRT*qCV@B3MHcq}HhNmzfePJarz3ta'
        b'7AZQ27>@{&B-Rl}jGh!dxBX$_|KQ^bmJtt_SGQR{h#a)PvOT=ZLMbw33J@MLl$IQYAqF=;*%r_vr$y%P{6afrB|Bd(KQA*hAx0MI'
        b'((q?-wJVlg4U3BEK_&KqU7bGUvSQjfMAzoe{YJ99Zy`Hpmz_u&naw<Jw<p;?_7~>01t{EQScJ{fU)F<0;XcW!bjj`jM?aaqYZI`E'
        b'xtI}!d5XG71kYY#2rf6t5i2?5JNJ-8(F@8?A7qdF(Yyg)S(R@4&|i4m&o~fm$ZYYuDqoHiP5bIMh>Q*6{F){)%=SQAAQ|DCxn|h>'
        b'x<4QcaC%JFrF5>i!p7{f5Q<<wke1wHR~Y(5`fV`+$hH6GlL>9(D`-!)e~jBH8yQvTdYd|1t}1c4H8dtYp?Jw_Z!D_CE7p5mplN{c'
        b')ugIrE6w>fG6(B@)lWthg>hhKWru%uj$NZa5lhW&d*^{x>5DezR{oYt0gk8uOfR>qOkM7iU8;w=`lgn2?G84H9;S_>FyP1$cAT0p'
        b'IY423Qy(#W`aL8Jrz7)Zyq`hstA`O8Hy+^#>TEP71WZvE13=o>U|n7k*|AnwGKL30Xy7N#(e)C&Et0!=WnD$EE)v}qi3mT}54EwC'
        b'{@SJpFXy5asR|hg3Wje%-Y|5dnF@AE7oH?~O*7NG*mJD`@|(R0d;l|-_|Y~7eiag#t%i{3KiY<vNaFZ?MV^~0u>iyHC7%37d*K#+'
        b'1<5lhoU_BF@SJR&AoNt%RL|u$UjPfpzhUG;Z9^ED;|=ZNCRZ|(U^t0+TH2U+UmoF;Bd1Z4HB908wZFaqk%+GX%XCpm3Ij5(B0N)F'
        b'zh>|ETM721w({c%76A@UMewDohJMU&^J;In&EMNrW+yCm!ff(~$Y6`uM>N&_o!#5&PX`{Tjv&vDv~k2YT8jv~u&h~>;yD0p!>z04'
        b'XWBqQ>LZ(UIts)i?VA|e*6L3jZ(17Xx2Iq!AO4yXvT`j+<p<DvSwy57D)k&u{StC=_=-4GAd&l5aflPW`~}Q)y2#eGqDQRL5h4Fe'
        b'EZo$}5cZF7E<1^%vZ8=ZFTnzuDco*pP4i>R_Fgis;6TrF5!DZ4>~$e>Hb-5EAD02*d)K%5MPYm7mcBjNkU{X2%|{m0d`i$Z>>+fO'
        b'cq>nWCLk+}7>}wSKw%WJ6`t!t={E>oEggZCdV#1mV7>p*7A8jTBhb!}NIxHBVM%IJN>-vA%=U>u$`%(<80>%|yQ7H0drt}23wr6Q'
        b'BeHDg6j2mO$%^bVi&ug6TI5oq1HSs_@s0jfd?X<hP*tB?UaE5EAg5iCEvZ#dky*6mwt`%W(u*ZMM=x8_XxCwiP*D@%UEk>HR5x+8'
        b'mb>OK(k=(BoKc_;*{D&<IIkG`4i*&FLX9{;k%nStwZ1#5D5g{36rh$&`zp%LO^2-pJ5u6)<9!=jfek|UoedELhP-GW7B+(fhvG3^'
        b'cB#_KK`C6bG*qVDde%d?x{QlDt`hVg#UdFMHA)OsiLL~CH6@!?Mhrb8+Kr1U60&lsfh8(CZCrajGGM#Ic-gK>Pqw`zAftNn@S40X'
        b'Byds~{kX`e)7n|LV15BD&|ISWtq5JFx(LJH#0dXqH={D3|0*F>LkyX*!u0~|Q@ac|)L!Bg7!XtSObpA>U*4d~PeolALaw@IV**DQ'
        b'5jh#K%gHM9Kx;m-+`Gu6hq!cuwp>1~yoibE%TCg+iK;kq7`f~`gh#FUb?Nn%b1BNYJNY|6m}`FJ*oQ5lN@mj8$yk0aQoUd%j{UWz'
        b'PrwZSxML@in5k%h*-3d{*Ugru7xGe98EoIQ0AnmlCQ+23LoLW?H?@Qz40$5ZzwxU&i^TOLwgn1W=Bl5VSi!MH`}Uo@BLE|6%~!VW'
        b'mN3y5TT-=QG)IK(8Btw^Bz|Mg6+#+V!<J^-)>bb%uzj)AH<hw_yRajU_U1{Z7;A=e%kA-R`40*@VS{v_{^Fa)Dzp+td0lkVxc{3u'
        b'Lge1Lu)#CE^_P3(=9z+*{Om#+8795lXL27Q^UM&YRmv@T4A#PvCe$X-F&LJV@7dM@t@bJydF{M3#Wu3hI<mYrztdX%PjOpxV{~fM'
        b'B~M4Ir1ss#A;i_KfMKBDhX}t~U}kz1jq*2|*wb>#M^HOj<9u=%PsrT0rfC<LccUqGvXGV#N&v1Kn&(WoJv1I)n<uck%^tbXC{L3&'
        b'agi~Hi59gDDVKSm-qx)uSz#(D*zkQ>r0=un`9UZa7)C$2wF?$vWNYG5p2BM8d<6}X;do$V<GK=XvTwd)&8>)Wa4JUaeu0v%JxX))'
        b'-7cMOgOy|yM>T^a#>lH-ITO9_9=i8zqiSo@*~6+v&5@?QXexE*g+tL-XPoygtg}WIM_+wKygLuJGrLTt4PnBVyq9!xGWORkoyj~m'
        b'$N$l;+E|{mqL2QR?Sox**BoS4*YYB#P-y$G-oNe|+|79ILGvD>S`@6Q#TsjI&EcR4`tFoQ!T-sOX6T<HLr%mZ=aGRvvr&VNwK#^<'
        b'S<#Ks>6gP~@RRRAABN>{CWzxcKk^9VP3vWoosdoYD%}>>;!9pz6VLV$l<Byx@6W1$a2gJ4_{k-&eV>#vPNAMB`~vY@jDKs3<ZWH8'
        b'Eyf})-FZ$^XO*0ld(YM7Mf}3S%u45~(RVj4p63<R5T^HG#b*|FdMihK<+M}U*_6ePXHpMTPsYqY?d0^cu5xn%<RQa1;-d=fn%mxV'
        b'P^03ejo%<K6nb}=x&|0c$Loa7qMJqP1PWBIh<!Q|bz2I*D)sjiT1%f%-Lm|uOXGQV*I5wpj3DBnt6Gv74_NN)@pzjRyL1H`^0s6p'
        b'>$JP^Cp%k8*X`n>+Lrk=%p-k5O_=udwTwG92jE&6!zf0th)%^F|LR>vMY(;QZD?noa9~hab>x6&-%j)fB>90lJMzsyfL?N#-|u##'
        b'FVu&PTi^g)HHXtrMjj`Vt;W|P^M$IB6@iuU(_B-H+1x6#@dIwvJWfw@t1>t}!L9n0F@sxWGPZN8GK~$~s{7f_o%a2AIPU&POC~{L'
        b'Cly7xZJr=Pl@r{6ctPJ5<`KZ2m#|k?|5Y@eXA;muAlAAok4VXR!=JgUpBNO1?E>X-Bg7Yi9=Ee-@qHWz13(uXQBbgW?TTAQ<oVI@'
        b'rSyiNFmYF&EcNAB_MTmJD~-vZXR-;q(xx(MbQj0Dc*>KpyEgeqG+m)N+sMbsR?_*bLi@>`J`S@zxAVz_UFC_y(C;zro0H0C5cC49'
        b'`~l>97UUqFI=txuF|=HIIQq5dA$Iu$+$FErUaoWHRfMA+sp}^^PK4)XS?Ug^^iG?1>gq<S^k!S-R9Et^MqVww-j=!pubApu^{c|?'
        b'cGj)5$^x8Z2%>iRKig?pWw9h%rEnq-XcuFVr%)Ed%sLIKa<wgubo@m;q{y3>x^t#6f1#x=Id5KCPF}u|+T@#L%yFeA7>SY+YJ@P#'
        b'ns84An$<>}iF-IYjNAx>2}75tefBa#)9*-*FurWF7%}b2D^^mgxq?oNQY;u258>K*|Fqiue{Zv_G6xS{4->)T;)4q3#UH&t^@H@d'
        b'3VrJC7qN96x={oV^Pg&CVhjhaGx8dZ%uKZKWQ*HGISz<WBN!63TQUEMHWUo3_c{~3L!&X@*a`D!AzOB6q8N?IYBFu79*lN`#BfwF'
        b'C~DW-WMce(Y8$$UaMZqf(cce^anHACG}U_|-<d2r^qp0sVG?1FkDdk2R=1}2^)_HCZ;Ipg??HhX4_?5b_3-a&Lob}rE2z0Dh8W!~'
        b'rY6uK)^JlqUTCOs|7HU68>tI51c#*%rzr11g4g2#6365xcoNfI$8Fy?Gl|m0!WoPlJM_Wm0A<y~(HADlRF?owR?paIKjj!3-{<UG'
        b'JMZ3{YYBNyHP@eS=0Cv$@+4oH9t8bpVB?Z}Nsq_pe4&leSnQbj`8M=Tnl$g*3HwyK+()w?HrqK4g;^(CKl{M;Rx=;_skRvBIlUCT'
        b'a0=paR|2u0_9L4n$FUM~LonC1@zTYBxM<H4ZH>c{^OK41(tm2Ua1QMj6wDQQC?etXZbOFWvNlGZHCyMd&?OeP(){ps_bUzCq6eB('
        b'?%Dw)`ECgvsEu7t8Hh`r2e!$WSL|=kU)K16zZjbJE8dqg;f>qa#0#wqKYY#I)^M^`wcR^#(yMyWyY<D|dEchLcV^q<zzM7E;Wq#8'
        b'+U8Q`MQ!hq@aGX`Zp_?7CdPB18Le7&+x!vu(Tjd~gk~deUeM+S#fdn>9&B~j+Qyy6+1f7WscK0;YoVqVy)7Q+>2uq-3eEWa2;Bzl'
        b'U=+Khndf2=u>0DWdk)Em<6ve(iOi&d=7H`1*m83FhEu<4L-NhT*t^Yn^?H;JB@Cx^$`8(0G=A$#qqjHMb{s`3hIG;jtPv$c@oyxc'
        b'e*<aJDe1pP-(;gHe*$XT7*FQMG|4$mgIv99+72mNc6u~zjGC0k_~bw#>AEHzL-_JA@*yToF>aS>j34?|@@E>|##A&C=+m50?;+d#'
        b'(QSw1gTnki7wwskri3I2uZ6TnlLS?}9t3q*<*H6(j$J63V=?wxD~LyT-+!||w=!u^2WlL>(0jEt<eER?Nk@PhU7qh+Ndkm3FTf!{'
        b'J*l<$e`sZ_q@4md=o;Z_RIjrLwATno$fi-OzWa}1X4y`V7^6V)ZN+V8T1!7}_57{Xh;*L{wJ|RBRib(aZls*VWMmizMeG@@?9HD$'
        b'Decx(TmrM&#q=xu-|l4gdN8z8*^$-?s))cq*sorXd8X}LFVBklhHyNNrGohX7*=(`{fg3O$4Gi|VRW<qzjiJU0D7b?X8D(%Un3lO'
        b'Qo*FI+pH|eAIqSpka&y+pRBD(UraNYek{wdqHyg_CbeL}*fZ)ZLQ=h2VRjUzf)!c8v9f#gou@rM1STclV5BPa92ZxzQf9PNZPF!E'
        b'C7jMhB7OmK{kn3cE=312G8<@(*m7Mk;k%IF=7TBTzQNh#EPbVweWmpis+cws<fJKSPo^2zms?4jOoPivLRR`|6NV=gq>MFv)btK%'
        b'qtQ1vjBu6GBr#b-Od)N!9>*E24xhoKZ=<oTALxlmwe_CbR*j9++vFNTQD7YN3^y$%7?Oy&pw7l+8XNU~bS<v85r3e|?;+^FVi}Vr'
        b'n=I+tA7-Wens9uE6(|!-=<WkShcP`a%fN9=rZA}!7TYGBE@faQmAFE3|JMX_uo$1D!Ey94O*Zy^R4aXn{^VE&j%DM7E<=%F!?H+8'
        b'?fn8XB`0L#l#)U}hyH<Kwy~iv#L?EDhh7kwsP%Sis6oU$MXj6Vo2NY^54;=u=juc9z=>NY-&7q==o`LOqa}tcnAbtl>XRW==js3*'
        b'OXfzC^prrZiOiJ)R+#(@Un(K?4nnMRQ-NYEkP-*v+4)T%B>`%5z7f#I1eV1I=&6C+`$OekWR(l#&JLu+*IGI|7)78wK2V<EpWEs='
        b'fIxVjZR#xIUCLSx5lp(|NJMxAT`2}mt+i4lF$uN`X$NH^-M9Z5axVcy=V160+Fe7rw{PHc=j?4-uVwsg%{AZ1`%=`NHUu}|Qag&p'
        b'Z86AkPiUy@2G`ja31Y#gXqg0ebAvB;4qX5lg>kI~vdAYv0%OPYc7?`1i7pYJQD@jEr&c@$zcBMyh|<_5XV{o*o5HZ|=Yln36;uh0'
        b'i1{g)9ha&Axo@1Dfiu~-Vk5Q&GbCU&V_E!)E%wPu`C}Wg9M~pID$w^cYNiHThG^VynR5|X=jnAIw7|+_Bix{mK&is;{Lg_>#_$8z'
        b'c^be0PykJT0p%tvp>vSAKMPAI?Nch%L-(URsjI@5nzQ(P%s5u?!kC*&N0()>f^}$2IVNR7mMUFipCV<(bq->(8H{$L@~r}N`EYWU'
        b'a)rh|nNAh~L%n?pps2S`)|v9N+Q$rEbDe|L)1?nQDUS0Z@VQA)m$WmEIMMS|Go~CXs2D5JtkBt3V6kI>-H-<JJbpJnKa!t~<5{R{'
        b'^GaL>M4qKZME>cqUufJiPUHWJu(ttg>c|?$Z*Fcv60Vv6Mhw`^y$}cpEy1>Y)b5gq;iK9Gsu8f=CD9<#byq1Z*4o|NU_%l?l1qdH'
        b'?QW7v1y)u_Kg17qfp*bacvtNgwRT@>mo25XYbjcaANMzN6SceVKL7vo@PvEk&dfP8bLPxBGjq-f68Mx8&^n}YzLrTtL}Ou=Tn5x4'
        b'UtC_#;hKWGG&ziEk1Xen`FDJvo=(VhK$Vo-6FhQ`<ZxdO!|y-i8y^B}2UN^|5ViqK5=2g|zK1rldA^>5$@S$Gg2xc)JQ#l<*F|!$'
        b'IF3M^D?><;rw>%0E6NGXf9V4Nat_T?VIde?jsWBw3j?)J0XXhHehh<b;_$_MNJk@&B8|c?BN}4?-2zUP@y{^p4ujw!>6-#WYIMzl'
        b'HEt<nrK^ydROy*4?t&%Ku!a3={UjGze$o5KK_vSk00{=*9Uo{Jpb2W)4WPz_p`bZ{o#vp0XM8<;(1FITTYxse9E?LF5p?-;;^kEs'
        b'n2v^IT>57C&Wl`4WQ`FA6@aW0d<10edKRFwyACi-!zvNHsILYJRWbktNPF@(B&Z3gnBJKVa#pkrdW?YfbV7ljD_T;$3y;d_mit$U'
        b'RA%>`4S8`oiX?t60>5}Xyfy_Fd@A=~JqHC0QEmmKi`1*pG^K3h<J*XPTaC};s1sLy5gvzz%aP<bGy?p>JN|rthIW+E*SWU}i}>>+'
        b'?=n@>+|`1uAAklxe;RQpx{8A!VHf4`B0y!HKG-DxJSZBc2K*1F{IGv^5C@CO=ec1B7%GGZou_sf$bJmW)tc}%$g9(5BHVqTVR7t~'
        b'0^?Q(hTwkWLJYnpZ2OC1-4~)&sF;gN@MZFx!V9aF_<iA*R%yiNep_F&I%(Bv-g&{noeK_UpxQWOY8k%d@Sg?asd(by0S=ylEXhGU'
        b'J|ry1>vejJU=4Ww4en|T;a}`}2%!7U{^Dx~ijd@;@Pho#CG5H`dY%{g*dl|0%U*y(wNbYXG5D5BiBH%L1VA|CIUe?M!@}ZpH(*b!'
        b'*P<ABrXSpQ5?Nk`9DTLY@-g^txy&G7Tyc#&LEK2=5puv%R*CornIz2k$Tj}0TOnQd&#;@!-rdA9cY}yWymx>k!|&`1X*^279a;4B'
        b'0p)O`hD0BR`^Q(^&|-u~dKt?NMv-+*n$3`+#cVuaxKD!hKqK+I2mx4af#B}QZ%M@(%>!J@3W1FRSt_PGhP2#~!&N-DdNUv(l#CQ4'
        b'V!UA7Dd$IS93C-~OR=DLcX=XKM5dJ-{auk&?0^b6dth0H6)$oJvsoVkS@1HvP~KG!g=~egQ4@@8ogOJ5*0|G1u{3=i+IB;jQ*E(W'
        b'5M&<8C%x<)MdykCgc%QE{^}Y4Irw9c-?iNZ8UODfr6r+g+MwcCE(EDzL9#I4ZA<yTFkk*pm<hplvY|wN4D^G0KokCZJ3+-M{{fTu'
        b'QyVUz$rQqPz@e-U=`mew+Vh0|M`?%HwBHg>-Amg&Ke^(HwLFzQ?u7Bol_h2}0{T3?7aPoYj!P6DfOf_L@11f(ziTreMf@p<bIk#7'
        b'zZmF)y>yG|xWwzIg<kTlV)|DIzSKmwAU26F$4#fK2{}ag)f(fwH$wQB+RWr{rO~Kw<$-_~ojm=$nOp>8q;F>Th<+RV{dZh&+2q@E'
        b'AzNi!q`3DioBZ34((gWlSq1dBj*D~NWceLA9LCEYoWn(vqjS)baB_SO#{;kYZt#fQ_}ZOv!(Id=`Mq34AXxNAY3O9{f24t;9Y^n`'
        b'H5$x*Ic{%2BSCrTdkFa!vvM3rFaEb~8Gm&p<jUgV&!BB=`l%Mc{Tuz#mk_g$OL_$jyd)g$;R1w)w4_>VTz@5<qfHf!en)xRpm&kg'
        b'hu>I0dc(mdlA~oS0<yYp62{sD^kF=CgEhQ`udE9UI2Vg2+rjey&$uAMxcQ1-t<|+ddrhtpkI<dH4XW40-MDK<g~zh@?5^Lj2gh;t'
        b'{aWz-Gel}eXdl<?6||vB=(a+n=)Z9#n@DWKcPU9|u*Jb;ieon}oh9P#Bn3U^K*vTP_sTieBRR}wd}K~L$FTiH`#89@4UGaSeo8@G'
        b'bW%eWXk;9ooER;~GhyizLt=DVia*i)FJhtFk0M?mBbMIQ0s%$VF?fRzwE4Zl&?TDcAhScX-!ieHkzjm+&)`mk@ozT*UJiIrWX#?5'
        b'Lv76Eg!X0i2=N-6edY+v<iwU#t)_0Y^>F$#6*dLULGfs0X%1rb(deGeVOG1_WA<9@W_mbHd7(>?6y2Gm%<57mW%|T!Fd3+K+d_Nl'
        b'v}TVsboK_CeCr;KcHF%4+{5iS6@1nss*|n3V{NCSZDn*o=uSBKu-7}gQn_XN{*3Acl&_Ty`LGTj4|{r9tTJpm`bf>n%!X-+>Od=A'
        b'>W@4hR?Vk{c;nVPy-vqfsb2GB*uK%;U?{rPS>QG+A9p}&%>|04nUpDM;jNKb*h&647?YFIxPvZXrSrE^#<kxttbZ~b8{<6Ir_pmJ'
        b'@0-QRJXsQSFr6NB4AyZU$>m_smAP0}yr;EDF%J}`=MX+(YEQ*%+)&?2BT+yuaJy)p8NJxaX>ErNx{Yss58DlB@znPtHyOq7_dVQ^'
        b'dG^lO^R1v8{YsVMoA3QzjH-kE=?JZ76|K0<uUvy?9u_Wc5?&|8)V5aN<85Z87}{70?ou4&F<V;Aq`6_I1jbg4XE!zC+W#%aD0`l;'
        b'W+pK@_Q~|b=;dp`{A+VBq{=`?qvmKq-V{niw=cU&tZxmu#zi+w{fmfd2ct?9-Ay|-^$8(v*Ir}y4KiEVAm`y!eya~}H!ERWR5IfH'
        b'5<@t#s?{g>PxycqKKY79IZrAx%Nslrb6kWpAEmNdeT*kq){Ju2XcFCGGEUOyC(>Je^PYc?u?k?Ow)(Dl?uC*44vG<q+8fqtsg+H*'
        b'$|_xtwt|AzD&N<h(P;2<CoZKLQ7>x+gG0uf8)}ktEr??D4#Onl*N>Lqs21)uOvZrGm+ra^(m+YwuG@IJ_Il9oPGgPPSMLY>3zg{N'
        b';3PA;Z}e~mxJG2IhYQCT4*jogq<aytCVJyqdeD&{U|&^|i>Vjk*b+-x@p5JQU4DUEbp{4cp8V4-O5BPUTH&!s6UvGoke&b+mU1}*'
        b'oF4Av2h3=7Kc{s$(y?*w?py}oq|a~w$xXh;jCO<1Pa|U@Fag)IS<K#O6DbDh>Sk_(<zWEr*!F!7dPlZ-6qU<s8);%>KNv>5WJy&z'
        b'pf3Ra(llI3{>p%!8Qlc{_k5QsI@q1=Win_nj>64tY7@){bX3{<?7*mg-wIfoPH@}kzeVM-Bk<{dxnIt<hUVgp&zreLCY!in>7Nzr'
        b'W~BBTct0*PuW}pzaEt%1;CYmN@*XcP{1IPHHeS2?EbExP`z)ILjtTLSyM55{){px@vHHLFf$^yy^#QfTbJrf2*zCcVvOAdJ)=B|q'
        b'+10D0!~wmQ*79$#b9LW-zmkm~wyD+oIuvo}XzW)v2Tw`{Jz^jYz=YCJviBr5eDrsY|N5x|3mpB6w_DQd5qrDfCx7W(+a4fmN&|eH'
        b'XIYF`BL<C<YHNO`bPq-g1bE?Lq0p~{$IEL)r^;yzNh#d1b^qa|GCFYuw7ZX}-rC8h6II~Zm+mou2mal_>AnX%nnV~LJ7&EGMe-i<'
        b'H*Qjr>gAq1+7W8I(i31kXLWqfPzjz+L81)9W5Ae%{2cV4d;5~~##>WXJ;@P_o*)IB(SU06{>;dbk4{9d-5*n`Nl?AWD^TMxYk9E;'
        b'pS<<5NPeKj;izqVhaP^*J1uv7)iU9zz0y^4nnRw3mO^AMq6={Q!aXqbwoOl+-48dH^;a%#?3^qE!)KXd5{4t`VKyA}O5QnA3`PSK'
        b'iph<sBf}8>7fehpydkjilO7)R%6>LVM`Jcwh{O~Uv+kYHDMvBLH&vYY(;Yh#bzj_8sx#=viHG;skjY1mHLeTKUHMT>E<%#Y)KOTv'
        b'=nXk*4%xUFXdk(V=50=mm#K?DEh7x|D$F1iai~M^p~lC>&2@H^Kgi%HTs3-lq@H6u`CXz6)hfWMF>;)-7Auzwx+U#&zp#hr(Np_j'
        b'LASoKeX2O-n=gw;#@XwZ`~5-zDd06~mQ16T`;jSi#(lhuX_TLeu+GTka%|Lq%W{(IrG}eUHJQZ8a7(HB{j9$=7FpWMv_<?8I;N#w'
        b'gvoS*D!o$W(X*f3dXS+~6*PDxK6F9r$%vp`5<2n$1J*X<z<1K=S*eRtLSSnyXDmjwd!c2)0ET#{je#4mUhrCypaSn3A{T?I@$ilW'
        b'u%JoTPn1-uMp&2aPho)1t(mdxX4YKRz7VvBpeFbCa00B+nUSlYj<{$+G+vsJ6b|GJph^V=jRtfv(Y)V`?rA*ZyRjb^0D*&gbN{{g'
        b'ynk?+qgxxQc+j})PuHl^F0(R<JyiAk5bDVOJ2nc%`(60kyGIJ^I|TtnJR&-qQ)7aAFYmeFHeQ(K?VBZko!H{~dvKmnNRm3Mc&k1q'
        b'r?$vj`{slE&;mp3b47CaMQBhT{c?a~jJqL~-NvDR_J*jX6SQQaQ_}AA`b=CQ7AZo=VGa!MT7a3)a4N}5Tn;aigCR&V>E&p=h?r9d'
        b'mGr+5uuc)QbwT3ag0TpoU&DueNMG%Kuz+av0>H|EAjjnhz(?qjOwbk~nK&*v(FdSKh9lj+$U-c}O25OYRQ|(HU;%<RhUQGnf66s}'
        b'cZVNRj4ODqtXjFhvJf6OnBycHrWUF6F5lnxr^iJM1a0HZTz6vh_tbYVcf!2U%;o9kcr@2Tu5u@OQ1dDe?TrFslb9u;65P-+lEWE{'
        b'XaPMV#rTJ><3jI&dKeoO=s2r*W*_3++tMSL)Z8+2502)ibKRA%xmCY#0Zx)02ag=JKzAosc`Os5b9x^Ktc?xmQW(Mcmy9=CuDgg#'
        b'{`3~LaKB&RY1{={#L80CS{KkNg7@a3b`5n-u3O1HLK3K(y=kkfWr!qK@SMd=W_AWoqaq8SbgY_h16d=8@7wNX{mGrIafoIUVm8DE'
        b'PfJwawh`$r4Hr3xUGTz~<-V`mhP|9~127z?`YWKht;lnSsi)iWF^ypbYrm;_U_ZI)3qs^d_X>iyjxwqvH5Z`&-V96xFS$;-)`Z{l'
        b'1!$aQs88BL7eC=xNnNqQg+4^%AGD?Q)|!=wv=j;X82qfotPBgj8sEKhXPp{t1Jscu7=6$8Ho!3&+6%wm0<)h6wKtZAjFp0N&RcDL'
        b'ms~(qQv4628fr6h(eyJ>6D<<e>#hl_#IeF;-^1l{BEcda$(jyH2GAain-A7LBRS(uuTKj`He%-r>%ULXF*C3FQ=5iBoUgbFxcQQT'
        b'$b6z8PTk#R#?XmUN%<4zGf`X~0?+JhKwO4ClUF0fo;EWNIjE#QZgCz2f~%@ih%bY>79`dHl#`7yGrIDSfCp*<A~vYORBsA?1sEBZ'
        b'&Pb<kk)RfXy0J}lx&>dB9;fQW#unf(1{VKY2A=5$^*SHY!|B*NYnCj;mjdObhhr{YsQ4Fi@GRBTV%=G(OzPoG&M=J^JGNe%tex$1'
        b'xqNPy;uPb2p)GhiT7Wp8Zv(&3=C`)ZSJP$=N1Qcn5Tmmulg-2h<P*-}u7RyIc>ohY>?gR70WD9lXa--(UWqh$Yx!R=AzUWSvn0SJ'
        b'GL4k0D%!~6g(X~6{e)}cB}vI&qbAl%h_bfwbzC0DZUzz_3L4uXnvrHNC^od16>Gkzs#N^)nzRr%R?qfrb@{frjC~B@a0M1W=|@u('
        b'>C^tBOh>|30TFVh@WSGX&hp8&n*qfd;!KPDq*(Wfz|Tb$VPBD4RHbQ~U_JDr&{{~0h=LjlSA%qLXZTBj?!-l?tTyP<*x&93Yz?#v'
        b'5(N@Xb2<Mv6}5cKxCNcj9@MS0X2MH+fV#ROCfpK00dV;DfU$3<0T4jF+ycaS>swvncgB)y(u<sqr)K*ecKIH0O&(&1=r&(OTYyAh'
        b'=yej(aXJQ1k6Xe?3@`~!8eIEoe`NPeMYauat&mBEt{VX!VHQLIg@Ibo2Bf&g8ba6xg^G~x8|sIapv1N0OPtDTiOs$<=bX1%145J*'
        b'>^W9;_1y#hcUkYv(4lj;^^DM}1Twd2bkI0It(|50PM^r-`&Vm+hv~QsWn$wohElY^yYi5V8;2=Di*E|dS24c)&iyhDNA+22%3LN_'
        b'x++rrackxi`Ri~&h6~jeAgaH&_NN0ykd7~&qVc+_XDg-QHDF|x<RH)awr{UhkG7b-_tRLBqfOkl1RYt4P@<NEhb6Rf#f~$rbxQ@l'
        b')2%gCE9hzj55t!lMsD?lRdls%6Zytk4TVTgm|4G=)<<>x?xycDZAf0$69%L|GqG4d+zMtN3@NKcXd-G`SY0%3eb%v69&UXz6WzW='
        b'zT;?XMFnQaL-cR9?)aaU9{xaBhn)d5gojUFo(3ZfNCytC1<ZjScGb&AtbDiBtQT7osvf3c(E132KC<J9S%YLD?d8DBD#Z%{9qSLZ'
        b'Chk<3u_BWxzH+BBFqG!^ifAp;(KDYvWIeCZi}OD->m?d}1XQP9XRaj2vOWueETBaI;Qt^jC$~ThG<gjlkv=FiaFG%~qm`0sHJDD3'
        b'n7CZc#l-48t<`(t1c(>~<hr38KC&KM)}({lR!FjovmfO0#F5;f)g%t)9>!gTOkVg_nmsp}c+I$C)<?GtgyE6KT}-;>3zdWRZEqpt'
        b'#DPQbiqhoZEG`)Nkg47rsYS}y4R8RL1*~rJf4<dS{6Tw;$$YjluD^$4Ji<WV(a>LUMe9UB;`|kT!Va(T3d4iFM-{gW3yKn-RQC=`'
        b'&U#ea=}6%sXg&_ll2Ym6SU`~uw<%J{xqC;J9FB$)Ss952z4)Vuc>Y9pWFfnb3?XdK3KZ^n0Q`}=j0bQXBDdAx<$#$Xt$`avir+Ka'
        b'M5>joM0P7!_uvKLl0wjJxP}W^_Puw=zmr-ufb+(yx6)Kft0rF6DPZ|Gw6-0sguYlTV0D7bYx2+EN-y39!!^KxL#44(TmcSvS}tN7'
        b'_*R`t<KbLPczg#}jRe%#HqkLzN(m1+wm5-W(pp?X<I74Epzg5+(CwHPD=L>zPqz3a3r*ePqHejrcp)G}<5!II%{d$n7uwM_lOTg}'
        b'QTkqR0ocD}0ANtfovYGCiy@mUiC<In1P}DIlo!Uu1OW88ze?EBEwHrZZ%lxTQdjABm$SW^iE0FUNWcu>%dz)&KnGzbd_G-EZ>~Ix'
        b')a37>#E?l52{b;>D)5s&AblC1W2Aw95n;6N3mRTNTn=yjp8z5=CJJ#tHKOSGRx0}%pa`&lD~H*nzK;g!5L0-=2U3F;C<A9mJbCb~'
        b'!O6h1cIwW(o^PFg@^K(yT#=c{tb=EK=`GYZG~|6BJ9i(q?lgJC6iScUXv12%>JfGm{@wlH1^!k&;yeqK3*^d0T;?x8{Nx(vsr_9-'
        b'=Lk?^(`dsQ=P~&9Hh5c1SEV^m!nYw%Y%$fl-!0GyZ_wm6kANE3Z#HZT#!2)cs*_GUJ^z{T-0Sf&^&j@<V+Z4jBl`hqH4YOK&e&bS'
        b'oei*>s}JngV2E^<tG?(Q+SF1KuTme}4>+qK9?@{4@x7Y2Z|C^yJAMw$(ouX_4?i^W$rAOaG#L4uZn2yldBU+@-%a<R1N;s(1D5v%'
        b'v&BvOxm=;2$6C*yWn%GQM;o65ql%@>@F$oZ*IGb<Fyl`d4G*P8o$MueE{3oc=ORFpnz%JNt9VjO$mOzhkt>PCb4KMXA@7)}l=VaR'
        b'tR2~~H~=-VPEuY%^*P~?@n9vIx1)9#XiycbI4=@|^CmbWBUdA^62(5iOTJfpJ`2{fcGPl`QGD~A??rlmZ+wVR8}?^D19Vum%bEVx'
        b'?N~+rgR!!-juvRY-UsN0dyj59Y+z2!m>~`!x^X(3A-Y+5hi=XV{hY7gAH0LLF7!W}4({<1PI}1{N|ZW7dj5leN+S{U>|GxdAngT^'
        b'R-`Psn+n&?b~@zat6mLn{o0^2XmXHxbU#Q=R>EBp53$PGkcAUZ)8;dBcIGJsp_s<BSy{vt08L25RtVD!wCdM1Sgng9;Ux=k=u2>2'
        b'-$<LsIiw&3K`-9Tzw5ulU-o18aV-4D0Q@yShEGH|Vbm8T_M`fo;{AZkM5)5qZ&DV-{sG8!hkwc$Ed^@~l=d11B8SiXWpJ?e^v}?9'
        b'FkA={(+$+En3Mc#p?x@~4&vkR`+<<RLOt<{Bpdqv#$WOJ2j%tks_$K1?`-#qbS{D)$T-O-Zo+L9q;J;MOPW9yQ}>{w+YiRod#G0N'
        b'(|PH|TVNSVQ<;=p?X{4u{L}y5-p^bhS*|pZ@bpob*v}*W39DvBa*;6$RCOEP=p{@_G<YHc>slVF3vUnB1|-)|bz}FcOFV%Q?}57D'
        b'-r<AuQW+Dhha?exXdi!a!!#BBZ)n}C=wzrOFc7p?NDMj}viNWe?00D3pH84gn*{=CK8N~~BN&?`V_ZPIL<cX^{m91&)#+08I_@^I'
        b'h&!K{nPnbU0)Uj&>9CqQmDJ0QURu&_1&V$D8K~EP>IlXRfL=P_OeviXx`hIh0v-_owflQ0tFhNBksv<z8qz5-b(^lj=t6^X@2vkU'
        b'Cz$yzKA-$3Z>Gdv58AByoeMM@(q0_E5^qU-O`@uI08|H{uZqd5tRAj@%Bkvf`mq!<H|nr^<-2B9Xz3JCzlPX@h5+;fN*v<f1MxRw'
        b'DH?7RXhoho<}o(&ibyUBnlSPuGr;MHnb&pSuuL+@M7ktf1;iE0T*!~mEV0=^J>^Q`h9^TzO|yxa_s32_hx`~(=2D_msS7BCb8bPR'
        b'XAvEZ9`*=fAe&XJ6Mk#v2;BR07Q1414hT~P&zXNRytFjjdOAC5cxl<;l?$P-puNgyz{k6|BQp&B&K!<H543mu2~t0E$<t=TSLNhD'
        b'$T*spnWypIm+>Hv$aVqh(Pz2x`A=az*v)L}5eLh0fspkxzgNtKS0x=m4_-$uCW&w~y&O%-PIN8vS0da(G<bo%RFt@%S0Y0*7Jv1W'
        b's59I0HPiLb$oCAPbl}{ec_<!%#KC<O%XdLKjb+23ooC~^twHd97}M)@_Dzncmb#!z;}TT661i@8w30+e+L7z&%Ty6CT{^rV_)r;v'
        b'@*hNqGDx%|Dx@+U<-3qd4Qg>AswbQv12n{e{*ARB1h*z;N-7QL2#r+Myi24w&8UFifZ%QzYpeySq(_NFr!pb|RN01D_Ofx|P|E=%'
        b'G4pXYh@7PbJT9;FquM3}hLW=qG0v4qBpP+cV^c#HY93A{{jtebL~xeB5W!*Kwh=3m5I`-TFvKFj-XgU?$&Ag1>2^?^ELI6?ehH`-'
        b'&9Rwm^kmfXF2hc;*eaOoC6Ei{o1u5uRnw#hnuc07BbHyY(KBITJ`COV>sW{(A4XQw#=?%&n!sapENq+h1thi;#x^;@5Z^dRG@ri?'
        b'Q4Kf8o?*eY#EwIle`1I)9Ard13=Xpf8POp~iWQDT9ddmb)josxhd-MfWB|!Sc?Up-L#K5C7{6Ls3R_?SkEtu!(0nf<EAwH{wLdV_'
        b'dk)oZ2dT^e%L)Kyg*mln7_eT!+ixqYf_Sdn2}7vtV~9h|s_hOlX$Dz0%%S{0Gb9NOGNd!#0GdWb7cIw`m9T9idjK%yN_O0K0nU>R'
        b'8&J;>u4X@(M^rcfEl5v%1<gGF6a^;0%5jKb0}SFfQjf3^^hRnJ!q(h*fmp|8o}PkEO@G${U<8>Qz@0b*P<a?EdHjP6;d5Bw2@~-L'
        b'2auCOqfL6dldXI};2zMYf-AJ@kb}Po#xw-4LhTKPXmOZPA!`p!I33Ce%XNlm2LBVt_lZr-{3l@gUWZbn)7*p}H3_Q&QU?rwFd09s'
        b'lm#!igO@n)0z<}`Ky@NMAfp!n01^LlkWoQSTSX=lX88b=-|4UhOcZ9hz!1-ZN4TmG&%hyVxQz108UAJP{u>7uO&i$)gLB?D%@tvM'
        b'Bjd|x!QIK-{<GtNxO^*{6En#W3t!@Bw*n5H+WhYvd|NZz!A2D?GnN<Fz3DQ5c#*Y4t6_)@pwEhkHO-x+${J`Q(hj3xf-J=j)jSxS'
        b'43H5FuCfFMgwisErde477g9prVnt)DBd@@`am}iKH3z9+%N%N138?^2*7^T;B#R+pnpIPwk9BjX_96IDIx~vPEYC62SIwjVzf?jX'
        b'%_>ndO;!=hXt*ZXQ0;OCpD_!HR4W}OvlymDqx|1976pX&_hvI%#D9q)?rXLhf>BM`I1`GU4Cs+3XI~WIQk<7Z7idJB99{id9&|4+'
        b'XmCA5e7i4+TM~vmIg_|QXXOkz%v>#z$k&_nK+az;saS97=k<h97T8^vvO5<~_A*`Epe@o`o?KfGhFVA8Bqr%nbR+`c@iBNHCg>(i'
        b'iQ-Ffd>iiQOp|YI@m7kZtv9Xc2KRjfVUPJeoOdMDj%L<$<BVjqor?;=`q0GJe#a>N+pv+FOzA^X;|&({7MM+U@pk88K;A&Q4z??c'
        b'(^1W6K+9$x6(zdXlOoQ_Ytk7EG%_rF{Z)m8`ZHZlPC&nc{pj{YxZzZk&_b<)bu~ulx^ErHCi-b5dc@F=f^XF0!S*T1#y}^BjTgh`'
        b'Ajs$*s7ol*E!UvuN@^+06npt_`qYy%I4?1ZN4!jzkjRb>IzMb1mWo}u;P<9b-hHe^pfvgB0QWIJ&ZS;}#mdlhgDAt5KyHES4_70E'
        b'zTvCT4XrrLMcohcNV9KmLzRB$5Gv_aOHlTskgQ^`-jQ!HC3+03w%2O}q&M+R1<K!zRIWn#G;;lk)XF$?WHa*S3Us6nsf<MV_aj6D'
        b'U4=q-sISJ3tNV+`upaINA7BMJZsjIadl0z}e(gx*Gw*jCyy`FJd%d->8tK`k#B;QKvp7+TT9zSu`|$Qj6C<@h$mO7jcY5-VS3$eF'
        b'S5%1-o`bP4@vx`DtYDbUXMVs%rmlLgsdhAfyRAjqpO!I;YT=fE!0(Oh*v&}W9{^SK!%DvWCB1#3_EXLn4}k3G1T`AG%of1fE->0W'
        b'1X(hR#SZgV1K6=L#q-Q)c}k5%4X>ASP&^#s@b(W+iKO=1;9V&~DyHR?gJd#RX(+~*WYi{yZAl#9#AbIq%N)F@<n^ykP5_-<`E)*%'
        b'$iDt|Km<LSEtpRg>DuQ=1t^s@!0+L87=9QK`5vN;7nwd|v+qHA@?(adg&@YsA9TCsi#p^Tzl-zklEWnrff)Sb+mR~_3`~%?WE(86'
        b'cs35O+??KdUp%e&km+03?2Ds2K42`72%;is(i@wWE6#AKiOhZJB>&VV*fitQ%#n)#)#S-)=13uIOby~~2ZWa?JNN{^8Iex|5#zc>'
        b'#BQDTquP%cB*nnq6!6C8ZN3J27B5t6VWiVvgIZ)uW|x6FfGiF01FArWk&%{P0US&oFFt|-c-h9yj5PZzkS9PO!90qm8L4a<v;s(b'
        b'{T!&rQTrg}dV4FpC&j%ta(a6!0`JOUoQJ-7%P}T)c*!g}@^=P;>-Z(8|DVKk6Tp-t3l64(Dgo|N*`zP6nffQJW@L&XK4}U$)DVAR'
        b'X<`u78~fCc?js`?<&bjniA7p?CX+aeTDCDPokS?g8EN-LfMX4cfsw5!nw5qL@q{gVQ2uWjK#MX(DQNHCK?WM-A={^GiV=Ltm8>oA'
        b'{~V0{=2(y;TcKkPCW8zyZHQ_5YMo^J4wHEU;@CcGM)^|Z2Mx0*Sh4o@`MuG`CqVPx2U%kUpsMZLXX}7`vW5vpPX_o@yed}|gFc&w'
        b'qz_?nDxQ-=X}HGA0o7>LL8PN69|y$!H;@TH0Qpixcmb%))ZS8;gz_^P%g-4kAB|lVJDd|&uWe>xHT->{y%jUckxub|h~;Z@!rR&s'
        b'xiP?iL{(E0;O(RNW)ubMw$A}S0<H_b==uQ^^iAc$Km^y<>_oz0SO~>Y@CmKV6oU*0t6+6@SfZncJ-0CfnF6}5BO`!1dR9Ak*Z-cn'
        b')>%|kn~zmuPpW_CtincH{oX^=jwaSD_6&BaQQz2PNO+)8hlj7JhDZ5ccP9pPn~D)RwV{c%jm1X?xE0+d>WQYHP_4wcn)nipONrrJ'
        b'JSr59^XeW+q1Cy?3Dk?d`F2}-Zj}-qK(c!UP9<82#uLAEo<R>Dq_#Jil@BzQ0(iS%^(eJtAA8A&wd}bH#TDmzwi+d<hCHKW?G0c('
        b'8mAjg5Q?utAF$4~PWA{$sa$rIC;$Mox8U80zAPu+Xa&j|4My(>2NyczwGAmtoT<(jYnSk<TVe~h+nhfQmhFlTp6RAImAqCBR~7G6'
        b'a&OXAJoUrQs|k{7xT++_capkpfs%*w!^tGx77~XDD&d!0Lp*0IH<QN(o0mVp1IX*6oJxKVdZk@2V;`il8*Y)6o8R5w5nK6(-Pr~F'
        b'RE&CP9~+7*Rn&uxTxZw}*$o~E%n((;&xw~)srPcgxOD~TmU*VY&)RDvq{!76p)h}0#rrXiIG_3nEVPx>zR%v7`re^LW60n>#Z)7n'
        b'WhU3)8X$X_lIriCbKG*!U@a_wt~3xTyvaH1@GIAL37vBex@xWQA9v0JOT5sPBv?EZTtrumnla?y8M$?Eo5*CWuQ1id<m#qwnTIdj'
        b'dDjVUK_wN)I3auAF>cDA@ECl7A25z&j7B+Mcm&G>#(7qkojH5Sj3cAXqg#6xnEqI=oo9|@(q}I`y1?;BeVU_o)MM%%^d6}15lVl!'
        b'8AHa5j(iQ{qg$>rJp%TUC7|)E21#0_{G3iw@e(x2+i})W4V_u!IBM+;>JbOfhc)rYu;9!@i^PgS**yud?rFCM1n99-(66Rhz&+iM'
        b'j>I9orv|O-dV6a<l6N>kYik%AOIjTkteCAee~-PPKRI2QRsi(Mj7P%FN);Y?te^8Jn##5AQdKs|<ye|kEN5>aSF9gQ+STqlw_ZYu'
        b'FpUtcHcnJZ3N_VrK(&m@K}eq_F(ro-Yh+?r>Or<toSZBduN6V3efcik+p|DKf@9@!06ESr0MwV(FF&_e(#x73p0M^cJ0LCZEd=d3'
        b')59I(O?)n~3LEHHt8LnPL4bbrNCar#u}u8j$w6fSXdHW9?Dptvw}STA6moS~k~S*;8auZ}QYIN(Hwe&eLeH)T5;}}SR$^F)yv$8k'
        b'q#*p9v@~a08iw<?0MX-7r1&?EZQL3KGEpY!3_BbR6|v5Sz(S<F`+^Al=p;IlkN8F0V<%9H7OC0*;P(h^Dvx?tk6zaEASQfdo5-qi'
        b'tIrTq#nS3Uox8r6M){8*gSms}awTVTCvqhh79xfIfVcO=34AfKEC*Td8xKFXUS1Xsz&yo`0f0^)d-*qos|!hh{M~Z162SHf9P_gp'
        b'@9Tv>_hZQ6hl-R96IqgM5|krR^o&FfdLs|u@MZB2grf^y#!)s*6({l2F=UP)7b5wbY=->#nTdFb`e6qyO^y#=rO~{e{x||XkjAXH'
        b'OfY`*oq(6|Yt9^#rH?;w@X@Os68vEKi5~8TQ>g#1*L%B7-cL=A<MJNC7!NiZLNb2N%z?JL)mBx^`WVszbW>cqvrYHKSK2Rwv@9>G'
        b'Rm&ViG~DvBqD2pyNZ%3p3R5~4Q7WYY%q`Gu#b~9#FXSIy@hB|}%gD;`zB0&K48mKc>^&X0?NLrGX*4S%4p!kYNMsIj(w81@Ogkwa'
        b'eL81wo{e3z?5fqRbI;>wkiLp<HLGtlLlgcFP%D<~(fDc$JsKgrC+3bm)m0^^ls?>V^@sBhKX`v2JS^`KrT5Ta+G}zMQ;1ME_CjFM'
        b'C5n&oKEM&~#Q{EqgWiGDdE<`lKXtkJs$b$344NfgmV&#jzP~rKJ9+?An$_eNoB_<Hh&OM|Iud<Gc$!`|ZW~^Jp3Yu;VFCB>ql*Rs'
        b'JMh+m+C$zr03~PL+C4LJGgSZCW_fRIr+|8=nfAf$z!TPXt62beP|o{u_pXCqPKhe-lg-&LFG9b_jF?%(ZTJ~J(K#4w2CT2MT~~c8'
        b'H0O>rL*LSE(Lb43A?Xw(wnubY8!rY#NaNn@Zoi1r?QuA2LF<&aQ-ybV>XGI#o>h?3TgwK?VDAlTe9z?3&|gpDgSf_51D{jbvkTD4'
        b';KlMB$nk6*ePzeNX7!7E$;1y!;y1}xh&M!D1VUTU6KP~ILaI@N7YQ>~Pz`&1t<3{`Qn|6?GKt5GiF)7-5NS1LZI?!4ZaY!mB=?AK'
        b'ZVkx9slvlgOZt<C6F)iqh;TUZ5*~5v6em>(SPj0E1fsSy2TAflkJGsPU_Gto3_!QYF_lHd>WYe59q$L?h353lo0O<D;+o(0><Ex2'
        b'_0KdHuir~1bZZn90K>dUBaY^*N=xD-Ny0WiPF3vnZEFUiLydCd<T&X)D-U=9ubv1)PRZQuM?T(}97ymV%SZ?$yi)gwe5W0c+5Sw_'
        b'^AaQ?2YJDlRtNCdeyaY(@PHZtm<W*=GDoe3@mk{NiPGkDV+BbfeqW6={R(uAa1^eE`kyzG2`>XohzIs+NPS-9?hrnto|Cg3lP=*?'
        b'kL>m3L!3%LhyCpyPCP_fh>f?Ox`jtW`29XGIq;O;-7TQso|oWZ!JbR-!=6ic1@v1}*o%Vg+p!uo0uaZy?*dP-!xr2_^X)le;a<P*'
        b'nRJ7mNNHB0Is>#9)h9L=3qY5B4zMH@hQt=sVq!F2L{p4t)Tlfz4LpY#)>D$bK6x{se9(7_zmfqj2cQau7WAFn-F~W|-#&yl4ZbVB'
        b'a%5-ng@jK&%80v=aH;OmW%x3<kh}=HZ~LYC-T)R*b1uLRd~pHn!dy9_2J40{@B<+LU1(6EeqXKb!dI4GhVHSXtii*fWdpt!UghRA'
        b'r>q&^P_jmN@OQ=TyuI&AIdN+rUA2*{DkpC4BdeZde@lrQ;CBQ2TSm---(LWN#03s=5ML^{)u-O|JDRc=mr*)cU*j(4=liU}(W)*X'
        b'oM%l!w_9gpy4)k|omVSL`)Y8sEps91d!`|P)4pc`@i!cgVee>txDQ8Z<ui#(uhPnH*4&>xgrLstqm@UbUAJiE=b`xOW>7lf;l#{v'
        b'v#+KhLKeF3<Ew3mNH+VPg>lF`>?FBKD?kW8c&MQMvd^r1*+h!r2@LUjkfetf(GP$J1Jw_{eaL5RDqytbRJiq+g@1_)+UR9Oi`~46'
        b'V<y)EnaaEhh~Mod3dZ!arr9E!Q1)H{O0MD%HapB?hXLh+2`{k;mOF(Su#s=?=n2E$;>UYXJfh(^2Zwj28?xlI7ok^ioOO2kV-77m'
        b'dfggfGSwo29EZsn1kCzkIXi_5u4jJ%)bcxVZPcy%27r*x-t)o`Rngvb?g8m*Kwi({WJ%JCv2?XaW!eYkj3KVOgsiB@6<4emYYgD^'
        b'a}Bwv#86Q}8tx=+(!@PeVla&ULlbvIw{8Jp+6ReS3i#K1s0K4jH{aI0%>XLXSJ-{q_CZhDZn7j{BOqXC4#b8aJvCj`e(F`Xy))VI'
        b'8_b~Q7~=d}vR4@5UOD`5DlYYt6_AQ8K4`TpGQHa3Xo>Qx5s##5KYI)h!-R(CR$?y$trW1q0gge9bo`UiP2cKN3~-EBm~A3mGI++v'
        b'4`;q>)RREzJ$TU^QHn1$*~J5V)A1H_L>XW!rf#u!YyDOUTx_k1*ne(uzl=+_N}#fbXx`&$uu3U56P^p2;(K)80H#l|8yf+S1#My3'
        b'EZ`a0Ja;=D13C%f`>s#=4z>j^u-c0ijYU@R%_#$EcuKGZkE}|*5ckPP4~O?|ln3H2Z8?dWO637^Q&ADtdrDlQ7T`F(xcABW618w|'
        b'ADE`FZH?M42HAaM@MKyA;6yl>rpCX|!4njC&VPud?W-#!IjiJ7XkWy>RNlEg66qvA$31w?BPsO2TSW(kg(rp!IVGN7$Pb#@I(UPM'
        b'K|n*n9O0vdp0mRs*Ki@)exP)zPJ#Hha{jIK?rSAw8*|t-xsde*w>RKDal)#JMhZ2WQiO!JKR}*B4q1poy9^4!@7v0`x=Au&k=yj2'
        b'V$=SOnjN>B;HA4SB2jHSGC9l8VWpq)+PnRErDNP4Y=GPG9is^=D+CE;R{go>B<I``Q`ule9TYjw)k%Dpn(XVV>wwfbQ70)sv8!<S'
        b'z*7O&Q@y92I4+TXBJYovz7UV|YP?KLZU8%77X!~EOa)NrvqNDqr_fa6MFL(nyyfX*v8Z+rqW-WcAre)8&}8z!w%XaYo+wy;?oCO>'
        b'$-#3cCDkV<-j$ra_^#*O(X(gU+Y3_PAv`J^JFW(LinKuFN72Ktqaz6jjdJsjqn3E2U!5~pJ8?kL*W1*7p#1poV`us~M{bNKc}E8a'
        b'2WyKa;7#9y%dWOd@IQ2W@bEAGf(FiBKjCTr)XlN!@o=bD2obA3_W79gd0Dw`^+cD%`TM4BkKa21^2;D$o$z%Ed%NXb!oJQXX*>dc'
        b'{RC>(^Qp~t=&JsZTygU1fT)w8D(vhvb{geL%fkIAAE3%#4p0pPsE#NR*u8AC`(A1aw*0`Z;{f~rz<K*b?e_mKoMZ0coR_ucZl%8M'
        b'p-S8TE9$$N8l(E22bgmq<`0E1?>GuES5c}U<}r0{Nlb2D7HWBgIhP=*AP3Kp5><IqwE^C>+C(N~l9kKPDdABt_+V$xF6&8UCRw#S'
        b'UxG)1)jqCe*;SxUDE<c!TY1q3a!76EQ^h^l*g`;Wqk!HvLVDW>&pKk(k8EdR>a=xmzI*@o!qM2m)#t{|u`hM!?!G<1dv5Q7!m-P_'
        b'$ga`LYmo5u;kkI2_BWw@l&cy^TCMzCo@DzTI79TRrd@E7lz97JM(qjZWC@K_@*>Xv#D??ysT)g5fP4q$d}6zFJFArJg7jIaC9!^>'
        b'J&-U0O6tZQp@;LaWDEsTG`l@ME|H3EnPuWHrY`xt{pFT!t3Miv>Gqc*mKg@>X`cyfWs;KnpKL;LG;u#_$wTyH6O6=}2Ytzn<RT^f'
        b'(yKcqX?5~*iIVMXk2%Adc99boBo{w+FO$Br*nj^<dcg^4_F}1UF;I)}MO~aEBHTmXzY$2XW5OPRZHGtoaq*YxAM_9_6q(bfimW?&'
        b'7P(d9#Z&52hCqb)i?38?h)#0ilw{~?<B3zl%hOH+4R1LTSgtyJ66)4L3B8}={o^1MWB$_8`$st*BTYh%wYT6x`SJR;1Mm>EtsS+b'
        b'BQ&URE2>RH==+}>m%!-FJp!{n3_1;SVDjUVA=(DA1dUth60voMv|0#9A=s<6Lw{=otYX*h-LskvPgX{6)V+eG^Gi3hVBzaaw54!u'
        b'Ea8{&PcWmKO8Djceg?j8<i8322T<%>j~sxa_1s{KJ5tFx{gisV*sZee(EbhNN#~bsXgLn6D$`zJMn6yImv3n4g74+*#i?}u#tkhV'
        b'_`Xs54`%lanG1$}<TEHQY(q<=V&ZUP(MD`1SkdL{)1a8S-lw$42~56TE^Sz3ZBX(Pqfu=(q8yQG0JZk;gCVl)3#<)0Em;ZMcVMt_'
        b'I|E_pxo0H?K33GgZbO_bx9XjZ>?O%z@5I?N_|o0;<2bxVcHGx{BJJEsvA^_5f9Xc6;5eS3<RxT24mv^_#i4duHBpFp9HpZLIiNdB'
        b'1)8@e%|~xFU=f<PX7Dq4{h}VO@oNGspVAXIgTTs5;U0i4pvZ)4QjOx-IsO$OzP9E?F3@<}@*-o{r3y%6D!mm~qyvF~D`PF|Wnk@6'
        b'J!uW5KxnIE+F532+X%E{;eW#J)vdGQIJtb|>4=}1mp_RwOT|s8E%fqIxv4f4ccixXmv4|ez@s;{MeeO7mzT-MS_b8{@IpnW9Nt=N'
        b'mqSOwN%Cb^Uq*Y-pfwwut7b`=B&}3_?j=bPyPlO>ovYdYD%-hubVJAngZ7?q>^IeT5b5dLW<A$KOkQVR#H=be5mx=l&G@xE568_h'
        b'dys}>W6osj_TE}^(#9Sh$f*b?ttuGggw=1GL^_cG@DynC2`aO3sQaunrx~+yBPdeTA%_J7|6X8pm#*O!j3I&`?p+R-IM4G<-?GLt'
        b'oX+I42LefH$FlFElT?SZqI=niG$85`SS4e8cx+UD6OS1A8xs&<!J3UIX(qUq>r7{IARZK4M#qDKOa5=cv)AC};oWkRw+T>g<a$VF'
        b'o@oI6ODjuZtS$Zkm(_%SbRSwh4ZoY?H#A!D2(W?$T3DBR8-BF;8?0xdp$CZRWn)-cZ|&}x#;t%IhqUV8_wgW{U*M4E<-9FVT#EfC'
        b'tb8;b<7hBm&I;4$Dx8<fTXr=+UG>r40<PjAMtb&kC;Hhx_g)b3hD97ayrT}fE!=g>m<40~$ZqAQ<D!C9`I;_n!4vtY8RH#}4!1_&'
        b'F}64bm+|Kc%owL}TuI{LNh<(Pn&iN=f_gUM3ya^$y;gy=Q_zXJt%sMQmIr`<F2-ZrX477**P7;VVsMUGeGaRfUG@MAp@rzspZ2yN'
        b'z+<45(Mca%9J>b3b;FB46M#;SnEc6^hr=bGH8l9S$c6hWq%z*QKg#{Tt_aB^HhABz(PUOGZwQz8e%oM<<Iu_agy;;%NqL}J-$~+^'
        b'6Wf1AauKSoL7s+@(e1mx4229UZSQ#Zd$!+p&-Zqxo$D4uxpwzlZ-1KOq!<Q7u)1}b-)X;L5d6a7^z)NP39o5ZYQ5>)+yE*JEG=#H'
        b'!;oiXrF<BeCTIoLONz;|(vc~4|Dz7}hxJZ>XcPYb`-2psce`MyYOfuJO;29leFXGR1neI&IWsX_d_EWU2AOI&C6a^A*k%ZJhRJ3M'
        b'_6Dh3o)|8nvK!L598$SS`UFP~dZTJn$0^WWwy|>1*l(HL-}SzhCO;_#N)KqN^%`_V4sE{I?#<*jwm{V<WHYE*z1JM~j5L}7?8w}r'
        b'mRfJeMrK5a6JJBMiAbdZu3Gr#8T17lg<BcnO0YnyQyYBQd*uPSVw6aazpKn}5kP4ddDeERmDiaJ6^>$aoWRtKnbn+04}mWQ%o8^C'
        b'V;?1Ike<bdqf7Dd!L#DQ<1Ih|2}GCmc8l@l-UBTjiJybe$_nXpxZ`CxT~%RiVRaq2YZOi<pzs6^Mof=gkr5$C_kWoY0mD}R7(uMT'
        b'7qNE$RSZM?#zgnfn}&NqZmcs|+$T3iF{cWBQx-frkX$j$K_G5!U$0HBYea$uSG`uTxtfI@G}nOs5MfY5q%&@S(;;Pa^EblDO0;?8'
        b'2oq3N^bUx7yIS1!Ks^IWnnyA+#_XOycQMWJvKU6+X6I334fVa<Ef^Ih2^ycFrtM0>D4Hdpez21QM0bHhdO2i1LjB7^d~Hux{=|39'
        b'o^C*h@9bpNPmGT5L%iY+A1GX*djbjZ0gdVddjYp&_I8jD{KFpN12Kw>ARm~VyZxx>ls#XA%K#fFxyuF`&sZb8C*<Z$oQ~n!K|XL$'
        b'U`<z&wiQXwz<yH<fn=<p9)^mZ{Eo4F9z3@?XAk=H^~<TK259q%k|^k4a`=3>-FenNN~Q{rOxfe1Dai17d1k%x<AXCjC?$k>!@Cc+'
        b'EF9wwV6gN9Fr_hDc>z#p@D4ppWh@|ddG{Kgy5D~IjYz5yzCR@z?cO~zC`XbYPkf4_KWYa&yW&kbwW%R!%tRUBgAtl8Z;*ub@F*XA'
        b'my%eizeEvvWibx@<CI|~hmbOE37QhiR}Qn$hOneKHrNW_5<QU1^AMbmFZSwM*z8-{M=aknA;^5z?q1bmUyCZaqkjAbE~6$PlrFB4'
        b'+nBD}YtJJ4to9y^nuj>!&;mVppSQ2x4tn4kn;MOyUL_348X8l$*96<W!@{~u{cTb?9+8wCEVmXVp0l%YjI+SVBPlb9k$j@ot^{j!'
        b'55@+o*JU%RZFc2*2Lk{=FRTJAsci3lWML!E-2&Y^$E0#CGk5s8!Oq60_6V#%Jg`>X^WW@4fS_}kIaprRz2ixHopfQ27DkYj<|G6o'
        b'2<|AhgPE}Xn4B7hb?dsZ9go}b=%luS!zFnsJBsXN7y@0)0tr0MLME((aoHcYla=cl|3Rz;NH^Au@dhw91Zqf0Sqt}bM%df-E8&)y'
        b'6ZYmdku(`b2&BG-P<pu33-EvUtKr>#5t8yln@l(m*2Aa%2~#Pd1t_;<rI1vv(^QH|v?<SjSQoL74Xauw<M(ikPcG;h=}WeQYWBkd'
        b'm+U(d?06Eu)WKp(EVJ*taOw2c3)%}z9|5!NW!qMMdq=DtFMw9g*O=5WXu!Kxq<x3E<J$$J{`peSGc}qdB5=Fei_&OHgK&}Zf=<Iw'
        b'XajpxsYQ?^QOHKLA9^y9hGRpxy$7e>gix$#pTO?!920d4--+o8_X|?|j|u%kjDDKye@tK<x1nG{qO>4o$yQYQ`E7TnTPS`0c53+D'
        b'`8Q>`=To}}oxH>}%F+u{LL?SS50GIbiS)i^_LJzR{4rkPNyTTPM$zsQcYN3UpYI)~|I7Dx<(*{ONwea;AAcMA#1`-}xXd^#Qh#hq'
        b'6?Mf+Wnrpuo05C8g!ss|`vxG&ZrD#&?xized_T0Yv*nWL{CV5Zd7JM%C|*l_Y-Kx(`UA|_$=!W}8iV<)@x-vrn(wZ`3mw+sqz4O7'
        b'o0%GcU+@K8QJvhe1p^DHw{3T9F3luDA4W`j-T)l~s0T;e1j5I<JDw)+=)3-edQhU@cKSQ`OD7{~wzNcnOr8{%fJRZT+xh}F;&q$J'
        b'ChmPrEVs%V4urw6h1X)!_Ph}|jP&-4hYtZ&=JbIpjuWo5Y*)r3pR-{tCGA$5D0E+m^|P{tu%g|aUFbdEAEeBz#C2B0Plm`Dq*%vC'
        b't2%3_x;w8^qdWcNQtBB?$jdV*cgEkj0(3A{4SQzyob8TG>3$;JAiE?yZ?g^AY<+f{&u*g{U@uxXjdq^5+J^Sn`WkGOADH}CMh~60'
        b'*oI8DzL#tOMThHhW7qk5+t6-XU%d?o3#L7n8#~WawxK#(A7uj~Pv<i^c9`^A+t4$%zTet_N=Kia+dT({Alz!2%SjOiUBfn<2tQwE'
        b'8>+VT)!DTF%UD}R`_DgX8>+PRJ!{i`0;H_Bj*Q#Vt?x;dnAs2p_y*w7lQWE;lm&*x#u+A^ly$y#v;2IuZK%xFS8db&4+EoKN?u~U'
        b'D{^(&H-oVdcWXwn5Crg45&Y6sqf5R4bSQ65{OG#;&vQ&s0M#dLL;1G8jW){wb8wx;ur&WWvzN*1m!02W8`9YNHrTYs7;1hGTk%re'
        b'{4Kz64(4hMF`78>hw+^AMYf?#Ti?%ZBRvdaHpGBlJGfb6h}FbN%&*+e>zAA_v<;=%`U-584o1EBB_LM8@5?lC5t+~Ay%upk*EXcI'
        b'^{ui&Q+=~x8UF_$fn}MqXq=nnPd9`QdvWNvcX%cB14IEIW#7`MYb-*;`S2PEH3MIQDgzs5-W(+2h82?Y_uGc<hqKHlu~7@zF-`|R'
        b'ugb#DCquvi9|tISq4{VX20X^(a9t`(Yf~Q-o+oWXq^&Q`=0j~116dNXBF?@d&E&#`xXjd5FSc`h6MMWX#A%uGtl@j-b)_}=+>*b}'
        b';pm13Q;H4^hj&wvaGotshE@vkgGJ;pn63+95|Cu&>&@QW!J^zj%_bz|7sU+(GNr9dQhGk|VU(YTxSuaiOgxTSa*@%8dUzvh<kVYk'
        b'ZYr;>HM2j`9oK%K?O5ve<)GS4$1)POCk?t+fXCirgPlWT=!xUh3$SynL&<f?fU@Q52l?MHsXRB<*7}qFD0e(8Ej^a8V7q5fo&-y|'
        b'ALM__Y(F{JOK!4qI)Sp+@KA=k+;Qykl^bmjr8>-)P4wWLY<%czp^fmU#=-{p6N?Zl;a2J9`JF>@<zRbv*HC+1@_PRJ44EuQd{}aR'
        b'%sTX*HQ;^P*K4JEU_VZkTP5N5+sR$zMBC+w%iwQNxyx~SQ2xy(fQPcX{TuK!{-9E}6?-S@%lHAfhw-Xx!TAB}&=9ETIe3E(k&6BW'
        b'$IXBANbnqZ2+`<;nm8;-F3<Z4)LVy)0Vdy>Q|Kz7aBSy_JXu5)l_y<LHB)4FRaCpSWTKiQh+(*DYoCF@DqfXO{)Bj}y)EM@Z`~li'
        b'mL3vMaXb4ymUuX~!p6`5>&{%4jCHChKO`ilevkLnG)K4CN_DAE?W}OU;XjOcyP%=vvG$~#jzRBPSH%g}v6ajEwpoFM-q!+t<y+eM'
        b'yQhN^gD0-SBPlG%d1KH_2rEvenNEsz8^4$9;u3hDn2G3$BA03XCNqIwjzb=sv-&#w$|N?<F6L9-7~1hEqqE;2iD;{DKvXn5Sl&sg'
        b';4oJoV)u}st%J!0G-b0Mskko37qWX`=;YVTUEe$BYpg>xR`F+{7@w0jnGXw*<#wHbV?KJjK_&olJM>j1Cho?D&?Dwo82?`d4X&s@'
        b'qm}fc)cX)5xjGa+;sO~{kt>P$bm$k>uSGeZ${|GK_e`to_W6xg@1Zw_lCA#L$k&{6?}Ja!S<5x1wfv?x{*81$nn8ytB}t3nxTgC#'
        b'8T1ja*VVO{|7GwlNhgZeKZTOXvMfpZkT{DoUNaXpg^h^<XT|=rRg<HjRih_*xPiZ79SDI(hU7+qQ=(r|LdvGF(wA!VQiDF)eDuhM'
        b'pQ0n*BUMow9!5v5Atl3AC3*>vSXb8!$^C@nc}|(+79V!-0DmjB)u}km)SO+{B-*kh3}52i(xTI5mq|*7;>$SrqNylQ0ACBTE}DFs'
        b'0d*{SnO|~towu!}XiG~)nYctB*(B0Elwmk}WQ%N3sk4fzFb-DyQdO~ju;`b(38SRCHfH_Ku%aStV!h;fZh3A#hARsqHACX+%~jfR'
        b'*VZ_kZ`Ma`U9o$P)-P3uTk$oeSbo&r*LKgB={5Q=vp%LHgKH*YN{C1RU1-opbPcT)l;{`lzE11KJ)m&R<cz$85Z92h?)4>lF<wwI'
        b'l;V+;amMRr2teBaf0nE#`<YKgprV6z&Cw%y%TWGN1jjV1r2NGQ9;MMo!CTXvLj$~FF9zzopqDAqxLre?ebfY;%U)etSsy5UfslP@'
        b'4AUG&DmK57Qz_PTAbG6|LHFmcC^Z)4Ud9*ad{BSx9Cl%qG=GIOH*tUqCMl@SxRU{erP&<ijH%EiPj)3np;`w*gzW)B1WiaAyEKs^'
        b'Q?e_E+(eckA7+vyc+Gb0o`QPzO9(FD?*U8~?xDpf{vkI2Nr8wNf6hRNtGf>mp!_k$a2P3ay;0#2`#TU^i!XtjFa)wyVi;0x<<Oyi'
        b'c<hHU6c0Cc20KDm{;!?Bs-Z1QQ2qeZ8K~;R*93;rI^^800BBripSY4^{8V1CJ`I2|6A{(jReG9OymeF6j;<A3pV@uAY?b*55xr{3'
        b')}a@%CTtsTZJ6Z%pk%<0!v=&9(O5WcT|+UIej*%><G38magcQQ%`C9O(?d!RCqRgwmyGWMxShBTaRb?C(DT0!Vn`D*>GV8HTF_N3'
        b'jHo27>H`8?MeQ4oHnHv<j3y!ghiiKni>U;ZK@-vaeU7KoXktm5MOnoK?cS<>Z0puyKcO%X@u2eIA@KwsVJmN~{@<!T-9^D#{)^aJ'
        b'!3fa6{fCglo@_r6fz-wAYIithX?=t<v%#0y;Bdjf-)*e|{ek+5TseP|Nx+-{a8A2xOO~~wPEwc$$;a?2vIX?}r_A;Wti~%a=of>L'
        b's?l?5hN5fq2*76ixgU)KKnFC<*bFHHG;ri^41Xizlr>b;rnQC15|UB=$4t&HS4F$4?HG(!sNP+lqm_@m$LyZ9Twsu<1@NT2Qh;iI'
        b'!{nu-Bik7B_)YDv;66REbc#D3nZMdVM19QtGE%b%O^~7^tC?>fZ0LKa!S_(Z@S(AeGdN%raEA->9%%QlwYF@t;q7R6srR^CT8{XS'
        b'-X2*Plu89AO5O0r3UeIt8QEag^Q@8Q6%97Mc}Q%NP;m{nL^jSCA82i8l6vw@W_kPW@tE}u!q<PaZ~?wL<3%nXWoGo8A2^?eSheDH'
        b'=8g|a^?%?n*&D*a5)^!`EDAAjt3PIaN3Xo`1cV61zj;P_@#cT5kp;do=QdOmk2J0(Ut!4gh|;oS-jcM5Oc0Wr!ur0kKrxb4z`NJ='
        b'eP!w4QFHL6i|SroDO+deAt{#=qd#iG@TGm9TY3bZA+tW5`i51<`uhIY(yaud%~$aCYms|MD#I$1GeAZ>r3d}8kMcl2sqUevzALhD'
        b'&!r!hYxti7tdvwG+0%E?GKK<Zj(XN!;|I$nCdM;u9+_lF9wIe_nF-PM_%}+bkV^8`+b_DnQbfKL-LOnXy=|%ZR5H|JkzbaZ*hPo0'
        b'a4;{5TC=f$_kp4gIW=a68Ui827kTIEt<)5CXL$Z%Isa!17#|q_oxfFGRy=tS7VJiJ)&DYcm*~cC?EWG(Y}wUcorafAfqoC>W_V>_'
        b'D0-{DL(gmz`H3j#aw`m|@;vEtJUpqwgxM${-@|R&abI9ae4KMj^s(e?-dIp5sWR(@3Ik(xUTF_6-H;qL@sh+%l?;jPFO>?+@7%Um'
        b'TBaGKUk&O7mA)*(Wm4P!<Llewn!2)uPfnhMqfK~31k{s2ARu-^Xe%)F4n&HewF9X}V5Tz!1c7P|;f<l>1cjjXUO=lr?MxC)1x7{^'
        b'tD=^fBq&7-Gk{tjl~%D>wA!)ws4qC*-Y0<Cdw<_Qkh33auf6u#>#-kePqe#D^MMIT1S+ZTymmZ<EfRXAqAs-ykW!o?L1PLPL!3gs'
        b'$AvzEBha!2U>N2$Myz=Qlhn(EUN_kx)G9_&OnSNn*qc1#lbD$MF~(MVOia4@3@JakAZB^ykda{qs!)Yo;$OYb@26w#0PQA|MM*ZA'
        b'l(!za_G6cuVpiMXrFwY3BvvNm_bqLwv*rT{$Iy;Fdab7UjZUwNftSCzaCFhp#i8n9yL1>@mS!QZf7bDTUP>muCcuzfOx6o|mrE`i'
        b'^eWy!1T;&5v+Qd=MLHKUZ40?)+REGPKaAMVjM&@k9c`J~v8zAW9jmK5V_O4TX|;@-Uc;<*)RInq{e+5732-Srn{x=`t~>gcI@_M4'
        b'%-q22i*ILE&q9#W?)te^`tF$BY_|sBINfV3+ui)eNWiRRzs%Qkzd01(?hN2|amr}p-I48RZEV&}(h$474MNrapvjy)lKBdN;8s;v'
        b'f|qpzZ8{$C%1|)7Apo-;CGJ+(JC5<vOESM$G2)5VzgnIC6Tj{!y!@}*4((p@Mj1bm*3SWU&>d2F>xtoPd0e@n_N?I^KoI=6$GSiw'
        b'BLTC4Ae5_+ehwhDIEL)GPlEZ{^Bpx`X(H7^5nrR{7m8F8QGIb217nC(A$nElB1SvYrV1M^#BIW`<IOD*`;V3Ajdj>cU&AF}Cpv`-'
        b'$LJGoVEp=W8dR@ZqJhB}Y!(I*_n;$aTrIW!M&APTz^fgr!ElSfj9AgCPz9P*0VBPoLqH`6Bk_Kz>E;$)AJ5pwQ}(&(+I9-I@{hb0'
        b'GWd9l<M9?#*B0B}cZg%q2D~u`>f%P$n4m!wxGmeg<WqM_e%e3h$DFWVJ;4XykGBAjA$hfFdSR$YDAA|Aq8Gj?N}FBVEE0z3g(6WJ'
        b'ulBM?xWx8V7%XiFY16Bgh=c*eH(Nq(MRA*aQ$us3%a&g{e)Ei9+#<}Wiqxy#bgDv}s!*p&(&bit0`QLs#bzCCMp=Ib6F$T&T$0|&'
        b'2d#kq_s@QE0!Eh;zPihIj^N2N!RG?^IQu?+Oq*Q<G+!IP&1^{PJgx^&eP>5<^(u+p_mxIpKxch3FC|p33NbY2M3*j?<bhUgsz5_q'
        b'=jE|8=Fr&yNt;Rp$Od{hE(`=j+7k_Wc(-k5O*9NPq!&tRj>8K$clTKY<qz~GT8%HtI!~G`TL5PJ8{xaU_H+E0VLRyc)nWeSi|{p<'
        b'_E`Yu5!Iq`RT%MGI9Z~&GGQdZ9)KPfhNXr^r746Gnea_T+H62cg>cDT-Oi}yyH9q?gdrh$I?@h^8cn9QjR+SdZ{Je398ecy`$=?U'
        b'K$CB7v`7`IP(}L1fo_hgLYB-HR&Ck9);{=@9S@y&VTiG9XXmS1+tS<kz+<t^MtbMlzM<Ps&^nIe0BJy1fZdQP3?S&D>5woCG_<Rn'
        b'_SH|y=pX!s0iPK=b{<`FD87lrxU7BTa~W1vA3|VIeg!XPVB8)aXwD0GT55?MGw6WJNi@+y_<6tFVXDvBDe=<_#m{UYey)@o>ig01'
        b'&UQC~4MqC)<CrHVG6w90cN*s14K3-pId!h0S0t70w0CE=pr>h%JjT2(GP<}~kI23@iD<D03-etpqhX;_@i#l^73ji+M?@v&U|-4B'
        b';NS8G<F+{Bw%Ck+F)_9fDCBNQUQWQph`bE<Y&>WL&$jn^N<!0bxMD5Bg@id<9Fd@cxo4d0+uC;+0P3QPFHX94(H^8S9z~3KUZm$z'
        b'h5&r;=|AMI%ZMOvLUix|b%3u21_pKA2ZwiSv_Gz7wX;8Bmkt6O>8O{Wv-;?3{6Tz+0|$+qHGQ|4xB_)#XK{HO#@c^EGw8R);R~|P'
        b'!DD*10OaV-9CH9|e`JPJ<U16`y?psX=NjFx{ZWK^IMdi-?{xIfYCBjfyu>F8bx;iR4Z;@B&Vb7XklE<yXe$6x_;OR{-<lk)0RtuW'
        b'qs_ct+AtFuCAGrQ+oVC*7p+|PxSb6N8079gII-FBWV6lqbM-~IJe5dq$;%Bewu}I1t)8H3(7p+v0sFQc1>S~}mkLB8HY@9A=(Ig)'
        b'iGXX`;`dR5XKO^7q1F?Oi3uL*NwkWC@lwymcgxE+pewoS<pyg>RGe^&t|b7M@Qh|@2tnB4;IzhKD}n6_Re0880MlT-a;Bjtr>TDE'
        b'<g*IKu1FeafDWuC%P*udnvp;x27qx<@3RLj8y^?b8jLi(!|TbDF=k7B6OfuiUq0(+VeYloCR5fAlLl*}sqfaXTR(>ae~)x85rhJR'
        b's`@8#YHgTi79la`@P7JKa96~&4k7YQS)1Uw{H;xKNvlSZ;_MhRwLX<-^jsG8hW3{-AfqTs0Ehen(AP>|0iavTa_UUu4ImueKnANe'
        b'J6blI)&jEj5-K>_E6UVs?G1Y;>#{S;vzHxVDo#F1%FYDbrNUM!96n?8RN5urx<cz2Xc5adlkai2FV~-0rA*+psDQR1iZ)YgphkmK'
        b'caUkm%(S=B((`ar{N`GRF&l3Q$W<9XlM?G;DPWPb#<oOsF|oI^l2NSsk>?n_HKH{+m6pq&K|Sj{K;7U_F6X9zj`bC-NKGYDA`~jO'
        b'994SK&K0YhSEqU=@6sh1c<BbI_CakxY6R<_q%w`2v(!K=JMzJb#`GM!_LnA8^=t%bBz|dPG}f0iDX_U_xa`uzZ>6pHda5@~)>?<<'
        b'Uz6_Hjn-$;?d-bKIIwm`m!Sqn1-H?Z{>Z-jcU`xGb!+XKy_4$f%&m|<nv;*f&lT0x-$P~k9vANQ0s9~5)v5QGHlY4}Nn&_#TVbSu'
        b'Hi>JM@Sd#|W11Zj%aa9yTZkx#o4jnZ5{3Iqz-80~`IgqG^J7b1M_Io^I!)~iztvaii1G}p)7lQBMJhvCPKN~G*3PoXN#$~;u^iX)'
        b'J!*~~ApAC`U*J1#RgE~Lz(@r}AV-c)etj9yj@2|T^ea)T@59p`#(jqy%&1X!e|NL**r4D~lNTL{v<W)o$#&N08d4BVU4znJoK!YG'
        b'6J$K=bhujHI%yNmf^QGd5g6=QgR+9=up}tl>qSbP#6?|F39n{O2;sfC)Tt}sfrOgf-;E6k{yvdNyEp<HusLHOPRXPo?^*l}a?B=}'
        b'4fD*;^G1J93eG%@hjt0{Cx%^f0GHz;BW);9&=5FBALw(T$xjjJoi?n@VPE^M%6hfR^tj4tPRP3FzJ7VNC*p3<ul2D7&aK-L>z4|T'
        b'x~-kFb(?_$4Q7R@X3KF=pm%7KD9~4;$D2l)=!!rA=BW>yv&N@TCys@;(iTck#3u&XYr@-jeUuCr1^W0I+(r7eb3|)>SocXqpszV_'
        b'Ztvm7Edzh#*A0*8wqz=d$k1AEV5{rb3P6iQHXLf}xvF8bpV7_`e@CuqMyvltf_4>a1roi&1q#@=7`OVyluiLWu;S3@U2-K*Hp+4q'
        b'5C{x044k4o&cs%3s~V$saa#kRwGSK$hWTWUW$z^B_bF<0g%EB6Q&DHD>d+P5z9<j$HSGM%$Ez{G&wzQw7;yKdtxdYx5#Tt~24HcC'
        b'5g12%KXGa8yNQ{J1@rDM;<6^E?s5aZf$L^tq%jS@l4cV!fZPz*Pr_F=XThbLX0+#Z1ai7Q00RcaveH$+Bn1X9QCkJ9(uNSW?kC)D'
        b'^R`1Z$I$9v1oNo{c9~Z#ZGzDcENSsl^2%jw9!MFBg}nf&u9<GxMINA5hI}`@$A!;X=z-8w0f|0)x;EOy0@E~W=OhgDAU{bP3V7wh'
        b'=V;F`2?U`{#O~c^4)7!{!KWe;<N#%PCNDt&K+7}v2^sQCkF2aoNo;I{F66qTJ4S?ubjSZ|ipQ>#E4dlnF)a9u^0l|ChJ*~qx+?4P'
        b'D$}|u`9V_rFL!wcqvse2W1FX1Q@WQGElII9o&^?qT5Zaqoc&3L0!6UL7jK#OPA0t@Ys}6BPC?D#xhXYG_Y@gEP@`FHkty9*+En9}'
        b'>8p9E-8t4=B89lJrNvrJM^Z{)cuqvf)#0o0)NYq}&*>)IbUGz(`(e<E;a+J;i4R&WLGnNUaO|u)o0nU!RQdyqZ=XN#4@LKz7Z3IB'
        b'O@&^C`%hhf#G?V^_T!T7*awwVH-WbYsF8jI&ssgH5c%o@W~FSYH37_0uBSSHn+YnMCY6_;b*exyi)Qiw7s#(Q&0W{rsxGP=!BtjH'
        b'l_{`F`@quWuE^x|P&?EqCQw%SfRUogF{NJ5y_eFh8U}p>_=6U5ic;<+W!qB-pgI)YF^}$zUC)Kucpex*CKc>Kz~yTW9w_letIv}Z'
        b'eJ%odFcCil%vi3?;ic#$6)NUv{-hxpfb%mn7S$%F)N7nMyBpPhZN{W@<7!^ggP5eGbp5FXic@&%V2Y#mT54=cJ+{m+IHsz3J@sk|'
        b'|K|17dn{lX8)?As8xdl)aD|<jG;D|RzMWnBbAyU!**IzVxk1QN-nu=eaupcnKt=;NZ2+?MKYpt(CSQ2{c#7)Mz0~W~@Uc$dO#^rh'
        b'Dn$1P2ObsGD^Q#Qmz77lz#adw^V*tEfaH$<h8z(xjK^V70G%_;?nj~jl`|>ePO^59h;}sf`ptW+gJjBC1Ch5n^=!($bb}rIxCgqP'
        b'7YBxl07F$>K+R1WEulNO@Reov8QKS6ERsK}1P*p$cV{=oo%0lppN|k>A10jDo#3S$+V2MsJ^k@*ctIu(&I!X_pmn@!O{oq8n&JVR'
        b'VTFos5T(cx2Nfz$y~+bX%s>ohQx2_(Tnt8SX0%p;p<(I|9;j*dvsUY`ZPs7B?%1n08TFPu?$iSN=ocjLbSS>X<~bd!sOW*S$X&-L'
        b'U7v7$zK`5>W+DX*VtxvmQSpGfOj=ctdRB5h`45#LdnIQvZpa}?cjDP35idEuG6}M6&n;-v8P0BC?6EA*3G(J|;AD&WDcu<X?sJOJ'
        b'^qhjcwd>n<^#Ci#e|_7!*BCXsnC&cxg**V8b3dF~o?rk0lC^SjC0wlNqUF*oZ%^*uDUb*74YXyEvlRgzX>rRsS-EFx@5SFGT{{$('
        b'o20V*X-4L(o*!ZRIo)$^@CS4BjvT!;M{k;|C+0vuDfnTeq5J4qZ0Xqsk$>8{^=a#(!d3p2=?2~xhNScGd?0`ZCe|0^uB|jM6;J76'
        b'L_E+Z6pSK8kn2#%L2Pplm7ZO9^hoa6_}gU8p^_u^+_M`vfcP|uw(zn@C%J3+gyC#S<QTOU5(}L8xpIDzLgg!0`2f+Eq4G=FnG*n1'
        b'yI=MVZ)HX%iZNnV;h@VIMqsGZ^ash@`dmjwsK+s))>La1Jmh5bJjxv$jhGZ1=fJrR=HUilw2+DnhVpy*HFy0`0L|*IHwEjR`~M{V'
        b'&^?|DY?@OvxsevL8c$M=fF_h5KejnmwbK<UZ@Eff*|-2`hvSccp(uw3b8L>dc6x@2uTXi6ZdkAm7@KR5YY&Kvp4JD1X&!*OcC-{|'
        b'YE}}0tmO8bBXi2DF9Qb8aNt16b$7YcgfjG@-tl&AGU2Wt7y8!5s&(l)LqKh~Ug$F-oLeg-SbCe#ub*26w1{@19TllOGgMyUdy~rM'
        b'@u6;?_E|$Jf6LkhLqh*6TlMrgj;DnFBFk=|*?aLW7UbLCk;*6kaXn6Jc0>~86>v$=n`U#q2|mT^7TBCp@WYb5Aj6peRF5NaG;4w3'
        b'TEhYOXs6Q=Nx3T5EXklfwkz`r*KwT~azxr3)LvH<fPWMG2EBO;$da3Sk#9nMXHLiGBYWHjFB6W-glP+5+y6G9*HMQr8a-=0LFW=9'
        b'5=`n+dlOyrE;n&0*4NG=RzcLRFiV{>=bJf0W#e+ER5Ft584}RWbm@x~hbVz1cyddB#y=@es>|9D6OStylhqY2J5<k?LW>ct9ZYms'
        b'%1FR0E4hZjUWf8Bqk%qWg53}s+?aWX)nsZc7-rVesIpB~@g;H>m!1=wl8pK2m(Iz}Of6`q+nl&1X#wW>5kp;7rBfGf-*0?vhtycO'
        b'Jv3LJ+5qo<ujEqK=b=4g-AfD^5gtX5OSI8<$Ubfh^~%m0LfXI$euhdQSItqVywZLGoP@E4_R*aCNd11K;WGsDRS3P;%txzZ5oNJJ'
        b'P8TS>e1XLxmwR$CCdNuHv>ypZtL?}a@#*UOLqdU5=mm^e_8mI42YHwL2)HI0XZ)29-35k4KPw679a~ourp<(N|KCTG+@YrW_=W&w'
        b'iI9{4zhX?_w>rH9SFavX7O~-|(Np2poE&hrG7oa(Jpgf6ISv$ZX$``PQLF1qj=z&1OI-UMF%*EB)Bvobi!EN^K7$L>g^PHM{FG_j'
        b'1uZmyQ&Ynk|2pLk_$2*mLFB?gDPhV0Rln+DTb9jK#a@9`VIUX>X!Ywy^Q$xA^G-tV1ZGU!;h3cRNgewxeBuE};TI==mn#=~Z;O+w'
        b'ynAfqm!IGu^$KG!o^Zqi?z(Qets`zhOVk~f+`t94t8O)K_s3^!LhqOuMv7l2^H^qzw|wcG)B@HW5>!@t-R#>x7)dzZ0QK*({zIz2'
        b'oZ7y%R7@^R)1Lc?yNn5)6YclV7HlNt>^XvSqnM;88A0R$2q3I8fG$^YE-nS*WtEFPPS;;DopuP$G2|y7B@W6Raf!*X0s>=>3k4%W'
        b'FEH&BV^hOZg{k~h8YGxV1sKD_a%A!&?i%0u@-zOJAVyi06jP`?_no45RZ@JF;66KEOC}TnlMPH@pkCnw-l~OOrBm9)g!6ad0=e_e'
        b'E(V;zp<pT}z$qHCp!Ayl00LYS@KtsVWK?jUHBZfDu{UV%cAjHg2c|G(M@@i)J#Dak@0g-0wYpGw;e!0kD)3vm>;iR96j)Vokl3Vg'
        b'E54m7DZrSlb5NE6HmT3aPG2{&y=U+{o#VRB`n`^|2jt|K$|6dgxl41r%f?g0UEEx+)IhAy>`c(Be27#nwTs}BA)J$9PGBWoOAsXf'
        b'EbxB3?Jb)lvK{C%pHZI$AYX8cox)^2CXtow_%}(t0|#=lUkB(}8=F2QC)0KJYxzW%4p6w3mMGLtxZdwdCB!DsFXh(DdgEkCWGFD)'
        b'4P~|v4|DGo9T6*7h;$IKow@FxY_09+9O*FF8wsN!b9W>fFD8LkTAs}kk}El^)xd5G!zhG^XPW@dHsKtA)={s84MHz4g~3GDK4CF|'
        b'Tj-|#-16loe^!_8T(>*6RowdewkE)N8Q$pbPewGSaPXtSd-m=lX#7{CnYlnvK3<n?&sdH2v*C6Y0H3vL681N3;v;UnnMBqd{fB!t'
        b'$j@N1vV#ugSlqL7EpR{M!Y7}BCQ9Bg`px8ioMZ9Ju7>BT30kRHHM&Wm3RJGaasc8PDm=%t3#cezhC>Pj>{qZ0Bf`LO2XC0sPp3xz'
        b'F!X<RmCu$tc(#*j7>1v=psy_q1DSN<pRhu<IK}Bqa7_*I&l5mUG`lCn=Bspa6`qi+aPZ_Rp&Uq8uKXO!9!GPYQg<=cak#A82b(|S'
        b'C~ZgOs`)b2f~<q&d)!^O*kKsu)DtZb_NPpY4j{->f$~%8pt<WXR3;3>e)k?K{qv4$F9g}Pe{nOTl+F4I+AWq}<|}<kJ)4#7^P}O*'
        b'b(|YO)ifS$Y1w`JO5+8Cq3IVr@I%;u#YLc{E6WXE*8f}E#Rh7u_Di5Q(%=c?(5J4oi*QW$$PvYl92^k}hlIG}O`VmaGyPT<MYBwB'
        b'f#`2%jNYA}GFa;93oQfUKGLkbH>-=`g!;k~F}d(E=Jy`m_*dq@A9mE8=T&f(^Kk7=cwK5G4D;48@hR|XJwP|jPN}$ZqKmEAOMVgE'
        b'=rsLQS(mo6m1ezDIhK4e)`9CxLfr&2>mj$rX<eX;8tQ1{MUAvN)zLe<*ozONwhPZ9W6gU>naV#hS*DtY(f50E!v9{G{xM$~g^vTf'
        b'N98+WM28&dPKVm%&&pIj<Epv9SjuW7KjrT7<!1Z-UMBPp!(=L4CY(o+zCjfvQwfQLP1JgGP=hKk{sfq@+YYrevaZbsJq}2XFw<Gt'
        b'p*&l67`)4Pb-r>rqRDhm?T)1Pd_fKwX@C+jpF@TKu!dA(ODOQ0wPzQ$VSX4UjpiA@+F>^q0@y=BvGUN^!W!M79l%|`(tD+C@J6NM'
        b'My2(KN|UaVsDLK>dv2^|@>6>JEmAvH^Dzo^xxuN^?Nqk7xhOcAH=)@}9%wT->;F=zE8j_x?qa2NPo-(F5*{bY8sXLtRHiuVfY<57'
        b'n5jdlBPp>86`qo;PzeF)*UaIBt18oL_|ix~A1@g#IN4SyJIk_1&;SjSB5;a^Nx+<?41#f$w+x<enIql|IrhwzX^wqXPH}AfYCx=k'
        b'j&#5Z^%L+^`vX=U_3#asmE*DpXcz<Y_V2^o&5k5uJ|wdub{*!eQ2Ci1IisiN3)*NlREop}#H`4S=}1RT1VBS-`-IENaXNBrV7j7W'
        b'&q?L+NeykC@`5Lzx6P3QT6CXWnD=!#f_bN}sZySQrWCLQ*O`uwE3GM&Kd-4Ap-zsN8Y;zuTrg(=7zp_AgfjYxg0@UmSgAPAvahDW'
        b'!{#bn;Yfh=aq!@Ho&x-n1a;pDa#!9je(;8MP&68Umh9;xwWDjAVIaE<2hV|34s%C(N-5Ja>+ci0+U}1FMW9WEFaR`u;jhdeK8Ekc'
        b'{_t1knom)d5K+l0^TR708!Js4D}fpT{$VOD>r3GNCV`R7S~;QQq8L-5@`r!sCFfRVz^&K$ik?!1Y5}$guyy<;QX#@dgx*PMJBNf`'
        b'jz3kJ{_KK;OfW~CT!T}U3_TKzl{=I>QtQmvORn?&n`-pKbQm!ar%rIe0hGeA*ak<C^%v^yfXjiQ+>`_4u29<cCk7|R1&p`fht<Ue'
        b'q`p3VzRQ6;8VAPO-JOSPYG+Lsg0CsfyGuOz(6OXa4=lh(AC8FlLn59jy7KOmo#JDF{xMTaOb;iNz7vg3YjCAuyrYSy+q$#KS^vd{'
        b'=>~r5Q0qvY0dF0IKBUWZ)vGY^L*R@)j{kwg`~VkxL-u?ReKatht|>R#IC15Po-wDMR_QYJ0R;I;AD1@;Y+qU;UpzjIJAo(yu-F5e'
        b'mNA*G9quU;$BhK(+w)@JVn+O9l3jFF-pv7Xee|zju1_p0N;C&}HXc%#X?jl-a*Tmr*N7)I;fesSCR(F7#TztQk5snu!GCNKXqf?b'
        b'G*ZK}ZjpxWJ-38)n{WeO+YR6AO*sUd^5oiBtkw($*Nj3vCVW(m8+fc=rp_r(DVGPNUc_C=ZE#Aqr?hZtc6hhCi2}SNXrBhIc_qP#'
        b'1P$*`IUjL*9+F^OfYA-;23>KP3LCvKu`8NxY=g%cYMR}hPFE23Zzrx?mY<^o&6K_tPjBNJKf_xINN*}TwLa@Ra^}uKB2j_P8BG)!'
        b'k&H~QjBbu7b5_VbQKn~V_lmQy0;`>ExeBJ~*X49*6><S_<a^0wjUn2Rgzn^bH+9jI;_$?7xGyzM!aF*!S65&}X+iT7R|IOzOTLtq'
        b'us@L=wI6`+fI+Qlvi@lx+BvoLL?+}<QLvw(e!q<^I(UWJgcEt9u_+&>i}*2eJdqZAr_5-^W7_c8bsu8PR$+_?$Cd#41JqLaA+dna'
        b';p^WL55cP^zF#QIA1-2G3@~U0am{P_DNK2=ui)cZicHUThOIjWk2?%TSS*@YvlESf9l_A}ui=2~&Vuov@IXrtK<_QsK4^S@mIvtK'
        b'+)aatAA&v(h(I@c#>m0Q4;`Ej2Zr#GZV8x_pyT2V6QH|aZ++Br9KbSkv&Xn8-E&6eesS<V<=veym_aSS(R;`f-P)vgLsCN0hxz)8'
        b'^rT@Nu=3bk$Gr-8@`MFIW#vqK?fYzDn&8yaMO@Z?QXk;e=tBjuqhiAuBn`pyYNE8n{c;^-W4OB9vX9tX2G25QdMev~*2=4!NO=H8'
        b'7|Rp~Cv|bSJQKqh@=QJ;1CH-Z*q6FD<d7nhC(rZ{pm#w(hxSem#ASls4tjhD2s;ws=@_U0y`u*H&v4+I@APaY*N<0Mk;r-*OHZzs'
        b'_vlD!&8i*kqKjXdpq8|`?)pIAE^cq9IdCrV7l;t}7OnMeG#EO&Xais}88Ss{=jhi88rJ&2S@++QpjH~2I8`nT`>^&JC>>&IEHxN}'
        b'p&#m1Jbj>Fh*huR>jV9TK_J0HA2_eIUa#^bhAKiF*b<Q=(#6h<kin*(^(v0o2FCw(nmJZ5%<bpGjL{B|awXcV^1?ivjwGHHm^dPp'
        b'_vnEM7{bmn`ONh$EAR%WH7?MfsiUm43FC5HS<dd_`uBnPi+K`xus`oHqO4|zWb}{oE4YFuOtTZu`XjK;UIC6tJJXUm|4Lf;p$fnn'
        b'QM5-RV?!66){Y7j>%-A?+#F}Aclz&`c@a_LQO-zlhVxBX245!f)nxEesv>QQ44<Tk5m|;eMwev>WEpc7Q5R1^0a*Y?8Xmj&b(Hmc'
        b'B>ejdRc?h$<ta0AphkBjMDfG_T5)Z-A_~|8!_zxQz{T>&S~cOfdI@(|+be>!*?4q7HXUUxMj~Se&s9X}Ba=rQ(x`@h7F9Ycb^;Xi'
        b'oi*mb1Xl+hnENM}u#Im(r@t@ns`S3}vmJZVey*r+d|6?ws4(?ZT)leVlEz)Xw>lWP`176(BO<>G|Cs%AQH8@^VJ)gK*(-omK9m78'
        b'GH=hPBO?C`|KR`pL51T)g>^%P=|n|56)SKk!+%J~hn45S%Gni;!xh%73e({Vpt*)J=7El1yf#+#!@Su)|GC1^QDOa4g{h+={u-Gx'
        b'7+J7b;Q4cE#hqD>0~OYk3e$lKc-a9M5KgH}^JKj-VT{HFX`@gKjgTwpJ%59D;tw8x;h|kT3#d0*Pb!-^!(6}?Hira|p<!ZIGus%w'
        b'6N<JSaD6qwoF2hXq#5H5X9xan@V6BX_lglm!oXRaDnGgiln1tP!Zs`TsF_fnp*Q9e|0**dyi`*gPU$f6+3j+3EX$mX&NUO0T5O&!'
        b'0$5^z5fd;v1p^G_Xf+v0i!yJg_Mx%^AK4C)0GFrFl$R&La6;JP&A?ok+~#n#`rq(u&-ylMs~>se8jUi3gXOBA(aoe;6^1KtFa>-w'
        b'9BQX=&oK9l1BQnk-3-`$*BQjsxeD&G9jx_cYNL6`XmlDI2L^R^hYlDgNfunJhh@317@K!4n|l$YwX-b0ncrwx$!#(<9Gu+kfmSa;'
        b'%)%hzVJWnu#eVybq49-?AaGXWDN|TQ7v0#zOW(^kHsL0R7W{2G)gbh5I^Q6i*N`<E0%$;4VMqf%$#h(s-UQ2a(VJ-Sdl-HX34@HS'
        b'IEJ+f+h?8TpAK(Oy=qe}a;l_5s^1WoV3XJOlr{)oy;{PnE5VH=cv)=zs})1S-$<KqbrbFsN-rfhsdDoxFq?2uUtzsbo4$z;&s-7M'
        b'dl<W)20O$otIyg<mNdgVwh~i_1xVR1NCbE?zG%-e5}>kdF4|)!dyc^0UG&`%G`~ZbThDnC-)T|rI}8v1Mj=D|B;`Kj!Vb1b7#4p3'
        b'3`Tay@_L&Vo+Bi*ylZ$J+@b|-S==Xfop}r!1`;AGYeM<tkxj_2kAr-&+Z|<Hh2{=3>&i1_-Y*Rfi8=OFbF!exBKZ6c>u;oBGhHsm'
        b'H2aa5org=@!t&2)0Y|Fic=9YPHc#s`*0r8*9gT^=%_=cA&o$P-r?jX@W!iY8DaxX~zPJJH`I>}EO@vmTBehQfM(2U7Q{MWHVtjy<'
        b'_)in?`&-HsgBa(K@cka3hvSP$Anl8&bBmPCfkOd`MiD?M>^hDZ&+Hs#P#Xg1#EdQBD%S=15*X7m6=(F1aGv}x`()L`v*@97bh&7r'
        b'eV7)Loe4~o^kLi)t~CzhcbHU>U!K9e?UCSSck{vScp5Y#jK-Z)_iP$O^IR8nfI)kQ6=N@4FJBkM5PvXz563Lxg3K&zzQC6@xL@no'
        b'ueI*inuJ=HW0HOYe{KkmZhYaKY>OG_Gq?FyxPzZ+9iM8gpK48>T7nNNxl}{eT5|gRcUK!?7SI5+!FsJ@ht|47YvO1LCM*t(fZ2m}'
        b'T1TDMTCa6IPBP~a|Aid{aT!H7YJDnwQV=~^{gj->VHANlXtj<it+h&P8s9|Rg;vsw`ws<^Q+=h%Ps{`5)mlfH)>@`D-PlBY|LgKO'
        b'lT&9LU3gob%!7DmY8@YFtsiJjmp2g?V3o%1IXB%0MOsIm*7`ogdwtuk&7738hC_48&?G}a&F3p9s;!z-`m!@z8<e?lgYphEt^hZr'
        b'PAIoBbFL?z&E1=LNX0Ho=uW3>5I{V@9Z9DE(Lr}H6mMJF<BlxryfI`%okoO0((<RtUB_t{OCK<6S!ch?<)$(+VtJ!$C%;ace0h9-'
        b'qWU1yI%2ifSgomb6Y&}BgXHY=c)H4s{z#RRXdO{nYn0aX*G<Hpa%zkuhvt+rBF{=i1@OKH;gY98VkxN%MI+5a#yvnjULHK-fRZ?h'
        b'CYDZsIn_K{&VNU?mt4GamWy$A<&o>3#6KgUT<j=;5BZ7wfc;=Tcx73{6`;$g$3Qu<3?G>zr;DCNPAJo!g<;!(DUm<~!txo8bOr6t'
        b'%JZz`8=IU)1L!vp$W*@-Dp7_iAS)2y^EiXHK-t68^WRaGmIBuVSayK0i4M6isQ#l(iG#5Xn}D|h3dI=k*mIjOX8Kz@;K3$Ji!_;1'
        b't+m&pewM3vG8I2-0a-mjBG3Xz0L<q<A-MHRd>`OYsJARTo&os*q|3DKg0h7ws89vURAP%CX`t1bmA-eiPoYy)_e{|Iu;&Zc*)wYX'
        b'oS(OcJ9urA<Ju<cwN0j_n}}FQY`F>r-j?w)zRdysrYt`o8JWh-hqEPV)8av9(AUxo4Yhop19!Q7SsoM5@)82f@1lu^5+YjnCU#?i'
        b'(3LO)SHjF<gFzl#wFw9hN8qM`%Qz6cu4>}XpMBj-?ZK@-Gqqn4i#Saj%)OmK{89|CN!feFf{CohH;LkqZTkot90ti=%-2s8vKQ9N'
        b'=*F|XxtIuKTjMrWKO}+Iqwt))rcq#~FAyA`NbkXI-5fwX&V=&vGk~Ad6CGx3gL^gBXA8G#&#y5YRd}L)s}=8}+R-(>|LpmJq-@Qs'
        b'_0v3T+Or9BTh>IIcelAp&q46dV{wTT$6teoR6-@FZgVVtLJFUn)xAaqA~kS20%LU|sb5pi&r}?Yk2Xm-Q}<D&(n9U=?RuMN{`PLr'
        b'#=E5J3UbxFyMo^Wi^7sjDvwW^Gv-rr2-f{@ll8+*W(h(R!k(M7n{1);N98ZQ85CZ!Nggo2oo?8iP#9y-V~ko<o<XzRBV_^e4F!oZ'
        b'U7NmD1aIfUvU#8^JatFhEvBLcz{}Bh;Lq^vO>J4Fo_^Wuj(WYh(66oIaKZ88E%ala#Fu5%UF1@_;7hC>C9c8Jer<%>1)vKRG;@i!'
        b'A$B$tQN6p#_SIlVd=(hqb~X_Ylc~`8-@2{j_FZmg64fv%k}icew@k}7buoy?5Ksm8c4z`U>?uU8ql`N9X^gXDJ~1^rwl3Gi0U#I`'
        b'#%|Uy5WyVMx?~ezkROX(Zy{&`5a5szC*WtcF9x`lO@zQ^0R5qJL<CW2z^9)P@Fj#_)!&jxnI~&_YL5&qEw6Vo!v`ZQcgQZTNwf)j'
        b'XPD+R7Fu>pz2A-kVfrH(>%Xas+YfveaV<%tmA{ADaio<4G;=7!z;B=-*!)`h2Cn|}r0#>NtJOTafv;c62nxY~i*DSIbQm}`Vgrf2'
        b'vkiO}f={@BSwjXbr(+CwTv0m?PXM{z;}|8oXz#(ptiqUb*a&+2mfrXuT^z50#?U^BF-YqSJZT)y^h-GqBqK)Jia}Qk`dCJmfuw4{'
        b'cnv7#jWO`IcErrYQGhqTkmOtCv3JV1iTW8`C>WkzGCzoFg?+=94)0W}ekiwoU*66l8Ym*)Vp+d~U;hoiuK4!D2=CAgJw-Ld{>=A`'
        b'h{4&er`F|97gO<lXnF?HU_?ZjF#tJH?<9<*z{dYlr8!Hphww$q7(tTRLng*$NEnJmib()NfIeD8kN=JY>d@81=s%{LK;yq9spoj$'
        b'c}(M*W+RRGJse7028`)FXSN+T9WL*u1MiZ!Uq+3}b{I?IR`Jv=acZ2gK3BZbt3}jJ`q6)p;rq+GxY&G(dhPVA4@f;A?-TZzJIL(='
        b'oB+}mlQS`hOnb`Vi@)8tMLuI+n0A-joS3+t6p3hhBh4tXV_dwY>Uo|2q4NJ{X41m6tuPJ1$s(S^*#gsm?gh!>isx+tm@#Mdriyah'
        b'iR<4=x1GYorPKBk%qS`EN549pmG4S3A$l}@PYUr-kzTTD`^9z`ly`exJ1y(K+{_tsP3vJBqwfP*L+mY{j)~wv%*HyAY8J5xk_9dZ'
        b'ZDlLYtX1UsV{a+)<|&LDFot4zsp3oyHcP%dU6HpyZY;#S<;&MA^6;;g59Q4rTAnkscE0A!dd107O`Zq~*5n1GIyTJG7&Qtya{F-0'
        b'ptzF^Us*op7-qq^8!#GtI;pCq28typ2a1NMg!sT65X`5<TiReO+5NFlZ$Wk0IFb6R&RD`>XZ#{qV`PI-wfp1ygtZ8i>v=-DBF&GM'
        b'ljaOs^=-;di+#Pki=F^lxXM71Bg$o>cjQb&8pT-Vxp4IS(<R&k(R$H47(-Xf(7%P~bd0+azV^J$2t&AwFFf7A?MrK?TfTWZ@2*u`'
        b'-ohgKi>PZ$6G@-*S_JqBykiA!x%`xMkD9kK6mV6ar-@$<Y;emLBwU_Y&XUm>%QF82MQsDD9PU>B9yiBx|B*Qcx{6=!*S4-vOw22y'
        b'q^yB{ASczcg$@Aqc?!w0E|hpsG_|ydATTBukqP~)>iZ<}rYOWSm#)1pd|1{qPWs2e*c+g~f(Dvtyv*hVHvK#z98%bv1EWR+&y2T;'
        b'TKfAd89r798GJO4I_r2lnji}So%eK7bl$VPohJ5kYpuuL8FB;yaRnoi0M+AqxBGILZ0&r(Ar_3pwGSV?F}Xbr9+b?wH0esQi~_rp'
        b'8GfnIaj9%5;GOXEWdoNOLral?0Vr@7cZd0wzda4VUTD-Y)DpfvKre46V+=5ygg#ThCpx^hOhWH-3Lg~8MGF$?;it=F84IYl3VX{;'
        b'mx_q5Ax&5=J3RShnS`m#V4AwiEJs-@x!GL)prg#;D6^RZO^!0c9nuTT9h;GaYessOF&ghXK6s+caSRj*fv0F8%T%-Uq4Y(795t`a'
        b'YLqt{YCdOKHnTziKaQ5LmT;BL6E4N%lA-SH?nHap%-iToP(6K?2*q>;KI}s8FW6iR)rIUJEU=7>J{!l=7ayl-$EW7B*@zH-Et`rc'
        b'1Ni3Jr)9mfx4-R@Q>NaMVVcp*1Ck`#cA7@)h6R<rlLlI-go;rG^mu*Qc6|$d`*Nbb%=P#Mof?;<q(ZpV*Uva`ir7|0g|9JifSsz-'
        b'i~Cyk)Dkt*ZL)Ki15MJpx<VZh3*+7qdYDuFXgc;yWm&zW2<i{c+uS-44#WCzh)rb;`w%KodwV)jSX@?L0-4N!VhidFFtHY;KI=7Q'
        b'*gHT;)#sN@CraFijb%C!k2qAM6XC=Lm=WSeK{QUmqe_|nP&oAsGh5t52NArDhsp3ZnAi#v8#$&wl^L6OW|Pj?gi~R9>i<wimA0mp'
        b'4L&M__wZB7I-b|)<d{~M*-!Am&ttHePVT@7n0bs#)mp#F-o~3Q+rn|YQwC#gZJPqXp%Sg}Wy7;OT*Wxnx5`XQ%Vq#@rmAy@*fLXW'
        b'*>o!guJzxAn6|@38LsKgGV42qRC<SjM<o%FWwwLgQ6Q#4yBZS~PJf%EWmaj~bS>*|%BI1&8VD<csS969bu+Cm?0UuMN^x_g0IE{o'
        b'`dq+(xdcwJ&I0V!;n`iUIE`$W<_FX6pu;Hk3Z?}@5T*&Ja<5?X?trweSulxT_B@^rFqCG)(wHC2ai<Eu>Pngdz@pOr>&0TUX_(-{'
        b'1(tXQ=V|?&Qq$8?3SFa%K5q3tm6~XUFDG3sHQg_MIq6)f>FZxryj5x%m`-xhVcOr+I2lgkGn<hz9ES@aF7u*L|Lt9DAnU&(Hvn<i'
        b'm)5u1ze<+9c;4LxmLF8?(Rf|t4ryKCp2V1~RXSba_FhXc(#kk+8P*erAaWK%X1uxBizVzUg;BXd@8O=qKS<!z%2-T)#^TT0;msY9'
        b'iN?AGv^9+91Y<1(F0Mc`dU;wD&*otsx@<eXTG}^9Fv>6oB4F+U7p9BW)*^P2$~1-)e;_p!;RdPHAaxf?BV)n;JXr%BD6T?XtsPW1'
        b'?=S+?B29lQy^<x^kAT{6IfyM@fXD(DW8A#VjJ1nr)`2#lnxMrJG*MVC3W*gN_k;$8gqOx*sI137geGD!6KKJKb0w_cqbLhUL_v!U'
        b'z_GEHYc$!5F*M#EV&^o%D>H1M-hmPPgqa}RUWjd{&dmED37#>ymr}zp6%;Ouj+M}fno_HwbgO<_NzDlkQC+Ij>uRFeY7y|J?%zf&'
        b'e<xd$%lKDLHinnENjz6Hg_cNYP2s@Pqiu^|U4aL*i%Y>^2x%fCQm4C*%>@GXBUF;C)7udPKSq+dXG;qoM$c&@?{EcM8Q84xeMs;U'
        b'Ui<9P17sr~kF$q1HSt+LkeC0_!t8Z72<>gsR_30T0prdqX#-CC-M-9r&ZYdDs>ehYhCCw1R2TDC4EOv*YRBWRx$I8N3&W%*tL*l|'
        b'_fX{(7Jjlysbv{F>NgjNOlVD1YA5p!V;BQ^@)9IRGlSaU0D3d)Cis5VOdV|DTCTzkkTZI^UyAphUUR@=1Kno4I?M>ejvw0EX4y+#'
        b'X_f~pmY>AsnTursix(e8g^{4+fNxOXBroE|KO<c_q>y-}V9H=Sj#v`e@RixD<?QX;nRrSrWzaW17*^^CEA{`;6jn+sgLc4ZB71xD'
        b'U`VMWxHJq#@|pHe58+A=+8|!)2rRW3gH3oT@mpAYk0*efz~0_AIIq+(uQcog)D+N&@Pq4n1g{X3aoM&iL}5Y&CmEJ{61Y>A2c$6%'
        b'SD0vmHaf=c>jt!7Sss(`(W|+jFrIW@F9c2kEopaEU5Xu9&6lpugeRUy|C{`j+jkroCoIcDQu_c}g~sD}(kZ;1)x^&l2cwxLYIn=}'
        b'A2KPzUVYOwHgCFNoZt{X@vww?8eM{FAAxzI`yb{a*IU11@{6)wQKv@>YN<e56)v0mc8T?NNk2;5fu4lkgtGJeiJL9}2DG7_q;ylA'
        b'h)3xry%Cv$W%{<n`Yo*Y-3#@;nW<++rt0Cpt~XF(9f0))VZ9}&2-XZ0{;LG@k)ZIU6@#e-^&ej>@`d86O?bK_G~#LmUu1#+L+Gw?'
        b'75+^F72svuz!SD=@Ft$FmXdCl<L|-s2Gh|J>rvQ7C$+`}Tabo#mS~>>->hB(W5HRc5ycWIJlp9mOhq{eVbD+!`4+kC3Ddq3>plp}'
        b'@&YW23)Y7etiQ~_s{LQEie83QUt+C?uo_-~)!>5lJ_T#rG%W408Cbk2SQ#(F`mn_MA%s==0<20GtP~1X=?tv0{{`#!FTo-<miRw5'
        b'aN5yMj_WlKgDE&f015gDHfx|Cx0w(kw`9tTbi7T`{wuqI=UA?>&(Qv>`1=&?Q%bBU5U<o1@Je;zC8O|C%rJ=wd5K`az6yD{k8hP&'
        b'--58>XJDm-$Gc!HfF<F(x*}p}iJ5}b$eFf-s1I{H39KXPn|OVu&A*c`5d*Y|z1*gx#43SphP;4(h^tMM!e2B4%c%P`{*Uutg5_Oe'
        b'^@gwnFTfJGVEqS{Bwm?;b+Gc+c-?pz7FuFOAuKwCrG0Aro75P?P`<`^m>H8yD-k*U+nK~=3h2{f0Mx)~I8bTeNTq?H5@-N;)J5>&'
        b'dPyY2G|B@M{#X8tR|O{F^!q}lv1033F>n@$o5j;ehsWM5wjHE`t~p?(@ax5fi0nwV?nk=rBSvjRJA*h5(|aRY=w0Y&0o{eQ3*Nb6'
        b'>p2SE`Qm9oF$<_D;ZU(zgp3x`G0vjtwL#PAV(aN*(8n{y&t*z)vHueTr*Vce4^#z*Li?^Z#8orAB_C2QRchdcf0i#5@pO8MA5-Ih'
        b'A%jDq-B%m+5gmAorcbGYxxhFw?a4RJ6wIxjKIcNT7sGjA074XwLE|F?jj6-yUD1`H)hOZBZ_fu*1nD~5%6dFi&-6*L^%JU(dm!TQ'
        b'njpmebwDt7rcB&Uwln5rMr55Pg&!AVi4s(P(%*nyjpNq^@RlbWpxgqlDHigg1YFi<B=u$=0@OAO{D1@Kr9C8dnRQ;(Q*oygP=$z='
        b'^cpVk^bW5oR#g>CU*n}`@zNu3<vma8!3ZW%0x@FWg16;}g5s;0{H@tJtShX+vSLSBv8lY+W?Dg1LFENKz)wiQav0gOh*m0Ur?Y=R'
        b'dln*M6KTpUwq_Rh(}}eZSg8nm+h}BbS%X#wA$!`0^kQ4Lzkzf01mL;j21qv_yK5f$%=rP07bDxFfk}CcES0s>1;21CU1X^o{Q7|-'
        b'K23Hi+UepUvK0IitmB9;lG@IEWwEZBSJLQ_zp}XgIvg?sJR}M`&W0bX{CA4g2421_U+pq!S$+|33f6g|Jx&r5&(c7$&O+J=p8P^Y'
        b'6*o}0H38hTCz@T@bu{s+FOZ<&-6ZQWnRSe0QTy_vCrQ@^z2zJkKTLul?D^3Z7YA^nz{ZFQ4-YQ(=fK%pOA8UoRWyZ)K}@ItNrVfE'
        b'4YKDGLI&T-eF!tGfq={DJO@4+iRw+vzBEJfb|3KL`TIU5tk{Y{o}V?t^RE$Z#gtfRL@B?Fof+hhPCI^>L|4V5T*N)4n5T5gN1W2H'
        b'>&IbS=Le+ry3{2_+^T1IbiBwqUIcmc9$Yz)A0&-&(ik8?R?#0Wl>rkbD8N4`LKNibp7k-@*{>s^Xb^7$zr{@?>lvA~m2~Y5X6+zZ'
        b'Pe?=#Y_TamG<{QK{iX=?;Y!hSId`Rql5>Y48Hn>m(>gNbf9c2r>X+nPZ;`bZ!aDr|tkW)7W(t;b8kY9b|I%wsFTolR@uNlIr>OD)'
        b'5_G#0o7Iv*#R7E{PR9Z@y^$Z}!Oj+Ogk41~RB#2;v7#W^1B{z3ze^m0NC*!X;ca^8x4^ZQ!w?rHQAxGrvmyf8ERiOngKEVf;YiSI'
        b'FKD~yMKWC#<!ffhKzWUNN`Hcs29ZqrNJ_0=&z!Lv(DS7RU42s#jNo0X(@T&&J}o)gr^Lq)RoAI`@gvvT(~+fUwG>f~yXWsH5}D`*'
        b'wt&MG{!bAQ(a;o4g)JG_){lxBeOe&vN7w3my$0aMOh+6q-%v!Y1lZ&F>Jz*em;VnHW&$VsjX$Xx)ah|BDG?^wLSNIKj5)!>yj<mM'
        b'd9Ot`HJtVufWgWsuTo0~GASwPwWQ}>cBETuMSeRP69H3Xxd`!^dS?Aul~9l#$D_bgVGW_)dF+~FA*u?xa<3=i9fQP~!qbalgs~yX'
        b'(PqpqI2u(S#rqk<Y(iB;1uf3FOqx=QFb^zZ-SG|Ke<<o_=XkczBLi~zQNpjnTWK3;QL&;RMCruB6N=0MNZ*;$`J)?Yz4>4Gii>Ei'
        b'bXfpmNS1aM=_2@B_hR!GN7G=?K=lQ@;~zRAfm#4QgUdi8F-41yyGdeKWUp)ZyU0kB8ELBD7Rj%W%Z{M&5+vJm4aRC`;d`q9_)E0d'
        b'-$2G-5RW$k0Qq4>z4@i=Qg)EX>~#$&D+UP?p*_DtL`E2)IV1QrZ7*Ku1>~G-y-2_AwRVP6#U^gT%DwqEAxnB4?)+n1@iidTU|b(0'
        b'e49Gk1BOsp!iI+={zVdeYAtnkku+N0bB4?gNC?M@G6E1Ki#D20Q!YnD2LZo~X3@-<2<S5;?MV~px7`#Ax^CR7!vwJJENs^CBLvq)'
        b'ThJD~Uy6AIMa&QO^ua`!XV5aQL9)<67MjRHo9P7c2wFkX0C<{k^efT@)d;A$oDTpS_W`KOW}rSOq@c!INdyyB+sQ?&_<y=&#>2Q='
        b'jEM<w>JpOj6jODz5VA5$@Q5M2Qb?UHB0huEFtD^eoj#46tAFEPt>PbVi#Bw$@vp*n54YA*c3w=3S9%jKhEh2VIWP+J#X?t<;Ey*>'
        b't*1j-J~89JGVxVZqlcLfm!_zku-ycf;B!XoKd5#YgaOu*u-X|0k46+U6>XTBKrRD6{B^bT`C6Swf`r#=q|;Vg>HpDYUj~q4ltrWw'
        b'A<8)<pqxTP&+$kQWxbDJo*%K3s;VBw(U!1*btaV-D(^j$^^h9lti_9a!kY^<0mzja$G$=ghP~cfNG+1ffIoTWNf$fo3ThKE(!a+0'
        b'ne7bASL70|GVO89=Xlo7B+C_peR}gNrcn7g>tR(+ay3O~rl652)E814<HXw(otfBM|6e+{)018>uOpK$Z%mq^Ii1i>Q9Nqn|7BAG'
        b'99VeP4)`eI8=NCmX#4^se=S5Kg)LyRlhX?+iMo)YI{WGlekm&Ph;F(HA2J5ws{;~#YYl~iRs&SlKpY>R9&id72}k>R%+vtD&&b#}'
        b'HUbqql@v*=qOfBUd<r|(3uB`~@{<ZN!J5VJbx3T^!zvoaR%hc7(_M6pk%q6^@r)&mDl`B;m3}}%MO?Fx6RbO|VRk<-uX1UC-C`hk'
        b'm^Io+Lg+8_T}9ara-P8hn}acQ%XY-*3L{0z##aCpdfr5G<Z=-LSm9wjsw>4YpNC=^#?h7F>~-+KuZdY`Wft}`2o`KW`-^eE6xdzL'
        b'Gwz0rQiViQO9O^!2w%JmA^3$7&K0M_5AX=w6!eAV39PV{qX&GF#{o9^G4vv>pWQ{rxR$#l{Fn7D+0TMM#9xvyYz+9(Kni~>xVnm;'
        b'CQ3n7_Y1T(T+Cb7;Gz1lAfMO>>B>^OD9VCtFGf_i3v5O-UBpxU`vYL=rn}|@bMzfjI8o5cx1k6&EBXYOPnW6X#VI=<5X2RiM1?%8'
        b'T9RR;DU66q3fvwQepm3E(oD;LlM~E4%wbkPL;ExpQu;=Li_%Q7o_uMJsSu?H<Kfc(O8!>?sBRV`0xli%fG6%lXqH|-1GAGR;TU}S'
        b'886OeJwW#&VC#W_*G6|!dxtN~S^orVVU0&na3{22tvwrq^uCxOI5N^^MuKFoJe2dW6~Jx?bAKp8twSHcK<hT6E=cjf`s&6bivL(U'
        b'HwI<g6geOJb1-+jvkItr?4mXMgBp)>!I47iXB&eWz5-tLk%m)Pr*;3v8jmjP-#3b!_c0FMxdWJ;{yx@nP<VfEBuC`Dt2ZIlcSwH;'
        b'XuHN^hsb$HzYmGON&1gjpMa|R;K+CU8?C!G)&NB_Oa?~=`RBO4sxOgmyVuxIVD0*s0`x#q&pFas2U;4d{+{&jweBo{Y5yjzrVl_*'
        b'tNTgJ9UiX<i^R6U`lkUj3AQ5JiT3o6*usb4|4A~;C(IpW#shO3Aos1mTNejER#p8EGA!k7n8Esjw6<wLvpvViupC#jtfQp$)dIcq'
        b'66U5mwxjyc6pcglW@NVq9voHV&k54_Jk&4L&yY6(l9vO>OO$^AIY&>Cm&n-oFylYO`48fskk}z2b>m`>Yrzqo*bYFW#U5W1zuy=f'
        b'F+ikktR5$^vjq2p#U4&#&Bn#DFF<~f?FbS0fyntEjE-0BVBI1S|3|R<LL@jc%0H7x1i*F%NAUfZVv@xkTi@mcM{EI<?)i@NuOgOi'
        b'TuhM{ps^Tq?J`Nk7l@pr@wdsa$QqB8!I6GpbHh0B)aW_VpA&oxWet&UCSY=@zN-4)WZ1iJb71{`lE~D+`e(?nOb803^^(L78j<r7'
        b'7%fa9t=-YnP5K)!J$!En(r7F=a-M$^@r`D;Z6Ve~gcj`f2=Fi4?J++{=0{xA#50kwR6-0=X9Y*i4vQkrYJ#Is0xy6x3(F<uft-8r'
        b'ZO#{9`4_lg&3y^hcT=#up2NCK!FpvH7WM+Hu!7)2yg~N@hkJp^y};j(7^jT$)gOSrv77=eb&lo8256u#3qs#jFcIa)RG@}&xB!#G'
        b't$=rUPLsyZD7S{)j*dQn8Kv9}T<T2nx1{!wu|=wO?f<Ys0~Dud3OPb7feiqe@|O+I_g`GNjA<OVHKs9*|5wDnDO_X}E~6UCEZYIg'
        b'6W2AN1{nu&j{s^`mVhX$VBC+JE{xs-7-iXA&8EAWWrEz>FgFFDMa2j?M;a{@#w@~b3KQ*yX<s62Q}Bt|gFPC@R~l1~hG?g-;KO3c'
        b'-5N^AX*N)LQv3r1n!sJcr53FJ4SX@m=!V9jgib}S!d)&eouGZ-QeGJwX7*Z%XYjYsrlDR<c#k4-hel2pUWto6s7dgGXKH={hK$@u'
        b'%Nix+ONGQ;SGz>=hUqtzkLc0rSD`1tT7(c|6uiG^raXuQidK6xruWov1<4C4d5KgPL36FAHRMQLDW;D#AVnHQS^89>Od_qXhwFn;'
        b'H0TP@>LPg0KkBz>UM%R!dtPsg=GQ6fKd6hCf=&E$st5RnDR1HhSq*f@L%rw20G=sIV~x@PjTx<>Ry|mt5cU4;>zb=O`OSt#j_JQN'
        b'+D=_9Z-1kQ>2;0us|_!0M7lN!-_XD%BHs<uTV}T-9?B163*q(4N#Ldlm6~DtR#B%2+FV2cwR(tFkCI2^b(kMK3h?b@_&b^b=yP_;'
        b's4~=QD|I%(fr!5+heQmg2<=2$JO&0C;`?MPq2#_A>5+jV(wM>^0a|?+QJj3XgmvUC)EEs7LczQ5%1{hrN0}7pEQ1O2{FJTRQI%9s'
        b'r7pvja}>*qu-cMVwC63FK~ZbfqmtVCz8-^B_r?yvyNFEarp!ztHbS!H2SJWu69envKI1|S2K`i7h}1act4Sl}?CWSxGtzX8cmfyn'
        b'8n1;v%qPCt2pkM}h$2L4ov+bRQ^TAqb)~p=hi5*md^pCfv2fucc53t1^<l*{FV}ksjFqYRb;_L$Gq3?ZzoW*VO&B5Wrpf%qYf)Tf'
        b'Pf!Djk7e{~ny#H598qD!8yl#_QBZC-Rc<_gTOoV`5T5MnWE)J-*$s!k!v`DI>vH%5CwS@a!$xvpYEC$CW#I>0Xv$$Dhxy6h=W8pH'
        b'l)R4Buuv*YPhn$0=`Vh2zfNDxdm%Ue<=i9Fxi&O}O6f>v3}o{MR`b%csFvA{*LnxX90&XqCnZ-`^Gh4j(qQvUYfrvfy;EJn@5tr>'
        b'n-mshZd(Ok6LjVKv!_!vXegDUKlo3znqe&A>z>!3GVFFnhnDX=_?^9nr|yFpr<sy^DvO9)kE<CSCA1gn$WP(|(JKb4YTrg(gj3q2'
        b'zj~FC-efj@NTaG;OW9cWaco_L{pt;#`X|7k_mL+4)i^%LyvdX{;mg~gVa_Fns3EA$CnDev2{G@k!uZTUBt`HrZ|Rn*C7k#K7&nz-'
        b'K|;RKMC9vS0)S!xiZ6Ml57y6crz_D^2G<0mlA%aRHoD}C>%&x#|Et<B)!UH&>y%X+W?+YZzP=|53gt+q3f~AilkS2H$V7D~gd6`A'
        b'3Fl@%IfM$F9^9sDPSvbS4x(xOG{-%CpPDfX3kLwhQRgsR4A&}zzlFAg2;gvC9z|l9lp{3#KL0tl0oF5S^K`3eNy_K!GiQd^=1`wA'
        b'yyp6x;kBvUBQNJxPv`ayQk-YEe-GcRUvF~A^4CAHpW>yvc)``wMF%VkM=^!pv4KArnm=%!mp%+jTymvSurg2=^z?LwJ)3U?Z2Te$'
        b's{gFFey*NQGNV3J!^U(*Og61!rYu{){g%p5xkJYy74lUI4X_=M<Vg|E6b%>v@Lz%A%bTRD^$88>tIfdiOIjV96k)#`!N0qj2Dnc8'
        b'I<=QUEjqE2NwqYN26)T0@D#<4|1&&ifQAq~=_GK!qllhAkqQ%<O7#4ZoZ1(TvENS`xR0R^moE<Xe*+UpGoX(eylWvbtlrj4EgQR*'
        b'j5z>Mo$mF!jr^@m_9p(9A#CD%^{;)&=lid_)c^PXE3h9XATEOA%<%JSplsnf@dn5?MD28y`T;f2F*x<?=GIyXrv*~55v6Q`sbz4K'
        b'=vCKOyict?#6DmBj3rXvpIQB+@EQE4+VM}d>7VL1-zT<0GXkz1iqIYrawGta7s7WwqYbKKYPjT>t<wj=<yL_YEBvq;XfNVAgcdEL'
        b'Y>YVgJBQUMh-3}a0-~svzYkA(N2F)*>JuR*DFt;iqgwz?nM@3t4f0G5F$n7}0mjw#y+rtP42f6a@9JleAXDeq9*Q&%12*23^P}UE'
        b'cc|fmzpEpea)8qzMtB{>DOyH!z3-ZDbYcPgmB38#k}w9|;-^s$1k0%h+L8~wpX72z8H5#<TFGsvZ$C-!sn!{;^$B7&{9-*L;X?Kk'
        b'D!w<y#e6>H#xzzv44{3))z#uUU7@m(@lX_hw}EfksFpVAs8>^UEp81a^guIp?cb|5xi)t6sxOfXF$|TocwCI_O)i6hcNpnM@V32K'
        b'E09mQt_O1(p8LKS8}r`4j>&>;y~hS~o}Gop7f{2KkEE<pDb<QolWUHk@gE?`3iUt+KW}vl^R9-Ul|a_Nt&XmtUSn-!3PLzUqFP#_'
        b'%gZ5(r%1yhF6Kd-Q?7=puc(FHh4#}&ZL}89q~#Dz!Y++70ONx)vKAn|F^JeCom!1wFc8XblVR>xBlyvg>OWLfFzZ9qaCqs`5*ip`'
        b'wQGdw4S~$$SJkr9lZy}gW?dp36C3^E>eMs1z|zW8wmsC2|3BK^J+7%MYZyM~<Q|ST2@tNfNiZ0w&Ooq|P@N$uBG5VmR3qS}NiZP<'
        b'@Ir094DFi}I*=gFgV<J}cAk^il*pJ7(6*>$o&=Rz3eSkWckmg8X?juHQmR(1dcM8S32JBF-}`>wAKyR8-uvvm_I>TO*4}Ha;iU+Y'
        b'd9^0H6MZ$RM?nk6;YQ_q{%WU1HW^QG$ophA{I<3$Fv5_E@;ETqVp*1`Z67V=fvGA~^ay${|Bl5Z?Z%V#d6&k274Z98+Mz4HGQMml'
        b'x|hG@UUT_n>{nr~9sJ_<ea3Qe`=6+`?V{rC@Z(PYj+phVEv5UO<IrUbHUg9;+K$c^%}r@sN#D@%O9RvvfR+@Z+}YdS#2Wf7VSt-0'
        b'5fHoV5x-2tb{OK`X5`z9E~gIJgI!D6a!pY;4eum$6Pw|H<f-SwEYgE)`6rvtX+VD+1n2Jhu7Y4(Y+O>ncdB5=+vg`kd!PzW<nCl+'
        b'GI7(+w1Cy>B`WN9<?O^7JF~YGclTE2nawoR68J@TYO{ikT=o*D;Dq&)8^PR#V2}vXzi)3|Bs|0)?E(4o>=8Z-6bP`ApqdHsYq}=M'
        b'-Mb}u?`9R|P>7j3EwHwiUp_y6WOL}qX3vq${bW8-Lo*Zs2)p>P%0uWFblEV75)VK?MT*?4py7wx5#GkP*~K4KL5$hKZzDO`U7WVP'
        b'%NHbk<5JzN&#XWO*+$dy0N2-r;(Ti&HY`JuR^thd0hxE?PVw<ZvSVM{T2b>$b<mH+ezf~ZL4a#{3Ef}G8LfbVqtwLf3JJoSn!(RH'
        b'oFc1VJnq^Ya&7jwL34j%XieM&z8Lto7noz4D@QVN*wF8ERuGUbW&3D@@43C(0MHlNcx-V+1~|C5UsLP(!(T?)NZ;4|K&=$+fsexa'
        b'7H{^FIPvsm+JCY1A{!qaWD`_19qr)v)ozx_@}|9LZ>OlQ(@u5*qKb_i6oV)Tj~h34^3TrshrH%he8P=OaAB^uktDZ`<^;WshbuZ&'
        b'ZrTY5G9c(BIo(+o{Cx6H8DF+=di$0yIQiF=f{wJN?<vGRzf+aZ@a}jbyh`u!5XGDC@|1Veo|sJwA%%PO2a$5m&c56yMJryyhQB~?'
        b'4jyA%-dIXb=jLu(!@>+NXi7au@spy~<<gI`U-o9Z_DTy7mq*Ia?yj6CeGS!VH*eK$&dqnMcx$dsvw5qA31h?WBYN`Aibg&@f0ToN'
        b'4i0TAhUM#!hR^Y<D<ts^A0%_&-)a1r6%uj7u~Ks03W=cf2vwuU-^yLn*f+V!OY(__Xna#5{Y>IX0n3}{f&-d+iIuyO4fPxXXrZp2'
        b'yhHe4vUcnCMlSy4mPVO->sEX-{zM1Qa7d8K!Sag`{KZ03!B)aw?e!q!Ya%!CoWN_s2Xp~m_#-fd6FFPRyy+9D4%_TUb9+R9FFAy+'
        b'M2F<;emSq<c7W~s2pYf%N&V5@7z8h9Zh`*G{4qG&kRuB4l$%i((fk_L^f=-&HTPgmg-FtN>pTBx<*e~s-K6kvh#J^He+luwBAX4j'
        b'aL-WQ1Z0QcotCo6ZZYZ4?3Q3n4<ZG+EntdYtWV`|wrpL#{iVO0)eUS72rh6s$1VR&b&N|#Zn^}HlI5W39N)*F>02*sGK@q4>a;Xc'
        b'g%wtz@SuQUb<w~&l>USX;rIueLLY4Myt}EN>?Zyfq-h6)Z70#*fy}ogd;JxLn|C_W@{dA~9RTnd>Nzkb#ar^G_oJS{O*>GM)^gs7'
        b'J{K92;typ3p5+WB{p@=eFaK{;Ql7se|7{8ZqumsQ*B{~as9w%pk&X?&O?ge+^}OK|RDkDOhk^l0$C}=vhUvXtNDTi-HUAUiW+BNf'
        b'L=5bLH1UVzRy>NxfDzZ;>Ku2XEym@ku5hQzjN4p&)6a^{iHN)Cg3$YCl%#o@hA+2RMdtO08O+TJ5bt|s)2A`!Rmd2-nB3;8V7qjl'
        b'&P|gxvAqYE*1rfk4)3(Ao^DX@d<0(@+%BtMg*5zVtjYkKSheuw^MIQzJ_EILh*n5dsY(KzLQEA?P?8p-9HHK-<biQ+f?qt(Zz8Th'
        b'x2a}%yfl^LDsgjhjN44rll=M$MEW{1B##>8f>tO?+50Q!fIS#X@4+3gFz62XEb7_1$;M{-QO$1pfI=E3g4;!)LA_QPcY*>n&A^e!'
        b'{~F@@{4Ml*T6|75O@55cq3!3Kn$?w&O6IB+h&KfxNlwNkR>m@Rc4AE5hE1{|S@;*Uqg676aW|X!+fDRoF>GU`E>FS+4PbboGYJ}='
        b'eB0%H7=?<e#hXIKn>>$h>i6y;X5h(nR)Py$72O9mNvpZ;a^gLDmM}cg6^{!XU5#yyZ5<d`*x47+xA}en9z}YVj|nY$HpnArFGE~>'
        b'M;mAIka+LnO+B3s&+>+^0Da<c5q|ij*)0GqA|ow2R!yIF`5#d3r2H`Ts!(dX5#Z-f(nsE3smR+;-}LOePGZ3(MZv86Y#}TxPuUca'
        b'ceO&8net6gCdVQau&?6}Zo=cw&S_tS21kPL<bYEq_m;Emm0<3u*U=fw{o0w)DxUt~%=C3xuG^dONAcuiXEI#kuK#qrAj=eO3Z6QH'
        b'$NZ>8arRfNmez}3x4dvRT2G?;e+5!TTrDqr&2mQ{nsa;}A*^P4Qv+L|Vrio3c?w^ph}(5EjX}%mh)>{Wg0+c$-Bkxk2itQ(KbN53'
        b'LACuvls6TDzIJJ`AaSLx;iq($pYKMACR)(*ZQUR*y&7b{0>7KSsl(@_TOp6c&Ae1MHYYuc7CmNuT{p;t%UPLU)}?3pS;Tf&KJ#-3'
        b'FvXAI7*P)sTqr)r&!^u}Y_4VGiGX&-mSK2IXrk@{3;)R*5-FE)18l+qzY~A0!<V)=4>3xu^pg5{Qix6(sr&wP9Zd6#)@jjnD)|o='
        b'SVONvL*N7#W=Ktp8-J%R^iG}Uow|PVX~IDB73};e3VB>%jlROnt<!^DQ^YgkLZ^piO~>&$jGHOTC2EiG?pw1+zBlg6H!tEj@T>dt'
        b'$u6;Ei`ZT=*|!I-mE_U>p%UT`uvGGhWjEF8l)qkw$J1;XqmRa%KA4)U9K`V206R%RIAQke_HSq3{19DrcmgEo3K+RD966k0jh5B1'
        b'tP<$3m=;#|zlPxH#99~}tw@bgMCC2xK!$No<RkR=w5pC)0KMg#py1=<l|t@!6ytkD{z4rtRAEF*9jz0}$-G(xh-Ij#d@7M()zJ>5'
        b'RSOcu<G-s5{SJ(0q33sX1WGeViNy1?NO^l5j%oL%5ybE6Xb#RBk`X&$5C(S8f!A}%qu$V_y78VW@}QHrQOi6cSUHHnJX>ZnZ)SwI'
        b'mhUOT27_dd3?^G=zgu9yv%W60t`5K(-%kVkf&m6baV5;Nem3(uCLkhiSHasr)Ju|@t;8Cbx}XamUs)Gg0s8X{_dN;;phPKM-$j;_'
        b'BpoNbjvi;mDVglNjQH<bIz9TX{ym8>bRU^6gLkM)>4h<L^-aw@cw+?6m#m|)O}1_HeEZ1NH?@54$akcwQCk0ie0%NQGqv=CAB2`%'
        b'B73*gDvm%|Qis6d%pkoPZS5JMx>~s!Zs|{OnM>9%<LJ*g$0*|9AqOlyfID`}`i{b&8;5e}C>V+&dSS|0$nv}ke?EyKhceEM!jkVs'
        b'(GPjr6dB~7?$gj|xHPLXL;R+8ue6R%{28Z}+;#W8s;F-7^{St}@Rs9sdvmL3^`%*H1Eb5-S~aWNq%=Z*FMDs-;uncqwM}QK`}awL'
        b'axFDPCIqmhyNT2E?!QsH^d>DtNj`8_Pw8sy&y-SbDFWEKOT+-oFaNGK`9`FErat0Q?a$h+upz!D0bU1Xej@%vm-+nP%1qXBXP}%1'
        b'KcQTGNB;NP(1luj9{w=Ewf|Gg;M{j;<o0Q80C30WNfgi&bbIk-V=Q<BMT8>x-jDqMrFQn7r}q-8caZHFs}1h~>n2|L1VvtAkpXsc'
        b'>(bv5%`jVXi?5JkaQB(o&|hjh_^$X)xjT~>s>SEP2%fat(+OP*5GP>%-5%l~Q~6N$IXntPJ(1+2k^eu^tw0%hBlz!&{CCvO-h=%E'
        b'QQn|31GQ=vB5g!<hila&QaT^e`D?Z6;>Q}b3OuV&ua#)@ty%v1Nftu94vR{AIGG1(y`j7UaQf&?Vzo(<*;&g(5UrSau9n_ydBjVz'
        b'frd!U+av$~5&3_XrW(z-kk~uhCM0urEjY9PP)o~T42c|C8w9Yc3=rmcSTBTFt&$cN6SbkWwd4D(<Qrbn=On^43_e)~HAskcwTzSZ'
        b'O_Bd{_#gh7Dkzl#YP)`tjXaSA+Tp5UKL0k7tt#^W8@kF`_&brVlHe7o5-x5}RiJngVS}l@#Sz_PxurJKQk&f$!@TE|SJt*DXdLg<'
        b'gKja29g^m9K(#<TI&{5>(S2q5WBCxVG$TF*DmT<BFr;<Haw)#Gh%musdET>Hh7dq(g_ok?Bdi0$@!!;jepB1;k$HYoOL%CqWM!>a'
        b'fk<~DigfO%#P=CH?8jO^8!xC0<$-*^;?mB;Eh#L|@>-&Z9)U+#%3rYL`r6FLYNbMSTvr>)0Xg%VE>e;9-OBF2q974V2c;&_@b?fk'
        b'DRlJPC6q6dZF^gRV`-@TR!sm+6BB4;Iuj!Q2))4;)jCO(83Er%iCl_8<PXAKsixtyWAyWAl<y@sIvm>=#NlMBz)<EBNSDo~6Z0U@'
        b';s1%8RSTbhyc+SS70L%Lv5METb+NV3YwQbPtG|5;YT3M=V6EU-V=+)OI7fU5qt96F9M}xTh~H}o)?KlL2tr+xh#T`9pu1^o`n&HP'
        b'3Y=(kFPO90a4ZTWaOu^+{C*CnMk<81Y5y~UxL%`su*T6NB2?Crc_1LmEpn`Q1U>`NHPw_f)iBW}IimZn#?caNUJMyC9Z^%%1Ae-X'
        b'ZSK2R0|?Jo016CufmT1Q`?3bmIDe{PZi_EQ{(EZfHmDHA^9sc{yHKb5pBlAJrZ-`tK6q41quJpl07Zd`(Uzob4Tm5x3-;H?u&gx('
        b'%l|9YGz!Keye~obUd@UY43NJ~P)`e9G4D&T+W*L%q{6>MW_>sjuh%&Fh~X1BWP>c94Dp<;@%<qoVlQY3GOL@P`DP8y-NC|RWp4#n'
        b'a(kEWqg`x<f1-46gRWS1CoG8L`&onBsxHC2X>STT$dOi1;TsfSgxv|WEEUw%Uqh=3)ArYUYlcV;v^ucQ0un*M=a{{_@9U}Y^wcoJ'
        b'araHMzee^oEBrzN&&=_>USoM7Ar1t5HQ~mD1?DKv!J6hN4E%<j3E5`8$6F&3%aqQ96(CH)u!Tri1M>f|ChSO{@wG-myi(IJl%Wu1'
        b'cGa{vo3nB}oi$)vgrA3#^n8M6e~t2aNRat4@Spi&4OD!84kmaNXt*IEz*08QpB3Og(r$Tc4J~;r!&b5~Qe<Wlg%5$7JjE`NwE!DV'
        b'Lavp?rp9Ncs(zD{Wj!_JX{!lur^_O#18Y;y8m+D`<c&4D#v0m0g~tj13)oEv;@Mtfc?Pr#{CJ+J@oh^8u*2IDJWtnzpH9fX4E9}p'
        b'jjldYYAaI;s@@}>%{8<S7mx^5;}Q9m8qXH`l0bndw?Kef5{SAQS|9pL8^=>q6W)~IvDX035!#yTs|IsqgmaV*=g4ENk?Cc=TF`e('
        b'U4mz0ji^Kxu1Tm589f`o;!xHk*nQq~q+f_g*P<4Cf@fV#xH`f9nm-Zzc`9m@)d`PVt#5u>dPbx_E!zIlSz;}{$xd($r#K2lOlm1M'
        b'9EW%wuaWh!EY<{1QBBwa>hgi$6Ezk~0{9Z%m;kpn2p87K`dQ&h&<Ewl1kZ{Z*-@4f#w?Wyp1c~_F_zK{W99^C)6*Kw2k@<CZ1~Gr'
        b'-p{FsS-5NO(wgQR!QMw}CjH``&JICm%3f_vXV$2O(A2meQ%TY)>9qp#TFcU*IyoNijwaMKxX_&f5)Wm4;S%r7sF_rW(>qmyw3O6%'
        b'S?Z3odDB)KALL|l;h0-@j1k}2=@*(!(0-s?S#u~l?Xh8qv*jr@X^%nuG!x>I;K^>(r5{AyVwW1=Ot(BOlSr<ar7sv-Dl@*O7Yd8P'
        b'F%Edgj3;H_94ML;BINSMq%6SkG=3|ckN8Rw7`|sc)TFzXvP6#8FpoMv-UxX=UQKVKxXXn{;VsX$JXFA+*my2Wd;)6J<!A#~IcpJ{'
        b'7~M$Mn{@JV7oc*^Ze-*`!#5e6aTo42I|DaF!~Mbje}((z&*1j|3*2idztsK19?>c~3_lVR_TDUUOBOD0lKf{~0K;^*qn)hBp?cB5'
        b'jkE7oaBjmbK%Q}lkKs6j|BvARbKJ~xb`^`*zmeut_C!hh@eavX*#48yoa9@boG(vc!;6s}=GF!N`a|3O^*e=I&)EI??Oo8Ij|Z-J'
        b'JTCuR%CFw)wp>?i*(KU?L?-Rwd9erL>>DQ!2Jx8gEOaHeZ6G-Izy)6J$)FqUlz%OrF|mlZX&DFFA^%EzJ@fVSB{{#w6MoD>U*)!J'
        b'-?dYV?Uc~eWB@i(qYrRZrNp1;relBx1MPnuMuz`R-TW0E|78}shr4U%t{wT`Q#!-OlGPgvv2sb%_f+dUo-TV|r+th|yc+3u7k$g{'
        b'HZ{f#%pDZu&&tMqLL|&Vpnfoed*$tRuZQ&scKMr-Wn*8P-P2}2Z$e}<vMEwZWNf7Q>L@=p0dk>D&@+t3ZTATfL(iRvtvRB}&e&IA'
        b')IDGw;Y)Yqgk6KVBpEqDT#}uGf%+ULgR+N%#1aUSJQyT)+3^H0X1JhN5%k&sTC=w)f(jdI`Ay>NIU|4C4o2o_W;6i(y)_cT@rQ}c'
        b'_l4_bZ#LlBRBPAS?V%cbU#<Nc7CvX`i8OZj9JJ3WWS2Z;2NXVsk#YK2goU{sIo#volssHT^B{g!aYQGOe!`T{@J4auO;bX6><-S-'
        b'vS;N*{EgBSgjj8NV}+7P+JMA`;mJr+E^@%raFf1&O>XPSIQNS9M5nArG}$SpO^qZ+E{)|e8)f$@>)0W`QyGcxz#&tWW`kUuD<YFx'
        b'YS&64G6Xz6`G!BD44a(>UyV5J(Zq12`cyJ~F$ZyY^xjN6G%XQriLgA7lkE#v!oH+Sp*4hmR`$*+XFBcD{O_23=f~OslvxFiguaLD'
        b'k;hL7u-4f+1x%f^E&g*6m{7s)zbiBDhxsD|Qz=G*3b8ERp-`Z+a~po(ZrWYC!Z$aP26~a90AJu`74(^j0XE8n&&3zv>-qujeZoes'
        b'IM^ykJi5@mKURB;8$ov$3L?El+c6gXsjZDI>lBkN(Y+6B`h(|KCHN-#**6B*=hdEW>%HvQEF5De`fqtZtG<_!Ns`alV4W_JtP}lN'
        b'Uirh-w6;$UJ%{qKYDTwqv^s#f_)rO5szUC)S#&CR0Gon+vmjnXoQ5bQqeqm{6U3v*l*ZXL_+Qm&vvR1FnEdT(4TfW*ta;OnjUV4n'
        b'l(Y-+KTW&^i}xrrjoj<>JvOv$4^eehCA{l9QeD6vWz*&x*_P{+G@b3=Hi!~`VnnkYXqU^4b%<RO@Gt3*yA*A%r`?K<OqUuYs5^8n'
        b'J^0sml(<U4e`$xwWd{G|f*0~H(sjxDWssh`PATNrUE7rE0X^ZUBu@t48W4@QSBKiGJ?+&ClZa|a;S+7J=0o+&x|cUstFTc}6by(#'
        b'g)(%ezrJ->|4<Ck40EcS%sMk6qOG#<LL}HDCOtt>A`)JNh%#m5XR=pWi&%I}!}X6BYjO7OtVQgPUtE1oFHVO~0)ASYu~-)b>n$@V'
        b'ibimJJz9r<d|-K1J2sq!jBl$BZK>`jcQ%OuA!m~e=<UAlS40D5zoPpULAk!H)UB|uE-y{WQw)iqJHRqlDhEwcB;~13iH5_}Kw4^)'
        b'E$NFd`^Dqyt3&Gnq$*EYHStT>&B@*36VMX&_vO`(51d;fzIoDq@Ol#TzU;e^cs*+1;Tyu^>DL7V2{&?Xp8Wo|)yIqaep}u0AIB@4'
        b'd@&w%-2PU)^!P42JW+9O&Lh>0b#s$O+us#&&r$7F*iaSgd=>I_obqextGG{iXR|vNK$n`Ci>t>tF4i*s;rQ`iRfn{oLC+6=Mj?H%'
        b'w%}nIC}jDB8d|`bNKeWd8lAsj-xuSLREIJ^u9p09%HJ@^em9#?!!fTDp3RoF+|E5MD}F;p_{>lhZ}=9@9_Atb#>bzOwjlkd;)#b~'
        b')`=KGT3yDk=9f3YVVS?+#ff>-E>=0qy>IsJ8~US>85*I^%`?IbL!%*9m<xX25UfanY}Hn7bs5hP%k8^VwXldtx6$=W?c6~OA0?V#'
        b'-Eu*-c1dBr!pbSNax;zvp}>HG`3^l>-XuN2?jMdJZo#;mRZYKF>42p)fT7biRr3~ch<#>y=h+@v@j90MdYWxH_^(Qlm;FBf9~2-;'
        b'z;Q~#y#h}-g@>L06LWVzJVQ0iz`Ij;pNoyLydLcBe&Vui?`7Lp{0jn{-~308*TWeWK&fB%!^)X7bh^jU{io!hOWd-@ubONT_rN9K'
        b'`Na0PtEI>C9eoj#<O0)3lZW*B|C^2Y)FyKU<saD`jdB&1q)1mqY?C~Prmc~mv)QnqRcw?8MH1vyv~SD?PJ9883wzWzY9mH$uL^rz'
        b'K~OfS;M{5PPYY%9br8$a`Q@i=%TN_IG<sbn*?lmLB@fxsqTS8yRXidC0vP{`4R57|D_VGNyP7+;gRK<RFuLMVsl8gYCLpM;Dyv%4'
        b'RobxzoZhne@_Ex`5<m9nYVxosxLR}wP$%6!@%W!@p+DRDNweqAHew4TrkYPCe4_X`J!-ti7V?8H8=J0EYrx4YgCg6cle-n%FR1}x'
        b'S)wc5mV*o23#zk^^UC8YF5PC;arQ)YuIN~?LMuq-;0aZ4JlQlC`Q)LG{S{{)`10^2JmJd#peb<aJAM@B8aqX8ZQCy2_%g8g9e-x;'
        b'V6gX%prbZ;Jn>UuGN($3<)5R<7Pzr;MOk*Wq+IRhRmXviEImHs9TDZfOCj&5MCUdI_sr>7v71Wj>|6njoPhG*;DAbnv{Qo(PaMPu'
        b'0xqp?iFkacEwt0t@7d<rX(N`ve#*Doyd*RQNbF$p%o*Qi3vB^;o`vsy5&2fzAR0i^P-3g?9`5faX`uy+q0s=Iud(f|vEfCXd}6F>'
        b'uie&eLx@jJ5LMc2hxmZ>5-NYZdyn;3YlN=`=jlA8w?amy%X%M`={DF5R}tc@Y42H+o87(<rIB%1ir8Yx*j0~)-+CEalk<1uYMFHT'
        b'9bYW+Rm^p^aT97>i;^GdrmyMFeJGp0CYydW*lW;Dexbvq`<FqLsL3-y<7n`UWRBtTP3iHQ$7A}I+YYh)Nv^1mdN^Gjfa`76!h9nm'
        b'Bf~GhjkY-P*aaFC=PcsyeceR(Og&jSkGR>LG5LI?GwR)>^v!t8k4rE;iRAq1Txu|9F&?vE35v6evx2!<LHHyuJO>#*M<H#tAU>~3'
        b'gPkXlU`6oU>fjf#9K+Qc(%~D`QRPWp?VudIT^q?-B*<Azv%R#PyN7I$n|P4E&P%j8Q;_x)ct*DlD8Hcyr)e)?a<e+40Y4FEqwh0`'
        b'|FUW%j#r!+zs$_gIvl(E0rjyz3j_0$u1bFxOb{Ss@%Zj6%t<1>{XszDhFOt2!~oVR316q~+L^J47~YM*=-R0&70VT!o{mR%t5KZQ'
        b'a`HqLQ%?6&6{!DO6)hPDK}HTw3*ohV;`^#u9#Ho^%y+qpmWWqne#c~0L1IP2BEGzvPnmURnQ&1Q@p)B*?*2#BJ-Qq0*+cxa_`C0N'
        b'pyfx)C1@oF4gWw{etCy1f@_EPu!<&>*GB>RK=wj#{9F~D+`JgY@#1~KU}x~`9MwEWD<Dmpmx8_kpgsN!1&ro^Xm7ux_o%}%123Q;'
        b'-FJ=AQ7$D#*^)S~0#i1`LsQCZ;xBMTx8|rMT-w+U9IKO6etv5YK8L<bTxXf>6Y&O22mB^sxSJ;Lt#V<lDmdPFBJo?8eh4#MyaS&y'
        b'+>F>T_1&f>gn)dotOV#fydF7(`fgB+r$0unL{|B3-)BQR^VKTZkjxJdUib=yvk#<0(X_8N-p?At2HCzJC<xh70BIbb5uvSAGW70`'
        b')G}<5aN?r!D&@<ECW9=6$VB=W3x60-RKAERJRCz26tvEp4zOrX?b5_M^r3<brL)26vUpGcZFrWS^6aYe-Mr7Ix=N38rRRCop?;D&'
        b'E<TRVghW%Jj0@Z+S_7EnHDtZe(8B54T$McHvrAVBr9w`*uskst?+?ZA?jc4XUN6myD@8@6dGV#_qSCy?QgmTyUP4)PE2l8FEV??T'
        b'oL$B$j2`6_vI<g4QAtu>VM;-$BCjwsJVmJ_^d&ltKbFX`0zJ+%lcba_sy8hzC8-&*cZxg*o#Z7_iQit}J+TlpGQbXZAqHVodr0IY'
        b'9WCyDvNynAh$o%|EcweucuOZ-h<ig@h<z{u{rzn5hBAo%n2lw?>%7+4m<aj;a?QqyVb0&f*bpg;WF=tqJSu8Oqwza$&y3C8-R}*>'
        b'x0|%*O`0iF4v}J_eP?OU%QaK-oQZTN7XNX_950sGt>rnfgdSIOT8c_CJWUnE44;K(eMn?KKZPD0Li_sB-rJnr7oZBw>xe?W*opSH'
        b'C={l}+z_*_{n+6|m#`!8KzwKXfi$<krHFF56~5KdVL*F#V)-{Iw}g9>$?F}`gl|y_g-}}0RuA3Mry$dd#YK;uTPz0H4svqpjK^dv'
        b'BvJa)hrOrs!X@xEs_bA;e#1(7b+R6(e6<y@m5L*WLD)NTtLLDlL^``h`W2XWNR;~lG{vf%LDqxy*jj<J)Ru&K)A}=-02>NLuTthS'
        b'd3fWqjqEh8d6=zPF3sZOSXv05qadj?aav?$;mLz@z`}nXkX?pdoW4)2$s@|;Qm|@2!>fhWcUM*xTv=v)oEa5crH?pK)gb27$Ah_l'
        b'G#(6a#A&$_K2fxKoC>kgCNrDGW>lgI*%jO=N)z4mcW6lLV+zqL#fl?$aup)z%~c^Y6&V#4u|gTIw<JJy(o;t0HC`c8SmKL)GObQq'
        b'qBZ&c8*Gr)F3>-)HuHzUq=7upI_`&*SI(BUOlyP%i3h-{J`kg2YfMpDT9aj|H2*qPr~|uLTapivgx8YL6ybxt3f8P;eWeM#hZF8g'
        b'w^ZJj?pMRt0bvUoc}oL!;u2{D9~3(lLz|zcp~gO-5l1zCwXg2Jvj3a!%2oG$2PeG5tsok#TD2P+eT?{M<2_m-fQ5fKTTkXQRz(V8'
        b'P-A^ttX@(TPM032Ahuf565YbI^t7C`qO^)Md)ltFmb9)zEEQt|L#01Z?^n2lE)}ghOKgB!r?m*|@*5Nqu?cKr1z5J!NiIS=*1APK'
        b'Cp08-`__OuY`*!@Iw8~|9%1hk?o8ZSw6kKTedn&7Ejzn*_Uyd4^JcwWRBunvravbHSRU}D(B9ui)E?o1Hw_hRO=&BuI$F!cSz4(^'
        b'UtK!Ns@7}FNm*Jmd|zQ!@T5(*vR{rjzA5t#B`Y6{SEnKYt|l7iPO^~vOB7;Dg*ejqy3A=p!Xs3Gt9(f6Lb=oTY*rI@o`U!Eq-Z6S'
        b'Q+8{91G!w^G&q+Rbm;-<#Y#h!m%!0>%kD=tLd`w^cmO3QbYmFU;TGuBeqyBK1sB>XaHoM*sygE}+uSdVvfSHTFDAL%FV36xqtX@%'
        b'6paQ&BYqDe{;)1mD}^NztF(w)Cc(J}l&(isbO_ALC4-#Dy}s!9G9_4ZrSlP2jMTz*$4YJNa(<aPz>Zp7ZdU#U;7p4|T2TM?Yh`TE'
        b'lu{)&$$|58?J4?7bmAfykwJDCk5{n+Y?WjZqm2r<_4(gW<)z>UDVU!>O|54)MeL*pSm7x|qgXFId`crpe%F=Kteu~vN=tcEMO!}s'
        b'T!>zev}7q*xT8W`Tq-Niir9?lyI}E>4kcGg=E&egcimA&#XA*fD_<M$W`U&{?ZUK@QN9*)DIBZCU{DmfvTXo@Dy2LtNs*Sq{f5@3'
        b'V23|Lh#ce45!BHma$$#ee4@ey`{yN39v7b&P(<O`YJA|)-T__rE9{Ye!$~BmbNENf70<m&-L(m;Rv^+W+Dn=~1+}o_11u#XUB;%-'
        b'DKe`+5y@MC)svL;G#lsJ=C9`m_;^yo?Ph7pWQVxx#UTNneIV+5A-+Cpv?a*}R{HkjtAQw~l7dFy5%YZ1Z~`iTu$6b>K)Y|muH;IU'
        b'KXI>9i`e<I_E;LOtM!OpkCy7OdOgdnaI4*Vcd6U#t{>zckm9$zLww>pBQ2+L>f<0(J-=zz-T|xOdc)URFl<@{*wXrTeT;j`X?{R$'
        b'7I}yAlvm=^=9t;N|9F3LtM>>+5SCe6xCG)-H{9&*Sk~}$r#gTpYoB#<oJ9if2<kj?2W$kFK7hK#PAtZ$;{#&n&{nS^W&rH)g>zhG'
        b'V~l-hFl%ZE>(G>QD8Ata?tIqC>f}G};xc!0uBmqNxiMD5&1P*fUARNo|6XpdOWaYtaE{}oV^VM*jDE%3Argb@eLBuCa;Ia)HDwi`'
        b'?wNLpEXkGB*<LDhPepWsLAyVT>e!!yJI{(*Z7Mxuu1{WQfeJF<dxx4Ruvi6bt^S@pKu~|^zcy%u0}9R4V23ReMrsDwtKquWEOJk|'
        b'XPjmh7`N~R3NChde=^f>BOu7`NYPA{lFt`sRd&u46_gIeXCF(XUEOgkSK~%2T&PvWDV(8M?mTc1;I!FD`s@tN2Wa&QWgd!$K44e@'
        b'u4N_;P*pvg0wQ%j*0cy=eD(RhjWeVR0;sPCsh6Yrp**nhw<l_$j_1d;(FEwfE>16zMdj&BWqOG`3H-|qH#vBWZ6^C=Xy+nlalusf'
        b'F{o?<w=dZ9A5eM}E7}*eGkZZAteh9%c7`k$<2pi@cex0wisuC2T+ULNQzDPro&-YjrYn>+M$DK13V$3YO}x2Y*aWa6V2;|}jrdIY'
        b'TO7pa<VeIvvgO0L{0kJqxKx3@FD_Hk^dIxTr?gYh;y)OJjErp^YAvBgjX2ml)gJ9$GrDmZ|NOh6bB{K*?QX0NIU1p7oQe1opPt*@'
        b'c!59avUyxwGx=Qen;g@p8=D?N{4-~#NX^q;@_F)b<)Lx!5wz#@o;lyl3GUukd}-g8{P`}T$4?G69{AJsy@UL3IAiPpY8jyhSz{=e'
        b'PT$+qGGX_Uqj&-?EbfASsXPB+8?QR*O=^Ur?;VPF_k}-+s}oKXb)eR?h0uBhICMV*DPW1Pv}&k)1zq{IA^i)`w-P1vi~A`G&@eY|'
        b'Yx>|-DRQ2No(ss%n;r;<;?Bz-Xsz(_u$-PleJ;XFQr+<!FAr(%I)C61{MPQb04)JB5-)B5JLr?|4JUqb?S(z^A4v3`{>$iym&a=E'
        b'>V878;ML5g2aqRr0|0NmnAOi?b-%LL6?zN8n%CUb^l^;BM$jc4FN=CQN42(p7`Q*WJf__nwfv^@5V>@}_^HaHg_rkm9*o9qTefTi'
        b'`=Q>1R?kxUoZR5HjNWaGyU8#$S}_m;UH^cJ_$)6_Hyq7aEW&xavvBE_W?4p4qa$M**Z|x2@%5*%+$D|Mqvz2ZTLZ9yCTooI*-5as'
        b'R?ZF_8}LvpfQ*Jhs|H!1-@c)^l|qC4j#(aSO|{x)tXxcOe!vVixYb-LOUg2n&sXgmx2YSx+%Cnq^$5;|C85KvzrcctN%f#$_M_EP'
        b'V0CDwvfsqG4<dB+J7~O;CEk$@{kvr3oSft#2YPT8_bCK17;c)ujsZ2uo4%lutl2Lg%Kwhiga)QkSvhKXEcE8f(dxnjaRy=Rz|<HZ'
        b'O_Y8RzNMK01jLj^XHDU$!CuKym&()t5cro5|D8h2in(g?`HUr%YE!)P2&E?B<Ljy{jGKwj{S9z@N8=2iJpkG~x(1gvT+dHKta0?_'
        b'viyZI2(JMo3EE0;E6bnb3^%XT%jW<dL}^F5<HYnHJV_b4e%QmprA>(lQa_Y8#)1y2c)n)JkT^3a9D<SX9{?HUMKf`!vMcWGL^G=1'
        b'!?M5s@qlWO51J9+I8BM?O$p(iIHx@Eygb1$!u85yQ`52Gd<2|W@WMEwQI`FdaLZft{yj#4;#p0j6k_FL!+(I?Qk!Ci&`dQ+^`jYT'
        b'6RKqvPx1MX2Ckb#UkL0k0NikKvR@w4{3w=BKwECTl=QQ|Yt<`-P0vvXSVmS+Lt{3W)m@Zkrk;E*`z<VgI~5ryr6<l%bemok^BMm}'
        b'@ECYC&T!(NW;q8iV&O8RTRN9Ul|7W90!$3|I|@+zQYi<H2|VpA&r*hwNiPZ+0iQeW@QI{G`@a1H%6r4mZc4Cp!C`0z!%%UJ9tP&&'
        b'x{r#o+OvkgrjlGuGgQOP;c<!{|ASQ1UJCk7^<dJ+c)7>KI9qQPfkXAUVm;b$O;1KY`vTj%T#&T708q9Cix<uT=OP<WRXEGgGFL4}'
        b'Qd!t=8q)X2N;NoHyhwOg>@uOWXio8RnfWsetX#lc)u$upy-586))?!=F|cf(6Sm&O*@bFAlkALL&tv>l?_urWTY0=4@u|Fp&a>=h'
        b'>0=Eb3$&#8Y^+AzaC${FKYOuVf8_d#eVajlPE+fJ!!+@_LzT+o>~;;$P{<BVDv$e~izaHpx!L^kpSJ$APX7V6JqBx<ptt~yspUM8'
        b'2Rg*)j^?S4Ol#5nuP6<wCvR)j8nITdM)}#t9#rdNnx?3R&sRjhWMyH1$!Y*Qz3D>=3=%s0K2=gznSY*I;z0^#Jk^z{>?H+Rsq8ep'
        b';(=1~xfO4~lWK_eWCYNzkBBqaQ5%t(nrxd{@v;bvI|_|LJ_}Y3?R_$7<4P`fh7y6(iw#y(L!4pPowNTOM7^i-ENdu3&uvj3yq>b`'
        b'qzo5tnNiG1K3`<5(!80JS9R?4AbX6y<k=AisdMFaN@~9YW*8SXeMQp<16b?t0MO^-prT}i*3*=FepPw6QloYrneNDHPLTI2Snqkm'
        b'zl)<+$<DZeb^r-1;C5UHP(wRxBb^|vxXr!A_#Z^1l?y<%dNZ%w>AOL_S0CUhZ&0R(D;sXES@OWNPh4R?_qy2F6P)Z3Ki<<9U+F84'
        b'-6K4l{&-8dFv{{O|K%n$AaI(*?Iuy!M77IBQP%c%S2^Wk!1kLJT&I~UHE^86x7t<6v|HTOan3Dna|NN2X49+u{nAA5yVLFO9%cYo'
        b'o}@rQ0E00gYV-$9x6Od#H}*J9WoBcK$b96mk>U9LmeN?8St?DgScP+;3YHx4n;|1=?+O2vGVJ2}%>eZndmKs|)jBd@4)E+JEw;EO'
        b'F@W2yK%8=1x-+ru5cHhQ)a|oG>b`u!uj?LI;4=Fa0|L7%spoQ32X>s_84oxiL5BqJp#rz$kitB?Dk*PxlIlo+2K(GeZb4`KaXxIg'
        b'T7emkB5Jb$Y{)QuGI<p!sK@dY^!d?x^B*6Y$3HapeP~{~kobtcj?tA#;Pe~{HT>{1!4^JeEDD}N&r+j3wvZZ?*t4{urfXCx>tPMn'
        b'&@_aKvq8@@5N8Ujs)MbG9==IUq0#-QXojTDhX9x0+f9Mf3*`O1G@5J6S|f$}fMt?~FI<mQb;JUMUk-54RcKb*R~85UcuGSYSU8`7'
        b'Qdb5fp!|PR&_o$&Xsn7Amh_k_Dym|!Cctm9!mBAm`V2#2t%A#q=PQj<l?K>`p=nQ-xhX^;_cvvT)WME8L3J3kB?{X583j20rne}>'
        b'3-;j~)Dyp7lMEdkmVu6eUUAP;u#G3mVuydC!1Q7ElllKa?}IT63KK2A1z1br;T*VW7AobxH%~m<x7F+=MaqX`SAul3b=M##{L`I9'
        b'+`?I%Z&|-=h-5>Kq7DxF?*1WCMA%`le<&VrC92G`d<MMJ8Y0n#n}nIknT!)g7<#lHPbSvimk-`0f3ohLOd``_?yEGz8)yNPicaL<'
        b'iNr<7w}SGA_@leLDToh8W@U&V|5`JxP1L^@z5~YOWo8vN3id1!Sjzx)VJqUlQz^KSw?T$zbiCLcDmHsc%>85|@wW}McFch(m%@*^'
        b'S>c;h>n>MftHv*3US{{fwn0mp0OX(VYbR8>Y^LiJ;%5$DEYX5yK&^>3nC8hg<MAEBR;^3mJd3)qLZKUQ4%(Q``Aiv{!{B(>{)f#G'
        b'Wql|70?*?a>VU8>)!dQpit6r&?TjMY)-kV)cdU)PRoN3Ypz40*dZ!Ao9<;xd-apBR2jQr;ru&7Xv>#QMuvx<Pr-QloCr0#i!9u%C'
        b';qwoS&<<84W?C9>IT3#xjPVES=-6lxewwD?qQ;}lfG&z6gl5`+-%9?(mBah+5uyk-Lb~g=Hc`V#6E0$1HeWubO+UnecbOgR{gU*8'
        b'`GBd=#^7wgyn|Crqgt`=dYX#M1GA%2H2pwn=7a3>X=d0^d0RDqMaSP17TRl?fgWr6P89WgW5O}w6co0aE}06r3u3V068L8LTbR^W'
        b'xOOVE<9w(Aa3Qc{s*zq%h6+i&{Gm+yI{DvCIoWE{L+RVsv$yZ#fmNOlA7C#8q?k8UM(|-D<R6>b#S3M!D+@Xy0Vn^^M2F8q!EhO<'
        b'=tEc$p0rd*>{&-cm)d{YJ8J4jD>?+n6FY_N@;E%XGpAi1-&xd-uI)^3m(Oc!W49M6aY1{LYA?%3TiC?~q*pm{^YW+ddL@*0ZuAbt'
        b'5Z58ZTkP`w^_cpUY$eA1h~n8fLE2{w>Cxr?Kq0Mv^YokA<x;X!<jGmr-8qCOG<{2T9P8{)I|l7GBhZ%J8O<934#B7Aj@9%N1rAEk'
        b'y>8g@WPIc(jLc;k501-nKn6ZYOu)_LdC5f7nP%@lpi_cZOrcjyo&%<S(oRU>p3taA4}$go{p_04xlN@|8c%F6(O)MX1L1W{So+v)'
        b'tzL6fs|LiS3tJP<?ug#sk?4}ZP|E%ekzXMd-tIpYLm24AQ*?{Y`z>6%CEH9cPU|PmBWO$eL|RK@>sPR{@ZTwE&z&avfc26wM4$q`'
        b'@Uuh9fZD{g92`q4DonRr0Y?M<HZp=ohS%QPpRiBWrckxXQ)TM+WD@^a5BIr#7UwYBYxqYf`29?In}RkZh&R_p)a*f?3!DjTe61<8'
        b'*5ok&0B4DD2*9s*da&%A2P^hDJ?#BC(gC#}Q((#yM@MJIq6XPSiHX*_rZv3eI+N4GRbdOdz8hl`kDDSMfFN#UU*N#@J!T5!n>@b;'
        b';J+r0L-1$y0HJ3ujjq_|1>l!Podw`WP7%K{-G^5rWfz-5T9YROl>Le5`9G9hcwgBuHt18TDYVe!k(>IxbBP16U<X}LD=TUQ1)H_;'
        b'xsGEKstm_5C{6am4xTtl$Y-I@WBUznjBZ1;DU@XLJODubf^b7nJ7`eZSq!M`hqt087q)}v^>DX$Jm^<n;PzyBZ0j?&T-kMuJSZYG'
        b'a4C)!skploY21jfrajmo3&Or-3~@}J>&AZ1ABlQq=oN72AF9}=fI}ar;4A(73H@2k1<uGRKwT17jd$CK$ft~eL{WIS`@6mseJ`5|'
        b'u>m2#3GkJ0$p9*HKujCY;=*O+M~OJt5I{Xc|CoT#P_VrU)&-XDPRu<yI`L2AN({$V3@CiRx#7xbUM$iS;R!je=3{eT#q#0fMkFT>'
        b'PgtRuZj)`hdq%K{M>o(ms*T|6x;g%VG4z4a^MP^Q--u=F@2yp0%-HagpHKYNcwgFCBS;xF&hF975#xfCBH~>m{RlNfty90h6v+}3'
        b'XJA5xI+&4h6_9y7SwzT4A4)_J{^vS%Ahr3#JmMsbf^c_MA|n&cytN@mosp3V`2^w(__gUrK$Q?jVK7ruk)8MvNq&IzhyhlVrORlW'
        b'@pt9Z;co#;h7hMV(8d~O$0$6_+)d#F&Fuo^so2Qq;r;~!;_*KkLw_`S{%Gt!I6~ZkILTTXL%a$rTY5cts5$X{N4f~&J>*(xG|>Um'
        b'CoXzkG^VF3Fa*k^mH!nh{p`-PQ=G1vR)`ft6M%D=jUiYrN$w?OtGNH9=zFx$9KsC7&ud2HO-5-8;v14WNrY7GW7?NI2+ai&j@cCh'
        b'bsC>HE*#Zhc$9)f;Y;-+<q+fO_zIl}*Qc3?r)hbt1m}~^MyF0hJVW1gbOlg_E|vM{*<>6<iLG?YyX3V-fKWEW$mobGT2tDbCCprA'
        b'beE>FXmZxW&S&J79<$MhAotxHR~qrr0#>Hkh(~!(v57t9H0@*5s@;mhh>H?NhI{~9dLvtlPdAElT$yFYmMkX=yJ!1duUOPizBa}_'
        b'(GTYI8U%7cI9_55l^8uGU{k4xS0hBl8Td_JXzY$bi&B_3lY^L-4ECE4;<x2ALUel2Wx@gUK+oPhV<^uE&NN>4eu=et9wb|;D`+iO'
        b'6jnXiEFN*W_^msVwhv#UlA7HDLSvlV57-rlmwZjjCl5MOu?0kY1%2cC8vQs(SxyVO6_txhD}Pa6`O9YMv7KDnIzE02k0MsW&k)Jq'
        b'^|y0@^9?tZ^-yYbDt<j%BY!g`W(GqR-T>HP|9{TS>5A%X7a%_-uq{8#-g-l=?c0o9Cc<4#-x%X_p|c=Bv)`Q6U*7{Z_X1V4Jj&Ps'
        b'Li+~<a-k8jSWXoqOLmgK_L9f~P4qOhpyZI>da6a?#ZaUtMR|*g$kySS+6pVE!{j%f!r3Zpk1!2w_;C^YRW?3vihOM$;H_8e1Eg!o'
        b'%u|z##T8j)Ea^*ZwQ^Cm=CP!Mg937}@zyIB-vBM+y2YLHPcy&P&6qgEJUCu1afkeq%&&CUOD60YUcdx3ALVDf?(hncAG^5O-K^(W'
        b'i#SPn+*unTP*8A<lGV#dy9`&fb`7$8|3j&)qxI{YX}pG+CMlxf@+#L13cabnxWE}>PhtSAygb6wjXi~905xueC~@zpr@Ultn_Kp5'
        b'%cK1Q6gin<jrzrOy*PdQE>}GtX$Ti@7nP>|vc3Q*EkM-;u-uxbXpA++8H6D7FH%X0M>|1!2~1Z#E1mkWfXmxB2h=*q0vYh3roTbj'
        b'8s@!4DSv^gg!v!SbH(y~Mb**1#mA{u=|?>XzE6ua+@$B!B^}kQYs~+N0%WCGLid5WScPaDzI>po2jL&6$o<tn8CaH42&?NpSguqE'
        b's)+&hz`fz1(cxV<k@d&2{GEXle&^rYwB-L|n|z;9E9w57qFQ4<+Qq;EsM)m*0^;7HRBWDk8F@nHo&O8?*0$=YMM5x;cOcGXHvQVC'
        b';HF1-U*V2^_JQ4aTANGed<<%UU4xnOFH;eE8ea-F+V9Gs^`Gm`$57{E7<cx42<;<dJ?#tq1l1b*FMay`Y@awh^BmA8<uB-=83sc`'
        b'cc$qoGgr!U0LEwwo-$h$!h4HyDg_1`0)`g~BmM;jD9XTK{3?MtdhcIg1lYb2symjKoWi`qfsXEdGG#v?*5E~qua9#1=%M<7Zr|K7'
        b'2pg;_02^M!!v{Aoe0g>aoB`wgFKx60DChhrLs_JaaKxiP6X^kmt}7$HK$-HPe{Wy#f73qyZ2P(?*O~v<?Zbs&yj+P;{(=h^vG3W='
        b'5h~xLTrE%<b&tGZ@*ksIy8uqQr@w#;Ek`L=4urv^M{pZ14EIsa^jHS?{pprokRJE*H02SH7VjC|0Qz%(x(|$1y6SE-nDU1~TJpcc'
        b'4flZbdH1D8+H5%l(jWYn`urg6p`Yi4_R^|#J4-CDQ%<?)E1es4rl(vlfjg5vy6=_mJGjAfaKjLZggrm=+ikgX&&Mxq7c29X4d)nN'
        b'9hsdQ@Ob#hj3v|TqYc_Y`^DE64A93bv2R1V%gINs6-<M2ZI@VWud>rS<-0eWbJIRJJS`hq_i6cs@!jp?P&w`pzcW7KGj0zi|NVy4'
        b'vY2bOSh;gUswPU_w844yRy&C}()Q85#T*+_cU+Y}x8cnl-^rf`->!3KeS+eVclCSM+@k@dPL>OMTjQ4;NO#3w+wqHQWreAlC8-5V'
        b'y$aNljrbL<7hPCCUod@AOh=VVkbV-st8a<Bo3$VKG*YNRj3D7XNIw0TF`OlZmK>CiNFiCp*k{7|8MM>Ii5;?*#tBtNv=)QUMy~Cg'
        b'd#$`MRU4C9_)B8-20(G)yNM?^>_1ruPy2PdeT$Go62mTpSh<1Lz4A37hR<0zAEM5F(iVOge3lCDgdas19io16n=c)vjok9BLg1@%'
        b'm^NuigJ~^4DYqc`-%<T6ftSRTD#UBX42eGlFw1w;@E5fIuf-b<U@olntSdgXZ1FW)RH`N+wLs3ybLtNDn>*4x4{xx#zQLoK1c+Y}'
        b'Za|pv1;ND#eer=O`6bHVAb^?$dBCi}xJ4ypcu`1Qc#`hcacu{Ft?ZZg>cHKem<`R^AN&%Z6`}hJ09&59SH~}59RPk&1g8zMJiMPn'
        b'TSP;9C;|;(pjj&KLQ`(0p#fNnkYNZboDUC-B_X8b>Uyb~Z&o1Ek9a#2(q>*MSFqxZbTB&K0<>gE<T3_Ed_TZg4rdSzV1T;?;azME'
        b'rf2b&p`{AMtiXmif~7S9Ztz(Lam@ghS{b(PJ&+dQ5kDAc$<&$`=Laz5*AUl@Xs|)<5K92!u#zX>(@qh>h^~-|mn#lB1yD<~*OlQc'
        b'L@M@!7@$UyR+DrbN`Dw$n|YrkKeN8|M2E0-XGeOgR{1qUGldY(f326!fMqWAvkDZ_RV>)>QocZWnY!Epx-&^#PIO@v$A<WfEO;WP'
        b'02@Sy*nANCoEoj5rSxClecwm`+Ew1OUV4cYK#%Ld@iCyolLM%49QuT$k!t`|UV<-kipIEu9MGSuATqjZkO$JCFd%?JCEv3QA47Dm'
        b'A7r`sKf^b~OY5P|&0YKqEj+XyCEC{GQMCH&tS+GodxGmIURC6BW5w3siUH0JNz(S6lDCyri!<Q!8&+|T!#FG>EO6BIr-Mby?O9LE'
        b'EhQ22k)Uy-X!2Q^;T^<qnv3&?B?vwjoK9b(;Z=xJk+8e|E7SmRRlL(2=QJnGDB=Ku!Q-dhjko#dhmxV^g@B+FRT_~FbdM19OyEY9'
        b'#YngWaiP+In{ek^<IjQv!fTG(@|JAMgjiN0U!icm6hq0z(?R>u3NP_%1EV?!`#40}pe=F2Zn%e=X4B~QN6w#i5(QjVt{Y+!S`B=R'
        b'J?hVJH;$G8evw}DLi!mC<T2n4f&y(@sXXTr=elGL|1;+b#a<oaAg_9Ls8h#s_;tCiXPi2AuH&jx$H{f+oI0*v$7^$}8X|Xib=cBv'
        b'j?rNAV$Kk$0fD|uFfYCzp+&V_cq?2*zAxc<-;?~rZpZ>f86w_8{;zYRx;r;_R{x*ohRp+r?(W<u9|iqMzHe?4o#x~jMIsmzoImZ}'
        b'=T#)Z=~0bAr{0!)WRDP}4D#G4z||HFoSL)r)F5DPz#xK;07PVZvcUAvZw?egs@eJZcy+|e0X-Mn=()gtHa|?-ZI};FpsoKq%}LAn'
        b'k-1_N#6Vld*b8FVK4yOY|CpE2bzrMrzi(c`%)Bhb>3Q+3zBex&m=;~eZY$oXCmlIE2PDOLL0pJS_h(~(i8*22iB(Igy5h3mis?}J'
        b')k!<)FJ=<yvF=ou&8)W{S&^0L9V#9`D|*J*#D74*Hq?2_QDkj-q#CU!9XQ8)#9^!yZONC79y2uZa2_`n!Fj_sDCI+-<JtNlk>Lj0'
        b't9Zn^OXro;c8YxuAsym&^I|-q-JCt6SPTwI!F1QY0Tkr<hId<VeyDhi>q|qP1C#kk?lGA!0r4dv(gimc@xWqFU=(qz38!%Z_zvI<'
        b'vVBsB7>%cb8dNb<Y&_~H_Bx1-^j!WeGMAI|ywS~{y?6Q9Tv@)EohvvD1(JRR(zZu=u18GzW#>A@xqFn3PFe4m^4tqzN2`oH`^=CI'
        b'A%j<kbf{OyBG2mD{LgrG>^3-`oOUp8ex0M^nRAbe+jV?L+tqfRz^RLJbTE^Q(~~?0O!ANpbL!^mbr1A9HV%=~ULChxC)AUhXXkng'
        b'oa@qc^xLPE!pp*BoZf>|w28z1A(2Ay$WlC2jXr^cNms4D>&l1Ge*$SY*WNWT8o{e<&|~6<wfFD~q>sM+m-xlC_rGUtRRf~r_51wo'
        b'LSpDvOhgwZ^2p%&Y+U(5jF*&!Ke-W!FBFC+Zzvn@zMqq|U2%FG4KvLNad`WFb&U7j4Efk<M-M9Nkv*~7a)WlLs30r%t26t4Ymh%-'
        b'=soW3J*uO%^QK*5$DtreUh$4(^uL$kIEf-X;@%z^D7r2xA1n-~7ipN;uNm~{3?yBw*KvjPd&z^k$#ij#cN)%Tkf<n|d|2#odr$OF'
        b'KP;AYLV%9n>i|sW*^IWfD*&d$g|@$&(bD7S6u0$&b>e_E>>mD@V$Q>IbUoMf-CE-d-Yr|UIW`83CS8lwSffj_R%brJeG`xrBy!CO'
        b'wvl7an;2Jx5aG3+zprj-%&3$#pD+?rYd!y5>u7W|pLj}ongg<{NynQ`&a@6ulermAozsM7<PAyBAOq+H-WWKQEq{x_c{t})&I%=m'
        b'amzC#N4I<|GrlPcV4WqFPh&btl2+$fpA*nb@gN(@kjCI7nugbQphR%By}C;C5ICC!#5?p{bK#pPe!c|ouH5wq_#OV50{GJO_FB7*'
        b'IJvfJU_$!R?Y<Lh0~|tK!RYtp-0qhn#b;#1A69{cYJh>=@;BAT-*jTb=b)DrPw!fMlzgr7khr49(KAH&)*jM<UB@T-SJCo&k9X}5'
        b'iT9I;yMze9Bv*-aKBq%W8^s#$EN=@Q%RLMY{FC>5-1+%^OIK^-p@FQQIkjJ~I^t@;Mw{?bA$^Bd-A(Z{t(BhP5>0EzUnr-67X!!#'
        b'Amp}tkURK&sjGWCMZx<$(DsQ}m!Z8sOWC)oJbpIiKpvBJp}hB=nz+}71^7xfLbk{Z!b=0XF<t<3msn26g#Qv#Chrg@tuB|lO4{;*'
        b'U0MFj4*7HZ_5AKb*l;fu;DUkJyqX?}{1%2^T?f%r7@MVw^kh^iDWq?+eQ!j!7DeTa<`vSiPB1T}a0~%qyW}58$&+hkW*JlzP;m@X'
        b'JbZKz8}SgUU<Rm@89<4WRkWlvO`PT#<RoM7dD8mAP|s!S^0lKEX+jOgS}*!J%6+joOUu#n=nd=V^oLa8iD*9${97iX@dDiJ=MD15'
        b'Ft^ER5~XeRwZ{Tx($Arjh_t=Fy|I3d&l781wFYk}%zRe|KCvxrvGRx4_J=b37#^qmLu^54kURZ?xX48oh>6s-MK0Q%;g)-j3=8-T'
        b'Uv7yw9`ti8|BUuSRkNvR9J)wSc(Bww_+kdHEkxfH12%@1?Z>XYkC!(gD_PPX=C(Qu%!WK@T}OxL=B{0_kE4;~a}Y#_gD_X4pzj!T'
        b'0uVtp>OmAw^eJQYDG9vK=jx-m`#<M<Q=|k7!qxBN8a_uA;L{YHNWo3vl_R1)nMDz+Cy^!@GK&fYh%*IWDQxu*G}4TH!*#OYpfj4g'
        b'-6j}#4Br01vIFlQNOGRaYfgfcFmbtpG1>5be~P5_y#O@NKzvDG&s9pGA*f75@g(<N?SH3hpAA?t5I+hU5>AMv&wMZz=PT%`_kDMd'
        b'UoVa3I+mvt7hlP?VEMm7O2n&*^JI>^l(K03liV+2`K2kMFJiHLF=9I^<+5>p8Ro`_Gfz75M7g<FT32~fVuv3<kby>MbrE!ni&%vj'
        b'F6{7t`RqUO1Y==iZtk|xjn1<d9fggp8_O|VIJ^YVR?*xi*trTBXgxOz3^f?l1smrUMCbMd3*K+d)2E1F=;%NrIU+kxD_Ksm5py)x'
        b'D#Q!0<WE*;mJ{6-E6RSYJF?1{C&Iba(YD7xn?Z}smB>3AqpU)XUV#|qBi_o`f%nTXY0Y*0sk{|QU=I@e=`j@^dcP?K0gcF)fl|X_'
        b'1hG9P<z6db6&J@;1FqVb7i@kBbv@}$$rm6<*};Lv3+yp&06y;jBJqLy+TU=q2?JCSnHT&b=HsS!n1O}<;!@b78XOy*hqTta%%d8B'
        b'trHRA>568!)|$XtBesGtSZlPg4q_9CU}^=+xsNN|aSP0vmqaahVw_-ZznTjc$^NhC8Mao?FC_+9md`2hZISS2U!S_S`g}KI7(Kqx'
        b'DS3K%-}(wa7G4qy?dl*zaby)-ot4MqQOB|4lH&?>DYxI8pfBYe*B>uEZpK@^L+glwC*h^Y%8E3nyB++wy~Gn0?tb_)G<$aU6;%NA'
        b'lo2}{2aFSJmxOMYLP}^V?$Htd`b~Y`x2RLoPl!jLw*N@pxjb<I>p#7XSX@Ex-vf!Dl|pUedp(B~L#J(o;>r8&?`FyXuD9IPt@XT6'
        b'P9#;_`|fd+Gxs2~@rH6D`u_Niazb=pJbatdm|LT{Vni2Pp*Alm^x`pvX0<t6ZHDv6LJmo2bbLqw5HR>t`z2#6{Bg@A%C8t><GaHb'
        b'DZd(D*iTB77pX#Xn9-9oA<VRfCu6|S%SvVP(`9~4V;_wMBzpna+n=Q8;rXihu9*C2C|Fasa}CjK-L-P>P+6f`ZB8Jr!26Ey4CO}$'
        b'QQt%i-m1m43avz|*OqF{0L#GXnka=fvd?R$)MkkqY?&y)$k?J>A6>txVz;Ub*xWBE_~KXjHFb!+NN5<j6aI#Vho7>19HZqhc55$D'
        b'#5=IAzE8`QqF4rZoT3vxEDz6(1^uIG;yRXQ{^*l9tEmSzSIW(<jMd~HU}@N;QZAmRMcZByUDoEuAP68x;A5L<p85zSy?DFnkASAw'
        b'!Pms^cDYe5T>m()Bv`(TC#}5G@%lhh@%xqVxSSM#y@qkykdFC1+sUjTc_?^jzM<>(@Dx>C%s$`?2$l)f3%F|$08NAL{(sne_qe96'
        b'Y!Ce8BsqlSs01-ZLOVH!hk)3Iph6HU1R5S{3sC|%^_CM00;8RlK5VVMH;Ebo(iWpaLfdHwhL=)>`oPyrpf)PSx!_D4Yqdk2fm)~S'
        b'wN^W=x5{trlYscv&Yk()`}zI;N%lEs@3q%jd+)W^+Gl_FG3RkBIPnt+4pQE1zGU^)ZV3UN-`VhHqPz+>#b95&kGsRMvd#Jxa2bkq'
        b's!wRQx4K%y=i9_5Tg_topZTq)rOkcMQ3<W~70)*<i#>o0#zrJ~ZxrDVW=?%r+(H=^ARRj-M8}r@02idgt_L5(p(V~zplu9sZg>-w'
        b'`C53Yr&A4AE729`N44!gl4AW7T7vvQi4%)}Z}FGvSG1Mi=vTPDBwh*snk)ZiNi%VD`~m)#l)-^~fadVC)N9-U;1Z-bckWBVB*9)*'
        b'H^uQzX#eznwEW+fWbKqadq`%eL75%lcqj2}t83-Hmhe5qPeN#Dym0sM)|JE@bRbZ1{%hR0z4&tln!Xjs`u=1*3#vZK2R)C6pb9i?'
        b'nt?TkuFQEh*7fX4*DImg-G5V?k!PF70sZnpzmqCBq);+=^;E)9KDh<r2rUv!x~VEb+A6Pe9Si553CA7bpr))Jmz;a8X&?RfreC1_'
        b'{<avyGpsbk0b*rq3$QiVHf)XAf6^U@{pk@2V#F4M-Vw5_SYw8QLcs?;IsujZkup4m%Kkt#hg)OLdo=Odgv+gtBJ5e4iwx@BgXFZu'
        b'IGcgwsi@A-m9fwM&GlvIvpFv9_)Df-6w6D9d0aWzYb~+rJI`lT*qCIu-~e~I5V+YTn2%2rHZRgNEo;rmk_TkH8FT7`_1c{3O&!&n'
        b'C<rbF>cp+K0i`&>HeeHz6Kgkx#ypWjPL|K;kjGK_)vkefab@hlYWP8Cl+19E0(r&i*@E+{#qxN)VO&1k)yL`wqj-bSJcBUb7=cOB'
        b'`DRJ3Rb(a7dFGdTzjO;Q492BDPrLW3n#8d3&A1!K@`iFZ6JULeCLu=h+yq8WDi7u58zE&LDi7r>_RTkzhfZ)8g0p@x!{}auRTxb='
        b'Ed6`1iAhhz=+|_t|2D63jeZ@KWp=d*T+qw&T&}fZxPr8PjjP()p?@N#&I)2C*<7v+F}S2)fRoIwbQ~V1`&Z!A8(rzN&ELM+)j}uk'
        b'DBtWWwb}fQhYy06bli-I*o(vpJl#KWXPVPj3I<wrkbSrY6R{VG8UE>X@QZ2Axp`&a_m<`9q&Y(`;%XT8eAU6T`ML}`Pm!*Y<_tV7'
        b'&R3Mi#&dH+aN-e6p5w|_NT-K4@RTa`R4iUY@}%hOQ%y#hX$p3Hhi_h)h$Sb=sR_dnxx##1o<emn5N<0nXzeDSbd@NzCKbz2sRJ=`'
        b'M}{h0qigz=XkoslG!<t0BxvT3*PmKgz45wc&KGB~Ux*<m)ou*U{&->5!j7z5O25`MkSDIpK?hpqxN^i<3tc2MP1e(^7Za-bWtqT9'
        b'x(a=~CRP!GDHUPkJTZ5=N&WV)7wfyh=lEO>%-5tZ#Ev$;EW)qW5&%sJRs${8%)WYjCC7tYn}<j8ruh=!T0sz~<he<V(&w4QWRT44'
        b'N1qrVePwm4Bie2JCfYxeM=uG8F>C0}SX>}!Lgo*sNAjrOWP5R;;9ikoxjY=q(`nA!E*4<(_u)?Qe6$hkN%X1`csg}bpB_?sHg8q8'
        b'EY%NuKyZub57HvJktq-#EC44jTa%aX(Af1^W?7!txPZuCkjH7^wxqnh6XXIy`G`=}IUofj%zmW5%q)X!;48^kYMwc;8Bct_>HYA;'
        b'j|@+s{4Jb#e=}zfjGJ_^(jT=H4if@&8BuHouJmvAN4X;)cZxSRJ(`=Yc^b>`XWb`Het#w1Ob0&?`GeOP;=K74qxlsmKkdyQ2>EHH'
        b'qFF@({V?()!&Gm6&1ilN+i%<)?4wi>+v}{F;KSAO0PXX<`mBZ3PsG@j9l<B$GpM8#*T8gW_JI`i6Dy9hg)5qtCD`mO9o2JU>`j!s'
        b')isbHZf$^{gjRIyk<F#B2UoA&5U&`TIG+4naBu&tg~6XGntnyduzo=vIX<|jJ#Jy}sS8cZ)iW{Fhci?~yezBcN0lfeLz83=c%9S='
        b'd3|d-lD5U@*HZRom*<R{X3x*-<C`|p3AR39;0eS)Ql@KQvpBOAGF5sRczt|z)rNG{JA&{4-|WBTqJI0Bl~=cKkD^o2C|#$12*chH'
        b'fGvOlr%<Yj8WyB$zEnx4D>d@!fY*guC2#wN4*8ogXxLP^2G9q!1}e~xP5e4pyCLlIn(bg%=EPLjQgWqhU;{Fo$a=bLXg~dIQlGFv'
        b'zFHQqN>_wWB;j%0J67Mc$Tv(FmKI?eiPgdu3)s(#o*FLppN+f1#Rar0J*1dBK#NOh*VE!8wF~_gxm-nJb4sa>+LsF>bP=5%8-a^b'
        b'qf+x0G)AOl$pW<gJnAnCvfho6t?dA9Ra;#H=;K!iV~URTDc>ZsG%c&!B#Z2*eltckh0@b5^wH`F_^G5_w0Me*BTY3VYu9hi&3L|Y'
        b'?WzmqdvNt`Y+iA0b6(fc1s(OvkJUeOrfHeu!@Vz6s`S+X(?ma&xFQ^~P00h1;yQZ3;`y02uGadCa}h3!qx$d31MiA2+XjAwAEXo7'
        b'_0BliTN|n)Wl^b8v-=US|C@4%htX!z$9dZ$I`qJN7*%a?T~Cm#wT7RJ*ly{N{TEX8z?ZIp--yrI2EK$J4_VjSGFcs>D@%2W%q9o`'
        b'+U*PG<vHq?ch^62tZA8kAfP<VYN=nYeS=5U-CjwS`e({Fg&UieRj!o*JKK<+?4T!yI4TN$T9KY)5iVo>a+!4l^c!kXZrFaVEY#>c'
        b'z%8Kl%=}zkI3_82pm>3!X<2FO;nl?tkb(NDl%|@=#b0#({X}`+kZXI9YpFxFT<`^r6WJI9<VFVTW;la(u93nHi<b)|=ltE@4HvHf'
        b'FPhDZJM5U<{sKAq3z|dvp7p7&exbTlCV3dEF7>O4_S3uN;lU`X?R(253CFg-<7(#C(RHoX*cNUZ*Ty*_9^5r-j<s?QqfRLa95)mp'
        b'7!vrrPC_??@Z9=*Won)ExQ#E`xm_P%sb8ke6B@D?Y=<HD7Md^YBlAUz=LeM7B*kF}JDPsgnxkLakp(%+DZAMPL$b1x9h_*=%>gYf'
        b'%d&1TO~SJD0nifKW}aczf~?=g=$##QC$)XAYha6bZ|lHb&yS=2ncbTrI+~X4Wr_X{5#0_%JH`5SdidRL){l@~p4GgesfA~I9=u?C'
        b'g{$KEA_*_=?;wt5iXdz=H;dM1U(%`$@?b_QS-ogs(ywE(G*m&3tFKU;rFFrK=9x!d&B<TlJ-aG{$$zfI@XGp;C^qcj;SL%<)8%)p'
        b'OMbyFkbfX+!@m@N!ugRZgc-}TzfYMxQp&JX%kH79T4XNm4J?cr?g$wz%ae7>+PI#w&M=-g7VYF#%>u7=m_>*gwrWSul4(H6CJSzw'
        b'j>TK{{~<k=<i>3bGWlW&`#MG7DW#*8d^^f?fTtA=&y6)(I^&D}G5~k$(A{_okp2}~06<rr8aBO=O<UOXdNzHAO~1jWFG$w0>)w^<'
        b's)P1pAC-G9W_h2j_FN{g&-Ca*LHk$zp(BL$W_Xn)b&P%fGRugr>brOcdu(V2JrhaGe%)lIfumzW%b2jE{No#8)?bIVzJM2ObO?;u'
        b'gp#97CI#gI9MKwxp%mFZXY6`~-9GTSUf!<{o`BZ>E2xU>GmP{Y6Lf(I9$bYD33)7)s)Z38lB-aS?)Ttmm=I4@hR3xm65;p;a2eJ`'
        b'3Rhirk5m}Ri9{7n<cL<&+lFbjLYl2m)~_f3^C%Ch<X=~%^F>r8qQkFRa9x$`Sy>x=(2f$c5azg2(}Nj9CbgQ4OD3t&k_7k+>jR&t'
        b'Hv56UFtR3rd%puRkti<~L1}UtNrI1LyMi*0djjrw@_ROZp?41(u6WB{t81|4iUlnjjWb|g@@##ENl!SIOsZ!6lWS#IP~?@7jV-9p'
        b'5$p@&s08~WnRX-3Vb3xQK91t7!UXMQ?5MCmL|Y%CeezX97zzk8gc(5@Q5gvtnHh^RN;6tB_Ga{CoXj|vaamRBrz#bzO8r%(6IGeP'
        b'8Fk%Z3FL$976K~3`+g}>96o76v?^C2T+VGbWRc|r5BYJD!S}DCz4&%aorq!62n&u$O?z7$LTtI<*;YS@6{3$XwFxcgb01TU$hnE$'
        b'wbaIg>#4?N7pAP0CE`;i<LXF^7GOI2p9^TeCrwNJabgN)5paU}#>063q9=NT`agX<>p*wbv@?4sQWVJves`K^)%WBB-ADS!-yHgF'
        b'K=+Z~9h$@MK5_(nv+g7B9-1?w`$$Xf)<<fl;#O*k@<AEIVWR5YtE+x_mUDnO^ze9DnDKy5RJ11+KR^IGFsc1*xJWe4DvqWjeW#7<'
        b'-9bRWQxznW6}<gIl}Hp1PA(VIUizMNnobUDU;Lh2YdYaQFT%4G3AFX~wRKCwyE*JC7TQ}H_SKmCwrlsD=Y~i3I2kFwNGd-jf^Vhr'
        b'1X(jS*f{FXF)7;8M^4h`qcaVwKGYoklnlyhS#8gHK^t~e(wR*1r43*6SN(XJpD#vpLL0ZMImal(qzRS#FNm;Cao<Pcy}j+5b9(k&'
        b'-q#_*_K4dZBWcmT?b~12wGJmf#JYZyGq6v*cYmkIF2cw<^?t0wUb;IlrhL}8c^~Z#4DGNN@3uy{_o6*JyREpX6A~*Sq22|F=XM7Q'
        b'(7GLICVa4Hft!!^@d!Ca`?B)4gwb62Y1z~SVk?FP3-qUD?iS2=_;-5!3yCXX!Y@w<uh-|Gowb!_fn9*5EyvxTV!6w4;xtB_0XlF)'
        b'eHv5$84LIIMebX9zCdlmL~C~y<LZa8`m!-)`;20#B_cF<?OaDoXr-ws%qJqi&2Gh?62^^IMTSQ3@<JEUboWmYI5{a&FwJ+>k7^T^'
        b'7s?iVHD{GkmgBe1*%BITgwixWA^<J2=hED0<F&FsG~=EAWY{#{7QvoCDF4#U)$$?&pcCGr&O&dUCBV|Xm*RU$xqo?c86qNp4Hj-u'
        b'YKFJ2$A6Z5kB!RrC}s{_Rr#vfZuVQ(xhFKZa(5KZj0%=V@uJPfr*Si{ITXy~;UAg>oq<qOr3sak(%>MPeToDD-F7`GYV-Ld`%A{~'
        b'*?j2uXPFb(W{&7L)#e3i5t}E_o5z;S=KAAEE^D&rn}Ii=%}HU4z|0viFR0)UK`>V%fjU4Dm2<m~fFce>d1aXr<<$eQ<k16YL8Kms'
        b'ojKeGof_HIf!~VH{q6iW;>vH>k@dFKc(|{8?^!jNGPr~b=$YjS5X77Qd$?Ilc9sX>>ZoBerQu>zB8aLPq%R>IMn`aGSy$UQrf>|o'
        b'^SOEah)_{ZpH=*QVPXC6Jzvhw<J<YztMqx=Z=EJTG&dR=7$V;((VQ<?W!Ke=s=LK^&t&xj_mP*xu({Xg`(#W$B(^US_H{hCDti8^'
        b'H>2MGhe>LV;FQz2`VYf-F;=RA57wqHQmhn2g+F+noD}Yho2Cq#9v&vcAn6VrHYtZOvJj=IVUv28<U^A9#jrYin4AGgb?~t1m&4>^'
        b'sNCdXb<yxlilCXz4r;T4X;d)|4fD2+d8dr|O<0ppv(Ul3Z`g)f)krlum~C_*q3H5kp?f$Y{VNL;nI|$VS;!uv*4X0PlF@t4NNpy&'
        b'SN#|%urTkb>qMA>YMh5hF3@!ODeC`fh?>7Xaz2SC%vg0%!Msj0Z_>;gG*hEuQfa1^W}1vltA*L3VC*!ri)MDyOdHL#)67nqd5>n^'
        b'Rdb-877OE0P!6P)SelDfsp#%cwe+xxawLVgB>sF2W!H82W$;zhn~{^EQdP{GD(Vf*aa;<?H-^>-jg)<z*~r+{K3KOS)Y9eG0fJGR'
        b'dyW*oBd7`@7Kt?V7Z+t~7`u*oPgbPYLCsvO*WaBk0vSkO`eU5rt@=Tw(ny!k)VoHe!NP2v?`vV|+2M?pF)budN3}>zIszh$79G?4'
        b'WNZJNg`_n)BYF!vW$Bo$-Bh!#cVOvWoOo0)P$Vv0UQE~t4A>Za)5j6TaWFd#*+}UQrX6lN-+-IAj%s%>Z4$|4$+;hOLQG=%QMVa0'
        b'?Z9*&<7I?KTl+(_k6VS267~BS)K6N=2uydVZ)qn^OcjCJNTIak9RUjDo68RMoo^MlHbD+)k?~Mp`JOML)5{+~uhgS`nwoHTps0+h'
        b'6}7Ht74)H#h|wBSnInDWi^m*Kb~_4Q;avEb^EE%{bkBzexM9`9%|ad1;$XHqsCU)D$Uf@CrG=(Itn6dFV@go)PjlZ2HZP5yE_HV^'
        b'wU(tpwGsTXDU(54yCZnf>Bgl&WnorhSY2O{xN=3=p`Xk?rG-XjYXyN`jbWbry3zb<-O?akn6)gdZe@|q{Zlak%Ct~h9n8DOE6!F|'
        b'7eHf>YW1&?QlfX4sWqmzhf!m^1dRbLv0LIpLWu^G3Uwr-FNd`04)-mEc>4>XgKC*tN(vz&YTW|11SzQ5h!oUuxNkQoD5EwIcb9t<'
        b'Wa<-o739Mz$VA*;KmR^#7QRMwQ17B+K)kwn05g7!cSi&TUzxi#xMJzFN2JG(F}053pr%N^F#^eYD3TYQVJQwWLiEh)rVi}%Pi8@B'
        b'At(m=1<Fe3A||6r66ICvijiJGkCjL-W@6R%1;q<M)DGrd=#uV5!x(mkY8ZG%e6Hwxk+`P_9_f5A=?c(_j%tQ1-R{0aouBHct?Jxi'
        b'on5bf2rGk5L!6<S2i)S)Wl*U5_kE?yx~Y~kP_DO|X?cx2!!*OqL!F=0K7^YxhNE!^noSi#Q8*c(esq{L5#x}ab@t*iUu<cuP-?Tl'
        b'fN)?i^yU!|TS3d9PHJBU&y3JYFf3cZ_yrS2s=ff+XQtjAJseF~;L0Y05vGnD)=;(kH|IJg^wDBRmmdo$BTzp<AK7-~9dpe4n%tXw'
        b';S}fODQJi`JcHBodvqS(FfD}I-c|ns?9sc@CAkekAfN&Qq3+3;vCEG>ftS%i!9UDR3tpWYF;lwM$keKIL1`fbO|v>)5yFd3QRsqb'
        b'>TLz}o4y=zg2!5e{aBPA$(PAqfL38k@Sy}W;PnOA+`udFtT@S`Q}pyn9EC6%5+^6>n0FOS1I;*><FoO_IFafD5(o3MSeZ3cy^gBQ'
        b'9mGuvZ2yj>j`6@a*te+gcs$SF4QAPq2Ru|JgXkdf0d5B8!Y7=seNTSUa|8li?Qpy>FGxkbOLSqZ=qXDZL_h&dSyY%?ig{&M&_S!#'
        b'z8aeq>lggPy61z}E(H~sKm}#GpcP?Wf#Sk=(W|d%porDL4~Pq>zqCY2<V)O5*zHS<W>^0P+6%-=D-4(X^`WH>(TGH*W!R`VtQe>{'
        b'eTn5L^U^_F{Rp=I>7|ZwBiR)ej3~W}{OVyv9cC)HS$6P6u50();MF5SYji=mw`+Hg)IY`JUYYf=A?^~4EphvH2SyPKNQ~M+9Gt8D'
        b'YsQL!W2U<_<Dha_A;eUp{TBogjyB@t{|Pzda@2qCCI`>~d8c9fU-0nHj=*>v*vDY-!4TYw+U*qEZX_$l$<KOz5ByJqZiqVJeY5Wa'
        b'%&^-E?!rG};co25<MO9sRLr|IVVL{ZzH)g1=}+?Hsts9L1t3ULjw|}O>Ljj9)exs43er(9^lIaZ{%!wXa~%P|F0dIDkq-S=#k6Xe'
        b'E$(@k#*qgtxX9aPAo+35*Tl)=J#IFdd}tUQ0P7aP90oGKlG`F0(U>~{$b-<wahMV$sXPyTRvl*C>hJM^+|x0OBM<V|dFfv`$@yA%'
        b'@?=jBqMpHV1`bCE<AZ3XRl#gAMY4*0KDQxY#I9YVWTG(868#A~%GbOao5YUtCBbWQBT`vIr_%*34ILS?q1TOakDdF$>Tkw@640Zm'
        b'Rt2@iYxR_qOhV+(+_pSh_?phjn0J#u$<$F>G*m0~Us*B#ot>oiJBpv?w($?}3>aGG_^NXB`bsujHwFcEy_4DhcBX@B?Vz?8endBq'
        b'XX0p&OE=YejM~yh9vEl%Hk&<-K%gG)?M~5u0OPv;(`*IRJg*Eq#yAHbA{6A^QuXw<|A1(UB*=ITQ?Fy3;KRAU1bWmXb1l@CT3iTP'
        b'2m8#Dh&h_ALL?N7BhA4#^kf?uhs8s}=10boxB@wV_1BE|Cwv&F&GfcE%U<xC=Rc)38+pDT<B8zD)zc|i8vD!i!FQirBYSK$ZO3Ir'
        b'G9%TXO3Bs%3Hy?A#}nY~bsXjx-pFR1KZo`t4?OF6To?uD1#><@bO<n-Y6!<4RZ$J(#A(8$kkv5xRCUmY_AD047Oc*az3^2xa&nw*'
        b')HcTY>PmwH$>?C;1X?JEg>e!*jMTwhnrQ%^8WJFd0{E-PWFaz|*-lei6jbYRoI{<<R8d=^KbD2cHB1M1uZVKTynwU^a3Tx*=Y>68'
        b'ZQKKR;mbZ<v6=nmY{Q@C0^?os%zk<1G$A@PoRy?EfecVFn~YSm#?B<K%+3wOlV8c!Pz}J2Xl++mX8+1;wC~8sbXu4_1~(!yTV#)t'
        b'8UDkgh$h3oXR{x9JS}R&(PrZPD9ahD$wKWp_cS<n(tKS8geaXFX2&$)Y|(N-xFEP|LT3N?Oc8h$aC?v8nQS(S>4YNM)*rfjGW-9H'
        b't<+G09t=T8<7W2fdu|n=TUsHHrkZ?o2^ywa!JClCM=RYbP=B?ErkQFT^mfTN3O7e%SAzY_t-%#Mp+bcbNY5%2CZ$2Q)A);u5_vSU'
        b'LpIZOeDzfYwF3nzu`UJEL`=ix6{1#rH1`3)yd3i3+**z_Rp&@5$krPjSsDhnI2P)&_4#7x6m{A8oGZMe+|zj2=X~fG^IpuYl|Wzi'
        b'8T12wjFdx9yC8ld0zGX!uP8HrX>GU;d@Oh0DN|Q(M*l|{sHF_kvOQ;iN|MwrXc85*DKn?*U`GEz&tsZxuFD`X3}&fH1(K`KntdV{'
        b's>xM+<^Id?yyt0ZQ(P^rpc<xx_^tXw94%5&O=%8X{UqkjfmyCu^Wjwu)9mJ8^OnTb;_75Drp+RSX4{{$w0;FiFDRHz^CU|*@%}qC'
        b'Dd`0muDTPrN*x!y<M?V!VduzVT`K!DurRt$;C4J|iE}WtBQ7e^@Lg7!eTf^bQ_kk;Q#!z!C#k5cRM)^lac0i>9C6kHmq@4iP_9v9'
        b'aZ^4)gSh*u>Y!ZVP-+};&>#s3ix#0EO$CzCsuYMH=W}xv=h?YK<%sL(^2?k$?}4fGib=kSIIUJ@PNloKiVx&c73hF=q(xB*s!0|K'
        b'dfp9&jcFJPfgrQq=V>8yWF57wG)KcUfagkY8J0yrw2R3VG6l1p<Syn;;}Y?xUFxB^tL40;SXrb0B*_9oLv7R9ixw#oAU16PPaMq$'
        b'A3%7&%|bOu;}dKOdyxf3Cey4Az*P37Pzf?$OoNJPF4g%AK4=;bM4J@UHh3tv=`HM&A^$L0iA(3^fQzq2eNkgCf-<N@KzOK+41}ss'
        b';0jaRW-Ke;kL1QpN?yzz@|S`AoU%FGNVO%=E|q{&wMJ@|<`|ha0#p|3Mz-EQY@ymz;LdOS7y{CS$H0CSq#7&Nu=KX;s1C4(y%KdT'
        b'5A;7Wp^}7p1J5&|<__WN81UnA9puQI8i9lBahtg=gTsFAq2+3XP&ev7fcq{Q<G$bQzt6aD|J~CE?(Dut;0o$JB`%*6qx5(0!dMp}'
        b'Z3s8Xu&vW`9l{ZD)N4kC0hiz;>kJ9qYcT9)-WzV_y%{&vVAt5co&V$IAGnXe7v&RX#LLnloREWWmdpBPUezMO?x@?ajsI(OtI%NX'
        b'0whT-X!Vi%?Ig}}k09=cZi?|tlmE4Hs4(}#qwKRBu<Vcci>#-Jx&^_;sK`eK_Fo-s2P3dwoZF1r0jiFQMD5^lNp8(Q-^2fk5Wd15'
        b'dK3R0Y#;gMef4pONZq0Ttz)CmA{jU*Mo$!a7AK}-`~SF<jlWsmP(X(QaEBugDry~Rnol`ji%x#p^HBzSLh|79t7F2@o8!>n+sB~^'
        b'*W%F8v2YKODA9zL;_e=c67P(}qG6KF5Q_>&qB8fdZV`&Amw7``)H`1o8^ify>XJLhaL&b76+xK$DeRvXi^}B}-Nko};rubvQ=_pc'
        b'aibhKrjEO_9AVj4Ar^%o5W6Xs137LIBkulVIq;?2Gw&f5HBDpJ1ITNED2%Z?#-W9eUA-X=6^)5QZ)SeReYe5A#i1l$=W!E?{9tU6'
        b'xOz5@*0sjkyZAfUJJcf3q2fKlc<o(E?zM&hd*_KSJ+dslW-m~vb{BgWj{^gX@{}HX!4|laEWn`dB%X+ttjg5jpuJ4eW$J9k@VLw-'
        b'Gr|?$f?}*)M({qkIO=z``#0uZvmX&S4UtLIUF=8XRrDgl;g;PrN8LDfZd|{+vu*U+c3>fr?-tzMI6_7+jUHRfF5j`C*dq?gA?ucP'
        b'*fB#S`vRYF>L_P#kZB=UQwPbDCxE*To|$tw&;0~?NdWmtz9B!2%?pm1b2)!DpUA{-WpLH8*#3i_Wxr8_3#{H*Uy>1fYg+%WvA3ob'
        b'_hxTR%RSb1isax}YYT?;W^3zS=CM;h)7}#Q0(+}g-h;gbr);dfU3j1N_VN{vy}i-enkL`TVBM0XpS|u!@=1U9M9%%%+i$M0Cd%|*'
        b'!~Z0EOMEhX5BApdpTk)8;`th87ewUDqWQ=kjf^k%&lz6>SN_-gGvTa1BO2q++-hxo+3nWWq1)bVfc0I00fwB3|J(k|!7DfTGxsdV'
        b'ZRVDLp+D1k<$sAklNBP9&^S%i`{;r}^G2!}ybo{*5(%9u%c#mmYn|-ttm_;f+OzmW`jn|PD&}1aOs2l!WoTs9BQO)2DJw-rN=QMH'
        b'X@frLh29s8RD)i<LGrXD-2a!B`syH?>d4bYw17xQ@7`6ELlg>gw7ifbmxUTBhdef!?v~4E%CZ(D)9F~&5}CH<3f<jDPLwU#P#}9j'
        b'a%K`R>GLJ7&cRd%uO{MjDy9NIBO5!lmbAnv0@$gZqxe9ss{e~Z^_R>j_hT4_-tX6|m?nBNrmDY~nJf$UV_{}c{cPc4QCH@?{`0A#'
        b')Hdz`J`gi#=CSLJO^zP9)a*#bj7*b6!M9LtWMG*urhO4p*?r@tb6)4GwsA7kNWx<0B-N}g_m!hnwc02U!$P%pP&=y;#HRX)%m_43'
        b's#%(CI;Ke_;4BT`p?9ZkT~p`vA7kq^$THCa=FacQjd440_laTRLCkXGX$#|^DTj*Mg%&U!a@q8#P#VXOqNXGLB!zM03R%{|WN1#U'
        b'>I&fpW1?RFl>@YpkojyiPj&EVc8STcwS;CG==y5aNlqd^h}NY3h3;Mg6ir+xQ0*71SA6ia3N2hY==zJGmMDtkC($k)g`6EII-74A'
        b'kJe9`dnN7*INMJ-I+dQ}LVqQF(Q8qE8m+54m$M+eX};_-HV6*(dp5C{m<H-=0IpOg@#>ldDxSu|Y_FP*UN3J4!%l`KrTeLv4#^tK'
        b'LT$Gk!9BNC_BHJN9omJy7HaDmYWqNjE7*4^Ad#T3W0bw)BfswDm}NO<Pv<Mmjped#$8^uukf2@*v#0P?!b0t-3UVLC9rb@b19QWB'
        b's)Oepj2+l8p2WK;`^(Miwsv+(S9E<eH!bo#3uS+$Ib-tP)FZwbosbO(Le6eSXitxaYT-*nRgiiwuB!hlC?FGUNr6G9`UEfIX(TIn'
        b'P~PFtl~HfD8Y+Crz{(Y`?09)|#bo&3JX9`N2cp`+JYXK0t{%OIXxMXvBnoqH#*OtC^#(nnNp(mjgSzY;jsg|+=3YcCqSCu921-j)'
        b'D<-R$H_A@pLu-6lvh0|@fv)pcEZsN8(%ljMCHgKisMttttxmspRXU42sw7^$t14f)CsjHbP^D?<b*iKqf(6w@t|3XHT88!qfI55p'
        b'_K+39ExR+C8rO_v$;fm%7ZXOR6WT+ITk8LM41%tAbnf$@4B)QpGrWVcr#G#8t9iFHwSD2-r4b;pJ)@~4u(fE9pky~>Yh3dn@Z;S{'
        b'^m}I>;wJ_115KKVl!`hlL`Wy`;@#zcRRMPqO&ZD$Bd@eXN>}i0lS+0+HVqkl*5zmzJ8_<Kqy87L`hOT#)L)dx=+&=qz{INTh2^2R'
        b'dj+TKk173sO!2-Ui$QNjw5=1UsdGVbk-nsVR8i#Qh^CU=QW{lp`$i6%k18=u@>YU&VNsiq5uyd`n+BZd;aI3`H1(#Ave(gQ_ZIbr'
        b'k$N8lAZ!wvc?0oZqyzp1=(CH6^hbL1LW^p2rm_5A<&2UBy1{%==#am{w1We_%^^Qc38(C7k>Y7#<LbaMtuvTHXcJcH>i-JdmX^}p'
        b'=b-{nKUARl6kk^iG8)cj#&53heR+p8c1qYz_Y{tb+SC|;yE8EM^_4x6$Lb*9nhpf(U;x-nJ{Z~prWx4+=K4?{Hk;6vzNo9eSitCY'
        b'to#<L39P*=QdW?~gU*#j%M>SY7)X+ChNiXwBQlLFGBA^ld_SVWf^=aML^cc=iFN3le3rg$l)hUZ76<fyjRp~=S5TXd{{_5*0$G_X'
        b'n6DP1@4DnaP_Zkcv2o3H3Wz1NQOjtyFGWQvJ~;oHH|Sp9k(u6T^D*y|rmmyo!hWZGpfXlDQhao93_b$-D~95rv8bsEWd56!c!ocE'
        b'FNs>R$&?12sY$O&X$+WM`gF<e;wB5*Go?ipz8RBCnubh5PnSXR+^}aZEDGe&fjr1M+exAzbwQHK6)YGEm}U9}cEh+UX=*e*bp5ys'
        b'3rFKloA7TVqYezg*il#P8FfYND>Bm}IzZbcO&Ni$se1$&?5HzI$Beo{iqN*^j~R0?@j%l>g~F|-BHXk9BNky*DWX{P4hZH>Q4V@F'
        b'*apJtsGUZty~I~Xy$Kc;dN8Qv4WJ^0<Qrw5;6o-6^mw*wqnD_oBKY;{2PYHSMH=WBNoJ2#bRb=p=wW)76}e!3FIbw=D47j*9O_y5'
        b'QW^7R8TCe_uXIJp<T4mA<vy%xf$A8&_=#oC0783i-Zf*^M*2Kkv;fEj`xYz(qZUs*gdsx<y7d^^7S_;8uQ#+|e#p>j7o~$fGk*&P'
        b't>bzdyT2LPSXt)M$oE+rTQa$|=!kDgX9u#eW4oYJL})LkKu69jVn<(_PJortS-+0SDst5{o|FGNMh*$dISbpnGL>?A3G{9a)dYSc'
        b'G=Wdi<Ir>pYMYMQrVLadUA$i!t6<(#P;b}-Qb@f4y>V!@klmO`2)zBwI680+>kGMr_T(%}{l)6_dQZ~=^{nZ7S&9p4lFx7@#ile)'
        b'Ox93u8rl7yk%C1b9s{Kel+vti5_qWl+}MW)ukf`|Gg(g#i~@<vViy2y82Yj>mz;J5^N0LnOzYUaornDLC%>{oxw&!m<gwcMk*^I>'
        b'cq~*wss5HG>QKft6SX^X@=7`q$UwHC)wt;e#8A&i9!oiRk+0312E$bW!xc1RcP|6S(jE`fMbo-aX^}LR3>XR%fIs7N7B|hqJY!W='
        b'!ZDU$&~ZVPAX?+<N!JF(5$Asae-V!Qi>;J`dLOj`4sD>KwvDtwhW|(#tfN`udrkE{hX?=0*CvF5=IbbE+pYvvzf$FyY7_^D4YmyS'
        b'8zMX?TlO&y>eo#XvL0)b=EGs&HoYzfA#L+v@UNqXOb8kR<UvuR=4lY*eF)sdD2jlII+z%m_=x*KWD9jVj<HarDiq#e4$lBT(lXYb'
        b't$Y>C;WQtJkTj?8_0MFaJ8igmCz!*sxbXc-e=vtTGn~_W8rMvLO2NML9Cd#_jCm&Bj7b&zlHJOt#??Ykf9N@4Iyvlcq_xH%{p{9J'
        b'yOsW+Cy;DJPpp=PR{N}j4&@oMV-;2S318bPMv7W*K~qQllrzB!YO9LcuA$yb3Rw`912d<Fc~5ddV2Z%l_lH}J)b?PWKHN3r|ET)n'
        b'Ffv7MzgLje-KlgAt@cdSZqGb&&E`0dL3@f6^?wD{<T-k97*Ll39URBwoy9w)vCl<iObKm=9;kFi2A0yV2qJevKO;^JkL~!bBl@u4'
        b'^Cf#PsV8G37X(vK&aYBNh5_Ncc-`FC^I_pfeDtNP@rd&d$_e*8)1={KI{M%<xTDsK7zQG4Mdt8Y_d7gzh;QOy?7jqNl?`qk@HHGo'
        b'WfWASih7TpNUZu!7S5BUY)~=pnZ_Z#yo+9eHR`C^rOmkMZx`KPU9?c|!liW2(iU9(@FmkDmsC^(M2e(;I1g7p|C4&dPc-$O_j~c%'
        b'(^-s;`~#WcV*1E=pA2SbO=l0QM+c=CzCr2Z3D~M1DmZ3N6<*;za3Au?R5C?Vd)Qk%+K#1#;HHI`vH5ZRLVe#_@gj4d8GZ)x#PaE`'
        b'MP|8zT0fYYU{*A5NSI!|phG?<CM$=^igm%QmfyjxSV#57j-;nzsxMJl!!CJTa)Nnaj`;F-)wNWX%>~JX;Q^(%Zo>$8nVdK<EUw<@'
        b'T8vjOSbhGYE1#q5Njkq^Lq^cLb0y-W?E(3eW;`~pE&b6yZJL}}+$-vR<S5?zO5)C=+_W&xQM^YjN`=8QPrY;#KQmn|#jq1p9_QtU'
        b'wl7|N{$uf?)2`FvPhyS=NWL1wN_$VlNYQZvCyV-5rR&^3oh&LQR)l?#y(WF`sjSyJRxZxcP<{Uq^K6c*??rJ|t}AP?D=XD?JOFz&'
        b'_2q{}EBbQ9@F?>!69T;dxODT6ne)0{NY8u5b<mjpc(FKh-lEiue>?O0;4dWT`&H>H<Ij=)aiQptsYs#cLlfw1oVGMWRr;8-a$3?1'
        b'6=SXqv(d#MXY}lxpN0+b=#~@1!mbQ^&xr2A3iZ79Rq6Ij_8^#l=gk&ozm|ULGWBwL^2+oUoO%rXyp-O|&j82A@Q4Z>V#9Zz#5(z3'
        b'iJJL_sVdJ06kbe52afD*!wnCkI$HR>m(jUhhPTjtZRQpA?=kf8<xkP2hKnUSrfk9$A8^Vb>885^vYGUywF>Ey_JZ`&_)&fv;f&@F'
        b'1>tTN_HwrI(3M?gocJxavZ#!}5{H&PfV=l%Q)5vKhqW(EmmQO3eaL<fFOn_uK31Hqb6?p77PB3a(SIt9)p4;EHH0*F)sF;@Meimj'
        b'uc+bF#g=tF)UHm~*)f{oyu!JHpXrjF#=E=dHm-#sb=iKp><M9^d}|jvf#o-tL+sZf7P~6NcC*VNo-klWpy4gz?R#D5x7Fop6*JN4'
        b't>$X8F`vlGu2{1u)&bHT$$mJ!w(b$>hW5zxHeV#1t!wZhpxPJ|)12MWbLIPWk*zj|FP8XaZ4ehtu~TE+LahBEk0Q8X!TiP`A8WSd'
        b'$dz3c0TD#}nn(#HPFLd8pVLUL5+`29@+EoM(I*zgf?mrvAt`@QgOq!Wc24akPGzjdj<u8NnryKq+fS1{0fdD+*UMYcm7ndL#5aSe'
        b'zIkgHJiRo>?ThKeeq|uBR$P$d(t*S|=y;8#;%8rSp<fo<Uz(%OG3H;)%O;6MvC)UtEi|EhE*vB1+lty35*GXXTI(+@U4iZ2q(zEt'
        b'Y`sCK-e6R3*m$TlJONj$u@3Qga<AyE>gtQNdvUc26h2N=2UolDardK`MNIB`1ve#P#>cQdlUl-TGtAkQtJM;8BuDGKj3z5j8mqU;'
        b'$gME9wQ+4-hCiZrMCN2iHfimOvqsJP!zn_MDj;K()5#EJYRN*@Cs(9~lJ6@wlM|IYK$!<UI2616qUABHWd<3d$QFZr&-PPfPk_hS'
        b'76BIhU7YPf1$3N!X>Ec?v2u(WjSN}H0ck8^KL@ByDXxxnSwL;EkkGs8#P${!`n9<b{y$c)DCEUwYd#E4h!2Nh-Z9)9Ft}wnehpQZ'
        b'ro<yIdQN6vvYIMPEAgDcHRu{fxY>ilVO^fV`#*@C%ul-+JDHPq4Li9Y?H1U{*V6u9!%jYx_Vclm*=hejcJluYcJj?R_kx{VJLms4'
        b'cCt<V|84A~LxtYud$E&+6M2p(41p(~n!_&DZ+0--BxWq4xL468a1LLleAEyvPqF#Z)aD3w3l&E3)C#z@0RpJa<_NUf&BG|nlT85G'
        b'Xqrnijt)mEgofMS*E{T-urm`NlA$9e`<xk12NJbs1da%a;o@T~Ak#rlCgOB_I+CY7#_gaSXwCU5E(zj7CG4r5<H7Z=^_=Z_78L=?'
        b'sxChVwQ2hf{i;iarzSwKqTVk;yT~a=utO0@$U^*zEGe|rr{)-!tyNU}7q-e1Y?TOul?vte?s1-&aEyBU4E4?h>Nnj~gQxbeuW<+S'
        b'p1TQATy?R7MTDxD)NJRY$(tV~@q}4pAfdH1W2KoU4{m_PgYF!I2i-M_2h~t58nk!4;YK_tdQlYOlF$eT3UO7`bt~S!k!a0ZbHkeV'
        b'^=p=nL8C8Pv-~#%2+hjYdk~>fMI(Sv)7%>Xp;|8>)HwnOWzTuNH6HZK$8LuQO}YUO`VE)GgYGgMee@b0^lR?j@Sxgjcu@C^cu=+S'
        b'e(|6WipnVKjd;*`2=7>MBi?b)ct3bh>%SNes=Xy1)Oiyg)O6|o@Sq<Hy$TwG2fdAco*jb+Wi>+t-hc*GAT+3zg?RcHBRqQq?t%yP'
        b'07Ch?QS9jL@Sx7?@Sx7Icu?m*2@m?lz2QL#;Vto??i=x-7&ZnG>W&!JP}coxa<AdhXckY$;z6H0=E%Ag9@LrlGw`6+e+3>?JBkN&'
        b'(oCZlQl!2K4{Akt(AeAHL7(()cF4NLW`~SXJZSgN*tcT6?|m!k=6l<>au-bKlVkU-WZeTM^bR^0jK2XBdiVXS*8AGO`ag&Xy@MEq'
        b'(LVzdYW){uLZ2MFcO~oky(_Ze``^1_{h!~vGKvW`y><sosFwI_1QTk#115Anrg1#!#e`<vj0p`B-yRb>YXlQYNN<k`oq<^#PkOfm'
        b'XWfhm4HJ#Ughq{ELM6Argwkj(y$vc<&6+zF)p>2K|FdzS3lhD!&=OV5iz#Dqp(|6a$Azv)@!~=sNbHv+df$3KpK?oF=&w?4feY2H'
        b'U!CH`g*G5us38S;?l<8=8^M+H;6hsxZ^VUafk!Vcv;pBl%Thdes<F6GCyNVhybUfi>pEQM!du`%ovM_a5nSjzFD_J&;@LB-t>Yn-'
        b'-xyrzPKXek;rJ{S<-8p%)Pj7SMwn;4pimI70X!AxiwzdI@4<vN(u|YEgf@Z%x5k7PCf*Sfn&-iUhW&}#_1>(0Zi+!O8(~7X%<A7V'
        b'%YzB^O&P_6)_5_YAt?wGN~dTjC$J-0+hw2Ce@Qh46Pi4G6cc(`<;8^lsJadl8aMkMFrk&R`YUFQVnV-EU55!Z&g%b!t<>;Wl@}BG'
        b'@3Z><=(+W&>Ys=SZSY`1O&(0B^G=x1yqhthgL5FVYPb;-+Tg*2nmm}$h8r=VX|wv(vsln)vuZ3Rv_?hMWaf0unbkkX^Y|UrT`{2;'
        b'hESn3akU``4=Pqr&M6^YRH*xxn0gE<6z!B_VWFm^n_!_ew}yo-!N`fSSXcBPuLFe^ctD}gsQz(KC<JQ%LzqzK7)+?siwSk!4il;#'
        b'!Gt<*hY59Fj|p{-VnUraVM3j^#e_Pq$AmhsVM3iZVM3kPVM0|16H1}2df1fBVK<{f-5k)D={iv8aW5#;=>>&4$ACf!>ljd|mL!Oc'
        b'9#E(?cL*nL4GO*GWaq*A6~296c)!^D_Tf!l2mUsG-&nldd@hR$RqwtXCUotnEM81#*4IM!+FM~lH{TKyT8mv{{~j@+6<$oJ={A_q'
        b'JE+!a`Wcu|>%HS`?h_Nrc(As$x5u~ML6*T+ezq+CI$Y?JV{xHb*Wp43m;Vf0=)Lg&b8(^cO}J3&9dV&gdT|t4H{&S63Vt>&H2&ws'
        b'qlEW_qT7_YR~*Gn@#qMSf^FYh;3)1Ck3MnrzHt=Re-e(u6OAIY)kaTSjzpvGI1IZ>JeqR#{&5ud8;|}YIEp*OqRzOhKQ|V=M-0e6'
        b'fD5(W3Kx2tAP||n!KnMkg<Ai~xX^`OTxbpxnRFd4bf*Uwilp3e11hvZJ@wAkqcE67g*K?ETg;=k$A#X9Z3iaq6&KoY9WGSM#$t~+'
        b's0J@Cv|$b#vNY<bMlUY3!HWw8@2v3}F0_H<8~zaQ!H{a;!L4zj$l$sax52I5$=>?j85erD^Wd!ac^(|`@;zZfpSjK2pZh-7{`~K{'
        b'_80aei&-o9XWCkI!o6TZW3FM=<Tqp1;_obm^D7p!_V7Q|*8Zco&^y`Nfg5q5_qud>uWPXPfeYo&(J(s^E)<`G?9u4>iv1bm>kt1J'
        b'F4X$}7B2L*{><%gp?C6Uy084N@n`Oa3%!#+v+K(LU4N$a{&1nOKWA<IPUG>OaG?v0s+_yxLbWU|)OioMQ0JX+p$!NZ+Ax9(ZTNY('
        b'(1xFl3vFO=p$BL8m(Co)g*F&^Xa9q^&;}M4y6YM)w85}2{+75<=j{G@Gg(|{-K<;VLK|qRK}GFEi<k}9aG?$NfeQskrUBtXoj2n`'
        b'8?MKNqSFRhTxi26E)+RCP;@LV^t)T&LbV7N>a>7kbUiM#VGJ(RIR+Q1{ioqV9izC=0v``9wC}E9#^tl`24-aU=={>BDoB0cR=7~@'
        b'2rjhfesH1e)*G!4+RM^(OI+yFKMxm*=sL4ly6bPmg_>@_h0aD!`dxMDoa@!)Yj@S9^qzF-R3lxMUJnd)dV!&{5Z>h0xKPI^E>z{?'
        b'!G-4E6&Lz_;vI0I4i7GLHn3w--w7A$^x{GrZix&1j&q~_<5~U3jNn37j=_b#%;|c3M*rh8yl=?1B%+ajasqWU@jh^&Z0Av+N=$)c'
        b'aiKNW;X;r8OkAkL8O`#~!EeTePB-no2^ShPrga7*P}_dTxg#=ked0CP)%)rQ4%p%vFEn&r;w_<}J}flU^Kk$c{o?Q-LkB4zt?;EW'
        b'$k3YGB13h$J0U}P>mp3VC@$3D#f1j@XrrDT!G+e`1sCd7K%kHI+%0jT3lr~x3q=G51AMfX$KXQ2{5OHX2pWpeVISiN8k#W*4NVvW'
        b'4Q;pv4IP7D^gxRo9$e@IkY~w#<3dNrU6=@sJMHDW;zB1U-T@ct8Fht(kG6Etb-2)md&PzBx^G;l!;1^ON@#-?jKPIA{3Ezf$0#oJ'
        b'M?%{=|7YStN9}CbB^DPNlyOH~X!oo;;6gpLoaYJc-qd@+g*IHnh1T2?E)=?=G}b0iFmFItM3}p4-|R4s4xGdK!n1_7E^!Plv|$V`'
        b'v}Obs`q=Gpp{nCJvVC6a*bV*Ic?R@-3v6i3SZwI)x5S2eG*tK*@OKw%Xz{GuV?$pWgAH{!KOwX|*I`4SxdS$Iz6TrHkTJQ!7rHJ;'
        b'g_QXTJ^~K)NLctsLR)z^aHz&p_GA1ye5k_%d+Z~$E3e^0J7W9WW3S;u#j|dO4{f+Nd?@P<^#FhOh7a{>{1EVSOMK|~S@(etZMYjg'
        b'6xm9D9kttIEN_5_3RsA!7i&C5S<VB*y<tQ<1g0rBVMG&dff2oxp$OYeXfwS4(S)2^;6r;7riAXi2_JfTcx>l)9nm{G2+8G3>Yx#P'
        b'XyaEQqxjJJi`UJNJs%EkBM?4x0z!v2deEVzjA2272OLUlx`?o$y*ieZ$@j+jVk;p@xa#IYp2jNlU7-WGAvJ-;h~BhUeRcx7SA8Mc'
        b'Xx={fEy==--=hP)FwzYhEX;fCJL@q(QtQ%YTz&eY=`#<I)XD-$O~1J0mR&;enR5h6YAX84Wb#5u5f(IqlP}gWxIv2QJi$3D{((Ax'
        b'ALTl+E2G~Y#L*{-KS7`W%T^mhCTo~PBcn7<^dWtX*=gq07AD-tM3@_N%xohQWwh&q@*E%L85!Ehgq1Om`ZF?rCe$zq(LY8do}p%6'
        b'pdRh8>yPq+_MyYyewr_=IfucGHauuw;lSTlU9hV*&|>vGK{+k}o#<&9y?}5~GpF$kKPo-INrapHFO;@t$|RMTF^bSeV1+;Y-S9VM'
        b'`38P`0D&-#U$W^?6rdWufHWt5ItZdq57Fx{#+^+`J1Zcq6*z&`)~6IlcK+dQk?MogG%5NN^Jj=Q$;<eIY9e9W_NhMAPql!6>xt<p'
        b'8C>)=XtSREB(o}nr+u1(GCA~+$>_k!1AOG~%i3_~lRuyjHz)C`{z&4HArT8?vVzDZZt(XWIKxR_kP(ueLgG_4`g=H9QS3Vp_k87f'
        b')dkOYo)_ckDG@4?OmpDGqnIdlV59ih2LW}{%03LJt2N`zzEZQkw7WcE`PV*INb|V4r}f(}7VI<X^_P0~6_}0N?U!23&EvOkzi78#'
        b'ynK24HrEg1^{z|jw_gJ3_3K>r?J;}J`tvdH6f=wM&9av9bHDjh$4;|vRXW<rBTBU#`KdOJpYa&-8O*+t!&lWm4PzJxm*tcdW^!tR'
        b'2%VeL@nL}Cg8-7WicWB=?HBv>7kgUut**YlOV#>IeP)-vI;PI7ca2nImQ{%6#?IXr*Ku?pR2(%W9<N%$ZXAO8=<c7Up!!gI#p99>'
        b'P<=;<X`}}i%X!5RZ+Hz?Fp~J%lFu`e^RsCx^3)%Kg@$Ye0<zZj*7bj^JSyz4pCf*YDT9<zN})0#zP6M5_PXMU<U~x8gvHjENR?Bc'
        b'ZITUMz~XC3qJ(>V5F;llacY?&i}s7mc4HXAYQ|?%Ei>gRzbP9dR8$1jtt?KC<Ry107jxyQeg&zr-T>kPPJE9RKB!$vBNb&LvGnA;'
        b'?5?Sb{wPHo4=sN9YnX|Ka@37Z^=POFrcFuuL(WKkNqcXg`W#NZr;HS+&*I2W^gl*TywJt-`&<UR73OeS>gA!%w~xhaR$8cuj8j=1'
        b'>sPQqrr63!ph>QZ@>ei{Za*wt9Kng^gO9gak*O+9PI9`ipd_rZKFt}BlvLp8_QwK}u#|dCm{ee2Z{I94G$3wbEJ`wPzHsjX5e(13'
        b'uHl&eH<gHEgFO~)VS8QK|GLuf8#Y~~?5|Q9Y$%OBbiP<*$Uzjk%*uYV(y%FZWM>*GUG2%W{g*PsTsG6$nEtadElk!<SrSy8itZh+'
        b'<1{m#<Wb&fz99vrsxqyN$Yx{6fIKF6iHdn3H}>I}=ahYqi8EunL$G5Z90%p!K}|HovLt#iQ4UGuGdku0HH;-vU}PSM7t2CiA`8j2'
        b'^((vLT7>LYDw3z{%IMEyYWSSuep0ZgsH9)Rh>eV&n}=DuA{de<v$<sQ0$Z1Y@l!G4yw6DsIWbr9Vq+np`S7Rw&q;3a=ixISA5sUB'
        b'f{Jg$!(&!mASXu}BA>H;8w{$GxF=(IpNBstAtfc>hUY}B`hoPVFjPDjOk3cYKSugTerq-i1tyY{Z3f$O(|qAJF%AP;0JqZ_(!VlQ'
        b'x-kQu$RZcOBntOG&-;AUMdh~{h72I0VI=57^u>mf=cW;PwP1QCk*RP;x^K^<^QmIp!GO+5OFPcD`Gg(7TH1Rr_lKdrU*B3kNohDX'
        b'9W)hDYi_qbSAmm%CH-r6AWXU})=%<XYy{Kj|Ex?ly-y)7W~c|033S193hh%R>9i$ts7Xpt_hI7+3#eQ!pKf>nX}u+RPd2H5(AH<k'
        b'q{GAs3A8A*t6>sqb16MvxL72Qq1F|dFpS|VwX3f*CwFGEE$o9zy92;}FeEJr<m;0PlCq}v6^gTejE8zka}M)QOoEz{QYix`)>~8d'
        b'#dwlHJGgwF_B+f!7RI5wIflz<kjt0Il9H))Ioj!0tJDsL*TL{D)B}<d9y|Ev#q^(yZ{s1(n$a5J@pE|mb6YnQ8-^q}@g}g)l@inc'
        b'Sv=~lio?T(L4~(IDV=UGvENyZXVRYo<Nr1)eK`3<w&4`Y(={`uzdzpaCzPi8;=dN|rDYdn+E9MiBQgC)K@MIA#XrMHX(rh4p9*$='
        b'rt~y^bi9Lku!9LQRC?AcAGA<G@SrgWC)AvnqcKOv%a6(11P6Q#ub~VzK~E4xU<E__G-9ef-umq#`Y?XNUt%NcB{A*G;(`7Jp#Ofn'
        b'hyDdB_~`iaf0h~EM->*gJD7md)DC8nikaM*-JDFjIffF?JJtsc#qr*O+MEoG8X6TIe!8gu<6-$RYLZcnp(Zr^lI3IXvii&Nc5^)2'
        b'es7_?kP&hj7O;<d9@0^hr_|u?1gz`4yuT8}59pvKEyoS(SzY~2-oG{;xB*^RyHGWvW%Vb+2PPQI=rXU}lOZz<@oJcZ2rm~J9=*nA'
        b'XSU8QH>~oM)jftmBjw~;7$YU>IwtRr^j4Y_p*NH%#uPF<63_0N#?{$guImrU+aHWi<Qqz^%O_)H$;8yY*fgF<rQ>0_l1s!391K0}'
        b'+AHs07;jiS!nyn7Ver}f71YGYWMwuC-81nVwCOV)tKs@n>iE9t;shFP6Su9WDG7`@gQ(=V1}lh^)pTR=?di#-OY*WylGQ>i{yFVx'
        b'd6z@pKL;cbbgnm~Dn@!5D}4HMvw6o`A9nv1J8U?y-aE=>q9=y$<2*{bg#OV}X^3IQh)j?ZrX0}NBj}DQ1tz1ojZdK`hA4$MKikA#'
        b'#Iaj`!_f`4dH#%UXzS+t4EejKbBf#3YQ%|r2!_-cg3ZP=iJR2eH5GlP;bGDoO)932gz?h#th`?sKN~kpWLtijy#H5naL3RTaD*jW'
        b'`JMY09P_u5!-Vzop-3rB1y<?k&9PCjFxn!-iA&IDP$<8MF1H9YqoMpnDQRIu(qk^L(BRkl87XnWL06Ai#rPQ+G0BU6E~4vr3dSPt'
        b'EflGt#>s8^gd9@Z=40#1?|0T>vxUgNVrj;ID|;$Nmg749A(;Pyr(y~qIf-NLD$t~4nOzXOS9E33u9AKW<tNGDX{ZTXFEs|p4seh1'
        b'+I$L|u*3BSg!Tk99XmH-o%M@_Z9dLlWBK*KR+8KGw&%Od-4r<YLNsM>hJgm22M5w&Z^Gab&lffZ1{@F`6+k%$X8nA=kmL_V&H%xS'
        b'KZjI!h&h?$=URiAt#Q`uT2lb?`t(|2d|p>^zcfc$l-~uDm7N20$RJ4sr#N+15kgEp-7JYFoUdW_Mwhj}wZ(2veS2>-VJ~tuY9|D{'
        b';cjtPE8SXD(q-ad;p%`k!rbNP32rr8`zyNaw7wOhsBy(zjS^93{ZRt3-GH^!oBJCB#~tA553|0913A>lrbcp`>yviK2Df0xSK`G?'
        b'XT7M197k?#^C@A%mSARs_1l*Eis!2K9N>Cx4>F*ABjuwzJX}yLJARyJ{k&0`e(J;l-f02(Bs_l#jLZRHbNyf=bU-Q6AIX~yikGaq'
        b'kVVTQnTU4O>`G=f&&(9JCr*-@rQy&GD;Sbbm@w<Ny{{CvFZNZV7oLs&<G>4*bt8_$P^-%uWRe_iM+gU|!+F>=Vej64T^vk@j&tf+'
        b'SD~FkcpV>*-M#ogulS=@!;VLgZy$UBhnC)eMYQL&7e8lCF3pkBdOa_{Khm(6ThTRJXf-s~i);sYw&bw1VPlWH<+<ki1AHU%ptBAJ'
        b';!*Aa=qb*3ptj}&>$hM}dt2c-K4?X@^&KIi4tXt15OCD_IT-&4L-iI}XBRx(-YV;@OSIJn&To|Dy2oKPyRhcZJG%->W!sBnUwz*='
        b'Sq0sy+s<JrgjHY%c+k6mRVX?X#QQ42r<h8tSsFN@_&K9H1|prt$&=yQDl{i2*67kPwH!ght;xm=%oK-ND1q+CFxdFw{#wa%o%N`>'
        b'kO!=Wwnym${5GGsO}>MVVT*+@et1~nW5~z1FOqp0wlEbGY&J;E6$aDZVa!1Zp<9H_gdkl6N|A;G<!YVF`dn?Je`oz^J}MHH478Wy'
        b'5XoaC-y;gt2(lEe0$Ez>ohFYcL0_HoIXemLqP2ag&A*tD7L_oG5?u!7_Qevd$nX#%orS>4C!dy9Ks^KxOY{XNqaa+S>mD`|SZ&~U'
        b's1*ihU~ey}S{pZsK*EI0zz%SsX{Mw7`%1<$LY=WtC4uZlghGW$<CVS&Dr#$NB-ibOC4VqeLq%n@Q{6MGCb>md2rfpsX6nFKZ?BRN'
        b'K35{z*|U|}@WDeq+3p$3x$*p?MDP3THHi}v&~~qe#3VUb*@qu!9~e$NS+L6Wj<9J{ocjCWqdo@+8^_Rv`ka;XRZt#xWsZZ7)z$?v'
        b'@6Tw%&4e^ezuKiYQpTsT!EPTEYt4;q=4u!HM0_#K)_c@*9{1nbFR?@1OYNA+{#$WF$IR+&G5U&*$_l+c#%^}i&!1`UG;X)KYD%#B'
        b'tuv8>+-j@eGPBiOKWFCWZ8PmH4*Qm5*Iu!GpQ|Ng^f(;5%~c=IK6IjoEfeiqTm$TF8+W~O=B(!Gx(@sAV(RLuEff&%+as=i%hg^p'
        b'v%1x_z0=XMWcz<6w{M(Tzj5aF{l?0D+m9vN+Z+S$psMz^R@WvQs@a?yll3-7KcqJ%SJ%1f*Uhw7IP@(pdwp_ctD$11y*XK5;i$GG'
        b'57->~H<S08p=7n$)mJBOwe{KHXJC(buMO@DoE2AoGxeLk&m4Wbll$I+o30<lmu=q$$*0=R+Z@spK;we*$Le=n<g_n-$62*}@9Ba4'
        b';+}m2AHk1npSX1&8N6#6ha`LUb=Sv~@Aq-M_xn~eA;#>kfKzXGMJil94%cAv!0*N9dI!EjKfPk|p+j}Q=n7#UeKF>dt5@u5b&(H|'
        b'r2VT6#>2DDnJb<*HgBxlM+){V_$0*^Td{f?*L$v$(SE*?_NJ*PX2N9z&fY-RbFaTnw|uqGVfQoCJ&b%1OYh~Q!v2(*^(iwu>_vu?'
        b'F>o^@C?hIEs4C^ATg=m|&YCR)DPnVcW_mO4)LxSSiw-8|f+rh46P2HyZb_f6-F$@<nuJ({Fp|fv0+Ui~ViGpD{+9<qK*&1{<(1T3'
        b'Q37R%MlvH4M%RB3KdFeHm&Wk(i<$Mm0DdYByRPw*kx=zrge86Az#4J7qB1pt7s*xfyfPQ3kU<?E1QfI`c&RePEYeqBOtPWXibb|0'
        b'v#~ns(jv1y>r!<!S|+G7SBU2BlYGca4@nDGc1~==rTd)U49^#`74v4+bD-j#1}m!gaLPyTdrZ5dhcwJa46@&*yf{3YH#dBM7Dt8T'
        b'`%8;-OL(Xy&>3l$W~|!;gQoi37`=gl4n>N{$*li>-X@mrE06p;jJ7X^*{Z&rQ9m@J!~T22YpAM{MG)&{k~L|K5v9*B_sNVk+J(mm'
        b'?5N;?@YvD5HoSr(Eh_wW*vyHm`9g8<hlDschHZ(RPb}w=O=>=tWO7xmJ_hWe+(&(Y$8UzEMY-Wa*Yv!8UX08rgIKNB%m+QtcE9yK'
        b'GayZO3-o63`oo?y&jo4m^jb4-Dm`Ep*H|G4)4#!w_SHwO_Vgb!-iGU|L*M?A#HXBil8mes`05SG6++TqJrUCzAvMj{?FV)0w_lv*'
        b'+dB)IAs7n0pv}kFs*?59)7dmnzXs9)Y#N7xK4%FaB&Dm;D}?AwqG->VN8p3u&Odr|_V$c=+l-F-B!e93j0{vRs>oy|1l<>><fY~|'
        b'5{tRBd0CIiUQQ`aHHVbuc23M~=1BLo;e~x366<EvR{)8{hF>5OmY#rto#MTFrumWr<Tq5{bLriRALtJP23Ckw2Lr%0T4^kOI+9Z%'
        b'E}`6E;5!Cj5-sls&QV{`<k<-)$N~Mu0<*F2*^2`MmkPcyt~5uP`}!`O{7gS^>D=ifF?}+$CWf6B>tC0hh?zTFG0rTW+gm>819}<O'
        b'9l(*0ya-?82LZ47lH+uN*o6l;t|FsMcJXr2$>Z2^@z*}Ga9QMdI*_A#2zSv&pj=89i%-&X{~z|gKCY?j{{P&Y<Pwrgy&)kY!Fq3a'
        b'2q3f}_yAO02s9vS7h?tGJ3B%J)Yi>emDcH+q%{Q87SdKAYL~>KK+7uhL91m$W>a;zDeY|QYG++_w!gNsu4^q*^81{d@ZeL`uKVu$'
        b'ef@s_z|Fnq;d4IE=iGDO$2p^lJ@Svr%!A2cGxBCMIl1bWN$TAI=9_fx_NcJV-(5_SD%FAcA^zkby-Bg9+-906or`g1<{c2>^osSd'
        b'3B7@-61{;_?hl*i`t<HtiS6k$-V%!>1n_IhMDJAK*RO1EY2ohtnE5I5CG)cvx#lJIp6>L)l=k%LKx-mREs!jh&=jA$LbMNC7zO#R'
        b'2-tomuvXF~fPTvN1(r?5bL=e>T0}){mkx`%@bixXt)j&e$N2#7%s`I%x!hr4LGEsO;oYhgi{dD}E^)3xR+R|0bC5XwQedeBq(+O|'
        b'!@I->i0VzFkB*+`RZJ}Pvz^}eY;Bmz*CZ<EjJD#WuXfIzg9qC*FBf<WSKT}FO6I-rd@8-Ox0{x{D@H0kI^p%Sv#sGR;u%gv>ph<O'
        b'8BN8Re`yWh@X7cU5Hbtk{`7Es?@MV_JNbyQOVIpsAdTX6(`jhT1uOq_(a9#6x(BaTx_#~p-=T}T-(K7;X%sZ5Bx^1-+$E-?@!@|v'
        b'bRS`qM5qUug&^T#V1eZQ<6RO^@9lwJ_tDc6a9XK@oP~}|E}UQDNX4F1xoI_8Af%~Tf~lh23XJ}>4HWt4alWwLdu)PjDIW6KyaTy?'
        b'zg1wB9gu;;TAbbg<)OoBV3eRyI4`1Z=a(kym)U!*d%I00ynMP-n+|i8Y^PP5zH=w`i#wg{3>T>Xi5Yom;creoNQseCI3v%>ewnRi'
        b'wdr8Rd|}W{D9k$98sJG<_}3HOgG@;JIlo^`IVbROP~G@7^q;0{olLrWLbh|N_)N6IYAv-sp04)DtJM+p)9*lHeVw)gavTcT4}2Q?'
        b'N&4SYT^^!3MO?o%4L_@^PYdUH^{}C=2V3LnRpvJ@7Kl>Gc45Lx0gt*nSwQ>JS5DZW9#40AI=hinuV?GEF6`opUllEX^MYD~e21d&'
        b'!sT;bc*?T%Mj4{%;#Y;{H!mCz`40U<`!u_eetk(Q=~>>5!t~v2JudySm)*;9_f23ohuYG;aZw$I@S_*JPz)MkYgvCFkS3lQ9?IWn'
        b'Re3FBQSVDUhuEXbCwP}l=-ei;QCKwTg%eB}jOpIy-ide$iEO`4wPvtc#OsgG@J^SVZVMF1wz!>yM_Y=6W~Nu4!6J#?YOT*Q*AT$n'
        b'>E=v=PNEgsf~T^|rW>XT{Q}fZl<x>+623!hmYJ4k8MZ{}o<E#Dw{7l}IrAycw(iz2;H%;J-xsz)>@GC4QZ0EqGi1%b40tlSv%+|q'
        b'XLPia37-U(3T8>BO53Rg(k>$5<G@<dnZL;RFj4C4UIaRUA^w&)@oay4bXd2O$ess@AN;reshgkUCr;o2LZ?cDJ|^~IuPwEMnV?C!'
        b'%{F?%5eSe;7<~%n`}=;LdQ>?<-4n3gj>BkC-$1AquPf5Wtn0XzJe3ndjtf+{O;&4fYXxo<fR;@MpS&aMOIipvgs-c07Y6IOdK5_p'
        b'?K-Yn9j9qgYqfb>etR-WmXh2;B7xom(gcR;ymaJb_c-hsH<B3ktp)<J{lLW}aqsf#tbfoXeu5D-ajc=+NzR&jP`K~846U8%5^NPz'
        b'r%v%4U|)Z5-(KyTkB#0}n0l0$VEYVv$engZ{o<jWpd<^C`UMh{JH^TUGvk1eZDP2FjM@z~LiRN_ILt{l!tN7-_1b4sY70_Zga(V+'
        b'Y>6wg#4oob*tVzQb(qgG)E-YwJuR*|YPUqLxnQ3iX7^a}77$em{E4BRc1vultaY|6KZAeY6%$&m6Lb;fH6)+I^Zm37pqng0XAur}'
        b'v61iM?F=36;*`fqi*ZYQPoI3a=0f&S`VWVNT|_$xy`HkD`YbW$EwKrYlOcPypnbnhTPvVzmxjTtNmYI5wN5EoEB5SViuMkqzEjmC'
        b'aX~;<jd$Q#M(VDrCL#PD?|AU5%5~$WP?cjy2%cqPwA}OOWfjbis;iWwBM!O5M677MbIpM1C#Pt7F<~0$X{Td1(WCng9-*Io=hsnv'
        b'2Y>U<B&zS=L5u~}ckq|*OiJ%N*jn5^e$%JKjvuHzzwD;zx;G!&@ZedZ=f%J~cSt?W_QPRq?O-))E&>56r{mK=1x=^MWs&W4@7w(L'
        b'EaiCQ@sw^^v4NImW?^G0dgE)l*?%HXbobZvI{%*n!#UFl5%2`>Og|SG_G@Q#JU;FT;b8$}S;O~F4c|}rZ1Dc~htK$h?rMC-&ve81'
        b'jQ>Y>4SdG=8UHbS#=A1UJ3eDt#{b7>{NIDms2P7V_>5!6|L?|UtkM0yh|g$2YlQ{z8(uC5n@-Te>9VClN`zl1jy7ha0-^x!6cCFP'
        b'>+_})$}<CvaSgAM#(3nDQ-<fP`L*~%{>C};1iN#0-rap}zRW$>^h;66eAUyY+1!$*y15VSSdxw>0X83=i}l7hZbQ3s4+~p4TUiQz'
        b'!6c_TpMP{`8`J5r?rdXybErnnC`Nc%VS5(W*eZEHWp^(8s^O=D`=^t5Z#_ayx%1}~HtFYfHwos)ZKWDsCALz#Wi5ik;Z2<FB^<jO'
        b'xq`U5yzc371p@ce1)3&7>Eqosnxft3jRyj1IW<$L=QoDHKsCvu`CSv(my2|k&310H+OkC*O&Kh1v*qbB%QMR@n{@k_s<M=%f=|sp'
        b'Zp%!m?I--)lH1%G-a5Uv&CYG1dy>Uq?0*Q;ahqq7$#crQb!HyGF{XkhvnQ_kvdq751bkzi!IG!8)ax*aqeqQ#aD4d0D9f`8$TG`w'
        b'YR-*gf=aC;(S}^zZ~s&j7qD|~tFBua7sP99%)T72F$?cSFB{s6-Z%oU5pRy$(#dTu|1hv2#<(ra;Qc7HA+gcUJ(~?F$FtB)uiUXI'
        b'3~zyZkEE&Pz6rFrEH`^~)0(f!EKMrIRFU1Xb*b2HX>eJ78N^RsZgJC;fpe=Kw_Dr>A^Pz3bUK`Nr_M}m_w$dpF5iFhN6%O7C5_b-'
        b'&hCHlaF{0y**eqh7LOxN1VkmgHNayxZnNFTYlFoHH%}jho1}~L`7B=Ld*3MAzA;FUGVdG1bI7p^4es>MF4AE5#ymtTs7?@sn{Kd&'
        b'Bg26s`MXHtvM|+jTCz3l<Z4;ljv;75AyVZnKX9b#wZEq3S4ETlKZLLw?+aVb)njNv>5(=W{&wwoep}i;X1Pzhdd+7v{(gx2Wsgt)'
        b'2*$=EPg?^mlC2`2Wh>~1e=ItZE9(Px&hn2zr}i=C4@h4^Wb8j@)W%llkDsJ^xzkc_FORI&Q04>~4r)6z!qoib<&kFY>E+y}BYCpb'
        b'bIosDoF_UDZT!$|**af{G3sy)ks(0_ti~1c4CRpq?rAf(sU**^|6&2;mRk+n)&=3m_WxC{FNI%po^cswPU<eqp1f>-V*p{{tN_Wp'
        b'qY$|)O~yRTCLY2Ov*|U`krL+P+~W(cgmA=s8Uf)*tqbu<acg`k{|Ux%6t;`}u|qs^4DzTGc*Mh8=BG|n?eDSFyUHUQk_LGc#JS{o'
        b'WaoKQi+SV>@~B40>o#8@#3Ee&3KltqYrfPM%rRJ+7Dzx-skwnpuIc0q*`B;}&>YxKlL3P{!Xx{Bh$9~^=e9b`0fWctxE*zJ?zQ13'
        b't7WSnHtaug4m5WK<|Nc{8>ILlU*m%}6(nU0qzbCGk<{-g>10~zzY80w!Lw*N<U<V-{AH2b;6n}y&BQ`=;b#vn4~J)A_=_7H*J6b('
        b'u0fAK@M<uo22zD~_=RyC8~jND;P&gQs<uTO$-p02W@qUH81oK)58=}m7WVlj0INr0d0<GXVvKp0CW1kz5~`XdP!$A~eHZ8^$jR_N'
        b'Sr#7|dtpXV>|<3)lT_7qOTBqvWN{p&i|6@X$$z7^FjB`oZQwRxiDl@1d$B-pWU?%K>U4oV_{}S>A%Ysf_{%HsrGZKivEc(kmuIDg'
        b'x(`T0Znk3sM6HHcVQ^?LVgpxS{4r_Nq1Ru{-^Kuy_(Q4eMS_RrJcem!aEvoTV;u1fDcLSKT@Y9#c{m0J`4$W^pC2R)E_;eG76Hk+'
        b'6QnsVa*gBXb4%yqk4IO=I`WgUu#>7^et%?DBBhJt$6A~yOkHQbACqq8b*u!azko@=d%o{kEPO;^+>8Aft|Wp=FkD>cal`#1hRatl'
        b'cJK(m4f%`KzCh(~qXz}%w+25I;pN4{+I%K4+IXVrLCH{F#M_YWeR6qRB#$|;F29AOo<cmyW%ox`CWJxn!EXo?gsFF5N%KV*^ddpw'
        b'ENUI5q4F&0xC6ajls~LDWltf;qU-Ao=4o?Apv;Y^A74(JG3FYyf!+)eHpt6s)3r#z+x%jowIa@6iTD~JM&b&2mof4prt-cZ9~;i{'
        b'Fd?f(j^W#NACIA26DS+f{roF+|6d(LX(`tI8;t>k1Y=Ddq8(Hzd)gua7(Y56r2U7W2Y)8uesBytgbfye3Y0ocL=Dq!fT|O~Uj|X|'
        b'M$n#dv$WfJy(n0W{pHnqbOq^)1f`FrZ_*%RtEjZJlvdD!(g{y3TUH9(*H(3>{t?mwM~V<j2ixvh(wL53uNa~0nF8Ytd{cQuAXBnb'
        b'WE=;1O?iIvZG-a36gWb9rUn_QBZJ@E<|j?$$7wE$<iEL<jris^Qq4WB<NZ_UGuk8ZvXrzeGK3)#$$u^^8~$84R6bN#%{`kem_@R8'
        b'rYFmduUyM+smHIjTeyd*9<mKb%{6ESyKO+jWQPG2BftH<Hr-UspxtUO*Lh%!7~R0%Ul{nG!c+B}AP!Z~eyQMC=*!0PEkj{D+4BGM'
        b'KW8ktJPuVzzj;gK^}8%M0AmQXG&qiSLC}cH|9lnwV1e10A^L+@q9f?fxDoxn%ji$x>Hjvp8mZq4DC6fBzrUE<d~_ffbB%rf=9o+E'
        b'xw)82?Ywr(rLGlotyjcc&$VN&>(*oL<JXJ1a^$GILA-i>pezPa_x*cfZfWV4{)!vME1+`0u+3gM28g+nzI_Y{I|m@<QfdFLF|6=U'
        b'yos3WNFB1(P{0LCxk0>rZs0#1Z|N{FO5O7TZ4(38KP_~aNSyH(Rq+D}8K+VF?S`4qI6RK3VY7sB01pi(M&|nyZ<Oz!3g!EY_<Vob'
        b'VnNVfetWvVNTA~y=y-hw3&Wox(pehnUrW=yOPX^t&7OzpFmrAe{%Cp(X~1L4A0Augw~Vb_fJawe3l8-%8I2elxSSC(ns~D^$`tUP'
        b'CM!6Hyn$+E3a}FWnWRPLyley4lqei~SV&9T1-1*R{0BbyZqhNI)V6i|V0v9l;uF$R6ZwUVCR#|%A+P0tDR98s^S6x}>3}f~;J5qV'
        b'M?(JB|J+Uc-^t&}|2j4Vz3-6jUdR7B?AP(Xw(mUWaeSY19{CODJmm{{|9h)*9#N2&RS6=qC;nUguQBT;{4XR*L;m;9tNrif8~ERO'
        b'y#Kx9-{yaBYR*H4(F%$qZq)~u&*XiV<8Of*`rwJT?1QP}fg9R4(0Bw&)o)03;ZMaI?7V^cVP><bdfROy4b;!OsxqH;$pgVLEG9-c'
        b't1hzn2O;}(;QXliO8YdQAax1YJ~K))nAmUDKNRbzPM)l4bb)=A^Y$5B_nMrDv8l=j$K<@sK5L&?EPf=~xCil7!k|hJ1M9LnLlulW'
        b'c}(ku{Ka6O)x&O=&yNPj5*h_%<%y<;h{pNRu#f!)%b>cIbU=QDN&Z&*4AOk@6qZBn6BGuLX{h`-XrI-*Zu4Y-<{K-&ou}m~*gpLW'
        b'uAnXE8nh)(8Yb*I_URnd?GPuyKB=qMB!&l460%SKf*>CoJ`UzbBgY^>#!25khJ@R(efm>xaSYed@vFzMf|_*0F$i$~uU7<h04y^5'
        b'2Ygy#57NB|D1MjtOngOp6d5$l+tH9Z2UoPl1P^2xN%zE?rMr{YiS>)c{-M}=?FuD>3DUAj?3TA6zX-cO8pwsL0t7Kd1gV7~H;azb'
        b'^2?@%U=o$b7~tB2A(6};#20Nc=Vm8{Cz`QgH|Sn`RO@6Q5JQ`EG###Oe5y{nqW2*vR+ssda*iTVG1JUFR}oK9xp;q@KwC|e>f=lA'
        b'&yh|v?AMkqVwXLXW5`9z9Bh$zz_9-atqdY-DTQ(%A?zaznWB4RV2Th5QTYhHUrj$%nV|qzR_530{z#PN{-w-Y7gJ&U0k2Pn=MXK{'
        b'anI?eGk%1YO4dsE3CACOKCYeW3bR{w*dp+|RB49qkk*%rF|brlrBGz%ytK+ELcPWGGnEsGt}ye9L`ex9PRE)KKDLY2R=d;eoUfDH'
        b'X3gk6EXD_%Znrfi@E>e>UEFrFn5e5^mFqC3y6Yg}vUvCXHRb3NLw)`!DTudK^w+PT{Z~lGdjW?6`GD#+-JykM&Qq$NP<XdN2z0?9'
        b'OBd$o^NG@h?6MU(%ZzN%+m~P-2}9Ibnqn$+{)O+aFqwpAOVfsb1T({T33KjW43;LH|9%(u9Hdj)rf&RN0&*Xva9R*A%)mog9Vc~$'
        b'>@<<iLzwyI3?5`kx0Z2D&`{~UbIRT&%c$%Plxi;Uk=87GgxL@_elEzk%=38ZBBn?wadBHsHQi^TNn-+vy{*p||H&7}1LrNj^pC>W'
        b'AB|tg$M^Iy-$a~RO7tv|HnnZ9QTK4a?Bq84xGlhkQ<moDI|hIcr?}>#PbPNqxF~yGvmZFuX=wx{_Wg-$Y=dSF>`^tX@2bAzg%1NM'
        b'HDeDsKaQx`<60ttLfdO@@A1W-$6xQ`HV^%wIeDO{Fx}3#REuBF1)H%;vXzZOXv*cw?!n-1Pj+%oxVJP#&|_44-Oi@5HG5ubJF`A)'
        b'{fRzHqo0TNI5pJh@5|!{iu%U~8?|B_`$lCoZmh>wz@w%-amZE^K_{u2YO89-F1I}CvOIC7<~nUPj~gh;)-2~ypq61kmd3<0q+f$D'
        b'Cl`00QIh_66dU34#UJ;&-5A0Eo#Glhf5#lW?Y-MO7fF{dl5DT$f{h&x2es?7G?&K=fX?*+58F7O_aop&+lyuXb3RMsAd*Vs5LngD'
        b'l*+Vr7uSf9RQ6OH3@=+Gg>u`g$Bh75!fhu+4HO-UE#t{t;sh$O`Q~+>QIP&P6dP{$#k;+=wLE=&LHZ(^#&%Xp%PJ+?9fS0VLB>F0'
        b'IfG>kBo?)ez6?yO5lCJBXH4Is9YEhMRmDDMN`7*?oomD(I(zaCiVc-KeIXQ`pp46<14R<~Fp5s2folYv%@XRkCl@OQ;V<kMwFN_k'
        b'yo)hgV94vUs4z4P%7xoHO$`(+xlP9dbZGCgf_u??G`fu2YUiFc70oGeLW6e8v&z4R8RHQzq3PY*6(7Wkm;2&ty{lInrO0=Psgbw7'
        b'wzzeD#&$<+Xx!Mw69_!$qFV8A>-*1v>bc%0J7%RUYJE-6@|vn5KdEcFye)4!G_c*VE{OaQY^3|J_4LI{O3Bwo8P<V)%mPyF{fHK('
        b'Ofy)X(1Bu^E<ka^kYepm=)a^~a>*~k*cQr2Vh|C7Z|e<f!i7tAZnKMf_A+paXYoD>m@TQE$!{i&J1!VoF9d%#<KLfNFn)dkV@@`K'
        b'XQvg30@7GL;Mg{x=AI4h(`ppP)~3#+B*+;zWA|%uyHY5poW~igP9YA)IR(4p_TaPOc8l@8q;;=}RZR`PxA0#7xlO_(QE;DQJ6RzR'
        b't~pPskX=FH6F8hq<J<OoDXnRRmR;dgZ26|~qlT6Ur%>vw5t<8-Q$dMQmoPz0D%}Ir7m!w>mb^ycmXwA)jI^~=f;5}OtwNQvMq#9o'
        b'eIaAcGurp(nfDuO-kvX{GwG<NFKa%Uui*D6?tW{_KkdKGtLCvJW+Y>$9LLaP@>?}>O*G~FdyRk+p`_eYak2pJ%7;KM2C*OXEA7d|'
        b'Mq!#j`KD-Um_Gs?7PgZ$oK2*LrdlXEys)j6Y9aK$?QT+bQ3qwGF9ZtJPVRtgL)+>V+Ny4ARS%vXPo)c#yQ#?&x(^G0j;}a;(6aJj'
        b'O6%;-u6l&3QLYuG@%v1L8^hKT>dJ>{Qdjwqp>nOca#>mB&+L`U)s;U{SFTZ4u25J0TwS?ZUAanK`G`TY)~;Er6C#yUtN+qa{DHl4'
        b'ZLh*{D6D>499`?ihj@D`7-fafu6Zakdb@nIOY@L-Yg}eHz1|=|g@q7)c0De0d=}``Jmk|nobXvdx#yDq<A6c43TmkG43(=2qE#8v'
        b'yy?+dV(Rli>YT~o9qvI>N$7SKRaUw3yyvH<JS%*jC3JG9XK9b;Nq$Q^Jnhr0HH(qzL|^6FKF`8;o*|7@L~$4C7>8ySR6j$))V4S?'
        b'GqnX@&V<Xz)ZEE%`4ECG;Qu6KYzmtqu6~6yHiS)SEY2j2<!ELmF8vsCxWayfFZ~ZgMfuDF`0hPu<^}j~T#BgmVdzJ@tNF(4p8Mg#'
        b'QH6fwtd1fbkB9jy(brI_h$#NSq#bafN5$ESKF^|e_&)8P#kg5BL9Gtk^$b2jyLc~Y{3+`5JO~B+iHKSehW-lGCZXbKO1ozn?(u%8'
        b'_7Lu+fG|E724nX;jDO97TC4G}$HSeK&^uKgM&%HgH$$QTHf4rO3(Nupg2<0j7=HxygQ6&Z8;gR{hao7Z$|x9<6|U2)0zr&XW%%zB'
        b'nKdi*b6Ioc$_-J}55r=GeqTUuny?|tKO+nhlXsp88}9^Fa7YjxMMWW`KQdv%SbttvpO`4#8qPnX*ZFTl^xcjK#8-4o4Xevzsrmr^'
        b'sr=(#99d!A_cCyQa+qDSqW9gtedn05Xd@9>xnjO}eze(RHRZ9!bzqur3Q6M~VSSpFCpXHDJI^^~_5(+1*V!vq`qu_FC>)wFpfy!c'
        b'oFS1;q?LxsmDIxl;K9SOWyxZrIE;>hb{yvr|KEuB4ViriE@z|USh2ZsjpK{pBkBua%-Z%avqyirM+`T7FoY;7RB@&V{?H=hr%=EC'
        b'e3IG6!f#jQnplzX49Z_fQWFDa%}*vnUYUYka1?L5?PP|m>>VO|Qi}k8>WX^2yF0zzeeV#fd-v>ujD2Td7HJ#{`MROlhs)ZbY-Wpq'
        b'KijBGvm9p9lVa_`Q(h{6qN`j!SuIj)eufwI)WTGQ8mv{bOs83XG6eA6Lb~1|O6IqUFjnUEi-*dpHLKKxh#HT#G=4-Hf#Ra#Z8T6}'
        b'04gT52#mt3=xq+ti^;_W%}{V63@v&jv6F_04TIkK`R4V=1>TetwFa^GZ%D5loJ9#r6Z-!&02D#;?npu}P{rFMKuPvgAVV<7;1IR$'
        b'VQM3M?-00HHcu_Gr|DwP&sY@uSg|@ol>jcUY^g3SqB4%srKRJkO*Ow}x>ToAYs=JlgW(c9yJ-=Ws9Q-q5rX0iBJfE8Y3V>ME^SaR'
        b')u|J-x&+-YcatUlw*qK1XhSl3VN&t7h+*DdN$cq+fmVMkPiuH+Jk*$fiB6oOhv*CgI(a!<lTx#0mFdp(`I6)qswFT;=b+YJL1+28'
        b'@0U(9=<3bV3G%Oz7#|JPM<zL-jx92YuCZ6HaaFGN<BuC>M<mhMlI`$YfanBhs6IRijFWCQSFWZff`4<4*&ZEM`O&>Rj#kM3Jr4eF'
        b'fI<}bzg4OxSLG@w*D^-h);eZ;3<aSd@9hj0ZMFqA#5n#Tf&v|9ID0apH~7S8XPeb0L2uUnrXqnfenD1DB&l`6Sc%>$tN>p;j{vXK'
        b'JCPpas$A*0mr*vR7fp<{YkmR>Tm^cOgI-9i-WFtJfq)WTuD?GC%#th(`iHV=pCnYuI0o`Z;P;m^vSRJk@foTD1DM-V9X1|b9UIgk'
        b'<^_$-88o&65=@}BcDfkz8;Z}0!1fv9_fVC1tu9^{D&MOx{zf!YVtZYK&#061#!#P=F3pNop?!=%J%-d|rmb0ASNEmnHPZiA{9wJh'
        b'CH!Qk%wB1;Wyj(CM`MFJAM$m=)${RxpJqi;xT+EFBDYT$r%|pF!A3zU<xfK|R1ESVbC?h90?dho`vOxXOGO(+vqX+K>?^B%(oo4X'
        b'A@xlFGvh0s8Htlri^@XGxO!}tu_Kf01a_>?5@S`u{8)NTek5vjiMm1DZz@f=k(x#E2Vm0_zMM++cn}P@r}EL}&jdZ1M`6rwx=G`M'
        b'SV=&}zGUR;B_NT66ufh$wFg3M+wRyt&CjKKUyE&}E2fHknk9*aV}0HhXvI}&?eT~^J!n~*)%Ih|b(h8pEuQkW^mwhHfhWR)rB;7_'
        b'=*=!c^I3tf^5^gzN>xZm>W3mvGuykwHwW<)c4~gU=93+&IX#+H?p~MX=RK9HDzbpCC5h9+T$+_q(DjuUpLyYB>r>rzUQYVzu03RB'
        b'_U-LrX#eD^GTT9%cW#tG+r2UVpOWtER^hn{+4zjZA_svEhZ}(fv`_O;W6YT`NnH{kF35)R9|nLT;KY`g4Y9@)k@cnSo#|ZVOJlYy'
        b'glr!AE&BLVsz1;ov~}PPHb`298={Prm;6$Ja;0#o7_t^9lo?$hZrB#9ZR*ahfTpu2WQnc2A<(WYpB_-QU3x#!FUP3~6gFjam*kaH'
        b'WJOOGg8?tW2JD}6$u(qQKR_=S8@2`YWs$%!9E3yuEHkiFvVe488#6bAYz)ec8H^DHv5z%?PfG@$X23oz|5`rH06wir7FwQms~3}4'
        b'sSH@B^5evyQ~X}|VW&2%REx-7CH0Nar&(z`l^C)z<JUqpSPW%|6sRLf%>>PwMON#Vn%$)T14ys2m5IU1Y!-EJZ}xk_LHmM-aG4}l'
        b'J$^DzR%o!#7c3U~H4xPsLLo8}PeCp-Es$Ax5?I#)k{Zi1V9*5pW4`0~GX-u}R`|`19~;#vuoTTokTM<HB`Ci$kcK_Y7U7meoo40a'
        b'JrP}!7Rr_w(iI9O3}u=}Qu0(4Fl8vKe8it5z&bS_nO_V*mg;$q@l{rB6)T;YMJ1|XKRfN){A@xr_}K+PKWo0+&zA9icG9)|Y~^+Q'
        b'EQHQl$F==z<#qgQxe)wpSx5txthr#Xe8gDF3szVbbheYm1=S$)!;qV`eTe6F%9u+a_Exca9(J!PM^ZROjVYT>rHMfPO9iPS>W**o'
        b't>t2nzFAYXH0WHf@~xNw|KJ&rFiADfe5G%#ypC_>L(Q;nU2shv499kSrb3#KrvV?nqVv9vud^r9G<cNL4cM`QSM@9L^b#c6B35ky'
        b'pL*ypxYXUzsy1+@(XHS)eqNCY{`A4b!qGnO&dZ!Bofvecr@T7{J!!~|YF}a#p2mJO=tTXO1igjeL4i^`_MeBtcQlfYN$9*Bfsckd'
        b'^afgbzVgx4ZMLuR8m;%eg!7t5TO@tnmQyL2o!(zV+k1AcK5=-|NtpFWaicL|KJTwrw*kR>cKM{})8l<!YjC5#*D7sVz1O|IQ;d4}'
        b'3<KKl0~h-Dfj-TnP_^i_OGXapSmkzt|F(zx_k-ZS?cl#*a<$T>sk*p$e8%f5N`p@Pm0f#8#d}C947F3(kG~?b6>~g_6f~zSInI0W'
        b'xw0Nj6*zI41}A<P^RzMg%$U*8KX4n|Y{K6MfZ-cTHf%BO0fAxrTKreLrfNg9@zOs_U+T8cL9~2l2dB?`Otn`TM-=ZJ<%>t>_R4Hi'
        b'xR6VCX&%A3)Fadv|3si&%4dZBa6BP}2_{VNrFmf5s;24DlgA{VQH%->yi45te+Gcc_e-FhE(sX~NS|+o`D)R<7kkI}UlhQ!)SW>!'
        b'5ZCtY1y}p_=HmmycHMB9U0=_)iGseZI(Y8cmA<V2eEW1huMYXPtMk=i*T&nmU63lVJ(v*k?0&1j&YN_!KphPxoos*ctDtMA776$S'
        b'3i1VP+MlpN-(DuTwsC`Lr&5#w-N?5$9~!{E9p~#Ke7oac^X)e|e(c(3Q83wp<hfBLZE8}f+)YwQl~qsqa*;KwdrMDcMhv7B?cy%V'
        b'_A8dpHh@Qy1=*mapqW#{2eXvdTSJLPoM#Uk%rs6P7=ScmOHB1s<0u(q`;m0GKKZeY0+wBY^Y?I<1i2er;i%}FudQ+2y^;QL0$Oa('
        b'MXJsXZ&&V>Li$n9hICb@c?6=0DkCLNSNRA;73ygM@ku*&!z*J&kja}Mb8pEiS~;A#Q@Nmf)z{a()13p~Ywiy7`r4XX%iWKV5K|7v'
        b'2X(J@&3QG%l;4rqo=2qc$-xvp>(7_x?}cnIe^)NKh_m*^=v&iwBZQb$!y(2vGQ{lMWliu64Ce3t{|Wg!jxiL(7<`RmjQ_t-D2Fdk'
        b'ACbfVocxz__@BhzD2Fdky*!7%kL)dh@Pnt_kiYw09H=|U?$}IH$;c;1!HUhSz;lQVR(ZV;f(a!7enTi()@!YM!3u;1gGsP7jwerq'
        b';tA9#%DQAsM5qsZ=?RD_eb<^3tb>3OKRhcCRR#mf;Kbm!;|3=N%G%?hX~AK9U^v7Quv1qGac0czLxu`mO?YA;I3?JyWJ9bY0YgiG'
        b'PdFNNd!rOA^mr5enf$Q`hnYwI3Uh&l{pL9crVYUuGv_JQ-YpX=_sUv?7&Tz8*S2lku;HpQz-Il${mM6l>BQ|2WAGwo-n=o>!=-Z#'
        b'5M!M4$K*#RoQWD0B&I98d>y9c{TL`m*A|4Eg-AQsY8Ig#qWutGYN5GRR9-*gmmQg)wJR5ndZDPAUl_wv1AZOv^89hdz|x?X9g#mS'
        b';@6p6yq}#O`&c#j*`%xeY{TV#);TzbsD(KMUS|sV*+J)UtqFv(Xf?!`x8is^SH`Ti^K*w_gqe^yG<Wy|F*3lIF%Ok{mX8cCk3)FD'
        b'^M=Jj9A1PD&4`@&s=V>^!eC^%EN9Lf@^803=1f7YJxhG8*wS##*dkmi#7@67<n)co>&BV<jF>IU&*kAbBeW@k%Byr&LX@E{i!v{~'
        b'7m6~Y2B)*lWxTSK;02$>WBH)6v&jnT+UXJR3V(tQcR>dk-Kv-J_eN~+!8GOK?V)LkTC*x!4f?6BT*a$sn#l31Zy;$)T`ZkPi;G_a'
        b'>sgt)(thwgn6uE~vrFS#mA`O#t?mYXIk{@e7EFr79FB^oBuuH@F_H9-M^hv_qRcqCQ=`;9JD$O3i>DsP|L;V`0`#L=xOCisinDL?'
        b'z4055XT?`b@Nq@{9OUy@cDzD5egGF0#o45hg^P#rJBc`C%m)7M`Ut->?$oR<+KYTX)aMa<^4Px0)xNezcYKs?e&JEDgbhwJ&Nx+b'
        b'fnKxb7x@1#aBTBwR-fA=^QOn`+0(fhbylwS-Wlh~WBhXbE?2YKJ3j7Qmuyd)&y9SQtDy_Jc30af>Z<@equbtTd%*bj0IFKJ(D&k_'
        b'jxPef?Fi;?oj$b7ZT7VXpdDW`0$O4veB~<h45ZrISy|Pmd1&5P>D>8aw?~Dknwlao0z&7Y%ftRAKjd$E+kk5G8+c+^^u{OE3scNq'
        b'@PSn&#nrFK%m)JCCObt4uK`XOFjrQ=Ll=Hn+(a4`L@eFCpDFru3S_T9Y$xx!?V2^K_x9Y4K*$Ru#S4FC(EMb}q<lUBgZP}C<=BV7'
        b'Ul{k{n4izv1k8i7vmN^(lrE3`W=3YLJwJJz>S@=AwS412RP7_FHxa+yO}#O49sKwBk+C=U$ao0v8-vUv1wp?r;BQW#gC6K$N(-NV'
        b'T(MSvI%Qxm|H$XxEx;4JTFbv%7(q|Q<@Dg??8_JH^9C2|)$b6621w1Wc(+h}t+je{A@Y0iYXwJ;Tt`0tE@W`^`x@^;PLI2S-jVM@'
        b'z7xG5lfvmYOK%DCuS7`SEmXcQGVp$XgVHgBCx)cv@CkE>05(VfpS1b!#lc`|MD<|45vQf*qTn+}$<@#Bt<fKm#tf8GrZ#KVfL?)i'
        b't=<dDmH&*W`L7uC=JfB#AfzsYAEkq=9=RNU4LO(71H*adm3(sn-}?E~DkVeJ;=7!04VUxHIf8GsHLc<+`POhPzD<|RkAX-L<k*(4'
        b'^0y7X6mSSG&xZ-163;_`pCjHI=y<lq#X9qoC-ZCtK53Gu(2`NCee&hG-;ih__bZ&y8r%=gR|!SP$w?#2hYHV^fG19)ct@=BS`C`2'
        b'?8)H7$~3FA6S_+>vMb6eSNV+>?3zcENfh{c^%$zM%;bo|d8KBB@+r`VM=FG=GzoJ_a5X0l5U~mbDm6?ZzQz;YOu>9XnP!DSDafSq'
        b')qmz!Z*a1ljFiU-+vm6lo|~yPD~ienfJkVxNbt`!Um7YOQEMI<#I)J{Ry(QwZJuVcw$o#^<>6Yr*=x=_B9Yo-P5z5oU~GL$UHGV4'
        b'aJTQ!T6H0z7UZc5QL6xwo`S!eyH{p<gSAcLc-SY%+6$L-Ne&B3x3jiC;CqV&$#2d73r&VFgDM0hWkws8&nxSl*iI(w|6+CwSNyc7'
        b'AQF#nb~Id51!{f~d3F^1APRI{1Rc}dLYd>ogq^<4te_fBi+%A*+bG=l&|V9xGtPc5g%ggmQ}fSC)lm4<!iKXJV-%Xah}FN$vOc!i'
        b'`-KvGLj*Qz1+``+RD(LL@xFx={HE_VIa&DK__o%x!l}?|S14PBjUP26rF9A0$>z@jFJ$wr-lkUY=cWJ&f5TH1ABUI@w)t5~_hP`I'
        b'LMTZnRVNG029%^wsgo6aoqMQJ2rlpj50({f$!^#q<M((>-W;xSwhC($4hntCCXe2};XeCtpDjce!N}P125JcJ)AlCIV+|b^G=Ch#'
        b'ZvFmnhTdVX#u<8x9mW|t%3cF!Xg2pB!x_rpzB|rP0{8!MhW_{9486kM49?K=?Eh|@AshSuBF<0_C`vooCFq@3qi7dH_xk;8^Fv?Q'
        b'J>V(H8b#2@iPV-Yc5Vya^lRBX1irJunY5_LfZD|g_kF?H$GNyBO;ebf+maLsnFaTYaXPs1lmzNIlkAozm|t?MM-<YjElr(1t!^K)'
        b'=Ov$qIIXAbT$4J9_x;hlA5K!*emaiF^J#*JJ-JMnG`+|t=;WI4meU2_yzmKhaOELe3&-(?Y-tVq7#~-+=jAp3D8Gv`Tb?!k18=B;'
        b'@}3x7G{wd-6|P)$W7wuX0pF#x;V*oD_wxPigE@*8SAVT}GS$aDeTsYLJh!Qb+Z^n>{GWu+@~r<P54cPYLI>5WEv~CTgVf%-&LG^7'
        b'I{U6QU#fdB*pR`J#{&#Kr{*?ag(qa-HtTiW$~mGkuF<}anNAtFC$p4;utH_;k{I#ii8GH&@FrEfpEdY_e`ud7ChzpAz=jy=*$|+R'
        b'zQP(r6w>1T!$C+P|HcuJLYWv+Xj%|b$bAK*ke@)yEt@f(&}RIp&t{A#v}fG)@Pr;6i6^vk9L5vkcs!wd`a^g^FOD0=6Pnq76L><?'
        b'uD}!8JOWS1vEr8Sgyx4W=Umsu$(e91oE-Zwp3vr-!4q=*2k?ZZ`5Upq48sYz9T-k%^9VR0{~cjIZu9s;p9kF>p3taU<J0M%-U6PG'
        b'>)(ba<i>bHn|VAT_eeY;cL+~t^R@7VHeZD&v>991W*$#y^VN7l2Z!;5HeZG(wD~eTq0N`!32nY1o{;N$ctR8K_l22P<4ZKpyG1-9'
        b'*MA3|&@{*6SK$e{ZisC#0e@SYdG)uo<%Qo7PssJ3!xNhD9lx!0UH@aTE559CtP9fc?RY}h(i{G})QPu<C*=Ci;R#)D45yQB5l_hV'
        b'-;XCWVdS^9nIk^nOBj38ctR6zmiCeO1~>6-Z3s`O{rY%98lgRCx}am}*TufMo^LvR+jqbda{Zg|gm^R||I63;CjPOj?H2A`jwj^2'
        b'CZ3RE6B;J_np9jtHQ&w+@r17H@4p%NpTbj&CscabxAC{CAD;%tayz=5)BLW5t45M>Yi!OU@tWqpj3qQ-1eQ?d2rQw54{r@i=!SB*'
        b'7M9S>>h=Q4__vGSW4wLqJ7NjB{=2b+{EuEE-rgLRki&JW@%HiS$J=2nq3g!mU*95@kn7)!CFD=LE|$=B<88+XETN%jOT}D0g2^|@'
        b'+L6H)dPg@AZof;cE#E%ypN_RxVF}$s;%xugSVGq`%+pP`h9%_sZ@?1Tt>UqSri8GBreZ9i(WC*7?V4CZSC1`-C6ut?*06+JH-Yu?'
        b'ow0<b894VameA>#AuJ(t5KG8yH1SwMzfkdu7;aif%_OhofN|DzT`ZyN`rn@qVhL^gH~U}5`kV8=4qMRs{(Q@s{B1*66AtV5G1vM2'
        b'aD=Ysx5_JS5l84&eed^(BXr&PQF4noLau)sju3l29HHy`-+OKiN67VW!x4%Z#1Z1Nqi?|xnt<_QGOvLnlrxAUbo8cigt9RHitCnf'
        b'gkHn8S<c%gzvgv49HAG3C_-SH)x2%;V{tq>G>-3tA>{g=F@&zm&(vGQ5OUob{?7M_A#}Yll(V;pA>{h+#Soe>0z+t|S)NwhB8HIb'
        b'zZFAhiXnIEjWLAW=G<vFfg$9^7(xR15QdO{>aAf2?U#ixgz|<lgbd$;A(YMgdW<0?!WcpY42Ce^L4^JueRSy<4CrIK6g>h#NHte^'
        b'uh7ML>1ba#a=l2n-L$lB_fuP?y~XtA%Dae-Vb$RY#cs8khYvDkbRQN$0`lWA{7W$}EwYCb#nD2%%Iw{DJo@O|U>AQ-;)A}5FVGE@'
        b'yGY}o1NgiBn}-W>gy4eQLAapDdAK0=77@>W?I2!|dk`<k&Eo~RuY(sfZ5S`eJ%|_N9)TA$?fQ5@$HIs4g5od33!+Bxa6vI+c(|aC'
        b'#~$1>3>MTh1Qt}T8w3kFKIw*FLBIMiY|J27P*dCGSV2ue9GSF%qC(v@u!5!yVg*gR6|5k>(cdQ|4HWgKUJEN|<}F|a1=}i*8z{<7'
        b'`j@eSnnqv+CEPxQ6{NlqR?zO~8)F6WZzrP%iVlsv3@gZeD_B8IBd~%J6hl}+(Ko^hs*C<Mte~Kb6GjabNfcLN1-Y|?ixoQV3I2c='
        b'w<^P(2c#P;PwFiAb?lkP!l2ap34RL8qijeX{&ES(W0Z~`Xm%#(xaMP}j@xSBo;A&xQ<A6So-|mVRlbGMg33Td#_sKkKL^2r>Q_JF'
        b'km5Ctk#Iq((9khlP_vMS3n~eR*7<k^g9deU{fX?D8$FB`^y_P&1@W{UZbk#jn6I&4xCU0x{0j&Tq6P8A_cvd<q%6F|uOX?qCwpDA'
        b'0H<)4C;Y-I#+>laOG?SWHQwX@Vl@9+UXNd@cO)3V=QRN%)MG;MLb*=?FB~-9^8-^T9$<*tc7bZX!2jg&h0b0uesTf(S9cI!NK6{7'
        b'1CA|2_(B#motQ5xvyis?a9{5dXJr>SyiqIR%S%J&%8_<CwdTD#h!(Sr_P8--%M`mM%PtS2!|k*4osYRJiFQkpb6c5Zs@;-e_gG`*'
        b'`QDgkx2WxwgyoiLkrp=65^tL~nm+?@$|-K@d2U*#$9h;8vls7OyEIF(=@SGu+R2!`3F&`ZbKYZkN-Z<a6jzhtAvho(Hz`eMn}Qn&'
        b'Vj6j$RoW(oe)7NFN}F!P?@kZG+v*VVq_9KhFM0yBSd&HDPK>Tq+et**Stk=Z<CJ@E^b0FG-W#odj<vmq+u7oVz%R5N!`B;*cf2(k'
        b'e!Rv1knkG@@xC_CXs6izE}<4D@om^5Mu+yfo$enzqukaox=Y{`pAgxTvOc2@3wxiY$L{MH-6f>({xuTHS4hOPa5`o1)J`Xd&+@bN'
        b'EBUrQ6X6s3%Ktgk-eaRbqeATkPy6HdHu7g=7Rk|6B2Bm@Z_TMKBDD~y=OFk?3upy9;VJ&iXB+Ts^jcAJ`gCG}fOgIjl?frCY1?!@'
        b'94#QN0jB6T1F3&3-Xtjl=8PL3&!3L?O7SKk{2m|w;FtN;+!SHHlBDvHfkbA{pG|qpkJc3{aI7yQiRB(f-9zSBN6%hAy6DF!=X})c'
        b'n$gRiOg|w$9EQ)|tdV__W0UZTCTrz__iSG%@bSH~FXYgYjpSBInuLz+^W*arrwNxvfPd)o|0WiGh|By3gWpT{`G1LTl$H5gtG54W'
        b'Q@^m`u9>@<ge|i**?I5Irf*~0wRL~e9%*AepFXzXzO&q#{>nSj&dTZ<?Ch`XCup~u-C<`nzP9Zt$)&$cugoUsh?K=kwx&ti>EL<5'
        b'Yx>LhvlveVDkRL=^i*{wk$l@$QJV1mm;5x^GKw|fcR-}c@K{}GX_`pCsk?yK^4tcAG}B3Bi76pMMGb$WcTin{qS1e&tEs(#sll^h'
        b'2hV40{%as~&L+syisgJ*a6;HcCY%{@fA#SF=8p#NgZ%Coot!hB*eIZDW{I)%lG;`+4?`Qtx+<n<*FfsK)j{cv4oPo!^|18TjpL=~'
        b'$ivdJd;V+%={c(vq|tz-7b_aCHvKT&yDqBZ@hDI_(R7)umKP2;OZu+N`)E|hFQN{MY;H_gYx<zL)&veqXjMpLqNNdd-@~`btT-sM'
        b'2{ZGXgl9R;w7j!i-P>CBS6E^vXwRP>+pyqldi$uL%%0(8CIy)_+u4K>GCM(sWF`&DtbG(OGh<L@IYF7NIlq+*$}H^qGCNCT-Nwr-'
        b'>Kxrn{U%WK%-`sBAiFDMR(^JbY~;hTIXzNl5ySV(Pmj32NqIu#6zjXcv?pcqr%MmoY!1@vzuYL;GRN)-<nNa1JhfTmnhX39?2u;C'
        b'(bzd5-cNgXDU%7djqx<Ba~-tBKHwx8#xFcJois)EbDc_)x}PN^oKFcq5iw&GD&5o~Qnra~ZAu)kyw599xZdOG*dd<I?NG`I6soXk'
        b'sKTAwqa__aTx@4uhugX48&9j&TFW>@$hK9vV|Szg(<Bk(Af7mzOIbrC5uq4jt5eoLqXb{tPIlOo)vcQPdiX1WrWqoJ!XLdb9qj4T'
        b'$kVMzjAas2#}sWLJ2|3-Xr>5<1nri=)k1<twZqrtBEl5YUrO{F`ESagq>n>A9-_RAFiHCLZ2u5XmS3MIO9y$fU}%W<9cvURYelvP'
        b'lnw>(q+*CC`CQoup3EMqkanyEbu74wClv5x9`J-2;tAG4S{&pEK9@I!tzNn28`k|&=K)*nC%aM%$Mz!o0Xt1vT~FaN|GfFi=bdZ{'
        b'<25QhYBqKWiq<2$cUMZB?QSKK>aEs}6ld)6o%|`$R%<=K?bSr~qdI(&p0&vyI%^twu|o%oyU6O~$;YAzE=|dfXDY;#ZD~pfn~)B9'
        b'Q<X@J2dR;$>+itVb+~Pav1+YV&EN%#inC(eG?IiEi{%-stmlIAr0I?bkYz%BEc_J*CF+kvT|~k`<nbsHV`Pabw|}|^iwz`{P(Xls'
        b';2#MeBajt-uNagm7N3y_Zcq*i^z<1Nlrr>N7nG-MAgZ1U^&8vqw<z52K-5sb;90te=6#4xJ=Z4dZe!?JPjB~b8E$L(ux1SNWyw~u'
        b'I%PC>HfqyZ#C;M4gJ-QB>K6l6wYE;pgz^Oae%ACyyaT^WP@Xt+Hnas{n@=XPWX;o%?NpR0rQa!r$%)hFLDtsCJk}K;dpSWA6$lxm'
        b'LN#v{?G|u7Q6^o#mKeVZ#U!l#yyG`fsnIo(ozJtjx1zw_p$P}xE3WtS$AL@u1HRY%BoRj-W&cIJdXV>cS1Il{p%B^jN2N)e;zV(5'
        b'!jr`NOInE2PY@gWTV&<%uQs9T^Hg=Rg!^?=kY4Reco1p}kwuixL$+6<fFVJWX-SacqIr>^<P5=++bD}82$oc>LUQiuC|>h{Zj1=x'
        b'_yG{fJsAa~8@zoN)C)bIg!JBiK@OSVAOr-dOo`yuMGczHj8zOiE2n(v=XMWgUxK*CD93m_UR?e$T)xOn0r_^m>L((wdK-V44SWGg'
        b'qE9dWyyIs)*V?5v2hTJ~KmKkZVbSN@15pBkuzS>?3(z)$z&@4G!lRgj+%KX)mw-gj<W*=I_ehj60&(|6VZA{>cdCygfQZwpad%se'
        b'gL($9vYX33Pfe<kaQ8;>VTAi}6toc1BMaggicWthu$AHVFJ~txz^9EUDEw%W%jKDfsfsFJ@Oj4%hJ=4FKaQAwJ=Z^&+d;dw+$cR;'
        b's#mk7Muxppv~ONiotgz1YNjYWY$-SetrOn|E7rcnYF>{xEIc8y&B0Ci%|PcpQ6*}q+-o?UNjUC7^qr<V($A?G&skO*5S@bu0~Kl<'
        b'=PPui@ot1a=tTOD+1}gz(df;l1r3d9-pNrNlcS&z^#kOc5Y;g;3W`!wz+psnOo*z8B&jUqO^)i&MuEtYR}<BdgiAXzkT*W6BN3N&'
        b'XpxtS>R@nbM;h`9qB_VZ<9PIDqui^C>QF@;8!PcfM|H$TQHjuhowM8ec>0us)yZRz%|)&k_ctVs3mTuT8)q5K3y6eN0wS?j8r4BZ'
        b'@n_F_KUZ{orbvtoOH|7~wHp<P`%*DWveT^X5>Ya=FCyw_M3ik5<_bRZ-Fr#VF`&TTg6#{7IvN&b6XPfQE+~$Eqp*p1-hsdKeyQmA'
        b'hr&o8?-z=WFBK!tb?^8<Vf#eE{)y4<Wj-V6F}sooI-HKCB|B@Ms&leC-j&*pE8a;G?P?$En1(>POmU!eDf*rLpycp~kLpw=$me$o'
        b'_E~1vR=j%PJ*GJFW_nMrZO0RgHBHv@q8(IC+IvndI}`c!PEGpx7wzgE+vM6&*7dTqQTUnqoKtq};XwD3-8e36^nRTxwe3+@KWFgY'
        b'Cs^N$cJ_ET8jHXB-l3LuysQ9n(_ezWEZf`7e?tfjY;vRCZ2Wx{I#(-`_U>%yE?P6-seLKEMe%-S-JPQP9tB2;ZAuFFOL2Lrx_aB!'
        b'(DV*<l)C59Iv>HcDpHa_DcKa3&*9jVZbahHRF}ktd{vH1!NxP%3Cv`lXcn0!m@2fjE3}4gumn>^e|}4tRxNSd1$A>;6`JR=a@NCN'
        b'7AoaOir@)|fO}E_W%K3uAd%S{6sClJ|D7o3Sw*3`FeBK=%sl?Qd!fy(n4C0TDVNwDhKtDA4GP14yGhiKGE$H_1?O+Jr{UJ?wd&eX'
        b'O|2ouR;SPlz#_+4?Mw{;ZmLw!&ln_Hl)|WESYb&ig0NBu<F{row)+*P`}?hGtI6EYJ*FrX^_!OWFCz;}<uOp+L=-|{JzvE{6@s{%'
        b'Jp%CPN+H3S6?J(88*fb}a6X_;8T92glvAjfU8vA5WVQ-`ROO_(v*#$-JZ3GKpFme8gwvv8p9!bS$daSr^a>NzuX&oJW)R+misp2}'
        b'KMn^=TbZIVDamG0RJP3bc{Y_+r(0{gA(WMRI<R)sdMg`qJRTvP;F;U)h(L6LEn88&=?-tIf*Y>@_X#aJCK36*Q6@qEu`#o_F$(Z-'
        b'l#W2hk^?3=j=%mp2xMcSQZzg{_Hm(itfGswB`SjM*QkL(*?yp?ZjxXJN2XA5_{KB^I5Dl$T67kzxxhNL#}=XTCk52s1IT3&G{+IP'
        b'@sUv3J4pf2+~c&uY@Cj<?s;sdbwy)(Z>GNXvDc%IeGEQB0mfsKhWa`-I+sgUq~w|M*xrQ*#TYSf5~D~XMF8LZLV|r%B&}N3%=R9~'
        b'kya2Bv^?tVfHziAnS#%6=2VJ&^{8Wuzu-QT^Jz^A^)=YzXhptHbY{%Q#@__EGx8jz0;h;_1%qPn1%tJaWlBu(_&P@hex?L5DbNQO'
        b'p<vW0+Tis?xi%7)LFxUhwlE_H6%cwglT2hlbkvq;Wibx?trN1mC)YS4I70ED(`4w^qZGZqpF1SiSEhsPIlsKjZ)4-x+6vn@@??T0'
        b'^IH_Q3vxO#zlAO!QYyIL$y4&C!~L8u<tOd3+B|^}5)I_tEoZb6#KqL)2yz7ammr4_*}CMww>Uxs(S<Rj)W0onA$F>X+#I4nCLjcL'
        b'dCYXqlf!vW$ukJjlgD~Ll+PiEwmi(>ek6?1$Cc!Q4Spbp>-!<v8~VB9auio$5~bw4FUR9nN=#+_rTRkdm>lvKxJC;LVFau!1sVH8'
        b'Kaa?VuYW&$4P9t+3r)iQ(x^fvPm-I1T8O$rCfKu9P=bgU$S@e-4q1rUetldaWJO6toq;ha`t|Y>u1gNA2AV)d++I0|2{_5^kvnr3'
        b'vanVyClR+x&L9a=9<sbDueF;d^&?Zi)?An?M*0K^qn1E>i-@{J24u@b#v~JZSqvshQNl1W(z)D1`Lekzh_(0boJzTALO-`o4(?nF'
        b'0+r=LY9s@~V&;Hl%$MsEQcO%CYmwZ~i`>a<S0r<8d9_bKQ3z=oXK{_dScHX5NZ7k$kPv*1o|`4--|KKLC>fq!F9&PG-;rt>#{$<`'
        b'VGJT3ScS%L>+#qaK?<<KI1}qn`cLFES-oxg>}hgqb$TWN69=$&leHt;Y1OQ>WXg3tHYCuOF6&rxei@&}CljSkM(r7Ga<W=A@1@y}'
        b'WATV(OL>nJ13oW(mOLXzn2QGh{yK{Q64IB-+4vZ63+WHaa~=et#^~7;{PO`h;;`fpOoQSJk+~n;TLOk}%I!~IC^rEY@5efke!pCv'
        b'BQVW@r-kVjIp`z0yFc{vKKbyqRu1LiXRsX;nNnIF14gTVwci#I(qB0t0PANW3)2IUb#|~PA&3a*0eOJrAmMCtS|_KQ#QkUF5isNa'
        b'4EqWw<PQYEH4n`PZ74Y>DJSQ%NZa{Hu(bT72mvAFPDBcFQL>!6581Nh`AI8gXUW%yt$7SMWZPu9oDgo0Oy?%aK^;L1)lc8XO_1kI'
        b';6(zyLDA2!F)*7$F>$$&a>fX93FCuUMqDz~kc4Vz<T**f8WO&SWKI8I4GGln{}|agIo`{WiF}-}`6!zG6?TrMsQ%fpa+hZugguri'
        b'oGq6luN&Wtl%woJaFY>~u<{h3KyUBgksQ-`C~)$3vJOV>dJ!GkyIWfKG_z}r5T`UqpPz1RSXuXUH@&`Lyr@P%MI$tul!IMCdrVx('
        b'Y$P|`jfsLL!IL5eEUb_rWAxU3TraOXwkbb392kWlHiSdGz7PplU@dw<NzPZ1C^80Y5sb1_*3Uvk77s2?fN+C6Q;zk7m#X{WrbCTv'
        b'E^uWq(-6Xp4IV+Gw1mQ;O#f!O{l(R_y>%N1YhE|jFRL4SQ}Lmk4<ca_jY!<f?4L!_Q(2UP^lqd$1kKBH2>1!?fCQe!$-D&ed^*kG'
        b'A<)}zeQ_l6l!t`8nenpa5$KqK5C{;A5PB5|2>ycbcuGU-qqd63WC8+G{Tq?o!bs3(F#qagDW1PTsHk@<o5Wzp+!K)|uz0ec>x!)3'
        b'2ZQIYUyFpqz(f`XFIZC{w>uI+k`TOpb;R|{!`G}R1scSo0S}i@Qk^VfVHzt&+;frjFGRxJqB>bz9~D{GXmwc-w$%*q3Rv9`#I`}b'
        b'&Jn0Bb2)G1Vc|)mtWcdqF1Hk^EhcG#+F~|a=9F1xuj!$MnpBCQ_tK11y<wX^mosxFJ7-qKA5qI{SE?=dvJXP?-A#+?$3$ZJmL!?N'
        b'`#1HVKCTESfoVx3A`hMNcupqBVm?o~LtsFvxy3u)wR3Y^a5G63)0C1-i(pRG$IU(2Aaiex3rBJ>QdNO3#)}gl3L`g?rrY}Q);+WR'
        b'z{RT8Kb~AETm3UZJ~T8#-N%`V+mD~jlbu{3JLNfNe&b@y=LX9>`tg#_OY^!<S>~^eFj$ID=F19mAlex`=L+jLhA#*+N>R?jNb?&3'
        b'Pz#nxK{;3>a^^(hpF{~Lh+z>rd3UhV3@6y*nW*1)QQ%u#mjCLp{HXkSlv5N5u@S2pks{A2!D-w3136$|L<u%P+-!-9`>!7EN4Rm}'
        b'Ata00u1uHiFni9$%stsAYir&u>Env&l_)~L)7nv+hqG>{*SfyDbZ&Qz1c~%kQ-@!I-Zx5%VPGfc0{cqtn<p~O<FKnovoFfP&oJl#'
        b'S_E@rM<Sv~bS4VFnZ-D<3A9v|*Dmez1WtJoJr1%RXL#?PEn@2v-8JDGN8uTebtAr%sP@iiY8O|H|6sfF&P1gsF;VFVN78B+klBPk'
        b'39o4s*VQeAELd9I31m2BF?(y*<9qiui7OJ~kG9H85&hs(x72n~N7`9n4sfHq2?hB8qXrJxo|1uwMKH~WS$ryzHnfM+crm*V8r&m`'
        b'IkBf}w^Z7;)5)IVOn+@VyI~QA5O0F{ih-L?k1_1OI8UMc<3Jxb2lVK8J_tMJb5(KSJ?<))sr7O5PCg?$#TB{R+kVv|=@O!tL+xUD'
        b'9s*B<7e!8iS{;`i{~%6^G9r+w4V+Bp?=JRn<{j;Sao5YIV=c-n-m%NLDuAR-nA6F;q9&1L{tL>^0la}k&D{%;qPw%(ZYgPAk8B5J'
        b'ke{0}`&q#QC#xYJDp`dxxuY`R84lEuDNK{qT4VKj&LPh2dXqqrhfY2s({d#-ZL3$WuRv;dGT5m*IV`w<t#(^&R`sGO%NkhkTv_R>'
        b'Ea;dZrz8QNKlESF(b90}fsglC0Er-gl%J)HPa>ri&@lIs4DtziKAti{T6JvurM19Y?@k#d!LU<pd*djSAw}vQ0tQ~@7lOTL(nw9q'
        b'DKNbhPHs?0t5nWSZ=#cxvLzN^8BIFA3Y_9*pP3eZ=63T7zxM0-cZ{<WVG2JDmF+VDdr}gYl54{q9D-~6K2u5(WK7Z~h)Bl{4s3`D'
        b'x=6nce<NNd^X)S&St6%k<_XX7d@C*dSlIw{1O=IXc`oRQf{p~wgy&gMz7xtn0OeJ<yr%WjP<w>`cBl*YGbln@rR5|L!sCocE0f5L'
        b'M4A8MnbD_~hU1h80WBFMA*~3NG4N#!gu3VAnZ#2N(SYVYpgC=j<}=Bk#t{lR5!JgAf{Z+uaDbOr_d_@e{^YwS^=y1_-NyDQQ$JJ2'
        b'yL!lHz{lbRU7K5(6o%J|=E_)*z99wjLT<JUPb9cP&V(-*T_N{F8H(!<UC$c6em|a@A%i%eB?=*2=$S%(pDZVo;i$l-00A5))5e#8'
        b'L&QQB;!<E&a-7rhu?L*JnnSiXnEGtlAYGGjp?Y`GbV|LSu-e(8ck$|4^AAy%#QQn}j<rHTQj5`U!uuP>*2Cb}E(BGM&sa#2Rkz-G'
        b'tP_$a9PM!I%|YqA7|7~i=9?ZT)5~%41Q9iTE5q<h)X*XH22&M=OGzIqs~>~8z|Kj*<)dW~3-#%R!3!q0FnzQPP3R9@M~%3akGPHu'
        b'U8mnB!x>>tVeo=kSePCm!}EaPwRFUF_=xM58K{etIH5q=ep5Q;7%M2$iwY4aLk>~hIv3o190BPd0olAZBLyZt@*Gm%*{|Q$Z~Fyi'
        b'2h4Izh5h{W1*LCd<OGSR7&;y=%iNI;z8$7#w1SO?l=u)t0Q~YI3MQ0_nK`vgrfj#&yO`0(G0<!>XIp~X!~D}hq7&nRxf7m4aU~4Q'
        b'jN%9~I8!W*EG%UT5z&ulT&0CDA21Ri10pUcW`0d%7Bl+@qs?QM3i6xpnq9`^C)`&2^jLZ{En<tGnk7<35r@eW0=&#?`!Vj*_#Eib'
        b'51I5IGTW7;|0TrD#Mh1vH2XJD_YVBGnKb63eZOXo{+i+I&BpciX_%uQj<UTn3a+=ukj7>Nw$CpgCnTfUFEe;y3u-#Xq1m0#kRGp)'
        b'*>d@s(ah1lQFNG1&;N>Ij^;D7BnzZ`+u2NLHI08cdwdkXrZrXS(4c)1=I9%vmU{@Bj;|NS9Njl+s9x%2^?HZujX|@Yg6{M7{d3gO'
        b'U887?Esn4J^{AsS4_9vH@0}lYw0)E<X1F2KE3ECc!Itns3BSts@u&_fLr=E7G}H%vXZ!UKS6zb*v=Xn$Y)|k_uVjv{<i}{M<$piK'
        b'9DRtf1#k<YHOR;L`#)ul{*<wOGvYq4XZs#tjy}NH{yyUV!~Fe9=4d5j`)tJh<^28onWOhJw!h;0PNGp}J;2tz$J!p?pWVkCy^q-_'
        b'*~)XOhG>%6%K7^x%+V6Y_NNhT@%pi^h&fus*#0=;{(SzvnK^1^Y=0PWe-3~D9_HvhjO`%4&#xNa!-S~7Jh8U0b+56uef(44n9Ycv'
        b'R)j_I9LMb2JIGc)0~3KM%<QSmkt*5hywxiYguOdD$aTJE$EXmWTZEnQgspwB-mzB^w|*4AOgmK++|V#72W=!d$0)6fnHoO$PBRB_'
        b'_E9k3PETaA)$E<2v#M-sM_KuoGyFU7QT4wV1>Ta5tZpUMp258xoQmP!g&$o$DmjPU$XIu+>-?Q9cJYCnU9BX=A>};jR=WE|k!|Uy'
        b'WB(M^GYlj!)(y;_CV4or)|Fao*!l-XS!;6YU@9PCm^PxWm+3yh9?Xd&ge)QHW)Zjw{FmS-eL2FUoFjJT|FU=YaZy}{{`hAfSeD%p'
        b'_W_Y7o7q)xLG4`@6Lzh+*(HR4CcS7PQJc14f+05TwZ^7NN}8P|fkClFNb4>!?JfxsXlM}gfEsQVOsJa00Gh|Ew<MLss7Z*iYEYQp'
        b'IkUU?(DZ)q{e8cGe%>!}cg~!dIdkUBnRDi8{jFS^t2&VhU!bdDm$`XY4Qr{q<gT;UdugemV>)+s`Z#*wa%=JQn%xUX7nET%(seNY'
        b'i|MpU*=p1<#hK&(WI5q}%HrwL!OJU4ESwhj*XcET;=-5cs;vwY$eX^SHp}#1(<9v$eHMRoIyuhN%x1l^dV1ySQ>n>9W@_3vopi|D'
        b'HBT-Qn*EbC?M9PjdiI>@WGYgZS!8n+-|yEl&nM}!4^6KZWLBS!<V>xMbRHjQ-_iQLtp}#_$<uS&W|&egPohpW^-Y&v>udVq6`?Vv'
        b'*XfW>N1EA8e=L)|d%9<Ta(JfoUd~5PjhbGaE_IS=JsiGtOt)o;fng0Da{fd-DL%JrjvmzMx%3z&afxh1!>GOyGmP?4lXNSOk}20P'
        b'3zU&EK(C=3i@$uoPx$)R=(u>r{XQM?@(D3oW_;60PFv*UKk3?O`9j9iH)yu7A3Zg_A&VIqcJF`xtA^=p>f9S;tadzfaBnE}l?Cy2'
        b'MI=3=$xN-Lnx2f@zcTf;cW-0Z)ZpIW?v>ps+P%9|YLXSc!di{Dm0p#VmNhz`@nkWH_LyNZ`^xEEmT4ykzWUX4Hu=59GB$2}?;c+$'
        b'`IY%GY+M0p40%_++eRAFrybpeyEUW_&~QL3`HX3>D1Dmd{npVN8G6z5-Bk>Ir<R`at&F}?t71A?U(Xt5^aeS-d>YA<@=3AFucq0x'
        b'AiSP*pJo$s4KqD*W_~m2Cninf12o@QgFmmz>D)+jl*IFx)HYL`*(|I1eSG&!l5>~Dx+O)k=@o>obQzgp`b9DEQ8Ly2iXvlXPUM|w'
        b'E~aa?tl2Cp|3*w~VpyT}dbXk{rgp~V`<S|ot%jEKV(8?#TUbFcpcGcp`>8MA|1ctF_#0@|K^8$*@e`4^(LwtCl-ME9P{fe0E%RwW'
        b'%e+XvG4JYaIXWqpUlb$vO{GWjrR8(++I(T@YNY-1eEGq*<jbwUpGMZ7tYXV0(c@Pg&1yA&uCi#3#aKK8N>b=Z`nPDLd&qdE&n#;&'
        b'=}Gk93!HD+0awd6;uei}*?!jx2k(z7O8)(WGP6myXl?0+AZujTuD_w`F@?jys;do5<;SdgZsX0YA=5!`;%qkQcKklMYc8FUr%dTv'
        b'HhNYRT;645i)7N{V5`|<(pfb0;9=P?5&O9+e3#1Qw2=1RI~+MGkOX$fTSmpuhplFkWX*umvPOzGRWBztla*r<4>I;8%?GWciA;y0'
        b'|02nEUKKxeuN^-e9~g{pP%9HxG0hgH{H2qTos5jjek<N|Al{=;z96(JTDndy&>S6a_N)1`)1+-2N*Ns$>06IyGv&KZmT1K0HB6f!'
        b'x=+3qzw@<tk94P=Cr_FF{K*Etj8*$<tH@BaobRFwu5+}iTUt*>!aC%muZQ>RfSgTc)y1_{ZuiEY%1ho?S!=6G9#)miiD?dSJ+k(I'
        b'xvbDuR@CzHanrN$m)bqDRGTUHwZbm{$b2?sZ$}J2K$F=wB<tEY(xGa3^Z3zq&2(JXkWAO^=C{R5D^ZtXYK)&XR{SQ-&(i0)^nJ${'
        b'XjG)cnFI2IZ^Upqw_MII(+8|Y&TpatZPERNe~b=B%IKq4eE;PY-#1?Vp8c!%LV4vy>$6;V%8@7Zo1XP9()xUhN{V8-vyN(q9*pnZ'
        b'7$4Xe-_>m5e?jB;vRVxfTqJu%L)MukLZ?qRCg|zVIx@8NC-Ksmf>t$~kRJa@hk{>6C#k!aZ0gO^q@=UTYO*q9*@beuVe_4p7mHgs'
        b'{zuZntMr?muzR&R4(}zSxA17(&=2B!?~V_wAj@9Om(VDVLe@y~^G<1|yU0u*qBHGKmVZsQ6sst>5ZOQNWTo=<C3GksR#X`ITWNIR'
        b'=E~2=p_q;7P_D}H+@s`grlGBdyHavSum7~`MUmc<xtNBH{a!E3T<7!q^i2X;v5G?S->SmOztfME9ZLTC_;5wS-$fTr@-F>rG16@K'
        b'$7Ne0%l;s`?AdhLbE3<>A^p42WzYJSWv{WMk^h%hq)AI(UNMU-enxchxzWX+3NN124UT0im$3>q<#q+Pq^fvPm31NK(3k9+Z<DJl'
        b'^!^+jyU==X<Bh5c!_nt^Rq<W^`Mg%Djpnq;oH^V|{poe)06A!`)UT4QO-${bm`0+|_gKnktkN9rhnmEL6N27TMz&s&DKXz%s7!p$'
        b'EST(uib6J)6x7_`%lm5>i?Z_K<~4M}6EuzXgbo#b?Woz_kecIY;74hoMYer;<{Z1MNY2VLZ(e*R^A6J|(<+u_RykDLuV1y0R8qH)'
        b'z!j#CrU}c6VltmxrM4`y%S|6n%bZOn$mxGa?0t9I;>~Od{~?{-W17U(vjTsaR(X+siw^T|OtV-@^0a}0X^&Xi<_6xJmKocs$;=)7'
        b'&(R+F(j6^wS?kO+Ey+}K)|pN-N58B)vmlm#by}-EwY|+wny~y{I-}6qj#&OEOTMk?)3NINvuj-yE;i-)5*e$Z*X^y|M*kzalJm;C'
        b'J4lUjP_&rX#K+{?3~nub;zeHi?=e<OBezyp^2ynfT}HQsbIz{fxQ%ri*4rDc){P~1d^z;|wBF~Z1)e6E{R;mKU1o(|bxiF20|`iL'
        b'COx6%X;P~tF>Ctfz7DqXVqckxZ=hj9_WrU8b;-NxB6Xl~n&7(s-b`g}Lff4`RSMayE6HlC>|ps?8Z+@zRlrR%=Lu;#x$CiMbVq%n'
        b')!uwi)?A^W1@LjHmg-NSi#SlmKO)5}*k9&;Ru@|B&fy#dH)_bCg8zjy!v`6%eOva46(+$|n4Kyt%`YNZbGxelRq<hc!CysEQh!Tx'
        b't^cI>u<7>LpT-vKAv>pYBS%V!U6xoyOD<ncW7L(CUHS>>+d{G{|A(0P>U$lr>92_Wcatd|lanIZe};TB2V(liq)&N4Nw_}jAtUA6'
        b'm+n_+UkJAALVMmfX7m`-)bH6<i9b})9WrB}oXuK$>}x@5UusbcNfyJHS6^~R%%)mD{T&6m*)2))71nSGs7MM2q+J!zU`aORO|!P^'
        b'IiJqoM#Gyck`MgkgI}@of=|SbX~)#npNeb>`Obdl+-)*8ev`ESHjs!H;zr!c%3lv!^dn#DxG(6mpT&{?PQ+DqabM`jCUF0T2G-I*'
        b'A=zY+79-GJ010SIt{x4qCw&e;o>;E3#N@rHu8{NB(M?c!k>s&X+LsK0bK0>6z5iLAkeKDO-y+o?YmIg?6T4tK#d0}1e-53cgVrh*'
        b'A^R3KyoQ+q&xVho9m?18_({4IXsgTYcW2S4cD3n0ub5g*r&edb7oA#N{iVq8U(u;lXCiek*)5Wu(OA7z&ekfwkGtgHY8y|VU^jOt'
        b'M|a5vG}05?v2==|FWJalucUSMIa|{-jqJ>)r84ui*c^~Y+HUDxvPe53z}U)Eq~^2v8HX&rLw2L4F2T9z9@j@KJCmfQP+7F>c2b+L'
        b'>Sxs4wyFwQO>%7R^Gb`drs3aQ@3S<Am8bh$LnOBImf$mT=eDYP=f==k*D&i`5xiYqd~21ncw=G<<6TzclgHjKH~odZZ#KQ_Xy_o@'
        b'dyoyh#di5u@-Insfm~)b$QlAn)>^Vl-`6HL{RhjcyfUAQjoT8()l_Xu`jz0yZGEU)>Cwu}sWNwqX_Hxd#@zRvv47dMuANIa?J(cv'
        b'4(690X#70xSX@7SfFsqy)#qpOth|116<5D8^;qcsF(K&QR#o>%>Tf<xO#NKVP80Z=7vE*4oha+lG83|q7_#M3*Q!1u4Yv<1bD#ax'
        b'eK<%Cf(zo7=2!QK;dTPsI=5Rt^bFhk4BHim3HaFXzBcI5n|$mhvsW${=v`ADS8g{u^n13qkwjA!{9R;7mEDv>H@HITFG^26ljexh'
        b'>343eJd^RJhBYuVoMd-2_laD-&Kqm0VOa&2smpCvYt5B{+svh!U(5SdZGG)7ca>>V^?<xX$!cp&K0W_yngqerMSsGPYc3>>das_d'
        b'1dGi#XZd`w+=?KnTDN>MLqW@;5S!)umBnq@H4w+mHg%99la)bd@_~&1DV<H1T$)K9^S(?l4W{3mCDhV6c=f6;MX8SHP_%q0R$j<>'
        b'lT_C<#X>+UFbVY2->Tz(C?!S3%G+DpR6^`(GPP9hwyt7Xbx&Ng|Hwm|^!wxHZdVVIDr2)HY1UY(u-RuSX8SLR<d|E34>NcVQ+i6l'
        b'f1h3UefFd8v+jqiCrA0)+52Um+Fd&rumiG=nDC2O(<el)>-}XX%35VRW*+5lAw_Z1CRXcywXxH^aYy2u#3cEUi|uuhg7#>@#q!BC'
        b'Z5=8;jdioe=250iMry!{8LX!C(Z-r>(}o;u?+qmGuT*Er&bProdEcwrq3hY+Y!X&U);@LZ{WAtXG3q$l|F0ki=h%mp<lBZd%=&v6'
        b'_bG)XW^NKYl*RUDkqQ3L|FOteW@ycsGmhF!44WCVK00arC&v3pQ+c^xocr=;Lmb=t9TNY!{&%Hz94il`u{&q619Co&CO39nJlV(P'
        b'qrT(p_h@JNkH=HZi<4>^-e>oum!4#`qklNgE-L>q`Ib(;X-0oUzO_7aoJ~om-$u6|XR}&<NWPVmZ%an+remKz&aN(}-_psqbuB-j'
        b'W1Eh%kEYXabU~ZSSJScNThr(&I)(Q*+n!Fpjcz+0?aOl;NyQQPO1txnc0j@ZmsU!vszXuNSN`<z)Ett=#t|Af{g211FNW(~_BK}A'
        b'+^6RMQ$y=TZ>^lQc=FU~mRdvP`JfRkKcc<j`Jkg({@4}6qx8%GJr6J`O8Zdud)iPQtD*H7DU@G-$}PEvRDeqUFr9{WGW=2}<MhMM'
        b'+N#qQKBQf8uv_g-5-huA+E9<CgLK6_W%6>viIVn<PIFLon$(lB>QmBoFukcY%b8FfUrA@i_tF1NKh<t;G9A=pq$HT$&}3xAoAzik'
        b'7O73Wnzc*hrtYbG64Nh<Tjyv^U0S~{xT7m(>q}a)<#xWL^*6gn({hK+NV-qGo!SNJ9kw)*Ou0L=YS!3@N8j0J-Be2o$N}|cb2X_l'
        b'=!K>|yGg+N+F+OU)mbvKr<m!Hf##)_&Eox9>0onoHSg21$qj`}`B{<wgT~z+^aPZCOJgM8NQ;_hv^#&N^|uB`r=K7l!TNCDr9m6%'
        b')JOX0ztv{f(^g!o+_XjOf9_?e$Ihy)W}UM^&%N}rKa=Zh;MkP<O;zstjW=pT2lywoZjZH7;M`4Bbw#Fs*JS@Je4KH)wUL(i_vk{%'
        b'?&02|%qE#h4$@U_megI+5s$x~jvYCr82Mb;`wQ*dKg>F&=z5O1Z9IMbC)-bc^dRXmX?H%T?eqVfe~`xfTt4(uEs1cqrvIE6Ef;K('
        b'=Vpd~K+DDnYC#>cODA<&)pJwWX0<Yu(tI-`SV%YN8Fj%#c-yWadlbKh&X0VSMLtWVO}tubkqhLo7a|oCLmK2{%1gA~%U-1o_v~V&'
        b'Xv^pvmPMw#Bl7ug^wYIOYf)O{p=NSmp43DNuSc#7ooJQwOK1%8Sx7(4W_d~8WVu6@H;2hnsuS;&kx9Oi_KkJCQz~}H=#cZ2!g;&0'
        b'*?%v;SSr{l&gMpb5&cRUNpyW&Hm%fp8KJS4Wob!6xFV(`kxkQ*Ccq6eVp~k;LlWUb8bRulFih_}?V5F@nJ%*}QNMNan5sv$cuC93'
        b'PkyS|uK6fkJCv^7nNG6(U4DkN%=YqGqoxEcJFC~E?U_c_)f8E09sRV&2*%F+dUq%|64Gx9b;#LS!H}NS^2y<`?2RjpY-;D5`eG@@'
        b'>QHA$Po~vhIS=wFYNYNb-znvRy!st6GtqQjV=GXTk>@nwNUHEGD~z4}`ci3j>q4}yrS-v>CcKUQK;ybT)vQ#8-XwXtJ-piV)%Kw^'
        b'{J2Ic^gXf;dHPY2^ua!)@49IW$C0bfiR@b>+fLBol9N)qx-OD!<QU*plESt`Da2)JR%IQ%(0o7B>}U8-XoMYxS!BAuNnabRY^qAh'
        b'Y>D$)N@~S6OF!M4yGVWco~Fh1X<~}(qjxn!?`n1qX!-(~{A<$uWlWtR{aulyWqo-43l59nXDm#6$a>K}Y6Ts^@6?b&-c7P%?bLel'
        b'Z_uwjvh=sb&_P<3!((EqFNjilJ!Ixd<%9Gb(W>ywr3NOg8^%S}5WP3JTeGZNvm|eeoHg9~GCg_kdRbHUie^b6JLA?@WNb{anT!2+'
        b'x~WU!>eOUe=Dwt~JeW8<ZDrN-*UJm8XA18z{aI7-;9$N!YffE(sa?a(aer)K>fX&reB|eTO-6>A&!h|g`O}(Vg}OnZ>`>3IW3`3P'
        b'`t-wP%x5NkMO^rKR@3m3X<q$jnuaCu4T_9MQdVUZt=^(}ZFlJkuB7FnMPXjTT5>WA&5Aj7HnU%mSz%VB*KM#=us4&2bY?}Gk(K8@'
        b'rC^N?FIlml^P1|vk##K-G%MxZcNCWllYgl{8F@v&Zf|g}e$5NX_sxqB@EZT0x;kIa_CIgxYzh|ph8qf5i$V2?biSzi^Kf2y4g3S7'
        b'nO5VA=YOhk=eYS_XmY!0HgTLXT8D<uX_J=873Z|KK0vP<2yrD3i_vqRbW`T*i;FipZ+2US;H{0Ru5yjdFQeV0dl}O`n$Qf>8akDO'
        b'o{VZ$Eb`JGOx)6(>a*drw2X`V4>Viv(nLEFnQ>0%MmEWGm!@P6V=AHHwUK9D>8a(f=|i>Y=f$1NGz0XVHD?)CJ=Yt<zd`eS#H(*='
        b'^u~o8se)=;jGSvNA7l6e4ZZyFEJ@*xMpA2Zhtsi}q(c=srt|-*A=Qo4yJPspng)L?`EDcMvuO%^YTl}0lcjIvUq;XC^EsriZ>?>N'
        b'rq7nIWTWR7Tk}}fla)fx(oUUkjy}7ak(YdKxhBJ)%rMKOunf<%wOwb~yn;(2!`k{uQC?mhIk(r)=V4P>P5qy${QixnKWupM@umhc'
        b'@QmhkN^{?O62_k1qTTVD&eK;)nh2fqxK}Ll`b=(%+)cM7n?w&4bUx8-7)?WT_}b4c^7)Uj@)}3}{Gx4kxoQrRR=X|9R^u?O?WXrQ'
        b'r^VGcRO~m~lCGOImX^FN>4vn-ZQie04{aKywQWnv*k=EcXa7g%3jfL)s?UiH{wKF3oh4H*Ce!KWf3~gruxI~!=L&n-JW>fU4gM##'
        b'd0%GFkQNL1E^JGBxyBLS;IH16l-%I2*_QNv|0tQoZ?+}HH28n38WmYv^+zIWE*Ocl!#<#oRFjS+V~}o*a-Y3?eUG)&eVt)UVU4yt'
        b'#*-&w74)Vk@|_0AJb5G+JY+ykM%nV@{THR<Pg-6$Z?;5_n_6$Zpi4EYE?u36<jATZe`>cm7~ZZ)o_r}|BjZSe%R`z9bnI08Zws>+'
        b'grw*^1Y@dDYYZ>nvO#!oDqMcf5+f+cNX6834>Fz6ELVEe%FFYk@mN7INcVuu<jc|NxJs|vtkarlOOmUtx|~PNa;8BcW7=mkzS;Gg'
        b'f@~V;bG%0Hli$`9V<uhMo0%)}Gt#z=mLG2yy^3M>%My#2kvLMquc$j{{>@GLu2;x##GETiS(}{UEo9{l2gYA1N^VtKTHBwMt^)MS'
        b'nT%D(Us<KjxIZT2k^dx9TM9FlU-!y#Hlrbq-IZ%#S$Y3AqQy({uKzs!G%(}<Wbs<$q-R5~8}%JNXD9X6{74>n`p%uRkl~nUp5(Cx'
        b'&wlY0`!#jj|7l;a*scz*JQG>>Yx2NjX3km69tC~4pO#U%vc_lh8a&T3q}Z&zpthJ>jbu&RW?N>nNu&>KZw&t|4V~8f9CKBj5S{lw'
        b'q|xy0<2?;Oa(lUlY7JUpQ**Ose{Pe?ZQV%cf8$tnWS_rw{ic=``Mh?$riSUyvPR1DwQ;YVmsidvWyHmK4W#++bJu$sBiDeu@@@sI'
        b'el>aae#84l)-d=&@J6-Y*4UvK^pS7%w#MMzptVWY>1nK=dJh8UnVl-IDQp~RglA=P+*3=<;WVf>HE-JG)pTo@3Y|WyPqVi5^JqF+'
        b'NxQzLX}Z_2MH8wO%&fuPP*v~V7%sSEe2A`Fu7R{<N&A;I^hdANdCVzZ!DF7`t_?1-d(4UTIUm>TO0hoaBF7MqIhi#y3G~M;%>lcb'
        b'%i+j@Ad(+~oa|fj%lnql+|XyKTiL3vX^d%$qv6k}w`fQe{w>>*Ss&i!|E%tvDu0pfVKyg7@g0$2t67#|)Vy$W#%z5?P6`QQ71oc7'
        b'tsEmAH*&0NiW%~q95~q7s&7R0>qx*k={G~<7P2oqOsa)QZCM+>#@K4`%11Wo7YUyI3G_@xt#mGrwbz`P$tE4mB14|cg>H93MpA5s'
        b'MY)!=feUM;150(d4?^p)se165@^&}LscXxPpzs>&-uETdeO4PMn6*MJ*~E-bUT{&YHAIiaf}u|BND>SrvFci*Aa@u-YKPozPR((c'
        b'r{-g8wFnx)GS%_BYX3F&B}D50o5g;48cX4|c`X>dvq^d^Bt6OhG(G==I3%U=T0`wr`l7?6YIw_>_WnbH!Y8N2`G1-R9JkTaM}NJE'
        b'O(sY52Ko$>x$m!}0^d|sZ{hrrXNb!fkN>gC@mzbMwSJ*>p=->iAIZ_P_C;MxvXf~IR9^54*4CfUf&749&^ZgaW^+Q(Pl{yS=0Z)^'
        b'TU_Ct?Ck?G>t6SWlBvsL6%JeEe)U^-J+Q|A>sxPFtIc=5<YIGk=d5u)<#PHLj`;Lr?fRw$CdJ9r1oq!wdCpyJ4GKCs+(MSY)!u)r'
        b'F{bohcj>*Z`%*djV^<!bf-JRG=G6#h?<&uJjxMva+f9xep+~j(J*xgs#maHIU{({YyU2PCDCwFdl1aPG7ENc4-nP$a$(ui|bC)}E'
        b'6<K<(%41tdA<K27S?9Ru4dsHMwptgC<>(oO({0^qwI(=}(S6rYmt?DueS5L`A8wa_zR!jauhIJN+IrH{SHZ@GJhR5=rGq>s)m+nX'
        b'wm&jYPv6FWI<Bt4;~&}NAqAkOL3TODR6W+<A8BeJ2V6~!PscjgLed=dthxS1wX|G%QKFC`jo}N@zMAKMe@PzcGQ}|~=TszA$1t85'
        b's#h%2Jim+0P{($}j3^ktnOpv5g?8<`H%t~POEyk~(@v&)Oirh))-ckf{q#m!X=0r;v8E?x{SNNR=~Z<4Ig#l@Hj6T`D`ty)fx1CX'
        b'lGCB+S1_sVulh74FHhFe--Iie&U9&*lBXv__xqF!;^@niQoUVj=2%>ZqEEy8<>`dFr?oy-VJl+j9e2mHA1LX)|EcX;;!2KA6r2sW'
        b'_1RhBD+i+&#Hl)g9G&m}Y+I5lwUJd+%b0nM9)*lGvfAbV^Ux;Mo<7@cOzK`X#o8X!?oLdKAr0#Jhwnb7k~3S_0*0CY{xjN5UCm3G'
        b'zBndzcW#>Iy|nL^ES{8p;JPnP_HpRh#6M5e%zrQS#5|w-wcw{O$k^0}Hmg#FO?}O`G5ueOJ#h=P(*BgDt~CjAHb$t}uk4VolC9FO'
        b'%04FRp?9NL^lSxv8BomHiWrM5^Ku`;nGqy~sv=UTzOC(IqPKO|o5royan81`(=~2YjE^|Sor-mx+2f^mjC0&ND>H5_9k;F@=VI15'
        b'*Q~SNJkD)g$5_{K1?x)Zj&q82>o=|on#Mcz<BV=yY3}%#e0+qyO5oAxI~hnjF(9v7<Mq&Yhr~tqI}Z(`C)F&5OodeD%a{SVLsq1x'
        b'*Q6fM3U@F5nsn)NljH?ijD>w)cEMnmkNr_E7{}ZE?fRm->6vx*JA)rL(gTj>fv<yK=&femNcakprbl^t0r~QAmcjO7(CqhHztGXa'
        b'b%v~V8b6CfrSY=HeU{s#%UUJNmC{AIB-Uv4(RnmPuF@q{{>|#sg#$u2k}|AfY<~YDdKt@W>9pS2^<uDdx6ZnkPP5x0?P28jXN+FT'
        b'k_O2v!pl=94qTKj1{yl+r762~_0p7G6^4QnqSW6c>;GDouzK-Dvih$kWm+`*4T5}ZyIx2-=(8*#iQT=rNjORl4F0A_B6eS~Y&z?%'
        b'$Q)UDfz*x&x2NNl3Jv=&dE-hPQXyzamNl8f<E;&6>VKO}FW3Aw#%dnUvP91(UUNJ?XVb6(yDHKLVAbb5=hD=)?LhB^%GWQ--=etH'
        b'8>u&1)mCq?seyFWX;+#|ztGK;ilTTiE&R#c6cokz^gAPpbLgi`r0Apbax!|7VPuSzgj>iTN5?<TklCmi`z;4<vXVc~j+n)NA%Cxt'
        b'KiynL;w0f5`O}fVRap%47aN&^e81av;HEpt-%9dVO#bG(*wWTgd8yjTmR69z6IQ151jm$aB+Fswvi?d^z%e9cQZ=a)&y!&_!w6E^'
        b'&x=ol*Wq#UM`DU!CNOMiy%hGP_*8h@P2}%w>Elajy}lO3*Xida`k^E7$!aoA68ARpH|LkR&NP$Vnctf0tlOFEbav%BOUd7f_FQME'
        b'BiGsaP_Far3*=8@cd~!ZbuN7Lz)g&fVc!2Z*IDsluG8|X12<KWarJ-Ab-qEu=8)kB$a<1>VVt{S7B6`zW^pI^e3<-gC4bDWTqkoN'
        b'*ZIN_nU>^F68U>`Zuq@4q?M~E)V#H`FG1$Wc9<M`TNyJtck*^kpiSJobET$lhAe&V<WDt$uf?Tgur!||A*1P&Khy-8Mcq!$lf@L1'
        b'uq0W_oJoH^mzxk9o{d9h&%Q0rN;-#%7_0kEx4X2^<m}wIO&Q~K-s$WtE!5lmZl`}^E)BTX=`Z!l>Vq3|<6`RT@2wA(=J^jVS!(V('
        b'J+fHuG<y!_xCGL(?{D&w=E{<sky`yC8=0f&ZE<9Yo)qNv{49a~^0|=rqH0MFdnV7X%k5UDnwtb|e#yef{Z|b8-DC0WboMBl+U)-+'
        b'|3{IY5d7CGgPLfNYnixgxk#^CE6bLP#W{3Gb|_un7dh)M$k&xhcaE%dg|0Y!En6uCl@*e)8%d}?M;{&G$`_a25}r?UGehRX=ZXHy'
        b'6WP_vZW8nUOh;UCS=>vi5~oiWu9AG=kgskKKe|C2^XW#e3?0f5dvnA=QdLDld8;UmDE8_6S4O;Ic3U%Pl<v6Vy*hum0;6{fw8lBx'
        b'b=G$2UV%7i{McUI$mQ|faf5qx!7JjcdlX~sx{>e{;f16<enm>yc=mSoZknM5QXb#lqey$4jUSjsgIrP`$BN6;;k+U1zf2`gWtvj_'
        b'^o+dv4w9#=f)uo_UR{UM;ToNs$Ze8WFJc@nHigfovk3oxqlV4OFluf4CY$}T<$lK6(%9v{m!Bs}_j~U=KN<M@Bx~d?qI7dl=MOkO'
        b'gMMw_(Z>IBk&IPz$o8z@&C>j&|JmuEPd_$&U^*=iWqhI(6wh9FEPf!qXF3U5ox|&;z!>%hcIM|X$6^LlJ+U;dkp@p_j;RJzpNE6K'
        b'3GneWux%?JM?WtF_HR8Fvn6Kiy~bcoW6c&#?)Q3LZBz<;&7zk(WV}+EuZAC=r1wD>8M`aPD6ifp27;4pU5~8gi;3-;q5qideSI?U'
        b'`ec{?EB*qFct*y2u3;ZzALvogRD4Fm*q==(NU^><95hOU0xwUpij|tK-XxN#jxxux(a$C-lt0w;C6X*o=unQHnDDo7xhV=du5j78'
        b'IXZh8$=8eo`d0IE((Ma@mPuMukS#*13YSCHGCDzOiNIu!OsXYXj!*cXlV(B22`+d2#``K_++@$MFYT6fS~vdkCo!F!_jX#PUE4=?'
        b'VOQhi$g_H~8!u`nyYLcWq+P%4x0CGxdp1q+P?f6YdPQn}lMtwzOxw3o(<38`AXQWOe@)bB$oyq56lPaXey`QpeovcXo{;^-q*J)3'
        b'Rx#Qox;&F@%2q{smzd2@wkfjRlkDwh6wJUhvLU6t+)pzk`{7A8o&=MU`an4NX&PL!;Rmjbla(i=qUnz8``JIAWa%zjq;UQF<W*x_'
        b'4_q^R|24yFBg0j6xK_FCjJ)7U#<ga0nPW0q`lX26;uvmej5VLjzI!tEUb$*BJ*E~amaUpB&ew$(J%4i9%J4+|9h1@Nq>AJ(8|2j<'
        b'#<hIX84guTp?MwR)x$47PKI4eC#Qmx%ZeuXqO0e%tROlZo@&|6R}CvGTds<}<BVMOGscxe7R|X7SI&CDWaTGQmFL1qRwD(MMnd={'
        b'G`F|@%cSdHq;-npzZ*?`oHS$CyerqHP@Qd=w1#s+ntz-tJ({j?{3};A&UM{2GfSJidVKOV;}fqLZ=4#xRh-Cs@vl<om6OChaQ3P}'
        b'*SU%4aJF*tJ+hhSG15&hl^dPmrl2Bx)6=DiXwxt}e0FL$`|}CcM-$RS&TwN=k^Sj}>&(?brY|R0g>-$y^!Y^P*O4nF;llFv1UVA-'
        b'KPWP;A(9&IicR0lTs=&Vyg6J!rRWOLWcSyTR*$q4_6f3_>cf$~V&LNmHf})E<&Sx2^9(^VHz_gXCEfX^?U~YpF{!?#?ewm?OCo8x'
        b'7DW1=fp;g;KN`K_-JpjjXyrOQ5xF8v!@?KEw;q~!-V(zfqGP1XM2QcJ>F18OXearDG_3jpZL4;kQgrqxJ${+l&vaU<xGv7LZ-R8$'
        b'Do3~W(VX$bF>d$9M7tP{NITV?wN)K*cQ@Da<S1d<Ghvo9b$x-|6XmBT>Xz_bbmpv<T|JsQxn1+oOA|vcP4xMHwezJ3{uL>$FVp|)'
        b'#>=xN>)JnhaboBNGTKvcUZgis{+W(TOp&!%CKLBCAGJ*kwUDv3{a=bLUj|9#z2owF^2|S2f1b4W<};+Jx!V!Ur>9<Mfi7CKh~E4_'
        b'x2j!Z6{I`)rt;4#PZO*{kWD3_`{U?qbT$Vn$KCDLV7so@dpLZ|&ez}iTKrJ@yS*9j1~T65@>izYWN$r7FJZL>-_Q*y-lgRu#kMbD'
        b'knBSFTx7W^iyZWjE-g1MvfQ|<ujiGY5}kF|llcc%=>5;Ri&t`N(yipUskX@XtXREruu;#)zT4E`UZHa(zC$;ngDk`;=tx9*pR<GB'
        b'uWO@eEMg6`_~uA`!McSR3A1L63G%mcXastHp<p!Kdzf@;X&Q_L7sPAEeV2^mRMGpguO7Me^sp{pRxjwB;Z-n3&L^|9Ki8a@Oi#<&'
        b'1K~E7?f&FQUx(!D390R4wFlWG8b_cfqpr$>wEbf_davAB7_{aGStGsKD<@D~Ot1PC#??I;*`-MI$_rMzmF!4#Cm?NVwyw)hFWEnQ'
        b'n7%8hcq9L(;S8giKQx>%Th71!POZTq7YtipA2#*8Q(UYp`C2bsMw~D8<}zHn->H{s1an13IAm~z-g$M1Yv()HhIITxNc*)Rc`wra'
        b'ER!zH5}9LUAn(uOl@YI=&L~w1Qh-qk&`EV#@p4YOnOql{`EyJ(Rx|-m4qp>OtD$S+@b6q3a_5mNLu?iE!~IKhMRK^eoBhyK{usg`'
        b'BP;aQt3$GX_6}QgZP>bZnEZc;SpLqHA<dSw%3aoWU2%K({@gSv)^+uf1YIYcAV{<Nbj7Q}E1wpb&5C!TxB5nByzH6~nsu4<GPgy>'
        b'ac3j7d3ZRSwX8h6mIeF7@HuUZyrem<xOh&6@m~_Fn2gy=GIG|9o}zhSvt*e5<sIh=8JD9gz9XEH45!OQzT{QR4d)k)GxweKSI3be'
        b'So+V2kqF#7{%?tpS^Y)$ctE2hy)*bNQL_3+#SG)Wy-<}g`)6x&>ZG^^lYtcHg!-$Z8>HwnRUe9xI4T;)`Ymx1R724?lSfFL;%|vF'
        b'L$yB|=Nyf*{#)WCs$Lf(`L}iSNNA08CTD*5OlU>2Y9d;Pknw?=hmU?NZPR)F$T^^S(qKk(kp2X_;fh<h4bc&X{tM#e`Gkf-XQC78'
        b'q7z0Z&_yN~pW3dcZQ+HQW)E{$E!W6;q5;NhmV6zX7aet7!4=CsYL3iHcX?iyCk@}j<t6c~R^`!V>FP{|X?Vz)L+=l_+QW5X2CeX<'
        b'aR$?KN4TrT86xL`=?%W2`=gl|Ev(`B({zLy!uzlEaBO%Vpl6CA_tzg&^#1lp$sDHlH%9`$J@WBe7x>>CxqN?P$e6wPh`H}lWq;jr'
        b'!BE<*3u#H6dTH}=cgT8784N0=bIle5m!Zo_C-J0v1nK>3j~|ih`n)$TRK8^`PUy_nZNEP7t0P^0CI1keKdXpbKqZ3>Z=BuMt?&KC'
        b'k-#sGq%GxtM#rnpi%j3XOP=|%h8HK?ZgS+}>b<%=zs%|5It86CEzkeByTQ~GQ}fbH=LKh4o6{F$;+*dKt@C5jo-X!ToqL0wKhQU='
        b'AXU)n<$38dLq~>we5CisBn4jvetcwfH&Zk}bMb+Nm527;w)yBtzV6mp+M(4)dha3;{!VtozVexcdF%`()ycdQ7|f>^KZ^49G}Fs3'
        b'zYDBf&CaR+9k=vu-|9_I9#9u0sX~$b<mwZ)$m>1`6dqxh@{5l|Znn=fXWD#u&3y@d!*M>%eC<P<mF9|>ONFKFHQT=+&6h}f%ywjx'
        b'`SNqA=@-S`+#@>|9O3e~;6C@BmlkM7Pe$)oNo>sUym-mBPeI=~I60WxE${z5)8%J9{>M9aJ(z2kt2oAe(V5onUNm(K)e3urAjv9U'
        b'&=*Xbo$HgUHZj5WAfur#2cEC63f84<v|-X*`E_dwZO&BD>r5pV6sbPC+BpGlUVV-(@$2tc>r1T;o%L&H+Ba5TaA~+HAsCOY9Ac03'
        b'P9quEA5a}>d6wz)nAkYgNzrXBCA};+S@hTLs$gfEep9=&99!1RL}SYP#>%(HCUmd9t{oB&_lk$R0<RZ*DW1sLKRfj2p-YE*FCFgk'
        b'AMQUXhF%!Dc)0f)GIXTiQ}MIK2fo|4Zsy$WStFn6Pkzj%75<1OxsJBLHd#qKr}jso6ExY|1NH4zZ=SzR*OnLixpwH(;oehZ8IKga'
        b'D|+72ZQfV&y1e=(rt*;ItxE@m&i@LIKePA!&8;KHbnm5Thdw&o`!R_;TlJQ>^go-9ohN1FuZMe&k)Vu%e)0XJ!NG+3W84Qx>~1=N'
        b'Lp${T;of)1SWEwZh+boTeM0AMZnx2!#Llb#gRb4zaNtsFa&25^JJ*)nn#3m8H*vls67LVXrtM^$BaU@QK_l(D2LIzb9A-vK-@44k'
        b'b?(-;@1@t@x`yY?JpIF=7Y_G!kc{|J)gso9JJbGDzc(mF-8x^}*=|jHy8h{4!5Q%bOQyZ{M$b=XcIS~YK=R`Kz~EkvbQ5;xHJRx}'
        b'zSe-SoIa1fTrgJlxy`z)`GQ<}kgZm3F;<?S?}Rf37jtw^Wfj%Y`Z@9N9M8TB4Hj9wUzvE48QOlhcl+V4XMY{2JzV|-GyLMEL7(o!'
        b'oJEd8Bb!coJw?X-Nwo^rXkE-XlJ2UKs}?eXI@CH;f4Fxm$*La~d?lVpiv42R&~Fa+){%f8sp!3Jga4(o`5zx_FimLQ+cncVLH2N~'
        b'w1*FpJzSagN2kwf6@!I#yCw9-(1VA2AEc$E`oGAOp=XDFez^DFX*sF>Q0#nN-?X<Vhvc1O&YrHkc{6YIT5Ug>Ikz!u<j169U=wJ*'
        b'ycDSX+Pk82m$iPcZug4NDdsvSb2c!RW4(}Py-DZD3-t_D9PX_kiCfbDrpQ$8vu@X&^ey%Il1PK2$y=MeKdJJK&F?$!)_r*Wk{ptN'
        b'A06)fF^RpdU=Jw<v7gCR=}hS5p&uOXT}48F*8h^oI6otm+2bR0{XQi%*yL0VHX_wvf21{-7+jfCI6HCltHhViNb9j`A+3he_jE0v'
        b'H}kGWYaUsTr~WtVv2^=MU**1Vs-IcptBtcKRURM%B&X}UOxt!PTfZTN$to45`ueTS{^Tw{*SXtjZ4Y)f>G$|(53|9RIWx3th&|lP'
        b'(h}Iui;RPovz*E|zIP*OXy=lBM18n7hK&4s^`oNa{+aeXHkp>Tq5x@@lO5lY*KVfusxQ#Jy#8s<w>(m({ZL-FEA$k-7pdg~kye`}'
        b'hZ*NfTyYCG+9^s;$`0?laAH<vKdUYMwQk+BuO{ftZzxL5y0ZUxd+rS}r1tCVdT?Y+S@+kW^TWL|QY8NrI6j>I1LoCSdH+pJ`+eTT'
        b'%Kh$4-O?IPaKCDo$9^`uhaA7s|3qe<IDVl=vHp#F__yAscdaTqV#<d^sW>sA{-IODy{Crh<~&8q*Q-OH4flRZhJQxtA%<*4&SRQO'
        b'w&59PTB}nCN-qfCIzKk;kLv}x4GVAZW{@&^aJcv2Fe#%2^w;x3ZA1Hqd;5oJUG}b6<nYbu{5Soke0rYzmJM@e-nY%#aPQ2!d|4y^'
        b'u3uM9wk@gIo(fc+7fR~4S=~OJuO#$Yc-t1<GWJXB`i;6rZdv-9ETOWmb{1(Mv<sG`$|LlpqDhunmB&9&)339HS?-{+?uDVf!@aMO'
        b'#8<1jMN;t!I`dn)x!v;WyP5W<_hya@n?D;f>pF$t-0x_InumLvNz~Z|9ik<f;}YB+t~QzNA`{ivv_sDf_cjgFx~@gE%wp$|@ts}V'
        b'?pdwLY?A*)-O2XmgO@BRJ`HJ5XQmV;SAOV!PB)gXbGLIR=d>l0wnF0alY$}kguL3!BtCa?>;l~(#yqBD?D?0HoZ?hwj*-k%4f~Tz'
        b'Np2nsR@e&7iK<hHM^1J2=r`@XU)m!w_Po4i-pu<NvdJEC*HiOGZYSBu8Xmqg{6c)`wubejQoA#BfxdZdIAFPDaILj;jc!f3a_OdV'
        b'nr+D>+cuFL^r<b$mHRpR9?Zwx&8C{JnH)K6wR6$KWZL%m8h@*m3k5st^z8zD#PUhAWoD>(sBpNqkZjK{3)YC4nX4Q=TSLW6%Ppkd'
        b'O>;7Z0g?$LA${g82UpNNK?t<2aBt#jS1eFe-x7XyLS18sGxuGv7^J07-SfouMegH@+|SsWSN@o|dEbu3DvK?veaGVXz!I|12YBTm'
        b'efRb3sq;7;ik7M0jw$(=8FCHxx`qRJ!}J717BgBd`j>F&<6`@B%?A^9?1~BB1ZCTI+PaG)&6Lq!ip^`3iH}aQ$|8CCJ)-~FV4J~V'
        b'YYRUD624cfZc*jM@?TFx?~#?)rL=6F2w%HT_V^jA^qfn{2?bYMRU*(It7y3-w&wLH(l?4XYPPqxjERE5-x_RQBTGLM{wkQ;3^jXX'
        b'ZRYSBIIOejGa;;Es$bCHm(hp(!!u4&kR_b%?%H>uLtg%c*dcE@Cw3^xPmx)*x3(EZPm?b_3i`D*ujMH^{_oMY6U`51xR;cJ$)PU)'
        b'@$_WosDjipw8?drq%G1eC3B|fI3d#i$3*M1T+68VLk(Sp0cHBjbR`~bHLPxLGju3M|3;QpXeR5>X1JBE0a@G^V*lxITR1JmYUw@u'
        b'KcH1hVnYm_;VF_Aqov}`ks<3ouDnQGd2`E0qJM>_(3XCi=rz<o5tL?E+#W0<hk!PtPqF<ae)3T9Stos4pnL1`{nxpleAfM>$?Yzs'
        b'jh)%j&%uPtNZk?PmQ=x0t`y2sh1&92W5NpZxk5<K?LO^D@BfDO3mlQ_$#n*^IsE$@A2H_Me0Dp1vWw4tTWX>A`E6Z(Mi=00uG?*{'
        b'@ALC$F#pofh+psi%?wVE`I}v2cTQuuF0T3D1iy2LjQ5{X_&b!g-rIW=><j!0G>C5-%KXUGI%F%;WqwsVWb0kX%DZOM8JqiLd^U};'
        b'G-qwzsSa6-XFU8{QO*9->}#yHJ;2A)g?9PRvoGw~*`eUQG<Hk*g_3nK*%OD#ZaTDR!!K`;n;M4}EzG^)dRODnVuj6hnxxR?f7to`'
        b'88+AFTs}>w&41e2&ZXq^`E_0U<RrCu{?q)EbY>~}*{2SbEjYC3`rI4j%lM(}Dw0rJD8cpkkh$!7lV>Q~O}^Y<_MhiWZgW|#>DNPf'
        b'WjW?DyXi3!aiO_vk=egrXLc_yb8P6Fljmn_{=ZbnJ5>BbQg+;N&p^zQK#!_8C&({6L_${QC*I5~HUF~VgC#Cj-XSyRGwBbGUvX`p'
        b'Y|3NjBl~XTeKcp!U-dqk(UJ4fcUUM!Ka9pD#s9C-a8jO0kt_e|%ITbUc$_)SW<OJ6l#zpK`Fmu-x^+D<{Ov<i@0=(vx<oc6DU+j@'
        b'!jB6~rHf}+Wsfo~)FI0&i{)GCny_|{OYZ4StIhWK|L9q!5#&8GAu0U3G{Vn!+J{)fp6<@PDre`$)AQW(8jlV)zsR`j|L$+qx$Znf'
        b'`s<9KudhE#$}fFm5ZUd_0d+sU7m+MWOPAC|mh>BGNlDQqu`91xP-v0m=k)ewjr4v5y04LP#k=WL9{*paB1=DTMc46ioL@?FF0xuT'
        b'vK7|aM!TFuwj1d~IHXG(xzCKh?ofkSMzWG*XpK+a^2CMc{h~a>`v-En<A=n-US=r3kgDW&<wrz1^9~tbO6Tp+&sW&UJmqPE-RN;C'
        b'dgu#q$h;%(b?57)>AxK8Ju?^>8|?B2$_Jy<7l)^}`QN{K22$E0({KIlK=Bjqn%(h3e;e%m+hE|YWELIiA+gV&Mo)6e_?zfViuCN9'
        b'yk(j~`Er-6Fd^;9<t~N8B+W<}+2-B{r8jmR9;{0y|J7>9e^)(&XK9FCV{~%L*n85oIdyAN^TWTDG%vq&c3-Nw)a-G@Sk1xP6xRHE'
        b'oaTGTREc?${gLwkbXvXBO{SeerY%gB-ormH|2DZJhMObBwTS(Z=Oe83fA{z+%z>C1-!y(;fb?u_hl8xzYN@*N7+A(gk4ddyLhXW#'
        b'EgB<5h}3_I=>9_Iu|G18=D~lMhp=YrD+4=kc)Q-K>yW>itR{z&2LFs2$MjzB;7;%0a5IzsgtY4Hg5KW^?)=?gLHKzBvpgxSmQ~N)'
        b'E%*54Y#t~5cmaJc(Hb_T(|wkeyR+yM-Jv$qrok)=*HpD2uI>?5o~bZBbBM$wt=;xOn<9Kp=0u*=svL2j&9MCXoPB2E!|K5A53Nmd'
        b'@s)$@UO_#qR<iq5dM2YV=as_S0>3@9c4Y?t3$kfX(Q)Jmc-q?Cm{vDmZQb9P{m6jz3$9ge(OAwz?xW;?LZbeJMkOhI;Br*DLHK*g'
        b'IB5}N*LbbqbCLh?;9_Z5v3P&MS&_ecko_JVj7hUskBRiYjBs&W#q%!=NRJ6RZ+7LmWO=<@k*QEaie_O#kBk(gseAOShdElq`spUR'
        b'Bu2}SO!k=EVqmpv%to{MJL`9FYszMj^sWi07HIBEQH127m|0_eerK0oq&wzTX<4x!n`T%v12L9ivhNM|I>`imCfzYj`~23})%S91'
        b'@3CltPX#Sq&gx)~tf4H?Q<gxYG?)_mObH7#^*i14nEPIc)&r)5(){3(6`OKySE-JRG(A71>Cu=;ddd>mIMz_y&{$74pC*(^(|j9C'
        b'Qqn<Z%KuDCi|S)jf<;3TVQC(S=~0s99Md$LbgSol_~?4`J<bh5|8v2CSkm4I442K|_t1s5CbHW7dpcAjEKSp}X-3KTHv&nU&SNof'
        b'`6S65swFE(yhn3xmy?bLDc6N&;a*mGYtlkCwbf>Qsj9D6NygvWWVGvVy+dO+x7zFvlH68Exor-_&P^fpk=UV>uJ17&>hL>+0?gLB'
        b'5WhJT-g3UJo-#FmBV7qrkm^vbHv6`2Qq#4{=c_%gM2n_JW-&;Gr<L#Cs@=pU@37OGlski^+qNq!Kd5nN`S<8CxJ|L!NSCYXm!6>s'
        b'*U@xyrH6}#$G?`=wq$-Di;RSv-qWL@l{h~uI^Gu<FVLUi4ILB=9dd7y$1<Zk?yCBx?AXAX3}$Ykx|x;_8d~=1+dVN4mvkscVj0pZ'
        b'eON_4Lr+=~NwPa)3eJhn^>>EuT72QQ*t_iU&h`1B`_e9K@N;+BWofZO27Uf|{a>VG5-Ea0clfYTvS?hmK?<Y4fvBJQ4aAZ?7cQr('
        b'hz7Ku7Yf#|2uhpk(fopsr0Yl?!!(k*wfoaqwP%^a<9BbZf4f%JDi`z?4SgTrmbcC38TA5Jt0!A*>OEP~ZvmD3jTx$bySL`;K+W4-'
        b'fd|rmE_%$e0g`FSY%0x{J)~MocJs=5!Rnbhu7!_>yMN9fl**R;@&QqxyP=TOBa;rg3pBOL=<k~8dbuwD^|bkLQ9RnTw3qz>X)0e7'
        b'Lnj59S*COgdbj&5N0Jz=I|metNsRPw#K?W)w4QC56u-5e9Z*PfI~VO^Nc+87+V5Ll6EAPeXm~c6@!l)Kdl$dGbMf1xx}~k|1<cg*'
        b'-_iRV?POEgcS%RP&_O%dAcE00dq%gK9+{1-+FwOG0U@E`&*M!^^;K0bTxgZsHTE1bTG+rEtz@k>T;7cIC!0M1RZWwI_6daUsUN!x'
        b'r=^fAtMDc1fEYShNSBq6H-|1u$*>7zSx-pI@{(oMH@WMdsCv!PN{*L>n!Gtm62-oOO>pLLjt!SnX(!3B1ys3B8oQxK8Ci}07t4$J'
        b'_T^dr`{hk#L{}z5>w#3VjLlaqV{_GO6|M4PF@k15DG1>Q9j{u>N@+Q_{CCSKW3JerNt^1b_Z@_Uu0N0OX(t19Ub-@ZMtE4-`N%4?'
        b'N=0{pCe-ecF;;uf6QD0tn(9~fC`sgs%g=_CF{wARG0r<0Q*U8sw8|?qYck?TRLpBB6@~%XnvCS07?La%bM(VjnZI<S->*Eq$G#!<'
        b'p6QjxojE$khSD-6slrN|8|mya5_&2~wOVmQ@yi^UMw_o9{YP_JLFv8s2=-Q6kBTfdL*XL_kCKJoGzVf;XQXG<4AV##cmIg=mV_-+'
        b't%2~fU;&l1?+AH6m3#JIV&&&73u#p^9V1U~5@f|Ixx11~LSm0b=q`PpW;98#O3FujVqKGc7n>>#l3tt9JbOl$g}#M})F3um7v?t2'
        b'wIs5sX0tXNI5p>zlb0%Fwt%|0Bv?GVQALj3B?m87pTDAA^-QEq^pivX&?f4=@6gWs4&645?9XSf+V^`S`@Z`L*OmKz^jw71`u7HZ'
        b'AK6^n8r9xBc6=MX`ylenM0h{unJbDnEfY%Sc1@&(>wPOyLY$Ej(){P~_Ixt1z0h^bp*o{0|4^%(HeAU8qcDL?NoQ5~Tvu<Jw8o+K'
        b'JXxA`VK9%BmN|`59eG8aaib=5l9t;-soW~15V~(!FYjATjbztKtWZXhv+*sdUd^@~>XFeVH;HaHlIiRlI^>bvAiT3Bkw8+J+^7jx'
        b'C(3Ab68>G>|JlCXI<;>no`@#kPMU!EN{5~#LVYODCG{N0y4z;U^8B)INlBMQ@!#!_|2JvLz9KE34E&GMBLDBxa`mzPnktA?;hU=x'
        b'NvkuwbbWYJkp7CpG(RT0e_(ke0Y!S+J(CvyzpI;Qo0~ScyLD;Ffjw{Sd}(0*mTgIDI(ld4K-%r3EyPCJ(DV-Z|4sYwlY{^J_Mz?I'
        b'|Bv<|sayKSUNOfHJvq=@JrJlK=<=78e?BRl6q8HO0ni>aZU6D?!L8bZt$AI&mRjDowfs`FQ@NKe*CQi`lQFNp$=l$Pj|lqtaSbj7'
        b'X$T4$*M@<HUQS5zWs}`bs+28xX-PE=3oN{MD<`<zZ8G;JF0l5XU(hjadanNO^-Wx0%|VXa==bSJV}~>*NNcl|XAOKQZS(Q=0XA;a'
        b'rto8&p>DsWF|@|t>T09uBwhXR^I-w{e7%C~)(*bqE3rorZd2BWlbSZ4Bu(B*(`l1ZY0=nvIY+kHEVH%8kV2u`N$bJTBD0LkR7&-e'
        b'G(RPoUlHGOTBK(z==>_9^HY-2Ou8>*u0`2ouCCkx(lT`=Mk<=TIkY!(^q@z^WhALHEJ<w&+SyH07AXo9mb|$M3fiZm%SlTp7>~RQ'
        b'BhsczALz{(2ykS(Y#Tj1`G0KFeM|kh=ZgB%eD(9aQXM`Jsl!zVr8?aI4}D{qtirIh_Q2{VHe?vt)EbA3bh$FVBOMP(U+WpEuN4=%'
        b'UV0f#qzv;nNQF^85L2P)QC7UW{!^*1rHb^m9%z-Xe!{B>9uJlZ_jq@cwtd-*kINFA6~U1>h7|f|Gy|#*#mSuwWeI%c0jaMwV_lA$'
        b'_O=>K3Ad{Y{ub^lRM6@taZLuTepF0Jld?zC=T9SBW{sKQXV4_@w;dpR{QS6ENvplqVIqaHNS`*F46(E6&adi`*^SbXF<h6eOt8%f'
        b'@AZ*(0j=-4{7l{)tyJTcXjE5Mc_rgh%Pf@h7ie0yS`T>qT&{z3O-OTE;n2@d%5}&{w}>>TmC{Kg+5tPdu2o*B@yyYeB*`uxQx-;+'
        b'Tu54!`=5~RJe;Ht7XCvzmRy^TMKQErM3Rw5R{dQm9r4$s!{a|H4ZR;p3F%NdpX2^%TIO7tmZz>r3n@3;-);Uct!8q(w*_K2dzEyY'
        b'`e)}eNZrwLFij&pHn8)-&{fYWu#2u9JQy9Ee;X-96Z`2q<9~PX85!$+NYHi1E%nh`__V?BlL%Aqp`s_Iw4-tKnOJrys~KgPy5;0c'
        b'N;w;Tp1Q@z(AWI>nU+{7&OBDrqM>o-u_@^qGP#_L8=b~P-^t9T@Jncqh{UD$fELp4i8dLDMEWs&0UhLT2}!5^I^?6@h|*3=-!Zdw'
        b'@>`$%jP7q_ei=rsbaPisMvgrFH<SFrP=o(8Cj^~B_|>gmbtTDzsRuZwrVD*NG%wUUFBF&;x?4+ML*6*ar-wL8&}r7MHEOci1N7EJ'
        b'deKwcXw7zMbC_DaJBReHICl;gy?=;L4v|@1o=DtJZ~0l1Fl+3eOcYH!SExueGjgZ3NMYr+GC6^Fzt)n9#%ks`YblpQ@7iFDPLA8k'
        b'6&XofbKiAVThLla-vh@LDH5AwV?S2U{5W~;$BR_68QX!eBE>4>{j(p*;mTY(w^Maqv<*y!+1@;BSJ?KA)GB<&w%NOLxMmke;(Q^J'
        b'n8O2Oanq7#WiD{sXzL}>h6i-EeS^^{Yj5`5(RR=72glq_?r$!u+u2Xw141SvNn#96)<BLAB!MJRtbE!SYnVnh&zM=CYPJ?C&VQ`Y'
        b'=8%E&YtCD(3+b&bHoeu%bKF@ng;k-LFP~Z?);vwxt|q4J`v;3ZQQXdyrt7|E=A_r&-SW9OO<62`CHZETTR;8UZm{Z%cC%G)wA-vo'
        b'qdm{c8tu!ioYB6<YBJh4Sj|Se$2!|c=DPl0|K^Zebqa^Us#iG7R;9vWv$6_Do|RKLmRn5<#~Q0y;n-lEt#EjzNzZq(3hVJQn$NR2'
        b'?l@hnv@eoyr86A9kmGW!*6^rsFP<sZG5^%-wJ#U_MWOcif1BZWeYNY*zm_d}AUif|XZ(vPT(c)-_!$uZ00000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'000000000000000000000000000000000000000000000000000RBJr;6MNX0002U|FscRRaI40RaI40RaI40RaI40RaI40RaI40'
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
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI5kg98Bo0000W'
        b'|JO!PRaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
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
        b'RaI40RaI40RaI40RaI40RaI4C4-NzX0001h{9hYERaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
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
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI4`Jvbx)0000G^#8RhYybcN00000000000000000000'
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
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000J{K7N4kX'
    )
    _firmware_identity = {'protocol': 1, 'firmware': 'CNC_FFST-S3-0.1.1', 'app_image_sha256': '89b549c7030882a08f2639bf5a41ce3e613a6c31072ab10eaf1a20a2821ad29d', 'application_file_sha256': '7a16fb7410dc94aa88b0a6f7b305dbf7c0932653482fe9a9cf793678dff34748'}
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


    def verify_firmware(port, identity_path=None):
        path = Path(identity_path) if identity_path is not None else None
        try:
            identity = json.loads(path.read_text(encoding="utf-8")) if path else _firmware_identity
            expected = identity['app_image_sha256']
            version = identity['firmware']
        except (OSError, ValueError, KeyError) as exc:
            raise RuntimeError('Manifesto do firmware ausente/inválido. Use o pacote Python completo.') from exc
        lines = exchange(port, '$FFINFO')
        if '[FFFW:' + version + ':' + expected + ']' not in lines:
            raise RuntimeError('A placa não está com o BIN CNC_FFST esperado por este programa.')
        return expected


    def mac(key, message):
        return hmac.new(key, message.encode('ascii'), hashlib.sha256).hexdigest()


    def exchange(port, command, timeout=8):
        port.write(command.encode('ascii') + b'\n')
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
                                   'Confira se o BIN CNC_FFST-S3-0.1.1 correspondente está gravado.')
            if line == 'ok':
                return lines
        stage = command.split('=', 1)[0]
        raise TimeoutError(f'A placa não respondeu na etapa {stage}. '
                           'Confira o BIN CNC_FFST-S3-0.1.1, a porta e 115200 baud.')


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
            self.nonce = None
            self.failure = None
            self._closed = False
            self._responses = queue.Queue()
            self._ready = threading.Event()
            self._ready.set()
            self._tx = threading.Lock()
            self._kind = None
            try:
                time.sleep(boot_wait)
                raw.reset_input_buffer()
                image_hash = verify_firmware(raw, identity_path)
                lines = exchange(raw, '$FFHELLO')
                matches = [re.fullmatch(r'\[FFNONCE:([0-9a-f]{64}):([0-9a-f]{64})\]', s)
                           for s in lines]
                match = next((m for m in matches if m), None)
                if not match:
                    raise RuntimeError('Resposta de autenticação inválida.')
                self.nonce = match[1]
                if not hmac.compare_digest(mac(key, 'server|' + self.nonce + '|' + image_hash), match[2]):
                    raise RuntimeError('A placa não corresponde à chave local.')
                reply = exchange(raw, '$FFAUTH=' + mac(key, 'client|' + self.nonce + '|' + image_hash))
                if '[FFAUTH:OK]' not in reply:
                    raise RuntimeError('Autenticação não confirmada.')
            except Exception:
                raw.close()
                raise
            self._reader = threading.Thread(target=self._pump, daemon=True)
            self._reader.start()

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
                    if text.startswith(b'grbl'):
                        self.failure = RuntimeError('Placa reiniciada. Reconecte para autenticar novamente.')
                        self._ready.set()
                    if text == b'ok' or text.startswith(b'error:'):
                        kind, self._kind = self._kind, None
                        if text.startswith(b'error:'):
                            self.failure = RuntimeError('Comando recusado pela placa: ' +
                                                        text.decode('ascii', 'replace') +
                                                        '. Reconecte após corrigir a causa.')
                        self._ready.set()
                        if kind == 'rt':
                            # Realtime API has no GRBL line in the application's inflight queue.
                            continue
                    self._responses.put(response)
            except Exception:
                self.failure = RuntimeError('Conexão interrompida. Reconecte para autenticar.')
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
                        if self.raw.write(wire) != len(wire):
                            raise OSError('Escrita incompleta; não repetir movimento.')
                except Exception:
                    self.failure = OSError('Falha de envio. Reconecte; comando não será repetido.')
                    self._ready.set()
                    raise
                self.seq += 1

        def write(self, data):
            data = bytes(data)
            if not self.is_open:
                raise OSError('Conexão fechada.')
            if data and all(c in SAFE_REALTIME for c in data):
                # Stop/status/reset bypass HMAC and the pending-command queue.
                result = self.raw.write(data)
                if b'\x18' in data:
                    self.failure = RuntimeError('Reset enviado. Reconecte para autenticar novamente.')
                    self._ready.set()
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
                if self.failure:
                    raise self.failure
                if self.rtseq >= 0xffffffff:
                    raise RuntimeError('Reconecte para uma nova sessão.')
                seq, value = str(self.rtseq), bytes([command]).hex()
                tag = mac(self.key, self.nonce + '|rt|' + seq + '|' + value)
                wire = b'\xf8' + (seq + ',' + tag + ',' + value + '\n').encode('ascii')
                with self._wire:
                    if self.raw.write(wire) != len(wire):
                        self.failure = OSError('Falha de envio realtime; não repetir automaticamente.')
                        raise self.failure
                self.rtseq += 1

        def close(self):
            self._closed = True
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


APP_VERSION = 'S3 0.1.1 — Controlador PCB autenticado'
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
            self.emit('fault', str(exc))
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
