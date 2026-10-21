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
        b'c-riJd0<r4_5YnEAqfvjAV!v;FChsDPQuKDtPPUM9>_8#VHLk*l1!4(Bok*QEH<r~U?Cv3ENumA+etKE5uq$vMJ*N3B3iJZZM7~H'
        b'tyuNzLe)wjA@6t2z4y(=Qv7Xyy`yhF_uY5TUC%xDoO@p$pJ>$iPj1W0|AG(_4i}Lm{8fczzdCo925%*4Dn#HF%dcd!mPk#I2veR_'
        b')gx%(3V|yWt}$@6+nu)MZPpGkZ;qI5B(utkN@g|M+dJ(Y)()3*R)gK{YO`CKtd8Z*uFg)o!!^t4X!MV6ZnHRB(;7*;&1v_`h~74='
        b'c3GEqbhTsLY!b}0++npeEq69Ibzb_&y2{$v1<X*Dc1uSSMSBOab~G7oak?xHm*HBfYU^lh>uR$4Kk9PX+R|DvBO}YmNbt#Wh!AfP'
        b'Y0%Qt<ha(3usS=J+uAKH*5%E1N4v!Z9Z_g$YwT*XxU5ZLD>Q`^uj;fmdhdd&0)5b8vv)X`+gDf}ZI(^~U~68z+*=W=(`j`Q6Z|?{'
        b'Vzb581{v8p#6+hKuH3{XF*(thGA@Ex8lXzaDdI|tQ*5-fVKR$LG#85cRf+oSRgj_;`mxO_#?29{7F1MxhX$q_o#_FOTP@JcCX35L'
        b'$2(D+EzX%E>PcV{V@BrkW?P3Xu+97dGLxj`4Nm8BItVBr>=wr1|Db9-3aXbx%ka;g-edND>7jlu($Ll1Y;}Csj`53jK+oFSp-_J@'
        b'wzakK2Xt<-Da(*NkeBa)Nu22>UivtS<adXV`~y9tex_mCPo4yX=pK^w>Rg=T&*i>4H~o9B&eeR6-N(W;3BpbJLj7l$Mo;Q#?vYe2'
        b'kPoF-=bBFo^>uJ9hHDvI^>8)8)e6^XxITpIW4Jzp>nvQ~z%>L{7!m3PxXK`00oRk0NdD;<lD};-$u~!k{6larJ@KLz>mZR4iI}l%'
        b'|Af{JOZiam3b-B$CHc|y>UwAaal!p0$Pa4=iN5S4TBz%<p|<&`k?OJ1_w-1T7URbgiPURJULS2gq+2H?)AW0YbkC493Br-^Y<3?$'
        b'lkUmJXJ1NE9!)a_@@ys2+#!kNgHjBmU8`!l9SVXvBu|Ha*0BCgfVvkYl6)QDH_-R@!gFcvA;?lST67x9mNZ0q{-Ts$FdkA*A}q7B'
        b'Ql?uKw^fR%A@0r6=`dmqAu%(F^<7QePiW-*7<t6w5ytLTx$nc9-KsNx(8N4@akpylPnzC6zx2!$*G)Mw;30#A98^Q>+nP)h5eGzf'
        b'4<=8In06NKg(-vIY6d*2#0wf>iuIz#aJLk9w`96oIwX=54g4f)-K(UYcoFZlf*K&ckqjo2IG1E_Ni&|f?vztH?2`8PoBN%T^>a;}'
        b'Q!+Rqe(WiSbhrcJZw);!CC(%6^;oLA&-WX5r_}u+<d?0^Pmcu5QPZ35Kg+k)DI~FuoM|Ozib!ICCN*MV?hT2hQ1gY)#tfDr=EfLq'
        b'lXhzc7iz3#&0vzov{*7~u-0W-{p{JX+N8o8o~l)^ttLWI(sV(%_uKR_LiB!*T0eiQ+e&L<mi|>C^@W|PkPcT!b0T(x9ePsrK|gWV'
        b'(=OGxm($K)s}UmHMhwo05T>~G80vlHyb%3Vwz|MWdS5s%Onxd`C4_gsX?)?|J?W8~ibP?O5U$_0CO=2i>s`lR7<lFD?kDqiMtZW>'
        b'#C#oUNXHJ&))<T&4IK3xXK_s9n95Pd@n()QIi_$-<~W065<^p>R1t<DZBIH5WscSqFZJ$uo<~Kps2e3=A`8Vz6wjm+>-WgCvlZIr'
        b'M)lhLl1}?A;9kl2!ubME&(U2l3o<PP`sPO3P1lFGqoqf)Z{Hj(^@VSnygh331Zh)WB>ffFtE^9IJ)Y>38&sReOFLAXc1HH>6dzM1'
        b'J_E7Z(-0d0u?M2$_%qqWJw_73p(5ME+#yo;c^aB_7K%GL3dJ?={Q1#uC6HljI-#=c9v$60I*KwIRuQp@iENmAcy!AnghqCMCP&77'
        b'JG%KCrtDJ-H$mMXv|debH-9xMRAHU}H7Z9Yhr7QV?TL?ce*wQD{9+d2G)E85kEZJXc$DAc!yV!Adx*F*QZR};G4e5t+!oe<depN$'
        b'a-hG*vt6X^+5GM(O}+1((NljP-Mce#-&^qO<v0-5|HkN{=Wu|Y!D0?XoO})+J`+K?+P;5iXQZ5VN7&(0n1gU1&mfFO?t6Lk-Rt(U'
        b'WMTV`jrJcM^=1&p*~8o~j`qJeDwon1vG4n%Lib+QGZFpIkM4V(c2~sSzDOG7{@v*QJ@3&h<g8g?Pmjv?{l6XE_ggR5z9&cJ>{tQ&'
        b'Mlp78Kx}yb?$LweJuD`i#q1nq_q{eU;IX+M#i18&64Kti?%?<%o-r6VfN`Iz-&G6ah3@?x6~_INrW-Fz`yAp9j>D*J7&YxI$gGLP'
        b')r`i+lQZYl0}W&o>S>7UpF4VZ?x--<bNrAy(=YA5g3;GJsw19BpiHf^H88Q&p5(2fSkIpi-k|Bv8Qt$8XQpU+Ju2T*m>Y)fQ9*rQ'
        b'e~uv~E^&$WAOsVaYvHF+`>y(g8t<()X$RM6=R^z~4m-0@+ke;S;k!mXPYj%b--mnMcVRtFL<p4!)tDe3cn241X)bQt=x)`vu<S|O'
        b'RXI`CTJ3JtLA7-Wfc17QoeyVTl_)~ZK*L)@H4qSHo(a*=db`QK+eTw6c0+yLOR<zWs!H|1bdvw1I5j?T0-2xQT=S(cb@y0n6m~>r'
        b'KiPcisL{ek#i&Z?uNoE8qda|)DQ>P)!Z(YfMpYskwzAQ)=_+`-!~4`T*mdT0?GCq?{8P{FMC%(`L;mRId@3NIUimE4Y@WknHZeid'
        b'7*(Qs%qUgHi6^xEnb<35PG|=XN1k~|dr$@InK5q6nV)NqPf1*-fi>`VTF<8%&;9|=K<^2SFwPx^yq-@dy3bzhF-9f3VIu3}MML7K'
        b'J8?9{tv5!l+o~0&Brep>aE#v<KMEc7Y`QR3|LmGGOQEiwfe>pO;=|Wl8?=195fJt9s-%e#y9$%0M<u0CfmlJK|G=ylNeP%LLb|@e'
        b'Odxz7!qZ_56u#yW-%2EyUdqd_O9CqeY=on5t$=GiT#y=U6A@E@)gqyR(8;Vj>3O&`XnO&^2iG~YchKvq4+r}Rcppc8FmdpIaKiFk'
        b'H<A2D;F>g*<VS)HHwiAZ<zSMKFepb5Bgs2p7k&fRwpfx678RkMTo&dtm%D)^PqxwaPG<HQ+K6bcL7F@fY_<_7zYVTv2p59gct2dL'
        b';p#SP>hqW__3KD(Q&Bril19;H6S>_+Z74GhzsSwl-=ndFC1}A0eFVyy-AU@vj)khD<w~TRpsrcWzC!y;fbeI~hRA6oe<s+okHFOm'
        b'*J`+CL)?9U`G6ngygK(Jw0H5FdHG=wSLP=5%pO)ldoM~KLwGj5kA(X#r7xhZdx0krt}M7nPZreb7AW%=^wFQ@7Gi#I-NT+8lI|G;'
        b'wq(|!$fsYO`y})M_N8<Wdc=0PUWPFYg?x`aU;BApKFR<go1s^ZJx|25zm{$~`)f$F7uvo@4I+RxyOxdxQEh?z2jCJWko=us6aUZu'
        b'NYXNBZ!26bxR?)4ZQ}a=+&9gT$4}t;mn6*{m86#>X0L)*ews=X8r0{Z;8E($_kcb6C6lm^p}cz9{_6;3zX{_1frFwVhwjDrF!Cbc'
        b'3o)3_sD$=+EL>>bqQMQRQ9g(BC#uPqv2=Gp%m<q{62`h7##w;=jD)Km?xn9K=|d<F?cfm@2kE9EsbUJq806Q|+}un~Lw%ooQ5%i^'
        b'2=YLNtI(E)ibAFDf%^AQJ0E8Vv=(&lLA6f3MWt`qf8D7R>F`Wx|3GPfiZu8xd0_vzQ_0fdM2IO{djZ(piBdncl!lUVDQ`VIT}p|<'
        b'&?;QXFm6YyFzpaqRa^14?{KX2{*4kWpNFSN{6Qaka0ABj6}V3jDDy!<e{ie#oa*$>$Y)f0pQS4}&1coV>!h*i_30{DHTAhvQDT|p'
        b'lU~}cF1dvm#z@&3qh@k$asE4NApTgZNh|5!RplR#Jb4^bzuY=DJ$C_`ajOdU95S2hz<4&-;*%wqPj;)I6|V0e8m+HeV_u;0z(b~u'
        b'TT5d?8jec!`9H-}+ZuL}`t->BMto-520xD07&N0>1&wgM<&)7(wQKShsOpO%%|)1`yftfbi1B4fuSfQ>9W}d%xhPUUn`XTOa||=R'
        b'JDN|6GPV*LG2`oV+1RJ&lWF;ACt(falVg%z9@qUfnVe6y_HWv%-xME-3YJ#hbZnG61Fdos`TeS+AjUApuX%{s?5eR4{nsE`t`p-9'
        b'juSnu#M2V@Z%j{*8uv8r(7K<+bs$+QOj@iK)aLrG+)RD)8WAk>hvWC$GBZicUX!ZXHSvfCatu54J5gAgctP@bzKP#cD9((W@t}Hb'
        b'G7;7uO((?YIhGZpKAK3(*{-D5)oZ6?1!8L#rK^vE4!a*0bz!OXTd6&Q-Q+DD{I}#WyM*cW_21|-B4aYcg|$$jpHl;69M)L4!}_%Z'
        b'!BAM_J*vU4q^#?28b|;q50gL(S(?OuK^kG>K~3Hi>sbk(|A;?7c|wE)^Af+51ogDD&<1S4{ld~SpG$&}3iUWB<SkA7T<X~w1;!}0'
        b'YJgy?ru->3RM6b6S^Ks`vVOMl=$Fi%7mtWf)n0e1WAw0nwEy<e{R3O9JITrPsINQ(T$vmdSXB4N-nVS$nU`rV)3s0#V(*7i2Ry$X'
        b'{77;)jFOpAu+n;Zy3k}^KH3A0PrS&}8o>6NP6ojInoPh;-8c_xO^7fxHX?BdI^EU$%4f_v8t^<b_`W2ESD!iU4NEY@1CO3`mtz;m'
        b'k&mDGyA(UmT||dkGx)9am^xXrLoH0OPK5UAMbQOjS;>d!Gr04p$rIuJ9%9TBA)b7fenp+$Q>SmM)7LD}XD>LYc4y#2alhF4sOUCg'
        b'_@KJ}zeV>fYLA4#*oL@u7|zNV3#s%Ei|%B+EzJlAk6Q~C1~VdKUyOYs_Ak27*mJR;uKh&9K5*YOI<V^|>JorIKs^C^(-tA$ZoUDG'
        b'kwes&k_}?sf9?sR{S!txFZUwGj|QcrzP<Hd(wPxSwpZfDjEW8UqA1%jyERD@v`O*8w6ks%)-?1YszQRn64Z*AM%>hOKTMeBmos~|'
        b'xq5nB&40VD_t@vcWZ|uK&x*fP9}OiHQy$$O-h1p5h<h;fg0w8+(d`kv$Noo{{B82zH;FD;K5&QuVRBRq?2+96yy)A502@v$5EI8h'
        b'q8Sffm+jiEwO*7w4<8aHdZw@8{Gw6p)r^Z*3q5^NVxQQ1?A#WQD&9kSQntcGHEOPdk<EHm)%_JsZy``d%m7-4XU<ClCNgkDv|>Od'
        b'#2!@bRwt_EvbU*)NlD@1+ZwjKeDSFil@Qj$x`)<ziV!AlSOcy8r8+;~HIl5~u;#Nj<27WzMs>WV`>VY(w@y2o8WwY()VDr4yvNwM'
        b'F}la-)W;tJ4?!blZ%x&doRhl03jLP%rF+-KqzU7Nuyqq6+&eDD9~tdFFRtI38YY)#8N65!N)|?IZ++xqR>t?-gV;wuh;ToG_`c_&'
        b'X#VEY^rinee9uM0FE3uyo<9BWigAaIL>|<Ds6B*fHh#K$jQbZD64WKQ0Z)Vp5c6}4i7z3!iEIqw?z`BlCJ!BR-;WR68|m*)C|g)>'
        b'0Y2^?T2IHzLfX}0f+$WGMKK!G+(KhW%#X(87nn{LMcq+!duZv;s4wBZ?c(MiUhL_L><eFagK2w|dnIP}n999^W;%Y~>WjjS72{5f'
        b'IlD)6J20+KwJmDnE4#zocD(EUYVGF|*&Vhz+<hmlO#8(RKk8g{sBcVt*P*+e>&MJru=YcgO$$EFe^JywA$pdIyF=ZLOpJDixNpbM'
        b'ZuQ_Npp!!1qH}Dw+Pw^8tsndJ)E18x+R^I~&Fk0nZ26%3!aL`C?)^Z&DH{BbcgoH@BpttSLJK{r-uMT16=nXAF}o}9ZtXB1OQv;C'
        b'9u$RngAYioU-Q0Vh$Ac<F1q-^qqE)>vbMo;c52SW!?#@Qzvbe7PyFBl(z7W#CYdZ;uR;qzIQuE?SREL*cc*^ur<$|R9eVorU!2??'
        b'wP8OA&-ZNFyk$O_+K2taWU}hr>(I*;rlLoiLHjq2MRCVhPvdU!Pj>S~?hC^WbBEnY7_~X}Vt?#Kt~jW>6~1}$#s0}bQ85?$V}hb4'
        b'UhMyHBrq!SVt?etOVkz0(BL<c5Rq6z8q^_z=5%w^sj(N|AA9i!>MciNXExui$x&5m4r)$lT5eF6B$3wmXX0Lta(^_!Wd97}=8=(p'
        b'a`9NyfjC&WR`iC_4UhTT<K7<Gd-|K1MW23XdUiw@4>nQ$bCGmb>>lrabA*c7%yjeVZ-num{v-cbWd3ixPrtyYai5Lw4anVNuCN8^'
        b'ehCwv$swmhiTmx59pM`;xZfH%mp$&tj2UH<4@S&idEfTXQ_@=(&fW60amI|>BXU&PlaHR4sDFLL6T9Cd&F^>r1v8nNo}&V1dwPy#'
        b'aF1m8)5v3YG0%5$Pj8~2d1rC5THIwC{IhiY!FM$}foiG0fMAVj4cU~ghjq8dZ94jID%YUZ;^S2X9&%7qIw2zQahT<vf;FI_Qnhr?'
        b'Vc)YO{m+h^c~+VevG5M2dBKA@EP{YoA0sz!?G_ep80}N7n;8y1_4AT2;pn$gZ#aqBL6Rm_Pu;oYW%1}ah*0fnO*&>cbRe?%xlej}'
        b'X5akG&3$i<J=qs^VCsh6za>AD-5Z}YwXe4!Y3*0i&Fc?@^-X#ve!a2eOZlc?eNE_R5`lacZo9za)axgN{uA18nCwt5%q6I;4@@v@'
        b'8hJW>O#Gf-9>vLJ-6MH&#h6b=4@T&O$bQj%A9kKj*#COuEB)?uBXlQV@CnIq?}!iv&wC5W;KR~qGodyy+td(|=#i2l9@)Dy%G2M|'
        b'7ZD$yG`3Gn{@^I;kAcHtWRy7Qkzy{4B*!oO;9Rn*S$#vYJ4qdp{4aQT=4aBQ6QYC(@r9&BO_J~0tvd5l>Cr9k3hL0m@cCz*Oa>nQ'
        b'*nKnB!)+beJb8q!zoFFO$+W0@_l)Wb#dTZDBKL^{M<Nr?Kv^NUB`+P+?pB`(Bl|6;-Z;~MC4bkXgQ|g3sxu!*58a)lecNCjIjA*i'
        b'NQ~wpjQl%N=vSCy!Hd#I+7}C;r_)QPPXmS{k!RkM7QS-fV8oGrvRmc81uFuL0)rEjB1p!d8jC2PMZ^@1U^Pyu2H%llHVpr~_M9nm'
        b'q(DnzUi|i;X6+gDk(xCT+40H7992qGsD^ZZyl(5b?3(0)oTwC4vMM`j+F4;JD|<Y2?z)G=Z%zjzFgHFFY*lrN>gZRJ-(HA2fzGJ7'
        b'5#eS~yYVB`@WJ(7b3(iDHFE04k;6BR#6I4C<H#U5vL~ZA{_<4p$l)m?vCo02(H}kHp2Aq@zRDBg!Vk!)sFA}lBmEOb_Iu*2YSKS;'
        b'<oMPjo;TfUme3tJBAYD!doqyh^N@EnU=M2D;WUNB?5!~)r}swn{P=pYPqlZyspmPdUo*1*j~Cs9j^v@?p4R*^t?IKTWPtRWFAjG<'
        b'OSKtTjk1n&pC6`H*Ty6L=Z0m|3rg<)H{3;f*M`ks40peE3Ge4#-lGA$TLO9C8}9z}65jW`yzd6^z8%1u6+iCO8^ed+7>@m8{~N>L'
        b'4J=BCIQ7@z!><p=zJ2t9BuvUm00T#uyeM8Jgl|fYq?RDazz;N~Th*b9Na^(JPW@^4@SleJPY&<zzdiAPB*Ux2oBuSNo0av9x+IRc'
        b'PYiFkcfD%eGwRSnkiC7c48N;AF=pVc9<bVf8L=>T{Jxil`(L7wTP&(G-%1N3t{Yjg@0sEL12po?za=4N*BzUmAGYip&dSkRem{Ii'
        b'OSUR2XX?J^hM#@1<?$Hd#&<(bgu*J0?o(<g9n^h~4xbo{4-SSN9fFn`_6@uDW1X_^gkbLMtOM%M8_B*s!~J_`Db_Egg&RT_emiW~'
        b'HoR{ejRH0I1r#0g>;<=HSl@EU@YCUz>=45v!}_cq%Ok^gG__<$?(2stWIawxI-x1~yR`2<xm?XruqWbvF>Giao;hPidepw{!$Qon'
        b'MWyNLlD|qqDCh>m&xYfc59h8ELf7qA!+Nl93rn$IC4|=3yVf3;h!7L{M?OxDBibV#5Nm>NMb$8_&C_z!u^SIUMbETK?dsHs<4cb('
        b'h+SiB&YE_1OX$>Ij|z0+rfhJIT@RJ#Q<HS#vB6`~W7=JBA)obSsUTEq^n8*P9TMjnKKd^SbUoy5t&kSZR2f4<VzpUM{$?$9UwpqR'
        b'^iwctj($x2=iY>@AE+CSMRu#j=15^ePxB#hf&TanF=w>kV7}&2)gKiPs&?+ME|(TA)#}B6>-)OIKE1wAKQ>OEZ34W*xJ5&tK0WIX'
        b'0sFvK4^%C?zjpW?Ys{krxIqE!9%Fr8GA3jR5qC5;G-Y{hu>lWp&%@?#9y7de%<zL-pq&pqr|$KT&1Cqn3L=E55ByFgjNRKO?mKir'
        b'm^|Y-6x==$iu-I*^U{RPnZx~<?15(^H)jk#7!NMNj9hikHgQvr3(aaFZ0$u5d)$u2HRlKFY;}BmmMw1P^b||H=b@Q1mP9R%OSu&{'
        b'^ix#k<TWtmvMuGC8(xY{>5m^1Ql^@bFgbb5j3?AbbtHa9)?$k}{!p&b*pdYcLJFa00$~S3cWbPb(4h-whJ#JJ8XWY{-Qm`~QdvyC'
        b'IeOvX8276eO0!+}r7sT6F&K_t*nHwbZbsHKVTNND^cg)_*<*X-G(8!xz<;ywAKGo3H!j&7V*LWL6ZP7hyEbY+YqTzvAjyCwtk<F)'
        b'iSD~~n;}`XJuEwBYW)1Z+?*8E`dja7KKi;u2I9yExO<_R_lJWagGZ!=^G4#nx&U3h%_Kx@(tjgN{n)L4e5>b{Lw$FV^r-yw#-}G~'
        b'w)KDZ@($BMO=338;Fy^au)4?X-66WqTo{>mF#LpOcgXfr?wuE4jJBQH^q82KCw&m7)fXMof6?=aY3<um&knFEpk~7MQ&zLI?Ns04'
        b'9bqvWMt4k#$sGk%Q<-((*s-_`&+HhxvHO_tah&J4{^jd7zIOQ43vWON2pi5E+Npo+x*bsuz18FS={p;GUN|)H2=N?m+!3|@@b*)G'
        b'+jr&{(wqA**ZF;G!In4{3$_M0RIjk{yj>md`7&kmSBDb>^-~$Di|Q12e7`#8&y(+Z`a<i(mZ#NgZ-$u#PlRy?Gy*t!?drX)TTh;J'
        b')wf5E{n?SjV*Qado08Xj4zBw8_rJ1?vmTXxpzeD=HDc)0!g*u1{9$za;S*s`rKmlxh_A(ko&8dT397ZejbptuM40kzhI%kUdN<<0'
        b'<{j=6+QdIfKZwAiX-&L#YWBp915ag4iciRjKO)9AWkFy@y8383iM#(oNhnOhgsdIf{hre^cM8*V!rmu)tSOLd%v&Qn+%fZrFm~`K'
        b'5-jh+Sa9r0u=7idgq+d96bw&xgKZcA3x7Vw!+H<%>&!;!@b@q1#_m=bJ*NlPO1ZPC{it!Tx<I|7jjtSb!DIcy;+cD;xb_QzCdVB*'
        b'k?c<-y_W0tJ}y3UD)A+$@BIU(K6`L#-+c?#UQbRtqn=&4ZOoX)=pCV+?fUIwrlzmDzSCh^nf~Eg@Md?!fQc(;VCCMJne1L@{5EyW'
        b'4)?~pg|UJr@m?v%y|Cfy?8Dzqzur=JAv<*A>)A0Ix7NHEd%xPK4arJg$Ls?235_sw@E>fSE>2}Qab5_^*4!S}FkRK#gzo<4@(TkK'
        b'$)-);?Cpwr;KAr^6CcP7T{Zpg?GHRv6yL8cxgOoy&87>G;DHBC3$wM*Cv&mAC&u904(>S^27~GFV)yqj7%S{Qy!e%e-RXGq&OBk#'
        b')CF5S^~M*(2Y&X`5)~oInk02-d_VPPdwz6iy%t>P5q`eC5p*?JHUBsdtl&MmlP@Gq40F%8kThKlzw0ODsQV^tK7Kwf@q*c`UHCQb'
        b'a>lpn=;mgUDel6i_(&R)#9~e^h{_L)F-^V@9CQ68F%yDg3ijY8Dch&!Ir5u=-$?!m1NkNj_vX`M>iE`)G$OLw1u4um7+2F8$uob1'
        b'$f@KCe04r3reNTbG@k~iG5s?j#@MQZ4yL!0X@Uuc?(=g0Okgpm7ewg;V+?Pc7s`X<UO!KYE=l<6dH<M!<k;>f^gAQXbTfXSHI}Bj'
        b'X%nvyZoh3wj@56EG%sO|kLB6?9<mVwGJZBF2D>f={r6;*D1O75$nRO#vR7qVCzrfH?a#gm$?Amz;bwC}(!^OYYe>@cc}eMaSQp|z'
        b'8IzOZ9yp)BKqbn1_cg6a`6d$t3R-8d{=zgrIo}zWh9*b`?~NzuJMXznf|RviNJP$~=lsdbB$;{ijFdF7de@qy=^f4K8)@1Jao<00'
        b'Hb-v?NIrokzajK3iKh`Tjs7xeqQMN}X<9Ii`7&v)4?QNQS&nHsFOw!F^m&Q*-{#8m#~X0WP>3i__S*mWy#J}8cRrwFdNVVUx3u0&'
        b'Z<FNPB(MqS__a==4<^VDCQ#E7_X8mxy<Ypy0KRdMk`y=Re13YA*cYkKre_(pBz`v0n=&CT>%187Y(nS|9qVnN4vyR8ipqkpc7*yB'
        b'Zw?I%<_Bz(xRcHc;nbd|e$;t!Q{BGl=g)3ev9~L>NA8O|zjtS(Z1=O*ET)|of1ZG6M%$wTA51zgZpR1p0S~r?i8}4TZVB9l&iJTJ'
        b'ey^>BZ5GbU_wrt==-TyxJM4Ua*m=qt7k1ve&#XNkP<PSu&EPk5gW3J<(152WU{jjC@N!{D-q9}kH|t|a3PsTB>h-S8Uk}Bowfpxx'
        b'@An=_UwHqQL*V@k^ykYZ<;`?g4WX;{&mo%c?=;3e_vm@fP=SiEelNWM|9g~wkjVU@|B{H&)1%)muKh~hkNxvd{~IhfVJuWq98d*R'
        b'ec(6PU$7959q{~d>!E;Fy)qPk1mEQ8KRP6WQN^DP^y}P-L$dE1_dCoySuLhr&+ZQl(RYmEYKOoPO`0@5?%AP@+v1)X>OD3pg!iOu'
        b'<^8|;H$(lu9n#0ESXakK_K(5F@R#tyg<QAbE8}5aMrsH<@7giceE?!wwKe^xdz!I(Y+CqPr4`oJufz;iYfYY^MHAIWvrvu~YlVtK'
        b'3&i*%r}4;8D`W{;VXEj_Q{xHg^-K}xuX)XL=YXeKT((ARU6Y?6y0>7_hyD^JzAGN_sOg?#v-^IGd^c3c<M-?F{-Rd6PDmA&@wf;c'
        b'S0%Iy%Wz+^*&Q-O&#yX9z5#iK@^p6(QHMyF1>6tei#yHk;d2mWx@#!TG(@XBBjg-?GqJnN%$7YZy%mbh{5{3ETZeMgR7XJjruHm|'
        b'q>Y0{-aZ!ES0UDI6`Ei3*sx)3TZOFD5ce`#>Vl)kWZ76UBvgI{*2Fk4s%g#I-G9Ssxa)?5sqg@5R|%EI_}4LBx5542=jax+yN1f?'
        b'{Gt832o>_N>3*WU4P^eOFsV1Ob6EOPUfAaRp-pVZG0c!Z<Tk<J_ZsqsQZ$A+ba*xR`dRc4mjI3Y4pR=3rylW}o=yLLU`yE8zV5%R'
        b'%TY}`tLqINWpi!tqBJ8{6dydYX`jjST+gQGj(~gh^p=R;M)KIi?bB1zg-PfsEel&WVN$Qhvu?r-TRh-5J+S3tAw`%p(0}^qH{iS4'
        b'z!Va4LWfzNhG;CeOp`w^Iw?ASV^LB<C0nGj@yrdHH#J?q;Yhjqu?ac2BRC|vwL`R-SX*d*bWgALvo~RGA78U9Oelmv=r^$ZMD=>k'
        b'CQW~-<TFX=6DIBsJNkuGsew8P=@3PrDhsz>tPB$xm%%hUz4o8XHe062nh<65c(S&rk5<A2KMR4il|;}QJ~;;isDS~5k(!FbWW(Vx'
        b'e0WZ{4x)uhp^Xn~BOkuZbL=hJe@T!?{E0zt+`swlbNY<9p7cY)Dx%5n(eHEr{hU5MswX|N&oJXaQ~zJj?fdIF`3*N%2HY>>T}}jT'
        b'ZTBml^vL`|dR`u8dg)v*6$da>)$$9M^wxd&9NhOlLgY6y4M)%AghMQU0j>YZbKQTG%g8Si-A`f}<yb~p*uXC0DT<^e(EI-1oP&FG'
        b'qKbIAPn_GWE)RF_rc-F=IrmOBb?`MPBP$Qqej&Q#2^4(84qvD7-if8X_OP$lSZBsyw2)A;kIxs=PtNtmQzIjR=yRiw4;_f#VYL2H'
        b'YM!Vb+(Z|M=1Iv(6Jt%2&h_qmo~2{mU~D3ZuS*9eBt9waFrN890$Cu<$;SsgVeTF*ByI)PN$p>!bKhe8U05fzU!DH-EgQ%e5os%-'
        b'%X@qpqE8#wd=A#@xP17ftAaMJ@tmpsT)7&tk&dJ~zc131doG{96dL*`Ci7y?HzYnvOcveC&iSvE?%H#{u=!lFH@xIr|B`cbzHf?G'
        b';X<+KoNxI+onChiVgpxV^Euy2jCttJb>B_X=f_837Ue-%lw6X9us&cdcVF_R*}l1H39l9CA6l7jK5)yg7cG5a=KLooJymGkkn!p-'
        b'?=an@J})VxkU|P6q>w@iDWs4>3Mr(JLJBFQkU|P6q>w@iDWs4>3Mr(JLJBFQkU|P6q>w@iDWs4>3Mr(JLJBFQkU|P6q>w@iDWs4>'
        b'3Mr(JLJBFQkU|P6q>w@iDWs4>|KDh*S*51`B5FP%9V?udd_WAI6LON!f0okjve18EJ?OcLoMrz$cxUTs_Aj3YJZJxII3e|<+0y8;'
        b'J5~qtL&+AJrp3|FcA4^f32A`PuZR=4EiKl7=lE|S`qSRkuibrN{-(EHfBwc3k8~`3R~cc26jDebg%naqA%zrDNFjw3Qb-|%6jDeb'
        b'g%naqA%zrDNFjw3Qb-|%6jDebg%naqA%zrDNFjw3Qb-|%6jDebg%naqA%zrDNFjw3Qb-|%6jDebg%naqA%zrDNFjw3Qb-|%6jDeb'
        b'g%naqA%zrDNFjw3Qb-|%6jDebg%naqA%zrDNFjw3Qb-|%6jDebg%naqA%zrDNFjx;g+2*Y=O^EtmH!1HBpfaxN%*T0Nl0E(yowm>'
        b'PCQQh$Y3$#G#MLGn`{o(YH}&HI2zi>Rmhm0YcS**a^(B!Mwe(bh(^6Jlitrxo1JF73jf*#r8l*%dOe}#`r?=C#~fVrWc6d;pJyIC'
        b'|Kar8yWCSYt|tGNNefp9T%mA{fomLGGvT_evbHpLk;Tzr>uAXpi#uFa2ZY4pT64NlEU?>MZFWnO)p7f{2vTmWCGE~4Ynx>?DX1V;'
        b'Ov@8CcoUL>>gu|RYEw~h4Vl$ubGh2A%}zp7rPihsW2Ql`PbaM|SEn;~)~ptrtF@~kt<l~-3p>2bR56PtC52Um%S%dX>%`i0vC5EH'
        b'lPwln91a^4SY!0|tz8w8w`)2n&_LJ$;q^iHMDVqLw)*n@vN3@a>{ybOUk`i<8QOx#n@Iu2>mbfQ-EAc$HFdegH8t21?527?57!pg'
        b')|OXS<<=C}7S~~1Vp`^GXSc)EotS3OJK@*pBnc%Yc$o_4&moCj#L{?YccRn(|G+47aaB=yRVii<EV;;9UR6?!_a%#R<?ewlP1UCv'
        b'($aGYlnc)aP3BxkZ@^jrOTm(2gtFp_ifZDtI#yU6yf8>xRb5qBOmj9Zs4JU88ry6zroQJG%Nq%43M-4|kc0%1a5G6LB?;3>LODsO'
        b'A_<F00%UI{3Fh*uT9N=gPzUvfkg38{Qwa!tR$T*FSY26Zsw%1_q<cz8Ub7}7&jwc;Tz0q|aCO183a;<N<%Vk=T$|zA4p%>1dV?{2'
        b'c1C7ac8;Z?vB}yTJV}SLwFRFQl7gQWu`$dCJPubhT)O|t%5R11G=#SS?gETlo|V4|(jS0p8HBS-Nx@mp8%(dk6~)6h!zGK;DZhAK'
        b'AWOX*=%K%=dX@kEX?4BY@BYKqm*;Mq5A&*=6tqHJw190;pAw79(v~ZhcfcI!w76^yZC0_#VS|AblL?<Qxnie%B}CXeM5nc_In`x#'
        b'y2NC2b#02+Y_YXjo8n*y7no}54D{DXf79vjY%D)6BqVPJT&ZxS!*$=IA$c#23Ca5#T%W_G3Jb}*9<CI)=D@Y-?U1}QNHdp|SglQB'
        b'tG%s>6s~TBnmJt-hYKohZ@g1%vbI@WR#NM-cZy9mrv++GircM@7Hdc2YDj7CBxZ-b!HN$X?HwJ~Mi;5HyX+3AbXS`kUddDwsj#)%'
        b'Tu#vr4R_d@AX|up0voU>o)12AIV>xzZ7hN;7Tf*uTM}@$G~g~ErDzOH3-?Qd?pc9e^e?*3Zf|p1U7#ENg8m6A&83iAlNHAb+q_t8'
        b'!?ua-whsR=<nFz*tb%Z>z1_-z*3iebB!Fv)AJ-DbwM6Dx>c_P-fNQBA*HXr{ROYJfv~@H=XTz^`mG`c*3mQjEU8^8o)XM>b95Bj('
        b'bU83v4rIuIOgWGx2eRcrjyFSJ*514g-pmc&+zsCB4c`0>-U1BX5)9rV4Bj$~-ZG57`g_YTvN9|kmNt8fud%*+L(si3=suW#cF=uB'
        b'(0yjmeHIM6(`D@>i;WDIaNxH~Iq=)XFryrp7GVkdWj9ONFT1IQw4ETDRCmaCPSM&yXX;`(u+$r~L=Kr)IVPHo$rtOBEt8)#nV2-0'
        b'0wx@r+=aE?z+!J`i8r*=8>&qA1!wz$8NOhqFPP;OQG16s2vvp2X7h_NFRJv0js8iEmq~1-$t!J67b$78+neYJ*}Gg^7BFP+hK$}&'
        b'x;Hf28_Mv8GQFWJZz$Uv%JJpwSBS3^gRdBauN;G~AcL<YgRdxquPlSFFoUl&qpvihUz>cT1<nUwC-_Aef+LK<5trmKJ2)aEI3hDR'
        b'B8yZM7l}3Wx0L=C(BDP$*V5#$I@z)lcnh^Fw1ehu6l<)Yp5+@fcJ-vPytbNDR@au3T64KrSTUbrt)8QSqmg4e$b-e%ilSUwBsN+c'
        b'P5!|qSOG!BV^Rk#3q$2Kw}LHQDApFvXINw+^R25pEln`5=)#4uJXo`s)Ga18wX?G`#G1vk>K6M6=dH!%qKW<%&|kiwV34Wmh2Y$D'
        b'S=#7IFD_=Vguzk<mFXO3bIjnF$uW!DC>a9S0e~yOK0v#r2N3P-%G!`T^er~RJ^B~h0nx|!Z$R`jehU}|coY!*vey73(EI@$3wRa~'
        b'eUXcR*8yG^8j?32Fd8rtFdh)?D?Q*Oz*_((16Bb}0sJq(sem1Tu~<LAX@Khi(ft1@;EjMg0dE3)7Er|c0LB6S889B}12`S<pMVKi'
        b'FTg~=5x^wC2(W`@0LB0&15N`>0Zal!KgtM*c40ms+JO~-serYB=twLBGy&cLhz8~=z(PPbU=iR3z+%9yfF*zr0hR&|0+s>(2Cy9P'
        b'X~21ahXCgTz6@A_{R&tK_zqwd;75Sf*bYE5;03^2(GLXstp@uU5KM7039t_P8E^sGuz(8zGXWQ2djJ;$&I4QmSO>Ti`yKE$?03Lr'
        b'fIkGh9q`A1{{{Ffz~xwPKs1DZ4`=~=6|e#D?|_YfX8@Z3KL@k|egoKy{SMdys0k0r>i`@JXh&NcuoLSIco*P}fDXV!KquPffNO9('
        b'0Pn^61O5om47e7s5pW&g62Kn=HUPE)wgI{Toq&CSs{zvhdjV%*y8!io4+2gA><7FXa1Y@30S^Fn10DhV0pM}K9|Har@E*YT0nyI?'
        b'4A2dD4zL&fhzPK!(H{rgjO_y4g1$N6RvZVwp8^&F{tR#t;LicAfDfQN0d52A1l$gIH{gSS_X7R`>kar2;5NWt0uBKF3UC+TuK}L|'
        b'^q@Qe_5;2GIDqp4@L|CB03QMT6mSsm-+=#(3Sn$W-lGVBJ8)hAK8C&o;7*hyK-_T20^9{y0Jt0V1>kQ07X$9W@c`V5as;>!@E*YZ'
        b'fSUlHz<vgN5^z7@ZvkHbd<yFa_%zB7-~pV^LTKJIfZxLXvnW4+&td<9-ufM27~nyad%)l0`~`d-Fb(h!;P(Iz1C{|E!FmF|09XU~'
        b'BH&WMKcKt-9>snKd<pj%0FPn61HKHn2JjW^cfdaa{u1yw;G=*iP+kCE#d!?)C&1?cPXe9*L|^hvK=d`=27DdUuL{ZgGtL*d{|n9!'
        b'z`x>r27Cj@VO&Vwn>Y@De*?T8@GWc~;M;%+fbZbE0DKqc1>oNSa{=GOaREGy^BeGeY%gGy-33OSy{n~FY_(cC#b&UpsutFY4PDL6'
        b'R!1DE1)m1oFQ>TDVRKn!9}_%WtdCkvCaBe_1hrb7sa9*s)N1WgwK}9ttq%R6T0LfyS{*i^R);^SR!1CFtH&m3G^9hLQ9Z5E(sgF}'
        b'3QJp;mBVs})z#(bur|RmQwmyjaduv0^d!(>L?EcdlXd#p`9)<F<~oA9QBQNwpl?2gV5gFM$QZiDi!QqeJ|@%}@}7}UHluq+!r~bi'
        b'+toom$U;jOE~&ZV0(uW67E`OXi4-x{6+GNlD|od<cDsWInM+E{E$w1)M-zd9zyQU~vnDGwa-DurPG(1v+BU1T6aCphPgqP9!F{$k'
        b'bfT-(+QDpvfI64i+cBF)>Sa5ucXfdg&;;%$m^3_+y57j+usXUr#5?Q_P&^D5lwpNvdz;v1?PzheiuUGa%pIx*?Xo#rv3LEP+y7LP'
        b'%a$oWO@lJq!Pf;VZ8gMqHMWYKZ59{aH;J8B=VZP#6DBC#v0AjWSZp2e!0G@AY!@w%114E%gH|NenHP!8Hiy#{$2sAliy20u1z-gf'
        b'+mv?s>UP?lHkuG6n^rRwdL_+&^Jel?X7A8&G_!f=-cK~MdywWvGusF0)@Ww`AT5bzHV{%nG_!+{+M}5*gmiZ_vxks+qnS;F^s{JY'
        b'7a=_w&1@K?z0u50LV7Qn*-A+Nj%M}}QuOuAW<r{CJ+qsTY}d0j3#kvn6M6UugroUh*4q%ip2v?sIEIH8n?v$$;NeLz*v2MOc9IlK'
        b'f=hqWw^yd(ziN&ezkO%I_nuWMw*QPc#>XVXccSr>Pemd*|4p$s-3b5DpV&!Y^T8#;6+a2>mnCE=F<ma3xhIZS%!zp8;qTceXmW3O'
        b'`qu1Se|R+WU{+|x&z@hHzVi6vhUJ~%dg-Iv(#&m^jt=manGO`4w!1+PEl!vqO<j$s{SxNQ0c%4wE~1oe%87<FL$i3>jD#5?2-ys}'
        b'NjifHT&uOMlkOaY;>t}(5EG`038i8}xtLHTCajtRnh!#&=Cs*5tRm#fu(rZ1CKQSZi^YU8F`+>Gp%^F56&qcSw$xRaSt_{=e2c20'
        b'isD=XbC}TG*IW{xkXmSOvc~J;MXt3mxS#_RmtUM%WOX(=Y@IkK;&Ho|GKKS};WT-8k;P?kt?sna05+uE;tIb^2H}-9xGbw6pK%eX'
        b'Kq9#fYL-iXYwJvP#kob*3+lT4?oGk><yGCJyStmrshVZNo}#TOtS*Aa-A4D5S=fFjJhVC-c1JFhH7=sYiU$#1{g_5{5DthU%Q}{I'
        b'R8>P6qDgE;7maB+do$`gs*N1>wl)}Ho72lATAFbWud&tA(SnV2wZcOuYk3+JoIpg71j{O$v)$snliom~phY`a*yd`sS=*X&1Mb9?'
        b't)QIcY%p5X^Q{yotqWAl#aPPC;Js4!mEd*|whC%u&BYKb3k)r*0I?H55ZE3(jJ}S96I+MN+G2H(<~F;<MX+LIm0Stpur%514P7pm'
        b'y~9atohxROPK(pI((Y*TW>Z>Iy}*p4S6x$=OA6{>SkN^D(3weg7O5((uB;`7v<#w$s|1{y_QPQ7g8sbYd9c9&{RSQfmL55g@{VRZ'
        b')YyCUM2hJ+iloTe(1rK6nQIE5*s|(M9QC@2YOI5)#spH0VnJ>z%`iYzDakS7^IX!MsnhH9-I%t9a@6EQ|CMIJl?|6sk3R<Z$)P`Z'
        b'n}ZK?GD#YZ$-$p&$g&Xma*XhknF&9$G3ji4Iy)VHuvqwo$V$9`wGxt6rsGW}{y=G!kh+p4$-w6s>G%VA)e*6Th_&Qq9ZA&@Q(fU4'
        b'0|UK|lvJ2%%SZ{dkQ5i2YpN^BZ3~NQa#4?@k=v@x(8SwJi)-Pxs(2CJ7FR8(tku=j5$q!!sj3F10tis3okPrpI#N@jBh|G!Qc$EL'
        b'#ekJ&Fr+F>b!C{&Tn-6}@x)F?YT;pRF{G-g1GYj_m5$t2QeIQJ$W&9D%MTi;)~YQptuj^6YJg2xTUT9UD#Z~hsVOcND~l_uYnH%W'
        b'QB65kp5&9tvb*J55iWXC=8b@6z&&PGP;IIy0<1JGhD?jiVhsum5zFqTrJ5Ej7RyltxKtJu*A_zd@uoHlm<Fh>aB8f8&bk>D8;h>Q'
        b'9iJBYi9Xf$BuL@KQ{lTL8y0(+T-bx4Ov*s7gEi4<YjozqE#%hT4t9?d!?MXtl_FPaFx+*;3yZ7ju=y3`mE{=7EhD)VOzJV3>-6F('
        b'RCp-WFgm%U$}Ss}sH9qKPEb#v?l9BJY8Vh0vnr|p*lmevK?Tl_O0(Swu!w=FhW=o5X|92Ro^%&sxCladq#P~QnywC#YXk!n71%s`'
        b'3!0)<LVGcn0W*gQTE@A|z@;Z2q`ROQN~q|7pQ1XbOm|5w{=j9%xJ8B4^cN$mS72S>s%?ayGPtn5W<;FJ-Q^wZCl%^evPc$3(w$HU'
        b'wY>$}4d#ALS#428U2%0urFg3-n!!K#CR|kz7NIJb6r(Cg5LE?r<5dMc(W-)Og8SFA+S^Hc`z+k925?#%|I0|4tSx>ad_+^i4VlS_'
        b'*qT;}d1BRa&}cPv3(U(a%BzaWtadO}=^6GcuF;)ojgVB#n*&J;p=+9K9bl2xu7(WTo#c`OT%tprCi8;hV`*C6h-}N7V7c`@pf1;C'
        b'pHLQR;&yc|N24K_Dc~9I_p>7$*)IU`Znrf$?9hHYNNw7(4p_)-?OpBQ&vaTL2G199VFE+D5vBx80JQ31DFmy))@W&KTa9_pr3;rQ'
        b'TvH8TiWt)}(s0$SYxNe@3X2+;;SE;Vd=i@-_IAq3eJ7Fnf0#uEE|eX(zNOJ)2gn@!3G1pxJbJWrLS<Ijz!I@S>4w>Q@y@cl)6hYM'
        b'^;mSa+QHt(<4HV>w5(=1p}*BhmvKAP$0atc?yx|^*@})widL{~to+E5`fmJaBu!jMD`m{c5bp#jcd`==`N#y!jq(mW=3~n@t*g`4'
        b'(qU<HipkU?f%e;1rUWMQ?&e-YT3!+P{FfCg^QDQEcBhL!bBbL~&<(zv<iyOR!B*KYV<!}x<}-=Pn=exibPO0u+$eEc+O2^FgH%A*'
        b'FGe|lGJ`q+Z6baYWb5eca(OEokczo={t1$u&~)a3%Ql%4PhfD{A5&RYfSYJ(u(jD-tD*jja9rza%$2^xTt5cZwH|BPh}sHe2ZXmW'
        b'9gXwK*%;3|t5z>M!NY`9PSJ*jVKYrxE8ZdoJ?W53o>60IrxL{qo8eyy)<f*-q<PSAlYJ#j5*u_Qrn0m(cA<mJXFx)F&TN`AAtOBp'
        b'Ex=AItySCV|0Ffklf?m|vzMQ>;egO5EjS^e$*ZhRzu~S!JJu@);8(Y`;hcm?)n<d#P+2fLnWGGI1#|Z$rqz{=*MxMKb5K<q7?q$V'
        b'=!yuEf%*wp8r!;>SazU+TwS<ib=t8dRDCq_Tant-9WFLWTj_oW)D=V$Rv^*Y)xeo;-uWid1IE=@Wp6{Bw)W08S)zP90)CA)TO3Yw'
        b';9RIi<R;UCoz_l^gJ}|G@Uyw#S7lmbD(}z()E$8SWZI?`=2)`@CLmv%M0VPb!{wkmX)r7>HeFQ4V055TFl8&~dmBvGIboVo!9oe)'
        b'xnd1UjkMU(bkX8y#B3X}%PozKT@ZxUTd?g=A2j8m)2Ta@CKgy%!lXqn2S#kQ2%ZVFlof=1W(6;{(Is}Wtrbg0qg9@7C=rdVVi)>+'
        b'Y%JI&94)kCwQuhPD@AoN%hlCtp<~zq-j+p{3@3XSD7<`*US8qJ!{q-CiB7DRMGBR-PAsM`m0$(f)(?Mu1SK3aw^#mn0lENnfpz2x'
        b'l&xzp^uhJBgR{>DyB%z+YthW!17{tucj23Hjo5&dHYeNrLfv)wZ211-WqStJ=QhwCpa*QYkq81~28r%)+2~>`JByf#Y85#hPAcBy'
        b'HtV(YD6Jyz)c?&6^lt`J`2UBEa0a#_pa3?#`T7%-KQ0~DRsy69Dnp(DPJ6S9wSp^hC*5>J3(3;hiu*Bab~CL`jScEm(CNZV6Icnw'
        b'8n%Dnl(iY5tA$s4wYOVg#!`LLYH4#hxmuu^qSjc68qz;!i`=tx6{41x!`9M5ZGW*G)vLn>lbXI<M70zv7Zbv)b<%goct*Y~z#;?Z'
        b'rped%R==%gzc%<6ZKbv#t|r`!vvj%aV1#ii5a0J`qAHgy%*FB=OkdfeHbEozjr><+T|f%C8qfu(%9)~qZfjUACY0qd!-BqBb&EGM'
        b'zamX-X!JmASKz9zW3@&lMQa&UbH1FgM~oX{X_06sT(#i(YW{ATh!c&q43{JeR)uO$CRg4qb^cPESkE{2?HwXF(Y-rQ^=b0XztalZ'
        b'A3L6A=^a0AkyD+#!p|;9LywbnB<?IhX)FWe=&-g}f>N^=`KUI>q)=fxaZoY>We%$i`oqzVlK`g&wAI4*+;Ks2QB$SXYQ58&8?>bH'
        b'PROp=M&&vvLvC$TCE7+;LzW{nxf9$3YmhO|?Dz(&Yo!&2nWk`}m*6k7vSIJ-r6y|w=;TIvI)Uq_3%lNhi=MpDvuQ;8+1F0c-K+;}'
        b't~8Mk12q`%i~==>cM^5XaIsSpoJXZu>9}MDmXnOb2CAb|Yydy)PI^k@fV?08Yk;3KMjPl8WE2%NJW(gK;YkK8vmK(5_7_`sai0=e'
        b'hZa^BZa=`o05^_Qf)t<^C$CXpQ{p_}6N|r42}&HrTu#&3*41L`KxXa&{_ikf(ujog3^5s3LVV?r);@*KxK_}mT#@jp(SpDh#AaJd'
        b'7w*A=b)QBmENHu-g3Apss7ej9jI+|c^N|e`o#dccx!dR80;UnDQ4H0ruwYp%S2|m%D}!QHnxzv<vvs&f$c(U@tTg`@$iNJSnTp4F'
        b'fzjwS@Zsq|-PMTpWpYy&te#XvQv#EF`{NpuTUPz&<gzusvegDMD*LdsQ~Y#~&m%_Bt@S!hjnEkmCX!Ap0wj8cy{(HW3wfo8??BtJ'
        b'EneOcph~P+oU0S#Xm9-x`xxf|7EDX(!~-};l8`F94md4f)X;`N_mkJFiJd;e&uVIsfFFW!vJ*lbMHhEtp=lPVJ3WmR@36P{qyW;('
        b'>-9>z<4$L%1!f{Wfnlm2y&-R7plWw|Rfta3z`l5SQNn&IvNqF9Y1h&R)cWO%6nAPlA6wMZNL5#R1HK6C)m6CBZbi49PcZ}C#AiWc'
        b'b{aA9<(0mK3j<9LJ7uL9{E)kSS9l7hi{pw9o9$f=SF2asqAG%3Y+<L?R_3_1qpE7R(t$*2fChBAFg32S*POZp{iAD6Jr9P`t3R1<'
        b'N38>=Uk!s&@x{curc=pI^M7NxEfrrJq^HqsUARf*<;9w`r<Hd!I;<#-=)Uqtmu4`FGvkUSHhY&&ng#9}rV+Eh)WD(+3XPg*?d>`|'
        b'(UHZn(YrAy-j)iZzns~XI#GYSFAwTg%Bv~Mi?3VW2KklD-Z}8<W;WIVyK1nSx^T+2I4tcj)p5(Fr2|>$6tzJ^bFu9XFca_<Mmz0#'
        b'YHC9<<wX_6+<At4skZbEsnyk(CYoe(nq}vAqK3PEG&eed(<0_uVIXB^i)9IRgdJQ8DBsRB6*!($naasv)%9s0=zq)t6*q`AwPdif'
        b'?}TETx~O(&mj6D1d+um_b%EH^-3#wSlzLQ5Hrd*y7BuT(3l!bPPYI!rHt&eb{VNxRJ_+-Yn`S{9nUNz$em9jQi<@(GN26#iFQN*c'
        b'9^-)&Kw9SFlRD;uK-IWrW?L+{G0EnUJg@#^(k95+YW0~4C~Rrs0^C@DF)P(WM5m1jId*g-_>c|@Gcy;+J1^XM>BMt#zPpMe$Tw=)'
        b'eiU4=S~6n>3=~!aU$Jbmu&VlIJ`NREnatoy6N_XMl<qIsn!J7L>rXVbQ@IO=<+b{o(cavl@M`utjBHXm<tc-IZ)5FnqEzzn@zsEC'
        b'lJFfEoBxQx#A15QWyda}7N%2PqS2IWvaYZ(dzrS2&%$=PQAjN-ZUE{17HPH%hMmcsP`}KX`3l2~T7b60XNOT!(kUh<q~{oQY-<sH'
        b'n2hwC6fWlmy7B3-*qqc3V*3QPX1)=RmNq-+<~4#?xhVM+CwyXuj+d2o6}1SwW|XWMsDMy+ioX?vuiH=;rNg??x1}U|T-0=|3`(EN'
        b'q>vU#-)CY5oR?cijW)SNY$<(3NPfeI7J0dR#eA_eBPT8WKj-iF8UWRPlr8XOqDvdO;F>CB@-A8bZ|Y^aG=Exd5#7O&y-#`5j*c`I'
        b'mF!jDuwdFj1*LemOz|}@@Ww5Tcgl7diUK%NHo7U}-6doa>g$jA%e5h%?nHoe)3os1Yi;RxYoHCK>3UzjO_!^<PnF1uH^6}Kb%Hz)'
        b'zIt8F1NN^m_=HY6dVYSex4ZbOb=U3+Unb}O>=2vjst*F<kd+gAU4*%u^!2;{oQZ5E1PxSWW-j*$xCbUH6PuHdxYN#z-GJ9+xO9lg'
        b'v_URgXA0e&k`IjVwHIHFDl_HvP-kO$EvO*6cg0HMqQ(CdO|C2z-9lO3QCwUo9e!2!n=-hC?k_o@fP-YrZ<ot&Ps_K9MeSC8qyT+S'
        b'brI^C()8@K*|3PM<|huarbB}*K<G&kDh0lEL{C837J|=v1Gj)a#+9C}fLCH_mk(vV*69_}@tNS4jx8sk(INj?4%tp@##dcr(WR?)'
        b'M=JPwAT89`wmWbNBv&o0#m#CfwFF&qPvHx2cCejR>!^L==maTb%bOF&%T6b>1I&dLbVGfW@4YFfp9_u?hT6d`IAiD^nEQ-NSuR|5'
        b'-&q<JRi~xd3LY=BC?PMjD4K9)2bp>3h+UGaY){hnW!Zb7{}*z-w61BeZUVDDEdx)&^-j8!d$%IGI@v*3ylgkbi_KjfjcoUwZneAQ'
        b'c|=bPA>Wl2o6GCxT)K$+Y)AUHK<s3Q?<)HHp!Dx%o!<S!fR`KbXal+e-$P`I1p`<-KLqnXG`qaPA{$jUJjm+;zm9g<g1SP;x|wpY'
        b'*RI86G*`GDPgtCCnV0UU;q7AEr+kY|EKa3I73lFYbwDaGGe2j_$zHQyZxB1FMz%FEug-gH_aDZNp2GeAAHAS$8(tQDVWQQyF=KJL'
        b'z~V&?-;h=m7u7Pe-eKz$4Of0-^u1C|T}!%RU_Ws8+U{VEd8skmU*m!yle??~-=2d9bRV2=gX?K5{1UWcAiFM@Sn^-M`HSBrZwBx!'
        b'h=3OZt~^m`KEXqhMhfL4e@lP|XzvKvaF;V?=hplM2mW#Z<jpo$=+**z#UM?@_f_~gm+u7^OB1XrKQy-UrNsv2*O%B<QI`;x<9b=X'
        b'yfK)N9h-A8pw4A8+xLPcgT9H-(gni6{33|4IOv$*4(f~=EB2WPew+jB77%%U06znF<Y;et3-Uc=t+asy<FHX{ROY8v5HF1t@g3$m'
        b'=2K}dorQ*%<%(0^F9leKU9#8cx5bV56aPJG_R!|_SqODq<%gLW8R;4R{IoY+EXMaD1dnAh7CgdiOp~1{@^im;Qk-&}-)ksNkQP|W'
        b'8u85xQtEqo;?nZy!LEGzOV3T6e0M_kpWjE($%mS4-hFMDHJ$vRRmXQZ9PI59+@$b(6+te{EZa4Hr;|QSs4L*_tK;^Ht^yx+P_^LH'
        b'QG+*$`<-U~c7|2A$nFSGrOYtU$%k7`oqXgjr*L}9!0igC$fCk(J_~gIFI(u?o0r}<IdlQ<b;ynNd;0@>hng;_E_-T=U01xyg{RF;'
        b'WFFVDK5v>#N7AS1^?G8$w<Kf_8SGs4a!Ch$t-<OYZ271?Py}Rc!{o&q?N#|qNl^>D%llP};JkvK28deFvjCB+^*eRue^XzEDl{;P'
        b'3s<f0tk)|=IJ=oSMuj!tkA~!%O9Yt5Q~$u~+syR#Xy5@P0QYCS@quS-d<F+T?36tg*%+mVWWk4V*g5hE*yT^H2u!KVA4!o)dg$GZ'
        b'+lOpxif={ed`Ct)-#O3a&v1B~FMpClxT${mgPY5r&-lKo02&fs8I%wI13#h>e8M6oo6R*T@+N1SwFTevsj2hsB3|aK!@F6`2Ac~>'
        b'kyZXnC@@9oklS4HM3c`ay!)73iUYQ;$zt6S-BNip*@*=)7_-?S0-vV-Cli4W{7)qUpZJ|f1m)#-8sV*qcc0rQD#1^vNXoHnlbob-'
        b'2~IWWkuKd(zjU*l)cV=~vWlheG|Tg^#J8o)><tpA#QAnGrqIdR%c6=4{3RRS%&XAhW*Dv*xL9)uPsYvDP8XfmEc43QDWt^ipvM&;'
        b'0n~(~fBr^CQm$^m_Hinjz=3h)mx(L7Oq{&+T+Vi!Nvi(_t#2>cPx(%t&J(r!?IiOki{HL+P%8dq92VK+b!XYqLsFSuhf(AyTCbq8'
        b'0-j!?udcjDOJ7%)w_&Jy;JPDtt5A2Py+hqq_V0B3bfq#gpq$_xs(^==G_5XRqbR6l!P#1U3ip!dvXESH|3`P}zKSkr0|Z-l`CW%A'
        b'?^#@Vm%=-La2o=ZCH^@BUAq02GT#?n`1(*Nuheox5kKOR|I#+-5B8YDOAORP=)$IRyMS50g#F!bu=mM4O+rtqXoqxgpK1kF*!ZVq'
        b'SMogx4!%K$zef6-4qBOcZ*mp!vn1SG<DKFcWt5|6=ksN~#ZLEkK>>R^1Xoqs0VQ<5hC9CUFmnUO=V&<tzpKR~W#z_`w_henz#j=;'
        b'h08wyVSjurE6PIj-}y<G{5Eg1PXh7JDckH$myV@lv)}2}f*>9#{1M;XleIRF4LFwbe%^>1+^ml>VDxLd8XT}<pegLNp+TA9D=p3R'
        b'a1sU{x3DX7ve7){X`Qk-$~^vFpYBRt8vWRp<uc-i@m}wUq-W38>vaZ0h7rJ+uE)FCnfh#ijI2x$SzV6N00?yefh)CwTtgm(fp3fY'
        b'W|%xVWFZOA>i*h*FYNLPA}^4${1!nxU~ggG2klR9zcSaDx_f5k?!iKi76aA7WC??%3``6->EqbnR*#Eke^>pZc=k8dyW-j3Q@<I{'
        b'{+4>fboO`Dd#AI%m41CX`}^q+64>8MyA#>pN`F6z{hjowB=$Gbg)`XSNB?>T``hTb$?Wf<9m(u(qMu1-e-GW0!u}Te{S@|h(8V*^'
        b'-#`z}WPkr$a5MYc=fCOLw`b<2vTx7apUS>H^HwVR_DoV5`}WL+H1_S8gK6xWGgD@<Z_X^5#lAW7(Jc1OnLG9Dn=`$7_RX1ndiKqk'
        b'(|Y#Jnehhp&6#2Y`{qoWfqipEWn|x+$uY8T&a@lZH)r~d?3**M8QC{yzBICLmyAni-!7R6h~LXB15C$n<N)G_{~iI%Kt4eHYUvPQ'
        b'7RPMB*x4a@_<_^g0doO=0{A@~2f#f1&T2+T-W>c}bHG~wzsSIE0zy4A**9-)$z<QWY0hNdjKRODzm4NEj`)q3<C*LmFkfe~Z@}D`'
        b'#lHDc47duvwUNcXmGZkR_HB`zZ1znM9FO1g@u&lV`XR(G09=<7lD825#yl@1ZxNsga53OEz$JkH1Gp4WKL_dq_^Vr>K7g+S-VQhn'
        b'*aJ9yE|d@04A=+w%3S=$C?R5gNZtm(6@d2vhM7Y0ehioh_&#7I;0J&|2K*3k2jEA5qkvOE;Ee?#d1C;N0!{)P0-Ovuu@K}6Fb!}6'
        b';Ew=*4fqIPKj6!Nj{sf(+yNM06q0uk@NU580dtB&@=gM-2gG@XvgLvB-eNY77L<qN{dwifbLGFsUsa(h5SOU}{)QiU4nq19#cXbs'
        b'%wu`IRm|q*XS*1`Olr<^nwO~!`U89VO@snff#+6VIU3IM)py|0a-Oh~Yv&2!WhH+H9_%O7C3&0&`{coFUz?Gqs8UsMphi{j=Ss#m'
        b'hVz*@54lV^_Z9~7gz@&==2uQ~rmr0O{e&Q%a9++T&Vzlw(XUM8aV-wyiQswv!>^q4!92ViIc_XZ_gN|E3z5l=RO;iwemwSgpd1LC'
        b'C!*}iJja80#&MoWWmoREU6p}#yN<UzrOel!U-|VLj)i$iU>}U<dCm3X>G0#h{O%5t>qy?$3;lRj2aS*DSB{E*2Nv^cze3%RCpt)W'
        b'Ch++C$}TUXn#;)OMBd+zmR(s!k5>ei6V3B_;VOMS6eI`NbDqDJ`Q+^rKYr|MPf;LG440qiav#qVS%Kqoe10I$4V)*g{MzT~B+ioq'
        b'JegeHZY}rK4SAa82kN)UoM-8G;F-dC9OXWpST-+EuA6oT%Fa~I^ON$+&js3^rGe$d@^RdA1s?3jlR@)m8rLB&mIvy1`u&$MW?Ow6'
        b'B-b}`xjqT$J}STbJl({3WZAii^L%<0o}UKsi1K$`cweC$O_&$h2d;U6auCPMnFZ;7F^!c|JTI^hwgr_F&v_~!UBf)aQz!Sqv{2dy'
        b'4+Zf|=R9{@g~t=blfZd;uEO(35Kkg6>*w>XeQqc5a`tc@l%vw1KIru;2m5#i@9Wp+U4Cw3IlAJ&zE0-4^z*Cmj0DZ?6t1($eBa!@'
        b'Zhp{O5>(Di&NFYmPYxE%4{T3J(EPcXxBGUUE`rZF{I1BI^O;=Rf_QYC$3Fks`#P2L^nC}OG|n^d9e8GOp69NCN0yyz-fw@I@6!jh'
        b'<$?Vc9n=Rooaf8=KK&NV6B)#l%Xva7eC0$#IJUw!#$iD`-{U+96<01t2;#}(GMZU&WqI2cBs+6>Ib{{Tb#6}3x;<%k;GDaKr(1TF'
        b'a=s}JTpQ<d9-Ch|->(Ri>*$iey5;k9pI)V$H-mUgeBB=QE2lCm&^{O`39Q>vzGjZCWIXiyS!IEJoxuCxKr`dHjq}`e6`tfEo@JaT'
        b'{VF`VAfDx%r}Qd3vx9h=_*`uQp5qxW&qbc@%D{CY+iz{e{_5a7>ml8HoF{la4dz+Jc^(3uzg#0vFX!0<Jpa5#o}HZM#Y*4&c^kqX'
        b'RI=~qYy5a{Op)hF&hwF9d;E30>M}gP=RDe~Yv-xs-&>2Xx^&Hw<*mNV$AfX`Kck;9r^=_VtEvKdbn^pcbRp*%tn&52twH5%Dh(`W'
        b'5$8Elb$MG1W#_}k1LyW)&hy??cs>r|S;BcnuEO(K5YJN16I<<@r~2x^_UtMR>;v3KK)rrfbzomle<mbPwhtBu>8fR%XI=G`ZNB;-'
        b'p4&N3|5bRF1@Yis2Dah3>MQH2Cxdhq?t7r^^15Fi#0C4OWr2NwdnBl@-vgdBjn5v%Z-A|fW$SkA?m+#$p7Wf&43BKXia|UZxLjYU'
        b'oM5>|p8Mo)51M^)-MKPI_s$FS=YGulEz0b(#c)5Q7s{AnW_5eZ&nCyT?{gj<JpXEt`3pEtQ3j9)%SrI_v+({y&XaGx^7zCS1@`qB'
        b'E~B?!g{LCOe*1`*bGO+yrd!N`vNICoFW^2E_S+*@>9;@63#=RNX`x^Hq&d)jqu;dr1;YzLw(?}o^U_s#hJ$!;uMB1ME%TLSbW)Iv'
        b'PUY=6Yrb~b!M!-lTYamqod3xPl*x-hb;Er-%<G0*uifUuJ-(2u%!SL<?IYd?GrvPQ|KvO+-+||2&eQN6cs}7g-QR)d5#HB7_v`CN'
        b'ZVlAE<{(|QgO?Lk<C}A`>?GB&dAcIV9{n9JXJ(C`ZCMjkPLQ2=kn=Ru_-y05Y6AB|4g}e-xG#%7&;vDB)&~_q`rstz*;C`2a|dez'
        b'*ZKoNbIv=*A>FnL7DwgO?;h*>bx<3f(Y`Wpd^ELz_RcuJdz8oPYkjsJws)G}bJRyO{qC`?nSS?Zlg#nEN4;O{caQ$)62E&KQ;Xj{'
        b'`rtOdd+eiCwZ8VD-*_*-zge~!{qE7<+vInTzT5+T_voknir?Sxz_2Fbjp=#z37YSnIDUK%E3wJ%TeZi)oG&Y6*I5YPU5GpL#3PhK'
        b'+zTuX+(WvaKRz=5|NV2{sE!>Qyc*nH#GICgihXg%xZE7N#}{`kVKSa>UK0<xK>4_*CPAm1^*&aO_bNr=ImGK&z|*5O0@yS6yMOT)'
        b'c`y&`cQOA0ElR7oB$?mGgl__o)&%V%s;^SQ-VRm4@8CL?tt~hN*GahEgv&ooZE;PxsY0x+t0^{Bil)N4@`c5uuDGJAxGpGiQE@?S'
        b'b>aL=;tMJk6xUT(*Odjun;o|H|Ha<h0Jd3`ed8x-(vPh`$GS1T<lfjuJGw6Iy0y$~P12-mTt8xyvJD1l)}(7(n#3gCx;a^a2?Ga='
        b'4Q1$*f*^>f6NgTjI(0r!1soqD3g}csRD7I@GT5;1?>gt)x$k_mE9&F_ef}@muKv#V_kHej&V8Nhq7Td@TveMZNvB!yB_@Y*i73Ym'
        b';NF`Jj$?2?zF5#c*e!6c01=i+BEN=9OpY-tOo{})iw4_<Rw~BR`~!4s+36y0G}fV;wYfzKUds|eC%)pdP;{U_#Ced3bAD}@GxR5!'
        b'l)YP_$=R*c-3L~a3=9m0BVnp}TxCKf#sP{duFk3vsyMgXKr}2Rj!0oG#4^BUclw%?`Koxho`FPyGc1SuLnIZGe3x3?-j0UFmKqXE'
        b'79yWzh(PQK*`ZUhb!pXNQeKi|WK_Lk8N!n!lVe3&O{E$@cU3*E@j<fLEy$AdV(0{0@H@X$$QC_Qy&6y_5{C!!cEU%9kV$4qYanrJ'
        b'B8*dOiZKIqdVNdhiL{74VSz}Kq=cn!)2YE`Yr)bt$#VkD)dv!zLte9AN4F`)igsbTIx4>h7k@-N3K>Ps2}eH6Zm?{Z6^-jyjoJH1'
        b'9Jh5HRhe3nI3*=-v^wf!Dpew@6la&z-{H=@aCX|H*%vOgMwe;rD&%hv!w3nD<JYVe1Yol>LaBFG$dSiDLNG72atj3vB#C`PQ60FT'
        b'9(h3u0TFz*mYS|}<V}9^Uz#_^U?>#`OSyo$Qm`?TBGrw~ylEwoSX$6+PJ)uZhRatHY_^J(v;FYOga*SYCNKM_J<zg>wX9|>m$4SF'
        b'mr2H$?CaHXV&PKLwF32N5_VB@?q}uJWm#dUkkW@q5xQR8ETsz1ty201`UAv*83=MtCN*qJ-oPq*y%xOHBh{d4k_ecuwUddP5!#K='
        b'gsO>w`8+F`;H2aJTsuN~a^=ihN;oQntBY~xUTPJhPSojY?LasZ<bk9N6z0BIO(7&%<ntuO@DypYxDYcH;fzh~7W~&eEqrd#g;3yM'
        b'ga6|NsbMa=uFW`OY7%bCa~!J_5|A(D$J6x+T}um|Fv<jRUCYPt8ZQMoFxMqw1My_82Wg^Rp2zvrNg{|U*-;DSnwO_~`l6}=;zZu6'
        b'7<5LW)HBATxTjM=ul`Df-zsCRu1nSKiVz22rffhZv;hMTq1<gO>!l|pPlSmR*vY(|`0JHYzDc$>bFOS(-sw!gsbq`wMgr@^Y(W>_'
        b')+GWM$*k0D-F~0JLCeXvl4k4aDYMmik606w!F+w2*}4k;v{$c$o%Fgs{(#t*ZioE?*uy^dIbp9DFk4$rE41D(?GD%rNjJ`21_!On'
        b'UPn4#!2Wxc&i;zgY_;93*@s!7HU2qqHnR!wXPt)f?K3!NIl342k@uLbhmb$5U!3<F9G{2V{s*)*%okz5UuXX^?0a?g8(uJ5ck1l>'
        b';qO~$;QE9Qz`O<ZNqtt7|2f#t*<iNzeOCBi2y-)NjkJ4U9su2QpDZuTH-b*yE6<i-z8`c<+8=~DiS!#}`+Sqaf}X!uq&Eultc}PY'
        b'cG`O#K>ao#ydwSQ!tcGHvU}xs5SXt7F=-FLd^PC7&xr8bVE!0rSlaJ^`4i_AS`SP6H(-AXbU@mF4D-{VBhr47@-h}$E%ylfv_Z4A'
        b'0(73VSHawhG8apG2kZl&mu37xn6E+kJ#_{L?IRyUKi>m4&mv(jN4PJ*{$ia7{}q^@0v)cE<$?JP&<xo>Ct#ko3H`lL^nVKNGXwTx'
        b'cWd@@VV}KNq`x2T7r-9*jIh55`&`(M-!Izt2>NXv>=m-SH85+parlMIwInY@CxNj|z8=yHtz7o;dXn!L;i8!b#O=}nE-;NGlhMWV'
        b'`I?Z%zVNy}1Wts6M64jc5t_afBqo?@W%+!XT2y%}QXY^Hvy#k`PnoAobU~Xg9ac+0_;L|V*PfB}fYg3eEjV`<xaRW}?#8}wM2I&M'
        b'!mR#hs;Vgfs+MwHr8rr6OF1+c7gw6;?n9WbzG?E5*J=6dNEO5rl9B-VZ8Ey1ugcJEs9vb1n(n!@S6$k)C{ws*o}vZAL7oat%XEo}'
        b'3P=)t;^9zFC@rW($SPGuyvUmqy<C=szD#v#F^?h(x_T;w#AXOK6bfhfZPtwN`b#SmhGZxqzw}iUoj}jbh#tw!pDr5LzQo1faF%Ml'
        b's74ekK@#43u>47CcW-)o6}>Dsz6{*RMT}?V)f5|uh&JQmFEXS+%J#~U&Xb*`CLW;*i_+YZs4=T@%Ob_wCh@K%#ZZdi8RtTbxn@pT'
        b'*0k;z#WhIM1+^X!H?5S4*)5fsimO`nHBrT>%Jk*nl!19ca<o<HrjRis<z8M9f_TP>GG61$i&+_cph`$lk{=uhh>dAD`Jd<+k6w9s'
        b'j_&em{l$Z<S~&v2^iEpHqoR9&Yq9zgcLw-e<&z?dNIH+y<RJxUxfgWMq=H@zC9=*I)V$kazEl;4;Z=oU2=y$YgxJGZGkF7+E+6zp'
        b'VjHW)F;sAiID3A6i#X@?d|2?%e(%GAzx~Rq#2NpgtAviQV^<0O_R6h--~D4-1)uxOA#rYO9};}-9~u&T?hgzJKKEY?2|o8TuNHjn'
        b'k6bPI++Vm_@VUQwwcv9vzDDr5*Igs{+*e*B_}s4o%C`z>{z-Dtnk4v|q>@NsxBN*7NO9gut8k;ahL0%{KuW?wg$&4y$y%4Ns?;H&'
        b'@Re`4N83gBYr@01M6YT_inHV{Mt$_u?C7nrE*jn}1an9^47|5g$+jY0gbRf?Ncm)es8*)5yj&@rJVU#l+Nr9@S6M9Gi494R(L@eq'
        b'-E3F-2a+V?0o#R8fUAB_D40{kHT-PZtafdWO`A$}*eP^FX?`NDJutwfwTFT_2~F8D{X~PQE!7i<QkhlB_;{^zEqIzNKJn^A)kvNn'
        b'=DKKdfW+S<`(rUu5vX3GRbL?i(kEEWWM8JG*^y{Yv0&i(nAO01VS#GXu?x?rI^%A$Ryb7@Hcc{=fShUrkz`C$s?mm-MJGp;P9OP}'
        b'Q!i&*_On`j?yruPkeJ8SA*Da`Kv77JPg-4vDz8Bbt>d?a)qBX=DAT`fg@R`xCr`e0sQ^M~qG)5jSm6;J+Rj~gYx`%lGQuWr$no~V'
        b'!^Usz$5K)>hmd)Bign-nw7bFDS~bisBFY5xzR{R+(b9{AEY>Kk50mtM>I<(8Q`Oe-Ue^oX)uf|pIytJ<%U<#g%csuF2aR<_)6J;x'
        b't5!mK-@1%pC1w*^^zjo|n$o%8s6doUn#&H%<#_~zTn#*AeCMB&geKgpPmYRBT;`vY7A0i;kPziwzBbMp=;?&CdIzG4)T^e>A>)>k'
        b'OU%+D^A{_hX|oI38H$GjTBD0;GdoawZ0sb2x{u7<sbA&cfM_JC{DO;^NtX(vy`L5{X%P{cfN9xLx$Tl91qn$pL!_@xifB~0YJLfF'
        b'kS~n$iswnlfvr7U%NH#a^1rzF7dbbO2ui+Iu2Hu=Gzw|{9J3kt%0C)ARU2?MIiltndN$H>h-k%y6&Ae=N#c2QKFLZ7Y3<LKCsd+z'
        b'SBnQz-)bb0g0yoCB=a@tJIPiaCyI=_qI`1KnmczmEw5WxU88C^%BKZZRoKB#q2<b7d(r75@GlVJ@}L|Z>I;q!dRqT!4|n=SpMIu9'
        b'TB=m4Y9>@E@pW0R&=-|6x_H6VQNYDP>+Ug=P6Hu0N?RQBwZVW8KPr?)Wps^@YSiTQ^4V8^(OpQ8_3$QEU*DIllA`tK#jJi5h;RuK'
        b'e4QYK4OZ*K|E6C^B&H&(Y8{#C7&5ArtJWc{lYw-tX>+@N(_!~DEz!PQQNzftq}?HxteN4-pQ5(KHEP52d4+m967ET5Ex{GO22U?V'
        b'^lCD7^0}(BRTzs6YqhE!S{v$_Eung=BTp3<T&3!$*rc8w@K&L1to+s}MwceUKjZKrEgPSU)hF?gsXnw4mZ|;mR9f71YGW*Wk0Zn('
        b'r$rU=kASQxd#>Vn$fJ?2XnG;p8|GJw`|;??{f9@YGRmkM-8k<fg(Px!p|v3i(@oL`mS|XPH}pfE67NZbxpE3|;H&AWqB5#mI$C(}'
        b'qM&SC1ciL$_%=t0ku*wvh@mUmfRxt6pXYE|IzE55q_W-gpVn>HiapJ?YsH@CscXfa#=K4JX_jsidz#JL#GdA>+r*y6_z|(E34KKD'
        b'Y3}@p*wg&%BVtc8`#Q0wS%00_)7*2N*wegro!HaNzh3NVdaf6Hnrp8YdzxL>i#^S~*NZ*P3)hQ1&3m?sySwe%#ogVjw~M>Gk8T%t'
        b'cVF8s?(VkSAnxw=-XQMo-hP9)yZhJ;;_mL>ZxDBP9XE=*yPIzmcX#*RDDLil{YG(j_pdjKySvjrD(>#C`>43PyYHjo?(X4_io3ff'
        b'KPv9-Hti61cT+pW-QAmZh`YOY?hto(pW7ks?j8e@Uh~SE%+?w@*S$&H<xSos?()(ekM8o`c$2ux`?;IMUEV+3B<}J~zggVnZNFLE'
        b'<z0WXxXZg8*hc&=z;@C{59|Q`7tlv{Gl6dtkIyY;>!ozQ4O|JVzlHQEquqc)NqenS*1izfANW8lK^Tq_a!rGNF$??o$1#5o$yJ6M'
        b'zbViBs*Ez`53J?#L=Ysb$zUf77oFzkLc{!AE0rHn{6gTc-X#&*z@%bC@ys$mjby)+BI1_<QvC@(f0t?wu}ILrnfc{#_b1~0vaG60'
        b'PckW8!XH?lE~s?kuLOTEEWQC}IEr_ER${TJF5!)632d~Pzc&(#1<3<%5Pw>RfxkD?8VCmB^zd_c=}UrU7!{f~p?^@oCIOoT1O%)V'
        b'&?8_#zy<**iF{%3R?}>8n)OgZ_0=uC(^l1=<m34xA(G?b=SQ%9@hM(dYE>J>PV&<O)kVx_A{g^?=@6=yuy6q&qA&S(dOs=OM(q<J'
        b'^g*aUme@q|(XAR^*p6E@-R-yCs_Ab3#I2g{_KSCEy4&x&Rny)6#alJq?O(lB)7^gPR!w*N4{p_TxBui;O?UfmZq;<Rzj3RkyS;Fi'
        b'rn|j-m!`XY<}OWld+jbwce{O;rn}v{OViyR+NJ4kAKWG8J^J0WOViyxyi3#F{@^Z6cl&`|VjiU5w|0rSkbd9aCFVo={dkv{6Y2Nz'
        b'E-^3C@2|VW+(^Ga?h^AO{r<5_%#ob;akrQ!IUnC{F<0{MP`ku@$?rJs7IP-&?b|KpP0q)+Tg;vGtJy8)Pksk#x0plu9i81`9_1Wv'
        b'yTx3}`Gj|i`ILTBc8fWc^GWR%^D5^9+b!l+&JVg<%&+|Z*KRS#(ywl}m}mL@rrlz$<?N}u#e7RY&u%g2(yx2Bn0GmE)NV2NaxS&q'
        b'V*cghaJQI)>37F&F%R?cwp+}_^!xg5F(1?K(cMD60_P*%Eo3av@91tJXMuiy-YsM;@V=Y+#MG*98yrtgeRArtM+}b2@|yD3zG-kQ'
        b'Eq9d<1DBU~l-GUB;JB>(vhuwL4UWspd&>6#gXO{UAz-LHT5dzQP36~cys7--9PcWBfaAmE-{Lq@{xrvz%3tC5=km8Wnx~yUjqt2#'
        b'XH6?cdNZcYn06lU>}fNnS%9;q&6*YgR!ys$#!${*O#8*O*I*xI24le}{i^H(gNiCY#@!)SC|q<*b(X7o$e_9|=umW_bDUKHew4oW'
        b'o=$goF)19p-E2((p9YehpO4<I@c>8Oo5{~#{*1vf^qj%b@SOOLnv!uwb#Xk_@#CoXywBPr;&?2~Q^P#9%(IYr>X>H{^DJhbdgf_h'
        b'o=f0G-tezMfEt9TL691RsX?F`gsMTX8icDwxLQgF;c6E$mxZ}%n5&k#V6J1XMa;FBx$4;hwjhN48fnncvHnFaF*#D8Euej%ZJ-^J'
        b'SMWB8dw~bY{HlTD<G(dH?g1W>{uRF!^?Ur4Odez@G@AKCy-7c<nx%T=NSGAt!mTe5sqSH+WPD+*U+>5wy~+8@dV1H*UnaB}W1?4P'
        b'E>$d92`oT3B%p<+k8HZonnw?b$vu_N93@}AOD7aw%Q-7N-+||b*CoRv)XjsRKN{ayTVWaOl|N;HQjssE`L*-vDl18+bUxpl%*8%6'
        b'yW&`BtPk|1tGR4E&pAp1FQzhgu2L}&j;7+Ngg;f8FT9kqHAkt-Ziy(CMt(XUK)GudEz<eWo+a&5Q&(TtuyAo*y)Hl?h5TfI8Vd%x'
        b'=7r@}fH(wI@4PL7g%kPl(qQo*dP+3yI&m@$$4ai8Y|9oUmWX2qnN*fhj5*0AbAn6w7HWyo6iXxq;(Rk2CXT-_iC|VfWEq?@Sf$Y4'
        b'56?+XVx#g`UCokl#i}f1ao*jsNN~yNA(EBMgfCjHf{NxBUa89YwUtz=@#E6BwTl(rSz|RqW+8I3sj1AYY&*$tPLQ1Qkg8E-&H&X<'
        b'gbIe%4y;?kzrBeR(Gt`I6rzH96#dGXiRLP;&0c?pe`RM!d+X{-%31Hg=vXG4s-_x@^F)bENfy}>#XEq7zQ~kvlqcIgw6h<Gl9F>;'
        b'9#T2bOGu3iqNed3hdm>quC(CiWE_)9PETgk)Wts$a`r?me}103A){fklNO&Ab&+yX?hK{XGU!X7%wINsiJHTMLbce2kUS<xjFA%l'
        b'_6<&=1ZGyCwc-JOB!s7#o($O`uFg(>dxxvtSD7~#@l;HxK$yaN=jRFkPgJN^pLueuN{yLFZg?%Y9OiEM^+A=Hy<tw@Ks6{Qp#G~x'
        b'dM>M&Gk~ErXP|Q2;OPl&V!_kX-Ppm^Qj1Y2hB$@BB!BAQ{He+pT5Umoe5@)~5i=yUo~1z}8cH;M^hdC9^@o#m_#|dj?oy>xBvXlj'
        b'o|KXfG_R7Hp)&vE(CN&Y9E8I=&jXKmC7<SD@KXeC;T@p99EB|vibOP9BCrujMM>PIE=Z0G3ERwwM6->~Kg)^$w2;s_WZ1Y?3C&8S'
        b'#nhKBJspu?SIq5e=`<tSllJ2u_!2TUIcQJ5m`_ErN$jVIvzk9WYC^q{fn=X*p=nk%hY|r@iXv8Kf(VqZ0)5dGx1q|ucK%~Z^t}&S'
        b'emZxj{lyKhzkmJuRe^`vtRFOclxq+C(YgDKW3PVZx#xC#CGf+2-wl59*{7emZtz!=hR^%UH^14+mvYTssV+dAHe=KHF@snm4_<6^'
        b'I6)RrIq2DWM#o9etDya$VNf@yZ@$rSs7jbCK*37HgIh6hZ-vn@2zqv|(NTAi(NP9E3bS5@!<GfYZdstY(<Pyku*a(r*CPFEfN*;r'
        b'ZnuH%2hD)}HPAj8rnTDWn8;10f#h0$yl;~~mcolJl;Q_O74y*M{P-!9s*>Me<}afV<Xg$y&gKO)E@DyQ`(1z}7RY3<5Y{Ic3~k_v'
        b'@}s1&Q{~>3jA9YfI7z(phhxMw>`#9Hsvuwb<bV+KmkHlWo>?@skus!nkxS4=ON<U5h`kqN6>U&rT)~V6He6dgnHh~}&=M0iM=+So'
        b'vzcNr&o(fFX|~a5o?XZcMdqsuidk8S$-s<sm{Mdm8f^sE5ctB;O<i6Gb0smRlgV(e;*}y+H5X@SL%1izYHAnOEn2K|Z*n%NelnSC'
        b'D?+5rZC=gX;&w8$8cj^`ps%yb#TI1s0iL-{)DMB6P(zYjkWBO}NKyOr1bh5}o_=%<aYSHg?C&2K^sftV2vLhC`I#h5!d{Qt-`r~V'
        b'w)mUuO)aikPs?hrzuE3?&B-hfkNXGWbaiO~_D$&N0HzJv1Yz}pgxb4WTbb&y4&5)mgZWA0DlZ-Dk0rzYNGM9{#D%pv8PI*JNGuSf'
        b'gE{d+;?>bPW8zNsA;*49$hw5Mb?v59$R8c(C$~D59my|wF#PgM97hyM49;}<Cs?F#us6f2FF@@qy2`>beQFmi#vB_BW8Ta4pzQ+-'
        b'$MA5hqcT*a_cwV<BR)edSQih+kRO43Qdn;wg6VUN@R-(m5Z<7>dq_@r2Ve=`yUw4A`PW5aYw`HOg@nw9<9%4|dt9AvPm8~;!`ap9'
        b'^0(Pnjg`KL;qOT$XiqI|m@@|WQ%@(~nQl_`K$feN<Qoic2op0Lc0jeXN>uIWRZ_#TIC~nxf^Pxe#wQmp2uFJ&1Hlk?qtp6?KN6|#'
        b'W2%u)N-{m2+%U85E-{{yF~<Up?Y@oaaR6figD2K6&JpN68j&to=~iqA%5}!vOI=M)m$wN|ncv%D?{qmU=g!UV-QLkILsXtBcMOz-'
        b'pT5&k&n7nn)1`))7l#K>TRQDP8!8q~`Zt7n&=jF$k6(O-W5kmw9C~9Iow0#LkJ!6nM7z8mf5(bbm5BdQdm@qQ;V)?_92z}FU)Ax1'
        b'`a`_~7^gk)0W1iS@*tg*Ef1xzxed9U75Qr&j`#3~PMT@LiTBJ2GU6D~rbf77d!1a*WH7NtpmNYKA539%la>XVnJV~NuhZA$U*)s6'
        b'`kOml@AubP+VW;DzT=3>C1XA53L;Vd$R`;q50+m<K`9?~VZzV;j~Tkf^JeVMwr{{9CZly}sLyIn^FCuf2y+c?2*`OMW0BCT@d~JF'
        b'IO<{JCCf$j#|1-yBA&aMvzVA5<@6;xJ4jPYBBWO6{@aa?hOPCsuITz`Y-5xa8Srz`l3n9-CH}!=4Es;!<u^t-S0ZcK=pc3TLOCB>'
        b'8A$c?33H8({ax>F(Yrf3UG^1R!*)Vi+Ep9R-5n)k8~+5O1PA)#;wXT*`GJFAt<Y{qW-#iCZ_`zRRg{0G##@x$+2Y0&?Nh=@N~;1?'
        b'dD<j3%{VQ0(R}}Evd({F5uN|uqOGK@gix%h`+%QFa|8rMcIYRes&Jzgo)lTpa6)^vwRI^Nrsx>KC7L&>K#!`novY-M<v|(fT_`o{'
        b'_78}3DjCfa3e%nr>hUE^TuP8!H>4oi+o{Mk;}Vp^<!P!>@LR%@RbZ{nv@XoF)}^hUCWZf)$14qXi)yG*4YjIap=zj84U1I6V%1Qu'
        b'8X8o?CFuk$s-Z?T)T)Mss-aFbh@_d<-YE>ORZUIyF0YFWm)f1qPS)yhE$3dXu6Cy|G<9^f`xN>{_Vky`))zo8gZ>EmJ7^SCyw7Z%'
        b'0y+nDA*c$p2(%2e9OMD52CW6H2c<wC23-fb1+)ir7s!>K6sT_oqGFlFIal}uBIgQNrH>NKoJ^QAHb941nu8W}J@yKrh|a4ihOH!x'
        b'BVu$;yK=Q+bY`k-45rd*gHfa=PnTs}-x}7$2e^EF29>pRxsj{8Q^e<9J_Jc+1s}elAah4ZNlwHa6~_XUKeh<;MVjf{nnRf8TwIe$'
        b'D;`wh<_}3LeYUPi7mBO-?g{WxVk&g<MT=w8WuZh2qmnaFk+g;lc!bs=_jF?RNO)b87#BpY9;Y2oR91!_ce4}APT?woxtsHc(_AT>'
        b'uhl{P^=UI6>TpX~WW{TiE|Ex9x~W{eTFPod84i?MUpS@9Kb;ym>C%zDX?s)L;v|&=@frcO0u~CW6R=3YVgdC|p$lNnm(A8XP&>#E'
        b'+6>wW`XcCY(A%K0hs@R)plZ-kP#eex>I20=9|HaL^MY=M`A*QophrP3fqn;iQ-&%1iWZh=ChWDK<<k8!U|1Js6U;-P>p?ezJ_gzg'
        b'`V8m+&}oxSo8-W}OKc>eC2R@JVf?gg)e-?r*<zjF)X~}5<?*?k($?;Cw|CKXbgUov;+Rz^^l4>btv{tyDsftT_tGn5{<1(#&Z>jf'
        b'kcm_*DHcU^-8&iJX8ImRpV~-{&8b$eVxdkeD&j=ptfGDNeKeG$R|VD~V)YTE&kvd-U5;<<Xj(yQHZDh|VhlgN!mFTU)kApNnN>2q'
        b'ixn-^+{~Do6G8}Y%ulpI$PQa$v9Njb=D9jMJ34`iofvrW%2Ti0@JoVNf#L;~=66?_^XYSps3x73h3Kp+?GWhUtavQWSHo^`voM^*'
        b'`Y9k9Q}=6;<RO`KhD;LsI|KGKMpn!UMDL<JeoSzD9an*#Z+0*D(-O~T_pb1-bo%^0cbluD%jfr2DSQ)InHdjn<O))Y=(mjJQB%q2'
        b'%jhYF3H_0KZrURb`kEZ##*#0DMVq>Li4XEh=keKKkH;gDc@Y~1x>1$zp)6wQm+kFF!F0Y<K5cU#m&yYDbgCiG0@AxAzOSlq`MiGb'
        b'YA-cVC)%rXxyxtqyPV5ies{aC)9>x*>TGf;7b|=>Q^gm~+@rbGzTEHbw6`f+6wZxQMW;o+aL;;oGSR}{VOWICrG-1+m}0kD#VeU}'
        b'#FnQCd8{7Vdu*W5;tioDyfM&r?;i*aguJwy;x{PZHfEoEkb?4#$cZ$6*}!0%xTTg{83+q08_E~~TZMuk>B|NL3Rh*BQlWG?FxGvW'
        b';vqh>SVRw_20R=;@~GGl!^1bP5(8{z1!BYpgr|DdEi()fp%1~zz@Qu39<Tb14$fmlUwW$OGu7yWYHG9+j`db3JRK@G%a<P}CUVwS'
        b'nDSC&Lm{L)>exhjsu$>ESMua?vcNdXjYyw`b6jOLH&BYcm}tlRm6W|g{iLsLPN#Hftv86J)TXpPPhOu2B_njLk}rMP07$(?ml!>Q'
        b'cpAO5aKctIL0umbyYHNIEn2#R^sFR(F&ceZ_oQ=+_q5RVHEUd;JGAmt4|+rWfp{Ng_Ugg50qg`?Vi7t;TKZ2$QmfJ=SQ5!5p5zKD'
        b'7!S<yH8(#G6djgT{8M$=n5D^i9%wwtcxubj_>dPuE62!57iWS4WY8V$3(*(uXium^-NlX3mFggsh4^=j&ka1VlMBOQBBs1`*PMv;'
        b'W6#IbDM~h*FR(r<ptLQ|iNp0-g?qfAXi)WtCpNUlQsLfBxwC3c9O*(C@}5F=1Bqm2hWR~28cqBfOFlO-S!ViliX&Beg^oSJ)7vho'
        b'zG>0IJt8I2AT72QDXsHp>DQn>+>Eb6n&^7;rL_G<bi73?;`|8^-6_NLq{Hx+wg{zre`8z@ii5pnOF8?Fv{?mHiR!s@X$2Nn_08g^'
        b'ROXq8Q3gH@i*rM(Qi~BksJ`RHb9g!TyCUc5VB&G0!N#?3hk_KRm97@^aW6EKcl5gXZLp<zMjxm#cZ}0Cw`8nY3{{|9)OjzcJEn{e'
        b'y66@K6#(Y0=vr~5gZdIpj2C&w0PkCE2IMcF_RvObhhhoR>25`)wTrZD^3AX_$9OE?Q3O63+CzhUx|2nvBGUGNm#~TR|L`Hkt2n4m'
        b'k4=utvyXPKNDoCZn}w1sp-50ho_Wg1m?EOV(4c%NSd|*hMLee5jaN@~NoN@0_HZc3_sy3p*)gx6!e3?SYUP7vE{zo)QR^xi9n|2M'
        b'y*H%ift;yz?5B}dmfAPEc!Dd$^{cxeH5gx_CjC8HQ0$55b~MApks3%uMK8^-p|@dT1JzX>6rBNV7}y5UyL^@qb<<CE1CbnWK1F6E'
        b'gne;XO!Ib9KPe>_h=$D#Bi#99(Hu*t!<RdDhKLJ>^412t$SH!YYDYBfN@_q!ku)~)dHor+ikI{Hw}jXAA+%Z!{*1MG*u8mvybNyj'
        b'8V3#5^w`gwI8g2;PnTL|(u0fnQIy0>8-(<elG#ppAqWRPt5A1{Hxqx5)0S3mIuL(r@z&B!?4EEmiibZ&<DBt@4_5LXv}`Qsj`BHx'
        b'GX{<`viKH)CVF3gLh)|sQHKf>X_1vS$b5;wT`;W2%q6~od#U>?w^OE~zLLbJQ>ve~OU2A2_aBK39&rk%UWRW{HA8D&uE99nI!nj!'
        b'@(YLDN`0M_8HzSaZ}K#ess<h9v*!`Pnqkj}Dj9W@&wi@>3|Vre^Ti*ld_`I5WXCtZ!}N^r&|Z*Lhisv?rmTESS>-inm8Brd-*k%h'
        b'F=e%_IV(O*p!8uJ`}klu5$N{^@h3g?2KiP#_bKTM1>*dVzbC*s6;6>1mU37yh}4w1%EC&qey<=8ot;ut4<`5rHhLQI4wd(=`Dd(9'
        b'Lf$(~l45fnBS2@~vvOm@nV&aQo+>8Y5=%2or>n)UJ;i!-4l+TV3;*n!6TrWg&Y^OhrC1N0Pk*KdwVF62A>IMrko4syCxUQLIfGkV'
        b'c8}ldzAQg4L1tg6ACI|1ILO(nqXYeZvL`jyrFvIytJ~}IyV^Xy)fIEqPegP*jeIM4q@+KPNCY;ePn9zBV`?NGh0Y>F2~1;`hp(s>'
        b'Ljr}+JJQNOZ#DRFjrdUD$J+sY=^sdiBT4baSjNYWzeY`XnUa$k6Z~`NdcW%D7atvxQjWP)Ph?2Tw71pUh@mX~><&HF$cE&zJ_J8T'
        b'cSH>G*>A9sHc`!f3G6@A*_XinxX%7w*q_kZNxkZmjb*p1bIDR$+3im@9_tg&YuW8f;r}C^fBJXyjBZlOrrvGy`s__B7C1ZYZOplV'
        b'&dW&lDM5QjyWiPn_j9jKUlRezasQ#&YAR!FQn8k#h1@)hO)l0ZjQ9Rf@b8t*KwH?PTz$9|6lcz94hmPU$(5&{TjpWZg}s!*p&oko'
        b'zU-r`>~RncZH$E1F5oJ^<+*sqL*EsZBILLXA?{706lSHjdMVwWpO&S4d}ooh;FR1;<eJ|0ie-&Ig-v!+o^1O2`2od5LnqW-s*Fdo'
        b'rl=3UN+TZ@zWw74{%9<^nZ8Wv&$s>S#G--e&$!c$BA#GEjc!P*WoEONnjFekjE*Yc(T9LA9|yJq%RmiqcP`cBiF;t)4)=afU|on-'
        b'5Y_Y*x}vfg6R|h+L9x55AnB!Ki{+fKB5%PT#yL#L7Dqx@wcu}}x+fmzl@BEn*bu>Y$r8$^O?WR^LLb{Jq_gC4n^%?olA@U^St^no'
        b'ldnkfW2i_?6Nvcb4JO*c=X3W<M<E<M$X^0$#rFc!PS#xvDg~8+%0V+g=YbT^Y)}QL3S<G*ff_(okPYMnwSZbd9*_^T3Y5)58i89J'
        b'lmZQcwt$8}+d$hvJ3u=@w}JM6_JW2%_kivPJqX$d+7CJaItV%hIt+44{eX05?frDu4Zlu_UWq=5^cyeCwry1QVy+vNi3_5|LcJ<x'
        b'h9Sv>t6R6I_e{4>FrHBtkJ8vN!FVQJJW6Bd1mhL!;t}39!FXl5c$D{^3C2@&@n~JPcY^V3x_C6d4o@)NkS-pri|?6WJhH0sD8T&_'
        b'jc3&2(VglCCmPSB#UqyCeG`pWti_|d+WRLOuS|<a@Baf6ji+ew=nnY7iN>>O@#wzzp^3&D(&EwG^1~C22fG@N#_D4ej%Q5Aqp*)p'
        b'IG!mTkLH;p6OLD$jz@RlpPg{LvUEIJc051fcuG3nG~K?)sMDFF=V2|D<9L!BU!}6&PnZ2sCfn&uS^jdF?&yE;M`f#(<)eG+^$nNQ'
        b'U$W%A4W>N21Ic(;zN6Ee<ecf81O&zs+P7oXGlLmD?dtExiYLp7Upnz~sX$pioTH8I&}6yucW$n;xO<ZuG|LH#k}Q{KXpmO=f&()a'
        b'7YnX2R|;B7h&#OMrXu}eo--u)!%2TK5Doc7AeD)!qEeqxPkewDg7a%wEY*h{PnspSCe1)gONt7eFMYFC3qVPT+nc=u(Vi+rU6U%h'
        b'@bWW(?iiQzb&!|F0i0PRHnU>9kB0mtu&KpG4C!=X(C5b<qSNPc(vn&vIg_(_Xyp`K<^HhBSd|p5f{kD_=ua0`7eO}HJBUH6VR6Si'
        b'$p;x<LZbV7d!i|9=fwA7`ryHt80pp%XIJTH^0&2h`8{^dP$2GLR8Z99<@7fiyP`7B!Jjq+MCOzsF<Ix$na&CLmzP;8FQwQ5a0$3_'
        b'HxP)>Kqa}`NFYu-5UpnY+)?kKW|Cy#7;T4%>7k9TkhnYi&iYf9HkLkx=_fC`B@&LY_gtWyf9`p6X3n~Bb|gd(4)JTyb>mQUoD@0F'
        b'Jx?_d57QPaD=P6NtQ|<ITMzLpiU{KA4n=zso8qZlADvy!5PaW_9Z#5ZjgW2yeh@Tv;dBp5l0PEEXF~lH57%fOVhgn?Odmp$sYJA='
        b'KVE@-2wFJRS4FJf^Oup44gz|^gSjqr1*S58Q4o{}S*9?*B}vBzPnIpfBflUR+OR-!l}nj0&xkuytDe#Bj~!^lUJLfBXC`*1O#h3^'
        b'INO1Hv*JGn`%%zwQ0cRoezTv=&1*lxY0RJL=TeyyBz8@j$mRrRPGW7&Ma<h`uc1FgwY7B|7A+=N*uZUzYHHbCF9<n0HoRj$@q&=A'
        b'V}W`13qtOWg7@x@7lb^X^I*RA1tF)W9OkVr2>Cr_HkNU;@z4DJzmET}{tVi$z+fmUFdGa;qp_gCWHJ|+3QT6EsJ{yODLKFGWtl%y'
        b'`X?Ri{AbAX6aEhVGv@h`ufqP{_+23Np<gC-PTvlCnAW8vH;LAISS(sV?FJF{JQ?RbSvZ#4I}LySI|$$Da<%&uaayb-2YQ6~O16M&'
        b'7)tVcb|kDiNusyrw=Z8%%{?U3>3n$^XMQNsE6#7kp__X47GB%4K<FnTNX3Y2j^yl}G&*j3)9APZ^g3t}><d9Jp1|A#{N~$6N99|X'
        b'w}2mcTi8`1_p#_BS^f{bo$G$aTjQreq~@c@@Y(t2OM~({LzkyMe|>l|uK-;GszQC&g6;-=7xo5(|HVmxlO>V)`cb39rWA1cn9fY}'
        b'ex3ajFz;o;d^_+yY5tj^z;Sc}q)#`SUMdurG8Q;4D-d>-vcoDy&3tr9reEE3S?;qmw=bMCe%{&nhqCgYBi(vszIKV#rx!T>fc#sh'
        b'X?~RdIcTRfy8OQ?^Cx#p)-QX?bhkINaI}}T+uK<*5M>r|-5A@az}lW*s8{D;cQiR&&CGWhTi)hlb80M?&%f9*{}TKB%L4N^Uoj`j'
        b'oitk;$(@K+>;AF@9G2+*vbz@*IF8g7IDQPWEG%$*5cU{o2FMC}b1~Wi?#~0ivsl<wBKNWAJ6Zn!y*Sr>#lrE^AX4*LBg1FspDzu{'
        b'YlSXPeg69JWWFBsEl^)wf#cJlpM(AZdkW#tT`X|9Br@NANr7Y4WrFV2nTY~A`vWjPxI~!m1Aa}KfB)VB$FT{JKHY5kvrXW2)&j=|'
        b'mI}K{*<meK&3t@Crr-NK0>kgu+`jJ{Kkw}P2eR^CB;5vOzVDaV)KcImXf1FAJ2XGae;(Q?rOW?GnLoLo^4W>fHSE+T)*fj8x4vP5'
        b'WDcfcbP3$?Klv)-8TDiBPnTf%nGeZO{IIG|`iAFkf9UDG)`j=o|Kkh)?!IK{eXl#;KI7inPu;%bN5$W`d`?sB!C*z<W0Tm>(fUo_'
        b'vp1a;H9!3Df!)o2d$aL(1sx4-wdY&jY}t6tW!7&ex4zUdZ9t@YOv;s;El;CX3$)!LaQpWJe&9IAp>5T6!Xsz)aNPEj+c}1wc!E&z'
        b'5A*f?s~cMC3Gcq`oPMC~H+wC219!gX@WJPRb#wo=zO+d#CmVkLBP;7RG_l9p*Y$tr^G$5&t=%uL`el=C$HRl?e`%W2^QT`u_wqR_'
        b'oV$M9R`{c1L(ady@0X7n=RfS+|EZsDY8w2#({X))Bfbse40HrE1@<#Q2d*n{ya>8udx69J5sWinV7suZMDAlzAj|*e?YZuM*fxF|'
        b'L~1@Kw~6rC`R7Z6@*?+}x98@s4^QTcfLDTwQP*Xlt3aQIy&T~mxnAIJuNOpS??($97554X>dZvv>+E5e<2!_TJ#ecufB7cNUlSmG'
        b'x?|C@n+qJ1Z<$zFqOBj#w3mKTAls|CefG|Yr$_lu&&vNVHwib(&BA`V#HV)^IBrD#mQQGYl>e`8L>+Ybm&-OJ_fySTbR=$4&&K74'
        b'{vy?oc2W6pj9OrGp;<L#1uoW3v9tDb#>uA1=0d~dv|;k(0vIOqU)msk=3=-^E`q5<^_oO3YGCmzP#uZ|r1L61#jgnejT{P#ii^y}'
        b'+GbM*FctHSA{h(F#$AL#?~jcr{K-%ZGdUL&|KISN#Q7)+&~Ii|$coSxC2SI#%u3m5>~wYpKcj!(M_5Najx{Ez;fVsrCfGNE6p#~S'
        b'c&fnB5BH--3LGOxgk2?aAB!lg-v0L^x$fR4#!rJt%_k_sXXl?U4a&=_%Tu4fK0KLk0sR*!{v@7R&?}%q&=!Qh@QA<;No4-aGgu4!'
        b'QP6&!nW$f9|2oWvo)zXtfKN)Z;kg1w(F91J?pSm)!d?E8iG?Nl;m@<&el4)|WzFrse>?H?DF5E9{2kJ5NY>#>i8Eg)a6E_nxBN=;'
        b'qx@^pPAhf!2W1<Q`>EzFPlwk{GTNI?adz>)-QV{{fn)fu1wtR~OJ-}Z(QG~Y+*4EL*D#u=?cOH0dz_q3<)3*h_~MVA65^l_O~d+a'
        b'2z02CoiPG(+t?33ZiCszyeD9uZfAd7V28V%)vUEM?}zMc$&Ge|v9mRwf!~+x?5czCAF;FHA0y1K?CiV$jc_OI>@TSIl1UDBZJ7h<'
        b'I9U1l4z}h(2fMe@fixX#@nQ$N%IaW`IvhyfaW{(dCh1K8MM)n3>ByDe9=Tou5Xssm8UIg#{zfvfK`&7?NY4Pt=OLYRB+HsO&}9GY'
        b'q}Cx>;F4E_4tYKg`Z?*LBN^4CdzSPI&?;8uP4cd((}=O`X<|*2-%qK9NjCTI<u_C+$1ZsW_78cs^#^JHvMl#~Bx9TwwV-R{_sqY^'
        b'bRLm)+y?p`@lMd$ILQE~b8V2Hbl=JHlRWNQN$-L*Q#*O3`E?n0n~d{O($6c~vqGN#(Rtc&dHy#l>rab-J@UKnpXl4F{Pz1%d0t50'
        b'Vf$rV!o{*YKazd%L)i}0cBGr3ndG3;85-$rkY%B^BH88xGR`+hj<{^6-;lg;(ibS16^mqj-XMJubp9vXm(n2Kr4usEFUvCB1iC`5'
        b'RW6m^yDhRDCuO?pWq%)&<vu7sr+-4W+hW;op9B3`wlR%|D?zV-&Xwth<hc5XECYQPA0}Qu`6>P;*{;vahm6KfQr5Xfj-Ns~o~f)q'
        b'kpB0BMo3;e=vT7LG@f_JvJ1Y<V`!G2)niMv5WS3{<GGlz?;`0Vvlu&!ruZ)u(|MLjwjuS&uR;rEZM}H2wP;QG!nvQl+WO5O9^1UV'
        b'C@$@{T00&InAbh{Qsa#IPTz@{zia&D->-gpa`I2o{w8(f3hH8S>Jm+8292TD&DH}TxUUTa1)ne90shTwJp%W~Uf1*-@ZWn(j&e|$'
        b'L(u&&AF`Vq+kqa?>voM_Z^i{CN7V(nVHL&XxDD=opo;ilrx01!%dac&t6Azz<YkIQ+#bvd6(8v7l(#~2Jh(U;apx@4Z$M{jmNG#r'
        b'a&CatDV1Z$<C2o~7D(jR?eZ0BS)M}iOQ5Jo{utI=cV8eJ86*9rdD3qtmhXx@)!|p9<%K3x*D`2XC^<{{6%grXT{>n7ng$Y7_;la2'
        b'3ORgPz19{;U+QEP8Ii<o&#~LP7VRw=@840pnsmIpjghxXycaIcE;}!De9)cra?#9LtiEG3YTlm7*TksRJ8M66=)RK%WbZT+7VnXl'
        b'%*Gw9YM`;l$2&`Aj8rDr#&+>-KmSM`EATsd8r4W+6?CvuwC%F=ZB=Se(e%Xl`_6`N!`MSu$mDv5V|bnr6HtrdOJfa759_h6Zda)H'
        b'f#+4Kv%y$RmM`o$EtP-dh@uXPOT%9Eev7nI$&h5HyM4K%tJ&{c?Ge{U^hvO|s9PS909iNjCo=!%eV&vpV@x<|cjYSp`)A%Zbm?}3'
        b'7Em-ACC&!*uKb2wSKJq)TXfPYuj%On^4sYMu{@NbIZ!<4i4FY5CLfC7RMIJL_0V-Z1Se-FUUKa*K1|42J_O{WbET`46jqC_6;|g+'
        b'5+%rquAOg8N6sh#$+d9EuGAt(S6x;*7cDE*QCDkupI+4kLfW=cq~W=mt7c7J&cPoJUNNSG)nGpz=JRmGaT87uQ&u>^<8a*zm@Bw1'
        b'qoCTI2cEECRmt?>vGpD#znBzBMne%gd;7eZ89r0Y44(wuR>TZ96*1#Y#mqQlWQM^4wl=b!>x7_u$!t|z&0SuX-_g1v?`<kBXEQA|'
        b'liN7AU^qp>n(59INu0%_Si!j;1z#iG;SyYZ$;*)mzu=_ISH=q=F5W2%)X7h~@vxSZqH*C#LU=35-V_QkvI``cDnsk?cuBc#tSZjB'
        b'Z6GIT6=)4;5VQrf2ecP-0CW)aJm^KxanMQ7j1RKz^FR$CD`*vH4QLR=g*h?eV&fu@$slwQ_}g4<X{)>aQhTf0>9=<-&vEnm>^@hn'
        b'tNSvSE;XOOxudJync?E?@_0Ikc`@xOMKR?h)(MA>c5iMjO`T0SZkM_`z3z_o9QQVRQ)YqO?QU<2F8B6Jy?%#XmkT*iNCfn`k;Y|N'
        b'f%8-gu40CEd)w^3rj`t!PM6*3=aTiaQ*pI-bS-c3dp-81%<R>|x7*wDd$icw>3)1>Hf<f3x_EzP6?lbfwcpp#;cx9|U!LK?c`%!a'
        b'<2GL&nLVucX?3+P_qAkIhsz)1NqRGU5T(mCR{ov7F`Bd8wNmZUJie=ZUNl})XTI8!pVKwAUsLn)@x1aEhi8_5^vV_<f6Pcpbi6C5'
        b')>)qIK3BWX?{qgeqske6q_AZ<&wjPXryt*4t)9$bOAh>&DK)jjy*$Gs-E$oni(E{m-q+dXX>~WDxBablhpRQi4=v%sGvjjR@pE+A'
        b'+nZYaBu1^H*$>NdtvDS%duI8_fvWDNYEYe<k*6=i+v{p|HBlorcc>-K@aHa6%&h+7aog;ztw^DXhE0Y~XGd$R!%hP7a$}|a@(+6c'
        b'vSC6ru(0@>+I^Yc<l=XGGoK^j)9LcKket)+>Fm(@qp8E`);|c^M9|faSWZ4j93;|D8wyT)8y+ktpG)+S-Q=9v&caEEw$GT{g-3R~'
        b'u5>rMGZWx0>R`@wm8|FaJUTp{Y!7#HroFAhnUzy!i*qLoj`pndFZE`nqnp-6GT!V;dF)>A%8t$~*X)-KcU);-;mT|*;oQ;H>J(j('
        b'TU{!ot0^lXPlq?lg&Hwm9jUeQxl__8ct=+Ce5)`$crnB~R%Uv1x|X}WzD|2*R?$7;m6Yr1)!y&G_KuaAy)WHz`d_;1mjdaa8H)z#'
        b'n)x_riDu5N(!-4ju(REs6T!90?ae8IZb&&jVgb|D>B?|JYvprJuV;Kdt-0D<cu+E$fV*Ul_e{T>#!0&hNt3zmV<aNqCb=HGqjk@c'
        b'^q_|B=v<xYj4tVFbG2us;#$?@!i3T0>&kS`9{=1CLrV_l>^$G!<?70MH1zKJPFBl^NuJ(jnH{Zqb|P<AKEDqBdh@sEq$oYQ+E<|S'
        b'+cW)EQH&1sRl8I7TyQTwq?+{$t8`86olfnQm)ASf@zM^Te$Ev+w`F&~Xc3yAGu=JjOnaxR=~Db@b!9zuSn~MX%{dRFbXJEh8rR<D'
        b'%@?4V4;;#WbsleLOOvNb48!dAU}hi;J)TC+JU?cz%voOxmOC%#<L7&0=z?^*@fxQG)!x)Hc7gfiI(Bv1y}E}IlR>^fZLQA5<7D7j'
        b'%$G~qA;jx7qpyThN7jxi?VA1E2@n06(VLTgS9^N7>2J}$S#rIbTHKy2Z!9`|nNM_!&zH4m<Sy7qW8661o%+`q_sM?8amSUNZal(R'
        b'huJgTn_bxX_**b4bPF)<qYhrYrrNz36P`X7{WHehUH0X6cYFS@w1jN!@Md+IuhpCT0Fh&py<I#V-i}smlBh8=_EuTpnmTFS=Eqxj'
        b'h0B){NZ;<%$Q?}`t?2bOckAk$uwvY(#m3q^vm@1DA}1_g@kHbu(Y$b4-LpqiIvv+ok$rgPM2pcDSeud@E+<dhg^7Wd=dG(r4MvW)'
        b'4{y*;$8uyq31nuW2J(7o0q#q;?s(y(NM`IU>|L!s@2P@fy79E98+**)s}@-<LFe(Bcu$$XAMX=U@$oCv<ry!4cpSzE;8`JyLTmbQ'
        b'5~2OPw?$orj#p-ncg1*Nd~S6h<(7J7M{6^$(kc2$A8rDTuLkEWiCNp-yn6insVycFZrp}R=Zdx7L~1*JfV`bZ6OK1`Bda;Pd8;hP'
        b'tfIY<J($Ka!*iE0-rw9W>qSZFJ9D#C4}Chbwwf7!V#Vyu^3)F0-k;@zqT}(y#N5^1l<Vd3w>UfVIeT60&MbFYu{PzY2MJu)oL2hz'
        b'K}JVb_0rBxufGLbyUcfJhPPT545IM^INi%#x|ud_7!Tg<nM=Di8s^#C0pTdt-r}Gydl#*S@nTi!6Dx)Z1j&1Fk|$gjwnpyd?XKL!'
        b'y4u}s%iDZnk2+?S*af#b$MnT=-JbT8@({i;DtH}!`heMLFfjH#*o~yS9asQ-1!w}E1ey)RTT^H)1YQU%G7zszp|#jRd_{%U5(Dus'
        b'6<Q|&HvlICZw8hE?*<ZM&ewnj;A21|@MT~D@GYPTSZ*k^nt}6xg}~*&B49VL82BMz$rRFIiF|-x1WpDX29^SU4m=I`Ch&CNRAZs_'
        b'3}7{|4Cn?<0j>j{3A`3K6?iAG9QY03G~n~V>A*LDX8~sv6k2Bh7Xi-(z8^>eCZa$Ca4XOV+yg8Ceidi}J`FSj|C_>3W9)Pj!UHb='
        b'8iC7z1;8tTCg5hE8F(A85V#M>rZe^o#RLA5;sO6c@qndf!~<3U&A@tKA#e?ln1oV51MqsF5jafl7L<?Nfsc_p@aMn+;2V@4u&fa2'
        b'0To~&uohSZbODQjD}g1zKHwzaCg5b?M}eilyMU)rKETs~PXNyVz5+ZGI0~E!oKl2#2UY^70qwx)z*WG7zz+iJfZKtKfS(2ife!&g'
        b'!2bgFQu%@FfPV(|0gH+YtzqD~zz+cHfa`&+zz8q^yd9VX?g3s8yo1sQ5;N4-fCiE%2P6fVzX6i0wG%)SaB2zK2RIK{2y6lt0oMSF'
        b'fk|Kq@CM){;9bDUz^?*Jfk%L+0bd24PRv)6&_2NPfpqu!65teIC-6*Q6gZXA1JXV1Vc<02w}I1v&jQb)^nf#fZvoE+o;kVDdJb?F'
        b'kd$gzfd-%#XauH!1;E`vk~4PzXa@cQSO_dEMZJI*0E>YRU<oh`oCLfcI2rgLuoU<MATffy1~dRifkxo8(~u9a8fXHx0?oknz(U}S'
        b'Kw=!c8)yLT2O5D-Qas?VDIV|y#RE<|9r1v5z#?EPuo&14B<8iPKm+hLpb>ZwSOEMb&;&f~45S0B0~P{T1B-xLfW^R%1IvI91E&C='
        b'1)d3f6F3z(vkd(JYz0mOeh4@nco*<2;17T^fPVm<4J@64egIm4=K{Nc=K(hXYbYMD7B~W22s{p~qkPW9xCgp{i-A#KJ@6J_18^UZ'
        b'7(|}}8i22oeHi^V6?WhZpb=OHWcwIvA$Q>A<PO{jECAjHGy%T|Gy_L~g}|f0BH(dgF|e#0=^VoR4>SOm0FA)aKof8?&<y-Eg*$@x'
        b'355ebPvL+kfd#+|rXf6VInWG@01JV;fJMN4z;~o8=bux^^KVeEGlq7Ze9CoBts+O>9T9w%GG!}OpuMY&mY_{ofp&Cy$5WKZ@8C(*'
        b'hAE*gk$-p2aQ7#PZz9*33qH)FCdRki!j<W?x-NCK>ea(kDV8clQ^J!>2u&|l%G?w=sOpe;a)LV`M?|5n>}o<%hDusoX<C3dSIE;B'
        b'i>>EcJbU5;6`D)W+A1ZStHdW)O^_-p?ni$Xe6f$l#r>iti<H}|NEyUsX_>x5nuIIH&L}#A$15r*5;E=#1ybIxQOYhh<iwjJ`LUNv'
        b'p6(XOH%<K5r0D5=lIM2?=fRy~Fr8m;A<{I^-N&P^o2{elY(r^5NvUC4;ko9yrIg9m^v%f8QA3)D2UWcgwb|3k3|lako}FoOFj|Ij'
        b'KjIyJ>^zf$_=Zh=7vMpp(x0xBrezl+5<-_t9^t*`n;gWKE`zbL!V#ZqZ91HVyHyc?@Ow-SMHhcU<$I4zYl~LC8ImVH<4zd=Bm7p4'
        b';Wt)!i5Is@S1z@@#HYI>?QY}l)K|pAJNF&dqXls;OqVCK9ufGRL(X?(){*M59e%{aZ~9cG9}V7D;YYH~On05S?=sqBoWA>?4yXPa'
        b't~5IC*=ckfMjdGXL3K&X&Lt9T^vg)ruVQJiG23H}ie-e;@D~L3VPMSIT5nTj#Jz6N__aqz8^6NjJ&K|%S>Ea|sPi*t`St4j3bXwB'
        b'bbduye%o~6OSAl<y1R(kcM{_|w~{QsgwAhLmS0NeH#y61k1nm#vi$DQ`OV8GW8Iiv{z{H)^*rHbXW365BV1*c{fsffRcG1DbbmAC'
        b'9B0|5j1eyTuG2+hgmY%uE5-=t`oBazjyg8BPtD)w`F^AFUeRdQSlFd=J5Bc-jLN$ywv0B`#?7cs=DpUo+ISh&$#T@%R2wIwS<k7y'
        b'wbf_3x!LQJ8pc<+R@W?9GH1}ab%Z^?XVKLU?^@MyV)L(jhu0XYR}I+~|N7`ho;<vSN1#JUI>i$DsSR0a{!_pGhj~#?t|6J@#_n_*'
        b'{2S7&yF#RC_&25*xkAj9YZi?(rv0Wd_M(e9`kI)du1P*Z-!-JihB{g4br|eHd^)>e{bnoibe63&Tj@^K{a$VUeRh>0N4^=BaPbBG'
        b'2-)AiAQ|epvX-0r!%;$P`3F)lrJpa9y-uYkkO)?_kY<3^a4HoEHG5$TB?5__KGN=_M6e<ZN7pg?eEVQH$yRZwS}ou*;pko$B|XX;'
        b'`$AEL)`wLqLZLV|5wS=BnUH|H5J^@G#z<XrJQQWkkytEP)kex#yjYTx*gzpyu}ZZDu{!4(ZmT>i+ZfkSRn;5{1(m*7Bv{q7sRv;='
        b'uV|Gw&>Ko^;)z!|xZHCg!n&%1UqC_?lBrm{%H^fMo<wXdSHp{ia+E95tZIvq&`-`?EX^AO3DW#r)f(;(r;=P9X95jWCA5$$)Vzw|'
        b'S*`M+jwl+jq*Aa{BCsJ8;ktG=D!o+PbY#*exk*XJdQ)gpO1G+gfxU|NMUv~HQBvu&GMwYQ$hETQu%$%9FqddC0ZLL7E`a_}dZeC|'
        b's+L$k-El(OOC6QOHOqw;R(V4yr9Xg9j-qc8;dP{IG=|NEZzFQ%N>oBgCD|9ih7IvUN;n!HNL7iNA@PAgq^d*KO%ZKD_3286MD@~X'
        b'RC&-gyj0X42@Hi~Rp)?Kpkz-X9H&-}qIpozK2c=auW&)+jMrP&(6S*gsE=J|aG3rB^ZjeVdfV(v@GQdI`a$vR)xl18^n9DNXOYS>'
        b'o#y##gd4s8*4!e@wDzL&-o1OwR(iJUB+lNW#XssdIN1LWenm{&K`xeeLIbCg`}e=Rj{D?&*71JE|AlotOV)9QT=T6yMfigM<#nWW'
        b'{FhD<zG~@6<AMpMU2%umIyK8}%kK@2y`Y1j$1X8BhSWogGTlHio>~^Cx=x{I=P=4tEAL|eGjp4oRvC6u`|r@LS^kZ`Ez3q4e|@jn'
        b'`ZrMFXU*2rKC8(tC^4OBV8%Zg4Ynl~gN+#s#sUM)l@B70TDFX_WfQt1RKN6^t=rJe`V8HtT5o2@I~ATQ={!mLwl`=}62w{;Yu>Ta'
        b'VR>bu{|oEQcYp8x-u=D%d-wP5@7>?KzjuG{{@(rlKk>`mV`zH`6)Rq<x7lVi*jhoWKoQW6=?%91R+D4@(?-Y6o%OaM(3;O19Vyt$'
        b'K}Vi4I(C5ez>SBqitmLcxCMV?bj&_tbi_diK(F0gZ)3OA+sZ++L3N;2pe>+#K#zlt-a_Z=;y2?gk$><NqeEZrq1KVc?N^R8mR&K@'
        b'Sn3~X+!7dR+_7e)@nrW%V+v%tQtnByQU724AHOwsiS{5gNHj_;kZ6)<mRKmUNMf<X5{Z)}PL^0I@id92OFTnjnZzj)&y+Y-V!6a='
        b'5~oW%OX3WPXG=Us;<*yflX$+w_ei`zq9Spo#90zAlsH@B9Eo!!UL>(XVx`1+5-*lmC2_vQYKaRZS|rv;td+P>Vx7cA5*JIXm)Icj'
        b'5{XMBzE`4E;!=srB+?+hZEL;lUHX5QwqqQmK(9_=wmW`hwi2mlNbehGz8}x8{7*vuC(W(d=SkLoi0=zFiB5?v5?dvDB>E(-`iJ`6'
        b'BLDeR_Pd7W1k0_M8+KuS`61pDpo5^k+v{!JotVe(skaS-x*s<>UWePxPBEvyCh?y=JAQE(^C{YMFR&G40v*2-?=;}6!`iz?|8vqD'
        b'Bj@4ryYh#zorV&XEM>#DEMtc*Dq+f9Ma<?!J^oT}+XLDMdKpywSJW9~Dl8^8LRM#Juvy-&w>^k=?c@Kbx4jMujv~z2cn>qU!F*_;'
        b'$#Ks)4Yn5ey$thFm{%F$|5m-N1vq?m125AynD>GPS%Yn?`p-!!y@7Bf6kMWciiItMa|W4GF(+Bcdf~T3nKdUlONr2@zB$23q&;kj'
        b'GAB7HG#F2WlF4u^%B|}Cg^o^tQ;Vx<1&fCg;TVYytf*0}R;6}vC2MTV<|gb5L>5S018JsDaw87IaDOP_k3_2b7^$LWTxopCoH#P$'
        b';(d_oAW9jpoJ8u3dx?3_ACJW%OO!UQ>Rjm`NT!svq*5-tE*c6dYd0x#2Jkl(N>+~*hbxCyBd!glHikk`iWP_k^^to95($)_>$0PA'
        b'@$cM9PaqnNrIfzF24t#42O<%L>)4w$j&^w}Ms*Jp$_rC5e>|0_;1<r)%8RbKWd^8H`1KPmU4#pvoW<Q0DuY_*cp`>=h@c1}fpC&@'
        b'XR29fk&=C}fk=>QP5!gk%sk<_dPo^n#3ctMBLT`hors7<ZJIBErBZ-YMk>_)T3JYq_bi5Swt)vE122!#OG@gf!PN|@wP!J&lA7eW'
        b'A$j-raKT(-4wzI--{;AQzdsO{>I+k$1n~yofr%xQ`ARa>6T=9Jgf@gC%Gz*>0)~?^tL#>&RHgHss!!DN=o?dx0HIkh99=iwFwp|#'
        b'4wbZ@a_T{&FZxmvokdZ(t8%d-L4@oRf(D6gfsFe2x)P)MnuotX9Mz9QE(>sDIMt`9N+Ky#{sF0PELCx2e;~0QbqFM7vt<k(CEm9w'
        b'$r)2bBn*p-bb}%@3yM&wMHMlqSJ6~_Xr(Yt*Y)XgOb+z)=}StA-m{Vk#|DzwnNzT=v3rVwW@VvkjPdiBIl&P}6K;CMCBprFJ_GY-'
        b'2Cd8`@Cr{%(d$A&ZLDwztWCxeYcqVQNFpwu!e!TU$$PpSxL-0voJ0QPKsd#<o^pQ~iuBE=LLwXn6UG=f%P`?+GL%T^U8HO$rNw3U'
        b'EJ4j8sW6Stcy-T`IYA{DN^u4rCBR>JmWDw*;lxxzPfq^%TAu_XNGrzGeAMRghx_A^On1o~&piTbV~JEnrLqx&hV<Hsa(J3h6vnkk'
        b'5<?WTa!s#6MOB%*j1{v$lIod$YqKSIQ!`m|5{HL3vU-7me&gr_?GJIKr+u+x$}i*$qFQPa7fY3;Bq~o!Odkc4#JWVFpQ~TZ@DMsm'
        b'MIYq4W2Q{S68w`V);;BKh_#LfYnFqclOS5_q(D}zYj(a_Z=<!&!Q)sr!AxtNVc@~n>up1CYHKfbtwZMGD@Gd2u+}O)7xCWHU^@hy'
        b'F|)z84fHxld@DDwV;5jOH7j>*^y+z7Go9aH3z8oe*X0OTcVUC=xPm+s5nh446louTpAT4tJYEN_jcwxWDm!EuJXvLEy|}^l?8T=p'
        b'gJ+&7!>jW$%MeF8b?4?U!~L=h>w+vckdjJeCBxUurKeEftSN})T4mP>(Vap=Y#tA;DmNns^yihL&Sf+IbM3zWLRn`iYSiQxWeCpx'
        b'_m*KB(%Un8j55p?We8&}O#a(t84mu3%5Vhc=VclC2hj)>;h4Wa77WR2QfXNyB;2Y~2yY%UgcBhqK1?V(e~ha;&KYu{pd55##K|*+'
        b'#tRt?qym01C;2zWV*QLA>lW>NvQlg3);VYo(3-hgJ0FJs(b@UidCx_7#^z?Wvw~;Nhd9292Aioevz=$aukRw!&PoN!R>|04K$N3m'
        b'-hXb~x6Bj$o$6!kxXi!1>fbxpjF<mlmB@c%IJ!1QB7JwV?i6SUv<<W!v;(vgbQ@?72(RW32E!Y;H05#CX!Fe=xnKu~^`g9$Cg-9I'
        b'H@r<!>WJa*8@h*b9w}e=zPs$lZsj*_%ir8wX~#SLeZQpa$0f>dN-TdX;R-Zb3XToglvfIrhC16qi|wg`p@mZ{vn<LhQ_B?gM(RoU'
        b'{&uhhf3LIf_#<xiR7u%S-OBIWmN(tDA-89zyL;Fj-#5YHj39D}^1G7wQze!+OKjJdcy2H0zON+yHBp>X{+{6ZzvNc_=(fD=w%Obs'
        b'kGs3u9gn+*hTJ=Mx`&6|`^GEF6Np@*{IO&o@_)O;wxYyyc}e&BlK6*8hCW)d^OGgRpD)?>$T($rdg}N4{uSohXQsMh|4RI4r+(z#'
        b'e}$p&$5UMw6#fhGpPTAB`(KIwld0c7>tBig)Ku5$rhh5Ex%5B596iR*W@pA>BYSnK`3*CxedqBPUrlF=TiLO-BaOsUclh%_8|&sD'
        b'Qt)TbeItzxmXXGz@PGC~=6I%UZP_}5*=lWP^lb?#92(tGJJOh{!F&8-=IH)_(ZTrxF_G?AIMTSMLfpY9gC8;RBF(L(bt8>W^^7z='
        b'4LSmP5ws0d3K{}!0TqMTY-UUWU!OwPbNGD}5Yj$s?7ppUq;Y$YpJ{TpZQN```fra~cM^ZM3FZ@{FC*O1KJpv3KMy?cIi%-ijxBE#'
        b'IBbhdj{Cz#M;Xdox*k|ya9G15jhi9}{{Y^XpQCt%Y|Ur!&WhpP0XiN<J0wv481YPw{t5p^>Ai9A&q(uQ$X8+P2>iAn{%ealpSjJs'
        b'3GqOt%_EJi*P^a(F~<>v-FFq-L1iGkPZX-<PPh++nd1=L%E>=zw*DPNvMnrVzvCh182+%qu?FcVAFQ{f;`O#}m|y-H%Kosy@gU6m'
        b'KwklU8T9Hy2FH#s8yvSTLwIJkzWm9N###57tv7*If!2eNbGNwF$%arT`g|3aUpl`HDtLMHNvi8FKyUC{H27b>ccgJY=NqN3WyeR4'
        b'z<d}){F$Xn8CwJYEuMnz(#Da-2+ZA}Ajo$vvw3bbIyOIGw%!Qp2L)j-M>yXV%+?KxfNYL4nC%?2$o|8od7n31uL5<0?m-&2fp&nl'
        b'f%Z~9w;CM>frs|e*sZrcf3&pwMbJ-R|1s!U(2Eb6tx6HI?VM?HJc#i3+=g*l$ZT}?ay!O0y3j*J48hb+sMO(YvkI;BHL;<Q#zATK'
        b'@TPj(F{HJ9h@OvMjBYVA{(a#*lym<KW~%@m0&c4?Im*vww!O%!wc6xh^G%LdK_0l(?J_!oyNwRdE%a@6^zEM_y*U`GuhX{*%)_N9'
        b'XF14cXWgqnYe3zgAgB*Cqubd1rA8`aX*XJ4nGJM;OoVfgC+ZZTGJuZRO1n>jUPK<Rf?ft$hmDTeRVK&dpcg-3bo>r(@!O4#<E<vg'
        b'(LF{-E3Yg2)+oPoJ%aw{lk1_;VOW)8caC0w_2kz2Lr1q3v1i|FavVV$&<F9<ezWziFPW{^0<Q;s9CQz;@LaR?MTBFY8fjdEw6_6='
        b'K-)n(LAQYh;ob*&5a!uvi@px@>o)9LziPH_8%DSl7(X!2q-VOmkoC2VG~TnFzGu?J+rV0Hpl_NmZ$DIV7-{VJ0*%A^L!(>q>^^F?'
        b'{{Atu^>*M%l>0NlM?pV*l=?Wvj3Z`i%e_X&A>_e7u9Ra+M|d{$*tdU&Ft@^d5oj0`0Br?*4HN}EjySLV&}=>H3G~_HX6t#NKY^Y)'
        b'uh43QTQkg6z=em)9x1;Y<MS@ecX*cQyZoxppbnomIvT!UbfnO4_oKh=huh~s`#^hPA4MB)e$H$?_!F}=0vv1|X}lZwHPDfr^|r@='
        b'UeKBFr*A=37}r%We-z{d(YK*)^gr{Ib{|BVYtH7^936eY(L1@C;C&{#3->(Q0~C9n+Qh&P-ivvX$}yeUw!rN%(8ocy6=QtE&x-kC'
        b'P3K4>$vGjJCj}sqb+QHJ8*Vf?h8{OMoIf>Ne*lVsj$FuWTY=vI9Y*}!z+q6uXN`_u0%!lsY%K+yaS>w|v@^E<2Z)dKpGE#_Uf|E-'
        b'G85|YAfBOpD7zxQWtCYm<{Lme(cia$c7W<Ij$Xu=d>v$gUmeJT@bU8tt=|BB7Sw|IeBbBHR+H7_*#4y1I(iG9@>0f5E@a&=T3Gki'
        b'V|?zrn%FUpqOMC3-iDStbcnG=nC&13$Vu)Nnmfx_D@S&02=hk^%%hFRM%kev1{i&r>~KH|1}6`<g;`6O?Eu<yh~~y2ayuO}?w?0T'
        b'FF?+}9vwZjjogYc39;_)O{dxTAEPNg?~I<XO*OKj$^2`kVmr#Z%TUMjP;Uj)4fE(<M@P3H-IG@%`~}BHNl9KS%}t2EuD7?B9W7$B'
        b'5w?QDBcYv??i-_{doj28ju^V1ecaH!vzv7v^RVuHa669HE;=+i+K2VQ5Qs`PdMC|{qg(NJC<3=5n2bu1P8q12*N2_CnYIIe!+Yj!'
        b'v-K^Y>F=29LAybtC(YJp-ZERi5A!RabKWppJ3%*segyg>{9grD95-8U27Mb;_@>#~3i=8BZUO!cbO`2YNT&^SKg<WeR&T5NM!hZg'
        b'aJ_ACKg{2P`RgFy;3M_6*ACR%j((-yW`+5|Z;3k@E|jkvv>Rz`L>l)29|L^=Zm$F90WUaVw%!51Wx%blw*&h@H^A*fz;57~p!b1J'
        b'!hQhz%%?$*A&+ldHq!V!?Z4-l93~&;K+GElXdZNpV0fGuRWNrQg1sB_*mu5$XXb#}+H`=%{jt%qi^TnB%gsi|R=7R+O|x|d#_EGG'
        b'?+2X^^9kVP-!fYZzHYYKfpdTk(AA(rp!sln0XXj)X6x?|zYq9rQ0XIPs~>b6RE{tY!>{2yX8R0~9W-0d25km?4EF1QR|Ag%PXHsJ'
        b'(?EXE8q6WVPviZ9Iz*99$zd~>9d;AU9|N8Ip4s|Wl8yGd(XkJ8pZ#fm$8V?#sDO$=$3A6rn1H3AZqQE97Em9k0n`dQiS%CuF_<4k'
        b'y0ehaAAo0m+iZ1%o`v69;4tz_O=j#x*dwqH!2EIGO>kd?_IeHO$3I1Rjx;_F+64E~Ll~#P4X0ropUG@<V0Xa&GVHT}XP(Yj4ctm#'
        b'Zh_eb^XuP*Kg{og`8U8-z@zX_0;i*Fe}?%Un7;}9Q3<w6FqclkY6<uv;y!^kQoe&e1s;I?0`&7D*p~pW01m_LExeDeh4~tozleDt'
        b'2J@GI-vj;_*bnzhK$n8{9;vro4tyN>twMeW(AL}W&bc3S8)zqJ2NB+>M?p4}@pqsB&{d#guh!eP!T&m#UEjxZ2YeRvF;ETcL-0EX'
        b'I12lxK;H$?8i~ll%>4L7!QS8?-upJZuiplm9yVJSz+4aP?d4mJ?-|&kRwwK!&^<)xgT3_bzu4q>55gXR+Y!*qph>W&reb{s|F>YC'
        b'-DYycX&s2?<b06zV@AhL&}&#{T@3pcP!s415LPX;oINyJaEy4uPU3kgIEcBamDWm!O1o{K77zoqf>wb%ARh?x!tv43?@$6ocM{jf'
        b'kH|<H<&&dy3F($^#{NMoVktRb4WrG6#n?TA=3gwK%ki9F1e)g)YvQ|>JnumQc+=1%-}sNw(MLz+?MBR`qrU~ciLKE;_|2!G0!Axu'
        b'KjH>KVNeRs&d{U=+Zy!iR@h%h)_Cj;UxE1;=o-v1i@NY`0zGso))s%qdk5G8_w!edG+qh3681Q7JFp&Z4KN3RRWv^VXRI1&>;cV!'
        b'{gc2cz(;|nt;XI3W+(8kpg8Ci(EXt2K)1o~zd&bQKGOIb;9o$aAm4PshiHL&E9h`Jvt0`819hI&VEX`Y5VRSz1vCfsXu-4B4Z{2|'
        b'Is~^FYp~A%GT;dCx1bixrFF0m*J54y3pBpcU^{Xi@&X<Ok-(tY2=n+%tjWE6tuVT1U^Bbrijl^jfxZJGg`)=$_AyZ5n|RTmz(x{1'
        b'G4to6qc2{Fm)9RhM_<Ep_}`efZt{;bHg{w00p5u>+w(~GgEx<k8sT;xh++TmGS+J+LB&{~90L|$b1@t4y`WCeVmrHf?#YW9imsk>'
        b'a(nU6HOZN?Paaa(4UY4VvBd#aYOI{{omnSmD&%<J<gBL+vyAWEcb93)AND;|HvEVJ*ZWV-vYUqQHXZxKlr29S{(RZa2gr5L$%pKw'
        b'ou4)xy<y6hukZXs+0Y&2y8YzccGJ);rY)Oy*-b~bPZ_?WZ0H8%8oOzFCmXuP0>hpucNLx7S&`Z~lp2~fMcJ<GR0i0rDZ|^#$XqdS'
        b'tKsC(EW=J%D-;xwq5NNd>%`3CCn)t3cb~ax=xX!uo+;OS>Dxm$mhIe5neMu{Y|GO-Z#Nyg1L^799@@Fb1c#${Oo7|{;_36)&^(Jw'
        b'^XgxpC_RV5Ra`L4OTMe`0;*N<-S;rza7Xdgzc_JC#YIPpnT%t9@x()48nxY{+<R5Y7fcAU%7{Og7=LqX$$YaK<{23#w58;lFO8~!'
        b'_82YOEvOW=yzvXBdvE43DEy;p_)R5LLwH(v1#U2gc9e)dvVZ%;{if+ng{9`zhLz`>R=VsZ^AqNWhRyd@m#jv^nvOm+W!}a3^NojQ'
        b'e)YuBN2Vx`-2Kb1oVaWMiI)n#JIwZd)jp@9Wd5YjneKhF=!r?Cr+>ltlA(0{z4J;c3_EH|C(Ze_k;=}FV&uF%%BKIG{c5<t@{ICC'
        b'LFwh8ijqrArL(7h_wCY2zu8%Q_pssW;S*?(rKZ2nGL%lW%sSMJRUVab=B+2}pP)XvX4YBP1Q-mpv#5QqSv%F%ROSd6xXbjbcbyno'
        b'SZ4b_oP7&aQ&-mTedT@C1TaOQ?ahTiK%ItQORzeVL_|>A0jd#goll@aw2x6stL-?Q+|WWmIs<4cFm~o9N)1$6z*h0WlweD(#Tl`k'
        b');hIitO4XLZxFrzIXA(_O#ijM|6hxBbI(5eoW0LJ`|Q2X>k<Q7sLN2Q{&dsCib-4+pGBzY_mBu&rn23n=|IajTswy3XU<l=4w4~q'
        b'1!egWLLMBnVOYCeVP&kP8bAxrmxQ;!p;&28dHp6(x578=Y2(?!j@>sG6g6U=50Ij6Cx$SuLZ0d7O9>thvHPvqC9T0Mhme*jXq>Gv'
        b'R36_3BSKL*qKw}#FWw}hV3*l_dSK@hK=sSzca!AG`*Tm;m+Sb=&HJ)};AYYfWNc*2J_=<%U>TpdL&2N8L&2AO^1fV0!p-}#$)K5J'
        b'M8^Lxzw{As`G77yafg66d53^6_vC%Kj$hooC%aT5ouN>gEsX_jP~RjYK}yq5Ohag71E1LaT`?`cn<SI&&pmNpZpqx6_hpmwW|C0v'
        b'jfi9RO&d#qUSTV!M)50q{?IIaR%VYlkW&kKx`5VT&Ol+7X*F5kzCBeh4k#|5Ua{|_Nu=}(?s(~QHuhmv@6>V46TDK+L1YH2wWR%o'
        b'qT<hW!&4W^!Ef1mtCc9OAgl#iIWSf1HET7+QX>a4#=8ZT4IJyFR6k4s?E`w3hak>#?Qop%waHaKP65lp*I6g*=9*hCwE$NS?aJS$'
        b'O8!1&)94(RrbO8^9MbE7ZG%?DJFM52Va^Xfu}LTZwIu-)2T``%hq5JMjIYbtEcZ-tURfxwB2JoM&P@SL25`$HSM0T8^;0GFQ#SEg'
        b'$LT3im+EKft(NlSsQ(+eyfLr-gL*|ji7JOV-X5r@IA{;R*tVOJiK$XCrPb!_o`~2&Xrql}pjNNdY6(z8IgD5aImp~W$Q=9zQnYg_'
        b'*?&ro%zp(D$8Hf+_H%iY9BxEBBM=Wq5nWV}p>_%wCt!5glT;1HyaUS$eKP$0RH*~8T|#Z*c~)A>yf!7uh=7`?DRm+bWQ2KN4<Qj5'
        b'D*m;^J{6ns5dX@zuUs!2<@nzg-!Et(|C=z*f%<J2s&pZw*oomb6Y81ZoEQe2gXa^UtV^Dma^y_Gj*f&jf#uD%Z3|LV>SPg1BS%Ur'
        b'M>(IpuMCz%Z=C`rTzinRJSZW>b=gyn?5TV|B^)X;gbXY$&M_D8Y9mFg)|`@zDWG*QxeBqdJbWc$OF|sKnF4gd3oI9f1eZgGr6ubD'
        b'=vnn#Neyn9FY(c|1W1-ji#Cv6yRAx@vSUgy=fTAq>~Lw9>d7fGP=itWy$kV{G1y)*$a05YHODb4rtD&+2Jt#JuidMh;>;%jKY{tB'
        b'63;XT?A1c)gM%SuFm6~fMFvG&>bEsp0sCWiQ7QW|8I=Fs6}q_{lziqA$ZbGLDa+;vhd}?SP|qkwZOU0FHD8vSTDlB|9CGflFpS+m'
        b'=~~=mAW3KwbCVZAZ8B$y76fQRsTIl>=@u)fY|Q3wVn0SOgTYX;d&od*t+ZU}Cr}F{DGDfLb|sZuNqK}4nw_Zgn~HcxPh#|QfutY('
        b'w2t(v5vb=$j)X=lrd;@elgbehi31Plezp<SrO&gp3Qekcu>nL4uFe6Hqh-$?sn2@n5mK13>e&pL#rz(jn;%$%YR^#GXe)z4eau*f'
        b'L{ChDj?m+}^uVQ9O9zM8TH1jap1GbM=VzNAm>)+5mz6#jSa>R96(anRBb6DeEW#_?LSf6lIK=QZW%!hm*HIpaFz+e{f-T{{q0fOj'
        b'erA$4(f7t5r5M#Z$y@U~K}cz~#O`$MxEq5o-%tKm+;XR!_?~jef0X<C{~x{RPbcj-w9dQ0BT++9`@nBf;)-WQ#=lLHfwp)_D-dQP'
        b'o^pCpMl;7I*9FK*PEIl(P3{lCz!M;wGzfEi(!l1}c$G6>o@Q#j+``y0Fu1(9c;EgC5gA}gln8s_ICY7uU8a>XJ_gI{^x7uIIq7(B'
        b'(k}jQ$Lw%S&iG!Y;!efofuy7~QNqVq%)ZHxLO!FS%$X#+ivr)g4Dhu0;ROATeUhrpVTvXJyKorr^lg)lf}f}V#^k-ee^+tw+vX&W'
        b'7j<y)zD4GO+uvXHBEB+tf5DgT6!g-F-ZEMLK}TsQLa{l#^}%a>rUy4~#VW@+CS%g+n0J?dzGtcuAwch|T2K1%Z6<>%M`p%6u-?XJ'
        b'Cc*GB5$Fn?VD}J&x0@7E@v3!`7vdEfY^CY@P$z*fX|TzfHB=PA(%QUHPL(_<dn(xvnDQtCJH@2H>}2T_!gdEo9aCe%C?wn;B}3EV'
        b'lh?+_3Mx|)CQ0EIK@FY(>RJJj8>KZuW;uL=)yKn^bjhS%5W6o50*nwqhY7p{Qv;;7gY7y3S!aI~m{UdubA?}XNULf0P|G-nFpoiq'
        b'evFhYiIUO4cPLYDM@LQSz{|lY=rmnx*vfcD1F?WxfpvuQb)4Z4-I-}%dj#6Fy~)~~l&%R#UIjDlYpjI?>(a(n$RI2P!V><*DKq+*'
        b'AU=Q8M^20=>0V~`qz$}G+{~-teO0t%G7{I@4rGEj(}ban2o@pzNEutdw}t>L@_hi}<JJi${Xn}EVSz(oU$#~&Seo+X!K1UEPE;wp'
        b'2sA2WtuKS<f<{Gb*~?Tpcp>UhAR{^J%Bih}6C6+$7$K`&0Xo%6&&-pyADu{z2xu1|q+p$2QhLusn)!f-6c?DC5x)Z!N2*C|<;uwA'
        b'8fB6o?$K%6dSwfk$S<(h2;UXIQZTPR>PwluwWmEzQMk5!ts?cazzt>))Hu)e(h>eT76nldi6w{b1;n65#I%c=I{bx^%M<#zg}B~S'
        b'v=>0L@lDS*ebaF}Zuxps-VNw`jDMW4g#`eaIL=PgvxqGUJznOo3-jkCQy$bJL>k4)?{2>(Ijbp4j5u&Z`4rNu!DA0}DP_0ISCP18'
        b'L!2fqF}C!}f(@WT@Ayo4b;6_$XeSVoSm9@6>LwD?4lE)i<!O;&U^*MG5yvf>ZcY*>NRR~u)&{D$ih89msCoXEvhvpH_9R6`e0#jY'
        b'^l9MAMBy-p)PLDatNl}b?K7xh`xc7rCbOMOGJ%-^Y(vR}iKtKph*F-uhp>U!3kk3B5-tOtC~i??d_?)LlJvY>3(kvcB(D_Ct6u;K'
        b'_xvZ}=2l1-5|xsE2IpSjK6zX7E~ZH`+qk5pJfQGMBVL1f206$_I#RN0!l9p_C8$k;c<0Wv1Ow3t;(NzSbQAZ_ozoG@NkyU_0ioJ7'
        b'VZ$2or7@)n;O3o$w$e1DRDqVJq3SJ&&4K0@Lc2oKe&1sj6j4zVj^9jxR6Q@38DH>g(1p;-(4mUs7}i1|D&>S@?F5L2;Q;r?%t0a>'
        b'9p?=#Dl-9{1=ec$fpfr3EW;}^knojjZL}ZxxMRfxK(M@k<iQJ&CCevlp%`Ggltryod!5U0bKor}9Sp|`JF>YOnmV07@oi=#;D>x4'
        b'NC0r8iUZskiu}CHK^qzBXKt8+)jyZe$>ndo0+2(3TZUo(l{_*5#t963;S}37FW7FiF3Jy@4HFPjAgQjRSBiPNS)%@bzzzQ2<5Joj'
        b'V2;!;a%>c(T#P^~4FZvD?g^<fh}*%wxe-g3Pwd=_CDbCZ$FY`pBxFBG33HLy*yqFdt|br0#xBl!3d^fNvU0J60VFF16BZ%1GcYDw'
        b'GM;~2yn}rh6wK>GwhxVyLAHp<B7F@G?I26!bs`}vVBI4~NIv+@+lB04XYJhEr0N~t;fIk}>}D+QIHHX(3Xg#t1`>V?5dPH;_7C8_'
        b'<txaNa5u65R8my(<G4m*)=jJSjgt@1^lIBYj0z{V(c0ZRFVKo@yzbHKv4k$5y*t=kNG=c5g$XYrl_n(XGS>1bqIz?@<n*|WPTv0a'
        b'ai~u72oMq*?22u)+{(`Y>Gg!lI=)&)({e}SIGlg+*W-4uWw4F&!AtSZ7%agBUJ4+$+W`gh4i+{}_yhpjclu+(1}^2dKoqI}#B6iL'
        b'3k1n_IVrGi$gN$gFpDEg4vg>k@Dnd_s6O)u&<fy#*qJtXxyV}pYTE-Fu@%{Q6wCV~NEU(0TUc)UQ{y`xkSf=Ol@tI;+*ea1l*cw&'
        b'v7?4->EY$zh>e{`vus2R*7AFVX8#gfkG1?3slh#$xE6nq?}T!G61*G&mFE?3+YRG8B33E$A9C2o$@!JFTmt`1+U<+S9j}htBINZf'
        b'9CFO=@si!+bRt1#BXkl%r{Q!&ERfbhqGcJPdSu)?iZ*xmt3Tz0{Ax$#8IIXFPUb^)0|A$OGt-EcA&z-z9Mq_y$DJ9=fY|fkU1QZ#'
        b'eE0Yf`>(#Q3LGy99;fM5+c%9<zaR`Yl#X2H?J#=FGCERD1}E&}$mPPVz)zdUx0@kfkz#rUWJ^VYl8`giD)6#I**xk|At2fEHK!7e'
        b'*F6b<@|HKa6nvbSI}SQ5b*`8U0v)yy10BY$l_!HfJ3Fi75zuFUxKGj%u+NHVg|L)U4Ug3cVMTd6IMv`7P5**=git!$9QtumR(XKa'
        b'o$-JGK%~vzYfC_qH;pV6?|cW#dytC`AGd{Sb_NQ-%mPRtq613^<W%irj)!1n<b25W{Bcr{YU-pzBb2&Nc>yQP0pet2<J;+RuPj$f'
        b'??_YCHs)P55WdU7K0eO1R6ya^;FYI2VHtSces+uubVis+5u2ZDWpm6YuWgr%mp*`z`P<6nOU8HlFWteuzSDozf(L*;B+TWCs<t<b'
        b'?TA>txf2tf=Ts-g$UT5Lp`Jr%A&7#`s6GNDUspCa!?7aa5P*MV2H(x8YQ_=@IWkaLfNXzn%oefQnn&zD(Qa21ua#TZQh5!&^)DwC'
        b'Zp*Z>;t2gBh8<JxAj17tmHcJQ7P$<r9&B00d_PvIdFXT`kfV%h$gQPvT6L^u?-9Rt2_h5$dAP^&{T^lhJ(gekIa4%d3w&oq*WX$|'
        b'%jxW8(1+MGw$84aylIYkW6Y^p#a0q94sudLFs}k28}NKx6D=dqW;1PL8u84U>OaOnL`<^>(};+Q75Xq5mrf5kz8q`Bn-7u9{xKMF'
        b'0T&~MmKd)QK+EeNy=}}MV9R_|7pe!LMkE15praor{fhj3F&P5lq=nMFX<tkM?6WF!447z|UUV9|m4(tHg|-j>P?$^3Bc;}=T-KV?'
        b'TBbW=(-!1f^;FT>%2BTMHOG5naA~p^MB0@OE@8+kNA(D&Iy9E@>oJlrnGjk{FO@o3sO}CHgszn@a>nIjG|Sln_C=Hht6m%PI^Ncy'
        b'te=+C>QFM6l)_$|g&^U}76Iy*H8L0Y8MEJQ-5IMkGS_Uo75&GtMhs}y7Opv9AAD19;#8YqMNX6O!9g9%!HTA00|ln9Q6~{X2IqBq'
        b'c~dcC`ex-aMYLwD2GfOx18I=B&V=Y_%>2_FUB>L_*Txe4?RfO7WBL2AmOV()Ro5a@D6%3*W(*#4W+J9AH3)$8R}(Y!p-FUNbL>7W'
        b'FBB=oa2u|*R%x9kG=CmuGvNoGH4%^L@W+t&P$VWaHbCsKKv`9O$APk;`e$tc^Wt=*KOh~wX)LK(tCwrFBSp)i9~-khHK#sIru-6d'
        b'JUwP&5zi)0-<)(*N0arTQspVcVFq%o{2vHBnAohp7#l$9b=qiSTz#A~t~Aa@;&B%NiRQCMzwlE|2RJ_sco!oRU$M_=kd}TijgW@g'
        b'+L99m&U4fDGfHtleW=J8HXDZgC<0og{AnP1E|jAwRGt;E*!aV!Gi(L0p`xw7Afe4MWy(#V^PQnlNne>l7gn7yWzOM|70%EFHr8s5'
        b'r>cJ9(G)IQqNz-`vbxGfiVvR%DXwm+vN<u_6dDCQ^6qIem_5C>_K+2rfy^jZX<{nCEIoYUA&6HB@W}Zf(g&n!?UWDs<RNF~d{@Si'
        b't%**6>-6C|A?_+3cftL*3taVyI{;=q#H?s4uLpfZ?x`&Ym<s_W8MOOm@%wwL_myTYw3#rgfuC~v6UVc~I$Wk*B-fcRJ#9WCRE>`6'
        b'{b0oJALrMiL>v>NA>^Kqm=mK=XdiI)uaphF4Y{ssFj>nXo_}zO%?CcR5sx0oc3m?C30FKj$Jjf{ygS;k!S<|w;$=R3PQpR=HOF04'
        b'<&8Q%9ffvw6(7pUV&Z7!(TSF681GWrk@1X>otbjS=cBq0|3C(7X*p0K&#$=XOQSk}1SA29axa?x&8X2enxRDKHOZu4GcNU<;=-pe'
        b'&l)f;fjP^^E$PpXmVSek&J*WL)-%UPZQ@R|7#a#&08vsi>fM;Jts$7-jPlElYeZd`FdnfS=afOH`ZyPUPL>facT|klvxasd2-%s_'
        b'u=&{=GL*s<St2sXD~|M!M>m7$EDlLOFiJf`7}hG1%@mjsqhvyc5lLS)>OwQZ13?8VGAZxoP-y_6wQH?^A~HT4XtFCd@!MryUXK3^'
        b'&L4{J$65C?IG?ch;~0xa4KecM7z&Ip<yZa2=SEY*G)0frV88%I{DkEl<5cQVN9O2^vvX`8C2{p%In@iJI^gocB9yisXpfEn0|JGx'
        b'esr}AG(q?&*O|E(k_eNh&mA>Spp}O>8>`8eDghRVPaIE<0<;WvRz`d|oPZ-FkYPd%ESvBNtc$g7#x)y-po)wzd6v?zlI5}r$#iVA'
        b'Q3`5E7yvkqL@@dGP@M26_dw>X^qV8(9>{`zw55+D6M(E+j&K`=dGGtyh=xZ>(ng({kSa;Zx>3iv(bDV?n??@<rM06~-Z<Q79`&xS'
        b'Xb4gkOarxAyqKH|HywzDGOapyDMp{OQBUs$@;dJST*|6ZXq*LbiS&4Bm?~*B14E9#6Q%lk#9;yw6NT$AhXL?dsf4}YT#hV+OEP*w'
        b'76W$%3E*f{OGjx8DH?Jt8MOrXkl<1U0$S0Csr|Wy!aV3V5Y>WF4aPg3ynb(cqUVqDE-e_Y7Zu<U8BePsAjF2jh2&mwiF&kDg7g+J'
        b'bt8_4M(w-8^_b&9prT0SES`|bJ266RXF0xt2M0^$jn+$$qURdLj=<5pQO@zes7K0y7eJqpjMiY@HM)cw-gS7zXsH-Ek_1=Mkdis0'
        b'PPVvh_Gm>lDJBbEDVSY&64cr(LoPQouR?<Dz*C7S;2f<vW{m)NN%L7C1#*(K$Hrk=#yDtKL~|pB_2hwwKg&pr21PWyA1=j_;zP!Z'
        b'=hhuwf?YhPEiPVk(S$g^Shs%(=KKQsli-;7v~Y+cv4mmoUSlJ+04qhco9kz{^^CZCN9vs`96ckJ)zba-v)Z~x+?@cDm<QusrgOy6'
        b'H3Hb2(7-Owc6&x56*H@uRS@RNCLe6#H?*s=VbbpYVdUTKBTdzE_xB^d47)euI|!}yfk=`s+(>F0_fn_O_G<YFwDu&-JHgkptM0;x'
        b'EM`*-3QV(hF@(oKnn{75mtzUPM54bK(c?ON-s0tk?{fkCY__pwM0*7_w8}5ELhLWHWigA_LS5Qr`miZEc?}%HPr;n^upWIjNsx0L'
        b'Cr37|$xU91vitytM6y>X1sN^eCIej3)R$!(K{mz64Vf@+3*0H(kqtK{60=F1oSXjQNbys-hPCLXczJR>L`lkyohQ(J!D+Ryc%m!y'
        b'2$CEx*Dm6#hWmheu`zMPw|$$<uLFrAhR5|#rjr_;J{(GrLt3K@|6<neVPu{G+3P6Y3!-$nZ~si6Z7c+p$Y=2RCi>F5T0ZCZoG!9R'
        b'a&k^;I-(t>4DC7RXEn|O<5u0y!9^0dzDb6>)pVM2vVT?I;+R)QkSK+fmb2EE!F+^yWyD%7XYZ_wF)xi!^^{YCcv?lp{N00eM3;_u'
        b'{vdL^FjD^^=V3(6DkOT#$UDy?F1!)*oEAAlk$2+pvq9}PMf(9ol>J<JgS56>0Yc^qd*PnC^pU1`1;50L)qW&5{$|9GB(L>KP;*`Y'
        b'YB(iw;pc_m<!|ss1YX>tvu;?q<#SODRyoFbc8VNNj?f^!c}wKu)ANcbeKllg(|c6qF43S35LP9P0Kc%oUgp;hH$6?Ca#@5#og=Cd'
        b'S_(lq4ZaFmnn>{~djh{!1?v8EroI}?(mM0*(2p$O4;V;8WYmdV5CANM3*iM)U%o1Ogvu~b6fv_;q(#^$$^)Lxix&zNti7oua-`U$'
        b'uvRx+j6|4-k-=&OiPd&Pb9YwUL~Ad6*>reG{|TOkn9|Igvxt6Z#Jf4B@v}T9YTW^X*4KHSY<`HSYp&g|h~K{!+h{CbBDCvVCb$Bf'
        b'3MK*GxV+LLik{`G!m?RZ+=CatOE9t#m1LyYZf#Feq>7Q1v<54hTZv0kSu`~fNxp`ImRHCaY$TbMue3*s)#;)d+_G~<7M4vS)x<EU'
        b'6HIv28KT-Ayta`j86R%nqp+4+nc-oV<fI)~K64~uxh*MW5n%p2du5(yK+maP67l-inn63f`)`(~MbVyNFNf-lBD>#dO=%#qyPGYS'
        b'm!=^N;^I?iZ9}vMduI>k!dUlmmK88phCwSm>i}2k7eyo{?BftS)*x;_rAXi#ZtcOXZxH~U66BY@%{rDdZLkD%6mTzihg7{r6#Y3Q'
        b'3go#K&{TE_08xI6o+oO@YU^_Bfyk-Q)=O<?hTUg|9iI-@I|tQMk}`2|Ia*v6eY_kN5pDUUJ<VKp`<*}I8jO4%kOb^~%(M4|2)5{1'
        b'5ztXEYJB{GrT`WpM|BXXWt977)h!#1P(3)ckN{(hwF)8ve^9T465k{OLJ|%_y;LWOwpT)iw;iTDD@DMcYPC5ALk<|^n>OY239ksw'
        b'6OB0N5a!)se%r;fTvQ`cKQq&3>gA&Jw}*G%tPy$=?knvrSc5Ueuw11Hj0{hjw~stVk;4vYRxbNbg4?#`+!D=D1%(;D#lI9eb`N{j'
        b'%+O?Bhfvk;hN&pq%-#_5DumhCU#oTvAJ)j2mwA+zyeJ@F+k<PD60v^rw(Z02?Zb}k!wY)gwCAdX$$_XTFAhh)INVMvsI^uq#_Cif'
        b'kUyOuJP51&R>IFE5M|D76TdT@5elD4xG{4$DjvM;B8=(Yw?v}#8uLHHSBNOPOAOjTc>YBI$%5D_E1=rAei)cfD&FcMpxsnoCK5dS'
        b'oO<mrDVf>nf@3pvm}Uw4vZ6r1n2gq)na;unD~}4)kNWn(R)KsJ3|kQI{u(mxeUdUV$WnljGAE09>=<Jj<}DCo^!*y(FP(@o@q8KY'
        b'bBPZa{W$-E!-(oYs#j}(kySl5TuAfb4-~YMeU^#k6@D1b100dV>P*Ol$*UUh7}Brct3x~N{>3mUV_Ta50RRY3l{*#=yXX60d>xLn'
        b'Lkq}yR?IBo8R4IfuwgGOns1Pl(eioxvna^Y&#8VGiVhi0d1#ngCXWstR)q{NUZmBIwjWePsp}6R?5QRL-9%BNOc<|q=TIh;*Pt@Y'
        b'5+!2<d~FYVYg3<;Y@a=B5+Owao-LSha)=D9fv2Ht@dy*hD-$X{rny80c@A+5G3-6KBR*WPnE#zQi^eB-qjEQS=Kzl{*LQ%YG#haY'
        b'4`l!uUL69}!$^?eBS8WM!5Nz-2kwRW5oRgp-iCbTFynk`@hCZ`?cYQ0ABOtoz(oaS2!fd#_dEyTQ*~vi3OnJ)w8BL6zlMze8iFwu'
        b'Ztx!N!I{rthVhdj(vO7xfsW_TgBg*f@F*OO@_nD->wBF-b$n>?-M;ssf@dnvH9!aI07@kDwbQ;V^iEB8;7m0no7Vvh=v5pc1?G0q'
        b'EYz=!^K%;{Mx-qX>A)o_<Re_7K-@{q>2ofo%RgIAApJO&J{Ojd2o4~~HQd-Rgb;G%nm@TM5B|f*V?$!3RZDJ405h0mEIk1E8ka<)'
        b'bwfyp{|o5b^AW*nLaYJ_u>$$XUmP81lv4=6kuL&etA<$LUB}&1>S!4`3yw#pTdvL*d(L9?!7l2g)6EXGeRG4VwlN<JdDYu3w={~+'
        b'W8jxu3Z@odfMetnFcs`MEGC0t`BpJ}UJ$EFhxR!1n8q(oMW^GQ6XHD%brX14{w`J(4b`B07D}h1mIiSRYWW*@RJMwN!taB$z`V7T'
        b'?^f@#1U?NtxZw$c#7O^*nBl418i9H@S0k{z#-+SEv;-<zfgokqkoR||@Anno@5{d59Pcml(oo7vL%eP#-&Is#A$~iQ^4p(-KR2{m'
        b'@H617AyWOHV4&{*OrBBqN*SK=8(3kaAY$Jv;1aiSHALk$PRMa^QBw_)nCC^{D=oj}*TG@Dvu=n#Zb@QRYkWjmfNIUqZg_YAIKe=Q'
        b'iiZ=KJLgZmB8iR}D%uC^A-&A2r@)3OO`K}Q5TIajiZ8Ngvop=`5d|W!x5VVq=0mk)Fd$nb27nL1L;bPXv<yiY^vzWl50UdgT*1T*'
        b'MT$vYuHr$X&&NE<cgG_5gtjh*Px4Ric?KOn3LhD|GZ!pMWPahrewMj@1N!ChnRQKmlzC!Mb0OmSD<APJLT7yHZ4R=?P(ydmdw8Zf'
        b'QU+kb_rNUYg^s`>%TL0YbgR%2Fa-RT`tL$-JPqfHLnVr#LR<ccC`LY1BIjQpE}1jrkPlUql7ahA&MKKbR6&DB#0kvCB32k`l7R`g'
        b'eDaVCl}KQrI3ZQMhzu<Hj=_dX@S#GQ42(E|l47ejH1)={MK3Yj4KIVtZN9xT>$o-=)zMh#*}*uhOkz7bQck<XReqjHFnx>&Qbrt<'
        b'sfKS*F>;k2JSpdyTb2<pqo8K$PDiLz3IqutZ0VSb<wYXRtXzAPszI4sgV1ewZU9d^&NZOloI+IXH>gu`RXBK3^q04EDpa{o<hXK!'
        b'xda)4kxV;$aa_K^d<|dVX@u|Li%UWJdj`296)yCflZfgcVC>6P0pLkF&)u^0a3mgEF<TQ&`WNk>=>WR9ms*^=P(UivR7!#L$V-mT'
        b'ZvZW;9N_2=IY$d*s2?8maJX-r2h$7YBqWgljbIH57t8tqx0|Z9tTqSmoO1L=@+o=B<Y4kCD)q}-I{?pL<Br-J%=@rZawWwa<$12T'
        b'!5oG!H6rH28+>qJ9vU~tOr)t6;>tHC94<iC(#a+K$RUn{H^BTxz#M>h!ch(&yfh~K2KsFvym}UqJ1Ax?%-rK%Rab+mDU2i=Q7|5^'
        b'&&=h#IvV}<japivrL8&^j7vTy365DsXXW0Q>37c|q2sL^7ia|x-K(vZ_k`X!rWu=4V!zSUM6{n)oUF1-zYi?Ph?G|CXno3sHTYR('
        b'Bk-hL7k0_d6?k~5=-Y}gm-z7C9(L_2$f(*8DRnjnR_!t$ymhi%FNxUu6<oxBOPV*rxw6e0xT=iEY}?tuf*mcsGm@1DgpTJS4^h>Y'
        b'dZG7xHna5xh>=0;dme4XB2mi&LOYrjD1dfh)}1j#AkpbJ=upHKic(Ql(*LjyCGo;jCu4l)i=MtguH=vP*dl|y2QzJ3f*JFTnKhZ2'
        b'd0fg3Qf9d+GR#NWLq;&itzBfiBcD=X%BmY6Mix}=6EZ7rT!>e!OpGMr0ulo+>C41tHQz20taw-S`3a)<3+f7yMPlKzM2@95$oZ8w'
        b'MV>zjfvvBc8RK^&v$z}NJQ$n7)t$Wyy?Zha#O9V4C~R(R0ZJyur6i@V-@b);wWL5*luFtQR9XH481x>)0XF<j0FHF|zd3@!yX4D1'
        b'yNL*7;1}NZ?!vPSSl+*ov8I9W<ZIz_&(ApQI<Le2;s*5B=Ri$3bi!V*-3DE;;s)@(`e>~?NpIAGQgwLB&>(Qa$?!gPG1Y~Gzi7z~'
        b'uN61Y#aa`aNXXNv3k0(K0zTur>+bk&E%I|PFJC+tZ#Lsp9saluL2=RE*$9R!tq9h{X%QU3{Izxdf-iBuHq_7Ew0n@E_5vnhyYv2v'
        b'APFT1@_%a~Yzk;5+CC^jK^xaIsZH&XDRJpZ+lSKq-fX~?|G0@>9yGM$h=2vg|I(m$ra^_W8jNmEjKe}OEp3bbYA`AWp+<lQGqn3_'
        b'A7wT8Bn}!7@vu#4n{5Jf?l-WOSS01#AQG=Nr6P!7dGZ?8<cFpSka)_JifU*?yL<yZeboBPpW?7$@bJS;n7;`RH4!l;!7`KZDU&GE'
        b'B!0;x$u&v$nq&t}<WbYCGp5;Jndbatk`J2{Ee|7EF}o2hC@%*OKMFi(EqLe*;9*JzkJL@zk+BUtc38o~Rtz4cEO<C;!K3~Hcr>?z'
        b'$HhVLxQayo6gMP~{z;c1r{Gf&W;q|$aXxJG6?k2x*&5b<B`m!!>}p?F=B==6w^}$(`Hxw;hf!n6pePqM7m3m8{s(B^a>Fvv^=Xf6'
        b'2%A2t$FyC;dOz*;VI0H!F+3C_VlcrnO!yQg%EZJkVUk=-x)+lj#K@!AtTWi`udq2kVe(<j*FI1lf#uO*J*~xt^*Sv+tT$<iVSTDr'
        b'Fs#qe3WxPOw4!0XO)DPOmue-$dZ$)8tgqL~hV{+bS;P8^+S$YUtJ*ok`XQ}+SVzmX3h-2D{f5KT=fmDR9~LpwKK4qOsxQph7Z!Re'
        b'>=10<kjgKON!+ear&R*MKRNngOoVkKv>b%PTS{Ja03E%WuK275&o0^JxTum}RVng@IMM({;queyeL8r*0-}aNEFF=f6#Tl#ZX7iY'
        b'BK+rbsB5_PDsKGMpq7?{C|`Mz0O)!x9C8NlkTcF5G=T9&6w6Ei!MuYDjyL?|A2MthF&JW+ntJf2^F&ijvGI{XLriTVzEGI$55}MH'
        b'I<TrOo!n=y;`i{>40)=DJY9r5h0gGF(f_j@II6mzr-$z0>EgXS)#Jv&f&Udx(x2t&&27*&G($U3KVt{vx_f1J2J(3n^7$3yb9%tX'
        b'=U4vAvvG84;66Ub2k!Fu)xCTk#f>fhJ3iY7evVH;7Uc5`<n!nqK4XwOYY}8X`ga3gK85%jka$OXjG}$5V(}|w7#ZyKH8q%F#@ndh'
        b'5rKes)&{uVeKwGJc);2!X9@;@^Jx&(Rx}+bAeBXrzaU{NDCX0F#jet=NJa~%eg`*aaW<NtVQND1-#A!|%*2GJ2khcj4fGjhyNU|R'
        b'^!sU|EO9^GXSe4~a^83=<;{MXX~m-pM45BRPgmrIkzs}y>T!Dar$7=yc+>oWp9V=HrD|Z8pnZ*^H9t5$YtbMnZ3#op?rdGMD?e|F'
        b'+psxXxEUX=5q*KG|B7m><!8~@iff|Gm+i6X2L?*s9oTBmkIP<_(I~7T%hAe8aT%&yIjwqUpgJ#V>*f=)+TI>;zdf+zX~)|G>a$|i'
        b'+XGRWh!e85eFN^|fhEsDPFX6TsI;wkz+E)3<aY_9oYfjoRMz&^fZIN>WKY5kPE|Az6;*|;a>9TH%$!NfU&YFxvAmn!m;pqPFz&tq'
        b'kFU30E~<Ak1N@?s6^eEt!N)++uMg-#kt}>p-R}nga^*C~E~XX&|5^9yK*Uk3ZWn}ldLh)j^|n%X+sO3SU?BMG;g(9xD{r~C4>S^>'
        b'&gWpALht^K@*>7OKTz__01T@Ibn`S#!!_X!uJv-;<^lKS0mu4*dPlaWLF{_15vwepId8EMYb|Yr=j1#12(9%f2-a@G{TDvSRz>v3'
        b'>Tama1L+9^l-e5cn2P=k)=WMC`EKW4keY*twv+*P3aGr$VHoh#i{YXDA2@a^Wj=|ttsHQ#0$F<#COGvQAc~P6-nY~lF4CT%8U>!W'
        b'#S5k8iizK2AjSm|v*!vFnlfm@^-3dVegFX&jQIPgw#NtDi$NWA3GjG0JXb%=v1c-qKc)<aD8{ef8_aqJxP^r9ADnm209X3dL!d>i'
        b'-9=~I3xK#_ME>x=-PnpUQL2yu(3C7p;SL^vfj?oH=4AkgxRnF3^%!`9z9TC80NA|Ywlef~%0vB)_;~@m!q*Fd(pwNmP=hn#fxCBF'
        b'w5d*QhK<C&e-uboXt@9|iwe&RLE!vH$ZhLYz>~zs(^UUGcMb&uaFv&+92eNJ)&?-QJ&m^pdG?8&83-V$mckhr7)NPX@5>fKkQF5K'
        b'T?+y7gBo*_OT$|K**4Pe9_@FG_SdtFr(6tUGgJ^B^cDPE8nx(jYF0cSul-3(%Fd%Tf)l7mNB}_vnP0lCQz6Qyz{C=%+{DRfGJwRX'
        b'MSHc>rWOwe6&r{-D_-j1a5jocfRj#-2j}$!@NT|}w0+m_{;uEgZGXMvQA?@V8!vk%iSQu3lSa(lNZVKa?yveCe+QhMv=obLJMh}t'
        b'ManPHtYuhbo)}C8<aJaW>iHXPM`HtlPFm8yWG8ExP+f(?+eues=Vj_5JYkAIr+c#BcR%x*Ku047z5>$9$2UrgF1MZPcc1Qed<>{O'
        b'=P3{a)h3AbSPh{bo4L11hJd&k1GBH0^lCoceJ33Pr^S{#a~5(npYEDT*Rv=b<3sRT7Q&|q@0j<c!HgHAZ5ap|TzS=Z&*&~}mF3@@'
        b'S2kd_M5iO_VQ;xR>7ki4C;-#l98=H_G&R4JQ04bWqBZEuwXHiio=%Rj&fxrk$FU6k2TrAjV|LEqybN#vIcTS%sF{5-AHAPA=7kx&'
        b'=e>Af2KrxkVEBU>-hi(yUYO-a0Q1gK;arU!<kuH2^uaZar~B>VGEF&Mrnd){>k9msb^QfS5=`Gnu`S~<TSlxcL+>q@lG;!D*9a_t'
        b';bb^Go{-iEUXTI#Gf%?g%9V!~f%(){FrRY&sjm&|s{x~(xeST8_w=>h?ybTaacCQsLF_8;9f=ye$lo%>c?S&Ow=#ifuTZd6R?snn'
        b')ru<rf|!EP0=xz-KyB%0<v6E7z4KLeggFGOrr1$N+kfXCmD)gf*4!>x(C@p~m4q-+{Z1AxRXP)Shy*UyDD@niSE>80wAF=qrZ|uJ'
        b'w&h2{HxHy>eM_ZGAtZq0Dp(g)h52+tMMZb@83X&ZI&17lLD47sz-$>jBaY5)3+Q(T0PQYt1oV5J7BfMx7O(#|%KJ&Us%9rhKdpLi'
        b'xOi6EtbVryAeXej4R!vYLS++?6{Ju;C2SM*yD^aW=ayb*Swr>!%~~R;!}^UAedn<nxPY4)k1#l_zv%M6Z}qi}_to9%Yi29e|HSx3'
        b'W?vK4j}V~SjRNnqYlXk8ZKTiL+gH!lC49qKOt;$)Dx$CTu?MY{gIv2)QGHN7$lW*hG_fcc{?wveV|yQ@8iqv7o!!>a=k5TNoN-+4'
        b'vpgYIe@q+zHg9&@)js#X0r;~7KCVdR&%~@JjIDj`V5T1C!a&?(xyCJycM+bSI8Pn0KT=h5AL$Pln@tF`eZRa7p6XhV15Kf&g<$^P'
        b'=QG3ndSPoHzdFb-6~XZ@1$sR*x9{MX&mbkxq5N4s#5WjWf4X5U#=rHkPGj{UT8d0x1U=TCs^B;Gvjx$PUhQM@-lNQMhzF1&f@YI}'
        b'ls;Fh&1sF<q~Ci0k6J{|O<jfr(>f;-TiOIFj^5V`drgqwUCW%_!5sFLuEM>q3#H6KABeIUS$mW1S%mqE58}MM1Oe&|O&^Ix;!GKY'
        b'YjB8L-K2V_uZoBi2z_^=;ZZH7m@k-W^u1&lnLY5O#NPLWU~^bVN*-(-NgO^D+Wv-u4<GH~d_R3~Jc!N!q+$jl4USJ3_Ki2@cXzo-'
        b'j&G`tN8%MpIOzuoo4z)AV<!e7CFO$k#&Y3)f1M+;uWnmkwe$CwjYSWi!io#1k{9~wrg|$%$)NqG;1xtWCF)WzBfTXfy>R_e2)7>}'
        b'0kmH1C8Z7Gckx#W{M!o^g*LnR9nI~t!H8Y)dBf%4>bi}6AuBBwZlm<TYnCs#%4^&ebd`Hg9dHocT$v*FgrxEtj&`8J5Cln7wXNz~'
        b'Ssq;8en_D$Z(`}D#h>m!1kXV3--ij8AgcJjcZsO5m1p*cU_uH}t?Ju_z4~ZT?3ZtsZYEMQ5ZXehR`kWG^;pu};Fvf}qlyzy@l6^O'
        b'v_C4I#617tS{DIB7cEXRCJEyB^%#U%*w=niae1n+XJ`%_uwAo@ep_2_ZIE^TnFy}_eDM#4>Lw811-HglU@bp@`9t1i5HkqjV5obz'
        b'uf0l9TW!6H!IBrFkopMZ!0h7>KH5h0xv4&f3XGfn%0Th)2SefM6{$;g31zFAfQHls_g$_oO&2t$3z=ZpTW8bDQk)nPTpnEQG$E^Y'
        b'2GcE{aU}i(4rSBEpWC3ejlfOSR0q~O&d7Tgo9tqH;0k@1admIqUwT%?csJ3$K)+L1p5!QM^a*LI13imgQoJQ<o#MZu052fz*s$hR'
        b'fepm*n!!FHjJLpG+bFFeJP(V7-n-H254q@(UJx=XpTcaRNJQD@GXFYHuluLow$>iIza})wo*zlsV~RAIWs!-RWd)e!BxlYf+IoB4'
        b'-M#e=gHXVKh71^cDPrzI+OGAwuK~Euai!NI65Gy#AV0^p5;2z{?FEW+P=mh{2bbq{ar&5qs~m_R9uUv?Qp<as#qCoW7<097c2$|8'
        b'&fV*7>TRp)sVF0{{Tjkj4{X9oms5(gUT$|O&Q-%>Leg(5&|o^)E*$sGhZw9k<&&Pmm}HYYDhAB{l4Il~ws=wOM<lbj$H0z~f)x!o'
        b'loN=HQh}5IjAJ)YMVDP@QAOQ{y$c0QT`$~aKGM4(UO41i6Zd2gSy2QT<jL{cF6Ict@g&dOCuXX8BgHfKh3Y9os#WFa(O`Bz+Ci+-'
        b'KSE*=0a1>Mp7R*{zMOr!sSjP%w(?{3zd`8peNcnqJh9;v2zDRsflJ#cu!Y{cF>m+ozRX{Z@m`-Uka+!@!H~24Prct0c2Nyx7egnq'
        b'L3?m745D0^U24-PitOiwAdZJQcnz)>HA?mVH5mLj1%H>><`CrjB}8a~Z4N9#GYj5aa?UDpLJR(r$mSsOONSpEWOnsNXy!3Hd-I(D'
        b'4;Y>v=H=e}((h;o&Tot`FZJ^Fg?0#e7x)<5n#`busuz1xvU?LT4G1)u=b?~JUoF}SW*6`uts#;A8W7b3>&_q2>y_I58-;ca2-qR7'
        b'QkYB1G=4QW$X*q{P^x_GCX}hpAz(vuedo;in21>mYfgW%ccXNdum;;DY8N5X-9?qDG)nEDQq_UxmyumqY6Oz120;tl)fXV&FFp{^'
        b'h}MX}YinU5u18}7Fo&U6FT5ijJ`QD&NTVvY*XfqqF}nuNE2iwmvcR&W)7O>Dh_bYz_2oD}ohietE~-q@E<wzfZ@Y|*s6EJ@2=QOD'
        b'qh-c|^|nml>l&pRKbH|S2d;@bLVNSz-j&mVdCw=NBZ=5j3|LrYm@JJ@{!^M5pnOA0Vrk1F739!59dG^S06o%RkqV6hNG?;zC}Go;'
        b'C&i#GxO$YILy726l%^j%;0Gm%ArEv*RDbGDL|4?Kk*JaAt-&>f?_8w0f*>c>=>yaJYw%RH638OeAzoJ@wS^M4v(v{kXbtE&$TZ&v'
        b'3#AD{g#2h#9q7v`sGQ75&q8T_g~aqJXU@3|`$oBSEa4VBLh~cwL|HM$?+rSTl+GSHouJhSkRwe)+HXnCQFAoLG{0<%GAktQW#!zE'
        b'G&)UvV6IDdo+v13!~rk%5@i%(IVEx#Ns%TfZO6{J=&sUi+m;mNd-FD}yJ}uOFMC7mF-&MdRz9^3{AMC$DaDyr%?W|U&t5fmJfI{b'
        b'8T9O4rRwvZ7l@6x%V-a>X@ble(vG=|-aP<i6iLd2s}LH~Dl=}SH}+_R8XtR$1ui2K->nHMS=Oz&T7Z@-8d0yFt}FxA^}-hFz_Dy&'
        b'qtvb>AHFKqz98*<PfAK_Kg?y}?GtpNjH&K%8PmjI{HLl>(44oV%EjaSa(|7aan^ZZK}oseyY1K0CmDbVZ}wvLk}}7o?Oo{;jA(0M'
        b'!=(%FDXQN;D|H32N34gB3hF9))-6FBvEZz{YaA&9B|wc)!+G5t8CYiARtOJ@Hq1Mcz4NiKZEs%vzRUhQKt}-3UR%2@t7*k!blY1!'
        b'?mzZ8{@7FRe4+9Kk^MPeepyPz+TyGx_|XbdOwMZ*vnTd$D#*2-qRtw@6uHM9SVNXOAfiKA*wZLUd8y~TOd|k#p>rAgh$}cRu)MPz'
        b'^J0(ibB_6KPu^!hpMgEeJL8Qxz!=Kv0ezp1C8cDCw+q2!!@QNqHttgHh>$Bqvy@NG+GVz<<R8acbjXIX{oq%N99ixHo+?|K-2w`1'
        b'pWnUBlDQ?_JSDUntI!M$mJv>vvk;R5h3h>oeM9<r6yVv>7o-L0%B{EW_VE+a-mNZUV!A!Z@N%Y2BR`u0Y{0kFrek~g%p+0vj7z;y'
        b'6RJs7I;UJQjY4?esEb2hAcVb~3u`3K1_2xr6e)V|yr@wKMnUU!c%3<A+uEkr>;);W#hAaoX<k0j(#IJW^dx)-+HP`S3Ex5)xDh&C'
        b'tWpCZP#H9m5sm>~fs$3s$!4Gs6w3TLyTW%x91yu4J1;13Hxj^v+1*7!mOUb6%xr*UUU3{tcnsOF4+tk=5uzNGd8PAvLH0YKuBy7E'
        b'lI%KV2a$g9dYog^=1dpEYkQI1rzz%cF%Ste^T`0Ai#c0ji$WV5z(Z{MhT62V3BcFIs@udpZgG!8&{Kc#ElZJTf!Mk^^E`|gP^JX7'
        b'cAf)xY+g^!i`g&sZUcJKN?l^?*!QRHfsJIjyJi;D6nAfwy<}_5R(nAS6a-1~Le{yMK7rwDidPso6wXUPNX4{w3#U1#F8qzU$Nr6&'
        b'(iO(b-E_K~4g)5`;58YlYuy<txdw|+LP40LX3;8z(l#sGoE&P6IEE#}AX;jXc?YR{Q<e-~GRO>-f_lkH9kXuRw8nglpe#)`_E(!5'
        b'Osh%In2oS8tA%#Lsgm<<6Nu=t5G1Y$%Yx2}N+W@Hu%*L$ST>d4>62}rb-P=-9iMd9ADZoXO|)%O{P(Yb3PUC~H^>)|a7Q)?R=7ae'
        b'(#;_ukic@74iUmHT<n5Gc0JH22A%qrv~}xNdR;x1_bsP^aE-1{a0Mqxkc;s?$LSFAd-%XFB;4eG34Rg==W)#xkX|EBN-NKC>NmKV'
        b'Zz<H^mfV>$cB<FANsDZ4>&r_8HG&p+$*~4w%DMqFhhrq*_3dtcI;=Z`+diDO#>ne-bOS$8S$$hsI2}j$mgeC4+Chq`hHZee3%K_A'
        b'6VjI7?auFZ*t_f5ot0Zfl@Yh?x{^1$t%XhbC!|$0?GP0a@QA*KhSMHv_u={;(x1dyCSjaGV{j?X@DXKpBFt-$2@ot4NquVtAZB`{'
        b'+onP9`M$=E?)&y>J-4|#xSn%(R+PZWqLts{mWOXw(LNq4Z*rE0ZaXt@nnmty$F6(Y!EA)IoixHI;fu?U#F#g)-$OS5f~zp*_3Qk?'
        b'22T{g8!_*`f#b<;=Hq+t-E_BiIlA)LZ8nPXu7hCecW=+sx4hdsecTEQF-N-Ue%0+*f1R8|wU0(LU{@Uob*kwiYZ&|o#XJsC8GZNe'
        b'>u_o;CZ)cwJBj(^olilDne{#fP;GalJdR4zQeWed$bw|=21)e%ZtYM0-o=WdgVB-QaLy@&|1&o_f`3QDyCn#Ch!K^#TZ1(r2>M{R'
        b'My{t4wI~g;e5b9vXG8FCKO&qaK@b=M*@KIO2onrn6Q+Feu$PqiCETd&=2t&bl-+RG+~OekOI~`6zeJdXsXroCJVk(Mhx~R#Cg{Lt'
        b'D~E1DIYmpldBh}~4~bx%@6of{1l?{yw?hc@?d8g4A|ukxuiSe6OfXn?d#QICTqdp|w7z3ZmJbLru+^p-xz2y@?ZH9S@bx_3+NpOv'
        b'(K2=adZPEUPd~qhjHRP@&b2MSg#PzF`HJiOk+ro=w`O_!dPe6cHYa2PezW4Res1Zx;iWR?xv^s1UUq&i6)NW!JZ$IOOJ!DFZYlfv'
        b'TlnEPtad&{X()=y$(xzCP}Y~JvK*_8Dz<~Hm%Se#fa?c7eVm~+lde1_PIgPyW1HF}$=^uU<H;?O_52|mQjT=_Bgb&0&L8;(hx?E>'
        b'I63?Wy)&KsPh8IbPm6DHd91h2vK?<pimL2bnV*J+<l)Eu{*&HJ+D@ATQ5U9>@_`d6^;r<RSZTlQ(!m%@dYiv0&Epo8*#nExcsQJm'
        b'_+sq3KV1)5U4w#=IME5M6Z!<^!W)TTnkj^ezA7dwwVw>GkuiBby$AkO^~QDM8`o(%h}82MMh5vVJYam%`1<vb2=Bd$I4pYib>r{('
        b'F@<}t!$;z(UDtU$s}F@wfEr8=tKnXd>BC$AB|p6nXngKE02;SmpMe&%sdtK_H(w{icp@Ze@R4aG$slGY<T@q&dg+Hvv;bL<3x;v}'
        b'Z?0=;ie8R{;3Niuf-88Ou_}7OoIdQlko+AP6q%ls5~+$*yo#2)BN;lykJ$_>aiUb2+ns#9xI*p}AXjjfT>}rO8>vz^Rj!Cr!3ypa'
        b'H%3NBqFz%0t6%@K)iWtDzhvokh*Azwi2p)KgeZ<juagB=@N%9_^2z^Zllj$k-t#*afV!%pVOF`(n+a-_oEO%!B6#@jQHZ7!VB}n_'
        b'Hq73(&fjk%5gs#Zqd5F2vF^-dDobcn_o{-gug5IUiOHbKOtJbq&NGKo1ztA>dOK}<Ae6ju?)5ueLZr8JZu52qZ*Yhd`SneA?(leR'
        b'&;sI)K1i>V@N#n+zHKdk0|*|fO~g0F%Xu5*?PKgZsf4|ZUcayJL*CeQzslUJ7vo(}g$^0+5E|*?RU!>H+(QUU8R$xmm#6f1`7Q}z'
        b'Jj(7xhPCp$+@xIZ+T_i~jh-&PQTH{+nAbT&hWTfw&%ycjiCeqw-1QD|`o6(d)ak4=_!bcO&(uknuewOd%-MCOt&1vNQ+J_jupH$-'
        b'8C6>@ulsvfZMFQKGtn+_-MKF6oiKO@t6Xt^#%EnrIn3B}Uq+djT0l5!IJR8AjaK+RN9gruCF{Co(lhJSRL+sB%tu|0kGlAxs*k#6'
        b'sw%1Nx{r5?9r1mSi8<KiWUc>ww%hSu*UaJWgwdIAUUfM>@AMw^mVr#liQZSl`2pm!*@4KM?3a6+?yGHI7u|dt<T_sHqTb&-Q_SgD'
        b'z@&H1oFi2gc6ryde=*ma&f}TJR2w_3f1Dd0I7jtHS5cWNx65|+HYu@2?)A01WOtY24_#Us^)``~J09p{?Y>WUL`ulTOyV6H##g#_'
        b'!>>DL6RD1NYZh$a7J|RZK;~`Q2@AYR7+>sK=MU#lP_GDbb<<jkZf@sS@X1(`AcLu#TykxQi&~X?k$uj|W>L@NQrWo+3Cj=DP5)F-'
        b'S157;84Tc-E7Mnm<P!e9^84vq1UZ{rNIt`-JwL$oljI9C=_}J0*=-lTrJ7kV)KOUCyJ_-4@)1zxK;tZk@vmuPLYM0K4xX(D!8m_w'
        b'boa~N1Lu*1_Y&#yWN)(x)%>nFjQ{>%Y8Z6iR(^D(K8t|1Y?Og!tftoNC9^KFTVM;G-%G|W6j&}!lWP<HKJ!hug<a$mLt^CoEWiWc'
        b'@rBB-rkThtG8n)B<O#qj0D>|L3YmcpcsvthG+i(TQ+3rJL3q8E#Q>d#Hx#{kpw;dJ1EbhG@WlLmy%J?tvDfv8qd)6llwI)Hm|s^U'
        b'4jw+ABWDy{GoEKAPM_n|4J$QbEgs!pDwf%If0rMJJ~+6*CcN!C8+nV1SWHnB&Bb*__LQ~wRI`mmj+aVpnMjp?d1zz|83-NoGva)|'
        b'KpV^E`#n&~4wB;irCnqs8R&Gh!&_hEmV{}Jj1&6KPDFQi^5(^`G9WyFE{YEid&2htD!g(G-ct;Y(H1r*VO4%{bb&5mf@A*G$v2bV'
        b'a?ol6tTv+elG9;m&3#5pE(0&Z5iZ<cVPglwLqAXG<w!f}Un6em=bpd;Ph<=LfjLaOdGD<!#AN0(V92z4zd@IdJcGyjDRe9wTZ*-;'
        b'Ms(~Tc*$Fhm{=tGZ=Im$aK7hwWqLu~Fdcoelbj8J<P+rcUSQ=h*mYLE>rnL&7k#Re`ct%4S6@=!seM#sjcFoxA-KV+tz$m!)W#^l'
        b'e8(Og(eSL}NN3%VPX6{@tzE9wQ;Y+q;-q{_cb{Wp<c4Lu?G+pU(rM#WK~L0xXhDA0#V}=^AZ<H@_+khmdPPT^1VDY014mKk?k{I('
        b'7!oOF52TR<X(WoBM-bNQZp3`r@n$DT!_NlB`{*v}sKJsX%p0&eqqUQ<cJku`D3ey_rPt!&$bh_$pt485-g%KFfNU<Dr)DJPIW!&p'
        b'+Fglx2f)E;GAyCqH$IG;JH6+ObYX~gaX{-t1MSjTTDdHL%yWP@u33SaaQ_hFEsw4G6EB`u1iELD%CEQvKhH4^l=z7QI)G$pTFF8t'
        b'4f3n{HS9j@?!Z$Ym{zTVykK{E@l?RhQ*?N*)MyAGX6s!`U?)_DPRcG<Sv-{2<`b%=oyLUDBuurW)3}81J<MR28z1j9_&)Fqw@moG'
        b'jB^|if#(y>Qq0})iNEN);}c7$P9W*~{0X^%8Svb>5Aci5=Wp}fLTQP1&`mK4pQ{x|4|^yF&mV63fCJ>MD-}NSUboFqoypY-YrGtE'
        b'q~oE^I{}51dWUFAQnb%}tl6t;(%m0{h@m}6aX;`H0Qzi<)G@o0`kL^<b1u9EFy+>}$ad-Oue5gg;1$IMFBeh=-bsB1@h7BLKm4(_'
        b'NYT#8tsKmogas~1soEUF75RnL3d0o${mxs>V5<Vu(`2WjM>_a=p!LIR0ms#HgZGX$9^KzzdY}KGBo4g1p;}&C!Mj1+_TgJPc8Ap_'
        b'*PfEs+9}<K@KX|2YmSMv0<#zW?~WDX2(NU0?6CTRn&|I4^7-%0f_OQ{aMw6`@xB3ga^a|VJ6(hCe#1b^`OoUY{(Ay5>mKmfxvU^8'
        b'ZzJM7cboKMO}VOS-mzfGX~ys{EH4caSuo)`SUwxGIS^|We`gzG+#P)Q@p*<u^+`u5A39`Xn>OVXXHg|Dd3YQM67SCw@mZp*0o6wx'
        b'B_DTapH=WmSDYm;sqZKTeebK1M`H%Bm3+|Q^T-&Ic^9|pUR;&4!$<I0z@_jp<U%eA^4x2@l+(*Qn5t`#L7^ks;~Nh`hV<|t_NWuc'
        b'lRap=$RCKHvk>NGsI`m%J{`+EOku~n@B<JU7)2;)scKJ$HzJ8JLJbl!rPr)$6+Sa2jQ&jr5DfpBLEv0%A8>&CO};=iD_{=a6R9;^'
        b'vM(-va4=kl<yCSdk#Gq3m9Q2k7ao8K-{;a-ci5bKM+tpiP6*Jl0_5Jd@eOk)bO_IKgZBW89W7_P{i_#?e!}wFxP)(f<M)r;Mkzee'
        b'r~WsmU2c0pN{Y0PI<x3COy4zkT8A~%W?f^mzTr&%A7i0yP=h9?Qf=$6SsyXh2pTaa8p?uwvx%IS|0w#dsJ6MOxV6c=K#>2~udClA'
        b'=dIJD?~*6!sK|)@1c`0d>o2^A$~J6TXe5<~A4N%_jE)L7IE?a4lzoq?uGFR*$>4R1v3eHSN=KbKPh7#7K#%W3rX<F@YCd*tG+u~7'
        b'&lBXV3r<vfielz?k(SDQ@%Q`=RmC;l=0rzz0F$QD@Z(Iv_Yd!XdE0Zq&k@>D7uIne1AWZgzBcp8R9MGbnC9wxezP<#r$%zP^np?h'
        b'7I9tC7S!Pm>Zo@vbIj|2CoZCe4QG$*h_Xxjb+R^Phua_I#S166vkjm7$=dun+;ae6dCM>eEr_$4i0745c~eoq{zYNsg2b*9uHt=7'
        b'<z0{-Rl$R2L2#9;IKC;VD`ApL5~Ot*);6s)t?x>5&BWDOYrp|<+bxg#mZ#pi#WC)IyN4QKS@Zs*WZR_2Jr2NI;UcE%V(dv-+o;Dq'
        b'3?R>e=tOsB!j3oi<)0$kZg|{%0Qy__of5l0IsdqrZ0qy5y8vukLN|wqvSn@E9``kn-k#9G?LOUPmy;pDV0G0O`0qZie+Y0<lxDA='
        b'aE_NL^>jq$ukH0^w*7(2b~gZhkE8SEAjoliZc_{u_fUDgzFxbyX)G5lukWf)807S`ACI{ZBi|FVSZ~MT>I(~E8@_M*hsXT|pqAHi'
        b'jw^HS4?M>A&s$jQS8eA!?sFg~*wN@w2MJ-PkYz4S+5S=m4f^D&tnFiuyBQ#aw2X1ZR6tRE+b16P-vHo2c;no4_HZ20aOrrQtnCAj'
        b'y8(b7YU$-J%_HdxwES$~CCRs^XSFuBedKZ1fxL%-n?GRENUL1$N+V8_Z6A8v?*njzu$@EBy1FEL7LX6ZyDzgYT*xucMk5|a4>YzN'
        b'_PCt@X+g_3-0^y}sHW|p$Nd)ocqH#4cU^F)OLpbEu1oVSTqM53%OtzcJYKFXm+vXBI8c15>DV5k+yxY%%GGkqr`z?kn6go|?E%g7'
        b'tfC*<N<8jTPrYM<<M$r5RCuZR^Ha)iANQ}FZW{a3ytcPI?n03H48JejR^V~xgVfUrBi!zDkArEGd{5QkPeddg8GK##oxRLXVv+OW'
        b'Bzq#O%fTQ$R^(p}VETsGa&ei4T&69j;1|fhv-|ECY7GGgh_=lC!`RorHC^rhpYL}YO!%tf!HIym4JOmHV44G>7!&ca8<LMb+zaRs'
        b'y>=s`w0?BmhRRSXL{l)T4JFYlC1{DI#ZU<iOUz21Co;9NA_YW6zyJ67ZtA_ihu7<mzV|uLkDqhS=bZ0(a5-K@m}~7XP(D+$9zOe<'
        b'%kdJ7O%M3&IhW(_FfqINY=+3{KfQ))TIg~ZVY=SKXA`~#pFQJpq{3_i<uh*6A*pZE3ogg=Fv&yVV~DoWQ7u0px@({)WKv8QSDEu|'
        b'^q8MS-ZP3UDrw$UL8kv&G-5w^YfMQ|bdiU*iUx|%M6AQ3*~hI;t89~X<GTE!*qFQnZB0ooM<T-iu>Q2CjEgOWwSn@hq$$?r(8K0o'
        b'`&gH;S29p{BSvgJn+IN*;&Q~oVnY1@Ez3!eQ7fu9UF1S`m-rT|3X8=1^CRhOVE19Ja7XQ1zLyX8yv5bu;tS7H&C!eJRcFqK3+`xG'
        b'TS=|<n5?j<R(JSY45>XkYA+u?@zzk!zFNh4Q_4~<WvTDtU5mFaUdKtsiSy4b?p_?ea7$uTh)bbNh?yJ}?0Q@klNdG16*G_iEX_HF'
        b'@m^IoFfLFjcX30<WtSa~Q`x%d;auZoGCol`$~6w1?YKY`R7QXzCOk^&Qq}b!BwyFKK!oJ&Qu@%qybzezA3PTZC*IU*GK`c`7o13_'
        b'y@c9drr#4PEGa5(VXS!3*@dygn*Qi^FfMy@ceVW&ms4V!UpxKNkmM7J$O8)V#V&dzTs7?3NzYo76KfaM<##Q%R9NWlWpf*~i|$%v'
        b'nT1-NH7)w=Op9)-D7r4jGQ$#Gt=lS%R$)GhT2;*~^7O&!Drt&pXsRhteuXrB*X`&=oS)ji=q_)Ttf^Z)C2-+qeyQ_o``3?b`lj2_'
        b'4$DJm2~A&jJ6fRr46OM0)|{`iUYBj!zWvjQDJKRteUvX>?6t=tAK`Ucf+QWHNwRi5J1K;wHhFbzeit`wv3yY-O*AK&>9aU^(_WhR'
        b'Jr?smck*XgC{sqCeIxsIOV%s3{dxaq4mkCOs~&!HZ)aB5@hGFyVslBC`*LZv{3P9PVke8|E>C;iY~0JFC<D`Nh0pF?oRDJcE=%)H'
        b'O*bW{n5vcH)Q=SEP-bkf_bMBiNIySSf5OvE;!1k!gjz@5^cfq>){h~@DsDnyqs*Fee(q7GU_yhL?pLLmRP7OYXC`pm*MV`?w6BA7'
        b'^pIa9oTbszjP&D+I9jAb<rZ{1-s-O2Ioh7qtv)7+W(tlqZR~bfVf0YaE&ilfr5c8KjgN>f`Lp$Hy!%jirC0e^MED3>qzoK8WQgm1'
        b'#`?0YqIM621lPkN7+MqZV(8_MN#9X^vexAt7}oS^x8v3B>azFkN!`XH612NXzD=vT9a%8@0G&{DnN<~29g*pka{$6}zRJTB#TNK>'
        b'H`8HFbGjWF-S#P{?dirENkugmga)cnDO8xc375FI8>o(+!JQ~Y0~J~%n&Spx&$U$*aYcy$s|&5Q#q6aZW`}j6H1DviDW%(y(rs5D'
        b'+;CU5<o>s?7uYto>8WnVQz(uV_EFvRi0XdHXOp<5S>28qF#LNxI>fPI-jAoKJ{eTZmsQ)Ymf09}y=0;fC+EbK5=Bz3@u)<v&wkUV'
        b'ak4Ebx8QgsYy47D>8<`!h~{iv9K8^Od$Q8YxQ(2(6}FtcuYZ@cd!J_A+t$@bc)Ixq^ZFRS#<NWicRL>LuHGfG_g-}EmT+ENfPTuB'
        b'Oh38}vmZmKy4w*3Yq7A$on-n?|BUq-Lo!t(GsK*H!BlUTh0)f<J-auC(b~HADBqOCYAcwd-s(P*5j;QVcBRO8o6XeHBN|RG@}f^h'
        b'@c0_PMTXO2;Tkq!<M~rQl_K>}(baBlXql~$^2FXU;|Ijci;%GrA1b2cFqul*Yqgc4av#y^Pe0_mCJMU)A$XN3=}a2E*L!3G#)&Cr'
        b'1bIh7_uuzjblkXDy{p6i<wfHTiAFUNqkZp1$2FLBf<qdoxof7&Mht1>tV8DfR#EK;be+OvrMn<ZlQ2%CnS1Z-D-G|$MThHRb-Ay7'
        b'??vOglE!0A7cV+4z<?88(=ph(^#&8ND=xpvTGOdaOxHTZ<vi=T`=BmPz4_j^$YRx7?8xOqYRW3ARW`Ewy?}}<9Q#o)S5aXtR@s=m'
        b'9c-aWeBUi6jrdtvVJWV*<=1YH<*a9I*4m0X%8S-lEDZzOtVH9lur8rv3MbugPZn_d8&zScsVlBNv?Fl)4nHePooiT?it)JL{<#E!'
        b'Zn()?&+ad&MYubxmWH0Bex8#G^?g5_p;Sf#r(X&ZY1r}BiS9e)>^m<CN3Wmj@*MNtby4V@>>pe-FQ8`T_b)p4`<dPzp|CRhs}oFL'
        b'DC{K{tG~Hpewx~<WA7B)vTwWin|C|yQ^n?)UH^98x9H*>uiqr?Vj6?`CU1OI;yD9fe*5<Q?^;UFH%(>UMMap63y5*At-C)4V#+dY'
        b'q~{U?rRky~+!mGC6*<|aVN1I-q7c<MQHH-<nb-vj4O>t>iuGG_QS}i~gj>e@4dv*!LXY2<1;39`zl81&+XwHy@P0L2Ioa*Ilnr8)'
        b'8Pr)cTPo7ph&G*Wu71~t{;nrv+9)DrhW7mM4@Rl!x_^K*nhg@guo|Y#UlXOcd_7tz^^++`<fQ=NTkAtz?)~7AT3fV86QK1ck<Ne<'
        b'fdo!ySX2hMBpTv3PMP({#c@$-vo5C6v0bDPzAc~V@X{!uR4gIWf{D_%>)%eza-tY!6sz&)L<mr>BH9!(t)E9(Mlt^xWu#LCJHgp#'
        b'&#~J-AGz3b-8L}1^rb)lydbC=zx(sLTUGG%z?h*u-0-12?(@5g&GbxWepQKMPt)NGU1@&T()=SuB5hhgB*CvdlELrDNS3}aLJAdi'
        b'X`{}j1sA1-H2is1DJxQPDo56dD_+PX*F&_j{z(isiSfHgCMi%tq{?&DxVBLiY103%zj~A2{khm(B%~^!PC4qVGPp<?GIR*7UeZnw'
        b'$NEmMp+i+lxmGz+K>}3DphzY_!3JoR0h+myqJZeM880s~(*vc}s$xe)Q_Te-eO*ewYf68Ff^t(Hyr8X97;I!FJ6omG4&39-<X=U}'
        b'FNi}$k@GE4|GJPo$z(VtOR<sEC1j0gbrG{zG<(wYN!L@|^{sG<O3(gA*8j{89aj3Z>Thh*hZhDO^-dRE8G7qU9mo^6o}`KXjZC{t'
        b'oqVVr!zw04#*Art_kVTw;C_J<U5@%LZdkjhdKX((7h^t2n_0oB3y!X)x~{6auIEEt4g7*tQuNh~*ecrmC4IJI#-et%(7m9rh^`c5'
        b'a)GB=dN__=)sz{eju5xglV$W|(pWJREEHqJj{RMNYN*FZ9V|u*7W}!w#BGA5dW_($Tp@OR)YUZKDOmc6CyF=x#%K875DpTGT%lrm'
        b'7it12S26VF_*sPWQA-Eib96)99M5^DcUk<>NqH9+=&E2jHZnZdbKXW+l1Whw!=SgIl!<1a;u>G6P^r6_r+i{mA@mT!;x4);t?gWe'
        b'zd6xK1s#8_N)~I4R^|KaqT8a`7=K~nT%k3`IR)8NR;)FdQa6@Fvn5*HVM(!SV}8CiBYX%ao<3rq@BI3oc}`5XUD2`Cpz<HbG@fgE'
        b'smt+FS5;P*J*&$VB}qR%C+9X5$TkW$0)-D-)Vom2HLd7!WOP+6@2W?9!p)+?ICf#p1mVJ;Y3KkMn%8T5a&k6VA2!h^LrUK)ShTg^'
        b'-Lm81t`vp~w1sb}^l}x`-Y;Z6oC&8@rX_j4=c6ntMWxSMwZ*Da)_m>uXpxo8*VbswUe5bxcu=Nv_@YNZOf+p;c3OH}IHUmbOxUFn'
        b'v0C9|iPkWU9``F^sZ-aRZg+_(bu#KMH|$c-6ZhOD!kz0KmTuZeQTfZKG1WFY+W*cM1gn=ZzLVgg{)+HQV3B;pEeL^0%!UD8cw<Z~'
        b'x8A05;xwip*tpc=R+vlBaah^qP<GizcU9ZRxI!fv0X_*=FBsATII$r;(9IW>Vq-R2jmo-K!4__^?D5~YW52a_<Hiz|`x3COd~MDE'
        b'jmeNG{7&1xWh`YO!}b6feR=E&rr-_RuOeHeSpCx-n%!I$gR*emi(1b^8wxkhW9j30sArm{yB8dHFI3yp>^Cly2S^%!Xd1lWxCH~F'
        b'`=vcDm>Z(sky}`peblG%X5@}7jeDAUFF3Bj#qy+U7;E*LwwO%WjRTRJavLj}{<z@y6;>-Y{K`L1pSa1VpBsyryir`!&leosu*$CQ'
        b'cJqmnSZqw>v|N>OxMf<>Oo`Sg<3cJW#@~33RT=$-V+F!GEM(6gE;w4?*KYsz0-cTzkwlhR_Ju``ubb}gOD(^LWfkT?s!#s4yV|#@'
        b'>4M{1m>f*H&X=8<=NciQtuUBgU}Kq;^p=l2j95<1)27Sv*_qeqWjYx1TrOUl?(Z4D@3&FobF4*$K}1)~M60O&A8cfp!gE&IOlBs$'
        b'$<i|X*9FI?7piwowtsZN$cr1Vt5mXrvZm?_j{Puw3?fQ~TBf-%7HR$Xg5zH>o3f#oFJH<m7|*DbVtE~D+H=8C4)YkgOIzbDPw^^('
        b'Y<J==>P|myi$b5B{`H)RL+C|%MQIXs3gz9J%M~|@=k9)-l_z@9qpX#5Az5=70<t#3Uw%v^_a|+MM`28b^*Ua@k+}Jy{L?#V!>%-z'
        b'zGk6`kQ;86KhEs-f4eFFf@2+$pr@+^G^p+JqQSDS!(Bm)m#|-|OetRQIic<Uujs3&Sz}BkQ?6kuz0@zzM&(sLgLQWhGiU;fyc0=D'
        b'SjG^#D@!#!Q81bIZzj{=VKH0nkX173vCM)Mv~#YwTzq4D@UTkn@;V;Y3t4Vdy@RhwDEnGw^kOhuaKKo-fOTiZRdL7b24Csz`ijRS'
        b'OgN{AktjRzd&N->(+^h@KhdXjg*o5?=X-ekVV}dXmK6cjD*}b%r``9?deQoueZevNf?ao^y6j!!Mez((`FMJYZTHrI8Z8&#`^8~x'
        b'<0k6KeN=j)dks}ln~iRP?hpKd9;rk;H=X}8p7M6yb4KGu7V{P51&8)R^{z4Y&<n0Maa$N=l(S6{7aS8|s&JpLr@Ycnc_r+EBLc=s'
        b'On4v(t*WPeocB0JtrgxTy`<@nh~YT4=)_$vxUg(XL@>QmROK~|&hRU}6pC!)dpxm(Wk~0%#`^EGfEB!qWqg6SaTe#lfgyz6inWwv'
        b'?N+E0*b2rx^uoP^bF}{*J4F8KowE9HMT#OFJh)&B`epS1k*f!7W49=5+4aBiAu9JfDypPu^`3j`g|>Rd>A3Bz-sP}gbkYv_Td}(}'
        b'+;BSjU`!ADX~b=;CcL1o>AKU=1G7`Y{h5#~Qs@X%DN%<DIqY83%dx8uKQA0moEB1oZiaS&-DFKzhWCP1;r<aL12Ei*U0eBx05)RB'
        b'MC8lYoqkpL5c##c7+|s@AlfjI;aiYa^;IG-yJMT4tG8v#gYVG%FQF&S)lqDvm-)1NIHAwM2$!m31p1X1+BoX%l+$s_SzVrC|JZ4C'
        b'pxz9~(z&L3r{e@nSGen~Jc6NT<$V}~Qe1Gn>7dhb6qYa1PSOh<N>Ug}K@0j+H~>B#Ehy<xLK>%3GR9uawOkt3)8ho94bkx@KsdF@'
        b'CX)GK84_>dFldU<>8G&M{=<xpYOZkFkYsj+@lUc~qc;Yt*Lk^*7aC4oc==g6?|6$IM^||oj`7tyoZJ)NP+?<Gmt4|MCw?g>_;Rao'
        b'4zo)bRtm0T*eE|w?u{ztFVj&){g7u=p^Gq98jLHHrH>U*eIDID8Nybw>X&)>iktPv-TU)n5}p$J%GFNC>(1(rhS;BTmhTh08$g!R'
        b'kqxt<?&nU_0gUZg#e!Hys}xW4DfqrA&FOd%*8cQF%L}ab_#Cf?i8Y~Z2DmEI>BxZ9B8)eX$^u!h$4KL2=ukT8yBz_n=Ym(B$+=B8'
        b'Am3#KspLP(G%?XFsr-l8Gzf9S-F=g>jVy>Af-+mm%TIYP61S=8!hq{0QxR^AV<!60@Q1P}>Eq$*BdAIBYI-)s*HhBvf4!4pV}vVT'
        b'%ln0`H{Ehgudh`@Kc41yFE9}G^UR)bfn~*VmMJ?fD|g&4ZP&ARAaZ&OT{XQO044vjkRdO2!_TzX)meg8f>vOBmY0veDL32^lJ^IV'
        b't7dD#Ce88C_f#sn|F<HXV~w-u5gwKWYv1epIHzNz(>~ByU3R*B3;I4+3pzf|s^x-1AZ`htg*<zYFY@wV?pjnLYVLKD-WB$~2yNqP'
        b'r$g$j-d$q9+*$q(+6LrM)S1}n5W#eZyKQ7GA?bpQ=2gO|FA3$)#fgd;UC_fvhg5nvJ)cph@m2;sjjwQbdKcuy4Cxb;Jq@~dM`~>h'
        b'#uj5ggD%V5)k(iu32WkDP!utSWxaZftCGl5?${pNBELSEvXmZyx-U^066=3=-?fZB>Z?viduLU9r~UIzDo?BvTiB$=Amh89^V})I'
        b'_)q1yR^if5v_dPABJ~^*cgtRAhSbnoxCaoD7@U`1W!!Rm<9fP!N*mvYh|o3PbGH61QMBW<xZ?Y2TX{Y+)6YEEj$EAgoAJHx`#TbI'
        b'PGZVpWeiIK<eDMekWio3HV)lUQ|(K39IKuaUEmv1!bvStr-xci8<u2V$Um08#GmuBED20sGGf!te0nyshABH1s;*(IOlXNIzxKRe'
        b'!}m2!`LE308S_lcPW7KmnLU}CbJQz+i9CJD$h|wwZ8Um|ecs00^cke=SgMg3w0zH`&sZQVY0#eaOJ<K~*+?dauDn{NM$^wh!gt2P'
        b'&ifB&NzHF}HtrCvVRYX`Lc8uE#WDCd?%tkU%4h349qT)*HgwuIbgEwzTT~<ER#L5!(>GS!@6QTv*`}H;ox)?eVxx<(oMkN1`3o9I'
        b'#o6-z5~EZ5FIqoigL=nm`kP+ubiCSG^;)NWRi`>rd~e^d=OWAzFS2@Lt~0|g>J^&OHKHTl_7^)*r^YXt%_}<v;lE-?X>3(*yYskT'
        b'MNHH3&Qss4_~NG>a>XizJ-yTQ9W!{yoI#T!yum`&2p79@+egyP1jWAFM~*6r@PCUf?5=gL&ow!-+rIsCVdt%qLRW6vBNf43ztJ0$'
        b'jXm@iQ=j^F-nEOdr*yhsi7h%QJpQmkC@GPz@Mf&2{{9=I-?b;q?4&2)HNus_!aL;V_|D?xd7~nP&;2y*tmQmIZ}?wOc1o)LkjW6y'
        b'31bawkL%p@MR_rE|IK3(IoYJmWTzhpjGEFZY^o64363yfOL&MHmW5Nt)hbf`ja0pzQI6^qc92d#a7ftsS^ukW5ApkLm294Wka>6e'
        b'y>0PUskK2@Gs$&=N%FmS{dGZ&`NQ^mcG1CZ!?8ib%q8u@6R6f8YW@v9#qLwzbMHPOuTJ3tJQR|&GcC7`M(-1nDC}fP*wnsk%frHE'
        b'MB!fAHGw*LC>Kz=+FGAkx900*H85Ts?ZX8u(@EURJkBM4E4B*!xgcn$u(^?zp-;xB`J4MYLbn(0QP7ii>UC%*#eN~yqLYEEi+{HF'
        b'bhs=Ge#`OuM~7PYb(tBvv%`qrOC4%6V?Nul`BI1bmHDoY&8`mjMW!&b4ne0l1SZxxfwS^H7y9=h&I-Scd(G!NoO}KDR&1(PuVo<J'
        b'>}6hVre4>0@4JyhXNxNmU0WHUvgO$%^SD99P5;c#a|OeeCp^=+TZ1T|k5IGbQyoJ2E?6`mWU}DAK#J?E4S9#z`c{6$I$^)7@Lht`'
        b')S<)g=IMRjc6vTcr3|El^dY9PrRnny#}^&dWxMS54%Z|xgzh8M^iYT6Q<#>!dv1$z#Alj-&9;sm#RZ3(syZAW!|o&cg}KO1*H%jC'
        b'o{x%z?ZLiH|LSn;hULc?Txh{4#hAlX4%zM>wSD9xub)L@=Ej%Jn2!J}%tuA}$`ZeE%r!@#`#x{=$9%PN1Z0LzUNd)e&z`xSwO})O'
        b'eeRp$g!J}G@1x>z3C4`uZ~5e0liv~@6_?o;<);~qx1aK{rXBIgZ&9@{=pYUARZ7_&W}I?hF2`0RjPs-6XMIh-(z$jc4jFp2^Stnq'
        b'pVT--oOFlswrz=rd!5C8<~KS#XFlAoIZMscJMQnjUD6@!q`0@=3;vXUbsL$V=y<UH`<ZH3)AA0-@{Xz%9rjrr>W9SU%nqSRYv?Q>'
        b'qr<VJqbj2#iC))m|E|eZ%z|IU5AIi9)Df!^LSDei?N4^(+%8|mD5rJ^+p<H1hf3H52PDdg9YR}mb5AeRG`GW%(ovPtVV}@ZE*Be5'
        b'+;WE~H{9a<y_6(ja)&TN(FVUtX!fhpiTm1(Bq1Z>5S6eyuH4Sg9odnvkG4gPB;vqdIM&m;Ci%rC3VRc09CJ?gn>8sx*#R^3Gs6Co'
        b'&%&r^X!q}M{TJi$Fx4+AszX1C+H1qef@f|N3b#L{@j^f0B`|ZNHRrl;J4U^WPaAMsSfewei^pz1Kqs~(k`0~ws(LA%t|T+XpB2n3'
        b's}C)I8vR8_aXr2H%xC)%iMv;I?(r+!Yck(%N2AL+q_9<(%BM5#CkUJ+emk}b4Yau4dJ3(@s{^c1-^NEth0KfGnHNDgKO@{>?rf(Q'
        b'=03+fsFrK(k-~i;Gg#$dd+F8(Wug-9C5d6}-?yt*(hm5(mD__M{oa!1AMKPC!aVLhhI88lL)tBPjPB_(S&et*j}cSU|7l$D-<;L3'
        b')!#(BUS$5$RKr%CYp*yPI>-DY9qjkb`u_-|d^wZ)t0?tFvAL>UIKr?-YOZK^M)<v<f;;Drej8QXh_`%Nrf!QM3yT9Yg4m>oNz)hY'
        b'jxXA)j<nm~Zdd;ya_0F}z1RMRmA-$mi3Tj?q<JA}c{{w#rL=ZmmsV)$@>bpsNtuQzOJ^$l|IBN@66^d@QLs%Irw#=_K2}bvz9L|E'
        b'NMzZ={=4Opp1r08vna1uFQsEuzJI0fVMhHZQ^P<w7>B-<3-Vp9s=Hc$p0Dt)2&Tb{D}sd3Yhn+5unP{P!gn!Gp%(}>F_mKlmfui#'
        b'Z=J57-BHk9^;Wz6xprfhDB-W|!pE^#=0PWMskM?7x``TT^*5oeFvi_W9~HTBG5t}`ao;&KH@V&Oy?P2m!+ovYv8KK1^>+KTc2}F|'
        b'L1<?mgqCv+;gyFndhM2bL6-lMuavlw7`JSi@OZmt{Wyw_8Cn&Qzrty>(b~rEo0haYmb6zbZMRQscl{_zITl(eF^*=+!u-u2w<r_a'
        b'^Mcv>ah_!$L6RsC-h5FZZ9_IagW)BZQBH2JI40QbuA%LzES)&V`|VZPBWO__mFz8Z`O^U11;~xEscJciVsUP=BD=B3EN|bq(KIes'
        b'eogY=CffH}7aiN^?#VQD5syvtG>b65s0r=kCvpBlgF~kr&3LhNhGUFo+)Hfq&KI}8q@Q@2h%z+jqY|aG9rBd>>jcLx3_ezKO#K?~'
        b'mhH_W+@eQ5YaVEGtNicv)i2PV_n~&jL+w=$wcA~7uH&M{olT?L9l`BYq3!jz_ykv*yI|F!jPhsdy-ej97L+SmDI;5iAceQa7L?Zf'
        b'Thn)6K`v6AWweF`oPW|V$aNE?V~1$Xf40?(5FT5xN@}gOT&QWn7I_M(ouD}M`H21FYqwX+Z6&q)OH4&e2<n(#vjgs-H&)R*e(vw1'
        b'c)%&0Z9A;osQa?^e;>Q_tpXdVG{jue_HXaOf86GIjAa<ps4b_r;|Y%@az-U{?=JArb-IJYnp)c&t!?)A+p0hMy}Vj9*GBz8WbuVJ'
        b'^-Xv)r~;>NVK+pP&FWU&WY#On^O@0^=r?PoTSyZ}$fuX7{5@UB<~A+_OffrGug`8=YRjliot;~{^noWj#?BZ5p~uE7J22esi4!ji'
        b'rhLDM&#bek0+$stF?H5e+VsF}nIyD0GP*Wqm2-;Uib-jfHWa@#eZ?eQ@%T+zOtF6_=5=kFI$`*ZI4l<AAZMAMVy_9j0};UXk;!$5'
        b'6l8m**GnN&8U0Y&|05HD5!=}MPX2$%9L$^f|CxR+aM>g_>3beIuRqPZ@0U`YN^Oi)4sX@m+edLJK$SMT&HYx8tB*8lT^CWN0t*?^'
        b'<tgbSE4_?TPdl$<IrdV(@Q593`2}8kERed2)r5J@{x%xuyw%C8#`{0u1Lf2<_x1Sxr40`nU{V`5&eM?S-F3np`DXvNdoqnZf+omy'
        b'm1O-Y%7Uo%NsCkG8O;}o78r=DnO1w9l=e91Npv;6SFkSB^%F6VYm1hKOp1|m0h}}|H}_4cGt+OOf1vrpmegYEy=WYX7$qrE`L8ZX'
        b'w-0MODpr3-HV>ysj2_~aV1`6(ZCNo@kX<-Y#8!x)YKF0k+SCIiBY-Zqszd4J_r{0#D6Y*dJ}fNK$)}23J^a;Yo1)qr+BW;O*6Q*d'
        b't~}Apw_52i8$k@msr+eJMvNoqOTHfYImz?=P0otczwz`ELsgq2tj*rlTK&;zSFR|^)haC07~4EOq@r4(j-Yo2{oyfiB@EuXga2nf'
        b'WBjnDz&6K-wyF_r_NG?XT2a&wt)Atk^Pce~;c}~RlbNt%+*kN&_iy8Eq9AS+l&NfV`+@5UodhSGY;{X=>+U9e+nS{Ie1&zY{hn0`'
        b'L20xaEiL}9$fk5*_tD&j)(Xn+R>|%f%I|w5&S(Ah&bNQj>YVR))a%*3u0sS>;O-*05ryc4yiCU2R8w}NHEnO}iju<hx%<w0qA~i-'
        b'eY9l-P3R&?X5FF_3#SA=u&HfbF`uLFkS&*Z4A=WTD-7^-zOhKUU_@VmzxwXoxu3QQGGp4o)~o&x8cLFoUHP>hcVR+EbWIqnujPsI'
        b'pRMM%T7_w@a2#U#;h{~AR>zmERkf`fD%_j51p!whRfN}4jU?ir@CiW;K|5OT<C`cH=S-<_HvgYdW{Pd@z2IWOr#pmkk_|sn!SDLL'
        b'Gb$Oa!lElDF&+Vj(R;xv>f9n@)UVA{YTQDD8j@MRESB|BlSQkxt!F%iFyHUlXWRvLBJ|zV`L&BzIqAz=rn%42F(X~&m25TTZJQ}n'
        b'*RFeAH41H#ATCEAi>XsCY!#ZVPN={b*16L!Qs}T!KU3JsP37+qZUnfmo(P}B$b)zv1VM$G{|wqHN>>GH8n}RnDa;d+7ew{H-^=U6'
        b'tseQIk}Rku;6A#1TT8jmGot1CMSa{X1cLS!5iqRjZ>^5h)~eK2`^Z+~T#+SgL}N|U3$2dlTB}}YrAs`P2EHhaQ-uXumW+rPwQoW3'
        b'E!8plfX2I|EG#gz*k-NGe`U|HsE34XiadNOa>n|hiP?6Vl(JSQeNot?ev5Ga8(Q6KMhT23o$8%LeodO98qxSelfKoF&{~zyYVT`t'
        b'%@AR1D6TV2dL?5-mTuIGp8Qw%ng7|m*DA1N#Jj#tx>m>J)+$|V(lvh3s+hWM#`{A^zTXaO)SoRVu|?^z*1UHg-jssjU?VYKZ@E8&'
        b'2z-`F?vEkKpVAbUTj=(v%KPWjqke4hjIYJS^Vr!70^1Y|$0SPAA51@rh3QAp_z@u`MJq-;Ft-Yu6Esp|h3A{L9P*-1tHY<Y%D2^i'
        b'xWyGCN;}d*S5VbOo~oXk*i37Cz2Hv}<mL^s54gZ>&ILg#5f&)tl}>gyJ^ew2vH7lNeY%&1XeYwwy8`mxeY-;~Es`G-{ijv5)bq0L'
        b'ya!^C@bIC86KlVx5gMk>qsz7L35E3EJ^LE!|M2i5m5aY`aeUuWb*{y}w#E3csNg`;*%rrlEmch|^c!^4T2JAk)KktfMK<BaO36Gr'
        b'!b}r>Rr5@yY+<%uls<245L=HHT3t}yRM+D8vZbo7CFy7Wfrw;j+2Ll61?#<q3jaGXuWqSuSNLv0X4oTjH(~n<${eV2(_WKt3B*Bv'
        b'Pvt(}LWLSmVtOt&*_6G&O6Z2RO}X+b|0dJ7pI=mWf0b-uO?W{#=Rc0_IN692aTh*f*-Jan>bg*SN(;T4*R$vo{8LSxtKshb{>fkq'
        b'(j6Sy^h%4Pu*F{3^86RBAko~I7Wdpj{W2;48()0NGCr_`&G&!GM^`gfyCP6`c(&$^m{Z%*J^cQLo8KR!S<);8zZX5cDIC+L=ZIO?'
        b'GUK?A{pkX~8^G_o{PY69yIW}aGmuWp|9PL^6M|cW8PRg$TF9>&AGpZ>37^#?GBQu4tO#7T{jaOWkC2bVkf(WN@v&{INN7>As#dkc'
        b'+quDSg;hC%CSc8y@z%WU<2Jog>1}+5m`Aom9}^Ow6UskEiY_pAuV?;VW-6aemVGMqFziW0tbUCMcRFxvf`7{sY@I_^?FcM$1jVFj'
        b'(<H7!Vol?Q4a{vws7h+FC$)_8%V(S&3fFgc_lRdFX84cWH%mQ~WCV}ZFChsX&BA_)d~rf=v-?EwFU>+PTs{YJaQ<Fb_za)ErYS9s'
        b'DJ@k~TI@eIs~M4SwsvxhaM|!;5~Xc1gpsSe(xO`E8<0<uxsff9nV%%)M_ZaATb4^5ku7NxTYeLV`f__0dl|3X*(0iCUCZ6_7fM*0'
        b'&Zzz_)=dtIPESs(<@|LAeU-|V*<a8-K?nw=zVM)!^Iv$NclH;`;FcueuA8RN7Ds4{J+!6T{<3<271qki`+4Q?77cp@9`6^*xHJ_C'
        b'B^QMv6p3Gp-48|5&gL^+Hm3Z`yYR7xZER^8*5Vk}VwWPkG3x7{Pfmzu!bTS(dXuFut8-GztnkJF^#JesgD<NSuSzE|>5Eq_x40rn'
        b'!7d9MuC<9HtqO}F{NBBU76onIH=7-|n(fz`tL<Bjzp*c0Zsynu?}%V!3^UU&UwLUsuzDWf&ZgEY#*SxBvt<$V`e^kpcZ8d6+S$_*'
        b'XkET{=|x4fuWf18xNkUU+?sH{d69UWc(G`7k4hynsE9^88%<jM2(em(O{_>$MCNza^o{HC4i2pl<@=8_9F@2<WW(=#myLiaPK%EY'
        b'qjF{+zu=8qO-;>?re=FXbM?;Ct}fQSHl6TgvqsE$3o_j55h9It4XgaLnO1#y3_<Zl)i=NBV+kX9vGnO7S05Ev)0Ys}Y{Gdd_cfpP'
        b's$h>Y#*n-6H*RZ~3gxzIej4SPlm)B(U7z2zir)0e`<yMm##@=!MH!1&ujj}|ne2u{k`c`&JxxBE!PZYB+cIw>A4N8%P$=7Km6z4;'
        b'w0FDo^BQnbD=&ZJ<{Aqkb$XLk$nIr!!v%g#dIMef^m?Q5s26zjGQVK_jiw#Vj`xwZXEy|5^yPfG(6@Y&3%0EOj5+O7+aQxaFM&%v'
        b'WHc&c&MtF}a+ltOn)G(>(_Wt+s$|ta@cU+Q!`g?P_C7icabMuuo^4v!?AXv;T{hPKMsxXhY|f=rs|<<Ev<Q2qlfL9h;}7P4G+RB7'
        b'-vt#m<j&1#PCZmxrY6RjcWK$j+>@_2-4;#_Yy4`WoGj5W+s^*#b&#K3ruHNC2l%npiI=SGh9f*zvOS1Rs^F14Zd8q*yHpORxBc3b'
        b'(d<}?9KPb!MmtWFM$Q$}YS}77czvnx74j!V*4K)xFHFd217E+Lr%py*Zbnu9z<O<c@U7~pX2-l{ds1`tu1Ab@Y*b9MX8;N&l_Je5'
        b'u$QN8Y_jD0=iJQK<{LO^iGmQrxu?WL!ARn+|IYJ0K<yYpej6i+JEJ0oUO%GGI;YbUJxM+Ouaofu=_li(;kJ19$#^H!&R=x;30HLb'
        b'BifVk2La8blko-nPR37ItkYKjbe^sNEd&CCqV?HPC*ui`k#!Ff1J8Hz_`9<N;aL$D{|C?OBTvRp&eiFoL9hIVFs>qu9wznsr_yCS'
        b';rSzQ*9~w#==8N6I{jAo&6%gu)At*AKAvu*;2Y=b^l?Z>FWf!<5yC+p4l0oY86oEu>GX+6%kfm5e%&)Vy=ERwqe)LpG%3VH|M6?7'
        b'nqPYb{!<YS3D2HMKV<hnU!bMw@8Jtzu0UAXDx&`YY1j>X415P%1)|5HT<3@l8l+`E#=@&Wwt*O=Q;DHxA~AGh##j8TPVXF#kqhZq'
        b'19hf`80Nsvv=jM%Ol&Z{j&#D^IY5kX&LOS)frHTR8;kJN#841M3`iRzMSNK>YeX0tlwCODn*pTxNa6xnN!)p)-8+Yn0p#-x)I>^1'
        b'1L#uZqn7GX3PFgIgcHMLgs}$Z;rn#@&`)&w8U957*QF?TktA+3sCdcA_{`^Y`c#DbBEU^P8Q%o6Y~Xe1&w{Q4+JLv9KL=_8a)6#w'
        b'I(<O^(HFMr^jDYa^n)~RnA_oQAHrW7*E2kRut!u5{TY}y0#@K8PzkgB)EqcQ^F-qhmBbB)KPS{z00!y+AQ(6gKVhJeKrAp7NCy52'
        b'tbyI<aKAJ}5*LU3MI%3vprI>t`XJEbsE<J8OG@(vyLCEZSQJAHdLXM_r#GP-tf;3xgf$QDayvq%(${oN;Mc6jz;}QZZnkDpej%x-'
        b'qEzB!Q}3z4Yh)el$+PJ!Ie1)5CPpz}EBp<|{~mr2;TDP|aXf#QFGU!;UeM`zo*5uyDUF7#fn6$)jCgjzzHtV43e*YkU-A4r=ryy5'
        b'p$&S)Z1Bn~$|t6;YT-w-9PJYb2YO&HokI*0fR#Y@%9HUmdr(&h_dMMC)Jo#AQD1#f$H9Fx@E9-%H`z}U!$BZ9O{cGU3cL+^7451K'
        b'd{j6H-b7g*g!(w3*vA;0UoeI%!1=#12E|{9VJZ9!Oc5K7z<%ixonG+|w5Px8^ylAU49T!d-HSAWW&?x3kw1wc5q;2c^e+|Z=u?)1'
        b'2NjH=4Qc2`+-p|SvVJ4+bx@vm7Wk=CNa7L$kah|30gz}y=72Ibo;M+n*@$Bu+*^TlaCc@AF*t$Z#l)Zh0<$D>b6{?Q{Yp@XJNjhg'
        b'orq=n)PJCy;Qx8hZrC*d-vNQp^EY@;_x1<o?C5{szY$pU51K|(JmDm9p-?Z42k#<`eZV~E!!w9sE7c>PR?v)$jQCE3c@A}ukx@K#'
        b'(xh)7eG%eBSWFM)qT01+$p)|lVUVWNjg5_gfygJJJt7)8p}P#=fl$dn=#HsEETeAtwbS`O?((J=PsWS>M0sp0CY<1xJdJJ{X@~G4'
        b'gL8%<{O^N2VOYZ76+Uss574rfF(eD|#L;vE?_3%{cIj;@rY9Q_=Ey@$H9kM>eEcQ<+*m2X6$9V#gFJuqGEbl$ME+WbpVZ4<q-Amt'
        b'?Pu~aU}|^}cwaEn>jO~^g(&kNnl8BC4?bBcl%aPb^8VGX3aVBlgzlwOLb8s5kG~>@<G?Pe{u=$D9CZ&rCSc7-Nn9<c6)2!>6j%p!'
        b'Cd`lOydDES4VsuZ@3wM?{$G2?Ke-G2`#OvrgW*IU1WZs9TE<Vj<S%;sv0HDWtZe#c5%-Ep8o!7%qEF~YczwVXU^4PjQc^O?=ch30'
        b'HsLtT+5o?H<Og<|mrlmZfB~4z04+p%5<vrd(AR)A{*HD9)Lw=DH;f&iTR}0*@g=Wq`==FdQV~uv+JOz~b-*Tr@`*qAwei4LkJYVu'
        b'dfhFIA*)c<KojiEaK8cgJrCn;jMxy3w!}ftqODj#4*-YuA$_AHakqRiwxN%;5wExpe7xdLJ|u~21O~vrdtn}SSQ5A6wUhBB01Nj+'
        b'U{(yZJjC5Eb1;)aEz^k&GN@^Lyz+@8?wY4>840te00R37p^RZ5gfUnHiT+)fy^VOn(RSX4`W1xrn#kRTcS8Rv!mLDG2dLjjLXLr+'
        b'1(w21POv2IN2o`^O*`lW#Q8I5AI%TIz+Mha05rfGz;)oCz$RcjP#)|aTh4=C2Cf4Az+J#HRTAfguzi8&9Fn*Zph3U}*u4V;L#+Zd'
        b'z$3s!KnElOeXmL4W`ednjd25cOMyBK$OL*vFoqXFR|9VV1wb}n1wI_&73YOAm-%|dl|nyx7-I+ml82&C<ru@D4`a9r6r$|60tLXo'
        b';I0a&0qTHLKtmwP7_!~dz!mgkXJK|8;K0M3pf2Dy;2JOhtelPfq8x5R%>yE+eE~lp2nYoffEpMNJPJ$(Vt^-sKOhSwfF@B4g&8mf'
        b'm<>Jc18M*FEBGN9dLFzsAM{z^Z@^MuIq(vY4Xgoj028nt_zS{W0BnT%ZJ-F)4wM3R;3HrUun%|@eDMirH86X$B<@qtBfv4>B=9Zp'
        b'1NE<YjB$cq0<Hpg01@1CKp+qVgaQg69MAw0fyqD&kN`{rW&uwF^MK{RD?ldru-nTk&J6Wpq~{&bVqgdG0q_Y>3p4=dfllBGaD&E)'
        b'_VFazLnLS-g^V%eLSF=Y0F)s-E3g;pYG4=Y|0_@%Xandsz_-AM(EkWJ4`J*A|D=MN{29Ya(5+MrG@u=3KExQd!dwb|nH<0vF2hfv'
        b'FJt%()Em4b2LcsTJ{e;QgL*trim=}UqM)7v!~zMxi)bS=K%W9qfO)`TzzVl7fTjW&zzX0c;58rzuuwO^+hb@vH~1}}#lZW(PM`uH'
        b'NW(r#Md*lGVylAs5O5Tz1L^^W3QR;rzJdBX>XrnO??Hb8+JP?MXP^&Qhcuah9AFLbDv%Ady?QeKwvY~Ca&T7|93f~Wu09!m?ls!?'
        b'XBp&>722S0Kp7G`SV9Degx&;s#R)g(p?)6VkMaB?NcR-r3E%}FNkRK?N!%h}l7gl&ZCV=WR*VP5zzV1Xm6EuzzJzRqI%s6H{w8$`'
        b'{kx!@KmyeDpmRZ!{{eo2T95eR00qX-Bak7K91&z9hk}mB5D3r*<t&oKWvzDi*;^MghI2C*Lof0Wz7YKi=sDOary!5pZ;SfRh)Be3'
        b'5eZ+!7`kEZ+#)8WFG9A1TDk^u;XfF|nDxKTy#hT4y$rYlWCF!N&P$BJychh8vI+uHe}R;OdD-d4IZrmguQOU~fV}W{P&Q)-eEnqn'
        b'Rrr|$ng|?>Mqb`x3^SnKin+rTxIGUUb4DIxm}3Sn=c7M_-5~t*Y`{1YK*$xC*#O8a1{2&Ix4{2Kq#f>70--S{<If-+0|<*?EL1>0'
        b'0CNq(?SYy24dmO05bN8FArIkAei`i(>KdeF4rGr^xXpzBH-RExFOc&tV^{<?byRlDh0OBLlkt&egbQi|b^&B9#(2=HKn1W5SW3-_'
        b'E&j=4kHkQBicUpbZvtC^0|1JjeD|_@jO9T`uR>o2WB_?UIZy{&27F&ZUjZxxa)1LsE0Bo%MFMnO{t5cYQ0JiE@B$;GBCY#?=YeWq'
        b'E6{t8G0X#93M>K&flMF=C;(Q{`~g)!GH?LM`V{q$rPDtJ_3<jkPzoGJI60s*5Z^pt-*)uDurK|U=Z~RWQ`do)Xnflwai<##P!0`K'
        b'YhC}Gks2e&%duoD+7|531NY=?LcAc&N=e{1;8~bwZ$@5$=Mh#n^ap{suNlJ{=!+3fCTQy8NFQio9C!rvm;Ej3>O0185YRWFUIE2f'
        b'#$W<g!d*77uNbmX3HlYJ`7@xH%ADUbhNZBx{sfA!gJD163CyKowja<yt%2Ebs6#>NIz{Le!~=Z}Pyj52n*!K1Lft_9LBAFH1Hdjo'
        b'dQzv4ZiH<1wN6h4`L$$lcoqOw?s>W%_RDsnUxoH}sC$8#P!HXKu?I8)^e><bL7xWA15F040i6dbeh=jYssMch^a;=$(9NJ$(0_rx'
        b'4cZ9074$Ob4$ziT^jnBm4mt+#f%-3ggq(+L{M=4jCo=tc$jcn*!MvnrEiD(Mc@1VFigl%Knal~Zxlr>WxVeV5Iru0kC>7=%Ya;J5'
        b'hEViN#ptWZAUzQ;Q&@i$+OGoPq`m`p&N4~dHqg<C?+EC4&;ihp_c2c@qv0Sy;O8fyx5kPM{^;|TLfwIOoCfs<sF%Xs!l8r|6Bh9g'
        b'*Go~Z9Lo3r?2f~(8MGFDhkYQ4`xE-nps~orRis4)^<RKDfqIx#fL;f6en9g?Ov(=>aZ{0|z#*syU>A~;1helzUj}UktpY`ysegyM'
        b'|3jK)g-l9%hQA9w2|}KypiflWBysVee*v8Z`X=an(0!nP18oJ(0QIp$b_I>L3*|3c33>o&escsNFG9Tw>H?^@fqo3S6K3n7zKXJV'
        b'4YU?!3qa3;CW2lBeH63~<)Z|>4t)TqOisud`1OMNQK+fxmPPB}2{-@utVg>8XkAjfHrft>t1zp98=AM{pbhXdZvt!B51PI4Wc&m('
        b'NnHav06St5rG}o;>5t^<^#9m^`OMqsbAXjlzX~^5fP!$TL4X4O_&+Z5LGXhSK9vy6KY4F5=TX)$`4QGo`>jqtVHd`jCr`%z6PN+@'
        b')?m!#5KrMd7>9@7<>P*!V|qL$r3|rt3t0kgR+NLsK<@xLsLzCfpF@b=2EXB;;a_2FKz(mT7+I*_$RYFs1fFk$eizWT1^ob}+tJq+'
        b'qmOIQ>9;|@9oPX(n9CYUlUd5sWF732p+Do%i%ZZql?ZD_WKFryCP?-U$Ra=vuoid+h(_P=Jlrh;IOI(X?1#GXgnP~P|N1)szq0p`'
        b'e}sJy>d$~)z>4{6ILupNUh_24(~j_u>h$}8`5&Rr1M-0ad9>boM5iA-r_=X-LF1CrH7zM4tT%9^5b4k$92sPgGoVtF5be6ljjO~m'
        b'T24cxsq#1zU67CwUuo(fKj|uXpLP#30R4IDcOGkK19bw&UtkS;5U+SQ<_VxT0o%(ueK+RW4cm13t8jDfU7bD->d9Fob?bJW-ua<U'
        b'ADGIfW`if_0!$VWgMNs<M4Y<T#PedRA5M6ZDkgDO>L!oZ2yQ+h{MrFN2x=M3Cj-$?#|d`c@SjQe_yL~iMPOLE9>;&kDun!f$x{X*'
        b'<oKsZr>X+;9#8^01jsxGzC*dp_ai~YPtv-r6%lfmkAYnlupCG(L^|H#`Kw0Oz+dP2UgS$}7*2ZLqiaDr{XzH(ET!vOA~GD4e?l$k'
        b'n)h81$$|fUKnY+264gYXnXS`{X@6CKbRxza=;wTgIfwTeB7Kss3~{NU00)HA_Js2K8h)eppo~F}Aif~P7XrOEa0dG0K=OCAz3_v>'
        b'>00G*G#g%oa%3nEi1b4GdgwAGm63aRV&ca*g|+lf*{i54_%DWkf^tnlm?gk6AQAq0VK)J7kzN|ek0I38SK@f^H|*vCnom&Q)jIw0'
        b'0|5No2L1p_5pFi@eIZls0bblo)92u?Y(#vIM(f3q(csaOU-3L-1x3$?2%B&S_YJr^3Ut3p>oLA|C5;DdJ9;&Ei_&*k!v@&D2dshJ'
        b'1o)XJ^f4qE#hP4-bR2~FK45Dp?eoxA0lR=w;9#pxe;!!zFN{gxl`POaAQdP^+d2X_=YZM@onEm=ryqd%R$vhL4Y&dh(S#9l9qJqj'
        b'(bvFDA<!$0)}J2|tv~1;txxoc)}H}yM1G7gBGLQ3bNlU{0GIW<4{s9<>U09&)N`qAz*XQ1FaY!d`cgvL5Wg$}GZ#s;J`iD6{8Oh7'
        b'-G_NC@I3U5kBbdg;HDdhqjeENNCC<#u1BX&Mcln;gI9ObxX~vAzrbBI+)aT0)4-d+8UEY&JkZ1x@Q%tW?l4t@{tUM^l#3PZ6=Ixz'
        b'K;RwE2OJxkQld_uh_JfhK5GYS$U)k6{fTmXU8gTV+UT0n)f~hR`--(XeGL$aaQ=kerxNlB5Dvrv^MEwqC18+F+Q77LRJzxE=-NX!'
        b'%A)}K^FSL=41Fo!g!<8skzS~00RIK`DIh$7OO?T&0`xDRxYxJ#?U%$YfqFS$1AYNs2a17m;2>}eD8;x&^K|ZjB#x`X{Omo}pawk%'
        b'eGl@v75c3vonHSw_zn3dpzDB#9_kRj4rE?LJ}sE@00)6&glB?%^+AO9A!}%WSr5w63bS*Stf3I}AdC7%9T$qhFThrq6$2dnvXB9K'
        b'VRqy-+LyDbq>xGF#|-kM5MydG>Y<R3;k9&~nHN2O0{w!Wj-xt#?QDdBF~fxMpnF8LKHwze1z;+$G%#Af2IljiJ^-YCBaE>JRzPh6'
        b'J_OFe&2faW@)YV9SO=bX9vI~R1P^={UmPbkoPoQiVK*F51A%2H<6min`~(C7wMdH{bkcFz7j1q-e-6BM4q;}(-9S0$PRRSfBB0=H'
        b'oxTxR1NBvuQ5H2vdww1$fI9j#(njriF(?1-dR!v(h0te%GLX@VLy6uOR0Obq43GdrfwZ6vOb*=r2$TbNf9Ls8Fz1e=E)hmCkTnPW'
        b'0%#~?j75MR$V5Mo12=J?HrVX~e#LxfZ!!jwaym}%x1UG6nLswsUyb?ykCM1_^ppPp0-;_D`WsOCKKjQGbow8mE-uySzXaVy)jM?h'
        b'&7ch2k^;z%h$9B--+z+Ctpsg6t<#@r5XQ2E=SLwfprJ^o|NXoqZd^0uULXe8H3n$_z!jvo7(9%!E<~Ho0tzRhzJYbY(fZmFoqp>b'
        b'v?G|;0K4Y6Wy2?1Fn<L$1C7Yr8K4392>KdeFOc~Z=AL%&ZyVZVE8GFKz(Jq_I1iXU1}}cX^DF0~et|5Y2j-FRlLhR12K@>!N)kms'
        b'ejFnvT`j-Xn{d#XFk&{yiM|K%_R{k05v6KS_VYS04+a8(Mejg<0OkZm>%-rn-<9=>H7?d*?T0)G^a7e2tU-2>HR$1H=_S^{5Tpri'
        b'v!N~oAY!b&3oL?tBIYsY5N_y4C*w~XDBGNGwOUCJAuIifepd%=D=1e`#b1!VxeVD7KC@_YC+79QgkO>WU(kO670@>T6;7A|OS@2B'
        b'z)Bzs$OhH}=bf~z{eihxE%+xAZQ2>XEF&X>K6f<__K98YHTwd{2sMyv+kgTU(g;k3dL`y@HqdO?n+hRQAzzKaHuwud9<ov1B~TBd'
        b'{CuH*AL{+US%5&_^C!=L33U_Di@bG%iZ7x*fx(Oace(?+(cWCBUza<5HqZ)S53tW;M$4rV>fsS|Wo<YKKTPH09=f04E=Irjw5cyG'
        b'*`0Sb{y;<OCe6nB_}j04m>iJ!ef*hAk~j%aaf!MQN122IwS$BN>X#y~$;i7EGzWR}p7u!H%3D6<@4!*7zsEd%;ts!7@%NbKochHH'
        b'KdvHa*GDZI^YHhspG*(`cm(cgn&b#~CF+{SLHA3<ynQj6ie_}8o&__y@8N+2E~6hNQ9sF3kq1)^_=$dBFTRX+02E(Ac>;9L!g^2n'
        b'G(evS9+>=#`+Lao0oGv46&dI^BopRn6Rx5k=;e93#wUEAggy&M{tadQo4b5zI3}nEf5*7_yIV%2{U`md!~Nl&m(%axl+q8(!pBo$'
        b'ia&L2=F38IF~I^|dw%##x*qct{g&7QbuG$(?t!4+$zZ;gdUbz4yBSZvp#il}e|1(lX>Cq3s|TR}8FoK^MT9j1S*`c;fs@95WRJV|'
        b'oz2uEqyeqfv<S2V@s5T1pM);r3g0}5p6+LFW`+AWxe)G@>y2>kVUYFVRZrarEhuxyIFWho4f>XvL-qpQWOY<hDK@Twt4eXmBx7#)'
        b'Y*ogR%dRgpX2T86f8$0@WYXqF(*5O8@i$`k+AO&R4fG<AW17ZUlpfY_{@id!%#Es;8}`^6;~4I*J)H`3%#DA0A5C{-vyQ&pVbRDm'
        b'{zXF?G%C|ZaiKL*p;6@gTxg~5TM3U<3HRvVuu2Omilq@H(&8XpiD>4c(LL784foy+Q)+J5$KJ50qG%3O!-YFrmO5GDI<K(U2&c7a'
        b'wz&7<l_|_)Xc`KFojybva)TRM!E#TY9?Csu4yNXuH2>b4^A>TaHh~mGTUU7xM4Yt|nL}}OC>N~W8dCa(g&{R!OQP6n_~v+iqBR}i'
        b'S`q`*l_4sz*zgH6OT`6oV#SOt6FqkgRNEMYFuShOS6vuVy0M1kIOE<B6)U!U!faG=qd2J|e+#{{FlWGGpszy<=Rb^t!oz&R8@Tdn'
        b'pM<OZQP=xL;>Rpu3X=TG!l2P9OB6-6rIxUV79OVC*;8!876wV}zxJmrdC2ugILwP68V2b}zTMYKq%8sB$5O-%GBQ3nMVxahdB>Ky'
        b'9sT6YFAirvYMad$m3(j9JVHKRVs7iN3sdA@Gq?6vhm9!<8=YUKR;mr*+Lbr;GsU&*{0t&ZVWP~Gs4z^`RQr2zQzO3s1MPoo3%y;$'
        b'C>y~A&|4cairJ(No-40!;YqYXD^e_5;u~G&_`09o4(k+=sQUhxYf&fqW6Hel?OQLig_`U7Q4ggXLkkqu3iCdy;f9o~c+1CL*<b9_'
        b'I5Qt5^1e^S@&z0DeEJ}X;4eCT@R_Jj`#EdXr~Q?pI{T>irLX1ZpADOCY2XiyW;Z-UPJQ1sl$>S7KYj3$Gum%s?is6}X`{)K?qy-c'
        b'S{ttmGIB#_*9jH;TF4VVavzCxRt=kPu&(%~&SD5Oz7t|)3w-j!xSzKd$2Pojp|t;edNnJqJ(0-ysLMFBwclnF?~i3RZ|g79SPJ*b'
        b'BKIoFGA&7%muQcjr`vu>&ULLpj5^nT!o*Sr5h<d#L@KiHy;ZHXQTB{c#zeVxPT0e2s;XpS{5XH(a*Zu)OH@|B-P~^pvnUkVSw)P^'
        b'Dx*8%mRLNzIya}E8<{>rMr|_`FR$uPpD#P@&3SR7EZ(GMWWLe5jPuD?`))Gr$!%KIZy6!e@AW%lmDv!;e3^B7`ZV$3$MWZAyf<9f'
        b'zl*}zSYXkJ4`mKNDz222Fm-7RDy+e;m<h>P^|dBr!)`8O)qEKj^m1x{+@MJnS>(+j3{JZJ2s1}&%CF5gZa*S6&+l(!(W0hVy^o6X'
        b')z*=flKjW4%R(~p=eq+8jb8P2XoFwgwy%^^`Z;fvimWn<SNlh;Qi%}SDx=pb6{+xlUA@X*y5}*(w<cx5bYk=oz3KD%e3~!>p-B(P'
        b'Sa9~<nH}>J{r_=SzCE_z9NYhIcXm$c&$(^Z_1`-e6&2ji`KrRgxLfqeIbVmOziCW=rLXI_+L{~nXuon|f26gH^D(Wb2jKUl&^^S4'
        b'qdw)0YT+!0b{C2CJQ(7shq7>jK0|$nMT2kmInAKG&kZS<rDBLGQT%`O4e}HWPh@UjzuuH>D)vhj9_%RkgcJ(Tb5x29$LVvy8HsK8'
        b'&iP&Iv#^S?u(0Z|@R6B*bt+MLS2)x#G1i1*{-N=2U~B8duCK!DZ{NFbg3v5S4fa{Wh-q)F#dd3VO@R4!AH5q{#08sg_Ib)Es;>`B'
        b's0}0ZS?}Az{c%xE@MQsaZeKG>W>=_VB13j?L51Mm$n3E`UPswV#`Vwy_cbkK3d6WYg&y^>U+Uum)Jcla0?v1~-TW&JpY!DsX_3sF'
        b'8^gpz#U!}u)hO~~eND&uDt*f<)fg|D`;HFp+9hotUOC+OC2V1SQO$|z0a+A->tS_9;<dTQ`Z#a%nZC`R_B|ze(VIKKjn2BPxMmM8'
        b'3s0)Ho%Ee_DEO(e@af!<uY;#mpSpQ^*#6VGbxUWBeM5I^SDg<jJglgcTG9fF(gM$>$=r8-nvc`;W$jg@exbOg^zTyo3HN&jT9g5A'
        b'`n>3CINrTLbc>r@=1{zDUcPyzJ*Fzg5z}NG70!LOd3~Sb<G!Yk`^xO$p|`o9)YlXS^>p8iuH(I*Ju=jAyyrKO{z|S>pDmxv*ru5b'
        b'Vlw^VbO=&phMk^e8kcgS+jsSX-Gkgv`v-kTht};P<>SMnUhlKN-e(9K&5bZD2~%$gw-@)7SBGm^lCZr`d+g^(V{X*DeVng0Y)mDa'
        b'o=7W8xvZ~JqEe~ADk?D%9=p1-*b`5p?9A^n{a=LFQWn>D-Fs(3k$r#QG0*SY{7j!klVs2BGg&2h{`A29o^e7jdt%)8CsY_ti)O^?'
        b'wniI#6uPAkm(|J4YiO|<RN!pI!t{~KIem5E-qot`GF6!IaJXBcekXi%Px(2XJ^_$0wXZrH)f85KDBP_uz7-DdmT>8ub*4mF#=7rm'
        b's7q<6^?wR)%CjW&rgCCm-Z=UQisl-T>J^I3!o!#DE5KB;&41}DRLKO3s`>%XT_Z*QKH8nm$P(GupU0LVjO*smzTII_wABs}AHB)6'
        b'x#(mq7YwF0nZ$*$Tk^IHwfYy8k?ldTc`;+g4$OcjmorSrKg5%$$ND0zGQne2eGiXzuM6^v3hvVt|5(YIV}$fx<4KfPpEfMWJca6M'
        b'`=O&+6a%wRv-Y0Z&pdr|Qfm*K&<H7ozV{nWt+aE!;=;5E3NApKFh1&TZvZ<pS#&E(-6tcnlf!PkM&>L0#*?UDBK6%Oc1CoSf{dR#'
        b'rY~7|1BmE<nLD~qukR*_er}VPs)XRaXor51EXKht<wP-l7FE*NFvZwO%f<%CkmdZBxoL})^%BAbCjH8r%+z3h{Vm>P5nIx{4QXug'
        b'%X5AD3Qb~Jg`c%5WKyy)RB#e5xUhVSYzJc(_qm6lO2(4r>l&i2fN;%CsCG;!Pg7@1eS36|DVK)%DjoQym`U2r-bh=vHbIu+Mbsa$'
        b'WoeZA<kP$jHb!rVTxBCECwS+2zhtZFOthc8j4fhh`)1CN$0k-RRj=32kXM(H*u)uuHXB&>(AES@A@#Fl`t7-e`s|{y^scDL5>wp}'
        b'Qcza0_~cw$d7^razG1HIb4Bewh3jZou{<`v3^IkdydiACV>c=97#N1$!bpsDVS*3|xj3P=7p+sibeQ)NRn)h=Tu2$l?!95<s{>uj'
        b'c;lOaT0u)Dh3R&%#`gl#HuYAW=&jhW>MTQiTJ*MC=99g&k9G8-f|3JnfnAb=ZxO%odiyO`QCzamEn@p6>Wg0CSV$+Y^?p3XJ1(K7'
        b'H*$U?m+LzzLzGqK9jhHH=X@bZfKw6<^sch;DaTD^;-#yDXIF;@%b!C_3Cd~KHn=c0a2z)(@?>spWcJnX>l&`r#^hdoM*GRbvC*GR'
        b'dT4)Sp!_<~22QE=UqnT-u>D)M937$^`&Y+@y$ITH+&TT--J^So12an4`b1*i-n%!yw87HsEM4Qw^^3KhsqizW^;Yj2v)5V{<g<UT'
        b'tZb2wb?Jl^d7raMkCO?rc1N@I&k{?+g?=bz5K9@!8zr^u!Y`X~Gg=5@^W0u4MU+^^TDS=&fsrhueCXqQrf#s3X|LFJWXt}4`5}`1'
        b'ZaHMJPnnolY<%7hde^_JGVH9F*cbFxJ>GkIXtUk?94%dU(2w_W4<Yb9%+Jb=C5LIar+q><f+0B{OT)k&AJg4j(=WN!z@HOtMs<Be'
        b'icZST+w<P`s~B~7GkD{qS^fX$di%I0uB>r<GLwW5MokDr-n5wsfq>X1LFJ{o3qd0)Z6Vf(R`+XyAlmJ-mQv9!Z8KvV1EpICt%9}N'
        b'Bo+lK6|gV9)GlHht;JnycegLwR$fIA1jM!$h54O3!M6K*KF>chbI(2Z-gD1A_uO;t+!ssQSDy3C@v4TLsM}=tm&xdqrKR|n$#~m`'
        b'suK%fJUgW}e*BfM7HN}&{fCd^4j-3ra!)F5ii28TeqW25+PThy@|Lh$Y{25w#!HQIkoU&7(PfAB53AV-=^slkoszflw|!(E6FQ_A'
        b'!k+Ofw*CLaZWgw`&273DWY<d_hk*=~d~*Dk<jnt>yhVtvBjNGKe#K}1PyAM)smCw>O#<c-#AE7T<NDdRQi9QgMh~N2c`L<?9tQO2'
        b'PS&TmKm{_(5O#`JAABnvurBN6x7^-zu;^vCyf%r!_K1GgErTsvKNFrg{L`$zHg3$jFMY->qm4=@;YssPb$SpyHT*LsT?)^6{8O3U'
        b'Gj6oaPM6%uQ9y7`x)`2w)2{$9GF=GY&+$)1IswlR{wYhx;VI{z!RZ2cmZqNp{6D92@Z7~eA5Wix=O2wUn++a}jZL3~;G^kx;kib$'
        b'MqpNlr5_t#Crtkthz-*yRCNoKo}b3^Yi9TTgel8|$wY(gfAqJ;4Ym^fI6QYIuQb@UYszt8xMytKd~~!=8>0Vc+;;RMZw6+#j2j6_'
        b'*T{JGQW^OJDlkK0BxL6FkWEWvS>jCyAR~pw^iX5E(wIIwGw1Vn##f}TSPifosWFE%t|rr;8?X9yoD`=Ot2!<6Z7-sZwWmIljB0CC'
        b'HDtD)m$8xf*p6{~g^GO)uMhbt0(blYbB1?FR)l*4v2AN2%P*~wvn#OHPh{)`W7%f!Qo+d&+9NUM-1z#n_6pe<-*_8{+GAL2sPvCJ'
        b'?Jvp5myqbKk(z}VQ#HPhAy<*29WSM{OG0kCxu2qRx0!Qq#+=U_iek#go7c$K-*(ROJ|bN4C$evCjRHoN2gC$AOV;*3rjuOc8uq*@'
        b'vcUMUHpYRQ{=qS;$I16TKRVuZWW43bI4ONdGAY{eO8%v7a`%q5&Jy`E#je>>GNG+j<ytG<8AjIbn~j@RVuf=pN~~;d`%KK{uG#j-'
        b'oqygcu}R2|lA<8hmVLM{4Xc^=?TVrxa?8G1om=Jm3pxwr+a7N>3E2W+WJmkMnD>H!Js;Kb%DAU&T=TrZ^U`?BU&f76%p8P4qojd-'
        b'7L93M5!B5|v#uF8yD`wcMzOHuRa~5mHHrJep&mA$s$kiG{`qku=w*Uj{u(aM!pwvaK70?OqbP-(FAGgswSO~pvx)nuLgSnRZ7_$O'
        b'f!e@{+TbB<{aQ9u>d}q!o|ja70{ULT{sqptfH-&C8o*h<*14=@^SJjD{-&U1=1^(#8kKoHZk~xnzG(hrJ^L`WZnOApNEb7KiyOEz'
        b'bNr2miw|*RxVVj5I~(_%<#x{Ln9V*Ra2K>8PHZkxO3yqp?s7M`m8gm=QriqHa>xFHqKB}p6321Q7=u@>8c$1G+PqZm6^B$VRk_?#'
        b'`}R|w;PK|y<nCJg=gY>211}1}f{&=J%6~tirm7;fDKKBcxx^tQ;kfuX*Ag(^+$aBh@p$KTd)mh;ux-eQzGD%}Z9_(d#HAENp2pP@'
        b'UlY1d@$<y-GrI9%qWNuAT}y-|b;wMpfTzn})9LRYCnG;k7(b(hXz;_1MnE})W@M`FIM{j^m<x3KkH}G8u-or&7>KatiY||8T>K+9'
        b'J-?$G2elNmp4|HoPU349t&fQaunDonqP5CLNXbSC`6l@`IftCNqkLif=5{e=>$tROQ}LGHFR=fa&3=rvzvOkDyHx(-6EjLu1W(Ki'
        b'a_&D+UhwRUb18ynXTBV`ZEYmo@mgv3K7**1K)WY@b8j2DO*0txkQ9-?-2@U^xSPY$@9;??fkYeeRq^2W;co5jd;4o!Zr^-^NRaL*'
        b'zYnZj`wQviFR>B~dMSh=X}f*FbXYL2mc;3dG=49ve&{9{%o12fuBM3Yh(|Yspna3Si?hU|>vz!EuoK+$9ao5u?+_uQFUa>q5D1r)'
        b'l5dnw9e!0v27_zp!ZG&KOZMjC4^Gc${q)V|=Hi!U{`fe~e%jEA3tXRFs%$Gh2Oi01Z??4+zcKU2KjN;>8s^b^Gw<vTztiTFHy%S%'
        b'5Ua4rM&BR@Hf;iVTF^w~-{v~jPhTM2dIlXSnty{+UYKIR)Yhs{b!QvSsLHF$TU>!yYY-OcY_8Q+Ru)&%D!(_f+pa2h+}k(Kw4w?y'
        b'M{hbMN-cKJkEd|Y(VO7MFGG>~rkkF(Zz5lSK=-}+k1IB2V9a7Z_V7(~l}1H(JwcMKXSOp(5Hu!Ygo?cB@!X_oeiI^bz(CEuc@O0v'
        b'LU{t+IRvF8eC7qvn+UW~S}_s%OshKqolW{Wf>;{C`_X&KZ#vMASmrN?45I`?+T_ux^p|eBs0I85q<d<=Bm*PMUCXe~_uM?Q=ca2V'
        b'HYw>ov%S^59U0Im`QOZIb^kNs6cknW1;<h;%54)l&)xJ=3u{FC_P^fh{_3LmWQ)CCRoBfaPu}(lzN+i^y)ypx>3}9d{xwcn{*&i%'
        b'V2J;?H-;NSJllqdu}Lrx?gKk`DoScL@#l^dQ45yuTazh@T)IN!*?5z=iSR#Ml)m|9j_syXSR(?8T-IbJ4^?reut5an6`d0lZN`}Y'
        b'hd?eW8Ax>HW9(+W`m1g#4~=vRG4W9jBgOusG|{~XeH`=XO;(F3bCE3ma*n^Imt!9JUvMU%Wz|h`F%sHBRETo@3}y@Zs7U3dsb%TS'
        b'c6YM(jEp&q$Tgmkna^Y%7lQls2OhnAa@EqcuMRK%4?q_1kP88-m2Kvar^rKV7d>hA4BF1f)?0#>Mz&rQHi?+MD3@06yX+a+%4H;e'
        b'@;G?UOR>IFoN}d*rdp!jja?w~fWwKWxznmjC(;^qV3r?fG`4rYzaZ4uejw_#<qJhQ)XnAp3NRjhZYBMrZ3eRhmD@3)c`!t||5jEv'
        b'oq_qDLE{0l$S-t#sAp#NwuIgU`6Nq$()oV5vYd>tPK_bq5&MNF^3Qa_XAmzy@efIrD<fJDmIA5fl^EI(oZrGJBf_J|$fd0Zw_dQG'
        b'e7{N9*TyLaXIlrx_`}(m=Xe<y9Ba8g#-Hux_1=c$jrCbk%vwI`hq3QOpkIy@GUH=45|--OQyXPIBWoEO^LpQHtZR3tGY=ueoZ+#{'
        b'BFyX-G>I=;`<X2W<~_LXGS#nqjRcl9TFzV@iwbHIY2KL!C9IR1z3;Biz3jbxrfY1SU=kk|e)Cl;7?%>w5fpDen6f_iw5UnacLeAq'
        b'nKNU*NU8G2Am*bn{=(D}C2mT<0Nv&p+*Wv6+#~|@oCn4{{}?OM=+Pc%jlKzoH`OtA?-RX+@HX;cAxaIOKx$(>gziCUc#EOSd;T^C'
        b'pJ>t#H@yY|+w#E})ZSfZXF5;~p<<{Ctz)X2s<d9!H~&Ue5cj<~kG~PTrFjg=X&b^shge4t`G>gqQvS^KM>#BAH0Eg-vqkGW#hAx_'
        b'@1t(a2p>YsoPn8EaafCY4BGc7pT$a*Wf1d!gJAfEQ3q;y9mVsqzEPUKYs|7T&>y09j;+I~*WjUvrM(9w2|*E!nzm@o3KTdkjA+c?'
        b'&*i@X^6^ubb?i*VSgYIpoe=ts=GA$v-j9)vk!fDzl<_~bdM3OG0Lk}p)K{Y(cFaa2QsD`l1d^W~gYFF^dp#5I5zz>ro+rorIuokl'
        b'K$ot9iKxsUZ7CijD}dfzh(gOsiFFlfNO1PEvx_ZH-^hOz=(%BCKGwB(?98^Y?}R`U(19dVTvtBtrB(>^y$&o?p1kf!1`%fdKI*^B'
        b'xlmlPcP_Z)2VP(njgcWaDSR)<#7N-^QO=`dD?}=@%9Ak0oI&`?fAv#`Mm?($i6$r4Vjkl=*`qvB5m$3!c%npzD5a*4d4!i`YoBFX'
        b'Z%*dePLZX*Cui>1pK1P}AJqNK)~gKVZvka|cjPvJiJ2$_P^NYjEyE($7p=rVmk1FE<gL|v`&lXKpRBc4Qv&k+Ju`32MYTI6;24W{'
        b'azT4so>%sqz)eqc+wDTj?QhS_8*B9pPKt(czKK|Cf8DNmr^SdH<(zWj8~Th4dgEzvR#c<c=$T*&Q7yMWnZA;`7;qYI64fyr^bi*M'
        b'V(M4V7}=#Dqo5c!;v25+0i!t!Yx!}s-Ay#U#VB~92mj^i8U^N-plouw(c~5_LL=q@Z%*f^jpA=T7HtW|9U0h@cSp^!nE4aIx&Y5V'
        b'N13fWe=mQ|e9x!-denMnbf<{<_h@9vF40bLgCw$q^$hM3x7;2r-%KtBKK+OgpOsoJkPtY90x|1x#{*dF!4xv;<hu_Z>U)|yu+8{S'
        b'!YE8>64w2{-&gE!5;EryVo?U>`Czp5D92=>Aai{5mvQyO7t-IGrZiKy<<)uVACDGM?ZEq8LQv*L0`s(u>d%a3MV&m3Y=9_~UVn0w'
        b'41tixJIW*>Kzhe$vM?wyMVKstr^u4`ar#@MDMCm76jrXGag1*71g6BkkBfu2NT=xth&fI5nNIWP4R{8(F9m-Z9E9kS8pV^+Q84aW'
        b'WA%M)O7Qkf=-zODZHqiqi8O$G74_)P(7F5#xR19{bIL~3%SMYdm@OIus|fuvD-)Fo`#x08m+lg675;Mm%JZZ8=SK^LxdbTz6k!>W'
        b'Ux&|^ZskwH;Qy6jj2D&kxp(x;=223T5V)gE?maJSY(j@;O0f&|tt-L40;9&gnOw>ImFH#NXw|;a1_>h`^=i`^0;^twcY>=ht;#YA'
        b'As2+gT!jf$TTrMHLgB8$uqqo0y*%nF48M0a+HKDN|D=4>tHzWO0_OaPs$F$i`zJC;^A{}{ToI4XHuU418SyZqMs+f%kDTX5pOAVr'
        b'80b3^H>i_A7ZVsioqMKt1bhaKU5m6~#MEi&W%ZxxMHlh9Cm}a?bhU3B@$Ss_(N;HyuKjpI%RD~nj#qgLfBB!hZIqUTRotW{e>`Gz'
        b'N!n;P7F!!ZyYW$%Jihi)oV=25<B#Vh!&qaO!KUC(e!0!hPm*GA7DDHX(=_M~i7g>do+c71ydOs~6(hj3sEX6#RUYOf`Zf^4b%J$z'
        b'Hab|hMyEeCay&%m^ctcSc1OC-$?8{*)<*;2qQK7ni?xc(R$*Oo^qKOJ&&vU`K05!t=;I;n(eO1X?tTmVPT2QAG!I`B&GX8Lt2#Dk'
        b'x{_W+Q(#OAYO&9Z=oB8N92H&@oZ@ogP?i1sL2>Bdq57RIuZ)m^&5cN#HlU+EYYY8nNAl+z=Qh`(h+1@tb4n(E+>@Rj)%ow%mhfTp'
        b'7i&7~?=Mi=6R0%g-ypw6Qs%0`wZWHIC=s3RRK}n3LG2z<`SX^Lzns4b%<Dwl_K>5ath}>U-V!((@7%xN6)55liFIWP03NSJ)X$r4'
        b'H<X6YS}SL!M&g~?Fjbte!sU{PO22W}%3PV#cLXuFNA4Y0<qT7)ZrSa(_80=}psrQ7=8V#ph3IGSA}dCXjPS>&Yj>(tuXVW4fl=DX'
        b'%2yX0h~t5%qUh)<tpK7U>FK<?ew%kC%9}pO#cTJR5Cmx}r;9-U55F8KMRv6lopOF$YUeTcM9wTPrzJs=Wp+C{c(^PAaIKjB;s{i&'
        b'hN$OHYTI@1o+OsS?Dp68M9kHHI>LN1k`x}KKR?2J3?Ddic7$&RGQx*r%=itjmg$s&lX2&ld%Gj)Al3^uW;_bl{mh|Xbo_nBx?4es'
        b'=^u>1dwI40!UW_+*8Rl!&k<r;MpW)%r{uSHfHOx%-oUkzioja`U5U(JN9atPd2<BJLHBk$Eh8m+g6Gohqhu<n1&<9esI2t5-7RdU'
        b'Wp2O3l=*?**qL-UEgN;p?JWO4w2YS>D+c|iUc$UK!k>vhxAN7{7!a~oMq*NM<}V{@F1hMNThQy}wavBdl{7kd_4s;lETOxoobC4L'
        b'ciT?MRHsmWC)V?E)C(iv7pqRm+MELWOMF2nf{vfdpRdn1t5ZOgj(|U@a>~+b<&`xEtJdG%2zA?B|Czm;M^r|YK_nva*?G7r2P0`!'
        b'qROyLv;{(|FzSgB{YH?Yn&2|RNox&dYUZ(#T16ax`HogmI#9{q-9{HGrUASDe}F&!{9Az5S+#zIjPQfvoOO??y@W8bvCpW6VPTka'
        b'66B{mR;8b*PCno|`VUAD75HDk(y#Aj;#3bM(}XbUWJPP#g_z&~x_v6@8&!RESK7##^bvAK>s#nz$GRQSPQq}6zv`(*N6QTE?bCg|'
        b'h9@*kpELqs{h|>+m@W+CQT2%<_wWp!@O!$0))LduWLhLLxYHm+FB4JJ2)aGB?_h{uj>r+Pj_E={-xZE_`_D+G(r$R}8)50kK>$5-'
        b'M`-u}8+^`4KI2dG2F@Ut9OSn+?!4twF%>@I#Rc;N4<GvjHG8D9T5iY`rl!>3mlEZvwaF{IZ(;646&)^3+35|J(z!DCJLzPws!>PH'
        b'7y&m;l_*m+%H0Q54Lh}4<Fwjvpf?bUE7ZotWom2Vaw*|RTn&2Eqa`;m5*391<hgspD-|6+c7x(>Tsnx#)1|i6<LJn{Mmj<YN)n2J'
        b'51m1!x<6f2tD|n-sI26R0x_#r)$Y_vp{NKbN=iae@lez@C~Eiy6g70i)XUGw<n-KNaiL2jI8A^tv+wvLHHw&&mHY()m&)ayZ*N?F'
        b'o2!>rR)&-}vIKUi7X2vLbY9LzNG~~MZT#<mb^`rEk#)!+_{Y*V|3Z-U(uxJ(7P`YBcUmMMLt>K!q%ci&?~YbBSmwfo0fiyd$2a&R'
        b';((P%lcyA-j!L!PxKt+RuL<V$dy0g=7J%0)#ov0V_ixa+AoiGydiMtU0h8?H+aY;H^_<ay;0fv-h!({j8>3ooT-q(yCAT?wwk5B~'
        b'6aRGYU$ecKdg}({X2S(AE^j$*=`57n3+#;h#-#!|tHoRgJGT`&O?v{D*k4?l=9H1)O?aBK&EBv(JFZ$4FSEGt^rOS(Blj7iL%?M4'
        b'im|>R+MtwXC&~;KDM_R_U<`%`{}np+r3RCrIa$ssrLH6QRXSzpz%q-}AjZrEk|v?%{okENSNh(iAfJ4kwiMs>_4Dl$^)pj792<wa'
        b'Sj}zl{VVVNZ1(>Lt~xdhnE~9cY7zfDT{r#z+(>`=2C&ya2(pC}NhcoAZ$nHrsIf|?9j!CkZ3msLncx72XFg*6ZfCB&T<EUXVbTj}'
        b's)>7RJ081{Zu93Qn$GJn)HcZkv`*)AR%HGUC@X)Hb^f1ukzr92Reu=9g3~ak=SW6uJo=|!7B>eRy<ybJ*SVcCk9`>Q_O#MoXS&VB'
        b'#-lN?EXDByhk17Lcv}(Pj^E&IHSy<g=jd*Dabb}NUHEJ@+$cGjbqO7)*tS#L$^W0obrG1mQMfNc>kX3@z0E;y+1@DIR4Xr%kd^yY'
        b'u3TwTK;Jcv3?qZw$9Kc`El&Bu^fg3%FN9}`K|N;*$>5{~0urD8<<E~>!8c%BWhEkAbMc;56__O|XB!oK14^yI%gg96DX{3U4N|I3'
        b'>GDT7e>w(p(E>&YqKa<waH$21=thg=My-UI8jh-<GX*q(H3{fU5i@HT*+7E)x5E9lfh$-Bq#sCu%2JcV{Be%;eD5hY6pH5u^7;!T'
        b'oB3(@+ai}lu<uwf-$|I8!_Z5d5`RAda`znj$=^Mg8^fK`F?swQjZmk-VKT^GuWEPe7!@kNsviKg7a-r4r60H+t?C?h1wz)V_%jnP'
        b'?U#H0Gh8p--&nKqgRMy}P*0gcSFVgyRQ@&O_)1-^PXF03(5ySfE2q~%IVEp9ElJTPN2DYhq*zK}@_s|1Xnqhsr;PY=ZunQe_=cMV'
        b'z?QSaWT2ldwQ^t!b#}OxiqpfZOc0l@F^BtgecLd!f>ZL#R35Yp-99!wlRIC+oEWAv-|+L1`r8movm|YQC0(VJ`C<8cXEHrQWT30?'
        b'VSa5Y^UiSTO_u~~X&SDib&wfq5{%ixHwj)>9q2xZCb^lz2+&dolrnD(^Gl1G1bwO*yv>nbH{@{-)6r;_LjUHlHt~p;6q}<%w27S}'
        b'%(;3eoon1mZ#C8%IwWzc>1ag*T3%Hz=nTNtC0f=@^7Tqn6=%DPm1Y6;$`Bj8pTzeSO5u~HR{-wxnoPzy<kDs>-!-Gg?A1PTI9%i^'
        b'e4;Kw?zjDzVIV$}$YF<+y~6a8VWaSX@=>8t69P_9CQ%VhinkIrjiOVG9qA>-MF0=LYF0a=cP`x;y>)5*f{wrytBo2(nV>-qDeC25'
        b'HEv&y7;Kq6>DBxh%)%$P4nHBy3^@F%USEj%Dfqt75r>3ih=2Y&{pBI0K}tu5GqVwg_^B>5hG&3|%v3uS%foyP0hSP9ksHfYC||w9'
        b'Mq``M_1VoV5F^0=q2?jy(lQ02YS+?T(f^w!rvUK8qa1%<Pvjn?8bUhO?gUJz3=a${LAOAJWG)q>^^Z#JotjML*AvTY#WhQ7Gkw>%'
        b'mjlt+uXJ>n_}~8VhMJG6(i$wJ^h3=jgv#pzMnB}y4}<P)b)(|igQcGPp=&S?4D%Dm5LT9Qp7>!Of9E|jXV?>ivS7o6`>x@h=wW8='
        b'5crktVN!-3{&gK-K;9fCa;PSl)!twErqEs{+*3<>B8L|zK+a*m!AlPw+KAII<bbt84wJYm9#^%hVrv79FxsGHR&PkOan2QMUBTLv'
        b'Bp14eNE_Z^?)XnxJXr9j11;Ak=SxhtxUy9w?pz-i7q@~8wrKCxuIK;JL*Gju8)|odh;E)0GV~BKj>d=D4<-W@_o0wAYN*|_7^2aX'
        b'ZUll*KMd)IuhRwLbU_#exL{}%tfIz-$RN5Piy9qjBItrhYGkPB3!E;vkGe5L7tG<GG&KxQHUEsJhTxgXh*6HDH)nV#j-aj$ne)PO'
        b't`E_9Pf%CkJ1S=Yz7=#{2-OS0*qo~n45h&i%KMW!kD&sFa(ag1o-*e>3`U;$C`T`kFs}`ym+nVr)?Y&xlIG{mM9+yy>i7_Qbjpll'
        b'V4K<3$lPmGW+Spr`}U$|{_DJ@S}XTl8j2#J>YdlobedY7(=b%Jt4zeI*_;bQc1CE<Q(wxJvmnS3FbZd*^+>D{GcWzC-Ck@yDp;RO'
        b'24*)@dzZfMb#pnM>xXM-XHRyWsx}?XvATt$<#KR}O8*0{a!tCuQROvaF2EIi7}<iTcr<wELPI*D>UY5`CBz!l_Twr<SW>VvT^WzD'
        b'QjAR(u<juKTfi>+&?`DEYvEC{gDvYZR`eme?6g-PfTV~A>w?{OVdrr~aOsIk|7s2+ro1qZl%i5{f@?02VHNA@zaazNWxG3Tc*K*_'
        b'D|?N=0CvwcSyj~#8`unHzf)HAmmzjVGa%7!E;dZ=aSYLJ=oJ{fv<6fWn%e=0TJ4oYk&&pkM<B|Yf@$>}Qi@gus_hj<PstF!K(K}k'
        b'M~)p@{70+9*`)`RW{eK~e2;A=8xTsZAF^mMY8|w9czdX{;)o{)^&!TL3Zd03dk~A2DCvMea+OLI((V?3ljil7qdGq*XJhn$V!4Ku'
        b'6a}&B6)-R`8;95e{o0~A^lV9qZMIh(3EInjSO^`u`J~Qc8DiG)a>$F!!kI21;asYHv|^Vl^z(LiP03b4R>$dpCSh4RvmOaX>3~<b'
        b'-<j^(tgx&PcWJU(-J2`-iYi~)UAEM6GK|$^x!jxWFN*AOU{b_Aig=I`Trs%)FyBzA!P*Gcy}8Wb4V99?Zv?nq)lKN)Fjt6>ZQ|^;'
        b'vhCnE)FLa#^{9{y{l4nw>-N~)FY}5sM5uDg!Tqw+DrVjgf;=juC20Y+*|a9x^){!Xgqv779Wu+0Lq9qTRp^C4uRD#Q{H$99%=c=t'
        b'+#V5P);vK~IJB738<-00MXSDWzE=zfqUYQYMDP)wE89Z(?j&sq81e)Sp|o#>((34nqU|53(A|2db=iQMDA&G6lv=S@Z9p(h)=%AX'
        b'W*_2O!Gy%?7N8t|1c_k#Z3?gOudI6y?Y6tM)lE3F6=5-7T-Rn+cxkn)CG)!Hi|c-Z>V~8r!Vm~u+p(8(S%rPE!64$AdBKR}a=D8V'
        b'LcgkPl==IVIEMoc`(6jV?%r(rE9g0|`Wa9W%Jmp(_jna4VVCZ=;9YflF#mYne4Tplx<Pp0$QQ{5%NNpQqxIcEOZ7}zc)((iQ!RrA'
        b'{6uV?NPqdd!M2RV!O<+^SCgW9&%gb~;Ko{Mf#orA^Mk5fTKOLO30ki?O=#ZY&{@Lg&7YsWzL9uYdYX8GAZOQTzYN#aWFC3EcGVlw'
        b't=g@bZEJV8Re%h9`=5@63Q?I^`Nc$oK|IJ^l)%_D&S6Uez!E+!d6}$P#osA}a-VmaV44xTe4QKybmx=}c06Se0g<@)5=REuG$F|b'
        b'7};ygPIY0%F7>XA`oxaF6tiJ^>?H1uom&kS<)rB>XO0Om&_b|INXbrhZbq59EW>GrG!jS?qnJ*C>=UC!Gif@(P0v|XUZ?N<Q_U$H'
        b'RHYSrHFI^kTZqf<;^h%Kvt|x5%0!s*V}Y_-fDzwNYp%EKzE0yfTCVuUAdqkx&wn5=LCWm9{>%Saeb#mGJuSxx@MkQm2_|O{?QYS|'
        b'LGyGH>_98Ea?l&RL79q{J+^GWj<PD}vm)x^QC0=lf3wHuHi}UhR3HE`@j-Q}p!rg?qNDC-|NQZp)WP;|ah43TWD1!DgRMt7_A7x`'
        b'@|KGXb-$zoy>1_nRlctKeC>7c7%D3lxE{h><m}GQ1(m0CNToKa?Dhq2_k!++1nfhE_n~|1@XtgKdRAVCtlP;jP~0x5pj8S!M6p*&'
        b'd`p5NhCXg*WtA?O+be5sl~HNe?X~EPVeAw*6SAr$*8#^KFF>1+&<-U3eVD1&z3z|5Aac(6z@WyLgJKT|oZ+rdZ&z%)7-YY=+fq8!'
        b'5yt4Q&zIcWKh!=#;y-4FSIxf;u1S5MHoQR)C$EpwrZj*dUCw9`BC>g7uX_pyft;#n7_*cu(brY<!i0(@K_@L|h6aFt@l*|t9F1xJ'
        b'=k#Dp)O9j2saE7KYroeEP43i@<vYq{_BNrNNmp*bnw`METT4bGYkjx;K8EbNQxdNQL*L)d;9GRq81gz9?#dJ}f!EJSuh&ajNi4n*'
        b'nj=!+l48xPRJz)>%FJrjOV#!lfYm}a3p1>oPS1Qckeyv@3+p{_hz;x8=1e-Suucp%;e`%#*WYOZdH}MNK|fi?1`mfyy)jtYyQ<X2'
        b'zHzQbOa^`M>U}E{$zbJslc^~zAute_-6;n@9Xv>qu&b*bquj}}7d~Z4?4*q~VUefM3TwpICz}ScFBRKn_a1PVXZLMe6Z@V#=i9-H'
        b'!rZ6PuM`k>RI1sHt(`-j7B&%I%j<@?ujCu0%;iB+Y|F$}wm*TN+q-OKqH=~HySW%$Wj?}XAHNlOsO|<=b$-woDCk&fjD0fc)!(Im'
        b'GDs>6OELY&gUQ5)Pmv0CcCTRt_TkPwhD5^(p(zkk?QN^9wzmc%3$5LXeJ#%)<RS~clAjltu5!$Kg9fnJ$M294;%|_`A|;+<gPqCp'
        b')Kr54i&e<k^8%1@0O(Tf0I{g2kn3Ddhha+ZU0Q;Z5ixY+kA^^t_ojCRF8-9mVhpMnBU+B?T|tOH;b;kA2q%z>AMZhvaq9@*-*{l4'
        b'=vUwhk>ljOeR8i1CgXP%`V9lDdb|F!fj!3p^o{|YGp{T-IhZ}jB^_5b5sVE9T?1aR|02=q=9p3x)Z)`Smi+6kP+qGB$OQ)aPeF-k'
        b'iK_HngOQ23LWAv3N)4&sIoRqsp3rf!Rd-OuJcyDziGt*3oYi2Cp`m`6+4es<PY#-GPw~&<obB*@nt$#fMP^%x*|sy6sCX?`$fC6e'
        b'v)6{vIa>$4BCPKZvRtBIVW#$Ay^vqHQ^8WJ2gql%Xy1cp-5^;3_G30ruaG3j5Y>WddX+V|+k^Ya8P479-wIF9Xc7U6={pX~eM<S_'
        b'9X{r`5Mr8Ufc!WHIIQK7LC?ZL#(>lpzh)omn+_upraT*(o<5jdto%Z0#svq~<fINlS`is_sYwNTnpEf-bzY;ufa3?M^@%8sNG@*o'
        b'_##h{5x>Uc2AqKSd4t}AA0PyBMpi}RsbAv>11?fl3rWoq5vgQxQBY!1ZsH~6`?CjQE;XY2Mx#*P5@&H%h5M8pDdzan+n6E^G>R@+'
        b'2TAOSGJ{dHL>v=}`&5`AnE3FZe%2uQi7l8|YngYcPQJczv{8PX@P30ALite%C>t?WF~J5CrB|`gv`qz!y+CF&6G3YVMCT2-@Cc#*'
        b'`?YpO--idhieCNQ0e{_4vR~*H8gU$oI?xN<#)zd)4I~TaCC03tpCU8`U>n7b4zArO6vIGj48}ofEP0c_2*9+cC-vh4(8m%{V|m5~'
        b'(6H{t4V$riHR<4YbtJ!~JUFQz93YojzaLmf<i1rehPFDek`%5W$ck2e^BnW}HPo&*ILxd@TMEp1m}S|d=lcP2Uf*0Ym#{p27rZgl'
        b'mKO(D8dDy}^1C@NjWPco_;t*pUc1K9|3jS{h{?pM&j<K%D(YHnazNET2FS43uY>6Jzq4+^`!u>~%l?~rsq+I)Nkxq-42umHIx`)2'
        b'Ilp@5;~KBk6f$Q9DjMj*Y^rU*zs<D9Olz}i&0_zZ2i6k<rMKCF<kGL=Om<q<M37`bu#|fJ8chd)bf1r)c3mR_kDFc=XX6vuh6zx<'
        b'WU9?As2qUNRTvZb;E~9fdH)mhU>1A+uJ-~*w{sSDN_hhFzJ)Ois-I>mWX`BUqW&%j6U@W@efCl<45`ILrW!PB=Qr|izE#Y?)DpD}'
        b'pSMGHQjw{CL+lvxN2q6DkWPosQ^}>@&GaV)1Ya+Acugh3_@`-<uY<=q;F4Z<eJZG|3}HW==~{Wc%_(=$*k{g0XMJ$3q=s$?(;8~E'
        b'amo2VgiQ1M30$X7Cvh^g1A1yeo~mls!2TCm5a?Vo9K;Z-^;FWT^1VbLR`G863q&Rsxdsw|ahBFRk?p?K7pV06{#N}p&*KA|-dAb1'
        b'Dm~i<PK)abmDa3lO}H)Qp<hNMn|o@$bW6kxo14>IRBmzMv^)0RDo)6w=&a7xu8Yb#Ep7^6{(zX44(df@jFztrnaARpMj{hN!L&3X'
        b'8M?eC!br<mwKg*(bAf$n8wkT2lC;;V-MPE7*QwH14Vae-D=tK3fr*a1_lbVUtk6)CNY1Xbw2_kRJ=M9w(hor2Z(k#`uTiZN?o$eC'
        b'4K_T`MFf_XR9bY|*}_XN%5#Ok#^WwyU}12L;<s589lg^0-+2VvaEXhM6dnDWKNI)=%0yCVtjYMVOy1$_|DB1^?6$AZTW^jcPm2)w'
        b'k%$)uRyu`69&Ec)RVIW8ag&Jo7*)$gE6i%3D%;UU2HN*kv(Z>l6SuuqzTNN4ZpPLsakEWf#zVYB2&r_xi17ASJB3z!AiGw+=^onQ'
        b'P>I(V(%K%DKQXKDa_$$uX6Y0@dHb5~UXEqLwMxOd%QjqUCZtbRUdwiXts_){3muL9ih-MrQX8INCKC93T+mzjjQX#&)e8QLG-HA-'
        b'INGd;{;%@h>TkY>hH{fw9oNj}XtQM&^+7*PKTuJ0TzHYlD(}2!Pcbe1HHAmMcJB1ggwB^9I9o40P|n;%EQ)MoD*E}|mKEEM<4hvb'
        b'Q(E-fTz~2s^U1YVb#_!%lZ4rhaN^d_mrl<Md)*}S9D*IVKz(?PzARwdqqVM@usEq!%bd6t7q6AnMs&0{Nc?Myt0BYr5+`kOat*X;'
        b'!f!8m9`9${H<2rrjP59#rEj`MNQ4cN6tqPN6a`2vYs{8m(B)@(-8cc&*nwyx1Q_ML2I3Js0g+@drv2icE~DEQsdUBEfom<VL+4^J'
        b'gueLQjncG(d37n0(^44YncpK|(z{VDuU<oH`9T!)p8cdQ3E~kT>Dq7fZN)WS$5w%Q!@)^q-NGHtIePXQ5f}wTj?!|V0BrXiGLf5B'
        b'!H4V9yZ81?N0HN;=vMdpC!fjVdt3&F>OU^<YO|QlpfJIqaAhW(IPW^IbIQxYom5$zQ(u;{Z!qw*pb1Cr?cZn38FjT!RN9MwOb%j#'
        b'`}w;+llOgf&GYCrRvHpp^Dn*_?}acX1r;M6<EHKBoUCiccA>3ZrCcp!g#9j$fYq+Dm&x{pEvoxW0Z#JXZ*X+KQls5_A-Qv@9KO?*'
        b'*&FK!A+C@TGE9or=C4tRFtoRj|8e7O&+_A~TsDn{nSSukjppdDRoG(a+_+^(Y?S@hAFh%s+BMmkc`xHjMA_mAa?UW`6u6_DRuJmb'
        b'Gm(xzeHQ!}B10Wi3ub1==FSuHlOGbRFvHoqam$oD@1T+44ysYzfe`R{nSWkwt_Cm2jtMWcYDwhSg`im1SygAPJX<=k|20J*My$Z9'
        b'e!L2~gUCs1wqoU9K;DOIn_QY~^w%$i$iRI4{91gY3N68T75BwpInZT9n8g@q5D6@2CHkp;WSaNYb96{FA&jQi%%Z0Hi42{Y#@0S9'
        b'X^oEcM#pG!19S1^PtVMG=c<=TXbs(f=0N0JF8)FOOs^MXIuLDW#-lPM7w^xPc-<1_9D>ofP<az?B{IEgd2_Qcf0exBnbv46gz{75'
        b'>HDv?t7Vr%HnkEufb<o~r`10h?7Qo?^9K6;Yd!k=+ub2(;_Jh!NPOK`-A;LwlzFHBSJ~CsLzG%fGs!XE_3Ms-myGc@68ZlReA3^9'
        b')0qhja}~U2fP!!Q=5NwcANAMc6%m@}IO=47E1i5OQcBKfM<-VZG|zL)8&|z_HmgnLi?%aW{rB?i2=@PvOs1jt)g$nHLOd}&f8Nj!'
        b'mXpDTQHS~sM>&HnS%0*@o~XOaH4u7te<pF@)p{axC9@wTTR}MPaEAD~%svz{*mAsdj^&%Fd;MJ5im^v=J8Op;=1*|^|CyX+{ip+q'
        b'_Ur%BpZ@e!<*pg+p3GMMZcC;Jaf!;fYNNB3?;s0{z4Q|>;1)*M^0K|^?2hun;(Nj4o4@@tfTAjx{Hy%%0SN+Z>TH^RBF;jU_ZQ+F'
        b'du`G8ZN({PKfU?B{F@vdI*XLjtD`BlpU!(gGbQup$(smGD`#c;VMsxP{=Qiq>$TD3Gic&Vv|rgSpj20BI%{9IqGeY<c~bM*EXxH6'
        b'9Ss@=SyOa$h?2$3qWzXoG&$P$n39erm1a~Czd~o-_VV4wCG}w^1P$`z+WO=ZRD=F>V7o`xL=+Jrg&C|hu$EyKq6#>x>IDswdU-=w'
        b'J=LJC*Eb|X?P?h3dNwbK5kTu_DRa@jbF_rAd#orUWNU`w6Aq(^>rbxk$7uC+n*Bo1M$6-4i_Ys<bym&nGTa$k8@w~AjNWB1{gdPM'
        b'Pn*Zigrnl3$O|oKOkRYV%`!25S{g+*37B9M=lNYfjLZV&0X{DErtdtzCaRqlXA={x33AIzSlxFV?GCBLz$ci=9=+nZbQQS@=9z57'
        b'EPYsi)rzY`h8_)#W*J&F5HYL!9qh74(CL(2a)KU^fqW50kQN~zfEh?92wdxD@pGy$cz}-+gn`aN!^g!wbkYbve(b;kH2>xjT)r-l'
        b'^*#kYhf?-u(-UY*vtZQ@Oq%~sE}_-IyU6ni$5(z?J`&7)+sA4bDKoL@Yre3GLXy8Q))oY!KXCP4UxIPqCo_%(<)e)}A4DyFe@mz='
        b';m0knh3C|wg`(zA;qv?-68RZ(Mk8s*EiRIN0^f*}0WJ~NvBG7-Oh0o8l6}V&3HuL+&slu(aQLi*^26b{ScgSE9k~Ym3%6|Hik4yG'
        b'aZdT=RMkJOx&p6Rb_Keu7?XCD-w}Zo#N*<5n8(rQT86d8vt&ebi|BCVy0rb($`p|+8nb*YtZL|U#Vx$s(DKz)G7Ie?`4XkQyK?&{'
        b'ZS5VCZAZ`q0<*ghSqZ}Pf&&*;mAC@1m`@j;4q&z+r~}8arhv{sh*s{u192aosEDo+b_`UxAmgMXU-OaP42%r$ea=Oe1a*i<ILnvg'
        b'-cR3jyNjb<Km4F@!vtDUXTl;2OrLVk28z$~^8#mZhU8V8H6yE6IUxg9S>p`pZyT%$hMYnsfRDQ{MTWW;?$)`B^{-q_&+4-geO~MD'
        b'TceFi%S;=U(44>fw79vsxYe5CqEeJ!W5#GBI47hi%~Ea7=<}YDwYy(!b-#Y$!pW0OcwaAP6udoO+9b3rRoieZVa?jTN#IZ44K*4u'
        b'Gts9Eon@m^SnBtivW2>Qd0MV~(;AiaFIUYuh1uD+w!HYfjp()P4KTY?%;|6E?6?YAhztUAGzam?^WxRhL_6rrIVfaMKR^bOGoTQI'
        b'b-pY8<I7e<R!@>LTp!tIP#eEg$n+WTk^H410GxjU^X4xDFW)jA;HBb}E3y19xrd1Pejks8TE19)T7vp6)X|mEYY8OszX-G@_QBXw'
        b'6hok02r;t{d|=i0wNfdY*2qX@_WRXdHwO_cm6Gk)&1UqO1#es4yOk5uXV#=EHMhJ(FSxP%wgNNJODZ?5(U~)PeLrxdB*Da5Q@2zr'
        b'TvUd^ElpX&=8M_<1U7$}%bIGI7aFM4(i^&FVP~Jry5g$-Zg2BPD#Wo<G9XTON|uvwHLXy->2X!1PN++iXBWtH1uBvNj*>}DME2oo'
        b'oAm)(PNCPTHCQzUYmC8~Y_O(nB%URnfc9T(u-<Q=w2=oPKGk3#fO|SiqL8}XYoL=W4pQMTJS{`~vMqB_2~_CSp9XN>w}gRyxI^Ll'
        b'6OkjnYS!dbgo>Xa%yeeJ)4145^u5MKeJno0v6L>0AS3o16Od9DrE7N!44;0B29Xb|mjoStDPhCGeTlJI<E`$>q;TA~64NWLwx5xm'
        b'{ICf(SYtJf0p9etD<&Ybhort5uC9_JLwtKVtcVg4f>;cT+#yq8+xP3mSFza_WLN~h6+d2vO@KX9cPbg}!{0Qh|Gv+w&N)(kUfSwD'
        b'^uYltIU@h((8JZ?RbTaae(r;YHpJz)ovM05f2EJLCV2B6MnpfARD=6;Sk@Qt7MBW00)W6f5GR0l;d_qZj_2^K)etg$ghIXzc$ON)'
        b'wV;scVLTxNLXHq3OOX_Yo91H%N<+rG6IHC>W5|cxtpjUK5UX$RW79t-GBWgk13A)o)tSu~WR|<@ftJf|K{BCxP^P<B-KHz<P?#jd'
        b'-dM~hCNy@ATq<6}@%`+;$&(QsXcdh+z_R~FfhG`g1lE~8;IO)9IWk(j3Z#p*#w<Qoau7HD30s_(6pQ;p1W~IY?2E;sG9c`@jgh-c'
        b')K4EO!Nr%bg5|hxHFkAv(4NCV`MbENrQ%c$D_A?uQukZ5fl6_b;oKc^j_&1ZyRO)BcG5-N&-#9}zflcFwdJe31~<-&Qw*u~9PG0v'
        b'szBV_d%c}W@@EnmN8f0oys|ode>F+e<{C1c;$;{Xvv0wneXm6+l42{#4CdKBB%kL-Qk<su(3bq&N&9fezp)bavr#=sv!x~K$f&bP'
        b'vvJ>7oaGRR)cwkad73|QQ7`yp{0@Evp!+OXLLS2T2WJ49dnWafy$1DiB{6RB4Mkl`I*x-zWd7Wj^c5~X$MK~4>C~6>F&q1Id%b4r'
        b'exTCeDNU`d%{6B_O_A8*#1ge(u^PA~9>x-mCCv_4tUzVFk1}9Am_G*|CT_y?S$(9WtlBgKTf7<|rY63aFhF9Kp$e9Mu}h*$l6l=x'
        b'hZVT*c}!`+V)o*WgPeXz-?n|V1j>_2&=ty*ixz3DT-2lDucx4T8>$gE7GcnKj%8RD3W*beH@R8r5_J@a8nk5-w)hJu(oxCjrM*y;'
        b'QhCSmGKXa)B065;^f>V1A!SB4liFvX67~=QdL<~uoQ|iU%xN}60r70!!{RkiB7sVLi7QcW%;Nd}3<u1y)LlF9zTw;z5QB}?*&qh1'
        b'zxyvSDEyY^YKwYW0GjuD(b;54o@Ww0qTkBEdc#U5YrWremfMhr1T>FBQg*)kH;v*?==rJlnM6oPhNrA|t#o<@dV!3uq>xtkT^p&m'
        b'w7NR`Qt@SLnplf%=qXXhZ}{dg$ayNZ0m;3in6oHJayR5gh8fP)y&=}s?AG`6x-#bY-r@{yYl(Wk!M!QzFm5tn`j>kQL|BX(7pHOh'
        b'p<YOU<k4+U)G`0=H54W|(BaYsHzL=O#2LUl`Mj4$`KzHY%!E$X)R#`@;CO)3kM@ueeDu${^4)r0FPkw}`D0gK1{YN<-aJJrptG2E'
        b'avRPj?dy-~*#c^X=JfyU-SP!)QgJTdhFXcKlp{4}z>0_Pk7Ps?QCVIMIod0WEd!qz&K=V2->v-mTSo}kHPF$Srrzy|Z7GGmJ}!Yk'
        b'joHvkYRmG(-CPz50x{=?5G4nJk|+ndSJU9OLxk^ZuH#4jpL>$?l)KyX2cX`jM>wP&_Ri8jjiBnk>G$@M$-WgFNUHefDH}A@qVxJH'
        b'lzlas3^Jx~>GAx<&kMAg&9G9-p8LdddsOKgjk>nwIPSYX#q8?c@)hnFm|_m}+V^^SF>tNanljMwIkmkoywnqi1H<*Dy)7^IvY-vo'
        b'$!D3R<L*RVWwp#@P0*Wrkoc|!>HCOmBqdOlB@&ePKc_%um=}BfLesfOzO8z+R<7UH`%JA1M0p;E8Q#LC8E_FXAg`BP#%62=&Wc~>'
        b'px}*SU9AdAa4beWP5)RgsAnQ$p+Wty_w3)^kC%Cmu5V04yW({xcQ@;b4;=HX?rquJYlzSMfC%V|;i6s@k4`p2>Dw}W^QKr35Upra'
        b'YPCh(g>0-C)}6cudh455Nj(li%DMwfv}-`&I(B1+w&3C?utQ0>ZzGm;_>rs7Pd!umupU;uRC)gJl7NbT^V+lXpu8~={O)auO@x1='
        b'+C-hl(3_G9758NKy7`Lx(lK6D#VjV04#$AX+;<f5C1aW|%H=@?(24KI^y=PS<ED8?J?(oLVJw-((9h}Jr50<jtjrSaf~@2{pzr>I'
        b'WrZQCpT`zoL*b{e#pn0TKD_v=J&@HG9CLp!lDk>GyTZh?k?rKRK}}6BVkKGyd+y}>nYiNu#{~2i6=sX4`wr4ipKz8RYxVDSgJst7'
        b'l>R$-KdkJjL8OG;BW0oo*jP61*oEnD_mIhD<D|$J2yJt?oBaZ3!z6194bw|Z>fUl6M!R-N(b@>HehB(p!?<6ECP{GLJ5$iU{?-+L'
        b'GO2&12RsF@Lg+pu+>ZA87CXi`=1xz`l^&=EIfp%W=OSUhSj`3<DIIh>W!`gl+ng%*7uBWTjy9pQRM2@2tB&w@(zd+V?Va~<t92z1'
        b'u~FJetsI)rKMPd}D9FIYS2)AG6p)woNJT2uFQK~i^i0?7Y!6vjrtn>Wp*0@zc!&&hCs+H>{Ez4PZm%^aW>5T{*}wNZ(M`_teuJ~p'
        b'h!32&BXY{~Ue9GJgO#RTwkD&_u`*4Je)xHsd&p3LX7eBxFs#YGV;sgb_8^loGtC9zqa3EUbQ``97>KmkJlw%>rT~!jI+t?xAnp)O'
        b'k&#V7bsLl&5e~r=3o>=Gr^vb(RTjj`&0(5KWfI^`OzMuQ$Oz4PWk>mGY27-6|HCAz+dDm3^Zm6WMVGCM#cy(0UxhLj(hN^R-h}uX'
        b'8lo$dzJW=-6`1r;heF&xsjull{CK{nDDUBoVqX>XMI8)QwJ;c9Ss7p!iob{4HD0%!mv9ZTnu>dfjQOV4Ner24)yPCE!1g4@XXPOa'
        b'><?JhZe(*^LdiT8-H^baQeObcbdI+sfeKW}F(|~h1xq@Cn>J!Fx`pGWvy+yXLnzteUz35IX>fBpWH=1i9!rm5+j3v^Bow>>S$Mu@'
        b'q2Ns$6o`f=;WI949NB$;Km#YxaFnMZujf}9mH`cm9J?oZ5;mxT1aTp@AraN{EgpH@Z;(>~ImNV-ujdA2k~$toWo+Q>&du0{JXFSB'
        b'KG`F`NtOV~e&^UWT}Cx3<8f3?$0lsUK`6;lHVI}ZnE^JaC!+^a|C)4e4{whe#g9#r8PnVjhwL8oStii{$^$|Gu-IXS{0$y#8a4}H'
        b'_d6b%gaL6H5(JP3#4Er+G>{7DeNn`8gs8`5H4qtkv2pS;#Hn@PsepzA>96g3xBD`}FgQ{skuPT8NzJ;K{)cWB#U_dkllpMfP5}3e'
        b'bYr^xhHcAy36qu|%c|b&@&=yRvMqAE`&Qr5DR-($If1p*c6sL+8`O0J%7#SW3wIIQe(s*G_?7OWJd<M%ln15z^VEOSO=KiF!Vv6-'
        b'd$4~2EZLzzu-Ce#VV3}w>X?aOL-+7L1K1Kr;H3VsdysPg`Mp>)X#mzEOVE)1vFEF<|Kk2ffRbjqdlz#7jv9ET|IfYDA9TA=!=(Fe'
        b'-K|iXMo^oR5!1<<f%c`28+W1nce<M!Ro=Wz@k@6x>)*Qxd{H*k9L>B0)O|RWP%K`4_gub^rk8ivsDs^PsM)qW$J71fC*8Crb2}}g'
        b'^D}7}?dSmd==ylIrBzhb+>QPlSPdW+pgw7LdaMHM9!#SN?TnW<(wAs>cwX#=x2n;euL$jUM)UsEhG_BpyBJm8-A)-==}gZ%-KFE2'
        b'v?&<Hy|#zEbf&IR=Cx%O2|lja2NpU>>kJ@T_k%@867(liX174KaJNoXtp8KDf#_F0C082dHY$~+9xxo8%C>;hn+B$FwnbI?Z*X|Q'
        b'`L<EXU>oYzs5a?@ws$ytq8xw_)K_&|^<Cg8>((Go8GvcYa;vplw@_7?E!3@%Z%UM90}pcw1M+a+Jgly9D&Ymw)E$h<={C?g%BO@y'
        b'=&0R8Yxn)mpceFng5S7MzoxsL&S_O=(g|}sJG)h<WG{8(8>UKcy1hDDovDJV<z?!#y0d5)(Gasf;d}#kyzWvapo{-kq`WYklhSR_'
        b'<aqOQ4BO`F)4Pk*5ATv{WT6egkbzf|(_-tUx6NsH|B=LBYNYcrnZ8c+FJcgE7&<dY-;H*{*fLE=IlZCVtj_GuS6FjFpDs%}B+dWp'
        b'RMfk^i+7L-v#Q$$!`>p9!Ma?zTdt4ob|$j$sSUOYx|#@E%rdkFAi@!Q*PzbSEd=*=nSOb<i&_S5XNv5=F<tJ{r8{(b;Uzye7pl;u'
        b'=@06*L*eNk8>nU0OP#t$qf5uL6Ln_Fz*5VySIf*+gUz~PUty3wsN1D}z?S!b%eq2;U$>cBrdx;zsW___b(12S+GNf%*{sW%k2;}5'
        b')|#2LD@Z@pWmc!Kc`0UVruBFy<Y=>+mhTMG-|lj$Q*C*vE~`oZ1K?yX{{by@@TybmJ`#6C_~uO#M5_KsC-47*sN<$ZclGBxbMut{'
        b'5+*-|x%b=L=m^^62vVf8>|P=Q<5Za;tb1uHVY7Jmot(dR8mQ%Fs|gqYC7Z1)z;<S8I&IW))(SKt>R9UvM<=pTv2G{?`V*<Z7M>Lk'
        b'bNbH_Js;%X=T+;_52p7JJpn+EPVf8;J;8VN=elg_%%mN1f=JObzeYKN?y^*>OI~Qt7M5OTskG)3vh2rHcAd~gC71pO#JZUm<)U{u'
        b'kadvk?S9Grrt8T+cm5*T+j+@;va!oA+0aHH+(@#miI=HFknc;|g`k;17%V07oVU81`2}IAZv=oFR9RW9JfTpsirh8yk<NI{k^p|;'
        b'&-Nr$c5=0jM#l^v!RdG2S843;(_#5Lr=m8C7u~UB%%GfI$-zlAA_CVD%O0R!=`y_Yey%xn;g9N=Ed{vmK}>J&A_zTUTtItP#l9xj'
        b'@96^RUT(u3zr!d;7oDfKvR!mcW<WRYGh#Wfcae&0v&^zkgp9V_2(88T&imVJKgQsug_x~LvW-@)-kq%~wiJ<I%&pxTNIeB9w6++U'
        b'1~-;syHsi!src4trV^ImYoDG$J>Erz(lk!DUj$`Bz0d`HK@}s@(JJNTz?{upv}S3ALVR)7Rs6YxXB-8n!zjncs6TY+BRUEEfnVF_'
        b';GJY!0XXSC&VWZLSC8ony8QD@gz*8#8MN0yF=`q^eiWT)JNmaxeBT6A0#B?ssDJDi<V0$Dm+ut!#~-pm&E{qL{>G6C)7OyhP%v()'
        b'nF9S=+N0w&Ftxagro{zxFiXwv2s8cl4y_f@w7etO@%kO8yMAHUmjk$?9;4L>W@>&+FfKlTY1f#8#j$<3&vggnG3f`~G51bMA1-!b'
        b'1TkOVcjedm{OOJY4?y2C91~1vgY{GwVGMw#F&};2PZ|{kDsw(fC(wlgD!dEywfmsRYfV>9sG+>%&;o^)z*DU1E*g)5(ZyoMn1Rmh'
        b'FjP%yW|xbaPZ(3Q>u6d)7==_|*W!N_1_N)_Dsjil*z9p!e0#!6Cuw#=PcbdIOW;Y=cUO{a%BNH`9RPh5v_D$z6+sfvZu1F{Ka1fL'
        b'>UL)i-37S-x?lT2qZ7tdYHpVbf>vNe!tAFtEVY;vLk3&IB51c!KiC-ycGBzEo>p93jM47j#U|sv=P*bb`&2a5)0rGxkQb%@H?()E'
        b'L7k1M_9w4Sas@$Fl%z|w29#L>2o3dhXVQ<juN|ZDBeQKYfiqERZLZc3yBo&AJNnN%b9|jNk!BVpkjiYjjTEUY)sSqyXw#!2;3vek'
        b'(E=E>RBKd_;o7Gk16BtV;f_{}`nZ$MTST4dT&zi^*H+`c3s};7xbGN@I64T5KZFlGf`5cj$2&p4(ZTl{6wzd;4vGQpR5z;yK&<}h'
        b'E1+A^o@Q$T^-gCpUXY;%P6dqPjyEQ93a%g<AauI*#iJ8BhE6{Rse_$fcl~j;(W6Oy5GZ!Ng;nmADdSeK_-3Uf6U-C~q0dj5ih9eJ'
        b'GJ#fQ1rvAxkr7}jL1sLy5rE{GiaA<CC~X*t$1TjaN^I18twjrn7-15Mp8#8azOvyz+Hg8A!SP4bM<9Ig`(#DOS&$?`Bm_xu>;O2V'
        b'OSU8{2qM5S!BK}gvx9jh8;q&X`ksUM<xk-b2d96$)1Xemhzrp2J{B@xOuLuvYsG!#T#-7Hdb2Zj57@X91aW`%dn!yd*d(rdCG;@F'
        b'ufX~erV>8(1xz63-^5L8Cn(hwf>^}=vqFsVHB3O7>^c>Z{&0RpC?R+l(jPY9z828si)>#AAZRv4(<Y4#N<BK+>T8FQKl>CK@^iks'
        b'(weu@-*?1?9D?lXT+8CVB@;P2JF{)FwR@#~(Nl|szW$$qb7uAO_t)T#*C!8%2qH;8^*!G==b^s2cQT-8v3^M>_4D_?CC<T4kU?Iz'
        b'0BEaYe?wb2qRsq;fDERWMFWgprlIC{Lfh}jizo2=$skNO*!;FC|M}3viMZ+cNi)5?BGmNkB*Ymm^EJwdrZY5pRcFp4oj|tf?;P;X'
        b'%vTmjgY2MBJh>92bS1>vmPK#(*YN?qUE?kp0x^T}i0OA6mUEFO_@0=VEE733SEf0#oLjtRtzzfm7m-XyV~ZEARp8=PTu$5f_at+k'
        b'0pG9#o9PR{48ixC-{Fvan(r^|gSS}7!#o%o%*^+bq3CVgAbt>h*=9Zi#RMrr>sHW!Y+o%0Y_I^Q?K<=QJ{_k&^uO@7ua?`II6xJH'
        b'!>zCSe%dGQ!NnR*zyE)sZvynU5xQxBBSoa?4UyTpgp4>XD!sdDhbpLG%WBX|848@bOfA6#^WF%;_MfeM1Fg7oS(j8fz9)=ScDTQd'
        b'<sG5oIg`}KSJ0}-&87(Ciz?Hw^`7hvI;id&61x5FMoCbKrDUQa9PBLpi7U{$8JnrjD`pxiy_rqxK)+Ax>DDU-e6!`LnN%};L|GKU'
        b')I0Do*K#Zb)WV+pC#l9O20E}njhohB1&O%BiWMj}=-KZLYBBnsFaeVCK@V;+WBQFyXWczHl<Twn9BGd2f#E%sFzTopP$N3(sqeK#'
        b'prX-F^>_h{NAFDPtFGi!T%ms<=`UA6{d#dNWxrx@gUSp6#p0&hKv@AvI<+eMK_NPX;Q1@rW;s|Ryor*aERwghUa6~{VHuR=-<%|i'
        b'9dn?gc>Z#wuXWOET_XO313o&=a%2X$3@kpUYU`Da#Eut3gA$Y0&QRbP1Wr{P=LgvgV4vgE|Hs<9hc$Jji^Kbt5R$FkArKJJ?!7~}'
        b'MAT$Q1+8t9fDuvKBo@51J%@mxPCMryT5($2Nn$6W#VN$;co{vD#8NLU6*Ilq3ugdZqza12MG-8urJd<*thH66lHa>_(9WFieE)pE'
        b'?|FE_UTd%YuC?Cv-q$UH4VNnSlxw63tTI_cOv1PVj0k(t4s}Dqr4sxj=v^f_3B1ZB?1tY>05C<$?EdlY|AbEFMip5Ulz8?g_+l}j'
        b'Zx2Td)$rbQSD%}tuSGB(grx6^_NzNtk9n`$K+Fxg<r%`-6q&zH0jT2&J_YP~--~c_KjnE_h65u`O2ZKYcWGH^M}qgjO$Q9Y2w^qe'
        b'MCiRWbaxJ&Xj^(GW1aQYh<)~_+_X=@Bq|}~f@JbRNwHDy`VR`|+u3<Zucufr&R3(^z7l6v+McQ>+CXft+Cxa+#fnM|8HKdk(faKW'
        b'Y3tiu^t_&Lz08*GDEe}G%H{NA2AC4cb%R<=Nl!-h8h`Q&x}M$>YI%aK-!bAEr`CO?*36(S&hekJ4!~2QqO$7TxZz5rr)3!_o%!rW'
        b'az3WuOWJO?Wnm@S`RdnVpze+zQ!MF!B&=(ZL6d%!kpAbWJ@(VJ(0grum4}etyg^E4*;|J0i3;z+n<jr)8<!nDHJg6h?_a-aX5u>l'
        b'V*ysKCfep>X=#M?$(!kwa_{3e0Xo<b%Wu-Y1EI?LGj~#Yygr0?L&s21qbSm0UdK&9G|x+FO6oiBJh8rQ+l^s4xH)a#-7tK4$*%Z?'
        b'Rt=wDD%sC2TS6175{S0Fn1`DNq(LX{BNWSuckZyI?_e_--Z}l(v1%c8r2S6HwYI7o{K*KiNLFCnxl25efshqsdGoT7Ujx2+xEF@_'
        b'ZrnlSsDFp^_%gmV%oeZzc@~{s7(4ROow+Z1S3z63k1x^lef)gqu}dih+haCVPgg8mx`YQh9$u<EusaoS8){j`V96@!qbnX4|7+lv'
        b'oQEl@0NX&8Z5@%;mSroRP|d^8%0F)Vkb{?YB($k+M%ND?OYWHHJ#o9$pA>8{xr>I-Vx0q*fYj2T(U3$Am~Cng#=Uh(q&A&BaEUa>'
        b'!}vH)UMdz1Q2X9XbjYEdpZ<zG)WXo)w8i7pE84i7m*{zw(C%%Qf+v2aKiDVPu(eoGxOB<Cl_$mx|4!N3VgmNrRzv1vRtAQoeCPct'
        b'X)N>x-bH)U-D29d9X%4c@C&l{-JKKQCCcvXZed*8U8D?)z9bi6V|}fQ{H*&i3LaofHP)|yCp%Pa=kL(g=cOCA@JRmhD#>_~n2BIZ'
        b'a>W{=C__x_`1rQ<Mfip!9&HmZ5#qUN<)A$ujBq8FXe-DQd*P+I%b%A5pmPbNWG3)Fd;?#C7~VPBW`u8cCVva<s@Vu{8BE^xb3`L~'
        b'lqANpm|P>#z;D}4&?Apt%2}dbH&DKVu&$1b)ZbZ5c)z)h0^ZJP(v?V%aMOLINj~QTzm6?&3f343**(*My4x_yIpY$YxJz1F)?A#9'
        b'&ZXj=4-6)Nbg7B6-XeMDG(?Al_lF2iR(HhlrAeIelE7z`t0oJ?8!@HO_u1UHgLkDztoFa|Wc|U~0hNR2rqjN|6K!*m?Uk`4>PKw7'
        b'!D%izI1rpOxJ!c$=k#CX&NH{{lP>X+YIV0=Kp_`n$&pbcVOa1-O>7!la^wz*x$sO0Hyy=XcroU3<WtD;a5;^TBe47t4G4J@h!H(j'
        b'cm>6L+ykI<#Sb5>n2m~gICC*efo3h{Q6R<{9s(oQ#ZtCt^7tSmecZ$FT*A#ZWhz+>s>}Jqkp3=A!B6n^)liqZd#dw`p&WIZityHB'
        b'+TY)yXLxH+_k%am6A15a)cHz{ginXwOABsrUknMnEKL<t_R^iKSEZioAh|ZxFC}Bjw%y6flfH1>1H7_P3B1Bx9QwsZoOTOL1Z(?s'
        b'F7{G-H6d-gZtos){(f+YWR}euHc7-Xi8nM7!9<A9@i&YTqlpxsl{ZYp6k1IaSlT%lUzNmA6X#97Wx}UGMonB>;w_eZ3dzHSTPIe_'
        b'c<uamEQB}i7PuRwF;Y@S6-N!L#dk_$Vlb)rTyO_<Z-O!K<q*1iMP)9~m=_w&i*n76E-^25ZyiK@KRjfAeP{{3I2V7^h%eIM3src5'
        b'qeNogKg10TkrK-i3r1RS6TZ;?@DR9!_CF6fN@DGMhZtqpAxTkL2#tj_S}651c-_Gv+nR8(Qdi9DijBH^ueiD)o|vo_2=3#dK=Y7_'
        b'AZ$9c-U|w-2vU3?RRkqIP%)*;48I$)|7J)<Dm0Qs+<QZ;5_pJZIk}27A$2X8!2<tUqznsAhfb3_E7~0fFF<;tXBPAYsS1fMq?v`*'
        b't(K#1LhlX{+<y!qi>6c#y3`&V0wXrF{zR#QTLa>8KKEbHF$K48XiKTgz7l#q4ZL3PgiZKU8<-deuc%3A>rim74B3+hmsg^lNs9D!'
        b'3U0*^B7&EPNQ;D9I+VCh1`ep<r6Dp`hC*@MhN7+%&*cJxg00CtGDMRkF`bJY6z*{qLs)eYZ{sZiG~$nhH3w0f13$d<9ATXa&j;;y'
        b'E(*s}(Tdtx%QXUi$WgAln|72Ef*%)(mKnaf7`0mja#FUGu(n<|7>B?TJW)niQ!zTRvUGm>Gqdf}hTIPg36d02k^^>3M{Zr#5Llib'
        b'$s~r+3Haf)6Nl9KF~V^@0$xSN5Ew2usG&Dg?Dr43<A><^P{=2lq>@dkIKXb$mZGStDpHb?TrxkiN>!$j&4jUmXHPqls?bP#%n$-K'
        b'6Z$L$nH^<Ccjm5aYxr5v%r83rbA92Rlo{5;KZ6i_X*1gIR_HmtNIWt|Bg04uDI8}(cp?bd8WMv?>BR`9zIiiR5lC9;7a&(}4mu5}'
        b'uf^b!m*y{9BJ6)CJ0W?g@mIorUG^)4*MbTAXTU?-G)xE%WWTb~@a-TJPyC6n=3(4x7r~VgM*^`|+w|)^nPT{95X`s^i~Wm1(Gbyb'
        b'y@Q5N2ko&i&Y8a$vu6ek@k2t1&I(S*eg~={9b0M?g#G#12{yyI!MQUtmMrxV)-odfZNmEkmNE}g-Z&gm)^w~K-W<kgsr1EB`230N'
        b'1c|W!+3Z)^gg0KDGm}oFrTSHyi}mZB?+gmoqk^>&fqf-G^n?YKH2ZU+?f&bABZIWGB)8FdY*0wck6AZ|tGuX@&aw$%y(nU&w}0kd'
        b'8`M~I+}uGF2r19Ul*wFR5Spv9WM+ft>y4n*kd5AR5j8(*-3>#bc3idY{5fR=we@Fgu6Ai0(bgNu*jz*$ao`{E{@Y6lAlU2N077C0'
        b'!Omo|p~SYIJ<8Q3+#JvXo4#p0#(?Bzr=ay_pa-I1N>L*J|E3H!4E~EUFkSrLmBD`u-ctsk33ir@=Nbli9*Z{G`{d8un!&kJF&Z~3'
        b'm&jfvA*5g6#Y|XbF%-wcuTZ4g#5o6fVx>BWbN@C7#Z<&(4Uvs0!Gpe^#Xx4wA}!h6vO&Wl^w$2zK{9tT2mvzpevklB_Lq7iLg2UA'
        b'Fy1jl`d`o@cp>mYi629Fqeg`{U2}Lk5tMMHAFHTc4_e*l6guLp2X7gk9}L6|rqKGou<i#3#j~xaaSsmKmkzc9><*?Qr7eO(t=u;Q'
        b'4t~Mj-(j{r<uImK@Nz9-{Q>WIhUY!3R>J4b<-Q%TPrqvbFflwiw<E62a}%sO!#fwFVMVkI!RQ5-J>Y_-N-yC;z+J-S!n3z8Vl9k-'
        b'd@1_5rvydtjU~=$Fx-w`hTEp6^bfGLEal*gFx<Sd(TGA$9!{{a)TXzGd2}5SWNdl{#;ogZ>gk`r=7C{tzMJ7V@+rV*6q61v2Xgo$'
        b'4+G%>5b*n5V!nra0F`V&VStJZrH^|M#@g{Z3V#D%I)F|@vjbXW|L&sAsI(zsd)WT&fJj%fA!*7{+P}I8L<M!}?^Z2<q2Qvpk&Ej5'
        b'r$i&2t31+F0V2i1fkC*}!pR2hmo9E3HeIdY^_6#L!`5E7=t$3ZIP+=}q&Mz_xV%=sUOc|{5%<vnbUbd`MS21+`KGlY!kYy?A=Se@'
        b'!rPO$4HtvNdpwut&)i%aWO${z;(cW^&ouIE2uS>}GJ38eZ&#~xp5n;C9H>^$>jm(U!I%+BM({f+l=O+8z(CA};oy#46s`9eXpGXZ'
        b'wh6a*{9q-12y_G5`>P3Hi6+d5b^x#PFxt`E7C+mz=qI%B&uG08;SOGm`H7IGVL^UY{S*l}N!Cw)2CBmJUkfFRiZqz_#to#+vM!Ek'
        b'GyI@)??p%J+~Go{t;n_Z_ZNj$y-GrXoOa-c=46Ag_k64uKAsC1Ak62?+E$fIQkXqikgh~JB`;Zhj;U--K{tGC(8LgxAB&IWq?BNU'
        b'FvEly5@<BO{>R%{@lwrCXtT5m8e;uSG|qL-IRiFn7$Z=GT57<?W=D$e&5jg51;cD~RZu{ORm#S4rlOqPbgZ@l4AkjRk4wy`b=}=A'
        b'w}El30y@p9Jd$2q#Q+=+5L&s?RmBunAvuH&1E~TEdaz=RvUnBiYNje*kNAMfI+PXV%-Y8;HUqR~$|fd((AG{GfE+aEQqGv#m1`GY'
        b'Y;I#~iz$7%vZ8}2?qFN(tDBpzHMg2+b#aHjxtVHp8lCwUE7S7RuM^VeG5gw!M}K?KR>cHV7c0y2Q|K{!?ZJytLk0{Sb@KNPX-ZA6'
        b'ec?q?niEw~q&3I+;|1HS@ZQf2GcNLgUS6rwXb2*z35xkJN#?LDSWGz_jAWT^9T+amfGJgH^MqZAx?*XVi75cJsz;XO1n%E2-ZgCH'
        b'+KacdQoYUB&;j-&T0DEthy;VO)Lbw!cUCE00Jb9-UTm72G(TbrhU*`gMdFY6-)D=(^|o#bu|ssNatUV&9T{zW8+i?&BtTAkM5%FC'
        b'NjQ$&66d$34~yI@=6o7uZ_pVa7euv@4y*u7?hxm5ZAeu-fJ!z*V5}fnF$<{;kP9GiibW=eL9_pT09YN}tB54k!=OAMY0@g~jTb;|'
        b'K)(I6fvD!t->n+dhAlY^ws92o>6eLOW!Nw{pdoWa%*p_>kOOGNv|$ss!X0xF7{rzn*7G`y3iGXc8(t6{3kx{?hxC{Z@=%76%*8=_'
        b'gRA$(D4mEHbxXj<3238hRiI)cyK_rS+40+1Go&TgJbiejjP)IPxweX_%x5d5DMc~zB9b<|Kj8RS4}7>{2`Rw=E=DDbb*Ts(tYao2'
        b'IcgWz^RrN+<l(WZfi6&6?xvtL3>u@<v2g|Hj<WmF&_S=kN9HaK1WR*lJUox_oV7c`ogRQ3Oe8F8LWJuZ_+<+RFy+aJR9tOKXLoZ#'
        b'<%vkuljGg~0a9uli=A1G;JX(kj<%hS7`6`3vp`FLZ@o-Gl13HDq7u1A;rQ*MqEYDy1ZQulyKcZp7&L@{AQ*KFuQOT<8jHX^JK!Kz'
        b'b|gsuA=3~BP|fg0Mcl8kptA4`MbxD)*0~3`{~QoQtU4xMM_Oj7EZNrB(TvUDV|j1ivufI|UE}HpmJw*0Udw=EXf3?voP2>K4K{Vu'
        b'|5a#60d0x~KkP5pxfKIoIqWsM*9_bZ3K~eL7Ci{u5_q|CZz&mV7KWPjFYgx)IF6hFMI#W19t8{Q-E;?ubL*`;U=xP#Al02Nu`;9R'
        b'Ax$D3KMFp-RdO2xciiC=ek}pHFP%J!VIV%FDexaOz}k%iNMn`cdmW=#PRy?f%kfjDH9Lw;>uc8QeP}MXX!c(7)Pa<m&_{W}mUwsn'
        b'd9+DRk|j`iym=Zr0awPSs`)r6n@R~vwd2TdYoq#6gLD!1j|)u{+scB1t52b7lH1s8LJw|9H7!#uAo4Xi#^rGf_}PMV;x&v%_HAA$'
        b'eSX?RnfeyapZfV{ex~9BI)Nq{wVRs=?r-OVEv5|LFo8*9pzT^4_r>{xg&CD%c&g@4f%yX|wEGBZo`=i2zIrwnx!~X*+57RL#Hv@a'
        b'Ksj~u^D+O|t^DE;Kd-B6z2AS$dY!_!Z!QFRd(B~oZnFD}3rOIU*tx)YTIL{<=tM=~KACOj<|ku)+|;SE+VmZ4A+zNbLb?IVSe_CK'
        b'y{_e%Ek2@cJ;r@;;h+PQ_y~5p;;<fcc8Hti_pkTi9|fHj{?urLtoFbTcH@qUJ&e!!P$f6@c5Frr%f^?-WpXE>30T>kTRzSLQpOLu'
        b'eU2I#GTd}zV$7oSx*gyQ!Z%RT@Yf4GKhMEs@};vf&#Ir1c)00Eo9U^>zbHMNML6=Qel`d_Wa);E{M9eoRX*+^WLm-4WGY=_W3&3i'
        b'<%tav_ZR1*8;sYZ|A#)S`Bjs|JrUu7=d$dtURYWp<r*$zlw>AwuU`<jso;rLtH^o!v?QWUgXK7A1)Ag6>{GD2cGR-#-vwOE!1OO|'
        b'cInr@yMt&mpfHICg^7arp^P}8m6@G$$T#xn?L!_ACV*6sCpoi`L@6XmN+lt<N6&-5VI#sA{uD`)8yGFuec>P(6&6TM91Xi)I4|xo'
        b'j*1&3K0r!wFJ2%mvpLTN4{GCVm5jo0FbT>~6|q=M2_e<s+;bOv;#+b7W#vIi03HNxI-r70qu807!M~Qi7I8QqayTu|OQf$xc;`br'
        b'JQCJG1oea0km^c|_hXsHk)6`$bfYwCVsO(zPqBKy_@^)ipr??h^1%Nx1`cry?()a#r6tHz7L==b6d6N?@n0C$Mxo^zEG1gSV3;%('
        b'qN(0Ze?hiqAtP`C;0rQ96>eGwhOu6JEgboW=dNXZH|JBAXc>zOIxJ$&U+=<r$S=aE)hLA{zeVM>tOMQ5^T0pr$Eb2dnlT3%%~9nD'
        b'5JXekTr8?Wu(R##1>2aN{jmM(e$lN$n$eV@v?pJHj@JIGa%A<_+({SgJ^iabCmb2Gm)DW9Iri8Kn17E?n|)xyvZFur2g|Yn6Gf*e'
        b';3)0*+rUn9FH|S_SFk&G5#BDW?t}h-=7J~F<F97aHw^A${ho})>VpD3uG^XGeybmCnrxrh&E?V)8=Lfvjq9UF$2hpTd+UAN+(k+D'
        b'8|QZ(Bcx}scP<cZ7qPh`OJ@__esQklC!#F_vtK#CEFrB7nYi}Oe&|clkFsN*Ia+cWm+WYg*e{(AYP0L9+xEfpha}o6>A}y`1z7#Y'
        b'+p|A2^q)T{5j3`CD{_`(Cp>QWpkL6;RvQT*ONV%eD^Q>ii!D_t?LVFeIc2M6?Y-wc&MaZx8wPKG;KX@{X0dvnFf74plC8a0(eB*<'
        b'qIdU9^eY6h>^+3^1UB;UZD?%vPw4n@!^Z$=YKVLTYIrw6dp@bX?%*<Q{kWR1QDx*C%a$)o5a!8*1<`|6Kq>{DW_!tbcj&y3a39*g'
        b'S$Lm-95bWdMs50BFEBQ6k2n*M!lvFUcL#3M+jre1Vfe1QwCS0yyRV=A2~417F$HEAill-8W<yhR0x$%a{X7fMfdc)7@G;^B8!Gc#'
        b'c&=Tpv^hZ9<$&!BJj9FS$BK)R_=X5PAb)-)wCF*w$B<tqy7Xi2ANO#r=+e8yBr?nv^n0R)*>mTC_FVr;d+(O0xuSlaXKK0uIqh}l'
        b'Cxl|LgUdmO*w>xsxv7R#=exBwzI6Jc%JhANbTif;LMw6?m84H1q;8BRc;_Tebw0<E;Sih?d1ngu_<5dJ)|6z#@jMAH153|$cfJd5'
        b'6v&A#&E{5}p6zBsEl<~1#T6B#)Mws)Vum;T!~ccIVA*R`AkI2QK>!I_pf#M##YP^H2DOqFtbf&I31>dv%Fjj=A;ap|jq|pQ2EOY%'
        b'_-tB%!k0N)J)zU%%(c#nG)T(!+;XdcRc5P?5kYRMPmVQ6e9ndFW-CZ>3q1;KXOgn6;Cw5WRolVVO*!A{%<?RFLz{HlnifHXd8;3t'
        b'W0x7}2A0a%GU@&;56)kdzhx3(of-*g3mm;TrZ^dtXibe_?Man1BU0aY%bSMer6>AUcG7*WkDe%+LQ`lN6vd96EBi!cofPr(;@#Tp'
        b'R_*+dOdFJ?)}K__-v+6m3QX;H520$U@ezzpa1?wcXqdpU{?Mz4xymj`q%$L!;Zk2tsrp=}kIUNfcLH(@xBHjvNCWFkh@f?J@ARQ1'
        b'0lOKSD(rJ+iD5<srr%@#Tfb12W6g{hzUt2*bCyVNMHYF03cU01MLy|oq2cHdfzmj`rG9{tp(4#xd7K=yb(X{?dfvQddJ4VF(L{iu'
        b'v^?Oh=@ZWrz<6_fQPq=BE=umGAeS}2GM?-24-%#_<t_C#Odw2Ld%s}GGMwnQKiAKbSs)z1zyd1b=dnvSnz#;-BtT<{`W%YQpwd+n'
        b'fOjj!2uFoT8t5?3!uuK&W%&}Wr9T)qjeDy<Xio|{Qqd~HVbcCVKU!GBt9a#VA2&ycdQ>3>+}w)ikTL;}Ds<!y3dB?~Y!&Dm7n-3#'
        b'%0?f}SXV0sVxp<1e}w;_Za{&8#(@kVVgLeM-*~qOFuO}MXCR448Rh&I{ANf3L9^+IH!DSEuRsC;`C^r#F9ykI2(MD~#eAZ!fnKil'
        b'BIOe0_X<(ntbL>}s%|Pob+h(`{(I`C;x5adxco3LVQS*)Q>5Ip{Q@`7!_60$ds%&4zJpsJl*}>M`#dF9L1Xom%yyJacMqVEV?*MZ'
        b'TqIi9^mIR31SJXbv&w!$A}vuS=T`NDzI?o2C?UcA@`xA({rw)}67_c!q0zwBnEw6+pV5rF_!Lus&%%GgXW_r%b4;P%#b=?2&q6k;'
        b'yAd+~Z`8NG{}=Tg?)?|_t?U1v>f1Rts=*JGa!1qq0~7ms#mX$2FR+D9tqz`i%zdU8ozbRqU+at7kgG}*+@yX7k-{<k4vS1&Mxy4D'
        b'`n&OuNJ8IY@5dVV9P}X)U2+RZ{@vBwQDuKX(x0*@bSmTIVfP0J9y+mOxG#EQM?LC%R`wbN7Xx4?aku&$mRP9hs}dDQ_S4%O#ANPg'
        b'$diL?5p{mn+B<za%Vdu9B<@O|qePVv<M3yoQ1wm}R+oN_Is7S*Y@3RbU<8!=&~{e)mA<+!`Z5XyNp&kXjaGQx7~bZg6NLrq8x%sv'
        b'=#av7V28ecb7pMUHs;-31lW^?FZx<D<8sL6c53zy;0iq*ZXQ(njZ7Dc6so%e?(`<YJBWJ%FKiJAYZ96AH}D+18;JB{gw=<mTIUea'
        b'c>h`g+0n}huB$KShuH*I)yEU~x0N0)uO><Q6lwpYk8A1^{Oxmip%-^(O&e9qiDlqSRhHn65@NOh*tmX~kiJVA{=3iNFX1(hp#GJR'
        b'Xx(|7%;C2zjU&8ANbR(^dn@jP+@Zd%!|-3564#O3#$N-ch^9ljNiQ9)UvP^@%hTtPgrb|M5Phgg-Xpg`j%yR+rpna=Z#KyT@Ai#6'
        b'ddt1Hk0es7Wn`{?>1v5XD|M9OTUHzGJNrCuMsm=pa<e7%vl(=B%+qLa41eqk`CZF)1kU#vw)Uma?}r?vl=~qx<o0cSIg+L8QrwPS'
        b'@iRkBUx-h4sHO$^G{XyhjwPuhHz~Ud3e8`4zuVmxE#&D7k|x83zF=;aVR~;!g^qn0IU0r>fuz)*lSiBT0<OMRf4p0ZDlt6OckiT^'
        b'`fur?ZCHp$N4?Y!&|F!c;r`xMp6ON<hX{R;S8C(OaVz@-E-QnGE{&8vKPs-zLD58;i`w*!LyRW6UP4?I<@{=(RU=!Cj3?l`YSDNC'
        b'zN;2XJcFXz)eNM-c#4L!QTgeR5shk#A6Od250JqGrjKYEL_Y$y_kn33o-ztjHOM^xk_Uw%3zaUO0gV&_NxDKAY>4<F>0pDeM;ckG'
        b'RpfksArlb#K!P-j!W1QM_dv3ndl;UB+-%cSBvbr0DxmAr7b^WCz(o=i+Txj_xE&i~=;Vruc*lu5Hr-~2QVj*b@2`D@VRy4WyE-kK'
        b'kXlE1@=Mol2HpJtT@drzOrs9}WHiI&!~}m@b{twC$H@^f>v>lWu`Et-Cg$)Ng2S04I4AJV<WS2K^d4=FLOKzAFn>9kTL@w4#>WN!'
        b'6KFmrA!0Z6@qQc({E>;b4A*-%N`!MbpPN;k@SEcRc%ydN%%k)Be)IYAAGe-Mp&JPI4N*WP(h~pD9S$Iq*Ls==L9>W{e`hJthDXp{'
        b'D}uiQ)f0e+XQ2}7?NKn`f__E)3`MZz>9T}dM+KlE2A<tth|m(a3%xYyM@!Ns^4)kPm$JOo!A$~n{+n*0Rli)rbCbP0F+P1h9V4`k'
        b'(h1vR^uI$sa@7t6-}){1o>e;t@8!`Tz6|<XmZ>m&+{@$39ArFNYcL3=UScJe#2-&`lu9d0V;tNBflFS_&lW}~rmbhx{!EV#{|GE9'
        b'UNXrcnapM~XqoU^y&g&I-t&7y*(DQHF}b8<CUS|fah3fzACpJ_4%sa8^S~^j6X4OoO+)dT?|RkGV4)VKfzUoiIEXxTecXvsLb?E}'
        b'2e*bxf`$mr6sX+coQPWCoGcJ|4(Fuo(r4XY_XfGiu4AmnSy2DqGYn7mfLm_UgjozN5J2%SJ!W{h7aaJYW+rK#tTGp9Kb&D$@;{3)'
        b'm|TNTHk|Ke*<_nhoRwq<uLhlRWq6=RMW!;0&J+lvbFBByFz9=OrBlleQ%7yRfya8we!dUdj>agTsNW~yiM;HRWNvDY3Qq>PgyA}q'
        b'AAMN1YX-;n21}-nyha_h^aiZGBUkSWtnQ6=koUK<I@fYycHA#`E}MP}EgO7x6g9)!iI)8x?S<B{q!_-u5Mi)nZ+}Fr{E2!K(e@28'
        b'bGgTQMJfINM%Ra>3nHAfClthZei8ctQ?w8l$!e2(S`RYATQ&jFmB|$Lod5>|60iR*%st#&sl|ZEfWTWfYJtSIA`;7(`5R59vCTe;'
        b'cEcLc#NjkN-Dns50^+e>kE$dFGFAw-FwlOLL}-caz1;FNY1WXj#_p4wP-g68|NAUyP9-HKF?l~}o=8f}@JyOh0;_tp+X?C8qgZ92'
        b'z;Ldo3iQc5yfUz`3V5(^lvmwX@0EnKGtlLen{N5%u!Ac=dbV8YxvVjCYi1l>+KX-ueIn;Uc>|GRsm~_Uf!^njj(n{Ar#)Y?-sqk$'
        b'?OV!@WU1$>fPZAcKhkR`eIo_J^a;}S0S+dJ$v`#oY=sdwg(x&X`~e=A(%TqfTm9I`r7%bIcFIHiJbF?vu(0fM*h>8aL(}_llh8cs'
        b'GVq{pAl}ZvAql=Sn%<8i+EPc+Tsib*DxMSIzU;|SRTB9*#;b9uJP$)Rjh+miH=9Wff5is(<3q9z%@8q_6u3NEvgKEL`^!B+|H@;9'
        b'f)>RqTAd5Kor^C!7hMHLco_ulLJ#-IRj%MNx2T(2{3PvaXFW$S*UOCS4drk(+xljtxt;NMu%3oUMT64S!T8@`>$Rl&qn^N-o)EYh'
        b'^4X!)Q;$yQz0B#}!>{V*AEkN^%FgcYX%%M;NptMTSpupE?$19aJ1~*({&1%<KYuXhV4x|c?6-8svmtI;kdv4Fn)U>-%Kf;jimj-)'
        b'wk0OM?u{N$4xS0A6`%n`HNr1X-Lfjf{diAZeUGr30)^wMRPqy2gKr`oQi0A0PAvlYkRfRxN8A**w<j2vD(%70vI!u$HzUIS8P?Y$'
        b'Xla8Ft#3^?#sFU1UPJ5j_dkL1>fz<H-XP+Rj0xp@7VkHKGUf8lfr-QuN#(pkC9#mPGtdEa&z-AHS61Tj6%{MNcc?VS2ikgo!|LS('
        b'_k54Q+dIyoeL5BAqWd-4{&J^MgOB)?{_JLtA9wgM{j$x>OeGkV_EqO>%TPGM;mkUaNLUZu0fQz7?5ZB2<dL@eJAuZY3L`k_3^W2f'
        b';ChMx_gBcYtIyqZXz=<!Dg85>^_4r&PMOEfRa8(+l~O;OsSu5T1K?G@a>uZ|hj-=)8oNV-8Js<i(nqAVcR&Cv>B)#I=hZwOFC1|p'
        b'^Vu8^0(TLqkNS(qX_(7aP$=|wnbj~AmF%W-VB=pI^O=mIABJLfRd?flRlmgj#{95f!hU03*WIvRl^FJ`x*PVZx*PUGzFN*$<PSdi'
        b'|KNwE_WVyj?Az{t@xxMj{@D++PwI)fVx%NT&@M_ZA@us<tDNp^Nl(jH=K{8#*|=#qjE43aF0}yOqSA`t<VRQZfSw@D(@a5d)fc)W'
        b'-QtYqG~1l8iIl@A9d-0<jx{1dCJ{E94H%2&68RPe%Db;c3mZ^jjeIjc4HV2#YY&qo*O*f^5^-&qc_E{egF12l9Ti3slF4C~lau%('
        b'Dv9~%13en^L=A3$HeiGtWITq+(ahu}R2ZNEWJV<iN!s1IspYM6DsxH`VSQ_KWagMG1i3ge<yK9y^z-ioJl=7{g;uAV<H0#dk%+rQ'
        b')q*m~5yS%b_1MM;FsXhJZy@SNh_=Y>GK0h*>EWu*g)|s~7I&XE9iVy7e0OyBIrak8NkVSfGD7-e1kBJpns7L$Jt(Q<^iLAre}E?7'
        b'{<9nW4?b>>uNP-isR~}-EININ*J9^_^io?W_nK}}GAo!dA4CaYIOHtA*sq7>Scog|KNPPIHUpCV&uy+;Fc(Bjc3eCZ<}((66M)Xl'
        b'{^*?h*>mEA%N!p!*CA4ICgZB0fRMraMMiEf(6S9tqJU`mZ6KpzF$1NZi8{d1)IA$mO!3@waDZ7G#e)M}2sF#sAQK#58<62celZ8A'
        b'Sj_w_Jfj%mQWQJ`LIx5>Q4!H+Mn}nJiqFVHe$d02ZOvi;u>(1@_O<7lc{D+9izXlFZbmCU9u~u#vrV5Un_EQ>dCfVr=%a&SJ6Nv%'
        b'oM;}k+E>>H2%eZ5bmn!$dH-;mQ+GFz(L0_3FPwAFKzM2U{cRtYmo|a$?zw$5{ahgHT-nq2d3Pe$$-<#yxIA~~wN2u@wyTQ@9k~O1'
        b'e`N?wY+H`p>f+H-0TVm}`*$c!6@Vgk(|XA0s!~3E4McKrG1XkIgp6XIEfKL+Y(p!i0Bgmf)$THhZbKgGp$T>Gq3FIm2MB=$@F8n6'
        b'i7|t`u_<xL0p7O&;))PhfM5akuceB2qhu}5np4k#C_vAC$^ytb4DJC-lCw;&D$QS?b!g_nE6nsYWSUIZPL$*|P$Ty6w*%bivndPd'
        b'WS+OUS0UuQp))AXW$H3W%L;6Ha!1J_(n_Es{BkTsn<IxTK~8T?_zrtwro*Y1-i~x@=F=%%UF(}94U{z&IbH`pQ?Eb)0WE&ZO`S8`'
        b'?9RB6xxb^Ed%YW7uM$U9feY;aR(pp!xS#izrY95DhcT}Itc8E1=A&T>?JwJJfjV}6i+T7&_1{K)+#FuH+Jd4uwZl|n2oPi({(v=g'
        b'QJXHocnqVX(S)uKSRkNHAs7pEmFNd-Z3VTd62<~j6(6uqUxoiLB0#<{D8(PJ?7gu-d%J)HEkMM8@Dd>6JoJ%|%Q1bxTELM@Q<}sp'
        b'OD%7rAPrD(G|6)hSU?mzlqeQ10x{K6{Ob`E!r6@=n47z6KR{$^6F({89yV`13m?L>DGds+jUQ5Iv-fcj=?{a5cDX1t^Z<mL<8fwz'
        b'`mh00p_BKZA`?4IffQ-w9t2L~IkSfopk#A1#j+G&!sncB5m(B9X7O+jwK@&FGso0SL6>Vy6tG{~oXomFH+_HgO<Lh=|ETt_n;UD_'
        b'4=zv~Yy9)(jtfWg(AfAUQnfoN^@2(6^=GeUsMQaT_b6A3Yr+8Cn=V}0uB`nN<J!t@`e1mk5^`(*#BSQ?+RAjj3n}*LoA9>TtAqj}'
        b'!0a)m@fCDSod;yYR>uDpDuUeNKQUnT)Ot`c*PoQ3HzQCIx(X#Ljw#U!ovna+0~9Xas`R}ciPi{%0oI%CJ!Rcf-C)DjB6mCs%9yq)'
        b'>t>t<lkRS@*?K5b+Kp}zImU+Us}YLt!=`L=xz_KKgT)7i9+-RYWYCDpyrtiw^FjQPd)@qo-E^_>dj_a#(+6Fb*v26S=&8Ar-Sk{z'
        b'2V(4sP3+UR8mkyYL#x=vXOxa3pW2F;ib59c2QFlQbWHQuTA&FKeyL0=Hw}4kz{88inB372>4tGdOm3)HjF`N5o)W}f^lb^3V>Wi%'
        b'UPJs0=8^eM7vfcTbr5m#i4sDZ6A9?M=eFjD)Bm94hP!zFd9?>alLG_>`T*S_HGycG7U3>*1umTBd4_%o-qbs(w#-OS?Bx4mCkOn|'
        b'PQDMF^xx~`v;KRX4Ex1S29JCS{q&bJXricy4We11u}%h${MMg`dRPmpE0qOH)b%t9M?m+Gzym4u<d~d;u0qG|_0t|ci)7ntO7q8E'
        b'kZeV}#>7s(p)~(=wws#`NqrMS0eBNfd%70KHln@h*Vsol?~V7gUv}NxQS)bWpv#i_d=0vIkFH-%+P^+aQ<izvv}C!_ksG^Q1s=L3'
        b'_luhPU=Xw9#=GA=i=qLPB{$2WN_D)6+42~NMrm1+y0?s`mL*tn^_J567M!z4WF<%bQJlwE=E=<7E;`+jx(L)>&4Chb>awB||H@?v'
        b'Yi2rnaEHVcQ>HCRwb5m0rSivNuxm@e5nR2wxJX%|O7(zTE=Q+UIF_IT$lbp_>sWT5x(W;VS2id{PLM^HB}d!O2FZABro3YX5aQgc'
        b'7zTCi9N|MPPt)($r_1*~Yi~Y_&S^)%jH9UeH7lAV^!r*)u8oYR<z?R~?8RL{GRvWzG%UeV<n9;FMo%N&g#J4>cRA7$Yd#M7aXKcb'
        b'k+bh^hEn#&x`O^uhvdCV{~cQqWjnBW<OSq+*Pmf(D*4n!Rh5MI&!ZW$XmtL$bRQDtf8;T*{R&;+-SrLHSA%oEJF6jPaLs2~EIGQA'
        b'h(+fxB5%8G>b17v?>ki9X+K#LuA}=FP3vjdmUwgB)U$g1`qo%mHa(MG&?M{j<BHwe6+55ccP_bq_>l6j=WspR4kX96j}t-3RdQ;('
        b'0>c+#+s}0*6~*46<Jb&6FcdnI9mn?(+`_Kk1g`S=ocinncZhh8d++S>I-bDRoUP>8cRk~~IgU=LJ;Va<i}%Lh85TTqxJ>!0OcfqW'
        b';<9xFHvFPeWu`Mf+m=b16<A_&DS?qV{i{-JR`L=lJSw(r#<a<~Xh8#=`Gd#FU@s<rnW)5MVQh04(}yu4jB#O%30DM)>8oGr=5o?5'
        b'8xeM4Pa#w+z*rF{UK6HAtI?Ho9EP?Zs2SoZI!w#FI0k8Y4!zNp0SG+TM1GlwH^rvVCj&mG`l>TN*BrORtSmLF)|nGncD?)4GvbM~'
        b'>Z@FQE*`f8SC-<cb$CMJWuon2)LIojj<F>V*DL)2*OCG%{W9Tw5X@$p#K&QlWOql`aGtUtkXt~7WbXlXpb|O-j8s4n099}M4yxZr'
        b'rqH$Tp_@1>{WAA)RAH5e@J<JVdYlGVu(%wp61BU?d05P4!a9~uL%#d%F7B%{1!kVl2iQ;pnTOFS00@!MpCeHe#L|~xaIOE1TukV?'
        b'j$UnTM$c&J8Hb^*GYoAR+bQ@#gvFndz8!%ieUd&eeFtsoT8LnTfGWJ`&Mx$78@<bV1fDCR8*=^{!Ip-h0+YCDM%o&|tYL3+B<C|y'
        b'im6CUoKGaArz031_I5;gj>-9fB+#3&T07AjX-5RnSgUvoU$8}QamKrkB3wXs>gz}gp7Qj0S00m+;mTu=?(VXf0gZZ^T2QBLAK&tu'
        b'Ga5YJGl+M~UZwL{+xiA-pKQa{bVc=+LUuS`S<<2}c&8v&MPU;UlM0N9(`^|-htZ%|&O+?LD_HUXNh`tYA<gmHSB)edFD|9g84h+e'
        b';R2ZjHIZgaFi+M_BMr;C=sZiVoX=H^JUNc{uha_Tv`?bTDuWs&dzevgi$Pb0YLr~jnWZb`9zHJcLl=#%>Rz={Zh_SIUG#GxK7;%O'
        b'bgWwb`k<Zl=dtr8;>$0)Kyy%-2q8|r5_f;z1z(QbCTVmT7uwQyPF!EZD+3RA(MbJh4dduIXpi-J1k*O$untDgd#;;thL!~<oZa~='
        b'C6F=eDrT!0*A0`)RqScMe@b;Dx|up7sX9Yp)MsoK&wX}dcCO1Iv8fA_)%z1{uGF-Rg!M6umihdoVmA^Op~L&pY19hL`Fa;R3sx<z'
        b'XhfrnPpqz)@J>d5S_a{rkL41WhJ^9OSt{8`5TqFg0fsgUnhCUv#h7d~lST^DQ(~;}5scL&A5$LWNV8O9##Cm?XqLDaoDqFhpmoZo'
        b'3!CB!poBqX!QHuM#Klfh6^@}zP<Vk6myj01Xu;4DObU-Kpln-&>JM=Q!z3S60%VmLbI(AZ0@)eGPxSzkLohM-wCD>WHwrVp0KvBq'
        b'Ky)f-K1D=fdJ9mQ5J&zq%=^b+YT(lX^yx9fK@P#35Pg9g#TO=36ebQ$rE>$Fr}vQ?wmzsZW*5$M_MIl>>9$#6an*3z@Mfhe<Z`{}'
        b'QYkP}MrmY-e~{cWT#PP5#x!BgLM(W4c+wRkMVZ8aD{%DxhQu4EMIT;7qS&|)hX*+lq49^)Q8c111Fcg9)&|7ulq9NCq%9F>`!No>'
        b'8szY?zJ75!+E?_=9Mq+|_`4K+L1@GmfLQ5~2uVq!psdFu_t5qWth1;8=U9y4?Nsyyes3(KN74NUb*|Iy-<%0vz%NfYdvx3BZuuPg'
        b'Mbq~TFSA+XuL?4nF6io_Y!8HOQ^K}|;ZFI68iV5S0Y^Tj3fJ7h;=>1)$nDCm;jnT=M0FoV#-?MqeD9?LJ@=9MDVluN(|+6c$uQ!B'
        b'Vl1r5Pa*SJYdBJ@48v;`JYSE5R<ohiDd;qV==~8-oJJS0C!7WDGA}ukU4B13Z|%y{H2G_ZqHw80BCMQRxiZP}(QQR}QJZ)R0Bx=8'
        b'#TDhN90pI!tE-mHajVXdl5|^AxMqLdH)n>u=&lHr3=`wgsbpSKG^{@|*%(|o72r5N9xnR%R@=9zes{rXn=Gtea;I((eYmF@v^caI'
        b'U8RA|YQfFZ&sgFyi<7HKMPftT>#E@#XBu$lw9^iveq=7mgE;L0Q!gdego1D>+^^4AIF2W>7S!?P$((>X_q>$O<DIN6E=(sW@`h8D'
        b'Y@G{>H(>_@!8J)fPBZ@kn&mw@_Y4`6?o&)c$(OM@&1qX^II4uLTd}%#&WK4}Ym1HD>q6IEC{Kfc_hlw~oKscitl?NpS9j=>x`fkc'
        b'+5;7x;^C&M@GPWQ&O|gg>ua%LY=JHlB!|Y#jvcGRgs*ZOMw#^DmGbPh9ao)P<%!{<$9{5?r|CGrjyShNc>fx)IMdXdDN<T?wD8Q>'
        b'LVDq}sMI;2{KibBZUY%}ABO8x((-$U_Nb(*qD&9Zx-=C*gEqj}J-joGSO2lnzmm<OO8jN)s?Apll@kj~oS7vY=WwRd5{Hv_IJJ(p'
        b'4A9wA!E;PM`u*u(i)rM^@xXF{!Om9Mt92(%(-Nq<#7|x2G>UReYPwQU7qe<DE%U6I8fvk@kh)%Xk#cO+AmKG*X*>b#zS?5ib_9ON'
        b'0&Lq6co%BXL!pokiyp=e*z`H4v^sTwQ+K#i498^wN})#{w0dbuE2l#%Lz4kevFl}*M~1lyS>GqOi~e}s-Ph^Kn6@_u#uUD0TUmgO'
        b'j5rYn)ZUhg1v$1}Fs|Kwx(PpoLw_9e6=h8Xo$r|s7BM~2Lbv!%U**!n9j#8boF}ADVD6or!3?D0g7(?|+V%c}>&xQ_D~D~Dm#4;T'
        b'x}mSu`>UCzSnK^j&quS)*c4&whR9LfnX4@};9=dLfo8nx&^hi-O^Gwr+Yl)i(GUVOyl!n0*T(0&4ze4zO$RN%G-G&|vb9CO=R<@c'
        b'1y=iK*HL$;CKdyUz>-hF;6mTwYoNaeuOLf9Y(VWXX1m<=99wamp(oP!(c_wL?J!;3+;xWe@Y~wMdjEbV=;RkmKTI}1e%iyO>vuET'
        b'^72y~NQ+au>6$)IU$LH{Q)?IQsC%NbiSlKp0``HN0nx2ao?Z}YDW)fF8bx==WVSz`*nL8B|IVc;h-@dAu+Bj9X?=4cQ+uZQD#z2Z'
        b'=9hPPoP6liZMW&PkK-NriZ?E_a_m)3Tb<?O(p)b$yWGWF4kdHu&cM)Vo{yt%f$nz?B0|<aM_MHjY@~;F8(<JJ(S_X^$}1b0y<gSM'
        b'>?}{rY|T^#jHjDofIx<6p!+FDyH5u*g|hdhbh1`=!{(Y%wCfA$BtYrXRSHLDT;OA1QFI^NBFWO2@%GftK+9=|HZJ6kLB0&vNh?<W'
        b'6!a6rQbd~4l~_<Knlh`wl*uVR4BoWH{~F`>udg{=g1(Xkj-H0H&e+q?vXZp8qVj7Ftuk=mX|P`;n6{p_)16LP=dz!I>MjrskOxEU'
        b'U4+s6+C!(EkDXRH+~YfKt2R40po9#MlclX7MhpLa?Y`5%DbH>sV}MRG*52v>9u2nGw(Vg<EDW?SJ-O14qoZG{0u>eOfkDI@9e^8v'
        b'Ew;H2wYzV0*fNm7*?`G6-Kf~8uP9_}w)HBU#h3z>nJwCIb1!Kg>7W&s)YJwkm}QHl7ANogy2FUGwzTN}P=)$;05Y|tJyMj@tKKgG'
        b'sWK(A(W2yfItqC6a0f^&TYPlO;6u)CXyQUkS}Hw-PQ>0l-arCO_yEcbFHp8jI9*_75QW?H`&lwCUi)Z7J+PmL;tKK3>5w?9uiX_f'
        b'yxWPE!R5+9eDI`=ozC*PHagDx;wT+w4FPMUe}xV@2jtU#lKP|eU=zXFPuIL8&iEhh_~ot-`{52&zuuE@*5b!@u6`D3*6x_~j&5zx'
        b'AF;j7ZYODaNZzr_=O5j<=gFxuZ!8wGTGyYfowBEKw-Vi8M39O&QPe6_u{fzvimS|JG(pEpC0GMJvBTvyhfcB9?;|mv(-V2U!CaIZ'
        b'X&~DO4DHr=H865LqW;yW=q&c)LCGBZ)(*d)@@Umf;w>fGjG!Mokc6&V7VjNjuRqLu_;pB|N~>rY9lwv<@~820pA|2FM@J>-*KdzK'
        b'KwhhnEhZ1__;QRct3mj%2R3U3Z4{FvX4uowL<ySt4Fp=ymgGWffQtb*y2G-CK7BOibOWW$jugFrJ8Qste(Zj#YYoJK(v|u{=CMV?'
        b'l)6CTeyr2yr+}=5B&ybkZn_qhQ9!L|Db3Q3@@*+ia*u`yJk}Xqs#Rtp)nVK%MaiOpQTMm#A@KK3K@&$$fu^7$50R6u7%Ds54?%AJ'
        b'*}r#!S4XGZy%Q3hr2LuKp1Qdmz6*FT_Mj*BkiVJ@#vbs+z6KAq)ok7LPM2$aFxKW-K!c3+EU?|Zb9Z`207QM}YM>r?abQ=fJGC<?'
        b'+mpUW;+t@G)!!3*U`G+@6UKRDHrH0Bwz`>~;L6+)y?;s5QP<w-Tb=A)*im-^9`ftj;CF%eTTu5g{La67*HPW^PFlV_Hsnv*@KStx'
        b'Z2Dfs6*Q@hb~R*7x-#+bsogXoy%VKN_xqiJW1ZD9z5rKeV87hw6!=T$rW>9D+#Q0KHA(mGQ}z%sRjUbW8a&7XhdWbZJq6g7_lPzf'
        b'R(G(ot6h2Wy<-aXH?e6OOMk9jqNoN$yp!>tC*SK<Na&1?eIW(avCu=r0#VWn8>>q_1q3~%WBbY7t+5n6yZOD%@AGtQlY9z4<%2En'
        b'WwjELiMw5c%2q<!)xowtj!SPwu=46gn&1lvDT(|rB9=}9Ap8n~tM1GoYU0HEj-Up5L9GbBNlwQiV4v=3ZKdTCcLNmbt;nXU&|mM>'
        b'Nc7${?zv8y%pe3izL<ED_%N<ZP_oA6VWZNyp_3+r<6r#Bh+YIWI67zNWHp(Vv`GCo%F{mT(rxw}|04U3*&Zdn>2sTn(pNLKYIf5('
        b'lZm>Lr-YOVQh#B^NhZCxO3KBqcU8lm(#5lrt~@A1_p>gRd%uf3DYt$b9TUUSPOusC$v0+n%}|<*%|PYQ7~%NsZAMG`?P^lJ42#~%'
        b'2Thy5<NGLmEb26w*6)&)XJ)z!I(NxvSz6|UU0cDZZLZ7fL<bUVt<Fc+MvAu&ZI`#jK;OsS&;5VAr<2sr-iqD^3b3~mDX}!MWj5Wl'
        b'OX;58xu<%UtX908Z&m<nAV=<?^MXvKYsJOux63<pv@q$4PcEewXUS_DHm}lsKM+V+1bStwyW1J--g^qMoTigE$N1!!DZ@PRy-)$h'
        b'n_~lsom^t)Zk+C*Cm;jWObKS0#VoHZ!Q3ySkE-40>&n;NPdmEJ65cF5s_Ja@<4l0nUWo{PY|&-EW(T^$T-|qFkWsWpy+ba@ByX&P'
        b'qP$rGB^ZvqlB+D32d4Q%qiLhL(xR|f=qWrn2t}jbZz8-*dSw<8VKu^Yv-C!@U>^4;BmE*|Sj<wvETOMuzeTj2h?JP=H-d|CAPjt5'
        b'wm?XSBCNrTgx^e8i3%&$ua7AqigV0D-uQ|9#JskjA`jvnQd)h*GFCT_>dqZ+$-QriF<N&=1X>8y*Ia%sjn#0E^U!9f#oHFSlBRr|'
        b'2kb`g1htW2Lq!K@KHFnqwAM$JY!h_0k}#t$0BcQe(J|5jTUi)07ZejZMuIXKQv9U~#0&WV#<6vt*RaN2%$5lfprNwE5%+O~+%(-I'
        b'NceqEs8>*EiQ;!eM}Zjfz(yoQ&9fsf5#F1KTM&JWBoKq)j8Z;MI=>{TTIF)ZmnShJkCHWq50<ts$v7M$(QU@u_ow(ctjKeV_m4`y'
        b'1DWZ@x5w~K_46d+fSmP$lN}b67N?4LPPB0B94*qqso>Tp=?X~+7`#baTU@SZNHaJpi6u_Py$@+k^J}Mq&bT0#Y+9&)Qh{PrJ5jdV'
        b'f9lX#*GqbjGr_~D7AxjdAC!5VoVymiY~|vHB<|mLh>LGkL1&7t@F4ONLe5F<EhxAB>=5Plc8K%F>Y#J-oScJX$a%lp75zG;o10X^'
        b'>D@1kl{oa7F5@8a-Vg4LD5IOZzm=Qpt`Y%#HdX$h;`|RmE-u8yyVs$-#quW=2hWDMgid0JbpHp+>XZ*D8mK0Td(GVf(GSED<xxQA'
        b'e?Xwb58cjt9}!KY`$;iH4M|2G72J<^h`Z#zR1?zYFz(R~@Goq{*e*2hbC@FS!)}Z?Ikrk*5h~o0-*Gm-Bl<j59^}S1KES%I|58J)'
        b'h|+mc&_d$)1D`*^HJs%61!_TJc@+zBlT1c7$fXEN$Gacs5cg-?A9TusfQD@GqdLRHjvFnPIi?+WHUv25)U%aq(4nWGwkveXVB&b8'
        b'Ap)iZdzcL_9k0R}ZuLn9m#c`eP)}PPinW0~i4Mdm6}Zn&Y4GvlksvxK+$6tu2a@~GCsBMZS+MECSjpGwcgFFF<Cm6L1TGOq%EGCJ'
        b'HA-EME>%ThKwrX<Pcb|hAeb7%BtAY0zbsDx3l_yXFdclX=NWQ7#xEU@%^EoPndvWKqnUAgPl^|cjTihB&rMVqv*YwYv)S=Fs03<o'
        b'v@p7Px@ACmDhbABxS*;K$3Ru6g;nCWE3qQuZSFr#s-Pc4nETr)244Xk;)+k|IUVX5Bj*mCT1?UjOdR--n&`o0X!#qSgd8Vx;;L7)'
        b'fXAko`r{E~t{HkyK^JVQ@WeD2ZY=G%_r=ImY1`%qMu+By2(KMjNHa0dedd(dbSB89hMY?GsZ&vo=;q>s&ZLlYLXcxZoYLKXN>mH`'
        b'6s_F2ZY}}XFT_poIJG`!n!DwcNcdWCghU#VHO0E$M|tiK(Jz?uV*tgENOQXT?Yq$0&x*iM6=T5O{9k|_jJ7c@<cufrbcD13$~km4'
        b'<V?5=It9qiy-%$5zfOru`MLJ9hX@h;WFSD^Pq|+aU;i;$1HX?rB-^kx!vh1xrzcJJaBO-KG*C6{QEq!Z)WU3g3EcQ-#0Q-E2d@M<'
        b'Ra4AJLj(j?dNLt>Ei$oC8jOH%Gai!+=yTa9xj^^ozcoNJgU)e~9FYkcJQ*F=6sI%di5h$y6kt_o54yVoH3TxDFyvz-&~9?Hmn^;l'
        b'^>X#SUZPvrFcg1Jp-pe0sR(!A6V#WLr|OP;V#^QPCWOJ6GU0Ofm6PB!Mfa`SWZ@-Jtdzhs6qYN&OnqU~$6?cO*z{J|6bvshOH0i$'
        b'Dzi#srgF^^(i}hXr-(+1@1XGg5<Hi{QJ8&>SiUuE>Is|P51S5!HD<Zd9Jj+P+i#A|H7mr$sgWf(R*IwYDqLm6<A7I|nCVjUI9kS-'
        b'lI!N4vMmprBu{N%tb-`Soqfu-ENr91v%ZWN<bc+|q5fPmV>DwLGhVhc0>E-{MxBhiKRk&sVKHDN?!|A5OuE9D<aJ-3JipeqJ6xNm'
        b'Yj+;AA2gf32yguifQTJZLK^{E{qG|H#P)3X{L%J6h>Hz!GAOpre4loEq!dlkDC>GovPE*+p|EXF7+UUsWyL!DzPkHPRe#1T5AQ(J'
        b'MDhAHa%^W9dIq5Ue_X+=2^Sa2(J^2Wu>&U~NVH^!F)F-0#(F&Be*P289=5Fx7e7|u-hL8|jo4G`$C2}E$C^44{^y1+F^|{22sj)+'
        b'*3e^hsGTFIo%J4QCk;(<A3j-Ol_T693}ZXO{y(g+Z3{#D-Cvw!7C=MCK|@{8P#<b2fEsIPo*Wtyo%XTT-)*QQ+_n$&Z3{+H<gv#B'
        b'D^HSU%3X-a$(i!W^Hly@hXQNt;AqFJl#nqoq*>xrf3n7zIF^!{KRHRp$V8`EM^i`uUpA;>D3T<i@%}?=#nXI%MoF{6eZ3uR*Io(2'
        b'@>syMKdk)`SOd)%u#Aq3p~lAaF>Lh#G6q+X#FTQ7>jmZJo9(t4VR33J*^;h^St(QDl4508WtJqalxc8jF%Og|HR2L@Hh<sFs^q9V'
        b'E+@@0GDfOL?)(G|E;HgXhELY(b*4}lYImogULIOyi5m}IWgcsBj5mMUPU10lLjXjZfc(uuW^0}0h^wMdsVG;^8b`(uMx5I9E}APN'
        b'<(in-m^Bh(45i1CS*Cyup{}aTnD*(2`dN8d3!$DP_r;Ch^f%XT#^)ICBdA~yGwo)57RndL_~F69_@GZ~2rq|`IHAI2O=uB0VgX`g'
        b'RYa|m?s_+I4T|a^?)s4Ec-CEl+Fi5<0F0-TMGy#XZS6_`nx-basTfIOO#}jg)t5$)@xEB<4MfBVP)dWxG!Y<D#33Q-osptFKTNvf'
        b'UW9<Ebw62eM>H^gIHrn;g_aNn8eAe4MXh7SX`!-zixla8k|Ku)%0X!;YQ&`sv0|)JD5)1qjyxVI`qecrI-%0T#gZ|krya+V(BPxl'
        b'JKE!n9q9%Vpb-hMhy+0TL=W8nDg-P8b}=$p73~d+;yhS=QAGXqHNai4A>v-w?%&O*V8nK_AQJ$UVn74PfMN&`u!<%EJ{M7`T@oq!'
        b'`g7^WQJ={ZH{N&X8?->?wRrHsNpiZ!G2Ww@M_MpXNvzw}4q{cj3VV)l4o_d5<^D~3%hgXj83pK$Tybw5Jd7-kxFd+5(b6UzqjnH9'
        b';RRf~ANV9Bdr$q+9rsi1XGh?xd^$zEp{i)bZTjk@D<d{sJ?BoAyneB~{tpW68if_?btjgIyT54{jqBKveZ)bWR+QC8{p$cW+g)6}'
        b'9-M_W_;0w`&aG>O`0@0FS|eLr{7fYmFFZDWcosTzE=F>10vBBDT~$B^<r4_$RE#u}$J{A&1ITr`Tiq^BCdr#9G8b!*)SDyf_hr@2'
        b';d15hE@k!FJ+JIG!vp-Y|7uk=_u<AUSkX#c4-kEC9NXg~&G_y*G+~V6zWDLtyQiu-I$2S@l|vNy*!ZH1#Di|MG{YS}fdVW)wbO)!'
        b'#M1wu;7MHY<9c3?raD<lN}*GBa<L|=K{Aqq=q2h(00Bx=W>R`KBECdhWM)N*PF@#}E!N<;Dux7Z2K^9KZ_pyokx|5DkBujB90oAj'
        b'J7YvW5cciQ-|1U&KDFhm69-oUV*eVe-geVRQS{{6qvqic^qYnn8>uU=E4$uf{2#CfSBCPaU5DEryKwaH0d%b_Mg1+{uQQ)NI=ow7'
        b'TT5Npt?U|LYWK0eJj&gD0?5{u6jeyF=nf6-=Mi7bgqlx+snV8{Cw3i1ane}K7aSmQa;Gm5O+cc>6C^8!-|F5zLB^6Gu6!{`(B@h{'
        b'1t=8-Mii4`-?ixx^@{JS>uT}=vU>L4x>JePR7r@UppLRoY*F%8-lKq*y06-Ov9ankUwAkvpa90v!%=&7qPxpwfDL54<YU!q(Lmex'
        b'>_p2+VzFqZmWvdHhpm3(dttM2!^<ZucA}C@qN&Ogqk^BPn6cTNizw%L@<9q{w0<4&Yx(>=5?V8roOH$h;t3&P&z92r3~!!j$@oOj'
        b'6u@wzc%8Ybz3%xFw1mz#&0y(?it6Em%ELi4F&&$_)r{e~-G=u#q&A*1w5CoybgkO#<H!(4oJdxniw<88_zPLkKE6+eEg#)3`r9q@'
        b'o9z}V-jbVT{=<o?-sfoP^HNW$P_wHY2d0dklYp*0R#BVIgWyJwODOxlpYSOOkJehdpQ0!3RwDCJJ0Arb!5PgUylEJ(jSKwP9-X1b'
        b'30lExtqlrD)b!Eg_*6q@Ow+io23EW~+o%p*fd^|##FuJNU%2jZQtms5!hJz(=N_VMAma0rA-^O@+A99EW9K%)+J{QEV4u)0HN@;T'
        b'lpUw5&ASYp@+R5ya(YsO3@Bq44xWx}n=&|IeBGw@+Qa{cv3CJ$>dF>?PfkuABu7mE0|K_m34y5CLTn3Kdq)BVe03lyQm36O(I9o&'
        b'xk_!Zjx$X{3z5<(##VvanVht#NTre>4|&K-BUPNLed@GRYK^aUTC3Jt1kS(KNobv!`~Uy_KEAN_Ywfky-h1t})_xp?wL$F=xC<s{'
        b'4RY;*MiT1KNjOKkN_LqJ$K#=E6zt4FMyIg0^F+A`&krC|F53Qnlz%giu$@65vF;*f)++Fm7}E)-cBWf9t9HPyo$b^n>6LpwsQt>m'
        b'W=i%sIX1s}5Qqk3G-=Xhfw(1u^$d%Mz;}W~)g)7V%I7370#YE(6ED|YCj!3}<cW?lQ+Jk{$-o&QFo$=kp<^|IN=~85H*<(3f}-_S'
        b'2K}wfGD>_gv?rVX{n2irog%9AINuvdON3yyOcle~DcRP&Aezx9r?zLx0;zJHQSMR6@ndl4@A~Sf+IqtoF{NUf2<O^j(k&$N7YUeU'
        b'QvwmU+%rWWR#dA9brWUzO<3rx#6zTd!6pqmXmSxI6Z{GCKJ_zGPpve|HSZralXU)ak!q*3@C(0Cq~s4u{Ejv~t9Yp7BLO3sS9sE&'
        b'YA#_uCK)n1-zjz{M8VM6tF%=Q2A$lhRU(@OVb(mzB!v6;?{zRP4(nd`!rq4{Gnq@vSFgb}!)(meMUB&>=d7Ucygz^56k|d%WToY*'
        b'8>9RNga3Pev+O#qu5K4)`8v!#b*JVtzm-ws8wG6RQG0^I$Gg|rCkA22>oSNySy)w!hq~oXxC_U$Yg5%Cw~O#dZmAAajY7}X@!7J6'
        b'D7R#uIYC9sVW16*iTn?K1mw0393_nIk@Uv~7ch!!Cs{s=&{05Mdbi&gpR77?osOkN>XseoRwsy*7mjYdW*5>{CfP2`1&VA-2bqlA'
        b'#qBV)oiOfd1=V}i_Cir@`oTioGvhVsvt^FF_QHq4@<)D*b+px-olT+7p4e@&rC`lPizr%V`8*7G;O7rKeRiJjlxdpvN4H*wZt130'
        b'&q+>BzK_1yC<M+~gyWu6f%nCu?6#wxGP)c;9IYw#yBX{dTM~AG=CPv;*`5fq?gW=~I_pGetl9K~beJ<|@{oHzxjlZ6$(b}8hQ@aF'
        b'U|-Ks`t@G7TVCsWGkv&H+2FY9P+IN1_Q7QPLL#yAli4zUy+MCk_=rX|NK;1RWX%eHa`L8JW<(P)IGmwe#H<#8uDf^+35)OXWJ1;_'
        b'8zic)bgd!go;@K1O(<EbzR4_>tdVMlkD~QX%=D6j#DXi||Mlo>`Dqt7f3h6fxyg5&`((#`z5TuNq@=G5Mk4<p#SD$l$B(zGadi>P'
        b'nWPW+FS!%xe?H3ekAs#AxUw#B#LJU+Z@T)H`_4wZfQ_(PH!YRf7ZW(^*cXn{HLitjIkO-mefU1*BK&@A^4wm-Kr$fR)n4}oHPP0j'
        b'uhniaD*eFG-B%h(TO~sBh6eZiFj{U03n*Hiba__|MN93AfE;;)Z;>GDr(oH3VbVt(KBt_Z7p<K3`=plGmsZw_oN|HvI7!R8WhZ3+'
        b'l+mxzcRwXly+@sX@8l=<-~UbL$=&MR(_+89*dl3tikiQud=jy}`{>cRH->jBkG*$wNO^YX>V6zzu@0CY-!wML#iN|_z0;qItG_6_'
        b'+L_$ct;oMUHnfPIiM|fCqxU@u6cHgU%eu|QZ4r;~a-%?Kc8#qvT@w+po|5-Jy86C)U4^J$Byb-Af&aPuW%=XsH{|p#`YzRDlzHgn'
        b'y3~7Cx2vmSO-BSPQ=_UT$!mw(m6b06XV*KrC-=*U*arU%u6t7cY%aEze@DH4=rk?v{e9W+=gB8OR^&I14Lvwp4t<q(><A$}8~m`x'
        b'vx>=YhiQt!?#X-ZXz&@sq>onq6*s%pGkb-Zgq)cnL=lkp{Lxvp!3=mkhEP2*_R!U5w@LGIL&dVbN1YL0nj&Hu7xAnjf%i5Lp2?t3'
        b'6QQT<l8)M41n(O{Cm-Vy5c&b$ubW<c6p99|Hio}#hD-3L$-!?97>^0$nN`#fh~@k;fv#HMnyFU##%+H-lG~zo+?qcV?}psu0{04X'
        b'b!t@uq5EqX9j=}k(&x%=aQr?=dexERhU7AJE;W)HKN102Gip1eLa@j=I9lOMMrWEn1t{&7v3@_EGHO4<A7Vi78t9q!fl)QSj7Ow8'
        b'!xm^preA$I%>PgBA!*jF;5cLF9;M~<kZs2i{(T{k7<AZN>D=hK`nhRybLJLwhZ*;OLErUx*!<?WXWS%Fc+XM#*Xy_RONgsOirq_w'
        b'pHtTD0!_~O-pRVUSSG(?OiUBRwPXGT&nq@;*z^>=;rBcKC|0Scl4Bo)0$o`p$M%KbedVsd?btV8pOaRgo}<>|%dL7n{zT)C6n<t)'
        b'FGL7<RW@PPhMN!4UB5|)eI&N?jY<BmIHG7VzKDEtF)3z<qTgI9IrjF6NgMuF_DA}}B-h`{dP~)+)UjQ2PS#5O*SP-rM~*$$@3NK7'
        b'?*&@&_uMY2e|1Z3ZGre34#H!THry_|x?z*NRwWss+jgbCUYk=MfRugtlAly(Zf(vf{N8`^=(1z}Ycz3UQc;wAu;8gly}gmW>&i}u'
        b'kG;REi}au2YSYR;<?^{7cD10sQmYq##1Z*Ze%RGamY?Qoqq9zh&MAK3r%^F*OoN~Lu!@+;l`~=;R_lEXDTSDA(<b&VKmI@FJMn+a'
        b'H{hp(5%?3f{gD5TK*t?{iTv%5zcH*mEb;a5_Jvh{2Yt748*W=wGE!>#)mVq~y~v`pFK80v2%mr7&-o4Q3-|qfSg)+KLw@T_tD6xH'
        b'%fVn2YK|YKr!nDmu<p@P^|l?>i2?sJz8;zcfy3)4b^i1ke~pldB+|mRo>iAA)yW@P=cpaiTyqpw8-?<DjylO<wJVY;_tZ?<dIjR~'
        b'Xp~kBEzmElpNlF)B%x*~m{%Z`alDuL>9Ch&hM7d-j%9|Kl<EU&c!si?vGO~$DO>%{2m*dnFDL9XID{49cf0rW?g^9iZT7pRQm}b4'
        b'r`X;&4ANT<s_hIkM;$_1sMhz=(dx7^)Zt@m-Nzz}=DtCP?tf!D*7;Anr0xjfWQQU@R@(0(dygrcE<x|>JGOopw1gHkD5@LOn&0}}'
        b'%ZPf?E~6GW6sWi@qSBu~oS!5*=}@E=r`aRxRu-rCt?;{LQhKrH!726#^zP#om^yrC0!u6-(#YPKO1F@D@|HE|?a!bXC}@_le>!Y?'
        b'<w$71naD1_)R%#nbg5HR$HoAabN?5hG4dFmyu}D9=p!bB5?@8W<)!)yA3Izxa;oZ#F+#O<6Rflg7AolQeCd=0`m*$U{J?m7B;nhC'
        b'dzgRo0&fy8CsbceVq{dJc@aYq_Wc(TV<w?ldf3hImV=sdM-pJ91?gN4YO~9ABk`=v<)#=HNk_Z%WiGc8y3k(#D=6!7V<x@G7fJL*'
        b'`rV|osWnqKYf4vx6LRe7wQf_;q}wI1y33j>@ji*G7H{g<mqTBRtm+$T9pw-``IAYCR}8E9>wruS#i)4Rq#m~AAa9_umFFZ|1Nd0`'
        b'attNk@x+-yZCDQ6qooV%Wmfej{7|1hhOSpT6tjgzHInMrDB4)9EdxHN)tS!vU%8;330A=D$2oHTh<zH7S{wzk9(wChBKwk*aVdf@'
        b'_KQXg%)zfu+e!~JOdQxSFo^xPu<Yj~FnzXIRiya-qa!rgKBe_RGV8yH1=dLC;20fMomd7_iM=_HkoJ`GENP!6-FWu!2I$a7rNhUS'
        b'UmiKqQH7KD&rT_2$dU3N&rRt)vh@=~1hJu30fq)DGPUZh&A4w~i;s9LFyg(oOr^S3v7lCcM(WI=9!+~9Ct<p#Xf}Q-lZh765n@n;'
        b'|Nc{`!bMP_+J6oPKBNV&I2Q<+nf5pyTyNLZA4z%Z2(vy*v*!pM$*f<jdHV=0V%9Ixcpx@ggK0T>p?W!flyS&#GQO<J-Z3;hq&)Vw'
        b'{xw8w=fNqk&=$=SrM!N`uzn%(3+gevMflH8%(a(*Gc;v(NgWycYU<~#HlZ<VYaDP!2<_2zv>a`sY1V@~W{dX3%Jf1!ku!sZkr10{'
        b'7>F#oZ!jeLQr-d!Z*f&l5hDst7`GNjtnE)ntd$C@^+taExKnFi`P_MW8b~o0OTlnRjQN<+qV<~v$_Ab@+H@rSm4V}iT+v8g-9Utp'
        b'$kmPT%eUGcpRmA-iiT}y0C#g>sTL55@R6U-V#2a*JUpE0r1(ALhos`~LhW-i)2bS5oriI|#YNc7)7(r9*l8Z)k8X3!1nn!2=;stH'
        b'GcvK+Q!|9rWGyv?AY>8LB+vvxCp;A+OnhuaCT(^RiLYrHEt&Y5X!YA_-6ENOS-~7T6StJ4!|0fb*Rrd^7A~89b+*XF#5%MqYp6zX'
        b'AX}y-CkaU!kC7>2gyiHo<P<_76H;`tU{UZGEJ2P4jr39yzhuy#b%p;<4y~2am`X%P@I@3#Stvgt7Us}PrS!B2DJ_&vnk~hf|2ZEJ'
        b'bsyOEapHgA*tao9^wNp;-F-wKG1{+58%QcQh07lm>V?LB!O6EkiuMjSz^@g4ZRyC_y%DNoVxx;Nu8&KcD))vTVZ)EumLm6ZB4{!('
        b'@)6sVBi*F6Ufu7~+e}zOGySkVKCZy1H$B=gqa$A`(F=WtpFHV=Nzgl7tDIR2KmD#vrv1^MODlW{`iL2GW@u+DgQ+?rgASj5HL>+I'
        b'yXz;TYi(khfPQNM(>p_$^$FJ)RwZ4vui>q|@~0+Q-My|ScdUPFZ)~iie+cZAO}JODJICp@h(%kk)z3++`?mZNwp(-la6RKNRKzHB'
        b'!(0thZ?eyb+fyspX4=LC&!BvESf3W+i|x!|z21?QSVMv?8;a9>c-X<z7=VwOpZY7N3G{=(^Ch;w!8#1NbF54+F2rTCfx9qf?cubL'
        b'3{QFQ@VZMPJGrE^IL6LIgG{ySl`vd~`I}Sd*3Jk6rPmowOP)w%v~nW+tmdu5!3SFLyBG0?gP&T&)3@XZKZXgy@urqkGQgPVnC#0@'
        b'L4PBR6U}RfiRiOv(D7yY_-=>?H5KSddFwEYPRE>z@c&A89R@8JOe!G6@&h-aphNZt@RKg2LTH>6#Huw;0#4esLYPU3HA9-6ha-$q'
        b'K$A9yjt+k15<f;e{i;GRlmEu*0|G%_<>7wUlR5X(@<z&bvL6~6SGBm=eRzp&HwFrxj-wx4Yl={GlcweJf*tO|>PI)3gp4V3YC*GU'
        b'ZA`(NrnS>-+cB#-lFoZ~AnF2{xA}0fX!F!3Y{j~Q`=8tXs5h^w{|WYU5q*>v(@VBE(VaLcUOq$!X7(3Go-T|)>*3yHdtdUF8hf95'
        b'Z`hWany@Vgs_T0DHIb(^5vsXN^_QzJ%j+|Vuw%a2@xu*I@6CiV&cg6udD}s(-`=O#(heo|%D;T{FdgI6gcETKhz8c>+T@!|0G^M-'
        b'rn_EOJ0BrjMe5ThhD(l)=F>lJeB^M6geb|3EQwdCj>_9t3MJI=OUg>NzOwJP{Y{<F`-+Y(LUyeEIDhh5Y5Pk*?*Lce4p?}M&D<}P'
        b'2y^u#ir`y4g@i3IP%pv5rub%W1isn3Jy;@QqT5Ju0pVU7W!EUR0!1YgK@ytWezlUn>lb{d-vr|qu`qXFvHm-j@*HAsR0I_zl<*gB'
        b'vdNlES~6QwT1%Ff6PkPbpL^5EEP1ZE;<;aMUYitCTA5RFTHuyUUnl$3)*oG^$*b2XR6D2G4E?KDZz}0i<Vr{Kck;W;rerX}CAPI#'
        b'A6QraGhi!3aIX-0ctereyqw0DZgiZxP_g$0f-bJ`$AP`)bHyWoht49BM{IHZ5j<Bw?8}S5ymaeyyx@<RlOAqc+CL%tBZ9JjjvzcJ'
        b'{-ICs?!$%Krbt?tsgzi@rkooPW`-BfF=)wD6&YoDUL)>@sWs!UFjJA0LTvrXRhwM>x}tm=$8voz1Zw45YW9X@RdB-0DE{pgVYYz3'
        b'+9oLyMMwy+A6FNqFD}hG%oWZWFpH%s)%9IJk^W;`;fVn-8+rE~nvGe0EGr~d2FR>`a1p>^!AvpUx5~TFSJ*oMOB+2vKMWPl+YD&6'
        b'V#&OX3UU>6qS-%c7#NMnCgdyf17j)e1Hms`KTF6opY#FcVl;+Qng=F6A^h~5OobtmhUGo+gS89ZQtR3{P5l6LvXGR9&eq&R;5?@k'
        b'!pw<zo;eAMz}!y#N^R1Jiqju86>Lm9^=L^!-xJ11$>PF-FXx7*egA|RpKr?BKA?Yi#{DQ_ANIV=p{yqOEx8C!7}qEWyuhX0?8kAX'
        b'9U;h=6fM@xzezPSB0U_(LrSuc6hsKZHQ)3D6QJKf#z8|N19T}KEjZJM>xZikZ*@$p<ypHpXsrJ=4rR^B(D~07`rWSj2FLad1NGAO'
        b'=)Ga}Ahi!p+dE_1TwbPcUpK)1en3ChF{8pT1?01u(YWk(eHeh#uY#?CVa6_J{I`Sn&`<fdFx#U8PCe-?7CF)?rjefKIUd)~(i^p)'
        b'<pccbi!gqFZ;~)4EU=eT%_IW1AuqdZfZo?l+Md8c2?iL_nKMvOpZJ=zrk##Vtp#~WQ%teUP%O8+%~i!%ZgD9u_Bp;%6^tiNrDz%Y'
        b'%-<Sgw3C4x(1FUY^EO=i!v31f>TPP35A>Bmt9=dQlBpd}fA)0R@?A9vOym^)o^r)GVf*s>OwTPK1Xc+3oHevbJ?H6NHI#mNYWSy1'
        b'WZN?5F1M}bNxR15rRDSSShodPZu>+3))Bk(YrB!r)!%fiVw3u}nH^i6ylr)edTW&S@W~<D$TZn0J4naUvg&ure2v^2GKk;Mpv1Gp'
        b'?{KSY@d2b@w%{6>qV02Q?+2~V+Mz9ylm6L+^Y~3Vj-I3m8>s%Q>}2&O2bq76IDP#3$=zkuXVj|8!b&@ONF{DkQgtjTr=m{p)26WF'
        b'{hrJlDW-l}>dv^5lGeA4Ow-zp68v^Nng29JOT`fcLD!Yv<ebNCfcT9`Lw`Jd{1zZpg$Y!b#^jD|Bn_wyITHUhZs=CR@#C>+bID4('
        b'J4aIfExxPd9<ONr+DS^1GU({k+QyUEXmab*$)Wa;q4s><Zx<4(Gy?r8HaD^^e?4Uz?hD?YD7|z6I9iC&b~m>t?Nghs-zh!6d#<B?'
        b'=$7~WetJH-Gq+>9s^fMy*(kI*F+hixgQaWxbFiSMqH-VlNpbuf>vKXCwF0|Tke?<9Jj1EZg5uH3p6Ijd74$4#vBovNw~yap30IMK'
        b'rTcqXb3YRwPUFte<1*FRI6h68Bwo!ZVBw5<S*)(uVb7q}g-5!Dge7yVQKAz{nfU3AVkq&HBzMCmh)IxFWijzjK}@c76Eld%Wm}mk'
        b'%-~I!4Rn~guB=+UX`dNCf-8c`*oXVOaoeV77w+@MsWgA<UAK$O$|m#%ItF5#gWq+N_Q7weJIbsx%ha>fP%Pgx8l+5hO`BfR%hvP('
        b'A|F5YXUkL_Op=I}=B`rEQH|2vJv+b%$8QF}WQ~vAhG&``f+ZqI&aEi3XArb|C;$nwMUYUjo-$<+apC#mMcBRv#(-ko4-!-SbWqTT'
        b'MMS<YC)hBCKOoO<0B6M^UMRe7y<GFxUbl;87$F`A{cS%jHXEsp{C_iH29+iL0dqDIS@=63SeYc}*_I>;wuO$~09+0OeGsVH6`l~p'
        b's>$nT!U-3n_{?YkW{vc9<EG^Ft9nD6tULe%Fj!b(4hM{MERWH9v(FuGu#^dP+pg=5bF|EJ?S}XQN6_MOFPD9e%$kFx%n_7*{}<LG'
        b'g*{>l2A5GK83I#=%#@)ne6jChvB<89w=bIljG(3Vtcw=im>JqG#-i>B%2iJdT`|Yct=b7uRg28=slg<~il5_A1W}rWwW^{>-IHPN'
        b'453?CYoX+HjHUFZ<w4H#WLV&B&TH&rv-$$pWS+G*X_=+?rtZYJ?QAdZt;ER9!Wy&x2ha^#ABY2PED@vM;!VnBDFaLBVQF4wZ`}HV'
        b'`=MVXX1Vtuwi(azJ}o?Imb&9paBFQ1`H30#*gQJ2%}nan3on{U&+;GG(LR@30pi#5KT?$7!#5bAT5@h_pnF`kg<`anQ7baJUR_y-'
        b'U)kK#Li&>lvupc02;NWZX(h#a2v%co9zpL+e1OcF2N8p-nKglf<M~@gapyR&hcgM)v{Ai6k*|vgbc`>RsT#uF`#H~wo5ib2T(9d@'
        b'dPC`}WY*(Eb{lS6*<H025d19wbpVL(C2VxBT_2+=0JRu}?<~TzGE8;lYq!g)TPqE04QmwZKDuGa56h3?x@Be<93S^WAGjEG7APHN'
        b'mvdcAirKYeT?{Gyn2TlnA97~b&UG>Rb@OJLUAxxBz;Dg!hF&_~l~q=Lf_sO_8baSe|IMspoSYHA$IXxTALYQB0zD+|RXlhC%R|-?'
        b'j&|eeJ-h1-pb{8Uaex%x1Hr#kM53#ej$E)JIg23PVT`V@#QU&iM%Um1W{sx-Sdiaw6@-`AvsJSDBim}en>(g%9kFEIWMt5bGDaAe'
        b'Z;-+a%7}v=i87-|@a!FbS*AKB%Ny=Zf1`&HC6%~b#t%ueE4s7>pC@p-*j>@2IF+#N?6H4J+NCj3#gEz+BJ%t#6g^FCTU+f&wp!6='
        b'x%EsnzJ{vyPr`<lf6NiFjQAsHt{?BYL;J)ZLi@5l<nZZ(@_%r2<^st4cSy6{j|kUQzUy%TIr%ehnM6tI1)EkzMmCb$1cCWCHLf0q'
        b'K!2{v&?v>Lax*YH;~Gtrkrs295hf9t_$stdFd;W^qhS*8k&2NNH`u0Q_Mu~2Z>f1ww_Zm7wJkbW=OytuZu_<#=ZqNDPe1be?f%a>'
        b'm9xzh|3HaL3F99Y2hZPRdDb3i6bPV#`_+4PK(tES;{R}**HbJkm-2A$zDk>rr%OmKm5mxy%L#@RBvKKY=Xx2EsDcFq{-4ihh(Og3'
        b'|2xUkuiB4UY0~KuSe-kZ8KR;qF}C==?Ychn<`omnLV_s}YVPY{m<Lb>ru5i_q^jU2So`vC-LeZsDm|gIb2v5Yq_*K68~|q{gHE^9'
        b'D{?!d@NVm6<B>+&-92{wlGI`{;1OG1<AP`EiS)?cl(-%@Ra4Y4i6)uM8eNYJk1P>{TgwaKD|ktmZU}VCH1m7tV?kNWP<6ZeLGaW_'
        b'Xwsye&L05q{;7w_tYgD^8La|Iz1~}RqnDP@B9oDNjx5O{N=(9_3Q{D)PY;y9c#9$ZzX5<KF%!WI8z1b2?56B1wnn}!$A(I@3id{i'
        b'&t)B!5Lw@GL8>a&N4i}~&jFbxs>kh808#!k`~#&I4w=I1R$8V7vt3-TpwH@jGR@?kxK(<CA9YsCJEN}kYSl~uK1JFj(?|fpBuIM?'
        b'@2WD7Z2U{_h82p^*A}?7{HDIZ_Bt}pM76J!B{9Gzw=#%(&w44$yK9oHF5H%<1MkQ*Hx9X75~Kxf6DU%*Z>ot|veFWPtKL<K<{L;S'
        b'G5uX`g1wR}=WHd|Qj^P;+n}f#F;O+NFY&b@zAx}XxcLLp@{Po-lA2u7m13>=w7@K0F1ZjBEDvQ;*H32m^_a8@pKAf$$NZRcQ?>c)'
        b'zw(8jV%{R~71rD5+1Gk)JFy-9YL1B8Q(70j@x4POi5aS+7i?ejxV1)~^a}EK7tEhyH$kfmv%X$dZQZn)9NO$WcD?$gGF7x{=tny#'
        b'uBzV?EiEyM%d4=BZlhTDKKEG+u9=Y(9ii4zFtT}<{AO}Xi78tGy4yy7kEB>ax7)L?_yu?YY_tG6*d9r!il>x_iTu)}z!NxvJ;%7A'
        b'MI{uG|KrHUO@~aGf|A4~sTWCc3Fp}&F5iHkhjzt-qK#_kW4*fF*WG}{HM^p&nLZZSA+x=Dh~8q?<35J?5@det;I0~#?Uh4z{j91_'
        b'*<5Tr6bODo&o&i#Zf7;t28C)7h1zC8MQy5`l#WJkOSetNR3|I2Yp7i^jazaarYBHu+j^*)zr$zOr@OPytLm>~T_->fs1XlxcF7fb'
        b'nssj(q~})>_Q6j9R&Dv7HT3FUMN(BAS4~E7Rv*^C{fR?v$(5QJ+tNYyIMVG#Y8$>$Ra8lqKS(4=<9^z(ZO0xx=oMU2O+_6kPA2x~'
        b'9|RpdW_6OIBIZe_d))34l+Gn{UsPMGDb$a@o-hkYyL-H}oh*;%Vk@>mAGot6<r?m>_KKKzyX$#GrX}XLSJZVtsi;c_>?E~y?!?)e'
        b'tQdmGmyAFPy)B5W{5%&7)hP0xyG1Xi<M4s9-DSPCimjicFQ%3~IZ<)`?`}G^_Ui4T-uIHXK6i2mw+ng))%_+CA3XsyiN$33Ne*j#'
        b'6!&I~6!MNxRUDF+J{KG<C8PwVziM4KAflrH)rQ*SZZc^%z4V+*da_noB9|PEda`tW6!0P{4tNnYE4C9N^RvgZF5$CF(6Xr2(AZrU'
        b'Z6Egh;SUwNz9<PNhfCEZCenWcn=-svk-um3<Shjqb9K)Smy6o^$<+qs28Y5GY{PdWTT3@gv<Sx$l>elnwgiYSu$C%HjFkTz2XVB%'
        b'0<>L-P2I3rLFZUY)mgVVpla7-7@mz{OUZRp79m~;YtA1I!6+$VHKnpC8^7sxyTVEmNt|mxas;1G`~%vjIR58ymO2i1)~^tO{p0yE'
        b'&h{jhO{lyW@^il3lbn3t&>a52hh$Ayjno-NIE@5<EqAfQe=FoyPqyCJzPsnguO_i?cQ46Uvc!Fsq+cE?z^~k5!Qu#C7?E&%($Uw$'
        b'eKFEc<dgwX#MWAE>HZ%$pOKib#ceyg=`i-C9%q4rzZS{IZSQ6)U?EAF*m{FF2bdF=Zt7*4if)D}R?iTDHr=mIq_RSHMAKjB&ig};'
        b'JwBxo_aE>-8T=nSomaKS2vK;{DRie9FNqlniNIAZsoy6MFpG%T2HjQ8Cm?yy@*RLe9`t<6-(^9%*7YP9XWcYK+1B?YFpSOIbJGxK'
        b'TiufouChJeBc=#jVNZfxMmrMI!XTok<PtiGZIAUN_<o4{$@ZI`UE%-q-w2)SA@R(Er+X}fJLSQi+;HB1BA5vYx-LE;bY^X7cOwZ+'
        b';rB4YQq!aWvx`uE@Qtz@9Ghqt<TZAi;!{+@DE8qVkkoFHFvO=24O(5>7+z{#&|~8HAi}$`0J8V?s2q@sge-vrV-P=)?l1sUulF=#'
        b'Bs-_a<l1UlM3~4h+w7hyOOnSntH-oRP+%}k6{lJxkKJ#|0eKV*M_D9G9=;=-4dEjbVJC#2kehUhsufG7LS(Fi&$AA2i0&w}63V=G'
        b'N4ONifjhz#kY9I4I1$2@pTjyOU|+#wN4j$eJc5@afEFQ7m=I845Q-#uM0f7gpr`HLiMAIQ=-7G-FfOnMxyJr*2w(v82KZlJ;&TZs'
        b'Z({-j4E*j8e|&NJRbVwR(c|LzbtP1yK0NrJy?6*R;~^F3BehAb`Qi}nvKR@xx{1b2*q-|Y)34?q5UR?AwunP^schdZp@^U#4Bm^g'
        b'{B^8b)=1ipbmLXB&%@*mdk)CF?;nDwK8%XZ%=(tYchf3gq#vx8W?jem{y16K*`+yh2v3iNDl&g82%HJl^$oTAE8DGZs7Vzqvb}x?'
        b'Y72f}kzO3EQ!FA{?@P6dr)L+W0A}lpR=1w;xrCmbL0a5cvF@V~E&Gs`zl3PH5TZp0D&dQV=*2<A;w!<ik8<c#n1=1Lo#}>oAa59+'
        b'sYG}7lBz|#r|qBcOH1i+LjM6jH=s^XmUXX;xjNMB_CvM>-Tb}4;JkV25S}SQr|3+d3$KEBs`z{rhingEK9F@2^Qgw`V4N95jcHqi'
        b'bB(y(;3O%lL+LyA9Y|uQ3(v(6b+DkQ+l||vu6pOCH*E=gMZ)P<eHl^|H0U4H5<V^I927J;l(oXj&PLKQ!i8jt!$(h}<<{4CIMazn'
        b'vMoBo7ar|&ZLaQAsE!lf;zK6{mZc&_08<t9gmfZnl;h9YvyUA*-KRL$mrUo(%{xIZEPQn16Sn8JpHW^GY}3q^#l4c0As;HDq0bh#'
        b'zcHz8zog<`GPzm(#^jD#=X;}$u%$AmlxU=!nK0aAGxNi^m*xENEq<)2H>Et(1?)3w4S{FJPCb0cn{~)_Ozn0FEw?z38)?^Rx!bjt'
        b'_fJ3@pcD6XA$i9Hw)tKB)z95mx=Gtt2z%!oYNT|}-StNqt)fLkZH<&|ZTEzb_NE+al-NGOe5$h|jk=4SdC1A6;1P5tg`IUM2!J?t'
        b'781JOkJSi5DQZ4NLa4T3aKj!o1XTk9J0#tWOH-q`gh|o;ZVc8lHtrAu7)ipbID{^M4R@K22(A_>U0Z_o9=}f12<!FjGi)tgp+Q3M'
        b'XK_70QcuYmg*v-|7SWN(5AWEkbiLWTV8N!nni+x;6;)icWkr5ISH%2Q^L-~P4ArB%LCu!YiyK9@3T)?7GF6A{4H;knos+6aHR{dz'
        b'40r0M?rssiq)}`e!A!#|lqom6XN%XbNPKNQM8;txEu3#!pvC*>MTWhaGo9?$u#BaY!#ufK0h)nz*r9YY!XQvt*(lwXSDWss<{Wu7'
        b'>7R{MEo+aiSMGT|%36;HU7dxL?hKz)wP;&d?25&;v87pm=iCgT=u^YE&?Smoi*_t#vcBMGkvW`NcfW+EQ~VF^>Wj);z7F^`gOvr9'
        b'6*Y==mE32ms+Kuao0X+Cle|Z}PY71Ot@bd8CU!;nw;b@V7r!EJHM{;h)hVXQ@<`ySk0JYA(;5Y~9&F*`WTW5>LELV;j2JEM7Bo`!'
        b'g+yRL&h#r(4WpXfo$P^b1H+3%UGP8K)E#7U`&2q65a2f$5(X8%!M`>&ZEBlOuEu96h}hcLhOCg>NO`G~^>iDxDKKn}q_k=ifbM=N'
        b'K9oli00(k#Axz)aZ36X(0x?`44v^(HH*h&KSKYE}Qx?31+CaTIh=c(x|M~8a-eDsYUNzn~@8)zraT78l<@cRzRjAH-6a3F#1q%qN'
        b'%fEqDJ@s={Zbl5CX92&22J3+}He3NP`&{>)OC<aTllbg*MuI6%^C^$qnUdqigx_~peTeTTP(<)>r0zj}Sy|o<B!||U5Peyl?7BPY'
        b'L$b2Fe<mSFmoD{xqibdN(MwYJ{RC*p>%KFCqXg4`&8PpGPhWT^jSim1hr4%2*W0%*?A|4NAo$h;Ju7e@R#aoRWpr0;i};1%B|w=a'
        b'=SGO<On0aaypk4dVIXO&{A#G5m7VN;|K6tXe`9rE2G5aM82vLznr_vl(7O{ste!;7W#>zRP-7%GOn!xQu!8^KCCs3PH!bmFr=q&O'
        b'QQaqGAR~2ebNq7xuTT%kc6VsL?qI*~0?CA$7?Z+ZuY!o+Fy=SNf-=atTWXVao}e5B6K_>OTFT!$SaPCOB+@Y*hbueY6{JIa6W8qY'
        b'(;cd>NEpw7*s+vPx^Oz1IQH)dc=EXV@Szy?S{E%3<Z|rkE>J1>!3#PD`)wD@si3-NiRN{^D_!>ZAdM6MLGw|qB7&t*cj@iQnm8wu'
        b'ejrq@C2}m~AYa`gj_u|NSQM=HL#WrXkYf-0OTDLmsW+hD>mB<4t=Iiay>=l{W3Ue@8_9~=DUOKP8dz6fa@0mtHV0ndLOLz1VFuTD'
        b'suPcCq*Qjewf7Fo2-Pux0eZZ-Yd6_Q>cYlOz0&3NcAb#X^8%F|znTTx^`{PV{JgFQ=HJH67+EJuD%rk8d&1@Fj^3uG8#q|RNL1{b'
        b'0ctErU#ur65_t8Rgg)ZWYZekOlT1YPAE`vMWb?p=r|;XasXwo%qi|zaLUgpM{Vu%I(@7Mik>wu}j4p+D>QBE45L?{^pj(TvuD7g~'
        b'@lky4zN!m?0NAyHr2fR3DVm%vRGFB1(yqht<<^oL+SGyTTzy6$$^cqS(M(eO5OH(fbk$5MA!f<uIW(CVwW0*@Tf1Owte*p5mYhgf'
        b'6nS$IS)NAFyGrZMVD+V4_@XUB8@l-M&imf5;8R!-Z^E&^>w++1S=NnPp_|vJew1x~TD3=p*`DC>uL<U0@0-Z_bnt&kM6_hxB+O^('
        b'8VZLWh+}l~RL<|}g$-|c24MwNt&$m`$8LlfdA?A@#+6;&5>PdYgBpfPCV@udc8!!!ALzB~<~5SgHxQZ?kFO~r?U`M{=dIjY5d-@7'
        b'Go1Ki4&#5tw@IG$6Nm3oi4FN@Z<c7qDv1Contvzd(4MFtFgCR->wV5h5>@9X=)wQk(FSPCS7iAsoa!8Ygi>YatDcQjAP|Ru*byXX'
        b'M%OmHa#JsaK*L+QFR@oOle(NdD$r;mq8);2CsiL&U9rQbOQ~$|6%w9*jJ6B#V6QGED5Yv5k_Ibk70~nPgPoO`?sy{D`}NvxiS9#g'
        b'g0A{GFn=I$2dVWL0O@X~Sk8>z8M~}%(ZA-)S))2nGzvX8Qij$;T>Y9m(%f3ff8reg$mOB}AN&j60UW$6<vGm{-mg0$DDL72>|)EQ'
        b'QO&+i7&j6Qh-d3Me`%M^**W~Gvd#g91MmeeHS(j{;s=q|85%}&y2;&@0U^ha77qo2rUQ@#NX|bSWdz&S>BsvaAwGMK@q8ZYwCjQ<'
        b'eochkl~hryv~9+!svXv!>p~s|dbkokBUS`OR1K5RQ!){ifqPG1rW7s0x8zz^;oeYD3|YRAP&FuVzAYk(=8^tIzZ6)eYKRC8`(PJJ'
        b'aAL!(*40r<akAvkB-qN%iD?mu!|l(Vsuu_&MX2Io)?<<}SQPm${ty2DTc1p1q=UWU=@`8;exh4+2S>{bIHD#){#<J!UGm;29lPP3'
        b'GS`MpRqNQY&hmcXA8YSa&A6H{7oTEgt)1ogJYvF@RW~b@39Fcd_4ud(61$}{OH3qGE&=HgLuU0&#0hwLQG(P%w<El<6Qm*n8#?`X'
        b'2M595cZz@H<DTmD-{65KJMjf8gnrj4zRGRRNXRD3oA{*S&hp0KdS4Ui2(PFW+2hI7nkf$7&@Gq-$pdP&PwlA>o;wLGqxp-*vu^)V'
        b'rkgw=oG3@tQvnb6%NkrC9@s^x>Ztr3RLWR8`$%VK;SEPc<ZWbPI@9^Ho=BoX@z!WiRS2mpOt1v|V@Gg(2Fy9(s!d$_<@QEl&>K_F'
        b'gsl6k9k6VOZ-(B-NF!UdWY#0Zk}6t`&tyms;#K6&+Sz+TRJchB*Z((oGCu40S?wwyi>As^kI{8P$WId{k}{=(+Vx!3i(XCV2>~sG'
        b'_+lkwQGFa<Z+l7rL0aTcR<z*$aDt8$8zJ``)x&bALN`+aqPI@=FWRtYC$=)Lx5KPOSDBb7CRbah7Roy-i`-&p{Tw`z_e;_Xx<c{)'
        b'mXs&x1kfR>nQAW#cjyZ4w--h_NK@fdt9>e170$v4s|{viIAk@Ef|V92w(5tDJ9SJwsa{BFzVBGX@Y?&FkZ$;TM@T0t;mL-HBvz;@'
        b'2nf0T3Y>0YDZskQQCy2&=>QmPK#Wfi0_@p+9bmIxE$-mVJOVKhyTaej5$x#>aYIPIe6F4Sq~kwy`asQf?2pYIKQqjX=0n-&|Drm-'
        b'(1D8k3mv>FkBzgIMY4Sz3Hr%wPshzPDcjYN5KXcLn4#Vd=`K%ZpmQ9vJ9z}H9Xs^|o7?f9Ho@<C)C)T%)NsW74v)E>$NV;rIi1H`'
        b'62z=)9sgNrcXj*-#pibXhe@%j0~UfiZHmA%*fRE49sjNe+wN)KUfp5WFR@ywq3G>@?qGLx)XKKM+yQ}?JJ{+D=Xzp$RY$&_*#1(7'
        b'?av*x(xBfqUEA)CN8M~+40<RX9q3rr-hXqBDj`B^;B_gOE833Wq`@mnb2LR60n{RG9jK!qw6z1${MR{zw{(DvLEyO#f9Rec=z60g'
        b'FUz{6Y)VI!9xVN6%Pnr`G>~l9KcFfAgP`N*cL04ZY_H`eR~>AZ&qZSRhhM^c`a_i6b$``}ZF+mV%u#Sc*yO`~99lYC8uIIa{y9Tn'
        b'xh`BPGr0(JBxQ^juU=uzzmL;h6S~%`dH=xk2YJmhe|;ED8dX%bkMuu46c^>+92ctz;;LP#4jTChLiI03zQ*DlcW6HAs1Xc3QSWdc'
        b'8@)MGfzi6ZLo^uolGx0}rLl}%MO7F&^@81uzNqS)(`BW_=ze(MzM%Wz%)xGoUIH|nMH+@Pm4)|q%oeT6OnfyPB1hYU{P?46HpRaT'
        b'eYIS<dcxtbIz)>*I(k=SBvxIkw0r=S*C>CkzDRr?eG4FvSGTGy8fr1)$E~lcMx{E_3bny6v<d*Pvg3qsQG@PoDwYX;N&tB0ozj8t'
        b'-<_0dcDJ#UI)bLZjX=PT-b6to-YSN;?Ju>1Nrhj!nMSchN7QAK<*+^Mu7g4QD%hu*$~JcNU<l2(2icK>4k=(U@HQC^ug;0Y(slsc'
        b'(p*dSD8|3|3mP8J<~H`5iL9R;WJL#o90&$)Ib(t6?x@#Bq&(Tiet8gNg<6f)V<T_CrK14v7Qi41oD74Nqf5p*4)UjMQIrYOslYoj'
        b'p@8Z}Z>lb1G?0h73ko^&!Jj7_djd=F!<(<i)W#k?2)NLE(uTCekYhq83)b;J|5As?^K%`6`J<l26Ll=SqmBc2)WH&(KeRJsuF6ho'
        b'Qrp;fLrj2Q+~FU;PUC}0p4Y~a2WcT5<arL#LZAXvY|kgc{40dU)JAX7Ga-Hwn)tRxk&!`xny_OUeIPp`limqow&vivh$*0bUcVmO'
        b'07?W#y><{+)x3kj?1g_sz?^_X0Y6G1CNMQ7lo~sy=*<eC4B09q3QG>M=Jp&hM9{I2iWE*k^65wb^JcfDS+eJl{)dT_@m6ERDal$g'
        b'@ENE3lJk7RrC)C|Q7@=Inw-0Ob#9Sj_00vVSFbkt?=At{n+}@&zruG&B*gl)^$ATDB_TVueoea{&!{H1;hRLu4njtU_$hQE;JS0I'
        b'9l{6{9Si~`E@DHrI(zDZs#5f6UT#NSH-WKb9t2#UO8c3V_JP=4fUuT*Z~GaWEe6qkY8x(9ZrQjudw3EtxP6!=YS=%9!JI2H45*9l'
        b'^YR?^#Ezzj51x>93+b7bH^!mWU%u3i4>-{;pWxHqkXojVx{jga&+Q_0uVWVWSbMPFQZBVJ+BlUnfOn!^<?;fpja1r;z^u(N56M*P'
        b'<hGC6YF3)0O>|Dhi}-lU)*q@@B<KFONYxT%f@UNg#6@N$fVv1?ZSb}SUARHl?Vy;Bbr#CdWs9^2BSAd~BUtf40NZ8t*|jW~JA4{C'
        b'bf@7stQP`^dU7v{Ci@O*XEAzv`HegG4$2f9h%~?KLYZCd0Hg`4%F?c(r&<Km$7cG=xa$8-sb0~`p8>*qijg?nJq?odZSCIhgOAG^'
        b'Dcb|cWcGZU>wb6gob=%`<-9ch4b0x;6}>JGUR(EwM!PZR2F$tpO|R%61fIk|qc9*Gb#<s=)wdO61TOzz`HZzATi<DO3nMN5>i`Ez'
        b'#z9|aZ()4i>Q=KTx+r0?Stw(_Y|l?1*kOz>yw=XU1Ke7n`<T))j_-2Yg;MrxJFKDXnRea{kXMz1;|5d0*pJ$WqTvTZd_hOVV<QQA'
        b'2_55dB)bP6*Nq?szN))vS>WsI#jDIJabi(8Ez?0Dh8=8ILET5Od=N`<2K!;V>Hz`!0frnI3DI(3e}bOGP5@Ne2)3s^K}E8M_@FSC'
        b'J>I@s%)W;qOZRnTlJ2hYMtn5W@#gNDqBK&RNwntRQM;mOQk+4s{q041bWpfmMBv<YF!$Mg?UJ=h41UQ68``7Jlk8r^XcS&lEhpIa'
        b'Ae^K+KPhUhh;0c4*#l6J6we{j#ck%uDHTN`*2hyt-Bp#vHt}HOlwA=0F2bgd@S9JG7P&EU${s+|z@yRT)-MlSyzSl7enLji^gJ;R'
        b'k?CvN-P+_F3TBAc&ByDCF&?)PKDnN@$`Bz=ToVHf{rI|jCI#97BB%`_uwX{^Mq5zg#huTN*33W5R<vhFlVDz<Tc8hg%;($7aZiW+'
        b'Q+xSH=s&+<&RUTu@$t}J^_dp6Ym+HH#q;^?Q=@HO8&)yT^549A7@rb+?TP(+n=w8mxUu^{x*%n!1(1YHlIIZ!oVkrK*A{Y!YlHS9'
        b'd%P{A&&dMkDDN}vPsthuwx?SG<!>~qj|n3Tl(mw_%=nyZpLof6(+8x{NEk&iQESQaUkhT5ns-~Arv>(~1(IU%W0I0gm~AEDr&8C6'
        b'A8T-9AZne&?aJXnXV|>dC&Z5}bn=1ly6h*!OQ!LGs#X|~Q5VEZvdkDXlkZ82q-Iw#gp7v;X02UPB!27xJ}t2r5=_B_#ETNMYe}%k'
        b'RB39FIH@%l2;W(80kW-}D6g-2*6cC_LrH%4Pm9f&0_1@p$cw-$qk*Hyp!D*#2}7X%O@J)^+W<~P!T*3%sylLLobB}%0PBkb0~pJe'
        b'VtD{8_g{ZX=GHy}`mI;f{zv5MU9J3^kZ~SLs_VOL*Tlg*k=h=^*!lJLbTJ+F2b;Yx&RIC!LrR^R>5ya3L9+Z7;dBws9KyT04L#EW'
        b'$YT3-EB_#59PYBo+5xwOk6@N~Z?~<xM0!WsATEoK3qK_(mU&6cWaJ~X*<P+qRYTde3%lyQ<CycoV1nJcM`Yb88m?7dZBSM>sI4!G'
        b'tPN^Q>ur#1Xqg%?TQ>y-?&S+im6ihPZxO?+Q2iB~W!|qbA`v4@Q>7~{a_^-!EX`m{wngR*VEWw{S_h$X7>ea{YwZ^y;tPz3;_;Eu'
        b'MS7X{GmMD9h#w*O42Grz3I0=6jrU^=%Q2k)W0Jlk0k5LX^>()9yOT<x?vs4oLQMDm4YLvmRy-r~9>>sF3+_sLu2t1}2QmB;hT(r{'
        b'3;&pii?teLL{fj^4iUbOzlhj)^FX73Nle+=f`UD+g^ppgvFKv@snw7eGFjT%07RfQ1Q<RceG$?|f#v-%%p}05Q06pos;C44?7lX9'
        b'kzHs=hos*ZWyrksNX|z{Mw-}L*_JRzioaUYyA2cG#{@&-hJ6{{wHQ8*;pB#N%j>thajYH1u(t-24hOUTYrTfVNvb&{R$Pr0yAvlN'
        b'sWQR^D0baO;$I38pBB}%1M@jBUwu?4a+hjAfUz&|vAX~a?BI*pCfYpFz{K58W5%s~#>9V1OjVWfXrAFyQ~xb>Ww7Y~@QEw`HPMhL'
        b'SAD>jEe<w74zTAXo(4;Z23k(X1g^;FSP*J*3jlIh=;eXSvWH}NO+|NEmRqj2mZ`0kYW}N|Dyi5G2=m)u3gY;Js>Cqcbmg~$Q_Y+h'
        b'obrt#fC4Yzd^aTqjpjxnK%TPO02=rxAptWO!7z*c_8oNFUO7O^7=0|iGA#LIma)Vr5WhR_UEVspSJ}}}FN>{p%Lq4~MG=pVdu442'
        b'iKI6S`_Y8`n6+r)ObGMl^NA5!THYwsEeBh3zG?S7OVij>vY}&xR5#T-(Ay~Tl#b69Prth006seA2_JXORF~fl-S0u&JXiRXOtnfJ'
        b'*f*9xA_BELSLj-$PJie?e!rju%;>3YpsF?s0n|Nv8`W2HYtR-q@aLrRbp-pHRt&15C2Jzl@c!>s)r*8lM5rL?aZDO2!3`Xc8xyt#'
        b'zIE{H17IS%bqo%-dFm>6y5<0TyEV9c(Ud)cNYhqk<}c%dSss$%K@HHWd@a1qtZEQBBf#F?m3B{>7DQEDL;eTjr@m<oTD4$U+TwAB'
        b'KLjRi>Z^ByNt=!3u=c@-;dbT8Pn8`VXNTUC$2#zGk6VimC0Z7b8wM!6S58x=2x8@Z(ll+pmcvJG+*-lO<w|_Ft-%_|8IR2r|2Xlz'
        b'rs=_UXn$_Ucg^ha|Fs?3JKJIX|7u6q9qqW*@-OX}`hRFg*8i;?8F#h=8sWJ_8eN1*CUDObugc6{#Ca}~kK;)O%C@2<c#@$~+%2PJ'
        b'c9EcB-aQ4Dd>wbn**X*sKRmr+q}PvGXN%WoCcZkWQEa<>AVhD?)ZR*E<+e|w-w+Rm4L!C^zPMAYAO_=(PM^ED7BnAp7c{Fqd&Zf5'
        b'D(foHP8vmmY=e}q#*dBD33`o6$g`lqs`HG;GC;dLGq$1p@3;qQAc=izUMAz}9=mOTMWBrGZftENbv<EVvy4!h=4OVOzR!nu=EA`A'
        b'EN^CuT7TY?W!K_ZVb`>V4vHvSL6iTM3pux(1Ancq-n45T*)&IC;AiAT&bz7=jq8J9ss;kAtQg(rV|W+O@*xRhz=s?ZoFD_=jpf(f'
        b'PFqveTpyuY&z&HBLV<XM(-bwcOF~s;T|nAXo@nvrK%KTIWR_;d0XD1E7oHn<ax7`kzKF29+?9+koM6HQ?qguVE1P_3UFn!+d2^#M'
        b'*ar4DEusD7kUy@FNLk+Ey}uRaw~geHE^H1yK8DAfl3R68k3q?h(zy6v3gdSp{;N6o6~UB@7O%e5okt*^tIhZ#x`1HgTRp4C?5-rA'
        b'Kw!tij)DIkv!5pI(r9mNE7&I9m{!}219$Fr&$+V#z`u1QpuMhN^^lBVlq!>yo(XCCWkQ({!n6#pz{65Hz4>t&n*Op@^tf68)ZN4D'
        b'W_P!knUHSw3_zYFUJnaJxph(iEwgy3%!K@}Lf(l$KZqU`9tS%mL=mGE8K6!wafbju?*O#XL!iT>vY^N2YHs`N%yX)C%6qv*(WmAw'
        b'VAd;}8k9D&nOEaTOkPiU&$XNo;GIk<aq7z!{9axXO_Meu&V?BQhd>W8c)&AZVm356lvbF6AC1{Hc>HjifZqu4e$a9PtH2Lp0xj&x'
        b'7FyUXm@BX}i0TEYF=;2E;`2WKj8bY$R=3Qso?r)CJoTbeM_bwjbX6m1yMQ&!B^_jqU{{(PBElxBJc-Z6S>1X8OrgN$aR(Xe*hY$f'
        b';JRh(!4}I~qTpEqnmpCo@=x*v*-gT*_Q4W)su{xSel;wfUfC&cD6x^WG|5iw=R<UCBk9?XXX{uZWxtO$*tN@5H6q?ir-~7wW66V>'
        b'k|WQ(=gG<j2wRkBjJBt1b{~lCY$OBA$J)_tWr6=1w)Q|^*_h_z1MNzvWZ76d?<+HnvFw36oz6j-#a6fA(}G$mKU|<wQ~4c)<`o}X'
        b'b;p3i@m%RMFiEOqQvM@7dj&4njjnm<Au4OZvj^J_z^HB%TIP(wh*rH$@RKgK!D1Nuc?6do2sylz0@X4h7JY^<`UfaV;v#x4loeLJ'
        b'&KHGA>bd8avYRH#GD)C4hDKV@XZ~kj+#-kmXWz4}(&t^>!atM|ZCi=`>=>E&L=B(5s)b$YW8UG^4ux}OhGubdbsfbp5vyzQ1R_1{'
        b'0x6)wG`pIstEt>tC1he|;^}!h1}|go7@i^6-q##_DhKP+2=X$0H09Q18w(Z2JbiW@DV{-~h*(XzY?SLSk?uUbxlm~@jBpl)v)R~#'
        b'wtpg3d7GP;%FLpR^wiv<<khP;<=yMcZzW2O-Lks`8;W<RiY6BwK(pTLQe?N1emzkXPi8G8Zr-<&eV|44p|mKH6#t4a_o=-PH8+Yq'
        b'8zoNNVux_!{FdrBsFQmI!9(xcg!wa+8>4;pK6Odd&J7zVRcbUF+afLk`F2jDpd-%}h8qhb&J`-NKIMusk@lh&8rZv$%#EVv!n<1V'
        b'#%-daD0;PX>dv+&R@t-g+G0r*#XfUj<wdC(%rsSt>e(Mr41dNEMd$JBKW3LT`+?Ym!?_6`lKzjm!fU?zot_ILCuH96mMj{tA0^x{'
        b'n%%@YXu|s($dPh9lwubXs^}5BMk&6)6<+Ywzb$XDd^O_b4)Fd0%NU+*WycPb;{!VE=z;QcT(NLxK4G4^b5D_~@Qlwbu2G#Obi-KB'
        b'4+paN@At4b4wU0tmhANdczuok{~`SMwB5G5(DUhPFLTwY>xCyf1sk>~no8Br2`g&Jav%3cX}35_Obk~jt*q7hp4Ix2RY*%Cq(p2f'
        b'zTL2ha2Ce;3S&HR5~n8Cr-|8<`hnQPHA?7Mdtppq-!;1?2A>3w62rTcP{7@%sH=-uNC;u=D_!h>Ji2KTI~F^>(d%W~4nX%v){){G'
        b'^k{5U9RSiC63_*tD8`|QQAJwz=mB)JNk;>xM$jelZZrIT`IgsxPcn=*&&iQs&cvc=fxWj?^Zu)TOVt(K`y<|tAOrKpcy|+#`mB;|'
        b'MNGv&D@YeH!MiLxp9o84%3bSmW8E}$=O1OMmdEpcXtt}w1){`Dr1&D?S&v_x^VSE^Eg9pB?O7=?B?#)L>b{+2863&m)_g+NErR4l'
        b'm~2l_?%qttptzUmzL{n5j|5XKIhdOFv==JM4v^wa#P+AX?io?QQoNPbXS=_d{{&>LD|eGSeXV;&tf?>>QqF0V-e3EMt(1CDX;SK&'
        b'8Wg<^>aE}O9>JR^c1^@NP59Mz<<?KFLyD#@byL%a>OU*3FRAT$dOFr>OK;*Y3;Omy4+X11j#omzTYZ%4U6HF3a#LHo*c{)fk^{q?'
        b'%3g<}$)P?y9S6HFhI(8I#I#LX<~&0>r%6{{j)ds`7|Ol>i(Ws~G=$gjdkfUrm!oWHKKK6baLz<it|JQT3sf&u^q9I0l2UxzZN6Yq'
        b'H6&F~xqOmc6P;UqV<=j+m-a3{z@|0>7i<^2z<_g_Xq({x)U28;*mHS`Pq4O8YWaK=`BJH_+6y8sw?!TJ$0&qMT4Lvm#L;K|U=oT`'
        b'EzjT(eDt<YO8^65kbV61UAfCBSM?^<Ga{2~q2#jS=pVuhB3w;WZmwu$ti<Gcf<Ljp#1nNn5>Op|Cc>l@xV%(uUNCumFu5i1a(IF8'
        b'=rdT>N#&YEE2lx?@AyP_hS=mHSZOnauyb!WLFcXukp6XqQ%Eh576|j-i?Y5563OJ+n!8*PH<zx--G<lW9m1W(6g@Tj5}CVF(fgvZ'
        b'K=|ZO)hiU%73w7EqrzN=f}Z+W+V(3=?iqJMyI>eVi(IZvu7a|r7nMLQJ_g5UH?1M;LW+K^qJ<iYG-XhEXOV`LFu;}&CZWh7ta@hq'
        b'So1CiDb6B7M4Y8-bL)2G-D-Abh;j=Q&Lh3Fl%85$P-aCs-0yNO9`mC@yGCJRiRu^2?1c)uQ1o*pq8wp9H91}6Gg24xH%;CCb(3+1'
        b'PW1u-ybtd9<_Pn;nm%4TkNp;>YkHH{NQv^#r_mI99V5&-L!yc-j}_1|+Xr5L)GOR9u_sJqdmn?UO#()z@P69FHh9rZ@<9`$jZiT}'
        b'X#c11qSu}9fLO!@l5ui^<m+n|Cvw1YF&$UEqL&WK-Mynacazu(s{j5TVCF=F@{2FZYn>Ssh`IuyeSeR2h2l{m1mr8AQRRLvM`(JN'
        b'%gt0Q6heTgSj(hWG#MjzO4gF)O$6J>H|8539czpy@QdjbQj{aywN}aQ;nRA(ZYnac_!=L*ZtX+q8@=_Jmhus=tC^P{QWOF8%XKe~'
        b'q;K_sSfJ>c0WroEsN6cCrwl~}<#v%C5g#cuyPDG9@vbZvnW&2@k#u`e(}oS3U`PaIhHbsi`%?2$GME##C@=qcnY^{lFjFM!rfkTg'
        b'mOS{_yxezo<o&kUog-YijxL#DFI^{Iva;l1B6bC=y^<pFl68C_sz|crWAnp=>4?BgU94&?7M5O+JeC!TaS;GO9q9bl5>b{YUB<P%'
        b'#lCJ?qbTs^DEm8Xc_Tj0P%O-QqIsn_C2wAnd8%w*d7;6}rZ?ltsiJmWB-vjz2j9&$L$FBho+`tSJ!~4`TPm?A@)Eot2uz~C3{7Pp'
        b'Xy#)REvAiXuPvd;B%$+L2(!L8&jd9*WO7Y0OLF_}X<ltntW=SGjL*BY8Tf`G;CtMWgxO+>J{4t&a7%J6zaR0ceR#f>)Lk9r@upf-'
        b'd5R{JD7r{D$wbN6xMrv`t~uDkQp;3he6BlQ<XJ!BP2)Sx^G&c^`u)w>qNQ$4xbBG&?;JiUaAlP5?d(nWpHu2h8l_nivGx3dM-;i4'
        b'>Z|$6tsk$>RM<7)5L&R{Lv?`?fTR~;h!q_cu}gjY-U0FB+Pl*)Hkn)kH}wKdxgOrpNCnIz-nd`|=YtirohSYAT>9rt?)ZocGSaW%'
        b'5@h##R*!fi_-vMQm@O-gYZP@;y8EsTzo>NfDJr+^mBy~{u;M-UUl9MA!^;T%+Z-!t7T@4dZsA7VG%o$bei-GupaK;~%K}TUEtLgE'
        b'MYc)aQ$%xwG+8)_@NzyvFspCeC#0zD<GyE!d$e+b|4ymSsLw5?bCzfCjLiw#^Qx*upGQ-)>Yvnx3p@Te`O6!=bCZeEyHX*SS)Z4)'
        b'oR+*SSx9gE)<;LKeql$%QbM?x*c)cghQYJv0-5#WxEUrs?Pd2h!5UqDeH?pqV08OeKIqYsFrqYO@`i@w)$5X73pSY-;zQyaKlgP@'
        b'`&~5~_NXDR?Q#?E*p5-19f8PhX`{rpV?Uny6#Fl5p!{7H`Y(<L{T4|D$;tOsILWLeA~EfrA|ol*5I0R>2~1If;eSy7kJDF#|0!-W'
        b'WGPn@MW(McFYISd3k=2w{XcSc_XUiPhoaF*gB6Cq&5urOf5z_qYlU+_vt_@*c%b}S$aD$uYlsTNvv&983TM6M=^%>z_y&t+Log8S'
        b'|BBN*6@;hxhdIsqARO!eoYSle!t?!SInCN2{FeU{PE#0!<NP0Tw%_ibskgIRDj9>3@So%~tAc6!{3kfg${^h6KgMa62jO@9NBOtw'
        b'mhHDQ`uQeRTFCyiE!ppyqp*J}FyzGW_7B(%+53}|Zx{+>`5A)k|J7t@#JBG4)9|B?2s}zn<a;QX?;n`&zNQpy)Bj7pIs0kSP_Xmo'
        b'?{eM?VLCe5US<e;kAEQ6I!A3-_})bNDNPeCwJ$wr)9rVDDmWMRP}iSnIsO0e^)7HxRomnEdCg%Mjyew<d0BJLFfgFj%%C!w-OG$P'
        b'AlkivifDB&41#FZ*Ob(X`}@uu3kJjcm7x-l$IO9|;iW)kYSKk4BBOhK)V<}cn^}}ume)!R)AL{Z4A}iWKL5{0hkf?hd+oLNUVH7e'
        b'*4cZltloXPYaqs+(rv4bkLYawLmZoYkd!A*xOKv&U@>XfU;MrGx;=Z!2Bz^N7ph~u4;`J<h13VDTP;y%IG-Y{NNMp+lY0ChL!i@{'
        b'H$#4zSO$iQ;MMX)x$8?~Yh)8x)+((k|DuC@(sB@fOdcJ-VR=aZs=0k&q921++@I0=f0PKd`{My<sb9XZcMqja!o0p|{;v;uvyNmu'
        b'Hl<%av-~DVYUmDe){)6GBbN@8Uxo?eiG`*;RLJ?!@eQULs{H)bNoPnV3*`mTD+OIlMy=Tw7XK`oKRF-}3oZHyPxz#y%x*ddb8**Z'
        b'=RR|wdaE}y1{+|qnP`)DCt!DBfyygiSboe`uQV;tSuz(+`Wk*~vVT6S3OWbd>i^Zhn&XpY_P`j7_x-=d0Q8T_6@<wZU(<KM`w`AB'
        b'O`8D{`C?RPY1#yh)O1e5xhl0)e*Qne!23So0LUxRrn;T34*bMtecoBi2SZ^*9$Q|iAxv%xa?A$~Z1&)$kcZjFmNOGRmTGDzVV@4c'
        b'e&&CN?SJ8b$weWrRLRRX-3nbm2iX}0eNX*_3*VZz`e4)xQt*i(-?)4d@A3oXH-+dkCXWfKfY5zc;s*6-%^AQ8X839lKXC;S5JL<~'
        b'%IXRJfJuO&rru6Glw(Sv{5^fWDJEYE{=W?%YNKcp|IML!=n?<#d00DHrgvhlKK;MT<VgJts`%&zsh`kp{{hkDr(B(?&?CR5!Jh>q'
        b'omw=tKbhbDtb8bWDJW=zFVt>6f~pMxFOU=lD9Fe&il#uR_0NVuDJB*QWgk(U*m)4jndVWUa>x&I3IcAD>R6H;Ohiw_1bHHQzyAQw'
        b'@$5?nbs+s(M)O(Yfd&1N-%EIBJRrckKOfX}!n<FNmEY{s9WY6%jjm3`h8^T*Er)9C-h*gS)KHMVP>-|o`$B639#5y>sNKhwhc4-%'
        b'HK06j8U<*cE3N;TcWpy%#ee4Cb2pzK+V{vul}D9)_out~%A<1rV5*CERW4Av*B^9of=+L{z^jstS2@*0TwwpMY;wF({Xn8MocFJ+'
        b'R3{)%ybxQdevlXZmEP~!sDq)PhU}Fd%ypU1eFT~BF!pkf#ks)ZG}Awbta7r*7oj2r!&gLBF`4;kD6_EQ(!~9Cwy);iJ}#e1T2mi2'
        b'F?Nim@meU>LCJy84NG*L_V*~=$)$0F5uDCchOV6=d)K=?79y%dGYxd(_lP*s)Tzu%#sqtmMIB*pJ!Lt05!ig{A(_Rex8z3T4E4+='
        b'w-|U+s&Z6g$^9cK3)2vpq1a5MJ=1;`x4!D6W-h=tsPgpTrCSc?5sn2I&pqUNi~>%ue!E;SEVTe5-&tGWQJQZYaH<<XKQxsnT@^Y$'
        b'w*i&hKr!;|+rzdPmNL^fKVR!rH$c(c9x=OKxfvE$6)KlY-BYT{p0Bi|-(w-(u^;?2Ek$Xuzhl18YggyzYOwMj(w6A#x%qbWn(P!4'
        b'dYQXMS_uyljKiafC|UoZLqo>vNrMO1vB{YHeBbF_(nh8U;~E>`ez!+D07pszF_&p@VjDKYJ<^-jHy*lZj1F!Mp)x{|!E*9K-r;e_'
        b'n<6uR!xr=B2b|n;Q;E*$TwZZPl>8W!B}C~PcQBR`<23eYFB8SvG4_cb5CTGU#`YfI?TU(<B5cXUuM(V3m9g<lw(|fC7d>$%)#NK1'
        b'dx~0QuWoSvv4<ffDm^-3f9F6OZR_Q7&>2394KMxxAk3|9U|03<IL6xtChh19;cr0225=}fc9vLV*Dk~b9A}rIf>@`Xw;wmWOZ>Vf'
        b'GJDvA2kb^(m#*Y|WL_K28y9ds+!eo5=PIlI@cN1fc2UoQEru`YIn>OnjD@}<*`XKUV?WE>^LzRQ40an5$9n6Piyj_58u!9$Y9?;q'
        b'YifPJ50e5&_<TS1cB*zY@TV@gp0~w%ws~aaQib=O3&YpN|L41K^zQC`vY9<Vn7Q$#Y)P+W<rz}}r86jV79P<4o#x|9od<8Yo|7TB'
        b'd$NTEAx{`f7UmxOJ{u@u<(Ztdy_U!`Yq`eUup-Ug&z1f0YQYy}_)+YSSH(31U=4=%Fw-quG((tjcRnbCR`|#>+4(Z4j?_gD$Sf+8'
        b'RR^G;=TS(2S$W2}<UvE3Xpt>+t~^tIxBwbjvJiQ}hB2`eVu4Gt;!84v^w0fWH;fBIkeQhwzF}3*77}X}>^I#U$LsDx{*+F>@Ab)H'
        b'xGNV#jC~;!PR(vlLATR%ItpD@fjTEHboUV6*$&P(@A!h6^WDJQuS#6{?7`coC%JV0Y+&OmlNniq_WTDYF5VtKxj(u!y}&5EQ5b(v'
        b'+~YCToa%;VLIxnT-C33Hliim5HN|D&6KAl8x{<F42S}0mvcBWp<rlrN4bZqQwDCUNz{T_1x2S+44}ru`k4#Kx^dD|mza^4~k`{{V'
        b'5(`q0#Tkv@!wrEa!hs^Vct>xS6!i&tN=Ext03pKra3m?hwmm5+Zdg7Rdpj_dp4``V1IZ@V5f%4h9=X^5C<?>=8_er}c(0YH=)q<$'
        b'tz58SwkFj|IO?#HBZQ+Ciz6#j7M6Gj`Z<i@D=iTvr6@)rL(tPOjPU{}^x|S--M4IIxA|5#2!(=LUVhEQnS7kGA_|MMBu1^Sv`}$s'
        b'`nt%ETx5vrMq+rUWT)`@I``HQ!<AU&f@O=&B3QMc3B=5HLek;KW?xIJdui-#8Kb_QrFWQ+g?Q2Dj5;-HXt_EuilF}miU5#62BTpV'
        b'y4Kn`3gk)fYvhB>zY_IvH&)qC(3@b44kbnbb-V$UB<a69<g&!^FXUfHh}j!ekH%pZjKgPuPsJ|4=Mm0dg<xz4gl2L69Vq>=$oV}8'
        b'#$QCk{~+>8Y(No)1Rp-OiSX&EiWMllynh!e`xGQzKxGe!#nl9(KAcQc{6l0=Tn+TyQwT#1ZG(npTKpGNp}S8)g)g8&MNnkt0fNuz'
        b'5-9qx$O%yZZg?xk3DKy}evzF6Z#NEamcaaFZwSW)4|s(Zl->ks9Vf&h99BZ5T?mI-k=1pBc)+zHCy2x8kncxBoCb;Gz&<R(SCuI-'
        b'7U4^n_=*C|BAiZzS}%*N2Cc9PC**ux`3m9iitef1{D*{BK6BWPLP14z^LnG!__=f&$mc6#G(LT8g-2wmZbkuBQ@6+r4->vNYL0^5'
        b'i8|gx7}gTLB&y=SCD&cIy3h*N%Z8st4i@tXA4kzogWmU(l&_O9F+R>zQ6{>tcJW4|w(es=It~skVPu+5SAzlvJ}zSJucg<)^O98='
        b';SuFC)>f2=?8UB-mI72$N;sS%`%lQg1tP8d8bC(3UfJ`g2uH*)Q9wn(+6sWj#EktO<}7t1QL##7&q&A^sES;KbMb$H=*SQVev#x>'
        b'>QtB4_$(8($5@Mwj$rO#cwR-{65S^u!RvV4>J1TwO$02>>&XN>x&Y@iX!kgPU8iHI;YFhRC=`v>cKlTu+o<7hME9XCDIF`F?RWQ~'
        b'Hnbh1oDuOmhbgqrS$u|6FF~8J#FPg?J0CWHc0N6Ud%DCz4Bv|}q~Rr*DOoA4{5XB8q@>4fMSodP)<0$I&`?;22OK|%XzINv7ENMG'
        b'%<K_{th5X*(j>mJ-6FK4dS7M#++`sSReS@*E}`mrEEU$(y@)DOy?fb;5S)V!P||mX(oqgj(p{l+v;&m%KZVk<4p7pc38fb~KuO;o'
        b'O1C-Q7um8<I?i!MG(Xvuthe}|S;$!kEZ~s=GaG&v#%xolNO#4E$ZiOwdn(=%*^*HDK*bR9xxQ$m5{Bh-Eb$0YF%OHg!qf2USfX`B'
        b'2_WAMOj40(ol(LQ75g#fg~ZnhM<rI`B<PnVIh#QiiQxbgS27<~dcR?R5A(Df2+eU*Ea@j4?O0q?rT2YyX&0wn<M=@=86q6d1590_'
        b'^?u$r9oak%NPH&<nOcO%VGNl_1a=WZk|Wvz&&qVkO7y{MHZq+IzY1+d&d#q?6ZEGdn-VG&2iyjm?LqZhvDtO-64^9nhhC;RJ`j2T'
        b'XQ-{$Q7>r=$kMA2tbTy?$fBF5+I~n*Uvvp-I^Gf4nNlzG)G+dgU2>Li1hC~%=-rUWYP*meX{1~o)agzYi03{|=W3(SZx=P#sd7D!'
        b'(!Czla6SeNNl3Q<^x3?BEr6)#6Iodolgx9=T{UB_`zTm_9ZDD40CY?iD9U>{9o+#4yO6D?8X&xY`r0P4H#-MlEgm16O>pQ&w7#N6'
        b'#CV|%^=l8n&*1%IsI5v!$MXI!P+P#1E_X69s5AEiR;FPu`bH>(p>i%r#GpRy7TM1_rIEVFF(kboKrmlG1I-J^5uE2l_QOsDB~eE6'
        b'A}{;};pTyorx9*{f>j>^aJ1qXpu4|z^29p~a%MKXO}tvCVmO!E7N_t9mAWM5e{>Th1{XX5*V0vNf_j6U91%rt6x{=zHIOzw<V^y$'
        b'Ms0suAw)H--$*gZP;&jxgriX8qZ-;T5%eELCKEu=kBV$>2!j}Ut;qIta_X0dS0ml$Kxb%=WrL8H?-P{lcRjosE58OKPHzy|R%mmC'
        b'en@otI%`@d+hnQjKNG_lsFm%Ph>9g5W2_hx*}6_()5w7GAft9A@2vPO;9T1oGO0j!KP2b}L>Fg+?r}=M)uXI<TV!{^xcyGY$>_PF'
        b'yRuU-{*H?}<7<^|x`{}IL&Krd{Wv@u;p&oxIDv8`0Sl1QEagZ57SM@^B@uLK8IaqBPKn~4qlO2e{jE|t1LcSl+0C8CEshwGeL~7h'
        b'q8u|s_A%(Tf}Sq2rJ?beS+P`Pi=_hbGJ2ZGIwh(asMsL73p#85+6CzG#^p?mE|J<(r(`04YMA6bUA54r|E(@&Da@j8Uo9kI0-=k{'
        b'F4wW0yCYCMY&KiMGYKK-^2q3V)Td?8{=ev-CTyhs>Yli2Cc?e7bHc5}d^g6(gU%`(skSlM%T5g73v9(vKa)5$x|T6Ym)JBoj^U4O'
        b'!xX_Szg%YIC^Q|$tD~4`psJ9Y)zO>g-*ht3k{_j6Sk+0b_4cAn8u{ZeTRWM|NvHE~IKBay0<}TfD6SA2Q=xVeV_ue8fCB!Ce@~oo'
        b'f2_y6p@$hApn6DmX_s`)rMlBY<ws`5SCMNpOZ7STblQq~9$^M#=nUN-QIQ9s2+HW8+zQk`6VP@fL+a*A(I+O)iR3xS;;Eup>_mo4'
        b'4b@(nSX_3aJ0|qx?GpEdOq?qy=2&2d%xvrwd{ZoX5}onL?6H#7DLurm{vk{{>i9+G<|2Elb$-p&j`DsUnLTyL;G#6Kl+L3oKX2kF'
        b'#H2hZ>X0dg+H?(GBY!x^M)r>68~kF2_uz;{{?48h<m3><;LLX_eh&Hcp54=TzQZfW8aI$~id>dJ%1LtBJ*1o<muX2kPA;3u&stui'
        b'??INv$CkU#c6g0XRKLT_<c&`a`QJqGU+<n7VMjVlrZS6tB=K{}e2XqF6p!MoFaMh-Ml1(!nUKT75zshLusU>}@h=@cg#81;9x3-4'
        b'mYL=%ZCH={wGMkEW}2&GsEla2-8egKu_-NsvgGF*dgWs=GVMytVp#U84anWqA%&!#2?CJIRKxprm`qfqIz7><;(hBX)q39dM5Q_@'
        b'q?htOzEUmYeZETX750bjyxKeLPu;^eMU*~w8}z5)pG5Zi?mW$H_UrE9Ya-<2t@wrgsvFcs*hk%aI+T8$rF5O8khByM3sej6!2BD('
        b'-b?Kv0vGQ1_(8r1T|E(6|6B3_=7xOGnhPn;#|LhUh#ngV`uAA7C6@C&0qNlfK_cG)iHhGMZ^4N%OBdxLxA})q*25T*(?PB-fJA3v'
        b'!{_Xl4vsTwh1)>kAl?y}5eESeL0$XyEY7^XqnA@9>q$E{oPeZn7Bf3LdhM#Toi2@>k=&PU&3UXN+aQJHz}AOC9iZs;%^k=q&BAea'
        b'cBe381Rm5GtV;&CSkfsImyCHE>XW@gk?7oLohBTAS1_rPxgi~tyTC!wWTS`EEXC^-Skx(0LzRpwxf`Hf73bZEWu=gd8N-#I`yTG}'
        b'|FP4sKn5DquxP}4Eh=_l$3l*@PpKFe&Ht<0h=-h|nJc<4*i~66kc1wQi*d851NCd_Fk1C>xOq-T?^0FPVhuH|02`M&mSW>Nxi<8{'
        b'kdLI8ELaUFxsocs$Wz%^befKHO99KWQFm>fl8uG}6kxyryJ?2<JHsD|<{2HF=FHxU1TZ`!K8u?ePRW0#SvmRc<^Oz#)1#7}&JQ&{'
        b'@^ueUc{G;qzJM%#8p(=BRG2Y0-XRzlIJ7V&19<T#BBI2Y?d{eWM4mAjK(@de5y8gH@{=8*(?7iLP-V;p-uFgj%u~Ftv$Ej}4_@<q'
        b'aFz!ok6l$k`7nWb@ZLI=`*N_s6C6Rr7JB{?J%0!yw+HY0O*hK9h;lBu4QPt#pTtnHk0FzkqtOEjsQ4aoYd*XS-3Xi%z}K9+n-ews'
        b'rI=`)73Zl`uT8W@<mLY49t{e{O!_l14&<@l#~ndJ+22I>FyyYQK>p5n|E@~4Ezzpx{ds5{Mnv~tg25xw*&@lTxd53pC85iGG$=$p'
        b';-E42YfxPc(yjXtBvcj1C$YO9UKU`A^L-z7Ajf~mWvaUe@(QJ`BINt#_*oC1V3l3ZG?qlA1__VgYjt(kSvaa>EAsbxcqcJ@4^~oy'
        b'VoRdSrpQBBLjK<m=SL)z$`f|H7rIZ)b5z2P?CYLr3m2Y{KmTy4F_=4c;Ld;|NE&Kx?pA=#&eWzx-Ir>;H=&MUUP-MRHhKj$M&lU#'
        b'1=)PpP2eFxlD;jPD}(L}T^90a*yn8?@9<Y*!p>QYH&H`Wd@7=8KzE%(exQQ6C<0RO4vAyZHCgHG7RGK5g18mtJnQ~zm*Ybz*5L;o'
        b'S|<)DmXs<5PCiyMr}|isFbbWmQjCI`SB>5vL5KVRvZX-__e9<+k~71=9awEsFwDYjMIY`+%<h}vTd2!u_{{cjkmI&7Gl7*4Op&h7'
        b'%~1q|JKD3q*eTe)Q(t^*g10{eDj_z?TVK>_WY#wANy_>h2t=ACxsg=jbjQ`_Rck#LJfR=!Tz=%+T`7+f%nU(~<-R2rB<Qa1(s(r0'
        b'mjV@Y=7d#0W7JDQALhs{Cr7JS<!!l*8qxBiB~sqKqHZOqh728%a$2uSPRdu$p-skG-4-1{$%aItGLO5Xee0K83O_!5@Oc$Ca@7;b'
        b'(8-=HKHO-GSoI)XEm-A76c_42T9*ntGe2^*dP$z<&hVJ1UHmg!-eo105=)C1b;W1m#9iyI&|b0))MokQe)bt=o)LVA;Pp>%KK!@`'
        b'_WVBw;ob5~hG@4YFW=Pf6MJy?g5bmrB@XHjp$AU?6f<-ACXl&WUz>2d6_N`E$itlK%pbZ={GqGw4_*F0c7=or_w9DrQXAKt7F5Z}'
        b'r#Y3-ngDw%0?{e_y0=R4E>vfJ*L7k=SKo>*|L?opzelxezH8@`p2)M}yyPr^UyKcqhMz@7f#~5huS)iu_Ne+>6TC^=5XfUkddLgm'
        b'Sl;+;Iuy?Z;4&kLM^tBi+jZi%U46gp@-OIeFOcxUgS>Hib?E>Zy5#LX_bZ;AS36Z4LNbmSAcgb9ulLsP!kg7~Voq1zoG!ni%WaV0'
        b'okaCN?ucX16%zM1?daYUF+c`xOkfK%f4X0l{QA|`RlIQ<g5Cd5LOR!)clmZmZu<<A#+@P2sp<0wg2jfJd)nikwdl(PWZx_U>eiVk'
        b'Q(Bq!O**Hoy>Dt4&~|n}=Wa&D-Cu!(&qrbWs{DW*=M5GV>Ca7hWg{RyAs_kYL2<b%eI|f%OGb**q(TA8#s5d4V?gB-u_%{}<Xq~^'
        b'fBu3Do8gRLWIeLjRe>2-O9DS7I+e;k9pGfRAVPwP34AK1I_3UvI??Un^J4XzwvKlHv+efyd&{M>=Ktu-T-V*Ei>E+_;wkJ=!nLBd'
        b'aaDd>^>pNUrK~#8PhtN5YVYkWKrS=Z<-K@&Z149Wx_!L8hk&sit!H+PU6~k7X$WDoTG8d;ykmDHnG5;PEY7?0Clq+HN#PqBtd3`h'
        b'B#J%K39D6}tEN_4Cwwt#u&ep1U8^pvf}fxT{;cghqIj)-L*5UR$1?k!wVq(q-iCW>cC>qw<~FVg$_JP#7WwgJt9Jpjw7Nw!+SODN'
        b'Wwfm2KHkC*`NP$3^@IWHk1Bk72O0S<S*0a;6?b6T2aoIcLc&{!zk`o0or8QkjNo~@evb9f{}czpt5|qboGImhtBCb%(Nf!w+<SG0'
        b'YS;D)+u<iTAO39abOClRUC2B4i*f!l+-UlrWEEeD*aix5Lur2~RnLBF^~+g|>~UEIaKh|Yk;j5D`yA~vggc|%X`I`r4H5&$b&S*j'
        b'i~Db=1Mg8F>?3LXaYgmU*j0wjRQtS>b3(@Besxr?Z%6j)O6{{m$hRdEG4{2{(CcG9Hsb5m|1kEiSDyt4C|JPb3W<Q<qa<h(ccR`S'
        b'rPJ(RiW738+0dS3v*_78Jua{m5DkcnzAWA7I72uHENFw8a}?TS7&D`d(c}&_V$;*G75+6jRy=>j=m%EZTC@PqBSnYgTy={^ZpBNf'
        b'{1p+Yr+2D$Jzpnhi1pEgBOXI?#>-RLJMBC%lVfF|Ex1x^Pj6K{v&uMK%Y|);L>*flwqemN6p^WY^74?!#>5nq4koUrf^Yg-=lb>!'
        b'#dZc_Z~h5=9L#8!F75P$xtE|+jis~ma4<af^+I!J`|GJenhE!2VXM7MjI`ue?KmnF`zrdxcvK>kt&EJ(>hgAuF3~!Fpx+k%MAD~4'
        b'EJz;>uP=17NL1^f>k9L-ZgqsyKZ?4y24hDD2zMNM;kYctVGZkK<Y&Y29{E2OP8&6PHjGNDWs@A~IY*)gPpMA5J`x+-sT&;}d|_wk'
        b'{sF9oU&M!qIf~=SmSi&Tq|BpE*s=AxXI4Vy)7SGO%-1>&8>hfFfh_y#gi@>dyADQXOv&RE)}p)>plH(J@a7d{fsd<9nOfrcgx$3t'
        b'*+%D36$F+LoX&g>TL*{;61~9eX;1wOVioJ&&qN|KJyIM^y0VHJB3mxiOGIJ9*{AngI3wCz-v;@fylX}tz9L>ltQRD1Pm1)XGw6xQ'
        b'h*HFIpjTE}J_F%(KsGjgj`q}@;WL0;#n0lTuPMX7Cw+t)?aWaoDsh3*{nrkRNOS3GCc}d;YMs#}ebY@#D+3lyEL8<Q5W73`*Uo;o'
        b'M-~vs4%n45@r;*aJ*vh`+hE7+lZ<14?2)<O=#bRsyw32MS53WC-s{pWiZh}%8TVvGc&=L`cC788kqh0Ju+a@Bvn{rSz9P<kGov1l'
        b'=#1SC3RrCV5CyW&;2X8Qy=B$!_K&{5ThaUHT32sb-mE)~-J9D66BbT~9r(b0L^r3>4(WuqNw*)h>u>59QefyFl!6$_!1^<AA%pNz'
        b'Sl*hSy&2^2=i)<Q%ss#i-lI_j9rp(aLf+b+1UrT(OyUiX5=MJAIbO1b7<ORSdDCGhQDH-0l7>#m`%f@ERFZj&yg5hl?LyCz1nZ;M'
        b'Gw;odqO9y;edHqhFbOb9c;uXdAG*#EhmB~q6Y}MU^E3I8>(`A}88TSB0JpP5YQt}XPvt#B_W;GAD>#Bd*6*7=R!!P{I68mS=7&{2'
        b'ksEk{w6H{bN<VVJiv^5S$axpCY#46c$UAk*s!Bc7%TJGDG%mL-bgp5vl!;EOs?~aaUX+EZSx^TM8(Dyl-MEq3;IXPQQjqlNxFNz='
        b'KD=MDXq4=VW<Lo?lBUu>w*!XO{b%%sv1qe?z{pc+z2h+ZpWmU+iWt;-2))A;ryM_v6JrM(h&hR6?`t2xdt^zf;(qZV#ptO;xg}3M'
        b'z;Ye71sz-=3T>4zbRQQ_l{oJMoY0_>hMPBzXZ5qV=_GPu5%>xywEOaCvHjF2Q<SFPIrD043JT`Q4gGxB@{bozKpj)7uK1f9+J;|@'
        b'&mHF8WH`rl(eqq_Ren9wkPt--$76Nro)=3tp!gAoH_%MO0J--VeuR}AcQ~w)y#Mjx{KpeYHzw>jXZYwlV3<3#dbBXDc+QRB>e{fJ'
        b'Hv_qbd)I8W=)<%pZv;NM)9=I0{|x3OWBnw?$Z{8>l79}s>)u`p`5A$#)a;cRwJ1PL#w!G@JIl%U4;K*?e-p=YuG4=79V$JcH0}D1'
        b'srfHj*@R5n;rxsRGWvp;Q1@FVP&qG>c^>&j8x?~u4v=mO8r<OzMbImv2;hR&7xUTN6`13FNRc>BF2*X(h$hoq%M#4-x6s?g*f1!c'
        b'M^sWLwY#p(Q4IHr<_&?|4{(cKFUaDUSmdv&OY+_NkKm&O%;CoYY35-yoJXn7*4R$oSHx)AkKham45{53ZK1I0+P={sl+Hm&Nj9(F'
        b'?VprKVXt~7!0G4a<znocL9S@7vFKwvI}}XXnzWNW5lpH@KdtEJ6`Lb~ykf?O83t|)DEtFK_f6F3*gTP46v*2(B{%+w>Q(uA<{1zT'
        b';>O1c#WCA0bd9<=_g3JoJH7%c@Wyw={B6Vk+$M>2JveD2NgF}hAc2kDb3O1jEM}zRjQs^;6vY8-@5U%!9|a;L69-ZoFv;HII^XNM'
        b'I0evUPHAw<`$YeAto*0mRi^$K@*yAI`>Im#O%3#lx$#Er7$!Ne^YxZ7am=pbgJOSJ45Y>b2jF$|=&St)L?*7c_s6)6fgaJlF_>Sf'
        b'eU+?xNt=X$=u`Jp^_l@%@~xR)O#dtv&%0H8^iHn+USBUTp2s7k*aZ&l*fr@8lMJIlv*qLYTp#XQFLPDMK&HG}qH>k!vP+OBtM_Eg'
        b'Mnk(eK))x8TNv0cI?v)>I&HTsY=exSA$RSh`s1GiLACc43dJMQEjnM^Cf2ME=KO0vlUi>JjFEM=_ScBv+1Qr&rOX43>+SJ;+ICr*'
        b'Lx#nsVcY$K>8i90UGE{CUEQ$d;HR6@mG;~QCT@AmSc}-tEq^j?|K?|vc^R@yf<K7W<Ob6`%DqtzcXlu>)0ScVlkIwdBvxlfB1?^i'
        b'Ff*}O+GUbhV9$L7g?fJN94wD**m5S)?l@{EuqW+7_r1Z*>AIza5rxqZ=%ZuH2~K~nEjq}p3$yEOY<SS_#MlRbmTY@quWSc-GpLB&'
        b'j&7ze#h$INI3?Qk_mcJrpP|H)_e+SR`q6bK$&NWE$b=*BT$!Qo|F&7d6G=fP0@-eZh~UhIAPO?K7&|`B`r8B!-3H2eIq<jwd4Q39'
        b'7s^=Qph6}igDTG>nUM@?Z9dKrD2Ol$@3R<l9}Y~c0rZ;0T&}Xbky{+6^n-jZpws<y$hK+ov<dOgqI<21ppn#d4st$od;cFpc`Om^'
        b'AQ3=9vKR9dyETB|5j4R2r4He#rhFaLx0ek&zBj)X;1!sKoNe+TrvZ&YcOt?e;n<Xf^QzHPu(c24$XsL;64d`jHUP)%$upbZwp%hM'
        b'@B4k-&Q0F^^AbAP?ihLM29?E0o7cB_efV9=dT*VICv>4Bfav6fT_=qv;6xIXhLD*bX;Wf~Y(26cqD(s)84W>^1icMgpu`^AhCRTL'
        b'p*NOX!t7`h^r+8PA_SttVmyiV6f*N1jMjkSZqO6_G0DI7kecxSr5%L32T(8X`eF76%Pb$~qtj0-jr}JcXzTZ(i^AwMI_#MtC(ibj'
        b'c}O-6?di}#b7TMrR0{bzYnxJrns*>%Nt)6)XiOE;&xP?m3!g`%`NuUdM31(G;`b_vam;WE6h<AEY%UIHa16ze)m?^SI^B;hUT{5U'
        b'!{n!Qm;yTD&PKKJ6FTzp0$7fsO)#L|b|g&3Hve<GXKVE(uMtbECyiUB*zX|y&jt?XZa_Wk*s9%lCrN?SGYM~Md=0)R-n5xoKlgrS'
        b'I<&1s*t3mend;2=v@~jaBr*I5mN}HxH{L^7&msqJipdWKwyo{?)M_=AR~(T<`5$j*B7j%A!vm6~lNiAP-7C~5z@tD*Tx5W(_E+}_'
        b'kwhOEz+%or@7yy{Uvh@q;8nI^yh9}&*q26*qH;cI)ljmK;kfYaHWUkYKIT#98?y_j?JvtsHB@#EwK|&1mCJ!Z%D*gFrQEzqmzyci'
        b'7t#jD0TIbbD!L&}6dq{<P<rT_QlUdp#bYt$I5XWb4McJ%82A=M2q>mK|NZcLu!Ew$YHUOgk$+YS-7JCWrwM_@1JB*i;KZW}3?I+y'
        b'94B$Cu(K7Rn@$M{&q5uT3V7c!7v4L%VTAwxV2%CvU0B+Mx9%b+g{~eR{=1kdjNnoqD2#5C?k`6O{uhe%qRv#t`9$qAI1>^0<7_NN'
        b'?@Jj3rV(RGuGQ%ZV1-ZElWa^o#_5C9@n@_GYwdB3D_4JEo@#B%)fD*2q1#WRzo{`XmKb^E=TpsPtt2^@%nBpP6f#SW?0A0@8Pc*2'
        b'OBH0Hj}GSX{T31)uU>Gfbn{&RC+Elgx)c{WjXKX|CACGjZP)f&sPgI`ER+clOVor};<eQpL(2Eb^PzZh3KU&94^+j<uckhk-%5tf'
        b'B^QU0VJYNdxvO7);Q`gLl;jF1cq|3>nq&`@UY2s&166jd;$$mFd1D~Yu3*&Ml9dDG^3fjLo!$z=`lO?kna+hpF=Pa%o40cgX*F;9'
        b'$uyTTaY~Dd9^_QnDN3DQm$RXj%b_{LZ}NyRM(rNi&!v|e=T;rkUZgFQv7FcGl~$HZH-4J}wc_Z4B4wRTyI*FEE<bD}K*_pbQE`;9'
        b'fK!?{9TZzW3KFQ?UWmK(2nmbfw~Sg_bOn|MeMm$+0ydr{E49hrqEL)j4;~8ay7n8#1(EZuOPWhx6fNPp?M2O&8HK`(0w!*N_8qS^'
        b'ZK@r7T{$>ki6VWa_<K2>$)dBQ8}lyT9R4`8W;H}Oup10t28t7kYke=Q*%%F>P%4vQQ57#SW-G???U?WK+Ro}XGdatfV#YCrZ{AiK'
        b'$E>-j3x5QD>q?_mmp*`z=QRY~2OL(J4Dt=;zdW%nQ(HqG6|-ZY83pEQSZ$^9bF=e{s?&Ln$j%>Jv!!vJkuzBaC4I#FgAn59uz0N&'
        b'^lj2k=&bgzbw5n_07l<G_vcbr!gPW*U^(me=gaa939Bd|<C#}M&P_-D<sK2W=kGWv?8!gwzmTWexa#UE_&L2wwRUwu?~j(^NQpWm'
        b'+CXH{nk0h>AbjmE_eo^8bS|OtxsRWJ<`whr_UDto6z9At93?FVzHnAsL5j{&%!7zIdeXma|MF2?zs`La)rr+}=@<y0^uI(*`|1tp'
        b'8-hQ5zxxB!eOihcgz@?keUy38eunUpCahjxSueMc<%t@CweAPpiA3Ygnz{SE;n?2b_ZN(+UEEbpRdfITUEFC-m7HWGwES)DirX%a'
        b'e)6UCW*OJORZQ+RZo_`gcgHI)ua4&ArqG_LJ6*=!v)_yE`6osvoQT;!5Wek&dm`#DRH+&~ur?Zyoz*4icU4z6admQCr_QJQ5q4ua'
        b'=cOlOi7^T$_7jEapF2O|+BI69)MZ>!^4yg6D24lJftN=`cwAjOc{RQ1m%(EbcWe1v8g@EggYGpAek8>$29D-h<mFloJw#v@xd|K9'
        b'!>Ueg%!S=|aDmDjbq|@TCW)~AQq`tgz4b~{z3!t+-h9Z_)Ny&8Sl-i^)ovkm+dtP^<i_$-KICS^sI8|M0xc%UI=UycoHC8j@4l4+'
        b'6X%UBcu=utQLPu=Ug?i5JS~Ck?XE39XR4Q0MW-L#rN}f|gJGY)YP1{G9D%QPb}?!cPzjBluZ$r;cw+w=fB~En-nf806=0%`1W({T'
        b';~*o~Rqb>kE(v90Ih_l*DR$i`V^4xwS}w&0o$wnYy-BQ#a1R7{d3j<K!M+}t{Pz4B6vi6+BRF)X-Xn3Vn!dnk^y!KR0ZdnxkRQ?4'
        b'AMp1F45vlk1W$&!?g+p;UXG29=qhb_JCH76xFs@#yDb3B8WBM~FE=qUm`9%&1%iBWE7Yb!cMKW=0)dTYp<9W!L}<Q5t#ZE@V8T6e'
        b'kC7j_<x1KaV*bD*KvN3YWpj21>@rMCiB2E(WL2QRq2py(<>AjfVNM&y%W>X@^NEpFs<EHN-BdzMSPxxXFZx_%SWwT~2qrpqm+Qry'
        b'UYk5Y5$S$5(D!V>D>tDN*!6nAureB7_S#W1R8*+lTVad=b;vI847y&d-5t)`!cDIr$7;a(w!EF6cm8^8NyVq3xKUh0$jomtmHG50'
        b'&>)!@*js>OGo)_e&b#LuyuNk7T6hlM8yN`{k^1#ibA2mDotMO{WK5N8e%~)K!^gHMBY`T>sS9NUkR&>vp(J2$tqX3twx^aF>`-~-'
        b'axxRwNmp@}TD_U_G~M{5{N_<-THm9zt=N!nWbkAW(`p*sI%q1(s8xB5gvF@X^CD$Rp;GG!IuRq~_z^jh9I&yUM623D8pA%1cK-o!'
        b'6m3?xyHQ}Cv&a=`=-7k8p~bBIlDrhQ@t@|zKqi?1^3oTwB+|wPki#F)7Y0yGUPDyxK%xXm0bq~1rp7-KbvC--2z~_xTv;P(kNrHP'
        b'K|&4X-Xk@2?B;TXy9*`FulTK>SEooWK#Xdm8U>Ou{84;Rp?&7M1I5<{IixXYJ=<86sfJPSkH;rv5!kCx0C>!LQA^&+RQC`^kn33b'
        b'>(Dw9blzkf_@mB6oj#)C!;M1+Z-n^7kp=uxBgjpX{jRV;KruyUOxr@^d9O|Ns7<~y(~}fTSJ-8%ZIge-26fJ({u9fEi_;7H<?>Gu'
        b'Rp*N!$_ejLOQVqK4|#XL7sEKH->;Z(THmjxGai%8*httO_J@5<&<PmS4SOsB=3`F{wLN;KKhs~c(tk0gaL9=7`AFA8)Z=5h0JaXV'
        b'kE)jg$)p|9!Bh<yNolSO{}f?6yCQ>aZFEV_0{_M71!-r-K~#iUK;hJWFXpSuFL5%t$wav%rc{3J>UI@S<YwScOXP8ir84*L(Qx-r'
        b'W5;lg#<XXDWC$8IcW46I0wDRq*!v=KPU|=|Ve4CpyZ_-w=B+4bHz8Sh)`#6~viMtZx572aZ=|xLQdzB3R{e=ARJ4Z(d@Vk%7=4DJ'
        b'C%y$dNeb?AzkSBEv`l5*T$xAB%Z-VbmW3593A?n!W2vcY+v8D|c&54;KS{`?OCX>pEz>R`?P~h%FYd!+=leLp9!8*>ArGK70spbT'
        b'U(Z{JqZsShjMAe3Jm&!+8}#(m(`>PRd%Q|Z-JB3dD?Smi(djvVYU>Xp{Qs-1_}q1E@^#)f;!1a=rTv)kYJ}m%@0iPDW^(u}h|~Sj'
        b'>E!hr&p57#6a6%d-0a@ymic+3vbt^r|3o$s(7=7p7giK`HmYEV#X@5=5p5E~&PEjuPuKuG>bNP;VNhL8f2hpP{;}~&_6NF9aTu`T'
        b'Z(vPs`iUcr*_@JFY(&+)Kua6$%Q^02VsZ`3Gm0;t81|ti4eyKYK0ol+(`YwRls}a{u^XY!C#ZnE5Hq|g!gOdmfA**~a!fk-(M5kQ'
        b'`L;@J)Ag3w$#U&F($??GncJ3k3*-fa+l*5BJ*r1G_NnMOXVJ&PQdk<bRL)TLO!=lC)9RJ5d-WjCy>SZn>wZbYM|*?5jf2g$ALEQO'
        b'{A?RAO<#yO(0v$s!`2NcBt>W_ypU^Ks&N)YlZ(SajdZH%Eq-isiB4k=(@<f~T$-nFCWExo8oPY+4rN~D6i_U55<8?*FecMgqJu)%'
        b'yz@uq<`!XTt)MHB?qfcriMf4xiprihZX#we)3Md(va_kH#j0FVSN_qSRmy@@x;jfKwdW<Oz)9^XQI>yQP(X$9OR4gw3reZeC928i'
        b'O+OcGpay?^hP79)iNf5M_mrrzv)4gh?qXe)9*a6(`U*5d;^a2v!%8l>@2H<I#DBfp^rA1MBxAy5j|xhG%2Ykw7aZ(JsbDam=JHn&'
        b'jpovsI|0o!J9Qylg)$cFY#+7Si((jRfqjlNh}F{zb__n9qNnISpI^s<z)J#rXvO_3Y69TuLET(9j_y~rUhdoLFWBhXumZi`Dxm<P'
        b'u>Ue3(6Ko0JZ_us%Z?w%(2*vUZLk&7o`*-BDjBm~wii*LMF$sy!tdKZh$Wv#N1gzR6G5>ZZtalJigbJwI+HfTXZZlPkZEB>GyT1-'
        b'oBnP%e8YCI)k38gq$uMOkm#D8j<hh%*peIO&Q@QR4mNT|;arRtKl+_^*AzZkrj1v4<D)90B_}_Nagv(hq?Xqgk&9){#gv_ju`kB#'
        b'K*G=IuV$)trJqh$Wu;h)EE+naXsQKPLy=tYHM{GO%$wtFon4VBGk@#LpkvXu<i~M4sbCTc(slO5io)Hkwil4PyMbcjOZwL>MQOW+'
        b'Vze;s1?eXHV!|q8sN9nmvg2!WcD7nh-b|7)YEwLl^M`ehFf_tWK{*vz)dY5VU;I?~Q48=FA>kf7H5++oYSRgeG5VYc6kp`HAug@8'
        b'J=V(5$SXs7d}!Ud{|n*DD8}9v-KSa@1#d*oEZzTZVUC4jQM;Y3HN^-yDH20S7S3uXj5UXSe7K@gp(sD*L(%jU#s7u7SGU%zZe_Bh'
        b'((vP%IFNzXTzUqv!QA2FNJSzQVLx~)4KWmjVH3_eT2CBq5kOd>tetlI?02pWpli(LwiYHS_Z-g4Rs#RcyM*y}hg)cYJ$?d3d#mjM'
        b'gjW?Mncw1PT#A5%kz%r>6Aiq~Mv^%w0zs}uhDirVKdmG3)%ExqRUMaasb|-ice%+-tj_?tdM*f7q+JovU)S!sC0#T_GGcFw;G;tk'
        b'<K4PeHlfuYi(2GLkx7kH#4}6xaOj*Gmle-$@iECAUV%{TRm@-%#lOROLQ!6iB2#aWOmT?uqM}Aj@S(Fhj?i~xfs<)3<L;MQfPHK0'
        b'un*NE_I?7LEt38Qb3Y*ifyr29>z&E$EdhX7i1^f^>7j((M}c&N()M^%uJ}hWWJF{ZrxI6kmisuFB9WX@{t9fq+!Ex4V{9ePel5Th'
        b'gaD+aC_}Yv-wWn15%{H~ExpD0KJKK`!b;FQI*ItiFP{nxGgDFE(G?c^NGdN|i%iJ=i>MB7kH>m1_xAo6xF))-Ern0}1mitUTB1T<'
        b'+4>k=;Tov2I#i|bT|uC+Q28;_6-bXIeHQ{>zOBHcgjE>=>0A;w(R>LpJR*kDGrpXLCYlV5BaIHlg9=JgE4*^t4!cT+{%V8DSMNHF'
        b'+?}~#R_%5NDVN#hR9~0iKO#7N)P|RU&`A5V0Cim(bIZ{;G2dY=(sA)L&=d0`Sf3!7dE<2)6{2Btvye|FzC<{-VI}=UMHLnomYDj4'
        b'?T41@mg(BusYxUY%Z9Ss3HBwyRwoP>VF~uH(cO&2Sde5QEvJ3~70497)Am)%gG6DfFBEk?J4F>TgP_Ni6z9iv$;vzq<I?Nep{<88'
        b'c4~|9tTtDR45q8Ggo~`*=SrNr7G2g@hn1XdwflEw$Ot+Ivr#R~#>~0sK+0cRoIaw5aIOn4J|N~jbB}F{kVz#*%D5t|cnyqQ!bJjI'
        b'UwI65F_U1Q77|}1=)a3&Z;0rCU&%FM_+8O1U>Rx@@f_sqCj_=YsJI{95qelC{G&87nej<<63L|#T)HCZ#iTa3Q(*JZn<^sIv(*;~'
        b'`h>_HYW5#$;b48g@HFx_?>H`Ec^`ZixN_aMQK!xN4p8DKMfq2o(eX|N)XYt%4JMEYmv472;k3+pC;C9gwl)hKvd;1eQGWt1rIsAt'
        b'!2@DhDwIs7`4NIIM0vn%Lz$k9b@<*oC5Y{;Nw6)Fh?}4rrTe!0w;_P;dBWz-!S*BJf^TZ^K4RkgfHz*n`%IPLz3BVEb1nTo-Ng3+'
        b'jDt2~I8KF}PkNe31t#6jp0y3D8<xa>PQVghqFAl4hL}wxk;uizV=b%4WOntmz3Y@VB}_!gp@oRstEtuN%z{r@{GymQj@f<qQlXF$'
        b'Y%)RG7UHO-WT=$$;HL%YXp!1;so_mx<`yUg8S5hn#|AM}WHt@kO2u`UDilHvXnBTHCivum_r+9{P=avQ?o_&So0%BixByw)1#IlB'
        b'xEH;26`u|H!C0<nCnDTqAW35FQN-A3(fzr<hxkAE_>$Gc1Lg;tE$2cT?ftg7Efz|VDpP>)kfOAtE5@ecW^1#cM^1~(XZ*fa%1U;;'
        b'Sn|2dP>&c{s7b@S;(BK!dml_HDhGvFuBF3^Tvp7ui0ImU(r+Y7`j@hCEp{SqbT0Fp-5zHf@aNpqEKs=9upC>czp4j~!gZQc>Ec}i'
        b'M?a}**$!-C0cJ#Dp298@feTj{g3E|=L`n|%E-sTOdP&LI!)%8ijT`Wlb;-74{+td!<3O|_vtcb8UJSjO@x^Zu85<_}HBDlejc69)'
        b'5x%J#N6h>Df^U%1W4cad-r8&IwPp*U2n+ye$t`w;VL+tc6hnZV2X8%jwP|7o?eX@1;C9MJhUGZlq%M@G3Y;ztjY(H1{>Njl%dNso'
        b'w|JbOX@Kxmuc~4<n6qqTI@VY2C&O}kaA0S}M}Nv2zd?T}7RsBu7lKyl4L4?N_#Kx398m$7UTsyGI$ftbRm(d2rx$d#1?oljxh9Un'
        b'fFp<4abnC=fx`NyKVtakTSyqrhQ`S_pF#C2Mi3d-9peb<LOA9VOktM=AnhA4FaIO5Cz@c&7#;wjj-R?n*GTlXT<+qP)un;zP;^@)'
        b'BK%a-)6D+fUsWIC<y^QTQ6U3CVeDIwHw;~9qynANfhUPxlg!^XvmH$W`BireFJNYeA1!0xS3!~4WeAFXp&2oe*opIsJhwn%0fvz)'
        b'Jo%OO(l7KiB+n#pdF@VxdvDVup(i@0yZ_$o6)-{m6(jdm)%GBByrEUx?u=(*#?E2xoy|<NH<R$nk<%#28m4f^`)lSS67iN|sZJ_R'
        b'VL--JglD4jH*B2WO0e6SOHRgEe6VpU0{?S;Y!EZty53jY?BCmL$RI3s!mRZN$v~snPt;fclik|nR{{@IhmdFcn>peutwn@YSll2='
        b'@f-lQ;g{>?f@YAA`pJ5ojso#W`#Q!JH~I02s)cua_5>{9{oioDv<ypJ$su%K77?k2O1wx^{10++_>wrBEs^^dQHT@0_$iEavdFGz'
        b'LYG))B0~N_%z3DZA?zRE+~PQnN(%!vy%G~N)3`QiPO~D5yRR76a-ioqiHe6X_Fulx-W+x*dO`+>?#plXkNNh5PU+j@$5IKNvU$nu'
        b'%8v-zhAl%!iFffNXacgFknyPE0Tf1IvBLc?U*UTQUKJgJm3WD$FkpS@&7hg55NKscq@M+{uq3r9B`Z-nW_!a&%2wo37_5L?yCavv'
        b'`(E>5&+Db5j>xi|o=Z_ACCjzX&R+-GYpzp?Hu#F4CKmb^(V>Jdn=1eC>ME5h9Xag^ElI6{3XP)eo+gk>QF?`>=jdfC>+CvA5zMV8'
        b'JX`9V9qM|n%5v8nM%v||l`{(TAsbannBWz|-@t^zT&NKT$kkBnkBx7SDe~zA*afJSGrkD3b2DM7!HSf)-$dJDBd|eezN0pTz_16c'
        b'!yFe#a3~(rRi`Ss1eC&!tAfSaT^HORH#&{W+piP!e~Y;?Dr}4xE*G6K^m<A*qnH?eTC^LNm&T-JP=hN~cG|e<W~jq<hw-Xil^kz-'
        b'%7={V@go~EJCVRiVf5o7qfTmNOMK?X&;%_YD&7duWulWX{9O$3fA$aP9ninim#86z%~(#p57wz&h8wD`a0(2FsbV&UrR%Sjsj?DL'
        b'6NaF(y1^L35k^E#2JC9Q%G}<Rg)H|@GHw}{Y|xg-XO!eJ5&etfv>U@pj~zuWJCERD8-G*yx5kSJ%IZ5=dqJ3Mc<DrUV{ijA<-$}f'
        b'D+8%sFcK%)8~Z`G`qv#h8OKaV9b6oj`DOK7X?P(oah<{TMk6rB+;|d28TxZ0GTKcqU<gB|2=s6KqS_*HJ&A3Bf|k1OM<&we*r|Q<'
        b'PUbOy5w`IQo4c`x=#MNYFB?l2VR?pBmtl$DnCJL{8kobz2HTTO9<*V5BdM=8$ZCwfy-~C$Q!>R^Q}TA+p72TZWTU&GQAjf1-BUpa'
        b'yT_;Vl}Q=D`m2fdH4#R6b$I=RPaLf;bQaxL=Kgo%uV>56Q+yus<4Z|o59#4PmU{`AoAJ%qAh+l-m>;*oR~17?U|3w1y8zYdRxt9a'
        b'g-MFtWSw<%O;uKhwc_96?(n+s#QH04Pm`ny-o+uvRj-Avq30un|A!W4wntGXf32Q9E2q2!wYMqCE0^(v%vEKYafx|5oMOLkNs0-^'
        b'04EME%!|1_JP~u7C$Q=r?yp<w<Vo^+F4X59qET)80u;_nP<gA@6|6O7XP13j9BTUlx{?r#1ST>-?&^fe8Qm4Til?y3d0#+<c-S%+'
        b'*@XTCn(Np%tfmPu6HdjbUC&d}QAlZQMq6~cGAqd_j%$WUjFDHs6vukrK63AcI@PZF3rAITnq&3-;Z)+jOGm=5&-&c6wAvb)Fnz@}'
        b'@$NX-UT-m(%6bT6d^efL$ylthBcA8x`46{LMe>{#9R#3khg$5;dC1hR<wZ`R(Dq|}y)8p+jQjh2$U7|6s9>+{vqoB+^Ejx2zC|Tb'
        b'@IRi>4F6kX$jSKRJTls+)@jgI7sZe|D>`L5^J))S{Eu%yM~3OhixDM1AZ~R2#P-R)up(p5-WERozHE;&SHM=+Md!TO!bJ4Q+~a7*'
        b'hkPT_!{5<^J$^~!n@q%zFA^QX{~2M%*(mOyi?boKAwF@O1MtWskoT?^O?E;y<BMe5$$j4VO_kAXKS7yJ>iXYR3BI!+9Ka(Nzv(?v'
        b'$~c31HR*?l=OX+WjgohFwKg9Mxsc~MO|?~Wj_$cwof+~&2eT&a<3{h@IDGCupo-ADhZG-M*smHn;)^^xrJYMz{CFz$K*dzd+_I0;'
        b'&$-Uc6UZaQpNWquv>R`Gl0j{YnlW)=#gMbI#nd^-Xxd*TbQawlQs<*U)eG6fLs7n^aIaE(4<b788r6+!t~)huN6Q5eDUBdfqN8Dw'
        b'*$`O#?TPrFmKI%hS?12Pc%8Nlf3mExa8U~v*1X!QVIJxCRrb*C^2P~A>Hu6TV}L-fiFt}U{*)G@qQt)0_T;{P-=QJjx?_jjrP2h%'
        b'KTvH)z90zDgO2hCT`u%R{HSp!Y}o7Oar&vq!)3hH_)2KJP%*MpD2krpoNipqtuq_XaqAXxdYW68!s!Wa-TlTCZk@^4%B@Q^)^h9S'
        b'vn%)658mOp`JtLjjKsc5b2FOV|AkQHd@evdyMHJ12w=Zl!d_kRH_`Yx6N4@uu~bVYk&ynHpKKW*hJ5*UALU+%5MN5LzuA|&;y#Xp'
        b'4xj^-C<s}!cI_`l<Z06JnRI6%XRJ9>miS^Md#Sm)$QTcLE&D}t(sV|R&i>@BnD*qqnzwsNG+e=XyUEANCNl3Ch4#Zc{TyaX*!Sd@'
        b'%_XtK@WYt)^(iH@2zm)t@&NL63vw4v9o>G37+xb?RQ*zPk2ZUKxKm!br$pz>EbR$<q<VmGD-oVMWQlv3!jWdr^!0UA;aklcraR;B'
        b'AAPxSs5x;jUOL^m?*5$l`>KnqGJ%r}Pp6yx_4_RAES7ky6u#sE?FuY(^~z$HU9CYyhMJQ|$6v)Gip+(H`(_)nmRhRgGZ!YMXJ#3x'
        b'?cOQIbZ26WktisjMhT;=9(P;NsMg_3)I;Gt$ZbInQQRhKpSjA=^jnhSjh<$U5z`i3vyxiPHMBz&Vq@*%5nQ|Q-&VW7z1gzP95{Hh'
        b'hZq|WA5`RB{@(NB07$Fr(5LkQ5!>9ZGXwx0=5K0dA`Cq@8F{5fW`1uUPd2(tl;e;HCB_6%y9@Kb+>C;cb>3vc_i8leH}}CfTFAz|'
        b'nlMIVvYJeLs0YIxL9r)ntVPsryv0QLUuYh_jBwPxeA!<Gm2vkgs5ce+L*KP5I`myvqhVrUjgMUbu35dY&)wWZ240`ETk$^Rb5a+q'
        b'9eY;_kBaghBzQe8kT@nk#gmx!CT@GRfr*t4CC*~x*pYK%Cn&2PwoMQVr(6L*X}#lPZ%~f$i8af<yzlO*yT+iquAydM1OFi|$m6_8'
        b'dQcL=f!#~8DLoO}^U-ETW3glAN1D<1Y|>n@57wM?Fpy@e8|)m1LbQ`jAD^>5-@r$Hq|L{9PA>&MoQC+-H6ik&0b~#5I96g*2xew8'
        b'FC8j~3U@o2>qaEUDU;u{w>MZghju3l1dF^Ik(fKO85yk~Y-Z$Xb9Js#U2J|6&5zu4y;Qq9e6U{Ssv1O6^UmO*s>n4|@ttow4(*mP'
        b'FWKK*w7Tw`-vreL6z|EIo^89?*h@_eKXSv>Tzk4owZ}7f+M{~Gv+ISbg<mJXbAI<!;gr>8X!a*IFQClv&F_%#^9ZvbVnHku;Vy4L'
        b'=k8;h7mdQh)9Arn+F<0(Gn-wYbP?y--A%44+l0fp=;o`LswxuDTB@l+_mU_0v#OaZ)l8hN(3NS2!q^8IcrFqFqnnv~j>t!%U}S@_'
        b'%#^`~!9D-ld3sOTnXqOg8$E=*-H=&x3vJiIn31Fo`Qb&1y05)S^qyMV-s5P-kUm?A)uCiC`n4GJS4av^Nd67_o*Pd2uc5ki(PUOc'
        b'y`1ATQpEVCBZ|g-?r)kHH7Sqq%7H?Xb@e)i@MdD<GA2neVbiIL9{yVLh5A_&Q(8x$&w56^`=3qz&zg?NhkT3rowS=oLqZaS$3oh}'
        b'NrI}{0zy8_a(M?b<t~*>xfuJmCJ>|U-W_M(Yhse143s#2sqe2%LFb}T_rL4Wl6SgKHjxAfaUOs}fNE1^@eemKR?<!Z9CQTne$-$`'
        b'E_-YOBxKVl&fokKnE8_ikT%0WYHq@9{Y`}jo7@MQj7V=PRU4xcUnVN{;zlZun2L<*pu|0m1z!89gVOF=$Hg$~oy>s3Ke&(ScK-u4'
        b'!L~J(Qn>^MibBN}%>7-%7I|9OSA^qnED=<P$FTBCu9uWvJ4Vt|bI#WL9sAY@fF5a!So4{iMgVwH!6a_pq0G)2Pobxgc!UO@s;x|3'
        b'K{J?sJk78+XYoEJF?-4Q)9N%rQrntfbQGrSwP}IzvH1xdXMxbr+1D(Ckt)@5TvS1k%xEd!u8XG%IGvMJfXWLx!R8XBE<p$KHTz6c'
        b'$PVm;0pE^h-3vp!r!22Nuki6E_VK0<seIZ<kW;25J(*-+H#LzqnFg1Ugsf1g$MBf!gz@?h>fa)5H2PkL5za!IB&KSJX`~I;<2a+$'
        b';j@_J-88oAoSv9cRpTyf(%4A7O|Bsn*~W2qP5lajA&H1f>czNBW24>+ufp{<;!kwRJp}zXEM>}6lO<XE-JFEq5RQ+rY-NlIotq%&'
        b'9!!tRQg9rTDNO2^6}Bm73mF(mC62BKyI(<Mu>zl>!Ey8<PB#8tSQCAP{_sQ!jxELsU5X;bhNY2`%KRy2ijP^0Q%VXw4*v_oY~#b9'
        b'iiU=thMyOiuq}3MxK_m6$xS=tJ7zpB7v7G1x8jIgIQ7fv*HuSj`bU1L)DpuM%;O+w_35ChW4%B}k{RJ7Jx$0kkr{Hp3X`Ab3nj#M'
        b'Bg8tkXDh~qgeV}-j<1A-7%0*4nxKskR!0l;bRlDYu*8EbdP2rrAtAcT($UT+gpz2XB*w35a+f0z?#1;Txx7<Z#UX-8mYk6IUP8x_'
        b'fm3U(6iG~hr9#?4DM|Joyn$R(0MR)ZK7n>sQm#E^e8#-)`Yl?<|5QWeSMvS@wYvnt6`X2EzPLLAIsFL^kEs$m`a=OQ_yjEz<7%k&'
        b'X3V3rAtUE%W40{xIg!BFalKuku}`53#HZCM_Nj@bkHHgW9uHC)+td^rv)HC6uKFo^<9I1mKqF$_3ZvsxWh2**Q&VteF|OE#ZNv;Q'
        b'Smk&czjmj6s#5;gHY^>M36lu){j{2?#8x9356Bao1lDnOGYB9sGm8;!(1uW`D0clM6fyxC)&PJ5pa7cw6yBS#n2sT4ej1ic+NW($'
        b'56?$=Qd2o44QYH9W*pCce%!?+ql30s_GZ+lbdxeBO_i*%Pm?mEI)*UWEJnLc`9?N6xHvUUxmIJJO2><Uq24|XP}JL}>P%T_t>b|^'
        b'hK`|%nbOCh1jpwh@VO~amb5dDDAAqOfGNkbOUDZ|Yjw7@SmZchH>|<j>38$9LivkvJPkE%F2ZF%<Y`(&<R6{*mBz>GLNp#C@Jls7'
        b'>xjx}hiJkS?}b&QivUG8eeF)1bcHNDX`<`7n6y{N-|+*SAmTaz(tW8e^toDtlTBgFeIx!4PXOBi!1P?y2UsMS&K>tF+St1Boj9c{'
        b'Tw5SthH1xP{y|35;FKPhE7M~zPEp?n;L{ap{o`Nzp@IL8uy+A#;z}FGPbQO)gwZB|5dn8I1A&0h5^T$*wo9T7mueSKBVfBrq9EG!'
        b'TcxyG*Y1}IHcTQ)5^f3FZjv??sB9s<h!=K&wrCYvWw))hc9+^^OR4Qzik9MKe&<X;-Tn6Y|DT5^%$zxw_nh;d_q^{p?<M<{8T!N7'
        b'HuyXd%sCtaYafU0xVnYWEZD#kN`(lI1|J4>;;+N%Vj$i^N|pZ45N5kk^nm<rkufE*YTinh9FfxHpejXvDw98Np*&=M&nh3q2TLw^'
        b'Uh4x{7hscc0^aw+o<W?T1E|&55Daz)lGAJ~|CF~=2nW#bzX@>zuEAI=9AHbHl`g5o;c_%45%RY~cV6IY!>h^(SOLsBDg-cV`!f)n'
        b'-8&%BG%lAQC4UVRj*?(g5Vgx0C9DaQP3%mAIm=r5+~pAW^kR{ZFIl){7ZH)&q3|u2sPkNNhxyVp3?zIhfxko?Qn^AKJ{@zghKE6d'
        b's9+%Kf*K8$s)`!?^cHY!t@4`eJERp~g~no`3Xl|wg~4BBA0UKa=!RHBwrjJvKsYmahOM07KPuY%5$pi+#Sx2P%Xt8VTu{VGAeOni'
        b'QI~u(uxP9X(m#UUg2re2PX`K0XZRriP8AR!$E(WUDSL3ZR;xl+f>$R_g}J(6$6~o91?O!CoPvA7NHnoBWZUyn{a2FZn3Rvnh{cNR'
        b'{E<gh#Lq%6F4s!W{=TN_(ZuDC3eJrl*g5Y|I;M*S<BN%fhyElwpF$)Y>g5sXU|}|JdqGIH$K!C9!#&`+xA>3ZKzO130SNB<O@+e;'
        b'3P93Mq+GvqA-Atfo)d&Wc8}4>=alC#UBoS8G_k2d<{foI1`tj8LN})vF~9J73nWjR$D?SZ4-h=Fl2~3u6#Y?^<x}|Ia)||SUJ0!t'
        b'URviQ!W59CESCrmvWd7q{i^Wh%~`p%5e<{svzz>9ORYpezIK43LT{fRxmBV$Ui1$KR0DNd3VRTpJ)d$RYZC$GVJ+9$@&~TUvsg;9'
        b'fQu!J&QtJCWMG~XCW5;yWZdn!4Jmk?xtC8Dp~i+FFBRPpO<CsnaCL8sCK)0SMum$Ka6vF;mE(06fv%^iMR?FNydnWFpi+xo|K9>e'
        b'YDdB~ciCBj7k<(b%*H$bvk)ajzM{PbG1*F0oi-R1J1ty9Mz~TbsXT24*@dGvJuNYKu*n=uNO?H@Mu+o1+l)hP{^lxdvhVIDkKbuB'
        b'?%$h~7tKcEh84%~QIlG(Nv_SBmgN82<}?4<W_+-pTo{tO8-4Lkqw)W}pRnTO|7eq}Xdy&SDw%xvfL&EHE5{hPwCBjoyV9QE(tb}q'
        b'a3^i|j575yQ<}nEm7-Yasv<KLhWw@8i7Qrqj!z~YKsL%E&s@2FU5oj3;7bOMxC5RZDU|KHoDHU<GLO9)dDv&9&ffrHk;&NrtTJz;'
        b'%bC1#)|tX@R{Bp~pM@u*#Z3KP9*KD)4g@@y^4%ZJ)IBJ^`bO@&=l8+ie}{#LQua^J+Bp-F^1j>8QOcpa($CC2!&QZRm3}<!Nm9)5'
        b';m8{7#55sMzCVqu5S1TI6GY(U|Lr@hfU@&!xd9J=Nj?w1{Exw+cco!aa{l);Saj^Q+i7)1vrj?TYO!!wUj7$Ay~8d$54jiLJ2(B6'
        b'muKBzJop8&t4%x60I7eSPyPZhd-;?{R4Yg%uueV%s9#5EbpFE2X*^wuWatOFvITi2dGyd*^C(X!{6z6|Tt$#q*N>q%oyfxW$aT(W'
        b'7rmmByB1WYu(uUH_X@_83;bo5eHxv<71?_7$Kn>~Pv3&o>tnCqw!tD|I32xfbGGCJ!M$G%zJCGaX5jSl%^pz;ra~?+B;{{jznn$>'
        b'tC`rPqL8r{kBBON<NC$Z<TrCkL9aW=DH6<`G0k~1N7?-8)4FMv8!xAqM=&i|1QhX;^I9SkYcpXdV~M1MNClCBN+%l=B2$xn39f&U'
        b'V=X=mcp#5hd`kzA+tL%)$+OKqk9bxAM-wD=K=(ZxBN+_FHuwUCVDz849`NwsL;2F_+dizzALY%S-x>h97p*>X7;bXl3o9R`M_M|0'
        b'JsD%7L?;g;BEh0;z<8b5p0)u_y4z#+FgCMuAXPQeE=r7SOH^gHs}eK3U$wx+K>J!|&)%KdJ-XR@JJ{u)?%?Ry^xQL?ik{%J0jQsD'
        b'4qk~nDqEIC2E?xT;}3c~Q_EDFChkq&GLNoo=E6m+A<l<9wKzr<G7)*WYFS3@giLL0CW?LG=R&p!onoSH^W3OAV=L7*ce?dE-F22O'
        b'X?7@FX4T_%Wa&At+&Y;&F3-O?IE4nu7mMO~(u-U{ce3)Co5|;O-?5x;GXfvxJ=U!?@RZS01eFt&h@4ZW1)Yj1)0KQ4j@+P2qY76w'
        b'7bs_-!1OE-0#j=WZspI8tvnoq=z@-ZX4s(%ZM^1I<lNgI_!0HHlke~OaqtFP{-+;1`GYf@zL~li4x>+{E}!_(=fUa6(RkWt_p^j%'
        b'!s=74Br*<(7wi*XqolO5*{f_ZtE9+2Q*;~S5RLhHvzap2?v$aptT)i!>b>s%xA>&oy~E1MgvgjD(h?$<tc2^Y#WkOn!GXrik)oV&'
        b'jJ)Dre1)9XJnL2$TQ~kM^0FJwDk-|1c4YiBa@?)E%AFgqO<aKVP#QFQ|KT>PP)t=S?A$_QD0#gJZuS4sKE#DjzHwr_CsY}wwQiX?'
        b'HcXz2(cd?DKbb9S#&|2W2`(uWE35O76HVR`_rJ$yg>8;Cd57J1LeQQ;T`k{so!KI1xP()j&?RVw1({0kd+wn~_%j#NQUf#}HNnZD'
        b';>@*GiTVamerk?jQgLgCiU>@H&Ki`FaQ5Z9ZoxEIQorjKk*2#A^x0EaW%kziApOE*`dGBc{EgQ;dA)r94LGG}j$!S}&DYaB0PcyN'
        b'*oIDQ@Fz4@71RQH4Vqi>?@dIhD(yDCAQ-)oC6bh{-K5Vq5%~<dKG}zH><7XpNQLEmUM~->osZa|Ej_&EC17mb^zF3_o0C7ygD5xl'
        b'7j~!vetrrJOW*=5<g%DOktRwC!PQURg4;tcHn#c4PHc|1c^FeDs_UHOJ~WL)(Zb3!dU-Q!{^A78>wk}hBQvzCldtUfAw_bqBhAC6'
        b'JEa7M4yx%)ln=_NQGewoM*VCvBx!olE&oe5>7Q{k;BQj+6kKnde4_3-Grz!OmDVo$Q+dIp+;*MlA)?I7UH$_%h5riPTiM3$(Bk~N'
        b'=yFo|)!WZe{wekjUHO5Xr6sq=!2izOV^FU7?_=OExoZsQU$}4E5|hi^#3JqlGnA<i@fKgXLdopN<7u_<I=5DJO+FPDd+ecR&zp$F'
        b'aYo|5xzTrA*5{T&ZU7||&nA10;{&h%ul>J%^5cQm|Lp0Ib-AUUcJ#?teA_OFj&a|<7UX<prdG=XLPB6!0GP18a@iIpH$%P$cZx(r'
        b'{vom0r$SfNt0X5%oj6F&-@dr%(4r`3!ct_zAGT$4o6wn{hR@y*w-G)FZwF!b;%;pM3bh@*R*Qk02YhuKRFnp|bDZ|svAF39a9+6l'
        b'KeF_Xt~OCZ6i!6LIhysE(24EsPBfH{j57v`CmK3NiFiW+wW=v2eAeG5Fw8VY7i;6y&kOQ2MD!{_%)uvaz9>-~Xt3L>>)v+`yyKZr'
        b'*uQBQwO3zmuR6)2P9m!#Y6Z{-_}zbZp)lT71AVXw9X1;-Us&I!TnneuGS0>iggXbg(9+8UXDKP19at!OMf46T1PH%kqgNnpgJqv}'
        b'3h2#ET*QyMEGi#F=acWbb|MEKg)rZEVZtNZcP8k+x~0;jJ0B-!8mp+J!$<1YgsxcjN!1EKQAsq7N*BDP;7lv)HbQA+1<=0BtMafr'
        b'!Z6DqOYcM(<PskJEPAN&@(J?}8z$^y2@LHbodU|h^S}K=LKLP`!d+zWD9aS87WTPht<D~Cr@(EXH=%+qLtX25Vf1%j7Y?GhrSvOJ'
        b'KCy@r3F@>9Cos#sU|f^_GeP<UCQJdGV{?T9A2JeA*-15W;|)ebCGyf;a(ZnO=evyq*6Cqe!d^p8Zs}j5WM{lOtwQZKaGzZUn4v-)'
        b'G@c|6G$KpPu%L|-Huw<>_d0*i5AumAc_Xig#8+NQUx4ZMA}fVn9C#-Do!3#l@U<vj4d2&=FMw4Op<^W6;N)vZiz?KEocs4DaY*-8'
        b'PFi-eD=+DO7qqRQdzw0V0nUI;X;#s{ZFGtviQ@RgP{?;c(JIJz)M5+B4NYcjPu(f+2Tg<sG9a|I>5guIvC$maTw5tXHpJ~$>Aj6+'
        b'RRnio>hl8nf1Bp)9SVyZiFbDo=GU}|0?IfbIh|c)LT528jp$e}MEmZIqW4BOHU2HQ?r4yx$t>J#$j+`V@KnEjzi@WLAy+qs^MnOh'
        b'P(J;-m*@Z4b$Qe+0{MEcjaW45l#RB@S{)v*i7&>(C4d^>p-{1TxcL;Xg1X4(3Bq|e07;aGr}Y3SFCPi*pTwa$CCF|D#Jz*!8XzBu'
        b'4|+j&P7~Zvv<49*ZIH3!^F;6?@@^(-36qT;l^yGbt%Zkz4sUoq9?dx4=T)fw;Un<?DHz7GM`u3gm;W$FAL(<A!8>EMw5cK=T|by('
        b'W$VW8Q7>rpb~mNPhV=&R?9F^vLgbJ1dnkAOOu3ma&`%4Td^fe+mEgwA%iT^-1e}|MOc_1Xf}AYb9l_`r$jef+Z{Qjs_8h1|aaN(s'
        b'vs_^I0?*!tPLcAFn`ZvOq1-gStKtopnreiUBrO(QC+eUqPc3&_MrZH$y*#*A)?$lLH0WQko-Bp_0#Ih%q%Sr4MDDs>s7D-cMavqY'
        b'lo8ayN76QuK|g6x@efnv$1R-JuD+TjKW_-$yO^nrw&3klcpl=G)gPd&VdR-RS^qMZH5O<$0JAYBczdFLuZ6tUpyh*u_=pF^Klk>x'
        b'40w2Fdr@dl&7Ywpw=~BUqWM!xF0M5$<!nLKSQEAUEAmebX&zBfgDHJWxON2j0#3&zNMW|8ab@Tozk=mcEd6@RtilVLs|yV=!Hs_w'
        b'$J<*{yQ<A9ATI{9{t91dFsnj>ujOav?h$EE3&f5@(a>MKE(l{JvOR8TK-mw#+UtsE4WEL1PfJVp>y1!!Qhvayn_A3#EbUapXoF16'
        b'G>$Sd`%;r_51-EqhnsphXNDx}#X50*F5C<Kizhv4HL1ZUN!(iDd;yBazMWB<TeKu_>}bs6=gRWJbIH6|&F@>xI5t`=D_w0q6~Pw('
        b'bcbh!>@)Je{3s~g+F}-fgDU#P2FEtY$g11K#9}0SA!H38zS%FI)R)dOe6S|Sa>E)-HKyQK2$4TxQa*8$g0&bmWi9Hx4aDNKSalmd'
        b'JdZ%}w1nTY=)OKE=XpUVZ_F}fmdz&?L1CtoXD*zt{1<!hG+ofZ?5t2F!q1az-G#A@SC!kQx;Hg?pK4T|U>(0~3Er0G0mrHq_>1g^'
        b'b6dQ+7IP?Y=voj&r%fiSi4V~yl*eC*dTDY)A^>d1_>UpCxROa?5vN{h@>C1IVrOAd{(g#ru!N^l3ibUhRN?$0KBh@%9DPAn^j^g1'
        b'S{a$rQo4pO;MvTO<HKNQ#{`q|ta*jX2D5VISCtjzrB~(ogui^Mds(A5yRp2RB{wt%7Chm@lFL&je6O=(<Tn8cIF&!LpscM_*>EGE'
        b'TuIh7D2_|@pNV{YtQ`A>;$v!g%P8mV7ekguQXmOREPO2(yY;<r5tOC)fS%Wa+#~y1U68E7ej%g)kxoAE|E6M=Pg$3!Ez*s-R7?g^'
        b'2!z<x9yaQdK@33CzX#5Js}nW?v6r6*{L|m-^MCNKx+=fG8!Mjb7B_n5H;%o+l9!vk|7;FW0EKZMb0W6~IJ!-42&HgHBzUQ4@2kGc'
        b'hMNAWxtGr%A~~z3L@OH2q6jEJ&|fq|uCA_%{Ja@46|;VH=;4MS2e$BQg1+gD$(mbpj&sccG3FHQIZ|@v%mLpS&J#3p4&A|=5;H2u'
        b'gPVr>{8uM*Qykst{=C8aPP5<5`Y$0Kx%>!Af9*ti_XvyY2Ivz`?{T<ZrNojsy)+(A{Z@1GbOv9(JY3V+oUuB04IxTz#B_N;9cb=J'
        b'gG{zeRrs2d*irdRg*>zh&dkDW@T_;+wrY*1!R)!$i5J*gq%8}v!DWE{z#0Fb%&A(s{b2KsMI!Hk=Bmo2&MkllAr=`2Z+3>1wKr^)'
        b'c)iWWe9#$UHY{)&BF1*z@HRV*NsBu}Aoph`7Z{qG;p#)-X?4I!Mr;k)5lJx5*f%RenYS~rZJQL^Ynsc-aAOWI*qXO{8#;x(A$}VR'
        b'afk?2{%r!zFhm_RxfZwvI=Njh7cfGX+-#6C@s$rc4KlMK%xDN7dwj|$oA31SkRnRqe2B+}oy`e5)n>fFWQwcUsS5O``aBY+4ve+U'
        b'<n}Y?v<7MJ7iNP@YY0PU7;mzdlVUjkhmaT00od?=AeMulCxw!|RtV(xi;a9x1aY)NwnYP%Q#dXy)$nntrnq^_o>&o(Vh~-|m7+(^'
        b'8_dcySld!rR$<ote1SBaAGE+E;M&9a%YpKP@8wz3%Gj&^d#AkR4ZR^mc=;|iP5YI4h10vdfr^y|UP0<d$`ezBXz*ip%f@gWC|%Rb'
        b'gH#rhI_2r_^%s89on<qgsfg|A<dq+0ksoU0`}qFm(SXcxpYxavsRWBdgQG_)8wNxL2~TLc24tt*>Ia<R;(L%OI=Wj*aSp^ljI_H<'
        b';bPuxeOqcE5-ns^I2McufC1^uv5xS3ZXf9f+{lW`8)iCr{s(Up9!Pb_$Y!I52Umu?3LO|JUt+gP)Y4{hely(nkg{=6J{&ee%SR;p'
        b'&O4&tH=DGO^2TXWoKWc3#;Myx9Q{U?yF(R-C$qra2@x;lvG3&<Zo%p5<)Nw4+GxIrfHZ9d@b`SLx#A!~`MCJ#cD@D#H27A@k*MS%'
        b'0XVWCp8lq(Q0^oa7b#)g!}E{}GY?)+Dx>df@X6+zI-~_13SZ%TM9jWn<!?_DXu7a5=VW{oim}rDcq4rKH47Vt)y%0~7c4+zt|)G0'
        b'!D;~<X}KVTkBeZ_XWx@?rT3%KmJitgAEV!Oo>{_;Y6hki?V%tsKrcuBx*a(iJLdH!Hgv5}WK!DPJ@l7|NRbl`Vulmw$GnjHDu0%h'
        b'2mVDKcX*FEk<#K4WI=EYvdp+-mI5OG*x$>ezJ(w{DA3MfHfb(7U^;>nY5X8;&_Q9~6h$QUz0;@s<AiQ}PS3~h@KKLL7UOc1naVtP'
        b'$}4D~`w<xQLC5Z+%ubVAN)I}QtWM)9XXQiOq5L13;0yY#e8}+<6fVH!3q+JJ5BR8+4trC(*wG5b+Ek};rDHF8bHTR-&dO9rJ$h?`'
        b'#TL+enp`5i__~wY>K4(CCbMyCFy^8csDJMu(sG{;U2!cgO7nD6E`BhMG&Mogsv96*am4Hjo^-(7T=Ux|Ee_;Ue9cRa{s$Y1;?$aL'
        b'O^~u0<A9bQN$l0Wdn?;l<NqZxamR?oox<6fPm*c6oN(r|JERJ3=E;pshUcA~Sg+8pVd4HQnkqCj@%dt(fV0Fu&BhSHf%b2Qvx+BA'
        b'3P;)Pry5{^kn%@ZtpKC#4o;z-j|0wnT>^1Z8@n=lxj>GK`Fsv9R>)$A>>&k*$Xh2XqI!_4SAP~N4x1WXBP%VUpW&uVfGW|x8?pUC'
        b'C#(upoD+_tbrW2X;g14TNx2o$k{`?eHU;;yR?KpoE&uulZ-KK{SpER3d9W$tX(+>LiXCb1+=@}=-X9Z{>Tf`{@ZAt^_;>JTY!6&h'
        b'lV$|NEZ#WQ%;C+VIlMU=^qHR6G#fi~_Wyim@XVLo=v+9Ck&7L(a=r*+X*j@6-}YAl(;kOu1*)RkshnSC=d8c58V%AGwj#&UR39yC'
        b'g2_oLbZX)zMUL7`f_%hjKBeGRo+_yON@qFEssg?UN<tE@LX`G^Q>}5r-MSzgDP2fszXbR7d!6R<JW7-dunV{Iuln!pf8Tgl`{Q=h'
        b'{?B0hEAMWf{K$?X$f)qU>T~>~5u%wSMI7^8^1PToK)&wKBfOzvxW^!FueLXQ;MAY{`l?U<0y~RBkAUb7C~id`7hat`mvbZ{c<eqO'
        b'Wb&43Mqid?AwS~8%g9Kwrbd0H(c_uwSenKM#DVnVLb4wntAOrPja`%pW-)d2**ko2UOlf=muJq%FWiLNP^#Lb;_I%?%F43;-ru)S'
        b'e-$bdg>ECo2|WVxHB>dnl1u#e!>Vo}ZC%o&!h$y>sIFU%U|mFOur|oK&Q|BWQ(eL_oOHpuU{%W08F>^NtcRk2aLyiQ^#uKm<8H9-'
        b'R8&7(5u6C8M@+r|XF`bPz&3{iM;%a%Hj6~^TpqpM9*lF6eqKZtJA=w~clk@9cQ>k^vES}w0e>bTBhx&ff(_D7IP8q6O+}a4yPUFC'
        b'1`75)r;uFlwFl!5AdeqtrL3L^x|o8C0$mw-X8b=QUX4??1VMQ2bfisY>M&hFk&5~ho+;mHUNG}*c>Z`--VB+o2KHIKx)F98;a)6+'
        b'l4wYHL#EEPLr{B>-;1#;oE)xEJJi2(`0!*iKjM&U*%>p(w6uw6HG&>?1cDz>5eWY62!1o3tmQ|*UgWr<ALBAF4d-L93xi*?y}U8`'
        b'jK1T#WsC)*X|gOeWLGTHvp$KY$V5A>ZcOBdCLu^oQwbUO#*8E9{y3S^sKV&vMko+YyF>}@dz_KjA-5O>#aYfd^k*^#(OIZN*%-64'
        b'SDYex*8KB<Ma7}a$*hQhMJ0!p%}0KR_NpQw9dG9kPO{GTrwI&svz_xzNQXBnQl~<fXJ@092`ncgN9*}n`uzfOej~&l!@R~^;gfhL'
        b'ej|$pc8=mgChHeIj}*=meXBm`4eaoRL<xbVm12om35|<=6@Z_Q1(nl_B?(P}q9`nV!8cDz+OjO)vh5EH{>YNw))V}osVNZ#V$nH@'
        b'<%b}i#&Dt4&T%o~Rsy02#Rq$nds6`Qw++ZWauKFm2Cf+&uAs2NR&XtCvHG7VT|O``_)rms3GWAFGD6xxHK<6#gpHs=i&+|hI^F>@'
        b'Afq1SD_Q3T1e1^<t1x1NPEb*GhGgw#OeCxYgbT$jYXB9_A#%p93X6wTwgAgsF2)>YIRFwe9_IqmSsLKuk_sQD+XqlsI)?ntzATZ#'
        b'BIdk5)wW~iffULYlf(egY2kc8pdfIA42Tb4md{x75+rZoIw)ku<f3#NtS%}>g=&5Qs9&y+$>1U}W0o^4x5#2DQLYzYE=*`fW?7F+'
        b'P!eQjYS{=Z|HDP%M1_SY4BY?3AP9vhN}DbQ4W!NlA0uN>-*mqNF>NSL$}twwHww!Yt^w-W`j}H(a}6=)QJa5c$zygZEDi;lSqTR9'
        b'03<VLCU$^p1DNh<;2Zd2tdE5#kN6$fGMYMFBW&Y0%ZgDCEbuX985id7d9W-O1#tTVOTTJY7uYFPI^0%ZV+_ivJH^8N3TeYFs|>=q'
        b'Y$poGvY#c3>(wjlX37k+uA9b$e_|;L8C%FFzk@gpBo{14*=4A2gL`0Os%6}~?Shmi3w5A|C3EY2R1SH+9pZxg*f+>z^p6p60W3R@'
        b'0IWp;0S9XU7maVQiX|VeZyO<1T;_>!<REo*18gHm<RI+i4hYJFaLW@OWXWnfgKnJ2Dm&zpW@nr7bR;oCh~U40V=B7rRPV40H?V-*'
        b'3}3~%>nvFT5lqb4R+AecURkcOq!Hm4^;c3=FI<h%e`Qx`_1YWAJ14oG!wwWmL8+KfMFo}D;mgnA3kpBC8dfI}LNtOS3Ln0N8Os+>'
        b'FcOmqw|oT4KW1kFCK|Vlz=42|XjdV1Xi94@VZ!sQ@DhC2+WA=O;3imfY|#W?f(y%8Z)gMIO6u^PJ`a)0%d1bwpk_(<H}$Oyq~KTf'
        b'|2qX&BTCSVDPLqQzvIrPlOf;*Op#8@l1XsP3P@>vTd}GNnSZpR$eJ)qoL&6^oSbx+5l*hE2nCnYv81qGRfRTEa>~hI(ahk>DDNlx'
        b')$h~?v0&3QW?6=?fJoB&{yvz=k{|9@pP2o)V;a*vfIiA6hlnW4vn>7RdP+oGEF$08ul{hqld2@IAPSIR#dJ$pV$v)sP~T%WnWZQ#'
        b'5);0}T9l~0K)o3&5WWDH=YGZ*jF8I3tWfS`;fOpj^}K|T6M`IPo>s!k*4L~OAXoLG+QtXSxA!OVi$cH?lL<}P%O<G-_DYdVvDRc5'
        b'a6*~3Y^|wB&>2D(qv5)k)wW=)i*4rz?Tl6l6uKHX)q3X*@~E>I8w`VRbixPnP3Jybg%OJgVk=>9OI2)c@Ki|U%{Lfqo$F`4A&>do'
        b'y!U1F@_NoJ<CJWum5+(x{;*G|`+-&Yw&H^~*y0D|<=45UGf_7Eg<EY4AbLaYI@qsFo_`Cgg*}^mSd!4VmXh$6U6oJbu#+L7Yp*C}'
        b'w9{EijUpd~J=nGcbl_AF-$2Ksy6VF89XAhWk#$ZLcG%d1!Edx8*gq9j7ii;gv1f!l0EYG;SwfX&xr)4C(x2~#nPM&-N*jM-k`N?B'
        b'2*~ZuA_{DO&Y2ss6;Hu0kN7;vboqYHl2D#>qnH1fkKogxsO}Oh%_vE4jHfoC{fDm=BR}(%*t%u{<)Q(~BhR|E6;t_;bE(8vEkWLo'
        b'2APF$zoXt^iwrp2ZLd{{C{M!MN=&#LR4m7YPH=5?N<}O-xDmX)6dT+DD#9`0y>J~mD>39+_0^d3nx4X8ypumFgis-hTd@Jt9R%0l'
        b'uMJc@{nxRUE51UZ$5S1nm7iWj<~tP|r3rG(vKZ{`CR)c#tlV}#pN9d@g!0f8*sqSIm6G^pQCv+T<jD{QPP6&cPlUwOUgI%U59MyN'
        b'HpqKY)2A>UIua21JmLP`ti1I;SVa%2<ol)0ZKKtn^M(bm$+4GVjYbc<36i!ER+j_7!YMpvK=>$ZJ0?o`96MB+TxHQ9byFTjgd!OF'
        b'etJ?Ox7~v8DhVi?P*n6$NqB{^kXV>rofNVup_dnv<$s1fctIuTc{C{=4tB*;xrj*`|Grm(4zxuxDH46_G^K>4GJA!cg0Uxm>XmrK'
        b'&hiUvcSgNe<Q)5y6=nk9AN@(cYo@@jD8Ci&*`+{R9zYO`em{7bML`Y{7H;Lr{}2yJZg$s<ciN%+nC(ue_x|Ycf5ckC0Z?CaP@b67'
        b'71H!Z4S8c<8YMij0d=kXDfaLM2x`*U7WQyH>P!{zv_izoh&s3$!VDA>kj1#Bm2gL=J(%tj79<-v%>hqL&c>^7WQly`CRRT2EvzMK'
        b';nZSS2jrz8d`JPLoRybeCVyV9h?5@1V0&5R8(DeQH!x3t1i?JYr&xK^1ndRm_Ih|oj-$&E=6bryJjbP7*R#92$^vH;C}u?WjO7R$'
        b'Gq7+98~huKn)Ck}*8flPrF{@mipo2f2CIay%cI7;{CfH*s%CJUB|ZCQopVUPvg~7l+PYuE+fRkxlT9h8)%WPoolL?MX4%SecoL>8'
        b'W#t_gAdFQQ4rjKkU`ie$CgL~k!GynOAudKKi(!BN1~WJ@0oXQCRS1ZMmoqp0^_Ot&H^#smSxP;7FbQUeZULr=D?4P{wwuiBfPLGP'
        b'857D?AJtA_aL3x)?ej#IuZG?KE6f@rf>mwXHnjutCo9=tBxVRt*{cd=Asn+Ag!-s0UfHt>#0^(@c(59sCJ1!o*y9knKZKcJ3ou`@'
        b'gvf)HnOYlmBx1r0*78dh<YF<)V+OKgYjpK&j8?dR_H4zB@#NzI$YOb)av<$(nW8+v!bEk^K1kb#a?Kb9_igV+^bt~B_(k6XTfyE|'
        b'%@2g}y&D`L6or^jz79WO6&X^P;b0}I?pLUUzmvPSF+-jLxxu5tpg4M3H+|cepC;E)P*9zVSKv=*Ry!*3p=O`w75c$_oH^|&{6w9h'
        b'V4pGmzB)Y-x^fG;%J;b1a46f94JzoUeVk1#G1SX1>oC#seL<#Lh4Zy>McPIcPVk9{+0dR>_Q>)X$3qS%UhK`aSzA|Bs?Y@_cUIs~'
        b'VHH>$xzuqAJ9v=3f1g=(UtKY5Zx^Z_qgU+bl#Vz{pDT!6aU^ops9-hJDHUgbz}aRyTv)tVdIkBDb&wA33P`0|e1%*L8_?ZEx)j~>'
        b'97G)hg*7Lfy~8|0Y*$p*CNFgG9MMd>_=-zr4YgSvVZpNPk-<A%;7|#gwS4uoUB$oQtQ2S@jw|u9EofIsifg0v9U_&05Qb8Tf=v{G'
        b'092tbD~xfx&HM}j7r0(=p8x`H7`Lm0o!I48!*|?+JnFhj!tirDYTZ&sc*vENCrrU<(S9zhSBj()AH2qL8M12KGL#`APnaF2puwFS'
        b'C<b0$nq`K~^Ko|GfRZ%Ug_S@5b*12L7zrUgiDqXrrTZ(VLv_Zk!lJ3*ImK&rM5dWqNoXPOWlF5Mea~^u?u2_`9&*b8=nv~0r|dq}'
        b's&=ts$nLCMRsN5;`@kX(a!ZL6koZ8q1vBH|;3);uw^d>)uPHNCN3YP2-!u=5%)RSHH<6GEd7N2W-eG?7ABkvUo(~d^B;1MdzH*C}'
        b'1j=VPS$6XDMKb}0>W4OW&NIDMqnlw5XE;xfJUq|-P)(}6ddO|+=<^(?=@iR<x)Du94-I~cVy#=Qu$>}K=@R1j6{9S*LUC3vD|-Q%'
        b'=xu+=z6CkP$hKG8YBjBPC=YAnz<}t~XoHNw5$~P|m_4mbK!hDRfqZnDMf{UJ*kCN^I?>0h>FTO>%iiY&EvZqQE%}y^V8vXmxqEE2'
        b'JxOV*)I2Cxrau&FR;h{bBR#x_u@pYDOP#e(p}<oase;o=E?e7|xU04C>{=Nm!L?#+OZjMpEML222NW$MvH|7QCM0K5Qf-tJmAaoR'
        b'6|101rK=>!0bp*U{@p3aBB8mev_n45C4$(O+M_tTSJuUuBOYVAH`oy_@6Ct(In~J@7L0x=W5l)27{)rmjEJyL9twl~JCZ@1J>I9v'
        b'gPr5<i(PKL^=8o4ng&+}WT``nZ}GD$WhJt{HGL4=ec0)><Vrh=X;x&M4_@S_DU*RPJ2lmjnu-&`O_23?7!)qIZ{=4h!DxxBE#y!n'
        b'62#hS1M@*?$A|>`<Ty5%3w#p(kz<%e2P)UW_B+K^wOcb_z%CgC2ofRKDq++v%_(xcP`>4!wq0LMV8Vw$--^DoD`clvjINN4%m?|t'
        b'fT!!&F=7E&oDJ4`&xf8}t0)PD%{<AEh7FxO^5SpvAI+yA@VCoN$spNVY@eCZdfv?cr4I*(9w<=Nj%LcTC|Hiduv0Px9E}_Z!`FpB'
        b'k@j|^jH9X@FH97s;b5Ai=7U^b7EAr|)M%VcBe4_mq`1)KTJ4)@j|1e*G<vONl=Wfn2Ry7#d+JD3+WGqqK77S5BMz1x>*TLHf%)FM'
        b'*41J1d~UKIRdkAm1*qGorSdP?Y1mhnhEYeajixM6HYMacTl8Ojqx(9D%Zh?(&3E<W<$5H4Vg>h`DDPp#Qd1fqs8sR*?h@%Y<4%>x'
        b'Cl(%B`mj?RlAf9FdAX0XAVgZHoSqIk_9&%4+iO;Z9jqjxL3lPe?oEp;PdzRjdMdkbhKqx<_zL6FyJiS1h+l>0>NOwMBlG-^Fa}R@'
        b'YrWO^Zmk&UiMb+Av{#BM<PY{RzEI(z`|k~ehU7e?^1RZQ`i26vDF*bPxyB-kl%M2$L;(JUULk4+n`@`-`kY-q{dWBopUfrdGs`?2'
        b'26r&tKs|S&2b)S|Og_;mNNfrOGfd{;$W!8z&c)}g1M{$xSqnzy@ee(GPah-)o@!Y8tQQZ6$(c8IPY&Lgt^cKZMOSs3h<>r&=|#tZ'
        b'$Cy^eEP^yB`>zVuu7h8XODcXAHEp|e5B60?*yKI@+FuZ(ZGFLRp!(Wc^;>SvuDQMS$WL`k<j+T!%GyK;tzm6U-GzVz)a}jc@JV<b'
        b'Zo9o2_D*#xMSPp4n(BuIj3~RSnhUtW=@DwZPv<z1@1KPG39YvZJ*RMY7jTf_i{)9E<Cz@i<?Y+*HQ9TqgpZ5jHYk=#*M(nzOk2U~'
        b'RH_hA8qDYcA?0QCLwmhj>U)KhYQ6u-cp`dO(up)c<Xdp2RUV1EY@~jl!Y#eAIS?gH5g&R=){``l@Y%_S!~+QziLfIlcqw8?YKTP?'
        b'WVPklAkmAwR}+eZHBJq$7r9uDt|%zfl$BNM1wWC$tWVpxL50b~uKK*s3_^a=kW*h6xtEIX&??IyggN2m1eU!#HIbJn3)%QM9kJJ|'
        b'sfVmXm1_Oi>Uhs-MZg1T^=Jq<5#?$<{OQi5K)mlrdVC=M<sA<xcG`&OZBIu$Cj(*G;CJ5C9T1LfCu*J#4QK#_L=2*-Y>fuReu<kQ'
        b'lk3yU%P0!?yjAkF%gF7)>u4`D#MV>sFG5JjNt>23<b>~@g@-cmvbW*#g+lsYHg61qsR#~O{vDVEK%S4EZ#{97h(zu8c;Vt8lDl>{'
        b'z;Sy{MuY@MF5ZVmF8*aWZu>%>7j4^yS7`tQoY=MtKA{1dcL&UOr^$0RpZDoBqk#nVDok%g_M?XD`wP$5sQ51-l$6q#(12M?tkwgx'
        b'g+Qyp6tSuBImEb@e$VEe+7B@wj-4_)KH%X&P~p_Vv9q~aPvrI3`u|?ncSd^o@Xn->_|HB`j~$7>xZ~l)#A39OJdcKN+r^r$03Oir'
        b'M$iC0KMxJz3I(Zw`-VR76M1oeTDeh$`MlNok#8)&p4DSXUP*)^ONX;Iq}u(_{^XUtJo?+c=;F^~bByf2TuPqX@2p%;RhE)x_fwTm'
        b'aKFXmhwyhD_gg}K0Dpf45t0zusXk(n!djDZ+lOiLULuN4tV6>1F2|AmjCiQBU5wV*KC#QCx3cZ7K~4vj!JOVI0&B^bPkEoN4G>Q6'
        b'GZ6V}k4AGkS{?fd%&B@hVbK+*s)IBC=Pn`WSN1zqhvn@zovJTqW3`)M>97YAGD6MXs@kxqS$!XGb!}LZ+4~HNX<ligs0}(1Aj{!H'
        b'8Qrkota{NzNzn}qX@E%vq?rCI_+X^#;J1&3oQ(yF+?;}r9y5ur2~mr4F{!tim-EcjD#%lrmqYfu)kLHCfJ~}2d>_W?6=2kI9=Xzn'
        b'^4L&tx?n;smtdJIRErOOKPM*)d`}$h#E7ukqdWrXP}gQEoF3p@&U0khoS*WX;@7V+VJ1^G5M|p<j$p%_pOw?&gy>q<S5PdUi;<(*'
        b'vcDHH>71Sy4%Bgb)A$GEZ$N%Mlb0z=E5y?@67`z>aLpKFJBp~XvK7*@wNkASzJ95tHWV4liYVh;;s$N((?v$(&_A@XhxKdbk!$uN'
        b'<d#GF^%qQwo8=pCY2RfbmKh>!UJb(GvGDk!`1KHhk$Dgo&h*4YW$TGoUADF)`)_fhhG&fRZOU3|jD7jggDHgEN0lKgws?^hv&8gj'
        b'gS{cbrvYwRWfOM|k3x=yuBgCYgi<LagS|YX2KfKU>L+ftDSLV4m)WfneG+^o&L7G+qa0O2q4(egb67F4$YhiD3Qb2F%wZ*vte85a'
        b'p3OCzWoWZylrjI@<a&{iZ<Zlp4`~0w*Wwj&d@^(e?21>mzZW-*TFXNqjfH*T$SkB8Sprup5e)|k!F$Fle;?mO<T19w>AeMv^v1Z6'
        b'GCnEVM1)r+jl_QT$%CO?>lK06i<^#PreZ~a+E7q{cb$+HX+#7;Ea-Zorbr{++YOf~>RX+zodvtE_Z?3ygOrGX%hdnrG`c}S_x!JL'
        b'xP4`*EPJ`46YKuxz7)aPJu>;2Fx%C4)-B6-BdwwX1L9)?`Me_cuM`JOEq+0tvJc`=Fh}T6zWek5%r%gYwH_#5q*nspX5PP*-hH*G'
        b'WPLWbC+Bm1<@N?V$Br@DNRY4976S@tf51HXJSrbUb{aGwezuu+WrJ+gqOcl1$0vO2wcAJbA*H*o!ZBSd7@K09A;q5yT049>#l!qg'
        b'yqE9)fz^hT<ims##&Gso*;$v&RMJ<r1F@WEcgVb5`)q5s?0{V7=nh%wv0eEC2c8TxKG}6*^--DpGeu9F{C9DLpvuEWuL$5LcSNH*'
        b'2~!?o`fP|<%+5Dec|gF!g~~j6BnH#%0h*3|@!^=JeV@sV`fB6)dMt0r*|%k7$NSD6mu)#ddPa8o!Ws9Oq0^^ZTk}%hC*5iSKdOOp'
        b'iabx^!>~hdVuSI(iScueVwO12qsi{89z7uI-m|auK<Uwe$4>R|4qrc?=o#wk>#HspMVh_`7hh?W5r61#6QN)I84H}gcFf)Sxr=8t'
        b'5TQt}5Cg^#^IY`WoXiz2&1k#KQMIqb?emPn{80$8j(OX}T^)*carf?h@;Cs0eI#Z!2<dc0rL$jAl)rtYSJFn(OKqGQyAu=0OG15^'
        b'5P~XP0znOdpbn}48eXp3-6i{iJwLGPD1`n$VBR)bz3u-C=IA>x=VY$DU8#4)Y^AOL74*mV)kSo#f{^nO<f2)~$2t(?Y8nqh9=*dQ'
        b'i(ZkFiCJD|&&JEjsJ^q5OnvXZEk>kkwSkJypemM}RiUe3_`$~AUDi;l461TTu8atWyM1iK;ww;`P<{ZBt+e1H1;Vz{@xo4gcs|6p'
        b'A&7755x%WQcOB7d2e+}&J9InHdiVT&<n@^RN6(%&$Gp(7V)w0H!Lxhk<quz40d@^tS_wkehOQt&bibWFN4cVvrB*A>=E%0~K`X={'
        b'*tZKUk|Iyfi<m9Glqzz93PISpzc7Trm$JU72=aGu%_p?Vw{b$rE`*=?ItuTB(gTH}sids$6uWt!%7!t>MRUjF=VfxqO>>m=tMQ9I'
        b'Pfw|(gYiXz=nh{ouuO7($i6til*o$iePSO*U<pl_B?lO;)uE`KImidy;0jPAEWWZ+mbyc6HbJ(H8!^Xcb-Sq15!r=LU5n-KFYw*F'
        b'-Z}4>JZphmya0+t#69i2L^9M(-Mb!gvcuv|k#)OU{b}LXnx6~^Dhx~;QY6gw&U;+y^M&J@6UIQ8^s8^wr^q&H^n|Sc-MV8Z29~6r'
        b'gc9Bo5Llu<bR5anK@Po#=XtFUu`z#c=z2{-M9UMwk=6!6tT<ZJasXX|wzOiFG~k34ZpL(}z<KWz=Vd4obf?H{2tf|P?6~5ntiQqv'
        b'vjmM@oJCS*yL^in%|dWgtNUNBgQQ~D?%h+`bx%}8uGhberwNPKHQ=FZi*&_kZ!8j)2#>Kt8;XRb!X6gAuNS@z{|7MqY^MS?<uvev'
        b'J@&ULrw!wp^Mx)ovt9Qg%#$W8S=VqBRaK(9%np5-CM;do(2m|qImM|o;rewAZuGuh_YZdWB((xg``{OdU)YKj$))7)>I&B5JK>J5'
        b'SeuI2%(Y&XMM2_<wF-IdJxr}im=KBSvVdw(u7%jzDGY|&vdv>^cUm&zw{6E!=XM4{u(Qv|j6%GimOF+xUdkBC>o_IJ0ng~^Q^ca('
        b'Gv^7UMt0QObu9JlajCEP319JgMs$>jR|(=X9)|-VkKobCj5Y$8&tuL=Q8paTVv+WpG4ty;Yw<AcJCnqzoE}LhU-=ufeaesB2sTz)'
        b'jLrb`0c8f-ld8(MO$#qW_O&@De4f_Rk`o@yZB>vPQ!ii$Wg27%_)(mteH7fg)KVsxf?8W1rJG`RwhSUW7U5^yS)GU>2x`gtlVQIw'
        b'FL{DkoI;pV8k|dt6{hMG!k*ILTe41JhmW3=28E}ZT2i7wini5Ap`uNJv=&<x$SHB6V)2z1u}&;#-G<hxSym!TEmoX;K~})+XQhl|'
        b'5jS2XI~NSCo3+7kdXCwfOjT|mKY7b+;JeAOYwYtlqjr%YTRyuHw@TpVxp-zbs68_5_*?C^u4;4Q`c47NskA5=H42!*$+!C?dWi_q'
        b'6l4PmE3@+Gk=m-0tXZ`l7Af#6P=T6%FEF%AUwae9BLTp*%ibu>aevqS{oYf&wxrVs0*R?dvVP`FR3FNW?BW(uucTAN$cBaJ+Nksf'
        b'5jOZC8xY~an#-S8nn}Lp8rzl>h=T<eJL6!%h5xtU>8t4Q@OHVe=TN!9YqK)*tF>@^ovLCKw@cW|=Op2~^r1B`q3`Cnb#)9826wPP'
        b'1Lsa}-Cc*jvwjk4J0Y81GK{BoRqvjx+YHI^tW+KRUKecVR|KMY+3zY67UBQdRxXx?^R&1id#Pz?IUz_9EWVPPrhaX29$)zYD?fd!'
        b'4g2EQ-VuplK!PF(?m#XHcik+{L~(<nZsw*DlDy@)+ID{4>Ril>3l2qwGGRotHCD-IeJey}oL6^VMG>KiOCe1f<Ds;?8ZLSa2VebO'
        b'MkH?&wP7yi&?3xoA7s#_M6}Cn+KYEFsdfjB))?cpGYW3ogCxW$#`?{BTMrP?$ja!r7j2I1eP=t6;?F3=)59iTQpTZB*%$e>K0X+^'
        b'w@e--IQyEy_djK`{D>9l+tr!OswK6dGOwoA9LsYi8R8?;?Z*{?ErvFVxRlWP3yKfutXf4XPDQrv{(3h2SaIvv;E&w6?VjoCNIlyj'
        b'MSSh<>8_qs`*A4>uE4nT89(U0V*xR8DD9m8UZux0C1-9p5^7<Efknl2J`_H!q*#c8+yt$_x+p1CQam`$oqs%r#)Fv~4_*BK|9DVh'
        b'?Di1!FWYNFA=s0abR34`6NbizO3FwGm7WVhqd}z@Pe>GSFt!?lgJH6of}=sHmL!DA=$n=_K95pukgw(`;Am8C7&`*{%XL-(JNrGm'
        b'`-iSKQWeLgQ0ReOWv(K(=Ew$|+?&C#Ye1sUtj(Z$(Oz@x)AC3bk|T42M$X)d2~Q7`CcJ^^5<rC!?OMc_>CO=XLq{2*D&+C=3yXLD'
        b'UPVBm%u%Mr-4<r}0Akt&0n;jH1Z_!3;3zc5icIymS;O;3Dv3pqc%rU;>ZOM*^3%jXWHAxicUszav;hhrfyk1s4k@w3bD+U3^YMUF'
        b'RVJSZwZEuvR+cdhoUDURjY6q-4Bfz?=<6{{)5An*zOU26Pzdb10qn7O|7q*Rln*2Lh9!5vn?PqlF1#&C+N~&$U{B<GU$YRAfuynl'
        b'9zd|Uyj@m>z77NpuDTehc?;Ki&|CxgIz#~yL0fDu&o5{7GuK0@3aozcFdI;nb@fWS+8bOoP&|V|np-wF%<i5!dm+{Sq7+5)=GIYN'
        b'6@A9$5)FwHMRiZpf3m4WLs+JW9=1^;pdaB;9v+no=r=56zb#GmbMO1MG$SBS+NjE(`}h8M+b?R64&*P@uLiSpK&x)I<?;Pfw}Nz_'
        b'$2Lm`qLt}EIxseU>tV?WTdtOff@GlRHW{cp#e{i|Da;#q{()OTI&e_Lq^T(D(!{4Z7Z&|68PBUhVW-D_U@cz;@2y_31$_bg6!duu'
        b'viZa)3=S|ga4yv5c*!<IrHBuY+v1QZ$iO*8MvdyzgOi;YoOm>c9fum`5A%C*RGL?d4nVS0BM?J_I`k;@9h7fL$4Y^w&UWanaJmq^'
        b'KPegN*ge^&0EvhuKFKrG*dWa=ds{*OU<n#C(GQ^7%8@DaI$21kfUZXGatbf@6)D3nFCdV=oD#g~6;Q%2!jfZzssS!?5uO;!1#W><'
        b'q7zYh0U(6L0*}6d%f6{~(DEZY+p>_e!&h&zt-@6NAs=y_h@yK?EA4z0zb;MvYg;DO{e-O(r-u+w1hPmE>hpH5v%wKK$)!dTm`8=e'
        b'yUxxjI%`7xe!#-HL;ZbXDG`>K6)d+3BlB%sOyo>B^B{RLAzVo2+Ej3_?!>vk_xdbWt+A>8axefJs76)5EtMPHb_*B9?j{`GX*Pv#'
        b'nVh5N58AkR*KQF5*#oBXj^Af5=;W7QVh@&9c5F|z?U2vU)}d&$^6dCvG{Wsl8(az7jwt9xRJXnZ-%i<x$i$YsLq$2s+v99h2te**'
        b'AqW1+3sn3X6yu$;Q59?I{y~xu=(?(5K`+jQQ=Ju3R-yBpK~CF#89EZ%h(>d(M4p7A4bsn}Ryz6gFVO#vS3^5|5|I2;OO&`bq*F*A'
        b'MX7Y}3sAVFD#Vm(jkZEkq)UG8;~io1xe%>8qJ*8iv8Sc&gWb2Ru$oP%z(w2k87q+pA+>XmlHXf*j$Aysc|<qDc3(x=p5*#gdTaX?'
        b'E0Kq+oUgJeA;^Gtl|=VGJLl^Kr(b&^=+PQWl#ruVvj=lx$+hBpR3myVOMk?Hj_CkMl+4<Q_8`wj@=&~g)Y?hVI+TIIx-VK?ZNri_'
        b'@%z#3p*~Tv?=i7Yj60v=`yLZ9=dBoAkeE}Hyl^un|MHfr%_WvUcPl0I_WC<+x#Nqw6C1n8)<vb|C(okTY<hqSp(xPxhS^79p9_Zt'
        b'`N#d!^XeqKkInhA`9I&4fB!Gv&nVic)Z=FV#NFTeU$+K4ED<&K={!xRHAT`MCyxqIAGWIaH;TyDth=v6r2HQ=P7MFzDLB6!R&KRi'
        b'l$`Th`~6n09~Q5s4>R0g(Hl_CHvaDGv=`-L;>czzlk2J?^6kt(;{AD;)l9ddFT}j|h&KN4yxw`V%Q|OsX{Lbl5HRg|3l0p#9s+9-'
        b'i686m|1*w=yzO786C>-aCx1Y{&Log(O-&F*DH3Dju?U*6c3Z3@V>MZ&U2jMgjH32H2%1}@7Mr@~t-vAB)gv8v1&T5!4_vk%YfQ~*'
        b'On>N0E<~oRm9a`@^_7s{75}9;2J2{R$L{z7p`y$xLeBsn#it*)a3-@+%=w|pwkkS*?sa@<r;l0`#Ee=08K-=0OW^?1_o9*6J#C%i'
        b'DP616j8PZG=bp6oKWXj$mDT$zD_x34k=ZcRcJ2vlf3dZDz18v)oBQ(6E9XkB{cEh<B~}Qcz420A`?+=2{sL?FIxA!rOnWZXwVhjQ'
        b'?SIVLz19j@p0=m6Z78Y8+Mi?XF0w+A&Ut!z_cWY>P{uT!oh%Nzimg2sdhRi6|0CA!$E>=)vrNNK&$&Enf0ng7&#L<ja#`;jK5tE9'
        b'{vuc5W@8AX8<0kiO|m{JDli}|pJdahsJ1t5l%9LU+Mi<We#EN#fJG5BKi<Q6TjcArZUo~h?$!=w0sv|1hv-Xtl|Jb@l%YJ?aYJiz'
        b'zsxp8Ku}Yy{V~?=`>d8;_TU<=aZ&CMW)GXw6LoHhwO?-SUSic9Vd*~yD_*3Zxd{o*!4+C#v^G}yaUAbloVA~@cE?%=J6T{hM#E7%'
        b'xKV42(Z<TmFW<`Pk)8XQwI8>3FSc6ztme}_kgY=B7i(j~GM>(PBkWwHwf_dwz0itG_07h`!k-`qmTAs(68ubGnlW_1Lm)@K1Iy@M'
        b'1OhR{y`|DeIe-Roks1m8HhKw)3|!25a}bGZm&(pz)_x4FGVd5ee}U*DlLmiYjS4+?i-8RXygVr2&8|mg0MZzfz42m6YK!Ke_}n$7'
        b'{~FW%Bjf#;fdUvT2A0O!mZq8-2{936YOj&nc-~j`c$P|2GZdKvckb(ot8)28?@bffy8Dw0UKt4Opua-cwIm5yDa7>^Py=weUP4Kb'
        b'lU1xWdsg%ntmxBj0JDBlT#zACSxaQa=Mo;oggL<VTxmkWQOvRe3_Z{(7}S6h@3{CWf|llto^V%e>w%UdDchF7YBwB7kKdNq=UNIM'
        b'yN>j=^$%mmj?#~y!D0H7b|f*@e#P28;dg9`z=gLo|GX!{6^Ba8kEGAr=I&D@qEfE=h2OK=j`wv@8yH?26!vN#NOzUmk6gNZz2$)v'
        b'yZMsI**6_^zW-aXm2|6zLwbdy_W*`;sr56$wtj`GueGDSzja5_TH#+=DoK>^pzNHN=|98-JWqM|FtiDc<9I0}3%%Dy?V?6oE{$G-'
        b'e|@T5_LF^z?>0a<R2{9~!Kd^0tD-jJ??-$c*Ne_DUX7Y}&cXCI!HS+m8gxJ|`4^fu-|L5i_rU!?YY=N=@gTZ9=gre>?k^9pxsL4o'
        b'#ypz9cP`C|3ag}Z<nt;g3v7*LTN*cIVA{jLI8eE{+eqSNuPVk`;~r~mNq^F_qmNkS?3a%7+qyrMxp_B3hOq$Ws$8Fhw`u5S(cC$d'
        b'dpxhE+B>8S-L5&Yv#jwg-yz^>M~0S1S`)MVeV)^eWycziEL+^IVIYUzy$Sv*Hnj?OPXsvzcWjwkmY<jXR-c&^mmN<v9hd6Y|ESQ%'
        b'#tS|(laXZwji$95%p`Fs7Cbi1c-y*5WLDlT_H)57=Kq}4+pbe&B;)Os6b$s0w$WFSPr5CyaA!!!*1^;WC1tY#lwDI0^SLuHZ0uY1'
        b'wlAJ@I;LO8NWYkk7dm!>{Wu>ivFSxT^Xs>2qePHzM`yx&<8H^4FaYz*tnWQhZDT}tCPR5JdLzOt>e1P-6C+e~*$P?o=lyBSx03A7'
        b'6{yAXAKB)pTj%a$Jg>aff2-E_DEO9l_OI|0GI_hoHkaP;#J!c~!_u80Dp}$JG_PqsUb^$J$J5xpK=^e~m!u6NYM#WXq^L|;TE8@t'
        b'cfM*mVjLfq1WrqRrz^*XV6TRbb@Bu6;r`#n5#h6ZBgrc=EG(j;#_{48stj_YA=3Q%;dPH-gFk}Gh;<KQgI7V(KxL6Z207M8tNIl_'
        b'QuZ9LM0Qh%2Dn$ancnPBo@A>|uh}Qrv@nEN=-Jeu*JYK+iu&V9c*H&95wHNU3TC}$>|GYtvG7G<(djjwmWF~&4P_<LB18B-iT;6f'
        b'<LievMcq^EsHDrv`^tW;E?e7I@N2<nxok^y^xB;v1qJx%TG?~_(iOQlp~?%__Di>Htkjh@ZjL2{W<$j0rMst{hDDmc*Agp>@!W{L'
        b'Z|t5aF=!1TW<#_;oo^<ii^y=;y4Yw4YwuqrDl#nCea&f*cEZBZV_V~jNNE)n)v>n7ASLpO`jg$V65jb8lO)7#2tS9`V?FHW5?Ike'
        b'oA&j?Ig2sj>wv(u%jLoafQZl<B9PW}TYs-$z=Oj&M+{NQRDOGZTQ~hCTFV}NYDqUNJwir(Tppr51j;tPm0cm#`aw?fd^r5MON+}3'
        b'R$L+$WPen1_AEZKT%NmBz9ONQ4;Lw{u6!p83(K>3s!3CRqavv>Ap+Cc0r^=CWFnlTysljvE-@uFW>Xue67X>bMZwps#@*vc&VB(9'
        b'BH<oLbkP}FwDQ++M#w3U(dVBvlF}_5hk7yLFl#&n3L4)kb4z`GK<J2t=n#ekn`Op+)n=Y^b{ro2X&56y%iDqjp)dW{PH$!ZriGZW'
        b'mu(AFb`vWD{i%KhzdZmu*VZkq;FTB0m90&M&6vrsEgh8xC%ItrhRW^jOE*8g`&!9z^J<B6`NGZp&*S^>t%6k{mIDxzAw3T16(c}n'
        b'(7d(xM_2gBP&ALL<KP;HNr&Ffggd;mU*+ZnNa=I3^SdBy$F3pRU^XWl`ImwaI>{*c#0-a8$aO7>&Lpqwh74R;^;`B9ss4T3NrpiR'
        b'*YY49T>&w}Nk;Z`+n-8xk_%fbs!BfW_h!vwn>QEwNTrdCgOv~TOGkx(tGs#3-z&TI7euRs&*Q5^gHQtZy#fxovwUP2*b%#{)o!11'
        b'8p0ezt(T~^H=-coEzKgsZ)?g{D1>8dJnn!EXSX(P%4EuR$ntX#`WRmYo8Y*A&TcEit2`p3VF8?}Dg&>oKeEaIAT;Nny=xvIIIwHw'
        b'^$0Uy2M0f7h3i?zcb2m1)RvH__#{mDDVx2kv8=VR<p_#=s41w))+q-6!tS23jIdzeJakiDA;NUOWpmQ7!L6+M{0-f2&^bN1Xq<mO'
        b'Joix}8SyFq>u~J`EMATcKFWSCs_hondd0N^uM8_k?}3B@op2%AgX|tQSC?!wz8i^@dhd^umjd7Gw+812xl)md*3`bW)Eo=GxMndM'
        b'1Wfq3pDb2`xnF9P(LY*lO02wLA(Yy%M9tXS?2^{q=cCuwir>6z<AQW`(gQBN&Q2P5Kk+`FCDqC|**Tw-n*V@dY{@JPmLTKHa3DmZ'
        b'qyFf%{v~mB$54xi{hMLs7jFE=9+~GYacsr3aiH!|>SdN%3sjcvA6ODMQ1N1FLrC|41+kGIa3bTH?mt^P1wm=No$h$FB5I9U0Fo~y'
        b'M1HalCl+-dv2=>u{boZbJ-~@$-Q90kI#iIg`7?U`R^sZHN8uGo=`bUa+=+eNP5%b%QLg^+?#of3?u$Py(F(tWP^st&s<Zo#mSGIG'
        b'wxNcz*Z9eDk&Sjwm<PvLN&w`>5Hl&+7WY<BC8(hOXWNBFxD`?FMAj~jqFt7<&t?6aEQ(7C6SwIIm3H=dNplt+@Z4A6SI`Y+Bq5Mu'
        b';vUa*4MUI9bJNpcIp?&%`9ZPdg_|`cg<}U%!49C`@-H)gq5k~!-Cw1IEWYxalSt_l%J*<>hE@dnBR3oT26n5&M@Ar*TOm-C7s#I#'
        b'5Q$|b+)6|K9v$1B_Xhf<M|n3TpUS=!3<sH#O0z+%G_s82a%*Vux}=EF7i2EFs9$P(p;%;o|CX)7GQol#4XhVd`l5u0l3Q<fis$ga'
        b'3-aKWH1yH#$;1$fj3~i^+b#sE=sgxTR%F1H#q5(3BqQ|4`PV@Rlf~oox(5lBBaMvsIwX-h#VE)wEAvBsQ|g(?&YsHlwD)Cam-$Y!'
        b'+IN4RoxfqkgZtoCXaJweMyF)Md?FNr?e_ZhtjnvPm=4~@=6kc(_93HsWM865BV|L&JNd%@N7lOsG;w8*<1>?|VXz60h~Q%~5Cqiy'
        b'VrVN+-6bhSz}gR_8iCJtmw+I$whM?nL&-!70qL%wRiJh^iKYT8E5uqUmfa*&YAx(Xu&vg@R%z2xYrDQ`tqSuycLKJb&+ngP=FYw6'
        b'o_p@O=bm#P=PUsU$2Uyfd%V8=$-aO~VV6I<cxvUT)lo$g&gcoGS=toR5#RoQewxm-G0-KK(oG8K<?_pBlU{m02C1cBEC<`pu<qpo'
        b'$8yQJuBtBQ*OSh3lg=(@PgkyC>dMznS7cqEx-+a3Z{U9uFd^(F?Ah!m_c?!+fJ?=Nf)k`<>#1jo@||hA+!qDIN!@}vUks}lY`$(X'
        b'4JI5E&1(U}>2_=7!S*L7Lw(o%xTIuo%~+_9J5(|tuEcK*#&#18>b!4Qv%0AZK{b3`k~@Dg_c4GlZrWQ;RSv>zdMos?v1Ou`P_oy+'
        b'+^BK(yd%vn&wY3Oq(9M2)MbA!+xtCL_18To4z7K&QkH^`h(Qnfj@4beZ@y5KSY>XwV7?6q!ozLhMHZV3oezRgqsK<XKx$<IJ9LMI'
        b'@jCQ5H(qgCznqqpm}I52K7wv88{m_CS|4fBN3G;{3mp0tp8te86f64MJ7SK$Q*N^CB{u|{KLtI}tyn(Ao1O>#H(b!7|CK!+6vkyX'
        b'MHurwGKMXiqI-F!4wwgi)w2n@n}!jwzEi6Yv*|-8&sL1Vl%R;EMxw0)uNa4=mSL%Gc%HFqzr0cQ_T!PGBd@qdUa>a6;yC;q(}Z-u'
        b'uNI)WxK%hMZ_$VC$@eLL!-tcf&bMR<r=3?$%K&_T2Y`$$Y{)VxqG&~gDeEzlVhx=&zoDI0M4A*doh5C!Oe@wpK3suvn<KkS`n9wo'
        b'lsW!N<h3|STX1I7w)o1_Py4?)7m~P=bn9bH`ZaESq+1{5)<+D?t2+(+V<kx6Q|*NC_b}iiZHl$oeKM#8+CMV?{%Pc0PVuV)!3*T~'
        b'AIjg7`y@J#$P&7oG|YTmvM!rBtFPY#P=n{kN=*6)Q}AQ0!9ZtIyEG%pq>nVW7sOYjMifG=4t<!ptMBsEIa}0xK+>V7fo#yaTZ%9s'
        b'(xG^0;f=2S_3_BrkVz3y-;XZf+&E&FSN&kJ;`PCV@MG3m`3himv=znZb$%pEm~cX?uT01;UqaDcx_trXN&U)O`V|ao1jOScDn%?{'
        b'51?-;R%AxSWoZ==D#aRY)_kC(R<ZVmaerL<jr;pmipa=9BkKgB#<Q7SlZut;*{@Wl0(D7INQ99MZ42HOPwS(!`q+>}Xyz?_<l6a)'
        b'&9A&DGW_s{C<z(yibzY>{=Q!|c4c?Tz+!RC$IdQse8zL0#(VlHKpN-@*p2B|0D@kcjwx0^MF*<z55L#Ne;qObd}is{e`@WCq&Ak6'
        b'2#>Ho%dpDkNQOl6YuRc(DH)PNbpc>$6-78nvk^>ArVWpj75@00py(qfCw|T%@iQO9&v=!&d4#Cy>z>D4M)ISnpY$hbOXy*Ar(yAp'
        b'sPdt2X3tferK6+wI|p++h!604ep3OL_ydx>d+cym1iji%NCvM~;bhdTKh8d04Y7Rr+jO~YS#U(-vZrLDL9e)iUU69dV!gDR`54Vc'
        b'5rqYzmtqQYeDbOANh;rY);}UD`zx=nMYNFc?QRzd1#CmN*x|<ElK^Odr@S=d-9`H$lYcK}%Ks8?8>a{q9i{C5VGmr!<b~7p@nhTp'
        b'z9Hl&)O#Ns-K{ZvyFu73dR0_03OdrM0C`{CsmEobcXqq(>~>f#SWoO`jw7u4%Bs3Z;nCA2qyO3M`W`-ggpTPsLa|f(3v8kI(bya}'
        b'9Xz%|a{2PbzRku7=e?MsiCjyEv(Gi++jYD_@u`eijX3L)%&h3}?+d+bhL5eTo~|7rg)g`D{jJT_8G63ld8%D{7N0;7=7<J`=Q?Xv'
        b'49DxX{?si(1Pu4_86Dm2`WIAxv+fdFo=V|$6mAQ(bW8%YPJd_`(r-d>&~Lj5ur}P%Oc05rZ{AI0wB7HBL2KH|KM-dB&X_E7gFp0%'
        b'6&>kG=~dc7EBsrZuc~^H*dW=iG540oB`Q*k9idc&)MAT{WSITjl9rm>0J<xh!t;ItnC9N`b1g#!ZOvovJ*?p$h{d4-9%xPWA6Z>I'
        b'Kbc7hg?=eI;tXGR>y{F4vEU|G!2SDEf{x}kkeXxfKO7N~J`KHX*1WH0%)PDF;cFA~M#LQW+pJHyJPH)5y6@T9wPD;wV+kKoBfME>'
        b'ub6iof)38ulI)-QOm$+~#>uoqCn?Bm&SYBs*Tp?)_^}dX6h{d#$S=ZttqYa|-7-?SGmT$?aCj0M-Mrgn*lmpkvYurgN4>qivS^F5'
        b'<?zhj{M@Sib#Du_@7+tw&js$%lN+?IpebG^{wbKQNPC7^#QxdL3zDW()47ehWNC*UW*a7DH@60AF-IGZ3v8DK&MrK=kg^8vZg5%h'
        b'sgBTXddr*9OajUU8cC<RBW6HAKAV?LkahR`r+A$)o#~nQHrXT8^F9XD%`RQ4Bm){YymNhKCX*4P)z2%?XQ%C7zo~swrhj^&G0iN^'
        b'Hb)zNXb8=W5&o0aWr+%&HZ$wqerbJcc7fCIW1F>ZK8Ce2Keq8(o6Fm@<U$)-c4?D!;_E+|ZB1KmgUkM}8K3;t-iPtsqP-tbpzV0p'
        b'5oTA7q}7^z&w21S1J{=sw>V1<&lKh7HX{0zymt>C*Vom3i6+w*BxtV>^naLFXX7)yNGuvoQ=)_0S_=+!GWJ?@&$gEo*jy3zouTq;'
        b'7#%K25816F(Ebvbj3wd074=2M>hdQD;cu`$Yd1e+(-j`3J16Yx?MB`rbx}gMD*|xq7TPteE>&QuqD(Ts`cuc4|Ln@XD0BT|*Q6^N'
        b'lvK!qIMOro$z{wiRo}imq`au;4m#~&IdZbaMp%q@4z>qRjmm#FbIFy0PxBB@b_+e5S$RBn4a#(BM%VgKp7XHJ<*m7K#-Z><u?Tn='
        b'a{gRG2*Vc$BM7wDi&eOpzZuiYrS%IUnQwMgxQ*pfNT@&f`P7*F@6##xrAbtQ!<~R|N@wMT50k!PryTP6=$q~5Z=U~R<>wwGA-x3I'
        b'6BFJsKxru2f{%sCTf!EY!h$Zgg=oV9vnF%}qN^u%^}e;sI<m`cOZG?}+n!qIkNKEQTY?;63-`XF4#`AE-L@=f++!9ag;{H@f2E%e'
        b'3yf-`!-6ABRNG`5Pa7sD{Y_yDHV2g&m1=Y=ZFvNN1tnmItyGtEn3LgjSWt-Bhc<0lKyL{W-eI+2!M3o4XHT}ia{jlny%UqhS8}x$'
        b'Y-~#)=<22|a;TAsLS5b4v1@`D;dk?upR=3WiMoHWP_K52Ji?^)f&%@Pl+=ASJEs5-tUuwo!ES)bMpq>SfxuTH$0@pg0l8t%t|{Jt'
        b'q%#z0`(RM;ZSNJ>56_SxZx9x*3*j~xiblt-9%JeCOPa7?^Zqx30$M{u%w#}<neu6CY%?}Yg5l5*N+zbnkYdA~l&2e>PsvT$vG~SH'
        b'iEw82E;sNES~r_wEm_ofmP5e@xuI;HK@l{4(b7#jG4uq6INcOVf<m#bVk4-epzty;>;kQ{B~oPko(kE$=S2NGMBOrs3~B(qET93O'
        b'=8u3Tt$dmtzf3NMlqof81*CdMy8Qrqj9VEBu6{v+!dsX?XzD?t&z~zz3<zPE=Ix(Bjvh4c;bWnXU3`lenqWZ?I%v_^Beqa~<`4=U'
        b'k*oofHM!DcEr8bK%93+5xqf+hGZAXF&=~ne#9#tVMGhwYYnI2pU^hr|1`~uRB=c2j*O-FudTLkil3muPc4>~YcF%lG4u9w!7Wq2Q'
        b'?9CWlw{vYqZ|eon(6bscP81wXGw;wY^LzIh+u@nC=hc?{TrdjiPcF=;Z@aC{2|_cP{TiDwINqf{Q=7d>nmJg|yN$_U#$V~^t>a-C'
        b'<;XoJrkJRuHc^>_Uh!Tq$c)z-b<(DjP>cC?MR|D;Q5S&~SH3)Tp(tOvty!mA1Q=ic_}D+RgKI9GID0q~SrtCt4*-chp=?us#Gv|Y'
        b'E!Rx2_JA7MZ&P`jX0&v$DbzRPl?E$dmhnZV3(QO?@Byp4{IE|C+3Y1V$0Q)XHn$I4oiJU}yB?T&$4%CICc_WPkLPQ1r9<2fb%qu4'
        b'>VDv7=nJfwUu?UbF{tl>wgLW7L&46B+iCgE3<jnS?O?*a+f!d`L$mQ>=s^MJ>_IM(l^j1-9!%7I%yRU(1oB`yX$;g@iNh73J<DqK'
        b'0#EUbIUT@-m|J%?q-QjjxC;)p7KL<K(y}d^q-j4Sq@`t>&MeiQp)yA^Tn$$<)fvs?I`in1zW#~KD;ctHzR0{S1kKojgW@--AREvM'
        b'yC7}CiR68^sNrUdUTXj2jQM7ZLaMuVeM;}mFd;^a1~|P4vh_b9n=Ykae4;-?|LN__FX~VrPOzo{UW*<x-lM>x;#vjSIdFM}tQTDW'
        b'w|!SPzYdZ+=`(gx!MF6ItN>j+AsQi&{Z%j{m&^zcu$aM<`NcQ4g~!>93udNpQ|5(?+u3F(Jluw+7bZeiG0;_YJGill<H>`|N*`Ny'
        b'hi~`+`XW8M77Xl^!M;IKvfu%cv;<>r)+Apro|a~uI2wWuJ^l7sbU{Xp#)SDW%sPP$)=Za~$nXPWSgV(r=?qoMs8;W9()$6#9L#(n'
        b'<HY9J)zE8?dTS$ejlgvLSbcj)Z<gt5hUwB5u5y#L)TDfCKDWT`d6xxChvQpvvD>u~`F6AWvIqKSysv0|ewaOQZaRYq7rX)0=%p}S'
        b'rfuAjc_HG9^k3CR9*(#`N+M5045nO2qowH!Yts<h4qZb!o%zCx{6qHCg784ui{gBxEMqVy)Mvp?BD-Km;g;=P2ZlfkTC}}u>*M_T'
        b'1A=ZL!a@^DF1WLbTb|&90Lj}hvjHtu4B*>v`?E7g_scb*GBds|cD^>$FDr3fpK#lShTBOuSnm#n{To(S^&ltLcj#MGf5G5_uVkZZ'
        b'Os+Mi-ZduccMNk4X|v1j#+nCDO{ps`w9t#Pwr<bb8n;USpO>@E(s#{iAEWbu01XD#yX=8R9EM`6F@cssn+WJdjv!y4Ne*FKaH8VE'
        b')>Ch9yO4C9EjUsBwsYHs7sWt)oTDweEYimwNS!ucD36`u)<V=^#4psy(zN<ujXnrOUyeQ`V}C&?Ozk20Uj^!NatV^3u#ti$=U6~d'
        b'$4$rCZOz+UIZ=M^Fb&p*Uin>d&d|MWqn?-<dA}Hqbr^>)g3`ijbNIS1c~?JY#zOJl&l&3j#(ng6_SfboNkFGLgKI2!!X_$BHwjhf'
        b'Ui-=6+Stw0>H{@;x&0aqvqS$qP!u)jV2;C;*v-q)%d~nw&lJ5Cl+Df9)eo3U{=FYC)|&uzOWxl3+f#*U7`8z&^buQ7Rd*Q}JjX@B'
        b'BsVzVohEcqcTKKm8`7E2nOlnB26d4!+h`7LSY=WKO)3^PD8M{(C_+Xgl`xAKrn?DR@1LU&P~M)=wci>W4C?kB(=W1rPLC-TjW?Qj'
        b'3ta!hm@WyOX54v}8W1AB{SB+T{~x!7L~(*#vCOY)(2`&v?r^VxSLGz_a7V*~{VJW~PKK$+73;Y|o3FMULqR;<u2{}gxoS^``b6H3'
        b';}X{?X3Q1qaB+KGaRC1tc!t(I1G3~B6CIq~+*i=^*5o0d(Z4gUzcbcM#&PsnW|NUSe9`LP;17*UiAlB=RXE#tCC^Jzo+gL8g-j4a'
        b'ZCp^{R=L*{j8)#!xT7N`xA{kgb_=}o#rhMRz>?p;W;(YhEiu}dw=W@y((z~NYP@==NfwPXMxtRf#bvK#fmt?4%%f*ry370)-hydS'
        b'i+WjW?svjAYwL~)K?Ba^ZR=Hj${vvL3e*|tWRU6U1>15ncXaa{Zp!{4P5QseFWR-sSXA0{)bjYgXiI5R)HYLQ3%dKgLBd_1NBT@}'
        b'IWuO#q#Qv$#XZll!;%gz>duo2{QOt49KBqlU!c_oWPJ~uL<+}_;O--==_uCnCPoHp6@i<V5Or!yS0>l+<hp=h&{#AYe+eldh1sRf'
        b'x0exhPVC*J?4mnk3b|Vm07|UrJ07<Od4qiwOp}~*i*$E=<mQz(qZniz_eL_-4B)@N=M|t$qk`AIk`qE2%LolABjq8RvdgKWO_REv'
        b'BGhZVOtdvO0GzEWL>ze=ARefqU_!2_$Ak$*Ma|{?&lLwUSN&nU5Y|Kh>lzT*bLKz7Mc~CnImNyqupB@d8sOB{a&FOH-98k`ev>?Q'
        b'`6!>UJ_$uX91tmg|EMVW7%B=hQ@WtmPwp+L%SGXy6oJWtgv65xX?N0kj$C}*4@eP`sCizZQ3UQu)aV0;9PInAQ;<5&9}Q+)!N6T#'
        b'Se-^@0BNE=DCdh3&|Qt2qz7L+=THPDB=9pr`ULOfW&~=UUXZy%_#F#{bphWD9~~tbmjue+5dMcPdVhBN)?PESJj?LWtCDpBWSkhj'
        b'M7m%rs}U`bf8-$}hSD)i6N&+0-Jv{<UVQ0k=&xRl((i-jPpu!g<R9@h@7+ro)wmK<($&|Dq~Ml9KB)+RVV|PTT$QQFlx5<GV6+|>'
        b'!_WTq%&U^k!Amsf7LoD<-LABRQr$<NYtL>>OWGyBBT6!`$vZ)1g8>ZFD;mJh8IV=!jvf%8@%tvNajzNRqY-R}p`46{=n=Z&s_7U8'
        b'rU|@NUWE@el85cHV_6vp^<6J?4H;nwb9&S?Bpm8O^#>;G+*MRms=Ihmb8aI%>(*W5?umj{g*r*ZS{kV)E~lIn2tPuy4A`W(AU}KS'
        b'WYf^-38U+jvA54CJOp0~td%hp?rl#O1XkY4P!3481!RVi!!~!aNgu>4HgLNLK{<*A8Mb6$%GG3f%1wFTPkWwmxMI6uJ`3{fqv5;!'
        b'nkYjc{E5Xjh?3T@CKm;A(rN^HHmI{_<z%+;PJ@hTHUfnk@Dzn%+8fU+lTlisUAo50Cd*8DY!oQ&=1NDTpY80pkx|Q+V?B(zZ=28S'
        b'jSW40lRai<D`PR|9*iZDlq^`KRrx{%yFo161bW*Fl0%63XEosLP%HqnP6aG)Q3SvchJkFjFBE`TIIrj}`}?o|zNl*d)`RL!W#<!n'
        b'+JN(N0*QmKPnMja;GrdO{=v72qz_q}V5z+7*4}()&L(0+gtoH)eBQ<x)ZVP=S0za{7TbF2A3pi;Jx3tS4?j_0_sQR8NBbEUUw;#-'
        b'D1Xut^62Yp1@@5qI&`j@!7FU~u4=75Ot+aV0K{|jRDu5hOi_v)S2PINKcOZ}D#C8Lq!auR9@qOPk^OU^YQDxLb-Y&;eVEEK(8FCT'
        b'NchNOOsGJ<GQ;go_6`l@&1n!6?LNus;wOw6J(ZlUbxAdPg$AUnMDvl*nTWg36b%T95-HVS5V>T`Rnbjo^h;FwrFqBM7bFL+iB^!D'
        b'QP2DV!G1$P@&JNLAEr4|6uxjPNvITI<ZoUeqJO`yE&#*!99`YcuMi18M0$(8gw_SKCXp~d=v(vqTg6|&RMUE@qvK%zc<V*8x$Q?2'
        b'*dZcdaT;nGPc^^aY%>gqU>a+9ALflLbOJf*fp_g<)s@<Nt~goj=%hk1rl4F>WAAva^)X`{t_++HqQ9H(`2(FXTHzXwsswQ#Yt!BK'
        b'9pJmsd|{87S$>%ed4Xs7tKj^9@7w#av__&^Oc}mG*QGWfH*Y=DZ-7<n2hFs(qm{MO10wBV_TBhax7A&{H*0?<-s`HJO24Fb-Kn+y'
        b'P&+N~_|ETe_uj6J8|&$k#!Ys*i{keWh*qB@92XzPs%?i^m3~odx=O#8<Q)wZuQJtUzb1>0qi%uTqYs|65M!=vx2wo&&#Lr6xAY4^'
        b'S;}i=-;f*#mgEQjmrAi{1*y_gD#c=s^ey^um0rR4RCDXi;Vt^Gq|-2B_nheF=lzz37KdiW*m%PHD5+y`1qvMT-?T0jE6MfA9E{}+'
        b'y~~bSaG*rOTZkb5)|g&tj{>{daAA2D8A6iL@lwl&`<#|ifIX&A>P}28uQ#692j=?t+3~K?{#sXmZSUz?>&99p4XNxe%oDb=Z}5_?'
        b'v4*Mo*9e%)&2FP{zpi7Rmx7+c>5{|ju`aW_xun)uwVxy1vD)6ETC2Sl9Vhbq<lB6tHp9IatWGy6$Q;X@%us9fR7Sd1uK?0-ULaoe'
        b'L~VAxEIJnG6QIJErPtM}E(o15IM6UHhT>?L2I?%Q5ZuxSs?Z6S1<KusW6zDxaqK^<IF3!)1jIVulMSrUJdIAZ{~#>n0^dl41zvps'
        b'C;4RHqG8g<=1OBGQ7Nr@D;cQOhuB;No<v&Sg*%97EHN};eQrWeHg-A`DN;?-UM<J%DsaGXC6xX%y8f9Ge5>xFKhWFZDu5b&W|kLz'
        b'QiYL$*_(IiK7Oc^3*}!3T-$1USJd8IUOUO19I@ut+NXSB%mNq$_~f)M{=ODpr%$fcek^ou!qH)KJ*9OeBl@_cs6WpD|D>V0?=*X$'
        b'@W&8z!#X^kNV>od4YLN%=62-BF2^NxU3qyzGC5Sisg`+vpFYra=avGLPf%h)q4JA=6@2{~iX;2=Uj>`rAcP7`FRU#V)ViLowLV=7'
        b'(+JpynYicQzEBzTY~F@xorE9-TKyvQvp9WiZ4TOcU7{VT(CU|xD}k+(K4rBuIjIOt%i2Gt2ym%ttubCm*t8(;vai{#SJr|>LJGHy'
        b'ZJTUx=Nx9Y2L4U|&db@zV<N?!;6fc3jr!s_)EC0PaCZm11`KDW9Aghe;Z66=Zc+k_cQi;iAOTW;F?YVph26Ua%G!<nC+i!0=Q5#a'
        b'N{eqW|9aUat2KcJIQ;S?EgPey*7>zJ?(ess2l^+>E-~Gm)&)<ux_ckIY`)dgCN(zhZ*w>A1v5(4Io3J3*GzSeA{)}Hx|;N)@-7&o'
        b'KP7$5k|DqapRq$<A{!0*(>vrmt<&T8P5cGTAHVEX^#OwBy&$hO1-dVuB2(U)!=1sjp`^ODdYwSv-Qk{9aptj*-c*=?7BiB5VnsWz'
        b'Xa>dT_HQtZ_33pxQ*5FBttYfL+~iLnjxo#jwo++rlr}V=4R2Lu1VW|FAHCcugMV@*)XYaa8kwu|uCeC9L)R3!)s&fP7)0@VGfsd}'
        b'p5CA)8*I?IHUiCKis35CEEWDZdro<Fa`}NZ(UJ|47I#EbMu)h5Uts4vIy4}H7%o9;UZF@{A;tR*@vD-dyDanzDBVCeWQwcwr01*Y'
        b'1Mxgd7dp;R-|pjfb57hn|DGPdtoeusGgI~!D!WT&d6Vj75WTt2naz2hvybi^q%bwa0#6EU!E$l~at6h8u5aXRI@dpQaQy{TK-ev^'
        b'Ux8uzNfi%ig%Ti+<}kaiHPSGdJeVF{J-|y#q*4aazSJ!i-O)j<8b=<b<?Z*q9;nFx&C|l<qba<&qX5DWIkl?K`=^=d7B@6A%MgFk'
        b'%R<b}M;#*i_&B!-NBa}%6)$JgvIGs4f~y^s78{k&MX8^9nG|#?5@?EC3-kxnGG&o!AoQy3&nU;x)sx_Nbyas)@<~2)nps)@cyWe6'
        b'vn*Ktny)t3znkwEOrR1^LJuqH>CO9zq$e<vNcseI$iY114~h!2hXZ=gp!%Wmqj`SN#Oqa~i(iH|o~NOiLsRT1`Lb)g=KL5nIT!(h'
        b'5*n_2aT=QYN#nhtet=~j6irDo1{ZiVA&KZd<&FKwnL&fBHE_(IXlygh!!jbXCuF8eytD}lSb1up>-`#Z@<a%r@(QLu34XXdOMd3T'
        b'N{R3&YYGi$4dR^GalYZq5iQFW*T)%{_p6MEjnV3I#}THW5}jqv_1AUXG-&GDSWPI&<W*{q&lnRaO)g3DHMue%14ZpmK9YGj@`N^5'
        b's>$_}6E~opV~1zXC+0$HN5858!cK<zyN;mNaUK7A)bZ`#4ee&P->TciV%r@;6T4kAWMsKDt8QX|r+jRhThf;Jn8JbwBxn0<VGEfY'
        b'gb=*bTLN3n=Dq>^JPamtF1=-eX^XsNOAs1$f0}_(St6#jN`bxHa20Y#T3aj3X2nd6NiQ{pg+%t6^fFV}BE@}3@H2%i?rb*c{h2pw'
        b'B3<NK+7;_%XMW^p+f9>RtaL#CU(d3s<r9(-3Hspaft2xhn?8W_bGy={y`bXI`asXIY2?DrKJ(BUrxmOLZjB4tGkcU3pSGk@x+>9t'
        b'WYI8;U(%oX6>855{J375E5dV8Q6rJx7ueiX-bIBj_%Sd{x&`)sE5@@{)z<)P#NqcQr^YV1dw17ZFW2PN`WCn=0<(W3D2$1_73Yps'
        b'=D63Wa%3txxFkoKu`AZ0%?V12nN;Njk~~$8T$Qt6C3o=@GN?ku(W}&}pCE+)g{|tV(XXvh>HSp}F`Cg`$#Jq(J8G`>LVeSsiMgF4'
        b'FtPmdHcp3ZS}Qrw^_V<sJ{2FD&m)AZu~_wJM@^h5Hht0+9oI4<<Z|b!ry*mo@05#_UpfDSZDeMx$nqpI`iBdzMBj;ibKjw?o9Q*K'
        b'*K2yyYpm@xSFYSqmiTTzT(=Cnbo0=QlXS?%f6Tv`QsdfR)0<Lb-CqM*`B)Cj$kIb^Owx-k{zG<CQ{(z`O|QDf`sbP?&R5`A&Z04e'
        b'3>99C3dh&D8ftpuYOD=4FmsLNEQW?(x;nM%>&5eL#?-iW*Yv7tth;NHuCfKAu{&1F{co<U`Oep6tm$1*V>Q;G%MPGGxTC!@Pu`Q$'
        b'mUv2@<w0U-lHI@?`Ww0vfBYD75AEeypq{6h)wPQ!B)}F9R|JruW%@w7$P&LFiMD-ceKpyZ9V1J@Er}=d!+taRSdHs*!=x+u`~`~3'
        b'?^y}?K{rm`(+e;4)4FrK)?&t5X*>RDeZwkl4r3o)ud=Cywsc~ljTtkLi;Xd$i2)-flRORvbfu?`jm6_^P24_Ie%L+7aTaiS@KASo'
        b'2D%f$R_+FMVP=oZTkD_D*`DoP+*UvK<W-zgewS(V;hx>BO}~QDQZNL9b6iDk%b^L$ITz<1b~mv5fpeI*aW#^4`-IzV+(z@5#p1TK'
        b'o*y+jT}Dt&((IJdgz`!rv$XGDx9}3AbqnoXidOpuNt?Ch_{>2+qHZl_Q-m}96-bX(h8%r|NGiqTVZN<rtXRze&(bE%J}k4eQP$TC'
        b'@Y{B#MX{*u;}*r@mc020Kno#Ufwjoetba0Ox1oFkyfz%Y_oDYPMYyGtBFRogx9<nC4_3A4f924xbnBzX^#6}}166r7yP`$$t1IQw'
        b'z2%gpoT^k86E$Os{}<gx6}3@rMf9iXZTfA+HKaqaa=5g))R0{*LualS@&!^ff};irDx35E$d<RGJGK$lNIOW`cUcT9nP6h*9Treo'
        b'w~!cevO{m9=K<cq7(C<zIdAA=mfCMGI&u;n{*A-NWNEr1*u{M!TCpPO7<5K{WNLGr0i7e<WRPB^_M$CXsLSp%ec;?rsA7;1d3n>i'
        b'`}Z6QS@QzKCkK59;T5Fr2=c}s>I#2saYfkFzp|yv+wAhUz7zh9mG9<hlw`?KEMfo2@_8$YI}E^)MTt^P9;yDd!EM>w`EjQwA%?Q)'
        b'mE>Y?UxQ6)*R#5;Td~$SyWxw~EyU0#ESl74qV6Ns@BlFS7-XI9+UFeO15(Q0O{4dJbE+7^xPV3Rdte?;Dq}&~@8r%caykcv1Sk>5'
        b'z@%`XAG4g>Kf&iV1c>QJx`a310OCtfrd4{e=eKB_{QvZmjnfa~$3Eg|=*7+nJRv_9RFv!q$|W#ZCaCWOT$UdnqP^|OW$iw;<AX^!'
        b'QX?#u{j>LMTIj{z3p$|CekV+DmTuQ<jpHj{n!AT%qb2Y$uU;V!#z(6Su4+SXwZZyBHFFaw8`)n`KP$qXKmOvJY=;fzv)zhu$!M{`'
        b'Rcz=jHdw!|X1+v)yi-Ho7IrQkytfV|12X_VnrCorHS}&ZSjVfGODH>10_KlyF}SuEdh-n4;3Ny~$$qhepseKR#;s3f&&cCv>K?Fj'
        b'IC!cN4rvD0W<&30gLSBy8AL#Tx&N?ZX11+d{tA>o(cs!(=-ptj_E$5f{%`(*nb|XrUcBu)IlNaJTpB~K#$f$>HPeNPv<@!##%J_y'
        b'wd>c0-rpd+w|5=bEzY=LKCz&ZNHg!Ke``HQwT&~nU{Q{DgK`_%p!^OgSHKOK)4E1M!51kPwjEA6p}$;_JebYtAV56ej<hpCbZ9O~'
        b'P+d<C`C#k%z8bR-ZVSdCY5(2KfqtA6nnHco^^JH<Ztg>lTI$&{^GVjs|L)&yTpNT2SD>Lc&|s~pW-3t|A}-AJr#GJ`pUd~K+U0BL'
        b'^)*;`R5O3{_EE%%1r_|*3(@orbl-#V%F}RVG^>juVr^rVLm(e7kDhZONgRhOqo-j^wa?eco>LuWSMT@rGR}cQcKiLLhb)qdrR6A)'
        b'9~}bvgYEeEx|ng8%eY{mVpUF%%2hDH%VVc?Sr1o`dq9;)X1*?i{5h^{E&hAm$HMgfYPZD<?FNC&wOgyFbM&EkVSvw1IrviDkiaB+'
        b'PQShaOcT)TfUqepjUv2RU!5|l&aVb*1u`X=DRoCRDad|iA3E5?%_42q%-)8paW^%3sY)-)Tguj*XECG!Bm?s;nwDStF=-e$6wO=q'
        b'eGfr?fOMIgyO3<*GHUf<D!tMk!kY00n=bf<;Q=zL_CA!i-yM3_d-jYQKWU0XlF^gZu9MZhC#$Uss+j;pY>l1(Ys+$(+T%iYQ(g#2'
        b'MuBDb$^3|{Iq{$}n;LL)OM^`6qP%8bp5OGt!sJlf^F+#t<e1LGDT8DfG9_$aO4x)V=;YCeY7ic-dsXKzQy_S~#guP7{G^@RgWG;?'
        b'cE3W6xvgT-r<>25MkLQTJZ>lH-al2-iP)Yaj0SaE#9=ZxgpNFn%H<4F`GFFWhR?l0)pd7SuzIxq^EbE3ZM>!O{^{%?$}uPg;)$nq'
        b'mmdOtZhvBezX$Er^gdkPX!v-u`IOe52-&24o-lYe2mf>EYnIbB^S00Nu(ha~oVTtGUwor|mr0CKZ>gz>Xo`9q9a4#kAdI`!)ahsx'
        b'YS#ET=ZMrS?g>*H>FAKQp_`l^41INk_~*FUhW;j#gI>}!2z5NqdaoewT6{zP6lfIobXM0tW6N2>$str$TivUzwnbnJAGO??R_%yd'
        b';?exCm_e)7S8GC-bo0!+lS>oKCX(MkXmW7-ZB`Y!#JnR#W$ZF_(&%<B%KK}`i%#7!Z<TT00?_5?Ui7#szPc-~!apQ`>#2Y>%R{<)'
        b'PVVUM@8G@T&$L%^cabZ2^7qMZg0Z9AAzjQ9UH}7xyj{YKqZbE(>6cYIJ{;{y+6DdFEn+@F$!NY)-X%9khA(#um`v1;SY9-`xn*5a'
        b'J-}x^M44(N*Q1hoD;^-!c2#m`J}rq(GAN;bUt?-XA^;&J$aixIACoU&du7$YAOmIISO_Jd7#L(sEqculCV^{3%tQ17^hd@K^Am>#'
        b'3jK`18`s>rf3sMnzi?u9k1YBy<=I8rP{0WLckF<~dbf&vZUT2(O6~h*<GB+cOuuE-H>w6CBVe;A8(8L7RWA@u3hNZZ%pAox%UW=Z'
        b'T++aMQDXXF#`w~%D|J$*S!Q~gA0A19iEeo@?IajBN;6A7w+CKJ;T0`l*0bTMJd%%&D;jR06F}a093FN6e*qn4RRmO_N{H*%OqTx`'
        b'6QwOU-*7L%9KF{pjZTzWKdb^lGHJork9un`srh+kmMek$H4tPV$)}##m+;7s0=n^qrT?Q!?W)>CkMIWwP$tf@#rG>w8PQk4Jang8'
        b'f4Zu-uc}+fY~hG}P1t(^y=9}f@!%2U;T@@=XSj+)Zw8;E`Qj!Mw=SPq#`*WbO?<4yg3-ANfE;~x26<8tQGeN0ashWn%IJ0c@QC?i'
        b'R{mu~7{ns>G8SOSiF+$~NuRSY9eS(q{9~>PBI(~O7mf#=$F!`mS#X9%%tWa`nLc!GPrtRHYJ>;YC3BW*ins~+lHizR_I|k@BZs~I'
        b'N{{U1Zqj@H#jdJ`4kedx)a&Nuy~LV;y!S;@KJaxII04dDvyXfbS&OPr#NR>6u6d+iSpQJvaFfbrmZou&1-H;nQbKj?`ngOl_x;b0'
        b'1}#ea9ZCZ@dCbpnGEo}Ly^yS|`MFMjnQ*~mO|PQdl<Apl#~D&tF{eMF59_N&h!0QZ6?@aHn2E?fl)<QXnj$tfUFt?od7BEmanB~w'
        b'mb1{Bfa>u40b~tRRyOAo!G+l@duhEdlYq#A7K9o_+H+g9g^S2%w1tbcmKRCBHnl=~u7LE_q-JXimuf7fWS}N>yS9+}Fm<eO;aF<H'
        b'*p?+F=eBF#t0*a?$z>&lp_#51eM>AQS{`=&WXGtok6opxnsQADk>3sE4L+OIzrb~rP+kQS4WmW)pdAo0s5~&b#ZrFoHHFDe81pH{'
        b'_y06TnSvS<5+j^qTP*s6uiasG?u2|p_gSx}c~2E<%faieb9$P3Uey3E8EUw~$I?YrD*8E%0E>>}uk&B-`S`(F$+377{T#_RHt<c)'
        b'U`8YVMug1pvBQE~xGOI{cu_K()y=bi_F(ai-k&Nvgv?)ea@Uro)83MH$f?s*&w9#!`GN2@H*Qq~aMiHC)l&&NxcyxgEl;EhRXBfL'
        b'?(dMO)uF<xCMsW$6!;%~dx4p!_f&>-ZEaODlck)LHS>-YWcqjT0MM|%;zH#B!Mw6_c4-mAkWVh=Nn~Hu-C?mcbfo__p5cz-T;<R$'
        b'c2Oeoy#ei&x8T;HN{3tQxkxbrL}6P2@)~h}=UjhVxuw6qva8;$L=5gJ<jy)?k7rJl0-X=_adbYE+Kt;)WM?z^+?Xp2#1-;L0#lDS'
        b'Zuj3SRa=(GPY97Gt|OG^tC^-ObWk$y(;07y-2-~3VAY{gS9j%D=yR(&E6;z*AA1@*e;x@O{*4Kl{cjIe9W1pN`9%>jQ>aPP%_f+U'
        b'I|);+=}`QtLzNM{VYlL)QVqQ{g}3UBN>$EME>_{8O6#$mOeboK(5r_tt(7n>H<_7(mE=OsU(0L^$^EG9W<O2})~m$cz<BVD9^(sV'
        b'{e3I;Jj&Bb(1%$n!dU+fL7!#!&SpmNO(;(*ioD$xH0O(~rgBjum)hQHOY!;nJNFdQws-ITIZU|x&Bc|RZyYm1uw!0*@chQe5VO&^'
        b'pC(Y@hJ|x*3o0o~Dat5*<Zgyb&#8Qa6X)WlxJQ7IY~TqTJU%cjXdXR1eB)_~lz4*fa`zpYb(Ne)9CKV8j_SzlCJq(^4B$*UnqSR$'
        b'evk;H^?y~)`59OKhh6n-rTYlxJeMmSowY_3#PGQYyvekZXU2VE<M3gqS^b+zU{3^@&-t4gZ)D;gk*FhxYyH9Yd8EH8d0q%Dyom&O'
        b'hq$XlmFmOcjsiC#dAFjH>M70R-<_3Zq$IB%n|)R$<MMu9UJ9<u;%$)RSVgOktRy7~&pYi0vCaLwLsc(GMg*x2D6)ijK|(Hv2a3o_'
        b'towl_mwT2HTigFN%LD%|_3AwfD%A@rNqb5tu$49?l=Q2c4?+*~v|vY12GgM!6_wi&IzYg5Yvy%?Qf6mVlqnaBgzR$1L&bMHY&3I4'
        b'0@&#;Kj`FfHw(P|f>%aI-!VmC!yU8R1b0}F@t%9E?(z&efDU<pR`O6J;5MTnzUodziv=p#AZcu@kBc6W*g^^9mFa(Wcn=_jHttSs'
        b'OQjolZJ|CiO<>_I{0RSg2LbvVSE;4vPB%i+>-U<uT49~6fcoiFOkRO0e`0A1D5_+L{ad!~p;y<ZVG`D3icc$0WMz7>;!=f*28=NK'
        b'6y8BJWsyAPDlCprT&VC|M?Dowq~9pB#88|sCHP4u47V*Y(Frk9^>D>pVl1EhLt2a!z4Ey->h~+=%B&i!FnAEJ@)pG>&?rwNZ<Vt`'
        b'y{nW<Oq)&OUgo~r_w&d<EJ{_vpU<Lrr5XLD+Ut1=dqs;4v08GD_4OTTi70nU4)?D8JNv)h)9>xrn@G*Qn{(7hD$>m8y#c+O!jj1~'
        b'7Vh1&CE1%`-CsufSj^H#X=aVOwSo)=Iix;_n%ba2;Is(5W)`-FiA24)K_ZV5x&B-+A^8qRXV)y*%2NW}edIdJ%yU?_%+?GNk?BJ^'
        b'3ZjuFovG-+XQ`%X3bvmVG?gNKw-yO>tD!<=!98sX=q`0`g(Y+sm^AV#OriG@ov|YZNq?z=`Ns|fO<?qrTaYxx`2@3Ky)RWP8b->^'
        b'8kBR<v!oA6+gyv7ZRj<!S&>x%Zv%vKDYjNJp4FRMVck+;cj3xY_y)=K_71`$#Zm|q+x!-;cn%?>(qM{|id88UsvJUPxgO`I$f!U('
        b'2!-TX(>5Bj`(mmbY%ade3xwPuemjOpQeeq`hFcGh#66Mk|MUod&EIU6HOzX{$Tc5!`;73JWb_OlK3mhsJTv=z8lE-iIYQ8+@#<@~'
        b'GeLQ{2-rA3^g9Fwa>UK%{t%v@`~{SlM^Mf&(cJv_J&Vy+0)<HP`ZKy46MBq5c#ZE)mW(Hw<MSh=aj9fTR7~_+`)uce><@)#j)gKq'
        b'v#};rRzjX5T(!8u@Bl@A6CyIILn>PN=13oNL!_C=4|<jqH!K7pI#YriGHDq_sn<c%QuJ?l0AGGWUn2NsT6d4vz*qZLbcES+L2NR&'
        b'O1xPEOF0i{$fZq3PA?yIwpr3+miA7U^mv&_0+q}g^01)A3g>*izd-<^cO&JBAIr_~$ZP7$U+5DN)Z~buBRTy&LJU(JNksCJ9<op3'
        b'IP}e}$Oyl;X=2C@6h{AtG5y!&fTNH(k5DQ8vb<YJFT>=jAm&4qu)>E7W>ROFy+4%8d4_9e;GVZUKe7>Fq`1DtKSE@tL(C1dNr@w0'
        b'!UY)Ep2#Cb0P{`>caACm(34LsjR+)zBKZ-5ocDqv0~*4(ES`S}`vehzkVm(Cfe%gf?dlfV|0SfAxNZz1pIQ{}DdWLkYF-)7{7ec@'
        b'-bxk(hRcz=-$i@8b<mvFv~i^bV8{y>4u}^uF$Pp`GGX>h!PULx4XeOpH1Tm1m7zo}E>Q=RsHqB7gSxW0gwHe6mDUPPgtkFn=`!(&'
        b'5<WljCe0T#6w`WXj(SDqXpTBIN1eD5C;2%v7A{m<|5D!jm+}!Ia|8`*(KTY|dCX0SyM-k*?goVZijv)c%nFk99q}CyWxq)=ucJgD'
        b'Upx8_N&Jw`-_p~kl>dS3;N=ao@@qa<_mq$BDR*1Ny?e@;W|WI5M6Dn{gg*FY$E?8NbA7M{eK3p0&mtnGh?w7_cSU)51Pw;x6EM#x'
        b'lla2DEac4OSd7mY5CHkuBo`IVilbmq1Q|5+8XF!$2#>I|n>AT5s&5~lO47=I3L_tnOho4pK;K0E<9>_qDb6XsQYULHH;cUTxI(<Q'
        b'9C2r*Soi_k_r&m1B$4zr+rd+Qz{;c8t6Alvo1r~E!VkHaQ&zlVBa^kmi%tgm?-0dC=?3pIo6t*~h_ma^ctv}>SD!5(O@`8f-gV_R'
        b'E5Ys60?&JfxLA6@KA!jC0jHv(DXR1rzF#$NX*b^<L#?@e^aSM~c%T#9#tvnHQmR6)M^DUmJyrg!?>RRqQDQhcDlf7BgbBI0UsQCd'
        b'R7Tl<f+4dkSgMFAr(#TsRps$81M|5mkiPP(a;VTko2<*rX}6T>GTN6>zp&}j!_oINtw|qRZaX7QaNa=yZr(I{b|aH2>rKxOUfp@s'
        b'B9t$hHmzD%ZgWd5hmD?BFbaNed%wd+z{PWe9ZvPi!Bx_7l-svl<6aS+XhdrU6eSOyiF)24AfPcG<h_s)l|M^1((x*!hTCgERe_I9'
        b'*Cr$*KnUecOdk9I#RAK_h9zC|(lh;j8I@g{rZXviEYqG@L2WVu$^$%P)>lJuu*eruYkoL-k`IIOF6-5&tlyQ*(%@Pd?OuUsu;`aG'
        b'P<&bD`VwYU!)*|49~PrER*hiQWLfWInM%t8jZn+CUMVAYsWc=xAFUf7!IUpz<dWX;GV6HR#C-I=9qYYZ27Lb+XSwrwFO_xL;#wf#'
        b'Vj1U|OsdL}J&Fl`wu}^8hszoWlZKyHj43`W1EsadyFgm%^>+u2q<MmbggfChpCc&E6Xw%*XrAb9$@l4fWwe0MX=i92u_A?j20mg@'
        b'F=Pwp!_>sX8fg@{I>u<?;Rjpem%a6^hKJ`ThHH3&{QZ=MhmBc?n~t)pj<WM3RKf{kw=i!AX6>K8rBhMCZb9BBEIMX_Vfh*Fako?R'
        b'`r-SJ8Xlo}28Z%ow$zxqZ@hhC;$z5HwI!P}OTkKxE+vWlv*FEuDl_o~V|>2REOXDp&YP+FLo$$QZj0jmRw8LBR=<WHe)czuZ>(7H'
        b'eo)zpxPz^?<vbD7Tt@m0i&u(OgEORr42o{tM@2~2ijVp&Rr&BtK7=twW;{VL^@yy(8!R?F=wiyq8q^_vh*y}}p8<fbYyy**17VD%'
        b'j{1GpTUKV@jH5Wax-T9M0k`h3=VRU&bNQhIDn1Y7DXJlcavW!)Pe)s~l&MnqV5BJj8)LSW$y<MlcJZTokoyv4DvpSR;*M-Aql!vt'
        b'J`b9{+HW4sCsz9{<JO~|FYEnXS(@`sw-5%0G96R=ciFfJesnGTZax|>|75w`DWKYeEe`aeE$p(O@wDB>gfOZBH{;8K{)c(0%*Gcq'
        b'wzSN{4z`oP*WWK4PId4Fc^mK$y6!Fr&AjiH>Mq~UOT>r1VHMAmHRX^J=4p-*C3!>aT8Zx3PgWI>#q;&j7kQSPUD=jWdH=n%P~`Yi'
        b'PTxyQ+o(J9qk~U$i|l_x&e-qYg_j9I+8K2G#NLP14Rbbu*Y%72^Q9&~qP~Cj1_26HXStK~V9q}x(d0mL$oT<^iFjnY>#+ofdbF+h'
        b'4WCzeK459xx!6WuIW0?Y2K1jew1(t?0;ker%;_Su%!+fWBX@33jN8PRaad*<rfgyY>ykOo!2@r-+1Q0UyC`nGQ1~s1%Td&Gr>D+o'
        b'G~PM&wz$Plu-A;9TL8~@{J3i&pDcyUC4OQ+9kP;ga-MP9zU=JMgK`wrtv-gRdkTx@3XMP;(=u{Fl&Sm(w;#{4%NhNIGd{kRaCVvC'
        b'yR*XNjB$0f*%Z>EqB~$ng$FO+9P95qV;YzT6Gdau?1B)`1Nl>eq*qYV2(OQ*I+FAwyE*o;v|-5W1h(Mkea{N-uw%y`p1&xC!H7bq'
        b'@!Qm&rWX|j*srs#>PzYJ1p;zC@^{yBC;D`5PmFUL{;CjaeNj|a=iAub)oGJpjV{}>Sco}-Acb3Bm-Ra$aL%KxJom>D9`f{E*iu*z'
        b'+|$UkBx51@Nq5;kLU@lQ1xX)s{F`7?yHv#kl2-|z(@@R(uLoc0LVeR^YZ~Vao&h`(XEqjby@^a_-rh^40BS55-+O-N-qxLC$wW&s'
        b'^a=`2=;eVD7(UF=(x3a^Mho+1kfk>1CxYKwe&Q=v?%cR>2c4SM>M_nquKf#?!Qm$!k*t;UAd}J4hq}$C6?f#U<S8$6@|?k5Bsz2}'
        b'`FTH~+!{FoS0WdKs7z67gktEE7CE8YA~LIslAVxR-X|`R3yKoab3zLGrNVOi)Fg@S6OXZw*)8W;-f>2y?oC8gc2=95i7x2tRw2NG'
        b'>|Jf)ft!{+74LML26%frDMnVrom=NqZVE=@-#HX@q7I$%JRo>bWz)!cdue9^ZK_m9#jKns{E`Jm;C0VqcpM|}t4?$XhdB4+%bt3S'
        b'gNk@zUf$O%jNhMmp%WcnNdHuic)`QAreD&_MFR4fqD{`Uv^!{Zf|sx<H!acGi35_PWI$B5$G7Wh*U032?A!;Fzz|($h2*^UW1HI~'
        b'@;i6X;6>-Ts^01Eb@*T*ZH`n7m;eJ*=FSW<fkglbSRCNP&>%(YVt;L;1)fQ^Bga0;YP7_SL>c7p*^Nl96?JG660%KNA@?SZBeYsx'
        b'jz+A}3iAF5CCCNJf3nCw5eIwBf_ZfdBso9-d7T&%y?gEQ?HK8+oMcBNE6Le!P`C0kfaJN%l4zC2q!n?$Xb^X3Z<u9(s!yxYnBAfk'
        b'nzRCCAF9>Qerhg;XNML9vgZ?o{U<B{Q)$GWlU$y>lXH0-Jj`vuu+yO?i?OHau(6MFj#J%4-nL(^W8Eqx1)3m{DoEHO#u8$jF#Mk7'
        b'Cp?{7zD=gJ7@JP?MOddw!9?8iN9bRdrxY~P=(D>LKBCax31Q#zOIV+mx-DX8udxGcXq2Cv2U55#sx6+|`M&#$^8(Eum6A=}^9Fd#'
        b'PA;Q3CCZc~GVw%jNNhYIOsmjO7BdCHN}DMJAWip%A15V8Ujub|&ffzkuy3+LF1DZ5S&9s7rsa=6`xRzRmqsSfJ@-L<14Or&$@C(I'
        b'u$uj*?kxqCB!VBknolj`bMxD>*On-bl{U2uAlH;k7aHstiKJiC&JjMjyjyrhz|}$XvGPe-M;OvkzwiA^>4<<)Bj~085jn5%6(e=W'
        b'97b;xWtkhoOaZ*L^C+{E^fRh<t-1dyZ*xBi-DjqZRO!2#j6~fJSi)NrQb)c-`w!@@H#%W%!66B1(@ACqB;7)#5qDTXr?J=K!p~uH'
        b'^nAe%-R9)dtAxT-dT0`UXaZZ-C%q9NYoyPcWQy9-2%?c*e1k$00BA4ET5l=JONDcDnzf>IjREMEi14<Sl`bNY*Iup_)*YpbR-m`F'
        b'=*|8OOY+bP{7<YY3T^iz<9lmqNDOF5NH^%4^q#4R$(v$hV}MLPUVr_wzFyFI$MJv(z8hp`CNeQdKT8<$Z447C&SW71C*vz6O<Q1k'
        b'pU+v~0i=XFvd==54$b)|R%|Hc){|)hC&kFrXxO)MZrxRpRLXt9DEg88VO2xh92Si6MGfdxm!ci2C<I*bo6=5VIG$5J6~8VWU0dp='
        b'afcsn^TQ?~{~9h&9ORLAO)FNEu3A~z<ml$jmW_gRuzS!Z`xI-IgwUwRdB{pw*7pr)B~Rj{#ACoozoD<$xp>iNkIGpZ9!uX%_6?6%'
        b'0%mfD*#146#K*#uf1982JtIfx!w3|86Sw#V<3IPd?WXs^aLv+&mZ@N7@+R1hPd`d&v2cmW_-x+(M_+^<wi!dPZ1XTtq22p1yXcmJ'
        b'aUo049^5g~XStObd<lhgN&pKE?JVH58dIrp<sFvmzu7$fKj$HXW^<X;c$^FdqBoz|l#UPZ$O5uyy%jQgzcbY@aT~tfxbi=<`L=WL'
        b'-bCpjkCFWqU7D6wN>+eMGYeIv=BFsMYJulluN`LM@dkKCV*q3hk5Ju>%_SxIL0QcEJI0QHIz^Zcv+m&;=c~I$#3r6#46VY4fgnN3'
        b'`LVDhk~1F!wz*`Wg7uvpHVKg*C3V|Cn|#0ZF_0%=_z;d^&yu91{$0+;Ez`5Z#({rUjG#Aqq5l#LDG`3n=^E7DQfM)11hI}5l72}9'
        b'S0^5xA()L@$V2FFZoL8XABf2oJ!Zefw&L>p(<UBaJgUwQCQa)QFNM&JF-hOErX+0W0Xuh2A$plQI$_JIrX4U-rN%_XAb#g5Rf81R'
        b'!@3f*(g{XTf`+e4<fqr~042qy#F&~A?_wtyT#)U$!<%c_m;T-~jfI~;BX*#l7Lb0VZ-;>MO<r8WNzs-3y8A2_QPwLbOAyo!WCbx>'
        b'QI2Ti7LYT{)*aES)luenGr&=al_X(0OD($)f}n~8Fdmz3aUTSRclL5?t*T@J)Wqj%(v|!yucLcPd$PBHxpgC4rq}N1saHqkH|8T='
        b'6#~!^e%kpvIYZR4OL1J100n2{I5|n+Sq!q{y2P7q_-3zn2{}nHoAAz~1dfjoEn%{@lq#3ws0pny=1J6qy=G&y**M#X$i3Wht}0nM'
        b'o3QXv!km101jimb2Pf?R!ZCb0*XCI`fZbez7Y>7YGBJ7KX2s$ihKC)*0L~=7#Kk|*(Kw#3A%-;gUG36vdhOdPVkjNY_xsp}V|hnd'
        b'#k?J{GL>d_2{JtAiMu((&{{mdgs5AD=bMg4$mF*BHU)u#t4^^P6jEAQg>Z*l^AjUL5_pI+gBABm$N+>7ff>F|@HSC{aS2Mp+eKbn'
        b'H3)evp#-BddlO30aw!@jyog)z*J#4I65$$4cJ^$Ma21Z(>)95ZpU@^<w{Ug-ry<s<l4IBM>e%%z(g(!pmnB@hf*W;0z#|#7uf&A3'
        b'()>W8?i7Y4h8}t=Ur7v|L5Pz+b}0`3F!w2?_|RLNN&5k%!Npq3W9yz6PoRx9f@l9T03MLY&pqts<sD>)rdZv=hZ<ZEzH#&2ElcwQ'
        b'h@^d({7Ys2<Hs~IUVgxv8UiC<L9wkg*wAV$eD_B3wao$9`CDGK$#|9swZ&4JuOgCO#@+@Rzli1g5lLlOIE`Xmd47ZG+Czpeu{IZ9'
        b'S;abVA-W04!@XoA!yb`Q*vNY4D;jk2#X~h{QHG-%o`VZf9M=G${40TNh=s~p^rF0YtVJP`_utS+@bECA&dF*eqV4z6p5Z%7Wq@v)'
        b'j&Dqq79~<8$3O4cgif@2(br0NB@)62DVwO*Q?s%*KfXx)r;?^b=GEEJpQFLo_X3XgJT@s0o!P<3KGL`Tps<9GP4KG{At8JnQFnw*'
        b'@Hk(cccth~x41#yR*d4PLHq7SaTiZ{$l18QwHQT?liwGU^+#6|LkC%~b&mdnsC$hCyV`AGdrFLxBHsH;2w^j8TE}}ha#de~w1E;5'
        b'&)@7fMiS?Xw%jO}T`NC-QGNNMX#-Y5VpYgAs~SG~)ThPTlCH!O5mpbNN7y7I>-Hs1Eh2<3!vo*J7og{Ac;=BIA?5F%wuPLAI(m9a'
        b'K}=eoE(tM%!3bJTeLOMrFLtPi4bNFm-dX2I2w!3q>r3SHXG{vBh(<!t5}rm)(rVu^nGi{QOi6<t?`Jtjt?%vTc{Z`aOcry<_#Oo&'
        b'@4q-E!B8wR#Zx8n$xoO#1OvsV1wIN7Ack}-^o?O>TB0;*I}0iZsidCaQ?xpbmQrC9oh~F-e(2)ppO?la2~e;?TulD3?j#{hW>aZk'
        b'T~976&l(+&tao+u?0;Z&!T+RjK8&RVTB;lSAK>Bq{Y27BEa_MlKnR~=g-z%(H7?dz#Mx<EHorv(pJZ=rlBH>l+3VB^&lqid|F&ZL'
        b'@7UJj7bHz>^8OFexEP9qj)&2(KrFB4g|8-rku2b^JA&?Ock}WWJmGP$@>fo|U3{e3^OU(PDY38j@^82(hY((z0WzXjzEblZMJf1o'
        b'X8{dQ7hA_kAQjG6c#5O5x7^UlqSvXj=v3M(Gz?!C{X%A-gj0_aG;V76?j?mA7r^iy;3?O!Ndq&OjqvwqS$UK&BK7BQNRGWdgDE~M'
        b'mebvebHz3SvmE9#7txxguxCc`NwM7aH|8VsnsjUisb}`*SXGoj{yY*PSJ0#iii3)eEjuwOJTgNP>Qlva59Vwo#rp`Lt{=<$Ep!Fv'
        b'XGt@+_suwqX>O82`TkMNr6~ry|CF)xdc~@NV#Vp=SRNS+bGM3zimEhtNSESd@r^E->M$1FMcK3%3L$*A;+~?n7#&MA#foXmQnZnE'
        b'ayvTYV<}}ii>a<$k^ntox%ucj|A^Yxf}&=(WMD82BYpO-#fw&;t?39<py>p9M<E!((Cex<ijhBxxw+Kd&L+*wo~2VCET*lzSpM}G'
        b'#pdm<XSet6FShP4j>M<=(HAK4cTC`RZc7XWf7=y}PNktW@kUgpgV)p!sxH%rs2a(86tBg80c(<U#Lv<P-p7De9q~-ki<~Xjpz_)R'
        b'!~~xt2Lw!YF}Go2vf_sd&kE297v{%5pgjj-fY0nK=E@*V9-TQrdo;e?1e1o=6T*XKqc0V^UMjY}RP3<aXVU)o%d=z11OWRw8fjhj'
        b'yR5tmH${mKC6n`7(s^WL8`2*&YVJ(@&ucYMrW<YDuaz|Qo1-*Gu<K?fqnO+I%d7SJjdX<a!Sn)qwR&bm()V;nDA@N*nm3QVVn%m)'
        b'I`(;a%ycK-DdS-Cu%w&p&-i%0W97ksiMXkcjB5kc_-6!uiF4k!th^Ai2@i?E7?qI=IedSS7tvMu4GX<+C@b7QuxT(nR8Cuo{1|ac'
        b'V-kj?WFb1F6rxkQDOKF@8Sgnoj|aI%Ys73;p4Z&AMe&dk^x%)&Y0R&4+~NtGTkaIvJ#3An>2ik(3>lqdx?99KvT`Ue=_vJ%pyxej'
        b'x3K4gG4Bg@xX>(!#pBHlf({iFLcsyNaeS1Yqphm?;DFh-m(3)c%jFK{@0fX2GTWy>wsH2*Imj|T2>2Dw$R*HBW$6rk1Y6cFpsi>j'
        b'#c*qAnq_`0;?A(<9Ko0$ia4f$!o@RN+xeh|{=h=1tuwkPHZ9S)E@p@fW||Niaj_bq?Xi9vhzJ5L=ymf*I#NdK31t^LB63X(8bJrZ'
        b'U9ld@{Dj!O^9gys2&CKv_Uz*zB!4?VfYhI2-C=yW0rU)j;Q1Qf1l${ZQ=&H^_r`;_uUG(N|04$o#XqqB4|EisG!HrftOe$IgjVM>'
        b'^3<7*u;E~vC80BrT+X;qi#nC^YY*qzJG*Z3ZqewwMWhc|Rn{nP`7ooWP1fED^6~7vkkjXfkt*@Qyp~J<A7O7F5LJ~vj^BIdmEmGD'
        b'1CG48-MI)1sO>OVyp$WDB5LgyFcA=BW?+T^MUiaPmUib31v5yyfR#YD-8)7iNitN58oL82q2UJZZkZn~vZXY8AyZQ`@AsT@XHa)P'
        b'-{0?_nS0)z^M20rJm+~qvOEEOUHA2N!^3lL0M}dXxwZ~|ZX-M3Ujh7C2AP;ypb>04EZLrg!t)gV;3F_YI|Sd>#?4*V+<e8C(&avl'
        b'#HN<_3gP82VB^}Ved#ttw`p6dA!<WI##ja|(JxjeB&|ylBb3i9NqD}RoSC}_k~Inc2GI~BPsxQ3c|Y(8CF_&KkD&;|DcBiXR8C#B'
        b'(G-&4td4nzknVtpicM7eezg@ss}P~!Ch<Cd_%RU~XjmmStWuDXy>C#R8a|;2)G>pMBv+6Mp#jms{6`^p!W-*A<QjkEq>3k(tQOCN'
        b'QX1;jA~{Hd@<~c~nWd=7x+L*z)GU~82KRWP66AQ;S6Vt5#4r6fk*Px>Bj)v2eexnuhQ;PE<~(TBFR(5lG98%JLP(vMHQF}yq$=mJ'
        b'>ePlYr^^1EeJE7q4ka9+VsE$CSoRvrUa`Max+j@nUn))AGPXt4+`IYdr+V3ttuodHdGy{b_5;g^Of#1Ebtr(8nlzTEN_{XlSX2`%'
        b'F3ihaDI#ZXc?c&Zxr-F2MUj$h0o^o9lQt8XRaop5LYj&t%&X3csU}0{qrCZF^7AYXJq7-WgZ#`GsSDrYggW{)N0;_)Q9b<>lyQia'
        b'*=F_axA*o@WYADBoS=)b0JG`|ik9#-Ls|ZOZLtp4-Vjg<1tDV7Hmja~k(pK9TLTgsx3p_v1{o;bTz#cASW&&tTissTT)i1|x_T<)'
        b'bmElDdtBvS834N3eGc?;cpH|t|5t6QJ?+755PNohRQpr&7QKB79O7*snXYZ5LCv%(9+DSZX|ldt2Bn)S=!nIJ_d;WyCF<Yj6TaD)'
        b'er+S<<*yV-*|?SP)I+O>Osck0cP*w(mHx#<)(x+N^FI>Q@s;;_`p|E&%fH1}w0ozndPknR{99t^w<54L8dCnJ{uLf015TY%f+M!|'
        b'6ymGIVfHQd)}`32b&_Uhx??FGlS<UTz&AHvZCy%aw(?lc-#7MxNi!5e8a-cR3R-7e1)EVIs&D0U5fGas;TUXmzNA7_5Io$(o4gxI'
        b'Ne$W<j##PTm@+9p-*7Cyw@zhuKw7d@M<i9KS`KaW9E9cCbzqGuCNJDZ6~Up4lG$QODDLQra!3_J8qsK$Lqjy|nr&bqhuV;-0E=Ki'
        b'0_O9=?TA(8;ZW;St(lv7X7|S47gZgtjqMJN7#%Todl_Vo{9&EIC~^fL8LF0D8=HMHRQ2EU9p4Vk0K;W}S2Z+)00V`Ms=OaSbJe}?'
        b'QbRLD_EFq>gc^a%;Skx7GB*4iPX<WAdDr-Ss~ns4RoF8D)<@+IIe~#KvW0SL1;GVqm#apO+qXc~L#VS4&c>%U)}C>o!>=t=;A`EH'
        b'`P{IPoYyC$MSQ+~qgObnAmd>qklfZR9G&n`>(>pj3}_K-j}C^D2g53%T&EC~45Q>j`;)v!U<G|P$T$C;E39uczxRl$w;zuGskzwD'
        b'C_Zrx7WgDk@Iz>;z2TQJZO?C6jpoJHdF2lOo#?ff9oUNGf7~KTt4PeUb9xV^+q+fG@zm7Is;Ms3;r7Pvv2N8wyQ;gLdvs$*2VEe}'
        b'TOk<|iCUIy^s*tnr&S&2PAVoka4v0Q;HdYFI@V1!cT+7Yc=TTg0-p)<Hcki+hCzmZpwW2JF`^{Z&|0g5^Ud0mnV<44F&p~=umfv|'
        b';WK>18}4P8=HY8CaT|NPR2|*0m|`$)BYB^<T?uN3eNlMzAuUlGz21<(QT7t<eYI|)otj9*sdh^HLnX*@TA^>J2FZ;eVoVr(MeA8~'
        b'QEd~dH*h{7L@18hwX2oG+$WUm*p;z%@53q0J9am>YMa?Bfk%3~9gdMl&vaw$Du5d|cTkN@Xk?`x{tmC@{dB#)Y^q5$wL^8nnc5CA'
        b'j=`If`C&tL_LUB&J5&r%zkE?^mSUMaH=kgiI}bVDVPuf~lO1FB&FnivqsiH>x~Aj^NN=`$x&dr1YvdB{s|{mE@J3g+Gh0{=a>sjF'
        b'z0hU=5|j0u+t4eFu6);$)=yyX@;||X)38x4TUcSAKwX}k@ePfxLdXKkm$PhHb~lyNQ)zfFAAEo<ii)SEpyPl!zQOK04u+@D8h>|#'
        b'd(V__k;}b_Di+*8LCuNO$)G;gE{Gqe$UDF1@8~S)o6Gb`>AfyhOfWG#2TM4(A=TMb0q+C(OHU#JP<hM24Fbn1MUKRmTihG$^$)_N'
        b'Wvo-B7gohG6n3zbAiQX(KxLOT)cxc;Ljjx@?}n4C+bQ}<h-ZEA1{-Ezp$ux9E-3(}rRX4QDdEMt+LVY3WhyKEuprNr`@@DlH`aOv'
        b'0S@aGQo;-@+;9DbNr6H|T*C(6B9aUBbm@{5LOrOQ<2B4DdKor6&ils4j>gBSYPn*w20xUraRcH`Cd&opTZ%B$&8;(AkKb-?-h3_Y'
        b'KB0Z((|tv9K9&s-wTEN=dHIIH@(th|?PF)S*%*sTB;e>w=>}5KFDFBL8|%PoYvn|-ZORytYES5lwut6LZ!1UWJL;f+Ix?W%C&$R-'
        b'ZGft3PMuFK-pvu;5Lv<2Ih3Fnc#}UH9tnm0{!b+oJX^kDul$?%+M5uYC*J`0@O3^foJSd!!VKvd8}^DdXMQ1HTNa)bl`L8opZ=Q-'
        b'Jw%o`MVxsVjz`YJ8+4L9vxH0C5dD$#afMZ(8c*IZm<$Gg4wt-vxe2jVYKZD%dHAToN!e6t^zgW0!=N5yiGx<HA@8D7>WBv<MUSXq'
        b'K~P&phqK{rY4mPsoMiTt<t6DtMPA1*j1+P%1)ZkAo<JsQ!!#|kkZ_2CXo9pmRZyj1<R`E%347cQCIaR$h-OffG3hW~d)fa!3MiJD'
        b'8+;=70Pp-fc*DqyrpE-@k2|>T9L~CxEbUG0JB~9!Fk@c$Z6_YDLq4Mc{VLng<N)OBaz?g6ph-oD7Rk=u44<M-iuWC3@D1n~cgjz('
        b'xZM#w+O^BY{8HtsQ)ZKlwd=v!uruk9_rqL=Dey~}!>d&-y%k6S;4wwBfOp85AF5hk!%$@HH~vVixvJ$<6|9FK@An<X1PZo%Sw;S~'
        b'*{N)qtnx?d0+=tV?6i_`SJ-Ka`5Y$11t5s54<5?JJ!12P1JIpK@5iWaC2639lPUl$Z|+nTxG~+F-G{-;TRyBpxjlcc8oywJe(^@D'
        b'dhe9zmvhIfge&k6tfpTvCLD+gRBHY2y*|nVor{A*RnYhKcK_ih9F~Wx&du-<D00uCD(+y_Gyu7;xSV;XihHNZUyD=W`J0Wb^~=_B'
        b'y;YtEY<{6z6vgbT>f8Sr0^tWOREFF9VeYjm&udlFqPn}Q{NRKN*eV$N>OHXm++((Z`|ieZ0=S25zQ?f&umCHV7Z5w+e)55HGY0M('
        b'Vr4My&oJ&=;v7NVN7e#D5ymy5eD{&FzXfpvK``pMsypu*<ZsW-fVs&CnDR%I`2iuy2jFQG_nW)3J>`c90s>g38b-C4s<@4)rvZYb'
        b'yepu^T*ZA}es9zhRooYq_eOcwbIbpu;F0y*Tz`}>4*s`|nj!HJd#jH{ikt)Gur0Gwh{&b^Ks0xLz*iCT6{Cftt0L<R)}+}}t<ngn'
        b'XqQSgC-2ZVZ{D>m4V{KfBb~9>Uh%#&uv~N;mLU}z*o#RaQthKv!{A^Ay@xh{{tC`B+#r=iij&^%fu1w~DJ}h)pRa)am7(v$IZ4kD'
        b'<`HErL0JJ>W4C&#Rr=9cnn|&H4nS>j<1jUVcXve(@p*+}J#|&@e2Q}F^-g`DR-c>>{wocwBFGoEyWsn~dj|`emdyRC>a0bx2Lq*{'
        b'c?MbZ{g`1+5~-*xHJ2q#+hwRCYGRUf#4_#EbX+>k?uw6zOW2xD5{BW(IGmPBvhdhBVLEB-K|)GlbWD;n-A;R-uBovmkwj)BY~2tG'
        b'U0BGX`ypHArX)+-1SJum4f{|mD>#h`$*U1_X4}%#be)K~x!&{h`bNk0Ee%KH%#HN`^>0X(RnvNky7CRt`6j<NXPfHm(YAzb0lMH7'
        b'?eSZ5czZ$w9fxmEl%9nK(=V<ElcB|F7HhU&A;Z7{`#hn`u{*o~(N5Eq?s~3E1-;pJ^WQ2ojbbwB@@rV^LS@g4$$fmAidyWAZ*NzD'
        b'oB7ONyCfrl04?v<@0IN88e?BLTR1l4of<9ek$<x3qUi=>A+hVs1=HzGE6xpn$JbuY{9L%($Pkj$AFcCxHy0CmXQkB9y1ZJcQ{7Tl'
        b'PIE*<N<qKmTk$!vM>P2f9F7h#vN$B}5m_#R@U0GHXj0KR0SywJaEK!EXYLwtM<qcOj)`;PdF0`@8oN7p^JhCUqLMO>QW>R5hNz^Z'
        b'cL?np>!BPeM}Rwaz9Li5^KrAAnJKGJf$}gGZIh8uiPR=*QcU|d7A}L)%j2)EAAEIv<R$La^~^)?R<(d^9pk&!4|c4d2R-Zhaj&<i'
        b'JT*SPWBuUH^?htCw_`mM53}zI29T|?rtb0P^@Gjp=N*AJ1-#7nLVFtw4|k9tlWW3qIYM((+}XmrO<3nuo~@*EIb72%B4wlR4M5@E'
        b'8+@^-UI8*w*;gD|td+&Hch)uMd$Cn2{i;%Efqe2${40vl!%!xq^BP}!6$<6ChpFsiRFAY>Ww{Jyvykoyu>6_NPW1X^Ssw`?<*{)p'
        b'reZxrKXf{x_Bz-n_CHH}e7Xx6rwt=?zq*UC)De4g1sUt%b)MmMCkbX0A_)$TkX1%9@2x`soJ4C6kM5>sL2F3vU@;#ou791UAC~*;'
        b'UFF`HF6YL4<*5HG*S*fu4a@byatonWg{(4OyKp@jsv{uQ?c}<M$jeD|I6SVpwaM$_6DJZ?G>0LzC1GB*+u^Hm+ZoEK)Vi!xyVCAL'
        b'r`ws#9}yqDWu2!5*0B@TVSqL06JpmR^^i?)y)fJT4JDVMcJ_#bmeMwiv010}Lm;d_tn>T<!g}^DSRn$ewFuVMX;`lRg0<>iSnJk#'
        b')<IaC?t+C2uvQ>g7C)@oL({O7K3Ey|!pdLg$%nAk-UaKsbqH26f|WZBYukUp`t?1qm`~S5-f+r$2#DuGHj<NzjnlvZeVGgzJ4y9%'
        b'7?Ziq$C)3ThsOQ`uTwb~Z}m=({Rf#>(AXQ+c?_^!$#=DDL}-^9wQJt=BH^%m1`Oa=0r&Rt{&k-FA*|?WSosO>2(WkyRJqD(Xr&p+'
        b'IyZvUCimk(DB$klef$JDbKi8GZ}RsH2B`BJ%RO}x>pTRkQ+`+b+k`sL!<@{mN<S<_$K2EYPws{FeWmC7N&xF><sDeh39vpyur5x+'
        b'+W*J@Y}fF;u+CO`&O%t{E0LxX`-YxP6Xz`uUn@<^sa{79MfOOT!w6_4?5tDXy6=xpxn4gfUWXKJn-f*genB##e$*iIo0e%UXQ&6_'
        b'qg}Y6O3zRwAQqUB=|(4{=dbJAkDQ=$uuwwoI%lFaS!TZ^vOh0&CH9D!4j4a@*d-buI=6|0Rtxantn|Ez;JsbxKPZC06{SsI2ld%%'
        b'MZ(LFkau^bXE*HQ-pV^?O47Q>n@)M#^vc{<7aI@pJ6D`gGQnwqBUhkzDii80dRl3Bp!Hag`4b--5Ai-%%JZW7D?IlM%2)xABd*rM'
        b'PG_vBpOztwMEk%A4pBG<ZPzg(t(j^OG+rRqs8hDAw}4Ru@pj51z2TR!d#cj&6zb#eVZ))@9@zE=!GOt14beS(k9byTqUAWR6|W<g'
        b'>4=P@kxpV_v8p*rxjbthA`3!%ODF^#aF*A3q~nKyYg-CF-~@)$zNHt?x{&&7!dzt$xip@=fYJodOqi-PO;zd_D2*1SF_FsqG593F'
        b'Kn5gCUZqcK>OqWoymF#c)o8Uz&q~L?tQ`EZlKZN%k6Xdi*r2S>Zff#nUb7tQ5k>zV-%9t0WM2`(bD>ZPx3JQ)u=1pcSp<P?rOC%w'
        b'R{VYgQ6Gct>SjKy?0YZLDW5n3*4$wy;^X-kb)mDqA~K_~rc{7Z9^$tedPJI^<edZj)(r6Vl|1@5-=7O=JH>AWf0}Z6^l84ff75%F'
        b'_Il-(Hua|aDqH>mr_3o6#Cu#&g4QYBbfmJ{sobQtR0}ArG$Qd4O?faeJjBDn>ulwv|A1qsx%m^*RoRN#)(+ZMd!$2XU2nUx{$n0g'
        b'ypxxn;Vp-FDYBC{d6X9n=5_v)&pgLNy~Im`pIWdIHGSfggoKwWBjs@Sy6`w{h6&F#iJ5a{P-O5=l}^K*4Pk(fz8}E^PfMkn7AXg*'
        b'&fgFYPBL2P%xMY*AM>a6)VVJ!JYQCTHUCY;UHkghv)2|ql=Cz^9l%aK3PCZSR<!)F5}p-C#BKs-g#?@xdjHXLxXibmeF~Kj_J<Xo'
        b'4<YP-RrvSQ0%o)V9XV}?(Gnmljfo`uL?x-S*C`SCxoayK?1LQOySvw41_Ws4RlfEMy>LPW)K9PfcPc#ZRKWFr1Xh%>pJx~A)4=KU'
        b'gy`BL13-^rq9S7w>6qZa&Obw&JB>VSr{y_l(QgNo@9lh+7wmv_KF>p4^$dXL`PMl1mkQ5cU>{zqxO0Xss6=PzAJDk8Rrv4Uxc|C;'
        b'pDMfO4BcMg*$!c~+yzT3z*>i3J?Dp2`^kUZndW<7jnS%9Iw2CB-%&cEX^0H!G9!t%4x6Cg59+(m5~G$`X}LC}vI{v<<dl^$hO4B)'
        b'nlZ&F;bzj3l~lI_(nOGtL&CO5m@HIN=!!&$4<&PqtkTC$(h=4Wh!;6%gS`&Xv1S9v|8SY_ZideYw4wI89@(mywx>JhQ0blamZ^#f'
        b'r^@cKJ9OBt&@Nl;&&&qcRKY@i^mRc7^S~maUXSHn4&3y01<i?^GL2lJ{jvfa{}9ck%aAIh=ie1=p<QrWrMes=A!E=8Q}1Hsrq3!6'
        b'm%+POReeO6=3}-(Wp26kp|z$pWkx}z8%FiTFQ`45c0@^r2>JRd7o@hg9uI*W-ws5v){4M+mz}*J`wj)49FV@s(nI*fuPQL+m(po@'
        b'0TWej6tvUj(A7P<({2d+H_r5oC~tQ#HZu)d%q1MGNYkdr<)pgFh}cx3`XF^ud``yn!zFQ2VLroiy%nUIOe{ZKmC#plQf3S85+z4f'
        b's8X~aB<#hj@RW2q2Fn{F6JD)wM`5EUj&GXWh>vV~H$3_&e6Pq5g*kKd{ZH8wRgJsJUnQmD<cyQz>W``3zuK8sVIAxV$^a_aS&?)&'
        b'K$pJ4THg95&Ef_YH?>w|oaL7ufKQRu;MJtGM@sFk1K>Zw)9Wk1!Voh<u)CY;Dn>SKm2H*9sArV764Ep%v^M-GMzfHoZ;oA1J3=*w'
        b'fHPF!MLEhB^oWN{GNum}9@*5VmFmBMR{lsu^ylEjgg$(+gt9WL8oEneD1!zO|IRZu*wzF~g+A3We1f+|WhInWn4_>fDL!e$^Oj@u'
        b'ez0C9Ex5ZB1AT@=dz1tH_HyZ<>+Ehjseyf$l0k<LFeYJaL0!<76se9${8emlC`psSF-t?n^C|}OD!9CgKJExJ2Jt_A6ja@s{D2pr'
        b'vS2iqs{mm3H2`(#G}OlgsF@xfBk6iCKVO>pH{r~<wzz_nkQxd(9LYN-F(sj;EY(~WYZEJwB~fN091W+mcDO&ZO+N94YNAecxI5L^'
        b'+YR3*x}E54piQ2Z7Gi8yrlISs)dsFc=GPU17WvvzpQ_Yd`s;u;mQYWiO5c%OTa<4KgY{-fHE)a4XQFz=Ob#rkllF+6>NWyYmFo0u'
        b'Ac1&Dm{F#`!v~~wSVDzW@5cz!|Cc&P&EOnE*j5dV<;~*3$mP-^n>vfOti#CQ=VjS-b=MZ-3uOTF)9W|q{dmhT%-66%NlC*AKiF!b'
        b'u(J(=KikOdWH@uvh795u0IhoB=77v{mgu9!#*e6zk{)sA2T&ES@J8C(l;sB=x)z81^%=TK+no2d^je)Q=bR0WvqaM-(SBk>yl!SD'
        b'8fOW)<o|P=dqmlHq3+2!Z<S{I#$3ew!zPS4QTo5(tDp^1$^y0F@*a{OsDrwhn~uO{<jXV?S<XQlI#I8f;i$_dcBr-zI(2IMgae$X'
        b';P^tXK#dKk4Yf7k${Jg&qWlw%8l#ifzU{M_fr82Dyct~YzNlp84b(aba|YHhUwYTvn6OQIY@}v&5@BXBa@MsvoRn2tDcI7NL^Ui<'
        b'mG8JE)i&FZIe~pT<Xyd!|3&((^qlM@K;0^Eu-tY+@Gxnzjfc?h>bnWyB^gSmnw&+7?Mrv0**7QCd2RQBQ5b#%vt?w^7+4C|G70-u'
        b'iVVFLjgxZw7D`qQjeBz=<(`r9lVaxYka1D_6T3$baJsw`fll+*TwRR|2S{(6Dtaj(hiy9f*`dK2utuPI#U|Jwrqs4q?f~ngQa(UT'
        b'9wJWTP)UqbbWZW`&+;jMQVKt!-{+x=Sn$!xYu_xNctTZ3=M$#ow%R@_T3OzzHoa87sSt`9=%m%ch(fs&IvO)&*!oz)NGnZkW`IT;'
        b'g*_pOUdC&mu#Kqt2#gF$Jp%R<TRtsahQR?D_Ss;$R=3d1;<+p)oC4oWY9G35q$Qny;(w8RD>)}UDX#sw0FLxR-$+ZM9sE6e%!K8s'
        b'#n%@7CMOy$D|a-eQHV%2w5}hATXG_ul73t#cZQx6-@Th1@bMHZ>#?x~lRJ?*(_MQuGK-wsppJ>{huE>_FQqY#aMBr@oZRQeVhs0P'
        b'%TSUl0NyY!@ET2cUN+AUoITaY+GBFBdSs;sa=-U9m&TYc(nB{Q<zyh$Uk9#v^0Y^9ZczU-Hd*WWLupLw2Y_Nf(0YvQ_x!Q6K|SE9'
        b'FQtdBkaDVj2S8~fLp_T?<~^~=a(ZaW!D02^@{u}FcY}HdJ@l>PH7xTYA9=xZ3KVt3CjU0F&9kAj0bDfa_}Ju_NShF<|Ac=mu%V9t'
        b'm~`Y;&^!<|{7>Fv12tW!|2H2w;<;1~<38j)m1fY>`jb2v2u*3uOD4C&^2Y%*9l63fL<|q}<lJlE|0q8%bY37x%mk=BXxyif0RwXC'
        b'P+k3B`FZ(|!362Myr<3zsvSPW&$9{DN)Pg$nsUd`CuD&A(2n}Id}AEvaAP~wRBXyqk@A?D&})vlj_Kjeg2O8Z!^<o(!<FMe!^@<W'
        b'UNe8sylKw7$&+s}38hKu&tnsV$sJ&flGGnDv8AzzV~nA+{xVPggZZZ^Nj=2;x-`k~E=Z5*JHUKvqKCdGMO57m>DN3Kc^!6Ni^V3V'
        b'M3ypI0PKa>L{;P>QkSG|d`upj_#7DN;m`QUIwqnt2@Nl3Mp7SqyJuc0r-vppzv1U4H>e+vO^%osHct*MME{eIl*b+-q^I~tvd9d*'
        b'qpto#e%{K*<golno_WLy%b(!ql|oP;ZiHv%0#KiT*&=m%*N)-$_(&(|fJ)<Vj4s3`&yH+oQp<Pt%_Z9zrhKP5DstOS^{-+K5loLY'
        b'Q-aMaU}`~ZP;APKc_~bnH8zD{wv@v$n^(bX1}Q&EuigXeNgu50dtkNuV6D3Y>jebM>W5W&7p!?t#=fN-H<u5Z%Q<s-WCU{pA?FXk'
        b'BR0LHycXH4{G$mXC`IM*D|01S-iyd7<7LR)u_>N`LWRe9_H{(o$a;v$t1w}!qDq16kAKS7UT3@X)xz77G(IZ#7@nJfF&eXAFQeRa'
        b'=WR!5%cJFki^{o2%OgKv_Mo-|qP9Fzj?l6qm>-N{ywf1Z0u#YCYskX#>Y)1KMWIE-phXt1P_0p@RsvFy`KNr)ETroAPoC{WEtWD@'
        b'OhQYRnEbTFyx+$jnK3@Qe2^~ZW|uS1p;mkilXJq$(H-|NDnmqn1%YNM7Ahb!-0~ry#Sqdhn14cEswsh-7BOc`!sRvBH2sdt{0n|-'
        b'10YO-i9v%bE6)&V&n`}vmS=@PTNpn9L?(m9Et7o4A}w=VsFw*h`R$q=a1iwmKuSV7A7cg)ysK6p1))M?^`n)0uncmiLXhN>-kym2'
        b'blPlsA%^?L3S#srf&c=HH0bm#7a;Eu8COfjeJ}k&pyj;v?u<Saoau6Bt^XOb*z6Z>&@*km9$Yl~sENDIYH)X4a|B<DQgXK}o?8}h'
        b'V-i-xQIUd7aE&n6EfX)OI-G5C?geXYzul$W)28MoES}d)_dIe650Fh($bS05=zos;Ch=OvJLFt|VExZ+sLk19Jtu0U`)P=CF&7aB'
        b'kf@*J4`eix5pd`~xt-8y9fLGyzX9bLhk1}4!a*$h-~1_BJVX=yM3;JOTpWFc-^=7F9!OT32~3~1IYvX&zk}r-y|qw!U<tvdLWEGW'
        b'a;1SFNm&Y)O9VMNGWZpleMepPlXcbGsJvOZ%by}$TlNyeOK@kd%i|z)u9neZr^o)#4$Vr;pbf|?&1SOT@NIg=3RaAaX@_Ij!dOX2'
        b'ryAn)tdCaHCuhjMAci}z_RpCdID&1TCp>Ot-YNwI22@*&(|a~s?PzPbEA&E)@bWwz^w{7W?@fn{i*(<^un_Q+TJJ4)4;W98^*>{d'
        b'nWkZb_JpGOmoXKv?c5XAw$D=(dBZWS1a-kYQq%tV@$vH}lDW?$n3$3=MwBnhx_$G+7S+?xR&2k_2_-KNCBW~5@ij)fO*M8zX<Ubd'
        b'6Je|^0g$pV0GU`e8TO7UC)HZ}Om?2KSCAEg@%b_`#&~zI_9H<Z%b%KgZ|VVmY9A4YVtS3@F{^59mC|TIHOtyQ9~r+exGy62sBU7F'
        b'YHMp@A(Bn>L|Ut>U#Q-q>a{9;5|ondPk<c0^hlXMwuXpDF^>IztF9KaTU7QtB~XIbEAFjT4ekHTJFKi0<fSCK7L>#U8L4V<?-u;7'
        b'G8soH4Sk=}W2!B+Cl2Y`9TO8`W4oLE1CEM(t}ktVF}*p_JMpEm`a7^duRw{h#gO53QKE0BmUkl|H0BL71rrwLRtd!Hnb}jh>@6n)'
        b'MSExJpQ~Fa&&=YHd=prLOn51G+F}<D0JH?qx>RyW#_825L~>)0-<XmEkCYr%IA4SScf#@?rSB<s)bgJ(^GwsQ6P`B?TackYiRro-'
        b'bVksiO98`#x)Z0!{D6mh^CW+Y&<v>+?Vk^sf<75!YK;CBceDiUn7NzBz=A`fcEW<&3k55?w0-+Au)^(?Xoz8yP0Mv!?yNSj^jNFX'
        b'z6#IIyR&>|O|P|CC^)^=gy8gA^Q9iRH?`iMIx>z{p4a<tOp}JK=LVgY^*6o8lty7K2vwaPgn8jC=Bs+ERO5Eb*uRuULDo`;MX=0-'
        b'0NrR5d#x%KEaSVIV0z!^QCa*^ZXy&_%o@dMR=jsQuS}!(6eXCxfFj%la9!o&VA+9_JUekHzXnVI_|GM%<?Z@aj;vPWDmNhfvR9>N'
        b'Cwiw6Ra2{Qu<G;=qIVL+bdu$)vgj8>JAwk^DMgl9f^6NzF~de4kl!iH@LE2XBMO+|BHs7roaVifJ$8j8t}RcBjeLmI=*^HujeTh@'
        b'v%s>w1F@t9cC;J-YPLT()uw7}_qMCvkCQQ}mj9$B@4W3^F8kl#b^-qI3v7$#uq0uw1sVX_O)(F_Wy4JRi?qa8z#T(5y@=nSlXoHG'
        b'sRY6ad@Oc?`IV(5vjp)T((iCT(;2#Cn)`{`Gd|NYIMc$-v^=toF+*es@(yWYn8pr7L4$--4nPc<?z2Faqt)(+LB{<;r3rx+aC<TD'
        b'LTITp!ZCv2w@uonNtTYez@V6dOQ8BxqS2ykQNxzxKiNDzyU-HjvQnhbno%lex?$Oc0J&<~&D>l&-9qLk_+5Vs4v5cY?KQgQTGYm='
        b'3{~ploQq{(4J==kEXe?EdP|(}Wf|n=8km<#{6+*X!17s={1BaZY>BFHG0YE5Q|iPyO(od^F)C&nO9TxTQPWZ8460o$@F$p$VMuz5'
        b'hm34!dzHbUJ*Za{X>E1aqVVSxb{A#0Z_aBIU!yapT2<V!GJU%pEQ#h0dsjd!N9^lBF8)GXIj;21iU{U!u!ZruF7@g3k(_PN$*$OV'
        b'fa>0DS%JNxn2&^dTJO-lq>P+dB}=owx{76B&&w=C=96f8HevZsnD&+B9=pBz0Fk)?%jqf`Gpj0BbxEdbRF*8h#a))#0EfSzO`?gD'
        b'Gq0BEx7aIf%>VHXjg;YF*K*p*;MMn3mu!GIDVprVyFitlZ{a%G*2PYMd>|z2ek?o<i{|t`Zv6dY@v3eE890%sN=>d_Q}>Ld<&R}Z'
        b'U{=2c2QysllbLOuBguKT%y9g6(mUanPx!$n$|50mY9+*Y_e%1*uhm{2egwl3PL?FK<F5pE(}+1PNRqa#MJyYAiG;n2XCrTJhBjy7'
        b'1XNL51qNG1B`TYDATAG#)#1tq@jLmqE@08i3bN)KCw~Rd`_-*GkmxV94R2XncBi@WeDNzHWS%d(b%(J))%phCyhWMqGu5{>q*zp)'
        b'yW<%NDw|aXjx^;K++Q>;s_t>Y#&B*AUk#2WTAAj5&iQdIl2h!FCaD9MMJNClb{bk(zX<$osn2%6^Tf5N>T7h>6nv9NH=yml*f0lX'
        b'(d-s$A1E732K}`&pRV<<Z$12Sib-{r+<^=(wa$rz;@mXndpjwMWd7l6fvCyNM6I3Xvon-$Z_(3xD<Pr`K@Eo~>0xEG82iS}guw~x'
        b'W6QwY%|g_Q2K}nb<}3EfN4r7(ptU|a3l!)PML?Glj2zXZo_<@>O3QSFo%Y$E18aN9H>buWWrLD3PEyv#W-^NqK_P;$vlo@_#ZN-}'
        b'W&=3$aWRNlPNyY$^M3rrN89{d>XeV_;ECBLZ)PP)9g^mjC9z@OI(5_anQ3f5Y&0$Dk#=_Aq}&=#3{zOdDl*L8Pq|Or&OTJfw(V$M'
        b'qilGw%J@1Jy%XQFGN4Clc@f`PDj6+=jH8(F>$Dn^oxe<u*d0o1mumde(!ozlxz9@b*q@nMu(_lYq~ytei8aq`C_SN16;oO<mFNYi'
        b'Oa6|`??6k^dN=n-qkF{U%<MuvxVWSj`C>UTHv-#;-fMp3A6GmN1<pL%OWiEV9Ea@D=M|c-#pLLKm>DTX!8W;PsFb1>Pr32lcBQ9g'
        b'E!z%|DlxWO1%lvv{6J~Dd?e`e8*5)7&$>u8sYr9zvFzs2RIj^kUtzn>6@*x8{Q<qKWKZI`E;;*#{;NhwuV+c@kq;jaXp4i&!LB*&'
        b'x=ev~C&S@0eK*IvUOG)vPRF_Zaf8^hmW<t40k_SQwo<wDMPm3%jFgZe#wB&R>{MFX=G7u1@7d&B4$EGtY+9oEDCs44lCwpVg*iEm'
        b'JZVqqY|U$U`kzZT{kb$P)4ufJjPyU1Zu*n(O$`47%V2LWt&@{;MkVCG!KG~_h|F}X_TS{yrRvbye@05+-%;|ZrD|2}+qvxQrRsp('
        b'{rtKN@?hHPI!_W9PdW1xZ0p_}%^5Yft+e)MrW6in+9gri<6`L3pa)-;Uc=sIHo)kVO<U@u<X6>olxx!_b1C^)n=Ef{K#YXQT#k`1'
        b'EHh<oVm1}KIgEWx>0+J<aGS{f^d8ydM_>xirdG3yrw-%k`K4WWTDKC=C42G5@gc3aPb;ha1rUZGL1(vvnyz4X2u5Z#G!pfTv91tO'
        b'oR_NXkwtIBolL`PMEwfPX=>;u>X%^=TdeQDYL%?!R+Q45gjoO^*p<Vq_H8!OB0a{t!?3LZ?>FX8>`}2@347E;{jadB^lC80FVw_H'
        b'B-NXiY<cmoBkBE{dIHW#+Q%(_=iA0LCvG|e>^Vz7(<PlBgQjmvEX_L+2(Z%#UlqTBRX}^Ele`lFYm4p*JF6IvFCC08<?aXTe-E=7'
        b';<WvW<|BA-f5Jg^OIKmu&D(8pnQ!qJ0(^{r28>B|_2Q|WI2T;H6=#u0vu*e@zA?%E7u6%P9OE@-esIb%|A&uQ+*O$QE{}oHuJ^*{'
        b'kI7;@Ln~bxPYl1yyG_z!+3;b$N7h+{g8_;s>JRe6Xs<70hJWH4z96KDSY#vfX%RHZ5&mOj6B)?dfB|PqMXD>@7UJY83SIG(akJAi'
        b'^*fb09CIx{r*OZCvxugt{i@okG#6uLFgHs<*z<$=lMwS0*hz6VyV>%j*qP3KZ=SHJD!WNd%?qI8@J-9g?E&@9!N_^uEmX}DSnW^7'
        b'ay_8LDiklB0@Q5wG3bedIgj2fa(X1o2wg~4PFzUz3I1TI42<(xn8N+j%nZPWnzf;t7>P5-B_#=I17E|+YYH*V>)4Psa6k%LF<B|z'
        b'SsDcP;7qg!{|*a-?y$eZx%bUBvCxkSas5AetoE#TixM=b*Gfsx@}Q;@aAq^1k}{E5jbwGnpbCV3oD4#~a^Lg&#n7l{7--BLg|Vze'
        b'e@UcYC{79w@w{!OhN#I0Ffy1V*r**8R6bAWG^5+%&qV^)WiM<{KS3^YL|_05eb?!pi$kYWubT&7H*+oKKKJv?35b4-sL23l;htR^'
        b'G!;@;0ka#n%}J2q&QLPI-ci?V-`qxkg`M;@{;s?$fDB~0B_|cpYs4T=Kx;ncl-rvn6MI!HjppulJGZ3v0>Dq~PNoZrOS=L<iz<9A'
        b'YAQyzUFJV|S48F{|B6CmyU`=hoIqFJhkpCkom2d@Zvr!&<>#MCU}5bxvyb1k3c^g-f-I(sn60p{<D1Q7=txlOeB67&`+h38Wzudr'
        b'nqT&&jk@ja-n5GjeUobH$7561sWg{c{}<K7qGNies^eArvs8lB?0xST8S+yKPKqyx8k@ep*!b*7a0ZL-{0)dX;cR^NqR17zH|Wr8'
        b'<_lkM7Qla<C^;C-)8tj2S!qT%2IAE*yJ0d@02{{Sm?7$5dq&YEWmdtMEr$c$F<A9MipfP8mV>E_cXr8LI8%ZcJ&Vl)viJ&+eK|}w'
        b'Ei#iq@rXw!O-MJN3_?bXmWdJ`H4g~i1)_w7=J>=e5tD61K9C^5s4jvem=#9kB!LX-k|Q~aETh0r1h_M?kRU?_4d!zq@@My;a&ncl'
        b'N6h>NrZdrI@{vZzUcrIYt4046)q$cY^AF)>7{}4(6g-}f{L?wn(Cb*=ppyCf8f1rH*7$7m;A}HD+uX-K$vlAQ3UTIn9$P_MgRcm4'
        b'>)?oMbSN{^jHGEq)_7=f8rc=KT;c_7c<ioxfp_JbE##ZLaCbiHl8BlwcC(S4&%?D6Iodar!~7c}2$3f&+xaGk_LfP|_#_11Gs5jd'
        b'7}(MQf?VGtj-Z*-Fndz#chffdrcB6&T5FcTH-;leO02<DmB^}w#-%U90)4MxWIW@6pQD8_A#~v4g%U_Ge&I{Z?xdJ*6LR)+tMe>$'
        b'umI>B>Guf#;4tkO6RFS<%x5NKaX^yr*EIlHh79<G2&NE5(yT5vTs1y!8XPzEvCFt|6Y~i|?82FUAeM5wkt9-D;uvPkgeW-oAjSM0'
        b'e!`EF=;QS?_AU3|d#3TtYuMcmCfg(k5j;LXz&ywNnU4z0TgwkTGXOu?R0>8P@uwe#A6%bl&|?Dd#!U#=LID^U#m8ZuK7VG9@S$Xe'
        b';i?$G-7K5DiP;BZV>`%kw`uSd(4VKEk?kIw*@No)TI66^`(d}e+o6AtqE1mvv=ARW?Q4(4m={cfoH~3%ZGqp8p{oayXTujGaC}j1'
        b'b<Nb~(NnD_t{zB{yH9-2>gqH#_h}z9wnUnczz>Evmsrb(MtVQwCA9_E9eUQSZ*J8OW*D^%FxP34a#FRI?S1+&LCJ?4Of^D|Bx&DH'
        b'c@!{<i-de=<N+m+k-?Y|Nb($qKc@rPA^q5>a$2cY-c0M+H}2B@slDXa$6<PmE$d7u@*YYnvSV5n)?#WIUvrQ2xYlH930Q+vqx|d!'
        b'K~HMc8o%CDv=Q3qXvsB^Uo$x-Xn^LfeG(SEh96?XdWc813$G2#Z%vQfL`;;(UDG;H%T4zvyxgLDh@wl(4D<}K*c5rgSHDmnlV-Z7'
        b'-LwtsTnWx~Q08X_M`cp}tIUHYDbl+m4@a-MtzBRmG?>WQ<XmvpCi-3yBGDp$z|;e%<5MgSaEdU5_b)stf-g{v#+Og$`wyOe=jpv9'
        b'>Kzbsv}y8rux>)5ALH3eBDO~y+4RWonRD>Si)`#%CfL{mgD@CuYLh!d+qJF)Kw6MNFhE9Z=h|_H2^Uz_+d1Ysde~Svv}cSA1i@=Y'
        b'AzJQB{t<@3dj8J$FEt7O-x~ezV4p)rCkcefAi^|tcsgz}uvqRKEd3W_iXnSZT?$PmF3U(!CucMzcGXOX0Hp<sYPux}KN#JEi?hJ('
        b'lVMUBOzMR1j6wiQQ8A~CXtyn9zV?5N`&uyS`~SD^{{w_ILetP+`rCvhOc=qP{e=<nVDiExNYezGo<TsE!$xFj1fFXBh*|uRaj@4o'
        b'ZYpHoakHHc<`JWCo-BmgDU1hIBx2t4{l5wSCol3@xf+0N*G!19$09&GzA6!tU-M;q*Z030RXGTM&&KQ2WMPb2N>;|uIJuk|fU%tm'
        b'{Px-p8xsy2llnpgSy64jv5`h+ydwj2ONeY!HxvM@1)ifr*Xsp8S3-ZHzr!pInB`$y`-YJwu%^qFbzx1*85TB+d!aD;e=vY-b*{oY'
        b'M?||6<GYQ6yN!Ju#qBmS+YnmfHo9r(<Ajcvj;bv`iaQ61rZeNO7zf)yzTZfZA<pPWL|liFc@;JLx1z~Rk#?ssq0OjK;NveD2mcIm'
        b'X4Zer``ULasqYHSVwN@@I#WTOhv;-9yM#j%p6}8m5r=DkRnmjUshB+9bZ+qduY&(thta{}!U#k!iIDO<rhO6~TLuKD6*)d~;Bq%x'
        b'X18zlS^5*IAaEfG#8duwfoneesqe0u_ZXzr7;z!w4_p#u7mL#?jT07C<+EU`zxy7%v>phz7D}u$2~abjs~-p-eac!Xfz806g3si<'
        b'aO=}E84HBEI-E2vwuA1*iBWpz`_N1b>V<GO=e-TJcGsZQApEAFji7*!(6Qmn<Hq!-OYGfB=7)luZQz4STW(+aAQS^hKU<P>wnPZl'
        b'Yq9jjMth^TVF4t}(myU)-VJ{CyuH!$s1aOsbHV}k83kJXWcnjUfa73B;kEct-#=e6-JoSSxp<k16fa9pPc$0RsSFdL^uViH6D*#5'
        b'2pmzy9y}!{Zqwu-kNh(*^B@dpOYcLzeiRDpMuw+T#-)t}K!59@4j8mR6cKK%{EKvgpZqm)`y%jGN*r=5?=&2;0Z}J~akGt<S>Zn4'
        b'zz<=5e+3DFMpC*}M9!oRdLNheF4-{v`8AV2^XV$kmFST0*je%}(SWqPBVhKFI|?6=XbSns8+?!0q7JVY{8%wEBT_?#`@$nJ4zUvG'
        b'glA0wh=ksB+Wl|$9=?R*ON8N=mbd<;gt{o|3<{T-CEU*?(Lv#}z{ky!PBJ{!9LQZSX*f@S-_F4BB(t3RsRSCjSA;JG-&f&xv?6>p'
        b'$p2$WXFxbQuanixR7vfSo>nG&U()DkNKECvD*@Z0QwAqV7S4TBGAV^`p<M*{Pq<hD<?JOe!cF6ylJFkUq!=aB;NNen?DG=DdCVss'
        b'7wMxYGmAq(;Ce3GskCMh!x7lE{FyPK2{F3gMkHF_JI_s)bYiG17Sq2bX2fW9eyKfOl76}bIb!2JhW}aOdJN-6OQLUs`xE?dCrT{8'
        b'g!PC!e+lD8N;+?aWqt$p-TNi!@B2y(3#Fi&J&ZeAf~-)2NazL+(;h3~j-f{a8k@Wh0p18>hDwmG^;b3t=Pl{{DUADDNhY)-h2x&T'
        b'mJG2*I7gTB;X!qzgvy{SSHpTl(bvMbLnX=_s`E-%&7hHctAvzJ{uox->5j+x6qsfW9{pn&=PBvD99H>SS2+0N_Lofl5Vpc<J@85H'
        b'F=fV4<(3ymm|i%;n#0n(_arnO5|c{|&%!vigz|`@zYpVHE$RFY)MWvmTuJnIVIZaR+c0FwD~$U~3Dqa+{08)4@|!SjR|)l&Xz~*5'
        b'5eT)HP;ZMSzlNbpVbDK?HCPVdTg}AqSAN>hL5IwHx}~M0AvK_-xn!bC)!p6}&>q$Dr;_%>(PZZN64xS~I<8c(Zwt!i$3s<hGSn5!'
        b'G?b7ER}_fcoA{+u)$&})giaOTt_z5ZiV3A+w#Ln#vfAVzr$`FN+`9E7v$zCFXx2lY589_o_6El-LdKJ|TT9{=LESeK=2VlBF5H<h'
        b'fV)&q12{8X+PDN}Q;8qH5OAr4s*+yFEC$y&pdIxqsV<^v`Gf*vm()ch0*a^ZJIx%-awbfmdy0|oqo{|prV>G@lZDgRQdH7gr|NK$'
        b'fn?+F8t>1NpDi0pR2_!edZ{TrM1g3&n0YZD)f;hSg%e;oE%^d}X!xezf0YmJ3Lo4?1UKvdAMPLTf&2UafO{?K*Xa+H_%xQDf{9E*'
        b'NpGU6F_8>#u=3wI!3ndc6>k@<fT~OD^Zjxwq_p-HK+mMiyb{5E&|LWcj5Hy-L?>d5`G`_^K2Xy~wy7@=JC6|3B<x_j<g3HP@B(bB'
        b'xhb}*X784+nr(_r;U!%eTRNcg-fi$yB4=fO$9EYvnF_Ac)lVy{_fwi~nVYz8R%O}5ZZ8?KClP;K+T8CwdEYr%+7Yh{Z`WQ_T{elB'
        b'V8o}#+q4%{*Arfke<<})GVG^B{1s{AmZ!I+5ZlxUn<QW}lQVjxx?BcBO@~J7K>L4&#fLxRZ~lf1{VEZEUi$R5r?+PQz^7CBIrrx;'
        b'BMQ{@Kk!ZObKkG^e7E+bl)1cC==b;NmEm3fq_k(oKtQISH{PkhCMD1%P_uCMYQI|R=0vB7Z@wLTAm1~&mYZCA%7jsusq?IcxxO0F'
        b')q!2a*-AHu*F#&$+^1_h1F*dA+dez-%=%)%c7veqfqV{Kx~=`!+GN71)~9+&by6xc#ce<0rRI7W9)e_ddzrtlCBwj&kpaE5*KNbN'
        b'57su*UfPCFz8gO67w7%8U}WA$9U=h!ea!bol5?5&?)o0|zihy}$-6fFuWJYYw$|fa`>lu!dgO4NcybIhHcuhWd221e@FmP)n7>QJ'
        b'91>nf_H{cYIifX)2I&%I`}7Tw2vb<?JJ~*&rm)GAw@Fco*v~H-U#*G4n7wOV#4@!nu3zmW$Ve<A4co=l-bC-Ok<H!uv6oec+o^8l'
        b'M7s*P6^-;g8f(w3rtVbMwpIJSKfINML{%KLuyEYz<4HBIO;P)J2xMsFjV_;}ZBiVR8gWzxGk;obcrOw?%)v7}xaGOE&}_w}d>_dJ'
        b'DOt~(t6^W_HPF(+zSX^c#ZO122D;8bJ`0Fe0L8Ds5$1VvtxxzV4A$zeGeD>l*<We*!Gy|tJ6G%PhWV4v2UQ&ArBzhCou+aB+;-}w'
        b'<EHTnORO&r^g>UA6vEf{m0*;a>LQm~2wQ_wbOgBw5p;S#LHD~Ntr4|Emqq#H&a;G|w!Dz?O=8yUsl43)?bY_?qbZ>7RyM8e^G^p;'
        b'TBLpa{{f842QkB!cwalz$ZeuNnPT#a{3hoNAlt&#lutG-%NMgFe>w(^TV5USRM(zI2K;>W+E9RglfO6Y#(d2b!rJYt{b44hNE`M4'
        b'XlMMLPG^20%tIT&r4;#%OK^Pgf7+7(=?QnzuNTJz6Wsj;cjW@-#bpAJv?g)}IiD=*V{zu~BDDKq4rCk-Z@E;=eY6@Zy?Ft?m4~+y'
        b'$fGLW+$^TrRRH##1TjkB!dHVd<vnQvu+zm{WZ|9cgddKv9sjSqPZZtBC`4%|i(s8jCDo4KlUMuo8l-uZD%gqj77IGme=F`GoN{Pv'
        b'K%>L%$d5W`8MxV?8?{g+a}XYP`fjDZ+e-$sQFZ?FpszU2&l7x{(C#lzCP-pbG<!<$t=#!Duj#<Lo@BaV@oqY~4*EWMh`}O9krM{y'
        b'WFCBXbr)xeN5K(;yaHe6HSyxE%>y{|7lBRQhIcq!M4QT~2LI|dt&?tcKIx*{5}XDQVQ5QtW`O^Uwj5_J_|I)KInChTob@bpUIyx-'
        b'`Y3?FbzbLbE#aT@E<=9?^JN};#Cxz`IsRPn;B&>?bH(!_m`~xQ$JD`^_tyCA>ONhpBSt|{Fd%t4T)_FeYMP$z8wz2bhB<W(Vb7Z|'
        b'<t9LNVcu>P%XyXI*yMannLx2;s8>YuMPx|r^^X^%kmBu$^Ti*(uxczr6%WNTeqNwoknRP0Kf$XE#z?XluOdI*wWPe27*52-%Zmp~'
        b'i~HDZ^(uf=+tmFTm7RNDR`#2_=shn76lCP*y6DPP1-TK6=^-U_&5<vPk>C-?3ZZg%lJAd;3A9Cg`Bk54JiB->8$c@ORunU@!ER1$'
        b'R~>dvI8{G9R=lEr>><_7BbB?aM@)39x;t-#Uk~h`dqZ(3{(3-v*p1YiM}EjCKD6AEQQY|FLxm2xiVQqdc`#IS=;=y`-H_7M2P^8T'
        b'W<-p(9#=}o_||e_s9bca9J@Fx`XYZ})@j*DQd=xEhMEvtd{W{REtKyI9Zx78oCg~8hv73k<_ReB?xR2<%V~ZnR&+K#B5`PRPV9~^'
        b'$92VnQ6N`i<~ZL~J0L!u#6-g}uTqR8X&Qe?I|{wMFbcSi48ylb@vsc*s#~#A(}?xG7s{w%*0Ui@KykjjLS9f0hh<Le3uk9fIYk8`'
        b'*ABlN0;wS-R9+p_e|k!x&#TLusYnCA?*uH3f+X&y8%6oDyqQwZXKUsyXJ!|n`Zbl(0fHQ5F0F#BfLlc=4=u~2t&&`;RR6XYGH))!'
        b'e0zUaP_H>G?i&tazK3D$wIU=tbQ_jR2E=treT8hkgt@T_?L6CqOJ66FUXQaa0srMu+WhA-KZo{P0ctZ7;t&wqpgA#e`~_vKF7vgQ'
        b';X5{bTPIG6+#K<4AM;sJ%V$Lw<mUoNdBa~MZcZ{B06DOG=0;zR!>79Kd)|ojI#rF&cj+b?Ro!q2a32({a5i>ZzDJK@5l%3T2vtYx'
        b'|L;Z2Xc6V~YL6G$>$Ex|f{xeuY|uP|$F0`BS7al+R+UlfRjRR9aF4eLU|#`DC+v~uZ$->N(JP8xrx%os$QnDU`gtBTCmr5+D8Ke#'
        b'(L!8D42@pbskiTr6KUTriVJo%w3f@57a@RgPZ8OK7+r6|{yQ7mwt%e^SUbA(VNGR)Zgo#UMR|Vt>W<vD)zA<39PR9>e03M`@G5qn'
        b'(z{Bz7hsBeI#uIb(I5v-ZZpRfF_RD-Za5Nln*KOGaQu~`!IwcwS^af>HNcW?L3T^Tk?pkfE52WmAMT8|rIG=z*ove>vVvKKmwpjd'
        b'NuCdEU)r{GX-Yt(gbXWxXJ!2i?DYK~cNLD@_tm~jWY||d0KX$O?|0#()Yz_UZr=ROjjwtZyx*13JK*ho$7^5jJrw?lB2rQwO=OPo'
        b'`LQmdfX+{<P!||nvWi(?BWn&_cArpY9_O+5b;_{~-sgkbmTu=G+S`{xV>Y1tw<Mq#ARfE1hzuVfn3rLz_o!9l>x%~07xi(Qx%EZN'
        b'8?c|+$|5%_hOe@%LY|=U@}j{~kmq+$_8QZc6%F7$(9>9H(Veru4>^&E776$=IOmItT8fLv<p4?e+nSc5qE;Kmq`~Q73XAs20UE4`'
        b'{%QJ6@r^<sj|1R4v$5Vn==8DoVJbblDDNu9{CZW(uUEOmtz|emj3+giEhJxD{_y0%mx$G=pBYzCnkBb8XJQvZu8WNuaN`=B{V09v'
        b'TKd?(sHtnz)GOZJy!44L(@D+Fg-|_h;+WSs>isfOlK0I`&7qrzLOe-Dd&ON5&cKhlB^_;M7H>#_`A(cTG5pfIc%y@y8JmoglKJwM'
        b'pj8aHsyi|DL6^8aBvX#H2Of`z-$;i1^bnE3VyV9wi}9u|AVXpw!bx#<qBkwk3&kTRgRtQ-9&5IF$=T(}#3>f@7JA24dB2<~$-8<('
        b'Gkl{WuppwN6_kT7ohK6K2c#~T_Qjj7DuR@q5<RVwMUE(}H45I*P5sf|^3262S}r`{614{d+Ag37y)83u6(+0gFFW+VPSB^=?c4hR'
        b'_OUaO0P_>Ci=PW72oM!y=$=Hv!D79AUO;Y4il%LJH>oGD^V9Z(EJ}fnX0E^&qJ$sT=tR!o_;@mSj{zq|jYkeA3gyzjT?6XB05dU{'
        b'z^Cvgf>4JPIrGIDKRurQ1<dy;3~N7MlkmBaRfk-Di<nQQ^I5`gFI3DAWIkHsqk;ah<_--6_UvAHT<ElnR3K!7U4qt-@W~(fPR(t0'
        b'Ib1u;`)d%<QXB~I1L|4t_|O_MvS9&ElG!`F-gfUukZ!iU37{qokAS`apxs@18U|BAu(!_+ZG~TkkAV;`zb5F5=d#Kq^(;3{M1K>S'
        b'eT*6qGX}V#n^JXZ=?$L`Q>JH4m%OQ4F#XP)%J=t)*#qM%Yky`&r{lElHBO>Q2gjQXXO6-6y+q#Ew*@!4LjO8{;m;}n`e1n+9M_Y@'
        b'*j~Kz2H%BG`(@)=*L41JmoKt}Kd+&Ns4j5eO<v(i@veCIOwf5Yv`ci77!Y^<$V14MEQsTD8sQ_I4-VLk3yJxPvtLJF<vTN>X(-Dw'
        b'>}>o=5jmF(kA4BCIZ57f$n>5))g!Xp05xjDZwuZehvLOxby+wZKpXbcw%qzPoj0f3HHhglNU7$OtYWZ_<qxS2;g<)M=LhxYq>nZA'
        b'5SG`lVntq~#A8|$d17*0^SDBzkQ68i!XwGP!O-p9%%kwK&Rsk!7gy#k4$Z~q=PnM<#pmTN4$BX2k}R8<A6yYqAkG&p3m%m$6J<r^'
        b';_8US%c8Od3l}dN96rzM)JUKKogWWriL4A#W@cH9SXpCQkjwIy+1~T)Sb?el59h<bJ12V#dJ5|iPj+B=ion)ErGvFMy877O9{D^n'
        b'{D@A({Javrm@4Lx?!jv2It<JMEv<GB>X|G4kRCp*{@@QO-GkZ8xBgHz%=tA84Y8Cj>z6Qi3Rkw`!Q}0CFQ1&Tz0W-u+G<KUWlBD8'
        b'N@aFF0n%HwDW|l_=e4P4;~hlk$8AAwB79GZ%t3^8I~(Gnbn4+LJ}YDx`m&%0m6fN?<8KY&o<6+y7s>W>P^ac~jMgr2;C+oWZCW55'
        b'<bA#k_JunYZQ;8@+e3H7xdNPYpwmT9zN;AqxOY2|d6Rdkr8kAV?xEz#TRcrGG&N$w(5;LpY-)jO`J%A}Dsb9Cs@kAmL@iYZW*pt;'
        b'KDu}^2TBH0yS>^=g{(WB>UL<C76KBV-oFogyHDKe-rd=+@vo6Sns5&()BZ{6-=m^0W5r-SHWiX0gC%VCRK~Gn<cSq5PxG<GWZm!T'
        b'#BoydusC^%CQ(ijaf4(K&GK=oIN!=5BL{-O!v6z6yYilvcuo{Xp0MoGfK_{jtWZ=;udFV(fz27S%(%*`dC-CD1_(z+D46><Lcsvr'
        b'qtl^~NHi1|wQ>$xWwcRdv&xLCb%T|(^gN#&T>lv~822%cWkjp!{kPL-Wd@6<(UhroC2djB(V-cZFsRy_@&s4}Mw+56q1l~ON_t98'
        b'imCJOV1qPufc`;y`@_&(!JrbPPX3E`YsH$zsbob~_%5)jcZH;glTCq%pvZ1b=5>BqI@rZ2IhpW~a9hIaeLM*_Ez15E1rXc;QM3ua'
        b'b0*vsZz;VizRLh5H6|_i9p4wPXnf~EwtWFO10b^eFACs@qsd){&Z@i0{x9j#Pu!IbZg{neW;PV27+l2YBBn3@4zAEcMDO(1lTcnr'
        b'M`3ve!ecIUv%2V3&8|YGv@kB*rHG4<OO0C|R~T0r_jFuiT*qFKPOwL!%h*-ZMLQKv9a3XvPQk6yv>fd68@%5)hE3EXvc*hD!8Qfm'
        b'y2U@E$P1TxmVr8KliM{_(0_;Kgm{}`Tllu++X}Z;ZhLxL<F<}%-P^w2cC)5ZSyLI7690?>obrG!g?1f3;-6RSI*?Z=PR?x-RRpI<'
        b'Nl}U>Iin(XR8*0XY>r4wLE5!uTBfPLmGn}m@c`u>ij4kKs38XHktPR|Qs`Ub5|7zp;2CLropPA4$rI2iaJ|NfOQ(G2JtPClV1FE}'
        b'@^Q#B-jn=W<aB!qdJpf&0H~KJ4v)SBuC`m1U3ju0c?SU8kF#gfPZD5<Tc*I8I(wq+Sts5U;EDsS)U}5uZ+1O9DspXhz7XMby)b*K'
        b'3)eLAplC2CS}({o`#gSr%|EWl5f^HfOY_yFbXT<V!KG~h<|XO@$qIL8U1)wZSaZ2^FlUIyB6iKx*u(|$d~=UDa8-dh`mf;3?A)fw'
        b's(JUdd@*QBZZt6=f%8+j5<O3!{ThtOfOxVtR448c>(mnjGVtKa$o!Ts$OS)G)||{KzF3R|l;JuNO`gY+>0-sc_mb6-$DL6PDRUxp'
        b'aZwNJkR=*Gg=A!4jfu2~v=^$fbE$$vpZy-shXrodZmH6+sT7>(j@!|{4|ULZlRPEVB?3z`*h!?QN98GmleVu?fkC0upmTLf7gdlL'
        b'LB~Z&zeTz&;>j}@vw!8#e%#)zbQ1fvp4O28J7-5u98w+brvu3(1KIy@Z-4rpm&GUg@{V8;?ZZFu&QR%9e%ki0fyOk6IFyIVh{7$K'
        b'L&4=)u30EX$0_F5W%1?BB5GJ(b5u;qZF7p{J#sRl_Ll}t)I^)A<AtFBGHF-fsbyqw;Amrn6Rh+tkym>HHPJjY*o~Rz;CY9kGLATU'
        b'1312-O`6B0n&_XU*ZKM4OuucM+Utf4EF%NY%^+$rL@wH8aAml1U1nF!fOMCJyyYH}Gi6U8K9wV57KEB1_uF|UMYY#!FQ$NDOQFG*'
        b'&S=dDah-RV?=zT{?xDreWuXRhh=1>|=!<M}@8_8(3;Z^Z8O&*@y}74tVeQ3sLk}LA@;jHru{^+i0(b1c4K{)^qX&1X97KpCT@H|)'
        b'y_?*0NI%%&^MaiDCvmvDE1@SI2y5?o$53eP4bt&Dhp1h?!YLKrNuB3g*=J6QYHv2AM54lNioOrhdY!7aig`iyBld}ayI}OuGlp0K'
        b'u6JW--ih07m!0RW0l4dOtD1^%Mzpu)Qm*qp{cO<gGl6Y8Q%T2&vdN~)5X>@aA1?6OooX{MsRh;maZ1J=yN{s$!RXv%ML(VVB-mjK'
        b'6~3Cm=~a8(ZC1L@yDmG-A~0@~=Xki-;ak?_+8aFqNo`Td=l?HtZy(phl`f9YOp-}Rrj{T?1lndsf`MWS!Iqb53lRfBREQAJt+yl!'
        b'BGp}&+G;KBO@a*pvBgjYT)Uk_BZ11Q(JETm4XKSv@m{pMwzaxTZLw-?%eB^8tLFQh38-ziFMB_~dq4O0Pcn1noaa1m=Q+=FUUlpX'
        b'1t|;KF6HIwe37ZUqmJSb%?irPBm3vs@Cv0sdx;CVv!NrPxZ^>&zOy&BivX9;=!^9A%F!tr<;F<xsyYR^W_119B<v`sg|2^#)F*^='
        b';jT`sn#R?>Y-so^qSB$c4!y@6U;$8OMXJN(l5Dk3t`4K4;h)xD6Hwummr^&NGe<He=blO3jW#}^=G(<D|7$>v6M4;&XHzG}qsoO{'
        b'WLt0fyvWwxi>qwr3Z>8j;A|G1+!97hRz$-SZM__*2$u$rV;ahdlto>eFSdepgy5*@2)a)al4nFBd(QUBM<&*%M`})UH^~OyT^9qg'
        b'gl{ze6-Ylrp62!hCnYU!Ri&F%co_w4XR#xFoe^I+RdoDF=)fbjO>1fw_nK<unVHK^MehG#U`_35QNOLyVIz&~^L2X!hIdM>_hIf!'
        b'htIHSPdV8a*li0sjybpEod?(6_4!@iHO&Q|HGe9KwV6BJY)|c`*RQVY5q&N=%J0I<`vN_@qd17ubs#WR-2U(`YCI(_*w_qleA`Er'
        b'#}@5!M%N<lJAIM$JBM;3mx@p2wc-`=iQIM51Q50qsR%D!g*L*WtK6F~&qRE0R2aAW;Y<L0m}@uEcA{x(?6?pg=#n2d+&z>Wd7Qqx'
        b'ah_91WOR1yw3(f3pgmIH6k>H7k8gU2y1r&F_!5xOEYd*>djG%l`@gfTLln6;ML7@txxddT<kf9#&u1pSnryur%U=Tk_P&zh5%Svq'
        b'u+G-I7s0xxZlm?RaHi7Cl{9S#?QH8$ulz_)eq(bOo-a)oS&t**(*DW^N=G_cNP*-~R<?ZEGIY6ewE<r|>gfwIy~~q!Ebk&L21+p$'
        b'=%3f!3#9)wxTc!Mb5%9Fk|u{z!Zj(BY+0Q=$y#elS`H0hMYBkKkjQ+vcE#9xxQ3kuRv|6rsNm$A(6(ldGL8>16c3D%ueYd&2Xwns'
        b'ku$~ms+&eSq9U%M@=^s!sEl_Tp@CNzb@J#GBm2Ul=3|wrnon2A2(lWZNK}&S5)3_n3Pwd&L&4NX7M}s_NIR3dham68xawDOb|po+'
        b'GL@R?>rKjdb5MwF>ZEw&6Bwq~Uo%3Bff{J**+6tf>V^)@mw~k2?lW<`3>6*W>kaJ^q-PB&BlY5l?lVWhHBm&u^Yyed;6R*7%c__l'
        b'R6$!wQR(C=00jTE{~rO&$c$03FC;y@KxK%uY!9edv=Dw#3PC1g9KBrv*Mvy@$-4pP{t`-7b5#?MRgB{rSNWd<dhr!7l7K7Mtjh0='
        b')L*+?P2UAEh@uK>A1CG7;F|&c#;?}$D48`1!>WDRM|lvJbO~K`0e#e^9<dL-47~(yloL;;WD0TQfhZ%cTFa|?_q}dqj|kA{5?BmT'
        b'#|`6$q9QGH)Ny*ezK?X$5pfBGUxPu9g(mNlYUQbW#mn|`?RR$oil<on16YNK@V|t}QW?U1c(RHOc<>~Z0Z$JqPr>otG^96Cu3l(g'
        b'09=1z&_jpUJwj;AXc^Ovfb8Ty(p59X*5?Bls8K~|O>HVjbyXnkQZ@U0>Rv*#A~3=zg)~y1cZ1W4SP;jE+jCc>e*ectT7VW@mtyU*'
        b'F`TLF4Cv>9V8|~6;PK030>l&4+m$~P(Dw~GaTEx+z8$x1e{^kCb4$14HXH1Q@#SK~20O4}-W84w!A%6NfTW@-#eY5!ZL?kq)Lio)'
        b'3vm439I&nnKtGAjQ=TTw+%2W}YGWvLs{5Gvc+C|xJNB8?eB<<x=;B=PY;z|k-Ua<4AG|7xr*9aeqOmw0;g835HkGKLXK`YRGZ9n8'
        b'vb?(rrpt{d3D8^!uBsET<4&x4BJU_~|87v*=f#cJD85z&KFMIjd?B*t7`B$TQdA)nu8fQmCRz^j>txevAPc%I`|lBHs+xm2V@0Wx'
        b'tJK@C<~08f=s6geFZOfJ>q=#uP_V{^u3cN17AGX%v2ji<^qX}XUjMzJK>b%@ML1zS6(GTksc2!SL#}u}&^}hE+CH3)Yt9AIa5Z})'
        b'U6m$HSF3PQ>h610>Tv6sK+PvPW7k*k2ne!jpru>?762yU{&xd~Pn2km2Of4{xtAQjDT(7hoSPEIk5@By>)7XW-atJSbVlI5gV}Zc'
        b'*EoF@UTKbti>bVnvmq4tj)Qv%f|Q-S&h@4XXOiTlKq&NHe6%2DoPO2K!yotH&bPA5O9J}N8=*VV^i=t?0sV#RMx3y)FXUA$O4}2i'
        b'y=eEr9{y2olIPqw<ee*41Y}h=LBf>SdXDoEx{1c;0O%Lv(5BT9UoTDPNGjR3AWdc2KHQp8H=gz|ymy>KpN-?R<ovj9J3s;jwo_s-'
        b'4R(Yhmmr&WW8{9kk1*MSiBPTDD4c6?eH(bEx=X0|Hek4?q~==5!*>t6r1Po<wo1!7y@Q?78J#=DB}3kbwc>3FGaBZKCFQS*Hdyhl'
        b'5Q{--H-ruu0(Lr7Qei(*WTB-H_8S?}VkBjHfyIB_uEd7xr5jrZ>ZMIKFWN9`eO1&Vi*g<rwjbFR1W-OF00jX?@SxZ-x7YBc9wPp-'
        b'PKzN=U)C9F+`g?W81cJZ`ywihGFi;LB8o)Y;b_clM1g2k=g@x!^s7W}Bbc7DPLrZC(Ad{)>=IVJS^oYws}$hc8O%acvS*{3I^@t6'
        b'gLS*gN9w+~-<{RoJ<(=#Gu<Iow&>1_l2&4$s4WsAp^(-vh(kl_!#WtFzbHD}KNx5oj}A|)kFF1Ci`*wdh^rVvzY9|tLq={Myl2?S'
        b';80Kb69G0)-gxb!L;7Qf^g9pfrzD#Hf*j?vtkN(fo{rv{uf8|1Mcs8&f_kB60{xwpy(&DcDkZ(wdL<CYyFZPnvHEanDo~z;Stjrn'
        b'wer)(`mY7f;A1^_=p{CAycePb*O~zIUXb@i*;ukNr9_7IW|oH4oV7i)s5Jr%{#>v@U!&vGU5CfPpHSf+2a0nNN?q;_gYy3oK*z<g'
        b'`r1Vi;=)b(dGi)U5LSpc(S5M`giApe>mX7$q02W;sq5nFeZ!7My|p)h-HD2i%|e7&pgIDb84I|c3_!$h-5bE1&<@`S<iA)FLs<VB'
        b'C<VfRD)M*$;kdsv!v9?W#79)Usd<@e2S*7sm{>j=tQO-CY`SI?E9htRr=HolK<{Kj%k2>}AsugA)gu`C?&c&?JG%c~?veXgK8h%w'
        b'Km&nmJU%wm{5X2__#&xB^IZLCoPp-Fd@Npb&0G}B8AF+M=;;v;6=R-#M?N%{JhR~Tm_)K(zq3e>W}rjRsOYH-D#~0ohubKm?-2E`'
        b'a!$Zp6gE1B2>J8%+|I7Z*=S8RL2LC&q959<dF<>UP#cjG`K6K}N7iZS$KuDb^u1Ynhg$DpYt02ZZl}_wGd9Le)boa}1sYe`q8iiO'
        b'VZl}MaR@hbswse+a0i}f`|B68xOL#v+uJS_CIA{}2g?<d=1}UX$X0P<x-G<V7_TR^;(CZ2(!<+g&7Y(1lptv15&kjyk%JS?p)aUE'
        b'z7*Ib-Z@U+nqZT(w??!{%z}d8itoSA8d*2AR?@9(|HIWbC4?T_y*N8wmz(cKTy0Eni~AE0Z*AhbFupqhWbcj|*)xsS8wRM@O?})&'
        b'Iy^l$8gMa+LKj$S3%IxbJnA6l!%2=^F9yFzV*aj}J4|t==+xzH%~YRxCqhED>PC80njl_0iFeU>ad&z`hXBoGw(?uT5^`f9s7Mc|'
        b'_z=89FP5gvX}%h-B!wUyC1d?6kQNKsW4T~hzu<;4HmCJNrW`|)EAJqYk=&dp?)ZB#MVQ|}l^aeK=aLh{34bA4zx{V^a&r5uGrcR1'
        b'_troZf=V()oJQ&Ag;mq{CI4eKy}URhRb{v@Va0s@ie@2bxdttUPXt%Y*;{H}ifEt@72BnWa{1+nZODP6-!A5!kE4O%QmE){R1p<D'
        b'MQkPtIOwvf@75hC_TckcL-s|riS6__DyA*NPDi%o+40}BCD`eEnwt3bJOveE&r_}o%;8Qurb1Y!;?%W^AK29jG}^h)=?gb6MG&v^'
        b'=X&N7s<-4b3GzfhSS9dscLTAGEX`K|tnovKv)E3{*tSr|_Sx-iK5D%6i$Lq{Hc$L+bUrtR&J}z+?Ts#h`FX^*`8?})0q7`!ycUFc'
        b'4Ar*_z0}SQvgX3|x!?xgYknU!CWp1y{6z8S{0F*xVoh=Hnqo&|v4^cPuPH<(Rn@;4^uJ>Eh|XoLD%PRVcyj?a|E)ST4W4HOpJmf-'
        b'q^r|*rK`ZXv=Jqd{MNB8tx>ix^faNRHPp?>#5X)|g`4|0<;lCw<^6)YN2<KoCTM)$vK?=*pNem&Z9Io68~R5;)_K#)b+Ar0+#HU|'
        b'F;(c4#`LK842p=)(<YQ(hOU8Ir#fOs9+`c+eIlCX7Wd9Ac9ax*9LZ)qqDiS9wK>7)b?6&3@Ox5mBY@8HFyB9W<j4cab6RkUI5wlW'
        b'cSf;80{{-2H3)!PZE+B(8TZa>wmA4L8M1Dbn_vjV{$2f-j!Js?=B#3F2Rygij!rJNI7lTiapRXq`Q}H8M{asTwvm5YfbdHx?tQq}'
        b'@gRUdZ+-xQKdc6Wo;qdhyk;kWpCUO7;QQV(KTv#!T^%VKTihF8?2tp*@67l8Oxc(_${ytdO|s(Nm|};t*y9{ymZE~KT)}jCUM&=?'
        b'OOMPn?LMVUGVMmA$!<j8{#|D2C=`yjp9_z2IPi*lCB=?Fk;nOf`6klnl^m$llpv_o`+xsmMK)rk(CHvowBGAhohCa|9H$GCmR(-8'
        b'o8260o{UtnKTk=nV&ch>JGs^pJv;>aVo~qcMUHbt9>*WepB8YeXAtY}o7c=B){kRE3b*K#`f%E5LEl^8U7ClAZsCa0$BV#4VH{-3'
        b'#xFwuOMa%84~~GKOQb+5172jelsm}m$(aZ+ZXSye3ErFM14o15I~m?--cWhO?QwMTyG1hzipc3^6iMIOGU_IWrsYxNGi-Ic$Gl2t'
        b'&_YuzBbyqZlQ!HWUw*5P;G1_M7MtHLg1+n8v4cgu2a6mBiyr^b?75>aG4~YJeCHMgU769e?jlGzP&C>`llK=*oRDYUSHvv{PEuv5'
        b'-kpM_NX>7cgd~+WDd}r)^Ey+^JBzqZ$-D#oXIio#wQm1C=GW0HJh!Jr1;<2_zt&}_l9G~9oM3jLuhwq@Xj>6_O#b7{)Tk3I`&X<}'
        b'3RY2`Am{D|xHUdK^aX@unE5pwcW}likA{YWb5m4zojs&HK{moY%001LdhDg5-j|9TFBN$<_nDtU#8>FT&1+F*Q?ADN>Z0B?C4?fo'
        b'hh5Q)HQP}7sSA$PMF|NEfuS+!@;I67<jrA=G(kDcNEzQLh#W@WFd~y>*Rk><^5XzEkJg`I)&c*VMvQ)@NY;S4RO2ix#wweG_{H>~'
        b'qZ`f3Ml}ZQFa2#%Vt*PzNf;JKy9OeVYA{(MCM%Ru#~aKGxbfI9O2k@fEm@)Fa`fJ~u?uIi;({L?|5nt4n++W18|lZ3z@R*VUi$lN'
        b'W7BkXDdOZwMfJLP?gDLS9-5K!@^wWn47+3Acuo=3pUX?u6;TrBTYU3Z`AB~Xiqci}jCSNIn&24nCSuCBsp-^ktu(`yoLkh8V&M_D'
        b'&-hm}lRWH}qx}6IkZBbnW|R0>R#9(Oks}KlmC_tG;#Ax}liP4u)E<uKO$e@;>>-@2*JHrUd-6GhXmQ|E#ohR(&UKTEdM6h_pC)W?'
        b'39G2P2e~bOpULew#!=OSb<#eYP1LwDdWHW=AiAzT#H=hDY=Lma<Yc#`i`dPkIAWqXZzeb6x`kUD)R4~&bTbPk=@vXtz2Lz*+3sga'
        b'?iK{<IwdjhLZ6Y5zjd$DX~E}Y9Phrkv2oPZ)HHg}gz!rQmiR4LhnCmIWNehQ*+Z~z#`DX+8lCk<JLqo&&&V==na|A_Q)AGjP~fv)'
        b'8$C;4Ei~?l%CYo!b6Vl4r8|VaHV1`R7G-cO*}^{NWU+~9V~5dcRwnx5oCd~8;8^Db#r43**gDdw_fQ2(3HtmTimxQrisSK`Zzl0y'
        b'<x}^ZVYehgY@O2#u500$IfIj>^HNHAvh{qGVp3|_wCK$}A#6|W^*>yA127}&rET;F$>*~!83blK;+IX@O240cF6(OHsj4I=1VMGX'
        b'L`hpsPBHe)Ml!XX_dIWsAUc~IJ+B3A`MDC1SIgNdImI+??BTio9#B^FS3hov7uH;|%CIz2xS*s*?2LQhwBRUzkN~r?p--6AGlwF;'
        b'H0qH_T(@hElg(_Zmp{|+h$jTc-keY&d0@C&ny_M(ty+ZD3>B;h)x|wnor~#maaArVr=7!DtfPV+1X6P$5Y0T&2I<pKy7C#>nQwAQ'
        b';ljJ1)*c>YpnTR3k#CLiUJoc9z?EXndz`Fzu5*E<VlX#~V}VB5iB61aPA7sFR$?|;f7;`<n(qSORvN=N8iEt6$c&?v4_x)|{8eCN'
        b'{_5i(tnz*YYvUcTY;g#bH3;hN+w9=X;Vn2L`o}B(M-a}?p&#S)@V|(Y>ttXiN8ek4#_$uXg0R3e+m<6h<n@4(FEmbN_sgBJ51_TS'
        b'C37Z;fsw<=<^~)6j5(;$W5RQk$;02YhKg^p$t}~+ZoG3SljdSz#Gj_7Ktuaz20Dr9s%08(nMRPK>qEG^Q05~%T>Ar!5kH{m#Zj6B'
        b'LgQUPli~r6HGW_XM~wCBpsW-F0HeQwnlM@v!P^_KC_?m=7_b)&M*IK<6b-@%-k$|Bdgli)y7;cXKzoERW<qck4#0#6OW^@$4Nb(j'
        b'b_Q%Nj#XcA_>DP=V1rfxY%~#%7Tloci=#U5Ht_ogIF@$>EU^-O=?IR9;}SrTV>r5^6qO&9{ZQ|Z@$>!@{M@7XwFhi(|7!dwG4RV4'
        b'g~nef@g)B3bBx4_Jpo$-8jZT`-URdS4%k+KO}f38gc6tU3fM9bj9~hRZKK3PI|G)4h#>Gg)5~{2`nd0>DYipeq~m}N=(#i91-wd7'
        b'-a;c-ejB94{21;~C#2tVN9qX9<sFcI?+@y8L)v}c&x_8kTb%W5Vfog8g$_NJRgYT|CR{B<EtBiIZ<pWMtaCK$d@MHP2(SrqZfgd&'
        b'X6|O-R=wOAWyx!F1HpS!lIwL;BwA#~lczOL8o6^f=IX?5u6s4t>Jn@g5q2ea7|Jz$#%p?&pU_4>ryHo}?n7~`(ls`xi?osL_G4(H'
        b'Vuz?La^!BnwFLdNF0M5EN@WCHt&2;O(9h^Bhp*dN%oN|u-66M37q{|jdZ}*D$}j2P!ndpB=-sc>$h!J(@^1TpG7HZ}97uDAZA!33'
        b'URn9Tl~Qe7+QV_VQ=AN5o{G7d#tSyWBMKRQQ_8(69>zQ@b!+b{RbQ9>SC?Ccc5`Fc&{~YUcNiPmEJLSiC|ok+Rt3+>qC`pD<(j8f'
        b'${T7=DO<;;6KL7Um1oCXnX8RU50BG6Xr8VEkBeGko~CPgQ;T~0$Je+fVI5)mRhW6Ij@t+4vSRvAc$5g4P7hl-bU%ESiEj=)f(7?;'
        b'dD!Ky1eDfy-BpC4Rplscusj~6HGHR7hH1VGcz7XBmQW}$r;*S{eb+^le;M$f<?eZl)omhdMB`ywWL)XwE0vPCwDEDdbWqN5D^+_|'
        b'#yg^Q6}HbQi8TashYi(WLH@$yWQ?2mprYMjidh(Vvyca*hTh9tWx-e!c^3}Jtvar(q^^`cc)Jd&-oe+^rGMoPb5&p*y#ToU>DzTY'
        b'i0T0Nc_TKhhv)dF@O#iEanSA?fi_&oK`UQy3!37095jG63G*XZLmJd!Jlu;F4i(B&A|r#zP6$^rvO1xT49R&T0l4!8m?eD_89eO8'
        b'^%Z){5cJ?(1Vp#+yo#SjsClBPxQ@Y$4B-=mOnI`4^gd%UKaNzblz99dNb3@s=jL%EQzfs&b`gs6$kz3x5j~`j7lOvj;XNNM?F_|&'
        b'Ls!_m4f8fzLeP%c9kwKk7Ms@sZ{UqY7qi?u8vO~z+QIcn^c#hZ`&-40&$cEsrYp_|eWqT_vAs}s3DjKX=H)W7A|66qCkjzq3|wpg'
        b'as~qzqin>y-9AxpEcjGLF42Sg_#$}wB+x%EI7)wOeWMwCS9)Wi>@!{$zAp>9kM1lgrVDo+LwA32#<dGqe1=x$<Q*k@1VGQ%@Y27k'
        b'M+oU?FrW($mCDNx2jduXePIvJCi<SeF~3-d_T1dE&*-#`#$9GpAtm9qB9HFtv=RBFsh}v&R!<aEcyqc1E5o8!JR5dEv1oD<T7JVT'
        b'=roo2<>o#uy1nY4H*b1XO8yufiy60j%NB+XJ|ov3!t@78O5_j2s4>txoyUiYFbgw&P4zik54I}OVjO2Nj=#i=0|P@v4%gS-5FPi$'
        b'pj$AyLfUXe8P<xg6$51<^|+z{8!E(XxUBmcYPl7WhoOUT8pkc$D?ekv%4cHda3n9r7gKi7TeWMR)4W9++{TG$^s$xbTzB(;_O@*r'
        b'O?yXsyZ^DXI7C^Q^~jQNTk?<c``t<Pwf&_KFLF9B=9aOb7z529FnH5U#ehwkX_K4WPY-CN&MeHte(lV{Em=I1J1f)nv?Yt5Y5Lld'
        b'CCId8S+YoVmaxfG<YQMlvxq6nP5s`w$pRmn1`j)Fkc;aZbh_Otsu5|C>r>R<cgEzeK_SpG?Z{0ozbG5!E!iyiS=sP~VCZhiM)3&H'
        b'6LW`bqAbRkOH35-gc1$cH#?bVBp&5a61g23Y^@kldW7{j*y{2$B$~sVXfTisFcCfih!OFmfOxny2aHcSDxWFZkrO94SuE#dQTaXj'
        b'1k*SgsPWuQ3>IVbRMCj6f*ZsDm!tfN;e1z6KK~PPIZyyi_39mR84AiJk>cbczC$jpL^?i|-&C+r&6+Zv?G7u*_EKU>){;s<5VODH'
        b'Sz>Y6qK)HH_lCDJZdLTN+!rH@byhsf7>&FG59OpJJADP+_`J@eeDmd8bi^-idCQbn(eTh>yqYyp0^@d5*@Dnz8hQV2eXWoZk`Wjs'
        b'^nV*r+y{iGs(qpQZ~0E<p^8;m&afqIQrCT0tJH3sOpUi2Q!g=-p`#2L-q_rYL!QrtH$sm43XYPlc<gx)=0lmg<*xCVD;kqcyf#S)'
        b'%05205vOAOK`I2k1DqbdONI<%*<0Q;obeTu?J^ZOP39vARsV-0vK-{(_I2)US$<zu<)4qr3b7$K%)?+!YZU{XQr0aWXp?5HRhZi3'
        b'JB}&_R!dEda`y1kzATLOe(lS`omo8ga8{H1X=fI{3CUAn2f4YkOs!83%#hl%M5d;%?O7p~EQzT#C}fHg@?9WgUlw7>8l%p-dxvSE'
        b'j~#Yqk@hUHn*H6Vtd}8Ks|&cbPcy|A#W57u2G4NEO?rHx4D-+wDo%yxQy}!Uxwo!W3hsY`v<tIu9rrq7SNTA(`QzEQ?F;gc{{Dma'
        b'le6z!&)TR0r)29L_bQ|Llm!tZdtpY_FFi5(UjA9Qla(vH-;TT|iWP^yEx&MU{hYk%vc+Mlxl}iP9A$4&g*%TV(bKf1PF&t8&tKyz'
        b'i{S2UU>CHgl6M}|(!JUp`<y#=WpTUnhHX+)hnHn9JNuG6?<ASt#Ia84j!rogeO#ge#jrTBnoBKdJ&rwEmMgZybeVNK+09vl3DQpI'
        b'Fp{U&{GT%h@0XhDo%=n*_e<q%2%zc3EP!b_oYd5G8DN@hxcx{{L#L@t+SCbpVnQ{n@xK=c_J?!v`J~|=v&&XHmn~avTIek^WHnTj'
        b'J((3<u{b%O+ygEJi(RomGcuLzAxI@={@ZLvk+z{WX@R_Mf0_CCY{$E^O|_=F{ZGga3Lv|RHSMtohO;mgo0(+EvKa8BY@h6HtQ$Wq'
        b'JPN(COC3Q8DZ#6P9EBiwMUs!km%S%1+avEH+6rBn5v_&M#TgaPhj2l04<C&o^&lY{_RMa@%@1j-7B5P>5Bla1^IlHYBw7<C(u6_m'
        b'O3ugN*MB|$_R_Fzc2%YM_1TNMPs!Hb*x5O|OJG*a3hwXAxZ$C(g16=7uW}$^F<9VwdXH+~9t+_gKsVkv*x6J+yJbO#bY7>a(`Q~k'
        b'yCVx)oyZ)S%Z=YV?6Z9=<zcb<Li1RZWGj@#3R<Py0cFRUXEu3vXKq86EwH!m8+40ydUDev(P3qscN|}~^VQsuYac4P<J6Sc&bx1?'
        b'IG&j;dz&;rGyB*JGdbV|0C^LF+;kgqt7zw@+#PM9-a9vc@2tx$#dmx!<=dROk)tV_vV&;@Gk4tHvhS=Ux<m>-#x}_H;?KIXjtaYo'
        b'`a;+J5sJ8oQo2<dT|Aez6*gsiH>S9gTj}RT^F{3)gnvh%iv&h|5@dv?AsDYd&fR-XjQT}tR-$9Y!P)GX@Wwnzc7L{(8|wtQbR#i<'
        b'WBc$&SmCtUa-$q=6i^EEXM|LL57Fl^??)NXp3E-Xyf=p%X^of0J9-2$#5<1ookM7!%kLkW-G6~|)X-bw1-C%KlTo~MLAsD@ux^2;'
        b'SE<MjcMIX)H7%UVrHpQ2kLV~-Z?G6b<A3iWWDrcc1zeIjew_=Kxdkq%tfHuds?jDN$%0S(a!f`?&-U~txe02V;$}o{Zx1=VTAF8L'
        b'bERh4>^vKHwdAtfmrCY}YCc^yatS1W%L{iCJv>ETIEAjOVjM(VHd--5Ez#mfq!7jg&+D9hM=Wo^X7XfTjcK&x8ui&|O@0=Zb#qou'
        b'vmh-@Bfzk%>+npbG29$O*0=D2r>S~yD$2D!LOo%;@RKp>v1H39BIg8|`75OV>Sj{^3C_T$GhE`ADA7q{p*!W}_6RkLS>@R1GV>73'
        b'GJ%>YZgh9oa)Eu#RW^6CWh}X(GNgMN^g<t@vfb})inhF!T^Ef!Ve_e3!Q(UD^-KtBe5VT?m0^C5o1R+`h7RRQ#+W(e?b`p7t9|sL'
        b'JPC8-fXGmN1lQ*SFMP8&(YwC99k1)glBVes3JNZ#mJ^ysvBDKO1=(^__Jq>0>N(`u2$60==-CKDBgHCr$w)pWDkbU(^Zhxd?9j~2'
        b'%Z)|O2@(FgF|4~5oq!2skywQ|$wqAJHXi<%8egWZ&CFchztD2{f=OH3xNt5(iTw|QZ#9<8=Vvl<z@AJ2Rs&ZjE*z6PHnY>4`)*^l'
        b'dO|3A+SOgl_Q{WPn=A+Um~kvwA*OPPnD=wirkh)4<&-{_6`Na@9ZHdl$5u`QoB?Cw0_@O2NrhOTW-xs$=3Efb{q9^s_T*LdTiH3$'
        b'&<4$Q98bj^?^?q#KtdyjQhq6hRZf$US8{m;1>uV!sxHg+)~&~FbLuB(LNKg!b9e1&{!y|EE$%-Xb@v_k*Ics_;1#ji-m~HFSq}vn'
        b'i|+25!0%6^2>(4;W3|oLp9Y~*6lPv9s}AX!6?DyPfM?J(?%)*jzrhQkVtAHjQnvCsNX^OO<-d)vfNal=0VQcU$4OW}i(4tt!z=$J'
        b'0N*BwzxQ?aZS8YaMFjWp^`D_*X6~Fh%S{YzjX-A{Vdl&cE%<tLJf4#5Bld;uV^liQV;ry63HPb@>Gm0^MyKy_^Pe<mQe^6^cuTz<'
        b'{_4RUo>lKbKfckvduPThutaRc=sN^X2(K^>FGglo&bsYK{O}ud$2ZAa!}-!awA;TgdmvldMR*P_H^<K6+V7?)z*3wZ^-gC8<2zVs'
        b'wrTE|zxyN~Y<>Byy|s=NGtH7&x4%1{nrRl@`To0^X5O9ePtG)Bcf1eX2&5Ss$C6SkOE61id|2zG!nH<~F;!(ma^zthVVpVcV4x3%'
        b'Kb1S|D36*^{#n4y9OYAMhAsr$Dk{;#hAA!tw8o*}K1l->6zfny1h8JNlhb?h-9%bd|5$L@bD?d&pO8&yl(DvO%~&+Brm~azvHYyF'
        b'Go8Lttx9DaZ~g?$O$=QMxbYs`l^;PhrW5H*dRV$TU6*bID}%(PMtn&>o_<DU3{ydqkw73*DY2cndQHi1RORx?PXlPhui|{5gFi{E'
        b'@4GqlIR}q=t2`$nT@XA&__Kg{FRE+jk(mlpM9_BZ;u7ATIrKsV(8u}2OL=Lr{c|XuwG*K$BU2Ydq-i$s()c<VNyVq*P3uE1rfb46'
        b'3>*^V91aUr+XJ!-H>`gIpJJsbEpm;m9w(9hQ^LX>Gp7n=3vRY<?Y0)Yy8v~UgCWq?2(k%ljqO~)rg+&7Z%3?t;|>3rKtTb2ldCIa'
        b'YRLQ$@;4YjOT*XLN_q8o+E@}t%$q8Z)!y{UNbvm5#ktA4M#7qmeY%VA$6?i5Oe^3u7VFl$uiw$>?T`+4Nl$j#r0hQgou{MS1HY#;'
        b'I@uLZwJ%BOK?Y+rBD_C=3<EQ#IV|m<&E3;cJCl)~*Z&<{5D#ktAH%69&(Xkb3}J5mcU0zc@u|LU4ZLwvg1{g3_J7Yz303Jy>aBEw'
        b'oCkPI&ugC5H+*4Q;XO}28}~Uc>5Bz!^5~cz!Fk#|4n=G3xO4RLyg|ScsJL+9JZY6-D>dz@{P*?m?Mh5~VL`zg@@0qQW(msdj3c_q'
        b'Wu4wtZ+67(Bd?1=&_wy(z_wN7W9V?E(wWcmQuh<T_fH>KaeUxC%Q;~6Q33FI3<OocY3oCnJ9bs^vJ~&KRo-V~^?N_l*pO#iiUWTI'
        b'z~6{^oD$21Zl20GDxhA6I6{L6i(cQD5#5=z(R(~ja3+p$#sQlOzFlzP`Sv%NZ`$ue>;2o3%^xF=#!dE+t2#RXt)Z?!Yx04U{z&Y-'
        b'2W1G6wq!I%$f44jd^Rc;e9)tJqmtj!=D(t{S7~=#Yw~cA6VKm$t<zb7Eo<{qQT_W6oo&f3H-J2q&>g!fW!Y!m^Rdf{z4|d<TT4(Z'
        b'FC+7LNno$_WX)H>D{i>`zk5YJyrp8mW{+qlF-h#6r)yu*SzM45Uhs1Askhd>liRf3)3lz3;9_v2w6kq6U7FE0*e0dMwycj$KA205'
        b'PkP9cluDawy@P4ehLpit_(5lsJmjTBN%gf;MZ>kyq%@QHMn0sPQcOb${Gmj?`C7h3iOF&WHd#rlq?OF&+n(t^?-yYhw97EQe*aAk'
        b'g<*AD2tR?9o-Nrzg7vXj#Tdo+lNc3I7t5b(fhXJ9x>$UE$XrWZ?A`uyaMmwtE&c^qy~S$8a<7=r<YzvSY+CJE_fdYsYSS9Jz~=1|'
        b'c|prdz1|n4@CMJO)!wF7k7;)D##SIRv(4+(O2H)s1Dt8|<`VEZH>{p$dc~W|w1u%-ydBJx-E~_+qTAZSEQb$*mvq90Nw}9O^+ayi'
        b'ls9r*A<<x<)d#tct1$`pGDRDf%fvjL<C;-g4SsKRsWH0v?9+q>+Py%1@Z4OZmMK-`s-ues7fR=<s#4N;B@+npK`g1*J69DwIc_sQ'
        b'U9GtvOVd&OXmk#(PFroAh@IFSQd%wHz)6ZXC@=)Be6F!nr9K!5$to?QUoXs6OR_g)V_LN)5~Fr&)ww!j`;(HQxw@)s=;<>-%zs-~'
        b'nA`Nq_ryF`TEN}bLq)W_5?h#;TTtXFD4|U+dIw9T4aMki(PD40w4lgKfoKXA*3Ku@jwN}3Nv;}QB$T3>fTgPxcLihaT&reNU}Udv'
        b'v+%?W9Qtc21Y*ZFfm|8dVh;yVg4IBSHB)b%ScM07uH_T){7E4sxK<DZrt|$2MlZ{^NvSBgEtGkGkP4A+tX1x86SOm7@qA`Mc=C<u'
        b'%oZ#)lCmQ62hijBG=KWYzEE(lC`AdM0P}PjpV7;0u=ys?EuD!LV&$VrbinD<NmK5GmUE>wK6!R1_<-ORF>mF>^WvvLd@u)`yh3&U'
        b'T&IpT71-pZQp+52?wnG*gV!-_(;Gk+0Ma5rjTZnEfUt#9VRD-svVpH8=b#1qKsPaESNpEGDesscL-{-Kv@jdK586$xG(8MSihvFQ'
        b'R7R4bCDOy(VJNo}a;J>sW^UzXHY~)nVVwIE%paD{xS5!zAb-pn^Td(-s$2P0C_gijKN9jY=_<FH0{9B*9dq<Ze%-D7I!<r=IQCAq'
        b'gwwiKUCiO8q;UOHe8<~4O|z5PbWhCtNe|JP)4YR|LF|Lm&`*jqwJlE7z9gfK?eH``mdv)(NuA!o3~A?P_{r!*#~!tLRcuUCZF8FH'
        b'?AS5XUt;=??Z}DwyQ=+3QjQ(FI)fS$)3<Y5PRyxG?MpQeV@QX!>I!~AtL|I1M61<hvf*nfy_i3++LO6G+4LgKy1l_OYTUt}wPV^}'
        b'VKUkV0D;*Efy_Mb;1+3KCuC|EL168erpD%6^{b+|@Q}g}XCS?u-pb$j<~~)oYHRcw&Ak}*st9ZWG&ohdx?=O3T-|wf^yGA1Qd9U^'
        b'u|A!@quG=6ax!W*_1-~rx!GVn`e~D{rCOR5*H-TU!}3^iQwyDx?j3AKh7(y&ZyQ=qKb10NG$+-{)6}`DxUm#`-uP;3NKX7qRt(Eg'
        b'T1R6w#e5NW)$6H1W!O~08z(Jeytxx9d4r6!it#R#W@^0Xx5DeKklLnI8R^$&KntD6<fbSINp?bZ>71>~oC0~cK8#P7<`le^EPv4h'
        b'+-hp|4x)?5&>mBCtWVu~xxIbK#`W@ePt(iE@`<#G@uCaFmGINRcp2%$Hat4poRYWhl^NQn8eXiqRJV`N?8WjcOWdWs>Ku<_>2b$z'
        b'&$KUbzP<mM2DPave3In)Vz1IEU!OG?FWtxt+Jirn?rLeh?}E~6cQ$>KHTatJTHD~a@Pl~5cwfCs{)gtKczHs0w9Wq@*#Gs#<O66i'
        b'=`8*ZrN;!wE9fS>_xk{;me#nF${lu({7b~@!Smk1KT0pO4W5UeAXx7vxqKsnE6?^yY*q*Wc1GmnmpUCweU9HAZ(m{>46jqP+8s;v'
        b'FY)QSf0{{l$8YP_$64B!G`uJWbhaZtvA`#%G$8?gIuW1bO0UJSRNmSQdPC>UP#oaNV=b;8UKwLDOr2qj!(<iXD(5)cmsE8guB{wL'
        b'MVcC?wQm?-`Dynz@7E2S_3o(fE^^A3iauosvJiuS++x6d27HL+S!nFAbg4*oA<X|(pmGIx(Oh1_$zm+KoErZrgHs{rgiTG$o2ulp'
        b'2e789&<%;9CVx^~42o(8{@|6xVLM*+x_KL!jh(G29lS1H8-7GOv?pLoX~hpCrIbb9byg`lD-y1yKn)>0Z+)sEdt>W~Hi6`g9j0)*'
        b'V~M_0Z1!t*K$H6e>Mz*Q{-PuJ159j>CZGvB+n?+#HofR6fSh$SYx6>rY-r#bC+c*IflEsYTAQsASb-@VB%ycn%{w#&e@QmEJgke}'
        b'vEMuRx^#c%;Qru`)A8HA>y@7NCHpy`e?dTZ0MKr!X^jbfci2p$V3!uSo7+41ZBKz0%+`DBpQ@1YOTPhfbQ492ExZE8R5+BUKFEh2'
        b'ZE@|qqRihV7wG7+V(&n?v_S8L9xd39K36<<!N}QFTEpDmFE&5BZZwKjJP`0O#F^gE<Go3jSW(hj@-E`M^aK1`x*U3};QGGw!qHM@'
        b'S01;9vT>fRsz0(kA>f&Ct1MsclXvlgWnBvXNG#gTYkUN})&RFd%)BY@)>$&m=&{{SSSMp?_5<(crck`pSE8&TSjL;(67ZCA(MWz1'
        b'%GATxO9C@eZ1(Q7ijM~&wE?B3*#Y#EXaE4cb?dn2)!eh4dp2{=XSnAVxaUi<HQc!OD)i=ILb*>Xf-jGZe0wVRn!$ZrhF(-mSmV2%'
        b'3Cu`_Cpl2Zx$l)6BF4tA(wy88t{&!LL@jsI%)@5fXo#&gD2@tFyaK)c8npBUykLt{WGN)m@$@W8R2Pm*RznP>Dioe!O)8ch{K%Aa'
        b'%oKAs8vn1S>kH2qqK_M*E*WBmYOu3nJ_n_-NQqNCmHO6t4_s%M5Uk4lXdbr{;Y2gI3~S=WHP`&36~^Q7sKT+hq?XwpV7Lkyu0r`S'
        b'6ZM}*`B0_cdsVugMpYs>g2p-DtCBk_t67Lvl%Rny=Zy`0m}Nplr_Hh;LW71Rz-L(Zg1X5T3jV_An8e8Wp75!zQUax^NfZS>Qriub'
        b'`6)G|1oH<MexbRB<{KkrZ`U=n;f5Uz8{K8D7y-}KXMRrYToBR3`6su_AlzQPF}kn?>D(1=QZgZfohR47!gsO-=6p4Zv&u8{*RZ4F'
        b'V`K9iWAh$=&b$!?gj%sSN}Hg~(B^69X{)rI+Wp!-?Mdwg?KO2(sJcq3t_o9EjaBExXgB&48Pq-85`uN%BlAn~(zuAb6V)Xu@lxK-'
        b'E7Pbtl8^j2+0d?=Xe~aAX{KP<B+^b`(boMPPBFGrw5&4}Vui#Li`v9?boI*p7UbL{?pf5vhxhv}OD;`(Q9gy3IG)hNV~hwhvi~S!'
        b'LLav-3M0sgm|cX&2rP$*V*~2`sAE~`f*xPNq%-?yN)nI9yf#TvbA=k`J2F81@z9^ceMkOs=rMus$Pw_(d`Dh8^w>kbBON8%9^7z0'
        b'(MnHDzef&nn51cMZR2mw;XUM`2gb-1mL6e3VlWo(Apsre)IJMTNbYKtCNl9MlkV!@O+vua7$ujNZCc(ak)(l>%fs|vU!h#qlL7tH'
        b'SEv`Q?~j}p5nPG{-1_|XxTX1JEjNmV)|M(R-jQB^JKc35aBGc|g$|9U=O!x!t#qlV;GyO=T=NkYjh6IL5vIB5OvA>vb%#Hsq6#`{'
        b'*@ESI#Z6gv7A1(@{JEg!+tY%%Qq(7O@p@ae7BLo`(Qx3B1nZU#yd&M;zw;Gs-<#Lo^hmIM(w+9vXUUs8b}Zksh9KX@dSB8GzA4>*'
        b'pj*O9FlwXb0Onz<_C_YxJ#tt6J9{HzJ#6LP)&&24v}R{-D`D-1hgI;P*#i&1-y11H<93vd6k>@YzW}Y{5#ttiN!=gBiM*uK^7}K$'
        b'Z5S3KGM$$DJ21=PznDzRr>uewzb+%ru}q6r);8EgtO(0lO87s-N|qAjX^cDra3Dc*8q@p(iwg-s?pxhlk){okytt>5&^&-SjCYhB'
        b'ut=lr%Gj6}XE-}z8?5aLp)%ahEybUx;3cZ#W0m~U*m(@&yRIath<MSYkeY8bR;)CZEBIV-jYVD@y2jNJ8)Jdej6fNV2H8s(UZUl8'
        b'*{g1%JB(6H3h5B-i-hve{J2`aG8~lfpVV1CQs-ho>DQMM1WWmU^W!q4GMoz*{z<8aM(UdN-=c5&E&3kCY_T;B&)Ha8=$h_*u`vyM'
        b'6Zke%ur7h0XtOLNY<zbtn90Le-J<SDsHwq<N=7r_Alif#qHrH;q9k3y4+_s4%-LC>_~#7o7us;iADe7*G!iaP<Vc>jEG}2ZXs*^Q'
        b'$rpn!fy^m!hscHx+UC^bWEAw(h#(IzqG5*b2r%MM!U!!B6Gr#|C<XZdT##t)!p<BX0HsEDb@0#93!e>tA#M1AYgwCGEr$o{_Mg*$'
        b'DT7yd0nMz-fFR!bUBE4+y6d6{O+vs%>v-5iCE5586+%V_&~fMmt+j2qH4a1Wd`YQ587nCsXq8?mFL(Som%GKhRKN<b=a^w8bd7Fq'
        b'Y)K*r7$V<^iTHVr*&8?9Vs}T#zVVuI|3Y30!)AOx-v@W(Lu7{_V%HKejfpdBUQT=o9HwZS60c(j&AWlp<W{;~0M=$8UYagSh`VQ)'
        b'iiis#tP=y)2LhA=9{sTaYkB~q%F#0&uxbL703ONv0-C}A^$<L2VglCR1gPn#-1vZ|BJeOxGKMWqdW*`iRc&zU44aIGSE~(wRJ04-'
        b'Vy9u3IRZ)5LT_~%wlk5WsyB3n@d0J-MLQJ9mzd||a>uA`?Fi}6_Fu5jTPR=6xA7vo;ZK^45==#J%_rjL=z2p{j!(?%GS@X_Qbfi>'
        b'HJ4R}wT$6q#_$qj*q}CKGlmw%&~7nw+6}L(3@l^V!x;85hAzgilQF!(82-c<Uen-EPlw&$RMAevmK27EHL4lkhk7QUrk$A+ys|KX'
        b'j%JO$p<02OemOoOAzN*DSxvvBJ3&Ol<4b2(i!C&}#%3|F8X@L$#@c&BJwO<}rSC}jtD?pza-KxzxIC{=XJC!=pX3!LBh<{p`osLW'
        b'5}<(!Vg5!?{F<w3wJv%AL%(J*Y_=P=%?z;{99(n8stp|!-$-{vTa6?{7#&7~`|-|W59U&>iQ2^1xh~6S*yf|%#{R)Y`w8+<(O`wN'
        b'YH20Ok{F;d^s>;IfIAIunD=HPU%;>v5?wDrB4MO=It^Vi*)`dPZ;fJ1X8qQ<1+(tPjDI7lNu9psYNF7u#weL)7Y6lHt<@xEJT$PV'
        b'n;`F(0NW^W^x{`VD3Eto9~v0$ly<g5j_3-@p@F)6pC;zkjYCuFiNf}F!XGKArduSPD>_93=p<q^hE(m$UG?;F=i@$S*|Yeizu}(?'
        b'qE7d{-NREf1>9nzp~Gp|=A>WK#31`<lvb5nBeCkg5uS-rG1q7OA;z{SadNcZXK1l6ifT~`swa*IZtYd_6LT$#qN)|G7RAPa3TeZN'
        b'>O<FU!m4tMVOu?krpB;fe&enD8snlUqoTE1v2j&}(SN;?1ZLXlZBD~$C+g2NHI;!dD2?WKh$)GCt2H|7rT`MgGaw9*#9o<@f)bmp'
        b'YNSY(5S(f=9v)Z(@%E=;C*5&>6(xp<sPlEOC5S<83u2Jx@W5VRkhUd~@Ye+yWE~KXFi6NT$V&b+e_jaK#Ltr+`ZaV6$Ov!7VV1uU'
        b'K4nzQjTzfw>K9FVF#5!CLyNOAsy$v{Q6gFo#q$%j_R1&=M9&;=HiDhLZWC3N17kohP*&2Y9FICllviV{M0^20HXy#($eJr<m2-ep'
        b'kKr{?N&mb6hMl1|5B^qqp<=i~+E)Rej6y7W1#rbkyCI9uKX9n~LnFOSQxY(;Ce6KAH7E^vhISA7rBzFykncYRs+RcZjx$iM-)HD}'
        b'o;qW2L*k+C4_fXetlB^#0YS61UMz{D!ZnWuC@Xmv;<J&htPa5zwTPqJ?9d>b7&N_n5@IWm3{p~d34F7Fl%QF5fbokVEwrNy+-HNs'
        b'pBP9a?eNwnhZd%Z59sKY16xX*cMmX9XKyICrHn*+f-XFFmL7NJe@^Ysx^xOZc?ty4MQHK9|3K&Q1sE~Z_L}BCut%>&FDTh81^{XR'
        b'5bGb0S$ad6_lasID(32poS51Y<-^f0S_~~}V^q!rl3_R=ub9A3oTf5HG4v)C{l|e~X-3dmgZ-E{H(nr@F9)e`B?M3c1o-^|TyDS>'
        b'a8{kfnQ12GB!NO09Ys)MjfU4$hRuw@wUn4j%qPffAy6D6DBx(;(GDZsQZhtXRoH>ui=1Nsaj<U*acM+pm><ltvlMV>$O6)V;vSwB'
        b'zw`nAdC18R`i?-Ls}H1!OQY2EYh*9Rkv?tFW(hz5Q<k9cM`I(jtC*;o7oSThNC}O(y5^~v7Z(8wtiXb5W7G=82tla|eq!xy4peX)'
        b'xQeiV`l}YFlXGSMcI>B1+{&)`BghNL$|;YNeRA(2r(~2O>k{l1IUE^CoFU{=lzGt*p?MHHuyB#{uF>o&J4ROh0{xnRY9nSX`!Vg{'
        b'i+oS+B{8+5MC*)EB|jziAl28?h!L7iDHHsQF|Nc<%N-C!C?GOgh6r%34y?YD3<9(Mf*6O=11d45zNNoFi1?Ne$NzspM^X~f-(R8w'
        b'-~hdoumj73_;W2VjR5p9XnfEF_anKT;^angWSsna-+uu9lRyoT68_8R3jrB!S-~&hk5Kp}^wWr>Cz92M*ET3H|L;PQlFFzsil3xz'
        b'E+{AiLNbfJi6_)231ha7JPlEhk%p$%l3MX^2R<orh6B2QW`Z&o^jB@@)EQp)=VLl&DM)bMh|GZU6Zq%k$rF8kE}FbIfDVB5OP~(}'
        b'nx8G{kc@K7p8?>3=o18V39@W{5I)Ba8_^mT^nv`7F}t%A@^2i0f9WLtx%lMCzCHw9i@PENN^x2gW9U>FUbn_`jD4zPbNHxTyA8=o'
        b'W56Zm1Fn^?el8`GYvl`KR+lKVIYVbOMlFgRZL_i8Yvn;ZceORlMgSy$$IzWB`t=d3mmXmiBY);6%X5Wq^Q_wNTGnHa8tK<{bSM2$'
        b'cJgP_Gc}<{iPO9;K@Z<NjD|TbHr#su9KCOiitOb-dW`p|lkW7;uba=K#1nZ0TI1rQJCD<^cTqienLnD&okk$ij2Tg<#CO5Cu6t*?'
        b'igxE$gU6Wa6l5Klj=Wpi!EFC`h^8o#O4At}MuQ7{IRANoN4p-i)33J>V&FR1XAVSi&vZ2cp)xpgoC5Ry=@x_29t6=AN~KVQ3ORs|'
        b'+s69?0W?%Mv;80P<)Qgu6I%+A=leHe3b=0$W?F%cUCA7L?eW#}>9q_?$SdR)db4_3p%Fl^3+kM+!Q1m3#?3EqYXA&R{YgG}*7-bW'
        b'1!#hKE=hVs7(;K4BOX=Lo2jvr#F-Onq4R0<Fo*Wd7t80=7RZ-h^dTq5<wvryIGP&FPDG=Vn+dejPP@TH@-fN?sf=MW_|)(KRHy(y'
        b'2PU5&XAC<S`gIlEd4j;{GN|YE#J|a7lXM0Tc&`YuCqF!A96=U<|6J79+r{f4%2x_|H%>jaa=JPHF+jYxW$Lk(sguO$&~T2D{tPNy'
        b'ZCG!i-8$BgRW-dNlE_*-T}N*QbR;kKHcmZOH65)xvKYGUhJEHo5Rj=7HbHLwU62v&=HE`|F5EmV=_1f#;$)QN4Bc+0_gz>B&Rz6e'
        b'qZUGxZk=KGB=J<qQc;{JruUht$DW=l0j~m*_nH4~Iv2%sLlJ%F)!yGuJvNK0)I1k`I17qaHT9S_m{fq0^kP0kw+oFKIzy9+fA<st'
        b'8tGO8`<o;TV`wshw#&Xy`Eeba4)(KT1EJ!JRceexd{(QmXa;yYNieTs3ZF6TmOt!0QF~KG??!=2idSW5CnsU~<w%N;mW&hS7gG<E'
        b'wBXU%MrUSOp~>Pb&>0B3v&d9vnkxmR*jP9hzrjDsJ54A)5`bdlKV8xy16>vlg#tbn+G%3E5I>QTK^f;)<jq~w5@!S-%Rg|++M6=<'
        b'm})ALl=+_N!LvVQnHn#ML`|>HEAG92>aqKSpTjtDT?2}tF-NP_K)D)?*-zm?H6^Nx{*MFsPciiR)D}iXZ=N_IwC3GZMxv(MbDV_c'
        b'am-%~y_{S3_D!9^?Z>hF1*t8BCJT(ITcXl!|3`s7v@CPE%CJ6PwrD;7yX?%&<<MM>?-OcGYU1t_wU~;<<tbh@I|(d|@dHRsqwJ|p'
        b'1LI6hh&O+nUCl1=qjAcqeA6@!So2IZU6Ab^ERyCG4;M=d=6EGW-P=hz4VF6b1JsCpH`ND|RL*prGZh4qkuh%`3ewa-8Ka&C@#9Qh'
        b'iE5bZJJilpPj6`6{rThWXI4anOd%LedfxqvkEePoDOwFYV4OJ#w2E$*#{!@Cf?+dkK05(|Oowox7!=t^Z?7uW88(CG%Df(sD<Rs&'
        b'l2me)VF$&V&zr;}(~w*oAnv9lerAe%YgmMA4ymKJ8`+9^stkxtH-jgR`h&M1yx(r8H%F&sw5iw%JG4xLTN93{*+ozZGGB(xYJ<DV'
        b'C>*-SItGBYtLW|UF{#aD=f0c`Q^*&4jeZ<ld=1h?9a{lqkVJrZsE>+-s!-qxUECI|U~VYIOO42y&pR6?2m3j3OPq!7%4EE15#G2u'
        b'+7?}GF?5l@vJ^kE^=!aScd5ahf8}owkY-E=`&E{0X;{s{+hL?VU=90anif9rf3!oTNKG?8*rAr3B{a$4$CWs#(LPm4fa~!SeVrEP'
        b'u6yXXsT3P;`48Z}OYU&rf9$_M^e_AGK^^#c_gzV-=s%?sNslF`hxzwloQsfimaxjPZIer!;!$!mt8WnlF2PC884~+fW7v;z-~40T'
        b'-Gp@mb{qYl@_$C~2ke!^yt$+e;j-u~K_-E3R>JvaBdkS){VZ=4ul%3ktxAXa%Mc|kz|{x;RV8uN1qt!r`=c1oI{tr`4mIX~;1>EE'
        b'1|0gM{vzioBDEm77!~=*fc|s0<X{2xD@)u+4p4PMJd#7uCHd$03xfEsm>^KGu|LA!!|BLx{v{oUh}0kZoso+|E9BsuSb|aLIf9&w'
        b'9r)`aF8=0lLjfHMz@5%gsHk&PG#}!hOHO{+_l}l3A$e%&%{#)-AIG6FKOKi=+>S$UwS`|1iIVMTDDIbIQS#N%SX3d~0<oxgG%E8y'
        b'`A<So&61H&6lv%3J7c&oOtbjsV>s9Ro2n?x{{;3w7K<h&UG`W0Vhk6CS)aHSi;_R2gTOSYKTn6E@Fv8f5CmdBisgWgACZyzug7xW'
        b'OZgxE6|tyw5;q<|-3~;djs0vKT0Z^e58_bC9dYQ7k$>o4mcg%!Ln(nV=q6NzLffJU%~S%7Yu#z@(tgI?A&G!Or3Hx@v3Ju-ZVLkJ'
        b'T`;~3(z58by+EPbFW9>@0uY#2njW+lT!EjX1rRizB&MJtt7=U_HM^2xsx^g%->c<qatpi(>?p?CV*&4jM<BgxIq*u!ZTq1l7>G;~'
        b'e!+gk-$WA;PQUy|ebf)z&JV}$e%>~Y*mgi6Uf>t~vT=lrU>bwAm>a(1La_&(v{UYrdsxgoo}0ioxQw)`KgwDJ*3?PylQO{F2hYs4'
        b'l<%L7CJ7)vB{2UbgUbt!nQN(Fs({QR{+Yqmq+kaQ28aD_8C*d1=lLZYwYS!F|2y{9y5iT_TkF!GwVfzCc&D`m!}?=u>t7PIQ~ynS'
        b'Oa3p|TTS|}u(#lp-Dz)&{zZFx?MBev{?OW5$N#Ls`ll%Ux5xb`0Tt#Si~p<k_KO>wiL!nf_#d*j<OhLYVQ;Pf8Ndo>X6X!jAR;&9'
        b'Wg&Ys+P?h%o%S_&<Nv%r6UX^8k~{pFe>S$h<fq2gL2ZAjfeqY%28Nu8|9|^42XFkqpZV2v{6ydKzv$0&-}pb`&lF6M%NT;89YSLa'
        b'aNa_@!TSK0U<zqe7g*GVXsnZ)&ibC?!vqI^C}Fimr#8H1ht4!4t{SyW2inZUWh$5^r(~2U)7osxT;9LjLT@%{nq>=Rabdr)JDQ@}'
        b')JGOpFd{M+&AqE>rz95o=%jKyNgivVok=NKj4vtaVR^xvEG8E#SRmJLxWV`asIl?|&1LfCvNI8Yr0_hUDaO<XZ%!eYY)lP)Mj>|U'
        b'MarJ43g^0dT=iCx+VQbU{c&D`e>#St`F)4l(9UeZ)Q-z}S@O70ZkriYKUF+m(wmWatRzj6-Now>05G#UlN)zzclISk+nm{$#n3KO'
        b'3G8$i6<HmE>7T~bY)I;4e62ve9nZ_5NIQ#XZm6vbNkXG)EeSw|o!;r8-)KTxY?_Y9EdX<N1_!gtXlPf9@I~Q#G<Vw78=ZM9Jq^`s'
        b'4u2F4V7_sMdL?x?;eS6s-h<hXEVLV(4DD3Yd(Z%;Gf6%<A(kO9#Hh)LKbZ<VNhL2R$^vof)i=mcXcG?8MJI3}BX3y~Uwv>PH^k)J'
        b'wwN(&W*klGllT-t6r;=jnDH$Dh*lmHXbMd+soq+sMgvz)#&H?gl0Z{}OvY=Zk+TCurwXiN(D;eFU*^9=aC(Xx)h3Du`bveMY0)qS'
        b'jjOwsa+~lbg>b{zKsea%spNce60mPGV5L4uG;Nrp=IiW+9gUOG^zsfc>{M)KZm8Pek*&t;^bY$GBABdZS99sR^+h3edfOR#$Dr05'
        b'6LL0u3Q1$fY1Z>jsBbA|UyASRe%8IUPVRF~4lWIe>bD#Al|M(?>3xk+{-cD`@yQwJ8~&s|IP5gAfQIEH;iK7=?ls%GyQ5e1zWG>A'
        b'{GaSJ`>b0#et-6n5N$VP1Avgz=Zx*^3qmb_hHQ+|>?hQYPk;e=Xh{k*I`s!cHD4!N!H4orr?HxTxzk)9LPa*Lcy{;7E%oE!f6LiA'
        b'(HbC?1@nLfVS4*aL7<A?ld=TNzlE?kE}P6I1e5m2#sj-pkF!iozq}toQ#On&i-FS7+4bYqhL@^O5@%P3aA3JM{{y(LCpow;-3fPh'
        b'+<9~_GqBh~Z)?i^^{jMN1X)Qw_lvAt{Hs{$G5{;Bi@wK7dUK4Zslt0!Hbo;x>jQwDeWClP`k0Qr+V-uh??lOB=yuH~Ep#`?Lr>Tp'
        b'pB#sv>s6zF7?=UrRsWsv&}?q|nm@SrMrZHLer%BvC}y?oiz7QL_K6nng=||_-vjuJtR(smS1H108o~!enunN*locYRlSJj-x=+-A'
        b'ow8j=v(WOY7DqGng0_god*j>BT7+wgbq1Ck#(&8FIUN5VAXJXaNy#S7vpASoHCtX6OZZpdy^o|Gdn9#ahKxotBl^y}>FCFRaq%Hk'
        b'SVBeocxC(Iz0nM+;-`hIn29Q}MvPQ~R$<ZWkr84<+)M*O_ThGVJ43&0q}h!OTD?WTWTAHf0c4wuF}#HEuP_4sB6RH{0{xB&O=!_u'
        b'T{#^7H}PAb0d9;y5_>jGW!;T~Z*wSAw-~QpC{ZmGZ>^2ILpnp#NPR|)(eVjjTUEvQhM@vrKUARpkXTa*G@1t=P1{l*vT}EH%0$H*'
        b'{)xDnUcWV*@M|&p<fCff0iWYR_-!7D)<6SbtwIbf0n?2x0rS3XQcNZFRZklom&*($BS*iTZU<{GkC&Gf@Iko>7`f_w0veLcXJF{<'
        b'fQVctkB`h_;&&-G+Yv9?MDd%?TF5o%oO}+x@fLi)Ns$Whe}@_oZBo(ePkapCL7BW-9wX3*(Y-En$JOuAZr!^2dkjb+^$ANDPL~qm'
        b'Rc{SHKN57Wb3U58wM}T-6P>+=NmcwMeOyCI`e^Z6jbrFR;9n&a2aYA&uR`X(J)O{op?OIp$#!cFC{w#hJ#B0F)T)Jx_g1#sIn9i&'
        b's1MPOU)+AyDh{d)qUQ%|<`fA)j}hoW)|sWqvg|pTYHy6_Z1^MA`>-FhyZ^`DyT>(kWqso(C&@`jj+OvMAk^jrLI6P_s9eMr0uA70'
        b'3b6!n>I{i;^Q|-1dapiBq74CQi_uC#wGF`_P-&6Ys#s<MwW&HVBXp*<o!U{KVq2fKKegD}K1zOTpM;y@tuuWtpZEO-PEPh^t+m%}'
        b'pX~2CW&0Y8Q^wkzG#uHTI{7z4RtJt?wAGb*tgiS#$-|iuZ6NKkec6G{8ArI;wAC3!qpYroBGk<VqihZW4=i0&7~I-dj2jnX#A2)}'
        b'oga^W1A^Ge&qF^Awg9tQ>Y#x-Q0AkhUIY&d8Vq820Y(wQ<qNAm#xEH8pz*Y7qaRU+S@7-F^#>8^#VSyYRFlUm+L0{FbP(Rf#ZHLt'
        b'g(c|?!a3l_VV;d^S7}~cMZFN|BU)D$v<eKSoI{HiMja&=UxC;WK&UUyA8}?aBxhyuLKrT@r?3Q^S|Tw8Lyi_?>v6PAw4)V`b+l4n'
        b'<Y?84vp}A6{{RlHZLE)drxE#B--k;g-=uwPSx|HF37@jVZOF%tRzU}!Q2&$;iafWNw!RiE7h5jL`F&hYv2$0$#n|7+#lnT~qM6pN'
        b'xk<5-rJ&s^Y9Hi{umqgqU%}GJsW-IL8%cq3B#Sqf$ICS@%BdHuToGKo0NQwA3y(gSNpQV-W*9b{<GLayq5fpHxo)6(yUw$;FnZ1m'
        b'ojBbIGsVtyrpBi?_@}9;7Y+3J&q(g#P>+L33KU6b-^BHd&be8K`){z-QM2ew4x9psi{lr<*kJl%sWVpM3}IjJi!*Mc&vw4=TM)G2'
        b't)#sTTY^SQ=SQ|WSnlyqh0As0x~M~QMqJdP$e@jqNEim1UD$#fS0jQ>{>kGh`v=(SxiMg_axhnrjLr2VB$l>B2p9Xdg^7wq@npaS'
        b'DHrk?&X>4xKIXAiMH$0ThJoUOD1o(xEt5tJ<Ame?1NtKDbpy?moO%<j0S;@Rpxzi-gKWQ{HP|Mho$rX~Pag0854Jiv3?yGm!P<7#'
        b'&Fr<!^n@DuF}J>A4*d=h7W7^9Hyp&TmGS6|b)V`zH&B~Zn}?9L1z`N!Bo~Yb8Un+EpoZO3Kkz#R(!?l=fIuBWT=1XndJy?St(IXZ'
        b';wy@HH@U;}K#yn@?awwo1MV<}13M(ur}*~Y%*k?CannI?hpQ68-%0WVcX%+{5yNTNDuYSEzntuGopWQJz?(g(f?akfX<x$@o<|=}'
        b'o-lsmw%aqC<B)s~X{kd=ejq2{Y)DSDlrC)HYy*Yz*z9OQ6@AQBHw%!UwwqDtsFR%!kyHB>RI7@5JvDS;R31c5mF9Kf6|OM?qkli#'
        b'Z=hO3Sh{fM1;2-t18(GsT)rES*FBizxUj_&s$HHqGU9U_eXyQ<dEMtgT5O&U5(cDlAcGI_L`UgCQT$WEb7Wx$Km(H;k%7x48@Q1N'
        b'LC=U!-J=!Xc|s@sGh5hxRT+elOkhk-IlfLGG6TXfFeWyhe6Q$FZ1kqAiHPzx$^rL0VN!oG1-<YY(oxF*h5?KFkvkkwzvKPyvyCi_'
        b'K9}IAvcjznAAJYvBc~b^)aw#|V$*lxaF#fIheGqZaRQRdtLP`N1}#-n(uf=XW5D(GfSGy~K8lW%G~vo=SB=xJDyVwcDUyESEL{2Y'
        b'b>)uh66$sD`{HdWG)5=(U9tZ2l%aZ`8cbiCLKmw?g;MmNq3aKmu}#-17$!y)Ug0gc5ADPXv3%bF>B}sM4a*G0jgMo7#$V|k*PVJ!'
        b'u-J6U1b@yh62#7ME;hx=sqKpslTGr*9mzAQ7q-Pd5|@)l<-|MTR?{EhR=mA>XItuT<EpPxIc{fcLRzxv>?4AozN@aGa;#3cOm?45'
        b'64dS(0xy&PXWfG8oz5kA^};Qe2Al;9?a9<j3wLA(Z@X9~NNo)$pi~pF`7K!wfAmt&+|q7-_w*jTdqc{>9%iPL(Sx5<@-x7A<||8H'
        b'V$aP|iZJXnwTQ8PO6!s>m;NSLe8zc3@NrxZmt-q3Y<c(TI1ws0@JVs+lPOx)^-qdRiFML1a#yF!`!r{B+r}k1D(cj;aVztjr`8B^'
        b'@|`(LoH-fJ4+F4gGS*MyuRE15fUo90YD9qdA4~TBICp;MvXn)?a~?Bf{i;+jcmCpx?BAUKbI2D$^!}=>jfodYzl1PUWGa&9dC>%_'
        b'jbodw-;^?{R?hC(`VFH#>toP|e#UU^oa=6V1iIzGFzF4qw?=d)R-|JccrwK{mo5bJZ>%}I+!ZOG{zR3gq%BWr!l{|)PjN~kI~x)o'
        b'{oa|Vhz;BI33izMHNTOqx6SmtK;iE*P{EP*7F<6C&C$f}{t4CX(m#N{SI@nn{4<7LzB~baR57s>yX+-g{w`w`T)HHk0lB#;B{g!<'
        b'(gQguXYd|&3*m@nUkJusPHcUy;r$zLn{eU}*v8^j1eS84WHRn*$EL=kJsfr*BSqXN&Uuf1A6_Kg=S{3MSL?d*Hh9bfa2fs4@^~#1'
        b'Tepi4#c%qNz_I8<WYD@@jN15Bol_3XO3~UdiH5O(aRWc!DL#XDbxK;8W(}#$_0{G+APr+%I#C6dS1`N4w@n~$Rtjt;r(N*CSrY;c'
        b'zb0sHccQ<|PG_?~6Oz(wsx}!4h();-TNlUMfx8pAQ&MVbr;BzR2uf-3LCje@`=`LD4Z(4ZxoszJe7`NS*=qN}QogDQW}*-~HQvR;'
        b'4ovh2f+-DQHw1Gmx#kl$-mVCUAQHDm3MocP5>EYPHpxuFiS<~4a8Yjb>BaFN*YcMTm)DfQ<q?C8QS%a`GG1lF4qTtD$`z<`eO0*+'
        b'0JCssEWZ_<1-Xt%Y!k5RvuLa4%IxKNE+0%Q@LdHQs|AI5PAzbphstY|2v)9jqQ5k_e|erR&rmS1D3>G_$49@v?QtVI=fW_6ye(*b'
        b';lgZNP-FSExij#<XR{*(R(jrGG;au+S2_`94Nu0EN~}#Vk!<I`TwOg-(~c_@An*zNTKM#K0q%MjGYiPKH{iw;%<w37WKxsVI@6R}'
        b'xkV{NB{`bsXYaGHMDaR{nA{Jst%Ygr)E}FTD)pt=b4g2Qf+cGH2cHu13@#a;G=mIH$|!rB&dKE&VdR@hdrAMKw?LT3JUA4aZNU5}'
        b')-;n0mFEh;zvueOb02`ObIn{V`nv?{gK|)u*JihHBLzvL#AwivMGWA^Ebz61*pdX*@lG>{Egmj(&RT)3$%+12oe2LQuag(C5_47W'
        b'g(N42gPFIv8w2`Zb0==4DrYC*5d)se>`S*$d9%wrHMshnZiJgX=9YGPjQ3xNoy?wnD|YhH*(2D=^x5NJCs)k=Z^KSLHv8veC(~yC'
        b'KkVfH9_-{*`MqE#|3m)28#}ot`TuV0q+Nl2%lBd@i~L#kC=7uo-;>ji>i60;ZwO6TL}|CYh3jztME#HiyJeZxM?&q5ppQ^t)IgFP'
        b'ZtZ{#)Lv5rdfLsxs7sz^TxcedFeMs$n>_=zhOKYv>^6o}<qJC*NkkCm{6tA0QFESaj}YoVPoe>tc1aMCpk+%US?WG!8)Zk&oCk4X'
        b'FcT)Bt9nj^)Vs!0+w(N)0wXIreeKjst#9czT`ijL3!4??JA8DCoU(`5<$;7a)VJ82F0pWS^)cyL`8EGePkEf45@E11pnv-jN0x6N'
        b'wfj7^=L+>o7gg_>UHT1f*Szl9heq5q&_*Ld6`G7(Ql7?_lX&v%QIOCYiN+$)?DOCTXguh_QFzd|hw-2)s!4^;uGim;2Sq;=g*t^2'
        b'gad_rRn(X#-ae7&nYZeuXWnC<S=##zKIoa{ZxA3fCs*e|ghmw)0YZ)QZUTg=y?{{15FnJU^Ey5r^y8%4;XzYx!h?Rxr179{>*M7k'
        b'c+hW{cf*6KNARGooAIE^r2EB#KFD81S#HLI&PRC1!kh7q{f7I&gIfNJ@u2E)@t}@d@Sw)4_lF1l8_z4CQFzeX$Y<p!JSZ(0BJd_O'
        b's2rg|Ei}ZFV~Fsa5x5H;)B^}*YlpF;x5I-v#^6C6qw%1QUkDHS!oA@^3EsGPP}j|PPz)P|2z5ocRg~qOt@$H(GzpETqw%0m^x1R9'
        b'!-F~&{R}*)<-Y<CsvgFJIwYC~FQiC$3m(*h@SyRx!Gk{GJ?xM(&S8h_VLWKp&p5YYx$ko;%Eo&;w{jOu=o6#Qt>oMTCiD(6=uf-}'
        b'6MFaatCssZzxpr4gx-OTqUfK23AOweV?v)8eRd^h?AaBu`~J_aSpM~ASB5d6#?5!YgsO?phA^R)J77W=U@H3)UQB4tt(Z`$;P#l%'
        b'*+ZC6LUemf=uFIPf5LktIOkSOsFXh%6B;#y2^Efm36-E&dK*-zl6H4As&mBFe`#Fkk?CGs=&xtR6(x+ug)UDRiwiAD@Zv)MZF=wK'
        b'>E2(xmnMvh3;lJ%IJi*t_NNoPxX^lp3w<g9W$w4&LK`5J^WZ`sioF>Zss<XpxX^lp3)Log@KmF5p$-}s+Hf0OXwDd1=;PzyLLG|q'
        b'ydhlZd@nBa+APnRVRbDFq5MYSLJz_Y!4ZznR#1-H!9vX_*J*$_>ji}ZgY}T9fG*aX;l2kG+91(5XiR7Wa4<e5^zYN}hzVWf!Guab'
        b'Vs=iN-uvAw{rj;96Y4j;*KfK96Z+$<VNB>QFDBGK0bxS@5>%7}$l*WN$(i2UKWh{w^zGPTOz6c~UQFm$v&LXT_s8A?CiL>O-b>Sl'
        b'F`*yN8iNV_YFh6JdQ$ygXL&K9{nL7nd2an_)-Q+&t@mI;jUG&><4%~+MYm!?`yYXwRsGGF(0UIh)ab#4*58Z?eSKPQ%QPDFX_++|'
        b'6S_-5?V6j{*)XlQ!SnU=v+jxs#V~{l-IY)iitwNUIpvUrdQqXSUt`Kqs8DoLj)sLAQ*VKV?iwE!x)dY*#qrMQzm5Tg7J5LTznS&V'
        b'gF<1W_AkPOI!0ka9bQbR<93)(<q#&+aXU<?V=N}rF^may+=2;p+!hn+7>fyYj9@|?w_rjYV=$o#gbAh4Q9VqyS9&Wd)WraK8OMM^'
        b'KlFk^9bQnVV-zTqu#5tQs!4*_=>dgW@-N`T_@K~ngPjNOSG4=S@P6_4ox>Zw3H)vHzR`HO1xy+hsyuW%Oz3mNym&F8Ip6SH&y9x('
        b'-8(KOv<4d?{~j@+6<$oJ@iv&yJBZd{{27=~%e~`m?h_NL@nCIhZjW!h126p>el{=vb-2(cM&m+r#^6HxSNsfI=)KVYb8(@PTX3P4'
        b'JK{p0@Zu<PZpBeZ3x75)H1X%{M+t9*qTBSjR~*GH`_UmB1--uG;3)32AAM}_zHt<mUkFFx*^MH!)lSb^4(&!=2^e;l{b>5&{o^R^'
        b'cR%{i;3)2}7j+~I{@lIjJz_xq30$aUJY48)Hi5|H^+(-5F4Xc1<3b<z;zIK@K{LkSLJxXyp@_@3ZbF6DE2rMsdlZGxsL*;PHBKD8'
        b'JudV<d^-?vuei|qF}P4Qy%&SMX}uR0x+9+6vNUL^1}`qO-ir%`?5tq~7g|rU^-0kl45<pf7#|mk9Ii`#8{FER{H@QOaiMps2WPp@'
        b'dT_-0d%}eN?l#Z<T=)6x&+o3!{-i(Bn6<)R($^}J?*$VYH-cG<y%n>TcxN^oU(=YiX}_qi{bzBZck;JqZ^nh*>!ZtieFl3UxX`O|'
        b'mF6JAg<g>(e>7}g@jt`9KKSQwp_czHT<C4{ncLw)@08DU-S{7q&)f|cdZ&Em?Hm7l^O@%R!-dBGoM-EIvd4SEg+6Xj<lPk)s-|(F'
        b'j(fm`I_`uEtw*@f`XO9s{m;XN*8gl=Xg!S!eJifFH*yFUTCaa6?w`bk*3-Dqw?}ZH_4*T2$Hj%d6xaJ^B#jGwVfy&E(0U0~ub>X1'
        b'hnV#vxX}9hz=c90Q;%?=j$3h|^<#0NsM;Wn3#}i<g`#8!x{k($em4#-RE=<<4l^W1V{xJNqi~^)QMgd`FNO=X592}$IUZc-sk?$1'
        b'm&Dx-%t)Wn`8B61SlKZiE>t~)3oX7MTqu3?M$JKIS@w;K3tjf}aG_{iM-Dyi_M35`#+z`Vb5N3gS6Mpdd1blzuCnCclPn!dB+KPv'
        b'fuRmBFmyJ;n~aYOwGZP$6&w#PwBW9|&<nA5z=hg9xX?L3j!}6hT&Tl~3#}g)7y2FJX89-5@{b$Bg>D>$3ti9XJQ&e?Fv9x_*~{qH'
        b'5%nhzP#v-NfeWRTM~)^j29Cys?izy&?fIFwP`e|Vrk{b|iVK}#Jah{#G<ekN^hcnz{f==*WT-xN1a|eNGJ*lVc$XI%`b_M&&`=Hy'
        b'4fVVnfJVRAJ;>00ilgSO9fb_tbz5YpR(mI8C~I4Ukr>8>+P%2Y5RN)(<q$4(*IjU-UI7Gh)ECFag=WOw1s942=nvqie;S1g1^2%X'
        b'7)H=ggbw=~j-a90!_d&=QP9x(5oqWr{Gtb1WcT1g9{_%q-Zw6E*zTl!WOwSH?urZbiM<0Z)MIr;1V_Dm@fcia{k`Hs-@b2LsNIVT'
        b'9VFDj3rFEX>;D;CsC^h0`XixkUhp$<p~HSwdX>h724~+97uq)c4!BUySdL4Cx;^7waG~`hxX@kqgbM{#6vbP)a?J~%iU@Nz^3D#!'
        b'u;Con6@5vlYg0zyLhDE2LU#?}LLa?7E>!U$j(neYbnGTQcAN)!kAn@}H5wcG{J7XqkA#Xo1N!cQ4P7+-_Sn$1qp+cN$H#>F<QQz|'
        b'@9uyNUEsln)@KJ*_<-sHS4fy2<3r$34~Ip6CDfI71Ba?SegB4!!H3#Cu*Xw`dgBN_G)UGPC>z0tGNzA*53Rp9d?=j`odo*s4Ik>2'
        b'`1?T5xcJb)Y4?E-t-l*S6!}U&Ep^D_EN_B{a%qUD7i&C9SdI?j-Y}wVT%+t3jA-&W7}4<@h4c`ip6dmOCg+WV4{e_&3p;oVKJ<)x'
        b'wDLPo=p1c?@TaTF;30fy!`Gq1_|Uq6F%k0Qd;M<^2p{?YLWeeZ(4osU`t)fYa47N80K$fLYw4kkJ~zjU{e&=i(8Yu{4OQs9LLIn%'
        b'#xxouddpe$m}&G`^~cdc^8@{w2{hdJbxEKXM!I8%S@SymoAoFlsimY5SDqO#e&zv^T4*4t@u90O@l~`xa|}UAjm6iEMlX~UVL`JQ'
        b'1p=)G*YnYwrx{-gu2CI$57U9&7=HI4j$TRpF?#)9uF?=1q|&4qG)V@34(Vga%`|N>Yr+kh2vfaQGsmEbGT3y%i|p?$GH4_QjdYdf'
        b'VLy%7PZOqRqw)Kwl=IY_E7ZenHeC-Z_$Vs=c6|YF*F_9&wBW%<i_ZSA>55IULn2Vl=a%DKkcmzrmMkRf)T|hm{;L=da1!Ar|ADS;'
        b'bH&0+%n(JWBe0@tKj{A+Q@(?p7(gIQ<Hz)M7}}ufKZ0vU;tXI!mldkh4J3S-p7|x0v{c{(dbTbrjXeCpZocB(j7$-F74x6b*d#0a'
        b'1BE|fc;oN73}3}U0zUg^rDrqI+n`N4`jyOzP?mZb12wYippn6jl?QNQ-xRmtjwi067dNM}s{Tsik)aU_#p1%qr7p<#CZA_yEzAzh'
        b'N+)sIPCpMt>q>p*<DR!XZ@S`n&+`&ID?LI%l9_g#co^enoZTttdpDpqX4QKEwKXQZ(MM#`E$=E%Uhxg*25Fiw?~JZ>pzx?cr@MOc'
        b'Xral_YP;HOYMj{GI$*O6{Pa`n8_sJJb<V4oTCW24x@}HdYh1fYcPS3O#Y_TQqqu3}yl+2hJ81H$%0fqZ_!;IC*J~2k*^i=}!Q>-6'
        b'KB&Cz#xP(m$0077%h(l6XkCo9_X6ba29TtMf0|is8#tvKIN7XgcAh$QwOV)el*wtUj;l54oI}%?#1;H`@$-%*wDp_~6GX`p@v5ct'
        b'!6BGW(sf;i=0oe1hzs9E^Ysuhqz4zv*q~3;Z^q>sVPZ|$x$LxpTnQEV=?5V^{b4BrvetCh_P!U>!)vo$B>sRU1t&!%@sg4gYYsDa'
        b'Z!7gD{V`!G7GGB;N}9TIpSb@DmRLg)Wy}xzG15N?r~0Hh65q&N7lt9MW@0Y&P*kkKSGF@kK}Aq)F{Npdth56$OPH}4zJ(d$?f~Kn'
        b'PJE9Zd{7NB1}e%(Vp(a6ay!k^-tE#B7JB&Mr_%WA*C93f^rVW4(CmpJ{h(zeyX-)Bpz<P4y%H12Rep)1JkhU@^1sr_@;xU8+KTcR'
        b'O?9zhj@^B6J7dh0zviWw>UiJ6g<|=BMzVxtDkwj>CeY=JWeFk}(QL@^_R8lfO4CvuPAoVTYpBa~1f-@G+PnO)fK)8K4&$X3+P2&F'
        b'iuF4XHF1U*GH?N}eIXyrGqAH*+WTw_qF6skhK{gpj_KVTqxYw;H^uaBiqTI**XTv(OZfUn(FmREV|v%e=y|fClWC|o+taG`*JAx_'
        b'y3u3O-p8a(nw*2;RG4}Oy7yr%qfz6z>|vc@>*LW?)m)2)Z?$U3fJK^+r3%gD{P<~cnwV3M3g*Ulg<^f73_Io5M)~VQ=^;*H{5+B<'
        b'&}cQ2m0(LG*Pxl4C=iD_`DT)7?M>=TXyVaFsYq5*XLj!*%`P^hw3p;AE-vd;X#@t1uZx9QIwLeBOKf$DV+*aFa*eM-BUp5fG?V`M'
        b'@-+=bgzCNP1?Na+>ACP(zq+6dB)Jur!^7h?T_J-a^^s3mFNc8WgsvcL(Yf$Pg`}|Ta(G_UrfZ~6g}&mc5Q!PS^TSBL$jc`Eg}@Xt'
        b'$f~zK72^Z9i3u3^0=S)}A^j>dL_4$L8*$`92%>QR+@f=v29hpk>$71Hl}3nOL|>{edn$%lR0FPO5}5&aL`RQIx|AW%9t$`;sif^v'
        b'3rE_4H67^wsdp06{krBlc8oqV0wfhtV>)1YssblJC;e*PLYQ=Mysz-P_y|pd-%7D~#wod=R6}uMk|l*RD0EJhlw>Y_gkr~lxQ`o7'
        b'n?dBUu`~1>B=x4WBe|p;wziz5la3Rog|MQquKLPwge8|O;4R_D#!=gfjTol68m-=PqcQDpF1^A(px^mi0pLG0q(m6V)}<Dv=FB)%'
        b'B*^_L8s=G^cbt8C63mpELFw0qduPi1JenlX2`<hu-{b5)DMQl5(ElEN8@p7TnnrEQQ_mQzQrb1FHVxZMO%|51Xybb`toLMe3ky+Z'
        b'LGyli5l?(-|Bh1q1tCtn2qbhihxPtB8mX)NxLdz?Xg-l7OK+s#vzn;MdJ3F>73zIF?R2g_7q#i!6V}@qt)GvsDQEOIympEBidY@S'
        b'?%WmD+W~yA+9>vUjYy&i(PxCy=QBlT@Scfw&4X>4VEx8u`g!GpW-1uIXb8p$B_l3f+A}e>FSdo-;iF%H8te*wj3@>#7<Nh}pz5M6'
        b'mlsQp<EQ<ER<dq$*nuaaVf-sFetooO{3}#Q&%{gr5bGn*grx`Unt<gQZJJ36P0-=o#x#kGp)c_K#`>UsQMA`k8`FSLy(rv6PZt$n'
        b'I3C+aO)@Akw1oP3G#%|v)@i~HtdFMG&lk0YhR{l%PJexJik1qJ?ZREjSZ97%??zxhppBZe0@o9?tW;sWYodV~poR7ej3Fs2KX!LK'
        b'pud59^`Zlw26Lr|R{eA|@Cu%O+6bM8bG5Em{bky*r)eL>V3G3j%^Cy6?@S8o4f0N!8llsFAsy98|4=l2ZW>qSda16P7It7lbP8Ml'
        b'*_d{|G%s^8r4JUv;w!W)EMIt)Sk1uDx1Cg2Z$`AfPwJ)I^*1-<Y<_aeKQb*T7fknjA_E=z%))jt{is>dr)CI}CFq#Ab-RQTg3amq'
        b'Wgn`r!btJ1E-djtR@(BVi*n1-lsqi)DfO1vPM@&e>A(T^@OJ$X>5!(;%x66{hxK9eG}j-n<NDLvy;c^EzR_Qp>Jd^u`j5U9h3cD!'
        b'c!HJ?azJ8x(H%uP1fztVzeV5ZUzK{>(@Xr(RQkwoIJ!YE&tK3Db?pMq1wYpeM(KgfU4j%gY=)E=g3TssQeIMGBO>}t#ll2+stimS'
        b'3HH+YQE2Z^Q|I7%6Ply*gV5f-P)Ns62slCyTlt;qA%^L)@Hk;PcOg<Fp#rP4lD+X!@nCHcf|RA`H7JyCM5l`nl2K8<{PavIk@~0;'
        b'JT&CBz6MHAc+7dyq|o>pGy;;9_*6vahv^uNxHnUzikc8>)g|YVq85&|v!K^egU#Wg{E8kk@v`{0apFAZhwp*=FZ^v>AzV&km^uqp'
        b'={Y7R?A<Fmb0p5PUNhw@%x0;m2liiW2oQHLdsr=;qJ7x$x(=Q#8HHoVPV8{q5?%|(@q4VG4#-M%Id^;B%iKjla?e8{doLIoWF8E-'
        b'mc9taC0M{~2n^`p^>Cq|9kZNUz$4igB4+~QrRU%(Jk*p%vhyt=n%z?^xi!WB4Kt#Kn7F93v{#fTDlX`RU}a;#IApLef>D|=yBHxR'
        b'mo*Bb3CCv4*5I`CHaFR98N1t~30twVLH$683+|S7HcOg|%Q}rLEL<7TLYO-3CqtS|mfng^n?%<PyQm4Joee_%;kq6IkzJ29)tP!5'
        b'0w;8^bjRu3!;TVa<WnP=jdiJSiThu}KHP|xY7W=&i^&P({uWM|M!FO;=`EL=>MEY9I?}=P-0s(a^bHh8d)!@ED*o_8mgQVSQr4%Z'
        b'J6LD9<P-4yZ^6lQ@EYs-8$ba?NPZ-14hUYj=}L|yHc}ID04;lxW)91wDLs%fNn{d*gBn(7NH$@_ESI}Clpa{(qeMS=Huz0|EL7Zu'
        b'D3+pCkF6IA^O$X+3<!twu^3)=d#`FLghTs9<?KONr%+bgyJS~4ezsfir)GUnD9Y_aI&fI&9azMHMF&csGNmog6G?PBRzYv1ehIUp'
        b'a}Lj<Z>-~6J6P5<X{Ot7GPdcd#<~u+LGz%a77Ve6*#Vm3*aNdQCR;9pKkaUY@9};M@~wM#Xmn_6)&v7ZhtGlYkI+}YCO+H=-?lc3'
        b'yK7UdHGvBng!!%s*siy+#&d@|3zv&qi^X4m-w>n#wd%4l=n<q9SO*KV3rK~o7lK(|Cv!@vlwBo(50pM-aK*t+ry(c^K3jOEw3J=i'
        b'EKC`TAmNrYLpEkiz|0g^d%_JqzO=VS_|)M#v|K0yR>In&>kf7cC*dWZ{ztJTJg^@YR`e*!@okI6o`o&S00EoyB2$Il*zU&c6c5xw'
        b'Itw=Gd=QE#97e9zIxSDtH258^JHtj@q-ikr3LJLw7|Hgq0y6?HMVo+^raFhw!%Fbi7dc-}0>5ZEP-68f)rgAAG$}%DHs<odQY^^v'
        b'5PYqfz{-Qph$>(nf`z5{K$1}yF4lIr4Fpyb_#Ik>{+ZbBrB%-*Od=37(wSHX6P9KMI=`Q!@mQ!M9;PIa--wVaFi~QXkDQ9yA0Nqd'
        b'aj>*Eqf}H>_5rFbs%nype}iCRRBMzLa`gjMLV|N6;s9M+sRi$UpObqyas@My-9vQ0Nq;7BLI~3CR*{%64_o!#yXwjAlursbIrs4P'
        b'y_BH*-rd9LAgm1iOr&!b#@E4%m>cu#Y^<g>P~(Vf!A*ons@vk!87RXttiOwc_FD7e8=30G*NHFO^t?TudfY$IZ(@giFSR#{{%^tc'
        b'_NeMN;&c^ll@&T&oXzB{n-gU_Y-qJQca>pvyQ5Ho+-$9TIjY%IH$Cdyo+w+B-S%3Vvt3|2>TC)fE{9{YI_o0nFCFO1CV$&&&a?Dw'
        b'D|35f)a=IU+BVxC<7#WG%@hoN>WHBFW#<87RCTkn^{~BZY3pCo4s4C8+ZxsSj-m2sYhRkJ#eQ}VnyS6Ix+YDpqg(Dw(^>7kaJ@6F'
        b'y4G3uOq8v{u4{7I>e4Ek^&6sWjcK|Hd$l?3tktf2F|FMMJ*!R5Q?-I->nSVzIeSFVZiPE%zZ6t{JN4UBpV?0xN;~y3+;sjZ_{n<t'
        b'#n7qNOIEw+G>mb@@niKKCmHj_9~qlgw4XWqj^O0cvwwm=&ZC0nqh!e2F$|JCd9<r8uKXR2{q;XLn+O4Ba|V36yYm&P^Q7I`pLX`o'
        b'f{Wc}zeaz$1>}_XYai;g&|iHq>MLirz}f61r;w!W>m7#UvoD$|o;Eb@tUO9`k1YH+-5Ou9C5Gv(>twK9s+4%IsYjyVV+2m$K%Zxi'
        b'{hVd~`f<C>SI>~39K_uHQxC5<KB_K0s?Aoce+-4&?BMLEY@T8{Gs|q6QT3(Cd^TNRN}QY3$ojP1$i<>V$a#>-Mns|hGqTKCGt_%;'
        b'kUS#~i{M4F=%>J>2=h<H=GFcB7%&KJA4F}1wKtMrWY~?&jZ7YX{)6brK=hoUM(BAUs_p@xr&2$4gr4l=s_!DqS^j6Y3bN#t84;{V'
        b'W)jQGb7?vm-1crjVe`VZm7ylSu6iKVik?<1wx*g4)j3xen{+u>tE<stf?87rf8J5yd#tR`%<!bc{w=uZsN-Ar0v<i_KxEzJ$Tr(S'
        b'{RBF<N&nNE9@lO^N$S6iM0L^7yD10Ub6E4j&q@SQp#^@TV(n5ES_xDm?Ly?Xm%wPMUyal0DNrbqPX^KX|0SzHbhJG32e7s;-1Jl*'
        b'N7j7^Q~g<gB@D(bTMT=>x#X_QhKS`)ui(s$H`sW61lGgt;Pv&KYQZZQqT-^<ZWAM6*BA0**OC)l81`EH0%8S=+^1w?sYYkzmOda4'
        b'weH~njo-RO#rfeEM&!J`GfZp{!(Oe%#0EJ?Y`)u%M#8nEi>osUwjc3avz%}Z34@6>RdUuO*kyrDnC=C3w2v-wi${M<cnhwp4%__|'
        b'iOWtuK}ObaeRTS?3LfdF^v84txQg*{`NEvK)`1wG?%A*mA<$v9x&Wi6O4C)(ps!iFt#BPcU*ph`^CbZTi6m876+BdvDB4r=2y!so'
        b'@mG(`sv_$uBHQXx^$sL6GB9az#ax<0kbP<TqKy0oVhM8&E9X)1`t;HaQ|R*i!~Xe=4AIdRyy%o?h-V_}Hoy=|^gGcI=92+u4+`3k'
        b'#Q2b0ls8o1^CXAl*Cg)-oLwhS91DQdXrp2IvPedSpp0@!A$JVGglg6`Mvo6j^2-NKlV^1Ug(kzPl>=wbUM>9Au+bD{I(6#mC!gug'
        b'UcGqcMBFJcdM1XQ5$K*5pN^a7u9#pF%<C?H<Xy>=SXTf;NU|b)4DSYP_8})|1F<WU8O~yZSUm7k@h2Z*D+J$g#Npz|iIPBub_(v4'
        b'7+~b(l2XAZl6j_i>%^z7mL#5t<jl*MXEjmfZ{fsgH<BAauVE6W?N8Su_(F-hz$>3LEHx)!cac6VlAnj_%q%+2M(LH<E|zw?=kQV$'
        b'l<*j5k@@RKLwNe6NZJzBJO;=sI<hVX<n_8f3(2b>xFD*4SCCw4UKHNl-)4s`ZGXSJDV!vh@XB~3LFcXz?K#UPLB7idv0rd+=5;V('
        b'o}y0o$^^8>-aVs{t!}>2!|p)ef9`H#m+_2O+_W=;bxh5pdRSTMhyCY1Dq39{N}%Twmx=}J!ohY<F#6wgui(L|k=z!a4(@SA`L4;m'
        b'oX9#>WT8vkR`;>~Aw=a7p2#$>IX~k2*1Uy?S?i*7kTG02TQe3f+W%TK+1l+Sd8fIUC>1+XXKN8R`80CpnJ_ZdX4^i`nxFXZO+Hl@'
        b'r>=&OnFaT=ebBuD{<;=?gR+C^c*`9_(7I_-Skl4Dzb-v%6-c_!)5=<VZM^;Db@{v35A!U{8WC^PwVK&nG7!D|Z=d{gR3#DmL1w{}'
        b'UUx6yefmiU57fKC-Cf)Jw+NJ0${}YV{UYZUEH*|XPb%EC5nI9{i3Q9#?85=5`d2+Da_>pHacZ3_LVq5`|1UF+r}w=ZfK+x+01m4x'
        b'`KN)CJrWQU)52Obp}KV-M>mjsRCm;wlY<_gw#LT6UM1P2i;Zh-MSii>B%Wsm^*=K&BgW_bIVT7%W@63D(1{0<CF0mPuwuF~=q5B4'
        b'o5U3$lNg^LW_%2p5dT~Hyqa*K`zw#S(a+HP!(vUoag`Ctra9aTfdM*Qp>AuO#O7ZvnXvs26vj=hjy(W54uKhte;sl$Zcl{S#wd^C'
        b'Zuh6ZtKJ^tL(6KtLfeI`apPLm``5GB(Rd3>`lj0^aYiypdt6b(KFL(F&DQ3`_^GMl?XhO$;_}~SuX_KQM26W<PC^eZ_twF;V)1sR'
        b'03*r#w^^$9uN`OGPhO4PDSn=OXL&SkTjj(!sZQ~B)cUPD@li4Ls|fMS-m&EGU6+Jn=&Sv8&<q9=SBhP3cMNxqk2ilKMMag6MSaS%'
        b'ofP+KBkBqx+Uj}wXVB8bB}e4M`{q3E=$?tTkeGg1gf3p3#CT`xyt-^bf3rJFu)Eg8u*DXlpqW^g8ZX9psXE>EBvl0iq?@fuWRMYL'
        b'Ky22IByF~04$H;FS{Oz9+=&ePNpX^j^iNXko+N**CpoV<FJ)l?VXJpGaX_w$*Zw@W8DjTbMHA7O(Hbvsyy~{aJCisx&GQbl;L?lk'
        b'70d;^Is6u43BQ9O{mQ)=H)WP8*E0%D&Qj0`RN`;B3GMb90y$0-BY6=de(+!ScPG8a7e>$pLg(;3J|<*+-PDK!ScEKMqMj3R3Ib#V'
        b'sy+q#{Z45_FA*W>a_e`XIIr#-^!B24g}+7j9Mza1GC{~Og9<kbDh<s|AgwIWvTX3l`;rDo7T6HFE|*^$>Syi>h)~2nN0m!LWsQ>9'
        b'*o@upo{bPhMK<CXGt~yG2?CYZk$wra4<XO^JdVn~RX{*C9KRmH?Os)$bd|)>H>jc}iZx^lPTi25V0G@4#TtA&n0uJz(J8j$;&-0x'
        b'j0<~z%jC`hS?~8Uy%zD%YVei3ak3SZWEm#ekAreYnW#&$<1De&mnxT4R#mXXN5mdBXXzORI}5DWkV{B3m_)-;Xe264s8$oUN+Z>O'
        b'j-GJq&&wn>Tg7&gThVLK_-(po$mJMpI&=g?6a{~RNs~bn(j;ig)hEd4-@AgnPwSW+jG_vh&f)2KT9`0R5<{+GjZE<;dWsV=Ihx|U'
        b'O-FLkNc2n>&uzMv+)MtYht<Jo!C}_(8d0An_=+Y(x)t}@vj*!-q&73j$`u^gHHpek9%<uao4K~5zUrfc(I2g|^2`vBMN^Gvml1tv'
        b'os|Wjry8I9zT~-wQizfu9D=8oi><Q#V`Z`L6XolKxG@wna~UD*sisYXIlntkl4XpX!LAlEWEVNP@5Cwcm5=@~sqe%eKbl4Koj8GN'
        b'LG_(@^`lvFeJ7goTc+;%nz8Q@k?mC{NmjqVrRvEq8C`F<Kbpq3ISf6V<`%G;P1k_{k;(YAyO<=SLzD0pviq;}@hss~%w{Xxy}F9z'
        b'Cnh0dQor{D>2RHKs~`P=e9rZE_ejokh7B@7C(|#vNBr99aJoM38CDMyvaFH&eIxg!-wfUV*VSh{7k+Df#xvm~^%?&jK2Ckc$7KI)'
        b'^%>)2KfgX>sO<mMXZ+t&pRqmsUg|TphX3!b&-iTk|Bdw-HP~iWR#??rS)6PJ$;uY2U=eKegW_amGM2^2f;(A^(tvFl*$m-@K}%@O'
        b'+qg0ev-=Z@y}Haw1mw3YT*N$_-ukHXQh}g0FXvVE;sVjmoLp+TwL0(Veaqv}CO~gSyY22^<3#LmdJn6K()%N2fnnNSd$zUNx6P(&'
        b'Z5G=X5*A9y#n84w{{rf<hxcjJ;dJ=40evEmW#i~<J%(A+3l`3`rsg@V%!1H8M9tfbJ;Y%_BeTcHO6em|?6y!@q174A?9eP`?anNj'
        b'm07seSs_y&zM?$tmiQC%S*i5F5MWdmIhj5+fqXezu6fx&y)4n}mIM+CO|43^Q>%Gtm1dW`(|4UVDkAG^m7Ur>pRfOolrACpa+6O}'
        b'c6YOZ+D&#va>3aD!jV%i&&MMdYU`?1bOFcUViHfDxoJS_S~jYDW3@t)A<=A?qauzr395r*M{kVMys`w>YW7N~S`-sR5;=}lrOV&_'
        b'yE@cuplWq;r!dr0uhEh`wq9crI*YCyK8tP{Rj&~pj@#Wvy<Bw8T@|dX=P2qv_Z~>J7^qj0A?0`lrs?)K?&6>$a3A9&vC2M!<Z9EC'
        b'H(ED+uhm#ZiaBh9X3q+)K~rPayy~f+yh>9`5(=tTwAG-gRj{ygZ%RoYvNn2tbc>7rde5q3XP<a&-BDawPN3}m-_~<%98BLNHE3+c'
        b'P&N=H{a}!;-B_>REv0{Mw8PE*Ubu;yDZ5=$C;a$FVe^j)9wyBAQLz^@9>RuB`X{SpsC;7vMg|aVun@Imjll;~96yzL2v@G;h_XrE'
        b'9?sc~g64h0r3qP>C}Y*}Q|pd=5uLd%5O@8>Tf6Z$oK@6zRGN@~s#$=rYp>DA(mH)t*<&|u`i4aKA?npGd+G*M8xQZ-xf^+V*mlhx'
        b'&=1#x*r{|uABb~-D+oK^>8tt-w@dv({&QYsNO|VeS)#YvG}{eDe&sSkB^98cwok^2&RkXGr=oVQqIR9i5Nym-y?1>P`wEQlm`by!'
        b'fQ4$*p&o37Q~;tz9WoR}ehO-*irTd}LvieS7UY(D6x5z2J|7<YA~m%TK9L#9l}I?zhmd$Ol3f-zh8AZvtjtFNY_rCy%s^tIOE@Ai'
        b'9l?!J96MDzb?(h29Fd$xm2f1U^U5jU{^V5jJ5<M!)xvg#49mzkB%?Nv5nbjoGkT`zSeItIxyY|3Vn{}wI+wJJ477|Yk&H|p8C9@o'
        b'-KINuMTFYlBq9@Q(?Dw0LWRb<ga?{R<hk1@>)CmN_KZs~9N3Okfr>f8SB7H{N6xLH_83)eg-vIig0)e#n|;of3pTD-96NOhG<P+U'
        b'B=o6O@X?oakI&u@zzL;0nz^nXC;m+E6G)+JHZoF$t#lRSLp3~vEUH!5F(ZM^M~iAk-#xj?2fpJV#0`pTAuKahlZpUdHOgprG|K>='
        b'P#wn_SA-j+{m$BT^%G9TBY<UclAMWZ-XT1MJ$CNgKKl$1_2^n2sH9Xrs(BZ~1|~$(bq*eMg@sC<4Y~>Ir1%uqhWUkDo2L%hvMyql'
        b'sNA60u3F}oA4<r>Xt|fr7`0`7a%!i7+J#muUjFX&Eas^MLGqkzW~vACih8i22MB&_2f8&-2}`W_j3Lj^ku3RVxFS8-SOrn5CWPf-'
        b'4LDX%+w;G|m2&Kzw=?T~fl36FN-kxt_or)^wt0A*=jCw}h7@mM_Gh_EdFz9L$q#_ZOqxkxE;&URf&t0$Gq@_$Z<Fzvyuv&L9$gb+'
        b'%#27vPHOwArGD$e33({ZYkoK@`Z?87M7oOBvBg0BHADhB^Zlzb)`kG(QRK%^CpL5fc2S?Lilw92r8_7O&=r7dGD|n_Co=2Fp#^j4'
        b'JWvsOz38$w-|&=rnrL!pWr#YAwjuea_^MDpy5_)hnT<HH1EWdSF7+#sa$t53hEU3ie)MLVuLIMi%()AQ=MW7gU*g7T*gNXX5xvpw'
        b'z>KB0*Bc~LN4#5GixIyaOPexy9NIu{h6x*z<@j`!GHIJHW9f=RT_qUZ!z)PCA!CdnuOljd<B?;{mvotswWE2sv+g4viezr>u<mEx'
        b'to#2g4~2zD_wU97EE4b<Jxn{OQu4#4OfY`ziih^cKo9=GfcqXE=n^()0YsqGF>GRlb_H~u0shic1#cAX@%Ku*f!2$xGUP9B)uWq8'
        b'FJ%@!8@Ee_DVx}Zg@t4Q$t;|)W97<1kbdksXY}77Eigv0(CQ%D{SsHkVeb@=()C29@-DuqXo5SDw}P#F2=bbuOvl8b^+{wJy?Q2r'
        b'HIn#wFt?czGig3mT0a_dD;R~j^^;IL<+OkD!e~#038G?>aBmF}KN>D97=a6W+j|>Js8=GH3vluDxJZBH!SU>t*m|qo!aYRwux%JC'
        b'#-SPPwgwv^n*&sg#{P~^H&HQUx3Ob&9t6Y1?&9yS4gOD&sbrz24wc7#2@fyi7+&tcinvW&^dJ9ocuA-0P<i#6wnSRLwH^kP-m0Y@'
        b'K3bR_BQE;KE%bv0CMSC7_tX*{MSuL==(mrdKZ>URPI@(3zn2ioZ?FIBVy>fi&=Yf&eZO$bCED*T<`S*r$6R8(n5(-f=Gw-Ox#s(i'
        b'xm#}+bNw-6$z9^rJA>L_jQGtj6LSj-2VBK>jaNYBk`bG|nFoluv+m4;v~>_-E)nxf@vz!8^B!WZF?!fmy#W_2<u37d@8ExTyd^nc'
        b'l=9cyu~uKm{z;ZG2S*vddL7M(*Ep5jI~%6dGQ!8Y5wiq7K!%Dlqx1clcgy$Bd-MHLI^Tb|jOp>0cTV?9nR2Rz3`>m{1N$j#xu#}&'
        b'D<waTtI`uyw)G@Om7at^(?Pfb@s>HlTjCvfYhfbpiYmdOj#;Boyn)LZwMH}Vb&V34w5Lh(>>=->T8T`gME}4^wkji8L0Q9D5B9J~'
        b'ehX9orI-fzWY*%w0z9_aX@~7~K91gyww$6LWLQZSu@E260TbYW8#3!380~;j9l$&L-wj^>>)LzI{x{)g`Cns|$NLWJ?rr?9(Qq68'
        b'tN+=19^=1q&*OjBJx|dx+W+3~o`>y`<vJ-_WedBb|5Ya4ga3s@Y1scxzt#UH+{OPcqW$l*U(EmB)1HUqkO2h6xL+S!G@tfe#{bWK'
        b'S06m{zI`z9iTkeh4K$vDR@=9T%?K)9W1tPx1v{Hv<@FOs8>owRRa$%O^8e%Ep^P!gS#{u!N4)lFMEOzq&GxA}gUhAJKI04HeM5fS'
        b'_H>A`JTgIKF@t>;(e~+i?v)UZYEu;r@njlfpOr6^aW@1i+cCNe2fBD_V2$ZB+(Fq&*R-z5ECc&2A91^Mel*03mkUBi6HN{ijq;-r'
        b'ANwO(gYqWa2>B5r`HuGKq51lGv<{Uo5U7w$P03dt`z)t*n<fJ^Us-ZznHEJM`*bb2iMHTzXp5XRLfCEW(=?>pUP*#|61P5+7-3|w'
        b'*FIfKJaVl0%99_B=7EVRXWf|x=@ew2uIT&Z;Wj#cD-WxQS$E}uiROQ&*rNkrk;#wHX@$W<cPUVOn(+<yru4|qW13U2VRiOA(F*ds'
        b'kYzO8Gw+q|Hd-gPm2q9ev3L9qi-!`Vm9xaVKY;v#vosLMg{%S=B83g9g(5wP42`89n<_j>REDntu5G9!lFEkBO|7c*<Zz#G6*BA^'
        b'`5Vv1ntUM;!<b|s=@V<&Q60Ow`)O!aow!4|Fd#f&zKYsg97Yi7=zJS9wwzIz8dkV8jXzUyEVi&zyz=QZMLM?9C{}X^6~|7ILQiEa'
        b'A<G{~;CzlsrpVtLOkqJIA``<tEhl%B#0P*Y)4F2ie`9FV|6N;G9bBw@gw`j;UX0|*slBP$zAg+~!Q0I59GKFZ_fQMb!7*s|>2FMd'
        b'Jc1u@KN)LJM>ViSCLxQhqUuPIosD(plP{IbWOQ&;Z!i`wCVj||oD*9Pk+J2qF$T)sM%C-$ojqLig3|_l?n5+StIkX{sJM*k3bF7x'
        b'R8!r2f??Lwb$&FZH*t8*zl3<|ZK=Qb9>zb28$Wg%128*K-7G)3OhwrWQ)kS5RKWtefXTvTX{niv!e!!>tJ790#p=J_fPEyeDA!nn'
        b'i{-9mpRUfyVW~9Ms;i#N@H9h}{_hHnRqk49ruITQ6>D{(pCuso5wafk)C*J4rK~=|<%;AOw%o>0(ZeZhSWcWyOIcx{!p9eCPvcr5'
        b'xrz|wfgDNM$_>6%oT+)R##-Cf!ct$gkY}d$<Wx8>1ma357BaEV9(M8aC+;hnS6vUF+8>t7yob8FeSe&Aeg&gzIp5mcP$B7}UTvdZ'
        b'wo|)74(Bxv$FxC^!+FY~zBsduu8Y!s#Blslo5li4Z2voMX@+5rw~MUXI?AW*KllBViU&`czM4?cZeGrVMhz8Hy6j<B5PBbtdGarg'
        b'$U*hoI0HRWCHi^JGmL?kEVQs-D6>7e3l)ERv5k76cDHo`86-MdYqCCA(SD@)!ZyyfGkqG1i!SYPet6J77ljR~f12tUREO%=TZH9k'
        b'ur7NRT{Y!}llqDYWQ53Cxvt{DRhk#gninoq+-5AtLxbvM*($mU)Jjy4#S(r2cgZj$$uj2!A?^ypLME8)VV~61)}j&y*m=s*_9x#H'
        b'6F;8PR?1&h%4;a6JcIT4fZFwG97Vx{pmTj7!)D4}_c=(T`3<e>l3imNs-$8WE>^W~N=ZzMnX;ftD(%H5e6*!}XxC8w(5OO7Xl&`E'
        b'LG{THEluWf6HtlFH^X@$0C$CAAwC9sSZ!TpB~4$ShrS8c2ir>c+7e!aafm)HtTB*S<croANK`jZ9#c%q0;I0`2coZZAJBJ5RNVRO'
        b'l+4H$17$%)blNjca1|vqecmcMo;5Dw52|_oBUN-P3d#aHo5Ye+FO~%imA^2csx7Eg$Z1rw1z6seL~yW?qFiXKeqvC)e4?B#&=EUZ'
        b'2ku4o`D87%$3VT3qh7e!1Opm0uL!^6D8n#%g|eLu0iT6%SJ}fV>o#sw@-h2K-wOYxBV|q7;v0-1UcQlyOBsl1btQLX^kbJm^~|5*'
        b'2QsFVHXUI$9uXC1Ms#HRH)mwS01d|HJe5B@gE)J1{nu{@c|RxxNC!H7m*A4R&q-F)!wSs{a!{<CYtURVtXRjSKiv>6zu{t|+7?1T'
        b'#!y8JdaU<!(rY&i)XQe-l`+LBUP0$1V7DZCDbs-~_gzyqUGsc)pwC}lQ+|65)tt0~XD0)~nYgli&{#hxp<eNx)3UHaDx>EUJj@h2'
        b'@9>e(Ls5jupRO}l9>q8jYGNJ^ZAb5hJIqDrlAb%l6<KTSAE2}Tc~({g+jGvb1utf@HeDe^m?3~bZ{RTbTK;NyoQTa?9V=dK3fTRl'
        b'<@1`x2__cbRKZeZVWt3ri*>N1TwGW?NL+@r5^Kz`uy#k)wEOa#+IX1kWo{EoWU2^I5}09`uPQ@nIF_M0rmXmD0gFr|Cs_w7J}(HM'
        b'&nO=LVE2C--pwedYe~$05IN;gUlNb}pu%4kNSMB>U=nOBB0ZWL$%MQ9!$mHJYCoi|F+?(+XT>mu@3ZG{TobS!RtsK1>EA{}H4>!H'
        b'+~y{tk&*hY(<<yBP6+z1x#vnu)Nw&o^TyS&>zulEU1)nehs+WlCK6^idze7SKGfMHTu;QBoXP7p5Ea7B>=^o-DeHO8W`?9>J&DUp'
        b'o>r7>R+X&OmON!BStTj?oup)wq-3?E<QYlHMoGz9Ny!F<Y_mbOS<b>lrr6X0MgC`olFi)##*>`wO%IZlwdf_@wqjplG0Px(Ix(=p'
        b'f3jKjbY1;}i9X~u1rwV)7sAh>tpejW?l#%ecG-IAH*R734cAw0g={VK5M?Mz)@B8Y;`tfbfk|BATX*!r1n>^O!sg&G?E*quvgV5I'
        b'_vdY^?Y8A)WSeb8m+eLRNIQJnC)=#zVxlvBC7b(f%RYJuSFU5^ci_f{u=!c#FX6DY%}-2>ZbX;!;nFWUJpnGC#$XEgKMPY@IVs%o'
        b'gSfJWlVZtF#Fa(Z{6y4x3uZKPo<Ntb_0Z9O{&95oSJ?b(@L#zCBerp{Ck~g>gBff~;lj8Md%{#c2{&%#xJs}epp}}D|H!O;aFL4T'
        b'CkOP|N<X6KG}y|}uqp<zk#p!J^a}0#qqy?-SfA}lXy6LRh}9hI3+Ofr%YRsCu&qQhE`@GSqgk>T$|pI%yKO!Cv;cZ-L~KumJ8NKe'
        b'qKHGJF_3JAmjc9;=)=!aF)>((%t-;tC!oJ)DT@AzmV!v-V9-t!pB0qkBbTj(g$NSGyJoXhvNfrBVpYkSs!7CSoDi1F?oQ2_Q8mdm'
        b'j{}LxM=x=vnm`qdJdB(~Ov13#Q!}a_bY*b*xQzTgKJ<6wbFPUP`KWOMMt3yM;Z$dciS2ImQTVriHzskMkNd*?1dc(ry8Cor=Oy0<'
        b'vF90nC94a#1%WD?E+<2*d=5<WeHN~q#_5x-Is3fe6VoM=z;OIj<#UFTHLlI>ssN*m1GGjn^W%B^nWRurvW8gi1{tgm(MEEWTn;%2'
        b'#xY*P=>JM|Zb)Uv;4=4GNC;O|vdMVa^A&L!1hct?qq3#;%YER69axw|cstH#!yl5Z{2KaizZjyji{Z1mWK#%Rc>&8@h7&X0D%tN6'
        b'Ag_$V_8ar-C!UQLXg^{k&uU~Ms4Lc0cet(2+4m7+V|V)@$k<!m3vlIwkgqH9?WnB*+9ozK>317xWvgH(JuAfEdCN=5@8l(`5+rPi'
        b'>?!n6Pr`~;NWfZUE9J6PXT1g98*%eTjKu{_Y*Z`r_RYO*C9<`Wxfn4O9cla=R|3WA{CX0oPyiJ(8ktJgE%Z7(^dfRmLlrcf39JQ<'
        b'CU({cu^gD4-f!NHT#(ITb(5#|{$1%cfU{VP#jsp|9|VdZc{fI2`-%K|9#E1z2gqO!3D`?*?Fh9K>>n{uvt*iD%n&0FxiYUbWJ|sz'
        b'UL*yVr(GeBnNSi+$YbKr)~1|(X1YQym&9r%a-erP+TAoV7fYIOv=M^lOD3Q<1;oSwwWzg1vO+GA#>%Dg5$Q(qTpzfx$)F99*#24h'
        b'^%F*9do!*5F9NNu5SmsWFF!=kKSd|X(Y<tXfKGZH#-&sxTbnaIu7DRAOf<TO=p548o9HZh?q5r%3Uu{e>4f#K;3=PVZ|8*=p^u&y'
        b'LRJ_`HknH{x)8WAmmNYPOE$n~CPqqOpzVwhFiz5;D%nWR1pj6VY6#?%eEv9HN6YK~wu1i~BrpQ}-&&E?T(TD0H3spUn}QmG2?+h@'
        b'Y^SHGL+`E%HeO{zg9BfS43QXFW#?k8%{n^|d%yCJ#Zp{(884oR6VI_ic&R#8G5F#|4Dd?bGsz%x$r{_^zCuf!dS-}0_B&AEb)Xk%'
        b'*#7YHdXFHpm;`IA{{GIrfVaZqAGGCmp0|}U2=Yge_rScQ5JP!byeLZn=C(qPjE7do8i`kU9%D0kj4cZX6R51r<|27R^92)-eR}0R'
        b'+$Ahl9wzs;?+#G@kv*TMe_4dyQOD~JCceeZveiv2Ll9FEgv%0RHkDOZ56F(-t}oCR+a!%XXWImZ61~0=buq~F(B~Z8$463t{@Z1%'
        b'BYZ>_bc)=N&5a?<i<!?eqX}0Gw!e5t4v8ajXkj8rNPpv=!&||Ap1pu=3`M@O+|Kv5jA0Q!x{)xxr-czdOH``$3gcGZ#)u;kZv$~`'
        b'OX4C`Lh@KKt~|nH<>B(7y5B?$>v>`ULB9Z-B+%s?qRWN>!(AoMI=*3c$({wC->=1$Pa-9OHMU1$=57Wgl8}P8&DV87h;2R`(kFX{'
        b'fAmO56IncmZI>+%pZlP_t`SBtm*~1|+%_AwvRS8}i$rLa>0re3b&XwhI?%u~KAu(^zdiYW2h;H-(_Zond=IUPc{uSH+vX5=FSjqm'
        b'XbRh8&uqH5PqeU0wzjt0EPJM_WNmR0(6u}~n`4%(;e)QPx&G4rw{$z4)pZpA?L+N&N%E8yE{uQnZGk=k&Hp?P#_kSw{T{DPZem?3'
        b'7EF!rVH+7(kB<^WK-y(bTY@hHMRf3hIFA^L9&-alAc@_<RUyhKw(d=5YaCVbX3*|skj=xq>aV^gesVXm^bes4s(4MTs!7U{8!kRm'
        b'xQ4ZY3t0;^N({{6*3^f@TAj(oFm&>aB(Cl-1ll!4*=}L;jZec}{wOtp#yRoM#Tko>lLE83V8F|f0lOC7Fb`YUBiMdrO}$57N}0xy'
        b'Anf&LiS8A=CAbmUn5xEWW6&;WC`M$3Y^edC770F0fqYu#cs@-5KFuodKAx_Xl;KFJ6iBBsL%E<+^jY{3r#7NgrFgfH_>pCot<iS|'
        b'd#z0Q14{xHLn!>15<grvL$;|@ryGzR#$BI5dX21%3s$E8OR(o`_Q$Lt`+_gwGJ-4GdNxBaS79h%ma$wii0U=o5SfU!AY)7m)~qN3'
        b'tZNBQJV*;*$OK(MKa>ANX018N=U(|oMs*%6MYaZ3nGES*7EO1@AWyTKwL4rcTa(Z}p@Y{*=ywKtbcKKogI2a7DnnEZTLx{(23G_V'
        b'=~MxxdczG_s%@{Yy=2`UuF#aIUMw2%vk%|N&q@Qq&o1%!S=CrStEK(ytnvM9$!+{Bgw9Ii_<pwJHh#8<1%5Wos{zY5T{DzyP!`e)'
        b'%hGzB?W~79YLIx&>t^+jq2|Ki8?fw6T*)HjUPZ<TA5=9)n@z;9Vf|MyquIo?JNeckF08&vwr+*Tx!&SikpQmJ0+7xUEmGa=TT5=^'
        b'Tj@|U;#-%DD}#~Pj^3#d!=h<GFJF<@y@Rfk6G##~N`DP<tl(8$LbSbv6>a2-c7snn*#j>1aG<CeoM~Vac#da^6TzQ889sNiy{>hP'
        b'GyNgR<4n)jwGMewuN#ehQ!L$y{HVu?x^6JL=Yj_XN)5<=_W10x;Ko_l6@LtTH1r{>NdA?QXE!$M&!aKxP6S<%J=@6Zt7|+TmDpDI'
        b'2N=8k(8e=851fTv4<8L0%(2(~VPi88+<wT;$G-lguTJMV=wGMfTQ?r9-PXp%y66l8#_t0c`rTlk>{;llK5|1z0Uc{=P2j%`UjO|h'
        b'_-_OFZ`fR|G0WCnFPj?w&gw#s6F+#Uot@u~6CA9CKz{t7K>uD4T}29p6E6OQ_TqVhF4;P8;v@-9ya&nD5_lnKGRzOs1~)7HZV&`s'
        b'wYX}xvK<x-*;m;Y2HCo*K;@19EPT^xScsAStp}*o#4Vzu!ca#3(Fg2d*rlTaeRGi4rJH3NP%gEBxcr|OXqWIMmdgiiNMVBs8+?8S'
        b'n6}889heXlc_H8d591wN$A1h0m7gw#cJc^J!NgKCb+BJmKYqPC$n^#jwxzZ4L=9tn-=1}=Z+Cn$IAYf|W9<5NzK!kiZRMW#p55%*'
        b'vcR`z(|NVmx80hrj<`13t_{p+o_=1C*R#8HOapDwflNstm~^D!jqg3KohW6}2^8cD$g~#)d3?K;Ilgg&X-5-;0=t`UcbptVz8&T3'
        b'qkOyZpY!ea$Uk!J3kcY3LGo-7@vT;osMgAdR9Upco{s5~oV&Y9;)5ZjXyJAc`j8+x+W;9QFq1(^K{Mz03}q?rG<g$^P+Pm$lWFuH'
        b'AA~excX0WRhX?^=`+lTPYUGyZnPTy3l)w9!d01_Y*#}eq_=7Ig+3n|gh)Hq{>6oak>aQh7`H+6N1HHN`mu-NkB8rd7ke6(Ls6y;y'
        b'V06-s-0+$ZHe~WSkhwP|sn?8T?nFB1Uis~HufJ{ZUz)qazP_^J{&M$IIK-6wfgatf+;l|(G38G<vgc7Le55CZPx{B${QYpCCw~_%'
        b'zmBr@GVG4&yAndo+K~{W935g>59y@#!J+)!^*<qhM=^$g7=x}+jB))M^XBkHaienhXYhYIhc5`cTMl0oJvN8`4c@&N!VlVZL;h}m'
        b'W3c*!c;Cx75sBITF;7Q_m}xsH_H=n?E(8;T2l9qcva(xOy<Z1}dV-0kHHs%Mc;gB5Q77F{hGSSC_|h{FQ~Ji+6Fdh2C2V9@z%KCw'
        b'l%b75T;R~gKv?;ScU#bdUKkFs1nkrt#kdeOW!O+bs?rw*JzIjR<y9d@DJm@iKA~3>XyJo}eqx0`316{MnAz|J>;;znq*{o<w!sr)'
        b'7VZ!o-95A9sGyOBss<db(+fr!t|%UC)|LO0@I6)>ClF!`dWe~^C@9;9pQnHrV=4&B43u7&^niz$4xggu5G|huLp!oE%SXk+V)Jw='
        b'Hnxv_4B|^A47ZlZ_z9yQJNkO8UAXLl{pxc1!5G>a(9iM4=8vlfS9rYasQj^%e$Hg3{cLu~mU8g35x4r;nz4S?G_;4Pggpd$&gAv8'
        b'L(XBm4TMm=5n@c+WZKS!!5a<q-oX=LW`qy#9sa@?9blZOxv+iJ=<u=?!VB6rl(A5FVHstka^_p|#{OlV$TB8pP8{}c_s?@8v(k{n'
        b'9WS=jj2l~6D_F?s7kZt(Qh3`qlNlepd)1{36lYj^!(>`{g|#IRWr#6RX8*_DDD%M3cGjV#m1Qw{;Pd;*bWmxv>OfuFY}`XWFOWWF'
        b'm>}LMdNcFrgep61Q<hKmZc`+(waF6DPf5vIT18{n#@By@q%FFPzlh}K9|7xG6TQZ8;$zsekUqHulg%anX0FrK*3gfW*QM-6r0`Te'
        b'SbmB$rE=d)+%*+T;q9BGLdl&3i*Dcd5_-3I^e5>5bWE9rJy8jl#%Wl7@<jW4f3(?Ff4>~PuE>>!*=?GA2XW&ga8aC}j4Q=(u^#;<'
        b'5sE33LB5ARN52`j$u_EwVs<;$XXDy3#C;_j?aj~b`#esy|5>nvDw7IjoT5CSS0(#5^#9*bY_rQYUTPQAMNMvRZ+jVQE7@2VG1->k'
        b'>+(mx<;phJg-yQHA!u*5*JAdPjW7jSd8m0U@x2?qBbz^J{y)m^+}OHh%j|DFYrO2XH(;=TYqMjAYE||YH;iL<U_eU<kM6uqH4hUV'
        b'Z7W&VCwqF)gZ#XL2OB1FL{{qrQ~{xF$mJn_lj-$0-Tyy(?*bQ9ng5SJ=gft<9CT*DiJNuK;Wms~1DJrJ&Wr?z+76hgbXg!lbaTIE'
        b'W|yUH&R8%I7LFwsb$13sfg%AbEpr1ZRt;OR&9zoHGBIl{$pB%5ng8cGGa#Do=Kgl~`~SWEe_tNvxnDk?&+~ac&*i*N1GGBhL%cA|'
        b'{P5f2<=PAf=)lLbmK49K%sA)<HQ6FUcn>hqm9gS+h_vCzB~@gyKM_K;exS%ap9t0~G`59T-ImD0r}nqsjeyAy$d)XB#2ESOZ8K7M'
        b'0}STpnF&R02=qmA8=mu1_%Q+NpqVp^K7groZOG94_z+7<)NR2p*~abVCm%w^HKh2Dh~MuPe>i?0{9_!I-06u*K8){;f#sn^Q15H_'
        b'ofD{_9V$qy<L!@Y_Ue1Iu2K6Vg+E(>7`$7{pDm1QPwdt0!Q0taZ`LP`Zq~DZA<~Rsnq70YP<*|;`iwNx;lRfVMV{ssrSNAVqr2bN'
        b'ISc8z?V9$EKMVPn+6z2MoA-0un}s?aLrC8$RG$<XdA(nzE}G9bh7>R24Q6ixXio!pqpjm!JQ>XLEgrQuLUrQB$P-tT_0u>Ubjuks'
        b'ITjhR)ESY5AXgw=PwfZcN_kmS`!xo=>G_ECK<dKuqb?$g$8X19htGMG>x!LuE!}KDHz#jeX=8)yYObbR#np7Pj-y*?NxkG+x>a0{'
        b'Zu4Zzf?%fbP;A>k%8t=Pfg-`x_Amjh#On~C=eTo&7@n-5A=Z?rIG(IPr$~+1yJZw&iM!hN8)GflerfaTJ@>)+EZ!M1PBT8eH}NtV'
        b'XyR#NUJ=JQ%*M#aXU2gN%Z*&Go8FogJ2O9b#rlrqK}+P5YK<6lJsT)qk!vcNgzd`6b?VI^4^QR`r&1)WB|+768)3#u6$G=eh`2Bb'
        b'bV0menIJcEolz}_7pJga@VhtISdK#K&k61<PJ-8FY~;GkTo*JF3e6N;F6=X|c#@5Laum~M-zSYE`+id7R$YtT%uUC+I%gJMEK(uX'
        b'ZjSnj6(rYx!lpgL3hu5s{4|?Ju!1Bu4b=<4=t=#m_g<yxLz=sN5)b<XR(sm21F|E+?42~X6Njx7M18XCD~j}D2IUJ#aRw?|yEM1+'
        b'&PFo)gCEjmla{<BN>$<hrAxpqPG$K`<a7~uh}4(^1Qk>p;FA#+=+iSH!(Uv{BdG~fb8dgUP8hvwVYY@^?iFK$<J_#2b8;3EpI%;Z'
        b'E+=^siYuV?Z_soNUF-Nk4Z6V>4{CpL;bV{u^3;dbEEj{Hy4z%>!C(1jooSubU#DBAt`}CGsnAS2AZ#RSzjMDflP`4w>(75T1)A^$'
        b'ZbA)%6wP$)1fQ7Q?xJ9XG(tHWCCo4)jejs3<<IB2M?4XM17Gl<Y2mh+74IndJ05XcrNP#EVTpf{82y7w9-YUo)Y*>ftRoH(3MHNA'
        b'<1>c$$?f&$v4)NaYQOPdxBmNZhW_aPQ=Fmq{jcB*wfSEMXDD^j{~FGacGAC&GZZrE|Hm2nzXxZ??*DUehPL?s-;Fc$g#Z5+afS>a'
        b'D2?O+LFdvE|3(Q^um6Cqee?&59W*6b;_uOMA~t86h1rHL{pM^P1K%mLY6>!qs8JIB;1A4NKO0jOS>?kr+cYY$ESO*W#X!Jj8RWBS'
        b'EIC!MzGPO7OBBQARJGLTV%ik%?5VL6JxyW@Q^jg{-5<c~VU3#mr5}&yQw1}2T&_?vFSAC_!c^farw<Ih_AOL!?MJrm_2WOXr8BlE'
        b'YMAnO-YD$PdsUo~^Sk7Je4z@`+k;{P#B``4-!_-6^x1Muz*i}+_=>MDiLb8>)+joh{q5Ra;$zH9r<s>8GF#f2t)9B`E)z95zw7Ac'
        b'0hh^9=%7t(j_oI)L9C;^#RE6Q&b+Izk8Q_bL&lsW9$@Gdmf89fJRu{qRUgx;UL?w8DlKh_d152;VuE@URw(xbi4jj;IQy&&UsA>Q'
        b'Sv@cKd+({@=JlL*mj#J`=LHnf=bJr<LOOhZ*aIolv2h%vP&|edn(cuUs=fwNsDnUjbGBkUp{@8;pRE{AsM+sEctX#N#}nG+hw+3M'
        b'9#7~Vrx#Di>URZCXo2%*;0evX22W_~I6R@EbvK14w9IEMW4k_1&h+cy<XEoY32ps3ctW=S1w5hI9hF#MuD}UZ7hyP|t>fT?I&Sx='
        b'VYW_5tFfb>hbJ`g=IGS(KR1CVWc!cd2~}e}p{+cgQ1y5`p=vLl(AMkW32prep3qi2y0-FoLR)`|Cv@lvp3v5-@PxKrg(tN2Dm<aB'
        b'{}fNib|XBY>G=J^_@ClS)GobAJR#eE15apn(X&6n6SDnNY=i0e-P-t{zFV7@_AlZI+5Y$Ngr@(C@7CIG{Ib|JZ`Kw)=V`+~#uK`p'
        b'-0<(E-g%RFLbm@sJfR!)p+|F*ctW=SKAzC@@$c5gk9&bHeDcr66T0)~wtYOl!OwWN){7_9cw;=FNTJ0ubV0_VZ-{+!Bi+<9;a|WL'
        b'vi*nfgm^TejyG=bPW*<Sj#~)38c)c2T|A+pE$B+KuiJ`iTFsa9Pw|9qsPBhd|8Jow#uLiE>fQL8m5=kDzTAqgrZj(R;U_(by*V-`'
        b'ka$n?{}@YX`Zz41_;FZ5;a}byme4=t!}YL)ey(gkAWpt8{BN9ZKlvB2glzw9ETN8Pt~1~MJS?Fi+s)3m&)#^xy@Dll!}<0PH;E-='
        b'`wwFYbxgY<me397+vagtLSwV7IOwN6i2IqO9Y5JZ?dWGrxBtpqo43>TzdhIf1WV{15?lM%#}c~H!0f5IIV>UDe*sHq_e35`DA9{0'
        b'Gz()1-9j31->!=#^wYk1u!O?PZVpSx_A{_v{$(to*+!=N3YO5P6UMNFGCWv9)yXCvOK8bNeiNgb5{eg)*HggQYPuno&<*wPZ$`0%'
        b'cKnC+Z_)EVPyZHi9_{;^ZD&(<jA2a_ng1PYoqr#W(2ev~Uj9wu2;Hpi{WszW-EjWMx=9=%+kXs4h`tey(2e!)JvWCVWc!cd2u&Ep'
        b'5#p_*e}E%29plBsUk69XFp4A8^|Nt=5-|RX?WS>r-o|4yj~|=-p4W|Vgm!ySgkWqI^JA0mOVKl9{rHzKglzw2451s+bLvfE2-$89'
        b'f9KzcA#|fY<k2^YA!PgSVhBwihaoh6SoZkeB!-afzltH0Xq-FipJNDBXUv`bGcbgzF@})9Zwy1IW7f@K2z{XRVhAN&!4NY30}P>='
        b'yspO>LL!VIl&ZiG20Vz+S5((rUkvEOeMgN$5DH$bzE@~t98^G!6xntY)zy@|eBb8n^3EmH))jXV8-0qU;Y+I73?4qn6x(`41O|xF'
        b'mp>G9P$G+zSP~$_yUdQZ!&KK4PZbMreCCots$#`nGWiQPesBNh!vz(2;ex6?a6!-Va6#4EL_GO*qj*8pqj*8pJYG=s4e)|yU%?Bi'
        b'9>oi)9)}k+`^I=d$E8>Bg2JxC3ldM{;er&tJY3K>lMlUf1uUp)3@j)wW)v*w^BMmXEa>$wN2pP-psI$ev4W~RI5N{*nQ1ZC!3vr^'
        b'iWM~bX0U?zLO%}IxH6qnuZI=1;3lwwJZ0sDx-w^K{*SSOs>Wdjh2J`c6~z8Ctf1Gae~uNzpH2q2G7nF_3M;7kX0U>)#$g48`;TD-'
        b'1^hFtpd#uYVFh`396r&NDf7P;E2ug_xY9p{d4d1HOLcH;brLk)nDb&x4nB@OyTJ!iJwLrejQNo}#*dCX8SrCb4Bye2@gU=o->74l'
        b'?MCKzrbUagl46(_jXA$le}d71a)Cw3tvmg{@PGwvdg{p{Io{(K4;K{d?K*}Fsul8ZL0M8Lou99u(;$wvzmm=KsVitff4B}>5Z|^V'
        b'waBFox`g$@b+Ce#4I(s(7Q`q2pmt<Loi@VnA+gMhoi<8<O}LyFI)vBsIsEd7TIRaWIsUKZ{IR?qAF4Npw}8&80z$BXUU;Fon}HTZ'
        b'6u$EVODG;-NW5cETsz2nd3>RBgUR0xV*Og}!55N{$!1s4wlRF695jzurp(PDxqEP3Cx~;(K?Yyc3hx^k`>q^m@e>z*Rt~d8da@-n'
        b'Fe4|?l9OQZ^P!}c^c3p`TTX-}M`PWQn={LjqqW%0K}%~sTx!W-Eji(9b7re@XjM)amn!GK0hoB2nRStw-C{Q%5eDtYch^Q1%C>xq'
        b'AfS;9+8-W$q41*JxS3TZFOU?Ik})`-8fL~cAvYBl;=wd>d@1L`y<XmbO3tz4{4I8buhk)B*V1F(U$na^Nn`@WwaZIc3yCNTZB=-`'
        b'amsuwe{Eg!$8!BEH1{zsXInK){6g*{>@NGf`Jfy;2YHW-zc7gJwUx`Q63YpKm1y`fxDlE6o?DM|^c&?|vHXC*Dmf*xXcE2?9}#xG'
        b'L``nnD?cC<<NIqQq|cX0DB(P@(Ox=_yz(tS?pse;--+-S`tmN1mG`LpJF&Ms&)5F=yN&!eGBf?qEMl5)TT<caZ6a2P*hL8bQUc1K'
        b'p1zs?<}-&J8{|)mqN3*!4+tphLQ$>|44Q^57p3R{((G1bzUP|y>5?t7Tp-SEQ^NSKBfhz0ixB)%!XEBRDP|IdDQZ%jf{Y}}uzz7n'
        b'Qr!RC5`R3`=aR%)yMk>e4Vm(Evpn;c$ncCjeX)Gai_xbfM||-2H%pX52F{85bwXLsc)~nFUY|Z_pky1#?XqbyD&$xP{+{A&;c8#d'
        b'563#*3jvQLx8soKed%KzzsCW&xgGV7@4SDDQ&@4=g1uG3y7b7INhi{&33Q{b{I9yB4Yd9IhO!6GF@??*w@*8#EU&Q8uUk%0)z$Pa'
        b'3msY0uu~hA{rl(@GYQI9yK>d`X|hJj^F81~XD<IO##8Qmnc`gZR5qT7ny_6oO?Yxo2Zgpxq)qq?h%^~DlxJs86Y00KrV`s;DU-?L'
        b'twe%EEJP@?;sUixe88P~%LS@fyx%>`^KIDC?=#kZ?e>0W6Zp9X)8mNXl<)u<es)~=sw?5OXGX(;e}3{P!#rZ6fGSxi!Q9g{tY7Pc'
        b'Hj?F!D>C=Grk*JFaPJl`_x2TE;oft%@!Ts)!rZgizc2&$ti}FhvJrDHL^Opp{UX|-k~b^mAatU6O3sI84zo~xLg}F7&2sq>5m$;E'
        b'Rv$geu0r<_85QhhnP{~yzW4Btc(%mDv*`;`s)Xm5$k|EfnDRgC=+`mFPEq#1ZYX=;Ty*0^56@oac_s&*)mrHAaXdRkd3h%H@T_qn'
        b'&$DC?&kP=(6<*v<dU)n@W1gKO5+?9Go779yir;f*zI=gt4tRGB&+^WV<Bi}7Z+gb_Y(zR1p4T%jyhwIRWR>V!`z)Gx{_E1CW7dH5'
        b'`o4{VZHp{+cgj9_jJ-60EF9!N!47676@Zl!;`Ov+gDi@m8x;16=WK_#kY8DeiYd#F&m&DLC$mdtVx2T0W1f(K7ZLN<qwFnpB6Wj^'
        b'`@Ia$R}Q-jN%eMn^DfCeW}D29K;8@wk7c-HXMn7^0w-%KZ?3i$4%zE<=2AtG2yr&qu6-&2Zj(%4Kz!r4Vp$2HA-r=4cfV{?sSI>!'
        b'BiXz}R$L#ssR;h!q7_7t7{BzQXr{v#682XAh!91@)WFPbWD7&o5k0GkA{pAJ1lLCdk7|eAwGR`fAZIq=Oy=JygOoK4YPS=$hX|9*'
        b'si&P|G?{&4n&ghsBzCNe4<4@+sY^v%wyek>XmZ~eO;VU8<7g5&mSNiQI@Fx;6Pk#DCJTWkiZPmC8Kfj0is0|^2GPZj6%NtWds+^1'
        b'A>Z!R8jtTsmV*|GG}|`gZ~i$FWv^Okt-^7a%+Aswt5AR*SsZ({q1;RvlIzXpX00`3Z4>{MXtQ|}f9=&oI#D_PlAgKB;{Db%)M9}O'
        b'RvsXWqvDPS5DY7$rzr9zaU3gyX%oyL2O~og+{s88yD1dA%W>H-$Fe#ztH2u;`R63KXe9Fz7W4C*bd%b{Pl{^(N?KeWzDWrjm3TPX'
        b'p+X0UJRM=T`$q&RBeb`ke+RP-IFz@W0P(<{JQL;>K3DYc6tl09@LW*#Ff{xgFPEX-at}Yb!_rNcrJj02nm^?0{ZTqrFKCtnM307`'
        b'ruH@{TN@Nqh`qCQpAwhVd_^*@&}G$jvRHcyb4t499AdtZLg#67GrQYuW_9JP!fPk!KcG#Y;v4t}1bGo---gaXc+5u;3Ch~pi2IAw'
        b'q;*;)usE^S*paz@gWbFic<)CLnW;hr3PvTLWbP9%l~PlTQ%6i$kAlLV{=WHT>C}J{S<|aDcMz)uD541871!IHp`a2zz+pWDL@0sO'
        b'&S5<}N_%{(6xSP`hPbz-(_~gjgd`+yfH=9TjtCzh%A9q|+J2&}H2m@Jr?OEpW{=d<Ufmwt2{wmFAZp)3T!Rz{;%PD^^Rzf~sS1Q#'
        b'LGaD3RE81+O$M(=e#|N<FZs}Jj0jRR2O7!bNuhV6!FNGEZ~P3TcQ^$GGVeP=K#*#!FLR%Cbm+`qufX5R$y@!s#m-n(A!ehrXbSEx'
        b'PX8@VpII%2=6}Oy{Z<5{{v7X|33P#$1oW)@zBz@bTBDr%4No+g6Ti0*Uhq9*kO~OGVrM}Xplk(#@u`Lq&SDBOk4iz7pot*K>(OlH'
        b'*V1HP#7viBxk1qGsWl7%jR-%DtK0TDi07BQYi4ck_fs_`GDa)qrxE5}DU{%qqa4H&6!oMFxh1&#tH}uhaJ~|Gm>)ngfjkj$t0v_='
        b'@O|^7G3L+X`w`^SGtN=l4$9>wO7(QMo~2Ed3i=LF+d^qMO9Kxh6aDRUHYf$16^Fwp)_p=pzUzBLcuK^j;-We-pq+E2SuAAkG=|%W'
        b'qI(c^hw1j{URGg0N9)|8UWjnzvv{7*k0F!qM)-wJr2mHQytN|${jutSippt@snX`DQb;78gB(%PW~~&GiW5O$NSmXi`6^PJfE>3<'
        b'o5Q8Ra^wh+Hc!T>i(-)@P}&@fQy1xw<D{fngi{wyLypfR%_k(uQ_vqP{TvEuvqE}&vdrNtZB|Of5m0}*wblG=bmF1nsL96{Birr|'
        b'Dm1rw1|QcX!DHbAB5yMRGqD3nn+YlZ?Rm!slIHg%5h|YuR(al%?2njlBnxFt8M*@^u@beB(k@cU3HeD^c1rHJC~5vtg5L#e8<unp'
        b'OSlnSZrgW~uJ0wB6T9*I<Bo46&EHCr3FJ5{Y5qns{=4qY4HE7P3H?`vZolF?k_y}lx<*O`P_m}d&E-~l*9kfIC&^zlqP>lii)JGb'
        b'E>kE7omSuE1R;kgepVO91Akg2^zRgVx8vOd$48Q*e~fPL<aWKFFi%sq@3w%b$vb;l<yqCGrpV}vyDe-x7gsvb{Je77L>$NVT9wD2'
        b'aJRnLisyxmj!RSJ+-`~adj<ac0$sD)LVw<hCgZohcd_#3dI>Z)x(@!*bZ0C74j~k<r5bh4#P3(3-cqH!v#G8%v(RNP-4nfCax%XB'
        b'4$-E)5{wdCrIB{Xae6shyyFrSy^Ed1wm(x|LomOSXf+^|w3g;=I9l6^NIW%_YiO^oGCU}u!xXydintolLUNj5mXNEF=!~r}5=^nq'
        b'lsX?BD=WGS@)~|8iF_r&V1~c6p;(fl5<v{GfO%E|X;b|0heXmji7DLKaR)MNmZY(1v7SN}B=O(77jiF3;xtp#ell(~I8^Cn65|IJ'
        b'lgNo;wTRVX`;9Aspm$5zQg2S3F^GFkq8Gr3yv=M;ln|h%vIS0sQKmy$1sg;Qv$7FPD{0VwbF6|}Dlt9eG_z(?hLd?hk}YzY);iaa'
        b'Y1w{3klsY3L1I0h#UxGxcGoI|pwZPrf=Q8-ClPd*If}sc0IT)ta*+7hFj>!WyWP*g6Ab}#?)ghf<G{L!(S;W`zd`sOjmwe0_0Fpe'
        b'+F4aqRgg9nYhDbti<b9^5+N^;&Wr)vXJZn^L)a&WZogyt9e-&Fz7Riy@HM?%VwEI9{y)Go8>)di%<s){Or7)j#CdZH7&i9VMW4kz'
        b')%tS$+i_e%>fin_^R_r;Vwdj&vwr#d*1dQ4?T9}Z5j0c1@>h4g61gW4%9{OZLj$f$k9ytibu7{cOiQ}=GBY#>p7-4DiAf+#(3ihL'
        b'pKhDI?J;CcJQMd@2m}8`czWizpAqO08iaoIzNh@0{c2`o`JBJ|t`D34oBBEFvyR&HeVga}nqKhXk-PWKac@AjuzBrsd>7+?pU%1C'
        b';Z;+U-l%!6dgN~z)Be^tXLa?u-4~no%y~o|>gssp-8mopy%NZDXihoMVGU0oWPX-`=_M5Dhr^KGgxd?hU~HO!7SABm3T=G`HSuZn'
        b'cpw06X`BsTg;~&)=yqotYkUu1oc9PkKR{Zu>3xJCY$L?S`Uk}8r^7?<JTwP=`sa7wZD`&%2xaM1NMELo*ME?HXiiwaC~+#phryFd'
        b'3ymZc-={=+3exO*B~E|F{qdZ{b#eNGkhXF}lsEv-NAM)xCQht7AEytvC0>8-yEy$Z2vfMAonRZf-E;Pw1Ai3wr-urS`&gmzd|8~{'
        b'{d<ri_e5lde3Vvb6sr+B2X(dnElw{4_jG8(2M|8NElM=Pvjy_s4^Jex?}w)W+^{q=zX3Em3N$+bw0Z-=k4_RN=I0|6kZ}mh-}_Jr'
        b'B2epsH6h}}jLG7}gYf$aJOXg5;W5B74IXIcu-i?bc&K;V3vv3B@JPVkTMlvOO5=dw_=YdSYMe}jG?F?ThGsRuzw<yFsArZxge_Qu'
        b'vQ6-~-2&*ldyWp;kqYUbsDU{6eGAI#f~O3gu=nEhCJ4J1o<2#u{)9AMpCpUd$3vbna6fx0PJez!oW7fj(@%xpckd7y&q2Puw~7-}'
        b';n8n{Q3*U<BZ}9*;S;a-hdlSg^HPk^xEkVj!c+d&IDOcs&{i5{BR!c7hIckH$F;hD{}}F1llwNT410gy32BAENA$)A!cP|FD%{Wb'
        b'pnxVpwizA-j{+Wlcqn*6;GyBs!y|-8g46U0vIB!fK*wk1!-Hwx1~hAh--VaJ?*qC6{Il28o}Y17!@fBPKgc})kq<)9@jdty&g`!2'
        b'<;MX?oe&v+STuWa%)_%qJD#7tclBRqS62l>dcFP^@$2W<-`_sN3Tex6dhkP@xrq(&u?VT>mi^(qI|J56&q44k*dHA`;oDPhF5Xib'
        b'pCg~Ke-Pxh7oKzQbi=bui_nLWAZupKFZbmT_?^@0c2C8A;9eO1C9s_0zsQBzuY)iRJT#7b2J1Hol3-bb=U9U%@s?Lbi4;5vC|3bt'
        b'e~dxs1k|OOb7&3?PZ&HQ@JuyO*>%}uwnR^57r=8)hqBKBkJdrC2$%f@)JWs;a~bPUh5HitK_0DqTQ9kv^|TpMxi9!5D!ZKbUvR(V'
        b'3I7v_9`@pYKf2xT;oo8Wqkyy^!blJ47QmDJM4VnfEnaV~hjHB!r!U+Sr{4xo*lQsFyFvaQkJIa3kJG1uyLH>4Im6$_>C4W>>Gy3v'
        b'H0O=K$LY_3{|#`*L!a;vDSu0pSiKkc0?$Eke+kb~kmD1e!@v4Stv63RH0LNhbCd3jL-0s;Ja@Z!;=H-f4zY9Wn4jQ}iQX7S{~$`7'
        b'!6CzPS9-2Xw_LGZ0Mny-#^Ur3Ty&D+X)-08S`jX#L`!N+c#8(*EORkST_&+J@+DF{pKv_ju8k%-uy7;pKKBZZhRbrVs9RQJ-;!M%'
        b'Z7ywv<x{r38CxW!jun*#yIn|y+ZVSM`64Qud(~CE<#tDsi<#>JlO0Mdnn9%0Of(6c#{(BK^Ic$7i(?3MJj!kI!)v~d+X=+QL#6<T'
        b'IsQ$W<4)HBl6%PIG5M1tL2Gaix{9m#MLek$hvI-ZHyF-3t2y%=DjcM(y5j{Xyiy?k(T!|5g4$4m>&2Bj?r_5j(rz`k*kK`VerH3I'
        b'd0l06XS}|2!@B{;zd?>*7Z_|@s<*D=x6EZ&w>HU?M0YMnC@2}zCSnqqEGA&C?+_C7Ga~upYijAv&++O`5ahA;#D8`>Cb?H=$s!st'
        b'{_YfZ;_;O~FsohsQd%p%1U8_;ol+w@8~9D~dv3-xVn8muEfMKbpdjp!x^dSOS*9>2<Ks3++=$6S3N6&Z2;B-+tMj-gyL2j?21Pq*'
        b'U0SRGr4o8p5k<tpicFWKQw9~`_iIs3nk%x%ml<?DY&993dZg9sos8b4Ul9$wXZ|*l+riOcbZI`2D2kxSlsbRzf{Rk6)KRH~HlO*<'
        b'rA?X#;fC|BZi})sNg#y9Epi+kQRrld2`VuN3<CWgShtEe=Lpa(ln}v+Mq$)$>K~~inpk44fk;&f2tj$0Vjg2RFpke%u>@&Pq8*>P'
        b'77;{45+<+{34`>ZS#!beJMIGaL$Ja$I+<fG6q;ocX$^mN;eM-Srd(&XK8^X<1#4z-qvdJL=OeUIi;|sQ??KlUcgGbsRH2)jW)eEH'
        b'C#5NpWOEIujwnx4cxu)OvJepjt6Bw6hfG7XQy-cJD{&1`Zd923oqE44=1mun8rlRrV)kHu0VSChm(`#k(@I%C5;41he=?*#ob$S?'
        b')MA?9L?)*$BW<n(>BD6TRtDu25akgH;H^Rx6h-KjLAX)=Sqepvd@)lvvSu+2Z0)?;@bZXhx|7*C0!s)TFjP4gmg7ojSkNLE8IO+W'
        b'!?h+w8l5A1h-bM~vC}__vAK$C1Y$8lk(CRXav&_i%qC>?-9bnQcCMZ|GQ!^_U`ipSH2UBOj5ds25Lr1Hs7?!m5b>+^D3EC%!7F2d'
        b'7D$o20LxGG(h-U*-Z3v-<uVsX#}k%=78vg)bMs8AIr6cb*GFR7IV8|$uW2s4xQ5?4iXyVD3f6v$$x7>3eq}&69}hz`oy}XpL11S`'
        b'|9T|WAe@Uk0BeK<0-6xL+(m~4fm(=u$YprQMJt2!v=)1FU5LS)Ln<c<OG6n>bZ-_6eA8TK^nET9Q1Kxw6VX{NKZC%u2x8Nsm%2b6'
        b'(cMn3ch1Na_b)~uJ$OCkm`H7QUJwjg{aa2h%`3ltgaAgrLX{SM%SgEe#*+|O1nmKS0O#}$XM@!o7j2R_&-(cuAbY;Ux&jh)xZSWE'
        b'7~6y7P?SMqF!+pcFJUd4qVW|FLT2KKU@nUC6F-Q!7hNfub?Gm<3MJ+w1t?^0qsxyF?o>rHWiAj$U_<ds6M$WYQWw8j5d@N`po6F&'
        b'8U=;U1$!_^FqcSv81smE26D)}Ii7YIe(T90<8#OgoufHqkfY<5h<n_H?+?bK8b(;#h0?o+p$Dc(&h)h|oBcLeYSD_c^p!5;sK$W>'
        b'E;REn1S$ksw4WAQptm@8MFq7Sc6WcIY|eMtcB8}l_sPp&QtS;B;$<|_r$n189xH#Tm3qEnil{^&4nQb<sSCyxl&1*IO3!qe?#7LR'
        b'B0-ZP1&pvX1sS9_J8{0G){v@{C@ByM!Q3E)1<pM#aKUKN3$hFgTu2oJV-W^rw$e#MMjCf6RDf`SJW-CfOS4%g1QxM~6ON?RserHw'
        b'0!KliluV4LGW{Q;ExVs8?JO@N%t@_SzRcBFn@SEF>W2jes2kUkzGIl0MI$ZJS0n$!P`sak056b3U;vYT%6cTDi7C`Hqn$v1{^W;n'
        b'*J(Sc+e0fHbe=CdZX^T(FhQJ9t3W{T4#IBF_MXXc=HVy;CZtWz3^RqpAkQ%Ti=*Ut&kUxDP1Wiu35;XriD46rcoLSL!<!0+k&1V('
        b'8-~TGiA?i2Xj2;V=rDqXsmJ}uIQRctanm9#6o`8R8ZJDmI7&nlL1GDF?jPQ?VwlZA#Zi(?`NQRvW?K%zV>K4E0v0y}bK9s~8w705'
        b'V&=i&Bf{=vWg4p?*XCrhIVO2Ho0E}|vnV$wy|A4UMoyI(J4fbE)f;!{=Q0_L$--m=haF{=rH`>W_tFoynxAc@M4RRhWBz7oOj75T'
        b'c65x%#2XLOG$bMqpSIh(!<9kbYi}1AQSjm=yG~e`MK%c3D1)lBQIsgz7cwmFu25EQ50xT62?~B3bTQr#|8mCgM$$CFiLZ-iSPl+9'
        b'UjJ$LW6Gx<5u`vt^VwsJX-VVf-AT&s2b8Dny%`@42YqkMSxP;d^?i0y>*<_jPx~5kmUO2m(+n`%8STAkn>I=x@JW^<12dfQp&P`4'
        b'R%np{ON8OpVeBQcKtPNIsQYeDrukMFk7p-+d_WAk#g=nld(QoNuOfs0FwBiu)CjGgAq%4N9&;Hc4*L;VcmU#Jvuw<L?ackSaN%L3'
        b'4BDxVmhZ~2_XaKQZcsMV?vov3mQar&UwxCgxiksy^jIC{=UcNEx0c9|NN+YZcgWDmWcd>4SodNeU)F<5MW&?;R`n?T>}Ak13iK;V'
        b'v|d3LMIbSW&Q8L&fiO0CI3*8GYLp+dyH7h1bsJbaR%z!u+a%@}T1%uGC*oZ<^G58H1@E6<)hKy<%HMXX?}$)~A|lj9QY0_7K{Kl`'
        b'3`t3)q`Z8&SO{S)&<v|GXn*PRIPBgkNq%@(SKDQiuM>3Yw$cOQqm48W2dI%(g*<eCUIPWV4=;m;MZ^@mb37HvD;lK~K0rMN1-_#U'
        b'I`z(heR6q2la)Trn7(c}S5|;OTTvw@kdawN1sXpXUh1#@)OCzm1akCw3NSn9``{&M_f$VFR)W|p?S5H#n#rtgY<Rs+c0h=N4mV2t'
        b'l3;1TZ^WMlvHD#3`QJk2DApGRH-M69`DpkUld-GutLjaD^RN^pE!nj<dA%FSt1zXbctO>WxgCS*78ky>$TIiBOwroXYRSo}eI9Wy'
        b'T{dZ*rg$eU_*Hi?*h5+CQ9Sd)WuO_Js8w1;mDyZkuCezbrrP#L0;vvnKdIC)SwRg?J@tG(VymNIoK{Eqcn(e3YBOhM3li5<(2muY'
        b'v)`gY#sr3}aQw}?`=FxLQmBES?=b@+fC1V^v{N*sJRb^X)?5aA!Y>7HQ-WD_eCNp1KwHPJFN<Xu>abyds2Ih{5!+5c$8$S`FkT|3'
        b'k&$($Vd!ZYKcm0=@nGwgKcemx%2hc)GKwr3aGz$<&(4;fy*1;tKXmB%doAe^F{F4l%55_Nd9)F$$)}}73<9^M&7{?U#U!tS8R_^T'
        b'SJ@<witLENxFosCnl{s_ReoY5XCWT%@lBH+2O~h?goFyG-&~Lre@X?K3GeMe`W8t4D@Y%V(?`~y_m)R=+zNRiJXTD|AJ;K5n8HJo'
        b'kxnV|OD1wVhR@z|dbJdrObFT%OA_*YZyF<?#z?U3!)GH-!;A)PJ_c=`HrnR1QRhPme?MYU=VLI*_{}AXK+CgEn2tPNzIswmhk4El'
        b'IPv98;>*0M2YUu|EIvf!s?{1Fd_LiKnFj6~wO|)A6EEY11e3;0zz#)B8smEzg*v@%`4#ucFh+VA<^dg%2GfOJk;cE9!F-Puy@}RB'
        b'0~qqME-VWaB4)A>r-E_ihizJZ?g3@bGKl-axoOBb+O9a9Xj66OJTdzLVYbkjC-8|*?Jv*)nd8q+P^|g>q<AITM>xK7a&9L+>L<i`'
        b'{C9nv#r1a_Zvo>8&vtn3HK6DoCs=i+SZDMZn5(hz1T$*%pRid1vnx~xwZT$F!DyrZ=G^p|6R1Eh(&F@=Ibkl;N2hrlin(dgC!A>d'
        b'sQdUh_n*hPKk>Su3TzP?(mW2u^0erWop>GKad(b$A0FpEi1Q*fHYkwJX^O@aqXlVtQ5phaFc8J{i$UFo5?~GzV9o1dwXpE<Gm!cg'
        b'r+$Z%+mFcss~l6BlV84|=r^H*BoYTvVfZNE_Gr-Uusoyu=`b*f55o+A56maQg3^D1;Z<k6a-Y&s0qYJ06dT2GyKs4!eleJMc33;%'
        b'H59Yf2`i&eg7mBuvsG!?iZnzx@ro-u4b}t61n__e^{|=WhhO1LuXO5?6srX(wRfd&ai)Y%Sn|?j>J~~wFWJ0Mq@F|^Ax{bL(IU48'
        b'*O~kZ$We(iy2QCtO?K=-Op!CX*jdz!(yfs9cKo-NOin><#m=r`C!ent=WAQ$?0VM8?ZEDxL1c0*g0asZS%ycU^xr!1VG86dx(%fl'
        b'LP2_bD#KOqIn$h7kHK8cz0CVkoL%|Og|Y|aeAzEJy(c*Qg&^LCODc*)ZHdmV0_R#g!4>oQ5}aMjujDgdmCrnuFA$|a0M#e8O>=hL'
        b'@1!ERC-}@!&aP!wGC#(Lg*m%SPVU!N3NpP(bE`*7!W$+0$x^VhdA^g1<5rB-f$s@j8l!6NXaV)a+e+?1zG%I(OV3xwW%2&m&aT-`'
        b'ZV`5S&%N&D!)H3XW;(fr<HGOZ!)G|VW;nT&ap9?ac#N|v#>pARg&X<s+nrsvJGr~C+e%a_%?Ii7&uEVycRk9vQMR3@R0&a~<nH9d'
        b'!<}8>PEI$jtULH{#@WR<IqkUcC_a3$vum=G3mX?6%7+I!y8@lutvnU*N#(7ht-v%f*U{x~)7&IJ7AVH4u`Aza5>IhVKE)_mI~1@G'
        b'@NuR~oJSv5K9%&;V+Vas+`>u5a*9XkTqkS^BRFz2-|@E)Gd#o}4bBpIF44^}pp7JBAJW+rv!tW<XbgziHU#VK=z*b`EPaRf`-oh{'
        b'keR;_fZZ<*ZR#BYZAqz$>q*u=dY_OvKg8d^>M9$GGSC|p=Dp9ge8h#UJZRWkPl_3&UMk;CweA*iUkx3<EZlT@2n-l=nc|%)KPfVo'
        b'XPZmtO@A9Qml(=nDR62?(Lj`UDq0WHhYX>FkS1iUGy+wD{}TM7&mhzoj#?D<I=bFaq(+`gA;na>nKKkqn!;gonXbH2!F3Mdn5O2Y'
        b'DjHvw+0;H%{Pr|hf+8g2?_O}NL)fIO^OGS{l=BAlc-ASIL;U1bNvKnO9Zf^U??^q@LW*<<Ira?gD$z16L*8YJQp+_B!8}tON>vi&'
        b'__oE@yvYKEGOrH7g3Mg}+)QhY-BsM+$J7l)zdQuFK$mHVNWncFa<nr*5&g<gxs}jWDS$F11S}pOZrD|K*QVbOaiv3X^^=(DD_JDL'
        b'Oyv*{CC|JxE>y(u#VQnFW}^-t6#e3m<zS$v(DF*U3LnQY8;AHsGS<VM>q?lHnJPr78cD8r2*hWh?BrpEk`5OkbsEtvL*gNKgdf?%'
        b'@YhF$C{Ko_3B59a&+UIRbmfkz=gvis(>?BvX(O38;vSWmM}~mX8WR5S_jU57BTM^HRzrRH@Q_W5x{sL;p7>$a5EUFbi=gDr&cpjV'
        b'gWsAqp==(srza4V$cpf0<iVxE?;c-(sNmN9t#2>g7bM^Rc2IGkpenUQR#}H{0`YbAOhpzgQpbyqLGkwvwP<|5J@Uh%Au8}Mi3BBe'
        b'?tiDMGw`jcB1)PJ#!%(b<Mm)jpHJAA`nC+#0JcN!%x{oQBdn6u9Mtv9LinQ2@ns0(I4V)q(oq~o{Sfrml8b8Rkod}umnL~GcZ*$u'
        b'$u-T>Pduh6|2Wkx77|UZfpublFBgO9Myc$^4SM}LOi@T@VI(n(lx2zHEfe<L0+btem!-`M#i!OS;RF;Ie%Y;l3UaL!%=3$i_2P6I'
        b'P)jIL!xDKzZgn-HtR;6+1@lBDldjyI-RD=Qs=egy{C41O$|^V_v@XT(@Laib*G(dBB5n^<fxCFt&B?JByZ`QPBqIbOaMn)60ku=S'
        b'dP8_MFMC|>JpP~o)5SIDrOS8jYw1GaZiL*JF6Re-N|%%^zR-W@V(qZoVi%v(*0JA-HL_D8jpc|Cgbv!jQO4g}=1@CJ*cc@wZ+(rf'
        b'N<U<%9dd7!Ri+;_ymok{bY9?=M+ufu%*@YT+e-OS`D<oucv_H<KuL;JsPHr;iQGJwQbi@;7YAw>#jY)ZEs?k&OOCKAy{FG@HB_bp'
        b'N22gNSjSozg+_)a56#*UpYOz;n~_)A0`}ggG|URnz(%sR$KCmP9ScpC9T94B`E+A?SzQC2L+ZmQKCR}ku1Ad;1s#`x?%XSbWB0qc'
        b'R|g&SgEom!y$sc8Q24@cy@L$mqF)(gY6dL=;cM19LEijtr^!w_YwQwk^B~XT&Y+$iH%8hIMd1s+&6K%oa#6i%bWFZH*!=RKg})tc'
        b'F$#NTe`~W7l*C@L0equ!UWO|!OQ@6N8NT&~HIhB=dB(Maqyj04sbquMylyp_c|xo!*^v2!I5SLC<Dd@^4GuOZH6~|X&mCu&!olGN'
        b'3lSW{#J!u^V(*?x1?_JXagXC>ws#RN?{_zfd*+-uxvB=owR91R1~d1FrxRsC%)^6|drco=dS>sW^JblyCKH3iu?{kM$n9z8iYxSD'
        b'@&+{|mxlxDN5=`5iM?JKT{O;Z8s}bk#T}hFm`WC2*6pCVr8u<vS!L;t%9--2s+pPdMEkTS<z4p-w*6wz@r%Kh8pcyfm9|dx@MRbk'
        b'HtoeUYg3h?*Q&(6Rp8r{Jjm}9)JZ7+@E3X-1>D^@OWAT@b(E*+l&}ao19hj8@v7(VExc^1rMU#Y@(s$;XX7j7u?dyKewC>wrCl=y'
        b'+u{ZtI;cB~i^fS3QYk;6=N){Zd!SH%>}nL|{Ro_*1j&Qm@fi=DGQRKMD11Ut;K#8zk#%n2H!u}bqDJAeSj$5~?p7RHr&<ye+w<nx'
        b'mfddr9>6U)tappjddsRRdzG@<3LPs*g+I$u3;XfU(ncYt81yI-uKyA^fOg?Oy1iz@PwN(V>;7!C?oeE}`;xcr8R4&w);)OXr*-FQ'
        b'Lf~&kK?q-aM!{sLzW0*1`cFrz|GTGp&<zRcOVcR<6|_)5r)@CJ+@PCICnz)DpBh6-3Y7L(1vOo_eDf@Ef$HSWwl6QW*r#%5aUoP#'
        b'J)w`KmnzS%VjVDPE>$ig^3}m@CvXysoqQ6f%8sQUkf{%kSe2F>;NCn&oy4XJ)vvHtCSFyLO8J1G#%&=xijhWGc=`EUobi2}G2XvX'
        b'jG?aCcw2C6f{km%ff{04MpRflF^{CksJV$3qZTo3mkQFOHYA9*-MMT!D5<+4a53}lC2RUTQPgwGB%1Vil6mt|R48PK?fBH))_f`P'
        b'c`Ar|6BqZiOr15^QFE#AGPe`^x!+&XXflm*N8P0-HT97W`=uzKI$2a)&wV`y$oac!NuutS5IGQ))n063Y3x{aaheZjyHpn++)y76'
        b'CM>rF7u1>G=)*mQUAgTFO0qJ##86<Mf_7#Slnmb$(^YP^KdH#PBrID58so5A!%*s{NqGdFkKeK+v;Rk=(`=^m6`5!IGWYnIHMBl-'
        b'15K|hTe~KHvre}zbJ2w^?ou0f$*~@Y{TBBGuBkvNKILwE5&}YMU?ueQCEjXLYbQS6-bfW*ZqE^Ot8th$`e06hB=fjrp2YF%OIE|m'
        b'<x#>C|N47Z3$4+0OQ9P}8!2u%PO1J{?6?mT=a+mw(y;Ur9;naO#n&7rY6=8c0JCsZdxt-+;!qBEFP}2`V2*i*qBF}JOD81HlEGBL'
        b'nfL-9MZn+M_uU1I)sPw;Y@MGp4@k36+_BgFgfjUHH%RI<oUr3t_Y=%QpVdCe@4(>HucJXq;tBNzEV*15PEnQzLz?AX(_tw8!L8o='
        b'mqwrPx7;1~Lyo6O5Xp{<;9?!3j$ZzkOwRP^!vhdWZkvBlAb+j3LDBin3BQN~ej$>-#EaDri1C1oIFd(c^H2R~mB-K5NUQ-GRd1y-'
        b'bCIaD#E!q+gW0YLm@3eDB%mO`6A*G$fK3y~OunRRP|{Tjdp!=XDF{6DtIvKzk;!M>jlQQOMPIwAAaGN+4lE$338nn_wL!u`X}4Ke'
        b'_}ilzW%mUI{XNe6jTHWzlNPqn-z$Ix<`-~a2@bRdG6KFDD_#XaKz(3QkEfsb-7`|1C)S9JA4&>H?(zUotMD?=`0v=IQ8@+%dTmPk'
        b'4uw^%t%|>!*B|+Q@lZ&-mHEQ}9jma%;vy5UR?%3a_YHV@7-i+o4e--XqwrlL_ZfC$tBbXpwK!?Kgn4~jZVApUiEbFpEh)O-MqDS('
        b'CBEp@y)Y~Sw##&t8}xM>>{aw|0$sBC{5k6RMq%x{#1R>f8uBsD(e=@Q_e~41&JGO}SNp<XK7?aBestG3NU!bI^A6#)BOE9uM+}-T'
        b'#*Pw*o;QhEvNC`D%!dqr7@%%})}#vOr7r|+LP@qu=!y*mL~)=`+)klJSZw=+;mrX|Vd439LnEZt-`%>M)K_dM*RSjBGwdGFFK%5('
        b'no>6CP3zRPs4~5{iu74YGCKxVgyNg7UAqR_b`3b{23qV(xfgK@b4h|#5jF?X=EIO)QBN{k2PknRQDvZ{8>MvdhKhjSSPgM?>-PyQ'
        b'a)J#e%(YA@E5FFL-`ab}o>dKWIJ1jgVs1^!KD7Be=_zRkerYgRLzgE-aTHk|xq&WU7ksL7Wv{i>T(P0-$>0~hRtJA4p?s}e@$Tc4'
        b'@41{7IT|6lMZme>eDRlHxP7jP-0`*flUA4nr%C506&-MU>;$SVa-Xv6se!hq23i~<$NB;8m$(N<ElOtnKq*^ET2=U_uEh|ykLr4K'
        b'pluB#6DRk(5vc6ySj=z%zh2~#HozPa>h1bXg%=|}lu;@)Ne{!3ZFkd2ib@}5`2Z!LqZDy95;<FFHM4Xu`>ydfCFLc1%o~`}q9bIZ'
        b'kdl`$RZ8wY+ypDrf<GHf*QA0`U#X-uttNJ^wyMg9Ufc?*b>rDd0xXMGA8pldG-l17BT_n)X#|ncM&Lp|Be*nNObf{uVninhD|0k_'
        b'uGU(DOQ=+eFSvOf(I}|B;4U1D_z=`JZn4!Nw<3T1Yp+vqGx?^7DYBuiUTpQrg512^ZJIGaNe)PB?0;Tgsyrx-+$K2+D&u)gz~tUw'
        b'>+@C2w1JLcH_W-^522$Eq3pj4xG4kaQwF}AGGJb>`?iPE4y+`;jyE(*296MoA`kd?_=vmGa3cL&P93r9mXjO{qF7o=$<2E=H<{P%'
        b'QirJn$gW!l+HM6wd&+U^0N2-#%^NXysozZb)%2ix0yJR3BubY3)aK#}-!An)n;)e8jkpg6-&(tC#a?-rYM^ZbgcU;XgY#ETI(pVm'
        b'LF4s*0Zh(5PYA)aHW#gV2$}yb(1;=fs4ky@HXq3FyN=Utq?sgVqb8k<VgA}5C0a9@wfwB#N-&i(?C!`nzv&w3Z@b*zVt=LMIB&;M'
        b'q+_VR+1Y=D<j&&e`mCA&W1Q>>JVV`u7t6Pu31$-mift#TcX|fDq2xWco}p%jV^=u1WVM&TRXh0%71T3;V?)kR+C1#a16NvYKaLGP'
        b'LuG|yS2(y<<@Mp%pfl7{JwM_cP*G_(c7=nhy7nT@5pafT==lN1-g0JiEl;ll#o_q4zxhx7M+Dq{Pg})}g0l9!;4{Io(8kT(IBocC'
        b'XNoR+^e(l4lGn6LxEh?8sw^QXjm0Pl(UhpX@1!2+=MMCbdnfhne(s%d{vNzDfcF7hZhj0!ztP`mq-0p1H45^|zNXV20tG1Kn)vbq'
        b'`Be!lGR{AtFWGQj!`1hv9o{FY46th6Cghz5WR0*Cv*eKBuYR4`a9Pi`iqC_dB#Qpd^MTpX&yuLq$SuZ&ad!Nd(f4nwW@hzA1o<<S'
        b'{Sn#;`0q>!^KyTF8p&+wAGKM-huxb__c7)D_NvxhEuu}fe&AfQt>0c_0Ml|;j2|qY+Ft0NCfOAe0?j1NQ5z=rc3YH9?Yhzu5RgNX'
        b'=h-4q8Tg>-owp(2guJyyw|6oDBZb8?1E!^%(sIA;=O>$!S={6ORG=*t<@LF_wf*LXR*OSu*KGFE4J>Nz4}Hy#_S@@PYwNy-g<!d7'
        b'?XsrdyQufB(O36J{~DXdbtLnve)}tL@+)>qqGJ_$o05LxO?wpGWTUB|^3o0F@^!Q1ork!G`pp(yla)4CZz!9`IQpXPeLRm05B7U4'
        b'aW$?4hKG5hFgmLrPtqIA6zDE~#^V$?w)^jb?(c+ci~1vfH~EyH<rTER8Q$Bo?b|QY`@7Qno74N-?T>KjIOTU_*Zh7+aKEf$z&$D#'
        b'RDfkJ;?nvlsa0Z?bjI_WI(3rBAgV?p><p@zi>w-0CT*7_k9c^i?}x>Xp4SE>H^=)sn`d!+zlOBJwATrW34uWlIft>{i;nB}tn5zr'
        b';beE<67KNkjQ0Lc!@mYizecDbJ8NKK{;ba{ycSZ}d9IG+G&lwPM&MtTB{Pk#a3f(1Lq?%QeJ=r7I&l_i6?ZEyc5h*y{_g_)LSc=4'
        b'ITyqWc96biGZ%oJU?k!G7!>`y^|BwQPM7q9AzUEJR8t{xFai8=!g^8X=aAq{oPb}GAk-%9&s_y(IuVm5`RLnI;sfHuwAvFrt7Y3{'
        b'UkduW1pUndAp3FdN4`M~dE3u07yGEmZSKAUzR*{9pQq2?<KK9Z)vxKG(%jkF-Ki|?Y$U14t({6r&Rz1vQnQx&QNc|gDouQftj?xR'
        b'CFH#@z6|(1#s3Pq=lLqhqEFpXYUb0vm}Ch={@I)8jHk!~zorglHecMTPONLOKKQuL!=op08pDTuONE^u0!<(HbQ^z8r8Ad1(Z>t@'
        b'0iux%Kk0@w*yk8u?bn_(q<FwheFS9d!2Zl{dAoXrmuxTxR0=`Z(u7uNlx&&y<Y3K8RAWcn2ROkl)nv%m#yf2~Dp)K;8>N++%o2CK'
        b'rUQ@W7SNY(_SLqXRR<AYzR}n9Mql%*eeI4Yu9`2OKxL}%<8Elnd{6(AKXH5B>tiaRUwDl=7e{a}_JNS^15y~q`o+~?=K&)8Pwvjc'
        b'5ObF&MpQKD=G$w5!UOV-;yt42p2B$p6YB=2n^KLwkFupNeM?`OaU)5oQr^Uy_lC`VIWP64rBahp-XbWGiKTr`Ph`sb3@`L)HIZ)!'
        b'HIJ%~`7YhC^G-7PPL%o(Q`T4T=+PvlHmod}vG&nn=F=Kfc05A;<RicBi-?eLB(D6CC;N^GBsPJtQ8KlRlBe#dQXb1e-!NQAp9e#M'
        b'IhN*Isr*J}OPgR5L_8U^Ogk@YqwL+cvlr8uwU;#lHjUE6My0ZXu(BA|E{G~%1>t3DH3igMFr=djLi{K)?j-@`mrw~Ed*qjWMPET*'
        b'bMpI^lKU2!GLOOk;9qsWrChbYb-yzAwZIiqCOCfCXMeS&>Ah(CPNu24)l_xNmP%<<;<NmIQPFoET2-pJv_48zTr~k$WR5j+i~8dB'
        b'VKULQa8!qS_O!t=8MmjsDXkBi%hJpz+@pJ+TykG`lG0>ar=M%qSzA*!2OH-0#n=hFOj?c@Ltp14MvrqP;LWHy!OTj$f|1UTE$Z{M'
        b'rPk@@68bjX**Ch7h?45{>!<+c&c4hr#7xKGC0?8byq7wRfgHjwxts6kJAzHm5kyHMD@EM)AF=+eR90`Uly)WrTg6Vdcds>k2ytP3'
        b'`1oT7v~bsE&>H(Z?RXp7A@<Jcz%)=d{OS&IL47v654dB%JrTE{O2SR(qXKzX-i6V9eNNd&Np&TgN81;ZB&0_77we1^Wzh!VUD~nz'
        b'=25(e2xH(thAcuQj9>{qEW+ZO-_l1JlZV}iis=AR&M5Nk?b+HbR4^qge|3Z1zV7_zw%yNE+rYD3c0Q=4eGP<B=QqlCy{oXaXM>5*'
        b'G=+XkLzYL;8%Z<fB^7|D3S7=84@cWD>c94PBRTa+iY!h@nmVr{o)m|nkdlgknBoK`e;>Z%93m}F5K}`H0k=)=4GF9Wm=O|HQTZcf'
        b'!KP72eMLY-Mf`)7gI^A$enF{<2HZCLa}@!7kUJ6bDW-l?vF{Vh!M_Zowoyh<Lda%+wxaS)>LOSy;I>u-yjh$u!DcV22ne*<iz@<7'
        b'bo4+GFH{7GZ1xw$J#H$d=u0=nCU<-7u+K1z2P`a+ioY6V?z?inM`_A_jPMJh{9=sAVk9U5z7z#+96(r%Km`kUBoGy2Bs(ti^G}G;'
        b'Lz|7G^QOGA+^Ps>#lu(A5N1{ZJQ6e8>fvjEC5b1jHx3Lg3z!Nxb}aq%!Za#tz-Sp(zhG;LpQnD!TI-`@;pBiuWEDW9VC>uj^7*l('
        b'&>|6DDG#Tktb(I>1Vja1Nsi+RE6uDz&SFcFF4=H}Ml~d|2?*2>imF1(OIxWBSaZCK@5xtGi&$97&PC(s>9uV~<)^X*pJK3fLOl<4'
        b'OF_cN=?+Z4$bj1`tq}>Lfq6msff1Fd6lpu;d~04{okUaDu!BDZ=pa$VvNLZjlSHf(MLhXe$gN3@$hhsT3@XAVrS`<BD2nVDa%(Dq'
        b'b{&`SuL{8gq^Z=9u(HADM(v*r#Dm_N>ZO6DePBQXe$gmRjFif9(EV2YHM;GejRj52)!~H~y?wui2J9>7s&PFU|C4%D*N?Z@9yC|d'
        b'>q}H}YiUi5>|k8A*sNQJ0a|AD7J0|*wQU@$%lmt6+s6F(bKYK=yf*E%WmS??K!j9UsR9$e%3N;Q>^;Y+B=-p@$=<-wgQ^pLl<Mef'
        b't+OQdn9YrXqgCK4kJ;S1zg1VQXtHcBAH&a~Euq0yDu|MTA+3#~>6hlSo;FBIYfAT2%J#|UTbrtMRkHlL??&5E2ex@}^~6fmMp<Wx'
        b'm8Dc>+lF%UI*;%{d?)T(oC>T_uwf}x$LM*Rg$=5-TG&bElGd5=7FJyzd%Ac}knTAH%mWrSkWy7!@kfzaN4$iNr9qi{>0u>de2`bh'
        b'hqcDmt|?nuCn?@6s+Z#M?UIc$P{VkPsKjZTH<IOaUqyqI4G?LQ(qeVAXKi3nkv5gs9NVfh_r=vqVpJlSU_cAOG-1h*cxa3F1yy)1'
        b'v8g0>dtZ5ZAB;3eQ}K?(rV^F&=~)$NW*-_$Z{gFkDhWi<bRTVP9a~&^+I!tHTc8lWSXL#X`C`peT4~(U>*{&5#v{8ong_<lf>*9s'
        b')}K$G;PvZRBEnDh+T4gxWkhTcgi!+BX_Jmd{2Ugm%QYcz!z4z9iih0PkKTX*{+n5(2FB$RprX8*yTo(eS*NNbyGxZbt(JrScvq!_'
        b'-&dsKi!a_n1)S7k(nL)+oBbmKd?GZ$e6Yt;OZZ8y$g>{8I(1AZUo&p*2aaDW|5ibzU)hPOfU<8&q*hjLEdfzQRb=vIcZq7$F0iV~'
        b'Bnbgl6*N{-;%6ljRGpFpGM){NO<>2$iK)|AWme7DBJ?U<!nXU5>Z2G<{FOYK)N5&N^{Whp_Gq9zfj4Z=&qxC;B}-H#W9=LD+wAU-'
        b'*pL(Jt%52N56hoR1DalEX~$nLqyoXZu;KTq*!C}AGAZ3quA%K-42>LQu|HktjEhgzl~31AH}qC1yJMA9{LB^<s7G~<!a=)LSNALI'
        b'Npje&3VkYF!}`zr)jVP!n<{Jhh)%tiT6l!e?KgJ|QJIz!B*b{{&Zq2oIM@E$lo|Q*B>fu(DlRT8SO1bhZ=c>>rR;4`R@+dJ9u+$d'
        b't}Gld7wKB93hb|iI_Q#>DSo2t<>u_=h84jy{@A0%S^%|{5S213Te-|~kj8a3?K8t1*7=k?>43Q7Yj>d&S4_!9bujenh!FQo4O#cG'
        b'8d+1UGUk1~#yHitX^+`^qRr!qJ-rcxEG{8L7iPeh+pSiKPB*<bR*3|9vu=}4=bs=P)j_JVfS3Z}`eOAn`Euhi>zV3D_4u{=-qKz`'
        b'Njoi*d$9^JqF}bz*4N=J)6%}~hH+&!i@m$l0s>HMBd(+v)5kV@ceM>Be_3&rf=ZxL!8Eqy-Z@Lc*Nc@_DgwiNkRPi?`-wCoEZ?MP'
        b'X;^`OkqB8PiQm%rT3+^vkoYu;x&_G2(itBX$n%fSaHR?}*Nu4E4*8xYan2$c;<I+(OTBz%1)o`VK(uBTJwCq}=MVGd?~Kt1)h(ip'
        b'<TQzmgyu8~Is_=VVQ-Zz^G#O?{w8YjMARZfnOj|*E31Ulq!>&vxUxlpPDvXD?K1Sot^Q?O<yDj*W*)+~|4zw26XN#}f*UqUGf$2r'
        b'_j%SG)MU>oM$e#oOea_b=>Bgi0>r_aDM1l|rfjwd2+EI=*ErDnQt><OF$+-eekw@U&?<jh9UubZe(ERppAwU3BbAKM)Dzp~r7bn{'
        b'QM(icza1AM`%B2}nTf6<d`8eNB~EwlP`^G>JoPWZ=cZJd-);T+HG&FW|GYTZTH0Q-0CoJ}J|LYY=f_isq=d1Ol*n3eP}oQ=BbF(b'
        b'MV}%L;F~cTB~^gI@I?6qA`KCBWj&*hz_U<+SE#OMM=|({c{$_M>6~=TswRU|CvbM_oqEBlrf6sOA}39+(jliV+o@aQq(!UrxvO+@'
        b'o%Fg@NVkekUX>l`qy?+itXtK}IGdDCq*#?5=j<h&-55&esZmTKn2#M~S#G5TV`oW6$DIX-;SD~GDoVi1d=5H7CJ^(K_<ZbPx%K|U'
        b'A6bVWE`UtdA`Nwd7*xfRy}wsl{hamo2Iai_@h(4g>(SGj@q{CL_{Y}ol{!|@?K#bo9T1+M29DEORm|>I)^68*ufX0_Ds2N!uZ5&I'
        b'oz_{US->B$Wo8KZ1Hu5xPgjM@uz61m0}8*=RVh3HowGoO#VE#ZpNWsuDm6{Ids}w5HodLT?Z<iE*6<??=0CsDV>R9jMR@9ysE=Ic'
        b'4<=Pj<$TT-MLD0dr9hQ@&dslVq5tn{tyzheq5FFSqBOFDDl6H$O=%4{T%}2a#=f0ZZ9NGSgT30@h_}bpjf-yamPnDwyglTx?WOar'
        b'wu8f!(#!;22yB5wHS3Aj*)Ep97>(_k7ezYum{v2ow|UKcJP;$Jtkg2^dW4b;SO!8Q*ml78vXYcDlQs%cD!qE6PNJ)9t+v%et+1^3'
        b'Vt(D%O9@hCA2ql86A94?OoB2d2jwNW7Rnrpd!KJ!Dr=ua)W*A3%N&b(=YuypiH4B8IM)L*$1i#n&9p^}Ob`}8gwJr<ljt~qA5Sp}'
        b'M11rDsSXxF0+G&qui2cP%IKTcRR~3T{k{68>{Mlp-K@8-i^BoS_4e#aqP%rooK#d^zP!9O+i3qJZ9dz6zB^H=XDx?g4R`k1>>bsW'
        b'Fcqf7c9$q;#z2WobZ>W>5{T50q_skC)2znb;<Q-mqS3C1+b0QTtF7{+%<0~HMu@uo)C6iGb&?9Mv9IQGd-2BC?D0Vl;2=XtZ#vJm'
        b'cwx?_3#M2sBnd)8U@xtE44g}a=2#+ovBKmzvla3|IVy-<2ch;@<!FRqLT~y+PdPO;2+HB8Ui+0y@sf0Dukm#pG4A-c62w$rrSOP*'
        b'l_%r})cd97LT{C#dwgiu@P)SF3rArXctg3N3w(sBN?{+La9nYlF5)Enq^A7}yJv9VlkqyKzCodD;LpURe0=YIMfa8XebS@*6|Lja'
        b'OAZKn8x-B19G*%-o*CB?Y67*8x*ro%%F}q^0YS(!)Py6xI7rCT_~?c7t_wVEp#SNAx-dqxBNx8DNER&uno<G~w3aqSqcFjcr*Oqp'
        b'lSMO8f`JO+`YzyYPyX*L8KsTzlgGU8s<9IpcBHG_++ttO{Xgv8dtg-6q3Hj4Bq5n>aPlA|5b9(gVR(2tNe~j$(@Bgm5$y?75MR9s'
        b'7>w4oNI6y8oOWiSFahkD1g!~TI}=S!qLC1+@-Ww#U?YzNG65lYrKMDk2paGSQgD82?U@OI+Md(jy?=f`e?a!yYp=cbYd!X3&CqG}'
        b'z2;4hA@Bb_tt2^4omO9B>A2hE_)z}Y_F}8!kvUpL->%)Zz;RqnPyJW9>f@`9T-A4#JRd3?ht;4l%GF24^o{AdN(9}N>o}kWMk}+F'
        b'aUVw?iSCQ(8YSZ%l))DbM`HS7J`M$a<#hyPU~8SDSN?y_yR+^{^pnwN4z2U8TDR&+!|dz2USAjGa;%#3`*yA4Z8cqkqf7oDlcdQj'
        b'$V$?!+!6HFo>ta&X)`rnZ!iQ_o%Xv<dtIkHJ)bz<8WIsd)oMOADF2~6)TNiXcv(&4M;G<tw7w@4)FOkt|8ZK;FEVucQ^iirugITQ'
        b'`PYk8QTH0UQ^YP#ZjY)wf6>!ynmt}G=atO+a<Vb6LhRS9WciB`U#gGkz4K1Xl0qC2SyU9{YctPY6s5#>Pj_k6QX=!qi=G$MB*Z*d'
        b'f!)30{;FuZxbofQTeKb46_5NNx})R14y$@;H;PNRz;^oR^9kZIp3^2S;agls+Y;v8e!9)2e4eiVX-&+kYxNU~*1N=N(|0T~bZNyZ'
        b'MA3Bo^u@IXk-qljlI*#suWPZjEos$HcV(BJwz-zn>W_B@3vNE$8r7oD><nfXpKjG>-*j5J?Nhy`Z?rg&>Q%l(?vU&oPAg+XusBm6'
        b'3I%^(2CrIvcR~K?>J#dzX%Aof*|Sb7@{%pp7tB0;*_?vxE2jVDis|X$=^8m*8}-bmy5c7^1yfGXiyA)r)rh9+qfK+8twpBnjMJm;'
        b')5WZj<#maE-nUMd6&XXTK07pTVrU^p>Tt2779?*k*R6DF3dWtbg+gQ1(8BiM<<lE~DW(gIr-y^0=8ZY+7;|}A^IASG8@bfHQKv^v'
        b'M^!gp7X8IfbumBE6r3Bf<(dli4vk3q)1m7B8ZJD~4JigSxI7%<P~_gO`)sJ-Gr3S+oa57>aBkz&gbU^kjmUjTZ1$-kYiLiX>BkkE'
        b'7%CeXf8?gd6&$-Fu|Ex6KL5Qd<{!Rd{=wn-b#Dz7Zv2xPI&zV?hd#e-vS9o064`GL9TJCmx<-Auqk4rc)XdO_Uha8wDAMc*O}{=o'
        b'oxN$O;CDmnLbgytMW6lBP{Hpn56b8qQuOL`fQ*iz>d(SY1VSgvQ$wOA?)gbjQ}AnfJVqS)Ce7v3qUOyt6;}rf+%nreZqXP}*P=Ww'
        b'*0XYdxF6zuVMvMVGjw{Qf4XL@%P=K1rME$J71wW=s(t`6p>b}Te0%IdP_&AQ!+jg?^B-5PIX+_C<)>sR<ybcqe)1{9LJxoI{&VPe'
        b'mS~6LV=+g49Fp>AuzA({nG?Tutd_A?o|EmMj#K)Mt|+HRYxZb5EH$Q1Q%22DyRLG~@j9p6GtM}T=uoHR1w#>KhpnTwrd?;>V#*wM'
        b'JkxzV<7Y!=on~#f_pzbl7cZ{8#Zf6&sKhIGRbC@X)IYBn3al9F_WXR)iXq1va+c$O{CDm7<JWz?w(ZY99tu1pW;=_|2Ib3weR5vP'
        b'cx~pKuT!>Z{`|mDpi<1O?KvH+Eb9`5cjcw+bZGuY`l;ErsGBqzbNFFQ=$=C1@O_KK21{*H<D>>lep<d|>W%VP=_cexp8ABIIqBCp'
        b'm&Q$W6*i<cCgo49os^$?WyB{9EvZ`!uW$Xb_{-2SX-RA_y9yhpwWhVCPFb&QOjY6<3)Ryv-hAm)3_lxMqN%L7*!<wd&_O!dkl^^i'
        b'pxL8U+qF|;Zz>G;{~k^|>>qb{@y0XDdVSr!SC#h~eNDdkuSAvIWf#q$A4V&&_ji`(kInJ;=3JY9Q?~g~>C^eq*`p5^zVg;BZTXqi'
        b'dh2SVBI?QZ*axn4eCwdtYfl>LVh(#_4&P#4*5>>9V{Ui3`x&FV&9}O(<ff*|ba9#7+?f&x4*G+GUd`c7&rsz{I%lzF!qT4igN5A_'
        b'tTT-d=pIPSH(wJS*;k$=8q+Dg>6)mc&V-EMK_zXqS@v$!zL(>k!SK7@4$X7=@+F$y?!c)*|EWRmM}xO+Z*JC=EzxA@b^Ryx%TDPF'
        b'P7MC}#Na0b?_?VWZ8uv_9{b?U$xGvmPmZ!GNzP-MTJ5UjPv!T^BLlu82NYWxH?~hJyRVOF9e)~Bzu{Vy{L#v*G@;POio*pT&im?N'
        b'G51htZbQXj!HIe29$xj-1p7&Szst93YkiseqELH`<J*JkquQPfP4*uKm9#l|g`&Yzy3S@@v1(jG%3m}A|Db>Spm+OVr{`zQjk-d!'
        b'R$MpBJsR7iHM5@?6WBKBe|6CNs+jxp=4W&{p097-JSOnkp#POY??w?=UHNO>grd^K(CR`j8Dwu9l+Ef~i++N6s(xvrlKt}FEjK<8'
        b'6&fV^n(#TZ@R%mBVbK5Lp!YeE&idnZI<e>7r}Qq}s<ec_^Miixp!e5e&Tr&*L2jKZG2T_1*xTTE{ZOs0CtCe9+Y?;XIVR9J=>PSg'
        b'ca4bpLi3Y4kD3vYj{CW&j3)<0$>TQLoo3DNQj?rJgSEQeEg7|g>+4(M93LJUes8~BmwC%y)%Lzto3V26);G)*Nf}Rw6g5V#DW@XY'
        b'Trt)$Ri18U|E)RxMeW*7v&P&V<@gV|Z)ew^5wS93FGlXCXXacC_q*a3+;w~PTeby8c>*t}j<qi^-Z}hTz>f#jXPWgTn&D^Xj%6}I'
        b'F=zPS0guMN_MJ_YgWk%)feOvV(aN`)Z~r=L{OG{qLI2`G?~=iLCS?91l4jj?2fdXC{c{ekuWxG-hw+&=bWV?EQ|m#|uG-eAq`v-!'
        b'R*CgDAMEsKUwlI+Hc!5DV_&h*qDi?^x5;%-Eb`)ZxrqEyE`QKF@tyUed#atXP2P8Ot8vvQo8fOU&PB$<uc$xR^gB)YYo^N1ukJN;'
        b'#WZ;r9pCg-@4JET4Enz#c4N0UfAIKEbiK`i8wUN?iGUqF=Yy@fJN5H_r@1qn-ouWA^CrBr>~&LFvnlhHuYPC{&0+7N%66H|HG}?d'
        b'i=|F_rwms9Sl9bnVEUkcx(GNWlF_v49?;(zx`(}CzSWUrEg!zMZ53HAm(TUA_N2)78m14D!uPw6)+Eev9i5ZVmfN5^>PqOy6_e_1'
        b'?}pTjv4b|-0aK&V7V4d(hVuB2mdVRl^p4FIWh&BMS}ZT}Jo+Cl_t!%<+f%-Oez_sJTzOH#f47`iNGuv&E-yA+X9`#A|LuOrGrz16'
        b'>$rRcqU>|@AKDZ+R9oTLcSwn=eK@_PwjjNvcAm1cHbcp)%~mXOgfg>tT88{ksb#TPa%a3caJR2bHd|Wb2Mg7(8RO-+8f{)*s8<;8'
        b'O@3#mtX#Gje2vx)^=3_@LH*pT!4Nv4;v|&SpdtLd|0{=%niFa>9PNj^?T5sQch+jB$t)x^gp#Q~=WZBIsP4i6HLaF7lgsLHsg3K<'
        b'7~XZiJ*2Exn-iW;`f-kD#g?i4(&6_netoF=WH?S_QS~~mKV*BlAk>+5AM&~nsa2lIbbDKqyb0-8aX`N6wf2ybda3?))E-hhz*%W$'
        b'>sB37#z#8Q4Y5n}&qm4z=b`XB50Pg+$COk>Z_2BY&nQD}1>5&bWo5~|UvzpJ`l7aVw(A{t9#9Ll>+UOGTp+rerFW!!;{3y8`CWn2'
        b'y<&;XzNKB?H>yk9SWv5V+$LlHEO%LvZ^D9xg3xnaSEAbLZk3<dv|8l-C(9fqEpl^fPB>tO?}~t1M+UU+lzV@t|HwOmPu~gO1PBFv'
        b'Z0H|38My91^=WydARIF2+G0L)#MtrSx}!&Aw8JhnFn;?DhK~Go)qj-FFE)FRiWpsLDsuLg!cX$#?%bN!sT(7sFN!~P^k|W1NGnnb'
        b'C$mU~m#B#x+xVtf-m^I&oJ2{dZnQeLV||Tz<1bA|jBZh9Jg1)SavwA-%E&krzrCZQNL&VIwrj&T>12u)i?3Tw?6RokphN7t>c?b`'
        b'Eajfh%YPj0-frw)no#}&8Rr4HE2}JZ7x(*bJK$bAGN|pH$n;`Qu&(gH>{+_v@2jr|msqVU!t+X$82O(((HaUWYTxlS8m;;2Wh{g8'
        b'3d(awOvt~g<X?;GK06qHU)fTvJJ%>;DDvx?{6#;ESCVW?*40fva9fPJ8c}Guml|!wGKtcXdYw{WIUu*M<gPo*uB#D!5o@m2nxn2j'
        b'?h?zQoQ*PnQ{|gR7H#|j(ab6<TTwP&#<(*SnEl><8AIJoCE?zRx@<{y;(?LVmh9exaw0>WDgTn6u30j|an#_1?6(evrxTV=)2*DP'
        b'd2O0)=`FhAEX|j<$X|-ex=U9)Q|*mpWal0T-?CK~&A3%Raxx)%`~L8BXf^ULi#kWmkrL_`$vyx1<$FF`250-08m+U`9U-UlvMUbl'
        b'7rj&U-w~lPzYX_|GP18aQ2eK0`0tnYUzW2OSLCdI|H{GP<vja)&IUEjXSMP=Uvy(h;xTh{XOdyDK4n~`?%1T5MY?Xie$f|4V%l{_'
        b'qczL*`uUSY-JbP!taD>fGfMto!LnuLnsGMG0<V36dR&s{>vapCj#A5^M~ljzsHuBpzug|?e#B^XY3-}ja<53vyFGrX`0p{fLmo|V'
        b'Zq$^QudqL2EWcmf8#1&?{`0`?i}hM%RR78ZCC&a!jd#O-HQlmCt>+P=`w<!Wv7!wPbqf#1%d7O!74oC|+YgG>h1a#>x|PbP6O-)D'
        b'f+M3=y(q`4kVzNyFGx^QAHHpW*^@Okmv-4wqdjyOiZ(p`@QnxK7syB}mMt(oTyRj#EL*5<+ltT))f*0$hqg6zgY}Uw&W6G@``dMq'
        b'IrGh$`I$zs&${)xwfAhvZI7yaDX88cS4!Q#UeYzDFRopCSX*1rIPdVoA67V`_RHVQeS31lyrXRiTeK%C+Fp>?|1|ef-}<2mj|@KS'
        b'Dp<KM-1n_YY*#C*V$p>9;4yizIkTeeYi@Gx)K=HZuMOj}c8;q4O8x?byUuPem(}Fskvc6!iR*tNL78CRT2nB3znY9~yVlld><HDp'
        b'#T&L1=tDcRK5LZCWh~Gfw5gx&%k?akuOyVjI4-<nFH$dKdD0eUX&(9f%g`T=HwQv<3YTh1426@8@<H#v_eF~?MNH+h!QuCt8WPn?'
        b'Zq>Q7SG;!<{@<d`*C~m1SG37uRm;8WRw&WSmKQu1{Ya*E;u)p5{Jte!`o5TUZGDBNz9P!8c|hz#=O2<qJ=CIAKk;g{lo$CP%vGx$'
        b'`7Zi!UG`32RA=`hQIq{{;2UbP<iA&wJv(qkO{TV|MR{B;D|}12Tb9S7FcuAv@=#+VRQP%u2f95$&&cxFTYO;C`vZ|6tLO8IBLlOq'
        b'*A?F>&(FN7@P%F#x}hR3-Kva^rN(f4Ih~hLk#Qg#Ei@e}cU?+K_ghDAkbk$F^UbQ!q}Vh&yw&@yqEQse(>XcoQGd@s{LJ!Ptxvtd'
        b'uEuYD)HX{#A8V;H-Kfp(8W4-vZcz_&Rg+H1eq%ru8dZ1QRrcCCQBGP#Eu}s>+A1pn%cD6Pec>|t_HY^fs2V@}Cj*5qYr+MqT3@te'
        b'v<-xBNwuh3YYI)M=`>_7eJ6Zhsv%VS4Oao-G}JdwEqRfrWag^8P+jo-fpAHuU7D|pnX37+^xpd$bulK*Yg2W_7ELHp**jvXp0sb;'
        b'%b`LiyL#Z#jt&J`mm0Gl9k5;s%1elOK^*(6JIB6uXZEf7tgZi+o;amZjtwG*b7%_JO&0=@{HW7v9T0g=E@p4sUwk$g{@e0S@#m4h'
        b'uNx@-BpBY_5sT+EX)c={F4seo?t1m|)fT@WPUoLlIDO=#*tO-0<<#P;yq^AWnd1_5!-@H#YM3vohAQoeB`#SrxXvAkR)3Yul_blS'
        b'<a)jCLaCBkR$JrEmM2TYeWK|1G^$0vT7cBvCoicL@eArV`owu63ahe3p`x{06!Xz?=6(Ge5|r_q%meP`nzA-+haBKHwCI!3ccewd'
        b'-&tmVN|v`z)xWH9FEECyou{@;vb|tx?g~2fvTR&*U%x9si4*A@2-sU|Y$BZnMo%c}eb1yui%z=TEt8o)+2DLxBYMp4C)5J&K7$&l'
        b'akK~8b>Xz57U`}m%eM!^?|6jEV%O3S9*tHDVp%|zrYP#8r=|Vxh?3U7InckQMijEX;X-!lbFr%?Mmzh$nQ&$qI$svOWMim|b}luj'
        b'fttFtfpDoE<1#ocMtScqQkHHWS(a{k_JCTPw(B~=Jqy?3Q71;ZbfJYJ?<OTy{~wvHb0S)(vm#4^hDSHO6%f;#)*J}uPF}VRRhxbl'
        b'2v1klT^DeNuF%xbm10qQ5!pq7$kV&L#iRZbn`74GOfnwT|F`RFQP=n5E7rIC()z9*USDWM6$eJHXjGo=vh`FYRv(s||7ClOJJe}X'
        b'Kl%J=-LC?D(Xu_T;6Rr?yd!_A9;~`MB0F}eBPw7oGTNWehAXrbS-~xJIAo}tURv1@bQB*@t37c>gloMLU8rgczvmNrt-L`FjIwEP'
        b'pf_pLcOu&o>oO?AM?uzaYrFJK-RX|lfC$Mf*Q))?djm}`>(#dhvXlwxRV-7}iVG+Gmhkh^P>A|kL6&^Y#*)?17WyDLOI^^?5q=B7'
        b'67I8>TuQV0)c-t9<K<}@FQr+a$uVo2JnBn6OJud*I!Sgy_BWW7)ILM?$L^i$E<KCgug;2Zyv^V)Sy%m@Y=J!G^=&u0pH<hawmS+3'
        b'UcOpRe6L>ZP;I#}ewWWz)X|%8DH(b9c*_zsk?xIeisd~|C4`e$Qm-4`x$&3o)ituhTH<ykh|Jqps|QuBw{LvN5Z@>|(QbE<yFp##'
        b'M%UtY-KZ+-@e@JU;tWk-T-CqGhy!)c^oP#|S!S6hO?xQM9;#WEOj9qi<0pgacj%f>^yLHMq$>U_IHDb+el8I@=hc3;*)mpM!j`Ef'
        b'(_~QuDsiUuHS&!$m)AaZ_*;vHP+aHKDWMY1`M{LWJGqI<v~LRc{%*hH1$EaMHvQ{BtuB0u8N71>o8IYH!y`8#)U(mMt3UFzU437s'
        b'K_>^=s8zG4^*+<@34iLY)&Z%9mY?mHv)API=O(Ce5;m>bKc`WBhNPYz2_3n{7v)=F*BE-f3fBv^wb%L<B(&&6F`n+Sx_nBydPhVa'
        b'@U`CRuk4p@uuNYUcw~QnW5RlQ3uH@v{{my+iGiFQ$>M02g^qT<uSmX5C@-+mIkJPlOP;`a2J5A}F`@mY3$03CDm&xks@8a`&)eJN'
        b'eII{af9N(xQNqn{j0xPm-+#}3?>+lFJ=K{x+C9(9PefXMZy5vmazB=gm+KeTd66l+-tlwtWlq%f#)a1#clq}+m8XJoql*&6c6(m1'
        b'iw##&Z=NH1MHbz*1$Qm#UzgyxVgLGiQKb~zCeJ5VzF3KExT4FK<6-2;JeDf*+?krI9^17uvyvxHJmb>s$(0dgi^i3dac{pVRG=jl'
        b'p9@|wZ;F^_iiwPSa{0`<zw9%L&bG^F3vEJD_+4+cSJpH&O};Xn=MBBvk@G-Wq#n_wpHOdHS@V2Ks*L0Edal?9={wKlCN$`5B|dAB'
        b'Pf3y=Q|Ed`uUziUxV2A&ALWVY)#t2vR?*0l58uSOr>yPt$WP)P?w4cnm#uI#?aNAvb-cYVYm(0K#XxOhzRs0c_u9UU&j!lMq85Ip'
        b'o`F>})blW_;Piky+|<hog^2E(?edU<4+gFb`ODvg9KAB6Fm#7O?WBiO3{Mok5*!)v^5v4$hmmSPk{V!CpQVPHz4NP#;ly9iL}EoU'
        b'P`&Sp5c&A?ia4(iTp4m(U}Q*6)r?RZ(p;4mdV?$b<>CF47z#PMAi;WhNcIZ@O6iqho&inK-$Z<NU}Q*>CB1sH=m?aBtDAH+*46HC'
        b'hOSm?igatEvFy&!#;1pqSu+qBN+Xi+sw+a0E;T?+rq69xw3WrKRdk`PEZz|em8}-t!lt;gvdLLV-%hE~WKFsyEBC?Ur{uoKv1Dab'
        b'4%ilGMOUKid!d|U*$U)6s=}%%q5UP}+&i%B@;GV)OV5|VaD;^eo^OaSb>&d#o{5a|-GTmZh%&9`crYvJ-(IfCn)IWkxog$9i5Vs0'
        b'bWV0(7CljoJ}&0nU^ve8GLH2d;v~leB5`KQIAz}uXKc*QNSqlm&a!WalM?f0FuecjCJgj0Rx9-xp|^Xh(qb+~$`CQ%d;Pxmj;Y6V'
        b'x+mPCm>z0HL?*LD*E?~<5Gjd~8HqjTf|t_SvA6fr$b!bmf{_J`;RVhQAJ>m^LMzQk-)FjPy-A8Q5|DJony*$0BeSk99<lEC%;B`+'
        b'E~Ry8(a<;24I-Y^8ueb2TG3`@?AdF}mE*5i^Fn1}mMrkpd5IbC227XDOANo?EC<l&eIT+kBPVMpeVLEm`q1^O4n7&W2ISk1;qhyZ'
        b'=>2~PES#+IzZLNQA#iNZImcUpOKtVuq-=k{+<l?CXYG7fV)+(hZ@ef|FRYnw@3kI@^7*3F_opq1rYz&MOc780248+J{`-Jh))&5Y'
        b'u6mEPEV-k|xZzswra-4B%JH&HU(tte?2F0zw?2PnOM?HUfcK?9`dr5ga(;~HlXma8;GChY-+0k(7d4m3-C!*AXl;!q(L-rWFZBG<'
        b'UZ2qwz3SC*wsW@hR$HS_6KAu#>t;l!KU>ylwQcux+?}v~fhdCRnqQbXuJ=IT>45)fk%QCTrvt~gYD#BJy?)os>b=`<UGv`2BIC^y'
        b';{)!1|49+y3vn5CSB@(wRK{v1*fj5W`-|iY{iTK5n&d6{r@f2rQYO2fHqE`K@vhZR?20W-jp+^VPm??ON!{AR-d_ZixsK(5@L)Dm'
        b'%~Nw43!A!=y9eSL4Kw0@x+cn8HEynJZriF2L$dcBdInMzSZ%&E?qlX(gZ>`|HZ2L53QfKp_HD0TV-O9%$ar?^vYZ<)<m}MP-;w*G'
        b'Z}t{l&#yI|9>wYTWyj{9%+8ay8|;6zrMKDV4A-IYu5B)#*j0_bMqm1**^RoG)f!)$Ph*hxPeo7MWu4n98zxQFpS6sa&6yhc?Zm=!'
        b'`U#D4vva)-g`zu@^4Yhn?s99s(fXM!{VQvuZ*Hh5;YxaMQJ^s3zftVK9`E&m=I1pX&I~0k=48-rEw|Sg?PArR*=u|qtqH5!)b->{'
        b'8<&zaelV$e-<gZX*WZi}TpRFT8|d`DS$sNpB6sJc-d6%S0e_B2aDUIqVDHO;?12B<V(LKg2f+`o-}Nuu500C%VcO9T6HXpe(o4P{'
        b'ZtR`6ueOSIPVM)5PsnU<@VeWq4TYXoV{754kK+Rw0e^;A$796@gU&t1H9J<lsayFSP4!;qo(sEO9e?zle{TEWnwFzSjEBa@2gU{b'
        b'sUq^Em_5O{|7ZP?v*H{X8}KKIpseDa;9zQhf3o|C>2RvDRW6Vp9~cwx$BVg^p8p+eNOHTAJGPp(CN-og)7`%@wl&u8y3mqV8z;I<'
        b'@;wtJ&Ar~#m@4A^#<+fin3o@?<f}nP+l=*|U%r@c*2K$S(pBO*wkEV~m*13h4on~S(Y=9V{r<o7i!(W<Ip{ubOMl6|-KR#an-Sm9'
        b'W=((A{j9I})8Jvt)V$gooIe=1rBIv$VqXk;`?s5pHYRK>TyK`$fEKT7z8vp$zALG^Tl6)i&2Z_|f#Pa)mZa(v@;6tKeAk=gm8$4h'
        b'M#|@u{ga(L&edDAZckLoNljp&-#^gb`TQ@uZ}wL{t{K>Pp}*1iZtk4?k|ZUwtjJWFv@^9<uOwNoH|3|^QKO5Qsd2^jwgh_m{crbo'
        b'dhad%BzPiq)X?a_TmAlS5%B#O`R#cBAB{PlU-s8$Tr?coJkEMiT;W#r3hx(JcvSjtZH-oI&{vX|XX$+_(Aw{B6}w~q%0G%Fd!G-y'
        b'*za!^(+5_*8|-*9Vg2^fT(R%+CvWR4oIdX625Zg_#!Xo_?dbm!1%r|-_sgr^>dzV$bZoY|w;Q)E=sl&m+NSy3dnVU<uF(1&V}4<8'
        b'SKv4O{@;kq-O}@ipr(3<b%XI_<J`u^RMFsA-%y*jGqw7yHG{T$jPG81ORmVkQ~my@MeGNQw~5nW)Q7s5Oil0a19koW{}iD=>UlM&'
        b'v3)2CvtJ&S+xLMe!M+|Y!H%jW*l%SC7W6I3Et!;Z{F9VdKUKHm&Y7|p%G}mDfBLvP)>#Y1c0BdZY{%RUCmXAGgmV4doW|O?ywvJl'
        b'VnXa`cW1^ko71dciId5yo=k3cU6UuR(_`w`YPGicI@Tv_Ym{%c)#pqd*Sk4T*zYftXJC&bsL7Y-S#I@P*WDl*+Ox$q@~{2=>%`12'
        b'R{kvLd|+H&p^_%gwo<QXmWvBNzp%|L%hg8jmieL=-8es7rroPsySeu%`K@pBVfC)k!u=ZCtMUzr;~hbDB+7vu=T1zl?or~)e_?#^'
        b'`PY*Z%x~$-&Blt~_fDA=ElR(R&Yv7T6SekFfouBxv&AX-l6QQ6=G~gtXX|>tqiMUpA*Fh!eX4QpDwE6pdY*37hm*QQ{gwHWNId2I'
        b'xi0;(x0X2G>XoBH=-Z<!13~q4()9KOGWz`)>ft;k&#%`5SNHoT$^$9NA&oeSCTGSJaST7TrMK8zKJ`bR>t>8f|LroDJccE+8nVPW'
        b's_FM@<T+aWu1upf@by0bg?+LtI~Xj@Z=BrmZwaf5<cmZ%EuTE@{%5T9_l>)waoW)zCp=gwj;(s%qWY|Bq5B!Dz0ugXu=m5zu`Rjj'
        b'%p=xiD~ylbH1}82T-DvR6Ga1|&1FfgJ|KUzE7dZw`u)SP^3RE`iFRMq+Lr^L?DK!RuhY9SW=l{Mye^}8k8#Qt-O773ZO?9>dfv6>'
        b'!!u@Mhs!tRTk(Oxef~iaby9JA(2`~{CEJ~*+BBt8EVL>oKCpkEzki=B>zad>iOOU#zoXN%bz)1JlIq!LJlWQ?`+{YBqd_#Nr;aa4'
        b'tA5w>g7Hj|(cWe{Ik`1Wv=vh3pL8XTI-y%>)}*{}^2|ATL7Z`B98u1`nraIU@60n|XT}V8(#pl&JmRa$DKV$SoJu)xs-r7m_4WtU'
        b'D<W&#?-x%WcYl4hxFYU&YWmUJ#BNj)AH6;FBj@U;ddozic6;wR`3A;-*K$+;Qfv8Q<KoJwxvS61-IgYH+iI}~8)GeL)jLh{ccy-6'
        b'Z^~HJInE@itu|AnnoQp?!{BMLntFX5YZKaB@&U~gX3MzVrob=u`F|mf=jr0b!KqX4%x}!8uNr5$NtC<kHcg3F?1ZDe2~%&{y&!b^'
        b'rDcJAwW)T&HTsn|g~ld|U6mMT?mlNpRM$TIJ+jgrejXJbFQBEc@;`!WcD#6fj3sAU+l$wa@!G{oA97rjr)~43;rB<|_08ua?<>i7'
        b'&mP(5e`KHc(S7m;#5B$E%An^KQ|9?#+Y3#*lV98%9lD2`v*RP{W|L^99DgL(v^Xl|XJ0E(rMk=|LC^EP*2Mgr*3b}3q4&Pl&Z+)u'
        b'<u4-deu?Sv&2<+;_ZHKf9*tEUM{3~-y{Wclp-V4^YQ7L`DeTf`t_a>>*wEH|Cg@7^wD_79YcoF${pm8dCa&71Z8e8RxVBD`V=gKB'
        b';eJ8AM=J->4JDka7i;)vOXrSr?YhdLV7spQ%V4{{@{~xbt)(^b_($T8F1`G-rLg%aIsc1D+ez+^S^NC6_IYQD{qcTgn&v&dC}(7o'
        b'>vNH}aJy8bEc0<f{sQ3fGePU~rsm_pdku0E`l2#_FE`?6Es1xvwI;UfkN-uit;8(0p*8Vlxdmc%L&2VpLT%ynUL{_RiF3O=Mk)2t'
        b'GQm?~UmPzFZc5o_-C?RM4KBK|`OiVm0%u81=B>eoMEB!9HMz1jU#X}9T9X>}8(wvs-Bb3tP5v5>y>9-_tL;xbZ+{}gZZDUOok?Pi'
        b'AB6Aytv%qnX@bjH8Re>+;Hs^hc*eCr{J+4JIeW`T`I$Xm$$mk8_#3IUiDt7pw$ZFVYs~&4WrG|!%`vT4ZJ~F2a>6eK7TlIo@Lk7b'
        b'8SFT@_oyeq{;RPjm)6r%ATH;0#nfqP+I`XS!Co=nb4u@NkIM1i)}>cob{vyIjz8_4`sa*4?#-z%PW_}dkmH}J=sG9Kgw5Sr$Ne(O'
        b'+}x#wr`om6&hzTA)-`!PQr=MF+q{lZa;2S~v&zfcHpzh-W$et?&n|p0I{V8#6|?rtS^mf@UB<4xb7sz-b#1|}z1Qn=3O*7!%<(*G'
        b'`|jABf{#r_GM_n~k8EwG@wwd|W9JT?$ZetLBgb}`*!ZIC_xDsx-ZSUg*|T)>Uf-L&Rb(`$H@V>Vd(9QsW^CD;{hIh=mf3UGlwmhl'
        b'%+7dqZ(&8QxgsxPvxqp;TrtP&*=aP}=U3z}@19)f(d2mEuF|!~I9^tF$M=@>Mc?A>iYd$WIj-3wLhdR`xluFM{7C)bTM86iyVhK!'
        b'$^6Or5#Ot|>oUK6Hhk@d@AVa*y?ng)oXC4q;*_5ei7U=SYb0Ep&*GFjUN~|&+xMKd+$OU}voJ|3D^-hFaP5O#(T<wE!|#SxmR=AC'
        b'Q=F5>FNB8U8P1nOqeOK@rT4aL3oAxBymCvFJZFK<=})iCc6xs6oM&+9y0orT`MqSU#`W-~AMI5Vw{7Vttg&^h_-ML)`nvZ9nl@_e'
        b'?k_wo#)8}Si2l09mEd-NF3w*$BEPuo%--0Zi|X@nC0?$nQ><x~x~9~~nv_LXtf+U6<zYE|Na&p;d98`_%JG<7%ISG~II{Y9F!VlO'
        b'B+fE5<x;D4g;Hg$U6-d5k@J$|AXlPG8-A|lNZnI!){0#zcIc``UFN~Fk+B>c8pkucXKxu3xOT69)?V+dy`7$?D-Q%^;_X_;oigqG'
        b'gc<rAk)|%)m6zl!(09oJ<|EIG#PX}u<umvCEqlFLVtH?6e`NX6(DFH+!OIg+^A=vdZsqQ>$L*`OjtQjg^{4IijulC?XZ8lWJ?Zi$'
        b'r`C}t6DdtlCKt{#l<4LcXiJjQpO{~u&(Ba3iV7d|hM%avh!MAUZJPL})*$}5Y>Ycg{iwxBHdEB7C7JQLYZp%_3ccDqy{LRr_XKmf'
        b'*_j`0HT!PWTZ@+1)UhQ}3cv0N-v^M(CfMv^*|B2Tk_qZ>t4}YwRhJ)anykjP1bf2os#@J&I6YNnZ}h6h(T<+oqGy}4->1Y{Ej1(S'
        b'zzU5z4A}xrZ<|Z2l%5f%kSPE3k?TdKu``^;VBg=Q;aXg`ardTg_qrR5?Yh^~VntO_?-{!)|0@69zD;}k2AVXPkE@%mT;t!<w`osb'
        b'acI0Avo1BgR*9XmRp<2RltPpGgY<IT|HaDq4*Tbd&OS|!nA+Q#;p>}bF|Dt;CT{Ixif*bt<JWsc%n9<n&sKftp3I3tt2OGV{qro#'
        b'FTTthm-1+=_doY6O)YSA_9@$4u>-MD%FdVsO;$<nYbCdOU3-=;%5uEa*XcPW=ZPBdBkPuR>1$`iT6eC?UcTEpWNOh_43<yBV*@z6'
        b'BI*xhRFTt%E=83G#Iat?Q&%A_jW>!v4mzIhyI!5vU%#{X^Pr=?Pq|J`MyKbkJQI}PgN9DWI~|VZ-RdxWwi^oy3$%rPQ)xztL7bW;'
        b'$z57;A`O3cZryK^C9Fptq6@*uIi%J8ht86y#4k1{na$r?_M&NV#aNNw#om}}4EK-M_v(71C!Xo{*g8Eyd10<r*EQ-`##oD?FWNF7'
        b'uDt=jO)SuzVLW1Jo6$1ruKP?&mskwGr+k)9+e%-Tw!R|8S&=NF)Muo0XCz-^aBs59I=6q9EC(`@%Zq%sELfd;TTIORL7AT)%KRA2'
        b'B0m+$N}Q5dR=>_I4xgcSs?77PipYt4pC`p}znYhrV;RX7gUE!XsV}-KO04IIp((?7*W`D9w#>Z5w%q4=!PhrRv^Ts16=NNn<w{#p'
        b'l=z+7+GCC?GEV~;V;7$P$|dq<bXpQkMIy`XF}EyGU*ow=CpsG9ye=`j?o*;}PMxVtXvwj@TGQ>167z3fpOlwy^Y;vS=9ZkipNPG!'
        b'SNFErJ8H^!UGw9?_9*qcB29a2=$&t`rmkj}!?`PT<QnUo6|s(4aw8O%T85fxvv1uZO1c)^j96zuip9{SwIr%1Pm5zqUHob#?ZrI#'
        b'0(^(B{Fx0=)rVK*$2&&%$!|3ETa)B^V|vsvszPP7JY3%jof=NhQd!!H^qdy02>EDRmq8Zdj+Ds!#_)Vssw}s6yAs=V4XIAc*e!9F'
        b'l{Xa!cQ4M;Oi77tlIMpEt@yaNEBeue?NLWZX+*2^(HQZ6?-Q03k?r>A;xB`?Ww-a<as9blN8OP(#<r}e_x|*A%RQz$^0eurTv>8_'
        b'(`9d~b&@y*U0Xuc#=<%0U9;4%BhgMvLTCg98NTh@rF@mjfVQ));$;hb>Y@5sQSqPE=Sa@P(IR(CcV;TF&Ut#L$6nXdTdQr+xe_b}'
        b'`KW(Kuh~4-?K0ISh$A-qI}{c2zTU#WXaaBa`n!6)UA>*&hcX`yI?dWXvD4C&339(|6UADZ-4W$>S)If6TBttU`mke%dT!}1RfsNm'
        b'8M;!tv}&b$jiEL?_Ed$&=r?tGu9dCLzXso1Ki99^Em{tL4fdXNY0cUwyDLEs`XjO!DLec0*WWG2unUIALXqWc^Vh*|ENA=lYHD9b'
        b'`WWhUAFE#X&2I!R9m_~~wn%vUh;aY%-c8GUMR6-z-PdS_$5)MfyPqcxRo-T`w(H%UCk}`!DQD8yEwQp@PEuk$HL?@X>#Bd{{QC9o'
        b'nwpo-wdnE;dAVY?Yq^qS6<f9Z(qT-KWq>zk)p~>M6S%gh2l`T8O2oQKUR5i^-rXf~UCD)$<+`FYO0rnj<LbH^#Jb$;?e52G-mtWY'
        b'`cl4C7$u_QEmx9lxu*Q(mvWgWvXSGBnZ4eSm)I2*-i-ej>x=&8^;!P$`i6Hz=Twa>2PTMhthsC*Yii!8YSA5ub{YDjT&~bSf|spl'
        b'k-DCn{?U3WG$XEO(Wbg=JmFqf=PT#8wTX$f4RT{#2G^tN#V0nQMLl(|G4!@MwHj-l&*_yvSTNkL?1~bRt1gXqRH2!0qY`cV-nt1l'
        b'DPvo7Rffe`V~)mX-WXq%*r#2bmDVNS1dGwU_il^UQ@+CEiTY?;-ttjPuBv|DmTSykUS1I;im>vgbuziE<gO}FtX9n``@Kml6JHb~'
        b'`j6&x`9`NJuO+7|MyxhV-zX}Ng)_fu@{Wr6R2>U0akS{-?mVgvl=b9rYe3DfNL#&jT!lZ>Id@)AbYEI#%A#JaBR^X0(v~eU-I1E%'
        b'O6fAVwv_))?r4$W7<E79rL0|_w^^B>PKsVzl6lhDPK*4N15twH$g*(u`YDzaWrEop9|{~!dEv<mRoWbHY}rCz*`#$bqV8U}`>!j{'
        b'j%Zgs7j6@I_xw$p$p74)P0#JQb+oviKfmnS_lK{2`{M;8ul>lq2&?srdQZ1FT+ghFZ75XEKO^5h2#*64x{e*15vR92C!#dB8Nw~x'
        b'x}D)O#1=k7nqE2IRwO1ilob4Y&)TGdpY3VU$%d<_FiMiek}|217drjv>K6C56>8J1Gkt~PY?-`HEh9&i88;YuPs;PQL_Ke#)DU@X'
        b'Sub5%>(_}(E2SzboSh%;RLj-u@9*i-$|kpno|hz+%Uj;A3ttAIi!D_Iio)auL#Q~3iWDb$H4p!@YrAFm+D<tU$-r$g12dxX6GSHd'
        b'bx&b|+H(-wo-;{X=+S;dPC706e{?<m-{fW5h`gl#&+?-C$9cKDuD_xP5=Ho$niSFM46WS|IuxS6lAkdnI{U)z`QZ$dCdlrYy83^v'
        b'Y?5tm+2Gz{Oi%M}-nr@I?io)$lNu{$Z~Cv@>9>itkP>b~%TZtcnfBqI-u~y?htuEw|It1aWlQ&&*UV!A+jsll*zJ8|cc*7z<;P#E'
        b'H^p@7*fz2UE!%$%{o8fAw_6H3{gzrsV_oHiNT>2uxn8GMR3~Q|64p1=7swCbX2jJO=tV=&WhiLbUGF!!QX8|yWv3R(mcsPZRrS|c'
        b'91V3QSAo4%YhP{h{;#(^E~BP3!Q}qJz24-#`)!kHg{M)zGb$PrqP5xLP!b)#mTf-Ak9I3@t5=7HSnS>6v8?M|>}e@zmH8B1{m__a'
        b'UO9fPUR>7sj^<B-UHVX)vNn{}^cf;+x)zzw95t5~Lyq5+pKUg4bK0WCNnzY1%fa3`X02&zlv+Ni=|ze3N*&D~1?3$Jnclxg(u)#j'
        b'v*^BvR7<l(ss%sXEn21pDdB>qaI);pytmt_HD#s7W?52O^|G^@9#yI@(OU|qB<p3LPOc|Cxi~UDP`FKZ_iq0^yS)p=ae3zW{;&Vr'
        b'Hr+RrpW8;1pXSTQ-c-x*zHk{H>`}{b&)@Wowc4u0I(yGuk1x+kQYNg**NQGz*0<F9Q1rE)Q~O$Rz1OOPy@$_X$G6p!QP&q;W$22k'
        b'I=JiuwXYQu?rS~NqPy$y27~W?U%6{Z!&cF@uNZr*BH32uI~u1EC;fAVzL<9X$xZbY$&P>TQTtkBAI!DO-d24^@@=uje+l&!<on64'
        b'l*L)H_=(XhTp!hC==P+GBeU47ag32!aNO7<uJ{>oH;Yz#ZGMJ0DN7U5Cy6O#lDzn1y0m#oYRwob%N8Z)Ob%W3;dX&6?>ar2!pZS!'
        b'iMP-Yb9s@s@ci&POLUG;WM1p0^f*1H+4-VtBAV0s{Dc{)v-7p0TO=CPQR+=2*#Ud+!4_SK!8ti$VXF30oia1L<`U7O-1)dV;=$K)'
        b'u)M#?$1PXpV@|Z}7l~{XicR0A<|F!wd^kPtsZ)dDoQMvU?FG}{&CBGGd3kC?Uc`B0`Xa}3+G-Z{eU3Le{5j>{y`Le<j^DhU9(rqY'
        b'Q|qqF#z<1;Tt2xwGCAW`aTa~~2l<<<zk2&Qt<vyQmvKwnT=~LgOMK*8*GM@mZ%oA>kCWp(DsvUXaYeIszW8H&r4o8Cxj9KAe@4%v'
        b'X&$A<nXVX`4KmJjWqhVVEUpvtj*r$ve)CWn@36}rk%%kDp7@3QJ0(ZHA1wMYj%qpS`1vmN)?d5s_*X&oqLpK~*M0qs;~7S-H<4ae'
        b'QoQ<dS9DgcF7sDkJ09Fs@A=5&^4VOWpGIqlt={dqG;q}La=o7gDt7rRc6lpy-4icA=U?}=<L+H1i_d0GSej(Wj_#4KCd!AN@$0PF'
        b'1@XC>+5~%Ug8bk-*A#hw$nkHxL{gU)I`;?p%Fp8DiD&-KLXo_iO7s)V8lBBrs<)czG`Ze`pT&!U#%ea1tmUR$`PPOe$!0RunM#vH'
        b'Tyyu;)*PR;L=GchD%GbnjT&_<cHFVFDaYo-Ow#1+I#a5@GwFdzkL8*w3XFDJ%-LX0-*8yYA3o31=j=FIt8YwdowPOA)Kp*+afX5-'
        b'=0M+>xY217r(TnPLyliW8|X9U?C6gyS$kvS_ga^1{mB`-&GeT7tKHTk$JrK(i7aUnZAzl3A4CR4rWD=iGfLuUad^&{6DF9gCHk|+'
        b'4Dq>Q;_TwHR_jdpYD-Rn)$EYN*On$(_4*mQ;Vn|kqt)Y@p{aP{?Xv&U-=-<gG+t*msiP*`^l@->RA?jzvETA^)(<|*OSBr3^32wR'
        b'q`Vw!R8n4{RY}U5Z#5<5Ew*MP<t?|Glk%L_Nl7BrW&iq@e4W*(&rh@_==06iD1Cm8Rng}cT21==`PK}5{$i_HpTFEXNuTc=t&Ul!'
        b'=&kQp$o)LYWO`q&R=pNQc$6&^KGS5%wOT{7LcMrRnNjn1)g*OY_5J3mXPavpzIXlH*dKiM?>^<ehVMpA{L_bhubk}t@!}u=00000'
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
        b'000000000000000000000000000000000000000000000008*^*n<NB00000Aph4!P*qh`RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40VGj-j00000fc#$@'
        b'K~+^%RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40g*`YB000000P=rr1XWd4RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40mG<C(1ONa4K+yl!?Fdu=0000000000000000000000000'
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
        b'0000000000000000000000000000000000000000000000000000000000000001BFMzdW{Q'
    )
    _firmware_identity = {'protocol': 1, 'receipt_recovery': 'ACK1', 'firmware': 'CNC_FFST-S3-0.1.3', 'app_image_sha256': '13bd0f5ea5689ba58398533c4b086bf375c00c64984e041ddfe9cdaeeacc6f62', 'application_file_sha256': 'd38c2aa4ddff1e2a35f93090a5bcd79898e7f93a757c111124b9b83c0c8ec7df'}
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
