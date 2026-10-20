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
        b'c-ri}d0<r4^*DZKNl3y&6Nr%|>PtvMf+5UI$ZC+8?13y}62j_-Op-}5nq=b4gvF*c6D$VAPg!gQYrmaD`G_bLkSZ=zK#OR>f__@9'
        b'N=vP2tsfU$Y64l_@0@$@n~kOVU4DPP1Mi)?ox7fU?m73~dHJVCZ9KRm&-ghZBpe<hN%&TUWxu)LDGhohX$Az~6U(1uvzACrkO)(r'
        b'SJflZ!V>~dC_EG3X}3FVtJ<s`V%~f)-9YA+6&BBJw6}NKJFFcp=iCOn-PLBdG+7<1oL!xrc86=O)6wW3+}vhywx%_bcAL}gml5?g'
        b'taDjcb#%33*gO(Uw8~+%G_7(rH+5bbWnF7+>;ht_O1q__iDG*Pv34}+Z*{sX4wwGBRMpne*w)o#^^fXu+1k=tF(U)Z$Urb=6$FU4'
        b'iqvUoYI1znj<7mASJ~PvE!I`dc1OF#1szdfX>06iv$(8HVk<O-6s_&FHhO(QRe?TevDrJEtL&?-jy6jt0c2}lx5`@)tJ7(95)-@~'
        b'F0t8SYlDnz9b%$06`tJ0CNVkDnKCJYSQ?;8$tmI*i&Jd0v|%!fOEedVy0wYA?6r`h75cHwD#pzhD;JlSe~$*H8=UC@(XAF}W|PHb'
        b'q2rw>&J*X)7j+~si6J9%RkN+b7T9JUfy5+fRfE&HiVgxY2=l@?{2x?}2SN3cXc_*wQ$J?!mmccpA`M;5%~r?v?HIpc2lTAH9SZel'
        b'V_RDrkDzmtO<9J?LwQCIOyW#8@xsSZ#Mm7|jE8zi{cQaWKRE~(f_q5Tn+tG`znJ^xg7jP7T%fsy`D5Xk3hpMOQ2!~W(UE$Zdn6SL'
        b'<Rj_L1?F=?eJwmo;aLe!Jv>eDw8C=^o{!-97@kkzIS<b_@C?HfMud6+o>Fj^!*g&dF`kPd#vRj$(HudHN5C&V^Qso>Adyjtn6YjD'
        b'fYyyjMyPi=JdcDDV|2Z`9$G+L;GYWlVeKH%7o9{4b^RsO)`$|R9xHuMk0fa^{8}QBdM(N8qwR-u_ese#{nJFcXIPpF?nsE6*N1V^'
        b'J=qxdg(T(CG!r1tRw6AJmWUCAVi@gORom@Q5Y!=gCiJt0^>+f)y)cm&QvrVieSa^+OAC%bma6f>b5ORVA=1lZk}>~UNIjLX%+5=h'
        b'ZdKfNDW;mZw@T;2h&6=7%qG^enz*0Pzy~n!n8zbb+^cfmkDk4%!QX0PUKrb}+Vy))@6*5V%ogvPermu&b`f$|4WaLAGEGDr5ZyhP'
        b'd``p-=fN*b-}S9#z@tjMs1c@H$29u8rMSB#)7{b$k)&wgm8^BIm3rbu^lJq*p!i0zE1AT(B)v<T^~^PAoYGO3bfDkd@06^cY2uuc'
        b'-U;Co&p4!`9T0w7=mjZpA#rcSQr&&Ncif#)_eYRlw%V8;2{=bhJ>CB;d#%$+Vl5eLC4+?|F<&z$qAvIP#1g1^-3u|hN)hMA=vPR4'
        b'HM{CGR<mYTlE$=DGH9^YrCQy*d9m80g6p5HQE#XsLSfQOLAdwZ^a(=r0gqa@XuI1=YhsqZESLJi&Xh|>%cc1dyTgtgRDIY_-1W3e'
        b'HSSfk^EYUO2)6;9^CN`mZXLRM-?$(|Kbx)2_mJLKE(p_}%~lEF-R~M+`BzVR<d#BFm@0(pcC0t%h&r9?<SPSjeBFJ}xF^z+y*}pa'
        b'P<=XfaJEKo;8@SGj^nu;r*S-o<5Z4s=6E*8DI6zrJd5KbhE0i5c^JC1J?S`<Ia*V^)cf?yJSdU{-6#oDm@8JIcrcw<Zy`6FFV{9V'
        b'sy7^vQnlX#-X|GexsdPaIsO#Pf=mm6zPXWh({&;4XzB6n+qXtbec?N%?Tp$wS=!PUN#Ei|mGz+3<B2}KNwxJ_X}4<2p2(g(;uEUG'
        b'=OI*k4niX!^iY%>KA2716C@!VDzY=o9U^sKpspLvLvg3ap}6KfKRf=d1Uzg_CzO}n<KtV$$B}2l$|JTgmJM@{jBk64(7^6b<-oXa'
        b'$F~k)%09Jl6Vwe{8`adi^{a8A66^fsxEz=q?*3xDCqB~sIlM)9V;12wM-R`Brt1HAocl3ycX<5MMBEc87{omo_yh*-2<tyL?%5eR'
        b'(BI?PDbn_AJv&ZQ@Bd)@%%8{i?TOs~9=yF2hr;^b89(wO4$$*h%%O<WFJk2L5tOR!2S@fq%4v6p9X*3N2>0_0!f4?B*T>IZvyUYU'
        b'+kaxb|M<8!gD_4W=6-d&|J8B1l)i}lKNuIf_pzRd=zn>9|I4(yBKGw~(jfOs;|HGp3(Z2#niclkxa{x$_4xi@d#Uyx9GA0W1?(Tk'
        b'(0u`+;r)BZ4`1tHA>k}!&p7k<+Q@*%=6)Q9Ubsm}JA2LHYma#*VAueLeWpIE7OoY#4|r4<_6wTsTH%JzAnfoY4BCM~H=GBaHIcaL'
        b'@%VT$ctJhTK(?TqhOqtx<3|^a3llvjkGM1a((cb6f6Jpf=9vn@)H+WC6I<;`-Y$yuJbu^pn*N;e10FIsUDNAP`C?&i=)1=S_5J-h'
        b'`joiDW!l5wOkAafSEKf<`ji^|)|<4u)@$cS3>*y`tkd@2HGcH2anCaYXW;#4ulp{n$EgUR;;<SM7=d<IotEa}wvF#q?Fh@Bx>J=C'
        b'Wv$WfRUKAamjSZguBG!~@J)$gs2NCjYp4bs!tB8i4XwAE>|Ze+TfP_S>t2qf%vV*Y2WArEL2*WW;$*TYy}9}eVaDEx)+p?V%zm=<'
        b'wsC`njfz2)&|f(&rbl`DB2(O4ri5=5#|^4PHf*Ki=hIaXyW1P<+0`}pwsyB$On%U_H_`fzR&N~NYNQMT;+4-r&DQxWWD8?7jX@>4'
        b'CyY~JoOnvxpNYLPcuG5PG;;6}?O_$HXNI^5gFn-roSt}}2G+orw4P5io&y7(f!<RZVUjxzX+57zai1USF+?T1VIu3|MSbG9J8?Y4'
        b'tusX4w_PhtPps3<a$LJVejGaLg>+$}?uGS(%b~8Gfe>pO;zzHuHfZ^HBSNf;S0zn}c&Z?2W>ix8bO;qRx)04dkracfBBbjY%mmyQ'
        b'z&#VzK;dg1@U29G;k7(tZ4ziHpd%cIXEi(<;ephkn~0bKv=#{!gifa2NiV~rLEQ`RU*H)+eFv?s`f$*nfc8nG2NehZgArzQ-9(I!'
        b'!83IRF-C$8Hx(Y#<zSMKFepb5BgqG#7k&fJj#y#@jfzl9E(`Nnz|BCCC+leYrZN2tbwt$HAWfbKI@>6e-v&=KxC=mUd;p$x@N}Cs'
        b'^?6K}`eh{7si+<%N#m%qiCk}^I+U5ZU*&4-Z%|pn611R$J_cpY>m>E4$3oRnb0yMEP}eM`U!ndbfcsNuL*xy_I2-iY$KYv&XB|BA'
        b'Anbm?M!<j1d2_*OXz$W@^Ne8-R_Z48OdnQ5d&i`Y!99=qBf<ZL^f|P3AJ8PilLZgy$%0zl3T2*vKKlKF0?ZGddsy5N>7EIoOJ*I3'
        b'eD2K!2cZwJFQt3XBDTZxI*ef`<a^@fn$Pl#$OD9Ig<d)FG7-=JQo8B<FCo!BX#3M@U;)(GwR9|qY8&J~0FN-4825lq{6GIANh_hf'
        b't?;<uVKz9`iR=4w-!(%XKY`~<Nm?*2Nv}yvUj?iD9OWids4qal<J6k(0e$of#$g{rdG)mY*APm66NLW_2Sr7W+>7C1<W<10#9%(-'
        b'66)Wv@Su8&3OA%i{v0t*QIiQ1>F$7N1f4e$#=0KHS%ChGgr^?-($|vo5tN5|@F<Lfbknd@J{@=r@@r{sZYJlTz6W2`Mx#A~G?3w1'
        b')TN=KQ0aT1{ykLB#~A{x1=)L8ovPlZ(zP78=1huobhdP0prk)V+I5yZbYRk%Wa(%kgp_W$2;}ZWsh?^}!^yamw;r7-r9`1?Ev{r3'
        b'w!2lh;Rst*ThZHhG*<fSjS?)MN2g0XqK`#fkD+`8?h^z`d|1#O-Y&kVI=3hCdDXrb=n78rS-bxlX<~YPx(ZfJT`m=rSZ3MO*LJFl'
        b'ZzcK(QntpRnU-5*{9rwVpJ+8{CEZz-@nq!blbHJT)`{u4i&2eRoB#9?v$+<OXLAk4EW>=VTLrCfUH|ZSeeHVlVwDFXnKW)Ki3w>q'
        b'F4Y?!#8f*Po+9<>k;X=hv+aPFqcsNA=vF}^Txa>`_?DXW#>J}o!bo!=CMj#pnigVsUDD~0ymWW<Q^Z^tshdZ$-i<kina++IX;Fq&'
        b'LIY-fJ(P`odLfyXk9rc;Fg`gZ>Get7Uz2G@vb}%HcHNfvNEEQN@}?8x+!$z;o5=lZj{_US7{BEqX0xl>LUdmPYq?HMIy_1AxDwAv'
        b'+`chAH*R>kaktj}0<HteT4Cx^wV*cFcjad4lGlr%nLir;^sTd##O(ERG*3-A=7Ai;j=Ura%M&k39?v)NPZx-@BWFFV-jGa$4ad_7'
        b'F?dd7#i)-b5_7gI>239fnOK3?nkDJ#;~>Kxz(rkHZv9qjk6@m><-7hRdCV?hW_|rPx{Sz}%y3}?ROn|^L79X#7VfZqErBx>7I}|q'
        b'*H=>3bvF$pfRTqupoJ_=;+K#{*nC)%H{E((!uTKa_|vCENU$*R3rSGla30!#4R}CUKKPj=2y>twhlRZ5iJwV5d!j%Y#a0avY}NGN'
        b'$A$`;+cg{Bmq^x6Hy{6k>GR?-@!6Vd&UB0)wU77TK7L?en{^L4ogVd-hkz-QqXLcUf!O<3?iqZY_A*@y1tInUD0RT|%Uyq$+zsPo'
        b'b`-3%o}MmLnOBYXfZ-D_^0a!;y=IaDP`{=Tuu?ZK#99*~%!rLh9EMJJHNWvG(~br_&+q!HB)iuQp7XjT7~+A)PrJ*o3*^8j2mdU^'
        b'E_4^tq1NpBR(e96tl6y=CR?XKdv&7d0=2C8BeWUZc~s?zaNmMB=9v(W(WP5mtMk<A+G=&xi*?zH53Ai77%3hQJ0BO_26P`**Z-I3'
        b'o=f$S5E$DKcPhHGGA2SQ-J_yA8NDSL;b3uVLBn85WbCW4&&2*AH8gf8_LB|&l&}xnH;oTGbrUrSz#gEM0QIy*$lk5jgEDf2DpRsT'
        b'%=^zhdAxt}IH%=S#I@r=DXDF5{Zbknm1KP-Zo;_OU=&4JkJ+n9nygKV7j8K3R$)y;$50d!bQYsj#5CfTt_NVkG{2tNv%}TX<7)oX'
        b'HN7W36Q&98-S>j{3-$3(Qa=6ho#DMF{t00ZhhCIcMm)YVqW8rA2-Chz{__^mCG!UkF<_V+<pWPk?thH=_8>rq6Z6Hy36N;k!`EcH'
        b'_G+zTlIPJQ!W7TU^_*Tbh`pLg@oJ%`FG}nadru5)^QhuIq$g!NOjLvB8W`EE7gXI}(exGqWyB1ib~t!J8ZeQ8W1<xuDk1i;YOgv`'
        b'EtkDRElf=c58u(S?e(!|Q&d7&59=OU=jlS2xM@AK`WI@W(KVW^+qC}EcjGnWfJSw)y8Ekrv$x-Heok1-{Zik?<nSIt<L2ldgHsoO'
        b'1S|xNn7w_Drg%u|{wnla-k0vD#*!vqD}>!QIl{erEdJPd_XTm|_Bmm4d6r#c`JtpPT6^1LV_6xuxOZV6{V>A)7~;Qr#zgZspQJDU'
        b'+tGW*^uHJz)1Eu`ukuMpjzu2U0INNMX*PedcY^!p=n~Y$xB*Xu$q@2042dr$xruBH;_e^oRg*_fxF5g>_h$P32_*~b&By5O;f-{>'
        b'ETmm6CWzupQ52&=%+(n}Vtzcqm~T2)7<EVC?V%+<rM857#n{##jrDXz_J!Yfy=iBZdktpxgvz~|W_s=Zbz{Pf<&#cLIRCWhc3@ba'
        b'YDd)OH};0P?da?NYQtv|*&DVl+<hmlO#9fTA9t=j(l?>L>&V^CjT06v-tZCfrUhe-uZp^7M9*?@Z>YPGvC-ZT_wDG~tKRibkV&EM'
        b'(K)tP?OutY){lL1YMVz3?dbK0=8fxnwtd)r@q-IJ_kO6`5)Jmp2c?6LNGC6z(n61_H~-dMNr^vV#O`wRZ5ZKW$)xV-!=kWo*FzHP'
        b'*SxP7#t{~d7LI-R_}sHX)(%+C&deV>dh1yKtz!o~@w*n2o-NTa$)s+h3N--X{3p0$b!gJQJ-U6LXwJWQ<hkE`etKurrUNA0=-IM$'
        b'+afZf5BrDlWaZgw(8?8NphcTO`!|gRal=<f!*2CYcJmmwg~7wjVRsS+ZH*o4j~(NJgPL36Tc?fnPYVi)8S9S;3Ys$3|Iuh*P~=#D'
        b'<k%(R3VCSPH<A#MSWOz#A%f;ybJUrMV}G4E_CxiyW3jWFZ`b6gDl~^Rr!+0stBaFJYy9(ZuSdE6KFWB15b@U0(S9;^BI-~aEL^L5'
        b'L+OUcqMdQ?kM2A7&FsQYJ~F*9DqIUXk@3YyIxF^G>wb5Xvf1o(^SN(?Yd`s$@kFHY*WTFAF*fegQN97Wcfu96Al<KF!oeJJE|j?6'
        b'AKe|k>7x6+(V^@~$7ancopv~4(VF{rhMtk$yEt^~*M?cMZjZ=OWluYPL8A8cF;DCPkF==Y{RhlsMtY74jP02@mR(Ov`rnT}aTl|E'
        b'r}gwE3Yrg=CacA#OuPPDI{ENfO{zep)E|JcCbWiZN!P);+v7GJ{}<(JkZSSqs(cSQtSOlsk@zIca!>wxkWh29bkAY`3#0unj1Ima'
        b'&5x+NgGpYnV2+BwAl4_y&D*<$x=rJKs{3Y#gH8RiBuqa3t<)P%Vs?|HsZ}%fY<pciJ_G@(r&^Ov=#LzVY<}^dJw5Yoe*WgZcPF0i'
        b'i#jx8Q}3UWpU>`%Pnyx!+mN*3E9vHqhr;@%J|Dl)Q2d4L$=_HV`l&=9pSm3vd6;_R<j{XW8;+9Q>bhKl()!S3{g%<^(kH|}{fpx`'
        b'xvWo1o?J2Jlkvk5sX}DG=)NC2FI713cH|rV?)ygRPQb2bB>lakLKwvN7LZ+!N}tY#+QjToLqMWON{V=F-<~K>e@|aTe0<WxJ~8>j'
        b'<0wA{j*5{{;x3OAb8$2|zV5@JWL2~J`eb*KIwJW?h#dT>^!Vf`VRC!{DOQu@yY{LEACw;7c2-b_{(;Xw>ohX(=*RAxu^w*g=+<eY'
        b'bo~vb22Z9%-TU;ou0XtRduil;ao|{F;vke2f?M*^VeMY^U>G@IG4;lo1}w&>rXE%eoKX#aC_Qp_lJ<SQdGxT>pdm4uF&Oy|q|mQ0'
        b'$NX2NziVI3hn`L^nRx>c9E%+Mi&Xc<#lsQD`pI6E`&O(7Gzt_>5Q@MVyVO`jJ}n}qa1^U?Mz!k$DQ45i&uWHDnWOny67%Y}hcz1p'
        b'(MD?4L}bS&8*)@BQK1^r{qcR<CuLVB=jTMFsFGFLQ8%0yhO@G-h0eY2(eRtoK?%%_4+ULSouWGamE^Y<;!dD5DsEJ`8N_b<C{=uL'
        b'z1N)5*1bi}+&Fsl#?ja(`)?fG1%~YD=*_=46FYiz`e^Knplb9-kGiKb61uPQj9B*}ITJN{G-kAa^5_9ioK;QwCyt)ne$4Z(Tg?)>'
        b'BS&SG#eYu*l6@9(Rs;H=)*Vh$NKD_FFnVrZRL_52C-$lK9WeF0DE4bc5BzS-P3TA-8R=;?PH0u1Hz5I}-#RwZ{Q{L{pf$=e&V6Bo'
        b'YF(R;^$(56suz^p|1a=Gde?@npO19EcM0uhUfSaUwA%t{|1#43$tARZ@zS0RpnX4pHY<M8nRiBxzB3a0yZ(1Zz#3SR5OL;@BS+sJ'
        b'iGBb0MM;>Nl>iEkFl|Y^N(kSQ97#1n;DH}%O17&*mynW~*PQwN$kE@A^q(F%(0_a4|48~bN4EZcBsVMTd3A9dai1F5bniyheb1{y'
        b'3xN0bzcF%FduqbKdp)4F|01F;_uBohjr6}p1GiaJgWpPZ5!Z~a-v9ha{~;PU_%BI_dFqa>FOOLEk7VU&Ex#GLqa|CFl`~`iiz6=_'
        b'Y<V(9xbbYrsZdzO(R`W{N(XiS<0GdgV#MLl<HOKW{r(a60jyK@o#4!!mvu-TdL!BY^hp2Hv=r+XQr)J|x^GAHJ4W{Jpg|z!K8K=X'
        b'UbyJ?jObd9=pP(u$qvy!HloYwu{<_%M^j67<o<rBLe`VCq*I#WKTG@Xm&?^02Yn*$=Og;&k=e6mrAO`GIU>ZoP*{?#F8-q=go13)'
        b'|8yj7)kyArLg;-5)UY1x-^NlLPzj;+^{x#kB_hOx{*I56<CylC2iTgRSy4HHYx4~`>e$VPp`wGWQoDLi#L49+7sswQG-us#ep~2_'
        b'UXKc7;+AYMj$MzG8L3LT`NXah(i7UJ-a|U;>r#HG*5LVPR&+?5YvlNs63BYU-C8cy%~lygLt?dA2Y<BzyDz?975WLNG{--t_H%DS'
        b')(_PUCnCGmVsoT0xu^MvxL9}c`j|m27?^K)RQ1Qj!>T>It*fNE<yxKiFI``k*r(I==_bbMvQ2>RFl^Hhs87$vBS1c|-2+w2?ynj7'
        b'z#8*70csFHdnZ_5mJA75Lc|@74NX~IU2MQZ+zYY!TPKX{pD^<9HfZNVFRFVzWGfjts)7Jv#zQZugo*q5#QjGu3e#r2h>Y7OLUEr?'
        b'ZC;+RHFKmNlRfl8<kpOlhvUH{n3b#U*&%M}aiLl*gl!lDw#V&QTyuV?&Q{0AXW8Or&rGqzdmfoRYgyFNxRl#)LqA1jPF@dFF56PJ'
        b'wc)kcl>Yb$A*HHW3Dc4%%z8$BJe9=H%35kM#~;Zx7+SJmK}aF=Od#xV=w6Mr0y?yAb~xy?>%c${-5YM*CzZw+&CzwcCb-|cSd#6!'
        b'KYeLvj$VKA;?`3ab2GA@57VExsLSZd%AVL8r|HRn1^%15ziD@D-MnmXi1l;GPSk00?%J&Vw9&d;f+Pc$uwILHG`jD$9r|R|&amv5'
        b'8S#tya&uBt8*jV6`S{xs8Hghv;_iiN;cpLz>^dgZEgX&e>LPUY4wDeEMfZ&`<72n($?cw7kM!L|(xZ&&jn7Th?CAgW_1&h!n#63F'
        b'!7;NVV0Dk%w_9`%UL0L`IQ*1mZ^+Iw?mZV_jCP#a@`RX}Cw&;F)fFDmectm=(}wq@p535TK+S}mXRKyv$C<vPyTf8OjqjcslRFNg'
        b'rXuUmi4$>~p5HxjbN311<2cVr-RswEe(UI)7vF&n5H<}S*`s^nn%z;4yw~G-@Pkb~uN)b8jCf8q?vC1cbmy5r?H~NP^zMGlby432'
        b'&?Qd9g02Au)f;R)Z&$~AzDU{n)zJh&{cMJ6Or7G6?^nnC_q4m7yVyFV<vI0+n_*@_j4<htMgT*vUA?b$`{~oJ`u50)KRtF-tUtDX'
        b'OY-{9z*OJ(*RL#-tjDDvs{8&rCt~<a-NFgmemlPN=&7)0Q`DX}#JA$Y&VM1o1l3yK$FW`>B251_L%l0PIva6l>u&ccZQ}2wA4cHO'
        b'v?g9VBYVo`foC(O#wTRO9~0x7vcNGbU41;A#657aI20yfLe_5W0nfSFdxRTOg?$HmtSOLd%zLA|-7yP^FmcyUBv{^siD1|jW9Jte'
        b'2pQDC6bw&xgKiiB3%?P=VZDd>HMm(i`h$z96ZfhNo^!i4NV)T<{-|-Uy-2O2&2JoaLA35saqwO#uKl8*$#I8HAqNskujQJ3Pm0f<'
        b'NqkM}`|F`IpFTXJ@BYObt|RB1Q7^37F=0Yu^zKm4PTkH4Gt$>y*Xb~=N&jdAShKrhK*bd_uySwCOm^29zMV5+w|n#5!bCxnc(0V>'
        b'u50)@`{=hbud~!%%nsfBc6Q9>?bWZwKA<*eL$Z?ZV|s!5lt!4n>u+qIE>5LCbwLQr*4!S}FjLjrgy#O%vWo*#$d)bN?CXkp=;7!c'
        b'Qy$6;T|4vcoew=*7~iigz7EaXt)`2R;Gu_2b=g|zlLgq`QxovEgL^)@L18+&)O`y&V}%1pm%j0+I~_eAEEJ~BSiH?sZ+Jy~=%)`B'
        b's|ZQfB&kE=`>8$K^W!5MwO~Sz^7HM@Age*E`P&5`1?$nBd@*TCn0wa6q?u}XZ=9T??wh>z<b}Azi)OR7?rYrTjBib)o100dxQkoj'
        b'BWXwy3pu?w$`}}8nszZb<hn~jCI^S)KaHEDY@eFv$UXVLlKc|}(oGTWHPU11_|_>jAhO#9Da_RvR^1xOGk=W8spJZLbs;Duf8dfd'
        b'p9H5d{Uad6(3%PzOuf@+g30>s3v&NVW+CSmN9h7X^zU2{%7Vk*zCa2uN%-ak|B!*?*zRX^dm_zrGk%~omZrLC3$GAvzims7)$NQl'
        b'FJq05<=OlOvJnF^ejz9XyDkOo_hgkQe#4r`{j6)*Rhial#jjBPvu|>;x^5ucY)(j;GB;*DNt(GZDg6#>9S)QsIVtX;3&zDNQQo_+'
        b'ZcQ?pOyJ0GoyGbK)BNN@XJ8tdAQ`MTo}ll7=Q0UWHheA-Igg$Tr!SLa_VGa}X-d^o>yu`7G^cN-X(z}1;DXs4y(J*|WSac?(Dx*s'
        b'M!+<>%cO}0HHfEa!8GQ}q`5Bigq&s-rs=#)nwZd+CEkBqD=wUDz%fH6qIjBD|Ht_LXNN!dkdEoiOiA9>dNcJV$=)Q;3F!E>PNfl('
        b'<%r2twZ#2E$VaEselUPH4pNfh=3g+TM~Qurx@>xuVN2p?6TK;u<FYP@0dbQ<hv``F0C8~ACRbEugbkzAu6TENV3#pqo5Y=TK?tY%'
        b'Jhh`Ph+As+&%AJcr;6RK*crJ$?!vx3k+R;;u36l0LHt<)o*C_o3XGU~LEMQE^#Kt(!o*bVz+MT=h0ge>Eq>Ql!nO(*WWT)ED!QKf'
        b'&>eQ6KkNb}jSIWr-DlQb2&lX0`DWKQbc5Ob?eKu7Cty>WU3j@TEbnL+|BLl8B!wbqb#*$|)~|<S)Y=12zwCF9q%XYxi(#;S2KtS1'
        b'NqMu~mBVPN{bQKs`;x}+^gTMBGgP2_qTi(#p#KY{-$i8l&@Uxo@bu_*iW|O?_hbKixc?oNn=lb7DGsOtsy^^5>@Qe|Ck}XixBW;!'
        b'tKJxnKZZAX`i~Ebpj7d=f&Nr?;;?M{#=V4@C#%J@>zM!0Fuh|GS2GNTXwuYc<6aovyd&=U;ocMDLU>QgcHaM6e>L3y>tS8Iigk5-'
        b'Wd8(g48MdIF66oeUm1_`GUkM^^RC^)-G?BgRa@PEuBREh$EJnXTCK35ehp@@PHXZEFPWk~o`rn8R4bGpSuDmMJBLSxS|Ll&3Nu94'
        b'`f5)|uV=crX#HEBI|n??;>z`6>w05?=-!4!ANfO+cvd{-QPVxgX7>Xacs5kX<Nl54AJYog2y=v$JS>8TRSNCGO5B%hc83hp^Q+F&'
        b'??7ImJl);H)F2Y(0`((!ai`fmG6X@UyN2UT!?en?LWbzg#O^LLTlTcnD-@aeJ;k`&hI7<ZMnL;!^em2~je|zsJ`vhiF4k@rn&0x+'
        b'uwiZ6g{(Ot?v=FE#m7&`ys>OpsQ3!BiAkVT)0(xr|Af_W*A5FaAOdPv0hPw^w=q0*ll#Ah=oYlQn)2zQ;R8<*%H$K%{aAYk@ce@?'
        b'skg9mSb8ZhY^!m23)^uF(;J7~CK&u)eco`2Mn9hpuLiH5MGtch(8za~au`4Lh~M;V`PW0+!Y1~0|LMLQ)eYxUdqc<BT-!A!&B_(U'
        b'hmUR9Z}Pm@v*pEOU|v19Euy!PJTYbG%#?ItDq2b_!|t0rwb$dhZ}RoqJYY9HwC!UdMVLC!fA07<V7uBt6%uknM_8WvXe_r>V_X=W'
        b'6dk|0Fe#yeEmGNd<_681k*?cxtW5pH<Q&`)9G2YLVcJZrEi^y6r&s&wyD+y;u3s4@6o4c28(4m#dOhcpX1-SZsU-9XQ}%`(|6Hoj'
        b'K%Ini2qI9Gy6s~XVM60dm}ciT{DbLcD>Ye@qYNHT);9I=3Yg&M!Lgx&2wMF=hhP9TFn};pGjNz}I6V4~hJ<S%Sf~)%_^>we;maIi'
        b'w`jkVAd&bJz0Po8>-$5xjJTfkBf?suG4|;8yZ=0-OONVFkL=UWI@Hwv$D#dy9FlLi!7|`}9ep_ww6)!Dc+w+{1@yc;%=Fq&FJ%W%'
        b'RMql@OX_tW9Rh#vV?@50sXsoH6Aq#L0$TsUq3++wWf)6E_dzV949h4D8+eL%3L|L=)ZhQBA@HLSRmjVIW@xXvEZn`9PN6+R?mcYk'
        b';58@%D-YIwA-eb(WPJT@U#IcjiKV^vsIS*pXU1T#kWjpz&ll5AhI-?vl951kxzQ(w55?~`SbrxqPf_pMLKleUsmV!GVog(rdiT7{'
        b'(y?wZG?B!&r9+bw4@$cYgC9!33#2*u<bWs4-Ghb1t;Ra3{p&RJEr#EPbyEA)>C11~K)#BYwi3F$$0s5Bv~kTtuwKU*;Z0WsZCvA!'
        b'sePzSjkuAHq}tdQY04ck@=Kwizh^uz_IyL)qr_y<y>iHZt#sE6`P}BAWUqVKQ2(+aI^Va%t8k%MGUQu6P^Q-oL1^GgY##Eh#F$6w'
        b'Q1{(5y)ixtvnUJ7qWF?5gpC1fx%-lvX8RYUCA^iddt{B#eCXC+E?NG}>_rEsK3ibjl=0>-?l9e?z91=}fC36Apnw7jD4>7>3Mim}'
        b'0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>|G&W='
        b'vr0|>BC3&)j@8afJ|G71gq$Yy&r;f57WxO)gW^@>Jp23LovrKGUp^0rXMZ=Gkb2T=X>{2g>w@W_WD8Bx;%I2QO!>WpG=S@W5hqYv'
        b'TC4%___q-KVc)v9?!LHa%X@FXeB-IdI+mYRMpyv_6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~'
        b'0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~'
        b'0R<FLKmi35P(T3%6i`3`1r$&~0R<FLK!NW9{|r?d-(8nw{G1RH4iAwee5*tflBbPV5ku{%Cy5`V=Va;UHKvm*L5riIja&r``rLVj'
        b'+<6(YzpBwC8g%gAkV*aX(&nWZu0o&i#?R_fR>i(DQ2AdoR=odA#QB{sPp-V#9UZrDW!ev&D_<f1mq80p2t1+iOn_$+JhS0hQBhNp'
        b'yTsz?uywTLibWkRs{>qOQH?p>Am-cct~R@+$?CX$QUob8)R1;(p|#Djj^vjUE2iZM8@vfgepOX%d6lWKsG7`ev$<St)@CQ6spizA'
        b'6GNt6r%NZTE?1{BckbL4o2#{}A+6EgJ{LQ@)Kor~CM5-x1*?jSYih-sbg@#OS)DBwSR4);6j*KW_N`qNl9!M`@-^UgfO}(*p9sG8'
        b'&r@HaUlK|FBg?Xk@6Loa8MOI*H<Nq}7a`0)-HPJk>e}3*>T2u>=BZkQ?!>grdCqQ!t2;4GuXDoN;3Nsf#rTv}7FS`~;w8Cqd!P^I'
        b'=+g9Qx?D_9T2x+MMVwa0YOA9=5s00byt1mYpoqqs7T1=}Cyi}3=xbj*hVsH8O+iKBd_v<e8k(PQGf5~R2{TDT8A+%l2}?-=lw&3d'
        b'=CaBfl2B7rTU%CH0xnazsk#C%G^(l^a6wf?g{iWzhQv+}$(x`F$%}wz5<HRcOo1l`o@wyJ!V?cqGCT%&a^cB`N2fQW&&$Zn%FeMg'
        b'G&WhAgC~)gsm(uVBKa%xSs#Z1eh{7yAnb$Nvy4;!Bg?oO{H1_hfR6xP3UNK~2&-T`ib(z;P8$qw!4t*ZH^U<j_Zh$N)IgGY+0jGa'
        b's(O{b|D3vB?dLCVeSJZF8Oe_>A^B6GE+>mg{yeBpvBhO+%N5HyfQLIRE?YyJRcvzDU_ixW!g)GZ?6j|e0DFh%w6-<Raao-%G1**I'
        b'lOi@-Y;D%2I2g*srs`TfeH-XIoxbN``A4-Od9T593ZA#&x%u&syp{<edF$YL0G@t$ehts-@SKH5_kKv;oBtJ(w}2E|txaO9y{(B9'
        b'tZRgtIb9Zqi{!W28}AgGtZi18mDITGonn*CX@Q!PqIRpJ#oE!h4pQ1XiP>RquwrDRy`#h0=pq$%m)!xC?rM|WYnbRD<+gU4%PHES'
        b';SO69WD9{%U;`G#^T9Zm!?N1i#sbJvvE47fWdXkB0lt8gq9HIX_?HLyS%F^cUv#bA-sZHrKz8{#{S#D}OCYx<D~=Vmd8ycjZ4=vV'
        b'9sX{}-RrZg1$V2x-O3TIp^s`=0M#--s%4C7nM}3Zk7{`U)p9?o<&0{%OjXlq>u7?`hPQRC*VowvjU%S6wGb}qWQSgM7-UDf?3gDz'
        b'GGs@l?8uTG*|H<Yo1rgjZ{B)u=6Y}LdT;i6Z~l630eWu<dT$YWZy5$}83tedy=53!8I}%9o4v)?Sf5`X<TnKQgX!l5`7?t2nL++6'
        b'7<Q-2+DVog7+%H^_b%s%dzZqDa$s6S%h;QFma{kW)Ii!!U`;AJWS>*CcF>u+RCX-)hAfj^CRUD#W@GY&`gqIa$4w^2O{Rbe$0m0{'
        b'jn}c%>ssb@E%&-A(tXZ(K4*r{ndx(8d0Eun;dMe)VY1o$Ld;7lyl#VkQp05u8))(ho6|*#+wArxIzsj?7v}|Z>Afz4*Ol&d&GWi4'
        b'ysk{IE6eN3_PTO>Ir|mjD@E@sM(-;}?<+{}D@pGwO7AO6?<-92E6w05&EVH2Uul8!!Pg0X0s7zoLvX+)dCUtA$OsO|3=YU5<wb>J'
        b'HGP-RcRqbDp>Io*!|G(qPM{ZRS6~Op-6&RDK|ISIR7Q2AqO7KhR8-ZJks5QESWv!*;Tj#sdX5borvpD&oUO>pHHBiM#nI&NY=RXK'
        b'L_8*S(6Z1~R(%`jx&>lQ!6JqWO=OXEU8ki9<`rGIFqAv1my+70q`GEac7|BJbZ+fZKjyrxs7y4`cRqdd1qGc<RM*)Yt}aU(UFpT8'
        b'3@u}5IYSlc9M9u8gX2t&v$&4(hlwG1sK3O7gyf;#A_7J|__J!Te^B=UKkENEfYAmh28?#VV!&a5n*pQU<NzFjIuGE9fVTifTj3Xg'
        b'uL1lkz}Esk2sje(F~F!_od!G=@Sg!s1N=GQ>43)p&j5T)DCmt?KfpHtP63SS`8>ck0$vFCCcw)9i&!7Pae!Tb<FP(~X9B(ta01o~'
        b'a3bJG04D+719%qTX8|VzJ`6Yo@NvLs=ez|N^}=(2Q4jnS@EpKj14c!E6tD?!1n5twU`_>G05}eCA=*lSi_mTaTnso5a0%cdz@>mI'
        b'0ha+@0(c=Rmw*=mwgE23eg#|sxEpXK;0=JQupNNSfFA~Y8{o$PS7Sc|t^s@qa4q&T;KhJX0<Hu6N5D(4J%E=2{sizcz~2B~j{OdJ'
        b'1@?PbNZv}oHv+yLa2nwM0DLRpRakGps0jZDU<=?5zzu+Z1h^6Kj{!FUegLo)@PmMxvEKo=0Dcs32jC|G+X3$f+==xDd>7!~0CoWW'
        b'Enp|$-vM5a;{o_ytUur%13nLU17J;fNZx&bFM$6)QI7|ID_{Yz3-A=ceSoI{P6HedcrLaJunur8;K_hZfbT}T9PkeSF9qBUxB>7F'
        b'0k;AE5#ZH;?*Z%vjC%fNz;3_~0qzAn0C)@Fy@0o3y8v$k{089dI1Ydx1pGI^KLtDl_-ANqM}*`(g!}|}2jED+I{{Az{4m=8fPaql'
        b'2K)%%Y{0(&oDcYap}hh4mw@X4dyt<1_XEBI@Bq#Wz>fmH2k>KnHv!%S_@{vX3$O?9<2WvWcjLSO`~=z(fcGFD0mcoHcK|;H_(Q;Z'
        b'QC<N472sjOPvdxiT-k?w1b9E-n*bjGtONWE_A}svfU5!j8gL`vXR&^OpF{oud<f^W5SsTq;Gcp21>_&VFJk`!ehKhyz=x6V0sjW)'
        b'FW{E}zX|vV;P(L^1^hAKV^~kXxJmLA;8y`(1pHg%7a=6?IQBc>*8oojd;<F&@auqQ0)7Mg9q{h}&j)-Ga0%d3$S;83#CZ((_kdRc'
        b'J`K1XFxrx90i&(?1Hf-%`n4f>|Bdqn{C~jt0r-zNp8>yv;{f<w90$OE0{m;h?_v7@zYq9Tz#rhe0DKnb1>ipeeh=_pa9jYN!}$&P'
        b'uh?F|m39{>b@r~7R<YG;=@gqmud1x85gWRio2`yGQUf*(m|sqDjl<@$$~GogxVTWL)nu|-tx8a<)tPFwrc|xgE?28V+SKaMAF0(7'
        b'wy4!%18Q~nLA5&KxLQ3iNuwbh8jb2Xjh3!6t5#dux~v?na#&qmjt*-Rsi-Ldsk$^fFEV;6(S{L$pb$?^)y*>&mX@1q3Cczt%|U~<'
        b'`2>QUO70;O=o&A&>>}8hP;1D0Rzm5l?pX;-XJKep2elvzEM2&y=8B7{A4)8uT5S_4WTq=vxUE*OY76al2X``)l$cxE#iEWT0tJBr'
        b'ikn+aR;uJW{eqlKk0dp1R%<8Pvw@bdI7bBY+2TkQU9Hv*rYi*0xzyf{*)&os+hM({3zUE+Fh4=1;epijMjD6J(bXZ|VQ+xqVYr|S'
        b'D+Jry#5QY3i>p<%H#cMMP&H_m&Dn~*>u22lyP90KOgT0U%4`Q)7qql>5Z=|;Dt5M6T<C8SJFia3Y-z?!P`YECXlb$7Iv~R801j*y'
        b'Esz5yS!07%B-EOhh|M;K(-p@lA=1SZBhdnAH5A*FcKPad+MPC<5ILJxa}M-Mn*Zj_^V6BWL)}xD&V%r~DNOG{_{$Wg`yhNdh3P*C'
        b'7p5>Bh)#!SrUxNRie|bH!t`jS4<W=yGo1(_Bbw<&2qn=>he0q$Gd+oNbu`nJ5PllX^d*FY(M)GTI2+CMCWP?o*qViq4DKo1-2m=r'
        b'zL)g_a9_v69|3m^cMn&E<Xz9*hpxjmHj&6TN&dN0B!BpnZ?8<n-)fFEe*40N?+vR|Y=0Q>1Rs%%z873e=~N_=)87<((~a<tzFxW>'
        b'WIQ}a;5l|Z>MzU4a$>q%HVaOjET13o&ZD>3Cu?%Af9|&Ir+)i*=HaZ+jGw+-m%irYlloPi;X3K>E7HtumW~dvmYEC`owmDy5iL%b'
        b'AWdD3DE$%^&L_mEniNsOHswTpn!Z_FF)Lw~2uwDM?vc)-4A*LH>!iE9Ah>c962yd=VnT_SP$ni+iV17ygX9C(+WBp^4yy>cGF($`'
        b'7844@gr#CashE&2{z!}y7l@56N86mWnAse%0&I)Q!t$bA0&|$q&DUHKpD?Gu-eiqWjTgDpM(5%V5L|v?VxiU9=&*I-oQTJ5UrH3t'
        b'W5a3k@Is5r;#${fr4DRJyTuiLnGC`!Z17mtLOzos<^YIf1=K8;zH4etwMDswRf}u8{rsk2e_3TW>F(|(^DF0?u%~Ei3aSdBaVzL{'
        b'GIQJSgh;EyVRz(0S(75Ft$0x2m5*s872E+qWM#+7j>;-1Lo|u4XreI*XKzM%N2QU&-qr>qY;$^vL`yU7;Wf5eI$E%?u2zV2vX-Yo'
        b'!3jhJPOz-CIomDHJE;c>1u5FW+%{LU&Dz$K8{iYyw1RM!v%z3d$G1|Pv@TFF7b7V%gY`<ySAyF?*ea-rH5Xm5EHG?Y3m7{A7=dlU'
        b'!|11yaANClSzD|Q(%fdZxCmB^td%Q49F``Vy`jtHvUfO%t#kD}(rIxz*Vr9R-fT*$s}`Ga^s1_Bb4h+J3=5iufKtsQJBw5nRaMjw'
        b'eOd<5!BY%I&7`AXW6c1W_A=N~fc*v@2bLZQk+P0vJJi^FG(?K%IEtju+R%mm73S)ED7Lh!0!O{Jyb9}Jsx|>vBU_LaB^i1MDj_)r'
        b'jL#+AnW?%|T{ot!rWDmi=)aOIc(UO!=<ub7R}OulHwPngGD#W@$-!4PWLbc8IR<!TX2NS8CY^_|^U~pk#ljl`EARo*3P@U!j-E_>'
        b'L1`6`x`HOj!1#=Gd_i8dL@Xv^4Y@g$%t<At+JgCdhIFZ<xZG4zN{XR{q^QVTT~$F=)D>0dq8v#hE2_-U#1*EcHSn%1T7ur9%Ec8m'
        b'snxXv`zV!ERsm5yI4G)_Ps|0Wq`EkjRMn)C{K8aH1h~Qsid4C&wiMHu%OF7!o~Wgg8i=eZf>hPDKvrO?OeHId%c?7un5v6%`9TAf'
        b'S~X=Qm8No94bTZ|YOAVEB{)LG)kQ^OMNvgn^)m1kR+nMriIG&4-Yt7YcxuY3D!uU{Gz0vYS$>tNx)5-MX(?n{WEQKDVTf3IH!an)'
        b'c&S*1EWo+4u&Aa0vX3{lSwJ;FafMT3HFVa^DA-tV1@8E?$T7M(zL+3^7f+e*l5AM$WpZH=L79|-TnBBU)7I$B1ux{*-VS<?6Wy}P'
        b'OobvBYB1cjMRi4$wb=afvWhZv<d%}$a>n%-%w>8}B?>&`Y8ahdQfZeJN)%EpHYbQD5O<hqMHLJPj9DcW0L)u#T3n9vqrz-=0$Re5'
        b'shYkpxFlE4kdAa0qPq}Wd87<A*6OYfl4}436b0Bqdkd<fRziC*mm#JO6V!}znSx7CK1g?dGn7!?0k6VZs7!Zp4Zh$pW7v{{D*DF2'
        b's?}H*cxoEqRSFN**NhnFa(7t=d(DBm6)%z5k#r{%Ky7b@c7wWKU0PFEURzXETp`{jie|76UYelFKMl{hDXRQWZ&2mOPEzHUPFCf2'
        b'6WqU^+ulyv+vnnTH6W+8@jnct$=c%Q!YG;&JY+TpVryC}=82W7K%!OGE;g?!FRLsfbK5~xrDx1@xkPuSH9}G`Z$2a~fUaq>b$~`%'
        b'vko$BcalraYe_1~G?^9*A4}7!MkHI+1k0^2f|^{HjiDq|#qH``g-Sy(Q9vB-_p>7$*)9O~Znrf$?9hHYaBbSk4p_)-?Op9)&vaTL'
        b'1kV?7VFE?F5vBx80MzPXDFm&+)@W&KTZehjr3;rQTvPR+iWt%|(s0$SZS@w_3X2-3;SE+<eG;1;_I66jZ6}f1f0#uEE|eX(zNOJ)'
        b'2gn@k3G3QMJbJWrLS@$4KohY->H2v(@y^n_)6hVL^;mSa+CksP<4HV>w5($}p}o~fmvKAP$0atc>##t>*@})widN8Vto+E5+HU-4'
        b'Bu%WNl`>>xh<5^)JK2ebd}IRZMp*|Q^ReZd*41fi>9Djp#bj!cK>O`$QUa5CcXPi(T3!+P{FfCg)1`?OcBhNSImIp~$Od0da$=^^'
        b'V5@AHu@eeT^QlB-&6g<$ItCOau9P?}?bg78fh(Zvmm(iPnL(X^IuSn#vUPNJxxAGPNX5)L{{+cSXgagNWu454Cos6}kEtxH!A!I?'
        b'*xGEabx{8$IIi{8<_ce8E*}HyT937CL}`V*1I$~Ij>>t(JPhZZRihJ~U|~Wkr)WdPu$iW;5pNZPVmjoKXH{F;DMzuwX8D(b^$@!{'
        b'X&%(wWM2c5#0K4nsVr@cU1%Wl8IX{kGmj=s$VksY4Y1QnYt^>y-*FAKWO0D#?B!=|I3P5p1t%mld9BsyH{7+T$9nky?CQ2QoRcuA'
        b'+H8;-Dhp~SGn8SjVD7%ew7RnLnvf224ytMcr4qyhT@isZP(A@kV_R1f%MK)vs|%N`PCK@QijQXQ6{$|$;bN1tmF{;yU4bQG1rnWI'
        b'4V>8Koo^yNU|fe)_BPaMYwv86Im)*q;MZug#o<H)&V^z`ZZa*{Y3;N)m?U8eKbs4FRi-tj{0==p%>n37CT&__jx}3g0`j#<WT*W&'
        b'Tn@UE2Ezhl(?xj<Mh7YdQ?{Jm+hDTJ3DcA^7IFyB6>Csppv9J?ixx*CX4{BeZfR`n0w=WIf^CQTpehfYPR*e-G2gldCM{YyFk<UO'
        b'uuPz(tRU<&D_F6OF0qqstynr5t@3<Bj%aKZyU^xiW5G7zXrUeJe0wKYDJqLuuC7)K9m5W=wk$GdI9X&M^YS@*d4VSnlm8u(RIy5C'
        b'DHPtRViCPmf)!v}Km7U#ayUqCFaPlZQUk;V){zTPwywd@2iMOI#y%VDcF?W9i)8j5IHv-67v5ZJ#0IRfIoaM9%C5_2!}k|2+cU5}'
        b'w}I>cIbg$$L|_;*aCC>uMi*PzSj1FRs>tbZQt>9YS-(q<(kk*!{om|B|7I|O|9{vBXJ9J=3SiTluRlTg<I?fnN`RC>WymwYX>WG1'
        b'R&YV?q??YYAz2z*aX*I5ZYI^KvO%p1I$fA*0xO|d&GrwRvNR)fweU)>_I4}GSSoK?Ep09*7Yj5~lp1SLLi*=yk$aY|LR9l|*jies'
        b'?k|?1cy-udQq#*tR7$aOF(J%aC%rqyGxB8t8W|WjO}@sr`fWA)wZXq=E7b*YHQ{QUrORapC5&r<c;BOmid?oZ7s+cdy|P7hf<|r|'
        b'`LD>S0V(8aKo_7WXMzg4tzn&*P@2aS3wpQeR&Qp0MVi`B>4DI$z*Rq$)f$Bqtz}Tn`EtUd7&U~_B2iJeYQgnY{BD|v6OFYDmm~{T'
        b'g-TDxSKcjkeko3@=bQWX4w0+q-kqoVG<oOWX$9$z9Z$3Ljvv>^sZ3t&rx&E5#mPDncb1?umH|?9SX(SXso6z7D$Ow|RG3a2<cvU`'
        b'!)k;4aJ1tj!07>PweUT6T##H;RjILB@AT#dEor<HvTL?cz7EQeYui+aw$as)<p@pg1T(=Jq|7rtzQO8RV})U+DV%5}_%p4n*n4}a'
        b'$=U!ixsjeu;QHypu6N<0ColAD8qt3CwG(7F>j9f9P2|Hs6$U(`K*`~qL>;qS?9>G3QAt)hE}4PlB;&Aw=;#z1z)ri9o)S4AFL1yb'
        b';Af1{2KpEoSp^kOlnHHkk^#$XhiIVv#nxTir-as_hSi1J4-gq(#*qr(0<_}fH41b}oCkbj@e7q8#F5SAG@Wf-Ew&CM<|g3(4)G<8'
        b'NJ!5RlW`@)D~Gi9DRjoQf-L2NginnYL~KE9wzYKO9xQ10X{6kOx*H0(+yI5DL_gOsH{ClQ*)Y*b4uX}Nef}+A5`ikkP|b1+mc??V'
        b'vz3}M$W|p;sbWcXD((?7B`hZ^&Hn-!sKGE(@fa^K7_A0AJRK;z8d1MYZt8;7ld@<^U~+GNe8=RLwf{c3tc|Z}wE>UHHZ1KFKiT86'
        b'h>>+`yhc+abcTbmq!Wt(j$UnV>tez}UMb=`P<L#Lmv;oH5Nj3}q>6F0w|<0ujPn2srX_Xa0URVrm?N7GI4xk*P=`SClh><>oj$^A'
        b'9o0y{4#6<l2%(0ei<_~~Gz-+7p2muI*js#D0O{rRdX3$2r?b-nGm)OaFwu|Jkhd{VwL85cBvqEczHoU_!hR~WHq%UL*U|{8{qjYM'
        b'8?~H{E$V5cva7uTF9LgI6>hX!(QM~aOiwrQnbVM+MofHprI&DFpy^?!EEIzyx!HGxSWsOYSBz}7cR5_GUTKS>2zs%FomyL&;nt3#'
        b's@+Nl61f2y(B;C^xXOO#)Wv8Yedp8*VJN-wli7AuJ8=5dFenvYOuTD4<?J;78_R8T@Zumnjc)70O)4)f)}%eHtfSFkMQ%j%l}BBg'
        b'!CX#^E0);oT{>wNxNDe3%>G;hi#iB2s-m^Gr{al@%$AMbjX`n692osoOs`B8b+`NSpk}4KnzFq3y5((<U&-vwfmb%Ou@2Z(gVof9'
        b'Q?|unX@{wfTQ)5nNJ6Km4H}w@ZFhj0fL9ppwCky=4aJldmKSm38S<sl(mSM9S7VxJlGSOJo!^NX?)uT(=mbuSSY(BPl#MNxCFl`$'
        b'Fe#vXJCjskcv4|1CxcbjCxM{<F$)yjz}8fg!Op%Dif!tm(xF-YeFC@KQTgfuwx_!n-bmzn6ihZ*+ol>c>tYKO-NsJ|p^!H3h|B#e'
        b'7lk$nvyq$TLK~TqBL{vzktDO5b6rQHXf7+H0-qk^0T)18X5y1tW`jW0xMXHqEVwbr=8-(F{%z7G$k}T3sS3z!Y2sqsSb#Ar(Lq3`'
        b'jWIcPbR*c14hvH=7t1>@+<584b8^1BiX+H3YT14iJg{0aWd;-!Rs&zLY_hPb`er^36&IOI;Yt$=Wfhd}FW8#Aed_B^RJG@D6AsI3'
        b'^;e_4xkKSq>^h9BQaa@+gTJ@2b~uqM`S|#1KsQPF4vfuz#9(4Ex#qHC7f}t<DKF8eN;X+n+nByg+r?*LJKZRxniW@obbgC8+XchU'
        b'<VL7p=1hHsVMZxH+u_s0s4D3clM~W&45@5u5p9@^^qdsV=X$#F>9E+GR1aeN1h!_r5s#WSJLu*$f>60A`HB<9*rDTPp<PKe0<Rh+'
        b'O9sjy)STkCg7CTxHBmaOYkXTuvc*MJ$BLlzxr_^Gk@P+jQ{cSRsZ?o`OT?DaD?;)OA6n$)@)eC@Nk&du`oGWL?-~G=ev~ZmGSQ`t'
        b'T>PCXW%4dr|8MGLxio)TZXw;lk*!a8(~gcb7M1K3->_iXK?J3Ew@mSx7g*z##ye%b3|RpTDI49C@$M2b4)yg%{N>sZPj@1KyJ=d8'
        b'_i9_Iyfx5<l60Lf-=@n|+$Tz8!5g4J_&Pxz2w%OfW&!)x7;Hi(9X&rg*xOzFYTb7?g)fuyzc+}@bkzq2amd1nT^C^{C%u06?=z9r'
        b'grI?{$js$70k^<pVPbRg5qH{|vKw$+hI5CQOdI5~b*9kWDfz$%uf6zcRFNsKhp9Fu*MbV7dsnP9&RYDZXmVvK>lVoTj_l$>?(nO+'
        b'-;}{EbbrnP0UX3*e!E<Lds@C-EULHiBL(PtDvMCol%!{;&4Wd39Y1l9B^@ek0ZdN{Q7G`OBYFbLwh(;Q8<+(&8drL@0$z!zT|Sic'
        b'YNuC7$7h0HI<}mEM2Gz6I%GYu8Lzs?tV>tzjyYiK0k=?P+wQ<AkX%_;gPYY>stLN}p27=ocF>*HrBeOG(Ft70mNzGkmz_>%2dE3H'
        b'>4y4R-@PfPp9zi=hU&pBIAiD!z<tW4%oi@Z?<|e7s?*YJ1&fzyl#mx{6iqm@gVa1U#4gEI)+gzGS#~e<|3a>p)-?^*O(52#W#CD;'
        b'&PkVY?^Z-tCp!p>m-U8tvAL_Gk?p?It#+3@kLZaZ<h#aVb9wEYOBZpU?nr+N#7>6zuA;vUN`E)&^zI)9TyDgp4d@EIhsXpAI<R<t'
        b'2<Cric6o(GR;p}xkk<uv9qqEkwFQuMGo@hHuEk_jSGXKcSekN~OLtW9cCqbKzQraM&7nsXXz?;}K*}*QKV!<tu34}f#7-)aZB5Lo'
        b'^B&v%o3W#(aR2|0UeLA;FN<E7X!UK(SX?g9c#*<4q~%40HB7B{*g8f1m7@&4E7jDrq$>vY12?bj4rZ8_7_$8(E+{g&D?9M^97NE4'
        b'aJ~($qoMF7sKr2bT`;laU%>gZ-z7H#_!dOK#egeMRGLrlkff0U`N-cAU;)}Y0yf;`jM=$0zu>?x2SDCzbA@g#uqy^>BHmZw=Ul!E'
        b'E|w-(Reoe>=SzzX%C9fBt)(U*F30sUe|bYNAv-qbY(S06X14DIO9s7((9#9W!0aLju{h|M;124nYAg1c2zHzU^cG-wegHoUcjRbq'
        b'dJFPJvR2x_fN|KUHY(FoEr^%KiufLL9rLL$m&`@Q%W}o3@0S9!!!Frs^xNXb{E7b_HH)-)Z5BdJS2;2>BO^V-pPu%ni-q_uLhw+='
        b'W5FZL#x&WPBFFpPNpZ?ye%DZ(z%8(rHR8<-QsTQjacOz<U{^l<rRSzjzB`fn@9(3e%7>b5-hFMDHJ$vRHI?sjIN0qH+@$ckiXaze'
        b'mh~FH(@CEsOwH%_)p2_zwHzZms912OQiV5(+nr{9JHwi~#O??XrA#qMl@GU^sq&G#oWkiX1Gg)nB1;OY_$)~Ezig4pZeDtCa-;^_'
        b'>yR7kcl!f-hpH}fT=qFF_SB-aE<9~+A`7{c^;y$oCW0<ar_&J=-ja|lWYBZj<&qA1t-<OYZ271?kOgFE!}!G;>=pS;NKp;E%llP}'
        b';Jkuj16VC6E`a4~{7#+uZ|X}?ga!t2=Bn|X^?JDoXE#&FD6<CqXh`;4!oWP7+6PwOW~R4C0}mhpaeKxa9(cyaXK-L-r);sv$|yY~'
        b'3qFj)&XG^RE`Mr8U`k#7NQzX@L+@tXK4e={d@CZ=cVv|6JLkFl84hpr<xg@5SJf|naC7<d8Q)hGKtke`LHY1M@FN<*CoE#J*<76>'
        b'Z*sO-TkxJwb**<7@iJ!}-pyh**qliUt@1CSKozA!Zga^KO+KIS?qhN;4%oUTOH-GnE|*7>omddPA)6f{@M-FQG7%Wze<~3e<98wv'
        b'l$YOWgtsc*eQqDC1jkU8ltbAjIhn&bc#d9&aOsBnrJLoX#!vs3MJ&D3EYH7U-<C4dH%Oom=i9-UB2~^_W>s9^FWK;BRz)gqhT)2V'
        b'i#6x)WZXRMbkTXuGOw7ILW=DUdRze<KvhWk^EWz@a&-f?kLREY92i!1nXtmkgvndaWo*Zp%<<o#_3b753E!DBd7^f|on#(l@!K~J'
        b'O2xm7!vdSU<}6!!$Q&luVHA0a)+>mtfY?jq)s^>X>2-B^8-|JpE<1v^3RADNcbIyW{kv3tx>AuDP)_g;RY2q=O{)#qC<<y>aJE*T'
        b'z`Z11W|AxJ|D;~JuaX+H0fMc&{I0{5_bjfwOW~bAxDA2A5`WG>mu|nM%=bkXzCIMlE43U@$d9<>U)l!!V2>HRL{Bw@E^Ip23z+sx'
        b'*zbOWtxslY5_(caJEVi#RI91L#-Em5$@U~T`1(|Q8|XV7q%yPK<SOE4Nw~GfJH;=^AP3RT=gWGFo$l{~0QPnWuBx;His^n0H+<z`'
        b'<_e6@&~gTTSBnSA!i^_yzf6*V9|>QD%0B^NKfaa)WdYjn{G?01&D-qbK>Rsno89S3W$D=LcY38Duty4y;=6mY)aIc9$8z4!8*zo3'
        b'^-%_leoa?{16B-Fg}pj72s6CW(o7F0Vc>BKyCNqW)l;6<DYK(Y<8Sq)Udc+MAN#UghTSmSYaNmF?0Gs}s$QRA0Axtlp>JNME*nrr'
        b'Rwl4)YK}n<80r8FS7HUehCB)aZ;Se7m^?XTCJB)0{?dRi?D7gCFOYNn7C}5<Z(-I4?N4vNGSirvduC?t!9tE21C_#L8AHn%GBL#A'
        b'w8(y2y*G~it~xQE{ieD+p8cMBZ9Mxe_3WAKchu&Y?6=a+ne6w|y$S61(s7CGx6(6`*zct8N@Bl}{#z3Jee{A^?6=W>nZ<q=Jvo{E'
        b'CVE*i`#rRn!hQ?wPGP@;9!z1sfi9ZOe*gU8Z1&sdb*b#zGk-~C-=3K>hkbkI?m6t+Gsow!Z_mt5W8a>+J&k>H=7lu&&6%Mz_RX0M'
        b'bJ;g%ChFKXXX172n=`lR*f(c-bnKfmPwUt>X9jibn=^u*eRHN?&%QbHCq4V-%p?Q*=8Va}zB%JCuy4-%#K68?ve&@AUGfHC{GR2<'
        b'fbol@G3g<B_~E}o!1#et2VnfF=nlYH9A^W532+YJF~GTi=gtesy9LJqa30_%0MEzYnghNS@PB6DHvyrZ8SI-kf6idvya~-@-;BZE'
        b')UV)pCCB)Un6^yz4Vdkj>>Dt@$z<Pr83eo*zqOIYzLl~vi+x+<Pg(4nAUGbs;p0&Y40U66NZw+=vvNZ6>Ht4}OGw@lz<&k26mWK4'
        b'NZvBQ_XA!I_%z@ZfN#AO>I2vb_;$cQ2iybr6~JrpH|q;R^7;VZu>ijTO2`qwn*hfcL-Otiyc_U;0{$)FzXJXY@P~lYOd)w60WJmn'
        b'cfkJ(@C;!1w*XH7+?)@51$YPGX@H*rJRR_xfHwh7EC|W_CE!B9{eW$N9|Qa_;N5_a0X__PdSOW3%Ygp`_%z^@q7WP&g1lt}x4DST'
        b'qkomcxUG48f&6=X<3d&b$IDa!zu`xk+aY~>5u00oFJpP#UBu>Q?Nf|i1~sSY;bm%reqfK~oLHdBZ>{o`qv15$z6Xt#)9n5pG$FjK'
        b'6W@ad`w3;q2b>1`WMQ_i%}66GQswuURr!xBVssNY-FZ$!E>ljqDUc?Nw`at!oOd&P<<NQ?18Kr}Ia7-n4fcI%v9C;|0mcuYiQsv!'
        b'FZPwQGnj_gO%9vL(`_yZ$$R@I#yh_(@zG#E>Yfbb1A)`*xeCp^Aeu>>=1|F%`^~i|ux{7zcE4WYYfojSFJByssY?R;;98#7U;Jop'
        b'^rON2J`Ac`B=75Q{b*7$1IOoMzrI%S@4#YSlS(gNH>CMsVPM@R^YEKXFVCZz%kbzF-rpsqSLV?NgUX5Kc{P?^xv!4|@xgVRW_78L'
        b'-!}TuV_&!C2hzlF{yFGJ)0h=FJ`a`!(p=AJj+TD+c{-KT{0V6O$ocI{zq%n!YFVIso5pD_eh-@IoMv*FPbPj`7Rc8pgJj|iPBXXc'
        b'@^gW<XGvf=v3wk>u0VtRm>tBUH*gu!R2C@X>GxkIFx|==RJR*BUv~n{hO*1g(_vnY%sV%6noU=s84aQld3!v(uaJ)plm+%dUTGj7'
        b'#PM=|59w~Xft52@7T5>mslamLInAe#PQ8%Pd?WWkY$)vmZ4k{&P7|^4$~0j?GzpwWyb6sFM3czN%3S!}=XMe=r;5`cAN?b!4?gkh'
        b'YwY7$ysw=LFF&`joNt2WX)>3k4_t-j)gYP_F0(xgeRKO)3xn2@f<T(toaU2-K0X*)7}%cnARfJ$w|k7Ii{Nt(zbi6v5##GKK{TnH'
        b'=GsNyy|3qRn&j_6lg4TCzX#1+PP5`W(8#=#&HJrukxw3cT^iVL-9dej!)bo9$S2=|Y1RhO<Z_x_e&rkl_e+a>W84`;a|@?=^(y7K'
        b'f@tzMkN$DdmHDkch<E1maz0+<TjxH@2wb;&g67<<Jl*J3%6X|EaBW<`X~N5W<;*A#<m(TD>SpBWHkDtw98X~&jft<@KldwVEJ#0i'
        b'wJ@-5%lVr5B&Wf??hjfQHuFB{X<{@hIL*sfq1h5dvy#)ieHEGqgJ@Q9ntxn{=8+(pCO%iS6(M=uFqTLYTM@V}kfpx05&Nry)1*MU'
        b'pKzMs^)#4fEvLx?nje2hnqE#*1vC$RN18pHrm4a=e|`Y&-U{~pe2pIsjw#X{<TM-n+T$<dRhOap4X1hRd(hPK@2wrHxOB~u`7OEF'
        b'M}uK#Kck&-w!$Z`Kd%U+`KC0GN9#CEQKhdBz6>g7X;EM~OE^tK<>hrT<el;$onk4cx#uc0<{+A7oaT|M(9{OeEax;YRr==X>B_+N'
        b'xQYV%0QV74u18e`_Vp`=Lh@w&;7E|HTFGf<Rb5%<I}t>4JEt*Sh33^D8r;jkHms<+vaIS3l2y3xfx3&c%GU>Hg6-3wKEOQ^l-KtF'
        b'&2hC)AH{Eg&5C8~_PtL9%I}SwX3J%0WF59Ih-MS#>noKL%-2YBKd0%h^6~Y%tAk{3X`ns#pS<7pSNU`?+z*L|GG41<b<6kD$uaF;'
        b'In7Ck-?od{3ph`a2apEK`PAs^YxIA_Y0h0`d_D@=KN#dZI(8MB=pg;=@4TGpX5W|^%z?bq6tr&RJ{9&`q4~=F_DGOCz&$OrYirGc'
        b'`WyYG<<A*z2;$LcoTlX}G>t(txL1Zedbjz?JbEsOM`!T%Y%za#-od>%%zMDEoSz5jA=aR};l3T_^_=;;>wLJ!7jl)kaJjnuo%g{T'
        b'-=my=aGJk=51NlTjrz9lPV-Mr6Z<`A9^-wTd7H1V3vUaQy;Fl^)oxzS{@Z+WPUfBCx3PKp=ODg*iI?++UpZ%k%L&pG4|5uIwNE#W'
        b'st()_=?T&kabFf~pseaE%Y$fBpgcIuX{xGybME%)z_q?7XwJ#70n*hkWMP=@em_6fcYAeU8>dA3%E0k?v^r4V+3V*=e*AT{PuIit'
        b'9`=hzdGv;#AKUszKR@auXZ`#r_Xqv_Xpdg-^W&JRYJ7gQ!NdLh*hf=qeC<QKF@gJUmUTuyKiYdbKR?=XS$=-B({APd>mM4?M7%RI'
        b'&pugm%c+wm=d%)<{JvFt0@V4^0`{B-_uYUm77&k60%82`tAQWV_5AL!MgQ;PeWN;YV(@BkcOf%c9x3vLo#1?P<Q`wxcX5+z>E<=@'
        b'pb2EeJv9kB<-9jqb**o+#&d+%F`uVL&IR1F;QN2^7ilmL?03<4krt)ZT$0T1W5PE9OKXDm5!F{IVQrf#|6X{`XK3?3hG!TalBo@t'
        b'Uo}P5Wu|hmrnb7sR3VxQYRl@1NNrJhWl?QV;F6;JnyP|DmxSk+FD|OBs;Vsw3O74!?Rdb9A6NCsO8lE<I(SNXJ&b^xHmmZd0v6}7'
        b'XD#@bg5M0!|Ht0D0Jd4x{o^NT(#uw$V;zh!;Mv$lJG$O>X_?uYq)FGfUSgAO1IC+XP1*+9BqZt9;e-wb4j8%(lp*t_A~$u)#Gxpt'
        b'6X)xSTm}xEuTv)uo$re}b?R`%{yyJx&XecKrCm{9|G)SDBipy1bH3+(ea?BF@A)3WT1n*Ak(U3IA6+EyJSuDpYAGM1`2{p=(YYdR'
        b'RMysQ+T0=)ucfJ=6JPOJFx=l4<TA)4IlnH%1^VMm>fSBU^z4@E&I7Aa`uhh$y&)=jR24!c!2t>?j?St9%DA*!e>fyHj!0!KBr?F}'
        b'w0Y~51*&?u&i+`83oM8Ff}|CbT$fo~p4QqWl~tscEJ!ZP5rD)K(tRf)-N~!Pq`o96$f!C+Qj{l2A;*&Ds#4X1?x=cHlY?Y)8j&QI'
        b'#n36X;Aeg*lZ|?zdex&&B@XxGX@iSUArnv2)<Ejkgdc}i6=Qm8^LUrd7jcnzLWPKvw1g#3)2ZI(Xx@@1$um67(|Z!VLmsp5rqdK-'
        b'1-m?1997<ft3M(cg_Nvj_#+o)GgNMs1&!)NjoJH29k->MicB?0l9Ez3TJ3c*mNJo4f{RP)&v2(6I6G(3oXeM4!ppUK75X<wV1$&$'
        b'@nhBsJg_+_zSOfT#N;6m5zNah+(I7xaT4E9R0dbnBM(TyBfQViV$(H_JjqY)%d(~z2qyd?sTWX}3pQp{baSI4Yg}<emQ-|`5uuc?'
        b';rf+?n5|;rVn4hv!GTbM$-_Qs3pB1_jaReAYgnVl!=zwL`tfQxv2d;FT84Tw4ZA2gce8No@-#n`N$J9*3SEzGmQt1HmMJ~`eSQ+b'
        b'^ar>klj^rIt7lcbUi04Mme-VOnh2P;sf~$~5!#8+n0gZf_C%|hkfh`8{C0%o<jRG&lu%eGR~P-xwag+^ov72*y8cjafP0cUP?+mV'
        b'HHM%Rk<Stp!zj{baiM0amkTzvRN}vGwD7q_=R<*e75<OsrHVOix;o>6sd4aDWH8GVQjjn8$J6l&T}=y_FiHeroh!z08ZQRfF}q`t'
        b'{%AbYfo_Ujk%fKsDB(rb?5O#2&d*XjeO6TkaUyM14LT!L>M8wEoYN_xM}MipPnEGI=PI?idPxE>RX3m#T#t?iU#@1B_Ry1>Cqg6%'
        b'>|mZY{PjpJ-=y1{Iaar<Xmcc=RI<jpdi~vEwxEM=-7!CU^3Y_n#r>$kPRq$p#Lbp3fC?WLYl6KnU(sx~C~&8}`Y`Ntuj_qJh<#~E'
        b'0(+etvt|3^!hR6;6NR~!sI<QU`(udzzK0BUT9-YCc$%^QR&@6Ju?Nl{((G22YpH!)yqmeG-)wol5c&Ip!A{Fj3+$mw&6cf5pVlvh'
        b'j~VPM!Q1qNwuWheJ*u;R0QP{+UixFRWsT16h5O7Z1HbQg4a}FIJeEg9{@26)HBjXv!u{JY{}MDu+E2nfZN1sj`>4z>%=1A9J}vC!'
        b'FgJppk@hB-ixEGQ^>ZEUyFo*r7V$j<^Yb7J?6mh9MENd+{}T@j_y2&~k3mOd`}`E<zkv=)yJ3UbG7FUWl<+?X=Ea~MX}=2QrPz~h'
        b'llE(1zY#Pj?fo#vK)a-UH_Uqtxt7z?{xs|dLC2;2MVQ}09UPMO-@!g@z--wg?bBht9QmJKZLrfmay#1D0p9e5!hRI?X4oI87XCdj'
        b'-w4`PDf0vK{h(vg{vgaxgEm!(_P3yZo`L<DA<h0Q>~G2VH-Z06*cW|D*dKxYKVaYgn5f@fXtx(&KRG1ge-&o!G!8$IxsLRO=rk}k'
        b'%f~}fpq1-BzJc^R_HxzC{o-_KKUbJWn#t(k`2tNzV^65N2cBa=p%E*<PlP591&Il!Tv@SzrWRG-iqr=r)U3qQ^iyWZ6CKc|Lx<&3'
        b'5x!hR)3IkH-7jxHDi@Nw70v~Gg}b3A)GO2*31wFQGey-d04kSyU8Oo%c}h7r5EVz7>Fh&@ufA#Wl*eiL<49G+6O@_&`DrpbrmyPI'
        b'tu0@u#+q!oq|>6LX>qD@%`909gaSMknwIGh6J?Mz`b0y)&R|kei_lf7s(6tnC%U*U3w@pzCDlBNB<Sd=R1%w_*ic+J!%wrO_}3p='
        b'AwQ%;3F#$|qUaQQrUrCNY5ru^`0Yzv{S6nX)~jknwqm5=y%WoyxOVoYt4q=Aa^uUu4P3=|T3Ypy{$5dMT>V9g7D!oN8QOW$lho8B'
        b'lwnbtnG-c+S!Q0OdfPajwRAC*B4oz75@UWdr_5{e?ij^6K-vYh77!<`l#)4(rKuNJHR(&Ds#BHm%g!l1^NeKNR;8Ol#tf8sctt4U'
        b'87Ihil`juwrL=*nAw`Mb*zXq`(@^|h(K2rR<>eW7mzV1g9;B7Z?hhn)(n22<odaBl)t5Lkz~?HjR9QsYdE`wVQh}DMqLn5Uv}!Px'
        b'_HIE<y9MS|sxl0ZstiM1&mwY&J$yNnCt&IDL04~NL%DbjW!fa(Jr8UW?|Dyd5;C-%9}@EIfBTSl$KP?YxFc-)%|gC?_+}yRzW5d)'
        b'=l-o*#CzkP-y-DPFCG+f?(ZKIa_+Yb3OV<u28EpawVQ>U`v*4*Irpubg`E2nn}wYF;mtzM{V$t^ocpD>nl19FLO1`!xoS;Pd`((O'
        b'q_SH+Qv6b#x6&kdG}rJxMG8nsS*XwfnKD`HB33VTh$(#K8|u_{(S4foaIVp-oYBQuau=fxJvBLcYIKJ~HwncYQV#=fEmgCvh!_5X'
        b'q4iQfnLn)MDXA}4Y9~**T~BRPRpqP9mhO!WX^_!W4yB!JSNi(nq~ihGg`l5b{T@>=r-)<t>AG2M+8&!Wm1?(B=!DXOSn~EjKiAeC'
        b'4Cpj8rR($)6{glyr$0=2RyE_}vCeP7({%BPM<<F#`us50h2#CC{wCfRiO>~+>LFV75#p!&1k0Ih%cM3tQq3tA4E#Q3)iYmMpxE@<'
        b'g(p;=a<*B^oT>_&CK-xAPPP8tctpEYqZu=cPLC+PedJqCy`F8^&T8?wyV_fVVjfq!l>Vg$vO;=%lGk;p`WmFtI(}MMJ%_CIGX2w5'
        b'T<|RP<jJQlWk4uR6m`rOD?FfG+qny8ZU3wmM%d&DIbL5FZ2Z)IBq3FE2%VQ_S@*qPI~%O6RYUwBqKrWA8jdJeEW1MJVhz*!Fiy{>'
        b'p3u4w6|I}Mx?cINrX5wglcQWc>?NPDeCkXcXskV)tVV?&wG!I<x>LH9m`!NW$KSxxl+G1L`NLe(T)Jnj&%-bDYG9D@oqt9YnsTom'
        b'*()}3oqtkWl+g7<N|d|!+BmJFCnM6z?GG#RUNv<N88??)W0n?}KUn!po1W3OU^M90DqT#Q>7H65V@Dyb`$$cl+Eu<B5S1h^zu+on'
        b'lDR@}@1w;`QbmNOU|Kd*X1&Def`qu3A(BTYMKH=-IX?tBz!%0@)$_z;$JPedip2|s{x7cnMa~VRf|9S5tJG}|^+K9I$E*gv@()MO'
        b'RtNl=98vO=dp44Kh-k%y6&5`VN#l8V0qIH#YW2^TCzPXPQ;UJAuQk$0LAP`C$Fo)GyGd5QP812Zhxz2LRd;50TCr$hd6jy@QMOxP'
        b')eAfLTWGoR*B*5G0Q?JtI6Nr3hx&lyou1Zz+Tcz;=#yhg#HDJbDre#<CB81}68A-A^e&z;wHI)8(7JQXbf<w(9HlLe`P!ggs2>%V'
        b'Mx`{3&}vlg@$lJKf6!fMkahDaRv+KjtdXkq=)tUh6zJs|B=|Z(C>t!-ssBwrkVs8MTG3iluVY9lR_3)1$vYY7t~G6L*Kay(-uk85'
        b'mn*6m*_5<9<eD{89Qi0}UQ(r2JfBynrF%o2iL@oS!q?!*rHKBTOr3tN^7Jc=#fG(9y&YQX>ZvuMI;%ZTRTo^Q-chkpeS5%bg|@Ns'
        b'TchY*niBt%mk&wZ_*|_%sfSGTpq8*q?TaRo>aG(TBI$b^p$<8zs*ryKWcBHD6;DIH8fgzF7m{5eezdp`Ls#xU-0~`;l(Nx@^B%g8'
        b'MD8xMIwWPfar(d#4vFoCzROeOov{$VoI<?t)$XaHJgQqdT6plRAa7g+g&cBxo1;WX8zp~<q03so)Yinub111DpFdj?={)_X^<%e+'
        b'J<Xik#GdBH+r*yc(c8qH<|ns_J<W_QVo$Sbi`dgVyhZG3%(sg@P2KHcPjl1lVo!76cCn|Ke23W6IPMU8nr(N8J<UsZh&@fthsB=e'
        b'@(+tWP4$Pxp2qoMv8VaqhsB=e8y^;DcYpg~advmsR&jQ>d#gCRyKSpDyL)1*IJ=vBr#QP?bEi1F+jFNlyZiAw#o66A?i6QtXWS*u'
        b'?pp2=XLql@OPt-k_bzdE_se&Qv%7hBi?h4#yT#evz}@2P?(VzA+1+2<Eza&1Zxd&C7i<$}ck8x^v%BlJiL<-gfpo9=FtCc=>uwWg'
        b'd8ghZ&hpY8kIwSWzek+qb=@P*^4@)qILrIxd&F7Z-`*q6@=pGUILliCY$kaZU<=9P0$YJyKrfxm1ik}&9Jq?!Zv$5YfA|r)PZ{+F'
        b'6qmGD%gfpq0{i^eM`DDbFd@Hb&?jbLAOAS!>m<F(;PI34%%|!oV?O^nu1^GBLYfYCvT)UDKCU#($8V+bA&5^X9M*GU!SzgDj3~w|'
        b'^HERsNi8BisUX!C^YLe?#)$L=d^a(l?C!o;v`^+$<#fj5k`ucAhGa%1i$4;4fsptHoWc~({Itj-VO_)<P!rf_GhbJ4BoZJ8JVAU('
        b'9R|LxRI5MWkJ8}heCbMxW*B9fSD|k}z(xT#3GfS8C!kY6zku}ukQ4d9;I*dNqBQFvhw7tSIw!5FJL$*s^#)0gi;us8^@&gM!cwi;'
        b'D0G~^Jy1DfJ`>)Uk86ieorHxe01<7;ztj8Z@@<qp7DO8a`y#Q8G#~BI<ig5!Xm__S+M(UuzI2Cncl-BtXm_`-*rDCs-m*ixyM5IT'
        b'?e6xD9opUP*YD8oZr`v&ySx4N9opUP_wUf|Zhvftc6a-}9opUP-`b(w-TvAR?e6xU@6hgU|Kkqr?soG|?e6yJJH@=m&oS-P?ryj4'
        b')b4I?+Ns^$zGkPG2kG~3JH=c`zu-<WAJVUXr<fDzw`Hf87wLEJPBAyq@1C7vex%>O?-X++{T|;b=1KZ}VW*fY`FE%tV!q@umpjFr'
        b'NxyIJ6!RwiUf3z-PWrvNQ_P?AJF-*Eq4fLNPBD+t@6$WQTuQ&s?iBMW{l2(U%&GjY`ki84<uaH%#oWr}L3fJzm3}Yn6mu;74(}B6'
        b'Ed74GQ_QvWdt;}VZ|Qe(r<ij^rHFZ#3&h<k=3XwZb+4Fzc|W{Y%)$I@*1cjL=KbwnF&Fdm3HOTmn10>&3jGT7OWZ4TEO5!Udxf3_'
        b'`t7(^=vtuPcc#8H_0)3)`^!^bp8CvJ4ffLFs^Wdm8tlu8oy9%C6~(Q^Bfx8luPF|E&0xQ_xU+Zw7$^=DHv)sj;o^L_Z!Er*<2}V6'
        b'=lH4O&vJaa_!}IDi(ljTlj2`;{C)9XIhv=PJB{$dX%|jAg!HFRn?CJ0@S<t6rkw`Po;G{hBBWC`ZPB!Y$mh?d{cPGk*hiVcm@`Vh'
        b'GF$(EqUw)vwTcxAR~=KH##LW3sN9NHMdv$%tt#-N_{H~h(sO}HVeS29O9B`JlAXUFy<d|7p8391dH$n^4EDyu20J?}zN02&n1^&>'
        b'm}UGh>N)SP$T03o=B{GyYUW<Z+>4ldF>^0r?i%K<W$vrsM9y%pf`=;jsDhU&_^E=YD)_2`w<`FnhQDfx2mY!TGG`@oRxxKabHcoc'
        b'ITthM66UO76|5qN{Tkh%qZ9qRZ;8pi8}tb12xt#zpOh7RPT~RJG0?#`4IJ+Sz6d-a-A^7D<-6~AstmGJ8qIvcuDFj@&GLHW-Vj}|'
        b'3to@Ex4e@D<I#oHK0TB5cEuMg@9gScuw2|`jEP>EwM?l@i=YDj5P{~KKC<b2YYv^HCiiSEbCqoAE}M{lE#)--d<UNCUl$DzuxLKq'
        b'eBtPZ>XOQVF8Na`l#*;QEvTNqsI-*sl+Nawk+|5WrWYJ5jT`(u$zm=a&vC9&%d@G>o2QiYhr)?yBIZk!X7exgY|T{`rPo9lOCuk>'
        b'A3(mV7cbVi(4HmfQnjdNQSHJdi)wTp{0XEdJycbqqiarBZuv<<P<75)BUm_*8_x|E52B?+)pm<F(_ohJ%gHuvQX;V^c93ypIfa-T'
        b'UphCily9MyD)o_AtUt;(qal*`3y}(D<%5+2a|g;4`um}|@kwk{{>sZ)JgQifg)GXOTV@HIj20qY$xOJS)=DUAKH-!oT~J+0xf(w#'
        b'eOtRy;f*y`C8TB|GnuN=)WWuq4(Ax@IS;Bgs?6=D@(Evo;JW_qrTp8Qh!HhGRX{#Us72APT$pH{($wJbwfa`KwYD@}T}mnI8H`@b'
        b'gc9Xcf^kNaNR)JuEmb`ISm=vHDMk5ayOVbI{b9P~oR)`_53~|u<BF)Me@9_YiKsoP_&FZMq>|B+DJ6CCPlQ}NQA?k{&t0EVG3il@'
        b'Pm8)h88Np7lh-onbD%6(K7NiGLIdJzvGqaunjkhtO!(U~Fo`0VRf5`z`uQs%jAj}cvO%0}ZN8RPXN$KqYbs(?OejN`!n+n^@&9)e'
        b's7s%Ce5^u^8A+yp&AaU8F8TFA)tSA1Zcl$XD8r-vt3`4yE1BDmt~Iy6bX@Pr32tKElhfVU-ql=-UMRXa`NkxFcJF*tW%I4pAb)+V'
        b'UaTT!NUFWcT8*eH(e%;Ri;b%<6sMO@Vn*ehGNmM*i1l|Sl%%KmrBn^2*(ZlKN802d81Fs}4DnJv&BNfM0NlbGKz%q0TO!!otJz}y'
        b'4TvgC>Na&=GB~7cGbIqsHahn-D?HFbLdQt4@mnP{E9DkbUo!XfiUhl2ZeK@lGs2xoH~xVyCPNcL8~I{B7174ApC-v_K6=!Mx_bNL'
        b'J*tJKS=Ahj`E@ahP^l5ZQ?dy3MN^!HD*DPL2bJ*q_Ei38-gev3^`|~?!wqZvPc>U^G`p4Cp81XA-t$hL`1B8cu<c9!@9lj)@ZjOs'
        b'zJJHS8<U1+{^9FiZ{kb229LZhK)h|nrtxD2u|~F*8tsLk(<MgxQP6JC0nlF1CQuKk1XOvY(Y|%QFrU1_XfFd5f_G@1(H;O<LA&P|'
        b'?IWNgpeI0j9S)8K!hX6;<I^Fb1K`(!x4T@r0}sMJ1X>G<f{uaq!QX)NQ>>3;oL_%@oiEz6(HBYJK^IK$7epoVQRn>iQ!r5`zrie6'
        b'PCm%Bl(`%Y71S>xVUqi;Kok`+8Z3nM5e9<md8GVR(%7+b=Tb(YNNAiiUiv~2k{b3UKLC}GD}8c+j|IzxYbj4G9Na(&(%z{CZ3LQG'
        b'i~1qDO4LDtaV0Yv*id!;WM(v?LJLgT9Km2R&tZzeJjcKcra4BVc}^}f<e4|;<g=mzlYtrOWlEmeXtWaCO5hEJH@181%o#_Yj>kh?'
        b'ibtwg)i{pe`cP+(RaGxsw0Mb*U+<__-DEWBR`^Jon?0Jj(dA&MHJX^B0dHHolU1a(0mj@$Y6pKnTtgDCh{rlB5>!8(fli;lvky%}'
        b'5)oJ$`}+C^eBGh-L8|dMe<w+ku*dE4H8j~gjlOzYeWSD5-FUUf*I;usWhCa0Mt%KJI=WPWeG^*Rk7<K8L0G*YqL%iiCZ;-cqxt1`'
        b'FdyBx%5%s1BJq%~HyEaM;=<~T1n9g~Z^R#<7jxo)#EYY2W8#kYAjLjR$hwHQb=}59&=>CSBi<sG9>^zUFnsb$97kkHbk1b{Czz#B'
        b'pex0x$4~VvnyQkex>PS-f;l!E!n~L1K-&iviePYbQyxl^`<tw}5uc$dx}%{8(j$-~g?0IRF@28VAJbYV{2O#<4~d0m0G9Aw-M&P`'
        b'*WDXghv5efDVYyNd$8JfJKJ3DMqhKQqrJ)LYqqT!D}E8e*O`dXo?6;4XY}(?Pj9|cdGhLkG_KU-8wjlrkuV%~K-IKLRPAV0x`ty('
        b'`ZR<EUj^UB#}`(F!kxYSfgtD6+xnQVx3|29sYX62$@p}7!_2y~#26=I_66$OJsXn!0LB<PPoz)0N1*3uujF8*Te3bN*BSFxIqMxx'
        b'Pd!GN&(mmYb2>`r&CBlG(%K?@l%6ehbd;EnzSB|5#@7duxrUi%hkH<KI?1376${0E>w}%BieS9cCqBb5lF1Z|t_XT(q(9av_O9sB'
        b'PLJEyy7Fu};(yeZh$TAtLz*&&N{`T2b&OD7u&W>av@_a|1tDS{pf_bJf(dMHgDyu&_ELwUoqW(qGfg<r&ba|b5+mBw2p+cA@f(=*'
        b'Ce{d)59;Ov3G{BdWr1d<628`J^Va*;cx_F-hBoI1e2XfZvnDRS<A}n=Bb~_tB2qr&<9Ox<imxEAl#aSE;qT;58al*yGj^og*JBZr'
        b'QoGdEXE!8epD`bV_ziCG$YmiTy}{YzWl+80sFRHsEmzqe6#@l{7<aQ~GciHR=}R_tfTosMP%TjOV@CUln`^A?;Tyt{4PlmNz|TQT'
        b'c1_Ne<Okys>_3@@pBUv*iL7yhovxb~m-DgJ{zPYwFjwis-}U@TJ>TBuw5{YfY{#UfMYZwNU12gd^G`5JpuaCFUIj20f8iiRE40&*'
        b'DT2D<+jN-_73H6)@f4+Jwm30G`;<_e;wk}^o-;{}GfK-{RNp@ut>d4VMaMrkYpZE1AuiU`eZY?;B?1B>Ikc0ws&IqmpDwbZ?u7bk'
        b'Zf;l5P0=tyN;GR!{!aDUc77$7%n$NF&q8^#ZePEMr<Bn=p)hT9P>U~R;!uK=x}giAJ#C6yGcH9wobLK61;3>{S_RhXRO`Z2>!PI9'
        b'U9a#Tb9<!0R;e1QR716DSg0BnsfNX>VTo#}Q4O`K;i_bWm8zjiHB_sHg{onZY7kK~kF8A@oNMaqZS5W>8CKaGjyBe0cdp=0P0kjF'
        b'Fx0oUw|Eu$MizV0Z22H)3+Nuu$3YK)o&bFj^fl18K`(+{2mKWEE6_>M+aTj!vt=@<7<36}9;gCT3$lTn$w`6Qravr}SzL03Patxx'
        b'fK|FEfz-)_IU@b^5=&!fUT?r&A=s;Ps*hkRN&Scfos(RCtr)#CRW<|?$!mj=rFwUJ<+!d@te$sp`S=Vd>*#PJzwS;EpL=;1q$?|U'
        b'_YDS^tCudx>2-z0YXM3hTLk(d&2+qmAf`DdzsaNt1C^xtgVIW$t*erm;@5n4`gtxf6*~B$#lG>HU@U@O$pxrLTf=$`p>Cv}jLg;>'
        b'>JF3Of=Jcvuwg`{CFpiFII!##T;a{tklmlgC4b%~JIU84%^1|7#*j#gmn@kh5v}B@QoLHsYD6gvimfM<(50V@jaa&Pq-)Y%AFXuI'
        b'l>^Z#0o4K)3Romyv4AB4Y8>J&fbXEM9tQmuGzyyWMYE+6)B@@SeG;@6^bF`_&`&_W0i6QnKV`NQfi4E!`#C}7FxP?FLEWGaf$ju7'
        b'ApPvo`6c=m?5}}-CHa2^7JNx_zX)apbOop!v>0Ro)q~y-I%m>3lkAvxNsJ`8lr5z>jK3{gvs3_6Hdz+bx3;ylyS+|_w6%C$E$wt1'
        b'9qR|aIA$dZeOg&q?Mo=7N|YAgUGxZ9u-spjvFe~TWGoShi$xI~_m2CynZAe7r#7y4_$;eeu~4TK6-lCSQPCcnmx6J6RA3z<Rv!WS'
        b'{Gc)EaC}p1{YqN1aXm66W4Q4ZUI|63zJ#ZpSt-+VEU2l52FBEs;6pfLexeORy5FkGN;ZG~d}mu*Ya39pkpM3qdFqiHen=22P&}ZL'
        b'^6si|K7Ec6#iX}oL3-DfWcWL|C?1RQ)v!yPEDXi5e)5aT)cqPIx#>H<A(h1b&VW6Qk>#@-(YnZw4-*_;$CaSv8(b@Vw8Zn;JS%;x'
        b'9bTW;)$D9-_xe0#3g1MQriQ~4xrDAo^i_`KP*uw4%jj9U3H_0KZrURbc<b%r#F96NMVq>Li4O2WXK`6?i$;5;@FF%0bfPNeMP9_x'
        b'FWuRNjOkn{f7<3iE|mrP=&go)7m(Z~@qJZ^)9dkhuJ%v`wV}S+Rye(tKBr@a)8}gOw)s4*?QQi=<w}L`X3F@&nL9Kz*;e>mZMJ4*'
        b'lftEu%IIy8H`IB9D;{g)&oC^)=F!5PZ%naUE#rmEc*T~b3VEnb+Iy_0-r@<OB)l?EcOU2v_6I$*o8l)Zz#FqoZX~a~Au<9jSl&O-'
        b'EKaG#SNlUk%Z4(B$0l(>kaT7J0tHuDu9PV4cJy`c#%PewER~{#Q3CFdzw#(qAHm?8Uy2Sks{|pU{lZZ_>XzyUk<f==rGLPMZI4I&'
        b'MhEs7!Izya_$)Q}fEpXEgd<%g3Xg~K&9bG3iHX?y0#jOwtSI<&h3y;Zp6UvH=u#eCMiS^pnE~mua0XWvb3MiAjfi^8UP#$0)K2=+'
        b'W;9B>R(k_jN^MNu=gG@cqNMn)R<gw}D*&-q=^~>ch|%bwg%h@#F>3mt*nMZjTdBo6Kw~BDjZp8?nkSiBw6l@6uW9`P&7tL|e83az'
        b'^GACyvzHGv_hTo}80n?ANX!1tKx$Fyg-9aV#7HiojB(E_TXpmIfuh0EvVXQF8#6Z<<AM5<45!vS^$&R<v~-M=bYUjgK?Ypmo*;eU'
        b'4tEAy)m_{eO{sQLnTdZ!|6I>KJGe3|CPK<ncMY*fANG7qouXv5dHpw}d6c#l8DaQ+R-sN$FdR@FqOtWYkwmC#W9F=y5k_(-LEchG'
        b'u0Iw}O)$HIh@+k#W68!7lVz$)n|P&4kI=CvczW8!)h8`#xKqSLH%N=EMM7&lTKd(hgPZYHNIe~oUPaq)1jkdfB+5sCXin*;GwFvv'
        b'w1qF-^BetgK)l#nzKo0SNSj3nm8g!(mX%;}Rns7TN@<pf7<u5+uy}81QL5472h?Z07>Cz#x9c)S2NT1AIvc-zI~braO?0%F_j_?e'
        b'd25%8p9Wi&rT2mAGW$49b4$mX#ZUxFMV<Eoy4RG^0VkcJpbWs=9$qJobWmHOit!+C?dNT)&4B#j(-Pc(?NB5}ce-1UX!T+(nQSxc'
        b'tTBe=y9&U2LrZXgPj@n_lttPe@Eq22`5)fJco7HG>9O8^ZThR->ylkj%x1xOW3V?M1J62ZU`!F=KyW}l6f8=W#u3Am^LX)8PBOt>'
        b'ZVv?meBXSnk{<Fp%KXih?M=M1%%i@-18Pl0y@M(ov-kSsJdiQ9jy)P_WvP9mi^lkcxIT3kq<Z5^)VQxx^NKwYosMRhI1>G_uxO<P'
        b'RrEBBt*5f8oubW;4Fg**T9?lfqHOx9uD>_KnNN`^5n*2(64ShmuAh{e3q-|c`Vo9SSu{jqYWL;LwjfEtP}*9D7b*2(tJ)e)a_JgS'
        b'x=0!u`K<1YYQ@84{ToBwJ@BpOgO9OhH+wY8kLSUq9^;_Sn(X_j69@8L?`~J~O!weoeiS+J&;}tnQc~*)4+O#BvkEnbcrx*UoU}A~'
        b'lAicei`SNJVt0qaVGRBV^>fA-K3K`SQL~YNE6nErE*LmY&*EDMn&`cKF~zgKQ|&5D#6?!xAoC>x=b&4UnM!m$cT)FPE{BXoeI$ub'
        b'r&K;|mx`H5?muGd-Qq2rdKkW5y%}0_at=i4)LAlwhaWiPR%+|GOi<KOa+9a2R5j=*n>~vP))ad-RLQ8LZ1%IIXGqg4oh|%W`O8a-'
        b'Cq2CRUB+j8m-d{rGNdcDHKnCvO3SY~EiXA~?xwTUk14Hg&1vCj0;Lb**vAJ#F@K*gfIrEpH^8^@nWLm9=#TP0zD_@vR5(jCSju6+'
        b'AYxPIDGN)*`n`l4baskSeKEm5u+eD5GgO|t=AW^GF?sGZP8XZ=5Po{+Jv%cr*!+D%>DfZkDY2x$bh23d*i)oa$B+@~IQ+A3h6mp|'
        b'dJmP!mTEn8E`6yERBPfT3CRxdili?$836=Cl?-ll+T1>m>zeGc1gUMMemv%kP=Je9hx_|{WRGjyWqPis$>s6-oXu|U)g|-PPegP)'
        b'ja*B4pt#Q;i}^Pu-zuf1$J9VP2)&C8#xRXt8@jGsbO~fa&!m-q)?)D2HR3~o4^IcQrLR8`>Wzyp#xgv1{8ehi%ax48n2?`C)B996'
        b'pZMqymwL?Q^+blGPJ3&Ol?2L?V|Vai9UGKmeGqPp&WIS~*sq2C1)cpW*uST<FNOU@o&9~VzofI%^{Ow|72U7SCCjWu_rF|svPX>9'
        b'qWhP@{S}^m@^|dK4!V?0J=^B-+Ui$UINEH@%uzw_%SiVrK}&0k&(Uo2ai=zKJpt))f5B`q6)`p`UyJe(@!X6}&etZ4AHN{v_X?+@'
        b'F04|oK6p9#sdL&J<gZxME6?u>kZBloe*aAVP!2u6C;in`dOrvUH}r<qRq!jn<$LjzLEj#hD&)8hA?{476lN#4dI{a0pO&RPd}ooi'
        b';FQu!#7%B{#j?hiz$QB`-)#E&_zQ}O`i`l)R2hzDO;H|xltvB~zWw72UpNxJiM~wf-*5Z6#iD`f-*G3IBAgIH4X;mL%gmaVn(Qa`'
        b'8tq=-6TnlT{h;D68tq4b9pLva)%1xE!0d)wpWELZq!mOteT6P5EyqOc3En7ncO|5~lx&fVH>^lo$cJ$W6S74S5mqhu8!PXOMtR|b'
        b'u^2W)a9z5T(rFgXOPA8e_7cgKGH&zBl3!9ZQz=XI#>bQ^lJXcTQq}l-eewhoZQ--=eUd4Zg9rFSV4e70VA{?)@<D~5B2Y1CI%p<H'
        b'0nGuGfXYCXphciskOgD~IY5n|CXgHC1+4+4%aHbh7X>9i1E5WyLC_Y^R?s%kcF=vGU7+2dA<!eBCqR2ZdqMj^&w!o-?FStIx#azT'
        b'bY|@Xq~9OEHi;gIUWxP@&(D@El=pmoH!2ecMDxY<s+buDr4X)e-J+f|-8#W=MqN05XYB;TnRMa!eP|O5m#+&)c;5uW73soJ+Pfwg'
        b'PSJ&<b=mF-hO_Fz(fm3z!El4Ra9l6y1jCV44M!fHm}oeo7LLwT@0n;glNOFdhWAc1T)q~L-%~r$a79`;dj3B%(Qt|uj?RETH_>ob'
        b'EgYQ}-#^iCgIYK`TYg}o;b2$8QC~ec;c&)eIP&}Agu|JV;b@*YG~sah$#8TQ{_upu6(z&bvg62v!zsyd({%eHqwdZey$ox<?8lR2'
        b'|0<O2ey(hfB3V!8%lsG1ct`(*KgwIR%paXwuc^JN=BlOdt2Jej9f(Im@)@0!B<Disq#!U7)4m<6jw!<ENv^LCE1onKKXl^bT7lAB'
        b'xI`PBp-JQOXKp52oW05Pn#RJSB#jde4$w+pNMJ^yV!<`$N<pg$afVmjR3tylbAbe3DDI2<!$F_$qzW;Wl<E`ejP}z)a6uJ|Bzmyp'
        b'Ns8oFB?V|{Nl~J6rEk`11}F+~db6uP+*zimYf?q$Uw$Ugy~gEo9pt1*0H<b&%_<r1qalA2Sl{R*fpj`B==EU_(dKnJXh|)ioW;dF'
        b'w0sJwa$iUltcr_T!A39~@Fg>=3m~iOU4)?3usCBL=bel%A<_I@o#6zwbK-k3eemEyjCAUWi>tKO`<k2EeQp~UC=h2bN+@XjTKXG~'
        b'TvwXq#h=y%MB<bn30Y@NncfrdFE6uISxT`5;2Ln{ZouD59hLNMBZ4UHK(vzeai*T3CK6|%2yKT+=%Ja8khofXj+(RPHj;b`(??Ep'
        b'N+c9vmtLk^a`DW$vu0mDr#DCghvYTrxN$H%PK;dUp2zBshG>hG7L?=?*7e8Lt%n$kB7hj(!Ek46V>FTJqO;2xg73Sr;|X!85xQG}'
        b'zX%#TbGm^N=R<_#OsJirp(@QmY@s%W=tD?65es+rMN6;`K@BH*%1HEk!E!Rvi-4}sKqiNdz?5ds3cL~_$pq%NINkBVqh%Es@)d#L'
        b'`U)vkE}kbx4~a8V%B$M>v11mKy%6?OhbDHWO#iEu@wkD3S5w1phy4lAe$e4Gx3^x+OluQ(n($|GTq<(|B(6yl+1$XaNvzqin0Xp)'
        b'RrH6bx_S|Z#Y+el)^gk8s%mEYvCyMq#WQy4kA;4nN|+b^Sm@nR@Z2r?vCzje6Xwf*EcEmg!+hC~h5nu*D@%E`@%Q}xzYhP8{tVhL'
        b'$6(0IF&hj<qcJDPWHRTNa!h8XsJ{~WDH*@5MX5hi@+TQK{xf9x33ogH8MFMzRbl^c{4SICp<g5KoW7s#!k~32>29L69u|w0pcaGh'
        b'J5z?aG!4h%y<7j6ybJ$rPG^f(5pRo?cz>r*U&$)?4MTB$&W@B-$4T|pf|eB(<=jCEoi31vaTWx7yTtn&@zPCw_ZC{$St0HxB1l9?'
        b'YL4zb`K!^s_Af@eAM_mPowtqlGoVL62SK-=G1`9*egN2fM%Yy%{#ewU=6=(eO#To5GJYIHYC0#R|Mc{;#X)KPP?x4YeZ7A&Pd#n4'
        b'zaMl8G#}-?9&{JX4E`VgtHAI7RS=n5-!a<rFU{d}oz6^jk<Pvj=D^>C-3N?F^TVT<?<YX|c+=@olRyj0vClRLyGrSPPw3)$;=EM1'
        b'k*PA@(==ZH^qg_iPEUV9TKd01dc-Sd!cT$3KTpoFe+lUqPu1Kg{WnI8_Bp!rZ<gs3zcTHYK4rRE8dxaY#ae7FEbI@nN^#s6+b93J'
        b'&OoqB$FSM!9nJ>ky@su5_OiKEmDet~vU0&ywguPt7u<B++%RWpwr0{h5iZyLWfdHj>i)9p7v|V^Rp!_~2|5kB3icY%vFaSV3HYr='
        b'sGq7F`w;NXMZ&HU@yDV&)7-zjD3d?6YWz5e)O6-Z|LN&xi-Xdds!LO!zTQ8XTS0e#DpB4p&|{$gfZYQBzgQ^nJV|8s)#TWfHG=wd'
        b'W};G^JqB~4R+uBeTcr7^t8(nmOn~(9rqfrK3v5}MW3PUnu&b2r_p~mq{jOBE^IHT~wQ9V3+Qv^iJ^f{A>A!Q8;8~XnKNm@y+>m4c'
        b'9?~ys*4!xlKP*AL>eBzXOrQ8?9Xnw<hMm~RTKp~l)F(`U%z;FN4uRYMCm&@zp+2nr=@2Y`=R-OaKcwn5yz|KYPrbI=vheXIUcda$'
        b'uB(<ke#-IAd5>0q^8RhF<bUnjx%H7ffs)*Vli1*~nvLJK)n6DkKmGJG_cr|L?Ydv*wAMCPUsCyY<Az(Wv3xUr%THRT^-GO|Qm@<`'
        b'`8Mimf!2=--1=>S*PrG%xTW02zssH9$#KgM@8=kN=_NwNH^kTXC)PLC5I%h0j6R_C&E1s`1Gis#;JF_F7tQ<A4Tbe;KH1Qb+gC4I'
        b'U(XJ<boYJhbM<W5j*jDNeqL|g_VmCdPfl~VfA_`@j?Y->*!g;M?kgt;9e;lR&%bM2@U&y!Cx5iDe&D|xlWxzk*WQYL2HFMs(Uu(h'
        b'4?%;VM?n5Na_ldGZv~d#A?zv<e=I6Zb6<5wCjU#fjvoh+n$7{~KRx|yaZp-c(xs_SU+<sHzXQ#?EysQcl#B8<fVyBlih8;2c7aby'
        b'BJ;&}=Gad@ET~LpCVF$LX0C!;?OnpW5V%5`H{Ol;YXYQ?cPz@?mSg|^wu$*AT5(^h{qQb<2OrRQ;ZIIHK1%<mY3YCMZoxY(%kTq<'
        b'pV*#bZ$tX0@7LTY{m-J#zOPIFsH{WcpKZ>fSK=o1-MIYFpQjp<99162sChQ$npH!Z=X~ugcG`Z<IN3DWoNJhzG)$hH1H)wgOB%$_'
        b'oDa_AJeUepr%A+7J&RwC%E%XxOe_B^zdZama>&ig&ok$1n@#D#l+QPcWXvHO=Lmz|9UD=&lOZ2wV&~-l-|(Bn<tTE{Zf2It^3WCq'
        b'Y!aKy3fVdATy`FRM<06$>!=s7#ssnN<=Abo*MUyFm}4&l4!@jZUkv^ez#T6OyGq0#i*}^Bf8*s${>9%LKMo=_oigb^J^gHPP+Ax3'
        b'($uG~_fO{4ppSrRQQk1<3!s-_cfkLDza;QNNo2m^RjdX6ThJz*nP{=jz8U7NuL<*Qz>iDw@b`1<uS|gS@s35S4(He}e|=(piS9j`'
        b'#{0Rz;x{zjm*1Rte3X89TKbbDuko<3&y)D;BRTeeNBWLqnj5A6*F!n>%XI0N$vPzd+2$>GtH(t;+Uw8q?&5#D`^-P(*n57TBkrR;'
        b'YPOi_%$BdtI6I|&4WoJ5=BanN#!2aH?y0W@kG}G%PzSw#8rE-vp#631ykU^b%D(q;E6i5rIRo<rHujqe8~8R>wa&&oAGEQhciG^_'
        b'#@2osZcp0S&CkJo*v5ulho3iW?D^lq-x(YG1IoR0lAYaFg!$<LJ1f4#&emRTXOEWJ5vQFkSz>25TkPz+c01y?KaA|W4Y~~!COzk*'
        b'`%Hd&BwgAgAkwu>I{se;{fTs^lk651gLGn(ejd=rKo5`vnrxr#R6BH+os<=!mpq>%z2Bf`>5MnXPr8q36)V#web>}zBv|$uz3Z0W'
        b'PpO7UH}`+ZZ>W@yo$?*n-{iZk|CaVI%6vagcNoy37Idrpp7|#k&$F_OTS&HyWG6_M3W)TJ?*sWjH_QB!KJFbP=O)cmPabJLCBtr!'
        b'VeSTfUDjubeE&!9(@x9xf1|Sev<TQGzx)1<zOBk{zjw>`h4dY^PlhF2BJ=Z#Y>V&7dZ4<ayBQkjeh9jwfpo9Syii?{Zu5Q_=4+tu'
        b'%6fVe^n1D^LJBM9$@2UKbQit<ll4n+knGYK8Rr*ep6;Q0h~-*kmHggaDf2NR<Gn$)_eq)W=j7+~Psn;(BHQgVbmxVvW9kq82Kpu4'
        b'Whmnh%6@gb%maNFA0k;l`6>P$S+7UrAfvt$mu0S!{U=xUXUgjf()|g#JA?H1lgy#aGxg_fGVekz^CYU}KWnfhT8LIg*KuFT*z<_`'
        b'&}_yIpep_Y*>qfJl66RJ@<y;?_AOW5WXW4wyl~!Qn=N1e-pQM`=0&A_ho$vdzqxzQPwJ*GaCpzm`gPrdf8PAs<oNHT{cUQ-mDI$Z'
        b'#8sNo4C*hZ%$7AE@YneRLe7`#;s!4Y>N%y|bHLBwUu?2lK(%#(4#9k4xyim4H~^Yir^)MCXPWHZnVEhYFEQDl1AjZHBs$P0RMvIz'
        b';|ly}mU<F-xl$=k52pEw_II|)Q=u6ST%C<LbC&AXud_8souDNdC%_gdrDN#hlA84@B=X~S*)p{}OQ!fCP!uG42umj4>ksvg5&yC*'
        b'@i&mjcS)Aw@FUXlKog2vIZ(M!N|y2?AkxjUY|I?g_s1yn$+l?{dic^>t=XSE)X7Rx0*TX}W7l^z>RSrlzpHRn$#7XKBWsa(D_ohL'
        b'cb@6!fGh6ds+rS7eaEQOtSytRiczX}SAS~PeK!@z-fbc*+9?m2joVvQPh<CwcNfhVu}rXzZQ|R0_MSYJ=XW(4)j(rqbf8Vt?egSl'
        b'RjN=?^(6TF?z(X8*j-rY<a(EVc)m~*P>t+MV--tw>#>e*m#F7~=a;Ip!B|z6&F?rhmA&VPtPY4n!yff~i?mbD5M`UIWre-H!RNi&'
        b'Esl@qqhL`{wk#?E(oW(}Wd6@Oo|H{vOgL(DWy=8jd!9CQ=ytv4QB)d5&Ia^ce!{Lj>W$DTI%$>1^z<J2>2&y55lqk=C<c0LJwLI@'
        b'yJ9F2cgRycbQ}-fiS58ct|h{|39;oMAQv5%j#83eEx49h9g{Rl5Q~nTZ%77C$pPuLu*;^@0!XedDIG^kN@eOwEzi@dcY)AtTM4@1'
        b'xtw3k8o!o<FBG_LObx4nK6;tY{gK2?C`LkAp%@Rt?_R)M!Ce`7)y_Qdh=r(1stXUTcOd=6bdh8@*h}x;K4)fzPv<kkgP{BJnBks0'
        b'X1ph#83&EbFp$I6_1?hmgrIcEY*CyI?H;Gk-n267X)3N~GpRL`+qkq~C_&1a>C6;qoW)Qq;nI&nu941g38}vLwMc{?a8ed1<M|K='
        b'@01F4^3zT{tfNcOxbh^Syp?osiVHE)GbDv7gWXx2q+T~x7G)h)kOQ;^v=%e~+63AK+6{UJ^c?62=qTtkXaqF<M%FPCR130z)_~T6'
        b'20&by6C)`$uJV`+;w}PTv$HvAb+xRrHMtx<Tic2Zp2utRIy1ShYn-~+yuOCk_7+D9$J6e1x03K;k}Fj)Wkl8nMr(^FGnM+b`V8JG'
        b'XPd{>+LFO<w$-O*$kpQVH0n}sS>^HBZMsy5K|bNp>p~pYq<PL#EO5mP?ea9+y!DMKE^SVm!^bu2r^n)KX>DK8=<~R3^{L6LnQyT*'
        b'XLo3{wb1$a)MT1lS2=lmre%1g^J<^Bwbj?u+Oi_Wfy-bvki>1aG*Vkw@6zOKS>bI=D-PE`#-sG4xFATobFB2+ykk^ni*vQwq*+|o'
        b'cs;1R`nGJPB{zq2Y`6M`72`Q&&kj#4d+(JsJbs^%n&@~_P^r@#TfEK|ug~FXXh4xu+~~rV6+HQ?-ClkFZf|m@c3WcbQ>IkacGrp&'
        b'hh)pOqAzkanR-`8ySvF%kJk1z+3e1y6gSj_6Jy5d$l_*iv$fPW`bdphYl9D#6<T&$y|&c+5rc~EqGC{)8<3_q#o6O*a@JENHngfa'
        b'PI2cP%4S;o@vzOdrY6KtPu(WPrLDE8$!;SBd6}V-ZrM9Mf7mdg8dz9-^)231XX5x=p44$9T-uy&C!%xs+-<E|d(^i&T>62aO$6;N'
        b'2<70N#7-*xw65T=HDh2o_*|k7>>_q*JqwmlZJ#o^3y1W2UF~XcrAELxYG=;mO40Ld4y|r?x`V4B)!y9dNJ}ZT#yJa}qa`i=Ri3nX'
        b'bkn+s#*<zsx6R{O-P)GMO@G*M=4#tYXKG~$c58c+Lo`KZaVe9|`m~7Lt)4UvRbsX>Qf+19Q`E?KYg+NVYcM@{(8XI<r#iGbSGYXh'
        b'Hd|X-*4^Tfl*#pI&v#%;>+00jm%NPjmwf$FAn7$_(IC00!$FHQb#9doE=+)JEw+pR&NVJiMiz8k%Hb9ZnD#bj3J<lFjh$T2c)eP6'
        b'H9Ij-QmTM+Qu}+VTSnz1xkA%qCVz}b<kKY6fj6{nEJ+8d=+?HYQ`u;e_GV{GS}e{r^-fF}&EED@etQ4sOmr>Tozv6&K)bU&ZD{EE'
        b'`bJjsh)JHFW~mLWI<_HgXEwK1{&@4XWW*>P+FMql@mo^e)=-F6v{j2kH!ipn?@|r=g;lbowl;_M$jj=S%3Rgz)z7&i<>vI}7d1i?'
        b'bSmHNNwv2*>sR4VlQV79VaellHDnA%$yU2AD%aNR$>yPfcN|Lp>MYKV#(H<X=!WUf!BkJ^dOVJdd45c9sk6T3EpuMbhtKxJ(0OTd'
        b';W17F)mGm)c82-nI(BhdJi0-N$sn7j<|fCIaT0JZ;mf6TAL8+v(pG}inzo}#a?{71aL}(AJsI)0w<MRFzDE6%CDXaS(dABa#-hWU'
        b'I-(oB-n2y{=U^j^e&cYp=^tm@CH)!4nXB7e7{XYG*;4rpPV9Vqjp!A+1sHcxJ1-tnEuNGKPoIi@jB&oxw!-FW$?lhykWH<gv_|tb'
        b'c`^qOG3#wDVsv;~o3Kfu%1qf?rTMFGqjj4PPvMnLZ-ys*y;CK(*0(mH)tg;SS7-PY{YK3;*5;`Vsd^JBVfl&?k+nzj%xPs$?@h^g'
        b'oMQ#{V$6veqb;yDCE1-09=8({11-;+uBK}+GMv45g0|ULAOVUXH3`*|$3qKnZ?bmB^Cwj@V{c(=Z}NK1<`vV8yCqrKV|rh+xbiAA'
        b'9xsXKtm*skJP`#Szd-Ho@jQs(Fop;BN|_Z}(~lDg?dLs>>MC@+Ji9$B$MfTLsU0aZ*Q;Bb8hDY;(oTAR6R3REJFiL1+OCGH$4{T?'
        b'Vj}*=t(au0SnExswBvio+K4pacrrJ#8r#KdWd&vx?TPHhG?wb0bH;dnbGNhyCB^T^Oj3R6)0Vc?OmPz{W>1=<_CoCgX)ee*h94&8'
        b'_LllgC%3QB(Uy(vake<p__SiJ&r%LjxUR8Q`}m8D*0ka!*$$7d5nH>|XK0GES{8Jo@jW<PE1bHSHme^up6#hiyJqU<>DvLp6l-ts'
        b'qAz_Ht@`m`Rp}Kgh6#Ad`r;&uzjkbmTq|0fnUS@(xSCfqd&M4g%p|c3ZgPz2isia3=_vIfTr(<U9X5W}Y%v%Z>xA7%ceev`fOh~*'
        b'z}-MI@Qc7);J1N!z#jqgfxiY87)U}l*D?us0dTT`WQ1}pg$9yE%C(SS&T61x3dx-0T8vXj-Y3_RGlgVXaxJDQBr}w2F;5}cl3YtJ'
        b'@K?Y*66i7HTJnJx0}FtQfs>}tnLnfh3;+v(Hv`WBJ^(xy_$A<Zz?XqVz+VHW0P~Ewmh*v^1E&J(fW^RTfYX2jzzcx)11|(V1Dp<g'
        b'9e5G&_drrGac&OE1H24q1l9s`fUAHeU<_ymegsH@GhZP8z;BX&;7`dv@NeWFIKu@0z(v4Zpc{zFWO1MYxEW{!?gZul_W(`6gA@+<'
        b'Lkb5Rp>PUg#b$&9UI8=$tw0hmT19+d5AlIF19O1)15LoaKr?VZFc<h5Fc0`9Fdz6AU;!{c7wrJN2sjydC9n`^1D-?a0M7;X0nY>8'
        b'0X!f05O6B+i@;*wFmM|1=fDeqr-2KBQ}S{xi-0A-#lYpj0I&@h1a<+tDF482;0|C9@Nr-W_$=^x;9=kmz_)<CKtq16<$mB);4a`5'
        b'zy~OPAPGaQ1{#1NAYG7oJCJm(JqR=bzXUXshB;s^@E5>5;0Q1uIJE%v11tqj0@{F+fvbRpz$ow>;8x(dz#-syz^?=8?Dda;Q-FT}'
        b'o)0{C66%ZM1JXHdD{van2fP570A5J(0jC2$0lWzK6mSOcc_3Y?aTI6({t;*d7EeaGfD3`7XKoG947>%H3w#Wi2mB^5ANU5a09a6n'
        b'asjUZP6jps3xU@INf2xs&;Wc0XaqhD%mKa(Gy&fNnt_wgK{~+sKoT6Z0}Vhg&<G3zbAY!2O~40%X5iBl4tN-t2Yd^dPlAW%=5k$j'
        b'mjMmHML;8PEiebT8E6829%u$02Id0a2Ic{0o`-mVOMpedcHk6X0(d^~0pL{Nw}8dKw}8`t7Z;%&fHvTT!0Un2fp-Hh0`39M03HHf'
        b'4Ez&tCh(#uxt1yl2doB$fD3`UfQu*{;9}sfflGkro}X)}0agHOfo>oPh~5Y^0JoBT2<=98;4?rY@G$ZBGIoOaz%#@LUN{x?0$c<%'
        b'0b77(U<jBC90cY8cLDQ(dx0d}_idm7_@6){@NEhYoKcMMz~w-82+tFs0XP6O0(S#*fZqg~fWIRDz`|)r4_FP%1G<6l>aLu>??Rq`'
        b'!u2|1+^&=Da-FkZkt5HJ2suj`vxN%K(%wu<(0Z&uTiZP2U6jbr;K{2E6XLo={@po+?~9Y%L?)XnKFo4WjCVyPzf7mexysq3zaFMc'
        b'sVq~pOL*cjannngGA}_4^*Ur8osbU5P*JGMyBd+yp^{Wrnp7apFXZWoL~h`>cy>nnOEgaBx-un{d5KTvH9@MbxL1BJ<YK=Y73YiU'
        b'E2Z9EMd~0fO6v3-)HGZ%c3$3jJX~H*p3re;$dUSfjZ$~9AtT&eDUZEE%5*nMxoMKeri-55FJ*pLav9ty2Gb=umm^LCoqZfUWwwm6'
        b'iwuQ11%-xbxfh$~6;dL%Bu_?;jvA7L-*ojr)J^UtX4r(jG;*oQ&S)9N-AH!$<V7Ys$qk$GFT+5j+@GryCUqAh5PTO)8Q}vnOm>n>'
        b'm)_V|{z%TXI_a;H^UCO~<i#etq6<Hv{9P>LnyKY)x|E4eITObJ2)8w3xQ&%xlEp34<x9;k$?0xO@~xatZACJ?^WJ4Sq6l+&GC!&1'
        b'xDReKh<#OR8L1q5;YKq2re&#a)Om}L3h6d8+0Nc}DfKZ<+x<`bOa9gx?Y$o{+TTL?X#YWFN$Soe5@PhrN!Rb8idrkP9;`c5G0Z9d'
        b'^8$O&F%I5bV^wv;oib?h+M}a&Ut;ncMP8aNZ}k_@xtY`4x^!;2X>L6_x4bmBEjs^&X>MWNS;X`+iBTP|Ak8hNbDNarme9FPPIKF('
        b'i|d>;w+D1?^Rww#H)hwrlA&8Yi@!N(_H)PZSDI!&Zw!CsY4#%BU;Qs#q0*Ew{H33Dx?&7}jx>A882+69m*~e)`^MI(+1otZZ&aQu'
        b'8cpj9J9WHsbmL%Do=vf))UnoYMs+&xwYt^%%cxG5qgJO{KN(FMr~2Af$8<x3$186bU+KKMYU$Fs1CCpU*^ym~H$S~|P3xJP-tZn+'
        b'YbakcXkGG)W4FJ2U?~qkFCpnImbjnVkQV3P_1kxVXLZk7(m8JINY=qWA<pA6PQyPj&Y9PVxw3Haa9z@E8e@;tGkc|t*+;B$2t98|'
        b'_6>Ei(%)gwi1768VyM?_A(_s-tIQTUQ`P9v=HK0`3>o^(u!M_N^ucFeUqw9F`ES+S)E5d9V(ZhNh$wx0q3m%eo&H#$tdVX8XbL3~'
        b'y}<?#Y{8g6*4ab1J1M<b5r)Fu%(lQb5Q?)k9Lla1aE)NPy2Esj@`j#ZSfTY{*~(xricLhM*N;R<!CjCvs|6x-U2`-TW(~cONT95l'
        b'E@SavNlt15g<i!n)f&L+oZoO;=3d>*_zhKM4Z&bQ>523P%IY_E!Vi}fE%W%hf{Beh@-jQudoEO1m$mW(NGL))5s8*LJ@nTdi>%|<'
        b'@M57H<`-#}HAhJ4Czmdk<_-QB-TYkE6zU5l;`}<!7%Het+(NEU^(sPUwakk$B5Nd)O5PGN|N3ArziW4c(nZ-#2B!NYH!AT+R{~W^'
        b'@s_nz*vfcY#Q9w`N+KCo3OmZPTrIN>TS8O}bBY=hpu|Py{AdrQQ{IzO))?udGft>`c}FEl&2r_1Wu9O{>GPwJ!)TjWsGIH@jbL-('
        b'-GG$&B`U$V67TV2!-nudB@~YKC(1<05P849x2#o`O%ZiL<!O%xMe&kxl(|tiJXcg7F?5A^SzEuBp?GI36s1}Yqk53h9+73*uW&`='
        b'jF($i(Xt|{Nnf$SZu%F@_qzi%*2A?Ji=<C5D#qS%*y)VksR3;)QeG~g^Mtnw9zFj?J|fJt_M-Q_mR)8GjqStt3p{YY7XFFr40iVa'
        b'gI^vKXOQ#dnNa`P^#1)XFXLW$o^`yR@qb|%FO+4RF4uflpT&R9|MD`@I{wMC_&;hHuB(_}+y^n%r>3uUPZ;b0&=%0iB_{iz`qH9E'
        b'*HMgT*Tt!>Q)uiYmJQcc%d^;j&)lZQRfL_?%m;L9mVe@}Z255AZI7BQ9|JuG`uwAs?t%i-`37eEozY-jT4}H{gTa_%pt*7_!l-#m'
        b'>04HDcZBMeT(fl;I#`dP<815A^l)dxizUsJq_2B}rX@kFb+P6hD;}0rC;C6I-hA)(-tWENd%yR7@BQBUz4v?X_ulWl-~SW8%sqy-'
        b'mr(J@(HiT?3u~<-p#15z)|nv71+~_rSDEaa4jJv%?KRd)(45a0?H1UNzGAfR0(n6l;E_KfitELfjrOvajP|!cwJ;BYc7LSCx)*c+'
        b'bQp9Tl>gBhYZ=H3+63DEQF^~F_rn*6^vjML?fQIIHVxO+{@ZZf{<Xt(&jHK)!*v#z_jC-`%>nJZPVPyuQU724AHTv+iTWTkNHj{!'
        b'k!X@=mY6FsPh!5r0*R9(PL^0G@f?ZgN<2?uk;Ewy&zCq=VzI<&5-*T=p~UGDFOoPz;>8kYO1wnkr4lcbs7Rb8akj+ECC-sJSK>U0'
        b'S4b?8SSoS8#49D1Nn9YYTw;a9N{Lkxt0gX!xJcq+iAyBbNUW83mBghI-zU)`ahb&B5~&kAZmF@pNB{3qE%k5Ei7Cu_)f;9Dk@^nl'
        b'{o~B{<GJnot<e8Tb8Gthq@(YM?+eEy9+!AR;#(3=N<1a;^gHTzi|p^G(w{XnCmh4G<lv4P>yd+aPJp%y8|~BY$9&U<dHj(Ys~c4E'
        b'g3<m6c-A&Cr|*{d_r5#cHiTyos0lRkP>ppT=m}6E?7N1vXOI4O3jD*;?Z6m*tmhy{1<TmbN0+nxR}?ViQ+ezpmE#XJ)<#eV=swUh'
        b'po1V&Za#?-vg54QdTgY|x)#scO@FJgJ_0Hpg&){QfSW)kDou9pj9TmIcaYC2lYKkP`9`?EU1L3MsI|H;s^xiF1YQ%Ugw<NdD*xQL'
        b'(&Z2J1_MhK?PB4|fw==rDVZBDWnFMvs?44npRM%Lr@py?NpySIQe|#@Qg9#|3&!K2NSIsI^9!wQzWPRI{Yn-M#zGNN9avJOSS(8Q'
        b'l2TSzmo81%<L|AIcMT+kK8Z&XhM~S-%-7pn-oxlBYQ`^(FPIxeVqCosQXN1pqotGRI^!-99`r>ck=~_BGr#Iw>FbXtly!8aT&O!7'
        b'3@Gb1Ds%hsHxZ1Nj}?Yr4zC7W7ffsj2E!D}9}egPclO6($Unc!j`GF7b1R+xa5$1sdi?8=s1ok)?N#_4d$Y&6U7oU0-pRz}g^7qS'
        b'nuwKf3zuo-S=V@}9?BGc{Df;4;YuiHbG|}(P|F;RMbHkt$byI<6z9^JY7$zYcu%CiH$bH(_t|V#7XSQuNEuXwC5Dm`0VSS{M1-O`'
        b'%@)BjsX!_v7OH<OFLaIfY=(Zeo_iz%&yUhYm()>(s|iwV&t^O(HOg^)^5*a4in+$@Fo}r1&EvhkK7UkRUziBSNHzciCK6K?DDhxt'
        b'1U;lTxIWmctP3T`V<;|@O0R`dRXg9=+C<HdzA|MG5H|~k!rkL_6U|d*S4p}lXYVxntS=+gSrn9Wl`9nq!e@_AG)Q6#WYmY(<ru}+'
        b'9DIGDu)ZI1U4R=xi5^A0B$9k(?~wY+QZJ6|^T%#L8T@fsZ7H2ciS}%abHNl52;JfeU8hJ*f&!FkK}85^Ra6!4S_$;i?jBu=@&3*p'
        b'eNO43_q1q2k^Xpk;^Zx@@17;2X-ViRWBfE`O|Zw&gq!Sfu~46n&%k`lpq9A?Ug3x-x;rSYjTH?4x_BhEF2$9yB*OA3TsA$|yr)Zn'
        b'yTyYfIpmA?hZ6kOQ|>N((S7rYpzw#zgg(a2(oZNH55^LDj@0d>G&*hWr6^f%B1HW&THd*IZa@hH6I_5t@$&~>W$ge)I0==|$jLrm'
        b'>!V-<$%}C{7qxnPp}uHuDqjl6a|i#rNGwrOs%$`~p?hsbKHT-l3gfp(l0X!*@S9!(ih5=4a+c5haVlr>sm+$+NzG)=NgW=Z$m#(G'
        b'`i*lZXkU<DdfF3-CwxNBAd00%aizSnlvL$uk?DhAlIV{4`}p;%DGuU}QqcyPe9V-I2#LzF%0FW7|7Wq*VOX>Dg7$!DtuqJs7RZV<'
        b'4Xt&0Ph;H#Gp%*pz}{2XhrO+>z0|c1nV-Sle?Qh*&r!HbYpv0X5vNjXT{NrK`UpsTD>tyA%dp0pow+vJH4|&5OKPpf<c7ud0mN|}'
        b'<|hzGlOp^dg8e!8=|LPOxF1DYk070Ok&Rqj#d4j<1G_ji4<qwyty``<dmh+)k%wLLQ}du8p5rsJ=V8soA`jgG7U@sOOJ$|N*Q{k{'
        b'xxiVwAeP@M+bvXgiW_3HIPj}-Q&K>C{+lTCe&t_R?}5u@nWd`HeKHTlbN;z`ScLc*=ZukuIU)}stcA(F)+h4N`!CAFAnIVN%tPM*'
        b'DxoA4@%2RlL3vCnsq2K4TeS)0&13p-z{kY92_@%?@av8<x?C_IJKY#zvUH*Gd<Ogpzfa6bzMCSEKE{SRL_O~*)#`Z!^)NWM)>=4E'
        b'tLFsVx6jF5&y81LjLl1}=R@#sA}Xo1?kh>H=Y!x+ze3crQi8mdGFIXj`8ZPguj}`xOGSGpdKh~`re9R{&z)<=OTVN{q`x5)UKb&i'
        b'zS~(x0yGHP0@@1N2HFm~53~z}NArz=(0Z;-dE9HX`DTzf*a2d_C{LxyxhRE)r%6KXG5mQ$=TJ7$<qO|&6}|3K-gH&|$;B`2c(=dr'
        b'6coK)puAa7`KJPYfktD_$w8~~%N(V4k#%9E_0^ogg;OeLS1P}pTBNYQBwmK=uLc_N_l`;)e%QrcEhzetOZl~{@@<!O(B<Cl>KJlG'
        b'_f9Z7!w6iU{JJ3eYC+}O1=bH2xbH9Mc)TF`6_K5@{$Aqg|HP&I##Q-_%W8GG-L8%fS2XGx9CU5p?iw0$?Hw;KFClP&@|%LaNdKJz'
        b'>&gQ6wFMnF6huE*FnD*t_6G}wK3A~!*>Upn+SKoK{v*P*-=FHd{vQc{c<Sv#|A;{0>r<UGa{qzwKbYz){zt<9aO!u?|3|{VI@MWV'
        b'`iH`s^ZpgW(PR9qHf9_$vJ+Fye=xJ^cOQPqW_q`H3maO8HP}f*N7?6qR@T8kq|m37$A{}qR1DW`hkMf;X8(Tkx}t7_*<xy9^lb?-'
        b'>>ssM57*798m?PZ#_T0MMmv`e#6)UYh`F{@oWa<7B`}|Vhq|S*bGWVy^c>u4fez3jvLlUWKyzR|HHD7k@G~eN#COctG15I;ce0be'
        b'$K<@XxY>v}-x)Q1gk-u+FrOK1>KU$U>>;-yn-!>h263-ob_d=0RBf_HyN&iEpu@=P5oWMI0zW^$VYsdb{sNz&aJlTjqbPHDxNZQ{'
        b'0kXt~>#mBBoaE^5@Nbl!6<dCXIPXQe3f3}kJC3mX7IE2f>z)CG+laLdXy2`<yVK0R3x22H3_fV!LrBMfkSOIE@Ef~Pci?XVe^=aW'
        b'`8bI5SyZCV_IEOS&j$_m1BmBPw8lCIbP(n}PaEu}FB$B`w++`#2VD%h2()*v!R~$1V7Dzt*_qkW^x$ya^N*P=3m!LHP6H<ck#dJP'
        b'$;k#$Ci-L*m0vf%3CcM>`ZAUEXQ03ElQa0g3GoEDtSEgUJ3TrGa{@#%nT1LbI{^1h?wpS2z&i}{LC}jJ@5RhIeXG$v<FjVVe9$?d'
        b'GT0BmpZ7Xu?Ev+HtoHMmbp~o=-vQGL@N?<skWWzI?%}!-#B&Pt7RUs<<D*9V9AL?A>aR7{BgYCmj)Ll7Uk0*(HtjK6lssmA=2DYA'
        b'0sp-_(KmCMmCjq%qMxA&-9#h=O!Y*ssprhjwNSS|LFHnF9qx@a)-{N0>mZGZpN(!ZGyY9sCi1y&I<uAl_XGFLHQ9?VV%7tc)|DoE'
        b'$$XQ&2<QfH1ZkJ;FxsczL*HXZ-?1USx#+8p(Dw<<y?ao`eIT!mb*urc1$BS|pdQfl4r9lYb(F`#4%ECd2j~Eq2<I~EZj`APdDsFv'
        b'X)Wv+0XdL{8`K0c{kzfLRBE!H0zI<JX#W6swI4IumG_(MPkh{HAK_(X-x%fRtcTJ5d_vtnIs~h7@}beo7(01O&HiJz<gt-jll>6t'
        b'fIfm3?=xF$Pns>41Frxr0XaaA&A|L{mC4?NbPDUxX227mlc3Yomeg+GPX`r$65}0pF})Re-BM#!zHGL<_0VvgbtUoy^DG+EHMwkh'
        b'Gy2L_`i4o9Z7mzwO5ZVI-nze}3~{i}Q$MWPKYB|p8~G2j<*tKfOU-x9mJ#H;9@q`q_+4t_2zwZAMV~g>qm%}HP$_2YM)26+!EfFP'
        b'KUFY)7ia|<K$n45gU$tQLYQseGh4p$BH9f29O$Dk-#9bZ@-Xn1u)hdgc%bOnO`k$JL5DDw=v(~$hcO>~27T~zMtcJ7_5|9i=+nb>'
        b'Q$W)}yI~(i9nbiI*|PSB==Z>qrr|m}a5ZRfdyTaR_{Z1HmZyO9{pZw2jP@5{z7qbA1L=EE2il*x3p?f@&b1fuqmA|+;OImAYT&&l'
        b'%qb7U|HdO`%XvqrP7G`g<~s%c_g;X$4PFmu3Fy9j^l`XZFkcj6?M%8&NY6<Qi1eG3A%6!gCVS%xM*DI2zy3#v6LjcuX1xq}4X6y^'
        b'7Xq!Ilc@L2zyqK?<o623E^EQuLS^{?<_)Aj@}GPxE;peZhcS-!BJYPj!24*C1%192bb1f^5$F`?IQs8V^vP48O1Lco9fSX(OL8sO'
        b'fEqx1kq7r@kQemJl9$bv(T`%37cw@okaZlbWF5Dh<Z~aMhRk#fWqlO>t*E*E`|${b`7@x;g7y%<lIG4L*2IyW9K`(52=i#&$x*gH'
        b'j{!!HlN}7iU~q7Mo0z2la}nzE1m>`gLE@c@8Ta?2qn9D&UyP3K-$J~6b^!S83urd}+h~H%JELc;Q;jTdGXH|9SdX!eB9!q(l=~2<'
        b'1Ln~`B2C0QvKjs_J3UGl<2BLTgz(*6U0v*09y<)bN60@S+D`HQWps2m<`(ZEL&xD44ISG%SjR~>>(~q4Y1DS!{?XAMtO*7|l(W%?'
        b'Xl5L}1%C&7!8?S>s1WfKfr@!~*!efnH_uae&WxBXpZJs6@(9TEXN(8XL*T{#YPJMnz610%&>uka|6;a8K=;6XEASww{IuEP13d<M'
        b'3$y`l6>pm@9|Lv3{50@4phlQ`zfxm8`qdh1@zXWdl6^3L9cHqB1NLWYth=A7v2OoTjrFas)mYblL!85S6XEuO79u|v0#^WgK$G4<'
        b'p9j7G-Zz0)0e=d-4E)~$&pBhZl!A9LkO7|p{ugLBsK+y0cPnTBX<UB|o*6LDDKXji0T*H3P%uwbIx!DojiO-gDuKP|&Kj%#D;NjQ'
        b'm@U8f3ibPwqeWMUGtZ~*Hrg)(Km2vGWjgw56U<)FB``k-JOloxfj<X+2lxhP)>lzKpqIe=An*myoiOKr4fP4y0~!VGdKTpeza3ON'
        b'lUeJ5L*RWCG~+q5WijmYfU|&uzz2bapwGiR3R;Uf<VEDa33To^%$Co5+syTaEr5A3XgBPCoWj`lKVUwhIrEeJT;Je*z^$Mt=$Qxc'
        b'Oa>-E2SKMn$3cfcL!f=20LTsM0d*tZ=MnGSz^6dJ23f#2eiL&G_=(AkIbbh@y&vW!zy;thMtym~?*Od<EdpHx{vNoWe%@?Ze-8Tb'
        b'`ONwq*x!KtIPA{@&p#K-d+<I3b0f^hV7`ysVg4_e-vpip4kE6p`^}aw19yNNFkc6JrGT-1m<uN{whOokVP86*<`lE#W#AgvFGD-O'
        b'4*OEzJ3uRVf5r3Y@^6_fvtj-M=7IBIeiGOTd>wcW_&<XA&!DD5HP$o0UZl4M>GhzlPY$79;kh#cJPkTUglB3a@EH8vdBAL$2D%h9'
        b'bOPf7{CP0H2`UFAK#M`If=<BgYruy<%RuWuv_>MTWM=-#M8SSwEuQ<wo;F)P348?f3d}zQc6IS>#<vY@f75Z;i@|q*3eg58>OUAC'
        b'-++A$C<@vF`Yb3h70)5Ke*$ZOCahD6us(8Ne0&{t)4fLf8c=bW$^JdqXM+C=;5#6!T4*`De>CSL$$^bvJmoxxxv7cPO8W~tte{2^'
        b'12uuxfZQN22=l_}(a~>F1bGjUq{k~{q|NcjC>=cd=+`5EqZP5#7O<Al=A+WsF`edLETIozoc|E?pB}L${?yVVZbX154NdZOe;XbB'
        b'?x;M`h?#WsSD?4C9r_zT?KGIfXytvL7i%KWMIZ~tPUWOp>sqvH1?;DgG=`m_6XqdMHRhN%fxic>TQyww$e%|??*pE`dbsW-;JI)='
        b'7pMShfxiNsfLrluJTHM;fd@fT*9_Oa2K!3jw}2afUkB}j`4sTeKn3)1&>GMkAP3@H5Be_XW1xpYPl8NR_V5_YBcKDt%$j>G);A#I'
        b'g|*fhz!K1WP#NfT)Kw$KUIz&C!)PUV2SEYQUeHF+{h-rWdmJaX3X`4v4C7U)wGPfiTEOifQWA6+eqNl#tVe{b%jn|%n^@g-!*zFo'
        b'ZY0^pS1>-{cL0?8HXih6u#rSd%=+o*=+VpZ@cPZ@=vx?vzs0<@%r{*3XV5OtLwK?sLA*D9WOVc?*k1(g^&>x6uZ@86u|7Eo%)#d3'
        b'F!&c>Z(#&2v9ZmiBUjYsZ7vzvnm>4JeAX2s`xSPl{gRVxiJui3OQ(Em?#QgmiTTXP?AHvljqlt0DbuF^-uqP1(6b7-PmIjAnT8%V'
        b'o&3a<P5(LcxuWf#CGM_~r);L}|86>V=afxf-TsN9!3T)Db>v~2Y4D?_O*iednGS88GW0;v;GN2?Hq!-dZ1C1f7<Nth)TEK^C5i2W'
        b'iNV=Zl&#8krJv27GPJdb%q9IhOe2G{4clQYQIJK3{D1MCGqcW|q1ewneEyoj&E}z9Q*M3on}c^1ZQn|X?!2;S(`(!BH=TR{@#%O^'
        b'ZQo@A<JbdJz*~@i!F)D2zf#7z`Il!3XOO>=%Z7N)clKOHrOJQ!5hfT9<ZpiC%&jF?9Lr}ijO}M<o_ccB`iK&|so?V_cv)k_pR0_I'
        b'-czu^tor$Z^fPy$;MONcRZqK&m0K%OD5`nm=S{)8cnI?Ug6hA&fJz9*N?w3FjdQmah&Hl4f946(1@*aw=Bo{>XPi^G{3qs@%ufxO'
        b'gYyfnM#Y+rJvC+imH6|ur)GWi%&}*uD9=9p^Dm$I)K|{@B<J}dw)e}nH!m+(FzGX<;GgndnpAl1=Z!xx6y6Y=S5RWuR$Vyh&7T@6'
        b'@9Y?Q&O4**g8yP~4CPdQUwJ8~@Y=a^3a&C0&bi?EcM2yxx-I|VA;acRpFxEzGyQqCp>S&D?EMW`<xw7I-FL?JNou28XJ2@$pTST)'
        b'o9g%0byKbNMRvb|b1vBYu``1Ui>wQ&gw^XVn6>kaeJH;$XR@QqG<Wu6?24Spvu-~#d-n9;4@Qp}*@rvNowXU(nMG5S;LnJ2$^YT('
        b'U7(t}vd7{3%7f&p31Es~r#BY@f$B5~wgjs)Nkjx6^9QPkPWzRIL9~xihgPTKOmjmE0dWSRQ-Rvw+(c6YEmOcwMJ-c;EwvVA#J+5&'
        b'P8l_Tyx$<A_dDk%_?YQ`t>5>p#k#rYoPEyTXP<rc<2)|IRt)R3$t{e<t_Ha9qJYTG*W_z$smv`PZY8hVGN$sv9IxJ5Qrd*MYLL=i'
        b'Cx$TlA<cBl<wP%s*aFw=lhk4=7HOS<%GnZ274m&BA{3P`%Km?t-M7dXIAk`z9N72-5dBKoy(GEz!O}Ailsd9*Jx~l7H<x}W`x$17'
        b'A47#dvw~0D#o$Zc#o#YJ^FXO1`PKu)WawNnD*IW+=tto8XS(^sT?D@5T?GEpGY^zHw72dnwyPy`80>kHIM4_6EixLU)Qx2{%#Cj3'
        b'6Z^j{qh<G!Wb%WhrynRS54rU~F}Y|i3FY31IOMmiECEJ^t)iO5FCTcdMY2t5i#nQL2S&P>R%6Z(VXkRCS?ob?HHd@Dim8`vdubA}'
        b'f5x4%KWAkhQ4Y<VQg7geaseVWSS;n8r{z^|)=$n{tOUOmTPzl$tctJ{Yh*xGvDYm%6ibaC&7SHNxEeXuNh$w51EdegT_FfoFLc6r'
        b'!nY<<UY!A&g>SQ7*vqxFU2X-Y9_p2jnevVqt6Jyy=Zq+ihEsYA&}~qw_@?!i3e5T5N7eue<XV$~ii03K9st>qILWu=Y>|0qI3F(*'
        b'R}m*oFzquyl0m-tCRgUuV}G3~|LcrZeBSZVjHpNXqxjZKcy!eN4PD`+PyRu>qH7}87{}`a)eHyq0hrr1QwlL-7gHKd{{HEx9fU?}'
        b'BttZMjYdO&DvB}0Jj_Aj-iE}%?;dGgGbuqcGUU;h5pmoOfoqT}yvgB4#5)e*a1_zSgc|B*fN}y#hdo2pVoW8hEA;cwGGlij*2}0>'
        b'yvRapnBUEavZJ6Rs_jnXq3j6X>v1G1TgktcADD^D{t5re_peefoZ$H1R{t;PA^)2=#ew#%7^-k1q}Yk!Ruk%-=A0M?jDz<hKd;N5'
        b'opJ1)fdd^4bpp$)ZR-xC)b3;va}x)2;RNT`_vVKJR!T~@l0F@(+&N>z6k^UR6sxfl_8#T-88SqTQTjtm@zzO*+Z-IA%$WfypK?+v'
        b'ML>Dh3@L`KCnJu`8GsnP!09ImtAqqg%AW=~+q|*>ps}I?{5V~=IA-&VO{`EOKI7!mU8*TA{S0DdLyGKDARj>IES10-iz~ouQQ(NR'
        b'#bUAKPuc`__OC_XUZq<)L8YfJlc7<KC@Ept{KPRR2TIg6%2Ap5OC{-5GE-}h!H`cb{2&5jw^F)R4;exdnxul1Wl$Q@b3{vmHR046'
        b'#fx;S1++G44KlHRMKFWGP`-cEKx-_tOc5yX5&@}^u+!{XD#b;)gaI@=U9XyndP7fQ^m8F(ApJ`n8CWauh6KDDu2s&s@uO!HUy4W^'
        b'STN7FCRCTTNYy4ZDHp{B6ScVa*MQr!blbZPxo`ZG6lSm6mMt}>zd`684XH&n=O~TV!pNaKWv@cCQaF%$T$dHH5^L?^tgW4Z2~XcB'
        b'iVw6t8d4NbhE>>~3n@99y$(tIfg=^!>&%H)xTQkj_uLhtosiX2UWc&o8V4LD;Z<lapnQIFlUJ|z`wn)DYP-p6;=2xnJukrKbnm(6'
        b'KQIF~|I6pNTTgsnJ>);?{qX+}pZ2SpHXLf!ec+L#rl`Z<H#up|Hj(ikH^~rdLO>f}WD=g*ep5;_pWfUYEG_^1CiBV7Bf%JW0$`IG'
        b'Vb0$)u=!SA)Y8A3WjsD=p<fshR#{ed_(+wA3^pYN2>an2bBk--rnOSue=6+u=@sVWO~<L5Ht~NORY$|kIlIZcbGPBj5Hi4?6u|pO'
        b'jO*s&6273S!kH|+2Lj)G1n{`{=?85_<xQ$CpLy#hAeR?^*v6roj;bHW|EHVx+wFa2Wq(Rf=6F_zl^tG|UVP{Kt3JS@n-5le?QTUM'
        b'4(%&98~)N|4@W3ApVu6ConLL>={qsk6vzDfrqi+L9{v2tR42g<y}xNa8OZmU40Vmq=@+1RjW65;Q_Do4YjlGBqcFeIB#%i@=H0xQ'
        b'AXj5+P2Yz*353}JyR6<w#Skp5DV*SxSvRFmr33;s9AjW-m~2>_BAG$h-msVtRG2UZi3~!?@Qj3%O$l)VSL)`Qq;Q9z7S9H4WkBF2'
        b'Nv)7chi|a?P4Fe_;hTCv+~F9Qkp?s92!Rh_TCl`=tW!rIn{AJ4j#11buvGXZhqRgYkG4*62(t#}=qE|(iWn&k^u8kPj`qo$I`DFA'
        b'1{yr~M%I<U#6u`x5?~u~d>iLDM0ai$=pBJ3<4}qwKXrB*qSwJf+eS+X!MZhZRZ^I@6y_!VjZ<U~Fpu)(6Ml4JL_zlhqO9O$`c`2r'
        b'Z)dcjH=}XA^=J<85ltA%gup6fASq=V4%HHXM1Bl_Z`(QTq#x>(AS^Hj>`Rs!IZIRiGI-SW@^rP_2SB4j*76eY3}{ruR=h-2f)}Cz'
        b'1w4|m?)<tM7@UB*Km%E9axkbCdM?J<{poaCRB)#NAqATQle1>0Gt!TGNpW$yGwQdX;b;|!tz8?vTCGSH#6Lc3-J)m(LHH6|t?(`J'
        b'%f*WtVm_DJ+WI;(<RzOrH_6jJ3E7$s91`b+emW{h$D+W4A+eP3LjW1nhL~nqb61csdUfIew-nc#N)LhDJUnw-^VeN>;#Y4m6^=k#'
        b'WpqwkBZ2`>9N$hiu!uDVJyj8;iwNR5QyJPSM4H5kZ|@uoIIpfqiaI)?cnWDz<8eoO6w*7D>quO^HC`Q`6leducq?eoH$PJkPMcK0'
        b'odiM>YXXf-%XCu4(Pd;nWkz%a2t^ar;`n8=Ey?1<0AxwArI9MDrd}=yZF%%_X=U4NXR^F1p))~l`Z#25k`NfHhR^$HRZyD0e+Cuo'
        b'-%_#7ly2jaO~9-7^}$3`DS}0*zq${xfjJHlZ}cIq09Gh|S#&~F<<FD#JYS33#kB!1mn>>n0ulH9C*qbih!-N2kbws0Az(XsUGo;E'
        b'PENOS$;pL4;E^W07V{2skd7>*ym;ENewq$ItpSKH?xh1T;8`I4cf34t`oXw23jr=dH0l))%H7jetg%QEYnKD_?kus|GZ4ERwP&EJ'
        b'9f;L|7L`D~LeqiYV`dalE}M4zY8s>(c)rZpf=n=kP|MKa@>3YrN+HUaX-Dof@MYly55m$zMOHfA=Tf+G0G=h58rjhcz)Y;dUD-(F'
        b'+D%qEkbKgSF%1CBFCc~R!eV*)v^5+9MB7=^Qhms|3QrHY?WDutTw%wz_d->t3nISBi3aqL?>LgD0Y%ESfI35IppQ7HBf|sJ8)sni'
        b'&n0$qMLVwm;KgCBV{rV+4bxzrK&KUk$L>X8Hj8ChQRsY_fH}nhHP!T5F|RkvpZNa(yX1clOKI|fIx@e=u`!flIRdqGE$+(WHb@kq'
        b'+#dGzXRs{g^xi{QVjU893TsV379RmAVF3~s_k84`P2`EVxaGM|VTDylZUL4!gyhCz!cxR~4!UD2rixC9_ppzEiiHEnZhV>ywMIpk'
        b'>T7YR2U()98(F*twmpt4E&{)W`;a~CyuF8-mA9w%1Y#r>w;d}yg=nIT!Vf?R0}&qth=0C^eHFa7egR1m?njn@MoP<vr_=%Ix>==r'
        b'ihPKs*IO51R3x#B*6iPVk(Te`Wsly1CH4U6-NP0@bcLWTOn3=#nULJ?u-1<eW#v?P`;?VV+5N*56sJW52%-!&`7T;!;iETt3!ywb'
        b'wO&foGRNPiVC=+SXWPS8z&<_-Udr~yVu^0>QVglx4KSqdVPWTl8$hOQZxAMI<WdW!$k4Q}FzZ6`5<!YhMhYxj3+gt>)5X!{wNrcE'
        b'`^bkJiq9ef^a9u*cCHUTDhii?)(*f<>_qmS#0vialBJ;WR+ihneQM7`62<0-@+!cI2U?1T{Mbdy_tbK&eLNo=adC@imW_(VT7QSo'
        b'?El0yV6DGGfE#+5YYhVBPRQq9fS2Q-@xo$m_r|F`QR@^%KXFt}k&n9SxJ3RNvb%pV<tUl5M#&mjIOUjwQ{@Mz=p=&9L+E6L&cNxY'
        b'IKZu?MC&R<xoXNci?;U;sy^m~{7QxE9LKykMHWGFLjaY0H#3OVQI2_S3bd$vV#=Al3b4Hp-VIi6<A*1ZICAwJ<&vrL$EIj{-R|8}'
        b')K3Y66{VwB`38*Mv5JnCkzt94IdZjdC$Q7orvP^VUD0BC4J1oRftrvq<<sD0g`#D`t3*Ju^-E3}I#vHH$dt9d#-%<q#Y9hm0ZUsb'
        b'CPTr1J%fP(V>iiCz?hw%S8f1f_UZ$ij)G%WM$3hEPAQtI4}}dC?%|XKc=;*y7@=@>IFhGGsp}}GJLd%sfJjqx$eM_xWR9;C?|lO+'
        b'e3;Y5O<BX$dqV^ussJ2_>cSF3IOX`H1NK%%J_@N`F+~c}Ox<*NltTA0&)~!bfSt_Zsok+tK3=Yu+~uayJL!w~g>P|ij8Ac`Rgn2$'
        b'!hgsKE5PgS?<dI+XOxK)u|)+IHb4E$_1&RU_J=UCXji3d#nj%Qm3!FV?+seF<RKsri3_>X>fLRVd!p8F@5Y4foU(nAJOGFj>N$iK'
        b'0x#&C@;pHKdqqnNoGSqw0^pnH;60quGnrVzks*p=WcQg#Yt(v6A+i5-r%hhANoLtZ6*l_UuAEe)HOI<|qx8#|_a_y5h{(Wo<qeb8'
        b'=v6TC-?54rn6#^Z@?kXKqm*hasH5`RbgcT&yMdhnh)@LhacQzB@Ns5zvdI1^!%kX5-dNM~w^q<|I&T%UAy&1uyQj8rmSZX=o$7V0'
        b'i-3NRlM;3TnW>nx0?XGk-8v3+Hgk1SEuLEs?VJQ2G0h&!Afl?)=p$%cGCS({ezFN~IZiU}N$7C_6C;6|7_SvT%^ReBZPFHO&3RlG'
        b't_QA0G@<<4q>g@)3@i=u`(z04la@*fXZ=0}(9g=flR!n&^s*13Sy?K1x5WD1t0e{GB2r?hE?_PBZ56t6R!wn%MNgHU2jP3$D~?l>'
        b'a9Ob*c-k%pmpJO<qiUQ}{&g}nXObjLCWKbeD<vT42W>j)f$Qpekuz?Yq*=}yd^oBiOnG3^XL#F2bFZzYRpDe9DS@Ln4?!YVEd$sw'
        b'OLPISGwFeMbmuIZ=z?_XZS9{Yn=l|*JGhqM!|+X&$tm~2hMXqh!^1k3gAL8Zg$PVvqE2El8CKZqqfKd_)VC;B$+ascYcXATB;W>#'
        b'>r9A_#?r4X&}Glp9+*rDvf<j2$)dwp>j5PBs(YC!99a`8H9j`!%t1^MD&PR=uO{W_!;|Txmbk-MVK`#Pa4W8{RBN0jv}h4#HQ`6M'
        b'nTRKJ_!CG%I1(Ek7c6$X40+}HmIHOe_1mn$i{f=;5J0WnJ(=91(aSWN@zPb=HIvq-7Boai6`v!H=O;}p;?3mrEy*W!G}#a?QJh5_'
        b'+W}u)&%(@ONiF(Ialxcsr_mbY8{(bu_IN9a$6o>{TF#&REKo5U?EE<REsRWh*|wljV*hLwAq{nP<)@3C7iMke6yo59aFH`&K6Lp}'
        b'1oTRAZAcpl`DhB4<pwV|j!rlu)&LzU+WAuw>Ks#!%oP5pGdw2w3sd;g>T{-?1w63a8NS5IS}X}v^)(($?zSeGDs*dWs;#8>#OcLl'
        b'HO<vlCx)BCV}M28KTC$OA0DbZZUJf_C&q10N&}Gg6Q_Ry;p_m8d=z;409Boh@&lha?#y}Ao&E04BqxA%`eB_Ab{!A9<U!aa?uMj2'
        b'0I~r>Ry9{PfH5Ku)Kvn=r2vu)-G8g>okKN;?Kw-WCd^{sL(U-LRGwIeOEt@6IuoX+)6WT&!byD~^!S6~16vh{BVckddEkBK!USa6'
        b'UpU(ripKuN0{3;8tm6>xKe(ipqwiaZ$B*W@ubV=JYql*g-kxCUCmOd}w*@7A$GgwTI2gW`_)E&F3CC9xP|vR8T{&rNJgqo6-8u{X'
        b'T}m@PmA!axj?8g+LigUQWSEAQ0TJ^4oYUTz&;=nN2|yHw(5&tW<LQZP1wwC3AqCrUiT5lQIfHpOf_VwlSrKl|vP{^&#_Ws4MFCrw'
        b'^AlEace)rV3TrS?{<jI=riyhV!R(pfmkc+GdN5%EVm`$wLQ&NzF7kpjJ5uI&XQF{MbP9pX&a}hs=WWea2-oC_$WR|UvRWs$1Me&z'
        b'$*P^8o+b>N<SFSCh=@@#G24h_Jv-q>vm--518Z_9-^PwTn9$fXmOm2N?+rEE<eB_dmyecHKLYb=*@G~fe+1?u_CXk<W5N(CONphx'
        b'{8D@|Xxu-M7NIVEycPorFzOms_yMPkpK#<)%o#g}b%MlIf990GpU?r57ZIhf_CbC0E>Iwl2|Fj&OF<WeA9LL~%OQ#gSyuE!`ZVe~'
        b'&RJP?kwgKYfPdn6b^?H9v-7eODq#SQkbsAYwXkmDN3bo{vK?1HBLq!kN62y&fi9NIEg`cM6HOA(LgEmBaclv>x0m9CC%K1m=4CCI'
        b'AP+zik|$aRI5H9Ny7gV|8DZf&{xu@eMEQ;hr+RU9KzZJTBX7c<x7e!ILq{ohqT1(&8@EsRR#(&nDGj56SS?>pE`%Ef#8Rn7Rj?AH'
        b'FIcHx9s>M274%%{(-TlR3*ge|DSL!+>qIt&oO&Zh*)#5V3UEvmslyzpfJT=Bj)HSFvJ@`K=m}{o+|?t1p;7)~g2s^2QOAY}bFd!>'
        b'E>$3)7fqNdh+8Twgmwc_uAER~yx}Pv^z}!(VuCkmVQ{^u7>~;SrBV-btQZ2k{(f=!6BG6Tq`#Q?WZd!Cgl%7>9&`K@h$!Nk$0IWN'
        b'0wctFp5q&Mc(^=fq9Fh&eXdFDh@L2%;2i1+uY?0H06!BtQH%N3=n_YKYv}ZZU5vb&3|G>Sa%#fKmUTQbQB^~V$>Nub=a-xTt+q&!'
        b'?;2ayAz?OPsl*g8j+Xp%wE$Sj^z(oV<W15R7msNe<FHMxl}(g1kVm85l#&<?s;GH8Y{!wZ<Hk!DHlJ95UAmwtD_eHSgg8Ijd}IaY'
        b'{0!QYu-Hdw;V4I9zP05nqzPMs*-_2*hWQ<{<DT2&4bC-=*>UrF$&rS69k<3k(;z3Q5c<2!^tj{ZI3ROc4Tn6>GdUhDpIgnWhI#Hh'
        b'^5JHFGrBqtCT*Uf@qdquH`mBK1LOVzo3Ef3=GOVMNRqGIL~5E2QD@Q48rf;I?hGtD&9}3!{@>%$*vwcIsAkP_m>&;uCWm}li6#CF'
        b'(SA3s$94Fk<*N<f7l8cpdB$(XHCIqWo9tp6g#Ii~8oPWGl%;*9_nK2uHo`gl6fD^S+tKHd1i8@h`FQ5Wf|N}t%TI8KByWvEklo5<'
        b'8sL(qz9RcwBr{fK$bn@$;4a^uJOy0H%_DJgVb-hTWlt3tHldjbvXle}lAIT}NTB<S(`aDzBzM}oNJ@fCvy5*V?&0ah#x3Lit=Bw$'
        b'9Y`ECHl>F=y{YE$!>I%*q}7VZ&*tqPLlzm3LyodTz)P3;_rCOb#y3GDvN?FZi~jV!)=&BUqDw52l9Hd6g=oeoLuY>byry|z-l{q|'
        b'xJUxmH_62Zn?IzS?4MP)Ii_SBiIH1q8Ebh7#3M}6xTQwM-dz`CUK^(xD5o0nwu#F4y8>B=E(`I#DsudOyx~30%ZOT(i1wB7H=ak_'
        b'coXLRP~;3p-bldDhjv=!ok!&{whNVwlDbMcaG9%YB?s#Fj5jC9`6XVg?tPi@SL23cS)GrA>UIHW;jGAww+q3`-{6Y~ym&<CJ+N`}'
        b'r=nWSHOYDRiX6|5)4;zuDDu<keOZ+C3?wM?ZOXMzG;9Tkm0QPwUD#@?2<(I#mZp!nTp~b~FRB%qOF%s}z7A@dXz@B*BEMDz+WvU1'
        b'y;{uNHuvsG9$&&A4v;LCQl|@m1F#e>gcnQv<x0~ym2IFX!k<=Y5H^PLf~WJ+#S%GdYc5|tUgnltYML)aBaD80xJFK5b-hsCofkLL'
        b'nv0(|pI9+?n#Uog)N^Mfw2#3K0l!)uXns!Awg)(^zvpSP1|p)Kg|@&_e(zaqrLm#_p-tyD!4>E<5Cr)Aa+g`8{fWN`^L9~LA71tr'
        b'!7LtEhK`rnES<^nG%>Q4R%4|LUAQETMbnayl<PR?d6kq28c(5RYi-eDRhFn0H}9R}g*j8C3>f$CpJj{c`tZ6YqFg-Qc|dNdv@pcD'
        b'JK&5BXukAl#C#{f&LTklc@IgwPlJ(D{aVD!Ut2cq@a@-`e<{*Vj`=85JtMLOeyFyGAp3jSN|`+aX%v^8Me7>1YV3^zm>Xj~t65gS'
        b'432?bdN%{AR4<B1OgO+HHmp(Hc~+jtcihs4TMiNcoDvk-|HL|0Ggn~^Xei)5?jDJ1qey!hA_e^11aK;P1OO?&z0M=GVRiNSwh-iO'
        b'c-!TUFULGzjyb*>Yj6&$W&$e2WtC`Ih4xe>tRmX+Gh0S_#ho|a#MK!2JU|J^Yvsw?Ac8&GCIT`F|8Jp>KF}3FBBZDV0<}(XU$47u'
        b'r4gzRr<M|6j<FU&RLH+nYaz!oMSw}dVJMfXWYO*qAi=v%P~Np7U{5uge1jn$O!Cak`~l$=K|9feg8^awGRAMacvp*RMXIOg#!R(Z'
        b'l=b%5{#&&|Z{h>BeHCjl#sTZOOkiesGkjy@HHsXS5T|R^e<IwqEC04=4lAf^=X?A!k>lW)cjFvR=8rH}Svp3=Sm*YJm=c(0W&e+|'
        b'c<h8)$`tY-ulYbgxuy@-tR&(BWgXTrk9Evp9b3`|!=9@F%<B*|_0=)$t7DzCoZ4ieVl7S;0_oEUB119PHvxPsfhh9tfVc<xMd9$7'
        b'j2rXEViLgHKEk-i_m)JoU1xTUT_Iv@ZZYTs;r%B8I17BM+~6AH&M}}qsRWCgfO=E)9g*neW9r;7GGK0}3(n1)F`6Z8t4c!vVNzOm'
        b'ZZ;PicAXTc9{2BqJq^lHFl~Xqn+b{cJxM7UYA(h|sguRLHjH^{jMqR+n*TQy{?bV(vx%?cdv5S&YS;5GIP|EFrun1>C|Tv2u@ahh'
        b'e;}is>^3He7x*z42RN3Gsd69@Px(Xx9wADBuMXpw=jUUjlx=GU2tY<;n#}RDG0zHr9^Z!J+tDRt11n}$^MvqE$KzwZJQLp`31j5T'
        b'_-ARTd5}{MjcS*Ur9L)Bt&(Y%j479nEnlY5OmrTT$EX^PBkb8`1Kmtf6U^hh)LlTCWxNDcVCEPpqu^W9_*zq)3E2I}m`Q|`277m4'
        b'M#&f%QVUNqSrZT@ninQi{DJy18R|XGF$>3hhi=3tikI`hbLYtT1g})?CGQ@-@t67!-`MjI2QiincsMo+nunes!Fz%P3Y;@GLk7$X'
        b'GYpFq3-3U>@)<FtL$Q2<T+lH(>KPgxSO6Cl7@Y41cHa}_#eHzJ8ao}xT!C$9`$vuaqtK_q4ZedpICB{m7%z^Jfh4pKbOL{t%ZRLm'
        b'$Jl6;ANy?o*z4rV^P|h}jlCZfJkxlp0XPr`P$PwJo%R=@cU!uf&zyy53%h^<y^15GAiYyG4-M?#0zHNRBhrzKbm0L?<b6Cqj(Cz='
        b'vKCy*l6|t8Kn8IvYay%=AUKL3*Ky-#qX;2Gt_P933gJI^{B%@|v}wr9L=eHGU|GS)mw12{Z5c(nf?h!X^e7@&Pl%NuA(kWW2Z^;I'
        b'Mj3?w7}+vV_sl5kzni#!Mx~XK^Wc1RdSt31vG+ViAM2scI6d{F9law|jg|Rm)F<8^nYl^aj)7ltB?v9R1jon?Fcs!KAtu9M{WdXt'
        b'UKA^jjUI65F?C?PlFq`tr^N>xs%G#o|6QznYqS>Si%>cXH8+ZDQS;xx!__7R0`G#jK-_u^{`#Lz_%!t4h7AOXkwMR3hNlW@1*-jA'
        b't-$;Wms&Eq0t#BOAhmeZ_iOY27Wsb*{lBmKewo)sQ(qh9Wi#cTpaKnH8BMkPSpNRe^@1PC-aAUF{xchh`&TJ*;_i~-slS2^Mhl`2'
        b'&jTiL7gtNTc5y<EgNvFfki@(%0$XYR6~7J+{hho~{-`90Su6=r6~RjL=ze&302sj#ib{Zi%-yr2K9*<`MoSL^eMqnJ$tlob3KOTy'
        b'7zG&2PVprcZE<E8-lu>Ec2G>NY&l*>h5@vtVvz9{@KF6#Y+8jR4*O%(b))1W;8!qfN2A63@ttDvu+eX068Yg+4WCfgCGbi9={wJ`'
        b'3ce~0qjzJ$(j?~RKIm=C%m}p0Q*-N@{4DdvqUj}w_s_h?vkaZHsdqR?BBLF>cizK0%aKx$x8%M&bGy(HJ!-xtoJ+R}9jZ}aw^V-@'
        b'`uu4aD~^`aqb1g&(=m*4v|P!*K2lDNI+UYTb~5D1nR(@pj8@U$5p^1~vWNw`nq)}gZ9hLkN6SNDrFbD#wu}rZ{gw$DEe{?op~;Y_'
        b'(<mvn_*_$;Ut9WXM&>7wSpZ*J=hktpG^(R9`}yH`tRldAe!P-)i>m{@H$nIq6{?6jCRGxnRIE&yJVM1%&U3fT;~=7-=Gx9es5A;V'
        b'3BYaXT8I@!BQ2~<bCRk>nfZ{bj>!>VX{WeG^y{;Ta%6-$D^tdSCq;jLTc<=7heeLT5#|O2g`Ug^U#D+`@xm8)8esswxaDM!cbI#('
        b'%8h<~22pl`xi3?yz>{)bxNYv^NIb4;zFJELmF}VGV7jHBT3)bJKq@kn3W4O^Upp?304Z|~arAqf;~PlOAUx>dxHQrZ!VBheh$0ax'
        b'!CDk9mJI@GGix-gCLhq8`teB0Sy`$CJgKzLZ|?y#e~CLhBg}`eR*H*aKIUou+X&MLUus26^9b)8q>oOe$4+M`m*R@oryZvOT5~s-'
        b'_ydPH-X8(+jex0zaKZ@=0Q`DV_%*cKfO!opB6CnoE-XCYSyx|+swj*kn@}(xZp_7UJ{i@%JyJ)@HMB*?f_cgNBw?}Z=-h&lxpDU%'
        b'7drlD<RUGHu6vEe{I<~N$FyJz$}2~jn~Ba3<!7pGlJ7%`v!f-|d)l6IV~v64`3O8&*MnUSbcdW+Df*@=!Yw}Ww@2LjinFWtL`$44'
        b'A=UfRkKH~~sSk)c^aWhRKPV|2=iGVeTe<4&=sfHBkm5b9{_~Blqe92;APq4!<_4kfY&G-S5#S>O-?trY!lF_0LqZ#x8zO*uVcy+2'
        b'L?GHdBXl@o4M(XM3mJ4mhmv^7*)y^J^F_~(kZbv4J=W+j-=RwDjxc8X$lRLDTpX7@LQ2iIM21IE_P7zmxOK~ncll!%ranCad}M*^'
        b'u#oxX$i)Qt+N5YAJ~%1lvc5umUj5B7!J4;3pPnYlKBKM>xg-`jPvrQ;2>Gb%mdN`DA<*@%xjBB%Gg~`CE`q)pT-`ae)VC+&K&&2F'
        b'vE1s>6r*HPd}?ymmfbs;-;@_COVdbOu`)ME0G-|sZ~zVO_2WoS(CgzUya&Ge!YxD~1;6m7b`PFwzzY9~Og0Zird*Gdd4I%U*ZU0i'
        b'XCu&FUjQxP&<Ojib_X=Y^a!xNdacHjtT$>vt$I8a9|1-<1>S`&qk3@grwtwPX>kKxrZKTege;4?NFb{(;&ZmU{;uuTAU~Gpql>5F'
        b'^%k6}$Dh<8C@wlQAHi^i1;Ls*4T2+BkfuIJ@HrmXfd+b-_YYIlAwVSTcj2EAB(WSp{%<{mT>;%hM}`AX(8n!IT61S~YJ67m?$NBk'
        b'*Bf!gKW?FY!-h^A5wJk{-x&5q8dNx|#^{!$cx*AIp{?5M!!fZ4H4ZG8p)*MHIIG5Q;-CXjk60Df`6du^zlOEOA*ufyMiMlpGz2lM'
        b'PT9zs0?`Zsl0cc#P&JKcR&S+ePg;I<EgmZak3ign1)1=06A^0?tTG9oGKq3b;$NEr3QUqiCh0K~dD1lRoN4|SrUlnbvN4mq^${dD'
        b'c0Zy4^=04@NP!2f0S}!4JWMIzk(LP_*}K4Fj|DueW#D0F!NXYx9t{`4qoor(E)9dnRYZF&epIHtrpuO5@F|Zlw?}lfM{K_WubQ-2'
        b'B08@`WDP`I9f-)e9dZ43E5|ARF;DjhYIF{Z3Sf7USdH#kAbqP1tH97_JhnAr_M{%u^o;2PH8;j^3=6{WaEyq>1gkLNQ<x|R6aN|u'
        b'D8M9#FzGRjJc-Raht2;2TW}4NjbZ-&f%*unkB;eS4K}9NY49<<Nkfe3(=>uHeYQq8rr)Cxjp?l#@tEGO2^iBmHIgxXgGM^0Z_&&f'
        b'(_hleAJbpeEEv;|YGh+NTBebMr(6>_7NKg7c)L9!YOa6ml?dfPgmWMw{C31~*uPO_U<Q-4Tc1TM1%j_Q`VmZo^&+$kxWhZjf8zi$'
        b'dNoV_NiCjNzRz(<DZ8qa7mjkI0nEbHAEFP);DZ8)rVe9ShzzCR*Fg5;=u^W8|G69LI<C2j8&ifgv<!Ipic16l*K6REGx(;QF>=@d'
        b'<{MEaH35M1JzQ9V;abq*F~hjQ5Zm0`hc~wq&9P-h!>}Q?E(u>M%nJhZPj~}p)z)tAli%R?(bNKIYJfCdf;26gqv=x6Cwp*I_aIG='
        b'-AB`<`)O*xjp+Z5rm!ES>GfSuH?%-K&@iV5WV-u#cMj5d64Lnvq;uXJonHj4&cjjZgLI1Tqw|aV={$)WzZv>p(K#~oV{{5~A)V(S'
        b'ohR?o8H?Oqiy(uudWSxL3JEeG369QKdFLki@|P<xGR$XdYB9r{wNbqx0uJ%Kt#G~jd<df%vb4#Vsv%%}8bx(g%}0w#Md_0-1h7>U'
        b'^VQIDw|ys)-O8!nz|(U%E6qok>cvH`9V<iTe8To2o48F4ZAQhu(&7sJ5t^t-IzkWFY=t*DpTCt_IVd%)d3=c|XCe9Vnt}*2!VpV6'
        b'N$>v{a6$-gi9d90m?Toq4DAziZj`qbg(c)J8zv>K5y<(yZ7cQ_70z&5x917B<72g=&rsE$QB95PJQ`PZU6k{ZEiS8esQfQOJ8ebr'
        b'dF!&9gtcTP>T-!IP{rC=<%yx1!kC@gPtWUkd&u+l(28F=-X2n&7c1W$icv?MmUg&?JdU9i&p}FAD!A0%;TZC~HMHWli4&Z~5?or*'
        b'@jpYJ%Apkp5=S`YTSGB1)z~^GbZ9{2Oq%~JR)kI#-tzejz=MQ-_Xs??-u7K-gU3F^FFKV&)-EM@A4vPhAze6<i!Z4E!w>*=&2sE='
        b'YALXv^(8}5C$aisnCtC_x#>IaD0Fv>_Q6^VIDdWIN=f?K+aBvs69L-X58D*__HPuIFy?nd<u43Dw^~5A%+fSm6Yk>LzU$aG<k>gm'
        b'*g4eT$n!Re-LEuZuFARd7SCX9cF-8E>f$}Lwv)hFy9M`Ocqd!=<Y1g`M7ez^Yx5ALvP3<hq(6ZzlMg|<JGmDm>7hhN_K+tVG+yFJ'
        b'9r8AafoJLc7su|T($63rzZ~*B4T=sWPIIc)fEOb>ad@ROQlvRYH3__b62m(K)4#)jj|)6z?-j^2Md-Bq<t8lsAp}4$;_qWR)(?5s'
        b'fi~(B;qh>Iu6~ST&*h~2l`<TsnD9ZLGwU7VmJ-5$aK4xUuJox!L66#cOV4>$0(L=<Tr+gfx1vmxa_JE0N-ie%EE$51KVhEbd^aEv'
        b'Pt;Ic0|uU8><HHY$WGsSM-hG}^|8Swyj=jV^!39`$!!QDsKuE@L-+2ZXwsaTY%7U<|2W{R(0ma<mX@>&f#dvVNNw9yKvSrnCh2`N'
        b'85Kitm6vc$32azfBZzH3#M?r>hsDlp1m5_Qzz7V?qYSM7B{Lz&4Hf#YkpTWdiMhpPU~OM@2!=euA%}3Nfn~gvV(6Qpg2>P>;OEV#'
        b'Wgn*HCh-2+AH}4!9jz6dM!iA;Fe)_t*LQSEMDY{|ED={GC#A_?5~r3O(omVLUJeR2U~_JQ#LMAq43!9jPOlf|<pj{4eiiBH9rW}L'
        b'I(h~h9FLprVxPb4y-7rd>YX%_-ivfxAM{)wbo?;bz@9OeiR-%Xy1HeG&(Yjfn5$3>LIGJl6_0xVhTG7%5FnH03=r((t`e%Mad@-n'
        b'inLv-D#a6L_;b3S5Blywx~>a!G;;I{z^x+u8A<7P9c_c2_CZH0!1A28SPVp)Ahuw&glcl`&Lz1R_{|uIzUI>F`E>8y^kNtmoA1Uf'
        b'<a$2cGnZ~)Q8>p(;gu?cPZPd5?@xn>7o@G(2pQ(O>c1m&FK?as-<*#(AX=ic5Y?Ek-re-*TpCn>>0XYh8U&JBWG9prgVAU$I(Oyj'
        b'E{wOEW6I}X%6J&_=zqYtyc}bjgDC_s03Fm*G1S~XnIGRZj`{r@-0ysFAOig_I57P|gg4~xi!aao1IY8ms4!Mzhxzq|e-FSljpqk#'
        b';tF*oU7@#yRO*TYnY_VbCketgQf$qB!kQgt&DQ(srREHhLA3%iAUF$7m<^Iz!3$Erf96@3T)XzfG7wMg1o4!I9q3RD)PmX0^g$$^'
        b'qXQj*1Jzg)4t2vu2wm;FBT<W&2AO9#--H45x)O=bDmhzi0RuB!Bd-oBjx7!^#%s}H)S895rZ_d~i&xok=C816ik)DLgLm&wsSJd7'
        b'<DK%AgI0d^-kOXsPYya+xK!y(;&TGvVvR!2!MN&)K?`khW8N9gn|{aq1L2PYwXnUF66Q^a04b2OZmJsd%Z8HD-W)JS4{CIlxc5V~'
        b'pAUd&89bv-&hJnSdQ?EViyf*#?=Qv7qp%g9{WmHHNw}(JBgjCF>QJP3UdK-cJ)r=&ycKS!^9L1N%|vdfT=A5!BV^DM1j^oQ?T4Cm'
        b'@c|%ND+KjHgT{ctcB~dI;HD)YOfYP}^t*r0AM6kh*3TboVO^@PFn*EQ-$m791Q>Rsz!!F{36gdQ20gb28rb^8uQ{{nPUkVXc4B}%'
        b'W^oO3olbepG1V~lK<sH^Q84|fWd+8O0f;pMiCQ?nV`{)N1sXZ$=o>I^5Uc)590fXWe#h8=XB1?AlF0iNY5bX(ErjvPKqrXQBitD9'
        b'd(79l<q2-WdyVtf1N|dWelb7>!Nq110(IZd?trJN4wOJuXl^B#9|rttm|rivGQh76@=HZ<{!4&d&&Bp#9P>5A1O}8p%ZK<UBOK35'
        b'uodG!23V)D<~S`uW-oye>r9jLoBMeJZ9~8230eP1<~)Q0KvALd$q-6kpwZ;F#b)Xc9mQjokqgsSAz`%6iNx8PLBm>CKO8kdqHis8'
        b'b`R6&uU(D%UYAOk_x)Lv)yUeKt=kahJ%5h#yA=o!Z>ai6EE;F3VZIuNur<xf69d&mv_R;;&kT=hF%G_Bn$iD~ZDfwZm-5Pi4T9|v'
        b'i&Kxl-jT$K<KdmJ$$9tDCN2upha~{-4CGYJ<w(L3636`WjVZlHO-e#@O#+f2PsYhWh}iU{$>%#U2pLc**kY^{9tqMpmJif312xXy'
        b'VOADBaTY5prpkXmP%j;*vXh}l&cgeLHcHeZX9NS~f&sYxD1_UOj{#h-_LGuE@mu)I#X+4V@)D~}{D%6@`7p#L|FrSDu$uZ82Nth2'
        b'o4IEsM_)02#<{L@SI~8y1NFc_^l}yQxYGfyuQ}R*3Kt_tlCtCJfwh%km7T}sn#yLDZeITJk>l_T<dMUea0Q~=H1HM?6S4N(k;Ryh'
        b'LX=Mr?8AQZcxl|{f3j~U(y|fSOeix3;#GPqd0|*=Jf>F03#f!<H46G4lR#qLe{gNffTGiiGmOcCcz!(wVSYByc}D)-OiAD90ytrN'
        b'=9m7euEEkM?S7L8tNC>KzYI0az`qM?i>ty~{{`ZQ!ta33AcT{lUNg{HEw8JwT*Y9`OEE}86moR_sfQo$&<=RC0}dUSH-oMa@u`Qy'
        b';pr8LTX`8}tDAv@)GrzMuEw4vXvq>XOW<go&#FjuVn|qJSdG(!tlJw#w|>Hr_y!#Erh`AXLG2oco2qFJtbdA8_AfWt#I}$%`UvAQ'
        b'{q+rfYh!(zXrH0q%FVyvC~9JZB+Y@IM=#3{irQxQFCf4RNPD(!{Efg0{CM^7fDrmyV6r_UsU^IRh=sm;&8qh}tzZDS%!;QlYd8{B'
        b'vArUwezM;)-rsSh&laQ(kFga+Q?}SrwR%-_l6qA!W<JBE=MWvY`#rb%8yp6qfd7OTQ1%iey$9)-==V&3e4S&k-zySZ&jTkv-?|n_'
        b'uRuDB<rkm?e=82FEbQU*v58kX;6Xejp0lOqw>h)NFEY^QYUOOo3VHpdeose#$C<vW3KBb_Cd>^$C!BFRB}m(Moo@Ms8hA`d@=X;Q'
        b'Mu*viQ~r2}3F=S1*jEypVv@zgg6J<LRz_mWm&LtLGQa3EuoI+UO(PEZ1pJ~jVB|mH*sWCQcW$(_s=m2@seozehr7&8{aX`+qy9B<'
        b'Z#Iz|Ly)1~e4p-OnjnlfW$rF8bEZF9Ja=EHfik37lns4q%oa#Hh|T)PNGvKi#_>*HJI1~vV}IE^fUfIU`&ZS!f$Q^qXrsKH*m@Q?'
        b'yNP{pX&VK)(04cH?f(7W@mFJfSD%XmeD=*?$luNOe^1y%wU|u|jmTEbu|v>_a$`1$RV^>IwF`kC4@>Y`TrX;p=!0r8_+bhD?z7b)'
        b'C<;uBQioX`Sd@Amyt(9@SL%cs{F=z>Ad2i`4-YfN{ZZ;gjIF=O3E+U@>0=7}i|pUh4xHZ@VP5O!^$YC~@+R;JxHXwg3ze_-r~alt'
        b'2~z_{lldKF(uY?|cY^2w{$n&GI!Fz?dZ69;LwfxZTTqkGrUni>q*Ve-NvS%p76--a5|&C7uiSz>)j0%gc!B?%IqwrOxv=G|XZxR#'
        b'>=V{v`$U~0WVW}|l}4k~9x6>0lKv914@-+e(p11{fxG$w<oo4EgPYJ=5qNDYNy7DLTrlQH?bi$MvWNFW86?`MOzL-fWH!vEhH=G='
        b'%~%mqk^JEe#VVpAqjXCp&WAG<n8i(11at-<>EGRP8=FvDs4WS?zhXlxjKy25Il$I6Nz{REBj^rX6L&1@FNAwnP6y^YpO}RtVJk79'
        b'VHFY53_|ghBq><&nuNqMRz=In(akzu`%yrS)L67!EeD*-5i(J*>xwgC&=*`a!N*V{Ivl0xhmQtAPGZPIy#dN&y-Dbr1~eKqF6^(x'
        b')r9|CWO@}rPH)zSWCYdXX(|QaMVdprxk_RUC#>gZKTxB!VB{dt{1_~iBnlDo{dM(VETs@FBj{f$DXI!Eeaxlj-+^PJ*g2Va8y=zg'
        b'0Z^i-n&kHe9Z2eQADu<eDg^M6rXlWwlJuAbYGX!Vo>`H*IO8S7!o?YMhU(}-x2~NiE^opCEw*w+3}QYjavMpJIy7U?-i7Esd!BVi'
        b's^aZMnVYYsuU?e5HSPmUXhzmPwHf^8AQh=)IakvYL&~;YP49Y0K?G#e^ZOOb%Y82p&){yOE!3(GO;?jP%x(1T0VrZfQYu`B(3nP%'
        b'eLL&#eQKfFPu_BY+sI_}szb{+_o}ZJqm}X|)F-EFD}Z*rxPv<SL7uTmVpEWhTor3xkaWK-AtiP16|nI33A$9uob7WPGsIy2r>RiT'
        b'or4m^@+p3~zc!$0Uc0ckywdUQ?i*P*82|}y_F}g33diN$Jz3L?XlF>{<%@62Yu-68afh<+T27o4)W6fWc?H^ph2<7r=SV520a}b1'
        b'E9~XSkP73j5_nLwanZYZd!LBd_4?KCdu+c2cmx3Kl})>Ho7X%+cl=ME=g)nPKle2_UvT|JWP8qEUXfb0sVuh{esF>mlZ%?f?CC?9'
        b'#RZnL)OjNak^5{RwPd9O0y-2WeN6$Wul2P{)dC<FI=69vxPtQxD?HCJul5N)<rqs};U_?zfj%ib=kqzh9NOCl#y$^APR)z#6oOzQ'
        b'eJ7D;+^5(RB~yszDW00QFWr_}bP8+LAzLesfL{&r?rJx%RC$uTR#0L0ir!u3oE=%|GeVoO8qHQ?*^xwgE@E<^aJ|Q^Z_H{(0h|qe'
        b'K~kKh*m>vP7;ljD?{piJvTUJ-mvXFX+4)qU1HPd$KRCn}z8iDjywn@j;p#MnbH*LpB!u^kdN||-LfFr_u_oetD1aeBmD0D{MNL95'
        b'3$EON*O^myZEAkSR-F1uZ2FhC(pOKn4sgbmeTm<KzMC9a;x~{79)!*kE1v*Npt5NsI}!u50wJqfkjFqK$Q4Bk_C@ZCIx2EM(Jm<V'
        b'G!a0B**vA8<^v){?0f)}zUCB`_yn@`FknvNGDI;U^>OESg1k3CTh;Z+<$3jrE+XsNjd(}q_8d3EOM9u!FDdE0V!#q+?vnvRH*>z+'
        b'8iO`EfQ88Xn#$bU4DvU}sX7+*c^36K6nzcH4w_3vOT?D#IqlG6Kp7|O?IH)T*u0#yi`mZ(?E-SrMqOrX*!LgWLYl}*PwhM?DW3iq'
        b'Tlvn|ownj~$Ow|;nXGd&0|LXB6fZDvDzpaxmx>wb70z-{T=*MxPy8D(Wyy_wy>yn0jsPmd;8PjOiQa6bOpQe;AS2Ra=Fv*I!a6T6'
        b'Jtf={^#PU`i)g52>3c}U>(UhPl1*kS<<ze&)CZPbnH$qTASiRQmHqklM$>u{bmm3ane{>&;Z(|avk6%Aoe(6h2rEL{MfPZ59jsaK'
        b'9+p)Z_~Dt3uX{b;^g1r~HXNVteMPh@GvWJ}L4%8@w>Qd`kZ?zKD{OFyu(g*%7DEK-FuhpV+QlLJAd-C#HHpEX9+b50+(~b4zzV<N'
        b')G%MI8xUN<NfMM|yv=bsg!~>punUQ|_+Nq#!eAWNLILhI;iSZMfm6N4&3#Lu7B?5nov~B?v6nPUH?_UAQcx>sg_j&_F{Zi~5OX3n'
        b'0KC54%ZJ0dbGY@rSxc;}zMvP_30KV>MagVD;a{4A>ubj-<}B<3j4t5X=QX6GqSsT=>!|E)VE4Lqid<25Y`XF{dMzc*MW-dzH0=<T'
        b'67Yz=nucLddGCpaJ~D{JT5m!>gT~-eoZ)>c-H9*<AQ8Y>D3$ov3V_d4)N56v_kCZZp!b1&TJIh1F0A(go*N@@vZ(8O-2BL$YT8eu'
        b'>lSDJ$sK1lPP54U{V2Y#AIysox06PgDEQ(IBr)cV8~5Q=!R%^``Qr_KVS`5s@|!T<zJcS}UZ(Xvcu#DvZ#mla!5ub+@~wkls<-aU'
        b'wU^%O3m<<AD>2PI^(noMoj1q@ROdugBX-q+P-mMjv4-J)P|SJ=$|U#hzX3yIF)8tXnMuqi?|#Nf%<S|NfEs(FW${$9hWZkZMwX=b'
        b'Hb}H9dNtRAe2W#O$F$3PVazFn|KnDx=ikw|-T(wV;PupAHP(zE=udmqGCh@~L1RIY|Fo6wYzQ71NJP>kZ~~V?^57yN!YqNWi8FqG'
        b'*oP|p*SImNmtXxzjp~KF=4J=MU-Hsp{3XI<O!Ypo<|zV%9kM%7IbZ;{xkhh8K50XHdB9|xcZpz|Z`1QT6ullruj3&gZ!fu4iH!1I'
        b'e&yEtCcy;tcG`VmaD}**(D;urng2qNA#GNrpqKwv+rz_3qPNh$cIsPCG|xP^p6L5z(~s{VV_E3kb8V|HqyN26o^gXevbL%D_B`KM'
        b'&&eFc<}aRx->f*HUueHDwo>Z6Fj=NM#6DU;h0FK_59<ZbN~uLxU}t}S5I+%*)jdj4YKo%r3+Lh%%JLFbk#Dh5Wj0XslJ5fqaQ(n9'
        b'k8`-@(ykB0DV~5WSY}5+%GUu~@RZhoE&L%IQik*dAs^sKeGu|B4)-BPI2rthx^sj46)xld2gNtIEY8<v#h!x!rPVg9B2Z03^zcJ{'
        b'|A}udZKKmeP&cNQ@QxEH@oNy9SYf;4)<GXja)-Yv&BK;f*g{G(_<R_R_<ihp_QvA%wJ4a00X<MVp&Kwa-b94a%$rcq*Tv?h4U%EC'
        b'Qs#(X?twj3{^^GCPd8{fl+^PQMuz$?JYam%_{STIqkQ)&;xX;P8^%BIa|-uehmXdU#W#33iywqffEG*+i{bt((|ZLVm;CsFOym9='
        b'Ak+BU8*{nE9jd)z?Y<ji1doIy4SqCDBpJ%sAl0dRZrI;zrUl570x*rUesx1bQ}k+NF-~H@DY$~i8>_WT77SqRLh`p{XmnO`YP2$1'
        b'{u{K?6V1@6fy_SGh!dqMJf5r@WmPh#0J(y*>_&J%-ALIzRHZy#2^+Xu-59NnMt!ORHoxUZn`g3NdHFAHK#)oZLi`uV76{@<yg?RU'
        b'!7F(($zS|8nM}$J-ts$Eg0`x)u&C1LD+H|uv<n+p5j=dC2*Gp$j9jSEMA$ku2L(PuM8?j0MjZK+Sa<Gb8cS%>4k?%1*n*j#6O*B?'
        b'9I@(K&bxq9M&B?-`vz@yG~~Q7^2XgEA+o;d-sKw%Uf~d_${U$?@9_9^&=TUVJcQjK;pOHGeAg!a1`s?{n}la3$ao#(8{?oGqymm|'
        b';Ee~ye(`IW4~oqFav_FtVLEQOi%8%Ti45FuA0jLjxsj3}OXYg}mxM4LWdAb5CfPk|QfGQHeZ{zOvWM@~1Klwm>7GNwband;oPVGA'
        b'O3&T9-iw|7@29=h?Q|LZ3kdut<^q`OJ!HV#*>&b>4^_6Y{@*>rl_>wosJcp7{SQ5LHM0B8M7zcH|LmdOh=6ynD&-FreBDD;!h*~P'
        b'3M$0Z62e)_v6Zr2wA}wGL7zP<&+C~>&#hBa`R`t3KIw6M(!*C(e$q47RJo_;0oo~c-2Xi$=KUTgYx(c9-HuZ|bBDVVC+5C+)#JF_'
        b'?K|o%1%;FoeV~f-FObd_2O@Q{pC4*|pfy(y-Es$%I)2|ny>n=;n$xj_+0#9Dj#T+(k8e%;rwe`QBRtWV^2Kh;9~MT2EKvTbr?f(O'
        b'xW{__4jEvHKIHFr`N1AXS&xQBeO;tw4s|zc^MAS{I)GfxY`KfWSk$v0ewi_kNON>ra$yH|5d2jJvM_TmtneGc_-fDQAQ(eIxgyB*'
        b'&6_B?rITO5C*w$h45RW3$W4pg)VhL8>~l^wmwLK@$}3n(nEy4~{FR)#LXk_zFpzJ)GJ8cxuHfHY-_PDA$ob?_@@YQp{TEFCf_z~v'
        b'eP#9%yX)dNR0|8HItpuiJ4-%HJ_hO>ZJGxm{yA&h+@rK~@nl5_rubW<`(N@MIFBZLmq=Hq__|FfSM<bV{I>(sBB1%U@UtUr8v^?B'
        b'j1+WZJ+<)=nR|)d0ekTLAu?{Mz<g<z+?4qDxo^V#tcTn%Dn{Dp0U7{}FSx##WtR7lVIU9WYygykOi*V@34=fm1OGT4S|CQ()9^0B'
        b'%e6EX$TYm6=#vAD<}jETWxk0g=I`s3NA;BXOpjRmbr%!W1CNb`_eA61;kP+5hVGfOJac|J<&zByHEt=JIARw|ZTr71ibo$FUSbvA'
        b'@t=*n%|$JzsH&E-dLw(*Qg*h*$|9%i5^D}p9aI?}9ZQBl!~C?kC@{pzvPFRp+1X)Ie8k>EMw1~<M<=}XMeazP<;ZxU|LlbJRyVI+'
        b'3~PfUgXz+Q$cPR84^ZK*NqA2&ELKy}l8jXc#?!^R#A%M{@8-M7Z#if*!4@mgf7$6Uv=uxpCRc$M;W!r=B)77|k>Q^v_H(3-45}5k'
        b'4ssiCKoc1YvOo;enSSW@1~HlQG?+4-zHiWFAy4CRfpQ(o#@Vsf^@xrg1}}x{5fh7O|IrOb4(CUX7p50fjkDU%yUF<=liWZ)@5^+3'
        b'0Ee!;3l1Hs8s)TY-P9ko8eK#Axo*wlN=s}rxevh&7EL|V+O3I|gLucLjcVNHXzH$S>gI3n)!AekJ;gM@RJ?@m>HZ6Btjw^A*S%un'
        b'd)-!E6!b(b@D^nEObk=q4bs-*h~I}Gv>9FT0U*~O95~+U-v9X=4nq>f9ECWNA&w-m^Ie4XnHw>mcD&II((to^34Xk*yK1rI0On7y'
        b'Ib(S@Q{K(b4<Jk$oey8Dmm`A<--p7k{bTnfmH@oD*iOxH%zJ!Rd*B|&d=uc<EE$p5;GZAHeciruM!E<@vpl$Mx{-G4%xzq55avC~'
        b'E7#l*b!5<D<NPjb%||{s9}9Hb5Z4!6W1#l~4%E2D0U1DY)oo-6vjftr%!I>--J5u-qqEAVAuZTFTD(<o@aQhzl^Qhx*lf9{32cNi'
        b'wVSfZl)v#(KAle}f6;B++?|XmH*^~}@S}$rY%=5eZiD~h%y7$u-^;kb0Ty^a;>=~-U7Psx?z=XzT-yye{eV3ow=ziA-TMGP?|%Lc'
        b'KP;4n=mf(QEBBjPv6kqf96Wuv=`S2WZ&@q%qxYF@M%$fIBex{Tz(6`4>%QwyNT@f6=45&2+=rHZvL@O8KJXYiljRR)UI&?e9V2l('
        b'(oKCy`112F9t4mw%ROM5Wd9c$n{4=s{GyKvi6gk1`UJvHORm26LtUx7lapCESauUuxGbUS@(ovH7uU-TS77e9zGjBo<e;5q8>JO='
        b'^X)+Ght~m$Yh(uB9c^68b(!AbKPZU<D{rWgl~wU(5VyW}P{;1ESY?{CvN{{3dk=m}!eYrcu@<2Aw4+^X#8E!(40l=lPK|b;tBC(r'
        b'Eby1}4fm9z53U=)$%GTW?Q}K1|1|?G<3EWD$8Q6cu6xL9<8ni>!e<cYg*#**YbsEl<qZp#l3|RDzzQ=Ekr@+ihV}C>s{^s*@^`i|'
        b'=292$etep(R$lC~^R7c4mYJDfmP?ht=H+2vmiS1ah%XZ54k<tBDsS!5Y?JdsSC%U)Ki5?T#@^o~55}P0@{hXw78yfw?!lh9A69v?'
        b'%a3pypi=k*a<KpfWgfE+b5>0k({vpYD0G;-{`nwe9`^EC>`5o!Cwt6#i9ZlQ=ORp@7uu^-_;hUaGH-Uh1wR0xhF*k%mMD*Q`8<*+'
        b'Ba|Q^^Y(SiCb?gY3AMlK0*v85GYE{U^)DQtKGW~0<_0g|M<T73OY!@~4-ZG`utFC{5{buwU5RLQa*@H9@EtDenJ%l7A1I;U$_W8j'
        b'Zm`VPH@;(@&0WIt-0*!FX<e=7eB-MZi>_gX9bDqq{`va{?imR@(Wm-1r&(=%K|+c&k2`bejm(|vo*iA5aI0mb)$*D%<ym8iby$t2'
        b'q){C&T(>-CtQ9n2j0y6BeZ84nRP;FdmZ+|!xvZ@@eTksxiT_jcI=N`G9({{EL&ro%9U(|;yIz0sZB)87bE%P3oOm21g;F{u(%>-4'
        b'a!~eds>Y?sGLm7NmtzeqvXhQE+fH1;nP{*7L#8Cgn`+*7Z8BbrMcWB--bE*>IZH8=4``*-?|-l8QoeJY*E!lJyMRhl#&_|WhaVr_'
        b'{_?u#XrN<RSN-E%?HCwiX2BdL9>+mUef90Yd1|*)9dN?_kX?;M-H>-Y+U0q)tHHU-5z_@vTxf-j=TGT~ipxiI(vGMuPXs7S5KeRF'
        b'8$S({c7%6%D3Gzbbqu%`#Cdhp^9ri6xit95vWQASQqO63+2Q8O9*B>s;<M+$>}q#eLUVFY;!Q4DkkMn<)V$WTr6<`v=T~bi!AHd%'
        b'^SeCrLDM@NVn~NeEv#rca+2(jba})edna7PbYF@)Bkd4&c?gj69Pmzb=ca9VV_?x)vIFb#-0?Oze+9o&VhbW4JtZbP?sz>nLEf&!'
        b'UJeoENjq+NJrf|kJF$z~|6#LDMlJ>ltEZtjXn(u@CxD953|qsrbE-n2r=xQIkFBA?dL(4k{zf40@pRz=1UZE-Y>uVke^S|?Z_q4n'
        b'o-9Bs8+sZNhdKTHCu1+h$_~UX*W0l8hLYmA#_u~iy`Jv?w!+p6T!r&U$OruR9K_nb==i7C^G{F`=J>l;6)J>-LRPrd6-VrH8jQ(R'
        b'X-BKq^92A{+&amXQNg7R9T&Zxe}IgK;f-_m`4jO(<K<KF(vFY3p3gw`Pg?uA%Zo_*A}u=~ayj6e59hVDbbR9Vw1BclfSEsPQcJ4c'
        b'Z%Lv)Bs-eDo)1BGl(3US&bxa84lE%bhIe1)UA&l|J|B&G5<S|~(dhM@1VBq#zvfOgpry4P?|VJ(fsDrrFL5^nmwTjFzU{fZ=;9^f'
        b'Tf8D*|G6hCHI=dhl~qT}&NhE=fT(l>0jPGj-uBCO11+YkR9$Cq3q7y&UmZ@b=a{#_vDNVhuSz1k-16yJ#Wzm|)y+0f{&7*q|9Cxb'
        b'g2Jcyec_HOucrc}ewjGV?Z5CO2%BUFs!x0*BI)R`8`5uW6*dx!UKAg2AiAa!OwtcZgDOFuzA>&+T%jgcX(}oB_3&?P{yT;mL-0|e'
        b'Bj4*O1Z}?Rc+m^x9rMfCF0aP|vMu-I?0K(eKgeNxa+ZYK0@pN>9eG~Q%OLl4znm@k6v){&uV**ND}-`J9yleIcD(5IyZ~~F0P}%~'
        b'wn3{_9HhTGZ4Zl$ze?8b|GWN?Z*WnP-Aap#4)Z?!r})A;AX|@A+Vyt7Y}u#nV2aol=&>jNU&h`AuIYOJAAf&7+hD*)9TyP+a~lli'
        b'tzeiNMmi=UUOFLpL9@Pq4$16f#!2hgaT}&Xu@G-yRNIn7k`lDS(i1}^G%PVsDc6b2tjx#|P0`Q)`TlI`Ip_ENJ|2Jcx!3#izF%JN'
        b'_xts}TU}P!ChNv^g(VXcHymhhneTSah5zq0p7Q2#sin9+B=ibtndx@UhRGPa)@|&Q+-$g!D7K#20A88qcFu&s*v6YQFB2f6R@QF1'
        b'$VKca3n*0<mx%Wl#?jHho<m&muKLXZKOXAc%r)NPi_g)IBNxvpPoEYS-BGi)vU<%?S#e3d_Ru%zQhRsR|9I&5=0V<lwemMi8B4f~'
        b'B>@X|FW9zV9VZzjE<C%SXF>G*tts(i-Eu{8;`sP6?#GmgDe<G-iF4@Bk~K%s-zyt#jtWu4y17B4@*T&Ll(rsvIM?_i8J(gS?H+~3'
        b'c2o#5DmPf37#%;{t!(IpPm%6XA@C{8t%#tW4TEPszwulYtb|dc@z7EXcf(33H4mlcKhpJtN=t^4n?F&Ud1n5^!7aq?4079l?y0r^'
        b'>~=|PbL*#l5|Msf9(O=)?(3#U!j*#;CM>k3r_^UQ6m~DLR9finW%IApOxK-hnSoNBF;#bFx<$K9q-#jDq*-*e+HF#u65~;ns&aaX'
        b'w++rwN;8y$vP>bNmr0AO$9WxLeqwL#sW>lL-LPsx$ox+Ov*y<KzcH+(y~lYKhM%D(w4Cd4{sQ%<V8zF_t@&!jtFlcycYZQ1<M_=@'
        b'9~6cz@Y!n#9qMyRf+#i7C|SD~CPdKKrmw0m?B=E}2+eGuk>(`R{TGC9s-ltKYcU`3L_f_!nNoM=wft8tD_*Ye-|&B?fK#o%;^jBb'
        b'c4k!rk32dhHdl3fE|+F2PSE`(cCujhbJ?$&ja5vBA|%IFys&CPa)zzPk?ot6V@l63)hfhUAIMdaOiZ}%N*ftRm!E1s=IJJJ1-*4b'
        b'r6sTX$Aq(uBT1=}8(Z8gvu2!|eS|3*+hnHuRcRuXdquu^$sG4pNRl=Ct1vA+<QE5P+4M9cU3?MiL|PQ?J3Y>KdurbwVPDy!Ix5jI'
        b'MMqoS?s1ku>!H+J{0XsAIT+y@9~NB-VjJ6e&!O;YpNcPuun1eC2#N9YbHBq_U$Rx!?}d=y9wUOLHF-lKz5FrtTgp$?h7AV>x2*4R'
        b'uJ5UJykno=V>~QDy-NsaDd=&Uq4zEtA)UjjOstK~^I3BM!g8U~%M+y*xb{@j!7b19I9K)9r=hf`8S5mKwOkk~s9GskV(2DZ;^L{G'
        b'T6zX|oD>yQsFA3S>xDhnR%PsE1w5=Rw$_)jm%^A`)^XAehh!~_dz_1V?D6n7+FdKTzZUik+s?K;+v9u|*|E$%x`!T7-7onxfoplX'
        b'$GHHS&o`n$jEVAnEJOM6fPAj3)^^2VV^ocjasFH=C$5&rQwxkoBzk@R>;BE-ZK(xC$EsQ5KPA<^s(%W>oM}j+7h-Ues(p+*$QfI4'
        b'>zVuC+ewG-Db}-XU3HkJn}0B_PYi56(~{KVOzNrKEwW2`+<PRP4;QSTur)7`Zo}+H7doNGIUdGhVUIh>3!3&R>obz%DTn2XxzKr2'
        b'eBBmC(~z{VDv{CHdiE+_mrT@DGDmz>*GX>p+%>nWMaJ7~o`xRLaQToI{By%c*9B%8PKkwU*o2MePxx1hRD(oUdbmLjTQTK{Du?l1'
        b';^RX|jKrUcC~KHJh3%F4YEgy1Xw@h0aX#aO-GLCi911#;M(g!9S&x2Vf*D@kk<k73K0Qt;;@xTg_M&l@M6Dc#-d@t<6hW^G9MU}1'
        b'Q!?E)V#p?EoHExp@>*wz`y>V{Jw;LK<WVB^?0aWlsejilI{PoyRs`6;xM<uiX+GN0chPwb8l3PFj=|QWH<*xIam5wZnnPt`I@ckt'
        b';92k82MtN8E%(+UOO>11VbA&1IVx+FHnQjK;L6J!`$0HYS!pd*+L#Ty*kYylzFkfl`;(&5Qd(;(tlv42v!1b8>nj^5FIr!=G~L``'
        b'CF&r#busNzIO+O(vVh0k@JdTvLuu`2yFzyE3beA+x|&rg8L$1FpG)BB`agN=nf+z;@OPKh($t&U&vR0tyzl!nh{|Z-^h;qPH9Oim'
        b'&U2@n{oqC6==Jh$?=kOBE()!a{o{+~rBu)S(M8w(K+~H;<yK~YZL;YLxxMOQ?bmnAS=3ZD@lMe#`<{!x`gYJZRcv0^{cq=e-@kar'
        b'=T}LGn1-PGlQ;fN;ynXjar^fDbuEQ=O;b^NQ66REf)hP+>z>6x3|XcQ^Il@0*m6-GZHu4V9XH;lX3M+Pq6p<EQEpJEVs1AK)NE1h'
        b'a5k{;qVfYGkG6~s9K_MJLa$qk;5L=IC3Jt-J~$76^D8-usUFwmY#6IpMXl-Ba*@VHG&yv0^>%;y`vxIXhZ89?sP|ugWfY0s_Ybh@'
        b'*f3Edt7h7R)ba8k|IjI<figLXyA&*}wLa4A*$*D4vFSwWU`-H-a|Is{A+SRIqB6iGkze2_#fpb7j*8EI`eGLC+eLC=ZTWbok6Hnx'
        b'd@-3CP85;d|8{DY6D2akS#=O6f`_3>qRAjr`+4MLe9(Ue8RrtgOt3b>d+hf2$rpS7u-zO|{^IX!x1ehN_II&IRrKV|k%M}<A%l87'
        b'=XV#F>6y&Jnlk6!mO~f1vjeYX2gQj*n(W{>g5S_M2EW7NSo*#QDV8^64?mL~UXmTr^!piwtVF>nohy!C_CX@KUZRopCoo(Bqr6BG'
        b'<j5gX<2`Cz-z<wW>HpVXy-Dv`F7{*zsR?dS3_qg?FHuAc@}tE|ItapeqswQ|Af+NyqZlS9!AeC~91|>OgEfj^_3SuNur538rA#wD'
        b'P-?9ybyl|2T@d2etq8oP2!b!jH^uP_ng+SSMy9hfm0Hcsd%T(cizxjWail12t|k8Ph4ciI;ixRbMzR)@)uL4;%mUHOglP$XWO>S4'
        b'?h=)s`IWr!6F+Eh`IE~3VO#cJxcP{0j_C5BTa&aPkKdX^BmFCx`XjaSo@OK~Pl!t#+48~vYVX1Q0^fH#f9U20cZh0tvyO&Db1SW8'
        b'MJF$u>2CS1yXL#@MUn0%e%?wc+G<8@6>a&JKHHI&*})cjCKNL1OhFzOa*Cyg<LFgQd10zpaR)tFMo%Wih@oJi7%6r-y9L!Cua+uY'
        b'j2bMsb4Q8W1w++H!C8e|?EI{|<vEvN7$_bmUjHkf8+1cBNGNhgis@ab$)rNb(3|6D5YAsE9q^3N4Gpur=bg5*_@#sLZZ5=K$#QI5'
        b'bb<H0jW8vXp&X1(Z(cd0W1rxfU#?WDdYC8t6O|G45W<3Px+ksuY-Nynu8RsfK^moOqE)9X4ASb_b!=jgFmSHan4fS7vZ<_8V=`rJ'
        b'EYq=N8toxTsd8gsp(Z!lj}uQDx-VdE<4-&%rrWM)-)c|>jbfV5wwSt|rtTVZx82<Bj+f*do3-XP705OUHv&Zu&g`47;adLQ?OfGe'
        b'^ICT!!V_*59n7)w>&6Nf{!B#!$k4Q2<I~gg$s1AQ{Bx!B&4SErMcW<6qTLw`7h;RvTJ7U5rLAAYTv!uMt4vMxuID2!szv3CteR5g'
        b'No%2Ir%q&L3pI5b^Dx)_Gd##s+I`U@ASN0&4LdcbAsSKuc`EAC(1{x1WQoQwl^*viVX0O3>mGY484WUOuORAD*yH!?rNEy1EtYQD'
        b'$WR7_PGxFsw70*?7lo^qG64y2(0EyR;jbig=q(6=sm%JDyzoAlIMjNZ%865%qHyC9uU%m*LHl7%w^P$?f4IBWKGGd2$qn{TzH`Bl'
        b'6U>PXIUydts1_UZ*;*9VwMw>llVxwv#$EfZ^&2;qDLt2fbr)*Z+@v8HQiR{BJGaJA7BcJ%meE(k9%qVPv;88nRf|<W+@Z-WV9_ZH'
        b'=e?-$9Mqv`;~bVge1~$TaT?O?9D)dC+ojzV!II{GwG8TZ20+8;c_ohv=lt}$3W|&KkN7wL8MkX|^WGLow^IZg&!t{NU#s7=)nv+V'
        b'z8SZvpt-VzbUOzw)Y_M=|Ak*fpSUTc%Z;VXhT&YxtqacUFv@T2@$iX)SZqw()B>e(h-GT(bcx0&<07gh#$S1kRT_hYV+F!IEM(71'
        b'7o5Mqt=-;rfey$0BykSQzNom-4by@Gs9_HbYcK{<e*EE{+JKhs3(hX+98CR#cbuH#9x9==Fq~dsW0{e<**`RjSWeE-<j4xy>DTCG'
        b'I_UG<ZeEiU<n6!j*HPostVM}VL|e+}l=S<rY+RJwdsf;^rYFD7(mXtT!P$7B_Wkkp&n_5waq}NarL4%&a`b}J3Ef8_qU5S%>KieL'
        b'>z5athoLuNeIH-3gqb&*Q7Xit4W#As3(ilWpGbFUt9?T=d`ckO9lwjR(~sIJ*XQSaHEWz7y-2SlTcXOKyj%BU<&DzWdmdv$Q+()A'
        b')@nMDto{)KvL-et^r$E_h_t61fi@M^8~D(T#KRXApWHzmc4xEnH4AlYsNv6w$Cy1qZ?^2Z;M|TV=;>?$^=fBm$$;alXm=RnBkY%Q'
        b'D8%zVC$#=Qi?)jDH78ax6>6s1NA(P?R6Z4HtfzrUqY*6eO(A7bxqft4mU3E(pfmN~bf&_=0=CvEt7cR&%)Di^ajyKa^v2Hc!PUMM'
        b'4LpqJv)u4TCtsKB_)2E<VK7>7LR&SD^(4hzdB^7lU+wGulE)xSIH!o7C_nBy`4JAo4|fYc&cA$_Ir;(@aA@=)|3eck%Yti{g$Tz_'
        b'd+wd}qUE>ff^*RYd)kFs$9CgIahkGXG(E+(XIpTch6@h(;*h3!6LsV{Dm~6KhbphnN3%fp2mXs5sYE#b|4TR(9lZC9#tSUQE1C<='
        b'DHm#YkF<}w;BFVUM^Q#O)1tfJoCICD=X^com43=A<1aXM&{kl;14(FQBW>e+M=>gm@UG}3b$@Ik$FU{H?{eYAj;*ob^iENw&r~|X'
        b'ulAA4^Nnxw#1fS&ovVxq+GhbP_!u30k+^vV7qp%sgx-p^gsj*jS0%HRjQODp_YTg{_BX~a^lx_@jnVQ9c@B7R-d42Bs+%NKHDHU`'
        b'D!1h~{>n!vJ@2R}Q>Qk1@2MB+>YpwrhiE(PeJ<J{e<SwP2I&Q-547oFKef1>RYw;!w1_V_8R(r9?$3l|kwJTyYKbaZNMX<FK8{^='
        b'XpwM0acV>vni<*z_K?+4xxVvOMhC?X3r2S<c5mZjgW1?!<B+ZZPyCh9excXyqJvox3(<y&i{46~$-6>A9d~Tg3iP)8(C|An{fp^|'
        b'b5%TB?PKorbSLyV7~xWN^gzGxLLEoBwYi*auG)%R`<E`G6Xj+=lFqjL;BtNs-DRF~tB7UjS$TiPpb!@wYdP+6egnf7X(Q=_1|>C$'
        b'WS|CpA{+o8jT)5t2qDcAsu^P+##(MQ>uqsDP={#$6D*wCWK+o8s9cG!a2Pa0X!JAKssEuzdo_17tw=Jv-1s}0x6v1!)vJ7{zYi)-'
        b'Lv+O%I_}s^kE1KS7039uJ6xzYyg|aopzcsfKOOjG9Oo;n!a2-tp<5~X1Kmc&IdZR8sd$O@DyoOPy$YR#u~Ki`kt}_zfPQbF+b1K~'
        b'YF70UAG++%#$%rS`H9I-2yLa+<=p71{lL$@+*Pqp?5O}|m-7wi4e~s9q6%hg3+3}BG8%<=oPW`GEh}Blf5141o@jZ7)f}7UGlp1`'
        b'+ta{RuezM8V3dje22xoF>+>jSeiRK#7k#%QnDt)p$}?+j(+$XX89^%fk33CD@klEFp*Iym+z?OOWNat%Ci)@Imhhn`eKW=FDmpRX'
        b'{*$SUHYPFS{HgzgSmgAvXw_kqq-qsCn-bv7>56CXWY`$t%GZj1Ve3s#sJbt}s-}ylg+22OM74<78!fP`IFw}^$7B`G`?>92cn2b<'
        b'uh3M}+X0aCF9`|qVb}j8ydAtk_>|C>g%|RnqyG#w+!3Pp8x5;&ThS)<vB<ZTO1l5IGMZzJGw2Z>mIZ6yYx_pHoNAZd&sFO<Rk0Oq'
        b'pSu+eA7|BY;SmtGgk>S`-s6jW=+Ad8N)grf`IFui_Kpa3<4%`zxT|(gnf+#0#apNwkV8>sLtV}g=<f2=jTMVYjv%A?lrgGHLOyhJ'
        b'qEbd1Hs*+5wU^Ti8C5oKWzf<D2zRG<Ltf04K2F)wpxr)9V`I>_82cGCS>`{w=$e%<Ck_Th7Nc9%tG2qUNod9$+oM}U{}{+vLXSY*'
        b'mnaP>jaNN)Eu)P(-Q~R6Rdcn={&g3XC)SBAY-)3ual7|CcZSgaQ#r0pxbzdX(2A%?y+_17vKOi$)%5i|<7t>m-?zNNc;xoxH|Xps'
        b't$gnxK=)kl+4{{Qo%58q^1E7FMIkdi&^)LUsW=yy_Fcd`yHeJiz>vkt7#0VIs{J^>NdH$h4%$^$8$fm)t(~PS3WzA<q?ReuBCV$N'
        b'i}NlN9?e-C#Q9hjhvY0Cy6OEwdN#9;aU6|Q)iG8kvdmOie=e};ySkRbmuJ48_*CNis^1xhJ)N6%#3yHQXwKqcRqvaB?VuwA`<#sh'
        b'IcdakG|R{gSiWO&(&h<M8nk8oC$m?ybQqIJXI?E+baXjLSZB0%-G4w!YJRV)d6#evqvtLX+I0JsCgR_ydwX&zpY7;!?&zx7*=66^'
        b'rFubZQ4R~Wl3HabePhM*cC7FYZI*d!m+;W7*yv^~XBdlg?z|>ad8Xp;Vl--hr{xn9))%AhZ&}~vT;El*q03&-rOFfE+c)gJ2y^HQ'
        b'tln7Q$_<QPM`OBLblBJak1mv{@t@3=*SiGaztXRKVvVHJbu6$lvE{X{lV30U;)h+K@|AM?%U$konSsyDt7ue&H(1DO;bK>A=P<gN'
        b'pfq6Tu;C@KL7Um)o_g0C1twR1`!~Pmb=@i}b{DiiTp8~3E4?w<*h_yg^l9wi-Mbn4Vj7i_(e#yKs#qrElqf)W?^V=z;og2SS4Z-~'
        b'E_wo9EnFEaydiE*?<#$6!|+&Pxu3?JwVY$<4gd2TC#9<Qm|PJZFxIj5C%QI$QBlg=f3KLtjW=oX*l7ns;-_^9n<@l*f+Y;tk{_X('
        b'j%aGRR!M5Vma29#iqT!d4$^4{J`;9+HvS^qLtN8d&29(^GuL(8+ZJz?TAQ?W3GU-eYQVkguZ!x;`#bKL>B2plF=2zvRUN_;sMav5'
        b'|1~|u?%&vZ?>?bnUBU%;$fV(2**n{5@ct1g!cL~-@{Xlj#|WDdg?njNhiF41x#03u*2cVs)n6^GgZ3(&KNq}IEAdS8xE2R4+a~bm'
        b'ys$yS=0@RR-Q3}GxA=BN?kwIbrzh=H>rhWh10$>@Cqh=0{$yvm+!hAE75F7xD&f~{X6(Or8u5FhQ)On%7dyAy==8i0|3~MR{!Y(D'
        b'rqHwcp;7dMj<rGHtPP(F?Yp0=GH_#+`KL}-RbW-+rdrin2GUIx^U}}M>1yA7H`dV6;<6O?HbyAy(0r12%%J3^eH!S!f?@09-r?M>'
        b'0c6kzC|Pq`r;xw%GH(irEIKEU(gthOhC^&)8^3Iwu-{c!mmqZwXz+V@dY`wQo)1$hLTD%b8PnX_@^z=PxwF=>+g{u0P7p)rK1_9+'
        b'I-QNst?;zm7RAs{)xle8I(L;89cpRlbbbl559kVWiJi`^l+isOmB~B916mGuI_qHg5jq!|F$yupFx7rLgW`7%d-&BesLb4GN7`I?'
        b'SZO{YDpZsOj$*DkLp=9+t3Kju6+<C2bn)uhBYOAF_Ra;H$*Z$p7bm~mQSEy~JSy3kdwaA0nrorAL`TF9duCy_(Rlj_e{1$(|H4*f'
        b'D}x5oFjuLN?PW$OZqDY|%H&aj)c+M<(N#M49)ux7t9FhTUh<O~Cx}z;P~NsJ_HwVQG|;@M(|hK_^AfYvoY{GQ?`?jku#@86elNIF'
        b'yy(#~|E2T6{O_mA!7Z<KI$!Io`Fp4R=}y%{V)Lt=LX}q2QNXHBXMShRs?Jn;UBmsmCRZ}^eilEtU-`MtiAured2Fct$<8&mD^@a!'
        b'Ii13`><HnZ5_aAJiDFWxP**+N)5o;rbUGJz)-3L{Ki*jpDmEU!<?%7paElA_QIO=Rok9;qEBs2K+ONzZo@+Pe3keZND23f|6?T5M'
        b'x-<C*t&3_&?18^<thaV01Wrs5_9mtsb&U_4k&vwEgdW-%VSmY|QB*XvM|HaY&UhV635+*%>JzBBCW_2^>PE3}`%|_|;A0<wnVYR^'
        b'{t#}*Xms=0ejWp>E>Bk)v-1EQ*p^AwckwG5rF6KG&Xj&yG~Lk{S@9&=i_X$Udh?n8&chN<tLoYtSX^Z?bF|W}_)KoAG*wJvJWmj~'
        b'$^v(76DnwFqxB?ei%%z5p|PEhA1)+b<Vm~;!ue_84)fnT=!LmYGY^VI)EOt-7m~&*26dKidypqe;a-wN*51>hT233_`$irIhMap-'
        b'nnYlQD6f65W=^}HNt*?)*1hjMR_&Yjee49)e`;6$m$f>!_G_K{1?E3>)ohKsqw-ATEc1`Fv)?!4|A!|P&oNoQh_YS~n;SZWBMhsh'
        b'=0hE>*udA6u;=<daHEnNy4k;V%8pnvzceH_j7=RwTADkY%^fwTI_&RtsD2Z<HU!q}>v+vd-@n*IJ(hCP4H4NJcKMpCY4`A|v{FN-'
        b'w>IpOIMj?Ihp7zuy|m-<MAtv%MLUFk>a+02VnS)rR|fBih;xhy+7l}2tuoD<L3zD)3GJ&2gQ^1#F{($HItIeQD739ySimY}!<EK!'
        b'd}UB&IQ3p!87BB%H}SJ~cf*2ISQqnV`a2yo;ZrzPVEOgM_vY!|>2SW&QS)wxeR+qmTa^4_hp;#{k$KQa+-R$2g=V5oTKjdRJBsnN'
        b'(nmz@0t|mtvpjbW&Cc%du2)ZBsJ|OJoP`}V8$0atI^6A|2fkf=;M<yO@UJ40(QCHe^RnU}e6_@#%6Mec<XIiw`Qv!nXK0ip^kq)1'
        b'(P^5$Ysv3$=6BTmt;0U4!~MM|<7i~H#5jU+L<N}}S`~9UHiWZ{qrB5Vf+SHSy!oO;-265@h3+MsQB3WqJSv#&siXDDkwaXg1FMvF'
        b'9nGpEk}8Kgh<fPBKyJ8AS<gx23kuTZ`OPKf*p7`GO`{4zuSp)<M7yso^XNuTOQvp!eRQg~T0{lLKi)AqfeR8U92#XE<HOPsj#0;W'
        b'rr7A6FCKTPKkzgX4pitP62<Ti$Wxxx367l~ezfkW>J{E2+nZxNqDLWX_VcQO?zPp=(3ba+4(B5sHIH=I``g{eM9uHFJlx?N(@`_7'
        b'qwyA>+~4lWSXCsWxJBDNhtk_EDE{6?8QCIuDZDi{ue|Qxs=nt6a*^^3qcP0mf>H-Vt{W$f@za>uj=G`3V=Goky|tc;G>zRFnnCKv'
        b'%0K&j=>F05J8MI2W%c{ZOeKp6%9viW1MZ<WR?$0t?(d^`z$v}$yR6*s`?B_b_g%Bw1U6EtiMgu%-`<1&vfcX_%V4HiQ$cUX6CO?E'
        b'j0)!7UEq=Hv<C;bTxoY+X}5pWUi-n-idxa^8tM)rO8}gy{)97wGGy9Tc6~hAGNDa7p7n|ME;G7P0%uJ32x;Qj&}j~3khckOv~v+)'
        b'ikSs^eSY&2TW)>U%!2YI4;;}xHq8%0kBwP+V2H;NCtey(`971+Yp^IomX<P!4c3*KoRA%PB(gM4SD(1jH6d_WLiW~nWWP0MS%S87'
        b'^d=34*jI^pd%L<p=)PkQi3K^x<p`8lnZP>`0c;<b+?PmEzIS-N1TvK|5V`&TBqAhs2iw@i|1XJy{(1iYjXxK%G=WY1jz`KHPw}4n'
        b'rIaVLnkOpcZR&gbC@uvnvlq2{-U@PGC(Ro7MdYc#LWZ2sjGSTBK1Qjxo>#LRdntHG>@K$A0<Sq5LTyb{M|scwHXG=;)x|4E2R+~e'
        b'#hiA}_4q;MO%E#I{B~}Xw<6KI>x4V<%~9?5WE#7UM#z1ItoTK=0-{!Zt4r(c%`-*w48(n&7JGw~wm9dAu9n^_*bwRdftV+@>!cA0'
        b'iBc|@lddQzcwOqs3!EPmV&31HRZ5+gj3TkaB_+zBRb@H$k?lvss&B~_IgO&u&m+P3#aFa0n<B_AoG5l1L{JsO*hAV?H%V?Voo-b{'
        b'(#!9S5ApFM+CAdK{1R>G6p_1^zp}8!(C(blZWp!JR_t<b5WN&Ytr%j7;TV-a4NHk}D1FJ-D?g`t*WW@}k?L2TUSgQg?i}B4|D&z;'
        b'gAwimQG9=!Fim4@_qLGoTDdBg-Wl|pSHqn=aPJQOpZMI-gIiSX&Y1R^n09-2n|rM&{!*KFy6K#^e@VXCCfsBu>=+LaR_*?+zfBRu'
        b'ts;lgMz<fhFVjJAa%-DMl3RB-xvMQz<z0n!sR9=&1+UZ^wT5Q@mt<3pu={BC`L;^R?^em4I?C^RC9Z{mRdemlZLYb2M|>7mxj!Q)'
        b'0#6gc4J}3^<YO`xWSR1tt=V6+Eh{U2qhQ}TZ!pHd+4|OHG@_Z3yoSu<^CyHnFllL9HkYICkUb~yYQ7P;Q0U<4cq3CfZ|L=+Al2Qw'
        b'vm4t4nKAo#+m)aP6(v<jZs@gMPi8_$bdMcqtmld1tv2(!ZNe~DI1VxG(4dwxZO(7oYFgUXS9&&Y3j(fMDvz$GAClOE!V-cCg0@a@'
        b'6ObZg=X9xYCjXy7=80{dz2IWOrN@U+lJ(zH!S9cIXH-_T36rjz#CRASM(+iyZ19MT@dM|n)VP&;<(JpEbRz4cBAF|9yuo-gVQ%2U'
        b'r#u;UJaT*1-1-G8UG(KG)9mH6&&W~wq+3lJc1#zFYxljT8kv?Lh|9X8i4BUpHlf;Tg#t`uUGE3R2@O`(r*d0`sp4(I4F&f#5@AV<'
        b'JP7xJ7gVVEPp_?_9A${Qi3^UMz&tK_M$~xqURsmdyz)aenO94|eRTS^o^qeJM=J=7|MI-x3F=#H@ZgpeZO)h4YF=uytJ{pTMV6?c'
        b'&2=q*ZF4SftNCjio#L@H@g-55GAhKfcxdeKee+6hDUZ?zG`15*R7hm0&01gh^4_EIj|j;WdHGc2niz;GW_#bHP_((|i^3+=X2J!n'
        b'Z}ZF<B?o!qsd}G;UXx}hhc^GKWp<l0qpc>R&F<6YP7|STC~Yt$yqr69g?9K0-t<=nn%_EKWffR5c6&feTAOofTTNP9>NP%dWn#k)'
        b'<NYqAFmRVOo~5OfnKRM4Vf&a(8R!l+60^ANeitI}SsuCHhopZ(V_adO+oP)QpHGkfvDMqZmJ;t{XMYvgrc^j4QJ(W)_)#hhKT1Xq'
        b'jVLQwHuQnMRoI-MmKrO)YucfZ7bDu75p6Y*ZT6F`?nF`csa86Jsw(jo_3XLlX=%S9xDy1qIRoqiF7W7cVUS9M3CcO;<2_YRe^72b'
        b'f7d%d-A8@26JhzTi2S!}kFVt=p+`mkX{3{SU)G)TKnxNdK9q1`&380F!<0F6y7p}$lm6RrfT8g>FF#VbxTn?G(^}(hwHLP<$B2p!'
        b'v|Ma;x>{?xTj?5fe6crkk?R>}m=c?CW2Iyc?O~=0zsfl#Q@$`-FUgq`6UH{8hSnBUw0zg<{I<2`yVlg7_y;1=*4AAf=9u?}uTbF6'
        b'6SK9o(o^7j1esy4)Ki7+e{V&UQRJp7lW{S`!60wpzR*gA8ct$*x**+@KhH|&hPF)wp_l(nroVbFv*G?M+5EcbqG&E?6y0&M5jo<?'
        b'e1uX(8_?Q@Nc-YedN;3k(kJ|fx(0XC-TUp6!4{@HIH+Y^tJB_Ux3@0(!W|}>J)_k#wotu9D*lHrJ!u&oQpOerJ>jpdo2^+EqCGTI'
        b'{aWJ59XVcpf6c@1sWeIICE)jxF`J?>Y<ilQ(^}Jx3CW)(@Vf#0zB^Da@VlpmRy+miwBjH4`8|0|t1u#Zj=1OZD@TW920iY-YG`iW'
        b'$&6(oOLsoIa`e#9Vd(PIFE2Q{V<m|!Nmte@7yG)_2QITJVrT?bFCJ~(uyfR=m#ck^PZ6`aRd-Z~fL6%=L@AoUiB;b5yTep5lPvv2'
        b'>Sfpy2w3$B5$<&0*yO0z$Jqv_tkxOgaE2vjYqBNoVq(qa2H%|Blw32v)jq#<RA3?F>Xf^`y}MUDGbJ}@)V>+2K_oXkM!%RO|8`#3'
        b'Pf;jNmb7|K1m8X{w89m$5C#|IbD7Wezuq#f)j6%TW?HNL$MY&iB%H0C+A3T&ynw_{X*EQVE4#A|t@I7ZNo00%D`e(L#H?>^Np5{k'
        b'>P&9Up49rQI5L2%THs^6d}ptynsq<tk-w0`njA*?yjVLvOqY|MQqKix4+bbStuw!%dxGE%a((_mF&8xdK;O(S6k}Rbg}ZKA#<e=f'
        b'wc5wE*4kfE-DHKivWk9QA#YW)hvD#kri{u~B2x;GDMFSgTkT3@Ne5fVblaGUf8K?Qy=-%9%g9#e$X5Gs_%~AZhj+;d;f&qrW<;;E'
        b'^ksEUYMBw;9IU#@yMN;y4dRtKBr#{f%I7TZI8wCR!bWRs;yA0^Vu-$XFQG+FtG9ovGoaNjg3sHGzp^jgJkPO}zOmtoL}q$mq2kiw'
        b'aMc{XgUxD`$Bbr9v5r`JeYEQ5JHkyj9qcIyKHUL#=|x4ft^MV^+H=D}^S0!l&S#28i5G}Q^eUAigOaE<Gf|~g4->0J*u;uB#pZo$'
        b'&Dpqa!@)t7qQan2h9eTUnykOdciRY<;*|KvU@B)`=jXk4tEKzAv-`aL{Q27VPr18U&)jtKx98Pj&R3A(Rt*)YHLF=g<9S;26^R7d'
        b'7yrZg7yK<zWWz-I^pN{H6<Bi?6ZcHQ`6!N@Kjl-&9$}0TcSB#ht!63}JFW$)6{|DmtqO8~e%C5`-G9U9Y{fO+%DgJd&18L^CLiRn'
        b'>r+Usj!k`%e2~UAP9;0?ZX+EfHl|p}+ghcMHSm;ghxGG0a8Vl{`r4nXEeO=*OI9MeKeFpD@T+s0=)|YbYt2V|z@tC%^G4rj`S85+'
        b'BP4C%`VjQKoIe-2*+0E#>#9$gQ~vc$vd~2m*wjNtqcY}9hkLju_r})cboid~`TVnLR`oA_-wbYW$KX@GM+PJ83w-;+mhI=AJI~iT'
        b'V(gpFSA5H^xs+v<A(D9(Vb65xKY7ypFZ0^-R`26?VZ}`avsazZ`mEleBF5==Y2GK^ldm`37ETST1MA{lEKxH%&ivwYke}&L1(L=C'
        b'e2jJ6B`drBFwd3k3}aI(c|?yJUKi-el|wo0zqG76@BAB5__9wsZ8(t|Yc88s$yOSo8_R`N$RFe@zLKx_!i0o2@r^rqYGv4u=TVgZ'
        b'VtuwfSgU&WywiBzKL32}?uU&HZ2XM#-VP|7REyLr!Cv0FvB^>xwC2x3O`(C4mMOjW0nv3RX`$i%-8Dg_>cZf%s8V&}@I>{fDgQo!'
        b'd(Td(Xp<$^Z-muQ8desZII1uzG3>uBZuYMXtMmWtP=Bg-Uw36tsnTjF8@+dUWmxPkrYwx}D>De4c7XE1{TCitLcW+7v+q<ayYrxX'
        b'T60cLh+$xcn8+DP(jQlOz89z;Nyz4rlBBdKV(1Gbdihzcp6E%|*bh%kuFN?xSqHmh&xy&!P#6EK)wlns)i2kan7jly2lT<7e1TS9'
        b'4$ygp5YTnNv0*xWbo`0QgviLi7-Hc0E*^h(7Q;Us{NjH@_>Y{J++)$|FN2o;s?}#+fgin0)^|_j$auo@%VBRDa2Rn~(W%vMgWDBz'
        b'w0ip91kX>V8$bB^xmx`d#A7$?9jiDo`7+XQP=OT42x-dH>UD@qewJ3h`YEkGat@87Nl#2PD#S$p@oTA?Ut0?IvIN98I)6G{c(>s@'
        b'Nkik`%O^oU1b*c!iT+*0VGr;T@GWo!*gp#SI$dmtL|j%+CWeDRlAah&19=Y<!y+{?6fH#hkPnLxkL6Iipm%H>F~q&E)n{qMhPYR?'
        b'`XuPh0&XInO~7toEWV>L!o8v*25~eoAa0Ba;a!d)h7{0q$h#|(h(U%h8GlJq2rEglBJRFx2)T)LnxH09LRN!@ARQ~{H*!IbFjvFB'
        b'eehom{j(ox_01n?^=Uyw-?;e1<aHuR(i@-$VgEAXn+1Pg0HUF%1I7a>z^l+p0zC{r;y}j&wv$?YQ83Z#+rSq~wEBJUV?VGNc4xug'
        b'wMo50CJ*$Aw&1%AxCYb$dbs@pv<cV`oB`T^%RoP%hWTAkaRkCdJnImzIMC+jz;6h@4q=RaTB{$>62rPgVptBy8^K>R&dBHO2wOb<'
        b'#N>j`h$-~--Z=1^{LvGWIiMGI2A0zDCRxbhEaGCb?y12m<O<Bm!W@<yJSHaN;u)|7{)XUxFJBIS<HV9Ap1;eB^G-~j^Nd!{^UO^`'
        b'me62G7|aL-4GZSmQc=#JX#oEv&qw0BcN)qQ-<Q+CJ886>O<!igO)<3(6aksQ>FKDa!1x)&(EdE?-d>~`{;r1IsxKu;VaShs<o$Mh'
        b'?}mLF@D8v9_L80;hBW}m*6K|&iJ=blq8#W0FJ#_AxXVz#p}qoK-pd#&4>5-QfbAK^a2fW;0`l=<Ll4YD7HjpVU(o8KpV#Vbn;AnG'
        b'%$g9!6~rqE>SMsV-@sp0h~GZMJx8n8qny+aF^1iU!#2dh^*qh**HSKk^0dO^Cr2(x>Isr0wIlu^66Bc<c@H&X<M}wGvz>+k`@KMP'
        b'uq3H;9x+q`S@TgRKo7o%ItlleVa~z42klT@CBhNQ^i40Iy@C5<pzC0k2fPTZ!8d<{_cl?#@f`9nayfV$sDFXR(KOi>AW2#WwRkex'
        b'N~9?SIE?Qri&6LCX9(KCUeMg!+{tU<=UJ3NZf@z6goLlr8WWNRznEUiN%d>dG8w=Ygh8B6H8(dOgnfL0S5Q$2-Pr&Kgi0eqlS&oh'
        b'{nQS>b{hZNUH&rs68(<4y`z-u6Wo#~(X=A&5SV1J&M<_(I=~Z#CH!4sS#@$2+z=T<Rv?_+h<6e2)}@<BF1^9UG-*7(hke#k=l{d|'
        b'kG&XFFtHN;?gqZ)2YCL-kGu`)B}jAIkQ4gV)Gu-nb!hxiV9K#!lBAo0o?gEOcJyJ$bDF=%k1X&>vyg|rDM<U594!kXPhPi|QVG#H'
        b'!OKU`J_5_B`Z&sQD9RshE(2lkTm4t$E!0UUe;sfIYAN)OXnh_9J_#F_GUv9!Pyb=n=t;ZLMz2HrKM+myVZc}wp?UoHi$S8t9=-J@'
        b'^2(-fK-g#Y(eOoN4cdig;r}y0I&c>LmX(za_x~Y^+D#q{y%eCPU6N#jSuxbBfh=G@phtZ6fwun&J_Ox%1?~PX#9;lI7^I+epo>7!'
        b'Rq<u7?D$77?2s_jQ`7_Li%1K;HyIR<|HiMK41D=$!^$UT-9#N)d1CSuAQ5&Hupa|l-N5sC6Hqr%clIGJ4)oh<=syL_--q~t?gF1q'
        b'i$q&We3B;l`y@U0kR)k2P|8V?W<dXFog|5U1-uA2V1F;#QUdj-;huJQAM`4r)}fy7hnm($>&KF$5^wwR8T5Vy)G+TG&KT+eYY5Rl'
        b'I$V<UFv5vO-FY195VVQIM4mc41>Zvv&Jzg#DX8f?dy7F=0s{y$65+i9^&!yLL7S1TLeTBNF2D|aO7(#zARP9#0uKRW04*>z+|y^Q'
        b'2HgM@0Xu+q0p%1)(g&a)0=MfWNuPk$0WrWMz~?{%&;)z~oC1CTdVuY(NRoa6eeFp}(j27i8q^HZA_WcyGloH+!+>yLED!>yfysV8'
        b'Ngtpr_M;4v@I4T~7+gRYu-~6C9FsDJgTT$dq2B@efSIs28^{E5fMq~&5MwAse*A{KO$Xnugx+c(AL_NBZvdNt5}*{|W+J`F=eMDL'
        b'4|pH=5U2s_Xq<t1;5cv+_!c+|oCi9A-yqLi0KG&3p6LX>2Y$gfZ3Aihw+Z~vOZ~_9b<kS?4~P-2A20+60m6VtKn|#YtMI2E7!CEq'
        b'fCkV4NkB4?3QPxP0iocXCqXlSUx2y5B49D_9Pn4*Z@^CVql^i3Jx~O^1H2FH0}cXpz+s>sI0iHUr+~A-dEf%z27U&91NvwhMo5x^'
        b'0V#NYosUnF0_xwvTaSS1fQi5);7K40$OBdbYXK{;6G%b*=mgCKT@G-A8ABAxPy<W?rXYQzfEiF{037Pz|A0zC^FW^m{tEcw`xVeN'
        b')E^FY4Kz*07`A~P1}cH#aK;c9$ru(v|8yW@7y#Ws{q$oDn?d&gp8^L*QW<5W=_u4E0Wtg*0WDB}53~XofI&|5pP;`2*ML6YPoNh('
        b'dIyxiA0NOU7y^U>k${r6N5I2EI5+qNP#y3%FoljW02?q1K+|i}v&1$V>iNJkKn{=#FjQzFO7c9^FH*ZCguD#83V0o`(Dnh?4qQQ;'
        b'E(1M)3+MpaffV3vAs&K&e^=-nA#CkKdXrwEZT||xr;rs=R-tb}9unGFLIf#=*=6+QX`p(T9RuZ$^87dO>wBOBxC2}QdV!n3cS0Pq'
        b'r!wG|6!ZsafIrj+ftUb7MuRqm>hxux3HW{#bS;n!buQ>^(B2ooPf%APyxqWQ$SsE<Lnt^R$VAzI80{>fvPq^S>72LCUNoOEl&3O='
        b'$VVZ!&0!4Dph<{#3*ta_-WK(r7LnN7B64LeW0(bf*H$rE@;qZmgL(x`-*Uz<@{M0+r$e0&tOn9oBYaQ-n(_i;P*kA~A+PFyte+vJ'
        b'U~F}&dDf(2xRs(mg1qpU>m|mp2KMIw2Z4RS5*_5FO=$0^KNttdVAl#6Q}za92wBS*)EgK>9kmD4tpjfd6S5zAc>rV<LmKQ9nHU4z'
        b'BRlI=^v$r>3_n+_K$`-;)WB(cXTj_oWXmvoFNd1=6OvwpIspI9!fr9td9Zg7<Ji;iLkhhSfCiWWq-<pja@fg%`k)0e$3HM0HNjs{'
        b'DZl}Fz?#>QK2RAD0yMu)`N%eT($R+#Av@{FOYj#M4?G1R`^k$hdHUG*K#u^w06r@vNwL6GAP3k0d<dKdZUB)l!#(hKpbznO0kmIU'
        b'h3_7yN1)yC0V6aat|0{|L(p*00no#>jNve7Gf)rQ1WsG%I2(NoaF(VIc83FXP)C634j{i*X!W1qyXa%aummWAKPjL$X&EM-m^^DI'
        b'(gwTbzwrD~<ZBbuX~4D}XiuAqkPl5$>fQfHlO+oB@<iKK<SWeez&$ye5FbdhQqtbU7?PkLvIS`cjzK*Ohy=vP(N9vp;m>JM*<&bM'
        b'&_2*i$c{<PD63Q8H9-0;V=w`ifwa?%;VkU6Q@=_f8v*kX=Xn5uyC#@7!z}$@;63>LIn3LWPE1y>Lw*3~pl*WRSf~$!(z%8nH|iC>'
        b'duaGHzK>%pQ-<<|UL25x@A3G43P=I!nlRS<TB|>dF((<|*OGxDD*&)^?~}PO_kAC2AU@xOdK)ku>T1v#pkIOh1@s2!lc2G?(BFe*'
        b'g3bZm4Y~-l9`rTP4$w8A@o%Hg0i6l@Cg^g|ZJ--KcY(fEj&{p|_8;G00##7|C6JJFkd1FUXqm|L=O8b0q!;6o-nBGe5a-nxiO8eN'
        b'Ju;aIarzx@c~S4$rr*FT1CNlg<-)jQ_08MJBeYAUXsgHoJ%ulmr~f3>Upf5AdIa`N2xkK55zs}TCqYX=zX0-uI3Pmc=T3a@*NP26'
        b'X!FGHK=wdA&W1V$YBB81AA|w<T^jxny%hP%A&;Me*%Fw&3VIoCKLXu??<1fSk%)tcO9Rwbff4UYk{Y3x2Koo6>0O#8Vse6BgqsjQ'
        b'<U6n%(YXY@Z$Sg!gPZ_58x&z?JrDJc_h_8uGAZdDvK@R9hBQw=n|K`hlR>Y7&Hx=@gWLi-3-o_L{|=f9S_S$K&~r8+|7DyVJcRIH'
        b'A4<p|s8gUWf_ehzN1#)nr-J$l@*)(p9(w)II|JGSdJ*(n&<5m>6Z8*!9{`nwqL%~x0C)syD!a+RgUcWH@PFnTs4D<1OKO$^o}LBF'
        b'fnFZ$(6r@)=D|(mXx5Mp+Fl6zW|HLst%MmdiL#ncX!XkrwEFMi?#gDgIlx({J7DJ=ASYZ_7$Ao`{<k0bFt|YvpG649pS&*#8OIt1'
        b'#;}GJ-(akWFl3WXOnw-+4E45fqTh#bZoY|rc*tG8{VeU%Cu2~`5cM~ZC3Zs&sQ{0Gz61OKoQ?uNM-aUYZlgiZ{!^>(MR^avj}<82'
        b'I6r#n0?((sg|;0?*@||6(w%7cfmx`>cWHP43;n*ou!bc79gJUrdDxSzq15}mycBJ7sW5Lu!YYJ1LE6jEW&=IIkH8J!GW<LSd-cF!'
        b'q~{<I2K_b1J@cmj*I&dg^vOUR{Eh^D2v`L4V*FYJ`gfZ4Cs>22L#yYGX!TjZb?E6nfP4ugLGI8U#(43pR=@iT8kUsKYe^YlzJVip'
        b'<a06nkwFI0y^a3PBm}$e$L5t{8O<j@X;x^GiB3q!NPskJfKRvr-lxq&8lcz1&AHjEAq6xID0-STOh>r8flWXekp7ZZzYXK;)jPEM'
        b'Ik2;CyH<Y%7{7vKrR>z|i{I1gL$cVceDDOFfLTGrpzonA5ofJ6@w}LR4<S6s5|bn=wX=a&3wAyx{Mws*7}PT8j|X&6CkbZ0aGyu`'
        b'$v1hT7ZKTNIw!}!$I6BD{gbB*M98tZdr)tHw*VWk7m$L-Qjjlm14&rgBwDuhB0}!+=V2zR#P|S6FGf7x;`xJ%Sp)wE&o4r{^oAiM'
        b'6LissTKy8ZTk|%Z*AkH-82l4zNawBZiby2f&jJzwJ&>Xz`mlVhUW{BVFG4&K;#hoN0e`>cyP8NR(U~DGD-z&<Xj-3;UrXV(1t<fS'
        b'BRmtr`vU4cfC=CEK<_uSzVHJ>=zQf6R2yD|d}JsOh$@Bn_0p+IDkJyu#Kezu3G?Ay^$5Ql?seaSr;)FhXngmg4+HkW-ENpQBcJF+'
        b'h5SfDU43~Fdi5|nOnKrXly|LGpML;(0XJ_0ZvnIZrq#E@{6naxL#`ZDMdRn>OE)6CM|Apw03j#7<ax*n^4|C0H#rP{!(s0kVB6nl'
        b'IZm!W3qR(dZeM;ytM36Nn^{8)%pU_>Fl&dKIYJvl(vhv{vk;HSa`fTA0L=S<D*%UYF|edftG5FFA7ac0UXg*u0t84y-HL{tBw$6Q'
        b'R(~2Oh5mS;9M}w828XDl2-ynt8VS+o?bYh_z;3BdZ}rpZm-y=ReV``rhO1hum&c*?d+YX_y}@qlx9{C1YLw|%z@_K1+JP&;W#A^z'
        b'2k6TQNkRCsSY(Str#}XNGyefu1K}O}kdF1>zfNpOhn-pFbWH&AQUoDM$geBEAwB*&{chC3a^UnMkgb3W*t<;25$<2uhyD>b&3`jF'
        b'7PN0Rct_!rv;gWJ(Anj5T%gtKP+uX&>9fiy?|2tsY^X{pT74h<S_k{OQr0jQahvly(n;4f5H~ufRK7;5FM@gITCF}0h=V^{@LdIb'
        b'3LFF4Y1jZ$jj<&#KnHDL+VE=6oDZFQ=s|vr#rJAp4N!{ja=--jw?GQiX+XqBlB8uobTXH<A5;!{^&`*x)~x-KBoX}b1N6W~U^t)y'
        b'rUG+-#lS4|Ycx&y2f+7mBQ0YM$3f@dyAJ7GgzprSR$oc^Xfparn)kp%4|NJF1Ys9Z-e#@-Ca}bUyn}z2VV-eNl61D5HLQkSCcb-t'
        b'@()?VP0EWb%2%w@>j4um06p>!>J{v=kO6i>Z}}^<EoZYxF_XoQ9N<YY`qXrkLop#k>ghZ)FB&+8wA;~lqRdy!gdf%DN6;T^8>-VE'
        b'Xu{az1Y`%$kPw|-4gEf-pMoCwTIgdB_(LrRCIjnWCm()rC(#B1(Mq4B0r15D|2uf#+sXBbV#5m9`wjRQI1a2q*ul+^&47dOQ;qLr'
        b's1uIKzGx3bzYJbm2R~0kKdS=N0T~>q2a?{@>em1+sLPS=bD){1&x?RQsL#Ql%b-PllBCDK{UfOd-#76catgcy8Lc#u=mS7S01L<f'
        b'2`~uA4qMMe!rm*uRN(Gao*xeVvrfn%@PoV$nPnEr6ZA05ZvrkL4DCQl18ca_uGLFn#sR-zJXDpA_PT=h6a4K(2saPN2X@p#-u#y&'
        b'i3J7&2Z52mW?<GkXdmCz>R*96tz4^r7Bq#bcWL$Upmu;15fXwh&O`m?52)kcBTr9h^`<7FFH2rD9AN>gOSJko&q<O_07roH!0wTV'
        b'0|2fdyGzkVBCqusNEe_Vhw=u-hwJn!%FqwrfxHR*JYdc&k8Id^UXrA3l_bRj<B>L91(iWgOismjCNKjCdjff2NB`Xp{%AuV1Y`ko'
        b'fHYt=VEPEW_%Y8%qCE)%<Uld>PXjWzTl5s#6=1j|o-TeIB_?e>zt)#<R6a+K*%V6jnFx0g&EH;8);Z*TUkB<Aa1fBbh46uaVLJWU'
        b'H|g52Uar3gS+$QfSb@VpFL2HU3Oi$aSOY_Nen0FcL7fRe#8`V5kcR2>DHzA(cOpFq@Av`7mO`u5N_rvZ1rdD;^p{|)69Ov#3*tAM'
        b'AzP!Tmz>4-FF^CpbbbWw*H1`)mn10<NOM6C5O*W400+o`5I_a2cG0@_8^&Js;Ga0uY1ibXxw*OYiLJg1XzMO`=Io0gBh*2zZ3l{!'
        b's5`)TsF!0LX9LZLd0a8dnbsTR#{~FoLK>ox--%E!f%;|Oaj4UQl|UZ8dw=KoXQ6%x=tJ7pf$j#@T||3*@&AtZL72t4kq>T9{Pdt{'
        b'z;s}iSC8h)6HpI{r88?o$gw&qANSHd0e8{+P0pV3;^I9U&P+bgl(k8{v2pV4SKmtyPWf)~ic6BD3hLh_YCjrz5((4~pf>22Ag$?0'
        b'yA^aS(&jt$;fCe6{K@mc5ufK1pFDntUn_q;@%);`1<Bv9B-wuqUpjKkckUldW4>Pw`!r6U!tY3wH4P*2&5JrJmeE1F4B^pz3lF4k'
        b'8C{e_*`!ZF{7okC5nUhG{fIgM=q@8K0lMda?wwG1^Cu5_J>Y?}KY7+eiuzeYo>^p|Ye*)H(VBmeB(3e^c{;~O*C%`NExRH~>II~~'
        b'dh(b0BZs>DD$4$<M@FRWCtcUschxg4r)%Go(nV%r@syY*pS(8xB_YZfV1ceZH)J}UkNJ|WCALDn0(n69G0=4~=&z+tJ?m$GPNr*U'
        b'Kt0r7o>3&MU2~q*1Ni<4W<PyNggF9Pz3-xsgqRQPN%z*-<h?>1P+Luzpq&Ue2I_whI*BW+c@o-Qt)+1VnF&z2!Re77O!ZJdaRYk3'
        b'h(BG6{IIHO5?!-gQE_F$V^wvN2?a6DeCb#u`ToE&MCS=lPS;8ezdto;u4efp$@`loefC1zq+Mmhg>}d$b+1ge9ernl8g}ETeSE{s'
        b'l%y(M0!GnOvJ8$vMgRQr(Xf^AlL;{Ei}-}WKX-gG_rOM7cEE%$=vpG(_x}+q+*`^;a3|eQMss687Dm@RawD?H;goSAbHWY!=A2XZ'
        b'4Bd=&L{cp_J^@?R;)n!eX7o&D?&2Ta#cFf(4K8ToMowhX6vWYe`0<Jx6RT{Nf}$pRVM?jGc?P9#s<|L;h%@3wO~eg*<c(1b_iS&M'
        b'+#GS^-`<fMeq+mU`of7tEmH@T_%*4Orj6oaYn)syU-MJ3mA(TeJnBX5%5GStMU|z}*fMEpn6^wbJ#$2_HE;dB_tg~sH|)|I7G*q5'
        b'fpUm&x6Kk4OWf6Ri;Zv^n|iBfzoJ8KW@sFW!d?DEai^afRLOFaP7UIoHV^dECxWDftatyPMI5O~CPg~yO5dBYXKX~~lph(yg{z*6'
        b'D1XhukUFs?MQk;EeXKCWngf3=DIqFLgi<Uve9X*Ha$%fUp0;(I_fCdd8v`F^HdF_wj1lD<>sXF6u8mN#V#~+OMkP0#lgbOX(z_kk'
        b'+_V_zE84<28RLNPfT8eKaA>W6@;CkQ|LPZsAGJiuN&3(8!$xE*mY3L;SfU=9e~51T&#(=iA11Y*>d#pGko#CP^h+SlhUrP6J-|w&'
        b't-<0)GsI0YGCDm&yyjN=uC24{`^o8_oeljcZMINU_MI_zXy|B(`Jep_QS!oT<|F;JQ6n8uBMKd={%AwAX8E7`>Eilzfd-MfI7Mbk'
        b'ksGF{YlD2aDREzbf%ZSTmEOW)bcb-k^mdEfQZ}`d=PDXod7?9DMDnGJ19T4O-hO(Eu1iGXEBh0##qa4)bokuc-|w(Rns?K3DBl=a'
        b'B(Ig5-xLbPuWZ?7fBRegrT)#+3y~x5_*XtRZzEqwA8rxc>2e01ir?AKS!;IoSBo0#!{3p<QdoE<YMP~q|7--i{vmSmyY4~c3@iTO'
        b'-4|WDz>Ni`t%0VECQFWwg%xXTyf)0p4Vu{?6!6T5$NfY7CDs{rY@xxr?CS=LA;h>O!pau;7e;YE?JS+x^zwy&^q<SAWyST!Q#gOs'
        b'D$cyD-)0l<pU7-k-S1FaimPOCRdPq3B^6^S&Czpodo)?|hsGdAnQJ~~CQ=3w$#q-f<oWmB^w!uYdnPIp<K3&r?qxRBR5OWzT##{+'
        b'+7`7nKBM2hxZe_Gk<0T}lrT1{jP4v<Z1M8y>}UJAVL3x()HGNA(wzRBxw2EfoDVnL;!Em=6&kHeIsZacz$Vk)f|fb`mZ36zRp4o>'
        b'%mz>9%B(wcriu?eS~xfN?IFTGXJpRCB8yu5S>BK%;%Z45(~!-ez?uR}nTXt#U#WA~@8M!s&XsXtFB$ri229Gh5?>B}aMGQJnORa('
        b'VSS--=V7r~+uzKhMoqQ)9uXI+ti!4$g^ya7M&uUG^>`SmTlrOFQ{aXjUn;`-IbWrctTc*O1;wvais0Kyqt8kusSJ8mwK7P$_fdqm'
        b'I%D26V(emH_kVRRjTpR8=S1YrJ9F=BlX+zSf4nJRkL))`_W#@6reXbSZkvbq-#b4RKX9E3P)0>@x9HP+0Zz8Rh3T&jaF?m91@VFX'
        b'iXr`RRtM*AdV^jRus4Hlk~AFgudu6xGcTImB+mP=inkmb(FARV>I{nt-{F6XL4A*jD4L;Uh%!a|f3yvu8LYuZX7^v$oAOPif$74-'
        b'CM6$}V&NH+YLVd>eO5U)rTyM{$g|fitlSY5RT~vOEHAJ@DXRD^8fxemH%DX4qz-Cg>l?)GZPAUl@7>GMeH}@T@4Rk_BBrW(i|y8)'
        b'x?pn$)!ZxM!p&{hy?GS>!*wvBCW_GK&u<I&?8P5|D+{=D=j!1yyIeImE@BrKRt(;a%a8H*Il@*m?mxzOuCpN%7{+}y;)uV!={gsz'
        b'ijYSZaRD>!=2O&vE`Up+Su%ZgB9j=OnCyOAg)FbQ-coVBI-tU$LVxka^&>;NcS}2lR1Yz3g(>vwRGgR|Bt|y4i7Gec+U$z!oUgg|'
        b'`j(y7pOC!Z%N^iGtoTuW%^vNDPOY__2uS!W{0T?&H16<M;Zti*{&{Nf{!;}FOJ>BproFYh!JiZ#l2=PD*})~*A!o8>p1V=aAJF)%'
        b'sFG)WA-|>w>Q)2__n?MY6v40izYt(J)-z9ZiyQB7%3n1<w`ICLu_n=(*kZgI#eKSE>2+uE^_Jr64tsRuZ7wY96}dq*Eg-l1Sl_1)'
        b'4>BC<{Z*vDT;S5@hmL1#Q%wdjnKmW|!XHVq(=%VAGLH8IteUrHfE#2tT|Y9YVK=GZqvD^wZh!i^A!-CS)UY^8l^1P)?Rv$AXbnq}'
        b'U%jq5`cs^-Abu4%R}(d|n$1a}g{7E&y;`DFD#0pBF%cdGyS%^~PKxaGRhj-T!mBb18oTek$05(Z-|?8W*S9=+-J(vl8?T$Jk_|!h'
        b'VuQV-1aI~xdhVI1G@KHpP1J7F8T{qiC1V^7GV?;3Z3ZPcTRuN$nBw8<4bi@}%4ml&%J^oqN1<90J)*bbEKi?GNLF31jYcs=RTM>g'
        b'6vmurIJZPgXRR}($a2?xM}1ADzBc|&!?ds@@=wK(>l;SV$70mih*U3^ZxJ2{^<0&vlx>N-UaXV}1~rX0y?3&d1o>;;cg2;-Vt$Ho'
        b'z>h!7cl-84#nW1QllbdRrY$8W>bY<*waFwdp15_x)<M>w5(n8CHgQAZ$e5dHaOD0ZN=QG%llWoR<E%2lVNGK%k9w~S3ydG=)0Tc;'
        b'&6*>G_+H~l{N+APRG2x8e$)Cxd$stB(2F#O+|&Dsr*Cs=>>*>DA*IlFk$tF<X0}gKlqOlu1#6N=$GiH1+3D$`Tk*cvWn^Z0)U8*@'
        b'TzTMV6903YzDLBS>1yO;^lavOy6{#K(f>S~@6+phNJ^kbC$T1Zpik%2C&&_=+!9Wd7-&(Z#ze_u5|+jU%aG*4m$<156pa$Xg{1z%'
        b'o6J;WZsRT9WD#4keGS=c=}WV(^c9=LvdTbfO+-Sv&{c2}F1)y6t85ozztrdHf~pxyc7VGxx-zgs!i}wUj;)xW%ANA&h+b0x_49AE'
        b'<C|b6*=>DswtP*pEW?MW{?0nGDffj=^)=WSy&-O;jbt3>U2g=YTTQ2RfuRnzgpuu=o)$VWrE-ZXU7r?O>mU<T(n4%Du<U2sk}>Sn'
        b'&yeYN78L9AOJeAqT5)Bj20v2ds9bPjwyh#XHAUYv+xEG<exKZ35>*;HvCsjTLR|4q)VxRkq`YHb7<yYJG46~Kgh<H6$&NnM&d?=;'
        b'eHSa^_xEuT4)onsQ5Ca7+)H_5Mu<lEBneU4U953MNcIbTHGBFh*RMRo5dT)a?Uwn&KHA2<--iN9555I<Ne{n80!QoZx7<sU(*17{'
        b'+t2au^a;mjx_FK6V;R0l$-DaE=EiXa0SURH6%OBtnwU^70D=TKC3$<_N*kYX%;XR+SrtCBHaa}?Y1EXkHRm-=ZuAWt#|@7=QBWV3'
        b'f91P|rfc<y1y`QZd^~2N?$d;a_Q!>U{y{V$6KaDpsc06pf9uvGewvtPo#sAxZ8+wdwtdft-qMiVGPW^=*kA3dDlBiZoOhM4b`=Cp'
        b'w4SaEG*9WP-8Ztz>In1SUnO&7`dgQbUAEzKHuW(wcE%nZ+qjTenlAK1kwz>IvSGN?vKzl_?w>lri!BL#REj9G#8|koCV`PG!~N+a'
        b'g{B^`lBr5;JG^!Ohk*!Wzef&P;O`I<i;dr~i@u5AwnUu~6T7ajW<=kqLFet}$7$|*ydKfVJp|A9GCwIcmK~!0p7M{}2!{Os=z9CO'
        b'Ca$b;d@_@S5JsC2h`ebt69NITCPB+fZ3{soDs3T_h}Q1c1VOaz)>7(Am+of9HU^}-7^;HR-6R$TDiyG;FV!t#n_8FdW3{`rZd(CC'
        b'd674<twmve=T5Ng{+`eC&rR-~bI(2Z+;h)8=gysTNhy2o&V<xHxy|0c%^A{{{<FU8Am;j9cG<K2&+@wP6FWgRK4&yk+GWo<=J?L~'
        b'oTxiw_}9rO8r4Gl>tww3l<LGhSkEfe#!oK$YLGTb*n8+W?(lI5C%32Kra0*J#SgW(sg3J6Aa5QYV*?hXHe6_sgS<Dqi!Oz<pQ>Ub'
        b'q|cXL_(<N$--?obROpam2zvNeX#4*O-6U*#ms@i`%dV0-4gndc`qf{nGyiAxW+A$^g@?cND?Iyu!nX)b*ZlI|C}8x6$JDVg{m)}5'
        b'!6>0oV$|OmOEIIwfRe6ceToZIAQOwAQ@r}yW9a~OQ9m~3_NIeHe{0NZlNfAI=|{&5wru?fq&a+Q)}J3U=0BJ|JZ7{}=|hmxe5y_#'
        b'gjB<)G3hrUoz17p^iLt3k={R+^8@^uncfTOtn@RGMy6kf^pAY1Nbi9(gimGZ-H^)pG&ublq^0QxApJvnC!|~X^ttp7NS`;-Y&Li>'
        b'Ha7h#WS>s|9@1P*yuhpuOW!rNQkec9AT~_X`(SOL((}z&!3#5b+A(E$Fqvqu{a*iX=+9>TzaZU`ywqUZsQG_5Fx+!#%zR{|XF{QO'
        b'kJ*m=-J5|KF5*T)()s0B_Cgu?18OisVkBhd^pG_RWm)1is6a*vjp?DrbfqzUMrO{Jm19fNmn?^}9H}vfG%hF8*NpA_`xq%sD^Yb='
        b'<Qv{V6Ki{2CK=V*psLSoIVWQy@zK07dxeU92CobGDFS!=4s(XLOO}Lt1F;Rck>wY1<?Iry<x?4Z-dMKQyHIfQSX(5<)Q_!NVXu&#'
        b'sT*qrQF{h!36(y-#lAyE?m(iKD>Vx-=H;=K47rRHZQ7C2CJDLa=6;IO-C;iaTg<u4n^Da3V@<j8Rd<{Zc%Kq3d6Dc{QLTWLWv-Y&'
        b'F?VghH=X1nbJ=sM$U@^M+876J`X7#&KSqA=<<7CrKaVy4d5n}kA(;?u`b)uu4RZIU){f2cS4&(oq+~*Cjmot`x+RRP*)sz-Eyapv'
        b'S(I4WthVWx&0W3W`7M7~FR@9;_RYmXs&#vCUm8|D``abOLFBqU4|J@T?=9>oly7*h%_L+Cg^}%TPh#Hl0`^=~^Gjo%=f*To3p_83'
        b'HE$d<N-=W~27{6Y_E|KhSu3dRecYNfW_DwsdyQh@=C^QhGS(>W35R~ze5%4leR}Jd5%e-aF5ZQUvoJFugg?F~QOHgq=gUG{ZEaU3'
        b'Z#8m1RcM?uVGL%n)6f_=(HJ~|ty;l`N<G12yyqnqpMbenxObj&768uLkP9%YRyY?mo5sAK@;53iGKWf=a#iM4xOqAj`G)z^RqT`4'
        b'%C+Kmp<c{5F0SX!aJTru!^H<VGF;rst(bxP&T?C3w$ET+5V#9l5hvCbE2U@jV=i}7>t<E4MQWRdMQ++#So{RGUg9{;8DsFBbH>ur'
        b'7B(%Ed&MD@3so-n<et5h=k~3pU2=Dg{ma;~!N4zsV8KV!>@3(3QN6PwwK1?j!nwpDo5OMOajv=VR#T7s%UNR`1NO8}RAAeX5k1Zb'
        b'<%XL^g~X*415V>|iLVjeJNaek*qPw5L89qhRjnh!l6uojsDP)7cj@%9F*5SY>0@W4@EH8C*CU`ELNh#B`zF|W7?=xm+mFamp0~~K'
        b'a2SZN#fnZ3J|_N=o7&&O$3QIwts-|nfs^=(hgZc!1lWYw0?`WPQ>5fs3HdkjU2-NleN*}T__b|f%+`Kk&6<*RkI%FJfz5t~weRq{'
        b'KD$u<#tYLnrwCq{9^~A+ue|WJX`iJCUYq`A;D!~Ebo;K-t~~}(4S~Kg{muP$<Oa>haZgAQ37xlqgyzm$gVOKt2_k_+0SkVJ1HTV<'
        b'Yq#D1Zm#*tt^GuTbW{0*VCC9hPcPrWN-&tEkc*`4_IXoz!R#6mr!&&{Z-({%yhR4H1lFFXSxmRbqnlLF_oa$BOFX)!2*uDH=ceug'
        b'Lxg;c2pM@@zCD6Ku%wjSUpjf{Eg=~UuAvLZ*v~K6n@WzIp4RgD-<q0A-kkp9b2$5XeG4vd{o_JqYsqKek^JLtt*s^dr~mjo?)pdl'
        b'Y<hR*-QD4LTb=TTqi73a85Y^#>*v6xO(0JT8i|5CT>Gl2i?&<NpwO!YL!9#bBnzgtR)xAd!*E7bURB=g3dCB1ut;Z9jjpn?q>@(o'
        b'y^(EpRf*&N_w~$Mr~}N-TTY2mi{1C*DcrjAmR7vaOp&*|F(`0$%bAVLE(H3lG$w*~4zPrOc%g77Dttm(aV7HAgnu*!FmIx~r5rQR'
        b'de0wk`5wcVKixvHA|x1iv&xqz^{?G>QS<mv58G?LAp;}JT??@<x7<3j^_FWXHX-Rcv$4g!5m~({n)he7xW9_{2%0Il%&}C8vV1&!'
        b'<1H^WzgoCw@BS9|<u61hn;RtsH#lYg9k1YW!M?|ptL~f*XcTA$IpxWpJcYMP@1lTqYK*x(iu$=4(NYYa=*E(LoBc%WTEoZ5V5xaY'
        b')w#*S$ix((C+`+>1Hqq4(yzFco_otlRD;=`;<6?)7Sz8yqFxB?nLibn^D)MZid<AOQ0Q8VvH5)8({3rh9tKm;bcDmm0DqWJ6!)i}'
        b'V;0|HwU{yw$<Hr$6!i3RjPZY!TgA<f-69ttL3;`{qKufvJc<5P@RHe_d}~1kSQYybtxpKdXOfQ#!Cf-(pywx+EnK{7aKV3|MC&gJ'
        b'P%UjWe=<oPT=DQrK?}W}{>YXugb@wQo2WkR>5rgWyzfKtQsc>H5|3!07h*lFoN}p<rW&K(kDVv;MBT#hG<Vw0(($wg9hlMk8jNjS'
        b'AI=Lkw(X1BwRpZLC-m0he+3wi{BbG$qiq_aLG8AWYeGYmS8iu@(HR&D1&U$JEc75Iq6f_+qx;Eb$t`0BKc8lx2kup>oBf*4xH;1H'
        b'R5DonDVM%s)FZfMi`I9DF;CCv)Srn_Bm5C!<_t`HifbMpg`NiZ#WAOQ)Uq^?`3`lAx;ARGVbpDuY96G$-memZA{u&*MQhSg=CmlH'
        b'L35hZKu05f?)>NInf}ohxBEL02vNms;77zq@b5Tq;inc)zZc~J{v=14Mm?RQHX2a^X`={H^!=zA3Pc$25dK6oz+cZ-qcn{^ScVRY'
        b'+tGbWB24-Et>&*r+uRZ$_?uCFzDTSej-ucSVhmPF%j+Wr$2evDh_!jNvtjhi`O)u0KvN?MoUuh*%g)}>0w(m|fj`RrLC@jQ(!0!p'
        b'QU4vrMdHo7A2f@weY+UXC>fIT4v#ex17oKE%Q-r_M5HpRJnm6uE~=os-A9FtdX7$!NaBv&TyxVXSqg+5<q7M*k^UDRg%A;@ynUT{'
        b'50!hZt(Mg5)<dJ2V$1tI>CVwV(0pVfPyx8n+Q#hQB~q#!zZO{zWfInUhH>yMUg;tw>_RN^Rdy)`>f%LI2wZ+b3Nsn+sR2#a!IX`9'
        b'sYa({JD6F2;(}iHdj0}_k*}0XTO+jm`};HHqc9Q^0fRUiq}rEew@_z5FZVQZO6hlIPk&l^`YH<D(SpM3)`A}R&(dPsVyscL`o=mw'
        b'1bFlMQF1|phk2DJ==?Y7t4C413T9vgNz2oyyEKmc=Y4EW&Zv!Q;{*7t3&q6=nAJ9#CyvZrDF*oO5xlbPUrY`{l%6%p<c}5!bC!%o'
        b'7Ooc-N$N$-)=@Oc3dsc#4eKS$?-1B)QcG$8l)|*rp?u-00-LA5#rsu6AsKbD+3O<;_Hz4PwS9@(#9uXv3!ZwsqG8QJ6_bL1i!(6m'
        b'($QpbP-2QWSqQ1na_Nf{k>lPZw!sXeZvM0*JG*4XG2Ef&A`2bpZd;maHGPGY545tzYG=h@ctvlnmcO)n1kkp`>I+(xU`3nyxTz*Q'
        b')MjY_x!VS1-RL@ndi?%<SviW)bj4_~2D3$j8;PM;5oMw>VZkZo9O+ikdf_keKLSVffxwA8f&>XK6P6J@@8EN!>-k6wC^m&^^vtah'
        b'Qj!q3sZ8!YCu?X#F&m}W`MQ>+uw0R3i+iotEo7p2l|4MNGjz0G!n`%&)uz=4?o^C=wF$1Gw4L1}kdr|!%vF@Ia}4FCLoVD^6t;5+'
        b'<$^|CMd4F>y0v#W|9-S&)T;(PDqt)lsy5X{?TciP2E9u|8a2*OpZ=*44>w{|CxdRuxi|8H)T@Ds0JFoOPHq%~PUpAB&J>S;4W_Yc'
        b'-Ah%Lh{@B^i|QBaL|@>wF99}pbd_%m*-K}J0E$D`O}wCG`bOOGDsRy*@8^0)Xh~SbEn4#YVWUgZO1rVxnh4sBkGSOVH5cOKm2@i~'
        b'7M2WSjbR3xf{!?Ihu`lZ#bA7e&Jm|+(A@>=LS8yeBvg1miDDv<P)1dp7BBNKndrZP5Uv!g)U(mSx?G)p-pKI~ozrWGR@fcsIwz|?'
        b'H&Pc31z!m4?7vv6$ZQqXCP$wM8~HK}AnT$F9*jO7(iRQ>Cd6IuVBZOQ=0@}7xzRkYjJT?OZKf;fEwrV;977HM!^qF3F!aAVIK}0}'
        b'p(}g&0A(oPP2HAe=tp2v1Byvqk3vk=6!~Ko@^N+ZnrhI48WcS^C6kX*pm&ex{C7J0qZXjI0#kWr?+AYx9dmaW?SBW~kFVgW#<js0'
        b'SZEPN6)NMSOHlF=l^?f+{3Y%qFs}n~+fzO=!pb{p<jvbh;+=c<x&lRfa8g&M0LtUFi2B)6<A&<+sI_vY6ri<XsyJbV%Ow$&UUApR'
        b'T$xjM(=eMx?uSWohN)Dy?e^Q-4FPu0l&ae^N9c<}^m6TCD@MIA!iVkFZc(XrwYyNDB5h>lTl4nC@r9_PNb_q2@Hmp5!u|h#i@Orx'
        b'rVnuO+U+L<LE6fxCeZts+>ugb^Egp-?c-8A54k;ZdU-i535qPU+fl&VvIu~+V)|tx(6wr!j*k$w_5S@lEQQ(ayS7Kn(k~uiGDecZ'
        b'gY>2m#t46KCVhk-1~S5jV+=Fw)iNDY%+hf8m;0h4=^)k%Hb6Ye*Z$0*S04O5y1LsziRtr4;CFGAKTtoi%4>h({PAm;xg#ofiBt01'
        b'yQi7>k^Q(<QW03=zoU<d8lf|BX68t>gmrJU(=t-BJ$M$~HbSP7TCji-gUU(=>~3KbEpz)Nrp#Y>#m=O=Y1xQVZfE)TOJ%(5STROA'
        b'QYT>)BYZ6OS(R^v#(<Db8;ME58FD1eC0Ctj4SKu0rm3c_l12ePkFNql{fuNp<!rM@zu)?iO!X1McVZR)jKW92&rp3NYjq0jJNSms'
        b'13G>dAJ?59R;Pd(9|rqe<&>q>$SbS)>+JpGjX*cd^2dtp8is}2AQF-IjC|abgORi<QDs;pS_iph7&S1g|Ie@!uMRFFoV3<Zre?kw'
        b'u2IDCm%eBfrG1tBonds5Vya;4|F7WrpMP7Rb?&@8Oh)*N;+(ZltG$FUvZ2SQZWPuIa!!K$oQJCPGu6pwTu1%~DnteTS7GTl_mMc&'
        b'H<M{X7<ICuCF*=kZ~)yl8FfWfSJnCV;WHl(lhaz>K^F?vZi;pihQs_7L)AK3W^iwun(Ng(p<((DhM`#h{;<E8E(+s8_07Zg;S8Se'
        b'`?`bH5>utgv`A!dr$LThB%=N{jBf4hIS}HPqw--eJ?SDr&sC0g`(yJ`{~Yq{A7<(2(53eKhH3bNW1hE%3mAW${Ww!SOw|m7QxkX2'
        b'^0}DWGwj6$a{><?{T;PyxT8vL$P}igRO1&C<*7BvOT6!3?nD(GE=}3u4VTh+GWUDwWU#71N9`B}Gg_4>Q#Hul2UPW2wCm%v+HjyZ'
        b'5Q{6)#>Hi7YvS@Kb~vsYC3WZs1FS@a;Xip^9rj8^hmH<WuMJ-~fZEfgw$|Y&)LH`_Aq6D~&A=a>L8W>qT~(u_HiDS(O@WwIscN=p'
        b'rO;FaG$kdWsd#8=12pv<YHGtUEdKnOZyjcFp-Ut<O@RHk=lE0AikOt8eBk;E<#Nxe;fwEbb<)bpkn#rbnlIF#jn_5j<ZOiWf>YMY'
        b'Z?CoyXiHkwE{E*%rLF!K>#L*{^BVC2cQ|0DMFKJ;Hd#Ol(^U8G24#a~E?gK;6haw?`Osv*N~FnCiqJ%*(uOaT$@%MPdHtRu;lt7M'
        b'dZpxBFEwwN#s#rQWt3qUZD=Pu`Ef{IQZ;j=FnF9wfXAZPqodT^;S1a3y5v?T&$i?x`Qo4Mzq_-SP&67{8!mu#dEIeKN0HoKXlG^('
        b'UnrD=pXNHyv7yLm+8+3*{f&ibP8k{Ah^IMQ?e*KT<Em8gGK&jOe{{%v_(4N-2$&3BG1e1A8<f)QM47=NC5aRVtikZWe|3v}p}{0*'
        b'N|v)qsq65Al};H7lx2|`#F)8I(kRp%e(W^5O7<QFcnWaZQgY9CgCC!$pP2`TV&l*htG)xiS>^qgcmDTkJJW{%8I;>q&ElV@`li1*'
        b'ls+~D>@^UAY~gs)iMjgTAz-pWja54B=-kFOJLqi9I0rC1^AYQ}IrHr0LU)}Glb%mgjo*J){>@N&haZ<{3fDJ7FgD2qj84ZCDze}Q'
        b'gvvi;9segTGAwF*=gmPZI1O`p4rj#1qj#ibaWh9evLQ6dSGt`t&-5YC+fzz=rRfeA8;{n&vJ}S;9Oe=8aO)AA@HcSlO?>?4ocD&j'
        b'xUg7+E*iEr4Q)P|bpZwPYuzI5;P-p;Tm<HB5blZ4dc&l}?{Y9(Ha5uC)X0k^WaVC!D^J=O0Dd|dMh3Z$Z-f80Ipyn9*WdKK9-b)%'
        b'^_(drgOlb7NPOxQD!*=34#B$0N<_M*lI<-jFiTX<R;qFcTCK**%jhsEu;`EtYN|fc6%2F!dJN{G1q?d`u86A$bEyT)wxMRnP>qBs'
        b'9g3=;GX*q(H45lV5wm{~*+7DVcf$R)fh$-Br0+|C&QgCE;=>5m@w2DgP$Zrc$m=hVZ041rZ;M?L!JebR{3KyE4#6yOO8oN#$lZSQ'
        b'C;#+do*(L%dXmrI4G4WI8X|-2b*eVEj(HEYzq0@eYR&`RH>Jm1Pw)KQkSh>SFXLnNUDzx4tQ@M7?ro@EdTf1?3)EAl(3K}66_tMt'
        b'Ilfd^qth=L0-ALn@yh9KP)^AkPD@g>$q^~Z1}T<Ol)TqaB$^Y%@6jQ?Ecy*!77jHEfGz1mWT2ldHF97Jl|EEM#p&UvOc0l@F^Btg'
        b'{bNHg3Qox{+bl3Lbld3E&KP=6KSXEl_w$i@Vvwa-lD7XPU8R-z%L;Z+XI>g416@T=@@M^+grU+~E(z8=d#IAu0Wvfs7!x;yh6Jyz'
        b'3Ur@Dn}$pbDri;%rHp!rKdJ#9ylNV6bEGE@dLA62qmc`)pEaaSJnSXK=I9V@VuuKGF5g1u8Q0V6jdg~0N!)TeT2YUVtJDcP0<e{d'
        b'mfQ)xUumk6Y<G#$ETCo%vcY>vd{2=S{?hakfSo$y#wZ6}+N{M}r&XK1+7}Lmi(Ex7)JDktwjYLMG?U1Y4Jx~Z=|2n_h5M9G3yqo('
        b'aDp<4ifB^2p0H^Y9b)WoHz_WL@&K%Qxifmp!u8SX7uL;d4_va`s8N&&>g7<QP7YS%#>I%imKhUX%^$!le5rTv1!-o$p||w<8-r*|'
        b'fk0adH-%&f9}g5uj~rAQq;zyRvj+(jzaN3t@C?wAnQEtEahR_@z!D-Xc4L_e<y&{zXlxC-wz-J~Vk8&<R6pTdSf)T!ZC$uE`hU~p'
        b'6abufgyZjtiQJA<LrD9IEdU9f;R}P%rr_3)%!Oifo=mB|Tb-%=W_)ptxO!ntrmvTKGZ4ibrK7{d|Mssp)VruFEx|(S<C{$<gvtQ{'
        b'^YKkj(;(>H7B_0HEm-Pl93+GMvt;H7<dvnIr+(1K-?h%XJ?N=LDA+LJo?hH@V30X{6a31yFe&31{PkQ_K>kdo{$_PBt9_{QZ$f*S'
        b'aC;5u**mx(0Wk0R4P3hW=Ce2rOAc5oI|fPI6_2Z0RIxRIMp$jov6cN2ZJcw-3Rkc;CCP>EztM)bo7?|W77rHu=|D^G#2ks~HdnTc'
        b'#GR|+;^LN&!4~bknpONePndh@FAlc3PoW!6g-p{;WE>R_wjD?YDjHGF+HkYYvj85WEsHu-LX`~a|8SEo45tgjD1Ze+t8f{$5ja8@'
        b'W>GH=HWGAUB=!5j;!8MP_#pMdAYC|<Pig9TNY#8AO+5!`D)Sb?NP2UgAB-cYb%W;ou$&Epbp8ue0sN23DT4nBIzNQUhiq(40c1mI'
        b'u!HhnH0LwauA4cw!MK;r`A>q8XFkHwizCb{0_lZ&QLOY{bP;Aj-gJ~|CaH%9*&~x?90S|To-1?bs?0`Yo%ZZTX~EmPrCKBRJT(|a'
        b'Lf3zf$YRy%oY=wAtz{xs&E_l_v@=3;zWPF*oCQISfK@mfo$p|cn0et}?e-G$5y7fFGBCTo%DeDwuba!6d-G5=?Yx#<tEx#yd!TON'
        b'NVy!GqSF6>t6ZIKZ%}!Sm<wP<ry`pX6;B7>JYS!VsCq1zrG!|6+J0Px2ulifrYqwyR*JFd0@fYG{}-@}PI*PAWz9TDcCcj?#)?j{'
        b'i%xq50;r03urk<f7j_&+1eczu^uHZ9V#@QgNpw|xPfl?4c`~eGW!)7r&|S8zqnZaiIdxLf2n=Ai_sVw42HC(SF#Dadozn){B~1WC'
        b'ySdmfxkofeyJ1#f^ulT;0Ld%^C2F--5=BO$*&cx?YYe8<Gf62rWu>-P7(GAU<PTg`li|p*Lx-tobvV0lpVExcp<iydO=kl_sc&vt'
        b'v>0{yCY>MN7Ambc?74vE5c4G(7h27-2e4R)k`4$Ym#I`CZEgWLX<lzR>hmLVHbxI1mR@XgaS*Fs0t*B4?M=2&zoK|1JwvkDHp8oq'
        b'1nuQMB!mgwbW-Q}*G=X!FNeIy%%AQO63&I%rz^I)LceTtS8rY~$Z9_w&?qcRXL<(!uC&i9-0MtttyNf7g}XFaE$+3IyG4~dwv{ck'
        b'oD5?%SuXcl`x_#A9GDbwPa__r1XuKLJj4%FYOpqfb+0WmctfRR@csa|tEv%QSmg>4vW=X*Mz#_Bh8kq$xSkfWq2KS^eA6Dg?M+^B'
        b'h6q(oIk;bTTE#TnL?urPX-QguZ3eB$cD>7~DB&7bPKP|;hoPT-0Cni~K(9NEar;^KFfiY%$#Q!{h*`4*JF9QfYNa<Y71)bT(ct{7'
        b'7z{+|tPn)-VV)}+Liy<=ZFb!Bl;1>k-wCDF(G|rTkEzg|ZfJDbfLjP_&r?dR*sC_6GELS`U2<jyYP)b;;&lrU#vef<*c&#5SNK=f'
        b'y`6U3-P)=~ocRIqmNDPdW>$D<wXFHy10M5DKS8xOrKeyCgsJV=&AF_?p4eazan0;tL~^;@MG0YERW``{b4r}U0f&8WgI;&9HT@Oz'
        b'oLBuSs0igM42^rd3T;^Lwcwq#+cE!o{m@Nn-c5sW-{DKi2FoRBve9ZBuvAT_h5IZ9IraE}0Y4F&FVg4SG}soAI5?VR{OLS&-}bjx'
        b'3~sE27FeDUH$9@tqm>_^7gTkc(}d<74#luNXa3T7^I76e>1pBxf}ByU{W@G%oq71Vnq~W?>$U4MTUTsrtpFML_CM|Q6{0e;^3r&{'
        b'LEO)MA%V4NjKdxc0899^<V~`A8Gn}z!an;n!OTTW^>uI<(48}5p#5co2#CbR7dSG&rU^+lz{*~2cB+dqwyL*g)FrkDrkD*=YbSAk'
        b'?OboLC?`y3Ide>iffj;wLQ1x%^D@fRWf@L0)R91)7{yc#WS<x<nhDbhZfei!ft&RG_gy(Z_N&rLyqZ}$-EG8Wcgf-iomn#z8D%0&'
        b'`H4VTCBTR))TM!D{3ea#==j%cG~%c6g1LbSQs&OUFYnIu=Lf*|v>YeEpRp__n5+HhYXR*{v`;6&_O(!#`@O-dm8s|$S@ZA!LKViN'
        b'B5LCis-A)0d^52HWmE<g2tZ7HP^~IxjugEiul?D-e|+X#f7`b>ONLo8g-lz2%Mp&fEbvO+agm|!9XinK_C8tV+qy6RJpdj<W#v5A'
        b'6PSyf(a|xl@*^EmsSPT-eV*Gruj>f``vl>A;{LhjGcEm|&j$c?8yN<Q+a(pWNWq6F@k)trNl?Tv$L*}F(j{|yWlb$I>f-@>4T^1x'
        b'eFV;gZ0D%~fU(C5&_^BUiw^%ij3)-X?!S{k<jiw{K@D#P#qJY0!(E@>so3yEko}8omeR@gFy_d>9LfFfG1`Vn{Kw4jored&HK_~K'
        b'hSv+?<aKe{lzK3v%Nc*XSg?5y4tRd-2Xb~E7&ug|Y(6lcqUR@6GzvOsIrC~i@GqXK#*w2j<^Mb~(ERoQ8JJWf^0&3u>xChA>d5j<'
        b'<uZG#(9WbQS7S|1;NR^>M<Q!{xBWiGUk03#cr6(E{&5E1qTR;q7$C!4nF7W+aHedaPSQeR@eME>kph<#Yg(q#)wEV-R;hMW*<S}%'
        b'3)w8puym?Ev$8)syTlgOz3(6!*0aHxbX;NGI?#w0InW(*rwNz=$WjLVWZgJ$C{*f=!P4GWr8e}8an)in=-68iE=?qZl^;x`rm%#-'
        b'Kwx&K9Q<_fAW6cmu5yfUC(oY$oF%c7Hr9kieuPe}BEG)#NPqT)65EXKeGc=Co(;LNAINi_8Tdk&_X>K20^*KZHM_ADGs)A!M&cWJ'
        b'?M?2o{8=fJGeC-Mnb^{{7x2$^FIt+YoF>R_DnVCh4|CbaZ$}=i9pZK_9xw(9+7}vQUrKuGvGj!lq{6Te(`O7M6Q^D#73_>|!xHS&'
        b'mhFZ_!xEt>5L4}Lt*o-Q1R@Kq&5C^^FX-nY3opyh2~5{HX5N4SEcUUxWQ6z%f4{rLV;Ja2mZzo~6j-c6&Yly1j6;Dg)ea>V^(1ng'
        b'%jqyo>Agowa55r>j{MOOXz||iF2Tj0b6AW)6=Oul`@BmC@uwUuAq?RJa`EFmXftjl;ro~`3>5uZxJ2YQdH=hk=>y65J%zr%k5zBf'
        b'uk7D`G(aEHuXE;?1t$ly2e_o;%0_}2=|ku2@ru1)5G`(wks=w?;!|IM_|LH*T;KGO^9=NhL5XRJs`NYkk%@UigY8A7hSdMm-{Lu*'
        b'(0;N-cR<B_j<7k2!sJ(-RbY;xrGAmw_WPWXezWamJ}t=^hV&Ia-9(Daw#{bSmOP?jSDug+VP^M?6=8HvZ@*WB_54njM-<M_)E=lq'
        b'tEHBxV5!bN@>MN5NA9`YPga2a_&sV+D<larL^W@UUS;*2w%{IensZy*x5CrY8bttN`i{f$URJ(wmw$3x2u~WPf&4i7IIQ`f{hs&x'
        b'nP${={tPtqx3%AZW6HCk>8<_ACCW=mGcMSdn{%Qc>Wavy3ymt!)1*Szpz|691{~j4rEfvch~$zsk1z5gGUC_gxB(~Nc|*VVz%c|s'
        b'PRpuj_~_T?gaH>RtAwQHQ4y(RaZylWQeNT(<omM+VlFhGdoJHbxFyb#tP1x>cBGi&OYdNcG|(uzWF1toC&~;)(WBy+P~4}&48g>y'
        b'1NuMrlb_mxi4~UF7i#6J8b%uA#|iHhya?KlN<e7DSj9LSOq5>7Leth1GWJ55%}fO47K+XpaN%J>zq+qY(Q|5_SJAEi!&Ki;wO{BK'
        b'8gU$&+Sd)!#)zfA)}Jh#ofxxxPKwYJfITaAv~z7np%@lYV=xX<W67TYMgXKmJ)tk|hdGvr2FtUtA1&){+^`laP?HY+lzj3#$^#Sn'
        b'_5I``>$CkUiM)5}#4uL-mXg9H1X<C-e~iTZKQ#2FAr75UF@MUL^D)b!3D2|r<m{eVWFBF8<sNurXe_h(SsGIw#|pYQFO4y|{lBhR'
        b'l)8_le@~hEV={3nyPsdDqIzSK19m>yPlm;Q6GXTDlXVL|q|pse_TTJFE$(+pDym&!SZuh^nd!L4`PDQ3EV-|`h)L_OsHcmvsmJ^M'
        b'pY2tfX>E3mS?rIsZ%ytmy~7qJmtKxD*=boLL6U{RQYx;GrUO8_&qYuHePrNq)0^UKd_3DQ4$7BIwYdeAeXzO;V<I0p92qnF_c4!T'
        b'vFGl2&vSGeXJIFmCou0j7=xkyX(mHvjwmGR?}9MFZ0z4>FVw)2T0&&1L9=#Tkze^%F%45o)G~bbCfP|vrh32Fant`mJq?3;I()WD'
        b'F8yx0zbXLuy17HSl?dW1(+J-OPe8v*I^g<TP+1wmem>o`bfDEKchT5CoDI&p;2KFaT_2`3)M(?93w{Wh;`a-<PM=QVWN16g)PQ`|'
        b'&O3d3-(W$Y^T==zL#)PANvq0t6M<O8`{l0_nOI~lQ~={Ft!X^leY+=6>G%DuANP9t`__D@(yUi{`ua|bYm1cDE4_`lE#`?|RwSEy'
        b'a*lLe#59|m(|n;^=fY`s?EO=5fTQ@V&eo=j$~rA>3}C)P!jyioj}#fB<tsvFvv{VF$b?leElo&<F0PI+(sEX<%?!z$XJ6O~!mwYG'
        b'wyVmWw=H|6D*b$)d7-f4d{h>g=*W9__5!jZLv<oKqten!O0u_C<q1oVfxh3EE3@aSRtonh1vLg69_S(hOE*_qblKU$3vbBtgugz='
        b'UB<wo;A+KhQ4}A!+VtNzf^E3OMM#Q|eC$W!{$EHWMaJrk|3dN}Xa8>`Mzh<#Du0zZiaaes<nKki*tgUvEcRd<ovJb+JP<dE7&GdY'
        b'jaHb|KvlM*l?=4+sbZtC;zn*`jeMiunO%#mP~v8r!i<M_i4aohegnbnu5t>kOkZ}5e9e8ZL!lC{F{Gs}tYG|sqKkQ#ensgNzO=bd'
        b'cOPS!aD`H^@}downhEJk)BCa=VCx7~;6g`Zze3<<qtu2cn27`)j|*likEpP(wMOt?q!|-z!O><#^nbNy=xw?WhOkMj!alP(+H84%'
        b'TGUI^b1RCE3%?+;$~*4cQ_SPN)kTNDac=SNgwB!fJ6k8+SI(3p7DYBN5xxA^YZV)ggSUnLYtd_SeQF=Gu&+g(9hKE6VJ2@tdEBZw'
        b'(y4u6ubX5@1iSA%^++FmQNXrEYhBf0aZ;@obV^*jR#Fqu-c~R1pVh1agmWZL+T!HuY16phUh@2WgKb+wE_rlhQ`rOhgg!zdte2#q'
        b'Pd-3VfYh?aY#9bqe!AC<6VMHwHbQ_=R3C^(@HjjqgE8%;`?`#7dsw9_p(6X5Bl^H`Y(wA+-hWn_b|AktMRHmSYdrIJRG9RBRI{QF'
        b'spXR>>plBvZ4x|31t0eQM&AbY@j7<ron8_LCzW*zH#ukO1${(d6c9N=%Yg#0-8acZZdwI@T%X^&{|#ysIrULe=MDenGkJWw%fKAD'
        b'aa`clW--@#$v|)@T$u?c&biL%obs}8Csh{b)R(2~=?^?DXvC3w`_Bhvj=0*!EA1seCI>O@8~mM<$$KvMdM@>{(vaBdfAP(D&xbLe'
        b'p=QLR+?4&C^N(I*o6y##QZ5%Vt{X0ofYmOum&x{oJzV<_1vtsOui)rjp9Z`4d~(M^Is8vsWN)Y?gt$UV$S^57>zu0)Vdz^e{>6>A'
        b'Ez1wLbkP(TX8K|3yiikbg)N58i(7=m=A9eXZ8yjzZJO-N{5SDOMcLwUa^@i37`UmNRuJmb(~*upeHQ!}B10Wi17>FX+Kv<Qlc$Jf'
        b'nBnZbxJAk>chSo5DjJE}eIelUGPWB{Rp15LG2!_ZEr}dEFY2%Btg53%o-G~UyGs#>5lgV0uipUdAac^`^;r2Oz<sEu(WS{oZ~an;'
        b'49s_fKih0np(8kN;l3CwXMQg&!Ysx>gGgXGE78B!i%j#LI*tyBCWO&+?gP|oy+nr2Ok*ovk+ej|dZS}Bd4YNO;#a2UEV$t%5?Vr6'
        b'qdgEgmxmuKnC|sr%rZnd+VQ9i$-{3HNW5+dV?t##E>zyaTZl}rTHe$oELbLQf3+oA3%P<6dAjySn_6};WK9d9gOZ+N`IP!6gMIh>'
        b'c3x4h|Ex!0Z<{*=ZG0_7TmV0&c8fep%FOwV?CR_xN-d_D;F#6Dx})GFWBg4x{`Uh5VeO$a6PO2XfcFfg;2Y2St=vD_TZdOfX#U7i'
        b'DZMRp^1(<cIjs#v0uX5a#4)pPc<F3bo60wBXJozi@wNy1-$y3XF#BRr@f<=tKDB?Y?FGxpV8bX)ui*%1uqEps>a8Pc?{W2n{=wc%'
        b'V&7YJMCMW^993IFIPP+W_*sk+<qWnQFP&q#GI@WVD_b!32ySQX(8Gdpj(<OsbM^+BfTF$nX}#&h4dvEpZJx{){!T>(LtLW1yl$hj'
        b'7H=YpO1$(7u;3O&*z&Wz>g@LNqLTaB<7>bD0~AG7Fk{#G<pU}N*wooH{X(3D3hXVy+jrZdA6$=90loCv2Mca-bm#-5lwKZ933}=L'
        b'xtd9tH(%aJXj(Wc)(cAtTJ-lk(7s9=O}>gYzC?SKZ361O>olFUr%Ta%=LUIFv+DuNc?lg28U|TYbaaT4#mu6;mQb`g+VhN(jwY36'
        b')DgczXWjPlZO0{bVJ8Ij^5fdN<P%iA{&ZlQN7qOc6Cp(ztTnKPVa}osICs_w>LqpZ`mj2xUR$THPln!AGtO0PeiHMS>#R0QnTNjP'
        b'Mdus4MvF5-)@L|A<uIBUc<JH|j8+fO>?J`fEsu{aKBr^VS=BSjaA#~y@Rp=9daJ?o702tJR*#)Igqn*Y&o`qr`2)mo%lO!7X%yKg'
        b'VBF}L=kyI&nFY*y{Ik?szH|JUs5V-hO^mlB$Spgt+V42p9a4#bPcWT5a@F(X4dg1Ar?U|c==a>%`So=oLywk5vkaXYh<KpuJ?x@K'
        b'(BYI_aDpC?fqW50kQN~TfEh?92wbZk;P+Hv@c<tu2m_skmXBwyqsR^X`mqTM(EOWAaQQkpD)YJmpGobykxh@IPecXFHeu3&uegL3'
        b'2k#=!Asm<evV1t0*#NwISec1UT`z@I6p{QzrM4gt{h}N9=Mt;~KbdhXr~rK!aV%=VhwDOR2|upe6`nKW20E`EDqLI;L?S<9=13&%'
        b'xXne<FW}GOWPnSAwJ&j*Fw@Umf@IHeMZ(@g;WHPUJQV&wLiwR^T&%+)Ux~~`@4_wXxZ*{ac#KniJ-PGA8?L}!%ho`b6=Pbj^QYCZ'
        b'!gyRf8}o!*cP+wN;#o4HsabR=a%I}yDrJhu6^&WG5$;U7?uwg#ufBQ34Ki!vAr)gmJ-D}Y<EO1{?Gvqs(FOt|NBHW6=LGxCFWc-2'
        b'z+yh1e>#A<(*var9K#v|Is)Oba_?PucIre$bhWU(Z>I_nCmsHVf9TD?$N=A$T;%4UcJVN0`FhOz`QO~`lBl;2JtAB^j!x8>u*gEw'
        b'=iF<7;&c4Iz!{vWxXvF#&dBOkj>~{m);L4@y9R55A*YDh&ObXpNrt-TZ_~L;^wV#oU+J+CJzneMEzw4$Wx9<@Xe!utTHMrB(qc_<'
        b'Q7OuAFk`e4oD))%W~nk~^mxz6+T3roxZgg1{^ZF<yr-Kp3f`R~Z4_D-s%<!ykh@}c68O{iLXAeuO!O#2AFxp=EcN)BY@x0|o|Y$H'
        b'ldG~$yJ5~L%Fe#M?u|d$h;Ga70JA&Aoc?ak57$8pkwIXNUPXNJ2ydJw+CXQ%i*g3_Tr!ZH28|f3b6n}4T(lapt|ckM_4Pdlwef3('
        b'O#dbPN&Z?90M0*wc?%YSmv0#h@KSNgrC7n&+!MqczmLa4FW;y-EkSb^`sm8&wgeIdmjbP4dSLA-jv>&cU@<fH9kYJi(?X@J$(51H'
        b'><_EFZVn!>R7$pE8=KK%7QAcu;C9aYJ!Vb1Qgho&bb}jf`X>y8ndl~!YjSnwjBei#94SdKvDVaeRSFlCVQ@=Ra@hhgTadsOEOJ>>'
        b'&GI4xm0CKaYZ7+!$gJnC>&ttZ{;onC`$z`F={}O>yn8*ZNWSJdRi#d-OO$69%5;S)k^qj9NsUDIp(>kot}Um?Yt<U88iO^)U`;ky'
        b')1D<>BVK^<Utq94WT3Q>2jF?C!9W1_be2RR<>)cc$rT5v>g!&55#pC^k&8;8-n#x%AMX2>Fwjr7D|{~!Id5DyYjP?=#V-(MIy2xE'
        b'Tx=zJc5zXkh!1ltrOP77i0wxOq|`;}+S~%e=ij15<W$w8L5FrEtUj<OF*a+g#a)>cj{BBkde`-~GqRJX8gYX)R?`sRO@Fsy9FRRB'
        b'^;L7Vl^hx3+s$Fcl#md_Vp!xRnF`yuSO3O!Y{q#R7Quho952Jh!Jeu8C>ed%yry6O>~*g?=WzKsX^Z>dv3*o>M8VIYhpNJNuDI^m'
        b'avcWR5SQb2s_F>+@2<1f1aJP6i0GG-s&StV%en-=;!*)gKq2rB#0knf@$E-(#~<;m<&ZP|9p!wh@hmlZ){JtdC-H;~$T>oYEJacn'
        b'ZkmG`C=D6!PE@giPXG_OO$XMRAXcA#olXCQ$jHz?cD;qtc-5Ir=Vg|AtALh^Zb34kdqk%DqN-I_(ylN`h~2T6PfTd+9Jx@O%klGU'
        b'-^r5^?dTMZJHWDcs8ACK7=d-BV;old8b?Npmw|M#)|drHHy^-FFJcSwlVWjSh#+b?<bAPNR0iZ7cQA6>X7wuvH{;?9Sm9#aw;a2^'
        b'B53=epn|Pj)IxD8hZU|EW2uKM+CZf^$?(}-a;EOhD!Z=4a(2Q+J;eHcwC}G1quO%$p23at;uJ$_J@j>Zq6);#z1!Q7B!4xL5nUfi'
        b'lvh@z@2w(<nmj|MQ@jYnV)o2CxMx?CA}O|#%wX>IAo=`kIK^rD0DUU8Eol$#_&2s${aVzuq#4r9>d2_GNi%TYWzKRCMCu`B{cO#P'
        b'T-5768UIDJ0>FJ1EFmAk{10aUny*dh>$?r=#Y$q#;JX>sn{*rpjmV7mBwfbEpK&~?emeC(_AuY}=yrR})I&g}!Bd)AQ<G=TbebZu'
        b'1&N#0h6QTimUs|LIGQvgV1WX)@gYLMdN4l*zD(SR>HpC~O3JEC)3620p~Te4HxmXx%qOUWrI)r!bV)L=JL-@E_x%Y|TCkYixZ?n)'
        b'Kh?8gPYr=^QVF^uneyR>HC8U_Y4JCc(7n}Fh#L=MFm{ebSQg5O6M;8*S?bN|C=fLm%SLR$C1}!7$?2=Rp(&;EuH#J(%SuFa?BMj3'
        b'z>6o88C}eY9s`xIoe0qH0;QPK{xY;V#fG<mcsBn@aW1q-pcZ#<o7K-|@qB-k1Ljz2d-r{4`0Of(!LwD_AO_37`!6vl`j+Qvv$w~O'
        b'v1zv##d=Eeyqf5Fz2`SFu*$I1$yy&Wo#j^NBLU6lkd&S4`puyDD|$BdyqX9V$?%j_uBA>-Q4f%DSqgP^-?fs83(KprFO*!grir!K'
        b'>T8?T@vE;K0y$5`RwKE0lyDX$Np1sdWSHTz+Wlf(^)|h&$CWYD_YP-pTQ{rc7~E@;4&f#PrjP745MeQDT%5+~pX-4NNFLqxL>-gc'
        b'V<<{+pa8=LHzL=O#2LUl$@YuvUkycJCKO#!FP*~Rn9J$^*iA<8kAK#cZ__X8VKZhaf9&kZ;G#;zYbQwsOcv7?ZuQxuJvXARtpl|}'
        b'bNb~y>n`CY73cD;u928ZIZ|T=sCdZ#NJc~vmE~1{(Oy|%>HF01*+JdjZOU)Hb%cOj0~4J|=-HUqno{KJ;SvZmnA#pvTb3{G;<8W{'
        b'i23X$qJ#!Yq8#WxM}ylA4}9Nn?LX=RyOZ;k+gkOJ&~MXI98wRvAJ7x1RQ<6&w1-UgE#W{?#XnElV4xm8r<Wo0Rb(>AnEvr@&on<T'
        b'&}lZqQZ4)0r<OY-O5aFS@4Dl-Z(x$S)4lF8?&zCjB75w+y}TH>mTFBIC>%*x4=gWr#G$}&{oU?nvWEq2h$2a4mX5g-b(K{zmo-7('
        b'aSe&@a*)2ilMSQ<y7H(5;r?n8WQGw=30%j+@(ooZHFAAl_p3E75arn%W_SmiV!#)O0bSkXA~s_!a8~>_2Ms?f*43z>1;+w3)AU!m'
        b'K|K>0^9|}Jy=OoEFka?8vZ^5wePygWxvfc8vhS$pVt4bkZbN+LF(RNRhKqVjJTlP)t#8Qm&7NdIK(wMYsZ|zrC$h0(Sa<Svn5}=q'
        b'HrL@Gq^vt|vo;qLu45Z^a2+mw0Xvw4`<}&;4n1`p=BZ~=fAAWsUZ^~G=+S_RfAiY2<AA&&5&Z5AiH!vRIjM5I*3;abk_sL7{7<)='
        b'@3=1=<5gA60wU>945-XKM-X4yy8V1nE)FV$N&FC|_jYd`GtEZoY0sMo;?xv`eqZ-iwOE5?Wp38a%Szr3`tHwIRv4oCPuPN9lz$mp'
        b'aBlmILkli%2UM3hrm-8z-JiR+hKXk&+sSQ%o|@jkHft5^XD2_*#2x23#?f6|lr5f`J4io$%2|G_(PzML8rxsiKL@{0Dz8-|Quf>@'
        b'WotLEv24t-71M9-CX>s?NRclP#%BIC_7cv9NmdjYrjD4@zT-ZGzN#ceD<Z`D=U~p&kNI_Ik_7j?HwokGA6@aM6Z&c0;3;?&Lia)8'
        b'M)WOaiDQ&wUhQuF9qI=;ll|=O7li$bDmLhFX}{Yk^L}=()v0n{sw(|<q!GoYK;OqNJIvpO+N`+do&98sbtw?>th9w%dUISK1YHRz'
        b'%)rH0Im7G}ke5|RMJm-hP~U9#`)2GWi^>$f^RTqWcX?+&L58`Lt9)qx$20Ak*BTSEJ%0O)$31tu$l2a2I4g}f=ENP5lb(6q7pV+Z'
        b'ns(8ej3&p@G%<SN=b770hC*pJU&I20HQ9HR!<e{kWKw3PxgdXp!}Q%<hD!nikrtbeI~dLs0J2`|QqJhd9l}X6vN5Q3wX!|JA(&)A'
        b'rc%0#tqV|RL9E;yrm0jW0o?e6?x>24(5zCnm!Fo_u0-%ZOrXBa>CT$t?;R<+Xk8%w8;A8&C}W|{-~`|%#Jy;Vu2A~=CiKHyFpb+4'
        b';u{nC8EBQ#PhKm|fAU$eZzs$}9V}Kguoz%j8DJKQzX$9ZuiMT`xCU8GW7mj`Ii{8g44G<G$V4l|wkO7C<s%F1cUaaoWOH3W)jSc`'
        b'pn|`qz6Yx59Pdm36{wM;(1>pxmUIF)J&VEW7LJ?FPFP|NqH5>6eyIj_roqi^lHssmd;WFJuwk*UY62QwjVwIhYtZnT)e1zzOYk=?'
        b'YYf?aze5Wr&~SvOq3bs^d;&B)?ASKJldxJ1B#4W!)rqK|@9@Bve*=61fKyCc_<pWNCaL2&)W&Mw?p%wl&PQ$R=BxelH`U&SYL7WK'
        b'Otn#k+IS9i)3F9yeE?c=ludvcN@jo!>S?<MwSTR;{~B+P8pY2{kQr0lt_F0E_$(7>0p$y-pkRT+4EPNmY^v<fQ1+1Hi3wN`r%KA9'
        b'WUhD#7>EW^0kbcPn0oN~HJ8;uWa!1liHq<|t@};|G$crW9p67(yNDnRj+6=Hiy3%Qv+ma~xyGWWiDJWq{ty}`DEIvS8m8N8*s#c#'
        b'Fk$(zZ0DRVZ{Ue_8zMKlZ}%*mbf>D6<5+VnOf+M?y0%YQpXhu29%9>;Yf~Nn9mt=_F%#N@*8Mp3E1?HTjxbbKa=+|pC`)!IP?>tF'
        b'ZT(YFmg<;}%AUIqw-m}Abp%f6zqt=(f|AF@q6q`A9$A8h^iMp6UH`@XM*$?wbnhPK0vI*$Ouy<rzK5^5(7>eoZr`g=nugJslMz$Z'
        b'<^t^t9Ygn^{W;f~8dTo=O!1C;nDvQk1paU~^c?NH1k|3IOehgAzV}&ykfs;6+bH@P8EUpI&QV=^Y2h_mlev+W(FK__tafw&ePmU<'
        b'+R`H0IrkcRZ(ucmSb+MZ-RZFkuzN6#CbT17-aucVA@K;W!LO>pUZ4nVe^vA0<mzbgoO>7*c&&{xw9uKJIoC?ZG-;EtihFHOc<D@C'
        b'gUoBoEEarHu?H-4lGYhOv>pPBjwI+$C(UkwYW_Bzszg83Wgu=SUzRJ4avPP(QgaPQCbKQz^rnGnoNZB+{u>-#aK3F+GT4T?T-6$#'
        b'(Doi@Pn1I;Wc9LZ){i^EQ`Y4oPZ<i+lI7NpF5P@pWwub4D_@f+%LX3i6b0ntzS&r9!(_tirpdb)b)m~Z=O|wm7NgLm2UqNQ%%B$Z'
        b'go58VU;kBC8=cdl&ZHA&dVcCseI(n_USOCkz2)}mXmzFvx|W}*|3_CA4J#UA)~B4W@2=Nf%Ixao-xVp(59S>2GH7zV1v!Qdv-GW9'
        b'#p)-wN;R_3`d~od)#NmHcF`MVwz;1t@f{6xekSuWswwUV8-~uzY3f2>!q_rRM>u_Rmsy>8qd;N(8uaO+q=V9ezfMNI@B88|GGWel'
        b'*<jgwSZ1&;R&JB)4|X{dS@^3Bw*IBFk+8)qLT3OX9I^Kd>P+2yaBmmseO)eU5xAWxvVBK&d9Rdi(&>d4{M?+cLYH+vqT2|Kr+;Fg'
        b'7FmDSse3xQbSyhjXQm7+wJ3YJ%xpE-tV{M31?kJXT<W>D{JAdc68&Gh%+w;?d_+jaS^eu>q{yZ=ne$CH>tZIW6Ix`gnMqrN^shm0'
        b'QrP?yvo+Idf?-=^vziuf3DR!{T&cGFRF~DHFF`$C`~y1Z;8myA{$1Q2;hQ}{5UKjqPTv0qQO8XW-_u(<^YWGd5+=Wlx%b-KD5Pg{'
        b'1S!&4wmm9B@ia1owL2yg){3{?%}MAqP>ao06EFZ;Hd~i~?aah<+Ni~>6=+1%vDPJy4rHVLsS6r``9vzP`Dew0oIV@TbFAP&uUdy*'
        b'FnxgN2>^O@dgX8E3BIQ{b=lOJNt@&Zk)nU#*GG<^dn}dek{8*tg{1>5mDY4Zmi>&%t`oYb<kJ6uSU2&aT>KsfvJR5H(J$F6yIu<X'
        b'RkAnolKoQLlw`vgfp8<qwkBSr5<$K%Y!rfK24S#lmglIuoCSqpsrv)K4XUgxQJzpJSw&theYhiD^JoBn@MmL^Dm%GKN29Q<hjIG7'
        b'4^<lbhjduMmdU8K;)m~AGNw@hUCF^o)gl7d5sT(h)4L4seVAuXo&TdcW?dofdj!*SodlsLjPq#Eve;d6y|@dcd$A37Jcd!CE;?Ut'
        b'6?D-tnE_q6&xqwjbdic|v&=GIgp9Vl2(88T-iI4(KgQsu`IxOyvVm4D-<GW^u@sYF%&k}-NZslr6<S*iO@kXt3A$8j8L9ZzXr>Y#'
        b'#aFyCjq2|tLuneP+r9v0LJ?>#sA6O~TBW=gm~*X@)-0@0h`)H?I{wFmR~?0D!YIc^sqZ@VbsYpg_t)_`a5vdj2u`|>GvHCm<)iu@'
        b'|KP<F#<`9&=vxQHh-no0QFNy5$j58=xe1^Io>*}}f8`h8M9SCc`-pq~hip)@`I)|tIZ|Qz2I?IQ#!c0epnprR>39uHebh<Q;zBx@'
        b'rRKDUnf`j0){1Ca-X83D`!4id|9<D!eYm3zqtyv!YEDcrF5ZV}bIrlx*dE;Hx(o7{^aJjgb$4?QE_PuAF-QM$$FKc)@vZ_7K>uYp'
        b'CK%TS>)oA%F#v|feB@7l(x|sVu;$Qo0$n7asyjhnyAO!G)^z2#8rn+^EmUX;JjLqmr12<NT`XpdDeBA)L*1m_gy}qoFs5i%(zJju'
        b'3Mpsjf`1hS18-I+amSn3j4@n%XWUCCX|};kF+F;Zz>}!wI+AV5msK<!0CN?zKRWIeK@u=-a|n<>i{Vphb7zjH6R-fdU;DwJ6UJ0('
        b'f2RtvR$xTJj8`-)wSW`@f^}gLwA-j(-x&*b(%abf7F=9{(eB4$lX2f4F{m2*ax`V@Ob#y0kJ9IM5_qaXosFsXCNEEN1pz8*d#5TF'
        b'lvx4@4VBlK^ds(T!)W~Q4BK?zOq5!ir!~ZGgLUw(KD#q#Q728LnMDbtGMjECMJh`bRGTAO^Rx)~2~S&T0W4aoTooW(@yav6>VRV0'
        b'(SlJKopk=gR9fc(O)|Zr3iqAIl0LwFM`6X$K~{VU{^(Kp-!UqwQ$M?t4t~g>h$cgI&<t>=s!1&XV)aA^=vMSivo(R5)0vDHW~hNv'
        b'0b{sh|9H;rtH=fjof>`d$aqduho6HK-RX7L9cLRn8r>s6vFjbIa<@zww}i#lDkYg<rdSAlLCR#*JHC{0bSf*DzypYk0Mlk<#?u-B'
        b'NS>*Lqcw!mhLL#O`~s`QM$OS$v;c?^CZYHRu;u3{>;Iz-r}GmW&!ag4`2*i4E85S3BoQJZNQz?<ltaB_OR|C>0vzKUrRmHL=9O$P'
        b'ratTYBRpUHGVXA2`u+}sIte4r!^rzsK)!%>FWl3D`^vdubtW~dGj==JxZ?!zQ1%BZOx52guKi2sA$Yz7>q(eQ_{0}5j+lQ7H?0__'
        b'-n&W=5A*M=5MzAx<4`BNRz;*gSx^y52%d!chYYx{8Fcx>wo3xYnoZHPNn?Xnk4&`q+F<3+{s=AkInQ*o<S+Hl9dQwdO73*5U~%80'
        b'<2gTdWZPsbc1wGrCl?5PH+}}rnbnIw%*7pVPwW#BM3TPZDnB=8qq(_zBA|GI{!|CG{lAEFu;XNq*DV0rYT4h=R*q;hUlNeP^rC1e'
        b'qZetY!yPd8+w<cI{2?+3)AcvKt19?Y=%Ga1^rs0ky|^OO^x6bGGhF0*lo3s5X!L*U$oXdnkZt-W2fQ=$odwbW9n6WBKJTFOm%>xq'
        b'qUeqOKF;OGHSU5T5HlDLn;zq^oM(7~?~9qqGM=OCnBvG{Zb9w}#g+wcAeoNF7R+Cvz{ShBoF{*g%-IHf^(Jh(F90(HKV*K7L-J{U'
        b'sI&)u#X`Q!gQ3OD{16$6evPZekAN@x7>__PPKwaE6|^ARm&*YfEWjzd&is&1$LZ(&FSw1%<+er+K*iv2>mR&2<r81S#Trhp{a@f~'
        b'0Q_A9ZtCMm5oy{lGFu-dBTkD-@2%OS3MyQ;9Q0C#0;eugk79z^`-8B(XDj!k6L&7_qdP;c5=JUJ+&{+h_E7Q62`Zxlotj*0ia@@o'
        b'G7Veh$zH94?(Ub+ZTFs)1Z}o#9<K-oJ4>J30i&C-mim7kW*RHKl}+nFzfb9DeTM;GYk7G(H5dLwSroz49QZTKax?_g!uEofs5lUY'
        b'z(O@{%Eby3afcNvRIJv^t{T*0^gdx6B<0vO++@b|1K-0keqRpd`YYe_9BGQZ2FrUYVboDGU{Tajf~(qMP|@h6db|MEqxUBCvW}b}'
        b'Bs)_iP3r*l>&3Mcch%qql^Ftx#Z9+@vI3HHYE||lLKK8x@@lqO4%P^7q9iDb<<0tz+L~#Wep$h-39`g7^JlaV($Uj0;k7<0{*(hg'
        b'I?i%r2Dl6?K67X9)n|!KZ-fRVCasvJz%vM(syNOsvKhcW$44C2kuTp{s1}E+<PmCoCPppA@NozFLS290dz;`B=v^@}6THghs!eZ%'
        b'0~(7w>Fept5R80=e<Aau;$s<tFBSmnZ3Cwd04Ai}U(eIT2RV!eCFvT`+?Yss+A(qmO>S6QUcpVLxy3IB0qdyGVeoa16CCx?RhrJ$'
        b'nlb#mc%0K8`93edJ=AgNXEO{z4{l2Q8L_wQ`}^<Eao>sw?aQWjxSZoxsm7~d64`L6K{TsQv?ft!|Gg08+q&$kPA61>abASp_Svin'
        b'F?%<!_JP`7w-*;5!z}rFZ7!)ax83}X$o}^>%WFEitxJ_(Ww|~#sw*}^29pxtF2b@H6&r!<HTrxvSxfG1IkQ?-Th(Kqri{O#RL>)g'
        b');F)J%)qA^LB*RdP3tI@vuE-M@%&e}5R0)O+UC3GOTcWJ#ma*L(02P+lreTUZh8qBG_kjE@r#o=&Z{p$?=_j5SzP?{9YXYQ&Qst2'
        b'qADEAeok|bYl4&fQHaS8-0qTf^JjbrIF?|AO5C>?i;2O-&;A@+EOk8dGhhchV&%`I>rhK^?f*<fedTZ=zUx<g?^Op`{y)~<J*=rK'
        b'T^!!Ggph1?hd@9?yY~*^5>b;K6|mYS0VATeNi2A2dkz6X+uAdTR-Bejlh{GDI0JDyUTV*TSn8#vVmi~>TFwBrhzbfQf(S}&nfCNH'
        b'*3oLClJ8wRXlKsveE)pE?|FE_UTd%YuC?Cv-q%fsRXTnKMDx6)y0E_U-cuXew%s0<gPYU#{cS_>75la;4`|g;c%^V3yL>54td1et'
        b'_F^7xI*<k(`zE1SUa)hAEqMo<%J9w^&qu0-#F6%U2{+oxZ}X=@$Rb&ZagHlIk%ExrXL<ATk>>$l=Q;W^--A1d4E1ku9$(J42HAoQ'
        b'Kh36-^CCw+y*KyO%GJ<TF8d0-z{@Xire8_O-5#;AYKCIjvZXxG@$fR`{@say+d#{528&loA7A;T_+JCR<a|s~4%h~=Z0iWMwk%)y'
        b'lxjYPR{n95E<1Q>M@*aQ=kWUBqwyV+Do@;P^~L#HOztm-&|;mWD?n<=FK9?21I#wH2jh%aL~7I7*(;<u8pg-D@JfMbfZ8Wrp#u)>'
        b'g5=lbffk0|rY#t!UfIT}uh8?$pxu#I{3m{*kG(0`xV1o$w`}RZmBdC3|5n-BVgmNrR!!z$RtAQoWamRFX(aRp-i3S9(_-4T9X%3R'
        b'@C&l{!<`f1CCcvXX<=O3U8D>Pza$r9V|}d+{iORx7(Bq1YOG%YPj;x<`tQ-!m!%uG@JRmhD#>_~n1x_Vvcwv~C__x_`0TFrRrrP^'
        b'9&ZybW#PH$C7?a$g}Bcz(^ilt_VbtLu6S7rfX>B`l3Bp}@C|$kVtD6hn-RX*8UG!$t9lc>WiWZ$Pa%!uagrF%Vsec{1HWxQgC03^'
        b'Ib*4M{XoeM!n!6jQh#p=QTgpH6!3OVm##vBgqz_lit{=jem=6$DOe*YWcN%5>Tbg*=lhrG*j>_^;^u;6bS@R|e0VShq)T;_^$y89'
        b'rz1KfDt`>|WK~BLUlhj$E(?5GiE4^Kyc<yjeb3}x9J(((BDMc{FYOQ34yYVFH=Xtao@kqkY_F81VLxK)ZO(t$!GYkM$*mo7IA{DK'
        b'cV4(--+P&tRH=LH0t&ep3lEPX3B!UvYGRYv!o&Aa%!OwPxfv+t!izDN!-#S`Tt*}02rPeC1414JVnmM>UO_Q0_b}*O@xytgnW&hD'
        b'GZ(NFXx0KA1!A1Pz6?gJi=}Mgq<sjIUhYwNF61&zsY+IZ>T;G|*58LI_z2#<2I^AxOmh}p&QK?*h{}3Q`@4Je%*txiegEy`7@~4F'
        b'>U^0-!Y4!TrMb7cBEX(3NflB2+P$>5q@G(Kxhm?HkrBn)?xkf*e{;(Nys}9Nyuz)#{ELk^{SKH2*7jRm)#c<WLfUrAZolkI7+NZs'
        b'ZL<bV60uC|ZH+`Q5#n?7ZKK3!BE@IrZ4)t-R?`HQbPmQ>B{5V-RmR^j;Zq@_I;t)94og0V<YCO66KiC=cEJZ0qB80ZxEn<gQc^}0'
        b'gbk}D_lhDSFsb;Qdk=MQqOq>{GP=t`WzN-@7a7fqv&@e#H7{|;ihTd?m+iXCOYtRH_~S-=u?AnH!gC#k5<7pHTXC6`Se9Ba(t?}t'
        b'MfRp4a0%^GE;|Y%?UODu%AiA%pt2Ae3u&}a>KE|Z<jb~af(1%l0k11C>K?q}n9DpdMJ*6q_T{=qFRKW`rbFw!pn!@X#RpPFP~rm>'
        b'QMBAZUAEsIQjrRcWHFa<nN<Q0u`DN7ktU?BB{NyzUyGDs!RgRxvSx?7!{E6{Pn@3(eL<>1q6=tdqjjq{2BDkKyMqMx{SdNfisYb6'
        b'?c8NBVpHo+6e+l`hrsaVCPT**T*BooMKb#rL!@Lnc)j2WoABp0G7%15Q61CPq2Qt~+Ybz`C__7w6v^uq+{Gb81miE0772G@D0aOJ'
        b'98iP&GMObqp}5G)VONUhvVcLs*5o>eXp$sma61Qu2VBJvR$ZvF@s0o*@gIaW15uj;KeX%|VVwof2kfs63da-CirU#LGy;CmQKGw_'
        b'b`%kU4;S*68(tU;+bse)IbBLvTW=WxLtqJ>C?>3l7#&+yv>^F~OnbwSyJ<*}B#@E}uwy#1YTp?G%hMy7%rH6uKeTSokUA$qIIc&)'
        b'%gG1=!{vt8hsdm{_WvAm?--&NKq0SWvPw3!bU(XsTY{pzJYPvlvdEm&a#gWLHVeiEo;~eIszM{}l|u;BEa<ZsWOfwi-<!Ltt>Gs@'
        b'vmpQYPxX2C5@uQt{RBerwasY1Tb}3mV)4irjSM3tq;Q-C;fWxmYe)<prI$jO`sbg+6@jFcehG4Q(~z?f^|b(8@}ivOOND)pq{qZB'
        b'Gd?Tq)1|*oR9Y}$-%NODn~n+of%Ml`8J<JMV{a1HY>b;Z2(FAc5{SLpX58Y*1jB|QFylHb_M#!t5Ycf@3>p4y$X+!>T2g;8W*-|e'
        b'>=+UXbyjdf_Bl`u$=EWZAneOYkFgmXLvv@PEM4X$ti?p~Ux>=zU<vafRT+gt%9@Ooz?(xDEtS4H3ZFlf9wQO<y_o)boAB;ib7s-8'
        b'v{b)(bAf(?bJmbxJt9~e5!lybL{C^yNz=a|+8(-Pm_9^H3$q%X=|e(NPQ>~-95$$t&bA3by(nU&cYorvLmG>Y`*;uqLP~NlWjx0Y'
        b'L334>)N~Miy&<$3va#}9NX?I0cf(Mq9oMZpe@YlZZT$(Gt6dgFwDpEkHs=$E9r&lb@9r`J2=*4Y0wFPlU}rJuP-5Fp9_5-sZVqUH'
        b'if<c_G9bCxsc5|!=z(yUQk2O5zbS*8ga4uo&RqK6mBIIe50n9Df}MrqxwIjk$HI-SeEKKu>%qBFF&Z~Ji%4HBA*5g81x!$7F%(3@'
        b'uaK{*;D!fzVwKvDb3=nrOhru55b2l_Jm`m53}n`9(vr^g4H{0PxAqv|mMI_v$gGDz0)*LLS{V}RUP*`Xjv$iXM~mQvy5AJ~FoZX1'
        b'RCv!dho@sf377e>(wYsR)xA!kBg%T<j^XZLUF~23t$&|&e}d$gdfRmFlR^81!B&9X!E_|Fg>a~q`}HLUzi{twG25OJ7}INbiI%Yb'
        b'h<Cie^Bz_!;j`v)FJ7|0H+Wy*MDXO?j;J=z&tTOVW)6nKif9>vu@YSNIu|rmdKnk$+=W~gJXc-_S@S|5U-ExCUx*_3#zN<G7;eWe'
        b'!)?=3`iI#XmU3`L7;awKXhb0=4=31Is^TxhJi6WmGAdqxG3&aYT6+_09vIf<`x%bIR{%z%m~?O%ki#E-6bKi9fZy*D^F7?dsAK~Q'
        b'1C*vHz1%z)YsWh%{0)5R06G!P4rq~m?V!!5v>{@9)IR@`NLQJVG-W95C4)dzP?!FG)dCm_E{a<<sLpv#G}5`U!%d|iQY;)8gnKRA'
        b'mO=Z|gPVwo>!rND?EY-ny5)n8<Q#`HyE;aC`(A*{ZuRN?EsV$cnETO7FktrigY-mR@@;EFh&Ky-OrnQ-jJL;eH!k^!k9aQIm%6#e'
        b'&+tlh>Bq`uo@wOS0Fd}0W%yi0-mX?>JjZzkGoV^MuNS~a24hAj9Kr7;P|~Mvf`OO?!@;Ewiq`u~G)75S+r&FOexM9L2)Y67{ngZA'
        b'u_nxjb^x#TFxt_(79ZQT_$FHTXS7}mamj-bHwkGH=I3YEPnCd^WWDkeP!*>CMkrjIufZyB-$vT((4{eLh97WF8g#VI9nMqQ@?Go3'
        b'4GOJ#m4pI0?Z6MtNe5x?`Ajc-HWxBLn9rHLtvrjQFnhcpU4?W?cD(u=Q`VY*ZcNyyi6F{86CX=RDZvOqh6yqx&}el1KklYQOEovq'
        b'W@!~P#QM2toa>zJ12$<8BT$4|YQV;3M+zRyjubox!)$bwQb330%El6=w1llVT2l%J>I|sIC1%vP?r)dd$hcMmoo19BPA({C0FDO;'
        b'twiZ6X9~)Z972bIlmi9LD}6>;u$px>Q)Tajyg+3g%F+^M-MLH60Iiv_iAf-|b?*#74w`c*VNC7Hbsd+Q+t``{N?)QZ?O+Nz*jD?R'
        b'=H?sCt!7$X(4lW`rdpjw=ZQ;YNjb^42<gk1{o17?qnB*uOr7^qSxHU;J!Y?caw%-cfPtfq|G^<msP46&x<pDd!YYciW;opgw%NhG'
        b'Ul`uM!~=SHrB0(Eh_EIo;DaQY!Lnd6WpM9YvK8yrgW>X@1Exfs%@cIR>I$SmCL$NqsvcRA6S>Qm?i;pp?WMbEiIvSa&;jElT0Hx}'
        b'hy;VO$ecSecXkn;3$`N|UTl(_G(TqY2kRf6P2!LFK4uHV^|o&B05m_mR=JQf1rCok{snmrpd>&}dqk;mUr9I)-x24xW(<qmE9P7Y'
        b'vp47rkPD*PNCs8_CU=PQxi+LK9!4b_LNHd4ES-(i2FL{vI0Yh;!=TyMAU%QZsY8<LQBWR`G-;LgM+QJ`K)$`;Qdo27?^g|K!xkR|'
        b'+c=E+<f}x1GH7`6l7`F>F)IViLJpu6(*{l4N_XWYU=UkIP|xcyD#*9$ZFp{YEG*#kAJk(y$U_-MG7AUo4X)n1qjW4{)Gc*hPCy%7'
        b'%j-%vu{*a!6d%8vHd9)7!*c;Ild;~zzpp80%5vB;X+nO4JfEZunU@@&>46VdE+r*6z{RL|u`U&XgLTZr#E0$TdVV%)lsq_AHP8iW'
        b'%l#CThCySLIyNd7-TCwo8an7T_{iMTm;6N;HXfeGc+T1r;+9;3984rEYfOmCyY$Nz4q(btA*s09mQL^Cgt8N%@~6kU9|B4>j>XQb'
        b'M)2M9V@KQ0gbcDv^lZ=);9D<Okfc#XvZzFsQ8<1#KYvtu0>Rl^<Yq1z34?|Z5Co%+;dMrfL1PiPp9dVos*V`x-(?!Y0IC_@sECI&'
        b'7E~6Vp@_QZ)mrQl_rrh~V%0IxI?^&*Wl6V2j;3q|AFJ~21FNR(#tkm<(sBY#(`y-U46S)LobO&FNrO!t_J0)`Qb3!c!4G@?7I$#~'
        b'EQh^D_tyjWgMtPUsznb1*8?wC?JXk1&B9Q#{^k9t0mtF9plAdF(W78tD=Y3Hac;eH4{XBVJ*2vmC01q>JtRq_<43{gw@U6};Ep?-'
        b'!t)Z4`_d_+7zW})ngIVn1FX9>fHYQNPNicM%ZPZMupB>adS*v~X+!k}y%){p=4b9TzdMjn9r!fc-xBREzKAx-Nzw!=n>SBKC*aEX'
        b'L^U5JWfLhusdgNGr6#N&HAok6|1r=+v8^m9xcUUDI=+p)A)Lo8iKgYMg+z`f!?+@9A)hHoC*8n!WZz~7k{2XRlBw_D{OO;5;%6z2'
        b'(J?g9sNLK|a2qfBTTCh5VFHszK-;x8uI%E0yp%FAJXQThUE4qc?Vg94=i$<Bt;ytmGvMGK+xyw#*z(uYKsojB3ozd|t^ASzKfkMM'
        b'gU@%vdW*uiX9xVez50+tH^p5f3Y<baH{&8La}aTKtRnACnQiChrz5@Gv}v-M<Q;4tv*mR{x)DoRkq`;JuHl(2UZQOS#uW`5aDWmY'
        b'!S0qG(u2+paMOLh4PN|Hzth5>9&M1-?BBs|+EKcP@j4$V<EGt>Oo?FG=#r>ZZXq-QE53Kf%UM9m_&~SMQ6oc!n}JM>*_2+l1Drwl'
        b'21*(p8Q}T(4lb21nw{FMenH~lW*}{*ryAc^dN_-4_=-LggdVbV1Bd_W6YVN5_XskrU~E#AuCcLMbK>fx28p}uVt9iwf&L%-y!zQD'
        b'iF-&KV=m3E8CX^*<<bUH3R7b^-GIPN15dO{Mb6hJ#Sv{9EW<%7&>X+!O$EDaM-98-L%_vMO#j+umwv;CJBT&|3X^zHn8=SGOo<X&'
        b'naqrX-jT=e9`t}P0i=RF$;d<!C66R2m4x7i`oZ6@5kU-pjwH#AjFz(x93aEO0;!23K{tI-++!RTH%NSdl;X$%(vr#H10K}IOqGnn'
        b'a4-pqQ5BI`L?I#7;9T&cSA0t@q^vx;h+4x6+zdbkn?$j*HiLgHeLLiEKH_j%UY1DT3h~ZIcz7hNbs^LbUPG$OFy4oy8b@|Y!_$q@'
        b'u!+IV06oR(0pnL-3_wpIPvznNWegnR7~JQNHOmT-sVpeh@F+5d4CD71)<&V_8Z0GR#bB5;=Ao(HiuaN2na2p60QiCoP=yui!7$c~'
        b'uZ6>Z_uRLP@8?``iI%arpu-~O{PjMJM|>iT8jVso{0b_sWgY0&l!yOWKZcbf(u^6%Xbvk!fFPRM<^oX_f}L&u(?#2uo&BhNQ@`j|'
        b'A<bw?QQCK3gpStyt8!%ZH{3ff+6((ve?d4>GFQ}+vN`sui<obZSDU_n;_@S}^!tm`0TcPBDc~sW_`ASPb1zoK`Bt(!cM+9cSnb08'
        b'I{!sas>fHwsBatG)_zaQ67>Or9@pc{a$EY*rpfkMJzN$&sj*4l*tj8lbc}<WySLuU&0QR4FTc3+C?V~}KDbD<UBc#$EXyP+`^34H'
        b'n?zd*X8+a2<uOUc$i%fj*$;im|A*}8=Z=<)#-%%&B=)B-`nBox)Lr|N7Y|Cb<<bM6t8=mXO?NXtH{@SDAQ3dS<tsCmrpG*KSlBOU'
        b'GSx-`$kHL+i3t=aL}JTSN_*KwkW;oQ*8aprk26h}|E?jrzs`Emp;@AyFAPht>UeAKb+mhzMfC3eOF!C==Eu_a5YiLa$fI|mvFSI_'
        b'@#BVUfHW;Yz6&*c7^CfvYp*@9Tw6b``WsXk`R?)+%VUK3GGSr(pcRlxey7<!-0wDA6k;Zz{hN6c1mu_*^){;F3%$VDz&+wjKnfMT'
        b'*X|Eo#b55bOTzGdcd6oquKTao-UJh<SxkW$h9aq8fZ5R0oB#{~W<SpYbf7?A9(;_r!G_Ab0?#!olr{%Qy9}_MfrogJ{8({O65kMl'
        b'2jtJsf)>pKdkpz?qDw#K{&A1ih%UWLOd`Xqug?=U%!2(ud#-<_y$=i3+?Rbk&s6sSa@uSACk7(111ms>*su5V+%&`A`g^oCzG%kc'
        b'vg9`j>1M1ifL7!#E=-<GNZlAs@XpCxZGVO(#UVH+@y-Nppr7ZJ)rBchJWs;Qx(oe1ogac51#+TGv$<8LXM5N{%i8+#sQlc7`qaBm'
        b'&8!Um_<tcXSoTIah_jAS5I}+!XbmT`u#v~4eyybCcYUj`O1S3!Rz4F^gbb@+Kd!Q6wC<(811~1!D!i$g>WQ5mXO?w#s6kS^=Z?Fs'
        b'&y$j=K1%qxX<j+jAn`gEp*vt8#VztEu$^(r+LQgQTv|;BTYIR#)tTm5_^vkYt~Duy2=hfml5MG>9$=}AEt4PGGH=1+oGp_H>$Ffn'
        b'o9pPsF~uprL~CjcYEP-8DWUoccPf*Ry!3?M%1*hRee@*J6q-uQpeT0qT=7Yjb#lnli}z^LTeS-UGOb^hSbs`oH-c19)g9||KZUBb'
        b'Mu#vu#*zD#pkeCL`vY$w<|@7@k<JQXhP8beMe1{%UM_9Re-n^nc&UH+jwG<ogb-Rsm)(b!1ng#Ps-V}ICWaXmn0}9ab-z%YVNDGg'
        b'O8PU%jHS{$p~W7cg39^$Vz2ZSXgE4VpeV}lbU#2zQITe<BuWn2I!$5|J#St!BY|G-Xd=K+T2beY?-S1xz<6_Xe)-c-E==yIAeXkF'
        b'ESk&j_Y<aK<sJ1lOdw3$f_}l0X0Z0#f9~VSG!PD8U;!2J^VwyaOxz-nBtT=a`V5Lqp^{Y-fp^Qq2uG<%8t5?3ya^48;v5NQ>i0)Y'
        b'=Kx{$IKLwits)#I?Q{Ck!Wv%1E7y3rIYQW@3NYa2mcE3P33yb2!}m}irkr8RLEpI03=L8?`f$ej8Zi(PPObe1{0DUd3KTRBWB?HZ'
        b'5a9a8`$d4+U7|SyNkqyh=N0gqAqfP{CL`V~6Pdjf2?XSem5II>B*P)RGSL_Fin<1RxlV$VOPJqFMRl`o@IqMKl#1$R-MzjC>ZbHQ'
        b'%b&RVC@*2Eqv{i++|PXiH{Zi85SM#dy<CoiTPPIHF<iOeDYOb2tG6)IQ8>fB5{(=i5YOZy(ZZ&0`_LjNiJzZc{A&_viDEhTw?5F9'
        b'1ARgv3HFyq#3<<Rj~JJzzrzR(2e!ua_b>PiXWYl9m;!v}{S!X({uQ5N3jIDl^F(~+v0>efkokY3z7O~PqQ0vx{EPZN*!Mrxw{vb-'
        b'gYPfmj=bGhx2KO+tV*N#TwCDu8vm&$+)rOXXSC_u>-)ks<my5Nx3|whByhj)b68~JG7>env#$sLlqB>mU42;No&#P)qD$`p$$z+p'
        b'J5tkE_iA6l;=t*YQ-|CO5j=Ea$G`W5Pwc2ioli@DM!{7A*vZ_B05%dT`l?XHdHU#W4q^)T0_4fvjy_T6r>(2#+gU7gB*$^T>T?vT'
        b'QX(9_6cno7iNfmAZ!m{10g`RgP!f!Q5--}$YX4PVZBbuJo*=1e<)+gL&%49hJanwEa6^Ma=olSRxc2YR_iav%?ApeBxQhUL(oodb'
        b'ni`csHn&rmKY}Z?HrPC<^ck5h6e(2q)VY(Jh{{3SQ}>%K0%46K6TSw|p>iXUe3Y<yaa8LZA{_5uM<6?T1;IVum+@mJ!QH&T6Zm&!'
        b'9xl5&PWl{a&*|gl_6ffBIlRz|JG7=vsujd?aHh%%aYrGMDF8NZT_vO+l7@MG4qqX!c?|WhkVNawqht=BWmyzad6?8rk9x4;-p{4<'
        b'bsd8L+JvZ%_%{9qI7Kua&`o~rQ2oL?JX)SUpClALM5*XQO|CqA7v#7$Hfow&J@8(Wyl!^i$m4h1lln*^u}Vf}>6fjMIJ8nn5x!-O'
        b'(XQ_Eycfzqr^;nY>N6R1bj-JCTn#aO0iSF6j=E)i23cPM{c*riM7cY9Q5ZC`FGI3yeS&+qSNzPN=nL@44%Ku&pJcdq!Lc-P<Y&qr'
        b'x{x7Ru>K)8))y{>_xVYa;pPQ@R+^!yH=shtzKk3RLXJRE>MzJ6kM`AtF0}fh-S4AH4BuRMaMDZtcXa+XEWo3qUg`&E?#l~?hTc}5'
        b'=}{E~2)&<IYNN+-UtAElv=kz|G*bHVsJK1{MH6i<s^VLR7)^A&hPW!s`BgxxMz#tWPr!FoqVWWLS0$Es0Y$Z|7)XKf6b@;l@-rYK'
        b'9Mu*-ur!JvAcF}^AJH@je*|pr1=B!0WfY{UpL-Z24+=%*DP24R8YuvhbfwbY5b{CN!TR3`HL_Hz$oalJrtZiEkRZ*XFh$92y^!qT'
        b'9))K=muZ@YWQxy5)g8Q`&r|wDfQuz4w8b;|Q9Cw8(D9|E(T)@MY`V=3r5Xx=-(T}O!|rCic6CxZA+?V3<lkJo8FcppbV1B-GmScY'
        b'Q_u{T6BB$%=}~BX9JloX5VM|lWf04w1ZQjppCUM%ae{Lq?~D($JVo!(W+<eSzz6e{pt*$rmTY`d@I8g*V`4(~zh2;dI2iaNlkONc'
        b'Uf3iN&f$DkT2;)ij|1RM+U2v3v|af17c2g;^;`noK)B0A0ToM2e9Lw?fJ|ogHW7kmG5zt*BBBisp}STDUn#1m4jx{FO00KB!GQDo'
        b'6!kL|{+6}HF?Ws}0UBc9*<B<;i{X}Eph+KEk~WF&!OOUW6|D|#GN|)k_Xw@}6&jwKQn?f3lNZntLhC3UvpqupTjV2`?@;iq-+}L0'
        b'zJsW|I_k%lLw}1?6^85!JigpPMx(U`gJ9~#mT__X@i<43w5%w?!A%sn_!WGnFhVhH=SS^iuNVImEGk|y*&&(2rZQ-mu<?RN61lg3'
        b'Zy>#JqADVbl*~ddF*dHO59cGY>E9xoWkEKWC3FltI=Ja5UbFUs`UNb|!ZZ-tCkO|Tt*(zcQA9`=V)fwGaB<KO!I=P+JDihHE1XjV'
        b'BHQ7doL=;z`<V-VZi?$D>v87R|JO{zx97nvw`qbbh875*_?I3tjK2U5yk9emG*3~PbG4t$G<^O)i!qp7gHJImyTG#XHlsKz$q<zq'
        b'bjp?C<argD$S~-Zd328T-kFB?di_PyiVsmo&i2-w>n;9i0<;~CQ4Uf6ri3T5(+lIdW9L<PJjf*s*O`3i!{S{tIbW~8aN5Y*)RC6n'
        b'y3cw?u1~1@syEz0-q+6RTq}sos9*40JmU^pHu&NwYDQ%zTK1>E0Ig$5F?@M3#9;B2eIc>(r|L~a+qcNf<<9krQu_amt`A8UhPXeR'
        b'5BM>jU(6n3@)zMESyi|{IgiZnmI@%cVwu9O1_r@^#OuEga{tv^rp18BfWTWfX@SJHA`(lP^=nP4vCTe;cEcLc#Nl*2*=QGh0^+gf'
        b'M^zF787cT%7-+vrBD7TXUTs-Rnl)skvFB6;%8Z=i`<NxoiKN6NCLbcrlSqjfo=I~;-QRk(+X?BDqgYv8uEE}04*Fz1URJlL9C$Eq'
        b'lvhotuapF|GogZ!iaWkJ?BGhnfA+Tgs`skK(4(1o<U%jJ(K<5b$s33SOMN<-4D`NWbmTMTKkfP2(i`6MrTw$ABVOvcF5sV9@K5y`'
        b'O5aF<Fnx-29mBx{F&U^vo-H-vrT~TJhmYZPhk6?WY^x6&xg6x&y`Ay^KcAlLuUk}nHE5;&j-l!OsL5y^bvby@w-Ilr;E)908BOm;'
        b'5p9X1Xs#UkG7ZnD<BEGTRAod?hVgn-BG1FnO{b@T=gp>4!(XxfefW^9Lo-B7BLyy-mTY-eZy(p|_pLgbCumW;qSd*m$GPOHbMbXx'
        b'gx`a}UF6{&yUyia<repFOP;1(?X2f8=K4M3dRIAI#kRf|YHnwI9jvDzRNA0)buhkn*?KMM&g!jutTzB|hCDN{X4;Wmy;nKiNBDK!'
        b'f+L%I56HUXdRxU=L(&{M(oH}W{(U(|W&0-)l|SAq%gGsxI8fIVQTz(s@nV3R?&svi&(j`1R<;j!m9wR#H?~AX*G}yP<=~l^SPB|I'
        b'R3rR~#4W2++!xQ+CiV(zC{Q@AG9^DT(f=OOA*JYy;KY284=Iuca>Pw>lY0G8iPG~JS~dYB_g+ZYH`Dq~2rX^!qV=uG#t6V`+uLZJ'
        b'{=TPBUOl{gvC@yYBV}R<pT_%4piH@*b6_IzL|h54P)RIg<V<t`-Am_cl9gq6bZO}-@Eyv`(RK5Cfy3(M1b6qmz}q{{p?x}|=fe9n'
        b'+TOocrol&iN?&@j$A>$7n11<YW|k6+O8d=ow&f_C;Bcnxk0q=J?}0&+L2y5v7YZM1tG`z_qqo!uPC5gP01vpHBEbC>Qtj$<KRYyd'
        b'{ToW(tY&@L4zyF|>bcTViYZs>GnrD+2-pu^<?Hth{pWdSwxF>)G?-!dyrbwbY0W(l06phZqDpu*k4FoKUC4YkM}xp!OzOk_B61q$'
        b'vZWLX{h{qfrDbfzIk54sjrmMQ(GNp0yYl;Szw%$=eq(;vFJZqiuj_u;uUriKmERBhmERBhAzv+HEb<4R{D1Jn_MQKqe%OoW{>2Y_'
        b'<NQDSVfMY}!>$-9$q=-QlM4yGzTi5i>;C+FOUe1Vv*$B$({K<C?G0RN0lbB!6~oDoTs#kYf;3Mz`N36R<lcTxoY9<an-esVau}r}'
        b'-RCz)8j&EA2%F6Yj74*ad<z5R-JWn^11hYMZ^oyCf;sZpc_vP-F(+yy;@U9tB1S0(b>c2Zh0%m$e30ejB>tF6Vm|Wmd5w9J1~)(('
        b'FhUM89>e5lW^yem4A1~FqmqLp?P;xOF+x)lnh5KkM@MFj$wH8eBUA5G$4kHXUcjRrhh1oOx;Yx0g9M4VOH?f=;~ajh?sw;HV+0si'
        b'KZrLF^&>=E=x(t=VtDmDck^68gCS^96ST<yt@7;mN8--27pYDXa*LM}(tm`&49%tqhjaQoNg1bqnyCCcXaeqD5BMK^)E;jy&L&c&'
        b'yuMj<`Vg;0&IReEwovX{J)~r|KV<=k62Nf4nTxUC49l?qm+N~ZTJLWLB>P_4T()p7h?w-KXei95ECeS2otd3=-u?4Aal&Pemz(Pl'
        b'sW_E!l~O>+;Qb;aw-;#HhA2@$wEPz!qhT=vrCta-z~R&b8(2*7+zfDlSsTTJ1Dppm%h(_j9AF!e;UhjV2dG%gd<C9S3~?C>o&g~P'
        b'38Scp=rg0EWK+dw<RQ=VaAsSx7(nbm4z2y#xn>?s(A&bvlReF7#mA#!m^0IKQrX-pddOd&LyJB-7`B7u63>g~QLBATeI3CQbN$Zj'
        b'j;P8%+~wZtX&}RQJk{Mh=YAjIrR{fjy<B$EM51!f-6L<Gt9$2M@!AQMJCW;T;m|Q$p8NCKCUIWd)kOsk-vhqCHiRa&Er;)P@o1@l'
        b'37&!dJCvqUKoMK90W!MEm1}Q+NG>R#noE?BQNXi>BGw9QXvGv@tw6NeT_(|O$VNRhq3%5r-k0Y9A+QiWWNjufW{^ELB@Q{j`xZc4'
        b'J^~96EWrLXRKaePtl?SnzH=Z7(6f)S0J08&d%%+9Y|~px^QIn$W<I>aOy5AJ$#mmHVRi#GVh?^dz&+KIu!xT5d5imR2s!WS4BO77'
        b'>QYF{N^C`ZN8v%zN}wbBGA#L<LkBH>PH&C*9(!t*!>O0v4fSXi&<R~#8=52ylr<7LUI#u`uS5X>Eq=$n`J7?Xxs=<f`#O5K)N|;1'
        b'l_;tlTwvdK+I!T2eY~$IIi9dSigCp~7XGp7PlqYAzigic>e%@m=HX-2UypjZIlOX>1x0achN;E?Ajmj;j5T#p6_;T=hSAYzLf0`C'
        b'2&f_eV}Y&`J;v6QQWa$|7LY1E#;&~%|6xRcd|^-uj<M{6u|RvffCMc-#DMTZAmVKFk(bLb9b+xv$R#OF;+3VA_fU`qC^($txrZ$v'
        b'iXBQ63m1WyYAF7l5DMY!Mi9)8o~t>A$kZl&Qpi1Oj_rXD;n|b~1=z+<D74x8IEeH|K}5S;6dHN}!p-qG(?EULfT_^Qdr*;y9i~8v'
        b'v~u%+(|FG8;RGnz+)S}71(@(UXIR9QGN4&J+#{_{1Mkc*HB->#8WRQVmoz7}mOV#5RP{5h@V0+i^ViLdH5&#ODvmb(X>-TLBdtB?'
        b'cAQC6%}z?aaI%}|xt^j{KRVu{TqCXt19VqhytZ9g^9JME%2pg3-m8S%nm5>rO|Gp>*N2c|*ZvG|n=6%2AOM&>$~3-?ZmIKtY}m^9'
        b'{)~zsxA+YP%$^z#D&~4a8F()QC84WOvh=7Dt<c#Ds5e02f~`vLJE3rmFc@IH**;R%e$xXsTn%!^)1ZuLtFpGW8%(<U#WM9!=4ubR'
        b'MdT<Ou&+TVo`6l==5lR#Qw|m%7<ypteUL&UDyuB|4xJC;3q9!Ow`|3w#vd4<s)}P>m)XW42I#4|ldX8Eu>&!7X$8CXPGdQPXlOOt'
        b'_=3`L_=+u`Da~Wie&9R?NXImvtpS<<;g`s?a?_Cq2RyuZjL97hp&l4l#N>w3C5Xuj<|{$$h2Iu(8RkHb?QO)*U>=!Y>qfi^uMQwi'
        b'K2b<WGeUKTd*-(01e5=u<o=_Z=U-NPFf=(pV4x4s9a0mCw&@{mb$8wJ9-e3D*WgXPlWI#1`Nd9tEOv6h7w+W8&`IBePQK`S(8-`r'
        b'?4<wj73in0gh3NU`K%w!5{-4zfA|$&HtJywsIEj7EK%256pn!IA%O={>gh2#2VI4ZJ?N+X*F8wKy{$Aa?S^D4+BGJ2@?E8QLr)Kv'
        b'2}ykuLIHRaM+&=_L^h(m={MNNH}8%1v|n}oyrcS0<{90V#Fwkl#d~!93ex^e4^3I-SJ9FcMn_iU3Ke+hmaH$U>-~Prk`?Wq-Gib5'
        b'lqD<8qDpkUhuN|jhel~xnz*-^rk2N8vh<ds2@B6zB(lQ8e=o>pEc0dN=x#dMk+>MtUiJP$ZrbwvLf@+8G0)6$oW~s!Q$(@0FwsUA'
        b'qm{~^1;MT@1V?bq=7M}>p(@b>a=8SZTH#oV4j^}b+wE9BL0ygoe5)E1BPYoGtCAxNdi-RxHdWrS5(shbbqs^Lc8>6YmbLW9^~v(R'
        b'FWMjNLFcriV1^zwzj|epg#K8|$+e;Jw7mFxh5d&vKbhvxP9BzE33B(n?(k{EchG;QvfGgqTm4zUhtm;$jhy{(GnBGl?ehCZ9g>gA'
        b'eD`emlx_d!k>4P{yZ$UwUB)LaE-xc0|1_F1n?~oKOW#Do{Es|VX}?D2R_^*1?W@5#sz*c2<R0x|vH0*(A{L#)h`jB#X*b%2f9OzE'
        b'PQPi5xrOdqG;N?|TcXXi?{w?+8(Jf6>GUjmVUw)Khbwk(SL}R>-?{Xm;e*OUo<sF$JCGdPK28KBSIMdE3JhO_Z9mr$mmhhLj$%{v'
        b'z)<K+b{v0`;4XIky6!rk!~LOqp*ui)#AWoXsO1UlneH-<{m?VMhvVpknu9FxzIbm8o?^jMhl`cZrmFBr5|^zfu;EvgDl?t>`L<Nj'
        b'tiWR9iwKOw>1T_u+3`!I@Tl0f8PmpRp#=?e>W>~LgS{I6w^$`63u2ptm_CRRL5vGxOt7@BfWH1W-CXVuT{a@<!k$B@SctJAPAW~9'
        b'9<4@K(oq=NexPQE=jb3UtHd!#({t!et`tDvxhC>&v3OHt0)48^>r`KNMrWC$mYS7CX4QIg49jkCKi?&uNUOfiMQ7nrOL1ipu3C@B'
        b'#9k%Z9!0HH;o}%v{BXU}SLa%qOC?_=D(8XOOq2LH%o6X;?H<ln=GJB9QUTdVfE}oWP5>hn5ClNg+rEeD-y{?0nvc*;oMk?l+m0$M'
        b'_Yjpcz@Q$d!4)hnN2^5bE^<B=ah0%+<<pSwHg<C_bmf|PJ_le!4P-V(CjcNsMt=&0Q4mRAg~7G{7jiM7>pFUkwHZC5rDq(5w$3oL'
        b'Wo)P5u@H+tC;dwZlJqIMU-|*s)U^n~2mn=7qC30Lt8Mfy>tT2<4R6T#YY1BwgbGaJrWt8#2(tz&n?o6&lTu7YV&Z%vAw3hq@L**}'
        b'i07D$A4vke8LPDuy^(f=5RJ8pxA6H}^cH8d`%#1o=uUktX~7fL_Per~gcMgcdnB&gVg@woX=-7uwtaj{M3)AS_6*`ZvbX3Q*0!O6'
        b'dQ-M>YqFwhOCCF%qbzLE=YEizrJ}G&he!p+MCrB+p~GlUEN2lm?-~|AK+;O^dPsA$_AMicM~h2obcW>aCR`xXpeE9c3Fax<>7?O8'
        b'7oBa%lJi-Lk*CM;zExUboc3vSS*2g2WDhawZ4v0oP>quN^6auzat|L>SK3XZtGZXOl3O74d^i0Ph)+L15gn_Rv%zm?ec9{+iTJX('
        b'8#D)ni4daHt8jNAk}4y2Ng7?og|_sa6W7=9%DVsRqLKR18phF4&>rip5T<RoZ5<4s_gve0mX`S^cJF*v31rN=3fL;fb=%}}6?obo'
        b'np)L}Zl+F&t4dKA^(mXhbD!Oq{ZCyEiA|jsuih79b0sEiBCJnfw9M-x6}yqR2prmnPNP;}PF*)T3sx<zXhfrnPpYb(_(4ivQVLPI'
        b'0LvmU4GH6mvsAp1AV@O~0t{^yG!tkSi!t74CXE!Pr^Hy{V;HN6KdL;yk!GpJjH%3&(JXQIofUmmpmoZo3!0*Gp@czY!QI_w#l=oi'
        b'6^@}zP<XBpmyj01Xu;4DObQP#pln-=>JM-P!^9s@0%VmLbGM>Tf$WUpr+R?NA()u^lkf{7D-1I_7s0m>Ky)f-K1GCKR_3BI0gn7<'
        b'm<?kvHSlRJ`t+#b0Eb}i55K^T;tP{13=@Z@(phy+o_&+txOJYwn4UMwx#}z_PqxhtimQf`hBqr+0hjAlmr8+=GD;&u{Db74;Zk@R'
        b'GNuV?7GeHV!;`NWDas@UT!EwiHzZb`6@7RSiDKgd9PZ~xgvM9K(1^MWv`*z(8xXHklCVyZwuGSVM>*)KpTo!cS~k{K^vxX9rTh3>'
        b'JBB}v_yQ0sJsct_X&99Cc<2Gzeu4Gx|HoL2;cdkj-X4sF^a#5DpmzLO_pP)3i}=-v-ACfi_Q>bZubO^fc$v*2e@l?jbZ%D{WqUYi'
        b'n;Nt&3U<mjRvQ$D_B(PgRj~RV79HHbRBo^78V)K~hEx+UGBO#%<$EvhKR<!YNzml5p7y)mlf#G)3b3FiCxOgit-(-%G6=6#@O&#2'
        b'Si=U^B%sp_!uLmfa|T_&9@7onW$r$kUh)t<f8F&nH2J(lk+;kt5mrqrTNP*d^sb^LzfHUafVP(P;);^h4udD+t<}rtxNFanl4M(4'
        b'uzFwZvt7fL=&lHr3=`wgiDY(MIIKT1#pqu(4d6IF8_xgfPTO~=es}*Fn=Ghadaw3L^x>W=(BjZ;bd?4+y9GBloV7$_7AIGoh{T4t'
        b'*Hy!HpKZXMpPX?J^&@jh9>nQ+F!d4=O(+PLz<qbt!f`y2wy>5rPvM$T=U$f5*}RjrMFr_NMfPx_lC5=N(I)Ibo&T9QFQ-{>5zX=*'
        b'Id+zeNcJiwqvY?g+9PLdsll)kwr<60XLX55U2BVt-RnZvUHs_`2zYO5yvI3BWlkH8#B{X>PuA``gQh)D(WxG8nhH-tisfubgR|Zi'
        b'8^-49QbBTP%<R~)I!y37$6=I7FJ39n-q>;7$(5ZL&VS;jyY>tn1=tbic8JQqhAhq`^=68c79Tl(c5ESi^BGa8b3plxsY=~OGGYRT'
        b'>r~Q`2Z#2kq^rYB56`+J6+weGz}P*!Gl^IKvCOxMO`{5Z#q8?M*YcE;@(P`)g&gN_CejjzlXp0^j<yug+0(#tOg{4bS$~UZ<mvJ5'
        b'(zA8Xo@tf6RXhJIErF^FebjYMqbR|orfa3O5v$kHGS4&90xdQeQr9~!QjV=2Br45V5>G(8ueX@C9flt=7u$9i-UV9pP$;0o!iRAK'
        b'HoeZNtxg@_)LnH(49BGbN})#{w0dc3E2l#%L*oHZf$R4!j|_9=vEGw+^Z$6uz3Pl7W%}L>7*qI~ZDj#AGU7xSP<vY<=I7XY!MHB='
        b'Y!iMEhyFMgD2kg1I>)mBEMj`3g>GTaUgwg79j#8bgeRm=VQ%die+p7@etV{`W`pm*hLUK)%3<5(C5aIgxAj$eUlr37X?+Oj`N%tG'
        b'ZHl0EW9Z1iv)5Z}z{9#f0nJpdN9VXZHHFT^%7##hh=u^5;T>y}xHdk=b%5QtZ3bxhWhukEl&vlLJ)a;9DX^M9xsFUYqlv^oBCzCh'
        b'Fu2fn_!{VM-Zf-thz+PY%50arUSdm+GxQ{S0zIzz&JNS1&0S}iPrj=;r1$M({7!y}^pkk=#WNl*S-+dvmYtK>Kw6yIiW~ZDedz{<'
        b'POMq9qxPH5Cd!+d2-pX521K_yd3s@>rGTDXF^cYxNo{{vvHOJNp`FVT5ZO*NVV!lrV$FF>&DrMb98b%df4{@y<O8Sgy8r8pm*X8d'
        b'igz!za_n_ZTb1VJl3c%UcDW0-9E|7AcGf+0mgl4BJD~gBPa<KdeTlS6LfFW8+I{%UbuJZM*qx%hwu#yMRqgT4lGxPNRApV@Oj869'
        b'$S@6bKlO<HtUpyK{#Z)KYjwA6u9^9}zLZV|lrCGXaHK}nWuFcB(0y==CCehl+XJ0-rn3%hRKOR3e3`?Yv|`OozmFJ}BGQzu!u(p%'
        b'lvx9&Oh&;W@TN7sw;7*rL-nCT^p&hme-_F*x152N6(&XHm)vk@m36;61NMsq)7I1WJ)O=!b}ql^S9gJEfIJxL%EcJXuS+@WJa<On'
        b'aPRH3t={b5fD%$XPL{TU7|r|lbqQyIQ(oLeMgX0rtlQcNJnC<;ZQH{JSQuz;a(tN&M@PSu*OiuT00t3nbO3Guw%F!A*zT_Ew51?{'
        b'vk{Y5+%DauFU@0Ywhbzr#h6@`na$t$^Ip=t9=dBuOl**XS++!Kaq`YhokpCsC588gD%8IPkcoxuq5O<q^*#wmm8q$X7A05Mnai91'
        b'qZ6c-Ejqkq@DXPLG;xt7DUqH^$6_BIZy*6Cd;n#J7b;tJoyj#bh{A39eJq(Bt$jSC9@xi2afNv2bU>Wd*X{}#W}QLH;IiZ(K6ui`'
        b'&S3d08y!{o>L?v$4FGE-e}xV@2jtUlNPS^@u!-Qh&Q!l9&iH3^{&LrcJ)@J=Z}7x)TYT8gH7`QV+O4xc(5>_PLbkuK+ew-pl6UO#'
        b'`bKx|d3u_xG7^heqw9;;PTkYETZwKkB1lD)C~6g|NSstC#Z~4qnxLbl60Cuq)ZucQ1E*Q*521)J=t;cZV9w79HIQuthIZ?`RX1`g'
        b'q<(f(bQXJYzhsU*w$taMJX&>=cuR>k#qY!R$D!+%#e2s$=npZUd=t<n(kfa;N54sKd1L(C7sU(U(NPKd4cjC4lQ*hmOUV5@{x(LJ'
        b'RUmxW{hPIdHjGIUGo%2+3YrBC1X|D*=R#|M3jjE}!?NYIGe;`VG*H^~Q2xhv(*~^lWA{_tXdw0%t<oPfk1ZOe)VUIOPp8*M0a*)i'
        b'RE-hcbS*5W+`mKkHH>tWY)fd8do)blxz6xXtzr|Y4&p#}=sKB!QTKC5PS>qDBWR-Nsn8Tu<Pmc6H3Qb^{-jgT<aDn&1701SaQ{w7'
        b'bdvJtVtZ;&b$Bo0{>THK$b-Hr)*rdw8~HXo)Ksyx4V^C627jc@vycWE>se^Kf9GyfM_t|-PwE<=9(b{TSEAeB>6h(E-Xrl&>|Xuf'
        b'F<!8vh~$amJTjYWD^pX|Oiy&B?g-z%bflwp!5QzGc=yGQS}Q!{)Xs<Bh2n2+Z8rQaxPRACt>p|Y-yRw8#cg~ox;-*^ui_e-)JD4+'
        b'QYK%Ubm;VMnvmWL)1^D}OkMh!DjA=Pt5dLF?sKXW&Q#p?<l=4vysVCUaG$b=h$vq}Sd-vER+oAvA<~nJZTX03(_yvAXS&*zr#?EW'
        b'P=6blw5jN)s-=o5K*R?rzdH3%k3vGHbi5f*P#udrL?jR;y{NIO$dgOZQ#-bw+T9vS(V5L3ZT^_2Bb($?`KiaYe3aHoNG9!e4Jum+'
        b'X;%l^`Xny>IfRu|HPQs1OGruNhY^u<901{05?sWY6rwsxyzdBVpcmGN;G5)hBm#D2PireJpR^mGSnq@?u0ww-uZP0-u5rOmnoJ=C'
        b'JHCW?n)oEDOHi`L=3%4Kd9#xygyUa6YeX;n8XTRobE=9=id(Gyn)0-dx^$a8$G=SfW4cF)SA1c!QTi&zR>fAFGnuGs*-A*6AoV^g'
        b'PBQ7mRZ=c?gR2VulrEl~d~Kc#-Osv2Uip3KX}R^g@R%4bbb`&8L%ut+Yo^j<Y<2_v8kNHFyW5PG_PbT2dN~%pl@FS>V8;((`Z(Qb'
        b'GHuu;D@jdtpX}Tvqh(2{^SZWzQQHhk2pveUwJHZ)8!6sCv|Zj70ev5Pf9(HwPsgcWyc50+6ku;B5+Z40OD5g5OX+^Eb5GSSS&eu*'
        b'-|RZ9fgHJq&I>Y`ZWI)3*e>tT(Zb|wUb&QBk|wWd*t}Zz!$4iaV$dsF-964ox2^-RoWGMdM|kC!DaAbLqd+dkn<MM~*vb8|b2m<R'
        b'&=Zk?YNiCU%wm?86=Lqm=%Xrke{IS7hiFHSS;Cv8N4%Y_KAfpzwbw#|4_kcIr`dt7Fjrr=CCDh+quwDGWRiE+Ls8x=ff5YIUdvME'
        b'&Ii+clF_uuTxL;NEc8?!9EAMQ%5OuwOnPlL5@FTCOSAPxvtS<ghLL_1GAw4PV3yD~(*I1fod^}0>3980a3BnPT)IF=heE8ujD+7T'
        b'SD^|k&~Jz+BnmRjLiYGc{G{x*o1uAlhm=-dvy9cvqq?)kTe2ohHHPc%2tf;>`s%AMC9xXrNgmn^wN$o+t|cj-<N>?kJ3(z^(D3&T'
        b'(0sNhf@rOeD&8jOY=uEap9|KS-lAiqxwhgUX3i}jbc_ULGNkxR<%$>b0gR*TJ#S-;yO=E#B|t;PheGZwgxn<EV@UY@K&V$zXo=$Y'
        b'L`SX|^1wzUMD>d!uMw3$BW^+TF%m-z22+aoDCvU2xGI&)6<rd?j66<OA39LfzBJ`ffJC<$b89>JC@kM|hxd(2zXzG=#<xfCPW8(q'
        b';(&||f|DH<loqFocTTc!>>Mr9!inJ4$LaD&2^hR_TU%VN7f3TWDzSx5#+`tqwmGrG?~L+u@uo%krxhqhrAFEADIEv9U9agq&KM7;'
        b'TB4X!bwK8Ea_$M}Wh)moByo@H6c^vB{LTbj-T~w%1e}xIQk2`?Jw&-Bo#MQ)+V7k)C*uGaa6aS?b%<Xl^l+04IlcQ{N4Uhn&vhvW'
        b'h>w1B-$EHZ+(WJ06!%Z)x&8BL@_CB>AN^cZfQxotM|n%+Pb&^|2e_C{Vu*BqkFq-DLy88fN#g$ceu3}@Vu_J3p#C2bDDgx0@Pm(t'
        b'Cel49rl=vw$m4>0phMgx_ct{meF@{vbbx<hBgS^2RlbBNl0NCdh*M*$1Wu#EEhjp<PjrNzr^)@?_{N7>_h<i7Ln}(TKMjKxV#n|Q'
        b';wkRo(>%XWEl4bHVF7Nk$;kS-1Yy~D_s1RL{)~tGPMIIj@PYVItzl2c?Ut(?(+)fv0GxB`Oyx7^&{I&`r8=cQcD&FK0#kxL#QK+w'
        b'SK$oz(<ug*tBA2sPg^#MwShf}4#X)ExWWz%K3+T$L<fbN<PYvZa!)&r;&btWO&7!pzfpfMj*lI`tk5EGu`p5=PBpAi>N0eRDiQ<w'
        b'5)NO%@OXe=Y7CP2_%Qt9Yym7-6zjlr@Ufm}$ORa`Y&<r5;K1jm_k%_=<BmQpUMMzR@KHQBNnuQn(gV$=N9&*xsKL>~=;rH|1L>(G'
        b'7@OjPssbDXRiPG2#BWz&`Nq54-BT*)2NC2}cQE)$=n(hADLtn{J!9ltO2-nCj$xv}htz}*E<?-T@Hpf+nPXSKt_3_cMbsY;A#=^}'
        b'L<e-irV36<g5k!Jj#s`KnkH@A9Kz_pf&fuz2Nu#y%6322AvT@ybBO_`(w!To>8Ktq+V6}DI4Al!Ccr7(3pzx#@TQ`b8`s0d0Q&{F'
        b'i5{oc>r8T+!i28{M@Xa*SyQAtQ>2lH(Jz?uV*tgENOQ7#=6z`G-6Akl#Tc+@{|m6>a2uln&S(-(Mo42tI_eHMWA1}a0J3u@h_#C9'
        b'fakdO?t_E~ehLsE@1xw&;_H}j4g8zLLD|NwDIORwJ~?iRhhvlDpn<Akk8;~Pffi=lYv9I*BR=5N&%5U5R80{h4IvO%$?=5r?a-t='
        b'sXqk1&3H^QpwD8%<O1ER|IPr-^gG8vazrL*@OX4wQ<Tn#$7=9#P=HmTJ?QSgqmhS9C=B@+3A7s@?j?(_M7{j#^!;9<Ti7rZe@~!I'
        b'e@0Ug?ir_0U%oh9JMWY&Cuo}(1ZT>G%iX^^4Ng;d-?~i}Tq?zi2uwp^SrW{2A!zz6Xc`Wh{v0&<gG<fQB6EbwtkRgNEVG0(M~}P_'
        b'(n#?g6uwV_XAw9Gv(FLBw+2n;gQkyzrh`F^S#C5(?J&#snIp5z3UP62Xeo{r;i$X{R~hjr;FYCjy2w0^mNBOI+GD3}D}pA;a~m1!'
        b'Aj)umaN4#!XrsilzKj^;fY!jF{wy<NG-DbwUc55|z_M^g9gn*oK8-O!F<>O_#cvBuzQ&m3wZ*6V*V%RlYqE9i&ZG7NX499!t)BxB'
        b'u|rB|BS5SFT?l~KUJUjhX|D@#k$z4F#nziAXt#%o&?JqrcIjz0Uv4`XwCxE(%YCn}T#rwv{oU!R&zTj$9cY>;TK|k3+ZlwO0Vv-e'
        b'S2E883-aXX7%++0fm0zQTGE3U72F<SJsxr^PGR<-ZB4M?iCi~*8jX$EQ|o7;{&izb9SQz(LzkMzYhMK%jvs62(OT5b5!B9l544kp'
        b'Cb?5jms;frw+DjQj-c-kD{b3?(0+H(X=WibbR0C)1r7D0h61RuhGxs5A>nBsYyJI(N`h@~g1&9RNQylAMBNvsNHgXB;v||KJ#_MA'
        b'D(BA!>z=WLqaCqILPkW8W{LBylg~I~$5K*r&S^42COXYJnnD8jszDV&kt7k0_a9s*p5_BIN}3h!-y*n^R)MfQT4&l9)cyll1I-w)'
        b'jE;<;#>VssY|VZ$0#}j5)Dn>Exh3W;Cv7u>;?!2WC0P-%N~Xdk1<IhxEQwtu)8Ntq9w<?2#3k@-t~kl6<fuF@C(SZ4LaImZ{6q~d'
        b'GvYFakJsyUra%yCcOOEnIk?&qH6FamY}Vo!Z+`wHiAUTI0T68h@;CFCt+kfJuF^cEqC`D=92r3vacb9xXs(QuYa${eo{<<MC_NU>'
        b'GP!I3bya1?v};4^7v;q*gnEwL8#TV-Yu9eZ>lp7PD8C;w?Pk3e${WS_;K9Lop-;~cl^jOmgbJ56p+)3~1&EQ=A+=7r>%-V*P*e|b'
        b'*C#~Bi|(ta-T8X}z<4@d1cBhz)T{!aNot}p5hF>gi9jH*`l1jr-j_%#>q6oLD5b$8ng|dn;*b#a&QSiIA17aPcOal@-A(J=kOsyN'
        b'$5auK&=Mk7gG<DssCBG3EmZt(p?uv<DRPLQ9F&HlMqJ7eE5|B@l6tY^$djS`XKz%Z6DmDiBpE?^+Houn4L+K^qdm^Zkscrc8j%2t'
        b'NC2cy_|OfYLclU$7bD|U;oh()&V$wGht%KP0NnW-LT>z|Z#ScY5!=mzOaN4h0SzDniXlM2Dw+uRTtuaIX(<1jFQlJ^eI`%Tc<;e)'
        b'(E^#bqrnF!$r&EUc#md2X~8^&k?zawAXdezu;&Qp@Z>dV?ue5u>rQ!6a?u^R;@&!V7+Df>zk;xamNw}awS%CEO2D=Iqmu#IN9xz^'
        b'xqoi&UIky}&<WxVRrxFL($^<n8?oW)Irq}!^-JXSe^6+jQCPuVcVely`?-^%aUD7GCUF3#6~*;o|GEy#bQe@@0B7MD{MTHjbL%=G'
        b'dOSU`#>f^FyimqP3r~z6o{bKji;z5+zy%k3S2>VD$wWdr4I|CuQFj8}0CHXKeyd%aOp-TIWER#SsW*qzAIqwo!zIe$UCOF;dtTpd'
        b'h6ng(e|B{h_sOO(SkX${01&<J9^K<5&G_zGG+~V6-sth-yXUGnI$lw=l|vNy#Q6M_*aL2~G{aqm>NBiANfQ<lOa6m`Cvm}t>v=tz'
        b'>SQS?g-+SY!kVZC$w&sGm#`}V1SnCNNojXTe2KQm%ns$Bx+NZ4tif?r1PR;>`XQ{|phcd;qln9%7*FCj3}Co-#*lg-=-rpI)4Q}k'
        b'vE_yK1FHbBe~nac``JrT^pu(-=HX-dilN3v>e@TXu8$bsG4{Z!KsL4OQ2P@XkNkHXx>lB=zOM7tn){Co@7CAUP}g=Vy9St=H(75s'
        b'<t}IkvbDv96_PBxLqq#T$Qv=S`lLTm+OoWT*C7-qjl{hE0TL&7dSlT9Bw9Q{vSRqHHmjYCBtcwxBjTXVH9iVZDhiA+CdIyMlSAs2'
        b'KUCFL=Ky4N=GQ%mL~EiXKv7UfaUe23{;SF(fS1~mlitWk^)p|3I4Ph2#?ix3dv>C`%VmHKWW3~HRqN0|+xP55%Sj@!aHf_E<p+nY'
        b'KID60nYdwcyTwkFk#RItc4AcU5v4OXyN{!he3_g_0gcwLC!Uut*dw7e)5yu!>{0DP%$_Yp6AW|PTlSw6G`TRGC|+m2*<Pz?rzLcb'
        b'X(mfgQdA8eP#*H5iRsA1t!50@?KXVGA+_<Gp*3;Z!5dX(FGmJA;zYaxU3B<PoiC3C?c+T;Z29zV{?~WR(@t8bXiHX_nQt%eeTkO7'
        b'EcGM`)w|kpV9M}03Fz8m6;;s>f*U<9rR?9I@G1$9)>^ZVq9^TEBJ)wZ00kSt8BHN7lQ3QzRabU0JVTEYw1U@K8x)YJzCe%T6Ahga'
        b'P2;*6Sn=*`qdIU69;_`PZ=ykc@s`I)xnD+j@%piydx*Aykk>~Bd=futD}7_f&TWMC0xH?^%1QdQhKSvU;^TCcd6%J6-XwcjPET%-'
        b'0cGsM!PBvAQ~D>4uf5Y=bBJ*rVykff^6}R8&{4dBfI74hp(?Xl{@-*IS{_=&)E#W+wT$bi*eE|%e-mWNSMDd<#WV9T_X_loya!zY'
        b'&1)ERCB|gTtI_#2Q+FTtXr_5JX(`Hs=XQVLDVnh0sseRiI0=mgU^L;-T0z_r;d+K8*vQ}UWc4^lqG5;tM8F%!t4~yD|ACGC8*blm'
        b'f{*!Qc_A@!kp$$3AvF|ORZ)5aRk<mIpr|N1#l@p|E5DSIel<2HYyMSx6X~I_>J-H94MedDpC(twhdh+L;vk4-6q92;+47Neh1Q~|'
        b'S1ZtEa46p8Y-e3Jys8OXCQ1;mEh79RmY<9BODBw|Zu@l-5G(4H7~4n{KN&f;R$?B(nl^CkNrw+}IN%Srmq4?-mlZ0wCGCX-o&SVH'
        b'{YRPe`4gl>DK3<Fj&^Kh=9Ts0e8e2*znw@gEaNW_JQ0`gmHLxnfpiWk-4jlRgWT$s68Dz~-*un2^GQ(w@xBh;7eaNfe)Zrys*teJ'
        b'ih?4fGYTy>ZR{vb)DPg!vJ?4pCRmd6P?T1vZ`>6p7}|amC(Hiv|1kFM0Zkp*1Mtnw&4c8s31C3LHn|}X6}u2>L2I{y6cBBH5EZH0'
        b'-IZvNy6ygy+WJ_#n_OCml<s0|6{y|KO`D2TDhYx-6;LC!xK;bM?Uvd`t=nx`wQ3Q_ch0@Rx{vSse*Yx%JacB|%$ak}%$$q6tJ_6c'
        b'{~pFp-KAT1!p5iyGeum|0Gpul@#b~z(g2XWVIdJH537#xP&eHPcOgx?Hdg1kU4%z=Q*(@J5_`6d&sID@xn=V#2^v}ngf=843g5c{'
        b'!0mGpYsT<M#-{@d7*&pwte8a@C_pb`@rlg%WX-{=bSy2=w(dl;Izgn61KX~!V%o+ev*LWf$UZp0EX-fr4olk!bXO;;*{5ZTC3P7c'
        b'#fGQHYcpmm90l#g4}=wt+=z7?sy#QGLYqCY$87hWfR;=0C|Y6tJPgLb&tG`@>}!5frs*!7*mf1BrH5LTnw*?`FMYj93?pY1k9*QY'
        b'UTT1o4|vMy3jA=i?z-R2;Dp%U#Lno>onXlJL|ApFf=OqyPlagBzIT8QbLLJSbk8Suyf(n(PMQs*vEwfTeLo+dU+Hzbm36MyGKQ+u'
        b'jgDc5+Q#;>1Ig?nBC+eE*$RHYL3>*Gi0<V9n##<atozEJoV+og8PPchh8C*xm{lT>br+|Su=&1|Oep%c4-hq%yH^u)&z%y3B$TYz'
        b'US}4|R?Bt29zgA#nCZ0-5DPB<^R9u}%CoNE{K-n_=SJT<!H;&{+uPr(OiKF7lt~nJP|V=?eEfL37Izn^l1X}x|B^eAF=>G59|tKH'
        b'U}awl5-(2PvvK%!_nn=14m)A9ZG2e4E+%l*apD2G*0sp3WEL#U7`j)Thu@D)p4)3WnhZd9x7WW)P4qSC?^?IkJ{u=#&*di49*rSo'
        b'W21Y17_DSM1BzBAeY3lkqUCHJprdT`<%zO?6zaB%lRoJ5Ih6#Rw_@6FlUie6SWzc&Dn;x&B(3OCoKpNlLBCAj{iH(kHg)#x(;v;5'
        b'^KIAZJ=#6fV!ylCDr<X^nx9uOiP$lJ;KbZ(LwnRG-yR-RpBo%LfFu^{fc5chQ<G9U8g#yW_H${?7v;lU$;~~g!dqj5dGt)Qb!Z*E'
        b'Z&M(Mh-pRktzg_%=?Kp^io_Pz*h=#i2@&fld-sFkceQIPCH)eS`#3QC&y_DKf2n*`N$;lb(mY0422Za|yJuCqwmQ~)T(lxBs(O;L'
        b'Zm3;d^#Y9SI!DjsegzTR=)V^1nN&DC7+c5tQSTo-OG|ryTR!x8^63v%g-v6F_s>?sTon}g3HdqU!yeD5CchD;D+#-&;N}UzjbYLU'
        b'EB=Cq-P)PG;w(bR%n&0BC>TF6t4=6@&tnM9<6{pDKeJt4@NTGD_CHZ(L{C#hEaM`cQ6=!!2EsEL<Y^-0%I?h*tc&1nLulk<Tq44F'
        b'l(*|<Ts#3)1+9(YUz_0;{Bg4I&4J95B4t)JH3)3Euv}!Q5xHh+HNJ6soIk%+>$o|8CcX{19t`|UlyA^#8VSQ+!su}A%#b`+aV^N7'
        b'lVrsB-!UbZYxAj*{P>XwkeX52AyuM0=fG&CGZ~F(#uUJ`N5MUG0&f{*`}s=@Xk7z2lRY}BMbCIdnlo&HZe;rKi(&qM1Rs!R-xTPK'
        b'Yd=9N=|Q^=YuOJ1$DqUJ%I8MUHO@_+n>)9tCoJ>87xZ19hs|$^d)iGB#Z4#Z|5>-SUq%cMs`e}y+M=%C4U(Mm?bG%3u}op-n3N`n'
        b'D<}O6{-9dFe&dt$`rqz+R;tlZWhdVYMY^-gPVNtd_gA?7x^w@0V{UqpHdSjx&#guy{zT)C9DZiYFGPrVQ8r=L`s?@8-M>hPeI&N)'
        b')k*%Zf<(z;^oV?YF)3w;l3!dZJNd?`N$dYw{w#fJlIySKy_>X}w6Wc(r|abYE5ZJTM^0|(ciA`1?*&{6_ueXNcxh{0U6J(LAjHQe'
        b't-n=1yndsyP9qzk5A9BSr7pK306F^$Wj|^@xw$#Fc>RgfCzhV{U!jRplS-nL14U0x>g|o}U0Z%idh*@f-K77MU|o8}$HBtj54&4Y'
        b'Ua2!mKL`?qQ-0XpLROp&)<tKZ3Eflt)d?B}1IIM@X$Y%~nOrp^)?u^V%aC$N**<OJ>~i`4vD}jXW4X)|w2**5VLKi;aYtnC9g&Ih'
        b'X;8i?tUWC8mGJgO)t`dATeTgJt*RI~HGMeN;e0!?B>fAT1U|x-pLM&useRG@Plt@^Di+GyX4>40ct{BfqgeOoae5jPUJv^oE!S?}'
        b'X`3MU+whLiBrqIaMwxaZBkDx0n299P!?vB%maDbN@7q$fj%lt`mCa5ee@@jVIc%&dscLWSq-~cW9j`{|wa^3OqK3IBLPQc;hJtkk'
        b'Tp8(|JVA%Os4&eW5_c{&&7?H%QA0D-HH?ivsZF`%cSaEKoAyn@ev?C78Gg5WZ|~kPMc)m-TP_EkCu@p*)^Xt8Mi6ahpgQUh(_*c$'
        b'myXt^m!k|HTjxF*Su*!kI`sY<`*Fd4)+KjG5T`p;g|YH}7ukDK<#dU9U)j0seL)ji(5R|u)apL>yO$CTB&(nnI8-RO<xv@vju$3L'
        b'PCHa-rRi*B{fg3zzW4oZg`8gOxqk{9f!2L|0#lEECa}g*BAx7=sdkI0CvMsVYyU!ufr=J6M<2IO_J_`!iJa0)ef<c@kTykgatuH@'
        b'4}1X<BM;$;n~a!(Ibs%4(qSC8f;NBg<zo#Jr=~tLMy$1Mgq?Q5A{8B8D4(*xSf0`3hk<7!3EzQRL%h!md`Y~F(0nzCQBaANJcc6J'
        b'0~Zlu7NPs}n494>2QB4}BtS_M@LUFBv&(fY@tnftrWhAVN4t#WF1H${kZpJn>bl%m$SCne5`8=UZc^UdmSvbVrMuAyCHD5(wyS8;'
        b'?GoAC<;_+2p2Ss$FLl^uFxL{B_L|l}IV4Z~XqMv>!y5iMAd^cm8h&h!AG4o0j)GhyvEsaJTL7K4FT+^!9WKsHTGKKZJzBniEw^bm'
        b';)nW-F?560p_(l&sg>2dOwpM&`f?Zttv1Wq@SqFYnHUOK{kTR}``KwkT4@yUdYG+8iJVJv#-$R%I4`=FU~us3({{;mhKU0m28h^y'
        b'6YG9X!l2KVYD!f9T;`|A_9<=mli5Ef7T6-417mblO=3ALCGNRn3F%Kd&ynmj`G%t7>tRA4l@Gn6{xZwoS&fVLk4`yd%9ZmU&rNyI'
        b'zwIMa1hKwO1&Rg=GIiQ*EqHEThfX{eWa7KFEVZ^ywV+P>iQJh>J(~V_Zo+h3$!z>oCKD~DBcvb*fBIvn!H<uvcWC|Rf$$+uc;Z|n'
        b'W@fT+d~hABOZ2Dc{mi;-U4oyEWY#U#8T_<_S(m4ahtwP$=H(j2+GY4r#zE8R`0{GDb8u)-ee$pUtBKgIjw!Iwmdui*#Q06?7U6h7'
        b'JEqqO|JM_1O#vfAQx=!pv2cHFL+UECmOnH(=8O=t(e<<vb)spuj-9h5dt((wG2Y0T!2u=2W|@vgmfSlK;(aNmW2}C0b#4hG5f+SF'
        b'j}&VkJ8r8|*=*Me8^)b_cEy&j>1n{lTpR`DkQnnJqetyG8-xwKXLR*=#`I(FnDQkf1;%3$Vj|x#!f)SNcYMMEFA5s=mB;Wj2exVv'
        b'p$Z?leHRn9?aX6CX-<kiLw-Om{XWz`H#4oe(LN6;6~CZsndW9<Ku_~z-f&xDCUF1oxG}Y8X(kh!Gj*Yunyja$5QHLvngo(S=!U0i'
        b'go%%h$f7MSBJpKCqbCzzmaKY1Ysga=mlmb6Ox(jH9Y)7gzMNAXwrJ_};n@;16YJ2gsHK{ufgFXNoFpb`yhf&q5tEZs$ti?NA*SeL'
        b'QJ!!OmLNyOne@XXe#xLe`!fHX99l1@F_(yr;H#+Aicon%D$b=JmebQB<g{2mX|^0+{^!0&)W63X<D`E>+P8DZjq-{9{rR{tVzgi9'
        b'Kbllw4p%-ZHi|R*MW<f}F4{ZP2){P?wZD55?a~pNlhRBVk-07|ajMe0<2bkDxP1`EJU4<S6C)q7|M7SaX=~8-yNvcBtf7157#kl~'
        b'lxZ|S+Bl=LP%blyeaD_S?Sw_pJ5;BhSqDG;u8rmc(VxpJeF?^h8L2b$GnT?qow1M(pFW(}_A=}GG1IjsF<nHzzJTeSA<q6N*c4VR'
        b'U%9{W^?k}GC)wP+t|xY`dwpMQtfPMr^p%ZxR&O{TH0lwGzCmwHO|1W};u7{-xB7Sk<1kgms0>5FTBgCw&WPJvC)#e_&Ior<esSEG'
        b'9vT;W(Q%{Ek)Bvff-D<K(=9#jU}{Y;j=IXDmD5DV0pWg${bAULp>(c|>BWt>d^U_O&@3BHi^=em+~aF6Nmz2prqURei3Xm^8r49q'
        b'L;TArG;1#m1EJR$PRkxoWb{fR{G3jITyW5e-@SP4nDD7ZynRcK@H9*ij@R_0nt_3dj>-8ZO0YKqo#-Nu6Vc~Tq2ufF={=ARVk+R1'
        b'qCXDQ=}4^%|9QsU$3Y4Pl?o8C{t%oH(4qK!_(>O1CC;2AK-FhXf{|qPVpvIuwS&5;$0IW3046<^juyUhi65h#KCBYW<iD|cpGZ^?'
        b'cD&#9MD83~*+kiYg@h1Sy|~4FY>9m)Mv9(_qaR&kj!^ZG=4HyFo$h1WM>m?qj5%v+QHyy^OwnuRHPh^OV^K>aT`>Dt)CIEO#<5b#'
        b'=Bba{OASSHw(NM+TM%>faqe>oeS((KOSU@EoH!|7IY@|R_7_K<Esj9#;b+NgU-H&kwokh+Y-??8*w%wJ^}YSN$g{c#&0MDD%T?bf'
        b'8?uP7lfK#ULyb@E%Yr)2;&7q9JqO!o`&3)op~gPtmmeRaW1PBhB5ncE$hlk_eUk}*^I_O@*DG4*BZR9&d-l{&*@@9Y`o@M+$I4_x'
        b'Syp6Oyhd|E*}g(7qlR8kS8)whec$#scfstdI=czQ$@X{no7ZZ4(ox<3uEG<r@EH4WzgQ;DH;$+TUp>Wyea*238D2I;pS=<2v-fVH'
        b'M#RLlk<uc<y(Ws)sr4dN6%#=cy1(^n)%;sO!B4*#=og_dcR-o^?@%goiG5KKRFqi8Ke)*uYqMzCY}uwdvZ8{}_4IFf&B-j;(o(tQ'
        b'e>Sg4irG|^TXt6DmQ7!)cyQYd*QVrEYgL+EQ|!I{t5$6+>r>^+M+$fGr_APLP{L*QEB(+OXjk7IwSSMnePWp5^(9)%G8#SI7=rF%'
        b')xK*ObOno_IkxZXeCY_lp|gqP5qo2Q1V1Xk_LU`|Ub+nip7BSdW`x^6?VsTN5d!Z|6@?4zALaz#K3uqEj-<s|YMFIgO7SsqR(NTu'
        b'Nl&I}$SCU{bT9S8(wYIOs_YbE+mEig<eFDh72AW{i~T?Xb;_-^`@*s-gW{|x-uH?)N5nsEla)v!WCZAstBNxgZ^}LvEN(n%k;*li'
        b'tGj<B{U?LPOOAos$eZs_ZOry#T`{pDKxY3f7y%<JnkmKiRs|dTiyu4&TN{0peh3<zw;90drLuV&ROCvSM2mmabaXT#hfppr42-3u'
        b'9TUEA{S2YdSrKz7Dnqc#PJBZ6snjf$DUycmJ@LIY3trb64h40I$6%7hq&#%D<{kpqIi(V3O|0{*Nl*pWcG_23vrbZ)@u<0IL;9IV'
        b'%ZmCQ&wP|DEiU?UZg~1XAGe_UrUKP5<3ls%Ad7v-^I{NrHNhXrMR>x3O`^ba!IY<uB3<c62r?$ceH8EYpiioq5gFk~4=KrFQWPNy'
        b'*Zt-w3<As>@Hprw6o4tks|9OuK6Ur><ExH|y*zt&5IXCBIf%UGbm;ykdDQJ{XmsrO{%C`|J$heQ190t*Y5QhupUd;~9T$#r|2S%#'
        b'>zGk#ngaY;%jjGzYYc<n^kL97FwU?_#(ztIhjz-phS@(p>NJwhQi&tIavJIRLy(7cn|q@a^xjea_C*+fzBfsn8y46X)XXFTx1cO{'
        b'_9(r-hqPb9PJjZ2c%C>~)R6eHytbW=OsfNaNmERz!c?lXz7edBvEB@(MD#np(iDv+PNirC+RR@cWAu{&9gu-4uJSru#)<ygteWjw'
        b'jSu9N0UNuTaVfNpr#^csecA5X1SWC{|4zB`ytsW?Lzd?zAObstHgz>^)}}tSyOuI8OAG&aiDG-!+-3GJc+{@&aB1ayyw-iS5BoLJ'
        b'ziot-|DDZb3=P*EE4jx0?H0$@CvMpslHOW18$LOt8<{6N6&-Xet*Cjk+}9L*RRQVi8`XH1_|4#|I&^>}6chHy6mOqfKL?~fTc^H6'
        b'N&06K&UdcUar7je<7mxi<)>>lI>^Ef;_N$DPwy$O`9!PvMqI_Bg;eGyWz{E>ax3eNK79)J>`}u**HX^(({lI1%PIc8?PR*1&6MG{'
        b'<H^FOC|WL!APBm?;(E~ejvWBMI%)9Pv+vvlpqem|=F*tbv7Mv=v?*8SzY-k0nefg#vFUTkD%PDVtN0H6D!IoiTmJ4OWl0O^=(M_~'
        b')7WWp+f&J*{*a;mJa&{76Pk1a?J0H!N3(Dp>~{Ua>xoU5F2IO>k0Z*ugL~6Iw!hx*lz+WvuA^b_ruUJf^n5gDs<E1;^HvYpB(^WZ'
        b'2pwJlny!6vKVMN-S+yVSq)0!xP@gEQ6R~npVY(>rbWn4Sus_zvE$L^CDtZ<#SmPf5^M3w>C0uiMdd9Lo?#q5AKAgsrqhBgCjd6UQ'
        b'I!U^UQNhL;^`cZ;xszQ;tqqTKiwSGiSd+{kmNW6wo1{?VNm>5-jgXR{tj=cQpM;cr+eT&pugkVEQ<#D4uo~zvZGCx-cH@2vegszn'
        b'jd92Nd+^w%WH+Ak#%Xkq^{w4aX6Fz_6CDF7&VlcHNOs`cn$B|D%yR84EmSKsj|!M+uIMuo`nV{>+Q-xWY=x$iNs`d={FN#?s!5)|'
        b'cPA*}_{{)Vtnsni@lLZtv_t~g`IY7DLV|V=1|Va$1TreuQRan2TzH{05BqoD7+`GpL1vDh4g&g+gedgo3LRtk3-bH{aCRKRh01H!'
        b'DRr~^+%B47#CRd}^L|=t$)q;${}#dmB1`;zmK;Q~_;Mc;uTE0(!<Hly`a(yqhfxj#c@VJL9iAXS)t&BV!U-3n`Yh7~gSDl<2M;Bu'
        b'4;xK!ii!Xbpio(62?vODEDzE9biX^^WGxq4-wD!+z?EzM3qgXG@^3YWobzOMD%P?@Q0##(Y$Yl-VhTo=Qe_K8=7kFLLTxeCf3Z};'
        b'YU0_YQ(z!yIh%daY8bOX-=$d99YMJosKLvY__@`)AgMaf5}zhyAyoVvk4gY(5!Y!-A`MT3xfhDv;yNp(q+_g`u3PU9dY%Xiyb<*F'
        b'^>N4h0#_8CHP>l{we-5-)VO^mu7i>orA1t8@&5p_LEC+CFd9pwXt#Kca#_nk6M9HqaJDyYUC|tv7nw!rO~*dtUEZg}CoFPzd<q_|'
        b'ttLOR;2E38KpwJ?hIQhL7Sglq2kv+MF1HHUujhZ|$iauMF=DOk{KJ8sam`kW(NmdviP`niihBIY=H6D)pG;U>JJv#U4zah5lo}yg'
        b'gVA{ey({rPGJ75*46I^S2Rg<Jw~pe;abR!IEY{MQ+U2T3Lqwo+{9#y6;qC)L&+_Y~E6ZH37&S)IrkBX<UlKWo@YsrV)m1|DR}iR&'
        b'fb?gCy}p+<#%PK_EJo%#i}0)n(_H?$+hsGXkq5SgHAxL0T(cI26~+X66c!+k<$W**E=HRTLWjlWTpN>OaqV0iLrOmk#xnl*gBI7W'
        b'wK2xE^JZFHyVu6RZ|$naUb@hgU0!i2_$HG*h_-|N>)9uRN=Ev2aDKf1L=dzokVE2L!iy)cJ!Bsb(r&!H$GTnxEMZ_O50cV*Ao}OZ'
        b'NHn$5kqee5XA{JmOr|R=@m}m%rfXmUv)a=LLr~Z`49rXF*(TfbfqkeKr@3?Lwh?RAbw&ZRs9?l#g(f+ypoMWTBT*J)37&o9FDf)A'
        b'6$QWU%b3;6NRrB2uFUsIiz|9lExIRgy13oZq%@7N$M>=yldL=@s`OF&+X%dHD@9M!+Sk-Ll5IA$S#JBJ2ECzb{gbex6(0tPSVsB*'
        b'bk~pX+@XKc_o08;?+4NKLB-#Kbk+hW{3+zwTM^*es<%8YK&No#O|v9PyI|vr$jBygyC^XKy6&D{hsb!o+SDY+r*iwSIO7^kRFGCn'
        b'SSBnYGVvwopJ;+_;6cMA7)L5bR@!KP6^jp^+;&sTqq^-Iv|rn6g*Goq&j)uz^*U$7XnwrGpSSxz4{Dr;%<=b?xzs@ausL}CswkM;'
        b'3!MT6R5VAscPAukq^<t<$9Xx$$^}!7_U^B;m-Bdu$%hrACe1Q};Y5j4gzjc9LlV_)owSc3zb<5mK=lv*9p&l6>`5C<I$a{0bEk8m'
        b'q~vmp{k6UwulJ!fuasaG5loR-*MEdz?n54U<OnM!HAO$d-dA|@CM%X`jD&#=;?k^_+gI@fa4u3Xx}{xKvW&_r@8e#>bbHeg*0?0C'
        b'lni*J)|Z3Aoq8g}*_+aM#7)(fbWWm4CaczPM1fb92*R!Bneb(NBuqC3dK9{oN9dCRFJ`FvJ^jFVYGpKO)=%dz0C?$MCaa!v^fG!C'
        b'qFUBh{8S$;qb24{Y71GGO_Z6%f(TNgz)ug90lmeL{$D_VD6<ekfeoF#P~4nz**=@^%gMnqy^4FP*XObg$%yRlg928S>muDQwdbHh'
        b'=Q-kbsQ@YeC%l8wjYrJk^((B?gkl%hspxYCpF+3iNZd-J$&WIt_03V&I<01=2wjmjD|9adfJu<|HojG59@#LxZ~b!Brk5AE_57i}'
        b'$R2~t(@eFmP$V%hOm4LRd+$0qth+0+>~1`krvq;)bS!|9Augz!K$ZIaQ_akh71jvc^@e4-t&mS*{#(I`;gwxJZ@+Q`8*th48&%aK'
        b'W~!F<CB8h!&jmgRx4cJMzm-`ua<famLaMi%6<MUqWEWzD`cNlr-DGZ7uUW71xfbAi%nyTZs;+R|SHAEw%<BYtVZHS=7ujc@iv94{'
        b'1c|u4o9d%CtT<AZxKMNAg8f&$ZhfXtei_GiH>{tN*FmZbv%OMYW81iy9Ng?Yd9~(+a!s^m@CHjts~h%4%gZvQ71h{Bcc#?vZt$}h'
        b'+%qF7Izp?bfU<d${AO}%nK?%WvfGA-dS#_Dx}D9r>=)q!u+buzU^bG_lujv=5`~+R0*@mFdrk%i^U5fq@W#jn@`yQ0RF=3T?II~H'
        b'3wpLnE7s%Zp<VGHXrmbVX|HF`RX0F!&91C(p-%>OD(uV=dMj(ha}4PvDEwH*?plp~IuQM=>W{g1k({7{@CiNp%Q)sNr?WMxG<g(C'
        b'n?;p%X)GxpjozMN|0Cu)IT5R)b}Mvl+1Ic<0eidRNDcpnk2PkvbH3IzT*bCdfhbTb9SE|r%k(tczH-PftRmQfk0Gqt`cKZ=>v;)L'
        b')pQP<Go{&m*#3?ihuyNvwKKM70Pk^Ru$k0$^ifq(MONHTB+27`T)%ziUL(jA!KB*CdQzH9>^0sGGI-3YBu8b;6HfOy>k@66OXfeX'
        b'wbf84AOC$qEg)I<_@;KUB0d;fxgF-fog=Hz1s`j#jEQGme?VY*Vt#vNeJ9k4x^$2wscmy7?$%_-5JaJD1aj!@0<em&gF>uURk-CQ'
        b'y_k+e2W5N8d+Su&K1W+j9d~-7;lkfsck0=i9g^O+lecX-J&4Bzy#v~QGl@=508C;jS#dguEk258Gno{Q9igc_tlYFkpq4UH2FqWw'
        b'wg&*wQ2=UvU2+eZw1<B9yi0z%PF<#yorrp3)BGqHi>Npli>O(#U65FqGoF13-7Z1TqE<m?cVDzG?fu>FDtCWT7ETUr(w3P?|26E&'
        b'&}LQP-qF)HRdmeo-kmNNwe6$fM)i7!$|dyS`;l#%)=%^Z=?Ln7R9ROBNEg{Qsmd}b|M?)K(Z))Ub|E!w{bm)NYulvFz8M6pc25TK'
        b'1Zk@5syUmGE`mMh)?uKMGETQiF=fNn!){ktSt5yR?M9H`%SnGg{S@hcZqQmE#FO>QMBu=9p(1Gi7V9QdT@2Yd4ZX?9_YS7=7d~XG'
        b'!)oQuFv6Kh@XvA=JN!38cJ*Z2wH>j&H@=$0-FtY+!X-=G=Scd+!6N+1Emkaz@P!cx?@T)JO1LjZ{*jV0A&A&In?1w-L(rE=Oz7hF'
        b'_``G<r|5MSIrwLheA?ZIIVp%yDHBI;kmdk&;?i}aLO1m=!<1@gNI;tI*CtZgp*Nx#;fD)Gj<E45O?du*|D^CQ+|H|Boe4>J)hYC*'
        b'86Sz6iiyB*Fsa`s5;1v1Y@=Z~=o68A(E2?D#eC579siaE@w#v%A#>JsbCms?BMA&+|MJLnQ=I*aBMIRe`)5a_6k#7alE5lxM`C&y'
        b'B$Sk0LL;&L(<2GKAL4$rpF6TU{2%^np?f_f-g)r!jD=vQbRNkM=j|t=nUG=V<}*Tf);{fNBB3k%8Ae!Ix*WpX+sHroPFXv~Ci(?s'
        b'PxqMPQ#9fz?${CF)NYb6#itOBdc&bHeAIm8h?yS;3BHYmAotc0jRQ)NP$Y104ALj^9VQ4h7(FeR$oY<#UE9oggqaMp?>|y)P4d_q'
        b'kC^jBMJDr9X_{5`*c@{%@FO7}WtA;?=#F>}#E(zJoe+OqX*Q^;moJ$LiLnm8%vyjUxuebssPpn2@l6m9+!3#Y@`gL&i4eEmjvLef'
        b'eK`*u@y;di3SO=VdW2)bgaSn-u|!tz$DaJDf~D<e6MZi-(XkCy7`VV*95rs^5eP%TXoCNSGM`IieFHNX7{K2i;jb@FABLfZLG-xz'
        b'@p?Q|qaj@Q=Sq%1VZ5XQbEGwEb-y}-r!1KSKHWrRCT#D$qUpnh2gRClvE6x?l`Hn&6iW#De&Jo5^)F*RiYC&Yg^M-td6=?s??Hw4'
        b'kt2|_0Fz>~vcC(W-?Xad>H8bx*;jGB|B@_T)T7Hfg15&)4Ou=E1wIkl`j*=Bm3<Soq=}Z;V~#*;!uJ*F#X_4>3DI_M8Y`WiQ<MUb'
        b'ZO_}>M#AS3dv*!9=&)hK2O(T$AuiKHxLgR~A_kF=IzlfN081|mw2yq~OqlLxJ@%r*unv@sLo?NA&R$ZT$6MO|0l&1I4kwK7@oNLx'
        b'1Yz0mr!iNjmQx+ElZW|tfx^1^7D4bv(V0FMJ_Yeq^W~&R>^FPxs^m=V#5$_AI2h+bqSm}U!ns=7U~-a_&7t<4{2n;5(}nk9h<eyi'
        b'wC$POpQ?WIh1cwt5C9&0_!i2M(V%@$Px$ntb3oMWP}hm8x|&GqNHD}x96ov)t+c(e)0sguk%yuqeBsef*XEiomF6A7d-3ook@aB-'
        b'BZ8%hazX}?JsRZi*>j&BKHH}{-<M41&Mi1aE-HR>!{hcXJ3di=BigQ;t%&<m(n9562@P|$xc${hhYrXpe?}&^XkVS&S?7Fv)DiZu'
        b'!YL=3C}$Rsdu&!=Snx$9e|?LmHSNZfce-KtGWDjwGh=6t9rhkS>^iA+yTsO;LEszdS81i&wT8D(Kp$Wd=V7niCq?#?-Tc$fJ(qh('
        b'y9X1!zQawFVar|5DrgNY89dZP*}v+UVA9^^!%Z^#3XE&cNpx>@bNdcEnH0Q&&ZKaShlK#JV`nj8`0ZG&D3tRTK1W7qwqtbtUM)m5'
        b'M@1}T{TU~^Nm|CF7=AMb`x*BNF#i-Zmi*~3ngG_{Wj-z%E>XL-3i=+uPt=MVjO{b*b9zEVLhyHSJvXQ)6-{EpW)m%;Ba<K6xliqS'
        b't#`qKjr(*nL}ePPv}Eh@!opw)^DEsSx;Zw~j^P?LTR|^wlGvq)%99FBr{YxwKmeJOs!Yo?S_+xqnaziLB=nLdseKC;8d|PSdHV2d'
        b'>AK~KFRz2dR}c|eJm0)PkMGe-O#5_eySa7PLItdo;YyGUY(oyUn-L3vs;VaW_JX<$PfgHKP@D1DNcGb8=mz!PSE6hUc+u5aOc_4m'
        b'v#Rs9hs7>mTo=13`_rJCAyj=@pbJBy#Fe*mF_Zm8kd|1&skL)tJf70O1&5zk=ksmAuLZO$Xso13YN!f+wz7JuL$g`Esdkb#8whpP'
        b'8(I&8U}Be7d>4fA>&36g+bphMr#YoGSrG}N>SM@$*R&>){pZ;2Uy@CtS4DAqSOqa!+9PVB*hNI(sFLYdX&Og$GrPIe!zPAji3Z`H'
        b'`&np^+o#eofdGHNkT9U~4g96KdE=q^<SKMaLB!U@HfD$TM#{8qF8*+)J_X1&layC)grK`$j*jw30>Xh@+z2z|hs_`!QNV^9!Xae+'
        b'#Wmc{EY&wzeaeE@Q5tBl2tXK+^2d8Za)+HzdA0c7yeDY*F*w09QbxNtWvI;tGyE5>gbjo=6kfxozU`T4%FRe2=vlyTp+Y;b$A+sQ'
        b'%-!tSdx?Z!A&W20GBV7$!snd2Gbh)L8UN_1ejoiOP=s(f(r`b&t-RL*D2Mi&5Pt7>aTj{-zz@;#_uNK7z{`;K-|+gd=fovB{C)&D'
        b'obI`^fTIla|H|k8mCqlz6GsP+<FTGS(GBd5fu7xp`vhMP^sK<W*ibEN@9(MH9`VzFmjPzh+-spR=XyeY;Dt1yhk>NAis8^a|D}s-'
        b'`S(8U__v`B%-~0)5tDDD<m%B}3i+K7pn4Lq6wB8HrpCySOddo$INN`WC9I&v*R1hlXLj{?clDf70FN}h5#-$o{E2!%v8PkFrHfnN'
        b'1DpvZF(!q7UIhsP8S@8Z0uOTTk=tv#PEn4c311bEm-2WQXP@X5iFiy$a^;>4;UT?_dv?aEF3ndY&~qSmETymqm$Ny@t;B$*AlMK-'
        b'7{hJop_PIBAXm@>A_Y&pAY*V(_Q0AF#64>?FY7(t!^R6ZPW*%9qghD^wNQ3>uqS)so=iq&s9kI1SV}tITwaiy&m)j0w7V4AwJr*B'
        b'ssGY$!B6c5RD8RO|9{)n{nRciCTdOWfVzpStefJ9h^>Wv^#w;=L{&@RxnM}9g+0vV8c%cLHI0<$F1P+?LkdE3Qe=V|H}&ixn@B_0'
        b'*qO;a-ej0GdS0L^$nR!CzvwPY{Jie_=HJ4@m|b1SsTBM3_J%99oxRP?*N|AGh*a!r0cuRZFV-Wl1YW!*VUGCwn#IJ6Boh(+ER|@H'
        b'Z9cmGse9LN>@T?1Sv=gG5FM>)zYE{=bP*-#WX1agV@TnR`qPIY#7#kRck40L^}5YEK8o({l|2xJ0IL@z^(WR&(Vgf<k%?&_Sp(9S'
        b'TTiY(qzzmRHY^NGGJzCRGLw`(KwO_UT{DwPh*`2Zl_nFTmX`tiU^ncI4XF^!RuTz$k=OIcigbeBy{Y~aZ2o#TdbGvR_uV|b^R_pv'
        b'_$^k%mvG$WZipk4r9F5Qx_PzchGO$mn!O4vc8Q0-S}4J_OcZ@e_%DlymaUzH<<4{uhQkk}F@|{>=l2cb#@9Uqu!Cw=Dl%clu7zdt'
        b'<3bS|KJ4z1fv9m&kT5g~8FU(tYvhFXU@vQ!*F?hHKx|e#dQ(K)k9G_0t=xJE1M>INLFtD<Oh3%`Ntyj)5dBh(rWBsLUZ$67WFo|<'
        b'>rTv}KT$tmYFl^qyTMG7sQ!8aAN<FOHbGy$A}jtB)SSnUP-<Ad>HXLQ242B{)FB|$(7hd>+%$+G()haJOPp0*b+?lT1rkj}v_n+m'
        b'q#7b>DtGz}DOHWWV#4#c(RLAD>@}naT&gxAX`r%B1v8(K(_NM2jwgiKZ_xM14DSag@M=hf^#hSRP;FQUA;Y&R)=x(7OkG-?_pjx0'
        b'S8Ki|n#7*VDTC`Etzq>Yd2YSzKj9vQkjq5{-uoB0N0E3r%5#<{-gVs&m39XSoMP*lQQfR=pc`2bkmsg#|I{zLx_js)b-e==2N)N8'
        b')W}n{)ekIff{apo$URj7age7L4+V^7E&vOVLH}&z5!`*<etaJi8fVW*ew-I~vj#!MuZ>_`NtJbK`;9JWs>Wfv-4>2v;7G8HFNh66'
        b'6;0zLw3JLFEyS~@k5WqV(3f1>N<14Xi6JW%5t>FduD3j*WFG0y`>DcGO=Coe?1d?m;lhShZK$Un#>G-Nli<R-CzeGdlG~(i&2vO1'
        b'MQGw-)nitsP!-2t`XA%}Z*wwHkQQde(>Z!)`oy#tIz}ssf<)~?<(9TYy6o*yI(Ge=<*xM`tJiX5cSS#pA1CV8%ot9Xi>{ctU{?jY'
        b'M@-nd@_LmzVI`BW4xJhxvOjiZONoT4CBQvm$n3s}G!f4){@I26qMJ_~?gFlef$zKg_yz}q|LBt5;M2bC@?YZvfA2yMRv5b6B^?fK'
        b'UYL+WRy6Zj7rQE&g#ErY(h*)+Ct>5swAv{S-{4JH2FXXYTA$X_Aly3%ZKH*G<Jq@<s?$TB5>M2l8mNFL_|qQT5FXe~Y3ixMom9#T'
        b'9o(s|(8e2%g2)><h#6ehZ8?!df#UU1K~xBdER0Ztd!|d+p8;}ixMpK8V^c?ySg^)4Fd^;!f4gAYkX{e@$4DpJ^knuU#FA=SiEc7>'
        b'b>LIvbsbz&2n#n!;r{<BkH#;$Zi`(-WXV(|$}z8ZLCjARW|A^zfY`OA`gyOb>y(IAKzgYfifBFzZ?Hcpf+#I<s4H9Xd^o{CN;9E!'
        b's^%djG+~%21J+xw_!nu|vkQA!@L-okkESvyQA)0|O)akKsw#0yq4%kHBk!lI=M2Tq|F^6H8v<}hYNxWr;SNL59JV;pL7I!F+SsX}'
        b'RXB?yY<5_Q;ZW2}idI<V*sG0QcgmPXQoD%Kt?$ZXc<DVgBpb$bg=Dfa9&K1iQkABXfSB8_!sRBFL)cI?ihI%IE(n7Ti0KJp2z&Ni'
        b'g|Nl1m39U#JOC*XyWHO%B)EbuX=6yflyz{0UH>7|2Wqe4eB9`~Jzy48AIeAni|8!wLcv|!#f$RTIa_%ox1cM*IGOu-*Y$KccYjwx'
        b'G|7F`iC|dBcX_e`UE^5X$pe_vwaZ9w?{@yDPVkRT1U=9>A%-L5nLOk~9<qUl+{;5Q6CfMf#%~MlcX!=@>g}EXp;CO(2^+zkIz`}V'
        b'>=}2s^WWuQdw2VeDP62_iOoh0M(>!^#f5j(DR$6Z5TU!cDP7KW#13Uwp^@03=(11hs*?+L+YE2JJ04}T{V`~vl%cSdpr3O+Rg(~*'
        b'H}SF*tQB{suxRj!QmU?GVF0B_q6=jd4BhI4Jpa`ohJWk?9)p3Ko&L}}KallCM_yF)$hqduY9na+(bk*6!LxueYrIcW1PVdtZ9jlM'
        b'7xveBJy;|3%jY67{=-jkKK}uVb<L?BvA@~gu5c8c5;yzs9EX<AmWS**Ab-vfS+9y8R+wFcC6daFm#$iFE4(*oxFU9~)AII#@eW?H'
        b'EL;~xlbISS$4C0_BT7pOua8T$1ToC2wStnLAlCk*<m;@?afj}+&RWsn;|&h?$<gaGRhVq}6p}%?m&Il+-W1EQ8miLNWfbjUj3w3Q'
        b'oh}<KMf1ab_X_5RqRt+QUII8gid`SdQWw9~Ia{(aEAgcqNc>%gFdok;W>dUp=-~?WstJR`st_*j=;+;5k=S&d+WH<eUaP*{e2MgH'
        b'v@HNbUe%_x>ZrwxACJC<Gu7HG8?*+$&?^XdYdTMf^BN6zQ?ZQjDFGNe?;ktS|J`Z1Ze}}I-6^R4_CH{NMQfs{311aM+K#XeP^s`s'
        b'H`6HY51mopklgRFKb)ph(659!)kU{+zncK_WGA<!(;){aCSE5)@|ri1`9nJd-12;D&M2l+KY`)lNZYyJOceb^C-+<jpaW6il`~ej'
        b'+3{1mb|Piu5Vxumc!gGr+G7*1z-1r<?-2nJ1x|;-&e5&lWS#tNTV!S83@Y%ZLM)<s(3)ykI2tHG*#(*0mmRkk9Jd5(@Z`<6Gjxc{'
        b'?gUt<KIubJV#qLIPzY^&*KubX9?$JI0`o^biznI`xTB5KJKEp~-AFq_=4)6|cl;1HJ2VLJizoc!S7~&p<av1<$KX(C3<}~qX)#~{'
        b'BDUuvap7e`H*|>JYGgv=N$7lsnk1PFGSq~f)98aa5n1#uh;vb$Ya^zB^m+AaY$FH}m=xKGyXxr<p?L8q1}q6k3iwe9DS^3lq1@Qi'
        b'lGiE$GaObiQT)#i?#uREDJ0Obkc$}pu>)g~5G?3Aly1#QCH)T(Db<HEBhJXykb%#FhA)GjkAfK++RfB+nhz%DuUeH~qFQx*!KziO'
        b'%>KK}0QS`mi~m9NLn0&At!YSTwyFum$#tvS{dh<9@FDa`bhZNuI;2mc5drs|4H(BjAQUKb5$kibIa3!@Z$g`9X$Q)>35@+{2f+GR'
        b'-p{18AC27&0PDE7cYI>EHz3%L?L(W?TQ}^>8Ja{4>=>enTJG5}SaT(&quP>tz5IxJVn<V+?>MFC5z{lRuZ}~nzf^Rf11I{$Q+)ob'
        b'a_h8F*GV+|xm~2;6)eIn3e8)}Glv*`oW>czH&HJI3!XaEM5R9ugS9#40flC*(!Q*{c7<8qOy^cUkIq}R{ZO+!IsexZO>3ALy76WQ'
        b'ZZaz%Xo%p&hU5;xge#bC2c&eYvsi&9Tf|*R1o0q@;GV~V?TUt+Iu6twJ`WALwMe-QVhEy~{2<2Ioz$*UwD$4`ckZ2(Ss+B3-*%yn'
        b'29Zb?SC^+>K})p+u#e61mj`Qpol>*Bm%jsq?-X|;xqBLA8S)PAj*ed{nkf5C9As{FyK9a+IW=RbTs<$H_kr1)yu8=t!Ds6p$!HIj'
        b'{2oj0dCmJ=2SomkktT6KJnHJy!me+>hzYp;gXXghn@O43?iNQ{{Z}CzC>sZPo!f-z1>dz<B+(@alPzKex2mHsf#80P>BSp5cyoYT'
        b'FLs|)TgTBaH!GHNk9NQw$`y6+W`Kg~T%;S!3FDS^3`WBb#Q2Jih{r|}j50dL<w$l9{L(Oj5csC<rWJv|UoBl}(MS_Z!fAy8A~9S}'
        b'hX&ft#`*%3(uLg84$XZc&Wtg~!h~og41a==#7O{9`Uvjl9SItedw`FM^SQi^JyI?gW7eLlI7o)O#+%S-rsK6ewI%7KG>d4<#jAED'
        b'(WG=C!DV!m7|}rCb`gQ|S3%w9W_8Hcs4@B_ADz(=^)<;E5n`tJqGlPvr3v9A&DWEn)=0Q}Ls2djDw5JvBICJ3mdGiUB@!-$$BMeE'
        b'I-C0$AB>!`8<J;Z*!%&0^C{7)%#56}7r@Nm!RYfFmIW@}@+QFAp=Wv?ABV(@^X+bZaxMic#H-`e4W*clM+qNYO<!q>kS4B<fdT#S'
        b's(U5{(g6a9764eWAoo<e!13a~&WYB|KgLNra-vC4uh1;e2Qub(dj+29aAWNiBcXr(z?=(WMd>@Cv+A{NTGvK%e2VAuTW5aP?j^8^'
        b'dDdU^;$eJ>;O&W9*`67nA{^}Ammx}7*#<yDD#<to0-xN%@b5#3@XPCuTwZ%fo>K(QQ{HRsPb!*3_BlwxztCwuBr<_e*2o^SpgY$-'
        b'>5{L_?~$3AM5ZJrY7JTOKcd)7-TXG^SrHqyKvpV!Ojec!tF0{jOxjxMV~uW%M6H#%UAcVF88$ENap_}=oO~p_KId`il4*RTx(x_2'
        b'>VkAhwgsaW@@-j(+~P`xSmrU2MbFAgq>tUl=OvaxhFQo+yePA{mIzg*%F{}uNo_(Td{^ZKD7IpvzOnili_0X$lKk*bOD$O<90QRs'
        b'7J)yF22S7rWk}j56oH1<AY}F5g5X3F{0HQ6!|^-Q>@(UR*iafcimBZ7LlA?2b<Wi%6>j|_Am4gj?a$(<4z=+<A>%xh+|YN6)y2U&'
        b'k=sAT)cFl;hLjHbot-U?a~4nckaDMPI+WPkK~~%(oG!wdOL)IHgqCR$6tVxcjdutcho@}Y+X435d;+t?yS07oCDOYE(~k3L;b&x}'
        b'3a=d#`uGHWj`#QNnp%q0FY0daK8qQhLI!KwE3xg84ArTJ8`U+9THEsyTcg(6b_+NgYNlQ+)<Z#sxA+QE<(mNXlL(<P)PCh=g?Ak$'
        b'ynzYksqz(8rFU&R*5)uJ$ExtI!TdjCY%Ro!F;>r)*0UEO;a8Zji-$)>mlze^Utoe06K+6u5yt)~ApHC4TJLg<S7E&HMv}2C0iUAH'
        b'_0DTAbSG_sw*QB3o5g(Z!&vkW7_59+;myO?HjEiOSE}p1IT+uJarl?C@y<kCoXw;llKK;OO3*)k9<kxM)+P~?n6j-E8GB<Z9mD8j'
        b'(Zsa*kSQ^wvfS4WK@7|Z1xz22z6g1f$olRW77}4nsBpS8O;QFCZdN;bWEYz<AnUg!3l-i(L}wYIkuLRywI`&?@mEiJ<(TmZW|$J!'
        b'?_cQs>JY^9FrM6)VSVLR57JsT-{B}Mx=<+kukD%=CuveiY<LPb>`t77s455-fY^NtkynI}Pmk)}iRENit|2OvxLb2ngsEaabvFb9'
        b'JNatFM4u-*n7HRDEO_e>7EJuN%rs3o59S)5oAz(HD}<`w@tG_BHPe)+)V#;ny?BW4fD*!<7kC`LJ|vW-m2^ztvVx8Urlzz)KnWYY'
        b'GVqP!0R=u&F?^%Quh81cwYDlP|5ZtiT*?B#4-UZ+MEZiJq_Ely6}N<?W=Ry5e3Jx1f#-0&n-c}4xk(HmPx&nfn)oC!0V^1TVOI9m'
        b'9eCTPx6%s67|ZVrOFo*FS(Yi1zBTTBuWe|by0fuC5nJb05N^DSA{`y~Za<WeNO~PO#b;Xaig@0{oe<`=KO{!zX=Rhxuncs~`Q|<I'
        b'tj%LjDh5vuP(4)d(cUJBXVds>>Ga_R2hr)6Cw$yBQ(JK>^u7mW^L+7>3e8GsVE<U*hy=v$e6ee#HshUxh5e#3P@`Wu1fpt_7=ngp'
        b'ZlU=4Wt*UjoA`TDg$9B<*M?C|v}|=GD&Bu<(>za@C4>gDKEtfRGCaTmzA>R&ps$0^4}yy9HZVwT^R(6Oi~|R`t%ro|i>BBJB3)mV'
        b'Rk$=L6nQ{_7d1exN@?SDW=*5S83FqC?(}=o^}wp?8w=kXKl7VIf>sNPrTsN5_yDN1X)oOkDy<*K4O<_G7;0Ca{#f1Fd2aA+Wvl}q'
        b'_qg@wDABrj+;o(}cjYu?jv!XtD^J%K>VxRy#;q5fUZzIBZH=}-?s#mL^v1;Zn%)%pp}*aaXAg3D|Fs|bJNprA{r~94{de?Z!@u_9'
        b'rT;@evj1=WSa@eYpc9@;WTuNSD@5*@(v?|-c|p%b@|Sp%fwI5fD%@nKlJ+QQ1uGF%&bz0`T4)HKQ6Cx%haVnaDdPJO;yYWqE-Ue+'
        b'Sxr)V=>)#DQ+un_Rog#~epNaUHu%_f<>D@>iWrDHF@5ghI*@$OT+pKR>>X$NsqA6Eoy?Soa!hi*89#Q;AnMIjLzxAQHiKt8mI2(A'
        b'S+R{3pW+#)i6r)~evyo;f9#eCHi2@=JKWYp8jgg4&N4#jG7d7#^!+}3GZzM`XXHUH(02Pwmir2E=FYc;E{fE&fh7N3Fl5|v9{o#A'
        b'&BopH$mUd)iC>WygWgZtP`U01(=-yGWyKgiAH%nJ*7r%E0UwT_=oA_Feyp(mR{HAdmWBw;y5K3&Cl*OZg1T!h+&iJBvM(U+DVJKk'
        b'C!kIHCkOFy<9i3W<88k1{J;}qNds&i!Mfa4j4zyE!bR?rpuww~eOkk&G2Qu=Cb7^5?p$l=JUL{KD<)FjYxN#%gY|7c#smGRMQ}cb'
        b'*PITt8J-%0njxX_<iAwL??w!^2wxFQ>2LM!ZF3h82*-zTd?JE-t<AG)jCCdXL?RY1I|hC|#-1fvd9=5_4RjN4U7Nk(;GL)4zB?NL'
        b'_}fMT`m4s34=5N$tuf2#nUH5(DprUgPAl*UJZz<Jw)|3os{i&jw76O!Xt;-$&HmhKVM4Om(-86`@p4!w$!(BB&^n9f%1p@qD&~y{'
        b'^!;d2;bCxp3}M9RB_?Q-Ox!8L&pQBa^dQLaC@i$K;IM6PVVNzOcFJ4Yrs~u34=@|l&5de%O$#r^k(j-X@)oz965*RnIdNuH8-6b@'
        b'iKa<Ai^M-e<PaGl1uuAd4u)1kvqNozCHTP@tHbMu+eQ3AfY;o13Y)+WVgfGQ|FqHK9?@KpwNcU_N{dN94GovI@OPBbVzPS_rga3D'
        b')8=WAoXKu$7tz&Cq}_^5&LtgWt!Q_;5)vE}O`b+~aW=P61WPEedE7z9I<}M2AA&s!F1^kAx<t53K$B<YwEcrTMfQ+D);`!G&zK;t'
        b'?bpKQ=~bLb4rMlx)@H?-d-xa~+eCT};N3coNO_=zHnI9;npz2OrPIVn(6AJb%->Pq-upyVBgCz0R7Tq~bg`|mT}@<Q*;qT8t*r2`'
        b'<Dy#wOUHD}Tieyp$kMTP-d1KF<Fu`J8l456#Z75L*MfSgFkEENQiYv_Zh8x+Z2O7eke;JkOiYqyshs~v&pwgMb*+0IT8K#8ol@kj'
        b'K-EoRYw8$KwB{9pUv#mJR@2yR3MN}a1~0Wpvs8>#ueD;;k%K-FiJR!ppsu+36}~DgQqMg<)xCOf!dR9B(qo9y1e<wWOI)7Ac-!`D'
        b'k8bgP(aJl@h_(lO==f-4;uAG|{wJ+mz{k89)H+nonG1Dqx75^A3=^@c4sRgR(=L!AI!vcISW`pg*QucpGZSym(=qrMbLY?u(T)WN'
        b'1y?!Po=#M7)<;urLr!L~Dzm_tQ%_1~5Xd4{Q7${>`g5eaz-TE}v&9k4;&9H7vabC}q`rb1Ee|U!l8f}z{F3BVt2P$&_zK&IvXeJi'
        b'muP+IPEE<=l7pz$TU@G~Hqvh-O5(}vhl%U=uHaf*HSfzyB1!3kgr!gG?QUt3dN#<MhQ$u?hOX9{SE<wcM8c)_?c%~2>J4xB*gkDp'
        b')UNgGDNR~5SKlfv0seMgr=laz7l&sSN1QKKXMY?l$wJ&qo@?a(jA(8sZz+DY6<^#Ys!F0)Ij8PA^!Q3P8=ozfMN!<fgDWn|Euf~o'
        b'+^Tuz2D0JLf<(#J`1K!)%a(IrY{Iepg!f7Rhr#0YEe*Ro7e-DgygOR6X?%W^a4pl~Ce}h1-VFjDslZDqtd!71kFYwm^g^(BO-sWY'
        b'%0}x~Bi`S)^7aDj7~XB=wzXEE10C*ntrh2krQ%(Mgk|cky(OCB6)kRQt>zqI7{Ycowr2C+@8O<mtw3LvTv;nVU*rGZhkwtZTdWH$'
        b'pRV?DSG~4De7Z}teygf^lXi=^vW~3q1)r7oNVBEHP^H?&*=%pyY%kcvv^+vi#BM_04S9sKIM!Dj<B5|wb+JBO%-*#3q@G}tjE-fC'
        b'V*>lHu(}v@2_PqicB`R+yH8bLAF+rK!``=Pu>;B&rpZ{W_RfX}ecXMmFg>!hq_h?-8XI0d2&g$^APdNmjYAisO7vVd&WcAq8aOk8'
        b'CXv|(;rC0E&wWoa(3|J<h)^=IWLjX~EzP{2H*BrGY<PFXJ69OMf-&CQM5H~V=H?)zQot3si<IC^7M_p9Wiyqob$GCDp1SK<MVj@O'
        b'1se~t8flRv@e(P$NO;!aSLeKm0=Ok(e6_tRWab1>!&Jj}v#bLn1@eQZ6g?8i&ckdrLA_@)9fRy%Vfc2I)juNST5~bCK;(mlass4u'
        b'Be6r|bI*u^A;ni&efEPb{3jq|UHKc`8Ef1#V$H?TkaJ$A_MY+$*(mLR+N?G<H>!FYwcEb!J&rF?SY5<<UHEXjdfUggK~;0Nwz>Iz'
        b'?H|>)7qo1Fk&d<5Gn)Cwg1!TPfQmK1$E#r8Z9dBNmc-QsrKxS*oZolmp9hD!)V&T>vqO7!Iug4thWe!(kU2DIsq+)kIZeLen@C9R'
        b'kD=TLzUcK+&4c(Hzqd%6^G%e!&F4PwJ+7H(%5_|2dyeXbh91)%f~*6+9Yl+eRRdX-R6d`@>Z0>&t_?<O_R(GtTH0D*6zmPix6bRL'
        b'?cRgXvSzYq?>AF?qBTu&>*u35E>+s<eZb=KTeX3|jY7<<Cw4tgoOt?oX0bHQ`ZSW@qqlr|0tOI>?8Cp`mA{m7)oj!}Eit<m$-YsY'
        b'_+5BWgsYj#&zG!-m6=_S^EdXFc%r_E1W+fQjxg&*E-#f|AY`u-vRf0s2`>_#cpB?EseH3!#WcwL4WH>=C^fqXuCfJUIJw)sFu7|3'
        b'q<<~p6jMv&MdHG@qioLuM>4y%<u6mk&82Jex8w78hj>>hMNiGSMCPwh^**mI5<l@{&2p7(xi(4us5sxDqNjeAzGJi3J>xFu7mxw;'
        b'$mQDTDk^V&UJclyGdRAuc{Ra`Df;EgR%$TPypSp=MI2TDfh{4-Vu?ds{q&A)2X{M2X*Ll;;v8L<U%#_p(?RD#Nq&*adAygF(^G4T'
        b'%58{;`>mjhhy19R)v3%JQS*E`TdZQmlG}|)a>a$z<c#NhnbgI?jZ=4Q@n+62Xr3cr?1dBGTya63_ro>wxF>PBX50e>C52z7(-c>R'
        b'2^NDXQA1Y5ifD!1?Bl6k<>rXJVG{cz7}abPF$R^l#LLY<xjUuU%jhFC3=um2DK7E36Yi5rf`MdQoWS`O9F!&oVaTO)T+Q-cIxK(B'
        b'&YJv<QX7c=2adpCPIRcS^rEuPxsU=@S0rW+9I-7|Jt~HXayfLW!XL~Po8JoNXQ>v6AwpEHVKSzAGb4A&){qs=1ee5j<~J>LY-T)x'
        b'UreVEqg?UsHEJ$_&wJ44rXmB2ukguh*F2E%y|*FDS~23i`ykIh<j4XVmKmNO$++bMwm{J{15!*Y(zp#`PdTy*%IzXO5<XFEaW!Ym'
        b'^sT6nn5l~ziG0Vk=Jo400!auw!~TuWt2p?i0@j566EFXHnS!rcV5P{`PFY_-ExG@(dHHYdEcm>|ohx3kmM)vYZdxl{vZCxEB6d0K'
        b'y|NPNlC^v!szkQrL(4;i`MAhJU94^^6>qvAdn`MY;vygbZJ_a6PefUx3=6Lmob>f5nk0eOM!Cx^cx-^~8A`<kms(axQwj!}EmIZy'
        b'D~g-FTrV#EG7Yu+BFP<Y5&ULbAX=hyPgUT@9yX5fJ(XEi1+RO75tt=^9-PXxw(zNmR`Z5Gd+i6C%`&>Mm9Q8~3(i0b513t3EVBH*'
        b'rj}J!)d~&S$N9XVc(_Pp0sq7kNmwoB=rd8)2)8WX`r8rjUwnAKmNX2H@^I6vnu0$!n<ddDhDl~h!M)M~ZNAbX^l+1PYG!=CJ6_^h'
        b'H{w0i!rSA&73yUiY{`*4?AC=F9v|`g_^iO?QGT{_HqJS(Hkx&6i!Nf@*9#s|<!5P!3)R~`T$QC_b>R?Ou;6`dks1O?&jX2-9FuT^'
        b'KK|^0xUuH$46E1d61l18Xv+1_&L%2g8S%a%H1M_1z@e{6e|#|G7hZRK#03TE*98+4b3Cg?yiUHD^*k2Kjte$PdMLxaSB9QfJNr~s'
        b'+xN+1mwPzr-Z>Yf{}aT=2>x3^uA)VHEr@&z59+1?&}N|W-Ozvrok2W&<zYo&RAR68p7}#dggjY1iSYiug%Hi^d$vVPQ9GV(d4{-0'
        b'uO#^Ilo~RP`K5I3vYcJ9xnX->(v%qsXo}YSgIa%K=d+W)e5&RAWMb1@X;8{yEXZ9(%U+Z%qBlI*LPxH8ZfC^9gm^KrFO1Cr;@NwF'
        b'%)T*hfrbBqmz(8<J-XuRIL_$N(H)i+n9;H@VpGiI^^M7^)+W0aY_u#wN8%eEYw3~qyK2|()k0Z&sh2lw$7s%tKw^))NoLnI<E>Ar'
        b'|3VOizi-6;i{pabBB>}j`QAz=nVm!=rr%SNNlJCZb#qt(Q<7l%UzGpjjFsWPkJ}7IDzrq2`R}^$X6CHOlzG4ZMv!%1!1Q>i8l5yy'
        b'Y5ME@=*0G?S@&Nmokw-@W>e<DitnJ%C4{ddDoxL@?r$oc4LXqk;sE+!(TyMABhmh^g1TEmc$$AGsJkhIWBs28bw3E<`Tlc3-4!AH'
        b'y8ok~?t38|=YKzF|MtL4Bg<{AVoaHY|8!7yNyyvpKNZvkgm9DpWKefr2*2e&!TYZJ@&L;i=bJU@A^p>S?tm**#eOU@<;L*(59kda'
        b'97s;SW-3w?E)?zPZZ<WcuX}bHe$){Ik5Uum-Vw_E4a@nOQ@G~;mvVgvXwp=)>-Kj!dmv6nC$r_Iu(x>!v9?sLY0=vg`DgypOv~Aa'
        b'JM1k7oF9wMhdt2!M_NheHNT?00%Gh*?K9Q!%ErCFiqo|p5X%!oZk>opM9c!>2-jSvt*P1AGld-(s*ZI&+%cgGxeipnW{N(;xD>M0'
        b'DwAsp-{S{p5^rbT6#O#j>S3rzHe5d6ytXuU$IcLzJ5}jw?&JY>#u5;Ik{w$1@g;)(wc~|}e)Oh`IDhlMl@Qux4?s&k`Ml;DN;89S'
        b'x~6bzo1J;>Ilr0YlTY7v6C^c!L!8$>acAV21KTdcgt6qj<QhtFe$@SV@(ya-x#0<CNXaJ338GgjK1{~eGUr);45s|%fSa6W(uX|Z'
        b'i+N@CiT7YGZrkkazdlg?lv5ak$6>PRY01uVz;0-++9{v6t<zPfN}j7V<<6V%HN149f39>jbPl%F|LEV2yooY3Fa}$E|7{FF|EOF_'
        b'Cfnk7Jb1wQiHKdaAPOY%g;;3Of)I`DNS}Z+%(u1e+#O&b-<x~@<dtd3wdJ;bqP|r==d2~Y!e>N&v!pVDOtw>yk~06mdWR@k@G$$E'
        b'C3MKg(hl7O?9&45t^W#}n|2`CMxj@#nM<CyB|Ja}*%=1CrY_{dcSn{FMtxPPC^Y2jmQ3KSII!)ed)k>~M>13aq5HPP4eHUOX8<pl'
        b';o$~R-xEk4G}+55t9_~i$!;i`+}tP<Qj$|CF3H!Nn(Rsy{mTGi8~=POg#UVB9-4yx4`1&C7FD%14)6144#RNN`GX?@*320O2Gp7v'
        b'R7SIVnE?kxyBAPL^wx7>5Ja<HGgB*i@654aF#4rKB_P6?fq?-W1u9dEUZf&2y4S4kEpLC!qRg`E^_Ci@=Ue*>+WUOJ@A;lbhkf?h'
        b'd+oLNUVH7e*4cZl|9c+J-7M2LIago&-(|iyi2E5<@iUvHenPtg2Ssy$_VlQtkNleEz{dw!c~<$<fee28<MQE*rJ$e<J>9VR2(C5^'
        b'yg*VIpdc&HE1v?T);}HtrPw4WRCq*noa}>g=J|BA9QK2piGiD?I@Sy)8yAV2Bu`B5g9mwz*T?tiK>D?gmFN#2TsR>4y@Yp%4+i1g'
        b'ls;V#y!-W7_0|4^2hEadqia;@pE|_PUJljt+CID}_Rx?%(?sZB?vJh!cs!X&;CAm{9=)W8*FfvRlQ=;0JZb&Ux@8;kHvaGY+ivCa'
        b'!~5?2r1q$iKk&sazV@h`Ka}O+J+%v!-fs?hxS-BpKf|jsOcy!TWL)6Du0m>}R()5REtU_gtW~FCP<$|{R(&@g4AlDnrQdrf8q`q#'
        b'_(9}3&llf|&38z@<Dk{O(CW4@{}J`i-Yl{uTBLO3f~c>%nfX98v#jRa<o$M`e@|;aS3;++X-b$JJ66+jDH`kG(!uBrOMIR7Go0?>'
        b'vbmu+PG{bVubpCh*P4S?GNDp44Rqu8$YjdgqjY7Upd-Pmj&ro1u)c8?*nHMYGOJ*)7RMD89-KpMG4kdt<(S4={AWrQqapL7v6(1G'
        b'zT*^Od)ZCTT1aeAxeT#YTMoNO=R(AD_jvB7ffKCXE)N=)T7i-8Y$)|9E!z&c)y<$Enk$u_8XaHUj7x5yS^4(uF<XpF+3A~~YVfO@'
        b'p=fbLENoJ4hQ(Ef%N5hNRjCRWD6P4-S;==ChrY<pR9YSHSpMAaP?r>IQ1ySZm*^bDB@XqP!b~%MS-eJC33rpM)2E87T>r6CL!}rf'
        b'qmR((Gm!jr{~!A)JCz-r(AY`unuF2-I7$kLxlBWl+t3VeUVnD~MD(IDKDbqg%LL1f);G?$4o^7W6xjtEwpiSU+}v_=rOxeMUUOWO'
        b'{1|LaO)#|VV6By=X?j~fo4`Ae{?`Zy0Z}^B-+734C~B^Xuq9W#Omc!MZ{s)m^g}RQ%;cF=v#@pi5qhzszS(;r!jck|9-XwmbD)hH'
        b'`ne)}hR<pzDn0@T^Xi-RUqyHV@s7cpc662u%*4e82`Dvwid^i_E+T>iq5lLIL_G%H@tW~n^0zhd_lW+ELk<(K%T;m$<?0}K(?U)l'
        b'JSjVMo~`vCUtSTXKM`5D#rO>~m!5TzwK6v(JM=<g{1=(`&B#Cy!EQqlsIN)6_)lX;lb?P?%_i@AMQs=mkQ6{d5Ps_GQSEBxPn_{Q'
        b'Wl!>L^U0{C3jaH2MlOs0pYLMvyIc3kdLuxX#VJ+#@jmOy_sylW&ZsOpdQkg!hEJ(-AG+dsQik2`$rhDHJz*?aRD9@Pg+K`_-!J;4'
        b'&l>;!TCSxyrd+f4E9F3nIw&L<e-Z~$RLRXDSc7{b>~t$PlO@f?JMWf3D}4O>g(Whmj@3mU$Sf+eO$VT$=LuMVS^2(u$=$}SqE)uY'
        b'z4HC)!==#Bl111HHjIh24290gD$dD_(m!u?1jdCWsr>vX->|9Y1k)N6`bQ%i$LsFE{*>PM&@aegxN8^2jeji*o|w~>iEpRrbTq!K'
        b'0(Fi*7>SVnIZjTP|JuSmRS{tB7bPxz>d^I*H@Wn{9AM)rvjtm&cK<I<T(Ld&=KkpQ_W`5uCm{ZixZ7vmQxbt@q6Q$m-Px4hqKLI*'
        b'O~uyO$uro65$r3%2~uQ<tiK>qeb%4U42|oe8}FZ*xfFi;78P*hVUQS_u!#we{-2uHZ;9ujq?P7+#nMb{amFL~r{>Uuu|N@AinFg*'
        b'iu!~-CFA`n6C=V41eO$G+rB9&Zdg8^bUiecxw)@B10<W)NY>nrd~$!_J{*SqcgP?3(_R}{6G3y9)-K#IN0VhEosFpS2<dD<$y9CT'
        b'qDmjhJc(Go)*4q?g<}-5Br^>m)(@cYi?eBsKj^1NEOikO3WI8S^(8ZB7C2>10!p@~C9JNs(#dM(vdE8~Wy#AXa%87ur|=6sdmG7-'
        b'T2#Am+2T_eRs(1PiF4eLbOz9zOKFYIkH0Nr)t3tlPBXR;FaC;EXC(|TSEnVA%;%s89N@S-R>LZE?G1Ak*puLQ*aul)CGO)hsCIy4'
        b'Ho+LZl$HS0@j6tJr2hj^mnF{6v45dp;@*TNJPxyA9KHm6YIXrW_i}+c3}ZVWG@A?T!0As#F5ts3{zo)Ei^(gk8Alij3dHy(QZUdp'
        b'D{y%Ez%E?&5lB3Z%f2L5)RV0Ga0XfP50S-jHSl-OU<__(8#FY_8aSH;-F*lud<_+9!lM2SK=4UjD$N`gxnKf-8+jOU!I`+v0a5=d'
        b'yxlmmSpxGvd!slmyvrYK!|6?s)^WikjKfN(v<u_VAnFeu0P%op$4(GOav?u}hd3J&uL1k82EVP%Otc2Sfr+mvMb_ZSEU5K@s1HC>'
        b'e2p7&zN>waboxba%K`pl(l4Ji;=rMxnhx*=lh*W=bQ?$zwz3+*&`{$O_5K5_0;*<hks1F)3LW%Z1+x=(JVF}Rl0rIN^B2i=R~?40'
        b'Gss3B2emp>LJAzsJPLZ>PAOj}V-p3=T(ed5{`UdiWYRW%8kCNMLraLt7Ib@X;J^n&<lQd44xg5+${3FX!PHPwDe5;Lh-xW7HC3e3'
        b'E$TNw1`#B)t1kg$eCt(Tg^O@xBAWnI6mF;icx>YMA7Re2Hj*`~ME##7WQ=r8F~+&#zd&?kNesVSaw}DGz;Ak-P1tQ}z(+@rcO^Wp'
        b'Vy=naB1rH$UblKfoN*HgOY?FD36CDYIUCw70I=(HdU|BB=*@$oGqv4+mBuz<<a^QUh>mlTbhh97d)$V$dyF$-e&;kt_c^Oz%<_|r'
        b'1*K))4chsL5w!E^sobNLR&wNa#8SrRW#$Z}wDOY;S(1{T{4oBj2W9;WeJUObD|wgmXAw`mAIG9e%S@az%2Kt~;l-M?7q?r3ZCU=8'
        b'^~ndU<V!W*L$PzXx&dXuy1E@xMV5cBK0XTPkQ0=2RWzO81SNfHG(FP^N_t#0o#X^1T^>y@c7l>Fi>5oAABuW1nof4UFIvRj41+cB'
        b'*doqKqL5Dp%xvUc7_*69smOtvQBi*-nvT@GCF*~QrVrK(W1s7bM{8kNzCvk7$eQ^m*#=J|uc9>Dib_EK05C~Knr%iUPu6rI_UW`&'
        b'NoOspbd$^rlAO(Ai^NC>iYwWVYyIErKkMbV<v?i8t77E<>Fh$u3AO$Y_5bMQ)N7po5i5sD=TiVvmu9<@7p7yI$3cnjgdtOl5jl*o'
        b'i6p2$fsy3Mj?m*WU4{~Wu$qHSCnGOITk&&BYSkq3g{VIsEtL%12F>x|`t4{=BfP{mjbqW5+0KtdKJX=O>s8!K#tO3ZDhz7?VBNd;'
        b'Dz4TE$?1#FK~3j7qP|z^g@GQy{;(@gk<JiWo`ByCi~5dUEJvDXPd9zCM+M@!!09|4H2&?Shk8_=r*OK@ry40i(2#_58$h4K2i5|J'
        b'ntoB=(934<+;Y#JanBtztiEog2X6p6wg436-JFi;282D>)>97<p2mIc5cM^^gRmA~8=pgR_(rs$rcFeAumksNH^9&11LL@@T1Y4H'
        b'fv<5}z?63MvWd7ecLG-C5kLM$7>vQ?JdjAleR@XJ|5tRRZgUPx?*}o=r}04Z!PhXHCq;dwG$d&<h8OwZ|6tsFQ1T?k?Fm@*Q2<A4'
        b'9s|0&x0fg1VX-r_k!|9|Mit9>y!K>;5LW8amH(@oATfC03AmQ7W)sx=LoY`rFdIehvfe$AHr?Y-2ew9Ue^e1nXkNdOW;3AV`d>(A'
        b'naC$Jcby}dKZ|TWfMD(u^}mZ^kjShR^>+cay)d#G>pqKnqkF7=0pyhkK_%!oyc$(sf)Qsnh<XdOIm+B4dhh7nW4YO;p5FcoIg*E4'
        b'*?x|!St7EgnsHH|+6!zN8&K|M)t-!<HNOX(^}SJ(3Uv2llDSLtaCYb(rvzMm%9^)DeFBWzA9S3InJ0Ru_XbUW;1b>!+GU%rVp8Go'
        b'aOiYDjm*KgPL+l@m3F2B3y{)!+L;P0pcfNM8tBq8Ah$C;62(19j|@TkgjCK*JCjBIjULk$XQHV8wFl>=)6N;9{+Aw3tzf2$`pZ4i'
        b'_{^$VD(e3u6-bdW(?tEn9!yn(H5)|lk3D<tIRNPKrsZs+E{)#ZsAS`SYS@h3y$#T2Aol>f6lPJ_*8oYFK<Fa7%X4h!GjTW`w*K=T'
        b'jAuGV(&LjcO}I~=K>MFFKTq07191nF>)ALj(L3o@Vu2U2^02#(z^ZLx;j-g{#6o*T!Y>p-kF8}*(j_(xK_KG(ZAcN`^6Pn4jziNS'
        b'UY)?s1geU<SslA-8S7zZN`91Pqq;Y=w(E=Y8SIb4GSb85-*h_vy7POGDR3K<o#x8WxC*zEmiU6y0u%_;{Co0@`}v6FT!bAPq$8B~'
        b'+g|CMOMQ=zE{V@isiW3tmKur<^w`fv?qvsM_zd0WxX9g51ZPBOZ(|QW{tC1m&r-U1QuK+N=R{m?s$!~Wd7>8^GBtEpRa(W?D+dyz'
        b'PySwUchtnWf@Y6}cE~J;dxF9gtAWC2Jl>AjsQSzZ`I~<TvyOi4EPHjaBg?j6&wuw+5AfLRslx^rrCCqwe7fq>W{$>8%7>#4nKS84'
        b'm*6$_hl6co??}GEH~07tjaudJ?9Rka4nYjgf2Zb`s88?SNPkt2UyfQfP;#1DmP*MfYT0d+oTQd%DLFwco665#z9$&Lmd5*+drN!#'
        b'rU&caVQ2BCM}`A$;`pz(&Wz|?J!bP(t7A0nE6IF|FD_J!5v$Mtn<q!Dhpw5i!^2U~IB>8!e4g>1o(Spqh;+ou{l;bHc}n|VBHkrE'
        b'j(B9Ar(@~7nR16|PIittJCC-Olo<Qu<B2luN@O)I`^^UAUDzXqq@D!=kjK1-7j~G<bgeo!&8Fgob+u{(FFaVQPLJxPyujD0WxOEN'
        b'`Y-6WL|hFw^jjk%S4Euu;JSWeWaMX2|6s(WxvsB@j9d~S$F<^DePsmHM%YKaxAiCkI&0NBYZ+xNBNwU`5}^fGe!G_%Awy?w2>cLV'
        b'j<22s+y5f@0P{jVXw79bC-9-`BBsY?lKCU*vL<oDgODD%8zk}_kf`}R_7<F$xO8zbcANha&iWI=ayrP>rI6@JYyL`)U}>AQ!RtWb'
        b'Al{M4M1X*Yp{{*<HfQ;{yN^?47$^rCNyXB)9$7AS_c>JAJ3SgXE4eRwxagPeLZcLt1FesSI>6EG=U|F1Tr}bRYfo_41U#rG+?WAy'
        b'QThopmx27vO&R{-czkZOQ4>qN8#JpjxM3ZXJHtWI43m%3EF~HhDB%RIp~}FOyv<Orj`MFs1({S1YrODF|LLB<=RL-SGSHYtL=(|x'
        b'Rq02&7jcwhO3j35xqiSzM4hEsWRWutRY4{sp+{5>VR^k9_iO41UiFQH<<;)KrK*A)4Lz+CO-LQfv<p342mWBl$J1;9tOlH1Nmrlc'
        b'=|VI!TgQ2&fMtcayF)#ajfMskV88&oX~yasBcF(tP&cP}fA3im7@mok%}oxc<iFF>dh^{2|N9-mj7fSrKiqQfcM-DoXcB+m47T`b'
        b'Br6_SV?o|$yMv~MPAyEyAW`v|h$%5~dzUQ{lV@TckS*{=Ot6Ww1ADror+;|irP{;|yzqK$;v>A!Q``KtkJ$4>_iP_X9=qzo@(~jG'
        b'h`vUZcSm=#FFcBgE&99_KYt7&w~y!_Jb-gH<D7He7rU{u)}O^_v5k;P$?@m`1=Rcta`#l;f^Gs%3gGvY-O5QA`9@5$%}(~!s@JC3'
        b';#|c)d)Gpz@|iEiWRS=Hn0y2aWq%XBD<OAX4fc1&2X@t}?P)eOA8_Gu7!|$ubcc^fXNx4W=0a@Nl!PvCUUx9zUMGXROQ5<Mq+728'
        b'5~>>Plh~ULFH4c)bpPre?D!A6O!eLcd1ca85%qoZ+9@BOYLi{gH&rHNg-KsfX!jgwv~qOi!`R>J;hp5jZK$#w$CkvGO|gft)RMm+'
        b'E{RL6lBe!?FM6Mv=jhZOg_nIZtz2ws$%4aGrf~82!5f2$FlF3x^%(`|>}*3;!W~(*+fy4^_QkBm5tBctMht=AFUaP*t^yAUQ_OYI'
        b'GQHdT=L1&iXv|j~KL5zKV(QM>tUpad)_fu2X~1`#qkf>m#W(^|_y$EF>6)x`b_?lc-5_qoxKDZSIpF+QigmcMN9!g4#mXvWkdu$s'
        b'&aFQdCQZSfb}2@|tcxapm}H`U0QHx{R_;O9i;^?L&<$8^QxLLp591Ga6mkeNghjf%<}dBvg*k2;I}2F(;1ucl++0N{ctd;YR|gH-'
        b'ch+-nP4f18KqW+DyzM!yMrP~KzCqib1c6Aiq&S{Vo9?{$lxnT-j4%3Qo5zp-uq*QclARGWpyId0(p25$T^gUJ{#>Yf?%bIA$4mw('
        b'=)+vO^^LLmRjw`9aU)t@w8qO1tY};bsv*n7Wu7#sGSW-ba~ZR#LAON*PzoWDrgU*Pv~T@dOcSq7A9_l~jb8M{vrL9>i$Iu6ajWiT'
        b'>Vr193CD%Ho6%*#&diTqtY6~N+!z@bwK>1&ul3r<rR36bR$cRDR2Bf$DY}>Z+{>HfH}|tIktGzqhvW?pasu(15BB_IynL4Dvt*Yo'
        b'WBH~5L5vXIx5JY+lsKsWBrd=i9${xK-vlyO`zw=fx1w^vAa$5iz5iM7@y~kuKkE&A-WwGvyibQ=OKn+mGN{VPILWDk?WwT0Vh}yS'
        b'-}Y81-i7M@_j-??>g_+(8~AIl_piA2p6W24{-Dc7@RG9tJ_ij_#$QBMf$8BSugdV9^r;5gQ~l}NFvw#^BGj2!<eIq7MB}*tTy`|='
        b'i0b{<dyl`~+y8oR;7G6ch=kX(Vcs;ozG{$)Uh?*q{f1}H#U2%hkxXU>so-hyw|nci;Pvz#KhWEMpf}Lb>+O)>72*1yb|<s=3W@ho'
        b'JaDixQlTr8*aFR;98hJvdht~iZ`y`o5B!sq&b7MEUysUdUm|JTSqh(;uEG$kc4WCLocy@eur-M7n_Gdpb!OU}y;b`rQ)CVIKhq1e'
        b'T^Q1N=iuVrN|5mR1jMf@2{{PfXvLBKytH373gQ#?k$)N#my6P80w}j+v?5z76rw%+|0;A0sC+UO<&x2&^}Queospp#?l@K!ktMAP'
        b'&A3<@`Z>+5RQBrtC*v6r5^Q4V3o*+r4{Yqkw}(%Q^>5m<!hzVZBjxsL>8!b{H-FuM4qXZjG89jv`$*4<hL%+&9re?(=asGXp#d5N'
        b'u6OnIm136}>s-%WAK&}0DBWJ`ijXk2V@>R?@e7lqDGecvRy)2~={j~plDV+|%nH|yCvf1&{R&}ts6K@y(`kKHFRWI1v6^0OoAkw~'
        b'K^IF@yH=f91wUac{8`&`MDa?~2G@URpLNbVYklE_z0J4nVZ#3Oc`a+g@<FyvkNtS->vsXOw0V!?(XOY{X_Iv=_vsdvEE%bPD-r{!'
        b'-=`4v4zcoI3#uwzH8)_|hhEe1Wu(81c!wDO{aozZVU%#~`X$N7{8Jo^t<%Gsir-23KPZxXTeS4{Be!4Nq1v_m%y#$*FMvOrdpv;M'
        b'^JiQi{Ayb87&n&tgskRU5pAF`H<b2=D)pSVR=-fd${vu_04FSb8G9@kx6Rc)MtVQ$a+~J0Xv5?nb{!*i!0O$DJMbP2!akP9A5he9'
        b'Oj>2!On1$HV{X)VJfKb}7IqZAs?<JCMtxhdapT{KEVDlGQxmaX{SVW?di5!QfP)1*ppXdoJz9b`c_->UN;=K{jW{VMT3+l*w_6Q*'
        b'mw^cCX&@R97li`d*aS;DNffq2&AAF~28@}>&T5K>ThR1uv?8#k$VQZ`82iXZ*vc0YE=qJt&Q-T)<Tj#;E?E(mb#kX_*HevhmRvuR'
        b'bfzFIXS^^~|3sK4XK{KNXbYaKhLaDg9$RIauH|C3#N&>wj@hvIT7>leyX)rVA)lR1EUg+!TTh4I6x!zrox@2zp`@!%;E#hJbxD_Y'
        b'A~D_%aB5F~PtW0SY|^V`eLY>TW`!9x)?a{D`<Iv)$*<a7cyN<m#-A8%5}`cI%2=(=wR3EV*8LymZSe_;IVqwrb2PT8%qw6~t($2q'
        b'a}`|cj%9ulb#DzNjSZ6CefWj*ycCDEriYcEiX|fQe=M3dX7X(qlT^$7a;)bZnK^Vqb>h|0q@*6**wE0^JEQjxU@iPA-b2n+yq00j'
        b'pj>areCpI44`24pPR)Pxa!H)!p`OF0DX>jo%f33b%4T_>hn1N!U7W&J?pgtgCKC&9Uc?so<l4-smA=pP30>GWI+v~?QEGTP`xR^*'
        b'AR<Wg0<)(*@e7Dm`e|KkJT}u~#nG(WT60CzE2Mg9I83-crpwBi@aFn9$oJGOGxEp<@giouAaVOLr9VAkUt(T@B8daNvex<~2(N>('
        b'@wmC#6E{ZQ2kdHo5pVjMGXDFfk8qQNJ<2AeEmV5%=|N<+N4Mu@co0^tGnu7ty4l%Vfkl%`RiTf>13e{c=e!${g@RN!?8^B>-U~@S'
        b'RZG78_dRpoV4Z_hMCQG_M^c|%J+ZScn)_(itI{os_eE_6;VX#qUAD#TSQ}xm3*E$+u?=R6J*kqpAkKL+uZf83N!ktySW@mV4YJSB'
        b'>kWN<TkGE)82j)UMc@Bv@bqnU&A!ocU~|V%>Z0ke124wJm2@KeC0+1s%B#ce29kS*6$syhQjo)WXdsUW=8=9Hxz_yR&!a}Z67Pv&'
        b'Zv$rV9)lz3cvoQvuC+f09SBpH#2fA-O^!lpqH+s4;zXBu^I<nxW5-{ThL6h!j<XRu-7-#HovZj^k#9+=?Y_(Tx4RN(oBpsNez9YO'
        b'0vMG%c22<$UuMa}COq4zCGx{1`TXeR%chGg6|PuFIP_#z^Y6otxE^C7KymmAPS7YD5ax{6Qx1W^=Z`u9u*xTMLr+syJ=v8xfL-vS'
        b'kco~u@4}W1<FzZU6W462te5)u=?SdH<F!Z6HH=lUGqdX&w7y>!7vO4E+yTr+782uEu4Fa)Y^uCWEPXn!h%lDlbxIbE%3U+{_jgK?'
        b'rZVtiHw>+JDjp-&sx9~rqE2M@O~CAbb%Qx2BB=FGTni~qIDZi*#|}0SOS)bk=^7*=vUF9&fOwB$?8M^Y%17?f2fFP?y16nO+A4MU'
        b'4laeRbl(9u;X$R0SFgNQFrX*QZ(t`Dp>Kgg51b#XaGV%p%d-tTXI)In#KAnd;a?70|MB#3sAF!|ReXO%+x)BP$-~^6Ea$u|`kqX+'
        b'$uH*{QxnLM6x5jOd#-W=jvsM&1H(2CQhSdPNA!~84yR3$_dh*c@<3|U#?&1j7(e+D80Jo`0WVA&QM9dlbwf;1ac8md_B9V%4Kdm`'
        b'u7p0jF(43@wcV}^G(aI%R-A)NCU?T?zCIfJ8G)+woRxVEI6zF^izKW&>l+^)E+=dLCXN?fX8sB~RBmcj_T?Q@OP;goQ}gYIOY#=V'
        b'm@{H(<L}u}?fiK5DeN0<ObkCaNO^z4gFEuE2zo^V30%<jT#3GT1#*4}DT*Md98~kZXg1HYE<w(}Mc?M25l}vlsH9G6cU_vR80ix&'
        b'S3<=f5mtjCC`)FOu)nHa$#<)(`#uupaAS1lVKr3YR8M<S4=<Fnnyw=RO94abvdy&8sJ@|pSvQnEiOWbfulG7{%A>GX$vZj2JXbN&'
        b'=X7)B^GxNRI`sDL^oP@T>a)Ak8}Ls%{&~^<VF-K0Oo=fLUKvyb7I%A(VKC$KMg578YuA+Gln3iql^EE^Kr~367%vmY?bq-%>WboP'
        b'p|@@brF7`^A1nCl#%Hfn<hlq!*(u6SQg%q7@!Kwk-iF1Db)514L9C)8g!XPs5c+8lA=zY*+JH&+y`~dh)g>!{E{nbmZ~2fMn2xG{'
        b'?ptLZm?0k)h`yJVL1AjBPb^L`X~&V|z)tAf$|keBDh`PQF^Q0x2pxpiGsj*YI4H8oeSJSAZwy65?|0#nD(%Zu<MY~d1foylBlT+r'
        b'8OgV1Nd@zZSTX-v#nBtZhTDZcU_1}RNwEu@+VM-$Ato7OK(pmj_+o+Zte1IeWFS*stW<d_b%mAKlhu1NcB8RN9Aw^;B`*qfitbZ{'
        b'pUHkk7PCRd&yag|(gP_^f}q;>B8}sb=oX)@=n(gO6E3>1i_L1XhsLQ!d)F)E$Q-mKWhr}C%X&u&pS@j{?UbRUY_vTvl&i|l)AhZi'
        b'bEuoQ9QtB&uF_H5%qA~S9B&f`xaAN1Pv_>xm99KlKFJ?Kd)^Oc`;>bVoZi2Mv-9nFwkPb5bW-H%!gy?{(U2B431y$B$c2vLdvU1e'
        b'S3ZE{u?;O};~mbU4iY_dJnU@^Z_d>%B~3VtMvyr=zMSL?x7!=T+`1Tt!LIj(9d4vQ7Us(ByJ4^F0(mp6NZO8XrY}X0H`SaF9fsQ}'
        b'$E43t@}YwgB3S`^-AS@z9tg9s*gIE#^!vZPCwx2{X5+B!HVqS;r6Y`k%;lihCiHiPf*igLR21L&fC77fk^LCWSl_I|CL^QD<&(@v'
        b'MzywtU`ZTA7>D=CLEiZ{*8qM^A&+OPYxEk&DFbnx13`ScpNZNw?b=W<<#BwkwJvO;bUj0yVCfq8b2Lxy4R=!*ASv04d0PMP5QaxG'
        b'0PojEjHj9wy6GRz8+ZK6vY?Y!AS*S;?88n2TEgD05O!R5Y)a~B)z}Hx+D8a%E;0pE)&Ise0O$3aXEyH-Tk~(;_p1tXH}C%WNgZr='
        b'tUPOj%Ian;KX>>A;+AE-uTjO5y66!=eDcDflg1NpqDWdp$}HzQlt@u%!1hC&>A)kSA!&+awxNYebpJMV7fVIoSc^%^haEu!?z4@I'
        b'g6OuI-oSebmHz>Z)}Z26&=cZ*$-nlnnhg9d48q+p+{;^jn0>)z)=x|D>8F*Zf#dIV3<&t5Fg}eAduG&$vty+T%f`_?9Xe?7hk!t('
        b'kgv11DP_2MCq|ZHXpNIWs>A^<h8L{7i_8v8XkduG?}*0lRgx3Pc)~j?tV0==uR|IF;TW>I^H5Bu`^m!xJx|(^{DclEpd;STajlZn'
        b'ZkH>BiW)nDM%>%()SI!*r-XeE*Prv7P+AjZdRU764$}V|;BelVn3lR9)^5C!uE6S<gf~60hFF|p-b}BbcPBd?+E!xh^)2K1>im@K'
        b'Y<hb<IdU(`AI|Qdh>*5Z*uk6P<_81&rLGcswVHNS#HG`LAG+8$;FVrqNV0U2qXeLPf&L756ljTyjgZy#^1fg^+0Tbi;%Vrew-@)N'
        b'C^rPJ3XK!pD(S$!G;%aubbp72mPHN6WlKUh7VZM%Q<s<uOX=+|$jy7`!XkS0Os-fi2Lh@7rgW8Z^D13&zPu!uJv0G`NKR7m4QaA$'
        b'K?pz@pl?cr4o4MFLdpqtx^o(c<WMm51Beh%OndrYBk#cuiu<aulM%AyloYyI0yDsnK|K+A@`{Ea?^7UR!qqcD5va`8fzi#SgQ<^0'
        b'9heGu-#riBI}gAJ|Np@n|H~~{+C|rHAt;5e9vS(&m>(P^q(0Dy>5%R(#{~mVR~ST{c`GM~+Q$esF0^V6$}|X>L%=i=%^3|kT`8>a'
        b'Nqdt0=`O?>!t`s8*%Y>h*EF7D!<qT2wV4+);iu@Su9Nt0R$`(xQC|DiR14WbQS+#R7>dfI3gp<1_cxKHtm{x#P!|2@V0pC5O2OmB'
        b'Gj5e`fd}9eJ=~?s^x)H|^F207TYlaCP?wdiuK$mfHUna5niy+}wq9e*{8z>TD4vlCMHkHnRk8NlsSkbAPQ}cla$=~MOe#n288Do='
        b'OLZ(WqXr5d%Y?lq!w038WuEjwm0hbi*~&5A6mmHfteRW0a*$d+79qT++F@89`mmjy&c!6KR2-+9zjH2Svuyg=JdZYWN~?+);#7s1'
        b'N}WMhbfujuVmRaPTx1NZ_U3hQxz(n5buVepGFIAD&Fc(Go1V)x{g4T@l9|$SWusl&DKpKiK5QaE$vR_IakQzFQ<^y)6k9$95~$o!'
        b'MtJ)%5?15yS+%zO0xS*YB@y!o*m#z#)MosELouQV5e@9R_Iu|UkrURX&tuMt)>z&4@>c7NvfzwTHhGW{UTZLKY8ZM|IkZ5DBYkBC'
        b'`Z%50s<Y;rT<5Qjd>UP|8Zs8x4I-9-;)LT`-wtawQ9~+}$_!Xk6-!Koiir{j63(yfsedz{v%V?j9a9MNA7%(-E6!T<6YyJ4Hody)'
        b'E<~NykWBwSJD?`WHz;s^a$UaF9`&eLm<Y`%kf(XIjV>uJEGe(g<vFsjWN6KnmUSl1Y#oyH5sSAy%Fki(+N}87q=VGi95L(uGwA~u'
        b'fB)<(rcvs2k};y9Z#qk4CC1cMG?4MEiy-IbV*hgYirUjR+%$UV^UgCa)y7p9SHaK8RjReCOZ$GZR>VuxA<+gVi}rLGOaLi#dAvm!'
        b'TlW&Wg!}ZV$6mC&*I7dST2WNoew4Br`Ldpl(oCJTf(H?E?2W*Q&gEme0i8D&*GV#Pxd;SM=5rBgU%n!JLkPUl>0OE05+lV7LcF2U'
        b'kYIVWlO_F>88sPdo8(riI!#0BU+Dzg$u!f|Jui0pW6|F5zs{IcySR&-YR|#WUEE1dm62{DwfuGMit8Sq;pR)}%`&c;tGT(?csn{d'
        b';f7ycT|bkPo1=TC?&Mbe{!Tx>=btt+^>|a~VC=T1Z;NX>Q>SY7!P;oXc2-Z&u&cg)Ki4SN_2>lMPp})yIX`nVmKdvGlRi_J|GD!M'
        b'u1llkDP7(<CC^RiN>F%X+Ie|GoX^v{lUFmFejPeCdAF7?W?-iinsu*eh$ETa|L#0mY?W7QHOw%Hta39NGr+3OYAJ@@cW9x?pKu$M'
        b'ucpYDfhyIeYkf^hbCd3qbN&*@)iiRh9^`ry*&J3%xBV-FRc@+2Az(KnCT$bVl6Wye*3sS3<&<xNe)pdZvdR9W(z_MA7dQCf?S+A)'
        b'vXc_nz5@-_ADEk@RnZf`cPa8sws6c>FPj`DHAfPw-My?D2UNmiCv0U&5T5k+-~pT)+p<u<w3D4_B6*S!Ohc?(SGUuHxg?ZL;&dM1'
        b'rs%Rsrgwl^S}nx~o%9<cy-90~^Dge><<)5kq<&H7&2P^OpfG9~h~w~?dY{Ct_Lw_Q;!jsR2w=LcsU>m!md=2s(|A%8CV4W<wW$-{'
        b'@p3das;jlTc3@q?cuizUub~r|H70^4UT$U+k<XBp0D^o)JJhD5cMN8B21ztlfNv#U6QTJ^waTmMWMh4DpNSv6=1JcfW&Xe;KvRm^'
        b'WsBHOhYV?H(Ji2d<ejBX9WO(*hrjg2xb29S6TF?^)8gw?<G+Z{(5Z<r5vHO^6g*o|*udLKc4pEp&vQHdc6q8I-a8TMp9uNoW_$v>'
        b'$p9GE&Loz-a?}D96>9IL5IYl4hwM_{kmtFEXJUDKtocRkSPfX;mbXh>r!OZ})_f6-8^y&%&HQHbR>5GloC~puu(trmW+~mGowv?6'
        b'_=R=AT6m7w8y^o8k@ekFOF{>tPfKD}22y2M+(C&M-oH&54^)XyT`1##B=PwSB?)_LV|df0-3|0mx5_V<Q~88Wx{9;Z=FgXB>n3i>'
        b'Z$5Rt?LAuCj)sNNp*PCecJtW7L*}h{4JyBhw3-yVpQFv0bXF6|q#;U99Fb$m0geAG+SFFc6!X<g@8|gIiMAlto7m1iX_YIo@v#Sm'
        b'Q;Tc^lDrhN@t>B?P(GCh^3vC`bjmJ-u)`nF7Zzh)#B0d<9axm0XaMX}@3}oVns91n=@H@r4!E*L)E@g~Sc8Qc+B>aXilKgWxx$-)'
        b'lNNi>_EmkR<O0N`HmPwS8RMVDyA|5UE<162ZIDA+!nRW_<@stD^??-PrYr(`6%GK8Y-hF9wS0AiJc3=vGT%klQBdd4Ab>yWJoL#U'
        b'Dn8aUeCSG)PaIjuFExSOB-!uEJ`duUqBEv#VF=eNQ+;Z)u+{t!4bv5K-e#W&%-EnV`aW>{MDXnNvH`jLGfdSbB8YOq_vobw*z||J'
        b'yWfrw2lWROlTPag)J)#}vKbpm`*(qu??@&ULEV`9Q(-=K@1eKPoE7+cV9(jW*~GG86S4afU4(2R#)|=LBhi%5BnOhoen|&YHEg1!'
        b'xibD!gzfBt47RngB}H!s&Q34Qet!Z)MVJK~PVJ9kiMsk6CzG4av`1n})gN5kt^$hO4E$+{JXx_+=KU+4<On@}jNllgJ@peyGO)Qr'
        b'6VMg_DG82$C}QWd&J&ZizNLhBHLk-ZK)b0K%2NWm)nvsF;xh`*O@1SlT`rZ?N@dlb$)ZIgWavBb0may3EHn8n;303&s|Y$~Ov}z!'
        b'y5`AzYF=(iJGU&Rd`Zl?B|ht(8KK=iWu<Sbw>dzOa_JHX=t;}8ODKn$dHd@-knD7SAn1r8@y(ET0@$7FOS<vDUv@1b7_8vVs5%P3'
        b'i;e{gK~G;j&E6ewq^Pv?)k$%*<}(qEO)vVjV<3hMT<@s(;IcO3GB1pJay{AEKjpm~XMFBQ_WZbo8aV~x^ni3adHu%sofpK(ei}!w'
        b'9@yw@2=FFled8$cnQStkfwwFWQyzaRp>$Y}qGL1}Z4#kV31uUbHb9>`c?xtGRF{(<D+>#MYPnGOkuF*s2CU+HSd*K6<|tDkr{r=>'
        b'xVj%`X~P{w1pzj(*tk5e;{5TI0o<hVL(zL@5cum!yc;R1A1R#Njqv9aT)<I=j4z8Y9on8>d}@sxNe4fAnXe?@R);%ueOnz=wRRn4'
        b'&khv5*x|Yc@&d+fMiuiO9g&THA^JYB8j@fsEKOJ{XK6>ieA7?aO-k6kBG_|pvckJ4`qdTh4Z#i$HroNjnPvop4q%!>lsNEx7-qx6'
        b'8!{=H)X+p(pkt}VT|Se_i3K&%t!B0a(B?{=#u1~TW8B3IPZMk&<zO@p`Q{x;SM3x~EOZh(WHJ$(@2S*5AvFK=k$J`CD7zhWCCZzR'
        b'iJ)j&z(CW5^C!&YY<4<Y{Xt<NeX&ASOzEmW*}Y0xx=Pn*t)h27PnWvs-IdDf?@CMQXnqx4{b*?weX>$@^Lf)Rr5os>-=1OZm2RSu'
        b'_x$ckRbk;e$Scm#)frI2>8cl@8H%8`DgUJ8GWu;nzKr<oZW9-XD#<8#-lu|6pfc4@7s5l`nKdi|YOa16(`Yf1zZ1~RcF<>XRX8I@'
        b'XD{h+lqa(ELdRTb5bLLx?ihMB(?B!*w+D545O^to53P7(aT5U70P5zV34Fh*{d~VRSh~@(VFi9qNGO0P95@dMbmzEE6ZSWS!juVw'
        b'k2I<5zwbcW)9|QMWq_RPD5pV-4(EWvFLVx}jMMnY6F|8r02KTDj_!7hR=o3*=$W*TVEu@&QrR)(vjTT^Z2G(L@D=+V9acKGG*g+J'
        b'ibdDlT&#s@#+O{Nq<07fI@rirg*%6+xbH{pt|@$mOq-(crzF(Ql$`wJ5EMPbO)qaMr*dTO9NIxAI&zQ$Ncc&^#eCJS+>^Pgf=pYv'
        b'Rm0?!Pqo5oD3=F?R__c+6<2l4smYgFHU{#TB>XM;0m4Bk*woToog+t4#&*~hSl!(~vniDW>z1}d+M%IYEsT3<uGx`8+GH$U{KlEW'
        b'l!hX*!}`Y6bQ!BQr{Fk$=)fq;VC)pMTY>5(v2%U>bJ=>q-W&*~-sYg^U=K|lx?m1sJ`jQ8%bi!mr49D;?JR@6GUTR2*PZuAyy>xu'
        b'@wY{9iNGp&6Lx0l{fodJi^ih%e%Zd~YmA%}i6JTr7j%)PJ@W#5tfE$-s6Hm(XnKl@|02A9Z{PFxcD6t&4L`og0~vVD<>rwaENKCb'
        b'Ql!ywjzib7F+))pHxc@`+K=Z7K@e7GTaUvr=bcM~_!_gtDzNFr9}v83CGcO@ImA1hUb6su{3MFU+wI3NUUjr&eoL8gE)EhVnk|q{'
        b'H1IMzMHS%)1jQN|k`9o5(MXo4n}{{4My|x#q+es%<)!jbe@8n-6@y?!ITRtoW$mtO(nT{YBmPbZ3QRO&ytl1gA8HRY;}*FpY*OPC'
        b'DeThS96qPU6{P4d3T#HVKS(O}DrT^Xia!uMsi<zkk*POGrZ~)aaZwWr3izy!Gx{Al$jP+l39mr__N{G1AFD?l10+6MB>fE+e@2Bu'
        b'H)EBpcW3Ay!w6W(l&tdU(S$>wK{~=|M+z=i@sk)eBC<JI<b|RW0w+_XQB$g4gw2;*g1vBzuO#$U?JxyV0NI(!Xl?t0?Uo7*eko-?'
        b')#m<?a5LF4m3SWAWJ=mMk3@%=tts{C%DxsT+Eu8<CgeaFuERT0P~Z8!zMn#uMDIvj*;OHEy3Nf<R48m+pQtPQ7^<v}Rw*lJ4>BlP'
        b'e%yQk(&OnrM!{EaEA=U1RYpO&mn2U%UrCOPiqZ6pZ>HgirlRA>;6w4=`Rx?F!Y?Nru&Z<%E;g%#CeKOi?#u(T>TozIxy&J_`!m`D'
        b'S?z9t-tasS8s(T4qAzO`uQ~fC=ll6K>9}|{=!qq9`rD<sCR21A9i?H*to9Nr?RnC<4OI@1HFYRCCN1kh`$NKI>vV1L)O1S!UjmMY'
        b'OX}m>?K9d(%2BH0JA5}I2Zbp%-g@F!P=U-TJM9(1-DKHeAsThQFjEyZgW$)NG#4Or8A=z2xZK7rXzNc%-_m9}r7hNCgXwCNdRFfc'
        b'JZbaR;>#NAQ01w1M_^~3jAV+C-QUJ;%%6u3q%0TQ0vRFQ>tZVoimu0Qv;RAoPp8GpxN=mn2F5P+EQznLoDV{y`K118Fzq>#`MWs&'
        b'x`+?>RbC=T-W44|l&8iK&q2Pv5Y&GWthp245jq_N85QH2pOVg`Q(P{|<toyjOYiW08PtD--_()Oo~=GhGRH-|qb-mraIn6geiZwg'
        b'cfKYf*GE5wE?gEi>a+zv0!kdMsQz{{KHjN-n#H+{(F`)-^6l;=oR(eh#vkbPmbM^=t+RY;!V|!y)RMzHc)%=6g_9W!KT7gtI1jjO'
        b'G}E`Sk=Wa)1hHLzC}@8bBe#@fTBQ57{0~up-j{-#dxpA>#0G__75m7^?*sl66)%`;WBc&;0ZJGUbd%o)5C?50a-0e~pVYQd3MAdm'
        b'p1ln<j!5D^7er~#)B5LwYsfidI)z<)eAl*mT;@<u+q+I_e-<X9@})(X+pFo->nuS*S@E3cnm`VLSQ;#QI%t0~C~XVL^inEX%6;gI'
        b'(p<bq9mVv>CNX~tl!A=)@uYKu7%eh~fo-McGE5Z?AqTWP!z~L6^3aE37EUNZIO}pNy=Pk4MBcOzTik<a{FJyCzw}g`iu%D=uIM7;'
        b'yz7Fz33Vlq<0nP0I~XDVUwnMYYVt12yRFs_q8sg<_JKAlt;muoKzPVhT5}cSQwhsRYtVq57Fh~|LOX4vx}U53N@i@rj4axu@m+Df'
        b'J6``<Ymmd`ppaf@>-J-p6*JCay0$oiCaQ8^slK_*K_-vQW1n<5lI@FwMF(1gG~qTbM~e&>4WLnYPI4+;iYLf14?Wwq9oWP|WI6_O'
        b'6LX#now>l0Twby>UUJBHc9}%cODazt)|>DcJAkjO%djsD7MX&q6Vryw{@-mIo{PSk@%8U985<}0HA5j}-`yHa!T4rv9JM3{gTfGJ'
        b'K)N2KYwacd<~A#-2n_;h$*m5BaZqI56r+ILhps*J->s7~=tyz=gK*GxDyGQ&CVi$-RqFO=7$jYxc-H4=EUqJ}w)otjX@Kz6q^i?z'
        b'uoT#-T-1LpK*bbC2w-OwM}KxrTwy*I%U)<bun4qDf2=8Q!ymX*;D`#q^kTcp+~YafqgvK8Fuk;=Bh(~%%UU@a0Y{Fq<Fv%7K^hHA'
        b'zt{N550EgPijI?M0gLO`jAAlwJjRjqnOGzQ%`xYLK-yPeUY-^8f5cP9@&E{T{KQ#ik3?_F<sM#HUlpp4Mz_Tx!q0nVx9R^HsB4Py'
        b'axPYprjUW4F#ZF`8^&HdQlTE{z>`F;>6ZK3^jWPz>e~Z}d=OdQ3gBf7{3<N6yNqEmpl`!WBx&-zBF`<9Sb%Z#0#ALbJ@+ef3ClC7'
        b'oU6;N@EUIsdYXH>cU7A|h=THOS-DWx5W(hnW4pNBox&!Le}KG18#~jVPx|H9X_RCQQ+V40dtMG;Hc*AK+;p<Sh>fcl&ouY%^!oxf'
        b'QvXwH<r|4s0X9xW=-JETL&$jTa=*GQplvhekyZz3c|H)PLM`F|*;M~eJ<%F?7SLBmkq2hRk>6^qBCNuSW>Jdg0I-d}UbcMR3KG%)'
        b')uhwWARcL7Mf(5j4|pc4mOT-0q@vUhf5!>gdDi60m+*aAOr#n*?JQaIEOv7Eyf{)Qk^9#Pm=its1&nousQ+?5zQj5U6Y_t=qJQpZ'
        b'NykS7my^uV*)hPTSE8V18rLDsX+eC&feWU!9O!v&vgRJ7zb_Eon`6$+oRk4(_Wz?bur9DWdP?7sGM+{9wB1h?)_y`VcC-v1CEmqT'
        b'pb5x|qQ;||yKoqV9EJD3K-qE(ua1erN;^l^7*YQlt)Q7_l6YlEq+bBCuq3r9B`Z-bvfmw`WGjkk1S_D};Vh<!{sjT_ltDV`h%MW>'
        b'#WYRPvSP=al69cH7Q2;rgRl8{a-n}cGnx<z>FSR!u2Ok&vD2>TlGG~b=qTC`><76Nr&maNjzPAv(V;_%aB&mq+tTRnRyT2V)?4N<'
        b'${`1>oK@ft*|<{bB(E6x9wrp#LX9~<v4+<3``;c{lrX8V3(zZPd>!N9X2DW}6)ADQ$+n-_4{Q*c?{0`9Fyh1Out)?64##7<=vHM^'
        b'f>O9~Rk%XC>x_5fez$3P*JYCVi&!k9W5&smYSEp@tfyr&D#(#XMTcp5RbqA?J+xBgU`(5?Mmy|qnl3t287cOk1Z-4K8QqxQg9T0+'
        b'F%O8WI=x*#E?CZE(PSZ6^Lmsn)7+%-?_!ky>p#Qqfd0P}(lq3V1r_}Rgk<E95yrX;oB{zc)yzRC*Kl#Gsvr$FVGO(Ln@x!vX~N`W'
        b'L>E(37GrAxw%og^<YiojQClgWQCZB!4df(iH^x*QJBnR)9wA~j{;ur4{by5^^*0Lkf-u+o{P9Km!yDKsXQrZpJgj=bNF1NPe*ko='
        b'&u=)WWOh34U`}%WH}&(R;f1`kbw>O0{lFNDQz#r|D0x3N+D$KINn^eU^l$pQ-YRiDiEV*`mbLCDHePV<)V_HmA4ijl+4!}6+WrVR'
        b'5MNrobv##u<r!67MkIb?IUs~JFo!M8_J8g7;SJj#Pk*~Xwx>(jo51+;B~y$o)3x*Zq)#HT#cSFhOt;+HQ$YvYFX)7=QpRuoY8r+8'
        b'q)A>M+cfDD=XoJ|7G2otePaJ_XUi@1f{*(2Tsjq@eB7sUKPmG*EzH;;w;B-4kGD>!OJw2@N-psJ*aEc<C|G&jqIAVGRHJQdO<h5^'
        b't>)k2GqH`aX-yZrF|Cp+cngOxSHBjzhM$j+fh__%$ERqNztW^XC8zx)y?1|tUoPWGnWxS?;~e{TEUkY~NKXtW0w)eHawT3LnT)y3'
        b'lc;`&w@PS~r^}nTXrCiwi`rfe3THm3y!Go!*P06pxBgHOZTk$qk`RsuCNfCv>Ve4_+m*D6r%~<vuc1N;Y#FR<Qhx%?b^Lq%p8c4a'
        b'a4J^qd5V^fLP}$^Owj4J+9+1>nr4_nth@%MILY_+k=xHSs&+M<IjU;Z9BUegrPKDEI}&?&_E)~8^|t7Q8EP(xx5mM~NHCkXMo3f2'
        b'0m{Y6^#7-&JB8=w2j&ZP@jPe42LWh%rr>bT$EJ2IFLDZnb^!I?DGYb8-Y4+5hv^oD-qT`>x4P$ZPz8UBN~hs}3ac6Ux5!dA<CF8)'
        b'XrI-n!CPGdOX+O*l<BOC5vt-J--C_})8R@KB|jiueE!6Ke@jfcsYomEDR&h5l*K``x^ZTaMquM2GVi09PKJe1>0uRqaHK40d6SJB'
        b'7UJ<C{923|XQ#PC9?p)<hQ#D?4!|Ry#NNA}GdoDxjIT57MJ@i6O|>)i10-#JLpSiQDkz)+;Q$`FluhqZQpWqZS2z6-@myTsgBHoV'
        b'yINa<qAuilPE&7_oTK~B*5^n4(7~)p`?$$}D-NIcb6gR6caP#ztG;qSM}F;c(As&lH9%z1chyWqmbopQVeVyaevmp+@uhg5Lc8(0'
        b'F9X!Jgc*}3R*Xd-w3&N`SWVZ<q|U0FOX&m}RK2J@JR0R&3ild~N!bRC`AzDUHJ9BQ?^|tWK%_K*NQsYzNoGS}@z*Egd-k{K3b*F('
        b'%udm1JBWuawUoWu#>KR*_G{RC2ZY)P<Gt20=|~-bYh^4D=q1smxDgm=Gbt(^o9*Jh0pX=#VcoHpyqEXk2}rrC-hq8Vke~-0<qvs0'
        b'_>1^a(@xm1*Uje)Q?ZB36r1VA=y>5`R8_Ei<_!0AQx3PzV)}qvw}>+^+`3H8KyvHuG-Yz@%%*m3U6!eVTem=ecAw+W4USt7t;r@z'
        b'?5nCcuQkdNIKcym7Y^)X?*;7Nm9SUW{7p1{#U|p5NBW&@`DAMDD*?W3kQ^3D90Khf#fUE@^<(>rSKPsI&;fj)5(gohsa^Z4345A!'
        b'ekt8qC|cK+FH3taUcbJrzTA`odab^^Eqywx#%F(AE2cekU)y#+g@-FV{~785YCq+AOribw#sG)xFYSA%qOCHC9QhN{zB;9HHpwhO'
        b'm3LuZw;*@%^wI6-$dNVDMb&Ra@3J<(K)B^qyDN3>{HjRIz4e2nw-w{LLzcFeEz4{3O<&(gm*uu?nC?!wbL@pOdt2IGqH4N(-JL~m'
        b'?yE1i$%33@c=}^oz}RA4XSJr-r0^woX;+}=)hnxUPQ3;fvA3mD&cBLB6#0wN_RTRBEVb6B<S$Ck%`Y&~+x=5ax$d+?6IohHkC7%>'
        b'6XEU0quNNY3HQWCu-k$NS<xYCAG^ph%v+M<jX7;r6VjGnvQb*iCA>qGq46&92%%l{Z<`~K+Gbs62_3o`A;$;ByA`hU|MLAb2-500'
        b'{AqnqM4P*G#t^_mf#fze&KSAM%4;<;%d!@pYVnw9=Sw1#7!QitT_`ZU4F@0Vxyr`w)o3h^78pk>)v{L;!)nYnvw1gtcdRokMq<X>'
        b'MD50FY+OLmHgX>0sD0slKn|4&uNAYBn$GBVEvpWH*VSm)Bv|9)XMk(gZ|p~H5i0cRO}iB@V4st^aKre!Qg~FHcQ?r!h#*BE`3asv'
        b'+N*>;XCIp+9ZH<d%F&Sz#*foB18kch7EZYUfU^50#$TtM6O(IJAK!B8)Ll#1o4RjL`ab?+A}CMxryD>?hy`{p$)?O?Y|l?yS&h|!'
        b'EdOl9-?J$T-2!V)IvB|46Zbhd4u@!`_J8_;U9*pm|3q6t@SH&kd^ipBt4qQ7PX@6)l;iXgqrx!XZsnyz1qrd<w^|!VCC4c@ziG?%'
        b'SvjY6Ck_OQy&F-;+km%M`)jSNJbRwbQ>9BP+0XE!S3S=+JQF+Ar1I1aVX1j%_@%n|HFU*|AG%+9M#etxcysaU#t#CApxU6~JvkfM'
        b'_KZI1+<ulHz2a$YI9aFK?HfAjQ$6k5^>p2$?=s#w{mj(h37fs6HPG3*khZk9zC*#!z3jrcg-L9jSAkbVpt*JN7(B$_2k+%(6K`p0'
        b'^?=evp4PLio;v%a!@0)Ri}|WL3eZ}rsl)e@C;9X4R<24jdA35gRXZG`f2Wz};xVwNTG`u<$VU@kWW!19l%eLK-JkC~xqIvTHLX}S'
        b'x(B`8oWJKWoDL_BrgzH^FIF^u=TB#LH`w>ShGz`xvsI`OC&M#eNyLAH>9MI9zr){iW9h&{xNhT2svxdO&T$$kVtnfnMaw?###UBM'
        b'$>aQTppXn*la3|*`G{J^rYk0GI*l_&zLR{RmbS80jU@i8XEJ!#wgyUDkI09G#RG1}yQdkS)*(rsm2$*VBwe=!gnXFg>TYbxT`HM!'
        b'k^T=b8+Ettj_a4VvguF;O1yTi|DM*cd-0g}FBnjx+v{khND$(D0EYzCrp_8z(#qN>2MuuW5yU}UuDe*ja1tbBGdRxQg5${Yr+px8'
        b'#(>nkpRik6%kF6P&TTbey{SrVN=SQwtl3MLXcsvZ8`VLHdlZFU`MI0c?pntsvg_UKpd#@57WRPGg{N6>Xsx1)Nd$^Q%@*W+VBZ#b'
        b'cFeb=^8u6ws>A)L`kd!^rQd-lW@=GsbKtFgYl46tWsh6)rT00EBTp&Vw9Pw|g#{Ct%ruIK(-2d&wHYfI78xe8jcbdB_pxb(OC}yw'
        b'XOoiJwjV}EVJ=*o9hw+lklKC9dk%w1EijtsDg(zQl$Og(*6QuL6uOktxhVyxyr2_ou2kw$bs%5sf7u_k1G{0sFJl4E4@10rtE<UX'
        b'_QQVt5Boo+OBfSLO_`SdP`Xk7{eH?W(-1O>l$DvA5s_G!I??n|(_56C!Qbl;=`Ld^a;k=$M%f7iL9kjKF`LbJhC#bNFpyK~_IS_i'
        b'*Vrk8U9KS&g{BGb?aeDlmLlWMsdEUK#!kN%TSpk|<P%KgZ6xzIlsRRp*_xsKac=7GNav@hP?>1P=O#!df((Q#lOT{xVOA%uuunNv'
        b'#==M{34A@+YsX`-f|#Nq2>c;VHt}A}e&z!6@$pOo<q)JUQ;}&$*_5O*e}T*?i8%zVr19g(=Lp#+M!pb@%|DMkC9*MF9B8CLMBeWG'
        b'JLEfNJSq>q9sh345qa>$uP0ws9Zeh<{k2w0j#!b;Niph^VO96~AQMmJ#Zt_)V4j)ElLJ;rewr_n5KEHiaC@O*BAA*0<k|ggFf|cM'
        b'biWeR#syc;3^LP$c?-goz5r;c!Mu6F)R}eG?k-jltehFFObqPa?^R$B-uIiji+Q)Qj>80#Avqxtp2x?Lfm3U3G(}E<r9wGCDar63'
        b'x`JI(0MR*FK9%v*(w^O0`MmiDnzm@!z)#J!-^vG4)!v_)u))%;c9w|G#9^mD;gNAwYWF}i00y6`WfMKk4gS3OOd(_x{n!3NS@d%v'
        b'iS!c&heG3+!jy`Ssxuu^)2i-=CuErj(;EBKOgo!nS5(yfT)1(fiY{d^F+U8W<5m@7*N;;(2{wmNY(pE7F%i{HWb<oxI;JY+_isbF'
        b'uuRxApzlZ3Y%N-iX*?uPb(5(3)MgMsU}kbKZqP=sOi|(aIatPq7+3=U4uAq^<_malMv2|S?1F5RK{=*vP>(FYc~VnF<IUN80WwV#'
        b'J~iRtGVnoLRJa-UDc7t_%vNP+9Mh!CgzjM^o6TysDPJ$d2N$PiE7xiqQ<)SIFf=%(0g494RGqmXyL}>b!`MAsGfVn7l<NFS1U@$f'
        b'%2E#2nIL-KX-3M4!m5c<&03v(EsCE2>_#-m`^K&Of@ppYL1g2mE#-s^h&)@1iTsn}ztOm_DN5r}0zbD0XdP2I;}p$E@m@?#t_V<c'
        b')7S1KC{NVFlP!9lOw4|H;++7%31hAUAidj~qMxfZ1hqegy<;@+@o``~0GOGF`v8js>Ad@XLmRD|*h$d3vbCl1Wk@>#^A9qbhM*0E'
        b'T$!7QI7L%GfX`KA4@`U)fCjQVCcO7ewm}hcDEVFtKtBiVH1;z|A}S{sC4=c`<Ze_S`<=Qz8R!-`Rn|8#zK7iM`P##B_uPanQ<gVs'
        b'F)PhMTjpv<7gAGZXk(@xxhKd`X!dELcL*&y4NbxXyc2+)0Zn+bajS+H61oHIG@C3K4MZ3iz)<Kq&<3nQ1F1pe>}|@~RWvL|cLu9H'
        b'9Jk{%<<M-YU;zLWJ;NX<+WiQiQ@tISraMQ05Bb|cIm&>hfV3-oMu3D$&+o88$<n<;O%*_Uu2^}HQq0)+7#pA6qYLIJEdOY{Y0Otz'
        b'NtE`L0)E*PeB=sm_}+ajI|&jPqRt1Ti+0*cvng@plN+e<fh_^g?(NFTZ{rMPoDO9eNHzT8`vDA~;T#jo{@S=9wvd?^c~`7DPc4ye'
        b'_y{_HeQ_8_GKWAY=Cm$F0aVu1kGm9{fT{*N@ITgjwGp30-qBLHc7lpQFjYu~9j_W6Hy)v3t!{~1jylhesvG;EV+LtS!MtsUDYyfj'
        b'N@ADCY<@!N`c{!cDk)OM&eCNUoLXXHZ;Sgh$Dus=-#fP~NzYj#d;iZZJEnAHkxm2pe+YXQuqLjwaeOkFgd~ib07eAtW(EQQp-Zrp'
        b'%i3KMX}G9epfv)vy95iOUB6YN^|Ev~GuUJjP?7;5pxsT<Qh~}A(u;WETfi1Ag<Z8bYIT>|WkqURi)blc=6B8nwY%Rw|Nrywgqbtv'
        b'@}6_v^PcxT=e<lU!51C+U&&|!9&@NyfF~o1(vfBl5|Hk8JDW?v9<b|e;o}%0KHvT*0Qdd<d8-fRB5^yRa{bOl{Jt*RB??}(prk~|'
        b'E6<^Zkh>+}_{K7Y=hrQO0fbZD*vu<N%+IsA0D0m)9)&}F0RNel%<?j%=#OhGpMn3DOB@2`71yhx<+Usxqyi*mrA&N~i^W=#Z;0>Q'
        b'nUh;XV4bwPil}s1Wg;T(AV~(^KR;^LNbd2X4;|DD)apreIXrtdG(&3>5$WbEx46<rZz$6^QnrwfB@E9~uuf=To*5(oyDebc9a;4W'
        b'SS{Tvr2Y=)WEk*L;T_?m<sKidUFFgp0|<nY!IBtE<d0e9OlZd8^)$H{^LvI@#bCK)V*VR{$YtaXC|vWGorPFlsmq^@c@$*93-KIP'
        b'do^UT)tXwpKPq-ou!Qis5=pr-X%^ar!!{pwMPU9WGf^?==Jgw$^8aiz3by&18=%R)A2*r(pvkCzZ&H~*7l|8G93g~F>iH)5HWjY;'
        b'|J&wu*MGDb?e8ZahUCYME`88w^ndRss5t&V+9al%a0yGs6DJNhG}Uu*%(r~nE~4j0X_I`~?}@h_q*cwT6R$Ew3H()Q4?JJVr^z7b'
        b'FZDrOvC^|bqU`{*QI@#xmFxegiGBm|#v{&G4!C>dK(^~*>&-_MZbv2bu+PZZ-yry6Gh2_?6rM&G8^3zanZj>Yx1PE+2hU&=P5xdP'
        b'ihAk~_}r-a-S25~0gSKyEPvkfd;jmh!-9vY`)B6toN-xc-~Hz>_3)3<Ke+b{Ru%MB`pJwtPIZqDht^;xW^kGM{TXP5sQ!2c$9=E-'
        b'q3^H?$j)=+2HXfp^16kkfA$ysQ5p&)=YLNFMaN&ipH^E!dsVpIiUx!7$`29pB)4J|a4+7IcUsG@&bh%@{spwFO*&BzsDG_j`4U2V'
        b'grr+y6~*Fcrw{<tZy<Gs*1W4p0z-mq_&Rm733?`Z{LtI;NOvIkL<$UiMSxc~j>9;e(8Bh}E#7DszQU8cLbw+5RvZA&y`pjT!q(!e'
        b'UY)_%0&P8o<53HZLw7;-#>iXuZLshNUPtfdJzH`d=ihJm-@ibVG{Sm>v|G}IYM{#tS?OE1uBH($HsQN9BsBIC;9;e2-nuYE?7Ela'
        b'_qqd}B7xi~GrTu*n5{K=#xTS2<HdReIMalN01-bvyD2o*nhH7@iO0o+s_+z8I=&<(G%?;A<NB6(*5ySJH{cNq?ivv2w)Dg;;#W;x'
        b'w{%Vcr_aR`JH+rE7a<$;$2Rx^hG1;{;FixV01u_hX72m2E`3}ucYbR^2q|2BbP#5CVvEWjr}A8#f}WJ|yBb!2;-SdmbcFG+=$^I#'
        b'Ub@>uyBRyp4kT*MwM$|{+hR4T?V8vWPnioW28wXaoxQXAJ%+h^JJ97H9^mNs%)MtY6+QlE6QUI~`LD#C|7uzh>XW*nk1uz-r&nk;'
        b'PClHxc^-AMkq;N~6h0d8+>!`Qz+~v*iWMo=Nrm=WBVOPQJ{z!E%u4avP4`BfjV#wnTas<x7;bUY<wob9T(ss12ekB@S8AJzpHSx9'
        b'8JvcL<c);!JSmsU?@m@ZdnbO>@D0cNHp8(I!K!Y(NuUm&#>vdESm>NO$?sH5ovaoLFz5zd9+vlcW3GA@2uv>^V#M5%fZ2p|W2+2C'
        b'0lL7WpIL7Be4C)L1v>X`^?eWf-6?GC`F`*=SNgx-cM1n*d403LG=gFDYP6-3-+SE{H3G5UF}I(+-H6+~n$>v9A?d=s(wn55db82<'
        b'Y7?!IL;Fn0eT;)Nrn8YIY3oh}jLZ5vD0p~wxBOdtQvTjy^;Aq~#M4PJp-WeT_1EN@PyGoDG)jj`GAB^tw=GMq5eFLQ-0Gt1CcY(}'
        b'YXP%LG~Q1;GVwXFvBhwMKR4Lh$OlLdr1mv>Hnh+h7*mxDI=iSOkgzp^t^PmS2e|O*S1c-cT9Z;_ZC22cLCP$Y`a`3~I9HZN1*`Qj'
        b'E;$*gsPz&%8$Ed~{~n(ew7I>}v%2L$2-+Oj)zYoEn9WLtPsrqjuKGq$kSX_Mv<!!WpL;Pab%<_5BbXdAindn78takL)AtA_8MSse'
        b'A4d)FtU(<LW?#AcE=U6<jl1vSNrsz#pFOn|w5Qq&=ohLmM#4qb+Hk8=&?{`c4W<;%F{oX==~j{(0ehl5vc3}?`~i+t8M%=95Y8>J'
        b'r4cXEB;BVMIAbi~@HqABcc`*PJcohTCwozz{ebucsIXEf=oNsq^D#HPxku2r6d7MPbAK&^=9Jq70OiI%<c2%I=jV_S8CZaMd=}ar'
        b'Y9{3XT;tSTus!sm<D0(kMDOu7kD)46Wi3mD!)e6x7nLVbCmTWY7bZd8*7rCtGQ+z&h3by$39^G7Np3EgmE$NpsHTp>d_YDG`-q<y'
        b'?Q|m`X-3K2)<52%UWQy4wX9L)Rq?%Hg?Q~QT9|9L$*qh3w={Q3X}^W{;9>MiSL=a0;&1);R`&4+v^eKSbUCi{#{K88)@kkmUAfN9'
        b'(USXP(0cO6V^FI5?_<zf_@gnP{<rzQEirMt8DGqwU<NW}62X#d*GPo}dOWQZ-{RNmNBg}RKK9trM)zBg#bHCS-`wsyuIOu)18x8&'
        b'6wD>Nk7EOG{K4^GKeb}MH~!-8P;@oR-R<y`x8S~A5OtvW{<R?QGc&PL=@a83%R+<+>MK=jX0lS0doWfa!E+8trCtrZs$L^IQN&_M'
        b'e9pGl_a9mu#>OmzHvB=GH?@h`7%h1ASei?~gZO?Bc29M)J_d%`4qvNBk<3TEwHq{~?hnnGtYdC0s+xVg7p~UtIUsnpNn*k<JRHo?'
        b'oX><#w5B`O)H*Z4m`H(S_!ub>4Ewb2>`w`v^Y@9EnEl}e`e^NoqHG-=zD5*r@aa1*%Tx#I9gfP{_t}Ay?n#y7tNJlV<<<6zQv&i7'
        b'v^pX)5Tj4n{i|je#@lA1A|ReIrmN@Ix2e~H>9kC6(F4Kk03TX<h3E_^2eShTg=d8CAOjHbWiC7eY8$Nhyi-Ko*w07&s7)htknkKL'
        b'qj@KE@R0}dP2|P=eA~_#<K?>=T{8Ow!R)Uf;|?FGeJU_x#itb+2ua3K0@!r!+bZ6)vi4aZjbtGDcLf!0ZbuMm8RV!LSiMpvpl-s4'
        b'3Xc${ci2&JABUrG7wHs{CPC{v*JHv^gBt82gGV_gPqV1crD$P$q@AK>6LlFDbeU>fCi23+xso>s<CaonqgN^+C8ApWqDj>9FfyS_'
        b'en^x&iHZ{t-m$q#g$<YBVd-(z%97iRj*Jx~yOh+&`+47OJg}^rYYKWDI=Q9(29w!nZBm)G*~EW#nLvgzt>1W(h}{n@F@yXzPUzsr'
        b'9N6nxd#)=dr<DzYd;(j2DS07ksDV}ry%^%2Z0)=S>jkg*(OU4nE_flR8V?*Nzy_yWJC<Lj9pv4=KZ60fw|dG_#jU<%_?_Rjf=X`e'
        b'6!>@pHuX*ob*F)qgyIF!v4Mc^0HT$j@vx!`i7)ok=$_iso;8iQ1TY|!r161nz_kWCw9#5Ff;PnMH>kz?X-x=!Ve0iD)ZP8}>>cv{'
        b')quZSHJDS~Ch@7G5ZO?Ag&Cg3s9}!w0R6kS^WPiW*zkA%x}%U-U25JYQ+j%3uDkM`N5pd*4)H}put1!P`sLFry@J+<ZYjg=;?UQ-'
        b'HDvJ^s~Brjv^d=!vrvi!%Mfxv07J!QWAtf38F@h{5Csb`1c@Wv0=*lN3v!^){%I7fQwHs3kf@U|t^xFsxZHzu5AFvWirypvqzy23'
        b'LV*N)gx<|0O+kvWql#nQptayYq{9=OgM~Bf`+_pfKfMIzBSa%;`q=D6Vd?dI^pVQj@4qwF?%Q9M1Fs+GNX5E|1=?2{Jc*4-kwLwF'
        b'J9}E_iV6LmdK~7Co-L(?BIAsR6*iMAT`|oly|S5ghk&_>NmWq0T+qpq!|9KX0lh4Rdk1dfQul#s7-tp8JS#=C2XWWbcS_Vhze5WT'
        b'4re6^U1e{&v|SB=k|agK>qG;P<;j)Jma)0}eUAX_l~!~yj0XKH&Yh+*o=4Pacc|k1UP*K9ZrCH9x1#>k0Hh4R4nCB&p$uwtX@rMK'
        b'Vy%nU+BH^k#B&Y)dl#BaY4hJs1!qHUS-S>i4I*+LWHsH(8j0vPAaqHD|Mo<i;Ue}l=!M8Z?3^3MKlh}&2Hb)(y)d+=?&mI=T$bqy'
        b'&^_kL!t^D}cw0~{wVzyhnONPB<d*m~n36XK>(4=7z{!{lD$FMDUmf_suVCpkM?LJCQ+VP1Su{lWH~u*s*SHe9DrpU(EI{V`6(%*%'
        b'ngIW6=?C}j5viZJ0CvPmhClQy0x*U`+hcVD%pL}6uPvA}eDd=>N>}&8`+?}B{wt>qanV9F>2%0gy+SMAKgK8=%gpvYLZKiSZ0f<h'
        b'8IqzG?ZkvxU@vT4GUZOHPV`4f;@1lA3s5rt^{iIl(i4dDMnkqROOYL%MPx_n?ljRDI#!@4dXhdJA`~I;4$lVIXXt<VaU}0*6D>jx'
        b'YN(|R&Tj!Dt8J6wOQ7rpk<|zJ=2qpDv1pFr12qAb8`NN~Hv7K<h+0FYl#_QzP)mvKA5GfD4fv9zNNpQ7G7pFGw8Y<W@V?$J=XsD$'
        b'!MJ6bR?Np217W69K<CX@f6E;lqW)gb>@3s7g3nW2?fLO%Z>YCUcmJ!wGufa%!8!lh<i9P=Mx4V<;1}8tpK9{F*F*;*&i9%iL_=n?'
        b'%`61y6DSa_hP^a510sOfj|o>nx45z?d@-+HX?9nNFLQISsDD3A0$73*NtO1^CNgh+z7W;5HjKTb$bT<nY^{Pg+*I_GP$aO^fa60!'
        b'XU9cT%CvcTZ`RZ5)tAf5N{enNbMV&E>F(nVp1(Adc5}p~2H(P`y=Z)C!ld^NZk+haCqqu>oLgAjR-~@K?NhHN!WvY^<;Kq?ULjhF'
        b'enkpV?f#}Q-rFw<Esx}g%rCJB^~m_$@5GCNEG0y!+9v28+1ug*WDWESA_Wr43I+c+6}5cExg>3&&8SPmq(Fs0fL-lDV=e{2066`7'
        b'z}&a6pb>z*!fd2<<~w7~_0}~vl;;KG1=HP3gJ*BU_^V*?HhD^$d?W(HxNonAZVxbcn_M4AVt_~p65-xg`6C-@s;sG3$Uq`Fr=|pG'
        b'1T6^x0t8ju1h~4|3gYP|$W+Yv(V<o~_&KmeS8%GPJ|gYjnseqh`J^Z-*>j}u+6M=`AMl=_p>yaC=CqX203O^t+}C<z(lE`_o$jX_'
        b'Jo={AX0G)T<dI8{aMX@^sCN&sxORZbsrRIT^(x1g-qTAH2(*th#m}S&l`DgF@l7dDW<7;Vk{eJ%Hlo!w^&|l%J3y0{T95B2f4)o^'
        b'SOI2cQ9AO1XY1BV-9rtu`(YN#bu`JF7NLVH5bEjr=;aDlvus;<(~iXwPgqk$`7(Ahf(PJ>O9t<B1{Al~Z;^RaO(i)<X8>(l$eKdN'
        b'ci;9z)tAIA=?nneA5APYErhENhNm?kED^FLU`Hs<Jnz_~3S{0%LAP#HZ9|)ii?NbS#3XInrfTRE_Xf1uIe<fWp!)BVV1@zez{$0M'
        b'HPFfLdRYh~b}4C-oQW=9&YBdoDX7F0JpROViDEwM7C=Rmy!il+P2V@h?9|d&uGt(_wo~KlPxQKFtN|Hso6YKH&gxC_tS@MjLT?I!'
        b'XBcmBSK}gh|A&AVFd(4e|3ECKFk22Jd%YM@J|Zm<BKZJE%M_b+U^xY2@*<rOlj}Zh+`K1Jg2+*TuIq~6Bkv7nbrPs;nIbJO?Gd3!'
        b'9xU`*VB%oyVZxP&`mf(9(`M9>H(DQ__WZNHHvkVV-OVNGFKf@So`HHYQto>dsvoIOOyiQlPq@v`1{;u~r+Ni|$^ufS9{SFB{s+Su'
        b'F6H^M$evC?>0u7~p@zPX-)tQ7DV)9RF*{TVmInGqk9wtkK$08tw61GFG1RO*$p%XoKvQ&hx0JvRL;#F*xXi&)!F_#Oav&5gWKA&Y'
        b'j|hMw^4Vh@!8!as(vR>XD=Dp??G&^wzfX7o)ghW1OWXpmGL#kYz)1Z^Zi`G?*9hc!u<t=-<NO>jY`9(sN%n(xNWZHZ^?>q5>5j8N'
        b'aMwp^+ax^whL*d-WsoPcfZYiaFZHqSl;`h)>FO20snXjip#%psEdy!o`A+wH77r9+(xcmiI>e{Lw#bfz#pjEVBMYOc&5e1lviOpG'
        b'HK==J9&};m#&U}k)Sv6UiuvXad2WZwn>Qa4v#&ViJ2N<(E_9roiVlM@R=P(Tz}v4m&@iaxp4xTpLP+NFqgLlWDFP#{6a@$|326Gv'
        b'dkVhvK3LlFH_j(SDSiD1OZibvLG_Y7Bp?Rx<;X|dptG@K9#30+SB5H;)MxFXN+6LUcCz>^FVK&B0QXh;0;lwSOJuX2)Ox72xD;9t'
        b'90M#fCYz&x&_DKf%CN5ihyV(>bI@kpRu-f~NTJ3L#0CQp22PWBT;It)^`9pV6ZiCdma$&)3BY1p4Wr4_gQq=v>Zx=H1{KFv9c6Z!'
        b'o8{C~?68e3S;Ln9j6alrs1dxt-}0Y1mjK}cxq2QC^JXJna<y|oW4qM3xY4UgWJ^{%W$<kgcw5MpCpzcDw-8WlAth{dNsQ84EV-pw'
        b'LdhHHk}dw2iylOavv^Y0_P~srQDM5N{aM(-D1zG$P^)%;NMa*)`%gN+Zm#=gzaB%B(?VT5+y8cbew0@C?S4R6OQI0HFch!Rzk4^`'
        b'TiyCgXyT6IOFG4KGaskW{S?l8dWT%a&ph$ve$#EX6YUkZ>Nv1}OQ!S2_6vnluZXwAAL1f#|3J5H1G9?7Pl?C4ZJ7WodIL&-&gn%c'
        b'^$^P|)C)0$w_cY4oYY6IPG2cfVp5@y$BPU_1fD*u;t_evR9RRLboJVr28)BH#-36X<x@g_%0#dd{ktLC-eN&ju;R>M46YmhiVS`n'
        b'ft8fn04@2x^zYMPKWjlP$GOrg*FAq@d&Q-Xa=N$or)&o@tnOdVq?30e)LD;2geA7tLtFT6fH%Sicr(5Stf?s)!Z3$7&P&cYyjgq?'
        b'Z_fCArnl|)>tr38`(MlY&wPn5*+mm5@w#(P&bP3D??up|`~E6G+6YL?)#Tq#g?r~!cFtc|wGL_v+n{4<vX64?2gz|7cxuv2G&-%R'
        b'IMK_}r&avQ)A)5?siQ2d$rVa~BqZZ2glTWF+CCQS*15q@=|VpD#lNq2vh=8cl*A+G`TO~Y|9ksef872HeETnh_E-P7ePV+XMv&29'
        b'KdR5UVLw1KS%Ng;oA`MVe*%2np`Qze3&0)&xjk!d@WAQ6^z~Jq`UQFhh8{t}JAk+qeq4NG?p)5<2H|mdy@1JErW<=jkp}&U<FB~A'
        b'eX8neZO(qTd%9y;k`TcUBp(+Ozl6h$bZ74GBF!L+xueg~;RW;RezmeRbyj))4%mhgwPuabaAQtZcKrALJ_7rz(wIqj8!3(H5fQ1d'
        b'YMv#RwLSu>x(l^+39|<E-;lt%UYx57Z}Ha#IM=!AR1d0)IffC@pe|6AI&oGR#`)_ZNkn|l9_PtPYV*H=^`N5pa}|M!VBJz87|eti'
        b'&Vl_N4y3R^jHV?LWtM>A9R4^b$)ghDQ`WCs_alEP)U5`s(0RX;xx(3)lvH{^0~(~xI~|O<O+$U-=wcNu3=r&lPD8o=r%r$T0qF4q'
        b'u9PPy{Vt}!qJURM?%CGwA+N@(TOxjV9(1HlVeT+rgOQ5*RPJf-kieh$K0FCO%A2CFSA#xl&ozK<L)?o5P~!D5Zz{B(H~^@<(C@|g'
        b'HC_(az2Vf(I=xstEetv2TJZtRGc9cr>Msy_&=CN>PlH4FIR_L)v3R{O1oR@)6~2nkyewFVf-VeR;d%w*%2{K_Ez3BEj3p`3w18c)'
        b'%*^>DnkJ4osIG=sVPG7D)I1%N@^HiibncH4hZ{5~^?Cyk2xnZ9nC1m+D0-+_3WMUT<Q@7mDTDAV)cI;d#Lix6g5(AICj*NM0+~~3'
        b'Ap?sG53QIF{SMV=LIE9b7Y<Hw?E5n~3ccCh^G!&x4XVWHz?JFguw@+0Ov%){A4+~iMC@$<*kh_~$Pzz;bz-;EsC^Ee;sPe?7hbm<'
        b'%oA1X@OuM0d_Go&qe(?*Y+6ji5^otI%t8Ii=>@Ww{i6IZG<o4y&&b-+EMIf&j}Cs%5x;ZbLcggg9)v`~a}>*UKb}VLq1DdvG2&Ju'
        b'cn^#Z_7?x9LbShWfbNm=QNs%4X31k^Bs$oF+)P@cErsdIfqDLivLICa2m+`iK-xhqQkH~@8;~+RYH2{Utxk{u8udV5$%bYGXJS$m'
        b'WhLk!i<DJ-K>XfGqY|+d!Cf$JSv^w54imeanxJS<WfNkl;bY99mIFvk$`gD*I!irxTw3Nu4SNw7mX0B|I9J4yXvjV9Pu6yn9!Ma)'
        b'5pfJ684}M&a2Nz`kU^q-sO58xFah!wYyd)LL>5f9gX+Q}G_dBEfOz4ENZ}(fqm~aievw6#!(1<cT&S3aW?4U<BxTUd)bcE1`5!(K'
        b'CoC+6Vc`BJ0zxQ;QQ8a<a3Bq4@E95a`)2qZ643_Zq#WajbSH^siJwBW3mp-s`R3{)Mq!(O<^X{rgQ8%dnbpXk5kcY^I1@XNn**p}'
        b'JK`PqV!V$7C=dA^&@!AlLj!2zH!BKY4=ms@VFe%N??q%q77XC_Cyr7(wSRSxnq;u8fW{b@({P#t`xVrNTT$+ZbHz>=j%6Q5{Hsno'
        b';GjtwWL-CdivO1*NoZ`LocadfG$K21Im)eoeH+{Z8q=)c=WREjJZZ24)g19jotMlcd=7vM%41(alhHqifCaE(6ar|40RacA5k4B<'
        b'U<F5fP}g>jc#Y3IIRPD{o~s9K_=y~Vowx}=Sq`>5@j;Hb?qJ}J6Y-q`@JVyCO}abc7%@QbuN)*Qxyov9I>Z||gqQ%YQo}8d7<bU9'
        b'l((%WzI14UEH^pg3-CXh{D^p`PW&WHzv$5Djr!ZrJ12480kH#yQc$ZVHDP|`b@1{N@B+inodea$!~l){1{#owzXTaemrOD;vl+8|'
        b'49X8V7@wKKEay1l6nKQY3h|x;OsVw}Djwy;m%w|!Lx?60ZUjZg7f%Xhn7EYl*z0juT!(jP6d;$Ut}Z5poFn0z94!o>;J>f?cMATO'
        b'I(UMOs$b?TzvIuQUk8BaGWiBQN3?@6%O(C;*H)mZfaV`9FtR4d@`^*d+TkUWK}ImSntT{s%D@o~b(#vekrLbM88n<3d<Et$t<&n}'
        b'uwdg1YFPoX0FN_z|1p@#5zo|V)8;<zm_ZGX!jH<SVLZ(80!KaOASL*Pd?K$-`%E26mJ`2a;htne4NEzEik9SR_c_e89Hxb$;y-d0'
        b'HEb^tjBBp=C63ry$CUUZr1CK<)H^vaB2Q1hD8rSwD3i_B%LM7h>NO(hs$ODkc$CPfixuVvAWu)l>`z}YMGkP+@)fGJW|OWS$h5_4'
        b'%{`*d0BRHt*M+pUh2vdZyU=fEv__;dRD-EDvbTwp`T}$?2*42!9*AZ2doc})FUIjLxT7smwW;1+CRaAzX3%x6hk656d7B0AE2xuo'
        b'yjjL+#c+!dm4f|Yuh?*%(|EUFgSWYYN0p_w_@<A-Y{v6<+ZF=!2Hds3U#WuD&72<eZ0a#tOv74ICRlMpIfa2v1_Z9XrdCjj`XX`+'
        b'`Y7x{x5mH&r`+gz>NQwbZIH3!&fzp7uwH{6F6lwRH_GkrpN6dUwF&sxGhzXP4DW%mgeJ*y1A4)vo`abpE*(mmczOyK#e|56YivG='
        b'Y@1=T0=8fY*wu4hcRY1{A8$#hjJw?{T;;`u)CeqAh$fZDk{hDQjd1@F>ZQ=nd^x(V5r?@bGt8q*ySoL|c%gHt*w-w6-j703^T2*b'
        b'p5*dP7}#xZR!B&9%sXmST!oaaM8zy}^T~v=NObU7<eg>c;0~lL7!^MZ)*)MtLf5LVMU3it@<y;u;g}de1u1UX2Gnp6xe0#lNZIy}'
        b'#+$Br^Tcj<WrSWiw3v9GRXr<@QKFV5NKH51GH&LS_D6&Q6md_g4_yQO>R47Ti+%yd)x-my31Gl9)2DyHW#;y3x4CjSYpbnZ*^`(&'
        b'jT+#QfW+$#Zmr^!Ek6ZS^uS8K^RZjUDlZB~M4-v>S3r#=Zf+wWZRa>cCW0)Q#v%s9kAt=&!qmIC;iC8oiw>%r3Q#-{!qE4_Gcu+9'
        b'E_m0-km5;ISsxjPm6hb-i;^qj0yf6<3L?^4pXUyq*NA!^kBbI_UG`iSWRfPn>y^O+ZOLqc%-AwRszIsLUU8>r{FxtmWgdntJ<oL?'
        b'sq<Lb@y|GMDuT3*{b1ZZo7<`?osM?zR>3U~fe?&+H+YqUK@MUTZQ;vbi3TJ$y=&I9gH?aRb-z~Ud4X;Hn6m^Ui1vAwbVnp+$dem%'
        b'gneHUDL%0QcCGX|?(lg4YTWo{?r;w5Oa<bGiUTQO2cHBmBdSTjV%*fr_@mPv)bJ^X#Fy}z1MY~-XK#R!#dFjfIpyTnpq8*j(@Q`d'
        b'fR_gFK?RUfPFZvnP%u@L{4fgIODlbrQ>J|d^7shEpGW;1rwp3}y#U-^j{wSX)ELBEcUQ6dxV-CDdRJGm?*kQ#8PPp!Il@H@ESg3K'
        b'|IWeYT7M1d{}&Oz4?s$i*$0zAl>l~S*tmzTqf#I)4^D8z!~5o(bI31S_Hu|epiWn}j|^UrPO8W!7Z~83Ow2TD*~0O75~METlpW^*'
        b'j1?#bX0|wYS{We4qc`qB#lPnOE{3TKK!5)ZGO(x!**aN~hv18@rf&S`mtgLnjQ}~))JE=L9LNyfgqSC<?NDspW~SF6j;+%)DpqPf'
        b'woap9$ExY}x<gB!1l|7#WQ~x3s<v*O-U0ZN)to;PGk~Y~HI+IKjM*$ieb|<u_yrZ@hAZ3xP>n(72Rd~834q*x1DQYzAYZ%;&jyv5'
        b'Tk3bjqT&?J@=FfMLL*j245UX^8|t_Sy?Ec;*$RycloKMrVtFQ=P<vaUD)n(7Q9HI5(Dvah8b!gr?fDXZ1XLG%G4_B~(04TReL+Ic'
        b'B_|RHLrkdO0H4sZ6gkLnupCx*5teA}<nL{0z*9gscw`U|M~4hE_kH>4PC0XPE3>dN>}lOOXE`?9=yktJy}Oq;r#+3Gs5Sk4Z%On|'
        b'YmIo|>do*f-|cF{fNWDdsG{2T@;0^jaIdhq!%V%p*UwaIFrhvwU*Dj?a3LNt7uxgM9z_o0Jmv)AMNO97){;@KfftbcS%Fi7mZ4FE'
        b'&v_a>c#s;{OKW~wTL9YI4Xa0~llyq3Bi_>I8e~_TZG1HvPz`xn!`mP5w%JY>8ZDJygZ^ZlZYO^Qq|q$7MjQkU816t_itbt`UdsSs'
        b'jRmuJSb$3%s!D78BB$9I&a_LfxfHfQyUpqJmu(OA-|7CrsS!2mh1wlXjqo;GF4EbY*P<1h;jR)F)kYdSBpMMe4kTkm8%Z1jsDWQH'
        b'N}>dtgef9EaJ}lMA^^N;qf;a9M6b4(w(t+iuv;z}Bh2csHp?0DAy-<qI02)q`}nY439?RX@FvG+NV7I8V1|%vae9=B`on`9Fa}<B'
        b'l4X|5_VRY#2q|l*4Jv){O1bFAFydlr8!WVmG<?MCQ00Ij2`ByM6sddhRGM6k>jCd&j;+3b&ynk7!CsgR-Ett*GkcwxPOoN7yVSYL'
        b'$(FAv{pY>=z<f7!O9>T_gotr7N@K{u(<-KKi_BbFU2Lul&oEBhp$E?0dpAn%Kp_?IICHkVBf|JU<Kg%`FCZLo7>f!nH%pfKN@sal'
        b'c53JXjU&T#!<#zinP0Cq%yNfQ*r9We&2#*$I?+)%+-&aXb04Vglq!F?9ZrT14}J|}ty`{fof2N@65#l?5=CN}>WooQ{1P<L+qT5H'
        b'89K&DcU0P~y2Vhi*GC}(lG9`L3I>C`do052X<>X4^vDV5qmz~hPxYXKkx18xKIW;euF7V``vSiuHH@>R+#KMqn6EW!kKNi6m!wI|'
        b'26AQc&jM+U77sqsBX|r=5Hh>9J$qFuERm6`c&+5(wSBR>TN=)+Rgf}FFGV+(j+H5L^qY48(J~|*AwBw-_;gaP50k@EkMN};Rb-KT'
        b'jSM;f%xW;cI}KPQI9Hb)fRA%Y0QM#JsLs?Vx_EQMV@&rY2gK!?9MGTBox%~(*p~`MYGorB+az;Nf`0n5Ake=fDfpS=eVT00IsU%b'
        b')oirg@!MKc$h84Q;;`y#?96IKp`!1pJ^=1sbZ9N{fdj@g%P*Oayev#o$0OqO#6)LeB8H1M0@mX(ByYg6MOdLm#tIc}0f$1NAl7E}'
        b'%}0tl&dJbEkE4TGh*u^&atyT?kn(k){Z6S(+pHTfp_fb|2#FZkB4e~J-DzSXPq}$P+wRMgsQ70{Uq;`V48>5!Scc-<d?d%~b9Ws('
        b'hA%{xq$6uRqk(7EstN-^GtUUaK|`mGy!_jo$8$&k{QYv%3PAP_I%cQ!?zeJ&>BW#kkLGHuW2uTX5|krR^t3_+Mk5oza3${t!qE<u'
        b'aWvM6yjXD(hRhJ;d?ZVd#*x1~Jr<?V*&MhsE-G-PUjJ6o6A1KX8ot&t#(B~AeQwUHKYb)DY4oQDAG_A7zz-H3>lCg#fqLJ&+0|io'
        b'Uo<<8syZbjBG_%%Qt6l64Ct#%$7sXXhLaW`o8royO~%V#8Ls$oS(RI<+u|UegGW9Ln)`^E^c+?#GbafVjYjFiToU6ZjMYfIQt_c>'
        b'kFnB#<kV#MD}B5LA=EnM^>pB|M-jEDmevFvEXTu<;B@4;Cn>5l@wj~Wx%9qSJ`T>3YmCe2n#EB+e&yvlbWb>-dH%;JgT*!LJ(W4l'
        b'dMVTsbA_I0FPD@lm-jH<K=GkR9`*$WWd2O!ezh<0O%-fYico9##zOPepJslHBf|5&V%QFPubsAA_w4$qM;+I^3YVmhR=9Z#?qEDx'
        b'9)s<msYJ%?m7E5|CRa4eq#h1EEj`698MO_}Lr<kGJU35x=&=QTfE>6hLG5#1JOC!A-l>`zyggU{5{Ig*vQ0uoI9Lxn4m`%RFth~F'
        b'p!APauH6T(OvuU}3Y)QCT7X_o37T3UwEhAgYwPoO1J>8pV%&UZZq3OY&`)(!=ugI$DcU44EkSKe?RlRJsjW%t@X7=o%??K;=$+<n'
        b'g7iL3<?2R6j3m9Qk`K7S>k;Zb+cR0{`zPiRT<@uX&k6k91sG)TVtE1Ncs`T8y6xLK-Ct|Sm{0PfHmH`#*9D&kOk3`giDVu^>d+E5'
        b'5>Q%9y<g+GQr9acHS1fSjK;%9WSvk0M7bGbT9l!f%T9c}SJf=Py~!6QPmmsZPSF!L5cBz|pGgN|F5p2&P6!gDfYjiNNx*6=(~(#Y'
        b'^j?jt4py@|K`(T%9A1{2rz<Y5G>U#8{#uvx>;?_047%a<JU<BdNz-6m-fJ~vbcbGD3?R%5F2&LGm5H%}SVh3IPf*?(PhTBi9V#^I'
        b'$Frl|Ln@ye(CV=O<V2XO<?v@a<9yNHBgxUe=vQ|9OtsUFhi}~;vP*#kr6a%dB<=ukY&}u^VxUil07#@rIGL`~!PqZRv&8FlNu|Xk'
        b'iFiE~%A~8%?ZF#xFEn}U$mo{=B!sy}Pnt4=tLES#O@j2Tm~xSrda=fH0K$|H1}yynOd>>?gN?SFxPynn_Io^Fap3V?RrO%pb}8@x'
        b'|Hwsq;mAe50>*7`z>AWtTd@iq0szOi?gmeAz~(&w^W7QZ*EL?x_M{RM@rODMYAk{Fqo&<;d4*uez64N`>XMjx)MDoJZbYAl=yj+n'
        b'G7&rnl&qzmtnqBG1DFrSPQ5(Z=N14^!PJ7Wv%6YOWcS$nf3>&o1Nqg%JLAqpfBtE5<hkezJ04qtFM%7$i*We1Ua0Q!VLqMU92~$G'
        b'=fNS&P!T$?Zy0?)5bMDZmS|9~r_y-tE6cCv^jP9o<AKo9;a4?Kwfm{M_|?4v>NmCU;_u-aXI|aaA|khrEniQT7ZJa#Bg>!We+!5w'
        b'!0$T#w~$x^et!iJ5|=p0K76stR-JI)hiQBb9!9mn`f7JOm)9}U;qrDVTxWZwE|<~9wYvs+9asisJry|Glro?6Y`6Mw*7H0-e(TY2'
        b'UPmjo4o6wd_L#-jSWO3S{?A`RP?2@4=CHE;4y*ZcE>=4YN(U{ENeQGq71p4zIei~br8Ovy_B;<`n%}gO<OYKTA+CdmVk)SP*1T*c'
        b'<?sfE_!cCYpkn$}@K8bpf^VOQc^eBDxj6wIJ*MJUa7h!pg!reOUMZl-HGrq0R|59C#Z1BYfJ~w-crVK96`<rw0dd|A^Vnf<I)B0^'
        b'e1hd(AuBfc-90&B;5+<iCyEDIj|y<8Lv2k}v2KK2DR7>)v!4lA=^HnhAhWp=k)%7!PJhF^pOv8rTyit*G7!t}#mLcJ+1Cr0bY9O3'
        b'L$uzSB;f(&n}A<W6{ISX@~|YGO#9(Jux3gkJMzim;tYB5TDiUiynd-CH{_QT=aVJ(5;y20x969X4F6LfdD!^WJmSNB5V@6retn4Q'
        b'F<SZTUH!Wpz%rB9?&;eHy>d&V^P|@T1cv58d^pn+ljSWZUUS*o;vB!lN_2vfNbkn9WhIfX99o`$E4^ef#A1sFS~1Jauhl#1L%ceq'
        b'Sy8^9zlMh)M*}m;u$O^U3dmruphSnX{);nC-f2_!3QDhXTV%#K@QjZhO8G$ji5dvK2hY<%1^8mKUEV7;AFZc@3ISO$cgWqFsy8X%'
        b'X3MA}{<YEdGOpaDfWjW4|4^vM%9PktU<T-l$FZ*$GyRXf^o|-22YunmET9=_B3BC@4h9Lr`+-OKKDH6hX6$)8YI7O+?THey<Qd6E'
        b'Jh(jWT;%7UE)VQlukuA+*mxW@7pQ#XhTL4N>x4XCC&6)iVb{~u`8sJ$H&~{yZ?%SY4yn4;cRaBeP$C>G)7H;s;0+4A=YN&Q?Q6>v'
        b'=_^&8Xm{zp1kss23gx&s-PL!dS&`EWwTcc5NRJKV2=beMr8;PCY8CaV`v4C4a|90OG!G4cTmw01%YlN$Mm6HyB>1<|RX6er*QfJ)'
        b'at`lTuEys+c8t-7A~||}0YXCU50EEEK<1#(PJ=@5hc*eWZBUF^R5sH^Y|^`4zb$VcRJywyj2c>y@oA0?D7YwU>F{P2j0iiiUSaEX'
        b'P9IR10}=`u)0r0(XIu(%VPEkM$a0?9q44~4pMCA-9f0c`+o32rwmWCwz%#yvXSz;2c~qhNT-6h${9P0-s&I4R89waPj&OJ<Va|q3'
        b'pB*xb={e>KH{x^ip)yY$i9ii|5MAuP=wMW**=KHseYNv_J(j)n%sYzW<9%n2D>fe=`#>>t{)6TZhKGh)TCx+~Cz`c5c2o!C6lJ!|'
        b'i=v0#LI<M}78Pb5MJ-WCk1oBha_oSjTez>~K+(~GRi}Fdhi{F>x`+Gv`YLnBpr-G^CD&RM_@6qO@xaS}L489vk2SYkbO~%GJP^ti'
        b'QiL%@><V9-nVR9!jkPPB-|g*a_PWPF{xFDG$2@J)t`1eZwENaxWfTH_y#z{|#MC=>==T0qRp~p|dSz_{<+Jl@>?|r$76y7zF#uJ('
        b'6o484KpoT|aCrG{caQG%_x!-_qX7E<fO+d!<<|c%n8P2yoSC}%ex;t1bCtIISI|fH)`oNs1IUFCa_b!A;~fxkEmiG@JbZ^s5uTBm'
        b'idtUb&O|GU$-XnBLfg4_a|zV7+CWC9kY!8HXy8>a_+aPnE~`mR3R%81OMwT2-9EB@$u%HOsQ(I(ttj_n6~wlpiM&p1WIn*RVSsPz'
        b'A-=7LcOBtt2e)$JI}AJEdUyZh+#3-&kDnQ(BVOvrsJh!LdZA`s&d8+<WcTo;)kxslzzjUV@Y}g_lxuoLVx{U#ref<JxI#>O_U?v@'
        b'B;VchGHQ=5BJ)|KOcZq1WWz<?g!TFPfWHH4KBh&vl^05OL;TD!kXR3p9!MBXC1HK1v{~?(Vgv<TG=Drks!+=A&|&h+6BoSho+3*J'
        b';|)c^JG=#mWs3Jh_C=1ZP?7)e(|b`IjoFV{G7;1Bdtp@1Oz4AdFayaK7hKz^NZg@16QkJ5kC?M)?{0GJoZ|dvt|iL%7kVFF&(1rh'
        b'Ok1dwE(Br`zMx$YO9VEP53dKD?1;2eV%yfN{VeZ_?gtZu3Pom22{L9|=K_~@G;cz8qQn;@zx<W<G|@(molx|z+<WZAz|zE1K*C#!'
        b'_?Bu99fz{DpF{5vxL@ysY|LNkyIxn};mTO#NJ~8~RUNHvIsh+0n_5sy62gKCH=%|^gnjtwQ3Z?y-6^3>0nj0s15+JU^#9WaviOZ%'
        b'*nBy&O}SYLXTd+JmHp&iKq_`uRZZ*HJzW;M-uMcZBraH2j|HyHHx$6VF<)FLKE@4i$QKuhdpP*MUi=RD??bUOohr~2YZCf<-1<lL'
        b'jA=qQn&;9o+YEmLd6LA1>*|lfstOHPx#2I9#6|1s+u?f=uQ-(?Ucaus8NRPK{FAGiA~V3W4}Jmpg)L~lQcld)=B~$ff*oD8HW9L!'
        b'Ydso^iojHBRZ8mu#;Os=grbHtL^G(=18nUS`@?P7=P}lumelC2+c4O<oxT9{%=3y8F_vrPk0Fj1F{Xdk@=B5e?y;fM_~NSBQ5>p~'
        b'9rbh_OFVO2?k#xQTd<yy9L1wGqUe+-z(6QN1Qej=AqYK+vZ0c6Fq{Pv{mF6qjXPE>NPlt)Kb_el>lCU>;P$CJcH7@rQ2{&yF#6Of'
        b'a8Ifz-8v(_3fR}i%;0%?cT;9?IKNc^ZcO_MgR7GOLm&*}E$zd=-lhE`<4=LDtqe0vb32;`p&g6(bN;NZk->3t>H1Sazo3^sjW0>S'
        b'%?b7F(gKyaG68oa)O(k%Q#rt+JE30Xt|XThsz&PjRFzPnqD=+07F$%%DRHc7$+ef!PSkJR2G=UBC{!dCsLs5k$mRF5BF5?B$E$GX'
        b'!r^suHW;k?m}9@Wq8U-1x=Wjc&BXXk?nR8zx`=?ypWlvJBWf171avcEJu>3_4YReYl8#;9DFQjwRcb~H1E%ou?OvHtCIK`B+JJ(}'
        b'Yyzs7sW`>an)RSaZmS9w*!AxPhIbpScVIjc1aa+lG{`fXzv<puds@&IH*~-kn|LJcAvRWfC^fW;Ur4>OP6?wJ5yNYvqT6`T;NLi('
        b'1oPKix?N2ZLd#9AEzTDO3NB%zK*2@-x8TqXczAff-1u){xxt%rGV>!07++RX0ONLvdxg9t{3Cs6T|E3wN3E-6@F1{*`RaLhdh334'
        b'`0KBSWI6$xUO0j!c2!nQ)oudhcuuPJe-HDw^D7+Ey!3ZfF^jSPY%2>*!UTFul)lV7yb>2Bh?ZQ-O47#FW((Dia>}8*ZRi)NwdZ7_'
        b'0U3-WxC6Q*+<m7s6~+w;yOWiK%d%Hy>Dz_bPiCPsCOQ-v$OPfxwn(**^JYkBOi(+jA@RW2Wq>A)3t(DyH6J~Ohi`r@BT=?V+E5pB'
        b'XfbN}DPYj$c({u;*I->tqQi;7HO4@9y!^HYNC+!M`vtWv2k>xcWpvyFH^=tAGaXRzXAI!!VY4?b<xrsFi&3jrh@5-4SQ#cd^Sa9W'
        b'KgDzWhz;u7)tYI|Qfr{X^EWFUDPZGF(V@wX<0{`~QyYn2ifQ=;DMYB#R#hTKhPG5)nF~Kw&@w*wJwI+$vt1pDXFBANudSNt>Pd7Q'
        b'm&4!+jLVpE-S7>E;O7n{oo$U$yUo)|=C<=~E2z-7xS-Yx!>1J%h+&W$zZF;)DJKgH1}FIQkD(ec9?ZS*Fhu|Vj|VA5?+-!$@fte}'
        b'!5+7?<1iSXAUHl`TuMx!{Oo=>8e~Gr37HBE#+DNQV3=)Y|7eh!r7?jDs>Yfm6p)$?$|nUXFdF3>#*cvh@|{(I&VI*LUGI7`QFUAn'
        b'gdWgU<_2_Y4sF2QH7UZ{dMNtL*$ir3HFV^5Whe*85nZoSGIt|_lY`_jZ=!}6q^tz)TKJdA>^U5TM;U<{=<)NnR?prVl~1L9Oq~>U'
        b'Uziah0MpKkm=+}?YKwycM;;w1G1p<VPS84EjV}ho6L$4854GN^9Kr`e3-G|cA$i}?dLV%KLJPY(<oHtef%;~JSAejZV&!C@<7E|F'
        b'Ud+_<vJN~o3M8XZcmoHcuSYCP4w58!uOtV-5ZFHk&|vkH*7Tz4We~m**#qz<;aQLiYm1Y2t4c$-6FHt#D<0~LD;^La5H^>m%ce5c'
        b'B7TFbE=Epo=3DohYd~LzFhC;G7TGIkRdUAJTY+R5S~qx@^J$8^dgWd1^{#3lo&h1PSur@mRn49`pXhj54kLN<>!`MZ%BgWlhNZER'
        b'+U?Y1H5$n<nku1I*N_s#cuqjN1!NXN>8wP0O_Js(o~)Xr5`-|+kmWyVt@-}GUsOLG$XRB55}Bg|dab4=Ti7~%*G~tMYv$-cxH{QS'
        b'2gYaaJ|;V1&(h;zfDGi{Cj+&onIQKu6}>^wI&jxd2M$V@Bn@d>7Q3ByVbKqgvFvIXc6$6eXZg~9ZxvbN_XX@#QDs(W^NEru7+`YX'
        b'Y@pq_q-K~*kRG0}M?q7NfwQWVYRzW{r#ewE@o)}14%N>e5%yxRGzC*?(=_J*hWd5rVQL;sUD~l)qzkM$^mZ`y4-0sIMmF40HPxp='
        b'Vj)d@Mqol~0L?CbM@7AD^&2x$Z^4IBXv(}!5zr~3uETdFi4}PB)xlR6;?Q4CA(sCtQYg$v<0HhH0X}jO78}V2ZUI!H6H<8*f{XEm'
        b'Zeu;4ePhd@<$G?fWifAuul<*O4XP0id+}R%7?sSx8$+Q+SevB%yFHcc{@mV)QLACwIJ8Lj>+^PhVh1CT$)|?ms9OWWyUxuiJZpme'
        b'K560Iq5eL$2oH))^OswL67Spjn8>MM=8^cRm|!t+%B}%>btlFLzBi_E+CIDH!-GE1016ubTPi=gv3&n??ttN);Sz+FseAPNZ95<D'
        b'x>>>i_JApW;P=^sbP7u^aR-aaJGQ-H-=UnJZh+BfmFdy`XoTBdwS$$g^@xfJfpr@@ux%bY9va(}eJDROe%mW{G5~?@V*v+VY9XVa'
        b'f-&AbcCzfL+J6#m0Ca7|h^QCi!>P^*DQn<)&LFRCzXBeKeF^K`B2&h}XoJ)*;9IAV8i6Cz@mgSqSBAv@&=e-^4d@h8Dex<`$^wL2'
        b'vP?>9p3;}e@(uC3KG_j8pAXTxBTU>W7~d{$AMAe74yw5ftGQs`w#$yk0!SS^q{LSH&T|(|Z8~Q-$8}f2Y!_iRW6|AhzqRAp(8~D+'
        b'mk<CAc-P1b?{oKjy<k+T#qZG?jg=9<w$pBuMdPi~1)6h4Jx4vogN_;yBvv+OBiaK!8z}>^{$JZWaY_O+FlhIByQ^(P)+T*Fygkq>'
        b'iTAFOdZifqoY1>U!i?Hbupm)Z62E8@s{Hb<tIZ`<?z)>0cz^w+Ss(b~?nK8gaJ6AcIq`ESHka-r14t6-dXx5&=tc2}DCc<V%)DAz'
        b')v<fNZ2r%8^*{d0_YYKUWa4qUb@IpG`X9FY+#DV@{@FZTygfnI9;FNm&@Q!WgtzmFID6GCfRwjif;|;pI1T1E*3Pe%3$n9O_Wmfl'
        b'Ckhm=q?X$F!J@u{IopI)w<r}a2S*VL?M#-d0?%<U1F?@}qc)ma48P#>+C$oeBlCLaQH$*NY%XaMVGkkZJ#T}70oa41O%my<j@AoN'
        b'c<6oqLY*iPXg_rw{<3jMqAf8-5~hlcj7CGK0DHH{P6XJ^HhI^ZauuVp9tePQ3)Ny1_q^>pgmm@D2VMoD%&7xc9mg6H(;AY0_9Y)8'
        b'Q_;fMWOMpT(C<p?XcU8Xw6&uTe1VW*v<5dah?ks0XOO~-4wtu8Q19P+ofzKfB^OigS>`-AgL0?6ZOgy_QzziaRL$7#@szG7lS;xa'
        b'NY7rd^<S`cU$l8H+NjSUC1N%Vx1Igm*8i!k`@GHa1DEy6@T+G(v-N*y>mIcM5FHJdYTM6#V(b5#t@{%jU>3}KF4eZ3{m9loWb6LO'
        b'23Vf9?df)ybk^2CXzM;}10o$eG*dMLrXY|p&!opo{jOrI#{$m|+4_5J-9t9RKRBj-xaaI?TmMm8_i3BqbHHVtJUnVkVm?%AFuEiF'
        b'&<#MN$EP?i8Ri?1mrij>WLVpqw~Nm9+WHUMx_fPgzj82w=Cd#H-WG+%wA=o;idFi-R0IJu^%?l3y}}rG3&>FJ^r+#dvc60=hX7FD'
        b'u=O9Xb^qCB>E#YSr7u~Wb)9x|nLS}=J8b>?ZQUI<!x4^J<F9zJarO=%I0rNICE@x=`6p3=v#;3tYi!+K+h8Y$&?Vtu)DAwYFNx4c'
        b'D(F}4X7(t~zHIBSwsjx0Sz0;W#+LwF1-~!RM+T*A&wMlJY?H13ced_E8#L9YOO}X#0328<oyy|ERBuvA;D8&4j(i7JP^%ya_%Q#L'
        b'NM-T>4P-$z5-J0}_(cXjW<BjkV(T)+S<2Q=*#HuFp0xoX3eIs7_<1cX@a&7QVV_3;1iZQR$P54)V|FxLC`@e99h9DZ-q!!Tt@{O='
        b'XRVFOgJqFrk@jVY<_27fhnd@}<#vH5=_U6vd18txb>P8$T|q^bF#o+799{QFeD13QfgMyCT%$|lpp`;YUoJTSma7RS0Zvx6mUd_K'
        b'<!1EhHz0F<Qe1!`)7T0X1!rTHqvA}&wW}y5<|t~(K!zXf6b<T-6DM851W{9CN>8vWvgJV2k%X;FLA4u>Bu8(J?Q<;yk6lOl+WJS('
        b'V@IjsJ+RmPaXaD|Tfb^;pZFUtLFB@k8h_Fg;);T$l}D22ZEfyT#lljqN5tQ8TaWj3ksBC68xZ!ak0!f{97ir)z18$+f`h(fX8UHs'
        b'M*F{(+K6WDNI<W6YyrX$F0FA^+}5ws^tE)f_qXhbTPyyEBjY47%N1u;w*F`^2hVwgHj0BZccO?<1U_shcavjHm&PuEzdp@w$EiNm'
        b'HyZ#PnvRxlz|-g>ny^jS`yp4Ndf^$yYhm-w%5D82prRL`1|6c5eGBK!`^I7aJ#aswH%ax8m>*qsd9rnz`b&LWmNPx4A)CUnoy#)A'
        b'g375(<-GE#Tzf<D=7x<asQxfgGEly$yM(}sUsH`cqE@vuB|qcd(TA^L`{fhDw(idq&4N1tBdCveRc?&K+H}+nhz!m*_qbn6bacoW'
        b's$F+tXK};Z-b0AH9U595X^Bm5?Q;(`6d!9ivSLYh9|Jh_?tg(_)y5Wa)uf+eXpSsyR^()-zuiX@(&FQZ=HqhX`tMc7$Y{~$G!a^y'
        b'+hAV1fhO=vk;tkU#?#hasIUoka~DM;XzNAJXum}gp^T?jmOIc_)J9dqY2N%Qe})8Y9n1|tQl?Ev@l6#zpFaab$G_(8`{FtK9@GCG'
        b'BmZJ9Ug-F3?vos3sof|M&~MzehDiY54$p+CsQWP`ObGo7=Y3CNZ3yY^VMsShMZ;xBK0X(A;v5-XoS_K6*x${3Ela<sf-RPQ&ozeK'
        b'J^N?I{p#EOFEZZ8k*@`3J_4Vh$=eOCvFNrt>g^;in#=}h6tN58ye4@C$?RdbyP<ud_=;bbqz%QZpFzpEuvA4-zdThiS}_wcfsM#~'
        b'Lvrs>`S>vC)$p-Sq3=Dcbz2l3JjXW@f_&4Wd@^hTD|o5Gq%1Lo(r+AI_j7dcd!#&M-EwsB29iHeo^MhBj`i`1ewCL{>=G0z?ug+4'
        b'_lh@Bo1E%XT*c5+du1CJ1>lR^8|#gRv_eIGe^j9WUoa5@3gBx%)&=A5a-fbyFN^bso^m(U=WeVoE|lk+g7?adk0zJAad>0cf&ynb'
        b'Rb1Lv{A+FT+P>Uhi^fV7n=8ZD?hMGy#m3eub_t6zvM^ke9jxz{Z+^DiP}Hy~5*O2^kWI^~W?0i=-LDvYbpe(YQuAijY@tbS3ZPBl'
        b't;s@~2+t>iLF>{IQ&4;V8cDusVbx96B<}=;!^by7<rDG>GOS~5zDbT}=l91qD+&dpJEjPL+W>wZt;c(~i!xBrLA(Bq!<kD^@f!$^'
        b'=~pVn3lTg-Zwi50({25|q5(Gs>O5x(Qzr`B``fyyWpEj|jfsWbp!7K+?32;}{UN0I*|*cn<oZ@5vvEEc{;XvMrMVfG@P+9gSD!h9'
        b'om;8QTBgj1=@o)S3aTsJ$$`SkG=XNyoYSC+YlsO!4Gx4T+yj^hmQdEV>w{(HxQ29c16hcCl0uT;HLam)0?OGhA-F`m2M}F&h8C_~'
        b'8&v{01tNU(g%U!(x#LhTDjwlV4k5V>Zx=Vqy{!mtz!$+o7y{X(DCyU160mdQu<C~q6b~$I^ACiv=-Zv1^8SsBP;oEU<}2^USNr-C'
        b'TUEk#ALv|Lx4cYH`b1Rm+C<O{O$2T3C^xah!c7~>x3w?Zw7u$P;Y#{R8M|`Prv4YPz1SAfngGiIfXRR!2lPrIpb>E1+WW)HyhI?J'
        b'$LuJu#zE4dcT&L)&-QDY1wKN)OEJ0|z;^5=gbie4!N~v74<Sp0DJN%n)Pk;SVRR;Cc{gC-iYwoCG|7$cV=NH_C|uKWEW8Y021|tY'
        b'bUU6)WQj#h7EQSj^m~(T)uv5(UP4_$M1jf&`sHI{gs;4D^FPYFjprq6#4loNB!fT#_r8i8YEJVKLCB8C-7OBsG;0cS)>u6?R!0L2'
        b'BHq*}F@0TKoS_nrbJ3U+G@RbjurZY>-l53Jgy>W98nO|L`$cYRF;?N0l$aKRnW``eD*8h!ObCEx^o1YI0{{nft+Wne2I%16-#GDl'
        b'&bh@}T$$Ju5EdPWia+DhcQ+KbG&CK7kq>o$txh+n20!GgrY+|<WbZt9Q(h)P4Zr0wlhDB}96fs5@EdqePb{7gjs|BvUP6R?CcF}?'
        b'-+)Fd(ZR>L@2u8t#_D0L1Fw###})uW0Z+If?SXa=n<@*REqON-D)q)iDT@&A8+Qli`?*qynbKL`UPebEUp#N6O(G`v>`trAMEA>W'
        b'3hD*x9hprqA_h_$8mk+Bhg;fGH5$IwDt+rm8yBFfQ*Pwa8{Cvh@Ppvu9H~~n#ohBssrwHY#)&x?EPlq9;Xw$8NB!YzTZyRJW3WZY'
        b'{>^gA^SA$FkIeQII=7(uD5Umr@)eF;i)bv{)>vaVkkL|dLqNCA3fagtaFgzMs{7~GP7$>VzO+*vkC%l#MT?O5OEICJ?#1xM-OH_='
        b'lIDKe6bRafEJk;ClC?tvSeu{2*RN%+eq|U|7MBb%;_;p6m2T=Q=r`5XKhb?PEU@{)4@>ppF9B2<s*LRHPOy%kptVcYyuHQ`mJ3{X'
        b'^CUeu&XFQSSrR}KvaL~X=a(a8<o|3v-vG8E@?@xWNf@=rT6|H_|1XQ`lFH0)I%2hhdr{VyhWXq-&23dtKY=xZ9Ts2Uo~dT23F_YT'
        b'1X<52tYCg%EP3%JU18q%L0GT@F>d~r7A`W5-m1Es5U}LhZ%#p_Qy|}iwHa9E>kr*zYBh0NWL_c!y4(r?qP$4?f(VZ-He)sl@b~c8'
        b'cGTnRmmd|}k$tB4S~TKkO3G=IR9(U`&Z{kf1?%EM#$HmmsQiAp{iOm4{r+8hnPrkgdUT*(Q0dDuJWOf3(<!}&2OcCFY)Qi(S53tR'
        b'kVHr!>fd$&Q2Fn1ps{=trY_)~kwF=uKdN;dfG}P<L9JVkYn(|$$d!Ot{uCoOy|}m)@SAe?Y<l{1y1TtEJ-ygF#OdGtNqWwPb8gHF'
        b'wn7u~nPO~OF(SkR0ocu+RwL)~7$;}^_pv#i^tFA^s2<vv=#mJ<@XAi1_#r^yu&RlfN31Q&dqPH|&VT;tk%S}3aa%9;C0>M_rI(P8'
        b'%scj%&+@1k8cfM(9!<#4?>NuUCi$6VkSztma+vo$ZeXd%w^TONvAd)1@}<6^OMM-ET^$>$CdMxJ^|x7ibnQ{?0vmQE<f6C}Z7t?L'
        b'ndSXe0$6r_SpFt1+j!*htz~_=#tmCU!-h_gWgdd;Jn4L{nm(D{6d+}R;B?)!tEpxArO0`i-#=7wa>cpGz=23vuVj~C>SRhMYSWco'
        b';TT<Q2duT~a>a)Emo_W_HLS08>`?7G33k(|$OY$O0@z5rTSi}dv9If>ym-fk6RR!-qfW|F{Efo#jcWIwYTj&mZ22xlwqQg8_@J*j'
        b'<K!&!;qHvxjO|0_IsgznTo-@JA(tZO145`bAtMqn)arC@aGC?_b?_hjdKHkSrKF;QR#cKE4e5NL7sD~q6ib`p60lB@&lEpC9_b_E'
        b'kF~TdJ9Kmh?RMa6!kEthpEy7)oe<uUg83URXH5^crU8aA#!Ey|1}GrA*CuvTbQ{<Q9`0HTrkeySVpV&->Hm@S?g33*+2Zhd<YhS6'
        b'ghxd1adIFCsB<B-6{vnCDe|)RLaGs%X@>+sq&kC$@-S#lR0vAvDq00<?<CPwq;iE=E5$NHLZ#Nij9{(S(Wzq7TE}+qQEOE=zqL=m'
        b'_TKLw$bOu)*Is+=wb$B@wIUpb@R2i>!>}YM6X?NM`@&lDfXp@^(+^BBx9wHzkbm%O^w7(-?w4!rvRc={S6Dx!1Aa3Nt;J2En~Fw5'
        b'#LgnWig)~Y`PuuvJo!}bwNr8c-`xrzqf6@ZEXo*08D+_P#-d!v<V~$_VU*DpCBx*&>Mt|OMXt~0q1x8yHj7~qqYP(%QyYCNQQ91u'
        b'8?!p8D)Y<k@6Lv$%%?nt1dCyz#}Mr?#CQx*JyU8=0sq(u%Ku~wA^JT`_-Kc6QGS;kT7mu#PJMI=d6!fEW?$$u#iJ*R_Z5CAy@%w<'
        b'ZM_Vvd~NbJhc&OO+X7HSrzS`(hA2zuGfkmDXG@DLC&prkwzd=}Rc1z&K&vi8gte{f^3Ai3n5lrI%fJBHpm%qb5kRB^NzlX5w!L*p'
        b'$k~uZ8CBPf9^i}~aw@8SwAk^wP(pNpvp?Jpm>q6HF?xGHmnUECg<fB~D!+UQMR#fU2b@O?^Y0qwv2U_~c%oFTOaSZw^j+n=+?d2X'
        b'oia+TT&T;N3Y63-7mb?tCbo<|+N)MZN0*qnULa}`m)ka?oS*&G_Nq*vE+r0&GIQb0p{tV^LyXRl5S9YnylaSFG*$V<_O)WukMD?6'
        b'krA(qwzci;`pu5E{5CmQEUu~8nOUxXkiDnyj&2%|2D$=v!-jc)ppT}*%6ZVxzH0olAM{DzhFt|dvvuq}x#)OmGe=29hqzy4Sk>-m'
        b'mO}Dt&H@1??UzAwL11Z>M)guwGnkxgGafB3`RRLM>F2$?_&I~b&r}dUSE{YM2Z`#g_9<*Gk{=D-R3OFJ!VjW14Kqh$D*C^hxL0w8'
        b'iH+Uc+gH#^e2PB|xEXXw&?7B;$PKhbF$)4jROkXVPQ^_4<Ln}9h`Dn=U@9DQLZf!fc|kt3f4h7Cc9-qH?JKsk%aBnORZ<*&DZa$$'
        b'S42mS&_%sx0;6K`zw!B6L>mbu+ub|i14sW|ZeYj22>{eXsxFQDPSJkM6+Dc;8F-0Y%_{<>hiT`(xqX*0MadX*>?nVMuOB%I^}Pp2'
        b'Z);5dS}JN6zbUR90v+jOkfN*h<g@aj_1oR+p^@`;^>+3*2&=A*)oqmM@Tsz)KWuleg`&^VH9c22c5-jABOE`RVDvDd!}Fw<FJJ6h'
        b'VZPe?FuwF^fvvT-%RT7dcC23crJOx&Mq*fQRkj9pg<rNpVUxR~Z9Pcg%gtTyHM@_5pR4FS*&;iGUqun-h<c^>HfL21B<WZE+%850'
        b'jP&yx%G&N;3eDfCy@a->GRW4F)#0|*5rB3i5W0r+n{XWT+jau14Ua4rL?Y#1cn2A6k6Po=p0?@@!WwuaKF?Yo2xDSLS9&r!RZZcQ'
        b'flaSgSFa_OO4n$uofU~G%8TaKa5_q6bHqloY#_g-rJ<IB?uwT1!k+=Awe!l^#{S~w-NPS0sS)f;z@Y&Wv?k|IoIXjA&Sr$exRf61'
        b'jZC|HSA{p)aEm+W(W9Hf*4@n@HHSZWGAN?_>N}h5h2M@_JDcnSx2{eZl<?s1aeftw7*MEcf8ZwehH(djC4Wv2k`vBeG2cD}6PmL!'
        b'Juq|erj)E@BUvfElrVR9F548CmiWBsrz((9JSD&&zX<EKK2!m8%gN;LG=2lZ;dyN6i*4@5+w3Q|xol_H<4Av5QdPRLxAEZkuA+kK'
        b'qO=c$x{n`b6%_z?8K|W?cgRgL7ylAWSEN0|D&qXd_-oRJOv~A2`gB>V0ahFK%r<@x)Mkw}9}_w*3wzt}{1V#Uysh4CE23M&R~u~a'
        b'#<G7!wLl{|qG^rq5mGM~W)oEH!@!&5k@zFox%g`NQ`8GD0P0q^K2w?l9UIuNBsZ7MiPssX6dUrh_AXi8vOG61`=&X|D$BRVntrSg'
        b'&y5%TmDA^mi(j&`X&?MyNmG7tuj!{|d+k&VYhr(D7BuayXx35F9cbI7S$+gx^2J1Nnmg;=&cBWO6*YA}Nop7G`jiH3$D2l2-8IrC'
        b'd;Y`T{V(?1o?~9wTXt}~w5VVQqEFe!58>yM+S;$tV)~jCo%MnK59{hge5SR;jDai_y11>g;m{@<k0wKICna>aqnvMqD{f&-q%^x_'
        b'o1Q@DOJFjVMTS<^m9EoNJV%IL#JcS5g0SV+NKAiL)YaLJyhZ9`L>_k(;MOj3YB_zT&{j=b<N<XjkFtN*mVZ(1UbJn*9Sce-R6!i+'
        b'9slAoX1ZC|GB>QEwDdl@?O{7~qR~Ov%=h=Vgx(xdygq)(oq>;$h$q`c-W8l8iGK!VxiqeCdZI8s>2mv8-ZAb{`lDC`B!-+nml2}K'
        b'X`(0so%Lds9yW%}s*u%9i)M?rReH=7GRUag|JBW5#s7?D;Fm^F11?W8!YP|mlsrlOhP&xfOhsjmU&_4y$tli0PDOeNvL~+k<^Zjw'
        b'85=$vp=gYlW{C*7*c_&d2+q5zFBV@{Z|jWTW`B8`$C2)pKC>pXHW2f(T2_X*BBt-!t_jOUSKU@l+p*IsK?<|ZUbnrQi3pBqW+FnP'
        b'EOhfoGpUPEP=S_+X)8j?%_<Fgl{Pnuz(SI-gLb-2Ho(hpCL$!v>c?1CPGeSvi0*T`h)_qw^fM=#wx9c*eAm?x^Y#Lr4I5q=47$2y'
        b'r2<-HySBhkch1>%l^7JX3shfmD_V%!zj4s6Zlxm1qVs_Q{g#r}elxMA01qrV?j7Zp!eXPZ7J)zzsF33neYcQWx^wGIvPXI(9BKPt'
        b'PzW3!7dsD*Q(^BAHlGXOW|)d**VYbm`Rz;Eh*0a^cSC}j!o#doP_mWwYu?dpt{(xzp+1~S$%v;Uru!K$)xVlikg<N|=zOVYeBv!P'
        b'@D18GyUE$|=qq_Hr2yoHYWFybpy`jcZd!=`=P<<SmT(FbinPjQppt^Z%U;<ET4`gn*!%+>wr%I}x(|ukIT#gE4|-WpJw7HF1Wj7?'
        b'5_jb?H4}1fYEUmA*EiFh`?#b0&QR#4*Q6-Cg$0DB0VMj=$*+kX5lqv<z2nHygZ5*5IQ*H5?-Tu3IS_;{MttUwBRr6eK}1j20?OI~'
        b'S-K8DYYXJ*Mr}brVc~d`Mzh@<eIu$bnW3ZmQvWu=V>h^^Qe$7T2!&+6{^za3N`bq3Yv(&#?cH0o$2g~Vs@5pz|Byqz&T~6+`qDNm'
        b'%IR!64;p%2ea`XX!&%n#x;X(KEp{9n&w5p3D=Gk^pzg%<oVw<FI%5c0(VVxqoW3h<h7@!Da#?O)ap!6_hrP1BwX>GQaw?E}PE7eb'
        b'GrgS7?emHE;y(7bX0u+_Z~|Jf-m9#r2q9{tuyx`sH_w+A$yV>y>t_JQw=W$1i>`0srQ>G~<|3=Y?}r{Bu{WG+=#J{sq?!3{g0%<K'
        b'$p3&YTt2R2LM`F`Ios>)fLYFsTsN4R@WH2?{_>M915|UCjUSbQ{94h{bNzQ)FB#m`TRVTd)n2jH^rPy+R9%6rpFg3_u|r+`kAfUS'
        b'u|4<3>U%kThW~)R0shcJ@rImxSw+1$EG!+mzT}7ZZr)gpR^yp4f<oTegF-4VJ9e}pl&HPH@$|U_@?b1=7}Qv)%N?XU!|4n{@49ho'
        b'Hh>GWHf^ZS&e>h&Dc;{y8rEjZ%C{|-W&N0(m6dNfJzIC0&K=5e*I&=o<m{%>tV1^qb<gEq%aMO~Bln&NG-DeMir<Kmsz*EQ!mO*k'
        b'NZz-L>+dugWX?a1TkkX~W%^sUZyJ0Ru1XN20ZwZ{w*EV8`K9cO&voY*zPy)vqZS3?1Zx`LH5xGULmDh9zE@D42Ul3a`M`DmtLyrT'
        b'w?T5J{(~D)3T)k|DnOT96%P`~{wf|<NXJF{ILzeDz46^W(J?OPyp=6ko_jv$UcR*#e%ynum!!Z@u`pD%>-o8f<LP~K%AZNQFEITG'
        b'W0C#U7BH|g`nvik>9og0>MV@ivN`>{`IIc@_~9^g>FIYbqX#nkP&gIqL0ENy>+QL2E0Gfb#<0#Hw=y~Ej3J#N&|(Mxh(^qMKIiy~'
        b'gat5aPe*GR42{ro>}Xv}Sm&3P>lZDTZnz&<?Ds6H_own3?B0(!uylC7rDl5E%aCt3r$4u^d)${q`||_bzO!RFM5OQ?XvQFe<uYs8'
        b'`rPwTH?rHeL?4VgPf4SXNA+c#&thcRO<S@M+xFi=I-T|WTEPKlW^rV&e66HNCC}+IhWkz1K;##%FIl;!ZC^iVK{M90t$J2aw@=tE'
        b'LRe_SscHA)`0WV+2#~_1<4e(IMGw9jcfLG+c&|bmF1O-o2~&090eLBDU82?J>+hwGa=sG^=XadG`mwRVzyDvT{o=l9-^hnfS=^^A'
        b'ou@4JH5PU?vXkaKNU-*uys4=?-^k3!TeT){Rbrgs4_orBvX87;7tsAcfCdxmBW~Xg9H!zlHkpw@p9mO5o**~SB8RXoK3;i#)yWT5'
        b'pHIEb6(6topm+88wGtpc&eIk>7U|;lWsX_TS0voz_d+ya#821Cvvh_~tsw+NpV1JOv$r@LmiDlsZ-Vv40)i4GFQcK$MjI&VxaAnP'
        b'diQF#F(%+cw%%UfsdykU_CH)b<c%L!bW6}&hk3Xblon2B6zIPuufJ{?4#zuRx7e#Kp2M#@-<p~#1)b(JuC?LG%jqor2sEL8>t~mH'
        b'Sv#pS1Zxcn=QRdahwg`<C~DEg9G5$#oirNcIzxc>pUf&yHdkQR(=C?*JJT)pQh>U$aM#o|nW8KVTPp4UoGY%by$lR)bknfN_4W9c'
        b'34P21i~HsJZ1#1_U1ey!rqrBowuaZoS(G6o%IWn=Fwb1dut8}RtRkkdc7ibk8Vy0Jd*k|+yTg4U?f%1t8O{sLuyV$g9Tsw$`xT4j'
        b'lBm~;_nx79M2K%+<n)jJ?XgiPPLMl+9jHNDg2A}Uvk;Q1ON`4C3qPC}8KWm1mL7M4_Y1~)z40gt;^}cG@TSUjXEwAa_7z@{x}UcU'
        b'yAxb){;Vqz;C~0dp*M>`mV9SnLeqD56?eQpa=>qBzQsM?V!y<?4!_KPZsspvGzHcNLgzB#)9s~|z0G9VtI~{@sDXA7`z}K5im=k7'
        b'_AD$OuDYxB#72#*4vY?O7y8zVCC7PzrFeA9a&|^mO02nXPjV`)7mU}|`1DYVJQit;MEy{P+gZf{vn-Wbht9b5mj#XFv@vm`W=>PV'
        b'_o8Nd)B3BzdYrG@+^PDK+b1Q9H96T-h~=ees|#}1x05ap?Q}C#;G2Tdty|5d<qd~z&+dt}l{dt!w&XUVx8F;p{PTIF&vZUuhi#aQ'
        b'C&-t$_Z4nH+R8`Wd0vU1`$ldwD71!YIzv$255P&3X!sEBImB5GV~y`(RH#lFykZtntHJae6<SiE4+;g1MXL>zQbJ0UU*7w{9HO=t'
        b'`zSTP^!~6?;ZX*G5-a|m<j){Sxi`TyF`k{Ff8eLE&cAbnMb>d=D{H^VdJg|jVKF*1Dt_x51tDUvoba%Xlp<_-eg$2+d_=!Nj7E*j'
        b'MMrbTfwT1`h$HU-#C_E?EXb90m?*ilbazGfE9>^M*Bja4aKhdPVBI}pr*Z02T!cPcR5!VIgtmQ1Lj#<e8_&+zrQd@>*)LZl%pKaw'
        b'+E2izpY@1Uzkm8E^$hwHXr^*Qt6w~vRa=0<Jt>3Jg~=%=lC$n-bsW0*b^wqfEJgdORI3c$nW8lW_q(`H-lie<ieRXjbvFZd-LSvN'
        b'vI`M|`JtL?rJ%c-m&^9Qb=IW}PEHo&gmno&EXWDgzBDa&z36)mKGp|)H*k1pC+n_<??*-d=1M=AIKFk(jL*$8eg392O^A#W)7MBB'
        b'Y~r-yX^PLiR8)U9hH1kwAgm{x)EXq0UV`!J)T#nL-TkHgQ@7%Cf%fBv8ADokN=CM3HA@NaDitHjAei<Un%uZtWv)CIM+9RGz!(9}'
        b'560h=t_Yo_Jv)O^B<r_kC70_z|4MgeSyt*+#eH$AiA&!ADjQ5-SYFWtzG6aFr6;yWi01DBM(bJFBS16wZJ5gGXo|KlmDeptF)&Ra'
        b'RdpQ-YNStECg!p#7}~pC;$F<c6z27)F~~U3hT0EK-mtZ_v|NAjqW0`E_^nU7$iEW>tqKj2n6vGm8~B<EN+|jq$ueM*-Ni-ut4137'
        b'ht#b5dA4%_D>?ur#rCTBO3&(-ii4}}=BRq4tAlbQr~!v3-C_t~-!t*22q8x0v>ZpeDC2s%BIAxC_~)IAUG9W-SkFSd^$e6NZi#b*'
        b'qMtczsW^2ZXK~XYCutVwS+B{Tkdyi5`}J~G#sY=w@eHMD%oooqmsQ!JU-})FEw=HBgcwlVtyQk*0LPgtW>%w^i*>M?uGM~T@2KzS'
        b'8tJh1HnBEq!TtmyRmFi-T3sYka!Vzm<)F9Cqj-ear3h!2avGp@GH7n2G6<$HOk~p|kr2$nDW&f_KY9E2rPX^^?bjSp9eHkNGjN_U'
        b'nArdJNZDx`el!M8-TwiR`WfdC&Q?_4-Br|UTuuy%(Qy`lFI+Z``kOcQrZm;TVXIF5#jgm;jY3gT<ndysU(sqOI?uTH_PfwT#q+kX'
        b'r=@QdJHv`<(Y<OGuXGp^Ogck^eg#zwh#L)babOQDQA(pb76j}J)P)gc#9g=Ss$h`hNB;z}fA&>R)w*S_k4s|@(uHNrK-)YD3Q1Om'
        b'J}6S<cs%L8siC?v27;o+FI}_leY4g;r)TTjGOa<W1?ei)elF@w!9Ax-dxWJaw7M^Znl<dMY$vpaS!%=V!eiWP(tWqY^C;e^XMf%V'
        b'u-_3<BtTFbBDAMVBd4#T2(>bTdhs<P_V;^ggD`C8;RP*%O0noOq_;SW8GR^c5sQjK{$>4SmE;>(YMM^Aw(jq~(sa>kZT`suc8C~Q'
        b'oPn0EWLiJjt*q%0!!lO?39K7==mv7kW8dCI-0#f~-HGyqp%JBWSV_D8%iQ@}v;9xzL|hd-6-0l#z-wS~hAQ0yF;yV$6CC<`{yhQ@'
        b'S}&aO<8v=lVXu+4KMT+OcF(R0vKpy=CT;o-J(pUF+`M&+y#rQl0CdygiB)YG>k;b?avvo%dF&eVuDrcR@XloO&Fo7W_j<Fv+&m`q'
        b'`cG~3be5SDhdbJ2i6cimrAd2x#0yRku8U6+G>(Iu+At#_TWy$0k%xmNakx4EEqQDreHZi|L+FT&7<T7-+@(HyR&5BmYnTqoQehMK'
        b'j&xtBv?%mH)yf(3D7ArBD`)bgZ!|=z4NA6o6Tjaa*=UGJJq0s%=kazyp^kwbhv&vSNKsLY%+)s!1&+vO^qE*$fnRQ40@?o&H*CX!'
        b'63Oo)h5%T@29+}g>}J#XxouP!Ma3q`Y@hAvwUq<xVWmoc{N~&`^YJ}ku3tHGrEMtD>`pXyCYkN$x3GUlD*J0wL@nGqWa=%>bhGX)'
        b'0@iY?$86rKZ=K?!ptoeK>>ziv&Fa~GXN$RdFHgF;=FWd_u}7HEbt3Q2{=37?Ii6i$b$Tda?r`o%jz(vobFy^?C6Io_G)dh1Tk`AV'
        b'u?aw*AT>TGTWD6F7xl*DK*Owfnx|nFsI$C6aMuv5MmJohskR}GJ$q%6W0(3kHg!1=>s&`Zu)^*!bgTVGQ3)UTMk*@y=>s?=pn_)%'
        b'P<{?~7F&wG(rH#v!8${j!(Hr6Viaw-i-^Ti!jqR2BzNRvr^1mU)iCDMay;&07fe?|6*#W%9xuaJ=`RKXy<P5NXwh$cZpjzb7!{nq'
        b'Vyphb6TL#DxFK}k+|v2pmOE`*M);c}cJCJFO@ElP00sd*F{V#?q{Gt;pKQ@x5cMv{(PeW3t#hX%`nY9iJWm7vWTCb16t}PBr!e%w'
        b'Ix>k!J<s(Ia3=4H7Uamz=$5&EzvZfQq`#6^Eero=Y+u{`yGl?#L5T^6#xMR^`0ZOLj_kL87Or@Q5GgUk_ATqSZE<_H*gacd83Fq+'
        b'7x(_t9~y&^EnGULmlBjvXPANh%*_61ixC~Y&eHW)>I}1~`M}nxUvfHz8c_yk<?S6-2Dv-8*j+wI*qE^JvcJ`1ID{+`O0;@-^+>(P'
        b'c#vBa{GK6UOFr_LNb@(i&;Z7wvABZVS&9Cee>>naV0bg-D7P;LZ+K+&P*PyL!y%#`DUkZc<ozx;_V6w!YomKl)Ybb>RzlH~W{$E;'
        b'x43t0v494+WXlL6A7*6sH@A#F+Uq<A^iQ7HVtO#94;^drbXIS%-tB0XnRo1M_UwKJkd_}AJ~Fb)N*@_QHl$B=wHPSX129H^PW_gn'
        b'!hj3@!S#QQY%~~8-<0z<ja_+U5lq{?Y>Q9T2MF4aLwwd0=)QP{Ty=L6cNWuyQ=0KjX+ojzgnL58nZiMSLrF5)%t-y26K}Yt?USI_'
        b'zcQHXV`&>Q9N~dY$8`?e5=bD9vC4Nf(OJ#3E<C6iZ&Kw1L!-N2-Eu?@|Ec-VvH+cE<i-`=;;elKZYf7L(N?;?55@1zISxj7cD;tG'
        b'cfjB}2(*qVGof52`f1{x^2FluBWGcxOQnsTsD_+YN!^~{BU700peSOX4DES2&_qIt_dAj|rTq^$7#C2wfo{kYR~snrH)H#fNLw4a'
        b'&QRCl=kf4P+`a!CyK-6kISDIM{z^K(O>TRaKEfh;^ToNl3%}x?zB$NXYlvyy4912T3xbS&5~jdE`W{mdnA^AHJo-S?E_PmnY5GMq'
        b'iL^o~5J!8EOKXZYjimQwJ2&-^St)czA3B%1%b_<qs8?5zM`=aNBcBIqDoFd1DE)8-nRpmL1R$qYb%lSmvh9-k-Rud(pUj*v>+ZuY'
        b'F>~w+e+b6}5}Nlm=QHwTEuDdDlB;bFI=PM3bZ@4FN0iA7O)UcY18TYQXbliLZp~uVFnW3t`jNi+!F&NFfI+jW>YiPfBh=0bRlMb|'
        b'D+p{CxcZXmloK$*DrRiOULy55j3QFMKm)SB5cz|mBb<?d-eS}~G=8`+0J`|brlA9yp^xVn=w|;-ZfNIb_is0!8>UD4qF_=&$5m^`'
        b'pu1n}c-Y?!u&jOJo6?-VX<ltu3VKgDx)(V!sFybd4+j!Enk`eXoap?ka?2$$>naVbd~>=xbu+qoA_7o_#baNDKAD@RIQ@9ORCJiL'
        b'ga<W+@J{S_-*DEb#yK<V5>0ICCNpAVw7cATh<#9n?lKny>f7#^w6)EgHk@MbRq2k6n^S0Q0YwS41#%z*P47)VlzTAxxUN8^EeKE$'
        b'qtMUcgX8B?3ZS<`g`0t}BjJJWaMU|~;D3(>zUBM=ZQPo>wOcuCjZ0+V)@b|99KUDPPV|tfXU6y~ZK<CnBD6<(rppmAogGC8L7G_^'
        b'++?+O_2B1VGFc0lmD4OM6^$!H(5(B@IDC~SW~XgZZrNOa9coA0n<}kVWzA-bL1u{vi|(`-<d%pT$|}eRutdx}vfE+^WL2A^-P9t+'
        b'o#10<LG)1b9g9Jta>4lD&U0uKSEYkeRN(D^oGVEVLl70<ac9XoLB(MV!QP`|$c3GA{E074D_8^k9vAdy;wmdXX3M1Y)#4uMi~*Rx'
        b'R3Q5i>d$L}#7>7h$~&m6kt!Yu9Ui)HP^k}n1`LySq4RU)mAp6+VvR)n;mFP5OP)@0vpsin;THd5Pi1iai^7ul#Jh=}1eMXVP;Hc}'
        b'nb0z$EN5$iOJ@wpiXTxMgDFyNRH%*9=JO9vp@KSG5*w#k@EjrfPb_Z1X2VA{YD1vfCP6E@J3UbzcemzxEVMT!zB+kw1SVEM;j*!?'
        b'<%^{I+MZG5O{J5<i%3GW087ve&Dor2Nyr{?$0jxoiul@vnlY#t>VMNsDXyLS(J?r_NNjr^8T|t#*JAI-zPsl@-kozb?$FJh=W6WJ'
        b'H($GUUsdM6=3wm{?9!bBYe$%{i+`DV=S+<|aC7IG8hhYo(8`C6up-M2yfebgxcC?O9e0g;>gLYg8vE4Esl2biVdIQpr5t@c6Mg()'
        b'ja#z0v#Z7~*$gY!uyH1I{L=NCTfdz-^^U8?O>XY&tg(}uQ?GNyLka5_C<5;st@+;H&DC_iS7YaD&|?QsAUv_Ym8bCeF<TO?$nzpG'
        b'G{P+<``<%v;*T9g?xB4=3)J)O=JYL+t5RSKmpcl`&^WfQMQlsji$vQVw7;6}$d8w2;I@<#MG-F!{i(+Ndd-MC{oHw)ukW1?^+7jI'
        b'-`NR?x-tD(vS}SlS38b<Syvy&uVLJi+tm(@$dOG<cd*$t)J$_cXkx&K=@iMsfT8r(atU~%qk%t%DvEgMI>rGmkDur-kHc^x*s5)y'
        b'E{yMV`&#`Iy4$m+jX&zgp1+Rs%I_SlA=0~za~S5)IvS=xsL@^Ou^qT7J?rM(!)^n1-**=Cb*@I5wnwza!5=ga+iV_N)43sYuiFgD'
        b'NtTmVSx{Z+Gq#q!Y11!3Uc1O?Q#Lu5N}KJC$Hw;u5Veaihcc2)NAsak6?XVTBDEY-MEEzIwr{EFA#KgF{DX2^Gi?v5fxpeC8<jJf'
        b'FElD=HWp4r02&F=JgiZkW%sYiZ$|Zc$Yva+V^Mlo8EHF0Q`8Y<yZ@*1PvaU5zi}DndknF|hW}vaq9(8ZP}!*b&9w^It_s>#L04(k'
        b'u{FcW|A=j-OPgtrGWN^tX2a@rHIz#^f1rH#JyZTBIl6PjQm;|sK^%2RShc(Gk6c9ydSe@9k9LBT{fNWBk_jdHKjZ+FwCO~DFW3J8'
        b'`rSkBkH^D~Q&ajcaP(eh>7f(o@^2zGEYH#(!Y=L+Gs=0XM`19EqBD03YtTKy&rP!H^e%Kn3vD_5#`c~488r+NqOfpG|LCDhDc`-X'
        b'3ixEdA0fJi)E!~rl_&a=pBmj!4$W^I*@|YT;{ESM?{SK4q*g_h9mbOPo~W2IZ{3_4;K<SxnYNJ9^q4%hT}Lh)@g~R94uguC=^JaX'
        b'DV+vRpLaLGp6E2)SkOrHf5D+ejUj43=S+_QqYEJG^tZm^86S{Ry*`H0|KwFMgmE#4;`hKhoVt+%X}^KLx5(=pG!mdhA`6SczHZER'
        b'cJEaIe;`1NJ=G<A^?DFrf-<c(NW8y8^W^`hpDY`Dk~I7|sbyyNUd5A(3P454ze>BenQT|-?}dDopPrzz?U6YxevV^(sW?(2Y_`1<'
        b'?`#^GnZ5@)pwNCVO71ORqg|CKQ2k-@9gc&MLSbQzQW1&|Ju<l;nK~bt?Byn(VUqt1{fi>({o}9h$+kLRJ*!q;kq(WT+@q$>QIoyM'
        b'#1^2Bd`m;&N^UY9ysr&a1*`!0(AOsSH>S>SO!nWJ*cGTcQUaz9-7vXtm^!~U`GS*7dno_a34*GMryIXNl|QaX8n1oKP2%8Phj942'
        b'$^C_?^9z%Gv5D0ppuawUSU*0|SHAuqQ2joWd%)B=V6uaL@cjR+Upzi>$I*wk^9>&F4@_>isncz;&o{Br=#!?tY2Wz`Z7{ieOr3v0'
        b'c&};Ow@s3B-g<mm6_I6KU-$kJo@&d+^`T;;?|^bOI-vX>DObP^xnuer!r~hl=T{%hIBv+TO7F|(br2vPa7Wf@AUbrHBIvf4`u(u9'
        b'u5X5IgvW;QNIG91-`9;(B1^b`TGyb@<mL;E8ku+H_!oKO|9gCY&-Y=w$-URqxz}WWvWb0&l*y>`ljG^D=lvaDZ<ER0VCrlz+3#**'
        b'f2iiiDC+pMN<qT;SY|zX@4@=yX{0Ka)5j1Aj$zvYkdK##&bpB#PQ+EQV=$*$rfTJ{s1I@r_WJu6XI}}o=27Ys4#`EL5(V;O!a#p;'
        b'9J`Vhe+AYuJ{YJ(Z46Pni+jjIZcLx|WFEB>REczULj}|~y7P7T@AVf%*@-Z%t<Y}}$b7$b2F7RzFN^?uem3H>_5DJN{1wC5N-#}8'
        b'vjf6rxV6g2-Pbl{3~9WZz*>Py$yQo3$3zM97w<tAoA_0v*`C{3e?9Sz)*w?G<b|`j+H)L+G=Owqz8PbRTR)`^0EeP=%em(X$PbV%'
        b'lWP}}Eqq0tAwq3XIm0+BUhmL{j+!1LqiWX^MazT!k9>E}`1zBnJRlu<*5rQH)cLH*zHbw|2N7FqAi&zPU8Z-sk=;}n29i-|+jgQT'
        b'DsNIesI8WI+}c<#m$_-5*;g1a_M{{|-0>=raXdZ#$ia+0Dgv1j4lpGgA~6i|(BVxWJlqwV&RwQK@cKSez5nEk7XA!w&Dn|b3JvD5'
        b'ODMl~0h@tHo^$YulVUpkO-u^5^AIaQ!xnXr3JqhT52EjkeRNT<lwzQ`bN{B=2OL;Ey1=O`niLLlwxWA1zn^yXNq~5gG5zHyfS)Ij'
        b'xGLC*&T2ZJ%-vzSu)=y$7f6IH*S$)ZyemTg+W#%b>zajYCVANY?@iQ{v}SzfXv<cM1f$>A&{458{Vckq5)(z3w`u58u_)B6`B~l('
        b'sa4Vup)oVDVa@$_ct04|HbqH(iJNWeZm_tRSq**A#;cs~3G&vNqly<mqi|+(`tEUuaTYI!(6>XII)^qnqA<1}QN#ZCO|F<(UhV&i'
        b'85DPRlQw)-J89jPUY=~VP=b0wYs8)RICc0e>-r3}xy^EfL9cUB-5#imZr!ok3f@})dK~>C`Wg4(rnbV$z_6lKCxaHw4QuN-vA(;z'
        b'mHaS}onFnqMXn?jpHS@t8;@#-wXuC0c>q0xqD9L7H_CJonBm<`uFr-#Qn$kRwu{*&l#SLq)dOm&bl`HkkiCSm63AHea?AeCrXB&i'
        b'1m)C7Z^xvQ^ByDAh-&`Mr!A$I3Q4Zpvm>)C1%Oae<h!{{fGMVNox3&xgDk4>#X=|x$G{+C{ZX<glmf05vzt%?=#PvewvtB!g?`2$'
        b'wH~Ev|H)xhfugGuXJoMlY429bfdWQ2zvp_S_6?h;SFYk7Te)-3L_Bu_gz3LH%^x@QNC&}YQPp#7d-ZEXFO40Mz{(sWu*w^8jG9$X'
        b'u9aFo9XJ1B>$O^0uT^e&Ne~%Lfr)Ngn{@&V8<mx#UfBuBa!8^L%sMVIlcWUbx}xbWx&h>i$KmCA@Ym2~R^^^*)Ch6=mc{mObBe4H'
        b'7nmL<TVr=wWw9wTd*&t(BqKI_$&jxFi$+jr<@hg<zXpN|rUdljJ;_h~D4-W#SoWe#n&eG8nL$Ah0m{S~Ze11MiujvQ61}N5ByH+k'
        b'u&G_devO7%aZA*xMyYEkbtQBVd3Z-^=xM$o@w=gC8G)q1!tcw6Rq+0OaEkzIv|&s^G9bsC8AqNJ#Pok}Ejy3*M$4HrL1fg_VY}cm'
        b'A`D^?=SB`-D2Rvi$<(hnSPp$nc>gll1d;krjt|F!?qk{(I&3&=M@`XcP^J%@-PvuIY#JoNx@6P%u1Fe?FNuW}6R*Viai#`*{z}yw'
        b'`Iq$Gzj1Mos(Yl=ES`GpWZ@q;3y}Ab_@*C}4ge=W-U9Ba4<h@&t5L+?KH8~$s$bY|Rl7WtYB$F)xW$Ism|jXsw{HFAn-RYJzn)H7'
        b'ly?>70h~hi7dV$t9<05Pt*ZH@O@Ntv-eNyjO?zm|;(XU>N>w?jKcRxN)q})mCkog3^6Z#}$Ul(7{(XZbYFWdjcI1?|p`;!6E~gyE'
        b'>Gr>(HoR|utYLrLIO!9?jX7+)7=u6iw+-mUKn$(eA=aH;sVkX5E!LIH)Y;Zj0$paM?rbsTug%QYmCV-K%Bf&&<{DiI{aNO4$@JmO'
        b';^CFE%FeFQeOy^q!ccR{O2Tv9YyHb?WjYeOeWG<p)y2ixs&Bflijdz8<PAQbGhC@c10_;a!$QLjA$-sY2o+Kh9NTEC*#DN&;v~#P'
        b'H2e1d>5M7^btWucbdzhe8TP+*pCva!z5Yj>&(plOnsXTO+S|OIrm<G{km=CEH361gTdihZ(F(EHL_u2MT<?X)i=;=BEX*sEz+5k|'
        b'EXK@c!Dy7+birjqF5FcYAFq`T<h7H|e>|Q!+F4oMDq?4E<ex2#WxX$JRnVvCjwQ77@?+6Ge%`7H;HrT@`^sw2!JQv*XnP`4q{anl'
        b'1+ODf`!ynP-0!MilNJXa{$QGwG_0%+Yg^T%VoNvhQr1cyEzS*WB>~Vtpi)=eL$GNZC$<(b4Ef|@PoOoh_CAL#WTFFClcxL1jOzZo'
        b'+>8|DdjtBbXvFP{VVEV}L7Lr$DC{UkUL&fWj<=oP`uj5%_d+#daBm5J*YS1|t3h-=(8bgFKxRAcR8vQGQ?CrWBS2gsk0h}4_~LfY'
        b'uU4;|r8q7^p12Ot-fzYm^3X-e!Y{{tIZiL=ox-@74eoi>!{M*QMOB~sQZW1ycJ3S!ID*lua_4)G<5U}LW<hC`+!AilwsXl=<W9m;'
        b'U^$Q!7gilb4tSJl8??;q3^Hy;wc0qFk5w2}ZJ)c5jY549`SfshS~V=o4OUiBO-<+hwM@j23`AnU8o*1zI<>?X7!S&rVS#AE-?viw'
        b'v`!Pj9OURIbKQpobB5bBQ5nI<QJp3fdAm7e(ihp2su?@@+?FOshTkvc{I9U)UAy*9V#3$oJzB;4#<3y<Tc^~8PTdh5W;L7lG6ed#'
        b'e)=TbZ>wlqIjSgm>TZV5zh3nYFU}<miBAC|*+2?iqyU%}G>?uBf%z0oNxdNt`1cOGFI4d!ajc1nIBFxeo!DO-)Pu9<kb!Q+i$cU8'
        b't^Zav>1SN^Z!Ye$D$gOT_iTY|Xu=v%5(8(W@CM6#(u(^fB;o_mvgR*Uz@7-QfcH0bWe3|;HA#Zj5We^OTc%Kf>hvjLjOY#$;H{Fj'
        b'R&}Nyk2?z7h~(XSRdh#rq2R%UETg1_b=bsjRXVQdCJQrgeIB_~YP5?N9GXu_lV9z1?#EVilLue|4GJ?|@X0LVH7PY0e$Yf-O6`vv'
        b'HP<_vSk>~k2_E>}2A|%uuS&D8igIRz16%1b!l{7TsUY+)ZzFd2L?{!E(J=+B;XMQ_w^p(>oVNDH#8?WjXsE7mJyC8dcQEWVDPX6+'
        b'{P+mTzbx>Li@7Q`_P!+w8)%(4Cb-XmjQ2j|^q0rc1$3wbv{Hm40p~48lYf0xqYWBaD&4W8E-`jc>If&0SEkp>eHW0zcWldS&SdJz'
        b'=5RlTA+X3sK~!L!ivWF&Z`9Utza63J^Lx$aSJ@3!&_0uiDJn75&m3a|MU@J3{)?-9;?wmRScDCjGN%efR%T`@S5&DPzzB2R#9N7m'
        b'Jc?AsVTpuNSLMBpMk;~G{$qtLp5}ci!Jl-(bk7zan;b9GEUB8zOb}3SWW~!+Qow(sNv)dvCQe&r@*-X(XCx&vs7^E)_hOX>-@s>P'
        b'O=R(j$#Umjl6qrCrV9S~%}7#N(Z5V*9jT0{YIGo0OE=o1%d=8Y?F=KI*8LCnztY*Y<-1bo$+Xp|39rhsqI5k<TO!h_g*HBIS()z3'
        b'um@I9em1M@X`WT9nN~%Gf*jH)P*>}<2%HXq*G|CJvWL+?EtM)_#O|q8SEb+M=<b>=Uv*Nbe}r6TSxJ{|<wVOM5!nSuTq7E3v$3jH'
        b'e1dA)hEV4TVM966cgIl;`{PQr4fp<+5{64NQfUj{3MP%B8dF}Y<f+QWqjs~uuVi0F@*zQJ_K{nddXx7FX2&|eubeS}l$*2bQTVZ!'
        b'DL;yFxM#3Gp=9)K<(HL^>LFCKu|?7=d7UGb_8XN>H?BH~FO}YIX(hZeEQ3I?&F|vML4=H2iz&}k#+|8D8ws`Tc4C0?VkP21_(+jA'
        b'=3p?VKc+Tflks(4BNQ&l2k}Iz5=##--F<Q>@wuYFmj(q3-*ea&vS(2z7k<|6Hz;5~LBFBk9}9P|A5Z)~1;5?Abti1l`t&u&>5xKP'
        b'3~XE!{yhQ%HM%Bhe+Iu#{0fTeDU`G9F@Amgfx{R(fkLGD{24un4?jvEysm6ZmtIM+CKW}=5;Li=nE2TD_c+dmIG>2n8Vld_PsEx~'
        b'+X;nH6nCJ~^cY2c+l$DkX{l@ySfl-{_0d+MDCA{IQa>GpXag#1)v>m6pM$3VM*mHZp`;F#L<y{n{vlZ}&@@!GMmP&VY_jI{zN&l6'
        b'c@JpFrA@1`b1NEbtF*%^>)g4%!^cEYXk<#imjf+UH0kU89Rd)25Uo&dthB;UvZ1SJx?faCgDZ-O=Jod|2`q6G5lyB(;hx8F7@ND%'
        b'Q2`$?M86X#jQ$_Q3`Nj2Q0iYtsH`ifY!@+eFoimV%|#jW{HRd&(+Otp4(DsW%J(yP=lkBDxTpw9Qr8$5CAKnQ)_TUG!jUiGVhn6g'
        b'<dGtXO<T|3qY47_6gOu_1ydo>f+(T!<B;f}`Ut*?_iv&uVN@{G(a)Xc$Ix9{+eOa5i5L~GAI7K`W+ZtxlJGCHa3g75oIxs@sN&#A'
        b'1#<U0W2dhTJHqeCviVYgp(vT&Bbm{_N>RJ%gf$=o*Th!V$AQUc5#T5)LzzZWrU@$3(3R?XP1Wu)0cmBb?3LOmUA>{oZ4nS<0zvd0'
        b'Mj)(T#~5Tr&Ah51qb9+qNtusR0waS(iZu3_m7Oyy2Ssc+;xh3qqW@LQLrB_1Wen~Cgl3^^4<Iv-qWlN_d&K$g(rhTo1oBNs|HD!~'
        b'V~SRGbg2|?P_1O)0H?U+cU@XJB(3z=C7serR)%V^56ci=d<J7sJSlJl{21It1y=EuGl+;8V)lEKRz9eRV!&v84%Qh}sz9`hgPPx>'
        b'5|BWT5kVBgBYadiJC1@u5mZS3TU=xqAv(k{9?oLJ=&n70D#fV&DvEwKItATB0DTkrkNXF*pw?ZlxK=CQQDGJP<Z-2BR|VqEDv9V*'
        b'uIssh7bqh2TdtK<eab0fxa(h541H1IvHOWW<6}<Q@z!PRm+O7#T;!QZoDie$d%%8<5{Y8ou0!(`o$+4(tYYXB_*&T6U*WJ5{8=sV'
        b'ytki^r5Ebw{RDpCbWAKwm;cK5tJWiH7dWHoh4&60r(FaII>9~cKprTiQ7C!%_*8dy#moL@J(N_1;pnQo)cG?e;^ThNvE?#3?fe<0'
        b'%$!h}(p5pnTa+CYNw5M7_$H9P(p~`#+8B$yt%C8$=r*%+CjBd$F58L9vvd}Nqr!1omfU+E1-N<F?A?Y;s=Rl-Kl*g%xVKTgSjH09'
        b'RN?T*YzNKW?HCPz@A=B15ODF1as!z@IT-g}6{vPYh1N4KHpPtg3>35?bUfx&mym$Yc#-!)wzlGBY6p{~MrydT22>R&Y`Aq*ItYYN'
        b'-N6*0k5MeJ!dqDCEgwCzt19UH@+`eYxv@fbdLF&p3@G=I$gJN4pMypI488Ej!zTnVDIah?eagOOk_M}R2J;XN0)9;cWkH3z09IAg'
        b'JrHfVi2u}DVVt3&(@>$-k)RRk1oq!oP+Qenikgb{jSpd}wHP(4^S2fD-&S0miqdPa&fE&%`#j!qCp%YE9C0KzLWaJA_e>^J8|6=9'
        b'!lzYG68n;hdcvX=6t2URnH8Y4mijhG%YFXtppy(KOisQZ$q0CYGNh=8xzCW|2W3BGFQ{OIgkCq!ki@(UW-%0EG4WI*@59tWVmlZV'
        b'xjNo#A@Ti9Nps%+mzKnfQX;jauxKx>C9z=}aVM_gdR)c1K|1-kxm{G)53Bai|6(%HhwZ|`FF16~1jCAQKIUJi7Is7VPg;`DF2><|'
        b'zFKB{?RUO0u?R5atJ;=NTV-G+$Cgt>(V58I{uLI1a9AKPTjic9*f}d*cR&s@&0|x3(nO@r#_ARdBG0@yb9COkPeL}%OWfadPeF=V'
        b'Sp^j^Aek>w_l;9hDkOHt9y&_4NOCw}w%U)h_z~uKx%oKFiV#^vqZ~HS=f*0i8Z;mQh*#M0jZXo9u51C5m<M4_pbrQ9qw~j&&J{R{'
        b'v#Y=Hq#w9-y|W1O#h5D!?@<d#kf*4Hc-nQ0i#-)<zp+uBApj#q^;?X+xlz&dbF5ns+kxDds4{UxBoue#{6@O8oDq=F^#uV_7y+>$'
        b'U=F_@HN3I&>c*_z`|To_9I9+gd3oa%3;fYH3fcu|zWkNrYiEFJ54Jeai?MNYLat<OGbcyT^|%$E6Y_Vqd!s`j+|k%L1>4_30bhST'
        b'dmz&#5Ed@Q!<gC!AT$ea%+_CiRG5PIf5$05-q>KIq^t)Sn;=d4xkXa_t)K0kKo;-S*=tFgacjP<T+#h7D;zogR4@;-vX<#j|Kt)7'
        b'?PBM9$Qk>i2avcb%sP#(pE$d)+5z4s@VS0*UYKnOAnLj&UJ#&Ab+-Gdk0<>j5)Cf2hMeo6*~1$qZFd8f?9vQPD|^T9P0|l6t@{_7'
        b'nQN!y$-P0{#}6!|NKoL^28_*EhqhU9UUlT}?MZNl1TzoFZ3DDJLSSw3-m~z7Tw*o1;k|7%zh5Z&7mCYK+Ht?5w%2UFfARxKV}Nj%'
        b'75#1mJU<NJpM?y}hRS6D5<nfQQVME{dG((B{PO(@6xFRRo~V5Ri{(EWgg$2F6o4pG2N0eB(zdlX_PO4qq$Z-b%>w1Um6qOkcU!YV'
        b'DJw0#4~A4^=-d?vfxV|KJyT$z2w69=Aq4b5{*)jq5M>RLT}1Vv)StK&3D0B=K;2$o3qj!zoajC`eC)}&i!zvuD0G^jS@UIfX=#x2'
        b'HrJ%Nl&zR1q?RCmcOCa*PZe~;_pZj@6hW(N#T#q=ceJ-1aY(TpZpX`5m^F%^M62GGce|o+-lMIe;HN<ndHODCEU5$T*}*oZV_`+9'
        b'54bKu^pK;3sTX+uO?GJ99qW3eZxVi|pqWqJ4!zcf#-`2DaD_K`dhlqR9Vz8U6Pe89u1n<rYB(L=b#BA1rVYdCL}NOP3JOl><AE}m'
        b'K5XQ##^1q+3dfP9HWDC)zjp&9*RI_k9leikP3sI8?<CiG166PZNCu^gq#ej)^!^VTHiu5qYMf81F7xu7#nuw7`uT#wpHXeC0)Z=2'
        b'NI+C(XtW{;j7g({(61C*HKpmjkXz9uDN_hbQ_%0^4D^?dDCp8q6nalQ%t2+3g0y|u8<V*!1yQ+olchJs4P)IT0$5PJtvNDy`J5M$'
        b'dOemNa@P@>{c|aQZ(TrpXqb(Mcog;GR=w&RAh=)c&??AXOm8w{snW#6&z~atngd24+o!O*OL>LA`gp6TpLah#=Y?l@sE8M)6n@LW'
        b'{QZR&j-cxc*<TtEFL=48>`MlPSV%1{UEZ6Obsz0ckjcvnvQm1F;D970?GbO>>ECv}ZE$2NcJ|W|V2HLeB5F#@(G|^7#r^we@}m1('
        b')gN|uy8N)PW>+Q#On?C@lXnK$gQWloSRCNP)S$#^3ICsi5qd|sR-<!-)9Q%P6gkxJ+lEN46SwM;lk+V)5ucJI5;`4e)Jn8EVc}ol'
        b'3u>C`uN?AE#KRu8VLsggNzSi+*(Zif-&wn24MzE^Mz}%gd}^W$+E)DoAbBry6xyY+=*0YAG>KbvqgFYf>epm8=Qrv^7M)Plg<1`8'
        b'o}7%~*{TD9?EL~^{{;uY)LM!61Yf7{#AF>8iFs@ob}HOrGj}u`G<VUxSLk-4aP_bEvDR&%gxV0XIz-ec!II;9Vfwu+NPelHVzpdn'
        b'GdCRXin6cT04CyeG`{YY8$dISJ+n3Wa~hqU5YCmqhV}Xek4*yoHMi2NKdMhn0V&)Z)11Vgd_VZreSzJtZlD_4r}U64$ybzQ#8~pg'
        b'7E=6<)Io}1S%q=3S!obfx?B+eX?QsBEG0es7O2yc{vLRNeTNhAvHk2XZa@Y$OPBuQSC~!O5S>2xdjYi9L$piSZ~w?6hOn9_)5LB7'
        b'l_W|KyFftC5%BBVoVR8v=Wb|d>_M(6*=RJ`b5f{)2A~8rw_S8i$hW}=u!<3RYXs6!f9RaKVNl5a9YMDQiK!_&wwvku)(B>qIL}%i'
        b'VF@A^O`)y5RDfB%b>X8o$rarwbf1+r)8!v&b5is_V#)8*NFDhaoj;(r-spz84TmgfO)nkqk+zFeX53{1oyNHZ7kvebqxS~ae~*_-'
        b'ZxTv;!+{a_!w}e<F4<_5d<S#RB3F)=M-e-inWHpX06=@0({xw)pj<S$rrCcgUuXil4I{kmKbFs+kk?+m7xug5Gv=YxXDH?Tj-yDl'
        b'1OGE;i9yHx$oT%IJS-kGB%~X3jri_V#24P=65@eOem;Nw6TV*1ea9<7R|OuBotKb_K?T?%kZ)sHP;vH4WKpH#^Q8?dVR?U(x4?ra'
        b'DSc><jV|w>^iQlDDChT+83Lyy$keFcGk<d5Re8FcFTrT$sr_N^g}%9L82dKrKxc0`I-xp(fGht}euNlE;+0QjPx;VC<sJri1>lYV'
        b'Yy|3`;_Gxl9Yx!i^1br7qvZ{*c5>p|Bajbv4?1MO$yudg3>t9~SqXExz5}h~d7P4ZO*j?M|1CEeFB+Xu^_E8_Fb~rGBco=4ncOOI'
        b'{=lUQu*me^73KWEzJ<_-87TfPapox7IGI{~$M?f@%hrsxsbFRDWjKzFJ<Vyf@tNuPMBVPEB_c1kdkcc)n1YE*oW36un{F8xAF>3U'
        b'!5yXi=Gxh8M5W|pu;9?i0?ueKwFXz+=lJoPsFVIn9V%p^mPLan%3&h<>Palwcn?VxQw>Y(P|;V;PWdB$;M<O?{ykA|4G-^Gln?S4'
        b'*<Z2cSy|;&C8#tLP}LeihEk^ydjI9K!z?7(Lz>M&P&qP6{UD)$k`{&Jv8m<5hd`YoEC)Hyz<BSQTL&c;QaFru;UhqhAm#jML@LFb'
        b'4?@ReHc-KyQ0|ZtMKLmu1GLFcnw|l95`p*Q81^znN$Wo1ecZDDQSRWuzbrw}cle<H8Vn^Beaq__^saK~G3o@7#)znZRDy34kIWHH'
        b'#4RKd`YW17Vf_O!*=WF=cey59@o3CK66V92qEO0`hIlEA*%6=m17}Ia`X6(X_Y`91XkwFB#`%@QN|hNO6OZ_vRH^%Du!r?!Xr~j5'
        b'pk%E;pCZT>m4lMvP+{zoGT&w=7+g^8w#!#*&ewsyJgrTT%pi7PUJ_CPlz*#`_f0-p#!J!pg4#zMA5qpPC-1BWsIABfV!uH(V$CZ-'
        b'&amICk6oaNu_jpoj#{Fk2+J9I&iOC|RU(A>*l?FG5Sl*R#qYJM(}mEIfN$wS*)Q@swxhfwe<he(qmgpM(E5%#O-#{_BE+jA06Hkh'
        b'I(OgLPtUoO$Y%*ra7Lb!Q-$7{AUkeLefg&EcKNoDQ-u>5A3n|C`3TVx7HeC%YA%kt&?IM1pf2pPnq#fziB3fC;<t0v>8gp0=}$8z'
        b'<;znz&V)%g2mdb|)0dNdo`3_`O=kGuu$VU&Q<SVw9$0UB(n_G?pg-{O5A+O<7io!pE&f0^JCa%Sftu*g#)|?jIB=}+5T~@RPmrs%'
        b'6I+mx#^)XwiT*`+Q5jJ?123{1i;^oGj~q$@1y{YvVepa4&MCLAS7?7`w;>7K&zr%@iuF_w!iT_2-zNLIsKxjUmFa_0AFf)2ypB+T'
        b'(V4#-<>>evEfHDD@AzxAk^C2tT3dep#3zwz9COxjjkqAWS(Y|^LD83C_EqbT-YTr+mbfWD5T^y}`FI7RwIaYH9kj2M<gD_dV50UU'
        b'hNXlbc)v(R^q)qEQ+`ev4*y~8Q_1lD_j!}{Q(B8lbhc;Gp1YFFm>mS^{4W69BUPMz(oPoc=lXAQ`sq)!xG-|riU%ua7X=Zidoab<'
        b's-kC)YUN~6(7Rd!qqd{iR$8oo0T#J!8THnRp!}khZ#v|pElOjvl^3ar)XmrjK;yMoQ2>#;5sPF{tSj$}n7$>f{}ShL3slvd3m2i6'
        b'kR<LSBNg$KjG`T!Z@pqbC!g70gEnP&y5UA#gyOgci4@-m9sL|M)@TqHCSi?Av7&oaE5#!th}vFGCl#-Gn6+5YTP_E5v-ARUimWt+'
        b'E<5&B$8vO|)rY=LN|s3pGvq9%-_Fd-Tk-4+jsN<F6qZ`=oBc*DzN8aybQW@{h3L)>PIXcKb^AqS0_>`wIt4N!(}>zbT(Y<K%_-MP'
        b'@3%|p4bAIN95v|Q!x;YIDT$no8=BUk$Z?8C5~}X-0-}FE2e!`PzYw)=abQ<_Y+Of~c|=TpGK&!H<}7LClfmoP%8)itM&U&(0){E#'
        b'T<OZu3i+*ya~Cz2FItvjWfWG8Otb2N!!LZfZm6s+rA&;~0q8+4)y#SPiIX!3(PsD|a0!Iy_a^vFQej~gpPX`poq{$xI?6#z+C61q'
        b'RxlVr%c)Bu`v1oDmvWKDCDi@207CQ!PI<OW!Tf_ggXE1?N-$DVtDzW;|FB$yBtE8MK#vcwou!v_wv*oFoG6#WTylX|i7C1-4ofi<'
        b'i%i*FrWpBx?Lsh6d|Ke6$RMI$&%xN3He{v9QrB>xf>0`Yv4CbYS&WR1pqXqDHUBd=PyfO!E>(zv72*==$FviKD4ok>fOWkEoFZ?i'
        b'N4mt_PCDP<^r3%cZ~@GvWJabR{yXq+(Ox3;4;<y16GVt!;6x4RF*PpH+9df|D_6Wvh@R(0m&>zs=KM5G@?x_?5ZJuV`8wCM?loyc'
        b'v!eSmG%xxSVc=mlOp_?;$jAkRD4GNO^@q@V?RK(g+H+nPr`Ued;}#&zo>UcZl+?Mz$G?$cBO$st4rD}0flB)^O)CYpX8;Xv8&}Iq'
        b'AT=&ft}KhqUpcCm$EIoWm`uheG)&)?{z_(`jFV3@v>tlk!6l^!7sB-JAysKyYR@?4AOgKQP7x!D%KW7a$*~W{F=ZZ%W4kh=%t2tb'
        b'g928M21C>_u3TQGaJ<L9ijt{E$B}yGe1%iT2o<j)5poSJs-QTi1=yV9Bcem&6rp*(toHGwt)xsv0QKEi;qPE5ct1<p$+K_v#WIFp'
        b'q)@#@Wqh7;q3=I!F27wFx3El^RF*(ep|EzVN%W~&i-)x-pDi10ldBJ6v2C<NhoKO{4=NujW6RLBL`#B%vCT#YSud?cmwasHY*ZQD'
        b'RzMM;N6fVz{_rm`dm2&H?8Y1nmSLpN&MKQR4;@W^um)YbIgZjO1cM7D<7Sj0e-x8zsk4Pk9iO;Mr%{wKb}~V5J6`Es<G#G6GqB7a'
        b'SQd?s31ZLF)a&fQHT;nn3jVe=7Troid*V~jH?3qt3#hv66hzf%@@c#l=XtC_+L|;$A4m@aty+`V(`$KKu3qi41&FHxis})vkJj-A'
        b'CKfw>pyZ4Y-Ed*Iqc&l+6R`K!@!ud#9^E-WXEgrp1p9Yn$VG<AhrVCu{(hbP`*kkcBcEOJ^zIlk0l>bFMOv5h0jFrgEivK)>C}|Q'
        b'Y?6v@M*5>x!{3SjWv>RlX-7x*i=++R))?&}?6#G?xQ;*hE8ODq8|excfawMH>Zb8QY1d1w;b7mhfA`gKR*vg0k0rdSh#xzGACdF0'
        b'Ni6ja_X|GW?>R*%U?OSgq7s`yHU0&GU*lZ(FHTVc)kFs*V2sMC={&x_s*C8V`i_H9IFJ_^7~Ieo8LnXLL{YpXV@E26W#l0`WR##='
        b'x*65{^%>tiMXwjRM%#fo?4-}!cEpg#2&yjSZ)1LI^hmDa{C20v>E&vq4VPQhV94mDW9?$zk(En{$%g0;g&iOFwu?HBn+tDn10_~r'
        b'0-j{87q+V5BNQCK7sp5S6*{V_3k{m+`^NF)vjzOc{Pp8+N+-q?$aaN0a2Bdu=>z;q#uZZNrmB3LIfTt=5i)kPkz%^rKgO{e*YS5)'
        b'jfXI{+{ZNV@w)L<Edo$Of8^k+Rpa^?E-R%sExw-$WkV4g@v$1A?+F1*i6{bX=(Up+6D?;9gsKf)5xFG+ji43a&RYWCR3aul@|>bu'
        b'3{vhqcjj3TlE3RAK<eM*JP`tg3G@tr;Qba-LOum$DwGoODH2lOZ~!Qxlm~?3A2|OG1BItffk6OkfxZ3)Dp{<^9B+*n2zA(!j|5Y5'
        b'*<{qCBPzwMCzJi1*f)7$-Ovl`C_k!t;|@jRXE`0s@|Gr$k7uTYojNywREbZgG+yHG@=S5HKGV^Lgy)ed_WxMdS-uAStfE@bzg+Yu'
        b'18ria0}{4o^ks88pPnb3OfEzfni2S>Ci{nP?AmpIqNLSviN7|L+2KoPqC~NM+PaDIV%~03%GM#(hCv%+T1FU~B8xly#sUGa@)?D3'
        b')H*6y_YyK|;*4t+2#`jes6z*NceuEJLdMH{hI$xvrZ_yCSeI`IiW9Gke4Y^PL5fN-Y5JtJ2tiv-^2v3LZ%n3NCMiGla)Elel$z1;'
        b'9_>_cakrr9sniT=2_^L*pbF%^2*Tr{*FffPCo{crj#|7z5R7hV1gsz>P=@X&$<Sh!7(i`ZAehOch02Yvj>pTO#tRc)i@g3^+Sf#C'
        b'6n|yJxaP-+`y%KLOR*(C`?>tsXNwjSsTQoLkPun1B31F|dU^I|rAc+?ta9^qvnPafgb<bxL2p}c{>no(+kNxCg2M@fZC^oB#kmUk'
        b'u8#8R4IQ?iO0lgT?a}vEm_NuMQjM7YRtP{!T5v92p7fk9kSq%n<mq*<l2mZT^Ef5cy(Hx^njy^cshdX8f^s5tEjH&qAxgsH-Yd;^'
        b'mQq2?$DHwkWW<J}NP&N{qy5ZCQ9WK^MQ`-WK2GbXkpDlz-aVj+D|-N*nLG$#ut~tk%XTsd1ghH*tUOv<ND)zMe?Th&f+T^2S3#t<'
        b'YD;%Bp@jr-7qHtBYIi4TsYqodw6*x4zl17P3tMpeUfo4oYOS@U)>^gJ`R=`wpzi*@@B1g2xsP-2+<Wf5=bU>UPeVN*TU<cpyurPe'
        b'fkBE49tnXHbS@51R{g;-BCcU1+h49L&dOR^0?VKxL|pnN`O|-9UaTKz0GX|u9V%EL0Mu@;ztkBbt>5FRca*i)Zvr1(KNI>{(v016'
        b'OzwI#5PW9eDe#q}Te1ATcXr8lIYPQ1^=$j3@t5|^8p~!l#9KcxJXueJmT7qcWG}YRWOGFT)NZPxBQv${g~dKcG{4U!*3@S_Sr29T'
        b'kMgW+{G)K!L)b$m*PE$Zkcq4IBNN#)S_9|*XmIyg&y|dkN3e^J;Hw;-nV&sJpS<`8G4hB2ERB}be>T6uVPxQm6Ed*HcAh|Tm3Yju'
        b'+0wZjn^z-hw`EwD<FRQ(^9x*i`_G-riL6cz%UxYR047aa1bOrVfni&XehutKp`f{w%R@jaMTwcP(*>d`L1D;f8)ta1o)k5pg<*{o'
        b'Ymdm13ktMH3I>|w7Axc>JJm#TmAoUR-n|6YbEpB1N~gcMff|BC7adR;M?!T+d$d(79Z?F#vaL#@W#@b?3nkRrEGa;OVG)?mZ*D}c'
        b'F^-0rpX|)q#4&XJz@O#aovjY5Qi!$~i=`Y2M}Di}1x5Biq(jvaS>Nu{p=$nt>%K5D2Mm|xkbGng0R{>ilY2gZ?y3h4Q6qB%mNDFO'
        b'kU9#{VL#cDIx+e@M+S<)e%HFaQ-aMq8~$vd`9X<QLSSHtY^H1~UU32X<!X@Nmd()g5Zdg6z46k9#xJaB^Xm%Z<ytp&J}+z_7Y_1y'
        b'k*CjZ@bDWI6g(UaBDc2lTPNJqhSVc019}AeqlWJ(-d)vDuai$ofk~2)y~&<~uz|r!C^vt~9zHl$FmO;lFa*c{#NF7)7(R6hR`@)K'
        b'k3(45c-60C>L}>=WCKd;xpY(hP7GMe_iaJ?KQ4i&Qy^s71q1J7So-Ac3DnHX@|j-w0Y_`!M4x=hA@6fI-`&vNO&1FDSBXXhf{w!*'
        b'JZ$K|XY%e-<I<^a-1)y7g2p^=G_fwKy^rc>uK~?{6AT^`-`Ft4Ul;~!|A9v13F}cAses;Etxn&pJ(2Y<uA^teU?8?{9WnX^7x{*3'
        b'1*W|3a!2omfnIrcAFL+z_HH2W@Hk|kb@(k(k0!LkwZY>F4H{$5<DS1ZO*yEkB%E?ks(RS`XHt!W@^0Gz5+?Y;mv){+2h~=-d9Bl@'
        b'gb20wdUtj@G1qY!J8@~k;khrheaEZqovL>BQqaMHKCAWUgJ1Mv4mqHW+q<dOHZ-zgH+NIk@_vR!Q$EuspV=WlZcB53f)nthWa>BM'
        b'<Xq~uxx$2i^eYf_W=mH{@(Kv{`7==B9Zm*YKHo86*~Gp*GM18KZ)!`4g#2bl$p)~v%u&mn<_!}E@m71EEr&-3iS@ng0q8RTsmZ#F'
        b'Hw^HjE7`fM^K<xh1)pOf>DZVvhsUtbp)F5t&W2Wd5fp(HNLaQ!r;o~ASfhQf06c&timIojqV0gm-eB=<2ct6x$M4(V+BM@ta)~EN'
        b'&VmytxIKv)4<2MKy!vsfq~{0jrp=P3y<C%=F<_U+h7h9*u*4-B(rj&2@H~*b_yke_m2@oGz)P%BB}jd_L$$%ud@sye!P?{+9xGO$'
        b'cPmTr%8S}6RCh&7(=Wa~6u=3+6;6u!CBZLz`dz+sZ6&5<p$=-7Iyn&LrK+K5DKYexJ|*FNopaTGSWsr_{H<=#g>`;`0EZ9oIpJCs'
        b'uD7A0<RHEwr+9-8i6neGz3OBs-wvv0eGT)eUWSiOa=!7gpz*QEJFHdakR^%V*CFX-ii8)wrSe1F-Z{7P*p2q~O_$^E;QRM=oxgub'
        b'&*!T;NZP|OKmB!`_v<>aj}EePTx_gKF5qc&=1d(a9g>h?1FcN}+d7?sxGq_&K)x$%PFG}mlBd&2Xu6wVd^$3)*{8?Id|U@j)of~?'
        b'UcAdmd`D!5m={pIVc<3HWJDBH_WOG^R6ILYw_EaELgO_^&695cdiV;LAHkslqp(1Rw{Evk`NePKYbzqMqf-Pc5;BJC`iX2|sxa#!'
        b'9FN=sb!t(*QRLiT7xRgDwbU$?Prg&<eFqHw0_Qt*%vMN5QzO(M%fU+xr<hHn#tuxn>%4nGk$C9U8p<wu#MT7BQuGU276*6fx@|3Q'
        b'iDO<B$BX9Am|hewmF9Q<#yk%tm%L3=P=65Ps+;9ymJ(J$Finsan;e=H9Q_5XOTrSrgXxB4w1PPlrB6P9H(vDLj{=V6g*u<gJ)k>J'
        b'ch()9)AlgW`#G09ehOz@GM4tF4IaapHdrt};)V@RP@|a9fPZbSYqJ9ObtThW$Md8D#EazQY=T!&<H9{h7)u@6#%+=lEN-#JjP>rc'
        b'GmZW>11d!m4h_H!3zGq5Kg?#B1E2Ug+*H?bPc<?Ccv#xb(;X6~zOM5%3?(*x=TB6fuI<RJgY6LHUB1njK(8I9I`WZro2;X}&Y!3b'
        b'WQ=tdTE?iVEi}dGVMcr)g2?*dp;FG{mA>~tbY|0gF{)2SYAJrF3PkAb%&h|_rpsyZQSg$EN9s^%_v*Sya}|t>x2kU7W{n|<GrNvI'
        b'0{6pahNKhxhA2g~9)HH;<2=y5=*_5uv9GuJH%ET6OszXL$H$;Z+$nX=C3Uj^B);krW^tW!ah<;vo7BCuifr`j);jO0b04boE8U_b'
        b'=I*+|z5hla{Gj>9{#5CIcShH_qw8i>b?G`kIKF|q>R{@fx1|O;zo;C(<5n6c(0Q!VcR5xC5U`2~L8x;V`MXndhVK|*17O-5n0A3U'
        b'MUZ!pjet>vX@RKR9pwBAAZ<7pCJF0q-fNJLoSFkmlaVmz29lBdj!*IdxQfyqxV6}&S|3dC!h>agfJq%wwa)KrQFnPwd3#{T>00N8'
        b'%G;CvQR_6;+@ADct@GG_R7|UN_W6_eaq!=5G>iyG*z1EVGUQwZLoJi@Q;DdyVZb!^e8ANbi=<;kV{4+CwC3dbGo9i{XlR#4wWsXR'
        b'v~SwEA|369ZAW|Ju-(EvU%+}X@t965)UxN2L&d6hYe&Jx3ceot0D2efXSh}@iV`Nj)ej?S09IQ3Ew@Mt<1541hYOOQC5%U9jRa)|'
        b'WR1n_q1I@|<|(Izt_6U!#r31qFy7Z2Gs5K;2{qKu8rzeUO{1}Cf>fH64DesA?G!+{u*DAV-(5Rc(6tojE43$0%3T<!4c#*Y#N35x'
        b'7bKI?>M~<_@~mHmTB0E~Sxu}^Jx#}F(Cp5H*!aXP86=?{jf%%<u_zmlTM(`m$Gt;{DU6Oywq;mo&(jSJ=46t{ih{ixVPOc1fS4gD'
        b'mboU%R<&&++mH|YFf2PHoeIrw5IRp+E>Fu)3z)67?x$;8t=l%Y9F#CyY60ork`_=;Ybff{cSO(MxZSy1<tGn!C2kE=hpciWY*yor'
        b'#7H_G-<Bjk2_2?a)`H1U;WUf2TP~5|V1wOGsB<k=4<NMD)nz-M@0G)7wtd_Msj^i_248#)i(4w|pEJFO>ylHMo&<+O4o>DT-t83~'
        b'4FY6&pJumcXYU02!pWkE5zow6S-<4-jpqzk854<JVZJeZwsF;|(eJs&i&>}nvyBWTNzLIVk7rW}k$+N59d62R6x$RX7b|Ed(UMv?'
        b'B)T9xMfMA(KZnE7EkquNg#7~3Iq-hH8#$Vk_Dn&CM8~ay$bz{$kGi6hp$W&-Dd9r$z?-doJ+E>nyLHjYy2F&NELj_!ocuPSN~nc;'
        b'q)q~yv5TZxyq%AW-NgL9!e>Bv0E?*%AfXXyWk8#BHoh@`7>r$<ytCGOXKmDZ=bg38+wfF1fnwd0k+t6N+J!K(uAlaLlgd}%lZsle'
        b'vUZS-b1G_?-LUx15CGX6(AGD3N3Hjc+Jy(<NdXV@ze0Z-%<tg};&pNjSe}zm9v1d=a4rMZ^E1a*Q+ZBY*(V?a#@-u-%Dq>)5<#;R'
        b'6sB@6Syfmki|4%5)L!7h*2pz$%Ag1G=|6I>NXHI9osgc(T;tDBDUUrs<s6~<#SXdYBACr0x<AnLCoU(+<JV=qKaiBf#mkv*9*5+I'
        b'T1_-w0qex_Cy`H1_l@o|?NNG2(My<`h~0U-j`gy~-OC;yCzw@`NU%DIfa)kl#{;kto&6j-o7#D+A&Hg6e6XC!kGqp$y`{I*TRdCO'
        b'h571H|5-2oad$kdcMq($6k1gTR41qoJx+$H2}pI@oV`TU#bi1HZdZM(cOFkjno5$>P7IkX@$;$*uYd>O7nDt=npZ(NWEMNx-M+~B'
        b'3CYoAkGo~C4JB+t3tP}6zWz8e58=#^<dXV3O0Gct>=*Dor7JP!vU%1%1j72Q#{F9jfF-yE)(#%lcL>%mHGWw3|AO`9?XbSBaeoV8'
        b'&D7k4W#M6cj$nP|ht;@$7M9EhYvOiTpVqiPg|JTD0;`sXHHu(O&cfRIU$BO6gT<6Q9(C0w=_eqa3&lt_XI#7z4(Q8d@WePZ=){;K'
        b'H9pC__W-=H@A|-FlX-{Cp4qYgAnOtudv}f74g2-ZE&W=~_lrgSdc)tZPA7KTfC2jIrQ5&pFE#GJKv=KM!YW8y%){CaOGah4bkfXo'
        b'H7*3HOX8=4(2J{|^T`t=%pYgl{2O=MV1PECzP(MR#?8PsTW;z9Jig6()c<E@VIe-|w*FV#4y&%lT?b)px&@YyhgE`LRnEfN`-lJR'
        b'*JHQCT36#<2Vog%kfjs*hK5ZS<}VgrE=$k-p@trb>K8HD2<SNo)F$cN^9P$mqgjxkMh3U-Npk4FAO&$h3Q+id^Q@IKv;*<+F3yY^'
        b'cSa3h7MSI;olea7v}SNG3W9zQtduxeV@oop1X#`sEZc?lq<$fzhUrI>dIiHo&sG87YaZUB8uuauFR8}AQ3Qh{O6946_H2y;{$_|T'
        b'OV_w*_>JnCn|sQ>ny70wN!Ki9?rDlkfb^X`p0Amxg!rf~)YxQ+p=J#&vse*67H0jz#U((x&z`zn(0qw=2BCsgfH-nW&FpN!s^(c8'
        b'(wA%CI<SFF6wX1{6^ux4r#g6x7f3a#WgXW{U=%^Rg>s9p`gQCsRl6@$!*9F>j|v#J2loA5Fkk^?+L(T>UpTKU$#jfUHPw(S)P(ME'
        b'l#Q6ml($FAR%Y)(Y(c0Gg+kE=XL_AOHhvg5w#DE9PGD%`n;M?13vIs4&s8>&N8>q*DP_pq#0@ou4K<p@GQCNrPonaF3K<6!$gqg{'
        b'xY}nmbuY$@RZo@4Tg{c?lj2EJjn`D;G}jC|S1~`r!wVYmzsxCDV*P@cXYeg_zaZc&F?u&tDsdjFb|0!97ce6b*cO_6m}Q0Uw-C*-'
        b'*v>xYk($BxqHL0>g8=6a*pM90C#VaXcb3SC!P?RQNx7ffqU{$bf06VIb6a%a>8vE?7&nv$T06mQ0e{L0Nz7+l<IqN3jip((xl6I}'
        b'kJTNyaLQ}}yn2rvYS7xm8`Em)ZL*E5sh%fk#gR$(D=R{X(Gd;~UQZ_{{s$a8<+Wd!xSCGXHwWlj<H2secLNSt^QRnW_$5yK1!vmN'
        b'iIJbY>BAiFFt6t$F6$Hr?Gn%PacTi3DhGwBiHUP-q9kzj+VOam&Vc6`giMVIstg9#*t9nngce@<mctCU3}CrH=B0WbAgoT&SdlHa'
        b'Eet#?nzd7RnyTHVYJl@K)witc>(5<&Xi4tXYOs*OO3j0yn3C#_8`W^H&?9jZ*egU}uh96no@|qEIr|JMA?!!0-H$-nk5&8E(_&^-'
        b'HQI8zkf0?npe#0u@H3U9+R`LL?B~ucWQY%PpzrK{{32jLvwr3pztr$MRABQg{x7a}FGl#E1{>1t<=9M3I@p~a6I^~s3&^9`=&0Bv'
        b'IyNMz=TFe*PAdodX?h-d^xFaTdwZVact2o0+c{{ft^;(Q567MJtKIYAH$+$8+(X~2MtdlU#${f$|NM>ruk%-6x@`}YR=cGTmh2W-'
        b'ED!5yIfNzj!)pBezs}5=@>^j|(DF1o@nuv#T1~W#kior1r12JB#oPCT_O_d16#-^iqS{g2ivlS+|5P2T{h5@Sbu-MLU?)`Ds;NFJ'
        b'<cXjhXB+H`i1`Gy6t*e}(nBdurn%ZDPEr%*P)HY9X|1IR@v%lND1WTncQ(Uo1X|m8MT30R%=*)vu*x+yOUH)lDVyA4w^-HK&amFf'
        b'#$TBWi0?xl@?);>I+*(&BAPW={>7k;Rn@dpU<*)6q$*Q2*#04zJ5Y{HA>C!wU17a&S*6*nM?)u|6Q+So*~azNNXp>Jl-D1WrTc`f'
        b'(3o3dUb5bBu3XQXbi<^<gvE`A(+|qXP`=z?_2M)~=dn;I@$E(&Yoh?{cR4wWb8d3*DS;UunfeKz`c)OiY%8DD7cl&_LeE>LOJJyb'
        b'bf#V9*KfSxSwa4*A=un>EYq2|q&i)d5ucmpA|vC{i28S^ap9=|CK=AgxYYOs=e(zyRFFv(2Wk@&tH%Q>LwW@%(N*$P)dz{Y@mf4J'
        b'gO0`WN65rGt6kC9*zsc<r#Ik7Hy(<Jc@p0(&_-jnT+PsvmLz%WtK^-@X*fA&Tv-1pHSn&5xf8a*9;dXR5oLAqfk1V}Dsx5W-)I)s'
        b'vbaHBtvksr-v_TE%^_<^ale>)wF!X#9M2Fz#1Jw$@N+j3)kimO3D^=4tC&;KNr=;-(%R^Q7|lYNzA<ib<58+T6zrkAEXrE3xL-J8'
        b'2w>7-<)a%1RbtJT(90hwjX4c=Oc=u#OFUC<R={wnO9P-o#J_XQS%}4nUsY++tfR*{b98p%nJQy6mM_Mq^?3eDjNS|IW!i+h$}sTF'
        b'aA*%Z!FPL{8Q{~|S1qIxe!G|qKCq9OszPH6+Jdp9NJVVYopB*yBu$3IE)SjjxXSx+mGk4OLFYl{e;_xfiH4?I(;sj=R2GcpN;v?`'
        b'z6PK!pN0AX4>ilpVI<w`;TDOr{+Hh~E@xJeB2r1AfFt=wM23A;5S7KsD?-&^74js?{8k1rS==}}6xJn~dP6?dBtOuXW*g{(_Y-|K'
        b'bT`l?Nly>eJ7nqTIP0tgM<esMD&C6xyE31t)GhYwfHxLVkD*527F~X*z|aNT%@!-)5@x)B+7&YYhV|6qexXg#MS!N#Y`z7=GY^Sv'
        b'<(ivvKw6C@eq+}7DZ&r`k2c4QU>`%&Rs)UY&*Q+z<<WvlMK*1!!N`#90Xa=gmoxFD0f6$;Xg1~lbX_~jHL$_S$)kz&RSnVD$rkU^'
        b'Rpd4@g4tSy9O7sJuX_C2aDeF~F-QybpHSnXeqqlC&=jxeYWiE0=|>KR7Kh*Kb99xyDgQ0;<)+HqVl>VoWtT`*P=#dO%&TaeMdY&o'
        b'&vEV-<lI8Kr{pG<=lI54z~uQxyuIxIqE|s5#FPnI!{slL>}!IynH$q!HwprjqJZ2bRcJ@GqEQc++9BUUs1<3BDJ$4d!S;o2fm&No'
        b'9~v9Lku{Mir~DI+I-`~}zUA|ofnHNGwwHn9-ItWYB%t1jm`c<;@hx*>z&6HKk;=8ngptL_d6%1TGN9f}!JfV-Xkc-wV#jr{>W(Vp'
        b'PGFB3MOW|PeiL61p9&ZUq+1mZ&`k-!!>s8p4nn`>+YN{=(aCHIavmwPEZ>oC*_1-(cijO-Vf22iQm3OafC`th2+J0V47(hIlM>5j'
        b'Dxd;7_jWF?bT6+Q7c#5i5zzPxyGsLTy8PooHsh8&b%PxTL~p!2W;w>3tyD`+j(C5pB)38HiWyj*Ia9e?Vg-0oEg2@J_Y<Gt&`6Aw'
        b'_RMhb&-5>DTnry#-sfP5Sn$xvsTNgEJti-r3kbup%Emz|Mpn_OFwCvo_!(3+P>bvN5rujubPQ(jRt~a+o|YM6%K#az=huWNW(BAE'
        b'N99rZAc2v=X$Qf2x~p<ly9|Q^GV1fea=B@#k;U^^jNb*mn^wJDd2^&iJ%8kW6I~FU5|0ZTe=UR~eW;QjX;F-oyKRjbuzZE^@<R{g'
        b'zE%mUyJ9e<R6r`Acl~(Wv^>ft8p72QTiCep*41o<m!|-&Cngq8zl6-0ZdtQY+2q|VirBazNFBT9m&aNoNLyS=%AgC2)!uPgCnHw@'
        b'x?y3^Wtwoumn{mKKQqW$V)K4>KVP;l?+5oC<*~+d^vKmH2^mBUHGyNE{LKBXu|@GwT#Cy5TUl)92Y_SW*Lj2-a^EOxQ4G69<@CrU'
        b'QbG;w03>Zxn0pcw-W8W3p+{z{POSL?7o`Smw<vbdBNwc%VOi(6sBhf4<t++pT*@O+UG58IE#ROz#l@w>Mpg1}&7X4*2ek|mfRc{d'
        b'0=fs1MnB@*XUpi3Z<@d2qK>+&D`DD)ocoFqd};GIM+QMxnhR6NZLt0^08LG<GLI0Wqa1nnW$=HPTNt)52xMjfQXX{fUr~X>5^8@_'
        b'^Sj)_f`?&-_z>qNDnPTN`?-ace6!+rIQNeg){)Q2K+FCe&2Rd~INs{QUQ$qTsZT~pVjIFPTkp2c4sSLbUI`dpX3_{T$BKrR*<W_q'
        b'_ye=BEbAIazR3)fB`Z$HC54bXz!)VfK4D%ji%Xhd+-1!dIr1Nj(U`0lVg6Q@tUUzsV+Z#!&lu^EA4mb!v_t$Yhech1pRdB=Qc|PJ'
        b'7#09~AudTC^$@8}R<u4WiA#DOjP&Tgxu_<lyDS+EFX%?{AiTS0qAKZ;>8$U#g()qH)p0423&R&mpoi#>xF|{7enNbLyFZ)MX{=4n'
        b'A94#HeOLnPk8{jHGpv7{TUZ7`fwZF>(^o-{d=6%dRBP-zM&IM2Y@`($jl(heCN5=ul!Mt{@zUVkq=UgKUs6OzZGA~`XRJ1oSy+)J'
        b'!WI@XzgE1Y2#!mgvoMv3tB6Y_n9CJ#%obKLKY^T|#6RB#>!J_V4;8n<3iHAG_9m<l1Z&z4>&z{%7CsU8rfl+bh4*xY^K?a2B(nk$'
        b'`g@G<GW1^+jmT$ZFnmk=XGOxJc_J+T&nPJ4MJU{<ls*fU3XgH@>xiuh=qILsh8bI=wNm7N{9jz-6}DGX&)+SH6Qc8u;CVWXdBMp0'
        b'%lO%F^KOUl%exickqYO#6;U5Bv8XS0)R%)5h%EaSmItGlVAD#lpd@h2YO}HYCTPBRj_*+k=#k08H>>BH6@gsj{;2?T3z<58#IZf7'
        b'$6}_z*OPx3{Jg}%XW|adncP|7byhfcRxm=;i%M85*HMAaxMK!%PR5*tK(nPwrBE1d`VjD9i0J0sKcOhq6wgizm;xhzc<ndL-s3Wl'
        b'!Zei)!X%itU`Aqdg-)P4nVIo?MRq9kh4Bj@WOOWUn&xy5shH(P{(SB=`2Cvgvl7j}gPeqT5ym`-;BBh#aS(q+W7SaMe5)Kvr$UkD'
        b'lg5&S`)t}OHGGP*rUImBQh5agn5b22Ix3*t7dcl;!F@OV{7Z+S;?{yb6P($4>ni>;<vpWcxk1AyeP6KI;NvE4*{i|XaoHMjIa=m?'
        b'#_WE^3{FhOj3g>zPzd4(v)MfLg1p<-C2@vSG!9wpvRz#YXQ|mu8*jVh<S!tDDxmmjqrrb2_g&Iu-P`2dfWZ3a4QS1|u;P@Ul^&uY'
        b'&BatA2_Vrt&F#~*laX-fKfjT<pke~@oI_evCI^;5eh9r-%vanAS~x-zLqxA)Vp14$iQCQOOMjQ5FcO$1eN(KGXnq^ZJA8eqc;7OD'
        b'O@joX^3g}N1W5*@I`fENo0ANACBU+yDd&l%`mI#{yu6i9lJ?EJiP2@aEzj<@5^8(L*r?5IS+Ya<D5g~f=9lF#qj1<ZUN-}b31H&j'
        b'O9xg#LOxX+uVH<>nkGdT@Fg+YjX6&9lI*V2iDPC)TMifuXto%yasOntprzre((oz#&GYQ5`z(|O?aqLLiwxhzF#qB{W4^uKZD8F0'
        b'H2-Hxrg0WF=+BF2<peOl=%H2YKg?aHQ>FQ%v7H3<jqzxM<Mgq~GX|2`Zs1)^1u);Ea_^hBZJOFFe;WEK915^O&CC6X@HuhvoZeC?'
        b'pExMf*C6FYm|B?#SXuZ2g;<pV*xT~l{pQAJbMj>aysi*TF9;xG^|!t@e!`n$`E#>w&)w(G9VFsW%79)tVU|y<k?BpS<$$i!M<>7W'
        b'?upDhte#pU-_luBgme?#FPrP@U#Q<KA27>&8kC}KkAV`t{HOqbY6FpgQmlLbx4vG;ZkAha)<78^k8q$-KC<`Uo>5snuP-H1cc3ih'
        b'Wj$3d9N3KCQb%`~Qqp(W+=gGvEJ-68hjnU7sCT&7-{Yvt>Ahv`f6i!6@=Sd#tN$J#=q0EzmI(!3=R_I@wXzQ>p)v7rGQcWhTH#!%'
        b'nfWt$>~$LhReR@Zo^M(z$;#%CeiJ}J#!=>6Yqszk073zTmon!O{VaC!iO&Clc$At8x0GC#-(UC_=L++G)V{6WL+1ZXdBZRZJ2A*G'
        b'YC?|wM25{};A40Tx>PVs=yT$wSs!q4ZH{v%2<3=E>Nq`O2>#s5%;^0Xm#0T7=I%`s0O63T9glFkp<-pPYH%+GFx*m&h8QMQs+<eV'
        b'H?a+%9&46a*5En$H_>O_EUwK%ud}$uzs};CFL&SVxy}CEqmu~pJf5#GWjgk_(;HxZ{F>*8OwZ#2-_&PbSQgG=fqbA=KFOITK9=cu'
        b'T}wU{!7>s&biH2aG0Rzi#<zCCkY#YUoBT;GA`CUm>V@fMd|<Y0fKvJ|lwmMJ#-b47RRIpr4(#MPNh1XfU;@B@9zm^iXx3P>JN0W^'
        b'fbq*&laZ6;nMsn*tib`+Y3@b$BuMBKko%EIlL`F@@`9(-fUHvF>n@%d)pLOTPGv^db9qjpkQpuJe0R?2o=Z6smq_CB%H+7HC8Sbg'
        b'ggk28i+3|`nznT#ku)!kmH<HQmV0Nq<gE^mL;ikz0JGoppS<MFyWNeZ|NCwi&=0@Cz9<if68lWh0nn=ybGQ^9w&ngR9X%#+#!xm7'
        b'k~gR&y~uegfoKAsh@D_wF?D=YiewKNH>IB$%s}a^^b_@G@&%Lk1(Wjy)BQEfX?T7@*&$7g(%8Oe=#X&63Ya0oA5Bo?Xtr2mk#oN='
        b'abl|poL)>C#OE{`(HJj7$d%$QWr}#h4hF^GEQRJ%NqUp4gM~dQc%prFcAtQxOc^q0)s;yYHH5Pi5La!lGPavNWS)o5&DY_8_<Yu0'
        b'rW-CtZ<x`^(=u}_O#la0u1OK;K%d?eCYoTM(zHyd-tR>4DOf*SR1m5bPArobWy12%HKkgZE7j-l%&3r&=y?kkLEB-b616Vm<r9nv'
        b'zKO4MP>>CMuQC|)2la|Hy{qYRG`?MGu~Qbyru;79Wjbr7Q|`<(X&e@S67AiV-oQ>Lv8Nk__zSh?+B14eBbf(a4-?eAiqA5R=5B>S'
        b'c7^(VRNt$nRoE-iMM$Zq^Cs_029R@W1JX^ft&#w+<^xPb))Q!YHev;j8SXaa9l5b~ACXmu<;IyNjPmL=y`q^0xhb3LP?^$N;P4lA'
        b'iInjY=1!Alv!%L{8879BM$Fs;pK|A!;L-PFZ@@4yE|?y~dqI;uZ{q5JEtxhzd>|t0E-WG)i*agv()hb366AeaGH5DEo|aO-uIX7('
        b'$BlBNFss>&gBh;(>CAR65akL?+G978-;OYS&Uyb)9tEXSC!qLpw<y2wa^uC(`!Ou>VSTa#e<i4oM#6DklQgyziEK2bBK8)UjikLD'
        b'`kaa9Nk!Fn<r;^aN|LqjKvEu<s>Wsa;y250S<IrF739q~Uh)dy_v<@%Ak|-LE8cOc{APD01;SSZ$UR?9=MH_Lyz>pNeX}gb=c;c@'
        b'Xo;XcZ^yGDR5!aEY-zI1xW8(8bkl0y$8cUhR}Z!&T9)p=&e>Rs^c4HW$%;T`ay@*3i2Zl?1QqS!{v-DJ4%kjyj;_B<*UrE@i41o+'
        b'9FR=y0$4=(s!-KmK9K^x*TNK+`tkc+2*xHP71<Iia=6sFAPTB;(@x*rNqH2L>+6A_&BeIa&&t`Ezpdxj7CpPR61&S0)LxjA(N#_h'
        b'vF}_=7o4y`wj9jei|BIY&*-<Ke35jwWULRAe|f!+&jJ<t1(7hM1oI+lNilo3q<X$wO;~83|2cr$%f34?`CPg8xpL=o<%4V%GlCcj'
        b'D}<f%P}y#L9QrpK#u*a?w31Fw^5p;Yn~%478t@!rYPe%|N!nRaa<{0xV_97I1)F-dJtK_`3-yL&{o<Z(oRpX&h*1iQTtkLihA7wZ'
        b'8#()%*sdMz>tro|uGPOz#k_>?dNi<KZ2B|)QkiJ12nvp3Bd*X2Ea1#V@~FisGxy3TOUk_^<<9k>yT9_ZCTRmX`I6t_jB{Jcj%(6{'
        b'luAe?c>w8Bup{ex(3A9mP5t7SejzzGr$_@1F7Y|8M1tInz&@h;nxDAU((O>;%q=Z<u_TiXM_{{D`K^!~8x}J8>(OhM#GO%2QJFI?'
        b'e83@d&#Y%1fT$8;ugbwIc%Hns+#xv{e0odiE96N#sUW54t|pe<G?wOZHSH;KsO`Z>v^Eqtz>0Pyo$8gaZ)nc8iU!=v;tqbeI<PAq'
        b'8VB1KIMi7@?@mU*Yx+JX6H`9RQ_iNT{ApfnMThQHtkAjDo&Kn7`Jai=uQ5_YhU%9!<*_sA>6_LHi2UbL@|;-Cqq4ST%1@GCbS2w5'
        b'l-Zcgsgxw|Dx0r-4bPZUzHv@@dX{DRJ99FE%Qpt|&&23IFdchid6R@(FeW0u0*AJlAhI&B#;?eqmn*^=KZ+8;zr*B{%N6p*xANHe'
        b'%N2ond$}4N`A+)UCilKF7b{^dL4oe>T;&%E=asU?Uzs0Epl6ixg7now7}KC1Uy;$k-e9i7<kXFuo5bYV`X<W0apUPS^5L$4{M~`E'
        b'A|h)gM!vAZkiC)NN?cBieNAR(o(*&v$f1n>fay=b6rN10XESFG;2EEm_2TJ$GQgMY##iGbD&e3ipz$}r7=8kS-FlV1A+Au2%x-BV'
        b'nlrK9P*RwmChHG~*?`-ame+{pRhZ4t(nmC}z#=!B-~X#wwAOjNjCP8c5!k`rT;>zsVk1rBBb+N7+Y<PGYr)hmIoq4KOF=Z>iDhTh'
        b'gDHNYAyy=+-?(h^pWi*2F|@Hi@RZ0gY5F_YHK{y)%@%0MT?V=?>iHCOedAzR{_!9{o$mHEF$|l4{!XVk8v@o9(;I$LI=Q>dySvQ!'
        b'm$E^27xM``Gl!(@2l0WS#CH@Oy+!%gZgj<Gy~$w+@Dc7=FeW+mnKLip&d#zeIEx~hZN;DUjY-bORDXc!2&eqwM_WMFKe@=v-lD8S'
        b'90o?a*#oaXrb}?0O1wOQ7(K+f4C0c2(F0t6Ku<9a1}K4Oeuo=HYkdVX`U}_cB_U42qFR~9;U_2~eu`=%gP0chV(X|%vqw~h+MHEI'
        b'_5@15$>yGUN^Xq6>?==6U4O$_#M3mMtvAbzC72P+&2sSWt}pvM)c6=SF3e#!nVt~ZGMsf~Q<d`SK2q860{C!vr)75T0_`rq$c3KG'
        b'RKsIf<1hLO4dBG8q%WQT+-%Mf7>R>1pgW7)e$fg-9h#jR9~yI<d#5Y_jPp8}<9xJ?Sp_?4RD~&HMYdeKm?Xq4Tmvg<D8iJlV<W1d'
        b'VKL~%bhYrMvS6?V=b|;Z8de6M!#;&Ov&t%k{C89dn?K^P#*?1SGSHy`GbKLBftFUl8O?%5%0yN@($yt{s}T7y9*kn;zUPmNp;XM#'
        b'(wHk6V_A{ryg;*5m>d!6PAa2DsOjHfWC%&H(K{$;e4e<V44oG9OL(b^8g^)iAXiu;F+hbLvbpZYVNj}=GH*<oQ&u+U+Rm(iSaVcC'
        b'2HJ{t?W|K)iS309jm|KFjIf1~ftK#3cFU$N0w8wsxA-ARZy*`OI+u-0W7Y{lnZV8h%qFq4i>7wVI|9r492V!Y#%}<9VzDv3P+i&{'
        b'2zvBOG2f#g{<O>bh_gp#O>?hEm6ccfC0SGG$otUm-@0dpn~hCiq_h3<vnKdisw+mHyz5H{Gx0L=m=0Qil=9?HMl$SZaOWc2bKLWO'
        b'8aQRruUp$+_N0%wEDlflIjg2kKJ(L&nJZMf-KF`9eCnYi8k@ZPua@Vi#A&1Fy(47kFR3^w{6^5)_U*aW=Z=QxSp202K+17j>vQJ>'
        b'_K@Ad`{y$T-}sKe9;gK=A!weaf99AIMnq#ESsil^EXI5WJH|{HA?Z;0th86md<0WA9|&^AV)gG(%p@vs%-HyAf~{9#$C-b@Dd~96'
        b'I2@2r1&SYo`GyfA8JvK4XmO&)I3A3g7_AT_zH1!jp9=+vhl~kHy#nS#J&J(@0Y>){B*7flqaX=naIXaEQM|9`<%xiHCYBOpsMl>g'
        b'B_Mxwd1cdU#Qj2M80Ist8Oi%wt-JXERtTkTPYOdxe>MK-Fv2va)0m1Ua8Z9eB^Y@f8}!PU;$q~7VBX|Tqj#s#xzjkvKEd=u+GnXS'
        b'>kNmjqRk<f__?(@iOX~tFDAA+1?B|kaT@s*HJ#^pYk2IIa;>+No6nb<{^r(l)Oi85Na$jtdbUGci5eRm$z{r5t*GOsZCsmG^^B3X'
        b'_$2t)GyLg8XxXx1f_%JR7)dj0Ve#b7?`M7VZ7?DqYMt4<+!&4=DKdvpwF0vOI+sQ=<H6T3GJ(;+$FZW=P&z1csR%NRMqg%555>eA'
        b'QLv}$Jttv+1;FQse?aty6H^r$NvWD()*F$>0a4<^#ei6b0{FN{=5t8k(5yNxLOz*e^yYx^T;a?yG6jf1ieU1P+&;`e5~&^W4D&xm'
        b'#KF0|6tfyW!iR^^!|Unnn=Y@;I7t+<uUeT84ZIS;>R|$w$@CX~h!@_Pe&m?@;Uk+y!Q?c5eky!$CK|mOBY-#g!#W7;5DyHD;%ZnX'
        b'(O+1@KggKJAXW_HE|yK%$lMK6<GRU7mC+jozUN8kWV;_{Vo`hF3al(^IpDJNSvBub)Cr1t&4AKFW@GKK7!zXT_0-`Vsth5<$j|#y'
        b'=EEB!uzgWoP3_dCu@jxgf8LiWaUK7GRW~Uc?ofT8?|9jO6n-!yxx_jiG0=OVEU7EdV%4xNO?#)t>(#5oa7lkgQZ}mbqGeDs!5jII'
        b'-u-$gkt8kKD7PH~vXf8_jUu1~G0iaLC}eq#!Jp59*b&Xdm~7UlR?<#u*f(ym{%Jh#x5r@?8alo;pv2oat*Gu<UD&S-9sg5&oA$VB'
        b'%FyxBI%FE<7dP;BQeUp~+fBvjp^uJ^Ndx&UGhu)ZXl_|2;W6vD5jMP^xPKetKxF^8;r?q#h!VAP)&}aB;WmSp>vTU+e4dxys@^k1'
        b'UG=rkx5xai;kJI$l~~WCU|$Dyeq}7E&d`6=dCMS1c6a1~m^C+4ZyLOA1390(8|<}%{2dJQGP*bEH}nJU_ymgsnxYHQ{Y%FM@CJ(c'
        b'v#;DP-+$-qJ<q^-!N9Q4=`>7l2Y3?}^DxJr7qI=psJ8o`VTxg~sMekpypKIF2;NRZm&6w4P}vg!Ye5FX7cz32(}7zJIP*tXew)*G'
        b'v9WYy*8~{^UZ3<OxA^`WP%m(%*7yIs@Bi`Hd$7|m&`Ba=&<ZeR6P{r)Xjv?80hZBdNY&;%)Ran-Nh@@ziWFU2Qg6eQ0B~Bcs<Ka%'
        b'SZ{E7Gqb_zqch0021R16fq%hL<xH*tt+q_2%Kwn#Yk8ILzs&c)68;ZC*U%<^pRmMI130sd1|);Yj}ReC6X<#d0bx=N$kPbi)sm60'
        b'c#Xk(k74qMBKB<;+hb)8>iPX-DYQ;uG^il~qx1bQg8$R!xa>S7ptc*PgxJH8pdV&EpB?QhcAxK`Mop%}-;)Vy1z8lU5R=uhG)}H$'
        b'?uV&8i~auEQw@o!hUCFeURP9=Y-pv?9&gow&*Bri6fK2-YJvOc$dzV3&K3VXG2dgR7R+=Xu1YY_1lD%ZWC(9t$=ro5B<OW9|HJ^X'
        b')w2fgIV#vGoumz3+A!#(oV0<tg2)n;!9~LuCv<{%Okw&-*yAPIzL<<Mc*8)s2gJw`XUzQqXSjj66LtF$!E}~Dr8FeYGbp9_<XnSy'
        b'4k($`{4M9}-}U6dOEim_x;Pk21w|gBGm!2Q4qbR2qDdkiSG`i&kH^cIkM;a?Uhw^Y1pigI!OG(N2*lhMDdsp#brEh`S_G#P1wOLk'
        b'5*J%;v25~r`s14*a6Sv9Q~q@3M+kKEU%s<y;lq$uV>*kVeBitwr$m@>PCsRmS3d`q`l0vWp|v2wTqH8jB|yu7uU-%__N2L51iOJj'
        b'1D|O+!u<4H<|_zwZ3L;$w1Cfz7oz;0_o15@^cDQsoc|WI+Wi7iCj9RZ{8dWfCG`9VW=x-PwbarlWByQ-dj&jD=_@VE?}ch08SC`9'
        b'>-79<vkJ?2Pj6}Uv@C{<Sw_BoWgqz2_0|UWyLxccMMMDVGaU5#iHw7KK;!&D&)*im>-+!x%?_==$;=gUQn(@`V^FWnpmYX8=7vYL'
        b'GDJAN1Z+|Iempfde&e*4L-84yH(*`pOYcLjc?>G+Dk3ues$bqp0P?pP+JHe1MDhr8^<TtO-1I#t><cej(OV^0{%3H=h6Ozo=G>__'
        b'1xNT|124h+@d^@K^`v-<fSgOc<5?{pShiyr%4?>7<ucmAr^HAj;^s+u1;gTs?!fsou4sH%q%7j5uX6oDlO&><k7LC&>ya5UTo>-='
        b'^dqbY2H`nZ2ohm59f$w!-u-*M^Y?mwIA-;&8}-yVL60CJz$kJ)t&b5z%mWWw^*uyHoH59`S>JMo0KYwWM6yxhd`b@;-D45U!Sg2g'
        b'9D_xy1?3y`JzO~2uTvDv27Tj*hL$DP>07NWNomenJy;e!zlB4Qe7LhlKYbm=AS1wkVx=DH+5ZX?Tr}SEYk0q4`Wnin!N1>EnO=`1'
        b'j|IePfhL+VvN%)(Zg%F_WaeyQG!na9FgG?VF;@LZWRm&4GtP2-&t+5>iyc}QdsJ_>eXUxn&seKRf!Lh+@IPDFjA71I`j|_gU*N~N'
        b'LT~yhykFS!Q@C@vzUN|i)^}jtW$81re6^PGwP2V%%=wTWd7%V}Fbp21%G5hEVLnY`)89jYKZG+GdSq*Two>GLP~USQ-1&e$3;L15'
        b'araU%M|wC%7C1-FG(DxGOy|M3$9xy=Owr47sh)4c8@zg_79hv;x$x>9R{}OD#gyytm~-JyjlSob@aorkBfy{YclznG;j7H%eV^wY'
        b'k?9W0Hvjo3a}Qc%2gLdBiD)`BHjfychdJ-kQ*J@bbhz_Qea}~*EfaX8^f6zBgPfi(!y(pv8Sb2~rv?Q*XTUd1p9yzH>Zvyc)2HDV'
        b'fwwR{^_F0I3cj5Vhw&-QArb)JY$Qg{`guPq9lG%84w=3sEwJMb{Zy~K&(Rg=i0%m1JCepy7*cP4NUex3<Ne!$x&;Z)RGkd7hcIG2'
        b'DYZv~#NA0>+vFWW{ghgs;7|v~N5_Uyv0LKj&zLJEprk+y$K1SSoO!PlX=paXm=CI}rMpAoA41NPRlk(RKLl;x446$pM%i(jZWy=A'
        b'ZCbEr+Eww1%uK1DzTj!8#P3Q6ps*Mm<A8V6JWBNvZ7Zjw7`v<~G6`@zP2VdQV5W(1p6@9^v5%scsHRGJrOw~MY3%rC=|Gdb+eQYF'
        b'txvVyl`T10K9M9p0Il`XQu~QQ!6G3OU5MI^Jh;jRsGPeBdHK-jHGljnAKc?UxM2wH`~UxNgKvWy_#bdDN8gk2cB#)|NdPmMfzp8_'
        b'd213GXk{f&*}x97s}pw!RzcIHYXyG26;j-I9gt^Y=8aN5d{7_!e^#9MTB%yVd|!Y#mF+>wL9$En4e`=JLY$1f;}D%aK#VTNwiw&u'
        b'dK-3c?rqpA-RLOo)ot#E!F#X3=E-?k-*dg%jZ=kJ==!H+^?NC0Ux16aV_tRn)T<scbXO9-THHS58NcIHK>9(C9e1eC$uAlNOed0Y'
        b';9aV3<W~}3Pgs)nAQ}Ek68?&~b@S6(Q;Dq#L`^cVn<=_}u{w|W1L`_-S_k_7G<+HTH+Ss;GVE*;zFqwE)~B~*{m5nftsu9*U<FaA'
        b'X#SCFd*4}C>aHyv7xR}6pk5uizB<H>i~Hvc2WI(Y<2_PrS_DG^wex$g%3SJl3O*ygyWl-k;4Uw9mY1F|VAMtG469_C3lLu&)JvSK'
        b'b~*88=quS-QrZ)U<@eq2`H5%Fm+-zDcykXFbLjjH)nlb8giWDI^N@<<H0X-ka?nHF?P0b<knF1-W_2kU4#tcO9H2d}O3b;kw4L_Q'
        b'mH6~v#B5xgtWq#CS^Q`K`a9G2M3Q$ix?7&pOMN#R@N9apG-GM0_kmLPgQXV)Wbpk5;)T-_ptJc>VXn3mQ1~Jy6_)Q6Fe&`)$euo%'
        b'DA&3U@gTi|9G|@*Qeg^jd^^Xd(-b~EeuEUG3jOk;(gI~P#;8l}#0rHkZAf7w$S5o_9oy+_yoT;yquTp46EDjTIH*3^ltYffibnY^'
        b'ja4-T)Xm1awy4(l-?xyEsfvg00*={yGO0UCQx!fL0vQ%{wby58n;Z|dMy%B#OjLpPy(n}s2lw!h4q+*DTTxx;V|gGa>%PALeoKN9'
        b'dRj;;81Nf@TC0^XbOwr9Ky(5qeglqh_r>)-<)?7is=v)ZzD?wRCC&#E8t=svXl{l1i!TOMJm#V0RDy-3asS-*sAtn==?YVvFAaQ!'
        b'h6Xu=@7qtT2OQfE#dZb%ZVpLR6XZjPq0{&ox}S?x->*fJmQDHe&a?Sf)z?LoZxXZT&*Z-f$X?Ywg=h+>Ta8T{2mRB*oGDiQ^Zx}H'
        b'RR~f>&vU+hC{Wl$O$x<)T<mu_rv=46SWEeI)3SXjio)3xIBxk(oK4Yq208HawOff^=)ZBdzq>GBH~Du}c!B?&87fw}|6lsK`{qYy'
        b'eaX*57vUT#_B)qw{(k*``jY_p12^+Gua6BOoPR02r4-mNE)syHHIQ@2MP%_Hi!(|5>W3web2z-CdcE_p0)To81AUl>cM>R~D&F2M'
        b'q#SYp`(}m^WjK4+f;`!6c|5SS>zywb-7HS{;piRsf0g}5@y&vKlB&D}wrP`54*a&Vs;XjSd6mZdiG6TAZ$tgS`hLPDfzAe$YV4-|'
        b'sFe-?CmRf-7A9ks!0lYqC)4zK$PhNV$-f^Yu8;T21XmNP->pv}NMcMde}<2(-194^?8bVZVB%r*K02id#y(lXU{PZz2m`ZjExdPC'
        b't<M&Yfh`6_1-`;56NJ5+hH+*-FDCE8yKQ!&OKwwue?^zdMz`CZu+v?MHZ4fdc4gRf;9u93Ys&-wd0hsZ5&RpopM$~6KwH!x1qisF'
        b'D;%vN{Bz!`9nvwI*0KjZ?+nQ%h3mb-^-kgXg^^4N<hB?Bw!FK+=U4Y?iJBM#Rl$Jdt8t#@?`>#%dT=C^xe5_MZROXz0h4W{rWazK'
        b'J~`|3$Re=mMVKs+V!xnX5iAmrp^aBQU7Sh^w<RqSe)__i37tFvs%QMVShG081J-_`M;3ySWC>nNe!6p6MJF+ugiU^3;yqI`$Zl<x'
        b'1ERW8F{G>R+4Zt)$k<EodO5IASCD6?tJf6fMP||?G8mepKoBd!Bas(E+2}Mk6dxN@8Ts|uLHXo|CEgDKqzdQp5+)jc=F~R%0o#;K'
        b'{^JKFtA-|)$gdr&e)US^RG+-B=W4{2prO03O7|yR2^<Q)ns)8rkKU5~E8X6b)<5kpvP$G+(EjRo!j$`;u7=bNDNeh$s;PEP<XGo1'
        b'nRtThtRO}z1Scx6bMs=(ao^1QEZ}HzR~&SPn)rIjxX310D%le@IZ)z#19a&3qhD~C+g9w^LxD=B&$y8|!O4Wkq>-@&aXY@A+*RUr'
        b'fl{qmlU#4(u<%$i^BNrUTItbbW$SP0hhelArYj$sMUGx4g`)vjZ_}zrm95y|dtpomEP67Ov6U1^sw9QYa99?^y>N2=j7?A|u<!8e'
        b'A&^Q^MCCU@`==+Rn*65xxzcp-`*z^+XvpGj+)`2ykUv-KUSGU$C9|^_wXdue4-@1VvlX_jdZr|G$%-u6EXp&BHE(&K@Ma@yeD_m@'
        b'&B_D9!O>8r4hb@zEJ3<MZLn4fV6Ib}s{$5@n3jCB@+$9L{yLHTdVJ+F@Lv(FDtJEYH1yvJNShbnT7lFC?G&QGUr@*DBG-5k-ebeN'
        b'bz)rLauSCIne`<d>r1|ooC+i*Eq@WYoTAY{D1qH|cg)3je5TK`>y0RnP2Re_S3T7#?}I4dTv@Wp*4k(K0bPnk+Q2j-QXS#{>JnyE'
        b'31#!BvP&#YDm4*FC#ZcsXr9I6*Q#_Sm4wGE*Q-1-1@;Q=ey{{kUx7>#{37=QCCvRLuSf@M9#A(jd*ZPC*M-!A40z(9@~R~zOK~+Z'
        b'GIm9+*!F6?K$TPyA7XFmtO#JDA%ICu3E74OU5g+MWozl$43<(*<Jj{1l+{)0wf%ur6$KS*yYsr%!Z_RuRP$#F6urcKYuG(9&l=fo'
        b'Kq>C(kxx=3UJ785(Mgps<&dy#IT-#K{b@qbWK@Ya0_2o8U*XmQD(RVZFz)8TZM66-HzX~Huq9Nck%9KOs^t9vh4YHe|0bvvZ4YuR'
        b'?^?b*H84s<hF84(X!9KGv%5a+EjoI~**)jU@U#7Zz9W_I_u`~j?~t{(Z~E@)+5W}v_a+Vudj{V2SRVK6kN8{~C8~%avL?8KI6F~D'
        b'7bI6H3bpots(D}`EB9Y?9hYSt<FNPDvWYs+_TaAN+qg)FV>xtY1L|KO0mlI8*zb$Uh+%?>fW6+OkWZd3_MR^ubZ&B<FJ=<pcdE`6'
        b'yI3K-m6h{lf+xQ&_MQP{o`Sm9nCi>oVZ0wj8Y{lJ_Ya~VGBE<4UIzR8$>NTa#pFsrBs@^u@z3JUN{spY8n{({Uc6fZ$Y5#AFSB=w'
        b'3F~|^4nXhB#|DaE(8q!MsEiMb^MA&e;WZt@YwW_#avW{O(@Lx|v_M#K-}E~#5^K}`tzSbam)+=@i+vM%MX0aC_3Lo<lZ=_m8518<'
        b'Gnc8ES3Cpx8B<?pkjj^qLi4n#BOd*j=j$j@{&&}u`>*W}b?+<QE$of71%1*d>h3bKcuOiQcl`MA(H9TltyXewTnbK#7D+l@Uc+>+'
        b'=}Stx*DiE~W=Swd(6Pvb4P@vqO9&l{r9Cha>q%QohQ=+yNnuWsCq2mn)gz~avC#<*Yp?W>^D9z_6D;N_@=UDpd_7l`|MOMl=+&yA'
        b'!pQDUP!Ha89#2{nn6`K}7H>v-G34z2gsxV%6<edR&S-c>w++Qy;F!&8I-Xi%7dS!yZ)Yn;cgu`+U5di;vQ=|Wq9)a1*)|BMkC&1N'
        b'Fh2?EguB560j7cs+m%FES!`g?1K5pe!K{z&HpTQ6Zq}cWNyhWh%oC{f`eL=f7Lt%ahV0Vfq@eZSfh4|O#^c4H{R&u!sRobyod_Zw'
        b'QYDPB*w2q=7-6{*_^#3yC+hj4Y83KYz!c1uGez83DqR%BtSR>KKzYSCc_6T6cT3{KW_6^3pcw2t^oE2_|HSnuZ?G#N?l4)!h-oPa'
        b'0`vj(oM$qln2c&!jFV)}4v)v-IU1~<Z)pRhNz47<TL93$UJVUj)4=P%pauF0zX&e_Azgl%w-?W2Wyy+pE}Dor6P9y?8Wu8x5To1D'
        b')C%!cUkp=bVR5gdt&ey8&g2&Qzln*3>D7(DGOK3ORH|Yd(WZvuO-3-8Fnu?X|LqMvj4uCuJ-=}$rGR`etp?lmbP2W_@43qL;<Itt'
        b'obuwH-)@OTmN=)F8lif@hBtkQBZWH?;59+diLhS5I58~j`H6#&P1%sf>CwYWIv*Uc8kZ7_q$j_P`I+m<g07)VE3lIZ;{x(-G9u;$'
        b'oOX)xS3;rp{F#1%=_+VZ8F7P;COMKI1lVPA;sDyHpSN|MU)OVOwqIUMts}+C69HA;L6+Mu-;ZDP%FcK-r^FAp^%JJouo7v0tH?dI'
        b'F6#L7`^wc)rBqZXEsTgF2fbn2`j~g&zMhvkFAtaHWrpS9i}Erf^6-Uunc)Q?ZK4%(3qq<w3xx%O6(M7y6@u*OJX{f(xgt8-Ta>xN'
        b'J9>swE0971+CP@4h-@7hU}RaPP}X2roX2t(*?}|cM4`M8kKiJ{KNavWj1<-{obJZ*r9quunU%G)+6UQze#t^I;-Ff<*dK#8rqYF^'
        b'%UjPh!<U7ir}ZwchOzqJH1KNm5B@iq%bUYI<A2M6CAYx05ti~5-2`7x;Id9UguHR+;`p3xgD!7ary=!(A?1uAjhP2gty7hHLX~nx'
        b'm3A`0N`!sd73?A+cBKYbiSRyKOMJ9iF*?I#hmOKn7PMDZec}xM<_PW{#0P#8Z94^RYF@`^)nY3?*h<re#bPh#i*2wc!Y1vC*cs*s'
        b'+Zk^Uw9!E}J3T$990jzugUGtZ*%jhzd|B5>%Jg-PrlraTp?2iDE*hIzEMNK1#9}$v?I2gJ)jUKkR|M$}?{OW@oX&-s!PKiBRrNa7'
        b'l|l7cRij0K#i#e~0ne`E*ZW@W`J2*@BZD;I8j+=cL}}imVlHAO03X|mNP*TAK7U4cBn3rc1?Xu!l1Vl_)g+7;8%KpH%alnHl8E<`'
        b'!8FUo%j12RMMez=1H}J5AiMIP7P(gd%rd!@0BgS>tE5%4m=y;x%cz@Y#N}q?y;fX3OjvbcVD6n^V1O+#8Bj?i2C9piomN_|ucVAd'
        b'xe-^Wz16h%43`qp{BP(m?o$ra#mMQsH_~aDj>Xey%J9Hrv`J3Kgy~G-(6slR#{d%OX^J+5<@8Xg8L7FchMvEJ1=7|Hz7P7_ABEux'
        b'yfTnG{W0fK36-rgDbnnSodBzMhNcQr3_(etibI)og<FvUR&i=>7ThFUrtoH;Ou|JAaz3U2fjcaSG2l1%gj>>0Ww)gFYN4jav<bf%'
        b'`(lUEw;$wK7K1$i63ZV`fJPik>DBhs-ctAf$d7sKmV9u+E9^9Lp(s^rC&nIP5({tA3jIXPc7HpGUl-BQSiY8UpDuE->KL1HXAyIz'
        b'C_ch2jZcVAi(eUE6ki?xbbM=k_illj_eY}E?QH0!ZBm;WnK3hYaOt$I1grci=Z}q1Dd-ne#!iXBG6kP?oqJZAA0c)h1#MJLGs;>R'
        b'ze9OkxK+9}V(ZGSMO&-4KE1VdYxmZ^t>13F)=({Ls18p}cvcE_dBB%KzmA`9+oe1A<rfK4^4bJdA*o_gkg814RppHds&pyF$fQ(c'
        b'U2CKRl+D+ZUkualqg*3VG0%l*W3hg5N(d>2u{F+fSY<5SBlWLSRs%MD90mn$RN8RyjBme(Y{11wq0R&=TMcE#yHXxOLAPgM^zd#S'
        b'AiV_fc+7clv|X?6#Z#myI{@GzoIRN_PJk6|ngKX<@_5&CHoPs+9uIn{c7&yDvOhN_uy3-x5NWf&Fn^{OSGIDXY6z&>%<DD#B7T0$'
        b't(N9C6)9JW3lyYyXN>LM<z0csWr|_ZDp$|eu!0zXb9oCeTd2|`w9i#m3JWC##(rVYnnGjDyI{}k*`UmBIP_Y95OgIkhL{q;`T6!y'
        b'bUl6YTQDNS!s&)EwXk2PR!kAd!Gm3wb%86)13y^yf~*;?M2HlWA)W}P&tNHZiFD6<DT=6Lw&<4B1(E9b==;>j6Aj=(bULgxi58HS'
        b'B6&_8RhZ=S-{XD+%(KN*rexD7IMLlVVm5|ZX}nF68fF&&)C{o^sfsa4Dq*87Yvf>1=yVudol-{^CPmWm(c%lpwnaGo1;+gDv5~#F'
        b'rB7xf_H6k~O$NR+KWb{f{J;<$L?&y=q5B4gGIqTzJU*Cz5Q}t-{=(V9#6NShzJIkercA=2K9nvRH&us$!?Q%WREV}y%x}x$E1OL;'
        b'u$=O+kd#y|D3SC_$jHXuT9naKUGnZ1Mgqy?ok1s7kR?H5t&ui>>6@c|?hjJNaL{2lW?X>hAArU<!kBWfeZ{O*t`;j}eidKg774Tb'
        b'zHu6_XmyxQhv(^t2A#l8+qHI`J<o2mHw=q+D#`1v5ef6<V@OVA)y;!YbrQdyXHw93rSV)U7`9XzENNY*F4TU;YP>^hl(|MSV~WDG'
        b'#!&y-Uo{xj=Gx0K7YqG9j~UFSZM?RtYiZ*-hqfP&N`1;MvaSqt9mlPEZ-9kh)Ai$axs?dDW=H_BvwNe94jlq3d||MyU>t|5yBbE~'
        b'fv|R;v5tf_UL~zhSp^QsDw~+UC$*jFWS<=uG+t{-jY5^Xq=O%%57^{gRSSbH2Q5>9x4;;r=Zvrf#P|HL{Np#eF51qR19AJsP6ZWd'
        b'i*$76QT8)F`)ttfFM_&WN+YdDWo?ye9q*P=b)eAacdARv>@PG23R87A{XT;By>I5FNQdZ@C%_6@D)qGtcCW@OE~CtT#(vRi6o7G?'
        b'KE**~hj&>Q8?W{UCU-@roXKN<pOaMPxVSPqZzL@Ft%z|PaI+%Qy0Eb#8*WyMR$N3ZcP2OpNaP+Aot@qV{RANSj3Z$qUJ82AFcpLW'
        b's;W<v&A{+$i?DHog*}gj<tGI8<2`*?g9_J;WP*jiIU*G-*Xd7@0}B8pGfbzTf--e^lun_F1pli1Ya%kV@?!Ff(C0|n;_NfYZ$ZN+'
        b'xP1GCrjIxsPORJ!v^6;{9yT7(FLroMIbmJi@1C|XW_5rSfU{ZiD62vhv^f$yshTfw=1@8Bj%j*nm@?v8iL@E)j(|C8KL+DTg5-=a'
        b'xSzAfDc{BVePLOrP$XIYz2`elnea>2k6h{*@hM~ztkG=h(xx(6Tu*|vQ{_zUFyiG)B`1!_Chlu$-_}&+wKP%b>6=c59r%1=Thl4Y'
        b'n61)j6C2rQTlR?zD+`<N!g?<rJ;SCv;bMQ!?kU?n>Dr6;9o`;%A=tBRN6z^jXC(`4OkXcM+_dwJD;>j<3!-shKW;kC4GYF`Fr7Vz'
        b'xTVrvOWq{INoh{^4#3AdPFGG=yy=Q;f}`&m3A4MW9|)_Jo?O|5o8uRvaMJ|%uv&;Bf>bRugoB~n+p)no{GA8|vVJ(j0UGAoZz=x|'
        b'b?+Y6)RircpPVEoucIXh5eRK_jsye6HUyPGwS|b`Q6C{fK&IXyQ65sAI*hH4(z!{nAt1IGt2}C_NfZfGMvYd{%1l6;D#aPJQ`=gd'
        b'VVq*s>BDQSRjcN^_6Z<ur;oXx-@Tvv`zJYPpS{;!kG<AjYd`m(X>05hk2TOKJ7v6YXmZ3U>c09SHxEzkXy0SExSfHv2(Ful)wG=2'
        b'I*q)&{s8zAkkMk-g9d%@Uxq{9*f%1IJX@pONB_{@=jO3%TH5B&lV44=-G|Lt4*(9loaE)P+g{md?>T^A-CxsUdq0dWw=gBmTS7XT'
        b'`%}vQZXmw4yNtIBQ~0)1$hfq<{Gq~?f)-LBITRPKT(M#$=tHHEwRFVO=cf5qDtE8!#H~hBJ{0IL>goZ~{}NnNO|i06ReP0FLrC8G'
        b'BvP`XMy9k?o0Tg;0ak6|YmVY+)2mlaxSvsMHCP38(h2UFH$k`Njxde`F%%n&QEyLPHyh|~RYc4c8Y=FZsPNL*((<dN1g<jOX95K;'
        b'HR)y2B$M;EWt&cxtExU(CBcbGj3iJ=qLVumg9=7TE1_WWqf5_2>rkIh-j5RxU`+L^8M~4sUY$(N?d?&fzB$Olwsw$g;+Gg^Fx)bM'
        b'#y|~}?Lt6Wn!Kf5`$a(A({(<UovNb3dwW7Uxhd&G4@4M*;a%rXfNLTj56`#N=fQzEuTC$W#8ZK;B&qZ=6##;N%Kx_jW}?TdoWE60'
        b'U#v1lSa$_fPP7odED0wPF^1kwZfj(O;mm!2bAJITsk)(!!%8PI%2o1*fI)a2j3nU7s8vZ=gyGh;N@^U$Ao2>VZK9ab!8ZejmM=H3'
        b'Nr^2A!zz0-POu>^>EyN61PoDEyM?{zW#~n4qui`SQUV_F;V2VJwSisn?)zPeZa$#V$+a4zP8lPILL#hG)F~>`&_}qb@Ys0Vuf?Fp'
        b'LX-E(YFY9D;fe!{{_YDv@g!S+04wF={udEhDq~nLD^cYPcv(u7k(Cl`Ji1doYSeC`T6;jh0J!1upqC1(c@)=L&@!go0m+%arKsi#'
        b'ZO;cVXhx+WRn^HL)wKcj)k^2{$p>)ls=zR#<h%$&&K;&z#DF-4-5z#?;m|)!6c;VHF2vd-;~7)g5ik^iV2CdQ;PFc&T*MR9+m$>U'
        b'F!T+&Stt-_{bJ(IL(=MsO^sdhdu(tRBTF#E1_!XA=sLrO;3k6BfT*-0$$u#zwcD-+s&4sD1{nTt3)nUWpr1tNDbM1i?Guw6jVS~='
        b')r0gRR@HTlbHcOhIHuVGX?_-XwpmjX#zDWx0k4W=8|ucZC@hwZ`{S@Z_Z6z3XK`cl55i{(B{}1Cvt_0;IJ8^{t}5fPQ*NwsGW!Jk'
        b'&^~Ck&kO5sk(_K5_#~&p7x9oa$FL3T)%;Q(Z*@d0FTr|@QzMyG1zFH#*?$RFtE!G>PT(g`t<dbck-6z<pyy~{k<iaLud5ZYJnnis'
        b'x^``~I+jPgV`rRN=r?P&y#DJibeg~5tHN;G*#H4%OhxfRTr&Cdfwl=e)vhZkEbYaBnx%2xNl~fADH;`vpS<q@l_tz~K2Y^>=7i0q'
        b'Y#f5DD$sP>djVh)%l~d5_pb%oQ-SF&EbFT4OhGJXdR9^_Cr(4(r*}S|`3CB#pfdvZ9n5a)Cld`7ta3|iY;^h6%q=0ncNVypAV|rX'
        b'+e~k|WG+Em4TM1N#X%-_qG9dbWB=%8xsPO&6a)+%cS81{>8X-60mJ3nCKhgW{x+wyOub*4QMT`BH|GR1$@ABV$UB#>3P>vMf`mz-'
        b'?IPnNbm8^S0nm>pqD`yAzMfj|+EuV~v07!_b)_k(CX({f?04Klf1k*-lD|#tasVV~zz$Lfron-5WD+DrcZToB`#UCCJQ=Fhn0O1V'
        b'tv3VjRCe;@Hv`741y#2Srr&p^Ra{gtutQwj;T!A_Khd$LwqR&~_y*z5_$TTX3PmNa^0(MnodT;->@bE583PU~L{#cHo@b@R5cZpB'
        b'!fGNU2CmhA+o8a&)QVf025Q9(b|2a>YkQU7D2Z|(zv4K)GYFt$K>!K@jNn1B#U7vWR|OF97k5~V#|_0DA*NkBi-Qrrr*&6&xk)04'
        b'F3KYbv>lGZJSG%~R&)&gIbc}J_n5%+6nB{A<$?OXE>kD3;?0sjO|*#tu7k#`6e(E~)zB^jT@2RUS~6Vsr-wZ0ZC#V?CJ)^usIW^r'
        b'J{2|L2l>qr5D5vILLm+n)P}axCV!qZ!#@~kibRJe)=Fyy%@GIr2yqpS8}?!<lVJGf!TYbcX%^H|^2>lTM^=C9@7jWs+JZgWf*A>x'
        b'$Iy6;I=wIyiKo4%>dS8pY?0$mh)^%|Y@olRyhp_ftw>7gv0V?uvL908RkmK1I2kBcV%ACQvL=ptg8x?FJZplN6>`-XIMoADLhJef'
        b'^j?tn1<3@WJgGo}_GT7_R$Z`9D{Be|gTD}L&{ydA^wvL2gg>7A@I+`hXQ0%zu23ldrvN%G&S|JF3m4`}3yO-$!f_kKo9I4RL;TgC'
        b'i**P!H(qPkM1{VSW9Yr&5*65b0@zqodY$Qr5Gz!NqcdXx*E0c#_-zLQm>cx)jli523Zik_Ujl_d7*Iu=3LqR06^8r234r+UiZ`_{'
        b'F?w(UM}vta^TBG-F7DP_CZU}A%5e7CJ?9N>XGn=Xd@iK3>eqI2hrYQxg~%S+e=qaOdYv2;QT!DR*R1#UIzucUp+|3T1X*wSz%UYL'
        b'pgFBxC#&j~<=tS;Xwq^LJw56rqb+|LlMl@$_v`MBNhH2!*z>Ld%|Hv#sOZ^LGRpF|1<XbvLp#5Jt$PyIN@62ph>-ss1GBSh$9%LV'
        b'8>fyL6nH=Ati?4y2-J>eMtq^5iQ#oxh6${bK0}Ys;Oa4Woz<2<>zSQOThH5R4_?b2x)rEjYmcf|dqRV&<XaJL=u}ex=^le8+WuO_'
        b')F~w2+Icy*9ne5KSk|F5SDS&1XcE?^*ag;OtXe!<SPPLuN?3D@<vH}7<OXd#!v7V+@WBbsqA#dFz8csn+_S~d6mJ)`HH9~eEbDZ^'
        b'72nI|53d{AAnH=Iy>g>j0ig$TFV61QWtJBaSL@?F!v1)~Tf49(l;ep9*?Xdf_e?`W`!qntZ0%z%(y<zt(ST2*NOXbaF&*>PpF<vH'
        b'd^pj`=M3N%i7aak%wdXi`Dd@~+(h<S9!E$>*4{~pQgh>kQ`n!HKHZlR-_AvInN6I=(D<wv2r5#-NDc(=(2J=RnVW9JDF_}&M?u@Z'
        b'45(uudkhl{8y4SD#AG&oM3-P_awUi1H8Us5axF5DxMeD;-1rMa7BM*t_vfPZ+l!dV$(i%d_pCnEQw327D(T8&T9lzEw32!-@jrCb'
        b'm-(s5D&vFks}^xqZQ?;I*P_Mn3E+ykdkQVz%tKQjT7yHJAd_92+>9JJD#O4$pF#t}g-}rjs)&@%5Lzrc2D+r;n~jeeysV-o!NI6z'
        b'p@W)8MmMKAsEFnq2kRHj@eb<#h6au!M@|YHIf{+H&0|hGCIwEn{OqkyKXhp1XtZ;QyEn}8DS~*Lv(UQ;R~?bf#fj4aUIo|3+zsS('
        b'rE9+oVD%rlD1(ENIGaOU59`{Rd&x-K=Yghu&EB|u=zMMroh$g3`i)Mm<u($@BDU?D0Cbc<o&;eYP4?|YFL)4n=q?w68~A{w0I|x&'
        b'HCX<dKQjM;E}sw@dV~g-2y~*tB1Af&R`qX#_CGYz=F)HG>(OYu<<E@4Rh^v$&nJS<l390BH0r%6DsV3CctHfGX+mRDlsyzZO=@fk'
        b'@z4_C9q*AaOAga`a&9wuKWFZd`Z(Xtt^dHfi&f`18&_9de-TwS^tXVd<F1YAVBO9ziyH}yu0W?WrbNZ1l6YKBc6`Y-=o*-Hs>62V'
        b'(ENM)iD>#DzvqK|*Xew(E79^^F4A+&h|LK`uR~v>f!{OoI{|c_hoxiw@R0|Q=N$JeezGsWr!U|2763SAc?$vXXsj+gIrV{}O;#7D'
        b'F;&u~^58TsKeV_1>IqRd$KuOpcEB^c?Wo=PRu`ebC%1fYf@3+9KYY^@vW=W`T!f!Dzvqp7*Y5%RB}*p)e@p`gJ$c52qD^i9KSOj3'
        b'!1o=obmot-tHWit<@b2<U9UmeZ!Ew2k+QFhDSLtgG;PlBc_rV~kneSmw=|%FO-#WQSxz++tVxMTGw(aAP@4Cl(PR%I@X%gM!w3|H'
        b'x1aG&FgRHAd+PFCzXebaTb@UtRx_ZIlY*d<ANuu*d^^6H=XMdRnjY||&Ji6+t|xPqE3U2G=iC-z*^BIYe~yA!OUDtzcXDmOyV(f#'
        b'Q~5nB^Ic^?-|sA?LDtiV^$!+pq7myS(tNpxe^zr$eU96A1iVYjl6yE}RBk@FD71@cZ23IozhvioIN%6yJNa_dWWbB;5;F&x-JFX6'
        b'vn&pTNbuggUT`#Mj+<tmV-Niz{N6aaMV~(xC-KZKTCTilPpz36qRt^BQ|&eT#=nYd(Lz%!HG_=IR9|V3tsLzmI2I++B}+y=^j)`3'
        b'&dTqZmG7FB|KvxO#N2yr)iNW$>KhL~=*o<wCFeuRqoX>Sn36wvQjSHP&nyU5s?t^O&cKqymZ>N~sq!h6UxAy~kz`TkGo6y<5%iyC'
        b'O^4K)L-$+a(JMT+B}E0tL=#soNL4A7i6~C6#4xS%>j2tTgdP(U<|Rj+b~^upb%?<#%Hn0r-2kKG(?g#_NQPM+Sil^dF~XyvE5W%b'
        b'va7}+D3M8qxkq{?cZpAq%kLSN?;4ly-PUKhifmG;KFmU*%4Xb%?yZS>*Bl>$>>hSqKf%I7>1Qvy*!l7CG>)M$>5^!P<jmbGR&l)I'
        b'3N5C4&qCxd@`mAQPUl9aERXm{fSE_@Pqm!P^YGm!jQT21QiruFCR&}CQ?V(CUvxJ*y3z7Q-iU6vFzU0sgnl(nifAVb?HbsIng*TD'
        b'r_)17O`Oqko*9n~CHYQkwKYA&@-Z{l(bCDH(_@1lUFY(;S(ZWcc(#T5C=U$EU(ri{pM8Q_Uy~$E+?iLak7F*-2KCSmpO=3!uNA|_'
        b'%p0G|Bm1-1i6`?&k^2b8VnKLV{+yShs-?4suc8T#A#cTJ+)Pd(uT+au?TK&a)g@Wk_`Ng!HS`p(bNdO-Auq`EG6J$yc+!{G<I8jT'
        b'^1LpEW#h0@ad0lP;V`c)jFmGfxMs2&cRPJvBQ)E&j6t-zSTluPtgRgz_vZEN&4WIT*VY(XT5~^gTNce@b{w-%)q^$SKD(V?zgoJ='
        b'e?1_rsTEk-@&+3rTrs<y+f(??ZRS{fvW1+-%(!l676(PlWd^$G#Z&Z)AFf>dNR4FQ8iKh6fxJzMEa~VoGV-JMDxKqgM#QoojGYim'
        b'-bhwc`zM86#j%8&U>zD?8=u-DYIX>)uOm4nUyjUrqaE~jf@fq|o}bIi7?b1CrBL9r-x@hfU;`-kWW@w(ZC(>RHFgQ8HF+q+vMPdO'
        b'$yVp%ZYMTbJ>d#E&B{zYl~+f*aTeAwNq##pJhqP7R0*nJIZl=5ksJlSK^VuX`g#iIRStRodFS>7h^;d>f$N%U%p064E=nq7OEz;<'
        b'@+rycS<-FY0%v#i?N=_p0hkfB;%4f@#7pT{ja-Wu@yjl5qCQBxn0_PoY=zPdK~T+JzH*1zEyTWVA(GqJ&$Fj+r5VJ?c`azm&-H+;'
        b'Qs%6Xk#v1aH@o$(0Yzzl<&)MpUe#5b1XB~d#Rc6$ckILGxF<M+IGB|!eZ2G;c_a>|@jay48&!F3XIew8?Af|Uy#f~Y=A=^5!&fTB'
        b'@vGL_EBRQ}kZx6oKK7ByEKHxpQe~lX#}+Ua>jbwOfz)0ONa;tLA-xx+E1s2{|2m7{Eg1*3cC#S^*=zd<`PL}!?STAYmO`j~pOF>2'
        b'^<rST5X_DIWT0Mhx&tFOrQpE}D>1vIU;SjY_L~5>m8MXJhTz01GUI6F15-Ube;F8_zxqcIR!KjC)iMT_Jr;qo1wq|+j~$FT9ECI7'
        b'{@5jd3&I(C`};Ue|2J`JJrkJA(03$IA9i|e5Ehtb`$`0exE)Y%c&3@oLo#>F!)UGT=>=1Sz{sZ&BZErcw*V<U#=A(Gy_~J<$+!l)'
        b'%sLD0#w$aaw4Vls{b_OrDB9C=&`C@;tg~3wSvWDWK7_doWf8)o^-!Qb{5v$gFhUcTXBr1I$scA|;|JC-#Mr(H%1S-}F#7ArNh3uO'
        b'yaNHNTwo~2fW2ri;yW;)Xb?v5{w$EuJKurP$!YBiw1xAcCk0pG08EIm<X&*r&_qn@o`AiTVbzxme&bId*wCr~Hkyb>3vST!rz36P'
        b'E#UWea4hKzSYt$n!eJZ{$3=i5!*Fy(DJnlA`=Ori<LCPq_<2U~YYW)l`q}uALg1G@3XQ*z!YQ14=NJj)`vdkmG#Yi!y$R;u7qG7d'
        b'n{;n42`Mbu8?dJ$7{T;m+eQk9_5`f);X&YI(@S<k`owRi$#+3ogzM1-K+o9pR^U~<Vib*F`JIp!{e8GY9gu$inABmMOWGm*f$!Ak'
        b'fwTv|ofn;5w={iCZpn^-l?u6-Udyt^Pr8wdG?VGN@0H&Zy1*5>px22FxdP638M8HmSu=MxFj_BjMp>e8!9eidltlglG6F3!W6RW='
        b'rVQV?8+~JP7t_63@CEU9D<8X_bp^^b{FB}ADkr{~x}_heW$r_9-PG4_O5tZmv^h?qjf(C3=7{0D0XN{(HGOPh*!A*o>c8}{Y7zC7'
        b'-g@k|!-<*WHZga|eW8zC{T218e*fw(sL$Zr4PxZ(S8{k={R>ar^8qDRwjDpL_JnSYw?|xG{qXg|>{#{m*sK|DnpKjFdFcAfcHGMs'
        b'TzON>yvnCzUMD%a_m!-zN%>3b?<8n9H--&uz?gf7v7u%OI#omdiUhe;!LzbRzLL3I^XzI_UG-T-(}WZpEgQMMX8iSq*|8~MvDuGU'
        b'j_SeVBG+4b^^I?4qu&0>^{rE|_E5uG%yL-I?1O8yVTO;{Bp;bhud{sUA^0p2-W_@r3-0IgI#;&FqqM%;t$7$)RgTgIOX5&k-8b?T'
        b'nD&c+mo0ERak&C>n{Y$aH=TIN7XkkT=AO50`mMMfuRmswh%KCYy<8Nlj*QKsf^v>st=hjj&eftXwSPv6Yy!*^I#h)P`3sLzF=pa}'
        b'lzKwt^DyvcArD9my_dWw3C5zxyKvQw)^U9`dA;zFdv%btu4;Wv%9ozd)>4e27XX($bFYp^P#pk2XV|87vt7@A8`=~G+JnQ;o(@7Q'
        b'Sv(3&{xky(U`@gN2-c7mbr{oou-qkjiHdKcG0AD(YFbjm(-VTsH{yXipMzO4L=nNmURu9IZ>ijFRwoY8Ej+K~sBsOOKa-`WF%ymV'
        b'as@M<>Lh&6nk|=eps5w&Prd_bojl7YIn2mZ!OJn7xcm~bb$x2Qo9JZ=;2l*m2QBRk!Gc3qSkacEZB_x=F}vHYv}R*PjqnEEh&12H'
        b'yra>dV5}WnpF~a7*B@#U)~{)buTPO*3i?bvnCoG^<SI0CiHDs<OY+zVaXnuk|1|Jv9gs5^_%zCn7wzli2gicXre@*YtX>Wu-aZcW'
        b'7crysmqyn&TEKUuBK4AgvO8G^)1mw5N++W`S*<70-Jgtc?PSUSiB{(1oFKZnK+jk3(!aKw2kB@qppz9MmX#a}#xWMYzMF05f6Lxj'
        b'IC`|_X4F2T(>Ch&S^~MGh}nufvai#Q&mqjZyc~Nit}FFrc5zpSN>{B3JuEMqszl3g*t!mLv0r8>L|oS#_2ta2NSZTV@5D^Ie8o#b'
        b'2A`D~-o^|^36k#*#mMo{J6&Q8<zZGja((4RmH}*4gw-_BYKpu{PXq%)MqH__zQaG&8;x$k=oB=w<i%JMYl9Fd6V$TgI&3Hxv$G^!'
        b'w~*$RMjV3<!fl$k;(+YD5i6OCU1TA7(Y?{dM|~B0i`*7fPH-D1qOsRmj?Q(r{723`+cc84Fy~(X<8ZPd%1Wz6mW0`oe}dERQPx)X'
        b'7ec(qw0R-3j0MFQXa<31HO!R{*u`mfnc4HqK(^SOj+vcbxzkzJbhg=(o@Rf>n$Afxe`QVQrrFc2>4YYo*I>@;b*^@&<1<#8`+YT2'
        b'xxG#`JnV7iLUZ{Voo=_5tVgY=^%K<JcSO%wk3yik*~2%v{G@CYqq6z0>>ra2hX;mkR5tQQfu86wvWc>qqOa0Xz!Q>xrFN5>mLl;e'
        b'P7uiL&|({ekkZYoWr3|OQ6teDV?=|2Y=DXI5kL%!Cke#EtT~{26(jQL%N{;)f|12aMi$qz$I2&|#?U}UGB+_;P12eCVOa$?hygAq'
        b'IFrLTtwH(xPsrs_kjv1GF>)CS$|Zqh<kB=oE=_m}YbK{bw?yMKr>^M=)n)idAt`B0#vzC~RJsOV8d}yeG5J7P6YWt+*Dzm9POPJJ'
        b'4Q(>94^PWXN_6+?x>!XWCpZ=>0$k3r9x>;X)=gW=s&tx3u4$LKcyY)It*n2ap_)hXh;WSL`ELf~4+7!In%)q@O^%zMR=PIb9lESp'
        b'-1;EaBzBmll93Km@>O~&bd-WCEt|Snkmobr9l@zy-3g*K4tpMiIW29UtThsAm12^~x2Eu*u}20s;*>@nB?a&u;B<3ZCCD%qAMvSK'
        b'bg!;>uUY3dTM8Iiel#r0K}K%XV`TYlS(SV?A}hp(tWYnFHEfU%bcmfE*+8>6ZG+t0EZcoTKCn(~u9rEFJ=2?xIelOCrnB7XZ0E7`'
        b'2G29@bWQ`3C)WXT^Q4=bo*8&T>`3RE8@_U+3#{oPb5l^rBqQW;AmrY3+?qaKlYZZB^O9cY6?Zz}NEd3HPmjoY1(J1-j#>LOSNN$g'
        b'nq+kFJagQnw>N~Qr_CT^RjfHA2wj>zdaY7${}ZGw)r}taI&4=tK(WQ7yJugJf3)a3?+bNf*R$5Ez$w`==3ZqqpRzD~crVQG`lbAl'
        b'_maPdxt%h(@8<A(f>3_!X35~_`Z-y{HLJ^9b+smPBI#&Ug}IL_sh(_e2TRr=o3p;v5YF7&;9T6OO58Imhf2%YebBvoZ#uI(?}}Y)'
        b'ZudEz*W7(d?>kEKn=GtDyt_jNMV}ODp<!6vSk=`=b+>C;j*}_2+kDOGaXYuA55|i-+*go1eU^E11|JfeYu$&uR~{0}nh`+r3+VvU'
        b'dQ92Sa1CIZ?JUP}WnG84S=`V8?Zk{~Snq#75bO^ZvKA4>|Iih$bFWyj(!9i1Y)r2!Eq*FpTDmlG4zV9x3MY2m3Tk97*pCwm%#x>b'
        b'y_;QEtz0atIaF-P)w%RKbG5nV&@UxNxsYAuH1D@^ucTutXPVNQZZ)!$8NHIXurAg)-U;ZHTh-wtkL13}&6IP4S0wdPtQGIeiucPp'
        b'@#fst>ETVe()`rY=LJkq+|5B_NHdTSjni~ZEX%&^ilt@h2cd5kSf(?wCeWHFzBUwMS7H$czy3=Bu$RV%bQR^6cwJf7S;^)*d*XDR'
        b'T+8-(!To)ycf1s)drM}qWI@7Gu)wv{e$~PKR@^^;ZoF|ls3ZHG+ZVTsi#p65y_PUtdpc+x-?Af%8NYXlb-hl~>%?kvEiRN~&y~b*'
        b'o5aikWhX=DHTd?W?L?O?IPcvz=;7~CW~W4;!^%3w9ACCanmv5&LpgJtngZMNYSw6q>#O;aw+PEu^H1KH%K+B_<gEyD!#&7N{5?_G'
        b'yPHFNV>f^A;bs@Ic7H3SCTn5DNXpiXVA}k7yYFq;cbDUxd^rbm*2xUQe|Dvx;C14)xvf;VJUYCPY7$HH7gF}zh74azk|(i=dY-?C'
        b'-`0-%cLzENV8r5Vh7sDjV7&SybMHAm;umS0BE3@>oXrjmtIrW-^k-x<W1S!uE#e_Kw$uNP<@U~(nPh0AfP!l{&m;T0@jjO&3uQoi'
        b'GCNt8*;&j;Yn(XF)y<8@-*Lt58AAJ9e!Xvg|7FHeLvQt$JzV+CaFU(EP2n*L>*0EP6!O$C4-fuZQ^LqB(&XWF^H1QlMyoL-?$@n1'
        b'!XcRSaG4}a+{V_g!#&(qo}@IdfUL?+Jf04pI3?G^sh0WP9;F8-C(5sdXZ3UwSJsJh?9ME)W%K+TJ9D+<ihGwzX7Q^&SuuPGB!Ei`'
        b'^WfcVd0H5WuB)P5cx(n*F+(oPW*rwp7{iS1Gn2$4KC2O%%a(jOzTTQ;GGw4N`RQ2t^Yb$|an+$(E{3H)2hW6>X66{uSHlZSt?Fix'
        b'QLXF4HIpKFACK2eAR0gByC+F3l?bk86Jhw6MZ>4_OyaLlqMO1(_Q*=?;Tk7qlVKyv%mtWr5;<2`@9C;$0{f~P&a7?L3B;;$LDwwk'
        b'g^E$xu6MUetw%Cyq<m)M_x#}T8Si>0h1S2*iH^#!7*HC$I20Yqm59*`h<mlqV`?9HC{bb_79cY8pW#fO54=d9&xpSDi+l09ega{h'
        b'JxQm#mRy2sAH#CFS-K3FIb%}c1kD2CLO5SPDda*pt`%eDdnE*i<QL+#xaDA`IU^)3?OJ`Fds4XnJ`C%sMkinbSp-%pRNC>KU8ZCI'
        b'AR~*jtJBg}_Ajv>yKK&`u3xecCx!m$;9E@~=5W$z8DLK&0jq(llb4LonvmAv%X+syLo+D^J?-tPcJ|3mF`Fz0IhbhzQ7R;}@aPXR'
        b')w3;<`I&`}r*F$D&Iloir4!0$0nUK2X)*Tp5>cs;tD!MN4CY=O-u3Q6T=LWn&5?{uDd?buV0bEQf7cd<0TNmnl=6!)tbCS)xSqw<'
        b'>B5#mR9&3mtJ%!5FQ}cQ6<}E5wyx@PoD)PRTHJpj>b^1fSKYGV;1xMDd>6vrx4j)?EV{dI5~p8H;{N-w`bxX0UyY9S!Yt?K)u6U!'
        b'gSKWFglA}L%)u#^bMS(zXts3|Az6JJq~><AN|uCMLADpiLnCRt$Vm9TdCW?QZg$DX0r)mW_^q#hnm5||T8qPj`}q3LQ?Jb3(?8FH'
        b'4{Z%cXB=UcKh6ubg0Du#<4Ms${9x!oTBRqvrbvyRcTjUsf6zqMyL+Fs%*aHOB8TV2S!*5eSL?RCIj`1>etJjx?mY+RfhF1!KJpHM'
        b'6T&N$!Hbqy+UDK!Bfk61HRhY>$dx(bKD67vFJmA>+=+XSuC#2M$LR0YD8N#f67^0;JKcM<+#<;wGk>>uF4+2#(Y>{<>vJu2^X`3j'
        b'U7c&G8T<bET#I$=`{lWo{~Yr^bSI!T)lVSASo*qoD%13AHyM^~QkjxfCL~8T)*i~3<8~VQVE9vcLQk;CCrbVq@X#kX<ocn@0gsAI'
        b'@H#`~mjl_Rq2NAABNi0vkTx7xFVoAYX>&cex}tvqxa?V=+aJVdkXl8IJxn_R4Xmjggkb_Fy=0!dw=i3!GDTVzBOHgW20W~8R;wnQ'
        b'tWUvH=#<bDO^QCn1Xc!#Ye0+6D?gQTUS$eZfy#&=kSQ10Pv5wu;MA+KIK(FbwBlEODbUWDA~f{f9r}!cM;<Ae8J@xoo+13tfMq(W'
        b'YfsiZ`Lp3c+o56-GUg4f3<vrcpLjW29n-&nWZOCrx)LIJakyH$m96IJB?K9l!fMzY@@a}T48y=7LC)b7o@!S>a`}$!ci>a3=Bp#t'
        b'+iO__YX2lJ_mO!sd6LC<n|5^Bbnh-k-Q}PFbPXpOu%?)fRn8=zv)$JoV`#bKKOfNPI9ppg1v3SU1jH{efTm`xw->T&S?UP{3o&md'
        b'S5keqS3-d2cQMvO)YRj)MC_BjxIY%F+-_b4uQ6Dc_5;K24qv<YN~icthh6Oa8@J<})HCpFDz(G8>Njo6lDd(>U?al&<B3o(bJ}C#'
        b'cFLkfJa$V6@9X~wE{NA@1|P$1ATCnCZ46;<xr=6|J`<kp>(av8CG-aT(d_!qw4@M~fgq2h;6xGNExx2(W2pPwyvlcpSQGmhTlx87'
        b'4{>6AH}?`{*@AokPwYkNdG;V+2~=FZe2K70u+`eOWX=bM_xC0!f4f-shHS;#GD{uG?2g5|h!q{awQsh^9wcrHLC|=~fxynS#N+62'
        b'ruXMQ&rUvs|2j`Qu<F#n`__xV>Jwbx^LPlVfYY{Vm?vg!{)!~uinYEqF@^*G)Y_3}TgU?ba)H0$wJcI78M=Em^#qrE9pZ?$5Mk2I'
        b'^{LVhWsC1rEcbjY?v4dE>25B*{CwM+^w(_<qV@jGi53$>4be@k?Pv$IhB^aHiHFblBe3@$ksw5x6VV(YgGy84g{T<tK~LO=O5UU_'
        b'3sBh`lqa?+@k)>r&);{e!(EE4X!em&{Ra`9&55lZ0C_gPD`sudihuep#jMEp8ODEQD?qWlgqXutg1t5nRbK|LxMBAH9^iMgmkR-#'
        b'{rtK36rra`-?pqHU#ASyy_9(N$i|%PhRxoF%@hO|gDv8Y=D`$kYV%;Tn4HkKIVN#dHW{g$=2a$B=4#)dT3nYjSPehujFM?SlCP|-'
        b'p2@#bEmo?{ma4gsYECi_#dC%dIF>bYtqM$%#kETcnnX=R7RUZ<|0O>k!$2=XIfg@bwIqhsY{&gLR(PRcI|0_mY7=54$4_8ncufpv'
        b'p%tF&7iwZyiv$a;H8J=3OTbybmTmPf#%irL6P9(|Vw{`y%S7`!@5bV}b?eOQDV^Qd$@f7kFZB6d5W^cho7edon!M)ui7ib)W?Hk)'
        b'mn{aD6bx{h-Is;K=d93Lyy0bE7Tp}`-0o|qXY8xlE|4}ihgy#v1uyBe9TPDxGivdy&>3%JwhE+RpfyLCkLxfI^D-klG>eXYCbRX4'
        b'!b<RaD+^81{0q<ETF`s0=IF(Rrfj-Um8Fs94=xceR8=IY*#(nu;t@=l?^~#nPL18hNzrH@!qj?_BSq)X>a#0tld;qL1cj9%2An8='
        b'iyTAXN*0<5Rhpv_kgUq44V!sc8d1iU3@lrtjljr#*_tf9sqHCI-a>sv2K4l4Am;Zr4rDdF{4Fsr6ziDVddTp`mt%5|XX*01x&q4l'
        b'f^V=;T$hgy7tQzOi*<QE5=5h0QoV@KxR&JrCRrMEkx-Iq5|*Npj|;}!SvKv~!0=w*O}x`ju%N#t1rR$nb7hK<Mn@Qk608OqteJWD'
        b'^jcPM=h_@Rjx$9-fNKRoU<$`iV$>IN>|!!XW)Go17$gO<mTJYGW^NlD8poj*hb2~N>Fro@1ZhL&51_|!D97yKeWBo9k@5l#4(90`'
        b'>xmv_gU#20F7aHn5bGT@RS7tqJ!8(A)OfM5s#lf~0zM$PMf8!(ICk7Dhz}Nklb72wXQ5l~H0$iLLa}uLv2Z~ltDW6GYwH_87XUhj'
        b'0M%axPyoUnLWauhGROwLl8k{C>;pacjJ<7pV`sc$`2)(|&QgckSqDLHvcxH&NK!a-2+(9iN!fTxs3#QVRzPm=aBg}uH@#&EmL1Bt'
        b'Pr>}5DYS=<{te`hUT@hkoL@DXUxo71!}%j1Kb@lTXh?uBC*QHO4CmL6=GQar#?Qju$q+HEu1Oz#tU(!O_zlOEk<~Ci(V60n{y;g6'
        b'N}J^yoC;zeoP~ap#L3OEs<vgR&CYgj!{dq0HcHvy8%z~<Y=fWF4s`5MvrpxWZm8a*R$Z7dp8R8U|H((PqW`LDdy0@@Cs)lO$4B?='
        b'c_=IT?A5mA+UXc-!`Yfrj;=|6QzOdG)~7kcHjoA(XJDN-ZC9fC1<L911<$DQ1b;S+Z+n?eZ5{vw<|72sa(si^#W@|2scsm74dWZ?'
        b'H)UyF<;R8za*O7mc00R?)AHs)RhMdqbiMWg411Liwg41Pm7*!#wjfJ?Nh6(_qE|MAZ4eq#IJ-A_l`kbCwW;+DqRY(&Ytc`$cmvtE'
        b'Nq%eHZZIs5CpI)v$`s$=CS*8~_4GBP_4G4IbLu8#wM?zaQpHXn;d9HYO@hq07i}1psj!X2YVt*V=Bn4Tf%4FqxGz>*O#8AXm9qzF'
        b'aRu#LB2Lr#&~K^FS1Pv8sxVRUb3j9j=&U3KF3O0{C|s~Zk*Sk~8A3VK`<c4e5@j!Vfm;ntzCm;m8QNotj`gY8EOWFiYuPM|^ESMc'
        b'D4R@~X&<^kTme6Iw2u}~Ze~d{EZ&@r6Xs<9rtXERt2GC4?E!2~d4Z>}rzg|vT7Js)tMhHk+;1IvwoYSi2%93hz0{|0%QmME#)(_#'
        b'K}Yas%DBd+2QMpp4tK-X>4UF{Z#56zgdfBc+V|=>*(;kG;$-m|QoH{Vu>YI$iHFf*(s`WS3a=TEms1T6-?sshjZLv<6uTW>*%ye_'
        b'gO_}RzY||>9=rrUL9o89GFc0PE6ebS>^2Ah_Pm@qr_k+M-s}3+skUY2!LS;6lf$*#@FItL@rRk@aQ&)gbF8&(S=|dVKxY@?lN0#l'
        b'7RSfKPY2?YOyRS-mdlzpLA#-jKOsNNmc>|GyV=FG*?9N~Q!FMaomjrW-L|Zv<5+e1L^8r$KdWs^WcepuUw=?DaKX2`)K}(~E$4qi'
        b'<3uh70lC$P^%_}2PPUc8j)|A^C6`0}Uk1uoffvo>#obQK>0C)henPWI!9`v}!^(yVndD)tp(12ULWtR~jEzQ7?Z7KONi4SeRiB65'
        b'Lbr4@CAG6V+0Cru;-UQkdr}kY7;2P~h;bJb{0n^E1`?Vfgy&7asmo|-I^E0_y|LRI=5Q@D6bdb~Gk1f^y@L7+=SY9i9{d3&wn=eN'
        b'VRze89r@-LygJBPLpkj}P|3PFMmbTZn-5%Crfb?{3&(WkFpz}7!?8S)srzH1xz+1zrFI|k4Zbcu)G>G{_~Ul{>cD1&w{6)W2IwCV'
        b'(A@yEOKe_mhTq+G^9b1GI?txIc24tezzcTP`f7huD&Z7<4dm!2^X1#wI@+AO<O$7D4)kbCtBdl|o=(*1sp5R!K#5pq@Ij9j>_?x='
        b'U$}Vq?5b?z!e1}7tl2mc#mXNJcxn86Psphr<y9wNc|_KUUlM=Fx=EElj}=_smy$bD$`bPgvxc(1$X?MOQ4$~UP8u!Ck@d<t*}<}{'
        b'a?Wrp+QqJa6ui~|vqQ`xePZ-1nNalD=D=-JF}36HyIDyjJNe}(n*d9Fvr7b?QWhG?zYk^V<`_hQCz9-rE_LZY2GRMkC{^tM&`+TO'
        b'0QA<SXP(*2vx9lYnCJ7%^BpwP)^$~~o*DPPiQc?)2=nQB@a56rZ&!n_sm!-8(2I%=t$)`$i5||t%=~tpV!kuez7Se|sdh6*xO(a7'
        b'h+5{Rndugm$rw{<l%L?9ei?fG^=Rn}c)?aT-<nILuu{@VeoYulv<_k@RW9$m)2wnj2mfwXo-{|_hsOVFsoLE0M(HVI)Kz2jP!)DT'
        b'$YG$==P6huTcsIY@4?a=Ck3mrbmuTT5l(LcmtlRJu<Dk7q{28>9I9{vOH@to3eZf2G*hAMq?!El2@X`r{Z^H&&!8$19B%!BZ&k^h'
        b'm9>e7R+ONDF!!A;eVBDpc!%A(I9!W{B*16bNX}}ohk(B@GA1#6z9)RDDHlO$atcX;kJNkzWoFHSlwkhg!Y?$}u<6cl*?V;jZMow>'
        b'!$#vQ*EGTGOnnx?EcfE@2F5?RR|ets>Yb5=EvU^s!%P^*r#g#dhL<^Rr_ORlgW{}`RKqRogz%&z$K}X*@;OT+3J9}>*-_c?*{Rt%'
        b'*+tnE*&W%3viq{nWM9s{rKt$fRERYdp_+;bnw;qDmR@-(c|Ws+peAg1eko2I8-8Dcra&cJ&ffD(23bRJkRK-*+IttR#dl)b85lN&'
        b'aNwBKcBtJg#Fq0{bc8^xkZ`)JS?EAluRLT$&P~GpvStpvKV)5Yb@B_c8TjN#TpNece9YwhTQME-q^&FzCnjSKJ}a7QJ%*p0H>*GD'
        b'<exRV?q1!L^9LzX6vv8wZHlPsIytfT_yGC4xBn2<d;E`YKhEtvejI$W-s7*m{rI%r<Lw1IAKCH{-b77KxnBlxn5f}Eb^R|cvbu@4'
        b'A0980Tf2Gj3Bg#rn*em6Q~PJ2R5Y$hoIuA3ri|;~M?k<+A0?9&Z(Uh05~;z-Wn+e~u9K~{GXcXh*U1-b9}J%t5nPG{-1_X^xTR%$'
        b'4l{~{)|SdY9h1(#m)?3gFuKOcN`=Hx3lkOGCaRFHo3^Q$rTsf5MN9g~aPvZRreXbC`ePrFQM&eOr*5S|epk|!PI9H&KI2y1JjY!q'
        b'MtwpjyJupKRftJb>keNPVO`>Zcf^PK_e{v?d-K+tUJ-Usyhl9pEP8YI?v?x3<HTE7&$yhyH^qkzcZr-LjBL>!#=Opo0}+WekB*!3'
        b'&Vh&+ue1C>Q@sBWTC;PY3Ac5@!&-RI?uUn8ABf<iaXZpZ@UR5FpNrP<2w7I=vYJ<f32fy#*+Z$sP7I6Yo6pJo?U?o0AI;{KGuA?f'
        b'Uy~Z^`XU>xtgW;2oqQ~FIqv@mD_D*b=P=?tz<~tqIZXREELI>u?pw`5zP1??y|BL=*FKE7{ywJcfK@DYC}N^tc*5NtQ)g?F^Aurz'
        b'W-0z;IXgiU7o*@5#uU+X?`;K6hR5-z2&!&sZCGIpQ}DU`Dyu9%WPNLUOtckB(_BRu8e}h^*$LKrWp8-!u251wMbOSa7y;#<{eHC^'
        b'MHn=~e^F=2aGgs5rJrAl8!YAj#rMk)iZCWv_!p(74c9gAzeV5dQTiUk>@ih!&)J>!ko8>$W1{O0#B=PZU`;$H!ERlG+c};XFq6k_'
        b'c=%lrP*a@^m6X!pAliAQ{IFi9nG|*MKFqyjw46$ZhJVrcL9U%8`dx#4fmX!ii5Sk)oX+GrHj=9;UG(|jiy(7S*v_}J2JH)KSws}{'
        b')rcT3Frw~>-s8ZCx8sLtnH)dN2S6#v2jGH8I}SU4YycWHva5rC5MTc1mCwa>pEH`ZwaI#Hpytp;EtoQRg%@a<HK`E9+r9~S#AH`Z'
        b'6t0aA*eN|5o2($}r;!3e8bHUP>zb;YS+-aVx$^~uTt$p1f1pWxy`;o7Gn=`^ypZeUV$ac6=#cgLg)s#QAYh1mCnvBjG0bk+GRp3D'
        b'!NExF#D60%iD6HCJKu+6@*%PXh}aEybbZ3ys+SU81cym#SFmbmT>EaIFtLfM<$|>th!dyq<74l?LWai*aNFd7?co3^hev-*z?Krg'
        b'$P)BS1#H>?$%RMa!GJb5Ku&{4ZFIo)ivT$rm5U5$O9Rs>f;Mh<Q`=R>9U7xsZ`^7!zFKMgoxF|b5xR|gE!&V(t<(;;aTgsysCq(H'
        b'nI2YTed>TBb3~R?S<EqNJK6>9+5MNT)ONDB>Si3@Vf?+eMTDuS9dq!w1^S*4mFr{6gXtR|NGI{sX;s%$#tpRbCEEBRZQP<UX3)k)'
        b'+Sq0_b~uc$tBg+CxSuv2ppBihaSv^LgEs!2Hom51K|SpbqgzF}5nGaIHde2pdp|PJ0S)C&o8*&(a`lwc)Dx1;)le_Rg~w-Tj4x@Z'
        b'7xkxcDLlS-VV%%QIoI2*MyHmC^}1smJt1BojN0CJyyR7WeH2k7(z~t|<?4-26ZLypso4ZIv$6hAf0hVnAO-Y$ILWEHq0#82i)rdL'
        b't8tsdxO1++VRSL-j8z)jNsftXm)cAOL>TQRqvy$vlfTa*n-a1UUT3;2lW}J+<uUaSmL0;0$M}P#;)><vgp<GkjiHx#?s%5l_=aUR'
        b'V!GS72NGLfghbp#?Qt7BC6Zf`%QsCzOk%rf+K$=wVW#)+N<wdFyph23YcNux-HSo}WK$)9ncf~K>%xhLM8GyuC|&w09|iKB%C`ru'
        b'bcj3JAcwTn`u0H0!A}yhY9^v7^#op98}5$~RZ@+jj#VA}0dx{E8bhjdXRUqal>5nEckvq5)%RGRaih-lz17W@Hv~LFld;`x-07xX'
        b'(?%ovXcAYH*dnmX_i*pzsOZ~Iyb^6MOPDJ4_Zk}=Wl@a^Zsp`i;MM^JCn3vP7F8*4vdUWqO2u`nD&M|s=T($gjXP@zG&P0=^P5KV'
        b'YfWWQCV5k(yk%{v$$z_?0A@O<oo?f6r)w`ZG!%m{NUip1#FT^sm0G=RYXAx3Sr7(D;(&xlLWylQ4QfbM0gG%l9UCZvc>5Efn`(ck'
        b'f)qkT)bTpl62u^n6*0(rY~TPeD7!HN_tyj&WE&6;Gl<79$VU7ye|{UV3!f*v)NAM%kYV0T#H{b(y^5&lJ5TJ4t}UDLi1hR+W23t~'
        b'sx6LdRUlg5j^iX`JIbT15Ir-zX#qQZ+s>~j0meYPKv@ZsA`*3yD6iI3j`#w6tV4XU6IIuX%NGEtUgK-fB>hDJ3_DM48~l~{a_N;)'
        b'abGEXGVw6!D&UHV@<5he|G?W_ADO6~+Jb<|Y1Te~RYId7&QqR2zqn!<6zcucK*h3Ns{K5a>+dzTKTn=FdLZ%bt`8d@z-`%q1RR29'
        b'TdhzOONMD53y?Nq9OARdSzal?${K~zW(O#Q8w1swLqKc=l0l8sxeUHpK}w*O?O^<(2`l9)2KU+M@+Slm2nW11%Rs}laREKmczAn('
        b'`@R8M?CuF+wv-X5ouCWP-G!&zb3P*vrC&YEI&&5T(TQiX`u>E@;|tJ2sO>fFgJ6$dlP)gUCIkQ)01)Gk#H>9b^apq)9Tk1!iOlHg'
        b'0>yOc3sz&J#uSw~iJ)nQ$EzlB5@xAPQ8cwxMg49dUz{4W)?h!17RGU9vXvkerUVyCfB?T;fXNNG0?w*4EP9riK7*qWMo;481e5VK'
        b'm2n$wY+a7e#24X21`jBX=IR)l^_0s*H5LrvHWhYwUzvM6AP)8|K30tvhWf!Qy9)t_x^y5NDDGxwv#x%~`b==<!@lDX=o$iQVPTYp'
        b'dX4D87}95zZ4&_mFlF&_zZ4s$T}4M#z3^O;E-57X#`@nxzfcA&umKAyO;M}l!vrPEISJMGI8e%P;0D41>aSRuLM)W{+pr%lF`8Zb'
        b'JCGNUm01!i`S^h{w`hbS+cIpF9EJ=eP64qTWiA`SwU1zjmz253jbv9jFrwlo=+_2REtswN`?P~E@-4X+L|2axtv5v#{E*y(RNq$P'
        b'!!(<dCi$0QOo<<sJ0OZsKx8xy;ow{yUN@Eu9JBp|7>7~<Dj}vBZNET>a8!tq|6kCdRHF9#Q*;0vpmz#(cx4cOMg!G2ppSv_feIc%'
        b'ay!e&jbz9;^VhyV0sd2<8KOq`Z==rxWSC_IKY>3&;iu47<H}zqYK*UKkz@X+1xjTx8A@`LnoT-gF%XiL?@KtXIfI)r^u#%cf=m>s'
        b'USo3Ue;od}z#RtY0-EuPENH(PV~5`Ox_=I)cNc;Li-u(el%HmOMw~g_=VzkH2Lk8-SicDRFrax&LAz*#WBybC4@95Fp-YftaDwm|'
        b'cG&Tz(4Y_GpNcu$g^<5x82;5Wtj~mJ&h+&m=-I5+h=4+<j-rhnD&y<6IEJymDcBY^V%P3LvQZdtiT;q$@^#N8r7>E*IC@=yB7-q>'
        b'CR0>d%!tm$d`ruNcJ4+~s2vAL0FS0RRMhLkRxc&oCPe<s50+;N-{V=O@wN05kC~{~^;8E{JUg*Mo2CspfuCb{a=ST}r_nISr*)(6'
        b'%h3CdsE8iNV<$I0=B7Hl)a#aVlz2J^M{8Vqsg6_B>z!oxI7_jXIgNm?9Y5Th65a*lx-mzqqC9gd!DCEzbJMf5$h)On^sfJeXo@6A'
        b'wchA58C$`J^IrmZ)TGB9)a#A75V#KZnE{bFL#sg`R7Q8En`=qYT8(Z;5JYnbnMC3$<N&(v8Sf9dpr{^t*WY9-L*|4|Zp=lV?|b+R'
        b'aNk_?ES=uDnm+p4lj~%&t7#`LE0tNPZJJrRCII1FT;rY(-k$du%W`Kn<NUb|XE@+l&tZcWpb6%M1mWdlG_@@je@sJdBPUD|rcJ7b'
        b'&Zpi>zkP6#P`032CtLYxFLH8P{YW-eS3{k}jc9Z;Gl34u?J%|y9E>zUDs9{bJ~cc56)M2bg~=w#Xyb00dR;|zoW@zyU!k7Y6W)`>'
        b'DD_4!c&`YucTQO5M4Zrp|D4y?)5-3}OIGuG6px+!dbZ`A#{uyk`C}*Lk4+JxL&F(L`cug;jd8P;^5~t$^h>h~BJlK!v-Q+AKu7dK'
        b'Pt;>4FU>~lj;zKmhw-505CSq&<cybDJ`XaY&GOl7=EBW$qD~wwCf<#*oTu6x)WOS3z`2tyG-X4G(xo@<n<AVkTF#H<NB3|ZJIQ`b'
        b'1YQLsAGDmC%|tO>P{h!2qv!U_lP8!;Egzr{7oeftn0fM8FzL@I$spv=R2$Efsy8;MIQPxqqLFS5u)je>)5Zo9w06noDnCo_Oac2@'
        b'umx9fgenb2AU<m}n3M+IPT>}n&fw6-eX{Ak)75uX)IJobB>7avHew1krvypyv4V;GIr-$n1&u6ehRK~)oNKnab$TQ2aOatG%?riQ'
        b'C|YtCvhHwBu+QQ0zjL8s%z37uQ37q5HxvT+SSh!e_CfqaL<D6#r!;3_S!1jTd@TRKSzAxf%#*&ENK%%qvx8@UO477G5Q&D`oRi;k'
        b'aOTN_!Ot5RaoqxnL7Al*4N$H@WA-!HP)&jAQ~y5#bACfpo0A)96}4^hq>!q2lWCELYRh!v+9xr8KJ;=P{abhSMvtF`%~_n>h-=fq'
        b'n0iDi{jR_13?ap7D^<qLb0lS(Ip1WYrL6>YHGP0<w8;tkPFG_pCrg&((>SMqg)w~y$!gM(>^9Qw<oGy?X?CS^u^)|7&g7V9dBK{e'
        b'X((NWZ!k}slYb>&tXtp{ne=Zd^;#@>@`p%?d+%zFDpl?jy*n8MlA2mngn~2;P)2KJLHszEU7)(c^c@;^vbQHB=b<?hAEH-<3ufT7'
        b'HYMjFx|gjwqLgZY2edmgo>Eb5vKZj=0WfUFZ5Jj%km=$r5kf;YQM)Sg^~P=Bxzeu(WD1COF{MhTGVUhXi`Y}xgc`}k1>$Z{a?+Ay'
        b'J3_-H3kW^6%j7IAQl&y{x(z&W)E^vy@P3zr+9p+}HmjVa4$w@aM;nG|oMli6GGE4R8l$Je#2dQbHXeYssi<A>QQ2&EFkdc&%4JJ^'
        b'CO->Yd@X8=dS@w=K@tJtp*}JKszQM)baC4;-NF!(ogALNh<zbc2KICE_E;;`nMV6Gd{+HBsa=|HHFgrfvLrvU_0E8U>ePTc|MGhf'
        b'kfzQC`&FD_ty{;y+ijw}U=8~v+C~oWf22bt3GF6MutP1lfNK-Mk1KGKBYmm@2iM~V`nqfubKOJxU4_sz>OX+{E*j&$f8T$f_HX;|'
        b'!8Y*Y?z;k4QNK^Ym5(Q;g!=bmjEj(Y0k_Gpol^_k!Vz+`>qdzIm*5QJ3<>?~FzoxdZ~H#(9^AGCyNCV{`9H(>1NI8MXdz)oxRhPM'
        b'2_^Vu1&nVt%vwa)kMdUj^8Xp$s`Qw@7*Wy)Tz%x<Z6vKVK|=fwd@shcMgH&7p~3tQkD||Dz@R_kFEXAYY8C_&qaq&}(0^`J4pu<F'
        b'yugFx09D7wAvpwHl7EdqH;DhLNnDjP=6m>inKtr^f2)l{MCy<E#>7OSr800%tidSsB2G-j4*#W$iN6`#P(X(QaJRb<D(V;!%}1=y'
        b'L}xzgdncPYA$e%|-7#V4_v6s$AC5y)@5P~`y6`h1QKAhE#r<?FO1wG}i^?V2Ar=*mL}mV`{zWLNT{awwqSm=`Yz!BQX_x+Z4A;8o'
        b't||)i{}THji$#^nYyR?|jNw8t+b>6BQR2IF;Fvb~$LWyg-i25cf<Wwhu^iCxJu;I2{a6lsDgX4J5sTWUFyjH_y+9On>__9!lG%5^'
        b'6Nie%#G&6ue%ik+gP#|Nl3Y{JO(+ck-6C=AOdO4CjkR~`AF+2xB4~S7keFe6H>=>DAi&-Q<I5l|W%uj_3e|qX-l=gwpr|k<XfK!o'
        b'KSm26XgY(>KtooQT3w}cHAz=$bB$LtvSyhT-nb4FW9_$s_rb<dyK6lBa=|_Op}=W~OyYmSe#G5H6A^B|?0bFGcXj8x<99!98;5N>'
        b'pb*FP^MBenLPju+L0ilW-!Y-sBW}tq>y>$(n5BuCz&Ey<sMh`{TOL?bH_1_^g1Zl%S?h9+e?FQdfczxaGWSs?FF0nc%egbTL=OJ1'
        b'46Zf_JA5=a>^Ev~0o5Ppmt@4=+BW|0*jwAGpJ#7v%Y)W-vgGJkYYT?;`_|UKENG|xoA#FYU$D2@l%HX5!6_SSZ}a|5dwc6n(B6L6'
        b'+S($2)L{Kfl>Xb}ek7L+^-o~^yY}|;JB*34eG&K{vbV&CfuCV-ZGR46x&7&S<9>+9jmOiGJsQz3|9?ln2Jifz_h(`me?~OMpZQl~'
        b'>&t#<Y#o~IPbt{I9Z)djO#J`bpE-KxJO0eirsD_tmj6Y6rt8lC5r0NENhYCjnsV_>(ZG2t<pJ*lT!I;dNu#rBa?w~PGoAG<$A=CM'
        b'{*b&%tzKh%%>kXMAhr@|rVDLmVlwGw$w&#wPqS?@r>*Q?X{ENAwVNbMB(b5taJU+xnl;Cll+t`63(dW2D7PpE`e<bdODT)7Qf_5Z'
        b'I^C;OPM7Hxq|;fLZn4a;<qq9DKu(Y?-c&4GDLEewNb)Y>+I&oN^zICt&cHO_XXIjMUmzXHsxYRjXQ_@THLicCH2=tn_s_;KG{5iC'
        b'7~AOWn8tN2CtVgB!fZ2x>SqcUiFyvEog7k&GCJAaTmWY2Nn^$x+uVIhsokA{S&eNH71u#^k`a{x%<v4RaSD>BvNmuvyI47yB;jzf'
        b'(zaCB2$X14tuY?Ra8P@^)Ef<Gi%r9EnH6CEDV2fQX)?BH_^h%p4w^gd>}g3m`L-I>YuWS|8o+$xI{9+)KHUF7fVdxX9ADxvx@pR-'
        b'q4uKzOt(@tH9m&MF~q2;h(Bp^mQp3t<)wo-4VpVd2<U{%{HYtbkeaiifulLPgc)LT?_5e7x6!T!%^B7VZWOK0_y^s)7$Dl%P@o|s'
        b'$*elEM1uyd+_dW&uqB=%xoNb|L?LGfiq7QP#-s5QPrt-}6=&Kh%cL=rY-q2f08NXA(r8@0bvd&MZ;F5!#s<Q{e$ONp5mSJD+W;%g'
        b'8N6Z30u4v+Fz&9Oil&!$gJCCQ(y~G{Mz3TY=Ad>vj^n{(jdLB7zR!>+a8NtXQ@aPVebIsoVKWE{J4HFY?}YR&#~jO92fNmIcGSpv'
        b'-BW{0L!$Z}#)Bo#5f18LeU$$M?sk2A9{PsgYmQ!V8=ZiL^$gxiIahnu@9gT5uIfom%Z&TIgL1C%WJey#I4;QUf@}Z~a`w7o`uc)U'
        b'OP(d_qqK)`jq77zKn_}x0!pX(5U=FuC9614-t9J3QZIE_Y6WCO-KsVFR&TG3g#YaqYWVAcR414REC|!rXAT0D|C*4*WB%>9)pgBm'
        b'F(a6iR}u;Aa(dmx8tSD(2%4g9cv%dTmS)sOYK$*dp207y6EI*Io&OHp)~6V_FOG$~FZL3;ml;@WrFJ%C{d`uomIhf#Jol5Vy!iOf'
        b'VP&fkSZOQ!7AvW3(fo!|-v!AGtqiRX0Cx6;93*R_+Ye;7?N~P!C9AQkbrE5ux<DQV+~NB86a-zbn*3LQ8Gv2oUvV$x%xYWzisyhd'
        b'W6zPt%M?JdGrMhRL`UgC{?Y@GZO6L%0iWTOM1N{6MEJ}?_<%@r5K~cOg$U^kUVfnFV+~-ZXwy?p(7cMJQo5Gg9KQ5GT-yaJZ+*Vr'
        b'=p?SNzRUjw4F4a-RjzBwM6-4c3rwuWSyB^&`&Y4gjwhcyo;*B5=0r0ihK~EFmdAl{aRM?lzBDdU(YEw}ltxwju#n|*Q6;wU;Y!dd'
        b'ENU|{LNuS5X~2m-mV??wQ!kk)XA6y1Z&5E=sl7k|(JY~jFCzR)O@KciUAu@tzhg!dTGWo#Oa}kEtWnSaH<~Moxe%(d?PGy&^LB`S'
        b'DXVgcNVP<`qdH=YbcSXThSVyP>tn#SqJr+d0u=!Jp#sfE`1*37(elg3)!S<YtM^HhCd=ROPiAST%{#(ye>O%fd|U%O;4nN0yT=3m'
        b'dQbqTjfbHnVEU0IV7|A^@|lF8;u(|cTCve=V(52JZD8$Xak63^2O5`-mZ?6#L6IcAMw;3Mh{*J^xQHA&Zm(jS1M#AnAGhs-l~|9?'
        b'$!Fl3M&bL-@??PjG*TkUtfDrb{s(vm#j;9SG*>G`_qr^cSi3)a$BuR1Vn7mMh+jrCZ7DuZb>zzP!$J2(>hY`{%{=>lX~udwS^meA'
        b'iFHXSBgIFRW9Sj!UpW*9j>SKuLgv3M1<wve^O8uCZMIBkOl@Y(tQ}!9E0!!hP~PTXTBfwLR*)UJwC#dT7;G|#p6{%glg9%+CZGpd'
        b'XD3M%XDmq5_@en2!XC9fh<!)zmbUG%J@9S4lgA>xGo=2<h}MB27^`*VL9Hv@bK$W}g%`NJv@JWLBjX@Ho6$O(bd1)OP=ujl;TWBR'
        b'jt4{+9|K8krMPVYMigQ7vqVW~4hZ^AQ9ha)>;z&>)Eic6&r*SjdI>Bnv|wP%ivUFmk1tk!h+nXYpv5yy8%?5)k`U5w9*QIkMS5r$'
        b'Y4)I1bR%9aHAD9<EA>JDUR*Y7hh!$$aj0kQvz5k|DybLa1kzPYBP&5+YIqE50qPjOgotIWVT9rGoO{NsljN-^T>#*s1;u4x)YQZS'
        b'7&5fL+n}LsXAG_M+lE#if()&pC=2+R^9L|!-f!F3!yaT~UwW)8ZZBhFmqvD!9v3X_@**2Mwh6Y12*a&e(2#RV8SU#d@v#b8_jIDJ'
        b')VF2FW#!X}N_dc5b}+3gCq+pwhSsg8+Q4rF5%5aqf#_7!E)%sYB|?RGv9}^gWqe6Rz1Yl`!qbb;8ZT4}nT44If4H4lM-}Ioxr9v^'
        b'&OGXHU2E8A4vH3_>!zAzvwTpKa+)tKY1WPj>3ZrVE3^JHj$bq>XrNLeq%>oj_(ABr@3!HgJ6uEjbjFhdqd?-aqy+#QR9`0dDQRCc'
        b'_d;l*Z9TKL^X-s@k!$v)Y~N8GIhH#&xrQiJ&_WegnE$1Tn*P{56LlaiaxEPPU?AItYTUN+|FQS&aZOz5-;+r)31PGZFap7v36}tZ'
        b'LQuJgEd&}a>Mq0r>egL?a`RXFv(`(sx=o^nfV9PUA)(q$f<d6tBCS=i>;|-{y3hr>+uCmJs$1-3ZC`7(wXTx)IWys=c<XL|m(TnD'
        b'1CyC^dCqg5+c|T-&me+M{gJVh{a3hoSy7;_a!^;`jK%pR1eTU~a2NZw28)Zuv83;X5I)2+yf1M5T#V6GMHx$1hJoM$D`9B$n<fk^'
        b'#!37C0s6vh)+<evoO%Pz0S<GZpk5!GgG}$iIoK+tjqfn)Po3!h2RAP<7&u=`!Q6ICo7p>cCgW=4$6Z?fBlI^!I8b-xUvOZ5p-ezW'
        b'tou~&xPaP>+FXRRT?op*ReC{>pdrvaFlxv=^}~1{hA=ULBEV4x5*K`?IVT}oSXju?6?rO(1h<&O^FWVyC2h~vKL_S8iU%ts)hGD2'
        b'GqW@7X54TP%;Czo(6<x3!5kjUv`6vkH_M<?urH^&o#$K_<9IVCRB+1<CG4x;Bw*y>)JgrvE}JdADF*T9P$6|F!5jDlBOBxs&7}*Q'
        b'cw0fB7@Zx-sG^U!c}+sZsBK2%I;^tufpTiUf@)DwuO$b~kH`hjsZzfty3E&yVf6dM{W_{8kfRB8T=0HGdBufHk<)7(vbqNo>=!mM'
        b'uG-1?kzt!-?}PdDlv_Uo(xP)U5HKK-10H;U$J<K}iesNP&z1!r00~U6hx;v)uH%Ov1UVx<ag7vw$4O1ddt6c5Ri!^hvSDCy%6>6*'
        b'Pz?zCl~KO&)H_9g<f1QSjYpKXQg*n<xJhm1Z1llr2uDp<FbsycADP2p@jKD~E?3XN=yM77Dl^<__s}MxI&!LBLA@sRAvSy`3FSyq'
        b'w=2}I>Bk|y{0_YWt1qN#N*ZweKdv}0UNKU?gP-CfC5^ap>Q();s|u<PR*Ix|C<j+Qb3?iPhLn2E{k{0fvuTV@^f8Hc$?U;=pK46&'
        b'KbuZgj}oP57o+PB60r@}Dp&?q6<*;^xDVwd3W<E*fsmIuQVW(IgzF#2bPd1IJg({4B3xwXF~Fa*3xv_r9g7Una%$U0@red`!}i4K'
        b')$?1UAC1Y*rLtokaI5hTa4XhUy`wexH!;;$sce@cIxZ#AaQ0E*_3x@{sBE(XE)!j66NI(f2f@pv&smqSdWT~%UOj))r7Mnwtin^t'
        b'm*#KJ4A}ZrnJ~G<cOj)3kIik)c;v&K{#m76o?X+r@ve1A2fNwnA*^ovl+rT|lxME8WG6Q(Ln+3v)6@divk$i{-gN0N!bN8sXM`Wc'
        b'bn{8B62q2tosJQsbORq3_x>ZP(0SwI;!<L5$mcoVCC&LHdt>YR#n~#V=lPfwxsIOI!t8uU_F_kNn&Sgs?76gOr+TjK$rr+-tjF{S'
        b'@cv`T-XF8(cKkhQ!BdXox{P0x3bW=eO3VE9`S$`p7oqQ0Wvq|?iu8^PMoFf^1<Z#gP;Q*bN!ouVjmVWFPSRc*@msqe{pe>6<<7a`'
        b'((XgI>=+hu)8)<)-GLQpI0ycbWXYlv!TgppTaa@x>67c!=SeAFCN<*Jo9It}QUf;=0v~PAOq9fi>--oy%)RK@z|~Hk$$UVeYz9g='
        b'($<V?_n<x+xn0*$-Y)G+=zd<-P33zS`uOsn&`%W`OR~v!;__pxm2l~lcKGJ>B$d?2#Y+zSDd`N}&21*^k=zRbxYL0>o1=U8=354w'
        b'_&v71cqM@)T_~A|JKL}+v1kp49XOUG>62u?Lw^r1oUZc*R+>}jy!jSb%mZ*4`QftILN>N`7a@+_@FRg^k%vhCwYylgu`4?sK5#Ip'
        b'(1J<TtaYrL`1uaW8N9PY+RQep$-*43!kmXfg1M#+l!4_H%qH||6$%}dLW{v+6Fzj-fI!2q3R~J7=x>w5(IiyAoYZ8fHs}@-3vwzp'
        b'FN(Fn=uYPBNvf%xCf<I)l+^5j250W*e;8V=4~S{VX+3rG`>o+kW}63=^kq!|8@bpiu}%SY;01;e?2tfieE`ptV?25DtqR{TB7SqY'
        b'h|(k_;M6aYNOl5FJc}(9Ey#&Hy(kv=TD}vF@|qGxc|>Pn)$C+d#;PpXf#;G`IYL#Amn!EW7%bcwJ>H6rg*o;KTmuZ%W5H(i(@D#6'
        b'ogP@B&}$`(I8RuR>nMZ~=c4o)CBhYJ9Oy3%?q8Ox$<-~qvLJ^f7R5%syY+EBI_JXD0l!UXe&NDsnO9@_m9fL`z~ZEEp_%SC0QDP)'
        b'`VAQmy@n>@N+s4R98b1+zFb{>rKSy6DuChRJZs_CTMKdLBbZT0zO@e5Ct<qBup<*1L(DS_IhC7~B9xM&X>R5|6Gt4YF-ge%;M<zn'
        b'<_>Ktl0!p^Er&F9#F--IzW)g!PveuZ3De1-gtW59>6l!e7EHd8u$S~ncoUd;oWY@3ELV(=VU07$AbE}u?0b%vJm(>JoMYr;k>ACc'
        b'C&@u@B9fZ<;lhLwY}BdAA{LCsDD<)c+Y*G;u?{1!Efy{`j#{Cm(SiP&9SHv)tC1IR;&W8*1SZCZf||Fw8hra-b;WO{JYa6at}vO|'
        b'mu#Z`Jgbb!!PW0@A>8b7S4an=y#Ge*<cV3gV<(T#8pcj`&Kd(dd2!Z%8+P)&Sw9^+>6rEZv6KIMu#=l&?*}`%F7|&nb~13*|J&F}'
        b'n*zPdcVj1ud^olU41p)-$I@H%du{61MFuRav`gO1x4W)WYZ76#EHisZsl8$J5h{#&CQ%Nzw!;EyuOSTWc5^W5Kbc~DC?=J%rD|KN'
        b'Ee)22EpKRS7FI}x7p!EYVg9`H<E4H?&3V2pOr%|sNCPr$Qhy?@kSh)6<n^&zDI3~z9>7HbZ0Ll}>Ny@l?;0kzXFjR|Eh{>_Y}C${'
        b'H#Hls7Ad@7v7&t26P+TbY=JhpA0Y|yDmJD{O}t%wY`Ry^n!nRsrqf*_3|1P{Z#!at#H)|meV*ELnR=y@s$+T&`5L#WUvut5EpE8d'
        b'N+UuQ>a?6%d5T$1;)%0HKtgMzYLisGkHHPlc+i6*@StxE;XzeYqY9l}ue%iwie3~2IYd%~1BG=}#Hbx_k8rf-t-58;d-R^AtzYMX'
        b'_AGym0HN7A8U_&>Q9K9;)z7&F5Sr%(gxUuIp>&?tvGJe_67PfuO}+&W`VE`LgTAHhkPqWQzh>VH51KcO2X)?x2UR9KC?0f@=Ss?S'
        b'D;{(%!aEk+ig)bSJqRAu^k0kz%^MRBYQGH+s=xYRc+kHH+zc9l2fYJ-R*b-d(wrguZb5^}5gOD)Lp*u9Fy@TFJ@B9mAe37;gdM#T'
        b'9@IVx4{9HY2eto9c+eN`4-ZNR#>9g<Z^eUR*a$?ZGt8x;OmA<_AI76eX*?Z`2YsT?mOU08)V|;+;6Y9Q6?o9RAv~yEs;+lKij=qE'
        b'K}`q`8hZyk=o9Y44%uTIcE}vUgLeLeb1S9?KDVN5xW98N_rQccG4k9>_I+SN@4|!r_**cc_ddUBdZ6>G|3*ycU4~H<`4cdqrvGA0'
        b'=o2H)u4IosyCQKt_}LZHzyIvY5GGW=@h+IqJmS+qOsMHDn9zBc%JzgC6PkTHCNxBNXH4j<K};wizB49t24=K9;XV?aeLE&J#B(Gj'
        b'G-41FDjEY5Dn-8Z4yaHiZSH7P=diB-+_=#6Xg4nO<C!s^#f`*;ei=6!7kVMijSD5Cdp)DwZ@tgQjfo5WIBpDFXx_HVac*2_9m0iP'
        b'ibIk6ZMe{S2;~@D=$`0XaiMuYqZ=1mhj5|i;ut*DNL;9$#)a130T-G*3K#nL7`RZoA~kmq7dqFC3tbz>oEgrm<sg*b2wdnvSRvR$'
        b'@mUJWekWL{5yd+7;Ah>SP#9nxL@FSQbw;?)U_$GqYCDYyt%nhejR{>CeOFBA0tOQr@*%sUZd&ikIIS`UVL~m_dM(o!Oz5+5LzvKA'
        b'ZcL~#4q-yK#i=MekmI?fW9PKqrEw!Lp)+EJFrj5}ZcJ!t+$c=wl$iU#gg!s5_qWrAFrf?LMqxtNPV3E}JJrsQb7MlEnbw=i+{%jk'
        b'88M-C3?@|1U_$M8!-Oul9TVFBD6FjNZpDPwF_=(2g9)v>6%(2?t#{Tm8uU3aZX_mjmx9`rmD@3WTJLn`F&TGHOelsSROqg_njnM+'
        b'70M~QEXa)tb^Z!djzEQ?lX5gHRG)ksEOgh{u+SwK=_84CME-dcD71h9g`S!DuY*Eiq4saWgxW`7LhWu$sQpfuP~{*d)P5&SsC_gh'
        b')INj>wcmybwcimFY9EaWwGU%L?YCh<?V~WE3WN!z&`~{1wm0N<RH%~${L+sCg?``$h1%VqQ2Pi_C}A1_3e6)4Vg~~XHRWHxiLpVU'
        b'V>&wq?^m?@f$)B@4;;hm-2wa^;=Yl1xp{0F6{<XRCrs#;p|Q9zq1j&xoLk1igzg;^6Iz1}lYgI>&<ZyuRDTCd=v`QA*Z%}esOkRk'
        b'HV=piRWn%InmglL?=qJDbw7D5|8=;~Cr08zvq#}V`<MR&T<HDK|5I_H(%W#Mrn}-opK#+SvTw&xgcST_Txk4HTaOa%3`KXSbH6x>'
        b'+t#ClI0|}x$G}nCZ9V$Sfd|G>n0_W41+yAOXsaE}Tn?^AopBg;kM(Hkz=Pu`9&|nWuiz-|vKF<+4gA!#=zU^9{smm9X)Ijm9TtJe'
        b'<n>29I4;!mGvh)ZcjH2H)u!pAaG?hoTqqjlo424s>y%UOZas<uX;f&Pk{ZL0-WeDA0Ja^7xL;go-6&jW9=#TuW~1udxKQuu^pd5%'
        b'kg9j%LhIbPP>9azhjF2GBv<=xB!eMU!Gp1Jp~&Dm<#)iX-Ob*5+#MHsuY7Q(2h0aYJbPc5(5LRO_vd`Ty+7}J?)`=QNMqIteokAf'
        b'OuQdVXv{EXE&6uMTKwIIVZTUY)~5cfw)S7eh2G8Hp1l<pdcRwj_qzxC0JzXqu`2aJgbRH-7TKdA{fhkw`t|<5h6^?Qci}?s7|+}Z'
        b'7kamNrt{|in0V%1xX`=BGjHAe-y6>~Js2)D_NVNv-%TIy3m5vhPLX?0TxcGR3$@<|F4TTETxcD_h1Lz?LhF7SF0}3^<3j6bTxhJk'
        b'_csxPxX?Q7Ecw5P3$3GZp>GZ2LhG~{kz?XQedWC=5i~AzT=dwu&^jqqr=Sj^P0YGsTxi_`;6fpgsYAF>`|Y^Uy3x2$lx>j4h1Lz>'
        b'LQ${-RY&4NzZ(M=nul<qb|VBvqj8~iBXFVi5xCI2pA8pk8^VPa@EBZZ&ppA6pTyh?%t)Wn`4z7!K-oSPE;Mft7h3!vxKR4&O&$-O'
        b'W!X0-E_CTn!-b-D?b&p@+it~$>Tkh?&PGA{J$Y%L<L2eYd-AgKzIbU@B3>>V4GgurfuXYy-ehcCsBH)rs^BrW(1rKJg%-u!1s7^#'
        b'aG|q-9KG^xxKO(r7g{$aF7!Lrt^ALt`5!Zg3tc|~7y2x#BQ?A?HQfD%EC9V7$@};rDk<gxaG|vD$WbSHzmd4mU88WJ-9Hf*YO_bu'
        b'^t15WaiP=ohi=1#28@`U{xCGR-?8qB48>xGVOMV`!&qR8ce$aV*Q3XThVp1=DD!au8vSBpkfHq)FHf*$1Tu8j9g(4hg?B@Sa<+!)'
        b'i6LC5&5a8U<mE-I7{rC{x(6=Q%>X}M-dAJdLXSn?0~d-K==bI2T_1r91@pfT28^Jg2p#qp96>`fhoGT}BcP#m!_d$X_(cX<WMgol'
        b'55ahrJTNYFNbf>Ck>2H9zb7u#5PcV1D5G^n1TSydqEWcey8Fe2zV*PkP@5YUIzZ$F%pZXZt@~GSp|&Ah=#NBR)4ZRE3mvkvAy;W!'
        b'Xh7y&aiKBMcfo}+ZP_mod2MO;gA1)2#)a;>FI*^yqBz#fm#bd{QAC)#;cs^6h7{+7rsxYIuQq7}F0^h0E_Bx*F7&ZG<3bf5;K=s5'
        b'TgPsZWBYmF_ZZmFT_drfFN}!|WjIvyDbRNhZ0Lv6?u-pxGXfiGvwuY7of?G=ed;dQ(0L3tv@X-X!UIGXMunL95k3eGWky)^XCkli'
        b'Uf@s_Q}-|UD14}mfj#yRdFzMqq5EXL^|E1nsAk$&_|Urh!-vx0&?%tr{_vr0j=u}^jEN83IPC%Op>_Adhay|)T}T~bjO8s5Q9cb3'
        b'bz_Z3Fw5Rf+#g1?m9LlGh7nC110y<?p$Iud<Yl=5qKUa<;6oFp$$}5wh7UdC8Y%palNx&~A-aB588C<st-lyFgb%e|8Ra2Qz0?0X'
        b'f$*UZA#`XxgAQG$)^<*1z@fy>D+n9fRY*6b_qf$x>?cHt15P%Ssjouc6>7(|Z%m~zqPLw@-#?W;tNu7TXnvqSe;f@reogA<hLLXH'
        b'ZdAWUzq1|zBsG;Z;L0;s^q(?7QWFg%)la_alw3vYGy5QvR9}2UuXjU95f(I)wNO~7#<i8G&(o|ggx9Ecyqj&uZVr8W5J#UR{s?{k'
        b'FGr~h@>i*obm|1150CWF<)j-n8P%aWb(o>9P(53xj?h^&0Sj#JEYPW?I(5iO^&{SDiMKjfyBW3LM<t!7W?!ZrX|-s&IRQse^0yoF'
        b'1iQY%;6^hZaJ1;`4;wC96x*dj<y?L_&Ig`oq!Q_T!bZ)E;%G~!GQdfMoBTDpwq!{}m6$Gq$P2@YuKl20G_`y?H{O>(n8pS4bue0>'
        b'YV+Wl6+ayYqR9x-Xs*P4k(&MmpEOnA1ln7dm4+XFf48UNSX#OmeTsP=YMbO_zOV2hbg%zaljfzEPrz@VjMPjv`Wm!BLw}N45yZ(`'
        b'%0h)~8YrZ*VdcKO=r<(Ixc!N1=)=v)oT@*Qcz96Qe2JtWe2Ej{y@}^p8S^uPGEzxgw!@pDXl<#-T%7sJ^M=dJcb*sH8L43kl1#VZ'
        b'#3Ptz+Swh#zGJ?%Q7hl^t*tTO4IW~HW?5%>;_|O~H%Y^|IcGF2R|<~mG@7fYjusenEtacIhKBJiEmtg-E7z~LyzaO*UgNlWspTq+'
        b'UbEF<X^CkwXfDOTQ_LW=G)Nl9&-v!V)`JF*stk0L$1}}%@<vS@H}f$RGZ;KXCkB)^To?v}%eG63vRJzUh(af;^&MaNF<+82d7frh'
        b'TdwqIuAFMpG&y>Du2yTV_81(N>X=%C#xdB9K~mv4Cw9)!xYq8o!NLexJYKbgJ~#yZNjq=IP=9E?;&IV2)L%CdMKZWp);evxb|WrV'
        b'i{fj_&Sj=7%#l*zpS&L^&?-X_khP|(wl{5Rx1iPX74ds4As`_lL6DFbUvrqfduyo=>4S-qu~=)FIAO|)eUkpmSbPmhl(9eP$4H+9'
        b'oGJ*-mU@NfI57-iHRE%rS0bVnUa}ow3M!0>nOd3>&Pj=$x|kiE=2eg;>GCBm<HYx9<AVyBs-q(GB$kn~Ag4nT+B-S4nS(Yzyj5x+'
        b'?e|eY+9#(}RG2z&D(MX+!?|S#y8M)1;nbw5;e6#6IEoX!`zW8w9UQN75}>Upm(^&E4z};^i}9Iiq<qxAQ>$aW3g%1X`&o%nlC7Y;'
        b'<!V2t7nUImV?}Zy#@j2;Qk147+Z|XyGFER*xBDh17uY(zG2dh?)rtv{3oP3#dnH<LB-AmisifaLLEC&!P*1;(D<QoDQHWyg4jDSa'
        b'b|b3yMwHe_U;i_z_n%SP7tl5O(D`Cd?Qt}ojvu0We~8jn$OccQq1v07QZ2udXxr#QXF__<gfyzN4@#1u>o?H74{BKrYUZ+=bB3#J'
        b'MORf>Cbg&8tR{UIr~{WM)D!b#r^cL(>Um6<726qv^#!qPly@uTqqWgZoWeYFNn)Y8P(4uzx<vAI>WT3}Nsz<SNV3hn2_12b0{SQw'
        b'$w}zQ>|LPV#buTDlKe%*WxXo3P^b2Caxhazn408B%nnI(fw@Dj_EM;Y3(k>7(kEZOy1s}|y>nyXIg(v^E_CKEE-3v-e#N(;p)ngS'
        b'lm6k_@Tbk+1_J9uPJe8{xzNW%q^RuM(A<a(*GP{FZN<}pQX@R`#z^n*Zw=ZDeo3UiS!;ee$^&i_<1nxVa63aydRL~2cVxm7N%(wl'
        b'qHzD*f^!?LBz&8x&4fl&Y7zPneW|wW=_q1B4Vaz@WE$KNA3ZYRQkt;vxbNW!C9Rj5c_Hms<AJX0y*r{n_N`6U%~4us7;q}A#&E#&'
        b'bOla+Mtax0i7@GsSTE6cv0>_Z?-dfs^d7meR88rl5~T&xDRfSil%_9vl-e8x>^`A8Z3LD_M^D%45!V}2j^vPXSlaTIOgKTD7Qu|d'
        b'ylOqroQtLN1dBbRW2mjgdJI#qiptw`vmxbh4n4zbP;I9#*bg-+75Q;B$py*T(|d}9Ii;wdWw|G~rzb#9$!V1KYN)%XoF!2tflhGo'
        b'mU^Aw_Jy#doh<D)=xOv4NpcFcH8*eiK$X&_=CrE0Mrxv{j6*A5N=R=eh%%yVA}uRl;qg!J-(IS{Ai{~4fP{|tkluN;u**-lv>y%j'
        b'CzfVt_4IdE<JB2YgYox7wNIp+&e8UuG96PwdXuBHe?-^RqfuWA+N6@plDuGUM{r1Q5{!e>N^#Gt#Zq;k_E;!=K2v-K?;dYcPij>M'
        b'Xn$n(D<>JL0C-RzfD=kqOh-uf_~^dqW`4Ve_97~<E8v$zF<8Oi9+i-iM47%_Bt3zj_7<5*t7pi8zeYm)m!W-W6x04?DzJO}rN2qE'
        b'`%s6a2W)EJWofPI2@19U;hcsPsgtEW&Aelsr2R0`t*8wtK&ZAhl%c1S^3|P)?xQB?lo*;q?J1g$wkNIsC-}e*k@Wn%gvvreD5dSB'
        b'AD?=-kn)%9!kvj&M}KhdkC8UYx0RZ(9M^84d383p_evyC1GLa~K{Lo@<wvgehqN2e&jkmV0$Cx5R_$x3;pGBt^Dv!<a|)f&+7(RQ'
        b'!pAU}q}+U?T1R<yyc^tWa(9{>rqLFMj;N%4C6YcjjVp89R9oK;K2Q~z#MLeyRqiEvELoV+1B>E#DhfGRzUV5kiiM%49j^!X9*flG'
        b'3{vj=iwj~lZ#m@?o|2FQs(U`3g${jYV7u7f)WOJ}>B2-QIwo%3CZ$B6b6U@`4^&t|xMWu+7JnckW!aJiIb|tI0T%ys-lph|n&95o'
        b'U<CZb+qChagOWxMKI7@xoDZ6&I)9Iy(4OAr)-pSKqAhYWX({@To{EFC;e%s>lHhWHV?pSSA{Crb+>YO%C)$TY-R0>i&Wogv{Dz_%'
        b'^z{4!-N>t*$GhO|oX#pekiJWp#D&F>5<{@rcy-cFB{s~WPgNXDoU2O1l;NN+9Yw*t>mq04S{^;~>fqjjU<k*M3y7zit^Ce8nPvD^'
        b'bb>IQyAUpxQhrs1(!H?}v7l{X!lWhWGbof-SclUSIHRJxJX6y{h~&o{V4)$d_0mzog5!=;28G&7rxuc&_@~1<K1juA#J!OsRn)j>'
        b'vnDZ@6gTtC9SeKyHP~zcim&K4<G+>sCPtF$_~0Ed{{_E^DS*ofEJH_uDmB~SfVF!?N4C^a)@!7^M422F_0ayS^}dpJb~mS)SF{g1'
        b'VQm*!5|KN$@4yaQ7Ymws_W#5dT7j%&r(-wsUFJ>-f_njS*?U3JAo5_rb;wJgT*7&RdOzQGK{p@j*)Y?&c><DqA$$f5y!0Ggg$5Z?'
        b'NN&C<P%Vx$<<#hX)w-}6V*G-R(q3_{xOia)I4cVa+93l(VXV@$S;Yu3xwJtPN!T}HmU@S&x2e%$N!#5PNmz;<^?45kI^k|<N0YRv'
        b'xU56Z!9tb3&4i)Db}F#RVCt>tut+scu!<U2+EFj^JZ$YI5ZQHDqt(z`?>DZUqd7sx9ySzEBbyq|Zm=f5Dd~R|`(Qm@sy=M>EGEa1'
        b'`<r=X>X0RvL2LT9(OU6z)sc2KbGu&++}BaO!V|87QppD&a7^dw6EZ$I-Of3~C!c`lzX2oDE@-g!*Mk6x5&uZeY+$@-!{uygbhtX~'
        b'0Gjp$^=ytoU3wsCg4iGq1u?8plUzcNnZE5>S9)NvhZ4Q;toI%VQK+O7Q5=G1J-SXJ%4N3(vA`Y9#i9gVZN0ryz#ZDYQqCHHc?#mR'
        b'9wR%u@UvaQKQ?Li1)<nJupNh)-j0PGSa6{9X+z4gT(MN6;VkS8*DhvPbj%i*v<+5Ib34bJ5|ZxHor-RJy20Ac)u|`hYe5ma+3g@H'
        b'_C3&BL!#+hu%}&3@Eq?qA=|n~fLe#LMs)yCbod+?|1fR!tCGVV@U*2#(p8&euJM~!FUoh0!*;!eHJm%#QLs$XQY^XneZ9W|#H!Q6'
        b'qFV^5z}h(=T|g>Sy%4~;n8+)ol6IB&JyiO%&KUzMoqB(N_-zsxQj&HRW?;%_1PM2#=rS>V9A>2Wg(qEL<4b#ML{A^KqUk~ruoC7T'
        b'UAJ?ad2u^E`X9p<3qXH3SkYrB#<whzFcVvp1`IZ6#fA#4zRiW%C;^B?$V^zIdjeC$q0n-5p~LiaO}+PF>lrSp5|RRKFUMgekC9wv'
        b'D9|H}rDy|;rO|5FGeZfu_!aMq31AmZ2TIJ|rD}0;nL0^Sn29+(up|>QJcMVVk-*CR&xk9aAA*A=c|ed+5GpC`bm<7J#_u~c3;i>&'
        b'-Ak&r#7!X3U_xeK?QEEu>FE4^f|}7#dn|NGAiEJJS774!1P?hCu|GDP?c`x8@+m4RBJ%(hGo@;R)AJ_5#;9pi3L#cMP$eRGH^UCl'
        b'xs{sn{&#sfaS_Ye@!W2r>kaxhi4!8=c9)98M7h|?caG&vbR~UUu)(oMuy1Fa@_Sb|ubnWnv<H#QnOGMC7O>an+PGLvt)DtLq8T?3'
        b';t<Uyhek)~mSX*#JhaxD6WhSfTXci?+(q}>&E(_$f&LOZtb3`TDfE96uBE0_zaFEhXsxW!Xksh|hxP3U%VAxM*|Dn(vx=vn0J+I*'
        b'4Vcnou)Y>?E^vya(Pnuy#nC3T9Cb7X4W+}em>t%A5$K^EJ#6%`yy`eh-!`+iHAKv6sIG0b{2`{cw%SNR<2^@&)h{~^aHmu^Ia&_e'
        b'8ke;EDdhlrij_U3<!xQ%(U!gxOSA3l9@JG^Q*}*>))j$D?nu#?ZM|^4Bc;05VZ9z<sjz7p9Tsa!Ws~+=gry-xQ(>z%rkpj~G%uyJ'
        b'8K7ph!O>GIY%=$l;m_G4!ZtJ9Is1jM@|!8&^n7aTIh4}#GTe0hD7<d|c6{&@^Ch!Qd>Y!gZ2z%(kAsZ*{12=R%iGSJeOq|y=-EHQ'
        b'AIDK)(@`?;ttb{ro;uoTjVXVdXM63vCIcbFEDqmKc6Uq)b)2#}`cuxnC;Y1G>_zmaOGrNaZtdibiS(n-M?7+L2^~!i@?ny+T->fZ'
        b'G3zTs#WT8w9hFB({*n0~rJ7?aHbt@Bd7X5YOO;ahHTC-l_!)-NH_-34(Z4f{7azA-ytFS#Q4C`2y5245ZH=(DMzmUrweN+%&CGzz'
        b'h)jWE89T#hm|pdT!FV=RXo%0sXyAO(rsrdkf#e*BWcNj&`qMLv8PoIj-XsNj0Tw0*=g_;rq!{x_#^zXmbsPo=Wp|^pqS~7Y&@!w>'
        b'vceOG_J0sPX^5Wx7(vgA5!M%ho=R=gFg=-xRo{gfGknf&7G}sR)5196>;#T`%%!PhK<hEzf~NUvDuWE3n(8abX0%(e$ee7@RcBva'
        b'WYA<^t*%Df1hs|=&pAg$?{G4L(nAvt`!wU?qxNrH^8|Fq&qP>PK*tBQRjA_=segQfG3~Zfq&6B6NPnC1ifcA!PUu;wFd}H7x45`)'
        b'2?xyt%8|A-V(U&&n(E)hXtWdv6zNI&)A9c$vrv4rJp2dHw$EL3R|_JnxzN>n+NV)hWs6{~mqqSMuMb=H%yM2<tj;3nBd~6MyP&VT'
        b'rx~wciHnQAbs1Q3yFQm6zm^#1#IRRm=Ml>}<US=AOV&FoH}wH|sB||EX#B<{F3u0VFwEy|$srP*1lDRb1}^YHYVq2Z5CPZHPQJz<'
        b'+!n`Na~yCD0fT`vMS9jC++~7AnC3-pq=zPa6C*zcycyS22k-up#AT<SAj50;9vW>*g@E){`d}IzTt#^}y`WD`%atgPu30b*fly&p'
        b'-a?G-Dn(O0oxbL1Hp8_qeT_p!-WLQkB$ifXR0vQ`qDUs^5yW7){m%@~JR_|9h*oQ|HW=}Y^h;P&kwuRXcwd^jAT7V1Sj?Wy$$m`o'
        b'Y-(wmA!u3tVW0d4miTBhUev=haXs96ExgsbSnGqDFrM-~dr;VRB+7&2qqw00pCdgaza~BAdv>i*aoiU|qxHIFOT$?e!ZOMk0<ohn'
        b'Cd%VnV|9A~C%<^;G<jBYrNE%;S#jm;*{cQL=++w|3_U$pKmJs6_Ucz>PR8^|(4H7}MyPo~ayn*?t74o%IH#-p(PPplu})u>h~$KM'
        b'=#Ker^dQF-`eBzRvK+-aiR8-l;*USTmJ7e;NkS#z<E4JA!iRB(R0l0Dla>lUmd-KESu5$eS`vRUoHr+Jj@dw!zljs4U5Ia<x%Crx'
        b't$(}`<|&f87P|S9f+c7B?k>{)A>1<;<(XM<f{Vf{iA@sH<(e%>R#2kjyamRKj|B>}hr(%1%oDJHU$2H+_XEFP)4m%FcNYdMj94gG'
        b'm{@9D5Zcw>YJ(+hf4{3Slq41l$^;}q$FAV*c}piiyvqf)UvO;{w6md~q7K)JIJCyzJ-vaO*L1U++m4=p=4#}Y3G|m;v@wHuOwOgc'
        b'IT@*keX<@CuPO~9(7wc_V&U3Q(4CX4{x@991u$zQzuBXme}YxMYhtfH+`1{ez$t09ex!W`QF%llHq2?t5Bt6)cRm`dc|j`h7_J;G'
        b'X^R%@e>IY9>2i>Q(|k;vjGeJsnk9`M4g5I<j7+vzw#_l;$N#<2qw1?EtH5Pu!2L`QbnlAi+Gc#6vYl;z(-lR~vT0D5QbEfvmYy{W'
        b'rJZQEves4`YddvAe(c6!fr(us7HqgyGmB69p^yLVlYfS?BtkuiEZ8A8T#E&teB3So@ve7u)%HFfj>1Yg#4MzDc-F#2`bcC+MZ4Bx'
        b'i#a4Qk3E}v*cWC0sslmp&7=z_TOSM8s?m_YNIQ|*cgz=w?0^sqR$1cpE2p}pz$mtfvtV3x%av@+mBgc(qmJxsw0+tV9Rq8XM1v+e'
        b'rlkeh#TJ8PjuFKF%$&3+k9TLEB>0$tGbc?WxsoWAM8|*@(}h7cp|HdtsQ{itdHgW_BZ!1NzoE~oiRQb$WW<f$Lth#aZSacm2v0Q3'
        b'=3nsh)o2Pdn`5LFpK|HAZL_5qKe;;k0K_;1raN&l@T(YcxY5EYkKk|HMxkfb+oC*ZUOlTQ>_pnQevRtg8yVb4yqOd7hRY&#gtJLo'
        b'%x7Wyq*KUNOREF(Oiq?;i#8$?m;V-b<-6CUGR$^r0@}FTYlWv0$u^}BBgy=?II4HAo#5I|U5(x$d4YU;StM>*>A-l&4#_rD`c13k'
        b'sD$bclf3M1Oa9IcX%L1U?YBZPXh>2iak^Yl{MjDv_>B}7RYDZ?iNJD7(t9q<`nRywI)U~&3e94Ugk{HiWj}83nt_&(nD%^_CRUQb'
        b'dVBL6Yo@Tj$(148U29-jq6?7IjJGDoN-#mPMzbwJRlx%8W~$;@WEkliov}TkFjFy`<78vatfGCcc$V#yBtb>`Bq(-IkiXiUnA?<_'
        b'G=CvssdF^)fUk;I-^*$O-<_psBpT9MVukkKxh%1c1RhQEoCD2x$XBlA?0JIOp3TH!&vsVGm#&StA-z=jEUUoaC<U27DgKrj&}zTl'
        b'kLNJ35*I+=2mdvHb<k`4ondr>(Al1hjR}0#+8B1=`7l}7c&$FH2OMM=%030_{f@e@-YsF$PM6jjxzW770e3B0Ry;RpwonaeVgtAw'
        b'BZzR5uu|952;9m5Da!<#yf5Jj$pIZg*X8nSgY}G^zF~^!EmXNQNY)^Yj!xTs>};4YBD?{|*vS@{O<<_pN_xlDPDYmT1stV)s{n_r'
        b'J8>h7-?g$l;VOxvCn%#P@-<{LPCXZPlGEW67OnGYXYXN`M<!WLNZx+3qb2y=O%pp-hV`xr)1ISX3@th@>FcLjKuDHi()~CHcZ7j@'
        b'D(nPDV)mklu*#|mj^v1h8RkqaOK0PN_Udv7sTz~2ISRE@r4A}o2d`9zXbTY=wFO~Pi=|>4$*<_usl7K`)8+7V77aQAB94GR0i;2v'
        b'4r~-Q=4juN(eJwg+`Dz`c2-dZPRH<cKh13DCV?eabB4Rfq`OEDlcO%qTQnpewM6&y)wvDV5_`!%b#vNT%{cUWUM=oZ2V7PMhHS>&'
        b'`mDw}4pAG~WaV-mteV8-r;fCGVjKCEqh5JO2O>XQYZe&6A&aNz(JCYI&{{JGeoxUq`F+Wj$w@?sKMu~bkdLjj{B1?C*AwMyMYui)'
        b'GxAx1+$n|)1KCfVC&@Ba_CRMd8Mup_*mtsreC5O6Pv|@OhYx2GeJ4+%Tu^-{fA`_cn7)&Z`OQ;yU1aThRBZX3gCwip-Bk7D7p%_L'
        b'T^~;MwAgjsyryQ*nhiIA0I@-T(N#>6kwFP~GuicL`goRT3TCks>|Rwxdd4RpWy*W!2h#35<H~#N2Xc$^udd;k=?oWmf=;Giat+(H'
        b'd>Ne|_Y9|-4N=zc{hZ<ZAzu&P|M%r*ERfxvpYaLVaDK)`vN7^AcFX?T@-x0J`|0@^t+M~0pYeZBe#Us&{p4qyD*NA^pYdks|BLw<'
        b')!0T(MsU@e8N5su$;lKh=MY@<LUE!p5zAm@z?}?MsqfabOqS@vfGMcvEnFFl*?b7aUQK!>0`i;YFJK=|ZF$UbX`!$-H~V+oMGM6{'
        b'vU8|q=IY#M_AQG+ivX<<?ecd8=*MG+Q@c5hly)z=0nN0&`g}{1SF1(S(j>9XCrp%*kD+CSb{s0ONAO9+;Z*o_jb08O&&1K$dJHqC'
        b'E}WlbPR@0h*$adA5H)YH_7I1K4eV|YGo{^!e7A|p2&ztVWCmrhYj<SG%<O{AjtW`c;mgVsE~yVOmy=8%41s~l!Y9(FCXg-X%GEFH'
        b'sF$Vc-BLe7p{`Y_cND63u2k=mcX+KWj0nrPsIpPJ=Xz?-&}&QT<wlRj%&sOKwVUh==Yz8Ui6^ICo{NXiFSJ&x=md@d#U!3MW5bm~'
        b'=h6}B8><!SG^u)<93^qINKqaf8~S3D`jy3ap?a^Bszp9QES2L}RjT~hU-N=oI;vJ9cZh<Re2u2W(fJw^&{_1tp|j|w5&0U?;kezc'
        b')XPQZTvY+eI-bJ%nfpMZNk_es2qDKS&`p<*eisiNf%^z2iIukLB)>2<alLuN_l0V+STUQcQ}0>M*Qsla>fbT>lUJ&1NkT!@iZ|=j'
        b'wF(Y)P992nkhPI>Bb%M{<2@^npMB!hwMTJfIf0`4-#*K;@Gxyys7`Is2XTR@koO1Z+>LeG09qQ<Hn`c}3pa5iWwWWRqK|$QHT|d%'
        b'V4}1i6?-xLA#CuZe`1~trEg5bNME8ACZd+C(RpBs6FupNaODb~IFl6Y;hkMCY}z-JnvjEu(^j77S$pL3$n>>-xbsi$+>O8Ht)#Z0'
        b')P$ZrO+tiSdzC(x*5S3%7QKGM*CfIZQNQc7C9gxd@$i0)t3j}bYg6w5`EX9cdQydbz|MJ2f9!mRm+Dj87UCWF&pDNW<>^yqir;Ki'
        b'Z_^cdm&*uMh!8ooeKJmD`pP126}4j}wW}vhxIS0)&W#1!%h1LzRq8zpIVeXRs=-x+2!Yk8LYkt;TS4tmQM(qUDURRBfY@@6g4(m#'
        b'<AdX$Cnp!cFEUNJ0x>7@5MobSqSNHU(B!OwnfcI{YgC(+X^2g93P;4IBe*_-XQOJTWZjy=5%Fn63P)m#n@_$E#;2mEP##B4GuIh7'
        b'#3TJ6k6M98behZb$Qk0}o$77IBJY~8K^`%AE@>X=XdYD}9vK)ORd8t8rYpEvgv#H-A_Hf`mE?^13blE$03?;jb+uCFvvY)PX_ufm'
        b'&>gb^C3A#Fy5rzS&aI^O=v6L-MWcThYo%&8dYmm6u76f>yyp@~?kdDds8g%(L=Wj2pT6sh6G~Skdu<&~yhnJ(ks{|Tq@)T<=}L%)'
        b'Y6J*bRI9LIdIFn^Ce?_ZJ-N~Yp79Xk2Klu>j*+TKMgXrGWuz;Tqk~^4k7JE9%mv(jd(GOqaXqmJV40X8XQP~V2oGV4&dTbuO$Szw'
        b'%;kYnO68-RcTrpzgg9iaT>w>Kq7r9;Y{EP#KEVrvy#ue!$qU@HHf*N2T&LcqTI!u2M970_zL(G#wWZ#2YKMZ_g=Q>Pe(XjDyC+VV'
        b'I6IS_%wS$o4KCCG#*eN*mj)_fiWQ%-<Y^j`BmWdvq$cXCz-!e6a+smPh!xbf{4a5(9DDn%^g1t~5&@+WOWDu*&^b(7nK90Bk8uQs'
        b'6mMqtXShlQ&j!FC--kh_(}RS;B_=5YF(6rf23G}nZ_q!NTab&uqpJh;>0t@TNNroW#CvThArGR*njgxE+@e~7NLSG^wg{-dhDbnX'
        b'zJF21S?8-fitHGw#Dz*QTvTVXV#$c%(iM~k=nTL$>7^U@6X|v2;Dk9f3{-@kFFLKw*8-)MCYl_a8N!OuIwb!DUm4_0=N#CQ-hdO^'
        b'F`DGUCEg_=Jm{Ul5QcCfAG?+28!+fncGf&%3!<Uq3tT@Hdpj?ESZ)fpWBSrN%MIeGJ=RrNixIyWO`9@c4B9|$h6o$v<=AwUvT2<!'
        b'<7kS5oFy1t!_7!kA#D^RZy+jv&G5123p!26nvr9;yX>Pe6v<qLL$aTKtL*=)V<;#<vVX5Jz$C#~BZp`QQA&KIlnu&{U1n(iCCI_w'
        b'Sa6>i1D(PKO@J7LI*LmS)2@K3)4^UcS@1^C9(%vE>u9;iC`0!0b~(C*^ip=g^D(<*n6i;uP*6bnlI()%+gGe80PaVxbwvIJ!UBB+'
        b'2h9%B-7j!u4EA>M2w9J3EAL^OipII(1<Se0$q?5RrQ633&QCmB@0K$u%#qZa!Q7^Y&7jArD)go?x55#aTW=|~Lr&W#H;lF?SQrtN'
        b'fV*>uc++rU;V@j-UEW<-O1%=!o`*}O#f1AP500g`#OB-e7VaUchjc?<F$T?`w>8)>**u_PB=&b~x`~QGy^S6%^S~HBb`N`hZQy?j'
        b'Po?vjJXDPS63kf0QDeEwP$aFAqJR9)8A~dihsrJAv?kK>UC0bT>CRfpjH8*&C~?u>ZlfPGFfrauKa)#z1pTr1qTe=({s@}>yUEo^'
        b'`Cd#Yzq#@6^SSok0mkPl`+jDhOSIje&m~&M_PNAZK38*#&$W#0bBzz~b2s0~=lWp!l6&~8w+9LXFyhxgkIyYAxZ*6nr@sO!7Z2;~'
        b'tz!V6JM->i2x%DrpG!pjTw_?}oN*sMS06c~t8Rx2nsN_+yLaHf+uxErP)hl$u4uCtME@j5pN*r4KW{BP5VvwF`FB^$5YzBD)()#B'
        b'j01S6I5RTdpK-5v|GYciFQw!CN6OfYy}Wz4U&@wKHDqvdtOSOi#FeXSwoQ}DPvff8c$MW@lBY^dK%i-VT!F@xK0LPgyNs=wjYd~g'
        b'2?ll49E}(on4A%FG~<5fD4tDQngnJIc@NQwXCoo{8%}anX^9HT9Lky0%^^LT+1e6{2Kc1c;`)Vnbd$pd%j<j`eIe}&ir&aDlN@3`'
        b'K9&I{zyQ~$*F7}S0HZvBcelUm-1gVG_rC3K+)uK<`YOiy4$1Bv?5|#T2m7o2$!i|{zjMvwbI&zT(Nfy}KIoc<%kXk-2v=nZzN`IJ'
        b'CftYpg+OV@{!Y8y{>I(I{w|>H@6?~o{@&M`hvbpI1jTw#8(cJ(wq5%F<GQB}p7FponE2RrPyGfOd!W=doH8P)c#V!$P$#Txc9qwS'
        b'AE}^D+Ef+VqL=*#GlnwO2xHZb+aGo7ryj*e<+tjm>I^OqLHZe65bG8A<JM;a_2uDlVv`Z{vxwGDX5T9=6y>HW8XS{hlzvveSjJ!H'
        b'r)<OMDm<vd<iHwLXQ+a*h0bYRlU@e;Sw3ub>G)`HEbdVd8k%Twh-efa4cpis(HxXF;(CaW5XpDdPlo0j=g~Y=zDS@%GBqV%GWuCg'
        b'%Qj60NWQY<?mR7uK>F!id<$&>W6%~pbC|F@=%-;&w%wcr{UmPRlNcVzBDa1z7c+dU`I3o`Mvj4vDQDh&3?UCA{d7h?;27>8<F}7t'
        b'6*2RkV_>8H-!5ik05mf3Q97*9F?5###iv<c^KS`{ycyMe7#k92W=G4P`5?<kx@X)k-L14tY%SwEhkWnY6&4K!NGoPacE1nt1#gKT'
        b'kPA@-OhghFLJLJ|0vQxdZ<{KZAS%sE0oN9k5=mvj=%Qv-YGSBIs0t}|jr{fJqYYl*h@nl=kMxK(ZLf}A)%6S%tB&6;n(rIxJ6A>R'
        b'Ee<A#RCK<L9bL{UNDeMolHxf-aXh-9RI=ik6h$hwLNCeV4=9fJkRm3tmWbm6B=9~%DO2R{3?y-&5Rr~ypOll^OJaS&lodLo<$qxn'
        b'rvAOqS{+cVe3X_a#a@i$%c;G|nO;r|TQ1n>+40Qe-uEXr6YV^mdY^W~WQZd?V{NCRZK)^+me?TTa8;C*6x+C1S3bG3WCp99r+S^W'
        b'Xc6f_24<h!bcl>DuZ_}CwpOZ66YJ>aqYs?cYkMZsfGw+$s#oz@)fE!a7L-%nc#>sQTRZY5_r5jM=PxEP`L^;t{~p>ui0eOc>3uO9'
        b'P~9XywNyn}3X-R1J*MCQT`<Ukr76kjtb(PI6{}KKC?$D+z6t9{7@}Nl4k(s8mwvJ;JDa0Yo2#xek>P2UD)sLQwOQ_5Vx;y$I2CPn'
        b'pw|)*`-nJ?F!{n1bSkTlak(NfiYvFURCIF+3zi+DDWuHMP{HH#3s2*PL}C>o&ILY_vK8yRs(4d!VU7zen+r<4@<ak7wI{p6alsE)'
        b'hG2o?`)t8qefzQNvif(<hfwYh)3+6qJG;Do9Cv;>t8<yBxv9QF+DZMcm3rAm?FK%aSKIAV2Y?UfDSO^mGg|4qC~Ze{CoZ+BO(4X!'
        b'zv8AQXy!zl*u1s9eCqylt0z}XI%W8BTt%C4nE(paS3KNl3%-od`>4%Rf3k-U<YmR^=$0zc>p7+wogh(U;y_bITVf|l{`OKU^<wRA'
        b'^ElF9e6-eJo>b9xr0K#|-qtgHYLk;r?Qwpn(f5ji2lB2@VH(w-JoYA0IcluamO*DtdGVCCVjLMJHdn5#n6y&;l2QHQg^D}0WuH8d'
        b'mnd6FXMtLQ60(>=FW^oYhB#T~xFEuv!C2rpqb>MjYi%t`VSt^dOs#+PIywHMhg(ZMSC$Iu%PFR@ZVwQ<KDE6lU;t#U4|v!_*{q)d'
        b'H=15AbY8NlO@o<KOhd`4LMN9*H5(}t%B0d(eA1(^)Dz0pmrov%XbH6)GGQR^RA3=Z<}w3NiPSgEalsdN24R67I$Ln9wX%|?uaBW`'
        b'oOx1fiDzMnpk6;nA0OrzNG$R~a||TrHBB6qOv?nMuKXLKuXG>KcSu~^G4ODDc(aZ&p(HwOX(#!L5}H1D79D1ei#!MN1U|!AbW94$'
        b'1Tvezky9^~`3|PP(4nj?C{@U5l(PkfyfuN~VZ%weP+R@PK;E+Paymgr^ehdS7ujbM3#mOi>Xq!g`HKwDpicdY=sTV=7^7z>(^2pH'
        b'X&`^4Ex6LUe!bEYvz_v)@M%0!*0?pcULWWlH`4JC78-P3C4ac}<Cj46jGy2Kjy+u3c!b?>L|mL6)}HCpl$Hq%)a$n}nLn6D9Nn7!'
        b'8#hIQACy8Q107zAajEq)k`wWWLj9r~1S|U*6juxh*71<*H$}^CI=Lvfg~*#Vm=S|+>m5zVwVOKXWh3><sN@u{pmP$iS`zO}x8urv'
        b'*OZOdnBR8v`{Fg_H`h?kNi$e>(l?ZiE6WG;bpulB756zU6DP1TaxNjj3_)`a9|<}XK^T1KJcH#Ctdl_o_Tiv5^liAqd~_~p%MrfV'
        b'Tw{A5o%PQ(bHcdHImc$an9bR6nGj<-UjluB!{BB5v+i*sI(t>LWR<~p_m8H}Y8u8FIG%<Ijw%B)_!4}qofE>xMYRLOw-8oh4QVFM'
        b'?ueQ;FVDtS0VaEy-^dXgDtwg$rd#TzN>l2Nr>TxBEB?HYL&lR6%vUNtTj)!lQ9S(q?tkizrIpjUB-&`B9OOmf;qO=Y$ovSycNJ`c'
        b'i-n~|^26D1*Jmin#bEA-<kh-x)(e~{w&-2%Y@Tx**3D_gD=2OH!_ZU%L3(60H4+W1<YNxAsGT?|?7!y9k{YNJ!m6hAtD@IBG;2H2'
        b'@_06xAv#RNO?Py&fsS}o*&uqBh&DJ9*RCTfL>swL^f^<`3%rdiY00xBE-!gTQL<50vZAo$X<f-mX~|R4k`2<5Rnn5@q$TU6C2OQ5'
        b'>lCt$I@v}!2NN5jldmZ9Kh>3N?DEy0;%y6in5?WtAMv&ndx?rUI@vSve)T>Rjk0H~(ud<c$gK)CmX!tW=g?-M{%cpO>=~Qv*^sYY'
        b'qPCmPFI@`R8mJ*oQ<SX9@Ds;+re*pi@QH6+k@MrgI{X5gjYGHdh{BT9mo5K!-m=POSw@DpT9$WOUZRh*!_z+5Min0upXn>v*k@V#'
        b';Z9t+mX+U*>nCG#Gs<`3u(ZvOkB@9XmviCLJ2Ev6E}y}m3-~`1Q<`~6{PKgivWAyr%8$pDMcCYURC*JpH}al9m(FLQqR-qD=<YAD'
        b'x!2&oaydq9<zY`8E~gvQS(d<sel7Ndp?m_a-^_ECU_U^qJXZdrGxxzoGM1m{+h-~LknU4wDMQVwSj2kXp`GXx+WALu<$q#*mM5Wr'
        b'GZZ6M@vzUK+Dt6}5s}Wa0`<5Asy%~x$zUm;<iXf2&!S)Rpw@ac>?v?(HS|st@rV=_;?2-h0Gr}HJTp{m3??Fdg0J!ksLxDA(Vx*&'
        b'5Xn3Y%86q${1ZInvNbRf{^D5YEUrqnIyqOODp_4Mf%qjakmIzulC!5*O>oZPL16OXPTmv)h=N{#krRjs7?#{Ky=sy(jn~I#<?r#J'
        b'pOIUf<1z9v{Wy%SsGrTNPLmMZT<E9hFMro3@EnhO!TmU%PPVG+bYI6MuSwVoEbo$43;7HER2EHknnbw;RP$X9uAIv2ldV4cg79O*'
        b'C4*3RqNj3;u4J`yqpQkSFXI8Nk?j0ff#(cTq$pWUJnI4;JR4XT&R6nz<OFC(e+i@iE77?jl?{W-oVAkz`Kpo)`fr&>#J9khjm<oj'
        b'CAmM$18&%02onf*#kpMgLvocDq5ihANh+HJej7_R1ag%Zu=J%kF~g;jJrxIWWdycgpI<lrY^<>GLssI<1~!7aVx88*tyV|hhphEo'
        b'ZHFLYZ*k4Tm6IS|SLEAJSsj#(Z(!5kHY${@gq8HnKppdymy)OCB`f2kT&e77w5ccML@K19t+Ewz*~+u-1n&*F@k7?4g^gU4EA!69'
        b'-DRb+HPS4Mn1YTpeugW7;=KGi5~xrB71JBoO3rQc+8KHgxu~ED3eJF``HduY<}k55=$&3~-ich`&7!<UCinh5>D7U;ScFA!oPQkv'
        b'iXeE`hhh7P{5k<pk~ka4U=K3bO>ONkwc~6bvQV)^np#X3B@etjr!;U=zBE=G0w%9;xjbrINf05Aia|@8a(d5nxm+%dE|kiF-eqWY'
        b')4*ONZN$++2#PNrhrSdL6$8|w(hBKvxilnN9wHy+Zn(htz6+ZO(h!dApP64bZkV^X(%SzL(CQ4NY4vcAhw%TG=tMEPn@%3kNzcQW'
        b'l&WNFvZuu?6ody54X!~t2c`BFI*Ydad+Ahxtllr3F#i<-<@2s>6@hxFqpb)eD|96rj3w)x2;7*nIgmt}tb^Zdj0}N>wrK)EIZ3;!'
        b'WIZ_p?3=;A-j7%E+2eE`Ew}yK4EAq;zzDE^Ys6+_$r>ov;P2Vg=wBZ|fa^zRJDH+(t*a_Pf0YXb4*W-;E*vAPY<#SxNn;aW?^gby'
        b'I0RRIix<zpi7lK!L9&KZ47PXy3#?Mt4AS3NvfA>vm&g>8HzQCddkO@2EyzU*wm-DIj$vd5o8XL=-=|#j1j`xwP*`pgxJxPhA$|mY'
        b'Uzw8-s4EYS6=x_w-ImLd^3dW~BXu*6Q8ojkY#BJHKxJhnAMqQC&l`vI)6MUpD#6k6V7a?|m#^{<+_?g+e<1osouDg#_y#x1RyA^T'
        b'{%ol~E{l)aP*z=iMRo*tevTe&l{R>sZ58TDv|1UeqLXQ%&N;e{hjbzOZ<DPG^AMZRDRNyVKZ-CeV!yzSB%D#${^CJC#1HeKnT<FR'
        b'@@v;@!E){k+<9Dm5VDo!HcxlSC=T(X3o+w+ni-)p#ifOAX52ouQS6AvTY(*06ZlA!5I>fW$&b)zd8m9a?>7;}d4ZTm&>z4i33NG|'
        b'=(J!k;Leig?O(GyWzWNy->t=!Pa+|KIktsk#x52Fk`RKo&ee2+i)}g_*e83=^XQSlMzVM|*CtyQnl;I0ZGcvcC7MnPztw`RXwqm;'
        b'h|yV9nFd-sZ*AzbYCr<dcrc~be{<^HcDDTswyoqjcn+nC1vv3buEj3tT4tM%(G<4Ip4;%%KJolc*_zreqwKlPk~PH%K-aR+OrBA;'
        b'+7o1b^^KkT-_&e(R9h*}w+^-8C5aC=^P&B-Zwa+;q5fYGK-*mb&i}+~6B{{~iiJ~RySaK6*6pDL7LYdCGp2wG{$cF`AdX=}(Jx&<'
        b'5pZI6KvkeJf~$GM(Go+Iyy3rlDMa(oZ{C*|iR-Qgj`kJQL6xA9Q#C<Za?|O_7Omzi=R?#2h2s4(_%(Hb(Pl?tF*KbxJ%O(|432hn'
        b'QKn1Obn}x?rw<BEpm27qV^P|o;sn1;J}B@qq`=PkH;qFY_9(VrSyRWzODS7F?1bI+EZ((Tuo%}P9aGh~bqvb+5Bi9Vz)dw^)55`~'
        b'DUeM|AIqjGz^0jn?(OMXX&H`$N`Yi5J%|r7MW2NqHfqB{Rf>0sh#xsN*=p^hVz-tlf8a<#V+e&eTk4I=rpq>zYBX15hjHhp5MCoK'
        b'<AauIe<5bhW`D#P)Gv4lmtlPI=Cf(SEQM|%yNu(Mfmg3_yU2L71R14TFlR+!pk0e`ViL`OK^1iR|HSdfvulkB9``$bq*UiYQ)H`Q'
        b'mdU_&cF{Cf6tXnCIlDvUvej{I<Jtucgx1F`D+DYU3T5je(!|BEWGF0I=L};bnOcacUUxy1YT4^$D_OgTFEYgEEfNpg*+=eXXG8qJ'
        b'&Ms!`tZKBKEu`)2%(3lk$sO!0xXw!b*mkz$4tBPP19tWg0gMDJ+i*=+vQAk*Pb{a9F}5=&Ghz^b&TVG3@1f$NfSWMwjeO|>WM0Mk'
        b'Fb|Y9rZAI;;==qdXGe00sduxjMSPfjm2B;D#<<>QTM+}U(hLZhDPEwu)wY)0!M4(_X4tka9+L;dz8!s2A&NuOfIhw=x4w<86XQq{'
        b'EJ}Y3GOS=#og%cngc)t%i+6)fJ=F~+^{}6~35=;<BUp~-isQkaJ{g)d(PnKKWlUEGFvj$}wPnzfy3J_x8<LP6$c{2b)OnNLl?4_Q'
        b'DAghR+3m5<gzINwmwhm>(NKr1B0VpcJioq4TY%cMW&~W8J>MYcvo@TMh;Oz29@=g@wEj%@LuX;t<B1v#;MuIdU*7}-w;i&1Vi!N|'
        b'vuc=w{#K2rdHvDat*v~lla4T;{XQ_E-wpK1o`<S=M{X)9pkqy~0qnQVZNHxc`>g}}4U4PQM%mgMWm96`URA&t@q>rjxcO~3!NZyf'
        b'WXBH*wP^u#7Aa^>wCH2nisuSDWoyBRlO!1NZp2fQ-v$4P&_8e+%xuVa1HkaAMOC|%Z7^X-zsf$>$<|i+DR2I>;0=dvK1TYq9H5fp'
        b'H;Ipmf>`-SAF>5wmyQax;Q?-wZj`M<vD7-^+kavpU80>Frw3Y)!U7W(_?~H?+G2C2Uz~sV1>c95fw%MR{}=!&KUoCj<YAbCjU}gR'
        b'V7;36_>C@q=j&`(me$4+HLS61d&cdy-Tv{wuwK`U((60fHZEh^%9-z;-D=x1z_w@7akbmF-5#$Fn>Jdnb?iui_N2etvO6_w9j(%S'
        b'Y^fipbhz&I?-|ohl(Ojn3gQK%+8_Eew!M%&wsM1NM-qeryO(XZpBg~69mVS-Y`gwnv+egeeq`F`5wO^T;MpYhG@HfZTC*pF%Hr*|'
        b'R7{iL*xgwY8vr3iGryhCzU)s&8^EJDb|MHVNak#h!6@bJMt7hQWNDKykw*WC0SGg82b6E0Ob8*`_a;4(!#BOamPl5i_}#-Oz-nuZ'
        b'9$4OwKWKs+UEa>gY?7}_#l)>ue=a%d3E{_Y{oS%Em#qV@B94tnlb5UmuR`o#VRX=r%<$?!E=2O#5V<!b<gFf#+=*0>z4ANDUVrPr'
        b'zcqG;b$w;UgT?MWIQWzZx9nAJxGV*q@<$x$^N0{WoC)C*{x&*(kMn2ZchRyNC~7am?i#);!Nsf@b}`D4E~e#>Cd4){7{5FJC&cf_'
        b'#}MFS&^7Wg&R=2f7``ZGL=68N{x8SyANt)ZhA)a79mD?`?^*=z2Q9lHez(0oP<>Le?`50_$80_rQ_(JATTV%sDsN|jGa&@PZ*V0m'
        b'x-`}MH9#oiOqkNhpS<YyCr~FZ;ifVa!}`FMo&lfIH`bb93pkYE;Z*^*gmEZ?3xgKF!G(dS@?-b1pc{QK9DE7rsWF0e!T;eQMFp;g'
        b'yg0xt396P=1?odkY6-9jy|sQOPteeh&G0AgOD=LV>pq9Iz|!lg`4}u47#}l#yZGqt86`)B4IGp;;HXtw?KiBr;#kmGXa053JDeE3'
        b'ANUxwiJ7**KhwiAR{=i8u+Tr<FXY06hZthoJ&Lv<T0RMYa%5$Ohl+zm=W0}3Y#;YH_?Jp(ZVi!k9iz7$y%=p5Eq!QzUOBxnhL#5O'
        b'KHli~an-<b#>$R}A4}<dCL?WUGXpo3gPje#-OkpGwzG!8HAE$>A<#aP+s+Oehp`qAqP+FsW1{_NJr@P6*U@VS#=}ex9a=m5i8a!}'
        b'Jc^2o+E$KqFPp)=pmjqT2e}uHUN$0TzAbL-U&?rvQ89D;kbQgbF~_qjbqV~jd`r!kzJ;@#gN%NG+vqDrcl0yqu>reRUP?oLhNERM'
        b'!YisR0WU+0@-q8Ba(kJF2A8w;LRwfBp$(sJCelu&#jF8wZME<ZdAvw^7@>n$hxm>3qvNV<uuS=KqI;Plm90sXf_zF#*3cpv#nr#|'
        b'BLr=cWu6O2e*O{Ap4E}7btgZ9H4EvHb9$n&<hMqvrnZLOPF|a|8<8SVd0_cTAxV|{X5h{#Sdw7h1QiPIq*!FzzMbgX;*lSt|I;vK'
        b'2KGcHT<WJ{`HACg@BG1HS@r!g^tmEu3TCsY_Z`IbkHST9ej=`vz{RuZokS3(Oa%TO`V74@Zk4UiJBrzCSf7P&Nt5)IthY5izwfgc'
        b')&A!}6RHd<6mg1kfnJsDx9I<Gk#Dof)?aE9S{o;}wY9#CwU(^6?we>y^K$y2ce%3l*1Cz8+J$XRwpz?qvL3o1D-SiTA-;FPGqUN!'
        b'rvFfW=fc)5U21#%dHuI8TRjHrw^kc=s8(fbc0oHfI|j4_3h2sfRdX=$(bkf+eX?g3O!CZKIH`UDPi!`iLm3cS2TdNbH|cJB)71o2'
        b'tKLBi!@PICDqk9*vVsj<yC}c>pip(f1!l69i=jQhqybgQT6kzg5A)5q(w7xTI*xngT}*=L6^L!6O}9?AVg1q0$1s@W#e)2$Pb*|k'
        b'?Vg!V2Vmfz6BG0u7}yJC2lDypv`)Y}C^1og99-$jz#r$t2kO$pCyRF&N9^S*Ph#aZoOl<b_q&OAM(%^ZhaM@rm`BP}=-e1Y9uXMy'
        b'yB}drpo326AgO_lKW^Ep?~fQ5j6c%pcMI?Y?bg!o7Dmt$JDMJ}ojrQ9K5cNbUiu*`O97$TE$<e}$J(n`WnoS$daa;m$knIQ??MK5'
        b'zsGnN(m(kYdPlws`APJ`oMdI*FTIN}=V}Z~c5p<Wa22%OuM+9!(8S=xd^%uu6Chy-po2E&<H#Az9#=jXZv;gXxft_Izv%X7=+?x~'
        b'aAho(@{vd-+W>L}(zX652v_<}uKjbA^rruhIFnKr+>c0)myg_zA7h@2$bsQF^H#nYfp6F8&?+KU++Z8cx0=y>GmPL{Wkn<ZR=(AY'
        b'#kWks!T|6T499kVpI$fkQb5lh9S^gBO0*6EevWu=Ag9?H6lh2fkE7WNe3FF`?k%H0UEJu{Z)j>E_RE^n$eahKtGGR6T-eC+?!pTN'
        b'V2Ps$+7QdF8ij0aVjLK;LfM+=>5fIQiN%E_Yn;k!I@vl=7y-6k>Q9suX6q-QxKg%Cv>oJOT`?z;#9=K7rsk{yJXQu<EQLkHQzEbh'
        b'@$7}{LfI<C|7GuO;G(MX|M7G0JTMOzof(jDz`FM$FpOFQSb+I3gT#~CchJIztrkcKt@dlKJuYr@hk}8yU~FXuwVgppph&<<(%68C'
        b')NsFIW!7quiCJl(Dc}q;|IfKIJY>3?``g{`|M&X;eR-I3&OPUI&iS0r`JB&rxbGVzh!>}@U-G***jSE2L7x*`E>42iW^ClT%$#AU'
        b'BoNIMxC<^MKJX+P`Q!+uP0L3OB>Qes<Yry7!^G{HgjayG3eFd)5bH2Sea#Az>po)BpJoMjR3BK+rW33niA_g!0x)_~zwWzBX?&mN'
        b'8Yc0uPhhpDuWpqc6lT3lb8)!*Rf4FGmVZr=KFpvz0V!UL%GNH+>AJOn41e!jM#-e5FN#uCxP2ML;1{Q|{3de7GY}wBV_FGHT{FRN'
        b'@zlwFy%QD(iYt31)l-AGKjH#M?^>8FVdlHU*x)!lC*`!9g~TUTR-VpIo`mA^Y5nUoT}{_G&jo>Q@W+EXP+agRWP?0)Q>#~sAxzz2'
        b'w9pW?eXKLCvjpmN>w@Zpwv&~b8Lh$wvgWMk)mc2%32Y$$-4v+8eYgtM3{o`FHA26bot~l)gfv1q8zo$vh%|vAY*Zkh=T7lN1Ri|B'
        b'gQkUBW>xM{@^?JqHcLY+b;6RsA~E_qmpr--kCkb_W!4g{ghEN@UKWqyeR8)=;<1Jf3TnRfVz>V5aE6j6{Ss#=ancyhkbcrtaE3mZ'
        b'^uLBPR5$6L#~Io@>Ho(W`o9Nf=*CIE24^U6(*NB!Lj!^TU&I+QfS@#xt%9y)C4mhRC|>^_UGw{MW(R0WvLw)}<3w!s7BjO2U;547'
        b'JPN*3X3^wlCZYyO_<iS?a{*Sy9%=VunJpR>SQgCLfEb9_D1&?!jXB#6>r3X_afxEsY<qLHE~Z_vXIHg@=zUpiX6&qn*Zsk~9@YeL'
        b'Uj*=YK6aR~<8p+Ww9INjGh@eBPVc?+>UU7Ul^@yqD1iUSmM*bfQO%U^dA;Cbu2Z}?`=#WI_(Bz=cc^26#dMe=&pMyA`E5EZ;ER-3'
        b'e$AKnE?-_dtWk70`&%_z#fO;}PcVNv&ur>oHhas?braRuFLn0tfXn0vbWjDGZT$sk5bG>&_QDOZvu-cAz;<A;p~UPY9$;uY%WVDy'
        b'o=_sQSs&9Dv_zD{*v##UG;t#HLPF38tWeHT5+j~Gf9e?-zNCupvwC0f_uW&))$2XsDN~DI@&O9z^GseuAsxOy?1dES+%OJOC>}!!'
        b'&GkYGRb2ro)JdSV*_$z*&}RIq&t{A#qzk+jp3u|d@q{7*F`f{^;|bmA^5F@I1IO@$7P@`~p3vMY@Psyx!xJi6cU^cw%l+0e)~n;>'
        b'%)A;-j(H4EX!EbZ6SDp<;0ev`v|)i6gA=MM!f-;H$H578-t1S+Y@U{0?LfZ{PiW%x@u~N}uLDoW`ftM%s=|0en|VB;s_}S2RX#kS'
        b'%~!({+WZSVq0M-7ZRYWWHvbY&X#W_V(B_}v32puvp3vr>;R$X2hj>EPYvBpa#P1iz{}NxKX4!S(30eOWctUfFp7{lyko6y88_dM-'
        b'*2e$x-P+vre-cl~`oD)KH1nT)x7K>?m&LAlv$p72Zyo+Vp3v3ghJP>h*6YL*vi|Sk30<oVy_)O96SDs2@q}iMf44S%+zWi+Q+_p`'
        b'(5=6=?&I+de#N`BK0Kj@YvTz;3eDc33o;gcP3)U%>89QZ{{)_p_1}ai#G?syzJ85&;tPK{ZXxdHctVz|;t3UPLSxmwYAvp)HBaXs'
        b';t5?--(MR3e+y4Bo>11$-i^Or`8eZk%Z=#goaS#W{GuhX*T?1r67OmLA7cs49ET+oKMqSM{HyE368eYza5XHUUn|@9ij#jF`WMc('
        b'AN`Y9Le~E@mQd%@SD9~r9hOj$^?K*qXRbZpj$sL1bH4q{bz%uw|IJuJoinb9C3MaCwrL!e(CBO{R{ydEalewa<0o4v9sP>w_Me$+'
        b'b6+0*-=1rKfhBY&iLL#sV+mbrVD{Rt4@=1UAHWj2S;1oo&Guml&B0hgH;{?AZCAw-`eoa^SVG}t*M}u!{S{a*|1_4++(f2o3`^*)'
        b'iKAFTi@jJvRmnykOX!n{{3b>fB@{0tucm;p)pSiPp=;{jKa5}rZTmOt-=gP!o&GK2yxR8<TTZ2H8^xL^GW{#oI{!Kxp=;@_+`Q|='
        b'5xQR8`!B>1y5{_`;yQ7Jtp7F~A^KW4Lf6*6cU~WkkoDh&BQ$XYM~JtM{tk}NOpF&3e-#`d!w8O0_pingO2GIl*6YR*dJB)uTz+iw'
        b'dtTSV5!&fR5rVN<%#TgJEk#d{w&S0|5VHP@F@&zk&*|5RA!NNi{GER#hS0UzkV{`DhLH6?iy<^~9EQ;NVc8paoftya|0ssg?8NzV'
        b'{xOD7)#CYce+7n66~+(}1dL(`b<Vjy459awJ`ACxF$|%^zk?w(i`VrSLr8=%gi;k4!hi=6%JJ`R_s4)f+(Z835QIYR4!TQdWt>!S'
        b'wG>%*5>-`{yu4-OR(aP_YV!lP6C3=BrQu7f*u^}2kTJIHpa=|*c7Og*%t?vNQetVa5brWO+td8J>%2vLh@WRJ9i%EB*i9yX>A~;q'
        b'|9ZHfA|G5(l@~7P86GaEYKw?xzitFCsA>c+sEWr6s=5YV(A+V+psEqPpsI0rL36K-7j#5Ah8HyTXLv#4i9B4;3;sM@(6>|e?->IN'
        b'vX6oV<;IMF1$}<oKLiVU?W+R+5wIY8{m-$2>|Pw18N-?BF;~F~nmd9OH1~S2f_S2T4c823x~5+ZD`??$U<G+;<%SJs&eHrJV+GmA'
        b'VFiWXIEod-{v)iQ8UFtmD~Lax3?9xrFy&`hK~>j-6=WZW6%-ygiWL<6kFbJ7{(lcE$lJ%^6NfWpfmdP$RV4^l1;#MX^B;Jr3W=>s'
        b'f~qHGzYvp+k7G|2`a!DaW_F5kf8>nzM`x}K`eR}Y-_Tj{AmfqW2E{O26PcHcOO~uiieX+z%zi28Ba9Z516`Ed_Hy8tUa+8wr=Bd5'
        b'<2{b?a6uuyrenCE8X*rCv_cBh`S}VO4dQ718`*S#8bb^E%T>^V__`geLBm1n0jw9Uf)%uU5TOyYAU^qfHJ2|3rC;XvkXYu0E-NL#'
        b'CS3OOox&^H9PYjxBpbfUIsREWe=M)Zhw4q?wV?CtzzBA-4_;{gM&Lyeh41{p5{d^H5^oz6*9`JO9$)D6VDfi^Sie?z@r5L0vT3+z'
        b'%P783HcBIwD|50*?jSDfC~;aj$l!}w;TJBCepik(2Z#$kD~H)4BiS4_d2#k^b9RC`z>kueGg2&t*6av#w#Kq8Cwq=LTWfZh)XS>h'
        b'UuMo`&Dr5=v*)U^X;t=A?gKgh4Zztam^tT}xy=sKL7{ptzPomLk!;g<2qGFt_1^I49}CVq5;wBS<b{%AQZfn$RL$HrL&&{?iFh%M'
        b'oLLmN-52D;_fVX3T)5eR@U=RG99nwx`-=__C5cR+I0IG6nn^^NX^X=5jZ<b3_3FB&MU;L!%`KvU&Xy{e_=Q|L_LqI$ltMuug%8O1'
        b'3xoJx+eFGDF&`yZiH4`a707+}+<ILj-zewARI9)uIW97563&Vb3cFsUrnKKiwF<@f{u&AC^JEfAm?lnil%|nm-}2*Dd1;*$;V<;%'
        b'x<~1qm!B2;=y|{P$KP$_zmb_4faVZ0gj<pdPHYjeLc}gX@Rt%$f%MFc{5PLD<Rq!}qNwOJ;$8t|StQC4f<aTi>AV!(OPV~2%y)*T'
        b'f3kFwEC-l#)3mAl*Ad@Xx=9G(X;UA%kW$Rd7N!J|;uMrfqQ#CcjY*1oo?RM<=lUFySnE)*9i-u7d4@-x`CDWdmS=n<U-LrramhhH'
        b'{Qb=m<s}36Brj;nI>sC474o`_K?5b*KyH=IkWrzBJMs4v=L#S82mNrk^PNx#NOC&&d*7En-1%o5k(1L|_xQ{AY;p-JZ(q3EF09Rn'
        b'oRxGmgPK4$=*s`5J5*0Q&J>p2cbX}1J#h1k)5`KnGyR(RI8{|e?=aJm)%7oHqq6=S{lF}O^4G3fy>*7Hf%1M2xWJXee~a<BCr_q0'
        b'9X*|mC!!{770nPH+to>-EfZ-YJ_90+iG}4^Su;fXO>L>fmhELSdAx;4kcfo{Wmf)3?GU$mGH>{iDi-hc%<+C3cI5kvHQ#uA-`Rxz'
        b'{80w&KPWgZY$d}_jf?+wEWYOCNIdkPRUTzXBQ^-Al0_2Sdz$*k*7~6hWclNY%-zG&j~07-?*?D*wG@x_-m^FHy;qckd(Z6n(geL{'
        b'DGnr)6LIf_il(u~|B7~2$eYULAatTMC0E3E4zoypROx(9-c%|-DB`4iT=YnH6?hKHs1RS5i5~XH_a6RUpDp$F+02D0cHwCza&FRT'
        b'ru<_a{TlAE<CNoXg=P1ij&7Lf?Xy4eeI|!Kt1;8z<NEA4<?A!Kx6c|T@_m-<?K6Y7&kD|OCB1#-ckMnqO(aa<`)pDlRU>}Klli9~'
        b'sb`_@uIRJe)8qQaJk~e8<NK^&EIzk)T)aqrTx5~x+b)<j@%-1NN5-rH>Gc;j2(~OSJ3J{Z@)$>H0$DJ~e}Wy%Oez>FC&cS%Cn1j_'
        b'=z4{t@>%PCF7!bQQ8{hpku=h%axoEdBkQ6G8PhL=AR-n#hO#!*ih}Az+>LTPUpa4*BdOluXxbr3V?yKs1oCD0ZZyL!F9*w-f^f3N'
        b'@}??F!6iqX&Qz)>5+P10-_fEH;5x|!2E<p66U$2o4dI(ZxX)!3QaR|-2D0fBS#e!tg-Bjphe<04wHUwjqG+PS=M#>$z=%*q#PrFT'
        b'TgYaHs3m&uCyHdKMG3xkf=9K({+b-ZsCH!$u4Mk5GDum?pbiI7^A2H@x%9MalqYY?uE~?HWWFXgjW+SVBQ{Y`sfhbhRul+4`CK-_'
        b'lN9ENY>X#0qZwu#sYOlQvMYHa2A*`ucC;u)d4gq-l6X0SzsswpiytkxL|5%<-p7T0w_BTdWG^!BGgG9=x)Fc#&$(CjiiOrHoO@&r'
        b'mJVHwg7wJk+^r4c-jX4?-ehXhT0+-0@?VKInJV~euSU{^%JG-<Om?&HThmaA846g{N)|`O9SJ5Fr;MJa$dklzP8m#_U=BGQG9<x`'
        b'jFhnz)!1K-X~P`L>P)NxZ&>7=mSECI=3^}G&pcVhpJaT0QdCnm^k{fRIsBD)d$d!9T8Z2U!r=&vP%9&}H=fypyA66Mw}t@mz=7Ok'
        b'+*kNq(c7oE`?e9@3(DRO4Nvm*GL&2H?N2UMR`Hat+|Z`^e7S4K$_35RO7z}HP}BSBm2LG3D%8={)}q9;c8p2J7++RzC5yE;F!#td'
        b'okq-kxbd{9iQVZjvAS|r;j<I;@6pCj@D2P{L2kt8x1qBU9`jK|g0f~V;xc7Mt;-^T#fhcbflPIU4%0g5`v8K-Ocg3n2rBs~vqiuJ'
        b'$&4{B9Wm`Oqz+&ILsNikdT@!X@fDg&!D<0W6ydw#dWS0vRKk25*L#KtBT$fQNY9S&9^Wd(<%XvtE*{jYMG_$i%{@aLTU|?ppCQUz'
        b'waS|BiL%o0$A6g4M#-2MnYX^WUAPf!HjzN&E<;?D3>f0AG9~lYICGf_gj_-J)wL<Z2!bX<9zy}lX(=!HP;ZO~QZx@L$$Tw^){R8p'
        b'4*7h~Z$o;gOJE>#za|6(8Km`RK9i0Nodu66@V9buAO6AYV9cu#L&=J!;r8P6Jve=4l^Cl3C7<;>5sdmTc<(IW3)CdIchwI~?@KY)'
        b'8swZyikT*J;rAB8^M7F8kqQXH>|j9_fVKj`_zVIH$1n$(^HPu{s3J)6V`wgOR+{XOm}V)K8wB;9Ud<3tiSVPixGkT9cz(+JX4T~U'
        b'FkMq3V``=RG{Sr&1qwbn%0@gxQE!TnJA&!|oSh&5XKcvZ`N1Sp$ukkxYEtgKKQwKWj&%M$z8z|po^g%Xc0iZgAl1`ZdX_fY6!a~k'
        b'_AY5TOG6(<&JJ|YS)dej790<wSoaYf`L_Q-;c*f70VdVC80y&}UBN=;uEg+7MA4myy2W^NbRVm5oThaiQ6D@Q&SUXBpBF<W-+}N8'
        b'ok;&J-F0JUF#5oLZ>4R9^A%~+D^f@#o`;;Z(xy5oBo)sFg&}RKmFB5PaRPE~l{RgcLYE`wW@*zFoVq9$Ic?IWDxA7Vhny><P0!%e'
        b'MKh3dskA9mnmi4CU<+`*AZ>a<dSr^sSte~Nmx?2x{Bld1>6z%+`-`Kd9Jw1=cfMDtxyd{DxLa_$diM~yB?QdG&ZnhKCMo~zd1s=u'
        b'$smnT`9-kGGv?$##N<mC$r=~yT18?dYUiZgoRllXx$!sOosUSH)=KfaVC{d9cK<=j72qfB4@tWpmU2(>yaRpb%$GK;k|q<#nJaC|'
        b'myZ9gdy_`W-6y60rqJzGoF%EryEOzQrGhD0W9i0n3%%p0oV!!{sYbNBVM@_l1j1zu1EJIE8(kpe@Q9z)#qrQT^Q81kirriB?twF1'
        b'dgz1bjxKJ;^9s`pWyel4h?=~sk5!&h4KzkZpWkU_JGi*giKge2GbZ9^Y@bDW<OxsP3vGB_*x($PF6VBRnto8=zt7XvJI(axZD<O9'
        b'>w5<)he|_rqa)!jO?S2N?+^lkO;xCC7Jk19^_42+U5&MEnFYg+(p}M^(qr-Ew}>iklVX%uyGGh6$LZy4@wNdVy@Q>^c065PO)yiW'
        b'S`7##t)+Pzj@Gsz5>HL#8rr9;496t&RE2J)BCcArh@2sqBjgyVF0l<pf-%;WQtPK<Wkt6`Uc(e=<n{!EM-sW6Hi)GuDiJ(^E?@+B'
        b')T9L94~b+TsWIHuc?&YAr0HyWte42bB>sE%LT-XIPBSeiK*pVs#A#F+a%tjwW~0c3Vzr3XV*8DgK-Al%Y^g7&E>X=1rFsF3$eT=N'
        b'MF|0FDofx}B+7J1t6<f%a77k^X(b)nZ;DlLpGu7PyG*RfxY)%ENU}sO<674mGCeCm4e5<UIwaQfS&ZUz=<XV^5Hxy_kYG9`<w*oR'
        b')f7cwdw|uB=yDDjPDwKUBGIi>Y!yINgKoP!;{yquq*za;gi{ZMODWOPY9lt6QT7`W=5>it?23Gm6fYp0pGkV3CpvG!lO@#a0gZ+`'
        b'B6*;8d9`CxR&lhcv<;@REJqWTj#B3XHiN?<q{1C{w-xy#Dx7;wQoQMAr$fU0Spw=4C>GsDq*PBd3S37fFJd0Xv%NTmKu4lH#sED3'
        b'cHT@N?nTHH3{Q@Ho9?WTw31wv#H)UjBcV~;E=jSSH>gOhILsRXN=#=lWu8U_gS16=Bp>Bo6o`NFAZxau*F<oy;=-M;N?<m3SWK`Q'
        b'r_`oBg^i|lw&<>SeQDv_!AHJD&c`J%c(|v1WgWR;K2%zpWK5#FRwATM#=MD`L?(*~;CrW#pr01WA74{LcYTg$T7lX-^28r|oL0#L'
        b'TKxTHrb3d!PCT;e9Fy%eYqa747>^qyDb=D=lfO-V$HT0U7|O6k!IVf8NR2&365KS!3gcAlHxx?{vjQo!PzF;dQLtK_*S|)hQ{gly'
        b'+C}TqV+|;k(6fptA{J&x-3pyjU4-9tLfMNXkwyN@<C2Fg#zdDMY4v&+GgqR2AR79fnFWg?j-E=F=5hZmi6SU6r8bcJorF@Q)KaO0'
        b'HjkMH3`m1`!)i&7Sy`GS5Q3qBoYN%=oeVMR5`(}X(C-2pLc~R5zJ(DYm|YZ!+KN<3Ez!sl^9@9*Qa}jGlN4!;!@xL~Nn#1okwiO}'
        b'N|q2reG+D{3klWwuod%R4BjOH|NSuAC%PCT&|6^?X$_0{c7sKe<I2*fGYhf(0)DhIotZ76m0FbS@&&=h8}%oR`Jo8i{B)zxl{G0{'
        b'ktCaMK($19y24wsPOt(IYOpXAz#TFj(Jp;hI#@*-qC8Py40P!ORxq&=U^UbU`iP0f{RNz4bP|g}L8h0o0VHB(K>x{5(1Gmfl2Wtr'
        b'HWxCwbc@sHOOQTXreI}2FP|unP(a@*RO%=~uT<ko1+Gvi)bhKTqke1drlDKA?lAn#&p6Y?T=D~Tu7eI$&Ii*-2^CW>fst|1Pam!|'
        b'D$?m}+5LQ%TNEz`MllLWakW4!Mkvy@h?xM4MYyvG8GVNu2|?%RnRY+^T!)cBN@=v81V$Tvk2KOY1-MQN)rffTF*KPWc<WZ61y&?4'
        b'#PSn;(vKpGx20t?`<aTP;|W+ez<4*Bnr2x{k&kA->KD_&A%Q+?O;f@7HM|)gMPykNtm6iwh1RjWmZqDIOhq)E#cL!r=)CB5zgUBC'
        b'K5hW$>jVO-5dF0uJyi{AA^L=$;e;QpRO@Li4u0i_7~FFRmO)d~(P9_6YXuB^<9t{2=YB@u;{8}AqCfKsFbIrG;AwjFr+y%h=nj`J'
        b'__5!Zf4d)~hoF~^k<@18s$tOT-*j=DpI3eZ2my?Kg(^Mz_kQJO7*9gzBB&4a2lN~mob?t{T(nW*Iu+pGN`^1M#y%wK^msrukE{pr'
        b'Kj8(@Y*-+{lw-mlzL<-r9&ljMn&ut-Ni^Hz@jMMK`lJ0f-!k)-Pn$!2jK7WWH@;P3k<5OjUi%ktb0JAIq<?3gbNal`C#KEIXV}<h'
        b'mV6fXRNJ58--_cBQos1itefJLv%CH8o%7q*Ht)XU!nXK*5$ah%s~)_4d*rU!Kx^(R_4T-HJ?is#*0D$*JR|8YH*;woxOY6BiAgXi'
        b'Lp}aB&*Qmi?v_W9W%kLqKSCUY&x7lo=XqM7M`#f0-S>|2bN1_54dwH`_kV2af<M&F%b0V>k>}qu?|1aV_YdB&d!DBdS*NCT%=5n+'
        b'|NCU#Ef1}pp7eV4J5`szSUls4hItQHt=oCNao4;@g2IM7A9;J;d*9pacKiN$I^dOp=NB?P!+@C{hV(;Ik=}^w3%{^vHvuo6MyL(y'
        b'`ZO}~Y4zBk@PIXdv*9a+3mbu}S&7yD2hOKG0`457H5uPU2;w%t^Vs)ph}WM4XQ|mg4}J3S+i%x5wb+1`PKETdgW~n;GWO4V55h0P'
        b'^D=O2rU(;BAb&xL^c1AY-yWww>G|utGry11KLKguFN<bx0{0-eV>gOtFFO;b-v@MTXXEs1A+8Y|EDw;!GjEp#{QJS(LkkmoZW1PL'
        b'DT~v4{tOb}nTT|dZ)T)0Q5=NOX((&W7jb$a__shE&OrQY!=l+Iz}*IJ2xxqOf5D}LgL%pHI`Hfe@a!n?>MoCH_L@oJ*?D;g?Snc('
        b'yWfRE5P{kjDniAx&x6Yc_j_>Lz`Y6XD{u$FK|O~&9s)U_+=b7_>C3=LKye7Ch-ceM<ACA#O$mg}VRAd9Y1x6}(42bsw*`0u<;-~x'
        b';ufw!Sw?Ukj{w^4nb!mLXoU2d>Nx%D@S6$r9sxHU+{b^3)3-p}+u*iKpl_t{`U~JrL!R02JM(y)e#^EveK{AWKL+_vP8TLxAm38p'
        b'_i6amZvjaNj@Q$oc>PMhc>Q}ogMxf--y%%(hcwCH^nZ)ffBZ4jl}1@ePi7$_I8$7k=g*Jg_B491c|-U8`5{QV9UOZ7J>f@-aulAY'
        b'{ZMeDAj<>}fm47B1V@1j1xJI^gA;<2;52=LtfMeazy2^tZ<@G&-XU=FlWvVe;3V6gz1cJ|ZT>Tt*m?RskP8UML~oed2L4)Ts{@=3'
        b'TsgSqT7=$@L};c7^U&iCh2ME?9?x_f298d}zXX;Y{1*-5F3~}p1{{r_J&j;oNKgyrJGiy=qS?E_y$VhNblV{AgBXM?@OyMF)Dzst'
        b';JUy~H&9u%S!9+(Pi5tUJFP=mr-5(lfG)zczl0KLEYoiMF$RTa0Ky<67QU_no@cyuhE$#(0}+)~&WC^Wyy%Vp9}ou|#Q%Qsc;3Ok'
        b'L-<DlX+f-z9?~rYr+6Yx-#0y8ud9Qx)*Ppwz6<0E+{dqgyu1c7@pzoRry)*12!73${qtV^Ax=O0RGgmPx_{ov@8k3~2#13IG_(ne'
        b't?o_H>{+`-vmNl84~_$8I*#SHeD0l}rZn`gn;2bie&g$e|Dm{S`I~z{|IPvB1iCX7k0B4(&`}1B!C)QcialUGrD*&Ggphf5STG+&'
        b'1&HrMoY|A2S(jn<6i7@-3NW%clP7=>zO0I7o`&Ivt-InECot<hhV>qPGe8a2g@RU7Y8t7-=7XM43+5Ba4`GR9)<O=MFUJ~>;Sp~R'
        b'8J|N|;2OyxgB+c|Mcir+zMmJ5su^KTH_FHxhFQrt$(51ou{v&or3|e|&$!2foK-mTHy$+W07NPTE9d|%)Ie``?TAu0AMo^isBBv9'
        b'vF=0%_O{5&UsUX#EX2!Hq)&-9RX$q&VjJ~b<up-=Kpc!v#sUxnT!<oUMMj#(cn7W&kOb=(DZpw<SCDGG$%XSJwT0SKqNKnm1oplZ'
        b'CPIS;d|(0T1uG2mJV>Pm`w9%LETxNvj5Kasm;hmdJX4NzNV8ZML>94#`{Qs*tqK^cAn+p~O3B1{{OUi5Ht&3@w5z;~FeSBNo556t'
        b'Eo8|7!%f2in0rZFO2*`2Y7ULGNMD5l4*>Z90|7x`hrj@;e%fP5MibMh8Ho-8ef-h6V9yB$soO;>oOG@~I+92T1TYL-P^v&c@E*e9'
        b'$nu?eaq{6P0u~t+vSCI%3^odwbj4Bp7B`sx6;(lYY@0E|myKY>kuK(bPsIb!c;5e84=nbKWV+Ww8`GKlJO~zkUjIGg{42)%v`7mC'
        b'acjV84PQ|lC87zn7?unRJQa&QY&I&6l2l}P%55fVHp2E-ELeJ2+z_l+M)s}^0yg_@=Htr;g+0m2bXG&I&CX=Ajq-3dd-3AzB{|s{'
        b'1s#+ya=I+B>+*u>`owMe`OIR*Xl53NOg+RZOCM#k@1h@SGd<Hri7MJJ<NjTtF-l#VI?!Pz6EEy%Xh=jJIN@;gge%oQXm1uIqL90n'
        b'?l@{@mRKQDqg30qQIsgzA2QtCQ>m=l8YV>n5)|?{*w=W&`KwniZy=2mT=+WnV)MSC$Ll`nc~tq-BZ3qlw17R#7?(DD-jk&4xmS6@'
        b'(YN^hA@vW5*~_SBR{W5a)OI3!`Fj7v?4>;^%5(#)U=kgD=@lEK_xdHvk)iVP;`cou7PLZ(3|JxzFJ8t$Vg(3DVm|7*!<%V=1;*p4'
        b'Nq=n>gS}|Y{!K^rJ-M$SL+NE$?_g0Qv;l?{@F@4`VZ*bR1BexP0AjK$tjupZn0qjB;Q^#nzZ?`T-?7-yr@p(VURht$B0J11r5;88'
        b'`bJYzX%gN^u{cf7wPoGiRw6?py~)_rDMQDS<x8PqJ$D29R@}EtWL(Bz^BrY8bQ$!F0zF8H9#fD-5lBp;Q<Ly*8;t!OPRT=(8svu^'
        b'o)b<)-2^LGi?nOc7K!Qkwi4-viFjAbv;li%A$u3t8zhfU`{L!GTOxu)5fMQ}QY0_7LN)Ce=A*<WDKB3s7D8MzRKucF?=5`}$K7R@'
        b'<b_Y|UU1py?*cn{OKGe4Py-Fj0dC~lk(Uq9YTy8O`(?125it$#%uYx0$_6Qg4=4`<!97a#@jb0Aa(R8Dg+9R;zo|c6mXALRVHXo9'
        b'ky%bnPJC}@Szyp7!-ttAAV;64KxeCe2w9qbXVv3kC5X+ko<Av1Fqu^i^{>^+T7^h`pg|G<wylES=sp2r^||u%FT&&~)*pq`gOX|f'
        b'aOg0zct^w6RTTkgSc;OC?%19Dm<P%2nA1_bplZmR&cUGOVSFi&W$ps&zpc5=oV}vvImF2>8?`QDyo(k**i#H^+!c?Zct&^`c!n2W'
        b'Dy_n9GL@LB9es$YvVK4y)q$QTl{#jHy8fxBp36gQRTPZVswhA2p(I;n;!JG*>@}6Nb6_azO&VlOU|123zbW?{DCl7+l)$gya0f&{'
        b'2WTJBPScR`JRr=R8iF-qKnmUlgr)M4moKje-a1bWiDei{uzqit7{$sF+d)9Xb2^1EULt3Zk+mma=xLdN#6bDuA(l-apq>YmtFwV+'
        b'6j{{oIl*L{nkzkZ<KkEU(y8a~jbuc`km9*0r`-tb(MCK>u9p@u2>j-DqgDf}V7VP;q$B%>%O-hMWM>S<{m4;Pw;NZl4iF<b3(xT$'
        b'+6?KDoM9*k5-MB)^FdAm!Mq05CFIjLL;43HeF#n;S$D=qkLbJ+@<M#9n2<lNV`Q)_3rj{ir7R$s$mtw9b;F5=rFa>Ppf0f_A<y%r'
        b'N#xTc5^TrNsfZIWqd}byL!D=g)cI7@nJ^+SfSA<vC`>W|^NAwR@~jJ{BX5u|p48J*y?gOo#ZX1X5U=WCjS4yzAJTDEK^i~2|G!~~'
        b'hTc!q!djmx8N!=GOgdx19z{$#Q#^#iTt5G^WBy}PnZhBM2XsU_Oc#1ZI{)qivu+5_3bYm~z!VJWrmg^mh&x$`Q^B|j!21;Z+yly<'
        b'Wxx;^s`&lTNWJ24qKc}_G%@=gVKUR1NAZbC&3~a*ne)COP^@`@q<9r-A)F5kaZe86qjW-?i@%$*a;UiOmLtuuAjY#Do_h@_`nN-{'
        b'Qa8rBqVF5h2jB%U%&5_K3@P|yM<@_VizSeP(MB&Ds#t=#Krhka^h<_dF4RY-dp(Nz>Cuaa&`g)lZye{pbDV#X&mWyOgje~7bgxIT'
        b'GCewV2=DE9{mJ9}N#p#9xGWTe4GN@l8KW`BXhFJOl#W0c3`B9=-JtHn2w3713Rb3z)d~!P00XIScImgdxLYwh1cbnt?&7zkQ1mTB'
        b'0R)M}YHBLpYQH%ebi1BaP=WN+HkjRD2EYf>lMspsTxbX%idVKMoysA7m;%T~F&u;GVgAK{p`&&rDbn!17&GL)pCG~r(!2YYrAp6I'
        b'q$9$GchR!a?>C@i0{Vam^L8`8&wbvVp&HU9DION2)ZCt-7)lABu=K?#)D4t~Ub=CSC}<LKkUTEHM|a!|TxRlikR!oRv|#AvAhL58'
        b'V$e`DF;vuqGDygKGyYpcCa0iwVyK%K;`7~v^R@qvyL;HpO~L+`)nsxFg0asZ35G|Zj6pX(tbm+FH=&GvcS^V(pL%dgK4+V|`$sqB'
        b'$4%rzt?up~_afQ7a-Ozi$ag}*U%25zm{L(BYHxOTpKz~r5FEkh+v)E9Vl1D_Jw6{F;`2>L8J|M&N$uO*-ACM1BzGP^YX7sl`=hbU'
        b'Kk{)^?(PF_?(`TT;~O;h%?KsD`OTl)RJfbocT;iPSEFU%dpHB5Ts<~IppJM;$sOfM?{RnU;fv!w=EE)S?iM$95c_@SN`K|!Uw3!E'
        b'?&dxi7r&2>Z*+Gzy1Djo@g02ptM2Ys-Q3=B@o)3-weId(H}?kiTL_!dw2v<TjP`~xBeuCW$hPvFDk1DjZs!O~{_N)J$I+_e<2Spz'
        b'H@ms*<KnmR@s;lGN;mh?xcIGn{6=^8MmJ~UxqwdsZ6me7JTcYM<!{m43;a{y7*~#cd47|4j$`(fj<B^;0Sf`nondw#dR+Nb(o>J_'
        b'^E-M2XCBRI8sT%Tuz4!M6^!IN@+M*)bMr@Ub41=tYPT8C29lZP)>##Eq$BrK42X$z>sUqf8uu)gzQy<bL5_8s_yc$BzsX&(+6~&0'
        b'QWe*ctYhT99+T(h?>BYd;EpoT8x*G9&o+O^g|6CX*j-1885FckzLjd*DdO&RA8`vS?s0<wV=7bZu?I+zsXWV6LRTzvn@SAjuoPJ8'
        b'R@4*aU5d7S^nODaA*2ae8;w9!;J*aF=rag4hC^nBqn55S6a^vgrHf)J!^9biDNVtUsZ3XHQ*g;{{G_p|(N5#bC>68a#c$1kB`88N'
        b'{%!*|%Z*LS+5j0cM!Bw0j(45%m5ZOeY(!A1zf<cj-Xry1yC~8j<ecH&QKDt0yM4<RrIypWVV)@tqijSuzRmCrZ?XVUCfp4RGE?!h'
        b'vn<t);o|xLhIL0zbVDxCWf~$<aA&6+y&SBFzR_K7A#`>HaHfQS#p6TuJ8EyQnC#|+?zp;1OyF1+NeH8I^HA-~gmJMVh9|2~fSHXt'
        b'{ZO>jZQeK8OSIfZ+wpN1<LBlV$yg72uLI$}%v2#t)j)Ct7N143V+RyUI$VT;(up1!5?}H}1dzQ9e?3!(a%E_S&?f`<T>PSI><*{*'
        b'PD8KDGwu#&1DSi-Ga@tJyMWUg68`Y_VRC08bH^c8Lw$A1W!0jd!=`;l&z*EpA(3+kO77}9u(vDZ%^4HQ(x5)QlTnGR2p=%*TNd*6'
        b'k%fo~Y1`ZO*0L70eD7Q8;>iMgYKhENi*MTSW%W)+W-SVe7aa!je|0r${J%SR?x2gB{ON3hlDhWpv3E^=bGnF<CWA3#TXv)l4Cylo'
        b'EvawGU=3j1@5%fYSv5ktta_iWcMifAVU8?E7$;GQ?8`=Q68E^Ez2+QLGmpeqVthQw9riRk@OfL!3~xK}n5F{bR5zGOG`$+uiNXHd'
        b'tC(+;%8^*8*RR7Ig>+^{62nMYmMGpdq2&hP+>oa%JuM8M3O9!nKrr0x33>{0trDaKM8*1WFb$|VjHqUb+)JLIDnwaIZl&_mL?x5P'
        b'?xwZ`)T(L*JYC=Q-$7Xf2Zfep_#K(CJ8eBA;!1FRpa|T=Qy%VF9K`<bJq=`pKm^{J={TZhnon>1@#lTnJM78jH@h%jo*3cFS<jVx'
        b'p>Q)oug#adtMDadlRvZ{npiXBF+0S^w6*M6u|{@Wq%j{9g3v+zH^}&V!5r#f2`i(7<ZZ9g_Kf|8noFJyGF!$z!>b2YNz*28`aQui'
        b'idlJCYul&*DsRngh3f?g36!Krg$hnklE{toDOFSgzL;OlD0Xa`+#HDsnX`rVjNS_#i@}xwJrafI!CKbLC^RxWd1%&N_B$)~-aH(u'
        b'3)p*~&@d}N1slkkUQgHOwJcOwc2KCv;nR)k<)CV4911#s;?t`S=z4=tgP_w5eCKX-jozQ;!d=cVmsKJRT8^qUD17O6zCi}hqHlCD'
        b'p)RvP_^PE=kbC!cGi1kH)eZ^g@8bKoOWoV+!ASODC_MAKOqr)T2i2)Y#^gj-(?pk<zkO{^6!xZmXLS&i#8FZRp%FP3<ATc)Y9+Y~'
        b'zVpR3kiGAC$F-BBCQ}k)NukNK?qM?Xs90B0nE8Y_bE>G?Nw*U9PBuF=COfS+;Uv?4X{g>zgv2m$Z>KgpdZttAy$vGn+$E@HM>o;@'
        b'Zcl@_H|^xH)z$b}b2p)=H*w!z;u}$>W=>t2(r0`h^E2yZIydFy44D`tj&+jBmptBjesyV-U(A=6G$i*Wj;I?MC)^<%^vUSKasC72'
        b'{2z?@qYqt5B@5iTZ8Ucn$M!s<EZt_CCAZsWWu}Q*w8!M#`!2QbzvSG1skxf*Qn71mRS&sgR9Lm=(=Cm5MW029L#rWF(RPX7DX5iD'
        b'f#J5^1_AdD&Qi7#x_X<p>Xfhu8UtmglJTnN?kaE_YiMp4UwEOi^qF{@JT}2L6ktm|Chcy#)ZTQ-Sr28e;9kK=5>lxE;Ab6AbQchP'
        b'9{U=Exj#WqQG(<_-}sD&MkT%**dTmDkRQNp!HF#M3%-S^m=ZMzm&cm#7jiZnTdP{Cj_rNtRP#;`zGq*7<N7u!EjO&TJM79T3p6Z0'
        b'75*$wEx3q(mNf{u(o0@N!u>b)0Pn(o^7zb#UzWYzSN3NkWryLipByRsw(ypbve#av>>N!f{9T+M%9p-4e+m@8dZhUO8Y%vJZ}FfT'
        b'5;B%$Py$N5NI<6-8fO*iX3`1D%y*~9kdl0*BUVAp)UDh&N1U%Z_Hz4gE;T!*b6J=OHMNe=$I{D`XI8ULm^7CumlJtGA?=HC5{ylp'
        b'iBo08()Y@O4qUb<&Dqd<X-rTOn<@<2&RUpwRembv2Z9>6iR>&!8exI^xg4Bv4$c@K*dWGG(rmmnBsRgy&BBoyV$0&FsqsV_Ns&?W'
        b'XP=K+!rXo-KO?FzLA>SG<ugG^-2stzGq+u`WTc6ro?R}{WW<xqEtjIgAVX~DC!Y3cmu5dlskvJ)x%IN36;qs{mkQh*jl<mJOBzjP'
        b'qTI<|dQwvt=~Q2e@~f3a#r5X)wvr2W)R08&4WV*iDyu!;$kN!e`uq$(j=EGEA5vcz4<;<9z=XQ;8vM8mgW${QP*9Rp(Itj_1EqdB'
        b'lb~eyE|$)=(eb1rb3j<O1T@A0kA|Uw)|2uGIuF0aNM`-FNT=CI=P5EzUC7)OVA9a~utJ(%SGIOd{6?K_UFMP>yWNBB?m=hYV6)>*'
        b'?mR9jUnxHBY5xf#LaSjVG%(0pEkW9e&vi6V1@4Y)G4~CQvqbO9&X;5!k)%nSrw1*DRV$-}C4qH!JuI|D*Dix*ENh^+FL27BZ^X_|'
        b'27x)B@%c!@;Xyo5pQ(+nK0s9G3$Orwj30G$2I3<2XLEn$Qzq}rHf>XMtuV#X3CVM0Fja5|c!Ix2(7!eBdh!{IAvHS0vLGo9ShGmn'
        b'x!d!EGWkmnNa_xpu=6|56U-vNhy9ZGz~I!cqd`jIiJ(F(x!g-QMOiKk=`Fl(CJg1jc!G9++Ta)drl<2B$g!RTk?cGVKGrGf?BjpQ'
        b'<V>$VY=wv9mIeC+@>kpH6<vFd21K+5gi1b*7YE%d#sf0qU@oQ2JN}bJ9=|{%u>@;WeKuw05>aW11AiL_ce^Hdx<KcZfc#)@MCi{V'
        b'teVM8<)E%!N!t~UIvih}KY9OypZ$R%lTUdX{EthDzVT3M@KZPTFC?f5rTqA{Lc&35k4aeY$3q%r&yNcF2b}j?Df~GtEoi2HP(T-$'
        b'p2v|TIMOniS<e?^!K(m>sGD5W>uo1~w~GwQ6>CI^?@RJY?orIG0ypqD7yC3S=bFJjtJ1MeVF}XO<L}`0M_xcY5Q&G;IY`GU9I=>W'
        b'0@f-TOLWYjw}nv_E@zORej0>tCvr=$A6s3l!=%MY<0Xt{Ty6=@Es35wl3P;rqX%)xIG6amPxr#G2;M5w*$VZwg$_GClt7nkJad|Q'
        b'u0dGyHgQnKqjIF;9Nl*e`rc#!>ummDag{#|=J~wL{N$;2l0Mt5cMsvSBb+EETMU{n#(@%u-ZzLjva&$^tose|gVYUBn^a+1#v;%r'
        b'lw_-ft}M(aiYNQUy)4uSi>?1<xMdJ?Sa_zx5DBUEceHIK^_7L?`gL6w3{ivnyW19##*{+6aa~XivSk$8NxxMjGiC6BFnp7=n;C3p'
        b'2AwPn$Yq?A*99cOstBtSY4c!6KTt<9lLjfVjj$Ui=>{oXTv!?W2a6%D_OTYBSx&GagsFxpW##ADjvM=K*|oZ!4rg|-OHFM_S^GDh'
        b'l^&ON;+OJ5G<11V6i1Qek%e^mx{%{ttNJW$rpm&yCqth9CMe{rgz~p=#XFBs{-?8><>)feBZ8g_$rFDChTG?w$Zg-4K5BzWaE5e2'
        b'Qc<hNYbQ{(kuA#Z3j^&J2AZ8BXWsz#*+35u*Uj_|l(II`qQW;}&4#!Zs{8Cf`*)B`oP5!PKxJ3O;tm(^>qQ>P0?ZMi-l4B3I3Mx8'
        b'j8dUVdKivu2R;h5`7vJ%Py#wi5mzmdvjr9tONX#;C;p+NykwWDkSQ%XNHz#5c?n}za-ZNTSeRz~Szfw26^weDlGd~t+4)+#-H*Pz'
        b'4OHufQ<DT(7A<~S`yVtW&8~w|I*e%mk<mtABA*f5dzef!$rDLLM+pmaD15%wQi3Vil;R&fypCuP)coiv7>sxy)HSZL#VNO-K>X{d'
        b'RdBEKRS{EUeQllC;<o~F^Kw_wI6z5SrPYp)A1hVvlSXcl90HZ`oF;fmUx?*7JF{b;a|oXYm*0;L-H)=q7jQKL88ri6)eM*((|y;='
        b'Z68=gd=qbIG7lUi8bn@j?eNPUo8f52>Fio!#|_80Ed$gIrKObIw0mQtY2A*XsX@VHw{4)^Hqh*N%4r+meuwMUAm$z!Fi`>3y{L`='
        b'4VXWPl4U)$vAEK|yL_O11El?f_yP>RwT|HjcFViV2HGtUR{*UK$y+t)(5V0gjo1JAFgg1@Aq3yr9JJ<sWcps95k&@5-P}Ms2N_=K'
        b'JmEo_Npd!7(y<uk?tv)LnvtyKrvg@isl3?XiG1VR?#Bn(ABFVWJCE>o97Q^RKhU&p;2_Cm;p+OWo&aN<><v3f-HsQ_Q71##*}=uu'
        b'qtu>W@;gf2t2s%{3dg>1@X2Zj@YO_~q}06#KaDs^X>+kJ7kue8o^Ro4_(^I-IQE5uZ*}f4_;RP7q@L=%3_e^?X*l+UgRiP)2<Ko='
        b'QuV!V{FFI4vX-aUf#Ptc4m70=929W3dh04~5R`S~hMx?Hg*tBR!D+*zP8PYndY4*A$*VggTqsUV*-A)CV@{NWYD!eTcRu3=xVV9F'
        b'?|jA%a5Kk+d-2Wy-Uk@=@M9?Y=7Fw6N{01WgCKX)H+1^_pa6xOmZv|NUzNZj<IEHKlEO0@E^HwEK#Rl{Y|*?$$h%r)4X_k5XOrP?'
        b'e3M!4*0XKmGoUAlqVM^BV5SVPB<f1!{-+<?KWa>p+0(zJirL*Cp$=qJ0}<K@`0p$UGjSj<on#aPBQ|UJkf&l<KO-A(*xPnAiz=uA'
        b'=(#3pz)@`g({e{l04$%{B?B`gJ7PkinxrYJa7tf~S=rd3D=h&5*)MsHEdrH+51RJ81rbN(ZOyvfQwSI-ES?!KFXfb$8|>#Nn`0}u'
        b'bN$q0YbwgU;Ni~no9f%lPN74y(Z@HisJWT_O=tTZwQV)c-@rn!+`D%9uHUz)_pQ;t>5o3$59QU8OmDwq`y2d<os#HSh2E;9Uw^|9'
        b'MK@Y$N?l%BXewVfN8YucJKk?H>l!Vzsj9Fnjk%#eI;fxTBg4^tpCw+73xVNb+8~VnxF1i_g(eDg7eC{1rTA&j_ky0Y!uEsxkuOa-'
        b'E@<A47P`V+y<5Kf>cjr-5Br-w?C)?q!hMKSo+Z2A?}r5U$U6HyBXU6no983$y?#n+kys>M@%*Mvtt3)SRZE0j>gxH(qJd@7R!Q<@'
        b'Z{P0ehsDkwOb>qF^8L2pU#7WVLt0?k>jK4uz#xa5Ls;)cH}!j0cK7hf>M(^mU(Q#2zdP`+p}Joq)R0}(FflLb_X)3=6n34iCAn%G'
        b'0lyCX%d%u<;&6B(kvJ743MD~z5s)PrKcQB0HeT#>_^<wZfqs#&+Od**k$<SxS8wF3*b7DyZjYg~pSNCa#c>(telUddMVUcVs2ogy'
        b'=W%46sOxh`a0_3oli$c|FYM1*4Q4tKlP>x2yW`?k@$B@P6TJ`1w#dF(-`~ByziB<N{RsCkUuJ#oj+4wo{nV89C;MCdp{-B)+MJJn'
        b'<3*N$#(hdtS6fe)vb3v#q^7iWDJePki1#TqXITIh()hm8$fsD*)!3zkysO63fZwJ3uaFb*MUq9Ic%p)s|LTuPmcYY1eTnY#lFSci'
        b'>{Mp)<W_fKU5oWWs;`fJx`;bsUjH&-*ZaWJa~Jt$<Ik0J<#3C=Lf=X>km1KXum<}a<CmTGrXj`s9_mA2n;xgi{EoM)zw$mKU=FYe'
        b'LD<rT7HO1hx%Sv#^(s{DK-^rMc!z2V<hz~sT6I*2Sco=AZJNvyPo1U{kLG63m$&rSe0VBIO?-88fA`J(P2v3=&L}RB?-l};sltzV'
        b'pf2xU<lCS8k;nVq9HWAE;WcV2e!xllLC9Nx6?;e9#f4%Ltwi|$c)AY2lQ+CiL`8!hzP@H49-Mm!?-9M`CC(d|SU0#llxpOC4@G~5'
        b'qCY)x14*e;-oTsp2LJx-3H|A*)TER*2})#SX}=Q_8CkzU(y!G-zAn`KKIpLjvci{dC6jMOsrNJD{`}t`N>Xa4mL)S}KRwlSLW9bV'
        b'L<Bwg$l%3@2nkn!3xDLNi-!dgt3cQwnO;W8Q@7cbhqKYQ47cf`7o&hVobGQ^ek-%4Pp}Fio>VW_rmff@d;6`dyXnjtw?@FGQ<~VQ'
        b'R8}yxEQWOmqVicmc-dM_J~bZ<>8SkB0E&!zQ9uPG*q~vLe0H(uYiMhB&&6eA%MxSeVfY{NV9%S%)qC6aDsx_){J^vc&d)A7UTJQ8'
        b'C))8c(^%DJv>&#nQW}-`6u)0obk@r&n~HnyBBd&}Pk=5m#hSQ-7vowmn`l}%qC>rV+F+TC+taRi5AQcvq?u26M)p3rwu?PUN~3X|'
        b'e!fX(X-nA{Vrab>;~?-dX(eLzUhJC0?7_Jb@Mcu4V3rN9V5AFTi!ONUQseS)yDnDjyg0Iuh?45{>!@I6=f%vah<Odim-uiD@LuW='
        b'21*DY@HEw3Jcv!t%ZQRh+C<z9nCCq<Wz|NTv@0RRB6fLvd#&M@5ckqWeEhKuYPe$~XpI(cJ>G(Ph<$T9bQ-7|eszbq7cW{Je&CM*'
        b'e+jOEUBX!|Qj>XK?vEq;`rLCDDXFex<4FBtl7!UA{$gz+MVYl~yh}T}-#miH5Ro{!f3Yk=C5&JRJ}$!SpVxeWN=zQ|AS$L4M0s(M'
        b'Z*R}qVWvVTS@|o44#&DPpIdi6U1f#9R@oVKb;lZrqt0xQ?|55b?#KcYp>Z1hriLt!qBoEx+?P}^o+>b%kv<%$!$|nb-wovSCn>Tx'
        b'A!&MAWjraKib6{&gJX&ln7kJJ-b$#nI6+KZstmqqN?+*Y%HZ2VqbhAbQD$r!h1OLDM^wh&XWsW!f9jW%s;J*%bv#=cd;xOLhJ1?Y'
        b'-&VGKWZw5_e`-6G2ucW99nVzS-k{Ed#R7gyW$+ut2@|Z2qRQaOR!4DV@X^j*An|-<u*m9oLEP)1Vv4@<P;7FK&kp+x!(_n15~=vB'
        b'QKk!H=X;c<?5BtTH5Cw(h|GxuCBT=Wz>gycb0ToT3;_u|ib*6p-TeF$n&{=thLL$wZY#GaLRj(8&v^(ls{owD#I||+HQ1cQGuHPE'
        b'3@$U63i#=0`m4ohRF>co8kT?%OG$vYe9c<R??>awevQZ?fQN$7a}UTDz>-3<L^wtdr=u)_LwE#4O&&{*pB30ltU}IWOOh@r9OF?n'
        b'iL3$w)rTQ_Sb1q16$)#PxAD7Al~p1Zma_BFIDYzU+Y$M(HRDqZ)<FcNp&ltn_&D8x`4<^{v&|BbAnH$3=S_~VrBbAIzw6Dk$+Z$q'
        b'ZT&X>6rhtt5z9}$xm*&lN)++r-ypXpHDd8iZ!V@HtWs)MoQk5z&PyJR4S3f%fPYm8CLoPXL&C}ipBr_2)E^IeYr2mI=8k@_dRT{O'
        b'geQrV%Dm6>X8aYp?H`Q=P0Y{Z3(ou6egzNM?dWIYdgS>p%28eYx!HQ3$wog`qLN!mtE*-E;;O_Z-8u|_GN-S|H*T-2<7ipF-z)1j'
        b'8pfZ?_Q~XxX|JSZBdOpBsnn(d6W(qrH*fTv<Jia+0VUZzIc%TmXaJ=;^lIB2i6drXgW!-IeC074+xE8UsuYdpjpd{GG_*M^#6qbl'
        b'DHzh)D4Kq80qd=Uq_nzpmrd3pUtnpp>+G_;+Os3|s0G`+xN4$JwL#WZVqqzj$y!)$TIUr$c;1EE7N-Jh6l_>Z)j4wBW@gnki<zBd'
        b'DruV)Z)StaV^0+CQtO^Iz&v1PCsV2_3;yUZ>x`Gsu{0=iA3rQ4j1O{bd|0Zj9h$ObwUXkEqB<##-zwQ412v4th)SHkaRXUSU#P5?'
        b'vcV#4QhKb8zTiE#RFPJd*c98QGhK+Qlf<Y*Fu{Npf@#9MSmNa^-WOEixx}iHI2;$s%P+u4gEW<UBvzHEoKMfHNE3ViXnHfBo>fWU'
        b'5lvs9Ep4NVD{p<TO0yY=@MKw)h~~+frnS+yrdQSTXpL8PuQd;hjs>4wv1}lpKEW5(u|!0G?A7@ZVakYDHN;T@-3g<PM*JKWtIIJW'
        b'@WUiVg^4eDsGoch{roqnNDYk3CqPB{G<S*jyt7tiBYR4fvn=L)fp}M?gx^=B;)~DUKm{MuV%9{>G?@Y;g8d>i!aT6YQ%m?suE@I{'
        b'!a8+SCtopc?tvb^QvNLhTR_=SdvMveB~lA3x0HaWB0HJv_LQhb>;j9bOp*|6Q9)%TB>@&PLDeNmAmiDP*aUWzPE4)FBC}{l7ok7X'
        b'C2U9Fh(3zZ#E<3Cq+ZEuOMop5>Z5`BOulA)enlFnDOsW_8Li()*y`|n$c7$$%p$Opcv${g9?<kUa|ix9AT=4R3oCv{mhJcwCX>>_'
        b'at-b9VN_%zvtxaMD=t1&S3XlW)6i#E_QWcw_*u<pvL4ks3kDq)UG0N7kmPh&6#7)Unhi{QFpX$oQ)SH`(y4b*iw+XHy`~-^D$`Pe'
        b'gc#r5`IKD`<v9MBa$BA}N&mWmii?|?qkqw$cg*auEBoq|RaT_dqhja2RR#T~B3+wBfx|UW23@i$B|wz5(v-E*@IVNSKc;B5<U^??'
        b'giU5)ZOhI3Xk2DviwWkiuBYTlt>VsaJOwUXFeMw&!O*UQLfo<-$lAhcWR0=Pn0NJ>#OeNxyG*_lZ63F4{RR-SxP(yMR0F=;Zm~#o'
        b'x|w~kN+i&mbQL;XV1jT&2dT<}WAcfsi`B2}murt%?^Hjc$FJ1)=8k+y+GU>7hgC=-3So<_7dm}3%^mBm`K-)pcJ!2*K>&)a#8`?^'
        b'eQb5~R9Rv2mlfL;R05R>rm;Ea);SWsT&%QG5g6u!{8&wN98FJz<(m{Oo0=b3Btqs%;x{$^=0EvGNc<W^Jp$xl>BaBo%kz%hHk>NV'
        b'TzA=9cgVM%#5s#(h|k)IFZJ@76?|q{t7y#*dVGE{&Og<czbi%~3~Cl_AZJLdBvhwC&?!J6^}Fq|%r}Nh@Ha=3C!%H<%G^BMwaPA>'
        b'A;n;QA+}}-IxcMxbjZ*Ln*+->%k7jPCJo`+f5+vY3GsUfA@v)ina3_CU+}Iws43o4jNU=ds7^2o&^_N)28%;BQi37^P1|S|5L5sq'
        b'uXduxO2vCRViuy1y_8y4-zI-6C|Cr>{q&FSIW8vA1}Yh$=|{K9OPi|~pbjYtc`Ghd_G#$NnX`wB@EJjelsM6~E$Fq&#nV3xIX%s8'
        b'db{nLR|zWQvFF4gmeP*ug{bqKr&T&b&X1>1NeN>iDUl_ApRj>kPApe0k3LSc;+ruVC6$lC=0th<A`KBWww}>P;8`f&CsbFnqZoX}'
        b'yqt0AbS^q(b)&(h6S#WxF1=uNW3(%4iHoLJ>yS&A<<hNj(W2G*oYlJdE_&T+q+3lVug;2e(Sp@$)~#-1T#ZT>QmoF3bM=v~9t>6U'
        b')ClGe%*Rf$EXQWX*i_Pyac9PHc!N))iW2ZLpN$TZ2}GI_pN~Bxx7;)PC)O#53nr7bNJAYZ237H7-=CG109T!(UYT|e-sPumJal3s'
        b'o^WIj{nYk@QpYNKyr)^RR^gc$;5ngH#q4Zj9S+?O3LIRm($?ejT1bl1X<c^BLjH&?bFq*=APlAgbaqU`>N_zEF8Eq!S9l}3=70=~'
        b'QH;Ye3m>W3G>y8uns>G}zNOIZ#d+S+@FNW7zkrcrH9iO=yyZ!P4!Ze+NmXMxpR-v}&gX2-S0$hJ@M~Xa|Jz#2irH>x{_fx?jclLF'
        b'LiTM@T7nPQHR({<w^meHj={v>sPa|ft#M^z(#<}K6q(H1Ltfiny1-)HH)NA$Ch$UFolI1*-sd{&`SKT{v0d|mNXH)5YDV@pub7Yf'
        b'V`P+tTJBqqP?COgf2ai84)|VHl5$qk20@C=r#EUPI$K+nwGK*!WxWqmYtK1KkShDIsUwg`h)!S<lrh;TH(_{@%=!Ac=bDzuIwlb{'
        b'@xu?xoXzJJKrkzbhM3&A;d^Dy*Ul-LXtNd>AugB*zirr&M8^gCdC4RY@zD#VI#>h=L^{)5CR0`_qi<YSDHQ4Tcj+6mQk5|dlisl|'
        b'4o9riJF;v<dE2@;si?esWqDgxqT{3V1#HKep4m!0Yd#Qbc=4Ro(OG4KsW3gZr$jj`1}HM+=X%nWz@+*ltp!?}Zb{rJPLHL|Cpr{y'
        b'Es_wn$|6t7oawt~gs7X3PoO4J$Ec8M$HQFvIlS>TcYM^_ILh#ca~TEa@ae2DTYk<Mi-jaXXn5irt$P%_%Y>#_BI|C2(R*eq<fF15'
        b'fv4*r))A{5d0=?>T*mLbbgHWn(BU3D=NQWrFUiP1m-rffFz)!*24bqWE4<=v_r{$2?YXap`ugmOp7F8Wzd6_bn{$U?82DnjW#{+@'
        b'M!Ui>KH)fW6&W~5i`2MR;qVR)d@^1u)z>R@_57K*lz-m0SJ5-}yhVCwucB>SdP%FGuU^sP&EYL1^yzUmp(ap^sCzI&^LZXGY88Y&'
        b'O-(rHkE8DAd3?*c44s!Z(Ef~@&y6x|`nhk;lSNB_r<4E$t+`#%AWSgiDu&~#$f8*&!9c0GC76Ww?;IJWjR=s(ygOX&AQn52u4ZGi'
        b'V<orf9DlF5Y2Zialyg)7mwt}F#M1a1noGsr`W<!L<Fg1#&_L|Dn@i&9@qej_XD1$?cyJ<?hiopMkD5T;bbP|W39S<$YDFv;%SVc+'
        b'+o&7PijIp8id+3~+FNn-W!Z7@LGf8{)FmgU!;y6r+%)_<=-gLvT(m*d_vyyA;*G@{WO28*?%pW0aK*FUXdt)<p011w#lPYJ6mN(K'
        b'AdBAhI8XOcWvxUw8r~x7KGoO$O`r3dzGlZcZf+kWJWrsrGHN~bP^$pfLe3NU-DLrY^*!DwKOE&e)<+4J$(q}PfvE}E2^qQW%lX24'
        b'WgS7l;=l%BuIsX+hK^GU@Uzs6{;7)iY~X7|ApRmlKYvW`Z0y6D0(u0i3PS=BK5!YdL_=RI!E1@|{>zT-JPCMaF__BNJ&-Rl!N@Pq'
        b'Y9ShR>mGkl)Y!PPQO6H$I}BmNpZj{YDPb7Ts)r$*Zt1C4X6)*#w@?>C1&<Yqi*FT#Bvo0U*wA;E$yy000#sA)kC)42K%aOuHM+j<'
        b'_F8@Y{dIzAmgw3(z2*KAL2t9i@N!?BuvQS>?1`@Fs}n?T@1qu-7odaw(2@Ko@4$SE-qJ@+fM}4^hrH3PIJ$W4Zw$7+g44WcntWqF'
        b'`cHin9<pfy!^Xa!Ju#GD5#De`xYQRe#NiTQ<#{ssS!5{c%ecR9MEd!J^lTBmK%`5eqfLE&D@pNlSYM|KGS>GQlN8>fGy5_MyqUPi'
        b'`$qEdisXZ}WRV#e9_!P4V<miSVuR=B;hj%I*zn(dqfx?)hx@pPe@-hS_DAFRTp4+N<HN#&nx7@#ah??a4jKL*_U=8fs_H-#{>e!Q'
        b'5ROhB$U|a#5+nx2JBMI3v34ejh~T58v>-Y&y?}*cr=3yj*V-9wn*<*Rr85C+O{h*!XsJM@LhJ)krU_a^2$+CM?A0l?W$LR+t5&pX'
        b'?%w;H@UWekJKy*H`TP9=*?X_O*4nT2*pGFt2$D`VoPB)MA3wb0-;WlaR|LI)X!g9^oaVm`_x6fehZ|-^+cdoS<Ab>$9!1=+`_<!e'
        b'KYiHbOAe>9dm@T|c*Dhm`O1brep81xG`ugezc_s2@(;gndF}g_f9UA)72^*#-uLrp?(wS(|J>^*Og5Z)bdAYXhYtjY`K(y<a>tSz'
        b'>a)#^{Orp;A2>YN?8r`!IyybM_;ACJsHu`)pKYk*PcAy#F!ID%6(zw{7(EB5__M=HUdufZ$et{(y&BZSJH9XwYj`8rdCB7r{hHW`'
        b'(?QKUB{^-$K*OuyUf$6fGzOwn5;q0u+_FE{59!E1oEW~Rs53L<i?^SWE;?h(sGhc<tGN2EiO~lj<JvFX5WYS3&Op#AnwIO^be#6;'
        b'!ml4XZd~KnUJVP^-@Tf9@)^#{KKxzr%B$b49@6}WSAr$c<B(A|4y;}As|lyQ*Ze{l`j#VMJ808O`J1*Cv}E!sGqFw8OOu_+isxS4'
        b'7+*N%(28HY8s5nm9t%3uqiP4T0mBa4re#Yv#+$YzCsZ7ou=-HN)2~*>W6QU9^uK!O-FKH?(){x<!NiEfRSVA!O4MKMf3<J_tJ^dG'
        b'xOxAp&F4mW{b=~_^0yCt_`T&DezEt}zTLs%mT7Megf9zT94;GmYTktN-y5|x_KTgb_B|3TUAE)ZfrU433kvT?j%{ai?2jyY>Ad<+'
        b'PL0JXGkH-vapJIx8gu=r>&|?-yZY$`_Z_~rr)zu9pUvwj?po6|>-z;WuWAaK6`voH81|XYd3C4MWV+7(P~An7ryQ8^^|~RGKk#(p'
        b'_aC`rL*0ZW`KjBA6G6SRao9B<YX0-5f?Ry9XvOHKJ4Qc!N#(U0y8iLYt*!G~?<{WJ&~@8}=@+e8SRR~q7k7^8D}K7W`00+4r#myR'
        b'Ec{-)Wm;_9q8+~)Xxu(7bx!d$@oP%!D$gD=c-%5q$C5AQC(kZ8*iuqad>}FQw#u-#5cOr6Ki{8wce*)tcmBMqV?EpZ-s$gtr@!Of'
        b'{>vU*yEZ=a>R45Ny!XZYYhTK5c&q;xZ}tE7-=Ca3uD|}`)Qivk`X{F^8eaUhp{Yb!%X6`1dAE-IUHCol@iYE19JpoC@Kg5Wh26m~'
        b'=QSVhkG_ezb>z#p{8=nJw|)N84KIBBt?PoN&u5pm&F^n`{^LikyY-H7O)uv6rn_!^VCBr{#hZ<V&Gr4!qt6``vB^*MC&r#%+ZZ$;'
        b'W~{1D-EiyZl2N~m_3i8L?&<I7>F><^!`k+EV`W}&9$ue`)!(@EygN_s+uh&&)BcX1221~O?Va(O%zGE#e{$cW{oOz5@8}9<E?M}E'
        b'__(PvO0&sjAKFju>JOW#Q>ydFRZh%bRGOH)t^bk>uPMk5YJ7I?Ugw<WVtpI?ySMard_Rb1^`RB<V9&R{l%I~@I<}<m2mRfh{T=rN'
        b'Oa3MN&Zae<E*+6xR@&3nyz{`a_>Ljbr_PyyTRTtg+tA;APk+Z<LD284{aQQ|Wh98F_3na-f9Vgd<krfjmde<7$CS0~99S0b*;28('
        b'fAz|B!<*keaP&R+jqwSW{2^*T=jB!0*?-wXmGjFgz7fP2EAB|v%pX}f|CHwQ!_%#@`?8wuxf}C3D`S=03!48a+_&egJRF3YFznsI'
        b'`_mI@-p%!6M$EqIlS>|{pIscDz_XVOYnokr<<a--oBE??ge#}Vjy{WSZVn?1mK^<eUnbUl_mi8y*x&KR{(bXf@1B(Sz}io~S9R)1'
        b'eP8JB{z8Ap4gG&TZo*dv<6LpsQypJ?s{7KXR<GQ!COC|DJ```s#5QkzDrl!{?M#gM@k4ouVckD^sxy;!&qMKG^TKynnr@g=9UFCJ'
        b'd~^F#!7BGW7_Jh2d3H&E$K)qh2i?8AGq#5J@miy>(UZd5w+%-I$8Vqi?Wfj!H#YA_$%UP7{Y}xf!ZjUp4{d&{=VyI0`@3fbyK#HR'
        b'CH;rK5bs&r_tF0D%YqpX?|6G)ef-M&S>KIanTzkbl}~;A&!4>Z$H|#%lM}xG*5`|Y=4Hp+g&V_Y{-VFTK3MC;j@tf(e;@DpQQrmq'
        b'-4_HiUJ9a#t&d-me`WTb@LjV~&1I>1M{gCUf-KJqpOdAU$_BrGNdCGkcmMd{(vtJj2hT6rFr_ViFkP}~N-!DSMs6EZQPp2x|3tFA'
        b'xIWw3ACt}Ff3{9-#WhdX*B2zG<{ewDcJTS`f4W{GNb8QS|NeRd2ZHtHO)dGa)(ch&R?V$fJFGmO%vF>B<$kEGyf+r4abf~N+1LDw'
        b'1Dl^auxx(w!2^lm%dRV5x2&Oj`m&EFb}p+()GnKxs18SQtn4_mBK+`Y-GX4vog<=wrn@$T&4BeI`WvHplTHoCso2obmF;DX=$P>2'
        b'&dRVeR@Bv=+7#XVXfKLBpK2@09?{?=4BMEw@qwFva^PTP$+C*(e?8FguLpvJcP`62Gt5FsTQ-^{M_SvCMzrFjC!@I54Ns<1nRL`x'
        b'9iDqn^FU&CR6S?1@egmlH`ubMpLg_qhI<Yyc`+AeaMkEK{`P_TuQy~nryU16Iu1ltUNZT~4Qs-idd)XK5xzQg_kqNi+{+2!I;#&v'
        b'9m=Y)Z?0%NkT`X)Q`$CcQQez^<-@82xpxQ#pP@XL7?a3P)-Da7`DN?g`cEWh&K%kEMrWpNPr=sCjrq-=eIhE<KK$u<3mSs%+l(tl'
        b'{kG+&r-$$9x3u1Hb(sC?jrn_qZp&+LSeDoPsW9|EOu2Sy*SOhj4cX_U>C&hbyFUD6WqoycKd1Wq#Mr@`Md#;cOzL{yjLVLnv3_T`'
        b'_jh)`@?>BBQ@KuccGho-dXJy%yX=W2uZA7(+?@XOmdeA=7H@iC)xl@OU{9x`nIj(jNYSRcRZIRYd>(Lr$H5@PwkVcx@s`Hl&Iots'
        b'1GSy;lf&S1N4#|K;MB}3c|lCMXy%6Vr$>=Ici&Hf^)vUE<f53~89ymnx@q;&%KN^We73kXs59=4PWNyhw9T!kIWXeEO`E0$m%-r&'
        b'^Kv)6!WgToyS9fDk5xzIU~{nVmV7zPQT4pc>+}A8Nb7^ey^Bib{cRZLns8Sxu3mBS6WyPBqIJ>nvmShMaC$*zV8th%IPcu}v`<B^'
        b'+fGlVZpba0o+u3e3s1DRhWV?X>}oGg)kT+aIIFf{-jw4e!oL=Wf6ZM{aA3rzXD-TXol+cxNQ7Uj)Xn|;h(uZa)vH!q@WkbXQ8GcH'
        b')w-y-ep(pCjOi=miH5o-!tI-W)s-_pyfkRrr>5kkYN7<fT~a-_=Dsk06T>%ms`Ez74w_jrXWlS#Rv6;S?99o(*&l|8cGL7+>pxm|'
        b'`sDFX96wz>`Prw!iHc}p_*eKTSan4%Of<V>@{>>Hrb`x`8NcP+*pJSvUvx=)T2<`#mxRA;RCQH++Bs3{zGCv!Cvvwyqg5*|%Rhdy'
        b'WOC2`+;ldX@UQA<NtB~Rwx1F1`PWa}^OM8ble-obr_PObL^xeLdH(bJgWg{B?{RYrzm@B2R7_4jG41CAxxXLUe?rbCy)S3q-hWH~'
        b'(e*a(-|^-^Z0(zQ;dMUu!s(^YRSxMaD_W30YV^YRbK?u=#<%C^&wb<B!j18RLt@wG=g%4+)a_M|4r{q@AT~4{VE@`{=fy_X$7Xjl'
        b'&5n-C$XWUEIbSb`%Ap&l&bxW(il6LnYAR^`QgJGs*K})C?oADseR9O2;J+`2JLJZamiuD!=H1ZrrQ&&?iS|Y~cX9a7HJ@CNpO+Zg'
        b'drL`TY}1`fJ2vi*;+@%^m-$k0>zBg7U!Hnb+ltRTH6px9Z@eM=h<)KxL2|jYZusymiJ{MrZ)$0HcId75gyTPiQBUoiU6L4c-KX}?'
        b'{Myp`bl$a#ikq^BVd`C9zwVPyjhGz<y5ZW{#n;VxDp)vkPPA<|WN%P@^r?B-ZOz`W{L&k5X6KLGzcD_zWL9Nt)`a3<pKZ^NFaPT;'
        b'Q#KYX{N6xx!#Odd^&3}jJ9*FWjd@S!Eo*51_|w<DFu(bf{o!xCK6-lF#}95O*^>AC{0-j;um3Y!7j><EW!#tguS+-F@_4Q<xwv#='
        b'R9Q_6noz&~a(J<|R1Imm{i2qgc}tdsU+)dC+BtN|Tj4Jjw617snip1+Hx1TlqY}e=Z!SrUYkFX5!w2?9(bPYfSKnT|DO>kWyK76s'
        b'$n4HsSv9miUEEOeRDJX*e3;In@Dcy?!se5nYML5d#^FiZSQY!y>%Y(b(Y$|Oc1h!+*z}^t(~H9gr~l8MAwid-aN#!xj=nF{RvJ}u'
        b'w;p-(eebd4{;!Uf#}lPZ=^@GLR8;PL_=d!gYp-v(d&rk2<ehdnF>T(builowr*LE5%K5RC^9!0E*%$1?mY<Fc>Y;Uc(I->utLIJa'
        b'`s|db+6mw7K3bPOxu>9W``n-=`|-X%QIn1Qk7}}e_r0$si`vscdAua7@T=#whUIZk7zYiIdD+HBw(#xPuy1>2Aai_q+;PPdo8Q<s'
        b'I4hNTef}%^&buH!?aJ`{tX-VD&=+TKP=uH6;)+d+igV$^>Dr3<HBaP%Wv8>{ZaOh)`y&TG68^pJNY}YbW25S04|gotp9&g9**t|G'
        b'7_Gap`@p^t=ggau*A?Bcj>50MvHslfdDFVZ$qVx)@7))yQh!Nwm=~{!CnoRN7Zw_euexgHk5&ccWGbkoqDL_ggq1+`jWzdm<;v(!'
        b'=E~?Bqwte&+Shn*ELX5b^~Ji12lwS}@vMusHkqA>;%S@wr6+UudD^nI-_a@{7f19aXLar1Q>V(swb{Dh@Au_Oy1Yeo@xqC*-_Q7)'
        b'&$P!2ld&I7j8ChMWdqHBGFWTJ*gv(GvxUy&ukAawqqDP8i;5>N+m|{vtG1-@JHfH9y7H7CT{-!({Hg~&R$h8WdpOocI6T6dT-{WB'
        b'G(XXFR0j+`cMcYJ?VtAMK<@9lC#StW`1fV|ru}vxx4p-$Ub7~4!t~K{Jv-UDGP->8ru`}x&wpp-^5Z9iT{~|<IJIDL?T+4DnUfCc'
        b'hUaGmRl}^HYFM22{MG5OW=J1-c1ZLqTIsT|Y#F&SKmN{)#F&}OmUc9TCrjI>gQ7pv9u@sj0kZ7V;U#s$h}kRe>k7`3ps<=bH(RuB'
        b'4~qFA;lfY%-c^z~b@P;ct!tOg+>o~^90WbP>eq%`F}7gDl{1^}2+P|$R^A(Hon4%(cJA0RzWzJOwc7?-^24%m?x%axC5hodJcs(4'
        b')-SCO;+b8X$p-!OonwXso%E*GFq&DX7q#3Q3wq40H%A5Br;DPQvF3m6+ZfNqT`)KP{<8eRf!sS2xw1ID=+`$6i3;MdfSfTZ5k1OT'
        b')ca&m(sn=6*SlqDP{?*2Eo2wnJ?z%ghP3R-Wum33sPo>Smt34JqgxggMKfb7?(WN#+J)(&mg?g0UfN(;djIid>E?T%h>FvV@lCm&'
        b'MS8)|=ZB`_*_8(0^(kHQzr$=D34&!iD`82{cH`zJ`-17scRi8IU3l5HE#CaCzTEWU6(8$s&0e8nvR6uV)Qgxrw{P%iSnYzLzZ_Om'
        b'8LJszd@%pNOz(jxy{7l2xAa(gQ;w#WP3Zb3j!$T4ZTy6E7MCu0I^6u<Z!B!hcACP<DE-A1-|E{lBy0~XdSY9CZbyDGI#??f5AN7S'
        b'&13qSrWQBdoR_Q6MuipJqUM$1+;Do)!nT3tE1rm|z2J<<)q2z8*{Ut~-c0s2?Y3~Bk<Bmc>nYnjb8uURrHc|rk3v|#E#H>EW_x+_'
        b'*uG%Sgn4;U|MKtp*4&#PJ&mtQjEk<~Ft)tl!YRKb_xv$CCwfd@6~4AoUA1XL_5<IlXvOMHxu^QoxjyTa$KqV_(*J#&#V5vDd@Rm}'
        b'SWRW#noRW4%++DFzkYn!3EAIPnHaODXvuF{cdk12Y;%9KXhi$vMXl3UEqNwvf!xv2^<Z)9H=~rJc1PpBdp{UXd}3wPq1tlch{w9R'
        b'rf%vfITp=@;ry$kNVebilVJVK9VNLau3i~Gsq?<Cw%)chtgx<bO_v0jZ@Miys8PLr;pd7*v<IE&*4C-5ZP6+hrWb6C4_%x(^!z}2'
        b'K}AX5=*9md47hK__j+?@Ls({2jz9BrwN2TY<?1t|i|o*g1JQTgv25_A`+}2d+G_*HwPT{s53=Wc)X%Q0J|(<_t0yLtrw2t~Vt8`('
        b'((nzibVt*~qu(yHWy7{iJR@7ewOn&X_8r&K#F>9;e#ejZH~%o&bw!&$wr^QHcZwBtT-vw!-+QC^gEt|fv$5l6y@OA$qxVnR;^Dv*'
        b'%cAV%b*$^n<USpb>VPo^u79&PTzvbK-YF$fn3BzR?LWUgdL|Q{9wnQm6yFoRWp#GZj<<64LjCd&b<HkW7Y~Z@@^mWQl_-zyh=d1x'
        b'dB>8snvUIIIcrs4dVg<w$?EVH$d<a^*~NX|*jMxL$lz$t%pUE!uBqYcdEo^%<NUCL|5$he*A}IY-Hplaw|F+G@KV`1JWT5LjwNq5'
        b'Z3yrCbg${n-sYHEa`8ha_kC`E_viO_e13mtX32z_yxrdpKe<@n^+<8wCE<RYerlM0aGg(0=F&a&{JJnFQM$u(=?*{f`;&z)4TKv#'
        b'wItZ?%y*iC4Nr`@`23((R2|<s`>MIUt4f+bx_|Y`ph{`@RCqq6>w-k;k5+Vb;rJ3YVIF5B!gFWhl<3$lKc{NsX{Q}d$9GQ&1B5M_'
        b'bXmpU^(M0gTG_NC1Mgc_8!Sr}4vr&o;=&bgK3*Jjw$sJ+*-a?Ry*nNC%GOLA8@_^E+mU@&qUM^hgY`(f{Q2m{RjRftF(wR??#R4v'
        b'AC&JrJf);9UO&AnHMJ{I7Ji&Or6cH-hkJAQ@|$yy#)9BWj-+Z+K_f4Gm=&CRiRGP{@DsC^-thNIX5P^JqsObthBfy;UNt`6T)2N('
        b'X<a;Bx?<Pk6$Sfe&McVoT66|3o)n#jRSmKIt+}RNRd!C$eXBolPQ#IX@1OJfAI<sg`{y)f?=VE2^jwU&iN@~_93Sw+^~$1$d(n)t'
        b'Xhw1LY%<&Iowc|)7x{N$gP{g9(E9lM=7f(E-xp@*zW2}hRNwJ)Y8Fq*wjnDQkIlXjHF?{<!TnR3opW$@N$SKolYh7`G2{L7Ht&l~'
        b'{iA^Q?mK?Yn(Fc;_Xiz;nYrqwJPP%})?9`@7}XTzsrKTTS7tZ9JQvMf`v!-m7>u~>eRIl=H9(We*X!TcRt|P;BA(sKX%7!%%hu}n'
        b'oHfH|&OE)U?9WFnja7}mq-x4%54{xbi<;`HiZAY~pPd(UC1!pio0F>ghVUL$<Ki>2`zs9dcl)kAF-#PoddKevasfWGFY_k?OuXfl'
        b'>^+k($p75e`zL~&x#Q44RoTbxU0OB%?-os29)&HfxN=|6-E2J}cxe=Tbm7kia$znH!=(O1n308jgJCWT!_52>VNNOBIT+?6VVG<G'
        b'M3_;9KN-mFzZH}A^(=@g^-0;cWfzYve0Q)636^(U{`fP`MaT54Os++7R<;!}I9U~Ry-SZ9a-?){LFtYo1IOYyu(#)TgDVyft~j_t'
        b'ac+gTj~>^TYqE(}oc(z6gmlXiErT=4-k0(R6ODt5J~-{Tw4bTW#dYejxQ?xw{pPqW2$xC~JhLXMXsaro*;_v)9M2?Gn=KQo!U8W^'
        b'R$B2=U-E=yrMdTo!vQIJt{L2!gC}b?{xBasE3?;cG?-)d8VKJe%#8>0Y<~AseREEabwAnH@l@Y)yN@(K*>|k1-cvStUti_+cb4o}'
        b'J}X^1Z%c8{h@eb;=k{4mJ*j64y1ELY_mQhhlU2oMP6)z9-?WF{U+?IP%KFAfjx5=onmKaQ)Z)87)Umy<GgHvKEsQ^rpS!UiOs;(7'
        b'^*gtebU)PB@lap+rOiJKmlp<o((Mnw(=sV<<$doqH3c<SvbC+aF_Tx{o(y^@?d6S`uQsi$*f!+WAB?U)QeVElzP&3pyuPV*#iSwS'
        b'-<;W=s(-L+(_fXWo*fiHSIugiFuLc7zVG&Re>cd%s~z9%JM=(o#-xcCJa*2Ky$@b?`!ffp7GHeYh`x@#?tcjayb)Z6+ZT?W-k3Ng'
        b'Hm*MQWJmAR@CEr9ja%1*x8%RxG54y(>8)Q+Ui#PVSKW5=W5Z^QDeTGZ&t&V!uf>-?-SN+TiA$T8_T>hLnOHforoC~^_L1B74R0@+'
        b'G~$c57gR1DeQEmA4Y%I)O4$3(J_Gr3-))u0#!;N`hk@>|^liSOFWH#vdbnxp56&(M8i0f2!>y`nx$m8thx5bVJsZCFye;t^--vZ)'
        b'5-pjpZo2;q=hcR{8=C%5U%sK~{G)Z~i1gNUSFo$vyV|?T$Dh|8FT5?*wV^9k6y84#dgAHSrR&3n$(kjvtvfYr&MXbTMVNCWe_VUG'
        b'*;6{&8iVf8sMkJ_YMqy=D^9&uU;b9Az3b9!QzBjV%-p_D^mTtS*nvAbF7I3W?bxQ4ip2237YCYB^O}|xHw8(**0i*1)B2LzHbm*v'
        b'oH=?_*{S_yOCCS`Zt;(QGNNx<U-z`W&W@i<dv)OXDLcpae82C)zU~Wy2>0)JaiHhkzQ(@p`e5pbX}=zL;eyBh$M(;TKI5)4557?H'
        b';&X}e>7U9q_TFx~EfutLmVK({`7qmeb+m3swKZne7q4#|`kN7bHGSPRK^kA4_S8Vj?&8}YzV#>ZTmCY(WN*vvcXp*W{ae@DcR$#F'
        b'`?`bA79TiuL|=7Z_rxIZ_`=--m;Ue7&%PO)BUOFfrw6mDrtKK$AJf}Avh~^I(_<13ge%mI==)$_cX_b1ddI&Gw3W5Cj@<M>@`19p'
        b'F^RKU|D||C`^v}OSvPjs@Sw}Ie(bt2iLtG#lkH=IaQ{-g`mSJE-S9+RH0$7o;+2`N-cwf@8xj8UYhw7O2TC?P7=EMCx$mseFaJ&7'
        b'YrWmC_XcNj;o5=Lx9iKl*ZN>r6m-R;5t}xo%D>tA&8}&`8+f{UV(qezwEXSpEseoB5bTToj@}282ir>?Xk1+xb_3RRq-TZWr_M^3'
        b'E!iIQHO`!rjz<HpEsIx|EqOltU8=IK3zFfLn#jLpuzVi1|MZrJkF2cDYt0mldNJ1b%iiu^_I7^zD;>SP3vY_;yYHRe_TrySIlpdt'
        b'Sz^M>smU2-JI5@`Pn4xDNY;(HVrjhaoLG8T&$_+?z1{u2ogIHO?Y9HZj~V*PNqtZDcJB{ne5x?~7Q6S~ifb}o?Oj>%Zqb4JN2lHm'
        b'uJBZJh4%(mctQEM>f2MPfv)Mbwbeb3^lk0!-Wu$V{kQyEux8J<`?mCU|0tM#;+CHcZ2C#b>IY{`3HDvx>03J+&l-JkTdL-7N1w6k'
        b'%!B_kC>RnW!~ODujwP?P&E9l>s`bI*2WI!Y6#HO(?DdYrQ&LA7Q-4`p*VwbI@4nvd`-03}vg4-%u_X_u?kaw<{nGaKF+qc4b=$JB'
        b'JI5?}<o5phzb^jShc1~CWMFM?_jiNPpPjZfI1Prr5HFk%>-k~dn%?eAF!%3v{9qtf|3Xlhef40teZLM$u=kFZU<acT>|0?8HqbS9'
        b'%JlK04*ho24}KSI$Cc-V#n6PUowLpweZ{I&W3U}}{CBqF(z{-4U-ED^*LR=azHE5ym?e(|6TzNt?X0--{;{dIf|Dr~olLE*E7oMj'
        b'c4m^B9!RA&bZuH)vb8;YQ*33;#L+$X_kE(b`xD_AxTAR>Ru`UUQ<gmP;g19j?el_b<YT?vmjw&oxaA)PTCN#g+n5*|o^3Naf@XPe'
        b';ny{8s0_>1_Kq#Hf?jm{tX!G)H}U27_uLVFJG=Jj=&sV7{jvHVgl|Y3+B6W2?6~jYBhR0<WJhAeyss30_S-)mSyK5({=CZK`H%IS'
        b'aqf_y^xM?=g@cC+mjAr(FM7MD2dCusI?n2y@K>=PpBLZpm$40>X&bd<XVb*uOK(l4n|@pyANs=hZ9)At;d?>kquxHUE&tj_u5Ny^'
        b'CmdxVf8&saeFM?y6zkd1SJT^F6CKW%!t?9LeW~8={}CR@pd5+?M={w_aYk?qe^+0=u0Gur{YdeONkhxOb!|F4hSSe&s|wE1lHTr;'
        b'@Eo1?voMbJeSg;5eNuRi2IbI<y7tpIeXQiRso{%67hQk)=+E4lTKVbGSG1pb@b61LyD&Jm(S3_0Z>Hz8-kEA@FK(aH^FsF6PQU2z'
        b'mr~c>Q2gbKF8!x7(@VB5J1uA+Y)Ds+S@J~q!-iw3Ph0Y<r-y}qo|ZnXsjFc5y?ycC?))J0w-jy}2nybGapmsfGq%KU`Rmw*Z$3Ej'
        b'?ey(09Ih<hl<qp?10(ugc)a_C$AjW;+QxzEvB~7frk3Qgv5C%LrCV!8^!@7b?q56}mUU|fs!vOt9xUI~nS9{1bz>7_GWQj~xM9t%'
        b'cdAcqFA5se6HlE!cFE5&-zh#kwYX_R^2O8Fj}6)iqh`IBE*<)O{FchtsPDXZ_(*s`9B!$2Hu2^U#?%iS-I<4jomsdqGj?9EH=pfV'
        b'Tr<6LRN+gbo_J}~wvyW(ye7ILs<!@c!C9j}vvP89MO<;mSqCo<c4MOS#!qH{lso$L?b@JF`()3N@C}T89n}~0E=tW?P`qGa!KJso'
        b'9qzWV!EU=P*n{oEs>d$bnGAo6@2gE~DsJr@oeZk24avc3viz<|MVWP}WKY+o<s}=^;RBkRE2~HMtm*sb$GiXe@!*1(wqRi5#4GFC'
        b'YgR5EU42nd?v~fbrgsE8;b2e6#EW*#&fb1mH@oS!<g(dk=ihQscC4Rax0VjC+<v6GG)n#G_q~bjx#v;2@9)<&F8p5uw?BN(1%=f$'
        b'XKuLXf|EN|1c`pG`Q$ypX}fm((f2Vo=C6Hw@O`E5-Lv%L-RZ|WmOUQcfH*UDXyHKSlH`Q92R3|X&90I6+&?6H54Yywms9sAgJ#O1'
        b'FAc0&P%!Er-b)nBh)=kBAoK06^`&(+>$5`^W#9W+e*Tg_Ed0vgyI;ZdscTofo4vO<wj~owMdLEfc|Je6Z0VeIemL~;I|J()x8+Z`'
        b'Vc;W0cWqdEcpzPxS=Y5@LEePlW&cc9t}nfHYu@_G?1<5+@!=RoiTtDef|Z%Pa8TN8#AEV<6kgua`S6jA@rADpY>cn{{lLcjg)aqB'
        b'ZCJOy^w7(}AKUW7Ki4&`y(3)y#$eki+#eS|-hJ`o9Tx@r<5v^L#-7O!%9*gq^?H!ET)Q-gIn2lN1L41i2U6cou01sHH$~wl>?xS='
        b'!*C=1VO{A}8`hU@%s=$YAhqe0!8WWfy*S*0Ah}ltcD$Tz3zzpKMucO`EDVd5Q7eap5xx}ci$n7UHlOi$>fz+V83S`KT>FcG%<Puw'
        b'H4`oyXe({KsVj<Z=7z2rK^3sRtUdp(A2bi^nfZEs`0F-JD`xHdVAIXtZo0XmscBx=*cl(B`0L!gzvWM)FB+F_Sy+%>I4-?x;c17{'
        b'vxEO<rzf1Z<>k5wJKhTW1$DV^j+U2JRz_n5o%@SeW%ty?UExS%%^&WGTIky|HMy4p8!oSD_-ONo!r9G#*n2Qj()3TKB-44BH4VY#'
        b'T%JgFCfDqGxB1B4V0q@H{LIFJn(oWD<tOfKel48Ue0cA~UsSxhw`P9v#NRIKtLZ)`5$_xyMqIf)uldF>$fZ*jHNLblZ*9xl(Xo!N'
        b'$-JC+C^2F~NAs94(ay}9iF>zh-k9I~^Dy*;AHO;0vqL5i?U{ec?(?tz(z)@9pY1*Wob%58P{YsmUXWkY@N$sDn#_&$A3dd};Wx>t'
        b'VLodzFV}BKo;qcFrnvLrc#zx1%*)L^VPvOHo&3h``L(;x|Im5o#y`Gu@8n%UMr(RTHtg72IsZcykL{iOXz<6mm6<n_6-|}%&#U<9'
        b'-p2V;D(BZ$JQ4&vr*i)Jm6@Hzl})qe*ImE;^u|oACiCdx_{PHKZPD)d#MOI-T+*?vaORY*=D*k-%(-gns0(A4R(@&a)0Z?P;v4fS'
        b'r^Y6H;qBwT|JoRz@aJ#luHD?dzG-isIDUG~;CoZSDL-j2Y;Yc?2ImLob8yNXYCL|u`cJgfPgzr$iOng?3oF&?V8!L1-8Q88j=e|U'
        b'4P7|no#0>w=j5SxvcuaP%~x|QQLwF`yk}!x<NTq`o#B=wYFirOE#2kICbwk1)$;M8bbMQ0dQABJ;jmcxy3JqRn<(A7WmDtQ`b{^y'
        b'd{)z0tDf1n=Dt`{>l>MM#SNd@9rV{@>5|sg*Msvn9N|8=>?%8k?RYnOKAsp6rqmgv)E1>QW-z71-1jBabAI)8;cy(;cap+uEjX{5'
        b'ZwuFI$vk>AaP)XE`##@bnC2+v8L89_iN&d9t7_vx;M%fq(5RqGn|rR-JaPBR%DiA#20QfD_V|RS-W(hop*hz4y<O*RIk|7z-tLR{'
        b'c3ix-GxPO@PYi^SZ_I1{Y#4W4$)x<6AkKJsy0)yPA%9yqVEf?nqG0`RM(dxux4Uj{$9ci}9SeI0*S{*eeodzT#0a9i<<?)Zde_XG'
        b'nr?mI<i0cacAvSoqbi7E<Ak1p?V0lMCTCvrj4+ZJC5h7;KVCFFKC2;b`pEK|XEo&4RYVaL<c@jU7ouO7ICbyxvB5vfih_Sm7&ESV'
        b'<<JFX^~r*vS5Fu*W%+_}Q?su&pEY&f`0e8==T)}U4M|mYU6!AkdUbs?R>P>q_jcs&1BC0A)Hem|o)WA(eO&Zg;Ac&}EM7Mxd3qGK'
        b'dSFNHUDZ_U8!ef|l^sKFZ9l2`z^<TYTeH6_F)UTR^!Pe(ek>Z+Yj&(>Lpm=p<8W{a1?6A<;Pn#5u`?IP3w!=3j`V^RUAs2d_q4VZ'
        b'Z;bzV?69CJS(!QI*1A9I{`sEGKi{)&O>DwV(WWQP?tW&^=4bXy%Z`6j86Q)=EHUhi2jVT6c%m^G{eXHnj{btgshgT!PsE$f3`ZdC'
        b'Szpn&=gjKl>ZNB7U;gDpd}4mZJ-dUD<HGko*XL*N$voefN);SzdcCUpE5ENDJ?h3`9hu#W#xyiPyeIKsdf2{U1&N)7C9$gMQ+_o4'
        b'vX1uMi{@4}KeVSa^HR7hr~zM2ZCO>meA2Mg&Q+6_?n=FqTo<n{s{UQ>Tl?nDAn4zQL4%xr?pV<9fHZ$ESQaG_TpABe`^`Y}clTTn'
        b'P3K>*bK2_z&EMXW_;5Hmq`dZ)!vo>>mD$tr%I4-D?TUuAtG}?Ju_3RqJ2|6bdQos{P9M1~FF28oe#f2KpA1XbOn8Xi85lf=^78&y'
        b'yt*_oVnJnDW#tF1y(hU~{wYCz7jzV!UG$k#^LyewLry!qJyYMA83-@TZ$@bieXin^>Y_bEs`mxg-oEboV1?}!#m^RPn6z%_Ri92S'
        b'y1Kfk>yEDK&iY%rw&ksyKdNQ^$RNndic#AuMxI^Ny16MD*X^;e9H<yMZ)(>ivu~Snd12wN2EzP&KFm*1WsslwBNM|Dr88HqY7Guw'
        b'QP0FM&zB{FoP_W5jB36y%1hyM6(g&Qf=pDe*)wEYL6FX~MQbXGuR8r_|8Q;P)%DkRWxmt3XK2vg=-4;^l;%gmMAwZ<jM%w#W8uL>'
        b'n5TUer_6c#t#pvL;+E>t<kTR`8w)R)9lgeLc|7Q71n2ei%Jiob1s9JwCoyhaP3i|rw|5r=%P(GCR$FrMCyHt-*VWX1A=umb(cZ4?'
        b'7<$I3@wGP%Y%GYr(}`^ymVM{DBevqs$C|(KSoX-ZuV|S+toh<_BNFMT3{5VZeA$+uq+1uCG_0jzRCUp|yz0{E<XP9eWyOfw5@YYF'
        b'4PSuY)HUzUy9$;(eQVu_<`0Ce%k}vWl!fUQ?uf>G%9hdL;rjFJsnL>I6qdF@d@a>^!JL=3ZYv54@#ZrIm$&DZr^kfl_O5j4#(3M9'
        b'mg-Zs3_qc~ng8ou3#wvgj2gBkJU_y@^WW>)Hsr=R8w(B&jRmdJ8w-Q~dv2~C6=ZwkkZHdksK54;Jy%?C<g%ex)Sg^_?bM#nlpnc1'
        b'lf0rfuY72_DjYBL+DD^0DL4hwTe8*0ob%sKpBv44c1TNgNp?hnaQ@aK$MQ8JoU!4}^t5YdcSVQlAEr+GMf4o0rSzmAcZ+sTNDOQF'
        b'cz#Q!X~lt_WqIr3>5}TA@KOI0J(ZQGw5F5GN`fPH^miTRhxhg7{4&<Jr>A>wPsiS#&W_JbxNe}OGH*|?)5a#oh5Kb|P^^t@YA$F^'
        b'r&^BIYuWnnf$N%|h|aC}u?jIAUWVy0+w!7H_w1r&xv`w)$BMg?otY1Xt<66SJhS@J?!;dOEr&l0^t_nPtIR8CN|%I#=mc3DEIaq)'
        b'U+`Dqm~aERu|>jicI|ruf3lq2lOM(Q`@ud&blne&uKTqQ4IDd`gYzc`5kGj`{O+Yao0s+k#ckN?K09`FywbsM;cJ6KReOI_+x6_K'
        b'4Gu`UtY-WvTZV--b6H|oW@*?7=t-~q{@bfpw=P|J?~!%!+M?Pi!Q%AwiLz9%Ro5RojAO$xpri2C)kR^SAiX6z(8uyJJxFW%526aO'
        b'XV>&Ft&xqVhiMhW5+j4OZi>=s3({&`-PC&1(ub<o1@&e4R$)O9r1tv6$oeVCy6cbSvNp&@O-JE*tBYz&w-w|z<NuHJhWzRDs{ix!'
        b'j_!!giLtO87#E~*`w3~>zVxBR>*CK2Nf+%YNT;&{^PP~++$f!k{<C!E$Bw(6gErL(<MZ~UJHP+-)(yeL^0she(naYTql+)tgmuxW'
        b'dv;OJhL*fos<x}8Bm4n?qy5Tl1wr7&$Hotu9~*aJVo3cbR*kzTamu>*;-UprCm$?~J#^~g(mi<#s>W^$-vld+J@d15d6{`PWHJRW'
        b'Z>_z4=+%F=<X81mitDbQH@_e#!se}66-HMza@*pdSY3SX%pWF$bw*4r4Em3i<>4Eh>DqNQ+X{nZtMc1}%45zsZ>{MVTKKzYY_-yp'
        b'f-dgPgVDfKUpv|wi1Hi69bG%=#?QxFcD|E{|GxU1u&9sf$d_+R=gpj(ykbm6depX}^p<(w4R>^q;lgM?){a`fy7vCWxM(uywUt$l'
        b'Kc%xe{MCS<1gQzj!t++2Q9UX#uCj7OcIMHT=e+pN;=G!UVKe7+%^bg~FsQrd?E1qkZywjKx;xh<>fHTDZKCe)@810V-ItvdT+gqc'
        b'aP4>JuKlK)8jipA2k%9sQg5uxY!43CovVhmH74G^Gkp6XH?B_hI&O{~cY25CL_zHGqFf7i&Cc8zQlC3R)_ni%4O4@OyQViR-@Ux7'
        b';r89@;$g!zs4%9F4Au;zn*N>6?(%4hdp0!Ym8Z_>Y7EYn(^o}h<Z)%jM~Zr04A0x?(Ro`C%?Yoq)Uj)8^{U{~8nw6}mz}TdjLOx?'
        b'f4_TMUfARgg4dP>>(ySrF`l~&vKQN!U}jL5e55E_oD>WeC;3qx{_n2sbw{u5QO^%%;8S4+CKc3`1ey5Q?#70w=MZdr&G@{=Ox~Z!'
        b'NoRHbe|A0of62>-kIT#1|95$b|L1u*v95n#5fl{Rw=W$Pv^uk?kINp4pubXAF=@!;lXlO_Wne~0*gcDq|L>JeVVgT_aBnFtAKUTB'
        b'&dq<=HR)@2ju{p%-u&jS^2>v^P$Jic4o6Y>@3apOKl<NqA71e2|BLovP_}G8{G-Z~`+9bD@7dL{XIE!t&cffk7u^(#M`Oi=J?OCg'
        b'*F5^s6{8+q*Vx%zy{x%?#lm+6JC#2T({0HMs*}TQC9B(3HiRF*O&Y$kAwOscri&UL*tN1dnI6+VIk@biLb<xJe9WyY&#rE6TaipR'
        b'G_B8Tx-Hpp?W37=acq4_vh|JD)ya;}J(^73kZBL!84Vf}L2GkebE35Qp0Lf={MB8F;kVtE9kQ@zOQw2N&w|XlhV@}SgRXvd46%-I'
        b'JlOo;vaV}h``dwS`Pnw*>TFiaCk0uHuM6{86XmkHsHQtvH@UJhuV%xL;G`(t9F~JU=U3(>Cl*BIQxso85Z{dEwJ#5ZcPzsAZW)ZP'
        b'AUK<Y?n@BsjLAW)4PV(6v`iaD<qDd{)5G4(GrL;yl2v1dRaK8!pC5L1%L``YPtUJzJY!^j*ryBADIYm)aJ-#do9=VFx<9|G<1@i='
        b'x%1He_x{T^-Jd8ww;or1R-QPPWmJam$(7;7k49y9=8yWud3lRVSKP7Vs++E_Doc#JwJtB{a#ejGst<#{*4<HGYk1FxqQTR1=Wug<'
        b'bTY>G3|U;Xtzhv}*Zw-{YZd1DTAy1Nzv`y8qOM<c%}Zb1_CV0KpMT18^GDV%?m9R;7M%2V7wswBnE&GDmGeh7-?Ag>Yn}4hDNSK-'
        b'Yh}gA%ZE+-Wwx&nzMq^PwV*02ehOoARu^n5+MX#7j?99}Sn~(NEHq!SBe>!x4Zk>OwJ)oy2u{iwCFSFTsl@p3;xF8mS6dd<jM=hm'
        b'?#P<cvsZntT@aRcotaqU=_8^NZ%$F+iACO=w~wYdJ>DD-lU(uP9W9yUd38b8Bxp|O*Og2fb6#Cu&@BoY)CJK^qp$<^%xBldrx&%H'
        b'UNUD)-myC6oLtJ&gBIn^o1zf}-U|nx`=fkZ^8S3BKP2oI1=(l}HvM3@&sL0mUp`tg&qP!Gxts(Ys`~FF|HHhTetcf;I4&>2d6Rsj'
        b'Ci7~lGN|usI)>yvr~D7^X9Q)(eUFxB-`d=~^|2Gi97>#j;^eNu$w`+5XVK6d(Ql<bdUsx;?ThK+EyFJjU)WqXV(?qn!E!jfF*V}Q'
        b'@NnG3#HER%Ly6e(S-~HtE=*+KOI}+R3xAd_6I(kp3UgMXXl+p#=B&i26N-Y><H52+C&dPTLojh_^NO%X6od`Oa`@-)?@=}3`@um!'
        b'rul2(Wb^XJqFa9(<A>fFh%VZ2O!O7+{mJnG2d}pvzN)ej(aT*!s;0yz{L_2Q|M=L-%*)AiSA9DBQ)6wzmh8$L8;I%XdOff8UH@43'
        b'^^bL2|JYxT2tVgv^<MMm9!pkt)mN4*Dl3{iYDf5LV))Q=#H!Tfh7nU@%SxK2l!PCgPe~5GKh!+$u^_5rD-91<s#!4dw8Q_wN`rY%'
        b'PR}1#8H?AaX5^=mD`HbRo_cLWP|&0*lgZS)<dpEOjaXTIGPxo-qbvwpx&4Ewny%FJa2SE)jQmk+h7Nsh*y!iRp7GrIh2vv2j~$+o'
        b'e`VP<<G(y5IlrN}slM>dfto!>=hgi5_1gTJhYv2xZ!cRv{(&jUH4Vui%qs&y$bEYb4?k(_X%o+``$$c95NzL`;+lth2iIJ7Vf!c6'
        b'U;V%r4mZ^&f7y^~s^1ZgTOF(xWGPl!pC}FLhaiJNrV{a!4kt=a3J%ZV%93%Fsp<J|K36niN-*)}f;UsCbHZ0!YD!X-&EascGs;r='
        b'`IF*Dw<uA0QgmD^V)MW8=*)l5zdSZ?Lh*+ylhLRN7yV}7q=M{74#9q_ji-M7T5V~nxU9A^RZ>=4lPV~yZA>M~YG<XAWwi@Z6=k*8'
        b'rz*>8TT<i8f>^Kpi(l5oQ^omprKytqy2?~ReqBu}kzd!CO6J$iN>$|7El5@7*Il0)pI_H<QZxo&B0u%3`Qd&ZpG^KLOg6d}gZTyZ'
        b'+4<)rlT%Wu?4oQhJ~p#B_Fp>r!QY*|uJeC){^K?8-F*MBh4pX#&tEOw`q8i4wd#!>y+6Hv?(a$l0000000000000000000000000'
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
        b'00000000000000000000000000000000000000000000000000{ttU_AOHXW0089w+6bzus;a80s;a80s;a80s;a80s;a80s;a80'
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
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80sw(WkfdBvi005Bx'
        b'Ya^(ts;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
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
        b's;a80s;a80s;a80s;a80s;aOD2Lb>9002P#uZ^Ips;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
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
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;bf+91;Kk000R3|Jn~`0000000000000000000000000'
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
        b'000000000000000000000000000000000000000000000000000000000000006cCfBz`!'
    )
    _firmware_identity = {'protocol': 1, 'firmware': 'CNC_FFST-S3-0.1.0', 'app_image_sha256': 'bbf22da8b2dbb27b69fe85b3086540f75fe483ba4e7e9c93f5c6d0c57258f211', 'application_file_sha256': '064f76cbb29b15c630d768a1e787fbe2dd6937c12b79d5563758b9b79fe8f724'}
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
                                   'Confira se o BIN CNC_FFST-S3-0.1.0 correspondente está gravado.')
            if line == 'ok':
                return lines
        stage = command.split('=', 1)[0]
        raise TimeoutError(f'A placa não respondeu na etapa {stage}. '
                           'Confira o BIN CNC_FFST-S3-0.1.0, a porta e 115200 baud.')


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


APP_VERSION = 'S3 0.1.0 — Controlador PCB autenticado'
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
