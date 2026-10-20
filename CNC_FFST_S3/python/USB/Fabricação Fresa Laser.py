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
        b'c-riJd0<r4)%cwyD-TT|MwX~AAqfd4VP-<s2ARno$TB7&EMm!!Op?(g6K5tYHm#XpF(|eyTEXhqNt91SsDM;)p#oY&1q<3%tJ0#C'
        b'R{dOXsU#%i{m!}fzS&r+zwNJg;JtIVbJugvJ?Gv#FP~`C#=V;hj9(B!BH$sCgl|=N?i+J<XwWN3Qy~DKIR2!VwM1%$M40l7su7VE'
        b'o)CCK;R%DM!|t>#ZMSxc1+&FW1DRP-TspJK-qB_6w063jGnd)zu6Dbn+3Hy8?C$EaJ6toJjwb)$mUfG?Eu)Ea*qnC1jHq|nDwlO>'
        b'XLkpN%_6}>OC45A^HOI^bJvAY)|J+#ZXkxLbXYo@DYkbKYiG0m2B*v7aOuBKRc)P3?cL2*|EO-4tv#a+GcvG@3<P7ALV$RKNS&7E'
        b'X2<vK2&=Pesjb7(YF*l5cXU`>&=EzJ_NMN3i_6+9wn0-!$;vKklh+qi73hOjo4wPy)V|#6Xt#6`K(>}uOT87bI-OQ0F~Qs65?d^`'
        b'cF4%qDJD77;K@&F7E_X(spBJwWf@c{B~@Huaf(frc1&h*iRL0vw=zkWyAo2gK|i)z#rWA`_58}pAJD)|gEKQAy3GR3Y__;8bi9+q'
        b'S>o*3qK*V6F=S;gZLxLQ0^7_ZkeDPdUFLKyrGtPB!n`mJ{|8m$K~TM9T84k_)Q{QwrHA^t$g=L17OUfjc8p)J1A5lp0fqXrv8}zG'
        b'N6@*+rYytcfdZokCULf#c;Vw{V(bYa#(lk{afbeyU+x7A!M!BsjX5~SpU;0|PUer^n4|d-^T)w63Ea&_q46_Jqa%$p_b4hB$Vbu}'
        b'bIhlN#(H=b!m|XPMtGXxX@ln!JRiaHF+88aa|WJo;TeJ_oCu8qJmui7glF$0VmuW~jGHGDqdAfo4}f2K>SZm~K_a6PF=N~Q1+5#A'
        b'j8N}NcpeHR#+XKRBea0Hz&{D{!`eZjFT02q>iQd~tq~<sBUbv3UP;no_?1K=japLBPumaa?vhey`X`BW$B;A$+))rWs~_W}J907Z'
        b'OGzrAX~H1SHX_X#l86z6VmR$uRr}3Q5Y!=M8uYV<^>-rFy*P;&(*S=9eSas!OLGoDma4JhQ&6^~A<~QIC1c^0ka`kfnVpfc-KzLa'
        b'Qfw`8Z;(!f6Ke>Gok6T8HSxcsf%jtIA&*BGw^QZ52R%Dgr~jadeeV2D)z&|1`ks8)Gef*<%CSKY*-FTMHH5yW$u<#jP;~cV^7P1S'
        b'&VXN-vh_R7phuN-P9sdQp4aGam*Q`iOt(u1M3Sn3SBloXQtC|*(XSQMfD)R>))W%&lJqWV`cqe&a7qVV(w+hHfK#%5u8DU_dMAXB'
        b'JK>NHc0%}#p~F(rT;g7frMmll@AzA#o{u2ET(vPX3UHp9dV2mOd#zJQQaw4{Mot%#q(V)4WJCVdNo7#;hUa3pmLtxO)!!uT)NF0g'
        b'Sk0QP$r{r_$)Lenmuq#iX2offi>`jUPQ9jv2*t_M1mVu_GQ)(JJs!1g-X^z|*2FA*RVnp{pQw}$R!XxYw}l_rtNL(&xEpDgYTQd{'
        b'=daNSk!}MzXGaQC+&Xmiy*4bwJe{j9^pL)nhK0#b=c<H=o_7o{{ku0aYJIUNOcEk=n^zn2M4irc^rgYqzUkR(+#co0T^;*Ps6G=r'
        b'I9H=LaIEK8$MH;#GdND?IE~}$IiA6BD#s}tPv<z9VN;S+8ICS(Zzc|9p4OBg^*#9_4~k+z*Gj@f=8BUjKAlOdKO)zhsnoVKsn_h0'
        b'(zM?J-X$4c8ZPwo9^L`7AlpKqZ?2`?bXABuMtUsw<_$4Yf5hg=TcS5ikk<D{(YLr(W!<awcw&y<t=e#<v`w{sdsOds@o`nsvk<C1'
        b'1)-4;x-VJ|Kb=e5VUiF571<K*4v~6>sq30EP~7n`D6VDuuMU4F0S{X<3FT$?*w}`#G343s%E<MMWy9SgV;dhOG_dD0IWYdau?=T2'
        b'Wxrau4(bN3wQB0!@b#EbjdlKNOb$$maDO@0n-Jyx0^TCLF^dSAqlf25Qw@AP#{C$%Eh6DbB5sco4B~bSd>jKehYy?@^K6M49O(6I'
        b'5ovoioE)R6cfUV&;%{TSwny!L7v5fqec=Odj~#d(2k2QWW?$s-=P~lxNJ`cIlLOnM<h0wu51zmrgnM`f;WTjft79jx*u|2C?>;g%'
        b'aCpp{K{zK5cfUL~@bZ{kN`K_;pNt7TyI9Xe4!k(F`$gJak-Pe%XpsAbu{}@zon|3t%?f*FO!g1_Zfy7Oyi~jQj>*}v0(OsK=&pd!'
        b'h=HAB`>*t{kO&sCeT@10Y-G@5b3cYdFI*>NoV;THm4`fG7&eGupQ}%*g)4=gJsuT?JxtSGDO~e8gzX=XL7Oq?nlr$&CK6vemXJVB'
        b'532{4k@YC2A#7mI*ugnt!Z^>-1MY0Uw7Uz(-t?#rc_x7{wa(JO#8!J!Hi=>*kKcN=W*~2DkB6L|qUrOfe6cV$^gUyO`ksM2eQJEt'
        b'BJF-~CN0&%t4VuOeN2sh>vh_#tF^Nu2M>myZqN?gHg@o~G0#(jC*b`^pZhkf$FWGEYQGv27=d<cgO=vvwvFvnZ4S?!v_+K{ZLQPp'
        b'RP9$=7Xh-~tflke^cxbzP&1J5)=&*Ngc+wpG_>Asviqj7xXPVSU-x1xWwxqHJvfaR_li>!k|vOOnJu+n3R8EEvqob_WDk%HH;x%B'
        b'Y*Y-Y#DVHDF*DlJAC>CnG9_YzIA%~Kv0*D8JCmt`*lpfe&(`kKZ)vx=#gzLzJCm$$YxTyl4Mxf!AYS<_)NGi|Le?`z(->5uJ8X;!'
        b'<D_HSfo$xR)5o-f2cu3uq}{KA^~?|-cKTP^qf?UZ(!d({g4Xk?#<OS8GuU@bBaC;)BdzDtiS9G!dkxVkZkWir1W}(f=1v+*b?XdK'
        b'cWu%NQ<56A(;ZjtP8frZdM;BKr+aSo>BUf2&tQnP9q}VqS(j<~cq2lrOHd_GjNDO_JS{poa|(nC8r_Fxok&VSRS`0E%ghAa!{D9<'
        b'YoPEA5BN?Z!SG6fu|65J6wnb4!?PToweUb{&`m^40a}ZM3PKmt?xYvt(V*@H`0wzXMSTaYuEq$^pMdrWqz4rT|AP@`bX`Y`kHRx)'
        b'DltZZ4mSxN)a783kZ>qR5TnTZpcj4%&*nH{1dWPNOD+fVnZwOMQXuPSyCyUJ40S}**C0)S2s+y+l-~|d47iIxZ@d?tRq*tfHH`&K'
        b'm-<Z<*Qux;CP`zcvx!`9qdJtCx?kpM?C()o!V<KggFXsn&FUhJsK-LpQFA5Ibx_wFreC4{C4l=gXhYOB#5e==*+=1NgJ%^yvmopq'
        b'z(&CT%zI<bacJ+tcM6Q*5LWIcjZ7a_LwnClAA@@q^+$pKOX&+}>n@;4f+q(a(whUdx&g{O0)6zyIYpQsJa@3T1JWH~piAZ)h<fIY'
        b'IeVcGurH-M&?2_O^D2yCDCB$O#k$W6jK~9oY=B-l@*)w>{6@O&%x@skE@=CcYG47>*|l^mh-xF`KM0R7ff%=gPW(UrBS}l3y>0Ng'
        b';9)j6)rlJi^4~E-9>0X=D@mF&CP}YIOkV}7{1oLTRH%oc;4x~=_kuq9CF8J<p}a=g{woM2zYfCxfrFwV2kyl1aPl(XmtrxWF$wkW'
        b'ICxOKMTHwuBY%z<C#p%<IJ!F^8bRlcg0XIdaTcIIqu^--zx0hHeFWv99y|);AYC^kRZamOgZx@sT3W~{sPEpFwJ~UqAPr==5_M^)'
        b'C{+3msDCfj^KphiYeDwzSEs2rs&uV;t~ik@9h@QU87vz}mA0NF59}F#B1Jlw1R>>X&H=eQNgAM<(ohO6<!uM2NvYB3T8S$ehHYyT'
        b't~tO~)i(6@AB>YexK@JY^WYSTNA$CZt1*<X!2N<iiT4Y-{hP$+Rj0N`J*(RF99_X_J}Y-$A&tvy%v8ausmrH=63eWZ^vV`>=?z35'
        b'Cgo}jn#uVk#`jl4_>ne~R??kR8IMLCKZ>beZ5x-FKOfb&m4#0pFq`W^c{bN!%p%Muw@uIrR}Bn}HP){-&sTXMl1byXve=Mihowg2'
        b'eVA(VvK^!`Gs@V6akkCya<s*w8r>#ngsUu{jIFO*ZJe)aERHf4W0H!toXH`ES0$Ye$;-FZ?jYvkDBUcY^)}2g+;noxNQ*MG5gIW4'
        b'o3pvtr^6|<eAJV$h6yRL$*+#@`G!n3l1&5aH|f?VM4^DCl{Xz3<HkUn+(hnQc^KFj#`sMSF`Her7NYwGSj%;6{QmKx$CY$S;`WW{'
        b'nK8qYP205Y=WrcJ(F&6mss**Vu{%Fom$F&}&HRysCvTXMEat9G*X)>h$OAcsA9z6&7AKvPJf3e8o-7h)L`{ECy(WbSYYt};V(=Wv'
        b'iB%s?BIaCI@>}XP)35?@bqg}phe3wji;KFj*!rE+5y?CSi?{w;@|a!1w8qA7by-od*%87TsL-#df-)X!EZk!KMgnIjEb<=J)~}_U'
        b'tF9YN1S1cVKnq!#q^}^2ux`JmV2bsOgz-P;@yCyekYH}omy)2q<_xp}8*s0%`1I$JAf!V*_6r4zlRlSvw?~6Aime(X*s3Xij0+Vs'
        b'H*40sCy|`{*B$<n>GR?t@#(rNPIQhPw2uwkJho?Wqjftuo*DhMhkz-Qrvi=Y-ne^~Y(M=f?Pa<a3PRkyQ0k!PH(UQHxtEQR8PTxP'
        b'dV0H2WnMbg3x-dE$kXaU_nJlqLH(Lcz)D>=7i&$3Ff}eRX$U&q)$-bBOgkF%JiGM+Np`O~eah>WV2B4FJMON)E|3GCIQ=&%ZmzqS'
        b'4z*_MchckP6wNlZFu^(z+N%>q7pP^WAEC|QE}$w;r29vRW1kA~7+t#M^*T?zuDxDYJ71SOf4|zDg^}VOvFkC>Z9w;ab>n}F?wM2{'
        b'34yT<ai^g>Cu<y}(mf)&Q_x$M6#*8v7Bmc|M8>@w_f*`U(?a9U#(lcx6AAmkecjmLj_asN0QLa21gNJyQuc1R8kCU(RGE?$V%~r5'
        b'31b5j#yBmvBCZ?@N=a>d>sQk0QAyTU;={(oWkyky^_ZQS<O$m31mT)9ZWY!v^gN0}g3eNuikL=R-+eDkn3h+wdpEm!dtEJmy`t~P'
        b'=fY&+-MgL>A66d@C6!Yi+Y-@t<P!*cF!Y?XB=WH>k$p%0N0|Iw%HP(DE}1`Yhylaos2qG!a{ueRZw~@=II&Pn3WG$`AG{*hwNq<7'
        b'FL@q0AWZa3Tg~Z3gV?7TpP&|c`=iBvvG2&)jUH8khxDdyf{AL-Tmd7S^PH;ZYnt9dpp4i-)DBM%OM@mdcu2IOLnXxRSM5|MspYaa'
        b'tA$C)5fPi0ZG83o)2S*Uyq9$kt@9KiT)cZVwEAJS(dZgY(cQiJvv(3SWRFI5w6^E#T{AXab0$4J_8zH!ZAwJ1p=n)AufeHHH~<!c'
        b'M$Fxmt|>h$^?V)r9q&u`j`PVAt`x%Wnh@#Uc0S?ISkJJyc2jz|T%Kj?`NB}r5Tm{E(epW3KXPxyKKf~-`%%Onc+QLFZ$Hgk{Evfo'
        b'oYy~m{=D|osef0FKX52&zXn+CAxyLG)16`NU!zM<m*NII5hg&$uP`K`l;kI|F^IqCe4m;;bi{oxM!46}_b(|~cwZq#_YAG2<7FWo'
        b'YB5n1r-`B%17fbh5EA?IFk_+VRB`kz#W#nR-A`=^_f6+F{Oo*hcT|7GU00j7M7vjDW{<1f%W0-p?p}3XxVCcqv9L2wif#vn^{X~V'
        b'uX}B0xZ94tp0C$@E|Hz#t0LUD(#mw4zx(H1D-ZOCHFh7k-MKbw-uyKmA#YkR*7&lhdrI^y7I%ian;0AI3~}F#uAS<wpMXpXeV5L$'
        b'ooe?I47GmjlT#Z#T4+a~M>MZp-MjI_o^$UH_ul!TZhZ{cAMcl+en>ic?wA&ORK4yG?rKW>5hHe2qHoOzA4?{6kM9?SxmzEQSics0'
        b'%`lFzaIpCNhmXxXDdcR1<?O`l^9OG@KXAkOJ)VTE^GWaenAjB3uvUc{fN<th+_Bm>e%E&0u1_^*o<H!+@4q;{CHn3?B*N%fzhUD%'
        b'GPNK3hw)_f$t%#x6{ey^n??IKg9UNJS4YEc@K1LAd2S1Xhnd6fWDMF6cYYx5JQp0)+=|#R`TW4-prF|E1F=Ct6VDHPG#VHbb$%e~'
        b'`~~6)d1&jmk`S3xOO~la1kI_I=o914e=zR+Pt_X_#m#8BS(B%#((Kn9)3jc#E=?wF3D3sA8twk)DC7Oph&POm4v_OlqW8ta!nM3F'
        b'lx}#;+Y<lY=&n=W&M5x$Bhz!E!j+&C8J~}$vts9!?srBho6X2HpZZp~^3#79k3<=N=Z*aWW8*&?<r|PY!!EG}>3#(hp3WnuLW%pm'
        b'(QOfTpL4%EdNz0bq3P4hC-0A(x8j~Hp(mtw&z-&D8^iSJH%I2Fawi`imZ*Jw$P>56Bh4Fd{~0rxnwh5pV|!YjW$TlY{*R-N-^MK8'
        b'$-R9^g692&DQa<tY3rY)qYs|cqzP0?{TUc5tSw}HrViHKUbpG+zbRjXR7*%u6?({iP1%IVq$gmOdkR;Bgi6=aJ%`=TjSf6FdiptO'
        b'c4WgXO!9&Sb5H~Zu|7_&-_#>C+&$K>x@$%R*wimd!i2-$NqrF{b{k2aR5Nw^##hC|XCXkfqb>P}{=mMdmghg|?VWY~v)A{(GwyhQ'
        b'^uDQg_x&~H+1$Q_<f;9A%aYf8EnUBMUwHqdXA{;MO23png==d=Ka&XL)3Es*4^yw55c)4@!$Go5-H=aETJM{nUqAXxW>~_L4<E+K'
        b'Wqnfe<cqPNj_r?36QTx0_dVEoX~LejqFx(t-!)2i0=7OS>F*pB!Xdt|h-`gC`fLW&CU&zL0+KvZa^$1Cwnuvgdix_25|YRDizy!-'
        b'M)@&#P>hNew|b=5bE7E<4IiFOQMIVAPH`uzBU8SD$kX>rk4=acCL|P*QZ-4rZKvw=ebQqaPYUYLKlAx#olFKF`Ph9u*28Tb-7tBS'
        b'uD_ww;K{bA`<@)r6^VCkDv#PN4jzh1It^uo;Fi3!U%OL%I-KmWnEK*PgBIhCN&8iUCse0DlpeZ0S^J*eJi1?N(2!Woc^LWkrO>Z2'
        b'$HJGTe`;SYgr3eUn|2Kl9Ev*qcd6mEbNeF?4UnBG_YGJPXcQ=%AQXW!wyLp+LRv&@@hDc~glg;iQtaI$zp6WH${sD$lGvBO+pk%3'
        b'8f~N&O=NCDiXl&x8Xc-3Js;n-X?$*NN?~4fswzd58-2|gVJIi}O6c6X9*MX<6O_RGgiz2`)v2n(UrT;_A?`#vqvA(}>p|=$j8er1'
        b'*L%$|ZNr=7#I>UbuN{qhV&K}*tzgI=k6HKdiMY{&Q%2*S2UTMrX4E}}k<fjWr^JR2$%*LEgR!Fn6Gr!V;;m{jFmCkdrbC{0+-jE4'
        b'9W^SeEdF~kknHo2lN!(mweAR-LSp(>*yyQU(Y?R8O6*td+GFZ{UL4Sj?s@&Zo6wOwFw)y*3~N)LF(Cn@-*A4U=Q%3PKx>p`oO^hL'
        b'YF+CN4V)d3RWB%c;NRej@~#aVz8L9w_X66_y|jk|Xg3DZ{(Yq9(+g<-?xj5$K>J<*ZBD}Y6K{_ke0wDB^?|oXz#3SP7<u9^BM09a'
        b'iF@zxIZ2q5lL!iqFnK|ON{CpW5=AvZ;DMiN$~LJ(7m%`PSDg6c$iY933>+WXGjMa#|48~bMmGF$BtIwTS#@bVaUUDG`_8qhyPj2t'
        b'76I?=er@EW_E^~9yS<>bKOEVRf9391Mh0G?fg3HV)89!Akynf^-~H^!z&;vy`rnceyW^G(FOFDtkL2WOEx#YRr8QTTlQ(tu^CQpg'
        b'ZG9qExb|eou~1mW(R@k|rGvWrv5{lrFk*k`;UQ?Le)oub57sI7R&eIe%Gsw5y_W2La%A91T8i~csp0O>hVMr7n@4tUra>U)zJQ`*'
        b'pF8LFjObbq=<ge8%?;5%I-<+zwLCg<OLJ>()b0VOLe3Mkq+^=Wze&6Ak;~N_27My_*CYCtkr~scXGZVdG9tu2S6r5<F8zxngo13)'
        b'-#-$+bR_>SA@r_2YFH0;Z)7R<sD#kQM%S975)ooUU+3fGIHWz~0k$S+R#cDR+I&r(I&R&5sOaf7sY9I}d35p7`EjcaEjibm*%&&t'
        b'&!YmFxIPz*W7k6!MyisoJF@kN^tg7%yGUn!RVobC8a$um#Dv7VMh<@^fvktzt(8*443!}?Bu<;N_qS`X`w|9Jp`U_EbNFLwKldf('
        b'{8YW{NK}tnY>5&k^tK!j=j)DM9eY{}2IiX{RpViCziRt7>r$y<u~sMkTi4$$_Um;0x^eNkTod413>!5B>eIXS0FV!E@<7#c2kJ)N'
        b'x5hq3fEonQ&M@nXk|8lih`gm~S#yq87aQ~t_grlLhOm*{VIvQ2gmymgyt>arHjt5nDhLp!KJbD{7`Llm+<oAjFnRj($hiF?6!+Pr'
        b'mc@x1vPT9m*#pl-ZO9sVFab=0>G|s3&EooA7pm1l_?q*;_P8C3YtB#Ax$1<399#U1X{nY3&qFh&FN$6mpL!#1=%=d8DXU@1<ytB>'
        b'EPEv`bs!-uq+B&UadJx7^rzH^(@4VfoP`#1!hw8)p*05<gj7P$1j6@+?$lVTphFvGM1W4a3Jmnnoe|buQhBV=9MiBh%>Bl>vRv0a'
        b'nF~Yn^!lUcHXJ*bpOy1$xc<mFT~=>S?zp~qO>Y(~@ZUE4L%Vsyx<xxftY1KOqE4H4+dA!MP1eN{BpI}X_gS=~G5t4g)~Bepgy+Ui'
        b'O_<l8pO>myd*eMVhu@OOU_AK{cP~_P|FAz~>mjLO?r8ki=b)=Mn}o>qx^IQ4AG>u=Z1UW2p#L_K8EwpLdS;Sl^T21XZZqxIB;~>k'
        b'j-3$+t9$&eZKC`1xzV}%BaUfyhHN?E-hK|oX!D8nkBdnK(ueU{UGV|k7rmdD*1RY6ZUe0XY9?$sVKqyePxK$$79M-|*tSWr`C}kz'
        b's&e)nITC;Ov)jh4>p3EP9Pc@*d-aNSZytQ(+}qFr!riA2Y}Y-0#kS~&-tG0=_x|0zFC7?slz5IdZHr!eaLb9m?mqo%>7Ct}>%9Io'
        b'pi3Ny16>0Qs@K?f-mFgWe3`o8>w}4c`spmyd3CBgVL%=Gr^&ZHbFOV->oe*#*Tc+$7-9TAjR1yThk94rrsKz5jU7?r?mu);Y&^7j'
        b'eah<3!Bk)S!Pl1Y*2B_I)%_o&M-H86m>ah74`W*n9t(duRqc6Ad^0}$%$FieP_6Yn9P7m)!j$i_)LSE^lac#2Y;zyeCcQ5GG!l=d'
        b'H3{0Oxf9n7KAklwAu%W6keJY%1CHsL>cg2N{@!z?p)d&(bGB*scuvjOE?ko)?AqIFO@&-z-yPlNj-5+{aa(^W!SXJQ1H-NqJHOOG'
        b'$Y~8s!H5($=!TK7@Eb84)_a&=r`Jgbe{wEu+)kCjb871vDSsB#A2sfk=cskG?zMw1h}JzKp1xCx?>HxD^4y^l$(|(AXSrh66XLTc'
        b'l3tPeKiGHTvj?a4-!p&BRpgX2`neUG!@`<kwuO4O=(dDS&0Kj^m&3Fo^P@Fj&2EbY6<5%}%DpZ-#ob`|E<J3Ud)@8AI6;$ir<CVz'
        b'SoTfs!SAMBWvM@x8@leT+}L%SYG01KS8dRS<fPoi^aAxUjWA>DKiEE9yh?v;SP0M6+#J4anyRlE&HW7(=LRQ|_3OXg)gAr7gE5;Y'
        b'K9C){a@y@%9(cMqVL)4Y6`HpjOy?lM0}q-Sa<$MWbFjU~!tl0(dp5d3VLG_b{Udb7340DMeC-i;CVJkVD@>X?f1{_-@RInz{r8os'
        b'2uaZ-t3wk8s6E^J^8;(OU_y`b^X+vYt3j*z$1sqB_2^DHmpn1tJ^ftrG&Q`}PRLXDPuOsDI6mo|*{p5&26s6V+S2IeX0j>%-1>wl'
        b'8j{RHj?a%a28Ng>p9>DT>Vl97!6AiD;wCBEr{+0wPvLJR|Ac{b6NNjC^q4xKZ6Xbb>Ty8|b1jC|wng#GA0=`sxdLAg2Za<4UXbR~'
        b';54Rx1%w#d(x8K>cQQ>dLEkeh_s;|ta%z6GE-*y@_OMV99QM{QDZU`#8^it~gDG)6PwBQtndxTyU|Sqbb=`ViA>4l3m=dSk5@lY*'
        b'8Xw2A`8{MK24wtPPzZKiD%$TUDpCBFHIe&S*RrcJZIer1qWWk5gcNndV1(J6m^^W2>}rxcZEkYrE!GAcC__qe`~$<r`6^M~yRU6a'
        b'HkwS}C~TX~`U}(ia=0rn4NZ^&)*DaIKkT_kg48u%NJP$~clh{4lFT@KT1uW+vtxDgw9b~ybu{gS_@4}$%`xi(l24$?uMT}z;%Nj-'
        b'qq|6&7*K<FnpR9>zDSy@LXXI4mSUQ&i=>GSeNp25x1nnI=rSBLWFm?ud-Z>eA9#A`{SWDwUeA=|jcwOcZ?f!72AzP8U)v-aF+q-)'
        b'KvhfJ4}^SlI_>*|c;g^7IezxAF*921kJ9DRvkY4@Kbz=Foe-ZhEC$3)2pythy&1&8QJY**nGx2EQoG`vp~0=jfNc_Y@~{v=^?7PX'
        b'4U6mRcTXEWvqi;jS8R#e9Y4Hldz7sAvuhUD42!=?#51EU(SZ?@hQ%!y(HIc1Ib2NB4(^n|T<A)OUhj8pC47T0Ec@lXR?)TNLwES_'
        b'K=?2vjSnC8?lWtL1L`h%zTNsQ-C%ZqH#F$!4cL@s7hcW{$vfJm|7Lv*NudZ@U7gOg;hUjYwRX>wFZ$gh>5mxratN%S!2zROQo#&&'
        b'^$?nB{~DtCzMwHYd54bY3>Byx=XdD^=>JaXw-T8?^ec%NJiWRt;+n7J{n$SZ4ZO{A6UIR$#X(g-)dzoz{RIp0xIxeBn+^oD>b0SS'
        b'LwJ*C;P8+LN)?YA97uB~4av4|{0o?QidxLLiuv~q(K|-*bwgl?CQrID{<)!bo8zAy>N_$fMD(U^;{Ctjw?hNJ8`34HSXU=R4TNE1'
        b'_$9muA>S?d%6NpAksiX%yS5GW?1PXtZSBCR-WKd0n-*RxwZfXl6_~*)t;sXAV50hP4)XCrtx$PjzL;?66doCBg&aXEOch<LYds--'
        b'o+;wI)o*%k9rUz_OIC|*tBr}Gdm|Qo;Lp+GN%4?JP4^sI-1lPO$xxwy``4oXyjHkENEepyut*+OEp!M=a9^^;9Wq4Euey%E4S9v~'
        b'bhi&tgGiVO)DPjsofh}VSqL)SHWY6fqE((Aa+cmq?CCbMWlu}JLW!B*Q;ffHC{Img1hj8z@BAp*IB4X}<Dh+&V*Mte<xP(b8`i!_'
        b'$Vm@zFQKK*KYT>yjYUI3)z_d+j0dHf)~v(*SFDD+en^-K5m37-s5FMZh2d#;yZ`$v-GX-4Qa+tGv}XsQOg=8tkF_@g&))}=dObUb'
        b'rI+%;HyDT3vmM89y>ZBGg2C_87YwCp^t0*kYVi75%n;`QjeLhGkMUEl_-*g{e?PD>d|ZFeU+>COU2`U_FLaE}wXNr+>G`7g;Gy-q'
        b'O`hj_*FS#<%&TWMM)oz4$0u%?mYOL{LQ82$_+1kw^?5vZO}Kia2kfQ?HhwIm3X=v0P96RhY*!noLPB2X2+LC+gXNZMjB{g>V-nUC'
        b'Cnr|1MJgB1+@N_=Gj(?#s!%^ZArE&1ha|Ulh&B^z3(b$|?bCkt4$SSNtCxfeMc@ei7M7prKF^utX|I%iCJFt*#GT=XzmTdlP$wZ1'
        b'f(TTlVbl4laG_}lOtVvK{>5~&C7PTG(FTtvXQTRX6-@9m;8;^d1g-v)voL@f7(f`QsW?nF93K5gXN4;uSf~=(`LH(e;mbbDZqa@v'
        b'K_c;&dYxg<hWF0uvf_I)4+txX#@MUd?f%<YU1oG|W>mj^`o89YzntCum$UK>H&_PTuc9w6lD4+zHBV-gv520RhnrqG+eg^}6jil+'
        b';gWjY2hW1P?@=P(%+wz~n->A0`~up*-m^Wg%VikLMfYATqXNq)4<Fn?JjGG81nM97?OE`n5mn5~ed_E^bwz}GC!Ipu&$_p>se{*`'
        b'46Hm@`-Pa&r;zdW+kBnIdnb<e+9SSRW1Sg`!9rr`Za!a3zdYNQK$VO{qRWptI<zlgo5A|J)G|@Mbv<1mS|+6=PmD87I@`DXMV5|r'
        b'gQ1xuy(R6NkhE9YW;p$!1iV06QjQLK!ri@CNc?iFliI&dXTQVn+ptb*zdC*O9UI7(5z|&em-qT4M87t^<t(h%@kV&lRY4oybk@{y'
        b'wnB}#iH@Y&*dJxeKWpTdLPP(^cwX%NmLx=rDWZGHS^u@tU3b>!HlI!Lx)+@tSag=o_w@-XTqqWt^(`ML)9cSdXy8h0KI>bFF^{yf'
        b'J-5^J#)N3hq9Q1Z(hIT>)&{KQ?h9_3?Vgj7_-3K*p%q5+z8ikCVDVEk=Ix#IbdmM$tT!IM#dMu|SW-X%1r$&~0R<FLKmi35P(T3%'
        b'6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi5*zrl91'
        b'N=^SFs*#Y+<<1K}AO`V-94GY8QrcY>`Ulp7;#K4f`}^QsZL8Q{J`adze>a?vM$%$wa@ifLg6W}T3r*ANSk``#^7{x`2Cn}iPN255'
        b'S_9(oZz1}_u2pZ|es13Sci(#P+GCG)E<UM@umTDwpnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>'
        b'3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>'
        b'3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0^bKd2~`_Ut;#WeK?sR}he#5>RU!!~&?cyeq5jwt#1FEXElo`peR{La;aWv5gjUD0c5)do'
        b'Wab-m`T9KBU(@6g4LbO5$fo{T8M87Bm!YqFb;ru8-+x(bt)27nw7EO}z2mowrVPJ6?e&~Lx&CU1897G&FM}4I5O_l234>=mJTu_A'
        b'sj99le}To(Y3ppw7fU)_RtLDmk~(vyK`gY}UF~*Dv(<6)_()P=s3RTDVr#o)6)CJFR!qwiF7qZNg*7$xl{Kc~l3Fse-R5$&TU(rj'
        b'rb@5NB!+CgPM1mAT&^x>{>+)JHdkBsvWzBs$4u<-a#Q6@nv@h(7cDI<t*aO7GR10rc5SX$WN|obP++aW+qZUANI_yEDb#@50q(Uy'
        b'ej@nVKTCayen}#Qo<%vvccwv`4BEo}>q#MoCqkHix|>Q%YwPn%YHP74n5SkQx|1@pXE}QuuAZa}z0L`5gOendmf}-UU0Q=_OBdwJ'
        b'?SVc>*JbE4^!b>eyri<ShB&Q`<yJ>e5)eBvd38;7Q3;JV&95(?O`6(m(AU0r4CRGGnxd-W*@VVnG&Dc)dXiX15~q>G3X)h&5*Lz0'
        b'D920^%@x&kB(bifzP_Tm3|yv4Q*9MsXjDxt;G&wUDpPfF9f_L~QV^yIDTst;JUmhGOoS&Ep2_gU!IJ<_3OojQ^5H3jN2fPr&dSQp'
        b'$<4DYYihQ(1WzI{TU)r-L<*M_vOW$6d>=gTL)b?*=NQEw=NPwv-wfCV_z2*I5Z4P&%u*PS5>mL2(+0zv@I-U>_3+5UeZnt1Es&&9'
        b'cJ$J>s!`?dKc#L|`}vo&y*j6{0_ssl3Pq^P(Na=43+hv9aar2)#fnbg;Vz5IwyfPMHal!EpkfN)Je@Cg*;hb-y;F2r+gs9IR;No$'
        b'G1t_kiY*pfyR|tUhH}2Cwq8%)2KvsV?^#&>L2XFEEASkH=Ph`qKNeEZ8WvKp3Z8r68Gz?^@VpAoNqBVcg%rH@-ysEaNU7D@EVkL('
        b'n@Q2CCa9UyWpTJjVY|KQR<YUIZgp8noy*=OHrt#Qs5vR=usT|;olUDCrM-)o9rk5bjBK)Zc3PWUq{{BHJD}3t?Xr6X6CI?|)?srw'
        b'MLRUyVQYqLArJ~&hDGswFwW($EVs6^0J2c*@XK#efNybtFCe982uut9#X){npcnfWU2nIyJFPB|U4Bmg1XboT$gSCmV})&AD7ItU'
        b'#131hzZ-J*`YbEK-DdBwaztzBqgoU|waAZZ5u;ipQ!VzRS{y*N*pF&4qgpIe)pglAo1wGeZC&a0b#+7Ih^c!ego`@ap_d&7*^wzb'
        b'X335$*^w<fa%4xY?8x(G=*!xhx89q%-kZDLo4wwfzusGb-dlp+TZG<QhQV8g!B>B883tB{rPI=GZ}m0S=hp}M4MF~3`dLB#tRR1O'
        b'kUs~8-RZJ+k%b0^7jeYBi#g)ng)pNWm=@6@_GX^N?9DuNkhTk0lgbX+=M=4-bfzwp9gDpoi)5FHm1CmWn0%o=-ZJ@dlZkPYDPY2}'
        b'$z4?Ebu9F{7I|HZy{@WEpL3SandNh4`<yvm7PWVJolsSnY&O3T^MWd`+u)znaFN6Yn!L*9bdl0_yS<r?kiFZ*c>!H|ugl<dWqMt+'
        b'ysj*-E8FYJ@w#%ot~_7Peuel-(ff+g`^wS#3ex*Z())_i`^wV$3e)>aGx$m~__fJbTHt)}b%I}jJ~+S-9B@G%vw{P%f&;RH19C`Z'
        b'NwHW<-(~b&NZ$+S+tTc?I@z)l=!M!9*+FtQiM3V`&$0)VQ5~tOsH-7WHFXuF&RiiDRnB9$PRFsHV*|&Tzz-H@8?tg;vDjpBH2XW7'
        b'VFd&ck4YW0EOb@W-UzyGkyuwWkKtkynP*+qWod?aMHem%<<8oLq<$f(t(%pbCDtySS-;SaId3ef5KZ)5NZ))xK_?T{4Pbn9TiWSL'
        b'FD_(g5krd^s><Ye7ROl}XLFpxb(BAk3n@VTB{n3a0QD9TFzUgd)Pntkx)1nK|IY)AHb5z0v;*b?4hP%<80{tp;7HVY0FMK_9x&Pp'
        b'4+Fje@NWTM33xByD8PpRqkeT9@Fc*013Ve<7l5Y#9s@iT@D-t;H)8z&UjsN5FskRX0ACAuF5v3`F9s}PeE`P;b^%Vn`T(8=_%6VS'
        b'STDdyfFA;!40t=>>42XGoC0`1;8ehe0i&JsCScSHPXR_f@H4>afWHBZivB2I6W~bDpHRV^1h@!rJm6xql>nCj&IDWvxBze&;1a;)'
        b'fU5yl0A2uiE-IIR=K;0>uEc%?Tm`rXa5dmHfNQWFfX#p(1bidlM*-JjKLf4<ybo|a_A}u5fR6%h0Q?ug3$Q(a7Xtni@FKw90$z;$'
        b'4)`YQ_wbN{C4jF5d^6w-z&{3j1K_1tZ@{Ps{}`|Za3|npfPV(K3GmMWHv_&GuoduqfLpNN0k;Bv1aK$dCji?4?*`n3^#*(!;NJsw'
        b'0R97DC*aosug38Jd?(f)@XrCC0lWsVCL*NZF2KX!{{`yt;BNyg0CoYM2)G~cWWX7K69CV|b^+D_&IddJunF+(XqN;23E+i*djKy3'
        b'{8PZ~fPV&fIp8}0y8)w~zYee)@B@JR01pCQ4|pfw4cIQg8v(xtcoU8T;QIjo1MvNT&jS7x+S-vJ1rH!U0p1Ka3h)-dQvg4R_9ft7'
        b'W4!@C1UMJ)!+;9`{}<p&z`p_90N8{41b6`OEr17cUI2as@Ew331$;N)t$^<b{NI2*fFHwg0lW?81>ncgmH@mR`3Nv>h`bGW2jC9@'
        b'?*#lg;NJos0{kS72gsFO$VY&81HKOM9>6-lPhmd;-V3-E@b3UO0e%|m2lyG}AHe%?J`14*&jS7x_@6`m0sK7nFW?sdZv(s^`5y4^'
        b'asC2+5%3#;4*-4-@Ik;I13rZH1pE@<uK~Xd_#EIrAioG91&6WU0lxxx0^lRq?|@$gJPq(`*zbT}2Rs|_QNU$@anq#+@EbUf0sj&3'
        b'QozRncK}9PawTB2HGcy5Ex_|uh7|k>=L`7%jPnEVUvNGHejCRD@H;pTfd2~kcYxo;_5pqm@XLVT$9VzxB+d)Ke*^q3;J@Rz06vBD'
        b'8}J9%Ucl9M7btc1?$$Q3&1&fqTR^X>Zm1KNb+@!w9r2_NY#K1XoZ<?H&1IEsOt5fqp-`*I1hra~s8*}9)oM+-TCH8IR)@5!)uBIA'
        b'tHai-)!~C`b;Mq^I`XhuJuX?JA)OkH>KToet}{!QTiUy=94&QNUEPjOYcr{;D+8&zFt;EoW)jhc6M>)*Pf63wG8UItn(GP5Mjg#T'
        b'gSL4X!A>Q2kTAN&i!QqeHYU^>@}8bpKD}pp;=<_|+TBSl$RbNOE~)wAeCmf1OQ=@cOp2N53Knjg6|CA~yWPQ^%p@h|)()|xvzb6a'
        b'pn&4$R<o5VxlX?zC(|QIUAxuVh4yTqB`l_kU_M(MX`-vm+R1c<fI64kJ20CjYGpgDw{?RO&<y4$s5Cr~n%+p`usXUs#arylpm-QA'
        b'D8mZD_I9z|+S%%A6YVW6m^)Mr+GTULVek4GxBsao7cEnc&44mHz}5vVZ54!fH?@gf?G_jMo5ilnQ!-ncF%y*TSS4CoEw)aGusVPP'
        b'J46fQfJs)^pcRSr<^^Jl&Ea&#b4rMGF~vx<09p>kHfLPCx?OgsjV46SrqxV`Udiy^ym@vC(|4$QBGY*gUZ2SH9)!P7WV#Q+R}-23'
        b'gD^ai=|FTk#4tSwVSEhJg%GC1FntIiA%^Khbl*6J=|u=-F-(U+Fvl=GiE?!e)0GhJk74=}!rmCBGa;OeVR{on#8qs~LP!DkMDAV&'
        b'?ijw8^%HPk#ls&0cPw{*TN6@nHFxj33ftIBqTV2dr;d@rp<}+iG8KQTIo9~?3lqLKtWvT4VZ>oRA{qT4xRTPTNED~PF7CQ(;U9gy'
        b'a5czycn-jG=xWqo7Lmoobg^va96MS$JM!&Eeq^7Z$-nxU8*_L3;j!%fIiXqizu1tu;^-6lrCkv^>7O@cnA<I#onS3987Mk!w*w<u'
        b'oG?L}yPHt@CC;5qh*32@vW#uYiTVtEi+I!Y#OWe1*>t)`I-N3Ho3*`*?(%}*%1=xb6Q_xZWnyB5m{=_)uAB{$4_qr}x7#|cBIL?&'
        b'U8Pw}ED{qJiizc7VxjmmF<zV_Hn|+_=_@g_baE5e7S+X-CHVyAFrk~T`6MARy~y5dO-M@+xztAI{7w*Deqmy<)!F2*b>W;yz-?bj'
        b'6v1O7X!3|+i_79#)n%m)Y)FU26>*UaBC2fgSXM$l<0I1nL~;|<ET6vX>P__}`NcK!>wEnCreJ?Xbr0$3=^?YLXPU65XlsgUilK2g'
        b'(d}gBw%-boR)@px$cM7VN7h>Lpuj61Ge{b^1A@qs&Ly4IHBg3V65G&3V-n8Zg7S_^BZs}c9Y)yZ^b(1d7Tm*YYO{2<Vq;xx5b0zs'
        b'&wzpxi3prvS!r{2Se&;~4-^Vgw3E4Qt`?iMy*WR?C$4A%;Vfr^!J>|Dr8sF_pkgjYQeg(`m71>vw}Y@%P!nrDx?ovg*s>BZb^<U0'
        b'+k%JDPa_e;*6FggS{<aN-EMIatQc7-SAsY!%{Ke8ZkNm6=_IzU<+Dha#pzsOcQkvmDXXoSZ^qH9sjbf^h4nBjXc_`aGn3pLQe9G0'
        b'RY&w0Swsg<DHt{54}y&~6=d3rU`qk^8+aU8dL%?DI$P{eWAD)rDWT&il49$!ZuH+|t}TRO%WJA|)axs2unwkL6L2-M1-Yp#OAkS1'
        b'B+r2H`J^X1O_!$Y!L+rMqSgrgSC#`$E<6SuzVz_Qqc8O4VPsx5zVh&u3;7ixQJw)_*%&bk)6K%zS()&{GT{w@Rro+oRgknQ6Fu4Z'
        b'f}*M*brnsLh4ERL_=3FZiC9X+I&ys)NlzoD`l8u-hIDD9w9-^pPD-J9q@=`LTT?}DYAC7AM<J3yZmKau`))EVtb=!T$pZA2RL`%f'
        b'ORKFX*g<Kex(0{}!9h{oY+^1-BekVzq^2&76c(qE62Mhv(4s0$_2rn(TmcD6@Hj1v)Inrj38bp62eKklbsD*;w4%0ZfvL76pPw>N'
        b'kyTewR&A=J)c}RCuD+($REEP-T3b>gR+UuM)Gh*Facu=wo)}40`R%e-gr}~errH}XLNmaRnHAQUYKs9^nHEB(C1$Y}xrK=3x6@Kh'
        b'^B0O0IR2a^i%aT?Ao~PUy9M+DlvOw{mP2P<k5Y{VSK)R~s~n?C_r(NBy9CO47i7aiFOmz32+E`!ggU4aUA87?K6oLwjt)?IoamPI'
        b'WhxQ5M1$e3FKH;LuE*wAR#a7>Bfp&FS2C8zU@p*0s!`e@OT*~olWM!HO`?QqwK+jHfvm$!t7>3CV9cuN>}TFm)BH-D993q!6VL*N'
        b'Ottid!Dab+hIFK-7~RF-Dj*f8uGV&Ul6(VbpD4ZN+FMZ%wG!Hk`3x~#n4nsm&$L^5>_K`8TcCu>PIwj9LuGnO>+l7S8N(J7)zCKv'
        b')-1=mz*E-*uX1>>zGlQYk$WmS*()9DR=PlDN79p61hu^Z+I^hVme&<m)|b?jR*5%?q8V(17s6D9$Kg3OQC0ZaHLAk6@v6e|397;#'
        b'f_v99J32^5$4uO+2IRCh{n$X7t*w48jG`&QLuPOww&s;$fmpp1q*-nKeDl)Eis}+FvjfyrdcHi9OLJ#N6C@Q2W<$~<=$U3)CupN}'
        b't02P;C%NFPmZYIPlWD=|u{1AjLb9dJu+;h@sJV5~7)nCb+wQKVs4xT*1;pWAKRdpWZ35u#4qKDM4(+!C(`GE`ghkxe(cJ;IOqUfx'
        b'@N5wmB~Y@PU`7D{qec(QAZP@(CQEz!D$Ii}Tevjgda4IC#E_Adfh%r(o42SoSkOQPUuKn6C$Yt0@1UgIZW5{OhgoFdBH4*+TLwLH'
        b'fXu;`u&!*vV@FFDRA!|Ov=A$luAik7Z!Nz)1C3Kyi$!Of9dvy>n#6-h%PN)=+FD(73AaOiTw?R8P75@gt>$=~Xa&8-%8x6l-Nuha'
        b'GQ<X2DMMD4cq=fulbvSB$0eX@RCMAIA6vR<U7fbpPD{H}Orh2YwBNoWH87cXC--}#<rR_7ep#_HU4~d?ce;3-Q|xwvXz=AECuZsl'
        b'w#tSXJE7nVpE^|0a*=YNV?asb3W?LwVGS%8xB|L<A@Tu~8Po}=5AkClTW43d%UjuiRLrFFPmtn-rZekX*2kQ9`hr{jn98yoOhn5v'
        b'Tf5D*3hKWA$F;H6T;)s5#baPy8?ly6D6EiofO)GjQ8BNYh2gxj>U5$LtV>Ac6m6&!w$PMy;tgU@Os8D(^jb>?<tSFzbpKMY9%6SF'
        b'&4ap|?JHoC*q|FRm8HF@8;xT=0}?ayX3?aHS($mL{dHMst=d=pC$6DZEDjKzz5JXF2ZYA7;)H}Iue3V-hPxhhST7%dP2Jv(a}p+1'
        b'yA4u9WkKa+Ml#G5%-xrmR##SB6Ek7XK~-&_P=c7C3nFj^$|oRcYVU4l*?|Odb>oWFWyh9K@zKJ)BGsomU2KxJ(Y+3+E3hOiK%%pI'
        b'87H=R=bK0m7gu4Gy$yBRI=b3rj`HmW_%+&WaX8U<bD<cKn@kIKTDvR`CP|pG&*p+(m1&JBze5jDQvmvtNt-s9V=We#fP85Z*-1YR'
        b'mxJ!2!LY#CbW<LK(Sb_Al&z$9Hkhn)!Zf9fg&e|j#Tt|uXt8CPqQ%jK**0O9Tbi1>!3nLmVB4WSsK!I5Q&T8IEVQnGNsAT^jMyp>'
        b'tP*G`D+v3{3KndWOYCCXDwfVBt32P3BbwU8ZnXE<Sg;K^T4?7g-@XY}ippY^tE<gI$FLJDEsM+<P8J!+ynK#cT;R#W<bQu8O{|ew'
        b'3Wax?SVAw9U<KH=55GEs91fD(%YVFpv;c8|b>sq+t!ps!!S%C)q0a`p15~T;BbmL2&1pd1jkngCumLM<PPXrbvg_j6@V&*0_6)4g'
        b'?I1fq4%l!L5g5h{9Np=%(ZyCa6fqT*DsnoURJ_UU*6-7!w2Hh_|2I3(zZp#6{~tEO8Q6+|0@(EC>rYVrxO9BK5+G$z8S)Hp+FM+#'
        b'6<m-z>4qa}NS3BH+>2qen@M%5Y*3?uP8X({z)C3Avb_VREX@dAExgjJqr(a_mdcwpOS{X-#RAO~rN#=Bkp4Ma<esIg5Y@aKw$@gv'
        b'`im7PUL7`=)bwHzl~Sx+ObD~qN$-vEjC@&uMh3P`v#;@Oe%s7`ZSXJJN_9b8O}H9o>2}#c3FBHI-t}mvB9|@9CGr|fuWM1ApoyDC'
        b'{ws1?Knl4U&;=;UnV^DhTeeC}EH7Y+1-(~wgEuq3B2De6^gw8L;Hsa-YK=mQ)-tH(d^urJj2c2|k*FwKw&2DZelJbLiN;!nOOgev'
        b'LZv6;EAMtXzYr%j@{N6ar^r=w@2*p0hP><Vw1V`<j;C3A$B%2|R3<O?(+e`t;A9<%yGl?R%K#}lt*w@z)a();mFAcfDoiI1az-G}'
        b'VYNYiI680=;PimDTKIlDE=Vq_s?=Gnw|aAfmNeZ8*|pdxUk7E#wQVXy+v#e^a)c&#ftg?pQs$W+zs%}dVTEC)DV%5}_%p4n*n4}a'
        b'*}4p5auYq7!1dFGUGKt0PhRNRG@||NYbVHV)&n+IhRBD3Dhzl&fs(^Ji8`md*og_wqq3Y#Trva8Nx@+Q(a|L?13T?jdP3xYyubl#'
        b'fS)l&8|Y(XWEE6AQ6{wGDF!UFouYyE7h896j}lsk8df*%K0suE8Aqys3($&_*C@~_aUSrA#V=EW5Jxtb({#0Wx7s?9n45tAJH!_>'
        b'A~7>dOu>~9uN%_Zr_veM2C|e35<WFr5wQia#n#%5`>&wgXOKz@>TW3D@&gpAGW|@$%uMfmWWz)!IS5v6_W8GfNd&4CLp3WcSQg8b'
        b'&Q@y5AX}B?q={v@X}CYgl(4*<4FAhxpa#QC#Us4HV6+<e@N}Z=YC`=orMVkcPs*aHfyur7@ja7UR{rPYvNpb=%?3Ow+px4#{A7>M'
        b'B1YD&^BPS}&>0TKl1?lFIC{Cgy_*ROd8J6`MBTAHLEaIdLaarclP1Q~-ufB#G0p=ln3mLqhi{N1F<mwta9Y5qp$>uOC$CpCJ9&iH'
        b'Dyory9fD!95kd_`7dK;}X%?tEJ&6@>vA6oT0Mg6r^$NS=R%e$5W+FX(VWJ<cA#Y=#YPWhtNSZ8xec|$=g#A=(ZK0XcuB8!F`{j!i'
        b'H)=T@Thud1b$7=yyaeo(Rk+D+MYEkxF+JVDXHG+I1~KvFm0rMwfu;wYvQP|;<YwO`VnKCrTr#r7-tBO;d8I9iBIw0dc4BR1hFb@U'
        b'stzk1NaO}+K(`B1<0|{TQ<tKB^u1Hhg`xDyPiEUu?ZD|*!=O}rG4ZbHl(RGZZ!5Q_<E24*65Za7n^ay}tVu^kMQ4-4irk3iE04M`'
        b'gPEKdS1hr`yL8elaMv({nEkm17IhG4R7LCPNW;?{nJt^V8-wCa=`i|BnO>PD>TdSsLCs2eHD!76b<5izzmnN~1FvjmV;!)o2CJzH'
        b'r);ak(g9N)w`^KFk%UfB8#FW@+wK500k1FGY1dO#8;YqYt}NlkGvrI9rFTfJuBHspB&*XbJHOL3-1Vcm(FvRpInN3MDH~fXOVA_i'
        b'U{XN&b|$I7@T9_2P6n&4PXa;zV-_g5fvu?~gPnaV6x-ZQr9+GS+XQa8qw>`aY)^MDyphQDD41-rwoNr?*2NYmx}Bd8LLu$m5tsW{'
        b'E(&cDW+OMxgf=oIM-Kd9B1vX9=c>*o(OgkX1wK8(11^BH%)}@4%m#s~ammcKSa4&K%_DhU{l}!ukh9h5Qx%ZeGQ|0~u>fOMrh|Yk'
        b'8)I_p=q9is9Tui$&X;#yxbf13XXJc$6-SV7)Uy33cwn_;$_ywdtOmYf*<@i=_04=7DlRga!j&Nw%PJ_{U$8ZM`_$K;sA{Kk6AsI3'
        b'^H-z2xkKSK>?(|`Qaa@+gTJ-0b~=$O`S|#1KsQPF4vfuz#9(4Ex#qHC7f}t<DKF8eN;X@U+nByg+r?*L2i+*7niW@obbgC8+XchU'
        b'<VL7p=1hHsVMZxH+u_s0s4D3cQxY@t3~6j@5p9^P%)C_2=X$#F>9E+GR1aeN1hy8w5s#WSJLKjyf>60A`Faz^*rDTPp<PWi0<Rh+'
        b'O9sjy)STisg7B&hHBmaPD|}l@vc*MJ$Eu+8`HTx`k@PMTQ{cSRX;f*GOT?Da>p}AE9$MtZ@)eC@Syo;~=6}xL?+O5wev~ZmBGHA7'
        b'od3NlW%4dr|8MGLxiEiPZZX}#k*!a8(~gcb7M0=^->_iXK?J3Gw@mSh7g*z#rdwsb3|RpTDI49C@$M2b4)yg%!o}K<KzAa5yJ=d8'
        b'_i9^dyfx5<vP_*X-{y-|+$Tz8!5g4J_&Pxz2w%M}X94@y7;Hi(9X&rg*xOzFTHW_Ig)frxe>RBCbkzq2amd1nT@_&_C%t<2pEHrw'
        b'grI?{%FgFD0k^<pVPbRg5qH{|vKw$!hI5CQLL20=b*0kXDfz$%ue|tbRFy5ShiNt@*MbV7dsnP9&RYCuXmVvK>lVrUj_l$>?(nO+'
        b'-;}{EbbrnP0UX3*e!E<Lds@C-EULHiBL(PtDvMColx5~-%z{O16+dy1B^@ek0ZdPdQ7G`OBYFbLwh(;Q8<+(&8drL@0$z%!Lq3%C'
        b'YNwY-$7h0HI<}mEM2GxmI%GYu1#h~@tV>tz&UCQ#fLo}tZFk@lNU3h9!_8_d)dXE~PvPY^JLpcU(x`so=mIWe%bOF&%T6b>1Js4('
        b'bVGfm@6MFd&jiN_L-pWRoH6vr-#+D1<_nkIca}z3)oE$5g2l@;O2`W}ie{YIL24cvVi)8p>yz}ZEV~o>e<9Zk>zV=UCJ^f~vhXBa'
        b'=cG%ycPpa1iyed|$a+J9*wWqE#CG55R=Z1{NA$!H@?BxExx9AHg^RdPcci}qVkbj<SJB@FrN5bVdiM_lE;i!P26P49L1cmj9aua+'
        b'1oJ;MySTz4D^)f;$m<5Xj&|An`Xb1>g;KC9*J28)D_o8zE=;}1g*&QvyV&+A-(nL>(&<qJTD(jgkV?$V&zN$uYZmPGu#-w;TQjrj'
        b'yvKI`VeIHB-2ea43);5fWzh>0ZN7~ei^~NXFH-o1w6dhQj;ZwyTbHQ6bd<q&otm1Kbj84a;O4d6!3^^<L$1HX1w|%*NhjW%g9y40'
        b'&bPsJG!)(hwHU~*8zz?g>o<S)yWnO3-+~CZ7;x!{O7jUGk_=KLANgAXEI@l_z=pe=F*~>B7aaKI0LYtduF$OocEun=#QQ4zoXdB?'
        b'#nKF`%FhfPd}*;k`HiKvmDD7}<+xGiFK-AYWXI;54XAP1!uGvj$)Gn8TDyT6m|X-R76%;@+(DgQYsEej!H#o)-U2Mo58$WcjvVbx'
        b'Z$Z9D)=C=~Fb*5lMrC@c1@Y2Y5kFwAV?I^pvYDuOSuQ#C{ZfE-*ezR)ep}p_Kk?tAW|20p%|fW@Do18#Wo2gh)6?E`u@K)y2p-CK'
        b'EO><3n5H;W<#@k4DNZ@e?;45|xCPd-CcK$J%6yk6E-a58?8>LV^xV|RcPG;R^L>;w`B1anyRQwiri&l6rtw`42fJN@n-qRm5#++m'
        b'vR>nNI_Z;yX@&f*I&QC|Rbpf(6${QZs_-UryVJ~XXIRq~*c}0)lqm*j^5K><O+Ip$Q#ie4;C2O6WI<64p9N|Dmo3uR#Y^u^j<kS#'
        b'9dcv+Zhv6!P}L>fWlwLlr<JU9;c0U-naicD&zdIF5Of(josO9BmV|5}gPzMSmvqu=4OZ`9%SY{jEFeo8#xLGrugGUYifZ89-Y;4N'
        b'=M@wiz-mEp0W4SNck0Z4PhXBAG%$!WSDo*y*ULpXyO}yhnKj@CL$c=r2Ik?^KCt>WGrc_;cmN5A+cVzqz%w>Jg99VGWQ#>sM(H70'
        b'@L?Qwj(h@k@lz`TQ|jVJQlyF=dbi;AA={ebTM=o#Bcn9mInTw<aCn<9ev(7Ds($f<n~R^%_`awB5)!Wr%7_1fAJ7OsVG&cz=Gs(w'
        b'le690iuZhK>%F^(7dh+jZWgn_=1fv-m45{Vswf?Dn@gT(^7({!ACq%&z}7Wcn6@Zwu{@gW#DeGzx$F>uPgDPsiNFZ|Q;EPBzY~d|'
        b'y!=ihyjAh;bNg5&IEJ#M9LhGyNjm4?biEGY!VUEcH_J(#pZ+h4SbC*do`0pjEoG)}kU$~Mw}UZ7nw-7Ns<^;ku;I<DiZt8|!xaM;'
        b'YtG>*xOv*;qVt+%UNtL~l-eEixB@tUs*v=jZ*(N(>IQ5dr=toS7*=tSu;Pn^$y?7AY{!|T`)|<t_LBXC@3d(=QHS47G7qx&?HdQB'
        b';$OvKfz4iXmMuLboym0=MV_MV5+W-g_5yiz={;I{TV39Uq2htdj^M4rv`g(Brd?+LE{&hARAmR06TCwe5P3n<>H{{4f?5`wt<@)R'
        b'FNl|!<dXY8X&3IRqy=q&VCycv>u~8ki%aiPc;^ppL!hw4Uo+69+ixlJea(fh4@L4yEe90yBQE(@wn0DEV+JqLQw^aTo6hwDru`E3'
        b'o8MsTlUbUCo>b8e>Et%maw@R#XJwbNJqZrJJ`LXn`pyKY%&a%Liug$qZmsc7@e4A@LA3MvvfgT^`@0~3y&Zz9D(!$$x?jT$UwN3h'
        b'0^>8ZoPpoe;(@Yo<H<WNk|f{<!k3})Pe9lYuVq15g!Vf>>5^~rw)i*@e@fYIce>J8IyU>AUMUFdk;<d^?w%~Qd1%0~ocGg4T;XPY'
        b'lm(+-*S*XED+a2<UL6{Q8D42=p@)+&@VJFtm6wa^DNpN^*-@tPxBAj9Wu?&%eOWHTZW!*hj!0(iES)Y*ug@|7GGyw|H!EA03n(im'
        b'8(20i&!7hkbpVDdvjSg39z}t-MSU|&o*Xih1W0v%X}}kDc?FRd$eDhNARe%{GV6o(r?+33X-v&MGc)&KAxDjYN@22yp~VcD7~*hL'
        b'WWTF^Jf8igIzEB@p1M4N{g&F5z<x)aJdOQ^x^f!(owR)#`|b4464`I1uSsIRlfF8c{YJVYnf*Tc@5$`9(Lb8bei!}TboQI*D^l3+'
        b'q35Tt-$KWwvfn}fG?o1Z`h!&V`)AV(_S@&b&0xQK?oMOhop~>feRn1`oqcy^c{=;<%%ODl-I?SJ_T8C98SHyAPiL_2&3u!=zBki1'
        b'lYMU{Ovk=AbFGejZ>CDezBkjOW8a&3LdU*0^MQ_iZzf#NzBlu*o_%lT&wBQ~nFs^>-pp(R``%2afqif09s~Ps$>Rq0-IBwA@mrQ3'
        b'0nWtlRb++~;79+AfU}SeFn&?=KEOE~=i+a@0prI<hXLo~HxFlp6#NLs0dN7}t$=3({wv@c@cSTH_&q?VXBPY3&AVCbdpGKA_PrSV'
        b'J^f7_FX0%!57U;-zW?&eZ1(+^=d#)NUOoW462B*!!@iTUFo%6t<j*<mdmuO-zvtso4-7RWH>6-b;Awdw1r2~7`B6y00>CE$F9bZR'
        b'Af#Xs;JW}X27DCoO@Q-nfcgNo1HKvX1Au!0zX*6GVD+4kf_}g)bMX70guDRwZom_aAqDpUeiZO803QVW0pL#ne+YPnDWu>dz{P<7'
        b'3HU+4Q-R^%02~H*St0Nh;QIhi2K*%8DS%%Cd^h0uqL6~$05$?10Bi;PDBxcK-Uj&hfcFEAEe<Jo5%8Y@9|xRN5`x1+khcoJU0K5B'
        b'(O2c*Uh(Q2`M3DSxvIjC7pVe%zmGJFAib@G&8-hBSYFFZ*xYR1!RTdBbDADrrZ(uu^;pi4IjX|88ecgYPV<W&K%?a}kNyCf5MI{H'
        b'KY#}N31!JUoCf=3ajvh;NF&Ts7517{g%8bRbYYzCGfqP;Qck5QkS3hB=d52jA7}Z>!FnGt2GT_Ea$-su4fcIXsjp0=0mcuYiR5|T'
        b'QR*w_{$LtjH#uw^PuE`-Qt-#?81MYL%twR$XnZ1&4+Kv0-<P2&4x$;)Y4(;~y5C&$0_%1KZ}%U{eC_#hwl7~Ci%AOt``}8R*L!|6'
        b'8GbaF-`7EPi{gF#wI5AhcHsDY?AO;S{tZ~nE28}3bwir>=LXho0uP^FesLbvT!cp_^8PL=zci2D7gSCR&ueM<rTh9o5FcE{X&mJ~'
        b'e*3u}J@$25VIWN`=bv4EG|rsB@wu-ekmhPmv%mcN&(leq=FdR$Cg-=${pyA^X%&I;Z8E3%?g!9J;WSrN_+;Wo6@h&HevnL@%4x2z'
        b'xcFS4?O705P8=V{d6%HUek>2-(QCL2X{-p8@$}m-VNADb4656;oUhw~rmy1S^E8~($h>nMr&)6u8X<^A<n4Kg_Z9NdZz}@(prAaE'
        b'58`<_uS2@rYgjoSR0Q@xR8TnyoaSRlH^%FBM(%^SP}&DEK{V4iP3YW9(@YAYN#rzfm!XLZqDkUq8RmZfxt+|*na636kNy$V2j`yf'
        b'm4kgeo%gkU?#1Uemh)}UJWb)UbnRtmUJjy3<ud!BxxTr*eQwZNQWQutgVX$Tu8$ACnH$)ip9b;h^}OA~JY6K8bNEe>uz8HHKM0~p'
        b'<22*uegD2r=QN2wfF^^}-0%ZvW^$SZ--AZxom}2;x6Sj(gD=Yi`)yrNALMbGd*=D%TQE(35KTU(8SpD-7r6J$^Nn$D5Y3M`&4J65'
        b'b7v4u0q4;-=UtlL8iROeHZSL+dA@b-d{*GPy*_Bp-N4fgU8bBDiUQZhIh-b>(pS#am4STyeo)<vJl&egOPAv*4x};hb^8Ioa>nNb'
        b'>IW|u2i9#dUo#)$G}zY<2dxVa@jmEnW;8c(n&&S=;|Zc!!fF0^8Jb6fXqIxCe_V!UM-WZ3{Ehsokb-qEmPj+HDsWvO3w>)N_E#sT'
        b'NrH60;WWYPX)w)7PLm5X_kT~CK29?aXde5XG}}2%W0i0ItN{1Vs@S*lHGVWWrbx4w)AaeZ$6v;)E<*ErPUHCjH1+&jYrn6$aLtnW'
        b'Ev3{)gJEbtqn+{BDxbXmv?`G1+wwpjZQwMfYF{6G9#qc4lE88naGD=iUtAYM-dXZQ;M`uwX?}7Un#LfSMVw~yWoVj%Xclvtebv5s'
        b'dbB#QJ+6|#KEQnhl<VVb0{i-<eIW(1esDZURxRN)(`qiQ^Su*9b2F!zeHofR1<~MM2DV{A&81~kPmrv_eGk-K>@~hV_#oIm4eA5j'
        b'BSCrn6QDV)_UWVe{jbD0wr=0IBT#;?<uvOqLL=+2n}cZX=6rpra)S99Y3|`P57+qk`s3w6vbQ|Yp8Eywx1BXUT@3d_u7fgOs$q4j'
        b'_0!2|A90!^5dVv<%wE8GiadZcSk7lgUtgpDBTn=FWya^Dp#6i>oJWT*LlYCEzx|V!6KnRfgUx}w;|f~0ai0qN&1k-KzdaNr4{%Ql'
        b'?OL-rP=7;r(XSbH1o7x(PSbQ58fOp<?v){rE;nDAM^6Ru=v3aGb>{ESJGd8zdH<JRIZp)XA>BcB!+kr<>nZd1*ZFXdFXS?F;bL|B'
        b'C+~y9KcJj{aheZ*0L{moX6y&he8Ooa-T3`!9_4*)xY5_w#v21=@1!7EwT+jv^G4sClX>URjclHN5yaOo@Ny3OmGjr&a)R{4{hVg('
        b'MxSmxzBX__q&G-U#C=(`fii0^Ee~Q$f%4!ur<qsln{$h51K0ZApgAW)AEaxX%fc|-U4DM7?=Ncu+c+`CR|byHZ)yYeoyYzB$d9{g'
        b'eYzgD_gTMqlt+jC{Mgnv{rsqt{MFBoa{mKAKiZ@J_VeSIp7-;k4IWbG^J5>y)cM+ncB9Ds*ULJipC9eLG(SJua+!X9wA1pr|LO-u'
        b'G?8ylE3i+{{OH)xqqA9w&3@mhJp$@{c@cZgfctj9=Zc6&D1)$<SQ_v{y583xo%jDf-Z!e_#s#kiw-+;`<)IQ^*b&Y*2k!8NeIGZu'
        b'l5SoT51K$m+*6aFQ_gs!Rabh2BJmvHbu8rRk#hm}&iUbA`$Zbe1N&Vxo})!+H5VlF`;hQ;z|xwaeMI$TN?6&hD!db(Gg;cgkKq}D'
        b'hh%F5=2u-wZH1{)tgEjrF;$7CqWX%45>j7MSzS^e6u6+Iu&$<P-UZ=>mGevLYijDtgTl=YTL&I6<A+s!vJ(HEnGT+EUJoPS=5?yV'
        b'Nr1&!>{$u^|Ha<h05)0O`{O5R(if;&q#!EF0|K^K`bMFZ1)8KuX|yj{lL9K<G&CvAY?GLzP#jl_qC>?A)lHo2TAez#u`5&DoVv*z'
        b'Zq&Eoh8x@1#+=^kcHJG@aKnM?@AEz9Jb9kHwA5{P|KI)p41D`J=X>5?pL3q)d%kBi>~0WYog{MWOv``Dk1i2-9u>9)wUm$1{305*'
        b'=uD9|Dr@UDZElf@*V0tbiLdx981C;2av5ZjoL?K_0{w9&_3oBvI(AES=YiEI{rv->-Vl{MstTc!-~a^`M`zUlWn9{=KOB-8N2IbA'
        b'5*c7~+r16SLRCFnSAQ(V1(rj7K~joIuFEVgPg~uR$|_Pz79^MD2teWq>An+@b;)bRq`o96$f!C+Qj{l2A;*%Is#4X1?x=cHlY?Y)'
        b'n~)@z#n36X;Aeg*lTCV|dex&&B@XxGX@`qYArnv2)<Ejkgdc}i6=Qm8_js2r5OI-sLWPKvw1g#3)2ZI(YTlA3$um67*LxDZLmsnV'
        b'N2e*q3U*PlII6q{SARq@3MpC5@JBApW~kgM3mVml8neqt6}M#_6`5+1BqgP6wA$-rEM+381Q(aopW#kDaCXL|xfd<7gqLgeD)euV'
        b'zz8Xg<HxKOcwlo=e5q$wh{;1BBAAz1xP?6W<0QVJs0^;CM;?%ZM|hvB#inZ<d6J*pmt{>c5KQ<(QZJw`7i`R^=+;I@*0|z`EUD)<'
        b'BSI-(!}Ti(F<ZsL#eR5Uf&-xhlZSoO7HC?{nyz3?SF$FLhe^Sh^yAfXV&NLowG8!W3U*O)?q=cE<!OE>lhTDr4Z0rPET!tsEmL~>'
        b'`}`z==?`#8Ce?3KR?n(<z2?2yEw3omG!Zawb2}3!BeWBtG4&P(=5?=PLXwWV^P3TplPeeAQbJ*&SY7lx*D{Mxb)rsJYx_gJ0q#la'
        b'Kw+*+)EI(NL_SMY45LV!#f6%wUM|?wT8aO<(Zc5zoeu@>Rro)imn!D8>FSINrpCcrk-;oeNIAaL9Z$zAbTutx!YC1hb*>o0X}lO@'
        b'$6ObS^he{F4s=WGiY)BYM+q;gW=GAJb3vBk>9eXTh!bh6D$p6JQBUcQ;+#$iJ^D)(eyWT$J6EdB)k_k9sk#A`;CggC_;R(dw1=M5'
        b'JP{&EU<dQG<F7|5`6kug%(1F<MY|*Uq>?q(-RoZ`W(zv_wl3yJPad9ZwzwZQ*l9WW>A2bQMNr{`Vok6c=8Ia)76tCKSAPL^y3_UU'
        b'N5#H$ZUTFq9J6Kn=Y@Sg>~9z5TB6eabJ!n2{CD4Pu+zHiS;TW0_TP%meh>D*`NNvs%5p7rpBL|DruCaG&le(p|8B6;a<mTi?hDP9'
        b'tw^7Lk9@>nUjg2xN3}J~Ww1we_7>O!I(z9)&6d?VyBqE^s|@_EUoXrTpgfj`ME+y2e-%{ukZ^wv<~KldrTrb4r>r+ydLNegg?T<`'
        b'|L25#0n852Q_|i9b1~v)vVN|BeJ5!6b0WU`VE!h^0z2)!22s9q;Q#Fhh5Pex`w{4{Y@eUN{1?yxX@4K)3pSW7i3fy#1?DPHkF+m_'
        b'c`5d!+oXLZ?0uj?X}=ccFleW=?}T}eA=h$3+P?z(e$boJegNjTQ3nU5{l8$JGGMmsmiA(pFGBujR2%HHkKB%Swt_cfk+2_u-39wY'
        b')xv)p%zdD3l`=mt-vv4<?f1a^70{+C(f$_H&tBM{8rJMzgZ&*D|0eLCfxYGdVSfnr=V9OXh^XJ4Xt(dcer#C8{|e07X&inab1mr$'
        b'(P?08k&lO@Kr7dMd=2S$?B%MN`^D+fey%W$G?UT6^M#s{#-7l+9(axgg+{CZKM|Td6eK2?a%IIrnp#wSD^eejP_q(G(@&WtPjo<='
        b'4jq<DJ@|4FO~;;*bicg$s9Z?yRyY^(74C+fP_IyLB$QeG&lFX={HI*%b(QL5<tgRhKvW!Qrn3(rzWS!gQy!<~k0VtPPf%(C<fqB#'
        b'n7*n*x2}AV8f&uUl1?>A)8bU+npv_I2nBd7G%eF1Cdwdb^ofRoUBRTH7NM(DRq-NEPIPl!7WzEZB-K2MB<Sd=R1%w_*ic+H!%wrO'
        b'_}3p=AwQ%;3F#$|qUaQQrUrCNY5ru^_{~dP{S6nX)~jknwqm5=y$j2qxOVoYyIaxga^uUu4P3=|T3QW}{$5dMT>V9g7D!oN8QOW$'
        b'lho8BlwnbtnG-c+S!Q0OdfPajwR9<zB4oz75@UWVr_5{e-WbI>K-vYh77!<`l#;nkrKy)zHS0^Fs#BHm%g!l1^NeKNRHd6j#tf8s'
        b'ctt4U87Ihil`juwrL=*nAw`K_+wT_}(@^}M(K2rR#pN0ImY3@f9;B7Z?hhn)(n22<odaBp)t5Lkz~?HjR9QsYdE`YNQh}DMqKzgM'
        b'v}!Px_HIE<yA|e@sxl0ZstiNi&LVP%J$yNnCt&IDL3eLtL%DnnwMo2tPHd9jeKrXhTHn74`S!p3t9Zx1=6Z2I*tYA1eESR63wigd'
        b'8-$$uH*OH`jemB7kaIt0P{_GA4hlK<j}Hnt_kSN0a_*}(3pw`<n}wYFmd!%W{h`f5&i&wKA?N<b%|g!oyc^9H`Bb4>f8t!VCMmuq'
        b'tt3*}Egva<sm@zz7Cf43c%LE#q@*lV=zvU_taTBqmpa50zVZ!qX}jn?O?f!i=vB_>(k!`)QHP$I96dGGg+tc~#T-%(18*%=v#p31'
        b'{(_<PQa_nLtmP@GFIQ?OPq|r7ZB$j|tIU?}jSXp#(NqqloorY7`s1YI0o#S3pI`ePQ!uB9WBBR1S#8=Ln>Lkdw^QhZ(!yBs=0HE!'
        b')*cM#G&H5_^b-}P)>M~2OnFu{<KwZ;Z@|-Z@rg$#ibneUFxQ3S{iOaT-WQ3`^?>RjTJ;g)r@I8pnQY6XHak+yDHaU;E@ss;Us#~n'
        b'^xB0dRGxCSS<9TN3Y#Vwia<`a{@!>*yHukEGmB1-D7}5;TTZ>6ZQ0Ih@wvO&TY_R9SG$z{r3bP?dVG@Cb*TCpq|!QmT39`Yto1Ve'
        b'(^g#WEcE2br!HkcC`}Y~%oi&>pk3R!3ukTrtQJPt<Ow-mUl?rs)P5u(RdWcPm#10xU8bE4*4C;aeh^Vcpmz;Nl#7>LEOfDkX?+-{'
        b'=TlE;ZHS7tj<>pA`L3oNRlAd;Ts`b1pRj!DOdV*fBb=;8g&(yN+WXd}bSp8N(4vpOfu$*(D~|Gqxu&^v&s?8}U+C4qAmcm#j3_ka'
        b'UOlo`Y~(usq_!xb>xYymck{JzT1QVtq?OwrR^**(>Krm|F1f}mEiiwu@|iY0qwT?H(63dxm^RZrwMNE{LR|NenmV<sd^sR0NnU=z'
        b'Rm>!Fh2Gvri<zW~2u;DXY^cn7iPHrMaWO+Ak4}nUl(}+#2y%cgjI*leiOG(w4Xzc77YY4eT>Xoj8%PBuUn^Is+aBtLG=Gj+4SeMv'
        b'j-0Lz_%%7A<SF-TB=r!{iVG_&dKi+%^YB8_l@!$KpD#}+N6DrZ15;mXq>+Md=je}TtI`jWtbCm)67C4|$z7}N%<i<JW>I;Sdc#q+'
        b'8(`H7JNR2@x$@T@bov1N3xqg4D7%OHfa9H>)_>aIPCn?9V@kxOYNaY?;wmM+F6$QeMP>9Zo-wr-aCOkSbIf$7flwT!EspuxpkJsT'
        b'6_-Y(G>y<|)Zp>(*;jwiU1*SX^D0&!-&d}ds`co>tbP>e<r*aTIzcEKEZ3?3O+JuFO+{MK+ETA$NGVq4wGPQU8R)7tZEn|ZI&9vC'
        b'rP`M(su<anv^(UQHB%h<C~8?!rB*zjSE!|XLtTlqCAh-Z;K`+k{)$YUey;NL>x;#PwOqX!TI=emHK97IJx^5^T&CVpu~B_{z-xuJ'
        b'vGQA^=v|r;|CE;xN!|Edtv;!TO!T0ZuuScXCX(u|6B{DwdmNz-IjO3Ue*|O=>2noNL%tg62qzbk-64LoxDP{D?myh}Dx;LL(TVdO'
        b'x{yTfF0?u%Wx8?tz!DCL?S{U~Q{-K-5Wk#4yztfTsiHipTRK{J@T?$jTm^+3a(tVkL`WMYe~F>XTEEoR#K&_esU4p`TN3F!{ipRK'
        b'H;O%ta+BE8^xY)(G!NV)_B21fN$hE+ZxMT%_AO#h^KV<kp2l#q*wcLEX0fMPf3w)r?7La)Y4UCndm8I4Vo$U67O|%pxkc=0MsE>&'
        b'npvL^dz$i3h&_$%6Jk%Z;S*v{^Ykag+1=lKLY&>bV5>O0+qG4k-QBuXoZWqMt2n!Byj7gtU39BByBoMwoZTI|Rh-@Z`K{vY?)2Nl'
        b'+1<L^#M#}B+r-)3J8u(bcOSn^oZZd2U7X!*zFnN%?Yv!_-Q9V+IJ^6c+r`=4qHW^rZs|60cK0LO#M#~0HgR@$8<6fae*suU?{&9{'
        b'v%F{BA<pvB9*@rQ&c8#P<#pa6&hmcZ4sn+E@jJv>-rw9I&hqAcQk><T3v3~I7ho&NH2~Y_K4_qqWFLX=13w2`N$<CTtAIcFB;BQq'
        b'dIO3J+N<S7?TdhY{*OgsgrP7YziH4XW?>)yIOgjjy~^P6lk&``>L_DA|5~n31YSa#4tBC|)oDJiG|b0urSc(&PbeJLb7H~uOkRvA'
        b'#w_zuPxeVIB0i}g)fe;eXQ{@B^agy_F`w-2zF4$R=2hi%#p99_`q(wej7k=NB=`a$@eMeIDW3UhkwwC~h&P}nu+e6|?%qfwKn{3<'
        b'_>wvdeBG&5f50E5!O!{9l@!e|$~3P+-++LP0<II_7qC`9mw<i&>jfYu@`1r?O|wO5)<X`}N4IoNT2*(_kLT+Rk{%Zye+BCkpW=n3'
        b'TD4K=IDdPfa>RTlyfGiw4xu^;3s(Rl+LC{#_tC}MD19u5HVF1bVjF2b+M&sXmF&>&ZLi#+-P^uohjwrKcXw#_wm0n1?rpzphjwp!'
        b'`ws2i_BA`Sd)vErX!o|qcWC#vZ{DHZ+kV#$?cVkWcWC#v@7bZ<+y0Fm+P&?s?$F)azC*jW{dYUGd)o~|+P&??Lt@_J->rtUd)qBT'
        b'+P&>fL)yLV-XSp$a{2ZlF&EO$KP2Wu`dvFD=0q-SH6-Rm`rSDs=0^J6Iwa;t`h8|d%#rl_+>n?j>G#DUF<0{MP&>qY$?uLI5_2Y('
        b'iyRX3CjGuMB<4=~y)q=`Px>7i5_2g1emW%PQ7&6MB<523Ju)QbQ~G^*NX)79+dCxYRr)<MB<5Bw4>}~~SNe?%i8+>j2ZzKwOTQlt'
        b'iMf`3KOYkFE&bjZ5_2y7P7R59m&-ZcCFWj!j`J=t|MGr#mzaa;xA-nG5A*(ZmzazBd5gQmd`!QtyM%rP`bF;&Iu`hA#Jhx^1^V4_'
        b'm(aC9zZa&yGWGbg2K%d1U!D5Y*A4d4;;Q1k&lv2>ik-zhz!k-9#ixK*7GGH$c-mmUs<^9o02n9^6gL5b#o^+7xNj`Jk>ef3pXT^L'
        b'@fSHhS^Q0oBgNn6__N~w;Q0IEzi>29J98T0In&OWb`a^$m^NeDo4|9Y&7O7wIA_|NX*EcvY+B8<1IXturu|~tUf4&O!I(2jzcO3@'
        b'fTHS;akYsR3RfLdp2k&QGN{~&Hbv(<gRLs?qxi-5bb6*@QdoVD*^&T;fn?|JNAJ;OfXhCTD$jr9puygB$Y5uO#COz$40E3@Op#^$'
        b'FzPw)CuA6RC39CXcQtb_V(uE|Ud-G}n7fv_>zMmeIFU2ltKgvuKC0lQ3Vy2KsS3WT;H?V&s^PDi;(@>FMa)^roK?(O&73gTFy~_C'
        b'T*92Stb$bpv0tMbbabMBcP}y7cYz)P9R}?N?Uk~E&q~}6JPJDSmVx8lz?Xq<OZQ`Mit^q4W~vObR2t2E!S1+^R?YHy<lYcnunS&~'
        b'zqh=L1>@00)jmCw^>)V>F7N7Iw{W?*%@`BCGJBa)nHE6>{2>C(H+^K&`PLk|NKNkPT;?g+(p@$o|60mv{`n3()4whn9-w9c+<f8a'
        b'hU${afo}OzDwL9JF)gfKP*Yk;cS>h-%}8AAQ_~BMmBuyxo@6nXkLNf~spHvH=FeA3`a|JFG!gS9O0)TwdbZ{%HR&}G#?r_~?+1|Y'
        b'>cxw7F0^M!x>VKF*3>OpQd6t*;7=eu>7l9;9bI$6a?4K=f~s@Y8o|Pe+<0!Vcn~cms&<`tGYw`bznpB-CM6P!Vh0&lmQ#p%@ul+u'
        b'OZgURsnQUM#rmUsGa4d^zYwWlRz6-iFmIqtp}+q+FFuKl%3paoi$@iUvWP`_bIUA&lhHz?E13yb)LIE;%_p1^r3<S|DOcl%rEhDO'
        b'D7>-8s)W=`WF}Kpnp)Ua(%~E<J?BC7MwNN}R6gM=5M0~8ZYlrvCSpWQP!*7m5^7PjD;Fl3uQWG$d~Lo}?QN~iSCmr9dIqD{GND8{'
        b'm0+9^B@!iFWJ?uKKNk8TQA$z1+3up9eSerPIj7|z<pZsR*tjBU>fce=QzGg}Dt?YfF{xy<WJ*b${1YJ;Pt?-q?{n9uR7`r*;?tro'
        b'P)5w{!Q{0J`Wz?=mye&L#?XMcT5Nq#z9xu`5flFQ3{0X3W|yG0qJI8L2&0)shHMaLd%Lf-&DrWL&6<iB6%)!3rtt2CS^WPE1?tu('
        b'9v`bvV@8tcU-K@zxl4Y1P<3XnpV!l04$APT|7ww(%Sz_;qifCUFCEu=a)O(f_vCapws$qxq8ExTPQEe8pWZtkRoQ&2HOOBds~4+?'
        b'8Io$RvQ8uFN;G}+^<v}d3&rW>lbBICr%Wk{Cu03w2_@-iK`B*3Y4*vX-H|pq2*w9b14F!&PxCPNC;+$c22dZ4!j=g3_G-46e*>Zl'
        b'le$fvmkbUm+e`^WvyIL@%?b~+kkBzwZ2VRU%}Tk&)R)XXy&}P`nA_LV+l+8m(v5%Mi^<T$&_=$PPertG?59bxnvWheqVC@Qc#mqK'
        b'X;w7{V}4zXB2;RG@RTe9ebE%Bp^CnC!2u=wk=>O)p1<98Wc~4vUUSWA|Klx|Yt3%url)@Exa+KAZ-4HGKiu|&|D`?82ktxc{U6*i'
        b'@W!O!nSc1kH=6lUuF)f}3lMLcv1$C2L9CIjrAB)p=tPOpegw1&v>&twv<cJ$DgjkqVzh5vAk4=uHrmTTh2R~WZ?p$MR?x1wM*Aty'
        b'VbG%>y$%P*LSa8qrt#^J(0=giz}r<W-GK*S9|o-fML|bFd*N?D`YG1OG0v|)zSbA*+31TT@SqDO_zR+v1*miW`YD(wliy$#E+-%4'
        b'TFP9G#tP~ekub^qRv?NB84VV~`UnHT^*mDkDrxLkxpOI_P$V=?8ZUjJ2uTh5k{^Id$dx`hz{kSn!nKqq77lKp1nE6$E!qe)vkvt`'
        b'bg8I=0^{Y(Xkf$D`IDK^hzcz*VRHn7$vl@S2J>74GnnQYjpn(z%#df^oRiOr3QPuOq?ajqW~0$ca3g^?6yDh3u`_2JeL5Zwbt@jJ'
        b'VpZcfg6l(FK~`10sAlmJ9lycRpt{Lu(yj23G`Dy(bCb)#P-`?XMFZaU4kxQfYXgkAjnoeQfVhSvUJ;LVRV1i>x&mE3e^(!xh9n}e'
        b'H1_rN5BS!F)(5G^<NTc@O~M|x%h%X!^ECMyYz<A$YIoBW9$%x))tr%-KN|J*N9pKN1@=v7X+Ne7+5}<sf{0o>nwy#Gunx^Hzk~Vc'
        b'##Np>))$F~e7(UitrHhjXCy%9t$HK=0KJ$K4<ue39UBvOyay@vVM5kL#I0*LCW5|je;@H`Sb89zl)>=HFL4}^CDA#P`JZ5xLV@lS'
        b'ryf7mvuLVHmg-WycnRj%a0v5WrUPvsSSW(Qv5xXklHA{9&5igBRk1D_iXc4#IZ{}+zZcWz82&M>b-}+uclMB2cm`kz-@VS4i1^m^'
        b'M%H5ZfkR5>L(v|r_TA2Qm%GW=(&p%BcKTXutH+98gz$AGVzj50Hq06QeALsM?^K?=dLWG}HTecY>q8_AhaFHgtrAr`T9vNhSdu;s'
        b'VZm3yxAE~s6`^ofZ+{@jdGxkE=IiY(?_sKuPf9XAo!&6B?kq9J$(VhC`gYHTWIup0hRze|6Ymk|Ioc~ZSm~Cm56E@K{FTlIhtt!5'
        b'QReeB+1j0s()shVJGZvAN*|@COC230=A-X))UxsQfn=^>=GoyM)S6B*XhX$9ao_r27pfu{@A8SyaExR!1*1EH-WlnSb&0(zdbHEy'
        b'_O)Gpx*YL8YD>ftUHl<UnM0*V=&L$Ls4v*vkAB(}?Z<);F%Qt2vK7GuHn%~Sqa=H&L(wii=%kq@oM_j)03(SJZE6G$+w1r>OnMV*'
        b'1j+|>^MM3<H{G&8GgAp)>$Q6ue5<{-W?y5w^P|3+%9gB&i|;t1aPdf2vVe$`5BWHrxq;$~$t$I!E=>5l|6_(uG2V=w>Gt(l#H7?N'
        b'b@e%oN!e%22O)lg8$5DZ$VhK+&UhJAZ#e2=<3-C=_D6+4fg;A;>^V$KkaGHxjUAw=B^Fc*6#W#|HrLl$JHpq5BOAgj&w!tUmh76G'
        b'E6ESWBiMg34?i)=r4m`w20L9hFD~a}tNe+s9$~K1iNEXlm3qFt-D$g=->@B%mR8lqQ+I{Q*up=-D1rXIsCX5?T>OQD5UtQoN2Uns'
        b'if_|pLR6H0rp8m0p4sBW6zx+&af+)1RC>lFHO?q4cTs(RZ?ukoU=|(!*sQIht%SH(Q}+QsmXrtxh~&^t;;O<8nt!^;in<f(tEHtw'
        b'K{rLi2r1F5QTe;nYuoviTrxk%13e4n&ANU4BA!x4^Mt~*(LpV~l!-$LQtE~-i1xHAa?Q9D`Ea@$sucW|@@N%Ut5dCuQmr*ftGhwr'
        b'Kj!vGgRN3ERH=q))v!o4)ToBVs$q$0s8tPhs^QXPgq5nHN;OoghDEBOMm312na9>H49?XJ4Ym%ClME|u4o5p{wmVmFr)FoXLl_#`'
        b'I$FI7eIpA$X0~hq4T5e34T0_hJp}qP=&PXTKnFmtfqnw|73dw%yP&^<^7fc5MWAy*b3m7XYCy|C&g7&(ZPOnX%PcOr!Y2?pSHLP='
        b'ltAia!W@x)dWoemG_TiSuMq6jIW<JEm85<|g3d`UzgCRinJOCsiR87x$Wnv5qjFr=D%QX|xO{vDl(lrYkzaSGh|j&e3(}Ppy!!?N'
        b'%+*Vm<n+42;<W&!k1Yayk!CtxV-VAvliy_0jDbqh{6T4@&(>AROz~^JyZk(tm<k<y(PH0tWiS>&ujB$$q^)5+hR`~so{Y@a8(J48'
        b'!3B}3+hN0qN=wk~YII=PDY(L$t1-JjjZ6N#&32NnPnt2PLro!(6fapaM<QCuQ>A#dnAM0<7!+GiD4|O~85^;5@krOCy&+oZpeqNW'
        b'RRXF7ED}&7V6lKD0%{%NE`V>LuO0;b26PfM{VQfm8R#-l59nUdZqQ!Pi=ZEaehoSXGCgj#6oSqH-T5U!3t;{T=%b)6&_>YBpifCZ'
        b'kLvsqeFOGaLBEpxKLO28XztTso(Z}Lv;b5Essq)78bN1FI%AR@^Dc>z1eda<G>7rGWviD8V9F-T!iKi?_71n#>5#ToudB6#j-zA!'
        b'z!%4?M4?YBi>iGIrBsR1;=7w3Aq$uLt1?y{w1$i&B5|=OqT}9iKR46&F#6O+dTdU&dKC+GT2YZC3Ktdaq3@%?I6W$`4iT%50DXSY'
        b'm~=S4xvk-HTC;IIG9_cU@fBVPMXSDqr=3|T({n7Ssm4ae)Rf>uIAeaI4MMu#s>({XV8H@sdwW|uP_dB!FCKa7ksE$U5GznTppx?L'
        b's&GDijuFMAw`D<k*Og@WySOMGi}Ka5OPnkW#j$?!i^@#<HA!-l%!whD#2(LpeT|XjvmDXF$deC~9AC?op!FMFD}1!f^V&R@`&K!;'
        b'KCi3A+1BCpdCC;Nkt|IOho^E0U5)6g9Lu4ql+oAG({vU3Blq33PaN<z*u|+OZx9PNbpsO};04d(vfdVr_DTUpY#QiPRm_XLh~;0p'
        b'vkMv1xl;bL4T4-Q3-r;O4f#GGxl`hMs}iTz<MUkMp$ck8eYLM}dMkZS#|o#<)#`2cdD=SK8=T4|3g6L`@x?QDXl%Bv@VVM;Ey^Z^'
        b'OC*)i8zXP1>l#-)*2JG<ScuK1#XH}eV#iv>3z_knElU;hP+heDSWi916GTaPWuWdp+8^u>dT2+*Pf>t3W}93~UU@@g1X{Sff1pL2'
        b'REw|jhlHjLWekta;*ucg%K8NguCiPyQ9A7C@7|5kAfH_-MGK<@+#i4KQL;XQ0l1(P9c*?9LPYz8qk7ye)ej<}kHJd+fD2n6kNTYs'
        b'>@k8bJ6-VEYVZLyHd+lwx=R!u59OO>OAnJ1vGoO}v=muU@aYQMH_~0z75dPnJi3e|(2p_$(x>4Jt}NzyiqRVp^_abovQ?;^^rg*c'
        b'ln$--2C$skn7q@Im#0KY@m;NCi(gg%Vz1IgMne#z(L;+TY&T=n^g*!$&xp5Di+6y=O57Wv-lsKBGPP(|6K!GB`URRp%TM`$C)nqY'
        b'_F#4|A86^vZlEdBOK*~v{f&XtqBIDxM6!vITtXS+o>{i)=I;bWgQaEvbWJv9ZZgIL^(Prlt$FGn@=$2$7%Az(Ot6CtxWYX_`pO;d'
        b'3bv^`xiOkj?W8gj|A_v%o_lt1g;-34lqc^RW05}W`<OaK$!hcZuSxSLZ7VXu@H?$SU7lb#pgKfj>sup<Q1`~nSv4b!<WPdVrI1{I'
        b'ES{QRb_Wqh13$`=jVC6{RF`(~T9qE5V^8q(w2P}xTGVith>32I7Tb%2)_Ao1t5XLz<13K{IwHN2w%`bkr)Wu(j{wn}(oa{?4}WM2'
        b'U%KZv`sILlxwm{77vYgMix4bP9hWUD!2+wcQT&wBEE6&Ez^7sH?$DxCqsI@Z&v-Eoui|c3XN(Reh68mregk(fKw+Bccrowy;+FEZ'
        b'ZWlihwk%8U1J!5tahm3qjx~#+2$YIC?*(+PDx(8VI!QqpfVm^QRvhb~wnP=<LEhHS+g6(a`NO9*xB*+DNQ~}vw;<8##ac4iX4u(d'
        b'49gD`fcJ*h-~gZQWL7DQv_;@KY~V6Lyo>Q74ye;(gZ--X*Sl9IyP}xQg7KzcZ$Ji~ecHg7BEo^-fP5%elq!uQhAHRq;;Ecug1y`x'
        b'3I_Pz`6?wn<kgh<>nl5&d1skVeT4_qnu>Y{RXAqv^~rf4V`?3HG}6ja`%V{)@k?=i>P|@Y#+RsZUzg?;`yx6a%`kB!`eR|yN(-y#'
        b'X&75iWmP*xyC0hdwqCR@pCv@u^iy4bZ-z6UB2yy5-Z&(tc^h3pDYX}fip}&R_<XWxjKtLL%bD##l7ykOwGJ;*>cw`oEu7@iRiJd4'
        b'G&b{D-5J%2hs*mnh1T`Jx0(+=##-F$;VeI%2bX%3gF0)n@25^2$ajOgL(MbYg^T%7<itZ8gycv`ttUJX1cT2i)Ewf;#0PTH((Flk'
        b';!iDJTe^we9SVmr_#@QM8DIEdCGSSfMgp!dp98pX;5a>tZy{)+_x8mU&-yO4t1uB4S!t8Zmk6ALZaroy(e>O(-CwyJG8XlbBtD-~'
        b'`LvxXW+u7+h^=>vH*xBL_y+ZMXwAtv5T%o6$q*iX=#X2ft>ZF5QAf#5o~BmSprdT|ENWO&?AcHyqmHuKPnVt{O}BKm@MGmKFD;(*'
        b'@a7K~pYa3QbJEI?uGrR;mX0Yczvi^O<fOTqPE$Xow7NB?g{KLWK8|A_9|*<#eZBzxB&Xg0-^yo>lAfSH%K!Mf{9Ib$G|^xwhXsR('
        b'O_{GODi!PZ5^~VlDMt0h1pmlJqY=+gdG?xr$_mEh+0!^(Zq7sa>Am-y%+O%-_YI||3rQ!%l0wtTV)3I-kuDuWMyTWPPrn%+d~4}l'
        b'R3=-h_RzWXr8-cpiI*fKKfo)JzTRX65DZm1xXEdA`#i2Iv&$2tww3w;nKMEGE@B<-@AHv8u5p*?xt?a1$Ln*pxV=}D%vV1X(GfLr'
        b'E#-mYK7TCc-<W)>l$st>1MwjAJ~9}?G<H?!>T=N~kO@7LR{mLw!C%*ij|DzF9nhA({zRxZF1{Me@YwNJsSz(%G7@7#h7L{dQ{8;x'
        b'!$Vx^GM85r8IpSKt+iGXDoc*t!2|VdP>%IMxG_2>Vvu9M4)zyy_Df-ZNoQXQ`^!4}M__+NXQwMxU#%~?N1aQSS&Qy@wf<O-Jd<+I'
        b'GPr+_r=R>CJ*$&0W>e3%dAzoU%PSo1wif27p!a2@|CFG$t<~pfvH7@DySIS=zaPG6wwQ_-o0P9bd60N+#wO=$6UI+p6f%5;Gf)>+'
        b'k)NM|my@45r@cY`iZ$Kx{LTQGhEeDDPvj5f(DQrJUtOj5gK%&|Z)j}=zxG?c8&4VZ9bu_Pj_VQP&ZJIZPI9Z4(CztYS=z&Q7HJDk'
        b'DZxbC<hEBVYkUc8vg7j2rmv5`pqQxdn7T`q;b_(r<>AL^<Y3|3KhE%lBjM}l>y-W-w{M+TG%)>p?j%!$6N0GW^~tN5S@Tkp{p~$Q'
        b'yBGK<@Hl86sQ4>J`(a=w_`ORto#F#9yW!U7_OA=l3Zk68M3<D7V<PqhuNAwy64GEwwn)YsR-`Rt#JH3R*`kODs}}r?m3Kv>yzs$T'
        b'3>zZ2E?r9Lv<T;=OX-7qiDXMTw*_U%uPK_TlqGuOW6BmunG6-FYW%%Ed5Vd)@Y(o2$rK901N<SdR(vxsZD*bNph8d)s2DT@G!vwN'
        b'=7LH<WuQt>4X6%e0a-x~P!p&b<OX>`t3m1CB6`7#f)bzs&?e9zXbWg7Xd7rd=x)$X&@Rw0=poRfpxvN7puM1{K+l5qf%b!3@{T|{'
        b'xAsvwcaLAYM2|$TMEZ^AXUi7Kdp^G(m5D>5`QnOI%nXB45LdTuQO}xgonSblE*!<NZGz!Ux^Vn1xe12L*M%dzdxGJLbm1uNof8bF'
        b'=)%#uY}W+CS#{xPejT1*xItYwt{ZiN;mE3nBM*;GG@MZjN9U?{Pc)oK3rAwZdnOt#UkgX)wf9amT#*)zp8roxG@PP^qjTWTPBffV'
        b'3rA<h_f0h1pcanKm+zlwIM~&2)K?EoIGiyVj{Lqn;c%v8IGSe;PB>hCG8~<UKQ!TRMagiq>^MB(a7r@VG~K?)sJk~uFUOiM`|%{%'
        b'zY1l$pDEj;NY>NYGXKRg-qC;JkMdS6^G9dbYwIqpy>#hE>P%VW2jbC?d`2gw$+_S;DG7|kv~S0%V~Rj}lI!ckiYJZ551#nAW}q||'
        b'F4acoXwvxnnVZQL=WjB-rm?UnN#lfr1GLf?QkapbSa6NGQqXEboa0qD70D0tTqwa8iu>aJaL^|_se();rTT=rqW!cGTv){-i5~2D'
        b'l47}4Ng-NVQk3Xi>6^8h0g6JL;Oy=Xca<sXnpDyGm!AoAuW`9-2RUg{z^PecvrESNXvp6LHZ(a&D4h-sdVSbKw0oTnT2hNBXLC^x'
        b'EuTWN+!s=XtKy<oun`Oge96q}0?6w603m2KEY6w7c_-sbNHl+US2%&~ocLZ$A3V4qBb|KWA}ehTzLu5_pWDU-3dA{#5(*l>ivETp'
        b'SC?ja@uzhGkvJttg4S76ruPK=%gY>9o>FW9xE5Tw8}Rp1M<w0ch#*Qk5Upf=oT+E1iNskbLfc^ydT60zB(64}qxQ79jU?Z~^pO*t'
        b'6bVJxg|n0k&YwAN_MD66_6BL-kh}&RISz)$iIL0Q^H}}S5N)y2f|6Xq+Wxq@^$=rG1Q4S;819N~j3zQ&bapvI@O?LSJRvSMLia21'
        b'7eQlZPB&2Ee29>o3AIx+RHZqHE!4&keF%vsV&Sg7XbJWqsNqCU8Hs-{Tuw%M5zrkP$mGy5n9}T7fmb3VnZW!Or+Yqlw5$R{z9JA@'
        b'Um+#S#q;FIL2+(Mc}+V*cGP0B7s7u0;Ka_A>3?-H9yc)XT59<1us;gg2RfAI_RedWX>9^e697$)OJ!bwL^f$6n-`cpiM2QuGf$JP'
        b'ivAE)SJ!Y@yo6v;9k(s6s%EyI3SBx@JY$#sROr~Lgn7|Vh3*{%&)u@03Y|PNVZP|6LRU{Q%(H$fbodlmS<0)8zvcJ;b@;#cXV88*'
        b'218zs*<dgljX60clR3wfV=^;E{gu#9$@pz8O8uFVKgqE1pCQXnxZC;9nB_;V3j2TKH%s1$ex<y3`X11ev@Rtb+qBlhVzCm`Y7l;B'
        b'$}ktE;aI#6>i>cd;J@AJZ1pPQZLt#X?-D93Sp~mkD9+E?k;3XYsoz@Ix}u_-J4nIPh4Mho!eDQ=cz+{ax~cEpLTkG!#2rNhi3mx}'
        b'k<Pxq80~BRY_$79&w}26&uBjhdI)p?bn{80{rBJpfGsD5T_xg=MJ;LW*PYDd|LD)-$3di~^S1P#o_@ACD6Jpq($uG~_fO`jCye&X'
        b'K*vD~P~MM$ZiAV@|L6ZA@CSbpMCP{ljrRNtb2weCGZUSwv#*6Y@K<5?0VC4<;3($%36MVCbb8n%(86-;a}2_+Qo7%_b#Xm<R;t^n'
        b'sWRWwG+zIVoN?1mPk&)r`oBeb#4BgQPl3cgP0q1Df%J=~YHpPN8>fu+xw`bPm+2F~GVPZ>Wx84$St#7iT5YW?><_a_apV}=C;!^6'
        b'K(JfKu-O|N&PL|FlC5a*vUydNS1r7xa^a=6g;)9)UU&7pFlTAD7ScTtF4z5K6&#l8{<4oP%CYaP%&~tKbOLlK?6shy)j4((@LM&g'
        b'pQ;@DF!0tIVONRxW6`Z??q99R<WH>{KMo=_ow?F~divSoptPpy($uG~_fO_F&@G@!l(!r72<SVoTj2j!iv*q}iOjy*9J{hwP@m3B'
        b'RI0PbU{2Hta|C#UG(Uc6j{T_#kUrjY`ucK#txI$4)gKXdmD2s5(8aaSmFjkOtH7!@jdw@;_-Uu7zbq~N_b(MZ>r&z8T#1t#bL=l6'
        b'{jwI#jne<a64a|M{ZGsEiGSL$6Q-lsiH)q)-}(=I!UV`1NJQu$xcz_fQN|PM!`hz?!t!@Mq(|{z)jOqcJ$%pO-`{0f^!Z0$zvxe{'
        b'OP78Axa0k^9<KiEJ=?yQ|MXS!8X~&`CAkMCvB9IY8^3L9I45j=^2w*}YJB&-`d{a?)wNV#Q2Acdh8wT6JQu&=XKmB^MXbl9Zn?Sg'
        b'ZPXP4t#=CC`fY(9JHc^qOSz4Impi+Q<CY)Y!!h{ED};(~n6K~OUf)zp_~6~=^#QGK?W%kbxc$QY&;AftGymOd3LDgXvf;xwuc}$!'
        b'zz(#o>-*N18rZTOoo}xGWrKCwlLHq#HqGJw-5WoA^SsL)L$9~we(%_z<4>3U^1H@`PdfH~_Qx9=27cq1baRfq?nd-8&`!{gx8&G='
        b'1R4ZA1oGdKV}AvFE3otyVONRxV^L|E`^sA~`A^(9ejG$<I{T&n^z^gEL1{gqOH-e|-anat2bzCVj{P7g7v*gPb;EoF^>WkA0w0q^'
        b'=JRjOu^)R-P?^q5^ww6*Tm`qf+k|-$aD_B)ydCq`1V|t6Sd_ah$NqzD6Z1>7;_g)Yp`8K`+^g}zpPhJol>X1t(trAP!8;+#@I#58'
        b'*`8x>NBSr3(cCEgFQU$VpiBRVtV80TZqA}t;wJUoxctzcry7zRRUXHvc{b;oRYRKReC;iE+J4SB*)-XlYnYrgOrD$r!({$T8pO|>'
        b'56<K~m<m*<NyJe-i(ih)$QO`IEB`dVJp4Cu$j!^oGv{lYP3ggu&o_!>%pn`+2!q}o8&SBEAs=R9=j8w2@SDWtD00wlW|qtH&=v)3'
        b'5}V8l*%|Cib{2m}AA1Gss28!u1hJQL>^9izL2tjDV=n}byqaTQ4F03Q9j^+zO2i+FcBHv~^VLlL`7ezh2a%dine?BYezrI$t@Cwh'
        b'>eJWzC-W-MCqZ>6Zy5CNpjTmc!2f@}BJdnZWWMG#tOfo{&?cRkXtB<|8Ro6u7v`IQpO)s4ALQ7-Hv!VeI~J`xlw-f>^@;f<y6Z?9'
        b'@0S9L-_UqpeQV<JQTpX+=}(fprbEI$U*fM1=h*)Z={t^UZj}CC4(8Zr>C!Kgbx8cv&0Fp^kBjuQH=O3(#s7BqneXP<dw!q8-&yWC'
        b'Vz#h)v*qjOot{#^hS5B2^E9|z<D_&t_te*dN51!(Pzk+n8rE-vpndi1tPzmQ%3k`k6=o~*oP>G0js3R52EL6|t+g@F$8BusZ8rF^'
        b'u{EEA+haC%{j+c%v9aOT;pYt-d;Y)S@1%|W0p(sg$<A&n!u&Md&WbOvvo#ml*~6uF#A#<sme|?#7CZZ{-H!O}4<bA7fo>ul1R&D;'
        b'?~vafNuTy95b4_{J^!zP-UX44>z`3ENC!9R=mC8SbT3Ju$@bY!wFCOAlog?uJYOQ+*`#}$^i-3canRRj6)V#wo!8W8Bv|%+de<$#'
        b'pHdBze(vAMZ>W@yA^8sMukzj2e@XjSWWGNSBAwW8gKm`HGvAf*JR{4vg=EV}c7pV&(0vK?-JkB_16?okPdd4Gker(|Q$2a4`M3<b'
        b'MTWVZ^ta3UERpa3=zZD=`TlQImY)^@JLPxZ-_f^K`R(_1`M!|8!}iIrgiB<8z9-w_C0P$tcXU5PBZxKx-E^mh%nQ{O={N6}VV)-a'
        b'_OhPd0{x!u2$aH#d9plz2Hi&Q|787A93;DRQpWienWsBISIf1^O8LFJQs(27jQ1MZ-p6FVpOv4}KO^gHiEOtofPN+GnEJ!Nfc^t?'
        b'zKlO8`_;`d5A<Dpm}LFrr}#T$y&jf>jQUPombpsypIq6WDX%X|_eV+BJKe!SGKVtH)StJ>ybHO^W2ly&)M87t2(65+<GzHk=MnY6'
        b'IgIT`ReT58bev<7bx3XUMzCVe4VPSJ$y-yrX#OLcE#G+Q*mYa;qSC&@()Ntsyl(f;>Sru;cu&s$b^U#R+Wh^=@!v`Nd(@1VQxkg<'
        b'muiYLsJ|RHTULX>U+WJDIbW`i8@wo}=eTy)0Y8U-zR7L@)zu3+2=m*^P4+#&0np5PO<vDB(`5I~%=FuIfyw?X_}f7x(SdfMwyv8W'
        b'SKvpp)RV}|l}d4XFwIxAzpGuI3e9lfDs9A>vsAZ!ovl&o1ue-q0al}wj-iuFYS*if$dB7)%hd8Lnc{~)QIPB*ESY?-Kh!%${L8Y$'
        b'-$)|gC0UBYk4Vb{O(<^VK;<GSS;~)qNH@!}F>}z+AEV4C+ooCQ;!A6_7Ju?kCo4$_Bu;ydUEkHHZz*{Hfx=ZK!)2|EtVQCja7lXJ'
        b'd8VTSuDFM*XHFCK9ivjSwoJAvMyWnn{i$8|gH#~<poy?(mpo)PZf{jRjom*!STtkAGQm2wiEsPad-7PGKhS7Y1C5o@fp$^1%af;7'
        b'sX|57li=?M>%w(ocVVHI>jU=T1wu_gHL@>_RV>-9$2z)QqMip{P^!)bV^vu;zvI+Y_MRiMIv@@Wd(`tS(oQ);l<lt8750uspZ5y4'
        b'I6k6}f<;ByvZw?|JBdG$`9JG;QZ|h-;i%1(Ed%UtdD_sS+x419QE3!88_;w43A>J{H$tcAq*Wf%(|hEn)8S)9FhO&m80fL}{KO{j'
        b'ilIc@Ay4(taXfe@wgV5j)(Gz=#Fm4ATy$JIN=bgT;96#NOwuSpEIM|+AsIL&2c*}+E}K#dAi27vbQ~=ym8mPWJWsFQ2SPV)CFqvt'
        b'a(+E){3;H<P~hq@wX6pE=w&|lM-n%o7zt&CVmu7Le*tp^cV*;NJM+LJ7NRPtE<Ci}fpi$tWs>1wFTH#Fl9?Gkm(L9Mf$q*@hCA|@'
        b'@s50E95gb+Kn`2mdkw!Ag3=|kMR7KEc$_|a^W|AjQ*m9JNzIwu#-#;A2~yZhXQoK&EQVqUmwps-jdX@fNcF|9LL&Ttld@15&xbg8'
        b'r&OqupLXJ5EnSSp6(|V>uB3lcT#AvNAt_WDT$ja3>ULvgQPyb%IY6sHYd`~_O`x5iU7)8x&w>tvj(|>pPJw1z%Q|O*>OdCIYS0?c'
        b'0EjDeVkE`J)gF^U+(+PRakeC_uGW>dW|zZfYhRJU^LTAuXC~KmrBfH1*VowA(dtOycsktfHWFS;a-}M!jL6!-XlwOkrqa;fkilE&'
        b'Z1=d@S~K`9wuaOUxmsPGCSB^SD?L8DO_vHW$R|8{U5Mk#G|yRz1+JK(U7i-3x1lM;rQK<B__%ic^jMs&Z5=C`d>*&0AvJk5^R2d)'
        b'><&$~RyrS_noLXEN+)m6v<zSFyu#;gYx6a?wXR5U;4+wvBypQ9jno#_yEHpnS9qJ!io<n~@hCkhE(p@$94q~H?-<qD>RhEZX%^Sj'
        b'UJoj-p*>q^$<5&$+pVE-#duEHv%?e1-g{*YkKbpcHagxERO&RxR<E<w>vOmo8&TvGH@dWC1yBA8w^!f4JDT08-If^qlqprU-L)dc'
        b'A=z?m=!;xcrry=j;cj*{ptXI?HoLPq#SJy##F%k9vbfpXZLJMWK2oFB*64#}g_fN*uPrry#Gs<Ps2Eh{Mx^OYarQWyoeflpjcsa<'
        b'Q`|X+vYFO?JZy`txfwAuP`62OX>V(8w%bTaUS_DITlP-RA2v*=2No7zL#sE{nK(X|Cv_YNmv*PyiRc_YcYB-G9t~{{mwq5<6G2BS'
        b'LOFORv6EUqtt&WeEf`o1K9}eNyNI1y&w?e?+ow$K!Xdq0SGgKpsS$9F+L<%CQuI8VLz~;3?%--nwYRi6(o#yTan3^LXibZMr6(;O'
        b'-Lx*E@uU~ZZS#0mwY8^l(;qgRxyp9AGqth=yRD<yA(|qyxRgm}Ls~@cHcuLdDluCbskXB5DQaZAEv<Oo)tDYU=;CdwQXSfzD_kCL'
        b'yRAJf>u&K#%H(>q=R2^qZB=UPOI}9%OTK<7ko20eXpr30;h;sDI=4y(7bd{=R$E2@=W3THBMZ7N<#3AyOh>yjg@@Y8#!jwhyk4!k'
        b'TAUatDOJEZsr^0GEu(UhT%l<)lRriz@@bOkz#CdOmZSq!bX)rsscbY!M~kyHEf(kM1}7$r7H>x?KfV8RCc2jF&gp4>w8PnvHZ=5n'
        b'eIu)R#3WBov($!G9ovz%Gn-o*f4uoxGh&nu9j%w6@mo{fR#S*Jv{kD^H!ipn?^2EWg;lbowswd1$jj=S%3Rsz)z7&i<(Bm37d1i?'
        b'bSmHNNwv2-8&={^vomefVaellHD(M($yU2AD%aNH$>yPvcN|LpiY(5KrUrL|=!WUf!BkJ^dOVJdd45c9sk6T3EpuMbhtKxJ(0OTh'
        b';W17F)z;87c82-nI(BhdJ-R`O$sn7jmS)G2aT0JZ;mf6TAL8+v(pG}imbRlxa?{71aL}(AJsI(Lv?iCEz9#*XCDXZ~$>mOS#-hWU'
        b'I-;Ar-n2y{=U^j^e&cYp>mO&_CH)!4nXB4e7{XYG*;4t9PV9VqP3RT61sHcxJ1-tnt)7$#PoIi@jB&oxw!-FW&F+_$kj-tLv_|tb'
        b'dol+QF&k{HVsv=gnz2cu%1qf?rTJ@Ur*)eTPvOg*-V9IrdZ$WmYiMgmtGBqCugLH#`i+`xtj$v!QuQWM!txa(B5RN4nbXRi-kXx~'
        b'IL8X?#h4Q{Mq6NQO0qj0JZ>i@23npsUqM%4WH@{A1Z}skKmrs&Y7(j^kB1iE-em2L=TE9+#@@o#(d_k{&MT%HcWbh;$Mn8>apk3G'
        b'JYEvdY18-Nc_Iovet|mN<9QInVGIxM%Vkz*O+QW~w4e7hsjJZO^6d6pKAs=1OYKORxn9-Q+{lY`ns(Crn?U8O-g!-8)^;^sF@E|~'
        b'7ZdR}Zp9>1#aeG7r5)cx)<&cW$CJ5{)z~gxD=RRoXisD}rm<B2oHNGro4chwC@FqNW|HblpZ2t^W{R6wF?-S+wHIn1O>;rkG5jzw'
        b'ceFNSI=OvKj`nP9kF(X0#-|l)LzZ%o!gY<c%Ew=1w51g<$#!^rP1xF{K0{NS)v}-yjqkzXTH(~qv|0VQ@oZ0B+O<$OPu~s*rdWH6'
        b'7k%lwXw{Dgt4gm}F-*Wq))yyP{B>Y!<XX|{%#5s~)zz}1#VhuxV<w4RaI<4fS1i|UNk^#<;mT1V>(Kv2v&CRwtP6G{Fb2#4-U2iM'
        b'cLB}7uK;s_-v;IZe+<kA{u)?dAPL=E%Ov1*;A8{I2<2J|4J3<{Yazj$RY1cOk~zt>7^jfDPp&0r3dyqMT1-<&W+>NUo<g!Ext3hu'
        b'e**JJpvRDF$p@YfEC4PBPMShz{*VqZ04xMv4?F{SFYrv@6Tq{8uL6sJzXnbL<{5J>X9F(+P6gHji-A`HrvV3m(}DK@&jCIKoB@0t'
        b'crNhwKvFPqW)8{&oCP!j>wr1Hl|U0P1~dad2_(Upe<%OI=g2?s=j0#wSMm=$&jkO#8elHa4Mb(KIM4vx3^W3VfH}b3Kojr)g#-SG'
        b'!U0cFIEArdGr|Ec1{#4@APE?)BtEc*_`vIdIly~>Cg2{R8MqIa3;aGX5BL@^ANXfr0Wd!o?EpL%I2m{eun=eio<ZpV&jj`X&jQ{8'
        b'JR5jFa4PUCz+&JCa2oKJ!0Esfz(v3*dAXJvU<q(Ba5*plYzGE`-N0_jKX4sz2e1eDd0+_m4De&XL%?f*?*My&hWuR1J;15JoxqEM'
        b'_fq^o5{6m@Gyp?Dx+L>vAn97W4`>2D0W_0_IbbgESHL{rDPTTuY60p8SPGm3v;ijrR{{%xQQ#TCt-v#Z!@#qE-vH9t>mLKB0RI3y'
        b'8+hg<)EC7Eq;uL<;548QI31V(o<s2gX8=C~JQw&l@I2u2K)O`p2+#ohBhUyeo{Vw<7XeAn+-jg1cmpsO_y{l$_#7}F_y({5SWt*^'
        b'0WStl1~vl=fgb~sAlNpb0eC;q2z(Nl1AG-|0=@$@11Fz>bbt$hBsgdX8h~D)5f}#M0B-`CfcF8-z$Ymj@DMN$_zp0i1P{;5<+|)<'
        b'0S&+!pb@wRm;>AlGy%U1Gy@L-bAj&x^MEtYLOj4Fz#?D=a0)O1JR5i~a4PUyz+&J#z-hqqi_i{08}J<9$AB|{w*$`w?gpL*JP14='
        b'_%3iJ@Z2f6mMRJdtOkaFi-0?UHIxo;G4R*GCBQS!&b8D6D}Z%CH;@EGuLT-_Tgg6*b|X9RDWDN}i1>RLdz<*clf(y}GZpm$tO1&U'
        b'tw1v{1k42v0`q`7f%(8aKoaizHqZe43D5|9kHQ1bD@J(Wav(d1=LygN8~_@DyMQ^s=YS^Qf0BP-;WVTNtOn)*-M|lYU(VllDbGLP'
        b'ik&fT*vWRm&grkok!MGQoTZG}LIr5;XrU!&16H7I?Vj;2OXO$p<n@LLab+U^?wrE+#Yt`=lg$+$X1ONDyP}d`rqk?P>1@_t4^yU8'
        b'mMPjLJn@*g>7`7WpCE>MB{GjrNC#x7DAeU$jY#THNvbPNDiG%v^7KR^*YKM>yQ2Li8mDV*nG(vp#3%EbAXQh~_kJ(rV!s;|=ZhLD'
        b'rQTje>L4yk>hvAdG+Z%uR^C}WTwYF|&~azTk@|j(Qg^W-BiuYGkG(?5bT>)4X_CjL%bqTiGQXE|8Qdub(*-#fAx;CGeH=V)wv4iK'
        b'4TU)cg@$Rl=bPsjQX)4bPezW88j^(H4D~?Nb?#<n*o3}x>Ozy9(K3v?k?ioXb4_-V8#d+7!a$_lpQ#ikbr&NLd>2a@;r-{C>?D^i'
        b'y|J<Uk(_IF(qAR#mC;$r^G$X|7k)zdJ72~%Q_J5BDHES^CXD|PZmY*|8!Nvgi(974mzrOa)7_TjTRETFiez}_f537?5$2*~ep1VE'
        b'H{8x6_NA$1q;l+m8_DpSmZiE;=Pg1iq}$A7JAK=w)W<k&_do3~`CDVO_kPl7e+T8G{RfpLsXLcQh|w=6UB8Db>a5Iqp#E^hNc~aJ'
        b'j4uo9LB}|FeXUj15qI36$!m{})<41IIf}eAUEb<1pmQ^)xpnK@a?{*;bZ&WRZd-Kz3)9@fy0eJsXA+}2UO}2$Oy@Q!%`KsGo1Esh'
        b'Qy146X>RxG+!kchv2M(+e<ee=dKQ0k)9h!C;jc8!e%2WN%G2ycy1)8gx<aKXWB5xy>vZuL{v2uck}>=_|1Z&xqxOxhQ?s{uw%@2c'
        b'S2UW|7lw4aGj!u%RGv+-rqr?4Z$@=G@3p$s`pc+Jm!npvT0a?08>jl(R>yQ>qsJ?68Nb|lMb*-!^9CF@jIhHy7jJ%YXm#7k>)!D0'
        b'Ut=g=J!oC>tD`r+x_>DTKrbQbEta^W+K?9K-}KwNpJ#RN8qzs#>`d0dKOoL`WSoY7V4QQW7IWpy#Uu4ew`q($)WGbOHfBF%l|$%x'
        b'L$YtEla>AsgVhL6?=E)rnk^*LxqGGALT9QR9&P^JwbGEG-waE*Xhk1<_Vrc7gI)hp%}srwFd?=+{fUUu#}~>ThtlPb1<IP}W`O2U'
        b'BGDUc^uQL3`D0x@bi0$%ixpugypGux+6F>#wwgoP6#}jlOxL<F-KD&tCm2>}eOPvRFc`%qBGT(eBBbChNSf6G5xTND8Vs|>-bf@+'
        b')<T!Dc(5cVwShvfVwq|UV0F%Kxh-?AYGM3_s<OslFrf5AdIMz*8@u3#%ZiqH{N2ICMjm;Yo$EapDy+-e_yHsoA)bgt%bXti>yAa%'
        b'@~e2UP!99UG|O5dr1X<Z7fbU7e~fN_E^7|;g%WXoC1(s3R3>gBSEzawA+uWMMH!Jb5=kX*iI{(Vu$SMryFuxu>?Q-#eUclMc%(al'
        b'Dy4YKS}Sa2ye;DVE*d3~j4Op5<yo$lS%)nlDuy{ljR{cVB6EJUhtehQNhxcJ^wAk7)V;i;lB8z2^1?DtFroDM(a2%6O)RvI?i-C@'
        b'bK%{9l=&qp!MGCd@nge=@IfUMj`k<YM9C0&zrVMvO_og&bwTCnhzCXSl5v!|Q8zqSR39;Pg?L$ezm}nRS1c5zS`MRnkkKBIW!kTB'
        b'MdXZ^TUXJtBC1JWvB7ToC(QQ`1!}Et)?qBtnma1S-f`IJjNY*UZ7fn=rqi1CM!}=!--%BOGp)VoeQ(`PvxUa?!FvSmyGINE=+y>0'
        b'`~Sf&kBKwL`SMJt|8#o){+E|=k37#h-p}~Iu#D%(GR}}|zAH}SKj(jW8EGB=*lGN~V;QNhm|)!dG1jN1uXW!x*aM&~pkqr+_CfWf'
        b'MUk$f7*DT@Q(dRf*x9mdq`q37#r|97HZ`sy?4-)>)va0nfj`Ugk@_1RHd}Up9t3^iVNG{If$3}mGycwKur94MSee0K%rVeh*^4l0'
        b'-ctIORooq+x+T|aorX@<W9U5HdNV!T>F|6>GbQQk-k@no5NlnmdB=)}Wz~uPcdR!*{C)WQ@b}^G!{3L$4}Ty2KKy<7`|$Vw#4mG?'
        b'q3tD9JbI+odg7cqt7%4^wFop9<d|M(J#wkZzUiRR-n6~eS_hi@1*6>p`;qS%?K?qUP$zigkBH)W`BkI6>=mQ^9Z((2gP?~#S!;a?'
        b'^fKrO=p9heowe2)&>GMd(9S#Q{kr%aoG#KYd(&vw=iAymQs4A1BlQQ@jMTpjwD?Ern_+&obELiowEt?kC&fnnfAxR-iXRa5L1>U@'
        b'l$ayYB+)D}S7M&Te2E1TCrO+vu~6a}63>))mc$~7QzV`(ajL{(iPI!bmw1lE84}Nxc%H=bCC-$1fy4_X&XTA|oGo#V#ET@(l{io0'
        b'e2EuJERk3$ae>53B$i2BD6w2(g~UpURT8TuE|ORyak0cD5^E*aNxW3zQi&gtXpy)~;&O@9iJNbzwSGwd?~;}JC+O`d%zEh?W($$}'
        b'4(YOS=KJy7_Wrlf|4DOe`un6K?~CsXM<u=~@okCkNIWL-xWp6htKTiMzn@Bf*3g{rHl8I1chp)BAHZ`0v}MF-SMI@hZy%{Id#KjB'
        b'8dUP4(Y_lzce|L=cT4<R-yPpQjAszY3o?P8y}#DF2UHC6@UZsm(f>|?e?+>yJcb|Z8OTw=GB$kYa<=c{0;W8G+1G<|`~i6f^?-JP'
        b'_JIz9Ou6|aM#$b_b=J2})mj61)^7Q0t#vnO<|zEYZi3qunBT56+1H#`XJv3JtTNem!dzs8`(Kb3;OcYhc%CdUdqI_~&N^24=f#z7'
        b'f2cPYSgL3j3s(-z8(>Pwym%?=hTBqQ&b;^>rI$YS%?nJT+rySB^Wu|&1JPJ89uGyr+^U{mXlwU1G&vhCXVG9R6d~1tB~^;WqEs&_'
        b'W%c#x(u6(!-U@lwKvL+FcqCyM>I=qvy}ji<jIN?){L=V>c~K<B)%zgT0pv1TI*G0`?k3?uUo;ZwU8=P3tIn0a{&+%JOION;)`f!s'
        b'W$i{~UO)aOg7NaP!tl%C)qrb*i4DPEm_qr(0e#@E{#Xq8=XcprzW8@;rOO`<M-obpe?1aa!u`Fy3cq7-&N#QrQ#Q)Gn7F(!5%EP6'
        b'u@Y|KGOax88ZXsDnZl2saP1;o3FRElS11o^nWM1?+MyR&5D|ppTsl)tLJJh{iS+jdsMO>>ht1C7pI;9tgNm@kP*NhG#FLSTP*kVc'
        b'B3LFBNTtL=^{?fHuJNA3(9hO$k7VHaQM&1pI;wCrL8|RJjK`!#Ij&FM{9Rlz*O(n95z)7Kyw}&~kIL%{6TukC24KKMV#-1#9_)&s'
        b'hx7*52YZ#Zp#*sh#br|IwNR>R=Q~}SsQJ-XrtAUYX2DQ+-FV$Z^OV_Dl5WcBJB>c;%Sd$=1?61j5=DaW*&`GUlGp+n_2G3nM)5TV'
        b'UtcJ!?}uC$;D%75M^P_{BwyJ(q`tD$izEB|v1?EUe_U2uO6O6cJsaa(FhvAHx42l>DN>W50Hs<`5rSG3RmHnj0{wJdk1oY{e^-w_'
        b'r*zSKS~Q_Ze>^>L@|M<jPm|HKBy^QAej2kU*yCuzP4>80sL#h|U_NG0%UlDmaKse7E-0>z6%7B{cqFzq#g(!o!tyCxHa*w8r%Qpm'
        b'#e*a{<cs%*68zRv?k;`Nee;Q+@Q2QXKE}<`PbeG@#u9pt)a|4+Ic@HxC|PeJMEx^b-nDdIKnVmBT!2UM^9NpK-2g^736;>u$v$7}'
        b'qhJKdi*Yp<wR(J^zG!bMUkb-_2mjhgEKyRbY(S@>du>HN+zrSI<F`nXKoqm^n_dHodS&i%me2fgDrfSk&6eUx&1B9=9Uh*@>H!A&'
        b'jdLexUyxsV+7pQ<d_vD4ils(ziM+CuROM-r>4RXBSQqp6@#|Mp9K;=^q75?nm?;wx5|w3jf5hJZPhzc;k2OmIv=>BcoigBYP}6(0'
        b'R$A*MPGH>xGp%)20~5!wk9tpAd#P(3G9SR+{~*?d`zhRob=HCN5vNjTwal)w?goi(<p%cXEUc&IWUh^dXJXBCL7jCbxnXhrGU9j#'
        b'<~@kRs|f#xVc!owQN&RQ_cxK&Zltp|vXP6cG+!<9kbiz^9!!_iS+`ws`aI+>5P2A0keY`Q#PiO1+4InOzR1J60E_e|<fXDw;A{4>'
        b'(_G-JT@cG}m0c%PcZwTgvpDdpa#K>kn)hEsnGY!cyn64wNS0Zu8r?7RFmvudHV+oW=bk%89_ETXgs>JS_a>jnL*k#5hpniC?J^I2'
        b'1E_?OP{h|42?XUasidwGQf}2QlsAv*!vP-??<SO-FT$@o&ggQ%fb4W*gvru{#`78QC;UD!C;6_6MEV%p(<$nCZ>d(#rg^9jQ1N`N'
        b'o;SgL=iKb|?7kRdY<_AzABO)zqLMo6vn8qZd=Px)Vo}dZ3G!BodCV{JakTWG*YDW^(cXz3#-5Vt&nWxH&NbtuUs)#7-w+C~jgU&;'
        b'?W{8a8U$?tZ3S%uZ3o>A+6ls=`Px8eJ=dl@?lszcGe{il0I^<_r_$tHl)}T)B%$^g{=A`cD4Xc=g%?~!ue+4DT$S&-_@x~m^!GwR'
        b'(dz}uTLqQx7Vrx+nsSZ}T9yCEQR-@}iz=<J<qR&GQaPtm`H!hZ3j1^7Rk;4=KokDnQpv-QxY%n2ML%{azjjr==dupE+}mB9!>;I_'
        b'31(*mfeVyh7erqxsC=)$`iTPfJq4YgFNl6kWaqTMS9tnAb1A=dRle`CT3v3ptFzM;jk*R0UE8<2hKF5y#>>kq2wb52wqOs^f4{(b'
        b'd4c<?g3fCSq8~39yuD!ieFei`D%kVPIC=U0RA=Dt5w88g)E7SX_k=$*)%?KUBT)GI)ECan{X4?{aOw-ie^2-yO?6KFd&0jq^@Re{'
        b'-xdDmynlvp^cX*@jTwiH?Cq&H|G~_vKX~{ho9W%+4Q$Wak$RG;vwR6?Wu5#(3jP#*ex&|H#Yp`y+?(ez`wv>y7OgXwEv9Bh-<A-='
        b'zR~9Dk@}h{P#LqA^cd}2J`fXW^P-XZqEc}NW9ucreEuEk25Z+yy#@3#+?#-2kb~?<;{fGjE;H7^etZfY%i-rxK#23Gv9quT?g9QT'
        b'lk-k>k=clN-yb!7lH|HgFrOS<1AnW@FB`VGft6nvseg6_vpeYCr)rZuy3S}n3_67T9%csnUikU_H6!%{@R#@kh0A4!9!9ytBlTNB'
        b'QBZSiq}~-FS;^7g;om4dFSh&+ao&Y=6-<3_JC3k>Yq)&5_1OW0+c;9c3AF!4gg?RTJK?wFdhkJ8{}t&N5E7+a4Sv%)X0HQ(8~As}'
        b'&6Xh$>9nXsz3uB__MVR$?1vD~;b^V340IUg-A@|qrY8*cxi^i}mw+w-m4f!{G1$G28SEcjK2onRvt`YFBlX{W#B3@3yxDRbm<L44'
        b'o#Hen8$_AtvsF}n;d~C1^XBNQRMuaB{>)F$;Quznli>2A^p)(y=ysU5fJiR0P$^=E;J(S7)A=%ZZ^C>SbOhu*pIK*YHQJ|t(QKIy'
        b'Dgc$iehB`&S2JrTs260lpT(@_p+@%ZH+=_w&ij(tatb(e*GPRK$OJlt_=<s!JB{`lVBIe2v#5`wg`G!0ZLqh1nn44*%@!q(S)aPl'
        b'WKY0<?-2TDF7ona^gZ-7G@+Y_1c9lZP^kTL=j2-GE8+<%7c1;sy|LEXgSfU1(zy7==q5Ac-xX#epL=I8YYA{4aQ8fuz4%;a-A`#<'
        b'VzQSkFxiWMZtzYa?Xn$4`;0s2o9yWOA4Pog&{ucUHww(ZkD{D=KwcZ`Tn$<S>I4NqJ)jw##?Hs;DUXGnsCi{B&;c?L&STbHC{r);'
        b'umyC?TG)9C<V6~tpfyx)|7Nr|mzwOyK@aUT+Wk~-pEBB&%S`r1KW(%Z*7Gs-%~5{VdIasyC)ItU!>}sH?jN1S*s&XG_Z__<kDaPB'
        b'*$<))=tFqXUbAJ{V`j@N;6<QnkQMaEd6*+EHQ5J{&P>F83V4Fr>9g4DfeJx&;Fo~r!aNssQPPIKu%*_jd=+he|46<2a`=aNHjU}p'
        b'TvpP8vTUXAm^9(mG1IN|EfeOg`${Z`qv*@j4{P_0-jK^qeaCFM?SR=*`(4C^d^Z5sfi`}Z+Bm`<gj><)jP^lFgMVmc>{{^H;DP6E'
        b'g`X;zzYDYi4WL<|RiHCL+Yn~kOJ>X0UN&3y0-pul3G=lxb1e@7{{!}yfs6JRJ+tirloNCiV~M`UAAE46zV{30gI_Y*6KJ<b(O$~u'
        b'M(SsSN<h0{A4MIX_d|@?ADJzMz`Ev<dOL6xXzO<LMc^M_H(MSD(l?;vpETNEhWQfse-lXGggVjw%w5=7gE-fm%a1qOdw`?&^Xq~4'
        b'm@ub22>%-on=NM@raCdO8q9Z<@V{p|`Zjnype3NY^O>~{ZWhcJGqHXq{U)UABnLz~PAtgZ0gK7r^rF%JCj5Ww$A}Yj@FHfN1-ueu'
        b'LHI>LE9e;NeKT-BXgB%2n6X){jBP@`O^E*x(m(YRJ{FgoP>w?wM|+U>qaWpcw8(-!UkA!Zdl!OCpyL>;N6;sagDT-x13Cu(MHl2+'
        b't^_rL_8||=U%<SBep&LW*)n=3MtLD)rxvl!BbBW4hGTs0!xNF2j-sqj!oL+Yw{IU~UxWGUpr=9462Fq>&LY;#ksTYv{LuvSX#KHK'
        b'wl9wXM&Bem7>L2(;Qlr-O9AF0)aMDzVV#4-I}<bR??*>xA?06<j_%t+ynMDF`0eR58~=4Q!RMXPlh&z5mN%Jy#Z;_ES!WT-cm(A>'
        b'3hIP;^pB&X#}V(T&G0|##3)^k*GzL0!msP@?q)~x*qiYCHu*<H+bP~ZkB;ub+~PfG=sfhYp>umD>pbRWoqNDLf!fa7H#*vbb-^Hr'
        b'ayEKD&5WZr;O}5Bcn2{V6(XJ@P%$qLJNr8NMtR(9IdRHt`OLd!%R?a3pD-Rk_k$Pzi`f!{`4-UApg({X{Ml@YfbM|%R^S0p`3bYd'
        b'2YLkb4rl}1D&8|&J_YK8`AOh!K}|3xzE*2}^Xs+NnNQYQEBC_u4VcOPP1v8QwLbJzt##)UwbtWL*IEPL6lXEsLb$!4Maa)Nz!ktA'
        b'(4_a#=YcPR_Z;w2;Lm}x!2fUH87J`^1@C+y13nJ?4QLl=z%x=m1R6vd*IhYMzZ2%UB_{iRpab(pCFUusa|GSv<fwwVs}A-Vn8*BI'
        b'!#H@#Z28sKsNWwOExK5odp>cy(LM|O@Hfns8R)CcFnd84z<eL@B>0~L{u1~C@D0%HucLlIuYmV);ESMJVa|UV^$FSy8U^iq2IU98'
        b'15`JYSsQ@E;C&r*-m_-QV%X;cX9EX;_W=t*Uxs-Uv<7p?5#)aj=*(}LEnoPynd=N&2=ijlF4+G#g|Y2_FxsOi`>xOOvwedP0e6B1'
        b'K~LRhv~L1#0Uf4i!@prH1CN6CfcAqDpia;LXdU8x9`W7|d>r&^P&4?(=P<W`pP0;;m!2=M_rtsdxDfossILI{QBV)a0Xi4_-Ecqg'
        b'yxFq;4D{o(ne_$O-+=v1*q;ZUeI}Op;C%t+CYX=Hd^fqn{2Q3x0-gX4BCe_X%$BbLcYqu)Uk&_T0b~6z7fxbqCvX$OzH&CrDQ3&7'
        b'z}2wNLOZ_>`%>WhKr48E!Sm>%Z<#G~VE%W^182ef7_bZYI`9nee+=`VK;DD3)|0?qq_-OB4bU?U&m09*2+9YUh=#Ey1|5aJTlbqS'
        b'(?A!39(}vkdJ6pcFuw&V2PHs@L9c;M!0l<^{h(!_wIEs}5mhoXe{G^*Pp}%#{UcABE%yS4K`+7l17LSI-)el@!1gsCg}n%TD`+O#'
        b'pcvGQ@$oe5UQjP+5cCKrF_l@%;Qkq`0h+N+Da887f${MT*iCmC?W;k>WhVPeu+IelSHSl{Shdh{cHd~uF_Hy4h4Ga0Eas+WS}W}<'
        b'?6iWKKn&CjS`Bi8ydcaACq_rVMG@rPPtqRWBO`5)PmR*yqdUJ5`75o6rN)3Yj5Z&Y#?Bcu|6&P!2;=-eLBH{cHSq&W54#Zoo-{Pc'
        b'*Z*~N^t+?-R3m26(f<U!hb_@x`H82&97ZeeSzgQ;pi+<pW2bIXoplY`wI254NE*Y=5QljW$c{PYU7(?3q&~KCr2e5ljgCG9%m@Ex'
        b'zzcyF0xN+{z(0ddT!Hvkjnuyb+zC7kx@h%C{Tr}f1$+(o3E(TB{V<zAPk<^xkAQkWp9Xmm=PjTgfgT1u4tfq$DCG~2k@+gbQOvB<'
        b'fhC|x=hRsj0P8?YK^D+ksH-N7y-pD3hfyndhd~L@KG3b8&x7*e?>O*4g~`r-fhC(#XWcpzX#sbFNKw$6SU<cx8|!l+?=rf$|2o!o'
        b'HTn=}Gs!o851SnL9R%gRhX?&hY$VYVvwuE1dgLNJynZ`6`VPk7e`DTi@r~5yc8=6P3cMdrw!?_`+E0#-J`ej5&^|x*I9RWp0_9_U'
        b'atxS*&BdGG&&S^4Y|s)L+gx($;<~)e7oXaiKX_w&_WV=(6n3lqf@5rnpA{NQr+jPfso8Ug`P8X7-#5%Leq_%BrcM8~=kcQ9XB2QB'
        b'JvGN>8h+4p>@!m~{bcw{Mccnf+?}T$x0$y8o9XDSQ#O5l`)7&<?<MZmQxDoqgLj%XT{mPi9o#x)_}-$yTa_Dars?f$@Wx6Qc20Sq'
        b';MDe##P-3&;G8MSR%N@=&*n@S-daTFlKvezrv~R3w!>PYAd3w7|H`S8v;T6EVn6xd*{cUPn}>H!x$&{*25&3czLgRkx}<2+_qX3;'
        b'I(9GO)A1hPzS9K8(R-(Ww=jSD0yemyQpUOYt&@f4k-w5z!#w9hJ+r7(`42wC1moWP&A&W(W68xw^O+1|`}xVo9~-qkq&$3G!Iw?&'
        b'vf7A0mm1%?qhO&~_4B&)6C5bG@v%|W(@taM)=CtLYTo!|)5Ev%5afSE_1|AWC4^%oFTkzF;MM}sMz(LAeAG0(A-B+cg<;isXA~~~'
        b'nfVp-<HP2M7ZhB9iZva5e9D4L@aO5rXFqlF=rdE4XCD0JlP4ee>dBwwJU`6#eAPB@Zo$GyUobuVZr&@C3eWtq@n?p@YaX6oP-56t'
        b'T{vmpFN~CTb`(A5{ZTgkH|&k!oXQ_4ujCY76`Wgesi|=8^yl9%ob=YV{0D~(n;$%h3R!0Q(;P$L)XF*g8nMcwJkGxBq-__q(T#J?'
        b'xzW#HsGdXhd*j-v)`lXx-@rN3H{X47a8Z$U5tXod?ey6@PTGg_3v(trx=r)uJi;!{`9GY!3s@6Z`Y=AXTu25@03(8JCj)_i+J<0D'
        b'uy!|zh~VY7Ko!xpyMPAKZg<t%>UP~W6IuvLcL7}m*6z-vrUq78z^<Z}mS9V*g{|0|^`~7{4Ip>9i|BmkOoEr)e$Vs$|IfoSnRCv2'
        b'&ikJCyyv}~%OF?3d7Gw#E#L9&7*eodhS~~}a}`R;@-LY4$e<0w+U-g!V=dJJTzG+BMEje{<@QwTZ6I!Y-m+(m=Z12x-=1I8fO)Er'
        b'qHYI<Fu#X1(@hr>Jv?F$Shh=6jagWvc@ipTYb=#7^udHs)DB7ZFPW{k$!IuacAp&Bg#-}&a>e~5x%}bMQxBDLnYSM*28^3d&(3~<'
        b'$?#z)^JSI^iF+8l$$J=lrKcV$<&thcR7{3UCnK|e#Tb1ET)s?~khq7yo4kj>S9<E9QcidKf#OoFY#Kvpt}G7pA@VjE1yb7jVjAW~'
        b')eDK;KNQo7`$;nS;nI^2m6puD{ZKJEXF3Vx-h^<9+cuT}qrz5D4boTlzR@JxD7Qx*+ED{Wx{%glj$m<)c_mrsMsC+hgNh5OSM57#'
        b'5-I(HKT-OkjeShrKY2pCN)XDKh}>wkmb9N#R{W)Qbn<*T_$^y!wGzb@gtbto0IG_;ZmptNYUEJ%c(=$|&$A9n-98DV56E3U2v*Ov'
        b'!+9dKrcnQT5@;5o&029c-_&xk8JK#gSI$qCoS(F5_1vXNNiGei^g5v1pjPot>vd(A<AYCZeiX>HB?A=)K{h`GvN>@~Xv@*0@J#Yv'
        b'UZ}1j4w_(ECV?b_e9JAq*sI4roGkfp(k4C2eLN}YQvW2rl`;Vx^?yT`KjxKx(5~c~#5v3h`am<uLwx||w%wdUOqNP1oo>hOiO9`_'
        b'F2+O#>kK-bjsR6u!-!>&hr~G{aq!zmF^4Bp0w)#7yjKxv+-8xppU=O=<0iy20^x8J(MN|EYbJqm0!oKHMO9-=8LTVz@$ikwQVy|Q'
        b'L~YVJR$9mGo|I%qLP^w?I*{4f;ojH7NMyEJcrDp88JGR2@GA7L+#nw1h2Li1FX*B0n>fyc_H7udav`MDf#EhY>Y3mj7zT`k=Mx{V'
        b'OMW@Yy*dd8ItuCpR#4lv%}7zHgGDS2JSlUI@;-g<obC6FtY|&y)uHOmlXgrc<uwwi7CTbfrOufogS8lC*tY<09)q}@L4NA&Nucs6'
        b'2W3(Dm1ItmQrLPj!u@IzAO<gR`pH7eA;Gee=RnRzjnWTjtVq9UoVR%<ebO#fX%Vk+^6D<lIG=tBv9ZAgrG7v@fX-PUdt`8K8MOT?'
        b'CdrV<i~Y7HtJS(=%q}Tq|3QWn{BVVCY6mr+zX(d}QBuaTJH$g^4AiJ)h^I1lERdyFD9p`WM&k~0*70zRT~Fzo-DEIH=#uhM7D9<g'
        b'-yoSEqzj{#seVH@TR~%Ewm>uc4+JwBjU~H>jI_>5D^vj@58;;@4m-{+r&64hQ|w2x6SZNJkp~PUM!y(L2GGyx$$)B+C)n?3SPV7k'
        b'!VjHNeIp@pV8z@U8&G}L98HVZtez7WL{#IRmjTCV`NpGlIR_pm#n~%1X3H(<2MGPV;A&KNhSJ4Y83mN7>?KHy9~?{ruFnd725au%'
        b'ZO!d~3(wyuh!3#M3oeK!L(58E4Bm4(dj*pCFP>CoudpOu;TMR-m-#D1E1{^RJe)ZH8V{T$@l|Lupp1TdOHi>7`VXZT)pASF#`m0v'
        b'(p*2g!?pds55e@_`Y*rZUOnjp^^pIl_v8ORd@<kLvg1&@?gEb_Ek*4IzsX6<HcCwYyhR4v68u^KBa`sdmRoX~X}+~KNM3U87W3(?'
        b'gFzU00${TiVLrcQWOvvEaZA56#WZ@Ug}z~MXnAq*{(}_~GRU0dC+>yw%q6XInU~82A1c4ot6P}5Tio$mcIkf`R<8EewC!Z7?loK<'
        b'O!}23`3XJ}bNJTWJwic6nIl<#9|XR62@r4zQxMvXvRhQm4(8A;KrWmD0{+rlT=`Gq-+${t+r6u}_|NIdyuj+v;{6NL3-4aO>IKZd'
        b'^>D?!dlkJnVt#k4?){F^Foa@v2-*X$@u?0xeGBFs=b7!d9Ne7y^a~?XnFKQozNQUifY4_$#5pppV}SNG{rVP|T4n-WrWfrVg8A)c'
        b'Wpsji)2;IfN-ehBd^yZPAWSaovUW8UO|Y~sf0S2e-jY9?5&%?jw2_@;vS4wFY!YF+L!*ytFmW^z5r~pu83`$C65>S8)bv}Vc(bS)'
        b'&jxL+g}@E6YB940zQN{K!<VekTLw|w{%Dwy3Nz?%kr!cFkj(aOyPiPS+Mm?DOEHhYQt>xD(qi5{)I823Od`xNjFIxi(Q+E-epTAt'
        b'm_@hr;N{&(X!KmGS!V)cfKb3Jz&4%|+Bm}_`ZH5N?}&66`%-i}QYR-M`WRSfUv1q(ur6I(g&gM1hk1z~^Q!DVCR!*T^`Vm@D!P|>'
        b'^p*|0Ox(_|7Hmz-oLf=2!FFf^@Dt4#%FKpU$N*B#*6ph%0ExmF0RQ&K2?ss9U52p0Ah54ktCTEF`O4st*Y74Om0kcE6|>e?fOkNn'
        b'61MCWsvNu!btvGGf_3evse%Cts0%cZ)vg4CYNe;+oNb>?q(ug`ix5(@HXu3c_C!YdArC1nOm{^79yA=KA+hDlqn2t_$)fltr)=v~'
        b'%^(n;Z?6`=BYm}SPF?hua(hcpdxmn)n)Wryw9kUqrvs<Najut+4AiqI@M1_TC2Su+2DKrkTiDnUD2`g1*vBux4d$YKAU7A!+}QYC'
        b'$KCj)>&*E#p}jJ(6SnXmz!UD`L>-IRqR|s&f%@=3fivYH&0?fMs`}yX+kR)YWl52TZmOO|nzVS_p)QsDZutrl*RGG(#wW#<ep$F4'
        b'H0Yh5se32PnxJ+9A&F%HCdNIHlyPVw=~tc+6%NAD1g$iF;Z#$yG|>;4UudnTiYuvC_k=Xf`%+%sGS!}}tVn22P?|ptUY;Z#=8?KD'
        b'dudHzny-IG4eZ|nsok7z=abFAvxj})Cd@>IDoB$0(gTQ%%)1crYA@n4V1?orMkPd+|2)|s@U^g2TJ87ho;h{%A>y9@MBLN@@j|3B'
        b'GQjBA2TZ4+Yu>@M$>}yeIXNE)Jko$yW1c}C(vgLf*eAH<6SN;{^FzF`FYSi`?*j3?<0T0b568Y)2yhdkP>+aEZ=JAV^#!unQYA3)'
        b'jy<;045U<vmS&)u&4`Ud3-&<0Lel}4F$;>Q^%LB0CP1oA;LEfv_!SsJsAcFd<p~UHrVzDug0oBje-=*gKrB5(Vx!}|ZiRCLz%$=k'
        b'r8smBn29C0GaHFmzQ#rekWX`KCjfxuB_tnSTr62LVGF|m(WNYEt=#8Wf~N=HanPY~uCODUx}mDm2NK_JhywJGf9H}W07dF#K%KED'
        b'z)Kv|kzoPp^^>sq7ZW@Af-P47@Z8YmVK{yzKc4{e1UjxTM0U*ywOg$V3qoeV1k5S)tE!}zO9j1I^5p*q*m?i&u#|2GP)C;E@N6`t'
        b'T7*C?U5#6E`BgGi2)~_u>jf-}n%KDyORPcSPGHRm$lQY<CC)?Q;(i^mZw+}QE^blIvsiuwl9Pue4j?(Pn79bBoq_(?;_-qL((UYH'
        b'pkjU>vJIOcLu`>zMTTk|>Oq#s??mP<gKdu>a|^(4{w`!Y>%Vhfqk3w5djLjaahtIG6NoO-Bt8yG7>M|7fcWRz**Cy@^Vg6h@or>3'
        b'Xr!oQU|j2$uAfrBH%`u`>6NxQ7!^TmrFFY^o~M;t1=*w5VToNpdbhKA5M4fK3lm>JoMt5F64v}FqCPlY(lTzNQ?~s$4#jB>0Rkzb'
        b'UAdK3ScM3VUPq`)$5+Z}TEVrB!}v+K*0!B3gMFL_UW#|dVu>#BQV6Nt1~8;=XJO~Wt3alGXCNl7=Tn(+G9>L=%r;9pUzB23kRt2)'
        b'yqY!2bZJz{(edpceBwn8#b*uydI4+@JKYB_75Vc)YkOfQwjeu?VflXq$s*8rGs|zYjBlSUQ>_gzDF>W*sHG^#kFB(Fdo|zOBk+NX'
        b'i<?8UY-B9f{0D?){~A|^HUAa?Zs<k6IS`aPAfNvSyc`CN=NIzZ(#E$(u22;`%9V|i^PDw&qVO%*Z7avQ!f{)qqK<`Ajwu>1DH^Af'
        b'2s#&`lMy-trz7J4w-yl1OAxhb+&halb@yvN<;B8kh4T#0yfjW0Kyrftl|nZ&h~^=l$r}ePsuzwsvX=n1=fgX~>J7s11P}+W{#_kC'
        b'Ub0}ErdMp+I!--K7;PvWwZuDM^yVdWl!6RR+|QFs#an=#&Kcj91L=yA(#s%O>PJCMNSXRM@UmFdH0n_!Aldv4uMQrs{Uyj$G{4EG'
        b'&KhST$H9Q5&61KKV8C9$z<{x96e(cL&ia@99E{l;4{<sYj#)9S6qoX9(RghzY$$&_ug1X3<J1#`%F)IpjgxZcAzpvR0~`Q}u3(=n'
        b'5lP7$c}BYP0G9s<AM@0>Elj&JSOlU9z=6mPEHRi@4~=n;!^X&Ykm{$$Nl}`)lMahi=|2@1oH!G(lL;N)rXTn6a;5AZH`Uk1yivdS'
        b'9UhMH3BI`kGQS#ke#DE*!0Wb4V`Q)+(o9O&f;=m`BmLC%ZF9y;XJcf+)^f$-@tuLsY-eBJ8MtEpY#<Mbv-qOQZRf_eN3Pt|iHTcz'
        b'^_OGhUO=4Kz$3I6ctK~>%>d==s-`A5SNwPcz<)dq@8;E?j3w^j$zW9>vaNp17P-=zPwYO~ZdVqsQCQbd`Srf_D+d)}+hAj*k%om#'
        b'-I!`S5fQMWq-M+(wFE~0o0l-XW2M?hKZ*i;lvDM2HPnt4J*(Y!G@#uN5la9++Qte3o@8#06_kF?{B_J0d|+AE$IYPUbnX&pLu^`G'
        b'XIFLp6we$Ob7)tvP6GNt4ochsWahw_4OqUeiRKZgvzdR7X{FO^qW>BL9x=_nn?XcYEHi}DxNK^O``@t!yy-B>92tWi7cen0sEP4v'
        b'5!AeaF}5*#kZr@0`Y;1<HKGW0!<e3anhYok^!a26@RJtE@~3=01<=pxSH^&frs;(rL9?<zc65*JgE#i%k#k6ywK9*j?r15~pRwr*'
        b'^Q;D{=qw1~TVCUikHMwIUf^jvIX-d7%SX)!ul{f>HEWC{%w~kv(9g&~;1Am5YJltN{0(nfJ4Um-EogsaS*Uu?nAh;O4CP!~N^8Q%'
        b'P*Mg*(H}t~mMjF=F>6#FuruiaclBqix~RN#+nt!djx}IFvNrQgLHpsGCX-k1gbg{&;ztJcEDsx+j0+Z-zd;?uTrxDj+e@3eWX#Z{'
        b'TB3|uG**r2!y*7TNL+75^fZ=!ZKghZM$DeEq(D0!Q#e+zA8X!=BwuwcG>0L}Lgc0eV~!1oIa~uAAj8$94Ti8}I;kmcKb9Yclw!CI'
        b'*I6rd4l`OX2eX;+LmSP+Q+oU<Bq0om4T}qsa<4#MIe*|m-7v#OThN?%JsAj4$7~%-ZqgYPI^9Uol9<FX+p{z4!sV(j5$?q?GmCgK'
        b'c|%k3F+EMzg~?Q>5iSSt)%h!!`EF8^;X+&xY0&FpO!0N`j`-4e8;QqX04SQy9{VCdH5KIeH0T|SOnTKmvtCyE#S}ssYideP7CO#N'
        b'+0Uq?L3LpgNB9ir^22YgUR7Nih|xekn!^-1L5oa-qmJ-pK!-}UJWfKLW8R=Jhs|?@MJIo44qH%p#=K#s0IYO`&9|{uYXVhyO#oB6'
        b'Y)R%a{qm|x8!0_<a&B=|W2Mc3;pVVtV3BuEk)iBI`)Uqbfg0El?J7-51CXUhPCg3ZN&y@>4|w_jRgInU0iQbT*f7tPeRNBb1Hd|b'
        b'unq{jLV%tBFzkF+UD9>{SqC928q4dz7?FEx$^qm807-`IzFqwHeO3EQH!QH3F{@DsIRl9kxl%nY*DX}&&6t5sKO<I)#tZ?_;}47v'
        b'XjUPdbZjoU_e183QOLCSdHdI@`ri6H*L9ez;StYQd{Wb)4{gMghjLxl%^~7t8)urPMwt&r>(|>h1}0q++~;H*3|~|H1$Egd_suBO'
        b'vnvEwP97UitBy@HPeFf|(v6H~&)vB}!F@lf|KJTWR7Wd-2zh?a$8?SA0}+q}AgX<6R>!ERel%N!(5q8O(I#BxIn75*VxHAtUIKMi'
        b'fLpR&A1(b3E1e@P@LR`xK5CP8rc0rsumuq%4Wr(T729fp**YpL8?KggVd4bDa)MWdpqdkW#5s9(go3LYtz(VtV&JkfEwKB!>$6qj'
        b'WjPWu#LJGX&qg-^?<^k4Iyy={PZ-xIQ_?9A5u;>cwh764Vbq0YM+AcgmTjQCn>(dJgwC$B{)x!`V4%^i%oMh}ytJJ7379vEABI``'
        b'6EL5!55t()QDdwkC6)s7OZ9cX>Gz{);o71nt1+MeBd=lk$9Z+!DEIQ{w6WuuQ4-hujaUC+R1ZvEc%;hK1NG5Spg<rKHjl29gD!|a'
        b'<vTYlf+)fjS&^gZ6R7hrZ)3FuG8KRV{t5TXQ2>_B`e!GU!vGv10S^<aVco<}U|Xzp6Rv$h44TLeSLCPyoGhQShs+8ZZIFQ$5(fYb'
        b'mjQxr55<d*@v}GhXZeqkdm#x)qs@IhnFx5@e3XAdod0*<8j)zUBzM%Iom=TwvT2mtG+LTF*QPZ<N69i;>Gi`+Iiudy6)i!^LunvZ'
        b'ix!cy;HCkwK(5o|J%iEbY}9l60KZNIzL@&lC{)fOxIB8IG+e!IG#f)s9EetTjBsgyW0D9x#-#unohmpAj-|)~xFlmB<gsvPj{t^7'
        b'y=s)kkfI@O<)|gd2LzWY5YUSTOcTg25a&a?fv6XcYB9m^<oA2~6Z7<_VA4Y2dQl-Bnf)9XDadgQ0bYNvwB*UrQa_}(kU2BLJw9sR'
        b'6=A@*1wcd*r@w&6><x?%+gV;{;E}<SsL?t<r0B&4DW@IHALY5oQICuVF91I?XS5pguF)ml^sb|;M@yy1(PX%ihLk)u>R^l89v!Wy'
        b'BBf;EtA#W6oC2*j$&pL-O)HR4JFrwz3K&Q0j&!XESjqIWfD7a;(jFI&=@`?XT^TcTbWa_5DDp3I5~D#Ctzd^saisXL>B70SM;2oj'
        b'&gqJa7hW(UjxW|8T#Pxsfc7Lbb{;Jr;z=xV*t=KQfX&BBQQfAx8Ev;m+*2cUj%D2K5z9*1!8-r8$r1NB$VtkF{w^~<!cB|-GAFcf'
        b'$aCGJBT>rf)yztm=gK7?X%sf3D|2De?(QG?_uxolmBQUS;w!Lw3vR&N8ebMk3Y8m3UBf==G}>OJIEmJrf@LR#c6QaakH}*)V^N@*'
        b'b&FtrJj9tC{CPQ+_%kHthY<s=$LB0sYP_5W^3Ud)z8le9L5(en^DPkii(Gl^qBT&Kc9}nDOi5V{=kT+zWF2hBkV_KeEbiP$=IXqZ'
        b'H7F}gaEK&#nM#!1%x4<mlBS_7`zVqbt1xbWWt-tn-}YP;T*%EOadKAH>m$X_<{8(ZnF)%N1PGFx8#hO!|AN=)VD%(d+EFAWL7`hH'
        b'G!6Ih3{q3Zh;REfS6By<Mh=e~AWv^;1^jR-K?-TDD&h<O-NVQnBeIVx-UqyNg>V1MkZY;{jVPw!g)aKiyP7{2_KYsDNJ`3%v@Aq7'
        b'Oc~pEwE8#rgL$iI=iwp=T;C+;zTNl{<zWA&xx+JsBS^H;N-J3FD<B?W@<*&y3ijT*7?U?b)lm*D;%Si-3wH*x5PcTnc|*eeVWjQ@'
        b'-or?m)JV+lMh^TMap4V^=Oc+D3^|a1pABiZDccVzqwVL)>t!|NO5ieA*!S$M-8RygpcIyPv6>GRrr(ShlNB{y4r*IPpoP;C7v3rc'
        b'FCW7f33zc!&bndamd_>Cm~)Kx?38f79HD`K^R~oCr{`5k*7J~{%=akgF3F$`AXcv%0d`@%y)2*|Zd#f@<#Px>%??Sm*s=%I)8Z?j'
        b'riqfSuqO&@RiN!pr`xN>EG^UTT++yV;edc_uADlV2ONL}a3Q=<<||j5MyPBfMG?NVMu)J`lm|Q=7tZfdvi8Q3_>p3l(puGcAqrvQ'
        b'Mh2^tBv#W6)!kWXBdt6CW#f^>{U-$+Qc630P9o-U*dgFoYXdAVN?Nu9r}cG#CR+d^>6&E^C=&Lcr8XKX@DtnhE;C$#P6I)J*DrTk'
        b'Br%Wpny_q=6!+l8?+{Grh<eUQvEAC9tW1+4%V{lEG|P$0(pWSt2}!w*gPvE&nShZLTCv<7CDmj}s&UKCX<k?|C2Hx2cMnaIEvf0j'
        b'YZ{0W$w>QNrM2A3;3F=-Q+A;F(xVW|UB6Nm0qW1QPwsghjGX3Wi6DP1*)-?fv$H%Wi5VUCQmA=BVh{L8TN;e)?q<ssr5Q-QwD>ey'
        b'Qy-(n4(!ET80%ijvLdE$81&M!7Eq=6jfBL+eLP~v>ZR?cm5D;ftv$H)Z32K(qJq*tv)oeV->?QW6mTzhyG*lM67xMo3i!DO;8b;q'
        b'08(L#T|jEbYHD}bgOSr=Ef?Fq9(I2{%zZOl=NQyX`jttG%hBSpm=oo&ie&T8>>250cMtpp*J9+a0ZKsLX99VvB(O&tB|t{u|1b2?'
        b'2f6}CgcP|UQ1dAN-HJOl8lie{Y5@V}7;6<p2LGs84mqAF0ZbAPLb=o=OSb(361?>Y<ykHP_Ee|aVKnXllRPtXN1ynLsFi5I!GJK;'
        b'!@{<UXQ`xGqIrIL%rr|SS<d0zx2wgT#D{8oD^_C+3+p+}U}ktSykq1sNw_kI)4Ak75pLbO<Bnt+E2vx|^!R5Iu4ve^dKxG5N0_VL'
        b'J4{8}ruT-JLYQY`f1$PyAJNL0w*-(pF9;~t_29Z^h`0bn8#C-?hB;<<eh&<LuKF==LeSLLhhttJZl{&h8Y>lRb!ZSspI#IZf;qqU'
        b'6JiNOwc{>`d!Szw2A|2e>E+?*1n{<tFm3a`B@r#xncogyA)@UrDd+>?`CkHX7Wh^<K~<*B!$5sf304;Y^`_<$k?0X(YRfR`H@(vZ'
        b'=VtaW%@Xz{MZthDIjui4m4gjBkBKx-`u4$|1LY`~w!q*06(rvKB;{m?r4S?K4i@v+F(z$T&_GP8?>7bh(n%<@TBzfFuJmQbtPoys'
        b'=usU?^GXd+vg*X)J+$EdKt?;*jm$DZ;D=!xz{L-1Hb5fMyrKb*5&Z(ba>ilz&xT1k+tLUSfQ*PV1^3Lb`)OaE&<1yLXg*oTN|^+K'
        b'5aG!!9QNj!gbv9VqfjP1i$W~@yt;oVX8v&M<HOVvMa;Zm_59&Q3w65D_IH)hn!3XXd%Dp`H&WCnvrv$_b0`xlNKhGOiIy|7gw~$$'
        b'wx&7dx9!nkvjiy$@@&RTe#2yNH9XB^OF$T{AWW$Axb`9$;yKJSLBrmIH_{`8i-h0lvt&X-P%8J6_YUCrN__`#N^=noAI=6m92x@6'
        b'Lr;(pJV62l&KaAb0Oo}mfJLfVcOhLn7zw09wP=)_*>-ct-9OYf6D}$+n9vXOfhQt}d*4tcb~1pu4BLq588Y<@L7xgYdJpH|%=fUs'
        b'^wkg<KtlUKCkW@cOvp3vC>xCmW1sCCd%aTq`Ou>KWA6h6&oqH*01m_f)JPFpr+r1}y_W9fGp8Wh{0^W%ui^+PN^h6=qXBJvfZOP2'
        b'LfVp%4%|<Te2Dug5qEM^*31i8iqDo3NI#Bc&4M-jM28UMI&L~Ugb)hkdLX$qAO54q<{>H4q9ZdCK?IY6Wd$MM;C?ZvdkE<Wd<p&Y'
        b'JVdmTkg7pKszg2vl*R;`6chqr6bnJ!lS8cUj^ge~O^lrMhx5_lR%i;Op0gPJZWndR;jS5K>$*u**_e-qyyERvSQ@0Q82BZh0igw$'
        b';260Irb0bOq+}?p-y((2^HQ~AXfJ2Lv;pyIIt%xll<ws;jo@MVr&N7ts2UZDP&x~>)Jv;T%g5m1Y>@(iKMZk!xYYrFeNPTPjXk(='
        b'6+vQT;0u`X*}Q6zW;b6gvb@Hp77i_jf>tO>wGVlJ3w*!%zTdZezi)bfnY^LYydgn0Q|=2Y&=7A7rM~e~`M)1pDf)@*SBFT=e`W)5'
        b'|2Ab>+?{ef^*6A=C{g5oe_#@~^3{ZMD=+4GxTvWCNzC&bU@I-Z71qI_zq4sbI4((IR%=3JS&(|;&~A8m02skwib{Zi%)RrYUY5ix'
        b'87kTj^dY^(E2lt*sm#23?GQYP<B(op(I!WR@k0uDU~fywXPOSzkf8u=krZUS4<4F-NX<)-#6e%Ix_pS71N;gmc_>OM9N{UH4w`&6'
        b'W~ne73GfMZ-4Y=wJiX@`%<xtH^PzjOU{MnDGcWW;=GIMUm&d2qHHBH`iAB@*AfCSo9?wE_+NR#+A&HD`=>B;R&lFF}LEgLv@+_@l'
        b'PCI0|CZ0~Wh`I0~V7D~?6np(?7%L8ysE7903Qk5d)KCc}ygpX)*bqkzRg{v!2T%EzJUUcCgGb~^%*G;C=xUO|iFbVbm@`x|2Udy~'
        b'Q^gC(;G!RxfT5DWp*=Ji9C;EYrB<(N>h)`jUS?+c2xMl!m*(kpTpNw*X{_|@U_4glXFEGmPP?R)0iIhRe2ffHMZPOn<3m)eLY;Jz'
        b'ilrQ9?pQ`ZL_tlrorO?o6mSxN+tM)$%a1~uScUEwRgE(KkgMG2O<-xq`Fixb(};TTCUsh&ehNG(`pY|dHLBV#;rebeT@Vy{GJ`^$'
        b'?wibY_ySKO^uiaHk__|=@<%IN=y#_O^}oQ}SE$3mlX9H9W9i{ZJg#DfHiir=+D_9!bW<<2C~tv?RAs1DBH7WGx$kcRDRU0+^anim'
        b'9VDn99`xYaZnlE(f;k6KBtj)vjl#vUen4$zm5$Zz05qqbxtVfWk?IGYRN9w!wgZ~K!MVnp%xPFF#Yr(|1ezOeGAH0mwS@WPrr;c;'
        b'4~?hCPGqPT;HtMKxO#xr(#a?Oi$}O)H$i+OVva&M@hA@fULF&F2kkasULA`lIEt~r!oBVlwbiJG!bq|K1@qy?bS&qU(HQ5=8d|BN'
        b't$G&BOTi}zja@<K<lUSech6xl_s-4pv=X}RRaVP;Vy_?5gv~4|yV=-Cw11>LRcV)94lc}&l2vYRdDey12Uunx@N``lb}_&eeB>F)'
        b'_Z8tT>5-2gbL}e3uG}6ab2J54?n;06&Z%;PU*x{8;UfOqviuR=m7Bhvugs3hwVe$v+}`Xv<LEpj=5|9GqN^-*V(<BC=Czx^M+Uxc'
        b'E82iXp_bWVJDL+Lf_lOK-W(#3m~A)dFvJ#yQqfj2@Q5BI@ja(c#rn<{y?B#cE*$HzMTL3~R@yd)GC4P=*JP&SxU8F`+;UrDoQJZ9'
        b'O(4dtS!lY)pHgw^b2ovHEOPD_GwW}jPf#vTiX!5Jl7cT9%A{wt-!Bv`dq?v5Nuu}*>I#uVViEolZq-e4p7XZE^G7kz_0H)ze%~`o'
        b'zDdr3z8PHI*|)&EC&M8&x1vyKbL$FGGATYaIcwdv&CKsg3e`nvq`gp`6DWdC?{OSJ!~6X>yx%{9!n@#~eQ_HR$q{5Jysh1Z=NPg4'
        b'|3$_c2O?6gM<_f$VX$kx2K$Sf&|aSdE#c4zd#!dGG{x$h!1@|ubnaw>Ne61x;;Gn8V1!fPeduDU3kQEOb8dRIxREZ_nb{;lkwu*+'
        b'kfrDGY1>_U&vxsOpUU&nB~bBJ6He9QPwNpBm+YH?V7SVPV2!*E!4WJ_R~sn$5)WuY1Kf?f2PtYFAQJXF|8EGASb`w`w;sZ-fNr9L'
        b'gMKLJ<2oj-u{|m^J}Y_KP*%WO^|<P*+i3Tou^mT5EKvSkgWgDk3S+ex-INrM&Bb)IE#}%_bSy%R01IYp57a%$YVlh*=s@ISHkECL'
        b'8N}RgV$E?#>ZL&>L1#`w5aZI6)vP%H%@838lsOI6(ui*9dV1=Z^=H@Ov10HDz|B~o84oiPv1ZW{v-nxFWP@4yve_@sEZb+6ziTFs'
        b'nf=e0XMAm*dCjaCHY=MSLvmtwBRWuD0UiMqc+fiV&>O+SoB|$cnc$JV6+E_E!NXPz9;GaJIBLM7?mT!jwS&inLGZYW#9WIXQp8--'
        b'XDcZ9REAqx!#i5TH(i0(O`5FX?N`FH`ogdFg>SeMe*I1}&#S)j*FT1uxIsxC>@E_k)Bg%c-%{feF!UKutPh_$X25h^!-fFejbR+a'
        b'0x>)cBVsYp5={IoCfR^VU&j3MFxfs#{w_uy!~D-+Grq=VUc(f_n6H1JJ_75b!v<Q14IA`2eAr;t5yOTwooLvQtrHI$w(BIr2AfVg'
        b'Y$(<F4I3Of*|4EbCm%L6>HLQc7j!d*4OewDhYdqI#ju`M=#=28)CCNOYg)tKYYmT_?jL(4T-_J$=nD_K6Mh)>Z%7@G!6a=nWYKDo'
        b'=v$tC43l8p2(19_@aB@=aX?0|W+^|b#&b({aTnBzt7>Kb5KkJxEL{2#`j8AhEP!arAeMzFPzq@a6z#^*v_VAp><x7t*ImU;zZlff'
        b'3gG3dE)W3Rpo3G+=$&#V&7cv?H=<Z>1_0^X`OpO8wZOT<#u1}2wz07XZ)_zRV~b5cA2i0+B;gChxq)E*iEjX{+T6*1_B;FmnwlU@'
        b'b&#eDkfzvanl1!>wjD=f9;WH>2WYzRAWe0+3Hg7cDdZ<<dTT4x4NXuF)J^LFh5kX_oq=>7gLHlk=_IG={5o)HE{@6`rc?3&onJpl'
        b'=P}&$-N647or42EMW-kS(s>5bdF&pYvB<r(2r?+^#=w`)B7sIEfoqRdwy#kxdbJEAL%p`98Z%B?8_fX;aESfa!}ad7!ORl_))oa*'
        b'J^+kQy`-k1@lYYDDth`QKemEmz8P5LD&2x)H}jeUczO<RqlE}lJGbD?cZ-o}pRi@XE^X05n^Cr_sIbg%kS5BK4$^&gd;Trn>u;qV'
        b'?3bIDJvm>pVHWx6vb=CI+!#weP4E5`a6$}kiqF0_ND`?h2X=|tS1VfzLKAWp4wACwaOCXHmc_dY@+bNAn{vgQ@ZoC77pUfMsIE$J'
        b'7LBX8F4^#kJud6$KuPt$7JET_?uzUNaWz?vI-SxoRJD9c{oX)Te)N`2C;i);18(QQ;^#Q$faa`J?Hq{KMxK<n9UgGA1B+jTl(JM%'
        b'QE3}H;6604`1gsUyww_1RMz&+fV*s9@!rIny!y~UbaW-Q!T}u`5IK{Uze!agWBIqeJ_GO|q2GNI9$jy_R8;3K84wnoiXm$k5P}aB'
        b'^Tz>w7?Oj}tbKa`06V96b`iAz*w5O+fyiT6tsUlidSPz*mb)tbT~kSaH3po&9{w3w`tmz&W}txpZT=p%DfaH)s4ig4?tzkD4?wqC'
        b'L^n;*G+Yzz;9D-W?Hq9L9N;z&)N#3<da3KR2FzJLecs{)tfdq*hHE+m53S`GaMo_a{TIQ>R>$|p>2IoY2C~uzD2+ApDK-5WY?+)5'
        b'>2Bv=lBI_bZCL~EEYSEKE@i+|Ck39R=SQC1LZzQV+SU)ap94kv5+``go4|`v9NGVjBSNA(Lp6vzf0n{K0~3G1fR772X3rJKG*!ri'
        b'>(vG<eKrCh80qEcwiN^J<)Dq)M0h+Lo~s|`*)tnb{y`ZJQw-hjb!I&S`~pJ!74MB1;7Xrn2=u6>yXcI2F<=+;$e$Rv?^{u3N<Du7'
        b'bR`E<y5|i*$DgoF2|NHu+z|tDbr^Vpu_K&)AUl2iT~*lK)W`c9@KzDLg4YW(Wp^Nqs2XR22kzfV(WN<b*)|fp{3PJ4*m52~7VT*j'
        b'1IPKVklL23fTlS<nq&{qWSTVqS9uBNxX6yR)PvaeBfKTVvtR1SMgU5U3`SsJ9%W#?uUH6CPKeldl?3n)O3ZCO18e!VjTmr?1~}0`'
        b'9m{yirO-D+MG+xi!_S;i3qMNBNf7+CKS@b>D_Si&iF(8YU{px@%Xjr^MD;8PED>iWFQ>^M5~mjK(@~kt9v%udU~^7_%){esG?fU0'
        b'PLBr{<OI;3eidoE(eJ*|&vo|KaZg%GrCxv8bBl-wF*s->y&Gw}*6+U7&;8h6$DXnjOKUptnwo{GFVUPOm@{7rLIFiB6_0v8#_eca'
        b'Fpx=01_*X?mWVZ#IJ{kSMcyjc6yb@J!a3b@{l5E^*F}07IrKH)RssHktmsnPm;LURe(p1X<wZ}S6o@uKti!4a&Diw4OL8von=uf5'
        b'O{Z51>F#^!xiBoY+>2Srl|s5}I$g)2aE=ebYgLGlCcJarmj)3pNZYazGSqq1cTebk-U`dVc`t83v_xkinqhCfd+DL+G^ha6-8@s?'
        b'4<xmqlu#e+k3y@_>1$W_U_6~XQ#=jxCjrJX^dB%z56=`#!@LDx06M6rqN(Y9G9SKcJoATXxZPej5P|*|9GLzf!W;1Q#hYjO7s&I*'
        b's4!Mz2Zi;8_CC0#@nXMSTBa?h%MAA5a(!U{v#Gz(L4xp&l-jbNvSr8FvJKvPsoDKxV715s2+o8PW|gd3^pYI#pZO(BE?<6RA&958'
        b'fOyLNx4yQZzG^VrnQn;0{g=KrMPDV>fJ5EzEQGG~-jS%rivlf^ym!I?dYy?xdxes%w1R;dtWs767RDBa72?%sA!^G)o#VU~^~S60'
        b'2=gIqnqo&8WB<K7R2n1US$(%;alcJiy|*PJ%%Xk=3zsS#NkWbvT&z(Uco<hb*>9z-F3dB@d(!V({zdrWKpkxF85vUn5g>U=)<sof'
        b'KG{%HF%x|zZNE-$jr%Yp=3F0$mccXf*o?ODes?&K?m{lS-}9W5iH5Cs?Z1iYC*i7^ogf2rntc&c|F%c^-E#nNNi*C~7Y-^o8;P6{'
        b'rRrI6+w6XK04V!Qb1&4abN2$tS}dv!=r>9GTd``mfSZ<pFoCfBqD%kw?{Aaz*ZTK2u};mmn6Sv~>!Rif0t~xJ<PE!)1<Koqe)m*g'
        b'9b23D9d9w;ZGTr8Gt$StYjqCt?G9ztyP84%q1e;RqG0+{3-e5aeGqFn5;<!|+gP7_3^a0v>+Z9xl4|}z90EFTM%z%I`zFZ#EK%?)'
        b'(u6ZH>j=~3zIG6)hr2M~_gJp;ixOOf=Nj*+1^P#(zR*Vo!o_AY0(IZd?t-VL29!WmXlW*xANzc2SXeK-+$XFK3QI+B{>y+|PsjEh'
        b'Jo7EY1O`+%%ZK<TBOK2**ox_&eXPS&b(oeRQy0L9wWleC&HY?aOl`03DMjxw=5q)KfFeU?kinE8Pp8|_5}Rq*cL<MONX|-If`rm~'
        b'2NGA>2pWz#+zUrdl;~Z{oZ8Nu@YSxwy{`*o%rRdUWizq%M%zY&dEb}gxU?7n;tf?FiACXz3+8Ka2wT;tey^{Rh!Tl?cbef*Ert~;'
        b'rkQ*%*(T;M@TH`zZ<T0M_}tV3uy-VJ<ZxK~n@Yibv`Y&D4510YI|Dft(>b!xgv4Rrd}H?BrzRz#u_^&cP$uJK07Pv5#_aW-7=-jI'
        b'7p*guiw_3sx%j?XYhRV)515TbkDSJe3#pPn^wrAxDoV+agQwy3LpvquQZhte3DF1FAH{I{@d<$I^<Gj|FMS7pwJ@-Kk8+RAE<K>V'
        b'do~oYD?hKl6k1jLQs3O=77PD^?9gkLFL>v5{tCLny|)$^h;F`28F$jp`5jMlsCX`dB&pk;>swwPTHbzGsVi?}>BdE$9y|=sKpxzW'
        b'i5Da4)qU>}(c#O_9Gr`ZDMbBT-!ANTPZq^}`RCG2L|QgNTL|^qzIcrROP&=P8;@z#@ggdrQHz59M<<Y&=PSNtAy9NN(hO6wC|+2P'
        b'L6~Ry+D|DjP44L#nh7Ut*Nmdy*3?<+<(+>aLaRPs^rNw=5%_nZEpZiC^N%2Y$iD=91~HrrwNLc5S1N0&tXDBu^FlOI7l|C2apI9D'
        b'+jM<yT^|<%=1spdSbE}-FnD@J=2Blo*~&&BA+_`RE>)FgiJG#+%se<+XS2#u9T*Z?9$MuvBP(`>(#@aoB)$rVylE58ZBScB;HGLC'
        b'hxLv#RPQ3QU1|?rW(YSu-&<SLvpm+jiS`BhgVORpJVlMJlBIFzS@fdvZAr_d@D&7j0crdC)xQ(jfFG|N>=Q$O3rw~bWYvV{F{#*l'
        b'w^{Q6A4Bv3ms#~JW(z|i%Qlq-){geNhkM&D_t*oqVbS)2D9RpNq}48oO42SV#4M-y^bJJYRIhuow~jN4MZ#yqfU=h%>0L<MNUwVY'
        b'<m<V<UXMg-I}4or9k%62dKuDQs5}QH_y=idd43mfh)ul80}o=hblR3$-s3H9pU6O;tC_c}%apZkz3%h9Z6|vw%1G>>max<Top8$K'
        b'kRdIX+Fi<XRq&XQ?E4Bdln%9v$9?e-6VRLbRnMN-6tf~a7DRt3u?iAfv@q^Nl3CefWJgKSvU(iy3HU{6z{r2bv+Jp%OD?piqV|*C'
        b'1tP}X3wN16>Rq289`db;d$Ng~Xo3v!?C|O?<|7E>NtwP6%$)3vl1|?js-ui)R&{NU7PAM?9I@8$1c^lkMRQd>tr+`v1^ZlMAG)G#'
        b'`9C!O2CmQLka}e+vHmo0c9-_RrEL`GLhs!eXYcMy!qph>_2)uAuYEHbcWnDx?`6U+smAP5XhhcQ-rWbCC>Lgz*|f?cd#f1u@vsE1'
        b'#to7NnIW(mgCCa=?myc&Q9(drq&C#XVUb#Ycyr0&U*v!q{F=nZ5e22gj|?*Q-bn2nrl7aL0pNh*>0#dLEhzng=5S$Sgvsj_^b5_2'
        b'1rzub+?vd$#p>64Q+M?yVOrp5GP@y@KDt`81w<F{AEY5sfm-0z1MMyx((9Gk0~^G4EpXT&tuk0j%C!O2I4E9`ut27I?Kb48o)fWQ'
        b'dA@Vzf=|R)V9Qy*?0rGDOI(fZlC(>ZsqP|Y8jVuhsWeS+`YXsTEG-gA(*UOh?&^z>%Zm;LHK5fJ@Y=E`2{)i|K^T|PYY^XKkKl(g'
        b'NR&yvtk>aI*fF~n#ubxxQ(16X@<%sRONg?JqIKoC5YCigRu@&~*Y1a;U%KluHK6todlH0y&5o9t3fI{-09)4}(+0RqpgV9)oQv(v'
        b'hkI8J4)dN*%tDf|XE2~)RpIgsLiMdIDM<CEjKngQL@CLkwR%DOJqF}Ri$y85O2D}dVkQE1U3E$d`hsglg&0aghoLn6$e{qpNer3Y'
        b'?Wg9tlh9>#XcTG+>aE7LgzsErdIdpFtThB@1Xkl|8WrG08Yf*_A+v=MwzE^mwP-aMIY_iH1`A|~Vubu~MJ*Uh8AQtvy$fUo6@KPV'
        b'`Scxk;n=9Qj3wTIM`->9C{b06344Pak~-c)XA!gp0eqxsi2H3>dh|@KDI*})qRN?@@rr8J+zdKHb7+=J-%1pgG~j?1dx<I<v7DB;'
        b'Or%5`lCgc~EOb|Cu5ELw>b*IcYp<p+os+vh?l>m4Aj_X!3w}2sWvRs*uBImj7jL|p-Z5K6_+`^GdR6N0dtM@5z+EPLh)o-kt|jf5'
        b'%jDeyP(_oZT)YCIF`X*=PF8D=R;=}rw@BnNG3njfkdigs+N*_Vxv~NE%IWelpk2>zrVbs?H8sfWD)O<bQr%0k&i7=btmcC}7T!KV'
        b'7s#1YJuXv*6wLoL4GOyRwoJ8XTv+a}_G|EO6&IG2b3bgmk#&m!knm<NW-lq@E^h0}nqVYbg6l7ye@|KU_p>rr2z%6e<d~?os%PzD'
        b'v;hmv$-mB%a!>=b7(JZd&6B}prmcJ6LDBj-M{{>R6~6VYtCzd%zXy0k0PM9jTXPzhJw>;@)8qbY5BJxeI>$@S_a*ihedT4T6>Exf'
        b'8sSGLNGUm|LCT)omsyx+Jx!f8fe^XJ9$Zb9a}bbI?dfUoOU>(Pm1{*nF7z%_A8`d27?yvQXI}3Sf6g;+^yGgA<QeFb{4-vk1I(dU'
        b'd%)P|V#%qw5$$3SY@}}?a!tEb+anb!iNESu|6S?!)PfUOvmRMrb`bpPkfTdoz*6PPa+^VgZBKV^wQSg&l|Cu9n<~+4EtVZYq~{=J'
        b'4u$JIE<=4*D+=K3=u5J~EY+5~_s4jZtappcl$2!;F}||Frd6Cx1v=n+D)ab0q3~$*1M|{g(uQf%RE|kkY=aoyH|pY%mk4n$@4_00'
        b'vmpS61XYUOYn3#J!7R9Z172rN-MXgnHG5&|Yq9Cy+)iIQ(cH(I7WX9n0Qzp`u*B~n58McyB~?EOm_TLINOlAUXaz!6F*BEeOi-!{'
        b'X6}mE6?sVFda6}a=x!i@3bVV5LM(eFs@NF-D1F%pEb%F1{eHll#D$1zRPN=@A4ItaKwFiy$tAh9stzLS>Wz3VbJGSFBS?FZ-6tvO'
        b'-BQ33X8Mx>Vi$9^#1@U#bHGAmen(~QYy|mh<1}r-J?`KhZdOm-yKh^HB=e=#O&eOF$AB^%?Cl&5SZqN~TBYn4`?dl(X`wDMcI@&;'
        b'_TUDx++FPtCB@wvZ7<mpyTx8u0vSP)0+aPFrcY%2h7tq@PK8!K;8HPz-Qp=8ii>cg?x}wx<}9VDyPM8Z(BVL37`-Y(J<^@6R%o$E'
        b'6=Xzuv_Gv@s%-wb=_z5>$m3XIETW?prf(-zZ^=`@OE#IUR#GopspHnInXA)}6O^UV#{PU$y?G@GI`b0j%u2DHaHti6*#s=QBnF8q'
        b';<AudNof?Y4z?_K56h+w_~=yIx83gVy1B2q>kiNGye8S2nQ-}4(BRyOP4$ZTB;1i*2OFF(Ztmuhxe&n`n4T+c?%<JK5Xr9D4N@?u'
        b'Z_8S?Y@yfIVfo+lT9~iZ_ld6HBne6}!R9zPv9N~^>_Xyg;g=ACFc`-*QGk05I4N_U<27&c)8A64#w~f%XYAB}>?SSpH7&0^BdQiP'
        b'!%L3U7~|>&#2ktB1Fz0*Asp79!EGN*Sz{Howr*f2oK<&Kd#2(E-_jghUwfBgPQgCF=mM^NUPIarcDoODb7kFi>`vzvi8J!9U0?F&'
        b'ZtI@Lf|IgJn&u=$1U#azrD51p+<m03hYTdK=3CIupfR`<XZ(;#cOc9jNCa>eie$dE0^l>{ciXh+1K-!Mbw9LE>$%I{gY}%lbD~8K'
        b'7Ij|6Esx!;q<u6xZ}XN%?>e$^nnfP$hy8(mFfT#e4jN%1;EOAO#F#(dcmQuW%&x?kKi&`)HUy*~zX9{^8*snuW<GlW-mUNUE=N0$'
        b'-({mI?>Y#kdFSqQduzJA;p1zt67z9a?Jv5y%{R!IRQqUTJ$98tsMC!XSmWSV6te<?GD+RLZ@|!4O3Hj+XOarZd!KTWGMjw_pvLYf'
        b'MLd<PqrSnTkohUz4U(9ryLHzBy^9q^@5aP;!<bVH|JQ9yobZl5)$NCXhZIpi*{#JI5d>Y(tyLJPBps>;MZVKk-m@WiL;w*%lfVg_'
        b'56Odzga|Vaz9vrk{9!Mu^p|l{M7OZ|ks8qrcg-yvAzbn@V8SKBWK8oRvFup_gdK{zksH7OZgdXafqaUY(=7ld<AO^B+kB6n(Kf5w'
        b'J*%5j0eO4HxkO@8bPFrDp1%-GKzDnoHw-S5RuekkF(%9V1R307Qxo07_u3vARO8+GzO_^DdZK0W;q^rCXPbU{4;jls@11K~dJ+Ba'
        b'ee$(8gd=Nf8t?df$9h`kD0au(3HZ&5BZgU}=Z2q=JI;+2>-Vwq@~AL{u;5`k=YB?R)#sJ6ufL5SiN|W@QIwXVs2%y!aSLUAg(}-&'
        b'wNb@(Q1puT0|apWz$cH>xTe$2<I)tj-#RR_%`fFUzjb&@v)?-55Duw8x&o2oI8qyke22q*$eX+Z{$t(gLH-t32>*-Xdt4FcZL@6q'
        b'+kQorcC0KwOGEVVV}1XLZ#r$K(}PhLrj-ef6Djj)5W7@mzw6RNA4_&uxGF8c7M0n9i!y|K7>)RR?ApKGn7gtX1v63F1+^2p3UlEN'
        b'L@3QvKtW#-o0Ha0hE~g&13tM2_Ef$9hH3u|nhqfif`pMFz6%eSkTm`A#@tBny^44&rs#(0ZDCH~-s|vDxY~Y0fV28Qgal~8%vp^O'
        b'W|=?81G(g<4`rHue*<KiUb``!TiB-ADUI2AgA5mtkfhOvrhz0wm;y+3>b4uDA2iY;WPTo)##z6)p`$5!DKZx)G2j$j!Q)MpG4p5k'
        b'VXb2F_hd*^R&r{TI!gIFwA>xV(5V5;PS}V8rOMpy%p1iO3Wo@}g0t*uctG7mmAa{NWxN_TaId;4Dkci`stVZrx}R*G$%5r2t8PG$'
        b'atK2F7f1#K;g;SY3$Nhi0-5Ch{5P4*FK!5ypIZ#ts*Hg}<tA?-Xw|P(T*pe_;k%^}OfSO7Svp;~y=`q^zzak~tp5wrh-anxGq=)M'
        b'LYKBrJ@3Xk%<`g?3~_FdYJT87GkLZ4hDqxkv~60*d6VYGy&)m8zU$oT9SlL?5UJFS%zJluygFz;aZesXZjkVDa|XV3jc@}99;!{k'
        b'GZPeo4)Tt1zztFbM_GB}p|PL)X6C~p^PpTvpj?;_8}A_^ydsf-8y`S~rSe@V35wLaUA{{~m;kbSp>d7kJ~gSgx-z}RxM{RY=+r~q'
        b'F&*ffM#FeIeFo0APkg!S-d*px4&OJ_4s|-5M&AO0@R>P3=2{o&H+^=U`F9spyt=l%Yp@&@J{eV0uBiR7tENivz?o>5wDwXLbs!wx'
        b'!75iiT<~odRSpX>A1Wx5Qu7H%HP4nSw$e)9=LEg>tYlNybb5N7n%Z&nD)VU<_i2|<RsCt#bW<gbT@TStu_M0kF)_!w9IW-f&vtXi'
        b'yQU9!Cyq{k^Qw#czSDcuTMh~-2l`MI$NP}ZCJvE1*e~}rKGfRbF1qP1DCPdpMg4u>bTtPzpV`(qeU4OJ(dAv!etecUeLx@@Q@_+{'
        b'{o|~N;F;?ET}5T;eO<P*cS%2M)IMLoONzR<KXvJ7)Z0Z`!9{kmcHgHvqWs83OvXJNru?qm@av4ZL>kv_&4C@<ObAyQ$o$Nmu)^;M'
        b')9YPp17QpW<%%FzHm;%QrgmWkpNu03GL+hpN3NOcqE_TxU|)2wIn?ucRBqk^!t&!(<F`uc3PsK*LqWdf%G4Dxxmb92UY@!`kTb{y'
        b'<nuz>^CL|E5Bbt``pVP=cI)}?sU{Xobrjb4VTyc&d;-)t)Zh;x{&&ih-lcxMLm(?sG%nm4-TjL9z<Ctmy+pb+#oKK{{d8A6CVW3I'
        b'EgYI}t1vs#HX@)eFUUbRR#L0?kvSLG&9Dc*-bcnQ5Lqrvk!uqFIsHwzXS&E$LsF#GAJ713e98Is6cgV?hJrkhvkFiOGC`gBdl<e0'
        b'9?!%W1GGR)Ojq4eM38HFERbn<L(wY-I^BLSF^attPb%EkD~aeT_L?4P%(op(L>D|ZMt4Qw;Ni153P#;EZF#2s^vAriVWmc_#iIvH'
        b'rE>f39}42pM+WEH#CLsXBk%B$izuq1skqj}p0*aBZnCk+iBg$u15z1S9u^f#21CRAytE)7*v7I20kcclK~j3Kw2O=)gB@Huy!AzH'
        b'PMqS&c(L#7M9gHTpk9p2gCc_HqJ)U>RlW~U;m$F5PcbxBx2Gu?s|<*z3-yT;Jk!%DbW_-J(CLD#Hlp{UgEO||JufAffEV!y9}%du'
        b'v4as|pC|V6q@4_`mNxhEt8hRQ84I#N4AY*z@6IYIx#4**W!k;ppvyv@$KwK&dX|kV#hO<ldUg=J<gY}`EE4n2PB3z~Fmi%0y`-t1'
        b'iaFOw&H$O@D)QIfOy_Ypbj8BZp_(B+=F3j%Pcb@uT}e}??n$*ZwvpV0;6|&imieqx7pnyEjy)!_ek1o$XYEIw!tK2pyFzE6m|B>M'
        b'mkB-HeU6P)7?%jTS895{(<X?5fv5)Fg5ti3VO*UcZ99zkd<Y_DZAZKx$n^yW+@a3hUrysNCQ-~^AdX~+BT4Ewim+aDBNfuzpF2Ss'
        b'el{?{hc}_48cX(L_QU2(#hpxXr!YT&FzNJOe9a!749foy3VX~SJ1?*V;LZ6~YMNu7!&5PP?sLpL0p6V=!xQU#^TV{W(|gWHACBl2'
        b'1+`4n(=NTGh0h7ZJck73niH&z2%Ky3@32*U;)V0FK)(@je$Cehc#iX+#x)+u0Ft9^A@?x3kY4q#;P7GhC!Xfel=?YH3wECtPX!!2'
        b'b%*y#jg|mxw%*qSc0!%fN!b<ZogT`o^9l8;PE&ekGNxYHX<8|a9%i&FOe;E#z7I6REfZlc;~WoI;Q55N6!Z6N;?Fwo*~AiEC*br$'
        b'_Jmx|@Sc130e;r`>$}3RP&%R=3{$MqXKJM}cn8G^^x@|Bd4S%!T<JsaHQS7?Go?ytO;CV=<R0(5=TOL~14Lu8vVHnv%U)TN?fwvW'
        b'4DHFvhcmB(OrMUCagTOV-w@vX9p~Q$kP7R4V7qMh*E+jm@QU)hmkJpd*hzf`;U{EQKloQok+PjvSb11>3s$%&qiS{-uPDy1R2r|q'
        b'+#kHn47MmiJB@ZKhUgU9f!YtR0Tfp$jNUuic+A}n^WTLJO5(uE8><w>6@nSWZ6Ca?XSZ8z3f*Z%jh)he06!&RweB#pR-pD`Zgwn_'
        b'MtZq3&|&pCH8H&%1;Y1Yfxo=Ncwaes;W_}ELOkl-PS@hQ-!#$+;j_4K{8nM<`q>^kpA&-RzkoQ--6aE9bDsK?U|6t}3{ylnmY;!0'
        b'ESPvLte=b7IK-MG+}XyMwhqDl_&i&y{;H!?a2;~7%*-9dIaEoWM}UD@(u4UDp-7T5p#HR@<g*UlMx`Kh#W{+SrjBAT_P!<sFb46I'
        b'eB9x)$QZKWKJ3W{VbygVK7<<qmExz6^LZ#Jb8qxw&Z_KSPG5%viaC?VHy^~zT#t~&9&-SGvhUh12nQnQ9E5obN-dKDpWL$^rlR8='
        b'_yGtl^deNWO#PP*uSXJTf)XTV4qvyfQTo)FIOaDUfHA^n27z(4z0U*cGkuO~PS8wYB+{z+6rW%G$Y6vX%Xji5k$4!`mGEW<9}$F!'
        b'|ITMU-(hnI110uZIWYjs2~v3bCUnf5-XT8A4?d8Q+R=Q*JH7^~<QkUW#wUK~o4<eLUy#8QeVTvsx}~<4WTZs*q$7u3&D^=}&h4;<'
        b'*{rK=);Ap~zcTHy4QkPpG^*{z>((bs)uINBF+pCiZ#9y03Z6vYk<>Ib7PmB}&leRu^^2;v$T@2b=sV;oIyx%yAVFfA42JXXq4M>a'
        b'3rwWy$df23mebJ@M$V+zfU@sVRZd-&i40x42&-d}Ep+thR^kfIXg$6UnUa`bss-P*!E`<rZ6!$m^A1#ZnqnUF0zD)5`QJ}>sH?6E'
        b'IwxjP2T*BhLx-Swgz*vVub_Jl1#qz)wF^61F)+r=jA={)j<+%G)%ODYwJwL&??~zFQY{vFL)jMH;g0U8b1dPaI^c<m7;*jC6MCZT'
        b';z7N<EuzC62Fen|6a3lw&jaLbbcg#fkg>FR7`PV1S#9L6RaALnQP9DK;pL*Fu9L3f{f*^a5Fb?`Wc$PHN>_10V{%vGEk0S4(PdoI'
        b'xZJ$1E7>*eSL>`nhoo)(9d3Wn^kz;1>2PYrWlaZ<k!^k*ZVAZV0v9n|7vfII+e9619OS$Ryc7MI2|HdNP;i=TLp$7eJavxW!ta#W'
        b'1Ic+Oq-5J2k9z{-ZB6Xv5lODRZPMc&0qJdt9sKT(8tn>lE>Kuqb%lYuTMdr_DvC1fbrX*9GL?aj-0%x~U777*@RHs2K;Gl&{Fw-H'
        b'0-x0wOT|B0UT3J&EovOgL(A*B>JkTe!;Gh6&&MkE#x640vG}?@g>m(l+y3Qo{{XP%H=pCn90!As3*+-P*79}RC6D_OC<*0SJ(>_P'
        b'92Bz5r7b&Hs-(e~T$Q(d=5b#D0CSti_+l!ksIKiRkNck>;}Lk{+;#RyJW+q~M7+H1V~_hR$bPiBm%liNq|eiev%werzW>O-rK#;x'
        b'kJ}B(9s_3nkXb9MbiE^s{D^G(#N$2<vLnUqJaX36<+pb}`3SuG;(z}9j`SI5<kRS(hPD$PcO3wl-~1haq7E&pZae02zYj8=$iKkf'
        b'5MAt&U-_Zy;+*prh#&AWzujk^F4vVS_Lf&1Dn8wKd@oV%0s>I!YQE!>?K)aY*{GWKpeEYC=*KqB<92xJxb@uI9*s<VvFY>Es_&l;'
        b'teI*Y`_r7ZcRcP2Q24yCFWgq{aUTS!=MqQw-RGVLVUuES<&jS$BpnrcL;i!k%uZrabK?E>Mpc!ANqW2}upHzW>f_3#Wm<BHuAG8j'
        b'5dXpMyJM&`1|1^WUiP@(0&Tv*z2t%Nj``&5w;uN!AlrIh&R+Dme-CmPubd^}_JC#eWZNc>`xTJ;mQT*+e-7kqgU7uU<mE#-Bln(='
        b'%G+M@xPJ|D3IOwgiMB(lRv2jbKa9N%T$APgKYrc!Hkfd$<H3nQxeX@ssbFXuMlvQMK6FA-M6+`M9g@}em~qtl(s3I;45cE}1f$wW'
        b'5=~BmmRMR0k<hTjtdz%z%&fFX5lzwi|Gw@`J?H!TeqXOY`rhZdujhx)bzPt9x#wm{SZrJmSDpWje)Nwb-;@%oO1g2YAk%*(8nF+&'
        b'HM*=sU*hGhlA9%{BDUdr_HmobCfjV=w63sZO5Dc%9j)nZ=RElTe$z>B9+z5+>x1Q&N$V`PGZiM|9gn$9{gRsvH{!&$(;LAn$!_N?'
        b'7))roN%JxmGHO-r<_lcdt}_2pRdI=UUtu&I4eUC^74N8j-T$XUeXny(xA@|-^yA2dv#L|4#6@>Bti7yWdsJ3jQm;Go4Z7669rZsQ'
        b'I`;Zd@4i~adUM)RE^Vp*!kr7ZE?mb+#)=EiEbLtvxnN6D%y_p#nHV=IW}N$RRa{ccSa;k!`m;3uDEfO<!_Be5$}w(k=-9l9#(0&z'
        b'mmbbF{Y1tkDaX3UqOlztjEu?&Qp82Zgt%1=eefyFJvJCVjdUwRsb_L{=JPwxMZn5PYBUL2$`CiKjG*QtsQFKHJ)z2)rs5V%5oerU'
        b'FlAUP-|Gx;JAUr1b^PLXN$m6MXM7TtdQ1_$Utzh{Lyv^3hAoO+WJ^t|&uA#@S!k`Y(%s9J%hXKYlVP2OQk^wje|n}>w^gKXh_j|x'
        b'^|iXKQoRb}QIx7`W{I~A&Q?j&R6{e(!SYL_wY%5Zk1#)ReBE1lPO_$9^<%*cJ`Kp6Uq7&ZWNUk`^9l?Pq9(Nd*z5cS>QBLnk8jQY'
        b'YQ-zE&D*zsGBNGg&CMSc$`|_Vw#rBNoRlC+U(qPpdKSfo(b%T0t}pE2rZ1FdG|)(Ml9_%BLpSfCk>72#9QH&%#Y&k{fBMzDSF9^u'
        b't{>R=f2M#_Z@BE`H_vuvbpww)Iw`j7?(tkM%~l?#`%N5V;oRr4Ua^?=Flox*Y<uydJqr`l?7bCPzM0wP)HHLgQk?mrLLJVG3H4oR'
        b'Cll%NQ|-q*-6XE0w@#>a<TbxBp={G=QmW!66t~E1X=mpiVTvX+Tj+jOnn=}dk#BAy$9)wXZ_D~BL`M(#MZ;PaJ<UiLU&MNm4uxCZ'
        b'>wLGj_JfBUFZHUAO7u+8(bgTk&QfSSoP3KvE>@|AAzafVqKkoSQwQ%k6khF9`6Uq+VM~<3V}=ZIzsuNOvRBpbhLGSMFM_5mabq04'
        b'{4x1k%1^e2jr)hSuJ3iO@2#zP*OA_9IxIoGi}i1{_Bzebdk>9}zQU%8tBuO_$=?rQxlrZhiBc<Ed#dTM*2TTfRlSa6l=ci$ousOk'
        b'3qb|ds1zy;-GobAJQY+&&)`m!qJj!F64h~ou;<#Qin^qPhqcAF`cn2{2(!aBQM&PvtTnsWnceG%hQE>STFL#juxHs0w)NRw=d;L;'
        b'<&Lqv^oZ&{$)~Yg>!My~1~i{<LW4La!uRns)yIR1`LbI3<qA8aZjwy&<K&#UTB1lUFddN?40*5lwM?=n7Zf#Cv!*X3)xPR4gkVlL'
        b'#M28gxT)1XrnkvydvV+8``_D0r|(JDvu#~{n5Ub6Fs_daXgS^bc(3#E-rAiahq%|hOTzhZL59b+<Oa}fm;>lSC-*vIVJsH*xRcz#'
        b'8K1H~qe-r6WR94Vr%&^BTN!Ob{GvT^jMm<}Tltz~infY5;;X(+azf|l->w#!ZnL>sdPKwJLtgaD2_07#kYPM27Or6vHl9D}S1nQx'
        b'6<zM-hE~{%DNpRFFug~7d<YpM@uMP2K9j4oud1&WRr-lmfAT)(Gf~(b2*ImDNk`IXz1|@k&`&&OftPnAbpO4i*XfIRcR9YfVA>(k'
        b's79i<7xy|@=yiibTBdtSrpHc<S>&`+=K4la>kM|Ez+k1fC_<AsR-~DG@9Zn}?~e=4>lbP({T-iOFm02x9BsXJ!TAR?IN>!MqrKN)'
        b'G$Xm<%FC=Ro65v=u0veOv);Q88sgP&-CK(+RlUxRd~QfxMOCfJPIkQ$RCS4CKMduns%)hyJF{^ITdWe_x64VRepXglOKa_g_1mX#'
        b'w$pZ7eN_YHMcd2P=9_QZh$c{BTSEI3PP*ZqEZ}iBs>)i|P+EI%NAUI?0XCLe*RU!T<F&v2GYLH1@F#COy|1hu{_e0@oBNUncup#m'
        b'_kDkcQW*`LelbL(VaM4fdhV2S?7tu!y?(yOd(8X51)+6v{Of`xhw53XFSzyvnBN$ourd2;6V0D19J?>netpOCH)^V$a;NB)<HHMA'
        b'd^>5IDz+@_`M2}F6&LRKT#<B&X$a~+dDA~6-ZSu(w{PEH*HU`dG?m*gC?f1!P@HFO-Ln{oA<OiU-b)OW#TOKj_LzA+(Ua^Nw!B9p'
        b'3R8_0<pj!=^Lk*QVT)=<u>rOVst<`G(mF0+C`Z={y>2an+v(ITq5H%3!nr@3U(Qx0d0dyXA*^y0wWepwMOr)2X4B2p+x+P7dP1g;'
        b'B2s2(-}nE;DD^$}53uUl5K$bfVLAdeF^ZqA>6Ov|nSw-L3=-B_AL;Sz2and;^&(A>HjqTSf{q0fSfPGV8Q`L5NWfU-ibpPtjmcVc'
        b'A(Qs)B89NFe5}hyql8kigiH@5%CMe)J2lIR;+RpaCXf@sL%E7*)5!Dz9(frP@Sj0OyF@S(tUcsCcKgTF3w_t@H;0%1{ST%`P_=yf'
        b'hsdKUdg|urp?%!&p?#k7y9+J!OlDzCnR9pRq4Pai0avpEqeUWZR!}s-uRNN;@5pGDzAr+G6%ARVPG^OdWQ8^Vaat)WQF1Ehies02'
        b'kVvkNXk`Pj3>V8NFOXOTa){J;j~dsv$fC`L|Mk~kHh7kcJy}9(f*O>gPAfx8lwm`M(BdVX1YxZ2_8B@<rIc%xBNZe_r3{H?f)s3!'
        b'RvDz38!ZabXQjN9VW9^~Z8fFNs@A&mLi~D^0aulQ@CEs%Y&@@RP#EoGCOccD)84$to2kEwQlAxvi=yXSV?IBh8f!Klm8IE9<`S|-'
        b'w7P^@D4HERBlcRRr@R#|QTgdBWc|<l&|&3Iss6^cetiDsqrTaqOG9r>)qy;5YbuTO6*B!NYUO?HXjTy$9XGnQ@_)7W;C_Mcdz?S?'
        b'aKk!9wL960hB(VPTFr`1oNw)EJ>64tx@U2?yO~d4DMee&h;5>`zM;={q-1om#hwX;3_4Sg%LSig>ESqfRa0(=I!fG0PnOY>Nn^xN'
        b'uuzN^JL`J{)ljdNI#i4rEVy$=h&u#B^=QFar9$ldw5N5MOE3%&PZV#s!si6u5DpTG+~Hz+7iuD@R5A4C_*sPWQ%eUuV{~J~9PfFj'
        b'Z7hE2puC3*c2}_+8y#8TJ#QmS$)u@<q0>t*XY}loT+7Q<Ds?aOq+gsWj2=Q**hBZEb)2aRw9Io+K_^hFl1;JcRfT~%eTSZn3ls*<'
        b'Ra(m&mmr(UO0{Nl=B6?|Tc*_=l9Z}86&7l9B8PC|86)=k&u{vf=frf|742J%s=%>K%bC`-J<hc~HRc|NxyKzN$!?sJf13(qn}i#I'
        b'B8O%4FVJ$Wul6`s_0+u5(}eJZn?;9l?1H)p!i7K6(Eu_utylTf)I732VxnJ;l)hPzv9)MhMPsBpjp2grkz1;L+@-Yj3!4vX!fBQ1'
        b'$=>yR<VCfpe6dYisybmS)Na>{Y;2*nPHU07?w{d7p3?4%9sx1axM|tx*$t790?5-57e`Fd3MWgn#_9C9UkOXCx?l6yOG;~yQF{du'
        b'7ek)7XD<o%+;6gU(?*&qP(GchwbS1IH@+xTy^QgXg@dL`!Yh9z@)5Tn1ST^ZZt}t#VPd)MHkA{nGex1MrCz(jSc3M$F+I+h9>>I<'
        b'TE}R2xFjdYFLCg^F*}G88?%Ewd{Hen<*~IWtgBUQ@n-Apz)d^$+3GiKDpPqb0qZH$=HH|t8Iy$H>D#xAp)6$F9wehLhdsd*y=wne'
        b'WUm&hf4oDJTfm}I7S4N7<9Vn<k*0Ypef$pPOye}H$2klU%5wPjR0c^}zHjAvoPN+Sd0xunLb)M^9R<b3c}M(O{*2zSrDb=kxW~!D'
        b'#&gM6(bpO_Z!w$mT5d*fE@-K0<<C2BpRaW+-|#EHm_Bh+NS7N+nT?~k)<4fX`(c#V)a&6BC9&F>=;;M2({Stb<e3t!Nydd$OH5aI'
        b'j#Zfgg<}Q6JS=2S_j%_paO-e%ou|X`A(H3{>)wdyaSby9{i)#v7}j76r26=yUA6wL=g&L4pmQMk8eef@o_mCZ*1}MFfsJ)m^6P%`'
        b'2x2`kPn#_(WM^Kbm+7F-bGvzMcA&TazF$X8&#+b%IuTtdqgT=I|6-#f6yCGa7BVyOHJ0Y#=jWZr&ewi0$?@rV6EAMLrc%j@Dq0)P'
        b'JL{o486rxKTBf-%266r3yz_JDJ+`5ruUyKck7HCyvAltxi*bGe{W!WyTjMKF^C^LBckC|8&M<b1!jPB!)tre#=tX)ZSrT;`<=wiU'
        b's&16d-Ss#tPx7HhS*z(pvgRiU$l9nt`B9NPkaQ#+fi@M^8+iF9;^B+RPwt=&yR%sOnuR7xZv3<Iab{QG8?9yMom&wF1D!3PUTv3`'
        b'3|4#<=?-Chg#A(#N^$yUgx3GRqOGEOEpgRMrG}~YQ9ny7l}}{~>uDfTXaq}qlSo-a&JemQOEn`&(3$>kI@94`AzSN|RWs@_O!{)#'
        b'I9L5tdSiR&uxj7R1|G%>SZ-94ldnsx_)2E-VK7>7LR+2AdXnO<y5n<$ul99+$zu>EoKr+klo$P-;s}S~hr5-Z=vThn5^<jMKQ!);'
        b'-=Qhi<w3Q}gN5U#z4y*~(eiudyz`m!jv41`E4G;~h*MOR<LD{2U0Z|dv|Nz?=ZCZ{o2etuQR#`EIaEb`9-0NZKk$2cq!Qr_`Cr1R'
        b'?Bu;?G+tyeUWqyHG@h^BIodJdyt_l(5kVQ{bgS;X^9krGJm>2vuMALLi9PSsL0gFd4<w<LO|*^k9m}Y-!rP)3H3Ly`9LJU%yUT?Z'
        b'S8Rz2rFV*|e5TV8ezlK6k!N~`C)S7@>3r3gz`a(mf{&?!FA}%R;sQ4?gwR{DmXZ~_6zW8_im^O&{@%ek+Ww9iBLByoil#_Knj#xK'
        b'n7#$=vic^Gs|W34wkYg*O;`9ZmFFE5Rr2&E?>+TGUA^gY`Xky-$2AvikiQXoYJ=~2rv%#cu%AZU!D=Fl8d^o?odkL(g!?lgS)|b('
        b'rdpzo6jIo`rk`V1A6hINP@EoChGvE~fxTo+M2>Iz%E-W|kwNHg#qO<qR1h1rV<OV!?}@)Ea)|uuU34%jq9EEZ(UDu|Q+bz(yyA|1'
        b'MuEYeCl9?t)4znCI9JE8)jpO^Pj^C}gAp!OM-TKXFVu0ATbs+-=BlmCaeU!2IZ<v#B<W1+4=(5T&|U5+x5_Ano|X4wj7o7)V{4<!'
        b'c@l<yr;Vf!8kFP+l7<@eiEsdX9BNSVqlC0PR?V3DG1hWxSZ|9Hj5<X7pCIAXCYwa&N90I+g~Om}LZhF?PX7-*+N-%EX+@Gb6sA8&'
        b'`X*m=R<H1KKOa<_hRDj(blmYeJ&vyORvgnm?r?H%cteGaK|ONG03G<H9pfu)!a2+yp<5}shHj(sEV<XKRK7%e74^g3UWHD=*r+$|'
        b'aF#w+K)*NA?UP|_HLHG!moNXbsnN4PKQ8e}p{?BLau&L3KOEwC-c`9*?5O}|mvbHThI*bmQ3o;hMT+z(j8-Y0=vVYz>q{=@YcLL^'
        b'Ct99mwT*Lp#uHm&M+&%Vjmx<TMj7aDAe9BPK9fnyWHcz<^xcji)_cJ#&*a~x8<6iZf>iP!d76~ukyQReZ#smy;hwh1)Irjx3_+eP'
        b'<>e=QGsGQgIx*n>lc|a{#WNHAsQ*J*<aA@C`Y=jTy_%j)@%QF*<zMfl*%{%=*UAB5>rJm*)9-K7(8bfj-gF~TFJ^W}3M?y@vrI*!'
        b'tkQWux7~~GK;-llnreDG0CN5%AwfRuhM#G+t5*o064V0IB3?f3Pr31q5WU}NSan;AHftKg-%+XP{@<!djy27qM|fBktbMQT3wJrA'
        b'Tn?$Lw&G;v7PNitHZ**kP0NLbLEI9Sg}i%@FYxkT?pjqMs_*kBy({cp5$eWZw==|5yQ|D`qr37=)D6g?D6?RfGYGmnJauEm5|S;*'
        b'Xg+0(`l65zJ)EeN(S?jZGNjte>4l6si?=aoY5aw|(|aH<=18BQ>}k|(8>zK3=vzz!44N#<)o!|GCCrI~L6ODimJRAH?rI`WyJMfc'
        b'MSg8CZ7Dqhbzh=1CN=%$xoa71)VJNvE8R6$x*aFFsXVbxY-N*MLQLDd=eg5_{-4Tm?ZTy>sD(B}Me02w?vcGv4XLKD=P6I)bo##K'
        b'WyT}7x2&hLr?m3Dj{x2Cy=UuR7wMfR#Z}+c+A9m0nE@8A3#m98kn)}XyE~Hdk7LMUV~k6J<eDMekZ`|Mn}+VFtMw;4j@Hi67x{;k'
        b'aZ>BF8R0hbh9$Y@3y)?m3FLgNOM<hPjM)4^Aw8Q}$5b2*SJyE%CcMmCSbsL4`MbK-!k1@%5chQ42kJkV3P&n8=ZH`C5_$HLk$XO{'
        b'T<)YJ1IN5g1=%U2;%KIc8MJ=KWT&JHQyR2o{esyoS~il2qcgA8X?nUGB&;*qyYD}sCAGZQ-LgZthS75u32nNEl*ZxT*n4|&DW7fY'
        b'c5dsgdAr;3cDMRPu~juvZX>lSIelZr^M0)G7Hy`bq+59GR%~)J*3*ntIzPRcRGqH;Z!sFR|EA?LCZvCiW}tO_w{v}W&4zA=wOgGl'
        b'zPE4KdlBY{7g>X;z?BmaQ$S<7Ms(QM@me>^)bs`OR(`i2{8tSrpHd_4ay152#kIcDed6oopZ~Z+u2`vXtn7Aw%M2d0tfEm7-e4hX'
        b'go|Cd?IY=Cf>QtOBS)1)1-{M}_tv}C7nogn9pC)1tov43vAdw-k*ZLiEA+->Qy=}s(5I=Bckg5z*)%F8<LFDpRIyyhDUrYM=Budb'
        b'{Js5T-JOXGyXgsdjc{eK@Q%3UsqWI}HjauCmiuYkS?gJb-teDZaYCwopUDx?0b?EOnA5%a^U6}@{+q=ldXib2%g)#z9FyEFY^o6K'
        b'36?NmOMHZCRzy<EwJK8kwN$;GQI72vc9724e^A)@+4QS$5Anwx)$GQ=5X-^Nd)wk|Qd_gGF4ldFN%p^Y{dG~D<>StKX8KT%=9rLS'
        b'mffAg6R5Tjs{b`T#qQVCckezSdAD!@9x^GUJ8N494c;#-N!ZDh_)h1tE#rmFh{C<JYl3z1a4x8PwXG?)Va->|>Y%+^@5co#(@8wj'
        b'Jgy}H%eM;rnI1A!*xV>QuA4Jz{#!oX;oFOME9gl(^*Yp((tt2q$?@RTr9V4Jx7*6#w-Ud6ms<FBTNp=QmkGZEU1|$s>FIiFpv&`0'
        b'{MD|vu6KDZGKHRP2pYv9(6KcLoVD>Yp?x3XstVY&$8xF5wI^Ut)#h6DS_ab19_FQ=sna#SdvD~^(c<zX_f|$IY<V8ZZ8WO58J`At'
        b'uVC2ngm*Z1YY-XqAxhTL)+OX`dd5v5kws?(Qrci^-gt;@YUh`)6ZX3b>k_1{0S$gHPw(?~(DPv`Wiaie4>B!nttYyiUw743>~z$0'
        b'xnso;x(`#`uezMapj+u_xvk0(pK5~M+Sj$CwCGT)v&;Df%s!+m%q0#ww^By;d{iZF5A|>TyvunIhW|q6LNi7w#u%o0$o9aP?IRy~'
        b'<uocYH?AUOK0K_l91#^N%L2wSSDnG0`@Gfv;%k*7ATxCHnz;}4?VjtM3$~C~=DsFQT-jOedqg}o(Uf!hb-(<p@>`-K;tEGbVV22s'
        b'`$<1r)?vTGHdPyg2GTfRrIhVv#wu^l<=Cpku>sWo6<^U+I`=MwAw#QnmKR>~lbRkAC*PsGZC~Q$URP;=WmA{;%!lVSW~pUC*ZsY>'
        b'FLwz$Demp}f;;7Zd9*A~c0HK?{Zuuq^_4E?D_u3Ob~zSxsUH?w)^rI~T0=(xtGb*och#)wN~YH}+`nsbC6oS(_`&_kxm{CKg3sx!'
        b'-0_#L{M(f)8RgSm!nW)%;h_>XeZNHcM3+!kJ>1jJv}ScVv%6}tyBzUdm2$D^*e#Eba^o#7&__uUle&Z+idOiQLbYF+O+43bqzefV'
        b'hpB|!ag`2!Zd6y|VOke8lBoTE;aG3&iVc{OB<xL0IqI4eFe^4OrVDy#XN3JFpGHv8(4p#b|2N}xFfAY^vC9xk&9xCE{plOU!tGC4'
        b'!v#L}5tzBfmVZsS9iz$3XGuK<Hhr$Xbj<esbYNR1+0f0eY?9L9N-9(OY0=Dzrtr$A&|Y+vHqo2U{I(yKcv@B0?ttPwW{W?qbSn-j'
        b'>{aH<8I0!%0#{kUj;%rkEp4)$KyC5q0xL9i@G&7m;zgdsiy)kz67DeX>!cUvKEpgH7Pc!|xGyAyRdQYBTOZ_!O1PIKj&)q<RKGwQ'
        b';QK}%2gdAsQ<{7yWrYZ@eXnL#hoDKD1+Uh<?_5^noBKo5W9t9ZuKFL=>e$+^_3js$|J2p6HNBlxr^Dx1F4E3^@2vkHo>V@^Wd173'
        b'd{Jz1b_z!r)<`XNovx^WS5>g*`XOMGiW~8|U)!{|qsW5N;G7UPc|2+Ty3_e}XH83|<GoJx?;_X6fSQjwU$xQqFE&$;rJQtQSk}fJ'
        b'zLveTdw4}!rKQtb8+S-5G)zS{Qx*8f_RdRFTwf@P-WK|)gQ1U)k<+5D3fdJGT`@jzmt4}f$DBTk@_Ox3+E*0@R{I}f)Q>WC41|NR'
        b'Xj{1u|JAC7%S~tbs=%sH>b<xsMDV?C%E9+`!h%#-7xQL%xlj_*I96c!4aN87>B>8u<()O}b~>K#H1&uQ|Ep729Gk*CXe0*Ot68C$'
        b'sFT)y9qx``JgxK*k-GrHAN3s1okMdoJH6}Gk1^EW4V_L~XH8+JV}7T*L-fG6o(I0=Uxj~_;fz7M<(`+7|KzJB?qtRzn<mcg^v)m0'
        b'&^|+}BJ!6xjaIL1`L6ZlPUp*=HF=$mCpz6fh|-RRS4&I}F%=Pkmijj3yv~iGY|~ipG>{-k6bWy>s1Uayo1aGa63Qr(I;)NfX1nTW'
        b'eX7VNu5kf-R1O`@sw0v;74AUlp(g{mQFc{5Cs8acNLA#ulvu`eZrWrXTOhwGd2kc$N9`F$H+fnzO+(b=>E3D)5fBsKIWCq96e=7V'
        b'Wj*7=(h-hH&v>TT=$$Vfcga8UG!hl4&_^W7kWR=`p4ADCT@ZS-?x=bd?~&~-YLDnq$XcXcRp7n0`dQlYKGNxYq_gIcPRI2QccZA~'
        b'gVu?i&T*YJ6FQr2@rl<vJQ=GFXOw@^cCSL^?G}`;wo^v73SJ6tjir~@{ae-dTtO~Uoo2MgbS^M?805N%(lJA{7N)aqgz(skO;T^G'
        b'=fcesw#d^+{RG9q&qnMUSHHbhZZE6fS7t6*LQux^njLTty|Iek@pFG4#RE?Hy<>-s8+BjS{-1qUYP-NjDh;vh?)bO&;J@hbKE^VP'
        b'Y0*~F+wp`)6FHNTxpx<M_&VKzVXeP*IDhSMRCm;V_*-SIXzo7h4kC*`oT>kWGovba#uj!%40&sEyKWNe6XRWGbR`AMn&}bJ#8L7Y'
        b'6{<jQ6XNLL!oU=>3k-(5mZkQb`pnq{<x3wpqJ3=25C}bXX4(GX9!H#bSt#ZE3_iEPstR6K%EUF;R%)|@-_9lBrP2EOxRtKQ0+z>S'
        b'm2@EcZQ09Xb*1ArYca(BjaasJXc~m>JL-^Fkb_(m0g63l@D4-(`-f)tMN*XK9bPYmOl1l{ZvQ`t2#$K2ZR+O#m&8H;9RL5up9@|V'
        b'%O-!vBjrsedC&b)suP(lQ<S6IHTU*WTntiWJ=5WNE69DFv}oNIkf#C*8MEbS*(0lcOj2(>uVy*+V$krY9c<-!UVAi{+M1$?@Sgo`'
        b'G176Xi&u>ce830Fr#n2?;|G>EKd6A|9o$%NMWT1t33udMR2}zZ8i$TX$bFft_*Jw5qSlvfE}geG&k&^>iTfNa_68|!an2HbExlK;'
        b'A>92VvBY)grD3sgQZ9&-t|%yYP3p=GSP&R&`M52!lsYdNOQJ?eN>qWX%d#C0cN`I`za?*trcu-n@klU3Vs^GIpC-sIoG5B5L{K%u'
        b'ID$IVH%U$qoo-c!)64Ho5A!kM9Uk#vL5WU2P2}$5FE46M>~I=89BfBz<qr2o(Mx{RiZO~98>#$hTt-YI=u5s{`8nCU{w8Nd>MK0G'
        b'#8BJejO}n-ZLj_CA$Nf&=6bs@O=IftwvdWig*uAf8T7kX!<{&I?+*T-`J8dXS|dB0>W&(9hvR&^d#xzO-R_-kI_vFU5^uB%H<<}L'
        b'#{Gp=yMOC%lLT?As6u6@+Yj8A=pZ=pT)Rh-TX#3Ht36rmU4?b20~V<SuQXbXmS+E#WOKH#`)Kaj_A1KnHp#9!%I~`+u0;WR<~zP_'
        b'cg+tt;<IRv`yfFPc$x@qL@^p6AG4_-)1230%lfQ+d0FxLg1u+G!I%Q(CbTW55zUa~He?)I@L2EzlT+=>=X3NOvgagT&Gi9`gbtpL'
        b'H!`H@Bd!+(s_)*Nd#qiM8M7MOF9$xTD9J){<yZSWnF%4$Jz=n^o+rvT+AZ(43&ULDIK+%YLt9(ho!_+AoNC`t<=MO~2)G)lBC?)-'
        b'NTLo1O9*NR+Iqo_f0B@$Go_~4{C@_SE4F*~f{O*09v{X^HvB*Zziao-sH|!iCS5s+=`c8q-V0XM;1L;PZl9x4;}+`GkldzaQ&=B0'
        b'$yoXJdd8ax^8*$=?a8oX;oCCj*DqY@qAzcm=RQySjBJ%ps?EId?U_Px?Y!4iBhz99aan&fu0gr1U8uG?p#bAp*9QU7LW7n0slr}q'
        b'u6&1ZBfx!4L|76d55j%m1r=)k(`%b3TNSKn=7ORgW1f&aD{A`fURob-_sS2|B)yh^`{?v-J>@=ck5&*6^Tj#A6V$h;pkb|lZ+EU}'
        b'uUXOVh-x>@6<H%jwA8h}*zSD3z2?PsI>lpc=1U?tRYb6L$%v>?d(%sAsgBYIG`5k7h~V&2yRE+P<=sbP9ubl$^75(3H6;L5%>IE{'
        b'sc3i67lqC0*9jN6q1`iQlo;TRr}_gTzbZ{rjcED4HMQM2x4mX=yF=3MP7$GRC~YvuzML~+g>KY~-t<=mSl&3d$0o33)HeUt8ST!b'
        b'_L>>($yfP|m2nMko9=fZg#kNkF$^uGjO;14joZd=PD6LFiC9GK_qz~*&vMEAJ|y)M8skbU-5yna|9pDP#WrvMT1vc+oxLcqO{s89'
        b'qCES-@S{{1ew2(G5mr{Re8dBNo3J@SBQ;fd*R<u37em{fq3tzc?T+JZ?l@6aOB<a*RhM{+dhWb)w6xa??gT+@-XQyc3q1N<2&58W'
        b'f^uH@Bu~{d98j3f-Sy5-_fsDoL|DEnBLCC1$Jg=_`BBk-8tJ9pmv!eo5QBt=4<(#f`yCC?IBg!Cu6;+yr2pyI-`MoKmmjHIe4)*G'
        b'p{=I3&GBZNX}qXte``;hv%9V4d>dVZj(O9Yxybdj(@cq7xUo_)kM=Org<sV?vpG)~t(Roa8xz7dp@!BLRkogPbAHoSbGj}0Xa0eR'
        b'RMNJ?!yM`BeT4#lo>(@vRe1`0mmo9jmU^nN<JC4q8AWd1V>T^;I2h<H+!xxYP{T>g&lIGZ^U`gEZfM(FAiwl)GX0ga84dSm$rjW_'
        b'7DaM_W9g2QO~?^X<|C9nv;nPc2zO++(YtxQlRlw8)-|}B@7`~pjP?-SfuXGhZBBce!``;|b9abn?#wpN*h2jhsr(yXdcry`xQs0f'
        b'e9})>H&?qnSa)c)=GC|pZ)bb?{Z$XYPp3)JECs)pjNcrIVbe3jGNUb}QAqv_f!~eb_niR-f!{qfwDM_4r<MP_&+m!j+Jq6&bHu%X'
        b'UpX!~Bk&2o)gy9pPoymmUbg+OE60tHk3^TJd3oW{w^x$zl2lc_YKgCFL%?#IQcWYUX303)#_eM_zg+EWdYV|G+Vn?-2<U|TkCUPa'
        b'oU+F|ey=cB&L+z~k$M^SI09C$BEp>x9Gj?WdxC9n%4(g#70!^jENzy=T}*6Q+_0N-n-go&+Z^d_V*?5qSC_*5?cLqt*-1HpWB1Nd'
        b'4<$LFV+>13;&11K{S<}bL~)zvMDVS1LMvQ32Vro5K9~3$zw52ZZO-Jjn&dXe#dB&#B%G~HY7;ISUPxk$ZN><4d1qE)8+`+EDw%6&'
        b'gUmdYSQ6S=4Q<a!orbooC)%!v!~MBE3w=zN?(7y-v+n0S@)vSgo6V@67waa4=(AIk>bXGO0e@vo+w9Njo*;OGTwicN%mpsk-#`0v'
        b'<+!$F;jWw332n{^ZH@_TwT_q6H(6n>ta5-?j&9SihvD#kri{%}AyW#FDMFSg+Z;+{Nhe##^w^ooFYdy{ZnmYZ_2D+>!)=Zb_%~X8'
        b'&Aa4;a3*YWGosg6`m#DFwa$uc2~ywW-M{k{4dRvABrbd5%IB=^Xi~J(%0_DK;%J+~YK**hFQHXItM`yLr(c_ch0j|}SJ;<soa5Lk'
        b'->6V!95XYZP<e4lsCpjX$!0bw#*AZ5vK3ME`e^kpcZ8d6I@yyFe7gPb(u;~{Tl>p7jpv4gmaU1G&Si+liWiC=>QkviMitR$XQN81'
        b'A0alYu!$9Mipu@gmc41+#sfpEM1_H4jYlMI4cYJ;-(x3Wij(3a!>F8jolk%DR_pn5&hzISXV2AsaMInwdgi7Rzd5H7bH0KMw|ay~'
        b'qg}%)kDa4MUl~V`eK9|rd(qDtK{igIPY=1TQ-L*m331ORoR9MGxsyIs>=DKkc31xDZ4FbUeEVvEM!6;}eRZJwv%5CYYknI)V=J%n'
        b'Hs%#kP6q4q4EZpZ-H=3b^lb7|<iixUX*zj3_cqc|VrPnlyscIF*aA-ac1l010~fXP@>l;{V@04YU$PR({fXUho?nyQOea2lUTrzz'
        b'10MZ}Pak)qb<a6xHIlYyLoj+@&W{U!-7mFh%j!>=lYaHhGWlW&Y#Jb=Q5kb~g?p4I_a@Y3clw_6`RrgdtNxzfJBu6EIqanGkzok?'
        b'Jm0aXb?Z6j+vjR4#yB>etNfPDznE#0A(FXPVb65(7d&bC-ty0LHt*wiA;rxFb61_qJXl|$CZ?HpY2L@(ldm`57ETRo0_tL1EYUD;'
        b'pZ?Y706)7z9YC7)^J8oiFWT4*hk34SdkC9c#Upy$sJZ}8t{lql__cM_IcFYH__9w2Z8(t|`IpSAWh;%5P36KW<d2FKUny36Zbm|z'
        b'`KIkWwKDRjb12I1S)Z*B)~cR8=UjTuk$$dr=Od;DHfH8IZwC}gszsWWU@vdo*laBf%>T1cTWI8@Wh(D|Ky)2ST4=m~cTHfarZA{1'
        b'qEr(%Do!(Y+P_cW-m_CG+HB1k@{r9~8d4S%H?}Y$F64h&eBG}qq|Wc)p@C%YzV52PQkBhEHg5N*s*tE1Oj!swq|7LE+Wx8s_g{Eq'
        b'3B?j(%DPjz{0{A&6oeQDXNie|k;Gs7jpzG-`q6}J8ZC)Wi6F-Q0AkRb(HV$=WX6AVJfSZ8c!C~wWxI|i*r6`{MQ7;!NoUB{9#6;v'
        b'E&<}b#}gtK>I`;(&L@O`+JKgkdc&lc;|YYw$l!Ql<oRwMe|MI^zZCez|IYIy`gp=+tIlxqQTTsFXUMz^Kl+%=@1D$-@r38|VQ(kU'
        b'h&Zk3(iyhGZQeYcfxa`r^9gjr2j4hfXBb304#3`-O2i3iIG{udWQ4S2=nV0QOMWKsw9cTIN8@NV5HpPmG1GtiTB_#PR>8d@7V(YD'
        b'n@Jbk_u+evmd3x2p9B36_?4$3hW8MMUBJJ9Z-L9ezOl&HnPQ^?aaof<j0b>t12LWgavvea#TsHPUZgW*ARjUjj}=h6pw~E&81)|@'
        b'-CD6x{|e#?y*a=j;@JXJ0Tb{YiIMGPH8F}Ki4k#Q%n0w&7-CGK6nS@fDly6sCgUfG4`wCtrHH$4J|Q=e&SI#Eln@(eB+_A~-^c|6'
        b'!dwIY_QHQX^gBM%8P5DmXGjSoh98z3Pgp0C#BT#_g#F8iZzlYG5tszM6d(zh2fPBkIiM}@!vGo&RGrWnih_tCrCn#(xm0I33_t3D'
        b'*Qs6jyEeXWc*0<x=q-Gg0at-qAQf&u2W<xS0jGg>;1VzZ=wW^rR2(LWk4HQYBVN&<XP!gc5q>kmh<*nApd-e0am4rnplJes!JPs5'
        b'ybWOoPdc7Z&=od~zS^q?zeP_zo)8X@rN<MvTw2~F6Iq-|Tx{k&HF$*#!Vj`2n<WPt#bja(1Gd25aQyG%%i(XdSQ5|kclluWvG`e?'
        b'f#;c<ge;}OkPw&=Kt{uY`PO9c1ZW1pf64RV`0krQjPvk)DFwWfLd)6wWhUI%p|=w#2XcW^Gf_{0NwdHc&m+CNk>~Jt4eajuQW776'
        b'{K!MzZ^QQi*xv_K19{Zmlf;-0NV9YX^K4?QN4?ky^n({NZh@bc>kJ)GUj{DiW{g#b7~?*`{w!m>1p5;J#U!z@7v|whbcVApf<K=}'
        b'-G7}ihQRDB!nllh#Y5c)toxl95AQ*^Xd^PS!CNRN&BKgwC*n|!IP^VF^ZV7LKR|g};qmiVg(SW=P!ivP_y<dnZ+b#5L(SNE-hgyo'
        b'Mi_(C-3#F7An<xRF;)SY3s4t8_x&Ap67Fxp4hQqgXos4sU|%dle2*ve!~Gf1buh~X{tgu3o4>((o2cJ;4tY2M{wD#aUZim}C)oWZ'
        b'@mr}nK@y*VG(`d}_`bY^7&-cl_L6|+<m4o*g`a0o201yU(_&-4Mk`E62K-|BC@0mgC8XI1wjd1Rbh4$T<pAvC3%r7gO6ZOTI3QFC'
        b'5t>x05bvXQ__Z_m-|zA_;g{$So;SZ;O7;qF$x~=r5qAhmGFWFA!v8kN6NV-HU12#jVFla}8ADbeoCAn=Iq>Gin@BFbxy3v+3Ev|R'
        b'w$}Om_`&0U4=k8c1%Gz}-|~Yzf8;0L4s{;V*FOBX!AAWe2T+G59R;Q}j+Depg?us?ieM)tL~p2r{WZwzT<}SUVCI{Iw0{{+%YrBp'
        b'x9+A?LiA4X@)2Sz0$!l%V<^WFC^xvd3539J{eQtOFbCzI0t`Z53jHHGpUJ={Arq74-Bu1Ue6(lW)SYOf*P;C%j3kB-V1k;^JbvQu'
        b'fuhGJ-+BXiWjCBg*gbn`_#(0n?ZSV-?-zkg;0*jND=Qo2_hSULn-~whc|c7E>LSeSP}_hNKs}I(_#6i9xI&C|pj$7a-T##sZNH$N'
        b'f!2X821QrJm#upHpXBcdHw5(*^&kZ5LAcp$R6g-LzcvB*a&p7Ur{>&5Kd|z6!qdP^*ipj%7~r>!JfHiR*w}}<vlnrB5B;_V`cG5r'
        b'MchDlfKQXcCFp*9;-~ug#OFLLiGL0#<s|VlpntSZ5+AtgctQYB0sFhrmdc?1G}O}$?}c6!)OytOeNfZ-xb9;~e2KSxIS9QgfClFM'
        b'qZng7U<)RO$)hCk;}K3I>dq5T2cu0KDe~0eY4{$2aAqO=r=h0r>n#CY2@E34aD=xC>O-Kffi@#ug`nGj9e@M)6lkGlKq%~O0Uid%'
        b'13F-OsHe|Z1G*6?0^SDRqxPmr;y(oa2)JD@iT?z&4j2PG3Va4M0L{QRz)9dopci;+l_dUW8o#F`@$-<jt57pYixfB<#2ANyjs!x1'
        b'2|zHQ0TPDz#D9pg*oQKR$M>K=V{`!_z&=05*eGR;2LLJZo&&_dY}lI%WB}Q~a-cYnF>XVCTt?nzf^SzsZw;^x>b0Qjf!Bc&pp?dI'
        b'wj_Qu^7$R8-v>SbJ_2fhIvQu79ykV^0KNsz0Ox>3DC^%L&vZe30k{aB=>mQLF5#QDfwcYG2!6Oi{m1uJ&>J*;0E2LS01gNMMgXIL'
        b'hX57u8~hmnqM#lRJPJ$#;()2ZG$0w63CO`ab3mU0E&*x4LLd{!0iFj|0^2o{nb$xIfI?sgU<Y;sHNYppA>at$1dahGfL7oKpbO{$'
        b'egZB7f6z2MggOC;DewFE#6Jx6AK<MCppyX|@Hj9Bcor}L{{ZrV^}tpj3H75LGz0VnfE&gb6)3|;fyaSqNZ(js2Gmah;VA#bpdp|p'
        b'&|KhoU?jd@2F<7baHwmbDKf^m74$Gr1r&!e#^`XyxET7U0vO{U=sLLJhA_rWpgV#6z`oH`Mj36chx#iZ7=8x<-$4Bx@FUO#40TH4'
        b'-Jrh!zXN{&0|0^DTcCFU5&ZH6I3NfZ1&jvNz<42?8+<hAWMB$l0Hy=wz)S#5uid~B`(L1*2P^{q1}p&>Dl`!l$%Xm_YL^6)6`*;*'
        b'tH4@d15g4C{sa94&=2$hSAfgFJfKvFhalkJ6*@-<TZfT`Ijd;fzrt7xSz+F4xI-Qi+F3#bse;)}^yL|#sW3YO${*$V6Y%Raa1Qtr'
        b'=%IBI=m)+P;+Qr44owUCgABk2yt5A&<4?#K&{J}~VH;>HzGFcD8%TsY8+0z{<rgLKv!Sj-cn5&9kXsHzhEQ@ukcplJ#As&;+MtjO'
        b')Cq5!y?6m*EKg>P;gcb^&0~y_pmPxK^HiqYep@tfN<^Y=i^%2q;1B4#wus5n=NV%L)MlXZ1;#jf{jYN~p<V~rfXp?p2Py+idXX_c'
        b'v<LA*UL623e}R;OvDL|zIa7<_R*L=z^1|b;ml$Ia>@Nixfx|$a9_`v@^bt_c!8kw$yTy<(W$PJZ@LI;G*~l21sXd@>9e6v4kbTh0'
        b'1t7B+Q(&ja%oyq3*u}3LPw0ic4*2=P3Q4>IerW&~zE{A^1=%tL-}z7zKSENA7~@9xcM5ikp<V-fjTpze;D;D`qku<%WFTn^>L%>`'
        b'73xOo@dV93F@`b2U(gUB99RPsy@vFGDu76!<2A}h_JpZNABltPq#vaIzJ##=@DzaTC(pm+>0{pkJp}v&uq!3;5kMmFSD*mc1+)Oy'
        b'fRLBr9#{>C<G`PYJMEWW#&<u|524-g0VAA6Tq6s>qoCtJIpA<DV{E~92XG3ILeB--4~U`erRf753p7JL9#p>{<+ws;IEL?{j~U}q'
        b'pa}jXfl3j6Fp#oc5<d}k%YWthqsZ5@P-g(eZ==6#DMCIpPpfzTGer?6$jej8x1cV-JQcVnXA|NBX;w-)ni=C9=*!+hT7ffAF9s$6'
        b';$w`lkNORNT%d}_F(#t=@$d(-V|)wB>Lg>#2c+LJMl)~;NIAtAdtvV~kWz|%A9xyZP6K3c*9`Lx8lUe`N8tCTFux2x_3Mxyz$K^~'
        b'p%)Kz9Vne^=yfy33Ha`(;e$p#0lQ`37pM)u3VcW7`zgQx)Hh>H^R>><h%qM_<kynH;VS^Ja^F+gFc*CwiBG}jCa8;nnNaTrodtRn'
        b'^e>>-sDGdlJ1`ywod-G()DF5B^f2hFpyxpIK_|W=iMN5y0DS{A7j!FV0q73URpn^6Dlopr_vgTeQ2!+W<p<gLMg=VsjEf*IbEFUB'
        b'lD@SxUl8Xt7>Otp<sO+VA91<@x4futZS(J_n}d%MO}Q}cSab6>+8(q^rD&_jAU%CAQ>6YZ)L#Ys$s7-R`3Of#{Q}JZZ35j2dJtG4'
        b'!~qckKeyp~pH6HHM4Lz6MPGz^oCUQCY65!;hGIZ|mxe#wAVt1%$m6GAmI<?efL?;zJ)p1S`w-|9B;o+#@&(kt0HfYR*w9M?y#|{9'
        b'9!(Q59|7%#o8TdYL;*VyogV0Y3p(_DwE3V<f+Eb!=b<inpT=1slajvS+rTFwNb_T86P?gc0R07Y7U(FuBz`_<3h3WJSA*t&ehB(c'
        b'&@*-+|7B7K${gXpHiD2LP#d5wf?5muFVF<&DWSfMya)uXhu&4_od$J*UI6_Xv;p~Z1oRrdKL(Y_33&mu0(ewTM}g?C!Grlvc=$he'
        b'J?b4GlqJmOfu|P(OQE+0c4*qxfi8uc@Nukh4(R1V)Kd$|>;tWX88M48&m7ko@(Of@i*PsiI@+8!(9S@81$Hh03c_WE01CL{fB%UO'
        b'fgAMjnS@~c$@`MviL7yOJZoI@jn2@FFceddCrkx;q23xw42Kbp^iA}`!|(DPXK0_EfI%rkG~b{;?L=Exi8O(h0p9_qBEZjK#9)Wp'
        b'NYIWiP%ly59Q;^;@{JxsFI(XGdH4<o=50YcK<Re0`@lTZ<6-z74g>=Ie_@SF0Xi5Tgn7tQtg+PlonMMJw^W!nBEgkHogkOX&}IYu'
        b'zzx862fpFw8Q41ov>-i=LR*49_n2qi^#A%B54Sd80{or;`Uvm>K&sIegRX|Y`AODj>(m*7kLV1!z#q_?^dV$1API7Z;jqqd;0(r$'
        b'pVP3UbY4r!2=fgbNku-};g1Y5NXk3NXR{FOx}REBie)sPhDbBz@pS5#$cVo*bC8d{4Bn^BLkeI>g`2Z;S>rs=44~*4);JyE+JTM0'
        b'HX!3AouM4#Z1dYX!%}Kzo6gV=Oj<!Q=WN#*O5aD^Gug~M@C2QJSwY00@1rddXRbB#yqJCuCp^g%lXx4ovys;bc0MNj+M9d`)H3K#'
        b'0`ySF3ueA>pG)|Jn>;ayNXQyGC&$0fDuncX!BYkzq;c*pN&FYUW}qCX1f<}xdB~Uf0VE`2DlOZ35g~W^?_tJON#Z3yYBA#RCeI&O'
        b'!W#K&JpTgHWiSp$`-}SW5$Xfn6}>~}wM1k%2LFT_(s}E<hzs1O0F!}uAW2OOiaeb`j9lGWgm@yvN%+1D{(jSU4UtZzGecZvIKTms'
        b'v_2ufmcZ>vU>lH+@QM-ML8w0fit)V;==+A&7k+R!ov$2@YQu|=j|}AjQJoOKJ~~xNW#m4dnEBBzVLrUO8R74Rd;PcIY2<4Ujqh&s'
        b'VZdRyI{>p5<P*K1kRMH`t1la&cM4`Lfa_l<?^>N9f4|O<2{+q;&A_~WAYCxu1@&~ul|%N>_&Is|CY@pDqmX$4LXLmQ^N<x3eec6>'
        b'(gJ_wu(uE>{|7C{g!*3iF%NaSZ<Wr_3rb#RjVhSyfWCL=oH)#dHio1kTT|yD9uvyZhXWiS1_og-95fhsp<QPv27Eq3+Y4UdKqG)b'
        b'_?L>hH3@d+0BfprhO@v{m_-AnKp}7m9HNOJ<V~paCB(2|x6Y6P?3L;b#Y6Ol7ku@GK~Nib<5IQGpom86_vY<4`hwiHZ{NR7G$_*v'
        b'fXl#Tb^w=wOTbN_A25_d7C`v2D1;-?8(QFR=0A0YI)qpM5$(J5hJL-+m<c<JY1)wfj4<?d$glq2AshSY4SP`scLJ_QQ9eL6?A?UD'
        b'X1ITDFZxH|6#q>^1gJO-yrcAqpAU5}Xcp{dAYTlquMp!5E6OSFco$*ps7guT-vo>)U|(O#8Ydxci~rCWG_U9kNr)SrQ`(uYGuU9B'
        b'xmIUb0Yt-}*YW)!Pz%%pXMsN84&Yyn{HKF9Fs;1WGv`C+9(s`<8hqygYk*RGmjn4we+?u-odS&f7y4TuGLg&N3#tJ9<zJrpt(1M>'
        b'JE$e_FCN$ci~uG9i9jmww~wg|3qD3%R_up6xRI8zMki=0zUz?A#rU3MMmbPELi*RxyayhBxJy_eP+UNHTaaf~o#6#Q3jc1x{4WO}'
        b'_m;CpGxT!tP2NR&{t;`Gg1*3_e8qZ03Sa{`=*fUa*kvID?1f(5D%zH_nWUJ><VO$kq!@i_D$1dlkm2=oo|zX7HX=O^_`Q?P_rnkL'
        b'8G7^w<s<Zl{mqj2?BkFfK*NLehG^*bL;W=L$k#$2yWbCL1&{y~!OlAP!JU9y0Ys{N;s?POgZv-hfo~J)<HW`lu=hLgF>s8!LD)ep'
        b'lK5AE1MpLi??k9$8)ct&1Q5d+@Y+`R>4N@>O3(`QCBP{l=?$G>9nc5$PNe%1Xa?%@VnF->?7^R#&@1Yf#6R)vwfJ6qOQ9cpQWDQV'
        b'Mk@^`27gcyzydNrLghIiD`W!`4tuMB>A>CJczzW0&p25l2R~#$^c?sFdKl(60T-Y^JCM}C8v8p?pI{aa{EG3=o>W5OD``K$-(HMx'
        b'bAdddq!#k#_ZaU1!+-<8XyA2V-n%H1_jHC;P^Xsb41WbpqUs$wLky?`AVq{kB8+oTzwsmbo*y8OokSgK7W%Tp#iI}wU@p-a-Z(3X'
        b'KMouL&H+0|BMtz#g6u6t8;QJ5MV*cYQYNCjf%s6pVNDs@wmWE7p}z)LI>#d$cAZ08+9rvQ0g{lm6u<x^<2wVG1!$f`9y!o%b|7Bu'
        b'lK2;ZOkf_60;~bd{{k<5%<~iGLf!$Qfnw;N0%UOa!qdkSGJ#Q&7`pgzl$dq({90ea;meF3vssQbBHR~f{`QG7UC8_XPShRX03dr4'
        b'@&h0a(HlD6plibhh2a8gOznqE1RMtXfU_>vcypxQFrk+<GKA;rU^gD>3;-g=+Pi=Zek5TWlh*~g6X6}(U-4F<&1NHgkfQ^MAqo0R'
        b'G1dtNRs03<o6C?bkuyuq;QLpg<rg|Xf-(BfNPjovYaqo1JwV(8{scHc1_T3YV2z8`wcj!Jst5l>qfWaLmgVH+(5JQf&!eq7@0qhN'
        b'f{aiHxwZo+Qlahulc0V9<2XBL9?bQ{=v!&ML4G_2zl)KENyzUwsPmvM0G@z46<A5b#&_QzJpWgyUjq7(wsoL8fpr(a6BqvPcprdS'
        b'v>W;0_QcNsngYxO=6LmJzB~!_@F+U7Hk>rpQTe!!?g_Yy-Y+3*+TWM#+ITu)e{<$$&8DV=+poNz8kF>1!itNK!>E53sr^XgNjOkH'
        b'2npM;6lqOG+HIimNSp8UM;czZ<wu?ej`%zu_tddF{948Hap&@z7AF3%l4M;QwQThG@7zC{$N!KI`!r6U!tY3wH4P)~jSG4zmeE1F'
        b'4B^pz3lF4k8C{e_*`!WG{LN<Y5nUhG|AaaK=r18J0lMda?wwG3^CuU2z2Jc}KYP|giUwF?u0>>|Ye;5{(OQ0$#INn=c{;~O*C+e%'
        b'ExU|<50GB*<S+F{0d@IrDEr?$G9qn1>AKF|-#p`Ty7o;eU1Sy(Pl-9<#MPNE2~oxX3v}(-;WO!c%$Ia6u?=c7@__DRpzCDNUrU{O'
        b'*3bS-plfJAJ=9;GR>rQ)KgSvXeE$rypT8u+9D%IfcX4p+m=7KC_tx1IeL@^iTg@4uT?ls!)c+)O5?5IBB(%L+OXCVM8=!K7(<48a'
        b'>!E(~2K0Opf4Ua=(Vjh1g*D5{%a1+2r!Ij|5cBMp8pFvC`=2FxPk0KtR%-m?>8bOzFHDtuuzBji7u%=qC>tfLLq4Tnm0&;m?qeF*'
        b'ji&bT4L8%`_vm8@kx$DsRtzor;>*b)D`OG}Fz54_*kQkPelmamCViIwW1rKtM7rPqU#xInDHq0_a6c8vjR#p2S@Y<P@S+N*j1yU6'
        b'Z_u~qoU&)>CbT1xYO(1_*s2zX#hNlAXRC6S{NygySR!w5ftxmQBD1z2n(n`kQQnxc$8IesYNi*ZlxkXLQTm343*?47!*0}s-Ef58'
        b'7|U>f?dw)p!fyQA`*EXgyfuoxY+}{OG=U{Unl&o(CULPXTA@+o|6FXN?|%u8c~QHv8#ZZCRjD+pOj;VED-+Gkc&N{oyW!ruYD&Kw'
        b'4(Sc6Du$*&HC(vUW~qxM?rMeAPB^Vyv&FMdu|i>CXdH?{U4BG)XMh`8#d1?m4&|P)3=Ytzfux13ci*2?9Ij0yMS9yx-<wgV?L_8O'
        b'92v@ms-Fuhf7Qy6I<YlLY%_k{SeRtXhQHRNV6`<&B^Db$W@f3l5KgQ}*)q|47elR`fe*7As{Pfbu<}iHEXSGFhN)Pw^<!p}iW|jA'
        b'6@^>qosRi8tw#EKws1biG$=e=D7+CYuk}m(W+3MK0g-sJH9|pBe_0UnP}&kjiG8Ux;^75{=yv}!`>+KeQpd@Gv?UL_8zZ4#0&zCP'
        b'KnflHHX>~c5>HMOH_OPl)HHGat<)V`=GG68Q@=PH22k2;p{VRTQ_cwaIEm$pfrbc0;Z@6#f!c`C6%h{=R;ULejgi_H{xr-K*RKmO'
        b'iZsPZGINr`I89R<=)+Bm{u~UnZ}Jv;`-;gO%mvX~EpkfP<Sw48Y-;0)-l!ERmM!tuS2%YM(A#reA`(+I5O+0Z*Fao_&%J&974~q;'
        b'PFfD-o5G6}wF=7{LZJ*PTmHJA<IRCmzm}PW$dPybs-8>V#23;BTLgFd?7^pFwhwT&n(YJCq6WvPccrTe3r|PPur~7tA7VE=Oip~)'
        b'GnAZW#Xr9Hcb7h3Q^6@)fO(VIn(bp{#acVB3o&s+XEz81JUi?OKe?a8Hmi;;G}@Mb-C#8ao0f*z*do8e2=3?YrBj+;KL5{wv)Q$*'
        b'xc*oY=ciuHS(Xpj?c#k?n77spRA{Wldt}jj6cxGFWQ?V>N6*r2(Io$x)+k1qYd>bDPzDhx^jo48dH3G(*4in1#wp`s+-oN6W;WMU'
        b'GjRc2plPbc9<e1RZNRZ)z#3syDDqa6Fm{`a?igHR_44Z6zYcICvq#9NX^!Hhc>~$=WhZ?(A8wS@m(-0cG})GMeuZlP&F0+&t@8$~'
        b'BV>j>0jF#-J3N^$vu)3wE<QB5aDL7^!-f6L$ec|@R*m>z?(iexYDpQ>kj0?DngdFiu$+}&X>vB~;-Xg0mvJF483*DA&8p}UUk-k7'
        b'((Q+tIZ|_BeW7XlVX;Lw(88idO}F_T5f`d$BdaBalWohwath~rJPg;b{3^UTVB_0gDnkZ1UzLiiG>KOS#;jC{;M+=*&q@`k3VcPq'
        b'GElmEGQwMvmOg`+y4lzKUYSoL1}`+(VL9oi@11F~j2`%pw*(yF1D5cCf4kE(WFY^xWz@jEb7L`s*ExSxL<Dz>KFR0rWCvQAfogwu'
        b'nc7wm6EL70J`ioI;QY+%=>-A1)9B_%;}O3~hgvx6qTNZNy$`B*%b_BYpv_R9W>Mig{Z2Bd?_<J>W~msWN)rDcZG$|GHQLGCf$Iiy'
        b'p1Cw2Rd~>(<YQ7SJYP~RGB(oZlyj0g?wx}?bKS}+Dk36kBO*uU1~jNdl?NlChK}j=NQ{{@fz51vgV?<_vg!7{`#5^8Bgrvc*R2u6'
        b'yr<r3zqP9_$kItQcZ;}COZ#<i9>x549ZaZ=AoSVu+rs^NG5g`l3hvy#W|YjKP!Ed^+rfntgLk9z#`yUhVXGPUweg;7Y{+8_<Nht|'
        b'h@YeRIv1o4Q-l|B{<9sHlhl9CpG%@yGIMSm6BiSg=zd3yEU&!YT6w+NztXBkfARVCBg1=kN;`*F4>xUrDfH{qoR}UUMmD&KIw$Gs'
        b'+{){much|-TidTcDS6SC+s{3;;wQybM`T50a;^Qif9%1~Co3XnaEHGNonCw5&y&OUoh)crI%~|Ux?4LN{7CU3MYYtL6;zTHd^$_!'
        b'xf9j$A&uXPJ&MfF6<3vkJ<0&#{?lNqGUzqG7yXTmz3HM`+@uPp;uXttZ_RYX)x<gDT1~%2aG$=l?7Fk~dTa6Z3P)u4Z7w8pmBOf='
        b';h)pf*#GGxLye7nS44(O1ujFLd=g`yZZ?X^jPcnJ{z!_0p7k1=cC6Qbb^5MBZm7e2{m9UUourbFh<WC^<C*Kmh=;fl#w8Kz+(^f('
        b'*DE(hYFU!_%60A0pQB9$F{{D3+KAEBY<3bYEalAW)e@CT1y)gsiSQWMrG?&bl4PfTlNtUZye6}-spsB19E!aA9gjtK{jJH@t(s(q'
        b'>AKk_*%(MKG}t{>@Md?M=YEMQ<4IA<6x~+6(NCdUI=-SoW?4kD&8PxrD;8vrR6cUOA=0;26<MK*Fuf7!QK*+jKGauvhNn*?B&x61'
        b'MxvM^DvKgL3R89@oLeKMbJm%YWI5};qrN6nUz`4*VOm)d{-<*I^^IfcBQct*L~2kd-Vz=L^<0srlD!puy;vm^3~HKgdhcQ>3G~x`'
        b';EFDjjrn;@1^l>Xx!b=hB8Jx5o5asxHosMJyq*gMQ=84=;wf7;ZW(F|EU6&dL#Awu8$IS`3LLpVi4f8c@g!#C^=O++a9GpS$D`is'
        b'LIPq2`*o#1RI`>aA--365_73v8xdj&q2ILr&|WR(0`$Ty!T0oj=INW9T1W7N7Dy@dJ!Bthq@C*%AE8ZDa6#I{aWSs`Aa-V|=vIvH'
        b'bs3qR8gXkCnXd>KM`C`7HuQ?v6n%|?jGN0`PZi!sB8Fe)^8E%wFG&jU=)~0|4)*JvhFDpglUvG(;sUIy<S`M7F|o_W1j&%(!k4(|'
        b'3zbb0!UZS)%9|}zV}8>u-fR_HvwV$NZ0SpLFZUOl#j>gZTTNJOs?b$%5-zm3a*J#S<G9%G>4K^mYnH#eE3zt}Q^HNCbxx>!Or10B'
        b'jfeWo1=P=f(2nmh3(0ElkGAJ&6J=>WME&1vMHb~g`E*~SoiP}rSK3M1G2XR4Ak}6*r4Nu-uqBLa@5~hWl%%Sq>QqCDytaZ&NlFQ}'
        b'+rhF2w<coPYnUZ7Y%eG_<duw}cWFhJnHz?XqKc}8$LHEBlho4;&2#OaDeCts+$9mE@+pNCkSWBK??$9g{*&^Kkzwd9mBh3?LJ%S$'
        b'7bjNqqjt)d4)a~2irLrCg;k*M-V;$dC)mA=H>Cw@g-;S2q1(ZlRs?6g*k7}&ziPwE(+u%zGuUrgKI*4!><9fQpwysSV3*X;TO?qd'
        b'!EwvIEI!rm7P0>l^KQRzY^Iyn`aYiK8=ttNKYD&NSKuF;BU(}6J4HK2&iO--0H-8w>tAW-(;Cec;-#xYXV*rC%AY|^3CTaFZFZw?'
        b';5cqn^znlF=)B9{H8fwXk1M$RwD#liQ}mz4KD;kFSbmLYgCDC6%%GxK#J(+CjttR``K!~?53h}lt{K~QJ=9kkoKwa&B@xFf{d)?_'
        b'o2}<u<!f980aI+Jssb$2`fK-&-eao>@!PjYR*~UnTRLI+#?RQ~$H|0QyYy_+B4TYmKLAAvu~v|cqomfI_+@kc)C*p`728jxh%)OK'
        b'D>uO`Fp_nYAAOwA+zVDR?-AP%|9^D7eOwb));K<yNkRytO$bEZw3!KkfLN2D<)zv}(1=P~h$W)6`<Nhzw%uAved*HO%-F_&bQeQa'
        b'u)3SXqClkrc3ZW&MQl^+(*0W9-KyJGKu})fO>ApXnBTb*Y`eeb^Zav@d*|G9&pr3t^K$3Ty;V)`$)S-ZzaO$n>J?(Fo7=Gu-G$J@'
        b'sxJyLPx77SnRmXNcE!UiMBMeGo_U9y1<30KeN=hP3554cX;e7~Bq?Rj-JOuyC%4=Cw>v}n(tpx-9l~5+$S!+!{83&PeqtBM#uto+'
        b'O1tbi#~j~PpA&VL4F5VAokFz;|2i3OJ*7G^5A0c`+W6^ZUk%bG3HuHo#~nT{;pC1~+!P1BzWAXQH??sc2j$J<V{E{J)P@TUa*+3i'
        b'_t0gK_ES}Cg!F~d3m?l{`P)#kj|m-83_%b70&V|4p__zl?{RA%WZBhH$6+7?RloL2b>{!9-Yi7dweawlet~EIPxuz0>AGM38wHFW'
        b'@tFE(O#jnZN-#=jlo<7Q$5PBFF`%R?S)bwp70ARQ=oGL1&R9A?UDS__xxMM&(cd2P+9U?s)B4ddgDqP>0%;DPn)T<$jQJ0z504pb'
        b'RQeF4G@q)|2O-t)X-xVpNN4k@GW|11XQcO!<$Mo+W~TQ-IxGDQq><@2ApJd`D$;u(4dGK+dN-tUJ`GO44ryunK}dg>-U;b8K7BsD'
        b'1JW0aG@A_(jEzmd2H9uQzk@Va6E85U!_s$;trDjH2Z#;R^gdi0sPtSJD|m56Pdlb84<-{0w%_Xi4gJ}o{}-fNlb0E6n>7D}1H(O+'
        b'#>_`YdL|Tl_n7VI-@F-^;UaD%B%NQ4WiOJE-=hXIBt}AJP7hhTNR}mDiwb0<(3l=-OjjDyXJqDlRXMgaed!7)%aIy$NaG4JeeKw;'
        b'zm1XNv=UW^MZWP(G_iKnWs*^?4XXOgmUA*T5+BVQvsb9tXYsm_A0u$bZ!l+gyJTs&HxS#H8(DrKSI#cQT0WDp=Z$6Syo&@UKWdA_'
        b'nEJ8REA17sGj(IFAZpKIEuqpEw%T{f$el>^a;0V=#=J7NiXoSiqRl%~+9V;j-Q15+y1UHhe~CGlc`J%}VXP@vzWT27A@9?|r7w{^'
        b'E2|Y?S>}ofbk?rzx2BU^WG;J76<KKfR2$>KP5+N$=8uto{c6`(=O4$K|2RfUpOj39Hvg&M!bZ7!b8E*I`D-Pv8B#K#wMOMyDcu@I'
        b'*6f{uo0efkvn)!iY*yQJ%;v7%_`=rTZIIX`Wc!xlAl3T4xGxQ>p8d_z;vjPU-iJCi$oCa?6v{U~-)0iBg~G`8wx=-fc>#Mas`=$H'
        b'&+}uNX9S)X$C@{d8Ksyx2!laM1OF@<)2tKJ_C8@v8Z)~w(7i^naLe1cI2mgc_k=?~Y(7=t;y%4~%m{j!AeZdM#aWn{5W*kdQ|PEp'
        b'A?M3NOKojeCvP`$KUQd*Ghqy7veVEQIMEn9iLGAAhDtrbV|?T#6`z2)SGaGUa~1&3+L#M4t5-S~H=D-1pYb;-EjEWrn{rj=)wp>&'
        b'7Wt<6v(@ZV*s68n_n=<PI4-W|&TzN+!NbLeI5J$^%B`G%`_6J(XSUB^Ulh0tTM;ML6)UA@^kXh}Q|lI0u|;Z|hDC1PS6KWcwn5@J'
        b'&KYCyU313L(iSx>l6%D=m5Wp^_vGGvl;_UvrrmOPjs2_GvBAJEh2X(Q)a)wQ8Bx8fBDFEFK*G7iAzQ+6@o}!X?{-s<{Hs}G9Rv2X'
        b'PgUUCkP$u32<66GMuo(s6a!A<3W=`~-8cDF=-8Ryu|cBgJyoqE!jgK+OsIgTOLpt@vN1C9tLbBBr0^Kxus0&09YQlaS^F0FdKkD1'
        b'blVRoP@cElA8;6muqBF44?ZUTfty<2!N))?1+6CcJc*O|%12knL<HD`*aFc?<<q3(ISKg}@;!1UIel~a{P=ZkV$9ZlVeQ(I^-s*R'
        b'|BlUmmbLHnx<0>9{^pC*wxkGNoF3%dx4*pb^=Y4{2wtE5R^Y~!k#zg+(yqM*Q4N8<F8$TLcH~CQCvi_o5ec2QfrRGH+k?_?@d+Y<'
        b'L<bdo9|v(C?$&O9@V#8~)!PS%1nK7Thr!FWzmZ<Pla*jFOCc9Y+wJqF@`BklBu;0f@!tyT|8biPW(ll4PqTz>k4HDCpzlf*ah7;='
        b'JrO!PcbuEL0}K)J2_j_V4f&1;0>P3}@<8e2;kSikFocFK9Am$@U~ek<==8LfFaFZhRPxsJAD+kAFX~%xf$Q%VDqBlFhlu3we`#$k'
        b'IWYZ)7jW0#>u1w@GVkpPzt`%NHylGt5X-U1246o1K5YVdTF^)o+~wL=PhGIxat0l_S}?>Z&rh=8YHL-fyE6=DROMCW&8|SKB?yaj'
        b'Hr41VD@!VAl|LHUZda8!9(-5Nyp1}*?7HogD7DywIG)0-yKZa6`^^-2+Z%%p%x*ceiP?=npOeN!@WBC=@OLj1?m~r6N-M5LzLxO!'
        b'#sKCml(&>)23qg={cYdl81skQ=!^&n2GOkYl}Y{Uw_Vgc{)mSiHCM>M$a2>r?5nM}&uqKxT82$Xy3TBBac@FiZ;IxF*)8sWMtls-'
        b'6kO(5Dn(g7p1$d}mzrNK+`I2Ui~I7IqLa;yl7gF@vj47EaJgXr6Ux<hPX{y#G=rS-<d2@h+oku=L3V14xigCTxdzcv43X%jlKor!'
        b'MC@M6pO3*(^OCA_lZBCqDMC-)ZRRF|Kb53kc{@G#wv(s^w>`yWO=c{pe|bc`5ZW_;CNSq?j2RWVsAQnfwGLzR`M#&!R(?GUuAu2C'
        b'hmisP<3Z7RKm8oD<Tk6tlzB*ge!iQar<Y@l|Et_8ZhrhWxc~{;)2I<;#5Cq9^rwQC%;x0V3o5{?IDlw<QeZxld|U|Ol8FaBKe2q#'
        b'lHG#~{sSdie@TF9S*!WeN%GLjM_&$F<n{DNwtOj!Xkgw#^=VIk1l{8O0E(9xPd1ZyL<7AD>uKeb%Y-!581+HyJeeozHioCU({`1P'
        b'r#0xnjo#m2Z0q`PUZ}Bcf7I?J^F=wKx0n1Yz<Bic%jh3$(-;kEw|!g_8lt><C##Fjz|aw(7{<&(4`L#E&`dJApK6xeHfHeiX$E@W'
        b'Uah*-ulbytBW+J5gT<e5=^IBqg4?!eeTNwH^o&mZnHV*~A0cMWz{IDx=J8SJX@FlGbGk<@%L18iQOBt3qedG>-9f45VcP5cXF^a!'
        b'L(fOinsk&oEsAK+oaQvp(TJZq|1o-|f3(Hz{#FD+R52U)5%DqnI}Tj<vBlHxMR|Zf$x)_JPv@wOMwCF>C_)r{H)@6g5e7VjKM@V^'
        b'*YnR&nnoWgLkGp}=pH2zrhMae^FK%1+!7%8$|yfyB-Rf{(V+@r3@oMPjgf+nIA#2ZwRyC&Vf4)T(QidSQzJSsW2?B9oxQUKT<E_6'
        b'f0X@$o+G2B_m~Bv{=18d#9Q_}Y!+ercQc+*G9>3+9&08B&Q1ZAb8K{}NM%%c+@s7~R6%*Cj|v&}9GfDM#2tIM=B81y6bL)U6V`t-'
        b'{ZBj!AtFq9=LYjWD)(AjEvYxGhetETmJfQ;ouj{_`4fpi1>i<&8?%#_NU3uCdSp42Nm%O{#=*CEwTqOni?GPo*ku@~i<eL#aQR6o'
        b'%w)W$1~gd*Q#R_Q8l93I;AZ`S3wp!r`4hxNzEUo2t<duC@6MEu!bnU64B}{zYG0n+LY)D<+|$S@rQe!8{b}jxt0{Ch3p!S}7WBY>'
        b'mKEEUV2z?RH`nt=e>ZO!B^NY!nAdoM&R<DiGm6fsU<O8zv^;~lOXDbh-p}UbjM}I+{@|YVp}05!v)V@U#F4qH!~p*tf>*Zvi^)NV'
        b'(z8aH{Lvy|&eGAy!VSVANxi7qI*KM)A-N!;VS|ME4FY>zYDo=%QkZr+lrLOeVDt31c>ftuNJgD(_WFo|ecb-nY+vCv@jn~I1y4Uw'
        b'(XjTAib+Ah#Tl4&*=VvjC^1ExEQC~Ox%6d<$Z>xX+h~SSH-FZVon5l>Biy0qA`2bpPFtF4HT@GQA82K*)y|5+@rvG3Eq{5>2%v3='
        b')fcoX!HYKaaZ^ors4da}a*qwly3sWX_4tE(vT_uo>59=}4Q7jmFcL$rBFaQ%!h%!EInr&S4Z@$#{RkY@2LdPZ2ofZ`Ojt(ryo=9~'
        b'Zs1Q~Kxa~@M$g<HAtecco6F?hbFzj;bXKDjJ73qb49pctwz$`M-9jdcSJ}fOyFy3nCCu9+UTs=^;4a0eSDWA}O54>v0y!Dv!dyiO'
        b'yT(v%I^@D#MPa*!P%dcHRTMt8rdxZL^RGusM!jm#qXNb<qH0rJ)V@RpY0$egq*3Gi^y!}-@o*zXbu#Fdockj$O1&DG2rxSg>f}Z-'
        b'=yZO0>`d_p_+T2l*1b$+iI_Ysy{LYvPV^;S`!Zm2M_2jAkiT?h2%tE0&BTjZrf<X@uksfC{C=)?gqDO=+@>Wj95K2it+X49t%;!B'
        b'_=rm$UvnW&UP-s|$H9_etTD`BQ}8E^+~wDMNHI8Hp>xD(8gysD`jD4T6A2aGPotO!B$QDVr^U-XOeXqoAcU&~tMqJiur61ppEq(m'
        b'MCbGxq7`;Wy3Wb!&yCbYL&28<JNqxzDl%JzwaL+E!bZLd1IW7Qf`_AzhqOh*zX@^IyV$qFp1IL{d2Te%D<iIIUzh1hdK)b%Fdv}?'
        b'|8C@GQyBVR9h~BF;?R|S{J~`Cpqsj_&Crj)rUrBtbv-&-vZly?Rv~|$ZeCLjdQgK-4Nl4APbbj3M|A$Xoc*U2ptk~3d1l`Te+eCP'
        b'Zy2qA2R}Gh!BvfGgD<eqB05c|j6YR^l8>nTxFzJz=RE@RIuN%#<s&1kyrV|mykjKZxo@8<P{bcf>dF*AdAt@;KYME2P#qq%R?d_H'
        b'v^Go?C#-O}B%;!*?i!gZbLvhSX7k8{<B^<UD%Bmk{mu?UfE_fY>dwp&`l1lMTzk}tQ7?}0$8~GBs#Lq%UFd)!ZDi%!^Y+K_g{Y%Q'
        b'^J@k0IFg>i{Xf6PU5Rkh2f29djuV0)ZRJ!G=zUD?NGbApoaj{T<5D{hxg&CVc{wc!iY&9+(LuLm5ddq&^vg$}Yt=*@e=^v%2lw)@'
        b'6lS;Y-VrfNzhs2T7)c5b(wjyYBmBXc^bvj-$Os>fG0d=6%XCOFOT)dN?}?72gIF*40P!ea`xA#=dGPn=>h1(3rq3UN-z8Q41NxCy'
        b'Ui%~GKevXNJEC%zI3>TnbDD`CIe=>=6@fMWyZM-?5jqoRW{y-#SobD7Eh8m6f@jffBV;P61rHc8sH}9r?iM!DGPhr1%KU{_?M%9x'
        b'mW?>&c9ws?RL0AW6=S3$brMD~!k@uDtMcv87!a~)BQYsBLyn}m<f;>`LGP5;G}W|K(&(Vi<Ez0@KO-4YIos^fAGCffQ+<r^omkC3'
        b'qwo=kGgKeTTAc#>PQD@ZfR3NVpXbgGt5ZOY4}*WMa>~+b<dxO@HTM4TMxYyK`Ok>$8V18{5Q#{9Mm}!J!AM$_s4^@Tt%uxlj2al$'
        b'|7X~VR|l67PFiayQ!`hFYZP((WiMJqX<sFOR~TKSm@3%z|0{Umr(YLnox3g%lM()+IA`rMYA+#-Z0Iqn8-=xloRc8G;Gru0Om*@Z'
        b'*U|q66`}(FtFZLS10+uMtz?=IMxCr^i8>z>96+~CMqO3aRdxPt_{=B6<g}J|(M5u_o1>kC;Rt`VP_>Sh8Qhzu=6W?xXqf)5!%(dM'
        b'VAx+w7lrYl`sU#Wa0XBK1KmMuiK)_LS|l>K(;!DL7Eym0Mz?kL91QWxQTZ^qo^+9*=Nd=5{b%x0{}}Qd7-s3`(Pj4ghiUkOW1e@0'
        b'3mAW$12|JXOw|lSP!o5~@`ae%JM6^;a{><^`wg{wxT8vL$P}igRO1&C<*7BvOTF)6?nD(GE=}3$4VTh+GWYxGWU#71N9`O2H(He_'
        b'Q#Hul2UYc3wHxBJ+HjyZ5Q{6)#>Hi7YvS@Kb~vsYC3R>E16ZQM@E<*|4SS`c!^eiG*M~10MD6KPTkCLi#99L#Aq6D~&A=a>L8W>m'
        b'T~(u_Hi4M&O@WwIscN=rrO;FaG$kdWsd#8=BQ*6qYHH&!7=Pa8TZdU(=n@G|6X5^tJ^pmHA|_=Se_;KEa=B;q@WuDII%#EPNO=Q9'
        b'%@=CW!t2^|ayCMG!6|Fymsi^ev?MKSmqYf2(pLYA_0`gfd5w61I~=gnA^{l^n=BxOX{rZzg0jIf7cLAa3Zaa{{E=k9N~FnCiqJ%*'
        b'(uOaT$@yz(dHtRu;g6x`^-9S%UTWSjjSFIr$tc4xTF_2*^5c-av})!^VemMW0FOnn$405S!xy&8b;+$xo^8oX^Tj_tcz0(np=dO^'
        b'He3L9dHr!qN0HoKXlG^(UnrDAoaQ>%v9ZW$+7Y<W{^p`Ir;H45#M7Lu_WJGFaaF2#nZ<>tFB~!-dDsvg0xpABjP(T32BkDRQD(46'
        b'Ng~AoHW(iGuWYd|GMEHS$#PaHbsc%Q(kVj+WLcyJF=j55Gzv9G9zTt)kiAa<o&ub<l-&2-<i{uKC+6Xy*f=!Bs_#N<R{7xNo&UYs'
        b'uJj>52IY2Dv-qc}zUglbrH>5(dkusjTR5I{Vy?b-2$*b8W0g)j+PAUY4mw*i&H)V1e8l?g&OCd$&|Rm)r03IA;}71IUl~g8@Z%Cq'
        b';kq&eW0Oq4=yXh>A`8ApsQg3L@qgkX!=lD_-5SJ#(=ey!NJeZtdPiCoH*>@z8$y$OmD?%vOdkThJ*Bi)neKA2@yG_2r8vIlFprpr'
        b'+koJNzk=If;?I4~d4I@@3yVeQf?;dZ(3X=~7tjHIty{$%{CaPmi@@9s!o3k%Z<w_BJq~8erUu#C8hNpVtlXz^<w+X@AWkR4$RPLe'
        b'?ePB&r+j1T+MAv?!ZXF7o->7HaMC;hiBG*k<?UAG5ZF~#BGNUL>}XMeTcUEdQk6r{YBgS7Mu$m(MTc!rQ}wZ~V3_mQV=xyjVAvrD'
        b'MO;OgOD$lw4>dc6Y9vhQP*eq-DWD0gQ9x&km;-~z2ND##8}9cFT){FReSZpcmipZge|%saKYPjzMdCSuy#4~oW?miorr0GB>^&CD'
        b'PZDO+5X=&%#6M4f+#Sb$^iL1wg`tkAC;9xHfY7I+Au`Bbr)qQSnD<fpy9%J7<~-niOZt)PnO(mbas>kF<@_0a7xu|LtA^^N`x>g3'
        b'eY7FT1?nkN=*p9kipoES9ABoZ(dm~C0nNIPdFAvDD5vC&rzI)c<cO4HgA_|CO5SHE63q$X*XR&m7XOMbi-sBnz?SqOGSJVK8ac3q'
        b'N*}7B;`H!SCWuSdn8W?L{_!Cg1*hcaWfmA2x@~l7WemNiAEGl4`1wdZImps1N!$OFuF}f<Wd(btGcOO4fv%#b_`QBi!cggLmjr8`'
        b'Jyc2S02vw*jENgULxR^<1-eh7MMEYA6*Q}XQbs+*Z`FVZUNw#PInomcJr57j(I^Dh&l=Ju9`TZ5b99I{u|tG8S8S#8j2q|;#yUg0'
        b'ByI&At*A%aRq6yC0obZUOYQ{UuQXLjw!1`W7Em(>+2DO7zPCsUe`$Itz)tOPW0Zp~ZPt=))2hv0?Td%QMXsV3Ya`@--w#7Fnn~oy'
        b'29@2y^zR3a!u`r;ghovW1VNcZMKmeiK-e^j4l#D5n-mvAc>q?u!Wq4F(T3;^i|XdJ2QFP<)F{dX^>V0DCkL-_(-OpB%Zv%H=6B#0'
        b'zT7+bqBJw$@Y{O*%|W!JK%gasTS78~KL->`j~rAQq;zyRvlj^zzaD{Xcn0XmOtn+7B+OSIU<nZxyRl4#^6h(UG`1F9*WAPcF%k>_'
        b's-JW&DpMe;wk_Hg{l95)3II+#!twXRMD9SUA*6lfR)B=g@P$EWQE*#G<{~lLPo~t~tIkwj8DCN(u3l7=>Fed*3Pfj(($Qh!fBWqX'
        b'^&aX<OR$jo<W|!Op>jaLd~(avGzhx4#f_S43zm8s2gxA+ESWh1d1Wc*sUP(5cdRq-40>u23N}o*w-@&u9Au8%g1E9ROv-o$f7w?R'
        b'kUx{Dzf~Q~Y9Fcmi_l&s+)+b%_6;sb0L*)T1()u=^&C!v$pLR==OBr@;&D}rDz+xj2-XH|TR9-n#yOX+bOmcul3eKC8*O;Ix&1$7'
        b'@!-Lq4z%=6%#oPxaAnI$+_^d~E^a9qY|-AYS<S!mgt?dg(qNnW6uRkD$TZzT&QbAT+rea@q7mh+4Y%4n3*a$YvZzBPRLP+Jcem)m'
        b'aJn#z0$6ag3YSxxfFpEa7WL9#BS9BNQokK6zJ$|-4^uA=(uFhml%`&QRL!T+)bo(0GH)Y{q&Me<!8n3iKWNSm%h@<c=f6l5!2hV6'
        b'BKWVM^Fye7$j0UrKsJ;HKPdktb3Q}uzLjGejC;kL{}ecR=A#_FB*MHhkY2P8osr&)F2F3vn~qY=B=zVZdvwx_W8j<Fb7k&amDz~A'
        b')1EyjEqI6bRBPm(rw5}*==yIFS*%)}6FXSCtxUwK*_@?=c1CE<S6|4JvmnS3V1={M{tniNnHT-pZZ9z(6|Bx91GDR^yo=uPy1AUW'
        b'w+>g+&g<E=s+x4P2I>}$l*=I~D*X?H%GK%i29?){xd2vlDzX_-@l5co^Y!V7s>g#_N{BV6?Z;J!u%uvTx-uSPr5KwoVBJCde*wGr'
        b'lvi|G*35%s2U}KStmqWG__S9bfU1ZGtAgEjVaIVqaOsIk|J!jRraV8JL|4@J<OElrC&MaM)m<e6-DTT5s(HYZQ#&P%zyNkfuWXlW'
        b'kPU1Cx8Et-HEobx+5|wfn~M#Tdqjh@8)gMYFREq&kjyerqE>q)QDh{V?GcEw#$Z}Kla!)eR%&~N(euMCe#2EY8IA%ww3&)lhqH_J'
        b'E6o@k`qd8GbT%NAx^l~+#i+}-==|`uP-(>x&jmDxn6J>d&}x=Fh{Z~jbU+}vT%`(Wa|<9y^LoospC6O6F?s;8^kQ3zgIM)aFbvE$'
        b'x7b4c%Ho;y49OPT46iy8w3qv^5GHifNuB3kx0uVk9P%PFf4WOZI2UQ3so3TU{i@Afy=8+StNnC9qp&QU=^X&L(mt<npEKRHPGMOc'
        b'?$TtnxYt$g5moNoUbe_`GK|$^x!mjQZ;I@3;8MgrgLse<T+zSjFh5YK!P*Gcy{^pQ4V99?2Ljx#sz!8Cl`BNZHgfhF*(Qh^YLJ)X'
        b'dPc~Gez$AOEqm<tw|K=FB2+o$5PsQd71MAFl{_P)C20Y+8MG$b^&Y39glkzj9rBPLhJNND)S)*5z3w!|?PuMiz<jSJ%k2>%X3ZAt'
        b's=h_5mEOQqU@zK5gY&auFc77)LJ+}6c&=;=<)@Rh*>THLehbxoH<VUKR}^phNQLflL!-+E+(uY?o>pqbUbO+0X|jIok~1?<+lAv2'
        b'uUmjH{s0oe-n1#a!auX_9kko-)>bv*%=d`5jQN%}v%*WOWzGK{@R)D;397v%Jq0EZrnX}b=ducWVuL}%HM4^e$>nkvC4_lZ*&y@J'
        b'DRB-59QM5fdfmOw^k>j>UiE9BB9yB!H16>#v|zo@f_K*L!2I_5kz3TfTL$6&BbSm5mP^uPqt!TIshUm;_gf5d>WKjZej+wsq|do!'
        b'uq`HW2sF$1-FfJq?QgCc+*k`OuskbndQ6o^EB}gKP}ONp6PkB9baw4I^H;`O&k=7)PZKW^<cw<V*WtSA%p=d&EI%OKpxuz!x^jDK'
        b'1<1fR|7owU5S5vgm&WT2;(qQ+3D~AF4qF%ip73eOTV(Ze{tg?2efDXBnTwd}>)<e;J7>l~`zr<!5Q&Q~aAbf@6OwEI%U*4Es*5tV'
        b'skdd+CAJ5qm<?05lXze|HyA9+3Da5591~)oh2Wi#lCA2zj52juhSLmnBv2<tF;xTkCq|2A!gPY0TC;lS7X9FTSI!Ups<aZXW|mHO'
        b'2XWb5vLr%h*33jsnFv#UDo|DlFybn8X`mUuMdLWy{xuto_-VXgZeW6xxjXRlyEFay0f;><#|emMEGr1+T0i<)Ksyty(@C)XE!5?H'
        b'Z}1vrD%wWYJUoC<h4H9}+IWPjXW&=gOl(CNl|cmp5ECC%s|uPUMQ_M!fAX&%pE=jx_6^RGVU|oG)7IZ|lw&UoypnfaWT<<m4)nUc'
        b'PgePk?yG+fK*Ug4InVVZ<|1cwbj+*#Scg<<gUW87=XTHQdQ!kXNqC=pu&?<{OTXuf0YKeGhJoUCNd+xZh#^Y6QsNsD6fw+kJ1eVn'
        b'$=qI9Q;UrHWWZj7&a}lohG0Ur>(l_i*y9E0qYm^%hyVV?69ZoN-^d_x=DEP2hPQ%Z_Y0iit}pIZZ2U6F{^fQ{>12Btb97*i<iYnC'
        b'ZNnt~LuUA{BLfhc)CFq8>jiQ0x;Sl0Jvh?kjQ^Zi@Ocjncz);ya&{dYI9#o4J~*JF=O<J&3OZ;x^IAXfFP^H#QJ^su|2#I({LTOw'
        b'm{cS3x3$mfg&}w9$nwqQGJC7g&ZH~XU`<Zo-<^dcku|<M{utv=15Qc2794&5I74jFZew;1km0UO0plDvQ#Md1X(6%r1{jV=flG=t'
        b'Em!GkS}QZFR6DEeZvd->Y!+r%HdUWl)t{YRVhiiue~1n1+2~9<uCQ(!XvB*g=x({w1k3>BDT98pZW=foD)q)-X&<Ok8+yjLYB3q~'
        b'(c2F%OC*Dpf1OB8VF`hO!0b*r#OV-0l7wAd<rv{ko<08sOJXN&tO<+!80}a^e0}+`{_G1Swi(^~9p)K58*^j-D$jX#;7eiNtLPO9'
        b'h&yW4?8a8kBu@()i7WEjTij*&b5bT}fE3#@v1M&9;-BwXyev^UO_1GGg09XU=CY69i9A$0#O+!#U<?$rFEYlyob>kN>5B$Pg<%n<'
        b'&lpH1PQ5}Z*csi1rP!&hI}C}2r9x96rrOh5S!HhtL>^k36}uuY=;tB}FU!vfOgA`Y-hcr-_OW|pg!n3due-!!80birr=}VdSgb<M'
        b'o)dtKLxC>U4kZ@#Bnq9&=`c*`y-!PUG9reK{J{`t@!s|>#l>H6Sd2jxV?^8gyh{o3XB;gd4B-R{@#8&cF>V#%`-CqH6#Y`TROC4M'
        b';Jc&g1IhS(g}%R!Rd3R->fdoJKp)btbLN)?CkL|!xuoODMuHjXL;LLUihW-aEpCpHA{o@;Q(u7i_pu;cSNh0#2KuF-#I!_J`rZD>'
        b'#5|$F_L5RV>VNES@f=TRKiQ%?sA9fA*qlUR@@vj2aL16TUu?GhHfN;YY<q=IOLB%GeU(o)lOnTii`lj{kEqz4CuBvK**#-r7@gDG'
        b'?-gM^zmeq;h4VAD2kVfv)Djge)!9eBrbYY6J(v5*3h*DlLk(($BteF#=1tM7tiIb8+(S-tZg2ZWczRl+2tZ8Va#-Fg$~W)vPmT-W'
        b'N#it-A4eaDHUFdE^Fcq;jJnS6frkFJ_8V|ac{Vh?wLiH;c}Z!;1^aVzPV_@v5gB!%Q3ZOMROlLXUZcQ(<NK@hE$A7MT+-(8MSe_1'
        b'{PG+(-~>Ex==UD{2mz4OvML%r{^dDgz(vX`A*op?B9$yI3QA1MOT2($fA(O^g$8uL<vR$s#95M6;r`f;6mxv(T}+V%8bz0^gDUn!'
        b'nZYPpD2@rmeJaclOq@EX|6@P-nJt)DX_<YYR=&Dnq(Oe1@Lt7>p#7)>ghq^2jI+T+=?yG2ZEYcAFO=ELL{M&_=$ru;9wGE=`q~sd'
        b'r}ldl-TL26^$k_~nQoyG$DyhH-7sy8So-Vz$->!*F)QYz2u%Ulb7Dt3*Jc!o!H^n*agZ8I{sb@rAT8<%eQ`g`u|zajo=yG8th;f;'
        b'I;=oVI{01k$?qx;PUtuElZ&m-^{*oG-mMeESnXd%3YQXOMGOBi67xT3=uJZ$+M{Crj5FtBmc<jE=laRnJ+sI>!t&~Uh{n)ZX7#f)'
        b'raX=nba7r9V{-d{v00S5kEMT0nfhZgaVoo?w^LEQvB?3up6VyVVy^_zZU121f)8nQvy=T->rzYlosx=bR~Qx>E_7x(?sI<i%s)%+'
        b't1e>F`YY<`qHOAke*b5C)n;0oU1Jve&)Byn_m|#f3zJJP$C>Q3tdSte!eA*C*GJO<Al>I8sDM5)@VMzMaW+1lZ5RjTOQzb~g33Oy'
        b'uELne$BsnC%>Hf6V_EFE``+^$-NsqiN#zO5`!2>{sDGNtkeMS2iTc|hOfVb!_t^_IU{XtnOf_iMj;r#k-zcVGYKdBg&)zIMsmN3x'
        b'5Ib)9AE>8cP)~=?R>`H`PWM*@0ADwEIJXi({L?hT_rVj;?~)F<z7SMahOl2ucP$%eb;?~d_IGE4vo5$sQcc%~X$>{nxa5NGL#Fus'
        b'BCgY?lQ<dL4l^|%U$yIQ-@Z3l5a>KI9K;Z-@l?{P@;yW#R`Egk8$>1+nF|%bIZJCA&vxJG2~_%Hf9of`p8meIAF4DPl%Br6)8g79'
        b'rS)oWBW{a%@@I==b5G8Zu8){zb90(6mFrzN?T&r0D-LiJpVisgbWvHS#f<^Xw@8@MFZPilW3+r_$ZQtRG!mI$1=G@mWayIW2qP_L'
        b')!NLE%z5@jtso2sBx$>=+<DuxSE<s^_n8+7E6zt{fs2l!cV{mkD>76kk~1nTt)wJ-M^&D%^dr#sn{s9LT-7S!UZtSMV8a7lL}2Nb'
        b'N{cQ#TX^A3d7ki>=eWxlSQK2X_%({+qt}}L8%MAWm$(Q?@zGEGNZkJmiKNI_o$+5t-skN9jl^hn+gInWHb;@CMTq=;h!^{pIfca@'
        b'Y?D(}CWHs#MiFC1-LlaNvl^(%cC?a#_PteXG*;ZmZK{!P@&~i)u$4;OY*U!=5HArzD&21)xII-)p_S>&u92^O0CqT3;x&e}w1pLn'
        b'KU8!v@6s<Qox+#5^ywa8EEBF&3RYdT;ZidpeR+CcwgY?}p$bCiXzUjV+-#KE@B}lFz~gbjY~>LZ_O;ds{);qYf-N}Otcd=v_6)sE'
        b'55N#MiB;HVHb<K+4^fMIX?ku&@p0joL{@pn1AmHnqPM!}$Q9>S|4Qf_>Hf2I(*5O3Ibu;{0~689f4x?*@i;_V=)V@dHrJ>2F^l?I'
        b')Y(y4jS^<^CX~mmo+F)F7xubIhD5OY&r^@}(H8}5TeQ|y9Tq3mYC)&O#cL%s5$$dD68~P!DnK|#;-oE3uAVlH`~4-)PdC}NwdB%;'
        b'Bb&<}(kJv05@Ee01%2`XiUOpTHD=2&nDW!TZk&K_@U#&EjH3ELJc7sJAsLKmFFnv@blamUT?rN0*BsFYfnys2U+}?m(zJv5wJDO*'
        b'Qn2yN-%w%F2T{$6KBSgUqOAAqXSGT292I=n`zw7L)W_@CU3Ys)9D-EVE!^y!sTcGSfl)x@2rUN+z<1v)6S-*>{BeD8|G_t?QRLJ|'
        b'Nu4+Si_hfo9WDcN^yYDaSDVFL?<E5vpm1d-oH*w?r*q27!ktuEoKs(xvbR6*w4f13;q5;jnmOWX8?UsN{E!^PxNq`zO(yTX-0Qj2'
        b'%SuCHtN+C}<2@h7e2$tCk8)G~bI#v;jcr0(n@YJt$hdC0JOWm`++HTz8}?}J-xUxf@41Sj`+OSg-t);Fi{$V>ZLz(fmJs3!DIvq8'
        b'Xs>gwLWH4jwfGk|-nJ}1+_J?}V3_Iqsr^Dty%n|?IxlW95}S8#TDRXMm$qrLGxOiV7mBjQ<K)aiyfJWdIjtbnr>7$wfBG!MF+_$s'
        b's0Q53_H`X6<R?!N%Q3^*`*DkvTkj#u@ERJ4+WjFA^D?%ZO;r#D*)iey7A=VaJ1^?5>#VAyMxHGl-?v*4h!IP%U2oh3>>zT|>J3=='
        b'CBS{SrqQLzMsNL6hz!hkli%BHRG}?6Z{xlgEN6Z%Ey66uK!ZqNIV;h>-iuuGo;r>Wi6(^6bnZjc>%ByV&P-z~UzM~($9kh<G<kt}'
        b'_>xzr=PbDCB@$Xf*Pt~JIhTijR50D^#hB%Ya<t-68Ip(JERcBJ62^qeXk4hgjkge)UbVcbNm#I4-u_xkv=(v&De`pf%{H~{V#wMS'
        b'LI)*1#qufjPX_z$`~AG4UjJT?!rnG_2wM1BhPVK6Ozl>Al$4qCE7{fALzG%fGr=)ydUeMjO2+sbaQyEF7J==dGZUDHZbI}7r4Sp>'
        b'`nB9I?5)EqA~e6}sFdCoI{8qfl$_RvP67~U{=hM_Z+hu$R-4K<ZD(Y?5Ae1J``<?<(=hvDQSlr?JU+F4uI&ZS$za1MO|Ri7XRsyf'
        b'AL*?lYVULPg#O{)Ok)4rbwuVeCLC2;N;vLuhWJ^G66FlG950<?xjOk^o-120_9$*=?a;%5agKjKlXLbant-Bx`f0uC#7*V4X>Fd&'
        b'7XB_p218t;zPe$fvzBZoi%Puoi(qhzB5e8DUUhbRc~QxO?D2Kq{0@quDwwewy!n6%0XB6uO}`jtp#po0@b*2n=!ZApR6sAi?%{&l'
        b'93A=)DWz9LQ-WSPf39Xy=FOKk5}FpyiuHm?K}LV?L+z`z(d27r;Y+kn*(RXgzd_Skd%G0PcW;s>HM<|OoR`qipka_VMMsAyS<Ecj'
        b'X9-1%qdm_m>1a}EMji1hbk=Pz-+o+D7j{BWFF&rWOFlu>>rV%^d323LF%eRf!CC`r80IYMfOA)!pk7iZuMexE>a}(H`ef)`HRD{('
        b'<|i?Ky1{C*lzHeoUbMflYqU5cWJ8AIGY+GPftN4d#Ax*Z&0Z3;((?G&;&VDyomD-f40p!X1aD0$qqiAM|Kxc6)9SG^hf#A;<oRY~'
        b'lmChsZW$jtEsY`@1&kX#^PIj3mRZ2O&p%7O?K{WsiE5+8*~EBDg50tbtNoUv-6542#01mXqt`r7-9({+c{&^MkbdvYU0>fIGW5ta'
        b'nq_F$K*U2`?_(D|f)1zbf)n(B4CIS2g0u($0Ng-2LEu{b5Wl7h#sgxUAPjUCG9S<0Kqoiw_G2>^p!qkK;PQ2HROSr@K9kygGn*bq'
        b'pNI;UZ^onr|Kt){9DIm8hj3i>%kq(6W+U+KQDr7Jb*&UuQAF|=l-hzo^owpjm`h*>el+7)PyzZd;-jbqAFdCTCH$~{cX-Z>n`pm!'
        b'sBlR^5Q*Z9nIn<3;|>=|zlcAFlL0Of*1ptb!c0GL36j0X6$$$ehtFJa@^JV=3FU{waj_1Id^Iu`y$iRj=ZY6&;xSJ7_2jOnZn^?{'
        b'E!zTJR*Y%A!S7bb3gdC{Y|ImK!?hS|iD$`(re@LM$W>|ks+1`rS2Sk1BHWd9!xcCGetq-Gn`G9e!z#vtdT@W)rq5d2+9z6%pald*'
        b'j_}nB&k6RQU%tf^fW>?<|8xLzw+BicIEFO_bOgd<<-U9H?9_>h=xSkm-!2s(PC9ahf9TD?$N=A0T;!IZcJVN0`FhOz#b4a+lBjnM'
        b'KPFr=j&{_Uu*gEw7u@TC;&c4Ez!{vWxWR8j&dBOkj>~{m);L4@dj@NQA*YDh!9P1cNrt-TZ`Zj?^wV#qU+u9GJznb*Ezw4$Wx9<@'
        b'Xe!u#THMrB(qc_<Q7OtRm@(Q2!3il!vs9Tgdc0?3ZSJ>Q-0z$}fAVA_-qXz)1@Fy~HVQ3^)HWPT$X&T73F7Jdp++NSCVG^i580>`'
        b'mU?1swoq3fPs@|9%~e^a-8APEWoO@6|K=ZTM7L#6fZ3g5PJb`w`x~Hz$RKb>uOU8pgf~wUZJ;yXLpg(bE*VHpgGLP2Ij;0iFIo**'
        b'*OQdt`uZM&+W56XrvD25B!8_4fZ(6NyakIP%D0RKc&Rw$GOXZh?nz>fKgMIBmv2^`mY}%{eRO4XTLOuKOM%uiJz#r^V+eE^Sj>$5'
        b'A6Y-?X`xcq=E_KA_J>toHwO<`Dka;ooz3Vm3*NK*^-j(QJ!Vb1Qgg>kbVC?x`Uebzndl~!YjbtxjBele94SdKvDVb}RSFlCVQ@=R'
        b'a@hhgTadsOEOuE_&GI4xm0CKaYZ7+!$gJmX=*xSW{-#14`&b6V={}a_ymuq5NWS)YRi#d-OO$69%5;S)k^qj9NsUDI;VPSTt}Um?'
        b'Yt<U88iO^)U`;ky)1D(<Ctif{Utq94VxY8<2jO|D!9W1_be2RR<>)cc$rT5w>Kk5qG2)kPv5QKe-oEi;AMX2xFwjr6D|{~zId9%D'
        b'YjP?=#V-<OIy2x^Tx=zJc5_jmijQzCrOP77h#kiSq|`;}+S~%e7vCTwa;j=!(BYj4YYy&BjLjNraaSgV<Gy8>-gTqxjO^s8M%-YH'
        b')ieZn)8DHY2V_r5ebroTB}az%_HbA+B_sr~7#6u%rouMu)4zEGn{i%-Mev_C$IGyB@Mmg2PDbA~ukF`Acf+gBIZ}R3+TuR+(S9m9'
        b'qTr{{!&TwCR^ISzy#WJlh|6(1Rds~^H#b;of;ayuMD#03)woZGWnF?_ajAeLpb&Tm;soWL_>N<^<M(*h3douMhH}0&c$OMHYeqTK'
        b'Q+PrK<QySHmLe$(H_gEel!lCVC#qP%r+|mtt^;pP5UWqW!KQyoWMt?cztKWzyz0!R^D@i*)j-Qdw;-9&JtotAS=Fj5X;+ve#GY8p'
        b'Cnhv@j$9<p<@kBF|K!PtcC?Ge9bnlvRHz9AjKDh6M;uoBI!8u}mxFY%)|dsywj9JwFJTMvlVWjSh#+bO<bAPNR0iZ7cQJDN7WJ!#'
        b'w&3CmSm6@fw*tGdGHA!)pn`2&)FN>zhZU|IW2r|h+CZf^$?*9-a;EOBD!Z=4a(2Q+J;M5aupg)br`mG)zQK+2;uJ$_J@gHGq6);#'
        b'y~o>;B!4ZD5#1O`lvh@z@2et-nmj|MQ@j|%V)o8Ew0C!uA}O|#%wX>KAo=`!IK^rDEBaJwd(vLq@o#L4`t_*mNi(Ed)R9qVlV;$)'
        b'%bev9h}0v>`q`S7xTrULGX9Hb1%Uf3SVBI6`G1@NXudw7ukSXfmnexbgYQ;UZ_;rbG$J$JlXMvuf6now`svjF(8GMwqub*(Q;z_Z'
        b'22W{fO--IT(`kyt79?&_8y2X6TjD`1;aJj)fCUQF#)k+2>%sgO_%d-LrvG~nDJiQmO~V$ffD%(9-%J<)F`uFimR{N>(Iv^e?x@2G'
        b'-1i4eX~AOl;Escw{#4J#y)^{FNhRotWXeY$)mXWxXT(<~p?hnp5H}vhVC)==u`HAmCjxKsveaADQ6OqCmW|kgOVFgFlG9grLsLrS'
        b'J;z%dmX(O;*vaWDffr9IGrE`)Jq9Xa2N9s(4N5Vm{S|0)iVg1o@ofH6;#_EvKrQa%wy2-W;`#m>2h6e5_U`}C@cA_mgXgNUK@3)W'
        b'`(I*E^bOC|W^a!lW78flI_oLP^ID?kjh<i0z-q%XCu@Dgbe3C_j|4QILsE9G>sN!~ujtv_^I9TQB*RlyyOudUMLj^qWhvCvecMVZ'
        b'F081^zEE<}nkLp_Yp!om$FI41800(^TZ81@QNmf2B)J{1kzt0<YY&KZ)!X&99#_Up-@BZ_ZQY`tV{orcI*gkPm_D-GK!nApad8@_'
        b'f4&DQAbE7#6Lm~(kD(~RfesipxDmOIB+dZQNw!~P|7<7<GojNJ_0lN}j=7xv_uXU!|M(|e`F8!{9yVi^@`uiz3@)lfyl#?Iz+^FP'
        b'<<^`{+IutV`g%|+G^bzDv;GopQgJTdni`3zlp{4}fQpCw4`f6XQCVIE810oMmcGvnpC8ig+pfIwjUxp78kp!zLeHke)|4V&50^lo'
        b'!PNGU+Om9c7ng;yK+Na25G6EF66HYmI2zn`c;LIjwf~?G>`u;CZg15`LcdK<b4Wexc}P#7QuQbL&>k|`x0C}(75_A8gMoVVoL+{|'
        b'SCPpeWBMn$J=6TWK)cxt%e3t0pIPpXD19SQz3Y$TzJW>RZuk1jxT9~9iR`iO@$zEeTBbE+pyNowdceHY5r+fA_4m4)$sQK8Av#Ga'
        b'vvkazsH?1!xvUBLj_XK#SAg{Wjcgz#(3OP}g!`Y9ATx|`O5i#km2a#XsgdjZx?ihtfhf=BFvGjp6a&6Q4Cv}67qc1bfV1LvIB57e'
        b'v93l1EjSjSnWn$m4eFW5m~T)&<vsh!hw(D+(bWx!=qqF0$?Z+LlKsa#7rUFUcN^j}KOzEpVz{Wc#Um3<(E7$q-|R^i1Vk%Zn_6X2'
        b'cOoAvhIJ?JfZ6&NY)c&uLdv=Ww`g-g;X1Zsht}ib7qLT0xbHbE>G0DxV4iv=^@pyr>P5<PhZhD^{F~RF9S7wNi4b>hOl&0h&q<Zz'
        b'wVvkglvL=r=l^xP`HuV2F<w>0EFh8&$AHS*dld1dt=rER<&vO6n8c4@dT;l(G1F|Mp7y?lAWls|==XPTQ;RiNR^}G%ysYFMpzr>O'
        b'WrZQC|9~y%Mfq2-1?P6mIK1HU4nTE@V;Z}W-2Jh8TbOtT@}1l^=&9*VY>QUGetz=9Ox$svV;tSZMcLx1xr6l6XPo7S8hr)~r?LGN'
        b'{qykql=6BtB4zIbQnqyi8_UKV+c5o>ZZf%Sj1>6-VQl7KXD{Jwm}F&<VQPy>?Yr*7=&MRnv@$}he;(#s{g_{eCP{GL`;#!f{?QeG'
        b'Hld%^4UvLZA#@)SZbIK;mN-T^=C$tT-=KbwGuhAYeM#8AtYU+Xl=i!wGVka2Tb(NRrK-|zMjFxC6zKc-<wy8CP@5Iky|bTcu`UB5'
        b'o|Cpv%WjS9gP<z`g&DZ`8fTcD0`jsNsYs=IC+eH+LEntsWKo&IcOFb@e3y6jlVq4Xxypyue>~H!d#y1sJK}fDc*1k9i=6GfinG#)'
        b'kDRz8a?&%e`y!RWO4BY{lhNc@mL^6o{5*5J$xtZG=8IT>uqOMCaTpWVja<siG#BKLa+tom%Wz3xAkt#<aR<Yh0zlSlUCJ5#xI;Ke'
        b'Mm7f3u2Hr}I0Ta{$W%&qv2_9JEQpnx!!(u3B!C;A&>d5e5t`M?_VUxx+Eobt`w7&yIo(-v{JkSZ7p)7#f8ns63S}(R8Jqyzgt!-('
        b'=nAE;Z$dxZ1=F})A-*}GpMk8De)4*8{!`D1eY;>T>cCjlfHA<bGQceqe+Sq#Ubmf>a1HXB#;y|?b4)E07;@FBkc(D`?MRHz%10j9'
        b'Z?LTG$mhC%s(B)=Lj`|LeGgRAIo_QBDo`WGpb_7CEa?PpdJY5Y7LJ?FPFP|Np=#&5ey#?7roqi^mf>KqJ^#9H*to=3H31E;K^~s('
        b'b!d3)8U>=^W%wJHHHQ4Y-yp*YG#uq===v26p8^e!I<`;nB&<;b3F0DbO(N>&yFBpaUjd&0;1ttVzMpH5OX_$YwXufxJJ(@r@=+Um'
        b'_-g<7Rkin^+T)ImQ*BhCHl9b_bgaeJ9E6q}WfS0rk{RHGdfKi-?O&=MxX$~dM)9)~WX2S?s{!3(KFb6$pnO3U6fAI<0l&e6O_lu-'
        b'${uk%IROT7s-zrB=8BhsgJ>WXF#Dp2sRwUdcUcWYhF)x(xCqbGx^GoLLxS{|@%`QPiwMHtNSQ#fn1LrX>p}gJ>nwVjC^k&!52JB{'
        b'a?fwCW4e8Yjf;H=6P6#!cFpPX2A){IF>;gpPS2uAcdAM`jy1=^L^IZ_Yx|V-iM}`PBere5KGpHxfc%*pGod|b-H%hh3VM*_2t#Eh'
        b'56Yf_vSfz>m8qxN);|qpsgCKW?D+?9%b;wbBXB~0<pGolN}dplCJexO<Ov$mKlK!L{TKHa0!W(a{(Z~^FlykLe)R)<k6w47fl2q>'
        b'xnH3)4Wlt9Bc`g&1=<%mhVDcAbFMcvsJ!`^;+^*~>yy_B{LyUaIa+xMs692AP$FJ(|MLPNO)qJ;QS@~()NEUlqq_d`qU*FKa}zD2'
        b'3o>c2c60!JbalMi(jwY5_d0rSU^RePfcm7}>9Gp%doYbAv?E^LKwqFC@d&TOud2abpa^Y$P4nU8nrQKy`xq5?y^S)o(3ze&*GtDV'
        b'X_H{Zy|yR4bf&IB=Cx%O3qGyb3m!U2>kJ@TkAO!<67*-2X172!f4fdqq95uq5I2>t$dyL9jY?&yxrU>Y*%k<T)4(;(wx~+~4FN9%'
        b'-!>{4d_!HXYOPLad!Mr>%ApXldf9dBC!G)}>vB<~425aQa%)GIZoaBATd2#GuT7L?0}peG0`hU+Y^=6nGT{x=<UNeK&}E==l&=Vj'
        b'(b1)cR_=Y=pceFmLfklC|Ie;AI;TaQNhi$o{Me=XShlmhz%W^Q+wIlS>P!`MEk9HL_pU4&EE;0gXPmF^p4VN<?C#{>6)DdT<{a-b'
        b'XmY#-Ifjk1^sQaR>Zi6zHL}q9U_jv2<TQ77(Hm#BxnCghoegw;Ci4oaDeea!hR)1s>Ox<_*fLE=Iel}NS)F;aKw<qF^y%WHL(+mj'
        b'Pey&<`|=)gVa|8i!0bILGgy}>x6Ad1x}1qD{M80q|J2z?*kTr=Jpd7o*!u=`rfxojw~O_@E*G^J!p;=g{$sklS4%hR^uh~%Zq8Ss'
        b'OS&J^ZGy(rKQ&N`t-tBiJri9zmYt|GQwEk=oV`M3wi;~KrF)Bl^yOVH^;}#2T$gpJ{?A=zYO!uUBBbK1{*5kDWK)~W`6ion36s?c'
        b'Ewa|kq-{a^*P%BlY<`N_nrSt`ur0P(O-r^0>9+u`R9k+k%WBe>pdK&z9&L2+s#9zKCT@@L&7L5LRDEhEAOC}><EBUN>n)vm`O1F@'
        b'lV8Ey`)qD>q-SyjDbiWCFBGBkG%|#>J0}y?iMQX&N$50COUzaiFaTOMTbF|G%*1rss3oiwXhhVp)}@XP<fHzf3mSp>L@KcPXT^h@'
        b'J{!^VQNhDrwGO>t`YWO*0O--_mA|4V_`crMWm9J+ZI%;6ivFQr9yx;Uvs9`}US!V}mJYB~TGI(x_OmLxPUxbNOaB96-NcJ>@%tRe'
        b'I!N{=zhtlKdO7eH$=<|E_RDcok_}@7!i^-`ns|{)1o^(ONeG%5gu${!o}=z^78Hi19teOisIsy|c|xIN6?wVzk&bxH!T^5b&!!|*'
        b'c5;=DM#r`u!RhxuRB7xV(qRQ#C!^MhAH8SEm_`M3B?l)}iwImtES^hE?=rmqVV*g4{txPy^@X_aF-*^O5`>;G&Z9lcV|UB-;x3Tx'
        b'B{tmgI7W%O=zP6Z&_%~&26W**BbF1<MJlq*GRu4sa@z7Dv=-a@A8xe$5QCfMW41=gMq0IEd$y{?QcQv~w{k-ub-R;PXl*ex4Ph)L'
        b'=u)X=q~aT+nMzoQuY7eH)!#{m(lk!DeF@5hBG6n=#mIEDN_jCb=XxitSyZ7AfBDc2{Pzj3ISSE)QI3sL-*)QjItYC3FXMCYUb3wa'
        b'f^;8ez@wBaM)f`Z!HXx1a~)^Uw+@OC(<q9g=uF$uPuB8t6F><(vErcq>d(N5l&{nGG55mv*`Q|gGku?Mq{4Is>KzKkP1Td2e@n0H'
        b'cnwT_+)2~oLOPhG=Cp^I{(O(tifCHi9_)DM9`s%RLFd<fxT6lE)d^;5PE0T^-j8W>&B5Z>9^B`;2lANoJ?@xwZ%Yp@c3}iDNB>I4'
        b'Fa3Gxo&pa*|7AEP7}o~t-JOIn0EWhV^bda0sCPiH=FoHkT_m8YJ3(K&4~o3jbmh1j+Di^CRA>o2#p>;(@hGq^7Bj{ab!La5Zc=Z-'
        b'be=;PQ?#pST0j_ul(Tcezlwr^H!GF6<1K8)7%sj$?xmA7+hL}d7TzcDB<lH&WSjC86-@`gTm|iqwtGd81dQ7p0_4wP_>9`pnd9jM'
        b'ECBA;elX~SF_k*dse-H(7?CjJRSiomAjN=SeOLtTHtIKY#)6;p4z{BO7nfkP`|;Rh-1mD7s>Z$&P1!n=gA4Pc^tqh`o@!8MW2$}0'
        b'E0SD6fQs7DsmcXqmH<LS<#i_gfcx4o8b30_HXS$<rPk(Y4YAw74&Kvecjheaq=_`MD1lUF)2*aPWvPN{b3|*O5dlBpX)7%NqovAK'
        b'0m7B9J`1c4D8?Nv7?sgU=RZoNbuQ2((<`fR-+3(Quek3RSR5T>#i!tp9+m$MqmnxHvpebFM+}N+GE@i60C%dI)B+$@PjrB8Mc*`A'
        b'6R0_z$#`Lg8aNd&hC2?7=iIr5e1OoY(HD=5=QMTrIY`l+UU%Jbw!x#(Jq8rJ-o+~S$dqwQS$v&Rk_m2#h0qtIOh&!yOBqMIvVsXb'
        b'fXE0iZ9#54tr39anMycXLnv(+iO0<^uu5#y9IZtQfEZyCieCg@evY#KKiY6QKf&<=nj?@u_+7H1{VYflArgY5I5tB$)JwJ`D+nUM'
        b'G0st%&g@`b$p&NUv%cTM^Chp~4hN_2?=Yy7FycInypILs3uyPEy)C$}oGVsmQnNZ^cYu#OP7se||5b&l`WwZye+oSe&zE9736lw*'
        b'`U1ug^Kav(mE+X=*9hWK{+$(KjIVwi>SWidi1eolDnbdtQ&9h~0rxe7E`QW^NdQ^1DVjEEY|!e_i56cQSpMvfk;%__wxcC~nSbtx'
        b'i#Swrw__!X`xcJp{MeCgldaq%?TMaTAoSh*2{>m~FZnPRcf2#PUqlc|`ig7(+?<W(=AMaw;syFs9n_BhBF@2%lR;j$0BEaae??n4'
        b'qRo6sKnBx`qoIsmtf7u{z}WA|k0<a)$RJGD-}IiU;18jP6LHfYCd~Abicr(*6Y$J%k?&DPG@YT*|D_}6A00rp=^q^M&dhffNCR{*'
        b'Ctm)dgU(+DPi>2%H~ITGmmk--3x+_<U_4@aoWpXS<q3WuW+uycj<RElBTKjixhoZ07rcpNIvQIrf29H!FXwWe`dKn(8}K!ovFW}5'
        b'%n<yD`F#$_r}>f69{3dt`7#fNjG6fnG8Fw9*N7j3SoU!qfnuB#p?xdJAlp~S0UA8ODZkGAh)>7q=lw6ZO)KQKMh-y55OC`szBUyT'
        b'U&qB7POtr6;A;W=Jp^v*<46%{Iv_Gz7m^XDMWy%GZdL^qu3rIqDMNu%7paAqVD^C^Y~R_+18B#c%ert^$Th-9WrzF6Sl%8go;g8f'
        b'bf8_6>r4?S7FDKUt3BCkbkN-c61wgFbCRGfmM!BI;oxWKlRIE^GuBc6(_yBu(%adz4)pt!p4N95@O73~rc-m_Pn1OwOwEBmvn<C#'
        b'KrQSjc$ta=VF)Z#<EC7!FcEiHu|mZfz3iGnEk^GX#z9g(x{jO7n10|pFyjy8P_DoF9nX=b*y~{4QwgJvngK>pM+vTJi$O)Bm+J8X'
        b'ut)Dt=w%%_K}dF{NSf9G>eq{FDejuV4JtDP6pNc~1!V;!>C~$1$Ast*g2`*yW;u8xyo-{cES5LxJ8EmDS^8xKw<pLF$IPG5I!H%P'
        b'%Y@guQ2ZGOd~}@U$P5S>SbXNL-fPbho8Jr#N=#ZgO@U_+I8||+H?kSPKF7x#){!sYSEv?;s^k%Bd?rRM!|-tj`a)fQ@H?B}Q|MhW'
        b'F%zQ76{^i|h65UlJn8G{%n*!xhTo9+QSoOPLM#>l_O^l32LKb&9@z6V@gWYQK}otsG&d&_o^g!aMUxwB%d5EQG`HlHAYdK!1q{B<'
        b'ae|{hzDCp8S~G^97msuLqu=G_w}(0o|73<C=)p~iKOy#(efQuUI__IJp?$^lE|+us8r66WTp}ATHHc=_iPk3S?7tO)d|Q`a)9HjN'
        b'aL$X++di8$A!gr}H9k<=>-XW}k1$KVUYkoQ&26{7C9?m$-SWDQZtGIzS6Ob%jp~Yxkinz`xQk#GqhceFzeb<$CTq!kEoauKYO8we'
        b')0FWymFjt<(fZakl^OUnBdB=GrD+|-a`sFfA)f!*R$>VjMB9A#eF>ONvqX6)0NQRJi!#RU!A&nChbHzmE`Dh;$9e5#=)ER$3yX_?'
        b'x=V;2&3XE}pH+op`A=!?aZT|5$J)DxHFc$n!~2#HlCAC#2#9F+-XUBfYO<pOR@)?CMASBk1ut#SAs}d5dj`>p)7ohgI}t6;K%9=3'
        b'+A|@RdTFVc&a}3cGk`6kf&z-5f>K+iJ-v-}wA!fTd)E%yne#i}Ki}_r9-gq*+H1dSt#`fmb<2#LLQMa~?_alaM*If=V?I`<Cfep<'
        b'DJg{X>7P?8<lZNL2Iyc%Ec==E?F&}apShQG&g(;XH!Qy#&?pLZnAh<$Ae!eT)y4Il_nunUw)OUq9Ne6??{6DQuh_R<c|fa%;w!~_'
        b'*`<qVVr3lBwg>ZYQ-L(-_%{i~(xM&PZK>PYbcT0Mdp=q%BoDXWOS;ikd7D2OMi$9(jB{M!i8O?)0Lz<~4nGh0I>*tM`5xRsWT}6P'
        b'^Y~J}HN+OJ`)MYfS`a<_>Al&ndRIbQx!f!CJRd*LnRz8Ce_Pc0s%eTPOBVA$$3sh$`*tM*Zi6jL87xsHeSG<o;(rbNl5;UdC14xK'
        b'vaKWB+Ol-{Q>wWbTKUIKxa{Di9dT`{pCjvsk0f?X@E*V0>Q4x?nA~3uqQyEXSAf(~U(k?57MN{n55^g<h}5RDvsXxSER2tH{*@xp'
        b'0JTrJLI)k%d8x0<gDnibRa-Phy}XT6U!mt#K)a)_1djhiAAM7@eoK*}V9DZtD~pdA`mM6H#RTlLwVKSstPBiE*^Y-)(rD-nyo>av'
        b'r^U2&8+s&i;1^`?hdai@OO)N&)55s6xkwonc}XtBM*CVD{z><b2zY=k)mXm*p6pPy_1~kdFH6^N=8^p6Rg$qJF$2Mt<cKvyP==V;'
        b'@!4JLtMCm;Jl-Z=%EEI~%Rqb133H!crmY}P?B_1eUiPvS0G*8^B{P8c;T!l8#PE)hHY0qqBk?<ESM>&X%V6@hpTZi+<0LVb#pD`^'
        b'27cRq20e26a@Jz?+KXk|3G1rxaQ(eSg!kK9DB$g!DqVpD2{+AGlHhYb{Csq=Q?N!+$nKd6)ZK<r&i60V@jIn8rOidD=v*q^`S3s-'
        b'NSEpu>m8DJPDOM`cz+D@WK~BDUy{HDFAID|nQD?iyc<;leb44z9K0_*qP72dFXIo^4yYVFH=Xtao@kqmY_GJ%5kF$fZ7y)x!GYkM'
        b'&aEDFIH&z0cV4(--*cIlRH=LH0t&epiw}(;3B!UvYGPB^;zRdP%!Ox)xoIfo!izDNLx^%bTvj9G2rPd{1414JVnmM>UO_P*_b}*O'
        b'@xwXg*{GO@GZ(QGXx1Vg1!A1Pz6?gJi=}Llq<s*QKJHO?F6OdL=}K0E>T;G}*58LI_zB*=3hGk#OmUW6&QhnS2yZ>6{oOr!y0;p2'
        b'KX5xWj_~e6ov+YH_*Ce<H2*eN0@#zKsG>?=yO;5n)N>0Y*T(uKWK`+adl|XX-`w&5uWV2PuW-vR|6(Ify#pqKwfz=Xbvd<)kha~j'
        b'+b=tl1{X_a+N>dyL@X13TO$!ng!mkL+bA)bNby;D+eA#J)ii;noQ3gKNetC7-o!g5d@^KI$F#-YVaex^JdC?@e3gvX&ilYZcw_E>'
        b'yHOG)C1q4m#IRa)uOuo8lZwyz_fYr78|z9hqq{6r=6sELfziA$$NczW^CEY=$oKz#*{-|17+;iwKW@YqYVZXrJl|0)vGbR?WtT~b'
        b'Ww8Y#Ew~9^U~d`(m(V`xvZFZKKH)N>3^^o8Dhr{pkVXroegUsdy=;3XRHW1u@wy_T?!haLxy%!j)B?ffUaouevWg&VI<(#k3aAKD'
        b'd>~Z>B|cD5B})y|W&7<x6{*lj7IImaStalg%W`rRX+r8+GMxqfwMZEjoDQ8PXJ({344#kl#JQQ!7o;jAx}atzTDN**0J;giJ3w&X'
        b'4<d`EL=L*t&Rqs0Hog9MiGurj5DZ^#B6Li_C0*WJBC~%nNJ^%H*9)Go34d-q6XoC))p2bd3NH4tegD9+3bZpxk-ApFT^K|}F!nNO'
        b'k#Oe+<JZc-0X4`klQ}XJii^G+aiw@J2N)D=O|Em0CP`u%w_`wfz*P)k)rGx{cLdOg{~)Ych}s<Z!6j!2>kN3_Z+~q-IF^i7)XrR{'
        b'5%2?!GTr^Oql6IrxKOy%@WMdEZV||dnNq^qddm<T1WWLEDPc{<==h3~d8sdC+ZzVmO@o3YiIil49n+Ch`_3R(o*v0WhS3T5!8N-F'
        b')p=3EF+BoaNk$PEE;qbBNajqo|L354`yf3J3i%`xRkF$D``GnclN6Peg-TMAL*}Jds!BDo889~R>}f|*6&h*x4kA!9pwD8E*-=_}'
        b'Z}y6|hMxq@yuxEY)fe1Lnr=P#69~cAHlh7)1)gII#Uo=hGK`dv!Z8+vCxVcvAu)KAUJ7ICpMQ>21d>+zCCJqcgU&|O*CKGqOY)X3'
        b'7WO`p8JD=k_^hy3m-#y3wP3>D>G04t6%zs%Ghbg}cn%ehze!kgF>d+*xH95MAogmTc8e#I4C@BLjO(!2O9n+lM8`cbX!y55d(|Lm'
        b'N&m%|eQeOMeNZUYS-}a}>p(T6VoQvIus1I=&Sr27&YqFBc!`g&mJ+FdA-uoAlIB9n8-qj2nu?Xdn}ZlFmA*OxpFfouClU6(nE85}'
        b'@a|i)X3+7pRKIdlk$#<X#-Lz5ELa;6*w^DkPgqb%Gru6(9=c_iI!H^4a~hqQgF;GP)Y@4bHlUHtv<V@-C}N~{f8w-*8jFtmcmM@L'
        b'%JMK}BF7Fwb5)k~Ob~s&VYC{u(R((m=0~i%U?|j%>((7VB@Lst{)EleE{P%9dc$d(3W-Aw{8Qe4cL@Omdy89!keEiWGnh;$vGpg9'
        b'a#b-m3$(z-ZyS#=Ai3GeXuTQefk>EAl*s?TDTA8>|Dp^|U;5vb!S@3XlmTdh9mQk0j6t5qB8~Pw{S)`~z-*})jhmT6WUiDD(l7BM'
        b'CZw_$ielkcC{%6ah6Z?Ig*t$9g9A`ZMNHBVnV1qh=!aMgWY$d5lF9WA7*3(L_Bh~{NgxEsoQFUHMA%>I4GVRzWWsny5vlK^Mesu1'
        b'Z;JgG!W%Uryyu$5)A68$EBsh_%{tKPKBv$TW8HtpaCe}tb|8t?zt6fqL2^vJbt?DCfc^YHE5PnxI+EJLIMmAh`jUg6zvs7@ZFd=r'
        b'={3AeOIUxzJ6_;<537~%IkUMJFWKK4xG!*`cye|}Oq=Itu<8uc2O?obv<$)M1(&_f1x=M+#)Ud}F_#0+-t%E=K^Wvq;ZNs^Q3T&u'
        b'?3@b2?f7N5ZF)-oFk8b?4$cU}%_|#?DCFef1RG0j{L2uJu6KcqjW58Mb=^;`z6mxD3~TfK49B4>0HaY%I=C#z;SW6ugbP5x?{|s$'
        b'9`0dOvH^tw%F~oSZVrsK;~f<K2EKFvorq=!w8*}Cz-Cn15V1XKpL<E9t87S`vXu6+0U#=<OMky=0SpBf#jO}n=RGGH>0HI3rg9J|'
        b'77h%;Jr-{Bfc@!#4aCOl<-ES){%qKqr2~%CJcl#4I!=1~UXaUe_3HyIjK}$y`_W4<VD`BK^mtzKZEHiAHw%1RvWI(&w<mBnE(M5>'
        b'crMqUzNsd_@Je<0$I51&Y2?`;koZAm<XlDGu2yF~$9V>_pjthz7r;jbV@4<*#_uIj(x+~MftUls!DSAJ*86lcMk!d^_&YqlzXCr1'
        b'x&iI|)zo3}Cd`O-0I&2g+L5~!KijtOCR+Gsv|bBysRL0r326!z;AhrPmVlFFz48-K6{i12C|+2o!MwL`BW-r@(x^7W_d6#HI9g{9'
        b'6)0_mt~Fx@gjT&uLV=ui;0I=9g0S~|rWZb&4H+QJXU*JNnL|>TJyDRZKsqHiQGJ%FXiY*lCal*)5fz__k7cBkV1y9EgcuTNG`9X9'
        b'cQaz8nww~|v<ezx{aiH8b<XySHfabWP=s1)z(!|BiXP046g>ySY;=`VK!=se#xkb7jNN#orW_2^X;6<#%&2kQ-!8YFajgV8&8j$*'
        b'T2#pZ91jp$nbK9s6jdTQgbo9#1PYo{{*1C{CF^RYD&7hEfXX_Q<z>v8vzM9yS~F!6lR#)|-nj@lXwIdKF|{k#bX;m~V{3{ieVMYn'
        b'gDL7@TkWfwn{PC?nrU@WhrYR)YIPc&$1hc+<fYysq%ULkYnKj>T(VU%b-qg#WqC>TsJ-^drHCN|297%M2ZuDNy4Qa45-H7!s3_8!'
        b'<#b=P%?$1N!tnkj9?;7xbs7ypL^MGWA0o*tmIaF`i+ksityH%b4441BXiC=EJRw)Su1FeUqVhql>X9Wmp1XYMzF{lZUb>r+>}|e*'
        b'4j3oV;@JmABp8$>=KSH=GfVJ%upPnhVpHU#`7u)<RR8cy5`WD9F<T_Aw{`n2Lh~bQm5Vu3@X$!(Uy#=TN&@7xN0b`(m4xHa9dUkZ'
        b'+K|Y-V$PKadxOpZxge^IRA2>Qa)&sdYeTByVN|jq3}Xe!@|j3&fLs89QzSAu44Qov(i7;OIwYwc1?2%rlU8Ye<RYjI$hQ|=if9h~'
        b'{i;E2*b+lv8%I!|dX*?rh73<$(vVpqW@Ug`$N{us+K`D`?)F{+2C-#@^t=wELVT;<hUZ7d!U9hJ0X?RJJd|N1b8yh!;Of0QLdPRU'
        b'-CXD61hmn$vaWmsyJK@y>9M;R)1}2XJm>KW8S6Xr`<hCoB9E<*CKX1>3rX6LeaZ2e9{6ziVp4(wT#QN->rxRoSjS9UV#F@4=Vziu'
        b'$wQ-616`oD+)qJi7&JzyV`K8solg&;p@Uw7kIX%NDNvGS<KcOf=d3+pZqX&k!9>Ec#)Y|pOTTR40H!<{mWr!w>C7HZs5l<3e0r?='
        b'A)r*_Xza{t1mC?dex&Vm*dV(^&jc+2zV%WCNg7ooi%R4eg=2RM3rD2K5u80GZswAaFlYz?K``nVUT3rzG!}vT`J#hZ(Ge&8yG%nE'
        b'KsCb~74eY9g37`(6j7JFT8mxcez+)xSanRSj<n2FSu(BBBWat!$MW8NVAZtUxWOe~T1ud4dMyKvp|#+K^W6(1X|Smy{;xtq3TRU_'
        b'_+jtg;x1eS%VCev{q@EBK|uov)uIQ1>w%Xm_LPv3W?`sV|MLFiMaQ8tplAdF(W78ty&LZ#ac;eH4{XBFJ*2u*C01qxJ)}saV@JT}'
        b'w@U6};Ep?-!t)Z4`_f4x7zW})ngstr1FX4q5oxUAJg;K}%ZhrQupB#OdS-i(X<hX?y${Xh7H01;zk4yMI{0aBpe5E_dI4>clVk`~'
        b'E^nTSPQaD%$!b1E$|h5SQtdeON=-yRYLG7C{^Md3#kR7b;Odj8>clqohHwtIB%7A1<`a3EEaS46`Fyq@op1x=k$syROr4i9L8iWg'
        b'^QV6LiJzf3O2^Seqjpmh!L7d#XfdVvh6qd=1#Q>bxQYw=3(_jY@Kp61b!``uX!jh{JP(&~YgIP)n~M(qu|1zHjIVq>1C&z_KM(VN'
        b')5<Rj@^ibo*7^N6thXqPd-h_0w^tu@=q9;KM1fOm=cZktWey^Nj#m`CDYNa^^mMe3n=(aKle(QPU^c%_NY`U&%aWp@*EKw|*+;ak'
        b'!?==*`yHUfhq1fm2lb${gWOcVf1MBiG~l%Gr$!oNHT$-+8@8A4W_->^D!3_kqtl{THnuD#otqC$z)J7k@o^TAGJeqQv((6t;ie%I'
        b'V<x57Z3kx%zJZd4M=tXGTnCrVm&{D>R=*(eaMO@B(^HM_D?OY=ICMpy4MGoDy1_$#^^10uk9!1}Rxmc{O4sPvtU7*mLW9IzaUrt7'
        b'm_Yvzd|v%*lf*qJjxm>E*IZmuEafsTrWL2hak`5FHw8S=Dit|bpOQedX|OB@tw3}9nl}~f&h0hqx(@*t(=q*Pn_T*JA8sew3@A+E'
        b'L1Cf*ejqJIXl1gq4)}&2zk9#~!UT{C@+2!8Nt6PTq*M}u8|(*v!$yQK{5g^&*E3qqesMn;5f(^I91gkZ3*sK*h`2%G1Eds3UL-Bq'
        b'9DdP*+L*19Q5X&;K`E*t8jC6>q#B$HUGRx-$@!F(M;B3RSb>`cs9;klcE%>~ucdE?9nMD_PRq*@>04pm`3Mh>gtab=`oU{Rbp^)z'
        b'v2^3`4rye%Q5rEZxM`rLSUq6;3XB2hDded<{J)HWLmY$q{IP0DF*20}<tiRU#*ktBKEv85v|NLwM5`DKlg0ux)w}V1WP27c0w(~z'
        b'AOlq4#<gG=>&4f?p}%|XTgLZuuDC?YSX|Iy5p(`}AI2ko5k`$hDI9tQmDjQkbZg4P|EwP)$`NVCEMzoClp{b8O>J|Ls0zW(w*TpZ'
        b'ZPd<w)V`r#bgPhNG^Hu+yDmUSYyMR^vickD9T)7y{VTs99BJ9hYDw8Fd({QZzuTwH+&6yd;aB<trI~<<!c!D*ly>Z0V5iv^suKLm'
        b'*&RCxZx>cOzrQYU!ISRsS260_2Di1}leS2`U!ceIICI>Veza+_eMS$LLr-XI(l<7)iyR%};AZcs_i?iqCfF-4>^MS5yRi>05N(&R'
        b'*~3e+32&b`*K(6+OT+BHy0A1Zr4*UC_9y$HFNOb*9r@hRlGV6)dy~Ze^o4*nv!1$ZfAYcsiMCR@|8sRdR=?qH_UDGe3;QL4#<p~M'
        b'*5b^#Ck^xa1x>cvNB~(n#5*y80)=R7iArg&xBzm>R>j(%xZrVS2y@>x#P-)&FE})d)N_R)309qG?Y)k6@3M&A-GAvv`_Tee=59iI'
        b'92<W0E;KgtCOUrHkPDEe1j%=yh7aSk{R!>0`<H6#$5elVDkI-rx@>8jFjpqbj~uiDQYqjx+lTtyh6_U6IJAGWV4Q#)Go#){ZTvzn'
        b'Fg9?HI1`Y<#@=i92X5nE?z>CE(0zAl;|pE)U$4FiCQ!4O0y7LnQo#VTp{Y3m7y`_Go(1SYf&K#c7;%FQm3al8YnCZ(4v=<PU^@d3'
        b'@gn)L;-VzJAq)@5pPvCOngjM2^6NyGe$@Tr9<32wdY70)hFM>qCt{d|`hoUb|4Mrw7OS~0`*@zI?g8Yq*Y=MOMq~Szfex`>@8`KG'
        b'hQIaqXl;DSw1pL^ZxYf?SYHsW$X!^RI+2jNF`D3=6S>;{EK8b0a8BTzN!-PLo>x{Er^WC*2`}r;_xE&u2yPU}i7w5iR-K;hVS_EJ'
        b'>nmdl^ONe+?>;r%8~XA8LS(S)jY<$_9U~xs1TD}SPUc|4k4XbsNz3p0R$i5G&Hb%>Hlhd_R=;+Pw`HX6rM~?yrsOMp>DlV>ogQb7'
        b'b!NChQo8$&yROfZmaRTQ1h^?aIo2TYITxTiU?9aU@F=hy3Ch|N{jFR^O$S?hu)o!r;hF!gHsP){C5#C3MMRQq>ERw=sjSTtAKE-;'
        b'-om`i6A9~-a8R4?=*2O`$$&&_Y7A*ls-$V*`tx_ZDM(&=B5!3U-OfIGf@lg&re#nRJ94)4gvvTG?CHgOw3)5ic|n;rAWN=4sj?eE'
        b'DyZs?_PL)z)mmf27#-)x|4Ps>b(#Iaw-9rcUXVy<gfYYFzN`}U*-jsqvH8CV$T7UszjS*FSZ6{Qt)t8BLrVg7F*a4m=gbhpj0#M@'
        b'+rF}2D9y5_hYe-@S!C8?>7DRG4^V-3F22wweFYkh4iPAcF+AN5P|{SSnJSBsgSO6)*hJ5p*Gx;ImpYmVFqD?nxfA=u^8_&799vlV'
        b'G?a^wJ1WR!%&Umy3i|_usZ@DKy%iG(6F0A4uw)pl{q~>xcrpWo0~lC9Mf_ZL$p#a*03->}SiC-qV$-Np)p+3D3NgY_E|La1%(Gxz'
        b'gQ7G~!kPL5F;h7}m^~rjNJgs&he-RZezdTLSMkbKK5mu}@u-3fxVhyoA!Py{Rq)U~6o{#0*h<hhE;K`fl#M=;v9?AG#6(i7{{jC&'
        b'-GBlGjRP4#!~g`izVUt$V0M>i&Oj28GRk=c{ANf3L9?ldH!DPDFGm6a`C=8KF9yj-2(Lo)#eAZ!fnKhWAmtL__i|C)tQj~TQ8(qH'
        b'x><9t?}550zt8f=uRh94nCh7NBq{fEpTN!aaP!3FUREEM=iufG#j^}o&U=cjg2w7A&UO?}b1z3D#|FhSxk$9I>DxZE2uc#*XO{k&'
        b'L|UR$&i$<q^yS4qp_l~w%OheG^!G=MOVr;Hghm2eqx$<7d`2?v<5NrlJ`4T{p9TMl&ryYbAD;yxJ`320?ncP`zfs?Z`hHR0Rp<Xj'
        b'eIMxipX%E=JEFn&m2ijO?yK9~$17H3(0slvcxqMP<P+|v&!aQibndl%5gT%4v4Y#v=OB`}-}gBzGI1G+n%mLWgMUgA`j)Ofta0~#'
        b'A0pAkcYx$ST*V!(>8pFSFKJ=$RNBdd?)eBFI<e#5`ywZH)T7R4WIm(dya0A0_acCehKjx_R&ky_daHw&#JvD{a<`*T)cF}}Humi('
        b'l{r!qxL@@-idAV*4u2X7RqsGyb?G;l!=D7nwkaqHMnIVlZD+Ors;{=BFReh3RJC$bX@%$Ap{*V|UYNhGK_PUE3@Tjvw(I*grAK#d'
        b'Wj@?VfIVp_>1$1o$s(KEsq7!Y6<Qr?9#Hy?Oc#n2s(b3(sZE4;0Qc1WX0t$86Ud~m!E^AgCsL0PRv(UPokc|A{c8whM=v9|$NRE='
        b'%qF;-=XnDEuEN9RRwqcGBkg&8-0VKV-#&{MdU1!=v_Z9uSPITmMKSIuCb9*<#;vP_^h44xr_bRp<~5I@{uPsG-Fb}6;kPV_A-so3'
        b'?bMhDEA9haT3^>e_^(Zh=}2tjZ-7%o(?Q+D*ACXtzr&;D>2pa!(L<DrKGa0-p}Qc*wec}i<m!v>HOcE{_6<LN$33BsB$BISWR8Bx'
        b'Dv3iYb(G+nR~hZ<KF@pMEOe?|wxm9rK}W}Yi^kOu*BA7=mTs?G(r1wMCD9)T9VL{zqZfriqx-TXOV%d2hkC`&42r%WpXyLe4e%+3'
        b'd*>aClZSt%?BVlSl6h+%a$|jwLU><*G#PH559DMRntFpObnMIU;Sl5qB&Gg>Jp5>1UHE*fKi2&|s>JZk`3EPx)PF}8ZpDH;I_jnV'
        b'BF%ky-q6t7$}>Hxq9CCU@Jem$819Sn0+*3SM3zQMUmg+H=b&h!%|&he)*(g{U9Taoig11v(5jKGLdFyDU6p7&0pC@LC0;;L?J5RR'
        b'U_3=a+Nk_A$cRL>#Sbiv;s?lJ0@Ft{4I&=_+xx&Y5KkEesT$xO2FZg$kp)T@&wxe>f+St83^auOkaVztcfyS<)hcqnzksPbd>$l7'
        b'vnWhaa%(Rnd$>p8IlyI`rXZQ(w^4Nm&g%=5ei7h82?}lTOkvFS4N-Jrd3mhk_&u9$lS8S70^s-8yw0$@Sf5>;l1WIdBRu&x*DeO#'
        b'{QzAM^V>`#4*w)H!{x*Te@bQyS|7)4IS<6F=UrLE(ip)RpT(yM4rhYk9M3xwgDp?dyR}&g=>+h>{AFlvA&8|KpA`I0q4}7&u>G&+'
        b'c|Q&Y{_uo5hV|z+NQAREpOaA)_v>Q-c!PH7jKgi`fBnU>e{4CML^lxbN>M<?(-QxZ?G7N5>Ag*apjk+NyrYC@!^7yV6~SMQ>ZyZ='
        b'7oigC-4QV00)9pPbVZ<Lb!pt4!-s)}7<hJ<h|uD=rRQnVkCvoO;Ct{2E@@e-gPREI{MS7~tA3e==O%e~V0`L4I!b6Aq2sni>3@rS'
        b'<jU;|zV$osJu9~p-m4=4d@1y|G+klHJ<sDy9b_z8YcK$&UVH_Yz#mI+lt?Q|q8!|KflFM*XA8p=({^sePWJlnPr;(%B@-QzNo+cU'
        b'mI)irdnD0&`u7Agi^r>?a!APx<Pu|JD*A9fDwqB(vRUTkf>}bx!J~tlisCh^&#Pa+f-Ot~p?!jI5V`95nBygcbUs!OZVi_J4H2A4'
        b'P`Sf70ky(8Ng#3^&WV{NFS?&OAK)grj<6nQe*J$<H+*{z+;W>H#A0ZH0E&O<F~ivN;J^noGf49!l{sJg$#lc#|Fal_$u;;S!;<qX'
        b'n`kqNvyu$q)u2<Z3@6U1$Yh2=x6Gq+toKYeyw@8jnNoU?I((+L?rd-APvfBNXpHiR`Zpy!k(*hZ$Q?bW!V^I*VYtrZM<15%oX+`s'
        b'1I1H@-=+??^wxdWJA8dy-B-Pl4)XqXR_9tqWXJr1=hA6+(6Yf7M^H1oooLyg{yemfCB^XNg)oC9di%m+<xka{h_-K$naiE+6{Yn5'
        b'8(kli&JS~cI2R0HJim}V$`mfZMY7uH{^T4o!&^22(Ur;+b~P{v1|(kpeTe(7-U=-SL<R)jx<Lyhwgr(`+KgXo(v5BQ5wsiDh$arF'
        b';;BZv;1>{&JwKw77|3WL(856bRT814s`qNkYSOGBqm4Z$H=@kwN&b&n(wt06Ok(mO(ma8bnBkc;C)NF}SG$dnJ~@I_)a4uOy_KL('
        b'=HeA~3o3yJ3r2X=xO%T7sGSZK3~#*SpT!O=H~eRB%ddK`Y79M^>4(qv!W*q4YmU5uNV3#tlBq!N^G1e0Q~uMQug$%YJzv^CD?1XU'
        b'p6dessRjR3uc7pf6bRF&NY_yuOc0ZSYUJ5+BW?;(Xny!8UU#s!G03+1vEj=h&fVK75At*AiGjKWrB_2%>hBnu-jA7x=24e|2Ynmy'
        b'b{Y;z@SV~0ehkr;Jc8!Rp)XVLtU9i=H%nDP<YgJJ$0YMS4Bb?E5_sNhIyLka8`z5v$~rWI#1vBCa%sutXZ7|my#fD<BL#vM#VcB!'
        b'3woT3t~wW92S)fk2;2o8?y>7!{#9;a54Y%P+SSf_4q>j}Gp=`)Lse|+d*SAG#^1qu8p7obN>>Ntf0wP-lJ1<|y2pBh;AY6PgR7<-'
        b'-r0MV(|v?r*UdY;sdvAuJE6B#oHZoP(Zk&YR1w&lcSN>t0^$AfUPWHsK-B)arl`_a=#CeI+|&RkFMXc&1h9&|xT}&aFTb%lDz<iV'
        b'FDM7k_~dfX0HPY<mnCmrndZK5t~R+>SVe)taaAb!@yUVrkPazFX9On~f_zAmG?2q?ikr|Ih)I^7!_cw`Ai4L#!rtlDcfx3CgAc85'
        b'O*KXVUfbSA>-6_Nh4Sj*<%`|`;*PZOWqbzjH-R$cdd`B0#1jc+yh0_hkkQl80dy~&tw~i@;IZZ9E5LWCFvr%-?FA02mlNFGa{_Pg'
        b'IE(h_jGT?^*JykHUWEo9_AC9F%^pAQ@MHR=o0u6&Fe>dg&)SxvaDu~`u`iym9=HbvO%}oZbWSLKtgZfD-L&3vBRJ^{Gy*)}dWrz|'
        b'S4g+3&;IPt;Pr1P{WF^N72DBHnX6~Z%PFQ(sn2H0MI&Gzc$Kf;GxVS1ow<U>?$BU{p>vLs$D}p)KmhcdON%Mv)jS?69C9J^*&GW3'
        b'cOj{d_>0JCn9Y_`DD;Q68<khE8_$A`e{IxfGKzi}irH1(kNZ{r689VR!+r_-je1@8!+w=w*st<_*st<_*bn(?S)-9Z_~ieCAGY`0'
        b'|MbINJo_(x*c<2m*$=btITvxoNJ*BUU6@)-==DX{IbHYX=UU3n)txz)jhlu-XlQTXQVZZMBCQxse)z&U&=aJ2swn`j`U3a1v*L{A'
        b'RNJhOiIl@A9qvB2DcXnxnMBxRHef88OXOP^DDU<}3L8*ijeHY66%@?j&(1Lka*a7zBN5kznHMlhIj9qNB`S<2Bojj{Cnxd8R1)*y'
        b'kI!k$6EwI1+JF&qkntEMM>CVFQDJ}vkQtR6Bxz6U#ug(qHK~cP{&{40#;7a=xi~!ePIaR6i|++I)^W&%R;Qa|!8u5hh`U79f-=Do'
        b'!0LW?&NfPb3H1Yb15rOrw1w}M8YG5S&v7@;1~nLh7Bfzp3edb~zCWCBj=ey2l8{@vl#u=-3}$F9O*ouW=SV6z{nLc^@1O~|dp+QP'
        b'@G-l6y*QgpmGk;$(dk3H7CjrJm)b(PZ}pIpnSr!<AW8tkL1#Y3elsM;f?U4;kyw488IbIMX;a1g*&t#vV`8B&pEe(y0CZ+{&N=tb'
        b'XT=GZSw3#IL!{z###K%MA%pjejND$JWgDVI0nzebfQ*L343v5y;s8fd4{TsD#dFiZ0cLF!4-Rkv&@5wvOmKj0K!%U_#T=kwG4mC8'
        b'Mlr-CD0l{h3?z)ABBIZXj*?9mpOJ?=$HSRz&0+wt139$zYiFBzG(m5RBv14-qZJ>Iieb)d(+OpBtLPzreHJbH=wR3mmP<Y-nn$hn'
        b'RrPfQPs|QDb30<Zf4IxN)zd&m?s%%Zch>zr!b{ul?)tdgl<|aj_ua#9pRIf6Z0YK8-W|wwvT*1aF3<gWZId{!?dqa}hwcI2UmHXd'
        b'+m=Ijx_Goyzy#00{vAqFIiQH$xDGP9DwV5mfJiPXqMFN;kWs|5#Uj><Y-q(4V68~B+Fd5mZOBDEG@<T264{sM03k3RK4fhsF=miE'
        b'IwcM{!21?JTp<Dr5G=s{HB`|ql&s-d^WL){3edBkvH-FUf_uP{<V@3BO7n&uhh{Fk!c5;lrpa{UcyVq6HEa)kcaeLlCusql$nzHW'
        b'-w<-%)fu*)P1mK7mgU&8#E#+vq?JHN_+?oNH-!&a0-W9&_dWL142M%My&LY)%%hXKy4E#G8YpWta=i9`u3nA;0$Tizd(&CNhO=q6'
        b')Ax4taOr2!^(rw`CAh%;@3i-*{d;+TNopcteH7zLdo288)t?SgXn)yW3)HdWJIuq!tG^!cakF^kDhrC@)C^ILK|qjk=qPLIqBdTJ'
        b'@fbo!qX}I{Ss<W|K^O~kmFQ8nrkvVX0b>EF@}unP>+l~&1jrW#rRXTjJ{SwMw+l$n0z?c5F9sscMIZUNEYnfe0*+jY(j;D4YIzR@'
        b'X@G(wNuGPy0;1TVM6qxYh^dC+-wC4-&MpMO{OH-5qlipx;wQ!2qvrS?_z<2=DNulI{DeZAy^n!Ne-uQt%SEA~2O!)mk23?*hYgqt'
        b'oxBGXnb;u;q)00_2RM!A%pOjFlFiK&%Tj;|pL3c;Tqy&Z#lt<)>NN1qEK@TDU9K@vz<w#S(rekX^g~rY(+Xevr!{}w)L64_V7}r='
        b'<DWKlTsYj?gKo!}K-KJ^)bl60iJt3eYW1UIJ<3($nlM23#tYZBDQn(fTwB<UM~C((A-CoYcH;)u7N+Y%NU^JbhPTaLB@_q(W{)t9'
        b'ucKS)JRlpkF#bQIBFHU%g8{Rr#)FEv-cSbL3qwihDwHfgqC_inwgBo4P`GG|()Ug{QX>ooSZ}tEl(paVfDKoJ-0=)3W7?vuZS4k='
        b'?tZasJ(RiHgKiNy!UpZD5Q@iPlefBD>)w=u#RrBSn0p_j(TK{tCEua*LHywd-Tao_c&YIR2B>P|(XPvE;~)d{)ZEE#e5tVmF?RVz'
        b'cJ-acN(Rx;O1AL@rQ^^QTOm_kz@q)Y1q_gmX)ap>Gy%ddnQ7&wA`cFDc;P6MI~u}0Fs_Kn4dsgvlNZfZg4m0^E#|V!!5-V&h@Zhc'
        b'GQZZ1cokmlN1S}Tn2=_L>kjqIZp{m&{z1w8M>o&EtoC4Na)7`<AD}y=#uIH*!`#a5x}`ll&(N>In|deJmL3j>o%~qr<VAm^lOIDT'
        b'{SP|%qW?iBLw>Q7fkRiIpZ+oiO%xTf0W?cA+R4D7SNyrChc%$Ol3B1sU8_+z0=kC;9!RODN97!J6*~5ypY~t(Alde|(!97ElC5ah'
        b'nApj8mF9IlJzO><^-Tx`;7uGZ?p_q#i1w!6U?1PKC)U$`)%ElC>OYyMbz72Ou0|K{(e=wn`!hW>Wtm$=OO_cOInm2h;GtV`zO1ef'
        b'1TafZtb1k;iUv@YoD7R9+3_A`%ViuIrDbvQo>H1x8fVGTTS~^wKWmZ5iVyw0D3`I!m6>C^=~PGZLQs3v`--_KOACwrE0)GRGsAHX'
        b'cSuZ8rP|_T8(oT4Dt{INyS5k{!Bv}z3YEpGWDm&YGIVN%V=+2_-2H90W9c|`B^LCrXiy9vCkwAi4$tcekg?iydB<`f#M##|4C>l3'
        b'%m-Um(;wHT%J;lzf3ydk(~g1}der>t<xLX$V=X7whR4$K((e`aAG!i$hC@4XNP;EF-S@g9rxD*l|DDQiM@oG4XF)$sM+G!;_QOq3'
        b'%6_#g;2&{FKC1BFvlUXdeVc}VgZ%FLGfZ^_pS-ZLg7E%nByA>*&OevFiG=wddCY6SM(2BXev9_i;2hPXA*OSW_OMuDWGNAg&S6B}'
        b'cH5L2Z9_kFsJv5eTH|h^`xZ^>XxZjibL~6bdi}cAXj>*dgPz|c>+$1?UE35pp5k{berV``@}TEnJ=zW=$F_|TLCIBeYMTPX7hv1Y'
        b'b|e%=-=kyLG(9jBI+Gp8-z2yTUB9lo&gXG|=$`Km5+89{J<Do&0(+*rf@44QjP2n#I;rLW3%oDh8-u4=@bsZl<+JH3JetI1YYA-V'
        b'Ri(;Ir+>aRoir=3_{0(dBXRoK5^QGTVktZ-wr;|-i8*LN1D*b($H`!?CjKp6iOE9PrVyqNVMGYyLKqV&uPdUj|4lcW`$LzF2)VH5'
        b'5Gv+ltcVk@3Dcw1=t?>UL)#D34DlQtqGetjgET#h-r!0D1fFdo{}zuoMJLfG>wHf2b!TjjIcBk0Sz=bLHOH~+I`{Kk;)%5C>s)LO'
        b'9<vx%mf)(jcwGEdqU}-CS`|Kqu_X@GEB$q@#rag~Rl++5%x0Rz$6%I3cYgO!t}?$aC!Y$+J_77OC3F%Psem8=s^0oNRR1QKMAv+T'
        b'ZsM%)%iMNUVWo%gP6LB_j0RV*xE!q#wY$i<SkzU*I+{;IzT4Q%z0j3!=J`B;4K<Lt7@Y)w5E=a`96>=eeH8}R`d`S!gs$u8Rn}(o'
        b'jFz5p7}`3+(3a7if=9zF{+#qLVMx*^>3-=4Xj9h$1S1Gk;YD|Lp;ue!oz_F}Tprnw^Vcx8Bm@<h#7#5O)-Yxbd7HyopOaEdMPlN7'
        b'A|X8;#_*80Bg}J5){i8C-i+4TiQY&%!idIN#as9SEqaSH*8M2L1$3vrmbBnWtNUHKOj4RFmpz=&Z7~BH^)xlVR@*+dC8|q<$9e|v'
        b'9@$%T9&20IK)oqjza>>swYh*D%2O7%=<`3w&rwm>goC64V`6lh2hm|PD3-GTn{y3IyhzeY@OnsdtoAJ<iN}gdX>^9v?j~FyGoU8Y'
        b'j0xsR+Nq@Bd>5T-$&vFpis7fn@ctEAVT|@^bXjFUqht><>a9`e%217x`|`|^6><+BQ&-+iqpP}Cu8><G^?Wz|5{S<LKOP;cmbWfo'
        b'XZ^YCJc;<Sv>P-Bg^3Vi)GKgzF_J37cS#yu#)Y=@ofX&D@XEUX>Y|bQ(Hh3kG0-0CtuUr-xNRMXocCPYdWMz-#&_>{RtaRxx{BB;'
        b'#&z4|aus>nADUd%h;F7%OQ=dy81-qJ#B-nBnEg*(4v9@&kf`1pXLBW|Y#^*pV6@EVCl$MpxCkEHi%z3fU`|~(Itx}Uu4qJ~i%+Pk'
        b'9{)jFUrHL`ormQRn1+P$#aSxRND!nM2LXmQ3z`YEi^Z5|G?PXO(^F!s@G*?lBpy-j=SZ_uW5!fw%4n9j`_72ID$qJ*(}hei`B1{3'
        b'vf%FSGvZ<=sS3x?CMZ1Lh)YNdVYFaq2_}U{7Erb=MD+(bf?*Q(D*>{~jJaFUr$BZ_@l!p(<Pc2E{Ym5nkrRO#n~&gI2p~EYG@l|O'
        b'FunPxOpqi08D_&MObvXRk3KzO*v}!D`ywxJqxiz4ionF7sdP@=lV{!}*Ke7lFlH9aaIQE*%2RDKL*lC8l%Y*ZSJ35p)umEkq>R$Y'
        b'5dR>#XSftuhKy-Kngv+k<j}-xMv5|t0axJY{|$-WGolYKB2jEyki!EUiO~4UC>l|hf!3*fYXjnSN)pj2(v~o^{RjtL4RH8qUn@rY'
        b'ioThJx^y3Zt4Hyt5nljerH8^KC5?cx9t%G}+b^*G{r?z?QM@f1#oL3ikRC?&AJmRL<Gyt!Z~?zMzWZ>(nI8Ep`c=~p3@@`;<ZlTw'
        b'n$GX)qHGU`Y?DK_1))y)`f7vX;66tlrV3Tx!(v1G7R&85T|*(|@~~<gMn<P%xO~s$edorJc}bc)*3*91cVY<fK@k?x<Ry`LtThxa'
        b'QikBQ3Z8F;gR9u!sw8xpLFE33Z%(5N*yFl^yUg8ZGRq#K=dQVankJu@C<>N1B*Ka*6)O@fpWaoJ6}E}D0MOQoUR+VO(qZsKy|r@b'
        b'EO+f0Qj%&*2vzT`eYR`Ji|&e0$uKb<olNE?M8f*RlZ=5CQvi<Rv!TMD?zDY}>UZ~_w#h>3#rJBTL?7<10xb^hMptQIGh1+T!x>8~'
        b'W^r=W$w+L7dtEhL_n8LV`N?SqQ9nGJ<UyRC15+<4*@S{{N!)j5EF8xZ8S`s-^CYerb?#*;oy$8}TTF;fP~;9JE7@8X7Hh)x*9D$Q'
        b'@Nt@X7tk#4;iG5Bs8pX~B1--qt37<$mL7^IVe1yGc1D+&)U~$Q*gY<E-Nm0ygMjy?CwiPyROXDKXiQgo;6&}-(`ecQ6`kzirl{}?'
        b'q*%^`H8|^Qv0-e!E*&I?#>|c$tHXq@a~wvQ^x~EB?2YZ$om|E7p~5F_x@%9<F@PO$Zin#xHEeOFs5eohwDj<~GouUXn@@{Mode2m'
        b'OjqjGlTqU^T&I$jJvg*SC0!X|dU)2Qs0bRg0mkm;ohiKfj}`tEYz9^AFJ)J5x>lf^P*ChlFXlLhGntk+oV>%Sb+n~{&Yl9EW9s4O'
        b'&jeab!%vTOm!GM7_H?W4t=hR~XbDtZ?5D1C8bui<HC-#Ojas>emU*6;5^S--kh<P+k#cP10O2)bDLet~zTRTmdI)~Vd~E9>co%HZ'
        b'L!qD!iyX!c*z`Fkw>ouzQ+L&AF&vixD1{z*(CVeht(*?63{3<;MXukwJTlBx!1_+yE&Ssx_lnb=w5fZtU`*j_wv`3g$cPhRK<#bG'
        b'Sb$^e1>>6dGfnsb9Qxy!rzmYA=seFnu!!m57P^HwbDc{Kb+kI!GM<n=g}Jq-18GRb1?<`WnsxsD>&jvYD~D~9mnBDSysfX&`>U9y'
        b'XzN2j&xhYRV^f5z>%)f+oVng&10L4>324T<7M<hn)D%0Dy$#_q5e-2=!#ma{acz8_Yd^bw>om~vOVWmRDqCChyFWn~QeZWIavdIb'
        b'S`&?dL}1D1U~r-D@HNoioNLI^5F1c)gxMx{y~LIuW9SL=IC@O;o$aPeo4U?0pL|zyQ19Q%1f2XL=_iTi3#UC?s(u%<H8(H0fwVZa'
        b'8*k`y_2ugrI=N=S_S$bcn<!s;GGHIb84%s-<mvgrmLhuM#u0RfOnUpnie1Mg5A9fzgvfTh3G1u_7HckGYR)uY=XhGy{QK=5Cm%d@'
        b'*Zp6oeH`z|Q@nejm1D1S+Num6m*V<;v&&ty`9LCfrnBy;Gdv$d-vQn4ei8{w?MtLp62^wl(e6X1uXE|>!tONXwGGUkuWFBVmc^&H'
        b'rYq}$r<<aHK!#|b`^ksxX9DR$>Bmw!QLDRcb4@SY`K5FspmfPfg(E$tF855(kM4t8C|MFU)*kGvGo5j0V}kxD<jWlDq!p`f2K>a3'
        b'6p^NM1s2eXrpziZWwMG6f;X-4zs>ml>#7eHqpxIj`ZG}0x%o7-tT-j6u<V9ItE~IoX|P`;n6{p_@9uQ|v2*FofVvAr1LVO_dlzCf'
        b'zb5UB^XzGb!@Z}|wsMn$14>BqI9b{XVzl7j*Cd?*PI++y83lBjwq{Ew@MxgLwskifWMQCvsfiVS93A~qSyx`Z4j4qd(E+#t*kY^u'
        b'K)c)9X-h)_XFVq0c)NUqzPy03+19CW7Gv^NX0~ws&wEJoTIjANIk`a!X4xXC#mPH2bQ*EimJ-<?s!;zHKqeQrhYPcM)q5o%RVJr5'
        b'T9jOIXFhNKk4}(Uw%Ev)!AG1$(8L9nlw^7`9glr@tbqiW@Bx$=ny+lxc{<<BAPTqX_p)SetoHG+`r=+5iYvrBr-S0GzIJEWFyk~@'
        b'2A3lT@xhZeb{fm)*ytGVt0Q!bH3+Pc`V~6p9FR}HA@xV>!6t(1I$iymIOCty`O94&_N-1;zs?iaZSi9}R=o%{Yq!k&K({8~58M92'
        b'ZX;=WP~NfA=O5Xz`{^k%Z!{LQO4paDoxHnomlEAzM39OYQPe6_(KxA4imS|JG(pEoC0GMJp~K}i2T!rqAHq>z&=YvQ!CaUVZXnwT'
        b'4DHr=t8VyKSpDpX=q&c)0m&?Te5c<}d9>;#@s<*8TELI(OF-8xi}#MN(;s9$`6j4Mrd70zj(wBd{KnYXFNznyqoWe^>$XMjBX3m8'
        b'7Loh5|80~mt3dd$`!;C>Z3L4fW=I2u6*Ti22(+Lr!G+cU7Xff|hh@uarw@BiH&EKlaN);yGcH>DNAIV)(Ln4gS)o5*9$hp{sq-c7'
        b'o=%^i0<snos2U@>=~`GyxqpZ7YZ&e*+nUrQ_h^{9vz?KpTBRmZ9m0X`&~-8wN8HaLIbFBvw4jNhCqq+Ekw?gh*9=&v`;$&Vlh?iK'
        b'G<bD%()~Lj(Migmi|wgB+2Ol@2cq|Tq7V41*g*6?U-aAXP*cU$HgvjN>jKd>&wLtWtY^OM{++u`9d!k#J?X1}df>&royqP%XF#?)'
        b'b+^PfzI)|=$N9jHB2veX@yKkhElf>SGd<pwzCCjP(&3KUd8d7=65SU%YOU~)S34Je=ZnAjwYl&+@BUp!wU*Pgd|PzTpRoS5*!Jku'
        b'J&J2+QXB1RNSk<V!ogF!XhM1~LYMCB({-7rt7LpWu1>>#xzDLiIKA<<Cm(kk;AM5fgZq>{L{#M}!kPjPvbyxsNztBsZ1YD%n+~f@'
        b'J>Au=Jo(WPh5Fm*lno_6RV`Lj0U|y~`_;*hdK3~mt>ew0g6de{A)<jO=>?5dC7yhOp4_qR<gV6eiq3BSXw%0$9o;0K%uhbL`J;?h'
        b'LNZ~OYe3mbNV_`N)+cf4&ta^rs*xu6d_qbhKa7Z`695RmoZzBPrxDdL;(bR@13kY+1m7g5qY<zxyIWgn`Gj2n#d;^a@jCR^dp#Vv'
        b'cZ~~m(qtMT*zrZg)5Iq+U4oJ|HV+w<&YPVyAsqYiStEK8(BSBtos(5$O2R_**OaGy#HHKhIre4dA2U5leB&238>O#eY*p;WvnCUD'
        b'EmsLC6Qtf}#YrZ;xJt^!u5(qvpVGy%6R*vYq5D}E$-Uo)pO#y{i;Rikd?(n9dE~p(yQV8m#%4FruTd!+ySvqBX}?=Vs+VGsTlt`A'
        b'^S1vGp^sCYCeyl|va<Aa_leG(GFq0BKBsF77`4rygwTNmTdMNVwUOfOL)+wSQPB6%_ecMa_jH2##XFJPKmqnPA}N|CHfPgaJC*MD'
        b'I(Jv?l+}p0^UbWo8pz>$=)544=|)k}x^40f9W6|}=95e5MH%v%hD|GVKU}O!S_pb&i@V1e?bdZ5mJ4+9<|v;WGo_g)d=$*bcyn~!'
        b'A3M1}cJ9LI4thK?P|cKJmRZd5iek(?5q(tU?yoId`w;EuF-v%}^suk9)sHiEtoB-1@M8<F`Ze3p73S*mw*(nQd(_+If=u%6S}4k!'
        b'B~XIl*lRh;{JCJ7PcWJ`m@6y_i-n%dgM&~w;{7(v%cR$4A`w<Cyfjm9Gz;c2Zy4!UA;V&p3T6p?BlFKh+wpL*nSM902nWKz$7BkG'
        b'bTG^s%t-jna22btBK^9kVxlO^EaZ-zz)#3+yBVH?cSvdVHOpw-JgPfqtR-jMWMic6jxe+ks;|EKQVOf#p5&p;P>Z)Md@V)!BoEk)'
        b'+zDzULx#V1fabG35khNyREai0XDbdd`h2j~^cEc>&9{|?Fmrwpp<^T{lOe@lDqp;i4`3Ww>v<b%+{tVnF98}VJs5W9Ampa#9z(+K'
        b'2SUA^LQ53CCpz-QkOwv_A*x>-evR<{jJO5S$8a1m5K1fIW2Ezn6RK1$S8Q1VGyFJNeQ<wC`{J~NK@#0&%&qR=W3WQc9o|18{T^hd'
        b'8{ZbiJJm0fhy$|L2~KuMP+FWS-Z{a-v9q*D3nznHpP(xsC1CI-Y-w@1ULeijsKggL8Fvzr+UDerfHNk*C7KrKpH`q4l^SKcCv_a?'
        b'cD<(eIO9B=YLQ}A)qa`B$+^d&m#tjPpu|0<Q(Szj3OJK=1^bbo5Ohv-OHpon_aNn#bc*xF>VR|7tgQWH(D{%%+#!CQ)Wc0I=Jf7+'
        b'9gz|TKG&t~CqDYoeG6sua1XU|liWX{=l0L1$mb~fe++OjK`z#P9px>OKdso`9pvIVi9yo+J<95o4=Ng{CW-s&`voE&h$V(2fck$#'
        b'pu`W|Lk~V8nn?G6n4$(H!;cH@iyh)Fxxc9i=}Q=Qx&!<R8!@^I&HECjNcp4(BTkO45;%nlw;b>2KHd>|o+1x$V;di4-JktS4Xr5U'
        b'{xkwwh#$M}i>J7UPx1VGwIH#)g$22ZCL<f*l7uB=-5+;|`!gO2IAsAq!w2F=wT9gtw_C1qOgr#w5OB_^vz5=FLr+0%m+O>)__0Dm'
        b'7)%NFARAaRR)sU%PbV2%t|CT5J#D!t)&}+@IuNHs;EFpm_*n5s5FHe5l0Ucu$vx#1iq9nqHeCoS{zm=57(RaNl46U%#luKhIMt9w'
        b'smszOt4Iv!OE`1|!xI65sWC+2V<YfOa|N(qQLF>g!N+=@A?IQIlCjv#i~Bz}y&p1~8F%a{@j|h&f}i5K2?}Foj2>t<Ggb$cKn;!-'
        b'MmJZt6i81c!PqnxR2AeHs0y`EB7VC9D>UBa?w(XZKZp>wvV*~wLx;E@PU<-w>KP;F(mEEAbQ}`{KBOjca2Z<uh9@A$$sE7(buHkr'
        b'DXRWh7@2E^Cpw@DHdSas3Jf=va?JZ`c#5=bQy8Oz^MZue4lJaZkn4V|Lu@(|;F5z*r8_@D(=k0<Y`~cibdC>jOpsH$=XHo`;Y~#='
        b'H>QV+1NIAY<2_ET&za&jMF?LDj*v(rvZiQvwn!rnqhB!RM*)f-k>*tQ^!w1-yG3BAicw%w{uf}Wkv7Hzov|dIijc;NbkrSm#@z><'
        b'1Z3w<5^ELJ0nc&m-3JH}{3IYi-cPw>#n*9>8u&Mf1G4p7(mXI=d}_iZ567k^Km%1n9_7||f-TI}*T9XBM0~)hpK~q1shXmO8^R#4'
        b'QWFX3+u;cX(m)t|o3WVWqCSU>kPCFL{yPISGvFKp$zhqG!4uJOO))wn9<Ra2Kmk^T_Mp4}jz%6bp)llQB+zbRq?atd9QE?6Q}=s`'
        b'Zehbv{5^>_{TWR~xTl>&efi>4?VOXgypU~t2%ISsE_eUx6gW+hed{(^Xt5M4AutVv<w!8o`H<<ekZCAn`g6z>2rV{COUzL!vr1#8'
        b'a?BFa96S6*SR=)^Q}|v9o<ra$%sxvj-x@NV3z<F+nGS?BX1UQEv)wG)YmUw_E5yaA;l(&sf}`>(TxG;#fL9iq=@Ro8TE>_XYmc6?'
        b'Een|>&#h;y11Q7&!71C)kc|@0`Z8jW16l)z`g6>T(Tr)#c<GKX0L#G{bt3M5_!P#3#DI~w7r!k$@fu^2*Os2@Ut`-9s>#*0JCE4+'
        b'n@wMawtNmi#11K;jR39wcVPfxdok31xV<jOMF%(;6kBT^r`;AVL6bDf+Qp~XLb>fg$hJEKE%(2^d@Vk%_IIbMK4+GNwxemHSp73{'
        b'Y)1%s2B7?ZT+TcbDk_kpW56V02Tq2OXvqv=RA^h2^;p=gIEmRqwpF2`C-U9&DKs`>PpzMY``3&%bvX3T4P9&=t9=!4ICiw5M`}?!'
        b'hfzE0J<v`Xn&eJDRc@6d-0lxy+e7|8EVpe9LHpe$r<nQB&@s?Z7c|s|8VaCB8=5PJhD4@)to8RBDhai{3Hr7LBPsI86LnvlB+Zoj'
        b'ixX&e^x%n?sk}cQsC&i^j&{@v2^kednkCM+PCVm`A5BTkd8f!Indmg@XbK77s|HmRMUq4$-hW_?c$yE;C}~!>e~aKwSOLQFNS$eK'
        b'Nc#_94K!oGGCDGf8XeOouvPoWC|pGnlgmJ^=a-o`pRi32iBnsNmQ+R53YiL*6e&Y0vm}0nOoK~{c%Ve75tqQTdE*IIB}e6PIcb)W'
        b'QBpl}=f`VsnGu&Ue4<{jGX+CXyZaz&&4HDcn6cnh=CT&YSo8BINIdF(2!Lo4kiS{LY^k*za+Mb-6=mv~W5_7Nh*LX1L~~`NToV-?'
        b'^^C+AMd`6bmdR&>sH-Y7rd=IYzbG$lA=I<vzL>Eazjp0ne2%d`f(isM(=OI$p?oonA08Zx5Bl^B;pH$ACseqs2`wT=EI<se46Ak0'
        b'ogc<OgQ9wfyFMX0UUXkY?JnF60LIdZA_xSxre*~IO;HoxWQ-)SCIW%L>Py1NcwZ#-)`i6hP)dVGH4z|E#33Q-o#DdWKTf>n?m$4*'
        b'x|`O!VGWEQj;W%ep(RAV2A7CMQR`T7TB!8j!iBn<QsfXpIVcT9jkuH{mXB5nCG}#-;U~j|&))E&6DmDiG#N#D+Houa4L+K^qdm^('
        b';T|9X8j%2tNC2cy<j@VELclU$7b6o@k>0Q<&V$t#hSlHP0Ne!{!fyP8e;1>I5!=OrOaN4h0SzDniXlM2Dw+uRTtuaIak%iCFQlJE'
        b'd?ruKSl@wf(E^#bW5EX}$!Q+PSdV5dX~8_j(eBIbAXdezuxANp@zhlr?x+(jYfgI7^3ff+;@&!V7+w^1zk;xamNw}awS%AuFW}n!'
        b'(TSk!BlT<d+&{N>uYj-e=p^xms>0=W>FX1(4cl<_ta};q`bF~kKPa@%D6C+wJF#@!{oD!BxQ-rvlh}{biqiUse_e-VyNjyUfwS-o'
        b'{%bDVxn+$IJC+__V`PhpUZ~(=g(t=i%|wUJMM)k^;DU?2vl7UlY&;>If{|wOh&zdH0J$!Aztt{ICdr#9G6!pr)SJWVk7ZTPp)%#r'
        b'PG!}a-LLO5!vp-YKfAJu`(#4|tY{^!1BkwNkL>o5W_(vInlQ$3U+h@%-E&nOov5hV!Xb)$Vr*er{C+oDn&GZO^%>Tlpa~0!rT#&|'
        b'lepl=^}HTUb+VL{LZ|HHU`<qmWH<}aOT?7`0+guCq_jIMzC>GOW`+w--V%>3*5J4*iUe*3{SZ-a&?3*F5yWLrj3sd#1~Ae)V_1DL'
        b'<lCFK!?(CUx#flS{VM>me~nge{n<xR^rV`@=Aondjf0Ji)U|h%T^}+2qwM|_!CY$R!S*LE9RBY*bge8!eO>3THTNGL+NH0lp|0&x'
        b'c3os@-ei5bl)I=M$kvt+QAo1L4h`)WVPDkv>Jx!vY0J{~od;2zG#c{-E|NI8!xxVxAkpFpk`=>mwK?r%GzsF$7nJ~QuJKcVQc++;'
        b'Fe&z3n;KRx|Dme3Iu9VLv%l_1CR&pvL5hMpN`ujbiC=jS172#&PWYmu)z5tC;iP~97)K9B?cRazE|&o|knxg-Rjok-ZQs2EEhmY_'
        b'BAHq)To@X%`jPL2W#fj4?G`&xK_<{t#qklrPn1vJ<UWQ*@?~-k1vFZ}mUv!1Z?}ZjOd%&;v&Xaxal1E{j5Ew`Z`pT3(B#8#qIjM8'
        b'W_zuootDsfrs*s_K~XidUwJTqCZ?m4x0o?px6AMmht$S%hSuaM2X0iEeH<C&h~tS0bkX5Eb^Zbtw2$w^kmb|6g<sz>PdQ<sVl6ot'
        b'X1=|$_a$2Tvec6-RPSuZfhi;BB%o`LRn*3Q5Zvf-F=hY$xKBxVwAPxv6g^>=5}A+Mc_`Qj&S)CpO~H6=OkKr^$P7JB&<b8_ZBRg>'
        b'`aC^`Pd0Q$HI3<NV8y$$jq2bvc(AsFeaQy(g<Bpc<$f9A#TUSK>?YbShJAiA=$8aYTlpK?cWfoB=TXU)S5DBcHAL+)lpdq2%sUO8'
        b'@+R5Ka(ZHe3@BqK4xWx}t1>WtZ0())nuCn%AX|k8mX5WyhmYV51k|C83Rjuc^8cn|(DKj{rtUyHuVq|E#6|_M`kNqAzH&d=E}of('
        b'xtF1b)ZOR`XkNphD={WwK8-G*nY`<mM>EBz$w*TkIJ@f$PszA>R~4xH!U<?J0HX<q)(Ya5h}1JA!G`~ir>e&|k`03dAOhY%UVXAc'
        b'`wwjR-*Ef(<9ys7D~pNY3nU;%45^{Os*2JZDDQ?af}*16G#8KJt^8t2`qk*1toc{%O{9mys?!j^HxQ*Ne2QG181_)|jR!z9qnI4)'
        b'$(0XhDzp|wy;^}TgG2EyXFKb<;Zu#<JYIr$Z2=J=vBG?uUp#JDbvvMwfLKv4$Jj=y^vUSawGwj(*0hdePdNOT!vTM|y$qV&y`)&d'
        b'Eov_&=)xx?>Oaby&mSixN^zmYbF^bUGpC{#=c8sh|Lu5YaRq;#;E9AnpEQsX52SNI=^l3?6697dm$<(~`2K$wd-s5*j_d*W=H})>'
        b'a?u1ZAmBE+ArKL}5Nknew}KQ9X@3wEsoUL!Xpp+?{*==CSi75CT8NbHVr&(t-OWv#id0q-1bNCsjnv{+?c26nY8$m~w`J9;MIhff'
        b'H=%VO-}n9gN#=Rx%$YN1&YYP!m-~E}i4XJe-|Ju;er$Wgvj^^{Ok_SSFJ6ahhAAUo7db_fuJeMD@{@&&XJ*7FLs43;x<0`lFnIsT'
        b'AC_Ii)z#^s%zqDIXYJ8!JZWJRg&6`aX_$>yczE+VcX=3CUbl?!Rfg0?yQo{v_@5w8J1S~(oesh!xurTzwFq51rsm7;r<{_-rg#-C'
        b'2Syte6NT^G1mM<1h&7{oIQ`?{rHmrmPFBq$bQGYMzT#v?T(au$H9CeCsoQs>S)CwK$l)DVSs`s<l38IsU}PN`W|rlz=!B_l2fk|%'
        b')E!W>C8CD(t`gl-Q}yZdWwwIOlKVpn$8W~ij?|x@Pod48*k`o5PeRM3xfCrke;NWb@bVX)KKYU#l-ZigCwE+fVd<la7bGVq-$UPM'
        b'5d!7R!YNm(z)cNv(qUI6U4<Wx*4*$q85|Jn8`v4m`I8LUnE<oyv_I)w*6ARxS@#dqA@-aZBhDq{u2+YdoY48e8oT~HJovL=`sD$q'
        b'Q{LcsHGQ;3*=!rLDJ|>(JDkieClY!-m@nhk8?>i|jcZ;Srm2jK8JaJ=$;lP@%(%urJi1Jo%M=Sh*IluIgvIx*WI{H$bC{^R(z}jW'
        b'bpEsuG@)dz`UbN?vQDb`)iCbfiA1+`m{@w{pFbI%FF)t-FPR~SepYzi@_(@Vo`InOc~a6Bh76*xi(*Emmf*+R)wsHd<xJ8${FmH`'
        b'^w42uXbQAkfR%OGPrNW=U&YvK&O1BtEOx?Tsdz}nt{`yMal&D`-m%;%XO=EYAH7GJi{Fn;UNm4hmJC4mb~e63P4_kF?`o&oIv)pV'
        b'-<1~98igTwbF*_v2rXw}2NWew`f6`IMN8RSKu6x}$rWUMAE?_YOnR@|W0w<j?wZ-ZNotRIeoceOE*G$Gk+iH&c3Soi8T}G{*Ap_;'
        b'o7A~C&wQ|O;nzK9_Nn*Hj``+NyQJd@YDsQYD6wnF@X1BjNB1dDy*W0bJU=pa2w5z~2J_?VmKM2q!f$``+^6EY&nm}yl3V)}g|{b1'
        b'a_L00b*OCvZ&IL$2x(c?ZGY@`@i;Fxii9S|<XYoZ5fS4mfBU_$x78b}MMENi^8^U|PvtMje<6QGPVc3EqI#4vjhxw#dUtWBx;Dmm'
        b'La-(^vNlxSFxsiCc^)Xc(bhL(NJhjod$0TZLJQ~nV;Xor>O&*vXz{>rDn~y}KJ&h!uw`=OzWH((tAZjgAw3`Xu*cJi8Lx+EN<;20'
        b'xOFn%#xUu<HGjs#Zgt{-Fq4oobA>1Z3Z_oZYX}s;=P`upvB~?#p57@fcsp1v>z}AIqNgb$hH(&2E8=-;1L2wh`ZN)AW%tHO)<N*L'
        b'AvE$a4gsM*#@lt%FP(&{fn6KJzc#}q_`~GDHwQ9K3FMiz)Ch>>!b*XzPT)vXt2|TISZ{v2+IDM6BEAi|;rIPikgrp#nhD*XL+CJd'
        b'Vo;x}y6)%CNz$XeZyAy+)%nzTe%yFCXw9hYkP1PreR!hUo{YvceF|XOC*vMGiMNchy!<5ww61}k$sU_fqh~xK)gH1`Gd^eRg%IyQ'
        b'{P#<<ZUy*^>pV%z=@F|2YgrG2#GpeKNf$*e(l1I|l(VR)FC^p8XY@}#4O!9_`;?O;N?K0R|Fd!Xkc1c;QS8eb-KK2Z3!0q$%`=US'
        b'F-&3iq?jg%tEaq6f3MiIsp1KG({FY^BUY)X@>A~wBfVMWrw#_g2df-^-F<M0J}0e6y+Ex;&#ihr{zT!A6n^GQFNO<vRW^R!rW^Os'
        b'y+4nSc{rx$l~C^&exh^*dPKglf)q1E>CZ2hpL+dt=%&9`K0}`lb^Nt*V2fInI=OejnFgu%s(+~I;Zxg&9M&yM1^}1B{kO}TUfkZ$'
        b'P$d4^5An&+O}8t@HdV+QRFZM}$llbK8*-|AkaMt5^1bS#TU&EVHk~|ka^)%SRhl>*S{f-IE_xz#U?5^(L*;4lskis`lHQN}4QW*$'
        b'`V0Nv?QKVWr9m%#&rcN2{BCa>S#{3e5S4W{cu(<{Cuvj+Y_s8~DWp1jM$Oz9o5gYuLrNiK=j`dT%hmtKa(Vy9av3M-Kmz`R?7IKt'
        b'9g#(MM5fE9Liv`E&X9zc!#bDOehm6<%}zYFs$rzmoUs_2{mqEdw9jY~<OpAW-Vfysoy!k?JgQgLuu$HTXmK*aQ8{cFg_=iB(6gDa'
        b'Mp*Y~se0#b%QVCP0I#1WLE!K@%IuTrktgegOaze@vg5qEQmIaU*Rnuuo9$SjuvjUS&kNK^HVdmrs@Y#3y5kC@<JBmw8hW5#-n0l+'
        b'hzLT>P%y7RDkHy>C+UzEWQIf{VfRWyBBgqV8l9`GV=VkhZOU!0J)D5w)UV<X8f?Pqu)Cc52lj`^25)+uQYq|tGG|)nodD^r2i0~i'
        b'ZbxlGTBz0!&{68NO4Q+F8l0yhN*BFC2j72VKQ4ODIi${T;!L-qFh)A$AO}t<><+=e%e!~H8`udgZC2DZt2Li`ohykZl9f?QZ3<M}'
        b'a;fyt6NO2lGd4wPSsEMBxTY+9@LjJ{CZ$)n?wiSmqjevjz%-(t39PY_NFxUll};h`_$^Do+P{oqprT32(I>1kyutHkBD?JJ;1EL6'
        b'rOs5HngmexL!W`h$U}Ji79*r!jF@GVcns-Q(BUn)a=b}oS2bot3)PkiSZS9oSI}XF(wR&3mFX>BAUqpEcn;kj<$Ye@OX5|8>WffD'
        b'MkSbX8H!*JT|$VNgy!SpPKMt(s3~Uz0h_b{o~uA@b~vsloR>MA6yqT2D2Kk%;Z(v9vP};_U5673=|!FhVsN+DNlIHgGIjH2_BPw0'
        b'#Qp)xP6bUm9RiE9vb6@^lQ<gir4G9a##&@iUsvlWo9OZHjZ%DKSjRsHWO67*#na}*aqGzwsK`YSYc5E3_|RGVDvTxH;o{7oHmm~b'
        b'(bA=CrA1wVAL`Rb(@kodV!p7nUQ+iGMQ7A$D}fGbb*8=P0SB}*O$wO(I7ilb+1W&DStQ7M7_CQ$?8{Qdp$LR=Tr@8Naq#QYR?!KD'
        b'iG@83FtPU**8P+OqR$trN)`WH<)z8anH~3$SwAC|S|aSjlXPTVLM2Qk?%Ct<X;0YClk9Bi=AsjuU_c*{j=rV*Jk#4<i<9>cb}41Z'
        b'k@6qUO?kk(;{!uDv8h1;8x2%s8q_=5@Z7usop>zGz;|t#N_B%`X@mMBsXd2!B<-=B_&J)=`S__!CQ3+$i$M|o`1@dkA0FRiQ+qD}'
        b'<3nEHiF1*VNn~UB;6_%H;7!qbnT=VRcrP8nY+Rwyd1(=|F;^1@so5IL%h3zftMH?YBZf0^m9=d5$modj)L)0z5ivboGhv}EohM3('
        b'_8K-WM|wd!hSv!1m(z1i29%*GlS67-cCfx_L9tQIADSGuhYQ)LMp}-0qS=<N-Sb8JV`O?E-pHBD0Vl*{8jeMj-ZLDOeJO_Htae3h'
        b'PAMY_Oc<vYIo3LP!cwEKSgsc~P1&{Vnr&awvq6eEI11PyA^Lqri@V<}P&V+M(X|ulbB@1d$QO+l=#PgBiG1BSzkI8maq&ytsAyQ%'
        b'9>>!hSgHktB5eGJyO^+SXB;0*wNv~V^8Hfrx5557nc20?*2T!F_yt|lY$p>9`!rX^O{Xb(8u#~4=ob{N%wS@&XDt&_Gqlu9f{=w%'
        b'p`Zx_Z+I%knYftnOxoli5?<0WS~B4!QSs|)U9L>OvS<Oz#6CpQA#`;0OWCy{%U8}Bn=djlF*fa*da6b2%a&=$P$5a<H8MrCkesoA'
        b'oJlBTLW)in<OZ(666ClrgMNs_FBuGFUE#lzLu;ip<`Plid=-UK7A#MQg*o&?QhIi{lom=u=S%VBf6hBZ<2$TAR{S^QeJgiDFP-k+'
        b'pHAq*Cx$fMV@XxUF!>`wy)a`)aOO3Tq64GN@N0oz>)XfBE*-8qCC+dV85?60X35>VPH?+USVxfNIpH*!5b?0}4=4IaOOtxYp|_4='
        b'4b98P*|^xE488G@=DFR4Qi)#ZIsW(=J4}Ls(FSE=1N;m*DvXDsK9yE`;`QNk7tGbpT?tcl?lL-T&R9anORVGj49EI}Gy(nEQf6ST'
        b'FzW+<OGvGB?ZM{P4#=MfwKxYHkMG|2+JTrD+t3K?S1RzVUU$K-*CG^clUBbVq4Arl%h+$tx)V)|%}^b!(2e@*nI<DUH+Fx6V5e~>'
        b'6S#x&^Aq~CAYH6QC-iz-T0%Vux@<5_v+{(EsW$)}HPy$eXAAVhf%_%ahhQCs(m57p02kuQ`9NLZSvHIol3^)1CpKIbv1HzsvS^lx'
        b'0-4I{mB6l}{L3jcYcC4{rPm%tOCC#Lv~nWsyheK>;Gh-1d-3Y=z^4}R_ANQi^Dsf!Ue%IH1_%=so&8m0z}^UaqKP;`M4iVC9bcDE'
        b'?}KzuQvsh8?Fryc+k)z_pQYb*0<>V*QUN07@BGsWIuySbKj}g$gc+d$sM?HBpd_mm!c0o2AJNP@5uPChFlh_usK8e)@nf`e#uS1?'
        b'{u`_J3IqiqCx#r4=Pab<EtK__$Oy5uE83jL^Q?&&DS9%Neq_BdT+v4wSILWZJCCa$sW1u|W9F=)Hsku}qF0UUXIt;WqNWJCVE*yQ'
        b'i)6vg<7J|)vmUdS>53L^+x3XMAo|#2+@~V?BrT@%w%gI17#b%ZAq0s-B@yRJ!g2TT(`0rqd3!xOs6G&~y}mwV`{BCAfgw%AIZe1~'
        b'5mWbh@mKPuOd{lzXMWsh^OFZMp^m*IEKuK?jqS68itU|H<AD7050BH)c1;)&yOe0=9F7Xl3<BW1A2P@BvfBPI;V4y~J3U%{a-xvF'
        b'x%u?*atTqM8BrdmQk|4{t`SP8(dU&lTvN^9*F&v6F#3w_UP5-N^DX}7wbGh&j5mNQ@B}O@+B!BQlnC?n<BEW<o)W^k{&<rFFPoyz'
        b'-f;BUdsm=F`1G)m;v&MiK9bcawE{&A6HXGEzYVFC{9C_(pME3oFG6ANfHLFXp;YA%2O`6%NTGy(aFb2eXVQ}Sk}VBnRTZJ>8`}1&'
        b'oyptQR=w?iwysZ#-cplOeoo+&%-JA&V8>0zmgM3M3e}#O)`6ko;)?P?MZR>ra1VdVY)pntxWsyO2-<_))i=ki-(v895Jq@YsoJ!P'
        b'Mo%|7zq3Sf;5r5!{*tGUANVp~JPvT^EFyW_+B_7_Qw7AnycD*VPMwYy{NW4I!>k_<P0Rl9fb3r&2n&dR7!!Q^aPhV=f)-{fCFUI|'
        b'CC7!CVPy*pS~68dMw)-Gd2tA))?7$cWTg;0zIQYv*S)N$+Ue(B7y=e(kZ-R)5Rz5x7iLECzE_0V0{&^6q*N3xAz=SlT#~+GOV)9J'
        b'N%Jw2SgKN8+xtD~J>@USI}Y1M-h7AK#w;(^6%uQFWY*vO;Xq+Qq8Q&>6;uqBJa8PAHu@O-AT+pmD}dFCC5tyJ$h9ztChvsd*hF|X'
        b'AzxkSn@mYP9{9rb(}YZ8M$E;y8G==I`V+!WF340EB4}9N6W&?B^fk5ah+mU%90plPN`rT6?j~@aQwm|`^gPcDg(@(&Q@>CfHKMZg'
        b'M~p?A)6PCpUNrbv#v^1|Nzvzv!qWcvm<ioC6)2ADADp`oMeKvF7yKxz3I0ef+!f+)5%`|<r#y8G`AR!ZkkKj5V|cFzeNrWcr-vaw'
        b'q$CSTLAW4H^Xp?k1Q<7vanMmH07Hsb3pU_*YVIDwR~^%9dDdP(bk_TlA7#y%;QdeXnA6eJY}@tiu_kF})PayDklJ0d56s=Uh?nWR'
        b'E*|6laZJC+Hn-X^6Xdg+(KuLE9|FNSW3bo2IK#>r@9h9Qv{U{y#QNbeyPmX{iEL@rvq{(Q{XDE6q&I3o?;PWAUxe`Id!fRd5Z?j6'
        b'Dv|KrhO*qbWAwp3(s~&?0UI#H^W?Fjri7QI^__G?Y6HkinqtaihBCSNb$@NN`IbK=e8~2Ns%R=<7Dda@X8zhFqn!chfDTl3jo-ti'
        b'pB$>stlOzpc|czowy^6MhfHmI@{=diR_(2iXCh|u@06=A2s>9bWx8$wBCtZJ7p$X=>IF~kt*7*>Qo}yXlkLo0w95J!kJ?opE-hbz'
        b'*SfC_V!y_Rc8s&qzq1*PuIYwtE!RA>(`4KJ_-%_#G*GW(!)65cM#dR-Sr;8c%j({!^tAY2kwN;VW+mPwe#2kffDVuX#R6+&ihIzh'
        b'T?ksArCVDnC%y9t`&&2YSUOZ=J688e<(aw)8(G*zoO|oqnSGUYAE{Me32RuikV>4Sr1n%&PIaT+qfOzSIi`E?ddk@$TIyVOCB-|q'
        b'lT6dH84~<<JX!c8MN7ru1VJ}e-SFGrvI5{&LPwrC_tq@{stOUPE>FsBJ4qTq8*(JxtNxK&@o&8qleUPgVVyaWs&CM*l5?uM?eBI{'
        b'lC+GDN^NL4gPkUKJeeHq4;k#wqsLewp-Lmro?>N?nuQx-wHpe&p4f8vB2e^Oq$un3?@#;C`r43P`sKbwwx*F=?uU=jOVFID#A>SU'
        b'+kIq<(7FmEbXXPabgeUn_==k9nuBO3MgGZw`b1%afRzdg(*(Y!{HpVW_0d5tZ-~_^=y|+ijcfeRhWHbfFx9y^>8l30&xe?}Fd9#e'
        b'ej!se$MSi~BylmLfQ2*i1+lt%H@l455EkJS66Vaw7Ku(MW#Z<vh@r+4lKf2-kP<Ji&0^x7fRubo1v8A-WjmOe%<v7E4RnaQv9eBG'
        b'anOVx!4*Mc-0`74Jhmy_i|4$tD$S#V8}^b}*@WIeM?;Ez_}e~`9satmyV8<ash+2XYK6v$0A{MI+VuEAE)uc!@Vq}?rs`&rM6@)2'
        b't%8nhk>>B;4V!TMW&ljqxR{-Ir`aaR6G3)<btSuupq(Q=$e1sJjOvY)aTyUCRw&NJ{@ptX80)^17~|%Ef<7uD3OzZ2jxqcNdHw)6'
        b'D;D8G<qaF<n)!oH2hA`-yb${75G^)kP@DOG6JY|CCGK8RHX>PaWsr$eCdqlSB}oE(p`$hdl|w)u1g!Rk#Rs5j&I~bOgo9Chl3@U1'
        b'Z5!&tL&-T~dPA(N$_ES>s4Ovs0Yo~6hv<H4$QfraR|?H<`DvN&>UHl$KS7K6w;DwD1u|;^)-r`t?4i#rr3yBDCPr6M<;w)dWisP3'
        b'bqO_esZ7MG;@Filfe^Hm&AMdPO`4$ZVyx;6ryNbx$Q4uEqS`%>RGVvxOATZpRQw!|A^_4PY*3X(=pGMoE)zP14Q5JCN1M0YFyH5Q'
        b'Js#qF-R~Y8<W3CwuF72NZ_qMx*$v(4DeGFC2c^++ld#_8{SI`4j(cN)8hK*0Tf9m+%$2YcdQe($ZXkAJ(Lxv(iAnBG!#?9(-Y118'
        b'O;TrE3LdSkBR??V8JkN-9x;)+jlxSN(zWV4?zck@rvk*U>wl#v!AGw%Lbc?=L%zN#)pm-}QW;v2(edJ%M*Pa={&v!vOqd+IHb8VC'
        b'vA=^9>mgc)(ZvM4C*fW)YcV7Y7c=X8T~meIC-CIhx8H9Rs_6{%YDJ+g+}Azz5X`4A=OMpq^^LN%<&Ky2D!pOLi)7X>i0mVHY{fbn'
        b'sv-JI2sA=K{8Pf(IKb+oRYjl{qwt+axYmTIuKeBUu;|uHeLF&0#Jcycn+rn<qy2p{6EMf>K^OxEqs{`Q!{o4Uh)yv%c5jF##qaxL'
        b'81K7&lVi_@X#Ix8i6+P14bkvhU)(%E7do;kt4{mhV6sNgb})1!>y%&4h~M-tiSwTH!)^-nkk}XT;t4DdSttCo6L0Uaj#mInAWZdP'
        b'QhYZ=|5P1;rdB#)>FVSxf_Q_;aD*h>gFVY|3@>HYxtf6lh23Kyyu_{@l6~)4M+b12yJzhfH)q~pWH5>{Mi^UYkiraF77HU1X+n|U'
        b'IxzKuOm#|D@T<Y}c>|0nsodenc$YLeqPEnddjh+I+Z#oSQweL_0Q(`yN~0so9<jcOzzeri^lY_teVr}YVnLhbj*sfl8>-qHiXE+b'
        b'-%rFa;`gAtUVP^c{S&_n{mXjSkFF1@{^qAMmqOu>A<x>505{b9#pM8W3KMS`MM>(V6>B0QTF9LO-;x`ey9aCn{e@aXixi*A9l+v@'
        b'V<JIDnoS`YFp0>77omTGX}N(14WU3sDq2$3Y<&fbkDS_ZOU<LY<14gZTk8XDUKU^Q?}{9-&y7}nf0I9N_kQYE*^e0G?k#sHf&XD~'
        b'aQ#(QFk=8Z1p=sOp?d#rNLGp4z3)!(dWxCzryLtNSYxf^@e+~`$tDb{RRqHc5~y&^tpSE4YMmPKAVYpx$Pm8T@BTZ=bH><H7Mip>'
        b'1Qz>l`!Z4Km1yg$gS%cEL~C9d!7L}3BB5repJDDr8Q9;?3Q1Mb_ptUA-nzvKMJhd^WBoWa8>QA_o&nBB1dMK}SL7_Ca7zcdS25k%'
        b'($DJiQp-r6OKg70AGlLbq}vBln){tpeQ9?nO){DFx_%j6St1ChmKVZT@R2ax?CX<hPW98L0<xH)8utx>;Hj6;q)|JEzX0H-2bj!8'
        b'&Njek6^Ls2V9Aq%w1gHJGpKE3c@|M_6b4j~QW<`Fpd9!un)Lo00z|oq2o%`dJpjdx*;lOd`M#VQDc35vCkH$Z%cz9N`qm%7s(NFD'
        b')1h=7mT6r5PKN@J@_xiSD6Qx>hBdA+&khv3v{6By*Lh@`ef_a(^#(8MtmZc+92?cDL;<=YZIx+W0sx_q_a?qoWggx<XK>SM#g><r'
        b'I<@?vzQ7ud!qZ4~u8}1%KqjX$0DJ#NDa^a8lB`}lmZyDh$TTc~k{~X)H-RdR2WJ_Xyfx-<T=m8zn(dHJV*X$J)8v(0xnRB8j}17i'
        b'`OS*jaU)evdlFt6;l~0Wgqz+W&0kAQDyh*ST_e_-&IwH7Rg#O*f%;G<b>j?f-hff7@Hm#@d(8L!PO71B;}@Q=v&?G*dSSi&B^NPh'
        b'orV4I*7=Fp{aYHNHm~U~PgtfpdC~gI0jD;@BfWz3-3#;Q)D6%oLo6>>)>$gHk|SH~r>@mKU#W^xjof5Oac$H7C~0|yxT+TW=*$r7'
        b'-u8bIjcaBEMTe`k6mT|glHW>hFE?gOKzG~x;DDq|LU*#+SG)pz05(ws1I$Jcs<N5oVxn+MlJ7C(VAm=CNNzbr6y6-)O!gZy1?35O'
        b'sh3D`x!<*2T(t>55ABEpMH|)7j|W`)t~mjUV}5mG8-2>RTV`eY>Ful@&oRW8q41+!d+Sx!Il%PuYCq)OMs|V<flugJUqYI*oW|0u'
        b'P~}pnZ5CBGq_U)RB5G&4^$(b9=LD>V+AGsIC11ky1njM{{yP2*AFEGyW`C(_x`u6?234S5JnUyBSLoT61C@|pSVOSGA3|8Q{hyqB'
        b'!1W@cs_GsyW{9%}vHe{)k2)n+>gVoE2iapwXEUgs=%cE%hOD}eNRq~WziH?0{d&+V{7LoIjifl4*ss42bnxinBwKa#<96p1>kw>N'
        b'MCL!Iw$xFmAOC%NTR^hTsV$vkRh&PjdMAv5Gh0%n@ju#G9UaFyeviPk#FEbH#%`z;dHFC)Qact+->u1tCWu1GIONbf1Hh`j^ao<~'
        b'io$KT=oNG<Iw;#$Inbck@hRG38n`pl4Hy3UhF#0n?Gg>VnY?4$nGrlL7#LO$8A)_{0$>u#$f`4bZ1E91o5`S%c7&?>sC>(|0JoHr'
        b'5}5v~4SfKJjs#Gf8j}0Sq<!>57aY<v4a#!4<YeUITb4uuEh1xq7LoH}dLXeddn)TPx?O^vMHWM6_g=ED9Qf^TtM`6Z9!8FCQI{J@'
        b'?{)0T=vGDH{)scU6m<01{@o4-wc~@aX5}WE!V&1hx8pmuY?|&7@)6Ykpt_+PkS?-pQIuy;-V1(6qxIFG?LunmrmYG($FfD8b;}P}'
        b'?VSPa3EEWoHDeYbUJh%{?W4dY<(y`VZ06?eN1cw4@&pp++D$*fmlJ=7`%~oqMSgRmA5Ye=5WYiGg)+bOYpfezb17)&)D0vj-!rm+'
        b'zwjYh7g8^^hY<D*f`68~!sfjdw5umuuJ4K&xcNmWchAwhWqEnd^CbPkND+SJ7Auy8dqRl#w?a?89Oj9Zejuj|2qLDzVompc=l5g~'
        b'(|d7i+)+A&lMUF5Z2YrGKJBifoEX%ol<A{4NVCCq;_?l>Of%~!!<4D#ia?tlQYTPZ!8fAmVMhzb``NgZ7Ce8ze=_hNxSdzKE(4PA'
        b's#EYyGd>bCln}l#f6|agAYgKdm}cFW-y<OTp!r(}3i+Vx8~!Z|;&rh<K4abuW2E(~{&<G5e%^n>5NrLcKR!%l{iI(^5!TWEcveQ+'
        b'64F8-p|t!m8i}nR_s4s_i~ZhuzJG7nKfKq2_j*XY^Wf^648l(7?#~b7?I(gn$k6rj8NoYiANRG8&=vj+BP2CV3SsU|lplPj%w3by'
        b'{erS*`iyZYDq$pdydNaBlOzmrDMYhYcVrSDHTU-$c{+&jZ7c-2zx1nYP>O^izQdD{KAmqfK&VOYYQsd%({FU_Fy<0QGQ@hYzt)`O'
        b'vNrb{a|J~P<1BHiS@P&YV-CopKs?ec$$RjQcs9gOOvmjIe@t%FDQZ{e&4R=j8((Gvz!2S0XARVO>5ljoi2Lq{S3`N-9q|N+n}3Mw'
        b'lmLA-4;}H&A@B-bjsSXuG+}~)B7;yQDfmNQ{;Ytd?WfayFEY?EO=cjRZ$DCvtLTR?1oQ^@Zz}gV1m@Q<g8>5mrk}sQIA;t<4McP~'
        b'czQh+tkDz}_~%Odp)g)jfiY4W)tX=S<0(r9floJaGZV7^9>JWk!oxyUrO;|W%1UJiZwW;NeP7^RocYg_eX<tPnu(Lu_i2c{dH-RV'
        b'`{8~_T8c?AnOWcX(QjJKbM$>p(yVJZ-+w`tEbr4~_T%lbU_++&1-_30ZGBDc`@*^fTT(@dtkM0@THyPN^ol^6ViD1CPbw>(lU<Yo'
        b'kS)(yoO;6J5W4mRaM57Hy7z*(%tKt}1aY|-#6<`yA=OW>2mlse3GhD3p|c^HpY~acj>0^UH;*PN(VU%Eo6B3;{sF(Vlnx{G@9=X2'
        b'+5}};_s2;`x0+M*TgjvRyTHJ_`5Hm+M$tr%1D}GpYWZ^Fe(SA1yegTfo}NebCL3d4M${X3hTGSPn+$f6ve=ZKQ{RFlwma}%4ABS+'
        b'in=pn=aaQ>JpZcoG6KMZ56?0w3L3NzY6*{)v=0kfZOR5=O-~DH9`^@jip@jMrsbBGciYp67V=0`xF;;i?$}z_qfos?xGx<&EigYM'
        b'VgxW%QBO!GvL^ieJ$vrsqvr+{7Y38*oJ9qv$>k-FY<|qTZP!Q2uLL_a^JTGrOj;%%DWze|R&>4+dgPF#`ln=aoBEX*-3|6PCu|`P'
        b'$?Q_1g|cS?yT@b}hWKBQ^Vhd{UQ<`3ywwZj%g`EpPfwmbe$;*9sN<B{=@6Q4`9W@^U8Chr$9mpA0eyf$T#UVTo)TD3_3}?Y_g(2D'
        b'tu9P-dyckHx@|vsMn<b>(a4b&%KAm$w2*eU9&M3W*I-<AUZnX;FL&Umok_tf=u8UNd^8XMacnOkbibLb7X)+u%;!i5)lQ6V+OLMF'
        b'>X?9qtUuvEw}{J`6y2{UVLjts2H~HA#*#lCMH9fLpBPUF#!8ir?ScIszfRN(oAjM?tqc2tOhWK?aa}j5CuA)`-BtrFq9c+Y+<idl'
        b'cy(au(uxC`xq@;PRaUxvbzz~ul=-FR_q`k&Y)5yUnlGbQw1})?MCA#Ys$2Go3?P8cNmZw2=uL%;|LoSIeIh!qMQq)Mg+^B^Q=U3H'
        b'U%YX3!b=+=@nuAW7A`R^)#7{fQo{kwhF)$XwonE0WULxA1IwsQ>12d~Kut}HbZ0?Bx~tA_E2vNZWW07|XH=7N|I3k<CcNlsFQIfF'
        b'@maOGJ40etuV{$blJ&9Q$q<S`HSmQlLFCBYy@JX5%ukC<Vbq3&5*|<S-~40GDf9U@;MWAZENHB>MXamwf3miArA@U}xurhTodt|q'
        b'{JPr3AefldRp0o5egpUwd5g*Mt5my~CaWTVsvd?Ma?EZKSbv7y{sq}0ctsGqkChP<WqpDcid|0lj>(xJg{pZ%li15GIBH;ck*Ev&'
        b'b3Y9dxpNjB?ep;m4DrJX&+wmHTPuz%A&b#11rgH_)0`EQ8!5AUxwxYl+7w{h3{qNK0YT@G6dmP}1cZG#xDcjGj~YQeqCgBcg+a*t'
        b'^Xs^rnQCvb+LWcQp*GND3IJh1%b)5C>K#@>;a1~&^FF`sd;he|NSWy2<iR$ZjPPH$78VdvS9l$p`nqqrDJLU_pld0=ga+DyH8xBE'
        b'VeVGn{>vo%2D13#EF;03t9;JsJ9BcJnDLLk+IP`^0!0KaN9yk5mz8(=0OjC%6U6V`9`0h_9rz(y-o77D2;ikl{cm`^-*@t|6n;Md'
        b'9M1IJS-@6~`G4i}|H|hN--)A*$MJaIzNjX4*Kprn*}VZ@5A;0WJ=jn^YaQyV-WmQQ!OH<NbI$c3&AGl{A9y7#&_iF+WYt)3od4Xz'
        b'wf%dacKsWveRFw=G-L7)C^`C6mxF#M0#IEESc>Iqf>2{5$R-aU9-QSrXbCf@`Bih=<k>xa?mc~{WgsJUulsp-0)M3Lm+kA;Z0q4R'
        b'^?_tUO^iw5pI1RbfQ|VBvVaV-?~_{VdrnifqG?|hkeBjU4`-e36^VGvL3ZVy3F0BXfopbpagXW?68PB{GnrD@htt{U=hkAtRp4(5'
        b'8;RyN_tA1+zMm`T1C@ejUeGbPC;DJc1=Kxr6tC+&*2l&LaGd@J%}2GC2-HH|<$=De>3cHi8NqhV5tAutd~>;eZV8V-ZlK+j(5`v8'
        b'pIh)R?H2slu1~?YyW;=1UCoc}vO=QXzz!>0$m)ifw(yvGSXZC7HH6o+`JVL$by`@%434Q(J6_XBiRy7`e>y57RHp<67;!`2KC*?>'
        b'g-o8E(dSNvL8BM@YW)0a7U&n<V~Shcd+(Clco?&%2PKv4VDA1fxw?Cxwe>nOix`oLdDTZv2Jnk<1w;a`UXw6J{C&+5;sufkk9vkm'
        b'FiEx^+w|l;n<|D1u6LJ=^~Og<sXBjxZ+d!&(loN_U4qf2@J9VPV-VtIBD*`anCf`VVxF2nclYu>h(dtX3X+Br>St<B_M*zfG?A<h'
        b'`OB##Hyu&?uKAmm`9ck##grzJ;`@mki|42ksrcx;tqW)}A#!y&!1wpU+Ss%Jf?0ARJ~!e<E?JdE(0jKueuT~6=tYmV82YxC=Xc)r'
        b'h84fYiue+ayV47BgtD>^k3zSuQ{9wpeNwewhQ%)P@Ye-OaBb5?pA7t$het^^gkrg~y(3}p18IzIvC95!ld$<U*D$Q0s<pBV7_sXi'
        b'89ZGmV)OgGeG*VLE(J6Ul}rMi#^V|(p*}po>K3<<Fg6gI7l+;y5%*)g0ryr;t%w2r`zgQpeLtoj<@+Sh`reOzsU}hi&)+E5id7N;'
        b'V$^dd=Fp$W?=ZEaH|uSG21(R@IgJng<3JmrFJF*VfAp&^;72G`EZ_7&Yytx>V?b;RAk@^m6QA5P2_e$_n(lKPRZVTLod*RPO?Z?|'
        b'P-mx_!t1Jcdvqx^&7Km%^|y&m0bcCYr39o@eR$Gvb%O#%K0Uj)Ces;51V+C}+b7Yz>z~G}X#vb1h}?l{(=rI@zD_ZJG;wF@%G%t2'
        b'Etj)S^(E0FbX`dq*$8P(>+Z;NY9;>(_ZWm64$Ak=zra0)%*#=(b3F5I?1iYf*H7ROo6k;Y=Jf*KNc@02H@o-8ep!{hqc18OZLo0w'
        b'y5OTmo~zAX5NXqFw4jgNSK|}<d2Vr0AZQi=Fdymn&PN%+-P`NM_aQ+#yH4?RUeU|y0$cq0aMqDj-JrDI?1850Y?dF|LK^z|{pEZ?'
        b'YzV5TnnTf2GM%&x&z?R=Da}P+avf{&Y^XGvtXfW}nw2=;a*5K#q&N4+3M*C3;X$?!450)kHq2^WBlQqYmcm4W3+bJn77@s9p}neS'
        b'i42NR#lft{tc*Zaq`&w-=>KnHGF^}kjEbv!;?DHxVbOI>R2BJ&`epKM9SL;#n-g@*rZ*}bn<{EIaAa@Q5YUek^s45L#V<lv%$&cc'
        b'3f&{dZ(n<(Mj5}BiQkA$4G`Jyd$Pntd`%umk7zP$a5_!E%Zq>ZpuFhi6UTZ$Dq`T<9xuMZ!Qel7#5ei0uY0`L`M}?M(1R6*uJnk<'
        b'{9BjBXOmT}eAcC&s+PcdUmsx$t8Ngnab#-!Oq*xq7EFWWV`{ZW?P?0#I|(kMg}GB%w|}hDN1hf=*Q1&!pUeN_8r&4-+e@h$slwe<'
        b'%JW^^>7L-i8-|L=>qx|OuIC3mkwk^!wTXbL5L8*1Kn?Ecp1}GHkaNOR75?-sT`j_ZHKvIP?(YA$2bK--ji7&wG_pfWW<5;g)zWfw'
        b'ld-1@pCWJU;#z`OI7tfE|5tc4e%|wg+EqlB&XS`Z^I8wYyfk4XDPuaQUE6A(b31xY3uqanmnor$>iw`L>k|Tq(juF(x*gAl<8`Ds'
        b'14=JYJt&7JbcqrWy^XSe(S}`nu$Ki7^q910DiafBWU*ydNli~psZ$KSUw}9Ae$0ASSMuC{%PO!S0Gp_O7F!Z#(-kdbOCoHfv1FEo'
        b'odvrJdr7#(3NtYbiW*758nYC8Rnc>&j;SZr%PGyKo?M34-WLRQ!|0x%PFBvN4HHSMP*oEUb9xmx-NaG|>uM%&Et=5-Vb}v=db|+A'
        b'u6@@aZ1Sqb-F_1fKupA}_ICOSuAoQU9Mmr*U0h+$f9UkS`fE5IH@klzm<hKJl@tF(br$xZ;x6prRe9{3r80tB+7qvz!Tqe~Mw*nn'
        b'uO~i=<UZ&|Ff8OdT$#R}DJ*X10W9p<qbInxyZ>`f@Q-c;J={I5h9l%e9&!Q?S;s>j;31a>AnQ7&eo)%)>bVKkJG=j5OYu=REChG%'
        b'DSS_1&$y%A|E>pHdpmc{>|ynJ77H~JwJWrT3+ri+?V@`iLicbpd+ZyDUGknnJ+VvHV-4+TkOu6w>F!Qv9O`BVqtQYsL1immyYR*W'
        b'ReZSC!0S>lSDf8}NrO+67HCSB`A~}_dQeBf(Cu!>^Ir2~`1@{<F&Mbj?G3*316^-o`~_K`lxyv-)x%Cd%6!W|at=^t_4lfZU_;RT'
        b'gC9VT1N&>f;jaty%i|z1{@sspKL37-bu6qMx4zNYDYF%w7Pflu9EX<9mj>-RpnuL4n6C*Rk{KO@DT2y~6Bn<x6yD?4T@^Yus(Jgs'
        b'R2Q#V7H$lo$qW^h?IFGQ5@n@@H>SjDf*50!>cA#HUa0<Yldmz`r)-)}y6Xiak2TqxrzUPBDll31F(kw0UJ{eJVoMCes;Fv1k6y5k'
        b'(U;a<usbZY7|jp&-V-oC6m|DebROXF2zGrmQ(5wt?)jp%nF%juL*j3{0`z!BHlN}>LyuJ{i>D0^#X(%0QBiwqBCzQOrTHCbyk7Z3'
        b'^QGc1(Y62rxwu1Z)=(=LFCKl3Whm8|7HAEAp;r)a*L9y3<~Hl@qGFi9rv!j@?mu*+|GP6%O=2fk+a1{YTYrxM7Ojbb7JO9<X}dzY'
        b'U`vHxx|vOJzweIxisXKW{oz#If&EorOf^xR+;6ABJkiZ<>$XV&ih<vgA$u*J&it+u0#0eZIeP-rsUN}caKxS5ucwRtyqkNr3($dR'
        b';FU90xYhMzyH+A){0LXv4YES5#@%BJzky3f0p2G7Ci0yLft90I#!0&Q+qNjmgz1#;4Vh3t^`SLYw`{^!fVv9`xzD?Pm~dPk*5KKj'
        b'Z)fxfm(>lhaQmbUYKcL^giaP{<D0HK+i<ylXv4Q;!nI<$jo~}mSa3%h9HANSWXOCKOKMIW;pPX40Ka&`KXr{phf1!OrjQ0lf;1?I'
        b'>!yW(1*q7r4}^tR2+imbdb^$p(v#45j<kp}7!;`SyJypfv%@p#JrL(2yElZ-1nu+MwU}m5A}}eU8&}mcU4h~y6BsbXBP-xXDZ~Wk'
        b'HUx8H7L>kP4VWQWg+$3eySUFgbHtE9$3QM(_=hfxML@8i=SZ44djaWvkVvULk`aDZvYzyP;@5rdcYWYb-`r`Wo>jd!Bfq#fzf@6t'
        b'V`*`5vC(^1Il#WwW%53Nen=$5#`R6{t!5=5JGF6Lrx)+29zB9SiOzLFL7VsqG$P=-vl-(U@C5_q4q{WbI(ydA+AV0)EbBsDH=eN`'
        b'>jGFGN{5(~&SNoq0bm37=B|&d)+Pk|p>=eNa{J~3*`uMv@UBsssOO#ufjL)dIHoSW$IVmJ6*H0YT-Rw?pO8*8zcK~A{#@3D4xH#0'
        b'PV@P%NX@e+9H-Fm=X8*|m$3-9JUDJCPak2lu`0U{-$cFWFL?4u3zha95Nm7n{W8@Cxph@%{TidRmCmVt4xP8`_^xhsa{jMGs`d~g'
        b'bmNUKTx8ZjP#4at4ar>r6K=qCJ1nMS>?JZZ*&^<NL{JYx2<|y7*ePquZs1_M!{?zvw;nmSNeDsIlOMnsyPMimhSpyG;Lf?5G6oot'
        b'=9gWlqe3Logte7vSJ6@}0_<Zly_NpDU!~No9^mf);XB3M$nLIYNxHPly{qdNvKGpE3yI9F>vSx1CND@ItyC^f<9%QbB(ENDxbWG!'
        b'OEl4kCBMaz`(AZF+Xa!oW28ms6HYj~)v)SYFJS^M|FHAffz6~Ob~=R-X74o!`^u+4U+1=9dcijxCQ(#r{0x&&#uaxJ#uMDHFui1R'
        b'7jF)5YK6{IO7j%@<z|Ia?vXB7L%E_Z-V9Jsn}d9VIU(Gtu8}DCff!%W7XIjXyk0^_J8a3$;a}*+5dz=TU9`;i_iJTqO)7ChX&5cj'
        b'K_r^X?ovV9Sy(>+rED3uvP*TZfHPvuwk$qM4&;y5lQ;+fN*m7otSeqca`*F5VLq4JwNK3DV9eZi4T+@t$y5tE&9uF`uf8;m6lW40'
        b'Ie68sG>Q~2Be?XgQau_doDRZw;TmlBxp`fZ^-7F>&PV5VMSe+gdW4uEyrf!1aH)ZClIqLQ$n_%bo?w()02N8`0wVp{Bc_O%)ukdX'
        b'g~y8eNo^MQQ$83mb1x*%$FT7|{N_`FS)LIwb3cHY%Y)J8H?8try6ujKxkD$q9-D&1^b4I%ZE_9;GsLao({*K-jz<X}TuWPP2p1=;'
        b'iw1(ef6bXlfp&lZq5=TSSde?NGa&I|zs!!(EIH1JyRxH5*j}MoU=Vc7sm>}q)8QsNtHy)>{DC>=$BN>&f@jqmI@FE|V_b^s)7xi%'
        b'+vz5-iN)q$@#<k*O2FF_x3)7QE+ufVdvCfRWo-ul32sTIFyQ;>Himx}OoU&4|H$Qb2K70a?*iq%-uZ;AMPOZsEc|ng>U|;u7-hZW'
        b'Q4_jz9Tew%X?%yw$RILA(UI%Ps{awhWN4Oj*v|>rkfo9`@uQOROqgxuVP{h}h#zfsVkB~d#OcW4gZ7ZcsgH>tU2f+iVU5|3iSuUj'
        b'k=hPm$jFQ0yetz&P2`)BQmM(246%&k0+W`Nl!_m{m(NQmgA8LJBjJ+7<j4zDnI%mv6(@BBB4K-~FG8_3)AjYWPn#TuKrG1%|FqbY'
        b'DL@(s0<`e`al&^J36w7CoZbjDy$T_-_cjElli=ScmFiC1nP#2a0l}s+-!V+(ZXAIa1k4MsJt1>y9|rx_?dW_4sXE%h`-F^jQBvLD'
        b'ZB`Qt^F(U>7*m%tvFTzu<hNF~B-UOs$3;r*nmJHne-~MGi?BNgdk*3L><C(>1yIEL*ACtxWGtSt?d$~DZ}JIDo_l-ehRdXT8>XG$'
        b')56Y5%4BXUCJgck+HCjlI#u-)t6kpP<bDP-x&s-kWxvR>M>N`?9BWqAHLESpi7d@(bH{CvY`8OZW3fI8D*T17FiW}xKtF*HnuG0E'
        b'Z<V<>V#4c~V4NjgW0t!&bYg7|Q?ku6_j=6#6UH_`tOR3?d}%Fv2@-yZ343^WWK^kM=KeV**fHTIWEWxV4*`UKS6lC1jqw_c7v4<L'
        b'm&fB%v_<a4orTV%EztJ=@NKi0?|ul2{vLzXPs!Z57~6p{o$G3CqdObpTQLs*q7L4fh=a2jWJJ<X!fp}z$Im4;Kil3SU=mVxw4-2e'
        b'Zl|LeZ48>2wjMDg1h*{rc0v#X3xff}2c#!l+9EK&J&A<`m=r9WCQcQVLxh{xi5}U7hIGjKP3bb3I|0#Ig=nOS-65Uv3#9m~CEZfY'
        b'co;Jb37ZZsbANFJ;<*@4ZcaD9e7g^MEsO7PBo<v3DEhDM8WKWP3rK8uCN}I$2t`z7gabhAy^YArg2<;u_U^`V5-isg8BE-(IwrtW'
        b'A)mSzg1+5+HDbEY(;ZCM_aqj)eFO_8{99(Ks*(qDozG4Ex7;;>s^9RLYyLIUkRVsR!`HoZgztbH!mj6e9KJjfC`-%fXx|kX9Ros5'
        b'Ziavy7J9kwE7|=re5RuNN|s-xwp6MuHERB=k}9c~1%U4zfhmam1x<-zw&|*F2d0`SAu#1zL=f^li}T%>5ZE-g2qEOEybVDEpClw;'
        b'24gV9%-+5OZ|j_PTE^&O_?02=gLxU{83OTNrrhszj2=*SH#f;*8k{o1iFZ-N6I1S;N8%Gmw+)B*Y&%{N&z-&#!o2$Xgm5h_ZxQNN'
        b'!CrHTao=Kd>*N!%kyFD|A2o1nphe``GBsa3XKd+VbUNk=n{p(ot8NG1_n>Z`FML9#S}XP)oGcs{f!dufbgWgUzje59NKg*j=ogQG'
        b's@fuipzi70sJ?#Q5!j0x_<K@?I)Xdjfl*bIWL*Sqy#LmrdX6xP2o+>~f>|Twcz^?PV|s6az79S;3|nNUjzM-?tgdyYA3Dr!KN48J'
        b'Xo?Ld(zG?1g)9AmBKOPiq6X+yDINTtS=B7Ehr@n*Z`$2yS`bx@&4uqwo&EKZz^)cHmeyCX;Qg?rO?~k$*wT8DZrJ*8_-Lo{%!kVE'
        b'?(-vW%42N!xW}nQM~UVYQ-)&{zAL9GV>q$q9%-7kQ0qr0H%_hK%qk`NZELppa;9Q3#W$zF*Yrl9AKD-K@yuZ^_rLZ-duKoV?f)PB'
        b'xbKdBZ2s4Ny!e0UN7nzXAIt9S2Xw-9napqyMw!5wC|;XcnCo|4B7cE587S+!?SY#NHR3)QEn`K3>cw{#nG1FPv&thQVerG_D@J@D'
        b'M11FqH)bZhIIl%)Et|%-e%3&ZvS#OpQLl)HLq;CmDPPeeRuIFnC+93$(EyqcnhV<0uKiQY5S29sxRV(oLAF84H{-?5=>!8AN+`3m'
        b'*`jkz#V~-oJTs=b>SH_uHIT%?buW;yjgQ_oz#>pdxyL$MNL_yj>{-SsP5NPmnRC#CZ{|W^>ltyF^L6}iCd+++ICB>|f)_>VIzW^E'
        b'#ve3p*^m9XuC8M5VzPCC!obhSOMdr99k{vf3Q;u^u*-_peL9J6@yzd%zyltnpx`v=`*yOh@pjs}+P0=})kgnm(jydz$Nie?ZQNVI'
        b'rm`*~?kShs-6x?<>qm$2apOCOxf30puzcU+lS#vDF2OpSHH;^WV8R5>Q?P?qwtCdMEt8rHZ7sq;AGq`F!Sm#xJ+6dEd8gfdxC7?5'
        b'^*9gogSLS4F}&t<s6+SUB-9Klji>&lGJZE=q%H6j!IYtP_x=uN0fBHl2*)EJxK}$|#gnWf$s-W3c-hhSt4a18$x5T#jUBKzaW`~W'
        b'n-1T3+U>cs0f4__+^4;!UwgldVU#MPlum>^{Ys%s2yt45PvBuGeWUFcGTi#_>_CgF8G^dIdEM+!?ItFun>_^~R}!y>1(TdQDFn^)'
        b'c&W?;?XN=Kh(O<m78M=__lF=xj8<fTHpztD0{pxK;6{&t4v)%0M;nrDXB*3GQ*~1AvJS<dnty=Vq-<?gTI<?)HIBsWjg-5j<Fo+Z'
        b'WJ-y%#U1#)yd;_?tt>MCT!BrXhZMZv={g*o4Xrk%1*YJ8ldJ}>AMO<J2LWzl$7yT=KZpsqaR1Xm3;P6%1m<Q@lOQ!Z?F=+r-p1ci'
        b'N{!CylNmM=Ty}@6Npv==qf<cFwvbjcHo1tjk@bSTX>v%gO*eT4-Njj)dI3x!-_|J`8DrZ?iof&s$+)x*^J}8OT>_dsyRhRQ<Y}^x'
        b'1h)3T5_#4DarKZI7EibAY;rKOg*3Oy&fd+(=$IDLbqMd)aYV}fZM1>au2R*Dcq^SMT7-tBI28W20_Xn6YnmZ$R^n!~GhGwY9@Eo8'
        b'`c_SLqS?v}{~9i;-M4a5v%0-g35~3r?Bs1_#z{`yey7nnAhWoc9q3w6OBIF*bZV-wo6yW@<K!JbG92=ARGWcGQmvHoAL%(Da5%2_'
        b'E=CIxiK|nJv>mv*MQC0y2^_6@ncyc~OtaZA`2z=&?LmW=QlMHX#H!cZvFi9?kATEQ^rui)So<<x6(*_c?jP%3J3MVHO9JgN$Y}wa'
        b'd2Cy3u1)`g?b#aD=Kidmca#xj^?A_o(fITyYWVz*+Bu(xdBd-^DeQ^MG;g-mHBt-{Ufh5;5b4<$NdX<AQ5~+Uqw*V+P>4yy+w*iZ'
        b'KE~WVI#;l3>EVE@9BfY`C^+Y#DW@(wqePKWpwDh3#d8T15yh0lN;&=%;VjUbN|bC#xV<Ed^P;Y6eFC|!;AY!HGLz^MJuAO7xwyEZ'
        b'pwCm-L6o1m#X1C=%66+tXOtesZN15%$nGG$dZILr%zB8panBmAy<PRLv^0VgKR}oU)$ZQ57O`uy#I9Rm6K?KluX}|$b3hQd^uAMA'
        b'I9Iv(bq_nJE|1)^X%nSNjp7>H#ibzME@%{V#D$WujFRvRCCaQ1{iT_Rd+D>y+@BE5&6RB>ue9Tf+XO{vRIz>5o+FQ~WwY?vVtFLR'
        b'T|d0$lGFs-w3pgdPv1l_{E43^{Sv?aV{%xs?~RE+o*(}%>3!c{vZ<|UkL%+2X_<Rhdlrq)kK(Uqn4H80=)&86kRw%iDTNgis;F^R'
        b'qZD8Cm#lAVdR^XZ{$kwyyLR4QV4lRgt=x|GDs-U3{kFa8g1=0-r;sqs+Oxk@RkEhdDXv$YCv>COPDOhb|NS2B$@VJrWyzJd<MTEC'
        b'|6TZZ9l6aq(DLc%taLQ0n}lb21e>-iTDPdT39B2(Dv$peX`eVtOpI15Eu6*jrp5BSMMz7-r9{jY^xcq4*h^wOCDE=}iCq)p(M0c0'
        b'eMju_w@Bz1wj|nj@G7f`Mwb9mVsx((DmVufjg8^U2_dX~TUOYhjBd7s#cFSDe!#=s+YZAc*+7cx(W0^WrNe-lO#-@r6va4nF|t(4'
        b'W#Oo}q!Yfg<7g6@e;9s0H+Y<PCj-B^&Ws02CX~+h9k{Jp{IjO*wO4d+kGmHI2v{)5o12K#r<L47gj5E&f^-oRyvf4#fv`ML?%0S2'
        b'>&97oo{^=Re^F3zm{p03L<yHk@g>5w5x+X;P6&X@o8+tQUn4Qb3z}x>zL{qp9xsp{J}v7LL3S=?v+>G(Tj^*N_cGnr^UU7yK(09l'
        b'a|;9>Xeir9iYtg+0*`ZUB#;zeWer*nxAC8VjB(^wIMdfV=f)UIq9EsjM(IB78MRRAVWm;2Z*5i#G^=-fJ#YeFqOh9q3!1R8PUVgd'
        b'EhCE7UUh5hyXrqEEzhgj0zDmLv8K23j|Dx4eh(GvK#teIxLZ7w<1Zpd50s{M^m1O$*?%4$?NJWc6s<P(xjD$}o@nY9Qb6WN=t}!X'
        b'q<yw@%~uhSJQPhi4}CV^rCLYuIsQPAI{T|gYlp{q=v$mKQIz9^!tyLN01Z8=J_1>XJiCatKvo@ORa5zV7ORQMue&}Hr8+>nL22n|'
        b'11eaXP;On&L|NU3p=H$!!TzsidIalRq~=d2kS;aq+5;fs^4rzEzfC~Qs3rD1N1S}>w??5j)%+B);3Ky^S^@|NO!ofYf0DnFa@19*'
        b'o)Q@y%OzhaPX0EmDBRIX<>!mm#7K;e$M_rjd9KK>A^_CMr^1a|fx}JZ7X-352C~}|z6vW6o_q@H+Npe_Xw7WM{57BHTqZU;2(G#f'
        b'VmP=v-7vTte57{+VHZ+)(jsBun~|31Kq46(JMvd4Vi(c%`8)A>yiK^LjG|{{UncX{C<dNW76~8!zHYU`vRa)aeMFdVQ_!<MN!zv6'
        b'?VS4)=ohd7^vL0;a1>RxKBok1(HR_H+_;Wlg%tf#bvrc@VO&NPlpzjlfWh(zqflfM);_gs$Kky;Qk+EukvLB`<Tvgv*mBsuOq5@w'
        b'u%8&9rSz=2qDl+m;rxr=!9#vT$Z8Zuj;MRCk}XlNLeUS6h;oF5)Qt3JJsH%c!irhDwz)Ir>Qv7XK>NUnZ;r4a*Zuzb#oQA(UDNM|'
        b'f}+AN(`bq-#{`qkkf0)~Vg$6zYV`12uW)k2{t%J%VT`IO1dLAME_HKrQSVMEaWmR*6+;Bie@aR{&iH%9BEK&gCnre0rH91{ejvG+'
        b'j;&igK!@b-+g+DmA+~_(f2bdbIo+YcvP<#?`!WhdU6GJI)Nfg>cti*h`D*A?mDismH2%e(pQ%_bga}c+o=KnO&WP9}Sx;8A5?m7B'
        b'nP0cjF&S|LeleXwjB<o~*DJYrKJNjKlZx=IxXLGQSbu-|x9+A)bJe)}uEV_ikfI1^TBUn#JpHx@!~#Vp`ox%4q;l$nu1XXYl+!`F'
        b'M0}#q<Y-M#^sK288L3Muk#yJf)=ir#fF%Ml!}^uSEj#>#4CaLOBRBtfnSw9cV5Uem%-mE!<=yw_;`}#u7kt|0%n`2HK$p*Dw`>sS'
        b'tto$yh*=G5ucTC*w}FpDmP+#8H$6xgPY6uZrP_`%;g*Y%N3(({4gvzu1{%M$M5H-Vx9n=cDNmoQMdW*Rg1gd&#|G%0p-fnCxowR&'
        b'rC_+#G)s1{s-)G;4dCQ2S5bQ}k=)U?fZuErL`&t)Su*_CL&Z4XQ;Ato@R}P0fl>6Qky%`O8=snBHg5it+j_XwD4`4636s98;4HLo'
        b'ztJ(%B*`CaX)87>)~Luq&f|uShl4~B@J~FEgxO+@IvZ&YcS`cjzZrM`*@O3MN!{244>#4UD)>{YQ503G3pG+Q?&UUU^X0Zc54V_S'
        b'WyIw><3z5F<L)DEygmNwK)v+CZP}uSoSHD*W8-cQpXIwU!H;%!#lj0py-}kyX~K7Wx%6R0ex`b?P`Ts%;!Fjr34_?urSGbXln_XI'
        b'4p^-8xQH9^@Mj0a&GmPso83l-z)3wzQ;r9Bw@^OQxclWm178LjIPxXwjq|7f-0h4DzbGTU8h^ZOp{sb@ZRd-bFJQ5(SbvMCkJ8<9'
        b'b@Vx<eNa)e^MEvFwTlz)UwBdcKYo0S;JxkVs@lZY{V2Eapl&t*Z3Qmh3k|5y8N@?ZACmbdMAlmO+26N?OOu76g!^}Ggkav_Gi^eO'
        b'+VxD^)5P6cIl+IYRF|R8FQao-W$%f}3EBUms$5?{Q?%+I)TWEOpPBLblWiAf5L<qd3Z+c?f}B;f<ORucdh-))bVTv9yTczMge!;x'
        b'A#64<&;E;K*3BssO#J8F+&nj|(N))`a72$y>@u~%h?a*CTcT%dYECZRknC7mVOoxk#5X_M)+Zfu)Nk6ahO*W&H*eUER-GS*#6D?@'
        b'#Hwk<Tc2X@ML#HiUkSaJrUG`0q@v{Hd#deZRuYkrc6Vt8Db^4-j3Mz%X}sZoQU8zCSBL#Bb}JOAQWK@dziYx;nR5a|#(mzKe%5&r'
        b')8n9ORMK#@;jc@g5;~t^oqw*jAJa%%4H<{4zJWrQ5x$0~HayKbzpA!3X#@cfhtLO$X6g_hiSmBo*W3<-XM0Eenp=TzjQ3N&=DR?6'
        b'iTAu;b2Sit&HI60^KBp;>wVX6{rXU%p5?aJFoq1md&aN19LPK9J?+={0^t_#DZl1IAp95aN#1we=Z9EEzr?6Y3+_Ly=MOm+DA*4L'
        b'hMZ`A{{#Dm_YNf|UpExV3YQ6X^|l&X(APaX8$arZfk&w6a&HC7{SC``T2r{z|Ce%uhiKAJwC9KKa`r)-j!I@L4Iyvx4q`0})Q076'
        b'PUoNfb1N-nAL_EU9kPEYxDaxG?;mJ6o!k1d`YNcgr_@i^#>t!a|1wt7c}OTt2)cD5LW$_5L_gQspsuT{=$pw7kJiT6AL^Rk3poze'
        b'zG{d%%Q$3`bqa%HCg0=xX%cT|-U|3-(li38NH$Em#JHg>X4mc@mb(>cO77Glc5WUhKgl*V`&eFJ|F!G+>3$5P2{>=-zm*8I%N~N3'
        b'JkrIjb(Cr@VRy{rHniGvJF|Zs>XFXbaSJpxd_$buIelm3=|elNz<{yj;^aCi;QXlfvE*IUj`L&F&XAG~lpR#B1^6%-TgzB%{@$PR'
        b'>qAa*u|XU3gfHYbvyZ<6WATH{&iboEwNKguG<XaKo1UF)uLSHy7b)%1#XGtk4T|JNYD3QAX<x%Dr~BtfQ$pupS^bax?aG}lQwKEI'
        b'=J{_lfc;1HN;26Jx9fpJ_KyVY@}-fWkuSqS%a;auWLMfWoH4$w9p~==1NrXcL!htBPOh)C91si^d+hV_1_GZE`E_1(IGJpvASGqV'
        b'p-nbHa=^pvuk+}jkELCjY1n51u($s!Y;N|UWDA8}sS@)Zza4mh4!ScCy{;kX!gp7u2dG}WKoBJP#=L2~Wrud$`hWO(AF!yZt#Npt'
        b'KXVv{qs|{3`B%-HVPHV5nL%YVyO$YoK(u=S713MIg+UO_dd*C&=)E(?g2CuZhe|+%GY19+5CtkzlU}qUGP>8S?k#VB%%aS)>-Clz'
        b'rsrGx4BGpBzwh~;M~8j(*?aA^_g;JLwbt2tEiwLmtKSM$K<K_Daf5oa>V3cqX82;5IJN<k2TKmi%IY!o0jmf_t^GYjB*&UT2WJiT'
        b'XIO;{;{P##xQ&1BpTvJ-WFGpY|8pMB-7M2TIago&pJl$-kNX+c@bS%ZKcU^h{gO3EdwVpIM}Adv@Z<fgGP8W@U^>6`3FYzh#h{=K'
        b'Khv=B5UzF{c!8`iKtWcSTRsI!t$iX2O0kJhsNj(17}*cytaIr|IqU~H0|U3pb?oVGHl{CTk~}fJ5AEkU-Wc0&0O{90R$@H3fBvBC'
        b'_Y&S6+%LkrDgA~Xc=zj(>Z=3$_giJv#?YuSK7D|nxfH4y_5FBJ?4lukrin1VG7woK@OUzV!0kS;G;&D~uYuP6Cvkx0Ir93y?UrrG'
        b'*Z9BlZ@-n#AK!D|C$)#w{Jt-C@U@4P{DDj_@2#D$_I-1}%ZUb)^9-*^w_M~jlW~EAI|`_YTJ7Dbj%Yr(yjGinLGfZ@t@a*X4Autz'
        b'W!!xr64cQ6#D3&G&llZ?&3DMSZNJ?!-|n$7|B;N(-7K;xQlxa`f@G|_nfYKOv#jRa<o$MGU{~t^S3;+)YKog2J66|nDH7}8(*DQ|'
        b'OMIR7Go0?>vbf<G&S2e)ubpCh*Q)(?GOkiL4Rqu8$Rx_zqb^QIqASj>jd8V~u)lE@*nH;83cFyk7sV77?4Lz#GV|6<^_b3H^k+&D'
        b'r6cnqv6(1Wp6e9hc*R5CHlJ9hDK<q{Z8}&?y5}RFyVv^w4V+-@R;6fOYzIcZy`j{vwrx4!(KdsAXsuLxYYco*GcLJ~W|dpFMr|@L'
        b'W~Xm_x*?!#hN4A%QbCh?BP^~uT&{?|y-HIsPi@b+-A=yaI`BnShT86W$M)v|m$sxxhpPXRwaDNqDsgF76=YcP%c52CO1Ot)-F{6>'
        b'<=T(kIx5*jnf-*pn2waE2mUxfIjJmhLgyrXtM<zW;3zpD<`Nx2Zb37AxdT}P6OoI?_~2FnE+dwk?QfhZJ~-iiQ)1_>+hp?`@Ni45'
        b'l?IPzY0WW7_G7R)CC=2cjkQ-=rWqXrY#i@G#$WqD2#C;`@vZ~BOI34Kf-Sk?6_OJ)x$D0%rX7IcVkXa|T7}KykJ1ZW_07HueJm+c'
        b'>ETKHI|tgRX@D!lXZY++qT(ZfFsHuR_*EZIAl@}}(~i!P!FXJ3h=5Y#r^tma{Q^QH2;(QXAnGykuA}C6$=}w*-}{Vr9&lNBLynpg'
        b'sNxQSx6J1R!kfI^;N4vR@#SSP#uI(>H<`a-X4AJ_WbMoi*$zFQ82?4#d$Vs)M6laX1nO^6FZ|Qk;iP9?)v`%@Ue%fg1tbTM5QLxl'
        b'do(+m`4eZnPdgL+Tl@-Yu`2M+nUTxV|L41C{O;C$vfe%*%%bEf<9NS)`TN#V+F(`}9^SA2JHsbec@A9hKBd5J_Y@0CBc3o8Ehswh'
        b'uL7Wi<?k1M(r=G_e>K-q6jiR<{grw!St|;0=AWd&WKB|Y2-e{4K6bjDi)Tq|(e`^3&<Y>>enE)>s$+H04>F6!>M#H(=y@C#V3xn{'
        b'S#*zivt(B+@GO77`d}$Ev}ghLf(>J0FGHboii&dzv;5Cj-3Q~sl2l$^gl{;sv&7T}mGQAYj^hn?Vt-0+d>9avFx<8CW5&N$h$m)s'
        b'W#HRs1_O;Rt3aJ&5B2qtfmv=&n0s{ouBtv@?iXb)ed@sVlQ+5a;4EO{8mkRkgLeKePF%4y`sV)V3-kk{2*e@&fV9(Z-Br>D%|r}9'
        b'c)N3`eT9AYl2sL(qbJW`7xZCY5pIwoOB4h7ebr|JiOtZsA+quQshLaWw{Fq^M?MY`LlZVJ;nDw7^V&_ZJe0K4T(4A`fi2E>1pm|='
        b'dMFwwf=hPy_sUV9u%~3aUu9rKc!9u@B5d0?CB=11#}luIrZPA8wP%53Qya;eJCI))2;Pswu>TGPf`8iWAZz;2ti`qS*Ui#pI!JdT'
        b'sysxx8&DEeo3WtMPcly-manzPR94{_g)GTTLx>FkDE#7VYU2;a>3z1kJ`f5;t+M)(m9q+*x+V@K*;C_I*4pVLEpu7oN6)h4WeYj7'
        b'UA9vMgr41v<VY>5oxfz^DGaLtG=YR!9!R=_Xx63F#uvulR<PR3`6jm&TZk8a#cDI-jxW`w#*xhDpa|^axLj7pstoN7vsKuW;CI*u'
        b'S#UY-<FlxCkYqN%7`>bt2h{O8RFb9teG!)>?$5D*Au(ZhToWFLnJ^At0zNf60H6D~U>%0B6%d-q1-Ie!rxF+RV;KJ<nV-YtmD-FW'
        b'42c3UzJU}>bj>mxUOu=3mwglx&)~8zOBMAbt38-b*8D?aaa;}j-BXOh4Q+vjZnFo^W<qx#h6-Opg_^Krd;<`C%8)`c2PIC718^gc'
        b'AWn?OeGW>-*Wm5?k&QB#|JfbEasJ%_u??p;K-$2Gi5Q3FP-zFop+Pe4-v{CW*N&Yaj^sdo5D#${B#r|6u#4Z;W+d3fZ(!nUN|9YW'
        b'nF+OCl#D@Wim&lN&Udvhk?w%xYuU$tOa_#<jks_qsHT0q$)dM>CEo@Tgw3o@Fg4WpC1YS8tAeVTn-u0hkwOPOTg7b09q%K}t4Se^'
        b'uKA1Xx~mSuH<%P7Pk>q-Dj@}qW*!5*Z@ZjtP_PLCXRX;R`Tlz!Z?WhbKNaQU;LsAHvIN5}960bn3Hi3lufwNht1`wTPOvo8R7%E;'
        b'`yyHjP)!x-_DIHckU@xKR`n%-jBmXft8fvHOkm@Hioy*w0FO-=|0B#<=6bSbg=GA*jEtGCDZ)5c{1=FhEQ#Tl%WkDg_600YuyH#r'
        b'4fyB?@-2tw70flsR|pB-z#CSsi!pB?VQF4YC*jcxIA=k-`2co}!AOrRlzh2RG+y8RS9xsXM!uJPuE;ni%4hq1zsGIpyT>>S=67yu'
        b'WS_GO=F9-e*idT5J)oVBm_a+Ap29s=X(vbSKrCf`L19f-%PT+0lqoCeNsr*aMo`wjFs9(4u#<PYf0ppn2XHK!)Qp5#qbyZxKfX|x'
        b'`qEar*p?Z1#hA3uPQG08Jrp~KtD8_JtgAaPRb&Qs8)GAI4!A){*F@5BZcx&vM$++aP|{-}=|ndu>B>lYp&OKRMI_zf{!lWKk#v&#'
        b'eaR;Erkm`+#}{yR5{3K<U}hul!kA6;%0>3oj7r8Uk#t|pTaxjoNP2(GaqM$_;b<)k%U3A%5Lq)9B{|?}<TaG)SXK$h?*k^ON_EVr'
        b'<jI;&#6FYy8tJY@l^&9LQI@k=Y>^lVL2)(vac$sx<7d4bw-gA?eO0O)B;8#oDXuo~q46KRoOYG_KT_p!()~2RG^9H2;)Uth=CNPq'
        b'J7LJwV?+)jY$6ejCoqy6*%5j|VMtfw4_33V>15;;Xe)MBNv)P-zL1Q^BBhdm+n`x~T)!R7YJ`{Arg0?lGRysu#0S5`ZM}wj$=E@b'
        b'UV&i^0<8NMUd7cqAvt~FIjHG=M>6)xy)e-u*dKP~DbgK6OXKjn<C3wX7t4_r+S^T^?9qUDE^r2K2aSJw>ERxY_i3E&_iIK<5Huts'
        b'-3HKS@xj#qqGmucHuSRTJh#-lYutM$4XdwP?Zq2_fz1a+c_(LJx&dJ?w)NBlglBMHJ0xRG?+~oTqvNwk4&R72)wD^77dvpjb^`od'
        b'J~)oss)ckSAN(4(1x#sMFPnfna~EJ`9SPuXgklsf=Y>Q9?$fi9@xLM?b-Vkx{C)_-d<G9RFCN8ko|24}@{pt|7+&JV|G~KVq2x)7'
        b'+mo>BBLEK9JPvesUoTI-!(wM<BU_}4jT)Bo`kYBBA*?o}ssC3uL1OU26L2j<%?7CVhhC11W7bQ)CB3^KZMip)25gPq`j|?LYhJsa'
        b'X49eM+FwX_nZ(C6cby}dKTB*LfMD*IjK7Oukie{#jCTXIy*RQG>ply6BYUiI9^{n>q8fA@UW=+P!H6^KB%=-59A)m6e0TQlvfXUc'
        b'NN@dx9LdG4Y&}QTERtAD&A4Pt=>;~84Jh}pT5tOHn%@J?#@>iY1-kn&$=oe@IVW_FQv<Gkb<Nw7F%HJ<4+c)b%#nQ4dqvA1xVZO)'
        b'cEyIPm{d4C90tQrBeO8BQ{^E}q1|b~0_3!jcBcRf=*7g63c9oc$n8vzOmR=qBg4=>A(u1L?j*^0qsOwzogf*1?ZJ6zw0nkR{H2G}'
        b's+j4L@p6wmKDX5@mW=<A3nVL;X_E0`52mW2nst)z$DUpH?gR9A%ThMMkV@}tRI@QaHEjCM-Uethn6r;v46`WgX@De5Aas%4;XShb'
        b'*%%xT+xU48#xo5g>Gdm^Cfuh_p#9I8pC@gk!I=F?^=yof=$&*cG0%rsW!O_kVAVFEV9Bu|V!pE??iY%n$5yiz`4XFsAQ17u7NiPq'
        b'`t>}k#G&aBuZ?5lfvO^IR>!W|#(LOz*^kmpRQHD7aeZMPgZ**XMta!1n@;CncYhBu1#W|K(p(uD*Wh+i6JC^CfC9mqe@~uqKi_9N'
        b'*T;?x(S4Nf+g|ycOMQ=@E{V-cuA^4z7Mlw9^*GP=-Nz0o@EN+#aglqV2+ruEeT_Z%_$$zMEK3>Y$k8Wmo)andP!&@p+mpT6kg21)'
        b's!}U9U)h%sc?$GOJ0m8}Wi)#vv`t|<*dq#4>?R7I@p!w>LDgsUk-zzeuo~#2XW6R@U73z~yZ*bUdXUFvPXji%sI5lY;5SsCwsJIP'
        b'QhpqD$eKZKxCF1UKOAf$dq?&SzOg58VAQUBXJ-a>atLB@-a9qFM0|Sp_6=0^1eB;{9i^nHB`K7WqL$oFDM@OHo>CIjlBxX6rMtvF'
        b'Y-xO8sjsvrV0ozi9riZf^62s4n>haKturIW;vTDYv)whC`ju?H#TOSU#)y^Y|IL%5_5;_f*x}(QXdF0L9X`)^Z%-fT`iOMJDg)*v'
        b');VhDU;2EDdR(!{I>*4$x$#PuWmZ<UH7l34mz0?MmE#Et{c>bCFZs;|<eT3khors@1R$?<7cXqHTIpJCPO3x03u|h%CSG``R+|>l'
        b'OL>8>)hc*Fs0~~&Zt5#;xMAGfH*!_N=?|_O*Y}P5EEyl_E7n~%R`rcsk|3ve*{{aRK2RHBANAedqYfJERcq{Jl)a3cubEGT=3V*i'
        b'UTPm1I&(wdhxu}R^+as{i|hl;2l=2im(iTShptPQ9-B$#kEqL@$O#WYdgLCE$hSeF=J(iJaB9Nhg+<tH{>wP)PYBEDAXk?{q9?Wa'
        b'D<guXZPAO@fx<z&Bawvw0S`l6{q{`G_H%bXr%5+aE;N#YrEep$UF`06X|lF^bxKxtU-n4hFWm)ZIV1;K8wquQqubBI6kV`j!uQu6'
        b'@wf$eP*1oq9pIw06IL!A1)7`E1IJ_WxzR>lH1V!z)ueOB4N&e32Sw8@eonWTXjGxN6S#&Z9ar)-L%ljKupZ@SP}!{c!Y>1-dxD?$'
        b'nCB}%V;YexM892Q9PM7fQLZU96O!%vJ_`|XmS$7*opEXMGav~)qOu9w>)p6tQ%CTsZzOE5b@wmU<Y(*XX{BgF?pTIX=;1o>2SYxV'
        b'X7gb+;N)_;`YcZup!h5U=aU1L72xg;_sBLH8c=`%1MH@mt8a{aBH2RSobLVIXGvgq7GfqhIh?ZpPFw5EcQ5|$cLXyg>*@UQmixZz'
        b'BWn*Q^83zUi=R%m;*m8r<a@4Lw9I$wVM>OGiq9lWi3wY~90`~_6LNuUfj44;O_&+n)g3wg!wWChCamLy*J~3V<%OQw=CA$4t|z-^'
        b'`a$y8Q5RN@kjPK;H)?#_x|{vsQA})+=gs)}V-UIh#K6!#oU;+<ob$cZjh(grEJcc~hfGR|M-M2V=3kJztMV3f3vf~ZzpLz4PTa^h'
        b'QmSKSlD}5FI@J+VT=cVVHFPSE`BF*(dF+o#hp<rgH_5jga@W*ge`kDfN3GVG>d^ARVmuC`lJDN`@FDqZk!;qSkIkC0(B;eR7US-7'
        b'Gsw3Hs%t^I^|>ISslh&peOd6b6sb-Rtn9&#|FFwc-`$W`CT|rH-#153`S}!w;&Ps)GA=Vr`bDALyRXsC(Up&2f3F9(lOwmI%5ofA'
        b'5??mO9>P*e{(i6|CZ$T5vhBUdeQKVgQ??ac_Q%_~=#-Lq2dgaMqVfGVhE!q7yzA<-D$v>4hRnD-GaYxNG_veVnT;csfT%?bf#5I5'
        b'<~yze4+&Gub;&lp+xO>vcIt4{R~`Pq$hT6;_L*!TRY%r*A>nDjcby}Cpu$Bs0#f(}MIiZ_tbBG085P|iZbf-c`R?84{#cH6xV%U2'
        b'Apph7Dz(Td$7^TT9|@Bdv8P>*QE=NuOCU@#5kG*&%V9hBQ1MH$GsDmgSZz}fvU88%4|f!D2{VKRhTP^ao!^ByZVP)Gu=1fP^7Xmd'
        b's*rd?f9h8k4cm9-^KVV^_Ip7kL}R?;dA&~I=+M7GJDvi8NVljcmQJ1SzWB6ewf~Gi^5dApkN&VD<3W<0A(~LpTT*F?;qnfhUsr!F'
        b'R6TokRQ=-?lN|J6w$lE_SpACPP1kWFdS0@}D)%jGTn?%s%fw`yG-=Y)O0=^XtEIuP$pBCaAd#vr=5FZU`n8BAj!qwbTEmTA^vAMH'
        b'x_^^ESS&Fs?qTXhhth)MLfyj{GGS-tM=#bdD%RZ?8JG0gzZkFeI>^Q3;&N77^JPR90M#k7m;BtzTa-8VvoDb?6uy__O%HJbanuic'
        b'eiB|jOY>N=%aOix!=NDb5x%#>lQ)z&sQ(l$z?mLpZ(F(nWUlsCC*5vE<bomUAg6i%v)*H$^$vX28~nUCB2@UE3B#7!vg)L$Nl!n?'
        b'X~gyv*jq7(9`U!mRgQO|dH=oMW2brtPW1-=+Uxr(uDz=|%%?q6>>zmASpc7nhA8td605@WaFW-g`%n5cgY7ASv@ICqkwbmdnP^lz'
        b'ah-|8a{;*QXzC%&`>*#Nd%bty_1@s2Uf&@Zujj(NWqN(p5EZ%P?JN5Y&z_4t8V)0w#12v7Y4W#w>$l+b^d8&SJFu@e*wO3jkl_{L'
        b'`k!_uvG@v!?=d`ZurpGjE0fp)&7U09q`!9YH4Sgsf?*H-la$Z37N5T!k=wpR^0>1UJ~ds1A=sVBc6T`G3A<^ti0zx3fw~P=+M2al'
        b'|0Yvt4-Y)s3$$GjGWcfU;=W3d@cB5zuP6z*2;OYRk^X#iKrss96ZVmR8Wfj{@@E1lw`jB?OD+_mz5M?wbOfk;G8W~c(ZaR8B~PDG'
        b'pc$SRR?(+OToIaau`={?sz<FJFaS>GGZG}&gwPjKrbiiE--~Y#pO)(1bY_Nw(P3Be9o6z#^WxsTHTyaY$u!7NJdN%ry~`R}R+Mzq'
        b'Psg5DHrIy+X%xKP)!$!=U1qE)e*XIS?tew-_F7jT31d6f#O@fsFgcp?5W;A+<C~SmM{dY67xtf7QGDY`9C&iCN;p1TpUjeJv@x?6'
        b'R;#i|ORscH`eM|fizS*JE6%KdpRgVNtnN9adbMd?@qcK)ebzgx{o%OX&A0Dj!hy6oEvv%HA-2wl{dgPecL1|=_>SSxuBX#zi+wfs'
        b'=_Zye8L5A(FA7k<UnT4wW|hC@S5+3*+<<8xK5F30$UqtK4l(}w+1R(kC{euQmqb7FPiZK+&IoTRekbSupi1;_($iZH-Enc7X2;eu'
        b'Tj3`>5B_ZI@d9=)oGJd`SIfM|xv`ul6*b>VXdR8Yp}ap-X=lB)^2K~s@t~pxIAOsn*ki%CW48Wr()Ur9$1<lyA0~&e>lnEMcHb`C'
        b'f%j+-_OUenpsId-;tKOdx@+zmvm?giL2X=-u&v-Vwf+e*;@gsq8UIdVnY9U@T8OpUe^>_BYEJ<K94z2Ll}y0z(K58jJ5ldZ@@e*O'
        b'q)9o^_EJ}x({3^rn+VZJ1JQuEDC8T)CRox<qOcQc&Q|HuVazN}R#$Yq1x?RF%Yv&49Yo2pv5y>tqkKM5Oi6Cpx#}jJ(m_<wCCg$m'
        b'Pj1)jc)C%^l568hcQV3q#*0&pPlkE&HqNL3ZNZz_aPkq&<0~xF^<31ZSlqFdQR^07>mz;t?z(w-$nRtmN~?xb*V5rPh4wi@=kdgz'
        b'P~z1m@yEfBy5vhceNny-aB9~;PtU<{bmD7e{XJc;Wri6xI*^Z61{PTu*{|B&cyJS6!Jil%GNC-eDp<Xtc>CBQz2`s7+tQO1b5cTK'
        b'=5TaVnNPr?S~t^JR-AvWJDT}PGQ2gMI5tH3_TU%p^Ku;4njThpDw^n1{$s(kF^hlQn5<gvRboBoQ2g)-&574W6BBz3W5dJGY>(VO'
        b'fVJ?ebT2tubu`_cP8GkQ@M}}HJ#yJUGbQh_%Ox?khkFiMroc9VE&JM(Du?aC9#&z=DCSg-^5SKnXfo08<|S-_PpZwBTIv7H7}teu'
        b'qqFH65~YNvvtPm10V0A-FED%h6Tg61Wt`T<#$q!)RvfK{%{5mfqe`xqio=8(qq^*z1#hlzgM3fjG9!;%kS=1@3lg_KL;lkf_9x`V'
        b'sS-KRD{Jjvg77+|7>}8)KXGH^eZa2f7wM+2Df7Q?`UtnU*u!jG>U_2D-X26|c@4X6h6iD_28&hxrkj<u8CW#ASQGk4+SgOEde*yr'
        b'ijYWk!>*i1<i42b*R<q0f8R6f4c0wG^(lP!^vLRSaZmJZ7p?tt@oVxeiuWabI^oZc@n3etY+K#OU>CXxQDf_@HfLfbb3vN*W^NM^'
        b')04Or6tKjc<21-V!>>2=_iwI$cW~^(XI1_GSA(~IbMed@E&Dch45uuZ4m<EdOk9a4vR*cbZ&N-4Za0|Jb6kb+Jt!4<JQoe-5@IeH'
        b'pi%LvUjn(*$XC+6QS9x&4BlgK1RdWB454`S&!P)q3X^%m{iMZJKuuI`B1hclGH*TTA#0rYOVaUU%E4o7ADw0!r>@Rc{jk8lD8+IA'
        b'<-9wJ<7kKRpec5tYlH$Al{|J%!5_cOk_Rn#wo^)!2TSt!(aV=D7g;J?F`sZ5$;{^8haW9|oaqCK!&h)bvtm$~HC|7-1OlHw>IlLr'
        b'pUe$CL)ndFSH>WA!HYr`I^w(wTQ<zst`wiR=Fnum+|N&sV|8AiGjgtBtcs1#s%y~ue_5E1tJ!e}FdLaqj9<Bu+3a^{ax<{>>AoVt'
        b'Sbo<jTQn+n#2X*zlqF4d@TG1TTHjPWMyy?*{~tu1$m*Yf+5hSWb4o%`>z}w5Qk`)BB2A7RY#_EYqp`1Ri0D(KX(|S#dsSm678X@L'
        b'dbcsy?L5@YmEq7<DaY^RlIcp%oq!V_RLXqy%F+BmBVm05JFy6T3lzHV{8)wS#28ziW!iq*#l#F8%#%C*%R&1;o;e0}tnG%1@2}{a'
        b'f3-Yykb9Hm+?OT)Qz;JR<vepr966GV8gu;5SFXeHBMz=(*ybT>_YvZdQFh$ncF6Mnrw2<OOsQI*vh4%&CqDwi+^#p_h3Oy)w{)*;'
        b'h$<}VEHdA*>JhssO8>@{&}TOW1;VzvyEq*UQixR)W#f`bo$$K9pT>Shpej9Ud2Ry^5R>~73G2@O#)k*X$(p}O<As-*zk&{xlTwv+'
        b'dE3;I=N-nBJm<lZ-1!RTjFi&&dp1-%H<o=G`$ij+!p{#;zMt^mj(jYEUJ*wE7j!&dVk}yQ+#f=UA_yuQ)x0lRt#j;)ko#|ux7la}'
        b'l+QyNxs&=Gmu9O*`X$?yP|-((-DDCKNo*qaSJf-~ZY}P<pM*JFADMYr4OKYR)1KJF3+1e?>kz?Gz>vBe@pc;3Hw-N4hSDc-8QJFb'
        b'Ugu4D6!t1*Cuf>dT!f6--CX$`OZlfRqq95hk+ki`tnRc1{L_wqUUGgI!d@|xqs&8BhE&0Y-M%9j%=lc%cp_B1V@gr-L-i|4Ozh(z'
        b'8YE4Omr3K!Yxo*<MbWj;TQ`JKI`sOF75sJcbJr<yO&>uyDauJwPDr5f+b@UShQ*9^obmrbtg0e}cCU{U251l=*(8wKfJycrH3+X6'
        b'l2kyKh2MrZeMk;YN7X;~udoizP#zbE{#VqZFg4UK6(w8r<4AU3C-iS-lh_><2c*HM1V~MU_QUJ=u~!E7OKehq|4&KlLw%C(yKqUB'
        b'{uQe61$`O<(Wmjz`c*@W>|3*>g84<Nn0u|_@QotV9YQ}ao(E&(*adF=_$B!elL9fI+49MJkwAFYD!erckSQ-#YP^+(f=cYk>OBR!'
        b'-rOY(G4Cmo7KAz_&nY6nWId~hTBqP=D81Y1!Q`hvQ0;$-#_>oD3r|;cNV~oX7vA5+W;QuP<5Z)w>s4}O7TT1&n7zAYtt*+&+N#KM'
        b'D^Ow<+8P|r(PZTs`d>D<w9T6ie6cY{?J8<!la?low@HKC(ue=2bK?{0;#@@@$sa(w-VbN_)w|=|zQ2XD@|?MjC!LRWQsl~lSZt}$'
        b'kv29FWu2$U`L3e-aH!{3KY-=21ubP`UGBp!5<Pq@>}w5g%rPt`EjWyZ$Q&MDN^+(<oQ+{_O_a;zH2T9X4>BGJbLGyRuvd10yct#{'
        b'ZpAm#7o#VdYEDQl(;bv+(q}07@O~MQ%pkt*B-=6fh1qEAohvW${omOWJ{AtMG1zvSiV4ov5ynC0veD5A<6R+<!?%G7V>=&IVGl5h'
        b'A0ruSn>E;EWY!e>Wiyglt1lr~5(g2+;eE1^Z|==CfL~L{>)l*DdX3}M!I;iL5ufg7BDPJZJ|reTf$z1}g)Nk!XP6UgU4ws)<QaY8'
        b'ZVCe=WqUDC8~+``@JI&W{o07})Y3vX{lj_lwtv~?b@D1?r)F9G*l9pZ*w+=pj_Zz0Nja?<I{{n!2!YK-7BNNpZ)^i_U%z=~^MSBE'
        b'@8*5KsxWu+?q7g3z;?$fGuLVC9>(@_M?fHMS=Rd-H9TpE909~9FI)zBJOL+)q;;gicD_T6R0Sq%Kg5|XJTf|xrbuQBny*F=Y(aOk'
        b'ROF4lh_rp!A)0WX9b^PVx83pv-czW&4`8&0RJVej5D&=ywU2Ab;P1j9+#SKayyb`4FD|ivT7pkMEw>CFd#7Viz!!z_X>`~#BTk%M'
        b'%ZssW9NE*MgSJ2j2viRFI&+I!ftz<@WGRN$xf!HM804aO!Oj<xS-}Y%4AJ);k@&r8asru8_-+duP`d5wkd8n&hOFT{6f+op^75kh'
        b'DJN2%Fd!9l#P>O_Rg%(OTpU7$jUA#H_qIFbW^D5*VgDob=K>a#+C*6%kz>Du^gjzYoG%{JQuibJ^*7Q~SUr>RrYBYr3zMxI>9uq2'
        b'Vy8pfYK*<HWjs%tmz<SFZ;d5K?n8OUvj!&mNXIGc;7xV&gMsr>R|&mROBYwfq|w12y4V=tl|Fw+wsexC1fY9?{tS2&Xo(BWkk$3d'
        b'9x;|2;6o_kH1y8bi~CZT6M|O-=80~Nd|+Q5IhrnfphHJ1B8KC#MIjsucOLR<ODqMY^wt-Z)?IW#A-yu5D^e<fK&rnfU7_B%!cdf_'
        b'ED^JYCjb%INh-b}O_t3I0VosnO|3HEsN#u8J;6?QPXm!03Wk0F5dw<oPycJ=J=j5UUv*Bhk1RPQhi;a^3^Jr>BtlPJ(GleRDnv{a'
        b'_e@X(DsyyTbaQAi<q4<*QvvV0=fHdSJ{aNuKUm{`xdltV;My$&<<Qk5BY&6j#8E=-1C5vt`TlZ@7<{I}BpIxmIYH7tPOved6|+!='
        b'Nyr!mrjcMxZ!j22VTDiHlbp|VA<h)0k3Q~DIU0`YyhWxnb2Y0oE@r?_;nQ6w@!!mZ1bc$A_N%EjvV)@LQ29|5l|khzu^sPk5=+_F'
        b'piEH_`RHJKtjkWp<Ha)`jbWY_;1oX6WytX2)2MU34oY8s-T82rovyC`kDayxVyU_)d$PV>XU_On`aCF}o&iM{%mr1k_S>lsf74Dy'
        b'&7rcRsHhAoTj?D%ow-|cBqO~B3LeRTy(ZlcrI%!!^h1>$D>%jSG2Rj?cBxn`w`lngwREhH@SSRhVSV_+c6K@!6~|IBoMG<v*_6Y!'
        b';b-d{+RCZz8fKW&6lACkCPU$scCL`&%)cupqgbskw~NcEw#=z}S$~$X)0S%9U{X7bT#n_345*dFl$NU-o%&9NCBFKgg#;z*j9tUg'
        b'mQqe_<qS}4=@>|$N>>@-8^B1|&A(^0`tl2~G?<qq%p+jqS+rcA{sRuhi28^~VAs{(yU$3RuqJH|b5^oP8@86W+GmuBGfLT{Ax1db'
        b'VBOF#{F-`ro*GB`$_Vyz2CLm*&#@GrzdG`1WX<ZxXka&pSOSU@j%$4ftl0z|sZy)cVNq2qvJ|K$N?b@dzq+UX%{<Qjrj&a`CCq(<'
        b'A&{debHPu*Z@pRc%Bs5&by`O<1OM!Rnjqhx;Q7gQ`Br<xqhdh<G^0Y^=9Lb*q^O{zygrBL$bypLRhwGYSU9VFSk^~uzV-+|hsEo#'
        b'<8PBL(%^7Kt@+QS4`BTLv$KdsDbq>Dj0(T$EK!u0Q&!MG#<yJrIX4IUm%C5WpT6Ot(Zip2o+;L>UvY5-{G42&S-rBf|0jDztV|s;'
        b'ZD6u!PgB4IkV2Q&SBSCoETT)ePoIALCEI(QCDgAKg+=X$DZ803>**-XFxV@25HZKz2%hL%I%XI&_;PTaL=%^TKmcVvmyrIIEAlsl'
        b';2WL3<(Mroa?Bvan<`Clw%0mYGC)~Tlc}~zX{V}Fb)@mtPQaZ^wOrlxQfD9<?GFFzj7779yU1yF?eE;do#Zs>X%<q?U)L|Y?)95)'
        b'zLeiA;hMRcn|qC~qmvVE1eDeF@to2c*)t6%HyihM2Jk)q)cBNRO`Sv0Tb{W+rs+(brr8f`qZ!*-y`pJHef?gpQEBKg2!@|vH&${1'
        b'=4LE0R>dZMrn3HX`zKtNPR~<@+;eK4o6;4h@<p}t%D5Q6w|6_QWj6ded}Q)&EnmdIPA4=QUeytYGJOBtdAP`~tk&z8<0P^xt!T^y'
        b't2(o#2zKA$`I<o7?NpwYBBKVYG#jq<H>s^nhEL7~N+4I)$QAdX;>VD~Wv2{VzcSgCmg*A%b~9qpH_<GK7ZYS1-Wgd=c^2sRz*&(^'
        b'3M7`^quRN!ApmbL3?`PHl)?7zYpDLf+9a=vo*=$Uk!Nv)qrQ5@;<9Ktl33~KWwkh<5*|BYGfRT-WV{y-;Oyv@`NqYaY`lf!NkXs;'
        b'vr0qVb}#0VP&Sb>c!8Uu%NB*v1!`%v93OPjZ;bpVwK2xGu#;C-r^b=S1)Vp)J<o%}sAVvQ!)NOKGPl}g?L3J;UGX4*88)Ys#0=Ov'
        b'gSJldNlBRG$uQTJPI$*F(b%Y=)>*s_>k{T`5=;6_oxrRy5j62iE1Q7)rqnnP<SW{tHXXTR5Z@`1Xe=M!O1vgP^OahSPuIyt`;~qR'
        b'KYGoZwmri9fk%L*6tT+|vYjpk($kVhKo2WBOWg)ufocza>5uX_5w9e8C&8!2)@jCnk)EYf5~BK;iY7_$Zbo4f?<Cpy#2wz}w+Ecc'
        b'6jiKmA~Y}&3Mj4k1a^}NFszLymb`k{1{GCW-=z>652!<Ssejn}e8aQRyffPR5_YTxtZ&oXCB>&NCsx*c5s4ec#YD{fR_kWLWVM|O'
        b'u?euZ0LNx2!-DO%&Nl>vHNaYUj@TU=3lx$0-Bep#2cl2QVpclRq}x2A%nTpcqK*Zs#HTLQF+h^|e1@8Yy|ppC;nL0qdbnE?P%5cB'
        b'!XRJ8S?mbpDYFa{H|00KHqY@Mt#3!ih0)<R%Gq}7*dxQ%&AAPlfQ7VMR6C!itr>J?6Un3^N=Y12V#xuG|13GQcFGd<RlM(W{Pjei'
        b'AMHzMXP>ewRayAhgUYQ(jzL*oidz3qTW2Vb$_07pYegF66hheH59kXEF)!kEWc@ZQN>DTa_G@?DA&$nKiZ4AxT)+WWR!RCJzZ}<L'
        b'p@#NNYnNlFUtOy5rQ@W{DLTHY&yZb!ShN-`4kTm#vviM2|M+D$j;{@JNK4pps--+n3!^@mOx%=3V6Vaf;F063p1PK&?IRCi*RjlZ'
        b'k#!^*0_g<sM}wC>c}T-YTaF*N65$hv=JSg!AUDbOyRy$k98+}0v`q|A{OVM{)+%haK1{=OMV)szCxSE9X$!v(9y=kPonAJmRDOo3'
        b'x<mp|PJEAE9EVMR*t`232ysw<P&Mhaeo)KgKA@Pfo^*Z}jQWmbQV`UQdLRYnW9Ke<Yy54&zXx}n4W3OXJ8mI%eq!h&n~3ou0NY43'
        b'#Wg8`WU^j1z*HT#Q1V=v|0%(Cc0mE#+SsDPw}WS=mu9^`0iq(z0uHD4N2x?xeU4KotybDAGo|VeE^gHTMQ#NCv`CqxTCDK>6;E;>'
        b'J${7X7^FY-6H79%xkD4s762&`$3K*?b6WR_Nn77y!nYFFVdJ3Plyvne0o`h{;s@zjmG>sUk;^WX%j)H_+Rqe`qJ3oOJLy5y*yAiS'
        b'`7PjKpXgJGt{Ky^^3=t16n-tQw4|O}5>>t^>f9o~eb<c8PQSX+Kh@V9q)4TF2?X?{CHh5_OUu0d^_@s@dLSseqDXu*<eeaP=lZf?'
        b'{O^~G7Z40qaA#B<2H=H9!~)RMS59+w2VKb;J$-dj9Ig3GLSxelf9)8IB7@gEDn7WZPru9yquv~ER@P6suf&+2|B*dEZlgv{fjB)V'
        b'pH5!8{(biaX|kW@(X0E``x=70MP1)GN_?i63~1mh3r3a4o{B3yZbXqWnv6Dy(5bkxkx3h%Uz;=qIt;4I$&b|q1wXZ1DEP<_DGmcx'
        b'@ja}`4L@^~rGQg&*%n+q0JOC3&cgg4n^0t4np<)H*zzE5()^+1yGsQAdJ^wOs_I7zCU+zJ`2-hml_B#h5=@7_=NG?Lr$q9>k6z|0'
        b'*|*if4nzND7geoaLpig8g)em!Ujumo<2Iv;d5`W>jDI2dKd_q;VJR$*TdZVhSDtdiPgzZB*uDC&=iVfhZ$ad%E8ZK#4h}ZkLBv^R'
        b'1ceS@nnHv)@O>C&-6QKVD4NvKL|L$7vCdN-Pi04g8tKt8n}TR#r9tP4($P_#B8I04HkWcSI+t?eHg$3B6i_S-GCO245S!<%G(aIV'
        b'_w=DTMdc`~9dsqimxqa<a9Yqr(*<)UtmI5~I$HTbK>>ZSLQ_N;sz2GeLS4GT&}grscfLTEdgz^%>gw-GOX)~{6<z&UX%&64Qgicp'
        b'!!M=l=;7a<VeOS}ppozV&Pq)|!5YXb$~M%QP~7RNm!KJnpth+0q~_8G93o#v{C2mA3r3V=B%b$cpcJS~_0xs$aCb%xi-4M|U%@n5'
        b'#N=%UG_zdvnH&wy$Tm1jI$Y%mEIr>fTOP#v>80C-AImV&%)lL@!3Y8`1@NI2Uo>t4;F>_)Trh#}SGAuX(2J$(z3Z0Y_k@fBh{D11'
        b'fIxS4@oB>OrcjVPf$)(gjq~>%NPik04VrY2b6w>$Xwl(pQ22$;VU&IvA9(^O7X^UgoZHdej?s#Be-b&9782|q5q2sos{FR#T^$?#'
        b'Za#R$d1r^6&MD1MC#7J~H75saVY=}}S8Qn=LcReua#rQZCMxd#QNLpfpRUj+s{+Y!wehl(pKOAnXL#tPP32U!!jnzA=mb|basdfH'
        b'WxANB*^zTHN0Xo7D7WjF-14b*SPkV$QE2tekX3O_$E=z>g>8K>mr2Cmk{={ol!{F$%`v#LRb_04Q-#&tbu^n?Ik;wVJEUDYn$^R&'
        b'm*!Yq*`!0k(nW8aDM)T8Bs=VHTuoE3T5B?n^N040vJA#fMSE1JZW6oVuYWFED>$2jV#@6<dKUK3)L{^_5%Ylr6kqPXA}wxko^NLv'
        b'?3E!WIkN72KjKY~RgJ$b`AP&<#apm5OW$7v_DCcaweQRJU0-A5<VXw=SvbFowCtJ_<fB!!DpmCn0Y}qQRs0v>`+NJYzqhmba%uSS'
        b'Paep?Yc403TxUxSa+E5Sj&U8hmW3IL%DjOvzSVv#M-V|+p&dOg*Q|Fg4dH9dHoL&46@5VPisit6i_an6<@Q+x*yATrJl5_!g7K=O'
        b'W%FC|jB_!Nu+VJ2e4>F@I4P<SM<6KDDUf`C^ovHaMB7BH(ll}<_9o*h+YTR<hXy*@DXItrE6Sw`nJ(*hT$3-FVHxpvf+#SNi1EI*'
        b'c4MeL*o<4`s<26oQzf&DcXIfg8ke7JyeP2g-2stQ?N-fTRTY0Acv4l}gd<b0lTC4$@#3NuBntSfjyv)lS>zP@^MubN0Q=TAqK~zs'
        b'u0ax?Et3C+i$0@5p_{SF)_T&7k7ESvWO8Qt^hm-b&>$V*v@02xtN2NZ7!ld*O!7kE34v3nQmHA`FTv)^Ey7+n#+MVus&<%y2!N~%'
        b'b)>fQp>|sZ2EUkco@(=aNO+j6s7gGK9x^%gn@1zV%+{3p4P{>o6kS}P$0p=p8Lq>-l2QNp{{Ejrmn7dvTiI1XwA}7tWGWOkuT3zN'
        b'eGFArMyizMw~GvllpnWVfb@9Uj}h?ITT1<ESd|fwo<&KM%~z5mqf#V2<C|%CqN&I@GWbxuZ*Dt9FAFFM7wjtCri;xQp~-s^yF2s3'
        b'th!uoN~v%u>4Eh2U}n2Vpx3<sghsihh3L!rglq1B$@zYvO+GH31$tshjPVY6uE}HrM@MMbc3XQ1mHGnd-hwIz$(lNp6qTC!kn>^T'
        b'vVFR~Xlfc|{4W8=!zGQe?amqPBjqT?^&P&Ok&VI>8*4xDE2u!$<n7K1;U2Q=pb&{VUyz}Rm_hL4a+(VghIDl?hq#=^E@<md$k@_m'
        b'Ii)YsV}t2RlycVS61=H%R^!VWYf$B>c2{tFu7YF=ku%W7uFso;52P#=JObHAde%f&?3aokzuoz7F^^7-RdD5~Vik;C%2^U$UpX&A'
        b'qj{w9s+jsb$^2a!e_g@{{3<VzBkxKs5#?%e#B-3ZFNnr3#G1SC9ih`A$fy|CyyP?{jpA}hE=QI2d|HR^OVRidep5$AdbaW`$sCi6'
        b'uC`!?z`^={<}vJV-hEU;#UK3`x^P)oZ_wxe2q<y1s`}fF_;{xZY8K@%W-G{qOSgI!ae8*G2Y;Y5+S)`8TW9%{xF>;2X=R6Z@PJvC'
        b'1}D=Qew5_Pa2{~mNTz>%BeA<t4Pv|TfarV;Be$4jTIBn-{0|X;zL&*~J;PmxqD5h9#U66<`#>OB!wc5h=zjctfD#4;!{qk?#6g=0'
        b'9H+s~C-rTV3dy&#XKq1_BeM9<i7532+W3OFikwBJQP{=DcWo=j6)x?x-D}j&=U^f#UtWN@y_R0N#wH5tisz-`3FH!p#bVhrqVp+H'
        b'-WHPR#Z;t}=fD@GIe3w}is+FIQr;#g1sQ8&N%uM_Qe+kb+e*!4m?|7X4rqCXM<EKz(1%hcPN+dR>+-05XIj|=-ZCFs+(k5gO4^NI'
        b'dMi#v{9r6qb&)Z?H6m|8U2)|2Ny+CC`^f(nA78YRyxaC}tNnw>MthfYu+2`ZG8HNi9x~MS9M$+#!Zy+>ny}L%TY)IF(+;Zp`O2>p'
        b'<|fR@B2Aj#mDYM<jYnHW4wr*MMxm`cfL&J1IE(4p<`OMb<=|ptbDN7y8k@sD<#HuC7m9`ZT1A@hn3tjjri&)fD7+^*jUm}9a?Hce'
        b'wQU79F&|luz}!TgCqrj0uq2n8<c^gc@||5GQ}m+BQwNO}JjO2ID{Io7^Tk4o$ht9YD4hS@w(j}Js~KPa9+R<ol3z0vLe8D7Vlu`z'
        b'bN#3-K@^2y&V&p->f+Uxj2qkRq$)H7q@}dGROTUxc~go2@*KGK@PD^X&Y&yV^$)^DJE^Eb&ztm_N=>Q9t7DLSh2lBCtFfq#sM_TB'
        b'fTjV$SCgjBxXzaEq;k-}wICH$)JFh2t2q2~@x&G8W2x-L)_n^=s|-Y2a@YNVO976k0!%NqYpgxqlRcUxJ%iIrdpbf*lCP|lqY-fA'
        b'2s=(qm@3j}aQc1bPkw-e`BY?_Eb~}gzh)GZapMt=q|ZbnL9|Al7lE{|z`Q&s8UKi<jO76k?)Ztb%r2SUmMXoxy1pt@ABk>@MTDPs'
        b'&1^INHCWda;pJSkDpjQbL1Fv{kT=Y|c%(u-@_{FrUejz3v>7v7Me5sq3A~7GZw2u(27VQm*d6Au6g0MBCXzULUXkbK%Phb=dV#0D'
        b')t~#7xrF7J6t1|-qw<+=5qhd;x^G2WKt!VQTUII5HS}R~yt!T4>Pco3#y>zlqK%CY<dFd-b{ZvH!&JWZ;I3DKm<?2+Ob?x;GGpT^'
        b'#xvFPJL8_9gEaosTKPtTU4V^K6?*RS_%JeGyF8$63+mg<xuo4i+Fl5TsZfhFNH*2~(@3-ip9A!@5#)iHapbppy9BGSqFIvTIRI?)'
        b'ua|9~w}ON;NHrM@G>Av~*O2i)dxPG|s%1|GT`4H#!{2d2R<1p%@@0Hq789wCPCZN3Jcpeez95Yh$mITY9OgvNe*t5iE*Zbvi!ZU>'
        b'h6(vUQsF=MvZU)Hg3C_g=&UGU)60>lo5pp>bDAGpvG0OqH3xd0hpf358Sf89_U5Q_@slz@{J=k2gKL62Bd7FT$>W(MPdfutLG33b'
        b'<3vmFQQ{pu1)6}OFk(Eaxf_R3$X5C850)*(@amWdtkiR4jTsHR(F&S*28maOO#1mC3(HcQTDB79Am=?nO0lenMz8{kT<#*87?>AC'
        b'Pn+bUj@YuDQ$*7gttfKMDp>>CYmrBdH~5;LCl~tH@sWg3Kv#c!afQa4gPnFomZV-qM@G@PZ!gHDIK52Pb4-fmjV=RHg^QX<|E5My'
        b'x3-C^v)?j@Q7$ED<*W*S$i|gYCV9ok_b{O_7h22#igdJ*-~0Bss)R{_U4ULb<Lf9FcN;7<SdlXKn{4~py}$;c`R;}Y0waFB4htoa'
        b';BY*qiylpSB`AgKSA;9{JI?sl@AX)gc3mc!zeq(2I%=F8sg^tm%vxG8qk<fHOmbP4RwZQR(!<L&F2=IqYNW$1x8<Tslb-DSNx(++'
        b'<k9tcJy_tR5%ZwLYSY?{<AUux7ER`pHLpkLGSx$x|1L%NzwtBt4(R_&Ayr3?*ihj=KuAU|1!1ncz^M=rQ_U=da!eODYw}ZZ6Xvj|'
        b'zS)w%krqr&W^^%GV>7qrW6QmVN?O9DoAs5-8I?tB%wTqsetlHck;B+!=OH3${qM@|-+MMiU4J8gHwbghFC1I2H@uFWa%L*Z&&8@2'
        b'jKs0Idj~<c`uv8AN@Azu4rV9ieN#V29$v^xU1N4G-3yGdD4D`hhLZMTquumUmNe%{K>wDn>+Levli3z1Xqjt%Vq*pOcKw?-@^Cb%'
        b'sP$hvr|s<{2V+aCH;?B?uskEG%ZSWxZ2N?;4(70>+4--%e!O7^V(D+!DRy-UyW<#to@|P7WE5||KIxN4YVle2ifOi6dn)K)dj*5A'
        b'S<d*)UrnR1m$WGBqnjpu;=CY4&Y}yOeNXQF?QFTNUhq?&o=c<pC_ne9GC(SP&j>TtDeWc%^W&=%>Jpe3gp%@oKej-veJWO2w;)aR'
        b'EY;{3TUD3e?Wp;;^lWrvbZXNDUsS8C3f{sY%+;@kuHolHWN?$f&ho1om9I7#PbujDN$=hp7f>pAQsJ$$&N#=u9Zee_64DaF3BZZN'
        b'3yKr2k4(ng=1Ek)%~vHfD$|rrT%^x^WQ*2W4hm-;sJ!)SN>^J83O4^x5o!AjzLF4*1tu~??dXBY8QYP#f~QgK+^?ZRGHe;FVp4ws'
        b'&2{{H<F37!nQ$6b>wTJ*k3!00vqUf$HajR*byRnpLaed|ra006_Mtn@G-`G<ojI&&)E#LWjHXlfoI4bKdFEIC#r2NJgqdnCNw>zq'
        b'xj?X5H}{d2<b6~zr!f9sE#1jHH#ay}sEg$}2R;ZuJ2M2AXD&9i>v@S&sq}+r;4a~K2kUzhk9(MIQ5n50j##^AE(cZcx2QB4{wK4#'
        b'k$+1pbu&IWkB#=3jXJ#5#j%vZflry<cCnAD_{aC4Bg1qQCrGj%5Fb8&;(VYbs@zhj7x?5m3;gOL5v^>DFVqQaOrOH{7^ais!l?YP'
        b'0zbHt7qz^}#vB)7@ge+Lj2Y*oxdUF#iOq(@<Z%wbBag)1yPmhYNX3k=)18Gaf#eOf@y0=tw!UE)d{-k1r$9J>M=p88dz75<KJL{`'
        b'KSVqi6a1h>_U^9Lm!OCXd7jhNJ7nkR{<HOY5kGV=Yw|vB3EYaq=ldL2gx=k&`qXZ$+{=+)7rSWv9NHcvGU>Z(rXt(y7S1&LGB;PG'
        b'4pn?9-LKNGzwS>5wJmPO<cSq?;RkKjo?%wk^$KaQ8)j1mfd*ACVh@i*`If`IMq*O7L1O`nwq@02kIwg2+ZhlkEg(|jqhYey5Lo>6'
        b'$@rcFZH9u)dE2v+4f+n^;Y%%LueEVett$gM_P#-(wvX{$YngPU4#4#a76|l`RIIuY9Bi|wDqS0$(w;%#<>SJdBQN_d@4*w0e0RMI'
        b'`+^`r4?4^r@OtqV@xzwwuwk#6%bBKP50}Xf%S(~*!o{d6u{?f;XSyYuTVu0)z^z%pnHX+O24^C<HFsGuxHVQwJGUm&(!i~mXFR*d'
        b'b>Ifa&5P7z6J+*PRg~KrVF{ez1;h&mx3l*F_V3ErYis@{S-xTu@WmtJ_O?7SCFj*3-!?=Z7fM_L?Hk32FD8v+dy1Cb$#KvDe4r8s'
        b'A&b|q{?&p#O}f97?<^FqY0FcjJ|Amb+g4w0Nd~>vSl*U4oz>#AKgG+YJ$!%L)&PZvD?ImE>OpERRs6V0|M87M4mn@m^KeC5Wg<E9'
        b'C!~LEO65$FS%fO@#=dSr?&9ggThEartK^HS-$=eCZ2^JsD64i>8a#PbeNp$-50SoBjOR8*>Tb3yx6MC&Z6jTl)3$E9C;6_i7t5S&'
        b'sk@1)>7F%r6~4KrzTBY@Ioa^^$F`uk#lFUFPj<-ROYYV$Ly@ajcJr)y9WLT*OQYO>l@6)$7NqW(WyxP`uTRcfkd~8|Z=tsardV=3'
        b'sR<Ucw3HqrEs7?>H-JaAkznKQjqby43;M{44oUy`MV4XSk{xf%YO`CAzWkDd((5ka9jXkCcS(l`{epixT)~t!`x;y5z|}r-d`P-S'
        b'Reb(m{-1_GT3v%btq)0PW0%1k0(dBx)W*h``>wLeTAjkSq=lziyjI%%vIHf@MM=K{1*f;+;A1^k+34Lmoz2w(<7lT^cI%>8oz-Er'
        b'?xgRDc88_DsPQ&Qzy2B<6I8X0oX0roUpyaFLS@2d$E>8LGxA-_ZouDlbviZ?*7*1t;F|U82T)rd6?*Na-HI2m&q+hLVf<Y=JSxt+'
        b'hvZF!ND)YRf~S!FD&frD!zRjy5@)hXbm)WeW3<Br+a`#GQ!W6Ytp17d*J<~}<eD|cw%j^(*An)n?AevJhyR!ml}Uj#6DSGM!0u()'
        b'l$ng}`DrVwv%8S(pRM?NHf5t*V9m(~0~uq&9v8>q5bf07Pd{+#_VBTv=t~HmGs%Gur(u3|NsRqu2-`zB&L}e~4D;<)UOrS17wvni'
        b'wQ*E-oO1J<wqlQ+bL+R`K(N@m5rupWczbmoZDo~Na}3@pLt@EZh9AA^eWBsm=;0=fw{93q&D+B-*Tt@)D{lPI{qnO4_666Q3s*LN'
        b'5Ig|YhE(q<*}g5$8WYd$W%<!7-qwbbb()?2;gf#NGyWaV)Ghcf{hia#P8Cl$oE@#f&er*~t-bXf3V!Zm=f})XWMh0Pydr|ltqaHC'
        b'AqqeEE;n0vTT81KlrHkLk!|(XIVT;?HMU;N)6`Lb)?!^9zLz}7pLe!$Rl3Qu6^70F<59+Unt3i31ADraz5S4KG!8~KoXAcYZXVwG'
        b'`Sz1LH@{!gie;mF(c8^=yB^2saKdO>xANdZRpWPoG-hXmbN5j^V_2W9LX9{Xj(;@){}t1sQ__Ejzvo8N!H03(#&{|}rb)?hIyqu|'
        b'>mgOk9^d*_R!b>k0!pBebVHMYB?EbgTEeEOCT%*6@gv{KzEDeB*{Vhof7Y{@e5+f7rLBjQ$AyK19>%w;8K2f6Nxz+PMN=eQw+V!N'
        b'nC0qjY|33Mn{tuy4=@{bx9*M`m$tHLPzFjIJvVS~YuK}J%=Z@zsL|tdwNfMqaejb9f@)J|4=!qD9h8d(IQR(S5H8nUWSl<<60#W_'
        b'=WpIIWc$+|kT#=0YTipYZLMW@w)$qbTCm<!rM1MRzDU;WCM<L@ITah#L5X_|g<k!+o7V4G!zHk5J?xMw`1=-ipRX8Cv(eOAMHi6>'
        b'6or~i$oJr$P0FmOZ%OxqC>2zP2T=7n?+faH3sKC}!qVp8TYFZCfF9+HS@oswd5j}Zso2zw+tda56B*1jiipt>Q}wm!%NQ1!CbG<{'
        b'3y<$%QwtVNJf_VeWwmWDjE>4$usSO=F+MM)`;_k-29uI+w$N23j*BZTS6J-TTMfx{DQECdDo}YrC)il2Hl!FpzBc}{H)03&z<^)I'
        b'0$u=yc<1KgrsA?6_8NcK`!QX@SV(Hhw6urQ%*OBcQci`AP*9|z%-W2Igo2cbrjMH5qMQu=UWZ6e8AFj%b>uY4Ntg(N)f<SJZ2Ged'
        b'+VO#joKm;TcV@57Ntv8V9jPj?O!)3-UPiJM8FNmXO(=9u`n~8n!sH~MWGZhbnZKcoDO0WXbp4OBQ+`LfKSc%V1S>u_K{9>FL?|){'
        b'0x48hZNf6=lv8CajHH^t*MogdJO;~%DLR6{AL0}f??vrpE-)V-%OFrTK^iht8BUZ%$tv>~$eNsxP0(r@KaPBkkaJ?>3(4I4^T^W@'
        b'8@0)WMj9mK>)yLfxoyT{O7ZR3cWVwQ#S_1td`)vWVQ}=<T0J>pM}9ZOXitVU-D^cAmdcH$m}z3JmC98DR!Di8FOv~Vl<9D5foeib'
        b'i39TN{#Hy$fD+xWiuxFFWxU8t7jx%@EB!&xQpMakVoH3Sy}OH5iIwqUWkPW0UY`ns@V(#EUBr9TbsQ#`blC}s@B%)L44hi;peb?+'
        b'EEUQHN=bU)z!mJ80*KDd@+pkBmiF%4%;(PC*R)B`27hX<{Z=`cqV@gMgbkJ+t-C~eHU>NW36G3xQo08t0WkO!J)7WdZV2SgWeOmp'
        b'@W1vJC?cN|No1Tbxl}sW6sA;qOq=1Fnp*V$JR#denASO`W;oewr>dgv=YsVURdgwXiTM#29gn5}yMCOSL9p3`Y71JA%n7J=B8y+W'
        b'-8EIMd|(U8fn~y`0)0QGWoyw&OyePCiibqqr#6BB0yC41af3F*GF655XR(Y8F|Y;z8~_E-%op(9iW0hyv-7f0I^~+SPCGIW=gCbK'
        b'jyGrV`N%R+@brY2OUDOoQNc#sryQ#~Axo34b4`;o<GPO{#Y|SeMg4jKKDanFOTAj>n#v?gfT77X4Nx?>rW&mIS?v>{8|LogHMhwh'
        b'hf>^MNx<i(Kv~Mgy5l6@JIzQvQBXBes#|Svu12vFfZd1=`QEsdpC8H3CWtKDw5^;_0Fh_uF_C|A>^B<sH$`YXLg43i0j*;yXWWt%'
        b'sosmK$&mnxVfyOr1m%rbc(Nq#QwdqGOuQ2WIAP3n0HkkAQ{;2Cj-d8Nv3HIJKRyO*2LLm3a35fiAcJquZ)l@66Wa;eP`0{MxdiDa'
        b'VE#cy(-E|ZP^xnh5T|My0Ps1gtig%zg3v%#$As_x$u=lL2_@f)0_f+UoyGwsQ9|Veqh>H2jogFkqrcPECjs38r^@^$%KxxOIahyB'
        b'>6sn3Y0A<@J!YlZXwz){=zMC*41LtpL-&dtg=U@>dWX@1)6gVLz&k<c8PJ3;3%6>DBB49LPP54T(O@3~0~iWj2ikx&Xd-opoVi6k'
        b'vx<i0=t*bw2V=IKrd+yB6)XUNqGuQcMY|sbbgH)k)AVGk@F9OEC`akg6p(g>-wcpY>G^GTC|SCDxTykYuQ*yMQmPs2A7^8;dJJN='
        b'%Jz@Oo5p;#okXc$so<AQ#z(I3hVR?cvYjA-AsYNZx@fzTv|18IKDmJ!AKVo5?%b-b{5Hl!#u!k#iPXX`z8}B<8tyTv?5~aMq6?Ub'
        b'k$0u4^VA~cx{sg(*cXS1B(n*GqD~u<RX}A;1Gr1#1XMLSf&a0-tBv?1^0t<O)e}?{f~i6Z?0D7ug!vE+Yjso1Qq*~VRNFWJ9W%*G'
        b'3g+$qChT3nnz+)&@yTQok}zrl7!k0W83+V~F2PnVYj;V+aH)2I)(F_{l2{P!`Yj@@m!-RzV3SEeNd|;~b~i~&1u9!eFXDx70b8^b'
        b'c9q_!)m>_r6{&44qNRA5-#HW1?tc6H|Ifn{X3m_;d(L^!d*1h)_p%dA!NbUCIKDQZ{6(q$vSc+X<)bounIb)Bbd3ssDDc8+t@P~g'
        b't1H&Tu3jTJ_v=Hu7937Sb&<&AGJMJ5{}qiT;4z1Ld3Z9iBpqq?AOY!ax3jqf>;b#q=C8pJ;raGQ0l4oU$Xk0T7m3>imFssc;r4aO'
        b'Zb9(li;PA-r#y%1Lhc&F@y(?&&#zkm0|=+Qv6)khSeR#X0rJFoJPL>U0RA&8iREQT(buRfpMn3DODqEB71t`FrL_zmqyQvkwM2M`'
        b'jm27%ZwT+)nU`BbV4Y@n6;bK3N(4mQA(9Nde}2@g65ZoPA3CHOsMV6_N_h6HYlhY)0@BS|Zm}hg-jJuUq+~G{OBkM~V4cvwJTpiH'
        b'c3Z%>JF@B%uv&93pZYtTlVQM1g?EILmV11-`f-=$I6xqj3>L*;0)NaZXF@X$ucyhSnBOzJA_mJP6Z7BrLoO|KK;fFZ>@39cN?iVI'
        b'^rIjPUWn%?+N&XxtyI-&{ZX-#f<=Val}JkENpsLH9JcweD+2R3nTZNXH>cm|l>TR%QLxS5+yG7X{kX~O2Tex(dz13~`AFQL;s`!$'
        b'Qp+{TwJCGO|KB#RyZ)oiXn#MsFeE>2boqluqyKw9LB;X^(Izp|go_w5o;Z2Xp{kyjW4`6mb`w26N}J-+eowshAgyXnnRt~hO5m<a'
        b'd*Jy>zL^Yy{!$;r6)QQ%C)y4|8)cFEUb+5{n#^w?-gw0M%0YLJ6v%d6Ougxt%<ZUz9`<P|^BV+TYGUdUo6OVbV&d1%J5%`0+Sb#z'
        b'=HVG^GLyfThoYYPgFZK^eD`}Zxd_Hrf0jG%`Mv-5-(kVSl>M{wcFwq@r0@Q7m~!|>=^xyC2CEACD*a^E9jCa*heK<yle4%)`Ti`l'
        b'LR5Y{i{rjm{?K<s0c7X-aszGzBzfKZl0W;4{wNIvlJmc(fua+y-%qPGn!O6#ZbgGZdHIJ3d5T>%2DlgRsXMJ@SLfYeto#Dn)h3;+'
        b'2h_jTD}M<wd-$YVWEI5XXeS>4)UP8oy4Jj_NjzPGWcWIDvk7`8S#$X91*AI=d?I-|t|Gvz>nC8GPH16!^cH8d3t!>MT_IeHd8-bB'
        b'=U%~ta&c?%Rj)>;Z-KU+{E4W=`k}j^dVS=r`!-m31gE2S^PVj^j&tuf{O?~Nax=ns_-41L2~|Ot7m|{<Ze2|yUTnhms7Pq+#lyo&'
        b'-n?~Th}eBE$?tUsIz<AxQ)W4D<}h1p@~m!_<;IKg@Nl{b4FMv4e0Ec4tTh#MG7^uA302@JuynjJCNweL8{_(xc-G}b5jWrw3-0O='
        b'=(hCaE#g;AUblE&0jJN!5j#Zp9UCDT^v5>%0)}90{ot0*%>xf5D`xNeur67{n?JubAcPpMK64Oea$-x$)=+t_PF_#S#9bA`L-9~#'
        b'X*xoC7<6yj04Lq;HM?oMnHfk_jkb$oL)&6isqL!R6i=xOECz~j&7Zw9+P%8@dppqOA0FW7#O%FiFcm%iX9J?<HTkc^o&RcD73vea'
        b'qED=JyJuFZHcvgAymbL}vylrI@f1E5@Z7QpRlro}k&0C*)+w3#S|eWI4L%pJRmh0(+Aa4+orx?{i(8Uy-{@|!)a6F!pIm0u6AozU'
        b'xuC>09X~10xidHe2gw@=<9Sjpm*1VNeC|&CnC=^v^KFJ>BfQ7EwFaItd<G{o!(yRx>LkBYF=eun&%>Y_bZJ=L=Z(3_IUq2-fCv#&'
        b'O9E!&&yTG<7zOA8kACLZ;qz_0#un(@yVdtS>~|->wdec6+ic1Ie&5L-oa6M({?Z7B(W_FIOnvWlW7G)5e#iWN_I4v~^QzY3DTl?2'
        b'_la+kQtHh{&#O&ll@!`%itb|^q%ob1X3}ikC4+HUe+LB*&z_cli%-hkJFK0K35|F<DJFFJTCo0_Tnni`fq_QNp`y%5l=yASvTMY_'
        b'#(B58=!VH}iRW6ttP+j)(~eGlPHb+`-Qdm*_BC<=(gUgejh;;{W)+O7N(P-<Vhki~jbN+)kM;pBeEJoG@}5?u6j_^P=Exv<7E1l0'
        b'(W9R)Yeso%wJ|O!87Zsv61y5bc`g4QpB1#ZqtUar<v|GA9N5*8@>}#)In5<xaza;qBPd9hc`{mtL&49zn3ftuv#AkG4jE;(R>bP-'
        b'k&-j_2qqb|emEaTb?~e~846}!zUMAT110r)?&3+hn|_}?wH0PhwHMGYRHl!Fi>$TbRwu8Q-+CKNDV$?ayK>8|BsT)~M0aF;Cp!28'
        b'9IH}tG4&ywTVh)yUZhI8PcLv<Z)EW}<?DB-(ndUohSw+iP>%h8_ynl1oX_j!fwl87JG`}r*SH*+*f4v4EraIdJ9q%)CO%|`JHY4X'
        b'kP!)3fO%XNvpdv8N&&d~>APTi=tU>CeBX)Q<82;86^hDQh6sn#i03aUOQKFSg61zwfxNBnv0!9|_jK}=9oG{ihdPqnY%(LoQFu^I'
        b'9fSFRj2iY4H!<p&MnKZ^qPwksyhFVVxiD%)qr$7;dc*MX+TCV;uE{2~F8$w<+-bS}7T$x0nOD1758e@e>%X_MPduQ-IX|MyaV0nI'
        b'KZmu>un*|Ub#|VX+#iG1Q$HSq63u@fgVw?yjREz)&G&7Ii4)EEQtkvZkS-PRmR-9>${f(+X{GQMw^lzo;8k(4$Bs3+--0X-6N>%j'
        b'cHaqEU$Yc&12CarKG}T&8+hXnj{o|p74yCE7k7uOt6A!9ho8I!_w9nHgU$D^1v#IYiIsAn5Eob$BXm$-iEJyKl_KAZF(MJ3b670)'
        b's^C@iI?2f*21DX=w!ePh@X|0QW(Bn258Aq=O~}Nk!L!HGYy=O&`$5<})y>)%7-~Cwy%t3>ANAI5QjwZJG-oo7`LU>K_HkagTEAz3'
        b';MpdM3B&MkFh}z~6FSkF?pQ<X>?Ca<d7|Otq=+}{Q@?W{C3xQ7Ct{!vgcoR|)h`ONHF)?sLBye_@4PHg9ISUZDr?_o22Q!B6ppXz'
        b'#~qbd+bd4<$kWj3h|ECrK7RMFnqe4kn}Ldect#tpp5NG}To0zxGRZ~{1TzC%Xz5jgv!oQv4k#3!5x$cQK!lgs@C>MJu<G+p0d?a5'
        b'7xAMujm$y9bBK)QUC_Zt9>_PD7xVM&yJGa0@2WJ(%o7BCpn{A$a<ulTz>HO&R%9R~8AtJ8)46XeIMd47XMr@5foR|5Rk+!mL8xVr'
        b'rDkFEatV*R2_GsveB8X#jtcu&9EH0`r+_r@THm=I6Nc)PU>6xY#?pDJC4DYg3)3U+6f_&C%dnu!P}?$@7yiwayg?YZlp-6wVi744'
        b')M}SZp_Ye{Nlo%Yg5)Vwn1FDO%@qo4*ocRv$5qRXw`mO-%S(32sgDnEzS}rp88_P$^g48MOZ^QdGtug#QgyR|`|L7+45ezn@gxy@'
        b'09s-O`E8ug!H-$6*R}Rsmru>e8+iEyw)Rr;VpLZHtrU7O#68v8c?;GHUh|{X;C(~zVo)_6I6;67PQHFTzf?WQxqp8K19Wfgw55t&'
        b'dr9{@zikDT+}O$UaRzM4T`KBM10xE>3!-BK0p9^cD?j65MHdra95ADMYtMMrHR2+`fKZ~w2f6{*8qA@M)-nOKA#T4xEj?gXg>V<9'
        b'UJpXuJ#f$7A@5%e_`6kuIn`|<pE3%O45e3?;8~0k=4cPlzI!|Wz46TrfA_CD3W?RE=4~;gr&s2>E8lrUIKSZ#Uo-^sgt@3+KE2Y*'
        b'YklaJJnSwGeZ5;lmX0&B@itkD)9o?w#aOTeAqRLcRBSe8KEo>|FYtMSU>=4baip84bt6(<4iwryje>Pbpxq1-bqdBcfIbpedXVnH'
        b'17JhZ8bpA!0mhEc6M>J=yP2pdNH%^<cDx(3795Clc!G1VaGH6aSE~A_m%x04U<6GcpS#E}xqgp6Qh5jbcgE`d2TF6`^@BN5wqbIS'
        b'`jrMxVq;QdP_N(4-pqH!gnm!0fw`mSO3ZwLepbNno5|I#m}b<xx|wl@fVqiDl~KE0(8-d+>5q;9y)1=$2X5kG_rYoyXBEgis|98c'
        b';;yOh6e)jx$IL%8oR!3PmA>gxcQpV?k`xKA6LmnACs#LH#^>+%Jv^{iTG6F28uYJNcbY<f9#N*<p^6W9Ma{K)V2?Q7iuzLnkTU!_'
        b'_)yx0GN|6A;vXT2^)60pS6|5z&o%h(UCd-koBwtyI2&@y>UA({5RvmBtKnYONJP5{F&iWNw<qch7qPcN%SR4jqiz`g+>`DaaP!Xg'
        b'!qA?YpS#TDicD94<}p_mrZukMY(dr30dn<aVr@f`TjbYZO5Pf*9fiJtlQ9WYm`y&gHt>O8!IBx4de}9u@WT1CXo&D{{PQ@jawT?E'
        b'npKFr0Gan!nABia1^8b}KDc*}Nd3eGup?G9{Gn$FfH4%>9xEGQ_ApR;ZNa?Zlb`RAySg7f07NI{Us-jC%gjfU&V-ED%hbXH<Fw4N'
        b'!erme=ktQWrXI|hA<25tPK=)g_QKX>)9$3|M1PbdZmn>>07VmD&#8GXErB?1G-UI$WZA)4M0TX+PLml!#|vadPnyq!@C69G!?OYQ'
        b'8TwydgXCRpG7FGHDr$Ly^IO2ks@uf)GAMgNWc5M5xm7-`FPdlgKuv(<1~r(fP5!R{qSlaU`P3Z})MC{9qe;EA0biCBscyqY7T_?R'
        b'mhd|k-q-u(JP*>zo3PB7Wef48K$z*|ne!GZzhw^%QGc(eca^GQ!RKkV_WZ=NH<aZw-T!LvOf@J^vd+IY`EN_J5$A9d_=Wbvr<*+Q'
        b'HJJku=X*^Mq9K#XX5s_%3FPtD!d{x10TDp#$N7&#x44pNd?}}1X>wNzFSGNoD1Sdg0$73*Nrn2&CNghfJ|ESzHjKX{%YQFqe7%e~'
        b'(p2;mU%<1Q0mp}e&Q1uX<!KA@-mEt(*Iq6wEh)Mo&%s+uX1Y%_c>dB*(#;Z=8hneN_M-762~*xT*a_k*p9DFRGrG9Atw>pa+oxPh'
        b'gf%EmNcEqKynM6-{fgwH>H|&VoVQ;TS{_LeiC<#jYmte&-wBrjS&ENPwN21HvbV(r$QtMuL<%I7;q(4)Dr)(Rb&1+Sn^BjFPJs%6'
        b'0K3|Q#$7Ui0dV^Fg1K*DKqCNq`PoS8?05Q{>#gf<$j|d83TC?L2G72RiC4kmZSs^f`A7tYao<r7-5y}@Hn~2K!~l`tCBnV0@<%q*'
        b'RB2N$pN2$oUQG$m2(u^z2oO|p6X5D<D~P9?AX72#M~8a6!Owv$xq?$Q^$}_J)|@l9$tOk`(cYtl*FHGt{ebfX4V^=G&}YQ73h>~j'
        b';l9=zQ@R<B?sPxh;L$d<HnXjlAdg&fl%;moL%n;5#kB)ePQ51$tXC<%{GMJKkEed5DSkGEFJB$3iEm1IGV3W^l-z*ovJthqsV50A'
        b'*#WA&)Ovhp+4H6HzzQ%kOVW`SJmuw;nui+9?uQvH*U=<xT7nL)La3+fqgTop)r#%mO*@y0JYh{0Wh<Di2p)hhH4fhC3@C1|-zM=W'
        b'nv6L}XMowTm@$M*?78iUsyD_h>kI(gpP5)}SPWMm3{R^=7$Rg_z|K&de%`S~5lFw2f|hSqY)6}li!oy+Vh}fNS2T1AdjneSEWjZ='
        b'Q2F;MFv9?K;N)7s8tCM9y)1+ly5weql#VW2$rxm2Ly*xBJn_VgQMQnA^PnP1-a>%KhVL6=cB#!+uE`Wtx=ZEjPxQJaj1HM-o6G8_'
        b'&uI<PtS`(4nbr^l&oJI%uf|1i{tp2!phG~z|AAOeezp`y_F5q#e?)BLBl!SFOJ!R%U^xY2(jpBXlWIO~+`2bXgh)|<t{aNrBj*if'
        b'Z4#($g)A*E?Ge5}8qD`wVB%oyVf@vI@~_{?(`J>CH(DQ_@%*#CHvkVV*~2DjFRMox&p<sHDfPVy)sK`XXK>NrC+yZ|gLO#JQ@uPu'
        b'WdW&E4t=LT|AX!<oAP{VWKSor<OmD>P($CxZ#ItmWX@jZxE-nliv#_mN4-)%Aj*w-TGKTk8){acVuHnspeZ`MTS{OCA^=7@T&7?#'
        b'@4mh*IS>jLvMLz$M+86->D=*-;2drr=|{Mc6_wP_b@EzQ-X}bO>JUwhMmG<v40#1SFjD@J-6m1jH3E4a?0ZnzI6nsr8?NO;lKtQv'
        b'((kH9Eug$nniC8V+_h2aHW5d^q2=yyDdfp4V0VJVOL_b|`T4tGx_WtVs<d{BFTw#$%RpLtzSI1k!2|i2_}F&72JvaIZIYv5@%aMe'
        b'=;CN<Yh&K448AO13F;nM09}~5vD_jV_2+u8Y@w+`n%kl9<}HN8>?>CO&MXe63!Px5qr+f~mF|%S@b+sKGz_Y_r*@sY7?QdCsI|FI'
        b'3cyIq1p$0a1e!kko{THKAC|WKjrH+SN?ZTIa&A;pP_1Y$35WrFIr`Cd=xpq`$J18dm7z!_wOM;9BP3G9E(V|D1o{aN;J!*;VCBAV'
        b'iEPG`S`U>LmqQDJ<A7zxB=Zyy`p5oG9`-c=5kLWV4zo#9&VY0XDb)CZ*q{T#z!?&c>pRt_{PUD<@}8d03dT!50a%QyVP-P*&>7F('
        b'dMX`)LB%mu$LL+AW-0X)Gi+mw>zJ~iafk8`HG&uTTlO>OG9X+aSI^^N-fYB6u5~VIY!^G1HhNWwjB%|~0^gQ^x5Z3ZqH`g93jxIz'
        b'Q~XAkNH4y{klUI?l(f-o+~$wD=t0ytgC}L}2+X({6{eX!kcAzJBG>}}wQ2{5Bqm~y|D*%#=9+H~XfZ@S!`H+!{cqRjN2xX69srcp'
        b'7=>v0p?Hn<-Mi`D>egRE6L%C})+wBy`8b*8r*P)eJERJ3=7}#47;ZD2Xs@tU!-D-=G?O=efX^3u1)L@R5F3H}2fB4Tm{lx(S~$*b'
        b'&jeV}8&L9dRx3cMhZs(wo{u4%^|}P$q&9MG`f7n36Z82TUS!B3@bqB?hsfKeOT&7gtJl^vSR6Dp{*<gJpW<^<CV-V_-woOR76Yn+'
        b'6=w!xaNYP<WbhgUR#IXEwB-Aezt4dEtOd24U`wuC_xz3N6_z~8YTiDOvIEGlntwTyPTh@AW<3%Sme^VkZQ;8C-tZsb&BR`?rl!ph'
        b'hIzbkUUJUk&C+{#bJp)Oz3qTsC+qP1|60a>=1Y9ZESW@!*PZinzJ&pNFM<x;_g4YZMnGDwD*t{e+&ix_^ZvrBHBejF1|3V2eU#$>'
        b'NRCs%Q<G+*(P>S^iC)HhM!~H-m0$OjI>wk)xqK0jgd|*rFzqcy-N%64IyV?9T}bD@`1kcr#yrL&MezuF{(k=9|K5K2kK2ENYyV}?'
        b'{@Ne6Pi%6+2r??{NA)>39RO%1Nf1YT6TcwhPk^sG{Bz!L0oY?8w`c7Q9ys%tzP`%Szd+Bz&?88A2N1WyPY7?!pUXMhAUqDQ7chA%'
        b'G~=(x(x4x4{1vyiPf=a1&N<+A&vdLv;v@LM<P$>TmvFd|?#u&SqzPm(b@VwpykK74uU3|%&dJZ;0ozcb+N9#^Zp_Qdj{n}@M__*y'
        b'DiaBBBgHX20wNVw&9UT?)<-~9ccHc}VN#*~8xmO8i}Q8iE&kd7=Q>}V;z4yW$1x%r)CH<iCeF#jSbsevi3so6<2*S<ZT&Z}9#ph&'
        b'z9KLYj9W|ugP9P*Ik4ZuffNRa(PoiIp2eeBhd<6q@|cMDl<_Oq{m5Smb*n+mci!)0E`Kg2CDlBj0u55<oetX6rlP)abTP6P8VL41'
        b'XP{jFQ>Q=v0QC3)SIU!9eiu_<QNSxB_gw4ukXPf>EfGIF4?5B&Gj*7*!AM1Y3iph6i099IAD)CC<xP><t3jXDqYa?j5ceVhlz4s2'
        b'n=<t$4ghK|^m{RJjg!MQZ#dO+PA?X3=7$`1t@^;sF)eK(>Msy_&=CN>PlZGHSqBtFv3M;%1oR@)75+Gvc||ZE1zi}t!uIke<a7Ft'
        b'Tb2nH8Bda>sR6rUnVt7ZG(#M9P+bkN{J=N}sc9xA<>81)=-eM8jx?xH>h%U75YD<pG0lsZQ1o!K7zV{z%{la^QwHH#sPol^h+Vzn'
        b'1knrTpA0N52&7M^g$yh$JiKZl^gC3e3I%k$oj*9uGVjmgDD-A~&o?2(G$;~h0#~P}!<KP0GbK~&ekl170kN+EV2`1;AxroS)`{It'
        b'qxL&EiVK*mUwGY8Fi%vi!|x63$oW_ajwThMv1u_4%e<usKL_<Irx!?K4hZtY(B#EmJtJvLvwY3AKRWn5OZ?7(^Zll#cn}f^&rvMb'
        b'{dgL|g;qPq#fV#r;5{%t*jwD20#W~_0lG)dM|G=^o5sgVNp!FUxtX*~T>{hP0}K2Qr9r6h5d=_4fV6{Zq%;W?HXx;1)Y5>cTb&>S'
        b'H0puAl6B1pPRFFkN{#3sgOpZ$K>XfmMnys^g1cbcvU;SH876i+RYB39$|l58!^N0GEeDa9lqa}=be4MXxV+Sh>h>WpEFDd3bFPXd'
        b'(U5!IpRDbuc_4xGM#RyGXh^sa!C?@%K^lqnp_b2C!T`uyunq{B5m_+Z4yp@_P{EpC0^)@uB87{@j9NZmxkVOH26Mdxa-l*qG|T$='
        b'6e)pbrj}<B%l~kZIALKS3<LK+5fDNljMAoyfCH&BfydAY*f-tpkcc)IC*?Rxq&rD8OZXI`UhIfC!!=hQF$UZGGYbe5859Kr&8$TR'
        b'^#~GA!<pEL+#Eo4I}q={7ZZIfKzYdTfR^FZ=^8*AzgblPdtd>N39Gm;e=j1dvS0wWKe3e3ss5{jR3(FL1vEy(oVqhC*sq{A+^RA^'
        b'oU3-ha4h>-;$L;@0f(71gRC27QQ`lxBngcz<kQ~(oJJ()EyvhZuy2EVL1U^_+`R1plqU^#pqeE<sq>PVgwFwRL4N!zXfpce5U>DN'
        b'jX?mdFd*PyHNr*X8?0c759-=RiPyNyQ<Km^>S#S^!%yS@?8Hp~%1W^12@kQvbq5V^oQUrnfKQsAZPMKlM+*Uhf8`)i(N#u$(;?i%'
        b'BE%$k73*%X#Dv3)iaFbA;!B4r$a0e<z5xHD$&ZM4>V!|i^otIaR<FGcy>k-h9S}QUC<UcrN)_f;UI#Bf0WUE8+$g9{A_QpkH_(7Y'
        b'_$A0#vTTZ$m`s@EV^Ds`LHkS;W*KFP)8G;AD#UvZFs0T@sBnxGUIOp^4nCSVxEU0kSUSa*V8RmCW3R_uaUI^FF@Rj2y1JMYa-M{5'
        b'akS8Yg8#nm-zoTC>fi}Bs(hKX{Ej=DejNawOXusfEYS|eESLCWU0Z>w0-Arcz{r{)%PS7`T8EcR1{uNRs`6oQDIH5R)Tt`qMoR3c'
        b'r_peF@D-T1q)x4w$AZnXsAUzz0z6Ld{l{P`OFUDjPMiO@a~9P-3O~xHhw(7W3oP}RgB0Nx@`=1U^)q!0Sw{SpfqRk-)h%c7X|pI-'
        b'z29LnOJQ0lD*PjBQNs2T!MNrMUt)>!I@;)ukjllZQ0`*Eh&(;>q6C-Yf=nh`E8(T<tJevjt9p^O;ZY)^E|#AkfIK}Nb0B@yG&#Ut'
        b'%a<wEn+%$IAk!AFH}wcQ1E?`LTo=;X7Eg4s?R>wT(K>-bR}H3G&)g<b>I=}pAOJ@^cpz5P@559mz7)r|;f}UM#g=+^sZ`#0n?^Ud'
        b'9_kHv+}q51Uq+p(<IFP7$c9_^s2J=I`-HmdtjfC$8@$aHJSs1_#Wj5lX49X)+qM{>H{h=Q{YvGvZe_KgXVZ^KVj9+y65gsC@@Wio'
        b'G9YmMHKmM_)fbWD&_`hpS{?%roN}Y<sn=j#wL$uhJ4e!pz<L#W#Mpy^Z<O2LKNVT)YvXaTXM{Wi8Qu$J300Ei2K0hSJqI&ITsoXI'
        b'`Sdg{hzSu8*O+_~**?o;1#H6-u&bk9cRY1{KW9lOkGtK=f82}nsS#ML5KS^lk{hDQ&2azWYsJvdd>Oi-5r?@b6U-w|ySoild7*Qu'
        b'*w-w6-j703^T2*bo?`P27}#xZR)|P<%sWa{ScR0XMuiM=^T~wLNObU7<ee4h;7+787!^JY)*(}dLf5LVMT}{B@<y;u{<si81u1Un'
        b'CRBF_xe0#lNa>D`CYr8!^Mr19WrS8fw3K+CQ9LV+k)xJnNKH51GGSun_DA?U6md@}4_^cQ>R3@GiGBgb)x-my3829=o6r1!OHA$6'
        b'Zd2uOR=KTS-jkR-gX-XsfXM3(ZmnYFEk6ZS^uS8K^D*V)l^1y<0?_2dE1*WBo81gZ+bFBcM35yjSj2#E4QM+eOu3sKE{d<PXrQ_&'
        b'55)r^41GU5Baz$hf_Ie!DV|c4_K|T|sWA^<l3W=VusNoe7m?QbJbUQ8O3<?=E*cDW>2q0-Nt*nwR{{^TMRN%feakGV1f^1Yg`I+l'
        b'XMX6Fcxa~NJllP=&SPaJK4XQc2+}(KgMQCkZmXhXCfdD60k=E^LNNZ_;8hj|Ifz-ZjVpg88j#%dt~t+6M)?Wb{aT&p1*Y|5))I^$'
        b'>gO5K9g&zJO>WQ-_Wenu@Z=`gwUX!9Bj*9AaT8nFBRQ}$6^I)u4y1$~dJ@2lD5e05aZ@Ydj!t_}-KQ)PZ{#!w+!2}2-T)(u=O{O`'
        b'@~N*uEn!P$mVr6|FAd;>3Lqt{yyz;RV2UW|5frqSR`M(>Px}hw@eznWkMcQI9ySGf0l2*$9+cy#afrF@u44BIY1ggvuC8L=2MQQ7'
        b'qI=GAl#LizGJ_8OorTS{{u<Q(FCu<FfRrS&4<&&r0qpXy36HssN`bgMILQ(Z@1J+hA-!zb$0F*0I!)bvGI&ussUV+Rq=R=dF*B%T'
        b'8_VHIkg|xCcbo?>R-hP|+2Y(8d4L#?-n<tT{+<Q67^W-${rx-0z@P%8e5xW3!IxZ3-Tcun!Q4L^0dk}%_3WWIkRiMYF-=|DDJ$P@'
        b'GH*Z}<uhhfC|7-Kok78lRnzTthn74Ey8jW#8X*Ezm6y-#1pLWb)*p!(z*GF1LYW7~Y!0G6Y>QX?f&y~G6>c7=MyK%u9Xjy@K<>YR'
        b'OrQmjFJ6LYgUU=T^*duxVG3*cC5vRC5vwBx(j%*Nb!>!IxPSg^#f<XglLEkEd8V9Ddt0U`@v$ILJ-!dn_Teluih_OH^CkQUs4n=T'
        b'?*Xl#@2D2~g7}_GP9zY9m{7g}KB1*4Qjp<L8LaLiEYaG@-P@P}PXXQFkwHKl9n#I-_vNQK?aa-s%)&~sr!}L_GHkff>wcAbcOPd?'
        b'dj>mMYxw&<WAsmJ^?2agt?(+}?P|k-Y*Rd_pxX9vHnsS0FTc3MM7_Gt&s3{0zBVdf+n~a5J{~e3+Vk38Sq|+y?gZjRO_tr(l2N9D'
        b'7m(apfm4N+qEUp;c?Lanh#J^uR{gZL0JOIUR*zDr_H#-{oTbk-$gVisxN20O8uE;avp?W$vz;z9S}eT={mDArPVNdwrCN54I0PEd'
        b'-GRCk-L+1<mIlHa17`0C4;MQWmDczrPLng7ZWmv3$!vjko73qp+aBt_)BS@}C1}+0)jORk{%xjAps_ixMa#CrT_rB6jnsFDR03QW'
        b'NX7~_lQ;xW1;1n%qj+2RDFQBVz2c_=0K8$dQzh&~ueKPraS!saTP_LB&+4!?OKIU@S6a3(0i&$@xv*Xdl1^;!Cd*|=vo_0MhLCJw'
        b'dX$3t!-E_!23~fOWsc4Ea(3PbDQTz;DtYlrnc&AT;zDXWEVPBxeZ=Wd<$xgxC;jIXsr&F$Gr1Pm0^Z9MTYdkYBiG4*y)YZP<v^%s'
        b'_Bk`1Ue&sGvGZ{!Q?{<;pZD$q^WD%bB~(D-Bl@kV8AA@8QP6$cB&L$;VpC;!hJNynd0_P3yIyn$3aNm{nYZN~;m7|O562gH0pW<l'
        b'7?gLpS+v|&GRMiX(?b``I5J!}yrpx2>Gf*e9D5{%85(_Tf#YY@iH^$QW>ZI>`(SmaSpLK9a58*&@M{=r-ExiX6md$I0LQNxWr?MV'
        b'vwB(aOVC7b`!eTN=olm2QE9homO{Z^8-)yr&WzW~Xbkf1u?W4lh4zWiqbH${PP2%Ax(6MMM7mD)(NA@CRW{4s=lLzEVVo`b)&PIS'
        b'T&-Dq?be>SBvoQIkSmja7HC$f@!+F9yvNW4KD|fXvrnPG5^1S|(@HL0-xs^5rQz&)87aZEVsvZCc&RK$yLBfJEkn`~(xZ)uPba0?'
        b'Fexnc2v;gnK^95ZNuUG3tOotNGk`^cb9LDP_&ApcU|(X7;%tqqi!(<&PIq5&KwPfL0sT4C$sZAne<`EIRwjbBP0^zw^wXaOf&Lv$'
        b'!Ox!PQ)PqBarecpX1(o>-`1K!t_{c%hZSFAXV=OKWqnWe0dV)BL+gnT95AL?zHuS)GCxTfj|kHf6P<~P7%tolSdYh$yaC5HeuWYl'
        b'FO;<f91ewoSew<i5Gm>ym7t%VKnJrBuY`Z}IBL-$Wg9^Iono81Su<cjFBt?75+SlpLaSYxGsI+`eCwjNJ(s6Y;m?r1jJ~rOvZ0Le'
        b'4B6;HB**J>cO5^DFGiN7BkMh5foIn%3Ijni&+x-RL#L0v{M(#0IV1r7ez_SLAbW=#b2D1^TRFe<V#wh~b5+*yR9PAc%8@8~My3Fx'
        b'kqKb9lJ^7QXot!;D(hrktS|{fW(jg3lEq77$zPrskCJI@4qP4=6}VcfeJkk+1bQ<KUvC*_z3BTsH|y1&IU1HU_R~X;U2B!$hl-AO'
        b'@;97Bz3<)Z>M*%4njFUzouUx|>^5wv<V$uI^wp)I)#2;INehroarv$${pGK8SNyoF$gR|Da}dwLBOe;geZ)k1jwn``lK6;9CHG-2'
        b'k$wxts6<||@bHSq7;!*yYO?#4KF)#=YMpX=I`G(|h}u$XRs|g@!^4r_bmW95DXJv#gmn11^u9SR4$iV`v`g=r!%;te<>fjwPdK1?'
        b'{>Lbd#Wia^l{w8?G1L=tg`R9L6P3zW_R!uy;o(Of_5}uH{!Hb5wJ-5a1#DA{Q0utHLi3fMW`2w#{PVp+*baKHowi%|?E0xk9oM`v'
        b'm#EJyb8{HnL3`932HQbXiL}WpIs=GJu3(N%Jra6Ge41G{W*b<5o=#glx`2Q9u|<7=9Jnh%?ektd04As2shS?VJzxJahoY;pO+-aF'
        b'7!N!SJWjXJW)Yx4=^rUvdk$Thl$1UcHfz7M2)&#VG`)y#{RKYW*5~gAtgo#_zxB@inv*!7pX#R2pNy}NwTWU{g4*cX^F9euTa(t|'
        b'mGC;69ga%SJJsC;@qL=g){O{gQF>P;7jT2qBh-3!WHQkAPs}5@)>8qW6S%tzFv#G=@&d^5d?s^s`?qzPzt)g3pX5hvQml|}2tE&('
        b'w%jKZ$vlMAphh<mP*P02U*ow_*DEAd8(W`@#=}P>olpZrz7?Ze<e`|$PJFyi(JZ~a#TO<`5FdU{))O}n^ZDtYi3egX;6X=E@)E>='
        b')Zj}=z-r6WkysD(UX3dbRWll1FLbdSUYeVyDK4(m3w|K}T9@?fCKW0Vy5aRaKM43q!(d(BYc*tahgMk(Aj}Ld!O`^9iLty`S-`VT'
        b'P~I9(Umai_DpVUMvZLKY3ZEO$>hS>NWSFbv$Y;Cae9_*c$<e;(S9bnPvCEE!m+uJKEklCRk>7a|cLF%dPgcJe=+hto5-}1^rfW1X'
        b'_Dj?p@p@fSNij(xUQdNQ=_+)4@CMuq4c<C3`egtKVXD!RhRooqd3Z<zFTEU-FA-8N)_4v=nDW7Zr9Xg4fXH*Ov6ho}@KD%(j|VIc'
        b'Jie={9*o;=86Mytxo9sOx#(BGxa|vgQB+=zRcH_ZI9|R7Ji!55@BqwrXNh0ecs)Ckj0WNlbt+VEg!ZF`J#~47V934%P?AbxOg(Bb'
        b'v068x%|o;rR1uj7o&${QsV8eZJL&-DgRxVtjP|*C08}uwVC?L!mXp~%_Wob(>-#`@^~kQc(df@VO^zImzOeJLW%x3<k-P|pulz!F'
        b'mk;x4c%yItUt9o(FhfCTz`mjP{XlF4Lugc?UQeZd^efA+=k-|P*W!WD(&1M%P__H1y7;xdJnA>K@Z#^`8fRYJ)gmIdjw#znmK71d'
        b'tRu^w=6(x^C&2Fp?zfOw2Y!DA5E2(T$Uc0j!d9Jd--l^@4IW0d!TM_VI9Jxu;^DG(F<fW+#4eZK#<sf#IUQIUWjqx)+LW@8^z5+u'
        b'aK`gIKz{47a85@nwhl)b)sC2@*BDg?Xa3J!LQs))jOvKI{SKr0az0kO8I%rM8Iuxd_EcDd!shjTJeAg<IJ4(@7}NZwog_EuL<n&m'
        b'JQPzwb!OGeCQ=G-V2E!)k^w5FUj+|FDiD18M9A4#z{t%B@aQoWzk-XJm}SI2?dH`yGr11%ROZ!y{cbT)Fg_riXbawla(V?Qxtd3u'
        b'x5GSk7@W?Z@Clb-xmU=F4Ssh|P8j$OKh}xjLDpkD9O_V8Qx%LGVOH~;XY9;pJVyM+O*+VAszgNT4wKX0Fz07wXc8CQOuG!k@_R9I'
        b'G*|Zb0w$f)^TH6dw<d{yQ2r+1*Hd|^vZOpLNh48zxF4(;V`N7@SzMeUEnY9x8o}$AT5?mqu{fVJ-b>u1joguMG!Fk$8+k<k)B@te'
        b'{Sdk3fPQ_5YB96?*}K|zS%75*uiewPAA02$N9RXx1PBbxgSc>}C#T9<PQK={x5YVriy1XMW2AR;+6rUjD~DGm;Bqfn46)eafmX~C'
        b'(`)sP`Vg-MX_l28;I83e$kD)zQtV|Ql>#!@%QI?_)_<}3sXJ}TUS7#ncAG>W2cGe<!zmvqKT!gq_t1HBPyxQwWS8~|O~>lZL4|;<'
        b'm^!5HE!A6OaI>YA5&zokdKs5*kwIY((SFF+Vx@9yIxqut#pBrDiy8jMUUEl?hl9RwWERkjG=ZxH4+nz;;r+lPe;?b7XVdn)owd2N'
        b'^!B8YG(IERj0cy+jYfX{>B_*ajS64nh0P~WQ-Q)qZpzKYx=u>-H6k3x7k52fov#tsbc1CI`&O%KXOXH~eJ2u&0VTr0GHv~A7T%!1'
        b'd;V8B+`hI#mcCliiFTLlPY|5lE0a$M(_MXMn`Jr8P^;+RfcW@84llp?SBgWXrdC0pvJc>pKS$tjPV>+J$Tg6Iwj3;2s#hZ3Exdm#'
        b'U3DYBaAP{RC+Bc}<!XHH<Hu=jD3YVq79b?l{s4J$cw`O=?KCI^e`pKu+9uh!MPV~s#HPF(wcGRdL#4aR!KkhUnV4ajfP#yHmJV-b'
        b'!3e(->*cpzXSD%^IUu2sHk^GycGe{`74{YHge>RToifi)_uJQR-3hqP@tv}w<9l)j4nE^+c&6**lgDK8&lNpU^4~?_f(kbqp5enz'
        b'?+k}`5~gg(^w}Y^n4V**a3el97b^4g(Fjzx7tzG-j}AsPs{N*B*jGE(*W=mC&%ProKGApfgly}H@egD}=RauvV0dV#r6oJzeWF>7'
        b'W5+Z=PLXFzyeNA3Ep#v%VNibNG1L-;^k~xiD#s7Xy7~KC4i+67c>GKc@5rsOSod&WUteYJIMnn#wCq}o4F6L{Gah*PFQ{+m=JDp1'
        b'i!PqcfCoakLX6Och~44qGgC8Mn(=m-^SgZ=&0hC7$R7p~>$s;)+|{9I7kA&<CyzqFua`j01|jv19lE`LRZ;TJwO&aZLHX>Q8asmu'
        b'<b{D=R0u#7E(f3n08j^22pnFn+udXP{5?Oo=NN$gKVU8&uPp!nf;s#F%$ccc?^o(MHD77Ve+7MHUu{VDFo2v7A-B#$KG6XoS5wt~'
        b'$isKKWZ@Z^si@@@_H4AQnCv@C%G90vwi=<X)h04Jg)CiuRt2wu!3R5ccUeuUQpmF9Su#8r?DmoM%dP=&LityKY(=>rD<HNNP3CoC'
        b'BMSk(4Fi1J2=Q$ryz2;GKUmI&@6_#t>)rj2(KjM;)|?$PN4(ULQFXUh@IuXkoRLcz$e!U#Ymvb9ff;y!?zi*jDA%;I#7f24Oj-F}'
        b'xIzqj_w9j;B;VchGHQ=5BJ&xfR1kE|V8aF8gpK+6fWHH4KBh%p&Iu)ZAb#fPNUR4)4<wAHlCZH;+|2t-Hi7~!nmZmJlgTA_%wf{Y'
        b'lNY@1o+3*J?F~i3JG=#mWt#It_C=1ZP?rDj)B8{yjX8i?G7-b``(RYhOz4AdFayaK7F^pUOWdhA8zU>{M$B2XZx1;>Dm(v~YnlB0'
        b'#omWEG7FB&(-zCci-A~#FKXw-5`oR+!y5r7J0k8B*|s;UKg+wK`N068LXlZRf`s1QxyYp+%bV1kH2Q+1m%mb<A==3Cld}HR`;MO+'
        b'Se|$qNO;Q;-*WZg6HvDHbLc%h_v?L-jrmJ`*Xs&ATpo)YZK=n_ieuGH2jL}XQwwTILKslt7F3srFb_XHCWDcnJ4I$g0CWiEz!b-1'
        b'{r|LqEPi7bCSOW#mv0rrS@4f)Wk0zOkcvH3RWsTRPnU*n)W3oy2@5vVV}a}Qbp>#5%oi34kF&#@@`Xjh9u~fD6utxg`%vs`rvfy^'
        b'82J7kxBgK%YnarG<+;@KcHQ4Vo+M%6hWcZ$szTjWcKFLAVbO;AcKBYzDNZE`H*TnJhVL77|75GC$qX><gI_>?VH=t+mlAWexf`)v'
        b'U`JQ1PlRmddXLJYATY&xh1|M`wyK0Np{OnmQ4Pwq09!kS{%~9N1+;aSB{jNyI|e(q%NKy2eO_i1V!2lC7~(_`ZTM#`rzAPx9v?b`'
        b'FRhvz!=W14F;Ca=#Iq-)-h!vS1siG6F+5r&h)#I|41_#{M*(Ucf|$opCRCIThO<DVJvCu|<Bk;z(w>^e&t&#UI{8W?+&<;UZ~Gf7'
        b'Du8DIdY>`{?nxCT<+H-8fPHPu3|^phH)RHgb6XYQ#?-ISxH1Va1pF}0(mo9AUFtv5{uJ2S>M-35yQ^ss+OY^f=g#UHX&fh)Z#*6J'
        b'3-j`)@ns3PDWRTOUZ5~lCg6^QdhhZL3I}*}C)6w4mE`h5#Ylahq7o`pv?-w0Vv7PgC5}}ryY@2LiTbVE;951y3T24}inA}ta=HDi'
        b'h<3WT@haT4czDCS4F=;r?l@qoXh!6x@0tz#W@6$d`yxiGT|~gv&u>Sq6EyQ&JaaQ*Jv!q24PD+<X^!34DF8W@RZ3b71Ez5D?LLWK'
        b'A_6o8+JJ(}Y&@!%t~kw_RU1K(+*SoFu>0Q&4DZof@4$E@2;$n~Xpm+$f74xFdxqB*H+0Y!n|L(sAtqLRI5o73TS&c<P7y5|5yESu'
        b'qT6`T;NMuE2=mumvO{Sm_?DY&TbwTn6kNtcfr3l^Z^5A(@bK_{xryJxa)USLW#&g{Fushc0LJYS_VPJN_(%HCnt1r#9JQgA#)H5P'
        b'=Bwx2>23JY;jh0QlI{d-df^C`*i~6IUAqO4<9Vst|2@p#&aZGt^U~i{#4N@Bv#l&N3FB!oLHY{Q@M>I;AXs)SD@h$!o6T1~%F2iC'
        b'wxM67){aU90}>cXa3^$0xaUquDvTQxb|)(dmt?Qb(zf%npUgtdnBZ_|ARUB<+ai^G)|(+RW4zii6^RGNt^hP?f(O&GtGVbg9DECF'
        b'X_355)P}m~!%I=iPXU82#lu}@Qw`QdCpw%MTw^qJ$IESdfP^q&w4Yboau5%PRz@d0aC2<$JKF&jf5rix9x-|2QVs{oz8JH5`N-(Q'
        b'#qu!0+1C}`|0$m5M{H2vuGVB$Ew={BJb$yABY8}mAv!eKaYEtSYG@<zOEE3KAo&P&#;Qof$k3LmEA!#U3R)%xzvsrSYObpz@oa|_'
        b'^0ig7T|J486H*vlfp+OruIs*G5q$J;(z(_srQ0+kr*Avowt@<MOABhfFnn5Jfe;3{@mqm)ky5g-U~rN<{}`$P<3ZmW4_);C|9FsM'
        b'^!^a^pQy3J5bSZwJC1<y34-H8#-+prO3xjDqd_JZPf8SEFt!=}gJH6n{G&mtmd6Cjs2Xb$pGT@T$)DsYz-W|hnm7vj%XL-(I{O`4'
        b'b-nA&M8ydy5PCpY=^N0kIkW+H*QD@k>!Ii~Z!@TN)tDo9$U|8`j?DEMIej-GI5|if^Cqf`K}wBq*TTO{W=3%o9%TfopvTYOT0Q$}'
        b'6h4LWF=bNJePM==08BeCpj+g$pe+sx9C_wQk*N+dYj~{-mH1LXJYiQq^H3YD@*#X6v;Yt68<O@Ns|NyzFSM|$Ly9kVAFOYdd3gw<'
        b'Dwa<LI$l;VWyN$oC+omdqd+nmg*R|8`g+8Q<RDR!_eydQ41xV)0CiSRNlh=RTmj)5kvsrz3Z4bIu(mj9x1uD3J(=T4wc??^xZ(jG'
        b'0%3D`x@-!4E#f!0>Y}CQtz7GVa}DV05C%v@+9G>-t#VdBcPo%AMe7ESus&6BSFg0Iz1~#~#4{kIHOmG^*s8g+=Mx<-OJO8$ZXMND'
        b'P&qX&(XcpHRJ((EtVSgoMpH%9+8R=X=tp^^n@46Ll*US=*CeTa;>oH>G9rYohAjI@Yt8rf{i6EmK+X#NlgK<B(5h86+5Fa-yM8*5'
        b'Tr*Dx!j;K>IxsPN_c6&ydzKat17sloJ{hPzLkGE!E6kgCtpj)cbl{MPPEwJ!6|p-w7Z&{>8OyGQVW%gqvz9OY_g0ZLeqX>|1yyQ='
        b'HlHYof&nH6&IQ_?%W8(n1o4qcdlWPU891j%saAb<Xu1;x6A$OG<8b}L5q>WQOH(kVHcd4OFx0O@4^#7C>hg}Y0!?7e;kSdSe^|i#'
        b'Gm_zss_8xj5({bKGdu%Y188>fI|}M;tKXQ3dJ8_3KvU)ovVcwjbsfITNvyz|uMEDr7>E9H3bFiGkwShx8XqB44RDc*u-Hg0a0{Rk'
        b'osh~45L}2acI)f8?3-H#E#I^AEekn2eD%NV>rfSc*o)u7!>D8$-Wc*#{Msb--|eYn_viLbj9LrZ#-T;JU!S-86FV4zOfEGPN8KtI'
        b'-gSOX;aL;x_bChK4)yo3MR-tbn!nsSlz89H#Y9d8Gmpei#{>(B({>fut2;3+@V!2bRrlFdA0G0722j`l*iyOCjph2Ea|aCXEStc$'
        b'Oy8sDZ`-+e*Ucgtum^P61HaE6q?2EAi9J+Q*0KE!`%d}7bRCRFD^HL1M<d++svWF^@}mkW1lFzZz_xqrcxY@>_Tl`@`0cOQ$p8ep'
        b'j|CifiG_@Q3dVT%*vZnTYX3>N0noJ-BZ6Lx3#U3Sq^yJIIfI<G{VI4Q_9d)$n?xQ5qYYBOfN!0AY6Ol<$7_KdUI`NaLsOWzH=t8U'
        b'rNFP$;}#&?lBHr&^^~?$lCO*3{mIUtg<Oc%ongXG-oy@R`(XErc2Lb_Sj`3d_T6?o7C`FYASKG}yGAdZ-ZH8iWxFe3wu>;EzUc1u'
        b'-`eqPXytr^O$dMnyz3;o_t|^CUN9=v;`eBc#!84^+s$s2LF29BMXFJ~mZhHJKu2{55-XXv5$%DVjpTt?|F7+xI3<D^XtaBy-PJZC'
        b'X%oL6-X7=`#d{wYd&L;@9N+u6h#s?{U_qjcD1ONnRQ}~%SDQ;L-+ebB@c#Nsvp(>}-HA?IU~9vYa^mMvY(Cvb29PAu^`_ZNq8EiD'
        b'f}9hrvkPh^Rmbo7viU#XmH+rJ-#<{ak%=eFty4e#*8i~G=VtM+iO&{j;_V5N_9%H+fO@%I#lM|T#M!HE0i?YB66`7e!Wl5Xv372?'
        b'T#%fLviC>XJyD=|CAHkf4Hoqs%-P1Tx<x5CIXH?~Y^Sqa6?l$=9*BJ;8?~9KrSJ>Bpgp9GKeC{A0ky<_&*suhBFtgLwD)Z=FaUdS'
        b'v`Hj>yrcC(6drotzfdPi1lmtuhrdi5l4whe5rrvYBcss}D!|??uoD4xlTF(7rc^;ItOo<&+(Nb3#Jz9(4kKMX(t%fjD0BMYRmbs$'
        b'#I%OwpMA-N$dt9vHp#rc67;*$Iu=Ev9c}IC179Fym|2DEX~av;qccdM$A-(=DyaAGy-p7A@{&ub_bl@soI$xW-nJEBfT@#kWU6Lu'
        b'_jpRzlS#&~3*vJZZ2cE(-4|`1i#F;rNQvl8!)@n2xAlK&>ppL@{J>_tGW_bf&usl4+PcSV07OT_rP}s$pV<2UX6ydM2ABoY-b=M@'
        b'=RUIa581juvH_N-ZAZEtCY`hO58ArV*?>sL49!-}f++~3O|$9oV!x|c>+!&IL$>~2TlbJn_Yan?AMQDK#@2t#)_umN`y6mtr;d!-'
        b'lIRcRD$HyQ0CWS;=!t38ONRLdq$SgA5*gO^=Ix?$y|(@%w(ee=?yoG2p!w`eoVP{3KJB(Yu40vTFcm=nO??J_X|K@7-2yU{J3VUn'
        b'sjM&4O(6i(H*Ea}ZQXyiS$f$+Pic)yv#y)nY-Uf`xei<Z0b6&6O?Q-~*7+-5s-L?92+pAltub61Dg7jhckUHie~qo%Ya8rj5wkHI'
        b'jM|}RwZ;f-q|E%v-OL`@xtDGI)wb?KHcKn3+58e<tKj!#+Q^`k9hq+iooll7|IXIkXoIHuX5%v94}b$pHK#H-Kh>LL3><Ld(2?)J'
        b'D(Z0v0zS;WB~qCjKm%D&jfBd8FMg4Mi&<~>Be8Xb>>Oq5r)&TTJkQ#I5C!Kr3H-bk7I^MO*s#yT0|MUsdZY&cjWIbIE)*s<X%30c'
        b'J#XuO-q!ts&9mM{<-xMZib(s4L{kGU#=}hQ)lxgplk}2%g)}imkvj0;zOJAmi=Y4AERJq?BtG}mfxr%`6t2<banMR3sxOxu0L#??'
        b'lK>~HSZ{V`^yOysX*VJBeo|b3Aye53Wd-MAR-(d8#I?I9CgvDw$v}o5?Gy}Zkdvoe`~*Q$V@gl3E3)Na)6s<T<)GS4N0Xz=WBXhy'
        b'z+>0ZzPA1m^!PDqcrWaAf85SE+SadF-zWTrO%S-SrpBN2gt($$Y5CFQ1?A0sidb06^@#90w){k27rBY%wE<zz`e?GN$Z_=2)mu%E'
        b'COFKOOibTw*jWG9VjIz{9tr3bjxR!J!ll;F3ETP=s=k(v_WqWgaqER2v1FVmW~J<$!qy)R=HNLG-$t>J=1vyTvcQM!<Q{Uo>C*Tm'
        b'@Yko><2c=?_+}G;L)Fpp4R{)RL>0CLdq3n#R4+Wkcr9$fIjOBb1XT0_)SyG;l5gR>dEYqVzX$F|v<9&@67!?WZcnymOMi)v&2pya'
        b'G-OjawrfRZSWp?2DPK@FoojC>-rBG^1=Suwj00s`x{U-@{F-9I5%qXWQ}Q$JoqhN^re8YAZ|nX{*37#TFoOCxSLOORtW87RfXLu{'
        b'bFcfgL`R2|rrI?pcNI6h?LCaR+o7T5(U#cs);{-8L-Fy3qpOy6_tAhu@BSC~Rcvk%R!#XihUUoPW?4>l`rCbGLR@?z(R4zp-}t>k'
        b'9~mw9+)RWP=QfzuZ!#13rAXxQS=!UqT`05h_OKTPBWUYIR&T#W5}~xGSCTu>SJXyT!)f07DtCqiZ5>PvKvFgvkm8#Pd?9xRhE9CV'
        b'-uK0G?mfEyJzDz3e7w+!+w3Pf$a1@0#52Ef*BT}Qd^<c7rlRi0lrSLXS6J_RB5OlPcMnavQ7RfPJ95o@*ojdxyf{M^ezCus{#ufL'
        b'Q2|>l`JQbIyL;}>wENY!`(LEJYml#bXFmd;pvl_}wz258JL>HuFPh8*sARE=;k+h!dCANXx4WTzvG9stm!u8FtDiy1xUf`NQol5n'
        b'H&!tlGKq~yd_z+2P}#&V=+*G?PQLFwtaW=79z4%C61;rFl6*335-WJA!XP&qLd|a++3<68@Oz{zWW!2y@CK4UP?m3y0giP|MZdyJ'
        b'$aeDzWp{*dfO~~os4Y(AX|`hMseO{oO9JpE?#=ajU0R_mzdx#whcB880R`}NAnT%ucUe%!l9z?~Lr=Mz>T@^O7Z*zN4Z-^)`bU$E'
        b'Zyebiwy3~aMirOz75`dYyuL5@*Mjj9+1ASN^}7OcbFuODvfccmj4TXSWe02frCXmZ(-k#riNu9wL&%mDRkMs?speNSzP13%3aNRs'
        b'YOc_rH3XOq;jPJhGZCIo1cTPaMnh10|2k2=VR6+>#vttkg~KN{MdcIH3Nox?eZE18XXp3FH_HlnV>_n_fZG6m4y`A8*ozWS(ILC`'
        b'jU$=MP~jU0j%ioRg^Lk9L~96vTGMU)y@CNZ2I?F&geepG?fq@t)C#x^-1@}AZcuuZ2>YZYKzkS|e)jG3QmM8T$!uH*hCgdXK}l}L'
        b'C46!E$JJ-gVxz0&Su5ljF}-}SNI`WayI4?Ip2ky6n{pZyaSbscsLp{9g?j-L!4UG=c5Sf46xWbWZXyejPf|z{yrwl&O+q>QB?K1<'
        b'_X45|&(Ok^>!XZ-Qy{{}UN92UtsRGZQQ-({JdETvyj|QZ^|m6o4qpNfVF+Z4%-FBm!ei#g;qf0vP&}}t%|8(OqHlM3%KA4iL500+'
        b'o3E@JU+e2nY*p~veV}t~-O^HC$rDk<>k~mUW+G^7N11^k7H`>9w!MADmK{|$3s;+;lrXE8Z0Uay+lOrvtP8Ll1egryaX_ya0vZA5'
        b't-U|I)Jp`ydCZOiYaApUekT>|@Jzp|ndc*<yJcg00Bpx^LfAky28{e4{SY!ln0#uELoMjK7Di{1mvsXMuDJ4TN0U_lKE@D1fWkGc'
        b'#KKDfW-vr(Pq*W_M21+>WKoszLBF?X9^bMh&r2wcL=>oepkF#JM7YWuxBjE7TYp}(PWU3WPBaK4aPO<g;pQ|i5rpiF+|%N4%rJ%^'
        b'XN}cUV|6sZAmUApBE#3!#Tg3W1RISxLBr`S4VzQx;+?XbOo%?l*O1L%+%K}_#aM+~WHc-WGgV>WRrH5e7!Ux>*b6_J2LKM}T1g$m'
        b'4A8;Bzp=uNtaF>SxH7RRAS^l#6@JF1?`bG*X=pkMBOhx1TAi*_41UN~%~(cRWZwdKQ(h`Ub-!gZlhDC!ta<FV?l<t9o>)4`9}CV}'
        b'V<bX8<6jBZZbGBw=-?XmJFB&uwt8smz^fz5@kM}8z!NS=d!XIJmde6sjqip+rQWzGc@g4$<L=->KUXR;Q5x&pE6kC|7tdSG1_2#>'
        b'ZkN?&F!xJsGU^5E9f^%MA_P(!8mpOjhh5%MH5R_!Dt_xn8yBFf({AL_8|<`!_XF?ZJgHW`#oqHtsre5WCWv_$EPlq9=0FICNB!aJ'
        b'TZyRJ<FG}@{>`!S^SA$FkIeQII=7+PD5Q1``3g&}M^u*W>#VVx$Y?RSDWF?pg>2+HxJh?B)%|m8r+|7KzO+*vYf8hOG7FISOEICJ'
        b'?!)k<-7Bq~qUL_HArQ0=S&Z)PBx{EXur@!3uU|`C{qiuZG%gur#N#{BE8Wyr&~K`%f3o{(SYY#oAC_x{UjnF9R4LinonRe7L2H+)'
        b'IeU#CEEm}D<|*^w1WO7KxiP>@NXnz$&M!ks$^R)o-vG8E@>HmGSs1m%T6|H~|1XQ;lETDoIzpv`eNobwhWXq-&23dsKY=xZ9Ts2Y'
        b'o~@>-N$TG81X<6?tYCg%EP3G;O<~@|Ay}{j(Qp0M%wM7(yH#~LAz<0H-<*a@r$D|3YcsIa*B`pY&}v|}NxVb|bh#A(M0tVy1pyvg'
        b'Y{G05;P2tF?U={cFFnS)Bl%4BwP3{0l$4nbVx^I#omX1|3pT`sjK3svQThE+`%48P^ZR%0rIslc>Cu3CL8UKC@G!aUPN(=D9(a&!'
        b'uq6$DTs0jVKoTK^sDIl9K;^&3g2wU<n6iL<MgnDo{;1Xs0K$0jB(-5Bu5u<3Ay)!oxl@eX^y1=Hz;8<3bLr_b>F)Nv^z>ry5UYLn'
        b'C+RtxM%|bfY=s8oGuilzY=n;o0<fDst$Nnw(NE3#?_+a3>FfKTQ9ZOT(IgSF;nkgd;X{DJVO5i}k62q)_JoW@o&WsPqX|co<H|4g'
        b'C0>M_rI(P7EI9s`&+@1kGnkUGJToCZzw<n8Hb~E|fNUucmczX7u>;EmzU7jkjy)ZHmoN1VUFz%T>+0B4H93B{ufNUGqiK(7=h?6;'
        b'As2<6XlpV1$sFge62P+S!?HJV$>yVL%1irl^_#W{hIO3+%K`-1b;|i%wfR(fQ-GKOg41=^?xvQNmm(Kre*aL#sa2zqfdi3}UeRve'
        b'^r@6i)TSx9!qS@B4p?i|<%&%UFKt=`YS>uq*s0ik3hbuSk&8xS0+>j=TVlTUVqe!WY4OfYCm+8Qj5;Yx@i#KZH;O%fs(G{Nv6Z`J'
        b'*}M@E;Df$q^;2{7hkG*i(6$fh>i|ITa9#K*i(HCa2neCpfQ*R1P%G2f!5J2;*TH{q>y<|umXopyv#gRds7U7vy%>&>hFG&9E&=Nl'
        b'_zdwA6Ole5{`mhR>)ivIy0XRL^T^9^unCWd;N#>#5K!krXe&_tN>b!y?S)h$Fw+hJL8Ll^i1ILKPE-g=?<iUYYVRb`RG@N&SS!Uc'
        b'Lqet2!i-?8kI|`O(^9AH;G@>6aDHo_fbG5CKal-6Yp=cb+H0@1A8R$Y#2)>y+-%)LEf2O_0X@;JoIgsAPlNFrC~7eL#*qLD<2<`E'
        b'j7>%cvUO#2Cu?qjb>KH0D`B`9m=Vibb%rpzA#~(y#V{-h$~by3+P1jHG$6AM$n*o#Ol|uWyW}4{8#(lHjqBwao2<rp_!ZU%>40C)'
        b'Kx=WMXjIW)2-{ugQ~r(*FF$+VmnWX?y>VI&;JaG@WMpw&j#(MSC?m`{&zO~qnVji$&5SbAtYnxRS>07exy1R|0#w@)*=9B@VU(fl'
        b'Z)zfM$4i@nv!m7~RHk3){`Oo*(n88@h%*}&yA6?ULzLSP(KD^)H1Lm&pnOj?6QbY4gpaf<m*jTIp%v)=;PgkQk#{-eZw>^{P&|5~'
        b'cwga@)O$pp*w)Ly%GV}uvs-eyy3GJJczT@FY=|%iKhqctbT&83vZBm}NK123LPdH+F|_J5gjw3Uu8y9wM@<JLodyQT2EDth3<Dw^'
        b'N`M}Ywe7D>K+cBD%81%-^Z;k<h(l5JquGYn1{0!-obBOG!0c!viqYHqxjgZDFZBAxb@|oHD7s6#FW@|4Sa{d4fPIq%#N(xEWgK7+'
        b'pzkUdWJks4=#&v^<zijVbfBb8xn#_=KfZbF(SEfuGP2mj^#V~7xa_tO<-*J_cUGnYbt!R3goz7n3SOJQ7@~BBxR501=3PVNlIhAX'
        b'cCHs2e|$%rjEs0?q_u5-*Kc;U<+jPeVsTE#&dzcEgX}$xcXZQ$G|&~W8#XKe1idsJRxW^s4piZv{h&|yCgeKsnYCm8sU;_pn>b1;'
        b'I>P-T!z%YivJ{eE^A-sxX}=7b3jj;2B%+tHn84&@oA5|^@lW3iOFr-A#m`wJex`%?xmIP_J4jS@wNGQSk^HFdru-?!8hRMLX_!40'
        b'Ro?&Y<h_csOmy`A-oE@6;#2&g-)O*PL65ZHAve$#!7TC<QNfGUI2ASNkF$%cCg#uofGM}n3y#<|?*;kL!JV#yJDt}5wyoO9u0Tdr'
        b'L~&8*<=EmppF%o(gf8qo>mL!7`?c5CBHBnO-s##6AK3fvas#^tP6D7FQgwO4dy4jBw%}pxsQ+bhEw2ca9Hkxq<_=uN6vgAr@nif2'
        b'zJBB=)cYPBy{$3+Yq_Xh{HC~K2y~=V0gA4gQ_sqWHtuw7ghnpd)H~VVAgsDJSG7^1qo+%U{;<=v9*RCk*YupB*s1+R_E7w2T%MZ='
        b'9$p~5di7G*D%17ehp{Es^Q|qtU9Lgjw&QimD{}UX35j93McLxt6?)YIg^jL`wv8Z#uQqkP*W_vqJzw5?s#$gxzm6iz5p_z>cbr8z'
        b'kf2}lbGsN3Fx<yyC}XE<IW&K#<}%uzN+Vl}*M?eKMgUr?KXeW0H=#J_x9tR28*W)Ph(yY_;0`j{9<{`xJ#Ez+gvGx#Hpf!u4`X6O'
        b'S9;PqRgIw){*A9zRjntMOV?>Fo#pXK%1fq}P&z_pwMR#?tUte{rJ<IC?uwT1f}a7VrSsakhW?_ay~7_rsTLfF!=V8Zv?j+-oIXL2'
        b'%BF?FxRe~}4NtjySA{oNakDGn(W6me%iboCn!}$w85B`Ib)8MNf^Q})osG7E+t;TJN_g=1IG=Jw6ev_RKX8+K!?>Nn5<jO0$w_Cg'
        b'n0Ft73C>!b>Yu)JOH#&)k&L8XN|?Pjn{D(@iGSYsQzghKo)Tb?UxM{oAFKenWu^0X8ovhN@H{s3#SYiw9kx?DoYu4K38cR)t1MaF'
        b'+i-YdPhoylVaf+W-Nz3z3iE-x4AgR+D`=F=#;<_sinM1~MI8T_cuiWLZa%j{pDJrHz-q&u-NEmHS}oD0<3jsYVQ(9rTTI)UcGS77'
        b'g>*~kT7&i7X!ftD7HA}`nwHoeA@y=WCPCFa^dBW#V_P$`@wM`&s25xW)GaQ3x-<(qHn3?~b~c+8t20b1GUR6LU$(M&Www9js42rD'
        b'%e6!sf2<45jurit)8~kbUb3($AN*liV{TEe@uwzR&2$WFWPfTBH0~{L(or+*XxpVp-ij~#VzM_)opmn9-zIzt8#|vQw2SwAN`toJ'
        b'Ng*t*YH6b__hIkB7kj>&XIkA`dU&FwFn<@KPwB@G;peiNny=7e`kEA-^@08m>*{2DruD?EfeaP8xUI9|&?Xy;CPQ{7CA7OD9B+gw'
        b'ZevWiG_!e!o<QeIU^1452UpaVY|xZHM~Gg;x@_%&kd-$`On*+))!B}`Me3tOZdU~0)-G~rIeog&T1A`Xezm8Lv47Z+dr9tEvSY**'
        b'4N59hK^*Cs_~I&N9Ib7hA5vaYav$CHupT+tU?;4m`v;qYM~4)zPh57T;o~IY$##)v6{kqxpFx=~Pv{$;DDs|kxx6j!ns6$8Q7i%y'
        b'L(ZQ|2~qeAQ3Qd`da(*O8^van%W7vtvPC;8+@^9FWYiw~a&%bnKjUfm<q_0?)18QL%H$NqPm;gpMxBc3sLcLLndd(_#kt4HNH0P5'
        b'#C7i+ptUq(#fQTb4Pi6PVL_LgLUdt)IoI_?;+yInov}M?FYj>MQ$5mW)}`0@V?Gx1>L6#>%so3bA=&7v+v*v+c3UJ!Vb<AdcXl&j'
        b'fl*CNSa5`yZW?JKbzut1-yAk$RZy8pr9rRK=0^}%P$G8NMz_fZcp1)w1%+6A81w2G%<3S~eNGn^Y!91x_GIJE^S_htxjtgrnXj{A'
        b'!>a>9S2wR#K#OeGHW=#8c{{EXgMxN}>Pv1_Gg0$54%*eNRz#R}UQnRlQqr2QC)X6<fn_H=W889BZ1hzk5C{Sla-5>?7E;T1ZyzOl'
        b'q^+Sy+XsU}VE?$tad?6Xd55riT?jY9R5UracbLk)yQ~chw(Ng5D4;Pk#6krmT4<l9T}`IC5ilI;LaC&*SW05NpY~GSt7-XZ8)uI#'
        b'l!_)M-*N-rpnbDZ&YDAC%W*0NAU9NdCr|`UU$k}8O!Pm8Ax<}kQlL<zRIC7%6ck?e+IG-N8zRM~ALx)ByHC`9NYu>3sGvH~%L3}~'
        b'als&H(yEuZYgeh+kTa@5y?|WrOm`gMj`2G~!CPLFqVN`G5Sj*%=+mdZCVE6LO$+u<AV&|{kMZHqXD+=@^k3&d5IPz0*(3H)e>Msc'
        b'Jyi=RYx8BPIsmQBm#5}w^Zg16CL%PNou<fJ5q*ga9od)sw@Dtm#VwcS^(Bf>NamY=-af1pxVpD@zO&udy<K~pb9km}^921La>&<t'
        b'c4t;!%BCe*osAbjL(i$pI#F~q!?IB~&+nt9_QMkyuWGD?`Ct^(o}8Ig+jLKt7lc+c$89dF?^>H7$&|ZNmfcs>xt7ghukCE<tRb<i'
        b'a^#*9Q~u6GucWj4yyCs6kNvI5q?gs7gjOu~D$2`)h?)p&gLvEMg_1(q+P!-HEWr4?i^u+=>sx&J#M#5y$g1%9p$ACp3FYd$Bl<Kc'
        b'Ccc|s?Ey7%KcEX%PUx6mbEt3D&N>@lmUS!J1!g9E@F}Oi`lQPM)f}Z0$D|;?RyFtB{N47;23OVg&fjjgm2WrxsJb{^moMw*PpGqO'
        b'P*?w>Aj?o>%f7YtURIysKcH`bKeSM^DeGQFVQ&@-ONXv6@!`GETWis3JR3$($UA#bNadx+kCg`#H5WOaK9@lrj3*C+8Y^|W0(56N'
        b'ok8f?Fk#6Aa3Pk)O?8=BdrRF#2OCR5+N>G5)|Il19}_b&a?NMv>dw&FLs_o6o7tMIy;O>2Xw*>qT=tDD`M0;S?}<P&w&I}pjVP%)'
        b'w8JjUxZaE8eY?2sPJ=<__~V4-PJ>dWzx~~)!CT?F1Th-mv>s&Zze84D&b;(ocb4JGz3f{xC=e%D(*Uo*fSDfBU{UeCg6cfDf@01K'
        b'uKQnIH&?w4k~{ey+=x<O?M77ry5zcekU;iV(S$-eAv(ZeMo;#wZ|{kYb6FQGZ1KwM3t9JaExqvL9(27p35JS=p{m))&rKXp?VDHj'
        b'Ov-(M@kbbo%rCcrft}XZ)kjHZJSLLoVC=T7sTWMAWmzYVhM-GNzk3-ykU4<DsaOufsuNge%XV3aEI%-Ybq2YG$x^2c=?wm6gC9W5'
        b'!z>rFPOOSs1f%wJv{t~-2+hZj)i#H8UNPUiWWIdM^}uYqXI8yGo!?;he8hpJ!}BdQ+wEF`e7iY(xdYu3-Xz+eAK(t08_y!bh3`N!'
        b'1{o}u87nqsUx>Js*}g6EaKr^l8hIk3FYQ7GBg<^umVwx||2ER;EEm=b4mr|`!UN^&C50+^R$pGI&x}n(Zqdf#)$7_0^n(^OYhBx#'
        b'X9cwfgzX}Pg*KF$aX*INo)CZlDOf(S9Bo$g;A?Tm%M(ZUE3~0<3!V};T^H(?la$gWT6>}HUh){{J)v-X%jv5g=jHqM{|mKW)Hma6'
        b'`Os;z>$JJ^wAr@K%&tXt(!2+8mcCP?nu-ez%&eR>>vGn_#~A*wE!QIZ$dYjp-46t4FtI-34(!5VD$ZaN85#76fKlWLatkeT2-~6)'
        b'6&Kc=`e5ya<nOqm6XhTDuD!5c0>sC8+M>rIUEG26am$7BxKVyDL<2_rOszaaX9(6Bf<W};8A7u57lp#o9#Z&qpgu33pah94Xy|gD'
        b'6%=*ce4JamcdaWg%I`zA&Q{l{cp%B^f4FwY6FZ^kmY}%~^Kd;VEu1b-p#O@z`MP;H6z_c9Y^yT6kG}4BYkIO2bec1`)`};tq%-s*'
        b'(1iZ2pPjB1?WE2Ss5K}YHyBtQx*vj~s6`iZoUWvHGS48_8T>r|WY&PPxeB|PYQF5>nQFF`0Myk5d#0~T7iD1Ba%unPTv1icRbcQu'
        b'7Y&PCUypa0&__KmyI!u#WM4PmRR-5-N=&&XOK4q;Ss65<oLQ#?^USFX8I)GSDq<XOCm4f&o*_VWZ$jUEcepR8-FMh9%W;tzR?fP%'
        b'%S_I2y<#?B7WG>2-m`R%2=VQUoc__j-Bt?433A1;1J!6tFc5dT7ei8YnQ^+K;fLcAljlx_rN<TL`GT?BY&eF3c)DG2ys2{2kqPaI'
        b'y@l7LuIJ6et~jTQKkJGI_}{{B=*?1)CEuEv;MBccMIG;t9P$}jXm%|$+b*-tqc5|coA}EYjsA81(7CkOR9i_!ZxdPisx<8-YM@=j'
        b'zKc-1CaiF)-HVHcEAMLE(GeqS{Ubx$h2HgI*$G}?DIVQ6pPQAD6m2TlmzYfJ1rs&ZUOm(-k473JQ8$$4a#V7_EX$>qp|dXiRY3ze'
        b'V_e*znb(;Ay{O67xbeEM4(IDOb*ip#2c%??CM%N)GQTuqZGQH~cGBsl9WI9Qe^XGheY>fotp2F=*?rO0vihjC=IjRa_ItUMe?E`&'
        b'na&67uoaW>1i6BHUf~9$Eqv6S=au;RujP3Lh1M`bX9&po0XT^g4IjbXM>z9Qtl?dZ3f3tDSIr@6G?;#~LQ5+20l}cLXtn-QN=S)v'
        b'%X&YUN7VFUA0_9O+#gmd+{yq@V#VK+{2AmJ_a>ModFN*7ANVLN3-7eD$U5$9VQrUK_tF0;C_;xuMQ?qrAVdt76&kXcQiQC`EvHLX'
        b'j_5au(WsHx=xFW)aJIe}apXOKc%X`g1-YUY6D5|E>@DwpWy5~<W&=AMO4#}UtgA=t$eaEY7oisy)hPFl(0TxAXn<2w!?{^|^!rdK'
        b'`<05g`9s@T+e!HJvmUYP_fJ2io<W}i%~URE^^1pdYVuLICuLx&Ffr+5V#fW9jw6@e_5)IcBxzrjYL$VzleC7wekb?I+ce}}6AU%6'
        b't|s8FTecTjb}?cwA5?R_6m(b9O4-4;&N-EViHU-&kS^he`B{P5mu6&d6n)RZ$NGS82aXQyW?gmg{g~+AT*)Vs$G48^iTOFk&)<}$'
        b'2$6AO{0ixUjht3IL-DzXis;Y8Fl{IXgms6KT7%^BOE6xYT9x0Yd#~6&btyg<Xg_|KHl%eWrDbZ?vXt<yQZb?ofN7tm$&SfZX3Mj2'
        b'L@>qxjN#|_VB$^bs^B@=bF(N#qJDcuVwwK)FLh^EWF&7_+!rSsxztUdvcUv~<rPifYer;Mx}$r9X#O5zwC=?{0yKl)hN+y2rf4%$'
        b'anpPZ1JeXjl{cZFTKc4UaxSX^p}p^lT}xS*!n__e4jG5qQ2T+2o3@vfl<6;B(w<uZzx64X_;;e9RiQx=bJksSJzrBn2}PeHSq5yf'
        b'x2Q08%}9O!keYQp&vq_iMTelI$W|F!;a>YvQDEiWELD$mZ9sMyHDGtAnhinhdq(~gAt+BdBg>vDO1qh=NV}s5{CW3Mrz@@<*0Uf_'
        b'9RuZx+u|&t=w}XFE>2#|nO!u<Nty+E)@gDl<z%kuex00^u|VNEJWXjF_r~+eW>q%mmwwk(vvs08E(#QPOQkc?&wloriPb3PV;!uf'
        b'Ypu`QyXrc+Mmj9LjjYv@e=v?nR&ijJRuzhr+;WL%CFpGnC>|kpIl|egoB?Q^3Yg!Z41g&N6WRDkBm}c?TFLv4Pu~80N!9)}2Q{s#'
        b'*5`IN0q5lf5(nQNDLq5OkA}eM2R|T^KjZAexr(a0dkTB=RuY3^besj?3sy{^{^pFoDNVL>*qT#+@hODzJfWyC{6vw%r*N$Uoo8Hn'
        b'`(0?F{CR80)6%z!93h1@=w3C8SJ(}4Mx7x{zltgX#PbYvk$(>?QOZ15Gzi#Ps0$;?u)8kVb-^IXkN!zy{~V~Au64<rAD2WQrVC1$'
        b'fwlz{6q2kAeNd>%a=TN#Q$uxU90WzPPpW3a`zEb{PR-Q0WLkq#3({4p{an<WguBm_^ax9mXmwu@HD}mW(N1U$bJT{p1;@G9qz7(`'
        b'7f`%W&;GmxV80`zNPwU=glW%|gwI?<5o%=^_2O$p^zZl81Yp?iql=ma6=Kn6NN;fzG5TQ6EEW|8{mb&n8p+qN)HI%IX*t+^t?`n@'
        b'()5!V><}@qI0G$ROSgQoS6SU7hGneo6IeHL&<*6M$KJh*nBSWoy5i+=LnBJ%u#$HD$<+B<lkLAu@wh5*I*9&ufycmP4OO@XqAEe$'
        b'$JzDwe0v0Lv|c!3C+1(JLS7@Se-@tq?Y=!1Wz|ysY})uOdM>pbxq0gte+R5uKj^029j)3n-Xqo><~~YjblWthJvsYZ@y<lkXy#>&'
        b'Yop0lW*QfIe5bd#J4;RR!yRq1_>oq3Ny7df@uHK2^U{+zjr}mEHq464R2ybf<k3J$3~tJOOCB9h-vzzL5IkZfhF!UCSBcl2RU3lt'
        b'8fJpBRM5!1BRvo-Ee!rowQ|-1N^PLk%Go^W8w}xUgOY99!tXbSHyFZ_Ps5DeeWG1ZpktuNq1mx^QdAfvbM`Gjfg>^*eL7Z}?~~mZ'
        b'NA`cj4O?-bMB@91Apq8}LFI@7yV-bQej61+QPBx9>u39Vtz`gvSgF#V7@c2hI<XJT^=oIZwGG9aT=AyP1e5K;HumpGWq)m&sF{0*'
        b'Ouo$-M{D0AU@f<}O{V?&mT6uJdWy$O4|B)bEbhH`wwbE-^Q4<^>iqXMTbK!5C-VI4yEoL7<=z8Ur<)RH4`+{LX><lUD^q7s0_j)H'
        b'ki@*dEw@%49S8IYP~-D5g(md{QEw~`G|Y&lc^YPbI?F2rcMXARbi-waY6s%jbJwOgcDa{hlUD+<&UfSjE9@Odx7vRc74v~_q@p6P'
        b'K7dmKDsa{S<zshcuqEg#on{Rcs56AvT}7S*M$v{liD)b-G;vveVn;4^Iut2V_2XVG$L%U|!gM86{uBD{iBf!x{*ph?+vzHT7JVk>'
        b'7k^QOQGvOuw(BoG(JMrXTSC|9w$Asq-D%r4!rvURdA2!5ePPZ57zFs_xIW>L4o@+BvQ2kU)VmT#m(2~d&XtPj<C3BAJOlibf!4m$'
        b'+=1esLeLBA@B||H0@pvl89l3-kt4f2m(2D1ZP%qE{S~}wS@1vO2ior6Rf6&fN=zs;e(BG`Z{9+2WWV{daMe46NQoJCZriY9o6Eh;'
        b'=H3R&2-t_&xaXg~&=`zt!SZpvl%Rw<!z}b?cIHRh^3c)i99@5f&M=o+2yC5vh0`(Ah%zuEXaBG=z}30U=JZ0s#)Sn}eJyUo5oD22'
        b'qP4?oN9x>phq*O@?-}B@<sy%XG=GB&4PZ1Hi)+Z8mFU0uw*y`ShBs4=aR;LC`bQQwB?ZPi8YJqG0;z9J-S2W?5ATAqHn#s{ZJqB_'
        b'B@|6*_87Z-n`_TDGiZRzwv90IVMb<qbKBUX{f_fM|HR2HrU&Et;PFOxXVo^#-Hs-iY1jTH_ugj!X?g2#>&PAp-8zJ9NU!Q@Hc+Yu'
        b'V2u8p{0&Ei02lm&>;DSbXfU4MDd%Y%zxK#1n6Y=oHm|A=5VRi$d95kXeepE8>h2WoET#*kG!t7=ghKBL_oRw5jf4F9;zYEWk^D0!'
        b'-gHCTCqb`&WiZ#rQ#Pg9L;V|1=<K-JpFkXAk?(1wGn!~!Xh0L*sLBe2M)$tDtyK>HsfEz80G()L#}wS=EPaP=D@V4_7P_tv#qZ5J'
        b'0Y-UdorbEj!{FKpw2mp$p<E{VY4V=(<l^!pXJ(|!r48<g`m7d7?Y_X)X-sH91Tj#G_Pp$9A|b{59m$*0{s$b43n<+{H)M*d4V35W'
        b'@dF8@wGCZosBQLfyLl(>o_~&CyQ=-1gq10GHJ#fgx4uiavWVV%arWMVFS)004$|0aVumM;v0{1o0eO8ACf_&m9+U5%-M8!l`ask!'
        b'cHDqz`b8Cqv_dHmM|+q{X^b?Er1oVxw)Bu0NpxBtI+wc3p*K3HSJ#k7X+`rRuLo)>K>Ly?^=KLye-uFYA*WWg1%I`$?UK5^>`BC*'
        b'%)AiG-lI-2bNm{A2*>ynn)kNmGV(+%orY@?tE_f9v5nSrZ>5B-%0z~ymH_<$wQPB$1_&LqZmDV*Jv|BjNMH3}p@0&=pjlM4&u+*P'
        b'YUc$j-tyJu`?m|6eTj6^Nf==jGrnp+k^CG+5y@Ym0XbNJ{6W!Sj&MM4DQX`YKU&}iU3_E9(4no+$MXzyvwxHu+P&5F+pXt^>5;w&'
        b'n3T|Q)%tPh?iafr_ICp;OP_dDn$<VMqYX(y?<vRjBWDJ6^2Wene_~gYc^Z}#nR{JszD#CZr-7A6XS$NNqMIio098;l{zdSU`8kR+'
        b'j~7ZsM>%t7Kw}W^#E$n3XNhQ-H@i08$R=+wAvQ+4%PmLP2bJh9bH2a6?T%4f)5K{*DfV8a?)Zc$iPq**lt7y=2Qtv~{?sGcha*qu'
        b'@@3k5KLs%c{Tx0#aXu*@dOK9G6$m>L>hB6gz2gV|_h{gozwh6{t-D*Zox|2SMP_cDw%^3@dsgj452<=)oZr%x`k2Fld!%Q(>|rz6'
        b'F@zALnbm=f7E4zTejX;1C7)S6!@OG2usR6My8oJhuX4ofj4jG-TkCE@?MPc=g~g(*-fA|;%wZvsoo0jF95zc?2^oIou-UD9%?5u~'
        b'wKdX3En!@7UUn8l4mI5|8zd?xjQ@8zc8%h?bWn;4JROj8Ex~RGp#0pf3|S|rIE*3Cb8H;Buyag2@y2NdYk=S5g8ociWyQy>>9oE|'
        b'+#{Ve0P~mfXFo#yc})=CX?I0<29?!P#Ur8JO&1I*^})}8VbU&ie6GBf6C*;b5syC{86Cdt?j*O`vbPp&^DS~$1m?adERK!88}E)&'
        b'<+&HD^W<tKxHM0ewLQ+M%L~eg9Z}~6QlvUhq0XDJkbigz71W`U=ornS=Lpe%Vlj)h8a}F48~oK)30l!zsqyldyVW<Np}leO^{JC1'
        b'FtPj!R*Z+NTp~Tt_KYHDI-L+&ND`t&Se#~P-qv_?T;_-?I=*30#Mds+j6=m>-%%H(xN-hR`{2Y9vGsXm^bZu@h`t~F?!H4gcg|P4'
        b'g12^_ueQzHdgI1@RjKc~!!`4;%Xbc~A7Mf+{bl-{v(+yDt(|A9ZT?$9D<95-6<K!Zoe^f%rN7AUxT;;#w|4ec+oo?#=6wYY=gk^c'
        b'%F)NO(Z?TFyChpXyQ*!Ht*~+p=go$WU%olI{hQg-?>MVn<krs4Y8$yV`6gF16t{7a!vD^(>hFDBTy^Jr)i$mgJ$3*E!X52hc?zB%'
        b'w<gev91jvhBiwSb|2_03{`fKE9@@*ZKt0c1PTwrKE(Nx5x*~uK4dVxz#ny!VNVM%k`>Uz;+*o-UZcRE_81~}Oe^t9)uO4xwp1(lz'
        b'^*sxrKIq1&yE`FKJFY)RHf~_)D*N#(wRJK48pb{OuF9?v*)xfmb~dw`nr(^&O$-<@l_Gf<FqEDeE)I{k*YoF4g<%h!$2q{|@e}>k'
        b'2^dZUTeSn!g^ArRZ>#@>?)I!}<B$5W=WpV?@;gs!2>0yZ?1lxjj)o}^oaZWWTMu2Ao^$c;VRrz#A2^43J6A1D*(X|O=MS2PtyZ_S'
        b'@%)gf*JT3bB*Q_g%&4yP8Ef<Yl$n<yuU+J@DjOZkrA@Ym;}Zw{h?*ssT^Y`%qWRFE3OV{Akz9r;!h9Rg*tS*okk%$y?qRvLiM9n)'
        b'!{4Se4a!+f7aNqb8w#c)01bp_0oEYTu=!T!HlcbwWD}0k(I`Ev47aw@6xFJ1_x)7<X-tFRH%`Msw;_7i@E`1a)a1<{DjJl(xlu0L'
        b'Q%+mU=}OH8wt86kAJI*8NfYf>MqkNnGOXQDO*xed2g>%|Gv;oQqdQkD^%^A}#8HQYm3s^R$dxyvH?|SBNC!ySk2nl0nP8&-Lk>_$'
        b'nMw5ba{V8m-#z5PSUlteHLd?5NAGu(965<D|Hfm(@(leE?9x6lqg;@D3<jexGJUVG8r>uO+$g(A??Fej(3Znz{J^=NQNti13JS*c'
        b'j~+Ue^1TNtflm(l5TYAM-4PaCd!jG?slgRt*Zjtwsc3R2-v3_o9;etrYE@L}Q7m!)$?|CnHq5IAjx0%%X$vS#kI`-2(|WPhlNd|e'
        b'4JvB3cdWstbQm~&&fPd$yu)~FQ3KKc1&0<jhN$_RGd>24E`qGn-~N(kd_YR|`Z!AelUKzM#zh>8-vjG#@@5XC{U-k2BCm7MNPrUY'
        b'EG!BKx-sjy{nrKjfdDc7RG0A9>p^@8%Cy=b@%#?WlmDN7vSR#6!tm#$mYLmq9ZxLG2NfmvI_=tFv|gvb7xGnpdV<cjN9HyA*pK%m'
        b'<4BFLTK7-BvuR*vdmre4Li@cavA1lUc1^rM^@pi<ICe$~g$310MKC_}$mn`x?0jUjl^MN;N$%J5FN(0|kH5Mn+hT|HtV(%JIy7c<'
        b'jTt+~jJ84}n~y&7E)4~%xv6;Y-ZoU_uma#iUm0Cr8#})?+J0+fSE1@i379@~%jmjg?EK2;4NfxSq5M}T2&zh+Zv6gK?t~&?qUJF-'
        b'g@b1U!r|{m*B8dlFO0UOMplb}{`&l3<HTfN`TBoA_4|yj0b}QY(FXd#^Z&Pg(Zu8(M=#!vH+Z~1FuGjEPM6WP(8xxjPa6AXeCso`'
        b'$>{1acK!w7y{_%R4oTJp%ZVA4M22N!?fc7ks;!vN2aEH(2b62k0p<5dxdLv;9@p;@7Trp_u=a4;2}5>eYF{p|g8=b>J2K7y(V@E('
        b'LASls?}MdueLZX?+*XW7(((Glfo_}<nL~Y3x(2-_H(!vak$F~6e33KpzsL9Yd>?iiUHgrl`;E3ITiAz4nT)tFHJ;vjp5O8HwisRY'
        b'#?E@9?d}%#hbn%IB2LVx5X4=GW;UYt9;{cMhO44EeH0OAAGRI>`FM5coC`_fcw7}d4s)t`x>o**`Y^X>zps~Z4it0i9wk5FkX$4x'
        b'P#`}h1oQ{{@oOou*I+H<gMmuac|mGdQ4d+bjq7usETDFSDv`==Du?=cu3R1dd;LXGW;{%53-lWVGT(2Vfypz37K8ylKj-0d_5DJ#'
        b'{1wBw3NTGTvjf7WxwOjgy*IX`4QV`Ez*>Pyi56Nj&qxV#m+nIsoA_0v$(G$&cQgKu)*w?G<OOrNn)4inG=NlKzFFgn+dm}_0EeP='
        b'%dzhX$PbV%Q)?HJEqq0tAxv#hIYKxKUT4<_j~O2$qiW9+Me~FHkGyx!`1zBpJR}`@*64cH*!ir{c3=y;4-s2yAi&zPUZr=tklj=e'
        b'0+LZ^-Ep!oB4<iGs4eC?+|p1dm$_)K*;n8<{-iiH)cz`wb|N*l^>A7r6^2X+JD3u7kr)Pf=;#&@9<K5&=daQrc)g#g-hc8%Gk*rR'
        b'?%d>gg$8rmB$Q9PfK5Xr&pLd~K{1`aMkWc{eS{UDVT(9S1&1(^htYR=eRN@<lwzQ`^Wc`62OL;EI{)db8WnbOuA+N9x1V<QNq~5g'
        b'asAaNfS=o+xGva@&T2ZJ%-?0axXN-$=TC&J)V)d=J*$HM+W!s5>zW1Yrg+%)?=94{lqP)kSo3zX1f$>A&=Juz{Vckq5*0z1c4+9+'
        b'(J0ic=~><psYTKerZF+mAx-^vct037wnRvNiJNWgt~WcGIrV+e#;ct73G(*YV~Q6*qi|$$`tAvP-W*;Ip>Kz_bPjE?M__C}qK577'
        b'TbxmIJlg*iGbrZV7H#O9cG9vVwJgzMrUZ3_HV=2)<J6&ZEF06*rZ#gcgI?#Nx;;=A-MVA7<-E55^f>xO^fTteEo}uA{vm~HP6aHU'
        b'AJW!wa$|RQ3;CfxJF|*^i(Ek}KB3wPHWt+mX=D2~^8k7XMYELsZ<OgIFvGiBoSzMKByWfDZ5OkRC>yPJst43^>A=-?A$u8R#gWnI'
        b'<(BQ8Ej<Eu8Oo`aeixNWE_jSkBdYj2pVp*aDk!mb->&r1BmhE5k?-bG0j8M2b?(^$46>x$8w;T{6a#~d^+n0TU<$Za%x*ympg%H>'
        b'*a{vE6#5y1)JBx5`6q`}`irhlo{>c#rajv!I|>-#_@3*L+BR*WUb&9Dt!0jVlkwaM5T^g)G=JREBOL^rMODYK?NzT4y)@P;ft5K*'
        b'V39ZA7&WJkTrV|$I$`?5_8T>_UW?rPk{~>i0u$Z3KI0@9HYy88y|NpUWspQ0n6+GZI!Ou8bw%S{bOXp6kHf?D;IE;}tjc{=s1f43'
        b'+h*&(O-Zr_Twr{dXo=oqkwquTZ0TD-kc?RIWkcQ;%o;&~h2y_K{u&4>kP^^K_a#2{qkvv~VVO&|XcD*VW(Ea41Sk_{xeb+kE8?$%'
        b'N%W@Lkg%n5(Ux`*`xP2y#cffi8l`Ta)V1J2<l!Bup=bDp#P0^5V+4|VGrun%QqKGL!Oa4!!HO~YiGUn)b^>`)5Yzv?z4QX!8!2Z}'
        b'1mO|Whi!tZh%ksn9Gf|Sp&%YEB$L17U^(<Q;rYu{6GZYqIX)Z@x{qmHY`5a94K+opL76^uZg;m$vSpA2>yl03yCSJaz9bfxPref8'
        b'$C(=N`YTm$=3ml#{>H^Ts_Kzab9m~tlLdd^%s}2p;!z(c9RN;%yhYqoA4Il)SD}c%eY8XSRKKv@u5!95)n1NaaI+P+GQE_PZrT3J'
        b'HzR!cpPo)yly@EF0h|K%7dV$u9<05Pt*ZW|O@Ntr!E8HUMZ0P9(p={mN>wqXKcRwiRfEK5Ckr-s^K6)z$UT(B{(X}<VnzMscI1?|'
        b'zPKIttfcIDGi`rGZFt@QS;PLgdCDh(3$t7IFa}@tZ=2AIfhbzBORPJ$T30-aTB<9at+TGD1iJJJ-MJ#lSDT)zE1s*hmQjJ)^mV#o'
        b'`m^-m;+ezgMZ>G-l%89s`?#XCn4#vC7KdiL*87%POLZjn-N}|ARTmdytr~S*7a_kJ$QyhvXSi0021=x;f`x`1LinH)5GtrVFuK87'
        b'e()`&*+G~JY4+{^(-~D7>P$$iXq0QP8V<g7pCva#z5Yj>*VDYGinHh8HQ(`in#NMqL#9FtHw0K_O_iE?MJvRj;{_@H^F0?IFOeQg'
        b'Ff*@E0#lv9yc9E;1Y;3$<3*<xxo}rqdc0mbkkd{&{_%MBSZ765i-?`OnSZu4p7Fk{MM0mYJC@OotB*zZ_<5@)fU5@lZL6z52X}nL'
        b'q3wxuks24I<iCzY?N^AvF~6&NO<LrC^n)1|(y+QJq-{;3iY?j1OIZtftSH;Rg#<tY{z_d{55cBvp4?i*FyxbqJ&D%9n)@8Kn2GdX'
        b'OB(Mh)2jOKa<h_<?+xg$q5-!pg<+O>25EK&qOiRPd5x%iI^H&Z>+jE8%nMbB!9B(NUB~YdSPi1{p)Q`zhtk_|hni~LOT9Ae3IlP4'
        b'Jd(iD<Bi+Buu8ppj^cy}dEz=kd%m8i&p{U@3$9Ffa~vMfJB2Y(n_LU3hC^S8iKse%MKJslcK$pPID)b3a>sj*V^o{0CP7Jr+#G7w'
        b'wsVOV<W9nzZ$6X|6H*mH4!D&mo3zZ_G%{vZl{#-OAFD8=$~J#98-e;F^6KI2j4D``>n*IJikiv$YnhB8>5s&K#gCVQwQ7ksFdmdK'
        b'!vfKyzi*}VX`M!bIn2=!rrHk)<}9~ovND2?qdJW!@^(|ulrOR;m9uv7xy_CCG@oC}`ClPTd-m*~!i2BCcdU~4jblLwwoI!Hp1vzG'
        b'#9}h-X9)Ch-OMSt-&E4pGE`CW)ZGl9f3xx(UYtwn<DUXXvVjyjNdYh|XdWFM0@G=ll6rz3@b4Y=UaaIj;#lJ2anwe3J8`fmpa*Bq'
        b'BLm%n7Y2zzTK}zb%Fnp!-(1XRmF^>0@40;0(4;k@BnHk!;PvK(qy_hhi^m6`WzAnIfjtpq0q<|>+Ag-Ma*6~kL45BIHczAc)v41$'
        b'7||Uhz*{73E$Vb19(NSD5y`vvD(Q~00>OhxSw=|<YO%@Rs#ILjO%|l#`W$k(G|whpbYvkVO?<W2aS&V8O&)>?G$>4W!Y6Zx*QC^Z'
        b'_(2mnNi{!m)O^oeVomekCVAj@o4k6@flAGRO3INI3T&lI3#I&Ori0MKJPp{<lfg_VMn~nhg!T}y+*-(%P}<TP6=lxHBB8p%`9!&;'
        b'%+9bkq=23N>f=_De_7xi7gJ?)^nG&#HqbJ8OmLqA8Si<>>90<p3+PY>Xr%~60?t#0CjZ9D1}ikOT)JylZG7~g)E-J8uS~C%c`qP^'
        b'?%I*wl+M(VO`$#vLtx<zf(ZXwCjt5#->9|Yemg?b>-U<?t+W{`p?xMDQ&eE8pE<?~iYgW2_!n36#H;Hwum~G4WmYAMtjx?-uBucs'
        b'fDz^x#aoE_9Ew!MVDW@fSLyi<jZ_?w`Nwi=EY15;f<LK*@t!p{Ix$wJSynlf87H9L$cUApq=5fMlUzCVO^mkE=s~<n&PqsRP@PCJ'
        b'=EX`4zKPGwn9Sl6Q{|5RB=yFubQS#bnU$cjpnvI(T2dKS*<eSkmYQdaEXznjwbSzWwC;bn|CP?HDch4oPo*t+n$XG&3rg3av^gx5'
        b'T5RRh=GCd*44Z#B<zuzTp5|G!ni-W;FvuZ|0(G@ci@@m+c<m%?EqfFV)N-jJO6;0md0qNFj_$5mb5*B=`bWrhmW6a$S5LMK5|Lem'
        b'#5JOkHWRCC!6&Jvtq*pb6xNp^eRl%YusyC&TXD~ylrUVHkqT?*b}(raRhaTd1y5Br7PXuCeFgh6k`Hl0lb77W<Wb%ym<{XvzGBt@'
        b'Qf|&|MB&F?rhF*I?wZB^gp!eal~*bt)kCP}VoRjgaymyUY_}>LE?jjAUoQQwxrOk^urvb2HouE22N5!AEv7tM5p%Xeokysx-^KeW'
        b'FI6BOgpU+C<8}sf_+sijY%0FaYlOln`5=}^R${4s#=B3B#6MT)|I(mf@q2dbV)h*B<l@iTeFg>WC+Ig6{A2Mh_T$Olr{TAYx9)`X'
        b'TCculKND1di-C;`L%&C0phnkZ?a$!%$zMTnK813QJ<hL>KX4dhBT$GmuRo&)v7yHZgx9qlsnTmnmW09xS$sMb5)~W${yzJ;AjcCC'
        b'T4Ujx{>fMqY8#=*6U7{=Fg`|+-}WOiYMLt=1(rx3OI@UeC=7a;lGM!vAzF{hT6C<n%<G`(ztMl=V<@RbB@qG(qkl-&2{iQ;En$v)'
        b'5Sy%Nqqpk*GTs9ka%t0&*SQ@Hwnf@uk#+9g*x_X&DKs*z-@}0xE1L54{tf|%K8RE(H&<BTCt2TBIMXL0sNNaDMDqH3ganp2iijkW'
        b'pK#CPIE>BR$Oyj=7^2?+6h{9KV}?TL8YuOzBUCozSG0?md6+^S#Ac(61wK?T`{^XJcZc#dU*-E5xchz2Ph3P8C8=%jj}Tj!5KA3n'
        b'R^iB(a1jQ!C-O)Uz@}{E?@<K+dWzAx5rI@tq##0=_i<2UKwTJL#q&2&moOp_>geas@L}k#?d>AR-$aZG*AHXV3$qeDn@RYWUa*<8'
        b'EKMU7jZ{%!xB|KRoweKBh7IA@x?-UeU?_@b_DE*cvr^P<Dq-<U!!^+rbunNvnguwD%22A2lxhM>HFSl#PE)zJR6tsoN?V0CLRV*~'
        b'beRQ2sX!2UhY<+tHZTTRo@PPiP@X0(Pm{C|rv!Nn7B14*W><91t{4=tp@_@Gw~78&F*hM;7nL%&8xWd<vfY5p0*dk-^z9MnzDu*g'
        b'C=<vx6a5cK`iv=D-O;5|yg{{)1p}Pow$Dvz#gMeZZIg6LD_9w-#Xc-WeDN8KLD7`J5%6Ph7Zq5<*Ulm$rit0_QCj(+Jc0qE@i|y$'
        b'RLKI-9u8`LgGxXGJw^mk43F?p;cPex21QUo{cmyMA%y4%$GADO6{EZM0jd<E`l~4N*~lbx4*~Q|<Uj5o$b#B%v;0Pld{?<e?3KqA'
        b'l0D^!J1ZrkPr0t=240|u<ZrkZQuQgPh~jQuDIfZx+->s_ea6R}vf(W&*ee^o=v?BNNE{cX?|Z<0juP==-mXLQ6`k?k{H%QF6Zl%#'
        b'*<WtA5&T&#@Vuv=kEIvv<M{-B;B-_pO_%-3_p8<|YZo{o>BaYso}irs2|B?&>`)FUr4cB3^u%;mclpb{=iHQ3h2iL`ywveCCgS6M'
        b'(a~ixIqmovrp&xxnbKKK$C{NL<q5C?3-~6GzS3R}4O$tqt*xAK%jh<fV>bOOn=aFV$}@CkgT35-MwZxn9|gF1*W}rOOsbrBJwJMN'
        b'=a{!qy=cZ9(^zhI%dCe@o}CyCfA4wAp%8HKjBx|$UO5=^r*c%gzFg~G5S?T~dj<+x5j+v~s#8cnXFSMzAzM@aGPR3IP$M<mQ4OjJ'
        b'6xQFqE*%6ysP15j;KwKySix;9`L>synU&>qZdr!jtlV6#JF|dZX#$jcNMzP;fzQDre}-QC<I$4>n3NAVuRdj4H${WBK!XK{27bS$'
        b'fil0`l@F_`@g9h_Y{Y+RtuV$=-f1XT>qyWDbpqS(%c<>ZEk#X7`^HBw)q0GY)A`$S+i%OSPe<u>SZ8)Q@O=(%xs#o%%3JO64UnNP'
        b'=RK3j)Oqr!G2v6nDT!@ac^zTa3JNx0%JgzjT1&heq-9=zchE_O6ecF#4`&2CK^an1$lPa0@q^MIG8dIILPD>bU`S#?8nYA%v8Y(8'
        b'f%jo*Cb3-%id-FQGL!hh#)NtA|4U2ag-PLBQdqd3){@w;mADgAelw>0{2-lp!qhG*=!aGN=YKKj=)-nl!5195W`bdbSs(MSQwzGG'
        b'{3k6*XqV#fJzp(7w&q*!n3x3^@>Olkr7beBlB3HgqVR0^Uf*)FKsYQAm@IPlH0->Eu013NndY`CKWQYA=VG;s1>t93oISQ+!6!kR'
        b'7sMZIyr&?=tgM{!8;~rNsQV@;DHRmGYabmUTOv8?H&^XLntcdUtlV^hW<`jsqA?B|=yPG^R5cn9Kg28S#O9{}Kvy<{Nz8*V#nDIo'
        b'{?Ym4X2&WV#o5*0deRTvy3tXHd1K5KhW4lhB*;_LLM-h(&PAV&w%yvSP7{EUqWUeyj&4>o{v7QRM0X(fC8~5B5edZ|xv-foDPsgA'
        b'bbXQEG)6!y@|(x+M-6Z8yuLZ3_kOzwCWk5$Q(oPC%?y9^4T5$7nlFFl_}Xcp+Jh|)^kS^syr63tJ4}gTbRBNN=LP+p?cQt`2zNC!'
        b'Ov4T~Q^40>%^gU03WNpA@erow0SL{4TXXeS9~C6w{oiuRk2lxnQBu~8j7^Xx{oE3%{`SwdP9Tft`rP%THE(;awM^0dFe4N>{!}mz'
        b'Gcs1_&-~;R5ba{ed&n94qX&?<F3dQCuAex%u$lqhCh)p`aa^2h_9JS$CtnbtP<7V($&aV}BNFvaw1%ATq1mIGrfhcumgv+B%_x1x'
        b'=S|WFEUo*OnwT4><%zuk-6sw$rbtlW)CP=A+km!Nab9)g@9jx&y96^0$gKmkT|!`O^4@dsgIs1Ywc)*OG{0Xc`WK4JQPOe0qo&tn'
        b'x_{~eNrRtoj|Kg106ahR<DZ2L%!SIOeiA?(s!|GSnrZF6+}yH*3KZ3?HkPP)0gL888iYP(WaWb>Q~MEaKhnCrH~P8WgoH+-x6KUY'
        b'y%px(SXWz<T`4Omxeta^c<}sHasIt$%sta!p$OVAxgiAfK>m~<%O7P8l3hgAk>sDaRdLT`3_#spU<*OP51i;eH+=lb`AagGj3{)P'
        b'ph<Hjv!o=z@g3Kwxtyt(A*7Zee|H`Cqfh5|#P+Vm-xNWs>&2UEe0R0Cwc4fFE|>jfEW{E)P@*+&%e$QsIPcL`k^j>mi9CH5Hx$<b'
        b'_v~UDQn8T2<Of_AA$rJB!sLrQ|0dcsu8s{o(l-g8)6mQ(ZwKFKLu1osufN6{JUw_M&W@Duqlrvra?j;505zP7?>WC|PvfTHRH7jj'
        b'Mg;{Y^zuL{OdmG<SL1JIL<JMbQXBCT!{57pk{dVfkB!|&x2AOljCYdjxP>Y>{Un3ZCDIOLGJ5_84VzsjX~|nis;=_#oW<4?E&7Fm'
        b'f}c@stpb57RY*WorfIYy35-dDg3zxPTQnu9y^vepB`H-1OOnv<#5DAm4$JS-P!xJkJj_95w}P~O*c+9;CkauxcZ<0<$pvHGC<0he'
        b'y{#!caOJ!g5_;X{9&%4B&HlNBzqc-+-89U`BRq<Faf@Dc9uPdJwrdsS9;P>uF;{A$Vi!&meZ>JIknPjhy(PTDUv;8I)X%#gpZCHu'
        b'JXFLB(+a-fVE+EX3$5t-Lgp0%;sp=an0eWt5DTfLB`bR~GVY_@2{LhIenwJnD-K9f(jM{V-M(!%+XhFbW9L2{0fuNhE25?~A6wNV'
        b'RouUiCNH|rRrO(ar_%=uX>z7xzyuheGIeK=JzN5ifW-kmObtq$68Hbv8KGx{Ysqtra9SNPmL!K7K06S}b>bFXVq&gYC*o6*ctWQm'
        b'^RyDJPFV0)_=1|D`YVV06Y;Qzt(aH0K$7#zU-pS1(|gvgScg%*su6Bbx{#VIgSJ)w07#yz9EEmi%sMgu7fs?8-IzrVsQNUTOt}p@'
        b'ky$5Hb)i=M9H*vYc(&+3AbY+**nhzRFtt|VImy>4I5}0vNn&m*hMf*ITTLDHhfQ5{?=`xeC|LXJeXI?eD4{k;tPT=2NU+4%UYLF_'
        b'3ld+-FJCLySxxmPx*}|AHi3ya6OFHH^(N3vqt9+n{G3K-Cxm15uVKBu$!(QDe@!hk>x=4B(?AM0MKvYxC*Kc#bzflbtDC6$_GvvN'
        b'OY#*ZX;J1Jv6&RVBejzvSXN=2tQH!Cl`dNZK<Xb3JWENBz6I*^l)ndFVBg_Hd~844i<^*v&C(^m_!VXoHbtgR{ays^^$_h6_M1QQ'
        b'h#{;d%QVrOKqZL~L@yH1^920*Ht(%D%K4k>8+wpyN;VQr_N*kzuO28t&2Jao5b|v>0<3&Q-V%m%)E_!$ZyFS`e@D>G0b**}uAL_O'
        b'z9o!VA<nVXg_#4$CDUk2FXd-aZ(scAO>$K?3f*U+O?25u+N>n~k67aSG*U;tLgx?Ytv9-1Zp9%BTGLA>dZg_ll?iuRL8ozS!$n`h'
        b';^?`>_21*=(wl@5-*jjM{xAeKuS+%-A>YNEH_Me1Wf8<KX7(73768y*<~80`J}47St!cKO$`%`eZo>#~+mB_lDCD)5?}hDd*{lU9'
        b'^%+VzzU3$q?ZE%cnWNBgKQg|*E(?hT4GHN6T_fH*6|n`QTwE-W$;a!jf6~_ry6<=`;JUyKvhy-BF(^N481iil3o6cDK^9dizEE1f'
        b'8kYArc?&#%lF~=^S?RL=DgVUEfiiwSnIUjWf=rFNeG8}dU6p6b_!5j}p4uO_Ug(?Cim`8_4s`aGp%bcB1YG%-vQ}asfmc42J!L~5'
        b'mAM(*>4)3>uo0+#ny=FZbrfym%J<4*j+NCr+sVmqTOl9p9(2e)%2}i#3>t9~SqbyHz6Gu1d7P4Zj5y`j{|z@4FB+Xu^_GRlF%MFG'
        b'!z1Q^ncO0A{J<p(u<+F16=wawzJ<_-87TfXe)bsKFqK++$NR&0+uDS-sbFRDX4sF9Kh0^d@|mglWZmwkB_a>EcN>CbpN5Hx9o`?4'
        b'n{H_sAF>3U!5yP~=G)jzM5V+;u;9?i0?ueKwFXz+=lJoPtdsgn9V%$DmRW<x%V8pV>q*R+cn?VxQT5AgP|;h?PWvN&;M<O?{ykZ5'
        b'9S`qWln?S4*<aCR85w0%1*kNWP}Leino_3`dj93L!^|YvLz+whP&qt8{U9!%k`@N#u*qe^M?jq-%!fJmz(ntx+Xp3PQaFru;ln_X'
        b'Am#j6STe<%4?_D?Hc-J9S7w(Ig;6rM9kj_$8lM4q5{CEV81^znNozmiecZDDQD*1Czbrw}cX^@z8Vn^BeZ%V-^qw;4G3o@7!iXrp'
        b'WP)!K56==##w{cf`l}kpVEqFz*<ipNcezGf@o3yk5~ib?!eGjrf_N!}*%h1o17}Xg`X6&s_Y|V%X`&NX$M}@NN|hcP6^r<tRH^%D'
        b'u!r@fXr~j5phT@epCrf>m4T9CS7GdvQtxIb7+g^8JEynSys!Mdd0ML=kwNUhyd<RjDBl(#@0)zAl$W9l1vQU2KBBBwPTtuFP+O1{'
        b'#D0xxM4MKFoMFG-7`;dnWl69A9JNG65$3b>ybB=+szeC$vHmV!AT)lshu>>erwXAZ0pHTa(qH6tbVpf7?rJc%#=_->p^Y82nyA8E'
        b'g@{*00CZ50asGZ@KRxeqJf9^*!5Mi@P8ND*gY5WD>diNPyT`kQoGhHo`0!~4&qs)suvlBmRP%Avg+@7h5_MsZ#T0EZO?D!355JwO'
        b'PE}22%zT<LC10Mxal}o*IsAX&7_UtAc@hp_H<jUq!(yInOi{c_d1#~YNeh9FgZ{wBKhQHcUZ^GdwfF<w+;C>e2Wp}}6EF0;XveXF'
        b'Bb?H*F;1@5PHsVl=RNlzkLX{57nTw=v+zRm@d&xX{>ZK*P;k{z4ug+WHcq*7qeA;Ly8}t!e%=gLmT#m25IzKE{3g-cMJ>i>sEi+!'
        b'cyZMt<aLA!jLzJZC`ZTVXo>I=e#c*{4d=fI*IILPCqD^S<CvqCYrqAGO|q1kiwduV*w$=3cDta4TjrvCK%C}p<l_~L)rbI(RM5VX'
        b'5;MvQ1Bseb7?u=z=>0+!(SHUZPWd=wIQ)mTPbI_q-{(!*PiZYK(OI8KdG1;wW3m&Z<4*v%N2)mYq@64{$n}qM`k7C(xG;Rhst2p*'
        b'76uT>`!K~<s={ZFY2{>Lz`I%kqjsX$R$8oo5f;8<1@+ddfZW2>Z`$RgH9}*xmKCar<gM5TK;!jTp&yaF84G7ntSirpn7%or|1xKH'
        b'2~<^_6BnVEkR<LUBNg_PjG|qfcfDdjC!gJ4jW%U?y5V`a2*q&?5GlSE+WR?Ztid2INWdDDVnz3uR*Hv*5jDM>PAXpaFk`8pw@eP`'
        b'X6OZ`Bw0xkU3&b>j+N*}s~3Hplq{7JCdgSyznz|wv+CJd8sCleNi4O|JNxsr__9vG(NVx97oa;kIMqe@)*cj<3b5;fswBt=Pa$fK'
        b'aEYGYH>cewx!*3SGc;{LanzuH52N^przCPVZfM+qBF8BnNvPVRi-`V%9N0QX|3cKf#erSzwsIY%rV%mu$s9tomoul3PX=$^C`H;p'
        b'DTNoV@*Adz^Chdt%H_Aq&tKA9y<}dFl~Pz0GR>+6j=peZ!%%5kQmGiL1<-?BvWav15~pSnqOI^l;1mea?=A3~q(VZ<KRIm=ISp-e'
        b'bd-UZw7E+|EMPE#mQ$NR^#6_PFX6)TmQnXp{0Pw>IOVxg1@jN~ERr``DZxldt%hPWzQb}6lK7a40X^Q&dX8S!*-m;^a-wVwbIJuC'
        b'C8p@UG%UqXEHY(xsbb^{whO^P@o9mN!UKqYJqKfB+?0_dOJ2u;3PP#qr2?AKWH2&1jAk-L)WXkPJpBtYxMU#;R)|ZeA5%^eqEs%O'
        b'0oL{8bBdgy9_cbyJL!0X(+B^R!38jv5*e9(`0v2Oh5L!*KX8<DUH~C_ffLoE$JDq)Yn9|?tX}m#A$p!0TPe@bnQ~J!iAzm(fq&Bm'
        b'$Ln0<hS#L^O^WW%(7fo6hk=LLFhioKCBqjHqDT(#*B?RewcE+U8P9o~oMPuGw@ZLDds3CpQBub;FaL&%^9a$U2_Pd%3RK#UX<8|$'
        b'ISXib+PE5C0;zF<a&>8R?&>kUJUT^_!=y7_p<(={<X18SWt@7Np>@*(4=yX+xDcjy52;Gwl6xjFJK^uqaf&EWMEWmfNRE9lfhluf'
        b'9NU#?rFH_d9u}~AG#H|e3FXRCh5bGDRg_FVHi6VL$19vVN~m}hiI5v;Q3b_8Ex_iT7!e(rpa{+Lr8SSIY$atf0;uoC3VsJe!TVX#'
        b'PMv+TFP1X=B8BQLDdqE&i@pD8Q`vVFF^fx;38ir)6%1>)nna(fwRlLI^4Zd{Ho5vR7TreMbr=dE{Gj5YGP)F9OEkwx80%bgkoD4f'
        b'bjinB#zvIVZTS=ddc=Io(GUL;wXXq1&2GrTU>QdG?3~hB3((Q@2kX$an-eIFLNGW{GG<mO@<%bXmO7fb<cZ0<bQ(n|V<Y1P-^D6D'
        b'>s(jYb^4du{7WP8aY6J2ntGi*ypBH-L&4v+N26P5Xit0^`lf}fZw6JDorb6yNj{C&;<$j-OIs2q=>zFupjAr(duBav%hjp9wg7Qm'
        b'Kv6wH_R$9Zz{G6B4;7ykq8l#kPShr>b^`YP2L2nQ$)h_5=#0j<onZft47u=N`Ox<pT;Ff7eZRqJedM)Ep57fpCIHyi(MaoZJm3^<'
        b'xH(FED3zMlkV#UJO-O&#YWO?xzwFh(H|^-?eu=cc+Y+Tcf_-OUFKysY{tC8v{YE-N1z>uCy}D&$P}=oUODNd)?BBh092FD#tK)I6'
        b'Dq_c5@m4txo5YguaKGT=`JPh*116ICE-JnWRO4R|_%+T2|Kb$IP)&450>-GEn#tq)tGbA;s&6?Mg+n>v{(<#<;h_q~Mij<M(sm_d'
        b'SXvIELs~JqrJGj8U!U>bQ}lR{YqVXM-9~!NZF>}njG(F#{x;?}d2Y#doZs#gIXqmowEk*~8Vnh|bi7^6JF;>rG1(CPp|IoQ-gZ&P'
        b'2~)u>ZlKsAjKdQwb;1@ke1w7nc;on}zC=e=wZQ?CecwEhcrKs6n7?u2P3h#A0@<!{ht5HjYkh!U@q|JO-BguLFh{U?%|gb8Hd2gt'
        b'`^PzU^9KG7Yu*uzE%P!Be7s>|O|t;h&>uPYYR!Z`ipxmqO^NNNg4tliMtrPB=zE;saw3928+z>|#YD;(1EFd|S43`0KqF`YxC@rS'
        b'Hx-CUTc1;Oi$Tg=;Lbh^Lh^S#1W5f+&K)LD7(vef2%c{sCFE03ra~zZpCTdkH3xvgN_aph{(<A~Fi?2%G#CW17TB9_ppvDE^of?R'
        b'fnd8eu{DsI&nBWCwW<`ipG@_4a^K{I4MQ(%pnRyR&ASv0pJjD4$(tKNKAxQxa{BxLQYAi})^M4>%QMZ{@=Qk?5}vKoZ2z&Lvuqvu'
        b'SxGgcf7$3y8rsB61thFZ=*y;5KD|IXm0XM}G$HVfjkXWp*t6&UWJ!ztGJkC<y~CSMM~Ncaj180JMZDdnlx;w&4TCnuw2Ux1NfvYF'
        b'jYR@p<;xSsP#dT~-Al-<iOE~HNPsl*cpW;(yTir&6Ea@rGt|SVGex19#D-i$K#X`p`16ElA5v6`NaH6Zg$UYOl22}Ecw;L4GD-QU'
        b'R|?cCrPQpB_h^TLi@6O=Pp4*4%P6TA0hK@ZMF1WXxehXaJC*5?bJWsRf<Saj!*3NSfiiSINro1)ct2|UBEf7PEmWQd>v*gTYP>M{'
        b'waDYkrF=ysNAOoh^49%0d0zzGVJR}_W<Hl2{cPb<BH4@;77!u}R;Vf(+bGZctR$iKyhU!>X>tdV_8`I>B<OAH&0T%OYQ1kdkbg9e'
        b'upY=yC_i5=-_uc6wW-4zP$9O~p*{NEa?=NCL~<Ucza0dS5*D40l_xx>^CwIF1vz@%t0Waz{ya_z{~uv*9}rcQJ^<f)=YwIm*vx<<'
        b'U)G(Az(BeUVDeEGOo*u24=523WM*K7uRtVAE!v$s6wDy*0=5NYyZ26!NU}0ih9C5sAtg1~!0mf=7cDX~i_A>Tyze>Z&Y<r8-uL}y'
        b'=HB!1oO924&N<KXoaZC=Avx+%gd|%aH%-!{O+;o57ITS^reg7L)aCTlk-_v~-t@8T42#1^fq&$nJTqGAz&G2Wjeh;%<pZ0QPeVN*'
        b'dyHSjyurQJfkBE490`IGbS?%^R{eod625*U%U7;5#>QHk{Y#-DL`>Qy<<oy=UaT9a2bnFKyEL$XAE@0{cc~*tUbn|x*Hzk9w+Vc7'
        b'-AwRji8BuOF{SfSfAE=or@&W^ZpHHU-r1?#)fLnUsb~8q4ZpN))>${hA>R6l@yR+Gv`j1GAbYWeCY#FrpmtLw9iEZ!UP$zFMAQ3x'
        b'e05#=lXXy*|ER#q#y$#nJ%l}EQk{jm1)2CNA2N}Rqt$T!j|O(1bzeyzc?7%o2)?SzJ@d2s=#v*8Ax0h%fu+%$^3SGMc#QNvaY6yM'
        b'*p3rOt`dt`H(NWFWAmydZT58Aay&YfXnKKfYx}ulIg#1HV>zqq2Ee2x6ha<7Uu4`?ZCC@lQ6OsS;Byg>3Q2qh>~y}QQdAH$+R7Ur'
        b'tRp4$Xkpl5qzOk9N%{E+NAd?6l~x<%B|Ef4Ql+vzxz4o&*6Y#&9F<Rha|1O5hc42uB8G(Oj*dv1R6e2>jb+)?MDx!12`rRQCuGV2'
        b'5)4bge13Bye2r-|#PVcE<|dw@>jwU;?CxmkvZ=*ri?LeEpm5~3YC%xs@JBjS?csH8ULC5YANcMIBXhuTSq~{k<`7_@ura0k1L&@L'
        b';1D%3M`Rtt-3O_o5FPfD%_$S3&-0|e6zq2`+dE{~ytARt`dc29*<=I;mdIwxt`QU$pkJ<f8E)MSO%I{XKG+*CZD{zyhBm*>5J9eW'
        b'Q|I%-26Ew`kQaXX{06tMQ9;4O(ExI5o3M4lO>Ia!!ZM&ous>S(p6uCG1@$_Gq-2;R8`+!WJ_s8atblU!ryQY!WBCIIl><X?{7>AC'
        b'jf~+_r(lK81B5t)6%AK?I;LIu?VoHwX+4*2%HN3rYuUanNdLzvl5~i~EW2RfopfuTvMr99d09Ert31%v(l^nkoa$2cb#d=*=<cQq'
        b'#CfYEBO+1z;SFv!c;GW-_o;FDR5#B3?}mUe_Zy9@lWOau+S{r@bKeAl$M`okObHi;feHUWqw$38sDe~MZ>=`YJ8Ms5{)=z#*)Zsj'
        b'?OR8Te!+*o;aq{K@4MXIyJ4VL+1&@L$vwRr$UEF!3eY<I7P(s&-0s}qb_WNHvFCC3UmK^osHsGp>Y_Atu=&sAx-QDIZ39S{5C&h~'
        b'aS|O=TZQHmIIj{S)ZXje*}-AX;|g}-(nOd0zLd5dueNn)+Sp402M79WwxbVz(T8;@0d3sYO|`V5k(Ijmo3fVo({;MCnO5b@4&`xs'
        b'Y8NOt0Z&S%ZbNqVrEa@3L<~s3d{IZ1e1$AGpJ1Oq10~*}WT5r)9TV0~?As$_$=Qy^*5q)=Z?+e20E^2Kv5d29m^g^HIQs0_0y@ZS'
        b'?_~`@p8-fs)>X7&Kp0)w&Sf2+!>`N#91BXr#<*+&!#;<$JUQ7LS{#K?1ePyj*|O|DDraGJ!h8AP0W48eJv9Yw2Taxmt9LsXok2K$'
        b'-v;Nd884E{+=)sSoIrtXiPU)DAZr!Wk5gnlKkzqgmUL}px}@|0hcY^d7+rwHFWHc4Z>@yqf$YU6kOHWzeaQwvVwEC8>dWn#4c4Z6'
        b'Vb%)PuG9%wu>!r@SV~Y{OsGV4S2Q>N;@v|5oZwsGBx_$1{UW5_<xNkhz!F%fgW9Q0@`rgTS}0nI55A>OiMUYbT$K+Nl$mnB)ebtb'
        b'jxP}4&;cPQG=YWdZKyCQKxl}QZtx<JOlYT9n<N+7LG^5}VP4hC(9ucWJ3dx4K6Yiht<n;-B>wwaB%Mr_3BtD&VW`_W=5`#r(bl%<'
        b'a_k*K|GuvE^$+R!d{qlcdpPE&zpnLsT?_WnL3WOljW#Pq0*%g`sU_t@GBRYKr4e9T2PcZ@R78uEyF%u4hPNfUJ2*nu-3a5;k^W6y'
        b'Jx1o^T4<_f*LwBhogDEUkriZFKnaF{*Z7lR5m4Fh?^RIo>{#t?*>`ab*B~`dz5(drD|}uUj|z;!0_mRG-D33@zmc!42+N907OjX&'
        b'AFk~uvcxIk%!_b5at_pLC3z+Zx4$;(6X|NXMXsEDr`Gch82km?JGIPKNJLX3)F8{lOASuSrcz@ECSA3jy`V@e^lA-d7d=v29AGK>'
        b'Ma_!?JN4c6=C`C#uS#Pj^JmO2N|(y>x_@JyhmuRdrYWF5fN|E&@-j;an<$VbNUL25O$v_w0@fvAjora?!!ik?ITU3`I)FD^^xcmF'
        b'j^%|~ugX23J5P7i9-Y(ru)zCqOCCRkvrYv|yHf{`;Y=$mm=|`#j>l<H%xJ*BHr2M;0Q<U<X{r@?QW4@sva>hAtEh4Do+FI47H#8p'
        b'*$Ec6+M>pKcRH8`Uz>gvl8G)Izzr*t4rM>gW|#w?ggM+)+kQ_KG5~m3-X_o;GN!J!<24K=Hhkwx)SRwq&#8s&5aeCn&6q&1?dDqY'
        b'kv6-cy{y)ksP$(|wN_feXsWC<#TZ~ltUrRtdf}l`-0=$UyFWU!>Ae`$ryvt3VW;v(=*{KSf)mrpS-ljzto@N%RNA$=cG6M_<KnHV'
        b'9k^LzNXBK=3P<36*vyc8Lf8=HsMh1pxV@YQ+7~_PwJ`SeHs9tbY?djtr{;JW6qzfzmRnLg3qa<rE@Kwga*Jzyt=Q$RrIloZPq&u4'
        b'r`C0-!l!hLl9;<|2lxIPf$)JA8v9d)@12XRbw$?Bs_N3UK5#+<ch$nwJ8w(%=f0>IzT;LJ$Dcb^;k_KI1PEBk1R>P9i~QZGIm361'
        b'uzoOY4otg1oFd3O$OgbD!Zd$W?hbPP1&}rz2$RIMH}5sbM^4RwrO9xZa|6jpekUY(0bE6C58PVpQjHfTcoD!dKft8+sT%J48q{4u'
        b'Q{Lg<e!7O+P;q<GKWaEr_3cRy)^NxEqhe|e*XK(T#=&>DQ9mLcVXqIe$dGdt47E(oPaz^&hXK>v^8sH&ERv5Ej;)DkOt2))pXrc>'
        b'Lqoe%sx5hku5HuK6=`TUY(3f&gY6dY`2yC9ipBI&aRPfTDOjp`w`LS<tl;aR51@C!eugJVB@yDJxB6iu4ZuoEzvUOnVSHs6`*1<h'
        b'vxMoWqJf|+fUL1v+|(M~*gW;L*tr0Zwzy%G8piv2qel3=La~neS!aKevg>qqU4TZHoDTl05;{asE^Kwc`*-IK7IZC{d!^>2S-lGb'
        b'wV`_kzo@&ggat{YysFexmNe^^p@yiBPSO%9G*8p9=`_1DE;=@TOFBs;j7G%bv{aIX$1DidN@Lz3q!dO+C)v}jwEOA$dP@>XWJbW='
        b'jj%9;g<sSV6w6$bWNBJAk*&yweF&Bnltu;T)r+~)70Xl8wIXI~jqB-}7TdPX%?D-7mKs3%H>dj5(K?E{^c~UjH-2}{R^`dVo$*`!'
        b'wLz=8;x=pXuJ~{|7T=aAJqaDASJZ&X(BL$SwOKEbp<sjEPH1ziHa8%&)3l{KpYK(|XtsU)1-ZIKOa@+j4U1W-=$|vahwoHU8Sc2Q'
        b'E+sgbzj(J-ax?&t<$b!{lAXO1><cFgCq~>eW2ODF&o`bkUS-TAc7^%I_}Ru)r$)c$8!l#^7S1*@m?U+F8{O_r#YEmoDRsCpuR&^8'
        b'wO=f!IifkGU`TR7e2VNBO@9uDqg#wT4vG6k=5yfvdN*=3Deswr4vCK2MB({!cOG>{CP5R9sZ-*G<bgL^`g&gFPj>4glk|rveQ8oc'
        b'WKz=GgeI;A>XC8;IAa&dGX*;zC%cLHeYw|w@&Fc9;YUIv(h9#;`D}b+;V>AxIC*D{=gyjl^W2>^%-ir(HG^W^li@X<(3*uXvaXNz'
        b'dXvgi;ghNwkGf`%jp0-^%x+kGXAppF@oVjyyraf*N6o^6@T7o;`Cp;G4d(Z71qnL2Ml6>j)Q81A?Yz^7_594URa7pAtNTQx-`IP@'
        b'P`URiUo2{pgThqyC7TB8VDapi8r$;S*czp7O)2z1KK)1j75Uf!s1wq2nQ!<RD&?^UsO%$DzqCtfz6fTsknZ<4|B25|bo+E!@AoHV'
        b'F|kVKo5vyfq16%%SHL>4{z>AM(|x1=Ea50Ur0ONijl}L;LC1R8<E~|oj}y!)NF>-e!mlcV(F*|VL`Of5&ZaiOYDi{dF)u7G>2X&Q'
        b'the-*dW&c4IWccN>ObqnKJJQz_3nZ7mO`rvzp6ORp~uM(Edi-+JJ(A@Tuh?F;C9ugdFS!C#HmCj&0)xFNtjnnXgNFpzo6_2&Af7|'
        b'OJQ}O-R+CapO73~@wiI?+fc(c5?~9u_}3pt<{`WVl3a3MN68hapZy}Cr*s9zT(->Ghd@}rRl9zx2Czi8z}g|e`VPVRrP>F}@n5jM'
        b'ydBoJ)vj+LteNVYu&e^C&k?Mze6Sk!&%#o8VNKi)>(gr2rx4buTVT})utpKA$yr!i{|naeZLpZ)$0M%VW&H%CbD<c?&c(#4;eftO'
        b'22PAqgB->jsrE|dJqO^8edh;myTUVManFwZ2bq`9*t@D-F4(VkZt2%@p<gWO*Bicmb#T~i0|w};mu~;Yzf`;a0%5&23oAc<u>fm3'
        b'EE$p2+(9$XRXY)+PMMDmLNCsK-YZX#F@KzG^KblZg8|xn`t~-NY8M0BY`&%c^Mp3*Q2(Eqg@yQ-+xlOAJFMDjS1p9K=@wXG0ah`B'
        b'RWS=|?;rlNUyt1mYhAT#9fW19MwU+O8#*>koVQqfxil^3hiZBxqF=&fA)x0VP`j*S&mZhEoo+##78%^OB`Tr+f@H+~s6gTSEwfh6'
        b'&<@1QyKw2%uJmfaEHKMwI~||?Y4zY<6a@VqSSfz8+MZ}h_OqTBS+|QFiTz?m3)7D#_KJpyo~<IG*8;pn)viSdUShRxqX+~?l*U~R'
        b'?b#Yc!p)FSmacZu@Ef(&H}{l%)e+b1vd&q|+|w8n2kARUtWYyv4e?Q1ptCFDgDpB*VYMNAEXe$YkBNhHpCe_vsOb{V1)zeJfH>mh'
        b'7IwB^Wz(z<>C4q{9oWGp3g@8n3Pz;0QSE}o3#1ygiuP+}Fp41EO1Y$0eL8lRs$7?<;5S}_M+FSq1N(k27%;!mgs6VLUp%ig(R_^8'
        b'G**)<w1oa}gq@hmP_{)XR%Y!%Y(cOWg@VxrXMUYWHhvg5wx!?!PGE4un>vB43vRkB%vBbVOXJy#DRt1?_zl&@4b{5E3WHf;NTl+9'
        b'3K|C#$gqU@xXNoabuY$@RZW#DTPzjQlhR3ZwZ~k|S*i!QRm_j@@PbDCFZ1e^SidOh8GH-fFY-G}jNT2EO1MK+u0vJhB4z{v+d`8M'
        b'v#j|2W}+z?+u6rFQa$)ygk3gu5a8SaJCfsh1$80w&JvkXSZgXEDfjbR68c5zUt~SQ{1!cUIxCAh#t-F!)=uzSz@NHY7WEn5Ftkx$'
        b'ZEaF)?o@63V^w<&oHDzgpx)zv8nkxl#?<OMyJ912t`kUFX?WuO>hd6BbcBb4*VDmE{{hENeeD+}rn&?5tqb(6;b6DWyMZo6)2BRW'
        b'_$6NY1#jNZOOc<v>BGF>Ft6t$KJye0?Gn!macTi3st3g>@$qx3BV=&(I`CMH-iYTK#Z0vsstg8J+Y@dshy-})TLv>+3V`Jzg@@{S'
        b'fUt3ru|j)JYY2E)G;62MnX6ppDuDCVRky6`>(5<&Xi3i1DzK2jO3j6!nBuDT8&z<xFd%Ug*efJpuh99no-DI>IeQH%A?!!0T#rE5'
        b'k5&2B(_&^-720w-k)XxjuQWP>@G+I7*4n5*?B~ucWRMrKzxV8Z{32jLGk@kAzSIdjlz-DK{x7a_Ek^jC3LDbz<=G5f8rYp46J35N'
        b'0gy-0krB~}baYTa&!3>rofaPU)BHU2=(hvv_x3!;3x2?Qw)4<dT@UCyFOGBbt6cNpH$+z5+(X~2LVGBQ#${fW@BEGZuk%-AzHJYc'
        b'SGnX6mf{vztN`n38H6SF!D{&Yzs}5=vRh$I(8^Rg{$*4?QcJXskb%7>r12J7DcJXe_O_d&Rely)rrA-|ivlTff2xX3_?eVj^fSz#'
        b'U?()&s;E92<cXjhXB+H`g!u%u6tXH2(nHA{(^TaZCus>wFr<rYbb_@J@v)`^Q2tn%_iTpO2y{Zj6&><bGwV-x!lu;Ot?e7CrtC_q'
        b'!)nuFJ41Ra8h&LiAifWI$d9@r=wR-9h-lJbc^3mVR#wrR$nK|>$u;IGu>C_acc2WJLb^(;IzxKlvPyN>js{OaCrkqwijC{5kd(ol'
        b'p{zToNb?F?p)t42vShvST$w>I>4r&zaf=%cryW#~!9uygs>P{Y9mj&9#J3x9tPLWt-(_bn&c4aPC;O*=WbP-t>Q|K*v#o4aU%>d+'
        b'a)V%<E`y=&(V2EtSiiBxXGM9h24Qp4unaDKNmZIAJvJxRNruOy5_RuT<Kk0(OcI=pak=RWp1Y@tRFR402WsNutH%8*f_g>Ck(J66'
        b'%?I(j@ftiOosP!xM#%U(tDKS8*zsc<r#Ik7Hy#R$dJ^9)N{GblIl7@It%=H(SIIk*QgL$5xVY|9YT#Wfb0=(rJx(QnM$}bF2mH0^'
        b't1RUmf1_DEfyIr=D*Z`*`963RX$e|OO8ceMtBnBs=XkmVB8HgBhM&8Us5-iFi{BQ%Xw{tZ4nmp+mDWZd#Ap`E^i45~8;(+K!C(&+'
        b'WKp*A#r@(DqaTw7D<9oBsFCWvgkJtgdDLmJW5O7|Sp1nXiwcHIUFruNBL1Cc&O$7X|Ef}#Y8ySyTOzaK&s3Tsu{<e0ZNT$ZV)R~s'
        b'FVkk+S&D&ghC_Rp1K;iD(!r;*uUbhp{B|iBcwiqhRf)zHv;|{Hk*es#J7a=ENSX|aULHL8ai!<uO77#zLGB>)KaiW#MMBf9=?{1T'
        b'Dhoz)r4j&UUjtB=&qDn`fST#zF_La_^NXaJ|10bnmoq9!38|(~z>&No663x~h{{s+6|rWp5_uA3ek+BTENvJa3h9(hy`h|HR37L{'
        b'wGZ^c`-wg~x*O<}rKJTMx)f>XIP0hYM<esMO2LZ!yHc;I)GhYwfH#&<kD*52mRx=)-`EM;&629$5~sg_+7&bZhV``4ez9HENr0wO'
        b'?cN0>Fc0yqWxAVkKw68%e`C@4D8di_k2c3lU>`%&Ry~d7&Evty<<g=GRTgco#>k-Ue%XzUmoxCCet`1R={Dv4bUk5|uV(|3l1Ag}'
        b'D(fS$lg*x|E6HtS7_+q!ImAf-yz235!+z$I#2_s;d_s*&`o%pTKvTTJt7&gh<{x<&S{#0_*U?qlro6YLmm4c`iqJSq)SVJdekGE1'
        b'Gq0j?mXOQ-KgYRWlzj{7o}3e3mhByL5tHj3@wU?ci(UnNkWyx74VSk>wyzP|W^PP{-N^S-OZ;+{RH7Z#hDP0QYKL+Qp;e`JP1(SH'
        b'3brqF3)Iq#`p{4hj;x6cCFPrN)ETX;;VrMv4D_0uzP%J2@7|<jCJyyZ!c?H%NpG1OBepTRl2orvB1|ks&b!=*lYVs;3ik9xQ9X-O'
        b'<vXrRHFs1ZcLIB~D7tzN|C{uJ^pxK?Al)i)fNp9C9%fB<@(}th-)=;7iC$q>k@HBgb@`4o>!xHnuk#Kt3ZwU96?#350aUo0Nm#c~'
        b'WXR<xoRnENQ-0;pxi`1G!nM3&T+FP7M?k|b>@FRk>GF;T*iBn<we=1h5WTU=sO1=Qwn8gAIpX=Tg4_npD`sGM=1j$InGN7cm28-p'
        b'-cNjnLnAR#-ZR6)Kl8u%aVdO=dY^|OV!=ZPuUS+v^_a4d&L@n=DjEi<C`EaP$~d=T<7ZISKr5{iMilCu&{3GtQ!&UA23lc^E(K(?'
        b'L0A)#s1>~C9~DQHg9JtfrXB?A>8^@d?J^7w$f(x`%jL$UCKk_SF<}?@Zd&tp#m$kH^!$<kO>#kUN;)oX__Y9z^q~r2q$N={{<bw{'
        b'#PU?)%MU$}^I8R{?u^3JauKP5-t}W~^YRG0WC+*F>>=agTUWCUUY-K9o|srX{Sq=~x@FBqWRZ6_tD<9uAa(4TUlwf(BkeKC$%9TT'
        b'I^mAXdIh-(&<zU%F4Kf7wscXz{Fy=48lC&I>-o}sxj(q>D2q0oqerer$jAU{s1Y3V<Y%sTP0gy0Vv;qk-%6u9J^&p1zK$d0kn2Wi'
        b'vufBSDWgX&kuqv%2Ow!9LR^!e@UEC-89g#%<FKX+e1sOX-K^R{k6f_5hGm}PBffFvlr^htG0Bfabh<8-HiLua6d#iu9Z?~?HGR%M'
        b'9MC*S07^Py3+Nt58vTfOoh_wDzG?c3k2vb8s(@)9@~$f;@TE=TJQ)C8X)a7Ax54_y05mPR$}&QXj`HN)m%;yGeqqSM0FappNO{n?'
        b'e?|BY%c%X0P4Dsx^B;y8(nGw9C<o1s?&lX)2+d00;axwL+eSVo{jK|VG`;B^<5-&$dr3vbq&yiRi>?p3Y`fbwJG@zNcx7OCnMo7G'
        b'92**5W`F5r(+|wT(#&f-`6e?^nxr}%lNdzq0ArM-`h<DCG$wI^ag{b*<jH?9CR37Xg!x-(Qo<pSA3eB_dB#MK{6LDR#vRgcc`V`z'
        b'{Co`-lbjM!%CG>~3o(hxh=)jRlB(rlSxn;dV5CR?%||pc-K9xrctJOk2I1X36H!5rOlN+_FHCM$t&T|!Ul_Vj20cW7#7D?t_7l<*'
        b'{QX&^UT14;`jB7v=)*Etf1GCyT44R-{K8TQ3Zxz7nZ9y*<a01vq*mwHG5Q`KVJB_SXdI5wH!;ccBf6OV<u481O?EL@#Y?Klh^;TF'
        b'?u<?dXBL)cO0b0m%&+AysRCnC<}6HMV#;Gu2<CD*9J7U$%ugWaC+W|(!Mf;$^+WlsutL1BzP$-62*H~6!8&sbtc6d+ys4NxUG6zu'
        b'&Ydog2xnFxLVu45UWWdwyaD;F41{m-|16JtG*^P<{TT&iya<Im74m1HQsFV4eI2nie*MJs&oE<)yhe`vkN=BrxWe}8>V&%`X<TIP'
        b'5j<CqF)x?|e;Gd;Z{F<)eR;RsGg8jITORQN6OH=fKz%t_j>xiaVR<l$arOim7LW*z*@P@CuMwIro)dah40>dC3(XpYW+fmOxqr$B'
        b'-9o00AMtDt>amom_x9u;MjtP+@R^u{b0&9|d$@9LXE`HAy{Lf2a=OaV8F$Qx&dI2=5NMWssT>N!%^w0@3=!Re`zI8oniAM)5tDBc'
        b'4zK;j*?U~(QJAK&Lzo2f7R-omD%XoNCo|HYFV6~wzA%0Pgp8iW&C|U8Aq}(KB%IH^MxS4^eKw-$caW2iF2a}x5xh<1UJl}~XsqhX'
        b'xwp!obSfBWKIyE9xYwqwLMNnf)#V^Xmm(-2z{CWtuDu+}eUWpuWZZkxFTAuH%Wo~{HNly!x32s@Q{FTAlpA!6+WQ5Yjb3izmc1IB'
        b'9hYrEmm?M2GZxn~7I0!R79>%Tf<h2Sn9Y`{7nI%hP8k<e-Y{f!D0X$KxDtztHr;l~DO^AXltb~;Mx*aK?z_ax`nSou0fF_;8_=3_'
        b'VfiUh3q3?bnv1DG5<sG9n%}2yBg5g)e|{r=LHPvaIfoKZnQT}F`62XRQD5;VXz>V53=zGmiAizPC4M)PC;wft%0ytgv`x`!qUmic'
        b'_we<l(tXPaHWd<t>PH_<AV|_Lh07%Z?Hn2Oil22yWA+n`bz7;tdATc}BpsV~6Qj#;d#=M}Beah8u~ECrx@3p?Q7l2@pI4gAjKX2t'
        b'c-;ap#*c}CFYQ=43Hj87SRL!-)pW^vzb}c=ZmjFHAj$4L9Y1Da63PIB0nHX;b*`T*R<tynl{z6sxOtv^b)ALMpxx<EaFOo47#3b!'
        b'XDqkZyA6!%pO*hj$uP~r2K{*vtsFn*7X!44{fDLVbc#H0G`fSJzA+uG?>c>K@{EyWwi^W(Q+~|%sNDOOZJVYxE1!nG3WxmcQ1fzs'
        b'JbaFyJZG?0C?^go4An?E5vEqe16CHkKp|FzANIB~XTPQ4+3Y;UfS@Y`)ARkvXv3|q4W9_+SiaoM+jIB%atDc6lrmrtPgs-_YZL}E'
        b'YT2*z^wG(0JbS`(4{N8^D7SPJ79!n5*UOf=x)<s;D+eqJuLh-L+hd@FH$TG9ms(H6p%mNR|E;SNvzwLHn>A2|+btewP>$^Vw|i7k'
        b'C+JH_wCyO1dD%eKi3c|0x75)erquKuc9-$jQfuOfuFEzxB{p<9+27-+%IUqOZGTR0OLR|tt*HARAm}BiF_r-ZUgspbE^1{TQbJ>5'
        b';beeS#<ak>&@%I9a@p&42CDYX)ji+1RF;{=BmE|Tf=pK_x7K16HUNYI2rm`f5yLEY3W?nRKs-vxfm=!rE9@`A3%A1ZAGL3*_mJg3'
        b'Q{FJn!j2Cxj+&99KZ$X3Dfk${f-VIN6Z)K3dFBT^T$|(k2|_)hl6RdRF$R9_VP*_IjLS8k6?6Bd34m}&)lNXT-B7WzS2MU50~l_t'
        b'LPHFbDm2^z%S~(psK;6q)-`x`-c9tGH;ZfY(CaL&39qxb=FQ!Adv232_vj?TJh%HROr3^3&UySSk6&{iQ5XbV5SseT1Ixl$%vTQ7'
        b'C?|RI#K#JQpld0lB3LFufNn5|-4-Pa(D>Fa7&DEoHnT6uNra$=S%Wyuf)C7=^;66Lg))pL$XFCWyvoM`+JT)sJ8>kx9!voE&n2jp'
        b'UAi^4tPaB(Ct&=t*Q94Bx@QuVGiz{wb-H`eJqZ#z`Q?0M)@49Hf`Z^F#V@l2`MQf`Mh!e*zf+je^?WWz6fmPjy!XyI&3!3*;u1+*'
        b'UYQgVv4m9XOpr&7dGT)MP4l*HB$5`y(J}z2&3f-lr?REX-KBg#){oh5{!d===H2c_^Z$Lf3+RX6U|-Y+B=LP_=m6+diaA^Y58E<d'
        b'mG&MpIAbWg8_65AvR>pol|VFsSHw;*ubA6EDnYV`^qbPpbY`GrR{DwhGx>tq^MaXs!F+!;a~htXP<BWYqcpZJ5;`QDu>oet_(wAo'
        b'Ia;i?Xyn{4L>k{>2B#O33h_CWMl{CD5ORgIQ=KfGaDYKEawX7wD$!t8w6m}$`A@XX&h8VClqp39t@=_KqlIvm0^+LmRmOg^hs^Wv'
        b'x#>C_5U<bL%XIza$PF`kWokxFg&E+$$~DOnJ?PV$;&?OcQ)&VeZ16b|d<xdjlH><##S_bvg&D9sbWN!h=g1A&0y8RRWCp>4Mbvtj'
        b'sX(oZ1^EPHhHujAJQQR@->VD;{XxAVPwQ;F9Eoq2TOE|ux+$+ye3{Oi=}>YRW?h#RphR1@wb#FcBldKo5P!jr97lRjNjUQW>|va?'
        b'SM^!?(VVR?$gbG1kLr8Xyb60oz6dGxbll{9Nk4LKjbEA>wpHv0*1VsY$b14#&qgf&G2`9l+#@&E?jtg5v78w5gh^SordKjkuQX@z'
        b'?HY4xGaUYcPKi2J#@uPvZMIfbFyke{&`6nk;8V^#Gd%j9?DZQa#zoVEcrR$O=S^Jew<W_4hz~?$-GzmvVNsmUD~-QvB2L+tKn6@D'
        b'DpQl|)-^sWX}?j16lQgsaWKPmUY*&F1(F<*IpNriq_@M&pYxu7ltn=4)CnlQ+%3uLyWDVb^nMJBf7p=Jg})NeM<e05ph+5Cf<!jD'
        b'5(#^Y%tqGM27S)N3Z$auyE0vul1fyx?Lbl<n5xAU_u@CpZ&}Qun-%2EH&*rv;P>k~b|BSXYAfD;s_bTWW%=S)M94i~cE=7wfwJQb'
        b'zHPH2+v}=tOK`EME_cVX5>z*<3~XtN&A6{>T4dvD!N+iJKVJv7C0dc@yUy8Ig7g&orAaD(W^z4zfr$Ng_yiU0;r=7_`VQDmT#l@}'
        b'OxMi7JBf5x861#|gaxpO`c<)}zic8Ie6N)$D)Hg>yAX_BOscYEHso-rV?hK|=cYOD-AP#lljH4ysMX21*3Zh>nZK<U))qaxw&J_X'
        b'5Y%3nlipcIi?Q#VOedVMLADIc-HYgQ<<IE1y=;+uw`{Brlz(}>m(Kzf`bFU|qy+OKYDqPFx1@Q#OiNg4um3rK+snQ?G5K7X=eaWO'
        b'xw1hvlNmt_g$=^aeyDUeJ`Vkx4daX%0$NF@CA#x|`pwJRJPmk`F)iFNJ7sOGB&l1{*1jwz^nzVG+n$NWhQ$WsvVLh#H%`hdVZ<nf'
        b'g|8t)twWUa_>JuSjcn(Rwsnf;Ki3#ur=niMcRlLgFE#%ef2mY5RtN=0(P39;73O#5B6-wmQ&@VHlf`A8;xcYM=<crqtx4KJPM++y'
        b'7}MP5(&M^RF{KexiEco;<nPG*9`qz_U{k*|s$Wdb%`Vh|gG+jjFP0&9Be0L?zUC)>wR}5NICII%oGi&?!4cRlSAQ!e$A-mB-g@-f'
        b'DRZTlQB=l^6CdbOxMtR~U4W<(W3MW~D|nu~x2#KcH1PD6l2^!+4pK$R)0~YgyJ;-d?QGmr*rjy@BGKBA{{So5m3XRG#=fCD+aeio'
        b'EsHt$;cEZRSZEyVSkR@-6nJ+s3|`asaZFU%EKfO`rtzhDuodn4SFr+at1InM#qvKBqhDjBgbX$;Ys_V5($Y4q6%l#QCFgQj_M?i{'
        b'W$I6oUUVke+tpc^om0z_c9qUozlNvJDcd-wEG^Tz{GB=Jfn^&5g=b>)ADEuKvAj`6E*O)LUx7p0LJ*nhSi@K3&&yRI4If2F;NM~L'
        b'$>l0#!&|xR{N*bD+`W9Yo_r^5ZKG>nsgsp4m!Lp*caHiC6?dhy;aBFzV(1y=yeMt87{)Z{$5*7+vp1OQFga!8=0+)bwyu$KY}|Od'
        b'lzh0;FK@Shw1mi9iIFd?FlKFJ_+lrAv9Bo{%(MPZBRQ1b?>GGkn8K5(b!^7W0X+TF(q25RPXYLn-S}#JL?a&5_%-|n7{gCsuv?G1'
        b'H^>=`ky*_xL{kRV8%&DxQWgDvQ5$eO)BGCIv<kBuoBN2S6<GLY%lm(|NY--4OKDERjKB`|<}jal7aM7o9^sv#*cSiyTk@xNDcRom'
        b'T`HpKPAn_E4ovY2_0bYZ-Nt2`|NQRJ^r4OY{--2eljgtkos;V0*X;h*oMoWvlAcdN*EbH9<{b|J)ah<-6T`3x=<jrzw<BPkQN5uj'
        b'<&(QhJ-bV}zmyKLyO>YlnK>kHJBSYq#lNF!?=8%`cB3;k^GzN@fRFIcf-%Xi%b0ly=Q>Ka;4F%0wiSQYJ0{s5Q~iGCBfR>HAMJjb'
        b'|K!6ndJ8iT@faBGCO5qPm@dZk8tL*lV)PL2G)jy8Mi21)emzAv7@#<!=^cI)t@Rbm=r4TpmxMGCi)djUho7Jh`zfN83}Bk!i@m)v'
        b')e%+^Z09Nq9dVRllifA*l+qN2IaZ#MJO75Wh^J{dTW3+2iZK(Io8{o$Rag3Xu<0>uT%65rGCv`<r*pNXQx(dpK2lx(0{C!vr)A-G'
        b'fp!;Q<U;pms{S#o;TJ=>4sc?X@)u74ZZ`V}jKskh(Vaz3zhniW4bIAm4URg_zf<Z5#(5pg;T|nzR>6*%G$HC}i9N?5B?)OWU(d?w'
        b'3o-TU*oY=zSPFVET_t|0G!U%8xo8cphLyqRuutJ!W@&|3_>M|((?>kkaMHb50Xj5bp`<5y(9#MxqnXf1naHd|y1HawB_cn@15vEp'
        b'_k3|N)T%iNH0F%NSXQDtFVZa)Cxr#O5=*HOYWjB=8AK9n<PHiNpT{pKMW@C5VnOPng&i6q$Q8D53{atm?9RJ!7?dii)Du<8DM|;O'
        b'+nE&*YmTZ&e|zDsowe#psiT0Q(HTaNVfGNx-`d^SX5G|D0K`uE7C$8G^(O;ZZrQjzYMmIA@$bmT>@sVcWNNpv-M_T2%gQZl_y*7?'
        b'Ry)%R)ukQ&phv$H2|WrBPP@#Hct?2VH2;cRU2(NvmN|uvybpc;t$Swp+1LaoI?E?NYlNSrxnlClyS{`l<1ZtR>7WHjDNp`nB14V_'
        b'b}Yi($KCIzf>S2#x~=VHciNcK+T~6=XVbMRXMQ>|bA?KCICXzfPCax)XIFOr)%qM2KW%cqcZ3Z7B?TwN--udTzdhIT+|eLCi@)>$'
        b'NI7nAdG4IZ5wtsS|9r;i9p4ey1Fa}I2+h;<&pdO&glG&Tt7Gng#hA}v$CwEdBpoWAmG?@Sk6_B?0|CxxtnM9(nM4JSnHqkLv-ipz'
        b'IP)(!CGGE-hW+9yLGfcS-#B6-1LF`6Esb}Z#siTPqZOj~cTK~>bAc%SkSQ*)SHyg1KrxUYz{p;LB$(p{6eNKR?3E!siuVnIJQ2{&'
        b'#8QF`_P9)^MC7kdk79a_v|r2&!+hp76M27&ZMP7>3Zc~PNg*iducjZnOfZe(OeuIAAMwXiqLJ6JL63qdDnfn;=1uN2d3Kt(ou)zd'
        b'38o*?K1;=!XLxKCZ3((0%&m<hF4G}`nApaNEOF4|H1aEIKF<r*@YpToT5c&fUnn>I&8_9A^CD`I*vUrpY=^iKF*Z1o!<52W5y#Ej'
        b'_*R?d8Ixe~NeHoLgwuyeU`vMy^6`FgIL)ku#gjU|pY_qV!GwIMbz}*0V>oi8#1cf+h%74TTpG!Y2VcX;I7SB_#|oo^>41!-638%`'
        b'yqVcO6ccMg!Je-7oP+@u0G}iM0nr~ErYSIyaxKBEHzAJ$lK6*<0I>`O@G;@c=a9gmS#3<1ax&ZG$p+)Og3C5B`G`RZV{(z)KEy~8'
        b'DebWg^FJoU!8tt?vl>3ahlkO_>uKzpPLJL+NffcK+L#ZGf)c^%VFH%P@D+YY5Z;=9<eB^7Bb!RW<WygN3Vh(=O&*;Iz?=MG9Rzkr'
        b'00u^JH7pbFE36Y96wG4~D~53=%O-DR?uMx`-Q=Xk<cR>^^CWb#-H$WTsJ(ARHkP#>a9aCpy7wsR1jW2&MCn1ZvG!Pu2{H+K>hKO#'
        b'fe>Tl=Y7fZ;f)d4zNpT|Hfqz@iH_qx?@N(6kN?1G8`br9Xg)BszidPbKNyl+V(pI@>Ag^v)ah@v=~$<(twZPW7&KD2q(37mJJoQ}'
        b'I;fivjC@GXegl+9lGbgM%K-s7NGOL!5l{k{CYW**vOLG&&u0Pbh;Cv`F>6#SYom4S8@E{hG@SR@<1h=2?cW+v;%%H(ME9&N>{rJ2'
        b'|0%jndt5VRY=3DTGL7<y8w5M4FW33(rlJhcM@Rdlk^GjKFhU13x2%)UsCE1Z8`@9Yzm4faWdFGF{%c5x60vjE2I`pcHiMVzbU#sa'
        b'UXb2u-ZMsA^|mjx$NaDHwtmwUSkI$iUk7!5Wvr;q(0|o=%P2*5cjSSnH8(VG8a*x}IiI{6?6rf!9Srj_x;N=J_5<$t1d9Wjq7%{m'
        b'OUFg<28#K!x7;r8f5+@S&%k-nz_6I(jMLiz-h@Ow%(Lf3Y`-|7_5Np=B3LY<rDuiUV-F01r^DDOvxjtP9Pxm)AOqnG8NQ9{!fi&J'
        b'`6Dd9jq_e?EFIZ3K?Z==C%wtd-v4^k3!JI({y*>ie|+{H>@*B?63-YDM3}k}Pq!KqSS)t|mfm1YNyvVvF@+`*SLjnz$@<pB-ufvK'
        b';Iv>>b)O`@&gk@HWP#I1Z&W52Rq-`O;RQ=kGC4-H+A^3*-$S;y<yGGQQt$st_&)?)Lz{hl!s1Je;LJ7|kqjm;OoA*;pz9d~gh??X'
        b'Pa|+wOG3ipHAc@p#>pQF*|(i+kBvEK5cZR$&^m?Dp@u|^-uu4@{!gFdvvSpd+OD4xV-JUeepn1bcBHr1ecpc>HJJu~PsV9gWMQ;Q'
        b'N>)YFIJuI!AEx#!_W5g1F~+ADlLmtYT~SSvv4uu^yiE^2OGxZgH5UM?1@5CGSDJ)4SHky1eUF)&G4p-6CeBC`SnEZzF|>6ha~Hah'
        b'pw~tH69dFn&l<evsA#8rk~Vs1;~+<Iw2`@j$P$gwNy8W?bewcdW&TOr;~`qVn2a!bLO{6(q{tCx)cqnZ)X3b4y8Vb~I#Z-k8{_90'
        b')pC4tuF*3Gl+0}UmiPAWdeYz}n#IhWJPf9SA`j8&NOuW`E<6v>BoT{iUMcCvW0lOu24Olcc>h0w{~FwAV{u^wqV5Zq@;s)w2)C^S'
        b'1g8T9KC<C5CtGH<Zt{Bi6Ph4!Aq%8azI5hC2z2yc-m_}q!;n{FItrnD;JhfiSe$;&FlAO&JqMQhq4(gSwIIw=D6z~XK+AxyUJy3+'
        b'q@_v%yMaLipJ_VG^7LHhD+qOM7-`6`g3pZ=qx_!tp_>@=6~ft^_ZGC;{Q^-Y!tW6LRm<Te^!zYp%#ePy#M-A|{!o~61w2q`E3M1#'
        b'g=!$_>kK*T48m)Z21|d>U~O?XFNTa+dY)lrANbkz)&|$R25{7cg#qd_6!iLu^n(UK<NU!O+!nv<{r~;V4z0k+j1@{!ydph)(2$T$'
        b'>5YWK1&?ZVka&6t*rE*mcuG#}#%T|a;xjOBz`D?v-iLhC7*y6(g{A-1u)Ku;<ZlzS0fQchlwp>tzeuO}>3dMv7eTgSu*tBz&)|>^'
        b'i+U)G+i5TdhIwNHFTs5A3gTM~q;!jjoJ+mqUM(G1wqqE|Yo>qY)7!wOM9ITq=E-_R!_x9@|M@e{NPJkLF65`L^8I47EUZb0W5qNX'
        b'kQp*u7p~_FBdi1l;W<|T5@9r*F5lg~>-Prk_Xc4&X7#Nb4AePMk0{K~B;lSmM2W)YfrqVz9wIEp6u@mZG@l{BZx0@pWRh`D8K9$k'
        b'ENnS=-UOecu&}kDe7&KE4@LWRvWnSYXc*DaiuhVXi>)~^m8&s;Wzq9nC=|(ua@B_E>nH{p0siAF3{cPhSD4_W@t$8p`$f~&P&N(z'
        b'eZI;J1|)gRCsvDek(7zWp(1b-mu**AvWU@e>~j9x=#cnm?IYodmiNwZWrm*1s4f;gv@ZIn!D9bfv(}Kl)_?-Bae44ROWcHE+$uxV'
        b'CD1SM!>urwe+umv_xu#fEjRRB49)xwth-D@dZxG5GNBd>vxjjH8ITuBkO;%zVVVpBmjUx>8k_ze0{kJANjD%{>$4RS?m<J(g;4GR'
        b'Lnibih2yTJV2%uMj;wHwxKsnBr_ATUw?};!$|V~VIaJTLq4gdEmjIAs`dnyLk24M%lw<03c+|O2PG{)(Cba6c-Z1dT{mw9bHguK6'
        b'vhVZUBMSXt#pXXBW$r<X?0_`yJqb+*N9Piw^Dyo%1LYD$O^0%K8hXA0ZJEI%Wr+GJ6y)@L849uP%TR8<ff^L`oB`i3eI}F(H&Abi'
        b'rcc8!0&gJ(>Mhaq6nr}!3gc5)f@A=`#YBvr_3?f-I(XsJ?FvJ4s(<?(hN)g<UstDpS7dvjp(}ALnIR31hqS8LQo+A1sGA=LP1VT|'
        b'M-U@5ka9;PNZg(HwO!dRHcV-iaa~&f*vRM*Dtb%o{25Dy43rc};h0;tj5F_*APvnX81q4MwPbft>_f<TvgVhP*oUC)n-R0C$Os2+'
        b'*AL?kr9A=cnGQ{CJTp_`qb~$nD*n5Y0Vpg6$2i~}b&pcLMC-~aImRw)3{M0cPviIM1(<mvRN#AxQS770C7P)cL8<e1a2nhHSu)V5'
        b'?6#8uWXn@6cV)>=mQ5ro4?t_Z)RcarK(t8AL>8cS!w;^q11jgP0zp1Bdd(NV$_w|n7j6iG`~Lqw+`!x5`u_*q%aQk_zg^<BSQ5cZ'
        b'W}svsQQ4A6`rBC9Q+BY!?CQX~M600b(zSe_-U=ygxDLoODf32&5I(36{y!^?f2~9-V!qEuoXYk9^&r`)`i6MvAR$e{-szH@JwS{u'
        b'#<rMRV|wd%Z|<$%D&N>u(yQOx4TJYyfz6ZiGQa106E;p2T%qfpR@CjK)O~(V;*NP$WmB)Z$>3dy_-bj}kbC@&Q+{a&-447<b542D'
        b'C}KL0j05k~e51S)|9ae#)CbAXUlQ?Gq%E7D-kL&eRUvAUf!$2j_e-_8%pXwKq0>6h|EJ;0=)d`E50D{e6Y=fRr?)=6CG$r<{crg>'
        b'{rM}10#(zGeCzvMZHcR<WLzp-I)Hk$==$mqKQ8T`Gwh$~la2Stv1thm3DhR+y&6l2lM{VLe0RZfDBo39!j+YrFk;k2>I|!9n(`4}'
        b'9nedhta5UA6ZDnL6_@n*V|jfyynf=D^TmSi2Ep6|#T+_+L-SZkGGSNgQr)B~DHXcnwjOj-ce|PG5G4Dmn^|2#hJrC8{Re2bvjXE*'
        b'mbB4sx&ogb44aLMlUV{rCQ}#<K!0a=pGfj<Mt{q5T8Z~&1D;I}mZUE&@jOuCda&ezhzz{{K&*Ir0(3S{F3w3P0TjN3NrB~iMNG1A'
        b'JF=(GF3GX2Lp(^YDBEjqh*X$D8{W?L>NJH;kKZ6gDPo_zs3cz<i80y|2eCrsO&e0#2{Hl;Ps4U{4cE~9YeZY0ZsKL-fi9{~G1a9+'
        b'VMQanm&TgveClRnom(_(eD7OG$W+BbcLB%jUYXP#B`GSe41o-ZxZ3MAv`vbIS|hfqASNO|;k^iSF$eeXpmuQybX!qX;AMFrC+oUD'
        b'AAU=m8hTnt%^&a?e%h+kFmwirSwM6EC_V#@P}jxvUgf7y*s8Bhf1yp}e<j8X6B_SD<?C*R`HMFORV?PFl~kOSrg7ig_Go9*X6XuZ'
        b'j5iH@g^mU}g!kJ|tOp$14@C}@@NNl8(GuiCh@sQ@7`mT}G~cg9la@t!_0F?|SIyUjly?%d=FjB43dml~Jq2hAs9TLq8wP#T!JH}5'
        b'{PX_>7*zmLM$hx!eyC8`L|rn)d|c#nIhO#6eXy4D>ZWCRQ&a`BDRA8K8hN{_;S6%%=WVwFz0iN-Z+~}U-fjx-n$UdTJ2O<Ias9va'
        b'bN9`U&iqoChfabUD)Kp(;C{dUKmAF7{DGVKo7YDN5!_!2ZYc%!i;DzcX^rF@auHcH$l^?*u=-&M<QxufuUgMNmJd*Gp}!aN@D2h+'
        b'RK?rc#8j6Oz`mIwMj2f1T9Bu>El&Wpc0KoU;mzWN500S=|F5$DD7sltNYa!Q!#3>-stdoZtfsOESze_IeqtY7FW68&u)d$L%b>FX'
        b'wHCXnKWd}>z{v)~sD&t)C2%{}^(l0HZZe3CZ1n91@#|xKGQrh^=6CCp36dBS&7TosEBE}$tGlt@Czx1Ry^l_Agt1SSFj&MG3c|pw'
        b'TMO@9HS4p)V_=IxQGu`U>Ns)lreU0!FNn!I@ou|==v3NO;9u3LvD0n#CmeKVygdOVBy^_R_26IMnPbld|GAw;y9xZ8vYvy%%RpPy'
        b'AO#4xo+~`9A$)V*n=qtjHmzk3y5AX6Op4cg#Opcn`i0?4G32%w0=B%n-s@NQYO$6W169F*<Y{q%=I^a<eR^;tn7IlOL2DD%yb)7u'
        b'q^1{Q?mi{UxfNm9^dd|VPqAN6uZR|j$l!)6pDs=z#oH1Wi9dZ|&4gYV2h}rvU94N2?gnc=-mM72NU|8OAwS)@th|F5O~fX@F7})$'
        b'9%Q#RDFIPkp&HUx_3V0CF=XnccfIUipwG{B&{b;+a>Fy|5d{p*kuQpt;Ni#%p<;BJABv3*s0jc1?4WY;!(z{e08%-3yqJlEpE<Qn'
        b'dB8qpSN`}x@v5PTCCY0Dt6selKGmn}>$w_sC1B|8tMdJESNw-Uuclr*_@k$I|4NsqxaCj#3vDtb8L+?Voe=f@r>h`!LrPQct!%8B'
        b'6F$~)Od*}%JIaZXa?y!$?A*MlbNn~+KJz=8)ENVvp~k;nJT9?|mdf^oOb!%#-T)o?{pc4w=CT*L_fVjc`7?ebMszYRJaJ@fLClV?'
        b'CwCQloS;-o<|N<SFf2Zn#JmQ_yheUBN!{{W+F=;&h3U+LW|5=UN%5#3*4w!1QFRM8_+ALp4vU@)X6(iJvPxM&6C9QWF)y5)KVuga'
        b'h#Wh7dI+SNlu&t%(EjO3xh}6UZ>~HI{J!nKJQA|F8@Cka`{m7*y4DvhT*>S#LhY-oq{9R`#%zUcYn~}iS+XLNwn%a<Qr%l_D7@JS'
        b'8{hp@L6iD`cyKhBsYQZ}CySBpP%EsJ44CVbrb@p>5~ev1t-OkRm%mOVy&hY!4E&czYVx1YJPrM~0@CIMxK<#wL33gh_zUV-UE~`s'
        b'!h39Zw@!?UoE&jzkXc{czP|Vy*(rZg*8CTVlaq}4LkaAzyQ40~;xm2LU2jCV?aG$zz1pc3WgkQVZe{T*drP1B2XrYGZU@tdNOgq&'
        b'tBaXc#gyHx$tt!sYP3W+9jEpBpm`RLU8~U-R}gNC(x7oGRM;!H>%n3`efcwq@QYjz6f^f1zak&7yFuOXtck<QUl&pf(&34R%4?Ps'
        b'FU7UQ$k-LFYTK)^B28j(Y>=b5quh^)ga9UW#bhfIbS;83l)brgGgwLi4P(piQ&&}L*Y^8YmgkqR?au973*&Gv(9EC7SM?J2tzq{l'
        b'+-nrO0j0RBM>$CqdnkZKCXOm*${=Ced@%Gg`qQ|8$%tZ47|1DWy27soRMIo+VBF1v+i2-oen_4lW{;~#CH);Sl}Y>k3g#7_|4mdQ'
        b'*&fifymR^T6#obb8Cw4KqfK+L&+huPxA5p4XZM^ZL(ldD`i@k;-;0w{LzkkhZPRyG&-O2Vzc+qh*gf#J+xobBf7s{p2uXPqkvYNV'
        b'$2f=rIzOpWRgmEDtDFZGvU>kT=W#{mF&=wgtC*;DZx8HTzKsv>>RJw+*?{^NNWd{bI`;b_GHjS&!eFm=sg#rFi#+Fx2Dwe#`64C`'
        b'ey8SKk&_j}TUn)0CUElWBF`C6<|(LqjcL9t8piukq_Lu#d;cH`A`>MN=w-0apDb!WSwyY`M8X3_?f)$5sKA)NuYp_T=S90^fDD#L'
        b'{W5!}7`M(V;{f!|d~Bc)27Mg3k4pcrDDP*C8D7&qyv8B!D8tcaJgvqmg7d}Y_f5a^BC$60--b1mdfAPhx!5<sSHy-|+^`O3KS`gt'
        b'oIdd}HFKGodBr`Dmp=7%I;nnXDKt-;I^s5rxxbE(<b8Kdz5m+&VAsB)-QwPGd%!1slI~6ui#Mmha>tJ!AARu<-eM!?#w6pUWRa}>'
        b'<uy$An!d!;dmZAg;7l3T6>uy(ZUY(o%MwD*VyO>IM7vWLlff}da8jI|=uS&?L-ok%Kx}k^$J#2~<oxnv;slGi3*8fI++WX?<o$eA'
        b'J$kh=pdh@v1Jr{zoyQXw`KK<Pjm4YZRs=b_KcTDDZAG?7tRoVh(XB&K7kFm#n)avGI7D4RfVZ<3p}S=!VO_Gy`m#-TPrNS0YTY&n'
        b'sE?Nt2{1o#+PJ&H1OcXk4B3@P*jQ{}&<)s)Y0<2Y?pD?G6@J#AkXa${(aaO5^|~Uh$Q~3IM+WUmz)4Zd!2^jxz4XV6K>Ove5K{#n'
        b'g*y>MI;6-LQ<0A!PdCAG#qeEYD2g`-MYSm8w}{D~EoTn9u~fb&fLT-I<$-dGZt_52&F+@PhRo_n1wb*_dFTxZpZ<yOQQu%!Lfm08'
        b'ixAUN902G8>N)phdJ!4Xycj3R>>X}*m-}d-cD}V0kS5LdgKq&q`+9XWd`$(f1A|uREBqq741{#~Wx-xNmsKRG<~eC1>P$%X5o%b>'
        b'3_^@<P1UNTSG_SznT18YverJq^*fVO;QJ;f8m3n@{K~AFP19(K>_n>;jyD;`WWe;@MBcYIgfP0o_x1e7pOgdg!Mqx5*VDz=ZoKCz'
        b'-;2-2W#g1ZJ-^)&i!6Rl5j8^ff(>u_5>JYE#=&cXo)aOxqH$ta-18F;A)B)xjniX*mvmk@U^Ol!7RgV38}&2alL=iznO9&Z<Hkkg'
        b'-DFtQ3pmY5@>W8j_xzcDk@+fUQ5|+eh$cA_CkEJM=5PRQ)W_R$=hyXIo9&ke)9Oj7`h;JlXOQLhEBE6UJ&H3P-6`qAt^I`gHLO^k'
        b'*CKIEt&2E5{l0p&TrHOr$P2<E$U#rYwm#-vxUc7C%*(|Uxfvn3_@dm5uv~m$ZboQ+P^)Cc-29-*-~w^JXhqPNWQ8azG8b2cXRL_K'
        b'@)TyQ@Qj|}wJN00fcB3i8X`+i`k7c(EmqVU7w5A4MRwo}J5iu4z{B{k?@#$X3?qg0i>JG>Jb6HeM`2^FEsjBUpkKC-3_GY5F^<RJ'
        b'jj4Pg>GaewP4HzQ=xLqPqhoBoHyylM{e$mK;q+uP&-mW5VaYA<ZG@$~MK{6M6S$%S4<c_Ix;Q>(+o01E(qT+FVN5<_Ol9UlRO`^B'
        b'oX{kn(WIV?vk@Vmb_P0$uw5yBHX^jo-W(gLRgKQ@S;3<)mIdumRGm13zd3@t2JwO4B->6wo0``#TC>=O54O;>ak13Hdt)2y3A4*P'
        b'!*+&rh3t%V_}l3KyMvw{RF4AMyNk%Y#yeEfYeHG)Nb>Y`o~GsMdU3+Yb$ui@vsk(Ep^3#xu-iedIzjgkwOkdTKfK3zIAb~oY6erU'
        b'x;0hnSZ6xbXVZ)p0v4a%y9Ycwk6-V5wdZeYAC3&tgmXlZ_7SCfkBYj86$5;1EhI$==Fs^w`Xk9G5-UJY(~%6a@u@~}tkg6rPF|)?'
        b'l#xWNhYX}yK2{m)#Vj&nI1nKI?*ZAB_q4>d0$`TesRmg41z9PtoW-mdh*>86JQJ?8sPDDm+F`<`4*_$}g@6IJMx{d~ktnDxYT<0O'
        b'(ojK}OiB~3(t4_B=@~vbsOjI(Vce%YrjJt6dvB!C3O$Rb(UkFl$7r*XjtbG6L!oK!JC6Y*Fwhij4$1DJQqog$Qj9%+2MeUN8+;%1'
        b'w?7KQ6?haNclu-AsS&GNW|HMuVLJg<?+i{6CmRD2L6t6b<`sTLI#|UiIhk;iaGFD#yfO(VEz16w0tD``D9VW6+!Jm|H<#X$-kSh5'
        b'HKxt@&Da+^)ZYCd+qxL+0gzb!m;yB7SaNSdPt7fL|Bw8r$8O07C%no*GZzX|5*)<XLri?ZO<JL!h}!OJC;sa~IugrEAY7*lovb#>'
        b'uHIS5oGFYAbI4=kVpC&R#umm_#XcR|65G97q!s*;X!SemduhAeu0>|dOfFnHtt-JQzsmb!V^oOxMHSIgQm{<HXI<x?mFI;?T}MG1'
        b'71NBm2FCAD9~W<xZw=eJa%<t%s;y6NZQ0trwQuXUTd&nuDe9|2Q{tYLgIyl*rO>bAC;WE#&V6}>;^f>`QDsnyloX|?ll7IkW1>oZ'
        b'vMD?<1zFdcXg_t+^`sX=4EreONJP|gAqmk~zce|Bl)~5==XtCm8t##X*D0G3n?4SM0yn7bxOB$5-$ORw;-gS!f>o@BGUHvzkD#F2'
        b'GcbC1w;qsQqF6lYJUH5}SM}n_^5h)=@DR?POdlt}3OCOHoH}{D^Eo@->hFjJz0`JvByVy&HzsmyvcC{+cf2rvrWaSY@StiCsM;jx'
        b'HG3m|e#@_x=QI|oS4#6$q;zML{oduB{-$NBVaY0I&(@IqD1dXh3ov`I+AMa=Rab}$Wcj9kalo1aQ`Ea)&+OTt&Z<B3TD}-`B{zzg'
        b'lEC@-_EB^_eezo{BE#b8`Vg(SU#wM45y-)VL!WtpFUSQySk{8f8NOJI6qF&Jh^EhA$#k)N&wI(Lh-3E1=9C5D+SthZw8#?;;6n6z'
        b'tR;~ak=8<Gb}m(r==I;@dIZd~)m*A(Qz<yn-8Z5(hS+GlRhAOs5CPN-vJ)w)F<A;>r>$$0U{L5Z7+jswMiwN7)3K4#3&^%bJpBd6'
        b'{O+-ly|}ecVJG%%`AkdtzcfE$YQOTp5FJ1!C6Gh+4Gg94dRcsYFz+B1-ZlCQZx50F%+LD%O`tJ#A`bPT^pUu^Dg+#!#p<PEw4Gu;'
        b'TNZEGETW#})rZBTtYSg2tY1ckH~iMDj-2XLcE2#<PbTdQII)5(4j5|*w*ySy9Px91fI5nY4!bea0zB^kG{zA}m4WRmYOQ*;R2}uJ'
        b'^a{U7oayt8({Lq0kLmSzuAZpZiyX8g!J&8LI!uoGVd+jadEGf8W4?S0$*FAmc@U~z=JWGRiW;sooJ#@2mO_Iit?$qWJI>flcO;k;'
        b'&XJ6$!jJ@0uy5_J8jNUl?&X<_1wNn03}#PgxVEcvX~Vg$gnm3C<tc~6w$k5u9JlSg0TzN?-;X<#HX_)TE(65Q?u|}5cnGZUg@N|`'
        b'aU8DhDj10e!rFbtHWJcsm9#x&6LrZ}*`>lgsr^g``|P-=;aYP_1ghLAAN(L~z^?49To`CQXr1!E1;!vfXM`mnzUPJH9lz0e(SF9_'
        b'k2@}QsHkvzcvnX*<v8QD&j$VeBB1l7RMK`-(ORL^3vL-T2MWA?r#cgu{RI|(af<$?-$&5C=gr(?`4FA_1Xy89<=&RT?$vO`X;L`O'
        b'I4;^uA~0^#r+A3$@Gk3O!_|KOq|V6XGr8>VvlC0ZF0RbV9SKQ#D{LGG+^odBE@Z6Gj$5>n6&Df9odFI461fLOXQyXDKLJQS(@4mO'
        b'hk{--%=saJs_K(uF);kvB5WLCVb5bBd2#;zcuyZzufg>r8DQaW4od;cb^24}zyd(Y2+^ykfDC;urB`Xf!M`T&nuH9lxR~@J^f{8c'
        b'IO|N(ThQ<cF5iB!`6FJB6DxNFY)y)Zg^m05OS?Sg?2t~+cTd|Hi`LHuz}aoNlue}x*c=X?G)<RyOR!RK$27e(L>+dmSl$G7N5CAl'
        b'9fR>CL2`Ns+|SwLl=ou&zL3mQD3Yx3-t!%=j{7C^M?U3@^c1oQ*6B8NCZsS4xPb&~r;<x)H{oSVWhag)Chlu&+tyg=u{Kg^X`4=l'
        b'9Qb@<TjMF&n7x9tOHJ&v&HE(Al?6?AVZ9fRo?(-paI(K=_mu9QbneCb4sQ><5a`~vBm4Z0v$6$trmvSBZru6CmG)uT1<AO$A2%Q8'
        b'hehK!n9iO<{8IU@C2x|Ur2PM(?%m^>y0XRblau5mBu7gSA`sf<90>-BZ3rrXY6}s=qdr1}fK0tZqCBKJbr@S8rE`;DLqKdXR(aG;'
        b'lOPhPj2f+?m6;H2suX9?PHk&-hH;8jrw^~SR;`-v+9!avoj&G%e)oRv@1NwHefC~^z4qE`?WeYN6U6Z?f3G-EzQ-l0LELxwBI|Y!'
        b'KNh)Ma3;5zRTiJfTsMsaVat(<uv3+2BOJQQy%F<FX6=s-V|G8B3xE%E^R{X?nzqJH@>ql2(vyb!h9^g!r0#1dcJc7EuFl;yv&#|a'
        b'h~&C>SZ(Xct<%U`>-U2%0U6CU9kiei{!4%G8{0-ik$Y>j>&PDl`dvJBZEMFIdh)AD*88wI>jA+2my<m_cE>9lZGHO@tov(Qt?!4^'
        b'6=tTSX-jBV%Rp+y-}S`THmBiMQ7Yeh5*e3{mp_y{Q_(^SB!`lcl`B@Pg!WKnU@aZ>^ttKYm5N;}yK#$wlnn<4ihKHi^uGkxR8y>M'
        b'W%VA#)KHSQKA9A+sFf<LH73PMXaK7=@zqE0^yxLLCfv_7Y!z4qRq}D}={KQm%^hVN2Vy8T7$aX_elHv7ZkI>S73eGP7^#S|xUz~X'
        b'WdyD?-e-gcUS`xuCCNs|Z_78Gs8CjavPz5-RTxR2l0-LmI2IL*mQ+E(lt-7I1MN_qOWB7L4`597s~NkJELxpH&h_;v(%u~6VOzUM'
        b'Ht|ag)9Y^<p~XNAl=XZ-QkJr%Q}abY)z@<_j-95YB7A+J-Q3iS;Rho1f{31T$H6s`jfdx3s&n8#oKt0#P2wq`tt2aTQY8R_f6D*2'
        b'0A{4eD;>X8Okb=tL|S$Rln%5IzC0Nxk}!teZf<*2r2h1Mfb&2hDXzY*iO0$&GL5VB4*|X48W>5ym1$O`;gR~ASF5OT5QE4nv5tu%'
        b'rVYLs(6@fMflZ37(HK_c%RJ78xTKrcUK`LyU+ES2(97_P;6}MvNu(G&;zQ9!mU08T^4<4)<h^`Aqnm3nM4vQ74TnZrsOXbal)j&E'
        b'Q4w(oxL<=okA)`h6*bb7{el(ynfALk0L7E70|BgzkNaOlWGM~dK30;_5%91SN&_o3s65(}eJZ3k(d~WEz5uxX(vXJ=uYDBPn9(w('
        b'T><gwzojbY3arluFi@ki(CV5Lkm}li>PnU4`IP;*W>sK>Q8HenKKC}G6|o?W5x0jOsXzD+BgI7vu8Xh^@p#5mb_MjsAQ<9{0C@aj'
        b'F&FU!^>(Gt2K4<yE*1&|+P|2%<DjIba#K@}>@FMZhNw~uvB3^(D89z9A-IX4Js>QrO!i+4NNm<Cf$E$769I<*Z2{}X0Q8gSJmp!u'
        b'^t~dIqc(;@r+R>1#Hzlgc1(D79mhC3L{g9qo^AHj#BtCsa=@!1+4}nNN(zf(<NkPT_kBf5=viEt?1PAz0&(s*?QE&>G!B{z!BtfP'
        b'cG87aO=cfwAKVLS`@EpxCdtWBf=_ZPVi6Bna}3+SUd=D#@m5F1@e(aZIkn<h)sO{Umi?Cqm9qLs)&zda)JpZv>sgzg26~PJ776@}'
        b'^SW9d$K$TIp=;MxtKxXXJ2u9tg?_Vk%j>`XLaY7@zA7BIo(T|O#*`E<)G3ucALy9CQ|`Q+%F<j2s90*p?Np^ol&V&;_$hlIP^!bN'
        b'=K|FqXHD2##>OGYs)m+seJ=n^V)@?<<o&f!b22d9iDh4Lo-T~zOwUe^<HW1!`*e=yv)({G6?8`6zJu9q|74=Rl2u`ji;JnalC>oi'
        b'_|5|N5(FteeT(T$m&_%ID}hkxy*S9^PSmfxbMzm*EZ5=8(!zkg>vrgFG(A<iCZNA`%gDklj^E~%m8<qiGRyZK>E#?}CVBok5qamb'
        b'RRMA39gr|7uwGz%gdV)%IRN_cM6_vj#Me{loI4A5ELJHkJ1;jU*G5qun*EMz`0o=LE&1ET9y>q+1-6p{Fb#HuBa<L5zCCh3-rq6t'
        b';>l30+Q?gIX}=M8r>dJLyAd#KEv&v-IQ_oM?V{q!!R?}wF7Hs6=!ve~b%n$GA~pziBs@{SP#`RQmA}Qx>JG6OM0P{yupwZlLWO1a'
        b'WBC?J1Yy6CCM-rmtmj(%x9oE4a-FEPd9Y5@X!D{Cv({JnP2y<RvCH;jJAwd87X+Xnzz7}`TjKT_epLt&e@U0ca7<s)6>8kMqa+yd'
        b'yW4k0R2aqLnBshrK-=Lc%xy%0Xl2*%p9A`}e76xyPf3?aRuO3E?=g1sD&H*q(?qKX;M!@-LXqM%(T$x_Xp6zR+e=64{`8<bqoZfC'
        b'&FH3kLMm;Nu1|%{_yK-PBt$|X&0!FShSY_1(nf#2B-1|>XpTaMC)P>oLRumZ@Dbul8rSc^l*W*en+NZ|?4nsvPw6iMj$CQO&A)33'
        b'PiP8vYYJy1njb^sF{+HBFeIMNzUnW(HLyjFJ1#`M(6fPou8KY-E37g(wa<Dj5XXK<g;!gBEKv$juD~pl*yYU})dc^|z&X|g4=ePF'
        b'BXF`0qJ;MK0qDIT?+fAyL`8C;812n03adVEn^xW&0S12|*r2b_@#*b<m<WG7*`bM`IH#f1)t)dY|EB;tF3zE^DUT53NeYXL%Oh|r'
        b'#GB|oSbf5kpo?`7sT;4oXQEu!&C&ZVJB5YTz5sSFDn3UBBE$mK;pog*!1Z(hB7W=s0Oo>r_(ovP3xzSb^)G=UAPlG?P6iN;2a6*7'
        b'-vmH>c;%a#mzZ{N97ltRrSrjR(N6Bxn?`|*`bvN1+1=;#E=OpoEn+UDvl`a+a)-aUGlj?*-G49jNPP|tiYWeyhHKV)e2!4_N9fVx'
        b'izFM&ALvKp3^b?ZbFiv!n%@oPj3Lb@(9@$HGRFL;d-9>V<N@v7F^Q!2^t<2HqZ#NBG%9)~jf^(`Z2_}UNZ-jHSnHaEwUgNB7$W3<'
        b'N6+l++CCqx$;PRpdO1D-ZPx6Z9|UT{vm(Ec)5OR+E&T-639r7-t9SP4J&qdlpLNVmrLE^|v>UHu58n(lthGfqsN7+}Rr2i!H*~5g'
        b'fOOr1C))m6&D1F%-`a60uM^NfJ6P7CG-rpNjBFM(q}oC(M_F}vj-U=Aht%+vSo3q}JIM{&c!d8e`jLYZo<(0!e|#mdRj_-DzB$1r'
        b'>}ZZ?5t`R&gDbw5%^z7ev_aS-?|9{UiyT4^=3bm#uS?A@BCa+hxCH|Vh_^ODZ5YR$0J3*SkL;NSMf)^B#%}FrF4D2+nbCkxqe*mu'
        b'<xws3HjqmmVSG5@iRbj-7YWU4^~_<4bNOek?$|{3n;%C=h}YgujaG5v1yk6c8b95en$XEbbD7PYrm%$USO_Xo!$}SV@6d~><XM}p'
        b'$IA&GNJmavzYM5iA$u$n4C@!)md9o_e?*sJXmTZ&;WaZS%5pB!lel>*s@(7keKs*U9QWs;_1lY>$;p}X&-JZ7*;frw2rB8!XEaJ*'
        b'99Bg=nDif7>dS((6s6(8gjI_;t2XgK%Qa{*d?L7FuD&AkH}lZchemG~B}%1NC$}I6j>^<C&nMBqa1m6Li7Fx`GX!R{mVqv={AS~$'
        b'dJn6(Ipjcei@;7zBx73A>{Mh+uATLZmIOO>e`6!Zo+~3m?78xdzs+Y(J0?RMF4>uzpMGdp%g|`&5|=OB{3(KXi?h(P2v;7K&c%sS'
        b'0bV87%iIm*aAs(}3}6i(IVruJ5<6N#oeyg}T6|=b_47dU-WE^%UUWV;hRzjyOZ7%K*L(|!WD(o?O#nJdAWw`ik0JZ_pcg!dJam@}'
        b'!3})CT!>iZ<m%0TEf}5uK$lMl^nC)oQwVLM(kwu2LZuvN1N|Q!)wzrt1v)euZ~il5aFu6f!SnIpvv}6+RJCePsuG+_8(tX6X`ay3'
        b'9Bm6jPm`LOL*2AkaNBb@+?>lOPwp)y@8`@tQXd!CxD6jzcCza2XX5K?8ZMy9hW{22cipiv9jwa{ZgwGo(Us_w#?<KeG!l=`%}FS|'
        b'3S9%UPIbhN9Gri*eIlAZDCqm3z<H{`<4iKYmxtQ9der6wqu1fD(ZKI%+3f&2&%@j`f8@vm$a9u^20zhX(AQt!d<y^^HNS-bxYZUX'
        b'o|5)J@g|Ft)08IeQMz#&mmS<QaOJqLmt*!8FgxIx-FDQj0*jN7<C9yzIL<L2EEu`z3E4)@SuVoQQ_%NDf%EqO{-U`Xfj_DSgPt;D'
        b'Lh&XSfS(~e3gG(>o4X6{v8y9x+Y0*J1<u!?>^J7${YcqY?kRhm12k<e=zFEW*;wFljW;)<g3V09RB3Jv6s%2+OgHU4BUhOAqS0hG'
        b'BJkiIbK@u!hPR*bjx#t|3i|2`oWBK751XGypjI=WQj&w9QXcyCiUJ$Hn&)y7tC}BhE6);L$<8P96f3T--Ro!zHSa-oeIQp(tfk|L'
        b'kvq9I;Js`F`>BGyl?Bdnpzn9)vLNee#QFz|H_?do6KTH8%|D|)syfT<KMdZbdC6TIF)FVBTol?#G_`&n`d`v>eH?HExZQjiQW@|f'
        b'dqm7ZW;f;{z$~*JAribd&j*eM&2iD}v+UttMBE)mH|q-K;v}BcL(3F5Y-zPqLshwCRGO`J@Ay}74O(c5rDc*)S*pv8(v@R<1jnpE'
        b'ZONQj0DafZ6SE5XW)(PR6+HQoIVtb1u9{~QRDa{<2VI%bw3Gr!d33CeCZ!fko|J1=6)+2e70L|dyECw4k$EagP$<0$#aH0wbtRh>'
        b'1x%-8egyreTQVTE_Tc^I1oR5e9m&zbG0~)z3(}MdMG}e=%(0AiejPyDiqK<H;=GjTQx3;pur3i;MQMVRxf@_?e0unE2+1(>0}Ggg'
        b'Ge&tdd^tEbMfTL%LrSIM5$=)h$vvVI;|lu56*$Kgc-s2SSCCCA(}kN!RN0K{F}~X9cTEYQ$nIg+bQ8=xlz!%tlU<OIK;sx1lP--B'
        b'i%;LVY!M~MFViC0cLpMd(KifFcQ`gWr1``@0?a(xK$`hPzMJndV$@gp;(DxIKGEX99P&*;{9=01(T(OW@<-c-6Qe%MPaII;q>y&7'
        b'(5`_tq#ASvpUwy+)$s=NIc7XIjO05kHI|G}^T*6wM{75W&WH<sbe_%cWtoT2<C#|KqkJ$Ze?>0?{k91zU2U=;X-9sYE}pqS8=8k^'
        b'<h=Y7`Ry2X&%E);d~zV0opd6f6uJ&`%w~j#`Oo>O$~rn{<SLrr81hzp#*LIz@^XzR&6f0betoiqjo&@vUrkT(IJO<<9Q1%pFCidX'
        b'1t+}uecpVhH{auwn>UU)6$j=r8xHe3!dbbKf@>ywahJpEF@W06WelRl$(kwXVQuZ&xF^4FPd@Z%ypE=@vfBHR+p=gLv*VbBsvfEp'
        b'_1kRxhSic){%ZkAZC!}DBY&s~!WEOtu`QMFXfws(lg;EjX2x|Jvp6VnE;G<gFP@@X{BYIcM{31;*AUDt2;?nNXwE>Nk&z#}SLrPG'
        b'Ga`=tVBCZ_@_LGj+BYfu3XUb-0PE27+W53qVT(Nk`#OqK`sL`XH`+meJ9tKx`T4obj4?SLT?z$0`_0j_1U5k9o-Ch0t<7(Sr>33|'
        b'YE3>0u`Kf7ShB_OxXXb}R!z8!PO~ymPvzIsE}VsRO_JRTjEt=#ohn5YEXS#ee3B!_HwfZc)n8BHyviZ(Kj+w%2(fk6CU9Nz4EaM-'
        b'Ma9WQZ1HA}QZ^+;HA~Xg8{+7#x%JAWHvluDPSiqum~=7Yih*kuA%59J&C~};7c#ErovBo~APB16!&huKxdhnPtwc%(`+4>ht|XHf'
        b'J+B3A`MDO5R!JR|Qj%_H?Pa(BH6Sk=sCv>8&#S&-6=N!bx45uZ;EH?rEcZBP2nVyWrJt8EBcH^<G`@$L_C{sC%aPt#Cw;d5QBMd9'
        b'dvj8m@Zrl<qJ&jzZB=}%dRV(ER2TP1RW_!}W+}5#xuXjhi*=mai$H2F1tj#NEs*X*>GEgA=f2J+cuU4Xt-Wl>K>Dm7A>SJ1y%mr>'
        b'%#sT<?=!Muw_gY>7l65uod`6DPjzABrc^w5VI^i052&83(R>pCx6&BK&=8zhMP?kWd|;}F=Pv^z^H=`}!YUm=uv+hdWs5_gtU*xs'
        b'-DL-34#(h(=pVcEZ$UW2Z+{=B>Hj89?WY5C8Tt+f8p2Pl4Z;G`Y+H!{5w`+z4$nB#aZu`teHg8^J+)wp02ui+Vq~z<_b)(=9^+jg'
        b'O&-qH^<;dbO=_8icH@<!Oqx#vBmOiw0~*@XbI?gl*DbSHmRUG4x;})t3uO_)qy1o@A>unUy)a4>muDOYG|3)jSmOuQFvM8D3d%}0'
        b'2rvff$w{L{5xo5Yi!4N6fdPBbV8nM|K+zzK;Qd)3qj$aoqnp#-ALxkS#Y_sW!U32NVaYt;tf7gR_T2$nJHx6k8T`f{N3cPw05+P4'
        b'M+<Jy^QWUa@D}j<J2;kh2Q0BdebESxh~q*)kzqKxq7;=MmHlwv_wn=o3;f)p_;mzqZ~biiNCEK67LCSVNWm1&-E)itvV8$tJsOR='
        b'>)r(O?+w`2f=#-+mxL6Q?g`k^5R72@h;1VU!@C2Pgoq&Ud(%sILHfjRr^$9gTBP&Q1whZe>FvO)1o;>m!SXvGE#~`hhr1yC{(DkK'
        b'a4zkH^as9EpBvI1{B~Y+cHPp9HF>4m0~RXuLPj0Sk}&Cd9%`9P*L}DA?yv>UumwH`HtY;I5~R%53}(&ToxoVV%o$}#f(3)YdsCA5'
        b'3&=>c$c!yjZJIK2=WfjP$vsT>YQ`5N*erbPTJ~iq*Z5C%<Exy67V4&Mu#UM8#d$;5uql<F6WL)ufi^03@>?QD?grd|Q&)9yMd8;f'
        b'BB=k;#i@kUS31klTXqL#ir>WCA@_wYZuM8xr@DQszo0&YZ`X;@yI;wXb@eYian}bFTi7=IkjfplHNh5nZS}*~igMyq)8n#dxM)^s'
        b'3g)I8F4=GoKjiY8BIZ>#9rHNIvAwTkU2W=L+J7fTySXuJcmu}VJB$sth|#GUvRA~&tqPu%Me-HQ<(g+!OY3XS$eSmm;%M2(wKe0f'
        b'EzF5a4Ufxt#C${t9v8XZ?9(;9nS*-!C)c-6!8*hAYcca79kUOv-HPcyW|MqmIz5hx;fLU}Sa4_fQ7pKh%i~zto`BN&Z?)%RXjM5%'
        b'8!C-QY4zX8R$!Vh0v>jV%Yn<}n9GRkqrd6KOTP&C&olSDwduCvHoW1eEi$fX>a_}CoGL0Vn+nP~ZnbjX>Ud|XuFUosDYS-Q?y%u%'
        b'EXZGYoQg3MAEd+`CYy(WHw$?{YUsW6MR70|Mc#$8eyombtI2CckKC<;taH}rYE!>-hqaes47~uj^qISLJc8-~__-rCt(Wb5_S?{='
        b'Fwh<xf%bF|TIu33XtJjnXaH*p=0~uGHK@aw-iPHa(TSCOBaMkq@mAB~TAq#w$$BFJxbr!fC4DpzJnW_YOZ1k;?PYc25Z%J_T8;`='
        b'v-vYwIvO+5xQ`n$<Ed`K`>e@)DHl|&2!HY&NbBaAKgnfArV3w<?Z#ynk*(`j;k|^99RlyDk~wH;XDAjNy26UL6t`JI(2m(%Hiabz'
        b'D{g`}@J1vB4(1(={sd#~;QAzLs;=Q+v!G#3b3#L^>|)So>cgB5>%><;&BbnZHZ9I)BgA$55ZR}JPwRo4p}?onHoSPRj~^ThK9iP>'
        b'_p*E(KD>P#7${~&=`W70Z#0ANN=50!|73Tw4rD<0(UU>ObhFw|pu0aA<J!%V{S&Rs$vsZ=a)F+&;ALQKFAvhuU_du3R3t4u8jNGi'
        b'd|fZw#{ZVRF>`ci&&`;9MyG8w>@f%ONFlQod30Z=4WC1pwE4NVI$T@k&FbN<4wI}}6Lv^eK2?F1->|h^rV_u@T!gr;KH|-tU70**'
        b'yv~6ccX~^fgbqC`)xVADj}Ro^ABK_Rp?A8-8qUWobkzE)3oJd@sz{4*qQw|>g`NlohK#&iS96<x(iekn!RQWYVaZCcX4VD)P!>|h'
        b'l4-HwJj})t_uND+w=D7~bPz7%#1;Fc=L}fsT<ii1$&2>IlpOI^?kRSemAS!foQOuBqXM1lZvKzlyS8aGZDH=+{>ScML6ntVhb#%R'
        b'CI2{Qz^$mO87P8yk<obpvy27B7-$B8W;M>04cbKMHmS+|%wUelm4TTYU%4_^mJGJZosn*P#*)EFH+^Nv;HKL$EE$A4gV$)v_c>O('
        b'GVmEIO#|NAsa&5!1rNI&d7v&|qtoryk_||U+CM@4eOJt!^(X|olQVLY%TLNiJ|>(0%K0(baCl(o#$+RV6zGY$M>f$GW6Tvg8hAqT'
        b'FV}5y(Gnyc`Edfd9U5$d08)B+bu6&er79$vql{=UkPR>qJ_3jl@g#$Im^BBqPd+N2{+y8$Cm30*WMpwI=U({)(-<1aDCQ;xi%~L@'
        b'KO(E(1~I_pIA?M=r#&d2{|UJ~3UV2~eve#+gK|kE8M!pyBbR18l{J&os9mCVn9|ntglRLqq<|DRrQi_694uRdFAXbiotUyeyqR_@'
        b'C2N>3MhDhawuUwu*@vcOB`3Lj+8$PM*Kv;7f&f>rEQd|GW%bjRvZ@>=l55;)Dp?%5LL(j6tFPgaJR$-kdHx##*@HlMirN>dzrk_Q'
        b')5_LnxWbmTh}s{-nniZwR5HqLOu0f&g^n`ha_goZ7UcPicRS>yPkWqbkH?+|VNOfmD{YU$+9jBH^35qcQ1+<cMx3&!BV-7C2ROZ)'
        b'b}=%HC5OE#7VXoP>@jIwCUYSp%a2B6ImF1V<{nvoTUMo?jmiqKAv?@NV~rbRgIywrTRPYxO5Y$ewMcgzmkq8HnHr>yqtEy<Fo*Xm'
        b'Uk1yS!FC+YXmmg0%HT92d2;O_H+P1q`I*5dMD`56sqrg&Mu;UtXlf1$nPh}K4utH>z%3c$)fxBgGA;2rF1s=adxk*mczRUUE0C=F'
        b'w9MM4xq?pxF(lIl&oReMdVHZYJ#7XVr)13`LFkg4v1^rr`=20fsdntR*ActQ0gBB=?OpqV{G&zRd0(i#cRg!^5}cCl_uQ+D=2I3%'
        b'jO>LOS-(^;`d<3?aF;_W^WGSFPZY?G-Y6X!TR$glylQcps;|^WO(gA2%5c{)1=W{h>S9T|q;uA{>m!(Z8yt(9lu5g1<x=UnyAHT^'
        b'?a5$v=UujmOr2hb<EpD);dw`4dXt59iFS2Kq3DxB4Jd}ig;if^QuR8g<vN&RyG&OdZkMAiV<<t?<+_aI={3)rGxU(iROdSAx%`kw'
        b'+JXR@UdRBLmZOTs#;X9+WMkQnDeAjSEuzLQ&=V7?VZHzTK(Iet$XY}g{zF@`&b4C2O4AZ=i6NuDtmLT-N!ik*ImAA2DIC}}3p68B'
        b';Xa&@W9EFV^WB{K8pUF1?ZFarp4O?;nrck72Y)F(!iDTghiRXMdpQGBI?@%E42yxK$n=Td!g^R|dB>qwZdXN+Jd*n=H%rD1UXkRZ'
        b'SS#L_mh6*u<1KmZ(<7SmBn4?@&xbHUaW4mrA<aNSG)&Vrv&?&QDwme49)!L*#5|pmHG$Sd@ik!(yAq2q`1M~5fW0(4q^+zlCuqxi'
        b'&WJbP-W{*)=9;(73-0eryX~Pc?ORf_IU5p|f(5Rl_9+kSv*7+gbmNWlK`lAp*tWP+RNQ6i@|nZ6of**T_~z}|%=o=ir1d#Sj{~dA'
        b'Gdod|El(WFZ5A;Hl${8h*XZ4wz5`vh;JAC=pqsy2k&_yU4lC=r=lHVSlAMuiA1avR)a2OiSF^`boL|iszeSk8nt$T<Tn4xnAa6yG'
        b'8}CAH=I@Tq+0_#2y?68XZf;HyYuC3@YO@zcj;3tQ45rPWx9jefeOCqE&6ja7N4-=p_-9YXab7oGm)A~3$YLUjsAiF*U?FA8Ys~bv'
        b'CcBfGspt8N_#K_Ne^;QJ07fj%VHlyQ55}ucGWVY2qkfUvA=Ehp!P)Gv@P=Gr=0Ii+Gu8=m(I6gzV>|utSe|db)F?$81>{`)IUYIC'
        b'i}yRt*(d|rliAHO&(3B>TH{6W&R%W|{*E(#_b}S$^6S0x2QD#=8hUHE<mSq5M3C%MZYqyyux_rWPcBOfck|%CJvE%nCXH@hFaJ1R'
        b'XRsJT<A2?LJpzJBH<w8=$8T)^I>OCu=ZVYm3(4x7q+=QIiBozlf@+=b=~K9Ia-!^NM0Q^<ae196*XGC;nK#eRwJ}#quDE-tWH!J0'
        b'lNBSEKmxe*a5vt|mZgW2=(;M}iN|H46*J_r9M&-rgfYz6J~K%?>a!ZKxoq*5;~Om5Mtvq)lb?ZQJU>5c6IT_c;bK_EbMQ>4Xl9Nf'
        b'V>P_6RLWi!8Qs1<LOm&p_wji31fuC<zH5@$T!rAOHxc@eSu}h)$0Ys=CAugqbhotB7NK@vRw*{R%sd3MOd{tB8r(fKOkiJq-I3j9'
        b'nLw<n2<e#xy-*1%+w<;LiREx+t%T2P{GJ~?KI2`_q_Bo}y3tV?W<5%y7l)xkxsot?0dcqXc}(r252Xss%>qP*|1*N=^MMx`^BK{%'
        b'e{nZn*G(WyvnOe_S5r!H&0|;|H(Q%2HDyjJnxI}loR8q^CWW4lz%?SQVvm^Mko+RN4mTgjGG&IQr(bQzcTI}$--ls6HRuFPAdA4t'
        b'1PU9zqsMskA7oTXPEC6H%7G=8qnAuMH4RG^;-tVo9ek?^#2ijKEd}g}WMDOLb@Gz&*%Q*cyxH$IWU42HqNhDQHI9DiNoJGf5C=0('
        b'Aj$+}HXidqmTI<HJU^@G@r<_YlFU$&SURC%7T^pR8y915FA<grxM~{H$6~I<5k2oN#KlitS0B#Il0X|Y6AVuUo$p%1F+f5ig;IVI'
        b'hE>cG6W6lYT5b4Jh^k96y|tTJwgq*QG$9yP)YemTmUEowMvME;N8fi3{?#|FICw>lOz-*d_pNUS8H?`jo5UGVk+}bUtf9(g98jTS'
        b'y)g5+d9_H_te|V=A$SH|V-8L+pM@7(NwY1R2=VG$AT^hRRk|d?0<yg@9+af%0wdw~<}oWJdfBBP2jJTj!MDEtY2KLjwU<N$_wfy!'
        b'qh6W2dtja$AKn^)&N#x%f1DT8g0Du$<4NHG{6N?NTB##E#wfLpcR+nWcfd$CxO`8VXJnyCkwf$1Ep>MIt8<y(oLA>TKfckvd-s8P'
        b'V2QRwjJ`wQgzySu@S?@$j(K<ei0^)L-t$d(`0^Z4KicizpE;N*>c%}sR+`)9G3|G2G+-%6jee)AllC2{FpIP9nZH{+7i@j$*xp*_'
        b'wYlc{d3V1%ugo>q-uwRfT(jlg_e*ol|9Q{*@a=%g*f4<*VHxY@DUH)}Tx58TQE5z38j&2?SZ5exjyq}SgW*r<4m-{!pD6ujz)c_L'
        b'kn4vp1>8z9(c=h{T?*tFhlBeh4OmdD!<q<Sy;LWqrp<NZs>*>0;Id~!+x{RSlhnv#ZQ+^;XkblgC-f6I8Kv`FzM>qZ(iml4jBp&j'
        b'5^%G6S?%fwvLO{urBlOF)v3BvBUl+Eu0ahtul!`{Ii)d72~9=_flP(acIx^~Ij2FH%^^MspcTKei-Atg6oJ0~&hTdpJo0eq%!pKO'
        b'@C@O92F%k@UAwdA$)1e}+72a?kU4L7WdzX2_{7WEs@Q=AB-`4B&=nIYiz8H;t!x!XCnm`FR955W&`(n};TQ%E333iE^OQRS;!C%!'
        b'zXP9QHD49E-d4vVkp7dryhrBE<cSyGY2Myr)xNtJb(cdS(AIFG5o?a^TIERgIy$|bvHI5A{&NAXmb10JJ7i|aq7dR27(i38*4v8M'
        b'bu85cf`ynjlPj*d;}a9$`CW)}6SWPvH3|D<5AKh{s<xR{!D}qmqxnF;tIOLdy4)=~-DMLw{>JS(D{&A0no8?(tolvIvgBT5FxZIj'
        b'fdnE9%$(+^sFN~l5RYAA!t?rnf(zntn83$y>4^&za2rFIoA02Rsm}yw`g=6+b`iY+f7CnwGd(#}sVB(8sW?##c#AG-*68a$H?8ts'
        b'B-X@z##Vg3*i9TC-^;y7nYSPxz#VsidY(N5SOOK7E?p$7Vr;dhBZc#U{{20Pir+5Qz9C)lw$xmYGP~mN9%4n8ckP><aR-Q70uVG_'
        b'x<9aEE%7)yoaz0!&$Ckw;=j(<46Zsk_`c-=u=+R`_&gqhD&Vwr8s?5&Td*S8yJD?(O{{+ZKQ%Vw*%q;Yzg*yNL>-G1h==c-NjuIZ'
        b'Uxzs2Eku}Pb3>Y>OVR2*8OJ>rhr8l{P1+laFFoJ!CjE8CgJ`{fOOn~hP($<*Yr8rDt>NxKbJC&H{z&ZoN5lw`mLxPs$e_}kbUr#3'
        b'e9+_fp^`T!^8!@%I^~XQPP!cA#Pj#v>~fW1D_Xo{^uPf`XG>DM8$g~(=!spMyyBnUi?J&Ty!!E9Sqo7tFDB-&6=1LRMD>@!D{h$m'
        b'zx(;U?BxQ$W*>hpK1JXz)^#lFD$pvzwJ#-|IlM79r*X5VaWe(M#ZarLt7Rxvl-4rTA|fX=ZH`Tvl|x1;rg;=8l&Qu$q!QI957odA'
        b'I-_Kom*gwzYG(2;*N7A<leu~>q?(dV!wH<>M2>mQT#FnNXLD`h!e(JJk<GC^J8;p@$1rG@VI2LzI~o$hYPaEj94k6sxQzhoW3dV_'
        b'lH(^ZGNLw?v(N%hw)3^ItVJOUEw!=t`AflBznWw5FUIODRwI^u&1{&P{>voOI?u+Ex%KNz>nW|x+s*famKS-wFNoj`o=xk#jm;j@'
        b'{G`@qATzzi>&+2?O9}=!-R8~4;d6Fa9p3n|H=Aw=b8Pc=(lhqfZVQpLw1ioX9sw`ulnoOyFEi@!?64VcWVMG#z(A{yFdx@pLgr;g'
        b'PFOY_^GsIz6Gc_v_f{1dB?af7!8OqCx#}Yq78-NtB4xH(QZTecv`|@@tYQ~V!ih&PMS*vrQZhBJjgzX@JcOxqBu9eIq1EM7Stnzs'
        b'_J$Ny2^nz0f-N!(fh%2TEK;hEL_)GMht_ZAWvhjmTQad6wI&iH_vWaxb;gdTg!v0~m6_1fr-PW^+c=or`0}^JyilZNZtEc<nqH30'
        b'JC?1@_h<_#(+l3AB2j$-I$X5CTOiWrdr1(Dc1g`5LhW3Z3z%f9(M3YZ%1KzNQZ_Cab7xyMTLU9|eK+w=J;8$hnhb&1v4ty@hc?;6'
        b'L6l%M&|uBXJEzvNf;-pd;PIR(Aq2Qq5Co=j{3J$wF~=q%qouY``hy`dMA}*--`&FPpu^%h^y2WOY7M;&ONk_{$ov8Hcn)QsJ+dzp'
        b'+$&O6$icxpon<}I$850qI?yAUixy(NgQhA0r!%Kb*^`<s6jl4AnW5kVf?Gr%&WdNp&w}`10XTVieRCGNbPki&CM^<K77z;;6tOzl'
        b'owK&S0dxVNqX<yLB>)8=Y@uYB)Fy>&;44WPXu&?vjnCNAu_tcEJLW&2{GBXSn2mJ++D*17H4I4#hYkT$Mwpy~r-r%1P;NQo_Kf7F'
        b'$8ytKmS8zyjQbSKAC^kH>6qU@{+RXV?IZb>WBHXRKRuE^67tijO1GK>_%iYxbL&Wc-B^Adqc?sQ_D-gd(Yj_`%+W?gxc)aBXJ&Te'
        b'{3J)JC*}jiG%9_TcW5ezeP|Z?NfxEF#3?(LrL{OZJ&lhiIXWmsmv<;l)YS$*X<g{pqZY5y5z|<+Nu@kLVLbWAn1K_IWXJqf+3^%1'
        b'#ZIi6LynK>-~CW_%$X}4%Qe$6q{BJtGLE)ccS9}A$<d`d!Z(n50cUWXCw*s<=>^K+_6E<WaR+}kjPH1vPHPzi1m+_I(sR8-+eEot'
        b'kg0wIfeqsu8#ZODU**SzhvXH{L3%s8nbZ2_0cDSJyJWrQ0StSU54HdroHA8i*0vy9cTp{wnyOPYhHnt)Q#rdfc@!@tp=ML(9YU9z'
        b'4b`Ea7SRT>X_M^cx?Nyc9#3j)q7<p#p-sqeBJ1gGLF?&flBTpxiW;d(ovn<UK*HzNSDQn!;$O64SeD#68mq|`@tLb$&jc#MX5!vB'
        b'Q3>tMo>ajeqD7UocZn!n<3+z^UT>MmHmlM|CCq^qT1;mr%W+|5LT1r|?eZ+GG+ZCXq2ABZzLq3?!2{fCZ1xVJi^$L(Q*^9P?PjUH'
        b'V_EBFX}qWLr6lQO%0zq71>$n}si(cPXmSfnl4<tjZk#YD=Qs5)R9~q*fNS<+b1DkmMSXo)9_R9t&R?DDSmt``;Is8=Q)BoP;jN`!'
        b'xl6h^V<=wKN)OqCKU2mvH9vSs?zOubzs?wXO?0zm=mz{Cp3vS`$4Ot=)EF;K$duUpkAVH(TtGaG7L(57?2>y-fV_-qw0pk|kZfv>'
        b'J1yU3_ej4$tRA}P9r~T<Qp?aq_z8mbZk0+~5nO4eS7@_B0I>VztT{z4=W?I(S0_7`nTEn^WzBZya{Y@O>ct;slHK{M+Rbs6j%D>P'
        b'NCBOlh))jSlS`D406$%bPg1$p;#@9m-UNC>9eYA{h%Jq^wD+=0Xp`a46UI19TsE;{fvaO#W!KS~iiu>TsbN;fmZ*wPdcOXkcJRD+'
        b'SDClmC0)+{gvN<H3<7eC0rMGH!w$BE!j6iT^Tn6K{9gttR)H7I<i%YM%;8u`MtwrF$dC)X#>SP6l~VD;SYu`Amc&q#UlA9BqT0b%'
        b'yy7@)*Q;JPyOnP3YEJHCce7hq$3(;X0=DF4)={LC;>dC5<^1z}-UbrX5W@53-_&QeHlJ$Y3g6ge3b#9#>5ByB*;%`w$-RR53&&`G'
        b'(HZ;!CU!`0Xu__Jr@9JEFL<<&vzBt$ywD`;>zT%hI^6=`(lTxHCTj$yHHCvD^lpy%ku2>WlT7U%M?1Capm*qX(ZQ~vgTWt{^H=*f'
        b'%RL>-4l+Rhh=A?_pgkhfdK3KavYAG~F4wv@b#!uCegj^xqt09Rn=&z{=xZQHH<>Tn#@5oNyd_Vlk8q$zTUt|`pZ;``R!5Z-cn3>G'
        b'TD=!~v|vB_T*1P{BWG9T7#99|sd>%D(I{5-aKJ<3=lViV_9?D7_=>~QZv3L?L)Hzd6nd=S`o7e>(NgBvCzv&q4aK&~fymN?fM?QJ'
        b'S&q~v?Pdqdw#zspv1kvw;Zg8f1I!LFv*d}fvt+{1V}~8LPQ_IAL+@rMlkAk2qpcxW+M7K>@RYLANdA2&Q!hs^3_Ou+v-haV{xO8k'
        b'k432}JAi%)4FI6G9v$<{W}fZLGsZlhW1erLnYNxQ;`Pk9_YL&sp+lKZ*McvPj(ockd`)A%eSuz-bXdc?o=Nmb24?2B=Opu;nf8Uy'
        b'@=KMAIl|RLPe;@;H_c2pvy6t=Due7e_teYK>#s*kU%(5txcHVlB9)bzLGo+ES;BP?Ln-rk=Nu-b!!h)Clj4La<~}t3Uq{vDoij*I'
        b'8ltZlVuq`+^8yY7r6FI=BH2py*m@6^&M+xhmAN;U*@<v!6SxfP;|0|>{i7Aev*J;O6Ij9;dS`%UDx{eTr6)|}pO15(O76F+Y<~t-'
        b'iQsS>7JREp=B%tuJhY+&4TQOFZ|TP@lOnoomc<boG$a8&!$xveqb(Hth0!sIk@G#_Q*DJ1N|RGa5`3hV+bA<@7Ni982N!;!xrR-*'
        b'N6Ox<Yk13TI~q0`XTGWqW@qX%hs<&<j%Z~3le=XQZm-@RUD$$j?ipsnI3dkZEY-ivaXGZ+(`poFm8R)$V#ft1?72>R?vu}%qfkJY'
        b'Bgl!)Nytgd$;~Owsm$rhIhfO*b2{fz&P{b?sJc?5t_)LGPEhB@<h1%^Y2^LP5`x<Bk@=-~QC!4*iRwb7U^#pDGnr&9!9jkUczDkp'
        b'v=-liX=Y&96vB>U66?WEmjGMNU(po`u|ndh@)m&|UA^*<1vxi~`^sB5@cxix*_FvJNN3=aqi{_;M)NVF<8LK&=#$p+Fr1i-+4-y('
        b'uH`6xV&1HQ=o5cdYkPg#Dd!GQq%fWp^V$?)^)+&$@7N&uySM)k?mPC!w;$*FjvWKv%y;ayw;!M8JJwma<B=^7;my?K)cd6nhY1_^'
        b'*EIa%0;`vJ`{D6YnWdMPkQj``dkH`XI<<cW%7o*ZMTvBL$dqvddkF}58lt7rlC3KnghCZKxok}T)itu+dODzg<{J5e^@EY~B7#ei'
        b'fLov49k(=(&t*oj(ArYjr}w1u@20n33XH9BvQVM%)WRe=x0x#9Yo~2$VQK!3Nzjr$GQzYFooU$cmhR|BWVE)k#-UxQm)#NfWRP4*'
        b'+h^SB8)vx-MW|2cX7^3ZwFodtTK%CbLaawL_>Sn{!0rjT{cqlU(<8(Vh<1xcpM`Jk+O=}udYpI*>l>Fl^rq<Gp&p?_h>@+DLzu@='
        b'xj!<g_R(>3-q{}+>v2@<Z%*(ZL~C~TH{;eGcvuS$ntkx_>-~{@G;T-Q2p*Qm_jA!Y9s$eZSXTRrAd#&&D}5-9*nwd&eA8K}zZ0_@'
        b'{iDgWa>iQd@N3iJoL}Uim9_OYzJrftEyw*IVTH?a;w(m-12~YNIg4rjhQ)=1Aos0yAz#yi318S(fomSdoPWQk?4U&?vCCs)UU<UQ'
        b'8C!4dkn!Z<er75DWEneA9Um*_6vY<PwC|Q2CnMtdQ$nh5XslRKEK~5gf@+JjAas3uXKaiGO4D3<I2vRxq}hp<yJfGt@t!bJHYKE!'
        b'e;^XdKl}Y^Ir4B&!hca`=}4VR0i~Z`iW@BD|Hb#q5b|&)SojyErj67!@4rRg>@oTt!)&qD_0QQHw$SxG2V!ID_a|^{s9<dZC(&kE'
        b'g4;OmSTK`Eue<p@kx)~;6_u3G;2_#~W&CiT!$b<Zc^~FoG?-6jfZ|^;e2`~j34hmUTc8m#c_K&hv}7>3j*jMP&Jcb+^diWd6m;@!'
        b'tRdTiIu;QPeKjJ;1B|GD!gmZ9@pi%pEt3;Q_y8yc`2buHYQ|ybjt+uSBfC2E2hpW}UjAHE|2fmLwl-Ui4%QyLpaD|`ukZqzS(^qy'
        b'y!D%aTSWHMM&p`<fQ{0zvB`3xVHz1iNCN0MbZv7@3(FdZA$Pv8h%1j377R9vu9cQLXXY@sm=|#!T<kgeG99{Jw=lLa5d;j8@8m?*'
        b'MTXg}TgKSk8FC;>Gx6WZOJdj)-_G~pJ^2vXA&A%wcuYg$-0GJSUj&CqVw1CKX<YMepeU)Cs^fyS8H^XD@)P3jzf4BNh2Yl70qes7'
        b'QU;Iy*nl-PfRUx>nF?4n0g?-k#Df7%UVxkikD8c(^%nthHYyht(3AzHQv_|;=AyPK4cpZQm(H-&Xn3{C@H<%t&n<8n_L$p{R4vqY'
        b'mtiLzNhte5R~a9cXMbvkB6Ec1liAEMYTG+QI&%gtS*UHKulhzj-){K5rd5b3sqJ&{_yxMYP^I%@^Me^1AIKo_v}x5>m4*$p;U(Je'
        b'B5l~BHe}L<Cfd+pF?87tuPY4>+OUr{?57Rgv|%@Gc!M_lo;JLuVL?5ec7sbvxe!~DX*SlNrhOmj>42JYrBCvT!?-%iVeAXd;i{>Z'
        b';v*6=)rObU)Qh@PxC9<wJikt0p&aXN7K1~>!+fq-dtayr2&1<3A1i&8-w;g{3w6$`#d$h|!$|#JT4pjr&1`HS%%3d;8psg(J)GoJ'
        b'UstPjlEpOjn#Is&H|&@jVmCOM=8RPtI!TU^>XcZG1Vk8}MuYpwt`on{CYuv;5?^P!ETdtEk8&FahRP4(#AE!SGEwF73c^8PfX47k'
        b'JXZqCWq89p8!_Ew*bRy8FG3=2q;|Uu-D2@g@ueF^0VcNIFmA)FdokmCcom`3H(gKU`PCRH*6hKcezLiWz>IGXmiOSqLqcF1DUd9E'
        b'm5%~>ch%d2m%Bt=9gss(W_f$C_P{5J*|ihVlzJksqXYLx3ah9lVb`iI{vbMu7>yxSxw6+jbJF#s&sDO9b>%(QXWZzs{crWMWsL#1'
        b'z-Z`n8Fsj+*EBK6J{m=prPfHS>OI^uIXdRn6R*VB$`hwb{60gIy*#=}&aIjp1>D*%=OkuZ%A>1f%@$efV40|XRn^<KY`n@+i(y9{'
        b'fu_c=V1DCRevPp_+9+$TlC`caGx~2;5Wq}3wZmn2?Nr@`#>Ns52C30JjhK?Sze=OCZVez|JPX1AN$eN%NGQ=}RU<{Rgs{jK<I%x#'
        b'h_^oxxTwyDDoFuEL|w0gEkO)&TM&ahM+f%<gL0Z8aer-)LDoUR2!nVGgRI04^XIn#o8WoEL%oKM0U6=VM9lIY?vqEy+<sz5OkMeu'
        b'M<l0C8k$@c(H-$ziyYDVc04CB$6gU_f#{jxO)J>xTQ+`WDKG}~0%awP@+j0vqP!Yo1>y_vu^#coMpR!bsaOD{dJM0DO8Scf7<P_o'
        b'8~T;#QrYD)QGXeHGV(CVD&UHdazhrMfAH;|kBrm~O<}<3FlipZsz7OobCi3?FREMyg?xV+tX$@!I?qA50iU7sdGegW4T*2}eAx5='
        b'Zp{fK;t(`j>jc6$GF<amfV2|h5TA{XimDK-yh$Kwu|tD!VbJvE5D;5|WRQ|Nmccg*NC}!{Cm6pN!a_Mqz<oA2{fU7@!VYgOQfOhC'
        b'_<)XTI<&3Ob>AQ@a`lBWTgnKeC+Na+SJ6q=oX^OE8CTA*PM-lmbmKX!{y(Af_yV*5YI{xdAlReVB#R5%1OPw{0Al@7n58e2{s6C{'
        b'qhqc=krh)@D4#BQ!D47q8>6!(5j4&4c-16M;w+^xnx?iYsoxD2h|+@A8tg~$!g#J!x)P+ql;A=M5a729Fu4I&z*%{kMb9$Pr*Ra*'
        b'=t!KLU^Kj@G_=u%_T~6Yd=XA$@_^zPu9l%$M>&mDQ{gafRbq$smb=CS;$Ytr;#7E1m><lts|awY&j8Ya;$C(R>&l0$&q7Xr*nbQH'
        b'U41|$D2i57uMvG1L;9@pHX%R&Q<fm}ORy2zm2`CV3(qBMlS5;!um4TV3+2E9E3lx-7`;k1LQsl~lUQ??17!>ct|Kg<{>r7P#6q#Z'
        b'1N-3;W7##o19<^iS*3B}j~^&^2}dciF2lyiVaPz@3?Y`I%;m$l<`L}Bl5*F$(d<e)MpXU;{hENX6|<InpLXy?z9sj<n3_?db;jtz'
        b'ACh~J>RT#&gl1FnB>z&3De=Q{2SgDHh>WIT9Gt5|>+U53$E-gg#^Ka}Qh=$)^cM&bj0rL7{|h=43Z%b3MF+qEdZ%EARtE8BTA&IC'
        b'^f73B&;$=6xt(F;Mlxia{%ilA0RJhVhDZtjZS;A74704@C-6ro{1o~sT=B~!wc)ibGR*&Uh(b|9hLIeFdXrXL0)(U&coR>lPvgc+'
        b'9dQ<-AR`4$uPLSMKMs9d=n4mP0nG$?Ht4U~(4{lH?w^C{Tty(k;t`nv<)>Jm5vNb}`<ZC+fdD!H)-QxU3}{|c*eM+4m_H4`1JS2&'
        b'=n}-4oFIIL9X7l<Ea(IIr($+j5#(<jfq&&R>odXW)BXJjdJd~SG9VYIqG>~y((t-9o?+~73fsa*?b=;PRtf_y(H}CceBE=&=}aqM'
        b'9J8)ap2-+GqcOTXcC^jLeyf!S?cDX|FdGh#03J<sDXG^-tX^t_Re=1NA1u!lzRR;J!)qDGA2U*~>!>cOWOh=eCS4PH96!tM=Js;T'
        b'PorUuPwU6tm!bFV(UE=j$4+c~%tdv1sMpOEDDhM-j@G#NsIHUL>)mAUICF`HIgNm?89$;<iSL4O-I%LUQtmlb;4!ASxEa|R<lRzE'
        b'dgp&aG({4mN@s8y4ej8=`7Z)IYSQC&>h&gE09*(A%z#Lmp;03cN`ouQ#WkmDEC!c72%;sFOeS$9asZuojrWIKXsB*_=ij6&L+6A|'
        b'ZpuTR?|b+RaNnHtEUnJ5nm+Q{lk23jYiI{9Et6WPHubDLBY<!$u64}^Z_jg-WxhR|asFKT(;V=u=dhs_pb6%M1mWRhG}RV|Kc=SI'
        b'$O%&f>62=p^J(zVZy#7BkS?gvN>_gBLrzY+AIZkzY^*oC5REQoCeTi~?1pxNgONr^r44Q1Q^NyLp#=P#m~@hqHteFQ*OgS)DV#<9'
        b'73z6C@jYp*LTB)R_lh8U=7eWW#0f3<&-wj*-RxexbTzL}{@97HXPe)791!o5J$6F&*c1UeG@PMiAdL)H8#Y@gx6Wb6xH!8o63@6W'
        b'TSv74I>HzFq8~ePaW-0aWHI#E4F}8z5s;ZeM}pM+d5{qu=Fes`7jB*vcH?L<@h+6*9Mxf`4qRFS&YfhTF$Y4F9-U$D6v0g4a()~?'
        b'rjPU33HD<`@G2nrfcflfCW`5SBKofDeYa+wIL=gR{s4VA4~lku=82=hq(7r1y?{eg9Xw;2&d{jj+&6=ZM!MC&{zf598ybzE?c&ds'
        b'ewNOW3ih*b3$Ek{lxmDXd{(P52@SlR!YwYF!J!R%rPIBqYVIhhy(myg_9_h>#1w2!DU#x2g%kO63dn~Gn^=-eqbt26&t!3Fbq3t-'
        b'$~Wbi7K%VATJsjNZgY;a&*HMbb3rlYJX6>t23_V2hXOtp%4MRx5I+%-K^e~}%UxLB6lVk<%RhL=+SfPpgm)&AlzHpy;Mt$zbd488'
        b'qNX<I7W5sMdE!9u^F~HoH-Tbk%o4R4C|9E~`x$Jgrcn8*{~v)lzoDtkDNVGJYMVSMwEEo?TBxQvvRt_4Nz7jWy_{S3)*YR}?Pp<g'
        b'7N<1fnhY?eZlO}Q^KV*xXi54?rD5|NartJ>H<{__E1|g>Kfu+Rl*GNKYA~gPB~A9K9aF%<7(aw$6=_d#8E98ZLcG~HyUMZHkH#ry'
        b'a!j*4V9nFjls3~llrPFHxLhF8F7OJCy0;WM4VE(bL)3_UchpA|N>{4Rl>!1uODir$L7EyUqt&w@ew@oLR9<HK4z(-A(-)fi(42`6'
        b'(W@dtX5h3YHTNOf$5tLzNYuas+Le_+DX9)=Ebw_h7&b%O`AHCDI(bV3pvXpQXJvuT&<36>{dzzuhiDg5D5XlnE|R^7J%vrEkX)P~'
        b'?nVVCJz2UvEJD11&`~>$j<RB98pNh;;EALD;4p;uJMC1PM3vT}bd=elWg6U?a7^tehf0w7GPJ1;?n)zX_<rkn0NSCXcEU$Ri^<M>'
        b'IUgpIF7+DyEO7BPNEdaEGAM&20>ndoWF%CD0$1qbwqe?Zp(HycB4ZKze3%sM=j3g17OFd)_Nw`;hIJB~q`+e6CV*wheq`$%0Xx;L'
        b'26z7D_aGomn+^7>B-2vAj)Aw!NO`~-4u~~P9N_<Ghe{HfO`KqdT6iAUB!M4S=psk^R5=c=#}D*%IV|S7ht4~4fpN@#0QX&ZkNf_8'
        b'|9#rO?Y{?g;K$u}Ij*FBpNcCUPf88*@52}uA?rMDm0~-l7P<tZ<Y?B75d$v4X~r26_}5|B_i=CgKJISZx&^z7{tx*-BlrXMa=dsU'
        b'VMDl-pT`LW_-2KSZ#KeOMA(n=R`&A$8Qv;&n7;&3(ga+6<lj}2_SzsJ{s+Dn<5{Ercj-`L{)flVXE0#UAN3a*PZ6mF!NjP@M+Wqt'
        b'8<T?t(61<TBRN3T3Gqk{L6_uT<IfG^ziJX!>4^Ov{vJk0e(`VVI7FoW*l&zX6j~+)=fo0>LNDONRP4}S%9;3^!3_m;C;)f4ilCyd'
        b'QPF(F`b>EGqyBetm=ltRm*2T34E=r_8uP<(XxiO4bgV7>j7XH|Ktpjq9g7mLj>e)g@ivG>1*1`!|EYfwifWdPgrZ10SKb@Lg<+bd'
        b'KOV!iFS?_Q#{9p;{>Nfbh2pBe;wNLcFwFYPu~?M&E*&_gN%?U)WO;WW7KI=X`(7*ubbODDlz%^#17FHN{b$6Y)+x+*0C_hMg*Nu1'
        b'acJr6JKu>zh4;jv-$#Dhzb%8G7l)EuW6(_~3x&2t;+mN_8rQnl-l=}X-XV#g?O8!$M(o|J!n=Y1dl!r^gS3?2wHGK<`w4re!U2Ke'
        b'qST<hU<&*gEr6i$G(H0jSygGYRgTppU8Tu0Tvkh4q!xJN+EI+P&jQ{D8%KKAbm-;6yY@ql(-4^?{Dl38zk?<sTz={I`l#==o$rp{'
        b'{kUx$vF(6DJlD_vY2yeP!88VKF*AI}gkq1lD3{bH^*AtdGc$p2Xg5;r1JTxeu%<4OqeugHA3U@6<sAQfG)VyYNv?VBqfB0K%-WZ8'
        b'XL5;L{9hSdO)_@qNO0J1%-{m5Kh7`lsJ*pr{NJ&+)>S{x-ddLjt?gv-k$bHz7}oDwTmQ14o%(OuTjGDg-fB{RhP?%+>|T4D|8Lsc'
        b'o414Z_Pf^B8ug<F>tCYu-yZiPxn!7s0_)$kx1Zl;OqBJD!2giFB|Z%N40~(+a{$X5$j}+~K}2pimVxZiX#4X2ciPv`?f>)sOdR9S'
        b'2=DP{{?*v}vL6~-2etjF1~zyb8W?gW{{QXI9J&1+f97Y?@dJI!|Dr$BbNl~@Kck%_71KCPIeEqy;Jk%$gZBY0!3@Hv)>_ngXsnZ&'
        b'&ia<)Lk9<cNM4mjr#8H1ht4!4t_rnGC)&)!WYW%(l46pdZrx-`UpcVSLbaJRo5V}Rabdr(I~${0)W?>T(R?Bs&AqEBmoOIkXhkVY'
        b'A&s?AE=6(%?NcbGOSKC!=xj{8SgPN0oAwQo6Qqkbl}J~L&qV-|yo<P|08<~iGXtkHF*W!ZdDxj3NPCJhoayRW%EJn^^B+p}KXMcN'
        b'voQ?K?>p6o4tg7=c3#cRkj8~F+svT)nSw>az60qehE>AMZgwvhfSLQ!nQ_MsSHD7Hb7f){Lx)(&wNu?>WK{^Je+E-KLQ<x(HgMHD'
        b'S-DvxVRx|7x75^zDA1@{Qv#4-r*?a&HyY6vo5o{O3&8wS8UwT2Xy{P$S>@pzG<VwF*P4FfZ5685yy-DCfceHX^5vAhxc`FyaX)51'
        b'w#065(UeO~?Lz~YE`@YzLM)AAh*47!f6`?vg;J``&j4}i)whXIXcJD;r!L?^TJDNQj{3+FW{AnPV<~NDqn(ZF)2tcXXj+%~58AgF'
        b'AX?c_pfNPrq&&PtjRvk<wDT&kC4nNj>9p5KA!i4Q&g5Fhqwy2>fY^TpXY`b1RGUaP=qnk5rbWYOG_KyhoY{moC4?Eq2ExI9&m<NR'
        b'Q-FPKfR*|*-neCfnxnHDb~Q{z)62WSu#>Ur*`aEKN4yTRQ@iZP@L;mqv5raKtIrRyQ#;O4yM}VSF(K!}XAl&2l5%+73H2?<?8{jP'
        b'de*qN*Ghe^sllZo(F1nFfzsy)J9VHT+J78(IX^xJeZ%k7M=rYz4nV_l8uw9-)$a8>dU_<Q`qI*~;(u?a9BbS;Q3o@Rh2-==HUJ1Y'
        b'eXiL4{vg!SXNiVr%|Tr4{1_OJi<YE7qf>u~S8;UWRU9bqav7_rm%7Y#A!KCzsx^C8Z>x)f|83`M`RjpH2bc#e2-Dkd3Idh=nh+;o'
        b'{%yF$dDUb#A()g$90lxhcw8lF>ZOASn!J8wSqzkxWY$Hg4KG%m#?P+{VZbtN{yT8npJL#?crV<&aTn3O%)nv`wWBfn=d-fCEXYdY'
        b'xu0a^g~xvmE87jgN^AMISV^_T@Egm#=fyKLQnWq**x4U?fUJw@+@I62ecin%SqwexiwFzV1M<-0cIU?@A?SM5=)Vli0PL#%ihC$W'
        b'cE|cx-1{Y&yAMBJE(eMoIUP$QyUGsmm+psb+t=L>_>8P1`cr!m!e<u32Sl2Sn2MAYBBaxJ#s1ol)qtJ6Lq|EF<y9_~&~@CFh^71E'
        b'JI-5p>kD)S2XUG8UH&g%`2R4jbY4{?nKWxyU}Dvd(%M+uzlzm&Eak+pl#v-S2bvktcil&|J`RkF4<W-6%HpHs9ZUC1XjH`y3t2W7'
        b'Rbq`8sRXUUqBbKVMDv-M2At?;*{Pj0^^%ctw9;tx7WJZq+5-d-En?d6BErAS2>A2SwTlS!J0>)tMQv}-V(`Di8Uqb*W4OZD^I=Ns'
        b'UKaQ^Z-?rZvZ|H{l}iNMYa;KF&hRWkpH^*jehk=FR?@!9Pyw(XDo}rfude_a&A)tHwXH5>^<GKxWZ4`3$t*Rsd3!kS&%vmLkE?+P'
        b'9EJzscX_~H4-LR!<zZ+Em~M0lnD;G{Y$l<ve8%X!T4FF68T##12UvS)ytG8i0p-%tQsoCYG$gUlKvO#b5vfiZADK(X?~%9J5ieT!'
        b'@oncV#Cmj2J_Fx42H$Uzr2zb=Q6r*EN^0||e}H#TBCV3fa5VySugk)Tb^CI*Z(sK<1|$>ugk?0NO9}DH!<U~Q3A#5@k7sXh;o0^{'
        b'GS|~7vOlIytWQoIEk4#bh93d`RX}mzSi(a}Wd1u+@tiO;FNq}CVa)<%>M*HiZ4aMWxn$}7iVi!YnUb=)kesNc9p|lrpvoY6zO!ad'
        b'mH_k^fgWU?9VAhbxgcHbjp3gUf7JRQ_MLXOv}3#Vfp51vSsZG2`n3NTZFOJ>?rn7y!B$tc`}|{Bau0BOX-7_ESLOkJ4%6zal6zWR'
        b'DMjeJ7T(k5pyL72CB#BfM;UHifDy%5!z^JkngfEqQ&@ne2D^b+BlU)b+PyTyNWBCW7Bm>x@*+Tyz~hTmAL8e&LeO|dwb3N%7zv>R'
        b'rr{_;U#tVgNVf&8q6_hIsR_DwX_*)L_mc8i+r=}%jzc|bpRF>yR7JfQA0k<`G^z?3Of8RLEkM18FQFo7dpM!LH0Q1{>n3?C$`$~)'
        b'n2?fkFls8|0Sp;h;BC;*b~1)m@@+#a3q^)jUz`p6%>4rxG|#tf>>)R@u`fMV9>0gNu}h=6%8rFB?eQQRd#?(%3km(rS)j<dWlZbq'
        b'HuAAbTKja8w#>U_`z6KGNeXxnU$QgWm7A)d7lU@|s1EQOK?J<Ac_2C^wbMxLOpR0`UhJt%RvKPXQZKgfCGhkjXyf@B0kbfZ;E(8;'
        b'Wvt;GHI=dn{pm;T&Z~_ZO+nEDbnR4=be0!tQcUxvC(qhGAwx&KWMS5S#`B9O1r1bcq=aT{6F&%@_gx(xzRlGqOlLefFbX6t{eSFz'
        b'dt4J&`uAj#OhOnf0gOPfX2K<apb%6pVhe$Wi@FQ3fVy>;pxpe`{;c&<t!|U3As}rrUP!2RlVA|2v`A}JEV}`1sxEYa?zXmDyXqEu'
        b'S=-lIZLO>1ea=j{Dc-u<-{teZ|G;GCT%Pls=XTDV?=!LUp>0roNr)p_>Imds@Q%@MrO$T0>$T8--J1z}>o@t2<j#-WyZ||4p$e91'
        b'#xzkg9~m}Lhr<2WOT(cVD0X2Ju3v=+I`v1!Qubfr=4C~Jy2?Rafio88lMq;1;=x_)+Zrq`7RQpl7ee?D&+xv$^>Z;sR~2O}T^R;~'
        b'3#^2p)o+?GtQaTl{|D#`vste+QF7`HGzU1$fr5H{a1JuP2j^g`ls3M@tUq<4{~z4E#9-ijEd_JiF>Pk=)R~N{kso(y`H#@w5aB@G'
        b'm4Cs3{e?0C9kK3Hz2gFEGiq}Y(sm&z|5oV*J%WZn^T4Pf^VARHeHg;T2#Nql9Y|d8ndY2?Y++#`OIPHnC=%Ra4$lKU;+3>LTmKxG'
        b'!zdoCkW`=G+s@3+u$ytiK`@6a<3is~@CI{uFw-8ztKTexPQkvM>UN%UVT|L=oKV3nJCv}mev^Qahf^o@AG>U}^rjfZpF@Szp#*Q>'
        b'6O3$-Pc)Y<Y~pPNfns!aB%_Kx;^s985u>&lk?XL^&Iih={R*l@MZK0BG(RF2Jf}+in&>iLABNHI5BKY+mOzds)N#T45#<#ZGDS|W'
        b'b;#--Ot4?r#JFlF<41;Vj=c}&(^GE!3`mR4)j+_2L=JfH0UmEJJt&TS+B{npd;lac!5;3nOuCLAeh}o0_{23*@Es>LA@6ZTZC924'
        b'7|Di#$tnBA)Il{M>{mwl##8SU{gI2llr<hv-b&fw9^)ppnX}OcpCKGIUBNII;(lZfhsEzi|GQj02cyp=*sIKNtKCDJgzCttdIj~G'
        b')Q8ycog|baN!_kczos9D`0_jS3aq}6swru}_5Zlyym-Y({SJPLkCZgx%BffN)2=G0I#?-^-k}^^`OFRF_8U^_HTU=8C(ouaI?=}@'
        b'+9k6G^L?r@t^aH~Sv^XWqFs!xKS;zjT&rLiSXFq1JK;W*lPDzeeFs8b=147AdJwLE9Md)YLi4z$XNz!=p~nD!&Mpu}Pj@UbM9Zmd'
        b'AH^pc<PF;sr&rH!jeayHJD19ib-=C0KftY6TlJ3C<ln?pU!}5Lj_A0QM8nxfh1b8UuA#Ec4!BHoolOwdZXX0MlRjr%!s;E4#d!7n'
        b'O_#1X7P1OYC10AqJu_hIS7pNF7T<-GYCJZ#IpdKJclu|Qc6oM9>&Cm*B^~T$r-!h*@l#6AG*F(o%95SjtPG_X!%kBRSkFG(vUt;_'
        b'zX%tdahwr;6w}Qoxk?OM)^$2YjM5E!T-^JQq(bM7kBdu*wIQG9e3vxmlkAPH>lbIMsGjFzR^&Q*RtvN99odT=*=ddse6i=!o}KEs'
        b'wkKZ*kFp-qBf$HQC3}C&n%nXBqy<koj_WdhQ7X)uyC^O5*XQ30{9J^-UzM>w{wvZuE*K@53KuXRnn1a6CMRkCnKU9-jyOqsZNzWw'
        b'e)OZCHIzH&hD*B--Lhj?$W50!M|1~Pq~RR+N0KFrP6YE?&TK)>#iUQJQ=ccLe3{gUQ*WX_{YeenObC3mK{HVj8?N(X>@fGDX9HI|'
        b'c_#A#g|Zna;YeFEuHA$BXykTXM|r!nFQNN+SvQsMVd&$_e?mW1Y%Iwp+lkAMu~x#RQ`+I1)00$EBNs0@@Ta6RcsIA1ut#z)1mI2w'
        b'_H2&s-J5S2aN_sa`r?%YmUN+HBJOO%ro^H(9CqMXlB7?P{SN&-yl}eC8(3*hq4VZjU@;HCW#os;Vhh>W+FgV=cEgVZjzu0K{nzed'
        b')yA&uc=*7<q(TcORkPNyZsO-VBxmr>4rw#ns3r?@yb5z33JK<#I#33dS1_B<t5qm;R0=HyhfVm<SpxzMzbb5LbD+OX4o8zv{c=*1'
        b'q1vEZNG!;y*t{s#2BSNfvnQ#hcA9wm0aH@52O6BYqyJ%OwLT!GA*c1!&F{B{H<@i7Skjj@0c_-Ar^Gr1*nt-qMzBKyx%B}&Q;zZE'
        b'&9^Fi!-)9J;UY?tlz>yeNFvz@IPomDP_!T?^7Nuu;A{C#G|FpA808V2g;leYRT-<YU<aN{QsoF$IbN!qhhVU9XY_b0Iu_>GCvXig'
        b'RF4Il)lVla%XNBSg+i~DFycI6L9U|^Mx2Y%Ym^9AtZ|^fG`N3Rt|nKv@XCT5l2{ZQ`R>-o_2`@nO9%Wmq4|Xiqh(%==~u=MzXOYt'
        b'!i8qK-vHEaAnG?{JoFlxh%1#?t8hHo=J|4U^_7}7T&VztkMpdBUvDkMosVEfA^FxiT%UyL9>b1IXbdsWFyvHjQi@PYj;6Vp`%D~h'
        b'ti~iE_k(Y1W}7>-sYnhDDYhKa)DdTjnEU=GgglK;#wJWBgA&rp9;ah+d0H^}M#5gwC*e(C=5YpxVzFE?K87{UAcN#NLa^^SUh<rW'
        b';Bk(Tk41hLXPzVn!HGy}=7$RtMzB$*CW}}w8l%w525d_ZR>wMwz_wVp&^T&^mPQBqYjz;~f2>Ac#EH*Qy%U%i9|~&T>T2-qf7KPg'
        b'neu?S4ZFf*W?!<2`tz(ZCI?r)!-a6O$6X;EjPm{)v6Cle-Hx3+K5G~|**R+r?BvB+|83aG_h$Wc?4)DX|Hn@L@4-%PioGA~<ht1Z'
        b'-Pp;%S^sZiCv6J!F5iuvEb`&lA}|D=oF7YX)$g^bUl$p$u+lDhGvDsIPOV9V)w0a&A*J?)(MPB->X}42+}aKcsJ(_TwA;<WsQ+Y&'
        b'@u8Sh%9g5at+q5+8n(Qlu~}Fl8D6lGk%sy6&X1S+5jE%ewlI-)Ng@r%v`PJmxI(TpoRinbZl!E!&v^hB1+bwLI;-b+2)%2V+@ATU'
        b'3bd@~@Ul@mTi(=cxLTy}g2jsRZBKNHoU#Sl<bH%C$g9|xDmC$T^|9$*J!}3>cbQIii7;4cP`~Yn{SmJ|YWI0+&t>YBPO6USJ>+ZL'
        b'rhd)254E`AN-K>BRjAW)YUL?rIf*CE8UYEdk*ZBn^*#nSK;uCVj=+PyHG~IMQH?5ecD?RaJScim6yy*|5e^jARS~0hygkCvp110j'
        b'J@3(bmbQMK2imjzH3EcY=V%y2XhiWKAXGo+7C>m88xU$A1ccIgUdP6RE=ar+9yIwDJm@!U8V~xGwnILQ2mP9TFFa`8Fdo!-D;`vt'
        b'@Su3mNuDby)2(>Wxd`uAa4X)iU-uw*P}6@g9yD)EJgEIPJgENagW*B{B5*Tk1RnGb{8=#q4@z@}@Vf;KDo1Eg6Akg?>B5*Z0{6g!'
        b'GJsHS;ShH8PIyrJC_JcrBp%fMGvPsBygxiBAs7=6>bw;XieV!Vq0TUuiZZ>uIe!?BCZ+LoG#>PcK3n!!cu@O-pMVE7{a4^Y^M>%C'
        b'cB#7F4JlIIh6gnvJZS74@Ssn)4?AR!ao8bq2oKu%6V9!e9{Ajfvf=*Dt=t0>`ozd{E7|vf3B3ys`r~iGgx>r7s_B8wul^e`p?4WZ'
        b'QRGj+gqr?~F`-Y4JiC%T`s|9t_26e$O#l9~D?^x2{l>dsLi31E2Qi_hyI?}+VJh1bZcJ$Q?U>LI;hiy|vj#Dtg!s;w&>5J~_JsRL'
        b'aQ5w(&=Aj&n9ztpOsHrKOsEw3(mS9+m9)8|QJurO{&V9()1%$E(2r-vd=@tn7y4z~Xk6%pI5#eojPCV}cE9yLA2%j0^y9cOaG`nI'
        b'F2}iXp>+rsdMOS??ziDW>mih5aG`smZ^eb?0gY~4XdS|Zo{MAfR3mYrb{ZF2e+OJ>_9$HF<741L?TXagL0sruH!gH-9CKzkua<*Q'
        b'ej{+92VsR^55;FGDEpmYp+*$z)PtXOgF<0|br7k5EY=y}K7$FZm#XbFCbS+#Fg7N1Vf0-wp$iyHXvl}`j=E{RE911v7=#J6OzX8w'
        b'V=$r5#tmUYceyd4#yErt-4>^!>_Cp^mX4j%dY8tHz=Y0-8N!5?#knz|rE#M$p;Kb+0~7lEwBFxN8^VMxh#Q3oT|2EegYHy2KhBK_'
        b'eP&v3Dsw9<?q|e=)-jk+J%b6g-whMG;C4)C|D&+7s=E~vTE}2Q^$aGo?p91_(zM=L(`eA=#JG`|&|L~@S5|Jv^l81*na5<@Ju#se'
        b'hESoq;%b5r9#kl&?6M#?D%ANaOgRD-icZSWuuy&SZLrW?W5Yt1V5E;E))D#VQJ~NQ1{8W`=D!XKg@xL`2@`4`feE#{F`@Q5VM3LI'
        b'm{9wjFroI*m{9u=Ce(f#Ce(gMOsIV{Ce%KR3ANvb3AK;HgenjwltM@KFxlRa+fkuT7Vt|y3KaT*8x(4HgF@{iK%s<b1Sm9*B#0dh'
        b'DAbgH0Vl==g^ua$7`$K6?gzsA#XfKhuXhLVcZmB&;^pSCX;i54(48=$TZYEs#)M{nEpTob3lq9`OiXAEHcb9~VnQq2m{9#4Frjy0'
        b'tzG{UFrlXV$J;z0CREK}ZENm~Z@tS{`q%yBvHaKJLZ29k3(X#d3+-S26L6vTL;p|3g-UP3g_`b)3w^?kqsYD;M-fu+lX0Q(KW#lq'
        b'xHA;pq0ar{C~jMi4&o^2`5gmCakus8F9#kNM`8Mza1_jH6rrtlFmpM$8g<5D*ge*xsRIv=qj=Eu=)Z!axXW799yjn)*P{1{0r?kj'
        b'p{B8Lp?6pWB9qr2@!+^n)6a|xecX);%~hMGkHUo>WN@KqlyBaG3awL4xx4i!3Zzk?bxLXsKYC|e=mXexAmV;;p>?Bhp?UOLY?_U#'
        b'bK^q2r_)Q8`a-JSjSH=F<3b@is~^UN){$K8yO9irR0R*l#)Tq->y+OCw{|ys>v4Bn=)Lm6nI1479P#XZVM3p}!``3s0r&pA@45FE'
        b'@*|B|EBHBWtupa`FrhKSn6>EJF>CR6ABO!Rjai%ev)bB!6&HFpdwcd)T<HC7UEc2=>;vFJSH-H-2N5px=~!fshV(1;C+OGv{~9jT'
        b'^xuUGy<<FcCtT>=;+f8y|6}5rd*MRw7SFtO^M7wV)AV4t(Ab}{w|+N$yf0kn<2ps|J#nFVG%nPBAGlEa-Eg6G2p3v6hzqUzX}Hk3'
        b'pNtEwqj90J^4{M>4B|rTw6o;@A}+L!#)ZB$j0>&PW<-vO3-y)vrbN)V&~edY<3j7CRGor4h&D0nhH;^F4}c4WK&B4iLhZNXLhDB3'
        b'LQ%Fs8W&nOgbPK%4pbe93;k{kTxcG`h1!h}7>&k-){Vf0+DG6*^L{p5sBH)rTEJs)p*{BmGky|tFEAs0M(0<&ssLsCSh&!<L0o9@'
        b'gWy8xqc?dxbe3h`n7GiTKMfa(+O=oX?QXjj7plJn7djgS>G$NNeU6)#8}G@>%KPG_U5R+PY&0;`?goa=LU@z0aiO*$T&RM_;6fMP'
        b'6Bk+(a~E8wjlqS^26FVuyWv9ZZd_>Hn7GjIShw;&p5}kdATD(M2wdp1td7+1-qdjS8?pfOb|mlPhp42O2f&5W!XrnW=>10GLU)bA'
        b'g?9f$T&T?+Nz>25Z^wmB*B`nK7aA~PcKXB6+<wQpD>4*|8HQcGp$ubzE#BpZhF*^z6B^2+p`pyj0ciA#jX{R?Q@lLEni0s*U3Wx='
        b'78c$O8OqrjrYDAQp*A-zG?14Uv0@Mxy6YaeP&WhoczIuqi3>dzeGgnHYM|ejmv?;xE)>lFJ{T~9h9Y#>UvLBs%^ZS;CXRrH)(t~L'
        b'N8lG3XpxP<g+2u1S@OWR&>_7G@kDx;cm1BYP($=xaG{LW6%o9=Ws64PLhJ4q7y8x%<3eq2T<8Fi7chSWF0}4n!G+p}aG^gEc}??v'
        b'A}(~u&W2p2aiIa3cg2OqMBfD$%Cu#_MC7%l-48CbZWtH3>%MTIAd2ExGheQL5kwJT?uNhFp&L@16Pltgh`idQ5xCI05xCG@gSgPg'
        b'?u-jne1Id{=WZRlMUL&~f!||bLwAkDhQ2T+Hk9E|(WgM)J+Pr4PP;QUbj=8CsLlQnk#}koHuR~xU_<9I*wDI6{|XNfT^JQ&=12G-'
        b'IFuP-(VvOD%6oxBRZQK#;G^)NHU{?CL*%U=#)s~c_14RV@u8Y&W8p*V?hhYIheM};zWc+6x;g$X&@(1JbmO!Kz=zh|3m=MXrFS89'
        b'h%uJ8Kt%a8MAVHn9>FYoJ8^#)(N?}*b{j@CaSV*;ScW3x5RsSV28br+j)4zNm?jH8cpE<SjBBLuJ5Flst%T_MRb{{+KD7Q~&=5Y<'
        b'dS#S{JoQfh>jc7wK7`Pr^$a?6nOfU9l>vtmJFg&YXjdWKl-}c3f3cqsB@Q^*P^P{LeOIU**S;~8#)#f_R(=0e`mFln=%D$5{`_$?'
        b'-1s%ApBqNHeY;Wp8vV|C1d!BJ(ts<^T+x5Z07*?WkW@eUs#9_mt<UU(P*Q#I4ZYqCB}G`!Ox8kSp&Hj#qCQWvz7Src+VO6-9lJU7'
        b'?Li!UlK3O^`M(^cF34Y{PSU9pbUr-NLzk0o*kn|P>eOL|x<d7AojO8i(F828y|X~4mg>|YE7gy9t0ms*VC`nqejk-|o|=7`dZg8&'
        b'>E;9+Makc8%oFVT3WFQXc)-!3vp;OOY*B2N3YByD<v1UBqLE6Z^9dU@Gm4`voyq_w5pMF==-QGc5mjQk2qG^GE4ucBcG1-G?c8`@'
        b'0$~~#(AU9efvU}eYgYVp7>Fh#NTazD_eE;@7ktuGffHzNT~-=?`2F3UieqW%V)QBId8loYlli{FhtR$LS52CiVm<-CeKJxr+30J~'
        b'1`Yj5W<?MuZz&5EvT2}@&W4ry@}l36G~@OsuAvV%Cv&R)Oyc1|Ve=)Dg776yi1#L*XJyRK49Z9)aoG-UhN88l9&>T#E6*D)Gv9e$'
        b'jAx{VDM&Kih7*rqo@r-y2>Xut)<&&-$G5h|fH!!E4Vq=0<%!F`=G`O><K~>vv|K4Ts?%t$o;q4!(6v~uHW?bmx3pZbSgu^Z-txNR'
        b'+IWrQ>ZO*eFnY~ahovQ^&7ipy15Yu7(9$4j96#rq4_gl!JgPF#Q6A4U<H;K}aoo(uP|RTP5S<uM-f&?U3@+O)DavB)3Lpxdtk!pY'
        b'<;Q$U(&TxXU2VD2qq%abNz>%$>A701x!PlJSgK=c4I0N_HwH<C=bYF%N8?(%&jt%4Wbt^_68hi}^e64SAw&J4`HIIy$54OWL=?&3'
        b'Vp;37@!E~JTrG;PDLa>$vM@(Vg@5vXpg^k(ML^b?uG-$TsojEB%U8tjv4ntxhy+1GVtmbE_U^5vKBNyOO2%TXW#WV>EA~nHFJtjF'
        b'BvHoxpdTZB5^$;@G+XKwp5w$Ygw>4Cp<aoIR(Q#Fgej;nDrRbFN;oGadg@|!bedN|nxxB@xQr9uqm2(LWU7ve(34n3%7UB@Noeon'
        b'&}I(W{P0$(eYD?40coF{Qc+>*z^SA+lnm#V9q95?euYz$riSyCU*ITC^zNg4E_ZOe&Pjl_qFh#^H9FY7yD!FPs*&<h`%bNn^(vSz'
        b'k?&_EN=deY@|LUpoL*RlFpL$+g&1$IJWElUl5BTi0m)dsHQnx;oLpe*^u~OXu~aK2NG`B!v+R{<y^&DIu%?oJ^8{`4JwZMFI<AED'
        b'4n!e}wL4_!2-}UQ-WyR`BYpkPsNR1@X<tCs=tJj=J+;TtcshQF>ir=~TOk`fnTBd_W=ggEN}_F}3!Mq+JrmNX&ORtfhOXa0_dcj)'
        b'HK>`(Zq6C5wiR7fWtr5TX0w{~U7!wJqEJuFkDVHGHmc__VODHs5Y`vOvQgfxl#kX%H*pH{%q5A1>O%EICFl~#*QqDQ3nf7gPb0}T'
        b'_a=12H45mXR3s;%BeQpbdKZ^f+Dq~m6_@p@)Iy!w%gMn^9bsycBQZN9(FNuXx!Oyi7A`nP8cCmg`Re*2LiNs#h380i>ABFEzqp|E'
        b'Bl#8IhK9y$xJ>$oYr~&5e;Wv_6FL2{1?NH^6Op2_Z$on<He4e;Dzp_(2TG0b%o`)U!@o6XFZd;q{${QD=_n7lO^n097QpQcHR)ZM'
        b'Cf<<=PbA^<!HL5Ca|_OGxRUT~rZy8AQK?1fL-eKEvZten1vOxLCXi`xM|||igiC3{!sEV&CzP~aYUYKsV~q#8uJ`VU0@=4VSvN;%'
        b'ongSKuo}Yw)6*3=`5Eb5^CrTiOJco5-^GTh>%CV<B-4B3!csM*k4lslOsCK}RZ^P1<WXvK6tMe*?z9nD9vwYht4CaKOgWN6%3*2C'
        b'TQcDUaasg33iGP<KyxmZ&J!&5jE<qU7V9xgy(%hi)6IsI!#VT}uR*n)zF<Gpq*Ua`)g%`rXHV}b66TbmewO8);GUiUJte16+N+`N'
        b'o^qB%kpw!y#arrig4-9ul6JDR-=L?_OC-rD)Yja*=>t_to0`+A<{GJqqB0Jxd?_KlnIOuDvWc{;e1*q9y?=YD_JRl}UIG$2;zN4p'
        b'(ZVi2;nIFI*q>OMq1DshS&dg`JPpR*6V*PEaym!bgUWPF3F%Fa(*6-$Q;$Y{EohTUE=%%)xgEhFy-6?*PAkPduNF(yf!brC^!ZHj'
        b'8N7SEO+Beq9iaV@*{_^rqypeUeE?1<Suq_U-Q%PCqMP~c9@>kjz^;H_62)KzgL_m$N)l!Ic9HZ1e%f1PCas<!2mTrf?O%rWrBO`#'
        b'm#M(+@t6K4(e6VXmL9OFeV3)RswXJa{)clKQlw6n_B8X3b&~eONVlRkqyVAX+E9j`PRdtzBD#;7pi^RK3bm(bI@+GJ{-59jKSa{='
        b'_Yx`#1)-F-lYV^a;X=w^whMPAVjca#y+20UDBo6U!g5@@h33`S;NB~dKn>7B+Xc-amz5v6+8@$xKtC58U<zb~AX>Grp@x?Ww9UhG'
        b'9?mIrMr&6vbqgQEV3Kn4jcOg`+3{|0ugTqMa+pS296F+s_LWHb+%&GtaZ_!5JNQ6VWD-}qcvQKU=&@vBN)IfG<Ebd*VELk}#3~ks'
        b'o_4$*+<Poin=?qc^Di!l*}UbHPk2f~4yf+=cosVJnSt$Mds7D^d!`E$rRbQrd7G3HfzD|?%RW$H1>urioml*VjFe?d7UYzrC<R#j'
        b'(|MbsJ8FV^UxN|w4{y`PhYm^_J@|~LXLCMin(F*Lc0zl4n_J85=!v$-&7`I1KYA(-(uNO?2}**?0geTsJBn0rMsYiSgPv#~4t1BO'
        b'r#LT?KJpuiZqU>73v?r|b{_A7w{tqH^g#M9VG<V>LrM(6X5-aKJC)cli#}CxFmbLb4O51LzH}4?_pXbajca-I%&UWY3xXjWLoOhm'
        b'Znp9}=VX@QThR%^bnZg9SW5X-6-xKUM#O@)g$a|EpwFOCUSS<hPvDG-^72eg4<V8tbAW}0xYkQY2@8%pP8k$xFP&OQa^jy3>-ZoQ'
        b'qY?K;id0eKqRpDbTvFW3Gj}ZPwbx*?1t`9v+l>EK@|ze*uH%Du!2B2dCZ+%`C$J111*+6+g9Fy?6&=}9M_I3t@)BioRMbQJuh#oY'
        b'+S%QlW?s=g?1Z&lU`a&o*uDchY+Wp9=Gp%fTWAHclAVs-%y*ePDG2Tb$Yt*ZMT5wL1=k@jfpQ7w3F`fP+XdZxsAt1W=jI7W?uGCf'
        b'F!0iIa1|P4NFllTra-kg(v(x9_f_k{YKZX*I!b%Rx#Hr59pJ1iENF)e5QVWy(`FST#N^TjQ6ypCh*|0#rrxGTizRJ$TO?sAcGTxR'
        b'6zGJzr5#PursA>=JqHU_`Zg1W4%?}~CWEQBqQfH9G{GurTxmzW$n&tZn?PjOVU1QpZ@u5Rc8=x*9edbNK#go_IJ?1`{HCP;RqTWH'
        b'c&YlZ)w7r!NA7Rtm8nCPU<R$}+eT}}(^W^>+05;JHE>@?@d{743Q8p(e84fCt53-I<a9gd44-@gp8p1nOuL}L+FuU>C`SAvIkSQB'
        b'q79d`rP1N)umfn?6V$Ug26gFyqzPh!I26RNLQQfBJ!bm0YhCGq#U4uZ!n59c97Lg#PDF7Cn)T>9i71!d8pHy3I2Vf&bhY*NP62ml'
        b'`${=$0Ol!((|U~T?847>3IEun-4}#n`@nV_W_mjoc3{DQ(x(k6%W}n1jfS(ZH(a}zUC}XHVA3{NJ<aVLb4p0MOLr=|@#zL@J6ETk'
        b'WUmE9>}I!vq}caBZw-m2Z^52+HNkVd--K-I9sz0{${N)HK+)lIVEn_h)vrnpcfiw@CP`OqlDWojUcD&aIS$+P7S?d?a7V#1NlUTh'
        b';`jCb3J|MK3yW?cqylT_fOG+=Q1wCp=VBtSluFuF;`dPL(>iAitaR%A{o%JsU`R>YRhWS(qY)(Bl%mVT^l_Mx;uoHDfsHTitr0za'
        b'*ovkLMZij!dvx8-ZRW-8^yq&KTPy(m;b29Np%~w?NWx5PQ5rDVpcNY`wE8v|W}^fk79lfXk?sjh5r;y{)rAhz(>3+phplJ0s7go*'
        b'w7ndMl{`jrnV~?BFqWbXFqTHEUC#_9;Nn-jFD8IpG#w~0dzY%k#bxRwQDG+L^uUr#$nX%Jg+>A^_dg@9fPM%LmgE6JMnR~gu+ya@'
        b'uo}Pb&@A-Nz;-XG+7dT`K!XXHfwi+?YNn&}`w41BL+!E9C4uZlm|TI0;}bmORK)(+aJG|&rO2nKsEEu1RLqpB2~N+O1RJBKO(}#}'
        b'{Xmt7;N1*6K<8F!#{1vp<-|oSXUB89iLN*3-y}|mfZJUv5)<WOE8jVmH_?^!alr=19>Knyamw#q-Mn_f%+el2GG}643|PQkpKIe{'
        b'HMM@~;D~12K!`&$n;aS)rCW;ick<9$YffwfJ8#hq;&T_>Z#R>V`v>|<?6B^of~L^_O}LhtQvG_2rlPg7LZgYX7#!BOBP@q?EoR5A'
        b'GR!KTf&%0wvo&B!lfn90#JRvJmPVW9)f7jY&~nt#7&Md)$6|I^_eG$GcJ#2($MUM<EPdO|-qsK?tD(BK)$)g!+S+O(1&#L{5mvwK'
        b'IKZ7!-Q;LFY-?Q7@~4yo>?v0El$N)3l}B6pQY_83vwKiiZB5lRDOy(qD!C&?W486e^^TP4T8H&|gr&l!X>?euDV0syYY~=)6itP#'
        b'+L&_IY}34y(q@2~)dojTt+2`5V}?Ixj|kh$aOdn7!pd)^eADx(t>;im&&zPr@uTp%`P=cqQ_PplHt}g_<Fft7>OBrJ>hnLaHY{&D'
        b'bM|fFsiSBA2!9+$g-u7vz_+4UBzfv+r!}VhZJzD5_nHiZ5VJUZKiS<eDb#Vw=IBp3`=0QtuCo`>pDrQ!@Vm8>J0{YPJ|FSO(Is>='
        b'Imm}e(sFUT?!>IG3>DAl8g^73CHY6@f0SyDt=JUBcIS1{SuRyd-PhFbBj9HkPTxSk+eZJ+FkXDzX7SR#Bt<cZvFm!bptm)`+8WVn'
        b'Db~Ih0yi@QG9xktie>B!qhWg07Y5_mRG}e0E2Dw)Nt>RJMFx^{Ad=k|f$C4sFlJ28+k2A~=ml7qAe=+*0+V9QCmEY#{nc?8Ae7yW'
        b'%8F`lCP2%u8p#Sz9NPau^rRtr{$m6^FGg5j1bQm9O~dqLCRTkHX3X$8yIGhauS^T$gtHSk?lG69k^!y9d<&Z9uc-_&cxtMzB%9H0'
        b'#UgXEL06r9b&)}neYLt8Z4=ZQDm>>L6}`jB2ucr4IPBAmi;vpBam^FZ9X}IcT>%{*)K;O6Po)0w4aT(FPLbMZL?Hcb$}6tfoH?Oq'
        b'rNW4yh2G-g!X+Fu6DUX8(ul1)L20Ug7o*WqAW)<y=}*W1m&`)((em&gK-)fd(OoTwu;xNn?`fY#U6n0@wO$svE4@B!*)z*|S+P2c'
        b'ppU@1`R#(f?w)46f+a34`qpJ&#qIiBe*9WuoD;)djh#m<=aBo9Tr64dsNB>C<e}2tJfQI#m$*1T^ujQow<U*2bP`yr)fl+I2dTwt'
        b'TS5d}OFQ`*gK%3MbIozUH3SR>&J^icgK(D#7Gatfxse{4@J)>T81QCXQyskfOA?ozeu50I;d^MbDHQ_JTj_&obZ`~r;q-z&H7!@7'
        b'Ji2DVGz3D0Re1|Bx~mjT^>q50quC7CzVtN?6?tC}(2!VKl~Ex;If){foJSCY;r2f>JoAjO@*`TU$=YDVGtw_%QAHL#Lg0OA>VmZV'
        b'dSWqqHYfWr$+M}YX@;O>`G<Y-8(89_&3I7{)5P^~>$UJ!>td}BYQlKR_v}Go+mR>_l8@qs3Ve?Ako=nTnD5!OLd9`k2#wb3mMslu'
        b'RS3%{X9&cOzL+SFbB)#Q0i68eq0{79&6NU!u4l!SvuCdse4|@$h%of@T>bb{&DpD8ojDoPBSCv&*cqYb1<C1{Ij)Lv2H~8p@<)$J'
        b'pTs(SSt61X=Ak?0yU~LjSLlabp2%_(>m-sZ*NZ>?09!8nnkNaBgpZf{u?io?9a0^%yi8gu{8&22FlVi#=W0p($#CABv^i!2RsJSU'
        b'oOU6;dFIwn;I;noMwq8a>RRaLPYRZt?Yp~3`-gDPT$E>K!3i!3uOv1}NSAB2AX!0)j`J26FFqD1&>jk>H8D@X0)D+3Zru<3dQJOo'
        b'Fx*`jurOkwU}0jZaY1NTf2$3awEg|A#!!-2EGQF@1RcAAx92UL0P!vt*nYvaQP9qYeu_F=E8@@^d-wDPZeG*PZf-kz{+X+hTPDz7'
        b'cG1QR<}o>!>gHsm9`?z4OuVWzh(P-imx_gJLqT^=vijd}Ef>J7k^E+lcK!)g`L2n*`f%%}@B*i#)%ub46-4C`f!HvoDL?G{mfZPh'
        b'u;vA+z+<>_w4^Osu>aLavZc#G3QqGeaWZzsYH5}<dNlCo7%(!~V%avwoFD)9MvtnmrmO;&nF04RJ<z=?o@<-&b;@?O{Y_UCLCdB='
        b'VM+xpzgT+KER=Sl-O5^9ZLICo4f(MfhXp2fjaabZTFopz>4!f4w@>~V%9056AhKYG+;A-xeDZO-0K~iA)m7X3csL3x<q)%w-r-pb'
        b'7wIFBB^B*jk1ghq#60$F?qOe){i_ZHxi^z8oNRq8T&qSy{vz!}YTq$mB(eiSFj!@Y*RP!FmI9;LCeDI!)h$=DHCGakYK}Uxv(ffx'
        b'OLPpZRT2%F=$MukWEWcuk~u~Y|1)#aqCDQ6eUji~2F{!`jpRzAR1zHnT1*!P*@VIpgQNm@66Nv3^p7AC^8AKAuO^!B`jQbhdJlbR'
        b'NVLH##v?q@Fq?nD&sU=<&}@#8T71f-<F?I~V*KRl=mQYr5SZ@7#lWv(#NkE@t2~0gZ5xH2Rd0*(pn3JIqOcQb<N7tKcW-2HBk^WV'
        b'$Qv$;)Dg}mZ84vP?UPO+TP>{)%riMzvMt((OkDn3+?DTMlgcpLsR?M~a<3JhN+jEqLX0Hy-{Pp=y>^0YJ9RaBhvWtF?PZa;Wu*h-'
        b'B|9YBQ0X_VlA{u;J52JjyDj-UH>5!rdbHmP#h@WcrNrrSMe%2QxZ^icTvQ2B)F%SVDM|0SFzesKTI&Sb>nJpfITDr~>y`buy=w+q'
        b'LSowUVVYP;0_*L~bF7)d{w7z3aCfbNWr;38PBY$`94o;D$r{bJ1XTqKxSOepXOUr~Z*<1?gu+b4Y>tzSHM5HLx#C&2Q<4M~>64(?'
        b'Jwg6zcVcc+ZqodPgr&~W$OFDAUVSgC34C{!qLFAwYl#)wf9JBqIudv^&2tVk;~`(Umb2#xW_vahi#^*}Az!*S;)e86<+H2;gQFB='
        b'0;Tv{W<aa`dOx1Sz)D;Ifgk+W{MA9P@pp#N2|{OkGBzggS!-k1f#<_yVdJ&>upV%bVJQ0)toJ+W!g{xaNjqIyZ{$Yv`Uc#!Xj$>x'
        b'q}f6>q=^mSa*QCtO~OiDQzLLI1EeeyZ1TQ@D<lVW2wj)UuMO5ScKU`XqPI}x(jZxbG&(wM_p!5K!iew&9AhV2U^aoFax3W_S34P5'
        b'#uspu_N@XOvhKu<Fn-s{@`S4-j-H^5n#k9X%{cX3*hx-@Pgu0htDU`vT^^ZaIU#xb$&QxbcQ;M!SQ*y4DolHhf-$t{yri$6Y5^fx'
        b'ib?n5AlwlK>Z!039EsVBBEl-GDmaoO5@wh)wJe>D1KO+0A*5<ds^%!vQk6QWP#wHd9ilBnY}6KnNiCL&Z6v><SEu&ga7~xP(^)j='
        b'2#7cW{sfQ)ojR~l*qEbzOGdx%3UKe%vD;Zi6*wKk)BQBFp_>GjT+JEoB9rbSJxq?eIB(IAeAE)%(^uy<TubaF|J2QCXEo!{>v^@f'
        b'PaSYs9T>71ck8nn>o`PhWRsQ4d9Z2{m!CS)>WOXSTaJ3=9UX}LaIINj1cxl1qDQNY$U|$*9QZv&|K#^2TP7zFCH^=#&q6-7((<<z'
        b'#a>U8uNC3?Ak4^T1#+htHVkAxb)F>4SlI)e&1B#%a$?`f9`cnBe?Ot`<R3nqN%WmOiE=^po&4R0Gh_NrHs&`^*>#b%?@_VkcMg)Q'
        b'es@#VlV7kpUw3^t)zf0vb@Q5<L2EYL00P7Y{Y6(XNk#@G;LT*$pXuXSqA8fgQm}hf73mqDfRrikogYZM^NcI+u^-4S&cC{bW2Q4)'
        b';0ZdJe#td#*Yag_e%v#hZZ<?&!}oKB?}vOnc>mv*pRqu8dw#|zWW)Ix7s<xR&)6;dZ_Cg4y6mUtXSB-xe}2aQJ^2~qW%rYxajNWp'
        b'cYem3q5m)DXH;VwIT^uKZ)Wf^StKV@xST_9(F?_i%0w)Kl>v7$Sf##O(=u723j?O0nzwLeFlO^16ni!4l?cdhn!kX3IJM<5$EAhB'
        b'+T85laThHV@5s)fmYJ(_pV_x81}y@#LbS`@6`&uF9Zv1$G*a5V=ms>?`s(v7O<t`QO-qx+HlHw2N<M~`720vAz#hRT5r<RZ*EM=M'
        b'csvtFXX`P{oVsv+mN_}sVP-E3+C$X5#o9w07B;ZEJ<ODLAM)KMDkG>m&5;?D!LHqrAv3cJHajY0d5146Pq?H$#9U4?eJ}(DDhr=T'
        b'pPE3noGVwqtfO9*s&`BM2!*;<rQT7f-nmk}OWxtNwlE?r<D$w&?VjtYJwvZ8sh1l)8Z*0^bkuILGn@~~{wJQCdU-A$KEKdft)de+'
        b'1{9Nc;*1Sf3Y|+wq;ITNsMDnCZE}>v(IQ28aBS#{QR-I~<Av(IQmPjD1hG_(V^yj0V}H#Ha_OjAjocv$V)8Yb5=ZB2Oh9MR3y034'
        b'n?~eoM2F*cw^A<`opV(MDC>9%>u2r*i6$NON+N_DuRu3lKKflebOi1roFrD-rjz`_)Wr4X4c`~4&0@uDu1>vYIbWx)F{*#Z<WF9y'
        b't|bWtRV&`CQ`agu*g1J9=|R>;&W&t#(vSD7Jbw0xSJxiJmE{DA?tl9%&%(pBVWB#;MIXckqC(yupmR6YX#;3!P}|^Ue=pp`jg-x%'
        b'wu(ObQPlLKLV$_VepKwm^oOv)lm3Z$GL*hC4I_PtR+xxdvPS2DDNgjHAHtO@c;ZY_u!nbcy|8KDP-;RBCQe&<qG#=q&m+^<`r*z$'
        b'xpO!EnzxeLhEfxH_B06*cI{RASXzhIN?Y{$4PTQ8KScem)0Vsr<;KJNHLeE19<EKj2js&!3F}D}_5nNRIsLKo9bT$Waa)LY;6LY7'
        b'29~E!nJIp=RlQAD<XtW!R3Sp-)b`0Zk?AXoyj9eWmDH}DG~xPO)jKy9a4$m}zf`IBEaadZb*Khc5h4UuqY7z?B5wt?Lq+Xcl%_a-'
        b'BLiZ~Jql{iVvi4wf1aFN0KdpI<qE`{$U}%dX^Bpg3qzB$3TEa*U#?MYR;D2~(J34en~vc62%e3qosxBH3P;4J5h)yrEp9&fJ{X^h'
        b'o<eyXIn7*W;1G}WgFI>l9?@wo(<5hyk9VrK8H>DY!UlQ7<hi7Iq@#IMiFjmScvQimWt*<xW)UiX3yTb#4Ofyg<}1|Z#R8C2BG=VQ'
        b'na|D<wxwNy=0JDM3Y5$d9_fyQA33*@+M`#w6c&yCVXT#^-RN<)T)6&O#qpj?Ai1j$C!tQQ!V^8DYkc~yFHR_3k?gf~IPo6g8Apno'
        b'vyhT1ETt<U9;y)_WKpfchUp1xE}B#$diLZ>4|v8yh#TbB0y##iCK&;|YLt<#NRAGEp*)T?&M+5n`|UMr>&ErOB7kLLf}D+V-XT1M'
        b'EjlZ!&o&)cJu;UEN-33(a^6L8VG!bwwRQnig^5a>1+oeAr1%6c4E7GZHYYD|)7r3^;&PpOn`)_deh?uKrukk%W7L*<%c&g-Y8RTZ'
        b'SoyIV8SI`oVdCseb~1x`MK!ok0~kNL0$m!Ygeg{h%95vPNRIqdT#=fnuL7@C6UbqP1|wEb+w#A}m2&Lux6<ppfJy|EN-SkR>qF--'
        b'ZDqzd$34ao7*f2M-Jjtq6+9aNgM1$bnNAN92A7zm48(wB`59al<h?=vTy8-w0*|f^)Tf6fAS1PH<r43;p@ck$9&3ImCvuBw2_juZ'
        b'%h)2I{u&|yo%#Mn8E2iZ@+h)ns1g?{!EjNX&59)>hD%pa9-uP-*QA$j+)t#}k%JTF)G$yHdcNqiHeU;rTAFBbaApWAM(dFL6MSWm'
        b'H=T1}OL_xNY{zJl3zvA8gz%tu216LaiG1u<ns30MOW9fTh%JbQk}q)mRP61%^kKOv+>Yr>?<_Znr}kJ^VJ$}dW;AWefH7zTxfvpC'
        b'ke6fARm!GyzKo+O4sw=YbPYEnQH8WojJ$!U{58YJnlI=yA!|mC;qJ1J#!w`46%NUM`mM76ua2Rh0LlKn#sHH9V~rf59YiVdky17&'
        b'KX#d+{g)sIe`CRYW(;%+8#Do85b7u{F-*Gxs!j)c$z;JBL3`}|(ypWBBBKo1%iHDX7Sc=E1<%Lql3~h5Zb3l-=}WQ;rf*-dq5!xb'
        b'z19)=7YGaV5gar-NO!-$l`+`c#Uo@ro~^uxZ7Le)iWe;BDkno+Q<QEWKR7?}Y`t5~q%cQPZw7Ol9yWs>r>fAK#@q@=U~avo)DAgq'
        b'pWHCoo?u}_R08hKA>vKLg@wa#VRw0VVJY=WIC~y0nHCf7qdYj4-V&Q{*IT%Us2<V{eZ?3wgWlF)!({V-ijmmgvFRo%2K6?2w9Erz'
        b'_}D${{k4JrDLj?VXYx=n`b#ilAxDknE<=&DN{asRKW8kdbRH_VeAAjp%Xc9&0Hr%?DKm~{HlxHvf4hx-(7?oaH~ma5(Gm2=-iv<Q'
        b'DEcF4`tK%JBjtNBq5S5?zt88|dj}YwtL*!keJ;^<e?FIJ8QbR)WBFXoEk4&Ww$C*_xX;~uC!gzs=}Ye6uihRg48VwA|2#gopx}zL'
        b'_@4d>s9Zd(v$u``eD2J<k0GRG0DLYH^>dA3m2<{@_*{MDkgmENE@;X<{O#U>|89Rv@<1u&uezemUJ(709DO#9BL2L!^g!IospQ{X'
        b'F+)tl<5)YamM{+Bq2kQQcz?#d;{EgPc)yg6_a7-^GxqZC;eIJwPSudX$*~d`eiB!%uGuzCDnE^@QsY&YXGxwaH35O9{c!~vTl(<W'
        b';_ouHW;PmKQ6(7EQFAn6Y+!Om%+ZYdouha*ZD|siHRL@+E1r#n=x;d5Riz~=D03)hQa6Y6Y-VdqC>r3CUW@A&;?YeG8!WH$arA|>'
        b'FDQB=!%T9B`S@4{m;eJ@pI-OSNCS-W0N&mHu5;U8=id9azi~gw{_3k3>pLX7cd);D-5u<&_9w4-^#9H^kIy~VJVi@s`}?449xlVn'
        b'wIN)UCHSuPSDA1h_7?)BA^SV+cKaK55Bs}-w!c$<Hv4;DYaWtE`VtiDL2Yo+T-tW&|BvgQHh9JZ+hF2j*FE(cXzYPf+i=Q=pyD+;'
        b'T0xz#ve{K$H-4moI%!i?Xp3I<AIuoaSR;&8J8pl}t)F@nAC=##pQ<ysJOt@yY(cD7;E!9M3DlQ|$B9iw(9a@TKbd{6xKNavs%UUb'
        b'hEe)i`C=J=ou9G|qpR?s3X=nCRGpy;$`(4ObxnF1=x6z`*`?#7!LhhUL1<{A$swXqd^Buhe?)Uo-iYfVK0+klRX-V;Z=6T-Q28Q('
        b'63Nt*e97o%IW5~X86f$}lDqS?C<5uHbMY;-1&l#k_{?F#?x3HBLD_b567-X}eNSR|AdB4k>0He4vF1xAJ{ma&Hm00;_c4S#jP%nP'
        b'`G8}%gN)xkhE>GOdyavP`hUBakpa-i#7F6{LdVcu3KXAaea*imJo08#^I>dAoS7Xhf98WMBk7)TzjU|KGO@Lc?;P^IV^>%-7$B{f'
        b'DcSu##236Jen2in6)+J=TnH@`sR?9IG`(%AV1lSLF9lp%P)a0~1*40aRjG-g9-%6v*fsLkpN}?pfg^@CNk7sf+O)kodR5mmP^>zB'
        b'yJ)^|sP9}AwYNB!AX3r!Hg<G5s~|bJU`dMS48`&2f>OzfXHpcY*b2QQk3XO|-b0F*%vvIj50Jq745dtwzcY};fkH$&hJ8{_ZZC=T'
        b'1yfe&jF$g}RhatsLThzEvGP$`o)mjAk}s$BCTDs%F>JYDqi4r6lY8Hv+)T9dbn1QD4U-{`@Qk&cingVq99Uw5h{IJ;R#I%^VqN*<'
        b'&XO6dcAn~W)}lqE2N{@sa?>F)y1X_@N7-7bI!&yjn~y$lTCeSyOar#8Myg)LXH{27L|af!b>m5vQElzWo80@>P@lh;#N^w``}})o'
        b'{~)ga$fftiY(RCB{M1qvWhqFWp7of519ZV43znuNr?U!{N>;2&S)r8V{rM)WBVmYgwK<?z?p*rGs_blzN^P#X%0z~zS*p~(E7WGW'
        b'bBU4K3*l6>*@0e5K<p#pJi_D)Q_!ibKE~yW#3-)Z!cx)ADJ)oajHZw>Lqi3R&o4ZU7ZQn8gg6)YNXk~M^Qz)a$%Q#Cv}`UY^~w_o'
        b'jMSd&3daRMTp5A|j_<PtfA#IhuFLA*IUho~KTO|NOz!OR`f=R(<*d$Sp5~_d3TY?xyH@ID8?_twa9(Y<PaOb0oTu!0U(INx^P;pJ'
        b'(Ve)|sy2ZT+y081nxL5zZDRA*_VTIw&#j(ZG3k`y%W)NL#$^I1RA2FMr!Dw0LhqwCPyNXrK9H9cqoZ4@M6c(VW^{r?k%<FM8EuK3'
        b'DEZq<t<;OPyUpWBfAP^;gLzU#+mWUVTX|d0^r=lwI<?37p+?^;3LeP2K80yigYwv$MCGWlPFn_@HRZ)q+KO>xnAlvowqnvs^-D(e'
        b'ix(>H(3XAjKwhG3C7lIo1xm<b3cY|kWf<aQnd5>8cLrmD<BYc8kFB+}D1`xbo-(!m(d*>+j~;F<^;}shs4u6O#=1Q~?E2L9qJROA'
        b'xjx`w6J@i02Ha?Rz0i5drZx>`QZWrBs|uZ564h*^Oem8|Tk%Pc!ctEtS6@DPM4~0scF2T*yi<XNG?~i`KqXS&G{*&B+!=%gdgyGy'
        b'wbsf?n!Y}UzH#PBttFm?C4zeWAbot8V<54}3(YZ*nAbFMR5C3Skh=13h`!Q&K;I#8amT>J>EX>f%7l{Ww56ToD@thk+*x#(IWF=X'
        b'$P@SsXVEb!C=<wR0!L20ROUOF{z8YcwxCoYr%}!p81mKxf`<(!<w9-s69ak6#>?ph9nrHiU|wXOO)RAL=%`n+^X4xyK!ZB<E28gs'
        b'%3zG1p-e};@27$MmA2qY>-zOdPt118tHP)8NLl07*m`}Sd)!FJLs)3gd6oR(){kET(KCL6A2{}KY2y)g!x3?DdRTj=Pg7bZG*GYK'
        b'!estn8gX=M`fuD634TxtkqmTrEyktR&qz+hBMSA4auBTSYfxM<Bv{8ouHO_byXoYj+!i8l)?h{qx~+FKA=hr|sF#h@E2ENAyn@b2'
        b'z-mdnGu@6W_gzyqUSodS(eI1bl;2!KIVa6v*-76}Hm)om(ANz}saM?Rv`n19%E-Bd05b&5IeaAOPy}J{q4NxuN3c!?8Q6z|+R(S*'
        b'4)f8uq%BAIVsnk{eRS48*USmyGUptd@nSY-!(~E@>3j+F1rCFk>Cd{yiRkQA(UMgL-`zi&KC5XMXW)1mDmbbP%-~D#v35=f9~adQ'
        b'5Z^*ri8Z8|IJ+Zi+Ppj)TLqZxWqu<^Y^d;65}0nOmnu!EJD#RGuB`a;LJk>EPB34o_-vsseMa%{`@8?CJC;^X=aOinjdG9|iHE;m'
        b';Un`S4Bu6-2`(0v8p#i5!(E@DBo~9ZACgz=!dWkHqS&H$xwCoBaacE}8LyzU=?_Cw4Fu_t)znBdu#%5C%%XPUq_F>*D@$siP6(@-'
        b')~||Q>(H$2M9bsZWQOQ45jWk@%?3K+QDuYZSt8otNL;&)s1R-BM$zX?IWO=wvZN)?lDNF&8AZuPRmqCNlBabgE2Sk*NlP|JOIArs'
        b'o|BfWmzJ!NmaJ3AHtJ*><s3|Gh)%wu$p2JVva!ooe~Py)>|wI97JbCqQtTxv=ICV4#QW9zOf<@#u}U9~_aL__*jQE;xSvCth5D~u'
        b't+HoqvS&lSc8S_<I=^%&WNV;?I89NqCc{r0>zS76m%t~!aYfFL1MBb$Y&H(v&Lav-R$sRK=XuL2n`Idp-fCIiX?cl0(hg7iWE)j{'
        b'Onj!VWMiLY>4!UU<yuyLJFcIM&CMv^iNn%1KR!OP0bS08OYg|kIJkTUgD&9zOiXF!CGpD-;>sFck|{qPR~BJ&<5B5NnBK^H0$n<v'
        b'g^E6NPoTTMz~)|q|H|bUv6Y8Cak!jrOlMgF7y7l>6Nd5$xPCLwS%UolrSe$$kIvi&7s*(DqHmw2^h3H&ouv#lt6~xBd53nQPiW^K'
        b'#g+ew^;w>T0?ts3SjEFWhiWsi{6|DO%L>%v5~%hJ>Lr7ve3A!aw>*n}&4XI&(Xgk$oz>7gQN$xsSco@6Qvqy>_wdY6u`!s4^a;Mo'
        b'C!jtv6-9qWQ$Zy2FeoRE&G1j~kjvJ<MEHwiowK+q+3Mt6iK=9E)db>~yg-iA=1R_<UNylvhX;YlhdX&w3?K@60Y*+BCSX`{&-AKE'
        b'&NN;hpOwGIgMLPCagN8x$MoYcx}ttIuR2XaY;&QXqQCrIpTKiG?gjVbcskjtuG4)Tm%JunFR;8zRxRW&^ix?h*=Z8x7EsN1Ik<8v'
        b'uTQr6><hw=4VMf;-HD#cExMA`&W)}rU%iY6v_`V?V+EcwNRgssHSw$qc<^jsVK`sO=aCbj9sMPY{;x#mhEz5TE_2pS3goLwHt4@)'
        b'9ueOHV>UMPRF>raFb}w4gCR^H+!g0?;Sb4GUWEGF$|k9768LQ_*$~K8Ucl0q;=~M>O7>J7#FY`)etmx3__MLX!Vg)AGaJ|l>WXz*'
        b'54Tz!eIK&cceNdYh`q%%4_8itcwLciLuGYPHok#Pf7_@~wh~s-GXr(ZS6)h<l9#NElX9i9r_rXKloP3tg0{+5$Ym?fx)Z!N;KmPG'
        b'ixxI=QLfB87k8JH%GOA;Fk%Wi()by!1d8+W>qwwN0aQ$HU@JMd(Q9YuMdYG_DkwMuhUPbt*qOt`@}PHmy?G~cfj5it8kyYt_oP<`'
        b'#$pi`#c}?104RdsT_1++C-UnAKuO|kAcH-~U^lh3!_<zmeaJ$^5@~8NU6efV@|@DZP5IJTaR`{a!sYU)aV0^7JSqk)ZOZ9A)8%rx'
        b'G`dhK2YQ#G)lCC?k+cy<3n3`JcpUmtKvWD+i%Kh`%jMFLXnBZyn7iQu=ld>fB1l6xwtr@R-MC@i-b!o#OF*kLkfzncJs!gUU!oJm'
        b'=x#cBKqoy9V^XS;t;wDivrrHoKs2}p=^T{WTj(s>^6#Zn1+sd-bi({s2$avewp9e`p^mm9kgU*^Y%rFrcOr0O&gMW8X|fJ}voSIR'
        b'8rr4_1mz^{s*?5O46tto|9U@O$!Cw#d9>X2Z!_4x0Rkhy{;d(4jU{WKT!X)7Q=@-<00FKao$X|b+O@8#0R2@i6gco7fx2*vtg`X3'
        b'mL`o&fW2G!hvE=i`7K^N11Gj{0tLw$PBGZx1uU>iT{B33W65gE<6a_DOx}z@o$M(P;I$wZDcJtd@;Zi*8Ek?xT7I8$%@ZtV>_cI>'
        b'P2eu2^oRHn_<dzgLZGfZI98mY0Cig~N6JHsV~y0!JVx0JjIw3mpaPYZnS8`=C_Zl-(oZ+PhpGfe%Y)_a@?E~lKXB&?wEltU8+C%N'
        b'0OA|mC|lLY(fPBb{<thYYC~Cd^%dC>-1#|ruvOaNakf>cE759YsESUeg*xZxIv&!6=)X<2D$GM{LZ`@enfxfixQP7%JCbllVf%{*'
        b'`4B(Mhh{e7M98mQvjxk!FL38^^+Cv1mfJktC8IdRk1oWF?`dX)&J>pxx|wnN*haA<9&ZJ9Y)#-JQ9}G!J|;gxqvfIU!Mxu@6z2tE'
        b'9zlNqn<UWXY@*YG!GJqUp0|I^?vy<bV}7?5S3Ze^1m@Tljv2dH5J*A@-a1#)2`;wjaA2S8InSd<0vpNV*<71!S!mWIo3#O2F_vgL'
        b'E&NsswxUU+Jt0PCRb?7z@w~O6)2aapJmbNXTK~<dciY+aFW9z{=ioV%Di+|xFS!=Gq-&XNK1Ng6Dtm6jSNp{CJ7sHXyNt5uI!o3R'
        b'Cjec`LNj?r*=kRa_0>0a?tfFW-BE3&Jl{IhhL<Eh+{}me&%PzpzJ>aKK>%%c1vvi`uT5;^Tq+h$iS6d<Sy;D+5?DamWY3raF8GJF'
        b'3xGI=4Mo3n0Y$)x-2qjB$_TFJ4M$51Rq}@a?xhgTL%(@nUL>x&8aUclPzP0lMo!fPWywvaCtI|dvz!l63lxg?%i!141xA}4iN(-#'
        b';`9W*<}f(g)kT>uQPa&&LY+P+G=aj|v5rM)i;5HcGWnpu%a8&)=if9AY1pIKeq~J^BQK?F{jd{u+p~Dra=~I;k915`<JK`K=RfEp'
        b'G6FZ%fK3Yro2EcEEqyGTrU08}7P_~mYo%p45-J6fsq`Q|$P|4Re%PoD3souJB_e+0*kr4<kBZ$|ru=~;1&tvT-fXEiE}JgfP^!^f'
        b'ksZdJpF((zw2Tj0ru~JOIh*|vXHdW3AzX&>#hcHj39}Tsh3qnpQwCnW#_b~G(Gp~oYQdZpg@JZ0#)(NZ0|r&l>HibQAJ48eCV1TM'
        b'_>oeb2ThT!hFK;9+u23aTv5o<?B?tamCIJgwT){RG!R-Jx2zDbU?`NWi%1g}!;+z}WSujNjbv&erh454QL1IHm#t*&9=^yBpSMUn'
        b'Y-b<2o1G2u13SBzv9qetcD9hVvopuGvn6-1v*0=_^<&%Fk~`ShA`aNuKLjumux!IMUCBCS0X?ytLdMw6oXm(p{5iLo)xL*{ivn)K'
        b'v^Vml3y^sg>%%-y)|kRfB8m(1znmS(C8plZwifYW_EoaA%NgT(n{7o5xJol1WTtq5>Q>uYatGT=yP9F!x_C?;4EuKUO@$~9O#}M)'
        b'iro4(x=xHENw6sWHOR1nRdtHc@)BmWfiK<-HuY3DnAF35;wCVrevM!`o-2+Ad-`N()<m1NWt1^p9l#jV^VXI@OX@bG(QimXb|5>-'
        b'7*Xd<c2^cyP@q(Y>}R*fJ`=8=iCy-=z(zwIvWoP)T=M+-CT#&~)0z=*S@wK`pwHTHJ|e!=`g>@*?a=x&-4C6GRgWiXG=OKb{(gNE'
        b'5Zrdi=80YWxX-F#4*FX)p62yOYqz%Yu}(U|fcE>qgnl>BCwm^M<{i1Iq=1e!wFa=?I=B6P6707Q>^Cf~RvTq&Z<I}meS1{_W5f?0'
        b'YUAd&;RFwBCXgLJDAc9}&{?FQInknzX)B&9?3AqqBTkZF#JdqsO@0^rCqn<gZ7{PT-wgo6s}@!5R<^-}A^j@*Tqj#w<)^&)&w@7`'
        b'y7?IC({g}Hj^89cDhgudAAQIcj9oe^)P@JRO}bIG4#iUIh;RRifpm#>a-1G$K?(~@Sm1l6fohA*nSOEp;TL=#Vg}yMxBp`RsQhFR'
        b'l#_>H3O1IUu7UMx-s3mA{GG3}VOd%mOVqH&w(S|W+jjfM1H*b<GfJ=TWZSrmZ7XNKdv>dB%K+P+NypW0+je`rI&9i#z1FcK1=^GT'
        b'Zp-e}uywRb`>~~dpwi*G*S}{>J5kD}11N|WkZOPE&)D`t_Snh|svSuX3hZ9C-F|8S*>)7KkFf3ff6cbv=lGFnpGUxA3xa2p*wbtl'
        b'i)+oE5Gsqe+fp%2f@61QNo)Xw6wUm0Li@5m9c=)Q;@F8Gq#&8IJqDwcw;SDoMv$dV!bBSVCk7zQ*d0*5eKH}0Xy2RkNDklh0$U<k'
        b'h2nP)qX4U|F?wKmKmMQza&&n+C$mYuE)^5ER{go;s3(LUzx8*^s$8}XyoxwBB28Yh4!jDngN4ySJ2Jzo1Gx~%XG7%PkdU`}IC3Xa'
        b'LH5e;EPMT}1OL|89oF@g6%Q7>_u$}DBHXf9x#6-De99kjq|YNl_;4nKPx#yD_&v^_iQh%bZlI{W47+Rit^^meX4u6jN4l7nLz)oV'
        b'z+n9D{GSlNBOgP6k3rYS$2fn5xnuaEm=Q7jbNIg;!++>^uNb~4a&!#;YrJa_xF59ahWOp~`atzb$-b9yA{?{%U`$23gl#z`VXC~H'
        b'1<r&J0KdVNtmx8I@7DmKj5A?MBY*Ou+n+$4yo8&|Pz>t>TY3h3O5a#(f-T@sf`?ZH+!Ds23@!{>{00{WqRNlm%Ytt7!Eo>;pr^(N'
        b')&>8EhZGgK8uH=*vm~fmRu!lZL8&FcCiK?&nLI&5KQ_akxG%ZL&8+(z)&fhftL9^{Y+!uM{O#hSyJwUf6*h2C)_|i{ZMEO9;)-KI'
        b'XPx=iMelH8^nT!D&?aWu0{=`8&s+ug7{fyUbia@b6CPrSY4<4Ff@t|90Lqb-86GMQ7M-h6aj|{e<KSN^p}93g+I5WHcJyMjU9|L}'
        b'{dwi|#u!=}(EE6!<HuD4%NZ*>B7Q8T_nC~eoy`o~R1S7F>~=d_GuqA?2G<aku!cbUOl~_nXdK2`K#20zgO7>!qxD=AuwF;69T*QY'
        b'J#=X8@F&(t2lFT@E^1pj(!Fd3_kz|9WgO&QIC|NLnEAH2v41J!Sw_Xo@k93Q!N(lWuGA&)$MP*TWBL}(at<>31#Y9S6y4F!q{jyA'
        b'UU?}E`5BIu#R#vcwgkKkG0MyA|H$oS9vWQE+6!r6S%fxxzL`inl@_xG#I@DJKjiTu>0yKpVjbc)(vOa-vcWRt%Zct~id42HQ3~=Y'
        b'Em=d0XcSlf+K&*lMV5IkAo=-6Kzmk4uGXFW2-Ym5N6zVq#**I}t(w{zdOLY-(r!eGK;?nuCxs+c?wf%-r(j8feG^nDxRYX$ZTohj'
        b'Z;MBMjQ&r<lo{9)m2jz_isdJcx4rWRi)GdK%h2bFoGF;iqTY89*FOpu#rcW2QUVvxqIVKOm@*Ogd+0Ot&bU>!KJO@IvtfM}z9mi4'
        b'SF+yL^!&chVpRK|2TiCls8GZy&INi^vfrZrzeT>yCR=~0O=xYL*w)tiGS*tM-nwt1CC$s}gWl!J)?4c)UTPP%HQ8!0TgiIpf~-8$'
        b'w1)WJ1<%N)51al&`JD?}yL74T_2>29x@`3rtlwH~*r8gLt=R?b*z6e45-6Z6uT{;##7A38*7nJsSun{ncj2V^2|TgcJPu_*XdN_p'
        b'$lj#8?M+t`P_23gEe!MC`Ko+rgvtswaP6Y}@`FOv2^W~jRxXD20Fwq(C2QfK5k1T|<4RvvAn7>nm3J`-qE{fcl{Vcv*@pE;J0HVf'
        b'k{1i|mp-kKJ+*sgIvs$4e@;x$cVJ*IlpV<Dr_(wC>!8F${c&)mD+7O=6CbEc51%aFVH~lSuRMvB+i>DtjNb1i-Wj<M{vLXy>|!1%'
        b'PoZ;T5P3vk(C>bPIe`v3p@XCbI{vt2uf9KGU@-njr{68W6SP}PzgrkVPwZ%V(02Cd&HA*#&3fsFtSkkDX1BasC?9LDUX_J8t?0Fa'
        b'o*`GCPQMEo-2EQoT}c1rTj(A6F61ZC3v-f{dB5~7!knuyEZM;keZp1HcE3ubpF<Oa6Z7eS*-e0iA%G6roR1@CFne72V7w6&P2^(C'
        b'GyS65pP^e5Kf{%=SjtBtm23mZ6-d|mqaa-AJGu7HQPP|KKjKVEU2s1lJzhR?JARCLE+Pkp<IG$6W(2-nr$eiVSaE}GG~a4Q^UW}V'
        b'Z<Q5|{9E}}GZx=61q%bfQ!pIc{e61f;7b8LdvrX^0xHou1o%1Py@8x&YfzveJv@$PEAUAcM!2_(0(EhtW51!Ph1f4^P9t+3oUY>b'
        b'ka1xn%exCN6o4g;B4|S_w`vr!wTW?H#0q6=qNh6+#r|LR-UcqJD*qop_s#?JaM76o2?wluF9O4;HGl<}4>Ke2r0#dn!iTLEC<v|g'
        b'Ypy*mZgYo%fv{j~Wd^mKK}n!Uz)I8DfQr;`zhY(9>P9AJrG=(|Gsyfu=g#nu>2B_CcfbGN>;L!VVa_@CoX<Ju^Eu~pKIh@S@2vdX'
        b'2OjH88MH({8KMz`u4gBUAILQoPr`O(^xBXO&>x=67fz>0SWAMc=`q5Ll_m&dVG;4$5YPpQg5`qT=(WZWL83U7{es`U!Nzh73i+Ji'
        b'@^BKoHe;jLX5|h;C4p#`z*Bg^_`s8F^phi)HoHG+B-wY9qc`bVoMvw4B)kHgRd~Kwg;=LK<||f^QvVT~@iZ&AqvpUmHiKXV$!rFy'
        b'7l6@|_Eq1VO4Iu^*EorXeFCdJV^yo{pfLMonoGdtuN1_5wEQcI^kW9)3rO)|RK8|eZr81iWaNA2GD{~deNmLA!tKi}0lzqn<u{Qt'
        b'pMe087S~Ep>e>kbi>FQw=$)`QSX|XBshJwW{Q(y^de_2ijj-G)#s<gfIjN`REF?a0f7R)nlu0O|fY!fG(=~Lh>s$!vhCn>1gT;l9'
        b'LN>@#Kegt5F@&i*Oja7g_K$U@wbo#rZf!`t(0;N?Gow}5NY<Y9zB-GiI)M%5zncP8xEEKUhCzyEx>gtvx5HZ;hLA=mXJdqmjYtz5'
        b'#>NEmd446Hh`@s{c+j+P^Q@{pO8$;V!X{~$wO&{nTr5U^=aNU);juCexXe1Dl~5?@yvyQIyie}7Nj%ojK|$>|KJ3<i9nMh7q@Uvq'
        b'87Gb54CyCb1!w4kN&jm&L-mvXd7Pn5lm364q5peuhHjknOK^sQC;i`zGc*wV|3#c319X%|vQ^NvtTeb$0>$g!qicV6&f)}3NtOot'
        b'bexFI*=%7p<4eCen?}KR%B`A$EF)@^MBaOjITvJO9MO&dmf5UPfn~v*4T^(^4Km1Q)mU;Iu)buz8J8%I&2hBU=;GQHdv?}1iQbpR'
        b'7RJG9c-<e$>tRg@_qQM(&&L5Xc0#UDlb%&0Xki@q%IQ6qUi}sdxbh=g9|iFr+0q%?6*Wx7p4SU6=DEa+b6!fhh%Zz@dZ#)rR7^)G'
        b'@@?~3d%(uS0=`Ij)mMCZ@ABof!x}}0v%gilMSPff@dWe7^UTH$W|Ob%JP%Qm^HOII54cQ@KnGQ_IkumH2C=S+79ZRYJL~qs3v34l'
        b'8#3l3^8iEJSZ34D@Pv%aCVgC6$P!U5W4E*`(#1yRg`|)XSfSjbBt|@W{?s!vd`T7GXZ5|{@4u&ttJizNTdo$r<OdYe=bL?qLOOhZ'
        b'*as=pxqcj^P$GsDn(KoUs=fkJsFOfzayDT+p-uQzpG_D~NEdu9JfWw@;|WCtV>}^-#}oRM+m9zC4j#i3TIl`-ctUfpz!Tau4o|3f'
        b'?RDV^Ee}}3*shL~GxKUVIhHXzp-sO8PssMafG0G!(~djL7@SabF@_V`G!9Ov^X7mWX4ABc8YlW?ctR7ek59e-eI0m0wtpL*P&LLA'
        b'+Qj1tRgcFLs`ldvZMqts(59c^32nloYZH$rwCU$~Li@+?gf{&IPiWIm@Psz~1W#zwKg1KVT?<cWCVsy#@#pvwwacy(PssM4z!REV'
        b'{LIhrglzv1+h8Vsw>I(T@7CsJ{F8V>w*Ngmp_%{WyS27!zbtmeo3+Ky`s(oa@r16{Z}|68Z@o@DA>02Rp3t@0(5tylJR#eE9#3fI'
        b'_;+g)$GyN8Ipr7Q3Elcj>pmXe;1|4G>&Fvnyf&Utw9w)ky3ogBuZewgE#1^R;h(@0vi+Ozgm^Te&eyN;PJGeN$1TMD6i>){RXm~M'
        b'jcBaeSFObrwdU#kLp-5t>ibK>|8L<b#uLi^$-D8_+dt0u+HxcMDW~~c3qNZ~{PnRpiNt%F|HoKDGsj^GC62=qiv05Wu!R1h9Il2X'
        b'^h^8pJ>rxfhW>@~?MMG4mXPf~jV09i^i}5DUxp=AY`fn1_L*zXw_{jB*PL(ve4SWAwtq90Q0I(mVhLSyzHJ_dB{VwQiq$`FLBcO&'
        b'?fA(SN=Lt7y8UP7+Ps&C|F`GbpJ568ip19b)v<)GH86V}*M}u!`ww6V-K^lTgl7A(gyvu@p&LjeZrfF{gnr&OAC^#L`SoE5*?s}m'
        b'%Rh}JG}p*fk6{VjIdK$AXt57Vs5-^OV+nmSk>A9qri9{!<kb`~wwkVqC3H>w`}+|rp{@UB{agIpFVnxpoKO4ye)Fl+t)o~I#pZv-'
        b'TIXMfBXljjm6v~=I6~K}d;f(vLf4!>R$M2JknP`wBSc>dN9fx6_gB}4BV_xx;RsC}!4cxEqrZbAG!x^+Bwhta$S{H<)cuQbgpx4+'
        b'itV~_gx<nqGmjse{GQjfaD;aFP=sJ?mhfYfZ%gshqwV;oFobOXVho{c@^kuiVhGu;4}a%hi6L~YHssOQi6LbB&teG89ETw^epvPf'
        b'Unho;?LUekG}}0T&OgQws$M*Q?k~U)s>T>Xf}l|hq0TwihavQy(vKmOJcc1;{5u#zvv^&PF@!`ILnuvwAq;pBq1?dk_CO5i!#xx@'
        b'4nZjFu8=#0HpWGT)<}_U2T@&3$t!km*dp&*N^N@Jc4B=%i8OL)HM^LH4>HBK9Tb59(jLekin%C}MM^9U72;iHS9^M3cfGHO5ApM?'
        b'rGr$}1G~tSFTD7@{a+3jRP2Wfs`kMJJ;TEVRc{vY?AMLp1yzsW1y%ESLDkp53z|EI7gRlh7gRkCFKF(y@q&&>$MAxt{sb>bJduYB'
        b'dLfX93;Jft{yk%0L5@+dpuD&du%ORx`-fmbuYFk<I06>rX!t2ski&-~Gh;X_Bkn3#L32m2g63WiRuE70FOizzEcf)QVFfL`4y+&_'
        b't-OfgtXZ1>W2_*@IIN(^8%ME%*nfl-G$ZgIV+HZ2lcB>|2d4Z4E2#Q<u!0=pu!16kN3nuJ{}EP@DDdxL1^HwgIdM2k7JMaEP<4`U'
        b'WpEtxJpX~0>ah6gWT?6^=Y_Z&d>nhKC;(DDH?vcW<&irokIp<9$YWw0-_Ti!(8r^{35jF27@3z$OO~uij$>Xh=DZa05k?Ej1repR'
        b'y&U|74=kwisV9r&c#mT|Tu_+5=@>4kR>;Ezt&jqBe!hZ6LwB_Om25shjiCko`6_5ZeBBP#qTvwr0M-jv!3tVFh|maH5TE?L+RK+i'
        b'GA{FbNG$V0myHr&6E5fZPT>`8j`Um(kquwv9RIAGKbF_yL-pp!I?#CzU<5na4=*%-1Ms4l!gqdP3B>~piMI}lYX|utk1uq3Fy-4p'
        b'tY52r_(Bpg#XMZRc@$qL2c;9smAN@2cMz9#lsK&%Wbj3;$P1T8zbi*tg2aWNRlsbKnPQ2Uyf|mJB`3)e6hKKWnW@$yTTYZEM`PWZ'
        b'n={9fqqR8A>SZ<WFSF#ZmYm2nIdfGxv?^yR_ko=M2H@-y%$)Pg+!m+#pisRR-(9=BNVf4?1QCs-dT(Ux4~6HQ#tp18Wuc^ml#Idw'
        b')iAfs5OS|zB0fwbS2o3M^9T9x-4y2<7jAJPe60>4r<NZ5{-V=MNurY|&Onv177|ew+N$t><CIxMy}Gt}5vAWobBidTv$+~3ej%5E'
        b'{pFuGr&16|<pVPQ!XUoaHj%PQEJq1eqTy+9g>wHrw_f+iH_ACN)he(`j*Bdsq_g6K!mbyoDebpWtwJ%rzeYm(e3^t2ri+cvvUGCn'
        b'TYlV1AFZ<@{Dr<e&nUg~^0Q(;J>S><_`8k#H!`z=&>UihaC36uiOnKbh}b0v{!#)en4Y<T|K>A?TqLzl6cd|H+#{f@i$u9XFlZV!'
        b'o|mF~NV8Xw_0I70PnK?!<pOhVnl_dHI^r8kHwqy<ZR$f8QcIZG!qgB_oQjMjTI~G7l&rY>*`>jFuFoZjHBJTFK^i`mXL{vXzd?p!'
        b'dFDs*)i1;zmmCbh-`^}%UNUe`@*PcC&-mheoxDDC&_K!7lUrmnWK{U!PW(N^xx$A7K|dVsd?y?NlHAVyzW1dMcm4@S<mPtPKmPLF'
        b'8{NXH+ZXO~2<tMVXC)uaq$bdfx{AN*4mHruGezb1o@NT&58OQCw6dbgLceA?PE}Xa+bwi-O~cFDnCw5rJ}`@*0<|kwZJ8l!q<r54'
        b'E_CPe-(o!O&6g=o$4+MxiI@pnL^FiPc6L%|^F-Q&&wxmiv8W<Ddxl8Au`P|*ysca&PqY$A60s1Wtg0WV?c!E%)(t;UCE~r_Ilgbh'
        b'j(nf7_G_>IJDVWSA7s$}gM#D2Rx<L`xcG0z;%iTi#Dn~7@)$!pv0gxxE|OsBX&N3|6M)u}6^|>jb`4KITH=%54SwnEE*X>Fvp4b5'
        b'D^AAJvpByngY>K=!DNaNOD|kBjWzvOtgBMqTp@=}CrVdx#k_EsMe?Ic*K_jbGWkIfC*|W}N5oa=Jt(8X{2~)Q9Ek5d{5_d1^~r4J'
        b'!c>RwG!s2H`7~4Uv5tNXOYAu1{A*G9J*Q(EC;DXeM_y)fkXfyTjvObm<CI@!a-Yl^C-O2&@yX2KlUd>UEu>Fo0oRt<X(DL?FSAK~'
        b'RIT_OZ`L1wpq>TUT_Ll))8k}g8Iw)#c$pQB#pm^oix<g{i>wlT+Xagzk^j2%$e1-Cz5c>_!R93vr#E%CJkD8`L>3P6pI`?wlM2Pk'
        b'3GsT`MaW|ax<TQrde*j|3xCi`R8718NIGd!xtS=riFMP2jOmv_5D^O=L)jbaL?I0#?nXJDuUt3DkyP(=HgA`tGhy-|0{Jt1JDTB^'
        b'mqTUEAvjr6MRT>a@RGA$XD(9|ix8)jZ{MvF;5x|!2E<p66U$2p4dI_dxX)#kQaR|-MzZ-6SxJ3#rAS^<k4Y;CwHUwjqG+Zg=M&Dh'
        b';HYp#)bz<&o5>c2s3UssBZ_5cw-S8q1dnQm{k6G-N$t)i+$sD!WstIlK^;z__8r0`bL(mMC{Ny&U6UtY%KS}i9&O^iN9>}IG7<NM'
        b'tT-5W^0{n;C#lR4*%(i1M>EVgQiqzmWmob<3_R(QZQrdJ<q7VCl*Gpo{9Rr(UGiw*CAxZN%RVmr+g)1Yk-f;W&q9%A+Xnp2Ki6K_'
        b'D^^;oaP5&fSvq_b3e_WvYnL{HdrOAodb7D%YYku1#D68)Y_8<5y_!fjs=!~;GdnE)Z%sof7ARn4D_Ihga3qvqTrzr^B43igxnwYH'
        b'f;r@J%8&#%GFrw~)?j}HrVVo}t246-ykU`lT7pR<nV+#(p82xMKgxJ{QdDyeNHnst0{%*T675u>Rw6Hoa5{sd)XFIBjc4{?v4Mp0'
        b'Y6<8bIFOfuWrfcbeKN)3+e-K@DEkB&ne3M`lw0AGCzmFxe9B*Lc=LR|+%;q6f@WzYdT%7C>3t2#wgv?i?(AyYt;DppkM)c(zO33p'
        b'mS}Ha?v`yljhK6J<7sm<yTfZ{brr0_Zzt&AqfMXS8~Ck)yr|J{L+2no=3|H?W$j$VWywrhw^ag*6KjnVnd^(3=CvUEAcDwB6Dm*`'
        b'D*Y&Hw}1(end00!V%lR!9l7rN<{;Vh&{A2`D>Rpi)dG+x#&^Z_PIm;Tg!wqG_Y4t1pb+<vo*m&mzEz6Ljm$t?BB)oZBuWyVcZN8&'
        b's*Z>}LzKJgl(pXx<z<nNe?Og#kuh;HUww5uaU<9qB8kXbhPW6RFvM47O6IF^)-n}zas|Ox*RG5p2$~Fg3<WW#rF_qadSgV8;(1U>'
        b'<|`?*ZY274$mf548`8Vn0t1=%6(JzV5N#mynRI06EO<<Tzm=2s@b?xcV_Ah5N>)4#w-=}H!RfQA#Zdh(_^jWGVATJO_s#;oKutn>'
        b'SAO68z7%t<QO>!gm}xRMes3YN;CtpBsem9XP8RwC&{iNApCLfu80H{zUJ88)st7&#F*KJsD@_SROp6rv8wB;9Uc(SjiO8e4xXqtK'
        b'_xzOi&8p4)e!8Yq#?(pqX@vPm3KabPC<pNjMZKv)?g*y;Q+7fJIAcdX;fIn;70*Omt4VqHeBZo5IwJgid^^-`J>wp+?SL+~UaF_F'
        b'^(<|&E9hH9?OoCemIfI{&klCd*`O43RvZtbSoaYf{dV9%;c*f70VdVC80y&}UBN=;E@R|IqWD*cy2W&JY#*y|o~CtPQ6D@Q&S&vF'
        b'pC3o2+=1{5ok;%;-F0JUDEh#0PnCU!>lJD9D^f@#o`+m@(&l<8Bo)sFg&}ROljf^PaT0QEkv4CWg2<6;leBp=PF)<2Ty|-5HBMcu'
        b'L#`Fl=4Wu~;u*-bRN9;+O__#1um`zbkT$;{Ju*e+Dwj4_NX1c5eucHo{7mfZ{UtF|j@*T8JKn3(+~ga4+%33Wy?cnfQUYdT*VEEw'
        b'vy}h#yvrzUHb|pX0a2{-j3p%)F$K~^vZlqlR*_hV+Bs=AC*_K8Zv4%6*CW#AHB$U8So`m#-M^P|h4@MPL(=YtrQDM|??B(V3Z%^|'
        b'r6~k*<w=_hq~pKq-mH;w_e$x%Ds+1lXGv=EE)79RsZdJRRJNhQN^d_Z=YA#qR3qBeIHh<lg3e`%fKI2?H@Tsc!y|rH7bk*z=1J+7'
        b'6uY+I-2+#K^w0;f9bMe^=N0A|%8nft=xXw=K2~{3HP93tdwz$7?cfs1CYqm9&X|awv3*wMkte)uFSOx#VZCc$x}3XNYW`k<|2|LG'
        b'?6A<Ex1lNct?%uu94Zafjg5xCG~Lz4ze5NFHddpqS@``b)K{jIcQw_uWfcxP%XY?wOOGX1+#;&HO^Q)s9U5t;9H*DFC0hr8^mcX<'
        b'+wpWo4Z%#2YBkU)X)Vp$aJ04!k$7sV(9nKeWjH3Grz&(a6$v$>MdS>@93jU@b;dRr38r{=YF&Vil@;F(c@0yf(c6*?UP<&e+8~yu'
        b'szmSvM8F8}s7VdN9}>w#Qd6Y6^A==KNi*1tcps64$^7^3h1>*bf@WGskc>McNzkY=<x=B&7L&-0;<bp?V*8DgK-Al1Y?(i&&Zy>u'
        b'QoR61<V|LaqLctNl`U{9j4~b4Dp)lwT#=1nTFHR+o8uMSrxMeBZZm5(Ep{^ll5CONw8p)f%*YN>LwXaD0g3f|7Lzyw#9b>Ef<_M!'
        b'5=^J0BAKA4nqvrT53t%1UCtrHDM{v^CA#|+TLe(mklXIc{6In{E7p;zk<<f`QcAS6#)Qpfl=Fs!d0k=>yQ5zu#R~}6XOiCMiO!qw'
        b'WC`_pK%?P~NFJzLUgO-DT@q_9YlEpQ+u4kJN15vZyTR!cQjyNP+KK}a70JCODcN|l%PC?0Bmwma6pL>oQfnrf1nwh~7cmdx*<Kt+'
        b'pd&F}QxKkiJ8vcs_abBpg(pY8$#7LlT1l>2;#0pV(a<Pvr=-Ne8&srL9N~)qC8o2QvrePJLE5T2Qh@R<3dBEpku68iYbLl?apA64'
        b'B`}*it!7w_Q)=^`q9*fNdu&&tzO3l&&?Da<*W(fxJlxa%vX0y^A1bX)HYL+t_amfE!Mur@M5c%d;CrW#pr01WA75QdcYTg$T7lX('
        b'^28r|T{g)BTKxTHrc#p1PCT;m9FyZSYqa747?0~EsWqZglfOxM$IGmc7|O9l!IVlANR2(k65KS!3e!~VH<U;avjQo!PzF;ZQLtK_'
        b'&%autQ{gly)=ld&;teQ`(6fpdA|7T(-3pyjU5wv#LOF{h(Zzwx<C2H0CZk)Aw0gapnJdvh5DT(rX2GI}qo>kk`P_d?VhD;%tqbOU'
        b'E1^`WbyOOm&1dET1JWVhuu9TnQI;hOgkWeO*K~<OCqs<7)F3bj^gF?Z5OJ}XZxMtDW*3D~TbU-QBbr!ZzJW+n3J5_(vLc;v8W`6y'
        b'NjyP1lWEsd$r6HSNX86yBcWO!v0^@q!8;}3zYk`6qnj}Sy%i>r*07jwH&`^e?rePqvk==a;79joFta7JQj1dD{vg<RqyFSEKNO*x'
        b'pJ5WZvnORJl4bJ^sE(+}Q20vL305FN4Hkw1xI<<j+O3bs0INttR2UVeV7ESK1rsj;RzsaYMocW07jTl%NvsA1nNh|Dk%*ZA@{^&E'
        b'13A+rWfs$IZe()n7H7<tAbq4v!ODPM0Z|d90NE;3>KH<=RO3nouTUt|^1GO$0juw#L9AVO82%byn(1aP1%Nu&fk2h>!8B4r#nek+'
        b'WLyl;M`}%q3_3@4A1`vN;^p8NMj<Jw5s1YIMcWrK6M(S@3!9M9cc_sNbdH{B58%&r7zw15#s)}WwBh$iqwQ0G>$FgfhzB1-lNo}y'
        b'ZUtIkMan|le_~GtP-My0^vsq3b4hF>0SgBh?<RBeEUP*C(VSNU;yO4a&}Xl1E<C@QH{)Z7Y^#EG-e9uQI+oYcbn}s^h^Di7jid&h'
        b'7uy~XZxGJM4FG+eL_if{zY3tIszEKpo(M3U2%wc}J*~yTF9Q&RC5K=cG&KV)cB4C2z`!@ncgKDnU;-}Qhx<hAX8}P5foTam&4~Rp'
        b'0Qw`k!|e}#95CkJ769oX=%ZsIwb^-U7_|B~-5eL->%T#S07kz;l@a^9fC>wYCn1Ok>I3os$$`PyU^OSink4R1L4mDg<N|E$L!wTv'
        b'7gY1edJz8;UJ%WO1rkg-X8hrcxp?XU2Ntb)-q9aLv%OyL)8Jx1+JEycGjI8{CG3a9+lWBZTcuXX>{lAJe+D-flEgy#cjmdK&-;90'
        b'`n&>$jelmzX9-WW{W0;a1THD<Z-1V3Q-X4Kci=s9e)HO<U3XmAnz%1YJu778gST&s-Z>j+&3&bz0hg^ueO~Wc7U@H0B;V;_F3kh?'
        b'j@LUe875_@$6x1py*JI>{3x={KAG?bh=cHXaJ}=qPYd)24MM&9-cf$eel@GHV%~Rwk4;_h`}%pAa}GK41DoglmR|V&!8>-%^A;i7'
        b')bx&dfp_75pUk`Ep;gn9U$1$m`tsiv&-h#8yoamT?l|AHbKWB%5yPF2ygl!|@9YkTWB)uI@Jhk+3z?r`z)X)o`k|>vZ^HG3Us$x8'
        b'ffr9B)CP5Z8kzXCdTda5!5YBX@Rh=aO~BP`V@=?J^XZR(I|pgargss7xb^TnzUziW{TXof+Wqs;Cm+B4c0==SJJ8apkUlviQU6Tl'
        b'{(0{~cpE(53~u!lp^*gg7nDd(L7LUu67(m%f0=jTcL{ncq)ogmn!OR+gW!(cD4v~tCP9A)=s3?N=+{786F68NAg_1cPAmBLgS(p+'
        b'8hdUM8n=}v=)He}9^jpb5+UErXrWOYg3xIw>xsW5=!M{a73y#X;$IsU%{~F{HgH2g;{*H)E(09QOXk;sXNQ1iM}b#&dPTEWPZH10'
        b'&qwGe)DhbKE);?Y)V5F&E}nfJTmiV>f!hl1O>kd=I|vTyIpp;cs0qrw^Z5k*i{K=nID}Kgvz=uLz;OJg1j6Pp`8uR&+m7SVoCf%}'
        b'4R{0P%;|!-g{x7v37pp}fVO+*^+7$_Aib_8LH{27W&yoNz)c5t?9U1MeGu0L?o~;mzCxO)9|AWBd6MCG_VEP$wyg<zI|san{3oXi'
        b'jaJCF6!?7_e)XFXN()WYYeb3qhXNAyT|grk^1XeF&=?45QoyDCH9>#uW2h^QvXP$5Mka9Pgf{P=9>wix@?!Ib?)%e2kain5^!j_k'
        b'j~3-ByiW(9&?Z5)85{zq02d670v8UB2B!xn1Si31`UKfWVVr*TVTj&5asRwS;N~aant;Gbwmy5ad1CtfXD+ex^nK7TARHIFerg-|'
        b'cSBp7z}10sf?KXd=>2GfW|}b%y`FIRo!92|PRC*3=v4em;J$<ZqG2o&9mHwC(fHZZ2*!m3?ZbQr_uB^1?4981z$t+4A&C1R4k0`I'
        b'o}RmZUJtmF;EsWtZlJR3vdL_Tp2{u&cUp(CPXpi90$qe@e*q=ZxKDfV#~2je0SH4MvGR2t@IK?KGo<qV5R9no3O@XU_eEd)|3G)Z'
        b'LHzGWulF7NJA{7}kQTZX(nGq1;6k5B&<{>e)F;*_=*=xKK6WPP?*w=3l>~j;YtSbiPtc!k1exwg&?j!*KkxPL6ZFZa67;$)`{zCM'
        b'U4q^T;pyNXgf`)Bt9w&4d)6+|Y$yB{faAbfkK_JZG51%WrZ)Dkofunqe#7fT;Gu*Z`I~z{|IPvB1iCW~k0CGE&@l#$!C)KaO1xk_'
        b'rD_5Ngphf5STG;O1c~oOoW+}}S(|C`7D~*?3NW%cvp0wkzO0I6o`&Ivt-F#JCot>0hIL+kGe8a2g@RU7Y8t5{=7XM43+59k58)ok'
        b'tbrUde~#5&!y~>NGCqf_&^?kv201!^gSb^*d_OM{)iA=^Zj_ln46~AHk~=fcYjfTNOBq^`k$JZlxvFvGuf1s20f<xxR?tCOsDa+%'
        b'-X5cFIpFR2P}#iPYukYi?A<M|cu}!yvJfv*kv=unT=i(hi*3|%RntVJ0&yrpnG2vB;6fA;D>Bo)raN$@fFxMQNC8$;hJsY<&2F48'
        b'xh>q08Y2ZpA+YzQFcBKO-~$UtFIZui=S3<t*jHd^Wh>n@WTbK9A_NE%<e74$Lz>OHA+nf7+#iNh>r}v41%V#{QA#Gp<5&MdtYybj'
        b'WnC5JggLnl+YIJvY#~by7;YLCz}!pXQZgqGQ*&sfMfz$Kd;rJ?83+ghI|K$$_0t|hGMbo1%`iF%^zldMLcJ%Pq;4mzaM5{z=!lUJ'
        b'2w)hvp;Uo@;5~%Xne9LG;^f0I1S~QtWy6ek7;F?U=}KbwEp9OXE2~2s*fwK^FPp%MBi+n>-pU7{@x1>xURdmz$PAx{Hf1pPdJ!!A'
        b'eEz$~`B#kjX^|EP;?{uG8o8n*Mnn^8F)SGtcq<os*&I|7BdN^vR@lw99E9z!c(C+vcSEpV8QHrw2-uvvn2#?X6!xSjGgu9|CMS!{'
        b'G07v@oW+ZCmgMGS7Isj==;<<J*X0G%^~SCG`OIR*WMLMEO+Caa%N}KO?xY`TGe6Tti7MMKWBIPon56EF9q2HVg%|cSG$bMqoNzjO'
        b'B9-dzwKoflDD1AK+mBk9B{qoEDAf*a3?)hlgba7}R4J>sL`YGP1cf~g_BGyc{_@q!>q*lDH@=R&*s^cv@%m4C9#uZ|h#(aREnp8b'
        b'rlpOa_arNO?opm__AP#YNd3JrXBqX(itn?N+fL*xUl(Z1S=y7T%rL+T#^~(Js9Z0-Cm=<R3{{sGzwd=^K`XS#fO~}D#mhKItbh(;'
        b'EI>VX_%bc9!gxG2=`XEfuorDPzwXGnJMR@_D7y^n9o*FjZIEFFJj#1|*zoM-AYug`fSBwG8}sW9=59<}cmOHYFNeg+w=Z_~sqgA('
        b'P&U-=mK|o6QjelQeUrJlEE(^lSY77l+OqFzE0rOU-fU{_l%ZoO@}<zQp1Xj3EACw;GA(1U`HnIlx(s?ofgYqpk15FFC?qD)sY&>@'
        b'4aWYCq~u}Ajq<}z?+F*8Zh{r8Rob;@v&8&-Td8#YM7*nIUXQ)9u)PZ$jgrTw{q5zDTcSclQBfhqQY0_2K{Xv1=A+ausi?SLEQGig'
        b'sD@Rk-dpw@j=R$#$&Z}cz2LGb&<%F-=CW4tp+*{*1Kh}SARix~)xZJn_RC;3BVrofnVpX0RgF>#A5b0!f_s$e<9k|n%jFGCR{8{E'
        b'`nutCc>(?`ghNaqBeR^EY<zEMS#ZcF!-ttA(2qV(1!1ed4_lh?tLn$aO6WGrdj6<9!DLl8HoR6RYZW5(fksIX*tQCOqx%GOtIw66'
        b'|1Cm};sa4w11Oo64~Gsji?=s^Rb3gBj(bt^((Sua9`ho(19Lit@2DCww{tM0Wf)%yWSKj``fqD#v*fI(eGYN5%O<Vcl<1}f5B8M6'
        b'8h6EGD3K9f2A<)?mrAQ}n9Zf;8fPD3s%;+-NOhp+Nu`cip>BBUsps+$TO9-Av^plhcPPnLn>jOEFne_s?HU-$ev^hiCNQjs#NU+r'
        b'H5Bx)6iVRNa999QAOP(n+G!e6o)3hXQ$w&u3`)h@fUs0P^77?%z+2a;A+ZcY2{!DF5TkfGVmk<Ecy6Z<#!K`JGP>>r3_UFqWDJ%+'
        b'9%kM60qS``xhe-(Mv=w+-V;pbskzcqH!gnl&z*Yy-biLt94VfQa@$S79&Oaa<T`0FgTQZTH)%Dn3YI%yMmn;8xO|dNMRvwv+>cyk'
        b'O}lB;svt3vv+x}6q0NvU$sLA*Afdt?G#~m&Fqqe%x`cfC7D)dfqz}XCqwCN3=@FebLSBfE7ZdWwb&L#_Wf3Vzr<4Vy5V@U0r*1g$'
        b'uoN$Y5!5A~B;@)2G)6v+kzhN9PDP!784c=u80tJ@q|T>e&O{KwLByo4M`4l)noksimS^2C9r=QM@uZ%f>f4LwDu*g7hj>*FYgEv&'
        b'_>hjP4$%bQ{r~ktG)Uj5g|$9YI)pcem<+~>J&L#trep|3xc&ZT$Na~pGDSl$59o*tm@f2+4F25*X6+E36=*F~fGHf(O<e&B5er#}'
        b'Q^B|j!uu5b+yly<Wxx;^s{Gy1NWBtpqRQ&5bTRuLVYbj&NAZbC?SG+Gnd{ymP^|gEq<AITO}HKy;+`DBN9lw(4}Ul3{-KikTaL8A'
        b'f*8+sc<wcz*xwAnO5GIij=gtCAA}dgFr&uaF{I#+9ic!dEuKIMMjN|qsB#JB0=-0w(=Qo<xlkXQ;qxfwXT&ZZLNncdziFKRSL6JP'
        b'{QlVVA-u{rWcWOa`!izGhVb5w&z~~RpFGZQ#ATrnY)~Mb+Z2mAMhi0Zq6`F`!9bMM-v#PEf`BDHp<rdYc&)%72r`iR7Po$@o4XaW'
        b'LqG^j8E$?{3dP<s6hx3ntfr>ot@fK^LAUE!1r<zBZG+hjW&nI3Jqe+x;Dv_Bp+x0wrAs-ak5B;F7=~joJ<Pv2Fm%+;WJNmO7h{Gz'
        b'_Yp({LHc(8vQ-(`iVQ@!@h)0+#(f5qLVyg22%nhweeUy~Ox2JsS@EzSwf6Q*#ZYSGgrzS|p>Ci=^wJHBL?M%igXD1mKDy&(;4)LT'
        b'K|c}<#R`UA4k0^tA_fh`5<|t!D3gS|H{-vxWJ)S(Cx*I-AwJ(tIA8n!c)Eu@+!XA8Sxu(YA{hJpkziyD${h6I!wSe*d=tv-_oPPZ'
        b'@u>%=<a4%px_|Ic0o+7B)avQ(@hp<vBj;&LhWsZa{Dm7ngeetAqxKe0_X*D$C&3YXz8#+Kzm4T{d&cMELwvr;DDzV&KDm9Xr~8P9'
        b'issJaN9}*|bbmCK`3F9(+S7f&!<`-@WO{?<z8;~3H^2Fln@Ugf`yMKR`*O4ld=F<}l&i-^2-FjADY>IO={=tAJ$!N8$9#CVr+c@D'
        b'JBa=MbEUuV@vnQjU-xhyjEmpL$2WPpn><|mxcCk}{#8%+s~&FexcImE_&QH_orik^`>ljsY2HUyd`A1im=Rk&>t$PbPL&c4CAVXQ'
        b'C4cg84dZCl^YNQJ-J3kzwsG-W`S>bNca?{GX<YmkK7NCzdxM9w^IX6uf%cJFV4j%k=!&;!?gjoSaEz<KzWjhmJjXHn%0}4Qsepw5'
        b'=gG8q4n3}XD*35L_XQlifwPR}G>`DPPS`S);0j0b9eEQmk9qi`w>cu;CAHfOXg$eH^XP1fInt4PDh9+vdvvTKcC}{~OW)%E{vgMC'
        b'%>02n_TS{GT;&06NvTTeN!B@XUysT6@b{a#Z}7wz==BQou4h|5<ic0(GwiA-#S98rCf`D}?GSPIc#e34m3Mo<fH9XV_Bev1$Xt<a'
        b'E~P7%dCaAT3Rns(^(Y#MiY`UlK6<|)f)LV#tc^yXD)3)|U-TJ-8p9!r!dXYx8;V1a@6tsHm1*V-C6uOc$Xu?guq(I}4}Q|r+~lC~'
        b'Wt7U<o|3m_z!DT88GpBdo8`eKWnGXAnPS}6D95)>`O?i#UUniREzqU)l<blEu3Z%C5OU4%Y%kR^(>?xWi&D#JJuuIdL{N630^er%'
        b'nm1X1C==;{1(~_z*;&>a=Wt0w5W{+6Cwd?k=rRovE%;TZ9K9T>h`rHMVI_191#qU6fW_lO4cqH(ubk}Rgr0=@Nlfrq7D*VR^6*gY'
        b'%!F~VB8DfcP=J|@Is;Iw)MME<*+;a(PCM{%7Zc#&7s*%;`>q3FS!SsarD`NO0(YN9vSSAnN;*=6LNbUR84_ReMg@_*41YaSi1K7;'
        b'hS1*!@VWR!_t+gy-<^hDw|Cqf&PFotvUjA<eCGyEYe@LR--pSYi7Xw5SPk{%DYs3FdJdcS9X)r_O@&3zAt<@K>%iWwus3H+C{Ks_'
        b'^iD>lvSNI|v~OA1+ea26Dy(g9+gr<atL1y&QkP5?IMPaG_BwpihA*pkI<ja{NTTR4kpGLjMHBe#!E*=Q)Z|ZR6O`1wcaNiM@|)8|'
        b'lr#m5A^Wl;^<YS!N!p$EmJHSaw*B6$Z;(wRbjWJ<>3ZiNd=ciza)fabmB_Jd1SfHi8`^8hMYZ!td?m)ule}SXixZ!>)z0v>6OU;s'
        b'I6-xTg+$Y9V4WBm$i0gBMyZ^}BE5bs<|w4IFp@Y%%Cbbs#tFM`0L~40%QMm=@TqW1Bmo2?J>HO~AlFJkdQeQf9|zNbS|W%VmdLy0'
        b'4XH+ywe(i1AYD{CY3y$5?w~qV?SQxI+x|N!tKgu}x(vS~Gj^w~heTW{t`8J}n|R90J&S|b|DCsyj1q{zTRR;`)K2s3jX(TUmc7H?'
        b'Jbtqa^W}*VzMS=5$rlPYBmCNY$-fF;Qa1)d`=N=oLtcwhd`w%%o)v3k$3+^;K_PTHsQ-Eye=nFr9V}sEl#smbRoaoc-%xwWyIy9`'
        b'+-G?8z)ETQ<c+^0SVl1`KYL9Z6-4E)zO87TASsEG6su6-2}%;ZVLqjbNx~QNYZ%4$jgwoVF(FHi(2?1D!D}_xGeIITcpj`{EsR1V'
        b'!;^<*&E<fzV&BcfvATf0_X!QN0#vY(tnKx7eO|{xm1PHonp{5Js9p}KfySYb11K@0=76p@1T_jeJ-~PFM)&CbX)e<3ig4Q`!jR>t'
        b'MuQ@ke(N7(@GSO5Hxur*2!yX%>jZgseLF*T%w6M@aDi@K#$D>(UN1(nk3f-G-)70YHMyu>H8LhAx|=7uE&T0ki&5B{_N~oHP!eZp'
        b'5rjtixfmB*o>V8vTkx$vu9570$2YEBBsH0mm`aPx=Cu!#Sx3dX(xR*<#932CH7>f9XmGJPX>mE}y-6pT{!2p*79uQ;Nq9T0#o05R'
        b'QtxdPapx{UH9NYAmUnv^#l7h#kFBb~&sw?(MT439?h@aKay4`6(v&{a`<S2EFVlIcCuhjS(BoJanR3bNtLK-OM)}2jaY;jRU*L%P'
        b'k#WKu!a;u@Jvh#PV4VMhF@Nl#OKD`GN4J&c4&&IKXOv}I?X%<#$E>V$(QfTAdH23c?fWme_FrnLVSH2^+B(%k9vBri?fDFAlS9#G'
        b'RpQVp2vxRS;&%$_Bvf#uy|+=oy@Ruq-w&eR>Z>{>EQZEF*=b~=>bW}$J*HZk+sPMRq%3<T(JqfqvJVB>(~e2In=Z9CUvf1-*(<nL'
        b'aFV1nDhT*l&lBAVM4!jLMq%EMASp_aGUy+liO?wHyTOgZCj<pS+-97}I=}E6n2IS;qi}h=<vt;2$FX&)rRw<JcTTnJ@Zx*+l{l_%'
        b'qtbfADu>gdthPeK3ew=u^0dN>_-9$8kSn|7QzYDfV-N5y@<*@VZ1{QE>-=SZHd1y3F8j%mvTuvrJyQ0XtCXFq35UOn3&Q!*7Z*%{'
        b';#Z9n|6e1;f9ES6bVE|+vP?=qsTT?8j3U#lBHc_nNtyNT^f*#dpmfG7sF}L^H_Q<isE)nd{_9IE&gon>CPGcEC-m|3GUb_7tP3X1'
        b'Wy<A5en?pRVw?nH6KCO6+41x}vXBFptx8J{NH3iUNoLc8A=_9hlc*|4qXM9#CTt`-OOQrb=y@&|XPkpGCI&Z(F_bi$XbX!^vT?I;'
        b'q=wkMIA&@hkxo)%%>3EsW0o+tUn<CqDM}J=zIFLbP*Qh5<Xy~dm#mrTqL^owOEj5@By-E9m<Y%a-}#BRecGkj&rxdb7EErPEM&zL'
        b'SNNqu4@cuLH~ErAlVy~<*h^1p>Z4uiOECd;vY3S4yxvxF!S-5`sJkIt4oqdW=bKm>dsdyF5x`NG>Jq~m>J!0)<rJ7uSAJsvcVQ5G'
        b'xg82hvNE>RP+*|cFJ}>y4By4l**7?!RAdbZ%a?%0IN;SVRLD9~9!2Nlw;0Ln{}$;q8|ZvR)~O3wJA=#`S|3qF(`(DutWMmZ)2+=~'
        b'@<X?0u-!B0>KklvzR8`(B^4;e$Gz=8LPU5Ctb_&zd8;KvJMp=WMyk-$kt625#&OozeK`e^tRs?iiR<*B)v)sZ7-4B}{hbdBt+92>'
        b'pc%^=DeiALWysfJ*C&I(oX_}tq~Y)&9;naMCDt4uY6=9n1AdGjb#w;fBKGHSf8kT6?8`B4RdlT|$J0qEb7U}8a0hsTze6D3+IPJL'
        b'jMb198)jXQoDQs6B<|eheL|V?g%^72cAT*DTkjLhqJW13Que^$)UTzXmn0G)MY!j3FX0sBc`&3m^S+rdl>h7v+4X5-K;)a=&buMU'
        b'Iug2M=Xvn4E>UM6|4XK1`Sf8cJR~<S*e8&`+SZ`x+H*80sx>HF@@b+t<Q_2|kWmNoC~f}nAFcAl1saJpRHN#%E3=k}%1WL1+c;S4'
        b'n$YP2ov#NJg!&@Fe-dHSOlGPEbqz||p>WpY_?m*r`yc%5_Y|3O%G(%tTvGhCmr{eDy0L#DK}{&*$FB_%4oZ8>!oois(kOd=P|)Aw'
        b'yx&OS&uM943;n$UL|}d%N0#D9>ttpfUyK#60wAJ(a&fP(o%r1@G9*u|5gFf?6p-Abm|KM&;Bg-IX;iM&gMBuobF0D{qID$R!RwFw'
        b'phO^&2%~e5j#oJ2G07yXRW#PvxIteFW2{{6AV2*y3g0$zORyhXU98ir#Yqz-jAmSJ3C=BvojQ_RQv8D#aVa>L_`F~D!mtS4BGcK6'
        b'^mRo}2R)QTmu@(7ntHBLSo=0{P{yNjq~RRhcMSU9WB}`I{$NRUAPnaDe4qKzTjL`Awp;HW!f!{oP+X1}G+&$(B@w-E5OZYZ!TMSE'
        b'84?Gn8=y96!t~5VpiL;r771NdR6vwW4oG-es1cUf{>yO7Am*^}Oot&FQtR(%+d}HAiYoMLyDk`F2K9HfEh0^+MS9cPkXmHVEOC$l'
        b'D@kU`-~$o(CTTY_*v<^PSQwDYI4Q3SNP<-nHW$+7!;pTUo@6EsQer#dFi_I<Qo5w5D)jeOLqgqSyM-1x!G;m$TBeMZpJzL6?7L;>'
        b'ss=ie+0HICw<Txq-*8rXT-u3W$_vxb70EFiMOH)?(G_dMj(4r>v$mP5iprl1d;aT?u(J{>(8`tUI6?)U&S{aO%S4X|Bo~%1{t^tg'
        b'&o$9ozczo=29w|n>4N0qR<F-apz5M`E4wcYv|ku#afw`g1Kei=Jv>}D(>GAY+DWSl--NXo5_VJFX9wE9g=FHCi(UjOyE+~VT)?jv'
        b'c_a%kM}&H(zOwLq)cZ0@g(m4?II<o1DAXRn{B3{|&@qaH8i|}Ow3=BujD6eq`_hWio#rB@toR_=D5T`2j6=zNf~#O<TJUFi>6$b!'
        b'>g`He(`I7lYaNaN`mQ!mt?N%s65zgQ4bVD%uQ6+O9+c7%Oe1s|Z4@T*8Nt1W$+VC>5hFTESeZkS^R?DeOu?=c|KR0yM5Cbg2XEnE'
        b')cc^WagD7mxfKQDUuT_yd!4U}m?9hM>c!T86_A_nca=>8l%!Q!<NWxsGUYyL^k&H+P#Mo@LZ|eFS)X$-+Xp&_@Of~>edy4ADEm7B'
        b'S38hdJMd-gfcY`qx4qo9ftAG9iH2s&z(Jx><OA1^yzI3bj%J?DsUx=EaE#kLK;2MQM#;^)HZ+;nZV#Cn5=wU42ioleEzYN0_5tp<'
        b'xNePN?vVjA6;#uU>Iu+*1(PUQ_EQ^5ssg(!2HMv{+TV*Wz~Ecs9DZPzyt{m$-3oDq(E70am6Hyg3R2K`{a*l+bHEcq@U6*3tM5bR'
        b'?*tlAbSTx$4YYHR;ib+KUZj~MXJaNEi(~E@h!L$G$y#wLXeF4+i=E!+H@@k9e4zbNNWZP~2ye$xr0aJB&1(k^l3X^fZosMuFviK='
        b'h?CUqc(ELFGK`%aT4Fm&?dc`IrR2Sulhmw8?281Std;;@ZS+Y>-HY(ksFRd75Bu`Kmr?8e2A)Qqq*g>?UnKZe<qd-`Z|X_vsou-r'
        b'!v&Q^VqYZqs%wXE4)!F~(CfiZnUf=Hd3r4<4p-VhbNawR0e7pfuHr^Pc}HI4$*_2+<AxrbHZta9vB#%(sfCohrbEJo<HVG`l%zBk'
        b'qa<8Ys`9_{nJ~a542*l{Gk$=ZIWF9bcLwl2z_6DeL$NmxbQvib)@O}^yp3Pe8TWw#6mnXg{$zet0*j0@Pv}dF&S<!Zfs6yYCH7FO'
        b'<}E_r)hcU*rI;m$jC|wktOk#sZ4;jXJxLUQ$IF44GQg6k%gFstKem6=m?X2Oe{(gnt3OH|%%}#Uv=i{(SrTUAKz;_vC<aDs*2p1m'
        b'<+6T8HsEx$ZEq1(QUf5lW@^A$V*t}~dt4AKpV}n@GbG#N!l9a^Ii_ezUynuE)S)XYg$}Y`@*G<XDgz%h?Rg6#j>_9wbi1YyFj81N'
        b'GhklIDJ?hH&rdeTR&eL~smZo9ly||)o#{6>v{_t2r)GnnZ(vb#Gy9v*_B-p^YFoaBg<yqm?ecBEe^KvWqkr8Wd%7RWt0S4-e&@C~'
        b'_!T=P(Xk4>O-aB0hBJn4veA^fqO8bVv38EUYd?3q-)zw}S!r{1QF%IZLw{^YKQAN0(SE-rUV#gN;bC4cjQzMDPtrwZ3Un7g<8fv9'
        b'Y0r0pp0mRCgZ<GjO*t-T*@hOnBi+55zy0#V{_YR^n?LODa6ZC)h*O>=yWj7J1b53i`@JLmf(o_FN8Ee;l+-G*O1cvHO`SSPw3@1s'
        b'2)ooZ^O02p%cL!ml*>NZ?&*ic&K^t;e&6!{?#91NOTUJ+!nD@~iV1;14mpRg-ivMS_pR*i=9AT93ibY+ulRqr<6lEfzecDbyJ}!!'
        b'UefRHycSZ}b-Iq^YH$SnI`J>dl3B*#NF!mKii|=@$ejdaNx@I3Rh*sgb~^l5|D8a;NLb^%pL>yisMgnP;B43nMiOq1p{$>`UT(#4'
        b'nU;PqgbPGjAyl{=On~QcWWA{Cb4YLtU#yGY$ZId^&s_y(IuVy4`S9E0;#TqOjM@{u56d>ozFgPey{^A`9kBff_b^{(L*Dk2%tQUu'
        b'l=dh4TLYo3Px{+jfPWK3)}W?+N^@6RPnWW+tC6Ipv~?*dIroU~DK%$V5Ea(+zS6{}SkcwgrG&gI$J2n{rTnju6Y)io#h-X%LYV*R'
        b'k4urj!(aIm-RmP+5Y*JE%;w3h>cYAf>w`4EjDEa`1u?IGnXv19;OV)Ge6#WAO1g5n#lBA8N;Hy@$Gorx`yAt!o%W?6#r<CDLtvX8'
        b'r^@=4x2wPOJtJTaunVEHWeBa(7};{|vB8>^sK$x7xj6B5)fC8gJMXpWs4%e*t(V$0S*6~3O(!1BEub%N>976pREV1R^5*{ToBNw1'
        b'`#W4QTre*d0+p*Gk9eUj?_cEGpYoB{_ud?%f_C9GYAb%gN&BIb?*>-v9c>pEj!Co<k^kfEIsi}J@I4U~4|@6fT7Y<H-XXk4^qP-2'
        b'Z(w5G;Pz6gk@r0m{h5mX4C8u|Ql-9uH}4IB{W%l*Gt#I@sc#aL$i&hCCnhqoeuJc6tBHPHsQF#U;lO1@FW*Y0+=|lfW5oRhzdMwy'
        b')J`o=VaR@Zs`-Qll^=-;dGe9Li&0S$t`Hag$d4Bf3nVsyuu(F-oRX()btn(#pl=v%<3%4v0dqJb(60POX3Lmh6GT0!Uan1Fv0nD}'
        b'TiJKfS+yRGfX$#Z@iA$vU}||B>lDNku!6|)HJSoyJ{Zz51>r#yned{33QDp=!yftUV)0kd)|{S;%gEhJOj(EFf7pXPZz@;qZQHBN'
        b'eRc8!(<Zn+yXbtSrRkkm=gUk}b(_g?*p^0VRN_<oeo^sRAFu2x?!AkYs>Cq?L}ZRPa|bUb?8a=OY2k<t_3decWioD0yYfA}-(Zzy'
        b'J>ebM`{dd#_9QD!rnUO{W}USybwik;^<tcpz{{lj5wrJV*Cb{S&Xt5Wqv`~+?05wuT@YV<!B>}Bx0l;_v2w@7k%dHzRIgu4g)%!X'
        b'W=%!RYdF5tk7I!MQim{5LgawAx&GooY<gZslqA|N;%>k^@3AYZH`t|JNnuv8+w0$Jjl6`omoDPtkF8L{?HfRA?Do~;EvSdsKc|Dx'
        b'K;7`GJH)+s(dG;Qe;oKraSa?2&U%rW%=_|w7}?k7p1Vj%b)_3d>KB(Rq(=4^>x>j-(W>z-?dX2<2p&U}adQ7+S(Hi`#S(m6lqE2~'
        b'<pO0)8S)}3t`oZQ;$r{ao~^?|g;BDKSBjj@wP!xJ?RdJ{27xWIGwPa-)euLWSufxIw!+ep4JJa<H2O^qSrJ38C(T%vR4AS*Fr5(@'
        b'j?`f!eC6+Ya{7}LS(21IJ-sTC6i-FrrB$JEB}q*FZv5U#xU?imOkJu9y=h8c_~fe4+rne2>_1W#Y#N2vSA|AZCEjb<_ho<D7nG{F'
        b'-)nO|TNQc%a?gf*is|1}?f%HJ@6-OYcFG7!2-%#^RN3F4&V$7Qerr|e8zo5-Y|i4U(8)GuNmc04&R!t#d{wB(=6pfi>!sp~zw}aU'
        b'N{`<T`wYWmz`_!#_^VOo3uEVdl&1X0s30{J6lX*hBS8u9r6};@2*P3nE?6KSfk$yhveU!QKjB6nZ`O~@n{s=FRT0LDhknXKm{|qj'
        b'BxbhFC)ZF*GS685GcdR;U@G9Jqv@{}r%_o$M`&1s!mOo1zVbC|tiKzLC;K%bs{kGfM$bJUUl2<QEfV1vJ)DlR3J&2B5Hoo!Ieu1X'
        b'H?s;ki!DjIv}lY+H6*eL2-FaP91#^|ZB#g{Io`(aK2=qVSXj!=N8|YEw{1uIkG%z-Vz5pkBpvlgp@)yt9hiU7p*P#DQAwiybanpZ'
        b'D0>=3+V;EOOrKmQ(bP3;<xc@RNffpG<eSSSQ7c7JPyQ8hYto_?-}L5UD#|9Mb|$DOitN1P)!2b|odft+g<t~G*fk`qZ1A~J$4C8%'
        b'ptq*`d0^@22djs5ibi;1q*RuD-ZvAk&~5){ENJ3>8ee$c-}Wnbz-~i78P_Ave^!p_>d!5<d(C$Gu~L=XT2@md+m}!+HtW`60F*g>'
        b'#r|=7WgSP$^8a30x6v^ET(-YYUYYhvT6U5Ojgm_3Dlp+4<_gOO|2dAG+%2FayCz5MQymSWREJ(|n<H_?ZD<r6a)7TQZbRGNHeI!%'
        b'$+Dqh6rYB+M1)x>H6;Z@S{p;tFD_txb&!<Rl<l<3cFPx7n;bfaEWhsTNImMnHZQ53XjiS5b(LCKN@cbcRhZZMIv+gm!fi`Xfi(&?'
        b'ET!rkId8MDYP;3KPBNFa%}TVeAr<i_N_MJs&l+GJu&|RURkam=beMG|O6YhRl)0ZDRuaYsIW|75HMR~-`La4m$p%rq6vuCote1fr'
        b'#$!Y!&e*V?te`JcHAvY|kv2IaUPoW>om;9%n@VhsZ_}ACB-BgdR3eyQKnuY%VOcEk@fPn3s_<N5Q%Ri83l$X?V5C8ssyz~$N>st8'
        b'XH}$`y>B$Vg-_3_B=Cr)FVNPu(Z!XozE`E$0z`PStV%@lWX;psXk62)>Up%<*LSZq4~&ilf4^ecU_O14KdfVks36&^^P?h^QSoYs'
        b'qXfDWCLN9VIV@h6YeL|MNsNjRU-D8v`Xl=JZ&HyO7?)3git=mjQr~%Joyt!3lqqLfE&GD;u1YDtuSg}9oWFqzJ*LI1iJ56O2S<el'
        b'L}`TiV2`Jj@{?S#Z#{%{>Zne>V%*#f62G$lTLt!@@}rK>@^4C|R#t8;g|3PmWQxaIsv5Bitg3QJQm9o0m6enRS;-_-mn4ZyWW(Z<'
        b'*ikxhbsDS8su^8`{zR9s9l;~|C{B|&mPeCzC9kbP_6Vqt2I@2Un)UewX`rTLsj76eej{O<)B7PCe)KV`z(L|+`Ac~~(`zjq`0Iew'
        b'WUwx5_#Iic;|rKf%8Dv9w9}7Kk%KJGb%pMP#57&SOx;XFpF`ObucQ)ZwV=s*ROc!jbXs+F58^<w%V|~U)94yDIQ_wNVmF&6Yx$5)'
        b'yOUaUkkIWl_XttBmJ%ez`R~rB?tCcM`G?fo^5x0;*9}xc!qi;-iw3=OW{*SJ*PyJnA+;Wrxc03q>^B$d+N=s3u7xt_(v_(}qU`(4'
        b'+4mbB2&3`G6fM>QD7BQZ%dD(@xn&=X%WT?hhB>V3DS2|Mxbtgop&J)W$wqWAwCkV{w=4v*?q)Tzrg&xCyLydrdSKH|v;Rb!$L(6T'
        b'9y(b<Qn+ra0bg#nS|vK&%)WRf66npkN}Vn^NjRc|ROO*@1;o|6)i0FGwa2V)svptgSL%C9M*$`6vP|j2D#VDw*b>`?PCrdc$J%Q?'
        b'E4NvkJ!KZ?03|kJEXAlkwmEyMZ7})EN*oF*iAn?0*phqe90^}8R$6HY4D&&LtQwt1GmNl&lcHr)3xbP9$TCU%rY6wx$ABnFK%=Nf'
        b'fSfG7`27NT{*l{;(}Y=TFZ=2a`PPv*XR!?NSv&EiUOuye&n#;dt=>+L&o9RLr~31E#c6~gEu!`042g||>NE;E1t_dxmqV8I#&9YA'
        b'=4i@9)FMM!n})kqI)pQ%7_2YM-XcNArHz6P8Tw#TaQP;=gA&B0BYgYsxcoCAeh(q6VZAi#*yWT9zI6vR#dnI)JLnzN2^Imm`<tpz'
        b'ao7e*P)wj{8!Q5X3ZmpSF7#NLcuz;%LKL=_QtKMp<Zp$9iom#^{?XmX#Uxr!r64r@=oWcdOU(k*Aw^+tC4|d94Zk^S_HZ#iBj}J4'
        b'C%U$Vymq-{`ln&1r#Z}Tw|)I8L4`f`oH)!{)={$%b)NIKN@vLV@f0p8WvnD6vKH(UHj>MU<;vx;$B9;aGe)DN3NYB5D8E3YA!5eX'
        b'Gx{hz3l;b~)z$1M2469+VB9*Ln~q!6WN_;Q?jF5cFId$S>&{-{rs-8W<kn@ob*tU9Xq7&9m2SS9Ub_nER?#V|vZLL!VAblitJ)ZM'
        b'lhTb8tFjZ^eWbewL)APrg82jUv5PFvwOcSYm2_m>S#TWQ;M1sL1bm;*K?lhsB3+5k#~zYf@1Ff5>k=e{k||oGp^g%RszkEyPfBZ$'
        b'yWZKLOurlN@>4e+I<WyyII@R+Z2MlRV--EV(=1u5@XQSGoY1P`cC@ihr|x?N4z5yZ8*q9pB*p2pZii+ef5euxSjZm`hEhQ~2c}{3'
        b'pBRP~ex-9Ld=Xu9pbv{toYOfAAF0_jO}aZ<cC<CUrO@rgdEV0SBMj!hppj!WJ_say<w-&gdiaA$RZ|6@vqe$C=WHoZrJVNiYhP&p'
        b'+gj_2*&b;AuFx2bY@f<X_H9;LLk~DK8Bp1`R#aP$!NlOK_E+Mqab;uDEq;m=nZnycKHFZpz-rq!WS3?o@twdnnW$!c&vmx*6)(hM'
        b'yXFOvjy<f^jO=Y*F(3EG$tWwe+`k^7B>k5Da0#{@@V%^L<*elOf>gU-Z`4V2_O@zUJ(LQ|dOxPto^zBSP4;1PM=+5To5Un3<8n}5'
        b'((odg>-BTbH7}EOOd@I%haZ-?TFxziV0JPMF?k8Y_sCqYol`W^7A-PCTqqHF+psg4P6!V0kx3#FV;4$wum}=}bmlwF=Ik^^-?X+$'
        b'DAMci)Hh|PDdU`Gy>o2>j<{d%%(fF1ZEF*xqKb<9E84P+&W|z{upMW5W-Ilq<v_gQ#d9`iXSE%s!i@NyQst~TpvY95>&Z|8lNyq>'
        b'R%mU8)wn~P5l@{rIu!}KC1Gr}Ri2zR(|^whQ8yo-Kux5MQDHUChq?B1c;jpC_^7vWl;QX1G7Hb)(^+AT{G2HscakKb;fZs!?oseA'
        b'6Pn|R?7I{u-<hqDkIH!jp00&hXS{Ocf#KnEnZNbXsi{FghkNjxb1YM$B(vb0@iqKl-0`m+x~blw@O5{GFXr5D&V4!5*XL05jF0X9'
        b'^||(6pF0G@z#q#kJI6mTITX(E3CEGE%*07{OHF$fPT%0bC*yTeeS<>Rz@Ldr`R9Fm6+L6mcS{fLRkV#uFKHF@H7I&~IedkLKRvD{'
        b')C6h~bvI^c0ng(_t%C5UsR;)IanyZ0k8e4bsq^s$+MjvzxlyJ~Klk-{vUmybloCKkYiU<B3X=?Zis6K6vUnCsGEi!62`1tDJ4Z%o'
        b'qk`md?+({EiN#K&tKHDzyq{Zij=$I3Jn(~S$~h{C%Q(khVrlv{&81;)!}faa@mT~VXe9RB#U=Cf_`lS|vlEX`JU9{eha4`EkD5T;'
        b'bbP|W39S<$YDGL3&qs==+o&7PijIp8idzG4+FNn-W!Z7@LGf8%)Fl_E!;$rs+%)_<=-O9#T(n-)_vwbVk_{#6WeK;p?%E)<awW6g'
        b'Xe78Op011w$G_qrlxT<wB8%Vkx=!~|<*h^{8s04HKGoO$b)W0&z82>>Zf+kWJWrsrGHM<5P^$pfLe3NU?PURU>$`nX0XWKatd9~b'
        b'leM&m0#lQ6k}~r=mkWgV$T~uR#leljJoja1EuEki;Ad%>{Zkc*Il$MbVEjdfe*T!=)zpVI1xN&|3PTbRIdB=YL}Ono!E1@g{>#p7'
        b'JPCMaHJB^bK2RVs!^p45-c2;=);|8AsHy4xCLKSt9WaCqf9mVms)S)Ys{w{^hP9_bnYpvC!Ae~S7d%!ZF1b|@mRxOxV#D8ECTk_2'
        b'2vAMEKU^-C0e#}twAhBe+w1fV_tgugS!3(^^w#@I1-&g^!^?g3!a6}@i#N8muU-(lt&duCUVsh;f*|=(-hufRySa~=0MXD>AM!=F'
        b';^>k!zc$$W3QzN0)9fGnv48BN@Q_Ux7&i3%<cXo;itzd?!e#z&5e}CMtIm@t&mu!{U*>&%BfXzbNY5703q-nPI@a75a6c)24(sbQ'
        b'LFT$X)BnTXy~kHo9SFldISB#6(dL3&1lyA!7!+qtg4IOZw@E|<FEdCBMW>w?P$>2?qt>amlWB8;%0X#=0qvMjJ3XPL0+kBUws>Kh'
        b'po0iO6F|j|cBn0Ht=dYft!UMJd+&3?#dc=i`M&SZ=lKJ&_g;IgwQuXPFY8Pz%_Tke&}GfJmC`pH8eA_bNFKW`eoJet@e79<a&w18'
        b'bDK5}96x>USAyxrzdv+jR?%gjJCy$1@o`-?_0?I&u65bsL&r`RHLpD`_}#yY7yn(X@#8_#$;LB}jry`f&Hv{};ra2P7ZA;!pP!Td'
        b'Ot`mK&OX#QJKCn<>B|OlKRk-Kao4NI<bKAmnu`vla(g0*e|Y1CgZavZKXy}xH#WW}vj27H_~qxlXL;RwmVfZb@|6<~HQoCk(cEKK'
        b'8UESVkDF{f`N$eIlMX!-9Og4((aRmp*Ei&v8HKr*d)|L&u-TED9(828ru0zbkf^Cr*pO?e6xNg+Y8-j|tje<BDvX{3RKD*}^K1Dh'
        b'0=bjrwO50hc>CuEVvWBKc3$$BL%$|={B%(BPEAg49%y_u+{@eBg2q6UO5&y<om=+i`yri$hZ4hgmvm)^eBri}G9{;t8P(e!bQM?M'
        b'H97hKWL(F^8^X88-W~{AMbq<ro6b{SUG(*X$Bb+I+N)vV`ny;2Pd>wWxre_ifAi{htB0ij_?uu!^f+YHjRR{}{$k=O@1}nhhQ8%+'
        b'*bdtCa^a?}MXlL_s%&gi_0nWlvhsyjH^vu@Ik@s?uZDLrhR1>q^{BdmT)?oywrTm&jq#Q($%&N*C$2tN`RuDz@z{!Oo%>%s_|7{k'
        b'E=vDLm|$W=;)+FQ1|{mx_P*M`_tkCLf84zH)%4j>UjHimcg0%=&wF>phMzt0YX7caaqILq2EvyGFASHBI=Nutx$lm8F!r+@ul7G0'
        b'EM30+)qzDfZw(6XM~`l2I`$`;Up}Yd6Vqa`uNEC>FH8U9{;F(2)LxuC?1H9zzv|k_&-R@5?818wUDMmWt@nNNdrQ05bkF{N(X1<4'
        b'g675Nh9ri4s%w7zNwwMTb3a&rK~3#5GrwLxq~?@oo4)_(MH}iTHW#LDElmXV&&FX_e=z+QPY1dAYRSq`&vuS__M)n5Hgx~v7u(wA'
        b'x7}IVwxRph4KprSvuJ#9`d!#Hs{eh@_Pp=e&eCVQvcFmMy?E>N*to^pe=*RsZCvWC(yQZFm)BRFIb`toWv`4SUoK3ZS#+Satnz)&'
        b'B*xxa74{mUK27?w`}6Nmr(@qNoPTAkcU%7-_xJp9f9Ko#FL`L~+W4$1W0MNweJ>SW^KxP1;r%~5y#Keqc&g^){S6nUUV7n|KR$Kw'
        b'@Y1giO(iN?Ux+O)ST^!^;djBu&iF_;fXm|HC+#i>yM<pYNWZ#2`Zj9W$X9N8Uo1DbW5KhHzq;(rYlEe~%q?wSu)p!e%MM?=?2d6Q'
        b'FBSG>x|cn$YF6|D&c@>ONA^dLK(|-MYM$Dk7<+DAQ_zr@d3!_Z`emcbM*Te2-@m_S*Z$63`@6DVTH6tCswxQ1$Lq4Oh8vfjbLWZu'
        b'JNNfIy1(<$VCg@uy)#~$efPrqPVC>lzvo}~cm6n-*}UkV<Kw2yEYBsEdw5^-<NaZCb!v6txT?v8i^~%=5AVO|{Hu#{gBzcjzvnsk'
        b'g;@VR`+I)0zjI>{&+3CK<H4S9d$}+ZUpBU^|Gxb_oA-BqH(2s7;rBLe@l5%M%<}Ty_Vi=VERSy=5`FTV9az?NV*mR6J>T8m`Hdjx'
        b'ch-J2o{cgR#MAc8qRMaX53cC8s+QKO*muWNwC)&K9`D^!*|C51s&&KDZ$5M6efW*>i5LAbYDX6oRQ~h+OCGLTP*M5yAjVi}XR>y|'
        b'$f^Y=rR&4ft*Yme+ManE3%aUeRojZvUk&%|Ijar@p(YM{XYfAt#M*cA{h1MSuJ~B<qYZOP!xMN;^RSjVrI#Oh-~KE6qi2PyX2gy>'
        b'lTNpU5e7?+{JSR`>$&Tx&Hu2!^B?x_SrB{Ygv9&Te(c>zC!f%N-Tt2I_IG}M|0l*x{PJL&D=&V!^B<n>x#;QDt2V3&4&$8<$6K?p'
        b'%?~^sv{xSNN{so@!v%?9JwJH5D_d~)!|`DA!gpC(uAf^S8+CbnbNkc5DtA8=t`dHMHgkXHUp}=u==K$y_F#BFuPq82Ju%FG<8XLz'
        b'9QOrlo?i3a*!&+R7j?b)$&#(bYdYs0-27(mPx}9Qf6reByK!6R%>4&HAMah;f9d|7i-Q@DY=3KDef;vm+24&_o{#U^l}}%G=2O@F'
        b'C^>6wa^m;j{9H-U%<P=EXk!@7hxhk<Bv|XE&U5xJ`ulkA5BtyC-*a9t<K-Zl*!uX@g_q~<4c|38m99w5KXS`B6=ZpS_`EFDQZe`)'
        b'MDmvv`TNKRmX@8HIdE>-hN<oG1DUc-Q-jIqc5?fe%8C0M8uleSN*i*m{xP{c{#WbNRW5m|p`j=_t>EZtb%W1&|I7781ZmyT{Xbvt'
        b'-DiUJ=1(j8@74=e3RcapS2t{YJejX9|J(ggS9MP;NaOefg0e4t;F--oduI89^nW~)7{2`4@#~g1j-Rpovc!(%m5I9LHHqqQG{>sW'
        b'(<{RdfYvPx*4!~78gROML)aWxKVpAVG;hku;dm7rI=gedtr4B4KDDDN?39&scceB&H$gf|qR*(>OL9jvI0?hHW`3OD^uIoHpsH+n'
        b'WqRu~om-y?65g@A;PfyHW$n3Wnh&?NABkvX;;AUEb;FaHR5lYeT61Ghue|q}#OkP;&gSADp8j62Wl?|c$a@XneWv-Pe3-#iqw9Fh'
        b'GYwyF%ym+;&va&=iK@J0@?#s;gg5unH|+~wp}Omt#F+d`3gJ2(&qN)|Nn_twdFL~UlLtGe?ZXz=zcE-ota>K@F2Ufllot|X5{1dS'
        b'rQx%`Tpir-(d4XIBYS_}m2KZ$^kCP<!t~YqqC)MwtL86k47zbMKR)WWt^amv_`ZH?+x1t5*{|MMxO?c<f{w=J1?f+Qp}#csnrYqR'
        b'=Cn8Fo|k6Iqt@*D@Y9v`)!}`e>T?rg2X7jko1ZbI`#m!*Id;bS9pT>J(evx4`r}XMJJ-2czb@%JcC!ECea)|i9q{~|{h2LQhn_Fp'
        b'^sCzsJRb&oHWSSp@z94$Hr3zW{L}Ecz<r$uf)HDySi;3yntnSY+?@~9b;VB%gU=iB@__@>vcD+^V#-G|FPuLkisXfRe;llzy{{}E'
        b'#f+}_3DMF`tCv>Y`<3MLrENi-@y+OT5BEX)yvmwqMm)4>)3o3+IP_3K{^nO0V|8`+ws7L{>Zlw{2m7x1i(!tc=VxD^|Mx@M9xCly'
        b'TsHqRVVJAKUAd%s<q7+GKDn=L@v*ZWd}?rdVRm5U?0x5)9iRTU(QCIeQmO0n%Vs2s!~en)t-WzU$5Y)MrK$SpG7e|eHO`-U%tZLt'
        b'lJKv2D+`|)an-EF1#MGHgAj@EtCjkBpBs^=Xt?tBmFMldv^Yv8D74xZmo`ifqnJ5kRXovHw=dkj8CP6B>%65w8$UI*AXOVB5bl!d'
        b'dA0Y3`I{WR!Bbr@VouP^nl<bCS+m0sm*-~Iys|e85$&cK`CdS@?u?qMeaB8$*F5)hI8hlb4F3v039GKmhlysF)$DsZKV7!?^!P1j'
        b'$9{Nv!{UqL(<jCLa8dXRN0Y9IPd_Va<yY36zb}6)G+MRtlEPyr%W8J*%}?i&3ID2&mP9#9<oX-oo`3!LJzo>fuIXM}nmRk$5#e-Q'
        b'&4OR<4SIdizsJli{#L%vQCahWebfJAApiG6dymW6l=tLp&E8w~A6akH-tBJ;#MZu15MJl=&Yw~KLe-G2ijsweqed@^zc8VAUVK|&'
        b';k@5JU%WAXU`Xt`!ot}Tg1UXuW5ZhS9f%DL2im{pn)$KO4Y4_$EpwvdGIDldeD2qaqH^fQY4dMhy7FK5wzL$r-B6m!6tpah%Drjf'
        b'vX6~e9Q^miaEIJj)_QMj{`~7(ZYZ7qsc3J6bC-nwT>Y_yg$0SBeYcb)#<twKwDX?5QM|J{3bHqpw%rg0{^GQ|+E*@qdPI1Y-gtfZ'
        b'G5b|d2g&8ry8gUd5<_2{(9+uY{Lp20hvPtmQBUieQ<fNW?I-un`s&h#Ou;paOIvb>VcK0^zxJa~kC+n%y8fCurPp5ebg*#N+-Tdb'
        b'&)ulJ^y&GzZOz@dyy5q6<mQ*}-54KSGP^1^dtzy@&$boDSA1g2)Qv@pzBdrvcuvf0`{ygSp16DX#)4-HmN#}>_UyI4T96*OH~g*F'
        b'$4+g(?7)VyEd?(w*zle3`aivGarf%qjJsj~wVB3Sp3L_tmy~aeDy!*16Y7^=3@^6UNkdw0yP$PPLG$wPE56~Ab_{KPGyLU(wv{a{'
        b'^TTTLrolRGRAPAF&1H#kEe|YhJY{bbO~XS44IQPMa&_<YyS6k|<aXw&NkbblrH!ReH$<Prhv_U1AN9{DPA8sjnHF8f;Yr&xDR#r_'
        b'f5`oj?%$JJ(zG}>qonE7((nQ5KkOb7bSa7#ePiIrdqeHzQ6;zR@Eh-WpC$i)b+kO5C~wIONmi$#a__wB6GN`KuJM~gZkSkb%Av&c'
        b'`Bz=JwQzUw#)4G~VyhMur61W7?8DZ78yVC?>k6Vzr`A``pVs~9sZq5PzT<tQE_-TsQP;M4K~46<J%6Sq8~LBrWZ&EKo|-IbPY303'
        b'b6DY5&u<IM<Df7O8X)s?jg4I4+qr(vw(LOm*z&k@?!L{h?-`tx%D%qf*L%+SP<;C3;rUs&B!8hV$=#?3FWn`Tn--Vm!-vy#l?!V2'
        b'<%8v>bLDO(F>2eR2R<DBz3y=L*-K-i8e)%hHt$UZjiOwh!Vits-PrT=o)KrwpIXoz-MEgzufMV3?C`nMx+Tf;3u<=n307&iC_2nb'
        b'*2EJvy?eq!W62d)%=+Q&K{=TUYN_av%mZO1P<><Vz1{gT`eXSr`o<`H&C)$h_r&rAYgAvXt9)=z{#MVrXls+Xi71}-nlC(+zu(iI'
        b'tNo5t0r@zhH#)292A@7vEvd`Z1%J0EU(yvUu8$W_j{RZgCqLB@FHXjOI5|GOI+hDG|EXZD?PLGkUd|OdH7oWU-O;&Osl}x=nLVka'
        b'v+Bx<zY`q$Ntd7W!^>+fDV+4cUym<8ts@+BBOE4SO}=hA@koB6>8K7EeEu9P{_)=FZw%!Bu6t_w>w|w^yl47v2lCr{%<8pkV#iG%'
        b'Dc5t8ZL6Zow_y4&^6~snRvv%sWUy=JFAS#^E~(qzmoIZNLEZ4;?4W9x9aIfV3SPW26V?ow!_N<ieoZS=5tc0@R~5$Jo|zakYx&a7'
        b'#_(imzbYvDvmH^<9~B_WuL>`z>qpF4b#HfYo&<%}ta-Vjbz4x(4+$4u)pu7};^fV>d)n46owcE0Q#crUZq=_2`S{qP5tq+uxg#uZ'
        b'?^tzDtZhzdzS_BC%Y=sSB-d^oXe|uO#(7uuWy%u6gLr<?-?DybLlDoL(rhm1Rd<dV5_HmA+QMjNpIXv-Pb}y$x7{2Sa95Q?Gh^wk'
        b'{Tt)?xQph+-&>YHG?0IHB3~9~7XR|bAyGjb7LYSXC89?<i~F7mO4^=B`unyl4GP)rBZchZZw^~_%8=IG`AoD<D(Si>=p~ot%IMa`'
        b'CDF{-%DejWrFL<qq_w&<yr(u;mfm-4S-Saq`=a7>V|-J-XOUSr^u?i>cy6V^cYey7|2@ps;UHM9vl5mB?Kf`T*B?x8{>Hw1?!wEq'
        b'eaYs3>CaCuS$S!HTkZ-Sle<!?qh3VK-2TC*Vs#6L{(M+%RjhVG>4C!kHoYxTdS7`@daXy(t2vThE}?7p9h=b5y7+PFEGch(Hr)I_'
        b'Y%Ffeb(+G;DD#Dt|I)vENZ1}&v~O!+en);GI#??|HMnCJr$_a-Oe<}<xgcMmjS4Hc#p#vd+;DpFqV|FG+<j5C7n~9KT5m=?SGDEe'
        b'pUJ(h-5w4&viZe5y%n4PdT?8YWl9o9jzU<!t=L+)X50AmnEqhS#Q6nL|MGMFYwjtGp2|;3jEk<~Ft&o=!Wn;2{yAiBPV~5bQuz8x'
        b'^`uQ3av%CmidL-Nlz+Nko$s^GI~r&6%m4RrmL4Bx>CreFW3^QUYqHVHGgpSy{`v`FCuDDXRbtHUlICBx?YRBuGtRxyq7faJmbA^d'
        b'z4^JY1#(Ac_d}&^--uF<+8s@M?)gAC@zGULhic3DBOdSWp0=sC>}WLShx4zDBH4EDkAwBIca-I$xN=qegsywP(st|8u)?~sEmIa`'
        b'zU9{Fphorf`JXKr(Ghf_+uEkJwMVO*pINvuK6FXy;EMy9g_WiKqnG?e7;w+Z^?muXAuO}1CY=7+x|Uqca^>mKMRxF|f$010ST1<$'
        b'p5UaK{@TDX?U?8@gxonF^|Pz0PYN&L>dDFEsX-B#7@l0cG<*{*)7dil$Ttk_xv;I1Ps^2XtyiCxd)Ku*ar&Q|-}%G6>HDKySF-u9'
        b'_AHO*PqC8Di~2Vo?2G0P-h_zG#?EK^2A^U_@1eBE!vQRoN7*aryt^-(|AaiM1I9da-5Y)3;@hV7O)ZPUlx_aT-g7&mXEV|1QMPGn'
        b'>D}SmR%e!Me=}b%G_3ew_nfkI@t_zVpGjr96XT;hBH;mF(b@cF%h4MwXWZVuY;Rvj+3N5X$d>xPIi>wy-&6a@$lz$t${p?c?rGs`'
        b'df^2&^W3n5|9E%;*OjD>-i^uaw|Fk8@KV_^JWT4g&gQpTHiY+mdOG`Zw>hSjUHI^c{h!&}^Vz+fpWWM)ZJt<Lu<P65rx)wHA1&>l'
        b'8Scj!Cx__=*ZH($KHZbgtq*e&r8_*I?(pNkLs|6lK)BJ<%7X3Aey1ha@Whx4&kcG-)$s@CTrscj_OkS)dsnXts+7i0hUZhJK1ihD'
        b'NJUp4jx$jk=5b~sJa;BfjgIY#vnGu^<&;C2_^zp8fUrfAsi^#1UouyqRZKrT@SbJo1j~}egX4)Dzi{R6pDYbJ+nLga+$L1y-=U6r'
        b'Wossn4PQmB>&(3~QG4~+!FnV<{>A9VRjRH#F(wR?>CC=oAB^8|Xlhw|ykSOnYFc-qBK$~sYG=?Z5BKKq6*uP}kp;n<52xx<K_f4G'
        b's1=-hi4|Sh@KdvNU--Kvv#w9y|Ky~KVd-a{oHQYx9<q0Nd3`)nzH-Ntm4$m}%_^GvT66|3nG&6clNty1wB?(6lX7!{?pwq0a~j{+'
        b'^WHhH{mGm|@14_>yTcH5((^IqCz`%LaBRTi*Q<yg@<lT$q8X*pGs;}EclMIfeB|GW4Tc)bz}KF9&z$hF;(Nk8w&%TbKG}cloZ2N*'
        b'a&5?}C1Z1MM%6rgWdD@s<{X$)mO6e;&HZ~4Gv7OJ)1KJ0KMDA~J;%;jQ$4=<zMvy8D_`A=k3xN*EuWzeL^Z|uR7dHo%X1q)J|E3D'
        b'_6!bDF&Ock@0n9^v;mq-zTWVjwsNp*6Y<<uPJd(|SGHEi=dKw(Yu2fgD*kfR(%7U47fqV_>4Pta`=YjbQsqDFX_!+GbR}keG?$Y}'
        b'4UOSFs-`8U<@Q$?=5u?lIX+AjpnCfs2J!(G@5%m|0F!U|P41pa802sF^!=G2r*A(vFsb6N?^!x&!rv{Px*`f&UO8`1(A{i1E_itq'
        b'e01?o2J&Gp3B#oROqh|y{exkqg<)p>nJ_06?-&g8p)kxfe<sYR;vWy>_utAh_Vg}{D)lM3w`P}&Eq-UP3<;KZUh?E~FGR=mjBLI|'
        b'aYn8cF*rFX=z5nQGxSLL;DYk)hX;<v^VAc)zZ+b!ba2JN6-x6fymjQbzEYb@v~tRm$>Y+kNVE>lsCZAxA4oI}F8aXqW72-EDj(O_'
        b'qj4QwHTUgtdk`*_Dtc~BRMAeV{P!msriSC1r0Q~I;-s*^i<XsFzSN&QZdrN$z2R_Rir%XScjn;9nu|ZoNAIfK^&1W9n7anTw+i#)'
        b'!aQHt^Hl%bQ)4~*`a7TMe__|*^uGS1ZS~%Yn*RQ(ZErVkUoksVK7UJT?}(sGefzfAExoDdi@LjuqW6-k%afBzPoEfsi@t3Szr+5w'
        b'{-~^Pdh~GfuGFlNo2HfC^})`b{;q6M`r$DCL}C8MelWS}(bw<XQr7cOf9FH}<1bF%A1*Hr`lQ<)dAoH=!K!=TX=w>+u4G$#X;ZeK'
        b'p(7deP&&ppWxvw0s&ea)W%rM6INUIPeM3igY<NRU+sY|J#(!g0N2=kW?oEGFwt7xb1YI$^Y2xVKef?|ud)5Xyc(rqF|G@`hGp9`c'
        b'(Bo${Kk?8dw>@`YTIq$SjOfqy_k1%5@cZC0+_q@+jHbj%v2hKtr#kzlg)hp_Y<h4_cuW54o%60poZ9yF<i(%pxZ>8EA0IYzOmT01'
        b'e<s^Tel@=0+0L)^CoWF6_U8wQnOrrwwxemywvpTR4DTqJGU5xj6;&-6eR1aE4a@HOP1yU+kCoSdYt_;56es?1py!|ZH-ElA*_7;l'
        b'q~*c;&nyWVfP>@2-9D-H-nVNXDGY!AZ0Hl`Y>99G=U7)Z(VG3rru#mBPF;Arq2-Sa<2SUNd!!B>k$EuF9qg)(?vC#96VB;~7vCD|'
        b'-q0N@3Gbf<J@HKH;`L#}WKHvH>rM`vGfTs766PK*9M=(U_SDYyrl31C>b3W$+UBR~OH;2kjDIuL(S32QDUqpoZeIWF{+^EpJ8*mF'
        b'CH-r^9oy7enHXOD(m+dUe#_F*mLTcZT9$TiT3>eShA5rd(?^f0IC+0X^OJ|(DgDupNAzFN-*Z8KSLctXzdG>Z)EyIgzu(`~-_sOC'
        b'xOe+Y1HJe3H}>~@B$(Pa{g(s3`q1NlvF+2NPrK{%1HUSJ>4n7j8GoB^?7h`;Ybt2xEdSfy7sG7d)!DWo)!vj{U%I|&=&wig*Yx+)'
        b'1ZjM6`qKlgyGn0+WZ947w|pel{6y=nw|8bX{j~e7Z$7mDwsi-dFMa0Z5&ft2_f!XgClv1*xcJ{!KmSH>j!f+DnGnpHG=2NP{xN-h'
        b'Bio)&K07AyK)6Evi2nEY_lygcR&W2;f%b~Fwvn42NIp=}J|=NS+rN}<=vejm+v~<IA0Bj>){k8`CNZ{cb+Thj5bj?}SKk#Zs~?`I'
        b'k7ga%P`WDnmAmV!Vk5#|fK3eF^g!8$hr(|)y7rtg`jt=i|E{m+wZ7m?E?zs(_Ey9A@3lSD9R*!EWyGcpsqx=v`$qTl-wixlJ-KfA'
        b'hg&~0dP`Gq4g~vRe`nuA$pal_4>YZ=3cCU8Iy1Awaa3n#Dw?+ieT~znWa7~PY|G=-70oY(zfV=s{h?%dr6vk*87!Yi?LD>ik;AL1'
        b'3)-?pqh5;jztGq7LSNUnzufs`-=dphd+vR^ucP!QQ_roRQIVK9Yg%$<#f~w{3lkNo4<+lze0*uV_^eoFSns<2r~7)I>FetJ<n-ST'
        b'yf|j)Z%*jn*VnTrnDMv8;WycRKP|1zex+|!<vS(M+&4P)PH=^%qAR>FxWbFZf2*M*l^W=tQCC;p`)L0IeLW8ZyJPPyKMmIG{dWJ4'
        b'`g(p4Oz*qpCj*;)T(<h5nNx#(SAXh*T}@|<zOX%2`<c<F-G2Ik{~Z(ziIL%cxxcgdwe~ri?n|{jRQkZ2-j`z^Xo$Vud1z|ta8v3d'
        b'rS(m{Tl>G?*Yo`#a~Ey@w}DvmBdNPeU+TEHqhn0a;8@+heC&=f&5z!;zu^<5Kl$KAQ-chAr>|#i5c<>89}G@|p}&e3PmJ~cpue-P'
        b'=Uc(tzuSKQK&;_cL1Ffl1L5}lGAO~`JyL=lh)S?;g(cWP_q?eyCX71x+fn!bF4~UE&kBp7i4S(oK4bL9Z%;J^+i}PLWIHat>!pt7'
        b'M{>FT=D8iqhu4j1ems~6_H<iU<(>D9O}!bMOsVK(YHM4$COft(o80t3Dz%||)9SJZJHj`{R@F`(-FsjE?7p7a;TgC+JrJu8&$Fq`'
        b'kDmA8prL(EaE<&`U(dzC!r$NWrGeI~N7pqa#)fCx%+8=$9$fhKO&hAha<!v#%j}>R-7z~~rhPKL;=bNH!f$BTJ{#Rtn!7jFaDVuQ'
        b'#KBDi(Fl)w9y$EtDb3pxBj$g(^wZz|(a5r@M+@gyl`eR!_q4Nz1f}1muFoGhRJ7th`aj&)b762wey{WNzKMSm`_Vb^?H`G4_*DC-'
        b'<{d4QOD|rQ%(VQdE<W^E6SfBR*TnAyk&k-o@Ycd>9=$TXuQwcRp>X4nMg0TO=@jeT-e1$#QxhG|m&5bxNBw`<*K=lgAcJx!797Q7'
        b'YvpOdG5lS__;n4L?&!ygS56r^{#(~%!ecn&?Dk2)Ia=D+QyQM5(|;1ivA+MrzMe#Qjt1q>%=(T~H~n?lt<%C6i7vSA)X|^1Gqvif'
        b'(I4+P{lMRseR@%FY@_=Y&2MDpw%wU(=_u`(+xx5Bv7K?jp&L@yTwnUd3oicJ>6zwj%TEa!2pclhW19DcKX5pv`jqBhJUcA>^OVdf'
        b'E!{;c?&&Y+>xl=MzomG~Kv3{zN~?C2p0*`^%O_$RzVXoHw=%c=>QGhbrcC!~?;p|s;*&iuJ{c5$(>D%Ok4+{=wzMXfk4<z1D=n)X'
        b'(f{)&dk#DqmUU|fs!vIr8Z6(`m3-iobz>7_viFw0v|-K8x2sR?C<z+WlTV&8w)rR7@01>zR@$;5`O>ND#|CYMQL|slln;F|eoIws'
        b')OTJwbU3^q4z*T3pLpZ`F%1JpcIKgAXBO|tj-4Ou&F8z9)Xu0HRs8a(eJ^j?T6XJ0S4UUGqz8Yn@Ql%)T2&KV5g)(fj02YjyD?FI'
        b'<HvG8&K-RMcTG^JeXRFz_y)$F&gu*L7N_PfEM2&$=;B-73U}MsV7J{G?7@y<)nl7?B*Wk2`%252%4J=nlR>q$Avsu0j=yV4Np@W-'
        b'+1tHoMcIZ-_<-i-s_N0bYx=+TWY5>03@(W23kN1ozP!GpcGZ&6)fWWi?)Zk-jLu*u9Ox~Ze8J8+x!W)6=Cs_JTt4T_!douLjrlWd'
        b'S^4m)ZHKGNqtuUl=bPA;e;$?p4u4(KqJJ8=?UB1bR9szq`i8qdbYf>)kmzUAC+rSR+qDypyqCGLaP3=z?<<Axo-KQ_XW5gTnJ2>='
        b'5U0luE*i*Ql$`k1z=rRv**Ws=`-bH1;nqI#O6tC3&`dda!@!z_MWep-ZlY*reBzY@*>88RFR!m%pBuU;_ukivbDRIT=*xreeg)Gf'
        b'uU+|0?%v|q)@&>ljn6dq#lqzBrE@cd;Sk7g53Fn2S~&6gfe)A5wPEd{flPUJUH6)W1rvXl`!iFuzI@q(1?#JFBS)tugku>c3Xk*)'
        b'R%Hvq!D(|5k0}gNcx6l1BZoJ}7yV{nV|?u&1~wKhdO3({!@Bk52VV*P*jgC=xvpvL9pUod54N4c{W1N?p6O3^P7C(OFD8zSJy#f%'
        b'GhvhK^&oHgc4-iEn2#3+!ha79q`sY8dvM^BCE+IQE}Hm*a3j97uKbD(>&rJ59{hQb+Kj4T8`hU!7;Zt3+;0Z9zmjVUkMB*42*;Ya'
        b'DlA$?tr`+W_;Ro>4$dFgJn6~QBgsWG2j-o>_GbgxIju8lCtfnpUfy<7cNE>M4c#+?Dqwv@N8w%fr-$~=dc7h1m7A88vv+);<>qg<'
        b'++5kxGCyqWObAl^W&YmZihY?2#${R;6=fEU%Pe1X%Aw4h;Qu+9iRWy2rGDb}H^Y8Geg4~{73Eb`(U?JJ|14J3Gc9pfI3ij4+}@~#'
        b'zAamue<`r>(%QzqN}m<ZPQUfUfoxgJ*G@`i3bJb&gUfk*BH5K(v-6$w8&3qwvo9BBHx||QT)MR|aZmbp;jHwlPfY$<<!_#-T~Ipt'
        b'x6Au$d(KM4yC#GYS8Xdu-w+15c<SP&mp2xyZG9^`*6}sjR}v2=Mr`Ozj}8;<%D$1f=fTYz3)4RhLr?tC8*@KBq^7uc!Hiw!UU$RU'
        b'@ychPIQOh`&i-KIvrl}eu(t7)AcwWt8yo)Wq}s+`C#Qw^tj)gCupxQ!)NR?)u1DfQZkw{Nq<4jpojk4P^<4|j-gWK=&pA7O*<(-C'
        b'JRW4Uws&OXzdcd4;DePro~YR#{Bd?w_Kjp^OVxsNDj$8KX~ER01$C8=1Od;gT5xVvc1LMd%j^a9*KIqsDI2TJKDH#ju{iy3v^zd}'
        b'<?bODb#5)5HMKka;a$O;E2fP)KX!4|4Xd8Ls4)@WSWq=BHu3Xs9rGR7#`wg)d?SDD=I`}Qf8+RZ)N2Rdn+i_(DT85y^Ds3yKRBO*'
        b'Q|@5XvFkN_w6$UCnyPGUZbd;@sa6LouK4uUA?e$nIPz}jqM2_82QxS)55Aon=H^Jg(y>I*)}ryf8w;8i3{7tiw<J;5+8A%`8Na-y'
        b'HT$jB%Stlwtp%Ae;dh9`Vwr0<fBA_-`GZ?FH7#w}bp0!5w48DKb9>g@8*6F%eRf@G<0p3o{q<O;tgY?!;QS3ox(_b9s?K5C--(`&'
        b'Cq{%Rbp<Ki8KpF4Fr~!2_axMNZuPa{upGH}lEP~(IIq&n!?jwoj~xjdJs!-x&o>yRC5m}wDs_EgNox7+b@3o@T}3!}RM4f(KUYgv'
        b'?^;z=5bVlehc4@gPkj1~!7&ojvGn?#=WIE#|AHrara#d+{fVyZ*B9*@2qWKEkiI&MyS{8nVQmm+e0-*^qP4MbYdCQG;Pawj{f=n;'
        b'4?fXT_eAH}!TOzx`Ucm(Jhy&rcK`7aM0v}vzp{PjteaYvJ#b?G<R^M2KhZfch+^Z!-hpk|@!?I*g7l0ql9^?RQ=2X;nGv7eSTJMc'
        b'_?u@p7S>lr5f$Z+dHd(1Uz!;E#EP-OKg&yke~ueFu6otbg%u6SqM=t#95Hpp!g14buQs1CZT^I9<ErLYwbl<wRdrudn3{HFLo{Z?'
        b'sHS(f=kEiA>y|aN1nZs@tUF^|^qb&kOuHmrKO}i-6t;R`d;VS3RNL=cvrDQvhb-$jA^r5upl4gVw>vQ`RlW4sI&eWO8s2M8tan4E'
        b'ATje$a0&(GU*X{O62`G3AIFQk|0Isg!j(VXx%nf#ZSAES<3AcZET~FWWlvgG|Gu7|?%w><-Fw!=Cf*cndg9EUf8V|N-*->Xje}Da'
        b'A2WV=V%TX9#9OoRL{l>QA@y)P{e_8>H?_Q;h_{>`jzrqKzOrxk>D9^AOV1p>;){v+<ig7D?g~PV3*Y-(Uzocm^I}sfRdk@`^-0xV'
        b'{zKj9Q8y0j{MN3;V;a-jb|)Un4BIoTD6ylsEH-Jz)E~~cq_ch3;(3$O5AE*Cz8o$KYQR@gTW%k}V#=`8j@xTmccy-mTo<n{ss3I5'
        b'oBQ<UAn0eppg~SQdo*ZxK++q6Wl<8rrSb6eUk{|$?*33TUHG9L(_bG*ui2eAFPt1QzV4Po1L1d;xzq9TbovK7qv7ou&TnjLENJRU'
        b'&a9kK5}cYdMs6(#PNXB>bEozu!xA<d9-_Ag2G5~_f`5uvmnTLntg5K0djB<dCl@X_Dah}_&f+smK6P?oZ@hQNDTlUY8@jRs;f1+6'
        b'N^9r~l_yn~>>g6RC%E?Z^fUx3Y^yANzGTCcbwjVXD!KT|>XPm|x~sbyZt31yuxi1m)&(PjAgd}zZL1u4W=Y%Tmaxt}@OW4bRF0fK'
        b't^1-mw@$sZxcC<XVSYXr=BK18$j^e2iQ$RzS*vbu3l3jN@8mGgmn4Fmgzxi=O5YIWrTB%)k<}$ZCaTx$9<sG4Nay*IHI=1Tocfb5'
        b'T~l>s!*$)+?{x1T8nib$_bfOm{YaSTx>1P{J09Fvd>|3#X;0-zbKiP16XdP5wYoexEy(i5;)~`)ukl<O4>}sbc|D^lb5)|~!ZBwh'
        b'#;vPO-M@5OPf@V^!qpXZWfy+5q^@dRZQbXCy<HgX?W)e9r=1*Md(*(iqUd{_*v4VGcfLDgE5H7D`i{qQN3LUK>w;nF>ET8sGEo_t'
        b'TwZg@mY}3t7oRe$wQ*E+$<~7E^62DQm)^2+#I1?3ch`k4z;EiFf9G9A&Cf2YACW#KY+bG|e4rvsw|ILr_EWBm4iDE~<W7y&?BcMr'
        b'4dQF9E(qql^5E8zun<pA8eHCyU!EBgmfJfs<s0MeV_K_E+A{pO@@B#R*|~61?6gtC)`aIrICsH2y<3OeICo>wfuXUWReED_@PF^k'
        b')uV!JZyYlH4+9O?e6085A3A)=(2v)h*l^9X-cOA`d|fvA@w$TXLo<`YaYL_pEUJ@&Q!uk7S8dEa_pQv?(Y)t}v{skpMkWa7KX~|P'
        b'zGj9qHoTFUe$AZj=umxW+Vr1A&yiZoPY80ic*n%Vu-3~8TeB@IpYB~=ur8h{t1by2_3!PisyeAHlU!aF9I+$6@30`euQ&JSvHsrP'
        b'p548jyL-DjKRfZ-f!3;m-N8;9n-~}Fmj{DlZEQ=rs4bIfJyNgb>ca=FP4A7)t@zOjF%w>fnK4@nqDuG7lI8g^ofgDOdy-w*4~DJH'
        b'KMp*%`r@9%-vlj(KMwT1lqskxC~C=+g@fq?SsW}ocNc!>Z^E(R2J&N!gyrnocL)A#IlH?sitP`BeT?Y39~NErYabpsdMpR$*8~wi'
        b'bj<vo*51vny+Lsswz|)Z9T~TD@SFI$;84}w7u9yXJL`f2lBuYjaMG4xVa;5T7?xccb^>}ctG@r%>eX#am)>)DUA(TOZfdYNb6uh$'
        b'6>QaYM-SuJung!dUbea<>=R_RL<jn4US<So&A30R5PNsd2-6zbbZVGZQ7kbsNb9C3t@a?Tw$&|dH!Xd*dR<UohHn)X1wrbrON?xo'
        b'nykO>XfEr5Y}9rZpR>B8u6%1zel!06NN>oWPp|sFPVdN$=$af0%Yku08n+#n#%)U<Ua~I!{E$q^?xIX4H$dNU>CB7Lx!}J_XF=?k'
        b'>p5ss9XC#IZ>H<}Z#}pnm{`#sZcL^mb7OSz1)H!gI(5%1>D|y;5KGl{w|0g<1aPEZxwR+=yyWOOLJMN!&QA<!_~`B9E=ZiTF21B>'
        b';iMA}6vrMuc}e;1f`yaDZVlfAD~>()lXV5z`PXN&MXx+qciqq{-`D($hN-3X*Uev06cl0e*W4aPH)-V7B|)*e<m_2LNCxYSm{uJ0'
        b'AFIZPZ**qr*41t;4w9Wz*b!77bI*EnP3O?!-$i4rm7frFad#Yu2B7-tk=8(z-yrVj+Q~G1F5bH1?L_<!)n|o8eN;!ja%-kw*1Y7$'
        b'$5duUZ7s=cng88zM+X@$j`m~Ss1>X0?n{h|CWBsEMb(6px~jup4+u(-+ORA<XZ2~-qY~q)sz&5y9*KGGOK&eJsO=m!Yi{?f3AYyq'
        b'b@$wzf4t?5W7<{U%(sa)@A{KAQP0L*n>X&d<b>dQe*L&>zbAj~x7^ft?6p65FCvxt{i^J?;Beh}`>^(=#9McUZy)5x*U4SS>DV!+'
        b'cX&<|#V#$$w{Sam<j;_X{28+5`)_TS7EIhVqw%&~D=Hdq-L)<rHe7=WW5&o}%`mDN-|6ZZA8m2(hNgn?sk6G9g0tn++oLk_m@?zT'
        b'CA}|&=k1K>ye*36gx6N;=(V-__TbVQwWKJYoqyU9m8&&>w`*%b*yIj^*Hr}T)m^tSp1%xo7u%R%W>A=XxFlDc6b%+9g;5^<@2>52'
        b'N3QKrFAiqllVJv?6xEjnnfR++O^s2{A=viX2?b5rf<Kd!uIj@7>U#YDl9zLj$;*`gyS&8z>%1Ia*T1I-3X1UCmW~Qqow?Lc&K-)N'
        b'zfxa0Wk^k8*X(=-W|oEBvncuhS=kh}xx)tcmeTQKJ0IDx`K_H(zIx}FVd3J<f7m(x(x5Gr$hV=x(Nz8??Za0e`=7TD&wK3uMf)%)'
        b'TecngVbzKKyLR^U?(FQ{*_EBU=-2N?H^t)7m@#1wI&A-?PkL<S$j8<-b@fy)Pj{?b^!8w<^3gEe)`FlqIn-XZx_wn+_yOFM;j0=8'
        b'gN9(Hq;bp6RXxefn2ws@vWp7k>Zb8ymaRIoI^Di9nQ3fUU(j-Evh(jB%VtVr>&udDzi(Te?EK7Q$>jCfj_{q)pfM4&HrJ&S<>~K+'
        b'ZNBuEcP574dTVaz!rm>}>f3u4X4f^Y5Azvx^>bs1b%x`@76zAfeR}P02euaG+LRr+td5@&WG%if%x7(s%j%Nao@9MZRaHUlh9SX8'
        b'QMx%S2Yb)0Do9Q)ipr-bzM>$$nd!B!41{+q!uW0;jISs-n}hC45bMmEAlAlz+8MM=8%N~}nx<33-pq45TMLqt#tfTOJ!XAj*x4Ol'
        b'G_!C<VRh4KBMZYmU6{`Jk<$mq-O0D<KC`puvpYK%2gl{kgL~ioZ`*W#ru=;HnDVpg_%SV`GJJQw41eEaQ5l~7lfH35!IJWotF~Wp'
        b'({+<7662QD7X)3dN$-#9!=SJA&8V+6y!V6AAnN&ZIQ^06WQ^|~vZQ2d(UPaH`DN7CD$e({KD#b{#ZB!c-M{FbpSiOAfuL=_;G`E8'
        b'jBHraePDPjIO)Gxvb%U=;Y*uWEf|@;d3)5?I_c9>Tf*Mfs>+d<4x9e-Twfu4KRGjM;iRzmDUQuuU9`1iTXuYKWENJ%((ezmke;(W'
        b'xZ<Y_zc6UEFR!l*PRf~O<0k}Di3#DwU%a)Tt|F=#b7k4Qk+rAhuKIktAS~~?vazO9M?@vw+>+wsi@dpS9Z7RWJY5hbxw3wHYc_dK'
        b'eb6-tn$v~#WmCqSQ(q8ti-HDqQFPNN?0`M@>2>iLC9S8H%^g#4v`#rIpYn{LMY-dqXe5Dm!$Ii&Bp(;OHy`H?3HwDsHkyJ>|BrB='
        b'tsMQHe6(hti>CJHa}so@8orbKPxEr>v3a@Un7jn%P4f4(*;i9lL49A_IVAr%<$roVBPct*|JeB4Tbr97c>K7rhZ5%=Ke=;oa>^ya'
        b'SyUWuN6)`J_RWGs`xi2$TZUg8zOcD&#NfBCgXM5|V`{{~;o<m+iHj2@2NSUsvx7fQUX;kam%O$j7XCb4Hnw(X6y}UX$=Z@I%o&N3'
        b'Czb@O$Ae`DPlyfvmSE!KbX(XX3c`kCI(#ksdsJ=sesIu_Nv{Ye)3-ey-TK=YKltWAbkT-mqpy7T&yEu~c)bPjO{y3Xz1%fq($x6G'
        b'uf3c8(&MYLuOu_w4Vm0ej<pYK-kCi*Ak&fcdSC0m_VJ!;AMd>O@lT8hKj**w-SlT3PgZv~RFy5RD5*JVd-!T%_|S92?Wvl^5mRH!'
        b'%UY(Eg&&+xO%A?4l>Xn32T>heX;`>Y?ZT0#9QsdI8q9lgM&Y=sSiB)MvoMuh8JpVq^lKx6f+kg!Os3{1r-pBB#3~w+$(6~O6+zgl'
        b'Z68S0cBf{9!w4j27LHmobm$AiM!zujv=`1To)D{j{Lsw8%PX#)@WrXg1&yUG4aIK^)b2hqulC<wuPdy5<iPU6j*9gY9+;Y3)0hmx'
        b'{AM5sxo7vG;U|neW%8NzAFk~Qg6-K|TKh=f;F`<N@A&BYD<Am$p_Yc^&l^)M4co)<tAo{oEXB$j66Hbt5M(gOR3d)Dp+xx!!QnYn'
        b'RW`0FHKXv27fMD<4JO`L_(m#qR`_a5ZCR=+9S#dSvm#YkI3<2$ixO2QM8~x<w&3fJ&H6uum&WE#EIqF(8I787!LJ8SD9VlG5bU?Q'
        b'c<Pt0)s?48E9$CJWfgU`siKOyrc|P$ZgwhJQMWKvSy6Xgs;Z){H8r6ki1nKP_4E38s<g1aJXKa$UzI8<tglTa3hSFv$-?^Csmj9o'
        b'g{i8-`s-2?3hP@>h{gg;6sCT$Al%OrlF46$$wt>=Fu$lFH~*|;a%w7-Ta@d?$7Yqr{!^dcdQtiLU%UIjf_Lxk`d@!ItKpV)AHH<s'
        b'dEKpl|L^l&s#!F%^6dct00000000000000000000000000000000000000000000000000000000000000000000000000000000'
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
        b'0000000000000000000000000000000000000000000000000000000000000000000000;QwI{4g>%I004meUmHPHRaI40RaI40'
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
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaJ#OI1m5;0002;e{BR+RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
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
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaF)C;6MNX0002U|FscRRaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
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
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI5mgF^xU0000%|6lvT3;+NC'
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
        b'0000009!z<D|r'
    )
    _firmware_identity = {'protocol': 1, 'firmware': 'CNC_FFST-S3-0.1.1', 'app_image_sha256': 'bd4a12438ea7e061fea7b23ef6344086a83d4dad3bc0826fdb58ea31654921fc', 'application_file_sha256': '0365d9926e94374a65447edb90597c37acf6825d0280731226194cf5fdd2c7bf'}
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
