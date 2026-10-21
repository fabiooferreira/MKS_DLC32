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
        b'c-riJd0<r4)%cwyAqfvjAV!v`FChsDCShhmR)frB4`dmW5Ek(xLo!K5lT4hM2>7Kn6Iu+4mBm)D`gIbeB0^cDiVGFcB3iIe+iF!>'
        b'w8pBnO5F%#dB1b+y>B*_>Tmn&9es1|z3-m8o_p>&=iWR%(Ws64x8xf?CxnE<LnH}*Rbe@A%-gBKs3c8?1bkxolWf)!sR=S+&a<ip'
        b'L|S-4;0c9i96arIr)_zgwL{FGD`ptT?DC?L*^T!0PJ4&7!{wa4!fto9*)2_0$8u*^XQ$oan(cHn`X@KHS)8rujilY?wEGoAqbpXs'
        b'tjjyP+A(bo2_{<Zuv(gyJDZz2FMefRWo_&NVrWXcrK5>rdk3+0H0f`0x-1Tt{<}2Q*3sD3)nxU5)#b9arMF^123C-P;G5-;Al@X>'
        b'prxtF@m&YP>g-%@Yqzvmmp9uT?G_gdM4_dvv8&DEvNnmW&=pd=s?*x&jRiFY#-PP!?{F@+-)VKUSvm<ITl4DW-iBD6POFoc;Md_2'
        b'n=Q6BD9F|!COT8$$xCb!lM|gO6C#LZ1vDu+MO<ldij9^w%w}<k=0Z`oDp8lS3Uai<IJQ~ExVd80!itLT(ZLLZGb7-2s|C8*WN}&O'
        b'd?$)?#JO`t9SO{0$jn;aZ0oQE_L;vxVv@9ch10p5P69Fri^4qoA2f|8LGzMm9sZ@$I2P}hAKK?4E4rGSt&Z<IFn-An7+HHeRO-*h'
        b'wzf9@g04-rWEmz8<r_V)h_l?p3m-=jV|NHK9_S$rv-H<Kupcla_mJ#2=HVKDA@7ZO88^N$Pje%S$HFrO!c9h@;WNymBMr3lNGcY{'
        b'hteDK%x8p#I(QbtvkaaFc$(m8h35=BAHwr7JfFdH7M`!+8G<K_2n_-}We~1_Xa5vpJQG8VTc#4DIf57uL0o$J6)m<wA|nzpW8eM('
        b'y&IN{(C!L&9tkDJ=mvEI^nkb^J_X9d)<LE(I*AtA`U_~S5hYRsHu~-!Nz!8aL?V#}Ey?er{fB(_NXaz+ZX(@1Bu#;EB)pr`hwr4j'
        b'bMW04l9W&LjDs>;i8OCWB1RC3VRUF!ZMQ;2(1zq0FwPn_-U-n5qC{d$1^hLP{g2?iH17};sTwOf19eLpBE2*!84D&t?kR*7c2>%A'
        b'tKv3GF*U@!Q92VwtRW<37O|ez#63V0@5jU=9*;17m&$z~Ms}$Nf2)akesq^=+wV2KyC3z;67QLIV!%VT5pqxssqbpCOhg<I-94B+'
        b'E#lg<5ErIx`&KjHQ6*l`2-B>i8vR{T++C9CF6od+QZ(?BtaY!Fdg4WlYXvo+_(rlVnZ&syy-S+;^i`*v(qWghuixD7l&t^K#5pCs'
        b'6Vk_@a!7|eApPdh^HSn`;$DZfy8C>;akop|A3}LKYGXzu;9ND0bpKI~TBni3Ix^Tw28&2yfhH}YKJS{uQfPVo^D*1X5a-3{Z;^Is'
        b'w$*E_X3e%FjcKuD&|s^}w7NNSVzo(y*F00JURzCsqNEvu@S|@t#tG5;JZjy7&2B4giCOx0h13^zszN$kA<d209(HKI>VtmbZlFV|'
        b'aWAKXzg8nexD6Pb8zD?{>oC;&`gtMxnH+V2hxERDUYPn!j!Fpce%tW!H$54V8;V3>iV&{bvc{Mz>U6H-FAu!_Rrh}5jz~|=nwYOb'
        b'^%*$8IU2ozV?D<@j%Rb6&T$&YsT|+H@hpy0I8NqxCdWw(n-ZmpFbrvXGH@z$wWfHfclS#?DUu~!Ckc~TC|06)FoRfcB-fs;&^9-!'
        b'*Y1;2wci5XBN<*kU*PFEx)WAGmW9CBTt|oL>JWFd^hD0B8>6MZ@GVofMs1uVZRm@nzv4QTb-&i*i9UI+YU4y{yK2LZ$etbIld8n$'
        b'AXR$?QX?SsK$M(5m_yv-Bq1CcvNg;dB6Xjqp=-}VbtlK5y5=1}JNm5zJZ#M%l$YIOV;jfDkY~dxA~rCV4Ra5VZF-#0#O}}J#JF$A'
        b'HlD+reQM!)Xd8sqscCfMmt#T|w)x*<a$<70`-`!j_(=EX@GHVE77<QM^zia%uKth5cpP7D50BqX#2t}>LEM3fPh#Shu>Lb+o~@As'
        b'{XL$oBJIz{(_=LE-uK2%{dH{5j>x_5z^|9$Kv@4<V~1YA33?8zIS_I31$_Bj1f^>G??XEx<-FU&4xhpjg!^~_VKi~?Yh$Oc+QYJi'
        b'?L9Wue{{@SKo}<vbH6gy|H_zLOJBs^{~i;%_pp(P=znQ!?@M&JBKGt}(j@nbWBYdhjTRvn%_@6#Opf>edTj5ny;OVmkIBWc3igg+'
        b'>Yjkq@cvz62Pb-1N;pf|F~;J(HZtI`xu3wP7p@o5PhWL#;t|g{OdG(of2mKag^5D<K93619;Nvv3fKM%(hg3*q%D|q?OEVi6N#%C'
        b'i;pLR=hXu%$Oe?tkk&tM?C`uXVZ7(~A$OKv-n|85fAFY|c&30bwa(GN!d82dH;ZBef4}V-O@Hp#J`Wk3rs?&ld~acG=)1=R^?m)h'
        b'`joiDCE9}!OkA#opGNIz^$9h`t=DU}t<lbn7&sg@Sg-BBW9;x9W1go6PQmYEz3w}(9Va4$%7bdmU<BH2^;%kr+cvgKwIwWP%2riw'
        b'l(km7OLb6fT>{8@tCp^Z!8as|p=BW9t)UtS2(t!5G_>7rviFv;*os}yUiVV0Wv;4HJurh9_lwix6DN@c8O=3c2-A0sw?^SWWc8Dc'
        b'H;)-CY*q}ag#M~AF(b;;7n$PbG9`SYIA%~KvS}+DJDZ_`x7)pMJ=?kl-_&k*i^&gqb|qTh(&~+48;z7fK)mu*sM$D|rEFk~rZK2Q'
        b'_qZ`Cj1y02`?GLV22W@Q4o40?qCKdB{mc+IZt!Q?<I@uF(ZC+~qSo`N#<Oq0GthfNBTR6|A+6`r$?mhGJ%*@cH!Ngbyr@qcb0?0a'
        b'xOIledp2u@X^HjPnU0Bj<Hum2p3e}*>z-dTxD?vz83?hqA%5&?>k2KOZ$yZ7@v5ZB5jzW$W<(`rOoLQGqx-<D6G;iEDnf>Cg_%J3'
        b'JcMV!9w>ap6TX#5Fua;?tV;qd1$2a?@Z1T{I(Q&A=q4iO0Ifwr1)-B^chXDnXi)b8{5N>cp}vDwS3@}HPeA(=(u0bF|AP@`bX`x3'
        b'kHa%%Ix$9q4mSlJ)a782kT9r65F^QZpcj4(&z4wX1dWPNOD-GBna9mQk}vCMd!{n|40S}**C0>62s+yc)ZYeAG=vL5Z@eF#)$nwi'
        b'H4XVpm-<B{*Qux;CP`zcvx!`9qdJtChF{@o>~Bz6!Wy)ogFX&*&FLf!sK-LnQFA5I_0ZOAreC4{B|!Ky=tJbS#5fD|*~j5&g=aN9'
        b'b0F<Lz(&9y<-RfRB=mRj+xf;YNGo%b2Br_Ip}(Wj#}J-F<B<^mLi!x~x(8?y;mL-F^khS;Zh|_G!5IC1ULlqT&)w|ZA?faMpi5>S'
        b'ihTBsdHZ1ua4e;}(IU3P^BT-yD3p8brP_bx8<7VH*$AU@>?I<e{e^V>*<V1WJ<#{vYG47>*|l^oh-wp*KLC#~i5Pc)PW;b*O42gu'
        b'Z!0`5c$f`Nb>fEpytmCz#sl#DTaxCDNz$tl(^tVNKSQ|*73%X)@ffw{dq5xkf^pc#P+tS>|5b#NUk~Yj$4OC<LqEdwF!BoEmt(M;'
        b'F$wkWSa?vqMTHx3BYzGXC#%W0@zgsY8bRlcgt=~jc@|(iBjIU)xb&4IeF*iT9y|i`AYDHsRZIgOgYsIMo14iQXz%`4w9#mfAPp3_'
        b'3Uz5{C^Y(RXnzmY^KpehZ$b7RRHv#psdO#-t~!+>9iAoa8z}8hk+z*C5AB<9Dp@+52q|T2F95kaQR=6f(oiyP<*kQjNGVYmT7^3q'
        b'rfqK(u06zd)mDu59gdaWzfOYf^YAo@zvyExuEA8k1NR96B|a$V4sI4-P@UNk`J8Ic^K=KN<*eF!l{7x1AwvbbrY?^PO02Vd%Bx$|'
        b'B{vcMI4MVC&`ixMHomt8(vP*8w36<$%6L5T<Z;aXTI=|XyoIR7tt!}k$ZW0y<=I?|Z<b&=Ijw?LxVnF6tf6j=d7;V!FPSuMEsY6T'
        b'aa3wBK8U%ttk_8!G9rzQ_|CQkejKeas7AL68sTcoCu19G*BBS78j2##MVO_$HG67^;WbI8L-MliH9Lv9C{j0v7QG!y3^Sb`Gt#OI'
        b't%N4b{OVi|j_LViT0iPZ*uwban55Sxbbm#r8p-DV4V!fv;v-SO(#D&Pjd5e3Rqi5>uR02B40HSk4>6lvH5Q`#3Ruf^V#2`*qQ{kZ'
        b'M&kC3>De*E?#As}_w%?9Bx{8!i`9bK+|ZSmrAuBTf@c0${O+4(C5bs}(lk3KAMrqmVTWE6g{6rXB#-Co_}zu#tjL)UtJfwIVeQcj'
        b'LJXc`*)i&)iNu`aN_tbhb_O;ewsuj5`Y6b-`*BkjmRi4++9Oybf9bYwB#+r8%xGx%T9+9alNBzkg$DhMDku}M#lmgYuOtYD!Y1!g'
        b'ZTnKnzWVxs1TgY23-plXN&GkD5!N5n<WIAnmGJ$K`TLV6M945d@e4^%Uwan%fE~DBSUUJGNf6SY9S4Q{rHTKNdUiyCGK#$#AlR#E'
        b'zmE+SG`DKjzAKUJpRPap1=HunBjPi)SDoq@J8U28zjbWiz$WVsaxx?8OAi54CRYU-)%~&eE!#2p8XaZ27Yah`{ZQ+G=NH>PlH4oC'
        b'$gC*XX+1q%s4_1f>jA?jUgUZ8pnJ_A1E79QC19nlpO393M3^2MkvIf{?rMJhGo~F4c%Iw#z9ffN51#RcC79xYCr-M{aR}tZrw0Ej'
        b'#m;vZ(W%yK`&N2Vovhie7A9FILw|Lm=mNE@<U_O>-1$`HiE!VDIOgdPkI|*Ovrgx!)3w#<Y8L8p79Lc)Gx4RkPwad`bQ>^yP~GrL'
        b'(LI~$BOx%iA?{QRXJ?LwT)M|ZcQQsxGsD5+)`Et?l*rguVxNxvQ)+1Jx!6zFej?!*xUU}@*m*rQ3BVqpmH>^kMaa>O*MKr|h$>UE'
        b'Ld?g{J!!0e(io@ZR>Z`ypq$jUxBgoi9Fb&wC2ri9xWXukvL3TblQc=26fazR)~&*phK`~rBp56~sfc;R4PE!cf@yv&t7nU=r^nU&'
        b'm#cb@{Y#iCymQa<;-l)Lp`>Ek6I;W3k9`7Z4~JfmmPI_VHKO;}KZU8^CjWJV=#u#Zrx-9Sj*5ZZlKUT{J|6_=aAJX&I1Vz+eE6yy'
        b'*DkGfRPsD_NSN%Iv4+!&2C-K&Azm%?^hJq%V(+nYn>?y`59vwS3=7quxe8`B`*~IOmo&eHKpimys2vWTmj+B^;D~6&fJ%rxsM@7Y'
        b'RLga5Q43R&!o#<$*!0@yGbt(|tcMK`ZSyoCOuTmu^!ib?(dZgU*4?}2v$x|lWS>TLyr%ohJ+n4ndp0dB=02%!U2=Gjp>ch5kHM*n'
        b'KLi$nM$FlqrYSimb$=Q9Egwtw&e5bv6NRvQCPlcnkH#Mv>pm~8+ng3A*Js%_S`bR=qqR3bKAN3*qk9{U(GMcrk0XBHGb)<D{xoCh'
        b'-w)qCs(*BJRD0&kHx&~O9f>@s0akki^Q`}L*EsjjF(jx<&;d_`Ns#h0Oo=Zcd5LTe;_e&mRg*`Kx$nmp?)CKd0ZJCuTY#^-ht|>g'
        b'vXFMQm>`NXL{W?eF;{O0iTUw3V}a>RQPgckw}zJfl-d&RTShnjaI~i@vM>CeYfM|C+$*uLCspn{X`vJMt{xSxtC(<N+}Yit+kt6)'
        b'sx49LU*8qxwqvaO%eDWK$gZ%};qKdMW7<dW{c-22Lw(~Kx(?mtTsLmP!nGeFZ(8uJ@fA_`wCGtX?h17`GB(;3;=UC_yVTo00htu~'
        b'4qaor)b3@NYW>(Jr#5-C(2rh^XkNFbXVVAW7v4MH^P>-R8=}Gfc&}{m5$X7a6IvKi_4?nst0?h@jM!a)v9-f|E}7Ilc~BJQZ+l2$'
        b'<C^~^!#Kmj;iAzGo|t`F$le0m*{Qjshi@9~ziD)zCw|*P(z78tCYjW)Q=tYRoc$C%RtF~R*`eF>spjkpho1e-=O?#D-Mf#38$BB~'
        b'ZdyR5_u=?3o~$~36<WE%bhKzQ>G-CzByRZXXxdHw*=`u+wlGAPIqXitq>Zto{jsB5a8PqAeB;#7{;5GpF{Ax4K}nNG`#&5BOo|-s'
        b'j~u;7Tp<r_`&tqr5^Kl`b%>xj(;Rhb{OJ4RM}MH+bR>3G^R1d(Ri);j=7gr@8g)q$X^np_?zJfQM<a~)2N7=^8R;jZ$D$6z!NzrG'
        b'Zzy$mEZ7?N?#P}qU(YJ~^h4A0Bf><`iHt8q(p9l*qWkR;%4V}N%xAt9CVu*N<FQENuf1<S$G35xjc^C#u5p)fLAqbXjDxx4Oek@`'
        b'JF-3e-V5$`M$Y9-I5Kl)+0=s(3s&B@HT0D9&V_R~ePx(A^VW!5RnF9-=Ot=iAMwQQ^GFN&-G9PDrf1};z}TLVYuUD2(*J(s$vc?k'
        b'JGG}bQP8}%I9V<3G;RB%bo}AdnpA;GsXqZ@jcX0rkfDQpx5sTd`VHl4kZSSqssax=s41Nkk@ys>a!<h;kWgt_>T}rp{7C=vBZJRN'
        b'b0g|+W0Dsvn8PA4i1kTw!{%<G{@$@Z)jhMq!KQvm5+)t}R_YBWG22Pfl<Mg_HoYbuJqHP@ovlg7^oI^aHox#mPtTkip1Yy%?eQo3'
        b'q7F>IxA!l}&*k*SCr$6`U6Hi*OX-Gn2g3TMJQu&tQ1XQwDOgt%`k6$aocb*nc$#|Mq|kpr9}bi4>iRr_()z$8{f3ceGsea5e)K3V'
        b'F6(Z|lPAV}I(9H3Rfy~t-S^?(r3(ArjC{S{ea{H>1Z;a+(*I~g2!r>%g=E`f(r2@vH8ES%kdWw+k|G}8vm?sW-_sWnAD=Y7PfY&c'
        b'D9Vq4!(wEVxXmNQTo_4?um9j&vZ`5qO|m;l9g+NRcsck}>4`~E!ld{@QlciwckEIPJ}5o0>9n8@{S#k*)~RIRv5(z1U_0E_k&RPF'
        b'=>8i@4W2BEx_9@Ou28&Zb6MnGao|W~;vm!&f-ZUKpmvvfFpTW8n0n((0~X`XDF;;pr&NO<NRQl=q<vR!9yzErXh@7^6lVTCDfCM$'
        b'vEUWyBkd~%Fwz;NGp+@KBawrDlj>i;a4_OXKiQ>n--Hc;PJzM+LJ>G)n;NSqpjE^ajbJlQskXf*#oRmmv)Xf}tdRmOiFxJQgPOI2'
        b'Xd^XiB68xB4Y{h6s89{*{`j8F6LM;j3v#1URLQEGsB6y(L)keKVQ}wxEc}KHPy+MfLqS(nr>Ks8Df#(A+zE6=#f=CzfY^;6p^6Xg'
        b'_nH&h`ah6U*Nq&$ZY1`p{_94zfgyV`di|rPVn+^78;N}ZRE_@V5%)AkLj5XFi}fFnQ&A&_V@CQXjqLNpS=FR}{K)amM?7!4)hwes'
        b'azs{H{CzTz?O!3MHJ}e_-QhHc#PqFkBWLzR_59>&u}`&UpQ+~sv0pQ??{}kaLTB>Oa8IjoT&w!52?-$o#?j&K=czOUtx=Y7?(@S`'
        b'>so)L|J<;wdO^+o-#{$VyEkn7e7O6ai)jDlr9B!zyD5<NZ^PZ6UPSvhFYW07+IItJv*Rb6dTaRbTf?!x>wjw)tbs)d5vTq<eE7}b'
        b'*msX!kc27O383HzQy0angzyc?kyH}|9{7Q#bhA2i5h<N<)v4bPAO8Jt|H<Kf{kJCmQ_{aNyz%$LdD+>|sY~LB`^50QKU$}{=Q(v~'
        b'A@JVb*N0DQPmCLQrw6q5M<eR<ChmQ8xc^m}xXGd#{8p-uxN79iz0VEzAE1eY-$+8t&f7M=G;G;BoSmz+{AT#JmK;@f?)1Gc3_riW'
        b'<*69qy3-*iLSYw2^C>NqPU_w#hEI&g7Y9R+4na@#dxzcouuVC)Lojbn_5pS1b!6}E;r`vU7V8&M{k@^}-wx}y4Da1SlR(UU4pqlI'
        b'f5Gh;*0mhcKRDcy6QX~7SeM;nd3^Y`rk0$@z5URH?5Ai=Cp0C0mG<5z*Q+@S`b6B%hxN_Fvu4iBh}ye#ScrMPs5C=e@@Gj11=*ng'
        b'>2Tcg;k<i<(0lf&VL#ZriRIX*5<(jqTx*X@M2HFf9iJ!15$zEVur)!mqG}lT=4*4+vFi^)LkC->c6D0B@ukNX#;!3mXJ31EQ|R<w'
        b'j|ybsh8!@CU5}I-sY<&3*tTQRliHo{Af5F!sUTEq@O+XT9TMjnKKgG7WIdE_t&r+xsSKeZvD)nYzgmmK7vHZ6{S;K1qaRcIxi=yE'
        b'2kI5aBD>XMbEGh-r}>b$P<Q;Am_aQVn1Ar78jgwwRXes@mrM0awL0+|U0;{jr_=T6#>eS$On`4QY|;>DPtUqTKt8b915L~6uN{8R'
        b'8uJ7JY7juX##vvI3<=pn#BGf$nzFsR*no$)=VSLbjvL-PZusF%(9efnQ1^PsMlyU@1qs6Rhh9_(<M;H5dk<X@rp|l;8MjY_>OPy&'
        b'yfk5B)^I;&d+7PdjhVv_$Ad{QGf&;KMcmNiLbX~5TRRGDkM3C9bAF)CQOCz;+u~-;NU_9w9+@?BNz~%Fl$+6^pQ17+uYo0(V=3Rb'
        b';?>xc{`herWvZD8Q<KNdd|G`pmBi1?UTiVPAIdWrTC!n7NFnr0Anai1E{(Mk2DE-wIOw#i!9Wk)6>i-lmBkp%(e>NLx!<@@n&Y}J'
        b'V{vG%UVr?;#uFFvGP9ox(;vH_%k0U{8Q&YH>B)o*{_Fa`YqxA%zhqa4^>Zjr)M<0?Sg-x8(YjQEECZIXUW;}ly6@&K`efDCu$-9b'
        b'@eBI$a#K|6ZoaSi=$jH5h$A1M_d+%Qw+BPE9g*tikHmd>0fu^uNr>2>`&yX(v0L}lX3tHB`tBeZQO1nMXQybk^ndo+cGE#kVh*g}'
        b'm{}39yT|R>F1iOVjLbh6enPV=Wa}ySjtekHTTX3wQcTR3K8VxmiVo>M@A<^E_FbuGJ7^WqGGXf}t6AD|s_*dju$X(twoi%48v{{O'
        b'nSJ2cvABDm+dh7M_c7t)IL~q2YgeuR!{IkByafXw+&g$^hwjO%wnshkPLJoo_wMa^`Ov`Q#B;oHd(^taTTlIE@8Hj+xA$VH3;NcA'
        b'E^#atbPX`5UT5=pt2*BEMasr64<`ufXEIfz>J)c;zdGiRQ}1~8LhIy~XVq(OfRzPrgb4>U0vLMj>OHNSPo8u&v`3Er>5;=?!;v)`'
        b'lGpqTO!al|e`%RuJu3Y`-S>W4#L%hw`QtYIc5Lh66JgJ!s6DTXe~1e^`-KP#RBL?~=Xz;~Fzwq+^|lD<bi{#;+ubL$iNBM65P?V2'
        b'nt1K>oXP74p2?gNpO77YM2v6BhQQ1W_0bFxcmIWwP*{Ws+1s`IJZEO@5Ux!X_U!Mmra-AN?~H7B$IK_f_-zkJu)Pc8!LTdA!7nio'
        b'GN^$i7@q6~-7o?+ej}#Ceh=$waJ_W+zb~YY-=#8m&TLyN<;|h`qsG1J0=16Tzkb*SuXT@!gFlku+Aj#2TzBYXvM-VJTCUpjl=$4K'
        b'#8;)h_Ya)<?BVHs_bps|H96yqdVb}WapM}Jw}*PR>b8!Xp0VocPKRk_#)oUcn%y1)Dz2b`oqK&&vb)~!ZQ8i)?)7&G;{{FPkEC38'
        b'{fe)04u3o2YD?XPoY3`e=ESVuT=Poo{c3|YBs=*YrWdGBXoOkY{?7b#aVq_Z^FmmT=GL$kGgQ4zXzp(;zc4VFY}oMip022e9**8J'
        b'`Jt@PRWt6|`p`2)@%`G8tI@pOXu1Fy9(veRpQD8_nTP#7F%EA#xaVRR6sE(A-8W(|R@irV@#~MdGcfYrd|}G;g_}GLhL^>Me)?dE'
        b'ijZVYk~%cLpW3rMKR&ch3nugkKi^&tvKq9Szn=$EupZsX7m_B2xo2KTnxTf@b(3<{eUmmGKOdKP!EDyne}!Jo_|{bF+)OgXUDyyG'
        b'NmG(o%E^UM#=sQQ)C<8WS6`GeDLAEIH#$j~pPHA*BL%;b{4)m9O%{G+q{r0pt&?d&WVZ`)m}@YtrZtim{y33y$qo4Od{9ckz(sjJ'
        b'4bEfwM?i|9H5CS!MyJvYll0x^<?)%sQqC-l(gmjI-#Rap2dBMxo)le_@s0ETDFex|-B0UwM4G8HexNm$=DL0ZZxFiQHYLaEwnmzl'
        b'u+GQwVtxa~hyevZAC!VamxA_tvPu-cW?kfQHni-jOzYH=m#O~QHz`?NKM-y<CnQat9kYfc&6uB*ahtUsC(4kV6!*}1<3g1v`|fL6'
        b'lZ+-41PWSbvhl(^51j7|%tJFIgZ0KU^qu!yB16jB&m|(4(R2RfC9=#qIw&PguHLyOX+}qL#(J7}Qrv%^H=Cn31Z1B?vtJYXj>Pi_'
        b'm`8VsJkg*A@jNY<$9#!ASBD;x^DM_aotMZH6Z(?G$8Tfh`Qs~a&X9>Hp6b>A@qPa@L+^b+=kx}qByVcHfku<$XcFiIbpBeW&=-^B'
        b'7n7)JiT*$+N2k-iH-I+|Qj+54o;PMhiG7i}9D0^vOX6n}y(yF8vd@bF?<R!~(Yf9N;^4SVZm7%%Ye%SE@%GTbHe-OB#GQ0r2&eiy'
        b'wWH398|wDXIDdAliruc*8o4*_{GJ_=vfj_GSzLQw{8<8?8EuUUd@<#`xD{VC1iaW1CZ=i!c1d6^bjC+*@VmAWwoy1Q$7Nru=-T;#'
        b'JM4Ua*m+7C7k1w3XV#t%XuIh7dfV63!R-EaXu#7G;FM+;UM>vD9_^BE*cd}rsDd_Er*m!mYA8mn-M9NCzk4Ko;r(9>f%P-cZ<K4w'
        b'pXII^LR0M@L$ur%HHO`H>v+k~fQs>cmtKJWZ<Kx;k?BMKEfIsKN4Hg6`=#uU{o_#oTdXu;JTy`qPz5x7;8!?aun~_R@ceG`p@3e!'
        b'J`{fhZ}RjX9TGvQ;_n9fQ{9O}vh5r9A{L&k7Spe0@dHEjj!|6g5E!CKQzpheKeT>J+;c;{$Hs*4o|Mge{5Sq;sQ=ePx_A{E>iEe1'
        b'ao8Dt2`^m8a|^yY9^-YSg|PFk?L*xMAf;7X(|@L?8HdNFg`ZVgVQs@oEMT?P<QZBtS$#Ac`FOEbs5rDxj6ZS)j|{a!wxAWJi>@^_'
        b'o{(P8G;zV2KX`5*@HC6d)`+cZj0vK96IOlbPf_A&@rXxFeU8oU`!Vr!sF2U&>o7j56|NG}gk?M}f~Qpp?ZPtjOE$YhhUocK=gGIA'
        b'tWcist|4j=3A2Iv5xlt5>>fS`Nv1o7;!H!d$umRF(VL0gU1qlJX=zj_HuHOmaW@a;s;P{C{!Q;$7)d(^oxF8C^shp!+blHy!DGXY'
        b'wQUx%(?Z<KXsrv69+P=v$&gU_C1?{9K&hrJYj^(zo8hh-5~jloXk8^V8q?pz^wfLZzdT1>(C!+_rwfMm?Ie`R$7lGl_7>pz2Vqff'
        b'VCS&(QeN0b<Io1?aSYQNhukKZ{9b+jP>M!Bmrkz+ub)K^aSqVPcbIY+KlO-T_iXs)p-o}q`?~*fPp<0Pv#GtIV{EN$8<l3}iQ>aY'
        b'HtaQdUg+8I!Vxg9p4}AD+en_AymdxOhA;&!rDb9FOq$Z`@!T`%noS<Cn;zQqv5+E68R$QA^lPwPZJ-JXxuL_XOno%gTc$D2k4}n?'
        b'Utg4zP{}r_96WP_?oH3o-Fu{5{p6%v^au_~ZtW25Cbky3AKlZd{p@X6+sD@|3lj<<5c)N2KT*A&vq>{vE%{6m`h>~5!j66}RcfG3'
        b'LIxxeXiEL&(aJEPaTzSLGi(3BbhBle>`74uk0*PR`e-FA@UswDTS)}1{*!Ysff|@Vn5pSFO*Wh!{fFm-s~}mZ6x#T-HuCAqI>&C&'
        b'{#$}f;sbh}Vc*7g&*?JbdNK|PtBA(fqucBL>p5LUR8K}^pMK_nrv5*l+xzEp@(nlG2HdY<EH{Gow)=HYMx?Qjo|lK2UOm@K*#Q()'
        b'wS3`{M%{<cLA>{IBHzr^A3c{F4ypVCTL1oY-M^FTFqVn#{a8mi)=?HVu#<R-B54gY-v6s}5Jw}bh}Zk{xn1h=aQ7~{gm#>B?_f&@'
        b'uR$4DeX#cn(IrnK<LkHk291wSEFHDSe51w&GX|4|gp$2{y_g<2*Beijj0B>~i#|SdAbz{S`a7w4vU=MFx<NEgNluy^YnpPdcgIUC'
        b'9~%Zk6G?niIxs15zqH*j_<;nxK$??}4|u}dJy=QHo!BO|f1A#Ii|Kb@o78@7`uDeNB40sFdkI6{<C745+PLO(uwTa+;g{|T+PKDZ'
        b'ruK8?YQ&9nCe_BiNK@W9Bfk_H`g_LnV$atkK1xg$-OJAT@0IS_bH1?oT(UR3<Xr!fb9B9Lh*#l8vFMy{`#_mqcMehmcVhE7-%gBW'
        b'q@L@(i{>}RM`01=K}D2YRD`fDU@v!Hbkl6_y!3=W6zCpVX*3_W=@*NZK0Rx}{wdECTJOz#<I&qp*Q?J<3Mim}0tzUgfC36Apnw7j'
        b'D4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apuqn('
        b'*kM+w>A#3-B&6d`=S3e7gZG4-B=n!9w7V?yA6O51uOesJzYpHox|;pV=K=58zZ*_S18KH2y6leC!SqnGh308-tZ2JL{k?>&fYARC'
        b'Cs12jtO4)w-$L|<J*)q4*M$We-g)z->rOo0vGlYu!wM*%fC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36A'
        b'pnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36A'
        b'pnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Vav%BvfsTy(`=JIUyt*9wJHjs}e~_enPy880t<uMf{+-QE$l5Wv4aS9In;mVrX%!'
        b'Xd_nuoi0zGnKvgxj#oFjM1x*5=nPpjJ|}%ny5S1+f9UPmdTem-o>LJIWS?rXE%>AT<&5Hc-u}95w0FtkA3X3J`M(TWctYR_g=ZW*'
        b'6X2Nz&n=a;rFn}ijt*N#OP*NV;j%g)Bo^12GYn#Z-R^3$TbitnTPH-2azia?cNSUOEUQUD1+ijYo^gdYBPpn^uB)gv6&2Tz*=;tL'
        b'tIgW%Bs5oAZ3Z!9>2<mc(&}<`I`d}FZn3#qyH=z(+S_O2fR~vnX49;su&Qu*Nl9&;SeqeM>9cBb#6pY1VS@^54BoM|t3vW~5=emt'
        b'!VU<p3yKrL*Z(={OOMNxL{jkhl5FE=Gf2U4gSOz28%P1BCqtTlzFSI4YU=WeYie*LSfqLZ57!pg)|OXS<<%6|7S~}~VtUpbXSc)E'
        b'otUoIIpNpfBnc%Y_>@<bR3lBvqCB~eFfM7jbbY!Z4>J@jDMnOQTv1U?oL0x3R!4Utl;K3Gs_Lr3Vw%mgu&!(_X>7B>H2B_QDsLC$'
        b'DXc7-OXxd%osd8hZXgMzBw+?gC?^S3Bw;a0fO^a%!CYQdOA?^<b>&s15HeMmYAOLkf2(T%7gkqRnyQLw3CWojk{_=L$xnnQ8J-*9'
        b'Nry)d&m4HN;h76hAv~4vEQIG)cyzGb=457N=j2*eG&WhAgBO@5OIt9ffE2t}z{bB1aC9LlSO!@9uWaKoc#<K$9`M(Yrd^(GeA`4Y'
        b'cYztgJ;kITr;yQJwASE>;^7<Mky+uCUwUdFNrN2dp}(pIm4Ez<x<Tz1f28%bd1uN=!GopHUT8}N;Qi2^5{t{ymM4~X0DpH{T(%W$'
        b'R<X%pgBcZ*3Fr4bvD3a166_tK)7sXY=CV3nVzRlqHbrc<*xIa3aWIz)O*M6T`fH%S8T5A!)_+<XlK*#jK7r>8cuJoL$zL-rB>$)I'
        b'JPFT1cuv7H2+w(V%<qQefBMUi{CT9rYHbo*?QKn@aCIZJ%;~Z?T%@4Q-gvv%WNov$tfbau?-ZMCP7Ac06t`O)E!K|4)sWNPNz4xW'
        b'3M;;Bw0Cq^8(pN*?y@_e(OqqFcqJ1nq{7y2b2&vjblhQUf?^>NDqMk8@pAB;%VD|G+Qt&dVzJ$?yd?p#r2(;koT4ExFT|Gy#aV@3'
        b'>|b@A-QMQ3x<Ib^1^qKrnoFUyCM(Vr_Ia_`hJ6#;Z5{q$DBT;gtb%Z>z1_+YZK029NdVOnKdL2+YKcs>)Q@Uu0M$}Is-=u-sZ3Sd'
        b'Y3pc$!G>S!DsQZ_3pz(kU8^8n)X4$895Bd%3^_1I4rI!KEIE)Z2Xf><uD3v6(cZH4-oo|X()Hfr_1^OJ-U{^I8uZ>O^xirQ-Z~7v'
        b'_Iv9vusSRqmNt8fud}|mJ}7PoiU-rr35sV1#j}Fq*)Z)+m$j2DHZZ(|BOYDK5sxm073ILZh?cNl7Fo)ES)>;7b^>cs*&)ZAqP2sr'
        b')WvdOsW)Yb95S(bOtcu2FV)9eCO>X6F>W#iEI78f3v0cB#oo{oZ)mAERGHxm&hZ5^eZeeWFx$(b_6~0lnhJ}}=9gk#ROt;H{IeP^'
        b'k=a1ASK6E|QqpF(H_;igceyw(U`X!`8N8tkZ)lD;l<5s+c|+OWP>wg0>nqu>5??KPUp0DPJ$he7dS6X?UsZZvU3y<-dS7h@Uu_1z'
        b'KKW`3To1lM@JrAKCm4bgE-GVAa6)EqLRN4>HmN8s5^LyhDg7;=zl-RvrO9D+vTY|Y3au-&gXC@$Ypfui<p?UOI#O9)TTLpfYs*Qk'
        b'xm+x)Sio?tj$=K?297g;A1uyRWaZi-vC-ma@((t_4hSM1vpQ&97%H#18T8;nv9@pl!$l^tz`DBA(gf>@Zd{nkgEfmu-C|NxJ0~Yo'
        b'tXVv}Zm}P8-dtQRn&@u<{pA}92AQa?2g9Vx(nfcBaWO+n7+T6uWd_G{IL_oai{osrqx^e(NIvQ>hLDha)LZfaqmCS28<LN9K^er+'
        b'HdqK4?SmD7(MGrfa2ViTz-Uwb1aJiEJAlUn-U%4(i01%b1^9Kq69JzD90~ZZfKk8t4Db}d7XVKM91$9lKMn9Sz|+wV0UV3%1AHyu'
        b'V!)`nn*m>kwi@8;0pAH&#P$G=1H1unJhlh$48V^8PQZ2nP6T`aa1!97fM=o}2sjz=UjU~7{s1uAK%WCfy>J9D>VaXPC#3<N2pElk'
        b'DS%CYlK`WFIR|hd;JJW{0G9wRMjH@t3E;(mO95K|mjS*Fa5-Qn;Q4^N0WSdjW55+Su7E26Zvk8dcmQxU_5<}bz|R1_8So*%H8{?I'
        b'K@}%|1YC#X40s{nj{(;M{u1ya><{3@X!C`I<Szjn33w@vJK$Sz+yO5GoCo+;!1DqB7vQCUmt(sDqau74U<=@T0j~i3FyKbO{eYVQ'
        b'KMB|hcn{!a9CyGifL{XK0r*wGcEBe9cVfE%-vRg?zz)Fg19k%b2jDe0AAo;^?Fam0z(ROP{#wA-1HK3F)qsBj_&UI?XsZEs0iF%G'
        b'4{#>nbig+Oo{jwitOHyRcoN`S0pA7qcEJA)*af&7@DBn10BsMzKLor9@ZEqP1&n(BcEE1HPXq1+{2Ra<0KW!!BlZjMCcqy7-i-4A'
        b'_(60<0RAc9$q^y>KLZ>G_#xycz+2Gv0K64&7T|{g8v*|u+YR^;z;%Eh1^i!t{|9g@;9sDP3)qAF1h^mYTEGLiE&x9U_~(Eh2mDLG'
        b'+W_wc{7b+u0)7JL1@LxU7l5BcTLSP7<Rif7EcpuXPQYV;ccHuhIr1yO(SUd3d;s2qd<1we;2Qz&16%?4X&h(3`vG?V{x#sc0Y8K7'
        b'1N<!V58wmXZXq-u9Ul82{yg#z;1_Uw0lx_N6~G6P?*ab?*Dv6g0DlVj5a4rw52KGm2+2Q!?F9TX;Hv<?0yqZnZ;@XBAH{J8{3_sd'
        b'z{hah0lx-#9^lt;+yVa%@Djks0XG6Zf&2pa4P3{7e-HS-0iOiC4lvr14+2J8^C7@*V*XVj`G3Uq0`WiL`T+cAT+e{t!g&DvHqHa!'
        b'zo0z|_#NyY;CIo?1pFSZ3&5vwT>$<o;BNu{4d(^$8C>5JLh|3o{sOMDyFjV4ceS*NtyW8?*bI7ARei0vqN};t>WCw?VAFv4<rG&s'
        b'Y%Z&8V}gZ?8--d;CaKk`1hrb7rB-Xo)N1WgwK}9ttq%R6T0L%qS{*i^R)_Cbt0Ru8)#H;i8q%TBsGikm={~dkPD@*tm80bjtE<b='
        b'VQnInwWT0c7w6<hMo%HyFd`5X;>oGHImV*03UeJn*{Gu>XwWtvM{rQd-DDiy<3*QU1RE1t4Q0<vD4W?mGhy*eOzrBR7G$BN3%Arf'
        b'aUqREjm1=}Z6Za?bOj5y)e2T^k=^d#L1vN?b4$Be+|fj!B2Yll@zrFdO0Lr{$;tFcQrl*=cA`BSXbFpHBACw>N2=&*wRSLFA)w7='
        b'_I50$ky_af>m6O71T=y92`UXwq^390IINDY4)Heo3aB2Y3+k{!vb{}gvv#z&T19(vGnNibgMQhZtvI@V#_fM<$tCNQ-=;&I?O^MI'
        b'mbMzwyBb@?&Nhn+<4t1cl_{Am&6o*lcdQmIEf!k`ys$ce1KULllz>@Q+MpK+b>>B4v(4dj#c@h_>0*kJXaRI5RNIt(>E?FYoi>^g'
        b'Ih!^!4Mrv1-+A+=X-wat;mJ(rLHNgHruQHWPiDFg!h~q1{~%l)&2%7y>!O(+gpd-=bRmSSXr>P#+!W1pB7~cxnO=m@7|nDTgtlm='
        b'Cn5Yin(0aid!w1Ygm5yN=}ZXcqnX}>ka#uQvk;0PJeh}o2;pe%%X$dHSM&4(5RT#DXmd#ZH9Y*stFezwWWyVzpaGs$Z}@y=D*mhH'
        b'SmWn2CfskVQZe5#;&DDA8GSF9Na<80lG9%wd;N9rAN_gz8jykTya&%;uR;A~30X=^mnvr7iQ^S>Bi?%KM*Ad9-ZjtOoU`+{Ph=g;'
        b'4$b`OOZ6Emk3Xef-WjfwKDs5{+-B+M0Bf1aK+$Qt3mDPjgay*n)ritBVg6j$byX80N|{qm)Tis4#am`3%oKsiW>P2VOv-Sr*0xUS'
        b'^##F|myjSP%n%bw#e{M(p-N0xH5ViwgjUUMvvpWSD3#&b3bU9{C?+fx6UxMd0`Z4poH$QxbUE76R$*aj<QA|ks){O#^9ZbALcOnf'
        b'Bt9Xn(B5Q?PmLG3)W+b#4iH>^X=0Jp+32u!;+lv@zb_>U=WoMl_V6N$%i>zyX{7<|NV~-qeu)CYD{b&tRzW!vBGLdvatpL9kN(!y'
        b'nd*x3imDgZb^FCl!SV8{ZqnV|P3Bh3HsMIo-V|0BLFaCv{$v)m-wrRW4u{>52X#$|sIlT9f>%DKlT-)?B#~tu%Q~v6p$^d`wxWr~'
        b'B%Hk&<sFqq4trZ0%&^VrB@!*o=)-GlwRE&#XI-uE(#d+B4izU55jerJ%I0jhIB%yBs1&4V2MgO=%{FUWQ(iz!T-gf3SuO^XMICpg'
        b'IB8p;VJ=2eZU*a>ny&=iLD(y3i8T*Huq`lbSp^se0T_Y#;9>StNjR}}xU4N!2Wf7zTU-PiMpns<AP!5D&Ay_`<+67;iLLX_Ii%C#'
        b'bgr~Jn!Lr7)>JPv<Lp(})a8+aI+zwT4FRQ^NlrGYDz2`qCHnMCqJyUdjGDB=A^G{!!7h3UY#+dW6OR*1kBdloN3$JT>^(Lj#dID;'
        b'Qe<7xh4EX=H3d*@S#>4OdR;{|w!u_m0<K23Ah(oe>LIC=<QnjO9_h|X)urmXF>ei}s4>F$m1e_}1CK$6KYIAdr9T+W#h1BRB%P+@'
        b';!h3~S%`GG2KdR!f}c5<bq>CrlL0?iE&M`aB|bn}30W&MFp`BoP+KMBuB2Hq@qK0n{y<rEL@Xg<Ex93;q@@y5UEy3kL%LK_Qemns'
        b'BPGy7Qe14Vsjeiq)EC#}p&Uskw^W;<i?^5-*TQdA@gj^CS1qipO|7XTI7X?Ysv3w2AV5*=Tw*RvB{e0fq`Eeh6cnYBV!)MVP^2nM'
        b'b!C{(Tn-tE@w6?K)WXZ!V#rlf2V{k&s#J1INqJ4>B2!Iq9zSTHQmeMSw8~ULn*lmuZC!PZsT60Zq^7u7tSqjqu2}-HqMCASJTa2W'
        b'vb*G{2oF8w@+LqxAdZC<RGVsw09Tq8L!rfHu?882h-G)tT1^WVi{;1yoGXipYYU<HcvG7NR09-OxHRsB!MXtj8%wT4k57yIMwjM$'
        b'6D08BDf3-a3`@O4DeOg1A!Q)fL7V8bH9GSk3Z=ETgWluBu&gpup~!_AOm|&zeQ{MCcE6&$vK#|>WhAeHaXlt;nO<Cl0uQ+wW+#tS'
        b'*=2<ig;a~p3E~OF9Tr+y4HE)$Rz(E>i<X!cR^a-mG~1nk7BOV1p+A^hnx|(-N4kqJTm+$fQjQvHO;-oWGk^k$0&Kp$1yxZip`)0`'
        b'5L1T<YQ}j?!KEi3q`ROQYN+UdpQ1WwOm|5w{=j3#v_*y0^cNGW@5HviQ`-nXW$<8o&4_U=cb9jtpEPJ&$s(B@Nq0gawDu<GH>mqH'
        b'Wwk{Wb;Z>smEz5!Xa@TrKTK6%hNmG~RnT^ws^F0cs)A#aR0Z7x{nxYG+ev%-Y;;!xa#|bz%Rri}Eq)<<MRP)g%;G?7O{>Iwv1&O;'
        b'w3@nw=H(UTRmEg>JE*Gk{CPH)=+5*;$SUT~g{*}zG)=Y+&`4`nLxJs1a?!ahNky3^(}Lk+X<FWhWXqdiyY;=GCf6n3P!g)*c6BaC'
        b'r6HIo;2rw=*%6Lx7XW*=+Zr8q=)WDfHhozKY~;4~u6D3zI<1g`=Zm;8fuh|AO9B=EYW1)cf>vN_w6wLY#xm&Eh1(PEsd`XF4C$Ha'
        b'xa-!ndaG)MO%2rW6;@e&5}O_Nc1p@^Cz0BJSVSgnlpVOgrPE^vC>-nw>#9aPdbD&xV^-Nf6R|?=`Z+rB_OiRu(Lja$Sai19LEp#Y'
        b'Nj!|StY#&lz12y#aXYlfB{r?@ut3Mzj*dr)R?uy%{K%5pZv1E@U96{#GGu0ow*!|u*@=dHWCH3&c?TZzvF)3-)oE+#u(UbFWNMK>'
        b'|LrSN0<(F&x!)l#Z-{*U%c_;>(#1-<)5YI8#V#kv246{XW~S0$uWVSb6Dm&ksYK<?m#7B@1{5W(lsGNz*1(E^D`4msBOgGWL4$xg'
        b'5kCsDb#!*Qyp0XW#mqYY49QODI<vrKoy>_RFzEKjT$Ve*Oth@9wb@*&q5X?+UK?u6mA=eeJ_fe60bALK(h7M8n71+mmGjCun9c{Q'
        b'Rwp{a!h~E-(T0j)GtF5m-XsRS>5yxlSz~FZ9K|Y|>0b-BL+t9LWzcYweI+as8w?}nva~gJp@Ga-Kte|D9GW#DGb0x@z)mY|Rom+S'
        b'#5L5C#R;OTm!GxagwQuFxFDg+tE^7H>8?XP*2@QASGTp{nuJBwW`o?&SWr8ep$uyUOZR1_&6SncgbY}7&{P{Jl^`bQjtHEA@(D;9'
        b'+q#-qaUg+QUASd++Oa28d^Gc@NOkHC7h9yQ)ZYPZ1(t*zNOX3s;KVlXdK2jZ<7#ZOx1&y5duN->Q9h4=U#HC$hZ7Ar7m5+N%d}#r'
        b'wbSBYl7uPzY%TaTnYNhnJB$D|2Vgvzv}uJk)@*?V$oD3Zo%Z8&IjAQMrUmAvi}D!E4m1juYz4iy!DO8imMLW{<PcsewxHBNt1ZnC'
        b'EsjPkwh@Qi(%9GqLFl~&`ws0vRUQVNnnUSgfpsM;TC{Rt##W19nLtljML1?wuwolsVkdL0SUMW5@_Iv#Xlxa`(B@-v!JKfk(vH<W'
        b'-w8H~%3@ZktJOm1umh|ui_95L_A-!p`5L{nz>}xR{|-s2SS_;@3hz|0m|iNu1~AtTzdnK-4wBo;f4qX!0C9nB<N}oKYcTb}?X!ci'
        b'&nCMabgS<onY{<jsX*R^x7r%911oJ#=KDg~b?IWbfANwd1N(Cu$PSPLHgqHc!<d1iJ6txp*~-Qu=Au$X&WDSNce%~_T}G5Pkq_$s'
        b'<^cM4g9-fq!%jE@dl66pTi$&C2`V4Aj_+0j<P54qUI9*fvy1hD3vwrQI--VTX>3J*3|rkys#9fyS`~D;Fx3QhLa~PV51g_zBXqa$'
        b'O0V{IE38;5Z(1#FE+-cYv`~~9D^WuFmu!(omhM7S^K#f)TBz<XmZNxe*kDo9%SBX5v3fBhtXe0%JH`w06#*I<7&lG6&bRuxn*I9V'
        b'U$vF$g1DP-HO|uIvV#)FwLrY@(L_Zq+n9^xJ(ynEqB=n%w~hRF<kWy1ax-8EP?R%41;e&twU|(r&lC%Kx9TQuVSZJb+ED3%)ULo?'
        b'Kb5r_g%oXNP|Nvt!d@|INTpSxqHx8E8>;!;G!YjX>ltoI7HkTYo{X=&E_Hq>PHf=LeS3$<RdlcCsUcnV{5!26{c+%Fk>2^^8ab88'
        b'clzlC>1c7Xfke*|)W!-xiVkawB`7z$$Va6)W`zdRg@c?C$aC0ikROhATm-m0psyD0bH@$IMOBqrtMztoY0#6#+o8B-8|CYu0=c$L'
        b'g=iby4OxlM<xVgYtU<~=)8kiIT`R3H%`}G-tptCjl@)vMC^cDEfJ|<rrxUn;x^U=Sxar9oJzGX}oPGTS+0914=1Ld&G*E>B&nQrG'
        b'co$K}Ocy&f!F5!coq=0sU_Hq=Z6G>2#T8(u-A+%598eYnU=Q#!#%Kq9jEt;;iYLm1Hay9IZMH)+(D7pXF8V2<cc@`?q5A<|2AFZA'
        b'61V`ZIC+l(of6jpUs(J?B?xh3b2(3ETUU#%1Btl__`gGZQ6~~IGR0)v3GvDyZG8$|ajhUrxgg<7qXiM$5Swi+UFd@a?LM7USWtIE'
        b'0hbq`P?hRu8)j#C*CU%Iy2wGWa<k9B2TUSRr5Ku7VZpjssdTkcQwG_pG&@x+%}GTcAydL~v(x=AkbxQuD;1CN0+Z2d;M3EAva1pG'
        b'%jBjm*gYwWrUYj9j>mV*Zdvu8v&-7}%2pfjsBFX1LGhD4K8qMxx7KSkHNs#x7)v^_3gGBF?QLC5Sjam?d<W`|ZSk^4fC{l@abBtz'
        b'M@Q?2IL5dRuwq(MCmz5-mV`9fbiic+vxYhZnxDK~P3-g$epXYB1ndw@lZ_B+D7v^A3th87+v#bnc$>Y&#|4mI-mh2M9k)9>EwB>l'
        b'2@DhcXbpKg15LZ#D?(Cb3G7RkHzgdWB5N}(lnyO@LA77LNpYi=)3HrGom6$TufU7IURi~Xb}O3ge2M9)6Q2bQIqAg2w^w=z7bcn>'
        b'cFICA_$4>{F7p;t7sq8^Hru-#u2!$KMNtH!*uqY&t;}$1M^V*or4xzV03GOZVQ$=IzjN*qw2!`X?)fm4UiryvJE|Qx{aP55i*F|0'
        b'J)LrPy8n&kwlusrNKd2Ny3k4GrNx%Cr<Zp$I;_ZzXuk4S7Z)&_6XT90HhZ^DS_FCx(}~%iYhY6cfksud_V!df(UIA*(d!r#Z%KpM'
        b'U(WQ(R8e=UuMBEd%DX8mi|<?B4*Av0?i_e!Gn?xGuNv&8E?lxL4of>Mb#&RZbRY>`qBiJg9`@Y<Y64ziw9}!dsy0+pUQ|)cjb|vA'
        b'N=xsQT3wClqDfY#S#f?RYUuT&rO^eP9<jg*6Db>8tVqx!>|jzr{dOj)!0@EPRL%ywu1^BN_+t?$xPh&yCWC{0J5<}$MWsWt{Pzjm'
        b'a!2K>3)r4|FT5|2>rpV-WNn*j&}@h;P<0zWC4@@ayfZG3uUr+{B+N!`nhkwqN{*cP{X~+?ZqC&mjiR}{hzfjqj0ao*d6|h%>X;1z'
        b'P2-Z8xmeIK$<~p)uKr`zCMelz^{EQTZ0X`cbS%J}mFgg&)5e$_2f7h#NQZ@~nG0pl3pZXm@tmA{S8)cpqn7!j;DOzeDKns;uon2L'
        b'Ws8M1)wl9-s<_Bx3Rk*VB&(p*zhG<fj;U`vQPoc4CLGq+>aRw7ONYv<*>xCMrF6<m2LIm1+Tld5<n!Ze0d<ma4~)%!#$aJFx#qIt'
        b'5K#@&DR0rJN;X;Vv@v~|_KUB=cIqgkniW@obbgyO^Mc`EawF8QaHhV(G@}%t{qX5wRF!m!$q5;`hE(QSL>neEBR7Tfxt=;c9TuCD'
        b'>Oss;U~A@%c+|AnK{sy^q{>yvSDf&T9R^+&+Er8|@TyU=WS|T}%_)8>2(Q~v6Q#qt(&ti=EiS4$RtDwIV_Zn9r1zPa0_UYprAnJz'
        b'BleVD5t48C&?+xgu4oiXGjr23{&V?$*8r&Wqhx`Xi7xKs!tc~5lXuJdf733@#pTm_i>L=jwmxO29i3^cD%mT(VZ*e82uks~O!1l*'
        b'SmTz)+hx5BSpf_w8+FQfy@ZTIed7^-sXoM0PXur`%?t0n+Eyy>4fLTjL+2~E=~4~%i4s}x1}G4|L69fH*RCsB!2T@;o6t#T&(99_'
        b'4i~>#_uWn5OO*Vd4PrCh^?^YgvT$P8MVQG+uiyRWLS!`|Xrd~!^0-aFEihS_*qnUEopz?|23(in+#x2@4!LZdDbzb99~j}a7hj7i'
        b'v*i6S)yCvnP({>t#cJcM#s3sdZY*WpLYd!@U0lc=eogmVGU!70=Nu5gK|JQ?<?{1s`Mg+EZ{<e{F!odyp{yy*$Vs0Ao7if8;vh>p'
        b'RM-NTo)n=_;I1Qj0?J$nKI;w40{R+vdbR^zj;LKel=W(-m&wOhf?qzioq$A#@@G3_J+T?Dy2z|cckPZeu=RjjsIqN$;1Wo#s;@<7'
        b'wUuguE_tNz0-POmr`4%cKXG&d7qacmiSuQr3)%td!kyHizRGuR%IRl<<AR}ja0{*&`p4lu<x=Jgm)&=kMp@NqX|{sJ%QQ+T3pI)+'
        b'T-iZt9vWg7l`89#^u8>+7y5sp)Qj7i4*Mn$>(VpvBwXjDTe;U2(bdTg!s2DUAzp0m>S$!%cj{_)$?J%o7(%%#EjE|e&bfFK_vw!G'
        b'Z-Lm!5cewj+o1ICW}RODVZh}^JlcSvz<Y>HuwVeI=Z9eahh~>nSY)Njh6j0FVAs(hTUb{JMK@ClcI{eBMs<bD@r1=Gm$-CC6>k@F'
        b'pK=$QSe!<WD$wF(;(%0OVSdJxlU=i5H;A27BHNmnRp&jn`ww$RPvQRm&t8z*hSx<eOtktOGZvQ%G+w0eO=(4OQ7u#J9kxzUfB9Di'
        b'-<4`=TGAZ@$AO#Ib_X-eOAR^x5*HMiyk#ADdk$VuKR9=T>u4(c64YX#xGq>&@?XIDv)@HG1Goz!;9|h#7b-0$cuLYqp?u_T39ta|'
        b'9RUt^xnOo~%`Z6c%K=a}bFNU=0=r_6F5-O^e$M5);9_ZlUFC;{cD}XPp#Fvu+bU`j;&$91^OrXTGqPiI&IZ)DY-WBh*fQu%gqAK~'
        b'24)vQip4?a1U;xTYpghCBG_>b&|84z`2qY)^vKcC^j741$$Du61IA&a+NexVwIE&_tKxgCbu6dSTsj*SFUw_@zF!W|4!dNl(a*(='
        b'<r9A&HG66E+AM^cuJX&Q%*>2Te|kEaE|%iE2*Fbsj|I;#o6}@xiu~U1PKr}b^Sg%P1a5)7tPyW!kW$~}iHqx_2fOm=FFiMPa_>ay'
        b'f4+~BDj#aLdHve3YC8ErYby70IN0qHbW-?TMUX2q%X*F9>7-8*rWWw~>gZlct-zNZR4h1CsluDY?M^eloncK~WOoFJQl=QB%7<Id'
        b'RQbqV&f)adf$j=u$fCk(z6w(PFI%Lto0s039H{~KI^@p!-TuJQp{h%o%bwO^Pc2^M!qes^GM`IXpEXTpAn4L{Ivp|LEeY8|20fQu'
        b'F6p4x8m!*QmXF#4SwNOHj9<LTUXjm)6xG1HykE5lE-UD50ILPP3t+igzf))aH}z#GLIaaHbJhCJdc9nPtDC7~lvxA*Xh@D+#K1hA'
        b'+6PvjGt)bwfd`O)xIN=d4?JVzD>(3Fr);sv$|yY~3qFj)!I4kEE`4f6U`bv2NQzX_L+@sEA2QbzcSWT7j*L=$=RB7_!{L3t^hplk'
        b's`{l5ZZ3U3<NK-tNJzXgC?Ea@encbqghfm?n`=^JCuf_r1@HOP)Oo##mpJS2I*Zw4b0#UW%6|z3swkaun@e73^7(|<kIA_>z;#U)'
        b'r!GldD$gc6u^@Uw4m(8P%hdm5BJhR(sYKu#zY~d|viwdXyiM`?xqYk>{D!imoXVW!B#m=$nqG%+u|xf0XE~|$)Bj}=OYbzx>#xM;'
        b'QfB%F2^8Yo9gI0r<>F;l#SQ)<hc~k-QqdWPI|gpnoWqmRdD`is>zWl_IVXjb*d6q^0yu!Gko3>r=uFDZ4R9Z)p$Z(BR(^@JqD!R7'
        b'uIF;*aVBa04qBft*-!Y+n87o(`+1UilEu$&9F&WH8HXh{dCgh2^^i0s*I^cUj@HYFtbn%{$*arzXz6uz*$qR*1D74auENyI`3_UB'
        b';J-`drz@3N0rdoXr~+PI)U~<*M^RAEf{V5K1nx!eWhS|-|0nfgze;M50|a|_X|KcOeHNGZQh3)7x*<?l;-53nt=n%a^L^2U?+=CY'
        b'PAw-C@gpwzFKvVVV2>HRL{Bw@F6=tj3z+sx*x&sITc6C*B=n?;4oC;LsqUl#8~?QIa<(VI$=9diuYvw%fK+DIo7_bFED5*P_@MYD'
        b'8RR57_<UP$u~Yvp2w?Ak;I2vspoIEsxZx{LGgn}IhL$t%yIMR^7H&Ly`z5jj{E_e#sQfb!_Q%(<pe#iDou72cw|Sd=9Eg8T*=BdT'
        b'QdvH>`kh`W2<(x<UvclAEVX%Rz_Fb7^G00ZW@D5IvtQe_!T~!5s={6!8iW~MX=$d1lQ8k<!miBCLG_g9b;|50)A(C`sh6|T=*PY+'
        b'mtZ$c_gY6JBWI3Im#Wui8UPtGbQqhHrON@7nVkhJo0@CT1BNyL!<AZruc3^>z}up}6(%nZnMneqy1z8w8@s%N$Q$HrzfBMi*jt$O'
        b'LC4cOuFN#1=AN0Ed$5tC#z3VoS;Ej#hD;1`_)KJfTm4!b`@3pWJo}sK)_C^!)DOn9zojmj!TyfAZ3g>W=?7-8zn}h}1orpRa}(L$'
        b'N@pjrzmvW{iT#bVl*Il%`j(mOZ=;82vcHQ?PiB7;-IdJ#9y&jT{VnvPDeUi{RkPUNKwD<9zkeQ^#s2pBr>X4QGsCIu+cV{9?AtRx'
        b'OJm=j`5=vbd!{6veS2ngI{W6#pVQelXC}{P-<%nk&AvG^Q^&qJbCZsJbEaL#zB%)Vj(v0HcRKdX8I_)Wb0%5OzBzMH&%QbHjh=mT'
        b'CdI(MIdiLleRJj~2KLRFrwr`dC9fISw@W?(jNiJ{W`yM9$3_i+@xy-&fHRQ}Fn)1#Kj3VRa{#{$I2Z8LIU)IZfENJ15$6GLKH%R1'
        b'o{N8L4)`X(J2LT`fY8oN_RX6Mne3Z4@mcJfG59z2w{X0SWBf);Ul#iY%<e4q4VZVb*f(EP*&+F>@LL<%>{}_Tve~yqzR70a1i|_E'
        b'4WExXV5q#Dko<*!3v)yA>jA%fV@UoYz@vZ{1Fp*t$zKBa3BXGMe+Kv#z)Np}_5gkW@U4KK1>6JpZ-7?;j-MBj-v@Z@Jp4W=A@2dc'
        b'7qGz?l7AoIR{;M6@cV$@2OMq+$^QWGe83+9ZUX!f;O7BP2ZsL~@HoJ|1;AH;_XC~^`1gRP0sa*5y?{-HA^E=m+yJ;A@Q(pM4)__s'
        b'+X4R-@Ik;?MIrew0saQ?Nx;R$Aviq*d21Pj+ltvbiYgDuU%&FTdGg=mADXW!XkDrb_#1wtSq=Hu6|=Rap3lnqSutCikMCskGN?Jt'
        b'BfL&+&>z@iJ!M8!!N=9UdNiEoSKot1%V}Qu9yB4mt`ENl4UQAak|9omWAbp0ug^%cegWjaSyd2Q!RW@xbR~?2T%w-ira+o7-k)nq'
        b'eDx$}`Rc)Tmj%&;^LplR8XWsFzdDiT#ri;+2wwIt{Ob92Fb%IqP8-kjZ7&VU|KfVaJ1>;_XmA{Ro(kjxfzuql0?m(tXeMx)KbBs8'
        b'+`e8A*tV;9zXwZw{rMlial^UTvM6v2Ci1d|{b)M;Xs|p(5MM{~v7S`sqgfp^KdpZCsQ7nav8<G`OScVamId+7B%WScc4;2fT!Kd@'
        b'^YLyhyF8CZ2h|hJ%euSl@?&i*2psFHInAarAHQw$qsOuSIEW^O^Up~?ny0e^=O=o8Ak8(L=5*P2U#C+z%{M^vCFi#Z<-WEd&Cc>b'
        b'`8Ji)#FT$`nrWOSz1$}gweth{I(Ane?@Z@33(7CO7HEGK2i6nI=kfN-(BL@s1+AZJxeVzk50vrr`!C~|ZsiH$>+3jQuZMgC<(FQk'
        b'Wt>Llo$EQxFRwsT5kw>M{=CTBgM9Qx&{)4%7RU#2yq<qTzD3uvdQ|fR$G{v^PdujygM8P`XEc$#p3&G)ItFz?G&49&(iLbH2hk*O'
        b'n*1x!EDNGZ<aO1||L$u$iPv*Gr$Ii_1dTzSUp+X+Gx=CQF#pnP8|!fu299+ym!(f$fu<;kCWXuF7w7xd_UrS5_L3l)S)3+xfsYR+'
        b'F9__<!5|*Jf%khV&lkbh9DY}1<^smoaY1V?mDAj?;Jc4?8mB4x9yIBk=D)rN&1_Dy@;lJTypzMnZQ}x;JeXJ>IBv&-#x0lAJhi|l'
        b'--2n51<~Yjn!|qeoP_Y(3w(2YD2V1pPIKl8^}G^9lh1kd%LSL`w=+S!Gndz+t?=!0bA$HnlR<0lCZ2Cf#pUbCFACfn=W&`uzk0GO'
        b'0{MDbQDEDQJl`*`P>)y~NMqvr_OpKVRAvY22Svq!ZClFs%vU)Lj`hKyec?TMtgVdZ7Ebf-6===`(JbRMUtEFa!yuaFoJLc5d796H'
        b'Xqxz16@lh>=4<niCZ{rRU+D4M8*#ikI88C+`x~bT-cN&RR&koeK=Y^XNYl${ZU>rwd`FrcoTjJJw|*Xi@c&e@@8@g$XmC!EW<RGH'
        b'@avDij8|QP<~N+?(D$IJ<KJ8RYvsjzmdtP4OMEn#hW0bs8Rsi~@;ag_kj7OW$fNa~#!}@Qg9$<Pyj>hv&mvCq!>UW`V#qs>JQcXM'
        b'7jv4QUxCIGM6-m`9Jm6_<3Th_InCQuzIFOp&=`Cjv`*2FfO0*pI&iH2ejp@Y)(;|g1=h2S(-c-;Ugw(<L~|>rx%CP((Lprm%fLRY'
        b'tiHUg8VQnb==VU~<$-G77{mqJrzL@7fIbqG*FOiE_tidq6u$vh7|ZtUKkf{a-|INd&P&k9I_%p)H1~48zFa-Qe2p~sahikGKE6&~'
        b'86<nl1MRt=@Nqj)?bF53A954a@%L)hwoQIIIp%$z(|io?f3=O-3%E{^2apEqY4fwUsegjgj9g)UnhFBPdXV$zRP*I&9t^V0KH~Lc'
        b'nSFCwWe((>{XzRS`l)c-8qAj;x7Z+gfIcm>Ydg(>`WyYG<<A-37qo9r<uq%qK=X7E4f@KEM}KC%JdZX6@#u8kpPlCK&O7Lf!?J(l'
        b'SI<8)19|e-L2X079hUW``Mc|U=;I5y!dkdg+dkrB@X`0E=O3I#ee-vx`IysO_dRGn;WRnlgXVEQ)-^Z##=7C=K-s$`NLFp<^_;lb'
        b'x8`Kt`QT=@PSb<zg%^1}ANkdDKDeI3K;AjXX|AjB>Bea_f&LH@)Hd|Xq777Ab9s62V30gG$!Tt{@vXVlHGz9Q30iY93_!j!^I00^'
        b'd%`b{?cH4y*vHw?zB+JzUaASycV6?0BR`(1@#%Wl-@o|1M|t#-UmW}TrC%I%lJkCX>i?_t#nB$U+AofCdaYj^ZSX|DIF8YrT3`Rr'
        b'ZZz`v4YJPY7e{-q!Y_`tT&-Um?X;yle$7L}nuxb%<l84{Zai`P_*_<Fli#;$kAXU0R>+>S5WWlWg+k&HN+IoKmIvaHujhA<FZh4|'
        b'-Z!h`#|Q5QcNH<C<&k1v+A+>Ihwk>JeU~tqNS)WjgC>v>eQFX6%31Gg)kLpQB%VXOjRibEY9oMq=6(M!{vr*Qf#WV3FVL#Anv1ge'
        b'eN6azU};T|A5ndU8iv|b1=@C1L1&h>pcS4~@btjrpQpCCrrcB^*4EV&n<_<9VO@EBF{vxAs4A`tN?cT2P+MKN;G*<`iiO2>)zx)n'
        b'LFs0Pt^I$o_cnk{R`>q+Nt%=vsun4Viu!=Ov{?E^p|uM%Nt4n@U$Q0@P+S_ClxC($mZYUPHmjmThYFSb#H)9!PB)zH%ADS@$u{P='
        b'o89nr=-j4P=EYsNyBD_UrUUKo^F8N0d7iwq)NObF-~C?$-+s>dp7+=1oaZ^``=t-eBwSUSD@mu>KG2gg9|wWQb{On?fTOj7-iG}p'
        b'*q;Rv?w3SvM>F!D_9I0CPoToK<&nY)#(sc?Ek0eOjmj#xMVnis;I#}9bmA*M3q}U|gZvCKot)no;s^Q@Ov>IZ)#U7!>FxuoQThjl'
        b'Lg5gVJf<E(rGo<$R9u}^1C;aAZUd2!lsF=Vwa}3PwxHA7q%2j%!}Scr<NUyKs6R+jG0AnM#pUU!Ur|*}V#$K!vI+s{ctWP{WOP$X'
        b'wV0HbBo8vGPSG^sN%D|mX<K!f>Opr^J*J(5WD8o5BtMIx6Kuin{8A=c^oQzIk2;Y!+>@shE<%J%B12jOiCYtX99mUO=&94=UAaWW'
        b'MaL5=MVurhEOnbs^|nCsmbyuv<!O=Lljt4tn*AoaO)*ihi&Di=&wFt3M|4IZEvs4n$c5PqRoi7jW4fcp>{1fPZP`RcrkbRalJab{'
        b'+UsO2<szvhKQ5`i!<~NN?6m0%E?Q}ctkUXL$lss?BP2AAU$a)=fh|b$rQTg3CJ%v#U|wnA7V_v%(D4mLWpF_~@`4mR!utX(HeKV$'
        b'oBZUyGG~f`VA3CwashR@U=v0~sv8|S<4Pd1l%U(J2<7=2E?-F;vsEno*bgsEa43{y^0JTG0xj!U%X-#wIcxEFm^>JhdA(XrEL>{3'
        b'mZ3gP!Y)eA-7MU?D#H(DQo1lHLf504rBva$<x1Z`zn_j^`UCtVlj^r6r)Twez2?2uEmfFmk_ec$wUddP5!#K=xT=YPdEIN7I7!Fd'
        b'xpsuq<jN0kDWQlEt}gnWYo$eqI#H*qjRT=@fP0cMP?+mtHHM%(BA+8FhEb%=;zG<+m>+Cvufl)bXyJ2<&W8f`YW$zfOEq)abaloL'
        b'rY68!oy9CyNI<@nA5YgSbTuu`gi#_0>s&p7(_}Hoj=3ow9f&2e9Y~Ap>KyD-M+q;gWJk@Hb4iZk>9eW|h!bh6V$d0hQcvrT;+{?^'
        b'J^ITOeyfbNIxkb3D@-Q<(`5rH!9jF9_;R(ejEA0-JQ1Rkzz*y?@Yf@ye3NW%=2+Xly3>(*Qpp<Y4f{8V*@7;<ZHoKRlMl==Tb{k&'
        b'V5jBezb4F<AAok;E7k;uVQy+OTSnndd-d00C%vvE4~TuKBWboQ$}?Mv_X_(l*b7d}w;cbXu)hcU6NtZL)L^G|ndJ)xdkFjQ(a&l2'
        b'2eAj<u5<5Z`Ih}(6z^u1511|gPP%jc#bBr9=sMVMxBzJ&eOkZlfd5V4o!qOfVLl4`ah<&%_G3D`>t|-mOFDZD?sr!kxGvx%%=IYG'
        b'f%`=MM__*uwC_IQ{wmDIL9^vPX)l7g8uaV?Wqx692088%_Df+7fa;~a59Uh5KP>BK3+($rij41ZnExGg;PVDM*DV5nHSpi}dEx#V'
        b'-2Mz&_j!^3zrcL%X0xS5+Rul1CFsq2gnui{9|pZ4?OiZmjy-A7y}~{S`z;_Q?Ym&U6*NcM_rv_GA>T42?a#q}3>1*|H()M69^BGC'
        b'V+i#DDwp<Jm{%eHduj}J+D8^6AKl>XStjfoU=P8*V43hAh4~gxk!+7$Fn<-)E$v@}`8m+ZYSI1&(EdkYufIpL{}}dgt%(05`qj^1'
        b'fAk(<UjTd!cIy{K{my~^U%(!d_46B;wc9xSLgq%27owBE*d`wjsRONC_VHCD-!aTZGY^Q{r2|}G8c8Oji|0!<A&q^ZO?~hj4+@D`'
        b'0e&Mibty<pFcr$`r8Kpu@>ZlgAR%TYks+TlN1o_{HeEWbkb>~#BATu}Bk2LD{is5m+^uvj<tyCHeW9=rZzP0S{r41AQvg&U<+@67'
        b'vhtR4a406OG}GOO5MO=M<SDPy^2d=Xh$ko|0rJ~qbWLBCp<7?EOpP_waw(_UlxcaoaLpW93xonZ7Mhmn5));RB>Kcc!Jc4BP>YaN'
        b's)~4#Hz#_zEDL>}YExn!MG|!NR0@er6Kp6H&hXo;Y5w(>R>%*@P(pgCt0+2wp6LPI@-%-cYh3#h7k|T#RO>}GB3p5i@ZN*vPeQwU'
        b')7z`)Wx4TX;ASpjJR_~9=s;N185e(%CIwQ~SC(|1%p^7O2<2FmX6Hl=S)QF2Dc&}LXDum)QpA~YF2tB?=9GC&>5fsHLnK{LYXNc7'
        b'N-15?QkJf`s#RYSRh+7fUv^IEnP((RTa|7KnJ`fH<rN`_XObY3RldBKmDUETgcK$5u>rr>n1&Mnh?a5dm6vDfF0asEJjf`O-5*Hp'
        b'q=h^xx(B!st1oe9fX`K4DYA&9^GHn|Qh=7LvV$fSv}!P(@oqs)yB+4sRACq%RTzd)&mwY&J$wa|H(=@VL2o#^xk9{#QnreB&%3vZ'
        b'_q;`)5NBww`Gh#%e(op5JN~Vo6gt8l`lLAD{`x1ydG`-rBhI<Ma*cRz{O&d4oO|7{IOpCwEY7*#H7w4#KRqnYxo^H!oO8e9T5-<('
        b'zH7xf_e0l;bMD8l73bV%T_?`DHvr{Rg*5*pxM)ohd`(hGq_A5)Qv6b!x6&$jG}rJxMFL1kSg4QznKoJLB36|;#1+2s4fSZd=zdLj'
        b'IG5;E!ANnI+{LIvPfd=V8k-`atA$_=DTjf#mMYm+#0!7H(4dr0=8tH3O3BNW(#g}b>#2>ZihPyX(!H@E2{M|<p^TgDO8-EDWISNI'
        b'5cG4^?{NilinxZKDVx=%?XhW7sdhVsZYV8{r?dz9xwQ6RKqsLoQ>LG&Ftw(7{1M8tDj6S-b*=?Zlf@?<ohTZ~^TS*hNeqzqn?!#!'
        b'N-6@?OSI}E#83JJE0}D{lr%dM%_$ZPTpzRQnJ+9*Y<lg&6RJqN+pJ|y6@^Wc3`HQPT7NhZ)s$+qVP?_E5v8|}e9Nhqvn|_MEk1Ww'
        b'drMHv<7$`Ezw|&>NRCfRU56^KK?<$ow}sVv$XYMcKW&AAXCWs~K6NPrLTI9>W4>770qxq(T{vs|XSFcGCU3~``odu2xAvn+DVjsb'
        b'ygbFa?^5k<u(nnW@r#Hu0=;V_sw`f)Sjb|H(E2bz&!@i7#t;>46K{3B@Lf$hs-}~pLcQ!IpRj!DOdn{hE0U^4g<rK2()%{0bt^HO'
        b'(4vpOfu$*(3y$(fxTLvE&s?5|U&z(KAmcm#tSB_$UVXAxY~eEhq_ij@>xYCW_wu!IMn_LYq?OwrQKViqbq<*{mt10&7MMR+`AnOc'
        b'(avBj=+`P;Oq-dW+M^RkA=G`Or%vrEUk->$lFBc*h?!Kb(A)cIF_RJzp$V9l4V7Il2~v=d5Hm#T>ZAxpnXBNJAcy$EIH!1?xa`>4'
        b';99+WnUMd*#lOh8fkaU9wQ{w(?V(;s^XG)sz*qi}=&9;}tH}{1Pt&uJl0!r*F08QVVMr3sBTGqEQc$aZzC58ErJ7m{Ont49L<-W*'
        b'F_6errSB(M`8rV~+!f)IyH?%V-D!30vWjX|!%;3Ru&Tli{uWxU{Iv(2J^=p$AubQf?x8;5c&DfJpEkHt5Bk)Y5^<?gsVbOIrNq}|'
        b'y+U79R`22&Q+ojy2d%ruOgasO;3#cz%-043Lj0&u8kN>GLaI@d$HQk|{Y7^nLDtQySbcn7zD|nPqX)D4Q6S7ENbq%n5H?t$6aSlf'
        b'Ad#4gjG}d<t7AwjR<>G)luicHwWiJO`b~$;+ti?axuS}ZO-Z{$E?G0pk&mLb71e6R^Ld3@IvnarW-P%Kz6MV%Mf7Sib@I6?GF2Fh'
        b'4Qqv}9a`(^={2D`t36K@7hJCDsMw;uJ>a!M+gSOnQS>fNh=1D4hm>r5E>@q!LnixBOIW7%$C4>=*U8P%%sq|}hnx~s$Ug$Irp&pD'
        b'ry*aBbVX7N$=(pZTHKGJEB7C6smds=Y;@zij}(%~-Gx?%BuqC!A6OzGvE9&jd5XLz9^%R=#0y_dPZi}+-O|y*gJ%VK<02^JkmK7N'
        b'B}&pL`AZC4)&``sCO)1+De3t9*^<oU=|8QXyiV+Ctk;V@%`Ml9J<WHn7kip_t`~cn72Cv~CcaJVX}+~h>}lrRAoes@+#vQe|K|p='
        b'r#X6q*wZY&QS52DZxnl)y*G+I%`a~hdzuSBCH6FppAvhT_D_jDjsH_(Pjkno#GdA-pAvU>r*9W`cUNu~cXzMfF7EE`-7fC#nr;$z'
        b'cjw<E?(TYS5_fmE-6ZbrK5~<|yZhcv;_mK>o5kJTbvKK<y8}0iySoqHEbi_;f3vu|d(o%G-QDn~#ogWEPm8;|`#&x2?v8(2+}*9('
        b'A@1(Fc8I&XSL_gXcSm-JySonoNw4|qz-oH0yF=XNt-M9t<)u9y-Q{h*Mcm~L-XiYue(@G@m-qQw#9iL$w~D*Gi*FToc^$wuI`0B('
        b'Cw=t54mtx3^wQl-;Jd)@0xzTY+rYKJKi*3Elu>WDnJq#|dyQ1qz6{v!|7bK$7>W>bO@lr$3;X!TF<%eKRR)jWlxIFwMj7+@H*$F*'
        b'@DkEwu#<(0PV;f0VLq;v%7-96A#hmFi3bOnRE#LbEb~!M_DLxsJ}Ds87x(dJsm6$g1HP-7Pj+`-Jk~Gss&aY~3CRh4^r}=wC5t~2'
        b'e1VYo2Aswe&-{$Yq7hxhn^6<kXft1LI2sL*1D+thlneu3Z@SeV@W*KIbG~#XK{Jdp&8yHiBw&kxs|EN4Y!uKVU_ij20OUkIFnFzL'
        b'wiwNN$f5e^md+`w>Q3_UeBmI;aq;n2us-oAURY{W8--5rw+AXm%xA(I^Kt1As*|vA0U)9+`FDCBDc?rv<3Y4Rus<5#Li5os?Oa&P'
        b'E=_m4dzYrW{jyz}?)LxOrRi?(*`?`j|L87FcYA!7rn`OXE=_m)jk`46?YHmJbhqELOVi!{)m@tI_9u2}y4#=KrRi>eWtXPA{kOX`'
        b'-R<x0(sZ|<F{0^ipEsiEZm%5?^B(_hHKOTm-!P)-Ztok>bhjr*#5~APgN=x}kbc*Wi20CyyGF#E$j=>(h<TBI508ksk$w-1i20Fz'
        b'-xv{dB>lcSBIZf@{a{4QmHa!@E-_!y@1+qjXVUN05ixJ_bIBuO?xf#uM#TI{zc)w397?|vBVr!qXDUa;TuQ(1jfnY_eou{vIhE_G'
        b'9})8^{eCtg=2m_lbVSUr{Cw(&m}BX8d_>H%^!xLOm}}|x-iVlQ`T51$#hlB}`Q9$(U4HKHb}{$zdrr5D`Iq;@+r=Er?^WC`=3(C7'
        b'ZWnVg{RVCq^D+Idzg@^zpx@5hg^UII-F>@|vp~Nu-!5b=(C^=7JvA%&O@saESx?WZ|AxU{R#IJ3d%$2{S>h~t<8gz1bxB9bR@g5u'
        b'xxC~U+^;C<DR~<hC<&B22@IA*O18t_mXhl@-cs^^INnq8C614ke2e2)$@3gvDftD*-<SM_qj~n}vkA|hefDfO;+r#j&g=m2oZ0hc'
        b'4*}=To<I9hVEOFY*)7QDtFvF7T?_x?%wWtLr(d~kU`SEr$GAGg3WbY~smS1}FBw#BWrw2koyArK_)+}gdpeD0ObSDHm@P@*tw6H#'
        b'_oH`cXMn>WN<YuP;W>l-$s-2)@DcGHH7Ub9t_$O~OddwP=lvrY#$CnS)y!SP+{>7|mbsTR_X_5&WA1w9z64I>4EJhysD_Vfc&Ub;'
        b'YIv%KuWER!hQAv4tD$({uVxu@RxxKabJj2?%(cw9oH<u8XC13#l|k&+NP~{<=wC^l$vzjf0JIKN4yvsaX9X=19l&l-%P$NZOMtDw'
        b'KItBNUEVE!J^c)_6dKKZ!QO<AR?Sj9ayUc^cERiOhbwwmFcDi;<I^))xHqwMRZs7xrK^NCV@&kQyp>8-Mg*1chX^#^^pQ>HTXX0k'
        b'F}bI5S*YYncjc7)Ybj^==R5Fh|GH>+fZ8Q+^F?BtYf7tzdgV{4R7!Kjw6tbPZCM%Vl+NXvmAKfaW)>VPjjQ~9sba30%yFSo&$Fp4'
        b'TBMW?gd)jUGVV*3<?=7(Y%Nr3GixG(rIC-`4<O$)%a`k1XwQ;zsjjW7tzWjHwod24pG11nLv<B8y5@xCmY+@ts?IrU1Pdo}<GI1&'
        b'L9~>p+D+okG?-;vIoZ~&N;DqB4l<#vq7Vxc4GRMed<)f}G)3d_ff(P6hUmm!h(s_eAFmo(I8?6C-%l(|OlRZrS5d(dF~y=RV=>;`'
        b'GE3lOwGhclX2KP<R!Uj(38!S)(wZ{L)#PF6+uFqnZ>)(bAw3h>$yAr67q*>bILArOc~I4;vT%UPCwv8h8wWNu@NaJ-M$`mV0r@DU'
        b'7Dc=A!$gae)@F~d!?(7xqrG)~8KtaeFnTQ$N>)$_CK*v8QIbX0pm+wb&=-kPit^2N5AEy+BBbP;mWPxNv=U<Df~cu~$6!y3s4FG-'
        b'IT6F8lGT!FC3W&og#37-mOg)<JD656nNf>Ri@HErF?R-2Y8mu7P?oNmJV(u;A)#7qFeqOW#3zUefBS}}Qv~x$QCl%Te<g&`Od~@!'
        b'h_kcP*WTf5_m<^MMU09mWe8Jv@6sIp|B3?j>Jv{)RHz9f$@Z^#m)+bYzdookvj-RU4OD=#JnFw%q~@~Hg#+kX3kS+3^`4sGrsh30'
        b'-A(LW&9&%-qKlJnO!BAp&PP=)-)ar=*T<@26){6n?N!xlL|uudkNz+=uD(!$UOtH#m2=9K(nK;o(34bBo|cqRHI(I^96B8tlY?Nq'
        b'|1>bf%lI@8gO37m3vU4R;V5j$U^uMV;{MHuDnjBmbzZVKBy2M+5Y09^_Y5mM&_Y7TNV9RR5}K8Ai>WV_dwNBJT`{+Bq_-K7o|GH^'
        b'z!#UHiJ^^rF`tTP6WCAF$!b1&)QEb+1BpJ>Les2j4#xeu7)7Y`2;nJJ1p1;WZbKD+?ffT|$cG-P`pKf5wwDLr{P0y*t@A(9X8D-e'
        b'tz5tVH;&uSIR3`xUwm=LSN%WS_e9{XBhUZn#-Z1ykIwzWH^14+mvYS>sV+dgZN{eYGX}9nK3Hb7?*I*fHh|`W9H1)D$x@^J4bWcD'
        b'zKf0af{TSY26|{Q!olta9$RFz9|X-^XtZwytpk;U^fDX{Efw~mr5c|u2{|f^_Wk7uTPfXvE%2j&UIza-s2k>5_<OrT_}N`<v`^(G'
        b'(?DXQFV?rk7fs?p7fkXOM5Rkm=lu0kFj+3Y!7N=xKFGC<xg5=v)GwkDI`><NC@N(%SP1JQ3<L*xr2JLV#IbVcGDe~3&^SrF^o62y'
        b'YS@?h08~n@^vMA}maY=6WjwJ+a5E)Ha(C*{MxeVvEth~AL>&|w*D#}jjn)**U`8V<w9tgj5ez2t0;U+u3k=L)T3|Gq7vwX;H1oB2'
        b'1+2KxWMD>mnKI36G+GI+Bk+bITe>`U=1ibZClaAv#Un+mY8*#!Fw_%d)iuj%m#@(An;cE5n~WyY3LhzRn@2OZxEu_%MiWyk;O*>k'
        b'vdWA$z?j=Y?cfgxH6)43M7*amN%hkc=<)e``q4CWA_7ZeU;n_6Z&PS6NHw0|?<8pw_PAZX=2n}h#n)tOYH`-MTh@Dg%{EtSR$~5G'
        b'%r_9Dt4o#GH=(8dm^Nq=gw+coYVT@oWvas_G{5`~<|B=(Ja?==nh5#A!3eDrm(^q?K=-Y}QGbA5%!vmQFOH6li96AU6#FqD>muUT'
        b'ja!mIUu2-4c(p7ukWZe$@X0T69FZl_IaB$cVwOUI-ZZB^Kh?8nsw$T5QnP#o=GaIG^Io<CZ68=Diovmo@=%)E-{j1V_zYFKDHe(%'
        b'JpwsWSg${f>2m`AnAUpW-=MpDNGv=9u!Qg3<V!|<o5InJ7=GZ8koi!o537B*v(x2n@wIh0x>}vSHru+1;uj%&J;^xjsih5b#sDAn'
        b'^yWLACshw*aHS;QKxi;ThvBdTs-ab)YDcS*8jcm2(-0PXm3$kYSXLQ|^n?cjLC&MM^>JS~T+zo=BcGIHd^)*dX5C$4jFSob0`={_'
        b'&8dC>V;r3)+ArQC&~r2_IaukI4hG~pW6@>KCWq70gi+@6wAebGj<Q9Iayz$ov`Zglr%D|iCGMl|bkwqm!9Xh4F!Sti4{A-P7_^~c'
        b'p@eTR*n_GFCVG70GaREcnS#+9MemFb#Cycv6+PPNar-*foGM5BkJ=LPWDkExQ|3_VQTnQm5$X%}4xpd*#0Ib+M9f3<rfhXEiOp@$'
        b'<tWWv>QJnQ4?1b42`ARGFu>@<h&DBXhwXLZDki;&H3H>>y7^ENy_>Ww(9BfI*Lt1aCf_=*t<~4u>HM&-wyG^>;^I4wC|n}ilPVx0'
        b'<wHKfSV^E{F?pqQ)P)Iu_kY~bEykO%JJUXhMNC@lQdghfoI3lA`5?qKxWOYo3mFXu=TDYFRl`van=D!`vOgvc6ewcc&704}1SzL4'
        b'+1LS^TH-;qK*v90w3lB~XYGny6^U++uxSST9JFND&biY0!9*1MPv+q_M)|2k*0R}7>gI)VKDO4M?CBHcYTfa7J-<rNw|6>iYq*B('
        b'xU{sZHlDgGLdG`!2}TJF^vA@j0OsN^9K_KI?RI3^L0$1}x?CI;<)5kX6s2djxG_chlu&}=Dg~9DHeHP~M$27P-`^Uo<L{V7$KN+='
        b'YiTPX6l>}};Kx%Z0s<mAw3AR(xLNa0ima$Rp}yMMx)gL%G>kYUnlmbYkE*tvtK^dTK_2K?C^hT$4~Tfm7|jz3(?$oicmorc66C2H'
        b'QV{LwROFhm0r_yco2nK38hEq{tTpM@W$D)1l-1p&@E>z~q`_9D8md)8jcQn?8fsO;a@DXxHPoqwdev}AD#9w&P^}tjRKqgWP^%h5'
        b')XZb+6b9$IrY2jL$4Q3EYz{{!YqdL9bEj5kyF(b7I=b4u3VkEH^<lH+4$vs*0nj6$$3cfcPk~+py$X5*^n1`>KzaMjmLkw>&;_8y'
        b'peoQMAUkLc$P2m><V;Np)HVYVvCQHpSNH@X=L%S*ixNnmOqe4&KrgX0hUWDu>=lAxol{d3TS@9ibkI4)<!Z&~ovE@pkW8r!MwXh~'
        b'T~(91R<kDF!R6yKplqbeja=QGB0l%>E=VdXc=rtkm@7<5a>A~Ncr8HbV~apvq?wM_9K<x|<eE%cF;M9=e^6TKvvqYUQ(Vn=kDuof'
        b'Q=x+|TI^dc55}YDmHYq|NoyFy5ZZ*)Q<2%ip-mAwxFAw>J8T$H840>w%?>O(1y^`;HRtxHamk;z)lTQ@Q)Ue6P)kT8#Y>jTk%(6E'
        b')Kk1#%xXkw42rEUl+>l4ij7#hc%*B}-W02HkjjBrwSXD{%LLR4ST10NfI5fJ1@Lq9)#IS)Uol(G1FZnHf<6k`4*ELiFz5*ASD<%5'
        b'g^!pm#h?YCa!?)U;Rgj>3iB19kAbcS-3huM^qBPXq|PtVE3p3-l=oF(KMT0<tD5_Am@S|t(50XcgVuq3pkB~v(@&dj$Gl6&NP-Ql'
        b'f#xv&wrpL40H$oUEN$xO?Cf%ToepVh_qy7<=sG&q4}5XVN)`IFvaH6JRLYbXExvo{5wdiZzdCExL2Jl(GMW&JBD(IK@N+YL52H_Q'
        b'bT;Tzt5>m5rxg{QMBzt8`{?^<FhP$BtV6`=BS4=YG$vh+Z|!JWLu)oJN2YWFH@?CvrD)Zc@U$~4V|tDSHPzhAn3@uN2xrVsv_Z)9'
        b'TU}MfmMmG~?Ck951S&Q<z>7zodgX>+62uA=52)06clB^SeU1^uq_<^3de@a=_<Q(KJQm}tVVAgB7)oIM<QJ8h@oSOfru#jHbP{_!'
        b'1NJpWR>1N^3nNcHOmciJSBlnecCGf&GS6%CtnsaNczs@1o3o?K>+_T=d?Q(w9u80CQc{iRtD4B6x{T4+(NlC4`Xl$<v`-xJHrd6k'
        b'C2tT5H+2IO8{!4e;WB88#lrFcBQ_0mt19kAUc~Y*)7gcL>0Bv)+6F-`mj(Lh&4zp*klHEny;Z5x>+yNkd#HjsQD2>_o!%;+)3Ms='
        b'bG3UreV&f4&L*dFvBGyW<$UqX9hzHht9`CcTbr^~;U|*H>5Y*$)N_?95pUtoF)YLu(c+zNPO)Px=Y`CA&6cAId8i)Re+*KO@dQy4'
        b'UKyyn4-W(ff*#sY@mmz&P1q(MBd@$6vH~q#H89jBZmK2L`a?p}hBAT2R-q(Fy0QU*f~%}jN|i1<`nz{aEXZe<D$&9y0r$sWdz21F'
        b'F#wm8p@YpUMTppda8$3mrTal7^f6c&7;<6j<59oUfjvR+m8S|mPYph##zw2*Xm6>)<Dq=BT<KwQBDTK3l$IhZ3O-#C`xeqwU8xUU'
        b'#-qzh0{tjEAblFn;>uzUQjFfHsK?xel&wPTq%Un&qjYJtH-zQXmXuCUUY=4V&3BEGD}Gr4h`m}D84W><Mh`8Xu-%MP(+9;4JS*NR'
        b'E#4s-D+zCudY{%jsnlXUEwqKr=oe@XEk6}Qo?yQ})`!`>VyJBZyMdNynBF9<{3`>gMQIYp63He;aw%nuduF++o4*qj4VIDpQ#ILy'
        b'xyc$2)SqNHwdSdR$V;JR6QraIGsO-v<cjnK=__}nC)lCx<R)lJwUf$B{5|^TAouLx0<o9~DR162$D{q&_c3*flGWz*UzOoe+E!<U'
        b';X18CJ)U4BpgP3jgYD5|sCP^DteO=@awtLGQb=wfo=8tHw}XhIiC<;O#S@cdx=W{ctxAv3i6?k^+9lK{Eo!(&#6()8#r7hpH6AVh'
        b'>ea!`_)4USu1H@-TW|!&Q?xY3M}TNf>8B^<hd;E1FWvJS{c=dW+*`GhAK{TUi#S-KI<8z<iUn3(v-l}xIVNJ{fltHY-JwOPL609&'
        b'pYdWGUcue2%o-g`3<v6LTmyG7Kw(<xdNJ?!LQ8o^uZ!OZTbZNxff}>>I8Ad66U|~M0;QtPdjZ|6%Gi*TZc<PNVD5@+6xTYaEm6gI'
        b'karC5w$)}p{_trJZpM}<8YjK(79?7;TuUa`3_EXvVfnrS@ZQiK9OBcR%qnG(wg^0jP5cZH?_#`&L+bR{WWOTw_3o9at|(@+V4@`$'
        b'4#>dsP8k?eL?jR#k`D!oQmt{sFy%a6Je8A5FwE_tV1VzPuTU~WUP+n%WK~xy?<|X`uke6cQ&I1r3dig{n3@N&rq+o^Bdsj8?{u*^'
        b'SBmRXcS5Q+zC=y<dNi-t7tsxAhKVCN5RZsfT3Ss{!}uVTRqYg=ery`pplDq_ONg@Rr@Db~mNTCs(;~v&I3%Wd8>yg_(hEezX8RF*'
        b'K3OzJ<7)Ti%+4U4grT&x4lhy)W4qcBNpVRPC@GW1W<IAoqgwIs^ZqTNO?~jK=7W#1HaELJ$B*a1rC#Nr&YJ4`=@SR?-Q@04^Gv#M'
        b'F+Yl&cxZ!=8Y$`Zga?9P@L7eLLp+)IKu%d&Jt<H8sl{tcH?g}zkq8EVl=?a23m>fH-Kg1Uz!l+h06!c!NzdY22%6}<{c*)J*rRq8'
        b'CgLJ1ZIbyCfpgHUCrl+a$eq;vmCGSxQ6EX-^C^{2+o@t^lKYSNpj*6&Q!m6fsoJ46C+AR%Zl0w=c=)A5Zl$(P$OJ_lr8aq*SXG0L'
        b'a@li;VNJ8=LY0g<%4I)QdWH<y(z(J<l)q^i@nnWKzt8xL@6(=_QHD&xwx*19Od0t#XXGU>!`*a>`Y~nHtvMq+O`!B~9Q*h{DDLm~'
        b'1@I>|^#=G>K6{k(1^qGp$JgWMrxi{S4VH3PFo@WcMar@=v3@Tl2c4Z_R9{T+k8Cs=@eGxBulc8}U|ilkO^|YP9>P!Wz2|3#2AjWc'
        b'C_7b1x+#`AG@U9IzxovI(J^F%Iu8Hzo8`f`k={jRv!!ScolAeZ1J#;%NkZobctz6Jo2&qWp`H$IaoXHIkL&W>=Lyo=O8tP$8KD3_'
        b'VjUUi_mMrJaaZcOo>rH~>vOibz3WRCsh^4HiW<3=@jwZmKOXmQNxfA{PmigAco2FY8H{5ZyCQUDh3FE<gq}$&|D46(uWQ7|0w10Z'
        b'XiMKfG89gTuf{SwcKp?9#H*C7#F#ikho<+bZa(qhAt7a%OBF?ilw5mjos|xirN-{?lZ|Xxj`d-<F}f#WkYm3d_8;i%m%#o*oxK6}'
        b'!#ewiV1G(yCl#wtHx}Qa&Lu0Y#dkd2c)U-H*Wx=?!u=VZe(HDhjBZlQrrvM!cx_E<Djl7+Hs+|L_hlsil%Tz%-REet`M6W3w}}A1'
        b'KmEXLF%>g5y+DidIPu(!%_z_&j1xZ)XZVWdpf0Q;KktH<SCBCW{t*63G}-d}+}ICA8b+Ppv&bLHq38EyzPifn2a(|BaA;#CSNkpB'
        b'ji(Lzu80&P$K?odXA-9{Keg3M>h}D!EbZevi;M-QJi$cV)V5bFYkWy;vJ>*nrmvsBpqQ%fxVlS~;b_(r<>A+9<Y3|3KhE$)qLHiV'
        b'>y-W-w{MeJG%)>p?i5pm69-WvgDKU_>~Mq0-uD%w{RprWm;_ltyFu$fN5TJfgC<k_ZJ3`0zu)cO6r>eI1$~JwEvvvp><NBM?CwfQ'
        b'f+^XeS#Ma8wm2ikPnnP{hKR6g!QXgAPb|g@AB@MbA%bf|1Etd@oEsYGgL|oD%X4l^%2QucG*cN%h7%K>Es|$4RHUl$hkf!E6K&yh'
        b'@qLmh1cV3pLtvx$W?<UMx(h%>pkh!7XbxyDNC7PXm4eDaRiIi>J;(yGf*hb0P%Fp{@`BcZGQUNH!Ha>Cpdrv!&@gBlXgg>JXeVel'
        b'Xb<Ra&?x9W&|c6(pnaf6LHj`mKnFpGKrX2xknXL0nC`3N*D28>(JPUDllj@Ujq+Z=^`kOzNwh$ySjEgREDz%9)-CE?)9q6XXVitG'
        b'ICe}ioJkjs;@COGa0R+>Tz|(D!xihoQQCW^7*5fJqjlNcQw(R-g`@d(bc*4Ib>V1TeBTtqkyQ;x9`;T(oKXu$_o^S7YB-Y?j*boQ'
        b'n`*cMEgap~esrqginVa`{NF#-aEca=>(88OII9+p?u;LtYPex79NjNJG}UmhtKq1xJ~`!Z##A`+dw9y>OsQ}*&pbQja0RJwbRYi6'
        b'l*1LL!qKwhr74F~QsHLn_C-dW-W>fo)&kj&r_26TB-{OT*&fBRp3ao{FOl(%{{w%Nw;Gv0y1QOie@WdX4IipE<v2f(h=t@cI(3?y'
        b'A3P@^fzi13?O1h8JCL5@`uefr$zbt|Cq6D2D8q%HYNLBJ8GQcC&1Q@HH`!h@SXh)~a3aAWTIq{Zn9-P6a80;U&}u^5<5f2msSoq~'
        b'P=YU%@Fo0_pig*G4>FaO=@aUS4bVbxX*G)``>^9l9m}mw9ipWrMXAn}zFDgopeV!*&fbAYPr0J5Nfn)c`I$iX8ke8#ASdk<aC(;5'
        b'ywb@&8uB-RO)XA3lunlhy*}(AI=xN@EvZG6^Y~E@EuZ3Kxi6$1u1bhn!A39=@TD@V3m~iOeT1OZu()TQ;GK*wA<_K3J&`1~bK-k3'
        b'eemE18R_N|KeE!%<ZEl|^0{sNK!Lc2QA$A*SJ2-`^vbdvFaESHAQGnp>7aGal<7SI|MD_lJx?jN09*>L+zt4{)KN+HHX?}84n!+i'
        b'KWFM0Y9a|1iqdwN4n4HdH4;~c&rx^E+(uJxVfx95Zi<AW?1BrG^Us^RaNhij7KDQ|aOk`ST{#X$CW(=syXUd`V<FmNWdx;j2^$9z'
        b'>efSyMG-)Z?qH-Rz9p8-cG21848ix^*ztt;sS(nzz+VJSoH^Y<N$?>;=S--bVxelyL2RM6gy=&^A{meL^v6oE4?ztl`^xF~_tI5l'
        b'q!$6bp`mOJU4tphofUW`LXt_$Zwb=#!J}oB81j{Y;9#XZSuW+aJSXl=jXtN{A?sdgvhRRB`P|g*mFa)`WteAy$1=hfKX0^`f~+9#'
        b'^XYEk=d;r~iSXJ1(A2n876$0ZCQW1u1M{Y{Hpg=2X|Yw)AEKI?S`N!s5G<?bw&m3|%>OeXOUH_5?BzcbGIpw9_WVr9-cj(}ZT*>$'
        b'$uk$`rk@E}JtZ(V{!Ga5DYmk-R~vuL@Bi!Yf9ubn{qhWkX?bRY!Duw*<(W+8JX4;@%oO!kN<Ss*x4k(1XG;Af!^VGx96#Z1=RaeP'
        b'AGs>*f5-1asT2KjsdxGg(g#ZGQj(WOYdtI$t3d4r;dibKb3q19#CyN~&wn5OJDtvUuOi+SD~W*~A;OYXaxFs%e%Fo!RwqdO*3$OX'
        b'l@;7U9z0ztFXSu@hI_^P8}ZUjefJjH*i$KV6cHq&bZU-d%l*Y@fBDZw`_Dm^w~h8s!2WU20#FOce9~zD82HCd80}A;5O$S_KM|2%'
        b'z5OpIviWP@o;(gBHJv``KQsMYaZp-ob!qC;*ZU{)?VulklJ6MpUjqFKG#xYy|BFuu^hhG}Gw&Mh+b_uD^oq_*bf?b#8qCMu6ZThu'
        b'zmw+qEYDs#1=7cxNej&a55V8O24Pnz({G<HuF~Rkx2+{I-?KH|TXQB)J2U++XQbaRdH*8Qy-DI=QJ#Gn(%(HxbEEV(qMq*4rT?Bx'
        b'pZHZ7zsxDq)!xiPkzUqrYiALEgjI<v$JjpkH}(XAy*h@?-sEsLGw<bWb(@zhtggCZ>BUt`FR?AX+`shdD;GvMOS83+?1@N)?k}t4'
        b'(4hOvezh#mKBqd*em-aj^mW+32I>ZF1KF0NF2GlSh0BFqCE`y+g&FQEmS^*Cubw;(A~l`+r2owHbHzbv-L6YhpT6EdnV$jW*W}sv'
        b'fqns6gfce+57g$_duj#VCW*|i*5%np*9rQK&P?=x&i)6O->etr-vP&^xuzk{UOxrW$D2u)Gzxqg{vP>|u&b2mcSskP_0n{=k#>P!'
        b'>Ckwmc_vRgGyQL7r2h%YJ1En=Q{tza^XzMo{zGk=8>JsdJsr@cf0j(2_@^8@5xR<<+``)Z?SI!NOn}URWRxy~+y6TsWjvvNto`XC'
        b'EPv-iauh$I>Xg3er8^#Z{%*^%FYbNeqCdGVS^32`9q*oTf6YJNvE!M7Z(OmkDf&>LH2=xzZ1`y1mhak{&W@NLdu;#h&2PQa_{+SG'
        b'`nH<$tKMnZeBI@iZzryKrDOJh{K6(>%Po*^qt*+w-X?JScLjd*ZH~j+Dr|h+e`XKIZ9l$)WALe`2o>KbU*Eqm*iuJ$@9uN^f!5dW'
        b'uDTbv^MXSMUIf-Idh4p9CN-aI^rait)($qYC)+pmf9Js_wsKeZv2{OhvhH|n==_IgJKVo}?Zso~u5paK(3bzq@nOfGF8%rUjY}VM'
        b'Jo?W++0r!hE62?@<k|OMhkgc{bA6tDJ?v{i4733B^BeQ*ZQvgSK5(P3t3>>X=z$FP7jMkwFS~y7IEd7A9MXSg`nlquw3g}8)Tgia'
        b'Pv$7-3n2HlJo}BH?}2^+`v&;WyHQ}JBr@N1Q=UEcc|i~9%tS$*{VOo<zgd{S3jDq_zw>F#UsE7`yc5xlJM!$FTc+lh==;0V?cO^D'
        b'w)~UE`|UqZJw8hRBN^#8NZ!y6VZTh`xx4c0&m;YzJ(?S(zXbK<(WSpZ)*<mvHD}Q)ag+LPTz=@ErW#Tl^*oMI^K8yHtA-5E1=?He'
        b'jQyN(hG~X5-!LO(m@y*{h8g^qGKinK0Gt`qU@BCdrV~f?EPi<^qd-6^t%6hhrs2PlL;kdaY32fLvnf583iw8mjCo|^9AVJAV<QT8'
        b'G8Di}?7V{i7k<<EIf^{Ao0;XaX=sZ=Hl592MeH<oIy-~EqyNKGSV#R3YfR8E=sU1~8`KBd0dhT)XMYU*QsB&Igk2@#Ped~_+*du5'
        b'&A;o1lgB}%rt^^WpP7EHI4G^VbZP3-*ZU{)k3pv&#vB9sEvN!zZU-KEI?sO9(*p01MCSi`4r_t`5_D2$CVEU~H$0zbFZhu#=K;@>'
        b'X4jECd&d+=AMZr;BK&>+g{k=^n)ONs@8<${zozk4{9@|yQTqRqk^aq+_oOVt7bJ#$l4rjF=^r|(xl#I8qs~63OaCERhr~bCyyfoj'
        b'xJXWW(<$Cv{7-kk`>j0t8^6yJ?>b*LTa-q#<%M%kP3d35Xr8utnq00)QaY7;`fI_LpLtG*gg!VM>$hRh!A5q*7|3O1Km0#dn61on'
        b'0_L-9>^GG*@NKMmqm6k!ZetBM+u+B>Hhdm#58K!$55RrQ#ztR&pVw^ciQmHC2^;$Z%H1&C&aN-EBOW^|Ip5AUTx4hWm)Q}govm15'
        b'XP>m#+4t>s#BaZs^fQp0X;6f8Cy<O^`R$S9X`dwh03ed{{~YKok~2<n%BdJ6N1J5yfIb7dlTM(?_Ss3bL$b2vSrK~4^C0NoNlr4!'
        b'sV4mlq@$Hqu`+Fvc}<N*2g{zPqiOQ{Db+B^=l+%ahD!Muk?+9Xlkc|vOWMC8^Zi8-$;5tx^cTqQnQzH>9+zd@M)JO?zmVKw5Xl&S'
        b'6yyVaQs$pza_<7YD9uz)9%+74hTSH^d>ZskS)Zly{U5zgdt1K$8<*v$MZg~U-S>C&ZB>5z{j_{vNZ(=mWmv)$GC$AAw)ml}2dX>L'
        b'&(KV|FG%+v=(92}R97V5d_acz2I%{;o?Zw29`tc}SaF&x&!0gz)B8VJzZ3_ZT{<D-{EE!eEubsqTIDkNy}L^0<D`uDD%sx0Wxfx{'
        b'&*}dp>urT>w+BG~A?uj>!$(N=JLo(ae^B<T8)P2nyZ9)b^^>3CZ;|!-k{o2zcM`J9)w2KO%l=Gx{eg7f3mT*EDJ1`0=9&8Q4w-jx'
        b'F7r65<)?Mn5-me3qwBaYX6y+>{p@_k4xuW(hip2|Hpx1qHhC>rIsclAueMCvP_k^%7p}E@^M}W;-aaiR?Yk@;kNeG=9(tv5&Qgc>'
        b'#JpcN-u0(zpP!NVowUD0&A5h|*ps|O6P!WcZr(IohCtwN^asQ_U*aDFZzpK`o0_fz`t3c>WIq7f-zdmE*JSSlRsr7z|L#WZyxu|Z'
        b'j?B&W`{em1y9HDXDvb?w3bA#){JH|anx)=EUZqrt+k+XtVgo&$@>Xb;0~cu{?wqB&4d`smQZ8s|)(x;)rECJ3TvEDTr9^(+E?1^j'
        b'<;WDj1d4*>4q?gWd;OvC1o5xT5q~os`7X^-9DYSwUT8vbtA?tU$&;o03W#*Gteh|hO#^Yte5!3)g)F{|R%`R8E_Jffv_Rsv=fw40'
        b'gZh>S@84Ir>QuO#m65YZycI6a%sbC?Y{-@HaPiC;M|~%#)SNAotBO&o_g8;v*L^<~$lh-vEY>40nN8YTRZkQ5kM|eN1hGu9j&0)G'
        b'e(s(;k>~d{8r47(Wpt=h)a|O&ZB?pJQT252_x*L@`iZ-+kjwQx`|uJWCZGn{m&R(A>edro-7Zz{11~94XM>5VESKL&YAScn5m_A)'
        b'mxev+{T6AboFU3iSNm#vSF_K%-Yu?==%ZjUQMMc+0WxmlPi6kkIi8fQ6HGX2bLGka`)i&ybm?|b^C&8fB4<N-F27;d74t^v7M--p'
        b'YkGQ*{B}BgtPUn=4ip1DKFDuu@~#+4CLHos4_(KDcVav6kZX_fZbEE12*^dprK^<WR|~FXR>vfX62ziw=bKZ3({ey^E$p%>wE&W<'
        b'OG?Mll2VzvQp@}Fsy-0XxRoR=&lOxfYvKwHzEI%G38kzC`srmp_eUpgLUB5j6^ipPT>k>*3hv6tt9IvsM=Xx2q`UCYdIyqWOv)r9'
        b'!7#mhd(g}bpD$pByFk0AF~cp>nDLeZW*jy$!%!aE7`}?@g`jlFY*C!eT^^^;-nu5|Z7MEnGbK5b+xTh0P?7{T)14`jI*XxL%1=Lv'
        b'bB%O|OPuOUT!BRR1t(>xGMNu?@lL5!CqM1R!$wk!#sw$|0j?x}Qz*sA%#b`(8Qhe^Ny>I(<uTT61vx<LKpQ|qpsk=ipu0i)K?guD'
        b'fnEl^4LS*$^D)*v7gP_jfYyOFfQCR^pcA80Y+URy8H7FpUz@WnWp%Y*W@~jhe74TjSv-%|=5=OsU6(s`v3Y&X9bN5?G>)gs?e3t%'
        b'iz%)Y#gr9UCm0>=p6pbbI-9b1mpMB<u8#IBew(c+JwvW`m#0OSdi!M_pWUWQg&5=$9=$Haae0R49K`}x%+M}Ro6XzQlIGIsv^jiS'
        b'x_)LX&i0P3)h#}c+t!qxyqfuTTU&027F#>rk55mgt>ZE$Z_kVjuW_#Tc{@6MtsU*F(;WC2%w{@qn=6g<7S_A8I@?!!TQZ8nWsvbG'
        b'J!vio(&d~e{Z8)$)!FV`t2Sv4*L7YGDzB+CS82)3;hfm5sd@EePPwzg6U*IuWerc>XQVVb-V{{o499k_v)$`+xSE?$<TN)@+OnD_'
        b'zuxWD_wTM&cY3!a2ES!WRc&{zPIE}LTnG9h7nP}Zb#%E~T}^0hU#rdTY)x}RO*k=ToQ@oB_D)-SQ;UzpsC6{^U|FqYr^9PY&mS?U'
        b'=q@S-mAM&ddefXe&Q@m=Rbq38n&UKg&Y^5(v>y-KW@~Ll3{BK+(p)+_T3hWl5|Wo4D&>~D)ANT76XJn|#n;sCO?M`a&*e!UN5ZAk'
        b'>2@MIhtJ*Fp|wX-hr^{G2--x@)s9dO-bw5v)=%pS4qF=rmV?hF`oJz?r`NM!3Gw!6le=)ptk<=!W><OyoTGN;Y_2?dp39-b?ap*?'
        b'HK*I#Ivg1(rPnxTp>won#DAG5BOcwfE~4>d7Rqh&c-D4wW^gkfHk`TEw#J!WS%Tfs)#?yUkzHKMq_Zg_B6o);gF}^=tBh1zx%d<{'
        b'GTxC<JnuS84<2;!j<x9yozB%RkGIp-nUQt3cqC<WJ=*gf*xs==z4aw8tNkTkzZ6J$O<OcbZu)T0B2AxLrGpC-U}w86D}ZyI%afG_'
        b'U6*pW#R8_Q)0xIYZRKL8)-ztOR$XmQ43xAg;GFdSp6-@aIVrA?G?~qxAQJgB$#&okts6_yfhxMAbA37+P14ooY|n_rxvt5H38T&1'
        b'mCn!X|D1`gCA)KGnjh|Rc4Z6=Jzw9*Y92Ak)6*=yp;gCDr0vY**1;cdzV@sbr9)Ty8Z>@;y4yMm(Sf#Vcj(3icj8^DS--GKmDJYh'
        b'&>nd?ozt0@b$Io2u1L8pv-w4h&;*^%cYD(9ozAAq@Tb+8G3v17@w%F`2BT!FT^E&WYxCst(9AmyrN2Ihv!kWS-6XnU=5sLJ6S^Lc'
        b'BWs?Y&|CVfuX)R!7xdwCJu!4%I$d~-(?GQ~wM?90KDka@oOX|HP+~I3<*BXJv0{=0+$;EUDbt5|yr#94V0C2ds8Za_aVH$~Yer92'
        b'{9Wy-<)*Ji|76K_ZfbG4Gn}#L@TQOG7OyvB(a1U2NTc64T%G#I8F$Hi#&PD_P8WtS)?v1EezOxhA72Z4g>C`HUDVEt$5gu~ZNk&1'
        b'q90?N@3gJ9x!QC4r6pu*hbN=ayse(>0YuCuTe}z?o{m;*lBhD%_Es7GnmTFS=EGBXjnkXuNnh_&$sJ7{t!VW&SL^yLzoOr$*~Z#D'
        b'y&+X^A|)(eF(PvIXr4K(?3ukO6_0bGz+Q|wQDd|P)}|!8)4}6*Vq&1>dFy&og^}g##S^sCz8VQo1nEhro;)5}fO}K5JDEQzk{Npo'
        b'TUV>sb1JWxZrtsu%AU~sy5&`upz(M~Jf}?Ghv$hX_~ZrZa!=+#42KCkxYx+6(3*adNN7LrX;D|9ljYg%Su>d*uS@Mn*|}cZ(b~+5'
        b'bc%M;`<p`LtKNA{V%Bywub(`9s*9=ko3vt5sbZ}+mC{b`A!j4fgyYHH$ZBjCua(u9RkSCv8`D_2f6kfU`OV!j9+VWnBRfg;rB7$Z'
        b'Rx`~_te8C+j@k>g4`;X_>ll8Rn7i7WvYp(%7Ds0;w#V7-$l%k8wJAqANZ`80TI=I4GCDGfmts3Sz7}ll(x0Je&T3iEi6-~paIJRg'
        b'X4;&7+<3O9FYVf>n`dqZ1XHZN#f!eoU9{@QgH@$htQe-?CFhHi9R9knHFB+PcV<V{)$VFr-R2d0)CrTsF1Xb(p(~c_wv?lkhj8_{'
        b'IP374FPSX{17p|2ZUl}1^MGFfnt%s@X5e$ceBgforvcvq78vNfM!uyGI3GCOKxb0&Ei>p&9<azj=bG{@bTDT#&;Z;HGy?Af=FOxt'
        b'HTf3POuEyTZ!yoL^D_CCeBd-gzGd1>lK-D?DFA*5SP1L_P6tMSGl1KGMZnJjPXm4(cslS$z%ziq1s2aFy@~mjnZU)sGl5OOSwJ7K'
        b'1b8)YHgFH{Ea2CGX9HgX&H=s!JO?;459K+Nu?nC8*a$QN*8%f@gFq8-1ZW2S3;CbT*wf@6_$v7azDNFn7ntB5*Z?#Gy}*2649L!6'
        b'>~^35cn{DBd<2*WJWSz$Z%{bkpD7%0t{LGJ#%h5E;A)@|*iHN@<d68k?ZgLu7MKV88qfrM7H9?@1?B_)0GtLi=c65fX9Ej?rNHUH'
        b'OMo+gYk);SKkzh42Y5R07T_7cF96R3ej7Lo_#ChV_)FkypkW&79XJQL3|I}U1-1Z}13v-`0OP<Q@J3)S<sY~S_!VFu@cY0J@Mpk}'
        b'0^bB)1uQDaw}gT7fOi0w0rvn`1Mj5xfpi#ZGtdCM2}nvZ?+22swa0-b;E#Z2;IDxBBuAzY^#hy>EC4P876M(s=|Del25=Bq1l$Qc'
        b'4Y(J0I`AOy4B#t3x_kW&a3=7~>8LMY1#lL{2c&!2-N4zvYk+3~cLUF+_<(bO-vFKid>(i%@HHSQ)i?<>0B6lWxq!96JfH_ia^{AB'
        b'X5i<5`M~c1rvYCD766S!C>O8{I32heI0G0476ESt(m}9?fCk{Vfkxm9z&zk@fhJ(lX-EfnF)$x^DUc2hZUh>DNuUvUD=-iEd7ugS'
        b'IE4egK;eLI0;d6sPDlQL3Xl%3H3AJlFVG0w3d{rE12h4j0-Awu0`r0AoPl_N7GMGJGGH-q05}u48+a!0>%dvSp94#PMa5_b;D>-`'
        b'0sX+Ufj0x^03QUN13U~o7kC_a9&q-|e9K(mCBSM52dn|!1Y8E(53HqhfXjh}XXaa004soXzz$$NFb1RpqPu_w;9jziqTR?2d<kd-'
        b'zDfLjj1|lRA9x<n2&@C<0lh#IFak6KZvy56M}gCT`+)_(XMuFM?>{IW;9n>n;5j7-4{QLMfgb^~XYo7%8i0F%M&JQp9`IH251cj|'
        b'{(<Gdd|)SV8ZZWYU;1+XI;A{+2NgRLXxPc6VCU3oa^&3+an4f4Y@q_QceT+Hv<WNFj!w^H$`bh<JgMF=DO4u%@6Ks_UxLm}WV5;8'
        b'!yIa2ysN9YGM!fEWzJT;dYE#hs$9{O@Fe0w(@VLsC`k-eB{GjroDRqmQK-wi8j+Ntk`h;%5+KeM^7KWcS8+|AJ+XmOjnlKSTnS|>'
        b'@yS*bq{@nW=J(=U?Du2heo<4El-sLF8N|gYnZCoCge%6*n05vaH!W|Pka1_olk$FzQg*Q+E8IeP9(%Ps)7>J^P1AX7QucJIJoCGT'
        b'pTV7JFrA-w5#lt^-N(^4&6aU?j-e>8u*fhw|2*@eB1+_%)Xm88aYKsmo1<Qcy4u~!3|rBcwq9tmGg^jmH#$2UJJ)2VbHk?63o#HW'
        b'_opjGDcQvc1m7j{jIiT8lbz0`OK)r<e{{~ZCgrb+^U6t=(_E8X(S@H<{^rWKEL#5N$TRV2cf$A|;kIr9w~6vgXK~AQ`BL*s=X7_Z'
        b'_*PK|B(DwpMenm5#}VeDRDROSQF4LFelD@sr<ak+Q3W?T!*9AW-Hkf$PPmb5Gn4<+ZI@ObleFD`x4+cojSWWouWvQl!zcsoKd3Az'
        b'*||jG82u`e^;=R^Z)Mge8%wIj8WqsGFAMBL$0)j{&Z^3Yd()tu*B&2l{3?_8D5hn|@>YKVotrtstykxkpW)W0bDNgowoT{1D8ntH'
        b'yNj54Co!hu6=t}_b#Bu$+>$!C85wSSba9=Q;dZCaZAmT}>&D#jSF&WQ=kT{6!+!b%{>n1!XH4L)BEw#+`>X$D3RIdofxpbVPKzh-'
        b'=g6>^PT<e^|A>4XwQp>nmAlPz{l?|JqVbHrFrwp~rW*(2@@|SXt&X*RGp>_)uhp&AU&eK^9JM;t`pJ04IMvs-I;NYOJzlA0e2sH`'
        b'bwk6#A;&di?4>=+uYGJ}UB`*5U-KT?V5nF(Y+dmmM{jugPy-J@FCpnIme5gc$cXc=`aODxXZ837k~wbdPSwHRA<oh(MVyAeW1QVr'
        b'in(&b^0CI0+iZ+i2ea?9G5c1V970bRQhh_6tn@kz_8>gHyEqUwTj)&Z;mgbxx>FVKX!GyfwT3MDW>~_-D*NHHzrQjO?D<FyH}!`i'
        b'gpAn+l2N6fFO)qFrN<u+l(&#(fYwkl84fmkU<=0m@t!`??xcjVA`C?~G22qxP$<FHaVTFe;BvuqZHkaC<;{J;h(hbb@-@L=44a5('
        b'*pEa=z+I3es|BK@vN;xvu;y?y8YpigWh@>n$w_RWkgHg(S_4>}b1k>!?zL@<Yp5!34h92CUo;#jZ`#rWKm4p{xyRodOm5+km)p7A'
        b'b0NaIyn|mrLJ<<lXsq1np}+2UbR$>Ai-mH8E7L4*i;~b!e!5tiH~ZtH{kgm~)E`PFxJu4ADyUp&B3Gz-6>(;@+>0_IYjh-)yd~rQ'
        b'!C;u{+uf}6Qg%~;NuT5vB@yjSqDm>=^7cwwId6*u*F~cwQ*ouSV?4_>GV8D<Ma3|us4)RbLS)X5_E37Ho|N*IXg}R?LfuOpm2_&B'
        b'3ok791d~d?AB`MA+r&egNZ)7_n+xw|q|BA51QSZ4&yNio!UvU5BsP#N7bQdF1O9M%hb)^S>VnGCl?aOBrQ#@eqi%Svs6OK83W@U0'
        b'0WCv`o_HumwH!h9AftUE%d}tNg2)*!x2~dPMW9pH-(awt{sHs-(LkMb!6g`rG(<lp#$GM#bVsjvi#8T1FK2;TuM<3a{>`~fm}%`r'
        b'?|awnF<WSCAHPH3(L1#8r5`ca+5ZoI)0nt}Tp;g+`cEbI?|*n1_sRRLll_eU1Iu`}EaM!x=39RX|9Stz%Sh|^hfm?ZeC1eU<rL#S'
        b'hOs^?gLmi+gZ&uD^h<+1R%fygt1m5zbsfccYFV7>I)%p0A>^q>-o^fF<~B91V(g^Cck0$Gf5+d}Rb!2xyWed23g`*Y*!`O9f<n`o'
        b'24?)7(O_+;GFX|xV9YbnT=@{fsCi54TUMbvLUl{6*}4tgtk2MWs`X}OxKrVIlIBX%*S$fLk|5T)So2O456dYN{cl)re(?L?_rdRj'
        b'-v_@Bejofk_<ivE;P=7rf5k6*kD=`)RGj-towasOz10e81$Bdl&#Jd>XfWANK5MjZ+gWE#g6@03Xg>h^2GAVPk!Otdqu`Oh4N^B^'
        b'D|in*WweK%Hrn@t82P!i&iW>(;I=yJ98f8!6%+&Q0UZP#xsBehi(k>%BK?Ps8SVOf54VmrZvV(wWAT+^jYYn(#;yLb#vL2R8c%kQ'
        b'H6}r(kH|eKHtPSQ|KsPrN7M(QL84J&o<x&Gv&4Lf(<By1ER;B1;tYvJ5>JzOy2LXi7E7Ed@l1)cB$h~=E%7XgXG@$T@f?ZgN<2^E'
        b'T#4sPyg=fG5*3N_B+i$3k;DZO7fM_tak0cwiDeR(NW55Lxx}RsD<oD*tddwQu}0!DiM0}!OI#tbPGY^pOC&Z({E$S8#FY|PNu*A^'
        b'{hB)K2lT&}wxS>Of!>(Otm|JhTZq(mNS97B-%sXt<hMfpC(W&y?~_ixE59$iC(tCZKw^=^Vu>XZ=e(zWx5)i|D)U)GbHajMn0rR*'
        b'tn0?`oB)}AfM>`Zb=L0AvBtjp>a4p#d%=4Hyq%q5PXD#UzxLhnv!i$hfp&tdptnC)XZ<zE4fD&R+OtRhtEV|k&cg-w<o07d4LK@Y'
        b'$wqHm#SShmWXe6$nAL-F{Grae19TtgCD2Jw(H}8q=NHg1LRM<1w=Q_M&N_-`?ZNlZ&Y*SU@N*8H!wfu_`>IX$J?GY2EpXcb^AVU^'
        b'jd1@9<__TQbLx4XhG5<a3bT6aMCD(YP<s8La4^uIXo`iah87MnrF3DUjP=5;L7BfWF<%MOr@n=O>7+fZL0OoX9vq6rgNZ~a8sS#;'
        b'{z6Bmuc^h^w1&lk@lcdR2bNYV7K>7|qKq{*W}YVO^M@;?u7T8{PvX%D!%%-P?hA)2`WUIAW?X4};ldaa<Klgg>JV}nE1OR0jC<+u'
        b'pf47Uh8vVNuIgOrA4nvXjigd8v?&q{C>ysZ3kUEw8BA166oxB@R|9SgCN~Fz5ensx1oVM>2I6t#pX;)teDUwxN{>Ghi6)gk{~!`o'
        b'A_L*D!gcJ;pG3PnWuu~p3FU>!s4td`mvRd~)5^21@zOn%EByKimoCDEP|oLkh4P@5ITnwi9m2?hh#-{Ur!&<gv_Ofz=s-9?r6%|J'
        b'Y+erkTs@==D#8*&NsE9IPemd^QJv<BV5Jlwl@<%tzm^wL<2|3DpAB-4WZ?NxdPzwgRk)fU)%JYGV^X7>)F*HL9xj+`!VZ&+>f1aK'
        b'_VxQ?Qhi}E7^kxV7%<VevQ$X~d!pze;ox8}tZWP=$zv!Xlgg}xGF3X?soF%%kG?Wx4-lFKLy=9Bbra1~c2`NcDW~o<`mC=c(ODFf'
        b'bCrt~3BqTe5Hv`~7Raa%ugfutuQ~YoLlJ#H<gx%ahmw7Ysw9$p<?fLB%2E|a_WR>kp$z_nthThyqs02QB>2G;5eVI4v9433CqV(q'
        b'w4fpcwJNHLcdaD)>83tiiiv@qK7CF}(R)TTq3A#&GjZ~k(RWXg(TpT?l`(l5^QPG2Xu?hPxOk}F$7f(ZW>Cvq0<Uny6ul`Z)W!;i'
        b'e`6vV-<ak~SrTFS6fT>dOWxC^z}*r-IyvM^41|(g>nV4azDVDEGAR6^Gog=hv-A^+B!cmzo+D*DDJ@Q$y8$H&CqvXfV--CO3j<0Z'
        b'nB)g|6hD99Rn-q+gwvrC8acV=Ykd@qAf*^rb5X0u7wV6N)A{mnJa_PKjK-6tWy)rB8q#Yk^5JemRv6bJNe7~sg==~ZD5}cbRjh#d'
        b'6I9OBQ=2v5NzG)=NgN)Y$m#_K`c0w}v_Hs|p7uo(NuQ82h+?TxTr5?VlBhf_GJOzC5}V@wey)Bs%|YlW6>X5s$4r@w(otEK#JZ>8'
        b'&tk3Pz?x+r=s1YhI(?ujtZTNtQ)i{M&c3&?)`6MUI=g}U-mJ4G-_h1y>RN}d$*vr0EXG=koriE2)LS0~7R{@-4uRePiErfwcI-l|'
        b'r{-s`jb5IMHPiX^)^+5D#dQJvm0nbD{k4KL6yd)Fc80hgf?EqvK^kv>Hb%Gb<0?C39vm5YuwGnmee&W{=fSZ=<l*Hd>3Iksp3?Jj'
        b'=izRdhfM(%9Y{*0vhu*!yp^X=;H)W#<yvJo3DKQGLu?KQt|~Vz1;&OyBFb!<_m8Xhy%)(cOHrdHpUA_y1%KZ>3?aT93ns|J0+ELh'
        b'*23hzUFKomKPV4}U_LDK&_9GqC=Eq@{n0>BUXx16Iw9d!okDo?ggzYbG4*aj$@!vO-Emfz3kGDTn;=Y%E;O0XfIsQ?i8;x4bu`+~'
        b'*zs;r&&SKOdbTb^eSqAHw0hnT_ah5(*Yl3W7-Ngl>$wDDt_5LQO6#p}m!{Wq5!^N`7WJ%@B5!4wd;B6FbC>+%`n_d|XzyenV{gm!'
        b'z2$%3xn{ET!{s9V&7sJ~D2epl$-0xEVbC_vcF+#cPS9@99uOYQ9}9#AxisZT)oAn0AaSq*#ClQQN|SR@8V^sCq}pTn^M>xBY#`+e'
        b'|K=)w!KJ+Js(Q=Cm3F+}-@g?Wzfh>WURd>3Ay=T$l6QRAs{A5PsjsyztFk_qH@s|S)%+^u7qf~L_UGi&aQ)Ar7W}=jiiaO_vF8el'
        b'f8tVp>8g6iWgT|8ce=VqU9o*r%+44B7b?Fjj6GLa^-iJnQ-$t33cJ5p82g&Y&MALS@$_GDDZg=5z3Z}CU2eClyW16uxrT>bJ9oN9'
        b'M_v0S%ga*;T&Vn}a39itx6rz#(0xT=_f>_lj~5Pqx^U-Rg`*D^?t6TaygWb4-1oN}uKm%h8zO&8_#?Ca?Y_U|K;a9sZnz--ZwUY5'
        b'tQ+S1E#ZGW%Y63V68^baH=Jhro5DM1{38xWPw=zam~qs|-k9b5lbO}L|L`lWrFV<hu;UxC4m@t?-ufWW%DVZ76#Q|2ajdbvYOL`n'
        b'+`AVr`;Xc-7H=|`E!$cdeOp2d2gi5Rj5Q{!#~NG8nSF1c(az5YVj|tKY^-rXnYe>-_r<^h{vGO?qS~>>?LA|SH-UD8wt<R3!=SC8'
        b'0uWokj7i{|GwEs$zl#Dwyhn}Qt$kyS)&PH>$$1uTHX`nK$G6=|XS+=>pBTRz{`T~d+o)|PF!sP$qosw}50UPt8k7C_CZl~F^6L!&'
        b'4F>z0@KYTgYupcik3K-*@>$6jQ1-}J<CCC$pdE4KJ4)vz$A5=^<Mhlh9Y>tEBV7e+8o1Sd3ACJ_F}I!^LbxqsjR!!c>&F@ozs>A('
        b'b{p({p9CND<R_4h0U=S!mk`I3o0xqF{KMcsnlM`)0g+sbD%71d!0c~)++Z(3JS88iv-ZX6taD&4|5t;3+gA<t0L*=$t3V-8)mIGm'
        b'BM%$wyH<@gD$H!T`>wIZfB%Bn;`*Z5QUY2GLdxCZMkgCandsA1On&A3HYo4d_|sI@S3!T~H)!zxFyeWXpBbeuWp9r^3-cimoy{y#'
        b'ido6sXh(NmcTpqSALcorxghU(%(`d0(Z1qKW=k`u4D=A}CGh9Hl3BY!VUX2+2D6@v8hP}P=@;<R@Sxc;7qkI!w1ONU3&jUIbeqwh'
        b'1P<Lz{kG2f($S*smqE9|ehX*^XwO4ti!zN_>n}9f--Q2PkD!m{Gb`P@+>U;YCUg_gVPL8!6zY&;e!hjiB-S@lKPc+ny`|2&7jbPL'
        b'rm^wr_*OIH-xlT~pO4OA)>7a>VEH1Gz2qEbbx>Lto9ug+nCv@&Zt%A5G}<59Wwh_Pg}%#<zq<?ZEks{^gT7N>4t^44d=})jvF>%C'
        b'4WMpN0MrMX({1d2xRLT$)Qy@~762U}6X8N;y&Gi;BM;j^$E`)(CqcWB#wh4+(6-MS?T5=u_9XJO;7+6c9`N>m#%LeC)MPKc!)R~i'
        b'Wo6$Q=l8A0(Efa4JvcrJt8)Bv;}>Erc}?BHqt{GhTQ4!$pG6(e$MC90&6X=4Hd`8jO`uLtH|U9TF;BqXex$Pjaa;Zwa|y@_Y5}!^'
        b'hQRLw1z=u)y6Ec|Yuvf5&T9Qvv&AwB^BVMBnCH=$uFGeAZD`N!^evMn-FjxdiN0sTy!~M5R>a}{GWEl{gX7oav$@|lTfX$9*|HXR'
        b'68Y`{ehPHw_o<De><PH-{JhbA5NYraD<zEW0*?(p`Rxbb=fg1nC$Jkh57Y?S45|PfMwo|wXtw<Lu-S41_%i5Wn0L+1w>$yN2mKnf'
        b'>`?LJhwni-LC<0=(Kq?x&yO|!`T?VT_(AktwA)^^S2uWmP#@@S*vC=F4KJE4TYqe}lmmxa#~L>RH-irCtg~(h&H_CTqVGUS>en!@'
        b'fqxT-z6*7u{h7O{JBc_qoWrj;+WUaxpW`Zm_n9!KJORIVzGSvkzC?9mV9EP2Ps0DcvzXNa-geMspxp(`Is`Wh=8FxTV~r%^gyfy%'
        b'fk@8DR^+c`rOE!}4~%xxPt2B^L6x9qFJjh4;MJh52=4)QgJSog{{fGI4uj5E%-DtPjGcVaXm=p~BS?Sl&-hqeWkNZ;7(@GzcSU^1'
        b'Dz>1{*MnNn-mM@9s22U`W%S86K~-?81y#X+)%p3Bt3kaWhWR}F0OlR^%a*6jmhsy#%8QWhGS>Za73;p{IG_8jrB8TAQP#JRXDe#%'
        b';6cXz4D&mnzkp5>zl!G0V%Ex$9UsR0(E{^$<MDBJa2f-QA0s;$h{53C{<bnpA+zpBeb!@KbPp5nbj-NFA0NLEDgVd#_`z+&D`1C!'
        b'-#v?F<M+mseBK#9VVz}U(`N85nTqu&>n=ta=c3#Ss2k?-KaP*rBHokN!vBSDkCTGDR+^g-ep7F6FFQJoEr8!r@{fpiQoMg2AHN%O'
        b'i}zVW_mRVf?w#GN`?#BR?*s2`)b_N4<Kul;8w`UeXXBrvnQ{CY{2dO1_beu(BE(Y+D&gf}XI@S3m)<g4=DcgRd;@q0wBS!>iwE@W'
        b'lV;29e=%EbfcXocpMuW(v)OVf=r+)o;l3C62B`gQv*jAl_drGOm@Rj}tpoTNXc*=ffTtm@KA87?t<I`^qt3eSu{vw`QJB94^VdPZ'
        b'@Z)vXqx<WuN4{ETt%7;<TjD;38TmVcupY!w2iyeQ4q5{KqrhK*_bPBb@I7E7_@|#RTb6=c;C%?F0G|g=2Oa?K#~$-}&;g|JjmyUx'
        b'UxN9*Qj^`}#T<-zBZhfu*opl()+h?*t|8dHn8&XD8ph0ivn6jo_50)F#f!z==b;@&dn0(aeiQYHz8Z!(2|6F<$ARa4%WU~B&;WcL'
        b'X#Bd_Vgn6>euFS~0e=O00Orzfpguu|K^H!byn>E^KLDzq%d9=XgW&xH)NsIT>4Lo(XakM{9|x9$o`U&8;0DYgb3cnY3uUN4`eWZU'
        b'bGcz{Fn56t!2ZXX7$tu++V`RCFaI;Y-#2^=_!8(KJrnLW+7AE^f#x8t7Emon0UZa=1bh@Y3fd3)6ykji@jeKA9#r^kvt<YP^MT#q'
        b'CucCW8}@S82VlMo*arS`)YpCB?*r`xZ3A5b{$aS!0S=yqetaggz7D$)_G7TW_5}Lo>5TmzyfK(t=#bAr^bMGg!8{%2*MW0@qX@GM'
        b'_#*Htpa9ID06tU5*k@oan$FmM;N1xO6zb?G%ufS{V80OU{1)sD!1KR@a)9?2Jdc`Sw!{1{m<K9hei(Q?@CD#f@ZW*?Ea1*(>#XMi'
        b'cOboWNN+#t+KOjRH>efV0&)=HnYstW4xvAQmV;J-j=fQ5wZOd@X7j&c+yQrkx<J1N)x+(lz;A=D1YHNBH4;%3GxJv`3ibs<c<!Hk'
        b'%xw8O@F3{FVE!Ypx0i1>zH49yTN!v&pl;9x>ieL>7#}}{Jqg+Y8U=li?6a_@f%`YG1~`m$N;%d?0gRJZVBdDT(f$%>ce%;_U$kBT'
        b'KM!<12&)!a&K?}kJ5J}pPGUUe9l+ewN^7NqMcr0V3y6VQLF+(nkQan`;qCG9?@$EOK1U}$o*^S`l24A)1*F@)8GVmd#8PU&21c8Y'
        b'Dr5H?nt!o`F2Oio3|it9YvOwvUUDM>JZWf>Z+vfj{QKkbW+P_O@&5$9gKg1!{MOTO9;21F4`BnK5a_@k@O+<MZ{2`)y$1F-ku-*#'
        b';j1to2VI9bW_j0GqYd=PWteOJgy#;h1^n~Zjx~M+_z~D+!0o^~@aka>0Ly890?t`C*4P7@5BpufnZWM@Pg{@i2eSkCM^Fs(3(#KB'
        b'i=f?b`yS}*E5;gM2mS#x4r)0|oI$JtzZG<-gjp{G_JNwuuD5;^I0U*Hv=y`v<!Hg!>jq(d7#{|2&IXKoAOns8{}a@LxwIDcmMW8-'
        b'y^2M<Qg1yp7ij^HfJj)-0{A&R4{LG{Un`6+AGn&`b|v~R=sO@%Hu@0!9suRPg9rTyY$VYV^ZtE&{N;=A@cPa8_^&Yze~WqR79aB4'
        b'J=XXJ@N;;wy@Yr_cI)`K5xlt|hW*1atk+J03a~yo4$Q;mVgdNQpia;V8@qP#$;I{4u3dC;d%^H^iFpf89#q&(_VbUk6@FG^ESveA'
        b'i%!m)N6h^v=Ra?lZ~V}{drVvZYu_WqqmL`#?mao*W*WWMbo`%YZvE-#gT*_)MBF_mAF-Kse%5sKrkPv6zVn}ohwmir_LKM8OvAUC'
        b'wq8AAGd;U~=IEWp!#63{*-U43vf=BhVAwPBo`RD*OOrc?lf(08D%+Kv$^e@`b98$#nM((D8BY$+H|&J9R6!OQ^8b|+C+59#f?_{$'
        b'@0sg{uQiYEnR(sA-yXiXc;|LXbmZdVt<Ueg!*u*k#HZsuvU86KjH7qX1aE1<SxeaPk}4VJwZ~2rolE{oFC67LAL+Z0N>y<0eM~U!'
        b'EV%aQiR(%iA1z=qjO~>Zk32kXy-!*A$-*z2;ANc=e=acwcNH!*tA371Kd*nh@VbY`RZn}2RokmjD5`nmmrV<A<sr!bldAurLMkB~'
        b't9Su!GQR%lLeWOHgD3Wy&T7gpGOstRJ@>StRj-(zGCwkEURY7M9u;dk`pC>B7vs-29+~&G6GtDPsXTt~&mTQ;&toTE$$Mgy?fX~T'
        b'{fi5iPJh6(@SSN-O)onA%f?p>MOQ6cQdnx(QBySi{@09@cXkv#=iPC3*00!Wqj^<7Ql82yy5jZ4g_oF$7M%6OyG7H3I}7d|HC%ho'
        b'2~@~R)1T%Wie^>KKiG^_9_4Y~$O+qB)JE6MKl?gAgP~?V)$es1XZ>H!-UO_vD}5NhTNaY5CV&wE+nWo4fI1DqmSF2l5)r{=K0rmZ'
        b'?F@@Sw9~0tthVD!b3+RO=?sfgfw8~2iBbcV7O<nZ&=PE^wKyYovrcWP8bEg0LG*s-+ys}Ie$Vs!|DT8F=ALujbKdv7=RNOomWzJ5'
        b'%$SDqISQuqjyY1MkAywcrYn?1cZ{r<#HBHrgo=I_3B{$#oI5n_XZnU~$B?{?*~-^JGEgR`Oh3Y$1%nn0Yq!eHjJZS&aN&7gA?<I-'
        b'S6LHZzXQar;7x1FcvgVzk9QUoHe#mtk-}~}hA^)|n(5{%u`Uj=dav9osli-_k(Mc_oXwF`F5d?OLQ&bG^xrTq-66x_kXb!)VC54)'
        b'^vh)rlH{sKOHV&iYWwY-M~VUCX43Q0pJz6DFqC;R%lO274DRH844%@{kCfV0-g%^$^q)zFrvH}tl?Q>tlj-0S_Yt_0_YrtXPd`#>'
        b'd*aSR#U*OV42F^{NfhWq$Q?2aq|^;XG|UZa;1m14E23o&l4Sg&rKcV#Emqulq?nvPlZ0|_Kx}jFSXcs#3R^)nieK6Pdb4DU)Easy'
        b'yB3UeKCQ;=e!@)S8ZzI>P1TEii}I;gtb1q@Dfyf`S@ME~eO%c$byB^S7s@$^RBtvHx1W+%{H<<e>QXuQE!$)^6Gat-IbS0Ks*1g7'
        b'uBKRO<WTx}x1h3tW9^jk$0;CvK<;u8#D1Y2&J(^hnX-KfXcoTBI$<~0+<K)2n0lyJ{xwznuPKXKYx{0WltsfSy$R?xs8!t4dQ%x@'
        b'|KMYb7X@-H@j%5vkZq5EY>OS^+p;&yTvMEz7mDkMohFzsrhp`aeA6UX<kn-yr;3kHS;XgUjZ>m7<<H_<BjM3e|1Wg8V{Z8e?TT)Q'
        b'Du+2<AE>4{s1Ly0wi*+NsS+`z(PZzN2;D|#A`GOTMyJte2v9{ajF<*FNZb)f9Q^)K#Nnv~pD7u#@D)THwM|gj&*e^XxB+pEKsX#l'
        b'wBi2x+9{x%fYM=4Q#BZK5Y`oXc=)HO5*uQ<f?CA$&9sL3!;~mJ6iTAH#E#5M4|cyEK|<4&{A+RkR8;z7{43wTa-DFL<9}N`zo3Ww'
        b'Z|pb++P7e+!hw)tJBC|~sB40=V;C?Fu8%#uE`EN>wtET=bQshLEU&gL+mON%JByeaIiNE~Igh?q1$afgFa=b&<}l?7^diM|+oo*W'
        b'rt-WMaH>cV3yT&NWw*WxTaX}TVD!w;a#&V_5?+>8A;rI$vi)Yt5)YFl;YdI^Bvn%UEXdlTn(I}An-+TUw!-A=wM<gDnRM%G<+>>='
        b'rVw*3T&%{9mUJl-rbs_EM(Iiy<1J&bpQOL*0i7Jj#7|kp3N_+3Xl{L1ImIQP2Bi4qm3X<PIiRN&OBM_UmO+2vms6yF=#_p;vl);*'
        b'W)+pN{~-PIzPm;@w}YC`T>+&HC@EptY~c_XHzf+NQK{LBCCOK1#+EL<KAW6-A{b*gQ`#0M=|>WpxSWI~P>PZ>M2mbiLDWjc@97pZ'
        b'Xl%^lV`Tq<V0yj2c;Aqo)|hFT!dsvccqRHm=CZ4(gi6XK^rG2`I^U_#w{;{&zu-rD)6Z&2?;3$>zSps!2%jkje(1DfL`34i@;SFO'
        b'qT00irdFX*IX}vmsKHg)fOE8T%dz^*x1S(|>8rP-OHIk|6554+HK^tsrHL>zIF!Tm<w(TTBp3!Au1)h>hP8BXh^3_+u;IB|dC}gM'
        b'g?@R_WI$QT3w{M>(pMwGA30KyzS<<b#w`}M{F_67GpPTBlGRZzn=tn}2b?V7Ptevt*>0KSRrAAsM+ru?PV!p(zVlI%<z=-yc0KSt'
        b'm>(wp%U`))PyA3l<Ui_N`u~S7qGi&GL#@0QJmS<8bpZUv$F1BVGBiz+ewG-oR=~_SJn^GRDa|xYZuFHFpPgh*Odj;bz!Lx))d+KH'
        b'QqN{vc#%uKI?dF(sf9kJUqE?L(Sd^%BGT6w=Oyfg^V1=&b{JPldEYCy)2)-3Ba=4Aq*eUi2HAFaa>nK|hwe9A?nio+#JT4S^Y&z5'
        b'0bfv2W{;OX0D*6A0(e~fbb|J#V3MlMX8t@0$c58@$N$EpZU4{X&z*eO=I<>k`fGAL$Fn-1=)jWX{CnSDcLVO7e6-^3`xV_dB3_uR'
        b'f4`$72%*?)UhCks9+iV9Z^tUfIcCeG-8TOL{rt#O#lZ}nr)eGO&G(t~uN;|~^FV7GelrQCmytkMY6bg-V1Bz%9v-9IG<hjTuEtgw'
        b'zYnq#2(uY>S-qYLCs<mOJIX1OCZ+2VynzZ2*Rxa1I#`?_nL^m^fbbJ4Oc;)Y_@HD^N=(9rm?%MIV%#Jt+$N~O(?MJD5V%oNBV<;>'
        b'H`shEd`TlGb%Lk^;V@%4%%Fn>ZiGp`63gLsErD#bJ_*z)GaHr)zv7Tq<G!JmaSma0Fh@5=N}mar(!gdYlI}$;n$&`q!&A^$I@Yt5'
        b'F-$mw0_Fs^q2}8-$06Et(?ItKG%2MCn(V}$35Y%j7FySv3kcSsiK>voyvJZ(>_?m;y^jgx%SS!v#E63KWn_~U@G@~Hw}!V-5z@&p'
        b'TxU6y0sKoNhB98T3h7Ns+4|BN0+7g$0q~3eHDRacwM!5d7!r23xmwQBl&1_Hm;G#_O6~@rQ6X#I4ZI2(6|rTzsdDf_)T4k$GS-n@'
        b'TMYvnP#2mIs~ilfnVyM{cAl6>3iWLlAf#ZUcYIpkL`w1@7b(t9wuk-!G#sWPu~n<WR;U&6g6JowEt?cAAb?+Ftr5N>ekFf?efSqr'
        b'Yimz?io9S$`v!T^r+%B0fiq*j&`XE<Xjv3^KO~kAR0@zmjfiQMG<En0!&b!haf@-Cv9J{6X5pz@n!f3{7rkPWG50pKJ%-{5ORz8C'
        b'iS5EfJ&Rbv(UWC9+F&1^Gv)p*LZnfw`0n0YUgy<iaiNE9E7l>+YCP&tmqL24d^L%yH%F_Z<DyEw$lnYabkEPkeG^8NZ##jI#7b`i'
        b'b9^E$<<Jt+t2`wv7=*DgYH{?E>E?KGtQWE<-`qeIRZ*`L_%|>7LR#KB-5xKmh-r_J8$a<|6(=0#koqrrX_Zfsr+<1C?B8Os)tGGM'
        b';*B68fPE;PFcK9CUs2+39zv{V{t6MVcOxzXmMD5jSWIa7ui|w)U-K`DYrI}5m|wpLBJTN5#LcY`FGMOKz4i7|U_N<W^A4ttPquLJ'
        b'@wq_YkwzSZD1#iNBMm8jZNm2S1nq@dybyQHOnYI#D?vQ(c=3}HkH*Yt2xX_jP?vyErcYR~hCE4Ri5!@Ddx51S1u2oEB`K(C8)C7c'
        b'c?D3f(6smWm<dIcK@+yr36QGi`7&b*62TBcEkg&%PhwaLg(&Aw*fvf8KNwDMA1v8lWTB(ou0>@Az_Z9)Ejx4pn2F_hWjYeFYJ-LL'
        b'CZD#&PXGYZi%2fK^jN%d!V-i5qDxrRTvcjcjwk!wwbKD`uCOCpyP>Mn`Vik{gaLZU_iRfi07Xi`2U=g~?IsTD$RO|JhAG(m3$dMC'
        b'-u7z%I541P7>-|Y!~~cp(BXxlwPSvO)ofmp=RX@JU{1bQbrroz%<IkK(Eksx3;y@8lqMUfBh~LYHk?u{MWB`jjz|`_R-*9dcCl|h'
        b'kEMA}>?y@!YmumvSW65Nco3w7IY?C0??Os9kVm7UmS(QQax0L`94vMK$&AE=g^1-G^vRwX&pRpJ#Xb%y=Jp{wN5)BiOK4c3t_FvC'
        b'kR@_Ek-(L(?GYp}5B%otMRu{X_LMd$`^R^AV<Z-}70W$|XhIFb6QG2Fh~EN;f3=H!9lW=E2}u&}Ll%KX3X6XlS9>LEr<DiC$$2!r'
        b'#xftHLWmu-X5XGmw0s9Id-NtOwhKt_E;a|E%LQ#=!plgd5y`xYwS0mot>eWXja%r1otMU;IL#-3H>|hHchE93ANkRn2xZRr8YxZ7'
        b'Y#)!qxQo9Mw~H-<eOw4$iuOceu@3N(52@V=FeL9{VdsQvL8f(&4<>Bj5_bVsBz=up=86{y609;(VBVZlyFs2T4lDkj@m(K$>_!g7'
        b'XFdUX0c;RE(+4*dxr;z+`(Y=xBYTcxxqk-9LeO{%%k4}a-!)I7*ce>AA8_K4mck%EcF^)&HC#&%&j(vn)O?y{LnE=4KO!{yKT-8q'
        b'%S%WN?z+OY_<(Xd<nyn=%Ms9cZa%kj`S`BT)r!2wYz5=w!pd4Mmj4dz&Sm4aKa5*KW%Vqaa?GE`i~lrE#}RZELdPR?3QmVc0d6fO'
        b'T9zY9?YMguZSC$?eZmR(RgTJY9P`_8G7pmL2dLz`nL@M-am?;<(4tZ`Zckqh*q#gT7b`dL!{bdHy#AgtV7&OTahhJeGku);1);Z~'
        b'bl7tDfYIBQ(_u0)Aoc)9t`Keqb~<HzX9}b%OiZtYWGUx>nvgQ(TJZ9WqIuM%L_o6TD^BS(UY7teWi4-TiNbNlZyXF*(p)j=4+iXc'
        b'3=9~%L6!i<?EI|a2ry=^Kf>uyIA%q(Tv);>$HwZsU_-gPIOXsdP5**=f>7AoY)i*UY2_hKd(H(M0FfrI)Dnv%q>d~T?|B=`UBE@C'
        b'$1OqXJ$?cZSpW`%c3`o7obtw)je?Dl3nA5u$4Nnwv6Bu8RcJrq85}zYu#=fJzB72-&C4~C``lE1HRfI|5Wd5~F+Rz)R6yp};FV`N'
        b'VHtSc`NbINXAd=!A~r9_%w{K_zPVF6UNR3O^LCWWo*Cccvuqdpr#(Ka7tI6m5IdJEtlD{IY**--t(}<gBBwk%M(zj133VJo3xOAO'
        b'PI(fb{F9=&8O{|i4gv5V%)mQ2W$jpO0Y~~N@{yfYW0uf0=3HXmsdlTpXoJkWfy!<0tb5t15KD%I6^H7UFo(w!yND3))y1|kOW1O_'
        b'YOrlN^TSw)`mwWNfR9qDA*YtgZq>5t(qrE3UWiZx_;GG5&-+Q{##mm-XUt#5EPijV?E0t$^qkIG4sD1<ZRzZ)$(`nyyfM3aHCstQ'
        b'KgdoAL0kp0EWq-0O|*<aoy~kXrWVhvrM8U$kC<i;rx2kPD|Nv%E}0&(T^wt~n~#u8`55%LfQgYnO^nwFpyu_7czMj~Ysq+08>9oS'
        b'Mi`;|U`$ItO?nslcziMh_(_W;xziq>0_bOD<`_`XG`-|3G%JfG#|kVTyk3w)&L<`2svOpw-CCwSXVK*6m~~X)c@X-yzGicb!6nIF'
        b';AvOdxY!{#A5|lq^4+n-q%o2(8WCDWFO%3=DDE~pa9t~Z&l%#zXqL119tbT9Q0^OZ8{XET%o{6cRS+3KO5iBYLXeQ<O8|Dv9F_y@'
        b'OtSYq?K!h1EGOA=H=<~)5d)I7jcfKj0N+%poN^m%$Zixa7}T;HY-lRVPhk8CwG)A4KyJ62Hf7G3u352M9<gw&2Ga(G0B(@D)`)0n'
        b'EcwP9ZTjqpePeMxRy^VlV|fR#mi<Wlb;lB85VF!=YItnSo`D#HRlot#U60Gq1;x{G%~1!i+#sX`!!5YRT&1xa(Y*PX#fTr;VkDl@'
        b';!hzlK}cj!l&{#f74oX`I}X$h(rvN$&X3lTJ^*z@`dECkMkmu~Mhcfl=*BGT=F|sE6<;8>=f{jJ;!5Ro&GE;zG+7@cQJg_+DS)q)'
        b'zlE8H<C=AsqkKu7Ruf@}u8+1ymqc4gJo+*~(R}{+=iZ8GU;8J%?_gxyE7my;l9JD-5mH}UTYM_teqq{rP9gTK4-(mfXG51CML@3<'
        b'HwGf+K|UITWSPE84L^<AgI59_D%$=F66zddhRhhW&>j>X|D`c#an(6v#vC44ZVy^yVa?_ks_F(0CU;okjAhzY)m0W!eDqXcQFT+5'
        b'#g5^|pm1Q3_f3-l?Ag-VBW9omGQu4taY+EO<mjo#AY2K6BNqZsAE2tWQXb&bN9-939qGrm$Jqg_-2-cfu&a64MUTQRa@5D|0+96('
        b'vZATH9*hyWzqTAeE(VaK|Gqm#@0C^`D9KoCF=A#tA9DH-C$q#_T&h_j(;6`yoqSHH93RzrLyzAl+Pg)8*rrAU$^9QPXGS5@-sh}e'
        b'DjIqlavV2dvX(<!|Kj4B4}EAMo;;N0xM}nkuG})m&_BwsqYaxaTYTcK^6qmy4u-Ee`m!>A)YdWz_3Ucim6JwB(~9F0Ez{87r8Fbs'
        b'>4AGPWVX*owI94r254v*5FyvExQMHxS|0=?0f?d$O}jE`s2)vMAoThKQm_@5xXy4PQ<!T#n3q7E<>98Zmqtsz!Aj<f^Sm}Or$#N}'
        b'&SWuE6c%5i_=8dRhKyxB!K97y%Z=+rU6?QiF`eWT{;29C7ji+G9wM_H8m(vb?Ly$PGate3XKhYb2v=r`NPjmw(oT+U1>RXSlJ-BN'
        b')N_P>gFGRb0ueDv#-<yPv|o=p(DV>L(7?(J%DpL6;!9|(8uMR>^bZD_tnyTTo6Jqi$)ACFz35SxjXwkPG5aWtp=4AaDNBf?!2D8t'
        b'*>8ApG$~kJ_+$+R6kzBLEcXPbRFB$Bqcg_N_VOr+tNzX@UmDc{lNTJSu=GHEbPOmE$b@G{*GNGZgr9Jo8A~CGU|E{qXz~PFd4#jD'
        b'>O6@8Kmq^6mM{vy(%D(*G377-M@YcK*cw<j_G8!<Yu<{hpBI8A(t~B03hzpm%Pb(%1fz`-&_e70fU&It!MBUzgvYsg8MD&vjgb2x'
        b'2}?&?`ZzKc@Vey~_q;IoJ<l4^*hul_QM)>@%By(OsBP0|Nmigmt%Huz#?dObA8tq)b+4|d2~rwB1F>4Vl$;AU8;HeHjVfmuMqjW{'
        b'&z1syo%DGjaqTEn&H}hZda@)~xq37mLr%UOuKaey76UjY3ejRVBcQQT0Y|~U0$B`~WORfy67C2Rz|bgvHA-Vh;gIc@qb6Su5L~K2'
        b'Krb3Gl@GUAm<#O&qWs0E8siO5Zoj)f5sOE8lNJEii}LZ%^k<b}Fvo(y1>|0Fap-7?7t)*0d^lpGMy-28beQdNAfia+EFO{39T*{&'
        b'^Bmv6g2Cc|(RweW@P$UP&3`m^l(WqrbxAnz0`N1^(HhLXMi+bAz5ebqS|Ub{#lw{}q*y*`XN%foqZQSpn9P4Ae|EuX&}y?3x!TaY'
        b'8VRrhOC_d&aWrQqs|CPHCZ7jfASX#{R5Yex41-pA1Ugz!PaX>Wo0P<8P({t#;SwAvI%2qdVdK$fu*(-TMMX<48xi~G8xKB%**}N&'
        b'Bp`AjEga%VEOywv$JmH1!b(uh*816PeIw5Pk$U?|Ti=LjjpShcthU|}=Pi&Emka$}=GKU<djya<p@u`A<?I{@lh3SXR>3?+7P+8_'
        b'-^i}Yf=R2hedMR>BTdyZ=MN*E0;{{=-!Qk<lSPtz<wjD|SW2Bi+pA@#(Av|m>=fV5-nz>p(#X_E6sTs+QkWkNamM?7R*uE~5{dX?'
        b'M2Bnf`Ab*mzs~{r=d%pwM>N+^eXHzJD}??$OB%U!1C*t`#t)hj64t{xybhLZg6-(CNP?VeJ3ErPJ||%V%JLH&BFS2*5Tv(osd~7i'
        b'sVhrAhNMQy^ck>h8{8q>l?68>;<8AboSU{|q-b4^egm2sBTI;ZAn{pI^99<^IgJKZk8>m)LlR<Snk9VGaQ{yyHmn-)Y};n>>p<er'
        b';c*@0>7<&+52q5OkX9=~KA*L37@4m}N^M1@z)P2T_RVxzhC<MYYzCh1q9?t#<uiV-=`xEXBxEP0A(~-I-=2MOR^u!%Z&mFaTqJ?('
        b'n`GcyO=l@P`*+n{j`_m~5-vB>GS<8s#3Rh!5p%VSy}vHT>>i=&DZ3hRwTg=P`vz%<HVtvTF0#EeQvU(xVnoeKB;tjUw||E?@J7sa'
        b'R%8!C-j2b~`?p)<?T6&y)(hnglG<`PaG5Kt1^eqVMw(*e{1Pu#`=QK`I--x4)w(&Tz9;}KoDn(ji$d`75quGW7pLgF6E<%8OjLta'
        b'j&ZI%B3r@;4g8z8L>@X_uZYrq4GBtpm#W+=8ngh!%GD#lE^M}zdAGyOPU9zBCgG*Z7S#w%1)!c9Ukx=)n0U1{mS3v^ZGSS;UJYhy'
        b'oq4w{9a+R5ERY0BsZ%+?0ay$d!t*7ba%JQQm9D2KVrHL6gRtS03q0+YFBQmHYg6&Uks^oOT-|gz3}M1X2CL;HR@)8L-Fa~nt-16?'
        b')6r-8Pw_a!lzQfTMFchC-V{@Nn_dvL?gCEhpLm)q-iWAcuGPDc-?tW9Xe`f5Xw^E5a0NOE1OaZpywW6!nB!@}v{h8pgBQI+FtbLK'
        b'(vc#oxjkN<Bt}-zYOHW>B`!%~(WE#e;U*4xULj?Okpx<{${HqCrHN{A)1Db#m{LW`sbSD22zXTKqS_w3wvi~F9B$t)H<z24(P4+z'
        b'X)Dlt$zh1;o>vKr0QKi8mAak-Bd2;<#LHi6I&E|BznPvDMRX3kDO5c#vU;CYm-r$3y4iABNea>+E;@tOHbkhgxA$WXjCHPHSpoCo'
        b'FzBUgBcMw4dl88V`#8jkHHh2K$Yc4An|pBcTLb{71bHQYWo;{%FJTR6DBvFOE{STrDB^R76!3Ecz^UjG0HplZJdf0h)z)QO{g5+3'
        b'tykJU9d>>?Y-<^=w-2hOyvoEy<!Dh^#L044MYQdg)|BM3dvE^@S7YSw07^jKNuIp5BG{uXA|Rt+)_CXxT>&IQijG5|mQn7T)psp4'
        b'LiOO(Vgk%D)+`A1`$4q|ay(T8m?Rv8a;b_J?K}zz-f@(2tr7uys?lWY_1R#Or>18239kt*5{)<*5a#d0{I-j0g{VfPdTwUSR4YVj'
        b'2Z#6FsS&zjAF1uGSc5SouwJDR%nVnGdyHHLk*xsYtX%$|2zTtrzAKu+3M%LDJ^rQ0_NQUj`Wc*z8RjbgI823GX7+}dKfpW-`+t<L'
        b'4IfoYnLRwnZZ`-h*Yx0;Wki&>tnKAt=gY&kmxmYiz_91K7xM}PP24dYv17QMmQx$dRHWIiLLhxwL5M$A`K=cpOCXBudq#d!I6VkH'
        b'<8gy&I6MZt?IjEu?zcFi^(K=xe2oaVI>ew4gzMh~;4JX1GJUHJ&kh6iNyV5Q1k{_Vt3<4ekEu5flU_4BU2tx$AEsHty1dX25GJLy'
        b'=cY5U!OG(T)svomu(hBZ1=AMzyNQr^_mh;8{-%74l-gO$WyP47VO|3<%RRqF_)Ev3Oe|l={rsgTGh!M4f<uq$P?B3}fRa_}h6`xk'
        b'{eg_Ovs;*GUf_pe9AH~Gtjd5y#JEKR9zQa`SDSX&sTn4vY-<xh05U?7WVR=Uor^trd>gh4LyO3IR?Ixb6T&}jA;a#xNWMc7M$4D+'
        b'&q9AwKc{RTig;`|ks79!%OVyGD<2zPx<sQHZ9gmzSJfXu*fULfx{0DjnGjy;E})Exm!LAt6fR{%d}~T~YpT;;J7vR05mM;u+J+hK'
        b'43T~{@D!9K24VbpVM4_x)K^G<*Ab2p4!aNRh>zwk<$q_+pz#S_sXR#DKe*#5^&H$O$wF+SL+OBrH-|v;&=VwhPmn-?bH=8~fO%nl'
        b'f<=nC_aI%_%p{*$I!exIyD{W!AL^R}7ZsQhn9U47^c;du<&Q&E*eP%3pD+<|ZOCwK2>MjG-hHSCXFi7o2ImmzO+x!X$MEOC49GHg'
        b'1dc}eu}}Amy;iO~HMI1>*n2?1Gl{1ffCF&=H4^yNX-^S)zoq;6%rS^Iw*x59>o`IRlG{bIQ13R*+o|_5AZ_tT2kxarKE%D`h%>%9'
        b'ZO-L1*{3TAq#wu9=E53Yf<p*$6E~b5LI@dh(}&!V3;#)E!;lzh)sU&NAc9H2(tMGxaIXmT_z=?J^CJ4!g@|AcAy$HfSdM(?BaZMh'
        b'$S4HB$d-V*?+vk@`;GgiR1s2g7MzcEr%aV6cAdxQ!(G&AyVE|@_T6o&+QQThxy9QlGc}4YV&Iot20{xk!7*|zOa-`(ipc<2zf}yM'
        b'm&D2gL;GzyOzj=5q|<QMDe-=rstG(y{}e0#JXC}7MJSzyni|A4sOcl{sB9Gjfqxs~0&(jBepublQux&O;QF-$iIG0fWBPSDH3HQ>'
        b'u0~*bjZ6H)&@)ib@&$>n4Y_|`_5AMj{O<AmzT*C6b`K@)9^z#);ent64Y6}5ap%wFzc{o;@H5$2L!|0Ivw^sOoiHQrl~O!06*d?q'
        b'2t6<hn8Y1i4N<v+6LK6})Kq~a=K4Lbm8O^Yb#UnKY#QQ^S(2F991~jRt4to+2M-SbBj`s_F))z1f9}-Hl87gV3J(B%NH2HGDbQgG'
        b'Bd3fX0vJqo@nsfmwx{Snq<{zZmY7`De595P0B8%vAme@TQ2j$}T#m#JdScaQhRFHAuV9`Y3KNq&U&Vt4kBy1qhvO;ugu3oYKFL4b'
        b'=NXppvoK=lek@oR$7tNpTbQ2P&@PY9tZVYK%oT|y7a*>`^B&I<bjGIM;~<F)J@nwbhijT6r66y?LwTl)LYx1P>4tD7-72&xhJf8t'
        b'{Zr`nr(vu(RO~ZUV97fb&Ug<Md-Jc47t4oi-a{27q~F2Qvx;Ry6*PE+p293FVur3J=@)y~!w>0Du@qK{7E(n^NWa4G7-FbcFjPR3'
        b'exavOQfzj+rf$Es@MQ+|5Xd0#rDbLv*FvLO8Y?+J7>$*AS<a7?(++W!w`&rFkD>mG(8E&Y=xr)erd$f1l>OXY(+G$tsF}9Y5GsiR'
        b'P6BXSI_6@zVMsG8(;TO2P=*_XW~1{qu(ab`1NzMwM0x!-bw;LCgC|9QaaXHE6$eDNA8#{P;Q&BS<~n?_eSe$z2EM@42tU9Vhn)0r'
        b'4RXgS9OyTv5oH^g`!b~hJSqEyyQUtF#G@)^t0PFC!d*1&OE>pYOLG<rNJWZLA&?w<+4lKuAZ3*U9Q^@jI}Zu!hX*}u=WbsF;RSOR'
        b'qKJh`um**TW&MEK)M^c@$p$nh{^NGS8Cl|;!GtqZ(ieAk0h+(UZS}XA8dxi#l4AbB)BM40rV75)h?u(DymOE|G@cwek)m9TE8d*2'
        b'RRgr9PA>LG4zX3<2Jwx6`5y=;9OVGO%VWZCpxp+{t7j3Jjbb*!!u`(Gbv3Ap!bq|a1@qz7Of2V?(TIb$YiYTLHfvchFL|FNAaXUG'
        b'nR9z)++9b6w!hrIM9ZP;UTrqLD|GuY&Dfmcg4<0^MEhC!=_;$_d%yhjFiF*})^!f7!P_(&fhXm<uq)mUzoW}U-&O=W#794R+_5)5'
        b'y=qsO#NO;zwKw_j-P7eduh7yj;UfN9lH3u_k(Ioet4a^cvYhwJ-__zd8(DcsX!|{+A-vjDFLa;FW`1`Y_{hNby@)nqVW?@I(28dI'
        b'37}q>b$<>KNJPeMItZ}@p;Wk;^f{_UNxb09=}6D{qUUdutN3F*maqW#flSM`04C-3%$m$h9JlT^DK*^@=@+8x5d(;EYnK@A^QT0Z'
        b'xb`;ikp-0pgv^@Tmty3r;=+h%-#EW3x-#*3^|wm|E8h`)c8VzaoVrG2l32(rk?mKv$%U17M6N#zfv&Hdnd1*Uv!`#9^Pz7BS9eMm'
        b'yZ2;lh{Y+(ms^~ge3XofPK;06v~wHtYH_}@Fp0G0D>Hor(CIya18Ded037M^d2<AXcgO`TcMyRTK~}(9-d%X69?ShVGS)N@l5jIb'
        b'=K2|fUFSB~pWlY|`T}SPhep_KwcDU6_PGtLuP#F4jMo`7pjI88I5G%~a00wXT|{-^;4eaY+pWd*bdko$#u2hK>JovhxP;Hx?z;Q7'
        b'TZ8;uo|`V7iZ`2ast$izi=eoubT)$F3NwN=aT)|iFdt2wkKha3yAAbrHtidvs8T>A?04?p5hS)4LH=Jogk1sMM6VBep`eeOn53rm'
        b'u*B%J_?<&(-fuSGihtcfzaP}M<A{I-%Kz%1JJO(nST#mB$3<g-n1;4Qd_5Q*iBKcJg6Z3RG*7Z>d=dv82z}h5u*^1snEMT^B??Jw'
        b'9YkU@#v}yMuSi(W8okjJ0TM$QlTbB{XjW{dr;nR|c_SJt0uOK8i1`@tAR`fJ6f8Fi*BM0_M)Au=uN<SK)F?e{B##?soion<(m3aa'
        b'5jeW?mdBCI$bE<g)R%#WHw7NF20XNS@GvHTM^Y+yr0)QaU1spG6oE$x3m*1b@Tk889?k9Gad{9tt|JjQqK9M=H?-+83O?n*ri;NH'
        b'7lXH6gV$7=&B5*0g46nfulEIK+zq~Yw}s;r|C*(J95s{<igI9gkw}g9w?O(<=$C_`PkCZ<@bqyVrs*2id24PB;~3_H;XxP?i3yft'
        b'!gZJ^0~5cDdF5b|QcQXnBadUV&SA5^#OB<<WW$)Jf1o}B>!ZUuT7wPiv>JR^XVehGx+INYSeLF54(oPlM8i6ZMm(%5(RdB(>>A0i'
        b'u3jS@)-`Kp4eKszW)JJGYvv5=hBUHaEiKc?!BejB9u8Jr41V`waOh0`*lWSczF>P_aM0c0Bd~u%O79dVZl^AdRtf}PbM)hw2<t{@'
        b'8E}WU6~Af&GI~8t{%H-KRlL`BSt+}&l;;j{q#k~u<1G4!3_dD=sBsWWLu4q0wD}13;b_bt!hbS{x`}J9;|9Z^hL!;@UvZfL;5rSQ'
        b'a(efaGt3**gZV}jNsRy?c^4NDqrc%3IIJJh>m!?*dhn);L{nsuA!1M;SsRBh7H0W?`6s*uv}#Ky_vx$nLo_u*n(84<mmy868JaHp'
        b'e7XxqgC3=cdWfdW57ShS8-@n{S2U47OVgV>pl)b}dZ2zr56H9+^X?p^^EjmQOGxLv0S}#D`mD&p(dmIl=$ssQK<Aea(|H^>od4g^'
        b'd41sL=oDl^I?q8mkKd;=61l$?LHefsd*F+8h>sqLv9(9a+c(IUzEXyf0d8AUgXw3ijp}U?aENDZhU?wu{TStdxmCvO9{|RuK~!7O'
        b'bSR%x6h8f;7h6FwEdxs(CEJno7Ebjxo}9^9Xg<PJ2j;zTxCoi?2|pUJid)stW|ZwM%rDa&q=~Y)gLI$Onmft4{jEf6ztp($$wi`!'
        b'x#TA+bAriWeI)fXz3&si2_d{;KJUgLNhH2EuvgH&Uf!A)5R<uNkd(9pBj@+DKC?G3cZ%D*HA}b^AFdI7j;j8SYN}=D(Wr`>qKw_v'
        b'sI>nXDE|Avc57aA*6Q>|VGUW1R#uA3P{pcgW!XS=Zus`Cr)ISs9B>{Sc;;E#!2#8IvGU+RxH|NdwC(KyXUV`bFF;CJ%D1qjtz^LY'
        b'=YePb5If45&Ax?YZGRbX77RSIKlV1K{PRF~conwV4jmd0Ig_TpixvK3xp&+?1MncB-+db%UvIrySntdk;1``NkhO~m-Uo^>4`_ps'
        b'Ongq=>jMC|a++h8Qj3B8toy@2=y9y>HJIz_g}KSw?<utR3_1NZ7;yf2xMh;$Rd<~)4>S^>%@<*tLihfS;xfkkexUd_1JJD&(9P2{'
        b'4cCM_xYny}+XkH525ip`)Z4OL4PwV@jaX&*%z2CFvDT7Ccuu~9_t0981840H+<)PnY-M<Vl=ikVWgsnXfKr)5pHkAF!j{Q-knVQw'
        b'MM<(h(Y9{Dxehd5U^5Q5>c#NT{tq0xok~89w5=I%t_4M<u@ju?4dBJdjviQM4-sk3QH=uEU&V_h$rTfS#DI?ruTortOjGzzI9_SQ'
        b'lII}+f)Rfo-nMMO`3z{IE*2gShv({tIrdye!apee5sLBccRRDL0d6rN{1@kr8Q@BvY6$eGwY%_~^A~_!&?8q4Jn*e3Bc*(70CXi2'
        b'lRFm-K*ygjP4heeNSuBHQS}&jg0Uki`#^T`=6i~udx=zkBYsf;5Sw~orsOV!5!B#}WZ=PF7EO{}lWrlg@1F#m6`C#q$ijk)Lf|+T'
        b'L26sC1Dd2Bnx^|7x@#yJfUCSj<+#9#wKjm*_AK7&?>Zp1rz7wNq69`@U>>Dly}M0>Ak$yyxfTNW2PNhXmx8r^-8R<m9PhV{_t&$G'
        b't6U6yGgJ`b|0VoH8nxtXQf3VAul+?#N-v@{f>WqVNB~CpC%=48t3(v*KwybfrgBo6^d)g>NvVcPZE<l>umPJhV<avPXTzyj7<9T^'
        b'I4>uF_T=kG+rRsr|L(Va*I#dY(o`aL`^&CLBE(;3r;+4tr0wf|=hywVOMtS|rXq1|2VPsdMDYchxg4v^6@ySfR!2pnu8(jl8s!IM'
        b'(v$*%oy_GzRTU0zC0&zVl&T8x*eU*;?%96#9m>j^0xgXk`Vw#}4}V@#c(tvu-}zC$?IghRf-7GPM4KQs!TXnEGxs&gK;SoHAo`j~'
        b'ui?|(_tSweEH>SbS;#efx@#s~&!TXS55enL2%je0bKa8%5idwv(h)MC^1A1K(Sy9zrk^-BZ$Pv}ry;6gcfI@Rp_w$O0Mp$Zv%eom'
        b'YF-JU%<m6FYtWhNTK8dGog8DCfnj(U)6jpwRJu6k)ft#Q00y9gdMccn*(dYhyTLIp&A|QM4F@97|AGV4A4GTqp1!#AOh1A=cZ>>S'
        b'HFl6+U%1={*EF8*w~EWu<#d_O>Q}DK_hvTr=i5mTzL8=}`cszlC`-D|T`zHcKj~8=Fad&-;PhB4sS&&=1^j0cU~<)}qf0<MwH?G$'
        b'&f>l{L0=7+?acQOiSw<#Hngt_Ys8^$SOKA{+;=2u@IoKc6z85WfZobjqP;@SR++)T3|7mleDWjngYxkjG#|C3p_SvD8g<93><IHN'
        b'Y?@+68EyaldsHet;aY#M_!s@2D_!vjv#8(B!lg=k9G~L_7i$zc4#riX{bt(iz+6+DEBT)3N5T^a(y+Z{5~dI$Kyu`)gQ~(jvZ16R'
        b'y88_N{Ti(~>O=pCvwa|12G7vrv)dH?P6d$ee4C=*^{ki)gsr&kzrnkogsW;+g7ns?N<+l6+UE2-r2x3N1#YPG2Nf!th)jREVx6$f'
        b'tKUh0vcI+TLd_buA4t|Sf;yt#Fx7VvtAPu+Nihf`fbADv{fX;qo9wIO`kL8F)z=um$n5E&>Ini2yFuU%yH@&0+s68w{eAUpUF<iU'
        b'$#}2*usoupk3DRz9OT;V^6JB?LGF>*)5xM=`cq4C4A=W0)?g%b?(DX%K4%wb<ecsMKGRyU>L0`*pz~(8-RyJT0NJ0$@_t1Ue<o%V'
        b'VfbfXJBZYS9T@O?OgFiuF%H6YgLBmZ{UcF+(ntEh#bzS{b>A=Vfv2h#lt5KzY9W|QeI7N;uNVHak6#_+mx|#0mjJn*iS0W$<}-*1'
        b'3@Cq=5AjS!IG*QVD~6^%)^4aiLQ9b8%V5OXljQv7ewHBOaIfYmS?_V?6odmnq5iW;KT4OQ(PXzqrs_%$;o(cjxk<~B09tEDqDq=T'
        b'!x3-y!ch~%y4NzNcQI9-+Euvwb+Lr0^kh*M18Z%vY(W^-lViX73<AU(sy-46!<h=0uf`#4b(6BJuZjp02t9Y9;ZZH7gs+%n@VulO'
        b'n780daY5f&!PelwL@VqaNgO>A)c%H?cOR|dJa1h<4DilCPQ^@)Bp@bs*fZalKR%!)A*QK128of!<D@r4Z2ZdT_MI4n^ePu@GL#Ds'
        b'`e<zn`|5V}RonlFSy=Sw8LTLuDt@W2Zo0Rkg!Dgn23|q5Qlc(7GuB%?)(h7kg>d`v34m)yFDYpdzk|P$@6%o&FR)m}Z>#T}4?wK)'
        b'&l;`<RM-8sFL0H~#62%L^qT2&uJR^#4PEWrUk40CH&-T)I^|XQ4M*EhVIYFUDcjcettt;FZ$Bc}lsB<-)6!249)V{d4<5jT&mhX!'
        b'zITZ5;8o`i24X@AQLgRVi@o|}Vbm9YE!j#Wr6aV7P{#K~t8`fW+<?evOs$L-P%%wv6!bqlhQwU|;#!vgMHeAXF~kd^`Slotd7`iV'
        b'wEXH+LC??}IAObH7rs<mZ*Guw{*4Hz{%q+F`sya&-vzWrRbVYYfcPQzD)1SEa5B^>``WAIwbkb97_50Y9H|dQ4$VHf;K??+&q?>$'
        b'g224#uk;h2To43LuSguqD=1sl1SF(xLEqKtk~BecnvhulN9%lAS)v_70?Grb?M7tvo&dV#Q;x*f;*d9O{J9Nk#|Ye1O|oIV<BWIj'
        b'QlnLD^;@Y6HvGD`&epRk(!GiHIr^R4^lOfyM%PM`Z0LFPiu^56>lFX>1b6{y*XH%F3M{~nR}c0Hp}z$t+w+nd!u7aV=)M!J`hbfV'
        b'>jf^eVjX4)LPE>7mig3m_Bvg?ZU5}C`ly4#t$AUTHL_5xULF>wUY?JcPIJi_L|cEav$wb2rWXqM&yN9RFF}&KkhYFqX9vjF+J5YH'
        b'iNu!kz{$_HtU{8@koJ7}1t`Jai37@WyEt8B>~#)!5c9+{w$$`4XL5Q(2KrnroK;ySuRGW4Z0>D)ucxAn#15(nQ$5fLryX_)(t5Ss'
        b'A-_-!j|oY>tw00l0IP7^6Av*&Z=$oOATq%y3y%cRUqYme#Fj3J`jBLn_2}7AQn0cChkOElQ4%onpK|PGs_?1<Ev%@k>s>5hj`zY{'
        b'=J$Iy#|Vc!YvQhSA~T#I{ax8^-Nn2QVO$AbGdk+M-Z1gZeW7|vpJY}Z?one_Z`wv|)IC9Bp}yg^Lp>KU_B|Q<Y*Qb)x^2}zR6haN'
        b'=X?JK`9)&$8Q|<j^}wZV6zD?t-I#;D`>yg=W8BxK^S#{mO|Q@1S={?QVHMS2Rxvapn>B|^p%dl6tP+b_UTD221b#d$!E11xs8OQx'
        b'slnh!Dfqk07Mmc?J2q4uV6kDL>RIsSl6_X89cu6!B8!d4D;Zue$h_7Ys-Dlh+M8zwa6s|&FnfCQO1`6QIKMH%?C$0D3vCnfCh#e^'
        b'HJMHel{<P9xA(?jYT#%xzlTgZd%bWwh%VqiS3|;l)WE9;+MPe7*DJC5GzzV1;IKnlC9sr~s=aG)P`o;3u|)CO9mrFyO~3}_c+Q#g'
        b'J`uAKww#vG`@CeYum;;JY8N5X-G!A&G)nEFl2m@lyOF(EQYez70!|Cu)fXV&FFoYjh}MX}YimIqu0x}IF`KbhC%n%d-VbGvFoQC>'
        b'*Y1>AF{>KJ6;oD2nO|A_*;|U`L|IDVrgEGQXUZ_MgDUfC_d=4d-g6ilQLDc-4#K}?MavBNn=Bc?)-_7h-VOuk4qOwrsd{ta-j&^k'
        b'xz8u2A#vC;3}{$Iur!5Gd@YIdRlFe~v6SUua&l;+me+oAAV+E}Os<v#&SeN0KiGA}X))*vt{UZIC=nfm()5Bu-jI_RGOyc9S<)Sc'
        b'uB=DHP=m0y23HfFbCJmv1Ua!$=a=GBgD0sJfEP(N@x}^?C5W(`pFW{RYrx1sqWLjcEQu8&<cF*4z*tU0;bg{o7EAIfyo{f4$=Ubd'
        b'*eJG-#omQSXnq8gC@RMIy+Iq2c&mp_BWM)@_(;<b_gj+W@HuKjig%Vtkr|k>TQN5<g-%f&n(NSBB=U<JaX^c;SP_nx&WIcaQl$1z'
        b'*|ldby0;|DvMo{Z?)=n^*OOPw&)OVy0u!2$RqHl_-wdQIu_)tua;#s`mg~tK^Av<vIz78rq5Qn(MdEqfVX*pJ)c(n8(uz3@?mYlS'
        b'I7v!{s}UO0DAMnyecYoKsy*Z_6*vsc%5JrPacsBxdOlh%Z$#a4x~dFl*Gt=|LnpEfjS{PZeEhmt^P;5lT?r|v{UC>hw@=W;Qs!8X'
        b'!;m5d^FK+2g6_N}Q7j$jm-}nH8fRS;<`<XSzT0^#ZIS_y@MbS&EiSWN+1Zsg!HBl|HC(y$uDtra^Ad+Yd(3?FxS;M(&&FraMl2vR'
        b'_a;Y5K@HGi_;7AFNBWf+b`-#aq7CzpW$k$?c*mR9zwfgC0pJk;u-7*1$ZT5q6y5fh9%oUHt*EEo{$l0(BI^sD^0LH=4Mmwv@M9IE'
        b'n4I4zW>1x-=I5BtQ0EOGMDDTr)sW>j2xwCj^fY=U?(VrLRSSSzXdQ+=;u_8~EcZOe?C24G#xXm4az6#~4D?CvIk(RN=1^7-82c<N'
        b'J~1n#T?m4W<n2V3VXtCWs7xW6rC2v>Z?ZKp?<CfuMK+fm1iu>O*a`=*R9TX&7Eod5;_e-$jBRPjQ$nku3QbpI=^;dNCStUqaJ|Q&'
        b'Ye>6@0yr!Bq9i{}vHjkIF<vX_-R>~NrCI&;yE80m+4)4E1HPqFPn7b7$HE_)mpX$wNS&mxPdOqRh48*n7l*t^2zxmP)<~T92QVb4'
        b'QuyvgQKJydf`8tE*O?P{Y-oDTnxFVuWb#*cl2=T$^l^q?^u&G#`fjvgvEM=-I1xHctPBNApwek1Jp==^0wJrIlf^(L$Q5~W_J-^Y'
        b'JtT5Gby1M-Y$SjRvpNg?P5VWP$k_lWdF4qg_9<lZ0l=KtC5U2F>gLWL1zB%{wyNsli?iw!9Yoq!x1w#STQeLCFYSd^kEA4bivdfR'
        b'nNJ1?9nAS+OE}tK0~R9n8!B~A6Ug5frD~J(I3+zcQBVEhw@ihiMPl>TjEm4?K$%k5+xa$Nv3WVUC}uw|-2vpJmAb-MvG31X{Tj(~'
        b'XU!}qDbC(-Yw`BT?biHa$Ow|;nXGj%eFFVg6fZDvDqQpeE){dVTR6=@ap7;&J@pe}Op_bF@21mabTCjEdbi3@c66sJWoj%`0U41T'
        b'K8se$6_#09$q7N`&=Xi}B%+~~B<~^>Z%PxuOFEgZlv6L8sT1ZMsq2$Z5R|FO!v1P&gK-TBI`doDnKeQyVOPp{vk6#qRR|K-gk}C0'
        b'MI~XtI#|-+JuHjT`|Rnq&$^xGyKT<y`XjSluZeb~#(e(@XfSYMYlCbN33p^y!v+@#Te>+U5F%I!(}6<xg^Rrq$=-R5Vlb$0Nm{pW'
        b'r#IGPx!-bXn6K9M39jKJ2}&{E=GbjQeh(kmh1fg%FTn?4Fpg`c0QVYkQc`(=Q@z2>d`qDQH|5Nnu~VA6Nt1L#>+WTO8bJ%Z<XD3-'
        b'72SZCqmf?ldobO6IIKN~TRxaJN6PB5yMdjktiGoxn2shqOLK62?J&h0gMEO}1zh{Qfwbj!JM+731>N=Rp33c_%FugOZE;?=xu7ZU'
        b'l%$HLZK6T~9?@6RFzm5(AFb~peMqcj68af52AAUWA5zJ7gxLp)0M0_8#Isfae5SqK7B%|N_cgM+AK9mM-Q(`Vx-Q_E;Q~90R(_A0'
        b'9=}&bduXh@!<intXHUmz7J0ZIuRYWc=C=^Hokkcx_~P&;F(&WULwFT1y9#5>xA=t(9x2Fg#N7J^wuElx<U{bz;BNPFbmfVAY&hj!'
        b'2f<YD+?#1{Ww$$g{2i>se9%>A=(at3i=0EXkA^m2*KG)Ors*=PAN&`^EQ6rT((Zk?U}!8RC7!Q3iTULHPe6&8XFUX<+U_t}G!?I*'
        b'zQV(hMG5W=l8D9Knj1du#frki5evIv%qfKbCpRLDe@E5bUI=)I5oKt%8f!uj^zm-BOh?6O&|pyHIc?=W8-j;;6CpGSoWRE*d2o>s'
        b'VHUvG*eQ=c>_(ORGH&qe=2t%w{kq|<xyeTGm%MZse~B<2Q+-IRTt|SgLv}AT0}SAn%AvcEPZ82?9xxu~T_V`#yY%cfQMXgnZ4(1|'
        b'+g-U_WWc)lm0Q=}2!`lxFL8&#W#Sq_<2lA;dY>TuS}n@4Tl{z477Qv!Z{>Q{PTlK?rm08Q6WyPC`uRO%EDgPXu5HB?^uPDX<8Sdt'
        b');2WVo#h_u8JVNl?7#{5&5EPCxg{5dmr3mx#)`D1?7|!>NX9RCSS~o1NzK}v682AT;YXvf+JzLQrYI^qcP4J3%)6<wY_o+bvVx-B'
        b'?hg>a^#hMQ&fuC!SDp|jIK4Juscl{f-*|1p6I#4B@rQ6o8Pes0oWPMfALJVx?nB<@WbmKz&J6O`xQzcl7T@BsD0iD>yWa9Dtg>Qd'
        b'-f9}6hadU-Pkb|JE1m3zIxw|_cbrIxM}t_!3hO<G7W!C{d;C>t9=5Q|>Q|V;=fh~k<73wq-wIq)gMyhj)d{r|x)yWbjYI&=6hc8?'
        b'9hsTbPX^RT8LLO`fjw2`-ZJFgqG^9p$4eOL@44`R@kxXER$!?6UPUw(@uypc*ZDbxyRXBC;mX%;@o;7j2%i8g7;R?#!&$};azHNm'
        b'$s?JD7jJ<~!|!g*<mR`j_J||4-6Df|BqXW#plKvYf96$4bz;V?k`J0_0kS9uOyjiFTN;|8S0I5ni2<kJ8Xj$^idZzK54$KN|3LbO'
        b'rNt+PDZ}KiqUFvohEDWmw!ud1C{^ZkCfzEkkl6*uHJoMF!vpFDs>Df^%cGUBf&0}BVG&`dTUEg3H~nn$%sN<J{Ht3Kq#S|}{{^xN'
        b'g4m*Nk@?r~a-K}`*Z)l>W4Ogze%miVTU8OTsNCQ#1g&~q6xOpMc=#>~f@uX9Iai|zwzh5b@qV5NiJbMkIAonzdu}p`B{WH;$_2MJ'
        b'VWt<vq<>|GSoIy}n!_pmZyEgEgSOKja^5iS*8L$N($078a1REraEL_jTdDW&@VIr*BI3S0khe&9xj6;jv4Ot<1P|55;i)k)UI)3y'
        b'n7BnM;3(s_9vS<<H&P!JnTO?KvI~mP5&eBcV_m#Rq~Q985Mhb8yAon#iGy99OF|eAvTuoggX{q{i9KDZ?qb}~*~NG2k?t6*oik{d'
        b'Z#z8(&a+Sa&#wD-y#wu@Z?FBi(_X3fEFkcor}JXI?jpTr&aN|Gc2Py^>n?W<mZSV9qiV}#b(gwot7Q+JiFSzVTDz#XgW(;la`~eL'
        b'pLJ2?upsr3f-*6+h_KgiY`JU)E%$te&~49(H+9XVXV$5y>|@uN6J53wU3^vLiLRNZitD=`p`Bt!Jl|ttD!c5g`M=M0+Z<gphr44('
        b'XTEvWW&6C-ebieD3Mo7KNEQ40kj`csBDJ$$lr}xm+S^@p^F2^%d#Q_huXLuG-L{Cy=$tu6sx0hsuWA2ct~+hziN=(_?KJ;+ZiwF;'
        b'Wo}ntnexpp%lUhxmpQD|)9>Oxb=jCM4UM|HNXu;VJ6Wse(;Z=6<WgqUeH@0pUHjly9kYleTe~?Ec5oZPUu7V3Q}@6MuM&nGT^oI1'
        b'3<c$iAlEc)py=jyeg&V5A_+2p%FZD-1UjhIIhWZN>})3WTn?3$vzRdbFx~XEoVrGli^u?wZ@M;pO-Me&zgK=geU~6-lZ(mc__XT>'
        b'nEo~S;!OJ5^ksI(rEjTb7EE;%*7$CkTtGen>KtmE1tI=DZHVhqzSO~!6)G6#Z;kHT?LKfGMz}ALu1Iiqn@}$9ipKcw4kiUd^KIs5'
        b'N75Dq^yPUe=*AjqeJPoFncW6^@VinnYO%m{d79i1`_Gwg!adPNt{oC17iR$)0F5tJemTu7>>>j|9>`e>C<U3I&Y}Y5b_YD3i80|_'
        b'&<6|Zsy~MCaxIMnG7WDiy5&HlIRGX`k$d8a`TKgseqBXw(<6@ftb_6Eg2%>uyTWkr@Yoy~<I^=`d1m}{xmz~O)QGug^k9itYTfr;'
        b'UNpL3aFIoL&vQ2NE*H9#qAHq;>J01|bJ3Y*3yYjAkytX2DxdP8ut?Gm8s_K3dER~&md*2?SHcdG;)5k!WEkmZx3$AtU*xvfX^xB*'
        b'dd^Nn^mg*<MZd~7#Fs9N2?<{7`2ZDOIR@`321IHKn&Yu5?`S$-8#}=<*E;!b@>>oXjj!24^j@*s^sPD1iOJ>QML5ER_{c5nU`Wts'
        b'vArB=C4FkdE&beD9MD8Yf-Dfjv?rI|T`MLto&!^+-Te)^G~_uv%3H2w*{Bk%WeuWb2f<738pOyV5lx+7<ZyoEcwu@`)i51#wv(I<'
        b'GRd{%@7$S{C*aUo_@P5pLtI2-C-s*Ijkdn{!%oeUN^@irxfj9pW=$P)vQrZ&2l0+IBD7(P?fuTW_dEI9d$m@XMn^G+VJcd}_jKO{'
        b'Hd3Zv&g)*Wf$g;LqM##cfVUufU}BhxPLQ@7K|DSL5fR@J?FDi@!GZ11o%_C+!J&_%n71H~c!(oTY(IvuZgV5%)3&@$kcOWPjPc-o'
        b's-p&r_hNEka|TN%W9j7Q2M{KW){U>l#gV?bA3|Y|Fn3;N3Ba367pWPJxsFUn?0dj5_XIdRO$Nu-d*+8>Tc`V+kv167EcI=jXrLWh'
        b'Q!AJ0gSigz$~DtZ9pV#c;9QpKkKJ%?7HGF1m0xlV-mViIsBwb>GJs^NTgd`uGo)9U2!{`QF!5A}rj=_UE!YEETorKed^+4$YSaW^'
        b'v-yE0uo6mRCuNl>vs{#0=M&0bbsFM2<1ytgI}N|&M-S6mWrk&)de4WQ;g$)%mvMmuEO33ynTojkHc``g-zFB*oq*Gi*b{OybK7<Q'
        b'K7gk4clY>Vp)^E07^X<M$JB}=MqQMRrw=#2&jIx2RdNq{x7lXs&V*{YIYtHs(nfXOcPJ#(+eA~mynW^)&2Cwf?E4US4DIpqM>B7N'
        b'OplI{*kqm5SA;u1`_fwgQf7VtY?bW$Qe%}3UXx#PQz5YlI;l?~{DkEC2S3&p%G)`anS*7Mu)-AyRhzB9CcCsouD=FzzjHS;*eVC@'
        b'G+C*Lu@1f+sQvI-KykH9@4lmrM+|lt-{U_hi32OIua*^6@MaLVeDIc*-DS4OG-qVBR!aK;{FH>*oNZ*yK<!1`=vXNZb#v#Z4ztIp'
        b'iTI%-kN?gr@Rzgo50s-D?h1gD2}j-A>1ur68+uyCe@+*U-&!nLJI`h1GX1gK=Mnpbd!#pO%uycW4GWf#Vh9Pwa#IkI2@`IF^|LUG'
        b'4KZi(ceXL+TnF!de3q_OIy*{u*C7i_P0cRKq>6XDco>)^KA0=wi$s|N$`c*MCp$D-<h;-oWy*>_>?i_b?`e_;V}@=P*LHX;GKOS4'
        b'fPL>_Smlup55g^gO5sz;r5qHLIg{O()Be`M9J>h#6xt$Pp7|hTX1n+-_P8DJlRa#?%pZuLGZAJFlv>6JpSBe)rm*83_yGtt^dc0r'
        b'MEO>S+an1zKnW5uf4ynmAor*-VMJ;NU=076L10`h?{k3qRF9*Y={tuXiKH4X!Q&S%7!1*3xs@DA#2x{5CAh`Th4^B^_qeoQcUbKF'
        b'KnXooP6)s<eP!;x@f~x<bqLRMgAZja?`S#a9$%eUbOXz6<6^(@%-=tA&r9HmKGjd0W`*TN2`SP%Y0sqBGXpoBn>)-w7V~<G`3-x*'
        b'Zw&>OK{c9?M72G4)BJ>?M$m{ck&qYcn@!~WyeH9jM77OLMXgQAiv)R3{h#VL$@v>~=sV<TIy@}&AVFeVb-GLMqSDQ&iw&gW=#wZZ'
        b'l+xiLdYeI(fwJ#X)s>nw0~xS!DOS%S+v)H#7l~^)<L~l($dtr*Q_cIXjfP8+=tY8@b;*uu&QOfp4YW+^@xK>$C=cD_bxy>h4xrMM'
        b';ru-F;>U-#zr5}_<ZV-R)P;0h#K0Ic$P6YP$6J{C`n%q<)DFAa>uAZm5;YcjOWqdP;SB7kw=cH^biflA5yFP^C$&V`m4jMon_q`>'
        b'E+~r;PH^WNKJ%8g`F1$vAY(<#FmNr1^XkywDX8+MLf?Z+g3ASQU8fvH2b#*eAU>*s&z=Rds~kl!P4Qi^lU%$YrAxn|X_awPSG;4!'
        b'uhy7-4~g42my>hV+qc;!U2ykMEi7w3c${pz<8n@d?Co$7({VZKw6ty9<s1b$F97dEdv3ytH+birA=`#s&H<4768uhy)rVYoQcSiD'
        b'xSZV}Z%1r5hlsMIZM`mM2T1RX?cnyEZL-S9K%lU?>hpc}UDQ1Ws3=Ua)=${S%M>~~G~@qR>&q+${g&@*0P-G9=gvWplla`GNGkfV'
        b'@_JppW@*z{4q9H{RUbRZ>1ID2c_~u1KXR$gibdBK<VQ7p-`3`GegUxMwp`%K><9f$@Z<9q*7{{ztIOF6N&;*jyHx%{I4ES9LtS>T'
        b'L{5V-xh`!x>2iJo00LXaxFX88u)fXdayEgC1@OkX<NVQRqT$NPXlYxm%Xu1PKi1OAU71hPmuT5}zbjtfo}Ja&+;+m{JPyhp2WI||'
        b'Q7x%*ydw!cOSaXyoHZajRM^fT=N(;M`xlW5;N6#5mo8-|&qhO^Mh`W%Rk@r;0MMeAZ@827XkkrTrOU~Jj3;t0bGHOnx}?{>>$)=k'
        b'(q-a1yv%Fgxu?rD<+A<d6^Dw>G@aN_lskX`R5@DidSttv7E>0gw%xaxo>llmTdB)=z*TSCY<u0Mk_fLfe|ARk?bANB(@kT4ncwyo'
        b'm$MKQKF9A1x9xX1^Fiv_*b#2ug{MK-B->wg^kWf8hXve{erGMSl33XMXs`WY)#YH4o+$Jw2YI@NsB&?cnq00ar{I^zzq5Mo7;5ys'
        b'hln=Q|7Glb;F_-X|MByFZv%w4I{r8jD7V3MnidRm!zji?#6K01B6jTt$cW5JiJR7?+=l5;Dne5*s%=W5S4z+lON*fr8s5aLl)n?1'
        b'T3L|-{`dWRp7*BS`}ur7kH-&v?seYh|DV@6=XL(Ooy+0pO8c{v&s40J&$8UkWzaU=<FjYn&KIF$_V8JX$Qm@go@-s;c0LE)x4e8d'
        b';al+8Jhw9&daEg)aqIT_1++fvcK#hYYmoWqqOG)7D-PE6TrCTajqBlR3jeJe{j<n7rOcxATeCrs>Aw|?*ahAiT~Veh^YT{N)iP8O'
        b'>u??Wh}C74uCuOPRa`bDZq4qF))coh8UBCVbj+K_<(ATh5ZOi28t--*VDf-n?KbvHt~OqY6I)NL0k7!X&UhG1Xu3-CG8Qswb=|tN'
        b'T==$%fO2JNnRr)mG#w3W+sBn|Zg@N3{Jy@oxu)xU=_&eg;Or^o@#Er>TWZ!;(V#gfEiG%%?)x{o)V|FP=l30cd#HC`t^6%hS`L?%'
        b'6R=?Gf(;8+aguT3;*$${7evippA>VSTdqiqn-mk_enc6U6cg@_n@fLk3J;>cS2kW97orGtb3?}!I1a@tZN2nxuJJq>pQH$Pk3(ZS'
        b'E(95s8!V5Dit%?V8~fnXQ1`eH_%y_=;HYPQ@XY5=o{NN)A=GFRv=shsSn;LizSR6YT~DaCq$#=iQ^Xl3=1&>c`d6=0<hHl>*4ck`'
        b'yCk-G4bwjlPdzM;-Yqw~d+3pH<*=t?pSGqZHDojv_bjkfTj=g(a~Cz!^<-FPqEu&2)18=M(QXjw8sjV}7G0fogP%@`@hD1FIit+m'
        b'24^e%(v(9pO(C)iq_wrzc@ANIZa>glby~8barxws`CkNP&TANaYh>%OUS~H9_o61W9_e*<K>Y<+@sSOM-!6Skx^B~^&nKoGzPj#{'
        b'V%Y+p?H1VxpJNh4X&;S}wdd*Ba2ngx<qgF>+_VL<j7A!1PBO!PLD;$-H1gXm=1)D*Pq9#@)SY;};5EzAR~iP_{GTb{RI4v~`OUMP'
        b'S=GoRkB*7WAM|)Gmu9Pu(ETQMvS7~hS+ALmJD4;@NVcu?=^YCa(`>ztEZ@v*Q)-&2P9e_xM6QZp#)SFi+sH(^{8aZDPdAAx=&chf'
        b'EqTL#Oc>iVnv^TK38gJkYuc$f2bhux&1Sk^l_pZTUF4gW$Z_9>#9Onz4b{>^e$lX&MNc!*#TT(oq($Mr)9ZY<w{FXQ_C>v_gAyH6'
        b'a<H|e*SQv2_a|THkBF7ZVF=gwpy*r>+tk5(4u#kFRDDB)Mc6V$$e1BR+#fR5Wwz>u?GO^&4~U>?O<WU4FMmw_p7N8man0^wt;>6z'
        b'%X{k_AKFuTjr%32cd-Gj1-;IE=zWAnNawIB<Lbud`4sMkuw1P4@<h1>u07RsSnCtL&b(f`4y8TaSTCur<3dqE)k?V%LpR|P7f%J%'
        b'(lfXd{ZK)L8j0$-TG(@KRgS%&fQNOZ)`oKSTqv{II?-><K56URUgz9iyAu9Jx$7i%*TSA*JJ{AId!0`rI~Lo+d+8C?U6L<ixz^de'
        b'&Y94Bp$QG*m`LA8(v+Xwl+Tma*)BS4jH*d8(VvrX;u?uOxyX1xqSqI^;omaJmRwYFsD?FuEvfNUeJuoYqA{Lch`~Kp<73=NPS{G@'
        b'PTc)|pLF^jV?Eo}Rr`6m`3K|rxWJYZtrL5l6MO5nitK}D-P<Ib4;QSTygo0GZo?cz7dp1rse-Xs*yB#}f~J4L`iv%d%8|KZPL@8^'
        b'*KJ`mjqy+Kh+{Oi-tCGvBvUli%mH830LcxTS9qgFWW2%VY3LCRmk)W-KR0ZAePD*+m{_=mP1tz;xPOgEHB@x5mmBJ^l~SJA;V^zg'
        b'e0&HQBk`vqN+FY{u)W$)BdYQjE&u#u&S#>qI}n1GLqSK<XuUoltI<zPHp9zX61xBX%30^Nvvpg$><wp)n<Z-HNc8rDXPy1f>jsCk'
        b'O!JgXkBu0z$O)&^^>2BdGsJxqgO%QrNOj^kk$TRZv#->@vuB;>&(>81*ms^azAtGx*y=v(JPQp@ctyux>(v`fNUpf*B5Td2GBKU&'
        b'5LfZ6_wIwnc-4D%)*{Q5Z?hwxA5!nAu2b5`whw}<FL3N9VO({!wOnaq)@)`=mEya0Ilr;LD5@>xb++P$O;b4Q37fT{x{>mt^%YC='
        b')s0r74w73J(LROqTYX0s@VFaQZK-c8uiLvhWYgwAD@(1bS*4Qk+TZl01fH(G##>M9s%U_}o2{1SzT`ok^ApPZu0KPmj0R3W7b;S-'
        b'<E;}tcgoqT&I(7bpXu=)^Zw+l&^p;|XU!Q@&;0RO*RDX*J0s*)W>;OJ=_|SYgR^zt-7?Rirm88oO0L_>&;IV)N!wJhc~;MVocG;u'
        b'_Lk4@l1?!VL3NEc{zKwD17CIH#@%%-g?CL;QG8Y&Y2$+9Jag-w#Xt;Mrj7JoVxX{`l}FiPl6#^j+0<-hk6IM294E>Rk|~mVV4!A8'
        b'>PE4Fub)+ZLgZ1F@qt4*x>o3Q`-<RJOWhK>KWrzQ2f+EoY{g`c>q<71Rpe1?I<``zu@Ox+-CX^?KmC1+kZGfcA2YP?$Cntz_@285'
        b'SaocuD2`P#9YN|C`T5H_g<qglPNL5R3u~?N9?yR8XpK!LQU_~-NVF^Xa0r1F>KBy(&WVNuj#Dgs@a(vltl4KXY2PlA3v0`VyL{9N'
        b'DCLXDv@oI=+VdZ$W;szDGm2FQaUysqQxZ)YnKsBHFJnai9b~ji1T(?fecofYe?_0|yKK8Uyz=G0E}s!pE#Ln&;8B%4d3E&AK5qEX'
        b'KF|5x1!j6Cv$(dxxxIDYnVzh`OIbnDB9SI5IGW&B7R}&yWHd|P7$K$d#;j2%vck%;!khm(p^%m-IHhyx;R`-UB-ckY(!p4Ui)Dh('
        b'l2|!%h}3$I8aK2^qfPq%=da$R_beBCvV_zIH!4P*P=u8!!iNr_#Y;K~!g#COXXsF+LZ(rSl#^hkA~c!_mb1YcMX-8Kv?y4Ym9i|u'
        b'Ob?V=Ys;P0t@USw`1L3PFDZiH3-V3z#TiYb++ZU!*jY-g=IR~ZO#Mxi`iwY26g|%pQ*$OY)?_#+O|y~AMP!9&c^R`nG%I#`?Bz^P'
        b'dCOg*$`iknw|?P=4y$}p`7GONKXdgV-)zx^q1PYNf;@WtF&gRL$+Yv-%Ey|~tUNY4ZglIW|EIls_X~X6<81EXhINYSwz7`KIP-V3'
        b'nw1<qbFioNP*3flo`n(aW<EXN4{bFgwu;_spwD)sWOTBno(Y8vI#ZCxg&bq);W&C#Q(mZQthke&ETbor#)zR{p%^W8*7XRgp<XRj'
        b'm>4x!aOaK`cL;{6(Soxox!76V)0*KD3<Jdz#jAhkbAzr32MI;)2r<12HIY;)8G3X4Ov3rA{BC;2=!VAG-t$iHv-qWh@*Xb4UCnZA'
        b'bX1Y|yp1p=lcpSoPA|QZ(Xo$nEw5B7RlUsP{&C81dI(`b58ad2ak4tdoa~~4PLM_^onqA~i-WYf4jmg8Bn+IZHRi`$f@~@+*O*M1'
        b'Yb$hYg+{wiQm$NET&&5B8p4UEkJuS7ujv<_6Vq*1v~M*igT^r}CtH{GIG6R*=J(k1d)zUS>_f8)Z%~13t#Bhy)Ub^H`5LZuNslwH'
        b'r}l-OCWI&4EIN#1=hsgVF8rB>29Tj?y~L-c7Ld0hC;I35(Kib+Hk7>YI27ehW4I7o)cP79cR6kS!so%7a9U+rvUfcnc~K*(Txivl'
        b'E00=>HJfxID_g9o*O>iWchB%3Pigl>kARqH+%)X8?8Yca0pzL3b0el`gp(y2!!&x_uZ*Qu-EVm8C8ae=slB4ebD@vkv6n<&^m~`3'
        b'n>NyvL9%H~osIVPfAA$?s^^%1SU709AiNG(CL3`bLSQnp`YJEHEhd&(Z%{dL8dDNx%<<Y4#uBt2j_h$p_Si@F)Y(V7BP6-O{)vB_'
        b'F=PjGVncR_hc9Zx#sanug>|W#EnR2X9<+AzE^EWuwG~RwC15?pn!>9zBtw$$J8jeYF_eW2n}VhE#j!`3lGkm&iEK4u)z7zRa*J4W'
        b'%EEasYCIQpD9SjOrH|&JoN1g$kCPxmS@vsZs)8jgKepaJ<GgvM&TjO)u*ZdQL-d=AN=pk4__th(-n_nLd+XpCXFqH_pL_{@t$y8l'
        b'lc}KPYV^9Img?5O&NzRE(c;y=@eAn_H^p?hv7A{mifjGtjPo3f3YvO7e4?PwYei2hQW}R_rX|miXpB-WyhdXDo#$AkF-SO8Ak4!;'
        b'_Wb#bvjcAJ_Ty*haD0d)+F{ul89lyndQbp0{1Jw=7y~Ik``5O*fYu+*IFCbTPx58nadfVGgoM_@FnWQFWoGi*{<277IXYL9EiGne'
        b'T%wohpwDx=c};eZxBtFdM~#1DElPAE+Hyvxq~9;G(UEfRS!pwwk@yBn^RVWObMKkDEtBlkXN<hK<+4&KEpfE&IpeH@?!ypKa#d3G'
        b'l`)9xt~1UW=uKYT&sXIz>EjutLM&?}t^YdX+y?zPx=UN_D@*e!gKT&BHp)&vZoOPzkp1oKi9_f`dSzJ>RT|~p`t#LS%I9o*gq0=v'
        b'(4(w1bRt=O9s;svY>@1rNESpok`6$d3hRx$Y%THdMb+oGP>0=FEPc&FJyvG8R`m$8E$E%rb!VKb5d}S+Euda)l9k<bd>iEsWqgGF'
        b'QVxYU{YygY|KHJ8QN5P98m3Ck)cB~Lp_R&~Duwkl5Ggc*Wxh$IA~JUf-Ib-Bo+Ri@`wyLIaIk=_b4qI%)fgsyF>Rcy&zE1>6gI5J'
        b'x2lnc@qCsW)#T*s6CK}5jXn%U3r=XO(pgVZ+|{>yuJAR!?r(Su!h~~*=!puVe~=&GF#K@0@)P|l7n?_%;R5!J-{-$?ie+(d-Qp18'
        b'_-XH*vtG3P9zWxJ{ER*BOr7I><5_WvvT8g%#kOrjaJ_~L4)|)Hrez&<<T)xm(KClCZzw>sK=%j!NRLz^oExtH9Zppz?>(dOB8%}#'
        b'<QeCrGj&@>+wVW)?htoGQbsw^I_`|~A?V6I=j$o23{qZEopFwXwgLklNJ9Bdw2ku}$EY;Io22K|gJa`3jx9TUn+q#-tREXj?-W(~'
        b'Ors<G8Xvj5!1w`AERnf>^OR$Pc3Qv+K1K&$B5s+<1+8WXp|@h?kfqz?szkP$F%Lg;=inS|f5!}w{o|ISDN3Fu&jt^suSdJAx=LiK'
        b'o3=6Q<+g&R-}!K*=N%Pg^0X%JJ@rCe{nh2X<*M82w7XrjLH@VcQyZ?ioL8Vt5BsUb9jrR4q_K6t<-7#Fqr&}}kSx+@4^tyiMF}bF'
        b'UD406%l9o54k%6wuRt?Ho4{VOA~M%EJwGaF?8snrw_^7Oerzy1cJoA}E5H+fWz-ParQ7IWmX3vJ!$e1|M_g4GiOg}!HoZu1E0BfV'
        b'qUm2mPn@e_*cu=6_nz*AJ_jRQs*WD$H(sdYD7O}uv&B_cm22PSGCEOi1|;cZYqQJwEp!)q%B^ZFL(j_lGX{mY<WTDuF6TEee3>?q'
        b'K4?&qBS{)+(C5Md@bRcY$qy0IGP#B^_G7H&R<qs~Cj@nf_CLYGsZBPC%!|yG_zH(X(}YGpjh*&idbC$_N70HTwablvk@U5`=&WAj'
        b'W&S>>IE_(NC+N82ZF(GC>8&`%f863^-tdMB8-sdel0iD~OFPV0S%q_$Jwmrqav9x5)hTkPSE*V?dll9F-d=@H!dQg|a3fgySONWB'
        b'L$^<cvo)-0882IWt?7_we|}uz<3d~cn#=i5SKTK=?9aHWc8Wa}Am8PD6?#KG&z-1(8QatH^eK!+A)e@8@<Zz)m-A&92hkHP&#;<9'
        b'vwa>Q*2In!aMfa$GY>`?=x-pEg|I#kla`0kpmfuBJAzs71+P3)c!O?0zRd_y$$#Z(Qj$kf`7ga`5aNb=+9qQMNuM$Vd6vV=j{0VZ'
        b'J5+RHz<rIWjxxqG6aA_GLs{hXp(xdUl%#4oJ)08X&FQMY-%7JF!j-R8gTmIEUYWW-z^bN;r^UVL2BKQXY>yIHRxD!~$02Ez^KNdt'
        b'pS}f=(^qJ!>Fof>`DH?aeAv~$2yYoL6+R`X1;(d&+4yTR!!03tf6}n(H<YYXABy-usigaVtD`v9IFlaXVOg;Dowje7%Q?zrzusNv'
        b'I99bDZJ)ah4IgLKaADyPw}fRO@809HyzJN87Nv;l`&^@Ug?%VO-T0&1>F=uBR$>38yXsxk4alJ=Gar{z0^QA?y0LT-$rfZZp9)5G'
        b'PRNHIPE^ilLmxOWq{hqX#f&P8w=!sH0))HMdmu07`aMe7)1ZBSq{haeZ!r!sXtK<`-E_@Lm=gzsB8$;2>s9OBHAI$n%l7bk+2xyQ'
        b'IrIqBU5V0=)bxkvu4S}Q&TeOScWrmKeSbHVCsv6qY;sGe@qO=k?lhtQr*d4oaOo#%p%qc_^BxiR$X=+1RMS_u2N04NtXExRJaT)>'
        b'TXgo6R=$rBpnIP8Z2j9Jo%5Ku`iDAORWUOo(0scSsW=sw@<YIfo0AHUV8~)+42yzg>LJ{a2>(~t4&7W|7eF>2tedSX2?(#?{47(a'
        b'M_5g(7v-HPKA62Ii1V>53dvqHV%?TvdN#A3aU6_L)iYKmqQX?%a4N9*hx*pyS7vRAdn#^=>MzD&PvvGG@X1~z%U(2c#};!J4c=m('
        b'yS6Ahg*Xmo8kw7xADHZvbYV(^wya+>+eOcfWa8+|t7WQ=E(ZzgjAh+-AJFnMmv*;o7Or9R+(km0?jhxI_&4s(o?OajYr36lx@)c7'
        b'c5AolMX^OWQf4J}N*R4)#q;j0@P=)sc~!UYNUqrEW-KQdi{HHTW>S5k>YrjXYX79=GbXfujC!zjdAD<UckPO9dqKA<Pkd+Ju=gU&'
        b'5ihcOW05O2Fy<dLrYl7IeeExIqfCuoGw;3BEeQYBLn^1#4tBZ@1y;wkzR-R2yTxDqyjdpCm)mo?-QP1e_nPx)RD?HJ$O_?NS8mft'
        b'x|yInVAIG^Wn+WhW=ne;TyGVbTm>Ef{%b+^^@>t=QOASTVLrdp8<UNF^cO>)rcU0ym9fw5_Ph~Wc0_pmVX=@?q5$E=SW(m6H%41K'
        b'6K8eP6Yy%`%3$IBadTpK`SWW=jTM&rY1~=MDTdzgpYAy7r}~)57104>J!^lgd)-%6<;>l;j!E<+lO~UyzB?pF*DY+S5bOz-FknlR'
        b'Q%y${wOpqpb>I1^HZh9uZea)M^xb=fou5s=3HK1&I%?Q8L80dDop-jyTm7uf+WJ`cVJ11?&h^(N^=5nL9Wz~+M{`W*F!KkU!V{?0'
        b'P^$kOJ;m<d)OY7TA-`_n0z71re|OgE4jR0Fc#^P_De>*j=hi<UY(^CBrCkxCl|^vDmCLP7d5tT+eXbtb%XR)-@N-&;XPU>gC~)xx'
        b'fj`qjhYFh;X&(CLj+*!0)vkz5rQ7B7q@8LN>PdNExV7v^$nx@E?3cRS76!jn`2DL(CH%V0jJ>DJh~EocDl=m~+4bIqF3;=oy<P8}'
        b'@A6z^3O(x(G>Su@V{H^TYt5HJ`#!`~9k_Ofxvk5!BXCFcx;oWL2GY$AW?4IRy25wol|njNT%6?IzzBscD<FA?3`%bL7lGa@7}h`P'
        b'9nM|9i46J#C2MZ!67n}a<EoIzl2ZaHZ?rbA*~d1u^NUvr`(1@~2~yvP2EUi5_j%jt`7os-gm%(<nU=QJ{awxjU3HGF_AOoRSTTg|'
        b'{Zw~fmvb+4t2`~YMKR(Fb?|$RuFd5o`&xH*Id{SA6S~4&W~Xy26?D%>b>gP5fYzEW=XMx=iq3^*j6#etOwEu@K{1;~KKR-RRAz3x'
        b'BV`^utTrDI6)P$N$1#_jA)foZRiE;8iV=_*x_R}S`}(%e@y-RC$!l}o5GUqz*7zO}k4rS>-gw);@RIDh=z!Q^&nV6^8gD%AZ_V28'
        b'U)-i_W6(ev<|!4@?aVmE)j1qnoj5L#`oHvBx=QEXhA^aP)lTukOMZUF$>QW&l(%h*yxi+54>T8cdCz=!-g5Rc&*-|l_tw}Y?4-D}'
        b'-wW;(nI0{3Lf5_d-!GKIT3_gLzR*>>q{}|LOLf24ytqrK(rP*i$m?<%yK3{glIe8~cki0aXVQNa-@9M=>8>eC!RK^VX4iKW-l)oF'
        b'6w|tdZQ0?%LnUnbZi(WdE}^b^xTl|KeX7ejx2tw;m;J%6Dw)`L_`1hOnc+GY<f9;ole>f-idOi1q1xwX6VJ69DMCWT;Ywk5T$P=l'
        b'GpZ}`Q(70*lCis=;8<_%iVd8SB<xL0Ip~@cI5RdevI}}>XN3JFUqn*T&>qs|{wL#gFf}kHwo4yN%{7rE{i!RZ!tGC4jKIe}0yDQ*'
        b'3oi?|V>G$>tm{Gp;$zk2>B`4!+D!+x6_VB6e14N39j>G@<zJM{a5P0!J&E?BtGtQceCEGtzr@q3y0!<F?l75eb)wQO-7B|Mo2sTW'
        b'o+k)g6@i;K2o<!v$$AvE#it9b(A2@l_zQ^_c@i&zaDH64!@Q@HUYPqg=3cS%cSZ~Mg`}{G+ntpg?&XP6xR)f3wg1?uT0$G(yG9-d'
        b'hU`02ntydtR*3Z4_i8@XA!yQO!K-!WJC9ZS=KVBwvg*IJtN(|!dbaL6o%==Rzjf7Y?N6Q6Cn9E>PtneP=gj{fo>V>0Wd0_~d{J!P'
        b'-6<SlSm9^h(dil+__`AITt5Y_RdOTV_HUcIaV(i%9+Df%CO<%04|F;Ybk=^|X)o<m{V8&-39S9F^K~nI|6(2W*pKsD6P~qZv#<Fh'
        b'TDq_KRcq+<)|$-{hnjI@Gu1(V6?a~k;`&-%vQg-#_J%z&Mn;RiI(S=nwBv!GZ8AyU4paI}%IkGGw67`-stMS~s2*bK83+gC(6(}+'
        b'0n3$*7n@G;)j`!^)O&GtsNj43l)WEqg#|xhUCf*5?+7I^m16~#UtM}<p6;Da=R2LX?{?as=`{9;5;Hr6#jz>Oy+-0fdkrfz6ZL*|'
        b'-$l418BZ&HK;$mM@JBV<bLY^Uv`+7O^<;+nyQ0(idS~rFJMGgu-5sKPzMZ`1Tj3@6R~5nNHS6zqS@kAgBXK7)9@#YU(N6FDaSZJ<'
        b'G)f|Sg;Q&EnwB40jh#+oXKik${h?0xPolJg5j7IyeT*YA$Xwf|NbXz{#x{-fP6G*&M2Ya`ixP1gvhFE#FJX*ga%c5H!E9SStxt|@'
        b';u;^gLunsJv+96khr=C2J@jNCH_E1L;3V<|MXB<FmNIi_=i0TVaYeFAl6yDNe%PLIaIL2$Q#X!%c$&9bL<Yt@*f~Cy3lb_E8f6{h'
        b'!_pCsQO9_u*yx=v9(Tz<^E46;ROkZ|g?}gHDbMNz$IcHsSbtFUD({i)%_BXcM=@)@-r-RN-D#_zp)Iex(<$$)m3P|DceoFUTDG)~'
        b'?sP_U*52RQbe&H;-{HwvRRp8>jXHNIz1@OhNjqg^i{Pd3)>wLF{eM(_&lTh%<q1Y(Nauo*he58J=r?AF#(cS>euVJYidE8JZQvqI'
        b'6V}VpNW%pA-Y-Y&8sD&~PG+lU*i~UFTSQRC^qL)T552L9-tlvHAH_XRIn%M(%8j}!YyZ!_%g`>cky1^}A9Vc3d+@tDypORAV_Gy-'
        b'^maVq(L~OuVD8)n9<fThXIN`zhqJT8{&7d$Cx2AciRL({JBTa+aHhHjX9i`+^!4oO81mlOcI_nAC&s(X=t>HlIm08QiO0&OJCs4*'
        b'CS-jF7Y?SFRixJ!wB*=w8!~4VRp#7tMEls3ArN|O%yYYkdmM4%=fWu8XYhHA7G=nD<xE_oHD8k*vN4ZDlt=3t;__XS0~g0;t?EGb'
        b'TeBC(YRkv3(_o1G2QjbiP&W$Q_t<@6K@M^`0_8hQ;2nqnwogp%bEKreJG{<;Ol1s2ZvU@DgpA$DHg)s=kHkU$H2=Tj&xJe}%O?N8'
        b'BjruUc+dS(%A=VrQxt*i>O1==&IK#89`EqH733ZuEgJV(<f*_yhHP0{_Q)C^qo22)*RULWE_nFZ&1}^fUUM*n+M1${^q&1~G0<_V'
        b'i&u^hy2l5KX&s*H@q;Rx?^VE*4sM*cBGJ3+ggf%hAsu&Q8v8gJA@@bH^f%E`h+4I6F0HpW&k&^>i2F1x_C`P2;+!J7I(n~QV}$!>'
        b'Vt$}Q=NBFu=f?$eeoKpr-tcqf1<nr&G27cR%c=9Sab)Z$NtrTec}2Ee+HpXv`kuTONTaA5;*ns6#B6L^JXMfgIMLV*5J6Q8W0!QO'
        b'u9DnfI^C*@pqJkp@8@HNb$G;w`DI$!RFS)nzxZ@(Y=?7FhrPeOu4=P;jcD1;cG}I3C5A&({xm#Cj3ekvzFzq`*}MKGV@0apd3uRq'
        b'REJa5Vef6P`{X`%ktpVTyD&{-?C`db@;bR{EWI=6Pp^hM@#dX7_<!MZ#}8|jbvQ?M)Q;@1|IqGUDT?{I-8<cM%G<vr{?aboWG3tw'
        b'4-i)E{-eK562z?%htfv3AGj~jL2%-C?H);P)$PRN?a3<dDy&Nt__R{+O07|AX!d_Y)@2L3kLDb0ucrKNm29i0{Jve{dOC2&Jo|xm'
        b'*Sx?3K2Ps(?<FV#PZPn7C`BXWV=@+HnhIL1Sv%VoSCqb0wDXiV7-Qg^n6||<q8XCB#*D-BCx_fKX>4CSkE8F9JumTUz7_bi(81I3'
        b'MuuPdh=GzI)$QAJ_O=T$W7Ze#7lZCqlw={fvP*rQ%!H8Wo^Z3NfhP)6yZPOAVVEl%hnT)^XzRgtXG42!WBclA&*p7Gz*YOnqZ;Uk'
        b'Wb7Vc2|)!xTPL^)ND{JhhM#d3|KCC8iEW;};9|k0$A@u})jv_e@A929DtYa~q$?*e?gxj_d%>z3JtAYw@29EMxSo17B(LeYDXfo*'
        b'WaMvri}7Z{yuhcQ@?_ZIi1#z+H7v+?(U-SObDp7nMz+!?)oNO^afVP_Tkka0$h25NT-F_oYg8;~7pkpRD8M+@wIwiGXs|NBklU(E'
        b'RUZ&;1h}t>2uot*Uby$XphC@mdu<hED?`-HT=3Y*%%hTLL`{F(N$bRRul!I$((4Ggk51n<Q10{gXhnfByG{$9puUX_9@d)G?#ynl'
        b'&2G1kYB$aiSt3WY)VDs{?tG@b_Stqi#basa%OW{tWQb+ah_Rz~rk7t=9;6RwyiXjFAra*^YeVrX+YiRbg=C7nd@6EH2}BjMZ80f='
        b'+FkTTVUy}@!Ue5v_skh3ioEeuZ6UHterd`PEkCvz+MQF|Yp1r`ue7;SMCcpJ8%?pV<c?UX9rdC&{ndeH)9D>nfhEVjAJ7`t?ws6S'
        b'8`qwEiO<N7YusqO+l3SdZnnl;ZbOb`WKXfKdH;cRY3L5t67xXY-7ZAnvpjOQ4@v!;#<<Etw@207J)a(Ps?FQKmJ{z|XU__3Q!X5n'
        b'sLZ}M{3sWOA7$f5gjbX;9&u0KDr`<r`x&dfYuYl%i(I>tYp)&JZvU#y9Vg2Ax{c1Ds>-}YJtz4zE$z1icY+`{_a=Lf3q1N<D5Mf$'
        b'f^u%<Bu~}T?~xl%-}cT=_fsG3L|DEnA^+30$Jfd-*+J2N8|nPKFYC^|Ck6=*A4)i}<_8*}Vd`8uUHgHMN&nMvfT8J6FF#Vb_{TQq'
        b'k8QO-wb{*W#s@?tyIW7TIa}Lme`up?&@pCj<|5bAPB3LQ;l@hIT-w7-6MmI*O{M~2v|g4ycT6bTgc@2`Qq_8>&Dqdad#Ek>7yh1z'
        b'w5n~hhdI*U@)ZjF1!8`!t=d!I+XR_myPu~D+m}%0K#`kvn2d`c4hDG(_wQ{~sNp20zZIpL3ev5FZfILqB)jk*GJW@{jK;gOWb^Bz'
        b'N}{-+adgMYTI7f)^AXAp+JM$IM%d@J(YtxQlRjZT*EhPGZ{Ka747O11o}sP(Xmgge*~{7%e&r4o&3UBFGqzAIBUR7x<wq^!Ln_$f'
        b'pvV2S^>Z|fL$v#5sb7yfx-r|!@2`9KT}zXs&H=xdJ+Lkc!=}Fxb6i`>AtCwG1%5Yx-?s+p1%CI`(5j~(omRbhm){d3+Jq6&^Ta)$'
        b'&mSL>5%j44@)5atN7ELEJh$oZ`Qt~(Mxx78zp~)q#(WY{ma1$}F7kD)4qR+ijHD4*v1q(?&8BhdUa9dlK1Ix<+H?nn2xx`;kMlzl'
        b'IAw=-{O&MS%_7fz?&oFLBM4aaDiQ8<;Ml~Fwny1Ur?k!);&6t>Wofb`?owjS;)Y$F)0|kF(q>O-8y8s2xVq%-?{9Ax&q~S-8n<(%'
        b'YADGK8>3%D5?!Z-{S?LG#KF^^6Tufx3$1X~Y=prD`CQ<0{RdigZBAWVt**^}>a>ax31@33w+WXGFCa0K+6<B8;?}I#Hu?tSV`Pq|'
        b'4Knj%#2nMss%d-P&#7t4dZ_JpaYO*OV}XzH!maJ18rJ>1NB%+%YqA;T3u5i0P+fLvQUe#H-4mdQY@78J-4g_Fkn8jJh`FHoyZdK-'
        b'rHE)t7Vf%fy}!+Qf1CaOwmSPV)m2uQE2|ph6@hJPc0U~6&6IIjN@PkAGDXOe;5K_OvZRwOW_oN))z`P-VmsT?)+%jtO55!I@Ncy0'
        b'vUkY|;Y?WTW<+nW^ksF<&oVQrC0KQpcmK&d8pZk9BrbbF{__@hG%49?VWTuQakN!#F+|<Dm(U`o)%(V2=grgh{?m2#4aVQuWxt%}'
        b'*lORgVTw3rMqshx+@dhmT)vadY?6-|&m3bNW9jwLs$XvjH{Eoy$0Yc42i&F?716e~<Fwjy!$Hf2#J1BJ;&I{yqWk)kN|8ZH)S6kS'
        b'(y9lE)go+SMV!XweQ(WPyK2pzq1B?|pmBx+61SSH{)6wa5irFu@quAf&K%&=U%%e^!)fOar|m~i*KIlG?qNN1(}@kI)nd+9kl~h('
        b'5UDjQSjFDcwCJni2(mAx`SgqamPoQ@3VnLWJwOH4>_x;qi*P=QPfs87sb&u_#_-#+*KeqqYQ@G&fojEywDjdc?k{g!MQ`}8`I4=='
        b'#9NuyM7bHP&)>)=dF<*WlB;8rpCq58uuap*#=ILyN12T&74o)D>0=E%=G*D_Wj(m4otM3SZG{Dax_n7Kl6#(AeTH9=-ApGweO_-l'
        b'-~%2#&!>;S(pq`i`7x6A^y(1wzMMZ7@wR_z$@=AAFvt8Gnx(RZ64=y3Mx!$3EQfoPC-)}QXLtG@^Z9ab4XgT*-#L>T);a8$?}1?m'
        b'`wZXlbnEKVPV4D9#~6Fz>8kJ9!gHBcDI%F?5%x?cf6bGYAI(coTfL9pg_brK&B;5RxwpZgBE}iFY2L@(k+0X?5KaxN1M6d4EKxHX'
        b'PyFVyho9w81(K%S{21%Rb5?fsex9q?6v`%7^N1cdsy@(@EBmrLerwG;?aW0AU-9Xn4JUG=@PcW%G~W=_R4J@N{w!bmt$gWMCM2|('
        b'Z`#CDD<jXJMp6FA`fRwjR`uj*XZmS-%IUhT4;mZUm`6@~JD@O9BU0ysy}Wf}ouxRa@LI8^*ueQ!D82Uq(RC=lV#D3LYl6zv#laPk'
        b'<?6Umaq4kX|8oNOj-7JRI!o@5`>clY(2C%=amA5xLJWno#6-?W;xGTf^L;?WXhOD+mc%cNB!>P#qR%<0)e}9*Ed1Azgsa&{5_GVe'
        b'y6s4U3+j`<YW4C9TK#^_k%T>fI`&9H(oWC?TK!glj`<@%O8~!6oxULENCF{JBAq}CJm1aZ@75ytXN6z<pFFRRhT9^oUI*IoyH;O$'
        b'5q|VBnLj+9E#(Q%?}xo!fc&V{@9EO&H^A+RxmrDa3xekp=%x(5d7f4uk9hRMUdSg$5-uPOdlX24l#t^YTD=}|sn68vO;2g{QFCb='
        b'O?qOYQ6VP!k6%gE{K^Y(p9z0RRKX0oDBg$f5)F-iA729f2>4Z?B>ImKhi$;8!1usK;Ltea>rAmB3URrbKn#=g#IPSoMIT%EATcae'
        b'6T^n5wfZFw5JL{)Q2=#6^iEAAhJr0xy-OoD6uhR@r$R3iAn@ln;<^*i<6DQ(CmBNwp;4fOFdGowO?+p7s*!g~5N0WGpT8tNgq6gf'
        b'Lfm}|3Au`N9;f-|M@Tbh4${#;zmW?K2(twKHNgKB&=1|I)k{Cq>QjP<UY2tt!6uT#|G4N#f*4r%H?2Ms{=Nusla3@<p;rLBhVNp~'
        b'Rlo+|ZG4x2nt(!}_b7NFnCMrvBaJy){Y@G+^zE>h2me>b_YF_D*(a*PcMUKUdQG6mfKu4|3G^&5E<zIjJLn)Ff}KEM1<Xf*%EKk`'
        b'@rd&T#4#FFx>&1kK>mgxo_?^C2YsoI7<%J~p#{ik0>2@Bg~<0>xStDqMP1=j=}Wr>;J>90BfWqgc4p_%@+X<d@=W4lGw-OuJ0u?F'
        b'<mqgd>^USR6Jr>#3I2xTe;;2De`kv&@jQQ<p9??ApV8`hp1Dd$4h@D(f>{KRO2dMA$aG?;r1k**8=kLB2G68`XYidj1H6<%%iZ)%'
        b'A>6p2*9&w2)j;Y@@DQ*En6TtX!qV+X8~oh>yGOr~#D^kJ3Qz{M`0j`OKHzs?5A5xK9DD>MWuacoh8p$61r)@J4X3UXg9&-L5b7mB'
        b'-VVl~{*p071M<H!hCJBcISVr6B(Wg}<{68S=PzmXc`u-ic!x2R!z^?McoTF#kOceUK7;|iLbMr`*;@Uo=e7Fk`x!&j6Q~P_L-Z1w'
        b'->)adfbz5fz|Wg<NjwRb#9u}Hqa{%52=N1DY&>s5Iw!!tc-Yrdz+UKl)Cs@^<N?QDmc;u(Uk7tFs2c5(AJR_5Qhn%4M-nE%eF&%x'
        b'W~+d8K+B5={|fJIvi`)Fp6Hjr{VG8E5{;uNVSj)m{v_<l6D0BF@FNG{V74TO7-rLNw4Zv=+}zxR58&rXltFH8`PA6h?;xEKQVzeE'
        b'KFUcAD^WWQU<<+^PRCkWT8_g$zQ8M}xP<OPfCEA$2ce0j3ULdy!>^pq|9P9&As(W?kRKb%NweUVJc*_jaffgtg>{A@{2w=Y!mxzD'
        b'Ei8d1?4o%sWyn&5(+~F@z`N(JBDwUo71Lv@@I7*GYrX%^TON5isA$R|_}c({&)?+v1LyhuQ13zd+J_&}Hw)#q2X$!DL13zDq$ED&'
        b'MXIOQx4_OS<oQY1uSdRb1)oF+dFY#jw12a(nyTfACux}w38{C2mk$sF_cbwGr0T=q8<`}20^I0mdBN`$pn9ML<!=Szp^k$70j<x&'
        b'z~`Y8ljhz~4AK8<$N0y#qRn1~{@`X5(WCv;Pf!t>$B(`oBzolG>+c}1Z2BO?QCUO77m)_E3!lQj8p;zuAN;MTs2Jt{b0oE!SO~oh'
        b'Kx>C2em~4yP&Wg+XqsL=l2D5H+=P1JAH;AKG~{>m0~d+G?>Azw0y>}rK-a}ryt?sCJ={cuf`?EKGN6tJ))^F!{>iUQ0KR#+G5^Vy'
        b'tHe-}e<Wc&Pz>`&Vc!7!v4-a_Ocom^pe{8dE?=V`PlEo-z$-fuKhQ70r;E^jW)h$Hzx(^dzjZ(QUtkX>iO+@p*?LKQ+N(zr<^W&A'
        b'{$aGIsZgH?^R&m!&^rWmJ?eQ2)U-Zs{S5t|w|)5mdP7D@;;Ug^5XKnvfHj2Z=Rj{J!ihrNSpfAz@Jl1|)Zu6G9fNS5NBA#8P2a>@'
        b'3HlB&5_WV5uMFxRK`THnAYE0UwZIp^0pJAH2YP|Yu=g1-1(*&z1!RSJ`i%{sTYzey4)_vyY^o%_5%gOi+$o7~1w9EEfLXv#Ko`&p'
        b'{0jU6Tm}f@T>GjdUIM!DN%S2^+c2o_1EOd@6v7zBfyM%pffOJbNCKW6;uGJ9vN(=1$iR0Y#~3n!@&L4{K++J#FbPOO-p>Y-fahTE'
        b'MW6t96IcyMgBimf<VOHtL!EgCdK-X4P=5ew2et#B0($`UETk9tuovpDfNy|rfn&f);1tjSoB_@OzX5%~0B{|69p!xsl!YJcQ0Reg'
        b'E&;yyrfnc?|F(f2IDCJF??6x)5Dv%z74QHM4NL-bKs=BL_`|;-AQ|eJz!ShzKnCy(kPR4tJRk;q@dD^efbV^h_+_9gfR(^oz*^uv'
        b'V3Yb`rV`WvR0I2fZ-8dtIB*g;1#|!|pcnWB=mQ3TTL1(9eSiQ!3aEgGfGEoQK0fh}Ld_vQvq0wp>A=&#3qT>T3fKUA0Bi+z1BXyQ'
        b'u7jQey$F;HV+;wXA5Q>J1Am8qNkA^tF98ct{{IBc09^&T23QNs$9Ea%P3jN$$M0dWp;^ipLO|mIH6RUV47(y2LkILzgBU|$AY<49'
        b'HznY&?VtyN6TtD&R7M$X>W2CpFc*G51^f>6C14P^1x!R85yS2fU>G0;MgV%)9R(TzD1kA+1Aqq50guu42$(5^bA^8rbS|&}coxV3'
        b'_5*nUnqHfpCAJr#eg$|9coVPy3>BJ)lB|Jx9kokB$h)BHfePRw+CBiaKs@541115{z(imIu;Cv^67~x55Cs0)Lgxr!>n6-fUZrjS'
        b'Qo{+z3LBO~hC&_^+F3#bxj_AcyiyKY3bPP^KgjdH!mmrfHDDC@f(1Ar1o%^kW7f3$px%J~pd1(j^>JWK03pfL?ns^fbI@3P&jI}a'
        b'NQBw~ItP?{3H${0RfO9QgrE=I4;ezi5kV$;0}!K~C1`_m8K~#WJ#BW!e8vzloiS7*4NK-RhOM9_FjGuM8aLe#4IUSfu{T6yNjmI6'
        b'-?d&$dS5_01a$+D^de&z{nl@DY)~HpngQDi$T>hNa0up)?f@SnuTBD)zd}mESnF8J?8l@qv!XwOyzoe7K4WNs{jGrbHS~#~dvxIC'
        b'b&P@F+lui(DeSgD#w>k{F>F}L7^>HRpJBEKc6HFR1``r(WegXf51GZ#3_F~eF_c2D6855ih&YtrQnZEes~V8wdl%J*zvcMe4>j?}'
        b'Sg?dKtbu=huq%C=G1Mb2V#pqH>JRkdfG2=l;Lv);V1xZPp%xcG27eRdN)!AA%>Whx^+3xTNFQh>kOM@#N%_c@@Yulz;~+cfB9_5l'
        b'AQgBSK=zY$%RGJTSD>c>-+a^^U@DLWya{Xpz6CA<!LOh$0WSlafFz_Z8le61dVEiUT8DPS2aFJkxaI&Mz+zxF5WgFF1{wiKffPUv'
        b'OahXCD4IUtdB6{N0jP(Yq@`ND1Zr*<W9a=1en9UKXbQrc3*>D=-vsl@-+2BY@-=i7_#EH6HllB7DM3CoPi=6&nUWbN$jejquSZ>g'
        b'c`0y5&L+eM(ySj@c!V*OKtK9Dq!kE(UzPY?LhT+#|499YKXTB_M<B<8CdFg?gYw(og0ecs7;XaA@4+X>F*X63fhgFU0OXZJHUeHj'
        b'ob!QHxJzk8J%QQr9~naq{Qe2%6COR1u!7nL)KK?AuMp}}pmgpb=Nw~Lg6~N*d>{vQQYz5iLu~?f;X4)IF9Vst&1S8BLJP)L-vT%J'
        b'mE`8|r2tsD?@0^HBey_Cz~>IAcL6h?J_0%u^epHTpuw9Z@lS$I1x*Dl0G$ik0J;#g1N3#!YoLXokADF94)i(DcR;P68$h>!ZU)_0'
        b'iFV6@_8;HvKoitY1QK!zvhm0*v`nP>Q;?TA(uZ+L-%6S<i1P}JMCAHPk4#pHxDADx7xk@7=|i61e2An}3geCyD{dlR(Jqyvts*z+'
        b'iFv8~_%A~JmBXLRS+G}$Fw;O!gRTHQ2f7FJXQ0$U{XvAl&)4xCtrHu9(B{cMgiMBdoCUQ3YB}u9A4-VpHVuEc-Vgc8A&*~%nF(g^'
        b'gXY2QQP3KEp9Y<RL`?dXF?2!g{}JjY&;-34(958eAJH@sQzxZx6EcL5vA|YDhy561AJB=Qr$Ju?MVOf{KwbASjk8?pNBV}p4?YP+'
        b'nkS=8JOlj%P=6cB6f_QW9%vruv!I(mb3vOx-vsTq3HdKo+rdK!|BVrZjDtE8>Jq5aKtBb27J7+LUqoJLKpUVJM9XvpJx~Xk9`rZZ'
        b'X+-{Xf?me=_n=Z4Ath8FcnE4LyG=lu?|;<8|J84y-T|~Mso4fv4}q=FtA`z$wnLz+;HGjsYght0VJ+&InPf(TUWFMki87@}wfbE}'
        b'TK$;SXn)>;e?Sz}6JbXU$O)Gj3drG(|MNT_3ODHCGYP@?llLVXCbEXY39MnyzqR@c2qW{cBMEN;;;mGk$5@WmyLZtK55LXdJW2cX'
        b'1Pn?UlJakqIqZz7Li|AY0hfW}k>KZWqPM|q6lmx-T74hNdp7)7it>#fLN7?*`3?A92y9r7c7W1NX!n6q)Z-`c{UneE6g<fqdY@n^'
        b'Pm}m^v`zR9ebV#2AKy32g?S?~sY<95WWr{&ZNMZz3rq(l9MS4SD$pha98DXL2X(_?&phh?_4fkYHUqQa_Y%;TfSrII<JS(*O*Blz'
        b'?NFyypL#&6-wFhNf;Iz~2AE_zec^tj|0MGED;ky`o!9bXg!u-Jlp-E3_#+LVZ3p@UlMw8x^DX&eDb1%Lewng(6P=Kdk^sNVn|$m='
        b'a1w1EQfL!V3O5;PtYHIaIlwJs4Mv390Bi$32R1Cz>Q7;uy?-O(2RqI0YxU7kPg+Vct(&y^lOH2*GTF=m@C2QJSxUs9AEPZ1XRb8y'
        b'yqJCuCp^g%lXxq&vxZj-c0MEg%By@R)KchA0(4Nv3ueA>pGWwFt31(*$lMilPLBVWl?&<nnx_mz$f0H1(9Qt=0`>!k0X2AR1M+2F'
        b'APFshjFxSKh>+X-0L&&-V|)OlmLeYS^8BP6*1%up`JG6Y-Y}e0gWCS3)$f73mJjH>mWT|;;Ga-KI*)x@M09YU2h0N&0!b>OUs#~k'
        b'i;=6Y62y~Ar}*Z+m&Cv8yMp*VMrVe&%m{!3qG)|Weigy(@4)B4euQ@%;r$HtLEt#P4*}BeX?@{u4yW^#!%=N`5%Q6tJRrI%#IKJ|'
        b'RZ<zbk0&O6v`d&D?-u_<tG@{M8E{XKuk3cj7l;II!d*YiE+U`krGoruLS20$PC$5--~k}wGn99oR$sqct2e>TUf^FqDg2!P^KYRx'
        b'LarRQgT~LvcdXUwT@UH>R{`{j-|#$S1$p1c@SAY(cQWj~M&;0d&~i*@h=Lz;QMV^7*XnygO>eUX1I*_G(J-3;H*<wHhNL1}Q%ez#'
        b'CD6|SW&=q;Jg|`Z15~$b^)0}de_`whUYP(o6^H;zP`3(Trv%tj4PM=j@`ZjXP!DVeE`USSk%W8(b)kglcf!sp;DVn{-!ep}ulCjH'
        b'b^bd2A@D}jr&_%{8m-^EH{R(Bc3Z#y_y$p<OeX*?J(t-5Tm&uvSAl*&UrERYgfAV7{!60M`@zr3H&L$;o{Po>-vx1EgAH~nY1)wf'
        b'jBrR|$gk)=t$r@TzChO=w$QNACIb%G)4|>axG&y`{t-CN|2ttSXi^%&Qu@UI18Om-9d<V$UkXuQA;#%<RZ`yZF3Q+Ym6EjjB=}{6'
        b'{rYm&uoQ7C|4XaSc@5={xY0Q!SD{v44fD#CTK!HS8vfMay9qb}xPYsGv_=wtAMgNhlMdRzw3BN*b3SzLp%?j)g6|DLIR(BeDWLuh'
        b'NTTL|_ESmxY9K0+%WMIagZh8wncvFWC5aymwF+1Wd;&ZS%muQ5rNBy{6#W`aQ|WH-1>9IGSi>36rTErC-2qrlTK!eZM@WA?&HE3J'
        b'B;0?0m#{*x@GQ#PqSeO()j$$m|AP5Tdl1%#tYJUZhZ{ZgB6hNd6wqoG<%=?2B}Tphv!Ry?5V&O_16+XKu2*SW&SsKQCX*k1lP9I<'
        b'Q&Uk6rGyM`p!3YUDB`drzQB(7Y}M);X2B2i83pJMPL0s%e`v;7`-mi71Z0Hh^h=;00`)6^{5zqK-8~*^J@72h3_FM5$AqJ(UqBLg'
        b'A_BO{{{<fSK0!Z4Y$%1j;V}Ci)D5&C?AR8J*@2Vra|OP$ppHEx{i-97=ud*zPQp*Q1G01#=$0c1p@0-Hy@NOd(NMdPM{3Xv)aQjj'
        b'64Y1Wj}CNaza;+A?=Q!Tk3qJ^_asmTGFo{A(FcHvs4NFa0SPb^$O>J}#KYc3zzE#_gXc#<e{Lgdm<>Ntfu*xio}e8t4~3jTfQ4uW'
        b'4#7?|Xa>v{0>5EAv?G;}!YbNN@HZAB+&rKFsH=ml`y<ACz=Oa^AOWZWN<T#V_>oq>5$cjkt^Q5W9ID=|)z1NS0;B|W9bsI9`qQ7$'
        b'_xyx@^%&yNEc9iG3r8U=V1Job|LG}7{4YQ!a1Gcx8gT%?734xW+DPPeDeCl6VAVvFH?Sg1r{7b7w&9i}z61L8z}DFw+3@yhw54s5'
        b'_&LBTq|FMLfLwg902Tvzk0Y<_ko`IkUOVCrn1BKx4=AVKpMn=Z<M}0XAnyQ6fnCt=1ES$>=Tm4ifKiedy7+OBn6wT2N?*d^%Y+`Y'
        b'Sw{5L2zMvV-#$@h1oA$lOA_DTiTng+zYF;R(1+^uq3_bQV!gcKENeL4&l>y&SVKIp6v#Nk8YaQc&R*8Q5T5S`Z|#Tr6aW!p<!xX#'
        b'%#$#V*#Q4fBD}-99q$!etya=U$dVwU&w+jp#yXQg<xe1fa~QHdYDQT<z5}`;pZ|*V0wF*izO6u>3wl6Q59A790uT*M0;U1wE?U?A'
        b'#Mr9={1c5j?MiqqH#e6)hZO>IagS%tz63HtJ>=RBphStf15AQ?3C3|Y&;pnjl%k#>4;p}UxI2zC6d=DBK)na*gTOOTF9phgdVKf&'
        b'#q)1M{T|Sdv~2}F1Z+JEnd0pK9q*GcOLe1taC_pH37Q8y4=nNO(R_Ik>fvMQ%-V3$TTkWVKDtNXHhRB=tf?<A+P3CI!tUnGb?UWE'
        b'2{&H*I5jxwhlJ8|ki)2d=cxTC<Vgfw!M=$c(dQtosYtsOv=C|Yo%UeklI#BD1>k_s3vo{#zQwPUzYur2uxUZ!Px&P4@~G!VKk$S5'
        b'XVU{e?T39Dr=Q?=Cd!(I5%<nn9Tm&yAUzu4(R~c}q;Dx*ltkI2PDT7p1bjr-%QMcS4geV!ke2}6gFyFEO!MZC6?$UuK>shE^$_j~'
        b'Yq($*8R#0431hU2zoBpG=XpBEN7pB%7m>Gs^mpX-@1Fdn{^+6J{|D;GA08Qzwx4uer{xdNxSXzkQ%V<^g~d~1N;rCH#xfzw7+`^}'
        b'JT-g<osap3t|hiX-GDrx`x@vv8T40Dr=In*YYB7>4QPP+n-hxIm4&BSJ%I0DVD`&5M3^IxHux?Ki5>HaJ^s!*o4!wo18S=&1GEd_'
        b'j)D43LML&BHBTWdDle?0@dcR$P}#xhks(YCP(OYJdcLqn*CYS6W5;83-EwKw#mSHCs81ji#58N!p$PKR?q^7bCrmkAFE#x2)MN8B'
        b'OCFPKS@+o97uz4(Tro;mi+ob|YJ%<Hhm%uaH<jAQH{48(-=T{oL^d_k;22u+^*0ZP=Eo!uVD?urvBQ4t{CwW-wYsc;$zRd+MEZu?'
        b'9#*(#lndvMR;5RA4}fGv)sDXsQQ~k)Ig$CnEA)*xr}P=RdF+6sMy#3(TQ%bFSk<#pvy{1u&R1<xn@3;ag4V9(L?%s9G~G8J6LDqA'
        b'4x6Q@q?sPV_*mUClhXIqTo5<hDZ5fDyJ8=CWgNr(y{}ttmR<Reci%#;yca@WB(bQa>Y%bA&1$7-t+>=0EmzA6e<`)nce{i~xTxKL'
        b'D^|af>T<ua6@KNR+6vK(jQjemd8_Zdho+ERv5T%)lrb~~%HhIYG&wGoRPB*lY=qO;)ayO_3mtOv%|Uu;TA0h9D6S52L#tWtv13EI'
        b'znQO4ea^3#_3qcRh$A$Kq(o=U_q{sygpEj@@&iM;F!#&hm9JYEQZKe7iLHk34izU^v*E8LDa36JSBk}k&zPA?E|e3?Q`S%P-l0%u'
        b'W8lNA#+m^43*nV(>sgLdtqxbRV#{aDS|vA%^OF~^r*|<HUbPtLtJlK07UNCf!9n3|Us;`h;*r6a<AWmc!<I-nN&R(x=zVF6<Yl%T'
        b'OXU6Y_t9<oX|`eWL;dW{gK3NIulg<u`ehJlL-nNC9$+PYZNcJ))5OhEGCnm;TzEZo^ZGeo4U*%(Iu8t@wAo@&#Sf|%N65xY%=-o#'
        b'Bjv@H%=LqHk)s`v_Z2(bH=_(unkCotGsF$60u3T{X_C~GBsWY|*9G}-Q=`8E1MPZvy>Ny6#Sku--bRsI&L(&9TvbyWPjm*2NdDZS'
        b'0G-3Rb&%eA>k^TeErW5FVjP2U4xc;w@g24Z^T)ItD%VDo$m`_hVxdrmR4jhm-@bOR+`nZ;F>>TX|LW({*Yd^mp%uZMF8k(FF=d0C'
        b'wYF@qM$~8@^`YOZ#l<Hgr(2r&z4x)J?<Yrp=ov~*u;QOTdfBB5Tw8S98faQ;vSj;MSh2>&YeS9P&{>T_0nZ74)L-T=vCgb#iw)Mr'
        b'-!)ncA*vU`t!#;ZaU}Q4rt&Gxubg>p@KkmkD{eTP#QD45;LOHBn@zlH3iIA8gATQ&bcZy0huo28Nyd0ebMO@1&P)m~YYbwPx#lxw'
        b'3S|(HT(>@2UU26PZjFtyXPhD~rfTJc?aaE`8YV7~3sOx}+alM;JU(du`=BM#B9|8|En{p}Dc$L}$l~SIISU54k=Y}p)HGMV?8(9G'
        b'dD3IPoDVn3;!EmB78|Y4asI`sfOV$rMXgT`T1H6qI|7eer8amnPioziJx#pt;o^C@9}E}vB_ngzmRQu{y?MhAh-)MjOk);<0&5N|'
        b'XTo#yzg6e1-o}m1pC{!)mpwWdf77IlF7xH!2j{nGKQr6URNPQ(+_Yb8)(p0=s8Q3bz6Zp`D(lD^N%6zh=fZP~=XpGg(B*#{(HyvD'
        b'<2Q=nLC#mHB>6`1@}QV}r3k*|8-4PXq&ny|Req4)_J<MPinR3UM0JjR!~eB;G-B{VogJQ=e&WtqBy-r{f4u=<A310qIrtxUkp>SI'
        b'-Y|y@-Z}3Tb7g=FP)0^_*XdJw0nS?ktv3g10;+5(Yf%h0sPG?*wmLX}(_8dl|MoPxsnKx2-&m~@&Zua%l4$QkDBf~#L=m(Z?o%u('
        b'e5e002K9YHc*#s9LzGG4|D$b?rLhJZne*3x-c(>J4@?yvA}RZflnT#|)QAj+=rhQ<Nga32FMdB@Vdaj<$hyd=k$HiQN|EvFD5#;M'
        b'+7N|tlRBuGZD<r%eGt`j<IX)AodZa6%;^D3Br)x1u-L9|s}DAxqMF-9T$uT%0dF3~oEQKTY9a}JuKb2@FJ8>2aAg5^Zdx%)YL~l1'
        b'qQf_Hp{3y6=z=l+J_pzurt10wp6h4GWQM642tVL&KRCbzyA|??5-wnt-P}z5=K{DSnk6&l#4&L(afww96|&qm&}u`L8;e!wFTNN!'
        b'FuZ50U+3_e;i}Crh5k1xPD~H}A{(lFRk=x*=GX=}UvtgCdu0QUOJ4Nlc60YFJukmxk8(sM*V&E)#O@7y+z~aM+y8CYw7R3$jt$#&'
        b'tf(<(=9t&D*S9wMlhS?i8b3=`a9LK!i7ct-E>p9e#&78kdFEI0ONyW#MWAqRX^2G;{D%LF0fs}p>7wi0B!^S}n)&(nX4vCu<D7A='
        b's)0!Ei}$hzoa+W!*9|!AQ4u$|(9Bom2G#U{+@3@IUpzR}aH#Khk^VxFOJ5+H#Mq{p3}Q0<fouqXB*jk8XpKud+#9ewecMfLsQsS<'
        b'2ZlCoB}Sj9nDhaA`hX$wK5m3zQKb8&DEmJKjPFEgSdv&UpgH(Uw6Q2AADpX+99_d^C(*)EBn{L^lu9L7MJXo2BVHF4c*9AO9{)qC'
        b'e?oW#W<gWWo%b{31$R3hvu5DE=mCp5*`7IIvP#wj(TfPSj}yGv9_P6iqS|mwlrlxTL1*xnYjYlOG)m3$Xto)Y;B5K)?2(Fb1C3F>'
        b'b;>A*GE((^lt<xS9Ccq`)k&T{ZICD*sEa}|MH<&fc@(PWqu|^U<u`kkDM^~U>Idp;BK5WDFB+zWB@x#Y{sU{q(Z^lXmx!NUE`LvW'
        b'(9?6ZnNs@R0|TW>sbEmsbk%!@N?DM<W{WGjLOSM`F%I}~*?g^kTVxEawO5J1-eh{O>_`I_2BtQd#HCZ#uUS9T8dT;Wn?k3oi5orU'
        b'Y6=`x?T-}F5Ah@>Xdv1u6&%(!_3^0p+R(t5EB)H?pK4gMOo;C#p2VE(*F=VzgXuS|KeShi>4IK_dH5Z@UwHbKrp6vJp#@S3eaD!g'
        b'Mw&T3@sXNDITx%+93Ru(AI#236<v>E2c%?HYUK4-$vk=BcoOq#w7yrwrs!(rWc-|){i(v+MnwPXoa_C1eJ@E0^ytLZCSK{+IrXv9'
        b'I476GiQ)n+%H%PT@-eZ`jR}?_$;HdKX$urh62gTf|HhllRAXM#b>3tVTe5r&S#0^TIp_OJO=4+vptUwUHdW{<I0+Y4TD4xfnX#Yg'
        b'_jExuj3q0e${kf5*eT&A)Hx>@A64Z}edoSDQxWy^AGG6}Y$jPh^+($ZG>OtQAL2H%jx5T3vT42s8>2Tw=i5lyVczvtV5-%0To)*F'
        b'uw{&N=ZqBDl%(n$ce*}BR_7p7l2Sr!Hn8m84T%`~>Ss#zn~F;H1!ZIC9azy7rp6(p#8JKA$Q)Z$l6!`}d5-N%dBaY5RYhdEY)Y{M'
        b'GKJW<H8TC-Ym|2k3`1|1B&v@h1tAi0apH&lsGYK$VZMu$G5_l4!X4<lcSIVW3UNQjs}_W4gijJ1sol(~mWO2J_18N3t5@frV2FR4'
        b'-ge#mNk464Kk7#Tr3POIyQGF)CxPSj_UlzI#i#mTC$?W>%KL@mF5SGw_mMQ;_{8`7qvu6)MFFw7qNNVsDVi}dE&zfAI3=;PKi|fu'
        b'9Wpt@Im^Rl)kTHL{)U<oT6kL1>_*?faonirBSj6-1s8v4Y`)YGS9I|y&1Vlx(R~qn|E}l|*=3>$nOql?K}EC3UF+8$7@`^TcV}Tg'
        b'yfz$iO@DveeSPI2xfN_v60sNb?<lTpww!iVu5c9vPO%=Z4m3a3U$=Ag4yz;7f7cGFBg5aCGhy+XFWKZr$b^~ObZpbp#L|3b5Q-FH'
        b'aga5m{487lKf1m>uBjt?{N~;ygmAS9fyhgndqW@~wn<QV)NUbYM5Qgn8mYDWH9-*V%Tns2OSie#HU^|y46TB-+awl6Di!E%t5$ar'
        b'+tj+aYqh(5*$POM_tUl(h5I{mgKhWs{e1tKWM<BsIdkUBnR905&OnG4{hZ39*nQ6pWJT1naV(i+=LLz4l%huk?cE?s_6DK*WOdWK'
        b'a;T&!V23;^^$Ic8&F$QW-Y}>uS6>ujp5z<N5jW1y_}asyBJKuIN8BLi0P@3vUaF$@IKq2g8dCuRNlMwXHz%d`sU7yd9nP@c%%AmL'
        b'2Qk-YvadWl|0J)EJiZ%b<1@w|pYfIFEOTu4;k=leWaO8r==P|^_?M}8>q*t|`7odDRU1G4%2&(ryI_Zo;SL{{bYf>ZZc2bwU;IFe'
        b'o7%XJ1M=n{#@V1n=?xbe<RI@2@1jQ>?I)|*DCv`B7e11=@~@cWzAto0F$CTBE42Opgl-bHz00k;6J^&(9fyDnRQ#J?i!=Xc@n#`<'
        b'W`&3U=dbYW{|VnBG+hnIf1`j&LOiBg#`QPG(?U@|qrj*iA5Sx*z<`3TRDGHYR3Jkm=rpf>csvuJF6xKI-QG;F=m*EWHi^OZuzq0N'
        b'V9V9_Lzu^hX8kAQ#)7*u`^JqnDzg_tnh({PJrHX6FfQ{tgmd{&nb`{AtW5uS-U$4eop}|)IhiLRjLz(Y@Q-|`$n1bHj1Og*S0I%0'
        b'VQA*}5SC^B8NxqgUWRZxA3l-!Erd@RX*L%;7#o}U4MZQw{2Iblex1Oqj>xPUe^i+HA0RfuKXiAYOzHVzTvIx$?h>Y~2qlvZwx{)<'
        b'LwmOBFF?30b-BT|*<XkQ!#)2THy<6T6Nc&E9Jd|)n>PzHT*Qrpq_cfIcd?B80achKF%mL!X4tyLvK;X`lprI8#>{YIrqY->D?9J='
        b'UE|9#m#u`fJgG5{G_E8w9~<9&e4G?#l&U%`@=dRxfwi+fn~Z5~P#w;0IV)qM@zIsz_DU7|7+xRtQxxv_J?4yTmn@6)24kC6MOR!{'
        b'C1;mmEuYBPbH?)Z-o=6wAGSqf%sb<2R@*COrw@#`f~Y-)wS-Hb+-Bb;BX=RuTO~CMG3M#<M;USjDcZ6ttxXa(=H`Bi(cNS|eLL=K'
        b'_CO4?VZ3RTe9cYgUEYU<%bp?qt7{Z6v)n5t(3ZaKY10WVdKG(C6<uWfSR3cSP5<H;-8lKz&nw3}%g39`$4Tjfl1b5)*9tFelDoIG'
        b'c5IcuQ0kf`C6iifRj$?2Z4qSc-dVV5IaWN!qQuJQw9Uk9?wU<cZu`SViA_SbZ!HN?ZP<(ZGO(JtmzR}<kQ?^i)v-~&uc)I)zUhfJ'
        b'laMVEMz^;;gn7>i*t0RsPmX(v#{Fvqp5pQ5C&rCZ%p8J2r(}SA7K`~e2?~cFuo}kAZVYs<Q7qj0IxbGd8pZxdXot<GDq7O3UpsCD'
        b'y-bix-@wH=n3)j5AKydhicKNs%R$R+ZQo3dHF7^yYMis74`#D7P#-u^A3TVyS<Qw^Ju}96&r2#k4r8xq-+bpB0GzXF6~L@n?Of8F'
        b'Iqv<0e*tNUIb7PbN@ZSyn`dItub4ks!#;#Px?cP)l#83d#fQ1m6Jvbm;o^fF87Xe%R?otHXSi*%+h?&)3EV}kh!g8el+x2l<1Tko'
        b'>sD2XMQWRYMQ_<xRPrFUQQ|np8RPKX+VPBx#Z8OlUU68}VwKB1wRa!o86InTL+-A%e@>4N2A>y#1s_$rTjPqV*<G357+fgfT;i~;'
        b'k+}F6*W5kU<d=UQIo{E4&-hpcwhb9o_ga*4(|}PSaVf=s)3{RNYeervel8n7J!5>3XnI#w_-d3TeZWkpfTv5}(CI_Q$>`66$4`qO'
        b'8~m_cQBV(|8J;S99c(=e%mupbN8~8a-w|*)3`E3IMW<(SO#CA^y}mO!25Ko}4Y}t*oWxfzToV@+WD{bGM5~n#laj|J<lE%C<ZN>0'
        b'mWl<5>)XVbt^LBfb)_2~m~a0BoBJ4R-{p0EdZFT#r)F$T6FfCD#JO*OMbV2hK1~z6IP=xuO{=5n_BYD9_8LUB1o|rUH}BDroBW?7'
        b'JSasZTt*}`UmhEjeuqyINhG?-=XL`4eYjh@<IZ<(&Ho;Ii%61gskj@gT>HzJ6}wmo2BQ>W(X`z@e>yIhTT9|}RtEo#ul}<!GL$8-'
        b'_I&??bbBIt`9#*Ns*6gnB%)`9(4Dsv-1OUBh>#PAkdc?=JEI5$OG?SN%BBvzE+j+2HFV(^``HD1Q|X7NX0&|vc2iU7t22Lm0%t!v'
        b'+=2^S|F}@qTKXw?B>#B3wYBuEnLj>>yZ&)_F1;uF)}F{)txkEv`)CPb1s2`l>*K(tO(IVT8i~T2T>F~ohp}5uqpMO2hdAZADHcp^'
        b'tqL`Fmf^IjqPn8l6^ylnVA0N|T3uCDX%(#scq2RPs#3?D@8Ox(Py?9CF{ebS#qRj=6z-`U13#Wdnfi(`k8=$90t9-;HgFBIF$-fN'
        b'`P`Ss&=Vn*UG)S>ww&I~l%v$RsA1~nsOOJkG|hipN$fXJH%9M(*b&H6=q)9vE$JU#NGd}~k4q~jqF-onC!sr6x1khE19(4r&xSDv'
        b'T99R)Kx7yt7}6$>Ol202xv2U4!>T)Lza)dBD_l#k&)1KgUO(nqj!jCsPH%2;Z$<`mn&yMKE$%O(K7y+1E^#cCrrb1<_t==1T2Ld}'
        b'yYI~w_gCk|Cz|c`s=6*tdE%y5@KxcTA5bRVJQdU^DD2^s6+d~hfgyow?3l}=h-XU?F*XSX!o7bBPsP@nb^LuQCDi<-dsk(Pq8Bd{'
        b'dD6$2e<Apj3o|pv@*Ws-3Ts3_k;|IOWS}N)6CM^peI=g?O4eh{B9!E!Qh`KQA;zxfo39;H9vtovV&bD5Mv4PhgrfHz{2ZenW3`wv'
        b'AIah`?-OXcIVS0UrCY_#+A(qw654cBi85*ilZO6O@>1SRk1eVM3*{9=>w^OG>C|IFaJ}?A=())ii<iDJxaeC*2@RwKsg}2zKb|5F'
        b'u3q?T$YQUjFS_NtFsgxh9+js(eNl9a_b-sV+<2my#G@MM#hB(Kr(7<ism7SU#Lt&`#A6tq;m+7yHj&Yw1CxAzgR!magZbgcw*4`0'
        b'EL|YV<3^YMJIHwSkIU&FZ8I1ds<(YYGb>E_&5fKcItxSBfPzp22L#TKMy1jHQ1jR*2q$VLjxyY9R0Dm5ZQML*dpa2^{)Edkk9zt?'
        b'ZL#_eG3Ggc=g;*~Bm5C!<}6Hn5_Ih-v~&zL#l2i*>BE>&^dIn=_=VKw?@)dp&nju&r=u2WFw=`-lyB5%!>BJ&sJWZ=dcQ~tiE8kF'
        b'7^}%dkyE0mhQbfH!sDDW>Zi{4Mo*s~ZE?H56EzAnm2-h#Q6GW0H3OG^Xz}!UQ5@jk=cu?*&&Q)S8c_;iqX<!adejUFA`Ey8f1(=T'
        b'ujhl&z<Be00jv;V%8y5ykBzpuB|z*cM4qKWV%;~2#*i3|A<M@@{w7YjX~_D<Xy>lc)9;ObCjxpJ(S;h@#C~?}t`?x@81PP+IN;ei'
        b'3L0VdXy9$*V)52Jcbi4n{x?8k$gn&ok2M<uqpA?g+dH~Uq%x{Je;8$CsDN^Q5B0-{XYVw5B<^^PYkqx{ECa&!@`NQ`%Y2SUA>;@5'
        b'd_Utt>0WEA<%MqRuF-6<<;K;_CrAH4^CK+jAC0)t+QvK`=mKSWS9ArWNm%P?W+Pu?R3|B67h};cu*<Q=ASM?j0*4=zo@j2w3#&P$'
        b'^a}ITsF!MVN_K)dw~Y&V+3R@?{4d}0T*f+~Mfu(7r$?a|CW8iX)It7d=eAI%k^Vmf{qwEa)0dH%xrRb-x1d`h-{zDPUoS7QEyWr|'
        b'Yp-wMuLf_<86_7rc$nYw1WCWjOc_P@STOA)NK#T!b7>su)BSATf>9gQ#$W8SAslzi#jK{$d~x)uN5ugDcLcA*zhLGgM49)FGD}B`'
        b'g?UM%(M21D#gfCK<|U(O02Yypq8c_z7$X9EQEHhGLn;hOIf@spvD!R+E#5DpipZD~&0Zhjujcl@VEY`miN9zR*FF3|Wy89IDkcU2'
        b'mt<kqdqz{mA<1dtR3U^yi=sVE<oIC<+hm4bH-FNRn_Ig2L)?+bMHe~Fa5UA5WDaUrXSK6pFz#Zv)+nCcHUcPH;`RPkC0Od{DN2l)'
        b'!&l&;wn~G@J+>^&*Nxs@IE?#v`y%hBk<6b)N;H@)7F<;fZFiK5%7y-u%6Zc5qK(2|?gSYe(GQLk3-bvQq`O>LP88PR^Q0U3+Zp(M'
        b'4vZ0^nm!kfp1wFjN|J)Nl*_$mWett!LPsffuD)eC%#AQ1x!04+8H`uypO5VRdE~H!DIM`@GY$vu{t14QT*Vo?KOTYD4Twd!ij#K#'
        b'8^y*T7U?RE*nI)ThDTh*k$3Lvy2%CBz6VCUYLG+$vv5S!rn;zoh78gCNlS(zjhhglQ-AM>=jw=2oeH`quVdsXsaJ!6z9DggI<-;U'
        b'L16q++-dU&*n1kg7HOlXsZ-L6>SyXj=kdB{0h>Fv+Bc4P2kmTebLc6Gr?kxZ5qF}>Tl~vjVEYIyiKrZ-B~KnPx+JZ%8;h@vqTTq2'
        b'OP*MJAwgb6xAIrUk`b&i!eCSIw~^fB*Oo{z7<%FJ#2Fg&uEB<|XHOAHmEMnIn2BLvT1@3B@d^*4MM7#IgpUdy)w8jox>Y)T*vPRk'
        b'ozrWGRoESwIwz|?GEyH43FifN_TQ{kWVQ<HQe#iw9RB>~@UgJ^*uuMGkA=0x!oNvz*E`sELjS$7eEO<bo>xX()xJL4mGU}TzF^)&'
        b'75>A>kEol7kebjmmlKDk?Bg#lLzm&yZ)=_$CWD(A(0$d1(e;zH#ew?_`8#*>n`%);ExK7aEt|iBNdNMPF7V#7gpZ>gi0L@<#}WRa'
        b'I_6tc8?sFUcQ3eVaBb)X7HUK{4wdsaPf(-7ssL^Y`OBS<z`PE`ZO_vqBdolmR^I%?NTPG!K3A}azqr(uEr9eyEuwzzbibi8JZi0+'
        b'SqISC2vvfx(&dtf%D!>e%3Rsg@76GDM($jp<cv_MZrJTNb{c~0pe<E5W{=Ppg=iyhp%tU@M))hewcAvxH`-n35+iMN)$8;3C-8}='
        b'p-B5{1&|$0Pvg$|E$%9Wn?ArLYIhzNglMa#t3Z1{X(MIGCUT;iw~tBfJmk*knH3eZBqX}rZbz5lmPY}s70Ep`t%j)QZx7pk=j|Sr'
        b'!tC}pc1F$7&mCdnM^Yj~^ob)(9Q?r<%?RHOWRwrb80)ZC%XCP=K)m(KThh^V2<rtKArZyve&*2j3jfBg?nX#*X5<L`F0Bq+;*UIl'
        b'x}Uhf-8PJ3MCC4ZN`Ct;H8XSMEnF+946Y5l-^XAhbT-ZiMrtIid$XOEk&>OEbLh4aGM&_dwT&25Ue<4S3!7+}J0LOTfy8g@Os1Qb'
        b'jX33Ymfy=N=Vix=F+;=k66U92{+{+ZRj-G~fsl<3$ED%S$Z&>Bt~%Zt@@7SCQ*B!njV=Q{wg#Mn(*wgQXPZ6tFRdTRR39OH$Jg+A'
        b')U{#oX;dG{TAc#>F1{j^K_|}P?|kRG)hVF99|m7Q<&<UA%ByPlr|tv&jX*ce3EU&=8-~f-AQF-ItODGWhmo`@S!Gxv+5oW?81=7V'
        b'{ojY3cui<I;iR>Oay4^mxK@$CKM12$l=W8e?}^dHis^*y|6jtBKmRsC>)d^En2ZV}B{=IIQF{qtbc5fhZWPuHa!!K$jEAZUFxAON'
        b'Tu1)}1!98#E3xeBJ4l@BfmE6h#+;~Zi8&V+8br5E#eAcxukQ2?pFS{5&S-fDJvLakCDut8j_}V9)#zxM!M%BUtk>{_M(AsYAz5ED'
        b'97v{%BY05#8^d?t44%k4x`Wmd)2XSnNMvwlK#X1@qIL|U7d`z4!UA&i^e~vFbg{sHg`?epdwZ$(hCIwLOFw}gytfb2@CU~{FAWzm'
        b'fiiF5OxZB?;;>FvnsC<gnV9;+uooB13qJJz@2Ty>9o2F}wlF=d2EULjPp?f~=6wfqC#&d4Y1%e#q?FE=x!=nqLsbnr>X~6MvsKA5'
        b'RfF7pKy`SVc4LB88wvCVV+qCDgoJEuZ9+a(G@MX_f_ijZ0%oG3$e%pFANEQ`hu$Betiu-$p!#&_t@Sv%hOL2)l7f<iYT%E~pi<qF'
        b'sjAgckARr*Re_jQt7^AtrBGEAR3#;$szj)26IAsus_LO(Q#bEV=Pem#aiL2jI7NUBxcAt@HHx^j<@}}g7b@hQ-wj`Um#ddnRfSbF'
        b'fQNpe7A^9wJ1b|Sq!*mBR(>hBjX=xavUWK{pDb$)Y~rtxR?Y{T&m9TaX_0^oi%%7h!VJ}&cSG4wnF|*N6^BuA!~C^nz)Gaa(~8kR'
        b'rDBIKl*{?2YkB>iCgHED=k-eIWiJ&mOyh$1_hpoF7%iTsI{AJ`T~<ANq$qTPl0mj8{{2x(F??Z%T$kGF<k^<GtU&zJoqa-kDJ4d|'
        b'Yr_RFFK;+z=_r=li|h<Oe4$7Vew^z-$EISZX=m{L_E#2XIAvsHBc9=GwIAM*n^3Jvlv!MO=IkN!k-H7CVPG<N#h5>YHYlaJ$ufgQ'
        b'N)l-fn1dlB@T`k{vB4y0N|m!psq4tyRZbbYM9U&Ih%s}Kq*16j^1D;$nc3SE;3>puOX+Rjb-sUMerCAA_yjb>YHot>R&{5iFtCTW'
        b'n;HUSkZxBsi+`SOoBqO3=9fdjUIQV>6;7lazgOQr1WY!lu_~t>oe|k#2c4~%-~fhaK4Se2XTH5c=&sjc(sLQAi97r9r-m{=4&V|^'
        b'<2p42eUnN+?{rL~A`5>&r~+Nq@qgkXBVs0Yw+~{W8JN>^Br84<?Z=iU%pUQK45C5)sM{&?3=M+bo>tnAnr?FOiD(WiPjmdhVV-L|'
        b'+(rb~{TsNACjM^dJlBvH7nX?7BgEF%hqj)`xqvSDYuzU9;MbP(T?FQC5bllAdLyJI?{Y9&HaE!D)yhjGWYs>ED_`0e<nQ6g2r|Td'
        b'YzO?m!6{#!ej3OBa%8p`)N{6w3{9CYAo1z#T7KRt9fEn4m56jrr8`?xV3w$ytyJj{)LMgAl+zJXV9_BPlvI7BD;(wm<rvIG3z(uI'
        b'a7SFlm`g2SHVidy8mg5r>xN<~>1+W_V2uJgTg1FLh-@H1;X9E5+rSkn1Jd`WL1U@^8RD-Ptmj8hg`rqHFPPU~Alb~LLzhcj62ad0'
        b'L-|3%JTe5M#3>1k6Ciiz`#%MS2a`M0F`ZMuzZ(c`${8X<?DeWPw~qM}s(<$~NT@vrcwd!%=z3(gamW=6s8{g!_+8j1_uM~JFWuKr'
        b'v;4!2DK1b?*+N&oj8s(pIqcYSU9C<(ZwP4CeZ(uLH$ge2ZaO7N)22qHr5dDIT5;+=L$PRH2)`bP_>%A&zG#OU1;7@~5E&d`ORXH('
        b'LTQF-sRTXzlnW9vHRi~GuBV5f7o3t`mSLc0=(f@6Rk(Q)CVGg@ek;I7YTh7Avm|YQEmNhH1=0%l%w+Ng$zWIUL;SfyMmAJ7=8|B|'
        b'cMVn1IzWcH1Y>3lp)SGes)OAp&;lhRMG4J8Kq(V6#2*U*_f<86w>dHugC1gtjzw;`9v{*sAMui6b8MJ4xkH3GS8k*8jT`BW#(G1$'
        b'Bw-~Tt2m5~#?%Wsg0M%EEvqK^c4eqabKRv%vw)f$U_<wj_}*eE{H5t-06Tr2j`?xGrOjEoeMXJht9|NFq{vnLR9%!jVEc6s0`b{I'
        b'-pGKmTbTLvpi#JA`H0Y{2?Hl6o2ZN>#TyBmM$sY0j&zga5=aliYF0X9w=LcnyK!;-{Py5wD~%dOx!|xIO4Q52YTUdOG1xL|(yRFc'
        b'n1#=_4?ZQ$4m$L@UjGj?PK^XwRu~YHVS%;F%v%FWgOrYqWL`i5#ji=AIXnw=WVYI=SQ_Cw9ApU-mbkHOh4S@VY%I18J?Y%U0x=Q{'
        b'0BRm|E-qIfs<toQ9{ay(atZ)WJi_sB$VBf%sv)d>^)`Tn#_)+DThYq|VcCnt=<J$Od#ff}`SrxoT5-+d+H7AB_i8Y@kCcv$5dSAI'
        b'-%ziirnH0#skaB3jtiCj0_N=j&+CJrdt2P7y0%cMXZIi(!ng+cML&ou%Q(-ggFgNpcIKr)PdP%tMhN%z;GUg>OyvOhm2DAH=9R%;'
        b'&u|45%x205YC>7<JymZD?d8IqwWQ~dgNu>?^B;Z#muVk(9H(K*0c+)%K@xW*;;I%^d~L81W*c-w<}Haf!MSX;D^#17;zDoZXd~Or'
        b'?cbIsf(3sn*wQmOPhz^km9HRi=bD6sgk@x?MSHt;4Zpt%V=r^%V4M3SdJR>`R1F~G$THY=AQh;16~(L-18tr~kd2ltoG69LAJjiK'
        b'Ko>>QMG+Lhf}vHkf_elvLKo#wD+e11x+t1550+fQ>7u)-yg|BXHXqVdE`(}6jHMoiFr6ty7)ftl?qC8ztr#>HMC3g*NEbXsErb6t'
        b'c{%W3K^KHkOCcJcw+y1;G}u7}&zK7s>iK~@(_q4L=7NX7$TJ`1=%rES)xq@Qedy?J4|*iCFn=a8LFY_SQG@K!DKn0NZDwC3bFWgF'
        b'jmSFn??GYVo4lo3EB7Q1#*onThY(q;TAdd%Shl@f#H!i6d4qOFXf9A+$d|Jq$Wbs0=c2PDtPwLW{<Ga)YCbAhlTQZc9<KH-e$(sb'
        b'^6nZqR6{$j=GLidGtnBSTR2i72dAj)TX2<YGVKj2uMu+rtmtHPGos>=(1CM@GZ9t43uP%G)}Xc@Qz61qLY<k)M2wYUY^H#9hw%Re'
        b'?2?mS(J5Io50V>dS%a~nlkAdHUV#9LA|5;%>b46zjv<1}j#mYC;*FT{+*}epWAD!ktvN?VR6bh&4H@h%-_cRS1D=>Zm1zV9useHX'
        b'yKfAz!A)THJ7v2^2iRpz07SdF_z1bDcYt=osKDsOHB3KZ83QS5wO0~DMx)Ulg(zzbrPZ@ZDLT=mwpSWG-wg1FyK2Zt<k+EuTeLco'
        b'UA$ju#^~_RciLvMLE+S?0gD!+P7crok!|79$|Ih?pfSY!6;(p3S@r-HFHzD#!Q={+Dy+>d04L4stw3$QPtL~a0mRaSZ7m65)yrUF'
        b'U|I**BK_);+4L;QR@*GEIvTW>`;ZU@bkhl)=lB3~l9xkXWERYH2?^(7?IV@jUE!a%xofs=6y&s@3ThOVXEJB|0j{jqE8OSIbgfrd'
        b')<n8AIW6w>ReMBLyLOZ>ww#DyH90Q#diyIPdjgmg36CHiq=i=YZ9c?zRC=g3igm9qH+aLPWawK#ZdY|9dd$idCS)5qd#!9U_zktl'
        b'%5gm+WW&GT{n&s#e#fi4;tUh2oN{o#?6ivc(*R0&L`X|Af^4&BO|I)*PDKgVv2r@>t^f@E$X%#GF9&<w8O+N8)-43)do?+3j|eeq'
        b'u3&c=^qA5coDS?oCw6dtR15~Aa84K^_z2IHP2v1-k~VJ|@H{<$%Dxj$t79umHh-u>@4cbkWrM~LR{z6Ft=OwJpfpX+PhE0m0&%Tq'
        b'LgIA`5XK)tBG~ITg;)4z*1eN<+uhpgMx6N)K`{#lwAqzjS}kk-px?7_AV5&vfb=9xfiSckdpMU>=#LKt5!cKOMI=|qU6c^URaJv5'
        b'Fs8(L9B|n8Cg^qddefgl&w14^fQnGA!BD>^s?ehKJ`3Jiw-XD@*P#Pc#DGD#|H!3OgXNMm)o7*rE!8t=;eLxjPTk#az>mili1Z5v'
        b'47MdC4vuCye-aSA#eMl3gBxq11(wIeP4}ttY2{zh23Ec16rp*CL-*UBHGdvA@Hp|R^c3+FLC&htei^B&$v*N#?TWXg8?_s=TUYOB'
        b'tppjk{B8T;N>RC4d1>OXLEOikm%!XK&SCclfhBxO@+w)gf`8`*VV`@7U=*lBeH|PIbm#rl*Z!PA1VrNE3mh3_(}blOU}mo|JJrQm'
        b'+tu5%>XX}p)69nHxs$jvcWyLTl#`}2oH;JcKnuY-Atl??`B~-a@+_wr%1EG0oMO5JvQLZ_&7|o#H@#*x-cR4z56k;cpDLr&tC^$I'
        b'-9TJ+moAOcnKiSKQHC~21j=dwMtnnk*x!7upT==?)GP$`_$j>b-ryuDbGiSQy*2%N{os3AjuGI`SXL6u-}}&)3EJ6colb)7Z=sI$'
        b'c|+GK)6tQ&=1ctu)y+PHil|FOs6Ole&G#9Pp@_<$0s)9i45?Fv%#)(s_`071>&K_-``Rw!EE!?R7Bb$xmZKc|mB1@`$3=#_cj-W{'
        b'+k0hIZ|Xij(GMO&Rn>gggP4n))zLA(>LVResSPT-eZJd0zw1E(`yk<c@Xi_P)2=>GV?Us7BO^d@yQG2^DfkejUMX>z1Vs#E+|J6X'
        b'Tr#&;*3=@S4)oh=(Y?3WN8n7zcDwrl#-1oZACRE0M*?p&zSZw_|BVbGXP*rYX?Qgxe!svO>H6$u<)-r?_VYU|WmD}DOm+V}$(?UM'
        b'+J;H|$Lz@6RsG<a)CX%L4+|3H^$FUv!(d2PFj@qNY~G4~&wu)WoZUP757j7}clN931xb~Sf(}~FtU;Vjq-t>FXiWP*clS5H)K3Pd'
        b')QSRi?elt}%bhy1VoQb0-YT>+naZ_TlN0!N<NlH8THlR;kMUf;Q<A6!LqE{Z;9IoYm}mOQNLRLid9wfXQ~mXl77|NrfbNJExTILq'
        b'3YD(5wJN(>wX53xGO$|6=3s{9)8(18zTDhWTSWK%gKUI<lQZR*!uoiBBVO!4@6VkgU<4pb8T6C&k^V#BQg0lV@fTHkgMXZ>5tAVw'
        b'zJB-eWHMCw*U9uWmJk>S%<hzfpAH@*N!ZoZjuGy}nRB19BzD5any~1P(CJvj*Jq>qaxawHW_9m(m}mJnt&0DvJnw=2^TPb+(N+qG'
        b'JF3;}##YZJPYD}|ujO?E+*k6)rObkUQf$k{mbX2Hf4XPM@?_-<L2gqidR}{&%RP1@`e5A<w|j2CF<8*P*ckt8%Im+&)b^7K!(vPy'
        b'-=9jHe2!GGv$_q-u#?+%8j=mmgr;CjwWqbJ+TIe3EVMQ&_O-mQkBct)N`6*gy2ddP{RXhu$8V8Q;&1r3-z6Spe@Ci3J>8(d;uUiC'
        b'tN>&j5_IWyNU^A=kn3DQM_@|tZCZkpQE_zikA`52cg(vC7k|cKaRybK5gjG;E+fRBaI}OlL=wowPxPS0xJL=!-}%H~(XWZiM2-`8'
        b'zHu7sOT}+1^yhk6^=5rq-_G}g^f!8S&VusL)KK;SmvT(mNH7<A(V2d{a^HEP#mzB&D5}M$zcvY+nL)UY_mcAs^fMvJ8Of^5%YD(w'
        b'`9g#38Ks8Qf7{pMIhNFZqD6N=#T-V(okUUU3(jgV$Iw*2#B6&y?~6XO?KwUy&ASBQ^L)646q#*X&9-g%MCBX#LRN&C-LqCl(0T2B'
        b'UJ>U1y)2(7T9B<hP%q>UT~xBv>0a^$EjqLAIoU^6g8le6o?anIkYTF%)ATB9ZnlN`$r;WaZI^|oW;BWb#Pl79<v*u<<rbfFOb9uR'
        b'GeCYEy&Tru(&wq^W8Of+k3Vk>?R}@ufMd!t;hFFBrIso$Db2WG|Ej#V`k<_cjJeRL0zFMCbPYPMQDDIF{nh$CD33@jZS(k|KO&=k'
        b'&BqNm0r`LG^B(vR0gy9tDjPofHJ>oxB4xFZ)Z8y3l`Jj_NlwX6zJPpx_CVZ)2J{BzO9;2bS(;Pn{>Y9Lb7I*|OpyT^MVG3BBKBmN'
        b'!6>?492buJRG1-@IC(%{(no$`3nf-t=3c0iuW1-*kRKzw-{8eie@qfWBgQHx*ifSE8Wx_hu86T0$!umKWL1&qtN|AuA@qxS+Z6tj'
        b'`@M>8{r^n24Hf%^ZlMv!p{o7eFl>xirnN6sI5#<N<-9bZDF}O9>}coOj6yL?q{dJjq{dP(35)<pi+WOT>4Pzrj5^EnNFSQk-MC>r'
        b'R;VT&{E7V3ca#Sv^$+%uORSlFj}rOs)Qh37_Ae)e%LuZvh5zu0c>r}iI>2C7qvPP_0?e{x(v#Uo&h^hB^9jrIx4|1jeW~kXX-s(x'
        b'E9~ODG*V^1&RG=E%hFF%iG6X|I5oeIpQmDa;!}fm8~VtI_^(6gwtup2!3Q*Y{mK5Db*Z_1PDy2rD*}s;6gsmVx4D3N=JO(YYl@lJ'
        b'zRJUNaW19q3w$D2W2UvawPtbP9)4>~U)fEzD7EaX1e2YXH4-FQ6e^{Hducidr2A|Xb-jlSK4yAVoQqH78YV#blIb?LpsE*US7BWA'
        b'eMh3><~|*FUk-crw)Y%Iw{aGBN_iafzJoE{h%cI{u-PLDiTb+`OfVPw&zTFgFr}6f*=o?N9pA{mxvZFhsU>O|K6i`kgd$u0me?^6'
        b'$WYI~pqvh$tCCB<n;9qy0KRVS(5fl~@r7xGZ-b}5*Cp+DeI}@?3S&Q;=~~|3>Xf@^>>thsXMJd`q=r5mp*7TM6H*I*2%F~jQ@Bo_'
        b'N#bO9JB-wz0@d!zz58BaL7?-=NDxD;)>B2RD)tb;Smj?TUM8}!=v7bvjI)fUiCp&$f3Py(`&-}c@%*!Q-3KboMy2O`?<sLzvC?{?'
        b'rxCZsJ^0IvWOGl=lWvHbVRLhu^U4h_oOZ|GIe`Z_O3vtPZMvA8Q{u)T<}_kj<_Eo`$QUbM9X6N6vyDVH%z_yiLNa`5O_Y(AvubU2'
        b'SoVDT;#Lrbw<H;FRJ-$c<UXp(e6QEMSXg;3CI?J(<h>X70J363O)@#F%F;?oa(7ne3(GzPeZP5?%)UzXsBo`RP;0Q^!7d`WY-^Q8'
        b'mzyiR@QOTN_-j7yG6oli)+m09qU7k6rvJtfYQrTiLQ-<{?*Sz4|Aj<SY^=%pFC_1A_Wwp=G`sC<3f7oo$WtOj{vQ!9_Ahq|OFY<S'
        b'r>a~C8RA9}V?fQa(F(H~sLFM;lEL=9)od(Q(#UPDm2VC>v+J?dO5AKynDH<#5k@NAuOPTR)lQ+cus63>zU~g#p>T=U7}nAjQ8;l|'
        b'@x}a0zoK*spM9)XcL!s+aJ5qK=tUbYH51Zj$9i%dVCx7~;6le@ze3<<qtu2cnTaGGj|)aCk7#*sYpvkFNHZqcLSxN}*#D|8w5RC~'
        b'7{Vs8_Vk#|v1ZF%l%|KK@2xC3COl8%RCL_2r<l8YYKo71?c5ev37se1f2Ll#zk=C>SQOpBOkC%`l&joy3}?PZX<D>xuAkG(XnR}K'
        b'xiLA766SjZldxu<bb4Lb>n522l(zpIb$2g)QNXsvYF#xE2~w?=iRn#9)Jkfj+S?9G0_Q@j0pUD}leRdy!?bB4U@v*TzRtF-BbVJj'
        b'vZeeky{wmz2oFor(B~zfC_rjiW3CK?AwSdW#tCQ!Pa7e?C{ZtnN9Y7(lA)OP(j8q!w=GoZN-3_Vc?t#>a}a?q`pe_ei~|LAX_8Y?'
        b'nBy5QN=*4nO!H4YNG<;vMZIS}sY`);l(4VoH~MzChu5*YFZYl*IH{~#xWzeJ@9!akV}QsJS`HL|?Y>1Oa?>jK<NECOo$p;^$mtKD'
        b'PG1i!K9k3Gx(v)~*N+Lj+8pLnP?+FQxU!RupLLzpIpyV%PO3b?sV`64+ZTLF(1;`V_Mdmn9&xozRM|^^Obub|*ZKD-Q}=$=<N2_M'
        b'm4?OF{F|@FdoF@GgsKsba?|#6-q9Xoo6y##Qmzy-CD&aZ0jphMFPH6&SXlQD1vtrjzQNI(KMi*8xzvuua`>OI#NJRx2yum!kYQ4E'
        b'u6mV1grV=k_>CKHTTTFO`I2cc%=ANGZ8Y!oo=RIBou9A-iOtK`tp(S~Wo??=?1ESE`$f6p33B!z-Wa^4f>sdfQ!|l{KXnHD7$Qp@'
        b'QVV8g`}&UK@)IYC6`0}7?Sv)DZMV?O@O#t~b^F7>=Vgr7o2tPJvSY$?Em{&eb}VYI>x`<SR-P-J*!PAa7$cTpyVqX_>>zT|nvGb+'
        b'CBS{Cw$Y`@MZ11!L>A_|&Yz<;s?ZUf*KuDQmKWJWi!h5Z*dP*E&Pepu9%P#P>p40smJr6$tL~z#Jw%qyOk=B`m$byjdt>7?`N8@4'
        b'(&uO9#a#CiNiE@P(He-H%f~+~oayyq%)N+mwBk_}mXBXAlz80|CK094xKKHUw-DK0wY;fGShzyo{z6Nv7Gi~I@=VF~Hnr?x*t!-%'
        b'2Pys%`Ly~cLw&acc3w_E9zDx@+T3Ai;VThw0sNS{ZSoi?Bma%;>g-`kEvA{|n2a9X``{&G{3|(u{Q)fu4>~)E8NLSIGo*rVjQ>{d'
        b'sh)bgGD`DDj+))mLZ=>#mXb5t(5(Xk%}X2;a@|Ykvf6aMYCCh|`W?LOp@IF#R2oKK2tqiI5Km06pOZacIT>si72IPu${B2_`p}+w'
        b'qV6_#n9vhF*~I?W>xt~;%p}6LjBwoI42g3Bn#o|x^U`^iZ>H{yb7c$09>wjf9a>m8!SVYud55l}0Vvw1AHAM=^_p_~j5bep3;*6C'
        b'({T;0Pd8t)(K$=Ekj155`YD)ji=%7>xn6Z{dqr{So#?Ukm;V4sF_p}vYy9*91%hnqT$+9=!9opQFUH&V*kbSAh*SO7>GgLPj&XGO'
        b'U8Iy=8B6)E(*^fxrexj%c_X1|;jG;t9ARkE-+Nd48f`530$TVI?Nhc1s6Sn!>72b?issAL$rGA4?y{Vd(6OLlkTpfehACOhEZS!Y'
        b'M~kEW$CPv|sWhX81Qa^!wpZ*pCaI4&E;uYdrmassP94^t3U2f08i^7jtT>Cc2G=so0n`BJ?s~ytNxl4VL_Kv_TdzNy3azVQoNL&E'
        b'6y_P|{TyXJ`eqoNaqJo`$qL(;<@kidXrlkw53Xahx}Rn*30i4+VtmP29jnf%nN^NE<7-2=rIgd#4W=(RUjMXu?95J7T?~1y8O_PH'
        b'sM{<P<ENxCWTSwwqdbr2I?T)h#>MBQkNM8>XQJ9@aV{~@k|ek6!s@=`Xm?l@20p<|_UILl;W}~^%rn`jyYzp!zWc*#M3x>+jb<4-'
        b'H4t@I*L&DSkD$XTyWj*pAOra#j36yS001+PP7=7*+{Le{!sG!yP6!4%3r!#QT|>7-@bkwOEJ*VoF3IKV<S6Ym1wNbFem$3-K%b)u'
        b'R&2qfg<o(<Ee_sAo<}&o3dr)2P-Z#sZlN+8n|^u<t1Kq@M@(%YAo@Ai?~Emw2Yxc+SV$rI2;;+;MIUSkmnHqU;f=_=Ti4Lz?BT+t'
        b'g&`#JGiHxO(~cWlH2oC*I8Fw+L|FSWmkBfd%q2<o9#bUkI}|y4(TPKmcO_LEip0e_Ec*HARcJ5VvVkjEf{DjD<(E^t4cA@4J(lgk'
        b'E-Mxg02hT7CF0__nCFJywFGNPWXY(eX3?SOM>F<SE7L@-Sj_UZaQCchu7m}*4>#X;oy<Y!|I<+mZZF^bNo!mCWa|;MfWVCUk(D4k'
        b'E7*T-#a34k7WdhLQ$fsEDAj>uSYuE}Fk~zD-GaQ6$17uNgzde%F+iMh<ZC|Dn}v}<zR$Vnts(8=Vb1d9xc9TS-R{zuHxJz>TswhI'
        b')S0m8BGYHwi^1Zv{JOwt9Hf*#iky|xt(=entE>rz%y$jeBtu>?vx(0;H${fK7wpivOZ8*dGEewzgx_m@pe5F*w9K?oNlk@2PKleE'
        b'N?WXHE-Fp=HD-)8f^$NOGAz~REWh`(tj+y;i~G%U=T4kx#QoizQSk0OX`|4xSZ%|xq*bf;q<}wtJKSi*%!FSVewU3(W2pz$<qCC$'
        b'@{D}>x>YLc=rwa*ac=I74X?apBf2eng3RtTbLP8wUta?)M23Jl`gg=9PtUbeL>uVLT_|Qy-%AFQGoTWKb)GBp<BL{9&earUq`us5'
        b'P#eEg$n?$dC-qB35IFw?<}F+TUcO~K$V(+Cmt%!rat{*o0zMuKt$d~Wlmv}kXrn8u+Y(F^UJAB){4n>F#1ZJhu((<KKeWE>Z=urG'
        b't&)+-+z+a~ZVob7DlONsgU#}r1@Bt^dL!?3zgd&1)ZFkA-QdQW{s|pnCb~)Gx>Y)JR=4j5j+7*sSZn%*YK4o+GPtE_tJp#@TbRTa'
        b'E^%4Y&GKRcm0mWaYZ7+&W!59t^qc%me^VijeIx_obRWs`Ub~i2EMND8s!Au+CChV*WV#|1NdQO5ltv==P_@l^uPv|GYt<U88iO^?'
        b'U`;hxGae^iB%Xr)Uu3Y}W1zIr2OvM)U?6~dI!m&UD)JlX)XD=?*)=b{1o6wZ#6=}h+phi8i~BAU2Ku3Ph3^?6Z{szyCa*GF{1joP'
        b'vxA<;#a6=q1{d?O_z1^Rx*URx+WEeKl)5Ngn_FP`>@u1}PFCL^a%fl5+5>x&<8#Ja+*K)&xNkY8-*T<(wCu#mM%-YH*E9rqGvBS8'
        b'0AvqJeKlNN6-S2o_HbAUB_ss#7#6)nrouMw({H?n%{nK;qWI6K6J^*0*fVt>rJ`@B*Y)W$uX)vZM=H)rTigdf+)t%O75*H4s5)}@'
        b'eb+o|uR%u}67t+mRXw3MUSq9E-hzh^(a)vS;65Fea|wRMWdf3bMBp8W6Qp<IJKx70f5dZELd^6x6!WdcbJQrW8O2Nw;YnE#bA%B&'
        b'ij)Z4G!HXS8ZyzHtYQTp10HgR4y-jnyk2vS&HR|i%F@%<S}2WIo!xX!X1TovXu0SXq!POOWV-X!t-8{7g-Jr}iN}0mLSyI1#o|>Q'
        b'KhE}_I1$y3PSLo7Ec=FvG{JxoSZDf>!|Gn-$XM|TkS^95x9I(?2XNCf*rI}zc-$8zh*=47Upy9*1#!nsjNGwR{rthLxcCBAv=sNP'
        b'#ICIl*?B0Wa61>XSe(vbMXSeI>K=<WSSe01e0qzVt$VfFt}C^inRHS2u)ZJdZ&ia)ZTaf9!Hx6c6h~@3;%oL~6^NUAkGCU5{z5X-'
        b'>mNy$S5;^3t0sxsd_%TVyadDI_Rc@J_l+1uN_-WW#dP?Qe11Bd<~02keNMe2WiRgd54KhPV$9W)S<<cQ=$JDpvvA*6oaG>h)IG|>'
        b'b2ZO!F)#aM{MXkC0QXt2qyhx<FU|loU!ByKcN^48mBhHgHxSd4atsHJ$b9cl`3e_*%JHNI=+uAXXIlNbJzg_)4^V0Fl%?0!=9{yf'
        b'rf6(Y@>aEBks7!q9>kK~Pni|8NP+7303l#KSO5c`CT_&^NByLvyxKGaTeK2VOpSas5dg&0qXw2;+Ah(h$h_{DLkisY5~j3ZaeHvb'
        b'0Z#AsZ`xZ+Ae>Z^u2`mAxKLx|VjdBHJq68MTaCD}5QDyREWvV6Oq>k7$<I-5RmXs+L0>jvi!MQxjw(*StsAORDsMSn<*=M&M8_^p'
        b'zZrP(pfanAdCPC0l6De7`t6_;^V*+-I;Yw25)jW8JS1KPH4>=CUEEgn<2gLvU*Lc_mb#w(9~eHp0%GuZbuNg(%J2S542m!FTy1vv'
        b'0~nk3c+tI5DV`USJ;lG3fi;HZPS$#l=?u5F010RThotOm*Kax{P|&l+|3WepBqP(-xRyITIesAHD=C!Keb-7VF08E1y-<45njzL='
        b'Yp-rqC$9bG5XgBtwid~~qm;8KNpc5ZBO?r-*1aXx)$Gul{I0CozIQl-+qzXf&){B{atJpWF#WBo1|lL(jf*ol{lk7JfaK9_Pu4MM'
        b'enWAR16^ora3gXZDVzbkllcLW{j;Gs!h~*f)b~weaNNu3f8R|;@!3D?Dt71-{A|`7<&T~IEH0*0ync#Qz+f?L<JO)@*?T?a>IP6N'
        b'G^bDTZ@7e;RGiDVwpL;)<4BDepb{beBN-J#R8>?1MtfDMrS}uVrw4WWb|}BT><9z91_nAK^KVXWO)K{Kxg-L0Cg~@&<pts{E(b+{'
        b'm`?`~C1Ri?#(~~?G`Q`M;rp6v|54w2HMKywqgBs!lM$weIiw!;+@-&YQq_Og|J+Tc`j&AZsp6lfY|v2)&+2b<1Nv$*6=Y0*ceiJ>'
        b'n{O;S&1P7xWk3DIa&tuK8;R-Ja18hLPcfIfH++RVdZ!q!+rG!ki-Bvo)|7>=KDpfu(@Q;ZC^%AorMr2gn+0u%Zmr5L8+Rw`s;Xr!'
        b'Ym&b8DiYt7Abo!$8%PN><$ejm{lyf>4Aavc5SosK@=etvwQ~LW?iXrZAj)$&%<v92&4BZW0lsc>37fSZI4gdWgNh#)>uOa{gJTgI'
        b'Y5Ko)gL)>i78ukIdC&a)gG8D4=$eLP^hLAo#EvFi>HhaUA9Oc=+HFY8{*Var$8j;Qi$^A#p!QAKzPVE@2#8j+F1^~K?nE|L9P3Wq'
        b'38VFGY->FZLdv>>w`x~`!gcJx4sO83PhkgBaNpxt%Atp^!8r9y=^a;D^<w4OL-z+&{)g9|9S7tM$>4WyN^T_h&r6jPb)Gl6)6${g'
        b'p7*=me8YX27_X}077;0j;y`8YJ&O2paGEd5r6ENyi0{Glj_&Q_rnyKx?R^zNxThiX_U`R!u?EY@-m0CSle!c1-Jh_W2t@Tu*rFa3'
        b'e-2x8cIT`^i@w?ks4j8L?rtP^CEeR2#Ium?<hDUeO|M{EwF>sr6CY&bj&mHdsk@{&S3Es-kbe4vv;0`AS3`Fi+n>{~fZvCdS8EU{'
        b'f4D=+<K4i<@^Qy@O#c{&UimmF@&!ZRgkNPZ;cSFtb+KXkh)LZ$?nCISOH#BtO00hv#@ylYfDTQO;J){!pnn6sEB<6sKYA5B1+PNr'
        b'J}BIbzSS&sjB?EHyPJ)u9pr5G(_7~W`}t}%<Vabc+bQ#Ydb`!Ba$l-0yFAi}?!iFc;;%TuzmwWL-sPS9P>Xdr5b?OQg<3u^q3`c9'
        b'sDp~KaPbw+FgFe4Werl1O7$+(Hq)K9#dVX#<qF?9m|7D7$Ae^qJGI(})_**MU0!Qk+|I<EvmWq#+eOaxeuJ~ps1KdEBYMgc(S4E1'
        b'Vx<`ut*K~mEYA?54L^^fn+%84Tt0~f2y3eEeGX%0bR&~8JHrL>qa3FHxXW-!U?4K$3vdU+nSwyp>s-oNeYit7MMgJ<)U8#vM>zyj'
        b'EXdUC?h@-F)L0NJH-~Aelqmo=F{yiBMMi1XDBCMeN$Va(@IOqVw#mD5<^@_uiY{6giQnchf2A@W$_!2dZbICHrsztguXj@aFJRJx'
        b'?F#YrNu+OqA6-{V3Lbh~?Ar}vQ3sP%EldVjP8OJj;_m^w#_P8860Sj3)0bC?ta+xENer24)yPCE!geMn<`f_c?DtsC4rFs(K*c;0'
        b'T~HuUQvVqg(>dOm1S(J^??WZN4Oq%?-1ImGvs)x?Ix}gBJBW%k{8|j`OoN--BEw<A_8h-z*tFDFJqZ=BMHZg#MW}e)S_PuvS@@ff'
        b'Gmh-O-=m2WXgJE#;Jf-O4fR07LdT9to`kh(AVFM=txZPle1``<`5WN3065LGjc?~#WRg0bKy|F;?auYs+5%L^9==%1Z;HJJ#eV15'
        b'G+jqEs^baNOvgHG?E$FCQ9cP~D47K|sOR8SDE(_u<|=QG8pV%Il3CN-E(3J;`7D!Y0_797Lc$`48SooC*mPP6q}}6qa1tiO>6E7-'
        b'<zDeJFc1x-0!Cj9F`ZF-)nzphS$eT?@*?D^b>FFgh9v2){rf*xFCqwoBW)7-Vg{bnoIB<7ud*mNS!|fp??n9s=^pb{Ot;UlX^Ags'
        b'((+^Z?ipR);Nu%MMQ?WB@GqWnr>m3`SaT2zG~;1)U9a+RvhU^Fh;3`HPB+{L@@I0)hWeoP08ah=(1H|41WL=lla>l;sSX87Bc|)t'
        b'Cqr7gV<t*__zv7XkaoW#cv64r4pbtfJRlZL8i4i45;SCf>@juy7xyUu$uQl%jky3u4LsBT?hd}Ft1i?rnZ6shE0v~U)aPW>bTI|c'
        b'zSuEz8|s%|ZE8??3$n$#Zev#cRRUj_3oS=0FF|!Dr;<v=OK*Q#D5UA7?KVn$l?*rAmgWhsKC8V-YqB@fGP*FEhS`n|qK~dgR9jj^'
        b'yA@Z_zJb*MVgc%tc4x*b!0y2`n(&T9c>{fchQQO)1;45Wd!Zt{{RPbjQ)^?z^KN6*U{@PuXrZ$`@~dUznv5x!#l5x%y>zy&LFTn('
        b'mk2(t+zS>uN$U(CTK9lOM-ucWQ)ah7wP1%%RjR+(WgxCApOY(%avPP-Qui8;PUTv_>CFJsIM<>o`wuw0;C$PtRIm+ot5oZBLfd<s'
        b'Jy{Nk5Y^x4vcBC3p0aKg@{}PlBUNtwxJ$P{Rh28$t&*=xmgNEu^NNECaNk_4u3;+aWz*CxjQUHLfzDGtCoDnNq#j(o_jd-hz#k5N'
        b';{yG$t~NTaMV(D2%?9<X`bf5`z0fdKHs<!~Xmz#<npTjlKiZW;!;FTQ^$F+ez2$Y6G0%7Mdqv7~gL(VA44OP|VV+^r9Q`|8CF+N^'
        b'OEt3a!=Zq{tI2Erq>J7(yUqP1iSKHl3$mG&sHC_LY#2H_@AWS9C5$cGbd=M-(PdU=UoTWxKLUNaB;}yA@Xu2*fAO8ag-n?Dx@<7*'
        b'EtDCoOO-q1`id@RG7EpTq1I<Q8wp$75_AS2$`OCtpw8AU0QYu@zM;!SEdjSPO}77iUH<cBTXcHig#b4fsL(^+_vto6<(VHFs3q3l'
        b'b?P38EgR2G)|n{-OD)M=DKlFQHtVvz#Uc8qyIksfZ3XwbtjqLlmzi3kTYw0uJfkn}B1JZ}$y{KvS(h?Nolqld%}&`KqPIe8(%6DD'
        b'vo+fq2i>;BW;HF{7NUO)aHZP{(p^@QJ|DGs=@00jgIAqi_cw8SlyB}NL8R-WI(h#eL>)IRyscl@nO~s%w=nfN%)QU%M%Ra?Mv)?&'
        b'Wyk#@Fiw?O!n$2kN$bTsZsn1k25PC<Y61p8&1UN|u$>ukr;S?5T7gDH9cx|Y=s-4VK^Ig4<B3#Y3(klKIsJS@&xeI~d(}F$!Sq)|'
        b'PY}?f)Bo7<D?OpN^@&|Jb#}@YIYFf9hkwm-gxqGSbeFu?o+~WtXQ_;)<FeexRCb-vMWvQ~3u4{Gi*m_(9LPFI_U3?O-{19YZ^ti^'
        b'y_uKnXJ<@HHuMn)H<D~?@<l2c<om*AA!ue02Fq4?UQm~_uqYz^tsroNs;Wwr#}!Iek-v&Q(vhgSKZrm0vpGeTn_8`-(G{^raQeLu'
        b'R2usSbVT8{shIWRg|{qOGpPQ~)X<a~5rON7CHGQeord>5$Tz1i_)#6Vp$PZghv~0&5`>;G&Zj*q;@^<#`#M3om)da0?=Y&jlP=I('
        b'{hf4Nc2F1YGh%sDouneyEVC>SA)_rnN^7yb_rWIHk8!wZ0cLBIY@$^wcjT%{EhQuvbE`K7Q~!YyT3Z}VgBwfvJ5_2Kskm%3Q%U#Z'
        b'tDm1i{j-w{r)ivSI}gf)x(?l$q>7X2XqEC}aNeh#v}SRoLVW(NYxp0NUT_ql0izrrrA~M1ogD;z@2~xH;8v=w2%K~uXTW2WD@XO8'
        b'1>`J|Fy8ApjlOkIjF?7|A4O-|j{bceKQ;lBz>_Nv=>PT$a5B}<>HCO#@`qedvjy3{zjLI*^fi<_7>b)}ra=FeUDfd#n0mXDro}~c'
        b'C`-+2k1+lD7OfT0w7fmk@#ZaPyS}FL%U;}3kJ0KRGc_+R6c_Kuw5!aa;&?yqbKL@YO!)zK%(=DIkBeOxLCn*y{EfUlb4!5-q5m=*'
        b'6HI7B^)Gi4#vte#^U;?Aq){)y*qcYwNp!J*D(eJ&?LHv#S~HasYN#(Yyhx!X@HDHVlg49UcCnZ-CZ{tu0yUF*7KZaY!kDIgl%@rQ'
        b'QAj=6x#-`;p}?EfO5E`(HftOg-<<H$DViNHQcU;XCh!z$MMtVl`J9TTgJ7(J_D9FPqDTVzZ5{#gXEA(2J=U4`N+)0e@PPJ%PA81%'
        b'6w|4Ks1+EIH0yZ{OD!VBfM7#J6zw+ZAMA_=JLyeqXA3Sa#c22M;!|<oA2BEz|6D9(0{JZ}h|#BY5_q~nor|gVrLIhIg#aq*iB8oj'
        b'P-aOWG}NNblpk?l8%E<tX4z%}XJXXae61mV2h4-F^z%FO5;|!j!z@Z7mAP~)DN<Rgq1Zgpx<^F7PsnYh1u$u;R;d8t>gOK=RtJ^f'
        b'juwoHhf%PQitSvaNu^g;<GyoP%3pEc`!M6^ASylyfAlE*Zx|KbslTg}4!y^qh$X{yPz`XWx=AenV)a+AfNn+KG+UD>d1oqKl%)nv'
        b'1&!m5w<hwwxPoke@af(ck4)sf-Vxv+CGPaP>yNPw9*yokpxE^eR<%c_OjyR^>y?shFjFjqzA$Yn<{e+!1Ui)!O5j06R*-2cGUI8D'
        b'03^>;%F!A^X~Rf7VL_o)Vx#71Em{D?2$N9!6xj0fl!w37M$!dIjwjI=f%t*%Qx)xJK#~ZN5G2L11=68hswGuH5J8R!jtcI~4ds<='
        b'D5gH+`y=EpeGYdxIQ>664C)k&I0rrNV*&Xh+P!#h3+}7nO4QjD-Wk6WY}^TgxF`3oDooYaD6V@g{1D_X!~988Ngw-yCJ^(-aMS7u'
        b'>Q7e)Vj;h0g&5;IJOO2L>r_PMLxq*$gy114f5?FQnn9N@v|SQF)NG2SO&S~2dUUeI*9J3x?nh|K&wHSwrC@nr?1+mwlybRaHH-W1'
        b'pUC^RBiANdy+`VgomwRHUH=(4XI3x$U={9ob8^3kAX4;CUg5{)Tr@WKOa_%K(z`pT4gW=)gPkBlylw%|R>%H^whBa>`I3MPrI*A)'
        b'8ofkARdqn$?<`0p@O#J*OxK4lO?xT)P%>_MY0^wDtqeE4I0<=%i+qc+V(Bc6en&@MO9zl``X>jxGxLoF(f}QdiDw%-=z`^tYg-b#'
        b'Inc&?`F>5fU<k$x#v`WRaai7cJi&Lw%w(C!o47K~k)_<CRjU=-7QKRGIu={BV6_4lui*0T`9(748t}DSu$jIf%n*8y`8^KFr}>^T'
        b'Km3Y?e3}PClbQJ*G93LH*NX20Uv>_UKrumz(76>fA=_8V0U9j8X}ivRk59+x!~PfC=9O|=BL|>jaJco{_tQS{Ra~s$^pgJtz7D|O'
        b'Mc}4hjuermw?t;^{bbZBQQ7TvTT~%M8&-l|%2MFeMe2S`F!!wxY~Puxx6p|@m-YVLH@+u~RBmLTkLB&*;@Oi_d<Qx;x!x3od{Jcv'
        b'w#JjYRtL>}OG3BZeq0i=)v|S>G7{`8eM|@RZq|A#tHVrVWn;Ot4)pu9o(}IY;Oi~V&7>6YC&r=(rR4Buj^+I@PzyT?pQUDiFa#H='
        b'anmZSC>eKHu_DD<{mAzQwHWOuOn{_(cojF9G5tTjhiUwd9Ln`40vu_IzY5cPI$_jNw}2@+s`Gno38-kash%i+`RKh#{f#Sm!&m5E'
        b'NE*EY>eq{FsjF8EZcv$Fpjg~=D<~@<NvBrj-X}zt5OiJ1HOs*o;Z2kzWr@5wyrZsmhNVwdI5tU^I%dN_@r+*aw@iAi_lrN_fRBzd'
        b'9GL|!1B=hz-G1e9V#_PxA;~GLXDIM20;ejE@sn&8u+Q-khjkRl_Z6wd;VOBQ8lR0(%Q1Yyfxb}J@A%#(_!wGOLd*uQa;0j^E0KW4'
        b'B2W2pCUX%QnH8AG0;u?V6Tue?g88<A)AvJu#+~^*Lwu0KXi$=_5zY0<q(>YhH__mRx#fA>bc$R0TnMm^YP<s6a~$WWx3AE2uGWm<'
        b'=fo47{<ZJ(3);gShkiCg7x-~g^3RC98^6D^hmQMJPimhty~E}0ze4T40w$3Sml{NK>P734b@r!)Am7$|ujq6_6&UBmXt&R1O^VyM'
        b'b*&H7_J)19_(RN6px3S<mFBjA?}*(0?6AD3quaVv1=W^o_r`R^N6BDN0^CKI7GvV0kiABq>n7{SeJ!Wgs_Lr!_8H2=>q_-}(rA75'
        b'ipmUpniW#A_0o)v5;=Q1pAav2VH@%PSbO)drml2xc;6C2veg{|0TFfY9l|A|COax<wM_yBL~WB;@Y41i0)qB3=ODG>v~(tkoro5v'
        b'5U1m%_Dm8>y|h%!%(V8x3}B0>pnxK%V5uFZbEfT#b!^qB<a^f++L`k^-#_2)dmf&!*V=2pYpr*^_jSw16ntsN-Ht4*RGY7UI|l0R'
        b'`bUZ-{nvzb12SmRuM^V$9J4?7`3C5{wxHTWNN?XFCG+gFuRIVH-lexq{;)PKJ9^?V{d>QE<GQ(t?*oh_ScRJC$j8#s2<cO|)2rm('
        b'CvF3Dup?IArhNxORgGuwrJVQr5Z(<7t^_rTVjbpn+y+GRyrizQvHRYW8#}h&8j*vW)A8*s!;;VK|M4TO8mym}?q^r6pow(}M8`hN'
        b'!_5NHpcCID6st;h?X;!uWHTAwIr}HEY9V#B^Ipo0j_O<dsR*)2)?nPc&v_yPAuGu8=2fFV0eqe3z8U8Ga0ij2{sqqCtN8XXTe9(o'
        b'd31VF?C7WW7QW(L2W{mtKBx12e7<wa=P89dVm8&zR;*mPf(JStS*bj*ClzoTYFou%$tvk%Yn~AQYv7k$j47%C+d!5bU6J;-RcoG9'
        b'EymEwKkm-3gO_$Cbf|7e*AE{{?waB~akt%{6l^oOKOIJkb>yD|sinW5A&DF?+teP6OZ;4<Hl3aNoHWP7_&8^NULqQx_Q(}F<k04)'
        b'zb+58G4ytA$prP94laC!UR(w3{`N}n#1HhxZ%Q_8D^V1!T=8!eiE$&pP`0<3fPJ>tkp-BQfg!2bHC-i*h2FrsXm9%3Oxt&$M<N$~'
        b'LH2&IYcjk<+1-6@jBAIBlwr}A<T7l$uMLqObpMEg2iQ`L^()}XE>*|iJ=*%RbkkNI$zNV2nMe|I5o}4WSVI(Lh>0Da-L<{~-;l&('
        b'9pVKrJU6QXwCAD-_t_QN3i8B$?8?H`FG~T?xdc)&7kD4OfiFP}?;7hc!Z*8;zkznuZHBiDChzzmqLDmC5))ZWu90Zqx8pYGk<gW#'
        b'73$|NRqQ0J>m#F$_m&ghuWzD&w{w<sEfOT$Y+qTD&-u_#VoRNZHHJcV&n%$s4vcc{x<V)Jme!ZImZYO|sd(o@LkS>V>f)?-NZvUM'
        b'(IMgeF2a+wU2%L_68GyX0-sf(nkEqM#*{(d=W}a@?@NzZ?SI|N`jxc{DhJO^r+uF%Iu;_^D`Q2}kJxsL^ImaqAUNl6%Z44!*+0si'
        b'7w*_yS9nRSy3a14kc+YO$QY6^Ecl})HjOPkau3B^c&3z_jbbjm7;`y-D96L)G((QS@<%iv<WV3-^jP5)6!UQpfzA~_TvRz974vZB'
        b'5|#qZTEe41jPt20V8psu$`(x;h9T+W9)aglZoVl~$!btt&d0Cl@52=Q1aDstb*cMiI`gmOsMA!0w-M9+@*X|MTZg(Iyp^6nc=w>r'
        b'S7{`CI`m#zc#F#i?8(wpG3Bq`%X&-dxe1c1rg0@1Q@;IPR-W`{H$A{Bo0Y&T+{0IXv=L|B0TaR6d6RqYN_s6J?YL>5d&PNoXoX~+'
        b'%^EgI#4?GuG!nr?h|lr2j1r@X6rYv1OvDUYO%qt!IT&A+#84OKO}=BoXFx_>Tu0&^mV6e;!-P90*2{Qp{`(ff8+QlXjj|XiDWgiF'
        b'hSl<WWic_BRD3SHhq^b}7+7)z-J78@7i!E)jpk*!=Eqi;m%DEcA->POVxM?r1-?8Nf6Rz4)8I>0c%h?IVwYaw7F{7FmK7F^wBROu'
        b'sXZ_ZE}@;c;wX)^M}`??*da+#SqP1VG+HS23wVR#itXueiBea>>q?Be2d}sr!#pufEf8GBm4N1oiXdz{wB8E}s0dPgAXNk<K2R}b'
        b's|<e`whs-fNQFkSj7zz~DuIVsmXoVU6H?cbIV|w6Mar<?bm%m>^P=5h@Is^~&d-CsAXOpJg*5Zfy4CZjo6x&M1lK!^ESfSo=u*4n'
        b'3K+4OjVH<!To;JPd=7_>DLCxP)-sv>#4stD1zs<B!Y2ILO-zh~SJWkRbSb!7!}i*t)m3O`k|O<i1=li+h~WA#X_0Ur4JSS?0|(Ub'
        b'w_!3@hC*@Q4o6)np34OW1zVFlI!u!!F`KI%5*~0BLs)eYZ}S}iG~z!9YYw6|2Yz_vIl?*@o)6le9TJYGq7}9CR%-<OkfTC(KkX<Z'
        b'1V1hmuQC)3MeP=WoSH2qtnD`qza9ol@I*ObO~vTMs<Qm_7v|d=hTVZ-L6SmBa=?!1%58XU7%WeZWGchx1pM%ZpAD-EVua&*1iYGz'
        b'AuwES_$l;ehTSvlt{$fIp^#59RVABId4S!tJw;JnU92P}xnx0RwW?ern+szD&z?>sRiTmgXND1|xzJ}Z$m}RDzPE5~N7E02CcpUj'
        b'4~<3lQs!6>{{TYp)h%ehTaoAZGV#b5jSM3tq;Q-C;fWw*Ye)<prI#a^`u6Q;MIdRVe*(Gs<goKssIMj9l9v^%S|RLzI6EPErSTbI'
        b'zb^ZA!fU~V{d3@<V-_X^FJ-^J*6<iAp7=ds&BM6(A#i2HkwEO#G5aP@rWjTYgBjOlvF8tqhKP>K88%pk?a#qDXZ~o+3d4r#VWCuK'
        b'1t(;`1J#g@tuzY4{(|fTn_=GY!nqkMR{98QIg$Q*!uvBUWih0@aX6%`=~xB4IgHU#=__OK`IFfR5@G*~*{^p9@4mHQE}ckA_3O5j'
        b'=r=ki4-3|#g0&feeLX?+gawr}`%9u@`b|UJFfA?3ZFWu>7Sal0o?pO?T-HeE*@UoO6fx4fKX9?b8jFtmuOSo&sVKmd$s9Ed%~e@4'
        b'vqALrN6>1>X79O(njf?7fuT@4u3LBgkTQze`UAF5yE2aG=#OM<DJG6M@K1UF-IW9o>`iVFLShEN&SkQp#P%ON%Jrq(0?-0AUpF6P'
        b'KytG)(0Vh_1JN+0D3SkvQwA4@{zVzQclm!;2E9WMlmTdhU8NH_W|-%(XrsMP{lIk%EtHDUxOurm_Bsh6{S#iogjE(pNj&@t#i|<a'
        b'(;=Q%s}AB^+Yl5}5z{n8Hl_p*dOC}N%$i49vbm3k3`fvg`|TkzcNz!*GIu&ifGGP*y%8bs^K2OJ7$W_*Xc4>+_*tnRLwKXcg!fzv'
        b'csdc3aFrjctltP)-RBg#;;aYn7)FKyFASy7`roo{KaykW?Xx)lko}{fc7WZ*bft7eaHy4Aec8b;+4l>~wzmSt^cr5FC9L1!T`%yw'
        b'ht*2>+=bkl%XZ(;eSs6hlMB1zIy|?*sxu@FMZ=0{8G_LZE_=WQO_g53g@C)1%Y|p}g^0B%0`jH!hx4T<f^RH!&Vu1~{5ae;J*9t$'
        b't!F6*XN2MAmCZ&Ja`JG3jiqXSKf<G{WFVvF1sJoQ`>E%?2b%|mwe^06<H+X#qghNkxE#pgk30f|3qZi{cZvBP?jcmN355YFGn77V'
        b'5sbCt9TffszH|Vch-L@0$Zi|58I?9fY>(Krmqogo4@pyw(q1?OL<M!}?^i8=q2Qvpf+2Omv!apCRUK)m1d(Flz#!ab;hr6`n};?N'
        b'HP<V7ebxQhunh}`9O(rPXI@=`^wzx)m)Gvs2iq8r^HKNo%P?T}%prO*FZsH?DZ-ltJ|We^J<8jYxWUUo;zORx^Ji|U4>G(`UHOr+'
        b'm1mlHHUuPoSQ$N6k+-YWInQzxLpe~bp4SWDBZDy`l#b%}QYh(@--Cge3&X)p84|7cIcSX1u#U-hc>G`$eh72}+WV^sV2LKoh;{(4'
        b'^Dx@6yB0s&vFv-a@Xu(y7U2{_G2au?G%U!^Yn&kgC&~Kx4?tCz{;xvmvSJP9y>$y|vtM2w*Jk)ZXXLV@ec?!v(pK!+@ZDvhU9XZ*'
        b'Ag3Mpp#|9>>^-09h0hj31_<*7^R`##k`!i77Nl#DPRUDFpJS@pQ_$@Un=~;*)o0>k1t}#MA<Qsgh6EaoZ~VvItaz#Bd$d_v1r4!&'
        b'AsXj8=fO)hX&56=gj#CA#%D)L9?XuEJPX5YbX8J7ht<mF3Z}AxtvOa-2?pwHsK+H{)VuC)m)pd+)&ZU7R2@k#sb&C<2MDb~>8fT*'
        b's*xN*hk;ZB1ud$4T3ND=b+uAe??ik+WnIe33TDFxms<f^D`gXtKxi9Yy#zUE&ZUAebt*SBUvBMS>q{tog|f1XDd}R{?dw}xZ?v|X'
        b'X?01LzO|KVcN(4VT&_whNWV!)U&id`FCV>n*;dU2HeIf&C`h5l?KS`9s38Lejym~o4rxkVzx}<-q%<e0qDX6w(|O4@FTC$d!>-Fb'
        b'pqE$bG#Y}4YJw6zOp-Y)3l>uj_u6G!x$b!|Tz+=Rl&Z6N!mdPJi8Rc_6oOjSBTI5J*M9lFVJp{OzMGZmZM}gGAScn{*#|}>7?fq^'
        b'!qJ8E%J4$49l`Ko)8wT2QByG7_|QBOf7JgGTOzKvbyr=2=112mmvW}ik+J6ABd-CJ1juQRC^haY3CEE;;{4X^5s`bvoX?}|4LSql'
        b'f~Ypqffazs9pZeh4XKKUP|2nUj1?p+=OMKLasdQRiOA$IX!d1DPoO*TkfeG9lm{eDTBUv3B~TlXZ_m3N)g1c!RfF2FC5OQ_j-o#O'
        b'Dp8^g8y>l=A#+5`$^f&F18BvxVH3B;{mf-x5L-@I&+9NM%(v@pcwuxbEa3DX(qlTvLm5Ug7YFSPuHL(2bRuHZtpOh=ppCB8fy&M7'
        b'uB|cU$M0s%k(S=@T)?YjtnbKc_0>#O0b3<aDUOjBleA&#WyfcF;KMa5NC^&bF)CTCOGV&d9Wx2ZQM<U2pNASH506(3bb;D(KLw>>'
        b'&={qTjVm+-!lTpC&_S=kN9N3zgJn539-hZ}&e|8@43{AX6A8<j5aH%u{&5QjFy*O;R9tOKXZLYJ)rm;;Qxn}JP^xh}c4jq#?_QiZ'
        b')^R3c_~sHl53~gM)~ggGX;hIcDv@gxj^8aV9+RFxaQ2nCZ(K4G1`Qz~2u2;l>x>qI#v*XTmmI{}t_11dWg5Z&su|v>i0K*&Dhtn0'
        b'L|yhu!=Em3eV4=#tB#4+k(PNXOSUz3EMp7!Sl+u2teTD+H#phlRRo%**D~N3T8nNt>n@U{!KRM-zX}a0piR->hyC^@*K!FghkZtO'
        b'*QNVGK?4cZq6dL{A6~BAS4Kvgg`sBs%lr2(IgXqKMI#W19t8{Qt+|K9x%JLHunEKWkm^pCSeY^OkS38%90Q-<D!Ge+JMM4_Kaqgk'
        b'mrfhQFc2To6!;GsV8i80NMn^2cpYO{PRvgT%kk5ur+1c^Hr8#_`_No&@%(+}`b#Nwp-=OIZSn5K7ttm;NtQt6@#b0R1Y8-Ps^;UQ'
        b'Y$_!v)s7=SuaD|S4bnxN<5CO7wzHt%8dIpc<PP?Ra2~g$npUZn5CxhX<LbC2{Cq(=<p#zh`!+9>o}V^FroMyor+@f?pR4$oPN0cq'
        b'?UojTE4~<PGiCTj2uvCSZP(g3$Hjw18C7C<s_u=z;Y%sBdn#(4hs(OTem+-v$-zIm@3Uoz)vsrPa_ZyrG5=rN`Q;&gaZk@izyF5y'
        b'CWUd2UJCN|y2B3LG<Uuza7yjmq>Hr7K_t<MilR4Vwq0AEiuG|bXUgi+cd|vy*4GK?CM;uhN-Xrco@ciDh>ndImw)M?1C;nEcDM4d'
        b'9&~nyo8|X!^x>ZdofiJ|Sd*;&z)p7a&dR-v&-ri_H}h_6MhwfwSHxv<GocAs`Mo<n&H_@#54wGU8W}R&Y-D20qx8C+;0(eyP}0C('
        b';`zl6E|V{tm)Wa+LE_<NBW<Rqnt!YGa2Dan=lb~|^pK?+I`T)qXjl2ThmmOoW0R?LjgQUx6IZ7+N!*T$(GA8|2hrA{FY2CYk+|E$'
        b'G3K)DF_%`BN;&3IMrmdOH}R6d%>+-hRz)t>rzH^`8Z5^_E6^Oj=1m2=duKhn@dLoc98CY}7MFhG2Rn%l0}7LPP?#u)AIgXm+L`$|'
        b'hkT=t-96+1VFE}6d6F|9Nt7azq*M}uYZ(N8!$yQL{8^GDH!)gn?xlldR9GN2aWw4yW>DN?92GZ6e1MeVzPd<S=5wPLJ*bWIRWb_0'
        b'!6Yb0Rm5U3rG!+2b5}0<#JA)U%F3fluQjZ|%?4DkX%stm3;5U4w<8Yc!w#qAWr_5y2=9EDheyI1h@gJ(8d6<_@qR4RIJ!$3oo<vy'
        b'O$=@}=qXkY82=o`0Q3~{R37?Y#=s$t!F~Q%zp@mW%7St|k0N8pF#avW+9<SKgQY~P7z~r<A~e-o^IK$l7BK=R0KOmtRAJ5YU>NJg'
        b'*TRv%d+uAt_j5jXiI%arpu-~O{P8}Fhy5aqdW}*z@^e&P%R11lDi8g$evB$dq#1LN(HvEd06{dh%_X8L1UuWl<)Ure&VIzcYEX2m'
        b'kY+SxDD5v_gpSt#t8!%ZH{35>v|9$(eMvYn=C5ubWee=jUBvu*ecJ2;lUE)6_rYL!HejOoGzA=`op=}6Y2n4%B>x(A*KWewgEeFh'
        b'2D}$NnI3;FqrPQurww{Cma7j6^n^ZVuA3i3n<hKw_HnuNl;#$FbMwaN(J>Bg;l4&6w{TgK{fUdajuFyc?EQ;G$7O8c=*szocR-wL'
        b'`JU*=!0an7u1ZKNM<%ZQp+V?N@jqn8zHqeVG_Tm%BC(q<2DRCZ)Lr`{7Y|9a)zX7ss0*>i&3EU2VOVhSphVEvR;|fdk)7~_A#+gB'
        b'%vT!;AWMgM|0YnN5R0u;Dec8Tt68>M)}C|G<IEBkziYTL5YSz8XqKxN3nLP&F4@|D9qrzw5IeeeBdQmISoU5*dIB4L<SsNe`+Ic!'
        b'xFG{keTaM)YWN^QJDAkjaB!8jaYEf+QDx-2t5&Z{5EjdXCDDUcKq>{DX8Wgu?u3g%!X&hRvuKil95bWdM%8?&7Z@A3N1O>rp{D=Z'
        b'{ei3b{e5>y7`g8*)x6Mi|Mhd<g9+3sroaqCkyJ3iY-nmu0EPgwpJxF&P@umEK1SSNLuGyr&-JU7HU~(%9I%~%hj@|vSaDGj-xPrd'
        b'<j>EA7A*pM4Ec4UOF!=ZagWrCF1<@kBE#&10Z-I0yD|v0=lWOL`=C_KeLBGNOkE!!r?X*jawrx%xEgeb{lXy6%`}`E?9<x#vf0b3'
        b'(%&ScTd;u;T9Lb~G<_-|bz?NaJEw9l4CYue9D;KS?@ZzTFv#=Dy3&j|o+sgD;G@C5?hn9?0y)v6+0w4lvwdu+?YYM4xZ=W;#>~4<'
        b'&hdu7`@awwEPJCG#97xE2p~ZVw1$(p*yy9upjOiM9|P;IO1QTM+xhv3B4k+O^Ao&nV}U0I4!)RHsPJXZS5NNtICHJ@B2AL=y?5O1'
        b'0Z+z!^)VvI&GgB!CW+6v6x{;@DQ>Apf$d6CHZ%>kb6NFWY{M@H+nrgSCGTpJ?po6#h%o;Rkz_|^qz_msXY17ITNmXoE7&@fu+EHx'
        b'w1tj-98;VMO0=ftu=bQnnh|NdaL1d5<fSM2R(8s59-ya)rqB#p21T)B=gLp2tWzVNe!Nec-LB0K$+SUPYU3%DJrSgWD)7dD+k~pM'
        b'#z!zZ!BO~?pkV@2219Ql<|@A^k<N`^hGhdeW$JU?J}ztPe-n^n`1iq8JJY~A6C!9GUFrZ@60nD{slq;ImKbJKVEVoGrGr9wjx{r4'
        b'C>+cob5=<2M3#Ag3cQQ)Wj^W8q2cHdfwDM*c@Usvs7Nza5hn+2oh7k}o;R<VokFj2v=Cq@tq!=u7sT@fFy0(rT>TW3i;_Dk$YteM'
        b'#d8Y=gM_JEc}Kk+69^MGV^FYU8FYj8;Q^k^0^tA#7Elqtm|eNq#LWgt0yLJW&!N~1DqS@hc(+Q7a8!z<fe!O5n$)ByFOYDlgTc62'
        b'93ae|6m+DbRfHp?ecB*eSi`G$<$52tK!|!&AqL#s%9oHb0gozl<Q@vdR5NTf=o=TBp+U+<AI*5aUJS%UQ_uYa{)4&!1qvDmGJuEy'
        b'2ylJ#{UX5ZF43HUBqC*$^K<Z<AqfP{rX$|05}Cac2?XSeRf)bBB%>j`D$y77iMj@Qx#7PDfFGj#UMZ@Z4WC?ys+&qt-E8<`;DNfS'
        b'ywCC{u0Fy`n7X*e6e%}6AaIL4T)w#6%j)9_9NZG2bb;ZI7d)j_L1Xom&Uci~b}t%02ZDseGr35#u<7goS_CBt^7G1nN+K;$F6T}S'
        b'fWG|0fKW<;{pArc3i|s)#wF_SC_<xwt#SSRBR-=U_wgyF0G~zwgwLXX#pk#}zmLx%5uZhDRCgm}{@<wYodZ9r@AVh{MSbrW_@C<A'
        b'xiG5150r67w+{q<Hoz;^X3>11Ep&Q)@YLh(MTqEWoqOd#)P`JFs^DA$4kCqne!yXoiOWdT+)D#}_@^YHZ~NT<*1Y$i50U7KJ3#Uu'
        b'tmlqy90;r*NLdy-opI{0I}^b}CwAlxL{IE!M4ivdep<mj17N3e{{~=Vp`x!!Rb0gYz1=}f<5okS+&ynV)cIK(N(Oe7%N*%R+=>B5'
        b'sVXDJ;m<&!>Rl+TF8wR!@TWksV<t+15m4bn+ga@^1{(4QGKvIAZ96xMR(ReW+3ukeg(VxC6hhb7u)=j<r+#2dW^B)P=7Ze?*pr6*'
        b'f%eR}9I~~On*SZRLeGU;hm?LJ(}N;~>b`(Gy@l`&;hw<HwhDwbiA?zmcn;o8MEWtp>cdg33y5gEe*=N+=+y*g9LV`@KEYkQz!Ug4'
        b'RUR&{E=l?<Y0nzq*a5-cxquh?afjBlS+$y21<q7eDefpG<_mz0n^y_x2c&@;aQI7k&7-J)r6gK+9w&47Ei2;)?-5cvEAGLH`yfXT'
        b'^c;r&+LXAi<PQD@I7Kua(oKE!aO09YJX)T<m?RW^M5X9MP4ynR3vyhW7&lX{zVu#;Jdivv`q&+J<N`^g*2>6S{mS(chgRw+!?&(C'
        b'+QSz-??rOZsdDorjq@3Fbj(>au7=weLVnk(oq>l24BuQxp+5>a$|(1{{U{9j?S&l4%I8zut^ML>hQD73@#zlLtRSCe_~L?NMe68n'
        b'%Kjx3%71>k`%f35g+?y~Nt5B?g<x)$;m!V#3LX10dNd3<0!gXAB#&wa0$*Ne_s6?;qDl;BE<8BtrSTiOcsmy2(NQmrmuRl@f?-F0'
        b'JJ0l~N<xG_$Sbw+6Sxx>1THIsh%SwkzC0$b&q2{dn~SRX+95_0U9TdpigJD}(5jKGMaC2GU9D(50pHb%C0;;L?OFy>U_3=b+Nk_&'
        b'$cRR@#Sbja;s?lJ0@Ft{4Wb_b+xx&Y5KkEesT$-S0?C6ykwr=u&wxe>fh1j{3^qmlkaV!YcOuO!)h=?rzlaIEegPy%t0+uS@|k`}'
        b'_HmEEbC8>Fnu%nJ-$n&?T+kOO{UX3+5)|6vnc}#en`7wY%F1}hiF-EP7Kc&|1;FpGf1P3Xus*vwEt`;9$9VG3u00I8`vJNj=69IJ'
        b'9R6u&hRcZw{<Q2kv_6je$ps*0J@3jPR>cX<#2h|Da5$3$=VacQ9BO-#-mA?~NT+}g=C43=3n47s_=Mnp63xdXMC|)7@O~T&{Lv|Q'
        b'3~MfImI&u?J~yj2;ity|@Mi6*xknFQ`01Cc|FP{{3f)AwpAZF9A}#T+-01)^iSKVA1kEz~qg`c02OdFptqA@~R8IgNUW7`lcgMhh'
        b'3;Gp}a}>e0=gJfA9DN;Vh=FH!z6dRWTX=yc{b)(r6uu9y;!;+(JGiN!&VSk`wCh)Ecy5|^7sjXO(=kH(7@e>qM*j=sBUkTK@a^A#'
        b'?^(T*@LnAY;;W#)<(UdY#swZ<<sjqHT7w}l^%ASNB>s4kqfA;=7USS13taMQe!ehDF&*c}>|dVu;h%y<#Y?6-B-7YT1}zg#yx@_<'
        b'?i<_}$}XL(ipeD<bCFAoO{f~c`ItQV7szJG&jYiBPJl-THw(pUY!}ooV4*gqiO@byIEXxTW88@{Lb?QN1h<Auf`$mr6sX+coPt{6'
        b'oF))?4(HVDvKQUUF9f-1u4AmnS=ji8Ifm2c!7aCG!Yqas2%z|v9y46;2M0c=nM<0dsmz7iPv#if{%0`;lWXv4hKDY&Y_iQL&Pp<b'
        b'SA$NuG8{UuB2yU#-Dr=_vEDbw;Oh^T%`87m9sO;8;Di41A0|QD(HIpFjc-bLA}_l%nS0~B3Qq>PgyA}qAAMN9dk*(Xf3S4s=-brM'
        b'#{R&e{?Y4`0;l_<9pwF;tj@KXm>>5ep37(7LCXeT97E0UcB5r~@fV<VEGdRBFGd(F**g#sD}S=lM09+O%v|n+eo;#QztQz!>5>Sy'
        b'@q8$V@%%FOW2Sg1E|OJ^d*69vhPTxK(Ur>-_AtP~fW#ZW4RgW%DlG;?1_a)|Sqmh#4Ut&J+@ESPjUDzev>VolCJtxe=|;QY7Z8vA'
        b'WK1P7kg-Crje+*7BtqMB{a4$bBh4Bz*4THd24%)h^MAyW=2TK*5|h(O^Au8IhG){85;)bb-9bp77{jUpg@(EP)u2xn<5hvB)xd*A'
        b'W4vloqgN8r&VdR>Ywq|LutRGMp8mEK{Z}=HKFyq?AN9i<ts`fVyopG$G-i|OK=1iuqn|1NY0uZQ{n0&N+TSU=lBJ&O0{*E5|5UG`'
        b'^vx6q(<e#S$2gcECIi*Xvz12N6r#}l@W*)Im;KElw%w17UI}yM{oV2qznGpH3@k0b8n#k@$I$eC+*CA=x(Yn#TZp$aa7cphjHdVF'
        b'h>p}TG*=FNnTh8FxF!8Lsw$!&$9O$1mFHpTX3^8Y^JX)tk+0a`etcNgr5Pq>k^+}UOSV3vw|{p&=wExRNYJ8qMZ0rppL6+D=d$a-'
        b'2(N*_UFzW;z0MV0<(Bnv%b%iMovh~w=6a2By{jClW!vA2w01K7F4of&sccfZx)}evY@?QRr}qbh{t&ns^7*0lGmqBvU*&Wk;@5Tg'
        b'N7wZql=a>{-!9G?lIGaaUIMBJ?k_kdJ1~Xtes`~`pkOHGV4x+Y{O5Gniy>}Skdv4Hg!Tlns{OdDnysw7u{9>XVNyRR2hZfxO3(nJ'
        b'8sS%`Ze5q*ZaLo|>lfBjpm1DON`7)`@I9nMD$yCisl^~4G9*ppsGH&<=Yw&n((@QvHUT8}UPRbG$NEkLEp70j^{wf~7{F`C+i0Es'
        b'{wGmhBfNak8${fZF}Z@z;{7I2rd;S8m`FU4RKY7$5(^nS2OU87(z*I{WfdM@S-BQ`hbnV?AhRDhtWi#IBj*L)-gOS`)46gkx?iK?'
        b'xA&?v_^4m$&u;bjafct%uiC=QRf17z?>}c-g~ACAXV!s4!g}Z)7&JKqcj>%P`e;Yvy@0B}(g;pE1C0O=xRD~j{S`9p>T|ap8ocoh'
        b'rGIX#zG^4hDbs$gvXWw|mHPQirDy~k0I%}(dxlTW^Ugd$V|QpU!>8vRWsgeh?|}e#|9nPV1+V7uc;Sc(na}2U5V*@oebiq>PQyaB'
        b'l0u=stE`5ptYT}<fsKD{+-EY1ei(|`Ro{>MRsR_G8~4M04Ev3HUH8L&)neGM`hM82`hM6C`D!`ikw5t4|AQa4_5A<z!`7Vp7eDOh'
        b'=l|Icv%AhmT`^LUBWRbUmlAq?$#qWG``P)n!t;UOo}Z7KM#5-lZ{Si3;4Lbx7*2k)<vi#K(mcx)1Xq2j`zPnb8O>R?1z{5@hfzBE'
        b'`}133jYyD5ge_(R#-h1IzKwzM?$T&s11hYMZ^37Qf;oEVJd-5Xm{T<pac!7+DWjBwI&rT=h0%m$a+u}hB>t#MVm|s`=QZXj8r%SF'
        b'zz8|Wcnp)HnaO3SFhB#yj7koYw6DFUEfJcU(n45&H#RzVTo!^{9G!8eE?N5Jw*nsTIO0O9)6MbV9HdCZU7~71ndAs!fvWSiaRN+g'
        b'9KxH3#!;dpa<|+dF|0q&T|5`kU<g{=ByBoC^Pc_o=-qSdMXH;G-11d~^dAv0L-T0D;heQdQpM??BD{YGO~4KJf&anB?e+EJY${dB'
        b'>sv*q5Aj;;LXci+3*{c@BPH{K8TlYe0K*|?A;$i7M2>~HLjS|@`d}*{+5gg(swE3S#AL_CLt#E+2{-}h%<S~@?%{Ldgv$aSx6mO{'
        b'aVF!cq=1mY`$a}>KhUxbQKEoo`S(CZBVq<hy%2SPqp1fru$bbx+28=PHi`!axCm&Lu|Xy{z&0Smhy7v>P_dZ#b9hEE#FZ#`280YG'
        b'jG`i<&y0?e%@m)JhrGzcnQg6N0I>@>wD$AoT6r`<Z;K`m^|hiEACHJ(&iSU3%GP$#L+(0<7JYOvY!}PP&Wq+zyM29QfZ&ORL1$i9'
        b'ocC9ExmWs{$mktUfiKRvcOkrV{PM1k%S)R~c=z5ty8T?>wR7dqP4ezSu9JmB$8dS>&ug2+d2Lq@6*_Vc`2N~3n%K4+xzod=r2-~+'
        b'2KMh#nkoTBY|Tc<=&4pdcLPLnNeR_jp@fVQo-GxzR$@adrT}XtqSfv)iEcw4>Y)jB@8RgaJO>DYCGa6@Gl?;Syzwb<$N}EB0OE=f'
        b'Sb$&w_OGW(_Ml`v&ziTM15tpU{gefebr{?OmL%ty-cp)Z^*J<);T2~3D`c8XH%^r1HBqDX@HdyZg?%YY>13X_xKAPEysI<($GJ>h'
        b'25DJ?txoPLJw#dwbcA1yrFcu^kR{0JtqI>^PtJ8X_0qeMK21KI($llCMbboBW0B)^@C)@C6cEtjciijF8J;|saVv9wS06Xw9J*d5'
        b'j;aP1*#C|89(8a(?=MSFCajNO+~Ph9|7hK(BNW<Sw%-DE?D_`t@QLcbjQO|)ymGw-MRDp!sOAtL$T;#bYwDqDuE2PVprg@*o{w1|'
        b'pqdbj1-eS~W46AMs;PppfK=tj>~q)QKa2>FFAPe_$1M9`EYRLAAVCWdF(AAYh&T^@<l}NoAF~#4<kFNT@yb%mdniZ)6dX<R+(Q-+'
        b'#SSHkg^NH;^%Vb31ch++AP8p7x%!V0ncBopO1VeOH+$hjcs8X$0k-)Q3T^g24kG;#5Ya9dg@zu0a0@)nEKnadU@CO-9#mvvM<|dY'
        b'?c5^ZG@dhiH~~twwo)uh0VaIT*%oo73}_Y)_i($@z&mqHtrT>*-b4ZWr7g&8pw7|LYj4vEU+1Uwf85eszj0`Z;#l)<wsc)Q`gR|>'
        b'9cKzvzl%~Ynd-jUdp$#~eq^FYxn5io2I#K2cx{KW{td>pjjj23WS<gp>)&8&HoLYlJs&`deeO2AZS^XlKnO5<jA?!y-BRZP*|3fA'
        b'{|*&FZt)uom_79#RLu2;GW1>qN<vqmWaTj>TA{NIP;Y?3CEJv~cOuamVKBgYvwf&+IMW9<Ts?Bfv!IM=o3bI;3ntzDV)OM-rlSwt'
        b'B65rk+1Dc!Pr_zwceyscDF=%W3_URS-p`;Bm3hm)LFa?`BM-XyHCuDJ`ELwRRn5meSJ>uZ2I#4^o2_}NxeGCNWexk>o#tu=(a<`!'
        b'`30rp$mh0Vrm~1d`+<uXARW_UwjO8#gkLJt&dov|9Pse6aVB>(MfzY|5tAD#mm?-GS*!%H7kyjG<(PlnXL}p*Gnhx_XL}K^!mERb'
        b'lTVZq(ws<OXWzp1f^hn;l-#4eJpZ!VgQ3X*0t0=3?vR>Hbj*ry`MrUKeLT<5ufm%~C)JS|35uQkNbKY#f3%YyK_~qWI{BjiK_|n0'
        b'v6I0gpF=<W6%3jvDrSRdmT0__!6QHS=b;|fgX&6U!4h>nhr$uiJtXizN<B3$=b)?5u?PLMKh=k1+uKUBu@{o<XxEt7$#;>I>f`1^'
        b'Qs0750N%t=OYid7X0$i`2K(5Sees^otFGHS>waUN)N4t7xei^tM>nn}?aTXU%CfkYmaH~9a${Gkz(cp>{;94p7{n~O@$Te46b+y('
        b'xmgxfs^dM(md7|WO3RAWedRQ@D#4Pgx0Fp<a?T==l^*$fNgiWaEHmHeq0=3y%Rueb9Vq2yt|~6|uU(b!^jybz+#xZ=lxs^<ZFD(W'
        b'sr*?O?AlUr1lMmVDOQ%MQavD-E6}MGjuq$ta`)L@$Er!{YAobm+oTvhK^9+?9G%e@B;&Q2@~$;NhzqY{7}T|Eln=E%M}O3qF5mZ}'
        b'UDJooX-C0~c+~v5H7yeQBP}P_Mkdno@^2OPGd)2v%b}e*BEeGR?k{?yrxAaS{yV?xaik^IeHQZLbWBhqXFu2irR?oJLI0RT@?n+#'
        b'o~@X&9oRDZGvs$So@MH)_|#?9RfP99V;S>kbpE;YO(e{J&0}8sHM-Ed`)jnX2Iv0Lt0Cranm!gwjxHr)(K(FB+wPcoqhsW6T`KRa'
        b'@2v?p(S3`ijkIiQyt(1EUcG)}d#o*+o=Y!jk@fj;#hx9CT~G46R!ko`q&)07+=#XV$*~<1L{M^-oZ6wl@TJ&}b6rWrvG?dWHbV~#'
        b'h0bKh@iz(X!=9f8uJZ-l=H4al5b+_G(zm*SC$Oh`t2p)p&%{2Cqf_b+vB3M{y)k%(1<xEQS3Z-e!edEX_B?@&yrNW@>C7*-XOd<G'
        b'mY7^dU?fgIQ-;k;ULl1?#r7?jHaQn9XrME{^EesomE=DsDlu6Y+Y-j~VT=f4To_}*m4Ooa`k!?Rxs5$GBJ9GRMW|SUu_8{qCQOf3'
        b'qbun+3~fJ9GsLrWn3j2Q4AS%hdb2A75O}VI{Bt7S5}QJw3izDr>(2OGbKDBEvdpY{-kiX)8{Nx$#1m=N*SYvyJZ=T9EW=gL;|YmZ'
        b'iH=85YgPCJ#+E$NsPqS1D+;OftAuwEn9VeaPrxk6?peJfdCI~-ZXp$teF)frO6U|YQUO5#RK5LMsQyhdg|7b)-Naetm$?n7!fFrU'
        b'oec){1P!iWaXDHgYIl)~v6!obbv&Pje0O3mSJYEz=J^7E4K<K?7@Y!u5E=a@5=B8QeH8}R`Um7<Lf3WldTT3sMoZ5)3~ilZXv_Fc'
        b'!H**>{;c%(5lGUf=t1fGXj9ix1S14g;YD|Lp;z1K-PR-UTp8Vv^T!CbG7J@%#7#5O_6TMTds`zpUyxEvMPlN7A|X8!!SJxRE5dV3'
        b'&UYk%-i+7UjowJRB8bM?#asA-ZF-9{-aQ@R0=m=KKw9vW=LTJQOiG3;k3D*~$6^LF>S=08gSK;G+gE2bc)Vu_?~}bn7qGUCP1KvR'
        b'P218HwOfnWkpg9Do4)Y<!dw-FO*u>|FeXm7br>B+gJL;Lu|?Og<Vz&21h0oQ$7|m*l6bthltyPz^tRvvnFTeGW=t?o)6OCdANA0A'
        b'mRvcXs~CN10`Fg|6((q(LYGwrHA?m{quw5at_;;ExlhloTr2nRae>EsX>?Why0vl(r0l))OCUaj{A6^jTEWJko%QFj`4aKvl3vgp'
        b'6edE5Q?JF{RwPwM?~*jSj0<h)J14HM;gx}44~^81)-ZvNgZ5Z&MlfyDE$dM9yyu4CSy~pH+`H=;C6F=eDq(9G*DaIFRpRNKKBKl7'
        b'-AtX4RGXnN>NB>8=RUhJ`<5Pu#HKDvR_{-+xl+?M6V}HuTITbUiakhNgbwdVr%@{~=fqxg7OYxa(TGMDpHf>l`TdN6v<$+VkL41W'
        b'hJ^9OSt{8`5TqFg0fsgUnhCUv#h7d~lST^DQ(~;}QH<3jA5$LWNV8O9##Cm?XqLD?I4k<9K<kuE7dFKeLJ5P)g1e8N6&E{6RXBz='
        b'LE(i)TtZq1qXk1tFeyB`fU;v5sz1aL43m6N36NE0%pF9Z0@)eGPxSzkLohM-zUT`gHwrVp5W%+)Ky)f-K1D=fdJ9pR5J&zq%pKz}'
        b'HSlR6`t+FLActUXjlRH*;tP{13KNH>(z$_$&b~=*+O|kx%r2Vi%sWfU({1y@;;P}aku6GB$mM#)rBYy|jMB&u{~)<%xEx)EjA_D}'
        b'rC9LP$kb~_iZY1-SK#RX4T%+JMIT;7qS&|)hX*+lq4D3x(TKVXv`!UTn-H&4lBiCRwnd=r$2jO}ki*CO>KN}U`ep&@(tZ3b8^@nU'
        b'd;y4+9*K~YGz!XkJn{f-Kf-$C{}_vLyv-lS+k>%?9!2*bH2m$1`|{b~Mf~dI-lMn9^vM^{ubBSE@G_f4{+1x4>B62K%Jxv$HY03X'
        b'8t#^Fsxv4KA8-_4s&L&sEIxc-h1|ZeXC$m#6H!gV$k=oYm+!lB;QS=AAVpKadOGj=PL3cxD8a&-f)uiVwT2@l$}qfE!Sl^XXgwQR'
        b'pMp*^h~6J@>I}MoJ)sx4%l!MZ*%j02#T)w0(Bw}filUVciLiEN)!HP>r*{<<#U0`;0JOELA6HbYa~M1^Z>?Lk!2QBmQj%^<3fJv#'
        b'c(iB4i|&e0$uKb<ol52<MZ@}|(~QBjGXaj{vytK-?sR;E>USSIW0Qr|EABNsf<D|^3tAl7jjqzb=C$GGhO?G<%;MzgQjypY_quAh'
        b'-=A&5o%_x>h{n-{BoE^BJeYbZsU{SJOW}IXS~!j;vX(UP=4qTCb?#*;oyR*_TU?k<Qsj-KD%l1X7H`5127*r~`8ZAfMKsHM^fzb8'
        b'm~@|FDoVbFH8h;DWrm|l*t!jCnA{^Kb?t37cApDfck%NxAmDwO$sXrSl{sr97SlBxI@z%044U>pMQ3=pnJPRBDVDPl4bJ-7Y#3Xp'
        b'%LK`xF|*^x>M-H!9EVXRy?CWOdt>KyCs%c1r1<gg-5bu(aey6hZin#xF=BD1skcz1wEXC?v*Qct{bxj_&H?2&XDW4@$e2kOu2V@X'
        b'9vs@ElCFy~Jv{5uR0Iv$0Au&^&NN>A>ni_RHj66tm$U1(Tq{yeDJpelmU5iKnMz9>PTt|vIyy2yXU_!BG5x6hY_QEV`qV`C<7Wef'
        b'XWC_NHDsQpB~W##pSsRz6cw1%bgi->X59u_=6QN%sLcjL>UzgT%CU7rgx8Fv@dUK{dYftc5%?hsvF%6TU8qeDg+e+kdKfog)90Mg'
        b'?$iNJ-RsYY;kYb7DfGyLRxizH=X7XgXfgmQalPj9$S_wC>pOY3_}4exd1pKsv-ah{n8Md=I}5Op5hucc+B;IQAjdWe#tnDQwBUzu'
        b'=#L{`QQkt(1)hAci0RQby6wi9>s)%ctKG>~@Pzb9%q=++%s?tGXrJ$|-{?QMu_B(Za@Y=eMQTjVEq$%tU(2+_TBid&AARktO%b+k'
        b'iX7c>_IjHQcv$xvpc(J;=p1*arqr40ZHiQgXb1rs-m$ibYvT)C2iZ;AXM>hsnK80k+1{q#`w7C30;~Ux>*(LRHL(~-1eSaj1{eAc'
        b'UjzLux`r$bu>tkRm>qK0OKjzFhMq!Cq9?T8*=f4GrROa3$v5?f_5S@#(8({Cev)i%Ipg8d^?R7@c?GFWq{XSNxuMU~S8inJ)cU16'
        b'8%}k%P`=Dmz&?;OAiCYj(@R2aCG^yqF?5GaX6HkSJtrj7cdbl8WINe}bq89{=v#}J`m?RqIi8lazP8ij<U^<Lx`StY9PcPlynC^o'
        b'W3O}C+AJTJ=6bEw<u2KJD49Fb9Wb5c`8fIx=>Dh_)xJbpB@t}&Jnh~IgOG_X?9NbL+sy3ys$qY3MPg=qrZVvBGc7SdAR{!;{fwh?'
        b'&jvGv@{go+vQ~G?=9*Ky`%luTfYO!g6pqZeK*rgSAKeGHOtLa&qTSaWNImP&#)bSb$d`Gon^vs<KIkV#q=+=7Yq6kKG-cL<DU(xj'
        b'7`$nX|82(a-&l9J6n!NN#Gi$-&S%d+%SzMYiYsn7w8}u$8L(d@n6{C&zu4{E)V=Eapt=V{1LVO_dzWD}zkxpM{NRkj;jZbnt=r<@'
        b'fD$r1PL{TU7%lqu4cJ-WlovOXF+iso8=me49u2nHw(n&_EDW?SJ-Nz{qoZG{1C^B<fkDI@9e^8vEw;N4b-F9MZ5c@5Y{KL<w<<U5'
        b'D~lMLZKDcjF{V&uW{Wr7-bb2OKzA*vsZCNa%a%(mPTsky+laHawCMg&h58o&GPSfbQk>JT-Y)^EG9$CuqU0>yg}nLEZjf5G_~@3w'
        b'hn*&9;!;amDm{Zv#6CFQL;_6s0LqLkQMT2bDKs;P!fpEfESVRteJrBBw4aCK3h~bAkT|Qa-5oJZK7*FQ<;p>P@T85M&GNZ6I?nsb'
        b'7#(K~0c)gxg$_Cg<kN3R{ZV_ch2Va7rtVd7#y_e1$Gbl4N!_e|qbH%);>UKae-UcdZkzYMZbQ%?vHhOiLDKZFylc15KelV{Q!{1W'
        b'SS)6}ZXj7ZV{h{wCAz_gAQf?<s8y(9aZ;faSDDLbf{vF;uqJv+m&<Jqoo20ni^P0MPvP|jb8&8@iR>USv|Hz`!0640`k67&S?tGy'
        b'k_GmgU4B31(W+a-TS~MUK|gjN30=1=-aEcgf0+5?uOV$Jt)gXg{F~&~HzqE8QM>>i9hIQpxFhxed81CYoIJ4e&*OAi3&Mvzuth6q'
        b'qnIQygA5o}(BwA}XhB<&3#|bz0pREk%eMbKbM%=rO_Vk}QvA`~tV`Cx@%yQ6G!X~N*6I(L#}^G#>OzV8{cfM10<sp8sCpy1=~`Gt'
        b'xi=vE8b0f)*q+iN_h^{F2i?)7TID8E9md^Hqh#@=G52FgP6w8q5j1i13}^}}@-R8|nqj2N?e7*e1-;A8fLBMS+`khNouvGQ*q(;N'
        b'UA~KWF!rD)_K?4p4aOeu#l8&>^|fq6L$}MdF&Jy}ETKWhdY0H8+_~Eon19BTxgMwoUL4q+>h^XAWqZ^2N_>-h*Zp^b59}x+eewj4'
        b'%;wt0)YrDslU<oRqxUa0bT!O4<6EEX{;;b-2M+}enee+r{4H$AfZzQ4cO5mPouTDBVnhC<O|Qmx#-{I6Ttk!EXjenV)N4}?pWZ_g'
        b'(tA<5bWc4Km~y68#uwu14D84IoC4}IHMcy4xH|z})+If-PuWAnRIewjY49KmOgNJg>nX&xen@oaum;7Mo=)Yd505F-U&p3xF8iT&'
        b'g`yS^@qWgCp8Bv)A)zz6-V7<IuB9F#7KoBw+FV=aDJ19_T{}+gX^*Ao`K=#r`G}`uTjVqN86R)`Fsq%AOxfcaQnnM)o-Vfi30!(R'
        b'f>qQu(*$2gNJ->}5wUa<0O8jV+}GV1L|vSC-x1V6FR2&7x5(*O1nl#@?d`OD${v7Xy%VXq4*m6Bk3{cX<F0hmWCkJF@#Vx*#3yk*'
        b'f|511ju@5Bi`_IK9RJfZM)V@6!O=N8r)tTxq-E;AP@c{)mu`#a_@A<Wo$XQLHDB6nl)jd+)v`6`OeX4Do)S_fNd1--Cz<r(Dk&Gc'
        b'(Nzn7N*B*gy|ze(?q^*t_kJ6BN^booIwppXy1`~FAm5$SGe>DMwz`3SjY{G8-R(w8=iORTy$Xxo$_Gu$-}$#FeH`gFnKtg0Rb*zm'
        b'o4R+)Xjxk3qMmJF)V4Mp=tc(;Y^yCm*G7uB5ABe5#6aK2-~Z<Scuyy(U%V5&4HRJSAW~v!V(WamXSdSr>)u<tTUIaL&NnZBHIbwD'
        b'(0M^7(~XjnjXUIBI$D@|%_o=A%d_P5O<UIK{&p#lvJCXfHg}&h)-CTsEa&a!%`rYXX38*6`7l(7@#fgTi{0Fd-FtAli=K=OR5K-*'
        b'Wfrr%suXkIJB{w8at}6CJU^Xw^qD2RS$cF+ce@{F0<890MDSzFuKG1Q(G}+E3pWKBMSIjc<$_G|?(<NTH%p)d!?D+Lm4%DJG@oKL'
        b'Z8ld~6c!6Tg9itpc+C5CgqKOL%|jxrPIzga-e?xg6W%b=uRw;yEEUWW`bPHeh>jDHQZxN-a5)ZyfltU52<dQyHJFj`o9il7VI}&F'
        b'F{MOFj#<c?IE9~**YSO15#A-G)z>WJb@Qn1+=-UlNi&Smy1OFKLa4s(>Pu;?hI@jCHbX7mj>xq%<r6$$H+m<ijSL&kb%ExyJsw7D'
        b'eN@RdL1!xsGx|cX*7Oz~BQ3O*hcR<u387;oD3c+@U#d{NkPl!Sd*1Ul*1Vh9I#~iVRDL+(PD3M-rh60#zrPXcH56K+_$|>@D26<+'
        b'Q3+A^;^?b{_cr1dL?5FG#85b+jE|G%mnPM!T(0<vBxdw6vhMJ~vd$G5heIT~&6u-w@o`wO=ML{5lYR>_(~a+l;hpN2NyGs;8wDpj'
        b'A}B3R74Mv4;n)RQq=i$#txwVwkrFU?leV?FTrZGja8wdYos1hpQrj%+3OeJ0T(W7Y{wW2DQH4?S-9*=+Ue~L7k2Ar;sg^4i)E<<1'
        b'oSgd~=w&+>H!N{~*Cj5#RRx_Xx}t-~PY5}uy8nuDJ9~#I_kVYZ^Tz6+bJ~KOgJj4#-Th_s>y$ojYAL68e=%O-&=<OlgT#m5xi6!P'
        b'K5lwDH_d%X1oXvB`69*OcR?;L#KpTWpuFYsrxXW!LtH{PF-*F9QC7EnSkXkaNZeib3q(H<OPq`X8vG7{5<hf*`rsp?g><)yDQZ|U'
        b'`k3JULzlQq?$2sM`Vz*4y1>7%5#zhiyf0yjv`_jl;?(#mfg`AJ+dEyo?{r0<XUc=z#O8-s_o08O;cXG62cw{c#EA#Ke3F}Tn&+3O'
        b'1&QS?EW}MU8QCD0BCMR~{;w`^f5!BnQx*g?>=i$1F#N3RR@+sM=>(n)0nRz~eC5;V&{I&`l{#fGaiY)^0aJoK%m!CZRN)MF;S__*'
        b'Rm6Cxry~!=+Q6Pf2jY|ooV81XPZW;?(Lv!B`GY%<+!K&!7)=&zx-eGySM~c7_{51TODzJI2qR_TR3jRtE=QNDA~B#Z;mGG0o(vF7'
        b'&0!Ls7=>S+Cx8WuVjY+cKGyRLnUC=+Ct~w19sI)d+py8hxNn>iFBF?7_$i*7qA+I1>49dm<8@F8)Zl1ibc=PXfb>)njLmRCRUwXn'
        b's!$6@#c$VQ#m2kb&?y!4g9vj=yBK^8bcj21O3&#~&lovJcP%IB1SSrANKN$MGPL{+PeP89IdR?VTEJsVOyltgGS>__UC;%aDm*0('
        b'h8s&e?tLXPQ`)g5g3+P;5aG203u&h0xrHvV=}eGI4LOzWS>qhh$HfPoNg?OtAjgC_rF%w~s21K-v~v^sxCCIo5I5Q5)cTxh?$jvZ'
        b'Yrzo`X++i%>z*po$aM4z=KMH7@gvfl?oPT7t+Q7IhN>6`ru<)kDWYwR3pwLSJRKp866vTn<V?5^It9qijfu75UE)%HuCw<LA%dR<'
        b'1jzd-_bo&W?%Suu8u&MfL$XcVGCVL~e0tI}567k_K?7AI9_99TLT$|USHX>sMts1jUvw?Vsaj%2n<5~v(vu14+mR_n(qII9n~9j@'
        b'l0KJ>k_&XN@f!m)Gw7TE$x)f0!IRN(O>sISo~XemKmk^T_Mp4Zp@u*v6o!0^1lmoG_L9ZdpkAIneZQCJ7B&pU-&1JQ@6c3)dlDiW'
        b'_leUDQ%~6n!nVm_aHdSS+`Zy7I8D)g>o!?<g%m3zFb##}N-)!fu<5g~X(Vj=UDy;1uP{r?%rPpnN@J#S%@WcaKl(;QBgJ=8_<jkV'
        b'OW-KXzCbMB9yXm1n?4Gg4uv&lxzQZA(=6L>j?FbI#KozR6*yLgqw*?TWyIrvS5}zmGV=sl#+Z^DeskKkI&6|WyNR(5p$zxl)3#M%'
        b'8zr9gWyBx{v<43K=b9O#8Pk~Y@?8-CmWwm$WZXUdG{%I*fRVTtzaujB8e@_-EIB>6!L}z{pQr0|9<v`boBkBu_5}bDJEVj*0<^|o'
        b'MgWNI#qi+K&OnHZ4RSIl_PlwLc1NTPP0}bEvQM+ca@(P>ZEqM_?tgvF^Z2BOs?)V!Fss8m(KJ!K{%JY3D-1mYQ2t-9VV(|`6v@#s'
        b'U=pzdry@wSWQQ>-yd%bXJmUWPBxVoW)`v?TFLYlM$42a_^|Q#}hViD3hX1*tE6fwMuK*4wjyLpJ18V0eYG<Pd+DSu`K#o;f<p{S2'
        b'!`RNS|5s~l+r!X)cm8Q+2{d#9G}HwR^`V9WsPTs8$)O?9X&-Cj{f0`y9dClZZNo^4Job3t#3|BDxsRVjv!mNjzDyPT?oi-qJ2=`g'
        b'Yb9h%3~81)Upe`-GjTj6HD{eBV`QS!tfMI;fUg=<F%(G>(Rlx%4dQ7&K%=Bt;VwsTr>q5Gc`RVsAJ+Z@SOd)%u#Aq3p~lDbacuno'
        b'G6q+X#Ec4%>xC8Obti3e!s66cvL#&+vsR|UB_+zR$}CA-E7Rc85*{c~YQ!b*Y<}`2tCFMgxSTZ0$QY>}x$~1XxXg&l7(Q9A*O@|L'
        b'sNKCCwdT+|OWZ{8D)U&2W1@NaNfM8_9|9mc1mtfPG20p}M_iRfN=1cw-UKp+Fyhqi571m0Dc8ir#yl-C#!z}JnPm#u5bCPRjA@^X'
        b's9%(qw-M?Ea$nrUn!mXAFh0jbA3+6!m}w8|vrxV`#t#n;#s__Rn(%TMi4!VZ)`Aw1BNiY=*G1Gi>Fy5_pGHwV#9f~dT`#&nL+vi!'
        b'3jik4$sz~@x4wQY08LX9-c*bvu@(Y>z#7XU$ar5a^#&s11SqA!V_FChDdLb2jm}8%-tVSfb00xK)w=JkcOx1YKO9rV#6nAmLJckv'
        b'i=x)C;<QltzeS35-%F801m&PK6gA>fhFCLRDU{TUB}bo#6hCvri%zKYaIs_z>FLC=BsBPF_Kx;AV@Lad1ZYG8EFuArKG8!rfC>T2'
        b'fL)ACRz-WmqBsxMSR7IR^#<TB*c5Sp(dpmAs9?nQupkovm0~~x$be!95U`3C0zMZ}sa+8%{_B_0&!Rq)CvKwe(AQ{z%-iwcgOlWJ'
        b'k7J@ovzWACp3+$NA38y-idSJT5YFN0>$BWnb+#3q@?;dEJ95Rnb?`8{JmM}zSVK#jbd1_T(1aIo?SAuQNcN%n)qC!XoxKI{RRNtM'
        b'-cVJ%<}Q7G>a|fDu3m62OWwF#-uNqp_GyI`>~$xWiMt;?DH_+Yqi+%iaavK{81=6M*nD?M?M84Gp2mO5&3A6wAjD6kC)XR<l9Csy'
        b'xOn05i6isSp>r{k2NSs9V(+d7GN_nLNM~ZCnLOrBp_@Ri%iXVZijzt57K+Tpnk0?pi25U0t#hP8IkH<>yJ7F^d(7|v|Lo7KtK~k~'
        b'90e;{i5mf;@7-g2eWV%R(|{(7aoiU_QGEAoEk`FSYPWHSA|IbvoRN6Yjh1G(*Q5FjD^Jpdg~ZZ-rQk_i@Z)-3kES|VN=l(qc5<;6'
        b's!1}MgXksdN&o>$RAy4z8xdckEi&^W#iwqH#};dFTopqCH-mnNsyAqn=g1i1vd1TqI1U3C?VT~Az7+QDFWBW<F__v`)Om0%Aoh>3'
        b'>g~6E6h%*~KWZNNSYI>T+)Q12N7?fs<NugFxHgnW?LOT3_{F3D9YEL0Qq*4p{s!~l(UCp+`g-cx9%auZrv6RVmq)oxoj|s>q^LrY'
        b'MR#auzl``|CfA(|rb^p#I(HvNane}K7raE`<St(#nt()$CrDNdzcpw&$ygG^l`kd<+Fb9a0Hvb9h+<OgyEZ+dUh}uwhPncPte*du'
        b'zEq+;RT82osG~d-Tb%rr_bA|{q41<HHdg)gpFErtPyplT;i$d4(B0)Szy>m23b5J@XrS$TccJAZu~;-y%SDRABUV51y|DSX;ob?0'
        b'ov0#{XsYVOnBXTW=WKDmjYjfiauEeI+W0*26M6n#39Xq)PQ7NoenLptyR~eRA*HkJ)supz5QY=Q>&zEB8@@h4OXvdA9G0G<s2w?|'
        b'JRC$5)3K@B%owiQWB8CmYU5c$d+N+XH)_p3jtp_ciDU)3=<uC@zla6x<2yNG`Sfn_U+$QdCoNRGB{$1VbXNDjL`z?mdQyeD-JLiv'
        b'W%Qf`bnUT<su={qjUHD}_U;otCE?Lp>-SUils!shK5Fw(uo0Zm48og+@!GgR@yX~6Jx<UHUTbYqK%(vfJ%LX(bjP$z=xJibyR(hz'
        b'&^36lwncoY2KB|89w+54L3r^6v0ZzKj!O}rpA7jWLDE+F#?D>a3F`$^vaReS{c2Op9z*$Yy4Jkg&@FF~y)37vHpzf8cH`jb*tRQ!'
        b'lP5NO-dTT`aUEuB@!+b7*3QT=yorE1v@wxdvs(V&bR1e9TE+x+bn;rpbxdqj5NrG%WXf0WhdaeH^Dy^9^pL*yD^ys+per$^Vm^&7'
        b'sF|_nxJNV7r^(7t9y+(@OHbLP{HqGoef3FbGytOsht>+>mWb9fBEd%gj;E_9I8qJ61Rw(5Kwe|2Li-PF^xts%^C$R(UssnBqZdg)'
        b'ju=uyfmIcyH&EWq5d=j=(HSlt#asCml=Q3dIa%|H&KA-`VRadZ-<ybX6+Tn0PL6medCegZ%_t_vdh+C>*$S;i(Wq9S%ivJFYjG#*'
        b'y5Unz+B#W+cx@>WB(dT`oL@0%RCOz;lYm%Juff=6s{D!A@wF0*2-dWbqfR>fn8N{oxZMiP?p;}`;0&Fm1YP|2|HIh32Q+mh55PA!'
        b'HxH7lCV&9}yU7iKsMv+r7PNLNfdZoKLez+E`&)?y(QWsq)K=@-ZE~p)Dc!}`Dp<Rln>H1xtRyJ%5P4~&imlqWeNk)F+HPyrT8luw'
        b'nVVqU$M=1|f0FZ@GiT16IWuz}SESl5Eq?fzP^9D!O8kK~J*{}4?0o?vnN|FoW9gPM<^z%;W6e&nJ1GWOXOGf;tv}@CRxK6T`!UQN'
        b'?ProAef;-27*`P6Uiti<2Pg|!K+Bgc$2G%ZEYQV_(xm6CpxAWGJZpk6DHV#+a@F-=euKgP1HV~z4OdsUi?V(b!A{(+$v<Xe6lSA<'
        b'Q}nY*3Lo!Y=LY(L<#ky^pgf{F&O_aFC*6fS?OIoz?{*O$$xYP}s!{0KG&)`O0Ogj<vLvZ!IWXFwm@vQl69BhQMywg#Bbi<Oa~MUg'
        b'ldPCV=qNxhbJ{UuVybHYH9DRasSj*Jw>m+jT{yPsDl4RIOe!lZ0F3NS{Y+NDyjGanPT;#bLCqdDTP&)}Y%A71HCmfFUFIlkEq)-v'
        b'JoHn%<6!OC=@k0xiCrf9OUIz)l6;DmSwD*a8u<AGPoJLW2W66G;Mk^XFf5(avKgtVsrS$~8ihbPt8mnlF7RGD#(jItQ%+alhodzg'
        b'_}vT+i2bkF8O`Bi4B46tv+iUt<xI}WFt6EP=%*u`dE*D%v&pTM{Y>7t>A)IW%lmtne)^Sew_9H4dM$IXO4;DJ;!xVyZni&_ol7Kl'
        b'd^lakuQ%vViyYEC(@#@I<9JP<KQ(n-0W+j|x_>ZBna?Z}fUY}l1__JriBv+?^F%*UbNSG6V&>VCLePX#wdxzpJjrsYCaWK<cVep7'
        b'+E2{6`~%rPU4F(DoIPF+{aoie5&Ur5J>9+C@|2XX3`WA-Mll1Uv+?8YYFu5!awg?n{!8ve<`2i1-citU0anhXAo1e(UF)vA?!L1V'
        b'&toTSwsjB7*m(rbI_}~zy4E$<EobIrWe(n>%*XG?rq1j(^rZsO9j!ZGrN;W2@{QUJMkNl?uFH+2{iYv6@`eWY><C)Uf&~;SPx*RB'
        b'Ek#S&d_YIu;L8`}{2Z#=DolC5-RG1ObpGN=e@r<L|H9%rky9>UPmr{%Q+87JPZ|9({i`Qrs<)^!Z=L$^-h038IJHZ?Yf}7o7Y|5U'
        b'o}gyuSBxXJs{4=4ygs-~dHk&_1In`lSN0)`#XDereB0P47Y_%WZ=Lx}T=PZwm5$V=PKEi_$Ur_l6@49QNB3J4C?Y~ymUAnZuu(k3'
        b'%Z(zT#Wk|jbX7#ed&=H<|H?b+m6f7ik-&Wv1pa687v+!1UzO84=(|*pQkH>JE7R{@)~c?KHysr$PLHV`C$Af9RaU(KlwIxU9N#M='
        b';v4+egPr5d(}VGK{5$Hs17~P)_aDm#KTAFJfx_H4GI0NNIgC|dhM$n04Sm?-X~p<AA~YotcNczoEcA?F%KMA|j+@=;solbCLe5MP'
        b'q6jEFcWhc+r~qD%AylhI9=P)K7HMH~xLVE+s59bAQ$#%DBA!+x@!kf)GamG5BK(xyUyrdag7*!flaFx;2z?*#*Uda}4625#Hio}#'
        b'hD-2AsiAKU7>^6&+11nlh-GuRKvyGhO;xLWqxRvW1qalQo3p3l-H;o>z^?@bI<=~S(EUAvj#N(#>vI*?gZw^8=Frg-hSYL(0X0;R'
        b'I1~k1Gip1eLXhw5AFgz!qBBjO2AForxGBf*lu?qOKg59EHPAEJzF{@Kj7Ow9Bj#v^CSQ3m!vD|U1JazEAwJ`F9i!#+fL-9{-xmUj'
        b'K}XD#&WxR@pP4Z;Z)Q<vgmK>&^j)7t%x+G2%1si*TaVGdUA?haLR=Y8?3zFLjB@7=(BzzNo!YrGo-wzNh-rejdfY$fImMba>z<(3'
        b'{Bhf}VwH+2JN|Asaww<l_}*}MZ-wjaZF^_y^D>ImGt_!~xmB;npIH2n!q0T+g(v~9$|g-)bK`#c(C?DsABpdHb)5gJAW<?8Uqrq!'
        b'j}$XR$?q<e9e?BGxHWH=KTDq+=X$%md%aqfKC)xRsXD3uYOuHdk>k(wy6o#`cLOfw-M7l>U)oq#S0w&62=S3|Yi^ZaS+h=Fr;-fO'
        b'2X~~uQkPc|fSkQ%$<L~fZ*IsdUU=-(u?5HdS83wpxRMxof6)`;y1S#hSC*d?AAe`ZA=3YGur8zGqo6tX<BkKUuhi+q?*|F<gdcY_'
        b'lND!zb+I|8!{-!@$7oax9FyRuKB6*ieASeAhs|~mLrNiK%cQZr%bEYja;g8va!JSNPy+r$Y}FjQBQp7p$XNM!DBl>-8j<`;Wb54O'
        b'Pe9+T+Jf6wRg9FHd?nuDd@H&n;|rPuIl`BpaJ#&rb?)9z2KCA+7RuYE+T4tAP!0y8P&4x=J&B3j3F{s$Rd3m58)Nv}@VaOc1P-sG'
        b'jQBHe`D=wtG?5Xp>8!e3sZM>*Hbd>0<eH(d*(sFIGt?;#8>>jE+Fd(t(`87<qfuHl^gutiekQ6A(S(|zU|xY#Mt;BGrz2jJ8Kx4+'
        b'+ZGt6QmS{U!70ib#>Vf|rhVaeMiKCv{&mt`gF{#u`78JC?%ffxo=^O4sT6FU><M=HQIOtxP;IB6IqDG7Lbbk|j#X!rqYfWm=RO`?'
        b'GV@hBeE%E!aom5#C3Qy;r`i?fcxkVT>^`n=x&+;?Y}@o+$P${<pr~n3YkK_d1w=i`%BVRG1uAa&ROUaAm{UZj9E$YP3^sb_;?m5X'
        b'R=-;&rRRC>pTI_;cOS37?8J8_u*L!+gY2HFbPK7+Z`wlM{w#`tiWVvN?GgLcqv8E#BDeHX&l?Cymp(ytd;~x__k95xBM;&6n~acx'
        b'F=DbP@fD<7;ZA??@gwyjr)sA$PN=r6gOzs9Tm>CzmQI+XFVEcS2g0+_gm2%iLH^APyh*%}P<=Iykx|K(e1;;}eHRg8HlgV_;%0cu'
        b'K~1@%2{6(^crFCB+2y*Pd{*XiQ;dtGV_o`kms<%#$ksmybzN>Oq!;<3iJtX-Hz{pu$<|GqaHzovC3bh)wkT-Q?Go7B<xN$1pTt#%'
        b'H+9&BFxDcQ`np<2IYf{DY?9&?!y5iNAd^QiDxNl;Blb6uHqhAObCOK~e5`#T#!~Ni;>@5nEClM&(m8CoO}!33)TfW5>(vg$bYV%Y'
        b'q~>LcHr8m%fevbQwzK|07ql}*3Yh&kM{@n_BqF^u24p>q))FH3l9X{NLSY;i%{m|setp^=IKnUqV8Z|t`)^|1&qyHpbg`;L@k556'
        b'CR-=8+)w8GhL~fEcJ`0ZF*V8MFqOC!N0Kt0aGoXENz%2mkFJ3MT_PPkq5M+sZ?DG5`xmE_GUQ45kLRXo{hK~CL=kK16kuqeB2%Z{'
        b')QtP)b@+(K93$Rq%T}uE6m#m-A4{Ei)RK%<c}bHsCDZX!nM|yZjuL|+{K?PZ23wD;aj5<0fbk(Obj7(y$V_Du_~2?*Blo9C{LJbc'
        b'jm%F+GppxmBK)+7S)H$uLTauC^YZjU^+Nn8<AC8*VtF;&J}@|-JpOj?aw5K?Z2~N`CDTM{qel&^=OVqJ9mDH{|NPio`|c=B(v-y|'
        b'b!6?Wt)H>XgvP8r{)jV5$j0uZ<!BR4vbAlSF4`S0(+lxL&J+$fAwJvC7hQ5se^~aVMIK?b^Q!Yo7*S}#xV6Z!_AigxsuVWcb#wiw'
        b'Q_C)X<~%(Kq?n7NfE|+KK47$H{pNtOf#-}qJeoPucfwF08Y+|?i4qb8x*>k~R=X3E=6F%ju+KVzyE(8_3kXHz(CxFBuxuNT45m9N'
        b'eh>KpsrdVF|J=-^>IVB=$f@`RUCSgl69;yh$M}=m5;ul>`%(Rjq6J1KK6hf4kQ%S0CJ=-yiW&!+K=_2GVu(qMkIJSkE+YA5Eu$rq'
        b'UluKUL#@k~=@%5uV3~x6Njid#t9&`PI%4jE$ycU}Oia8(ySSEW6bEu;T5_C_r12P;B2Gw-pFvI_6fz-2rwZ~z$6yI^NNA)VCh<!K'
        b'y*Zcp@8r;0DUG>AY!qKbp_GNo6JlW={jijt6eXpF(s9$Jc=JE+U1I0EtUf{fIr6@J^HIHYtbgoLebjKT=8e9T3R9$fiBK;z_6knD'
        b'4pOvxumOH;@N3`KhkofO)p4=WMHp8nBu|ukpE}Atb=2O3G|!8o$>iuq>}5wgNn5?T*QK|2V-3x7N7%%KBBS24q+v?CSt`*BeMcTY'
        b'<%CJlJy@rlS_eP9u63q;v7bpReM$PLDKn;Mr!0V}IwgyaoO~s@<z?3Ov(dF8IYU6dK8NX^BFy<P*ceeQUAnj7^*!<@#@XE6uE)2n'
        b'etl1TyrXvj?3H!6SFbx4)N2unwqC2Bk-YP}ic8pUP43Zp#$l+8Q|JbRwM@N<oszJ-PO!zag$bQOdGM${BTN_j?4x?UBO|$%1YI_q'
        b'rb$2QU}_CON6pH<%1Hu!f9QOPJq^}jD4l0xx^W>cpAOUoo@FCxAsLyLa&+Y-5lhZrUmC|Uu^>}fy%N}UkiR*FZtbiHP<ow_v}9E>'
        b'qm>hpXEl<ep$A&=yBC#5LZ4d1)3@Xh&%*@acuh+x86Zq-T<+H~A%7$AiRR`JBK9mAbbMVty%W+wO$B_?Bu9Ze9WyE;f0HRZ3R*Cj'
        b'RDg)}$KaTP4#n@oPr8r_p>bRYs@6CTD9LJtFq4vN2Q)t)i84w7OvVg4HuRNC{21-zD+<9>{u`_J2?T}zJkslWJnvpw-bmShgN%?+'
        b'J+Ik)WWHU7k)kIP=p`#mQHoB|v`}8O&3#0@WSvRKn6f7pHJet%6}@I!G07h6g`$>dx=?u}<^oyx$&pgghKZ}}rMjYfpV_*^TR7Ca'
        b'iu+7NAEU+e{Ebd@Cyq;$4-kT>y~WXIilfka_;o7Vle)2%?NRTE*jQT|v2lOR&hB1K^chW*Y9>?j<+88k_1Q$kao_aB!G<UIWJ4Wi'
        b'ab&2zJsDADdlVa6p~fEhmxqqfaZXJnkuZm7;9RbCzVQUW`5<Dl>lL;05yDlXK67%g?AWlG{%NiENSTBv%Z@HfRH=^1TNeu@)Zh!s'
        b'Dz3h&XP~#K14dubeu$7AZ#}`EyjI%jKHdSYz#Xv2IQywyp+s1qA5w(g>M17dc}MCcc-R!*?2W=VdwKE*1yN(eMv99F_lg)+qtpr%'
        b'RZJ8~Xb$(PmHb`5&^!Gm;9rEo+yUjge}__$N9>7-qGE&+{=!WzS({Burc2h>krfq$=GES3UUM?@pJ}dq=C>PGq{OYS$}2k~a7!ky'
        b'ls&lVC)fJaWh)h`?Gx;--et?ymGvkJq(kQI{4TR86^w9+{S3AT*43Fl`#TuiBZLuNQ=+ykr17O2UC>>u*mE6&u3+)fBYVylh=%|U'
        b'okOG!*{gb^c&dQdmzRKf>DK9Z!5=jvGt%DCJ0|<1Lb88`ATlKWVNCGu!-ZR>Xj+)9lvp>VJ#<8v9a%cVpe55)WQ_GW&AMKgT2mlZ'
        b'k&{Mj`q@>NTJwscVoQ*Fq8C`8PQI~rPee{-P?#OVzr7;N74TQvBqgFK2?6%wvf|8n>vN6-i~rJR5ldC7Ydd}>{l|mFsYk$U<lT2@'
        b'Hs<)Tu8>$9AagzsMgfHdQ^k1Ss&HX%vGxcoZFC>~5HvVz1Ax_vC9~El$fYod7XPrJZ#XKKkS{U^M$+PsguZb7G$GSGgqVxb7)nze'
        b'8T*9rlQXgvhG-g=_vCk1%z0g{I~df+kH8=cNon|O&D{jfb4nr19-HUc<Dd%6?ewqICXJ{xbBU>FZN}*(Wko%!j7!MU;-W8SMrQo5'
        b'%7V`~6<+VtKQ!fD6tNF^UJRnFCipG6C{IMNQ4n}On6{)3`AR!Pka1}heR!@1-=vxvl^Kcrkd`VW1yO=X&2RgF2rzCS<DjEZ0EQHg'
        b'7Ubf1YR32Ct&Xv^JZDD`I_rNqh_dEX`26REUbm~h!Ljw-zIthE?4F2vklJmN_DtC_lb7jRkN0t>`}8v%Qz{J;Kt8J(jf-XV5fGew'
        b'1#AtBGpwBP-wMG)KjqsI_CtM6J?ShJIWj6Ik)G#*JgnQ&8?~T=ef;T*2!4NWoG>pUuqUXRN(62}S+1pz-rGsq2e1=hfFYi5_7&A9'
        b'zbvh7rK8j9Kwi=mQz|o*%B^n%tK+OUgK5`#9ABx5Mw2H}v<!Xbua7X=@qiBKKo!?`8!q$B-rDS%Eozky^p$=ayPR>!)Q%@VeKKR='
        b'j@l$9dIEn>x$>N_bzyzB=O!QmD};K+a@wSx@#KzLO205Y@}v2(E!i^{+WUCauJUkc`D{Ga{caET>+{}CL#*^0*2w7UZ#b56f9c&~'
        b'acq42mdzpRu2r&;<HNR*X}nX`M#s~#nm5aRjloxCkiMotiD!x53@)p~2arO=LThB&)*iR^UeNk%?b;GK>7PzGPu!pr=y96I`)WQd'
        b'KUK5NL7Ll$GbgT{+Erfjv0C-Du!=<wsl-i6s*k7SRqoXLv}s&%pC|iz+JRnL>dv~H_D0VZGDFK6CHU=l()=VvOT|$HLGP@%5p<rg'
        b'1K?N34Lp11#7zLIiV&zSjmRBaNE$#J@+AJN!GW7eCr-p?%p|K=cb=r;JA7BkJzClPjgyq5WYMwdb&aR6)8wWnQ^Wls!~L1l#|jBm'
        b'27&$*y9lXiUQOAJy`kF^>n~jZioSysW!=Hu86Vjly-w-*T{9i^12?^fK6*B~Gp}R5s{K|c*(kJUAPhRP0xVto521>h%BsESCq@2A'
        b'f%=5GPQXe9<_tmLsi5jCC@DQ$YA>r-(9?Lu8rOKHm)~KDRFQXO-qXV!?PU@pY1}z_Or|=Uz~?Db#LE~3ESxbfiq)0d*eq&gWVBmI'
        b'ShGhOB|4#$Nu1m$h8j;u3f8QHlq7j|4wLu<q!ifJG5vU4wuPC%^xuHlKu4%|me;7)?X}=Xa7EA<SKr%-+cqUTaGy6prJ3EcatE1{'
        b'OXv-B9Hcn=zwad3{%>pA%WYH3)zj2a&1@PDVWzsO%@p@=w|W4OkLUgAGF3a1BBG@QOBHlXqqJc6HZa2Rn*lIc6XUnwnP!Jzz6i1l'
        b'D$Cg{f_4uCAY-}+GAdV7rYs^M(k#x${@phM80&tNm=Y(0f<7oB%)Y!(#~A*AJih^)lYnrc^2*h6&A1-7i)I)h9tiE}rNtH_wU+<4'
        b'5Ef8b67RF*B9g^#1H#G_IZw6}NvJP$>>8kQ1n7f+)sD!d5LC_nUM7-oF^W%(1|ZgBy`8uzIr)m-kRYoF00V|9ODvH9k&fpfdYAON'
        b'6AjjKp|$av?nIE5d9Gd;UkDPkxWXIEJxAuuz*?3lirx2xtwg~_O~B{^sw_)j%95F~)Ww&2E|!W|RU*4!0uX|hvN;#6x)BTXU5r)T'
        b'QIxBm8n|ppoLRjclB)A9iRqy%go>ZzQG`HRgmtQtXx-xx?ku5OSZAf=bewhl4eR|u&*Kq+H-cVI54Wc$a8>46af6mwOK<2-j@lnU'
        b'b}osNTZFY1|Bs*>wA_~f)R-?uzr|~m%UTYW&_mKfUw6XlqI+RnBo?_h0sD++d7l&>vq;^EX}Gnvocz#&du$#ZdC)@YRtqm$NYBC_'
        b'x!?D?+zJrCp8u7i1RuQ42-T8v4+lC&RU0WrOBuBylk26$JMk-<yAP25RKnugx)P%I61!VSu^yr|7@bAX+mr7jb7nz8|1xHIpl#H='
        b'aTs@w1G|GJp_(?T7b(oTs6hMZ!!lJvq<de`v*<?Y(lXa8dX?U={v|T!F(UUMZd<Xgx=M)t4+M5XK>TaMzOkFt$Ek`yEk@xxjqogv'
        b'P+k7U?Xu}sNCTT98pXQzuUpL#=D1*|%mU0Yvj@h&#i(;Y>9Dw*E925Eu5ByhNbv{3c*g%;(Bj&@GETp8)>MmY$I3YPtzFj8O`Bag'
        b'<rOD`Z!$Rp=sW1Wk#jsKXT)y>XD9lP1;LsEJtW~JJa_`jL(b74?Z(r4tm{?45(rbdpA_E>(Z5wjqpOvUp0g-5halc$jIM~}d$4Cl'
        b'SN|Mlxu*e0U~azx!b|MgB-!=8y{{XGxqafMA#3&xMh2rOV}uE2gA`^^RsxJjj0Hu4XV2)1GSzWeVOCG3yqgiFl(}5S_ehH?c6}{A'
        b'PvCTMJ7P(3I$@`}*^fw88W&T##J(4Sn>SMQB(;4-jU&}&L!afQk8AKXRJDH`cC_MyAQ8`q--qt{@t!;MPy8PAFXz1=K7CN}d63SY'
        b'1BE|<JbNtyTv_!Gj|<Q-PrYdprKsnuTO1wTNNy1XX5Y|^?{*0E=c)~jQoJfxjl~()aI%cFS|W@viOA%apnrlfxq%xE<A9D-oTRkD'
        b'Zo}dO$2Z+n^Qdn68vWPyKZV-7Bt941`cs#4N}THFpZNWD|7Ss!^Pnm5zA~2*_#YMr&)c%X@4BE<Ab^VQRqx&g$tv*y|9hjno?_*K'
        b'X}i1kR@qB<yoBV#vSEX2A;EBhWGYJYX*WX>)o#sY_&;xEh(Ps^{~hJYSJ>k=nsmAZHs>~HmZ;=%oV~JVtD^_Kd8Gt1mtcy78h01N'
        b'+=nvo?_I2rR2BUUYoGb%O;#vU=?NVh#HqPcYR}>s;B0ir>6U(3&N2$`x7}PNrrTfaV)gUWOUZyoY<)QxI#W+%KHZ&G)#avYOWMcL'
        b'B$HjM>yqJ-C4z8kc_DlmFA38PflisGp^H8qlEn<Qb5}12o>~b_nzWPo0|4G{yO`{q+~eJhR)MIRdx{tL&=Oi?GE&cwWjREdNf=T='
        b'N@V!yfimE?IMV++2oPl!B2-}Q-@2i=DfhBn!T06(K$%v-E$;TYY=aUa=lfs?tIE~UZkN)tU#8jI<#s6mDgVd(1EmYQOp!YmTPKBz'
        b'U0ki8&+2?K&8Dt|rFw%Obyn+}!>-k8)l>mKMcO3OJOu#8LEc+<SCx5Wt)OSkBE|Zb=eV`}roO;Fiint~*2S_E2FT=AhG6erEroe^'
        b'Rg!ZEx8>=;n=*|BKuHi6v`wJO&b<>&%>2dHC|vcfNHj|!pTzus1jooLxqQz4eit_2vKKTcs)tNeE$vHwd4L}aybx}Am$ZH>v8bdb'
        b'mvpgMYdIsZh!;vO#D(fZo%Ge?xe47St-|M;gZD8%2)d~{^XjjBk*As034De1)_Lw`xBX}AhrcFBB<x<lGj?ryS6OnF>evOlvD>XR'
        b'`lOeUzB^$49KQitWrXdO@*3N^4dlQE=kaSbFO;idRRce<q`10%cdWF`D6Xi+KDv!!-8;cg<8aN4rsycOmIBV^UGf{qjb)}>3FvNX'
        b'r*un7C3GvBd)Y6*3t+=VFu-gyp(>qFCML}5Qv$1ygFVNC1NmhXVg6}o?YYCIY(ZJ_{Pc^YxGd<|D6Uw8pNDoOf})LTXjivx*EKgl'
        b'aZRt>*-Re~Y?Il^E_x%Y$9)X(B`Ex8+m2e5edI8!pH}@5*NnY~3ZYNv**74~Sx#eXP^j`L)HaJM>(W_LIvl$t)4mpSot%KxP&;HA'
        b'x8yubPr%-O`EU(?hmX}~x^vH~>aSs2CqWOW754{O$z^(yZBIGmo2v-6|04*iHvYi9+^u^FQB}2HF&V`<J=p%%4-dN~mushN$pqQs'
        b'$YhPw7JQ?sq>8M#pGc7={Jdt%w%vNrD}pJtl{-msDzRICKj`3b%TgSbagRIQqpVA?ekNJ4S#7JKP(S`=%q$>T_vrdovLZ1UU%3Uw'
        b'z@00p&;%cCt&B@#UC$vfEit>ba%Vf#in+9(C8<p_$IjN|#1Vv9G6XsFmJqOt^TAN8R$+eTCOwZ%zz529m3P-EHhqS^m^$v%Si|N&'
        b'+;D2ynysSlw^BDfb7}y$3%dK&y(SVLJpnMurDVmaAhx&!_hyU~(vDD79+t0vCd4geqy(nFYGo$?qGJHmn!40ZGG!P2@Hv<CRGqR+'
        b'E;$zS`1;u~K#Q0Jphe8I_zp-k=Z@xF!e^JDXEDp5vpX)@)4Tulr^+2)ltq$*>(yl@(tjPhGPpru-aUNkrh<;UvU{7$MQ!@<N`rEZ'
        b'L*WYb;rpRY>(`9+2>A%=e^^;p21pm#)+@@4l>b~1(rA4pXuFV_zGj1h&a<so=iCeeRy)Q6dp3%#W!FqOgm^BjIiDW}E-B+Q>tz$x'
        b'E<NmaMU*9zIM;p(5_~!Fk7%DF|IZ9scLs51{W1~QH)@sz?eAdSq^gTyKW9XDYU(`$Gx!4^lI0P#QfCC=G!p!^+<6ZF&9GlR)pmVr'
        b'u<NI<#&OYy=V#5I?><Y?FAfypS8lOlX_PO5NIEg@*ej8~IO&IS%77r^>umN+|BpeRkr=bZ?bKm9g8Qz^S>)iaMe=FEPVO=+Bxz$?'
        b'Z;<8ybK=qsy-f3CC&QGgr-(qC?o}sKIpI5^nO8dtKks4_(;9LA0sqO+f9P~x^>QO5;ZdjXoo2iwW+)~CSAr?MK7oMAC*m7)SAsqP'
        b'$p@|9Lr};EJ>T(nSrD(|T}j4iH%u}1lU+#+V?Ww;!;oO_>q?4L*}J>M6k$KomBh+uM{-64B$Sk0LMO4kt1HR(W5Un&!(BTf|LMOT'
        b'KG#FynFmkjNEmk7-?|DSdH;!EDrD#m@fqPWYaN}9By@$}!-z=FkV2SiMESvY%Gx$E)-NdA)M-jgQwd|Z`Yw>vZjvx0rV$NV-N6yO'
        b')cjhPiKl}I@5Vxqb9Sj5P>O^if&C+pK9=t=K&W2tX~sludzZ<z$&^o+$OwB)SG6_8WB*H+DPK@zFijMvTP2U)Ysv$86pF`KCG#J;'
        b'Bc2QKqhoO=#8=5pIz{!O`4b^A-ocky2{1%=)L9I5UcMu~9^!#J;+0TdcSk%K;?~=7of4og;-Mqnc?2H8%M(D4kS0txP-GB_B!z$M'
        b'ESMPbwEcRl??nbWzTOIi3+zU!aYbDahJfAx|Mg`)m%#c4W-vfNQx|`Haq<-)H4xF`;_3BpxJG?s=%35)g2H%61;$8iQfrJ|xXWTB'
        b'@aiTSGZDM*5lp^f-Y-;@3++!IW~H*dH-#dCzCUy?&ieO}PFW*q*W+Xjd=?>Z*u7uoHFQBzA|}OW=X@8$chjmi)A!d)bFSfhe~c`i'
        b'(y7sR;pwq(LzWK&fsaFNeM{~7%KkfSNfj%yj~<5BLf==U=Y`r7i-?wc(pmB3+@dsqY};&e>j|Gr=-D2^MT8CO-Vft40dWz8ak&u2'
        b'MF=Y4rNi{R5Mc4;5bvWLIvt^z&}pB280LYzVQ{Jv-P!Z2^LbC(KjD{_(vgJzU4Cvro1iS~{yO4nS98}7+b?wT_X0!n<`jb9ouX5H'
        b'F1!ljspiXFK5YLK%Ym#Ln@6=42jk2lYE4_BoXf@a1}90`97^Bu??DnfU3e~r*a-`Yy4ASl$?7*>c+Eb*Hzb^V#g`>TL4*E5E#cFW'
        b'&VE6YLs=)R>S!dbL&302aro#-wA}W}HfJW$NFI!h@<qlvT^njT6si-1_r&3o0_(#fMgUV4^@L0!XE?~8v*)@FpXpJY>q({aW)_|#'
        b'=N2znyUPB|){m863$|#c%M$*Yk|iG~p<&GCwZ1y;;66#^ugTPA^{eCC>zr>5J0c#IIi*A+<;(_lkIyzo1YeZ%$G3Q1Q?E;V^AM2F'
        b's5Jzh9ywiq*t_Sj>$uwO5?XHtL2hJRqvdYb3f?~feSkrX!(O|O3+xSt_^Y40E_aglEtu%tez=j+J#*KyGFnB81`ak-_G6u6LfZS%'
        b';YNvl7RFU)MVh}H;$A%LWYX{mI+Moz<!~qf;@DYC=>9lTD+uS5^EnbiwFRSVcB>((>JzY##UeX3ip!WZ-5*9^J>#A`%m74^@IHAM'
        b'T>xwDG949MDN(vMhU`6lov0Po>szPTW5<|;;LqZEexja`H41eb477-jPJL+G9;NHG?m2VT?a@pTl&PrFl8uYZ=3oi)Kbqek;!48p'
        b'=&n=KW%Rs8k^M4)dqSpam%S<j2%vLPmFY&k#modxKYF-RM9*&&+aE)G2Nx;RmK>fgUcD&!<<*e*9M+_TvrTifcptsQut$@7h<gNE'
        b'sDOELr4lp)+n__~W`v<YRaK*OOJQB6rzYqqtj+v%sCq$bY`t>#D>1fuJm~5yrgR_kS=ISlBH|a#tBYTs^GVRn5Q-i(@P#f}<jUVR'
        b'kIDHWNQ*3y)XIA$Jf7mugI6{y3-~tR*8)}+G*;3m)>Q>RU0S`sq1vEaUpvk_6&Q8d8)^@OVB!~5d=~`zb>mm$Z5G$>)16|PtcV7x'
        b'`WUj;HK|cxXRzCkk&S{^1qr)Y88KYiDQKkFxkR8(&h#o&4Z|AQAui^yf#F4>F7(eug^Aock&X)l_zi}neuc09?@dkX4$dZ*;j<J('
        b'd|iA)PFQZF{oKJx4;!^<z_vzGTD=Z}?p`TAlt&T}4&>oNnE7p|3DhGB#BhBigsi{2j?0;)`X;MQoAWwq1ND{=5C*jTbDd$m!%ir?'
        b'YP@gW8Pxq89FrMopLTHHcZQ1Bo8aHP6c!LtXTFY2ox0tWn-N3MGlyS7L+!vC8>xUW_i5+uOC<b;viRaGBf*>x_#E$@IeBi(INe$O'
        b'9=@MI5uwA8y8HQM<zOeE9A0n2`0elDj^BwNqSerO8-);Fy7d2sS9|BNOH%m#5OCPvd1nDf8Rq-=d>@~`_f8xgJdX99yJG9vt$RCn'
        b'$nFch^*~Px+=C6(vi3JRE4M`bLhv%c%$j#SO!Lj1;Xd$6TBwJCl#z-n;c<ShgWK`%eR}HONFA8MQ{*q0d>f_bJ5`s$?@olEdXlje'
        b'%hv><#z>G&9z;C275_m?m_ZG%SrbQ2Z|wAL>^vz08L4|C$Ui6WSLy-Tu6E6m4sKy5NG8<8m^A)+6(oe%nBO1^$sp%0seMDoNy<?)'
        b'_ErVtrOoZ&tYf_*5s%5pu3T{#5Ah9Lvoq&(sJ<eBp9AqDX|p<UI-7#rZ!q8~4Aw^u#Bqx{X?dU^$lcosDh1EHpkr`_oiL|D>Yg>0'
        b'*YzImWD`R;j{Sq?qgqOYYN76;?aUcFCzHv9+qFiIq$Tjp<p()6k3fE?-E?TzIycD0{7bv{{?cwh!MFSC|KD~+zqHE=iCP2OuWTeM'
        b'>n1p&;%i}DeZf%|Rn;7LJ{Z<%VGT35M$?^mOe5`PyIcF~K^dVsE-=7|t2%d)jifGO<n+};-e?#!dRCw+$ggIhetp|+Nt|`)zS*~M'
        b'GiE~vN-Ejj{N0gqb$fSH({*GPF(MWJT7Vh};TP`-i3DD~CSi>D^P0uPizE{j`z)1gk!<K&^W;5i*7X*?*IxYIp`_SYRqI`Nr>BD`'
        b'$sjA<BN$y8@6?}s1w!1lLlAUpG1c|D%{n@a&)t822%->RwStu1<k|_EHxHr8#MG0l4*AQiCD$BO2d)L{vjXD`pv9C-CB+XAH)c&%'
        b'O{J3J=5LrmlgTlQ$^iaXhhS~2p8>%fIgykfeIuW&$ROw)>vw*P&7VDlFWO@0-9tRT^S(E%cnT}xO*roDLl8$O3p#Ntbi;DhPqGb9'
        b's&>n;*Z>cId8h=pW31?tq5ra|Sjoz9Snj}~fk^m)G)6Z|<@~;0*zmfiA68J+QkfA(?0STerwc`_Z9mj00afEfNW)OcB+zNxu8|Vz'
        b'{oSl?RwD^x1F>m|_?jZ(zWY$<c`LV8#DM<&R8agu5Yyd!pX50|2k~91;WYEv8)aItN+Ljv{(dLs(4UweF?HvmoOgmolBhmEh7bPZ'
        b'KpUVhUy&7m4XV!JM<`V+-*gQ&fq~~RAa;Zhsy?&@uiVrNA=2==?n@k1&6-0_9u#OaQLzp|jgzX6s;S)O)1_54_=*Y7=fkZ6JlLyC'
        b'3rVTksFeQ7It7e;=Cngq+3rLlH2U@0PKoZl;22)@GhqHe<PKEpvmm7VHqH9+@SUj(s`LM~T;6ikd7@G1xtunz8q(^Q-;w9mO8ygW'
        b'AB0>kD)8>V!0kik<tWb?o_QZZ<`o|b5;(-x)5Dqxhk$P+K|r1x>G-8z_8&V2UsCRLfZ+gi!Ap%iS6lrc(#F_mMkl$eDj*E<+~T1?'
        b'&`btk0W#>HjxvIaJLJdvAz?auj`MW>^&wUlGVyDpSXWAAozngZHdW)W-EIqM80ZR?@ddFVsG@2Zhn|wLq%7Qf`Y^2|AK#K|S&Dl@'
        b'C2?fMTtd~L#QBy_l*}Ui`M*?HplXN;vwdg?B{;ERR_k_B594GpPbIj2c8pDnXk@n^I#kaSMv71+!mP(EW2h?9U;H2R|F<z2D@cb%'
        b'#nV1~XZqN%=-P%Wih@LKmi(EPWV-CFVLE=zo8_)G>#A3B7dk3>fqq<|Lp9|}(oB4cnft1v0-r}r+PL&al`?55le8KiH9%xP>&Ouk'
        b'NmcVfdc=`AJ!5GCUS7P9*u$`6_`MF0iWqpe!;g1xFnGE{{1cycs>6Ss54_WXFIZvd?GEvk;D)TET(Y8x&pOdj(HL6qYoi^Jm31OE'
        b'kxZ|h;P4IHglUl4r&jyap8C+alkhTX&L7RW^-G;j@}zLA9#u~TJi%Yq;QGkG4obC?GH;{O{?NvGJHiWZBq}0rAQ3Y+cih$!NmM9a'
        b'9}cMsVU>jm)!>$Pgw|((oENED7tCDT)+h{lW9pf(b-$nkmJRWZ@cS4UWQ&%}d4!l>P0R6_jHlc1Dsp}sw>6A~o1}34f0ak$!H(N%'
        b'R}on<QI2|yqXS}onlO=+DHGJLXR0@QpYJ#+pk<I=s)Qn{4<hUBPY57NiyX?z1Gqn&q$9;fC_O{<kQ|!OO_hM?-6{JQZP>FNds(RM'
        b'uxQa$CMHVBWwwdMf9$9#af_k%Gw?*-FIms)idX%&tilxtz#*!g$QDOBbVc{F#nBGZR6NnfP6VsMSsZ1v!%U2Xq9#(X*eb<d6?NRH'
        b'W9muuTuQUBBcI{5_ZeZ`aI`(Fla=vk!$cA*RFwq8+<pa4H?b7Lx~gGZi>|gq7;HdHPZC1dv+Ej!Eq=AQJ!s(ph>7?`{?;JD-P<8<'
        b'2<w*@Te(>s|Dn?dYOmpVeA0fKU=}nV%7_1p>U^;s759tnyef~Kvz144i5*G$@f_1}BSXslsv{|u<T|iGJq!6RPj;YV6pK4~0Fyel'
        b'>j|#8{XcDj(>&<C?PF><LLSdUmh+G!c*w8wkjp}lbuFW}m3CprPf&eV`+t}eo$as?+-Xw;p2D7S?)HDzgYCOow_a;!_492uY9My&'
        b'5AEEI_Bz?tEA0@u(#~CLcdjP3e&24^6I;J)xBt*yCk^>+Gq<+76HzzY8;2gsZ`#qZtiAWf3{_H;*1+phFjp$tLz4!tD9zB6WCc)*'
        b'Jl~Ew3WmODhdlqaAcj9{2N{EbPuu<Bdw!tn4G+C2>y&aYwO8xG(vP*?3=W(Dlv(|Ksv<B5+Hb!D=yPFztv7--p?>*XB*uUICC=wR'
        b'K(VfStB33_w6@9|MJI(#KHSHlrPHNhzYgf1Qv}v)!iQxh7h#E}jEUl9i)`k5g1W0h*J?HIA2`>>YnJBK5j1I3QMo?Se;-j=V!kmd'
        b'RujY(R;dmd`AI_cFGjw`>Kt`wK5efR46LemxQ`Ftn5w{J-6xO?#=Rsyd*1qZhE-9Oh7P@87o#t!KIe4VXfe7U?z<=Cewf|fNzwBG'
        b'hX=6hgW1YrXZv)~((L4yav|~eZ6SI*E1OR7FGF9cP%ayDI4ld};*O2oQ5B6%*D0;<LgTf{+s&7V&!cYv1oE;LwN*pSWBj=Fb;YPu'
        b'XWO7P_=R3Uz`L&fq%glh_bV!%34KZcXy+|!$M^3}Nj0)oZcTg0^tUg^0E^y4K_lKOhP18!Yz31FzjQN+;+D6^d`)r|><>587P7BG'
        b'W2(7%ko)}@n8J4Mv37?Ppcr_Y4B6|hvCNNKA>fu4SaXLl{n9UBcsLgha=#rb`d~X(+6L%AG<3@uD|~uKyLKY&>_INO9b|=Cjn-o$'
        b'Z@^`u0Phq469rC1z{+t*#(mSqpSDF&Cd{M)Z_0!MsuR7bx~$<qA?hwD<c_x8o^V_$_L66BzMbxa+|+h}h31nstR;pW6FOO_jWhq!'
        b'hR1Wejlk?-&%CiV_TJG(%pGlTgy!>BhAdFAq{efQQ-+BEzqrFcdX2^hl{_zxA`M;%)1Xk=P747GP_aE93eA@ZP4_{1qn-)Vlh8O1'
        b'Hj0c43e==+lj!}qQQ7o%h;z5vRz^(#?ep5T_y$lSFzIF+uB!XnLdA;*F<?nTR=|%^hzZPnHk=zjqvW+pzzoSMB#Pf}<BqoGi6McG'
        b'hg`(4tPNw)5G;J<V1_k!2I+r@NPGOCG3vBr1sV7>sQWVL`7oHdsMSP0uX=xc!LnrqC5mM?<}6#b%;f)78NmLq&EkI$-yx9@t5?(~'
        b'HCdH}?D*>Ct$sYC`nQAlCQ(Zp6m*E6KqmsOJBu)mfw#heG8eHXSDia?PW5{9Y0hs$T{nrb?`{KFA4z+ewAQ}(9RRS7du!{*cDn<?'
        b'eq<k9uiUtHPwwD2qJQfkP1JJFM!=jaG4!cR?(y;z^~4XSt!g_d>lD&ct*?$kufP1R6(4Y-Up&d@zbds(8g?B=$Di9p>R!Pj-1P9c'
        b'rI`;h+60v|fOn!^3KlLn*hpn;24Zc9dqAdIDYs{|)-E<lo9MjC&G>lBrXOn-r55~Nq&g5`f^Ph^4Huck5Y$ESYD08e$b}nn-S&&='
        b'cxSN;UABmOC=t|y2!dOM1zTnHxpf?vJA58GbT=XA)(atsda@Q{>^5q9DSCVPjXU=?$`oQmnqPLI&QL1^GKAIT8CTI$EduQ0v;F14'
        b'n%}3@Eb8XZ0O38w^~mm?21(|(t=^~F9+Ndv_D_+>TyCrDUU%w@%)xTytPK7Q%<j}h-7XJaTla{DJF(=uSaR2E-qJRRyn~TOVL&+S'
        b'YFERmZ$E(vxcr0VvkaR_8{g^{MqB;YARH(g1$~|S9i|t)-C_~NmL!e02xVM$n>mT#vM{}PQ5)|LaBGF`<4Wr&zRS%DrQ8E;u!eH8'
        b'+juuXVRatz4dz5}8Epfx@B=Zvq9f|jp(MS8j&nIu-Tja0h7bbZ)URk+;G1iuOD!sKa!DjD(?KMTo7Sd+wx?qK5R}p^F1<~4pMbj$'
        b'V~(t(SUHeCNl)S+04Qw~$FwD>NKV5?g$3N*ZM(!=3dXFR*N{lMyG9%F(M-o{yJ|}^NO3mNl7~m_N@7WI7QyM-O7!TUaJz`WxocqV'
        b'a}(MmE0h@hl8=sSi#bnnG(t2AFRB(2Tzn{;qB=h=W`&504M({cs7Q)u5SgV1EzuJyOGMm69xLju>KrbL4@OVe0m(`Xo8HH7J|$b_'
        b'#^?#V0n9iajJBYDVc_B|uMFl6J=L>n6cRK2t!`~<9tAVRE8^32rI?Oe2_Ig|SZat8Cohi!f_`w#J(U9O009iQ@&K$@kXzgul6VQ{'
        b'b7M8Lk8qb;b7M&`uh1>f13Kop)(YIy;l6CG7z+RM8|K_sSW$c;yjPvuqIRt_C8l{kyLI~at={w4#4PLYdG#<cE%e$G_nTH@Vp?cp'
        b'_r6R)+N>4;5;jTBVIc7FEeu=2iSWzYkKEm@VSP>(I7fLuYJEc1D6mgL7XF<^^#Nf7Mp+?w)Pm2s_K4@7H@!<5jf7DY7qfz__^lw`'
        b's7YvXo)NGSb0nqWM<r$1Fx$!^Pp7XGKic5NNX$x!+m*)$oe{IrSBW2;>*OPmJ9Afw=TG7z)h)n~F&D)1b1WFOkZ(y!q!w2y#EeG-'
        b'7A-3&5kGn#pO;(;8KzK1@<oZoH9u5kqBOlkoYE4CL~gIV0L2!M)z?=)ZE+bwu@pc2(_%}u0BIly(IW8I;lME@Q0CVM#|(k`*C1r|'
        b'--6&+68s0GQr*!z)9eu~5Uei^^kFJ@7VAU6dhfL-WNz&vpx=6*Z+#Z2dZdMa6EeX=Np(H9SWN=V6REumQ)kz+nPNKPPj<FA!C5@n'
        b'LrR^R$xvc<8(DFaaJmR*9^vgfh@NQy6tVkS_y-{qaF^|gR)F2eCouE9|I@ni66t*m)AsObk*6i4GOraAJbZ#S*K282)l#f>?xA{b'
        b'F=qTNl)>6|i)`CPgLTR)4a%AZwQaM=)}Xew+ycplmg&n_tdoKYPQJoK>3RTNh!Fk~ZohJa%=-u?RAGW?qI9uU?w!|)wKro*u2tsE'
        b'!+aKFD<Sp}#{SHg*0L8N!H5YPd3a=OiC*S?5EGupgr6XLHpa?A2>-dd);km9f5f=?rxblz5?)1{>AkDf>`qw^ZO`D_F2Q_n8WvrS'
        b'!OEv(-n%ij3}ZUa)#{zzX&8SL<M1Ciz&|G9;%o*Pk<y#IO@!~`=M!sJ9B33U$!VJopkS{$K*urKcyuv6deD#@Hd*3YA&7xV;eg>o'
        b'(ibId6j<LG!9oH|3Kz~0r;ExU!cAz!7ukh|Ovw6UNtVnjM|3g}oeZ(}p9hm>Nby%odcQpg83xQSB(K?<<voV+yD^^HkZFD8Rwwe>'
        b'RKCNvFe^D!^k3UGB#%?gAhF?V2hk&+JPuKn5iS6+;}#<S-N6v@88L^pVYzRxTzyP9afhl;fT<Vx)Ey8EY~!n)4_CY0!Q@>}V!<!?'
        b'g314unXW45!F<H$rvF>+;!xEyeCFbR%`_y-Rqyh3PlP%khp^`b9*6!g4z!$(3tX1b@gUUXRtU&pp_d1~mOUWDYbv_0Wd#*#Te;d+'
        b'rRKjXsgjCW0N8dArXcbcG$n@FrmMIWnrfEh(3Ec!K`8J%&UaIC$Y^d9Lda8o3xWndNl3s9#$be%y>$oP_L2RxjM2yQE5rN`ry0wP'
        b'0`Wgay$4$c_bA&N>SghDZW-amvnb->QSTE6lafjA<2a57kR@~S$IgT>uRWI>rKRPKLft~JHD{Z4&9XL)JRuu6-cNN>-F@ASBG3BK'
        b'>Eg*(=IqBu$2^gvuBqyZTjBdXsGAoEpOC4RiUWH`%tInjy9<P_rRvN#_nUhKWne~cI0&k0qY#3+r*EP9dbA~EiyQcJQf3{&9d5y>'
        b'Dps;Q8V&E>7S(3LBqCIh)s0yLWw?O@a%0T4z_$)M_k)S-)-lL#v((k@%)jpE{^ww5`JyQ{ipbDbWt$fSLq#5t;Xw`1t0uPaHnXZh'
        b'<ctD)dq>9I8CnokI~&aJj-LMQ!H`u8hNZm{3qAlQZTd^U0+Y4@>4vTMM-8?rPkp3pZ$CTmmOS2pmwVh=d??X6Z`9C7;k|O2GDQ)K'
        b'?~!I`&DtP7a^uztPAyd8yKN1&K;CG4w)m&9?=`&;>WB7rKOWo9-Thztp}n&oUmf`W=*O?_=*Oae?Z<}yLqBr<Z~e%+vmek2&n436'
        b'B1|%Yd#ZS8wmCoOxkx^SCmASv>w(ZohAMHVjFzz?LFKHwi>zi{@br%@1Cj8<<10pdry#!5#jCTEUz*k^w$C5Kw{~K8m9lEfN3pMp'
        b'`y&P(-6EgYAyyFm3CAYSoL2{$54sDQ)t=p>OfQvl1#l;gB0;V}$~WW3&glf*MkSP)(_qtiM&lX4U7j7^Q1J=wff`6+@A4PPgq@Gx'
        b'GQc8GPI=#JX(V-B5n!_nQ5wyDhMBzAhj->8!1TP{%)Qledry`-hB$NnmheH5buFODe-{ipx14={uc=wLV;0#oLt)@&<i()3vjvUo'
        b'wg^=N0ajL=?z0iRi)Ve01Rn4q1qCO`!1p8OowqWUS2x#3sa6M1l0Kn8JQUQt*Uaq;H<fb%aZejK;C&O?w0G{u%Z&&3b9-8Rkp+Rr'
        b'M^gIPe1dhks~BG-!9)t&$H9VEHu==L^&^_z=0;(t58UAc;r-;WKdzWaJ9xlb+XD03ULOM59C~~Vk2!5?(LFf=HN#5dKmMgMem7!o'
        b'bLcCAX>T0xzR=<>BoNMagyRzsTxE-A*$C@O@d*Sh9(D};euO<kveH=ZpIg8-@jlyPuik&>Zuj;(8vyv5h637a`lS!Z7)GfwN$IJO'
        b'r(YnH2_a6)@CrOEr7tu;CPUNzi5B#@S|O;ro7c_Q0~RK%n>_^~PYSPxg_GPmDFm(4c&W^U{jWmai9p|v9u*!2R~E*I(TWVvCYiiV'
        b'fS-2&+~@(&;Za%G-i%~h)yy)_s9GuS{1!!zn!kWquWV{i+SfGmY8;8#t10h8EhhzdCsRtC&Thf)<)zRxX)i(MpCWJw^pJuFJh$u*'
        b'&xR(4(gsuT{Sj7!#}Bs%_>BPXeJv-k3H%@?;KI#lp@p4-nF4Ers9umBmvIUjHZ}8Sl+xpJI%S5{1UIe4Q!hF_wWU=+S2vROx!B}P'
        b'(m~b=c4WvQ;qkF1PvLWMHn&~?Qz)=u)Ir8Owvgf<gPk%ip~d>TD0G&9CQnal`6qdj>?DD$eXvBHRzY0dtA@qXD?1$>&TJ&DO|sLG'
        b'e2k87Bt84^Y#m3WO>U+QtahQQR>XVhRB<A7EJ;!LI||*qAFpbFxK)Y9Xlte>xIez5kqj&xX+^h{75+8c@czJp5zWj4tx9NQ!AL9b'
        b'D>IF7)PXyl&LNq_T|0nJ3u-BIq(G;p%<Y6`#K(Pq2g4yh-}D)n6x9ML|B;?O0+;Lhp;_o5x^Mu`9(=nWxVlkjoiPF&t$KyvCtZAl'
        b')i83KgD>n4JG_(v)dC?_{fMvnIaDQa5&bpP6;{8(SA|LHx%-#8ACA>!Qb2nQb6Ut}KI}`#cj#~Xp6xe%-o69;Lm9F5qdt82XlU#c'
        b'HGF>O0q&@ec{8YXD4bKXG>y$QJ1K^VT2_ZA5a~%5NC6$88EUSnp$h7hP>7j|r|0Q7yo|YRaEf4S;{MQ6IoO^?Q0Vi~lv|f;ELIo`'
        b'^|?Dq@e~3@#4^fdr(A!Fb{Fa`#Y(m~%2^!AHK49*FF@`q{G|C|nMHJwo>)+lx@_6H!dHFf7NYF<P1Yq?Q@Tx6GQMO#n)Mc!BDaO~'
        b'>xq&?GUs99#yyL<x&x~Bq$Sa$_(8(bqxQO*8^xZr5~psSL%8<u2WnoWPVEtd4!v&?nx`n&R`}Q+by>{zHESqUdMx+n1L6{pZ|5`$'
        b'I{I93q_H^aT(L6eqhLuk;$HH61IHqoYgaZG+YjK4+hj#a>@w%X?FUyaWpnV_Vp$BueYAh^MX3eMv}X>ep8g5N@TWnd<UD@;$KtZ('
        b'-WQ*Aq#)@%(*HrQcwuw>cF%>OlQQp92Xbh<ew1|GXmJxOp$qQ>L5@`5p%hk3sA7j$jZ%CeSe(~f|AxH5`qhxva)9?2SV!<|E4S=G'
        b'1wNp|{r*73xnQYqyP2>|+`hX+ReXQ5TU@I;OXvo%ouUId{P%mf#Rn?zElbXP0I#p{|L?)S=in{Yg`Q7WYq@Kux?XsyL$GF}qG`SQ'
        b'8DV7|S>X#lEA15Lh>5{UrH!-M-m=+VunB2tl$3~Hk8d~R6VBpzUvZo#LE_ZJ`!sR8)87?)f{hY7o-K|G?7hlr;_yiTDKWT12^HKu'
        b'ik&;7<`P0!`_|8MKpEX635(TEto@abi#q_rBUwp`Ytf^z_L=>FnnMD*fE2|zbTOtx%T2{m@koaQr-#rbqTCO^Uq<@ecc%isc}@+5'
        b'N+y>~3hcS1n)RFdjn$WR?+ke-hX`0W!n>P@^rw~FB!pB7xPo*M6THj9^P#Y8s@%02H`YxPw?8XOw?0-_w4YUpi$uwnNbyC&vl_oT'
        b'=aq-R%^%^b?OrS~B?;;$>b{$1?H?-qw)v#2Qv})hn9U|BcWt2KP~6LO-%hjoheEm5Jj^Zp(hCjc21xNbV(XV)_mmhQDc;KJvDY^9'
        b'pMZ>a6|8e-u5eF@Hx<W1&N+?J>-7!VD0RQmq|`SxD7qWeo4)NniZ@YMP1HF}<ds(CrjKj`il#&Arl$AQe^J_AP_u=4I^Jf_Y~n8q'
        b'`u05s6>C6_SHZa3e3a`SB3B2LrZyeo8hoeU-#^%)>~<)c9O^TZk=cE5)MHXW=HR#m&W}mwB<bR>qanFBj&kq&qT5e34d8YB?jm*W'
        b'*D>~;KKH)wan8h2uA>Uu^Heu9^r-qEWNq_pJ?{%;)j(DyRlsMln%IJx>jSZ>J+v2;mYvN&1$#Bht#g`K`^)>GWz~4W?yo2K1S=Y)'
        b'*3X8KE>-I4Js{!=4yXg44@1nPCAM!Sjy?4!lTe&)eF|A{$t|Cj00IJ&eelg)1q&!w%{tXnB9m*b<ZH#TKSdTrxtgeg0@31liOIE!'
        b'Ke0dG6Z3U6fI9Y6lu0Xad8vZJQ1<Fj_JQQDBa4K`p2E6Ls=y>#JP9)Yz-PL%#3mQP{h=9RIJm2Da90LM|4PCsq~=SDgyy$mY@0zM'
        b'nOvI+7Ag{E(zOL!@Or#MxV@C3C+1!v3l=N7H!F*TkN;e=NMT!~PLVDV7C032#7{G}76F6Y1^ogxfF8MA>s&?UO`DZ~Ej|Xv7dI^@'
        b'SRqBfTzP;Rh&E+Wg?Wg>VqmcOgh?oJ2&<pkx@`Xr2Pw`W!bqH@>k4*mEBxJlXO^g-NZ~x%O-t#CHAUq%#KZlMpo@pRM969sCXT4t'
        b'T+S9NSfS{4BceQ^nHry2>N8Ro&Fdy^UE(!P(W#y%fcBvs-#lUARPP5XW^si$T{9!0pvZhagQhq$CRlWaWEEKvFQ8@i`+PjtE8HBh'
        b'J3?ePU{tkEz~~g-94|Kx_3pGxFQbi8F+_O(r#Ro|PP$Jl3I<Yfa)RVb+%HZJ0?Ea6Ld~LXI-+3Lwwi)<VjHOb`?`RbV;wS=UX<54'
        b'vnUXCMM8F8mu-<^i4Y?4MbN1Ve=tvI`bV%JTQOG%5u$PhllfzlF?zdX1zFKVa0<RNzip=Djfn()F`Yt;@`O89C^;FQr}eq1=)k<I'
        b'eDcZ_4`jaUt<Sbr40(n7dHEql5m3KSw|OY@3m=FDik=z}V_K2QtrL36QB+WF7wHl4i9(C3DRaDUafQf4T~vvrTi<J1vt}KzL`Y`X'
        b'Px`#yH9sMPIbrYg@}HL}Jk|^|MY3|jnnG&+{g2Kncyn7}PqRBuxOgR9HicckQapcg*+WG9B3OGRCF1!j`AAHOWc~-1hX~VAfrYwQ'
        b'-BK!Ce?jtSPB_IyKmgi6=eL%KvBv1Kt``2o*C}fh1zsEG-fqTi1ALyLR9HCByjYx8Sl?usDBD|6{F0Y@y%|?d6}96c$+??D?`B&d'
        b'S|WE(l;Ou7)(!DJl~@&p4lf7-ljv^)6S=x(J~i2DTFZLvFEyDYwD|yG(U%q;fEFGwxh7a71wC7vmsu5yRb<a*pSP(Q=!PQT2i%c_'
        b'*<y-49b=7hOA4%i9P*a?@O&+)yE4qfO}DBF|J-B}#g^#CnJ5|eTr;%!Tyv<0>#Y-wi3RRNk!SUg_myVeAOCHrUS@4`uIOR6CQ`R*'
        b'$h)1-3S1uMM>}`jz2}sAlSXOLL~S}h=MhCgw)%=$x#@#t*$P$@39&hI-cuJTA&{~eSghoTh->okdk4f%D}I$Z*K2YK+|=_l<$7pa'
        b'BNea=d7le4a6Z()!Skd)F_`(F*PR%3K}PyD!6ezeo@GPcr}<*mb66}VA=oJDq;&UO9o(#R_9&{h?2*PV@^Iqa_g)bHHi(xI{I`PK'
        b'>SpovAj&P=sGAhbydSxI2Q;7x(z3wAS09!IhDG)@-qXvQqok?AafH{>ObDj+6gLYgYHM-x)5P6cIl+IYRA<x|l+t+%bGOImMeKe_'
        b'Ri-bbDO&YUYR!dh&yN3car3$H#QM9^p_D~mn75FYyeOGVuPtn*qnACuE$U%HIFHy9!R7+<?7l$e{4{ETiT}S|Zh{xq=!$EjIHG;S'
        b'TXULWM9U(G^>O3ZG^8$Dnd+Le&N3Gt5??!~xl`Kfs$H{N4Q1`~y}V;PPIYz&5<8`h61$)YPkoC07lNSteJ%7~91Zy`Qi@Vj@2PZ>'
        b'IVnVP#@!`GQmi3vm?Dyxk|e|bqW+(tuZ;Y2!UiZ(p(aX9-)OGxW6lT+#{2z01zGn6OizTWu_^tPhPP+OCbvGty8mA3?9*J@XE5%s'
        b'_zntPLiie@((p9v{<_jxulX_rVjsT2qWL@&iS>UK)O->OPx222H6Mk-@&3<(n)gHD+5WRZ&6!a6b^nJ!%{!rRg8#jsePG{IJ<DyZ'
        b'Vhl#Ye=4Zy59RIkpA2e_hQf{h<3UYtDEtrqG5+nko_#E%pKVfQgzZmz`##qU1^bb}kQc|>KVUZ;*q54m-B2VmX9>2tnhcHj);&83'
        b'KkA5qCDd5CH$&w<$8y`7(l$5!zm((l(WIeh`|a;?z6x<VHkB<mM7+g65Nn&EHq3o%EdO+Q6D?&QZnJOO=ln=;F5-bhf1%}ce$y-J'
        b'tDwdnS3g~yC~w&PKM9)JeL`t+_*o}n91%B%=;E5{)HOBhIw!FGgVpiQhug+%A=|#{*9@_z8JA45Tw!oc;CuW4P2%ayo1u4^G#i0b'
        b'BpWH6ZCY6xzxBy5mfI8=O0HoaJ7qp7KdBBiyJ~*O{@VJ7v3_)C2)Kr(e=8Ac*Rl^<@=0ek)ljM_gwr*Fo7d#bZ_WL~IG=R#rkkLt'
        b';T_`q*0D1q=6#zk!+^2mtkfDR^!U-CRjFI4O=qu+J%*HOpq!w3&A^Mv*qU*c_2*#PynSwRmO&eS317$?vyZ<EV{zMOXMb>C^^?vJ'
        b'4OYQm)00x2<$&GbOr=vgYg4<cPLVoOZOEH7_SW!>vHrO-l+Za?R{x`aTc?hdsR0^1=KF6n0Q;kI0hww`-1@71&W{D`+&M9zk!N9{'
        b'xpTrivNd)L&K16`O=s@_1NmOXKG0VtrPh|)_6T~iea>m~yF;H5`NRCmC^FSf{XcxY4Oml0_BcHEBbN}anh%V8+2-C52&iomv_xxn'
        b'Nx*<;cL5dAw!eiSh}P~}Yt^>wZgOoQSh}mBt$+y0g-8HVpw_A_U8F6gmhM{nv8~%~tu3v!Uv9U46sz|=bA$HxfB*0EK97dEb7#(+'
        b'nK^UjoO5T+fgEen!Hqt`67ev5|5A3+$I>q12JDj&*pL37u!BDxuy|<fl`4JdhO3ba=pZ}8pzmy&bm6<pJOHC!nn6qs`TC_d@IHT_'
        b'`idC;w#8?GDj;;<l(<1XTJ<*I1v7jhOdK!3<iV0dva)*o!U2m2MJ;{ZL?p+OK?l_XeHoTO2JwFkAa3LB1C#h~jLbu?^ncI8=#4Uc'
        b'lXLaS|6S&9azDcwA--AeC$u|oK(YjBPq!xWD6DD@9y!1&Gs~wAqzhXgQx2yu1_f>C$%c(baJ6CJ1+u~b1zBZo`4lL%_OU1^#U?_b'
        b'f+L#aUmS#TmU(of9QK2pfq`4(I<|Bd8`B#zNuHSA_Z|><fxB|h0Mf5*tb}{^!2AK(?<Kr@_J9cQ{&UdK4ex$FR(+-aF9$5LYGY{B'
        b'aO(~Vvz9_NZsH(b6uW3hpJ^hvrvAtpfya{>1a9~KrIAZ|cn$pNz)2jSd9J+vXWq08dAI%V{9A733&VTv{jm0^TG;=|4x#p_QaG6D'
        b'5j?f?)!q{aJ-lczI?f21bn^vXGZ_~+xTAoYsMX$?YL6Cz%WJhM7?dC;)@tt(#9*!ed+xD=k)Vd$JqM8Iyijy6Hs2wx<bcgR-{!V5'
        b'|CP9hZWJks6e%6~R^lGGk$HC{v#jRa<o))?`*#Wbd<mVlswr-A>{wmP50O|0?;eQUu*BDC2XVTa&*Fz-c!Om#zIKZ3UGopv$hb<~'
        b'G|-LTB9kafx4JkTiOx8iHpbb0!uHBpVDp)W6t;lTRuofcIWU{rWD+cy>M@<I=y#MNN=N2JVlz?BJm)FG{=A!>IiFakDK<t|Z8}^`'
        b'y5=K+zuR*^4V+-@R;6fKYy(EVy`j{nwyr+t);5EFXsJ|tY79bAGcLJ~W|dpFMr|@JW~Xm_qQS3ihN4BiQbCh?BP^~uT&{?|rAkw9'
        b'huW5Ni;aB4dGM3047JVqhBdq2sVyneq3Zu;EiyQZN}SqN1sN9nvS^jO67C{dmroN@x%LB>j!HICCLdwo(vk9Xe?~v$pt8gXorCnw'
        b'KOi4~qvU{?OLPRe1<mlz>d)$*h+H(r2e&M^j96~6y>h1b@PzACiM?apCade9n_p_FG`QVMYmQ5@AA`*)amJQytgX^KjZ5lh;{+$-'
        b'KI#P_AVO!H?x5gQ)m)KaORjjH<O7=A^<QvP4#IFTlV?&bfz9I&(+i#T&EB_qSyHCbqm%Y`9<<S@e!dW&;j=l2iuVA*-1=tjm0p2B'
        b'f^+bO9i1hE*ZQE?AOWSuPmv3q`UQkY5ZqB*5Oo^`=S!wH$zRsQ;a*OA&}kM7Ich#Y6?YJVc|IQ?JjvS)p3U_iTv`^xb@$HSWcq@c'
        b'L(jax+L-II9eO@7{*%Jn(K{d_*lj2R^);y%-ZOSI>B$$gY|@?=w8nt|k^@Kt0zdY3Yj!jXC(d}Da3uP+_!QJ)mH&-1BbTKA&v()I'
        b'-Oc-CPxb;~7A044Z}i!gzila{4JLKr-UIsg86mmKeekm9aRqj}r&v%L@r1ExLD9kQ3xE=qzg;-kXN!G%HQ!PcRj%9pnR*~uD+c0B'
        b'KS~41nxy6stii3l>~tF+&ytp+?RP1l6(RQRf)WK($LgXFWEPFZZU9iw^EfQPEPva*=q}S{$);G~UjBCV;ZkU5(E{uR8^**|hC=5Q'
        b'73UNt`JeaRUKkgar1J72e8aAtEv7c8xK+J8FBopa{*+#M*B?;AaM#X{8UI`%o|xU4fp4c73^cy10(Fl6rni^$&vx;Fc`wc1mDdZ*'
        b'{esM;PaV8=@&=b4m<?=PW3ggu(9ZwGi7U27-`F3$Tl#=e_~VdpP}=FU?6UVlGZ6z2-tO#bueH}!vZ`Wp^yC?AOE2~n;Q}eLMA4t#'
        b'TYc7_*bI#uA{*~L&3v-3b(01-@-RpYP1wYQNB^GYwVPrEC~2el9;q|~Tb%I--qRfVeKb%6pX}=Ek)u9gPsw<{(qTk|0D&b%*tTy-'
        b'itCn+CteFpWp3<iPXWoMHj*{BBA?P9ybp(A{}u8F@7Zl9YkJY_#kKR-&DLewNmnDPJVLq}P!d&}v7pjNGLIuxsI|pZR^b?hEXhnm'
        b'i1h;~{NikC<2T&J{nmB8AQXyPW%Umh-V)%|HE}4(mKwLR)<!33nM;x|dX^<GnaPpuvYo;o=-%B(j?|*s`AZg_!mt`Z6G)ithNLTq'
        b'X8(}d_{{k03RZh5-{`Vn3-Q9wSZ!w9@KSAR9Lf9}6oLIbpUdi4m7%?1jtYAc{0jRZ3ogffd<xYLkjw@cqeH22KpihbC0Y94A8}dY'
        b'`ZxA3Bqr>RYr^9&3&!D7z^7&h;Bzk@tiv$20z$L+;5MB8NaBM&4C8N->93f)Qk!vvAu&LVZy*Ckx@H*;FCW~2%RUT=Cvn+BQbj$<'
        b'Y7eKAHUE@Y99IK>_Y|XWLtCJsnYQ5BOz7@|P~mf^P!pE8c0llPLki6tmUuA^z>PeFcrhOLIVf>^;O+X6jWU?O?T+9$|4zTyhSM7$'
        b'ZQ#X3jKgxMv;*VNAaQ@$58?sej-4Qm<UoE94{;VGUIO-E6Ths@NU(`tz{J;-BAa+J6KXvxab9RjsBuHiSGCWPF2Cfh-Y<MW`js<B'
        b'oH!KJBl`uTS#SPKz6}%zY-V)<V?&Kk;x_GPRZul^lfrZl8R($rsF>}z<GrM5H5o{wYyK>|?plZ88;pvP$FPIN5;DNk%p;)pmCN}C'
        b'1)C7yEj61Z@Bi!<%w~P#N1}Wj99lwDR=}_e2M&BdLf)0~>+osWs*Lf73z!>fDkZL9e?&_Gs;MGfZi!nA8H7k?RsR5x@vT=b4;SId'
        b'1U3$+DBMs3@Ysa$-@=?_t|x0&NZhYwWK48T5yrXV4<I_SB!*uuyOpx<_nRMM<93=G@X-<EoeR$^n5&Z43JJj=7*?)}F>N4WX<kYv'
        b';n4#)XF<E^0CtUmqem7>-c%?WukZT1JhpKoUrSy-GR}$e*?#Y>xD9>R7;nb>&Si=0bGCpf(@!#1l$voDXy+p)(9Wl)@Q+m5$dOwS'
        b'OPQWgSkl$<%1<(8%1V0DL-;QT%K9f9gNMRK-s!q1;i>oISTv~_3A0C8s@68VP?!4LR-4$C>3^R4xyMExs`(m<ox|0QC==Gzt(Yn@'
        b'{kypzdt^8VU7)1@Cz6hHfs+1RBpvSpCH?D2I?)A6`ngDYp$nAs@kqME^{&L7jii%YZ%fusdeV)y;G+w88;L?b1u(ObH(|_9M~dvP'
        b'8I`zyM$)}CuSwjyk@SI@VeE5#;b<)k%V#L{2w5`^CE4L=<VBQfUsego?*}HSO100Z6v&!=h<!5kMbcG^D%~XWtSo1<*dj3!g5qlS'
        b'gIfRB++YvSF9kw#U6CpWNLMFHimUa%%e~OUYgf7cD^(7Yt|tJdA=Q4n5SWf_9tUK;6NXGZM&vNUCK8eB#z^vHN9ZwyAzh6>Sk1<!'
        b'lac44t=QQmwOW$-MB;*xQc1vV&}<*B-;QQC!b@z^XpX$ha=j-B!B25pFXCP@Hjt%PU|0hH>)wS|aJ7AqoWAfJ)O5WeaZk#<Fw!H~'
        b'A9m#_(iK8W<M6v-iF>>U%aLZ<(?y@`)_`~(;0>M*8vpjtL){wB6FA-H(~OiLXh=r74WQ2!f~x^UO+N_XJ#4zbFZJvi_uNLq>g!T_'
        b'@CIOD^FdMG$s3q1K-hzAJ@o+LN!-^CiL2}xgthq6_-vBLH=>O-Z4wg14&1Mu06$j<j^nm!A)P1$KgVqWQ!43U6L4p42dpe3e*BG4'
        b'jKbwSkVwFNdP?Gc8yTrvT*LDFK@9UrJkWyp5{C1*#JS`lNmVd{B#3{*xcQ*uNsQYcVbw<f9Ibg2=x$+;K)%6ZXJ#W?qzjE2miKra'
        b'Nvc3tZAer9uWo|G;DIOLT85epQ17-Lo{VGGOWs*MyC7}8+n)w(jo$i*N{nk>yPjs#q2$`1NLQI8#5H%GBbnbxY#xAM?vuD%A{Znv'
        b't0gWGsO{O2m00&l>WS>JoF4K@0-~BLJRoRM^$#%O%sPqFK%1k?-I8}|&o0f4HaU9hPvl50Ze{B^vSyLQnrp@-j_Cn5jSVPwv06|1'
        b'_L^S<&O}edqypXjfMo8JJiG(C$EyKXpStFCiM!Ix^S?3h3TCe4z1S_9f5XSU9cWi<xPnQA$HQST{5Ucj<N94U9^w?*l?E(8PII&?'
        b'1z12gCYDstr4>MKXS!vIdz>B_g7!a^%b93blEnSH+q}t@AaNhbd1<t3hQxi?&1+T6bcuVvTOOa8HH#(g9l1cVf|(|9C%Z9K4c4ra'
        b'ynpZBW!(?x3Ff72f+3aO*{Eh?fNI$EojncEX3)H!T@14r*wX+>m_X<vyTfyA`%^JE9ya%~jAt4~(&JMwO}I}-q5Xd|7bk6`!S8#M'
        b'>e(3Yr`?loCGPMdRvC8J5m>cNC|GiQkeKhNi2I2m=&{wTS-!-kBM3y?zXhqnn|?meDsgB!BxvK<c%Z6?o7J%^*8SaVyzED57OHzi'
        b'Z@;!MkHP*ptoypzyc<sEUv_;BG6imfa?pGk8rR@<QWKt)TYv(=n*U6masPX-b*z^i8>D+F@0&gHIhXowA6*igmt04!(k(U?)^|Hb'
        b'dhcZi75EI@FfMWz6u}w2w09fsp9N?;mZc1H<>(VP&WRMesfwwRwX6plGIexkRcgiN%li`|PyQZhXT-$0jAoC8wkfR7c8h^2HY0`4'
        b'c=Ytzsrrmw@)!RQ76bj#S@z08XQus*UH{WvJs@DSrvV#W)E165_zcyjEj*2xln+N8vSiR3et_559}c#Wy&?MsFX;9k9JMLm*qMQy'
        b'9D*2}_eRZ65ue_F?d{L&_A61#I!Z}XOHwE$MJ>67Qj*jXJ*6b5B~yi2OLx`uVoT%wOTAg$e)I3^-(Y77=7)!auj2TxH_wc4cXV4U'
        b'n{Cd~)X!w|Exx!=F-ELB{~v)IwH>@_!43~cLF2%|>hO8SIo-Xa^F7iTtMr?eSmvr7<-J~0w=))5<{DT!H(u#9&(6xWWaZMfk`hy&'
        b'ay&tyUyf|1CBN8!yz$*~Na~p&0C_CCguph7g|5}+q}nw?U`?&oC<K0At4)jOr9wcc)hdKQpw|B_SKM3NaGfjZ9l0Xm^gGwM-}H`L'
        b'l(?eaV%;@vY46An666#w`<ct{1+@|OQSbFGb<kj|T4O7tY-Qwp&3qzs$K_w{rS_7cGuH#ckWh}Vo`~&#mVJPEAs@8nGMWzvp=%PR'
        b'$7YiGE$Xx-@`2w&dgLyU$hSeF=GWL;aB9Nhg+<tH{vn)o55jUf$knBg=uU0^j62iC^Jcwx4JaJMI}(`*5b!Y6)vwRut?za9@tSla'
        b'<wPSXSo-FW^<-C{Q<Jsbqf@f7`?7}$KkO<n$ssw=+DNDa9NnJ96kV`j!aL9{4x51ob%z_%0WL~AVd2w}zqu*hKOBqCjW+6{i8n=y'
        b'CY>KPK)EwK6iqk#c->;6QHA18;2N5AT*=!E_3C*4dX%3*WwWMlf9ij^J2>2Jny&zjX+$y;eKrjj?pnZ8&M7q$lJ(R5W+LJ&&HB~;'
        b'Gfqu@1|*?JR5oF4?ZW+<I)YbyBVpas)wfuapRJ>(m7)o`V;PReyZH|M!BB{$*?d?HIJumzJ}b}#C_c-;d*y&-1-QE%-Lj2_1{7ex'
        b'0J~|X>gyvPO4cX3c-`B(&yv9K%)~5yayVuGoz_3yc=zo8en&84vYsvsx7_<xFIjsuQP_V5Tl{pg6_2d3BJUr%MDu)?9;RfFsQ6gI'
        b'l$fx!)1H9IGa(nq7I-5j*o0ZZ2fHGte}urH+JtpN;N{wchlN0QZS&_oV%L3LvwR?V?5GPXM@Zx&`WiLflCEZ7coY*`<as%M{s2U7'
        b'AJHG&k8=ue&N**G7k1WqQHm7HhfGR|M-M2V=6lH9<+=&o44f3e?{eJCi5vMsO0~~Q^3`frr`ltRi!OQ>K&SGUPo*S~$9|i11Pf*V'
        b'ki2stcTElUcP0dP)M_26cC8RB#^W$5dFOP6kH}|>WV7acY}S;8E^lg=7<aFWL0%J7*MfBG<sqS|!9Iz-26$PDRHysz?8c7&u*+0$'
        b'BIK3HTSdh8%}b|zLW*5+DbHLPml-B~VxZl#ztP6il@DQmuZOpjBe$T+avWO{UpB=a!ct1!KU@-%Ql(7U_EzLRwZPLU+X^oE;%$6%'
        b'O359EtIXk|@dMWfRbk4s>&jCq(An9B%(&Y!?YE{hvg~u2jU#5is6`Bc;4jGLJFWl^2~*59$$ByD&E9XLjz)df;q#AtDWz<m#rjiq'
        b'WX&fMo(6o^IpPN@T!bSag|AZtlCR0iXSWbH9tLqM%6$qHC)WpZtV4UZ-c10Cl~rnySB}@tsXrDb&0=@E9HU_71+za)G7&$3-1}i0'
        b'|NG+SWM_t<>#*9UAY|ho!XNG^<P6LREHLCYf9iN6%=25=nZU{ir^wgm=BPsAb^WQIoiuFUnNPnq$=mM+l@N^y_NVnag}p=n3T=NJ'
        b'1R~v{qF6e0y6eIdn$^BDzQ~V#t}yz|j*JILc7|v~MXyPvDTYfsbUt1Exlr|-IZ^eGnvHVMhdD~yD`WL5iZ@-ujpzl*7OUL9tZ_N0'
        b'hAb14anh(sPb<;RVJzkb!zKejDS$+(x|qMNf9>ZYns{mY&=VSd^nx#zWzv0{0)*Kdv*IqMUbHLCI4;y(j3E<tW?}R~{i0&s^^tK&'
        b'pZyc}NspaeOfD{GwKbncWC8A9J(0cS!ydt`ys@8simXqB?<NJ~@A&}nk`MO$pTqEOX&y^<+S8YA7zjwcgts$1c|(bZ`c-&+@y3VQ'
        b'nM*f-%+>zFq}#2CTrfx-<~460?>T<Fr~i0QaJVNTRCw<X!<O2z>ZGViPd~|P#P$@}TQP`k@t3_-j(4GXyT9l7;hz4(J;8w<?*Oj7'
        b'>)x=C_WNQxA;``GglsfOnSPR36{d%if+pQ}(x(|{Pw}U1!61(v>7~v@qvDBcOeCHQz-32Mk7(W&dyb1e{bEnBrN`SM<MoHIV4hxI'
        b'HAqD+d3znd;MsklTf<`{lh{E@JWc*`Z~Z2`zw{j6+0(zXC+O?(`eb-kT>qo4Bo<#G@vg!H2RkDbx;%+3(EP~(P5O%$UepNYEg1H|'
        b'zexF9Yw`JO5xMPCB#%2w;ZxIj7=q1#tcl^I$85&UBDQaC2I@9gXiL^+{i{r&Hr)SU572f&$lzshac@3I_(B{KR+NOCgkZAaNPk}1'
        b'uNVdK3H!)D4T{SJ`7;5OTQpjcB^L_O9^ro#ItEle8H;k!XyKBck|)k6&<uABtLRlEt_aPzP#L<I>Q<}!4S<vBj06cbA@qrq=~f1R'
        b'(}QmhpO)%hb<79{zv^@*-&!r7HDAz^w`PBbA(;jlN}$nwq-R+}%ZieY`svv7%I5me0F8nlclPy_VwV|fil4qVzWe(K-TteymxQq$'
        b'Yhrhde>*vv@({vkwd0$W#mBD8G8gurSy6obk2vt;UR7Xts6Lq`(`ZnqV6`fXwDd~*q%TGtx=^CovEs}M_zBzK&+6_Ysu!Bp75|s^'
        b'*=E17+82)7-F(ZgFFO5cb6Zx0m4j>@hy8eS^*exB+Pxt>+VylAZMLoEKib5SB_s8(^+o~e_o)KAhgjv$`Bjz0HP>O<hh8!WWu(81'
        b'c!L=K^&ITmVU#G|@l&FY`Ij^pUB|(jieJh3->4FOoAmV7Be!1IrrELe%vSgb-vNI%c6$K3XU-JA^RxMmNBOawKPqazl+ZdFb3=K5'
        b'sM5}UZRNB1tl|Mh4RFGO=ds6var+$oqonuwPPch(i#|*aV%ITp2W;MlaR=U_LD<LA_yel?^@%G?8|lt@ugr-Uj|a4IMS*PvFRJyA'
        b'krCgPY|Qvq63eVj_{dDG)&A2wuvU8tAmCsD52$1Uev6i&P2P!mi;_>Xe<4lEiPnbBG>6T|6&neWqk(8ZTnywJ#wJ+OMWV0+YR*yV'
        b'(_zfa4pvt*+=8ZOp=H5Ug?6H3+1Pt_!d^a~D5fNr>|Aw|PH88q=#phInJ2evc0AFjWXZMhq$?R=Ipf)>Tv=EkXY!l^v;|LQ!^wv<'
        b'kFGFJ*Yi=EVsXb-My*?T6-Q+1ym5KR=U@{`tA<k7(&1MF?Q;YBh7-F(iC6xJKMp?MDPP*@jq*N+Q@ft&?mirjPJFTK>F&-KGs6rU'
        b'?axOm{fo?u>{snpJh+L^<4=r9GNC-gDp<Xtc>CBQz5Bn+>(U=7=A?we%+ctkGVkM9RO@0I%Zl@_c11HkN`}{l62}Hf@1OAt*LgV('
        b'>-uh1c`BOdRsM6qv@x@9-I%Oe?p0zv=Scj}3C)QYM-vmf4P!$?Pi~LgKY+FHvvfB(NA*&=EuAWUMd8z?Y<uXEZ&pg)BbQ2ItSh<?'
        b'o2S4wfi3&mlq$Qmu$xtwGm3eYy}WoCD4I+(ym<~=;FD@IrdIks=C16+w$V9s4T)01)7j5p>i`i!rWcq!{fVDItm3}k$HrnaJysko'
        b'hRrpXCGNajFBOLg=f2!$<IQ+;eI4X`>ZTca<Xh<iX1ySB`!eJ|-C<usZk#HS2feb^_9+OjgNpH(Ir<aVN8SePYJQS#_?j~P=Z24P'
        b'vy(l_#-+|zd#&Aw%<>p^-3SlDY7J(K{7pA2YcsHDa<L}#p0vNaWcBPfdley(>VjQ4kH~#C(Whz2a~Qj4zrwl(sa}Pb>z38$;_m2~'
        b'7c6~r@r&{;ink?wI^oNY@m;dVY+K#SU>CXxQDf^YR!3qb^Q|=d)!Zf`raN&fC}4>>!!*b~LoYY<^=+<yb71V<r&N7^Y4G%IE}nJ0'
        b'W&g&Gp_B#FVFyma#Fcm=>ySZwo$}JS-5}~7Rv~;3N<|LmqJdmO%q9IaDqi)IKbIQ$Ou9RYy#<)TTMUk%<F#W5#j7uhPJ}5;<_-6e'
        b'W@iC4QMrj6aiL3s<*=Kqao{gW!^f2a$Jt&w%{oq9nWOq<fp1ZY{k}_iw-(3IcJ8n-cA;~G0vMG7c1|G-Ut-C_W<1*|CCbAkdBW(W'
        b'OXdqK6|R_1I5{%2`Pboxiyvirf#UEL9MPm02+SU@r<?%-pFipd!YZH44LwQOII=Ti0K4EtAu}Cu-i0k2rmL5WPh7QYG7t3$)8km3'
        b'$LolkYZ$9y<Fo1-^uC`K=HqHM+yTr+<`d(WFK0IU?3&yREPc8zOE8vi?2|1Tl{@0OCHrJaQytvh1w-ro4}Qbi^!fiq)QPOV37GxQ'
        b't}~}31hrno?~v+*>nCY)>|g`2rg7Y^&OxGAk*28_knUEEomf~@`S6|G6J3s$F1`$hwn`bkjZda4-M0Zwcu*<RmCG;X4{(I#73{<!'
        b'^d(T}{_|rM&J$y7d6see%nOMbIG86t{L^9EKc74fbu8_Mimxy0n}0Sxewcri<z1H~-{UEE<)u7RN*p<oj2d%%PgkzP@gokeW7y_F'
        b'YWFeX2q!!4aM@*f|D(et52RGBPucd4>BH}UVQ$wO@xrtdg{!+(HbfQL_7$0KUG<R77^Q#Za_Hmh0|CPNtFGd7G(aI%QIw5K{v3kW'
        b'eSI|cGXhoV*~@bqaDbTH=SWz0wpZRgTu#>fLmDr<#QYs}sGO9ltV`RbmOO3eQt}*!OLFHcm@`sJ<FDCJ?Yvm_3G5qfObS0eNO?cN'
        b'gFEtp1bRgr30%<rbO~3q47uKg6h#nJHmZ4BvRLNY79rO^B5$+N2q>RNG;$~PJARm>8tId){|ptqN7#%;QIW(ZVt-XVvhUUfUH6eN'
        b'hxw72ht-gWQ{C-}-9n(8)pZ^rSPB?Yr#;?Aqxy#a+q<CjAzVhbdG+tRA&<gdbuPpk=N1<sF13p<pKC7v$jO<y(jH3N&LwxHHQ=9i'
        b'{PUdSPzZa)OpY=QULI5h4PD+=3}$?u#C3;?cT6ct{(b$55+nO4hz3a$<7Lvg<0`&JT~Ty3^xE}6DII$Gy9(i&>95x)a!oHmIVj3O'
        b'QVvL<@mns1UWdhub)50PAy!opLc7<;1^Q_aA=xC5+JH&+y<`ZyXh>24T^7C>-t;axFdbE2>|0?On4ugF5Pi?9#lX~1pH!4=){i6E'
        b'fnA_)Gn>Tjs5mGML?u9KB6I*=$B#Wfa6n>{`ucuMS|93_yl;g|s`SrOjnC-Q5QsjF57)06WMto(B^At1QpLQh6-TcZ8E*~r0pocf'
        b'Mvh(J(vSZjA7WA<1~gkCSttq+p0x^3jRIuK3zZsArJ<k_d$M{<!LB!TN`uT>ilhaheUkeW;b*d*Qbes&2s4zP?eswM;~=Q^JxAks'
        b'B!-2jD>|fIC&Gn}PByd25gMl&9i1<bBeT(_<i+frEo+_0Le^GAmP>&Wv(VPyP>v=m*U)#!;M6v6I{3-P9JRBknN3=nFy1B&@Jk<T'
        b'-?#BGb#bmDj}#7~UC)QJeCpkCF7I>UtUO1q{f~}S`zUf{K`ge^=twJ@h_cR8<a}q*y*SkK3-7@4*n*a_u};@fCy5>mg}p*}V~$}l'
        b'X~tnRMCR!DQj#~`>ZlI$YoeS+2e%>YbR(`c%$GZM!d}@4@@80-xE0?_UyL4WsyQJ!jki+HNuQzQgMJy2%pkt*B-=4}hS_NBohvW$'
        b'{onDI@bUUE8-s1PF__@2zAz3lmyKSU;HHH{9^VEkyb^jqg+0J1zKdk6ZPs9ukx5hRlg&sbt-gd{NgPBNhxf@w-uN490KcY?$FsS3'
        b'^eWG*gWrb+M0~oRiP$zBmpa7c$MC(@2f}8`&^^QltepeDi{x<?;VudTBxQTCKy&YfFg%h0ct1B{JhgP7i~i=kY1{YKgnfbv*{InT'
        b'A9fnh687#0VaIjHrlg$KjGch3eT2Z~BD0vH{SUSQxUStev-#VwE$_yCzolXR#@#<ZX@KpHRc5Z!*xZcuy$*kXxM^AMYt#s&A#wx|'
        b'pS*Ay<naWYD3aEZ3hRjuHBuEAvHcKdI`PQpNSY#<Eoi<P-M<Ch$x@Lwwj$Dcs6#a3KHJF%h%TG?6}+cVdGEkz4XSPiJt6Lw{c8_v'
        b'$sivF;jR_;@}?hVpSZ;KQ3*c%wA?&!ysKj%fG-N;)9A2gMw~c1mltE%II^ch2d!H|K%jES*I8TC3f#O4BTF%~&cz^2!T=v71Z+Yv'
        b'nH8MS!4SRK5sBZcCMS^TgqH{#P`Y(Aq$3cHA!|4f#SDfYJ%Z?Y+<}xQ3`hkX@xF{}m85hP7l%;cwhqyRd)t+ABewZ}I(-k-pYxkh'
        b'Y7=FCNRIsu(*JDWaNcXUhg}cp*I!RlVf9SLo1R!jEKIg+q}R^9ot+MCt1<Rm%XpqPFF7lV-Wp4e+>7#tv-&4`N&6}6;7xVogMs7y'
        b'&Jud1mM*S{Nuz@&JJ}fEmEH{@+0sdl5`gZv^vA%XKucU`f~?Nx_lU7%e`N?IoQB?cpTvDBG>70-foY;kBOln8M~<comvrc8MZ|Di'
        b'mKMUXaPL4qZHc*{l-~NR(z1&#D5O`$^F>M}5J>eGr7P4MR~U-&lqF);&;%eNJ4wYiq{*^`5P&j5-_$Atjw+sr)D!G<*EA5xp<w76'
        b'5FwzL{`B`FZ@~_V`>J!0y=2KLIdroOW`H3@jtD(|Sx1ofsSq(y+&w`Ns4T7nqnksEDUU%Nm<o8`H5cBy_QMGO|G^sn^G#U#1y^q('
        b'D2J{d8F^pI6GsWT4>V#r<onApV(`fdqhzpb<^z)cQG$&Lt(c86jDd_HU>XUQ^ag{W6ju18J<0KhPQ)9-^h=N0RrZFLbe<yPnR%Mk'
        b'85c6(r*K{8N&Gi6A;FfQto>}N^=vyu&870AC@O=>S7JNfKO~m2twEWhBJ$C}dS9oFg2xMI+#16j9)MH0veS^^!KYE@dF+(F{F-A$'
        b'r;V<z|F4a<0Ai`SC|k0=UT4bqKK%|To}K|k7t8}yvG&WU5011`QFE#6C@Lz0%2s*?jA!oD9Lq?rfr7^}V6RE{LFpwKCw)+5#|mDt'
        b'd`vKhik&J}%P(3!NG%=fCA<UeFsu(AYG<eOQE@C4!yD#ppF`QL8!lSr(iUEA(=bE4rXWLYFd7Q~+0GX-yy;iPWE89Q&g$fIs?Brj'
        b'4(ZP_HriY*7>sH=$LE;8$$(l(Oli5g(V^d`FvnLPHj|)aov~?n+FZ)3ExZAWEgb_1ROu`uyt^<GHq)<Jt-kzQSQ^YB3G)cpcor?!'
        b'r+<S(F``}~64-V1*RC@XA6Sz%mpLohq77TiTWvGS#2KY*(jXIfsll?LVdzEm&>d<V=_@1H#~Um*gDuBgeE!PFN0BwFBcp-cAYut9'
        b'PB^aht*~YjbfikHPKQNRvB+GYnkaFi!1>kP^{?jfwpXRxW2(TshZq9ci!vAd2>jNQMX#*76H%viB-8)54yXz84GNy0T$iEth)2bO'
        b'1ZYNuJk2ZZbV*S`NqK#az>@_fL#sBmtTFQz+mNh}Sj*ZY{2Ugq-G;wSI!S}w8MWrWlRkj)_s@MrG)kFHGA2}bVqb}(#FVmv1~Q&`'
        b'0p#2q>|gF)Nq_pfn??@~?>kehS-;}K3ivs>LbG~hY2S~widdOCWZJ-F(VnJ&2_OTV9<LQ+>s~~c@E<+#=yTToeI?Y-6@|9;qm<1g'
        b'l>McnG{a!45J1EndnI^a-_kL|fWe!L>m(Za90UR=^KS|1pT8`BLkM>6^V%_6V&s@XNHA6!<E(A_Skg~fP?NE?Nok|1Q*|V_XCL5B'
        b'rkbzp+P%*ojdq8>KV#PH;4ko+UH*ML_>;UQJ<Uw&g=_j{*E~MsjhFJ9C44hqb7QaZ`u6dG>waZ*eLSzUMD|R>$<3U1pC8}zPmNDG'
        b'{>OcT(OaIpC8p_2ou=6bYoi(4Sv{h0M}7TXzENrDHUtbm!fveO{mhM6Vyucy{8(lA*Y*$jPMuz$47umj0zaiQPUZbl6qIo>K2Ohf'
        b'LCb9TdFa^W-CCiDft@bUY<NLO9Leyy_Z=;=DXaB5W|%}ar3H-{VO3|g6v6I0G+*P7yM@ZrQe@OXm1e`$z9zM$$?)Mhe+lI38u{XG'
        b'RQw3CJ8hI<>t{xr(p-HafZdFk^-VNO;>846M|Vb+Q=S?6-9Id{N&dvryHq<DHu&M~w*!e~CuOjG`x~m?u{6o6qC1H1QskNK;i%7^'
        b'H#^N*o+MVfdsr<FsD#HZu$d)6c;c*h0Ov%v%;)CpW8=-FKoSA-5UVuQZTDa<31t&`g9o@Nx@1;xDWH~C%ke=c{l>^|QX6BuhJAvv'
        b'IyH{uZrOL^+j9aGMlAy|JU&zJleyKd*nKDQrz-&jFvI4Ql9>MK`-0Q=nNCW9NuCUI&F+JDf)b658fqQI+psQSx+<}xH)<a+YfJ=9'
        b'g3`h!AfGWc4g~p%cBoB9?igGPi6k1!$F~x%O3-|zR^z=KVxxUZpII2a>Pg!kVgA4)KvRm?WeYEaoC>6;C3gTl_)VzPWe^mo_VA~^'
        b'D7OO%N<wfDLTYTCX8b4VDLN$~s+Xx~k^-L1C~OoQBpaW&!}IiZzeAa#iuL|G)c^00UunT7u$zp4VQoCI<b|VFsHoC<-w(0zfI4KC'
        b'`i4ADH#`+BIHE1jVaIB~`Zm2@QhfSSVr9)Ik+@NOOvKD@v1|?)E!MFRn*e(YaBP+`EZBbYe1ku*23U*06T4$$fg&=$nri*I9nq&{'
        b'F)JNu(ydNWW`_4~QO5#R;!_vu7$8Y}K0{5y-r5-6@WajqdZ<g|S1PGI!XRJ8S#0;`DYFa{H{>^;HqZVRt#3!efzhE?%Gq|y*h52>'
        b'&AAO4znQd|RXd-iEg5uX6Un3^N=Y11V#xuGUzF@x8)c6AEZ%z@e?8IXM|-b}?Bh12DhnTbP`UKTJ|N3WQS1L@-4V*8azS4DT#-gO'
        b'9uHxMKcFudFfS5xWc@ZQN>DTa_Gx!X!O^%=@uf$IZ*jntRg(VLPs2Ja)X?7l%1s@+vQ*`ritAcA(f(O|hU@~wtTk(KAQ{u|q`Or5'
        b'M=!Z>d~J|JTEg~IE#-My81;c<;)W~&dle1<kL+jl)YUv~FL?yJj%B`ztRvCjPbYvs8a(vLBN`#vJbdtSgijoqFDy2L+$7uY%7#T8'
        b'Q*_3(O$<@|!c?Eu64-2ckcR1sI&XKJ4$fGoEqpV0{D63Ndf9+d`7x&I5(z{(@hy6B95(%7@9wuE#6$f7)uhw<0WFhzzhcIE((y(x'
        b'>MN2-K~Oj9{uG#xoxA9*@iT*mgS&=<XA{bX&BV?R4ZUO&F<t~<8;Pd4CMA$e)*%B-)v%e8=gRai3AVFu6|k+1Eh_8`o}FHr_4Wja'
        b'iZBZ}oZ4@t5^eQ4UZJ#DXphX4s^7V=RRa{c5%|+0Ws+*K!aIORzLy?9M(_;MpZbv{8Q9#R31|y|l!)W+O4vEA>%^q3Z!zIrfa|bv'
        b'&~8e)`cwejY_j4T=_!@x2EUQZ-Y%Eb%Vo76D<VaE$<SBQ1FEq{S!VKEz=IW{_k7SfV_H_8x_GX_rxldu)N@Os$`?hQTjaCty4tbR'
        b'r>^u(^*$P;NTqxU1oWgO`bCse%e?;iZAfvt{|V6<MdF(wT|w;5^^jrw{Y%9Q2pnS_&8RvGzzbW&0?^Y}PIJ@+oyi(KePvP{t@&6&'
        b'W77-IbPPn1!B0CX-npbtza#`kJvpANtRHiqk1;*{9eaM<N{yTXae6>LoxFDa+pce=$$pwfuk2s%eJCiH)%A^|#K(%sfCgSiFseNE'
        b'R9xvWhazJ%8Eq1wQ*mV@lQuw~HfaiU7*v;&AE*loer)-+;5|d6I1E_D*RUoxT;wTp0k7t>&A7TBXldPTh3P>yp~$o}x8nTqxk22d'
        b'>0QaI6M?^;#JiEI`r(4f-3Wg^!3CUU$n?Af)1mMF$*0vRk$mu@hxttQZPnai=-ce1s`YCqhap(FyQBCj$O{;^8CA?%bgyFk6Uq0E'
        b'&6o&FVR77IB}+T=lpB7`YEr}Q)r&p%CaJu)M83M>y`iRqhs|~X@#Y!9$2)*&1|r0P@53<b9$J?{(WH(h%AV+0taF#gQ`ym=M!L1k'
        b'rXbo_Y0x>Nbaa%vh!JRl&83`-&Z*qEO<i0&1r!T|%nq3h#O8S_4NwTpJAGtsQ8~(L2VIHsnlTX+ejhN>biup{3ptCOj#j=?P(WX('
        b'&=gUI>JN9WP?xSSG}@}@ozKvvZhB{>y85fqQaX}fMOQykT1B6%)ZBR9@KfnJdgzyDSbL=#XyiS=vr<z~um<vqvJG`c6nDDnIcSC='
        b's4ePy)O>n>k|>lBzuavigApYeiRXP9C<Q80{q#V1s4Js}ML^Bf&tn=bV)C{FnpsZzOpXR;WE&g{JDlYSEIr>jM;^rb>80C-9?3A$'
        b'Og|+WI1qR#fDf&BzY0JT0M`iW=7I@)zpDLw|3t8Ky=UDr{Qgt?9*e@k^MF8CcJXP#(Ge&}o<R6Wlg44}K>E}0Xwal1$9ZQt4O(<K'
        b'8x;P)z9E!;8XtKAC?_!#M|?+DJ4P$k^<m^p+7kiWdxVY3iYlKO)OBol-*ou0L)&4ab4oMRNhw%#&B?)9m~MR0W$ToVK)wMsa#rQe'
        b'CMxdxPQPP{kgm`ttNh7vwehl(pKOAnXSnI5P32U!!ktY!=>%ssasmlIZoH7E*^zTHN0XmnFSqHK-14b5SPkV$G0^J0iZ_zNi|w;('
        b'@)XwJ1ap~0{4Mzb!bz#vl+ql7Gh0=5q22LaJM2;GXg0ZWV9jEjcIs$W593~%V{vAab_Gipy>g}?xuNijcH1jg(iE)Ll8od0q5Y#Q'
        b'gRxW5ZWXGV#IE@Bi)Fb1$De{?$}LWMHulieVGy$s^Ns`*U+%grEpBl9y`5#SSB9MA$hz~M!nm@k@z*7<J;162Gj?X_{at`P7Kuge'
        b'eXV`hC`L|>#1N5%^E*lNuDGBOt*TY2s*eS5G(A<t9|-TU_Fc!?*?hS){P-phWZ*TIlS{6%#sqmvl}g7r4_?i}3`J$yKyY2{$CCph'
        b'2rIO`+v%MB#t(z|8naa!VAG1;Aq2&8;J?M^kl=KA)dAS!Cs7QwJ6bVbb+l}LOP+Bq1`=kP&6iI!2nq*972*g4MLGqN50HM+NS0`u'
        b'h*g?KzQoqVt+MX$QhBJ~2fBI@2v(F+6*6AZ@3<;oG{Z9DEdepWL?Xs}x3_b3?ZH3c7Wpb{QsY(0?Bbm~KBva#Cv)!x*z_*HNUC<L'
        b'X0WP?-w*<+s&2xOsn^M-ILvr)Q8N+)_^ggA@*P>^75ejpmkI#;);FRLw4=@e5}z%S|Avb`rb3|`vC7uE)4Bh_2-wKv%<}1xgfl>c'
        b'bcEB+WL&P|M=4@NWV18LZwn6uc!esJno|87Y`**=?1f`|Il(P$hbf2v$jVShYCDSBtuh%drW^xp?so|{lND8o=h00jr+)EpWSH5S'
        b'QlFu0G(geC1$t~k4lcrV1ZOhpJKxv$W9SFTyRWV6qkw3>#m&f67}&fv!BF-RR9P9RQg&Or$e>91am%-m9#8u&0={}nsZR~7G6K@Q'
        b'C~30!N^)dWilk?JF%3^N6&XhcABy+Jw^Q^ozmjmmuF_?^(5wkGc}`+?XC9bUr_)6#6;37HKeauW*zOL{>z)BZqny)1^d)`5RagJy'
        b'd_UYK9~aL8J+UN)qvW|JlMOr_p<yf0UP7flL%O!0$^o*b4kbmUX8zu>B5=tzU0*acjpCLCa6DX+yCOQSiX-JH#rYM!n~{ye6dP+h'
        b'@iVAEmgMb@#euuXvgSY}>U=?lCSnG`kIQL3NEp)9#XRD38att_dk|OMW<I4a(qn_^N|bVza|S%Ab64Zb8f#GHsdi^@d#-|H3Xx+|'
        b'8@oPlE<TWA3Ah7fFX>(rU2#Ave)JZ{dtx4)8mr*TQN=14yOgsezP|Ez5gN@SxsSxur%C30Y5ZjgAMmUEfgE{La*8NdizA+ceEqh_'
        b'y&~4!j_(M)EP{-Ram`CkW6~%-hvaiqX-}thcwZB_qxel78R^-|vm|p|;`p}Ui~tYo`^iVJzj@b75-NW0yU@3n0_zR>{O<rIo>o<V'
        b'xe*`lR6)(69L8h;nQ-Y=_aa`;u65%NbeyJ5<gs;DNQwI+a4D_q@D3g@%hKRvIwOpdLK)5jZX3z;t#2fDH>yEw=Nd#u8%Az1$+XD#'
        b'ZG~?l0KJXk#_plcBhg}DYQ-LM^80{4StA52wb6a}`@olN0|CS2_W{I1n+ZIx!OkZywNff1-_D-31vQSy;y*8<)Mse!5pfkcn@ppy'
        b'i;uV3R*oy2+G)Gjs2vZ%L{uJHfVsVvUb)692GkW#OT`n&86XymWq%MIRieBtB+-khNGbQhPfBy}B6SwgBO9c=O;8Fl*2a>qbyB3r'
        b'YzDTKnoBTMID{O~@(i~^3@AhIN|`vJ2H~vJt@aMJvI&BDKDM}vX#AA48^82aoQn9tSgPtIW4w8yU`CyB<oHR+>k@m({}&%$w358j'
        b'+S6)#C$iDr?s&G%MyoOvDi9tr)V3Ve_*BBWuT?Z+r$yGeVxXP2Q(aG2ex@)rVMZ2d()6aZ)*Z{Ww2C|~2ZgxD+q(SNWyOrMn69lU'
        b'qM523Sj_#Y%}FMW&1D~VI+Gj*v9P{XqzSiaDOzB>U<8fAbCTB>l072NJor%CR$vqJkr{`1iaJk*&V0*~d~T8}R(8mDc8N^Uiz-hY'
        b'=2$$&PT(tR(j7C!LRMs5m^Ks+ciXzBBd=zB{%cIerb&LyPzX6Twu;FZ-^}%+*6TqrFvJ^?p<7+N`Uh@#n~hY327$DcHmAxoC^4@}'
        b'5kT&PS0DVJ*2x)kCOiL0IB5qJRp@?|K2xbFb$fISlCMzw)#q$1sw1j4`P`ssfbi9%spHmJ^Bq(U>i;B2MHTfDz|Ja;UM!xt%zPk~'
        b'ZE4-V0JKVfv^jU(Z}=48h$_JJLc7M&?K#=4S<*c)y|lX{)FgQwtvro@BS+YAYQj{JMg!CDHGTLEBuu9w<7B>r#r11OF&Q@=<4O8V'
        b'Gzy58sPiI__GOrtze?Qgc*<A-0O5|GILqvk>20afBdF`ELiLg8wpc{CxNBM)HxR6AitutiT9v9&fS@q`4agg&9z0T^Zu!8IOs{Fy'
        b'-?nixT1D#1{Rx7ItX)C8jDcT;C3c4?ECm&9n297#o>vt3`7#SIjeaXoU+T~O%>01mnH0Xb)2;F<ZW4N`d%Aain_ont@=I13sB7rO'
        b'=6F-PwAG!=CXBy>yyLBGyg!fhE3wlk*&3$u)&_Sq1u+|_LYZzlNoB&uRg7n<`&ZnbgLabpptbUq1X}<$PF3iym&S*X>FTBaORd3)'
        b'R#Pr%bCT9af?+DuA`OsD_5b2N-5Y!e(AP$g=cc#u<d=Gz1go&3S(4*90BqCGm#o9BAR!G<O$GxE;*tJE#J#gOxMs3ySy|ATf>Pf7'
        b'6(7jTwIx*^!uMq{k?QEwvt-R*v6I7Rq>%!d+&_=QoapIKV64+6?)YAOiFGC><o`;AFYaYY=X(U7oy5~wQNX5`BT+Yv?~vy-Kel53'
        b'x8~J6=y`6k=5E9}f|0#B>RkM!3=rS{VrwujxHED}-<dp~NeZ;XPZiXDNHPwz1Ro{dAyA+RC<-ISqnbN$7=>&VXr*Nq46lxfz)C$w'
        b')|gO#XDevt86;jAGU?}oEG$cHYS~JZgB)CtQY<T?5v+hBr>lr2`V)fa38Q?}5nHx%ifEdm6-Cb3C2K%?Epn^z248b=a-n}7A4voX'
        b'=;{wHtk8IJu+y%{lGLl{$S6AM_kvuC)5~N%$EaA|=rkZzxTuNrZEAFPX`A>u+f8#A<y3-J&Z_W-Y+Na2l2?p;4HF7;p~W1aNJn$-'
        b'y|0g}N|+Sb1?c57K96$pGhwO0ij=wEWZMty1vUuHcQr&181dnCSoj%8a5x^*1-B->5|qOAE5a4}9cR4xd)?-xotH@F&r*?sjv6ON'
        b'swH;<vzAuOs31okk(}nGRS8+S^w4sRlQD0&66vthWxn9lq$fK*2w<an^62`!ZY*%ph<QL_wQ23#8v*Ozv1l@%ta&*?m#J>j^u83~'
        b'|J-r>4(R{2K&p-$v7*8kK}beU1!1cDmRBJlrkdFZ<rpt)*5s$+CQM;>eX}`%C(W3gOz1+g#v0w4k1h9ZDrpIyZqipOXH*ukF$392'
        b'`t?y&$Btr`okxhM^}i~+Ywy_<b^Z1H-5|_0KXW``Z+IO$<;+x+pNmy57>VQ4_YQz=_3!IWDv6zrJD8o6_eK3&d3Yf&b&bg}doM7?'
        b'qGSq38Tz>e8||i-vZN_b0{S<9UT>4Rp3JsDLCak8BO4oVZP&kgJ?|L6h+6--<NKCgav-*}dh>XW1j{p`x{S#D#=0{Q*1;UMG&|ne'
        b'>%$wiKbHP-onqIMf!%S8FHbhb*fWZ^Uz_wv^ht|XxmQfH-rQ3`2lECDfz5KpFaBz(1A9rcvOc<L(kIR%fyi0(z-I67_Wp9V+`2K~'
        b'qdq#9M)guY{v)NIRCxaon6XZ2Ga{HD?*oCl1SSTdq<rt+TcFl{6|1aUkfwTyYP657s>|=P*ZfC%D!MT`wdq^$*L!7E@FosnzJ4`y'
        b'4L=_tgT(=Mwolcle4&XurKJ5Ny?bw*U#SpCg{RIk;~e{XG|d$S(h|Z6z=^{PiW9DlOvc<6NL0VgyEM?KOj9=Tkv{j5Em}t|D4cnq'
        b'^46~@U2Q2S*!)dJr0p~KN<ugmn8+ZtqZ=k?Y)9e>fkw6SK8Fg)uw}4{N&N{l*YU5phxcM;!fRNq=LuRq3Mr4x?E!;fvz=m9FX@IU'
        b'#42lGiW7aWAG!5Rqh?3bnWLIU-La;DXgYPzxg*h+W_{*cTyKv|n6c&u>E<{%ZV6Z{n|n!f@_wqAS8%^?=}H#(dBONVU97;{@j(FE'
        b'F(cq~&%>s6y&&-_m3{#A>jJ|atoJ@V?qRw`#g(?$V{PtvJXFEoqS9#ipUmn;{v)x}jrimOHri)4>hM+<$5IA6K4m)dLN8VE&#ys8'
        b'hUq9ykYqm~UVQ$<v7{xc+*~-(CM4fh;8PcgXk}x3;pH|qrdQ#;56|atU{rpXj~|@Li&|b~V}=8<_z?bDj2Z8s`GX$bfz5`*<Z%wb'
        b'Bag)1yPmc<NyUuM(;e0pfAWUfcy55CEw2~`-qeVJQy?6`BcHtCElSRK8~5slA0mN|2|nK<dw19BOHjmxyuj<~?Xq)p-`V=Sh#xwb'
        b'HF+O5`)|hK^B%_)p?7zyKC*H7dwKHnVkfPiOWT4(CVgkkRAimf!W-vY;^&Ffk%~{H`&9b%*L>-qw#ChuJh5Ube4)+KJ;drdpC=7A'
        b'!yL*Gph4A(*ux`HzU6SQa(jU`Xv}Zcwye73)_J?y&VWd129XjU4U^4=z~Zk>#`k=t%}}s8Z+lj<LEk|<_<l=STN@wMy3(&>?;Qx#'
        b'_A=g2S|%N-18}{91p@s+Dpp+&KHFwiRXR61KG`!6I5ZqsbL^1!{XKXBlJBf{VqXv>=s`z?gB}n5B7W4o9X9MW^LXP_?BO!mZhkH@'
        b'Ubq-lC6>p}a8Ea9^J}c;clb36cq7BF$>5D7zvgyx2EWE)Zs*rznj82vcW}ddoCmM-{2h^+Y=X?bs)}-3y{BXX2zUVTf`RSqy@35e'
        b'8GCKbKP2;KYy!S`#I0@1BU5r-2v)WYlEZ-#XMpyGG2)9!ZvUR5Ww-G>bO0Zy#6ig7^{an2V^5Q=Pvtucg?VjxiqxlLxg~A&<>qA2'
        b'Yq{LEwCSuCpZzIbHtj)2+g3k?hbuhqDe3`gFID`gO8>$20UkM?-t*w%w#r0u<Q}AdaZ2SZl39c*@5H`tLGBXhqg&6BBdg?#s$WRn'
        b'+uQsB!mX^@S!r<RRrN;QTR%v8|Ag_}rbyk*md$GOO<&tcmzmqvO?M~XKK5*xsV#LkQ8nGY=JvvlJ@w^wg~-c>r;N5>REuqm&6aGJ'
        b'!<XEtUxp%AuWY8-^*UU{)RsoM{w^I+<t<3vGuxcM*jAsMw;(MiFW*dW^-nS9xKk6%WN9fqMw%5(g!dUds*MC2cXxCzc3aR(R&+@E'
        b'M=!7p^P22<L)~UGBYpV~c1o}N0q;;{XuMN8Lg*L#$L<WO+H7mAp@Ua?$?-wyE>-dQ?|nZGg0#8@e_9`u(8f-KDFpCP5W&hf^<H6>'
        b'wK|3M_7;I^@mOfrAqh&1i;{i^3jWlJgO7DzVWW5Jbk>v>7)Kk`vRfC$>MVAPWhZ@Cv@0z2Mvb>g`t?`YnBaG<Bj+)W`e)Avzk$kx'
        b'SC3gq&A!NYEt>&<*VXCRL|EhFXMk(gukZi7wU-LLc*AZb1hCIZL%3o5O*uR&&bx~gjD$!LNO?k_kp2qcFz#U!<wJ?HSS330&iHZK'
        b'ZiH<U#KI}x0-&tEiSd_d*Tm$S<*w|xdFrku>}B@siryo9K#0mDf0_}LglJ&*vTVvs#`Xl&S7&n~>)%@O_iV~~ZV#+E`CuT!O*A`s'
        b'9*1bB_I~t^<G;;9?1%aiLg0;Z;KON{U;QA)emIEjp*+vYj0(f-X%*x{1#!{duGYp;*>TE^Z`$L{Hr}P*jswAB??x2zZf(Uz>p&~3'
        b'%$jTPR2dRW_A<ig70)vbPel(kX*_j9SZdxLK2#UGimtf+P1m8P6znt3R~N2qd?(ld)dp2>DcRmFPjQLo_Oin0Wlw9v$vVwW-_S{)'
        b'=1Jd<C+ik`mHx)*r>2T0><(XRa7XKW+FINC1_eL&vh!o+C$cf#^Ue6&{hwMFj={s1_`&;rvstiuT0Nk2k*B!}dp&iINr!XQtrzk%'
        b'brhhrSXYPdB~S9_&8>WuZt`q}VY7ZXitB0?_*e{VT`POb5#?wcjBGfOoifxswDaHFPww3O_WD*V8{LgwZ_eBGKR6vu7)|R^9$u(w'
        b'{K}uk>}+uCehJSQ)@Q3wBTk0nUr4}z#kA;@^k3ocxzTiR1+Lo|PvyrnDS2KeM~rVhqH5XW{Y@*YrIay#B~VDZp~=9K{yao2VbfHT'
        b'Hl4=!k*{Q5s5z}{RU?T%>zR$-U$q8vT8}7)0}BV-jQ2r2Bos;dY?L#aBI&wKAmqa=S9f7k?qb=Li#Qw1M%~T3<D8|HO@lH};-z!_'
        b'*4D6l;h6V#7*M0zo6<^=AjJ6q4hgDFoh_Kw%GxO>4RG)g#J#v&R}nXJ5+r0ZIL_Z4$C35ddqCQZ0;zc~;h5f9rfv0VTFqE*s?wU{'
        b'QlBMjb`xg0n4F4@>Y&6uf<iA`?4tEM*6<1JS~okW3L0D3{oVzb3vyAdRdf-FKvAgKguI1&HYu~Bz9d}_pj1#D?nl+<JkO~8PDC+N'
        b'3$vPoU3*rEfF9+DS@o%RGsaP%RBY<TZR&#ji40~MMa1ZcsruUVWekgq6IrI!h5PofsRfHB9?@ozvf8#6Mn`2SSe+G`7{4Q>>y-CR'
        b'3??PtWTvZ(JRetDt}xrGw;Gb^Qr_UERG{*LPO!03ZAdYIe9e8lH)02N!+@X00-hg+c<1KgrsA@bd%2T)KcGt(Gf7REmiAzpiTlT1'
        b'%AwE^3W`*eshbgzP>?dw^j_0zl!L+F>k#QKV<>W}j+{n02qQtTdIK?wO@E3(JKiypQ|fkkU)`&7P)3JRN2&_U6JDul8Oc&)%sFi~'
        b'q0l+#x1#F^ql5e-Q+W%?`~zi7nQF16>%W_m@+;Ey5h_q8Sn#<ClIcZ8LXklbNTIT56P7uqoGN2sB-I4I9_;1t7%U^E=m-LTh*M0w'
        b'6}6Z7migd#27$5((vYFbaG)$oR+&FRmgIzNf>zV`apd0!IVMIvkxb1ON1l+_s7+2Z(jX!4Q+u~5x6OD&DZU>2X3Y_$c;e@iFKUh^'
        b'42=F<t0zZn$mgOM?a8pFYpuw{Qn}F-Gfm93P`OIL3Mo$uWinz{n=l=2El^E}DRDraU0;eR2~eWz1yLU(u8bF%>0<63;Ywc+v{W&7'
        b'u9y;EXY1-@RbpklSeX#qyw`gkgYfn@brlJ2bsdihCS7(y5_kq5M+Q!<x6>3k1(pis1f?Y1fABJPO#wvbVucjOQ%iexZWeOq?Qhzo'
        b'XM-O!*M6xSNYQ%V#c)Np)>R@s6@#7rgh$3TDP04R02o4wo=xyHH~4esF$IuOxNL8MBJw$rMBIeYsnR*8Fs0HX+6?E^)T;a830Wt?'
        b'w9YX#!@*`dR26j>3)W9m(WML~=7(T(+?oRH`f+Lo!DbVxEoeP5C7{}gEMfI_=Tx=w{w*j6mI<2*^!<pItwk#_jfa#eZW48!+6V#&'
        b'%uF`M4cZXPR280!Vi_A^U=08`01BX)PvE@;C3Fq5cVwY-$~kSFcH|D6CpT62Mst>skIWMVPfU3DbbQbj6>P+P%CV>uvNY*B=QKGp'
        b'u4@=6X0iG$>X!@f!NsXr>eV{uR3=#h42{ldfTGbk)nLibYM%&QH+2oy%#=S4rMNzmfX_{VvXql`#Yx`YW~81dsG2C%tu{DTqu2?+'
        b'ZbXN?oj3FIBl+0`k%gPKmJ<pf@+>_j@(+*yLgQ6U5gLyW__<v`>zK+Jmt;Yzx1wrtB!FU=zIr=Bc_J2`EXnhDLe}#WZv+8O7;_x}'
        b'=`C)Ge6H3J)ZQrew$b1R$ARqtU}i4v11u6`@c#K1w9%T0?F4NoTV1MLg7gzG{~)932--*})j0`>S2gtm_#9Q%z{FQUXdtU&!h6?b'
        b'8x*00l5a%;^mEWoV?UE9p>l#zGnkG>?n3p^Uuo-;fNp_PWquLmd(f?%r$4N8&xzYKWoe@xv(jv|X^wt$J~d^AK5FWbyG5QtvrY$k'
        b'hR}l3&?HR28$sw9(1h23TQx?J&>di>S!Dibu$O@W427-%ZNM5dk~&1r+M=FSMZ<D*r?dLQG22d4PTi&o763reGYo>FT@M2~)mwpS'
        b'y0caIkiP?zqjYErNV~#k0!XOz{5BhuEZsfSQ~|VC9IX^7)r|Fzvawm+1~FS@eWCG&F<)&XQR-(Z_+^vvkt@96d;i?BogjfB8hk*y'
        b'XuE^7m=i`myp9?l*c9~a+^VkpGR8>87*M*A)WR>mAHV<_t}&_XK;ydT0%l_5O{wZUwMe<{J?H@T#bG4LYyzRE(}w?tuy=uL;>sS!'
        b'CzDA?!l(&gM8IxlAP^8*g0?)??vjY%QSAb11Z;OnEQq%5Dy7xBbT<=hG6^Wj@Jf*GCaF}Q(n9(WAM65c(Nf%1`=ZwFQoF2{+SXFE'
        b'h>!W*J3;O4cR&CC=ffw=+_{f)?>+b2bM8Hl7zw~KcQ5RcZx$4d)&Tm4Q)4cuiTqewe#tC92mw=t2%zIt<?oe!7+9;7!K;y%Cr^gB'
        b'dO^pcxg`bWZ6}z5`;oJe`0AkT&r9_eB`Z-WAC=)t6q$KvSE=y(g3qtiN>BfxrgByM%2k3hE8BL>JD7^<qLE8W@I?pzA{tA=;|})o'
        b'@Kj_`CgS!YL75(p(_IGkfal)iufh=Fxy}axxbHO;B)8=w3A><j{jNpazAkxA5c<dhqmj=k&!M`o+r~(IbGgjBvK26ZaLRYPImL+i'
        b'1zTKzJaHb6BB4G&;LJ*5c@a|dRVvG;;J@Vpi-38>wTf729fOA`07+RX5w@}MSbOSK;jLS9a_f(9n9QDPVx7w>5fJm+NHX~D`H@>C'
        b'y2Fd2ZK|O<Er~t^&z=+9(Aq>mdRWU1w(P;H@(h-gEaYMd!}AoZ8yc8rhls##3mA7tPD2t_XYS`y1F*4Cz)MATMUs{~e7Jh4OVbJv'
        b'2qi;BahM<wv&t!R<M4W#T#N-g!z<#jd@{N4wLj+5QU?^Sxy#OCtYDQZkd1y2WWkH^JVj>>WU`g2I&B~-c1oy-FuRgTsXS#C+J(b5'
        b'=ewe?K$F?1ko0i+jm~M;f3+C{+kEOOXma4EO~&7AGUh*<lo!rL;szB*@nMr%uE~HcNK4}XZS#}=ZZkH}Pc96}Pa6%s*J$kj?kA`?'
        b'@xR(6K5W5744FuH_B&KHb8^hzxwPkqwx6VpaA|)aT=&wdXO+p9>5?Sws<aQDuN0ce5a=)UUR<%VGkl_MKeSO6dG3@Oe51wu8sbYt'
        b'oYwuGJ}HpxdYA^&5t+wP1wHK3QsyZHUu<F;5Sz@q+r=cVo^z(~)av#VH|F4Zxy4NWK^~5JckcIlP~|&6n#lz)zWNi~dCwmLzyApf'
        b'9-$nZnX_}oC1nG5pCgo`KS_W8&NEn5&{yflGoA#+9X=ddgB_p2CCc|^pcSI>qZu6czx2m}Lkb`}&y^eUARx)-;g`J{DEgB$6iCkh'
        b'nFfkZymB|K&S>^2aJv-^1?A-*AmrQZiZQ^w_};$NUU7NO4aP%XK)c$M;|+lN*ZJfxAZ9P0^oXp2cpUBK1Aqo~q(;|Xa5;siOOlNK'
        b'Kz-Z-J(H|D_~ty)6AV6)JRMgN;MMgLFit15uswW(Gunl(@Z|1cxE2c(`@wU+U_!aDz4WqAqtmxSTTlK(%tHOhZBV^F`o>)wEIf+S'
        b'(YtoXmK?{q_p5>TFA%vIVZ3~^N7RC<pvwzM*&8=5XAqCK;JZ~MH1^`*5oNF6I6p!Z-$@F1-GNS#K<=~|&YL;R)}A_}n_;=}V!S+@'
        b'Zb8F<h@Y6-5*}|&2c3+@6XL=Zcp5C7Xp9R_PV~jOz9Vv6J{0i)9<k`Q4uNh<kKZ7E(c<%n=M-=b1c)7?`<{)G3<qKxd;vo+w!eSF'
        b'@8N-mvSl-OeOQ;R;?14k8W7@}7Pve^Fq0EoRI!SB(ACZBOPjc@Vt6PXjx5eZXfK2A=@{aqyFF$PZ8tMR$*QxRqWJKRcvX6*Dn8Ad'
        b'=K_m?61e8h-Wly4-Q2w$=<@Y@I65(N=NU{zU*Oq*sK00qT!}kJT2_Sn#je<64|zP(D^!~&?@!%2kNUWo3m35t9}9YNNt7yRGW<~G'
        b'iZtt_Ontf;FY<++3EC=T#CYA7JEP7-SE#>nr`o>N-C(H`&CVK^S@oy`T6)eavrQ#llIPtTo`!?ui-z$$scKiioveKJR^piMTbA=}'
        b'hGVCAkMwE{JZ0oGPG(2ML+8{f0jFZhR3)E>K{x2qh=OCy`N~-!Fg=S15mRdtX5-I|tvnP3=mL*^X4%nm9lYjN=-j*A|0C>oH^05_'
        b'$Kji7*<XI_<`2(u`euJ_2E*u6smmsR^m#C<7h=C-Za-^k#%(^;YCP?rc;R00HBw47G<)e5vq}o>GevhX4$_#t&1TYU-6ex@SvgtT'
        b'`|H;Kh)>GhJFK3H3y*p%B`$pFYOwxVT=S_vf`LZO;iBwID6zJ6$ra-F&2w&b(G8crBYxEiW|esMZrb5XpAnC=>aKF<2HTps0O`Th'
        b'Z=1c@t!5RBsY-^NS!4_*wlssS{=eD>xbVr>49a^<l~!VP%goUs@*I@<O|v&+uB;j5t=7i5q-3<L&PNnAdmn85&-kpM&9%+m<kov3'
        b'XzzzzE!%#B-YTcLgr(dW&eP4HAYI{AwT^~^pF1%vHHc<qGngDQ#%!&O*Eb+#C+`qUGG_f~A&%<cS%Weh%)Wg0ZIA{^>UZD9Q*_q?'
        b'K6~ma&E6UxpkJs=9}O2-d*h96UO&J6CYVw<$DnrQmK!M^1nh~P=!R}|_&OY`a&jSc7|t!RrWr3$rQD?#IITCbc!KhkTa>OD&!ge>'
        b'$zGIWKOjB<DlF&o`gvgOe8i4!?c+5sMJ6`P++E9{Ir-B(fN~Qbu%lhz^OMLa30QyyTo$t@+(b$NxcaHvV0-9CC${|9jo#sH9!3?4'
        b'syc?a(FCRuFI-fSLcQD!nm<1Y^0vRrf{_{B-OX2a{g5PS>q_yksf-jy;XyUk2J-<KHR3~VV$@^JfTZa~x7+`8i=sHOH?&#dQ*gau'
        b'_;}rOW`4fOCbcg9OIiMu+<pV^!z0WqUG4jC3BL>6TiGY>(c-+H(B*`(t9PFx+Narjbma$jj+WdVgZ8(7ItFE$|2+on#XlJX%ICgo'
        b'OHBOPjW6a-FoWrG5pT(rE2PW;J)TwxZ*Xh%jV7Opi#_&Yv*!)S;xOUZQ#S{W$p+j~zzx8JqPb+xF>L6yKRW*Br*_Q$+Fw0gvL3h8'
        b'(+NNMitgG4QGayby%ywrW+qq3{X$$|S%}af17)(UbWWOl55|Z@c-}#=*r$S5)oUcjOBf7E%-d1hbZ~J56SoZ7@P};O(jjEx)Zp2>'
        b')olb1!n;A(y_?<II2dX>a=jKsvLE!-ZBmh%P3~;QF*g>aZa?RRtNlloDsgv+;vz6S63o$@&xCHYwm06;e(e%%AbFzEqojy8>Q^^6'
        b'rG?J<`$P;CO_4>~SoQOQTn!$%MiABZ*sT{Oiv0}^M^)W>%+TAONrmI<hH*#L<<80zJn{szIwG?Wy`SH!b;B^;HUq^r!NX?5<#QW5'
        b'l<UECS}w7%L!rzN7g~CS;4~=(vjYl6W<~BKgAn0GHZlup8?5-OTR?r%#6|q5%OLZR$UH*j-US_e6o7n}3gUjTV^^I1;%${Cm3fq?'
        b'XsRR=4jryr7o4@?lgccFBonBA!P5C}Dmc^1x+j1%l7(pB;Z=Irogt`Yn59008RQZk^(lO)^zw1@PCF_bU~v@gBHaSgz-xc&hqwq-'
        b'rv$sm@DY|SP%Rp8$y%8{aks#2phjRpm!YopQbFXmUlk0)xTTb^*(Vl}B0-&Y(IjfQAGxGSy-$!ji3*bt&at^dfsGpRh|Gi<x$!2g'
        b'A>(<eE;-fL#QARHfMq;vOUNtG$t~rF$xN&|rCjYcaGzZUkfB^1FrFmDP0$iEBw*u&4u8agy{^6Q2l?c*ypdN(V5={rE<|;;&`O~n'
        b'Lp+o1-8W#p;I%MT4c<3|E(BHM!4m}7;N<Ja3(M8Rocs63F+lfLPg$zj)faTX57<^vk<HyaKWD(E+@+#EZ)8N_cu{P8FyK3YXcb^Q'
        b'tms1G-6k`-r|zUz-HeL>143PHx~Cg(y3rioY^@ML8{*EZ)b&QQDvY}@^?4EMLem|4hl1fo{GICIyqXS?Um1f)Mlvf+@GM3Eb94r2'
        b'-?>@%?)c`$e+1SYg~V&p3$_?CGpq7FRc|d9&TTlvU}Gpxn2!eJ)35q@?f2b~N8HAtuXk(M;&Dbc-XUvsdb}pS7z>pk<PZ;rip|B$'
        b'Cwb-Mc|K1N%EJ&Of%NdS9z@E^gF^c!F|bYvw3|U<-iC1vppV3dyhv|X6WCC+1`!}_fU)EAMBpRzZYF98k&Pdb9qk3Jg$5&C-q1WO'
        b'l4joHm8<^cBQQT9IE7}8&wkD?`{53Kq?R`Y?u^xyP33v;`oSD6+i+=tx~9<^)|?U@(jTz1H}hR_;XhI;m^*g1%*+?)X9Nu2O|Eps'
        b'xl!{<H{%Hda}$>?qaJrbCrb`zAUX#0vJ~kXx`vBA`)gpFRUq@M6qvn;r?#P6r2NG#Grw&#Cx!1Sf8C{aGy+PJ5)H2tbwHLUSGq0Z'
        b'bNBmR9@s0b=wcWR`q!){L!m#1C^K$RSxr8XyKXn^5yx9me{2L&MnDH2O50Ed&2Xvshe#sb#cA#8t61WZ#=yOcnM~^l+)jn&LT*{D'
        b'hFL?1`|oAd+{qe^Xg48dV^rYwM6GfWPc&-zNE>$61LL22V_ZWX-syfA+EYWi%;d6cSCEEq<zQOlGR_uMUDiadyhtQArg%gF4W`ts'
        b'q1v<17jP;jfeN#cO{;_N`4udiW~mU@oWcv7tDMHDz{Wp^<G3rir^>8C<VDDwzrqlJ=0SniviI-YBT{@9z>av)=m*{#EkmAgXnQPZ'
        b'gxPPm(4xAcIm4#_-!t3N8`1<sC*|K*^-PPIkEWaq8*h-QCmY9UnPZvBzK74}g@R2zlruw;^`qSwKL_lE?MtRSDK*J~C`sH};d}v#'
        b'Ccc?fPqb(W#QAAsE<Z<>8=6DpMr*!kF=Oa>k*s8``D7ShfWSLE8(^QI|K(Lk!RZ#W0BKWE!Hv!j03)mJ5aUar>;;k45BcVH`INq7'
        b'j^P6}0hSxoV5%_%z5<Ba!=~huw@6TnQS)|-`g#MtBqdtift{L%!+2W4?^$?XACU9BNH=f7GHsU4#}@-(rkiIjn6LbfZ5yHf(m?Mj'
        b'SH*+RQ*7P2i6^cqw@>$uG<yHms65U({Vjpp(p<#Z(*k~>{qQR--p&?tFyicNfe?+DOg0lApieN5zZ&+^<OW0lu^;6>0^Q<Drtrm_'
        b'dZo!zCA`Sa!J_=bGznk{O(qrUmKL&Lejy*#*c!)QkQKfgHojg)I9f{9@dZ4)8E||k=<I}GN}e&VprOI6Tz#>kysYG^JP&U#o9_K{'
        b'qxYr8vR;-LZuBpF%!ekHB~AKXV<(8O{SxG4-r0qv9VN<!n||eLVzxnXOsfA(<m01d=+`74RX^7<&UyPqq2-Yjkpv_bz80Cd{k?E8'
        b'kfrztwY>$pNA|V409gb5f=GdcGko6vO+_uAvMy0axEpn;=rpJh2(YU&WZWeK7yze#519K_1~dY&m!FHY&wQ`X`=Nc!RrxvIMA3Bb'
        b'Q;psojS~l0;#V!++!jBHz%cG>8=%_*4BjR;1d|vb61-%%_f`GGhMLN2>F3jsNY1G#Q8kTbQ5X;)sH_&i)zwuJnJtj1nDe7UJ<u57'
        b'z!rUlQ%^QTW!zbF&gCtBG0KSc94@}{{(j&4oF{1L9J-4>DW+9`2RDrlv|pXnO>=aoH?z?j+tTi4+b=*Kx$H1YZD@dc_YjNghNy%F'
        b'?|opsO7W$4^wM}db$CnSOd4OlGE^gNNn4w<4i}|1qPko}y|AS(1u)q`s)EH0_|A%F%H_e8U}hF&BF}oaZ?Dpzjb_jN43_U`k+v*C'
        b'hgTrfiiX&SWQ=Or4z_vcVv+ZDb7jRcW-EdR;fsyKx4MH$I~%r1yjY7d59tmv8x}H#u!-F_y;y@WVM%uo;Qq|SLc{fDu=-$lS{=d='
        b'VcUXshU4@zjxCB{`mHo{`)0+Ce>azwV#aL5@J;g$tg&0zAJlGV0S@88%709P83w2WC)WbjKsUGR<sh`sB{v(SbZo^#j6r5LgcuE>'
        b'6OT?CW%C&i4=SP*%m;XE_^df@m)eZwn@lm~yHx(cWS>XE=#Yty*_=W8jMgB{`NC|FX$>Lp4C4*<azYg6{}Av3Is`QQUx?-8=SqQO'
        b'uN5Nl<zgcrDFirLF59XB%PAC-mT35xRCBC(>z-&4B1HkZZYY6|oHv-&DWJAxvW$X^<$QrOlpnCb#KGFb_$v|R-@cb;%qXL;w%<SP'
        b'J=xG7gol>xW>d5m)qckNaswGH^&f!hN6O>VxM=uecIy+NI;3P>KMzn@K<bnu-|Np^*PUk5o+*#+>*kdmVxb>u==->(dE75^zQ`Q4'
        b'LzQ50aA5Q(Yr~KzKkhM2&yZ}yt$v9K6)%9M=<seSi5ZFl80m1CLdCqh`nKdyI9$l8P&5z`07ay;N4rAvxP4?0;YL<e)-c=6Yk%l2'
        b';Q>?!$oNJN53CG%B|I=v{)yctQ9s>G>}Ur29#l3i%mc%QYx$65-+PDjyR=ygC~u5rKSOP5*2btiL>&Ewmb;_nkSDW%-3bye<<alu'
        b'=Wc`P>gU0!(%LD$2nRGR3u*8BUh``P59VXyBRlvS#IM1&Ne)LO77CEV3uCEAn+x_Z_>w{;sQc7B=)%l{<(J4ProkthZ|aifcPV@Y'
        b'^C2<&nw7sbgTv`UCzz?&2pD6fx3>|z{e}e%gKF-mUFR=^WUeq~b^clb7-_j6h>wXt)2H8+ai#ac(w4uoem+XYHoU)-8`U&aE80T>'
        b'VgO$bf4BoW8$0Ut);08GDbh)8&K^n!i4;-9;Io`SKj8)3SJ|_y-2WXB&v=(KK&8c{(1PG7V3{$=90i2_vA>r`d;>rPP{5tTY|`X2'
        b'ARR&qHGUvA=zuVAlEf1R-X2iCI;p#KN6#me@sW=L7UOb+nM`jx>8)s>VjvilgsDD4?=rci)N*Fj#u(Qy6+h<=<<VyF0)H!h?&JaC'
        b'0=aw+kMQLpK6175ho(-k^A-?mlNsY`=eO|f26$V@R3tm6;M+_SQ?Zb`*yIxF#Wxson_EOpH<^vw0x=i8i2AY<Psw>YIO|$Wgy!R>'
        b'9IP#d__7J0R^1R0!bI&3oOFQQTywTbiy`u9z6NIo-3^5?YRv~tfU+865G_9(uhqVDJJVOw{wrwWj^azYg>y5XAk&1xna}K!D!7>^'
        b'PBa<DnQpXS*sfv0{w<m=c&CZa7yAU9CH@E-g$D+@eFvCTEOAOW&hA(Wu%bVx>=&$7fKs=eoI*VxLpbYo3BXBh^y<u&0y!q;^Etf8'
        b'l11T}qY4g@w@sBt^g&mz?HRB*Xli_&tfY|o(g~+b04veH6Sl*}fU01{*`XL*H-Qxyx(b1nl-U3+`LXOD(_lYqMJ>nJvaf#dzRvUu'
        b'%N}Gk?xwV-fefn|cBZ_2J4%_eJSrl&y#d<7_X51(-@}`UJzz~unIQ~wc;g&$&f(4CJ9u+C;4{6hDWH>8JNJJ(6FBoFPB4oup+v27'
        b'PR`%T0KOMNNACKo0BOA-Enii5H<gpSm^pu8H5#ZbY=e%a$pNaW2_z?|;Hin5c-Co6#|bZEKB?eVo+_aGO1;RKRr!1okc1>$g)q&<'
        b's1Gn;x6TiRN*B_(FM)mC$(YA@q$m+V&)v=6^S|3)_tW<ET>BJgfAvq>CssOP1Q`|fllq+5O#sa#N#dw)6X!+!8Sr%nf596q0(%VP'
        b'_N@J(Lnr?_Fi>^km*{C2dIX8=0^(NWG2zv@b2(=ngva6Y0VZ#mX8a{t2J|D2zvS@^C~9id_cwVw(_PC__z1o~^_Y-&01h|OyR@l?'
        b'G=VIpt^r4v56r9QKvh}#to+<9uni@vO)9?b>YS`x^}qWY4*RQ6nMimWDURzC5Q|~e97`@~Uk<9e4YhR%lL`&okifbOb9LdZf!YA)'
        b'I#(Tbue!LS7$F38fvS|rv+@WwP!CBW!aMdjYbU8k{{yUh6-_k;DgqP1c*MjH4r{s)&Vl_74n#3Pj5doz@*E!ZPe&lmN$Qx0IK~8&'
        b'>we-dh5Bcs`b)>%PUiDx<I>X2Ln_c9^%tjuHg%||zd3psSt|_$`@WM<u3z8`#2<hjKj2DPI~i~>1r`OoGV;u}{|I?CPTdj-z;mx7'
        b'9Wqmw=?aWgG@$TI`$l+y%y;3D{UmRi%w7ZftbVHzbQ|JcG=LIsh<hC*IRL2r(C@{>6;2M<G&t4&aQd)BGe7L0YsLF!j%n!-QGbTe'
        b'gN^|3{VE*7|4#=LMX^LJKMeFD+ZFi;mw8zz9|c_){)+AAO~_~UT{kQfEHa)V%TNP$#WFMJlW3Y~aZrto@%-Qf2&rj0F75uPOVGJL'
        b'MmQQ(C{^DG1i~4YD9*ir2}cjQ#V{z&O3tA_oi+^5LY;JD)UJMUlIU6U&xRHk1=A-o!iE+XA6zjX`W>oOg#$X?$se9#nfGRJ6neA0'
        b'<C~Crwo#Eh9lSC#6Sj<_*=gBY&wZ)O1;ma<fIWuojXA={v2N^U2K8G9M{xm@^-G^e3g(G=$`SAecIaHZ1V>X!(D;nF#wEUTgrA27'
        b'l+%kOaZQ542sCx!*N;m&GA!S)oevKG$PybJI6q)&iiaT4@EpbRLjX^sxX@~6xEOJ(5xft^2YZ8iQy}X6M(7^75Y??ft{ERLC(+?n'
        b'<XXxSbuLVo56ufal!u_g<p@#l1V}rqM#@uAVIxwmMJ<hp+U5iqpivL>m8^3kI31TJD>tIU3{qbCK4Em4QIXJ!;4T=qtN|%!Mv2Fr'
        b's*qSvWeZ}d<zmdCmi<Uv+M`@RI!gn1Tw3l!b$byQmX0P0oGao<H0+M|Cu=8a9!es8Q3*668WGM%a2Nz`m_}m#sO2-3SOv&is1693'
        b'Q8_T(4yucYQo)*EK-4lvR2mnF8MVC6a*Hgg0_J)F<U)mJXqNShNm2sMOf63!mfv!bIALKS3<LMuC<vhtMrqSU!GYA7z+-q6?3?cQ'
        b'NK^-mlX8?LVw@zJBV325uhvJM<eF=U8iQ@V$`VVQWJnAQG_x8R)+0zF4QFB}a%~9JJ&pK=zL*$b0m?&u2eb^QPS*(9cxpuv?12S5'
        b'CavJY{5_AX$bkXe{>)Nhr`qozRjFWG0gcfxr|u*R_A96jx1u5d=Zal09Lqi+BG;>5c9=;s$hu($75;@KNoZ^#pZXTyG$J`?Il``h'
        b'eH-2b8dI&{=505iJQ=V9H7xN~y^qW$njHWa<VU}TCZn&0fd#N)3<79{0Re|=5H1?ua3xE;Qr~fwuydIwFF^;XZ#9560z?kLPMiav'
        b'JOs8pVH-<);-KM;6Y-G)@JVyCO?tW#XdyuGzdJ}&beU0~a|k!F2r&v?#kw0T@t(tsiaFbA;)FvLV!6f=?}Goa<cCCay>Kl|A9Sd+'
        b'dhJc<os;;B17ZgZrJz(ysv-i)>)_>Q;01=Cdka)25dt)N9W)>jehD&`Et#YxCKG1)2$X--LHkV<W;qMG1|H$ALUcO7lv*#K!ZB8O'
        b'0lc?6_-OL*W>9ou@g!e@3CmdTZyRt|LYHr33?P^HclB{;<QxfK<7lM;1^;#Ze^T&2*TWNRRQV!n`8{_wT@L`yrwesjme>o%ET8y8'
        b'eMgb15}JRs!pNE+i`Ah{cKFCtkP%F-st^X3(y>HUy{Zy!q{M~>8jYlfUxIm8)vJ|rSg?5pwXA?xfG6mE{~S(diHGae_sxCWIfLpR'
        b'gdgQoqj-enS(YLkqzFG>NT}=857#qf1+kWady);+EoJd3vnXF(=`fk4FfAMv{)x3HVS8a<T=Ru5uta`6Z45+6<ziMScd=kZ9-Dq%'
        b'g3ED1Hj}HB@G|u^YXs0$y~x`5AQ4j^&o2x@9-E45%3Lu;4zX7XWs3DCgR%k0w597!eS+>F>KGiZ^BElrCwkaUe!$LXjX<HR0aLAK'
        b'ZW2)qMd)w{fI|u%h(!&1F%^n0#_?^qqa#_drNL7!l{ep{(G9Nq`hy<vxq0u&sF&+Gvy79n(N;bx2K&Qaq3#D(<=ci0-(-s(l$YJ$'
        b'nr?&H^yhAOEClEcxa&Z_(s}J$SuN<<)Wedv#`UCxx8kaN3Im-C3SNIjDWk43CFD5tQP_uWkAnwJ`LPX@4c1i`qVKwOD1-QpQK5&7'
        b'eJJ=w)dc#dBJ2DeJTCT(kcS|nd!Q_#O0ispUNEUgV5X=G2U9LRHiZk~!UV*JOd*NvIM3t+ZNrkV%V&L_MCyZmoF$<=;buSo5g*Q{'
        b'dSS6*G{q=MZHy&1!~KV^6+=Js73hX$9Oj}n!94Pe+uKl;4?35Mf7ue?{U{{80PJ_<+ial$1H0|DN)hRadrOH5tC8}RsE|RftxYPA'
        b'Mu(q3-dctZ??lQ&QQ`ey9WoUtbglYw)R?BP;1t%)9~T0sAjK`;gzDOmYv9+8lt2C9M9URlfzacriqgtQ78Bi!;t6S-9JMS#YJ2h4'
        b'2@@-~FX!`6#51Wpcm?#UYgvUP_E{KL6AyYkhz8SaK6xFNm^y1brmE4L?Y0JaUvla+s)I)YBA+L;y_%J`J^-rdgOz;W%xoX8`kZ%4'
        b'0Ggb53Djuxu$uvCJIm^_5oFOc7BwVX1=@~^P(H_wmLyhMG*I1?hvLByhJovkOXT+3;9Vs_N+%WN17reLZY;nTrB)>bZI0{bMP;-<'
        b'!?vAM3Hnwg#Dc*te=-L$NteFwm%syU(QJ}L-#SAoL8<h9VYgu7@$3B(?^8_KIktCyz4u9G;!{?bjv(#h*Y&$+^V=0=)3Ki23b^GV'
        b'5Q6dVhcB}*$U)qqZCv@UVgbp`?3wj$WRxGXz4m%<3Df=&YY9aVbumMFqLQ<usf`+9>%J6HczhG=TG^BAp>qJ#go&-}p*+}`O2h*d'
        b'2ht+i)&iIj#Ux-cu4yIQ(P<y5`-DXjjhyCyCo21it6*gDJmqFqKKTu(C1TO^5>N-=r2%|U0i=wTms}>y^@<qjAr!QiQT7BY&-fbT'
        b'@e@cOkMc=Y9x(}e0l2+B9+cy#w;|?wdP+UVq&+t>dwNR!?<-);h~8PtVK!=L(KI^z4;D7p{u@yLzX^OFfRrS2+fqQ40CsuAgtxq&'
        b'ih{U2e2FFI@0)YZA-!nX%OdKp_i28&j|^RqNh-*-3v}>KCT<$FY-2e*2~n1?@~(3L#!3_eGh3QJEe{gov77gx!auM87bBEKpuhhB'
        b'85mT6Y@e(wK=4JE(>H(kD=_y@M1dR`N<G__05U|jAg0MHJ7wE<n9Lgx$M$J6DwL}}vQDF5$Exl1dBV%qg6@9^vPOwORok~u?*#nG'
        b'YBmsw8NgHevO-w^#%va%K5UCu`m6$S!<8N$s79v=03AN@C_wJNgG`_WkS|e!=Yq;itqnWlQDGWu`4x-gpiwKMhBBjTboFeMR=98O'
        b'Y{iW7<d+11#q$2m3AMLniZVY764e8H0c{`6F{3Ehx4kFeM?iJK7kwXS1$|33-yg#F4m*)x7-B;C8u)~kr%6GEwhCC?AS}_|&E4CW'
        b'0Z#$l;E^Ff939ck-1X(BdBvHZUzLNEV~=Uxa#moY%|6co>cC#koc1Jkyw32Ky~fxF>hyT<>aFl9-{b1QfNWDbtf1(<oJ}o0+RrcT'
        b'GEsZ>2AFCU#@EIaY8zD;&d0;%LVI4>Bg><me{urxqBh5FYt5=q!3#+4tiY*4%h4F3*?AIeYomO7&8i3Lia>k2Vf83=a3801#98`W'
        b'f$WO2j;lrmsv%FRIQs+6Hrwe!W5v=d(4VYxkCVFsQmK|)AxxkF-7Tm~(YxJ=*U>;&W5Dbk;^AV4qRN`M$oYgblI|2=amj4KcAN8='
        b'K-tdlz@6?Ur%KSQ<*PS3Rs5Swg+Q~-c_mi1749ktF&(77OQaIu!eBC9u$jamfGYSU%NWDk!cP-$f$J3y2mtVgN1Q5QH+s3%P{2LN'
        b'BW}1PG(V@y>Xy>NgRYERVG>3?xsMC$l_crLhOe<)h77A)1~Y`^3NvFA)TVnmU<|z66w54|>*MUa5mM4v7gF~8R~3Sv!iWp0^{~(u'
        b'QuiUJLv=qGl1MUePO*3|o^B>r<66Lbnc{2i-g7K>GGH&vg>E?z>fyc4rB0t}O{duTfRm|MQ}(Yr_ko2T=#~;HAn_6XR@96kZ6_7<'
        b'z&44gtftgd6`7^Kbjv(+_RhOrbPEcpfXA7$<vqnud=-zx=lKBPNWd7BchN0c>Mxt+WZ9{a^JW|wtsmXeJ<s$?jc%4bl*WvleR!VZ'
        b'=QYWWs!_M8YrwO=rduq(elwDc93B1!##*;rVY@|~(j~z0D@Ivzx#F~5R{8=o(c8guZiS99G96WRtLByi$ivzgWJq*!yg^1|kav$q'
        b'=sm5pUxXe$4t;c*Mf?+e=x{XBb9{ha*V9wwmc7RdSW?3{Tk@?zfr`0WbN1M+eF-V5<Xj+Erv5zGtWx8lhx>RBqe*;vx4LbwLV+dI'
        b'QU#}#T)KWBes^o*>Gd*Ff@#I**0S+(S)O+5P9R!_Wg?_k8<&_#O0^MESZX;}Dq2C7NY_Z91Hha{{X5fuMS^qnz60=aE)l@K<UYme'
        b'T3HWgj(C*r9d<xmuFV7eIoZuWB^duwMvJXX6m6TN&x+7bejWn)cQ_3{eQZFL3p&T$7rWeg+pU1DHHBOmk|mESzQInfmKDne)(rq~'
        b'_o5@~iPs!3rdgqJKJp?zMVW{QGn12@$;lWl+zeQchmnGp9ozVoN@ToP))90t913C`R{wmYr0c8%{p1)roP+oz{KH34iw>#S0NU>s'
        b'+thB&kO9455I{(T$TkVBc4<x$mkQ)t7j*2tIEe~>jtpcCoX(PsWQ}LZ&dx{je11>Q(WCf6WJxBn-a8h2dcC4J7&P-ZKN2)_;_!>V'
        b'%UhL40^skKo0b8xXL8I=Ydvq|{mO?S2OrE=S;y0586+r2qUcGP0*ppBfZ?lx>x82dD&wfEmkQ#ADHt+Ckn@ooUIt74>g0HgOtZ~_'
        b'%M)UPS8BCyq&$j1Z>Ev!E#s^Yeb4V<ecF?UBT~j5XnXidy9{qDIoi$Na2)l$d#$I-<oVp>IHKqlof5!q!<NdvWM@EMT^d>)xjvG#'
        b'0NE6m?`qLs{95-_0GAc{Rhj|^@hf=bL!<f2O{DjbVwow0kEm2~KjsqYw_uD)<P!@IE_;{}2c@Q`dR`jfEC`|2DW|6ck3CAL+&Z%='
        b'q^$yvL_#x>W8RdQvgBjZ(I+zpX1O>xORmr^y=xXn1Nc?2+@VQvK=b^MP#Q~cYrR!@Zmk&ViMhg$cUFkX<q!4IzF^_O<@fu8gR+0F'
        b'@*EgQeq90E6eCm;*I0O=@{{b3aD;!ZUkKYl@3hl#<BnZFwb*gRCv%Ag%rXy$!Cka>A&0?s&{Q&Q@`+9YVv{eJrPB|EpA?^9mW<hk'
        b'=AkDt7M`8QKlt#10YDBsRiO4cFCGAs({EKz4d0xrpXX5YRCS0b#KCysao|z9l{Sk24a)pb;o9By)g?*!eGxPE3k%STX(3Y!_|{+I'
        b';~fKmZov9FTJ>9R&8@j_>!F|OmhhjAFOzkM;#xyG=(=-$2~t;^(dCoyy4(&&73iJnc9QrmP5rX|lz<jx_Ed2JH#j{)t@r6{2KxSq'
        b'TaIhJmGC)<ySo5`3|=hHf*j9eGnaRKP_KElmW=zjFlLitnRG+wIl#2#uT3Tk5K@C0JxEYlDb-o)JyqW?Bvl*R*T&+JrzG7_14O<R'
        b'qg&<Sn9EKa*{g6%Z*K8NNRz||pOp0_48?tR;^*R_xbt|(;p4m{F(5VgViK_0@=PS&3%yt4inba?!|R7GmLtpa3pAyrReHg7!e5{A'
        b'#3mIg54q~|J~IsXNkdnCfu)v=?b0es0fgD1WjLC-GC7_XFAI9&QOaEFJx~u=hf3APiQHJvh{Epyw0b-UIUeC^J@o0W1b?jWaB8eS'
        b'_NARaSM0Lmk=vgRdrpRgWFo)!Chr7rY(HM}e6U}G07%40B$=tvz}PP_vqXJ;N?9pMB0g`WJmoTUd+-|E3k{ZfGWJCP2~k?BB@Nl3'
        b')pPKW243cNOuk4+JznemBZR3C3|Qtpm;{JC4;yPeehUwW?e}@X;=mJosvE$#JtxD10wWjegCiIF5*W9=LC=e}Z^tS%2ml=4z8gHj'
        b'0h@OZ%y(vpU)K7(Pp23S#HM-`sy9OWQNyq63(~=meF>l>mBzRR)M8?_9z<J!Xf>!JIvG3%8P`+GYP}ok0p^3TQ$7^y_wWFyU~0kG'
        b'*<G#2bNlRr+PwqsOD`YVm2fupvrkf^&&HnL`S22a3EW7Yhr_r1d`*uZ^J{o#;Q&5A4-R3Lg3y3{L+`&%{1ObIQHA=vRr<4ETYfXA'
        b'$C9`j4~CWwzo><(-D&lStNVFWejU8{n_ugEu>NuhvAmwC*hp5C5X<VxipRL$A|eI+Zs2~42{rirH9$yQ<RAy|#R^+Z(p?{>iM4nH'
        b'RR`;<+wF{~r^TZconpAo_KICDy^Za34RboMG|G4@akM3EKIwhh>c<)HGXVLmM<O{Lt$Fo0%BY@>TYQC4b#dnZ+$97RRL`gm$vbZ`'
        b'sxRkawVOfdkcZ;Zg3aDaYe>YLzK^%c8j@i4J_BQ#e{3hoO*#=md;lIwscZYpsuxY96yCrPe+NkhsF*$q9*op?;M>PS&c*^pZcc(n'
        b'kLmbVxTu9$LcC))ujHA@HGrowuLSIOtBHc~0qJC0=w6i5D?rJWJmRPw=CQ-zbb*AoxCG0cLRM_}`#W;N(D(R}ZWIr(9^v6ohuWI1'
        b'U_1!3lIQHOGoSJp@oU%U5R<725oJ0|&OpPQpOukIxaeBOMIe^niIJl@wXYvA>71SyhNvyIDg6EN*8#tt&P$i26ksVDiTdz9ux5<W'
        b'U4>+6X_mBfy;N%iuU~4(O@+qNLeh9Aag#Rs=|ZD%^k3TOL;7{|h{O9Ja?1hz`T*5pX89AhwePS1%M50__rN~rm0KKJ7`qW5Ff<S1'
        b'!kHeQtY|&{vdi9);P@S8)bNbazRelSjL|P0d?*Q*`^Zv=#TGBLVwRX*Zg4b&`80@IR?);=!^4oH!CB?li$E#`WU!xS)FAEuX7!V|'
        b'I+Xpqvdio?i9P{5<6{TY-dBFC1VV4yIde!6zSv}!_6to%8q6WZfUKChq@FD`TV!yvrIk_t-t2l2mv50lVGq%Mz}I5sa%?I%3v|U>'
        b'wXYvDJZdkyrNkpaUpO)gXhw#>)rv=gL4xqU@0GuYZN_tHd%?!Kd|G<*l94n%F4~NTRwSH_{_K;7f_pY9{L$w(A45$=3O~6iKOgHk'
        b'E-loEa2#LQ^H@!xMqJwqmMQF8ovxEbs&5P&OD+YJ2nWlw{nHtEg97jQ4{*4BWtl8<rJ@_{&E1zIIK4+EpAcrc22Q(Wd2Xmxw0}r^'
        b'bSRHk=>D~$&D7E^7*GxX917$J9?f%)41rujd1&kYqQ!b8;@iUekJ8mw3yU{qa(i+f=U1-Q?>Tyu)`lZ_T5S<RLhTQbCyz(wq0ml)'
        b'Lh$>x@UCo<jaw8p!{^wfZ=-g{gZrS;-NjH;*NRL`vrJIY=YrNQUv|+cemB<7Z~uYS1{LRlgksuo`dQg&m&{Z=P`VScoTqonyrKK-'
        b'>$mO%T<7>sS;^7ec|-dj_cuP?bA0U)nfx<FUyS_sF}R@8!$xNLu@gHZ;hlsj7czZz$Sh{&nJPVq-@}E<JaIS*)$Ktv^Y+Dtq8fak'
        b'$qoBz=lXgycj@W3WTnRjP9KwPJvRQnY~<Yg?)OJWMp|2QlinlTY8*SF0dk5wSK>p_gKwb2u?U0mvyY&b7^F{=IZ!peU)FnZZ|nY&'
        b'BSVjz?BgA}F&6I`9T*s>${&ZCzHLjcw94>5ce(N4i+@G^BiD|)TR(U4Yz90S$`xXSHbgxaxjs8R%cU9blsP}z+vWCo#zFoFh*(Fx'
        b'9pauYMW?v;pL^vo2>A68sM#Q-TJ6y7{Q*VUTUYue9R$^E=hWC4R3I-7_Mt)ms&FX)H3)z@tU}=Ma^3DdzBkbG{kx9<=>H4m?c-J3'
        b'|G!|4ya#i3`s%xtdJoQ3+WJ31@7-G$*4qOh=R?S!oP&I#3qr1@HU}V&-06}<W@V?NmY3Mmv9eNf;4~>yJNIriLS3s(WNaE)zVx&T'
        b'UIl{>cJA)7hE%1I6-#qucqrKIqZ^i70pf)6Zvfd!@;_2QY%94`(2bp%5Abai;M+!sZyVuVN96k9?QG;u-A=gPJ^wuWT2$Vu(_`kS'
        b'7rL^lZ}$tHt(}*5>OvN>d-TF;BzS#r79OPg-P}3K6|F3}N^v?{wtWv=A%=>*yWt`!^z^-m+G9(|LIx=pgq+dXaDgvrV__lS@4%Xm'
        b'Yn5;3gp%D5Kl5}X)(4~q5=K)=+So02^FEcGLID@e9gmO6<dR$F2<gR3=Y5{O5=$5D3r8Zmd_{<5it|JEMS`tZR(Stodr=&XYeFsA'
        b'h@p5djOv*Ueb5bOA%()CE4yULI~AwnWZStBbN*uQZgTvr?A)iWCGz(c`tIMz%sVR2SSS}S1Y!}sppzF*1iQ)mHv&%fl(<`D+u>G!'
        b'TJV+Tx&cCkA~S|03B99xflEDBa7lCA=ns)z{91jI=pe_B%Le229z8y^H2DOO@RlO}rRsynplluB(EE6vR|X&(^Vf!+R}^@pJRUjR'
        b'+JK7{M`~L3!%NVXR@9P$FrdOMs4f{{?tg4d1|vati_C@~=n%|-DUQenPuf71fUyfxD5ZDEw~FB`1V*)LP`DS6irv-K)7lM>m4|QC'
        b'zl5a-i#9Z1!RrfkMR0E{6c!7QvZI>{g(bp17QSy3z6JjKQS5ZL0yM=K_<<g`|4BJxxTF~?aH;7Xy1#=wDZ=6n4M$*A#k$Mv=$9$N'
        b'k_`==@V$gnoJtXH+|b~L?;CahVymafEHLfEUqF6g8(Jur691^n--zu3JGx?hGGsH?dsP+%fhpE2<kkhWRV9oIM|By9YFMrX*xD@&'
        b'gxj*uqpiCv>9N~)V6bz${6XmHXJkepmT%>bA&!;MhLd%ilH`zQeB>m)xO#RBhiYU;ygf&gPal)|iXQV7ZKOp<@K}`~HtkU`5b`h{'
        b')k<r_5c3$ygo`r4a2AQQZ%>$CyJf{fv~N%0C$sw`-F&4HZlCg_Hv^586u~n9y<eFI_oT|Q?K8s5fPHPw4xOj<v}A`ya$6PP#?&=5'
        b'u1o<80Y8GXw2uILm--KMAO*IzGD0`a?rIr^b}YirxU;%vX&fh)Zafk4OY_pl@FhvODXD>3TBI;lCE<>w2H(;R3I}-fBsC~JRpioQ'
        b'#i@n?MHN)2=ukkd#a0D$N*u3Pa^*#|8x2^u!L@3Z70Z%~6sKR1<#YR43GJ-r#;bVO!qE+LHW-ZOsH4eL=|<!yZkr8!H!*RIeIBFL'
        b'E+S~_XE$Tk2;4ju&+JC5hfg_I)7yKh%<&t$1t6!gT1l&6z!Xlt-7C>cM1ZD18&FW0jYnnDl_yxUY9lC;->!fKp8L-Nqr3IiTQD98'
        b'g1B}&8l~CpZ+q9(o#b^SjO_QvCm+tZkBL_wOb_qj7E-^YTSUuF3E{O-$xS?D`0uP=gav9Yds=BG_?ByIM}j{F6kNi@fP#zuZ^4nP'
        b'@bK_%xryJwa>Li=Wacm$j4z`qf^oZq{d`Um{)s-c28Z9xF&pY=JOu1u{szvS-iDtX{s!tn>2AQL7oWnCd#b9Z>b3xKJSSBLzRy~@'
        b'c7BaRnwR;GB5pDE-)-ffDHu<S2{M<NMpxp3B*Bs^IVtM-b-8@ygRFeyb_e>!lDe}J!H@(-65I)067IfLmJZ_vMcm3s!6msXbF`iO'
        b'+_gEV850}~52i!#NL#d$&-$`NW{g)irXum+_+@}5P4Hk^ZVeYbhJ$aamKMo7L>;J$KDZdQJOCJUDIV!En`*HhI@#gG;2NW$J6>+v'
        b'10;kIqk|K*t^4svXk~QF3pdBkfzw@3@n;<1=^>LZA?;wW?2A6DkB^+azf>L}IQ@#k_uJAre#8d#?dnWs)lzG)%=?<v9L-}A46)&<'
        b'j$;b{RznAgUx;h{CCNvq4yz&=Bg0#(znTj_R@6E%{3ADR)w4Za$)~%dkgu(t>FG;$9FxM}3bad~_Ji(Q7QxRROgYmYqx6`j<@8Nw'
        b'lND6xUtCn@gW=PPi-a)9O~4AQhm?}VMZ=f4^N&~Ic+hvoLl^u1KOUqQy*mVhf3CH|5bOy{yAFZz34!B7CZxp$OV2z5M}tf<9+xP<'
        b'U~Dr62E$}C1xABZEsYD7QBPV^_&idzNxqh+0HaZ{Y2q;GFV|TG=<N4w^$$I-Co7IgfzSiGN?(O;&7lqWp4v2iT>}(-=4=Ml)wSm6'
        b'r{&=+AV=l~jhwz66`C3%je8x{#UbTJxNG5GrZQ)76dq*+tDwivUs=67Y88Hk@?m94%w1uIj{r<NC!ky9w4fsa3LFLIXpyNNGi!M5'
        b'^Og8wKs;erKlM^Sx5`KGq3|L+cwj_2aHIhUApY>;o-QfA)U&_AE%WgZMpY`G40gPzU@A)K22R$2r$)hKEDCSnVD$B<WvL;e6yH~='
        b'Aut5?PXUazdUI?0QROlS-zmvG@Fw9|kPGWbkoGFd!r0?^-o;it+@DZ7#6uu#E^m)bp|3*%23I|_)V!5zJz%Z@eI3F8iAYCuKd)WR'
        b'>Su2RljUgr@FCW(D(&f)_H;J5YJhkKgfzEo_!L_`d-`0m<3%Zq<jt+4x=QN)T9;^4951SSnj&gdqER$mL?zdfB1C_dM|yZ<4nh%D'
        b'BBnM)^)qi`ZHf^g5^BkcpS9Qic-Jp#fDYs>)2~J5=zvy@*XHuur*8-7KxFM49f(w>2I#=V%<YFI$L%><JOYq`!n<Uk?j#-JIjS&k'
        b';<XRm4$y%%5uKtUZOh`H=3H0|f@CbW28NxU_<^;28MwC!stx!8_9-Zx7215FBnk$Y96A$hck*gS$t3ZiOZFIO3Nmy?kyfMnv~8*z'
        b'1rrbFu<KyM{8RjX43>TZrqpGq&H@Y#=+MJdHB4RFwOXM0&VKOCQ0lK1@cy`Dw5xh*K!L<Vn)o=+@NYYy*`;qOD7Q6W%tX21Lm4z>'
        b'-XIHt_Nee(PGUvALS^XXg*fz=Q;ZcJK#KW=XkwI5HN-_O!s4U3z%77EbVDjHKyV?x(4%kQvTtr3w*1J>wJhZ9@YN&sHK>X|>cel~'
        b'5mY1%Zw&b=eqD-s$evF2{?*=%Q4hejacGeq(C6(vY6l~bz@>)cs7D3EyUxuiJZpmee#yeQL;XX12_6!k5h%9?CA#fgOyqPh^GM=U'
        b'T&R$E#jXN-bvMQZzSn24>H~Jw2W@`Pzy(+Z*iyOC#kv0H-2%fq!zS@9Q+MdO+s?(ic8h4h9?%u{{62e;ZhqMXwymV1Ye$29r+j{<'
        b'4o0JuXT}Di5$>SvU?prnte}2`4e7hE9WU7N@c5S8gN50NJFIpx2!ZZn0SCUyLdLFxG2UOWljZB`{zdEoK-X2C67*wSIMq2JWeq&f'
        b'8RoR@SHL5&6A<QY5_tlQHb_Oow{AYw4O{DaIk?LwK@zXGM2P!?x`k8}{7Nmg0O6J_7n7=W+Hy&uF7dgKcZSU8LbUFT5O(t>o|bkF'
        b'_ZsY=nh{vddHasX?RY$Z)WJbYth4Vrd;Y|hv%0fvZxPHk!1b-<_Kvl7JQrFyUuBbmpaJh1iS9l2j;|MtT5Jh;v_|74#7eu_gEDBM'
        b'RlGoTR<C8LG!ArBhamBiIUCVF=-Egfj18`|cjMG$SeizAe`$AhoRV~i-;3-F_K6aGkBEI@jCqppdqhN!*-)?`QAU)wXbUR;^0uqP'
        b'C6+&TJ1O|?`n%71&lh($I&q$@i%7{!oI|m>bUztHl1R_%W*>=uE<7d3JJvokuTD~Z^o}o^|MOk>&;RlLeMJYEe9YWF`O|NMA$Grq'
        b'#Umy@ou`r7lO&xn@`xby0=tTTvyhl?uf740^85?1r~LCL!Tip%bF1aN<c!EZD6)G+pm-Ivz{U+0bq40_;8)+EFisARA+Fo#99Jct'
        b'=b(q;m*=83Gj$8*#piW~b?{Hk>z_y6u-&n_G?NH(5Ham}6ATQ%9vp2Ei67}|KOcjK-}NuljS}D4PW%9WnFJ)+mK-OFP{c>aqG8n6'
        b'w%)I7#Md^HP1^IiR6#4O`-9-zLbcfBJ#YFCB0YW5p#wmaIkEq;<7i`YMq}#FzvMz>%35igWKLfR`dw)si=ol3j!yKRFAy@qtits)'
        b';v@M~uZ1(2jiARyD>^Cz*bQGVjqdW1i>Xe_oCjx6?xe3{85m%y4USCpjO`9j=~|m&j5seoGhiDWu=Nhwyn{BXA5tQE(`d(;zuE?m'
        b'*?RwCvs`C$UK%}crr$Pr*w%a820(N)Ua0FlbJRBYx~=!94KNF)Js0Xa&h*&^U$yo2*#OJa@pPsgCcSAJ?6UQ~X#*l1Gcr>>1EwID'
        b'HqB%viUY1<tw)2;ylNZt+InBL>Hf*m4WoT$4%r4@wDlgc={^Ho*4u~1Y$@~yausGa1_8POX!OJs>mwulL(;M-HieAnc>QL{8Lw^7'
        b'Ve9qUbbn)E1kJ1$IB$!5ea6i|T*Yeba5{njn))#O(pjlbxB+A+PiD;Mx|}aFO<@4k2HW5tZM}@m($BW7(;64&{9yL5*?kdb_SpuX'
        b'v-R$?=?=40QlR3+`q^86;Iw6Fjgi`D>Blj=GgjN+?`*vm+i*9Fn2nKO)Y_iV8l$w)GV@Efv-@OcDBIv>Td&DxX=gRrF95a*eqW-E'
        b'4oQ1D`}L4Bzqbwk#@4&r22J(N#wEh*fCEc6r!zP|-Irnv9`fMOk?+t7YAFN(ALZVXsW=Xxp&Y12LdC$BfXKkbtTzXc*t$%1rpz{2'
        b'W&=pz&9PBg+#IKXpO+(o&lq6CelHIQcysHK9s)GR<Y+u!oZO;m6Q3!z4HnyaOKjeB8}%S8i!6(_FH1Hx;$l3))LA37^SmK1c$P_%'
        b'(-i4L_wMV8Ds%XS@6O=phUJO*2Zn;Xs64pNmL@<eg_wbSatJKfRWJ!~vWoR)Pu4(w)_`^sGUq471sF1wtyorcChj3rn2oreD~XFc'
        b'f?BeW(FeN)!y4rH+b({RprtvjFVq#?y1(Uc()OjG+D(U3W4Ff-xR!y(p2GtjgQw7=N2o)4V6O)gb|%oaLB;w3;kRs(z=gFm|Ew>}'
        b'6$4Al52w!C?jBIY!&0v0!tdGb#|C=HO*F3q2z%BCQ(YyF!xt{!Xn8QnVZLBu24*702EP&82)FuFP`_||0YVclwSHFEF{n@tw03n4'
        b'w(d+=FZ_@t6GU+j$<AQ5K?#_HC%qSG>Ptv-FO|@;;QQ_5ZgRZk!uSR7H=x?>I5D93b`yX@)z$hfcp6)-ir9j^7xq<5KRm;DIbz<K'
        b'X?k#m_IsX%8gz(U@*SKv-)n~g_rQaQ)*#kKV*zw|&YP>*GFawkbDWuZjky$#?OK){5mG^A%jZ>0<=Y!ew>EB0L$!wx<50zxUL%2('
        b'zO0yV#5~g4lKQx3=K#Kj8I)e)cl3TLbMtNmokIPbt8#q;)}f(3g~;G+*yDLQ+0iAXsZP!DU8Rk0`VJzVPH1R(xHUereZVu)SbDVa'
        b'@QNk92WY^d_l|&H#pYIF^<;o!a7UNAWqG-oZw{CVap|#S(=n-j<Btk`bgbYrGZ9{z-)LID$xPrEqLD{tXm3YvvCPKX&3-O8g|>gr'
        b'>g_j3BAoX2OY(;XN;;@baGJLs;Lebst%Io%NXljdQhH5+&*#p-(1~x@yS{kNbkc*JwDgO)c%c(F*^l#(rFOlDXMXLrH9`dVc6cUC'
        b'#oUc4VL;3;vA%aj*2b{jHk$OHlmsq2a@AbeiL+#6X_hSV^T8(i8%gHp3fN-Vk8E?q?K2GRIq>G7f%dIJzTutz5PX6rZ&%solAE5G'
        b'H&c9QDifrV#V>^On&RW7GKV~##?FPpuL8Ox9VlM&I7%i&q{~tUrRlt}%9*fB*eQvBMCu!<m>31U8a>+0_rHs^?}))e=lDi~S7=yN'
        b'NJd=3ie9KR$c=_@^J|AT`~n^R5vd5<@DMtD6)7C5C^X0b$GWO=P~jtF&+&?7w}fzj`-NMmEl%YLwsK_MUdiS~LHHui<_5hkqgYlr'
        b'7*ou{7hDPh1@JW>>w<}QSWw5J7lnl*>pU$D`I{R`i=~Bz(7h7<gQ>>X4sDKDP~@zjO3MaHf1@s4Kal?$!FZW$YgOd>T|xQz*!X(c'
        b'bNrI591K_GhH3|;Tc4=Vl{9XN#)W1>*p_A0GmK%eMoZ(Xi?E!q+SjXRiw#;skl7H~p2{~9k%dGkXkBbHgmezB5fvI1R$pTb(r!>V'
        b'a$-|VAt9|KBf8cX8l-q`;b5X$R?HjQIYj{62JmxeJ<-R0E&&y_*|o17%3gvBUqf(AyHYM(h~QybLm1SW?ilPB40$k6=UGF9GMV2w'
        b'*wITZg3G|8PcH5SrOy%(AD0Db4<e;cyqQ@p)wUzq&GW(V=PWBK%g?%iFU<U?=JaXo>`HmgGI>^9KOZboP+i$B78I6e@KjT#yhcSr'
        b'V_X=jb0EaSdjJ!`5c0ZCZK%YQ(3nYXB8!oa(?}A$W;9k`f^zl?2rd%t0Yn#`p+zd!#~1;pKtzr`Yb2ywyAJlF!c(mAAd=tsW~p21'
        b'Ye#S$z6c(|5XcspaZt5|$IOkxBiB!%cyL)qU?B7*-|g~N3~pY83j5g(e?>38+CP}wuHbk2LFYPprRBV`M`KFYCxd3pM99{z3Ijtd'
        b'+_I@+N9VFFPgh?nUTIz{VOB2MGWa~U7uzOS6J*&BFd5L}pnfp~Gz!jJ=U`;Hj|hhIm>UDuI7mA9Ryx?>nL(AC=O?7k$;NgA*p6O<'
        b'uz_q082LX1AY_OL`Q$8zTF`YZjLsyl=miX1Y1NyK7ODO{j3Gh*g=={Ti!2A2!4Tnny^bf78Dde3MODEE{obN^WXqNUAE7i7F`)9H'
        b'LFu><;VN(5`p=49{W;MZ;q%xU(J+v}eFu<(?hGFhg6xdm-Rf{mGlmf7@2uY6Ssjfqh<Ho0$Z)2nG)p0zU}G^SXgIUAadSFdx>J^y'
        b'4bjK=GO`(r`{(TTQmoP=G8z_wnW{AKDhI<W4G4f{?Af2p0{{nft*jnm2I%1M-&x^C)>&XJtx9eQiik}>g`cvSyBkYe8(R*;$cGw#'
        b'O{PvU`~h1%Z8^&#d*{KM@^TTX`yHE|f(~zE&0{xpPr-9~V(}&ZSZK~FBN6r~|Eo~#CNx%#4zFUrf706fl-2u`b?Cq;<@f?XDBuYf'
        b'q&?8?VM|r<6UKMKp;B)`jJyQ#y>@$eet;_#nJA6*&1L3j<cngf*&v`p&pc+e8O(!Hn~W;4-jdjOr-VRiL*q3QZ?Q{TtH&bOTg7ku'
        b'Wa9#Kb;^TWc#WMh@UHVdpCi@EH`qHqDK-BE!vrx0gC)TD(i{kp@Tfm>eLE3TcNDe=*}qv<e(vUf?UA|OV&^tg8-vuXB41+3^@z%{'
        b'Lv4-UM8=BAO+md%D`X?NLxiq%y`;5U5Rk?@sjgM!5$ntXB=JIA_$PZYd~t7twOiyKG#i2`CCozi_R6hYD!|&1@bw#sYfv76l_#Wv'
        b'jCf)<`c*IWcj!0OHF&A_azwEE{Pm?;;g<j^6;)1l_sXoNP|(_N4QH=$-Ey9dbWfUxCs<N|$c;f}Lb5&P&B6+#oc!(fbB$mtBHs?T'
        b'E{ULSSV}*a4USk87ZfIL(-A5i?DLZ549xF&AirHf@nDT$hs76oW@>2a5_M;Ku364pwSf77vE+qYG{prIZLnY$qTl+RnZHOscBA@Y'
        b'QqYnsPo02Dr$D|3YcsgqKN!Bn&~9M2Nqj^Ybh#A-M0tVySpgnjYQk(3;P2tF?U>g;C_TcvCHYkLjo?&(DXB0U#7ZMeJ1@5e7i~xg'
        b'8-GFOq6!D4_7{po=J#&f%Po^E(x(CSf=XYM;1P1$t#0uhJn$m9U`rbPsCp_sh$O;_(ZIF~fGT{K1&tLNFl7<@xCF`wgE8$J0ECI+'
        b'OVoykaFsKK2>U81o;$_J&nzu%2mGegGn<(?o$2Wu$jmJDjj-BxewLZH>8uCyfvwPhd@38CmYw3`!2oQxw_VS=y!y$Rz<q3<H*@^}'
        b'G^&U8C7KjMHoCH#FT4*>IIQ~8%yMh%Lw#XmG3P$}<Z#mA)P(Jy4<vsMIZGcQJvHy>Uq3CNg3Mq_#tO`Y^xV#KwAmm%y$rIYKv<6O'
        b'y~_?Q75JA*M!I%)4P3l1Fmhp_YoMoVQ}w0sivxpomOf2qOefEVeHHe(up4bJWj~(f{8a*2c70IsIxg9Kc-8jufqea@ZGur<x4<$F'
        b'L3X|E{8f$l?aY=SF#`mrA6(D1v_5npdS3RA_f@{V;%s#AP_(39^c-*M?X+&xrYZZ1r8RY3u-58}m7C^Y*t7uD@XH#<PQ`O?gWYs0'
        b'dcoPaASN2`ousZjKhSeTTDo)7@kcI%qRui)>9;b+w~F0=u6@1b;fJ1+<?>F603Y-XtDl^uKiHkMo3?#G|M36F`qqG^u596RPM(H?'
        b'O?X5EA14QbfI1gKTY>5=Ns*Ve7gCMDOlJrfM5;50C=Wx;i3$Pf9YL!=?MxC)1u7MyR*GeYgi5W2xq`J?N2iKSYpw10plVe(-`Xc&'
        b'd++xrIs3Kt+H0@9_FDU~HXsNe_k<T%Y&3K_2tth>8xjMlm5J=Y7z^Wd;45yt;<SD~Eh{n0N@;xr-LScrPx5Jfq*))ekl!J2>KAxC'
        b'p-#nuo|e|wLm!rzt-HwO!Im#UPjoBh-{6f;gZ>*VY}Eh8kpK$gJi8){i9!alb!Bvy!Q2Y-z;8NNLU+?JB9^sj^<j2>=;-P45ttGb'
        b'anw+>jjA>cO09!Z-QYA+`yP3n?1N_`hoh@q(bcxG9nJ%<F#kqs=QlIZT-+qQA#c=&?JV#qd&h^9pMA$<i6{H6o|FOjo>l-ESyY>2'
        b'Rz%T?2y@OeX2oJUXL@Z5t%x)$XgWt)dx=&oaelS{<+en&oApa*MJVG}9eFce(j1%}wKkz5{mY*3&V(c_B;EQrvwpE#AL-Udx%Cmf'
        b')2dGb|JVr9_e2XJ`~wX5NV{T5Znq3-f%Xqge{>Rgms9*^Z}1HHqbKrXa-XEWgR;c-J{o4ec3HdKlGEK|2B^W)<0NK%ggN+`reL76'
        b'xkZ{4W!6VpS_%`&(<6$YR;ND9(%yaP#u<CmbU@Onr-5wHy1R-nAkzK>XyNVlJv9l)*^pTgQPYDi;M_jwkXQa>w&69wgz!9TySxK1'
        b'JJf{U=<WMlmUyKPT7C73?9xT_x=V*I;5@2dcvruGS<e9C@e-9H4zLH%cNGh=qvCV4iU^fru{LKqP*ST{a@({gzUB6#Jt{?HWRZ#O'
        b'1EMCd+3ll>g_-?3D$;?vq$ni9#D+EpuT7x!QCfXmND?&ju0C?fbVbjO^&;a>?}(C-5wD1}w(sfwO<j9#y9_KA=XC7!9OplIeJAnG'
        b'9tw~Kx&n41`UQZXm!>0%1yIr6O8m1QbqU{wTme3_cJ4W`<Y;m;OG<<X*<WN>MMES*BKb9M5ucO{NTIp_u(XOJ`bdijOird5kCYWX'
        b'_(4$oc^@Z!P9yO%9mLP&N=w5KQQ6%wjah=^M|}_JPtw-V1L#h}?AuXg1K&-at2j+ZNAKzD&u=9@#UJ|J2)M}al^7nfgY6OYB0nJ+'
        b'yhw$UQIq~SyLnZ_{P`cyW%hZ&5q0xkkPUCy;o7ppY5j}sg&j;B;_ir|!qAJcMR`62RQM=W(0AHDA}aSAudhY4knqY5*Poz(ec&!T'
        b'ST}ea0QK^e7bm>CXg_81AI9GBzsOt5DFVfZD969qy_Ya~(KvnNFn54&067Zv-Uml_YmDD77j}r=6qOHyj&veG-d%m-S=sQa9j;YS'
        b'$vK;R2jhpZ>fT)0P6`j5EE(4BaAiW$=jfQ8GZZ_qr_dgXABxL!)4?MPB$qB-=w4;I()Td7_)5ODwXfSX<lBCvR`I2bahQ-8mRS_7'
        b'{@tOMERfjb>TKT#QutDH_j}E*w$QU>eJ5I^r|~Q3g*l>D;km_H6oU!6H9vQV5COw|e1@Oh;fjIk?^Itz%TsB*)}pnc*49yg*5(gQ'
        b'L;6i94*G2e0oI0Fnhhe6^flZ;M%$y-ShS|Ce4ViPx5egIYW<;4Z0JZ&T9>jZwA{bx)ym5C#B#|xjiswBK1p%H)EY`fNUiqhNQQZU'
        b'$k3)HmxJz#rf|d00MpWS`Ap+LVROUC$4{#Gd*g7ZfCpNW;{mHn;HNTaq0leI2m8WP?%q}6jaJ<33V8JBhM={f8KmaOCr^fiq)%;E'
        b'v(51Bgr%#=HhA;Ov>`DE{vPX7CXWJzs`^KEa%~v5(^%r?)DUmd*(>H<hoFPAR;T)>FWr)qv0^kMsgD$7H)JzS{weX#8y{4FjN&K('
        b'2Kfb;uXVw4pj%ctcc$?h5Dw2{!#&$wUv0O&z1?X&&Fn+^%d(2%)qRZzCUzC%R~DpvAkcpNFry$JxJyqi*Sdmk@UrnQ!E{C1Gt456'
        b'e@?t6sZTebS)ognw(4QF@vZ_HA6hNZrXvFTB|%?1o?ArOs<zj<tOZnS=vuw?-Du_j$^{xpo4Pf&S3tgO$Rx<>hyFKsZLw{c+4x%7'
        b'Q`8OT0d<Q@moCYIh7E37mYvOH#cK7_3iY`edzP(iS()vhIcUnTNOLXG#-D0KvtxySXLUKE!j~*e$_Ia3)|6Y=XME6XtDcTwP0WL4'
        b'ep5qPvzDA`N6RkFvNn9#7n7}N?y7Y;{xRWG(A4!Lp+mImQwp>lPYPjiRY{s`xexpHz1Vweo@sSo$$^RDg8Vu}pOTLs!soK;>aWpc'
        b'`kDmo^@08m^XlaLOzVkRgBeP6a9eA|p-#ph4TkJ4QebyQI9?Bx-^A!}N#+~dbp+a90+X>MJh;53c!Rp^IYRg%)@|$HhpfEH!*pka'
        b'-CZ5XTcj>Z=ypW_ZXH60hSjADtd*2m=2vs#Fr(d`dqL(>Y#((+gOUna5J!3@zPN-LZ`8ER4=F1y9z&-+tOt)b+6k*^Y+p<8jbZuk'
        b'Coa0u@NpjE$qu1s6)R8Ru0feEPUxDR$n&0bySz2mO*j?4=q&;shMYf_5W?^o!UzKG^<w32W;&BmCaswf$-KP1+-)k8LPX8JuWpRU'
        b'-ycuIFOH%LobE(~Qzk1fdXoGNd&4Q8j?(PEq<Q{}m7jT>jPw#@Ph9bi0ZK#BR(vE(-WWE+92Rt;IYb*4m~%x}D7q%!-Zf*pEqc4#'
        b'p6Zc2vo5{bAM>%8R|h%6X71Xd4#`GG-B!=2+i4Lag;{H>+0jFX1x7W~VZjk*s(G}Trwx;n{^qb5tAa{RN;SHbHa~*Ef)cR<HmY4Z'
        b'$jNXzEGWd{Lz`F6pjQV8$5?Gxusv+%>Elg1&i+oe>&mEUN50mIjjRp?UERD|4mC1OTcNAFe70X9hWH(P<yY*g7NYteEYz!AEsrp3'
        b'y`Vt9B_-A0OwK951IvzjZnMi_ve8uvK_Kvz$Z?9UM?fy$x$Oq8SJD=Ww0$rr`1X$r9S0`Jkaq~H*M)F13`LW3Tc@e?)<sQNuw~D?'
        b'K><ynAr>+q(L(t&*EO4JN5OEY4JDJ(Vo9-aEbXP*SJU#-HqO4iP$Ha|yvq%IgVxP%u+|*va*k8M2f3kam_RRR`l6+q7GmHz3~{<S'
        b'lmvw$rF;dbq@eIJecM1QZHyF|exyRS?>t)bAyGXKBZF!|FAJ!}$N58`Nh@DsFJB^OL(B~|Y6Zl4N4jG#dzf1p3f}UX1U+wI2BE13'
        b'i9UU*G|?-BVQSbjfgC+(KE_8vpSf_17`VcMAav5A(+BOL{)_|>JyioJYx1S3S^%xdm!;-u^8E~ki3qiNtts+)M1LYpMfNBEW0J?N'
        b'v&$uU{fR>KB=fax+eQ?8*I%}EG23i^*`_(dIy}=gdHjJ7S>)?HyDO_dWz&+ZuBLOKq36_Q9W6YRVcDpi=l9W4`+<p!SJl>nd@u@X'
        b'j?c`hX}+h;3qmuR<0hNcf4N;BVai=8&F(MkTFYcHmv^*wRr9c{GUT2UQzV+Gl~i`WSG*VYGcTG<I%)lJsKs)xysRvUsE)ukeEY_Y'
        b'bHxSHwGBGmEWr5I`NMzH_AkD8^z?yjWL5b5*b5}~gtGNL5&i1<Ca#%a?Ey7%KcEaNC$x01In+06N39Jo%etQJ0y7f|e9G!BJ?Yj%'
        b'Hb=?CVF}2uRV}^O61QE{yMDi|>&0!h-)=Mhq&z=en=c*UcBr##kXQE;KTBU|%f7z$URJ-}AKC`^Lk)$SvhHOR^kp$Hb!ht&AKtrh'
        b'eJz@eXG0GPIA;%XiLB(v;j&<&`aH|g=OW01@#GOuV<k>kfc7-2)eAfuCM=l%F2vHbsWvmKp~PLduc<hs-I|eWT`A4@DKR4>*L-TO'
        b'_7s&poaL&$maWceAX6;EH}o~nWnaybeRn<ko)9!+D-Md^sDi9TE9`=dD}6}bcZh25H0q^}KTTNfG%BRJo40Q0y&0~E5u*W4>p`~u'
        b'J7nd>%nQ%;Wa+=Wmwmk&J;VvtG{9@rW2T1`SX5lAAUg-nP{ew{^?cubZPnW#xs(6Njw<-p9+VZJi?4`=2xNa1PRJz_!o4hJ^kiTE'
        b'?w;@nn|02@6s^oYmvt}K(gz>+py@?P&{Yg{RrN-0Y~pxo|Gd&?QpWhkpP(-?`?rFDoz~yoPfBJyCX(l1%pcxJJ!d*8%{qE01RZ+%'
        b'-OK2L%x3hQisb;zI)SyeY?p<|@&jX7tCv~mELGaDR_|}t`vJr}%yKU4=&HCy&}&b7YXx+Tz<lIzO-o2uuld?Z^Tq3~OJ>^zv+~$<'
        b'Zh_tN5et?M$G7Bcw`&FR?dI@h_x4P9gJ^wzkllM`Jc|eyyaUzfr7&G)tk{@+F5-G-!`8?H5$8xr<k5)!v~wA>G}E{>1F`MEO{CLV'
        b'&aLO~ccd4F2g=rq3zV{~{=8718JmdQ!i`0%*R}5*04-?Ny7o2C@@w`AI)n%dO(;2IEQVX2;DZ1$ET3487At!3wYcNui9>tjnoyYq'
        b'Pl=nZ4fV@OO6eA^Jy&}#`8Mm_p>TZ1>M9@S<@*kNkLoY%pYe@s_^)QyU(H>AHQO@G%yMKW&AT6G=|6EpU4E{So|Us^UCx^L7`=9D'
        b'u0{HhCF49g9|+K3V12~yt;1m`K8B$vg*Fk;iyT3&qe%{7TX?km+?o>~tUZ@}i!D4__Cep;bL+)Ge4L{#x-8Po?oA)JoGXjF!L5a;'
        b'!HA!!k!5K0!5V!Kh`v01NY<XhP?*|73cd-{<>eD3KXC;GP0q7|qK=!7uxlIEy7Hp@K4fZbwO#W2;=F-}Yll6t6Y?H08tX6)*Mri+'
        b'YV-KIuX)!r=8;gmOJlbE-t0c~d&gVTlO>?joWeC$JaHwJp&NxNbZ`Cabgk&%Y4w2`z1(q?hS{O#At;I(bTG&1O6uU{>1A5IpXXon'
        b'8c;S@Vb>OzFZy>aFxyrD)YXPv)7Pa7GcatqWZ-kQu(J9RFnFGef=RBw*E>z<qVAhrFV|)=8uML6aIL!7lxwnt*2b6>L8FS9wF)rL'
        b'oQjYkNd?Rz#_<k<*8At_1C;kBbS-yB`hz-rNA$BC=jjo}tjl#~-VB$@Y`!S$v*3NFsa_%C+ZS2gqkp@tBzh;v6~`Q|LQ8^yxYNBD'
        b'g361u(;W>Tjtg|2I~ArLSDfby+H$S&FnYw(?TX_}m1~Yns88fgyex4An@3!6P8YY=6%X*ggKucfQjjIznd#uvhVH`7W25_hhG9;W'
        b'nQb32&O<LV-6rnvMU#K6KQt~aHq};K-q*}4c~z435;@o*WU3Krmj&f+m3wjFNX1=^J33-?t$$=_hrl~uEIY~xEcv6G<}<T0lA=w9'
        b'-HFMRjz3Xd<<&#YvS_3+61Br=E=L6m%(7f!89wdOUE(+LW{is()$^M2e-Jj?nl@e$)Z$#;<}T%z>|P14P@R=Y2AN-)u{J+@V+YUa'
        b'rW`Js^na6IyltDQxU~L|_1WFg*3$Z@wdU+bboYC?gu6bE^qH<p%!n0}as>Gj_q@UmN?N&Bcb-?^XTOo<>E#;z46QyO=SScqQaExD'
        b'cOPWUhp@(XF)~=I2wXLXs8(aT&2kM-t_uhTjYXsJmyiNdm|NQS!91e65Bn%Nw|HzsA$KbRK#3Loz~lBHZ?kWLX_9wlmhQff+_Lb_'
        b'n+&p!yXqO+NydHXeM2GIG%9@S8#y7Qv8>RL&7?eJWo{W&ymC~xNrZZhmyNdOjsj=viV#QM1BiPoDVUJUYcOGAadAUg&np|snQNPw'
        b'kx;^R2*A2}MUK4bPjL}=aZ%o2-w{~%A`K02YHmC;YnN^}ddhyKJZ}E*8phTPML+8mDgW@aDESO33N%x?pw=%Q&Z*8v&pjyuQw51h'
        b'#}hNgGCB`lc-s$15t5{NRiaS@?o86?0|%V!CvQ^_dzn96#ki_~yRO?p8HPd(=7Vysmw@hSS}EQ4))}WFFfoyz71AyEFh46$^U{p$'
        b'jlv&TD69+kZt&3XpBUGAD1Te{Z?^c8$?aQ5)x`W9<L7TmQUu62F@BA7!6sHCnj!z(Lq-f_Vwffr1H!sPc^bX=;!Dt9T^gm|rww1)'
        b'K6S}I=W9NGm^Q3&C8cGmmouc`u0lSl2!LUqrp}JZR%FYvaYQg$4~*gG_+a8q$*SNvnlrOVd7^GxMq;V%^RKk0S7an_laGm#jcn>B'
        b'P}yJr!}N*<@JB{uRl1{l1!(;4r#0@yy?iu+--e-_iiT(lU4G4c7z5J;LKW8_p-S?kWpXSl1EIcKMXpE&hA^i`jYGu#c2s|0;-+oI'
        b'#ihCn7c^&9z_%{t0(Vaov?|m|BGy_*)pI%Jq(JyNl4Zaq4TS}{Yewq_hUJVanCS{(g!>_-&{h#!?q2&+VPM7GEM>1`Z9sMyIcRsM'
        b'n)N}<P9wLA5R|8wk!4R6rd>;wr`?eU{=9Rk(-qeN^I4FmmWFisO;MIW_%n+w7bP!d%`OV$B%c9#)~a(S<z%jDtX9U1nSjEzc$&gE'
        b'?tRZIn^D@JUAnqUX6r;*TofqomI`O2pZ)Y@6Qh>T$2u8x_gbH~>uNi@M>{QjO^nr&zb}qRR<dA~Ru%{q>~gViCFpGnNDd)pA;Q_I'
        b'm;q>=2$<if2!J6B1KIdUC;+o?TJbT*CvX3uxN^^$ed;!4+jBdcf%EbLiG6R6mYkyCqcL#$z7L4x&se))uDtT@u7bY2mBf$;ZD#>^'
        b'!-@&i-kk9_CCPRcTXW)XJ_V4TClD5dA1!qF6s&ci{frB5zYA5AJ#P(pn)+6uBcz}jovUW>a=SjrsMUw*R*{8(c%Ggr^zVf!N|EP^'
        b'1_AqI3p8O=5q8%ly}}>jalL;W**|+Lr)ykN=f}m-2Pi`cJ=ng0ghU>58x<%}X1U#|-l3tqGY*2H#V1w0p~<AtQ>mF+msF!yXh6D3'
        b'G@lFml5qE_;$A^<5~b=7BIk^_$~y>+evV2%*KmY=O|ti<XaUI?^~{$D_B#TS2M|>HFwLpr@R@5!LZt{JUwn;-{=@F-01VrCXi*El'
        b'TqOJq=`D^zS{KZkMZ$uh?=7FK5q|?yP1A|i)_pyfn=V)^%@53Ahlqg1X{hOPy5*AwK~=8^rm@;jVBW|<Cy=8ad)F>vUNSv&#mnM`'
        b'M-_?@1?Adk>Uz;+D>236%E0L$`aAd@J)JdN?i!4$0C68@*WL5&<-5^*;fS4>e~Aovjc5I<;OuXA?>aB7lIUhr#_!N|spZJcTj%&Y'
        b'VAc9TGwtqZ<<{|Dk@f)lQ9_g3rZnx!+0%x1g_&+-UR1kQnQU36ae>EodaJujXNn)`Y?sE5wz-QF_VkJt9VeU@p2Vr`2UwMUR$Qh^'
        b'Kbzzo3KYk9w&uPii;k!6g5IMK9<>r9u3WdP*lW+K^g(y^GeKE0G_mhU_6AD|g8xgUn6-dZ=_!?BHb?qKeYi@mU@Eq7>&@Yf`mp4a'
        b'Fk*Ke?cf`<G_*K0JJ!w<7DP#%{R_~;5t+0u9V^NA$?lKi4Sd9oSaG04;xWV!0Bc0AbVPyOY&<u=oeUw#=me?tv)z5xQh+_8Q0k7}'
        b'm|tT$x*N>(%cn2556?EaW}CX^m~1DuGDnfh{@OHQ3;PZ)`6g?;QS%l7bGgNBGVRf|PV-XGQ#4+3fIZx9aW|abYO37Bk?t8&*SW1W'
        b'u?Za~^8D=EATnjScY)RECI#6e*`rx%t)9xt)an&L`c*T;F-==@Yh=-JK%W2=J}>jTt*UdvzE~V+m=Q~HG|T{XmQx7s>H}5igv$)&'
        b'cEqt~E>CgnLNCWAuLNS9?aT#MXc$MQ+J6!jaSz`}goR#x04Mom;H*K?$L`8tGEgb4dJP$<)rZ(!g`Naj-i|woXe=o-aan$1XD)U!'
        b'6e&{m<6bSt?J9J_a3z%f6S|&>5`2yBf<MsP=_-U8eJ17?eNl;#fw`-;>CQjV$%XRk0@vWyu0L<R^WR%XxsxNdPq#X5_`;Y4FbMGR'
        b'ab3bAEuNx(Z>#paux}-f4x8&Ktt%DL$0bGmc?$R^1I>LW*}X*%LeLHC@B||H96K<`8a=C8kR!W1m(=yr)+>_HfpSi@G`v5)w|(rc'
        b'0+dfsVnU(v3x5@S`xbgf_S?S-R=q<A6_|eQ)(wSQUGHwSy}K2r5wH)lanHYep)%-M!}4*Rgdhc4{Ven|JJY%~4{g29(GHYr^>fLE'
        b'z}CrMvRaxPRRm__>={u6xZc`o+v|mdjSCEyd@XLh1z9AdaP7$2(OP%j0d`H`d-_>hbCJhHiaWuDIxrgb#Yf1UmGCdz-2txw!<i|E'
        b'*}YMC{UeK;lmO!$3KI58fYjHg&Ud-6hj&3)yS?XlO|9=#CiI%p?AuJtR#)j(GiZSSv2~P|jnGothOM_B?Qxt1`X^2<G2I{61&=qm'
        b'yMDjba<{WtYO34Q>~6UCMy^HHHqth_%R;pcBOB7Ix|;Q*@;(@&KPP|7k|Dqa|6~WgMm8Gsr+3JCn#M0bGV^CN#BKGe`T#-magf)V'
        b'0^Ju+lPT{`;m%;%P*Od*B}E|c?r=}4IMY~&uP;hOiy6s3v!YE`HT`0A`&SBMeLQ7TnmyFN>8RF@oBavIF&5dbCMu(u(uM{!<4ww}'
        b'K&Z4~(bhH@{F4izW<J`{$c{1GWG(&sZz=}1P!_7TAHCn3brg*9%vv>BYlqIY6KEb&{07pc!UvP*lqV;bpI9?3SuSaGN7QGvifeWU'
        b'woRi$10smQ613)3jRq1@yx$SODH*uWLcf604Rk}MxJplYz8T+}z_Yfa;|w(|K5jSX#NG3+@ynMqpYvd5%3V$6w#%&VQf&;PH<z5<'
        b'VEBrCdgmaGsUl{0(r7D|mmiSVFQ)T-Bk$4q{@MM@&Y=Rr4w2(34AU<vc}Odi0C6-2*p#M7<7jGsX6=?<UPcm?){pk3?y~5P4r<k9'
        b'<WXAQ^2qCfnhemqBuqV&#*04$ApDS1s~W@KElh{Fwt;yI@h3em#L{rcDWZ>D<~HGIe?tA|H*#rNqJ~Pt)l{X`P9?Te>c6}}3fdHj'
        b'G(|1}`U7g&vPd-$I%eHc<p{cZ68w>_^8P|T$%js}C~KbGkR{N}3zom-tIhZC;5+*hsifo3!%BL5)gB`GIgBKdzd#+b&w%_vQDKg7'
        b'KyN9kA1Xg&@Pj7)*Op<^8_>qHG&FPI20Q$xH(W2iadw0n?T>&#2@O}SABX0CQTK452VhzHMK>f_{WCn8kR)`U^7bC&%%E1*6gc8f'
        b')HR!@VOf#6S7hdkyo@Upu=0(WuBbQA$rB-fG8B$~5&UF+j{MZ)g%aT*)*Kqp6vR2P<9x$eA{yt-u8B7?QCm!ijnV3I>p|v=3Urn^'
        b'-(S~$$Ec}pW;LNCbFM;rWWtn0Y4S;uugRAI87OK`>cQ*-kw>-pQcb>}oVX3`962y?HYp!kJDm0g5Oy@w-z7q=<2wEisN-9H7}(CP'
        b'yIZ}D#nw56W_F!sz{GNERvknyPx;I^x1=rcF^2{BN=|p%!)7vP5ke5AR|hs(EZx2MSr|-~e0uc^^J;nH>L4`g{(AyS<%pQam5Tf~'
        b'YOg`=NLy36#iG!^Vb)8{VIh%SX1&ZDHcRmuMEIG*X16t%_5RGXHzHl+6518#WoLfmaPu9rUaWLN|KG~7tL0ZDLlTtW>4cce33hz|'
        b'>F0K3NV`DAq4j~D!{f+>onzvO_nlU-2DmjYXwT$PR(#x=PU$K|y^>jjFn&pYW<P4rYy9{wyDP#oq^Od}9|`Pk$}ptR1wR9ZNr%Ak'
        b'x#Dt8%*`rbjd=Xw=#7z!?yhgEY)jrSZ1pX4mj~v)C@6}JzZ>t4Q|7rBtMX(jI=CcHnzb#?sm%+@h#ghs1(G~fo?MkTV<C6(6f&qn'
        b'#nCb9Mb8n!|H5KI-q2gCRC<4vRg7kIS8BX0=8LLp0Z`w#=*ra25tvwhh85!>E0;+2wm&1!nNB5y7Vrq+A}mfl?DIyvIWBY56&>F='
        b'B;;}%)Z>sb*!PBulwUpjlYMAniOBjqGWrLLu11eVzq@;X&Yfdbu8FFyV^y~Cs;gJWlqJ6F4ph&>F5cO{ev}Tm@VDuA4p+GzRCOJ$'
        b'vOTB*t$ZX8W@PF9cSh-17yc%@<EV1ot?D{hWxHFI%=ro&$(uEzkfFk}QQ>#0T(_#a_E*_%Rl&?Pk~bR~e(~CkZQstGerIo$>)WcX'
        b'x2kO4RwZ9!3y0%2E|UA-*;Vy}uj_hM*Pp9w*Q?NF2T&l~(cYQI@cg(nfs*HVkQf?em-7bRLwDkj97gV;y*vxl^E9x!7V#Acu!YkV'
        b'0c2<#-`gUxChS3?Z8ut9O||F7%F=La((!_@7l%u#T$-v;SL)ew6qnz#5b}d=oVv3M0yX2hGrXn^48PKT<jb1c7;X+@pWLdntA+MV'
        b'Vy2yWu8N#(iUmy!7%`RPaWJ4OJ=JU+9&fMb_Mr;G9y*V(fXm}2x=Rz#od~vaJE#j2J6+yd{~Mj{S=Y{O^<&Rp!#U-5o<<+;+0NSa'
        b'3n(oGLm)WMRqVFzzalx~;@rb-2X^0k2J<$qN|Lf$xX#XPG>=%VZfn!oVN;*W1j<Q<gHoDNUdc1omOUvmFG5_0&|y_HIhISBZH-4J'
        b'_W2RjOE9}4oQXi=p-~xf=tCm86qASfHl4ENSM~C&&C=WhGHWwsduW8;=2MM|S<UAg6|)-+(-DA1Lbw2Hlx5iN7;~FZzFuB4j=}*|'
        b'5FSy4TiYm-Y*Tdjek%JkrcwVJr+%SZA3dV~55@;odF>zNjf&q~EtBplqpW3Ag?fXbYDDoL(altGGv!u9f0@~=U%R1-bSf4OmNr~4'
        b'=5CRpGgl1x8YvpWQG)~(4Te9lWi9BAZG<h-0aErO76VHrm>Bqw1yoXI5(9ngzz68Nm$xq#4>?Ls8#vEWdmP0FkE6rC@z{tgLw69n'
        b'uv<hc79<~r&M1gXZ}`rL&JlJSrPrukXp0u=a`=qzJ@YfF7$k(jFs^&_(5a9$R8|0=?DHXnSCP6SFkF73D|*oAim<DHW6zW~JLJcH'
        b'5WdICxAQbgvg8n!xaWA;v;`Y{s(>SllcX90skRy2)?IDq+dPS}lwGeRXM6h^Y)Xfo)#cocv&B1%*B3Ps17EOcQlp9L&spPR!00^4'
        b'I^E5$IK~I0l)oQG;eT<e7{a)aMep~(Je<6l1!=#DJGaQ`9263uL_7nN!rmUtdS=fRKDQx2j6c;Sy!m<&UxG5N(u+O6L*wNC(@$26'
        b'KS>z*oTs5@_g%pg3-Uol$-P3k3XRq))DHqK%Y!FqZ+moJi;w+Ce=?5L2&;9^<UN~4dban14k)xg2ow8C*J;+o^Ob*`x`$(@C6H*S'
        b'Qpkhx;eQ!j|1x&{%V^6oGAocimHQ3#iz4j#)346Sw%TDnt5jT;41aEPeQxaf+-OTTGAXE#cWN-KW~bhR_tv2-gBbuHK5cZJF?O9X'
        b'+Fmp=FQDv5379_oiP80mvFo(a`#8yrhq7PoASf$1x^e4MxfAk)iR#Df6b_yZ2#2FaSC6r)$7qW*GT{j5ulFA|PE59y%l}7||B%tu'
        b'Y3%AW+GZP>;QyPyaANX|qZe<->m1%KMwi3b<uKZ0M#dKvY3iTxozHN#(PcAs*%99B+V^f3XPvVgol!w#ST@!iTgFjs#e^<cl;_=`'
        b'T#Gg+e?ZC=a6|UEu1-*RJ?-4u18GO~ODa<Pb2%LZhzHz}aSDhI%_Rw{{iOjPET#LK5i8-gVjPl=-%srA!AYSx)HkJj$ZK+Q33+O%'
        b'XZ6GvITQc8fB(R>VXe_sZtN;I+OBS4E+b_!;@nh!dh>aH$L0Hj(N%2hDmL1_*usoda(xtWbVfNp?p!pz5#9G-yz(?$8O`dVh&cO*'
        b'bw9|*OT%YeND{~6%II+zQ!UdqvR70G*hPDMy^OQBh+X$6`3Z~U;%FIq$d3*I{lR|Za!TxFn9I1wK*g%OAeF1ImuFzdbvaKKkUK$@'
        b'NM%-{{CTciE&d1Hd12;k7}geOHwa{|-C8}Jrw=uR0X{$H;d6BZ0<-KD{rlx$nt)~pgiUj46yXgYZ%G?gf4T*%708rmq0~M`QjoiJ'
        b'H#*qF%_7aV?5^5t@pm+OsY)+1%w?<3vKZ0;Qi1tqjmvL7NFD?ZMe~+p_Y;sGAYG>BE+kvHj9Pt|O0RT;uok@5t_!|xe2k2$T~FjK'
        b'_Xj@mo;~BnPqJdaWH`v^3Nm&D8EutYm@-6cjh+B&%X*30=|XmsAp|6&z`Ff-K}61!cu-l)wYa6RRwi{(UbD~OH~yq3HPrqpk#;mS'
        b'w(US#KN*Hh2|Jh)cA*G5d3fg*5FW1IZaI620>SGoraboKixzGVZrz#5{R%bawuwof4n7l!NS<}zvV)|%?rfoxu$>2)8z?T~02v%Y'
        b'M;<`s^7^TQKnY1ha@UqE)%RJjdbIx2S2fA)yt(q8@!SE**)Im-iN|%9o&bJsf8q*%C)%s&dNRMxcz%`Tgw~%3S*d-MFnU%6|9#+F'
        b'meVy2>!x_vc5VwfEu|TseY<6wS&UJ~)Ko+?MLmlSsYFE(rtNC#WHfqe*7Pjrh}0tP3{#uv=#b`tJDeYkkGDjKe|b0C*i&zI(sSzj'
        b'p^jHs?-k^2vv12^0FA<t$?AG0?0IuIIfTj{-_mt_i#-Bk+EL4GN4Gem=6E#!>&>8;_qS+5=XCHa+fz#uEoPEmOK9?N$30dRI>)jx'
        b'O=W5~x6$Z!F3M|zyy(;&Lzi*h0?_5?x#%<Ioh|K#a{rKmH75cV&kt$uJif7~r<M1iKQmsz-9;|v$v+`G2*w}f4ryl&Y~}#;67m)a'
        b'V@8oq0@K%Raeg-3nY<19w?o7jQ8b$Gl=sQylEF(I0_GzW6~~K4H@9remR>&d8x&I|xfPYlTksg6_DuzM=F^(gM+PO<?5;~MNdh3G'
        b'1o>_*;bZa{Y**<PU=XUz`xZh;C<X=@^8-StAeaQM6)}H6X+VEu95KJ+&_GW=V-Q+}Le>9bu?m0TmB~G_=mV5z8)-)mMmT<8dnLB)'
        b'E#xa#aJRM8v3v48cLIdz_pJKWExnQ<uvwI~EYnc=8qr5#ZDN?2qxcqCBaV@CYI*A==1(U~f82JpTH0rknP1|EN0MNoTi0hC2g62b'
        b'VaZo^La-EqXaTc^4NvEhd~{sVco&@j^1jF6VSDk{&|y|ZStY83xOLNP{kJJe+KBUw4-+lXyDZY^B&qE;TR@PETJdGW-WtqmzQMwB'
        b'C6K=cf(#`2)Y9FFPyHyM8(&zaVv9O#%T9WT-%Efpahl!m8dr<xn_wQgQ>~w~r7L7hhmiRMQB{6Z*d<4yeiXVKJcK;FBQ^9CSCQ!5'
        b';4?H|TyN&q<=M@ge;?e;#~Q5|ou3HE(WfVnCj}Apmu)5I@V-bHox%@~m_B0TUqXaIEaKSA0t`9va3L@GD;B0hZxx=uO;tf8|BL0G'
        b'<3Z;!t&8neoY{f8l2U;(z5mS49^0+TAs$$l%zUmX;(Fvuf@6}&`{jC!9Q67t_1nzdr1$)Tjrmt)uY{b#QLlq%_#<lu@;(yX@PX7p'
        b'-~@<U#6I;wWII=hUi|H+9Ga*4h3y}ePB*D+U}+jRTX8GhM@p#HZNHQm;L`v6bkL$W7m5Qo2IdzyAE7vydm&m`^-G-qGx40+cC3<e'
        b'Q|6_)&Qqkad`f>p3GY`95uY75Z1Bd}Ff)<6KZ`lC$sDnw{$dAm%3EL5fqPbx_Pm+41E>zq>mX~GFE>y5L~vnt>n>XF%e=n{-57|X'
        b'<aHwLnbq2&S>#e}(QK`CJ;~Rmmut@ylD?YsTy4=@jkS~v)TFP|7Ezz2j}*-uNiQ5(J*VW%I_<~hB}FtjucRn6+qK@e#9E@|VYiOA'
        b'4lBFanC+D}Tvvq1?*{S)pUdj|Do{rW<&`keFvk%-Xa|H0DhrHmw3h9AOJQ~prUHuD@_!nmOhb(ci51>p8?E|%Z;dh6H$lFEN37S='
        b'yr+`2=i$}2I6Y0huCkYx3N>8iW0^&jD*6?T0E>?2r})qJoPWGTayY?Eze4g&wS4nZ%w*!<j*uD8JFUotyYj;0^^(Dy4xZzmk7wWR'
        b'`dwwKkRdj6*OtaJj!9eP)Jdvy8RfY2Sa^>cw<-d-YS7=7S_wM1<0BR=PoxV~I6o!-_ej)!j0hZ)SoxZy(Erc}Gb}uPYGp|KnkFTa'
        b'v5Awi7T)2)Z2wjs02=gHJYU&MF!MK0E-hjh^2x<Cmm~Q##$t=<NdL7w<CtP$<-lEbRub~P0qvDH;<iZWX0d08VhRz3?S;r|#A{Fc'
        b'+r};Z{gsWGTZtIlQ^cKhyp_Nx5S{mTb9COH-hn$*WLpFI%7`lr#1-;L0#lFo-ELW>YV{oXQ6cigb&&FWGf|&|4oVunobbjtJfL?9'
        b'VkDbf(#nz0S7OM@vtRN@Uc%0vMFNL^`-;r*-s2d-CaZ~G93eA@nl&A4q6N8=Fz1{1C&aK75xhaSV%{bVJvWUPgH@{X=5lWpvK6*x'
        b'HZvq@i_oiwGmk4^TCTS+k1EKSoWGXIHzXgRwp;u-DOjTtdmqMwG<t+Dob>mt`0;6;CW1b|QW2(_4+;7-yK6Etg6~0jn$XMJ%|TPX'
        b'$gWn*s^el?n(S#lzoc_tA<esX?U}-a%ir*M1?L;bf)H$-RueqEE;7VoGVP%WRJeBL6x`1$C~GOoD1Pd0hKoN{@eU`>#r5$|0VCPK'
        b'6F7N%U|P^TIy?EMlN2fO1l{NEJ2ZS)!Fj~7#K+^Pj_eL%UtvHm&KyJYs|7Cz5`naKR!sRBSN@xgIa1+1i1nSxmkv)_BMM^hOaxwU'
        b'UdXfHK5_B*Ak?h3R{(n=$b8P<)a5#6|5FmR263(5*D{UtSEWu1p@nyl0B;qyx2n>8INZ_0jY!`8xq|8}HSq6G$}&=7sKF+`m8rPA'
        b'hi6E`bveA{l02Je(ZPkJB=OZg$3ART4{tvVpdmrJ6N=0sUXzgX;e#S_lB$1V$@!kS#G00WO!7eDCa>O8S)s11ARTF;z*gF{P|~k@'
        b'ItV??(}*299!!T~R8)RzXfFZNt%cVbN?H1%qRjbNBxIL6pD2D?YNwg262MM(>2Vv6yIJ7vm(>-~(PQQaY_N55n_!Fu8Si<>>Ml*7'
        b'1L%+kXeAFt0`62P8vLs&8m&;ta!FlXO?>o_#2!i@uS`oyy$6s&>$ayir_;5(=1?D+Ca~~EeuRIGlK_2=tJK;#)`8IU`n_h7Dr`$D'
        b'pnf_Xlb2)4pIO=piYgi6_@1qP;??zOn1uD1VsQm}S(%=#c%ec?14fwR2Hr~4=a4*Q3>Hr)p0DuSLOm5nWWHKvjioqWO7N3P81GqQ'
        b'qZ4DL>i?*iij3ovuV=(cQIOA-QAbrwm5B+jFnSQL@@6F@(kM?PFDA4??J4CVGbW?Bz*M?p5089(R=N`Yd}bvmE$A=ZQNvS+D;n*H'
        b')l&0p(@HavQ0}xmF06f@{a@kCg3?_{)Ku7#rxsOYSWvhYh0S59<YFrqHm^?gM%W%~CVi|H>C-riM*X;)3<f!*epHT1Y7jUr0<W2b'
        b'tzmYej#@5}M~Pf_%dbd&z|q+?Yp(KyK=%l_&a&{F*42|WgG6LPkhn%P(qw*J-il9BO;aE2I4-C!Mf&b2%3=GeTxG>Qe^x+usRzof'
        b'q1(Wukym1hkIOl#GXALE%;9oo0it7^z~m*jAo&L86U>Hn4VTXvM9NM3M)dsH%cKuU+g-Dm3n&=bpy(}!P%ojJi!G5{&gmK`w|!FX'
        b'aN)`m_;SgumR7<e#nK4$w)tIL(S?vvX)wj%@|eTrsysqvy%q1LI9ZN(5DLk2#_crb@WoVl*wp(vuMu*m_=8v?S%Ibc8Sg$h82?;>'
        b'|4T#s#qZgzi<$RPBNu<x;WNZ%-b3Gz@Xy6{OzY(LN%(f4?+8J?#;dQ{PX!rp5wLMV=nn`C<k&x%`!o1%{uPwHPobP)c60ONk1R&p'
        b'2=qjn*Pqe-*wDiS!t3((RLSKeOF}_}G(MdSiHeOrw%dLt$nivo=2$2*F!|Pm%0|fZgfXUa<74#lTPY%=`i=4?z9rJfQX6R@3W8oH'
        b'#kDg*h^|9vty*S#sn<c18T}g{L&_SI62Z67x`(`4zPh-)HO!F@Vw1_;=*?PQ%6ULTE^S)#y4Il1wn#cH(yrGxc6yme0+mb~@UWo8'
        b'3a5O%ze50`_ao(soN^0%^6I+_X8J?~)jK2TNKSu`5W^Hl5|O;*C+zb$4t;YsGQ#fzniy~Zh0*^3OrH)-1Eu~y5h@!}$~%PgJWQ?%'
        b'V&YN60v|G%>6m2po=`4lEZ5G!oyR;6*oZJvT+`?uA+pdRmRj1Z#E~!ILJVwA<dGtPnYWQUM->3*$#2Y!2qc3d`4NJ=kAoruYQwlJ'
        b'o_`3t1rdReM>l_l4^4G%>kvBrA*7YKZUiG=n3dq!%!9vl!)BgkX&O)7L>2~y%aOa^Sv$RT>_GUntym}l81kZ-z2aH*%*_&X{eZCe'
        b'rQzy;^4b_M8O?kgy~<Fc7MG|4O4L-js#aamP{QX~=n7l8CPG`QuW*_9L<yfCd57i;YB$h&X`XsP#c-ZFE>E4b5GVP0G!`yY+wk%('
        b'ynIN=h!B^FZW05pVs1j*AuOSBHy}iyXg46UfFyl~e0xQ??^4VJvO$1+<DBW7^ch{Sy0cp;f1PaQ83tMTO`mH&mJR<{=C+Buek^0g'
        b'P%h>oY6bZj^ufzh0*BA_!3avQh%TQ-L`)MgLny4cR2D&l(fAz9Gs<MXa2JbAH<SVr=quC_@{v*QRX7`t9)lvtpn<p8@DM_Hkfq(M'
        b'*@{u!y8%^_R{mWW`D|noI)?!ICh{NmcZAP|Q)O4HWp!m1kyjp<i+7bF?yL|CKV`e08+?HzlD}nJdCE^&c@%rCw`{lv+T$bqjC*s+'
        b'hPSR@dN+E}Imt1RC@xCZf1l|_fp`&T*P-!>_IR%yDI0zdN(;K$%j`CS+p7hh_Y81v=>_|EK7kLMii)PF(qH+0)wrb{d`Bd;_}-zT'
        b'l#}3rPH+#~p94y11PUHHI^Fe`vX_0&xJii;!_iTBiQ{KX$i4eTMVCrtl;dX@GV_9^ioIo2tXZ+AECFU<K34_OR~pKoLMv^y{dXDd'
        b'mQw8|$873XHeF^dO3%=m_0?teQ_{q~G4#OAyC%<eWK!k4>-ov6JI8EA`J!oajIqq_mRb*(JUcK7e(!nHArWx#+-3*Uy>c*SV;Ra_'
        b'T&8g^h)y!0H3K;%51xp6)hQsLF&^Z-kSQvAnXID|R7eeXRDr4jiS;+HNQQtA$~%}m_%V75%y1J+zUifB=4)kCZfS<jtjH<To?1Yy'
        b'Gy%%JJY?2yf#P71KSM44>CkaL49fegSD&(FOwnLD&|m?gf#0ubphzimrIe9A#(N;z;t~I;G=i9=WnD|lR9YTrgj&Asr807xN<)&<'
        b'(Yo<LOt~H-=XAYTW_z*h%5)T7hjlF}1HS)H&T{8<y-?O>k8gyCgfh-EnN*c0d-^8){4!E(`;W3(!mQyNHeib1l!4M(>|G!&_4>Pm'
        b'M$$Y%V&Ygh&F2V8^MnQT7|j#iFZnSuq>L62I_(6_BNn95OCb@9iX|I4AEss=R!5_kt7A=O9=@+BVcxOtH9Wi^DO|%76zriiJZ!{D'
        b'+zBkZ7Fc$6h)O(a>JS<RVAlTmdpaEz><}2fV9_xX3@ga`n7f^7=z;VH8XlopibHuWTY7BuciuiR^D*SB+L}vQq+lgSmy$%m>F|a-'
        b'o6UT|2%m4V$lTMgvlgmmzYJuW+p74aiAbJ{)hy<RpMG)n?F9=y3EI3MeqYl)IZwolZ6^H&#S6u%{s~e-21VEHrXr+E#E1Oms(g56'
        b'AHozXGaaRvo186mo5cqEU0-h|t5ApdAzoode*plxvKdTb4umO=I^_4yt}iz`R^jNKUETF31Hi2t9R-;8jk$u*UKO7Q@)Xq&OF56Q'
        b'(I=yApKMm8@xe$@{uW~fH_MxTj&|{*JCXYmWjc<Cgx(!Fv6(6^rTIK)`Xaw+G@n@HH;-G7`e1XHYjZ~5Sceb>hcXjW{B84PGyLcp'
        b'`5k;TUjEK<xzj+k2U{HIMO)c<L6<YOn-asQTHJ!q3;G}CFPrUrL0x0xG;CiB34Hza+`)7wUtm~{htSpcL1-GT&(&ReWJtmXzGD@w'
        b'o9pvP3G*%@5J-~&c8NrH^Jm*zKo-xHx$Ak>yluJGQhCqAj8NqGQ%*n3$XKB}^}xv|Iz*25kTdp2_aSgakZ}qfKXG(p)q|W(;C21t'
        b'I6v3yN7VF8-XK6v)mg`qA5Zy5B<h`L4msOPF*`R++3tEQ(WxGOyx|?6H+eo_X^mZIrmvoqCH4jM9NoW|<beXG(ql~I2DHqIbE+eE'
        b'ZcmKc#h7VOW*wyLVghTI^__ta-ZG1+9q((Wxb;He_vl@Y;?A+o>OPZc?8FD+MnAzW3;J#ZJU{f~u7wQFh0G;>Vn7|Tl5%pIY3=UZ'
        b'+|qq=^r~A;EK&Ue7R?nJf;MJk<%1|w`4MhEo^@Ma^mBa)2~9*_yBX5^%FTVTuJ&fTLRwrr28L94@cdPA{(Yy+z0+W#cvw8SAO!S4'
        b'{*)l<9*P>`brY2blOM3F;-1MEguH#g7JS2xtZ<ASIr8M}1t|<h^mH1(S^Z^ZadCj-7Tcu0m?@tjAeSM3cb#L=C-XaF`_|%b3Zd5Z'
        b'qRrL5bsg<(b_rJJvcHUlSRx2gxaMtHk23=2Jle|h9}Mx3r|+W1q8i|yI;Jrd3n@sx&vp~Shb$>bKF{%QqFwFUv!Pe=CgF1us`=#Y'
        b';H&MZZ`$qkmpOx{7mvglcQMzS$Ykd2x>yRJMpE%zXE*I?+BA|%G^RqYpvMWlJWv9|hmriM|LwHUFo7(!Q9lv<-t`k-y*hUL_82-f'
        b't<__klU&Djl)>pI9+E7PbRv_{^FHb}yH?zqw~(j2#L068TTis=7V-^0qud%f0#_mzgQ!eXYlLFxlSVnATP?Dvi&Og`wyaxRA{P`V'
        b'q3^^r^h<^1cdJPf-6tMlA+uY~vwqkYmA)$pQMqr6xi85DecdDkSdhKFIXrOXycZJs+~!{1t~QF<TFjkW=TmM9M&m&aMV+Wsr#uS?'
        b'?o-({a^5bwFOfD^sH0*RP7{930weG`rZF2hM&MT-Z50l1?#Ji7@C*kP@xnC2w=9g`UwEMn9bd@&Qjd7S!!~7J)XPNza%u6(zKo19'
        b'v^v2{T$!Jd)YpaslBA?pw0Wm*`?dC=(dpQkPe*|v+D{9~X)T9WHB01UV`%WA^IVl5_H;RYu#jeFItEOD0V-2x2AOTe00~$e;KR@$'
        b'MJaLrX{QCAQMNVDG0JMR#O)**<nY;!NUjyNY7-N4%~~NB62}u-EiX?a)@TKWze5RfhVt($@=wIU9<gFx-2zF@uYOr4hDh&TyL=r+'
        b'`YK1+A<05=G7aih{u3a1F0mw9r7>$o+%Fo$t=iib8KCOZWHRM8YK3O4K-rCI^>dt<dc(6-3j*2m1;YLd7J#WVV$X3dkKy=K9w!fT'
        b'TQTfpsM%`jtUqAtrur^Z9fV=+uh+3wZXyMmAdxCa*eJ#lWBXwEz06O1DZgy3OlvjOAMK8?E!zYp;?IAA{&l5p0?jn~^tQy$DYSP&'
        b'I9C4}mS&UNDu(u&S}EoSl%JdiQn)#)If2{xzW=N90u75ck@X$ZdU?!sE~7Xt%A6xI^F;4R>^vb%tI$tY3kAYTn=J$&^$!Q1B_)U6'
        b'0(E-I-vcMG@32DdZ9iM+CS+iPu>8fZFf(UUWa`v+2-Me0bcmTxyoe#JCezdbn?NOr;72dwQ}g)T{5J2cIf`dC)i?Gc*OZJe8thp~'
        b'q+dNyf}GzWyei=8p!rzYsH`;%>8L+;;hTm8%n=0L93Ud6)$K4*W0o*_g($~T8)gpREty7H`ba;MYTM#RZ}L|4pr`vRl!+?+NRySM'
        b'`w2@tMj>_NYqbA>?s}sW=2je{pf;UkqF2%(RGM(76?7WMR$TZMOpc!G?7%%vF1<-8Jf-_b;fE%$dEL_65wbe^tXZZQEsY@R=-Ia^'
        b'Gy#D2GOy{b;!>$_YEHBLvvjc$=;lOt+rBKFMIx`gTq|r}l+Id!LhqrF<2#n*p%wU_S#uQH?nlP=nbMG0(2$UB&^_usQxR*p!N$b`'
        b'nS8wd`X_z8p!1HG1FrDhAUi)oCI;ze4MV<-VM4{3USv_F;tM79t6_TIz**n{q=Y)S+e(!VO!+5Pbe3}K$uxnJVq|L6?p`>x?y6`j'
        b'<x((;erkW%4no_UR*cz#8qjsH6zx#GiGVBYrESDu0;hZ`Y^B52Qa6n|{cyV<HVXOw%H`P)dF1Wmia(de>?*BycJL<4z6tSQ_n=Mo'
        b'8>~eVLZcq%AuC~C_jjO`JdcwSj}a&R2EJvd-it<iRDGr4arFIE-|&bzU?#VU9Y3<kd@MZmcLiBLG8G7Y7=fbi;%DDxHcy4t-tm4I'
        b'Z(5ttG8N2B-U$1V@uxA3RxUCXpUm6yG)3rP8}bn>`!q~c<nVq>F1n>*+><3}5AHDOGvCI<ASxv$f(3_m7I0dPsnob~jOF@oGEc-W'
        b'dB~v2TxK;MFN1;T%_lZz;=MewkgQ*3gN)vE=DR;~8@?U5^52vB)^YFx5Im5_$o`5h&B!Pv%R!}?gsM{W(-c~@!1KM=4m0z3y*!gC'
        b'05XS1sP4z*lahj<944xC<RGY1g!usL9-QcVbK8*E%oB{DRroLvBuF_w9F|OS=7YdK6%ACd%__A^h=M4o+YZ{~Cr!_QJPE@Ga148y'
        b'BqcQ;aXxMt|57^#{$(+OUgw4WYcQll_${YvP`gT@#i$WP3N0l4k_oO(JUmM<`EDT(p}(r>Hq3t@CL8sb<1X8T%O8!Kd4%bZx*(V|'
        b'ryyPmq3dFke`L+c*uZ0U>YPIKJau&9>X?6TgqbQmHYyhJJ5Q<Vr@$W8m7tYQFoF^_d|eVh^X5iSQtV2Mxmw~~>;!`gvfXlebItqO'
        b'-y5f~@)K#q4)jX`(vS3Q6>z@EKQG~==t6$=BbIwn)+;B^BdD#&3S!Qn9MPuLAZM5}8>1Jgqbvy)fTI#CNy2=Zns+V)K@|&NJl5ak'
        b'5(LH%cX4a2s#F2g#OG@Iu;dqc9o<>lnY$Xyt=r);{qc>RHR`B>x&p+jLI66%&p11lH$ct17|%rs(Bq68CnpO$vq5&;l6d2d-|g})'
        b'AtwtaBR+f@!SNBIB}~@VQssOcHK9qyG@~Z$vY4VRrpZP`?&6knRjJC!h?!3#rsT_0IF7g}I5qzlj`7Q>Hc!F<?4}~Ta2U*!jme8v'
        b'DNGxUPg;pyoN@k<d;dU3<9LCF7|`JNwR6MiB_F7WflR!>@4Owy3<p`ox{Yx%m1c4YGCc3O`+3B`61<><sGfxvn2$ur<n~8)1%Vz{'
        b'y}@EoNNHmgYd6X@KQo0$0uOLzu;RBH$pC~8ff>I|^fpn0aS=-62gP1oH3)evp#-BdcO{C^axoeryqH_@*J#4I65$$aZti4}a21X@'
        b'YS>1cpV%x-nYpOo%MjbLjfZa<s@Y{O(g(z8%0}+Jg4@+Xz#|p3ucX9`(t<#u`UHk0h3-FApd<!PA;d`^hZKi@nERAceBc;o(tb*5'
        b'aIx0<Ov-bY6KRv3;5q&bfO{qKGfz5rhJEb74OTbvi3S&huUK_|_1uC0B6&9^|5{n_>|u?JR}k>7hQP=j=xr+vHn0c_-@bx;YgIsQ'
        b'!Rj~dGM+U;ZMBvbsEFh@un&O7>#+hqB6%|wPNTQ3JTGFpmXLvqtlh;|R<cf9h;Bmia4#9ju%~1c*0J9CiUys0_COU{l;P-x=ix&1'
        b'j%$EW{*Aysz(Qq>dXXUkYgCBjJ-0OyJUoo3?qjtQ(Yl8jOZk1JGC(&&$2TQOi<795BVTo{L?>Fk=xZgs5(!~~n3dGq={Y&8o}Hz>'
        b'Q&OMA+@2i$c^Z6K7vShHu*n8=W(Oy`N#B}%!V*4qg<qKj5#cFB^+7h#)A#1ItHom-;#z(42K0^^wC`aQckz^moQ><7HlUZ|<d4K;'
        b'&7noaz&;jiokM>ks^4P4u6A45&Jxq8i1*1HLfF8XQ+Q8?u6<mBw1E;5FIeR_LK0_-SKls^-7GtML4E0hc{x@>VwK1=s~kM^!j~J4'
        b'm$WC9h_D&}J;WxPShp{6ViqBM13vgpz5so1fo~oe5>ocbNqfjisH3y96vU+M-I5Rs7>uCh)FcoC|6m7-+3>t&<XDOyA^an&c)vtW'
        b'|C2e4D58-Nw1lToleF4*L?%QMA5+qx$NO2&P|LbHc%GH4Fq_4kGQLNF$$Ku0NHFvknc^=c^3gAt{RjqnpBDHiJb)O`vCuchO&Lkj'
        b'<aI2lAf%F7%BN^`1}&w+C^}O}F8s{J(ch54CJWGGg}9jfDdjjJOl8w)U|ml>E6*A3l`M00@EotRy5PUlI3LDRA}!U8{15PO!5$*{'
        b'k1Xk&7eEMKV1@PQGBqyNSjD*+t5+Q(gwM0LSIRQ9rrZ>D;!=~H@87(^@q4yu!)ucIW_izNXj}}$L&w8tm?4(e@WK}n!bleI*BwOn'
        b'wL5qPGoJG}S^16=ZWkYE_B>@iOG+Hey!;z3$|HmqCV-46$X9AUrYHr!`ZS>7X=kfB38cdLiqw+m+|{>rvgj0b4xLVWg@*Cl;$O)O'
        b'6mjBdgvLz`-oL1D;{q7oy*y<Ko7_8r*$ID-mX${dBhr6KLvrkc2~6>y(2pI8g(Y?ZvmW3x38*uKofC@q61n|7W)TV|AD%$!nd22!'
        b'6(x|ribTj&G^v8(pyFfmj*bcsPLPB;xTN~=l&z$QLI8C=nBjNO6`Y?X&D7pE6Iw!ZlN8FQDB<E1l=q)9mEJ0kp-L2UO5%8AFwEU5'
        b'9xAHR;34gbppx6|GSvYrx}CCXG4zD+{ql#3fD&{p(HtkHt#i>vR_J<k$j4gBkR?=mK1qNcG2e3N!@ouCZbYwUH)dfl4I_P)D4DeY'
        b'ZB6f8hmPGGMPc*=Ln8{tz(5L`d_NfSI$GG|iOI8c>PH)B8!wK3D^_u8ovUYE*MkkV2OA>saenkUiu^sZZ5_8Ih8}<07L87&p*8Uz'
        b'P?=U<eG90%%nxYsDw6l~y%xtgtX|TZFi9T>j{vP&6PUL3oGn+Y^4bE#6+TJ!3YdRw;5JOmHhh24X#qOn!WdAUFx&B&iyOEyNRvlr'
        b'4$vNrZwJ8~MTT5>uxxmEgKKz$ZFqyz`iMFDr(d5PLnZ*&*U?Dpa@=R-?YKEgv_F-c)|km7Bb$-_s8Mrg;(uAIfifLv>wbx(zQ+=!'
        b'If&h|Fef)~JAa0)UcZsfP(GMmV6SeO7?O0q)EWx*J#*BX$5B3^yEGp6syueQ4R4ciuz6VW9rhP|JU_7VV8BFN-%Z9hgKGQ>0>8%D'
        b'@I5Opf^5S5VlYN!<V+6VU*$z~Rer}pFYM0=_YbV^4-b{oHliR_oK}~NVQD#t4rxW`lx|ujcYMZsPSN8*uF>i+yN%~Hx9w3pWCZ=b'
        b'm^+R6ZJt|v1?QGKg$@r}C8@vEsscksCmHV$agMB<3QRgoeJJSsxUWOldDLXM&JGq?1aWwRrB=|Yf<owV0Pj0K%CFE?RZVcfWZO4S'
        b'B%aCV4(4y1cvCXjr$DyL?EW*5<#IpZS2Q7)Kr@x46ZAoBUW<UXp@kIV-GOnI$=Sf2Va+>;F<D-wfx;Um*0k_J4gHCQQfnr3QEWz1'
        b'UrOu%8O%I-9S!#}uN@QTx15L|(1KnEkEA1Iw4PA5qaz|W#h?+i0^9}5pv><OleRr4?-7BNJI9`W7KG&QdI^yFH&}NVUv30F10Z<5'
        b'g^+*?L7EbUgj|RRp>J3KBrfIvq4y6Q{{tO`Cr^V;0BeD9A+*|-%F`!W!v=%x*2K0zay}D=TGXbL-+VIF-pO^7xf_P(ZXkWg%FT81'
        b'#?P`kn`JFcARkXp3psgq5UCQMPHVi#o#mP4Y<;G)9SP62X*T~2U0LhUX9d}U{<6_e8d}6m1thG^sAO|07hWKl3NA(&ni2S>CR_9C'
        b'yLOFDrnK5Ga>u69JH6p_6ezSkE}l#;<m@)ZSTRy<XtXe<p#{-N(iq3<i};+%mnVq1T}%dQUqWV0O!B%#e58@bYtcsD9X7@d5ifHQ'
        b'su9$f!qCibigWb=G2a)5KTimEBSoc<XZ)nN06|;J<ANJXUY`oT%p-kNEBUIG5^`4Odz3@Y#+-qwr<1eDWu(N5fYP7+A^?x^T?diB'
        b'or?6xSaRtqejqxf;kSw>hBS0ONs1=3ct3L6BK~X+EtH-I^LVTja=b8ETIlg*Q@$pWBe)|YdFy_fJTHRIuoRkeGoQ<iezssKk!;2a'
        b'41~~v6(|dDZ<J*oDNd+4Ymu3DnA|};dk|p`;`g=p<*q*X{|Ni`fF`c&;hD*kFxVtu<Yjj<2n5vK5Nvt0?m~(P+V%&i2ndn{5?+c('
        b'ZPhN_&4ex_h`WG&0M*?|EETC#LR*Vkb^}$47PjE_VO`xtcWJfuL9O*w>wNd#Nl<rx-}n8K%-qMhckbidbIv^vmc43ysbpUw!M;?I'
        b'ymex$qNQ)kvrqT2LE9v(1Ip+<TdjvOiF6Z|`(-eIl$<aTuSk9<Cs0ruC@jd$StTInZhaUhMLCbjP>;ezSv<LE5+`gS(l=t!R|#=4'
        b'7WapmY)1_lL?7c!A4@N=IE)nddnc4<Mu{ExRy(xOuRXTBZ>!?jr=gBRw4{7q|3PbCKSc%%2f_)u6b&e=-hfCES38{HE7u-vW37#T'
        b'B~TF}I%SLE*%z5-Yx-(IX4BRVH7p<jwOeYgwgt*+4tQ!hN?K~RfRC=32|67=<M5nNxK{ar&+It|zH($cmV5BQcE!Gqz;;MI+drwh'
        b'-m+C|-3o_z`zOZy8XB}rD`Fvgv5h7h$|O*`se%qm)4dlQ^*qt=J{R{tHL3Y<QEFE4tZd9Gi1pCwAropW)IE#opOwDFMAnZ~!TBEz'
        b'=={QSBX#&m?8=k)$_~%W51!GduRKW%KPdoPqcQ344SP6@^gDG*4p3~{DI`~k!K_=YZOgHFRiYMqs%<$Ql}t3ez_qme(6*dNZ{x7+'
        b'xSBpNX}SW)qvr{Xo2m?JU^nsw4Q*Tw0#YuD)4)#Wi7Ev7fg{bFF`|YP)uN4Iix%sS%M<eQbjS1h>J?TS<R#lQL_&q4HN3_h3hQ-f'
        b'z#5fJU%Z1Ff<qS}DUT+hx}zh)CYBAW1Y;RC716kRzK(?wYF)YvEP_E1n9qxM!q%8Zf-O(CrElRFaZTTgiq5vC4x37dP>j`D3WX!*'
        b't9U_?!w>0DwQ`$UygF13-*TN_56=O^WqnsMJcj@Sg^ejZA3%52eeY7ka|G5g+;fx~h0EbE*_bpj@;i?769atLw6jf$&HEzcIX}y<'
        b'q&6vmfi1F?va5N;1?ZQnR*GA<LeoQNvk!3N=}mQKYzX<a2lH~RyE>nfo5)4|d|uf34>x&uL<I#8qyFUf79Mp%q&A=#W*N{U*dGmi'
        b'PaJBjgnFHPQX))}4j)YL9EA<^mqWSvGmen{vAn*cioO9j{-+jV!(;f=IauK{e?AUjdEHH)j%i0;>yb?;t?TMt`8&~PEj_di>HoL{'
        b'qBen$Wf%0llWOfzw8T;~uPA1^6-PRndM0`lQyq$)4yS8VXD6L6%v~uO76@9qH+k5gzSD}%bK|n9PTaY7lmD3K^?KGtwe(P}TdF{F'
        b'7X!d!+#fbg@fU^xy1${(c*-^^Cza4!tIg@1wWrem!L>Rz_4{Fm))6CTxUkn<nV9O4Ypu<j`nnaJJ+PW=sCg6lfTu$aT8G~v^Js%w'
        b'8#Z}7LH=XxW!&?p`l$|TDjuggDD`UC{AroCgBsej2_#JLgD-14iw>&oeDgY|R|yd+Dt7N~b7HQOa(3eCM2F{*q?TQKTiVnu>{b7x'
        b'eLXhY=&#Q7U>yoT8@F^)P0eUz#cuAdtmXYwt+sTgSuwLqanhdL0SZpQlag7zDJ$!0r`;7S1f*Y{pe;j|Db2|v*xy}%67LW)!1~#)'
        b'3F{X2?cuS+EJuBFVi@E%TT?fI&1DH+=3KF9;wawa=&@(<%Ry>;FQX6o3_xnK?vzb^{OC$|FKhb@eqG*YSYQe^=FH+(*k{m|Cws}J'
        b'CPx7jf#peAwlu4U%9dB@-pd0IV2h&a$w>$uFpD->z35<M2Cea*ZF23K@h)<yCtksV6DXi1o*ED6XRW;Yagwy_TkfvSlD4H(n~>V)'
        b'P(%e1BMY#&&`rtq<_dToNMCviDS%2_LpSjft0XB>Uv3p`vNk*fvocw`Ld&m;O!RJJDPDO|SAptgHr8MF;!ptRM)f^#5;ZRiuJh>v'
        b'FMM4&remQFYP%-E59TFlplB)XM)lo3#p8UP@k$>oC^L1QukLqYZD$bRkUl;qM90GYHc*h@&o|`!vf8_dq<lNwngki&4ytE+74xcI'
        b'hKx*d-tn=b@v$pfO%;~FhvQCFBk5$Klo!4w@k8CxHn;7>otBm@*J2*v`*(8oTalj6Xf-75;h3L4Sv_>J8sO1>c8-gUGAjf;jn0fz'
        b'ld=IR8Qj-Y4^~^7QxM%Qj}j>M1<z>@Yl-)?ISFlNJ&aFB`Zaj<7@5P>&{WN?@#@99oWxf|MxbQ@#Ty3R;?9PKLuJ4IN~n0&TfJZU'
        b'RczfYNX?V41A6!dmmA8V0zI%mYFG7sq3X;}<g1yX84-zs%-B?CbuW=2OcJJFf#Z?=$7+oz*CcZ8sgC?a{DjORQ%t^6J@g6~`~}We'
        b's+l6li&4W=Kg+>O4X2n*rpAs;zF0l93lxcgUag_*qDyRx1uR9cpm9k+yS~%j_?9?wuQ*0Df5!Zhc&RM6^CzYPN-lYuCjVZ4rlES4'
        b'msv{K1OYTbTI~vGQZRZQ>`THLvy1r+ETa?5p(sPb5xnk-?|u|;EZeHRD))fyJpWAf=$z)qdEU<%y5Stoy5ubFN$x*^Gc~YaZs;95'
        b'9;-nyqXGX~S>0>{?CT1qvYO{f1&9~P%Gv_2qQ->>jx(jz2#wpNr&!!-iyZ6T?O+VPHYMevi4HAT8&)P2%6^!2Fb6*IbC_4%8d!-8'
        b'03MgM@N|ciSzX=sDuxp4zVaoik8f;!s2a9IkU#SxV*<UlW>%9=w%FyZ8P&c-jUSU<ZKdUmsM1PPOd8CH@k0<<FFaJr*;DR)_d{nk'
        b'eGsF1<fM+`F_j-$-p+@r!HMZ|TD=s!v{hG)O1tB#Cs$O!xOl&)?z>xKK<Zpn%^!h>VKW1=2_7NJP^}HW_INoDgcpY*t6}Wx9X{m9'
        b'Bg^^K=jM1B6sbGB+8J6s3qb0vE@gtNox#<<R_rpjx`M3p>DD>}tKGZHeM+||iFu&9|KL9n2p?#^u}$T^cc-M<EvcSW)fHF!!0`<T'
        b's$nW|U#g$;NcrFc_tH3i&i&=y%drZu04td5NSyIA^5^H~3_dW-N?_U*nD#YsjvyZ(>j0w&)4oRK9w6s`4blb!VA92nckeaGC(q4+'
        b'rO7aua{(3pIiKVOa1N#Y^4?;neK5fb50?2GOlm#0(Rpek>MpM-@9=9qzR~$V<@YDOv(cGeb$?RCMrZGTRD5uw^Y^|aejI#v8@0p2'
        b'VfJ=Eiwrpz!cfcP{3Ig0c@QwoT_128iN&(9g0VH>^*T$!{Fyd!7&Np?rdkqrX<N4J&P+kruz9pA8rv^Ca0b?kjKTC`p^m+j5F}Q+'
        b'HjV(q3ceot0Qxh)XShx*3Ku54)e9qO09IQ3CAU}x<1541hYJ#(BTS?6I)btQvc_uhP;0bf^HkG9*8)J=;)W4w5bx=Z9OiNhgj(tc'
        b't^H}ruGQML{%UPvD)_I|wF#hH*y@1y@2*`e=vtza*?88h+J}MK&^?1B@@JTCK>{hOEHRZP%=%^6NYq9pXoyVpvvf=<&F+qkiiz8n'
        b'N)oz}@EDvHi!$)&1tA)7^gD!@!sw_3d#aW8JX>39Ng#>zaM-(H7KX5pL=Hf)%q>xdx_JxPjC|M!V;O-dR8VfM(0ROkd2*^oz!YtC'
        b'uiw~Y+p)FrsFW$(2uT0NWJwLJrKqc45nXR^`?I$z&K_%z+wP|cT-g!3RfBiLh0!tij(G7|=rH~9jbJj=IL%@$)~jR)K(IRrO}5qM'
        b'0fcsnreyc;x)m^*Z4dXgOw}YL1FpP^MK6{2&Y3>IwJWGJPi#kr0-Vfe{@g7Z^#^2mk9NOkclQMQ!r6j}Vb9E1Nw4&?&6kWf88eC9'
        b'U@jU@Z(ezB<QuN;O8R;JY$Jn6QhTi4<JnR~<en8%$Le$I#CB!tsWRG0G$!Q_h`tt{BYOqYpTXhi6e5p9!d`*-5_rGei5yMJx~8B*'
        b'qLVg3Sl-;-qppYqXu>gdPPm9X@@7*{*Iw>yr#>P<e~i+XB<La%65b}%b2dUfQYQh<*u}DR-p<FxZeiA!c?~F!V3Fk#5*m?~OPXb~'
        b'@s0VzVC>2yv2lpl7=GDFY-Bp%scHtrIw!deLqBa;1S9MEXs<V^TqQnvZNt#54gGAi^V$YxCoH}@5J0v_ntLX{-!Sz3hDAr=NdXV@'
        b'KS6&Rj0x@_UMJUx<v0n|F=1CL=Q3hlKX7a%mE*)!JpxiP_TC^=?!Czs2^wUeFqL)HrpDS>JnQB9mOKx(Mxk9(0zHsV|DM|;8#@AZ'
        b'Lb|STbw5C*JoX5cb)4!IcPPwPz-$)Ky?*9Da9QylpDyd8exx)yM!}42faHfpL)6^>`^5SOkylQ4QGZ%DN)ITz33ENMKZn<`j@jUj'
        b'*)UEpzko!7%}Gcq!<i@^fSqXT<<QyG!dneVZ7k-6<qX^44ukd7_tXoXt>?nL^{D@>7qGz{0P6+9dP|{Ig`_f8&2AurH3X!(?apo@'
        b'{7M2H3ei=M`jri_@l){%+KC~vC4OGjH{q>u`x(kES6{bK9dfG!VYf5s-y=Et)hhSZD$oX!9_nBV+PJ0-$UNkq7D#e^Q|0X_nTh(@'
        b'E8u%dmt)K)mRb7{2<v>6`#gm8#XYdL^03AbtiR8~a{L#p_wI-F*DCj4A*_$?fmO=GI*eeA`e4-^o`og%!s@#p*3l~WQ3z}39$48t'
        b'tk)2%w`XB(|1Vg3?t{goZV10=m-Z5n&V^zmyE8gQ1qbvMGGJny>UUzy{wl9zey9_T{RbYqe5l>xnH~EN(yyYif3eE_BJ9^I_w;Ka'
        b'-!Cib*B^ZSYI9=u4H%%Ww%-4Zwko#`!m`i8%8Lu;VQqvZ!!sJ&Xr{c%g&?&{eRL3darJUud4iOwoo(|C?!LhQZ5G_$rn$;(hHX~e'
        b')Bhi<P@7q(|HZSg5Fc}2|CiqnE2qkx17YRe1M4CWYbk>D_$;i0zx~gCEx8}oud3X?g0PlVAxkIrbuF7B%v~b9R+5taw<>x#yjR3%'
        b'5YTZ5)Glp1@LRi7t6dPQK?b)i@e1g_AQ5ptN>Di5GHc}w?LfS|i!-vy9a#mK1!m!Fr{hwOR`nl5LC_z7mEzv6vd3EzCDzLV>rSB~'
        b'zE{XdVftu%w_uRy+AiRG&BIevxfKZByec1}2mnWv`qe6E&sHbkZ-)4?;wrZoej{0R7pHVqh2OGE+h<qif%@oJNZ&bP_?mIo%y8uL'
        b'wRU;jRkN0sTWx4P=BHohqGKW5=SbQqXt>HbFQbALfH-n~X=Y~&Ry54&kp8v`?gKkOqHqq{Z(u}93)RY7yg;f^BX2!p2BQelt(04Q'
        b')2Cy1y3&2R5`N=9;86j?_Q1YB1O`k}qKoY1dWG{!;>{;Gby*desUh^o!tKOVnxZ8_z9QoQVhe)2ODG5-IP+^9vhl;fu`LD<Z~}ws'
        b'-qiABT~Na{ey%cz92(DBLa74h#;vL{uBy^5ksHi%Lp+uHec(8tKn6w3;YzR7)I$J+R8EyBnk?nwv*O9js-es(=ZdO+=St>dcz8i0'
        b'{#Q8F3anQU`D=U|-7AoML5wVfN+nLV(#=+m1H=M>ZKKJ@SyuRdBhe6r?e1Z8RsHXU+oe-S!J0c_M{+!`pe}gc7esm_)|?DT%ER0?'
        b'U9UiOUD`FsZPSCNFQkztxPctd+9_@u_*0chBTsX61Dm6&tPS$5?aIxym8}m!Tw|B;>OBsqL2DOpez2;>F5hf5*YG5*I4u5ARaqc0'
        b'GR(oj>uTe~e}iMEx^<oLuWCbm>i~VLJKD+juCGJh@F@oxewh=W;mn6QG4hi)eT?HB=5>9<rJv)VUE*avPAyo8s(xWoT-?pda4Foq'
        b'4m?J!H{v-)A+yp9RR+JSwCnC}2pzoiO@kTktCcQVARnT-eo5GzqOk&dc5^UzSUhW|?#!%oXI6qW|38)Y?CaalUwiD~>~oc1BZHl)'
        b'gP@qy%GL{&5LXzGxC!725x^B%AL`MVz1!JqPzhn{D&0B=JF(KYpO!Gcs6;5I9SK_eBqdSdgpa8tHP(7LVn26pBLlsV{k&)QhAV&p'
        b'P5*(b`<Ir-P<{=w>p!^C9gNohgRmj}L5@w+rU2};T5#<#9UzaQBEqBM>8L>eu0KGZJ53zyr}=l#qu(y5-`n*($NK^6+Q~s%bv>Z-'
        b'yldQvSGsZd4U)>cIP~R8ghRh7h2!#Lh41{0`LFZ$U#0iq&~GZ--&6otS1azqdY*^%8G?1u2dnP0|2i`#?t?W!E0XEB-=e{c&=AeT'
        b'WI(qGX}tYZ&fE8c_BNZNloAUqRd22AMu8NaPgO?gejsHQ{S5OI{2=wFN~*^Oc_Jvs*#!F{Vh*8}f>*{vdI<0_m6cv`l7_GZLAuCB'
        b'>#X&Nk2UE)`TeEdvl(6^(7L)CTI8!{)}QW#O`)}0TUS+1*%elY)uzFA2X~j({m4urz7KiGkG#R_U><smXwYK0SNu0WQAs-mc8N+V'
        b'Q)gBJ^bg70mQrL2>0Vyh9^4JLRkFi28Z-f&F!iO$H|r~rl);mxs5vT6@d{g^F}Kw6@OtBkQUh<&4U_s~m((3gIVvZE_;US~OOiX<'
        b'P6R=TZztkd>jVJbWo0eNy34^Q`lSw-dkL@lRRzXWmCou580*Unymh)1hPp>*+D(4{#u%Ry<n9f`=B8k2&bZLZ6m@D$cCw2Mi%uqL'
        b'-l4{Y=Oj!RoQ-jr=?v!#tR$6WeA$tWadRujCFOzLg2adlMUwi1xc&G>JSmlq!g7bnIHJ-OfsLI!v3YtEKDznc(8#Cp{Q_MCX3y3R'
        b'JZ+6vH0>oHOi0GbIpe~bPpQ5?TNwhj!Jedappjb@2}k@isVgmIZEw&lu48fI4;A{e-10;4D$)|TmK67jslD|8{AYOTr3$bxgp3w`'
        b'?&i-cMmKMhY?DMO=ajV(;uNT~Hu5WsW}!^q6uqQwlxhhAIFy$~*~*sm3WtpnhJuwxH}|W>+J8YWf21t(JiwSRhA$R3Qfg7caH&fr'
        b'&>`YqIpzbnMdC&)w8^%Slbj_YBW|R^6oKW6@o58|y8@#Rg7q?O#$6>C_+~h?$DH81J<e3{>Fi!Bse<1wCIgNfVvbdyu?20xSW=`i'
        b'D*nOfz+jRl1EZD)O&+coI$YsAT+#15%EUu%P8$JDx28Yfc&IEG%@qm&n0*yMT|Nu-AP+U&&0!?n;NcdF)BnQbjB9BXq=-~eDBwu$'
        b'agnjJ0xo5->V{DLQU&rP%A6~KD_LAOG7#J@oqAm{Rj)YGlWgznf%g+Vc62w;E=@@ZGIYpO&~esQ4vt2qt%A2AA1m>iO5J0>4tQe`'
        b'wHh`0w&>bpdB!@}ZiZO(mN0c2YFEho1=iDudxdsoI{}(XwtF`a&pgD{lxpwF0ci~uH)hfLD8hsPOPgaRfX5KERZC;J^EfbaIkcc$'
        b'nL(SYFfwqbB&)vuS{lAo0w_PNc1!N}w{;_2EgO)KFcP=AqBa6M+c>nog4{udGDQ{0A&w64swZy^O3Y`8ep+bwgc=w13cEglrg#N6'
        b'Q{JM?-*GUsIQ(9(qpOrHxo?TD)t6_dpm7$d+C}O|E0C<4sYl~1BA5L?$GKOKbr0#Dm_4^N%RA-*=3(!M*OdHk^eX6sm@-3axZH=O'
        b'hw7ni=H>@sH}WJZkt92`0%24W8g<FkF2y!NqfG9YvH^Sw&=<M|YHCD%sH+7>)<l|u@=ZAEj7D1bme*$ndQD8-SOSiBZ&D&N2lY<G'
        b'WT4)O@0lATwpms|s@5hDCKe;-U8~1QNsWbqJ$*?~%i>houG?bu_vOf)zyS@4uHMD{B>q}_PBIQiw+b9Aw_6ZH!>s9c4nn`@+l`1W'
        b'(aY^havmwPF5i`6-I7S>wm$$yVdPP)T(74wuoSMP6V`1M8GJ1gC#BY{l%xzg_jWEUcP}g-7cz0Mfx7GLJ}sc>a!>l(P1|xbwGJE*'
        b'y)lZ&<rwopxkh?+c<AGDatAc8_z0F~M#}d~ZD5^LN(YJQ!^CME8i|pzt{D#gng79!i{V4$`y31r3m)1ywW54#wW5H|BaFS}b^TPN'
        b'ysS-WyjiySU8riH5!dh|3iVFtNX*z(-p>*ST5c4V05aOZ?+H<4CZ~R<d{og-U}Qk@QLvu`<+Ivl7#xrhuMd`M^-E1Gp2K217Wisf'
        b'-Eq%Ii@JW#{UrKYbWS`jtotz^jx_5XX;Gw&yKj#fv0SC_+GD@WwwHtIu1HKJ6Oc;iT|WjlFAuki25^nk9y~6*cQ@PM<tbR!6BA3O'
        b'Uq<Fk_w3p5402(kGAeoiQpaw*G|CoA+M^Q_`(0R+?tyE1Ik^(h4U7D*(S+NtWU>GJnSRz9mGgtUqU2D{x9;ytqD+_Q;hW)7(w`cr'
        b'2gf{l+WkjUqw=HZM78^TNmSbhfMY+@cAOk=Unpr*4!SRu(8E_rDK)SQkhI~!ZZ{~rFFH|556{?~Si{#`xCXS{sN6*le{FjeOTWa0'
        b'UvxiI+NiWeCq5b8?w%}Z1P9GIE;=zPyqte)_>6npzp<YHlyvwu&^?ee@)76$0JL<m;on^NsQbxsnD!y(K5YVD+Az+M{?L`?qC|2B'
        b'tbYPP(~v7I!^Fr4M=rbu{*Q5sf*1LN%ydA?gU<aU+;31y9j<TqGq))3ahM@~mvet^0nLsa<`$Ln&5GaQ+#i?OhCd_ytcQ0syy+d|'
        b'7@G@wSxH4FJsmEMstvwoTWFgd-V8XrQZT%X+XPpR4Gk}|r{tRHTSi`zev2dDWL_vqP@a#D4<vViF-lN=!Zejc$4@XXmNZ=9$iFdq'
        b'Q-X4sX)8(4y$kZA`VTSdO!V-#q=2g5CH|7b!f(LOS7XtMN#P~T^8nZj(eaA#$4E_rvgvVYbo}qYNRRxJ3$JH>Q<8v&7jz?`AKu+F'
        b'SUEjBo&FWKD6vubM08@<qL4*W=pp(eE?gRYm=K@h9?c;2T3da?huor7k4s_wagO<u1=c^wEh>SaK-wtB{JxAH{tV0(snI%ijl9Q&'
        b'+esTV8i!+aF*<R6cn7nm?B)K2WC!!_vX_++;oDzUJ{YA7W8`J&B5YAU^G}c(5S=t<Q4-@{7M(;eXUgE1EvjHX1v%e~f4C3UCtg^8'
        b'yARfF3lHnBcVS((Kv*Yyutx5IwdkqnH|3MZ%Z84ZIggixhcSy01Jq)Im!ZRDb;xJs*G5R7{G}{*RgMVDeGvs^yaI(g<+A6XQsD`X'
        b'eGRcSl3rr^2bi%<wo!)skN<<KyTNvAYxuh*aco4+aXd$lG22YMzl@KKckg!izPQSUUMq9D%ECWjWT-D2QD6R4hRCv$usj&WSi4S&'
        b'`NxA}R+oY0)<g5fOMH)tK#$BGzF7m`tO(>H_fL7CTgcS$BaZDtJr*;$-k!W^^zjmlejR;u&ZM<$=yzpKYZ-G9u`7?mV%g7?p)+p3'
        b'5uKBfUqGN4vZXR83^#uWcriqD^X{Kelxm7+rv=QTCjRj1FwWlNG6^tEy#c}`m>19>SC;7o>a%I76=fMg&=<yaK*;D>+&s<cA5$|6'
        b'P5k+6H~RdV9kLM(KZl%zcrnIAAb5FYUJl~7XsmL}ob9DhIu(R8pS0F^+-uWTuH{pl|5FB1v`M@I0!-9tw5==4p!5pq8sOfWe*UF('
        b'S=qe>y(T!b^?p_MpDFuHKIH~2bBiB2X06f7P27X4!P#-m7I-Z}?ku*ri!I>9G+U5FMGOkTHNvd3OueA!w6{y0*DZAeR)>6FyVCiX'
        b'#Vt17cge|LKz?h1;-_q*?>g?Q_-p#N$%TNx`uiPd%_%QCCupJvXh?H0k0S{n(J;*&(zlRdaOgj~6DKX3fIR1b4wXStLga^V2#fqT'
        b'cZwDc)5HMLt(=$?MqcIiGr6*#Cn`+@rcK!rr6L;M#&V9`UMfDcj9`-?L8w}_N=J~SB*~dW1lXNq;2w!}SAEt~^)=h6+<7@Go+cez'
        b'_Y)(_aC?r!Z6h>}*0B-0+xqY>)hbM<_RB5FVtU}PZJx4#6(eCJ@TK+N783HQx)?3%<<+!_dda_tkxs1RJo6UpbNl(YJ`1BN1q=o>'
        b'Ta3}VKebrV)^Js5`4s-<dG^))0h9*qPlbYuRPV(w|Kc98++XiLFz&xt{xd~mnuQJe^DLTw3G=A|TE)I&X+NJN%N>boBdCj}(b|sl'
        b'Cnhf#NoKQ=cQGYl{))=IZrQPAYOCT|==yX(VuzZShvVRL+~f&^wOlcARBot3%84+wJPxq3@C6F7$|cy_itIg>y63WT<$b)a5KPaL'
        b'kWq$vU+X^M&9QvB>G$Uz^5ymuF({?aAe^u$Cf3LeX4JBz{ru?U#i0XXIma|pYZTks3JQ>JqWia&nwl4CwkrB8a<2xZXvb<$!kZs1'
        b'@uk)hu_(oM@GmtrLUyaddbbA3@OXrMb&BDG|MZN=Yj}Mrk){=8F~2rYHNw8F_&s&>$0!y3fZc8UXNfg_SleNnni3j1T<mXfROS4x'
        b'l9m@!TjD)apUZ2$0Sojh)EG;H0<TLVZ3nfY2PvU30dO+FE@LX;Txgj2Gdb*SI|EgF=W2gfzf_u@!6E%7umqXsN}P{atULlhO8~7)'
        b'xwFeKyE^$qXFOa-N!bvkWV1Ye;a{AKE&oybzIxG?|4jLVaTa#mw}ufja`Y!Mt}6i_!&}fLfnh?Q6C+FifP;H;oI6FRhLy68^TWn~'
        b'&xV+f489eoGoT%_aLWW(a7fjTUvT@OVr93w{~!idxU~`uF-$5~JEfMps|_qY)*`pA!LxGjE}wa`Yi%BSon34E>+D+d<{r8~x51Y?'
        b'I*C@E$MbJYm4a<>4qY~HxaB!6H}GqLZ|d|AEDL8bPtmtgG5Ig^#K&?2uWQMtB3LGZhi)(kJr)HEmhrt^Fvc3)Tg<*B7ZHpaW(~p='
        b'3*I+dR-%&q17#S~A!Csb*Hs=4mL0(4S@FYpwO|6ke-1&d=+LgQWwaUAxB%mqwI($y-ZK-gm|25^Ri}Lj-IE}plO%h<tWAS{1bM+z'
        b'k|ezt`MQf?MhqNazmu4e^<0jV$Y(|hIq#iwisx$9#8r~Gwjv=q{9#h1H9;OV`lW@;%jO-ONF>dRqon{)i}j(Ic12T%r$h06jD*=^'
        b'{!d==?%nPh^Z$Og3+RWRU|&>6L~*}2LkB>6DdyE;c-Ut6s<b-H;EbW{9wcwjNV}2qR07ciUJ*ONFy_{`ijnLg^{(_Ym1!xSm42fB'
        b'Ol~s|Z8JN!nIElUj>97!$_{B_gvJg<K!=1gHoy!SYt2yPXtCO&kaNFaaa^?-oL<a>a6Ko}h{pIegj_CeS0#!k9AHq4OffW{iZ__$'
        b'tyb8Ryr)`bXZI;c%9J33R(*+-At9WlfVgVj%aq^kA!CNm4Y%QdczxDhqie54Y?{$4lGCyuH-j~>Vojn*5Bl_`FfJ4JDOtzdDE2uK'
        b'%!N-GqP!rDaAKLFAPts>t|>Lb>~D&*cxF_{d{xX_un3xuF&U_JAupd`mccjiZ4L^uq3=}&gZ`lQ$Wq$tuSMWHWmX4ewQk967ha>&'
        b'XWA4_jal1a1xuo()7tIV<|Gbuq7Z*Uj%-J2S8*6a!yd+Jx|OF>N3*xXAiF}tA*yGuc_p?-wiqe(wB6->NeMZ3qa?))+bWWPJufj6'
        b'=})2Q*^K3_Ha=j^IeusDAtJpR%l0=<m=u+3x<xa!3Udb6Dl#WG!r{+v7pY>T3}M!8wN{ohZtu{DnFrug_K&6T=zF?bGDwUIru*@3'
        b'&}7$}xJI%q%?^kUL}dL83r)cyom#In{$~@hiXI*5KNYV?POMp1|D34xLMc+1)o#VX4A*#dX4@8svcD+Row$?mcBuI?Zs?uTa44NZ'
        b'Lh=2g+@5Q7S4JMiusE$Dp#$IJ-$NteIIl@6E=D37ZLx^GM`j~!X@NdxVt7(fJyELdP*CymmR(5715-7){2}~q`E5&BbhCoI`Nl~1'
        b'0DixwZ5LAgrMBa(L#21SE6o$`5g_+`S#7%v`HHsJxt6W+EU&A+Z9zqXnw(wFiBR2)Qh?IrTXA32l!*E#cpt+#y<81IOSC-2cb&7Q'
        b'80jhYiW8K6jC(zNfeZT$_yiU0A^s72eFy9$u0_;bqc_gLJBid6OW}Z|=@!5us=Y#WYw1KH_+BfMGP}P22*KEeq%uQlLk^eP7KB4}'
        b'ZrbU+J1Grk9`g1;(ClJb*U!q?ncuJH_ZB_7x8i<NilEwIPHJ5#EyTWZF?Ddl`q@%2ch4ejWjp$Px^%H@zjUkzl>ha5FP{Y}^a{dY'
        b'ND1Z{)RJ=cZb@BHsv)ej*Z&+?+snQ>HCbLdR9@;VFYRa3nb#0QVS%u-9xK_8k3;`vgE+Gc0$M?*#CvkT|H;eStOq>Dm<D3Zc4-SM'
        b'O6U}|v@VMd`P#0TZO=qwgF=IGS+BUO6DOsXP-29_!q$)>)&a_O@=n&_dbWL6%Q|`EiyIBEQIRj>`&Rk&ip?+LFPDhM3ZUR9D)a`e'
        b'#3UE4kfT<c+|sR>Of4NsEp_TacYow*P0|i>a-}~-o8~r_oYW=@DYcM__W;r*Z&&&^peHGPTYANjy+U$sR)H2AT;fYykrcTbfqg{x'
        b'HQ#ej$aX@7Gxs+oE|z2#!4cRgQ++8U#|DMW!|Ty&yVM<7N>OPuF1)Wp?*3>!+X09wA+}cmUcvKZNNI<3G~j$;@gDN5gH)2T6jwdV'
        b'ZW&AVxatoSbZ8s_NVGQK*T;(X#h>ezvaf5uXcG0gmqj1_@Cm>67-$^qSkR$K=XrNB6kgN!I2pgvS)Ot>P2@`(!ZKU+d$D}yc6Z7u'
        b'`SKTuk<T$wL<Sj_)#tD?DJfgl3W(h26LXwc)+%}PGSw#uFS!!zt*Q*n?o>$=_La<6y^5z^DcO9bBqiOt{GB<e-<53sj(;Xb{)Xw<'
        b'JIm{(<bp8~`EPJ&TL>aO6|4I<`NMK$aNS4YBKUWVe0sT3QTJ93JAb*-FXtdvr6=D>SzGV!1mh`XPD6q2{%qA5rSohFyelh$o>49f'
        b'Ql1dPm<GLgW@;^ahdB$AlQwUy7n5Jq)KiYln~#@}kGD&5_xnYOi1Za0`9h{KV>9#5B9{|mUzIzU=lonoav-%=GW`jd!n4UWY}(8b'
        b'JoRWvH=fcX2YktX{0V$mE$mlI>V5)@;U_TI?U1TF&=rJ{8I4UuLmJi{L<)10<-L-~O}L$De3fWeiP?>fJw!t$7Pi&${+}$Owazz6'
        b'Xs3vA!47t3Ge^9ejWmmobFL6<o8S9Qc~kooY<Ju~CDHI8mXTTmruc>0D3PdU^Rlfk{&_TYU~{kEIZ?-?`LA62r0V1?yPq|C8R)vG'
        b'>r>G6%`cVYp7aOQsl(fZ6E*?;olbLh1gt%>JLIfva%aiV&Jw4sq@Uf#9DyhHfUM;x-Zv2Uj<U78Aotdt_L%fHISc_l&OHalB&#NE'
        b'=4IUZOvyH!MG?)m<Ij1=B<o|US7JWSsm^?7m!$ul3rp)RNPm~Zz-Tvk;PuCJ5w2H@m&Xz#?{Y4qxJWW`gzJ@b72;rkVu^-#xDmA1'
        b'GntX=T;sn8aXc2@#5@i^K^6Lacr)qGl))E!Yeljnv^>b}tSE5AQid&d_sla2Qz+(GaZcuX17{IWQ};!UMQ$p>Oki%7gLn7plFx!n'
        b'tFdum7Q4m#l+d2)%qf{FS5)?ps@fO8hr>H9i*p}ncL7E&@@%DQS7UY84P{!uiB-s6It94dtm7~e2eS;_S!DN$G6_vkMs`e4<Vo(G'
        b'5(yaRU%?z_LJ6}FcGRQ}Rz->I*$y#Dh#R?DR$5ztsb0f|)&7HG(2MCx;maifU=PkkdoT`G2A{(|gF9nO%7y%QR0tbB;;_22o~?4w'
        b'p*{;GKFfiY7Q-1$hepaodJWRmB?BrD`7s`VV&%T)i;JOB&e74BD*|I#k@m7cyHuDE8swf=LJd>XKgY;Gl3*itQPB82PFjLai=PU4'
        b'sS61^G(eD<wlEA(q3_yV3vn2f%CBU|uf%!P)bHBKEQYIQR7v{T3-;}<R#k`{`HUEyVFVd!4<`Mro%Jo&E$swY*a=_a?@GJ<NPpJ3'
        b'Y+M$(P6*2QwdG-UskKEkwO`TtwW+7W>ReWL5zr@AJJSu-r5%2tN1u9o^lcG3?b1Ku9AW9x+#Z>#{ARB-eF`0UANu@Tcg=9Ku?b9c'
        b'hEINm7LWR@$t&-A55kN)gFL1Sn7>0xdGb>e89W-$wix%E^t_)8PMMV3ww6~sDPt~chbQHdP1~%P`TqFK4JyUq(*98~_1JN(UD5d`'
        b'>+@9H36tl&<7CkFB%Bmp6f`w|d8z67(Lg<mzx+#(a?;-P{3U@SaDTwz`OLB+{%c&Y2O2?QAeyJ?A2{Za3DFoxR>vq{G3H&^G3G53'
        b'Bpu41lXZ)k0hqG&h`%cet9gfF-bMv_O?5xU+PkF=oEe5w(z?$yD2c5A#d~4C@ih|}5Q}(daonq>@c`t+C{qyUG7a+2`GPps6dT_y'
        b'VBR#K7)TIcL^nYa%o_$2B!LX*mLffh*A2Wp5zx-WQi2Q`deL-FK>p|&l25M@_X-&&%xCN-^3f*Sem;N|Ui4o{x8c__^``HhGr=_H'
        b'?@UQ}EEoR!bAsX5u>K)A^JpRRLojdBY8tYdoK{mm`xMg(X`iLS^a~uelC}h1<>%JsB(BlHyqMVL6j)-R$7$qO)O?xat>LkI%2nS}'
        b'Za!ab`r^IisLKLsvCzeackP60C48)ZIGb4xYlWXQ@8Ftk>S7ab@k#KpXZX{H(6J?h1i7JC7)CRXz~TvQ-^}{xTV+B%)Y>w5xiK6$'
        b'Qe+9FHVQ0C=v*4fjQd~3$XF%_K8_Vc1=0R#OGS`jO!sDHbx}-!2?cw)-E|fQSO9#E_*+DOI5G876DiXWjNXJi4v69w6#`-z3gDx|'
        b'm_bP3(5xmpR57{4G_(YaXQp$BiFp(;NTJNbuu|M@14$&c#xP9032|_)A&QBEkMKc@9$rgf-*gQ{nI<o+WB1y4QTVuwd}5G*Wi-CR'
        b'(Y*NC{2j+o@R3cXVDf{${Q2;~IoC84WCHLeKSaP-9vB$KCt#VmzQRHLgPd6cSH&RiV%fya%mXkrx|5s~nT9a%Jx@a?+r2m=L+yPj'
        b'u(7Q5h|Ahz)4oShrzl<$&VCs<8*7innCnJfPaWQ&UWL!L;U5kq&WATf0DV#I^)1wvu~Tg)e>jvRb)Ec{)zqtMA5b4OwEotJ6n-!y'
        b'xx`v^M*1L>CAIrmZCci)ZE4dEbs5xO!cwP6%1+f?vG!{xcq1QjXpaF(BuVQI%DoX5agb0BjUu4<GnFu96tX-g;LmA)c33+xCZ9E`'
        b'mA24Y_Vs(Lf9fv#>~R>mvGuP;lz1Pf72Y|k3p;9TjW4`Udt80Y*t&HcGL7<y8+bdZ_tyFBrXmf{M@Q@1M)FJMEhBV5bI(2riCo7G'
        b'vmw32qdS=A5ZUiGK6(oYQNnl6+CcRh?=yJ0P4^OomwD-}dY>`;rnh~*J!Y@*zJAl?Sl23m*Fl{hnNn0|_kY!CH;R$n9eE^j%^mg2'
        b'#-SID<a}}=z_l-VZxYZgM_jA17jVa?SRBw4b%^d?Ixc`WP|S93xgFmBXJ+qt`YsFl28GVw8K-xGbrT%<ILBTVu)V_Y=0|_cq`+d~'
        b'O<kG1k3BF5L(dr7rS{+swIdF&7GwZ?A;We!J8+v3XKG>j9ZqH)-}vyp3DO_D=6jQ?y#KkV7dVsc{jc!;XU*P&ori%=;><>!08`cD'
        b'sij68i{&i9QVqr=UDjjuNi-RssZUZS>YL-cYo`Q&(}Go1J)*ePM%PeU1~`56MupC(jLSCiFIbX-dB})%TN?9(?_r6z<zIOJmwW$z'
        b'4*v(BYv@d0pRl;cjNr^pHzFBKZm0-Znn2ex2naLZh&+uztQLlZ#Yx7YK;z_x1?<}{w#&x+$-v{2rO-Ns2|^7Cm?-bR0{%~5;xckn'
        b'fZDE|5@L^sfqtwo@Yxb?v7dSW#i+>z@b_%2MoAV#DaB-E6pfQB7z(C#E%EtlpKpwtZ%pV9;&nyUVa6sJ;dq-Kd={VBu58Q)R13tT'
        b'!#5iEI9L4lM1F&r8!_`ExO$F}Ca~r!W@AY63Pyk~B#3p9f5!l^)wKri8Wrr8O^S^}Vq?FPa*B;SpQ08ST{MhwLdS~7l;-b+T|-3k'
        b'nMuqzblcGH{G}K<;*5M$;QYzJ5UATv3Z~Nq>RX1m9}OxQK6%qHbOn@5Z}^h)_V0E=|5cjB%<UWurh+05(Wyvx35PB`-=#?+23Ir1'
        b'y?Bg*Ic(skbJF`i0RPp~1{;g>BM|vWn3&@*^(PQ*=@6VY6!^%7OI>WK)w;#&>5p%M!1*kYPWjTAk0H>Je|XQTMUO*Xjj1hw@`1~O'
        b'tRi9RxM9kysC*u5^>^Qcht`5nOM%ETmjEpTzIs9E*wdCu5$pyA4Sc5QP|LG(nNbLJZ769-vx3i!5u*IA_o15@^cDQsock8E+Wj-4'
        b'O!(j3@K+^+m(cS=nLb16xngUNoGC8IJ_{bGloi(H4?#7M)L$90e`Vlb8`N0pK7+N%)3^jOW~s@B6+Pf*-&>p9E(18~LPG)d83KC!'
        b'RO+7$fW|2?@VCV-@4xA8hca<8EmJ`XGgDJvGU!q%y^)Z+;Zdy$6iz=3P?Vt;Ps)zjJUzsr_zcV+U|r}-??bL(3@Ym?LsRPw%bN&5'
        b'{x(1xFzA6u5o)RYqj-v&{sjvA!pl|+HYt{S8V=c@po_wsR)aYp)EgW4Vayk=Ag<a#inj^KxzszJC&Ycrb`3&#&Ge64>K5=Rk+RU}'
        b'dD3pdpt!8lZ~lxc0v{Bq3b^T;T(8h94Q=4#Sn-!WygbNVZWv}oFbL0ye2@sE>2&z+?%gJX(`4X>V^-hVV4yAux&)yTlgPQ=5Ge?q'
        b'2Of$HT|{WK$=|uo(0G9Wzg>7}f=TKuFhEE5Sm<)_oClvHvCy@ke6FF33qklgQOT?_)D3HCd0dX6$<`R3?94WRZPE2p2o%YOIRD2m'
        b'eH+CfBfx*$;|8c_|07Ir(RkO7A-#g>TPT|b|2|)3X$B;D%p;x<Xd@^Si$g`=24|LCZpk1<!mw+3bEAUeqBKv2#arIH;LI>|T|;%T'
        b'sDX7+qXvupbM+&J)JF^`5Sud@{$~gqFwFT2L*!M^FYx1BY%qTx(ktxxKE%1u&~+sw{VTBVVhyRW-dZtyEf{7Gb4DAG7fO%_!{A|R'
        b'jlrpb`8179e**!28^S~ykgfF><sxT<q3i1qCv8ZFexz{Rtp;;sfOBMkbL4!`K<O#-W$^8hUxhfs4f1TN>&uYZA%jx|7RU6ZkjgGs'
        b'EY>f>RO|4_OCio6L)XQS%2&HX!JkuUnEoPUrNwgSvz+5{{W1C07e|>uw8@T$bKeuubWl_dF)|Nx3JjE65IG&<Bn(~u25p(aqtFof'
        b'?+}pF^{)`P>i!kt#0^xxpz8wohUp6-POg}GQ!srVei3-PT}-_tn4W@f=R;t83QM3Az_*x)kuQ9_pN$S$^la<Z;>KjZ*6)j_x)nVg'
        b'?S35*t=|=Q#E&I1GsTX_G|HF~-oGuVn->dB)yZH-AoFE0DRV@C#QpJ~+ZC-Bi>EY-*ba?fOhi;L6}2s9{*0wu3Q7vZaLg^+#+iM^'
        b'NJFy$#(YqpE8ZU%^B8iTtp0m(%wy2@&4}5RWVi#j>j!a%!ma~2)1i)uV?HYO(HA@|6*p1b2ZhDp7zezgb`{l4G_RPFVeGQ{uz0}n'
        b')PJK|fSD&kc)q6y#XgF7SbeORSL&Ptr?K@f#eMaPPCMyOHa*kyvkd9k(usJ*5ooQKoYYI?3l<9*K|X3X?C456pmMl8UOqH(%NM`O'
        b'3-=8#+#9e!>+Ao2xL@bp3-{80z`Yjni`0%{uf@{8U?%fIabLWmDW3GRvC?Pk0K@ES!#e~kq3P0@JfGeQDXzN>$TKnXhhjc_(C^{@'
        b'bK*FAu|~lBH4kwrJN;GtWV`Yr@$ykZoPfR4A^PG7F|q{PW@?V^uHC=2yLP*5^K-@B`mLQXc<)&_0_42(Z@6yV=41Ic=$dEcH3unG'
        b'kHkehFt4(7YOjY3+82*MA#NG)j6ZNrl5*7Jz&q5J6jzJ_UK(!4+tn8pH{xE4eK`47WXSb+e2=(k>$BUFi0w*5O`_YbM18MVlf#st'
        b'u0yAFp#SUP%g8^uTfZcOzlg_oil5#7?6&mpxYXb0W$(<(B=VIF-*L_FJ9CQN*~Q~x{?Y-|%R$#y?{eef-Z_JQ=|0(bmkgU0!H_^L'
        b'JnmJmD0Vpor-`q=9@?Gf&M0<f6rVC;)D`Lit70s9h_CkVCeBv6oOlEDmF!F{?()NOd+vDs#4{fj@xB{)a}N}A=<*$PVsRp2S89_z'
        b'q%t8Hy5hDT^-v2v%ti>3-RoiEipdZ#W~5&q?QxZ3&Yu^z&>p%RpY9Kxjf)do3`QoF9}Pf%YrIb+xsZvv=XpV~_htj0O%cVZ>f#}~'
        b'*d0;)wSWwG^hk_wdIEGdS0>C>6$1)i#LS1~y9G=*e>-xZ$1cjYtV29Vw;;=FZ-`WwLh9bm^6E5&Opo6o1xZ4myy#bXstAlBiycI!'
        b'(wjD*v=d}F7M6nTcGlfO_pjkCJ=%#^6h}I!9{E&<0)-U~_g)&SSLRW78*AUDe#rN}jf6~940IQ8!tRwxeZM|Q>6Ian!QnT%y@s|4'
        b'F;Hv7RvF0LUaNaA99_&o93I$uaXoZf@npW2<$;{6J3J45ORNfdS_sYS^BI2HDpfFa28vlgv;inS1C9{)C+oe+Pa&{XUz>h>o5=r)'
        b'#0wJ|?}_rX_rkpHjX@QId1wU{Yo%%2H@97y*|b@@!W`{Q17D$~K@Q>l_CxCd$M&~EhmwD{1SV++@-f8FX?+acXNBs&u0@lUL3#Dg'
        b'Gx%5a$pXqdi5c@}a`ytVR~?v-rhvNF*tD+SHyzAKq5A0m1(+}&q>NnVy!}w3u!-74iaA{9b2+C2#a>@ad3Dn=yeZf6W>es}<<@g{'
        b'W!(kjz|Y%mIeMYr;O>8SVcu@?@9LXteecZfLUrr^rJp<Resuc3_<3k2oVyEs&Ly0t_5bNl0_4ANH-Fvws6fJL%fF`-z!z5tz|tDY'
        b'Ipkupu%E@5dHn8&C6IGCy!FZT&cr;h^cMMfS03I*popq?ON)@|PypC>GlVF^X<rNS<oD(Az#due{B6PA;)D;5p#%S~vhNh$EyyRS'
        b'Gm2oFb~)97-&a=sL?N=gO6L8<My%&;sOj~+gk1`q4X8BOUHwrTEdeJR45Jn-XF?%5*Y?P@JsvWUji~qGgSqQtd@{i&2(@y3B0&;k'
        b'g84IiY~`*WIaMdt{S*@btM|}}^)U9y!weQahJr9KkF16FuA=oB!ZCniP*mU>oGMn>y=4$*a9&K_j(6G}M7zSS1pmr*wViIUKjom?'
        b'<Lo++pleUH>%qUiJ=>lG{&U)mb`$tFWjqgqmw~pZehLt9T{k#dP59=#TQ{I*R<C7`dfpk3PhKn<x>)4AShOgNNrl`N^EsT}{k2}d'
        b'y61{C#2Baw1|(O5^E7{VZS%AJ!$HhBSW;u-_q-94Z>FXfVV)iZ>-5M&vFXK_JdR?|P<sT61!Pd&jZc>(k-{DEi-n)Qux3K9h=uAI'
        b'KQ7TON%ereALo$=VkB9FZzMn6y{xQ_7>UOwPZkZ06!o*)8x(-3E>{ldE4%i+A|Ehy)B9fW%h%`SIOxhX`8i=}^spR;=ExI7iSRJw'
        b'g-|{+%?-pv`Im=%{zboH^39^5HvyzF=Nm<g1b*h!4#g4slwI-N!J?G|6AvqH9j)AZBW$Wi(bIJ^^oIYy!ke<gu{Zn%LT)DCI{IB#'
        b'(cu;DuA-(t94@d)6{P>+%6EcQho7y4)D0<4eyE~;<D9Uuwi9yk1lLwZ43`N`m0_3WMPA}A&O0p`O=ypX&QRl;ipE8D!BXjg;K>(?'
        b'hW-FL^qY}09Om9o=s7@vO6JqtaJ1lTY*_s8*n;R?pHJ>68fpNgn$jn^?z%zYi3G+D$9$t~G(pw$Q_3+I?S<Kv3(X=&Zj-_h3D#Y|'
        b'a+RtH>whnpc^Vcy8^mlV%9B<|^Bdr>EQo&L?ED$KAYb6v<<mnTRiuc@t%vqcPs_Bq^|^CpDd6{QzvU5-#ob(3lqboZD|YJ(7p-8d'
        b'g{Xa1rFf7a$C!NBwz{||>EX<D+9Jxah_!Edpzvl5T1C&~H>i#X`$vM993;rdFG9LQ8(^(Oz+5LaR7e(!n6g~7^U5Du{u+_+T1@#e'
        b'@Lv|8&ih^ZdFa0tkT%=kUV+pG?G&QGUr@*D3Riap-ebeNbz)rLauV<MGy0-debGhfIX_a`_(ze;DH`#E64-qUBd^5ZGd<RQuZMf='
        b'il&|2nyDs54_pGypBJsPH}#mmMVDe>b})^IR7dMSu88?X5oPzN7Zq9S)fys<j@5X5&^(97tW`%9l@lI|!l3rZmDnEK9Z>|RFFz&_'
        b'evz9lVyL1$vOc>9)D6p+IHve<5w#!{o_MIdI<#mht|5lUZfKM{_QnX*^NL~u9gS^e5=H<4Oa>K^%}CItfHai7v3)DpO8#|Y%O6oy'
        b'R%q7t`c;(Wm96c}X<rNDa4%5LpUG2p6OXK656C@h<of}oxUWkwDJ&Wif>mU43X7NwNZ2+W4LMDJ8tXra6%E}1IK8yt2DcVaNyY16'
        b'+|8pqXz>@^fGjW69$TJF`Z=O25)Mo9=M`N3Nw870)4yYR`|{;Ue&HfAr0nfg4Rf&5Kl`-1VDy164qPTfzUT$?9jSW18z;qv4tYz<'
        b'malGp(YxgR?zp}|Pv6@f>jux^(9dMyqOwRLeS*u2b`be=UP6U3U+0ii%mW))b@+<wq&)ouhrO?nPgHw$2DC5V!G(2nEQii)K>e>t'
        b'z%f8N_EaGmI!G{g;C|kxR7`$YIP_s*zjKT8!$O|dQI8k8SRuTX{edqNFnO|YXatmb2I^j8>h}u=@m?5dY^3lm?(auIWFiGTy$tZY'
        b'r?AyiNUi`x0$tepm%_GkjCo@XM3sYu`=x*kmPKBly;GdC&MV^p^v-;&uK)&p?0bYteX}t42aMUXrghI6hp?>_N62_ug_Q^83CkXt'
        b'e&;1(ZSp@2Ybe#SJ6&_Ji$OPphHBif4rf0}ow=4e@i8@Xjhflx>B~)>`aG3Xy}T5fr%fIA7{)xGhl_H*x}`dN>u`{}vv9w#JIwC?'
        b'Nsp+r-NfRJNwD0>lP5=BdKYi9k#nOHaZ<Ec+WPA?%(H8H;*%e82s?t(rC5jmiLlsBWYG182|bG?|8gSAle~lsihdX;g<0{Qlz0zR'
        b'kDLy`MkY9{rQAc#FH0m&v6!d8GqJ|=`CL)%4>wgKH!J+}!#dkQJ$Tc3GJdgN@{-wDys29XA!qj#x?0^-Xp6wwBH$U_JP`Rc$E;n`'
        b'n!Cm!=m-S7-G)MRx6G*4B`U42*tEZh(<WK1JNg0j@p3!?<|kGYyAVteU@FMqeer~i#rpa^fZdoD%=+kVR!-mGX8j47<vbtFtVOM_'
        b'F4PF@fw8e<;65Er3Yv}{iRbI3W)*_=SEAd;C&43sCxS?aBq@_#=;Oyz(_y((_^wVXj7#H-YEZ~;0e?A(%9%s&ER`+xXOarNJkZ01'
        b'cX=SNXZK5Ef@gK4{Gk}^GW3RoPk+yKsqU~V;M!qg3lY;&<PYcr>Uqy(WFZ;exCAH3tX&>Yhi5cEGvC?_NR!4#!M6aQJ>6Owz9xg$'
        b'zJ4q86@CR?212_08gDP2!^#ts^IS9$c_BFKI5j9_UW6;UIa#9=-}J^XW#on3(&irC^*i%WzVDkD8BDLN`;qy@Y?@kBXeXLAaJ<P-'
        b'Mg!CL6S-gB;lt?i-`DjMcUA_-2lEpET~8Nb`|+-uTsJ-&m(BUZx~`w@iA5H7WgRt4bpwPqeU&4HyJO)sLD#9^ZoxP)DD3*4gOJS`'
        b'kjCjUz)LzW9IzXg5{qSLzl{8W>q>{Nq0E`s+1PObxsVKvd;zDOqTCfw=ska?S75#gT2zJJ;iE|o#|pvfGCOeqZN$ghIzL?3b!)a?'
        b'LzqTSidCm16+`_jcUW;4zcM7hFr+;ve!RJtFu#fw$#R=S?qlo1PfowDdP1g>iSlLnq2XlzQ1Ff(#s%?uPTIU2T%MB_oP#gUNej)v'
        b'7v-dd<OMd1GUw(6Rs`h>^8}fJW1>t!Mnn#-3`@(5$QUX}%N!cHz-g37p#kBKht))eo|KqaRwb0z8kgj-+!eO(0y~kf$j3vu&~MI3'
        b'9*2>_dWF-SSgy>!ZAflotxb-8wy#&Zhzvcd5ik|2;f<+m5$PJLVJz@v5$I`+Ye>tOd~aHKwOZ_Zle>npn03ClELbuRz74aKx9Dp4'
        b'dJ31f;eq6xcdv}k+0pMB3T`tdoiZj~FeWp%V1AoA>6AM0f;#zZtc?i%v^~H@gzig{*ocrGdt*$5MmaLWWdx1DSQhk<yz<lq{LNw9'
        b'-H-SEB-(Kf+SI&;(ds2OyuXR2jZ4HsoHw??fl#}wJ#=?)NAT_#ho7DHw>#+Re$@z|y*r5XTbx5FzQvby4JS_D=4e``suk*nZ|ftl'
        b'nI(!9k4-F50Bi@jYMu5mYPr&1f9!zkSlV<p)C{Kfdel#@V_m6Kk4@cE09btb-~sULI(fTiZ`T_t-x}$s3D>YZ<s(Y_9u;{7D+24W'
        b'xquYt%pvn<^v4rXBv!CIO~=#7`e*8eF=Eq*FmahGUP=-%Lu3HWaxsb+@5&;>2Lr&u{|z9!a-S8s7lV~$cB#OsJwsN=DrQ%fKU`TR'
        b'{X7${u&5rg;hI6hrVj>l?+gY5Y>iBXN+OX^UDV>V(F#L3WilyDxKcAzNsBLViGdCOgbw3A<uHAuf<AaBg_i4CJcXu=53Z)o3OX`a'
        b'Zw`T`y|1hWi@-orv^hAdi%LpO%1$zN{S|DG=1%Z^(BJ+D3|BBD2f5Q9b1t<|)ijeR%Lv^KR`u?nBw?b_KOR)+P^I7CGE>1WPRdS)'
        b'NWx_fY4FM<T(ltTV+s(sgMvsSeitX)lWs1#C%sz-H8rNq_}$nSyHs9$kY!y0Z~!EhKc)bUIF{J0>)Lov-Tx&&a`ip=;DlE?XlAk?'
        b'N#`KO9%JU_-=!6LiO8M4cH&MJ&=FX!j&L6@aIu<5yJ~j<Gg1%}>X606#w5qAh$)DvjCnSuDW-G3K*ReZ(dc*AcGGs5U4zV+nTO!k'
        b'XkGz!`AyCj8>3v%D=3ee5`%3DKI=C3oGdp~>^=b6D4%9j8)5to)k)!Y+4j)wE4CMGuiXCZ_NMKf+k3Wux&2mcrM$K>Bq{be8Nl*@'
        b'FNJ;`KjC)Db|1<u5GLj{3n~JW#H1iem8h@C8530K6HQ_9Nyxg^L`zf+w-a6pHXNc{!{L$72kWA+UU6a|DTc8%E^}CU6vUB+*C?A2'
        b'n?4DH0@tbRxOm2k?;#s-Y8BL(VC7Fhneo2FCsEMt85ljhQx8ZlK@1*w860i5E4%STS>i4LcmQY5rj8R}hnr`>nmT*3{dqgy?B|F9'
        b'z0`CBCvI^(KPGT&vA+;zcf2rvrW;o^aiD4-sM^5mHG3m|e#t!{%PuQWtq|uaN%8JT`$Nmy{Y=Z0gQAtLuI<5jkzmc`EWqqRDznfr'
        b'S5+>|m*$yzh5l>uO_6^FIJ0Y$Dx>z@SM!9RD>;$GlnBnx_$qWgefCQ*B7?%|+F*^aSEx}=5y-)VL!bUNm!AWEu#5%iGhC4nDJa8r'
        b'BAC8_CDKK*1Mej&!%x^F8j}`;X<{NC(I8JWfD6&<v8H%hKw1kFSvgdGyw`t^TL<RZYA#W+$rPOE&O4EtgKae4EKLe_2*A<|v=d3n'
        b'F=-NEr>$!gU{L537+jswMC8YZ(J>L?uaRwwaQY0!C|3_3#H~GYJ8@v!X$|T3^8E0r!-^vVv_F}kBL^Po8%W*vituEA?olkPW8^w#'
        b'4;KHx&HDb;(U>Y8hx$<Z2;5v53=YpC)lwlsr<l){#alLmsAW0TF(D}}Ur;3Nm6Bm~KQ*c%rrH&qFAV#U3A_DIWs*hyV@+Xpu+q1N'
        b'|Iq8NisYcfZp^d*&piT-afFej0DVQSRXrhAMgAzh!7Uc1`+Vcn-O%YVy&lie6SaDQgLdc~dPk1K<ft7K?^cnwUBgo5{nbcLWz)}t'
        b'Q1w!upJ!4~ccbo75*W558f<BOn?A^K!Df0uXOg>y(;^Fkb*3QS-e1`t-t0QaF`wl7d>%8HT~~K&U;EO!OC7piJUr<chsd_V&vg>F'
        b'9lQfJf?eN>I}|n|$d)Pv#LoWBE;?uc?C?ba_PlW%?(Rw$i3h^kf5A2!Tz8YSJ!2DeNLSj${5`4tLL2+sxS;M<V^TP(+%D_?Af?Z)'
        b'Xs=ilU_EM`^1BB{KRsudCE$9`4bDAzr~Qikg2fMaTxnBMVfL_&wj9cF!E2ul`hCW~{pDoRHY#r}*XVh-jOst;d;Lze>zF<H7C&K<'
        b'{;uCg(EiY_oJ83Go%j^kVM}G+mI3yvyWuj)9Tyx|Y$gF1x9M{nT<q{J>q_0tUcZF)h{Ovy>~FH-OFFKs$jBKEPIxPH90%O2$h<Ci'
        b'tiX<2G@{Hah~-WL2LXxPgQBx@XhAOlNIuhW@bC}?y=a*8f&o?4Bg$Z4__f8@I9i2WtAlf6{d)1P9;{Z4>xa|8#@`y61h(t+r^tZ?'
        b'fRYxhS5p3I`W#BHREL3ob?z+@8B~5H;U(yEBzZ~3g@m`D;S=1xy+ZRxoE|4u?DF595FG;>m-LD|hRj*P?L%KZYiBGPi4B0W+j1zI'
        b'QtiJr3_PhDu5y+j1@De&dTFpK^j49q0bobK9JQQ)@gzZVYB0p->`BUdvHnPK`Z*LymVfX1ic`g2Pydcfx*$G>Y=X7gE$zA_Mu!_n'
        b'uy-n)Nv$TlbgA^z3Hih$^({N<D~7D~R7%R0v%yC`o7ho*PC8~UciP1!_PNGGBID2V8-9j$Um3l?CO+k2f5RRq*+1zzi1!@Z8SsCo'
        b'd-u4eu55Aq<Rm!>$*Cm>kyqQCBY{A%g<vI6Z6RVH6g5N$=+rwT%0sF%4rA+M=u8r92#76)D&W{QiADmIQKMC~G83XrmEv5qQ>V2$'
        b'Lv68YZR@qxTC3)}_6Z<ur;oXx-@Tvv`zJYPpS{;!uf6tK`}yfT-gPaSPg*|a$5~BXZhLRtmRE0V=;eRPJ<jQ7mG=jF*~eKRPS>Hp'
        b'3_-`VJ!BLq&}?pjIKKUZsuPuaoH2EX`%YhE!|vh7B9{ry<hQXZ5|f$hrg0!_8B!5;h8%5#Lsz*sW1a-o{^&4f_rtjW_%JtbD|Vx4'
        b'YwRSCHP|gVslRtPA@U@3Z_@%N56|rC+-)^E?SYO+u9Jt=Z$7!@5%Si${oqSLM$=PTXhHA(m+s&<)(wav_m*hqkv|XgJ9+H-%^d}F'
        b'!b_=^d$EFb0AT-%X&xTC<BuDxeftrt`|3Aa{vJ+OnV6EsO`%=w0~u8x=!mbZ4*gJR2H$cL8JCV1-;+5q&_W6%hqAI2%a^Z!_E4i|'
        b'EgALnxmn&7DZ5s5<7Pc69S#gE=;;H}{}x<RO|kOiwR=*ghLXH>X{300y(Gm_XG~cE4Pa#pUwH)2npU@R;(biRR)AGdq#fs;ejVD@'
        b'>`}&XAckUtG4k~l^|FC(mn?F&Kv#XoKt)u<S5#fCAaJ?iUIR4n3WHV>lV-60zOv;+mAv-jm13Nz!AJs?B)Yl7aj0N)ObrxFe{{(?'
        b'&<@49^nEySKgLwQim@wcqE+eSY+qkW=IcW|Y)co(CVq)wI^9hJv>2#?vYZdZRHSd}RDB*$^!1#JXJ^W(2wz`lH#Z}D`2I+pAfo5o'
        b'ad1tf6X5xl;v6^-=M>o$lX-GzD`|4AL=J%9pYs1RfEnlsa{KR7rY(}|Bh5PlaywcGUzvszsTf0VH`f&vsXKiy;5<-5ifeDE60wR&'
        b'Oyes5b3iA!4n`7iWtvrac%<&;wHoRkh(V;)SjQw0(*|D;=r(_`o=u7^(HK_a%Q?=5xTKrsst@R*ul5Rj=w<kMaHE{8R8kBc@u6q~'
        b'OTM06{r2B`WW9Vqqnm5iN1xP34TnaWspykbl&+s}QW5b<xL<`qkA)`hQ|ct?`vuGQGwpY80E(ws1_D?GANN0x$dc>BeXLZuJ>X%b'
        b'$n~s@pz>%=_9>9wM7#Q+eF1RYr6CU$UjHbrGNENmy8`0V|ICoj7FeDQV4y}7p|y4CAk{Si#nl@7v+4VB)ylvKqolk@UH)xGE8;*L'
        b'BW@2nQg`q}1I0xPu1m2F@dU<Hb_H|`KrqDT0r2?6VlLtd>g~#(3F!KVoGcUwxIUk><6ul(bxUiH^e!80`lxaYvB3sxSa6+TLvRy;'
        b'D<G_>PV-+3#8@p?1GP8(Cjt!rw+1X50?<#Q^OR@uvi6Edj?xeco$3L4A*=Sf(mwH-wH(8&keK2;@NDy@Cf@`7A_u%GlC5i;Ag8c+'
        b'HttWvc7IVKhn~fWN#Bi_ArR-^qnRZ!oW?<OA-JkZ!cID|ngsT7_QAcNw$BQhZjv0e9DI^f5es?9nq$~{_9}h_kGCo^o|kMs%BdI6'
        b'tc5J-vh2S_DCD(AawqcBr&cR>-pFnFHPCY;uu$M<oYz&dcpi716<xcwN)gW^-m)@IE%cl9n_m6Re`=I}!&ipmmNNkY%$S_wg*qhC'
        b'X9FD*dGeiCGFYk$0R>BGznvjhh%%IN7C(LO{c>fv<y@flquhxbE7&*$S+&s8E$;+?Ni6@{fkI!2>SSP=1IxSW_;X1-XIfrbJSR~}'
        b'->bDhoBJB-sh~3g_Z`fx>*GnfYF3pgK0dbUYVM{`;5!T4OAw^^^ev`0T|Ap0t_DJ(_u?RvJ4v_Z&e0EhS<b^b<s|`K*X_{VXnLxA'
        b'bwGFNmVt$v?Z3~js8sBW$*J6Xq?dD?ndJG$B;=h-R|dq@cR<3Vz;c1{5qj{Z-vQ8%CZSEMBfg$O>u4$2u}C2|@4V8MRv$%qX!cvq'
        b';SVM;TJq0HJvM*@3Tz_<U>a-)M<zkM;P%M<cpqTmMF~)?(!iT<c6}XqtEQVL{W_pGmek%XnRf3LmuNxt;C4}2mv^X3^hDS0WhKM='
        b'BGwCbBt6kMUmz@hiNDFh>JBmMMK*otus&d;LWLE!V?}041Yy5{Cd>vxtmB&fw`?-(N`q)~+hBvJ+3H0bW-TxATgB1NV^?g)b_4;G'
        b'&kI07fDt?>w#@C-YfB*FFY7YvyLDw<p@yA1%7PKU+qE;I${-fUE+`@iv>lGZ+y)egR(B2mXF#`x?>2zxDeE#ys{&2^J%(;x_3Pz-'
        b'on#RKTpNv<DN?*Ty17#VZ82E4t9+#H%Lm=r9X$zFgPZONskX*+T^6?C2l(xg5DA5}g+Uw|(h$~38~jBvIsTzQTNFAxu_2}*q&@Ng'
        b'A0aNMaorwFZU`B<dGNj~PMQVvl>ahd&zCga{2;01L{iD_q>|~$CK?U>DY8q$ka#-#YQOl_z!rJWaUtr3o(T+eRrSePVby6FeU|Hi'
        b'c=m$|yw>7liPC}c6wExCUD?J_O!VIjoMTP&utKle11I|+N^q?UK<@>4pA%0cs?titXm4g|SnYZ1Bb99tVDRUI4f+xtpYHneB>3Y='
        b'4^0BaISr+*^@KtBzXs58adur@WrUy*4B3Lp2;2hkCb|z+mvlAgVjV>4#&h*dl4-j+I^Pw?=Q>MY02_~r&z_A4F++7YIx`k<Jsp6E'
        b'-?Be|IiVfC7ASbGBo?>)El>)C0ae7w0K)NLX@viq0EiE-eqHqf(+-Z~XfUySE?6zv!QFDxAdph;>CQZ}+plxlL(8oZvmu?;w5FFk'
        b'{LP&ygnD%Uy~HE&**Pep@S)+FbsnER)btnh=<!98O{PP-(KrLmY5DA|+MA~R!JM(A={5B9sE3R-dB){KbIH3jcgG}B59oI9*P$8c'
        b'5Hu=!CX<Xd9iGQ*6w-C_2i7<zV=fXK9YcitJ9W&?F3ViBCL5=A=w$c+v{{pBZV;#y&yD<CMiV3Jv~&|$C${POw&@%$oyT5h+M{K5'
        b'Ds4GurQLV~d-!IcX^l0yN#PC)u99y+xS>-`Q61y(MB87VWa<=<Z|t~KxE|0zJ6IN@G{-s}8QCUi%CLr*kFpwYwV(kahm7#{IMXlC'
        b'caj^l@d*Dv=td4s(4jA=KfW5+BG|n~*Op`zcC<yb3r$s;;EL~pxg+a_)(d-N9e=#hE`!j6xff^Gs}fTU;%ZZpTQHD>cxx5ZhjH9V'
        b'AbWT8$ew9Xw95f9Zc9INkxqq<84b7`O`;1dcW9Wmfqe1^<HHG0{89&gk<j!XI_5CN+59utcC?WFrUwub;x)H3q7~dk!4&po!{xmh'
        b'Nu69Ym)XW?4NJ<4gP<ZKoa8|84!xK{mfLb8QAY4UIx^bwML-b;+2fdCShwi5EH1b0eYzY&lPeD~yk_P^S&nQSiJKx(<@(2Uc|<}u'
        b'?k_~^x3iha$@}J>>sxiQuNI;ZRPwnZMx%5K!fL1oQk5F&@5Pzva{U8ID;IKBw(vm9RcJAMGPq*SzEacsbI{aBlFlYdmPoE8v?B+O'
        b'lIfV|lW1VL6e^OTipZGh0#mt$fiAB8X2SzI4{JeN$bsl~fsL9(#<pkLsL1ww8|xSCNjB=f=4Os9UrL79@?{$gMa*f(WQg4<J#+K&'
        b'dp4yMjdm_}`oc|v2;wcye9uB$epoUaCr$-;)m$%gH;~<tt@<K>HNEfP>THzQ-X7`*({!}^$SBKafwsNvp2WTAd~OV#EBJ=uwQjCy'
        b'2#I7N+wx5SI!Yk#CNhb!Wd9!Ya(-@*HJ5J92RHD3)1!!0j*G=6U-9Vt2fBRXv*NzbiXER9d+gPw&kB)Al@DwM{XaIUbJ=H$wP-Zn'
        b'w1+Xc@-s8xd3W$xJo9#jQn4pP4$h?&FNx%|O>Aw8wuYgn$*panZdxq3?KvE7n!+eg{w*f&XUsiPM~ki8rgzOdS&g<ciH&tl7f@xx'
        b'{|tz`?pT-()@ctnnUTQgYII6tMs#8(i6`c(lgh6_*TAe(9kC-X&%N6|5lx4R`wkU54i<YHsip&nCYf^7<^-eH;jhrZ?`i4n06NdZ'
        b'^!(hBBM%_YS?(G9#Gi`${#5Mf1OP`(od|$iX?Ec0nfEVfF*`V|nc^O~8>eyU!94?4j|+P_rftQ{4tQp_9ra?d*+Izggw3BH=a^nD'
        b'9=YiW*+$M;F2Zk9abJ6}!v^3lnl>QtN0ngE)2B~d(BcH}(}hO?eE(t7hT?H{b);;4abHuhqYlb`V>16p**}acdz=F_tuF5SL$PB;'
        b'vBx>Vv;q}uV+v+S^6Q{reMV%Kaqk&fig7O*O?D#!5AHFo7=^;{_EX+*28W8`zF!qP3;^mOlOBOu#ehmr3xZ02@Ha)pR(uuD=^$3N'
        b'-S3v4CA!iaS%oRfudUf@-x_LaMRt84Uq-B<6N!;Kxz^*oYy^95abIb%;|ZYeWmA5T^)zDr0}EPc#QI4zU+U(cQ65#C<@O&2@6wca'
        b'7e|bGq!?Tj+Cj8#{w(yrB<K1#;0SQL`BJ1Z;6?U`n1jsTn~eaoOwS-hg7@b6z|o*NPMUp|J^YJ^yW{AlX~nZ~63^|Sr72%qGwY{@'
        b'D)PywOl$q#2`}L)w9pjG%ps$46<3-iE5`Z=jwu}VFD6+r^j$YkBoy~06gv`%pM2jGQFvEZO_Ji;Z`}N#D>IrFQw%8&jJ46!`-&4L'
        b'=bK`SnFYZq@@)Cr)3G#>DH0{5$h|2kUxJ(0m1YVrW;!L)MD(9!&W6<bgZG&xpjUYANQ(}RiKdp$%ao_2q@p;%#Amegs{q<ogdS7L'
        b'IqA`-?DoH5T_UiGk|YUpH^A8V^zdik$zUdY9&>QUD36A(1m~v6o_bqIxkNm|J<^@fBRcV4MScHO<oK^5&(?m^DP;aCwBe>J$QVt('
        b'5$mgue%qK7itHYCT|3eA2}(b6$?<VfQWA}0XiU01RxCb!=ZaaBB)dY3Xx|x#97f+TJj-t1V3!mT9|o9tw1G_1YejCp(|}R$6^R=$'
        b'mu!;Rj@e}`LHuHS(b0{jw~I#Gh6AHc6eSNRa8gLyS!mZl9a0TCn@?wllFCHA$<K_(hLL=`xz3y&YC6iyb!_ft(b@6Aj}8cIS*9Zl'
        b'=9{U%6oEnUp_hSv>qLdNK24C?T-2aVWG>K#=AjxnFaNb77lw_SH{Mr74&<>@Un?So&chs&9^qlyQ<NcZpw%N+(FDhkx8T#iPR}5('
        b')QK{!sjn6_rkUCJ-824`^c0VM+i}i856JX50<uMLVp~z)wj#&2B9B96dV0jEXrIk&I4tT2XXQ^0u9@t`op!HBkD20TGX~M@V9gNp'
        b'u(ot<Xf5h%ErLFc*U=hQQGXwDTe9acJC0eX>Y;j3ztzfbS{1X>e?1UW-w<M2S2WZL;fm2|-<H9*Z#Bl_38pKvnHkq@%;KOM1<XJ<'
        b'y=aPd(L*(h9<CSfT}?2zAdt66p@~9yk&z#}SLrPGQzD-IK>Wmb@<zIX+BZ4;Dvl+84c4Lcl?j=fh3&Qw?5ikF`4^+J-e?E??cf<%'
        b'riHVa8Dnw+x)ch0_M4+;39N_4ogkY?{YOz7Jhk?OPz#Gth-H=q$CAzV$DMX8K{4?PI?c*R%`IxAoj42Ynk>B)7#UkfIyDPbuneaP'
        b'ib#$OUoS{x)qXXF^Ad-=@0@*GGQ`%oE#SHq&MF$3Dq4_M$`)_r$fZ-#6*FVD_J-Jd>u&w=(rbVj(I9H4-b=lheO1pjeTiUNMQzl('
        b'sTZ<u6rQP0aY7JOzlWc)-RKlxUu`DRJJ`>%r*LC(h|%*}(3YR;0ZEO-UM(T%rp>)<*FOTXih-IZ&569)s}?b)Ab5*PdIiq-ht6`3'
        b'bB1s*E1UXx*^(j>2h(@}HSG=JBBwp8xk2(w<D;Gs7WVq&3gJUnYD7sZ*H~-#SnaT8WvDj(;hH>5o5zypp>jLsF&67Mw-<p_T?)j|'
        b'kG4blc9brAMttt8Jc76Q9;mgK4H-zE<$dH^qrA5Q(uY_wf$Hy!tk|v#fn@?PH_{V<Ch@5*jBLrkgBMm}R`G!1$vV|H0dOk~VGIqy'
        b'iB)9A(aHy=dU*aKFfxDjVGvgN0D`r794u=*0%Zw;y7w+S7;`uVXGH(l<^K%A8GiHoI8FOEadMpw%x3629B2wZwI&D)OtW<b0z}*j'
        b'$T&R14EsTeGwva@*7o4MDFR^RJjBRgqyN)9)aWtZ1=8r@Y*|MpHd`g;nP@lO6DX7Fa$v-tCZ|I~n~NG+?G5uxmU$*ljIIx1?m}6J'
        b'@NgXrG(~)ersqa!;_?jl08P?|7}ofKH4HJ9FN3m@4g!pUMso6KQ3P*)z$^{XRbjwhG#K$67*I3_BY1xn$mp%_!06_<`U4#iyx7UX'
        b'RX6|>A}px~oHaBN<Jujtx)@e{!QeOHID!pY1+dXXJX&yro-dE;z#G8t@8DS89WciUb)_RXB903IMTX(%ic(a5RQAJt-^b7UFYt4Z'
        b';@1(dzVWm1BL%=OYcv{vAq7)7ch4~rNcRP-jc7FLu6q;Azc*lA12*aIUJ_DJz9(SKL@<KsBesnc4DSw@lOlq^$ETO?g7it>PLuA0'
        b'v`EJT^MIc5=`P?^l57l(VEG-87W;j;!(EVm-?-EfoXa~Q{r>ON=Z3TgzMU7HUAH8Abz%ATfSC%tklnyCCr!Rlh*~Dob>A(&`?}U~'
        b'UF)-B!;XMGNy2Q+VAjmt35?atoKcqgnRYOEZ%XQAEg6XxnXx5`mMJ55?#A9o=wZ57(|K)@)y&7P=Ustv&7ZKFU*aUSQ~%HoHZb?0'
        b'IL>ODS~B?R$PU{Hv{A8>-yS(~H{g1ldRH4?8h*Vhf_g_AuMkr2Y0XD(+3c7xv4y!q?rm-SsxPTQ?Y>o?Qzzit4Px}}S8`-sefbl2'
        b'eL%69ZN(2M++kaitdZAOJ#@WP9j}-cpEun}v&z#kH{Eo}ihKAWS6&w}uhMCl$4-vzeI*;}Gydj!S&VjbW7zO|jJbCh8*Ue)Q#GW2'
        b'6eG7Pcvcq4Phl?CJhMvDSa(L&HZcQ7%SNuRo^XA>IzA&jUj4Aitp$&ZTxZ&@ZGByhdiy8Wxu#&9VY)S#$*yJg!MQA$?jttIN2b$b'
        b'uNr<3K8po+h9AX(`?);!6|N+d)_==YgrQaCC~c@b5v4VLBVCTEJ`Z@<Ax=9km0?Z;u8aPr8!!Jn;6KmY^H#6jf?M&Xqt?jy(y7<0'
        b'gz<`~_&h2o=lE6feX9~3zt>h+KP82h5X>DmT#E(y3y)JVX5xd4afeCgVBpO{9*`P(FMnPfj75=m;rP{99oJWp*GnJ1TL;<TsMOYH'
        b'eBlmrRbULg0J!|=yLCK_>HzrpBQ~v<?O5<_Xj2$y4~#&Y7lc;6XbhV4*9<g(H3jn{Si>sRVNC183iGsLIp08I;#0g;w78z9B|>sv'
        b'O9JkE24+bYO#}~naeaZ_GP%91ZXBXpcwWO%;7T@s21`q01{(KqL#98~O?aO%n)>rW)k^Uv--5Jmp6SheW@M`5#kg)<dJ);Weg)o3'
        b'_}C%vjw&fYOFKic;LsJeVAF!F<`A@Fc9%89ti~3!!W(!aF~xS~9gY43W9{JjBq~zdbg)g(w7M;+DMNZO=ri?UjxeqGDyX^G&Ca96'
        b'MQnt)mLDR$9Jt&F<O~HaM_cg)dwu-iSn!$5JiM3X<M83_qrkudW|aQo*!o5j_^#CLLh&c;Zq|Wp=stR~$=Gg|>jb*{lQFK{Ea@j`'
        b'WlsKaqL&Nwd<icDYkGN*js^p|S)n3H`O#n;W4c_}%eL~rWp7Lu3eldMG5d^8+i2Qj`mm4`GFy>H_jOwF0>Y>%%C|P)nhI}j4|i2q'
        b'%*xeahoqHLQ_%7owx-Ki=9ichi0jHD-uzkBX$2FscFeHTTediK=oyLbO-y%$Ao>0<jGO?y(?!;B5oV^N*412K>A+S+nhlf8hN!Fb'
        b'Brq^!<dufH+x(NhSab_UcSt)+T86c;)(e2LkOr1igAEsAR+hNuCTh7Akw>9}a2h5p-!D0*$I5487g$JMv@f>oh_`yr0;ee~Ke&w('
        b'(de^Rp>y3$kLBOBO`~ZU`FHyto1FzwR#pSDB+Qol<D3C^N<-a1Da4D6&I_1jEGWi6GYB-RdA4-WD$24-jP9og)gos$X0(6l%x0Oh'
        b'*+zGEmi1|KHYdyYr8%3MWz9Bc6UuB}v$4o$U**ikr>`&$c<ZNfeRc&r>|P6UaeakOw_8ItAuV!!jQabo*n)K^1p0@1<R+J&l#Ogm'
        b'HYe0SCL0b94BeP)q>lnUvEyVDZ8pSSrK5o-B>zf7i<6E);*lLEklUfc)(aq|m)F1oTV1X|qB+Wl1_Rju6X7F(7!gkzh=*BoK>K8)'
        b'^665KoH)VAVg)0MQ|j^Z38pbLkWtJ{3}!>j4E~6$f*ZsDm*bp-aE>b|pZ^KDJOFYTzA;WN!$G+ulZ;$ejgw0op23>IY1S-O+Krj3'
        b'd%`q1UQ$4cThnm}Vh&cU#+QUuZl09BKfH~0%VSnEUkrAvt70{6Ft86jlAD(5^l5rn3%ZVTOa=tFie)}*%&%yCWC^RrZX~&eoyM|7'
        b'q03d0fxWsq9?2sjFp}s0Iv{-j2v1k~LUmtrob)3VYqFhTOWQ@R2e3Ag%`laWvKi8^(o><M47sworH2K1KIPpGIqB0JCtQixvmnez'
        b'vi3?`QJ5<R6DQo9!UJWG3U0)yh&n=sz;}St%W;X3VJtiBRj_EErfiQ<<20Jm8CkwRBFiC0Zi~jr^4qd1|8!JVhz)sR9vW+2FCFX>'
        b'+1--Cc2U-Psj*$M>$r4qt;pCUu^)ZfmyOxIU;46H&TO{*Xm+#vX=gU48Of7t1G%}gjcrd4J|VJY^Nr14+Ok8;*+OGmP{<@B<a<EK'
        b'zHHo_Jwcg$?=ItFpZ$t6o3LdIl=feb%6d7HwM)aSeVQ$}EQlqUHh7LXZqnlmrRhhelksv^0SQ9?CU5LorQrT2NSm!0JMMMFu5y54'
        b'lS*^fz99c7`#bM5G~?H^Hp#&$**@-GWi+2MKVoDr%*gts;?ei=55k>xiPZb`$a}Itdi3k^p|SOIlICk>hq3l*ebgk<)+!Ho9!sHI'
        b'YGW5m(j_Ta=h8(m_cquUwaQa>C*)Ic`MVA{ckRh$cIREOij19JyZxH8KgIJ_it%+8)+O52C4r((3RR#OW+zsAwN=sUh|0G!#daC5'
        b'+1*b2*6g7qQJ3=ylBd@sFBp1IWNdIA^jvvRBxy$gjn8ERO!Lu{=H_bv(`aScj-@nq8QVq8U7#mMRKq&|-vhz^a6W4xp;v0k);gCj'
        b'UtwJAEz@T=R+K%J9aFI+wSd?ME`=StZiZ%LEZK(>GR&mVIQFX>>rxg;>JOHg9?>|aX^eHo`h&j|AK^lFx!t(W%)OG0$?aJw=4`W`'
        b'm6GEVzk&6z&hm~!uk2DpkUWz65;s@M4PKGtqgc!TE-Bk5>Bid&UDG1k3S){hE1nHug5q8d8bgvGA?l+vZ7frpx_U{a;sNNJLrl?('
        b'tO>LximwWT*p*m_!LR>f0PLmyUQKnCX@aJ*=Ztvc?cMiiy16FnoZ$Yx%-bFc)4U-u>5-x>0Snwf?UNtaXU6@5=*AldTSE@mw=L=v'
        b'E$A|K`Aj$Fc4kAX<C`pb%=o?I%eg)~>9J!Cg(ee9vKETtxNRclfU*<UXE%HIX6-<iE!gkgH|XZ?4p(PHqQlC%#vNa_JCHYW?L!rF'
        b'oSF>V{p{To$9r?dZxE*U=AQUqHUnG(khdVn&37TU@ps?J+tnWG9l!Z|_r<(Y)~;`*ROZc(98KAh6HH5+v+M4beP<Qk&6jd8d!s}r'
        b'_@pQMIIkOTD0EQ~(%6Vns!bGAJfE@_Hs^RZr@2$xsAu^L`5m3Oe^;QJ07m4h8AhlYgYoK<%)RIMs9&VC3$=DZa5g(EyeVIpGmxWZ'
        b'#yUYR@rZ}u*iQQZE8IR;VvwMX0y3`d9FH96#rqv58Onh6WOlPm(mZCQHBpr4=;g-ZZ#fco52Jl9ziFF0aEWo$&|A|bH&^;~1j)|e'
        b'X7HE>>*jj;WYWxVHxK?@8R29eX>jv;`N#1Fy;&cc_#4-a2nZ(KTqensxWV;Rgq!Q)i7Sdq$Xa#kv26InDZd^;{eG^eFU5_Mlcd)o'
        b'^7?v-D{DphR(qbvw0ds7mAP7S`Q1w;^Z2zNFCV!C62N7JyYXJOG%K7$*HzIDJU$1lm?4*{S;s^W#xP_1RddJ1@_KAGTl~d@CUc%a'
        b'mxI>iXJgs=xw$P|MVN|<VcEZgXF@?Ua}3!}!V60w?`4tEu5}U0$x*zICMYKotsn87lf}U)WMvDX`-nxur*llA79~0<EOfV|+!~>@'
        b'V-^WEy39NTGfyUG3!2<LbxdGid&8c$)jW|{SryVV6MCT>RJP~sEivZ9IrTBf6E;0QH+X!;+n&i`O>cFhqcTjHD2-keh7RRQ#prp&'
        b'-P+|$?V}InDVUoDhz$QBg6Z>t7t*<m=v|-Rjn}mk3FEBE8qKxza$NNoRydri$&nayCYMfB&Lhr8@U@de&qv@Y5mvQFOmIkkDc*pa'
        b'+H;LLp;=kinu?s0BmDPbSWg`~0Taj~unIwn72nZgIQk(ORi>`X%33k7*nISoQC-)xcs@=F{L{d<nn)CIvS<llPox2>fvX9NC*)1c'
        b'>hk8j-ISx89EzUy^win=B`29pmO~uOFp;Pbka>9QySa*4rkiteOCQg!&nwFbC5a^yt7ZbufU#i__U2+?g@CK1F<l(yTolps_IzCY'
        b')D7j~oZJ{_gQiQ!Zjpk{w=LlqAfb{#DZdEAs%DCb>v?RACVUA*)nz%}`i(5>yoSlD5DY8b+EaIybDZc#i~G+<-#ZTf+M5;}ydry!'
        b'_k8%@EpG-Hi|+25%o$LSxc@$^sm5v;P@rSIFq3~yJ<>G`=$h#WJcF(=2d9|&;02e{Y;y}CUUdtk=CrfQ7e|;uwihOVlC)l6Bz#~F'
        b'vr?j$UH(x3zD*H)>#JwZnD)8KB7*z)2F_7`n7w<~95+6^B?6ssgqgO^32MQYqvP?U@Bn@w>;Ns-5*|a8Qp-D_JfJ;bAe)@NCrz=r'
        b'Xi~&JC(+zsgTDr+>6JMR9`xfI?YnosGzTovrijsZ2%HdJVGLfh*tBlWT|eTx-<})yO?dc9fv6wt_V3Rb%n^0to+B$v^>di^yCoX1'
        b'6l6rd)zwM+j#QbhtH#aW<<16MUp}_C)^U2a=~r{^es`RjZF*|_`^nj+it+D%oo!k)?tS=nKw)T_NQkiPsyTAQG_{iqR~zJpbh!b^'
        b'k&ShRG3L0FhCUen<nFNJZ1RcnPXccGIEP#}d@10TlgS=?nDkOWZ5R&jlhk8Du@0*ufb|lsgo>K&#ue2A6TxNAgSP!{QVyw-#aY8u'
        b'6Vbq$+(zgoa<bKPoW4@ETyBUm<sux1uLj(#UY1K4K{jRJ8FWTihB8B&VE`+G#I+0YCF5kqIk_QB4oyY~flQUqdg{ha8K+5}$00rr'
        b'pcTK;i-Atg6oIb)&hV!UJo0e)jED?w@C@Nk0;XtG*Y4yw(q|%qwnNM$$mR^MhyeN+pLiKt5jQZ8WLvrrx?&=IQG`OZg{|Od#RQp{'
        b'!D`+ZdO1TCj$z=CAm{K3PrfrCzI5C2GWZm$_=?DN)&>@V^q=GvPMkA?Cth@?ZF`SJ^Y$XtT@HmnTf>QFtSzo<r9I7S@AP)Y={Dc?'
        b'p9^R-oGq^IkQpHhLx^8s08PPKXDwwnuoM#s7GmBEuDI@wPfUR4cOl+Q)HmUlRP5tDxIZ4N*=Ae`uW?w9>RsKgE^nvkO1J2AmsMo{'
        b'C%5ZtjC=4mRA!fb<!?Kdru8C&@iCea8b~6-z|5(RiaIG%JmRraOn6@X1Gpd_yAga0r;fNl0k<)Px#=7#^QquWe~${@m?=Tvk8<Z9'
        b'veH83I)Xf$ffEY=Z_!27YF*=J#+BZS#OnA@*(skbaudfV^l~p!rZvb1aK~Suo@EaKmO#a&OBV@?7+a<4Nawt(`}>~cl;1DXye3)x'
        b'ro{9sl-U`N_YljwylY<Xj6Xo!5`dub^8JAwYlz3u;Y_d3ewLkn5dY0o)!@pLgMT+)09GI80-q;9Pz9W}Jc7C7))X&K^DbZGT^*;}'
        b'|B1?qJlj$h@Rtkxjc8zz0`c&jGnvP^<f{-zbRxoHHa2C(bfs+eo{Z<7i^rYuz$VSti!MFe@jCrg#{+1+e|xG)#ZW`^5^K6T0j=Tg'
        b'KwIje)BZ^8?+=R+BJHVYj*vm6E%khK9QdHe??olQrh+ls4ayzgmU<<~iD&P<+2yRjmbZJ!=z#->&h}K78$g~(>WN#Ew)_+C#kl3g'
        b'UfqN*EhQ+H7ZU~S6tLGiqV|j66*tWO-~Iev_A&urvyVR;pCWKC&~_~CD%PZgYhFk_b9lo;>gJ7}=8Y5t7ekvxUF|~|qRjT8b`d$T'
        b'bz@v=f|`s<dBl^FP8sXGLkdx2+E5+*pfgGy@sj+MhPoO2D|Mn2h0#<t8&ZvF#^EH+a5BfVaJE^7iSxKtaY>u7jmYCzpBcF5=VKVO'
        b'%P@}a;2jl-VfEW^KaQ22FWE+b^)Xun7|HPy7#UF?$C+=2C+qq8IM%|D`R4k#d;R6$tY1@`{fn>$v&DerT{q2|o%PF9<66&#oY{?Q'
        b'jq50l)!WVYf|i$hz0Zl@4W5l_z0GYN<J{EEZ9ryLyVt80flCSoILqqI!{KvYSOebtqBoCj53_IccGA=L)^7`mX>SiRA3XwI(kUw@'
        b'WL~B>;CW%wU(0oc#DIZT9$`MN#e~eubahxB9s6{y>xt4D@Ox`Y4Kc;%pT<?t?zze%7v>w(bg4W~8B;v8STtW=ou*)yOvZ_av6N!('
        b'e0j{&_^q4_rRqUUp(Qyn=p0(Dy2g@#o!T2xS|en@35z#LF$AuBzM)jEJQ4}Xay6~n$jeg-b2jB*YNaX?BloJ6d0IoqQ^KP8+UgwW'
        b'>9au0?`+tc*ZktQ#5`Z5VQ%XoBU)dKE9}nG6nQiyl<_(5P^qY~7#%KJ>@5~)io7I<MzgqXA)$0E%?C{Kl;|R%H2GvKLoU517<1=Y'
        b'R9gZgdwpAYr=DOze@%u!?AXqg$U<9f;UG$|8fdU)#+_4ZSizlZ1$ZK7N(ce26$F7996yOsZx>iaWVFN@O20cqhDbKo$#%DMJLs@P'
        b'4!tNmwM<2C!_p&33o?HIJ&{Az%o^Dj3hostE#cr`p3btK=wmk6d==;s%|;8ccA}|D!0F6sW8UP}3#GL_NlqyEfZ!I<hjSCzi8CQS'
        b'm<LW?p{roNQ)@SBtddfZc^)x;UMZ`S-8pm1Yd{wO+JOKyT>?-5!Wv43Nvsmc2ELMnffnoo-T3r99ed)Zzh!cw{GBXCn3Z(^+D)D)'
        b'BMeCjhYkT$Mwq6?Gs4_qD7Or9ZyL!>kL9K}EymPgjQbSKAC^J8>Db>w{@8V<#*zH;vHWtBpB~8{3Hj*^xm!sBd@1>s>Gvb~wPX3U'
        b'jNbTJ*jqV5M(f(Nu}7Oz!gaspIAnRvb5rdZp4fL&9-*>kdWWWh*oS7KpEOZ=d%V13X=b~<)6@KTs=b3s>GBR`in_MKPi7Z7_Nd(}'
        b'x5qZuwJ7B0Cr%*$5<75WVqWY&<Q-2D670k;3djku{k!kYi#>C-W0`6ihICl1tl((cv|lTQYPB}Y9=@K`2{?mmJy|<bjn7ebw>Nl3'
        b'jXU_WenQ8KbY}Y?ATSppkd^Np+9t~Hf=rDg2&|vb+|-h%e2E_)9#Z&N0n*!9ZJf=oACULRx5ung-H%}}@xc~AgOg_{E4I$d(_U1@'
        b'OwG`yG>5Mj=rTCFT0AK)q@rfi;2lDjn+-LfpLWrDvb9BebL}oLERUx)w^At?-k}y`IFa@Awxjj*Ge~1*OG=$Yq0E!VPbA^<=9k(+'
        b'auc7oU|6oqG8(H%7xI~_Ue5%o!e-#!cu^Vc&6`}s9->9nw0E&6OXWqs6<%+J$U3vyKusus7P^4WOOxTkoTQx6dD~^V8cDb=j6=Pi'
        b't9d0=@|*{_)!gPCLKl&tJ*MbbpZbjwTgTGP8zqUJ<`+^W36zocq6@@j@Y6_pX;DHuD<;RZDSyLPPpE&}_+0JP`UALXKUPpx;x6rT'
        b'<$4^;PC9;du4Ae5jf2lLDvizIQ-rsccx6t>#_XX)(Pnzc7W|oVPixx)mt<a>v-zv+p;tsV+lRh}AH);d`_es<KejX{N|JJ7tp10='
        b'{%<TM9zu&r=Wuq(JVroXN;TWO-v&sww#A>8?Xr0!pCeWeUGxsUEV|S_bP;}nV7*%;lFbONB*!bXS|9+}y(+h$)ah8}bNuRL$5P`^'
        b'c)hgE=2)hC9xTQWGs))oRsF_zbH~!g=Olp6PQ)iW@X0AkN`jv*#3zZ&Yj!M?w6%cVP~A^R53wb2W>+t}j5g}+PZ;7camA#ndCrcd'
        b')m=yHswR<<#-^Dao1&^d?)mE7`oZ(wT@~I+r(_xbV;Uz4F$l=bdd#P14cpmf3Og!V#ur}-^M4VjS_xh>lNWc|F}r;Q8TB#EB110l'
        b'nwwWNS4+eXVa?T{o03C~{*?Gw6x9y?(JPL}cD>|vvp3V5yV}w^+1>1R)-loWzJN8Yjdc_$r8x4Q^D_Q<K5sn<Y6#(Z+ix3lHn*K>'
        b'=L%ojWem4Dmg-6cro`M`(B%Gz`V0GLf6*EI0Va0D;LwDf9Zz)?8=v!NAZI;gw|b#THa0Si6Lq@9z@?>{wiZhSrZI+tBy?_$X=1MC'
        b'FR4bC$L^wb9rO;pDmvITbTIhibo^@nMwzE$=|KkQUl7n;0JKMBTxW#eT~^~L*ku}bOGhWC{kPx++Z((MzpW5+O1}bfv<ZCaHnxT~'
        b'7Un&nJi>t<ZAsmNqO4!1YP3{Yv3Iasq|teyM+^3&zbl@<XyoiFwSN9@mY7y=7>#134+T6ley%U{WM9fvJ3r;Hq#M5|dXM!rRSrE?'
        b'aD87!;b<un{|ROdWzzy{^+05KQou8LtSm?3lXSC#WnEIvNG#gJZh92F)&R3Z%oNBUJ4@y|dhD>_mZ_M+cIfTAG?JbEVzea$%Y3~@'
        b'2%b_N8p;0xW$NYVgn=j0thOFS#fL+X`YB3P*Z}lXXaE4c^=O&rkC|s1^ZXI>e2#hkfO)<uUdN1kpG9vTI+XczI{5PF$hT9$*G%Ty'
        b'+vr73hc&(JnM{vl_$veIB=h|(1`$Kk7YZkHgsX?1hNxw3nwe%|8T4^Adg*cQsTZNwUx${yfER3b^38=r1}h_*<kyF@gli#&k{9yM'
        b'*^P3$edq&Y$_Zoay=eTufodo`r;j<QkG`sp9j?XB3pfmvrXm@OWXqLf>pfUn{p4U(CPzNA6X8?~xD4wO1+_Q*qZKBy5>bT{S;9Jc'
        b'XMkoZq?rmOCyeBO9_K)n+;3IsdKy)U;BcGfeXC05tgIFuT2X=q!ko7^^<(DA5nWdEq6iflk^rA!!)0Z&H5B}X(J_gU^F85HeU%VO'
        b'lT%0%e5Cf<DDwwOND1Z-F8o4s4K24v%HFMOc++hg8aBGe^tTc4Ons({O6Q`8X2w6cTL$6w((TcOElB6)GZV&1nf3(|-HRNjU1K_^'
        b'L~&MmrtT(oTyWx<e8)5SPyWtydlsas1?p&Zk~&kJuU??8R(Gins{7Ta)tA&amDQojYLT)!Oj$iqnIEg(?2~4a_c2Qd>cdComl8$s'
        b'5%(r5OXPxO?A`No$a;c<{5bLOo;zqQz8zCd$FM1c4aZ_E2RoetY#D!fS17~^$)_sY1vYf`%7bR)+$8U-Z0ErHgXX1I6P}Yy#}lG('
        b'RU$_7F@yb|WpwD1mdY@kNWg4-RxH<i6h9%KIS_qfr&81F(@Z&cfFgy7tk_qk2y3sClYGYp$(P^!bGYx=U*3G2>pOM~d^6v%SKfU5'
        b'5#O=Sk{u6kdJu1;5;E?SKpZA)-e1@Biwmq?;?0L9NTlXoUQ%)}7Vjkh9q80P2~-I0X%i*Wi6K+&8Q4oez|#~hk(6y&(IgZqz{zD}'
        b'x-YMjF3ahF?&<5~bC!2U&Wi{xMFMVpdUxE?bXCoaVxhIA(#zx0FW*gfT?&k?aWYe(iPZd58Mlop<!c^kX=kZEz+%vnJ~F~MADwB~'
        b'^oI86`((7Hv(Bzrp_ASb_hggYn6003Yrj6roi9RtLN~kb8?{-0#bh=fx+=taM1yaM4i4=8O5OkZ&DT9b?0{(Zm!r?Z*LUq&v2Ptt'
        b'yn*%omwM=R(ZNGKLc0(nH>(a|9((ov$kh5r?<sg|e`K7;UbVk1$$t>7+1cNQTYBJO4Lqp!!NYI%NAl6Q9cd+aSTf(wMeBG3EVF%S'
        b'{T~I%?3A;T2Q!Hs7#7Pno|X7JG4s*C7>z5YuYnG~J~Q6&wi>OhZM5?3d@Oev?tdRES%wp5G2$G+fdtiAO!ZGJJ|qOWZ}s!}s&-8H'
        b'+`cMY^$_NGV_exmvna+Ui;I2k31??qqoqU2lZE@4rT7U_cCs=tPR1#XTR_vkTQZ!CNaRlmsr_1I!Aj$pg1;-SHA{*^*SR|5V$D#R'
        b'=E}m+AbSbTPBz~yd&7<QgptxIA)WjKkx>4b?^nx_g@Y3Qi#p3k>RbXS{rpngU@8AEzF&rrg)_mzzbN&{NL_ROTlCEuqwg`y8dux+'
        b'JFDFqx~}IyTx{e1B#spotWV-3Tg{7cE5{uNX7cC_H@_zmYHGBgk})(mh*n+&Kip?GlEQA@dxaPECQmjf{ssNJg;tjE<!0+Vm5|93'
        b'Ig+P6o5|%K&DEAI{A}oXkU1&n<Xc%o)_DyqA{zQ?M34s<(fEY#7%<|^q!C&Yl1BIdC<XZdTo9`6!Ok5W1f@oHb?DEcOP^f%Ow{-p'
        b')3Ua-nU4<EAH1LfQwFc_0-9N$2|>K&n}AzH_S8q?s-%FG(z3Ax8PW6z8A8Ma&~fORwz_tfB_2cWd`T%+7AGtoY!h8CFLzLC<`(l('
        b'uAPhhj=n;NuG7wsD@g_cL*$!~%(}=hd-J9-c6Wvxh*C}ZH}aAg_QbdIy*Dl&B0B^TyB?2iN}gT&Lh|$AFvVD9ta=((y&Wh`ZKE2v'
        b'U~L8yMH&30`1`Jq5%D3oB_UvWC_qZ#(H|GEWCSp>96eJ3iz+~J;gNVCpehWIkHDiUHemThfSiTOMFmt9foT*$>$f?nZF2o~rQWI4'
        b'Z!zd!s?onJ?cliuPW>KJ9g?b<+V0fvq$3G=U+7B1L$bWfHYidcH0{e{j#1m*8Pcg9xMZfbk-plm6Ztm%pH!QLn4H>PfG5t=_JztF'
        b'ADIGK8}4M0c;+Lu*W~*3wEhKJ|2(bVq}1oo`c_)sVb*uq^smbGc3QuW*6*kF-L!r;t$&Ty|B2SWqGCZkoi@EwPB{@<(r7l;q@;cC'
        b'>*#=za%N5Tio>{C%5LZjRdbcp3yBd)IZFKtO6qy-DLe)qpFh7=V5aQrtY*Dk#lw8gI9p$+2MD9K^&cyLiQg1WED&lP*A^6N^>zdG'
        b'CrO3T05!9*fiQob5NIGn=y!0EQ+q?H)W$5LsaMSUtv3CR*&#N)gK5rKjlPrQ7^uz|i-CX$qtl>wKiPG{mPfWFtCL@4x-5f!hmUd_'
        b'28JpR;>2V8p$bv;vMRz(V1UN(3p{5M%c+0OBt=Yj>UTq;>v>4T4b*O@zFRE5DZcczL4b)ZUmLbzmc5wa9lVCn>RN9k^ZZJT6sz`N'
        b'P(RsLLtutC2P=DU;z1#>jTFQzd5Mn#d3Vj5gIBslT^*1kro#N@VEuuQlk@5)p(*ubUPlM+j}+EWt-`LAUHn0G5-}P>s&VG6dHSUD'
        b'NuRT9HS6j-tWUYoXZzpiWlNg_Zh=AH>D2FVQm?3Dk$p6Xs>>~rSj{`QCm}la))Rk>wN@rijq&^Rt+vYORvEV@Aqu#)U&cw!Ggn5}'
        b'NZZWP&4U%9#+5a1-m>zl%gy>74FsAR!-Dw@WBFBv%4mbMtwy?eO@+aKtBL?-+Nd2){VS&$E;KinfiOsw>eq-V$@^<mTFaII62>zi'
        b'43NZrF^_~2TP;eYNahe0*={&GSPAj=#{wtS`Cv6EfQYE;Rj?(9L2ff*kmu;&eqfNgH4^vN2N`4;6pS#4$1uo3{4jrhAFv9ZB|OwC'
        b'=opX@-b}*G@8CXJbnNXXcEmPRPI)-y)Jc7-vnskHk!zMATHj3MB&%&z(PoIA8QyFLJAKQ_uPz71fL@@igh3XCI!TmQWvD`Y0X{Y&'
        b'zF3Lc>t$8*fK-qE6;Mh4f&hk{qqYwHN_45>N`<Ju0zMgdSj<Y`ih*)N7N39c&7SuS)DBfiz+gA3?#F6CX^3-_d&n=UUJ8YLe;uq|'
        b'>Z3Z(LAe2+zVlh~oZbzIZ}z;`dOvPa2a<6Jnk@|iVLTbGdMrR%h<gy94fd*<5UjFQ5Yujh2I0h@=@k$VTY+SdlG>NTH#0~Hnq?;#'
        b'zgWUdIm*C&);s*kfn>r4Z|xFjVXDM{mTEn;t;BinAT4tCg)&>p2&5<I!gFWoNoT>Q<iYH#XIQ7t_|RoXYF7VW(Rq9US^%}ZqIv-A'
        b'(JL{FO126BfD!=2`J*s%Unu=9UPDL6-gqK6wys1rE#^71zEx?6&YeuqG{fVSlR3#V<%VdQ+9Ic39xN7R2CX&Nj|KA+xf00=kP1_R'
        b'3nf5+-!8!923!GW`DqqC(@3AjQ3#_YadM(T|B76{mDanK;WO}sIFZ8xietGNhGs40Fi@=}!?;C`9ok#zoB)V}eM^d0;H6=HFw4$T'
        b'z@af4NC%30*=p9+_gJ5XoPMwW7zDbyfI?6jt)yNd`Y?v{nU!0G00B%{lGGoAjnFQqqidi0U798>H1@{2-^M;y2`sPx3u+9}E2Sd@'
        b'rAs-<b$2;X!EoRP!UF2AUXnq~7yCP~A1*PLUG*}^3&_eXj~9P*f2C76N|9wLHbxFZ1`=lou?%Id9L7}-V}}-3I`0|HF1KMs^-s{R'
        b'3dlEOma^~D4!+2@<X#e6H%heD5MA;^at~5{OM#EjY)qT%UxG0uepv2+C_({|(K?KSb9HF#crtLz@)Kel&Irf_m~u>ife^u%5TpLT'
        b'pd%#(>F-a`0dRocDcGSELHwB(sK5bz3>qIa!GlO{XBfGW3>l~Y(f?P#e+sA}Qo?^5eI6jgEGzg4{1FO2g}wq$`DLn7|H>vQ=Kpm_'
        b'N=g|SMsiY=EgDT35Rz5wO+KYOjT>^b#94@f3=}lI*7S=1IP_78GaS$bG?Qd`pub9emsbC(zW~!ZOF@DQMq~z*pJIJVoIcg>XQIjb'
        b'1Ly!)zYzK`pm}vkr*M>G{!9Q5M4!T;OAzO9g76u3Sn;;7pbzAqirJi{kbm<C{Hv!~p9)T&?(av?)ht(JKqgQ`)A}yC{#8pN!`R=J'
        b'Yz-f^Yj+`8C=9qnzsI!lwZBWtVp{p4*tI3H9LCTY4AGTwqir_sTdh23=WeuxS#f{_@Mx+_PQ5x}^)ezX0_4y9V0otSU7pqGU&-!%'
        b'%s{=WrMjq`S*deWS*p<E_*r&0x0hp@hvvO6H;%n)(EIl2$iAA#PW<LEC)MSlUNse<#8de=TI1rQx=vEBc9XsLm~vFiX#{-Lgb{U0'
        b'ejAMIhKE#g%3V+c9%H(bo1Lse-Yw;zcm4sQDUu)+TD`-dcYzP*zX<Rs-s3jv)mB^pTnGEifJl|7ln8`e@62^_P4}tHdZ#T2qCJ#M'
        b'BXK!$03COY_j_DusBU`aKP4+d3&Ijw3z6sh4n7^+HwQgaqqVQ1kG%5aTFI<B+Kx*qBxY)>a%Q0cK-d@6JLiJ8=Q+wUeK3o0{+zng'
        b'9Pq3Q*w6~l1oM1?@bEF3+8U2Prlhu#6Q>BWCf7md)8wJwJg`t8nOCQgthnq$PL9iuWMg(TH=3M?Mkg~9Xrr7qy^G*rqybWC{Z{a)'
        b';Q^?S1AY!nGFd|FchS_Va;obT&Z2x!&#TGrNa9kodJlN72(qUjJa-aKXuy9i>hJ4j_u}QNczyiGPP{+MwDWO5ypQ|X3GQQ41nAIk'
        b'hLV9yGF++OXr|m+yFUB)tddAPdtjE9+6w3hpX<9h<HYe<Xx))n-(%AsFuja`%n;g>B&L%=Ms%1?%wjIwJS*(R(PH8kQI>O5hmAUL'
        b'X)!o=G4l;-2vK^p`n^*GGla|d@%-4nk7k_saE1`P3P?U+>YK$xF+EU3*L9=s%#0JenMzHE(1-J&Xz$KAu_KtY2PNqQ9GdFj88Wr{'
        b'W;y5H>0C6@tpxTr3u#*4YyfQ+e<t^{wDt_JpCy}cIY%H@Vg%x|Qi;XTz}qR@1r^gdw0^H-n)g)Q9XYiZ1uAJ?xxRy#f)$h_DLz&*'
        b'iC<7mK2*}mipeoJv&ssMW~WB0$8F9cW1(@r2$W)T;e6I@&T;lxT>1eQ6r<qjl2$S3GH*B(@G(<PBkhIwiHHo!xS%3`er0RC0emd~'
        b';2BGwW5x;l3?wO&aaQo`PjQyY3nEcc8}p0%+Gm_-4}N}{5!X$i7#eeoQVEnR(U|>oHdIq0zwG}oQ1Dxt+L+!-%c-pilS6CYPN#)R'
        b'sw3BltDeOC#n8*SwQt<f>fL@8R<J0&6<1}0F?9>&+MWN@=t9e~R><`m3&fQhIp5@DWvzhbYIqk{s?wA9o~py-c9tZ~tF%u63uAZ>'
        b'k`<&a-KnRY=}Czu)vOx(B0n0ZoWU{9^nf+bQc{{6?@*B_zxYbANHfnXG-%&Q(W<cYg!fP*_T5n)Ns&7<w9a%8NM`1O1t>^U0%f#v'
        b'Cd7}k*(LHTOy8k&rhEEA^B*jj^dP-5B4j#Ft1|K*q<w7p;glF9@PKyaCQ)*#LlOsk-VcUNzxDiN2r?bK#R5=d1GTfdSgYR(o-6%o'
        b'Kq7-^7fX>#<oaDCdm(!Yn@}LRI6&OZDV(e{$@Z`a@jOCH?KIdc7RWOpHr)!IIO-1$LwLW_Ms1BzWVXxg6*g#@dbcVZQ`#$`5@f#g'
        b'Ta|iuwShN$pJf67?T}MD;bTg>(Z+l^A10M7@f!RraPd`07q#{ZD1#&d#6x{#Bvge0SLoulVVe1&Bs)DKdm;OLm;~%+!nSxb)tyCq'
        b'm3&sy+8Aq0v02|u0L#++$ky8fHmX|*?);1IKtP%~3+z`}j=6Cy18<js@_;oQ5UW}_!2i(>l_XRxoM4AqavoQuf*)7nBuD#H84j+;'
        b'5A=0v7IWQ0=N*~AFy=pi`z{>kzJK3;f8^ix--9~v<L<i*ms5Yrz*8Pi%?R`F!x$GK_dITqU^}LkI0d8RsMd}V11`a7#u*a$*J9ZB'
        b'ao_rV+}*fk6LuH<AM$@j@CWQ=_=5R_72#5O9w$=3H!ER$vk}%J!hV#u(ii{F@K&zH{AGxeR^aNx|E`j_>Vt&%@BdzmXNmgXr9+AN'
        b'9~wiS!GJ-3)L&#gMWhx46Qd#@8PNaTm>kT2epQJZ$pNZPN<?x9x+MP^e{K-}m6N%0d))W%_b@v0i+@YUAtLq1ePdvv&<Y7SC+1)j'
        b'dI2Y<Vu$`#$;96bZYZEb0l3py3KeyYispURr^3_k_rIlPPDmbJc4u4|`u#XG_J`xp%)4>uSX=lRktorDhT?uY7A0O9jYXy6Z4iqJ'
        b'Mx!$SQ~x3qRV^I}MUi%{7$3uhVX7rR9>cj7-jPRR{$FDMW3gyT$~Ax0PsVUznB|vau_*CfI&e&t{^N8=3-3TI3PB+Dy;u(D_#PSQ'
        b'|9&h7zLbC3&xl1WQ<(7p@@^msZR|(m(DGS#z7vNE$Hk%FNB)t2TLwQb4kfvUpqo$;3T=zTRWoojt~K7?DSpJ>A&H>vSwUh(?A^?g'
        b'yMh3F7mP21v{c@;7bsNw345o&0f7aj89{r&6!<Y(071iPd^#Gks!?fb?5jw+MpdZ)n^Mv)F~b|zhGMLJX7E1PIMTb;Lob%xwI4E^'
        b'hR7u8C+tV!9W)W)^h>_iM}4>Le0Tir$8F<?Z3h$*xqkjn8%M|prZH%Xnc+Jo6nof7IVC=c$Bvn5nF)No%RspXqAf*WO`RksB@^6z'
        b'@XTDxIR3e4k^u6PT+@_CnY`ebxt4KfaEW~UUm09g8g}SNaM*9m-~y^Y&M)z(y|rxk-?6url|RqkT9yT^ZG!m7cxwxW_50S=zcgs4'
        b'{+sre_+PNMs*ImuZ^0=WZ*PnKO?!LucF^8_*V<a5e$-(7OO*cG<9;NU4D(N9{k!(|v)hb`vV0!+AF{W^dx4)}Z!P~BzzTO|YxVme'
        b'BG-3kBYQO3zWo24_BC|-|GYmF&-gRKasJG|8e3obLu2cpwm;Rt25&<HL(atizx|mbx4+}h{A@aYpl|tK^k;f*{~z&ZG?OJ_8mB1-'
        b'&kzfoH&br#KENfIP8gILv$7D4bu!ag-*SBD;NTC*t5Io{`d4hwnTEvIpqA-Co0*tQnwb((O!BiVEyk=B11rqbR->v#yjUC`_6wV%'
        b'Il5hWY;gt6C-TtTyOMGW<DidDDQBff;>?sYB`urwrKC)gXy#?pd6;IAM7QZS?HeQ~N*1-0Nmhu@MF5h#i@2&7Qy#f99j9|JCHNVI'
        b'*qP@@Te>`)>FQbX!zoI~hjQhI`APm+7>4He9ZG!%y$w@3uH|P-;zOBjW>EbM!9ro*OIau0PzZCn*}Yr<W^!dQ<BlE9{*)N2GY2#4'
        b'JH&FXjp`;NYeF#H)0om8l0KESo~zu+%FiVUo1K-lsjfaG1&yk;CIJ~XYPW}atr=~xX+9<~158gQ1GC$p?@;ntmEjyTciP?e`>Yck'
        b'3RJIY<zr|7^R?^bi|KoD|GNR=KFoG(u}$x!DW{U!hXyd6DUzv4aWsx0MomTh$&#{C<PuF$Hi%QFyiJ5cn{XH}JAn(C`OBL*$|H-J'
        b'AtvXJCA5Ak?Pyk>W=-ct)7qR5Y2PA%XkkNv=Fl{w{P1EW8n|-Oj%&b{B#Pu_(Ov_EoE<1SgKL?9#!uV>V*gc~(NmT|X(ZX8uVe_C'
        b'77e4(xVmc@vk7lX2s4ZggoFK_K`bPu0Q<HAR?5?O^QL)9j@G8%)if1NFYf}wPR3>Bg(~$P@mkDA?Xn%igUL$!S|)w3t|-Jt?Kns6'
        b'8d7^>L(Yd!Cn)SBW%s-l>RX1{maz`>tafj&m-w7hgG)oA2W<KS<-a3r)PbgG|8d;u_~;z;4S!M|x#HB@0S)tM+(+40x!3LJ>4{m{'
        b'cYjuH;-74keYIO1bui~xh`I-|0YJ#<bH?@e2cecfLo`LJ4&qA3N5Fu5v?K)@o$@`rhNBg)<Uo0+(@;ab&}C`}AtM`CuHL(9TSFB5'
        b'Z#!SlUk9Yx!8~9=nBIP45UBJwgg6QFZ^O-wYeth1!K6ImC}5Y}<1ABBFC0YBWQ`-sVxV+PPD7MZ|9s79{QTMw1}xL&zXR9x6a)A9'
        b'@o@LXUqtsZ1B=bnj^@0d&q`NCkd?&mev*{~kN+H2y7a(GOXas%No|egH&=Mii>Iq3Xng>%vp@6z*$~^gU)`~N?Rb>T`X1Lp!c6sm'
        b'Jao9t@zF^Lx?VE)uK+UuyPALC9?G8AvF?xV{V_SaJ07o;0mXK8$CAjdiUa&5`yt!*wf6x&BP)si>MBL}%tZKrNb?a>k+MRBbQ-VP'
        b'U;mL3u#<IYDLb^h>LoFB1Ghb5$^OKS^Jd<<Vy)gzTw#5e|MM9BKZMI2*HTiAs?{tou}XV+eH`vz$?EG&Khc>!GDEf&&5Y=}?xlYJ'
        b'I4~|TgbYinNQ{zoEZHAJqbhz_$kN%U5=+ELC1@2EwGkO1n$OHM;6y*mM(w1j7YvkrGmTbnQO}#HJwO1_E~fR*Bm652fIlByyNE!)'
        b'WkeHN)OJ@cgZ~}Y7-)bS%N53*50hK=vcR`_GgP~TRkK(qUo6;O7dcKk!!rq8X05^T5nx+gP5Z7u1;Bo&K>0qtt_o;0&3s(3ts!L9'
        b'-k7um>1+N3mXg}IJskI|F>1!+O5g#9;X(La9`M&e1F&0o7+M0R9bE$EeZwf7LFlTVHaM=8>5T@4ejC*R)?Sh*DbsL3xiqvy{w@v;'
        b'N$k_p)J{M|qLm~@=F^FLWLs^B7w!DSt>?|eI&@Ax1K%(P-*1$r1N>j3MnoCq)W%aEf_G3RsgcBTRRVOc%lt_V`_$XFul*JS(g<DB'
        b'Qkv1Fq(u4QE6<Ju-5a=%=WTE2S@*@{tfSMVf618Cn3geGe5`Q{KMee<g5tojqzC25{C8yF>M%4fi6q%!$pvNVFe+zm51&!Jc**{%'
        b'4jZGHF%=CV>Zm0h=PiPu${>2avt~}31oRky9%P;EBvF<#FH7l-<)06K)barKop!gRW4q=4Z?`*XJZg8k%>Ni|bzlg_x4NoetE<@E'
        b'|5&cf1KeKHp^ogzIlxylt<DlNuGN)OgsyA;xHbnJ4~Q-)4w5=5aLYW5Sb#On6sDm$Am}@V#b|1<8;CVfubHXcOF|6P3t(YEgMls2'
        b'1C$tee7@#A{Jcd78qcUUnnWEVA#}hv97X6BXhAWutU;^jM7&&LgzjBZ;f4Oata9dd@eHuzP|uoYYV<GEP|qiZ#H?HrRRayCp2x5j'
        b'ppN59s7T@pCv=wz?i#ahlDE8K9)ODtDXRpdrXcRekf8<M1`TZ|V`yW(ZD^&T$k6H*<N-hP{|pAr^KBb@$c=35Zy&2n+{4(|B~e`!'
        b'$3m9$c#w@9uYxWip}RQ~6gj_wX?@)WK2}X@ex0hR@NU|EDdpFxDexe^WMi}|KO==+1lp~oI>2uP5%4PJfav7ZP6M?wBT|ldv8Oss'
        b'u75#JJ>Slcfv4v|8_(AXn1z`He?-sBV-4r1v7AllPCsgMTx;H742l+@YyKa5-yYY*mHs`MB$E(EO8_GfteHRvASeWti`YV-;iB$B'
        b'EFf;(B`7!F+Ml)FSGP&5At3Eyw31NmhF}n=v`A}JEW3efsxIsT?Y6e7U3H7StnJTQZEaV{`<$6@Q@nMzzsu)+|AEQOxjg4N&+VK!'
        b'-)ClOB`FT*DQcD@DJG@CCs|GXR!^V*4C5~jVhmKgpIA!UCO*?T?^YQexXH~8pG`+{U=&DP60;E62Gy6y98pq7Aorqov|$^4w(}jY'
        b'eE$t^#P4m`;y;=@-*a;V6pV!`Sgsw{L<KxDVxkU(`EQhlK{HV7;uhSn8WD8rkBp@pxXR7Vj0AO6fVu)_tj;GPu(Za3yV$oaSX?ZQ'
        b'A$>2(_z=(VKEn<3F-BLFWh{Le27(K$grPNTnKYspC++_U^o82$t~OH&>UA^+ILv{PdTnS9GQ5Z8V4IXSz9XzZbz<Nj+}wm<;Cw9w'
        b'bKCjQ?7oS!8CRn?=F(l7OMgRz19eyZ1qb#Q$^~@9x=(%F1=Ob3<{+ePJ}Cb-=|uyAhCuVcsA2Oo0ONfa!o+Zj07o52T=bdYoPum&'
        b'VIfOj<f$wY++q$d06pSWv_0GSYcPkAJXj&A&*0lT=cd~&xbYyE!&R{%Z^e6qIXswQkK{ExCx=eKzMSfDo_Ar4<IR{<!7V!!zpr77'
        b'fRTq&Ck-FDY__!KXvCjGh18*VZ{QP*Y=}=Zmo9GMZ3BT~baphOiazA#HVYA>wwsXasFPm^R8aesRI8eLH7RIecn)|@wdPgP6}}-9'
        b'qu(Fy*Hf*59Bqi>qW2@Jt1e`UoL(D{)jb$*zqo~Q)lSBbjMyA|Kg_46qV5wQEh<L~0Rs{_;KBQNoW1m*IOgfibLGJYKmz0KVSdY{'
        b'8~9-dLC%OXuF-<;IH{HWi7RTqrt-%~HVjNb*)OFGsR3cXI>tAiI$rcgF8Wf|L_~QTWrur=o76=j5dcwEnXh6P3~@g)ha=*5V&EOF'
        b'frHWK66{qLxYgmIlb|{ZszFJ;D)k{YeIp6sNK$qvHLn^bAin$#y#i|}q-shUal=2ZIxk%{QNM$q;v*$ZxN7<}!;EW6svcH~q<07h'
        b'S3Pq>wd01Ade!~Cc=lWxqZ9SEM3**qDBq_B)7?y@lhva{DY|6z;Qa(_)Ab6LkyV9PxD)O}If+uD*mpqo5=Uyq(t>cq<CwnjXWGZL'
        b'y<3HgjlD+rb8e9^YNlhcF-k#g?}$q<DjIhr%&cD67WHU!Rt}XF<A7UDe}G#tw(6a2NxzD&zD8xa98s~!3C44e3V-;fx`xWKIN&nD'
        b'buM05yJHBvO!}O239ENHmf+P3w_LvJ$Y&LvO1ivoM@GQ5FUo{Tt-kq`dLlNzCH;{PUi8l_?e^@R(SvtyNIclXPLr{E@KY+!R8XGz'
        b's*)GEndvGqhMlGsvDQD_x@61czX%tfb(|G`7~R7sxhf1>-hDb+jM5E!RNVLH#6stdkBUo)b+S*hKS-Q+CTnxs#wA&5s`uIGl{t>y'
        b'HNvbsN7fQYR;uHDU+mYZ>!*9J>&+9wqs+$)2=M-W$=>fX=Xbu7xacXzF@5^aN`;y87pG?Y^1`12KNX?xSEX-^`-1e24Ms_(!UW8R'
        b'CQxo1cB1ZYiKBAmxaR22jQXvsMn48v!?|;AxOCglEjxzEZo1q#qC2r7E$6_W6RnwaBADNB<_fZV6VLoW{V_4QC$R~q%;?X_#71rg'
        b'1U@?6Y?Q=?>--2i%)R8<$knlDGapdMn1vFKw71|o9qOZr+x-K|+ofBD?&oISRQ(A<A76eQ{ZzBDM4S9YT=6z*6<j){oxa&`B$m`D'
        b'#7hsno_H4T;kFR=2=2uI-08s9XY1d&`KA#kevfS|UPWMu7fUAN&US2C3|hls2lgdO`XyP%>F?o%(RE(OO0x@{H{S${c>pdWK3E=8'
        b'$i~*~BE&J9z9(=j;t=V-ZWpUIW>x3I2P}z&R!pj4ZD8HRFLX-I;$5B67Pd)47G`@DW<Mkg=9)WE29}pGo6xIGD0EZ`twx7U_|Q2c'
        b'0u8?+Y;AX-zs(LuvrzMFVzaT@sLv-BWmi16IK~E}JDIIZtf`$L-f>`4Vv7eFoTYQ%VQ94>Ai6QT?bOY0w}mxZY#vzR=QROr<YK4A'
        b'I0e{&rx`}DWr5s=0G>J9bn@n#6~3WF+;d?fYFT1DPAL*ec05k3$MQvsvLj9}jsd=wzlcV8T?L~&qPMbYUSw6qsIAz6UnQ!uh3afC'
        b'b@oFrShzEGycM1K+4f0XBMjAJ(Q}%d#N|0o53Eq=wF*X@D=f%y6vBveP<o9L;mWlR^p^(rFVE5D=<}~G$|i}$F%j=<d)$D|xv=!W'
        b'Z!?--xG-54)R=!^>hwF1oERpw(ESFWegjdzvWd`ZNCK`>VQs>RWV`1})zw#P+HsW<7(T(X7Jj{%k2@d1OhWR_4Y(l@(?5nCnbah+'
        b'%ra(IZc&L)N{;6F8T-r}ag5e1A@_rCYhhbDb#f$!#$;PIY3__QhtGfa453KnlQHo#$)Nbuvd8I|T#*_~z8=4q^of51n0buBp;)a~'
        b'O^;zsv&bMtwh-)lwwEINA$Xi^;$sot#9F2(KyW4|w(!G*@uS$N*N{al7>!BjWdpXw3#(%sCSY3(TxcD&LTi%){k1p{{y#>mDB{Fr'
        b'tB(gJ#D##Gx49a92VQZ-Jx6^xCms*I%4B9=x`jGCr;N$LHQ;a|-0U%ztdmjRe<OBs|D4;glZ|smu#*jQ#=%bZ&iQY{PPWbY@z}||'
        b'bN)Ye@_!F@a%s%{U?=lq{&!<1u{r;5V<&A&^e*3xoh<U<*upUco{Wj1x9a!WG_Q$_SZHatqJ?jF{Xi{FfYq|x;vuE>hSEo<Fe)!W'
        b'0k?L*0&1@@6zz6%Flr%Fj1R@6QnplMYqO=o(y;Y)t<B1krF+3jMjGnRyD(AeN7P*4+d@UUv;-QEX_NXBv4vb|7$>)%-A38ap7S6s'
        b'3SdJgbXL!a5PH`zxjpBgD$ugB)5}J^*!qTc)3qX{7c5p(Z+W6q<diMYrtl*qL0-kC6seiFtDjBx>RI!5y31*Fmk5KE3iaEM*dOug'
        b'r*>bU_FSP}?xO0M-eq6nHqEQfeW=AvSKDYrs8W-fy-|_8K|$gPb4EczYor>pRI`u44bXVdgQM`EZw})@)l`!jon5cL6%UGD6a_g%'
        b'QiKDAbyfJ79dC~?wCAn9WzT!;o~3O-?}7F#e~AF0S=m|!5gJ}R1PC?Ey9E%M>js3{hXA2;p4aj5pos~0!h<H=f(QMIP2)k|)YU0Q'
        b'@StC^?}Z1=9l?V-Z^eVE;vW<bI>mDpWxf>;Iv?R33vR_b4(J~Q4{H7|#)IaLiwCveh6goVdoVocUj%LjjlzT8fj=up;X!H65Pr9y'
        b'K@|uMYNjEcJbfs0M&KTJPzDgnEgZ&<-U$zCAA<+AkH&-Ae<D2S3-^ZyB?RN*L7lhaK{0F;BGeh`Qd8!)p357-qe*Ez9gPQlqTiM^'
        b'9v;-b=ttl|&Hoj6(A;4>s9maQa6^hzx8Xs}2oD-_2R!H#?!yjQ;~aL#7{-Hk{fKib<_A8vqH4Uqb1V12gg!C)+)CDcU_$T0gMqkP'
        b'FroK8ziNJ<^Q-?xOz2&PQ55kbFrnuEVoc~0qtC8njXk>}aXt9i74yIU?8-1E)Uf$3n9y9};~`9_`7W5y1(@3Qgc}o@bvq_hCcHBy'
        b'bj}baln~z;6FLhs*`9D83C_A56Dso@jR_4O!i0*(!GubYFTDdQR7IOR8r3<X>pwLvR37EVh5mka^oiKfxX_;1vAEDvv2I-Gr5Szy'
        b'nBjiw?Tj547yA3yad4rz+ux6M<3j5ZF7&-v6uIAq3vGZ<j=_cMqHe{7<^qjwTxdPQg&vP(@KmF5p>`S<+HeP4Xx129=;PzyLhZ_w'
        b'oFQE3d^axi7qQHl;oMpdLivrtg&u?zf;|MEqonM2f`yt;tkVE~)(r}U0oFsL0<u_dg8K|6v_Yz|)0of(7{U0M(791}#e^<mFrl&!'
        b'*qvKu^yS9t!lMx;R6C<jJA=W5J`p>N3Ekz!gszQ6n9wz`YRV4ecy8@nGovp(b`&PmKYADwx**n#37sE11{3;F^nGALe>J1;motVj'
        b'p^33$Frj%f`XcB~b+NH-Oz6THeRAg3^w^&e6I#z;LJbTi)P6Ti=%U*(p#zV?%BucWOlUoW2{ka7(E3|3p@B2{#4~8n=RaqU#)R%t'
        b'QoAy9I(=vK`7)0$&%P%n6vGfIbXROm5W<5B6_i~b<VJ-$e}Sn+p+eC~IT{vfNV*Lcx@&w`=u(XIk;FJ6-Wvl7Enq;QowNUSP$(?a'
        b'{!N%r`zTDP-Hi#g-w6|{8p4Fy?}Q1pkHv)AhcTh{+c2T_J7PlZV=<xj5lpE4HcY5}3?@{GFrgGWs)xz<%5F!6I$6Lk!x&KL`)*LE'
        b'-3<!0j{=1f=24)~T#_JmGN4d%-bI`k9~3&Svt#gnMY|se?-%pHF}%SYz~3S68;zG+z@|~5szZ0egl-)kiyIS~^`*eMbv#Vy-f=OZ'
        b'HP{IG_lXIuaAQIZcff?+g|&9WkHCbQ?;mgTfS6DXgSD->GrsjMV;R`+qsQ`JhYNjTG%hr23@&tF#gD*+-Vgmh78feL4Hs&@D=zd2'
        b'H;y9fb{vJQ;78*^<9^(FlyGM#x<j4&#Zlb09v#9_(DOSEj^b|X(Vq`KFpk3f6X7VB)hI$+?PTV1Xf^7L#jty<M^gqL97pk>>(PG&'
        b'M{$?6s6BS@$F4>169e)u;6lyg;X?1Q2t+1tApF5`q2`|$7y7sx7n-BlG;<6t^dN%^MWcM<7F1}xYTDhcM^PY+3awXB<M`1#<3b<6'
        b'wgVCOiwmtEgA2{2*J7|Xt#{)>zm1`nEDeQJgBurG@5Y5fbk;C}3#}))x_uE0hExp?#>a&sgX>h>0k?KHd+Tv`T<E>>!I>X09~`m%'
        b'zA&Lr-C^&~`G9+W-uK-5lYLKP)(U<~TdPXAA53WU2xcwncFbDb-G^bnL}S*b|D?9|U&V#q&EB576&HHHTbK8{2m1iH&_yw7%|V0<'
        b'&51$wXjs2ueuRF#`>)|b&Hr7v&^yL6cfy6<EuQJR`9CI}xfd?<Zt={UH~;s>GtCc%3yt|Pd+T@8$NR#CKCV~h+!Gg?OXEWA_kjzw'
        b'-whX9k8q*&L%7iTABPLA|IxV6dKwoxS<&}s_z*6%UN=?oFXBS$X<X==Be>9dT|~sVxX|m-eN;G&3;lY=__)w|DOIne4x&xW`Vm}c'
        b'{R7}aA&{v@xKR7;xX}8sxKNaBkj919592~nume>`<3hg~2N#-)aG`b+1V&?Vq4lG1q4rU@(A=L47it^Eg%<D_Txjn-!HkaRdx070'
        b'GdjQERRyRz#>0i?4&g$J9|RXlAHB)tp|dRe#>Is$`*FBX)UG{?Zg=~wxKP6_xX`&MNWUj9?epBc+<Z@7K6PKbw5t#=myZR8+TFm='
        b'IS6kuJ}%TYj0;ur7+h%nJ#nEK(Raax+8A8uTp-7wx*IOk?#6}IkBbZahIK3d<7oaz58*;Lj>3hmXLSaJ^#z5w-;fPPA<h5jAxaYc'
        b'0Ju<Ecoe7;gWqUe=&mui(4HTO3$@uJX!=?B?YPjHhC{dELIXz4&Oj)d+izHRMTUM7H3GYOT@}g#TfEB+4gEN3TxckdhK4d92cXd}'
        b'HU=3wK=E<~YeykNcij;gT3C2DWGH7_sDT*9h1%S>&_G^p_{t$%=&pO<Lfs7T<K=!aE-rLm)ID&asDS}rUhWU0aG_xS_rZV>G!&u3'
        b'{(>WDXvQ!!G+`7pw0;B{ItstYK#Ob)F7zQ7&(a6Rg%0bT%oFKd?hp6Gg+3W|7hEW#bwva(clqKmxX}9h#f854z_?JG8y7lA<OVDp'
        b'g$u3!S8$=WVO;3<L~iqfABhVcwzINpG%hqC<F2^SNl|yfg)(i~FB7@#srQ2mtslXK?z%5rD2Sps#==)<UI0-<n7fg0cIbx{=Y+QC'
        b'Ga|P(aTG4JeiSZr*AOoBu{+~JmG9%o_PJZfZjodA1>pBM*w9_0v7yh8iw$KsRP-^>cMojn(HVEfhOQlj4Yk=nByvxU!G=C{7i{PP'
        b'1{+$R;a}kaq6?!!%={1^0*5jqEP9W~t-KdFRL#`=3qA%PYGYuJy+rQD5qxO5yw4yX!G|uJF&;j&{{HZxbU1Vh=(|6BsGH;O06pX4'
        b'Lp3uV03TX^FMKGnmEMKaA;wtV0uklY5K%YQcoehj9mM@%MBDfV`E3}{gmEyU;~5IsAtE=^4G>Mp83!LaWrjTX;BENOv#!y??>MQo'
        b'w-KTruBifs@SzQtf`;*-byvrD$WzA$ULz1b^dW=}ZD7!$%Qd=&=?plOc=0O2hISXyO&L6H^%wgIQNo~;4P_dt(07G8a9z!G8Y6n!'
        b'S@r7a^jY=C(LwVA19=l@xbdq}KR1kY#}1R`Rr;OvC?Ki1q!Cx0y=wTF0g{?&AgN*MHK*hnTA$g6prnT48wP_LN{X<c8LWI^p$6AI'
        b'h59_r`b>D8>cD&0cI@Wxw+C_bN#YOD=l`-*`XGO`CQ+}6*Zc5D4}Er;af?Y4qSu5P>kBn=^_p<KRU5F#c6^auBh_nUt2B>zYb4&9'
        b'U|lI{zn@CHK+U~EJ<?{?_HY7@qU3Kk76^8Ifx(RyJm6^2x$ibzu_|{+g{t}da-0u5(Ml!Kg@lco9m&znpUwa$5pGh6uC198Q6;7i'
        b'CvrovqU+!39+_UggB#~dAWUN-eI1MzsJaBWX2s2ffoRi%wA!n&pQWUI#wX1cIDz)o<)vYV-`(x0d^<Hwj6TI2joKzT8Sg562>ok+'
        b')uwtW7ZUK>Cp{&DjlKqL)Y6}1Rt9l$m$6VGn-&V`ZCJT4FY0wk3vPenI{I*P5~u1t5)TUsT_}+hge`SKyf^s*D}7-`P<jf9%XfM+'
        b'6s;@un2$4GdERt|`OfnaJUt~;Ns?(coOlHDOg*<#*#EX~ZRD!szO^+*ywO8!)GqHTPgwCK?<Q%SFz>9k^=iRUy;ghe)X@T?zSVlI'
        b'+1NO-we_midi94NT3>TqpQv?QyWDyWMz7uGu(n3G8?~3C;VEVmS{o%z6X$*PLEAy2M^!pH%Hx@8I(efemYeYyiW!U^q7#Fv8!ilk'
        b'!DZPcMVYK!0Yssb)pp!h@wP8XnmtdmtF2diwO3CyYnvUtz1OO>*LsZ(Yjt$3QR^7$#we-qoEJ0iXlz^0xnN<qJPxl~N*^48{-j+u'
        b'<fuP1UvaqTZPZ^65lJ$*Sk?wzoNhC&(1_w{%Fbsb=Vwc)uru!l3UnbM2*_H~UE3Ery+_by{et*C79S8F9xsSbh^slw-o35VhxEZj'
        b'Nmxu>nK*vh%6*c7D_C3&NtChQAHYbTc$`WK$&z}7WjiqpVKw8jDSdd9(o4QGR7r(Wlctv@hjEg9r!QegrFs>lO1gcCD>(5j+W4S6'
        b'rt7J21Bs<4FUs!3Li${?77p6{@K$SlbRR_mX=hHUsZb3zo%Dv1VcfC<-F~VsaEdiOjIa6(M{%NeKjm|!ljC(>0<;z7u$t<kg6+He'
        b'qrZzZQ9hdMk<~F?1q&sL{j3Bj$yQR{3XPxB3riP<vLd(;<Ly;sDoc}-><%m-32UfJv->6`71+AGG2bLCr4AD$6<D`h_eyl%B5I-s'
        b'B1yjmg7$@;pq_r6@5%ZuL?ViH>*eSO+quZTbCJ5W^!48&`~DWGdm3G%51lXZ)HR|OI{zBk_t!|>3i;5<G*r8kDb@N5iSA{(P=~Cq'
        b'L)N6pIw(nku4~Y}_iI^=8s@TxbC#>yg|4bH%^FXOMML^7(gZG5Y9{B!OpiVm+54C<Go~vD>knetDDO7PM`xg$IE8uUkVL+wP%~Kt'
        b'x<vBzn#plONsz<SM6xY?@tv_v0{SQw$%*gG=v$=O#buTDk^IHQWqoRmP_OZFaximesD|W7EDlLjfu&QS@ltApi_ViK(kD-`rlE*X'
        b'AHR`*o@AGv51IY5iz+{oU-5NFNc5&Fq<@$$>}ku_fxtSE(;r)OKIAbGDJuIqBqw~+b<(3kSMhY9)CAAGG15EiYoqR>Un1#m(OI63'
        b'^nlyM1Pp8e+)me!-j%81of+^%61EVWDBM54==`Ru@n2`?GN2K)Mua{@U#cs6I+9pa1EyyZnF@ErM~_UpoGL6l=6iTjN!#TXo~#3F'
        b'I?(+?-}*?9{krD5(nwu%C~zvY#(2Q|bOla+LVDM{fiUTk7%$N`F`=3U@0AkC%wC1CR6{L~Opq4Lq|iB4Qku5(QK~c&*nL8O+5{|*'
        b'ikhigj=0{Gd?cGxz|xktbkYgpv<PMt=2iD4QarJAfnbSeR5Z1%*nnZ0MUlB%ZZ;+#&ZcL0F{<tK1^b~Pr6NDBHmM*fYi4heFnd1g'
        b'XL-&E?&(R;Q&K9W`!K}aQ+8S;NuU#4yk%Y|xcxGgw2P(dM^B@cN|KVPZ8^C!2dh*z4W~`RHBpmAWgJ@hC|O@5h%%z=pJ<Qp{V(vi'
        b'r}ytD)m;?f#BYIwPCr>+G%f6k6E0oHP=8`+y3Rm<XEjcf{xlf>|3tM<B%jXKy@ASfddm8OBXzH#Ybq%6OF_F-az&CG%<bgJ`Xn$8'
        b'P8-F&pb<+ofx3Mm^!ZHjS-fYWO*5rU6QDcG>{m`PQ33FvApj>-tZ2KeXJS-;R13euL)VK6><aifQ4CfvxK}NtIFaVB7fVmzr@ciM'
        b'vhE+j2mTNN?O%cRiAbjXD^y_5#LIt^=(eE_OApvIzROeFG?SDX|HIjh$x<gv_ZIVxb&Bq2gj-P?lYvm(Z$cP)x+q`$iKu>Rl3s<O'
        b'Db&46)6xE9-JgRG{567}zh_WcC<vu=4fNwv4;NDY@?E$y0qZ;-+;=v@M)|f;lUCrmGMZP8;J(ulKn>7B+l6IATvmPP>Uc<3fPOAI'
        b'z!b=oAzF1N)bI*{Zu<zGhqDWvQM$*Ox`mHnFiAOiCXJr*?A#aJx5?dUQm9s!88WJpP9H&^o5oeyZmR2c2On4&k;v60k16*IJ(f&N'
        b'<$*<VJe7qUEKhWeSk1!F)6U-p_w9?&%^ITI`4<<&Y~BjWCoDNW8&vl~919)#OviSyy(vpX?@VEW6de<{Y?o3Z&^euF+52j&AWX8W'
        b'3yV9Dp1geNqU^F{l>m!-I(JJ{=epoN6O4d=c)KnzWJuEJ!KXhxm-Bw}bm#A}6S~ve-C9<Gp6D{%OiHI^6P}8LbQ6Zg1SP@c0LOUf'
        b'jxq(DQS8oNp(i>##9f}A;)DqL$ZrU`K~IkY-N>z7z`N+}oXILZkhV*h$c4p_3PZ5jI8EY<Dr|&BAFDZ-I7gj|slq^CIv)$}TM{uB'
        b'*Zo6=W<EK%FDV$pG2{XQ>1HdxaZY6!zZRV!%;ztLiKUcZRiSimOn3}vTc|K`Df$cw<rUiL^aReRDKF2IG#Qcfm;)>{#I;^}N?35r'
        b'amuLFc<D7lk`woIXy^MW7>&3$QKXuh5M|LO<dEVPo~1Lt&t8Mg6`=TvZZqy{$*-a%Iga;_gZVG`RdfMdPGT853)CrDMhC3jD>}2J'
        b'j<P-z<t57CsHuncUu*D{bg+9kExe+A*onFhfi(fSWBX3*aNQC?3(x)^SbiOlmE?5nX1>eZML}>cKrVYPC>lf_EV!2a7L-f4K+xdl'
        b'+ac)TLp>X2KEFUfaxaF>f`ONwhpUhvV=~FjGY4v1)6Cg52478aXbmxOQD<qNI7eKZ-wDpj%7S*t08uEbG<8lfLQF1e6h#pB&6u^p'
        b'VeV^gvRYGjw?`1xVn;*nLxE1XTiV$yZ7weBG;pvGm2V4S?6jQ<Y&M$vDmtxFZ8NN*CX{wIh&&J1^$>{cdaS9=*w^4Up@XA6LB}38'
        b'6i_3Z8pdv{OL{{x@Cx?+M!ZyWxX!bfoIvhx;gxA*OEII){B=`Z#nV+sI@rwZ0S$0pPw@&*xC%-o@4wG6pKpjyKXbZ+bCyp&0ndL0'
        b'My5m1SU1oB0w_lOBRO+{@uE#vvZPUAn$QDi+T%5IIYv$Cfy7B-qc{Y_utGy}2?J*Sx_d+Efh8U)^un{jdjdqEk}gEC49$8}y+oA5'
        b'ZVO_8JDiV23cB0-4o(AiX!}AnXAtHoh|~5q+0~7o>lXg8Syvu}V*9`j9A<h47J6XOfzqdq$;)%ZQmvMg-xsD^!mj9?D=_OC>pU$T'
        b'980n+&80sT)%0{@T?bdMnPRU6MeJdBfTY;>KyQr+=C8q?b~nRwe87xs>mC7W9m<+C0YK5=^I-f#b=9v(4tK)S)@Dg}ZK9>dZ$X17'
        b'&p83x^(NMM{%~i(a!G5k<kGhd{z?$5E-Q;}K~{lva6r0%RH%9}fO9E<S4t)BD)D=$^l7~_8df?D{{HaWEHEY~?kY^jR8a^LZcf%`'
        b'V1`)CMDYtxy1>Sl_SJ}<K3s>U3q`;xn0s{H!ENEizUVRV7`8+J`oqDB9z!v{b+Lq**rHTmuu&&AR_F}vF3d&=KrCdlVUg|$Oc94b'
        b'%hiPr^V2mA-iPbXa#0moGPJz{hm|}=a+#q(k1&>^O)!?GI=g`xO2DNrc%MxIyJ$X8V(~83h>OcKiK4;`%;|w8nvvllJPS<(R_=dR'
        b'Tmk(M94yfTf{cO?Nnw{uPhd5E-=J9-n1$_LTD3KH5`hLIn}v0-VQOZg^ZW4{Mnml}&?SNFMyNuGiR0ou6jb>Bm@u}Jhb4=qsj2Xc'
        b'1JtBxRg;{aHwiXI`AjQ>Sp7hih~V7}JwWGHYQYEI;bn`%SFq!_Jw*5G^luU;M8NHCHHnFGuvN$3&YkQ^{HS1)V~=3pi?OP2T|K-G'
        b'!ot#-k<6J{mjV{CH|E&5SWT^;h9BO78ws&YyTzf^Q~G7tKo<|KwdTb%vU3;TAU<``{q`{VxWA*n#189TiZ_k^Z^m`pY1OYqYb)9+'
        b'E412ZtI<(s4YwZFw^|&#%CI_DI0}%PEp>z8&Bi)Y_<3xawaI3ECE3v~v>tUd1r4Xev05B;+rrU9J9^mUV|~SOj=pVSZ?6iU(^y^G'
        b'X8l8SZEdxQg2sD~2&-Rm9QZuEy4lfs*w(bP_0P!%J`Jz?G`#gKedW>C{$y*5?c5&JReN)FO|tIqbjh8`T8pg@u6HI^*E;Gx4!2g='
        b'v`r3cU2<i!?o7C~F<Dz-t2QN{v)Hu1O>Q?r&1$2gw^rC}>9xS0b4P^j7PxcnGhyXd)4uBc*w%X}x%VZw>G)pwgXQZhLDMXkEjICK'
        b'Xyc0g`|3RoGV;?uur{q|KYQ*i;i;qN{s?~@M}^Ht$-p-wStNPtXjffy`CB~OtAA=X5<<-C@IAA;lNI7PWpfN9pZk;Wi|%um(4TH0'
        b'`S3fnQ#=1DLytZk^~ljJbTm82he^_UX@~yAoG*+O&*&R>Rvsn!M;3mVVu`8P63KSwb<$feS4!R2lr0>7hT`-M^!w$pztc^Z9=BP&'
        b'bpIhmF^H-AhaN%SuJF2D;ceDpT^n+@837sL83N^UcDl(pv+6UW>0FA?7?+ve$T`z);A0Vi<UELEw}qqnGt*7!GjsReBn1Wm7Agqi'
        b'(7V8-81qTO=GFb;7z_}~YEfBH?ag>-8CD~iVF|<gKZu@GM9;iY^sEZ6TLtt~>RuS3CnKTin^04_&$;J>>59tKP)-;-p5q>KX$l$8'
        b'_O@?9^TM^2K}Jt)_0=Q`+O1e@NiyoIv#u>RYO}6YSEFr$T4ROhyrZJyob;fykodzsEx7oo{VUf30o`$4c-`aB@j=~6)bWXwKfcbG'
        b'cH1dZ=Y<HQzfF17HJ39l<eXF(9+dAbE-qZkK{J7Jq@{;%dl8hT`ghS<9R&hKdXoNh{D0XZ6dx@Q`wq12Qy1M;Vt8FVboD1)4(h6G'
        b'F|746$z5p;q066H!OM)%TLt|D*2C`*^!N0(;1w)!anaW<BP({-r;20O6Jnhh_DakGVg-lXr{ZEs21n(VejpE(?%@HAU%AA^c_9}^'
        b'_`E$>Cece^tyW{?0w1JSukBO9;ab|o*BXV}#mqIw0oM>P7&+6V=ZwN#W>|!2U*JY~Xv4NJ@?*qXaBX$)?$1eFe)<VAtcLHQ)g@O5'
        b'NN<%7rq#n$q=(ZB`qZ{wjr8cA1Je))6;|iwV{})^+Ul9~HAnj#T>H}3I8@|)MnFSiX;pfK0Ocf#U~(Qo42Ij^V|ezTVRe_n+Uk;Y'
        b'e8e--FMe@FCOtyneQC;~)Vu~_341Ol>oLjtl+sjV(DJ;)K6#BS@zEB%sF!Kt<FL9j(8Lnmcfly<#wp)(2ZilNB0WexiW@5MdD26Q'
        b'>(aM<&#e<GkNHAqv{Ao&Ss1HASVlQz5Ig!}qFl~(R*wg8^0S9dljpQo3yk{Sl~>Q5yH@a(exotm*xP&UqmQ-cu6=R#WOT0t?TKM$'
        b'h1%yOr=#b&Dkd0(^Sa9)eOvk@*5%6*k(^Ku{oB5qJ;(`#e%O`CEJv|kBDwlQ@kj4tD}-P2Bq5TpiBdmS;lsE?s)v@BOG||xN#_~o'
        b't&{X#D~UT9#+#Qq&tjy?-@u8}F2py_oQ6rfwm;qo^%O~6`ELFsV@X-QyNh)7VV*fC&&;9|TohhOY!X?wYpx(kNr{f}7MU(R7AVlY'
        b'6h>=eu7Cyn`fXTUHSp_I-7AP+`2qRi`GWj}Qq!W4?twNNENKS@TumV)u|!ZNAPG8l1#iz=HVNWgF0lQgYqOw(4gC~#x>m-bHTLeA'
        b'jojSkn?2kP^!yW76SquYxZ<LX8O&o+4%Nd+PdV(9`IvZhX%K<-B`y~W*M)%YoMa8W?ph&$StI!^9v%D>tnyux`<92*m4p>IC2e&d'
        b'>hy@pBLcB;UUOdPx2-t~(O@l$Qh>*B<!DV^ylDR`5oBw(gA|<RW8x(2Y@M}5(&W*|pJ&9#B&&7%JWF2O-<v$DzL>TeTxL4l&+tI^'
        b'u6nL(!8fQn*!DMEkpwN9Mx{9gwER-(Ig3!*g?1}zZM8ABQ#TZE-#9EVvunhHP1kGY@JT=P@xOhFPf(Ubs0Wb+TXw^>L~!P#4grXF'
        b'gR8r?FD?v)l?sSiNbj)B{KbX{WJyK4HeyRSB(Z=!mwVV3W&f%NLGFvB3n$fuh3OtcL;fuFL`whLzDQ&Tg<!DC5`MUPsz(ZpVw*XO'
        b'CRDdx&C*^?II2DB$jU<7r>#-ZuvSShYNMiCTajICHA?20K>W|nOO5n+XYNUYj~O}hQniw+2~tT^G-xqh7-SO)ON^2V;7O#%cQZeP'
        b'NXYXm`n;NGq3d%-+~_^@bXk<qEBedO1mj%(ML%Dywm|z_wAAWTE}gKQl4AU%>Zk({;}Dqs#HGM5qFtdTE2})5zkLmbo>gy;^q_gQ'
        b'URl_Mv~lBF^*cAxxe<5^NA|kQDs_ahNn7-Z(0$TrWSh0kfq5n+Nw!CskcrECle_Aj>ry#pJ2eSyT<)!drxM9_l@KGzyf-=Ocdnn{'
        b'+D=`I+9`RSd~10GZe8WTcu5Y)c2xR}I>}K9bs$volDjR%@f*@03_aRk2gRTvNu|W;az*mzdbr~^Qe0FCQPdfM^^~OVcxc_*p>6d7'
        b'-Nz_2i{2BO72}olxV?K8T0&wvXQ(zt63=?;xp{RN!hvR2x^Q=`k!6i4Ku$BRE-6NW36iwh?eXdg7H~I19mgU=N#CgS9r1-3%DEgT'
        b'8*5<|?Q_MkY^NmgYSJfOxqFi0m7av0=A6WZ`GmFJ(ZmD3Dqs0iW;6KiOl1?%nA#d6wExa!jd8^DXqx98Xu)M)xK^+i2<CdW5KBBe'
        b'ShCMun{i`WscJo|!00FinLsK2mK)J(zrl~^FtQRBLEs1fwSRTcYy1tNbb`>io{WtNTwnKm=z*o7^3aL8<)OXcAVX31DOm4!mWTG0'
        b'g-W|zx^F48e(xW2*P>;`bBlH>)tD+ag3B?12saBW_03Jdt#pvG46w=j;;)h%&>?hPuDCu_&(!4`s*Ku7l}m%<jnb&7)ZK5N3l)Zk'
        b'HR2dM$qKUx3{}*T-m$e)k!5@yM`_<Gz#;2T+z91&uPTqfM&jrR%BYEa4cUTIzY0Cc>HJO}rT6M!?_rlmBw9~M-g>fgXYe~)CU@qB'
        b'_ALt49Y<qm)q6=_JJkw8vJ8{%$3eKmjg&g{1V>`=qP~z<R#k8$M<mQJXX{vc8wa#kpG`<Lm{h}2YNTpSP@yJxl}4shAvWq#L#0-0'
        b'#deZk(WlpVZ@R9}=IO0kbOb~k4u1kjqh1r(By7so)ynDjT><XhI(7%Er~;>Bc)Fh!HgpruQfN3MT}0AdObb<@E-qNLBp<az_w>d2'
        b'P1h6p$UpaRI#?|@^m;)f?$-od(FDq#!`=F<!8%`}HnYjf6+BoqiOWwNY4gN3^Q}j{a*qy1e6Y?UFo8oBPcxuZM#Q0Y77qNLW_a@3'
        b'lC4t{i4uPtoM#~)TV?&*%3`l4%GZf-Ll9=-vjVx(jGG3tp1MGiWvr~ht`;(I7dg5AWH0&h2fv@xfAS9>%qIFzo<zBz`cMAugW1vj'
        b'C!6wGrtP}K+V`l~`a1_nR==~Q>dDVoU9Y)5nC@w{>w9?3Eub}<ZU6ydqv4XPm?R^D;_();`#t)2mS`GgwHEANT}67v#Uo|PJ^meO'
        b'cb;|SKK32C)%jP~NX&GW3p_z5(=WS5?AjbTogeosr-uzu*2w)?Bll%r4&DFv<!4Nl-=3c_Nj{RF@e%nr`56z$|J(92?vVfZ{ES=W'
        b'|35$D|DODef%5yw&*&}x-<_ZFe8~Tc`586XW=?u=)f?%&3>L}B5U$`5T=YV5vMK>fXQjiPbXKYFw$u!k=;EL`sOC*v6^z+@2<2XF'
        b'S|tMVn-?x(A5Lj~%yBtiSeujeJMQ9q@y@JlYPqF4=b3%WqtPNjcMUD)x&sUovBN1noF+<VM6VX0nYLG+ZEf~yvuazLCANixnNsmF'
        b'w5-s5jcV)>oC!ai0>94C%fVwAI67O8VV0Eqg_)M59EXLSAGC+4d6Tt=I4o>r_jp(+-8SUA%~X0&b*dvHD4kuqGhJ?B7d+>vkmnx0'
        b'qB`M{`VjLuN%X-G7^pmKGJR?S*>bKz^OBx=Nvhc`^&^y;TD4|pq2|R^nq7)cuXTmtq3M^@Hfr~LPhF>sP9gbHlSflVce9?_O?HLx'
        b'LD~PzQ&2C>$HNvD)>W(N1daj4B%Uy9)73)fvQg<9tCgBmsb;$ZC2_P$Q63x{`eKyk<t2EbX0Md0MLt0+Rp3}visJ3R<_5X+RIOIw'
        b'5Ct*$8qEn~^EJk!v*?AxXVJ~0@-?Eval6~7mx|82ssdE?JZ0S{?gNQtJ@s+|gd8tJH{CvlT|9II?n9g;R@r8f{KAxkjh0Q{7HTYF'
        b'<y@{_vu6cguc<L<e#hibUZtre2_;o4eon8cRdTTNq7c%9tc{o-(c+{Z?^$*1+!L>?JBq8y2^8J`W<Af!!*pbbUSl-`ae*k=yMuJ@'
        b'#(LeLjDFo{gPQ|=a1%FCHk+nS^x^lS=I@mPOqBY)axZ2$gbkhaPso*{^o^+)=}WZ1MAVWsdJjx_qBrdju3E_xXOMzDymK3c&HIK^'
        b'6LK(d>Z%jH>yCUHk+#kccmCO(yYZL2Rn&Hrn$WYiS%|P}uh7TRI=xoeqBd^&l0^6+>UUkXqzx!H9zLLTH464{ZJIqGAI>RQZ;G%V'
        b'*tx*zk6q~WQh$uwWZr@QoL3oGo;Gc^_>DHrc72g|xtvhTgvhDwlXD`{Ruy@xshz8+UA?KojXCP$Hx_ZPKpQ_-Yxd-GP>woOgR7JY'
        b'fz_x&s<OyiN$pfqyB4P^kKIUz*m94O+Ox#t{bQddB^AIgGF7z_F(={>Voz#<)9k{~<gA97`M{TJ(pXffh)r|~N5rNhxFMWpqiUyR'
        b'-kQP@@o7{FM`Ej+PreVvr=q7&9!E|K*BLm>Bf}7n+JHxNn#;6^S>j_|n(d|{@0!pd9x-_?X&&im9#tY985tf`aA?`4E4W#N%HP5w'
        b'BWKgqr1XVKjb(`dB$dc<wNaLH^MviGm!Ub(9g7krbA(6wW8g>5ucG!C)Gnn}Yj_xIqiQ#MoGTY@T(3OVdl@8mHR2@Hsa1NShjfjP'
        b'-|@u>l`De1t{x};M0m!MBIg{Wq)Kb)Du{<_1PEDFtF&PT0-KK})r6isxyl2c@etw$`L#ffiK<CL0IwQVge!uhhhHd<V~sP^1>AmX'
        b'?YjC2y)g)2nGmmFqnvjL4`GYS%<Q+#1XhpE<$+R4<)NH+kz5#rShmhCfT}Q233EU;VV;y{@WNp4!0YpJ1GlUToh>fcYqqPGdFKTY'
        b'ieQ@WB{W8DnYV)4sibzH8H-W8eIuRS8!Jqho54<EFt4Zv7is|G$5x<A1C=nv%8yx!R4vI-e2gno5)4(~wQ2%6%+O%ON@{!F=eSCN'
        b'z4c~Vy%$i4fKmyi?Dal$4%0SfjPu-M9EBmpTi65Xu2RAJ02t)EFvv7|kTAG}L{%ULBrDG1>LBk;hF|9t<RI|qnm|KZXgo4f+gC01'
        b'UKc_rg6Og4g>WLas+S_t)wGN)2I{XP6406NpOtYo_^OT~JBBK8p%M%i)p<_2bkuO^3aSHi2H={s(#`vcw0d%A!kk(LDnic}oz~_{'
        b'fl5acO%BZrQHRkwq&S1G3i76N4s1<p#EBgkO>*H<?-CggdS@_%GET%}x6*tA23^X|TtI9^G?aXX8>VA#<))3uP2mpAP<m&%K|Hm`'
        b'xC(1A;#Xs7Qw5Ae8_3NtVMDwepRQ6it@C9ZZE=vZ1fy%X8Hp;Sj$z~tMCC6TKGu9jrwLg*dJK1$eKdw5xvOwk_S0^a{eN`~1qDd<'
        b'?==RPBp7SNFzp~p36GSrLHV&O4DCM$Irtk3?lWVcQ`n#h5Q9)ha)}Yzl~8pi*h?l0-YD8*?w58wEf?u!$X?zqN4Jn($}V^|dY2qi'
        b'HE|0H3P@j)T`+UU%9RDc{it=0h`&HsU<l`+*+IJd8Lo=P-YOm?>v3$=J#16a1XrA31y?l{;+mo~`^2I7iDMhwawdg2l6o_k+qBSG'
        b'^f=Xp-ZbV`I0|#?Ev0rUX#3=b(e?%l!z1HycMcJ68ZImxfeX9Ky9-OHm&4c#aLJ75Fdx;y@${B>?smO}dx+{`-7r*)Lo?`Y4K_kH'
        b'52zT8{T-ifqGCvIqsGcSFouua!`@#X{GY;8=|UzC6{EidGZu2pSne_uNt>kTAOCa4l0xU9a?3ZZiL`tdG6PV#vz9XBXkjx-T=ciw'
        b'=m!l<h;!4=<Psf4f6Tq;w~e7coTmS7ay44Mmk_G2Zv6XvuDx%N@wux0pV;RT?f2(%iPrIbE-{|Z)!yQBt>gP#(}Vlm=kDZleK14G'
        b'J^a;MgM|SY@ynma=N1%Pbr#>#Ujda%Ms)VpF@VpVefKfQS_i@B5|KaE7*;!H-G|RLL=5Yy+u?$y+{54Q9sKY1w<HggQt^r_%Hjpl'
        b'Kgls<;V9zIT}KbZt(+?U-4#=29vR2F5w(PI01uUCN5}iK?iKG}aL4<lbiDsa8Jn?}cMtbV*$S$L3{HxX!0;2f3Qf&+AF1Lru1<+l'
        b'Ti263bxJ$}P5a|YG`6&nvBlkGY%Odwx}r)jsAJ}6)Y!n}jGCia_d7>%Y}(SqGi%6uh*lgM3DMthlB-TlP*Ro<&XgVw>Dj{8&7)|5'
        b'Pg*T*$j76a9X42A=i%rJY26gPkzpY@#6o;L15AJcZb++tXtV)Fc>wQje>b@8uXFEx+uzt9Wq%D-jP)Is-8<M{gZ>WoSNEgWJcfVg'
        b'n#bp!Yo4NIwEcb1H4m5J<vJNxZ4JJw{Z+-^hy8^>Y1sbGxZVE7-oySbqV4bWpUnQ=*P4gqk-h}QdQcl&G@rIzhW~Wk(+1CaU>i()'
        b'<hrMR1C6~<YWqcr2|>kc^t6IHVP&(cynf<n1$EM<s?Zj-{QodxC}WK>RvozgQMY~?P<&K=tA47_;tCnk&zOQ3ufXrOJrigs4~rF>'
        b'O`xAew0<)CUa=u4H&xNln2clev+{*9{suo)J4RRGK@}zk)|fiO6;!QsPV1VqGSJWR5wlCjM?+(AkAl$BM3cirqxfjV#(t0Hpu7n;'
        b'KzxKqzN>yRG~c*@=ArTh0wt2EDfyhy&vII}X)-|aRV8=lX;C=RPv??bXbTvJwy@bFgxx_ujYG2S<|ODRar>Uc$Uqjm_0ze8;bYC`'
        b'OnfwY3~Wp_`|e|qJ&g3z8S#K)xPy$}K8DrA?0b%ZjrxD9n2`a{$b?7futLw!T?!PRW_`)OB|P$GRP$kMSe%(1Eq~^NETie3b-#4C'
        b'(K4~EjPD%wz2jF{JQN_UoGsb?F2onSrG7vzL=`X*iChRRlqvCKP!zpws$_zwR4*l5TTx0RwH2d_TGS~CAs!)Wq}Vlz*Pe|sdVwQ`'
        b'Hc3CyBg(v^I%;+IGf=ELZii^0Z;0=FHMO@mm>^Qn`8IY`IjbNkxL|3r=Pc#1sDe_-%4d?5DcDMbB$q#^Jl0E!n9N!tjt`K)`vj#-'
        b'Q5+vk<Uk=J4a3fqlRHXce8H3zI-?YSVHKwQy|Au2pjh=NEl<k57|B;qdy_J}oEWx3u-UUSZ))G6sVzhYPp{dhE0_v#glCNHRFo|R'
        b'<-igfMI5f0sw2fVF4mn#zF0Dg)xlH0##+3X^dJMXPHs6wMwQn_>M2_rRj-Y4^zhLKP8)P@Or-%^btbAo&1Y3tNJLvvPIc2smPu3B'
        b'nJ~4lcDPT)6eizR?x){E`v-Buhc1IJW&^656{nV|DQiK}%*@A>9H0vZS+FcQDUDUIOtNxy@=BE?_r062j)Wm9G?sv3g>%`N)md2_'
        b'wZ>9)jfo6Tv(zbnS86N@=TZ~37s9D1ivzuufY?XGd4$OqrleC@eS|BN36Wfdm8GVeQ(CdCXl)^7frbhmUs!k=FC-GG2yqVZk(968'
        b';8n$&mIHHKXnn4r)GJpcFj0H5DjXO6aFq-ToY-#*{^IM8Tvs%|b3TM}f0(~sF}17P>-z~8R<OF3ds><sDx_W1@7k!BY}9Vx!v&4q'
        b'K7A1QaDlStele?!&WqB1M1SIPo5l=6Z2K#2ZiZ$~w2Lj<I?AW-Kc7FfV#+Dw=MyU0P0IyPsG;KFE?e*wgx*JOp8B&rY%n)7T2HrB'
        b'iC)h!&FBRQA~Oe?GT9QkQ1Z9mwoxzC?zT)I{l!OXjg~1D?MIp~ZsTn`+pjS@>C_$<h8z7;QSe~y57U@NwJ49hSyYZ1>$0WOSyNs('
        b'rK^}ghKenf>nf(K()`w>dEsKk9on)_9n4LTucEU+twae~%pn(XryN6^EOT5G;m%+zaDvGe{83$PElOd4U7*ZufAl&z@xzDPN<CMV'
        b'3L45Orm-Fm5W9Yjy(nN1WUe20*i6~#J^^ktzgFnHY}1&BGO3t{lT`_(mPEFgC^O2W(q4Shqp;Ky$~BZv9hGPawJn=8n0qR)kS24v'
        b'5vWA!o9ejei#vm`Ko7kwxVEmclBTbpp>Kj^N?VC%VTqu@Fhn08<`_sU@<MYAB<40x9+OPV45Y658=|jtAJBJ5T-<r#;k2+8J!M8o'
        b'blOu-@|7hteeNte%p4ba4(1AcMzZLbm6RD|HlCxPep}`{l>S1GvbLa9A*WH!78vrjc!GzGB;`VF4G@F5%O@)61RYUxv|wK3pG+>K'
        b'_UNgXvvL<MHbR4X&C8;1c&cEGo}mm!gYU<I{8hH#%DRmkRi2pblvjmM(~+{KZ7~goK=-(jj>}kR(7BcTk=Bo02GKK}!4K?vxU}gA'
        b'yYYy)I4!gz!>2hl0~%;BY-KWkFpW5Rv;#M8iUi-Ogh&QDy_Vq8x=%<>_#;Zq3knddtm{x*IV@PmWIx;#Ex+mHqTCiDZ`M#o47#o3'
        b'TG{oRdg>(;_41hH6fdK560lklznEsnRr{{1nyxdy?dbQV>#DD=qnwi#u<WF72pd<G4;tzRrPRyrb6RFjU}eO7LVy{A<{dr~bSRuK'
        b'`p|g>%fneGgN*FMLG9?<aEJNmT+-Gfe6gj*_AWZ>pJU;Ka+!0EEqF1Tv*`*U#`L}f`T~d1%lw}HaUv>fb(Cba(RcUv=1*!GCm1=N'
        b'#tM!)9W(k8e5`{b<Kv>*LE>u&E3w8@GiP^rO}m$8Q=0&jzr=6ih>aD#Dgx6l^HQg(^v6=w$5a*X<#Wh5a+2k0#V7f`^cls&@9zGm'
        b'{_WIqI+w)Dv{4T7BJr?yD}3aBgz=jSHo?V0QzH0bY`E()oaACC_e0VeeHiO`P9$6O4tFlkIRWe8wBQw#Zra1pR3kxpWHvVujjW`%'
        b'9TrgsaZ)&N-IXadQYVB}%^O!ot#fGCb)n_)TrypBn24R}=wSmLfvB=kw4R7EIuh1xASy(gxsmiaQ_l0e%`9ojdJ<QZJfkextS(tu'
        b'Sn{;KWR<k!DQU?jX~}A7$*-j)8>J;{r6n7b^38hrW(5Zm8>5o0D)T<pmu&9#HJsvYCm$v&Ytcu%t;JrVVvb(^Oq^eX&t#MQnL6U('
        b'I1h50l8t3%g8Mo2oY3&4t4;olO}<|CrAyR))A_keDPIdU#Hq@XwdsE17|+xUzj!|Jl`CRlELex1VRLclb^%dXvgV5QKQ35T+pNpU'
        b'ur}+8F6(dUBkl0CU%pw*$HZs*OE&jgmwoUeu3E>+>%a|DvH9ucFXFJY&5MhRXhfIu;nF)IB^EB9!JrHHKO0k7c!~V-gSe`OmuSw5'
        b'!&ODt{5Vv43uZ9!o<Nt*^-$4g{t0yVXW0Df@L#n8BewCdCk~g>jp?mR;li*Ed%{>g2{$~)bCzJ=L8)9;-lMbk!9^05m*CrPE&YJ*'
        b'Q*SLp&8k_%M&6+p(I>R?j^e8S!1}FELIGz8My%#xpF*|SSl%Ndy>%t(aVb=L2KAE8Qa#Cov0K-pUkjktMl|ecaAytlP89KoWESGh'
        b'@KgYs;ygUl)octVB5jhd>ItaNOhwUqXex*#9tP#aG3oyC9t!zdm<WGyjB^fGEnkzABT<*EshULmoEOM(+FVIlGpi;!=kXvg`QSy~'
        b'G$V+DL4c8yh)Ech)H}0kiZhkh&u8WB@t~iPTb&az@-f2%jIL;y%d1Y65Zhhor|2(#H^lQCk9)!WSe{<Ky8Cp0=Vh-c*z+v!lGXYA'
        b'd_T2So0Te2Z3WeQhl8u8^ZMm$&OI;u$avW()Su|B+^R2G<J|13@-@hLKx+g$FGk=wixeqK))4Dmz=QRHg<*UZpGQuDb_|y>`o9XD'
        b'8&caaxXk{=lt8|^WRu}*<`MBVFlKWLPi;*a2=#y)HW<Pr!d-Db7ygi3)g`FEeZds9O#;77C7S}ds*70KGMt#@Qp=x;g}5>t+i%FL'
        b'pLi}tSoi@eVRj=ML0z$~y2EXCj{Xl=8@t;NLB!tbT7avjK)kNZv!SwjC>z(vroU}eC|?CD>DhsL<|{8HPbo@P#Y(wS`O|1qPs)i<'
        b'N<mxYD;4rp=iCY28*$SIti}0FT$C&G&c)qjrSi4XOpKU@jx>IPtAOI%ym}I-Py!V*8`&z(ZS>k1dJ(y(pc)F!f}#11CU*7+u{`LV'
        b'UT@xsT;R>(+$JXX{ypi{gRxkQMRJ^f9R!LXcsGP%`-!}I0Z@`K7sy}_G1yIQ?Fh9KY#*>tu>_i0OdqKTyfUvea7&&vMl1u9SGYnE'
        b'IiVzoP(((frA;}#XSzb6kVX|s6+rKDw7O|zFP1jpXdwi}mrOuk3W$sbYEfyWbcI4Hi&DrGBis!WINx<)lR+B7u>G_1>L-lw_EuU4'
        b'ehaiZ18G`4+~Xnq|0Oz6jP9nB2XxZ&FfOHP`P!@*(fNX~0HV<~MCXvy-a=>5)_*UZYLM0Yr4#1ALZEuqwS7gP0qW>h1d<i{l1-+P'
        b'jZOq^%q|TiktXZmHya~m(9rf}fuNkEU0t$~oCWsH=-=SSEBWMcI**py{yhiwZ;-$UuzzdC7E{SuDA(xk+1%vc5I}(IM`t^kqIR9D'
        b'D!_1!3k44RJWwBokySQ6*4nJK39xr6|4=N$RbS)9vv6W7Cs2^2<rIT0Uc>^c)IE#zH<hfhKJFzlN9WE8)XSd&0bU1kk&NvRDX(W3'
        b'na(CSW99cL*8;%`#y%95+XU`XDu0L{f!|l>#RuxkgJZ<$N>H~I3Zy)=IMztr%wv?z$S7Mn4k}PtnZZZ=hT;n*ApLand$>w)lp<K+'
        b'F5m5|`U7{qKzCD&zELOW4j{h5P4d-E9KAnV>W|CgA~%&)S6`JM!JVI?2iv5L9_QMG`VyVaGZ4i;avjt;PuKB~=A-{M`RY&)u^F8r'
        b'*Jtn}3DaWs^Xv%18Hw#L9^ymX2p?M5h!e73y5<U2aG&Qc;2MIEtt_{Bx=TiKi0@s98Q;>(2$?M|Ep#*E_OXp&M;zV;?AR91N1}xI'
        b'v0_|)ghVMq6hnExiAc`#!~%l;05(aW%eh3C6@vkHl{{<zlHDbL7RLNeEv|YJ2?@-xEetbtvmlU!5WH=^whLTr^WngL`L8{X9tmtB'
        b'i|2A}^5r3!Q*3pO(2A)<+hygqS+SMPTHSucb(35REncW=?5fj(1fKO^N^Sh=)H@w)`)6!h$*<u#lqweB#Lu}_yQF)$Z6QWe*e3t='
        b'rZ4u17k0_l)^?lZzwRnoTO1E`Ef2}yndECcLDtvYcya$5+8vJSI?D6SL+yA;!ow|mX#d=sLR~HD|9Jtl-5uck54<*^iF3JFI4!1!'
        b'YhYnL9x7k~X_G%=4!Gza+93eq7&a9B+yxW?Cw2!^1**ci+SeVe(NxLn{=1h!G!OmeetwDg!PUso=}`w&f+kMYBvr{xrzcyqhO>eX'
        b'Q417`^GoN~)CWdc90|qHbi&MdzV<LU+BHQPE>ZK%Ga*hN6q-QctQg1Q)WyZ|ei?jF;N?hxoeOW8hBfR_Y`?0eo{^VQwqe8xyX{$='
        b'YlUD5Za_Mwu5s%al=C0*5$S<jYQUz2flX5)o0c}7O;dtRvk2YW)3wqv90`>Y$y8bpA7qL?3qNAiMue&q?-mi?b8PZ8x}YH~Q+>yg'
        b'g2oU^Z?@DMm(P@MD%EPQ$`9ktk0HE9TE+)0(<#Kv+3XKFL;3{|;WCsje(qeVFjJ||XP0rDa`5UkZWkGcmLOwP3+AjS6trszPE4U0'
        b'Fr<P`{~tO2ICiZm-s679kCf^HXo`Fd%rY6+!7iHNibR%XH)nT<LcS)peL{zzk<fh?z{m;#3x-1ZhVWEzF)SGhOEx$|*+{1HG4*RM'
        b'h*GV4y=*1x_V7i<xZK6!5j*?H-R!K)5A5s`#?Gq8+Sx+d&dwg+&X(N4&VuW#G>mU&OYUH2i#T9s>jM}GSib4HzGQ={fSy=RA!BT3'
        b'Pi4d)?!4Q~>e^6oQNT@@_9nh`5i+l0L#PMJ8dI1-L~>#NSFj_v#Pqw_)*?R4zFNL+1!G)qv#p2$*JuXFW{Vf8Z?&x@cd)Irs~NGa'
        b'OUC8Fh;K*VREXrzG@y^KDC*uq*9oyC2^M9b1{qecs!kDFUc!tv^2NKsrk?5nlX}=s+ziIluL&&2uZ!cro<13pIoVd%I>wmh2QbF;'
        b'LS5^SC3Tz8sMjU3oyd+dM$~ze-JJ;*6e!gr``P2M&x{*pV^@4Iu+dP5tRg+Hlsvn!S(l31tcwV^B7e3~&|lYhAv~_F?)T7k`=O0z'
        b'dmcIms~%6(XaLVv_xp{_KydpZn<sYZqy9QAbI`v|>uK3|w02t?AM2tc3~0X}Oz1a*{qkp_YVMJnDhlXWTWbXSt#{k+C&7N}!G6Qy'
        b'YK=+0?nc?Pn739JFh=~~p>}RwJ5KPh76RGvgF;<s0G&k&niDPlh_>Q6!Y=tbFybT$M!W~{)a-ZBe=_tB+y*l%`(_XrUbVPtx2hc`'
        b'4Cz<dr+WFiDnHfDe-^y%&@aSDpVk9ZQrs5tQBe>p@90CeVC?cyp>Bd(O+j)upjc`H@%2A3kS@`S9H$3bkir5J7Wkg2pxR<fhF`3I'
        b'*hSxmn1Ofj?f)1AD$gv2a*9w)$;Oh>w6I>yef&nZzw<RVEK6%+h#J=TwmtoJ+iw48a73?b#_08(Y#W!cZRN~&&u+DC>0sM4=(yT#'
        b'+is6nM@$>7*Lrq@K-c2$w(L$VTTiRBA6x1NDjlYO?OVpQ6QyiAfP#1dsrFHS#<mx-$5(Dp?FfQUV)wG`_EUq%wxf7`lx;WsYqtG9'
        b'$B#_=0s<CW5Imd3o)(K(Tx;=!P+7dgmV#;H9lN_qVgewfXyJDdx@Z0AXajf@%T53x1<9Q2F%+e|)#MH|f~@TlCej!<F$iJC?tt<g'
        b'QwbqN``)BSQrMQ~*%HZW6u*0z1Xyj2$pg#%{yS}uqubj#l}+;XDVVse>b;Vqo)CT%`nzRSA>ROAMH~~Jswmk2UWM4n!swtKnc+2o'
        b'T!`eeAaZYv&s{STxf3ZMd*yeQy@9sDe{1Xx>-x%y2aDZ%aquY<-LhA?>53G5${%s0&!a;4FeZeL|J&I3UF^@q@1o^5P}E+A-8Fny'
        b'fs0u?;$l>zT}<mCt;{w!6u&$FC&cf_#}MFS&^7Wg&R<~e7``ZaR1E)X{9lgYkNVv!hA)a38^iw+?_Lb<2Q9lHez(0gSbb8m?<JfF'
        b'!)!hnQ_(JATTe-tDsN?iGa&@PZ*V0myS3H(wLmE2OqkNhpS<AqCr~Fh{-!Df!}`INo&}%MKi-;PD>#(kkyQb=gmEZC3xl10Lkj~@'
        b'<wx#iK@a+1IQSCKQ&TwWqW{CgiV9qny)eiu396P?1sY^1wFKCNzTfznJwZc1vcR9%&$-CWZ1@z`0?U3-FT`Nk!1$PjJH$tK&nh`8'
        b'Y~-M<0Y~d}tNlh4R~!R6>&*K>bet2t+z)&V+Qdv<<e%Z;nWF?BW6bwY^OIei^bkW#hey#?M9Y}~C`VSNd#E{BRE}27#rAQJfq$ul'
        b'=GGFaKVbB>qZgy?qGb>5&n>4n#?aD$-p3moKdv5J!C2W*@nb2y&t#(QY)0Uga<H?Zx7*p8v3Axtw1%jJH3Zsca@*M<<1pR=LX^7^'
        b'e2lLjt>>bEje2_Rz<8LMA;W8jKeI+Vm>^VK)V^x8dwCAr3tBgnagclA804d3=G)@Nfn|(m851+d4coT|A9EbLQXkJB&$rZ!>svT0'
        b'ILPQ1xQ)I_bVomv789_0)#X&=XE?fn$+Yl_YD>V&5M#W|{tw+==AohGti6yHmc?kpr++f-R9Y=s5Z5*<|B%NEq=yMQh;fKtPdhrH'
        b'$_C4np2_ZIid4QfK??FIEm=#8Xe8J0>h}<|MU;6iBKdhoKzr6itkIwR5Y{ZDNA_EjO(nlE)oE*M=<VcniMtUg0<{O0mnciD+&2q%'
        b'PQwxf`zEPTa3{qg+V{PPzAYZ{5&Ay^Q>9~1RKlfUI+m9((RTa~R_p3-m!r=WIg>G)RkQCPZg><fit`e1l>{!<qjwTPm?{DId*~DN'
        b'&bUp!G508Dvtj*KzBN_SU$W8G{OrC@qSgDK1x=_js!_x#&H;MW^53BUzd^puCf|6uU0C=0<o5Qqm$0^yjdj~5TT{K9KImPpd}Cet'
        b'<jWnx_GVixW-HkUU67TBn%5HFy5Jev{6X{oQGMgW)-79Rd+k}n*DhNF2J5#r8+NExZEJBsJ2pE8v;+$1%InngF!9m0l6C#^XBJKI'
        b'%*mh9Fo`F&SSFwh2yH_q580bEx4r3Z2CCJ^(ZVqI_!s5N!qs(P1J^CiD?cbypKyVhY~x~R4={01U9t`yn$W{M3$F5I1(J?qUb&YN'
        b'A$kR3+i26Rmv7p5wCgbpCV7b<Z`spI`BS@Rr_liz_~(RpLnj9ILe+_Uej2S4untN{FdPF{x+?Jdd2xaIw6Lk-ou*NH`KpsxxeX`Y'
        b'!RY;N;`r!&@IRqPs&3|y>J&OR29ZZN2L0|wm=oxr3pz+_q~niU_UZ@12Z!R1H2U2FJVCp)^t**o^u&y%2W@AM-K<X?+N_s;z{*rY'
        b'Xm-oHh4S(C>eZQ;vktvhFfimA(&%>~L%ZMOybBqadJDay--Y}rdSOm7Gwzq(#h7yqh9x;TqBC42ZTG80hIuqGII)lpnB4?O7y{^^'
        b'&G|TT26HEr55*fnQA7^LJTol5{TaG7`4e0fgC%!})bdRrS0G&*kAiTey~wqHijv+8{1InT>Vo?b8SwJa+wtSfa}hZ>5@+7ZHxuyf'
        b'2RgJ0j}bT8#`3LZEZ>Zy_*Plb#J`nqHRJIuLy#W;o`T`n?r+oThh7R8*kj{i7Ep=SA;8a3?+p|*TZ00PX<@N6TY*pV(ErQcyTC<N'
        b'=Ktf*IdkF6%t2=cBpk5LIoyU(YXA!{FEdC8sJnwEUbb2wLA2VhwPcs2ZO&LQ5EhKBT-0_3LxCazD{rv@6{+EV#Wu56H!?9ZEi?t3'
        b'LFWH?&J34KcXNMx`Tt)3zb_B-+%KQc=lMLJ=W^ah>fJI5w#5F}_8Va>*nX+=>OA+sg)H6~GFCe_y*KePIcVakQb7?%JIo0YPfU*m'
        b'C6*PjRzIzEdCc^jtd(m!k_IdhPX%bDpzFDb(v?}Jf(h8JjK~Yv0P^ruj(7@9!denkO?Lv!SjnOw4i*s$13(wViI$17BJvUfL~+u&'
        b'+!w;`4K|h|QNZT}pMsO%wHX(Ym!35Qjf6teMXvly2`iuCBAyz?wAuY}1IfLY7_mv;Y&Y}e6YvUfdj7=%HR9~%$gen2Qr*W~>a(2a'
        b'p6Y|oaH#|*O5{>eod}Gc<ga?~Rhd3u__7HC>=Rh+sjFM$hr}7%7(NKsze*JO@v^UI(u*0CBO;{>QORRVvpVl=Aj96jkoL%gB`-^o'
        b')wq9Y4}n{n%n6&wX}RDblA~J)T2nL5XJP0>pPq3G{iWqSRCQ<opM@(NxocszhFI>EVuRz%%(-V293(!uqWnx|(gYNn%NX8dm};iR'
        b'aUlS7gD)P`{?h!%AsghW3$0!u1wVa{$;yDg;xBqrp4DHk&kLv%SDY%>PHho4kTvJsuTK|B9mn|#-%WugB;Y1gvq;&*)QEkeceo3J'
        b'5YmbjT%>qm0@C^iagqK)o?l4EBXHmg9t<PiJiUCcO1R?@yGa&gtrHjd7f8|Hx#ZD#WVFsOTxTuOLMT;C_EqT!-Y2h_AYct064iX;'
        b'!EXK6;SA{}{1j&>e8MQsQ0Ro~;0(Ps;lGA6w0^=rk2Cb_g#RCB=>Hy^A#%dc!5JFx|Gyh&=&%0&U&I+Qf}k{zEuzk)Mg9#GRBw2n'
        b'srl^%iybs2S>*50aS|?bvxVJ^Fa2h28Uf!av1)VE6Ho&c_P_=96F(bU8ByuOv75DOuq@avzi0^9AcuTbttGP()|c#|F^QtN%*y6!'
        b'eRP|0@6KvF(X&lzVJkVUp!)*_J**Aj+x-MQpGugqW3$BCl=Ny*Gh2zToZf%s^|MgHwIA8q<tKb(OP|oDtY%C1zL|eH+aX<;`AX7d'
        b'e4z@`+cnXFQYJ*1W1GWO_-s5P5~@^`e<jqnU8t`O)+l<MeNW96=@Itjlk6WZvK!mkO`f{5T|{-}D;?be;4(Q39aP3;+I|8W#5qcv'
        b'J#a(Z^t<yfaqSpvC?PXZ02q3eV>kT-Pbh)iWQcAJSR~0}D=clw6lntcQhdNLtWef55+k0xc=|axzNCupvwB|e_uf;*&FeYoF40I|'
        b'@d64Na?Bn?Aw9l7?12>OSU(0*C=Npk&GJABRb2xq)Ip%fGB;s7p-uQzpG_D~$lw1)ctX#P#S@bIV>}^Nz!Um~(~Bo`)^8L~Xuk7j'
        b';0evT22W_y7(AhZyqm%kTITZ@Yr8&9&a~^{<XA@Wgf{&gJR#eE0Z(XFM+Fv`Q8=Nh0t_d#X$+iD$L&7V?54@7)pqpr@Px+S9G!ap'
        b'=O*xkZ2vYqp(>0gv`N4dsv3(YROQ7J+H^fUp-n%*6WWAF*Cqi^Xwy&egbs}232pijp3tTr;R$W}5uVVde~2e!yAhtyH2i*H+)wc('
        b'YL?z4o{;T7fhRPp;JKgR3EBQ3w!t*~Zf)F8->uC~{U`B+Z2vtxp=tl*yS26(zbtmmo3#bcd)n~#@r14?H^O_VcitqPknO*RCv>Ae'
        b'^k{DqPssM4#}k@1_TAdJF)#3iP5Rk*LU;b$wvWX(_!;lkdhvuBZj2`sA+~siF34Ea4Y6--q?>xi{S$aXwto|zkboxC@#YQQiC_2A'
        b'aSLHT#uKt$7f+~QBN}b?bz5;wtA%p@A)e3;_5GEh|F_T-;|XQ_=-v36m5+0tzTAp_OljfP!cTe<b8}>lC-I)<|1p-(v@uvhabvKA'
        b'!oIvYETMnMhwEVp{ao3;Uz+s&;J<Lb{rI2660-fLv4lFFz0Q35^RR>pY&SdKK6m5!b`(qKhV$*8ZW2q#_HV`#>X>>%ETJ3Dw@qWP'
        b'ghpmtsph9Wi2a$Q9Xr`V?dWGrxBtvso4sx5zdhIf1WV`_B)0aik0o@Yf!R}eb67&Q{{WVdS}9-&&G2Fg&BRzjw~z_AZ`Z{V`f1-h'
        b'SVCbXH-{x;`x#g-|1_4+tOT}d6iX;>{0NrNLJyWuRgy`-652Cf*u<!!#nSoY^%O9+nr?_CbVL37yJ0M$t^a2ITkyiq)4v70NBjP6'
        b'^Xa);N3bRe%>RnD&c6;v=tg=gJLe{Ggl<;%{tI!0Za9A|zeyY++rJG*h`AAt(2e!)FK!M;$o6l;5gIp)BP3Wye+Nfs8pex>yAF<!'
        b'aTrIa>u2K##bf*x+fCyL?ZIO+TNs<dp4W|Vgm!pPgkWqI3S(2~OTn`v{rIOaglzv}451s+bIMI(2-$89f9GF`A#|fYWHUF3A!Pf{'
        b'VhBwegCR6_SoZkeB!-afKZ+qVBVo?We~ckiwQ$a?pMfD%g)xLgej^w{9W!qZL+E{#7egp<6hkQC?_dZ`7j!+w5RzaFp=2e7Fc3h5'
        b'l6<>rd@-O8Z}J_3AQZGX;9jwfb<ly;GGyC9R8`T6(%l=jC_0zWn^xXUtoJFDg)OP#77Fk|rkK`45->n&e1$_X2Q9J4h$Vqyyvyup'
        b'o9f%O-c!X69G|{qfG%ITi%j~$jo;h<`EWr6Ubvtt4_wf50$fnlW{E(4{V-lo)i7RAm4FvibpyPhS)+JCRl|5eRb%jiX5APs=%{QI'
        b'FDUd!ctO(f0$k8<eFeCnZzdhsI|>$5IRX}x9X$*d^!Z)?5G?48FEf0H!GbF5e~cAW>A{hiI+UIoeI2ZzS;JUCvu*|}NGSBrVcMZ|'
        b'=alPV1<k(+tRPQW*&##e)3yJ{SV5Izu!6#F9l;9X{t;G?%J&~*1qr8<fkWvBC;bR3sOo00f-1*g1%>&KU<C#KBdnlr=)Z>*<l%AH'
        b'_@Q*U|Fu{_Rq^6g{?Y7<!UtZef?}!?q3H>kFGXkK<Ji;dd?3{e(>kP>A6X;(=*X4>KgLH39i1KrG9K|wKs380fqliaXwmY-X!fOq'
        b'%vS<F#%MuVz@ntqZT??)z=F!2eyTu$_c+GF1qFG#j^To8!~$H<av78^%vaE95J%fz$)-2xQM8~xT?Z{lXxpJ0G!&re$9my9SV7AM'
        b'5E@1c5|Y1PbM<OK>Q!M6iDO^tw9z7L!ezeLA-<;1VXmtI@}cXT<98{9V|fEURBsBa1)Wz3gy1H6;f3aG09q8#_|6Y3p#*>->DB>h'
        b'&4Az)@P*C{B%K|=`nAe~FGP_^=AnYkBltp@D1}(2%E~19CS2Ds;*4s5#TT{0E?ph@t{iFcljeU`3bRF8k|ku~!ps?#%y^5R4=uB#'
        b'&9$zxWrkZawbrd!nKLb!I*Z+`Sz7(UQcEUh$qaiebCx=jQD=touPKCY0M0nc&b-LZYPOpXi8cH1-L<O=<QvZ-2xuTR`@*8W&%bC-'
        b'*ubfh=2L|vH3A1z&E7Rt%)f*S@n9M`5^3J*^$LCi%|AcJ-)u+tS{*`m9W(O%MZ24(BI0R2j4tLZB%&>hRq6f4DH}z<p4Svb8(wAj'
        b'C>qMyTm=)qn7<vnOFnO!OoL~#;E@X#2JyYN9~4%~a*W_8txyJ^q43^w>v0Z$qntmhXc1Yd6B3Iy{=D>%xbtOtQk#Zu5liv?H4@V2'
        b'$SGQ!B2BOtr;wxH^5YkH$~rH>U+Bwrjg)s(abD^z&-1lE;clbwjm&gEG?SPr-kg|!a<haJBW@9bzqE+<XQpiszWK}}$7#hglE|nO'
        b';(ifrT_DL4gF#cj@uCdfPnzAz^mm7*e6nPtJPU|(+vHH;>xgeH*(e78<j{vN%`IeSi01~7(zz&sL<{X-m=cxuJ-@^s&-Ga(@t9r7'
        b'wUfr(inOm3>AyzClZv!miZw4qouCf+;O}o1sje9L`vpN$)v=y1kC4};4H#+pdUA_=s+<l!(t*FHI7|G9FX)FO9q$H%hsx?W;CWyA'
        b'NXH*>Kvq^q-4omH+vpUR-#vd<rMNaNVtV4SG<qD<pfCNa{%}2GKew*rfirBrbLH(*&!|evEzBF16LeJ-v)#f(RM&6QMP~dlYUOl-'
        b'_SLOgy=AJrf%be4INzBie2ejfJ4dcO6E%g4BO=FbkxUgI-`PQ<&EpvpJ_9063F}HTGNwul8(Wi!&99co6>(M~o|1|YN-zJO-Y#u%'
        b'r{D5DT`1k>p6U5E?C|#)Yrb}Szq1Ma{8$eCKO{OKZXv@?j|o3C8eVg1I2`!5RuO4TA=ZoNq6HM@p0<ANV?Jm-S^9)Beb>;GV}%~>'
        b'-Qwlm?!r;-J%5|Py@Eu{J&XMdGjPvZ=uajkVD1G=CUd4=MmZi=H03Ek=p-pBezm|Hc7fuU%JDynrr#(IN%-@)VRcc%?8<i^lG8z6'
        b'mPsD*#rGcm9?zC|cs6bR+)D8oHey!d8MgE<dgcwxu@kiYuj@+gKNHn3-ovv$2s~2&&uT18*chIjpuId(czD(@Uf@}hhi66)&+;#B'
        b'Aw4|vxiQbq5b@&#o=xbbYozbG)Bo^2{XFpQ8lGjJ8N-{LQQq{7<yppPcy`a2@NeWNBv#7MddZ@V6TU7zJZ6o^V7Rniw0V)m?w-3_'
        b'5p6GyC-Vn{Pq2fTNe5!(gake9=#fVfOuf=x{=Dq~AN-J&D4)FIXbNdkJ6XBH#5oy4&VDWjFCylxMHw4wB?0vko>buZ${|u9nZa&v'
        b'+D@ggZn+<UyczyHlHrbRf$}D&9FjGbHdR^kuh{GK=3-@m1o4;U+jpx)xJ`1A5ebds&&rDkE#aL*_&>?Z&dWiUHjqtw<b`z+W#7PG'
        b'T(pwVNbyTA$|fdk4q<Qg4-Zy`Pnnp$nQUf>TB7GcqCk#ztH9Mp2&i`0U6VzaG|mjdnIybZ1}Upq)NUtg-X%<Or-5;f(8PXYntUMl'
        b'cJU7*U3}nZg(RR@!oMdk@CTawNj^-Ix$NFCG$|U%F!g9HYI^G@G?4;L8i6Lt5t?8bq$v+Y@OODNOyT4CSD31u&HMS_v%7Q&NB1Gi'
        b'ehW>SZ5!}6{~Ujmzh-50O2;d5JI4gCMu7%oaqQBC@LS|aVKAGUbk^X<8ilV!o6TjywO14AM5Xvkdge-t_gm9Yiv=oJ)j}3V#vTnM'
        b'*yrWUWMvK&%ReuNX%oyL$8&N-;Z8=#xv~Q6F2!ZT9Lwp=oDy$X<eZ^!(MawkEaqpbyzD6tKWVz@9^hqISswhQJRI#%qZT4NoUq&d'
        b'!!@dK-L2>LVzvQ?vTFzs5A4ZK!o0%giXNU~_H89R7nD5=4NLTL8R{+d@ROe+FMGgSZ!k0&*PA|CFKCt)qUTnEp3+;dYOPn&!S>G9'
        b'-6~wx_EE_grOWCqWTEaB)*#<_2C)ga^NhKP+u=5I`ch8mwG#~QGp0}Q4g3~ScKFD*p)(O4^N~cns%94Ar^`(`r<H=miM85}%ysMR'
        b'<~-oNA3>xii<Kw{6@8q(Tf{nLrf8?0n7kHg!k+oAsb4lFut?tc8pBV<Y5|HUz<0$Bc4r8vga{ngbB+ihP=IsLzzx$L-zvrRhNU7t'
        b'7}Tqk3a5gz&k@I0*Aijph!SV5s^(jwq&Vz}@1}5(ayCHjX|H}K?gW=f#1q*|5$`Jpf_R!t%RMblU#bQnR}w;VD^wu_!H_{~kssSB'
        b'6C@wnjS)c#W<w*{4`tB1;o!R=pEv$4WN<h|Ml$;=LPU@OI$yR$Hav9ZtySW0<zzqdoyE>tRwK4oRxla&7pL#W>C>yE(EKlitY;-K'
        b'>i;G<rvqJ}C4oJwzH6!zsMet1|0csklRNQy3t_q6v0G&#g0R>*kOe4PiC}yNKnce&1=*uAkR@m$Nb*`Vi|vvn`670s49g9Ic2B8h'
        b'31~#vF<jl|&p|vt6<pJ6vc8+5Et0b(GGQ8FcgdgxuN-9}fuN{ou9)A8%l|PsK>*HGAP@5cN%nUF5pk;~WZ(Z?(-R}ie_iN@#%W-k'
        b'!?qoi%ReeJFc}7pF;ys;J0xw5vQmx#9!AXYw=)@_6!cac4x?EAF%$8Q?;-IC3I7@{s$(IvbDL~A2bnt)!Zs2Gzd-aIrrV=>Ii>v!'
        b'qjyVsAz~<p!}EMjG?{b{!Y_0p!#7OltsQ~r!^->1E2cVLk~O^~gGAEV$WbC|S}%j7(ixyIWKAWq95pG8M-E=rWR(HSk>goelNqNj'
        b'h(V5gS<~-v>H<A-%#t<b;?xCGk>hSz({x$VWb|Q$pX0Z(rr*krPLey;$eQwG(r~E1)Y@u(E^5Ys!pKQS7bDw__sg}nc?KWvhx^sD'
        b'm&h(6U?z4vC~I0F6TUs~2$wa5$->n>;hgH6CCMML^JNR<jSKZH5~&KcWy`v<W&BE<8-MfNu~^oWF2nDFwf$Pw^=lcQfn(ZCvaU24'
        b'f4@LG(07jcvZe*HBmy~7WKHvBW54U(M9cUD8S_`AexLF@Nl)CRC1@EPNXr|GH<VhL?Z*^+wCq!@WLLwaf>{WJ%M=1ar!zD<LC7IW'
        b'nAN3mz@HEq^NMoU7QB1lxLtPm!>IO7e*23`^Hf#)4hx8yqO+G%omTfZMnqlQVd2{O*y8c#7gSTn<2bI@syh0lyY;13JTI(w^iNUn'
        b'YMJ>vCI0&&Q@z8&eBO#C;kUlGa|&oQG&f2Ce;KB;Rd|OG3fNeMI;Z3Jt59#TO3~R^+nSy~WG~(sg=EL$O7D=AX=E5Bwo)tWP~h|m'
        b'u5fEV6uq6Bz_mYHT1~KoOs55*WOR&R!!f#6MB=HbRLgjEm9dp#LY4Yy%Ghej0&=QorkIz=^a-sn5==49xwSrePF`>~<TVnqh*#r{'
        b'Ur`aSGRCviT(tyZfCcQ=6r`Q&hd(5ec8W5EIXmt^#y%>QOO5dqGCxuH-o2Q=NX2R=2l&bP!{AV-eNQF4Z!t-nC`N}k9k$>2a}e}S'
        b'F<0!(sZY@GXDEXRM&xZ~i?WCSHI*T9Dih>-q*HPlM!Y-&!L*VJ{Wr%b`F)h>L8qBBn-)6Rzfu_zr|B{08ZtG*PXp;qL@FdU2w6<h'
        b'RA6_FR16wDKuoapRB0l?gqkA>Y!7g{VO`E6<40850ZP9@xkUs`4Y+G@+G`Y(sC<T;8%D1TlhKkT)h28%qs&%{eU~yxoe?jS(s_jA'
        b'PgKu~M8|D-vgF^PR%*4-x|Oxds_h#y3Zu-$tuU2k*qg9)6gyT{80~g39cEwLTHuT5Fy2NLZoJ*`8U+ml^$8^w+(pc-9&Zvkk4{{`'
        b'rs3IM8cm?1k#3V8o_{-TClLQf$P@@MN54sRY^GXB{`Zte{U${~r}%QJuu?FnNS!nU2UJj?#Pn8k`Wcizz*zN1b5ZtXk@N>QvSo^T'
        b'%miPCD|eJpFq_-0W>}5W8uQ+Djpn?HsLnV;@w#^ckA8z3777Lr|Dd<7qqodqpQCh%rbMQ51wxu6Oq=itWRjEsx_5{P=2?m2i8VD$'
        b'=jV8)6=^&pPx=?P;|Xe|4u8LyT}#d7#vfgEfxX9L*65`DFdiSH=2lBiPy8n7T{oLe86U+K1^XLHi8R>p5SBtlx!e?r-NuJ0#4bll'
        b'9n`_*Qc6yz_qgw+^lF?2ML8LLYK##j69!HhNyNbHs9&yEX$tVWPAD^qiYV}9@1q{Jni8A_q%#<tEJqnuMgi}kSy>%C6Ur3l@b^-Y'
        b'1WnGZ_2(B+w0dqWolNL**bpE<3WOVfNp)LP#fc&@7#heCODXko#A=F+BBRK#6Kn_xKLOJ%gpk1OqD;`0O`&RuMvj<cB$8DkLR6Zl'
        b'OkwRt)-jWcAxL{7<CsA$B8d7#OkgJxYYZXF=fD_@r@;Ln%=QUR_D(2oxk;ik#tQuokejlc8HQ9g3fnK>Mk`WTmSR*ol;re!CsU*D'
        b'$Wb>`p`Vj#5<4>{q$(5TbBw5#C{0y*YSxREBSHffh7zblrXt2^2uTI2NK2F^C{6xOgWqyCkOERen}A1b0Ol7^lAS<VjY=}LnDZkM'
        b's|NnbQNY1W6;*68-Q`3kr+#7T910o2<VsEs<>eBk;Y#4GQmu(33@Qz7l>c(2QlnVRe&w@fF#~MvyvO*ik7=5dJ>diDTn`LY%>mO$'
        b'1r5_If|2pLk0DHFQl>JQ@&^T$Tb0}VBiYM7h1DXd6rqTU1?&$#kP<VSkTdsakQj81fvxco&UM)HkWv<P&Id*tevdSwViHiD5o-|f'
        b'&{{N+J?(?76p;={ku)F6Pt*Y)nk?L!lD5&uTo@Hcz`_B>yUE-%-D-|_JhRj%x}8TNL&ln>{EKS@Gd_~YuqrwGEha0Y=L9XyG#w2^'
        b'43i;fBn{}is2ZObqj(PP0O;#@0-6xD--ij+fLe(9(8u_p52Ml;7#;R@_#hT@4#6@gG!-p$qI;Laz&FitMggUOiVtF$i29R{pHXC5'
        b'1hJ`6@A!Z`qI;ZP?;f8~x77#IgV$4ziPU9eYhchC-gffYJ|6k?BSbLzmFm=}-}{tWU_6O|MbIAL2XGDy&U&jkHp)afPy6|{kYV$%'
        b'u@8wl+-^|K!|Or(FZ7aR1}u<Z$}!^)U(CW&4?JMenr9FEAerHIyPt(8>f-~q-!biuPn(0jkGqTTHSH;~QZrtw*Zm2eS&$?O(!V>~'
        b'F=h7W<5OnmvRuq_i$05ey7dondt&+c<iGuC`fahQ8C|~j&;0cpn|9rEX=~j6aLx39RS(_$YQ)YNP}Z#1>g#dc2Gr|z=W)moI5qKJ'
        b'7kgzkJny>Q;}c<0hIagQw%dK%tj&)j>x@&ezlSjJUxcS;w)<I;0igkCckjEZ&$+LrH<Zr))^}~_yx-N$PMdkyp5xmz`!~$|4-Vb4'
        b'YqonGvW2F!&-Pu6|9vw1j)zxINqn>V-Kwj9TR8P^4YMDq%G+_Vap&wu144#69(`x_``=bnR#qOEZ30^91$rU#b1azYA;>ToiVP;)'
        b'UigJYyBTQlEJCf&)@RWgA*}%$6mGBva5j9UaDF3DH6x+g_u$2pN8z~uY0akh5Q4Dv5FbMY#u>Em9IH7n8-4PZciyRQ+PxdstwsiO'
        b'K%C+Iv;(tGf&Uc5ABU%Rk~o2c;xDO?frd1%zZz>e<^J<*eO|0#KcroHRWjpkcwT^K@K))J&F5kb^eu6Q<L6@yHV8Wm4=fLm+dX?{'
        b'Ex5md=Qtxy$bhH2B-Y^mBS?UIJj#Q7Z$^j{qyY$>fx6!OTdYA0?sL$FhqdB_KMzS}kZ#G0bodR1=WF~6{?+gc^OE^ZpxI%d*)gD1'
        b'9)y=pkj}`-K`3zH0lb2G4=O<fYMrkSmd;R5lFqQg?*@3@gXbtb1caT3Uufr`+fATesJHaRSi@m>C{P@s5P!Tl76^{tlt9=VCNDvn'
        b'!R<H<&8&xi-9Q_tXC_q}YnZ<VWtiY`yG77<_iR0G$2RCoHS`O9*Ft$^@XUuN@Li|_!f1HTP;rJ%S)3tG4iDrpgZs%7v4-xgv4+3!'
        b'u?7ZyS4<Tr)Iz=|fZh~5hRp~)2RvONi8Ivt#2F~aV}fUfUYsx$;&b46?ys?iz)zs949Y+TG6R|5F~_#L|M)oWPoo=~H%#vzOCat0'
        b'@Sr!}7k|7UOX+^r2L(2YGR*KGc$Dz?!$ZRp3=ad30Uj|t6i(AC$~Xq&^sA2o4Ce6%W*>%UPU4-h2p($d^S7JFr_6co3O75W7vuu`'
        b'(NXI|yTLsGveXOD8F;$kS*Anig9wDCnK2FBu3-3`-RgEv!G54<DE=j|?BKs>2(v^FVOn??9QQ1OaX}#p(;c1{>m@TjhG#!KN+?$e'
        b'VIM{#bPVd!&OR`kfhQE6V0fk&>5SS8GJ`VE8M*MB(W8trK({<77vZwMfEpPr(=Plm2Bo_n{2(J%p{@Py=R9qORPOKn5uH&g_`i3*'
        b'><Ry05C`nV|9)`0-^IU!_(ut8L9AdPqKx_Q-1}s#VcOI<Ltb61;hpAK!<wD3hEjL}Uyn5mz5z1vM64kcerN26H9WZ)==WW$!F(Fh'
        b'Z8<Qz_S;y)aqvG3?l|ZZ7F*NXk{Qc)NoKUduN58#Jnx^t@>@FV7oW~;=*t@)m49)=n}qM-*i6OSdqMxs1my&}GZ~K|H`vgTMy=6k'
        b'8{!MyU_H&%`iclK`}~k-4vO@XK7e?Od#*Mw&En3d%!x`cvU#)Hj}UKDN3qYs@Wa+!;mhOLXWYhT+`?vn2CNGuqoFkn(uB+bJ)sfJ'
        b'A(9@(63IRWIpp3PYuv_1Jvrn;4tc(FIENf^bo?6etKIm1UL2}s#Wh_hEoTU3CDR0FTDIF}zYUf$j50OtJ~why;lN+H(e#55s1z+{'
        b'{B+O)gT=W$Qqz3U-TjfOX_?!$10CGATT%M5a@RyLUZx_$+$eMT<E1aR(l3-xmK2Gkfe59|12MprC_|Q~rMOM^;6_1_U>zeRSWT%)'
        b'Qe!YXalXXX;L5p?G9VNJdtU|<q0tR4uz(Dr<;K}=q}G6a1%_6J%E>@R26rw*gm8fZQI59DGB_s$7I29F{m|T6H4s)w;3z1RmP_&Y'
        b'HGCLl+3|F7XK4vxPHe?CgSiS@$kajOZ9^iMdr4eN+QcDxCWCayP=)*tLh*h^0=z&Dkr7n=<h4l75R>Vt33dYg<>L#1?vr*>zmriq'
        b'm~3BkG=UI_U>G=|R*{Gh9E9DT;XU)>6+@8(EHcXEL#%WNY!oo*3L_PGPYTTcvZ{beFnSR?bkzh_9O+~qbeFA!&I|5eyJ4|sB2zsM'
        b'#+1rF;6||U^SJLD<6b`MW+XZ&5cdYG*0AM;krIZ`NMXq^&t10A&1Is(NUAK&U0PwbWg={U#ek)U#SOuFWq9w}DB>~~vwyjINZg&I'
        b'O69cVW0~n(rb!XTWiDKpxhN|$Ex(->M@*3?bY7h|#gMSoFo#{pnk?+XpwPpds`zm(^IqoRR`YYMw4|)<D(3HUtx4wG*p7~{>3Cs3'
        b'RZAlB;7Pl^J4~hdPItQ~0R=5yvi+EaU1Wnmtx8j=i=-t<zK~&Yce$!+ONb2lQ7GsMu&?ok^Ovt*T~C_EIq`Mug_iw;Pt<+V{kZDs'
        b'M@4g?pn2R8*0iMI^X^1d_x-Aq_TGgb3~Ihh$XrT4xBR<|#MYCU%bxK~$XwDrSCwjn6-<J?H??fN?0%ml1u~XjUHE|;#DY=kkP%CS'
        b'@#U-7ODqQgNytUr_joeRv%+{hJ>kzSQm_|onZIh!yf6DTWGuc4>m4j=gwD^n9HO$H9Wp+D)sI+?2OutXxsCl*J9{54Tzn9zG}{8A'
        b'6x$ctdo_!@>s9qNyX8mNCG_LS*U)HgDo(^ZDOQL1h1QJ4twnMqF_=wF9ddL$NwEYv*1Z_WxBP*n64O!^o9`&?;j5r$l;|N^vQ|kJ'
        b'gd-`5PEWwMZ7}wC7_A6OY)~AryH7e0eH*M`t+LL&n<?{)twpl+<MFPRc|CT@gZ9m<Y@nW){I_iZcZ3H>!ovd!WJpnHgJxD@n2(|g'
        b's<d>4R19Iw&<v|ev#<CC9CmLdl@k`)HSem)*9ms==HeFV;RXhX1JuZ_L>@XouYm&m-B-bCM#N;iGdl$-${S=fKA=1T1@2X8PV8;j'
        b'tx(iATA7oq>FfG4CAs*s5S3B_C9uori3#ryF7*%iWatRH2;}JVxxj4AcR@>1e^K>>R0U$QwEGXLlWclbL;V}I@)j}D9BiQcz_wKi'
        b'8{H>CtUgzL{<jbXit$B3^`K;$KN>v3F5KSmRaKc^3YMb8CEIr;t#u<sC8l(wAgEe0t79Obc?e$$<k)+``fqJ+wPY@@c>(eAt0tY('
        b'6z60_4|Ny98h80x6vv9M0?qK^ORZB@n$1P#YI`qYt85<<NPV#TDV3gGuBm_e=@)VkR|N}Hwkp!cb12DGnRzppJ7Y~b<LDpEc$)zk'
        b'6B(C>;cv?Q3MzU;1~mw4ILv@>V1VvX-DEAP$bo{{(}S=^^qY&f0b!|pblcTufVPg)gHkz$60F}BB1JI@#I+O9@vIIpjF*V1WJK*r'
        b'7<xL^FTr2&M38mkhp2m{YIP=%j3x{E+$Y(z)3ao!Z(aEMpE?Y}y^*x=Xi_>0Wwn`rJi72l$Y*2)ECRQs&7{-9Dp*koGt$umLnRYD'
        b'DzYOQ<9=kRs@qJfSNlnkf`fRxhc;DqG;0Vdf`m$^-yDz=e=x5>b%}-a&5-^fNFRjLN7SA3mPd5l3V9(sMoK82(6e$_mW3oCy-Mzv'
        b'L}Yagp1$SeBQm@UM$ncRl2GJ$(<BIK5(ut+@O1b|n9-okN1)A9hueHQ@>~ev??+7Nd>kejzd1w!XnD>F(~-w3R8Jb1P|sdGUp81)'
        b'HYliiSfhfD#fNl!Re;t9@BgnKWPtk#I#}zoMT2;Ah)rd!*rAM0WeW#Uh|}wSe$;(DlwCIn^MIa6h3UeeOcmaJVDkp?tib4?0c`%D'
        b'K6E)KM9gF{P6gx25ARb5a}Owcjs-(tu<W;k!|jU2iOQ<dQ>5JcgxSKRAHydmHNQkHa>oOMpjdPKN$D!In{ccg<ewVEN9lw#8-F)v'
        b'#b9CG9Y>pCL5ycRJog$=)UO9&rEZFGMm;cS@WTsYm{Ftd8B_|#j!+@g7DFH<tBYDXShfgLfmx)(=@$*cTxf_&^*EGsQll0QqG?XA'
        b'+cd`gi!ts6UUyW=AYSDgQ#}sliqxp&LA<x)aVL#&CysF^;JQ!%HYkwZX^O%WV??P2Nh$(iFcO7zi$UFo5U|82l$=~2qZ1iLen!&J'
        b'>@;k3@^@l#hzOA>)hTRAp{P3s{Rk3CHFPN6YQH@Sbi095(*8_nE6i>%1K<Pc2?&Mz&o_n*#;JCz9I8P>h!Tp8WO){shv^p$hK|Ob'
        b's7%58V(g&nL4pV&NYCzHhB`GvnTiM}-bKqueb9)K2;cz`;$gF}&wbIArXJKMDjyNet+_i*IXE|L+>)0k(YMeNX32&Hl7I=sA@YO>'
        b'AKmd&ah*x8f*gqkqeO$-0?3Y?h(&`@#9%=aN+Tif?f7pEnKT!*5rbXCppfr2oUiSFU0p*ieiC+X(~wCu2*$o}Bp4Qn(gs}kumW-x'
        b'+=kNnTyw(=_|$_}2{~I`UEjNCAAY>xYjJgTyB5grR|sWOgWeMo;lhpJ!zC3&ptfdL*Gbo7c7i8_d^=oSe;du`bdAj?_=J2DQQD_a'
        b'ePY{ISJzP&9l>A3QEh*8b$vXV`FkO(%GGty#h)21$n+M&e?43h-uxC$ZpvIuAGqjP{>za%@I9RV5vm>^E})LsqvDSVMelWW?G>uy'
        b'|04KzySjF}_(Rz3Jy-g(5dNmC>rEH`;h6CKLU^OAtI@@`jR|iT!e4iFz3$@ojR}882(NW@)w=k%u-i&hsLcDB($5%=9}{A$YrTAn'
        b'K&c|4QpN8WCdnUNeEpcR>V)u3uC7fk{?#$zTZQm)S68`<e`QSg79o6tt80UcuMnt!PXa53TY+g}u4PL1F#JnGEKrOu#jYHm2?E72'
        b'`HF|h+M$Gn0Pjk(xDG#|dOGpx$M^djyM?!m<TMY{xmMg9O7Qu^`HsGg*tIU<=xwINb4l$kBU(?glU;h7a;9wfo{AB%5iUKaj9TNG'
        b'&M|j*zdy)xF0*jpj@`Gp%2vBTThi*nI+C*w-`8VvT*CdPu3KD@MrOUzyzBYqkNDtK`;EKmNGXc~mMXT;tve+A{jQ@faoK$?Fks9j'
        b'%Dt6-GGs2zFc&dpOI_w7V<{{JmbjGlL}{n8bw6{!7($2{Lf*<CP!;$uAuRfgVy*G8MQN{P>Wl>e$aCqUkWMr6#zI<~KWHw|msTkG'
        b'Bo~fpY-+4z@MV;;8Lq-TQ(*~;kX*Riz)yE!ld{%Nj!cox8`R@jr+n!YCa(%2AlcWUa~1BDd9Ga)=n-;Eb!{)wu~S^$Ws6G3>s&C;'
        b'6o$|hL@B<_@U>vFK%s1y3l?PN!sn-3tL;OD^?oepiW={NT%gOeM1<%U9SXE9P#JZrtJF&9E0sW*A_5kV57%$6y}N9pix<0M>n5=N'
        b'qgkjRR_zj?+SzeqLM5zFtWpVPHtO&}Q8Jfh|3purr4>viKJH?DT*4w5>tWAzAk52jHKNrGBu`-RSs*`tP^n_VBq$)2=$0et6?eEF'
        b'*~1FgGsP%dj;4yeGJwy;FFQx?aC+`E^f=vP?r=7c*;n1eGV`qyD6J*ok8mF*dm6H|ALg|5m#3XJ9qK+}-hb@EDJLBiF_WMb&d!7T'
        b'I)mPxI<6!I+S4-;70C<m0n`4aLGK)$kLaM*eXV<z?$#*w?a>rY6jde{$t!B{O&g)Eo+-$pLjiG;BT)RGoy}U`vxhDma?%q&ok7qt'
        b'=f1s_ofF@lBB5nTU<_3(Jz58b^tt%m$$R9m2CyA)r+<TNT5+YkdcVGBCc+nCjxIwOCsBnemk#43?sY<cEm^2$Hi@sqcxjS7<Zia('
        b'^R}9)o_^vnP5Z~HZ?TYQN;Rw#1AY0|G2LjjJz<@}kcTM>=`1W2&B{2ADBL)1_bouVL3c@NN(ep`ZVn@$z%Z9P;AzOUN|fRk8RNyl'
        b'G@|AZqM9SJuebxM5N$2Glg>?%6ipbto4VVtR$bHY?mXLf4{a445?hzzcVtHIv~`n+FT(ACDsUH1yZPs_7rVc8H;~~X2{>z};DDOR'
        b'UcK@AAM>(j$ek^0c44|aIZT)H?rZ5n<8B1sm@YZjq08KjzR-W@V$Go2VwWD*)pF;hTKNfy)^bP;LI>?%FBk3w^QfI8Y^(~Bx4zC)'
        b'rX4WWTyd|LSETJXzJ73(EM?-x-x3_FoSu{MSS#&E=d8JF-7}*2c$z9uqx_RJ6|rFst&WVx7xSxG<@Sven<H>RmP~PFTF)i7)mV`R'
        b'9Ers9U@d21m0CHTJhYEp^*Jx~+&mm@3)p*~Ffc1X0~^Si9(U*GwH!2Aen_m%64H(6<$!AF911vy;!>**>U#oEgQ&v=bmwn%j@+N-'
        b'!<>!~r;QQ^EJM{=6t?87caT9`)U8f7*l7`oU$@qZvKOD7DnIV5wo|;XQ{Zu@rl-e^k?ccISo+y?xw|?G)v1Ta<alS(c&A0UeQik)'
        b'_avXS*$JAm7p()|u$)VA#U=5zRQ9~H-mnI;=UvaZc98T$nlcrwGn?}sA=8gZ^+oH_pOmJDN~#@93sLXjGLxe-Q+nc0v3*wt>n%i3'
        b'G#mR)a<jdA3a#1KAmJ}ufo8UM5zX&)H%NO@P90xejpLfT2xYyQ|MrT|i4qNa`pTqU(+8NI8QYlbxu>Ser66&fgG{>O_O$cMD<kw`'
        b'zqq0$`7dxl-S9Z!4`Z)aMh}f~9~|TUaMT@j_)0RF@6vB&_#-&9`#Dwd){5zh%F5~KDU#i~<BG2RSK1C-aU8hPT+Mn)snpe~A9lg0'
        b'u<0(QS{o~sy;c?Wtp;CN>lI<Apq8Tj!zy|jMEturOUVjg^;S>QX>kE`2I@{G<J2$Qo9{B!F#JxT@^z}>=i(|9G4U0Heig~bWnGO|'
        b'+M2F7>Y?uC{A)N#d@}6^^sEyK-3f)hh+Pfh>>q$rv?yu7J3ix}Qwi_+H;A7U<@)iPaU$!S{BK|?rX>yHWigfq#e4-0tyM44#Pqy-'
        b'x_O5i-?J~nVZ9qw)>~Fr+ACF6R_Iu6GW=PVoPQbrENu|;#aBFvg#RDx0NRE9;P#pgKdt*2Z{42_*ByfEermYxyTW!4*ZtUa>dw*z'
        b'!{3Fu!9wi|b0<OdtB0%q<#6@ida4KA5TCX*jTX_G1tKPOooV_y{WK<CmHyt8Xp+iR*<+OSH2sPVGo`ue<J;PPb*0%ph0nl+(4lpN'
        b'A%<D1I=7m0z@)iUwT#FK2x?o1lVEJ(bet+9hPhuJaPX>CWyu8YrLX~sT(UUeRnE%BsdJNQ9}v{ojbuk5(u(t4FJ$42GjYZ^{{|_B'
        b'lIG%UK{4?*emV}+5}OxBhQ<*oBuz%nnQ<|45qtNQ+_cDb@zTwAE}I5Q>K+JO%-(gynwBDoe0~|FO^YMhJFY~AK!%u(Puy*jugrLX'
        b'*6?@W;+~NQET7~EzLM|a8SLjLUeRjP6BG{a%2V392#4lMq))9pGPWnXr-huiy@n)eZwXcaQ90ekMvlRb)fcDw@bs11xS;yFI51&('
        b'B`&Blr@@E6Gytxwb|p=%iYhYZ8fne8bb^-SyIA^)4fdy$>HXr8MW8Vby0t7F@C>O4XL9gcjAX|DNc7qbOpY@B^riHjer7FW2wBH4'
        b'c_ojniQAyp=cO<DzRNYx<{EJH4m8`}<}c!!a#hk3?zSHwAh;S<Lj41R)e@i^|3Z5Mo$qSTl=5HWFl*HQ%v>t{D3wAv&J0+Mt5!sc'
        b'i~Q^EeMD@Hs$B}*SlU4If5RyQzLq*Z835vZCgdZHM+WdfeXcgH`XEuAE5ZW!7aY~z;g730kjej9NSU-h)4WyLx!fGX#3#*^!&Jc^'
        b'6bk$;0{+&#=gwuV#^k6V>%7DiAk6}4$1eAis-!R6AgSAN!j7}<C)ou)kN70*g~4gaV?avch=6ria`{(qijr&?(wha>G#JW%atG}C'
        b'w81CrZFk3gkmDH=M6%-|xHyNTqgVJPlhQr<umvK?&GYt)6tB0|D?9fd^9yhB3#LAelLp)`#RD?@P&Td0Iq`#45jRguSp&7|-U?Ov'
        b'B1v(P9e*1Kvt1iFMWpvgKyIKXAoxcCHtj^Vd_Z5XVk(vPIvie|JMq9npZ$&|lTN!Ed{0mXU%P1yxanK_<`eX|VqyH+AmM<l+bqui'
        b'{b8-D`+Ftx9nSlW4E~&v<u^0mDS-v%7ja+_4zx~WpAo9D;#B|y)J-ht@$?hF+eHRsOSO`O52##{e;iXQ-vu<z#xAYev1Xvxrm}BU'
        b'S_5>IarX%NBgZce3W<Z!Il#my?J>B>c&t^l)~M(KPY)xleAa+4{WOT*N#GY@H@3PsyIF^m#!;+xOl}J2rlLZJb5jN1yAhv+b4f3H'
        b'buSEyz%6op#X3XnI(sEE7|#@KICqAAp+Q{p4sl2>pmHSR99{Pec;93I>uk<IVU;fo<~f4Q{NS#3kY3xZXD{KkBOE9?Qwo|d+K%Fh'
        b'p0|jZ@)Cc;^aqV`1N1G>nq+ZG+5*rfG_{3d%Gc!*g%f>Zw~4jlLfbEmcMM<(i_f(iBOtZmp4Kg-p?qDbA+Ph2F>=7LxOD+(n!C<m'
        b'$_uDL6={W)q|YjnoiwmA1m7g>Vh7sT0S5;Iaw#tpbOA|lYQp9~x*QnNE9*#h!T>F;AS#WtY`u&rTvs0WJF79acI|GlML}>ugt>+-'
        b'<`fsX_FH@J*txo%31hc&OU$i_83#6;mz|Jx;Ft1(v`lGYBu|s25$l-Jyr2`Et9q@i=JItVPX)dBbwJR0iuSegg*%SYzGpI<73eC_'
        b'EdkC2<w(B-!|iiz#MZCPAGg9JI8`<;v7p86u@mUph~28LOZ{z^`kNgRM{hs>S%0?x*Uk3!7jqS)RgG`LT8y!~>8|trZD%2wH0iP%'
        b'fy%Cm!3-A(>qP;{0?ZMy!EPwazZm|3oK~X=1{jW9J3b1n@L~VfPm7pHWo$L2;PS0zjtS!4N%&n+Y0*yeI<~mr5ZNH66-8{NivI*R'
        b'!OAw{&+;<W$zar1s2FXliJPOVtn^_Pw}NV2e|mxl%c9jsSNS`wS-bO)j0s^IKxA~`xRB2X{(W3bGbt33fQ}JX_Hfu7owW#;P@$53'
        b'?-q1KgQ(_vcm6>52cWKTi>(fY75U>|d##dxQ)r5mChKeKq*kBhkXw+uvc`UzYLQjj|FX7NwO<yonK}$A;{|Qtq~0Lw3zh8l{*FO>'
        b'9$fk$I{YBY_*TT%^rzMIe_7LSUaLRb!@t_UiugLt*ktKHL^Mb|;M!qV-4(`TX=gHPiS4%>=QsD$w-guC3iGZFjpn@V0igkbWLHIh'
        b'TSb4f{b@%<KmQxtwgxHxXup~EtL{N{1ZcqA3A8-p=?#VDzFnpLZR;WJ@1&Pt@I7W9TDeQnRnp&Pg|K|+eNfJ-35QSnDH*)}&xOg^'
        b'=SeZR9?L>&9z^DEMOsNjAl=3HxABnSm5!5cq@AGPA}1V=W*7HIO4bZ#Ej{hG3QXmNc6Y>E-*i3E-}X49f3@SNV8_v<<G1}ydHsh-'
        b'J_9$`XZ1K3<77|BDf(`_SdKgu#LWmSv>l`O_K;_3MUVCrJv|J&!oVf3A;47=af;UTARHThiq>UgS2nm(Yuw*JY}hG!c^Gzufopa4'
        b'5V*2KPti~JTm=`ds5lI}!oXEkGl+9=r|9|~7mj654X@>yJWw2t<o>3V{zD@EPET8<4Wg3v?66ZoG0?^h-8gMn<f#IeNAJ?}X+?EA'
        b'#RucWbVU(KYb^;>u(n9;edjZ_pO5Vy^Uh~XKR<1ZzX$IO;C+B0w=jmHZtw3*pygPfHHfk|e$Avl2ntZl>xA+r3ab)WWSo1_P_*ux'
        b'mJjJqJ-C~y2()VV5Q@$gc>^rPESY53TVJQwy9`{b^c?6(qTpMB5A39Vjzpaa{Qvf0`$vO|WcT)Mu3~rfg=_p-b$_^S9R53<V#oLA'
        b'q>`+%f7oUX8+4Z~?PKNr_R7}n&5|;@A2`=U_uH$DU|MdE_Jie98`VFR+8!MY%_Pl{>n8PfTU3qh`r;xGkOR~UTmh&Ie9*La4+I=j'
        b'v^MK^O(I~VaCm0Gv{cYKexOg7Y>qGIFZ9t9ZOJJ6lAAx*XRdFxIK+1C1~1*fqUNXdHJ$IX*S6L)e+>)4QqS7uY@c^g?_HyR-4}JH'
        b'59+HW*`7Z8t8WP_cAC<2N`p<sy!n<rl4-Otw5GIpow+n`rlRuzf1=N9(KlKdbJe<%6!w<BsDM6!N5*4)UQ4_bR|3Psyj~pjmp(j6'
        b'uQSu2yM!5!FUGOm--^1=i`x$MMZ7ZUgsAydG~XHK?Ad(w%a8iHKI&`wsIT4rDE|>od7kY0pbrw<C-3NU56cA|Xqkif_xos>m9kQu'
        b'al)ofEft}mt0{4(rg{#tYGIkQg-W{W;qBf&SnTY@<-zYB@9%E>%Qp9ENh?fyouHTy803(15bM3DrasTg?mi(|9WJ5HoAWjA?{@ra'
        b'tnSl_wPa^COw5b=yuxcC#hqtrNxm8fz^@(uavYhSFcg+RB!r>_F%@tx0a=o8485AK5X4T8{~Ep(85W4E?JM|~g-DH|dIN96PB4;i'
        b'e~iU_g7tDI4okE2fgzkLNe`fd6<`9qhy&{+ou5O3JA`T-!bV=(y1uN{V5Sq%snkbjPe@y&Gg50#_B<lrEdTPEzOHBbnw|l&ALSnr'
        b'>a5S+eu{m#kDk=_R9}lP^z|ukpL6kVoW$zaxL;-NZ0+t;6?Zm}^rY5K6|LYO^~BOMm-^8`jUT8?LW<>`jh!mUyJ~D1@Vi9#74s6I'
        b'O0wV+cVqzj%f9F&3L<~uP4s}L$Xvh14poLw-0DuOYq35^_VVb5%a{?f`<9A3KLDCuxGZ!Vf3Bo6i(lvw`WB*r3_I?IHQ47EzwC@B'
        b'4Jqw&(;orZ3^-N#S;4OU(i2C(98e(!VM`TTWs&k_y5j@Yt5CHa@w0H^?dnO8?{2|q)6+pxF<LLH(54r;>$DwsG&h63yrZw?qtgKz'
        b';>+9nx^C}l3hQfkMDqRuTL@I54m;|GwtR3|=zr43ZqIvjtQz`-*QhNxf|vDyknaXk>>KG9AB>A=A;SLG-FXmV-txpq3I^Oldo56S'
        b'VD@3WNA!lLaKXUDy20tD)x+<5DErcseW?lSNm@PkExdVe^zF+W*O!`1Pni2QK}$>=<8yL6EAKN>eL8K#n_}&61CIDEUAOH{GU-l~'
        b'{2(js%l+-)M3pYIB#9;am{9XcEh;%09`Mwo1DC_YDLx-p{^$>vkBBInNZde8DWMg~TPsyZGSN3IzwxpMqkuh<>RX}uMs7<TXA^}#'
        b'rCFv+S-xKW&Yq0LOnQw=E8<dVZA@e`Ckicz=Io-#Tuu~L@|ZT4o&$z-WNxq@O~$?~qW$74pkt4IcDdjy=xb*8<)!5AMW*y4@IUCG'
        b'?zdH|_qFa*WxYOe<>YaW&o0|vYi@iu%D#<ltZFq?9<e3UTDA1FuwPVg-b1SjHUIu)T3uK<4p?N4G4qEm$L_{tVi@tT4)yG5gJm*i'
        b'PrK}Wyx(Azr9bH&-uvWRFLx)ZOr|`;9JAiqI(I{mvE_2Koxsba6^Pw;xpM-$7w3w{n^Co*=@obdBbygfaLLn_8mF7zdAV%I<>7@y'
        b'q|9K*qXXF;m(xQL`vwj#^5Piaz0^Srln~bMZmPR{2%DZ)5lux@NcdYY&ATg9RU0Z~o$*0dsnhM<YYn@C_*X9D<BzS-!tEPCYwY&4'
        b'V-K`L>YdYpX`pU|)g9trzHGDmfIAx8MYsi(6mPvuPZV6)-w*HW^DkVcW%{BG!|jVs6w|}|i?s<fZP97)F73#E^DrJmc*4ZKh4OH<'
        b'IGiJduyBiSPV*%?A!*Q!=;#g*<%I>_y**pIg$|<SrLV2C+w;zSZrkx}l?^;w<mWWi?Q0;6KDS=6{T-#HJp)XH#>vdvTCy~fSx=fV'
        b'FX=!$Rp4@lc{tpLVgI$i>&Yok(PUwK;*^x~I8qvlf{V%nqYLBNoZa}nm0($6yp+CD9(dcN-r$Mlfp-N*mRI~hTd-*qTvr|#ULN;='
        b'W&f9b$zRawf<Cv+{(O1hCCEJk@+qf$Q@;CS%l=RMlH2G6P(sLNf3CdZE&3u@Ea0}52fkGpKh9<^C=Z-yvlo^J9_#3VB3>*Hl-TSq'
        b'NqgLMbitQynoH{T+F_qzm<(80BDHWe%6w_`e2><a{1EP^q5Yy0kR^ejMfg$_xN!hsNdPKXz(YY)bOPDo66T-a1P^W256_#5ic+gG'
        b'h?5Tfn1(R3ir}HlT&st#ftEypu--T@xGZ2Q;MkG$*9+6Ct%1X3Sp9;mMSh<8wU1eUI}%RzX(d(>M2bevJs_VSM~W?!c(gp6j<$*p'
        b';}H-!aWpxO%daqVN(F~4Nv3GsD2=K~WD^mnJ_J>Uloq$r!La6d2fzDNUM1mRDLV&^p{Lij9hRSpW_*gl*@=J@)GY%EAEP@k{UQQy'
        b'uds&4OZrkYITOPxl4;U*!1;E{#9B&QTfbE}1?V7A__9-PFQdX&Ny4A{E9BNDhcCSC?S*u>O-ApGRns)tamB5z0NQo*<6kv`2}oO^'
        b'C1GWQ&yCtY?u!GxHN{H<OM4$!J)B)KOp^p!ZQ1XBJMJ3Y_K(JbHu}fm`4_!?zlH|ftLR7LdN}?k^{B5OZ?QdKu3**{sTJ1Z>T3D^'
        b'*ea=6pN9cZX7(0%$L+Ok9I4Cudu`iB{P=U(UYWc$?X_i9kaS?UOje-=6TZ@1YT4jD$EhH9i)d=s#E|{!V}7*y@awHJDSPyW2GQY4'
        b'aFs@HXx-PUuTnNzHk6Lw(=e8hAS<n*Wnf6_A{pl8d7P&WRB?6j&I<W%#XM_crM^<0Q+s~69kpPa7gmk0P_LJF7Fju3ZMLl|HRpMR'
        b'58^v<-(uBZje-qJt2>6z+bo=>!fN3rn2TDc$62_5(wLKlJ2m>}jW7>bxQVp7%8EZa%sJvHCWZlJ?xly7gz-U+jt^_KtzBEPw3aH|'
        b'AgPn#@GaDOIjCVgM%2>O4eQBL=2CgRj0=?L5>sRJ%q7pcrJA&<rRJDcz4=mX9TlyXzyt$Y2&M_kLdrv1yf3K6bBRq&+3lA~OE1Al'
        b'gEZxPDVthSDx~Msq?vngB)vsQ&#5VhVwg*ewRL21<!SGA%WQ^1gkm|hgb|80Pi|#!ORuZv(Hf8J-e?{e84F&y;y8aHeZ1GN=ZJ7W'
        b'`RjASLsa208VI9B`jaL-gM>LOMxSLu;D$+z4v}7Q(?56v`h;&%ky;p+PlAf_YVIP>d1tM<g6u9<O}AS1`{P}eB4J;Vjw`%)3mte|'
        b'he;DT&207$5A+GwigUmoPc9NBxdP962<y}loqWx>xeqvgt^8X>6@DehDg#TtDUw+^g|!Go6;+Z+E_ac7*e<ZDOQ`rjs~Q?h75Q1o'
        b'cy%WgPsVXUG4b3;InlLRtK6y`S%m&bmvHU=!}=&%8#kIqn|v*;t$r0D&>k(cXW|Xp^E1*wOUWX2(MbD-{WiP%BQE&ZTC1p%#KZFE'
        b'(tu&|EbaK~fb>MLE^PQ6S+4yHm`sY-m1-Hg7o#E*S?tf`J7eRL^`+DF(~P~9s_qyS9XGuhO*EidNB)4_s;_+rdlDUXtJ09nRCE3*'
        b'52X;hxnz0sM@;g)^nyc#exJEpj7oI0C_dVIcYf~9hqLUzpL<u1BGK@sk&cZG%`&`fG}xzgSE_pJRaG{mF`z=n{#E&X<^p}IRf+vI'
        b'PzO`AYObFoV}&_mg>hvNgFmKdvF1XpMMQ<%%2h10>}PPDjl0b-hjl)!NNkaIeC^J6;)-ecunvZP9TMZ71whu_oL1f#ql$jdpiP+K'
        b'+ql#0J<%3$yPjDOLKYhztPeHf%k5SxrPojEjZq<y!K^RS>;2=!!#YS^5*VFJTwknyCSPtmW<68=upYlw-&@*qX<4UbQZH5^2`Gpw'
        b'v|Z}(mT76vyJ1|3&0_B^wtxT>+KAB<Bl_58@2;}J<S#F*RMPQuGML7etUG5?LcLgNB_lA*2ZXVjU_X|c0LwQSS{j<`Um!u23DUQ<'
        b'zLr1ugi}5Zl5P>QbIigIauqp8?;1)Lr{`Vuv>oz2L*kqTawKH!z?XW3%t|4%yhXBRJ2N)F6z321=I@NwiUXP@>&dB<jfCbjh&n_l'
        b'sD4+aJpHYqBK*zKr17X(j?y;`b*`!uPnBV?zMzU`3Z0NOh}z}o!%hArn-rC_C^`k<+kYn%pNa8%2toDhW$DMSCSCHZJLpNCQ;ePg'
        b'_lQogh|qoClm|+KHqfF10!`jv5fQW>t*CaOwZ+oC?a}j5&^}tDuWwcC2?&&caX;nb`%Xwnw4P2vXv(oIisI(#d8l26g7(A)%Rddi'
        b'J$=Sd0X`#Wmk}pBw+6g%wQ$O(L1!jcn%`;t`gMX1TKj@D$XeW9Js)*kaJR^&DunSAOck+Kl9pI=_lq0IWyCVovZxb83%(hnRnfT^'
        b'Y)+DsE71~>qw5(%IG%-ay+U<8JBr0u%u89PUhib0S2r4+dXcl+;53L<H%2)#7C9MawH`V38BYBgCnH&H$XczR<7DzyBmHV7X>~?~'
        b'lM$_6lefB+bvCM;NVz&A*4axsyD?PF)5DlQFdsX}lB@~~#-@@Dk2?zv!y9~Bb)-m;`Al?(j3-i5_<ZbPh4sD}KX49FY#^DWLt6S6'
        b'F`$kkd;h4i`Z??D^{SNn@Gd`n>*13d@Ps3O_=nc-RC-R??K#bow}{V81;<I9I(kPdXSeIWQ)2IGwXPng*FjR8PUo!D&KHi@(ie(_'
        b'1HwSsPhW}4uz61m1M|PqS1LULoijm(r6}5NpN@~zDzuIIdz*K(HttdC_u)Kyw8993`Ok0oSWWOk5uW;}fI}|fU{c*!D&%ZdmI^tW'
        b'bJa;_+``%y`u~p3x_pKUy1y$hQY+uDwvxS@Ro1|RmD*Hj?4IRS*5fcS*sHva*fXYXTy(RyM4C(z>>-bBFPmqz?H{a=rN;|GV4Fx('
        b'ah`a+?PBRmQP{3|NuuYD=(NLoo7c?8ebI8-N-y)SM`)_g(ico&+X3IpN>oixTrZki;nf?pl)j?1%2o%p!m{3rskQe4ElQSu)YR@z'
        b'#7D)m@v7)dlpQ~`K<;?+!V67H<?R!Qnz*4y<c{VG^T3;t$UsPT?9lyk#~T-vO^ii{Ob`}Ggxxh{Ph?{KeLTg)6LC@VWqMcyi6naS'
        b'y=HSpGHYneD;G-)hI<W-8Of?>yV+pRi^Tye4EBr)qO>(HRwgMeT~XSakzoHgbspD#u6u^cz*!E)7+=0%vv*Wgz*LwT(_N&R9t|b3'
        b'r5CzWRY0WrM4c6Sn`%wiAx({;FDBTPvAd}tuF9%NOrPexXN2h6PmH6-)5qzcYWpL6+XcMwHEV3pJ2=Sry9;Ug7x3w<I8$-K6oZ8%'
        b'UTl2w0;7K%oJ+;#7$Re_(&Ra_6$?R`k3wu7gxX_N!x6?uE~Nd&Q%-d?f^ztWF4#vi#ZhUw7ZTpU5o3;jD?m&Ql}eAeS9(G&{QAO|'
        b'gT1|#%I>kDUB9}}_NxnrVHkKr`K1?x2veofJ~rW);>yx+lHD@XKBe6=IPl4Mt;|rb)Yl7V;xZw=cb~F*G=8`2@IGbhnDkVOsJC9('
        b'?aAS(B>34eEuqKJ3+VeWL30HfFK7`3KTD50<cotI6li?Mg*3f~HqigH+b@g|ZOVnOFOmg|fTpwv1g*JE*&vQLW-EtctH^@sDBehG'
        b'_(iw~&)=DHS{Lr8h<<OV+D<IABYn+=X8Q_$!3E)7b5sBKj!742KR)$>aEYbyR}7zwo%P%6_$Q_lw5WmDyO>WD$`k(5<Ij&jG5*ka'
        b'EDxD{oDejQzU{=gL*rV;L(uXVK1K+X(09?doR^%C9Fn&9;Iwz*;H&Zz(nHeoo}eoZUXKIo%J|9ncfhf~?1W^!r1#Set%Vy3*UMw?'
        b'ZrQa#Y~>55ztuqS;X=7`J{bQ>{ZO1S+>b1H&+RzVOP90|VQ6Txyz6vt+t<C0uX~&A7x-Ddknkdb&dcd%=!aWGxD^Vakl$Ptfmq+?'
        b'3G%@~j^n+wXsNupEf9zrpBbN)?Yf#PzF*!R03`Nr5NA8D+H06tjR?mjr}c#@<1&G+;r{rG41K~ey`!-gYYN~9Ru#s0BCP)^Xo-g2'
        b'7DCVxVSQKauL?y#oYiP9&0Co(F~i6&&Dc#e>hqp>NYdE2qERml?MfKJ#y|FUZ&krCo?Z__IMv!+uS(n5TW_T=1&h|MlNR173QDZ9'
        b'Lbbu~EtR(rPz9)_p6{=g$f11V_2j7f-n(lJ^$*sGCR?LwdkxkHi$p!mZsWGzI&rNitl1q^(_1HsdbO8ca8ZN~`2r(_QQnT}7PYyT'
        b'9tXi7sSkUCTX1mUW4|(1^yZ%tMAPgY`%!=BrSXtW5g9l1{wT&+dX0bmHU46+e;xK0iOVmNN&gRf_a0bPbs!4=<Rk=0j%^;uLt=Xp'
        b'9tOobhhR0KcABJ!p!ODNq3E<79zwCxPStv=?J#W;R1Qk#2C!p7b$UWe4OA*%AE;%TphbkB3HXS;Izw%lTD6r{t!UMJd+&3?!*)7%'
        b'zVG|<_xl5~_g;JLwO{M8_uA{+7;Cuc$fb*q3|{?Fz~uQuk{1t2O;1i~Ix_T%c;PK!emyh)(tkWMdwNNB)ANp8x;(p5^L0lC*NZZe'
        b'hpvg=)Dmm>;*t97++oq&#w`OUPv8C3V7lS+M~=-Zxb$;Jnm>1PT$fILY4(Y0UApwhiPHtkH=Y#y&fmui|3236@nF-*hO<wM`qCrI'
        b'|KnKZ`SG9?5Y1kYo74Pv;n7|*=SahxXrG2RUpkoj;Zej5`(8RB^)rV}x#&nLdnBUxhc{d}n67O26L)oZL&G~F`|BeoFMt0#me;;x'
        b'`TLG7Uo-AV<K6!r%{_6I;h%lwq{)WUj;%3e;*lqV(|lGe>fEvX+WKrYBR|`@=RHRTs~y?tk;kT|lpJXo5>-|5>$4S={3%688b+Kv'
        b'tFkn>3#0b{mG3^X{N>ymf$YWd@=HNUy!#6Sv4&TJgO@zv)NhELJROw0Q<F264>Y_K9_8JwL1iG?O5%oKJ2xH7wL?1ck0gfgFWR0N'
        b'^2J+DO&6UpdSp*q&{SN1`=satkg@F-Zw`Bpy*Uunie}{6HXWzGwB+lDPZ-zu<(I<D_4hC3-h77hvM+zv{Pv~qR1azX<8Ol{(d&?r'
        b'*AHx5^UDdRzuo-nF!W7F!+Oxx7xK66ENIE(Rb^sZt5+nqCo7+QX-j;`=)-G%{!;iPV|XlRP>-w~$Oa4>Y+F~Y*b;Brk(^L@c*6R_'
        b'l~27?6_2gn)zSab;kVveeNpqjhZ{^3CoW%dc95g~{NPJ{2VdHi`G;)>Uur%#O6&g&|6TpY;rGA2dh^d8d8uz-u()N$YXf0t!3)D>'
        b'BTvhlFzxM;_r-p`=cT>}gQcr>zcjG%D?5YC`@!S;*&O>5pLpTC`W@3_vAWTdJ`|pa_}Hnr6Zo~F&e1!Hesu32X8a+096QU}s?v?^'
        b'XKotPIr@zCdF`VU!`mC9OQyK$_~ny(pR+i&WZ_#IKl4`hz#eKVZT?(;RVFX0i%uGLL1V7XcJ<h&y2m`V=<Xv|^>pp(dG~^zlCBM1'
        b'bG}zF`|_rs>hifEiD94KzM$^ZnoQTU_tjl6W&D$~zFs$E%DbOx{N95XZLXWJJU?}FNg^oQwhX)Sea*=yf<66O(VAgTbqsszqN=Ml'
        b'cm2bcT3Z*i-d57Ox$EZ5GcVY%q$0SqFWf$|FYl@Dyr(+iPi@cqcFA|+Ei+<cm+t=MK;y2lsdGxMj9*z+S9SJ~!D}P4IF@`NKY4b+'
        b'p_bChyeAW5ZmtSjBvE^*`BVM5{@Km3JMtGSj`i&7`%QoMZ~8la+keUZ8#l&hFOE&jkM};Gf7J{54bS)g{Q3UhJ^uKVM1TE-spp^l'
        b')lbGR9bWRap{Yc9%d@dnc`HZ!KK$nR#2Ft92ZvcY{M7w<VUzPqdCfoXkG{KFIpW2e-W|)%ZD06Q!>=!W{pw)pQ`x0$3;P?MyY%SQ'
        b'D{md!^n8AAx@+aVYiCEDd$trdPw9_dukNmlO?jw4F=kqAV^B$%wXQyO?aEQ5BYzR=d!WC2XMe}e{_UABZ)}e@R^<iP`ZbwY{q-x('
        b'yX{?lKko1TVSmRDgQfql@wRwP=Ismbc~{?#{_d^)9ovGL%a{CfeC+gDW!cSTI|fYI)*n`dr&i~Wt(ug-v@9{@d;J%E=*oiZz{zLl'
        b'u9<ny#`^xHzk5@E$2Ws`)*oII4~~563;F5z$}y#V8~eMz)!)$;Ecuu4Tb|Z<x~w?8s;sB2`Q9g2#di;hKBvwMtla*tzHjt*xAk{?'
        b'EeQJUjbDprqJ#wTwBAur`M>*v+@iIrsii9Rozdkjdj?j;dv;Xb(!YLf=kVqio;=pqeoK79MSqOy=y`dS>HbT8T(z*ga%B)>tfV7Z'
        b'vv5S!!c&{i3NN>+?n`RA=Wof|UKOj_RnYv^@YtTW_DB$F!mzgnpMg)Pc`MgeDxQ1!$Cf`>Ker^jfafkB)-<=|vSWSuukMfDL#~|}'
        b'JNCZ2`I<1oV9Bw64`gE9|Md8_Pxp6xy8pn!*juM0-m~#zZ%;h!l)fwayRYc)SknKAu@k;B80VS~Jkjy#C%VsnV*T398-mk#+mGWd'
        b'nb@}PJ`vP~?%SRi{i7e}C5Cn1`NZ~2-km>=2fG*clWDqkUUh8bW$|q{KM|~Q=l$U-;n!{N@9#)HzCLJD=ACh0_^hxs3LCwR%zZy`'
        b'ba0ILg||Mj;XAPfKTIy!{`x12b{1~vn16WN>pef~Yv}K82oB?}j`#N;{zANGW8Vk+yFU=jcwqM%1DoQP<<I#}?6O>ZSFd>D()T=m'
        b')sK?1Hzp^1@Ac0W1y$IN`AfEh(fn0^_mp6*=Q}3#FZq1D=ZAe~_jjKi%y=P)CblVlW&UN^=gzm!Ni~<J794vVoeGk?Abb~>YAPT6'
        b'#v=Kv^4v4(Ln}(Br4LOj-8{7|ekfhKb!spfJ*sXST{)`1zW%Xfdr5t^MKL;?#=o>qZRO>U*Vh*$r{^7Ct#<Go@?Tu<ttad2Z|(Z;'
        b'uXiL|Z^87^|7yKprC`<EdbPtU;>lc5{9hi2+N!%^!8T6bK#=z}A9!-x!6#QOZ0>t9F?`k46`iXZDrT;_G_hw@WukV~ltgtnQe;)f'
        b'nU&$kMV*U+HTM)pgIRZN4yziQiu)U*d6Q2I$HLg$(Uon<6?cq$d{0=o>?rDLPi>7Ju(TINpJ=reWzT4E5r*~H+!(~oTc12sRl2IO'
        b'`R*q>?tU`Z@Sat9XNE~AZOcZp{Ag?2v53~Z{a6%N=kR1Yl}Sex;_SHAYdW4xtdFVynQZ*So9_trENV+0>od{z<nrfpVFp)??&DjZ'
        b'tp9pLwgJ5M$&R&8MnzsS`LWF#!Uu=VUwka=p7l>pCPwEvKt%lwo{So;6UV%^X4R94(*_&9ZNrw<y*8LX-0)<spTgjKnr9QE6Zy&7'
        b'72$iuZ24aQ(d6veBYIxlo@v`(aNqVV`OSaxSd^)~|B3~R8iFR`tdEcUUCU3$hu;FUv|hV7On&v2{QX0B=CwDh%4_~e82ZaoubSR9'
        b'c5Yik_FZhcEUGDQ3O|e4R2@Dus-Bh@Gx$JiT5iVVu6NA1<ir`9_Jl`&Pxrq+-uKGmxrTdo)^Cb>Pn_)gz+=l_3LE#iIsNG!RY#sF'
        b'+4}2shn@+8J(Z4T7T^DYqOEo7mj7G$&f%VpLqUk0Q7qx&9gV-679P%fYq!VW6$YPQ{KBC_(=)%#3u4MeGe4X^Gm7NdyMGd_pSh<r'
        b'7sbr&@l&FuTi36sy8EliXG&UwGUJZuau1I|+x*ILPZr<5b?fxtHaK#BUhctK7-MyH*RF8l;p!+KYz~gy@-Kxcs$P(JWx?l%wBBFR'
        b'yR>w{--ThW3=ie9>NNugyFc<+>(Ucv-Szn3^rFnbn(2?7cW!*fr=l*sGgGN+bIWEX3d8@x3$3kT;VqAMwU?yoqT4u}Rok#&>IoC!'
        b'U(3S3=C676iQ+3}FU@P6S`vgvgkQwe&Hr3+qP%|bx;1A%_Tj>4GeM@+y0oNzMi|AcnQP;ThBF@v_iyIqm(70vilF_FnwpoYi8c@('
        b'lIr<2cZcbl6!s3P&MTf9RI_H!zIOJUFvMlqnN$AlU>G7gOfz#WjA-4NQ${>?;&k<tN1g~LDx-zrU*YFw)s?w0(d^PGyPwESmo7as'
        b'e$%<JAD&si^rHBTiLpOi6#jbB#LMF|&WTzOl~dmLSne@vv})xg`6o`6PT6@dH=W%~_*ZqbBuY^t+m;EB{3|CP`6=P-DP2oTQs+ho'
        b'BAl+Bvhb;cL5ni__k_8H-^{gVDyNh_Hsjw1a({0*cv8wHzawS09=xgl*m@fd?tX0`w(+&R@IIgap_ygRRt?!+UbHBG<ftX_XU7%J'
        b'kMGLQpa1GJg<Il>hQzMP&!00cDBCAKG_2+Bf!NS+5dW*LS`ZsmADi3JG&edgBj)7C=Y72(%7?C>zTn0cYqlP2YAR^Gt|XPtYg!rQ'
        b'd(*>ZA1huO{P(5sfLveNa(8UOf@_<uD_QXA=xBs<mxcda`LRX$d5NLDH<c#FG~KqM<6jO&@y>3~%UoB|dR-X!OVe*}TQmQO;_xoL'
        b'{@U<E`FT$So6BwM+V|g-82a3}rj~|hhOWFb9AhGkdV25N(!}ViKXP#P*H+Z0^R8N2(v&?7({KO!)fYTbJU0w<?NxJ2uKv&y!NS?|'
        b'qJ6tI`w;YlPb|ppYxbe&b+5jbou7YjOMGz2oT}KI2_?ZX+m#<*{fQk@w-hY-?m+ZVJ29*EpBL|Z*Z$#K@}A0D)zE(FQ&<0bVRPZZ'
        b'@ONY%8sB#5q0OZ`@}66``P<?Be`f2_uJykidtLw4>4uvg&9zsTm2HU%s~JHR>Q`S1Z?=|+Lz-^6pk+_q@>Ss%g2N~78M^%S@K+I9'
        b'*EBUP2#d)Z2FtXOiQ&CBmL|qF-MgaU-3Oy+>hI61Z!g)JEqiC&zN2AC_F%4^IJ7=p(hz^5KKk4~+|JUl8^O%N=C>bjnjYQ8;YHgx'
        b'F?QW6f5`sPyz4-AN#oMk%%aBeCE?52|FwTe(4;6_@{NIGeUjSBqC#%v(bwM5S0?v=b+kO5C~Ha&Nmi$#eDD3&CWc&fO~V~SuA7i|'
        b'`jNzp1y?NInZLhqOWxXrv9${entyO0IEF1h9TAj6oq5q`S(~aCOz-;4)Tr1A`;Q+h%O2lfuzlD3pd{-&@MlW05&v09cE^Etlw?tT'
        b'I>?WghXsE1g4QrU4l?7Q0<s`m*~n(T9p5;xD>INeF+c8@`PjDqI50RXm3d|1zaKd7{P>K^!t1kkS?)$(mVF2k-nz>ww=ONog%77|'
        b'D;JJ?EEg<0oy~XCiIKY=JoJI^@6MxL=dOs2tdBj=vHV~vs1#+>6n@0id42bu1I6bon3~rWJrs|^Z@Rwz-0+=N=d$F7@}~UcK(I>v'
        b'MbT+qwjrLF@~;QNOk>&Qm(Tv;x*(rS1*KH<y64`o5U9Ss=I*Xs9{sUg9({cje#-wk(0ErYm$63WMQ7z*2Xc>*I-|W!W+$R}+NLaf'
        b'JohZAEnE5>D*|$HM7>3;YX{$KRV}N{mIVtA<Z`;arFHSbNwGi7`sAnE<AurC4=2TERL8P`<~$y(wR_B;JIdKiXUbO&96!+6S*fKZ'
        b'Q@(s4b$nKBY2mknb3gI2Q-65bluPm_-usb?vNPJl@jSvI7&hd}rh&e}^hDE988G;6J6OE!;EdM>a(|!s_>5Nu|Ng*%8NVCI?e7Vz'
        b'*KCNLG<_^z&rY_kjc(t(8NbZM^WRyy;>5||&@NaMPAytiySq1+=cI$O;kh|M(J&_{8kXffw>TY^4C$lK42gcJD_tJuEhE<E$KRZl'
        b'7(IK{ijJw_#nN^~ko9NUqpUy5KvrE5-cr{V&s}?WS8$yKnbqw1*{pR}kj)PX7hchOduigdZQ~ELZd@^YbKcf)p!MvkUmNoAF$Kk!'
        b'&2G9i%x`a9dsnP=Zb`1#xpl|5`fn#U?i^^z5A(+PSM;V!6T^dep6F}Zw4y$UXKqO*8}y3XMh^)Z=}oO+G;_umwcHg8TFk9CMj6}{'
        b'MbXSy^WA-0;<>mB=EvWem)}2->z9$si_=Sgb^VYiBMvjjStAqC>!PK-j|Vwz_YeAdcdQ69*{)-m?9w}itvr25%l=#<S|%24zbj}Z'
        b'mt^zkmZe3}%-EWL>dWQYh3TS}>XPtz-C$mN&xv{IwmTk+vePZ`t+|#(dePA5hNk1$l?MA0l`a22VX}?}!Lp5&Fehlce%tQ8V0zov'
        b'9?PXJylvZ-ZENkzO)p#X*L|(oJ9KpRPN|Ms5mPSg8+_wdyJ+YyhSgNXYQ~iu%KtC7w>jG0)$iEewa2$tb!>at4K04`#0?Ftji0og'
        b'Wo65s3U~hxTMApVji#_LN`G-pYv2AM(ZD&6?aa>|$S+1GYt3bY2X<-m(7vYWB~3Tx<qEWsVF9<ac||xkoL;)5ZJ>GPV^OgeToJia'
        b'Z)QAOwB`EdWV?b#KOV5{X9s%9w>1pz%dm7&;@DXT%eU1#^Ed3OXfEmt=1f?S7qu_{wr|5-`OzEyiHWh%T^z=i7u+}%7v<h@X6Hm*'
        b'0ValBW2z@^-JJc1cw)3-_10X^f$ChF^`hf(E`Q<wKF*Sp<19HIXG5%}DsMw3>X@@QEcQ2z3mYK^+o}?y_ZKbyP3xX@$KRhGj20EQ'
        b'f4Hc1=DOuihc%E}JG$;KY5hjD<*44#c;K%0h7%uM8#SnQe5m;0uCD1@drFT-6FxoOu{erk*WEt}*3aBpnu}ub+W0Bk@BV7*%`3tJ'
        b'YjJD3G)R2Y&CyAX%Iyz*wy3y0XhgTRPH%0CR{2nR(U$noWvRo@4Wt)U#`{Js`yXMz18dgz=B|b?&#D@C=4Wf0vL(ynGozdA@bd%F'
        b'x8t#F@M{kQ7uAfH2TrKRM4vchulcB*T~&Q*cneogN+!n#Szuy#a{Y?1msz@_Y0|OpBigcITPB^6&EZ<EJR{qWwk&bxpPS#&d9e9A'
        b'(V;8aR)1hsJa>r|b)4U~?aAI~{@_E1=xXfP*E{%zJnG}p77qu<SQRBNucN&;llwe9Dg#D8dChCR;o@7S_D(I0!jx|N+QDh<(R-ih'
        b'@+jRpwdBsQC)e3UyI;?h3-znt*EP4aGah8)73oyED^U?W5eZND>W<~FHywY#a@M-OFCFY{FI^u#0@+d5JGZ27<$;<9Mg(VjcJ^%7'
        b'bxjYu0ERc%tZ88b|Kacgt}RL(e;SiLZt?7<!dqp}@NiSNbS!_PX><78r+Zy*_A$rw(hGn5uD(wm?Ecijj!zxjo>@MjCU4)j!p}N3'
        b'bv;<p_x|uW&O9yLesG^pPv*9J+O)bbCDC?==e9fi<ZoP-yf6^%^z_nTzcb%%3U)j(`od{JtEf7D-`vaR_pU2#{@}s&Yl9-C;UnSo'
        b'l&%XlQh%(Vs|&}ls0q_JD-m8hlcq-JcJ(<EN1T58k#v0D)G$C;qe+)n{%vnEo1vA@I6Cl-Ws`zs$-=?0N={z5=06@S2^!n!lKSi}'
        b'l;`?qN3F6Alg5PIoNGI>{V{5;95Yys#4DbQ9$ckryAq?rFzJrWJB~rco+DFB+v4>zyHeA;66N6s&{I2tR(W_dhp)ad_xddezWiva'
        b'HWgIz!WU-2wU=1EJrjP$_J!W?H&JF^+r077iRHtZAAWS=xOnqx2UeBU#nWYL?tQfK)dRC<7tDJ(x&oI?j;_Or4Zl0knyczf%+3j#'
        b'Z}lh7Y54Vlcg{KdCv%>C=bXmu6Nadfo{KRz(fGZA69b;SUU~EaF`7{x%_xc9e`c$_bC#9lBL8-5Fw|fIzWV4p=7g^--x22C1Mi&k'
        b'k-ih>)GV8vtwUBV8<XvIHRXH9j!#*3&Y`)bsgvhS`ObmFtar}aa3D7QPXgX?;KVr_sw<Y?6Ep;7=Zc$(DAapfa|wEHR8mx=+Dm3%'
        b'mfiV^Tr^)hFgX0hV8pB5F{k`^1vHs_rT!gt<>1gJ;@Q2N@xVYfZ>^5c+c13g?C}%J|7zrl*u-%cO`Q6f!!Lx#qNaLc<);tS&&>;('
        b'60<*=P07UihVU6x<FYfd$14o;w+F5|IZPCwdiNg&aslQa$o!cAlWzKL_L)f-WcGpHKNIB4-G>JzmVe}~6%)t({nDwcqp)R_7X_E|'
        b'h}M&Wmqo!x75;1>7v`_SFsVNiW<+7%V3>2mFth(mm{SY)42Jn1VVJA_Oqh{{KN-j!zcr^H=vfpM>XWlQa+i%Md}}Zd36^*K^`lQe'
        b'8=cd$GPxSXS=m~|;N--h>0NfhuqI`L3(9sM9XKA(?niolKe%Ga;EIDQl;l=;<Jft9u_n9G%J)2)JZZb-iI%|`<?q<?dlQX=i{3lq'
        b'gl#`vm5ZzRcwEO<&3@P17KBTs3ZC8&6|@s8_dilUH5@Y~Rh!KdCx#hbw5+W1>AvJi%gS<nlEXnSdafKin1dH<HvTXjJ!`Y~Z!}<J'
        b'_8tg(Eat|Xc_zR6p}u+JW8J&^Iv(nKcHhzF-F?UF>OJLC9_Xvu_2%;3tLLQ47VIeLDGu_~H*cBK)RTIqpsTAO>hoM(mYi5}=7b<z'
        b'^xb^;jrWiGqP)KG!K2IfrDl)VI=$rf_jTOUw>?wP{Jk*#M1JnUelWTA!B=kEQQEzwuVYJJ#l_9v36~cJZPHy2yxB52Z|&W0H8lk#'
        b'SF*LOq%o6M-<}LwDD4%EnXfjjt=u_e<@ZO`AFZ$0RNvke8(!bkx@Pi_if_zrPu1Vwwe@dG*Ut^Ipv&hpP8ikmSl?}Z-M0lPc&X#I'
        b'zQgy%W=)=S{=?@if8_p4Zh899^pXotFYa60*ZseP0IvqO;jSg4W;P~Hjg763J>JnfJ?w-(tMR@K;UoF4cg(*$F~0Td$%{YHe)-Ke'
        b'K0IvJ=)#`d@l3Xk_*#7RQyooxiHn=B?aK{7GpTA)O?%^pT_biK7~Wnqx%i8>6jUu6b#eOQ%`0#JZP@zGz61G8-_2FW$7-DL$ARw8'
        b'_ibC!muyUSJ<xRD_s=d0Du9Dy(5;);a`&4x59Eixt#)+(c{}2}|2eijlW56&b?ZG}IIlK*+|cyL`ijj>(~gy)#p(OfUBRJh?`rR='
        b'7<XQKyzu5&*XFKRQTY5cXo;s&7jFtHCL5N&+<979ommln?=bIZ{@C_#x2JZrH3rS0kuSd|)w&>6SCV?UzT)*%d)LL;szkc{>G^%r'
        b'`?@a(4&d&NzwX=kt=QI<%Ea)(=Lecn3z}AxGzFV}xoJh$)=i~1Z;rN8bLOa#<)`(RFMssNTO~jGNpatKeck8vZSVNWjF$$Uo4RLQ'
        b'&-ePy>FYixi16U<=LdT3>YLivJtdfWY{st!etrJK|6|u@MxAl{nTLK|`uwwrikY9vRrcO!x;Yipb5?z-=eaQ1w|BH|PPH{=HkE8@'
        b'9QvE$zHxos<AQB`X~q)+E&EDtd0^#F;x~OTw)~NneQ)kfZ~eEfH}1H<|CY`}&y+lQT5;c)zV6e4z~c({4P5+x)<5%FaE*-W>pnG@'
        b'HF3u7f&S6Gy(3zmNj^0?ac{UnU2$JYU-v1&((2v+I?z_$+B#zEy~%sa+eRnOYW<gz&FyO+ezSATs^LMCDePyG7}L5w**-c5_b(;u'
        b'Zx5E$4NufXvkq-8S)2Llopn{Q;_%mH6T`ROTe|uF@H>$02hJMx;wSrl+1q`%H@K1uHx9JEQD5=h*897nplc=<Z{3`#_(tnDx@P=-'
        b';Hm0KwW~hR@^_<lGzQl|a4h;edhbsjYA?OFaeY<T4Cw4g&k4t9os%wKzAI>JoH;oij|O*J6|XK|{#^LmSLI#jC&N26k$=-*{yg&F'
        b'_?8EbuC2~%%@mA$KGyeGZ}(%p+rRadj_%$iH^dIy{bp}_$<L-vtD9M#m@s>Ka#s1C(W~+k<*D<Nb)!GNB3^h-EIq8Jvu{st_rty0'
        b'J3cw%cLUFj9{Sr;`gZqrKN!sTRAKnNckjQI)MUQeySDPJq9^Yem3k|<!&A{6-W%NE1r^_{Z%?HLx@OkaR`)#E_uby^?*@nC;7$J)'
        b'tl9IezD>Q|cLvjs-So48tv@MUfB&qh!Lh3wf8X}TvqoLmma6%?QD>|>^U&W08AD=3cwD~UvHaz>xm)i^wccNH@7$gjV(+bwz0z@H'
        b'YU*fX>VqY9jXgX2GQHiIAaNJ%{^>w$`2(rjOP+7PxV?RJP~lkLwrb3t(aRsarN90YB|m%LMN@+W{Bv*jZ9(YI%(ySO42J$XUN|Av'
        b'^Mk&1z1?eqxqrX=`vbB1Uk91lR}Y2z_p2ZWd;3@pb|}ihz8U6V16}i{&Kx)L@b5-`|M$^;Ty{>F4NbUj`<$~zeSBT2G1!k=|2z9}'
        b'@$JvIFMlAL>N}>juNq!Edile_L~x{Aw^!bF&zRKf!Nrt{E~eJjH5)Qxwr7%C?@gsPcWqr?dS83k8*OdPq)|Qh^iA*Wo*rI-yPF4M'
        b'b>Ve3b@_wu|3FaDJ}<aO>U+CC5G;K4rY{e)Tsf+?F)=2*+GceG)$-uRuWQ^~73Qn$9XsX(t?2eSxjgNY@zwYA+!}tLyYZ>$snWcI'
        b'vHI_aJtPiq9f(GcJn+EL=T2X~J5jvgD<z-#){jP%Ry~-%psHlyj-E5l9TMbzTepAV(2;`G|K9gkz1?-eCHdWsirxu-6Z_G5@!cPc'
        b'ZT@uI$mM&QCY4;gGMR4rQEhzaugC2S%C8CE4I&@;#?hVmS3S76d3R4Zl0*KMAxruOqRT1Pv%7CxZ}+(9biNQ?Uq9-r?CpMUcp`&*'
        b'C>ET>WJ~24!8!bWeMM(|x-0r2<TaCrR($iSba)PDp4&DtxJKi>-SO}mo$<3Uj!k{B-tM;_4fC=m24>Z@kKg){(wnD;9f>ZuX8fp6'
        b'-<Dc?#i)<BpLyu>rJq?6oZINR#q!tE^IC69HMN(t&+GYh_T0|A;K+5UtFA5i(ghd))0yezyH=eZR1h|&t4A+?Ed24r(bcCf|K(G|'
        b'!aq+>pWf6}u==jPmmlqZ<<adOHx=#}2r}MuN!7lRGj_yp`b2E=H}0SGM*5atAE_$Yn(jK|J;i-Ld$jv!LC|qCwhUB{NhU`$wIo-K'
        b'No)^RT3J)v_xPjT2ObUcx{U+Xrzge-%eQV%-g|oIn8fJJ-6hX&-mv%0>eJebf(rGd(`JrY{<F-tOO8x0Y1*88e*C5}L0w_woafVJ'
        b'L!XP^R23Wf?dOji4R44eEtStCUi<#&`hjBy^GI+o3lC(*EC`O~GhNGSW>$?Xd|~8cFKpdedh`8PMt8)-`+l(KtWlp{J0-XyK7Q+2'
        b'hdvw}#zfimAItvmcl3GPRY9iqv7V!04~zpH)fe<GO)XedvS>-c#W%kZ9=0*TVY@jvg6+eq$1LBI41e$Mt4$j!S8gAb42rGI$-!c>'
        b';`Yf!na)(Qr)%r#(#`4c1<j3B)uVbg^ff)&-4vY9mu4&)m^A6Ky7rp2%SKgS5ahcR^|6^9!9h6GQ#$E_y>qjVUpnVD-JD!C_w4+e'
        b'F3652G;C$r@Ty%$tIMLTANz(lu`BmJD))_lXXBE89Ju9yJI^nyt~qn_o#(%+qb1nrXPXDY%XZ_qV|_li<Zpaqu)k8+_v}lLc7N&7'
        b'jxRqNK7cqgc6iA^=Az_;HwHF;d&AxlciuB3`wX|{ffrNvB!g<o;p+xAEGiiJ<+l?Bv*HsL4`ja8wW+MGW>a=pq-?*h)zg;$amiN('
        b'`+fz}r)^yGR`%KAn3hZ|6^;Eg@45WssulCn`Qh-&Zw_=e?#!QX?Z5|$Zr{A|$UwR*)7iCQQQm~#Xa7uBZ7N%NU*4vw?5NbKap5>g'
        b'iTq>jg0-2vaNyf)#G~_rExfp6`vXU}#FzYbU`u@C9|pGMFL@z|YIEnNvcoS1f9%W;|Lknscx$-))xo+`csyz!?XG>a<J{nQ{BpvW'
        b'*wgtzJ`+~CUJ25ctCt2bhv|53ApG~pK<Zn`jfV$5SrqQV{(=cV2zTPkon@DA-c+_F|L`w@t<9_o_F+@mh2b6qoBQp+?iaIl;fkI_'
        b'aX606yzm^2TstI;@P*)599}T6ZS<q52a-!>4b1=0#-9&l=C;hNnQ+NKTUqN3T~TziH+Rhnihxb!?fJKVzxnljvtOwXe?g~d&73{&'
        b'ZMyMWO*d9HH7y7$JL7^a{wnwEZ}ns83&y5fmK3Cyj7_gva{7_<+~EJY=?UlUc(HE6?$^V1L0#^<rqyLtRnd4v=l(oa)jd6NdpO!z'
        b'^W>hWhQ2FPlj{`N@Zp+<|Jgh-oZbB5BZo4jP5*RiGM$&%&=B0t6^Z2b<c7U(HUIjNV0q?+{LGeun(hzp%un3a{L64w^Uoid^z+I?'
        b'kJKzIne@9=eKp<ZB;wo0g%MZn%4@zd407?*rHwCa$=lfSMs%*@8!|5@ew--Y+|fKd-01eqYl*w=+qNaYxi<_w;YY8{`^=CjNB1qP'
        b'+c)i+>&}f=?t5g~Ip>}GzJ`5|oS$FQ@M4g{n#}d}|MS$EhTkNohv}@zyjZ_EdD_%nnUd`f#Dml}W?pRG8Af*6^eO+bZ{ZpHroHdH'
        b'bK{rZ`^c30gM`-fjA;1LBUKCES9#wfQ+5P@oLiN7Em_%AweY;kA3oB!aB9`U+R7gU0ne#gIISwPr=+TB&ceEDc8zb$#A-4REsJj{'
        b'Z2n$!I6k^~|B#D1b{5W_+SUA5`+_-_PapZA*u_=Xt$pgEhD3ZzUe)y2gfF~t!Z&7H;uHSrwcNd%d)7DOwUftauNmw&6<qR@2g3%}'
        b'VQO%Ga6Jc?+~LL(*Q@_%Oa0UhRhihl^1QH6tqxXP{h6IZns0pMSl`ekv)&9&W^hd&elt6S&areg#}WlQ3o3fH<TWlF+Wf6>PZG5)'
        b'4e^%lid9ouGT&^uv?v|lnU@|Ne&aYSmcDx1RgWaf?%T1oaYg;sYhOI8>8y26AJ}krtf}?YOlL{MNA?Bn^;o*Jwe^+Y`VB|X4{p1v'
        b'j$ymsir$YWio-2!54N-_+S2I3EhXl^V?#aDs;>@*{K)o63h%Yxx@!K1aIKciL&pL~uLraJ`3A#W6U96$mAW>uEVXJ~Z9E8ETOJNf'
        b'6*Osc@70=5+qbqVFF2IJ0bSW1pYX(MgX1qW$C}sgJ#WXm`p$c#yY`We+DEo$zP{wKfiUtddCh+l#$8uBIlm@|GhUIdEpKVa-x&@H'
        b'Klr{VSpVi|{WBivKJ$@|>R|njCB1{|Uz}aPCewd%1X0>@>#te0clHfUEAM?*-`GdG$3D_ADu`msgr0$2nTqfsXI}HPFp^oNiSdn>'
        b'7R`*$X~>&7qT<Fm4f%DIQA7o~bKdra=vOR?A6Y#n_-9p7@Xtx((p9e=x~RN9Suk|*gyN~I7mb~s?b>|S^abN~jjdWx)lxSkRn>J#'
        b'ero#S`e;0ek&SQf&OHYR*DbAY3f4U}Sa;^w==a9Yntn;VZb))`6t;R`cdoB$s`b^D%(AMEAuHQYY2LFpXxY{r>`DwvRj)X)3|ttC'
        b'h7Ow>>)D*nOUybFTtY$qmp^#FgmLW2#qqQKe-cM}(VA_0w@vA3Z7bOl|IwIXK~b_cbLz^vcX#*h-`2bTz=qg_8=_rLoZY>D|F-@6'
        b'XJp6Nsfv%TSd|!d#=Y^DOgzz;jDDm&9IJm(;<T+zuO#A4XNIGk_H3%$wg1fO<oXq74`2PIM0`?yW!t_W<k+y^=cfGZGnwZaQ>lVO'
        b'O|ML>{>mR}M~%FGSjU=uOGh^}e}8}C{`9Z|!wM363QJ=XXHNa$%u70M-nVrA#O5vgw`X1mmjxx@i>V#!DppS(mfEv!%C&n_zfE?='
        b'tBb0CpZlJ_`CCEIzYBu~DgEs6py3H=zCBnLZ6dfeemvth1I@SXKR=qzKY!1RR|cAI-Jf`WI60)E_NF5P;WwPw%ki@2<~#RBL+90h'
        b'sG+eTudzEht8!*haB0pQu`@5YkdA#To;sKebJ$FHiryR;yoU1f{xM!%mMC6SRbEx~o~!OmE?RhMklsZdg=ZIi`n3F>c+Zg2kL=3S'
        b'Z_f;bH|FYSTSK3%Jhi%L|B&hf!M%5&yFOT9S7pgFMVlvg4!!(}<kH2}MP0XcRd27qscUE6+Jz%q7LEvltgRfmt8&EIMXlSKqJiKa'
        b'4)cM^5euewT{QRRsUI#Z{N+HHp3jBpDXI$6vv5RWc%p3f+I6kL=_~4)6sGx-M39oOKhMbKE2Fd&K3h4Wx+q9Q^@jaJb`}KNd8TMX'
        b'Wy$5^fA;08sutH@)0O#l*Z!eFeWT;R!c&`n5N@<{WTJS_eOn3-CBifvs62Jv8?UE>w3W0}mnEkMN#0U;(cGvT&xhkdLnFAZXI7=J'
        b'NEBQ+`kchr&YINsSM2I82$o;CzPz^d!jBf!R(00Yejzy8`O(p?>KJ;)Y4MFW3~VWgz6FYH8J6wy-4R=J)5Fa-KAb&s?Q2>V4r{Ir'
        b'cOsFF^3dd}DVOXBa=Om=<Y6rhBdd#c=2e$P7f)yNjy1(MC&t`a8+L%-+O^=e+Y6RIwX&|b`Q7`&?<(`}Ef2R_xH}qGDw{`#rz@Gg'
        b'G+HuC!`wEAucbOKnDgR&JBz|hym|EC^7h>F^yo0(-kUDl5^o#bQhn-<;V0!c3;XvjnixA{<gg9l^%2fp_)^c#A=l5_QgCQ!EU1-U'
        b'Ul{z~b7S?$AlX}n%=p7V{Z$|9`S|%qFB$sr+IQ7oHNEH46-TehBtKr8S1~j_F&vZhs)wR7DYyjFJF>;bylHQw&yD6iGo+=uG&|}+'
        b'IRCz*$I~?{oU!?}^o*<Kc15S^%hPB4JbI7RQg%v^x}|$2B!;zIn%|OXTC=BTRbFR2U0PifzUu#JPgT{at?A^d(%_68`|XH@;d8xt'
        b'zlinyYftx2dOCj6v%TZ96RsX;smj|Q9JDcsvEgyKFUZ!$G&L8rrc*7)%C&5Hc<<HCKaH-f`0)ZU9o~lN(L3{^Lig;VRk`t^7RE}t'
        b'liM@z3u~Ky9C&*D#odX&32F|19O!vIomZ7t(3CC>2kHruIGA_t&p-cf!g1#Ya^shT`RvBG2mWk6yFWjQ?GJ-(jOe}}7Txz7e>`yf'
        b'Tn^5k5=4Ce3G=(J?b&v1PmtY)weGWH$Hqh*{NBDcI90XxM5SHN-rC@Vq|0l@ow{RKSTdI<hGkZSjewr?+V8!wetqkT6?Yx&jMo;`'
        b'P7M~PuSt}rg1x%t_-Pyy<^dgrE7uo=ZG!ZU=tLh+%gkU~Gru1dh&_8}hT9s^I6mA~K`b#M*wzivw%USiwXSb!y<x?Vt2=}8GVE1Y'
        b'5Co~cCNZLZYO?N{<Eg9-l2Ox9c;5P=+OnMmx!w5xV|zpX{PwE<^7f7$i0zYNVLmW6*v2g<ZR3^|KVH@ue`ZL!Xn#REogMt|r0vX)'
        b'wsXN>+Rnn*3HNhQr#fj2;GXpM@4a!~=3ruVTevgnqV)CA%@^!KXLRYFUDUI=B`=n$?P}==e`MfTyK-ki5O~?~F^U$(#(pR<r2eDp'
        b'#$J#(wKKk~Xwk%X9V(3d__SqZ`|}n}9J4d*304?;`e&VanFZHoG6gT*S9{IS#qVDJ%lfG$b=NFdSP*1k3pT6^qnkKl=dvJMU3Tv5'
        b'A0&fyil-L_?Z>K$ut#UQwzFnuVX)bW`RzgBG4Gt$H*^dw{CzZjTiGc=6L-&{XmG2q9jgsQ=?&tJ?wxew=i)7U-b}>*P<>9A)kkII'
        b'i#Mn9X3tN4d~{`c<j$h>js@Qd4|I^=!ss~Gj$FOI_MXJpXfkNEl~;{Bb$fOA%LG9VQWNHd=dC}ZdSqg3RaJ3z=CPRPJ^$viyqb<-'
        b'v*&fq9=EPAD7)wF{o_rqolvj3BUdN-*1kWf6Lo)c-?ne=yX2JMetzYod%rt(?>F7haN@l`_$(rodUb7PS8%#+TQ{t&G4aN2Vef<7'
        b'*ge_%xH)#h<sDuV1+fno<!ZR=_T;XR`rH+=;d^gvo*qoxKC|H;_pL5(SiY|_9#&j~0%PWgV9hY9ncv>tT@meZ&*sLwiqtt>jltD2'
        b'eqEGDo{(pJps45h@VcEDUAG0%obcXC9ly8MuM2Lik;@8l$@%=AC|{kjVBgNXu*w|-uPqPOtG#ARJa-#pZ?@6F%pf!QKv6b3DHzO7'
        b'@}o5T-`(4t$L{Ts&kZKvBVht27u1yoiKyS#*bucGf_<+Um)Drd`!gxoUY-A!?#KTxX_<UNTHf=2mzMZnPRq$<{X4RtAPc``#mJ!6'
        b'ncaFKdn$tVN?qmTAyeMoJ13WbS*2m~EZY2kFK-I#++l@#M@hw)jvwsV_Tt{jU%PGeuyFCV=k`{7IH(IHa&_o%q?Z3q{qW}x{rBsK'
        b'XFv4+qJ9|UExV5Vu<BiXJNI_~>)wuk-Mc+AZ^>`ojvk7|qw#3M7IawuYc70f&5(yW8@G2?uWD{zv*gXeM&%E~?Y86v#mSMj()Dd?'
        b'8^RCZCJ$fRkRMb8(?t!N_pa?urbo9=32wV6Q?72T7`<}s+11T$Ym(`PrcHTGHzzw5K9ot9#5R>CTVHKmpX~VLL&@Z|nf9>HXi%95'
        b'YMY(SiL&Olu+G<f)!xMLn{Unzi`cUxQ@yTdQKqwDQ<%=6sh=IEtRozAHb1zn>zX(IZeVAAwoZ9VHmMbpgQUef!*td}sjM!l=}y*7'
        b'sjAAW**qk;C`z`4`C!kqs=VZ+f+&BA;wuQ^o7KGW#ewjNMHt_8gYgvvS98#O31Xc!C5W}*^LvAuX~W1|M$<SxY|T8qw<Rw*arCf>'
        b')uT7%hmGBef?4@9^Q#-r7?B^g>B8+)jF>SvrcbU;_sPB8pW53oKR7S99X|N>e_5ydGx_IzC*+@1Cy$pI<>C8td3fGKQ68T8leTeQ'
        b'-m<baD|TOg!!;Aj6JuA_<poWyiSLQZ!=SBoN7U9D-t)d_fcD%q+&m?^7~}hgEGybsu<VJeeigN~3Uh6(&vwQyzoD(D>z7>%(u>>f'
        b'4eIs_Pknabi27w+hla<3i~f$H{e@fdpWn82;fUtzc1LZkQ$I7cDQs=6tsL>;VKaV_Z7YQRlhY#?O$@W2!q~j^1v`s&Wh#O*v#2W8'
        b'ToNXsdB*PGj-NdI!l2f^s;)A)C})*cj0>g`<HDQ2aA#g^c~mlH^RoFPYQ|^p`dqyr%<r~mVvXaAqa1HuQQ^s1-n=)CZF6S4`Q<RJ'
        b'YtG!=l1ZLd7c@<R>U4fx>EzMp)#U}vqM$-u5Ir;s8(>d=rZYaXsAYWVywQ2b%an6+Tb>!zDEHhDjZ*M-IKbVXq~oG@reoTWuw4`+'
        b'qcPa^z9=2T-jR-$%+t|Se=a3KgR1`9$^SGh<4;V>ttX@<xNefK)?{8vRR!gJO~;Vj=am2H^Nb+x$UIb$?X|h>yAPi<u2Evz$&-5r'
        b'CnsMLTt!EJ8vc%I>qB?sCEC82F4-~s;;_SJXYt^-u7mk-_+YB|@bGYK#>B;mqQi;U>N&w5r!7fj`z3EIkA**dmx*m08ihG4QM9or'
        b'40BfEv<XGQ>hWON;ZtIRzf+hvt+^#^5d~qx@gkbSzem=D{ey#cO!HU5$>x82IC}KAC4Ttzf#{|U$6a6Z_MaVtaPWQ$;+t4r9Chv*'
        b'GI45r!au#;{Mm=sW?oFDyXw=~pEGM4wtR2q_+U@R*6Vq>Z}G$3iy!V-{O~7=!_WEGz1{rDhm+M^^;M-y%ZsKA-5qvK3}1Q{uS-p7'
        b'D4rTyRoXPQH2mOvYI3muQ1hh^2T>hg>5ZR;U49mgIQ__fveIDMlQZ+jR>k7=sag4{<eJ#jjwfC&4l<flRWg}ckenL!+K83cCzETE'
        b'v&w_8RlDAss_9D242Ka&&dMLTVd&6jhmCr6%o)#4D;yWAdHBez{L9L(9QUQE$%PFiP4$JZ4b<#EHm~NVuhiz(JaA}LetY?*araJ5'
        b'ZfHmbVSYOhggmhS$naCfoIdI7x)0QJ2f+^PFR6K;cW}*BA8P;Trp5Pu;Yd?`@)r%MruyCC*x12pL6Tx+^@*~ed<YU4Bq|X<<w&CJ'
        b'l;HFnsVW^?m71CV+OtK)Q-g`u7QL2AofCF#sVPlWHHSma&MHsk=TD9w+oMF)DbabYj4fRG(Cq)n|8Q)<gp&7HC8JRjF8IyBDFxY)'
        b'9D?Ik8&Cb}<=V1TNqKEms<gbeCRI>g+n7p}*Um{L%WD^<D$8rHNmZ5Cwxq_D2eDrD*T1NXr%Lkc%2K8IbycZ?{JNS{BEPONmCUc3'
        b'ld8<GTa>EGue&BSF2AnjlxUp6M1Ja*3&Z0)E}8sgxY_7l4CWWqXXl@jOioRuvWv2<_}J`{*k3gH!L8M2y!W<uT`;ZU#rnTLWA*x~'
        b'pFgqo^h<C5&a-(_R*!t+b1x47000000000000000000000000000000000000000000000000000000000000000000000000000'
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
        b'0000000000000000000000000000000000000000000000002+|F8!K0ssI206_k)ji9Qks;a80s;a80s;a80s;a80s;a80s;a80'
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
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s=^)|2mk;8008;F'
        b'HiD|Es;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
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
        b's;a80s;a80s;a80s;a80stS8>AOHXW0089w+6bzus;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80'
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
        b's;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80s;a80sw(ZlAprmY0Dz$XuU%mS0000000000000000000000000'
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
        b'000000000007d}~$$-!'
    )
    _firmware_identity = {'protocol': 1, 'firmware': 'CNC_FFST-S3-0.1.2', 'app_image_sha256': 'c4b028271f970e453a1cec406e278c9a22e1d6921d519ca6e201318c16fa6df3', 'application_file_sha256': '7756ef666d03e2fd8799a2772837cd809e4adeb86dced46ee6d75cf92ac4b532'}
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
        self._send_lock = threading.Lock()
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
            self.send_payload(b'$$\n')
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

    def send_payload(self, payload, number=None, exclusive=False, probe=False):
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
                self.port.write(payload)
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
        self.send_payload((command + '\n').encode('ascii'), exclusive=True, probe=is_probe)
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
                self.send_payload((line + '\n').encode('ascii'))
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
                self.send_payload((line + '\n').encode('ascii'), 'macro_m0' if is_m0 else None)
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
        self.last_log_message = tk.StringVar(value='')
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

        serial_line = ttk.Frame(top)
        serial_line.grid(row=1, column=0, columnspan=9, sticky='ew', pady=(6, 0))
        ttk.Label(serial_line, textvariable=self.connection_label, style='Muted.TLabel').pack(side='left')
        ttk.Label(serial_line, textvariable=self.last_log_message, style='Muted.TLabel',
                  anchor='e', width=1).pack(side='right', fill='x', expand=True, padx=(16, 0))

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
                    lines = str(event[1]).splitlines()
                    self.last_log_message.set(lines[-1] if lines else '')
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
