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
        b'c-riJd0<r4)%cwyAqfvj03%D#mym=6Ct+qn$YPL8_CS^~31JaGGD#-MXp)ID69K=pW`f0l*s`=0tbUzDsfbV(ts+VVY7s3cXj`q-'
        b'idI@{U8q_U$nt*Y+<V__1ggL7uXo_RbGLKXbI(2J-a9Y<(5Q2t-ky{DIUyt*9wJHjR)uB0ws4OIy^=Ho0`Q69Pm)<nq((@DDKDt%'
        b'5NY8FfhQE6aqzU+owil2)^;&xftY3_b4v?~<~G>dI_&M%c9(N*z1{9=wObmkj#bXijt;xSHP`8A@DFZkwK!W+8%UeYY4^*Bdh6G^'
        b'tgG5P+c0b%2_{<Quv!{dIhz_gE|0RVu{Lx9F;u0^(%wk1y`5Ow8x1!*T^5JS@NKGUYj0@nY_$4Eb-HY=sV$h1k!55g7_$lj#G6Ix'
        b'v@|w4zHLWXogJ%eZI)*1swTUm&EkTN$hWjMbhcVt)<&@fnnDWKbXXg_zM!f=A2i$S?ao#9yR42@O9ugDYg)U?TM?_%X>}44yd5sF'
        b'$zp4TjBM><f>Q@ic0!|=l;BLB5J4>UP^F|~aka%MHdtCQnZ+fV^F{rd1byZjNYMiQ*lHDH7l;*0%F4b&1JjJow1DUq3pBIQ;<C{3'
        b'P7vpb3l@la5}3r8K7Un{t=$&bW*&jWBym-})47Tc0x}5m!Z`dNRE-Bg^%7|r{<%{>X786C>gOW$olQ+v$9L@*zhDRSti25i^=D&S'
        b'Yb%eSbCXS3hRK6DxgMCr^WDS?A4iegt`L%YsGHQyG0gnY(|{qkn`FGU5a;;w*{>~3yXm!snwywE2A-+lZp;<xKE*V8Qb%)-q+)@5'
        b'B)zuKd`_sVfoB;!E8(ewrxBhOc+SD|5j-Em^C>(R;Q1P!L3qN5P$$4s0`4++o}Nl_&qb5m?bArEIfCRK1;6yvOIoahM200|#<u+('
        b'S~n!+LcPo2c{r5hPN`GZK?{fr{8J%6tQ{o!qJwCmu0My`=AuNZ!%E-NElFAopGYK9rzJVPwEd9oJ}HT&-$$f-2BoRsj)b^*y%;Cm'
        b'lZkO(NKy_>GY;}>A=1J@iR6M%45MAEYP}5#f;uG4f_~Pp{*H&b7bK8e9pJB_@9%|pY2i`GQZ-s|4$77^M0#;V%FUYysizW_*#&97'
        b'TNS%aimoE=Ez-F#VhthDbBOglP3(_o-~$+V+~X0(?^U_)N6%i>`QK`y50C6s?R;I+v+ohl9Pz&Cr~5r*Cm~1F5c+4$d=nA-MRzwQ'
        b'Pl=d$0sO-Bo!@BsJ*tFD8ezJ1L}R#HioIJh-7OszNwNlBNm}<BsXI<YzgAEKifbS{lSr&fGPtDKPhE4?DIIf32m8!@PRaV2Ce|q#'
        b'oDe?#tV2514&k?iUX&6R5%&fx)!plR$KD}zeFXVss&msK0cWYHr|b8!*E*df)R6Nn<a_~1$kU`m)Mj6oPz*J%JsiEW1aWq>;Z|v{'
        b'W@oL&YS!#b)R>k@Mh(`wM5~`SFGib~f88_H>h+aGC`g<o2={)IHcpsw(4*Eb-sZN_nwX`3l}Wu}XUn8xWzvF(U13L`R(;q<+;y}|'
        b'HSSfk^Ve&H2)7ZP3nGN+ZaunsUcD$xc_vex=OI16xhPC~CQ~JZcfD==&A+?TA~zR^!c-w#zkOY9mZ;aePW`6;)vvmq&fOj9$y^ux'
        b'Rj45iJ2+EgFmi0*SkLiXj#D{K;aJD<jU3P6IGN)lj%Rb6$gn9vDhorGwmS`nGD~ZUlX~{O$b%wT(DjlqnYm&liqEGJ>rG_lg)(hZ'
        b'gL?fzNvHh=@P5hon~Qm#?h|`p7R<L0=$q?lH(eXzo+3S-dE1sLQg8V7X*;5}Op-SDM$)&qL1lef>+wuEvr)BWqO?o3d3R*@Zt)3K'
        b'!gCO+JqMu?5PB#|4nLns+~Xu694fLS%pD?iU8Js=7ofN^qflJa?w_9cMgktTrV+}^?$OaLqoc^PVPz4U8Ow&bheo$PMrdHyr*dHI'
        b'H=|nyFlDb=xB==0t_^DH-SXwAP=R&+*Qgwr6z=|Fv^y@+{W-ivcw-jfG)E85kEZJTc$E7wa#wiVJ|gap6pZ3-4159uw}<te8};mn'
        b'?C<OL>=0>tw!Ak=Qy+MD^z2_o_wSB8@D9Aa6o<n4-WomnJPy!vSj?e_GtXn>a}kuP^}mnqj+E2x3OjZda}e(58HCZm1Fwv}cg=p5'
        b'EbPF^(Y_O--VDMxd6@g9(Y}{P<x+Yh4*d71(6yiSOhn&{qX%B3-4(IFH<AXqUl={O?|qtuoHZ-#*-_cw_p8wZzw%NYczRUMjumiV'
        b'6hrq1gogL+9X&G9!$QJY$nH_*@3E17kInr!4!v-Lkow*=M<yQkjKi>g4Es#|o?4hFbRG1lFzgYUZlW;rGYC5}0fV+<(98?KvnCQ-'
        b'H5wO3&R<mb*OSdCry;Cw;pnl2qr!O4siW@serXTnjlSVg9rsKHVQQVHfr+j5ByAJLIv&6CI!#~J=s^!TKV8$~QTbwFZWy{o1@--X'
        b'S%&1;gyq^J;7nMhg;#_2J@sid`mHx;cdpYei0D5ScD`2IcjxG_J4ZcF^`C|Jqdo3Bu^y)*gz_V5Oppt-J8QKx7q@M6uWEZ(=F}ak'
        b'tSD=>cCYG)+PWN&^)@Y?59eQ#D2AGWgtvxjz#+^zAEKf4c9R3Qj>eSjh5EWzU?~e!<?8-fB=>1?MqI)qvN)}&>I-4U-tpEb?1=e&'
        b'WXmn1MhhDiqbk0yVpL3v^7KX~ySYpW-y)70RS9g^N=7fFsUUWjH`cSW^Zc9IU2ZYy$DX|j*0;2V+|ez$ltDne@>!_avVetbW{jpW'
        b'szmp=Q7ViRPHX$-W3QY)t?fS+dH!MT5f!Xw#@KP^f2ut-J>fnLtbs3RJ)dYi2m3w!J*PFo1a~abdOn%#zA(~lj7oCDMApZNhJ;af'
        b'!f3KvZ;ZTen^u^fP^+Eon0O#=6gui~nlN5}c-{FGP*+cXh_w~*qt{yNwS2r0A=byK5+_IO$xoaWm6$diLIsWfL$h8aMWCt(Y5ICI'
        b'0ry34&w@2j_=*R7BavWuIVZO!5wsN05l+B!7d#u_fz+Uzh?oMj76}!E4yN5nFT$fi-3##h@C=~7gH~5vIOtD6`y|qXii7{b2+MWd'
        b'Kyn|0XX*@+8wonxRCrLAgGoZdpd3MrB=3S=_%%G+V@NJ&RD@b`8JN#PZU&MZSx4JHjp=8oBci?rX>vr+*@mI~R(Pg>J0JAM2jE!?'
        b'PnTI!m&0_apGR_?it1sKG>ST#$n`d=Lz$`jC9cN)8kHq1K?^$QV^G$-4pN7DEL0seS0dd2b<JS<73yCCxIcw9M9w6+b3mVc44xKv'
        b'*1|In!tMv03;1tYuPr<S?OpbEPHq^4mAFYA(}&g2-Vy0zaL=RuNbr9leGYBi4>SqzWWYnZGoV&CLzyR`k6vGxkNLrK4~si0-7^k!'
        b'$&90s&%U<sY3Kv&OX(i8i0$ya0%I5o`JQ~S`m>x|<N-pqK(Cy9k%$+5F5Ph9=a6VWw0)l%SO9f)EgcJ@+6wvi!y`;0xw}Cp{^vg>'
        b'X(hC`1s)eX%m$}Aaa~{b+h)k)NAUbhk`|6i(#sOlSHUVjN4W_V>WfhDD7EIhK_C5saoERDUL9@!HH4Di0O5bdK~a&T_hNV$c?s}u'
        b'qA{OQ3H9$7cu>7Xg&R^Me-7nNR+Dk#>F$7-3p#HkjCCE1vjF`W2~QpPrLQFEBPb8`;9(dC>4rh6Y&!55<k#HP)I`ofeV=|wI|c0#'
        b'q=5|Ape_v+g-YK8_3x&7KF$zmEy&&@YMpwkO5c3&nzPB$u{qMg{^Gu5Y3F<7!GjadCP~K<Af#mdB_MYvNPSdO8cf2ayye&|DLD#V'
        b'Yj7pQuw5;}%%f~oZ9#AEu^8!t>m^t|k4=|&L@$fD4nz40+$#u__=uoCvQ2zmb#8a$bE^G^=?YHsS##hTX?$8;nhI7;eKr-8SZ3+e'
        b'mv^X(ZYG9tQl`eJnU-Cc`|dgjKiOi^O8WOyxu+t}oWj(vw2V*7UV>`en!J5S&E^_Vp3T)5vmEouY!S4=wS9x5bv5hEOH>|+WYV~$'
        b'I69>MgjARNV@$QZeh;Zji_C4nINNr3Ia;DojcyS%!nKxvjBc)8m%Bt&R}g6~z$B$D8Ph_HuSj}5l9%kN+C$6*k@|Tw>s^>*nCZRI'
        b'Tw0W|h0uW6UkzkppI%I&<)fa2HH=G&PJCrT*H>g(F4@+%d7FN7TqFuuT6xpSQEm*h$W7$_H79_LVT|AK5VP4;Wg+^nfVEtwCmfj|'
        b'dRz(TByQiBo*gyrYuKfAAI5bcNh?fUrWVxZy3XwR`lNLtXy%W`?YntSqL{fZMYCt}aS!AecJu{NSdnl^@_4?E+m|oSiJbkAdVLZR'
        b')}Kft#OOJh5v@LvK+Ku0#5dLJXJG|ms+XpzPk;=202g&(h4mY$ErNM+R_y$@<T1O1S#@<^>(e8n=Z6dHp+Y~U3d#hmv2eTfD+!#T'
        b'u*iE<JHM1NuDzi@9*jIp0xe`|68;5ggiS{@In%8dB#i$7k3Vx-ganHczK{g<%nQ&4Y`_D;iu0dIf{+6BI3nb%Ncc?Z-W>(XD7LDf'
        b'V5_FT9uq2PZquy)vqUm}vgyPZOrIBzi_cVFbGCi-n0>VGw$X$ATdljvnY5@cJp@ddEEQ-}55(NRa`*XHXfM;XP!M7sfKvNCKi~N`'
        b'$z4B6=0w3t>*?-9m3h@@HyA!~B2Q}o-D?)<2lZ<j0V{RWBCItb!i<=RghA+ZSJSJXGVQ3}^W4r4B-y?8{5h{%f+6mI{EWL4yFd<n'
        b'^88<<m__aaI@Fq--$+lWlQg^3!X)ctXs=!rU7(f~eS|iHJBO+~5$>B1M?V$f$#v=Ps?mFD^sP1eswMi&B}dfmbc_@aiXD%OZX>#n'
        b'sOx?qy5~}TBm~Ab#H~YjM*4V2rGHd(C!x1EJsd1<Eoc}_iHvzE=Bb!J=t5%#Vm?{_4+;CgeZy$~o*Sr10QLa21gNJqLiTRC4wR9j'
        b'RGE?$V%~r5Nuzy}Mma6FA|{RorKGmK^<UEYVM*3kV#ke&^|_)b>oI#ZiIcR6al*_CZWY!vbOc2qL1z(4MNA`Z?tB0yOw%j#ySKZ#'
        b'yIoCxx~AvkXTmh$o%;@pkEl<ClCtTK?+EWX`40$tDD;xFGUD+a5j`jWDNOq&=`Wi_m&_kH#DHOPl=bhE+<zbO?LmMJC+3L>;~>%O'
        b'hpx$V?bTXGB+sKqg~^^->o~n=6niui;?zQSZ<N?8_M9Bp>QTjcNO$r!n5ah0H88RnhgDr)()1PrWkmO*c6k1x)NdmF$3-hTR6@)V'
        b')n0XiS}uFLT9}#`9=^SP>nkJAB&&q5Zq_}t&eMf3apO8@^&{%sT-R`te&f1N-;UFegBsPTs;)2h&)GKfLP}Wl{Zj9Sr0{NI!=@?S'
        b'MyEdRC|C#@F>_mrrf5Lw`ZDwz-k0t@BZ-qH3Ssw6ig525i90^pby3`~EhS7Y&$4qQFO<|y(cbddNJjci?w#02--~cRhWG=|h-m)$'
        b'le86oJ$BEC;gOLM?YVRRE}L-lc;pccu-e0zX45Bo$GLxoE<s&{8}LM!1R+1gkhmg}oxsK*_WqF`HF@}?`vHt_Z=&xXQL?a}JdExd'
        b'+(5_6LfX_~yeQ5RMR5v<xmsgL^bf}6=9$hFMBQF+TWIl5s4d~Xb!5x;N4h&Bd&BR$&a@-Sy&5xnLgl`TW;*e}+7aRUvI(chUDzkO'
        b'9T?WD+8(v()xBYEJNml5T>qIw_J*wuci%xP(>Aj42OVpU_KvITJbJft!??vu)_;V&X~Edsmqh(jqGyG;H`Lw0*l2Hv`!;m#Rqy-<'
        b'$fVGB=p5UtcCW-x>&HGhwbi4AcJz2e^M-ZZTR-f&^zOy(dq31~o&xsAyCvrzmQGzdt%V*{Z~Cpff)ankh}~uATR+6dl1be&M?_)K'
        b'&IcvduQ^{bj3X=@D;W9k@wx8_8QWnwJG)@y*v%t-H;)|j#O+){x;IaWP9n7%RHy+67e2uqt3wm^@7C}CM04T!qtE{O^D{f5HXbD5'
        b'xt`5iwk{?!da-{PPgcBl4O+Rv476y|Y5%6OAa3~TY1qyF$!;9swlH{@IqXivpe->YeK8|ka8PqAe9N?vzG*>0(Ib7)K|zy8`aT*C'
        b'42m4-iyXO3Tp<tb{8|zs5~@hOIz-T%Yl=EMe&mDkBi~bRJsvZs={8N4s$6qKb6V4Uow_KIw8T9Z`%0AiZ^MlD&m-P4Jlsb{PDUMy'
        b'g@x;`o>02sv3N)9pNIFK`+82nCm)#(4+|4PC(3<3lFo{~6WwnQQ#PBEW<K||F!7VW=AMkq{gpTNbBvAsbeL~I?j3i9ElBsvnDBfS'
        b'ITuRYe;(cyzVVX#o#BDZ3CCy8E}3>DV)5$xcZ8mm-nlez^H;{%vu}&YQe{p%aZ#f7^>I(kL65Y!&;19?WJX$+3XJVpS(csqB*W{&'
        b'Pu$5Y-)Y@F34-R`Wl3srk7?)crBe^Rr_l*iO8o&CYg|jn<}^L5yWMWniGNeR2B{Vor^@q?Bbwq#5eZMiEcfKC0|}L)rF#ws4iEPo'
        b'9zK6qS`bltJCnR%!5kBTL99=Z8@F`{wHrr!Rrk#a2b=muNtkrv8>uIpMDHSrQ!8ie-ujAoVgLeEds-4t8jc={Y<m75-QDwUeD22H'
        b'x5uC9jXE@AW6z(Gp3CfsOPtZ$Q=hp0OX<c9hr)WNJ{PyaSoDSL$=gsB`l&=9pW5x0c$j*_q|m=Z8;+4(>e_6A()!RO!{*^<)5gW^'
        b'd*lR8F6%zYlPyMnGI}IJCq(v%?)$Oxbi%<mBVX-v-#1Km0(L$n8SWhx!XUmUpX_{8`g9J|CVIOX0unq@V#H(ncSm{px_cwy;u6RA'
        b'ib)@yK>5*sOpJ^YcY37gOT$TVwI2>7shZT+CAkyT5lR1o$n!su9-kB?Op41VMQW0C=U&zMA4`vKeNRw_{(;Xw>on5;=*R9Gu^w*g'
        b'@Rn)Abo~vb2G4wpx@X_0K3}|VTS?>rvHy5v!g(kw1h?d+Big;{^I_zm#ncmP>bK<XnR-Oke^zz=L+RnW6SaRfn1_#OjT#cI8G(_1'
        b'R|@?SbIf~5`kVHpJm~4P;#o6+;CSTu_odobFCB?E-bePT+&5!Ipi!W3f=~p`*r~=M@@Ns!1;bd4v#Oo%O3@pKep)?Xnm?SUCDAW^'
        b'b40WLJlaT2nuyG}Bx9B;IVw~`x<0;d+l0)jq`a)CWL1(XGiv4qVK5_eB6RM3kA~lv21;OdTqx+O>SWc4FD1Xd5O+MCQL)3qjUaa8'
        b'hN<F%>%Hc*w)PEj_WI#t*AK@$*?0Z$PB3K8Oxg6v*_h#D(}!c82UVkQ%CLJnBcb~$Pl>f3lCx36$D)V(CJi6-#9Gy)Z~XA7ZO1)t'
        b'yVWeAJ91c7S^W28AlYXj?`c3E)VjlI3W@1k<A%@ekLv#6wPLSo|3Opt^J1T7_~7qG+=Pzg(V^~^+;J`H3nnCh^jk)Tx(-um23n&m'
        b'<J=dAsMfXVc;CQ~ta?Goeg6huq<3xD^7&BLJD1UZ=A}ImK)W@N_Whx*PcEZ<-%I;m0PUXxXfxs_oPBHP*jqy}zw3Kz2&{pn@eybL'
        b'ICSjIp_o6PxFiWvGvYzP5vDDTQwiallOm}m2t4pTP4PB$=u%QV>zcE#4;_1bsPD|s!M@uP{wWz=8`|>vP<BSfbLyg4;yyjJ@!k!p'
        b'`<_#W<^%5?cy;JK?dfs-?{tIK{zyb^_QV4(5B0rF1GidK=f9C^Bd!^~>%enEeTQh^`F~47^q$+dyf|bzFqDy{wfuVM_U24gM%Ii2'
        b'&kr4by7|dy;rjPNPKUxOj^<NJC>_)Tj}M(5j}b>gPYgm!4F`tY2eD3>cYrf{UdADH==J2lzM;N-v=r+XQtigj+HZyo+lLNpr$Hd*'
        b'K8K>C4_|V7hV;!x4L=@g&I~a;Hl)w!wmdd;dt-BE<bgh@LdKJ{q|=(Bzeoq}m&?_h0DU6%XG4ajp*gc>r$rsuF(gDEE+|e@7yVHZ'
        b'LP0hdelirhYAE|YA@sh3YFG~rY-K49s)W$GI@kJB5)q<9f5*qkaa?=c18hyutf&~mwRvWiI%d-msOb3?sZE^{acae>B{A!aO&K#U'
        b'Yz>{!<57W3+?)x<vFqW|T&j|8I=S<t^n`ZLJ4k1JMam1+8a@BWm=Y4}8anYW31mIwZY`5)=ctUKAu-yFr+>K~yDzR!75WLNG$%f$'
        b'_H$2s#`o0qCnLMmVpF6rsk`Z@xI};Iy6E#-FfiZnsOnCLM^w9aSyxH5E3|s?-}>H8u~)C})sK(WXPN-tZrrLNP@nD%M}fS5n+K|v'
        b'*;hUEt~L5`0@NUY_Kvf@C>i53goxW4>Kik>x>&!5xEEpbw~QM)FmC9ft<cT~pI7&I$QCkmOa%eLj0ay(3FG(oiU*Ef5~j_59vQb+'
        b'gyKG(+O#5m%lx4}O!na6$SvtZ55<8=Fgsh_y<Obg?LxI$2wOh_Y>(TqxaNFMovDtC%do}HnU!pb^E^Cf_VTD@vB|gKhJLcjoU{(6'
        b'T&AUTOa03+$$fF-LP}J#<EJH!oBfpfgpS0`&RAwK#~sZ!8k;j<K}aU_Od#w?=w6Mr96GdiPB`eaYr#Md-5YM*FO@{+ny1w69Or)R'
        b'QgNp1{<LMGSq8(YOIuD~%1+OCF3fQ9l0LmVBXfLDtfo617Wl7g|Ek@-Wz+J#A=b|!J5jIAx^t8E(+2Ab36k_%!g?&);VHehY&RsS'
        b'c7$a{&xl*xo1K-c+HlMLO())zNPjH(5O*(Bi++0~Wan|IcF}O`mzSWcx0{5B&HAr}86Ug#Pj2(ve6;sYk`|Sl*6{39&Gx=eU)g0k'
        b'qDjbv85}()0#^6f{kuf>`Afr#j)b4q><!s**1h`@jM4V9o1YL9a-<Jqwfcgi`p>)nVOsxZse2b_6;Lx_$62dc+J3h8*sieXjibA!'
        b'MrV(Ls434lbn;~E#^-j8-_&(d_&C;cO8?3=o8CC~+NHOk1B8v|kM7n#am}u%hu`V;{P^9C-M=~7{}}O{YS<OE;n<F|e>!mfXVTjT'
        b'FxSPs>p_<|83Vco7*wya@w`nP=lLRe%a_OE1@$xOsu6XvJFZV1{rhQmK6|NUa`Ut5^*6%If*4`KA&mfrUYmM<%eFITTy<@c<9~Ae'
        b'm{@mw-R7iqpMj~q;e#(N6Rans@2Pt~NQoFcTf1o7*58iqICeVhnPj!+Rq>73unS*^FhRA}KjT=h2oa`#ldj$wA-xxIXv;45X>G#q'
        b'r0+%G(X=K`J0o-Qrv7Krr^dx+#2pvo8Z*E#J57Bejl@21sVEdCVSL6e?Lp7EIlG0KI${6Q-PUBtHTs?5UGC^bL>RyGM-nXW!gw(3'
        b'im>yGjD(!mz!VHma)WLd0SkXFhQoRf^XvR3>DYf?(v9D%GJ4MKTrXwMqxz%9z2*|NjyAn|%mvZ<N5%8^O0jL11WlGZbTT=ZKzc0K'
        b'?0-^x?rg%#Qtt<c&VKsPjNbc~tiP6=b4DFry?xxchAF#3Jv;O}#?44ub8Uyiv^wph^<d5JiUt)|(7?*QX?~Ks*7!}zxLxi|cMIbM'
        b'O~SoWmb<q8tIT8H%(~W6b15@))0>&mo3>TG6!U=Es13<Tx{v7v>eCuw&d$HGeY#kc;q*lzEK_q^Sp6(jPa~T9TS_nWPbQl;f4#pm'
        b'>cNMmY@ht#{LnSC?%wg>GX-&d+M;XGyxn5D1PLB|$W)uDg+5t`?L9pXZ#%dbpc@pXW6Rt(p)*D}cx>6LkGj*)^X?*H>Wn2@J$1(4'
        b'h!6hc$3-eak~E3x(6~No&vyUd=mssA(8K(EdlSfN&}#mA5lF#$bSGU(oE+w!eJOF48r~ZwWvP27Z8>!@HsO-ltgZbDcRAx)baZnw'
        b'(G+`Wb6g}1Nn{~smPF+ShM1;Z3J$sUvXDu^A$j|7la%dK^BlP+@0XH)!a%yo!o9ilm^!XyG7X6AazP4n6^2!{MDolZBXTOa0$*MX'
        b'3d!rgEX^muX-t0)2r;(kpo6J*8ci_C&~;JnpGhp_+>$7LV2I(Zi$ZB|*qawg!DR_wyXYU%pA^&elzw-lnQq4Sx5Us?H*Dq=!tJ-M'
        b'Niq5zk>=&B@i9D`Uqd!xK*ooILa^(S(SA=-iQ?C+iQLb+mR*%;nO5{0s(<!QN>bPMhnvmuiIe9>uOo@G7A2<LZmq?EGA1R)K6o*A'
        b'iAt3B?yFi7b4@02<h9IZ{e@|Mbg?5a4NZ^))*DaId(ksSg5>p|OGM72`{J1~lFT`AUP_!?xo2JCtoEj~O*HMK*#Ew0Hc#0ckbDwN'
        b'eqHE05>F#w8vPh)rhpp6(==lm^B8Ha4LvERS%qmj#z+$#`l7`9Z%g^bQ}sAz$V3!R^XmT?-}lVmyC2dqy^$%&TU&0V-bC4(2s!~B'
        b'zm};qVv-y&iK>>k9|-yA_1bs)@y0=NV(fy8xoJ^iZ=^nxo@Lk)`PoEI@}$^|i()|Bq|iY+*4sfGoU+Lkl^J3EFtsb*9_-(l8?a5{'
        b'PP{0DQ+=M=Q5VI{H3w#0ys$&XZddGxJP><v|L#ax?`PL6W?mG38joj2JE8(3rd||xU_@O&#P%>zr|sV>fw|BT7q!{%+Dh0K;iBx9'
        b'_gY2Qo)6t&7yH64QqtJ4i{5=^?Ztq)i=MA{eoZ%+-QNuMd%6QQrP+m-OM~)`cG16CA45_of>u|rcWwD<Fj}oWxbH>3dnCQ#eP0ZM'
        b'_0!*%E0>fr$6YaqrrO^JX}&LLjQj4<^PHgqW#j!Wy#W3Dlzu0X=|le|5u>MDze8OArMw^e`@z1qSZ>02sHE7h3aEPjFR{O1As*lF'
        b'`Q5go0j+v<Fzz_s<mo#xD1uVO<NEt_?u0?v_Kkf3Gfz^Bsn;_9p+S1bD7JbK4AI1?6Jrk#ZrUFE++feiQ6aoLc^mKlEx#P>`_-U6'
        b'PQ|)9F0yYNHiloq3m3B8g0GB6c^N4o?7VB&VAmlCY0*~oo$GGG?y+g%wMHwfuUm~7tks%4gG(o?Ph=n;FVhNTN0*3k$Is!Bp;pKc'
        b'w89M0wXVt&(&L#fE?)PB=Z=0)lelu7*s?A+UUYB8qL2O|N_<Z|?orb{$0qj!82DbOki-2O&_ALTt`Sm%l{_qhhgAq|!b;qiY;uPT'
        b'((|j1GjBm&p*-E)gVZ1r<^uJ@cyXu6Jv0D8raK2?O@p+`vqJ{x&BU%wGh6nw)GHL4`8~zhTL!b#R7ODiW^^x!q>Y0{-ZmcES0>hM'
        b'6Pn)e*sx)(+k}ji5cf)2>XH*DW!_jmD3pH*+QbA<s%g#I+<(GqxN8Q584v-rD~C#B_?sB6+vxtq0NsLiS5ZD)Ja}*qp-etL&5yOW'
        b'1JC~$CiP}^4offPg>A_l+{|_y!wk8DZW9cCk0EC;Sz}m0hgXBw&!!A=4$#PVn6el@b&FqjZ~pg#Tf@fpcKzwTEY-{lx}MNcHrIBJ'
        b'NVBs=@uB0J512g9cW-|FIG9(@ZjI<^AWux*F)KMun2MIt%CP$;P3`e`?wfSoRu9-s4{rTfNEW8{_nkZOHQ25;P=$o7&>@zmVG5R8'
        b'qRCw}C2>mJrh>%ya<)ii;+Y#XZ$_Ga<MC4U6O*!VM{rPbYX@mFv9{3sDcwEVPv3^QeQMpxFd-itp<l!D6V>CnkT~n*qE98ESD3sv'
        b'?8N6%xd!Saq(KmYs?=^9DGw7GR>CwpxBl-;H(RO6m=tC7crv!CPn5$1zW|Q)<wVdL{xJXpsDS~5k(z<SWW(Vxd^8|j1HnSM(8`Ck'
        b'fe+vO0d|Y_UlJq|e`L@b4{rJMfIdC8JME~jhG=rT^#|O48PKOib*Dx48fG7A?EB-ufj<t&H{4(uaKD1StO(lLu2(&2k-7QwygbbG'
        b'@<0z|2T)Yi@`X$4bsrl5f6rq?zL{w_F_0Awq5J|`-_rwKzmv<zEfL*MV;QAbMoC!z9^xs8q$N;)-!BKik497hFZZc|z3S3%_g*@M'
        b'b`Q9Bv#EpEpp2|MSo?)3MNc8)8+Q3RjrUFr?X^dJy~a8-8iR%Sq62)sn0_?S6GxSdc%sjqa%%8U+%BW_cT&@2_0G+7foPhVlsGxY'
        b'G<Be7_lqnY>jq;ZNqAE_G%4X}X_xW*hZ67tX-YcP?+J5vV<EA3VV%_ebsG2v!|%j8sr~BouW#5uzJ!>z61u$GCn0*Zu}uT8UdQIb'
        b'o30Al*oFa9+d!!raRVJmb#8B@DSIH7UkVL<o$<Wb{WXb;5|c#t$^rki(p^2^bDIZ}yzb=#eai>veBT_W!i8e#fN%LgnO-vhp@A#0'
        b'dBC?4V;;JJuDfaa+_)&rqBJOrqRX-nHUzBY?#phP9axwe|3;qv;nlh3LpT3?>58Z3EPi_GGx^qy>90L<yXgk?MM(h#6i`3`1r$&~'
        b'0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~0R<FLKmi35P(T3%6i`3`1r$&~'
        b'0R<HJ{|39wDmDF!sJVo+-{rjQ17Z+Q$QeTaET!FLp?_dKC|*S_u)h!9(Xy8P<@11e_IJYxsUuC62AAEjHkcktw$L=qj{4Ry%I_hh'
        b'9$f!JoIq`9wg$xG-$L|<{cGR2`_kgg@4Wfq^`{?eU-6zY!U`y$fC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUg'
        b'fC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Mim}0tzUg'
        b'fC36Apnw7jD4>7>3Mim}0tzUgfC36Apnw7jD4>7>3Va**N2ogYqcs`1pA$mD;USWQZ<R<wa*jr;h_UAMlf)0wvN8<w8q&y>pxII1'
        b'O0EJ%L-ssFcA8Q4S2nmrqaOYn=TrZ@)Oo4KtI+R$>eWxIlU`ZA>A}uxH^=_y;ge5P4h{W!;O)ZsNl*Uvp?}{`{x5?To)CCK;TZ?d'
        b'1bF7aQ);XxZO#H~t7R>j+iG*UTCGh^Qdn(HGp1Ch5#xM=UY|x<T&@mh_T0J6Hdjk$eQJZfZ7z0DiK%QZO-k}B@>dlVRo95sX<~(8'
        b'epRNJZ*e$mR)<(+^!0_{tIs_3*!A3;Nb+_q%gEi7K=KNPHF=RKBoD)N5ayrm)}o@Sn(V@=s@o<+a8Ko8bSI?FpXcmyxVjQj4SFZM'
        b'jZP9@RD@4yMNuWDEn1o_*B9EDqE9uX>a#IHNnu%8C2?9EcUc`>2|(<`<Q0__`Gqvzw4|nF0cmKpS=(K{cnsx*Lz?{Zf(3-eVRU>v'
        b'iNBG=7nAr|B)*iySCIH+Bp%8!lX!D!MKy`9F0833ttbYUsmxSW4j39$Sp_)1vb@|>QBY0xObf|*P#u!<5Im2-<ALW<czyxT6Y%VT'
        b'=O8?X;5iP@tMI%5kKSNRo0mR6BQwiV-_U4n3TEo5M4MNTPx3y^XMMaKaC`yDYX$uA%8cCj+cI)9!CwPd3-}b^kMl@gB*ahsuZ-Ny'
        b'MI^7JfYAoS8}LMN_l@w#!+q8-To*`ECp)_7TUDp>_n%YOsr~$?Zhd9pg+(Oqu@a~=)MX{$m!LjH7MG<pTP$q{9__HWZ1t^HvC(0J'
        b'0Tq)7=h<wr!@e2<?Cqk{+S-)jvN~O2lDV=vS!}Y{TCI(-FqBJ7RW%0sHqv(*eb2-4Z_$S2EQRMbcpBij`LU3kfzXhg@NpqIGvP77'
        b'QwYy;c-r8Z_jX9m2aks2EF?u%Yopj=Z*3&`Ya5_uPM5{uf)2Mg+#xnvTdgiDsdm{r#73Lb0yQUvZB|FKwY_02q_lSsv%_9*#mEMG'
        b'd%Ly4Mau0iy8|lS*($qNTO94S_GVIMYqPnWq8%FUur)%q5C{d<V^KUGjB`0GcUfCm09hus`Q^7fz_%j67m!jk2Bro7iXcBL(2M<x'
        b'uCd!&omQ92>hN>=Cnz@;LvD>$94l<|GO-ogCbrqy{oRne*JoJ+?iPESl_Oe1AJy^zs^xxE%Nf;jnQDa})rtVB6@FAJ7}W}ys=CA0'
        b'-UyuyZ|fSbucH$hM@*e-AY9bT4ukA4%8oSIF;8}+%Z~Z7BSUs%%8o2=hQ6%5c^kZ$8@#z2yxAMP`5U|i7`!DIyhRwiWf;9>7=88k'
        b'mSJRNSlTVE_GVvWeSSlb-x%Z%rk@w&PY?3X5AtWgusdDW4zkS1@N$m0cLhh>y9{QO1Jfc}&fd(kg1woi8q#(EYf{-E`<$Y+ozB!{'
        b'vSWoeWV!4zv2si_8<Q{8$6F>pZZa`$G6hUHHo5bwy^dvG*K)6Gh1XS{=5x;TIn#a4`95ccmqqREUMEx)CY#MK#JsfJ>o)o)HI9+k'
        b'NRyY_oGwz-YPUDi5wdr>I4_{f;B^_jt~9S}p4XM`b<Ov>GQ6%#uPe)!vtJ>;QVhOg48C#<zJd(Ck_^7048F1qzQPQ?(u}^+jDBtM'
        b'l@>T3e4XGIU<eK{1_xZ0$GqTx^x%N`!2ubhtgt|=qVHn*&ZF<8^lfQ$Se<Oy3G_nk^6enG8^kIrh-cZ8XScibq`b7cl9X3gmy&98'
        b'shD53nBi(Y#|Dm#9H#+4Sez}$%GCv8gT>M4?`(t>5JWsCb<ncVRa$imsHyp4b^c<83ru9Ob!~^G5#|+LxG<DEtCo?PWu&TlUS_&j'
        b'wQO$9GC$_LrLa^q(RUtw^92Q+OjOs}9Ij4FD_!ZuWehE6Xaz&%X&levIGyA99A|JH#X3GD2lba<fPR2_%YMKbz~8G1$w6KG1@NOj'
        b'{t95!$^Qr#_44z8!vKE+80{E!NJvfu;7GvZ0gHf9cTWL)4d9yrPXt^5I1+FbVAQYb08a(n4tN^i?*pC=_=kXJ0RA7qF<3vqGXXyb'
        b'7}fKa0ACOI9l$pL{sgdy^#L4<b_D1-aabR~vjATQI3DW-I01D!z=?pf0nY|p1ULzBIpAc#wSdv?s0WOCVFzH;1G@mH0A2?e75z<s'
        b'O@JQ)j0)y1!1;g=04@N07;qur-vBN`eGqUl;6DH^0sI%hrGWnqcoE<WfENS42)GRU74))lG)Vwg0FDM+iR}PvM%xJREoi3zuEKr>'
        b'Tn)Gca1Hh|;3a@p0<Hzz1b8X72k<h$cccCX_+G#(u-^gSiv13FCE#BIz76oN0sj}^*8s1=dILs9_;bJ(z@vcc0bdgax+dUj0XG7k'
        b'3D^oa9&i)(JK$!tYXP?dz6r1$unBMn)*JAhfGYqy051XTL^}%bIvfwc_hS74{{VGt!0Q2T1AHIg4S;_Lcq`x*zz+j<0e%#4FW@Ht'
        b'rvg3*crLaJupaQMfG45e5BP4t?*smCz#jwd0{kW5?*SeL{C%`f!$WfJK^p-u>iIE%-GFBU?m@d7@MgdZ0B^x|0p1FD1>kKs4uF3Q'
        b'*a`S2fbRqRQ@}p~{2=lZ;O&4tfOnuB4)`I!PXqoL)*JA{fKLK`1nn5W{{#44z&{84H^3g`C%}DxF9Ghyc@Y6N8Q_V49|Jrc@J_%9'
        b'fPVp45BPB$7r?u4UI2aqZ3)1;k&gi521PUAJ%Am6_oBQ2{7b;SfcN2e0N#&$1o!~peSi-FJ_`6L>}SAF1O5>3uK<4q_!+Dp$fIYG'
        b'e*hl>9H$D+c@A(Q_zxrh0Dd0(7w`*!GXWn#z6bnkoWFoy1pHrsj{?2}@G-z^03XMC0{#u)9>6aF-U#@&$S;6TV7~)?8E`+~li2To'
        b'Ujh6S;8(HV0sjv0X~3rdzXkX-@(bYCa2^AG9q<=`&j20)jJ9N$0JbjR@qpjN^s7U1evk77{C~jt0r-zNp8>yx;{f<=90$OE0$d3A'
        b'9c&-qKLf4-{4UN5!0+L_0Q?ugw*!73#|7{?oZo;y!1e;Ju)9F1vv)SPh%Hu2hu8#qRYh&JSl`*yWOc-nYOra*{Bnw`9X6L$wlTrN'
        b'#f3txCX>`^RlHiQp08GGO4MrY3bi_<Rjm&FzFIwQvsxY2uU3aYtyV{zP^-r$YBZ!>qftGp(b9Eh)m@g>PAf;N99CDSquts_%Bzb('
        b'sxHgSiJSsfei#u53h^YJeqL@tNtwBZplsCB95iT~k0aQr<Q_7PuJNMFE`p5-wT8TB$Cu3RnjODvHimY#QwuWR(uqrIwz!1)p~OO}'
        b')i#m>X1aof+hPT)w!m(8a3?cKiMhE=ENpKiP!K4f&@Zs+Qzh5w7vyAmB&lw-T07954YY*C6cNm4i$f>6TCD9%R|u$ciM<W8X`oiN'
        b'!+K{YC;^RNeu7HF1F7kaG!Cnyvt7L1UJu2?a6uVX2)4J1t=9HtSBq$GYQo&1YS1p5vjuzC&$#_hH5s!^IW`r_Yy(>tw6wJl-r3M1'
        b'cC=bt=x-D|u1?8pX~s-Yx?`<qX|~wfA;Rha4r~)GkOL-JZG%?C*O-@zO*V(q70W3h(!~@b(E{i$D7G<m?CN&doi>^fIh$591$rgb'
        b'fAgkvI@5Qkdot5`=sw+KruQJ&Co|m#!9AJjKL{HpGaU$F>tv<}Av`jf=|XhBbTZS25DrdeIuXKeCo{bW;jPI`hoRd=lbN1`FmVdg'
        b'l@Jo9FntN3U<%Wj5Zb0Ny$NB*6t-p|90K=b?*0<oQ}|xi_-jLQu9f$(z#Yxqy_F$3*Kv2rwb;f+;(49qb->g6x^J&c#oua<HGccF'
        b'gzwd=RBXQ%@i-rmjJ^|0q;x70$?0#1x#4>FM_*;vfeeGk3{TZ{sJ|>HD~M^VY!;qARkk4Ftw(RNPts&x_v|g1dw%=){398m=|6d~'
        b'Hf{B(Ck?AQ!u8VMZcR0}TH4#eT4pj(blUC)MzlC#f;4tEp!ADhw1ALY)r5#*wkanXQVmVwt+V52i@;>F=^p89%5W{#)(*PM3xX><'
        b'K3<HUCB_$v@ugyXg&4nP0Z2Y@ty$1&YqyG!E5p@gW-&frj9(_kmx%Fs;`hZ^aiQ4Ya<rzb!OT*~tzcVJ6qFTa6PUw<ZoX!dxcHQO'
        b'd!sc@7bkM5jm{<QAh`U(!~(0c!C~vbIT453zLY4O$A;77;RP0##kID>N*&mcHj68Kj10odZSYvuKt2;9QUFA9E7UBTzN>3YHHFy)'
        b'l}l>6{QRb1e`!S*>FVkt3o7QCu%~Ei@+%9VaktX#WahTt0g+aR!|uq2vL-}SS?j@w^UB9mq62q85Lwy2vb~}b$`DOr3z}$5!r7Zp'
        b'-cf1fu(!6t2-}=qBGJ->dw2~kmiA_Btg8hgovh`lP;fjEffFoiY|b`|^A75PLP3hQGq=svWV5z5W(WAh)h!^L<!mrm)bp(rC#?%q'
        b'%*9Ab&0xJ!^OfLs5Vi_xV$DVuEDH=<)&Ry%07hV2@G$y15>9OGE^D*ZL7H0a78k*aku`E9h{Muov)6aJT=sS+v31-vk91g^&ee8D'
        b'qc@x4s>&s19KFh_nrxC+1H*!*At0TZWM+_x!pib$Vn|IVdU%S!sG0d|(CI*aPJaP(H^6=aj{|!vEausyw7tm=HD1d0cfnOi$5A8&'
        b'*7{EL-)gSPgJMf6%W>3e$||uArYaL~HL?Y{wK&}XLB%A?i1FE^Yrame(|2LoDoRn63;kD|0Z%48Mm@d^@XDeu^k!jX)_jsmL$dId'
        b'30dYNU6v7E^XJ2B9wwcKvGda4g~h@f0?Y9M(sD>zo`#<J_=3{PA$2)Tl8*7|Y50P?YKT}w#A<S*j-=>_sV0Acfg!z)6qT8(OGpv4'
        b'kQ5f0t18RMt+j<!*(gU+$*q-UXyUD=W!3PmC|ru(!ipv3)w-%0f_<bT6_r4g2M&s=7Z7v4j#L%tNM*H-<Q3>hA>eW|C{ksnni5QB'
        b'E`<bzd6ktlI#Lah)rF9%ss_mNO%*zFYf))c`BGC=VKzT#pi-;4w79}lMymljVRcPqm8lp<sHm#2P%JMjudG@QzJjV!tUSpj<t2B^'
        b'UJ;(^(#i^Nya>$zKW3I!X{ss!Ty9zhnHHMGDr6WUmfTHCH7!{tmLdyqt}H05&WG&dOsy7B4NzR+)VK>e>qZo8EVvwZe46DLeTpw8'
        b'NZ`d$=DRE#7CJ^QEFvhA5|HblO?22AoY~-o+}hee?{T7AR+*_#<U$RGyQZ+Vu%ZT=UshUPijM3Ol3m8Q9)r0|FRVa;hg=P#lT9k@'
        b'vO<YMs@diQ@dV-yGcB)#0f8~ApaOt-i%d((aDJ4V?M^^T88TJT7X}w+8yM1)t^#xyfGdZTqQ+X)*-o;Jpn#$PTV!uWRn$soFJ?2u'
        b')M0{}aW+$M>B$G_%4>oW%G%*oPy?0eDyqg8JZ21AnqNuZ7+851)&-vG26&aggY`8d#<|>8+Rk1nP`9F`GCPv4_<X4C&CqU8_p3^('
        b'3(9H=D~rm-TSU<e_CZ;=Dz6Tnj%!tUT{o!m_FSXNdwVjt3GQFdZEGWKZF6zE8j#c4@LxvKXl?d$VH8aX9x{gmu{Ev{bHs{OAknI7'
        b'mY7$Sl~xpzxox1T(lg|_T%tQu8z8BevjCFjL)SFg+Cd|&UJDtvImu<`wM2(9O{N9I$I`f}0m)W1!gA}2peEOtF_eU=xSbuVP-zGz'
        b'3W&q~es+W-+XcYhZMFu79olaPu1#Ip4hy-ht+Ng6nGP$2;Q1mhOrU5tz?6UqfLc8)g`gGK8Z51?YcUVHbm8)ZYpMZM5o2n4Dz3UU'
        b'E#9J9U{M1#yxuCSPhyk9-bP8e?IcqB53@+eg|Z#jw^VxU0GWe5VO`UJM~{{csLUE0Xd+f9-7rrt-cfRQDjKM;9*fQvJLvm(Jc);q'
        b'mbEM=w6{9wGH!?ZxWvY_?G|V_ThZ}I(F(eal^<DB+l?QMq>8n)QpWUj@ebf}Cp*!Qk4!+_C~e1MKDK<*x;kym?Uq)jm_#iSXuo}R'
        b'a$qv=Ztk~8%PS(E|FU9bx>T{;?sV}ur`YKP+2G4bPRvvqY?Tc&c0$3aK9#7nX^e89V?a^jN{Q3bW(_PDxB|L<8S(*?8Po}=6Y--U'
        b'TYE>R%UjuiRLrdNPmtt<rZWp%*2$cB0)yNBn96b&n2DBpTdU2r7V5tg$F;7?T<%NE<zrx7>#&v$D6NopfO*T)P&qH3hvB@ls`a81'
        b'EKEq{6m6&&Hqn&T;>}`EOuJn2>?%te<tSFzZ2wZQ9%5$)&4aod?W<vu*q|FRm8G?z6AffO1LD)N=Fz0_>1kQ00d`nvty<UqC$6EE'
        b'EDjKzz5J{V2ZY8n<Aj7JudzD)hPwv!ST7%dUESJ>a}p+1s|`{^WkKy^hBC|*%-xrmR##SD<I`ZyK~-&_RDzhGD<W_P$|oRcXzgrd'
        b'*?|Odb>foMVaJwG@zKP+BGsweU2KxJ(ESdmE3hQ2K%%p=o)g==^G&1&jBByV-iA7DZ5^#LNBMRH{2FbxIGkv}xloMAO{N7qtsNEz'
        b'lO#;xXLG@?%CyFm-=PPnIRO31q)iLVu_g;lK)yDK?6e<;%RzV2U|3*mIw_CA=s=}l%9hc48%)+YVVY9LLJr}%VhxIowAkV_(c);p'
        b'Y#Xr4Ee#Ew;Dpv&u<cMEROO-5sX3G?=2=(6q(v(SMr^GJmI<_!6@-0e1uM3}C3di_6-#@ARi1Ci5e+S3C)#{$EZ8O-Ewp{DZ|?*v'
        b'MP)I|)zxC5W7rPXmPO_aCyNYZUOq?17I^Y7`QIVYiIp--q43s;h4fMhR)B5&@arSU;UKxa{KpH>1&9l*BNw1-U4x+yuAd!@eKy!_'
        b'pj&+#$?QFF)&Y4ZSX_<<Y`|)plkI(>>>4{8zP~tT&%pZJ3bF&_fDJbifnm(R(d{l9U2J7z5mQmABB#Si#hct}{Wd*HtH?X`f3pMq'
        b'o52MB|6wDXfvpHAfK6|{{siTZOUJh>0a6B)A<qD(y~)K|!3DXKZaSidWNB!@{TMd8nN+9B2DK{abYZFqtb}3}+dpv1(u~m6!YjSn'
        b'+N>~Rsk~{iw7Q&JEYM6*YOF>H>7TPj?peADQO(O?Yi_2xzgUXm)nS84O)nQwDaFdggfMHJ^zInX$d?6ZWMJGh`WoNjx7F;|2LGb1'
        b'R2Rh6gsX9uPL~~&Fs=pSeUC;ea@oRMD6hfv$`;iL8n|ubzar}bQpnYSE<jPv1Qm2!{aP`;B!?*$^lsJ7-pu@pG_|7A1EHOPtG<ra'
        b'8if?CWl+uea>Ak*HH6Y4QBk;R!F84VZkmV_jkOGyBnwuBN>9dD-Ys>0DNd~8oBQ^5k*nz5ou|4~dFS701?i6+PqXxnAJ@pKOuoxc'
        b'FGxj;lXWESEJ0~31EgrTHd}&Hvx|IGnqyL^Fr7Ha8G$^9)du<DXv0Z>(*xRS;d}15Ai1cjQf;-~;mr+N(r^c4*JPu79h4#0wy6+p'
        b'rK=&!5t`fqW`Z?HnP+-@z16ka3d2lOIMGV*XIfdY_x4hwwH{=013jI<_0xr2@4`h-Ug+60qW$b^C&+Hr12$Kx$cKR{40uL?lEXWR'
        b'+Go4isR_=b;*2z0G6Ty=!eIl^(IM7@opuL3C2~Ms;D9y2&lsZ(^f5BB3M!r`6I$^k1D4r#(MbD?t-H8S39Um7s}r{$ATq#=Bjvya'
        b'XvN8E6zG&V5BS957b-!BBb&=<I$ArMZS6?RO~C&h;>#KlpO!8r;Yx^C4r%R^>5OXuS;_?opBl}G*n-$(YwpB7SkUfMNtp$8HxzK$'
        b'0SZ;IVXkp*ns+|3VWN{91S>cD{9C{z0#%Bknq?L&i{(mZD>Y@1t%@^rVsWMp_XwF1mX(p}e}N3tV3?_Rj29S;Rs$cNc9dNWs9z>E'
        b'cEajOSu{B?xwk*QWpc}!|D0Ub##gu4fJbE;mUfDt?D1K|$hy^Dqp1Np!@*e6iA4ZM-(_#@WWqvTDdO5ucWjN5cLb;qYZ4dg#8}!}'
        b'-^V`2d4L7ek~;7J4wA&D$fg5M3m7%jA<+Ef^=f3NkMLScH4?BxFibW=sG;cMW-K(#0(GaSvEuFaW*-+odU?HGZFk(^?6AO0q$e;;'
        b'^rJQ8Z46ZH4zCE&$r9KXE-y;hPX*Q{nknsC8bP&RzDRMSmea9CJ(W~+w$<ZBV6Uvgjdm-V?R<(E=q5gM8Z%Rgi7&785-tohJ?xZ)'
        b'VsIok`>qfRs*B@_kxlkahpWXaZBZ0KFE+DNYb!I{+E7%rS?NF`H$VeAU6>kI*>9b?2<@Y9oq7=rrB{A3+m31nPQMxkrQ(Z;cTK09'
        b'o$7yMxitkZ4${-;)=u1{^3q~W+EPo~8yr^TMl@e})a4n><;1vRiA~<6lV*XthN;Bt&o!{9gFvGyT3eeAPjqCqZ18Rjinpe~=&xdW'
        b'rB2k}=F5YcmGWxJ^5W~3w?Td-vpWY~+04c|U{?)RQx{IzW{0H>raErfG`AxOouW2qXg0Rp0crwXVYJh(r>Zs-Q(90~$c<;nmr6_T'
        b'kXl_0siH|%r&)G>Cu+FsM{}bSI5lFi6$Vl^wpf;+N7%unfb#83Qi0(~g{hnjR$ZS2g8s)WP;diVQ%wdt`wl3!v6D)NCi(XX+;T_d'
        b's}tCs?p}B!k?T<~*<@{-YS65UEl_kTKP7}hTD>DK_pe+O+9b?IZk!8kWJ-=4_}xU3%x=!L?G2*2w15hHdW;8L0BM<tPimMA0#)OZ'
        b'nQgJ)#w43Z^1S+wNgE+&tJS9}AhV^4OK@WW#;jNm0Ub8R<k-;-U_&}AOwC*(@4Rs1r325&`R*!?Am6BE`%&<~YRQxtP*7M6e8sZK'
        b'!m8?<`8ZTuWHN;-RV<KIP`bZhYxMT1uRl@MPT?jTme=C1MtgII!YkQz7+Ixs%2Nh^Z)0tDB3JV9@zsEClJFfEoBxQx#A0&IWyda}'
        b'8m3cTqEVG>wBBW7`Z8@7pM`C7qmXJ=TmjPiEz)ck3_Ft>p?;Y&^%aI0r2uV*PY<K2q*F|aPs=ju*w!N2FzIPo$(+v(bmP-uu{o(8'
        b'#P$hnO?)FBHEnj#&1(dqa#8XXCycQ}$IC*yf@%a_HA<EYltHLD#cu`SbsK7;v|CsEwv=Rxi>i+0LFuy@7t$i>eI};Bd8u_&X_HID'
        b'meMOi@(mwa<XHKNxngm8R%+UR&fo7E0F{1}EbubX<&9kOttw^mE?NI?>Seh+e_Cz<-NBKqPkGahjx-jP<Q3nrVA??hC409_@tPM{'
        b'<CcayWW5Yo0SqY{-IVd}5;6|;^+()TZHS{g5y0IvEyR1ZEgf$Sw4pdn@5{Gwtcv?Yi7a>n6bN4@$OGZ4*VQaw{~Ci$=%l0PX9s(`'
        b'i(jq#_NMR{Isa#a*i2V_U=W8aoY-{{W^&T&cmFvPSxpEUsPg&Q+$P`_m@G_ePCnvJJ5zQ8uFG)l5R+(wT(*v6x;rHw7~!=SUyaJ='
        b'%j==e#^hR1L3HnmmBv|%{}fHGEM?t%nctCJT*w`MRri}RxP|V|IUs<8c+78?%WqH1w~IyfR(_-aeNSZ(%9`S|%+z_Xh^^%(4zi>}'
        b'g)M;TNdXE4zI8-TK-m_8&w2y1fJWm=&sM-I5w*#OvR>`<3hDSv@Jq**6OibT|6GTxCpO_#7nybGs@<LfwjOW`RkrO8oB~M|wbi&;'
        b'ZKax^OYSMW0A~l?X|0axCyox_Lbkj)alGtwLOVcRxQlM6ukqcRa{8IzIAN$B+>A4Z{&w4^T*`dmvir``D62XxO;)gYnMMhDp+?b&'
        b'GdoDlLqqJcTxETd-j`+fLjN!1dU;(_Vci5`eQG+MgzKGjDfezgbat?VusB(7h!dMS+Z)*KJKbt`$@7Sw7(%|QEjE|e&bfRM_vw!G'
        b'w?OP<i0>-;+o1G!vrg~+VZh}^JlcS+z<Y>Hu%H8r=Z9eahh}3dEV5E%!-Kp|u<K}-Evd<eteYqWyLK%mp}NB5c>J>DF)rOv#oNWU'
        b'Px%&`SeQbOD$wF(;((N4W`4$$lU=i5H;A27BHJ37Rp&jn`wwGBPvQRmk6zHW4KIscm}v2B%vfA5(0Gx;H>72S1=UQgci1{a!<D0q'
        b'zAM$#w4^Hr_5(Ms?G9#`7aKGEB`zp3*(=-e_8dgeeQ>@FuBV~!CaA?gcAYS><X^z~v)^Sm1Nat1z{P+oPgI&u@Q|dEeEG=V5?}$^'
        b'+XFV-<&4?6HNW7%F9$&0Y;%QfEwC#FsUqH2;pbew3oe#MSXI7nY~xFd4a%=8vaO*eAuh*tGJknPFd;iO=WIZY%O<w(1xp6KiO}2$'
        b'%)sm-2(dWmnBWfT>?$kvnFw~A1N0VPd42#t8+YVrZ+Z*zMY2}fz<_bss5UCoQ!R*>#)|k3a~<<3Hy6)E#mjQVsqdEpw8Ku>YV_OU'
        b'#{7x@9yN=!d2JR#O;<T`etLRZx<5VbO&1ICU4-DFjK_jUn2l+YGg*%JyOZLS!~CwHIDuPWEo;D=8Kl^EdE)Z&=)tah`b*DEoqTsf'
        b'_n+^h=;TAqR`0$x%$g2<(5mCR91eE71UD)Ct|G{VnPt7k?{v~933Yk=zB+EN=*lp%or(pgjw-x~-0n2<+Zk5fQoAESlrqIYCm(J('
        b'b@GwBoWkiX1Gg)nB1`it`7F@+U$)S(o0s039J+ve9dcv+Zhv6!P}L>HWlw3g>k8Mn@U*#+EaFnuXHAn?2>MjLUQbMTOG37gLC<BE'
        b'OWNtR2CH|l<)ijM7LcV4;}>tRSL8DxMK$nF?^i8?^9qU$V6~vQ0G6xvJ9Xy2sV_kh8W_ZxtJ-(g>*XSx-Ao;$%o^~cA=z^o1M_fd'
        b'A6R{xncf}^Jb(nm?HO-);29gA!GVz-vc)1Rqx6t0_%IGTM?L`?`_ziSlp6a;ij>ns?<U+nWLr~wD?;ZxGSd0ZdB#4&;cXuKB!_TS'
        b'ee8pqvCn6GUsV7JiB|^Y!~ejKXat|Ih)HI1RkFOv*=lXZdp=b)-d)5o&N{rC#cZ%SlN4CxUqXQ@N{8I$k|&ycKH=TR<XjxEbxoG('
        b'mg`o?qsdMzh{2f24iWe?^*@;ijPO5|2#oPNkqFAm?=-?&74JT`k5z(WC`-zrY?GX%a1Kr}=n*d8P``Y$oK*Yi|FVdscbet-SLEAL'
        b'X8HyR6ykh47*puv>}6KP1^%)PZ)R2Ka5D^73|y=^hbQ6YX@`r>YnFNWykt^jchKVs-~g&Z(x1Q4k(8?&uzj3@DsW&}=@?-JV}!|D'
        b'&!ud~nWXq{(E9e0{e<tVSv*mj-%c_QviR*A2c_a)#$kbtUUQZ$JtT$6br?mSqU8!AD<JkVd3EJIT6$ew-iD##fy<8ItwP<E_6~Jd'
        b'*}v2A)0Oi10p$emPz6L@*0h>{jiR8I1!rsZ3Ea!#WhS}e{*UhReHC5M1_-up>|KW|?^#@Vm%=-La2o=JCH|a&F5P}hneU4(e0|85'
        b'S86$+fFE(mzqAed!5%YsiGgYeo!E4)7clLYu;2X#Tc6C*B=n?;c1Sz7sqUfz8-H4MCEJtW;2U)KHqv(*NM&Zd$yLP9l5lH{cZy$-'
        b'Q4XS=&zJRPJKf&}0qpG%TvcfY6w&<}ZurW>%oP})q2&zxt`-lJg&R-aHb#<w9|>QD%0B^NKfaa)Wj@;P{G?01&D-STK>RsntKI3+'
        b'v2<+qJH1j6*dv)o@!dUHYV**5V>$2Vjkv<i`Y0Vnzq+&D0V@Wo!d@L3gc)9GX`+XdFz~pAU7nSR>M2j_l-W_H@wfVPSF+OR$G$9M'
        b'up5SZts|0_IZv<G84T%0K*lsZ`sU5oX97ykm=7$g%Q6}OLmhzOimkxckVk&tZBgG0lP8DFBmq+0UmEa*U0y-t1#+(6B8Ug<&CL3s'
        b'{psyjW*Sp-&&<p{SjbUhpi-DDXJ`dOCWhn><B9CI)eB<T@2Y<l%YIY+ZY=vfbyytxE%o6z_B-lxaqPF!npy1k)05)a@1+mKv)@WT'
        b'nZSN0tx9CSk#;7s-$%cm$bK7bpUr+3-9MZCCi)+<+3%tEC$Zl`M<ui0L3bvz-$4H%nf?CRF^B#3Ib6rSJ!99gZ_gajv2V{rq_A(#'
        b')TXd+&m2x+-=6s_g?)2oQ7Zf9%zdfsn={dK**9l?HkW;K=HOiR&6yA8vTx2r>e)AE7V6nIXFB!ln==pV**9kl2KLPvn}L0E<`Dz?'
        b'=FC|G`{s<=$i6vqgOPo^WPy==yJQ7m{9ff6!1#sGUjW7r|NS0tI?|<u<lt96lK^LMoC&xLa2DVP0A~Y!5%5ho4)a2CasX!mUVy(f'
        b'2YfT&>(lX@fKbnL_RX92boR}gpQf{K#^7)2Z{>I;$M}ty;dJ&5m|64LH()B}vv0n10$zjP+L+J2mGbF)_H7Yc2Ky!mj>oV0c+>zx'
        b'{Sv~L0Dd+zB&QZ|#!VqPO99^rcp2c6fR_WFkpuMsTnG48z^^TU`T*A49FlVz;2QyV1Fi<V2JlY-_X55IcmrVb!jPPefPVq_e!!Wz'
        b'Avr$;yaezEfWHU$L%_cV{1M={0sjqfstNc77``6xIKbZko(ecA5BLgjKH%wq{|oR&z`p|gbHKj`+z0p~;Ku;Z$q&id1-J_E5x~0v'
        b'zX;e?5R!8S@N<B1o*{3Y0r$BAHjjQ#5|Z=6?XN79e~*7=u_|xPt*U_E@FUG<kbb0q&8@piSzZx^Y;LaH$mnHIbDGFPmQEY=1A8oI'
        b'nMsv5X!ez(;WTmIfkw+|GQR^&2rp~dcc2O7pLK2JG}tG%>wIlSnup6&d68ABJY6}X8^`IoISm=3oOkmAX~KAW?)NKaFxgiQt#=Sj'
        b'I4@@xr@_8|!LLlDIkhy9CW7ZZxyV;ea#0WsFGmg=&(p;ehvYQez<6hFv5yA(F>^y89|)W#`zka!K{OLMO-b>U`%POOShs6<yO$UH'
        b'+S5MAmoJXRu4RFJFp=kF_oKPlj|TJmB&cqYysy{$(Ui^!9G^9Q<*4{~U@@;pu246mX$|6?Nj&`d;<0&DGX{@N=KcLv@s)WrKB$~2'
        b'Jg={=(%0tvz`nkg(}b4z_-$H=j~@GaFo-6a^G|^v&AJ-{$0vSqAkB50=9ZFgKToG}8XM3waej0A)eUK0SQIGVrg55$-+^X2r|B>8'
        b'$;36Kfqeb@AelIW)4W(R_FSOtSsqwU3?Ik$uRw$Sm>a~SGr0`;x+GA>)9=5GW4hI{pt@bp`I<l*qD#k~r-akUymJGmnSK=-Z4iyf'
        b'+oR`wg?yA(8rTP?N(1>ImY1^%()})mmD5=o*au-j<-~ECE=aeP*X>^32RoudX&(qdG_yF(Lsy}R45EqWH2beYGbM;7ftPin^xMzv'
        b'L|)GOoCf)5bx<FCxxrTs_VH}q*P2CR&uuK{-h#lsPU5n3=2d8Ff@qSt%+@dR&Fz~P1+67PG;=u3-HUvDaNnZ9_H+jE=#9MH5Abvm'
        b'e9qx_MSix3@%5jAXmp(B=Zn65U#D=IL*IcWmD9ZO9cboqnty%^8ku)8dB24$_Q`{FC4v2RZ%`j(ahe+z`{Y|NO?MDYHm6DVE2jY5'
        b'Ws7}dye5d|CQegxm2$d*XmU7@HZ8s~zg-C8odvv{HH&@g+=QTYyEkag-OST%x=J}^g@J41LQb>8ubd|r2l91mVPM^IdAjLkS1w0i'
        b'6i8#@>-LRhzH(;X7^olA6b0681z$67;xyRThM;xf$Gi_Bn;6ZloTl<BG~0t{R&tt#tI#|gM6-(1tiB4(V?i{He6Ic&XdVWA7ispC'
        b'1+EL5{nke8uXaxJ9HiUFX@b|&V45|Y<`mHE{FXF5oaTL?dG=e<?B+CIm-*(;`0|jPN#*SO`5HeO98;uun$tv=``Y6#<5gqO{F>9u'
        b'`wlcU{CjIv<(IEnGQS-v_R(M%+Rtcbw3Ykh_4msIY3^MV$fLEK<`3n*K5z$>^KnsNIZHXsm*r#YV#qr+8v^I{GEOtG;>tA3f@qd='
        b'8r@ZBRtC|m;520wzIj?#5!fDWabO?dJ_5@1zKX!Ue)Cr$IkJ9mGDudf<TTG#Tv_Kk6GU?xr#X8Sno~hExR-%#_-DnHWt9*lt8m`~'
        b'br(&guMhqeY@Y`80q&8Yyq*X&wQ8R}ir)Zxb_QFwH*E}*-y1lMI0lWZ!)^|u*~t0&O63IeHPYPAX$+M<zFu~FknCL)XwUtS_nWEG'
        b'r;Fi!$U!J$X(g-MB0rrR(|*8dRzm!{H!ynv=PB|4(qK7Ve)cx{KjJhUl~*1gSAJk$pXWUKz*T4-3$o4r#>?65H>Src19_)4Xx+wr'
        b'D(tu4U!~u4LGl3iw9u~os4`H0qu;cAh~e9Vcyt=48Mq3~9YHj>SB5+qVZJhtb_DV04Bj5m{Ox%M_u?>bqhC4CCkOImTTtC_-wyLC'
        b'Hh+7a5BK;&t}++Ks@vaqAFTKe<@}w~-1Qx3KISxAzXQ!bIL)5#K=T;y>l1!`{d;qu?A;Zli|yj&m~QdSIhl8AZ(;NFZ$W(h0xxI9'
        b'ExvNvZV4)<Adq*CaGI^R_;lmGTLSk(B7^FN`?6>Qy?o1+<-ub?^56`odH)vQocrvSz_mUyXwG@}U#dcKE-YqYm~MujpYGLG1-9|g'
        b'$-XjheA21{^_>NNe&ol(Dxa>0?Jf6<M|rfu&yQ_w^7Erk(&pz!x!>vMM|*UGpC89`i=Q8D@Ev}B?4w<N?L)iqY3{#K)*1c$Xzv~M'
        b'^P?^IvY#LAwAZ-*x(A0e5pT`Pu}{+6bo$h(1+2tIzi-u^1a-b7pFJ1AeK+7s`NSg>L)dRv8t_B9?%zGO`2T&pZ&b&R4_*!KE?`E>'
        b'!-c-Elbmmk-s21VHf}PJZe9})nn1a@rzSzCT<}J#CVGV;@f_uK%;V`%8v)$C@VkHU7ilmL>~}Hu5-m!rxh$FA$AoVHmevIABdV`b'
        b'LRh;hZwfpgOPaiM@LYgr5FY<D)rD21rZTa*rmE0XE}HUdN^1*AO<`F@VNFor(!#vz%KXKbh3AzmDXgiitSJc!H#=-?c)*MwSM|wC'
        b'{F`Qt@N~h0eiz_#55U|9Jatq<pRd8c3H<lMgSeGH824jNHzwd85;zVWb}#f&*f{*-1|V3jVP!*SX@BUGE&Ri4L7$*wr})I$-q~iQ'
        b'caZVse7%ic=ywwS?cF5bcXpHgeh(~XY3W>JYqep^JLF5KcyRzp*-vL>0v)~W*7?8KdmF$etFv$XBx%}Gsun4Tih6^5v|6AoNGl68'
        b'Nt4oOKVp;ep|~_{Q<~W(F-f5~riG!R!>x2~;>Tt|+}NfQ9X?|YH|E18-E=aijy-deN5#3#ZRk)DaQ*+TbIzUn&PNMwd-lH1|21&+'
        b'cg}UbKkswy`<&|v1*OChDXfK#46tcU-fCr*Dju$_CmQ7kmV?~^l8Q;L3oR~BW99tPG7?J`AeTi5K*tkOeaFKq6RO3eyd-&$QFRI@'
        b'2~U!T9E<A9id7G~tLhQ$93-1oizNA344q&Le&?4mS*t%(uX@yp#NnPiO>hw+WMV1O8c5ul@Z->`Vnk0(9`C|SL|k+{VUCECq=Y4I'
        b')2ZI3Y2Fey$<sW|(0dZSLte9ANw+CR3U+a#IO=&1F8+wlC?sVy%^$fio1t{0ENDb`)R<jC;<zm<smN55bW&2DjaGY|jHN^*73aq#'
        b'^>?_FFPxo`H|^qume3-tUWNP(Ixs>)<M=ge1s>S6Bwy;?6=L!bhzRC|7H%Pr{umwKP*esN)FUrQ!6Up+(_+&#j=afF?h7-f*dB=c'
        b'gHkS_E*EUXs7Q08BV$}KM3xYAn--xwU&G}qiDR~kg&+Ijg$eWq<4j)mQCpyP8LM5+YOiLs9uJcTV^XhI%ZY_cP1iEisY%#H$+??_'
        b'TNkDHp-f5_CPnCabhDHyJhw#Y?CJK?5lnwOKgp!}t<C6JJzlSQuXDpAzc!YTM8LdtO-$U3&~AiARZR@c>t4#lNjmP%wId`ZSAKX)'
        b'35JAlb<yu!3oSy_i8@`i_5{1yxhE+Dg}E+OV+hD2@)@FH7)9DFF2qcA@q<kbrTDKKEqrd#`B30qhX12^DPvBXuFm+u)EIb+)0ia+'
        b'3CNf7<LP>ZuBOGAFiHeror_0s8Z8FdF;_;zJ&{<t18IU?oPmAnDB(qw?5O#2UXr1B`mCw~;zZi27<5LW)RX$7xTjM@kN#qX-zsBu'
        b'&LwJdb<qjHWZ8g9U==zZe7Wjb%0o{|o(R%OU<dOw;jc$Z`6k)k%(1j#ag!tQq>?q((dAz$W(&IbwleBRPc9v6wru~J!A{G`OJZir'
        b'B2dc%VohL$`MY&yOC0XBS6>c0>2-bc8)9F&8}@s#hkbpAurG@vE<?6upR`9|pO5(895mQzT~_dQgZ;PIf5&z9nFzmPt7boW)NI+b'
        b'L%f^$2EsSxn=N-fVzAS4^cmPcxBz=Bq)+RY7Wn@Scn7|rtzmu#`#zohzhU34v(Gw+GU)8D!~LOhgPp&>g!y6Qr~g5b|Lh*K<qFV-'
        b'2Zg%_=2f6xY43yiLD1f>$^63n1ZdKO!u|u84}$Wg{pB7y+hewPW&Qja_L5a*%hBy3zBw>Af%;+R?_*HDufxAZx-Ws-b)b^%BL5+n'
        b'KM$HL?VDkK6tsVv@V^V@AA|Nt`w-0U6=YiuN&6pRH<0cjX*a`c1idBgB`|lrXSUQmAnZ=qmw_s!eFe;GQHE*KeiQ5uf|#`LfcZPf'
        b'|Bkr^JMAN1M?1d&-i~>~UW#;n3;Voz!vAY98+uV5*&b$?XM!TqeksgOQ2t!e{{5(*TC#7`>{r6R_A(Lw0i@Rm`^Ig;ehl^{uovzS'
        b'_4^ju?P}N^vb=tnwc9xSLS`$;3(-knte206#DP{W`}jJN@7TpfGxvzwr9E6=8c8Oji|4a6A&s5Em7VY$4G4)??fgb);!=>9U}h_e'
        b'XVKK6%3G20fP|QpSc-hg40)mp+H~n~wiJXf7twU>8A<m@?MJi4$=x~5S$u`Nx--}%#2X1=R{t|a)f52DmU3OCI9Yj1InWysSDNYW'
        b'Ly)h&Y4ViUY5C(w6~q&ek^uQ_GP<U(%FwNxJy(r2(Q*l=c?r{H$-*@=WUW2e&SRlznJzI=21%k%Bp7H5Bm}hxS*5Co7kP7{gUhne'
        b'=V@L-%%ezxuAWLEu}Ojrg~Azrn>ES5{?ZEhAsI?YFL4z`C(tuFpj)2iPh^d2U*h6#_>pS8s77QfN)q1Nu>6T>cW*j66um4rz6@N='
        b'MU1DURUPi>5_QJKUnEI^l=YP+ohLO(O*}#g7NzMqQA3ub=S7OQjp12KilG#7W}FK#=9)QWUK6@w6lX6<7t~rn+_X}PrqvcFE3T^3'
        b'mqZn(D&v=(Q+nnZNz+!Pn?gnmlzw?d2;vzf$Y_->FJ>jRfhr+IiCy307aP-H?BCHcZoTsIG~MO1^%oCPN@e%ACw9_89u?gKY{lwJ'
        b'+!^3=l~;-^BI!I*lZO<b<(kt-lL}fj5KVcvpr+jb^Ac4UhDQ~KA=I;o9AXbYo5>rnborp8E4+HPcnx*ur^UPH+_mC8Z{J#RhW2l3'
        b'#rgKne@49HKk^x&BTTtboNr%#qd4#W;~T{}_p5Fa?~Sj&Nt|>4)=lD^`+wae&bgn}C(gOs`@}i-KlO=o?qk=9bMBMYiF59i>%=+t'
        b'_I2W%`>pH5Irnb^<x_<;|HQaxO%i-fQc0w+TRu|!Qk=I^CwMg1@IFNXNJ&_zkO7%AS?eNJl{!QfzVZ#WX}jodO?Wt$=rx;>;w-s~'
        b'QHP$I96dEwhJrT;!5mT!18*%=vaN_0{sO^OQa+hKq~$3gFIP$@PtvZZHmWM}Rc1@~#)c%wXd;JFZni7kJu#B;fbBxS&sD!i70fB('
        b'8h)y5R-3lRrcI^V?G(D9G%K3W9_Z)N+5_!62~DXo{X~VSHPz-1QJz)F_;{>yEqIzNKJn;8(MX;j=DJX<hs58+y2D{o5vX3GRUaXK'
        b'(kD2Z$+k>Lvm?=*V!^=mF{_^W!UDyn*DgGv*-3YswalrauxXN^2;@}j?}~*rr5g2^S#)wl>Fp!ma_Z%5%XU_a&)wDD5)kva+NJa_'
        b'J&+ZW<C9R=p~`EJLhJZ#Vf7xe*30xyTcO}t$jOsWUCMwEnked+FIIR!yS8%|&f5N2EsU_q8*;q9FxdF5{cv20<`6P3PqFU1Lc1HR'
        b'tyP2kBBG2y?-~j#GZ)SjvRFg3K8(@xsWaFbq@u0lt*#fot4T-IbaKpAFMG)+ET1})2O4V*C8|;3SFMEfzLiPcO3Ws-=;Lo-X-emU'
        b'qx>N*X)e_>m*?RZay2l>_|88q3Qf3Ir|cDLxXeE(ElSAxAtA~gd~KZ4(GwAA<@SdZsaH*%Lq^Rdmzbpm<_}gr)23#$DG&+xwMrM$'
        b'W~!%#@W@dJbsx#8Q@hHS1EP|o@(V6vCXp-j_HJ6tBt%4L0;Xj{rPoW06ePsN43W4xDS}bvX7fvsy?kMuQ9Msnc5H2MExv57kpIQS'
        b'zsR|PL{Rdza+$jAp<YPy=ZMw7SN@^!sp^2M$q^+_(zB6}Lqsbstgz@|ND|LOvq)A_K&yYgJfR#VnpzA@eXWs13ewKe6U$VkA0=7&'
        b'I#DFt9O9F^R^92{Y4N<dv&&QsN13$1stP;!TWGoR*B*5G0Q?JtxI8Gkhx&lyou1Zz+Tcz+=o4c~#HC85n$3hNCB81}5c;ChdKb@_'
        b'+6%ZiXx%+#(rF+BM`?>=zBcF);zxzjsHCP5QjMxT9zOf(FS-i}vTk0*>f`(BWm2>rJ($&x0$p5!1YaizVS}@E;(rqlBob4RQnbco'
        b'bqq<xN>}TU(8)l$*0i}@zv-}fs~2cruBc*UQ_}8`OV&(s<fEv5ewkYFd|siJ?h3ZWQ<mTgUxO!>B6>BMI{93)Q&kv?4eM-GJG9o-'
        b'lWRhCR(qZ*F1SS1QL#pSd%$ajwz2YCqv&0l5dWl?4++`$T&zBchm3ckmat6ij>Hq<uH&o2se2qD4mlyJkbeYZ)v0q8PeZ;MX$~b8'
        b'k{v;QwYVEYSMERDQk79s+33c3Cn+S6y9=!jNtkYoKCpy>V!NU5@)UVnG{}`xh!?(^o+`?tx}~Fq2hR%f#zj!bA;-5lN|>Zk@|PI8'
        b'to2A~O?*5D6Vmbdvn8I&(|=lztQUKlUF*f3#_(COr@8F2Vo%fkS+S@2=4Zv8=8eyaJx%!rv8Vac2C=7kZiCp<<lQXxG~S!Vp61@0'
        b'#h&Jco5h}H@-1RdbL}l+PxHlF#Gd9mw}?H>Q@4mc&5O5)J<Zr##h#|&R&jUt##_bR-A8W~cX!{vRova3yiwfU?cFHu?tXcrxV!uG'
        b'Msaud*hX=8cgAhv?r!upad-Edw~4#E&)g>N?*8F6ad-FP+r{18n%l+Q-MelVcXtonF7ECgy<ObhE%}_dyBqtQxVyXkbK>sqlb;iJ'
        b'cc1&5xVxLZN!;C4fTY)aIk1f0>uwTvc^}v$?()(ekM8n5u}R$J{q-hsm-qZT#9iK+JH%by8}ATzdGEbL+~wU3tf%uXzy>-K25bbr'
        b'2lUdtn$Mdp9|9|YOX&SJa4B%*=SiP3>J2EAw3ka|?Q?<M{!fLYguxIY*EHx8v#^hU9P_o2TxIb1O?l>1Wt1_Wzm>}qftR2rgPkl~'
        b'befL~4fAoWR6Ydp34z0UPBgHJNyUg_%rYPKWS^8G;*$bWeNi8OmTHV}SG(^9=9Ass7makwysDhGSWI$)pSmuQQOV+u1Ydhld;?Bm'
        b'if4XGWZ{r5;?<}LY_yrLqbnS4CkH%1d<hu_zK&$8zuh09!O!{9l?2T&$~3P+U$1~Q0&WoC7tku8O+b%;RRWL``M}_{rr9Di>mi5g'
        b'qgy&Btg1W7$MbasNREq-zk>CNPw~Q1uG%PcjK4ilIbuE&-k6U|hftk_g$n=?ZOOmW`$+jVN*@iN4FcWa=o*@j`n7Xmd-^rq?fd#Q'
        b'-R(c^*L1gEvsu&K{;PgXcl+=9HQnuR^lQ4?kMwK0+mH8ay4!O$Yr5MfY}RzQ&)lr(ZlAwd)7|datm$sQYO|)hy>+vuyZ!pjn(p?`'
        b'Zq{_Se`&L(yM4!IG4JtniJLXu?FTk%y4zpgtm$rlbF-KS>Gzk-VlJfLyPL&)$dCLCh&hqp7ab7uB0q;WAm&DX=WsyGkNhswfS4oc'
        b'S1};wNqz@sK+Ki=JJe<|U(&B`K+Ku^9MyoBH~D${0Wo*d&p#mMPx^HZh&hy>KN=A8DE;ORh`E&CUm6heDZgJcAm&uAtA0SttMqFe'
        b'5OXU(4>};`SALd$K+LiHWZ!_8XZbnf0WsIoFFGLRTYds<K+L)H>mLyFE<fu#Am(2B?HmyEFYku~Vh*O?(14hSd4C%ab1^?7J0Rv`'
        b'`n^9O<SX#AvR@Q37WmznFA6ye{Ep-og{%eo{doMd<12q)u>XAg&&Qv9!eB2hEGs;=$6#Mr=q!8)xVW&f(E6moes$s1g*(1)uwPTy'
        b'R=5Y)Uf5o^2^c6071qJun!@!Q?<o8-$E}6m<oI~u4>%4LKF{&Dg>P_tyYM(i^Mo@e5S}yPoC$@9Z_<QG6N-T6PM9*m0-QQw>V#fk'
        b'$%J_m@{!M1CcHA?80^E$U^ETWuf*2VtElp0T#aId!bQi-PT{IA8C33^Mn&g4jjamsqxi-5bZSdX3U7VcY>5MncbP3@=kG`F(#`-|'
        b'<|LozSDrW6H@#@EJ6;suQR6bq99<Ztbo4OlJ@3UbjJuS%%b2^Ix#u$XJm$WPx#u%?1#?$2_vLURXSkQaLm7OO!AlwZl)+OOe3ijl'
        b'8T^&QUpd7Cf8}$Tvy?f@n6sQYVV=jFmoevj=B!|I*qi|NYotL(cl2*R%d#H;9R%eYvh0U|Z_2ZRM<gBt7Q!w6_Xds!-#~eQlMTXs'
        b'-W#HP2M;HoL6$<JnJ>^0^U<nVsz>e$l7e0EI{jU<+gKnLnOpADGg((hY}TT-j+L_(32nxh=#?o8mC}?5=D;5!(0tQJHl1(Hp^e1k'
        b'p2}sqk}2JVr{!NuImJKUfv5Y|MZ*Kky992&P-Jy^QE6|7{3&ykqD(Q(D!*i2aWUzX&g7bwxY(zr791;$>-?RGVlEoZak^5;v#HFO'
        b'p%nE5L-9yF>Wdd=@-O9VO;_fn)<g(PBOkpVK)%Z_yG-XodzOSt*}RH*m2>CMtI&Dy$B~}&P*#eLt~p`3<);&Zs&mE~!NQ5$cy6$G'
        b'5G^IDcBObT4Q4S{PPTTf5{^c&gN!MQD8%&Gg6ZuG_!eq`QXP&)dm?-@8l)3{K@!2Ne7dxEdT)tBe?K!lmdA$WZ}w~!izpUlE{pKy'
        b'mRSNPt%XQdG83+-wIa%zPdLSkXO$OIu0{__-_|Zwcw>!J3CWpAPo}Imxv&i+!#PTF&I77OmFYcHKH;l9(Au+d0sr<UVnj_)6_Af2'
        b'YEiT+KTI@3sjKn$8huNf8XM}C7gNf52BX(9!T4+{!6+k2BucW#7AT$`Ec8X9l%jmI-9|h6o)9THr{y8#1FeMExFBlk-x1i8B5F<u'
        b'evU;jsid`JQc0cs6CppIsHM-}=dMbsnAE7nr$t?$w3wR$3AGIR94NCEjh>^LV6RXuwkjZB6GTUd34c3#^C*HTMX0TapT82qXr_@N'
        b'8^qbv<ZEbjHh7COrXohgX=Mmgc*m>^{{Mjjb?6h1jZ~-+BT4tKd6(VXCBHtXGP74r@9dckO7p1yYLS@Bil+CVYfbMd9@Tqdf;&C$'
        b'iRo@+?`p0^FBDyzd}ES7wRb+MGWk|(kiR}w6|0CDl4`HCQX}e0G<|e;VdLrx#^~jfm{B>WL@A2JqdjeLCE@9kVycGX%#%ZtBV}?B'
        b'jE|lMhIlcb=3($r0B+$8pgtUhEgtCV(ri)xYD5(xahp0XX&e%^nG}d-8=ZTK6&`3Ip<^W3xK;_xO1Z_<m&iT6BEhbh+gs^vMyM^}'
        b'#y{{yWoTk(BVWv?BH9@C({!?$j~+Fmj;@|qr)r^TRy7BreqD?rRC0vylqdpy(G+{8g703iUkQEUq0(Q^=(oMR>gZM1UAN5tSiR+X'
        b'vs?M>?ms)ec-E0OA9(4dP2chVZ0A$$_rCD_FK_96HE(e8J5N4Y$Cq+79;q%syluv&(P<EC<PDb??QW0-q<{_;8|}HkqrknOhd^DR'
        b'c!|;e%%#FS4-_dvIPeOAJ7yZ~8$gGq8|~H^M*C#YTQEmD*Tnd1AsPoBx64;kXY<ths%_P^&T@C{a*waZ=Bi_JT#lMK)E40oowc3g'
        b'k3@Vu5xPAx2TNC97;BGkgw~;WfFPoV=DIqjI;;%DeezR;kCa~W7uBpg91Hro0wH=-&n-_&fUdlBh5haHZbZxpb7IjpJsV>u)`=9m'
        b'F(z~oack?Ec)%Cx=_cMhmKw+>KZE<^#}JOl5?Y!*gQ)pG%`64mJCd9_{m4`_5EqZ^WS8>G=A)a3g6Mkb4zz+}!7w`4O3Fh~Vu_hC'
        b'H{wgcoRyJa80iuC#Mdg;;qO8Z9>G6)RvY~Dy_xzhh<F%>SVncM^u@!zm0jUhe;08`(04G>i4~XI+2nH9`sy1U&2>&+y=~b@35XEB'
        b'ws@5GHPY4{ZtvkEpWZ$u^Q8Fq6t0w}+8$gLqytG<g_hHkTD7BDNfp9;mXZfNbm#D`RBY~?V5qIDr#--V^u{#m>*|`_$y6hzvA9ph'
        b'r<2`e*4^jCGJeF)K%KjDb)qA{7)9?1cZ<Co&1GGZgVjdSs&+Zo&sgHDb~ruN7-l|Ct*y!FD4sDRvvWgZgY;2+s?^a_qCWaoLQNZ6'
        b')t<;T%se~XgId!G1}$n?Fy>noXhT&5Vr@S0DTL9vIKk)$qkD#XqHSXTfG+LyxP6URo+?NDkJ=K^cpIN6DRZdwFn!s?5XF|b2OYI7'
        b'(u0RGV(z846^jFLY%l^YM^WZd2P18K)JZeVIFYvL?To(KBaTSBx2f4lJZy1d*D>i$%+r()>gK(1^lp-LPg7G7f8I8Et9{G7wmM%;'
        b'lk+OyywduNiHmpXqHwWrTcUu7l#lrsV}<R7Gs!EZqdpw?``06e7BSw8EvfcZc#tI3E_L;(HHq`5m=J<oixxcc^Jw9&z|_$)sA`#M'
        b'W1~gO#imEZM_omXyD3wdm?7o-B^$e)=9XwcEztfBJbOM<VQmgw7YeTqu^a<_4q7&8XAS8LS1gP@0Q2x$d;DY=t6gm;mES@^8e8g*'
        b'w{;40neGU(o?oix+nb!WE4h~AsI)YwHlDgGM8<ml8eD1b>5ho)7<2JWpZL73-B3$9EGfPZmWbne{8OR7y*)~wBl)(4){4Ox#Z?3<'
        b'J|j<!GeS!aRNp@vt>a&qMaRE3YfEW4CzKoNKB7hwUuD}xa%d-^E^f8vpOgtvcS3#D*EcKZrf3*(QZHjv{x(&0Hdl)z^MgFl!%%8B'
        b'?d}or6f>G96sC<1YVie391NEyA4o~Br->gG2=vAmARkV5b(w<S0v@dbYk9JDZnAY=!s@P8_>Z|g(qJo94P~mKTs6#94f9mPWvXGm'
        b'YN${Rm8#+LM1-ZPp-eTDtA@F%VV-IbQ8SONNf?~Vs;h0y9w!-=*c^@~R%drE=1z6a28S?IH#RqT75Ywb%R^?%7eHG;TS4CheFwA$'
        b'^kdM^LB9eW0{sE>4(J3Z>tVCy4A4Z-MW7;38E65h8dL{rewgl}sFMP<O;1Ryv-s%&K7q)&0#@mwv?os{%n|OP7YQ0e^Lkw%8VYpj'
        b'oT|f81v?!!O>nttCwgzCtZt7dRJS5a)$ZofQC-VeHSgdFb?mKl!HlaMQ^Y4X-UUf*0PntmcIN6LMI~LXkl310`kpm0`YOnDyqW-}'
        b'IVaa9QHOy_C#nO|N}mqP5}D$vmfQS1mzWA2e9>ZGb9EpZMz7?DSm?(5Dh#2ONIemmtt+@PL?4eus&0o3BPu09x2wj1b*JD8Z?2lm'
        b'{xmN6^VZqvjB~<_K^?3OillhS5;+plN}hU>Qj1xQD2YL_bq3?Q^b@fWOBauHP1vg=r4ADN9w`%0E?};Jc>*pIFke80L&#(QHTvqC'
        b'Amg{qmhqt3AP1-w)CYPLv=8(Q=vC0$Aj2bOOD<?KXc}k^=<7QK*<tp8f}l@>HiNzbdRY3|tMg0rBJ6K~PDuWlJI$60c53dkV4es1'
        b'1jr6@f!v^_pihF%$U7s?j(L|p<p&n91vH28Hx|nl2w=)u%dG0grlw}M*XfY92Cu83nXUw5{lFK;tVp5P+jGl(aiv&^(Biv;9wD<9'
        b'`ODH)9khmw#=|kOD55L3F+VrcHwpUOLEnc?wR#l`by`u;X#jp)uamw}1!DB5z&b>%KHBLOu*Red%5{y^SJIk|%kn51!Huu*iYQw3'
        b'MJR2}ikY5cK~2@vFs7yiAHo^)6KxPu{g#!MvP&+x#M#u;*aTE;bchm<JoVZGzo>;3C>~IWGso%yX?i6tib-!Q0`$Hi!SJ{7<4`QZ'
        b'SHmuGyDJ#O`pGXUQ~jnZ$xYwb49O(+b_VQcj4YR#M9U&CK1^<W4OfI#uW>E*(eln~^IYj$>hSu!u6k!<v)AV-QTPtBI5`}i#zmx-'
        b'&R05;Ls>DSFH@)JBJ@XYxM_db>#eqn8zbHT7HsOqCDO|aoWW(4EfVRHhsUs4pc^ewFY+RmeW}haWK8Eu`O`KAa+xg9N3S&Gi-5!q'
        b'iSMb3oL-O5v)n@!)P(wKTI}?e`kao%PM@p6+vM{!HaAr}l}i=AlPTegX6{f^XIt!ZHQDNwwF*BCQlj87;0?B2=ZZyZ`SS}4uo<*y'
        b'=bKXOR7-dvi`l8GkcVocea9;5DV_jI!Yc!HcU4cIC*Yx-6hFZZ-iU2-J$dB~krrsyqMqJ*aZ4z+)E^X54wMl*)(HhI(v|fH6kKJI'
        b'QlvE7(a*hWA^|?Dl!_Kc3AjK0zN2VW7z6K;Vsx-6MF<h;5svCrqhvpbgg(S6J-se$c|7Vj60k=IzVKARr>Mbu)!1ki9PTJmcs!JE'
        b'mMJ|<O2pO|n9@>YMZu>lWM4yig6HT%7xU=Sl0ZL74@jTo(zvpit0+cqSkz<YLdsU5cG8zNtx=k_+UvzKYE43)A}>#olH|Kw$rQh='
        b'0K{IVi;RXKMx%!oP1t5esp$h^=baXBsTOZ9jg^=;OubKQo<wSqwp!Y{rt}LmhnAn&y`Dg~KhlX=eRgks4|V~y;VycEwD2Dcq!y)G'
        b'90?<v7|BJHG47dVs&4)=P&8Od_D|JhBjzS;JWzj<;nbR^{vj{q6_1dTF3f3mkX~1)GeBP$Lv4XZbq6;>Q>vX*X5wGbKUZ<j4lay{'
        b'iIDQvQ%yA7jr|@|rzlx%UjKC|9;Iz@S{SZRDA?u+gxXbyNOV<0I3Da+lRm4ag^?Uekhc_)>xssa6U^)&;;81=2r}`+WSQ*JBwnY|'
        b'BXr~mo}P9w^+}5wZWA$)24AtQh--~U%f3o=a5KIFsiy0xOK9tj;CPA_MfeC1%_;q~CH(M*w(zBUexqOZikEte7V_g0(q<7K^;O4('
        b'3yZL@s;Ch^r8vVxj6CpZSiCc|DCOw!z3MYwjKgcV+qG$<gNfllosDZh4zyF4I=b4)`@PT*-Pqycw{aF`=zXB7^gd40+=7v2F%*GP'
        b'QRlsO-7CsSuai!(QwCse4z-FS_0*QAVm!zjdwAPwGa!HXGz3;-D-@2BPHhVkEx$}lCesW%WrSh*kpl4E&=Bb5)1AyJWs$Z9Jcrf%'
        b'`~~k~yokN(^jK}bCiS)MwTZ4MX0t%7Hqg~B15Y_+U`!FA_CT+EC|Hy-jU$FB=kemHoJ4|M+#U?H^F8x5N@~b!Df2g$HrMgaGK2aG'
        b'52!U2^$x0V%-*XK^FZ3vI`U|wl_eI;{Hco7T$C#$^{G1`)f-=;#(Zs>SL}!Ab}GZf5$}nHL@UiIqo-kX6_r)(6iuW(ovjkB%V!Bu'
        b'HvLrB)0O7Tr^uv;uqO_RY2HTa|K!baQL*WM1fNe9HQ}h*eL1r!K&KEWZLPzLl)A7@Z44#2q=u0c`C=2F(VbDPc=%cC+ThAg_*V15'
        b'$5_3aJ(%Ig^WajC(Nkwl^!?<C1Np9YH>-IjJ*1c)MNT}lK}d|0<a)vbK`{8NLd_wbOne|GEOnlQC;rspwWXWb-N8@@gFj6DobiPZ'
        b'R`PDtY`EPO;&T8$m^Dhz;#&xs=)K)h#j~nS?J7*fMONAz^Cbf3pj(faN@NvxQukLbhm1viB#G~)R6cEoikV67KccJL;tia78M#{3'
        b'%&R#$dn0t~ClSKKFMM$;wRKD;DC#J&$<sty8g!J&o<Rg=l06fuWYke6`>E11q{#Kn6n>=q<)p-u8s7X7<1>ClyD6m%sX|4wQqsvv'
        b'$*(yjFQydttW(raR!ZHPQ^L~(N?*mXk8ck~{oTHH{7Fo`?R+brK1w<R{s{l$YxDDC3a5w$OF1kUL~P0oWp1%pzZa2%&Q39^FDCfM'
        b'H5!e0hRS=d{1a9nD)0TpNU<~z;ivcAQ`19(&EGc^pDHBX(n%axO%#h?I|;Yx7&1Z~hkx=-^WbZxcTnkUDON$}(w*!;wI*JY(76F#'
        b'k@VFjEr4LCCo^lEHn-2?x;pbYg5<VRKOA#Lu$>=o4fS;U$R5+U3-w%2oy+6(IqTit<wY~p&qH)Qh+K<#pqS4ejr!Ll-YO-h$J9VP'
        b'2)&04L@|wB6TEh|=n}|;o=GeJjK$!uYs5zaAD#|qOJ7es*cB6Bi)DE1_{-FY7b$6pF>!tgP483PeBy&cOv;g#>R}8Cnc~(8D=B43'
        b'jNQKdRjf~r^**>UI-_rpW4{vipX%(F!~Qd!eF5yx=<J_>{aKxz)LZ_%s^BhlE?H<Txa;RtM>?f!?z<Mk{W+d~;&<q*7E+3(-YxQY'
        b'ZPi!KaWvWLnPU#UFC*EL1PzT1K1aRH$DNwI)dX}G>1neitAMe*TwRpJb2BzJSDP^Y^t3oXl|Kn}VHNrLGkB)l<T>pf@>i(I^`_qk'
        b'G7Y27Z}xupLpk*P&eT^|sr?`nSltzDox@cw%Xi{QgT6T=MR;);F5H=}vQJHH_2RlcKP^i;`OYF`!6}a}5jU~z70Vi59GmQze6#86'
        b'<}WBt*LPIirOI$LYl`yls|<3m@a-RG_(I{(4fIt?|8Cp2QY;#n{{41>DZ+_EfT2|hwYY4zDa*dA&uHHZj1z)3fewMTgPsBZph=VG'
        b'{5s5&*BR~IZvV;vtsrL87wDqm*_enuf$PQYu85>Zk}aI}h81ax!(se%3E3iu2&)$Sjm~b1M0nu?(I_@Va9yx~(y15D3l`9a_9Dra'
        b'2iz_xNqj}oOvNnT6&vwPkvxl`B2|sQ%O`J;&=x)u-zS+uICDFH2(*fC1zG*9B^Q(rDgYINCV?h{6wowK5vT-I3YrJ11X(~<kONc;'
        b'ssp(}UeGd7s_5)4@FJi%s28*r)CbxC+6dYN>IdBk+5)-{Gzi)b+5vh9v=g)ov>UVsv=_7w<dXW?=+4kpBwroBCW#)2UWxP@&CiAn'
        b'l=ob&o05qOdbvWqC1!>`smMyVZc*>~Z9L6zMqN0rck496W$D6k9WSRDE>{<h@Xpf=SD*_=X>U2raEdM**Zq2$;jFrFG`|j>X1G3G'
        b'I9eBPKh1DtRl|{o9j6=4sD-0Dtq+}UxGXIk-GAMAy5VxQaCBF8*Xf2U(8AI4fA{HzQ?zh&2Y1iuhO=tn=)UgW(+$_Bg`>N@`%X6;'
        b'>}ojbtNTwooG}rO{62Hq;j$9pXr4K6+Tn5&;pi^%3#T2fAQ6t19S2W4oRSDPLANh5>U5Uq&#&gnew-)!SH5ibGi7@e$a*?k=D$$J'
        b'JN$3_QQpdB{w~XKRv;D$%I9+8=r})RPD0tjQSE!N>X>x;Ji+yKW0jM_;s^bGToOx)3qQd|_ZCw4{5hM>7WW;}y{53R5J};L0==}l'
        b'7bh;m5wXY`adn{8gt#}UZX^;P<M{yuUohs2`9lGp@T4AEDk|0|)E4QX#ow$l7LIpfmy<YxTb4L5OUsBNohyB(Rx?0Rh#PYqJ)yP|'
        b'MO}v~I{)(1fbP{TKgU5%+KJ!fEU_s?qkSmkZ~v-mopb=5E@^pv*f%tJoeo+?izuh?V;x#P#VK-MP(4T$6SacPU#Q)e$gD1atgep`'
        b'f>yxdUT=(dGQMm?^LMm`;@HB8Z^ZPGgCAO?n<o5tN@KOJzP{P#w(&y*;?hMC1&v)pe?#GGi!;3J)4G62oD!r%)frQ!cLV%u%T)F3'
        b'q*(TIsiSfS;P0Z2O0td-L4<Z4TFJUOQ_oNniLqdqw!n1Ip`PxHxEg(qic{t`oOtunO-^(zBp7BFUZh-b{^aRXrd~X)D?kH>&S=mT'
        b'&p>FD82K4{9;-hRq-|A7P&$jy+7nZ^8)7Vq0Ah3pLT%ACk$Ad`&Ms#NzSqVsC&*8VkUV?-@@M4C=>|%S4-q<BLhTd@mT3-R+q5P~'
        b'A3tL8XsE3_QiQz+YB=6mLPx!4Eg~ar{yT!b=^VQAQk*#}@JfUv<Cx!Kq*sAQ%jRIn&uI^=nj=q<OZgdtM!t`FOCpy~k&XQo?0a>*'
        b')BR;_6=5a=OSdM6Ujcg@v<Wnr;<kHhdRn#MX@@-%<5HR4PRBE8BAebmC6CoRE@PfrTN(W!DlebM;j;Mzb1S*+va)jKJSb$BSn*t4'
        b'bWq4NDTTS>ppbQ<;8|OGP{=@;4D-x`LN-bv%oiUNGE)kyEa`Q|Kl1xO9sZyF8ML3tV8}6<4F;ppXfkDGnN3-yEHhKoUlIM3wBN>p'
        b'<X=|eCmA;WGi3M)cRT+XGyKR^VgGOZE|NN^ua<g#?*cteYf+M|OzS%=5KBP~2H|(I40B-$j>P+@{xA3l{+pc62CpLC5G%2sHX$;Q'
        b'&EZ;IV*Fwq2?&mnxT9GOi|5Sd4)T!cEP456R-mgxyt5H6+SK=L!Pd4pLMIGCJWMC$NM6y9(O&el(LM{b5i|t*)1V0GPS909Guod7'
        b'zZ7`x&xBni;*Uh<rnuMqES>+r)1${hq^7e=`cF+iQyi4m1G+Tz>FfQI`4!N_{g~H5?}6r{%u9gJ{M2ZV{Z!!nlE{4ivqt+1e->1%'
        b'GZP(tMl;WbTj|e*`BLB~q&f5)=KIqieY~l3{R;wf4;bx#IUwvRrTX2ai!1(0vfKXGWWHb5c(yl3PdhdJ4^q<q-gAO?T&DY?#HW5^'
        b'wBLmE5520nQTpFTogLAoe}zn+_@ybo)G5=|P{V?u4%T36U?G2qm6nyyop;&%iptCVt!?dr4jsd0uXZ?VnD=V7xZcaAmz7>K>(bI$'
        b'm)mAt?VokSwbMhKrP=D~u77B@?k}6eVS(;1n{P7N+nLE81nmQvVK;#uGMelMKzC%B>>q&N1#Hd|c9n=f5;do|ug^;7zrse3gGf#1'
        b'i1eSDex^7mtygqu>eJWzC-eCRlf4Oa5>$@zMnMBG=feLZCV{^(2_o~QIVSsCGX-6)GZVd=t(h0W&6+FBp8#Gd%{PuQ**Ba9>ElhM'
        b'o6i(@UY^PR_dH=&Db?>jU0j>aO?La;1p+_3P~$D1I(piv>5mzkoc_=l!OPDReh$m@e>K5mzYFOfo2<D}`aeLO<zA%4-73>3{wc>!'
        b'i0)m-*RTeE!@u+i(@y60c$jW|+y5sYWjvv7to_@>lT5tpA=!1GQDv;%cJQvpp1;pB_v<@ey!buW<qN-l)bZh250-!Bu1(M7K5@<T'
        b'>hMGDMcMoFSl^+FHUDX=J||>;{PEpita<l?sy~<-E9=WIDE**z_4=zVKaAb<+r|k!Qre%C=QT~fg<3Aq`UQa-|5M<nj&bbUFx$pu'
        b'@15Poal^0f;uv`LSwh7p_7iWes;wa0cISEBK<nZAO1A;~FWk51CE&an?_QT*t>%*r9=v(!yj9g~f5Xb|AAPHuE!^Dl`m+D7wr+a7'
        b'_ku?zINX1I^`+O(yV5c6Vtw{=NBSJ^UGd*f8)rT4*!7iPuc_|+qvIv7$)44Oz6NRsJqY^)pgK?lG;4{;emD5}z;~O4T_xg=MC4a*'
        b'pSmQSe^b-waS*BL^h^J#>1T?A(z;2PrapbWe=>g`^bY7gkIDW#=xmg^9JmAdY-|?zX-Q=M{W6n%PgKw`otfxSo&7_Yv#u8A;pHa#'
        b'cxiTCgE{OpNFVP=^gR6CzvA@#5{++9whwj+yfdir7IdF}e3bq-Q_{ah^7hFxY?Ij0VzOU|^!KgQ+$jB3sHgjN>F<zrNc>aHTl6YC'
        b'OMNFUKk(<Mh6G1Fhhx+{o3qWTA;oj9_VzkuPiGvPHP)PM7@IJR9czMNEdM18;%CkUXKW5kV^pU+;;5d*&!jSP1!($(Pw~sae<O$N'
        b'oZK99uD0Qn9<p-zW|530vT=?u=-sgyg*zGWMCR_M-2WSXdHno@3GHTP*(?WbF^1)_u`HjR!Omo7@pto!zJj&XJtq70pl3j5z&;kV'
        b'>pqkHAm~e9HQ5dKn(T4lwO<u>m54tQU7O;5`&ZNXzrSbnIEd7Aj@={tr>37N4oZvow|_M~eZ7A&Uktn&l!dY`0Nnt(2lfK^|L#`='
        b'zV;PCWUknX^}rK?YISBJgU((Lvv->?Hv(Iw`AZL&?Dw7q>Ej)VrfxUc|GNG3{1W*dO5yDkc<51$xBl_dkB`zno|67c4+vhN<i8`!'
        b'^7syu{ZmN4V5jCr>HlQVWdD;c{bPdyiGQkj%iZX4k!<YhQ@p?U-|qhAK9hakkAz<IUB5P4?p$QHxXwE@C4U8@dD`ZwcDY7L=~V8?'
        b'uLfU!?iWG~@7@VjLSOveDt6Wo$Yo_e`?3{gEAyOyd7_Q|d5#Ty8!KzIG0&%MY{Bg|__47S55Vma8@q82+=pyz@J0A})yAIs3;dn1'
        b'v3F4J1$lP%*#bM_v9rPp>}<uwcJ^Sg9dX*({P}ivqs7jiw%ZZEeH)#tB00_^3z_87lMHD2&5>jnpCnn)Ad;>A3zEl7a#caUrDA}7'
        b'Lo#_t_A}^iI(a7Br=MyE^mlnigqFwOBKg&z?~`m`lBEp#F0Eo^+9YR~8jTK=Jx}My<abl5VUmgbNBQlP@-ZOagZ*8;-};lZKPvP6'
        b'b(*WGFM!s|@0jn(c)l;oxPjyw)0qj<8$h!3slR}HB#&O^pX4BK2E8QBR8JmhJ}Sd*kYPSYvaV%)7Rh&j7jZeY;vL|yEI%y*w#e_j'
        b'f2HrM@|*AH<U2$9{@N|W63&<Tc}}*)&tyGN-H}ZE8W3#=IzV5Qd7-)@nbJKn%oC(LK-SY?(A%I-%R`DevOMpDZl`yEvVJKJI<s^_'
        b'#`&ns(;Xz6TCP==$nV^xG9M>pyw}P0J|gqIM}9`XN7mbX*>2w;-KnyUsXu&@&JvP-02zNk_N$v^9_V}cAf54(pWyG1^?FbaGU_`q'
        b'S>`g?f3jtNro8@Cy6+&F*QAFR^s3A=_2*48@8Ue>5md{6RbWdr7p;u0<Gz%!rx5jlsf_JIRs00mbexkV>yX;y)xeyoH(h#zC1*w9'
        b'+!<e6XL<5xM{d}d6Os1Kmd5Y<%_|@JZPlb%4)2L6f2g|my>-uzjr~>HKcHs3lA72Pzg!cPL1lj1Y-s_3-|BA{=X;6&40yeu$lIEH'
        b'd44M4Fy=te_S`H^`(gG1cK{=xjk(%6y~;PR?|LKMul4s>*MPtA4KbI-NHam4wBgMb3aqc;;0v~2JEADG_HNpQbAR-uEEuJaslg}@'
        b'!{yY@m?3mxG4iUNPvjAcPfW=!Jha{cJ8~Z>-3bM{XubR`Gc!DZrRlw(J9C)fjvQvZBbOQbjLgt$Vy#`*arwEFE}1Qgv!>bO^x5mK'
        b'%y{yd%fm`Yx8gSbl|L9?gL2XNW)cl&S*R58Qw!oe0-d)OU*lufAQ65TS(&Ab=0hBkSLUeK>a^2|t)xJL3po%%)<{N{5FVVGA$b@g'
        b'urh;_l)u7CBCN#<a)6eBR)BgzYe8E;_knhU_J9t8UIrZlodiv~p0!K{Re~&_WuO(HUJw_$!078UmrY0pA-C06@2pQ)T@6cYbuNd`'
        b'*0eZ{CsdE8aa~tCb+LJUHI2;;jwFt!*-Z+|of=n)O-PHZ35>=DPkJiVP1R|<CC(;~tFa-CUvH~U&XB9Y<*C)B-mt{uv)gp35QBWe'
        b'qt}Hvu1@isp;+L0m%E+5dY7l(=B=(xa%pnf96m0EG&L4yLu2#eTA#;lt4>Z{&3uEcKC?rut%2^cB_~tgxWviZGbO`UI+y#rjg7v#'
        b'#)id74*cvy4V{$9ltyw3>s{)c4U4_CDaGM(LU@#(Bo_o}c8-*OlXrybY;Z1Bn>2&#GOq`fSKXAUwB+V+j_g)lvv@S8%-P|IW$wMQ'
        b'hDYx+Qeq5m3MzGqV}sY(;Pp9NH8m)5k{b!PUd)qU?)K{YcXORPx!V$h-w2_qw!0Q5IV4)H5q*)1v(mddn%#A-YP7bm&SrPkCApy{'
        b'oES4sM+P^0ldYk;)<+^w8f$#8EY`Bq=(Q#1j~G;R7ZrobT!S>dNzNW;owJ%Mv8GYYagsadP&QNAkB6<d)zu+}YU(ygE=`Sfb#@yG'
        b'vPln>aLe53`NM_@5q`qrt8VZnI}^v}@+6NV;nL)EI}x43=Wc4$+M~MB;nEKTZ6auHKqv?ABz6+Lqjd#`tsVo*!RHcvU>C8I>shdb'
        b'4BDj0T{xuH>rz*ZD>(wrQ9E-wR~{M5<k0ALr#iT5lI``4j+B&=Yn-#tIT}*pU*buLM>nmDXgsNfa@#zfrHxG~+|-8+XD+o}=}fLH'
        b'!ES7>bBLx$FD_-$S)CFQ_UtJfs>DoXq}s~Fr>K$f#+2fDmtlJFpo=#yO?GH<E_QjmO}3_#th>b{DV^)lp6|eh#-+)vFL`P0FZueV'
        b'K*DR%qCs+#hl3Vr^4uyNT$lix8f<9+oXcFEv@Gbll*26+FwITQBpzxj6Fae<@p`rDs&`_bBvk?DB=`4Zx3tPhaD`N;bp8mD$frrV'
        b'18->ESdtD@(Tz>Zli6sJ=6YvCN-WN0)lN(p_1@-Wero^cOmr>Tom11is@d6`GBosjeIu)R#3WBov*d<W9h;E0Gm~2*f4un`(qfbj'
        b'%?($g@f(uemQjdCv{i#cH!ipn?@~4Tg;k=YwkC)6$jj)Q%v{pw)z7&i<@(g-7d1i?bTZ%VNwzmRtC!$Uoik<BVaell)uatZ$yU2A'
        b'D%V!;$>gDicN|K8c?M@kZMC~vbi>r=V6rE4JswBeJU^nh<XK<ymOd}&!)JP8=)5$!@EE6oYOAgtIm3K%9l1CS9^IhCWRS^IeVt?e'
        b'C<(ad^W{>i5Ak?SYAeBNOxaN-xT)h#IOx}mp0xOz8xqS+U#<ShlI~nx>vE?!W6|MF9?`X4Z_1*PbFh&{zj3&l^p7*{lKPC}%%x2('
        b'3}LLpY{~o@Cw4x*TJ#Ft0*t$;ofnU(22aw2r%y#c#yH<;TWoVRWcEu-$ht;PN~3w}Jm~|7nANrhF*-brb=V|PWhU*dQv6jn(Ynot'
        b'r|^|dZ<;54y;CJORyWq6)$3h#%hUXdexqg^YxCrWRK1Cmuzbac$k?NK=Crb>_NGKU&XEFpG3G>#(H2;nlI%_gkK2ifftKfW%Sl{y'
        b'nzI*A&?ft0BtQ`)C!u=scxVCcP1Npa{-pRs>@94~bzaY@ykfd>HzX>1MDNQkE4>_z$4lZlW%@omPej2-FHp04G!J4pjNrk2rOXPg'
        b'=|_o#_Vb=vbrm{Vp52}+NAu%#sU0aj*Gn7gYIu=O(N21Qr&0N;cV3g2wOuvKM^B&X;&l9tS}}=KvDQ1C(vI#SV<Xap<4NDhYHSy;'
        b'mBpA<v?sC~(^#^9&KcqP&D~NSloY=sJxTSYPgBZPGs#V?m^~?u+6%R-Qe2RA3_ncF%?;J*PHtbVqbU>H<7{xG@M*<bouM2g993g2'
        b'_3;-OjVZ-TupJ&>Ew*;a&(I`iwJhjFqkC|;7CUt_ZAL$CJlm6(cJ<WFQ?~<xDc0WNMPKSJTJ__>s?sY~45#5G<BO9F{+h8haxHFf'
        b'rbpJ?;HqC-?-hI05tGC&xXv-6E0*iFgrmH>IPs|XK5@s_%@zZldxzZ!oDDPq?Z7PHGN2jQ4a^4K1k3?`3789f5I6?-17IHTdEi*!'
        b'AA$M6zf(Hn7#sgC(g98b8i7`z3AhB91&jdAz*~UXzz2Xiz&*fR;IDvVfNulyfO+pB9iRft2QC1f0c-}I2@C_z0^SZR06qvD2mDXq'
        b'*}zwT<AEoDg}{mLn=KQ7^MDh99^g5^IB*hhGw@vC!$7(W`ct3*_#2=Rcob*?o_!4E0nP@RfmZ<OW7nsE2H>ZGM&La_6YvT04}6LI'
        b'1CIc+f%zXG+(gFa01d!}KqIgLXaaTuvw$0bX5bfr*}&ZtPGRf-g#*4u;eaQJUyA%42Ol^MXap_*nt&c)7O)Fw2CfBW13wSU0d586'
        b'0>1+s1KbD91HK3x3;aDWANV2g3`*w&+5uP$JPT+Co(;SPI3CyyECk*RoB;d^a3XLQa4zs!;5^{#z{`Ngf$hLEPns<O;8b7-<sY~b'
        b'SP$$3wgH2{)xb{y`+?U1cL2M9PXg}(J_p<ad<}Rv#Sf$pnBzZ0{Q#!}jX)ca<f1GEW&y)MGw>E*Ht>F64sbUxm!!A=#{drl^MD@$'
        b'#{$p(JL(5m0z3og0G<h40Xz%121s|Nz62Zx{5J4xk~#w%Pw@fie$`3f1mO9@s4u#Q1w4o115N@i0iFvC0nY>82qXd6TYv`OBS0hY'
        b'0MG>d>#&dsQ^>L{W;cB!&$eW{=?p=(CC5$QVY4l{Zu*X$Z5iXHa{}3xJU4wK&bEvN<{Gjs`M?=K`gmIlGytyw8iCgXO~BiMS->4Y'
        b'Gw^9(Ht-D!7r{J1;eZ83gacjzGy$uCS-_=0Gw^y~Hn1O<1Ka`31?~aT2j|}a4ZtH54{(wR@c<VBvw%UM8Q2fZ20jkV0UiYA0^b1^'
        b'0LNuzTgCxPfoB7of#ZRn0Tu#x04D%{1)K={5O@x7hB@0Z3Ah+|F0d1L9&i)zeBh(N$-ozZWfTrr4xFByZJ7)70_RaWz{`LS0_OvN'
        b'3akMB30Mit&p~<n8Jh((03Bo>M7xn47zY}G{lwqN*mmLrze{}JFM%fD5n$F%k`sh_0Zs>I11-QDpcj}6>;lpU`I~?S;Fp0$;N!q7'
        b';7b%9c%1wl!1H7b`~l|yjlg9<6Y$f(EZ_q`GjKmJ8~7Js4lqA2+wzfQ+W%vM^Zx~6@JEn>pGgS*sYTh#^Pb{tgpAoj1!!olrzL1L'
        b'R-lbdp3xK<@w4+%1yNk6HR9i$llZ<E$>B<8b0I|;M7nzymvX`Pb<QQuI=v|O5~Z|6(FEqlqCzTri83Qj453D6)*>FAI318CPDqz`'
        b'H6nTUIU!msA?%Y2&+iO}ujAUb+9Ewg8mFzbL<yz~+)o$jugZ0K?rm|F<>`nx6I@*?W$Y<ZUSL5&{$8IZje@bWa?ax6a!ffw9*w~y'
        b'W%C)OoIyicxasl?)na)Lt5%+MqBB&akl_k>PUlK~Zf2Yz>jKloh|@s#6*j(YwhXg#4f&=q`GyJE=bLBbQzADdZZixI8xll%$<;&5'
        b'H@NGVVJ-U7(Kk(YM$0hnM(2Ire9dI1vp!k-#$zB-?$1>66LJO-2)+yDxt=|*o9uL!OnPG@`J=Nb<q3bKoL53JNe-LriZ1+V<qu(a'
        b'TnDxMO_Jx>lFo7SKf-O<2yP?gm(I_W=<=oJm(JE~O7N|mPi;l#Zf1PMa&#ih#fkhRmtzy$&Lj4_$z`N+?0_4cyUY3@*^N4HE>a;m'
        b'Bv~Jxy6uwcW0bc0pZ2HzcFi){_xX(W*HJ#&e^6Nxa_)%4(YHk;m+$Dsl~!imUv>22p(-|Qs4Dk!0(X}&_QGc>tOnlotG>hJS;w3d'
        b'Ih*RQUFT*_aqG~zWv94x>fCZt+&1X^=cl-ZboT{P?+rwByfG<mQJq^}id$UgHa5j=i!QD+Qrzy=xm}V;{;4tZJ?S*Lry2ZBOR=9h'
        b'g1_Pv`&lFSo1J1W(EZi_QUxE38^K@ddE}WR_;aM#i$?J0{J-QLyV^H4j?diYnSR6a?C)?&Ul`Ew&d`m6VR?SknpDSHzZuraqt)tG'
        b'>o3DPIZIldYW-w5Wt{43TOHFiH6E|j{CTBwdD(&m(|a8^4Y7k;E?f8bz_P{@H@xcIx56-cS)X<OYlm+B`Mw1_0KIgiw^l-Lq#-5F'
        b'f9SVsAJ6LUYe*ibu_aLl|AIJ=$T$uE!Z?doh`F((c&IAjHUVpJC$sOhGy5jH970bS5`9CRtn~7QI}x7VRg`vN&rE$`iP=Kuo)0!@'
        b'XIe{^8PepCV96Gl(+!{9-E(4rwojIGQ+F^#h^=%_JS^2WdmKueKiXbWOHzAP)y}X5qW)-GCuv?#NK1Dxw369o*?NO9wv0o`asgKh'
        b'rfX%0^c$}341^R~50+dR2t=@H2zU9Bh)_o!4k_(nQlm&JzH7R|;r5bx5|r-25}d^Q2>C}Ps<j=fajto;#J#khaqST$HGx38(i!e*'
        b'FR5PB20#34Xo<()5s0thk(b!HOj03UvZRq85=IeX@o=QX>7l>wXt<TD$HT%n#1&kX)Q3qp7ncz%&8z)U(#Tj+7witkV_Z#E6ctn='
        b'w1X;Cy+Sd2ti+2lB5QO6mAr8+-(6e>-fE?TvYQA@x}Mf3v2aHmRZ8)eG|aJ;@V1C?Iq^z75mypB!n0g1vkqHaR19;98WW(zMCSZx'
        b'4@K&Vj+NAgyGaug>R#%PqEoV5$WVzV5LdeWXyg#uCK_BxI>5r%On6r#WiH@65L05Eeo|J8je-&kMS9{TqGX7?$KO@bD9fgZx}fqj'
        b'#{!~wi8xB!s2iRus*fnTLad~zN6S#GEgFnaEr(D&$Y`g?GVM>ekWj|Ut*dBR5$M#lw;1eM|AzT~M;q2cB^Zk^uZ@VYmo;msiq6q*'
        b'=+(v|<z*tBmtQA%^!(fOd10ot7QNqn<}R~^#&)|z?_FB>N}s{b{(tbxVd9=puDrM5Kb3r*|K(-eDes(&_A~x3EaN${jFaS=Z}}<w'
        b'oBo%Vk=F5#oWlRf(xIw3ry2LMEoRI36yC-^80<Sh`$5wTS@u5lB}IX*qZm&uGfQ2k(Ac@NY^bVS-k18QqOlGktQuER`&otTWYsOP'
        b'E^0BfuuenEsn&F<;ZB9;OPVZ6Up|9&TQH%IeB}62fB(dK?&IIbzmI<(|33bG{QLO#@$ci`$G?w%|4;lf?<<mdCl6Fu3-c?j3aA8R'
        b'1-0Z=T5C;N_S!+Cz3vMYRtxAzuhE_h`;PmK_I8j0Dp_N+bAM7V(3Y<n?Z@sj+IN4&XwQPV4z%Nr3hN%w0nj1P5m4dhE3B2E7SKk}'
        b'eV?cI*W&k9o=E@LcZ_y@zIRp)RqeiNsLJXds<Jc<RXyY#s@l^yR8<1p?is3@ca?lkjg9dC>i_sn8Wi<GXpm@>Xp)#E(JV1rVvfXI'
        b'iDM+@NgOLNU*Z`O&y;wU!~%)qB%UpCyu?C@6C_TQc#gzL63>-*p2YJdPL_Cq#0w=}BvFw#MdDP67fYNbak|7A5@$**l2|P95{Z{e'
        b'ERi@%;%td?B$i4nlUOcsuEco~FOxW5Vui#?iI+=UAn_9tEfN<>TqKb?vHQjf>&Nu}E;*?Gf!-X)tP5W;TZq*6M^}t8-;d_D=TAZg'
        b'7R{}x?~}H?Bi`TNCvi~Xc8NPAJ|uCc#9i;G-vu(ipGtk!(46oVo+U5zS6H`i!E*xSzT0S@_T>s|zjLUn^nnWN3eZvTc7nIpDdzOa'
        b'H3I+9ce7jW$1@1D43rDn`_&5TF3=>Hx8JWldy;;r|3lL4zzBY<XCOyo7P7%FEMj|Sj$z8y92P-dYu~7_c7Zm4c7t99y#>n3&ZT2{'
        b'EcacQ->$Is;aNNQPK9+psPb>{L(k!(71lwR4;?qzd(W)2PKI0736p&n%q8z(Ui=H@PGJ0uN}i`>Fh@XjM@J|Je$!)0hd<aAXkVac'
        b'O7%*6r}r|YXnL%eb--<bGIe@vs?tTD(x$iPkrs^w%Jf)Xpf?f?#A3m4h+EbB0F6z)>RM;@l`O)w8Ix-CGR0z1%I6oes;bn}d7b{Q'
        b'Ia20s;t(bA=)@kW8uoQ{&F*BRhLLfFsbi)`kQf)2gH(Hw%Sdq^sq*Wf!+5?(INY^Bspo1wmF}KcTxliMD#4YZK)ceqMw#A&zwtn9'
        b'_DEs4VpKI?YaqTl5C~Byf2ds_xJ~FqPiUIu-;tFze<&1=E1mvTNK^^+bag3Q*UZ#WG^<iJX16h+#3vpmRk%gm!q15EtZTev4<!n}'
        b'&cUU16!WZbzCw9W%N&V@(GFe6f`}j}6wj(jXn|s#;hwH`DmA%JWm7Wv=W3E<P!X0GN>T)rcp?%Jit02|1Pi4=rleS?{<XZ23d^Ys'
        b'{cIKYNCuuCrGu2UP=%`rQf*IVJSH{DQGN2}Z{s?xN9-{1u)fV>UA}IAM5^(L2cq=t9RnsDRc0x%KwB6+q${v0(518n<K!_IlS!r4'
        b'LNSS=;<B7h(I#qs^pz=lfY7iL46Pikn`oZWyGp`MId!MeXMG`wqN1Qehw!C}1mP21x*da-js=iWA6}PZ6kl`jbq7QGei-Qr#+B8<'
        b'c&DN&OCn#HJEXp{R0T@i{^)fmgFhy#EvfS;k<K+Se(*yCLbsTy>lDdJP=I1Bs0cx=imKvWD~^7;vQw90tf#G0pHotDni5Sg+!ISp'
        b'oV=y<-BV;VB?(<+jGo4n)9i6V@2%`i(O|ca&%k`lsG6*WBc|w;0iixkF#N5taI`ham9iwl@+n+4J+-qw1@0CL(8(NMtS1=f+P}EF'
        b'^hLT>;{o9hoe6!6o28#%C>Dsu^&BZHiR-vtfRc5^gItO9?6w8d+m-e}oF9-;{QQAeTG@*cPKP#V<Yb<&^-(0L3}>24LSc8XJJOZR'
        b'mxs-{gTFN#jTaRwtI=slznjR1yBb+xT$>UdIARvA@vL1@RmUx2xy&D<aweYIYyqCsOy-=#%i)QvUI?JyD7vw_16=u6XE+x33AueJ'
        b'mKw#SQgs)Jp3@@J2f-w<lC+GI8nPq@p{q-@K{_8ZWjstrQJMGmSjYZRtaYYg&C(A#0HU={EwBLVn)W|eSZS@({}$FwFw<Hm4(xxk'
        b'!s`9AwysgvI%KYN4^>&Q);dJt&aSlHc^2X<th6qhP-)!{65pZ?Y~OgSu_jigt&R2+R9frCRaz^_4U6kH5l8MhmDXnvN2E~rKMJ=)'
        b'@UsbV6v3S#js2k3@EU#`WRJ|lw6l`)pj=dG-Eq;W^Dyl~k%v7OCg;I{cyiCmoQJhC4=dXlX*U<j)#QPyDGN`b$WT+1#<i<SozOy4'
        b'S_TKMGA=0vto^SNWq!Tz-&gM&&yi)8I;`h4i9A$J`q$=R8RF}jG(sLGi97_c7AE)IG7tU#raWwi+e0!B-My%UqF~t99c~ZEYexy$'
        b'AtWrSshF!k9MOjZK2E=zP;$O7SNoUN<pS-p(~S@&Ll+v&XS+Y{_lY^lcSAVb&6wg9^?cw0t)7*0Q6Hev^R#;20{2~$GS_q0`50s8'
        b'CD-#&_%9-wTxmTxIk}$S0^f4JsAr`Jc`L>qSmxv81^>Q&Klwt@-tkVxike0G^OS$>Tr*nwb&5!TbuiS5g)dWej*q5m9FOMf+k>mP'
        b'Hq24gN%GAgaj*l#dQsl;l5<fK4^NZ0+GF_hhVFGl=&;(4T?H??l*6vlcU@d?^+)~vcuc{IW0b>VO5YvBg-F+$j`UfTH%v<9JnP(2'
        b'>n}`wbH|lVEmhtaU!bt}<3ES%?|W<U_m)x~e#pgsF{a?xF69rd(hpqLK9{@S)iUUc>^#lv3?c9s<qu;bzZg^c!5HhUW88O*Y5Dq?'
        b'$ah6{PWgM5r~g}*@@H4+hc2tt<#xMTT3nHctFO=1-|re6bnP51FV7<I80F7nb|U=`$5^i%<GyB0%XMQSpB~fqxiS6sjv4&cn4RAr'
        b'B`?p9zuEiG9A5q9c=I*?O!ybZJ2(F`2lieZZyuZdPlSJIyxIKEg#Xp}n@#^r_+N}SA2<C|;eY)8|G@)~RvR-88rhrUfBdSME2aL3'
        b'zxnIv-QrD5Su#{b=jrC%2DGvk{vic_a&I20%AGb;RRH&c)0zF3^{oXKgV}OtJ)>_+h+*&WiWx&yj_E^HduK8G%a<GN{A?g5(iJm@'
        b's<vDr?l=^{jSk5o&YN~3u7^M`!+ke!A7~fI0;&XU2OS+pS6=uX4-n!zWNcY`%}`ZjDSwa2d0pIWM4TTE_kDrROlQG-V)z;O+kXwY'
        b'4chhsi*6mNs&g@W!H-S$mXjv?G~{s;XyXE-z0+v0Pg^lm<@X_O`0Kir!ez5(K8rH94pklVV|@(T6Bw%cUMroE9R4f*4b!ut@NH(_'
        b'awpPNu$F<_TL|lz&(CgKOS%va^cHB|DwOpDW`7HQw_FcC=vV~l7!VSrd<gu5oy@)i{FC4p#mtr&F(DtK6m{kfF#EB!2D^je30GK4'
        b'LA5X+`45A=c9+3^C(K(w_k!*Q9eot(>@?V)E*q*+nAx&y%}~{g511|1?PkkZ(1qK%Oo|q%xV;Z$qEA*4`E~P$Ak*u^Kc}+30(zg{'
        b'Ou_$+i04gyPL#fo9UIOnM>$}p^O*Tc0XqQqwQf_375qamzW_Q2@}AGEk>y7F?5~?Gi$GIA8(^=6Kkv27+5+kVS?y;r>v^b=UHh_r'
        b'2S4RI%$7pXq#Mu&K@4;Z@f85?YcbkOf%AxuXW79+`7JMlu7uqMss;6b!)#G<n04oyCi^q+zpo8_Gn-lI{^D+|1<-_UB06MC^@Kw0'
        b'J2WxdLSGQO%BdgZx2))`u(lwsjeRsGUKw6%X8fDNWaM+#BxWrF?geiDtI1w?F0<}IT3zp&?8;G-Js0Q(&+9kZH?$h<kx$b1*x?WB'
        b'5#Mz5)t&Tx0&~Y+lyN`EYhx|TKr28kpmtCvXi|%@<&i4NV}1*2UYQ1TfU*duGwXdQQy22E0d&Ng-*OV<Mj9(X%Lv0pyW?*r`&*!s'
        b'L8JXzs+$hf--IkX>onT?cv;yGhWWkaA+$fAQ1=cG!m1p(fA}KCj@(qS_s~r_@SbHqfI6U$;6;y`EzJ*^Efv5|fUW>71I<6rY>B{M'
        b'gwjFWM}bGE?WnCjJyewi+5!F+&}5jWp)R)Ak=M_nZ-2*ZIr<sQC5zBLFi)W|U6IYUScj@wZl!OS^suXBxf|&_Cd?c67R{qL=}u~2'
        b'#opnYvRVE<v*n&2n=OlhCy{Rta5d<*ebmNb_88n=jvDPpkOu#tQpngk@L1peAKnc=Hkf|}bOXnM=73g$E(D!KnEUpdEl&@bE&G7a'
        b'fbNHR*0^lTW5D-de;GJ;U%~e`+%!~G3OazXMBn1~_hEipW3)eWgV7#GyX`=GO<FfpbuLH&-3R+H>iEK6nk_9am@Ngs9aTeBHNa~?'
        b'o4$a(J@EbK&6fWF()XV_^y>pK&w>9pf%HA71?|t=`7I@gbH%y*>Y%+7ID9`>kGC@mbIRA?|1&R|E#qILIx(;k%y&ibzjGq9D&Td2'
        b'7J%-|W!6%-SukI0at>9ItPqkLVgix8kcW`JdD&U^!h4MNH{n0@65<3MxR_Zl27VGW58*3-4$z*M(S9><KWHcDteK2m)PQ9p@*PL~'
        b'FCcw(kdMVhSt!Rd7)LvicenVCRbWA%uLPaE9d@+&F<>Y9(aY$QM?s}<n+Ixv|7Xx96VJ}J7(u&{hxV_TEnCnpD}QFT41WQmJfE?X'
        b'b6LyFrL5(qBYf_|(~xByLRlY%e=BNk?_S0pf%#F;W1wBcFQvJ&fYotiNBS^-)WSSmb!3?B&0&Dy*U1hBVlX(kzqQOVhFN!`K96D!'
        b'Yw082nV50k9v;33DZe&6ymtffa@juMe@>*?`0vAUKJN^lu#PvfoU!~1reZzBS_)7`H_e}*7MO?sHavU;@t#}<{}&w_Cgm`7G&dpq'
        b'%8rf>b|{A}gWnb89})FayzdVWV;*hs9x$}L@Qk6QzlF6NakG}4;2lG4=j<IG?!=m)4@5Z|zMp2s;hXTcuM4~bn2hofPXVZqmxrBw'
        b'1OB{;J(h7X`txHI)<4!`?uL2tJ0|-);4X}xB8=Cam6#LotX43FOJSdk@qGO*v*n`4&6dCIqV_*BTrgAIt#w~(w9f(m#wYMBK%1?A'
        b'xgB%?%-;fz{XTt{t@_S)V165ZUIe}aD*F%2L!jS+_c`Eyf$pX_zH7FGL3==F?Zy}b?E^mms+`QM9^g*!hCr8m&unqRJ|9>H><4}e'
        b'I2rUL%x3{tU_8BmGI&83A}`<DD`ZhEgxLvt2=>2?L%yFf+7F@pcYd1RA?v#j*bnLj6?CKj1J{BMfY@5B9e@XEt_1A?b%B<FBB0fX'
        b'_j$y7FYqbQ2OtOdXYawh1%7-i+Mntb_8ypPfD6IDjOq{kPEZTT0xAZ758QKstIj~1p3ST;!v4+=&6d|;e;#=DnT-86c;AD$7Um-`'
        b'Zzp${kHdTznENE^2XR~s{0VR?$P05f@VPOJ-3)Vn9%DOzn-KO{)X@Q$e-7+~{UWsWVb~V{&-ek#0p4-U&2wQchxywW6Boh!2rveG'
        b'5qJUke}Fj~7}-~09SdBG^p+vLH&NHeZXBwbggH11#6TxuKZ)my8+Zi%?*5V4G95G<wD08#>rwFM!~8C25oiO*3Hoo)5xD&n_z0*T'
        b'6a~?GfvA+3`RfA(YvTx>fkz)RTOI}O2E7LJpMV`5e98Tv2DZ2E80<yhF9Q{#4e~(_jFIPI?*eTAZ2|oN6d%v5)8PJ1JP%jknLUlx'
        b'3K%2LlD*w%-wDcp&t(4%>?Pp;4R{8Pp}jPvowaw^bcD`CokXjd_F$aW(Yj%8ev1`U3u2%;&@zx4<ON|o9UC705k-)5Kb?Abj*PU?'
        b'IXO%haK7+l`0unjlsD5?Fj|P08e1mOT!iJM17m$D=<3B{eYkbOK{q16tV<JK)!&DQpB|RC=P;`b{~q)Kwg!Law|@Fej8>svK-fD$'
        b'cY|^<cD#SDu&zM6J_7qu+MD3P^%~4dE#_v-GXdcBpjTbkL%cUUTzCb>7WnnR&jUXX{vdESa3y%1Fy9GWL37lVSTlmY2x@};XFwb9'
        b'ec-}6JmX-F11|;+0w)3w0<(epK<|MTHw;xx08ItW0Tsz}cr7rm1??+j)?0vEKr_ZxTJHhw0DTkm5U3etsm0i90bza^-U(i9<51P>'
        b'z*67`z;l4Tm|xq0dp|JQ*(=y16joZd7a$$rE)WTz@xsqDQ<!y`IQKDpS<emZhwh=OysL()-UgD=sZH>EA1M0+JoHXrQ-zk8^1I>T'
        b'moLUd{^#N0w=fR>f_dx7rlG1;9*iT<{g~wsBHrsiKRjFxdmX40Yw6dqb~y>k#k2Yd(1eAy7yK`S)`RBT*t(9BGb?k}1x{|v?OPw4'
        b'(tdKU!fvx)aD>hGvwUOmxF5BioYF$f-6y9$Z<uQQ#Llf*YyY(Kv4X+xE8y-pIn|amxGn3*J>%B?*WkAb`oBrsEhitdW%YkG>(FiE'
        b')_$-5o`Sx+iM#RSHd|KT7qZsgFks6%uyNer-35KODeG-n6PsAy`cfFSjN7{SWPee-zc1c5b)2$M=~sH#)Nz9w3&>p5v)OjCZ>pgm'
        b')*=O2WXS)c3r<d{r2K6>vF+?-ee2AFTgI(_<cEE?7xZtWL<cS{So?hcU0Fx&MtnNnWBpsQz&LdGIPhlWPP~NmT~aFJTzB!w{PW0P'
        b'(M5wi=L4M=QK@pbZD)dUcka52POdMSc_^33Ft*7jAA4ljx?MT^v)qTX;ANQ+e=avpe<gR8S@kns`gw3Dcl{&7s;4c+(v77k6xF=('
        b';jF{I;UUO>j_Us>xl}?pmhuAJW_<A1xuT71!zXrRO{~t&H!n9VJ@1VCMZYyaYkq9deE8G3%TcjehaMYu$)))7#A8$5J8|gy<CO1j'
        b'`|rP<*n0HDZ%t1PvYr273-sj9%KJvv;hLOh^YYJp*!WvR{&j~}=N1_@mFMRj{+*HX&JLmHd^pS|{*k>pXe#}s@~kQUng@GwFVD)K'
        b'Hu0$s^Yf<vE@#`IVcnq<sE~zO?@cx2k1w6Nw+1U7%Hxz@oUr}Z3FLeI)N|JR84Tr9seaeDj<;49*!>31nYixx6Mb_FtaGV^<*gH^'
        b'Ja@uAn451J>*&auKJ{yCrfKYyr%p_rIw|nd@F63+we8F)KY(>|!8j%G3UMwtvfgMsv~gVDy1s!Tq-DBw%#1@D#$B=Tsvn#{cf0-O'
        b'jmzHeJb&w+6D6CTG(PxEw&{=CjBMTaD9=-$I#_dfm~A|Jac|zk#_5CXC&y`W?whOJ!pmS|iW1Lh{p7lDpUA(2nrx%&2OGHsUH|R^'
        b'&6<Bjvg;E`u3Nu)BFPyQr`peHy>{J~WeQs)a|^d5QV`Ze3exq7B-gFCoJexcKToyJZ1t_XQ6{iMGIwxGA^~AdBp_X%NOIj8I-zqO'
        b'D9Te)80gHaKp6rj@{3_B+TA~uxW&7<W$mx~rxs||d{?sT_mW&UH=jsy&OcYRQopyctqmvE4`!iN2Jcax%w6@lo1V&RAG>kpees=W'
        b'>D#6j8MjT!?y%S8-}a+LCmzc!?7vM}wQ=>-d^RvN{M~`;)(>7ZrR2nSi|To&Jd2IB_VsN(^u2NS-23R<69?`FZdu;fm(_nyR^M%<'
        b'1(>P^U+?>-GN>HAul4;unjhRfJh)Anav}9T^t)Ra+xF8#G){PI1ye3MftiKJ`DpeZho5@p;7{<Vr+MYf6PwRGvA(E$>!cGool|K@'
        b'FUQ<Qvx*qj%eNS}J@Ui#V-#@LyD-I(mtc~YV9k3xu5C{h96mlQ>SE%nY}?eVb$Qg2!4G^e+%M*_caCp<=lJ^E{aa5S&v|o7#`Nm)'
        b'cyh`}$=&jv=>Lc}=e3*%|2E9$gXzbIX+FT%-e`Ac9UsV5N=xHwkIf8bm6qA^CzV!~mX>BA$i%;~z>#6f+-t{?Ig+tc_Udu>_~Qla'
        b'(p4<CB4~c_FT=NdFl@51!$--V$-v4lInTQDI3_1dI)hIr4;$CLL}9aK9X@${U@KdH(6B!D+`g%$>z+8C(>jxSV$r}hc24UwVcgDU'
        b'woc*3&HIm6v|h-KynJ_8X1_bk@h1{dLXI`>4<r8dM#ID%EI)Uf(X`%fIDBk)o6(4e!{Hywy54->@vXa#Q$rWioG{3z?e#&nX<*wR'
        b'3p_cTpZDOq!*aeq+?l&DZ`0NJVh)}1_2V0j6LW_H%W{g0UmtjL%J$>=lZuQ=<rim}e)1lreK?RiW$-wrd}W*R;L6<1Up<~r^Zt4l'
        b'+xnH`NEikhetGBLO&QMHd^b4lf!5rIjSu$b$}}H5F}&{1;~R4)7BTT~5_8w|_lK7}!PXB>x^-YI`UmEmS$Py<@)j6xJ^StTPxbZn'
        b'#oya#9vFQ5)?dFm^{GP$wBlg?c{6t#^794<<28T#|2TUSu%@oG0r+lN2p3HPrU-O;b0H9@wjtOOoH}0;5y9mfKt*)w44^@D+KyUU'
        b'ZO56(4J`zuGc2}(AD!MrQ-R6|*r_XD3AWT)oDsV_+EOL#`>s{*f6l$ZWv2i0eE<JEJU3@~&pGdT&wJkGY(PFxqpmTI%E(<POFJkx'
        b'xAqu~x#YYL!Z3CtrEhhUfh3_z%u8Mbxgl+{WI=!~lv=KOfo`>e+NNy&X7=w0W;7a0_l_B9ot2iWlp;%-G-WgFG`oUIc2SyiDb3C_'
        b'WZjB*%RplEZv#ms{VP4GtP@$bOOJ*||N2%nUUgdag@nX`26Jy|LiL&RU5|>*>iMw&L>=yV5m1}<-Ey=s`>iKPan{N$S-zIEw+Q{?'
        b'fpw_v9Hoo4GXD+vDQhVbod^fgfa@~@mtd`3oUOG35aHS0f;gq^@xX#OGPt7bw}C}xvQ{Dq-*coYYo#UO8n;j^zRF!AE)wzv$}%p>'
        b'zrg`RNqimZ3&@`Vw|MdTpzTnGQEfMQNqo<MD9iD&JF9oyw;!0OTmNBm+$$%2pd9jV<wE}dwHK|tWyhgp-2*;}T8i2aev=ZHZ;_Zt'
        b'z?ZgopEf|qL_9@y%a>+|Tk8XSOQp9M?ACz*4158wS&J~DTShk5#<N=5mD|i+0b6Jn1_oD_l<YrnP(lWn6Me)3aE?_=YpcyGe0lpR'
        b'zgv(i%*aj0#7(>OKb5Lu_~xwMWP0vZTp39ElqLG`_7QXaW=IjAaj?Rf<a-|kh6Duow)p7>b;egWsrp>z%1wYS&;GEEOE(=~|8)D8'
        b'Z$7BE_mq^pnU=)yqz*3GzbLKn?$zr8;72zfF6h2jP-r9i#LdRPb(Mu86r0OS4!qtgHt@9Vm}{D2>Tfz7^Y7!&k4#M>OfYz>Hjqlb'
        b'&t#BmVphHY$!n^;38t2rK$q)9d&gjUhglI7uXf$M6tB=?E6i6zodm+X3%jgcOGObZt;?U})PKF{yCzu)#Bh|6y~Vr(vy)}F5VkKk'
        b'>H`fXjzYryQ8F|=K6zbytjLwJ|0XHkCaS};KwWP_;3ip}m??)LSbZ4`WNy4^5XJ6~f(d_t33Ql9XfQQEW;@iOCy@2_r*wxX=2@64'
        b'{(?i=%zMXLr#Xaq4W<~TNZ)6od}$!}RjGHQ_uSNjz@b}E;Z?6?UGdDz5DKUSSVt~j$2ktspSum@j!2hYo~+AFiMt7#{~gS<ueBBt'
        b'Y_%@-pf60@4$~6;ms4d8GC6$yq_;UKqM`=?QZ^8n`7yta*E7-UZ${z<Th(S@BbqUkSqF=dO465YEUzN~iu@P=+xF3$PWq7!8Nvc('
        b'z`kUyRj@SW&4b52=iRJP2mmxHX00y)%Ya5DY{g4dB?u6WD4>y?t<J5lh0X~m3nY-$t^k8-rDuJdoy5)5h=2|eLW<TalQQFOrl(bT'
        b'NNHi3GvfE4;z$jNtymGcOsh%~#XWV~wn5bjobUzqI`P}mmkZ}NMt$aMZ|m<!R}`)5Sf@z+IB;VcFi4yi2IvTXJ&OVhhQyLX%RysM'
        b'8e+Od&0YTD$YlwG+(O)7E-nYDIe5mF=C8W$#x2`m&L4%k%Jlt=Ei3@g#G$&`$Rf5V^hAZfKFpt|Ol4537-^EKzP<Z~&v|V{Vno%b'
        b'Y7Nq&#bc{_RK9mBSCY7PW1KcFF}Ccp!i}IpVSc7um@#VtItYX$mMcvRH<OrNwTSeoOpgo$u4ueg8n@_nOOiCf2U$>PJxP_+P%jq+'
        b'wLJcrZ)Mx<jwHpw_>Opm`J=!UiDICv8b2GLHU6pI{uwo}e+#8{bDEt?G6Sn#=!2O!s0xsz9DSf+Bl81nc&*TI1<*oqiz4GAD*r3V'
        b'z|*zxqO{KE<)ZnG3t+?j|K4y*8*CRgDkGIfXF1TFysUW}(<Y_axTK_f!0<>DUWa)`IEY6kQrbG>D4d~vP@4}T_`S3b1}qE28^%lX'
        b'W*+u?GZA1SM4}!Mq5j*94LeyNiz!n8_3kXPm8BzP3bZU8)oep-4z!>M$`zVcUd1dZqTV^<I64DjjXYgub-~*+jVzQhbg1G4hP6_N'
        b'dh3ki&<wC;;RN@`(t;#5I!-VtT$@2V3#_&BstZ6(EX7?}Ncf6%Hd;yk-0|iN0I)od<ipE*rR6iWPz)el#-i4ma_3S!E%1($4u*4u'
        b'o!Ht3MV;QC_<D0Bz=wR#kv{`4QWpU1jKxX;IVdATm1!q$!RmjT(9IQWzXpIqf?LPo_?7-)2Fw#^wE95pGC$aEwJs_Mngb&+rO>Cg'
        b'hF&4%<!0%N{~utt{oi3JT`mwumKQiSic&2`pp>q|T{+xpnJS3e#lF4?%l!4s?s6=l9*I4HwZ<bM2S7}mhs4G{7hb-OJQ5qbIC~A2'
        b'e-O#e!xDy(>=;a3jM&aWbL^Svf)mnR>|>x{{vfi`I70^6A|i_obvTrRERo-hge-@3Paq)$;5UB{vWxZGUEZu-JhMxQkyz|jEdK<e'
        b'i!g~l067e7_zlqTf9+!b1j4PKLzKjOkp-ZV;?jjPTAwuiZMA2be1xV~+2&(ZII)A)?cIHeR_x$;kKTYK^Z@SN#pc20@<Cmg_%h-$'
        b'BiUE5){hYNSJS03z&6P{LuMd5%_o2pWwa}H&~hv9z0n&8b^G)xUz(OXeBpTK^H;leu@$h7kApzT?iehg8UzX<wmU%!X}eh1Iq_<c'
        b'Xy5IRiBEDV&C_I1>X(>po^*jI*)AtV){S}f>lA6y$kM*)UB^BY8i(vNp8&l8I*6U^gMdZ;0#MsN*op1P?&DbgpFy-3RNl&RI}cCq'
        b'dPJsLA6EJ`pu|HpMM8S)pcT97xYmB24vyH^`83N$#9*y|Kxp=_v5i>k?+{>ye#5o;gM25X^M8ZDVNiK~A-A)1dRN3sRl(03Urm#b'
        b'yXv_F{=L$j`=%YAOxq&ljVzpU%!TRF3)6HWLFXWJ5<;irbVMwm)<U9nDWbMc3$tiz-;m}bPRy@VxXy9Rd(&hAL^lv%$#*lIXdUAi'
        b'_cW+c{o=GUYbhXmKD;NZc1**3C2`>Td+Ke|rO!>%^va!oo2H&1j5d^xTq+D0y=^HSDJO#y_H*Pi@pho64^IQ?0K6il^m2%ndJ`xK'
        b'F;iE9z%#0rNsk%<(bg|G_4?_CDv&5|eT_?5JI!QIg8@sOCnbZxfNjFSfU)c3$zaUR`<4CyjM<+aqI3itvl3b%F5}ek(+%rkMftlp'
        b'wFv~Cpq?aD&UQ!sH0kTA;`HY{zyOfw3d(H>NOH!+66x-@u>424=-g>rsCIXt2zV8M0ufzULLjG(o_4_A%E`we)~`&HqEvG?9U7t1'
        b'f5a0wVJ;vivtfGYj%k6Gt7P}6sivm|k6-*Y2gmpX*Ln~VA58eOoVWr6cg~+C1Dz3OQo<JGS=rpQ)15olPnSJ{kp(*{<<Cs-_FuA#'
        b'{o`)`l?xsL{E#q@E3Vn;12|&U)^1FEkyFd2$$bDhv4KNqF|dNpsYRg4KdM?<;9T+H5CDH?$_wx2)OV*6ia0V*Rfz1Ip0Y)(vgQ+e'
        b'Pj%Q8CF|tYbyWUI@7k4<3b$>xvC;^`B4%_-wTlQ>t}Gp%vPCY1p8vL`Ow@Fl_Gf1!0Udp*lX>-2ZkwLfmLFAi_#k2lpvT<l0_9W8'
        b'lhXxdpD@>^Y=Lhr@A=<W&~rLxDbyi0t*yJKF8?;id^zRRu4G*Vw1b?KxC`*ims2*N`FdtrC!ow`9-G$A`l_Z!r-4OGvxm}&h=a=w'
        b'VKgqgJ?5A{-GsLsCK=BZw77tZkwHm}*NLFy^^bN>*#m5wpVEgKfT<BlsDGT&(?2Jb#r|HK3;}l1LRtQ8uT25uv-<rhAfjn{(OIZg'
        b'7Rrtm*^d3GD36>^%B(ectTnf-LVwPtE6lSRsN(a$eQ$f!F);;~6$gN&?Q(DlV*(vD6P$W%DutaQ39}iYHS`i0aQZ==jv-*Wx?bQ+'
        b'Z%xrGXA9ULQ4y>@KP4#Mwz2FR%V<p~8BEIHDEc8t_|iq7b<7%>2lPyu@~-}zRTr6;X1f!8b*c#ioVAT>3D^%qnhZ|;cUY0rEPixE'
        b'&vLM$Td{#6^B1U-2qA;>`vlz7|C}<ksFo_CUzw`I^r7K^8YHeaBYGN3yD?XvH7EM~RHDBfkN#w;U_aKn4@tUSy~rGjED!QEJvZgt'
        b'jF`hTzyLB_Puy$>O`;Q9V)tYDp-35q+i;z=M&~r61@keR8L!%6CZ5*gPb2Z6NK9yKfYfmu(#rKM2g-&Tw%7vZ$LUFb&~)_QrjlB8'
        b'2Dwf*QM@$zwJF=0xs74Is?QKd&6Jr%JQ<v!CF!`HCL2R#sxye=FrcgJH!$%~VvFH&YyfG{>!M9@jd9MnvN#)w$6W?Zw46WwsZw=2'
        b'!1+<Y+ZdVnvVHDJS=pzz5z<&+UwW$0dEvJGoJtzd7%Fjw&4DIAihy3JZVX3nhIBNC%CiF&o1UC<hAjs&RI>dE63QI&X1O`^ac5{$'
        b'(&y&Tg*E5Qo9FVt3TNm78*8=3Q#ChuFh#X3(OjWlQCnjprAJPMl+-rY*qj({4vhjDdGBp9m_1uwf7lAdz~-pxvcyyXS$5>q&mdeG'
        b'fFmCVmOf~z-cEUePak$}e!M#C==MY>fOUFdoe*{<54+%D*ag*%iMs$~BZNHIT-gZ5h}>6S2_P2&NHS>ek0tMw*X}RdywGOGtVZ7D'
        b'^e0Z_NcFg{ZjoGX#td}YIk9@_ltBqCe*ZXSs|s->Oofp9-e)9m+9mvrvwyBSIdC$sx)Vn0ImGi%F0rNReH-yqRZexMIY_*G%Usjq'
        b'DQ0N$<VM>T|HLc2`J9A<;cJPztp0k^p`3zpb|r7h`NqW2s^c@Qx1qgD=_aPLLUwPKJLXO4kNt@Z*3ojnLZ1KPqQj^3{s@Qy5LG#v'
        b'88&5_n#@um^x9-nv=x_m&T!$kFwa^rFM&8Kz%7|glVx9FW%H#4J{uU(lug>5CWV5+7C@B#I4NwZ*wzxvu}OZ(aIK^V6UQT#6Pzjt'
        b')tunMFZgDK%N;$FjjXXl3`}-L2D_iLF-s+0o-HAR1af5JQ(J*`7Kdc^O;XPi#&wG1GzxgcD4CFDLNco+tI@3RKv2Q*&6KdQQx-tz'
        b'>^kdTh^%A7&2~iwzttt+a^fdo{#5cX%=({z`H+1W#`N8!F-D#oLxK6F`h3WAYBDuUTl`cV1_WTl4J`iyPW|$vqhWGZ**QL(Byr6<'
        b'oche99;m#q2$iiL%A=z|fIuP~nOx-yx*-0D>)yN=HW4Pz%$`h}L0yMA8>=mlsQ?tPPaIW~04$63%Zjgr4md&r8Ya}ivI!r;x>)O0'
        b'T)RmOs>lkHXRDMhmdh?8GuKQu$v_PW!vMzd7I3~j6em8;J+j#^bJZld52BDi**eIP34qqEN4ZVn{P(<TMDdfQ?@l_kAvHdwu1SY$'
        b'vMeXWrZqrA>Cj}2V27IyPYSCmT7vWqrU6?mUQEt|8wSKeU!5jz2}WPAQNJn&^g7}H+my;lD4a!bY4k){nEJqE7KWU7D@v`Ibd&&!'
        b'Ny7D*<Iey`mkN%8a~ZM_F3A`O-x#>7M*u~m-Zx2ONb#7XXwnkk1%gWz2<Sx<rt#+%iu0k~K-8~JYB65%<PQn`iGF30S82g;y{Hh6'
        b'$oiG~C75Ev5McEWNK0RwEb~DI3K?wD@!X_+Pq+bd{1&h%;_~AgG7F9oVmr_A6+Ajpx^=SA2Pyt-lhlztnLo)nER!A?2LhmdX8mLx'
        b'CalpVj0$V$znLtPB1e<pN*YqSY0}A-v_Cs}u$GjPg)bM*DLM^mZSh5}oNQT%1lxh8l2Sl9T65F1BA_MH&I2ltH%WVJ9HwJTBX&jf'
        b'>dB%;vMS<#d`XN3MYOygF2j+M!=}p@)*pEWyL>@cQnKi>8F7BP{=hSs^HZo#f@2=1#bX?a32V!lNE5aID?@c#8|SpgO}ZCPHaeF('
        b';wC+B`y6QWYd1`~p8_d~`Ow~Fo|<$#4M{emg+rd>j+u;9%&unEz_jWd^3i5~GrA@RM(yqelRrE$*<34kM@@P&>_SEaOs)4OktAQZ'
        b'iPSZfQ)keQTKOro{xr-x#n-c^;b)V+F&Qx^5Y4*9Fg*^onH2a*C6@3DB>Is_1FpyCFJ5N6ng`O)=a>Q}b=Od1oBUE6g#I+gH)ioV'
        b'$V+?7$C{Iq*TOlx2Ig#l^%!zUf}H1&PG+plOJ0Yv`~-)M<SbW-vRb(eBV5unRAe1RGGgS$%`k5p+~wPqqk;>$IV4Wb%RD<#vL?^C'
        b'4$X*{C&xpOq@39KBK@bFP6vx8R;M0ClH=vNMSRt856>Vqy*1(8dd=b2fus@R(*{V>n_9koIF%rVv{n`Vso&mlWWEt8ca)R^D_!p0'
        b'`!eL1z5$iUXW{uSdgFUqKjHU_F0)8-a&BrSq8q1-9l00%n*6}L)pT%hkp!-9k|A$2pQW7aJDNKj^T`AfrLfX+*7_3gN0^T$thI9X'
        b'-ntm$o}d~jrxvmNOj5$1o6kh_nTVxb>^L*gc#N}rE^bjH(I+O}dJd_^n=s29i8B;=D;_@|)L~O}R4JnD7b;K6>MIq%WIkvw+ShPw'
        b'qB&l{FY#ja@5@a`CyYt*dVzx4iy}~ipQIYUC<XyJ3`ju0Uvl0JEB6FS>M++7XZcj@sG6Wz#PYq^i>KwhIP)MxDC1p9b3r^}0}ZPW'
        b'OaQ&G(O#kKfE$+PkGO2Y$MvzePVD&?D5u3&LP--TU1?9?*Q)9;jY{IJuMYD(IvaN6Pb`3I5_VaLFLf#p7yt|5LU^Ifo3H-U1eIl^'
        b'D8d`p=nyuF@_?`N@}(jLYi};yJyBAvu+}zTjzpN3CPr!%Bv#)C#oc*nGp)PyS@V%+hEDNqNGa{?8HwoUV26NRtyOx?iraS8;g(B$'
        b'e{D)c(lgJlEavx~r8XKX@Dbbf)n>Q?oeG=)!7kUF5J&&YTZQMOxTGI1d7EH1OsLmSl-R8uNs3e{vVzuP#q%`ld{S97H4#bfgo|eV'
        b'GA4N<nU=4xM@n6dVqh$vpQW>>L99-g@a~@-7uWaW^-V<SvWbp;3Tvg6F-=taoVEkWmllb5e(6)jB0&6EJTlAQ#9-t;67&4mmPI>+'
        b'{W{N4adeCqL)YKLcI8=ZSs=2vkFAuKr6VV$C1=q3lhIo2t$kQE#=4iWtcZDh0xp2n0IXaeib+g7$RT#@q_pFVB7yI?wI8>>K>%<{'
        b'R8aON>sZD-21`Ii0rzot$y_dR^gP%opyv_Lrm9B-8s)dw`9|$neM7E25IGat_D#ED!mXHaC?^`7Bd(P`71EMQw4@^XL?tXD+4c*2'
        b'dRoQZxBds$V&rq6Nq`>CqxX&&_UP|oz@uQ+c<}>W0VqO@xN!i~I>~*t@{Wy0sD7MUNPs!UT163o-?{z=QoKP7h$J3?eCawU-Z?%F'
        b'5Z-ZwvQ&wIKGo@RjmBIs$ulx?2gTP!7l|eu3<%Rd&TqR|4v6a{uDaPVbG;?byfMD_$2zg4;-S()!8(lj4wlpG2Q$M`D~yq)T<rJ?'
        b'wyAmZ-y7VqBlnJEwpCF0pRll{MC`aQZh3dMO{NW|sy`j4qHME!L(C^I&Bp#x-8z0m>&u+uLEHie$k+Abx+O%cQr`aIxckF#$A{w!'
        b'`hm@=S>(gCK+u%4<I!iwJ7@*9&Pv5tof-t<_Zkr%glQsucwYih<=zE;544Ly;Wr64HH=5agU}wrbW8{(5^bGK-S{;k%3du6eIP6g'
        b'2|!t3TV)5-nvRSE@kzy7s|hGKU5^t99^R)uG*0@=?sUPq$&S-3VP9Gt2oUq7_2+J9V<Q@oNb{6;AFLAOqhQ(sd-rXKyznJ`$skK1'
        b'M*2Eg%wxxxl5t)FF@N#?{u%z#i6~RXml3{2-o)raK7d1usw!3B8X#oVuZ<Vcy!itO?PRwwuft;b<IoRq>>hW$50NMlSOXp*dIJU>'
        b'e;jx39VdO+wr0=(NC;1rJAOaze#M){*Wpl&FCZIPDP!Xi;lGYu-n2jQ9g;DB<n#D%agb$*Q!f~g-ael4+&HyV9=&Z`y?uP~BAsrs'
        b'<B%ds(|8zR&omq9W{R3*cEKX93n;S_20Rs*=l3#Z4PV>yLTxTzpPkQ+n<YqbfM*+KT0Tw&*1?lZws?fe=9vkVexUt^4DuZ2nACCM'
        b'(2ev+;bQ)G_8b`>;f2cm=)J=?-dykDo3b3lVH(c@G}OWBp(RN0mLP!w<BUz01NFizgjuS2cOhQ6%rZW<c#@pk{^YoO!T8`@xTwGw'
        b'`F{M@1K(fp?Ed(84R%V&1i?sj<hUskj;R(m3I}s=W**Ei`HhoG66yy!o<GZFLYBZ|Y&6P`eU^9Z^$N9UeDVFU_kx0NDvvb)2kZb!'
        b'B=fb?-YoQ9P5087nK8&RT|j_d#}QJL)*<mjmF=9;ZS*lA?MX-%?xRND$9)utJE<je?&VDRvI96WgkzcWU<n^l6@ql)Ch<5z$dOKe'
        b'az{S==Yhny6lv3u8419HNyah*kS}nbXp|d6y8NF<-+UZ-{cT*T1`(+OdEZ|e9cYqM2!N3<0%fPiSnoZ(y|-L88R-Y-qth*SeIxOl'
        b'$LK>n)M=-CXskVAjH<OUx5otbcFR3;q!%&pOD-XOHMb-eF>*DG1zT=P$Y5ChQ7QbYrRt8ceGUVrRmQ35Ox)rt-RE#Az{m5LRDETv'
        b'4&}2@IurHyNb69~T=3ESObQtOI&2I0tsU^!`~4n%js3WBH9=ye|0c}1Ca+GU*~`_5EU$7YpNu^N8Ld#1(mE#me(e4I$oqTF``aS?'
        b'GVZYy_ZZKc$@du*NQkDfl%}6bKQ*>W^b^VNkCB>xPX_G%W%4Y$yL|DKqp-qAQN(^fpm=t0b%bjNC+0Y~sHp)_%<}@&mA~WH!J)n5'
        b'8sm>jl9<&RA5jsYc8=|ZhX;TX45X-d=*ZkVJ1USQni(tJ59A@eRNzw}!&GKY{pJ{G!80zo%%UyMbmRLJu)w~TkV{$)*OS3@nB_ZQ'
        b'?r9Ks_C_o<FGUhYyuPY^jGPbb3Z`HzQpz9SDU^<wygDY29}XM*LRrV~QT{8OXRyMc`VV9Ge8J*GX0HIfg^7g$xLYo)Yx1+q6N9D|'
        b'A)a@j#iLn-&f0i)Ifx?j!r1-u9-iAA=?l`fJ(%`0u_JrTv*@1v^r+a8H3syS>oKulPeWgEtn@cyMYe)dQOvK$N`K7<A1mE7=J@s4'
        b'!7?)Nz-hnIXU7iG;1h8Qv$2R3nwn%_!W}O?){m90hlS$ARLLSTu=rahd8{;LtcWH9BTk{D)GC;!f?ZquBD30yAhU|^@9a9RjYjn}'
        b'R(5_Q4y*97ou8<rtEDwc&rRSyMg*xM4*9B0V^oY>oj*#&P|kCAEEB+^pl0jNM5t5>7zw~^>6(Y-M<Ok(Tz8zRLz$JMP;JDFH4&a^'
        b'?j-uv8AScW7<ERj&K;%BQ1oYa^lDVKU*dRtj0uMbK}+Td7;tFE7#arPX@n>ks8*2vo)PZo!D{rY(}?;}F!$x^tWm0#a$dM&>E}p1'
        b'_TU_CH0fWwi>3qUmH}#U-a-+nN>{5yvZF6L=8XX^a}9I!G0qVH5gLLAJsfk#E&}(0k-{btpb)G>;bPekz&4{+$Lewc&MD|v@)>!`'
        b'^3mioRO)AUb^)Bfz#Vr-nVYbC$u5dPd7OV7WhP-torJkF${Po1W7BCdGwJGuxa##8$J8jWIJ&un?>WRVItu(75z`0Z#FHEVcyUVn'
        b'71Y~+c#SL~cTmhBn7PlrvH^%63M0uT6ikZVSzk`z(dZka^|V4qTlFlMm%L399J7+n&KsQ_cgvK>@vqTKv;vy$wN}rxNU&pCu(_pQ'
        b'jW#zE9cLA%YwWVCfrVL-vYK6OYpSu6O3NGso~-M^zEM^O9$6y!`e0bK^vM4{R=uY%t7ccE%-IrHvnTD)ozs;DpNR6$;UfMUviu3I'
        b'Iwx%-SCbW)V>=&MxU1EBzELwIa-4=ZMAdq5v2eDUIXMb!WMKPVM4PZk)RQB!quGHXzycP(**Rn(kmzHhbSPpAMX4w&>3>9zl6cXX'
        b'(=p!jMKz=33jSD+Eiza*RB785%p4w_U6Yyh<K7u1eLbrr#>Y|iunG9M^@~jR=+h}msT>71vPjb<Vk$;2#Vb}MMiOxWiGkl3Dx~MN'
        b'UoR3Ze_Qg&DWc?4>Kc(vV&Q%g$G%bWam{Lpr9)IFa!t*iLBDUA6^xSep=}0NcghzEdom8h=9U*KY;Ij4N+!moBxP>cxs7?Hv`}4~'
        b'O4<w6+5RGE^h$964ez+)NRR*P6DYhB{ra~*A|hV|Sq5({_u$z^EdO7~RP%6na%Z^Q^AifYK~UJAjzWDM0&2pc5*D;}J5<HL83o$c'
        b'5Uq138B97*ssT?ijshi|4DSV(P(3*Ki(Wq}NO2=wqBFCJggleFL?9ol@9FM_d%9bP{8XBN7mtM~0H+%8pX(76mz2*zFkEFtux3t&'
        b';0WfgYw&+P1Xs4BN_X?#5sE4YNWy;Szk?tNr3mu>)<f78&`tD-Q6CiaaRZau+!2`)mzlJ4EK@0x;i`ZBh-ycT9XKLlf$$F>6+8_p'
        b'l+|K%OJW=rg6U{mw0blu2B9W^1~Yc}>z-n@_)Q#iAmTBb$~MOgeD2q<)>tGZa1@ExnNtzOxGZ@sYgVG^A|#$Nr=nUK(Jk9Z-#%{r'
        b'#f><u1bmdZ8S^*ep=Kh+ELv(7uQ5wDo24(Bee%q*a<lItGkM(Xcg{TLbMxFAX8E{T(fSyY9kUnFf%0<jQBvST>%d2E1RrxU_@ril'
        b'Pu33b*<}SETM77-vEbvZ2cO1E;M39pK9@(p=Q<L7BW_F{eM6rmr{Gr+X1N&Fbunz~HF(ve#TwReEi7{|?D}BX<~w1XcUn14^-n+j'
        b'W2ou-5lJ5GE)t{D{|0d1GUHM(^yyD-47+{Yfa!Y14N6__IF4cd7#@ldF_>s6CSHR{He=EkF`qn4R*v}|!pP&8-#Ki~=h)mEn0y@b'
        b'_79XtV0m=hK<lt^gI<S^8_YUl+>ojhjT^Fb;&H<+on+i#(@Dn-Wjdd6gHtCPH#F*e#|<qyzj4E5-JEg5b=}-?!<bG!uBYWX1^6m-'
        b'%JDGG#jtlThDFTwkG&SA9t?91hK1e<I}H0brdFmii8~FMv|1$klA|BPBv>Cp%Yiw(t@ITK;L+=uie(&@Q@Y1-SuMY=R^*Ryq!G-*'
        b'WoOZcc<^BcME^X3Wg>EvLfZXbzlfnFBMATW3)PA1uH&XRMs&0sSox~U1OPYa;FL28Q_i$`#0cgaQQ~U`0BO6p;CSN=|B!LxgwYt&'
        b'+}w{hUnH7iN=$zkF~-y<;tRz&{$T!zdx2DK?dFz!hCP5&3&g1r;&d6}v~w1x%l^wg!qDG6jMH-u;B@&xoEmY{FaB>hrT-*Oq81Fu'
        b'ffgtS8fWEzT>l{L&OtnnLp(o+c&?bm^K<`?Phn`{!+0)x0ME}K#Pc|A3i!X_`NU7+`T7Zn=Q)Vy@q2j2AotcH$big<k<Zp3{zfF;'
        b'(GjEQSf^P0as@^P3%aHbGtO!oSGO1##C{v$diVK2=J{c3o1FQ27$~2UlKO+qRfVLg_~+02um>qdIkLFAY&(+G%DK9+v~12s^B$%)'
        b'q~NtfCCIEzC>ya$+q6(;RO~4(tS}s)iHgJn^q}3If0GmJt(32Ze9g<BS|HgxkNjwPUKkl>jG=x`@BIi+LJV(AKXPM)BvPh__lP>y'
        b'D%uKy<Fglykh0b=<oxcoXZ952-{LlI%@J?K$Ll1YqMCP5U9J2)8hfx)viT)@Y-ZnZY5(wcdqG^z%B&`F9a)KLrX>}qYQ=4J=WuO)'
        b')b_2X{Mv5}yKf9X^DD=VVb^@A`o?gSHsX|T`}JY>cf-&87Gla$0mWtQ-wnI33_tVxgh|e74JfW?|JShltKnz%C5&?FE5lJyHP}ig'
        b'G-!b5OnOEns-UU-9|fBMSdh@}9)(BO+pZKhy8k)MFFO4Ll6E1%+d$E6!}?Gp8=u?o*)Uv|yv?zTsf9p)HheN1aU5%Cg{htan3}fz'
        b'u1bH`^v|I>3>bg?+!9&ZiaYKPhnomc=P6jHSlGW&UB;Nx!=<&u(5x2GEw^bJ*v^(NuI)<u--q3QA9frWZgk{WWYX$an=noP>{{_A'
        b'tgQ@GhHJWb3$5)qFxGyA`!Bqat==;fs~=S#9?sl9OlhnUPpj#VVa?<t5bqA|d0AQz(f-b``yEhuk>k(97D5UvOV4*4yPZlqjkH$`'
        b'yDLFfdBO~*c@0=G@+13~IKw5nb5xVa(k+2^24?<%0UH-C`CfxWQw7abzubhSJ%Rv;&m~u*+6#x>c2Gw{0z4iL&()7}?77X!f2WLx'
        b'DJEk`FlIf&+(JV9PfqX|;7Xrn4D_h2ulSt%RX{Fikv~6t-?pO6lzRIx=t?%GaBmxihCgAs%?URk5cihh*hUO|!PpV5L6Drb@vbWL'
        b'Zpw2*P54C-XxK6U6J>WGjHnK0(uVKfN71D^by+qNyZRKMtk`l1Ko%EW6a&NgD#W(!I>2eY7pKGra5AkKhO4}UCP`$++D-x&b`IVa'
        b'Wa*MPvk-XW?^mJ{ejcS`121{j5!pdv?==!YKgcmZa_Lyxm+j_Z_tIg<(&0vyvGhxzZMKF85BeNF^+hc@o0=WZ+iO2aNZ*TSo#+&5'
        b'Nyh=9g3?~Rt5+kcHNde%Tp64%O$LxSwWwT2Wwd%Y$k>3)+3_+<3eHAR3DD`Z#Ns@k0Nm5ABkd8x?ucQB28`8Ho*NRuUbd_RZ5y04'
        b'lGcZ`tB2j{VMhqS?6l_xNqrYyU%yE88JfKm(|jWVu7JFOibE}O+>XWu0-m&_17|0Dsn~T3gExz=`CjyOUBeP?@#l1<!@@mC&C?=1'
        b'jZ}ROz`w;d$%?PE`wY8f!wwv@@>|QlBz3rJ9likr!?=9b-X%kT-HZY6Yc{@$kN4e+hd{U3a?fWWSMl+l*?1$1!Z|($uT&v?oDk-`'
        b'Hx4{r5VvI^WU%YH_m0s0w3U`0IDt06TcR@&&A3qRUVLme4hq0{AIE$>1UR*zj8K0$6p7ZMvsbR}!Fakk<{z^#7kL=V*uTNJJRI}!'
        b'EX+9o1Db<!DvFxjC-b&<gJaIj!krf2fCu^?aA5ia4{zAp7a`5^JxCLLROqX*BmDZp&mh+`HA8l3g|?EeFxUet^@U2tHB{&%f%`^E'
        b'ZCOv-vSMvn2BBOEJ4E`|i7Wu&zrv!cWp$$GeF6QMDi~d{;>aT4Pi+VOl>6FX`<lTzFxwd|%yNG_*#67G8mtM2vY`|v)d+Va>hNNJ'
        b'%PmfrFaTdo1>SK`!PZ#8z>L%?YWxdh3PTI=I<yeAWumTWPKyfuDm%f94MHcMon-zvbnpI@s}%RFy<7U~kd0rxw<RIWo*^d-mnxl!'
        b'e2NcTtWg;_=vTcsWTmaunCBMfNxSRO5ney=1z6t_8S@Qn0LfFZ)l?1U<qb6z{q&G2dq}6Z#=ajEEgb^hGWbRupVOW-<jxvuWD6Zx'
        b'Ll)q*=fGM7{crm95D8b+>;$RQY0AT;e(k>+a<2!#rLAy7oj<6cQ3BDSP^}TSuN!hFgS`J~9e|QGWFHvMKNAhfL#BkGi&!08z)g)u'
        b'm=sul@s%G|4z({EYFIhc!n$1H7{AEu?V`&H2xloL1h;Fszi+#F$h{cU+>r1UXEERHIHZWy53z@=t`V-osi-}q8Q~uCJ<Ti%ra!eP'
        b'&-BC)Y&8stm^Y_=(U5x)sN|eOJLLJR#3d%GMA<=e+I2(jCqeSZ3A|mA%AbkZK$wDtI)JAhR*eC>$I{6yj;|&>H#iFp<c~}(2OI?#'
        b'o6QJ3m-dUh@QZ>RC<;A~5KM@7WQG0Fpdo&BkY6f-^Irz|de*n^;uwF}5*SeaEFa>XjBq^X!dgt^5bHG69;Ri;?aN@qI#Lz<=6;SS'
        b'dU!zhw0z(=BZ6=MC?aSM8AuuObh_NOm<&UC6&|&SoR_*338wW<B(|&>R2+SM0FIg{L0HSYy^EO~6iV0NLU5ss8TBSnHWO=awrxR}'
        b'0dI=)$}<RHZz%dmED~qBV7eBEu(i$V&cPZYQY7}?XNE_$nD6+4sU~kA%fx&O1EpULt`=<#3rYE65R@f}BZosfUQ_Vqqg`5{Gz7;3'
        b'>kOnEoK2Ah$0v+?=Nt3seQc8Bn``5dctsLUDq+LsFU*4N#2}<krD%hxQhdN)@7O)q@V|q#&Ocx_7CmwXD=DN(&kQys4jwEcgASa5'
        b'_Yduqq({M+2TRR^aQ%_retZ(Nb#{Q1os_<fzg+0wQKTrc*`;r3@174v?21oLUJ0&kcyBOdg~h^cl2yHG`IK{Ya@Ww6?tKkF?e=jM'
        b'ir7;=uCF-Sfr>*ABvIX7Ik=)SxU%E0LRZ<$(#?xMI&c`CfjqDu6F-Bf%Ld;jqQX|3I}n12DMVd4xCeXXsp8nr-YnZnq-G(sg;2ja'
        b'7^g8{N%MkZ;xMf`PDI5wYf;eusCW|d{F7^2R44M-B<ZFkQ5?VKiZH()>^QBsa;vC+Y%ZLzJ#&hGSKnwo>D&E3L~!jVi@!70HUs-E'
        b'xGnY|*7_arAM&pNn?VdGL&Nif9W{#jTI+QTmb@H=G)5p*b51<^RQn5q?iU6fzZ-01hcw$ICms!jr&nav>TgiCrWtTZ!?wXIwPl&2'
        b'mP|3T4UX3N%!(8zh6Gmz*E-F}%H6?q>&G04uf`#5+WB)E)Q$<bshaA*2Bw)`4=gs@rS`z(hA`8?frjD!6*0ml+NbEZ3d?_U6g9b8'
        b'mg+#yqu(grkhI<6UqFBtkalfc`-;d0?0D_SpcvX)V6ttJfuEfcv2d?hbBv2N4+4`}wFa|=A`ul^EBqT`2Hnwv?Lh-}e{E=#y&#gZ'
        b'#}sR|OCuAtOA9f}X)bLu(Y|=lZ5V8H7{wy~IV~XUWk^~N(ykwL>p{BS@%W%+gT!_o82P!j6-ZhI(ov|m06F+uX>etJ4`+x;xX!`5'
        b'8<JUFYI&ElxV<a`ZLU_%uC7ot%pG*k8El{KKUhIx2egEx5y*to)lM1GcBP|QaiJC-6Ow&>5Dlh-?c!;#Kg1*tr1%XK#Uz{MQ8B>#'
        b'OOBC~*y2U8?~}~Fej__cik6?mA)SC-lnRvm#~iznD!x*U79VW5Gq6y^a076c`PRV3c=4EbP2BQ6o*hMyL6%lr*gv=hVJyzs^VQ7s'
        b'K%{i`zEC4&Otq?q`?Z)|Njr%3h9^lZA|T4q(|-|T-;=YyY92&awy*fR<_BQ<Tn##@xJYa~1B~6gez>%a0$C{Bjkz(f_X>YCM!5Q1'
        b'=p*PiqcL~qwSlXIT~deHrBI1%)Ez2^MpQLsm)W$6V*5ogu;XD4UWXebO)`Uj9R?qk;O{=$9HIhcLWDNh=D;Gfe(>g!)34YGt=Fd{'
        b'HV08qHvZ@c(>f5LozHwcP~Ze`K=AZ4=LQPOzNH;FzcIqN2YC5HJH)&Sd>U>|X3=8x*@2V~1`;tXFf^IdkVt2*7jFmN1^g#rNTk0O'
        b'SoJ`<^M~{XWOn~1v0V!cc8IGC=90czWgQN(SH>@tsb2jN(p2vdv7ve1bLPBF#2kV(XI2etlI;=KVS6MU66AJYu`88Esa;g6CNS+K'
        b'WDk}afuw4H(E@k%Mab2~RRK+Codg8iiV|@H8XJH){ybn1-y;uihcZZ{N&WhO(=E4Sb}jTPZrM#0ffY$-dsRz`iuB?Ql{oLtRAAO>'
        b's=}wk2T8kfx7yT%+Jo$g5dKv=T45^OVA~9IU6V|!tTut}z%_Bl&VhWmcja_o!uiBZBoSMJ0ST)L^GzpIU&;~#RIkZMEPZLDf*f0~'
        b'=cV5!z(-mvQlV7<%54@iTVU5!r=_4TxMq^~p(J!DO4E;4DIp~><dHrfbw^(!y1WsML`|s!b-0%Bo{LO7NRTt@4T0(Yb$F^q1!$4#'
        b'kgh){vxO42^S3|HqIF>8AkzF8ER-dP5%T?&4PY!2VY7^RV4<wwppW?@E-m*i92?d4sf0UVE_=QQn5Yg;@q2>~B;~0AI+LI^2%sZP'
        b'!?xd$rA5uvn$ndy7FBjg`b(;LA?b9wrfOcb{vuIW+JpmK?4|JjKPjm;krHiC`mWvc&^={2wrwe@cjsrUzn->ie$K|&4=}L>S+Qn4'
        b'_}z?Dq?ByFo|X_;vgLYO*CQ&zCySmlpi<8pc%ImVSDWlXHf>Ovmb7ElCSeai6-AQ1;*|)E=~P*FGJOZMVyzdw#iD8x^JbqmsC0jy'
        b'_Ie>&sc1q4K3!1(r0b<^RMiJLrY4zPMLu?2s(W76{jQ9Z)gQ}a;q4Q2p)WJjUu{a4g884SK|y!kkf|0=^UM8pK23fX#f7Dnj&FDN'
        b'X5M4~B)r*+*-I-N-|XzkoM9x}15bW)>0L$bd*@}<LF`fMk>jF<p8oaEpiNkCc77*E`hpUm#;Ec9K8_5mFzqOU2SrcLKbo`q>98HI'
        b'U%%R8|2=3&1i)Thw<EiG`O|d!zxv%*`yE&N8=cQ<5Q+V_-u#M`gX>DNo8f~Kq?DZBBxO&PXB6gH&rs)0z(wx22iB354hZN_74<jy'
        b'q`3Pp`f5dhFZ9)>LE;+D6D<Ec$DHjKf5I_M{rMjQeg^U+|D0fRfI0MjKN$NQEGZ=?yh99}jkN7Vj%kl-SA<+8@l&nw+mmKbDL8?('
        b'>XD5V2f(imIl8PGXsR4pPAe#|^Oe3Gmd)ET({73FrW!O$i)DoqY1xR`fx`8kYQxFQiztAzqtD9<GgaH~-XG)DvVrZ@ro>EpknyF>'
        b'Hm&@83XlO`QyCwW^O;AZ9+;N~lQvYFs&d|{j%gCZ`$jz+@;o6P;Ht4E;(QQ*AwiMicP~ns#9$T#^}*}RDLd9RziKZ`c{L{OiyzaL'
        b'&9n}3rdRtDz6E_ZJFtYWAr0IJohenn2#7#s(MVP}25<#Tc5rSE1Bswe70lfez9*teQvLKrQK7qu03yupE)Mcs6{}+A0HCzxC$NO4'
        b'k&XKSaS|3Gs!3mgI)4!5yanp2X-F!~X;5_$nN(k#BV+64YKG_bV!M}9()y%;B+TrS0pe=re5ox8J?Q`%BI7G6V|O!1UmvS!PwRK5'
        b'^*h$|Hy(P!b4|QJYTdf|BD5G#=KEd%GT#9-HqR#)rR=BWI{=@wQQt6j?CM#2U=vyCuJePO;vR^ymu`>QZZ9l_gdj<t$ogt#P-Ogq'
        b';u!``g^NDGq+*`v7vJU}yYM&ap8f$bXDUqEemYZ5hXIjc6hwwv-=C$HYq1CwBt%-2AFWoXY<@Xu$)VPW53qz7L`N-3+eNBg_e}<Y'
        b'EHX>2pkB06A6R!}tWEoXpe)Tc_P@5CG_N8-XWoOIStYg;PPLp@n}9@D#2|7_ToH6pQWgocgDn%@!?LNBXHU2L_qzl79e(|dhv!(@'
        b'#5*$Luf7Z_44K(_QoewMJF*90g$u;3eH;=38z_hI5OHf4hwOok?0KX~3I_EJS=;vQ^!i3D|7%VQ)3y3R(KVbTK`zGY9H&Ff@8JWz'
        b'knkh_OYlw@^y6A6K)oiMl({Z&n%B75w-kWD{bKekfx4}awD_)TdufTNPSgr7Io4rJ7i82UF+L!8qmOro_2+QgvD?-dc|&s_Je62`'
        b'S5<U7j_@wc!S%I66f*<+0KE&i_IU$o|FX~hWuN1#zD9Pp=B(Hiao4Ud{k+dw)Ld{%RzuScNihMB=xb@{_WYyoNMk?gPhzb%p`Afv'
        b'a4F9CK9%M~nDY<`U@R2NylVx(X8NelrbQokU!%G2p?zA<UG5&NB?Q=CA}5P#p1>`S-L0X$IJ$o1EI+&J%))6Fd9WX?5A=h154P>3'
        b'5oQYvR4Yl0`MmdmcC%n|4aT(f@(UY$qaeKr6ZQ=pRecQJcOTxpqfc0lc71S{jiQ8g5KQy--P!ue`vmv#B&?6Q)6?)qpW{d`IhX2~'
        b'j5vv1cOcZ6=F6;c<ewB%2tk?rzP-KBHI|Yx@5@Y5K6>vNCn<Bpi!l1fzDRi-m87G-z$1|b$-)Ln^ecV38~(y#Me(8N-F?vK6vO}b'
        b'8vPO<Msxdo5b%N5Q~R`7GlHPM?bFH)RH6>u0kXWOt%S27c({@Xr%7N0Zinc>MM8wx27?K=y!NorRN9NUX-gl!`jN7w5AK?K#&G_U'
        b'mjUB15hh_S5wUy?QAc>>cOy1~0o>vmy94PIy}pkJOu~7S2-f*7J*Rz5pL<Q8V=dsfmo#sRP5<4;uiRP&aVEL1qfBsvE2MRV&U=i>'
        b'!{KCLn@w%*<KJp~bVP0H%lEFG3hRlMTMw@%3Qsou^d2&niQYTc_HiWopZnx*_VP#8)-~Vp6UKU$=O{KeWCp%jal|mM?85jGU+0CX'
        b'5`8)Qcpeoh=NCL|7u-vHt@^w&_K$DiN8+&h$0<rnQB-dJtlvUeU!p2<tv0H}4zgYn9w3102VQ=hZEH5JkxG-@J{z!%cAw<0d^X_8'
        b'tv(z0LpY=y>G4NCz>x-j<SQJ$@IT7Q;Xjw19po=@Isg9{zQ*OTLY)=6-tZ}|v11iVEe)H85B2?fd$Vynofe2zV_F$+IFT~11hGq1'
        b'_Pf=3Xk*Fl@>ivK*y0L%U~xL14!setjoomqH)K^E3T9$L50p;mYOES>B7$k=8_4J@W3p3+$ly9(<_j<11AVH#+-thrOVdH5f#)zX'
        b'$a~=d<D;gw-jE34UPT-heWBO%89%3R;W~UIu5Rt+;jCT|J_2emJFLbBlg!8RKq~psLy4wSy&%zavUfJMu-$cD68-mHGK_D8B#qu?'
        b'nn*H;`50oIa;&%PSTij`7UY3xoO!fYM^p4NBm^fhU=&=#<4iTt3+4`D7scf7$)L#0q?AZ?q~aB{(jCdrDN5$=uo5RqRk+=M?JYSd'
        b'cZ!f}ILoeu2h>eenVYIq#HnEg_llb$qa#s4RKV&t{ABgaJ21a=UoQlygdoI!fV>4k9C^KD;WfOHN0a>T|3s5{qnFqGj#oilHPJAu'
        b'(j;VpT752x8(IFX!aNA37h&W)oi5DYzTRKCi3pGJ+awKNBh{a~naUEn)N=K<-VK=Ntb`2G{9U5?mh;Tz)Y-kJY+=xLW<$!GHuv5e'
        b'5+XC8XNNEtyucw+e%+gK?+%Y3gBB3?_#wTQgqNGs@g3{<8$j?-Z6cl#FXv^DFviKfqzaDmFMA&v`;gZ%9%h*b`C=L53-e*)y@t#J'
        b'OQhq*2O7dsmh>ja%Tu1|^<EOfc#yq|jO*n0u}O*T%@DG2Qw-m4;-T)CzUZE9h6(NQDmd>xaZvBQyWSyA@B3+2x}7egcL9NaV$O$A'
        b'_mV!dXV;m>da07N4L|E0sYLlFqv|W=4I#btweknfL|0220(+^q!r&dOO2xw&{=HNs%*c2sqe4n8Ae?m^TPfc`E4)t$3i_<n)iWEP'
        b'U8kmUk6vf6UI*687gb}uvsIPe?Rf}yik<Mj$Ha{GI9cm|p6zx_^voXaPMDm1^Qy-&uSYoQ?F%v~C;Ctk=ieZnEe^!j$$nPe{7`Mz'
        b'd+3(CAlGrGhkCDkwwTkgfH~GZdyZ87O^>jq{lq*W{soUTrhc#6`saD!fpgWDdx|U6?LD^hcS#>>WVyHBr5Ab}7khLxDs+*SJ1pI-'
        b'-TQP$qz}26dFx&qrjL5|!j~Cyh*U?1H5+zt8^K>?AoDYJ!ve1mrn5ck{h<#9`HCP{HLs)SmJWUepNu65GMLKEBiDsgQ!Dc>v%ht+'
        b'+0?UnR8HPP!t&ki<}Vf0HHut727`3VwcFRk<THHOb@lcgf}BGxB%kHup6_7%zscuk<JWFqW_MirnrdOeR7YWnZ*P;2l23v%RZV^n'
        b';$OE-`+L+)T|8P5qG|rt=-!uv1Lu*1aEWwTve0cp{Yp<9#=jky8V1$3m7g7{TM*EfO}?NTtEjc*WcFot8|=Yz<z(zak>&Dja$Ukd'
        b'X5WPSeGj>MOp09e12_O2pLczJo7vq%27@$^vKn9t5<!^-Ma&XNVPGG>45t$FyPn3Q2+!BPF@UGx4Ml+ubh`auVw4CIPs-odE8Wsl'
        b'BB&l|w0}3Vr3W4x%jk*3!N;p}<jik+W;M^OoxVxn4J$QaEtxz}CiS)N{k9+ueRO1jO?+42SJxdbVlhP>Y$<6lv1hC$XIgA5a-vLT'
        b'+l<usSB6H$kbzJ!KPxRz2HIG*K>0`+J3>kil=YC2WT4a00dIYg+Y)YbWSrQ0b|Tu)!;2T=ih%F{x;Q>OY_<0RD%>>%?<oey=!#mB'
        b'uo`6?U8ql(;h4xCzMK4(gH9J<wGji~I332eyl184QV<YNaN+(68#@vn`bok7N7_mMI%(?=w;BgHkue|%_%I!5<#$#~$<5D#Dbpdm'
        b'L6?a<i^nPzdX|kX!&+A%dUgZ^@>d~d7KtX|$l?6R@yztR=H%^YX%9IEB$BJi=Y&Mp2XN^A(FKPN)r@h`K0VZ5qILSlQlv-sl-e58'
        b'OzuH&qgB_y;61t+1@L$5(Ge%NIBs<}-0J3U@73GoIs?TF!&sb*@9EwPY>eEvl$X6y(?GY4X9WXM2doA8eHFuWb%VI=Fygf#i0C)F'
        b';(S1=*Ew)p>E8R<Y#YWziuo3{kp$aFlsb<hte|eBeBAMQH;BV$1LM8z+PdnnBp>E7tj_e0Zss4|{QLmSq|*!SwR$)*Apd>H?9pxA'
        b'mstYP=F&xKmSUd6x1-N@-=ml?0S?_J!x9?3^TYJ_ZsDAfJ`B+<4rrS>NmuJFZCtiL=BeU^Yj&VE+&{#$vddQcp#Ue4K)(fXea@X!'
        b'dOqMli5nc?0VG@7Miw#eLVVS4cZ1=>?oT{T)opbp#09&Li{~I5yx(*QS8B8bAhY$pB(M|eKX+4hx%vYSCCGe2y|3G}zdH$27j>J8'
        b'_|e0RcDbpr+vt6q8E%>Iw(tcGkihdHXDQ+C>BPO=_jF?E3*CUy59t$fBeSII-hF_*-Ot_ShlSD+9blMZ6kb&;jW%^r4jw<;{5K9X'
        b'Z(X7AHZQ1c=7sL$T7@-U4hGWkT=zYLLPotsG$$!KW*=G>cultVePA(kBq<(F>;#Ek86$H%+f98z2<f?(-T;tt>wRFmZ13kfyL{xD'
        b';*x-c%#qSfeGK7eWY>><Utg@~;N(^g=G}w^zL8P&xyEbqORE&dYcTa&p_-941*oUlPDPu$`Ff!A!|MUYwQ{3yM;niRrrZ1;|DYre'
        b'w7juaUUHCEgShS38+vw^)h5@Sk=NTP{W18Igw>jBX01T%ML*fSTpA%zXJNP1Yt%$Xbr<k&#R7Xd*LYtz3UFZnPA;Alw$ruv-q(z@'
        b'oPQD*j^Ao5P5+3;&SeK-`I`{ug}bDZHRq{kc*TMxr<=mVu>5pHV!_1gVfh@)=0L33{GDx#nafWk=_grQwO@A`Z#v{)85y}H*;J|9'
        b'!^6NN>4AI+pC!p2R%6|zc(-ngf@ivtY<VftT>{45TO|+1{K8XuyUVMQF=X?7*y*kZVAUgC-Uhb-EX7YFm-0}M=XMG$XLffnw>lw$'
        b'V#l96-uWPAHhTCZ_P7(!lRad+%pZuLvk~T;2kNUo!>^;%!+g{AHhcg=3#|whEmMEnC0Ha8Cdffz=0>M=ox&@|#L-8)0AcuN27z+5'
        b'{fz_IXLt?O?0~uaNTk+r$zHqo(UEXHmha+7BH=L5D`BlpE<6AezsF@B?6Nueff9SQoEU&*2grrK@f~yT?-HNqMjlA`OIPbTVSEiz'
        b'$qg*OolE%2JAePoZIZzgeVQLQ-7?$rGE$;@%9%~CWq$5)zuRREwOQBNtgktfe`6}LjcC#2RI0tU)B2>TPSk`ke}c4NUvDPo7d(Z&'
        b'Evav5E@^8{TOcZU`j@q@lk?Xb(6`CcbW~)-0fNM~8Vr}-MSVABEHsg-BTu2E*q4q9H#$u6%_#dWRqN7an#kbwi?K!)*-l5Dxky~Y'
        b'nQV{uAyX3LRW)zBHkmHPpce_!?~)VMouQab0?-m)ul@Z>m%68umpRdUx`0Sizud)39)5gy{maXqDy3s*SHrHZix?PVX4Py<!d->u'
        b'yZ9?9n?2s^FE4cQPl7sfx|m<{e6Y2vqh0}QP0EheH=3+xD97fm#?S6B>tU{|=T7l0M@HA6<eK=RsEJ@wJP+K1c(&_~cu;hWfGucl'
        b'a+a4w-n&7X+S~X1eYJP3N1f6|g|ei7oZxc^izHwump$UW+@)U8MTN1^t30|ztQM=fuEm4tNIYAqQm^uW3@ujNI3H7(yXbcjD$Ew8'
        b'@FU?Ginr{~`Lau3Sp@Ez9R<aGLGghs^)o{0Dl8CF>mZl`tHSjxqR)bdPTrKk@9PM%Y(64I{YJig0afcf_YU?Ous}Qx)1p_E+GwhK'
        b'+@O{!<P@Uo^5@r}!ac${8J(Ur;97sZ647<|e;j}S5Lg!+<1XAs5vkts#Er=4%z&;8T28m%!vFI8_&c#y4T98WWLXfR_V+w+n}EdQ'
        b'(D|5FN#dYF6^-aqk!4dHpk=hr!%gZsaFEA?Jvt&(FgoKI8E0qaR{d`DW+xwN`{(G7La6wcGmrU=kaPV;gnJDe7<g8_u%Xgj(|+oQ'
        b'>zRtNOr;LT^_l)U1bkIG6nr1iVes8$q=ah8oPRkps4O%1{OD!1yi85f?j0ZZh(RaG5kxPaib2U3^j{t%h5{5q8oXC9n%m?$tMMnl'
        b'MypX+MiWSaH2Alu=U-L_m8paMeBkgR*AURg>)(t0{AjgGuYQC={AqQd4)v!nf4$mYo1(-04Vj5M(;0Zs-ri8*u5Lg11CQTzwPH-I'
        b'1hoLVsn2%mTPR>ACSfb-SpCc_ZzlKS$(x7}T(`~^eY`U{#%ew%Pi2ve&Bz{ncNw|?Um3GJW;{a}Z>j^Yx;%)y-pl#Tsrn`T8?60E'
        b'=ggCmEWF3>)-Phg&yriefJhG_%eo=RJNm~kDn=LgSo_;Q33vbA)n7dB5)V1&8s2yqbGF1W<#3u6U-)64r@h$IQ0#d&#B-iY+a;~T'
        b'Ehu5fOYKm&C#GM+N(4ch4kc&~8E_GUhlb%5_MAXX1aS?XxP>P+!wC?;K;SXL{i=r#`FWExK?In=d^t}jarHW%_84ExMG@{Dp7x9z'
        b'e5Qg}NaPQ4*~)4DfHm$3A>bQPz~`V*_@d?tgp>j6T994lmQ~*Whw&x`zED_QCj&gy7>Vh^^1SB|c~zB4&(R&H(yCAcwwi2vv6|L&'
        b'qN`<bbTB-ewc$G4tGoI|wUSwN1MZwD^|XAk-9Q&AV+~ggSe%k~)T{MOJj}My@(R7xno(3~z$*2zr$iNWQDLDzJIse9md`utyRNkt'
        b's3N!>1$_xKt&Bw5zG#p0xZ^wxi#?9T9#6C=>!VeBe}u1p6!ABu!{($<tk;w6i#%?fry<7E3fkjeT$)2->rXD=FG4Q^0uY6L9pjRd'
        b'bCK6W7s|4w@GaN${l#xOKMM1tqGSLYR$eFeR6yw$ybgfzr}&m7c-J`rE$Z;9XYKk5`hvYsf53p-u|oYxJu~OVy|aygrh9*^Bj9Uy'
        b'R*0J(Tb9)lrqksjYeKu`E!OiV?)2tm@ECL%20=Z45a8ldTjUTfFSILg$t+wv{0}I9!Qf(cDy>v4LxH}k!z@Ewagb&!>Kg+JwD$1-'
        b'`J_xW?^d1Im4N2YaQy#GAXN4rlU<Z$8Co1<+2V!m=Dg>P`#atJosRC#M#p2G5K*?j%+%Xy&hjS-b5?-B7j=Xs7i$EAHCBz4?6cJ<'
        b'iw@S?n~RDnY2k5%>xKHg@KsWqIiCM6J5U}DS;&0AUk?A9!V<LjRkj~z>j>BDcVTz)Fq%dAbFeUbEto@LmbDoChag~_Ax@umx<3U7'
        b'WjfrQE`L$mm+hZ)x<3X97U92#kU^x6@nBv_Np6#@?WXQvd0S2Uhn?;w0I@A$j3cGSedWM7ZJW{U%WJD{Ki%p60Ay{?@8_O{Pk$G}'
        b'Wta-IU_ROYey95w$jWW)6!=7q*jQAzERVL#wJl3X66q~+GPq7;8RSTewkQ{R?@zAAu43(Mr`rX}Ivf?9@Gy;!NawU24b?@pELZx%'
        b'%)f%nhSq70KK9;`M&I_TPIo0pc|T#Cb6!~MnJ0p?FbH1kwXH~aL#7HvY!}w*v*d+X(ipsC40N8y!|Ah>Uj2P<j#_?&0jG|{V=GVt'
        b'4dX9hx=^ZQ_W#=^nf`!58ot!&wstliTIAT#Y2k>rahjGFJKO)z>Ha-PeJcMZm#vX&r^5lRuXMU!25C>{PjId+Xj&9Xs|i&L(w^Jt'
        b'-T~6%;OP~uM3pKoV-fSmcfr^hBg-jcZq_HO7W%*kM#?fpnpDWUC%dbs{~yY}1t6+wZF}uKGcdwdX8;ieb7o**G%Y|4Fp6PB#7ieI'
        b'Q7k(F0+QJ|Xq+VD<P4Y&O6LHYf?3U=Byyw#O))hYG(y9ZctyE5pi@>>WJsv!{-3q?pmo0Q`@jE3pLy5)zTWk&wb!LIVds;qcZ>_&'
        b';$KY#Y~8oo!+dCvhxajww+CsDIRaz4VYGqwUQfh!p-sDwKI}+g=`FvyAaBF%iYJ+!9{*^Wcg^-JlAv!qCDe~@i+9OD`Ii9>AI3%a'
        b'j#RFe&i{<i{{Lt2Dr(joQO#87m}(d8i?ma@RK&3&gNUOEEOCt?W&RmM=+`REj2OXW`tMAp!^1+h)~2Xtw1Le0rIa~Wep~w6meIqi'
        b'T`L-RSTA6?QH?gfF1q|nMY;=9?W(oGSUaB;vy#5xzRPcXwJRp4v6pyZ|29UV?BKJiBV0M=tS$URw{1&Jiff$v!SM&(4o=Nm>RG$g'
        b'i*C!;UK`v4OY6`3n$7!~mAO`1{%-nJX`H5FJl);9bCYLXDCg;Z=wN8`2I@&XLNZa5Emif|U<-(*;ym4Ij(Ga6{?~XaI(X;awO85Z'
        b'Gc7+{wcWc~yJM{No2!m?X}dpdC}&!3UbXeZR3)A}qHU#*ww0f*+HS&F-S{gHNoYkQ<#Dd#7;UKV-qJU^zMu$>V@tlc&y6lB-xxHS'
        b'-nFE0nGR`GQcbUvNq>(gdHxylL`|T_?mRRFm-KSJP})3;^H|FeLT?L5BUw9D+Gw_tF|}SD+)zyUZ{QH`zuhZu3{cHgrJ@ba-w3{}'
        b'?I+&a0ZZUUl_k6JN8VQ>-Y>0*o!;oYzf<U|wO4J8NVd&deU&oge@n&Q&~VjO4`aFsS|@F1bpeG9EuUYt9fH|O;a(v~7IWzcQ!Ud5'
        b'2syl#)620d4=xfmZcq0u1Dl~N@EXbS&v2c;BETbPq~{U(*3>3G$de7)IuZGD7t^l^7~*~NJ_eYqAc!_haKJ|Te8>&rU4G9pBVTXH'
        b'_8xtY=6^9giK7i+t6fZ`V*cqh*}`R$7=eD^g+7jYd-tmC-K(_~8P=Su={D4x0a-fNQhe1`1k<Hry;TG;^bC<3V^B*AkGHJ8YBR&~'
        b'uarr;fT6_tley?YpVEUd+VSW?v5ynd{6saA-b;`N9qZ&cUg$$~{P7fav$HWI(LY1xDr}OUD=_`J?DRjF(NWD2Ks%Dcs!IQb%wO+{'
        b'!Rig(+sy?Xry-!?3<j@?cj%=P8fV9G_}}Neo$(D7KA3cS%lhafaqbs<g<062-YpC(g}-9hsAwgFql#8VM-}ZO&QXP)A~6dOhWWAd'
        b'5?88UhnO6`Eap1PdGDpS8;^_omLj5`5qPEHsx9Vf?MFkb+N%}2rD6wo@~SNgW<$kmptYWi<$2ZosZ6L^I?=80Y|DhJws2T`(4BrS'
        b'vZ2T4xI9YC(d}_)Rg<pTLSU7I@di>ECeTwz^As?YEA&2NPgcD6O3O33cj?BA`-~u!{Gm)^Vnj*h4`$OL#0?jDQ+hj@KXnM0O&afg'
        b'(ltriu0<1-IBqkQ0qK#<L^m4#P!=V9JV1LGHK|=m_w2blOIkbh{#*+qT!mH9Cw!8)=B?{>H|yx4Qo*(P2BKZW><SQ?tkj!j%8x55'
        b'Y!6C1eaL-?oUQ_^rl+P*^2>z`xv*=$6V4K430fI?LHhH&_xRi1hI>Ntex`BNZ7STLJMQ<MMnm^SR0eQt`YgJ&k!8`e2YKJcZd-S^'
        b'wV}JV{8Yt8@IJ?7Fh0&4%8mAgxFt-NoqIB_^4{Oy&(lb#xyx;Ohr;_3^o{-9wzJ)}JIky!-4*{t-+&y7I{UiY_HUSO75hfkVv;Jz'
        b'Xf9=p_8Xxbx;aTH6Xx^iks;O2mR`VUQ+P82PU9}zDcKEqF+=_oZJvg(cSnX=7>q6HeGFKZsk)oa<%RWsG*A>VhGo5WqobO5&%I}v'
        b'veEn3fw^gPYv==s(h$@5lXwRmcvL~Rt+KnOvfH|*o5~Ywq<L&?vrqcF&T}qvh4G)tac#n7Na%%TBt`B#IwQ(n=!VqLReavaFdfb-'
        b'ZZM+U-uyN_&__GphxDSmMCX~KcO>DqQ_{+_wU&wkW~S04?LsbEm2qd?-`^UOdjeAyGh<ln>8%^W4e@h(ef`j_b+ztf>#^E7;f3zL'
        b'Wt=>3+6+IlaqZ&Fu7YE!i#<4(yv1Iri$`qOUO@M(*D>YC{Iqq9nei(#7Sy*Yo6gp?6udTjd&F}Q+qJ(i<<@v^&JmZ?#onolM^<e&'
        b'U9;1ffpy;c{M0y7ek|GX$w1y&CN*xpu%tmb>*vfa$&!&w1l>)ZH!a-7F7o-}7rGxjEFd>6>~7vFTu&oDQbSqykkSbJ8#lODfwr^w'
        b'Zd-hJO+vRdp<DZ^G*2_q+e~UT-t_Ki@l7q^eXeBFGu^@iVA6C4lXr&6lPAt^B9&(<-jsr=y-DjQ(5E+0*Vm%&w&}ZTqPwk6b!#)F'
        b'gZn9*7X*!XmDQ)`+cT6QPt%m<NDjMN!@KEiik~yZVcml8UpZvk)S3ai{kXC+qGfXT$*-0ky13O_wL)c`*zNe588~1Hp-B<$rY1SU'
        b'g;(5`k#v!@)P2jyQ6)hh@32MJ>g{jm8|~Tc|NceOeW$F*k>CDU<!F~5g`4Dh=r5)|jUBvW2V)&WlTtFCzTQR^ONEk>xC`%KNgBHb'
        b'zq4JmM|*YClR-M+DmCG4MUz{1>C5Xz1qsWbH0^9&D?@KSonL-ZuKke7kkAQZ9cy*%-f*a*lzH%u8ws9l49#R`?DYy^x`oAN!JXg;'
        b'6SnB@y6E|@0P46_Lu$X0Yqv1!YhA*Z^%;8)2w%h-e-Q3xtGrUpuJiCQePSQnE@YOQo5JcQIlf?G-3PA)EUYu_v=7>aj}{FBeTJE='
        b'cHwC#vkx`@ik|LqYwQ_3XWi08$NdTv(%G(*e_Wx_yZOclUwEQ7+Lvs6RQO0M+}D-k73S^7d2U;2Zp>`R`Ep4ej8}%cah^-UWa2W9'
        b'eX(-sCZT=K_ZcdD^c5Z)%NUhdZ0qvdQnX7&cOYxmpr4c~ea$5&yjGTeXFb&A$YbzZf#1)%w8F2$#905;m5$$<F0F|%z28+_(<Q!~'
        b'S>08<r%Sxx31;RYV2VRvVr~#x*1FFG{yxNBsa#)W+TLZaQdU)NsMW4!Al+0k%Xd((Ij*~Z%cZl$r7@08j8NI$*(CG0LBq}1uXG+w'
        b'+xV1oI#+oQ1@sYW*7R<dP`>k%`h`puwhE-Q!Q8a&Alul+FI^+-0}wXNlDY;k{A)bD=g>;`&1%$MbdWy4G+%CcyUVt=tG0ZHby=5V'
        b'k`zMsVQQM!Wi!IGLgd_e>Jj^Op2e?pZ7nT4*pl02djobK(Yqc?taNRqjIM=OMsFGI-tu~vZ3Qep#^6E=MlHo0rh3R0kB}`RAA92r'
        b'Ix{!EJT4IdR+^4T3e;uFam-Ddmw3;i_G7+QJ%Zj&#p@Er^z2Gldyg0ASZ^f!T^haAUhR5BIxgDbHSmsG?oIDIk|WY`Yf?dq!*k#n'
        b'H*?Biw}Q)>%M2K#AyK1N>|(~L`x7{}GJ2enhM)DN3S*dKC*n|mtF`jN3n%jQC#13WXxp|dcD7!7snRsP%efa$e4$Qm^5}Z7C*iR!'
        b'VTF0{I~e?_$B9NJdDp}B-~F0lEt9)!le=oBbXiAqX&;fACUps2T1RIAAzik|x@tnYgr`Lx+`+Sgng6}?;k|SIT~jqe$n#lm>k#yh'
        b'iWQ7{SeLL}#aFn%nVr8^rtY^3eN}8dy-bT=mu*Z}&6qChZ}tjrspGY~Vu;>`JDi7$nnd$<VT7U`eudEOSELg0IHFR>h}2gjd^N1F'
        b'@(JDc=zX*=>SRHC|HQG*-Ze=%HAeVm8+Xh;SvhM`^bI@Az-NSY_x=7<G_-cu9d9yD57U$(19tr+Y9H!P=0Epak#H(L<)pwTT!hBl'
        b'Y|i~vI5pVl;8Tu?7UuBG@Y297d+EfsOt$t4zoJo2rz`PH>Hfl*<&Az7&w^jrOB?Bp5N=xz%S5hf-=!?7GMXCg=yX{JRF+C(#SBKg'
        b'n$=#W+`38VprwuGljtojooEV;?R>~tyYOjD%)A7``Dx*9$A8)B1(+`|53A*fJy<wL8ON%>v~Sz=uuL?<dCdsc`hi`$j56Q{R-y+('
        b'>fn;*XLi~Y{GINdh6}F<hLkNhjRy6Ztj;y_LeLZ1KN?s5hqF4i_N#EmtIQuwb!^Rt_R2GUbHIPmK6lUhe+Z=FWhVItN%E^wQ?6au'
        b'+La?Wy=J!uDOYLW&VE6;Uc-%e$L;d8%|T>AsaJ*%8~Z3}S!=hgwb!h(TNm23KTGWElr<UlRc3lG@CF*NoRhEfO<A|q)wF~b^&9fa'
        b'P`bReZmX<Z$CRfsl^(y$wO^lV|6EnLSs14djD9lEn^t|L=T6_?@<%;(ddqsMjPqyFwqBb?$EpI4YWIVT_Hm|;fp9Pmyp{8DU#V%h'
        b'(b&pYdQ^_4!AmQBgwX4z9{6Af9LR;cvYds!K&Xjn94j>WwMB#LbPMdZ1@@XGyEV|B-Ytn9XQxYs6;qjqOyZ}`YF1zqb@JM;{2cy_'
        b'$fb`+9QpJ<ggN3_>;zxCC`US;U}(6}cH1<2O^n^Dushl%4@0~BFtps82(QAA(T8pv46@=azFOvpWklID+Qsf%KMoO}946kcak|j('
        b'(B`u(kJ)XH*=ruRTl=p#E=cAc^Q)Gnk73IFJxm8X)WhxTMzf9MoXbFhBvB~bg{?u_hHQ8a!^>z!&0ncJCfMz)qy4EomDtBCt2EY|'
        b'w0$0tRh2tDXn<k?a-%GodQPTVm>;joZZ0u(U0J{0I4<A&rtIMjUE4d8j;$9tnXVyd%5-P9@K=WXc4hn|&O_*MV9Mc)3rlA>>EVpH'
        b'#757;ivD6R@-z|U=+H-G>a$lMPl;bAICjD4V|B;0uk)g8Z?azzxJdzPI_6Y)4D#w1Dd+v}itW2AHQ!ya?z!SPE@|H0a{Y?Uai!+l'
        b'D~)&f=sj1Q7c}@WYJu;SYn;P^dPOH~$azAL!W#_px7Gcw>x)-2N;GGfP{VxABX$_%x{30@A)%(jSL#Lxmr$E!_2zoc&p2VD_gqpx'
        b'L3QA>5qrkhZ>jaRl-2JkGnOnSsAGEk7_En%<fmt!*WPf-gb!Ov)s?MgZqx%=`#;C7xK5!NX>`PtcI9{PWWI4loC&87W12%N=&d2b'
        b'V=`R2ni;$!(Qi%IzF{pNU9o+1#hQ7g_M@LFY9$G;P=63v+~G}o8{P~WuNfQJwIQT<VrST7)+NOGnb97joHbJv(xgG&Gs-m{P8PE0'
        b'3g?SPF*{$c&u&h$WYj0m&fk{y&=VbF<Ay-!u`o;a4i`Of(j}v5yHDaX8}c+>OG=rD2J?#0RIkmM#IH0sygp)u{R!pLNh!}<LGhbY'
        b'mre>R9ls$IQ|zCJ>Deo~24VOPIw%$7AbYt|Rb@omfe2vv$msZn6lOc8*Pf86(v>Lf|B?x>pv`RK75=};9Lz8A|26%b*OEzW>{%W;'
        b'Z#>0|=k7HplbffiM|SE4&su!rsY&s^BHp3yxJ8;n9amANLK8Bide2QAS?!W8clPsYmSey193Hflt?1%Ik9kp7Q+58%GZD=OI&Zb}'
        b'n(-bF+ktx674h0ok8Mp4JD~CkH_q9S=$#(I-JzzA&Ow>Rdb1M=a@-(UKS;75Y8~jXhdD>{B*}aOaa^L+-XNzOr<H`)()(5#{2UjF'
        b'skbv+?mH<$&Ute3to;1H%k7!U1s-0eogK-g)O*P|5;RIyqVZT+mTJA!c|@xHniOB|q+-GlQGyu~vaMt3G(mRZBte@Xf@&GY`tMF{'
        b'KgsZ<%dJ{JdMRl7BYeokPEmYVP!i@nP2%X`Z#>^J&}qBZX+6?eTd~!#PO|(9>ckL449BVbX;?ziN6;6}obq$8^ZT1OE7AVQ)5~3c'
        b'?6m#VX|3+8{b-CMUlOvXQ@pXf-N_+UwJL28475Kx4bpoC2Ja^Qj?WlBtmR6l&E8pK@3d~~bgY(ySUR1{O|8!HCAzj#xZy$AN#ibj'
        b'wfo(88zYEYh2<Ix-G1P>PA9?9n>s~FZq5DZvd&no^DC@ft9)J~1f>hrh0@|bN;afcyHp${2^%{rX?r)zcGl7MzDs6*URjlBUE66-'
        b'R3348zRGccpbA75!Hp;a6LK-8=O-Jpo6RYI>s(q^^mhL4R%bNn%7n0vr8J>Qvdo60FBUxE_0VQR=h8%uzR&Qo%xU<x@_Au^r}K>@'
        b'`TP;L3O%&<?<W{L1(`8rb>|I_haDwW$gcOz9<eYXB&N3wG}iM(J+sr4)G17Jg>7Op4i0T8?6ehh)@<lpTPbd85d>VFToq7HHL{?6'
        b'!Y2eR1nqFak9&+zoHOO=v-v+pnJKl1dt{`7PcejXvb7he;P>m`-o21cVbPV7r5{EMqxU6LHi#l)$gk~GY82iN9g^9&WGd^TB}pqb'
        b'zs)!cAyN7Kb7Fyg;rDKGV*SDucKRZLF(HtS8L1kVc(ZZc=9xlu?HFX$D6~m}xEy{gqCu_c6uNDgP=OJweY-MPU|7lfRh9~4#e0Ms'
        b'fdR6S2%p5r!+0MCL4}$>25pw4YP@t!oM+Gz%u})#C5=A~=C!ZGDL+(``LzVCk1pTV)7Ix4(ejlc``d*;(BFbQhqa9Fv_0Bc^Ju5F'
        b'yCXe8lIK67xvoXmX$$PE(RI=#p1dZ$#Gljnd*v-25j1M|{L(v`WAskpcS*UwmtU#HTwn0ou45tJbqMKlwo{3HsuEqyvfZd|>#)<8'
        b'){NSB2<Nf3O<XgIZg!?qyPbI7l+V?SXg=TK-f81HYq(BpeTO4Xg0Z2r!8qx)j1gI3qh599zfx&h+g@cBnq<(s?k#Mmjqj*oJ7aJ1'
        b'Nh=~6Hm5%rLJE{y%^`<7P-01`Q_bt%eRRWI3<v9p>GO^ULx|AMGRcE6B>q#H;)*;1j#B;L+)jwK!#Tc|66Yfj=|Zz96}FFUOMN)~'
        b'C>5q3CF4i<mX$0W@zC5XY);V0(<`0dw7nrOp6{@o@2I)ZVO`VVh>)bL>!2&B+7f3~C(LQ5wf(l>PY~qh4X_VefoRV8Kq?UyDCcdP'
        b'EOtHpK2`dq`_A?0?E?tWN`%jMh2%edi=l2S@jfQ`qgA-v`Qq5ThhmWMAdHNYhMuJn8m7&o%eC(bh4i1E-3^UDJKH0bi$CbFeb7<!'
        b'VTW~ANBX0Z!o4l;ci6Ue)NJdZ-=ITgISUu1KKBe$Vi9igk<Ftc%yi*bGtX$u7G~=usq+GT*hciw+QN#KcRFkZ9X0QC#D2#=6p^0k'
        b'*eW)T`ER=l75)k_89FM(3g0Qn47=oF7q(8JjRRF~tTLuAhB)ZqtlXduD%5Z?;|uxm#_aiK0wJzwL%#R*-^uijwxos!t7Hr60ty2-'
        b'k8yOz$$FHCSonygiZamJ20!bV4ti&qbJ1t?#kvMZ)BOkh$zbsb+c&i3=?>cq9o82*79Dc<ND`zS;@m>JoK(ETm!8ZU?^VVYcs%14'
        b'R+kXE)GO@ZY~8AelbchW?R}Nl-U-c;E)DIy<k1ZQm^QsYOl(KoaUuINg!XPgd*7kd3+-L(p%u?TI<0u?L3@vOv<ow$mx*Hmzhb;s'
        b'lE+hSD@SBxo}9bXYsr>BuNXhVdnATD-D?YvZC*kAO5!#3n#Hd6waTStwVgKFoW<kK>$Z&B@LIKN`g6q8-5!2SNI;lS{t<Gpz^PTv'
        b'`FpvsVm4XwsodFMa|ZD9IuXvgacp!)`%`R#O;Ky}D!2JWq=cr(97V*O!VT+BXo{{;c371i<CF!Ay;J4*`u;BI?3fIXal2<}hmwrZ'
        b'f%?THdRM!!pQ1n-eY9OXDe-B$z=bR3AP&yM<vO3?cB_TyurVDqOo!Flu4N>`nFGFExP)yX3Axv9@FzERqzts9#aBE{67IG`W`3HO'
        b'?zFeuZGTyAyW5`9-~OZ2&z-AU=#qZ@-Y)tE%*&$ug%S=;Wi+oy!zTNLr^d(Ba~@&)+|@VQXCI<_f)ET!eZf8{=doaK@9aZrM|-Sr'
        b'2Ds(hcH6h@)^FQut;@Cjtgu#A(Z{PVx9ix$@c5um#-(UbDETN9p-9@>t?ljOlpSmV(`{iYKEDqiyV&N-EtlGDm)fmo5#Ctsug*_S'
        b'h-boj2P64AOJAJi<ax6Knmx7syyIuSyg|Aml|-a2T=8<ABbXHK$YTRSEz)4KD$fuwcwbANigxeg?Y1x4tw#{@rt}}#<+be`Tj?4!'
        b'S{=d6R2HbeSv*=hkMCfU8&!ehnNw_e5WQAU`~5xP1aJp?N(QaN{XRXwO?hoayG}g$)x0TsdwY^}oOGdNOpit*F=&V`bT+!Q_Az44'
        b't7hrP4K^Ss^J{bJ`ZeqJ4Xu<Ec#Ja~kvVi^?N5BSg`iQKk{%gG<;+|B{8e{awzb=~wOco~*KR-M=w`*W>F9!Xos@GGWVn?hB)ZTX'
        b'R&5ljz9NF4_(F=?Uv<m#C+nutE7={lsKA=Km^fw=&PBbl{gg{3dxS~%z3;v1u8yfxZ@#J2sdMJeU+Lla?7ms@ceiz)u@yIYGxLTd'
        b'BZ+l+fqaz7u8koX;cV=)<fAyYaXQ(Yc^CO8u`oqK+16@Y%*s=)9rDlW(2Cl4?^U;R@(`)rm8?K^zh&2U@j0nYbm7xwRr3)Sw9#+*'
        b'`Qv|UNpH7hB5TjD^}^`Oxp98)xWyN4T)Ce)<yPOM@LnW?OFd*XDr3$rcZ?ECZ$e#ahwCYq&kj_x+VlMGS=_LWVW(V=3`5*qeEah)'
        b'&$inV+H1=Lt<&2pzGid3Nj58x$V^)PF7&B-(tO?&(QbA=3gT1Ll%EjNo_wIbTuaht-lt_BF(_Y89S}}a=#+IKc9!Uv&1Zga*~iZ='
        b'*D6WlUOvz~@f$O{_At+tZSi4aD|sZ38&#(iOXXl{`wuN4?Y75}!`EEeDdR+G<X$(fRID%rG;R~VLS9s5eW}ViWJE@r_{J?fbu#kX'
        b'OQ_28tjnf{->Q7tZDZT5%J$kFkEJ)TA<}l|05qCZOLQyHyqtYwLtcSL?(Krm0s|*6(>Tvb)9+C70>gtdy&k2y0?#u4QeDKT2;I18'
        b'zhA%|bW<wXke4xJjM-4?Q|1{luE0OS=RY03<5uZY=XT&=U##=4_ezgajoDB(e%Gi<pP;QwnGZLl%peTf?wW_^0!3LuwV0%*+^bl6'
        b'@8R$?r416eFg}fwPdD5X-7UY?X6tTC{iG+WxxS%!cyhC%zPx_!$I|%cjme3MS7n@hNo{h(h)_%Y)F~0uL&jg8`EG<Pq_xfP@$p$z'
        b'5!zfy@OlO3a>TV-{_+%4;3eTEh~kzuYfIZKO;%O?n{N~qB^PZ`6jjx)uZo*qp6(Z{QOv0IZaLXzJK1Las;$=YQ~JNyyjbF!(RhtF'
        b'H24NjR=mu<>=B_6MPKJU_u<^u_3|ICe>VlSIrjvb$orDy#iY5RWq+G(f1C9{+nhrc6>R)s5-4F$e=osgH+pYd*WR{YI$A?q+w?Pn'
        b'zwiF`Xh6mg#XGLSoM&D)DPY!l-HaVg$nOoJT)YX%7&77%LpMvj!I-LOgl5>>SUa4Ere!IYqQ6VHy&SgXqHSqPYxMPm{^jd7`5M2M'
        b'oHp05J6IAgZ0oIdG2OW=95-!LlaQh|Zq(Fp1LlJ>H|m44*Ns%tiy{i!Y-`)BYf(6>D#}=chRL%qD<HM!<cDn;*7A0nZFQS<HEiFk'
        b'*usWd?$6jeti{x3d!x;|3WmAqn_1tOnI2+v&bLBVwb9wpq`__ET*%6{S<_yY3O5>)iOx1d`@xbn+ln@8Cc@e3C}vUekblhVx>3rO'
        b'zqHwwwOLbO^8sCmC}PbX?&boI=2FwX%LQzsaDAD^!mq0x){@p{OKG#thtnMu@30mjA)*|mPHKbbTck1OX~;)Do|r}yu+4Sqd2L%u'
        b'Du*DT2m3qGLHmXKs-9pNbwb;m!<rONb$pxnenV)AmnLO|DTFpRjcrb-EvcHR)eudC)D%a{KdhvOUK}dFC$^tTRvUWH*?-*=pP!d|'
        b'T%V|*4LC7ZZcJ1xd~k=x)HY$Ett5^($HEk1dXfeRn+LyVEX1~{wI;aD8r*g!h1?s;JyJ36e&Fb#Efd>p6WgqhwJq}1zBL$T@w7|U'
        b'S1;KNm$sHvm7^NB9HvV$H8q!vMcJR#ay|zRGo0L3eW}*M>^w|QN$fGJgeNPB_d>R&=#qG~Abp>tKvgVlv+7#6YA`MYea4npNRi-H'
        b'e2GMSU$1}g{@0YPm&!jPm`*y9@4V=C#HHMtl%9MCW4>FP%?-uaV3oExUSpdpTI6ju7Z@Ca;Ju4oD4F{aS?COJdBLTGz*Y!kbf3eb'
        b'JFmJOaYZnW7icj3mu+`0*IK@}-n^XtSGIY7OW$Q%9}Iq=^7}6KWywPEUdnBAgH4{n$r8?oc<71Q3Sq&ROgE4R8$BP~%kr(K;I`5O'
        b'6Va(=%o3|6m9mf-_h5=)USB}R5g)bvvR;2qRi@C3XNP^nH2&ZGgsYQV^?Io)hI!~M+*vRGcYlqDYg7IIzrTajUviA{fAa@V@apsz'
        b'F85<q&hv5qYdM5#b`!+$#|XgtOz&N;*><@g#kBP@H>6;>Uu8kGUtB=~*Hob9!V5w;9r4i<jdi@5eh9Bjr3=*VxwkF5g6qZOx$dn7'
        b'!EC~4GDc6Ttj?!K-K~DDO>}UnbE_{4-Xk6ecM}fWl)8yETI4)9=X`tQjmvfoL_AZ@Woyo5MBG%sjHgLZmWsjT_7{~t2&h=vsuMS6'
        b'sLa6+FXp5DX6a>a>mQHXXIy^xTAbLoQZDCy|KHr{XL|9n{@rNtOYRGotuI^_hCG#OUR62WqhrdwNY7X<xXk%H9KTKTE(_vH;Hck<'
        b'=Ux`}E$k9D5y&$lejDTu&s=`E5Kr%I(R6b@oJ19#FK$bs^`L)F6(8@_e5=+{dP@3PZMDRda#3JvPo^cOMsqT5<^u0u^1cWVJ}wkx'
        b'FQ&=YRnsRqnX>2t#*|21ubPw<Q}3Ht8to#yJ#Y39zRB&18+;_TRyUO!Rdk4!OKs*<r@@5!|1g;IdxKp~wDg;7j@Fhtt)j(2(db9F'
        b')4$iYOuLx-^XWs1L6cT<ou;QlvFE#ucJaKUSuk`z^pxA4h>f|O^gY$RRy$lA5ke8ZX&HWz(BeE8Uds-n&Xe4Ku-juSKQRc&84TS?'
        b'&>ANM(*4O%__yp;I)jL-Wrqs3d$#6lK3T2mP!wUzcwcDlv<ym<)Hg1<AKJ4g2Hl|N5VPl?;Ejf;)73W!&(-RjccYj+a^IjS(j{AZ'
        b'lm99!I;1$Ap-g^7SRbTCnW-z5U9=@$EXw%3QEls>KGnh(&$<})1RMKj;iO+&aB#NME{>xgvR|eRtu#8NxV64a5gZ|OW8tu1wDY11'
        b'QS;z!*`(snFS)11XD~&R6mY@OS5G67UUla@^@}$aPrCSwix3T%R#ApRA1fU8j4NTe=-`Vqe{s(*jDIp;uTca~Vw?w=X_4rXLO-GD'
        b'8%Nh+bc}l<#H{%E?D)CDX++U5<k|)5LMW!VVDV_A;5RO0^u^!nbs<|WQH^lAl$wZd6sw(X1Y>2$KQB4;%8c>s+9$~V@%oHeY-}Lu'
        b'o5eN;k-+EaMQeh;kS7tm>Va4F9Levs%8+9hoO&@DsuG?@RthQN#7hil$@l)T<U^=&NPUJP_z9sPs6IR-<;sQRNebcjccv~MI?uwY'
        b'Lq=Yt??j2}y%+wFvI+l@vaJ`^wm$Gzd4XQmS@9b~`+3r|IFD|Ptk%;lRpLD|o$dB_Nn#r$lB8Q5F2YmhD<qP+{utW>zm(^F!V_1$'
        b'(O8_7l}twJNut##o)Yz%D`DrqD;4-qPE7LK`NjJ$7>&}Rm5N|9V_YZjJ>i|rdF~nX3py>39A(}oBsn=7vz+85LTOObO#1Wkyi^Ip'
        b'xt?CD<VG2{<Xd-K5W<ZwV=OBbMdIZaG22Ru)t7|bmO0r)W<~MXONh=HSN4-@IoIp{#=Phb*L6GDwPS@QA9FfU$@wf#yb%9RzTV7a'
        b'Wegt1joJ3@@?n>RuN;}#S&53}+$C7X&lmERE!<L(BERH35i1q+D{uWKn!8`9W(RHNYRFuz0%g`9VG9@4O~SnJU*c_L+{~iQi;oOD'
        b'HKdxk#1urACD0omP22^#U+~L-(gb^zvW~f)QniEj|M5i`^;>`PUD>+a9KH5y=Q>)Zhp^YQG!`P%w{OtSmKP{9ZkV3e#N-wr|J;zk'
        b'CfD5CM6NF?DmEIE=`guwa7^>&hMay|$@v-&=0}gXAOxd7#OTWud&IFfc3WNazgvaEED3a_hv~m+)jxRZK7+0x#JQNhY;~U5rj6DR'
        b'NLKdti3-!n^P-I*gT%QR0u**BDg2wbnLqu#hxfIWdI*Euy8hpscUXD+k?K60-vEtfnefsv+UJwmoGfca^!u`vTKZ`@HaTta5y>f+'
        b'YNjNGl%z;ahtAWrk}te44plP3XYO6P<e2)UlZ0W1zU%v7EIWTnTHBC>k?iC1|IJ9|^*@bd+t2^UNG8bB;K#Xiz}F=gQGN_&3;`rr'
        b'6gEWWYqg$lu<(}O^JD9uF4o*QKWG$e=}mE*4~t}D7mBZUJ3D%&uvsvIcHK<%o(zT4J=KS+Q^s9%IurFG-!*gI4ae<IQFUd1{S*1b'
        b'TThNzbI%4tC=%1uFFc-Z`}cYG$;p!#q&2uoCAi;}qkm$f@aDQ|8WZxxd3e#!65lK@XStB$=Y<E}pMO4n|3>i1V2o0=4_;%}<%E7x'
        b'@8r?*oIE;5a3AvKdBbkvWURt?QK_yy@4T8zc<?+^_3)u`U1>;2tMir9QgQTqFa$Wm5Z)!#h38%s^_t9ZaV*F<@8on$Mg;3Jj`YoZ'
        b'aY-4yB6t5dHdaSON4~A_)i~<ED`k=CgseILu%Jbw;0#5G@qF+@qj06m4%B_%!V&uyhRl%!9(>l%BM4Ec=~-h(xpQoCeUKhOFN^^~'
        b'2N10fT%eD6i0WT2(!(R7dfNHeUwCJJf9E~4ocuxmfUk?%q7tF|GO^d3;r#!2_WQjSMVp*Tb*Y)*ji;SF$BePz`dkbRb1^hzGS?TI'
        b'>BwO2?~n;AlxDgMtiY>8!Vb*jeBul8tr4`bl%|38Tgn91FEEgTG}@)I-4jbbsYg2jvx-j=S!)B>yzqoV+UaddZgkD~^F<Z;@m0(o'
        b'v%)DYr@bRvFiPsaFy6RHIC@#Kn-nD~oWsthI)C~x@CctL5l(`noi;1EAqc1aoN-sa9^oV^ETYr2Ej}`O_ju7J;T|D3ddWzlqUddb'
        b'!KJy0mkXIbJy*>-!<Hto|H;b_@y@#=oxIqb@okPwV8oO`&h!>`)0bwPJ`YZ7J9O@JT|Ss>{R1YO@xFZB7+KyaXCm?f-D-DZmaGtY'
        b'bY6y=U`UELopW++7kY2Ef}R;3<fVIm&r54EE(+|ln%(1^S(sB@ue+LA(Ua31_*5HBRzIAHlNHJdN^@$O&(WK`=3jKCj&|G9%$m*T'
        b'oche-*mKV7jC{nNq7!BjA<v#0yk;>x)%B`8R6|1j6?V!08s8ovzN!Ba->Qf4jeiiI7}11_zmLc@oc%*QnI5@RwlnutyA+9&COR0I'
        b'UoYN#?v#wm1FDNhB+i0-U8t<$mj(+q!!-PyF-Bp0n{f_kbZbCdhN*y>Qhi2xDQ{9<6ox&t2<NC5$BILn&<4yN5TM12&B|3Z_Vdl2'
        b'H8TeDA~(Bn4{CvqZ-w+gg`Y`rj=rRx%n0+#^mFCAX}Ol@0);2T%EaTQ=s13Z&rgdc!cJ{^Qnp+dxJO{-<$|_ErxW8V$<#ULtnm-S'
        b'%>Cj2Jxs+P!&E#BGn#~Im~!FhNcmzq?C%n`TAnS{a6YHpa(^sp+DNBZ;=JpuVC7!+j9XFM#@u!)fo!tYA5s*(C&WyxOATjskENRD'
        b'N`whj-8A<T_4P4(nw1ZOp{vJri-kZMJ~;~imQ6}$5Q|ILp|zi^E?S>Y2du?KW+f7DTrX6rFm6v<=H_08Npw+BOi`)eWtus)nsv<#'
        b'c3kJpscQMTk(rNChi8h*&pKPf8Or|r$1e*PZ&}eS9xrq<$M<}raM8c$eARh0s@Pxo-^nrabDVGQU|u^~;GrXgx7x<3Q~_Xt+z{2)'
        b'd@`CYEf~kC9;}y(Zu7<k4L(L1B(xEjkN@w?t;;W%{wj!UZZ)yz3s`3pbF&)G)pQ6&>NdCtAzo0|a(3`iI`~f^rK~+)DJ;2Ybd2@G'
        b'vlfBpYcho~z~|zM-%eBO4U<k!QVMRAHS;e_EfY363C%;fXOd!P2}G}nZjHB{<AT0$N`0cTk_8+0GY8YXfx?Oit?)u??rr141(ruQ'
        b'wiqs)E>mu$OCWU-rxO(|&z=uG=7rjh7i&ABK1OL*5n|xHr9{QZB7gmf=X-$qv4o5nD~lWmAckHg(Z@7}>4}~sPcAqSrJH{uN&)Qa'
        b'gjsu-zA*4a)Eb~47=ZnRq%eIYK$mh=phduS_i%lT_CypR3Syo}4Dz>6MDhF;9)I`35pP{0^gr{wBH%<+k10$q2R+;srq8t_oE|3m'
        b'>@%qfp78t)xbs5XcBE(1nJ|3}{N_Fvrl%{=JRe0H4BtF2OwR?Khzfwa=KK>;*OC5xYNTF4$higZgY+0*3e&Hd8>ZJiN7HH46C+Iu'
        b'G17nhYO3Z}`@nxN!XW|KGwC5Z74(Y&X&!p`MKD((tZWU@{|RYW0Q?zP4QvC#A4QptkQ#JIi#(bbVt{5K*?{tVoEWZ+BZkt2VS4)n'
        b'V#q`~a-hx}PYm&}i!2Y*Ck;ppkvU=d<8XHlkRqIONb4S8AN0F*#E=t240T#!K-w5N;>&_rGr}MZ49V3Kg9RuaB8%LC^vIER*IYvS'
        b'kxv3OkwcBLoQ!<*fTDCrIO3EB62oMK5eIX7RhYiDI!qtuLG-Z;Q0@|0qzrU2{P!ZgJqY(6umk!!+8%)8zz|jzc^I@EVeA3jP0c??'
        b'JMkp?w6D=N7KiC4(6R-_z->FQI<jYY)Ig6!4fQx64=@1ra5Eb;3D5(nz$-uwuokF<{XalAjh015BAv&Pu3*sC%rN~m#2*g(@aGYC'
        b'1TlC$Nely1Q5T<~tdWlxl(QCj3ecU1%J1}@hH^B{LwnPYLmLLN;3oG4THhoYMVw6RZ1SKQrAU^+o;;t*l6}XeWMT+|W`V!q_}{}%'
        b'K)Ce)&)?_QAdKWiVS1it`Uy#+(U3~m6#**5QwaNjIMf|z6Tlzk`Q0;!!8nr`jzga_3wASUJsXeqz>i`P>H^?^RvPwfVpszl2Nu1A'
        b'{<-c%)EtB>m&zhPJ1mRzL3w1O?6uGbz>f+T11y8P=0BmGJ_{s==@ri)4D^di;0D^l^}A>XFQeT-eGQoKFUD}=Gse&h1i!=>a^U{('
        b'9AfafFEO;kUX>cAZ(oM;UmB+O`zK?lgxzVxkqg=k%!7NcUx;C!8Et6&iKw)cF#R0VQ{7m`Fd1pEAPvbc(ehpulkyVf4@BscH^GOp'
        b'J!Fx~kp3M22`3~Ml(F!9Jo0%BaV&%TEMOnp>5_;c9OwaZfSA96N5DK2_S-<^T)4h|E#i?X^l>RCqHe%{45*i<EV3W=JTQ=q_<!S_'
        b'Eb3>TLm6(P;RE^<nnq((u)8c$3iYO^Ws&j7lOGTXeQrAXE7gM+_9N_!jEtz^2>TrBAS0u6+N4QeMH4XHCWOWG(3Vuc8ae}-1!0h;'
        b'Q_aoIF>ntZ+6p=<p{Eq#fzX`=0$ZgDsh+ywSI^*ozRzbOy^>#e-nhAxL<)Y%vtX@A`(2(W;GAIy|I+|Z7?$w&g(Ff?c3Rd7hGZe0'
        b'0Hm7({`pNmvP*BNG(No#VU9e|Qs;JY`;&k5$e$XHa3=#_^8-A8<Xb)%>Sf4h+wc?mexcs>p$|<y227hb5`8q8n(6gx;3f@a9tZbX'
        b'w64%j<_Klz8iTwa^`dn_RMCa&D3y_>2DHP^iNWtE`YTm8q8>-cA{W6=CQ#{(eh-=jEJFP!0n4B+h53;%mnp!fJ`-c+-Bl0K|Ep^J'
        b'(>uVU*MR?HEYte{6SRbu@l${GkUTl%&OcCA7X3-YeR(~NUqZ~_3!MnB12_$&AunZRWux3K`ct>jyJ2=5`1F!2G8lG>RMa!{b|4t)'
        b'WXeB4m;Fo(I?#Zh!1sSdKe+*(55xgC01Q=p+3TC%%7U9Bgj0!rV5a_n4F>g7Kl7`jfTL3yRy^B&8+|SPMAR|hAna@4en0TjI-cJ~'
        b'q=sJfok-|I(O2p~uL7^^Li&7Uk>k-$FZ!ZQ_sSyg+?Pe(9s@O?<7APSVSe^g@Y|P9M45n4xQ~FD5$f2{A|H-~Svb_e=;wN<X@A_d'
        b'TNbHt@|PJf`#Ye5{Tg4!5D%EWi2e(heU5kn(05Kjy#rzGWW_#w7WxW=*@3vOLQUTi{}q%SC5tSCo86!;z)ZLq3c3h!jsn#J<AD$$'
        b'mYM@eKo#H*w;zKZ0=@*!j}pfWIm|}_en24b7*K1FMLq%gB;fwJEOI(%9IzjLjsmlwo(m)ae+FIzmH^p+_H|k08=!8_$|C0>Z+TD`'
        b'1Es*65scw|(49aPa2VJD)B$(zAx_lAGF}$h41M8H#*hV6a*RO_%yVN5F+dK=J{QOa+TgAWxDMO|?f@z;#-KxatbPRPL%U^BhH@Ym'
        b'>fxXxfH8mu&;i?KA-|xH0*?cefG2@yAP$%V!~==I^T10$8t^jk7vMvT@ykJ9r$C$e3y=Z42|eY3l>dE*_F$ypL;p7Ddf=bHCZLRl'
        b'0qg)Of!)9!;8Wl&gtHd-4C>E;2H;De8E6460GEJv;3L%K70_<rO+Q(r1M~*)D{vdQ56ED?MK^^}fO-Rdz(imY5DCNpaljlP9+(Ft'
        b'0WSh+z{|jL;BUYxU^TD?C<C?wr6_m(U0Gxe)F!0oC}<OK68JZ81?U0#0Xf?KaKHx$0wU2r{sI~gng(ne&KUMW-vIm@IE(NO0+*rg'
        b'1`1LCKZBY<`$6vl_knfLyP)o~5yk-8j}f$0$ruVj_W>3_<;NK6$6&mMd9o+$JQ%}B_}PZ`H3l>chy`NCQW<5e@j0lU2i73$d>{qt'
        b'3}7j+92kQ>k^}m8Adk8O3V<xQeFwA%*bHn1J_J4jb_2CQ9q{=hG@jr1W1vmIDc~&73Irn!?Vw=27ClQWT~L1u{0Q6x`T&LsO+-WP'
        b'(r~C-;zcCz=L!r3JScwvw7@c?DHBKol7Sb2MZodQ6H$)}`4t5G`@-M|VQa!t%r#!7yg$nj3t8bf^w&{_gbtPvL42U^!C2k|H}z1*'
        b'0Q@nY|1-kM0A2;&0bU1;fEidkmZmXfdNF7k#)C{?E7UP6@E~_WK7;y(TeyB4^pl|f0{Y=lM?>8QbpkyX|0>!O)H=i$0Q6!Gbr>>)'
        b'nj?Zt^a~&bpC#ZyyBDAxFBN(AjU>h}A&xP4@e)Jse8%7hdKh-UAPr>8T}j_*2?@F@A-M|}Lo>|n8>OUo8DnUo`2^<ug)xkM`-g<n'
        b'G)|x&IQ`0rsCd8#oP+(8o#;a-t2iL}dq^pmTb*j2^Rx<f5KRn_7oN;|jWG;R_rT<37!!dt6Cf`YLVkog9`gV>+-`!5X<5q{b{H8$'
        b'otZI&!|odV#KFw$2??TrG4z{hxWv#3H-34H!2+{pxSI#uK$s*8{S0BLfF9`WGz`d=3g~Y@y$<1|!43BhgbDk@n19B@ycFrL1{#3N'
        b'K<OsNu;(4da1&}B{7!xyZkC^j^2tV+pk|;DxDE_tA#b2Xz$ReMa@vM0QBNOxECO;<coE{O295()0Teyqv&8ZB@#V6}XMi_>&A<WR'
        b'Ja7{jxdQwdNCwscyMe2K`)jgDuZfT`F;2QdErpr@)!-Q}XasRc>n0!u*b3wVWFKRQ1f2uufgB(nNCUEgc{G1O84wP<NBzMM_t!A}'
        b'6sS+{!T1E6-ivYr^+9|AK>KD{<omGS_5;r!L)pfyME`(30OqHf3sDYD)9M{>#RX3kWaX*B8&M9huLlNYY(iWh$;yf9Bx5)X^BqOV'
        b'D-eUQnrYZTTqF1w^qB}J9yIuI$a|n(!RXtN8;z$JL)yQ=>wr0@8N+d4LJRmEFc0n)0qt8L7nOpiAZ_0Oa`@xUz&-3XUBKJ}Vb6m7'
        b'0K%+<St-yDbrQ^WLp=wSt~2PqWenS(PXn@n$suS*u-gaq9>56wap<oC=YaOZVS26}b9~G<$pF8a3=Gc#(2RSY?SuW6a`Yc)A1Q;3'
        b'1k8l`DbQJ<3qbz_x(@VN&;y|Hpw~g?fll5E*#|TpbQS2Upt+znP%~&7=s!RQKsSMod=I=C)NLDh7UGSC{#jru)PGVE(h9kFLpiMz'
        b'g}xQCGDmtaC+S&D%LQr9!7N0z?>$i-Qy>i{sCh}xYVH^G%Ynzq;rE0&M^5BD^iS}lQt&A<K%dc3s5X5s^j#IgNj?g93dGY0`V8m|'
        b'(C0yQNY`vYDx?7kLVNxT^w$`v!2|qm6V#n<;HXgVhkBD$7P(+3Av<^)|8Tt=<;tOqufnbuc0=CB*w0E0PlKuv<};vE>6!=9G8gK%'
        b'fNG!-X04#Vf+{|sc_PLH(AVI{YX~7hzz!tmb(nn(Y6ZOn+69U@lV5>4@I#trl|oK>hEHcGA5y5E06$EGc@*edptC@$K@&mSL0<xO'
        b'x1cUSr-Hr(nrRWrU$G7JD)R965rn)C^*N{up>72I81yX6K85-Q%Hku?dYG*RJp-BzdKL5~&<2!G0_d;MPXkqWqgX+o03L^$%54_p'
        b'voJ(#|E)RbcL1$RYImIWL*N|D%y2{Vwh6Q!ev%($4R+9ZZ-B2%WDSe9gNFeh0K0)?jBSguz}GRCTJtXE^>A0TDNNrFOwJ<7@tec+'
        b'+dc@>dnL2U*+!D=LpZv&qM(!QEFw+jdAid=n!MV`^HQoGPI!_mC6Q(VyLG%yaPtYKzx_P;ezF4QlYwxkBLzEG_|GJKR6kGj65_X#'
        b'uD|dfst^yW60TwV9C|vzKAyP)ycZ}3_5z0ipB5@7L=8|U;a|xjPx}*n6Y`#@BtFfcmeH6?8YM_`y@Zha{0;c=uRxmv;){^RfAW0h'
        b'6xNVQ%f~RBq=9Buh3T)uulWtSwjm+IF##mhlCE9emypNdHyM}%%mZRDPYrl2OfN;-tlWU~gOi3sKY;Z7(=~_4pQft=T(Td)0Reyy'
        b'%JWV5bpX{s58^9Cd|yL-2#|)N{$NI$Y5w?u;dISvII_u0_)Vkf3NJ(JL9$OsV-H=jqOwvCPmKInyRa^Lr5R~ZA)GjbK~Uy*5biS{'
        b'$s&D$I{4GUt{vq^FXiUP66)({ILw-1*92UvMw_S!(;I8U^f~bJ39ubV%0~IX{wUNhLcUP%q-nJAI|{<|_5R`dR)CNbM|mFOhN|a7'
        b'giZ7a_c6Fz4p_2j9Y@vM5ym`UqVN4%nEo1Q(w|wwRM<ZY+<;v&{LC}bbvzP}qK!{NI&`Z}M5zEdK!AR@^8r-==C8x_yMae4A?KnU'
        b'1%N&Ycmc~=!t}v#69?q(4AZv*yI~#&>;bF*B-iBYXeBy-LUux*D<k^s$}s&LplJZ^?}h2jcf<5P_rvssXd^dvqkJ(R?*HfAfAn}d'
        b'%wK<am*`Np69BuOOKt~l0M~(jpcl|@Lq=$Ng9wSajdDb|X@3vXpGJJGKrrG+20vT`H%UMi${@)X<2K4naSeSEaqmH2tprE_UGqK>'
        b'^=G(S26uM&H|@fl8#vAXJL*Z$?CB?>c6+--z6!Mk^u<+ltPRu0pkHHH*JrMx?Z>$wZ$USUL0u!PQn)XAnKgtXZ8?rG{e&E(3u&Y4'
        b'3zctzU%)=?tuTEy5R7mtp#K~=3A6$|fV>KGT)-a~paMJ^?_*Ws{GZN4uhH^=z7Qw^N}=BdY=ZhK5Ce4_@c6&LcY%OtF8Mg93Y6U~'
        b'u5~0=Lk@#_3@{J)0GJ5O0Tu$8z)Bz~FHBGKWZnZl3_r<BS;HmJOz0I*?*rmjqiktALjJQrdx1wD=@eFrBQK)9jp*a1Fnt!lA-o>g'
        b'XVl0dC;Wvqtby4Mw6SE`CV|X1Sp#_!VfCSo`%%Zh4nPVsInV_6EXIW<nC1M9e%oM^NfDFGj~(EL*VDB|FdncCt^wh%J`p9|j`*Gi'
        b'-GDv;o?SO2Tz~8fS>%dFj2ocg@^Jkem`kBw3@DlezPNWZ)WN{BKqcJtA`HJTQHFpW?V%1B;D15=e;qYJA~hJ{jt7nc=Ychd+y4aS'
        b'kic<-84P^_)RT@Y4rM`ZYF85dIkYut)QPB8*k$H}8X=DYO+ef`=rh1|s4J0YJ7^O6*&<*7>gx!r2XxafvdE{t{xz}}dSZfndJ=O<'
        b'jM=4rMDGqN0a!o*$bg|hiqBeR0^F?y5`p_a@q9mc#3<NVidlmc;m83C(#C-{!;Ks~xd${7b)_g_4GKzO=LOIc(my~>u8N1;mQUqj'
        b'{_Y~gp9y3GRiB`JpMeYycmQ>PKTr%LZ3C}-KTN+0>Ur;l=~F@DsJaaDIcNny3JLK;JRMM%oI@R*MW3{xT^tt1yy!)v5ErnfI80x1'
        b'9`ZS013G{mW03}cj%0hbfM24_>(RF@K$;qL4<ro>*XNd^ouDkaSd=a7&P9nbL-z&n!i%!VDL^FhrU$}-S<o*6{&bP{Kk!mZn10hG'
        b'^pjRuWEPMHBmr}PT)_A-+U6%bzbytl0<Zv^V15qpg1>gedm0!e3!w|*$A~eko?q=sIOvQRL7TjZJ{j?*(emw)BoCa1tZ^AU1E>SM'
        b'{sDOdP;udU`#bb|A(VSrgWqx1Fb^;Thk+e?Sc4bb^uvz9-2X7#%J;E`005%M>ifV1*vCM=&1nOVL405AEiW!Go6V$$kY$*Q$H6=e'
        b'GO!P*>Q6{t0z)<i%q(ez{%7Fax8M)Jz&FT$JH`-TP6zw|@+&A~Kmm9GKEOC2w}bY(pCOaiqx}S<U)!UWWMpK}r)B#)Ws%oA#dX|5'
        b'$P9ImRoa0<4f+r;8R}(_?=7I&u#fyF>XP;!l*d$rZAKn;puC@gdKuJj0?|;<16~KRpzryG=To8n8_<iqnL#V5Upv~G{eMn(9qcA|'
        b'gU5D@>5BoK13Ux7JI!dhBtShph_1E_C+9w;a&Qm*R(v11i%OaH*Tp;6or&7pl)OQ=zA@_V8z07d#+;4Hxhjj?MZ>vD-3Opd{DAra'
        b'LcH{8$ZI_EZU)_rytz()tYO(5H}VQ_#O0NUXTP||uU5ShaVfWPVf2L+B<0spOU6EW)^XAJ=!F|_Pt)`n!q%g%X&e#%xEfByG&*_n'
        b'5#pnN@zaoA;~cab{Wb7@K<_}ic8GbWWsn8+4b*cxkkrT;CMQS?M#$youFE1<_wqdbE>6Es({EDrJ9|IOeZG@L_5+IVABLm*UW{|c'
        b'50JqD`c0OutJ7}~bX|Yn58~X6e*2`9eq^NIu<3WIlQ(BB7nBf0Kv%a8pGoKBN9nhu%TV_qzw|pc{Z0aN>W3G<pWKe3-%x;hsE?je'
        b'Pg<ROiPZzpe+RqojuK&>sHk^c<TWYqBWvW~cNX1`LK@IBjY*)Lh&K@Gx9I6EB7E}_(+Tt00F@JLu&)Pw<~QhFk#718>R(k=Pt$Kz'
        b'Srs>)c(ST4ick>a?B&P($c4Qx61^CYihd(A{PNt>iJ{A$mTlkg^nq8~p59tEO8EZtZ20R@mSgWf5e&EC)IId@GcB?zd=eqv(~=G4'
        b'LkmAYI>l#2NE89)9158<?E8*S6ZftUPjP?Z5dDU9^($|^aX5GoFfC?E7y;zl-+s(EeCD(@w>435G+gLIL*5BM`ldAr=_+~}brABW'
        b'i!-YGvWJJ{-rTs48G1S_#eM&02=l43vNGf?E{gkwx-~wDG|{|9+k4P2PCWMb<i{`8`u-gL1T!@LV1Zd42|t*#tPY8?PKe4>YbLFE'
        b'?o!yQ`gg+*hM6MbIzOK}HcT1WGW5l#Ui$dG1JirAhc^X|p6dPbD^KnS+8YV~NXzgTo^OL(HumXle<S9|YhiEk{7vW`QT%EN>b~cw'
        b'^0MaY)as(BABMgjF#FA2Q3+3-wqy*giTaCb&KIYqABf`fNlC!WhNz*5^zVGs<I9##h}l<ubnCs&xf469qh8&b{mIQed!v?n``>R|'
        b'emLs*52eT^#suWiha!NsF@=$S^Gp)*O|SA4CS-H=pf#Yag43)v#vdaD_3{qPClyhie*WCy!&NnPmS4oVWiQ%nGt}E)w+YDnR$`#@'
        b'I{KY98!}D*3IJ|;;b!hlS!57U>gf_m_mj|dSGu?4F_<j_=)Mpt)5JjiHZbpdiJ|p7i9wiieaQ24Pr!s<BnEnflkPc@g6=?^*I>5v'
        b'SICCIP57$=@}aH+TmV;8D&2QN=Z<uJMS*@g!ObNyBLlTQUD#J}jDFu{Nd25<g-hheN|(q0;Bnw3U<L3#Pyh_hMJo|+5_oqh9hWfn'
        b')x(a?kBIoOnB5Kg;~xq7r>gK*xm}O}o;nS)IdtBgMd!~F`e8jP8EL44`^nZY{b5iK50}V^z;%R4<(+yO7BDzRq4SeW_@VN8Qj0iO'
        b'*aq44I{dfyNenUY>xnYn0ZQj1^qVi8i_p0ZosZBt$iCYW!wJ~4a7Xuo^wWJsD$K?7kW=FUI<9~CH`*Td(D@ym=jq@!8KC<tgnd95'
        b'_kH$Al8pcX6o41N0e*lA&;wFHPTfErpl_G|i|!w_63&-9>3CMnJqq%?x~8Geudv*v;3THTKH(s!;zfEPz!6!sH2oR4s+RgrN>5VH'
        b')?_UHHhqQGbfAy(Sihc=7(?@e>0L-6`}(F<S@QA=o9IU5H?+;ODE+IJ^WcWtKJKgexX=1Y-#CW*bI%o(>EpiNy>Y&~uXuN#uxCx7'
        b'^C%h8q|+GJON-3GDxE6#yCO4vqgr@yn!4TIXO<UMmdb<5<fT4gWs;dmV|vV)YX{%{R+Xzv+i2K@qwQ`)UE0SDtz@~UPYvZ>Fm0jc'
        b'oV<W_o<+@*`h`Z5!f^8n*Z!b07NW4Jjtu2SSETuFTb0L<I%!^v)NJ_bctMOg72)Q^cvbw}S0j}gK4E5QI3G@`irYBRdA76G!XSj%'
        b'4b|=y$-djx*RdSuSmmo>rFow)>owdc=ke+>J-PjP2C2(!@gD8;fx+{oPqE&$Zqcvwg=F<fq*L<zRV4oV1wLcuE>@LT((?QtS#XeE'
        b'sWjIzY=Mv5n%OsZ@go&BHOxyerS#F00;{{3$S-?Jr_7Z$DaiQvxzgM_@mn`0ywFEZe{XxS54Fe^NXpJuWQ_10FEcIdYw%YU+%zTi'
        b')%uSu_a9SG?zpKo1cWZTt)D5aU!ycgbVV@=V~ol$O;_vT!c7Z4god$a%0_xTyTakcdD0_#8KrD&C(l(hUgk--AylGTve-Sm+!oV!'
        b'#I2gOOGwDHzKEM4hQ5e$m%+P}$}N7TC|VEO*83HzYE`C3g-RJxw)7o0>x8~ix8|Aj=;Qltl`qd<&lk|gLIr=}sRPf2g!Xafn$W&#'
        b'NrQFN`|{Td%xC;(<TddJ#;~!EkdtS-hmtd_^x_A9v4<<y=btt!jq8nhsV;e}G}OX}`J{3~XEz8H9P9g(oA+g@c~%`;U@$NJsv*zd'
        b'<#@^0%oe&8_;cTFDGh6St!q?YYicbkt^Xp1b4y>znY{Zf7U`a;OtDvAxh}6rIJr=snYWfDp~qTXzTtC!4K+wn;h~=}Q#Il_#*M+M'
        b'Y-d{wwa}&+p^gaAzBq0dv!SM%iBNJL6&kI@e`5%L%S!t4{PR?*?5q;TB5cOaTb$?gn{f9QH!^jEg4$-NmiOFBO;nt6<y^Q?d9I{x'
        b'WI?)l3FlUzb>CpzmEZEqt-KKmeU<XGuy;K#QDNSaI$e5jN<m`Ad&7nMV^A>b3-ff+1DV5*NULRKOhXET%4$-UGQJrrzSL!`-N^;5'
        b'NK|k>%dgyu958BvOI$gG!O6EAX6DF^1@#5#TMkQ2=WaE#=uOkju1BN=TJy+iS-}+Z65ou1L@_|W@D*SBH7VC^KC0e-i*waz$cl97'
        b'N{^5g8VN#Mk?yiWLn=Mq(5~>1@0x=6a^}vTK^#}uzq`GWNE3!2bg8}>^Un<48D~0t>kn_(Sr6Va9lZ6sH{(9Nm3!B;|JLAs=a5~u'
        b'ICqV|KX->d1@CVA;8x4~x2oM8n>FVAkdJSvci##&mve5$x9MrZU32LsT*DE!iVrlx@t@EgB-r_or?Vc)0|@v<#Tgczy~FJkgP_#D'
        b'g|jpa(Zopq2fpAvmo->O!p2*AW45tW881AfS@H=f5}wVhmKcsRNL)rt``|s3S-0|7Rk^=^t$)DCOl5;cQn61BHB8dit1*Apc{H*0'
        b'4N^z3y7BJdednubmP6jWmFG{4RrPt6J3H$<O{=KkE(tf<lrvaHA=$Uk2t)k|ik3dWi#&xS!&e?!=a!sN^zn<E6MVOFK1FD{!P$Xs'
        b'E=SmEM%$_zJdevT72o?FakHl1;yfMRD!)R`eYVxKl!ni_b1}3?W+p^15g`%Lj#3SZJo;8kG>W`pwFYBA(yb%IyLZSthF1?yFM=)1'
        b'Kh<zjdO<6S!EsNW5py%afTm)4_EzzvThGW|b>;SQW3s+g-LwXj2gKG|PPk7xF#4JDfEnE3FGo+WJ$d`ousx^p8`5S4t_r)eqrr_7'
        b'9aL4z^HMxZQoPQjD8x7COw(xkvZ_?chg3J!9^GoC@V=Z^p4#*8Zm+r<j$fNExx-B^x2fJRy<9xg8c`Eri)hjQqT==!%Wl~w-fEe6'
        b'tK1skcbD@?eqCkI&T!A@KHj_kv7v_JJwHnH*YoZAZ12g8WxCNIB{LpP#iWbGS?N~&adW@8=Du?N&H-+yb<C|JLmPIGbXFbmTd(!E'
        b'UW5M_ZiHd6zcyWM9eJx_jXIPi(cZU0k9`-Mo*&|cmK*9nwwg_ip_QfX>#de)G#WG&4c+*Uz^^ZK#uKAB{gXofC*f?s!p82waZr{0'
        b'V9+t0?=3#to2QGlvbT(8**Xtl2mLr9m|YR#{oR#@Q<Au;VVfciZmO`fiRBFn({H^fHiHH&TeTo{r21rULx5|oCZJs7pT0pYDzqtT'
        b'+Az}3@v*{Ay6F1e+5l9Qe|mvhRA^sPBZ#~J`J6Sz7)8dKuW88LG~~t}8gCv;{BEmv_pTEUtKKAXy-HQA60Tqno}tkwiko|jGz!6@'
        b'rm^37-+hUPTj+LsaG4_TyTEdU@vG^*-ktvRY^u4RxY5I*B`4~+(P-H80O-_>>oyKGdz6%uEk0A%MT`yXkAtW5I+aic5IaKl_6D03'
        b'g2x&p41GV$M;WrEH>~tRHETK`r1vIILN@h=`umvnQ9bQLbW{uZC(Qgzdj`$EL%*_-P^;I3X7P3nQ#rK?O>l|y4~<rFo}tm>L*DH5'
        b'WM{@p?u2abRgl^7{&!v{i7MrI67qep{+fi13$Ia;@d@wu#tZNB68-lH@Ac~S*GP;~G>NE*F6|As=_e^7Y+M>AiBRTgVgvovfs>X5'
        b'dMc3Rg5})wg=!ZU!g<C1z#C1}Ad%iBVa$`}rMMbW*wW<*=H4QsR8grk*Z59~7sd-t#*Hqj*r?dbSo3<taj2RpsHtdES1LPX+=N=&'
        b'g!D<8jA{QE(__r1Vg8NYx%PzV|IqdAaZOy=<CB>rgfMEtBl5D%Ob7(THW^eNwYwx}M5SGbHKMiqH9-*Fc59LP=+fO}Xk(ys7eiIB'
        b'x=mtHK&gP+`l?;THnlG9TJ7$(-97+`2!g!q3x)ZeJHfX5`+mOv+~l6Q_uO;OJ@?#m?%X*SvuwYkb(b=FnMsTl{towAkOV501R30d'
        b'OoO(>jhQ~+x?Yy&I&D|d<O(nD63C7%%T{D8ZrI@e*P?7in-|MioE`3VgV>&YO>YojnagFF`^u{`OI`8kz7lPnts@w#@;0pbD9>HL'
        b'*#FU@i+S!d%JyT*!ad4bMMi}eYzm>;tu!zA0m+U*AV4>PVg5QLZybWXtN+Cvn4yXdGlL3fUCtdc#!FyWlgghH?%&AOo5C4Bi>0Vi'
        b'_v7_j!YxsETC?snI7+SxFzM%+?g{%+G?2Pq-hlzi4VwUQ$&H@C<Vl&H3IB@pT<HYn9?+%V;X{*s%`ribn1UAR7v9mX(vsyNDMiE<'
        b'Z%_skuOLIfkN`>1>+Y1eIn(<#uW-Zm=oM{o(TXQwrbL!~#$5En`aqIol=h?Yc5Uh4wT_Ep?dj!%E1BbSGt%Bkd7wobt{BId@P%!m'
        b'`N%X=wbay{3ufYfeSXdzKy7%xYw4aNb4F^zi|TOSV$2h9r>Ww=MfS6<13UOw7*`tP_OHg<jy>4q^hQcsnq=O5sdGc}=3QrS<0Dw|'
        b'@*`=uZ!N}N?EV)1WMixs+Z82Y--Hw|`XP-+vHS1i$dagI<5@D<#>){KC55HYX6pq>vNZ|a@7A;&l|v(e@95YyQm+tW-Q2GIxbH!%'
        b'@MYyyA?EpHy!F)h<r$xO?4OOJ8N{PLHBLSN$QuRyRAt?1g!i&Ewi4u#l(HAUpOo6B%54MX&hUQy54xVinCm0ir=DGZls813-VL(x'
        b'k==h}(Wjn^_EWnX^J2dzqyC+SZu(e^|2qwDe^+^WezTykMrnBeQ(qm@CdvDcoWdPGF8R!^4BVIqy}tU61~+zaU5DhYd&b$IMHx+3'
        b'n&cqwO-IROGRF394I3?ey6nnXdAk$cFP(cr=#XNlbmdQ_ZU1NK7GcLxZvFi%yH@Hr0%V}-FZ@*9{(n|)6&i=9%m4PL^6dXvzD;Pn'
        b'9+3ZLf&DV#F;y_G+cTaXiV_+n2Hk7p=_ZsgDCtSlrMo}{+ApBe>0Vv+xE@Mf)%|JQ?bU-t|HpB!Rl-<*rF(UpvF7TkAkE`bldfpo'
        b'Q1GDsm2rcW(pN%C^QlT-0jZi#<MmER=klpSZ-I2S-Z7rH8~)7EzXa(6`lld`(X){Lo=?N{c1XkdRHnB<D(BNs{U0DL)Bh6E-|1h3'
        b'bSIzwMqdW$(*~N&1rNr`>VF5>C-g5sx~ecqU{Xcub>po&#@7h-+r~+$p&(K%QgmjB(Qcf-6I1LDW!wZ~{jKgf=+k!H7D#ubEoZD-'
        b')c=D6(>=c(Hyt1GPlo9p8MhvP&zprYS8)R&>3(`Vcd?B81~r-`F%UA7K79RRS&n!;0?0_AK_6kzD-8PC*?Aw&9bcwjwh~}@QbQhT'
        b'SV`(9#&)k6C&ihi$}Y2f^UG**?P|y-W80gQjoED%Wo!&SIyPpjQnF9t4dLHK<Bnfr&ZthwvM6sbws}=d<&{-(b{W?8fsDOmsMz3L'
        b'EI4zrBL=fC9$&lKRwX;1HQo;5_9WI8A$@v>?G+jM3KG9nQj-v~&m3Q4Cs&Z7ZLg$vNW#b5+;_3s@9iJH5q~jzFxDP4-m*%*_Iu|n'
        b'@2`Z*o+bUOYr|l5d032Ipn0voHJ;&OR<ReAF-3;=HSrGI_z%v0WsH3L<K*$~#PQZdVDV#;Nzt}H6<*macW-O&+Ae>g)HPd5Cb!oq'
        b'U8|)#BFVaavvK2ctoQ-50;_nSV<u*G*KU4#$L}^ttP-+wdr63L<38M%iPg^iVp&NDxpCjDu1)g&MO{Vm&A;g|3fUrIOlQaAnD>%^'
        b'y%^g{j(f!8>L&yq$#`qXxIv1ULNFMVOt919F!ct3`q@R6t79fN2Kv_^7H)qH7pGy(;`%7)ht;PnTGFq(H)a6cOpr_W;Nl$2L<r%J'
        b'?{Tb|C=_zO9JDLb@%hwPGxuGU+BpZtU=BM2je!%5!DHCk)og^+(>%s|U{djEkgKBo^PLYs!3Q?4f--AYJD0R}k9j{pQ?z1<DMH$^'
        b'N@-e)n`UA$FPlDC%RY{+*&sfOzVn{I#f{wg{bT&#;o`#_86|G#R?o(L7q}gBI%l)b2;4>Oh!Y!16w>pZV=i|~`*vlCS!$hu#cbPO'
        b'RPq?MN#Z!g8RGHX7soO)7q={yd&S|^i<K_-)V}?c=TBoTd*tpq+s7SaL&2AYV97_<?XGu3*Y2*$Xbx6OIF~qldlW7{#kIaP*5a3c'
        b'e0r?wmM!yrCD=D)wECrJ#pXdnn8c+J15U$AiLaT1W#HqMvGdJiLqy9_rQaTH&KNWiO5o|zJzCw-F*4@k#<BDD@VGfdZHtC>2><P='
        b'`d7i;!@y*qJHAB@^Ze;RKnxMNG_2cma7_FyH@(Mma12ya$XasmV>pSgUbr?sI>;)-7Kv6Xenm>2l8|qZN69(l%x#qmk~VaRF>B|Q'
        b'_3KMF{&K$UcWmyHtnC%A>%%LRFF!M5d%ED6nIX>o2P%tRobh40;KiA*25(*+LwD{e>)FSM>If7R;%E1&lbikC_{XG(gfc`zYuVV4'
        b'^h<n_NG8$E3!lY<|A)IZ<@dj{Y<+(0AdxKHR{0=Uy0(|}m9MZ83}z|hVrZLf{&Ze2w~oZ=tV}-Egl^Lq8Ojn^XMW+b2Rr%CKxM7U'
        b'`tQ`{Bu;xmiQKda4n>Wg=EYh>$jD3bUC{(8OG?RuWm8996Oy6eBD!#l{pgCVrS#;v8EqfE(b7`->dbF{gR>tsw&4QT->y`*mwpJI'
        b'$=}{+Z!bMK^V_F!*WViF(tES-?v1+J?vyv3KwA+ju$U&_00(w$GI>q_li+)<b8X-oaIEb-y4tSrHmA5Wh2pAdl&HJ2ne)oZn#xvJ'
        b'FxD1=#W-8)wAIz6)wD9;m6Y3*rH=dYi|r4i4%m~&oDziwyYJ6axFvZ^BR*iFPL6ux(Z!@~=eO9ksOVGD_-Niiz>@#w1z<7)J|?aD'
        b'Jm!VuzcmNhH7IYc#28xVi5m0$0<%Ytp;+7!47^&!)+t@&n2Vavhtl3v_Zb-+Q|VfaeH=D+K77oz9GjH%oZr&s-qI{!E$RM!nl|?*'
        b'(PyEV!cRGtN>@})=tIW5)Ph>!zWoQ=+@D?+ooQ{B6!vk7f$zP7PyO^F#oF)B1%cl@#3{~v=MjvR-9_K^t1$bYMo~Y%8%1{pfk(Qf'
        b'^uYE25qsA2amZO}eroNiG+|6iy3jK|YG+aTcT;s^qxz9iCs7NQd%DY#W*<fHe4<eZ?U_Chm<lla5CXZVG@#J60b>jJzW--b@$X?U'
        b'2aU%$j0_4~!-nov7~t$ZqpSu~<Rkg{F-D;OCTIWhf59!{*3U-CMM%&FP$P=y8TNkkr;3-%)@!4Ss=%^HN1(?9rt@j1gy1rD^F=RB'
        b'u2{Tu&(Na(0OUdd5~N(-ZhC);JiL10b0Lepo`IOQ%fjd;dm?&Fdj_KEHt$~myxef6mBgc)=*5`7ol`6q(o}QoUlQiaJSRsnJky=I'
        b'yKEw}Neia*fhI#o&pY!Y3>^nz_bgo?%4->2`p+Q4@!v0}zqQV=w<E-z6Y7X?#pic&dgv?+UA2Z`_S5J=e6%0UB!m0$)<dI)EPg(<'
        b'p$G1@%E1Bkhul1AX9gK6{(#d*jCu}?TH|zGV$5T^|EG4;0Dpv-DGL+7%eC$qg`RqOR!H;yFlt^NY~O)$)bB?PR*d=+N(-q6z1~lf'
        b'L!z4s|3VdJq0Bi^bd&lVr-qJ3|Ioc@^!&@CZEp9MqGo~rSq<<b`YedkDd56)ZJq%y%0u}x95p)PDI2xYh!RMfMTnxEqb2}|FyJBl'
        b'iEe_wo@YmC8U=)f4vITL3JfAl@zPl9v!fku2@qU5%Fh>xB@c<FL5#slX?|&>@Fb^58nNVzb}tz{UpV@u2xw|XA8hXs7Zzz=X#?us'
        b'1O6xmhCEA0%kJ9$JpyP@&=T?Xy$_m1*nvIvMWbYR-Y<Eq*%%l*g;?I>qsv4}gVOWJsQnVEpt#dd{dL6i_%w+m?%2z<t{5fDfUw7T'
        b'!Up>ENjwT6B201ThJ6`=doAtej2jliXtvn=7r$OL`a7Dx`2kb_Zm@LN;{(H>n7AHO2`~w3Id7+UA^g0Dl(37jm>1aP7^n*=0s@yG'
        b'lfq2K{dJ(py6kbIUaHwC*#&0SAGna0yq-USZ{#cEGS>^u|N82@dK5-tGH3`#gH*Um(?*>Kz3gx16w)tEo`Fogel2xbcn(L`7uJIw'
        b'_|NhZ>r$*)w61R>f5mF65av{q#~u-w6`$$98$t2F?GD5eY8Y)x&^Yp;53qTIBUY+|zaU{_1TId-ER!So;+R!y#87@G&%%y>+6U1e'
        b'ecy<EYNS}0*E<qZv`JVjX%w~I8$pw-h+Guiv`J$B0Tp{uYR(7(C``M*p?uNWLaS$>&HG7o5gB`?)$1b)_j3ncuzrkN#h)~b{r`NV'
        b's%iaUrTr6BxFid+_(#&jAt~wNG$Euy^R>(ABFDWcY_kbQ-Sk0MZf@!7lek02#S}R%fVk0AyYUmGe4v%}78@%D!z*rkt^7It2%v3C'
        b'(AA$+fE8`*=cb$RP}`+J<X$VldeL>&jW`NdgLG8hTO<0nMoQF}H4a=!484x15LF24Pb%g~cZxO%e~hpG=7{c1;6y$_f`nHHD+vFa'
        b'_&n(*KGHRc{e5=i{Hr6RBsq9nh1`2l*3^tb`$@4&4Q<O|xgyCn_Xe+9Xg`VQu~&}lZW(Em*dHG8YBC#xcfSR{$*$te-G3N?+)>Cy'
        b'x{8x`{}JUHAs6K;j@(^=a)(D;#Zl9HyY=65fqm&iBVHBgQGs1BqU=y!)jUgv_@7ggp-7`92I$jG414yE7*uJXTk`geJR|k0VIsin'
        b'U{q<%V$kXQ7TNh3BVdF13)JrAN^|toIq6l^vkjulc;PC*=8miJjU#*Md<B%^&^_CEYWqtg?j)tR_{Vo|<s-BtvTBT$JbldIlC;xq'
        b'ETJx%cH<*1c~ae#M0qvc&R@GnMzV%T#u~;)bpM{;^C87xd_~L?XR6WN&>O>_J4Yl}dEbw<zcUO>i>*2*Ug5D{NB<c@xJIx>$Hs+f'
        b'S7~+s7(NxQb$Xe&Fq=cKb+WpGk%l+`To%~af3g;l$s$xQpw71qf7}Ko8{+&i)T!`}IQTay?s*gYQdpQw@$fu~=am6hc5cXarM`x?'
        b'73?N7Vt+I6v*`qCyf!r5<;0;Y`}qrCoO}eT)>Fe|a3JJJ;|@OXOCS^_e{W&_bliyiAHxAkbdQWohbam~g+^}&rt|g%s6}XPFKP|h'
        b'i-Gvnu3B6ZdWD4+QAjU7+Ngv&HmnTbmXJT*s|C#KLfrPKM@CqASDn0-9!YZU-|q?*@t423vIPK7(je;RPLCU^!=u*7?X#h@CQ_Lw'
        b'ta7;|qO#B3buw4BXgYSMeB}N$6wXMc@{Y}RXBQJ>15K&CGiQXpDnu{X7FsY$GQwYrs@b7b?&);#F<4@%Uz>j*kq7=1t_dE;(9^gl'
        b'hJS{;8sVl7aY>q8rv)LJ>gguXdzq2pGGu=_qxtw8HooMpn3<K8v?L^^!p6r`s)**}gy?PzL)U7F2L1*X6l$`9zk7qiY_>hSq94%p'
        b'4BNjNPK^rDbr0LWgg?0bi(!5k$Y>u9M&z(pWABn;=BB&+#mk7!7&?UYf(?*_^7TJ(=+y@wZ&Z6HBt?H^7=D-51TI2GR(bt*T;P5H'
        b'`=w!}yVNP+Upn2NFCPpa#5Izt;JQF;S^LRhIvcm28m^VF?kzT2MoM;tK0tSjkQt-~EMUZ-in3cax3Gnl1%jR=Rs?{b+w6KbEgNyl'
        b'Z7lzuse+ds3udn$ZjjjD8s_i1eW3cah<FgPhT-^h+<s&@(<N7)ZV!3AvaY4BqnbvM=1#2zL;d`rVWqRf7WbF-vod8Mrpa3V8Fg?N'
        b'{0!w;S-VqUdxdWZJ)n~w;P1`lht(;d_6&o4u5`*W>*UiRYkrIzMsI!~a2MZ;!?18OA`ywtF2Id>7)dKrl*|&*M#!zeD95mF+prU_'
        b'4Xq%Yw1%lr*-MA(!V**XfG%NW{ngVU)54|!JO4kx(?9$ipmFZrI!s0fK#5Lup3+MQW10$oscaV34{=U{{D?1A9bl@H&$y2N11iJ@'
        b'{}-_Av-?P#s=+jx5XPRVYKy%T9~wk=OvQe#Y^dp8GkkvSFgc^`O%y~;y_Iqj%rQQcS*@0qG43tXbG?=)G*Xv43}D@_hPBgCY$5}}'
        b'<8p@Ymt#Cp_jL!YxgX#xjTVU*cP8ZMB_b+g_#7C@{sZ9wIZ_XU=}8w0{9kjlJ8<_Qwez+oZJ4Eh0|Mwt9j4(Aj(HXit8IZg2XTAK'
        b'Ff||Kw>0sh`6DsK4100Gyx=1zeobkIyK3Z2wlE{T7Qd1r&!|gV=6w@$rzq(tY5ERtl$6ewx!=;0p~@yL6+aASv@%7eY?8YVDI0fa'
        b'HYI8_Q9y4nmRPJwOw88QCFWCeh7)U1(!j?zC-I`F?>rI1Ua9EFiQ81<@RdWTJ#9vN1CFk;X`-X0pd_Ig_@iZ%%7^sIIxQ6fV#YTG'
        b'VpgN9+o6#{Q_;|rl!T^|psCH!lo&N78b<Ntklfw7&Ei6rNN|n-`)}W=U)6@ir!VI(2EI}$_k45v>QSyiT3sDp*#utml{&Qfy8fb^'
        b'jh0?<%G&uY)(!$~OUpXtkbSzWJ@A5kt+Z->GhY9C6kw-C0x~=yO+X4W1Mi;DyQxr_3l|0zhf`nP=C6JMRw7NFUW_Ix^`F~UD&*D9'
        b'c0QyuKqZbJ?(3D(FTB)0Zqv9R;e?F3d>d_Qr#bm?NLyAjXQU`}g8C31ixN(ZQkQODDVJ;0+MPVx(v}s7zq|hq&sIvEyA9Z^xB%AW'
        b'ji=0A#d2Gb&3^j!l_EL#X|6+En~R;sUBQpqUS6E(l#x-*c&4-6)>xjKSffmmnO(U4=8);wgG^jFm<(Pqrk?pAqmbsN$QZMfB+?zQ'
        b'22aN_!!m7)8Ka;jP0lK$u44~YJ7wr160?*MW2Pbr%sJ+fb5d~qryc-2^}+|urT2V&{P@KFU_U#QkSOEht$}Y=eg6es;N9BpFNOda'
        b'z-`J_@%`9Mx?Q*Rf4mLsWe7p8a3b~e!@6?BWJZNmJ8kIfM!5}iwt9ktGCcDU>&u<_wo0M9L5oQ*Why7`zcVkrt^ZvBmuMPSDH@wJ'
        b'0!F868Wmai4MG(dvabIV7a18lvD-Nm2*rIYD<KKJE3HVJGvYZqgeLhKw^Qb690I*Pt+dw|zvmK?&>C2g?)ZkoJRZK>CRFZ?pOxEW'
        b'<nPzaTXx%v3rj>IkYvk>+uP6NTtOElweJvj@%z2`E&_8m3HL>7ypht9qa4hZElslZb@CDkS-oHB%9l0=fuBxBk|FL><?#Owr+5j|'
        b'o<MsrYFkvc7}RsNkPJ<oFCg*h*QoruHTO2GtE@z%Z7JQ=rUbJ@>1?Ow-iB6d@yZH1QVJ|OVuhN@v)aO8?tc7j7cH>Q0Z~P_bh}gn'
        b'`vbRIsoQlD`|R7XRdlw1Ca`7!oh`Db4<Q>!Q2$0$z&3D&%7F9(>Cjn9aht!Usezw8l}xdCULYnpNVZ*e`->8nM6mA!AEQ0Z9&#II'
        b'iBl4oCqVA56W;}<hdt<a*YuMD$M?M4*@@d^h^;}{;nv!hq4sxU0I0hJcwd#CbUm^Ahap!mpkBe>g>+@V+;eBBLAt-GcKOLosV-1Y'
        b'*+N&oj0~&(bNH#{+B&VScL-?Kp5>L(>!6&{HlLHEYto|A(-<k1UYxd{DHhEO;rHkeU%G~V;>*`V%>rP{7ei!lfGu@$U<>udP#u-1'
        b'gP#gPqQ3C4sDQ5jYzRidDfw}m1xAMM7@gi3n<uef9ip=j2KY#QKgiN7N!$LUS88MdSmEB8b`lzL6+h0O<FkJ_R5s?4V6DEPYFZ1('
        b'(2!vE_xT~g>uZADXV9jh{X7D+z6X@r-y7nOY=8%^oWa{1`mY8(XNKrF<bvx?4{1`4c}cM;E?kq+CBmF5chLEUP4p&11Jfx<TuH};'
        b'HKJoH4T7#9Y)y)J)g<4qOl4`VyHsHkP^Smk(ETL7uUJZ59Hi-GP<Hy9o4sw&rO8>kb4IPnt9j-~l*m>5OntOGVEes31jJ_(d1nU|'
        b'y+VEUkU@Ar@r2Nz4hJVFo2ZH-#hVDLI;=~K9qT2<B>)e?YF9erb}Zf$w`p<1{LbKID-G(f3PGbBYBb2fYTU9EG1xqN(yRU*n1#=k'
        b'4?QEz4m$FhPRF8oY9P>-!k~~0=kHs?^zRHR7%3eWWoHnF`27g9hG&6}%vL$WmPYy-gUsQ=5;v9|rg-fx8;7lTw%>?sVSyMFigao1'
        b'W6s4DVTh`oi+9HTZ<?F}C?_64K~{H!$L!)mmv*k+0VSa`JTL@p3hoTgUM%*5vQ%j9)@Ca{n^;;Wu3cQ0?Yqgn8jRlK({YjFe+AYX'
        b'%80ts7AmBk9Ber)RNNBSHxGJN41w-#bED=uLZzPUAu=Q|OXiF~UQxz*77qa;G$sp&Jeddu8!6m(6ZiaL$euk2eq~3b)V^rwr}I@o'
        b'1#|3A4AzFSnun_25ZWq)yXr{Kf}uspfSLJOIsJ;kr*ImU9I#g6he+I&ge%*W33b5+SZ&bpm4gyZqI215SEwdE)rCUSYoa<$o&Tvw'
        b'0t^0Ju=(cXJc;oRSFwV`oof>l6PJ;pX3f32wfuWen0tEZP>1_nAP{`66@$n)nlaRIC=IB{Mmfup!4A(Nc#O6zvJixtHKdClq>G~H'
        b'qDTtLf}vHkf(ikS&_y|vbf}r2i(;tYp^|GjUGyL&8KR5k@F`6NL8{`@I7$p@hW%lLk@V&T4J8s3K4dD0%o7dK1<z0z{Ey8e;C~oh'
        b'5Kc`EnhFx~Fvv#GU<VaEYbvl)+QGcZ!Njemg2%zgGacvXrO~F<!Sv$&$n3ls1ZiRZO!QwpMSVQT9-lJd7}#buK7g#rz=!zVi_*f^'
        b'QCeRo_Y4filF;>FL>8-3<#h~}?W_>7DmJfo&}J8!3RG9}<tzwtG>UkOj(D&J%(VE=He0FbxL|EQ8Jyc#<6Zo^*Ujbq?beZ6+Ic;<'
        b'URkF{d!TONNTnQ{qO$*ht6ZzMH7UIY%mrmd@5ZzuDxL@(yws>iRQ)29rG!|M%63YL2ulrh>J>>CE5%s7fOUuP{{`%lcfF!>vR1xG'
        b'Zm4-J#){r$mz?to1W*<Adrhd@ChR(e2rfHa9e6`-z!aC}l2X)4UTEzlGO}t-!{=nMyP~|SmM?f_`oyFG7{KnjDcgN?kPU7Dv)?J('
        b'-7v^5Yk@+vn@fn4d)$Mx8)gMYFRrzF5zFiVQK`I=STY99_Gm;|b11EvLrT$UE0wLv;MqOMAH1q1qmW~V4pq^rD0cAyg$bi0KHg=W'
        b'$p%GGrGsV-Mr|FW3!*wAq*cc}zd>`z{xoWYR<Z0MEJ326gM!HwN@aM5TL4a)*ISAD{D_>5*Fh2UO>BEf2&-BK3xj?8AX}tcT{4HB'
        b'E!l3J?N!Bq_HrK)!h~))qxEbVv~T6*kQbQ+GhIT$xmfc=)lOH$#~tq4?VAKSo#%p@g%x^x`7J0{*6$VWcj{dm!pv)<T<V-Q_lD}d'
        b'qUu-5D;As2M6&7}mwSWlWsxlrOp3%O5D(Hrs|L0l;Rh-sR1?j*H&ig*2q_tQFv#tyX+}{wUExBunX}c&wt(Ld2m$+qkd63icj%xk'
        b'q5M@|afS<(PC2+=Hd<+4GKe5g2x&=Xkaae#&UGE-l$3BiE2qO}1<KG*%t9S{DcI}Iv_BGH-9li#SDoYbh!C^p3U;T!h$+0m8Ngn2'
        b'k_P8z#ZWMM8WWBPK8CnbUlhSlCuu7+=ur=%|8GRls<^6>Ehm*;H^z@H8#KmaU7^s3y($L5)H&bv$n9;2Yef?huUmj{eG3x7_F2Qc'
        b'!auX_U9{Wg*3>lP_G(nhK6FcyUFD@!vexHrd4_HU2&x~Hz6(nrOl`+r&Seq$6GB16)pJ7;$(3>!C4_lZ-6RXlDRCYL9QM5qdfmOj'
        b'_-D{_UeybrA{1*eH10`Cv|+v9jCa@X!UF5{N4Kbd++u_Wj$KP*%-5u82FuWZxn?FUJYZ(z)W86PpH3(c=>~5x)+Hnkj%Eet<Im_d'
        b'FkgJmxUn``V182E@`y5@R=kZ~P&KH}5$ZQNbVuMt)5l-ldWv{edX9L8AZOQV{vD;Q%|7;<x)ledn>3rU+gF#jSAh(C@t@AdDp7?='
        b'ac!cJ5f5;eC9pP)bJ(LnU<sd-yh_%tK-cP`WvyZEIl_JkvCG%RVL*3Y$3W*+Mg&CS;wu~(WL1Z!F|e}Nnw+ZQtevWzSq&+j!RaPu'
        b'dhI0cubrD1vtrVCfiuO2Gqez_6H>B6m7i6is>pJhppFFU#D`7SK=z5jte!NUo{o`gZ@NX_f8Uko8Bk`HdeskTwRaGg-K9&TwI=l('
        b'WR!_8#rpz9jQ}G)r+#~@_24ZU$I%fm-vE$s4ljH-I9Y11x%K0_GhN{=@IB3^2=HgjD+zn$0QzD;GY9R{Nw5QLROx^>be$pt9VKh6'
        b'yoFGm;879vNeGqg*3Z6&2tyeqqXYqnPYS75hRl<qH{|s{1on^5Zyo6P0%yrcbGFd_>w&i89Q&!jD|ypJMz~+mq8qIGW!0~1KYs2O'
        b'cnsCm^IeZ&E^>BP*Zk_UTBK5&ls4OZw|joiV*>Uu!u#0$^Udd<8t`nm1*kj7NKo7^sh~{?K18WkN_;_rB8E9`V`bGYncFLCX_HZF'
        b'Z`tb5-GSIya3*BCSKmT+Z6yiN2OApY{rkF}xaD=fM~0AdE(V7*y&95mK;VpWee`|R=F1_r%jM>>sm@6I@>~3t0{=}$$1sV1n;o@#'
        b'=`D1XLa-*PQIIHaNYtb^f+1aL58THGHn0AcXZHY*v-=mYW+_^KaZ5=rNUmxYbkTCV0&zBps>P9`G422SYoK-EEiyQ@P84Wszt;;x'
        b'?$nZ%+bU(YcA?F#SFFQYoWQ?3kB-FD`R)XKjHFvmNs<N({pmZ3w56R^d;Bdj%9Sm!t8Sf-yVW3RBeA3=7>*c$ONzCuP-^SitFvpA'
        b'uhiIH0#*yz9E@2$UEeMo$jvRaM)n>!%trb*J5x`ES;B8M<He3IMd&gmm;uOA2K{6SxpgE$>W#-T|Dw!j@{e=1Vlw39YY#3@Awv~!'
        b'PiCaEgn%J1n^O*cI(U#IVN=yOMz}K<E`7w3*cmIj1n?{$I~w@<+>QR+E2Y-iy$2ko+5XL|65f{QeLHYjnEyO_g#zM^S~a<`)pN*m'
        b'!e-(#dHo>wsr)IaeQ<yjTeGp{9nat&?p?AxMKME=+foXqm3o-VJ#{DMaQ$s=ch7(!SkSrHknmjUYroKcJwS#ri!t3-18Ky&TgfnX'
        b'b}zFGdw0h!CWTohGzMeJz3tUCwzgnop><fW&*X&zTujlY@{0oF4bJ|L0R}Ag@w;TS_;aMNNQvk2Kv$YPBZCRU62j!{MFGe-0JIr4'
        b'fS6TN$aSuyBQb^d9xcJi=y*EjTPE1-9rG^3#UF84Jfn;^pd)_XWrX+xj+PKi6oFj)BoEq*TSNH%$^(N%KLMAC9A~EYDyYVRH2hwe'
        b'Zcjg}+M>JDzw1Ph?s&h}Sx^z07RnytQco$GVaE5P^Y(bv{>wz0o3q!WtOlR{5F~Jp1>t(BpPbLo&xWLArYQ9_12HN2LdN>6LQU#i'
        b'18tsD$(?7~w1<@TLR8&J6s5i3tO0WjE%i%G*5Bs6GGMZ9<<ru<N=TpQ(`}^4WZiDE?#L&q_T&p$5oU7FUL8s2l@EADnE%(Ze4=PU'
        b'w&qX+S}iq16-$-%lP_q{d2-Lz0kR70$DKUALXsfEmGh_RRn&gp5$Y#rILkY}5T2XSEP^7&FF7oKtK#Lm{F75cc+xxr<j2v^VXd16'
        b'Jii*S=b-7wpM!?}J_#!krnnHHe{vwLRB=sV!UYFb<vlR~bwy<Cm1ZUAX);XPr1csE42~bD(LIKq5ox6z9$(B^GWw_IID-@Le93_K'
        b'&`DH)oRL%2boQs`1cQqdH9}JTsEAasxF{qgH9zGF^8MLE@mHGUl}+}A2)D#pnp5RIYeR}TsqA|!EE6<}HcbmvY$-CvAbM0BAA$Rn'
        b'7!yjodq|f!Kz?8iC03i~Ua6O_Z5nBkpCY`U<HgW^Y%)S4#;PXRP@?Px7LmEW$Zji=SxrR9sv^-v1{WS9bV2<cVg7dyc*A;iis`<g'
        b'YCqB~G~hTib)XlfjRDg~4x|a^ro^wDmo790VNZ!2om_`OD29d95Q>A;m<uL>5m3^sn$*oeb1Vf7mM3HYE$eQa*?<+QNC$sXKJ87#'
        b'p-G)^fLvnvzJCpo|7L?2#_GUwQn-vDtJ?UFlI#;V(YW5`&>0oe2b`$@GcTF+eBV#b^*=!76Xxgd8TotDsJ?!d#uTTp!XC~`WA>5$'
        b'pVlnu?>AZcw^Vn3d^S$q>gU&~*qaGyLA(3=$;gDyLg<davu?pVG=KNv&-SHy`kj)hT2~~N5G8bGJMMAwe!P#)e(h#$vHd^&RgH9U'
        b'F7<hT;M2WY6RpXuGl>It8C$OPmwnF`rIme}XtdF?W`ZP(LZ#IEH)%Qur2Aqt<+(`)pEABG&c!EknF&z7WQNr(sP2c=RTv-h$g!CC'
        b'xxbBnB!|6t&wGiZJ2*2tr8tdw-^A>%qy82C5I$!lOrrWS1QX1~{&nF>9W1G(M79bvYuD%U&%X$pfvF@a89sNL>`Yj;>Y&&$7<izX'
        b'fk8bjK36H1emOHx6$<!zxg)EpQHf8CBYYn`-hP+#mg^%yb#*xV(M;F!TkTG{i^l%uY;rb))=6sV#z+lQr%6n!9|@o4_cORwrzdeT'
        b'q7!CnP=RuHP5=IvSrF)aG77{HtMgRT%F4Y&Fjn=K%9n_2EM^r{0OKsPWg^#oM=eqWe1FTDo1T~Z*T17I+@SEh)PGLwFHl&XzuAmi'
        b';~)ERMY6i5=1Dh3&#=0=!i$QHE}V8J+&>iuI7%*PtsUCfoO9ylAo~u)H2pLEq{t8_UmZS|#j_1WHmrh~nL;vRX>GKDma{5Nc6j!D'
        b'+v0W*hJ%vKJvHw9^4v8_ePO?8v9Rh=Yz~;{$a{}Nl3C2urjWC%&F!QlcUMimu<Ru0`z`$KD{F-N6oNX&iU+%h;Ii%2W^Hb+@XE{b'
        b'eBn>eahD;uIJ7qG=O{{!f8FxmI6|$s#6?I-j{h})#QndJNQw=$S^tIPEzb7eNDL;oZEe9?Q!IH-gveijcyVC4Q&{4`wm6j)LU<r<'
        b'7TIt20o+Q5nN&bkuA`j{w(YB7<FJxuZcCkfOTd}kfUQ>GCTo}p5BCz`q{96&Dz~@BDYV4)=hn&B-!FC~LgF=qw{=7oPRuI4nt$yl'
        b'luqGuq5azX7%POU6@oQat+>=gNS|xGnd<;sN2mlBIu84(1a2}&t$4DDNapdlV7Bsz1pV!Gg8w4TkZcW&Glj+dS9_QHTJ9G^*d&%W'
        b'ZkkMSCi5(+tB<B1t|~btyiDX&cHOt9?4S4579ab}xg)R>I!}7wLWA@`rCp6iKBme3mp=Y0wyMpiz}rGF4SH>^`{zyj*Eic#xv@FT'
        b'68nBsCUNaN>GZy^*G<|FBiMmU)W2@hR|RZGoW@lfnJCq0K&K=oX(V;gogIymz*)^2KsZn0q|HvQkv2{Q>?Kc4AKS5>T=wY5wu)K0'
        b'4{s6@VWT7+ef9y00;HBT<jOFZ@-w||oPcidv=IV~diN%XN9Y7RBttRHwfnk^?pUbQmQwHBY<(Lhm;EVJe9>Q?l4c$%s85%ilfoKr'
        b'UxR?De~E2<>n2jmt5DW^;e+~Ac#Z&hH-DyY58n*j>sfP?#KB2r-NJ3oIl2QkiQrfua)g!x1z@{xlZo8468^Y8x)-3ug2j^4A10Oc'
        b'1va0_Q@dP@eMR3Xfmf4b|2-&7a41~a$)_*6E^3|fiYO;lk?7P_r0*LDJ|}3#k$e01S#w5Q9TU~I(r?p3?2G!K1}jP1_vuZ~Z*Q{F'
        b'@Pyib^38ZJMcS>X8SyALZ9nG~-86IvtsP3mN}>IsK9@(pYF5}PWcwl)`acW<CwcGZcvq8L*<|xxO6yuIhyR&NY)$oq5D$|QGE9oj'
        b'I<E>7Vd#4;{>6>ABPUR9`I6~knDLwG^Fk|bR$1fe{KO?lY<}5inbSuu>rm%r7rcr;D#{g4kaLFc=HP9WbQqyJHxudja~HsmA+l5<'
        b'bzo+8Zs<BKKl3iJ0%I=ROI)JZaTl!&5ojd*`@+HJwNKq>sR1v@h6yjVX-MSQJ&OA4x}fZ;ljlk&_U{P`#)xIu?g#q-JBXaLb`w^4'
        b'4R9Z+Yj&w~(ObWCA`A2N@n@S2N^}J0HQX1E<z4BcMVQ$T%!mZ$3ld%AO=Oz;8#p>Vju6Jtt7cJ=H;F8*iN;nxFKLTQ@W#cf^Mmv8'
        b'rO(gI`}BsFNN$T*hxR?>Tt0rXaHiLb*>51)(2hq{cs|}&DDk=__HG2DaiL-iZzHn3DtSwbuyBRE^M$rJ4de>b<@)z;bf{!k!`HVF'
        b'T7dXV<kRY(4E5a$*m*=i9zBAa9qw?n@#VjP#Mh10?~unz?HBugl3lGWT%p0#lbrp#KJ5wck}>`sufY3(ult&DIy>2Z<_37r00rOp'
        b'^v~*2pY}E2Rnh9-bJQn&ZFJh<7%4fU1LVvtQ2&9m`)+vYTvn68H*K>Y?Yob+Gc@o%GL44W*MY$E2=T=9{`rMIu$&kxMz!}b$2rED'
        b'ru(R`fvCU7H4?frec8l;*BXfI<pEu^jBwoLn4|~nttiJ>^SpGP`SYp!^IXw}vBz;6Yl9vZPH_DDnY>^3p$RD3uWRVj|M`Yu=Zp?d'
        b'Hn0fU`L81`QP144(m6}Fk;SE6`WaYoi=(Xtxn5OnXJv8e{p_g?U;GY0u~qgz-r$!Hs1RgT<<j&siDv4}zGA#{uQl$$O*rN4qc=QQ'
        b'IL6Ttvq&kuGLAaXM;AP-o|1VB<jsV-jkCPo2TKYp`s#hNI@fCA$QRJYmuSDDLqILRLDM<=dcs<3`p7ftJ+sW0By=2T7-UV+ap4LU'
        b'Gl}+_BhcokdbNU%BNZmpk$^&H-L}f|Q<8?r(}G6%DNRG#X{u3oF1W*^Z6->H@Zv1i5?p7u{~C3`xw}EoC~1&4MmA85ng(5C8uYH#'
        b'?p(_jq}nrJ^m7#X=zCstzOiStBrAMVmg55sqlsJ3J=2HLs#`RBP0&uulM+fUYFSlI?d%HNnNSzHBejCw$rwN3c>UAvvDpo%xmfa2'
        b'D_WCt(Xg2(#?MJ($!3B55%kQH-v=wRz`l%smNDkL$e)SopvAewL|d}l{0dh8B}co%t1<8iX0pe>_VnLCu7YVM8$C<M^zAOWL1gLB'
        b'(rA*QQv=bndfvjWdIVig*%c?~0U5{_VE}0nLIE%X>12Ux?JRyz6&4ThaY8WAS!ntA#*d;m@axAmEJ*z?F4^Vl=BQqO7(R#6_T|zO'
        b'=rd8lifx#*@Dnb%&B43K^9cT4Rgk}9p>`4QZlNMOFsWD^t12c#(A!~a2#7xM<6MGu;5!qJg%qL>BTmLHdS_#VEcx4wd!q8%ZlLq('
        b'5yGW~AtdrM=8VM9jyqfo{S5vTP6oL|Sm!dA5i|b4B}?|53QOL9Bx=s0Ge@FkC08Da!o^xF=J}Xa=v}yZBUiEn6OVI>e^2f1zu^kL'
        b'Y2F#^vS9WnZ}6wpv7#hgJQwr))$dw@wI#7+bW5w~NX(kd{WXeokt+@}e<s|0)$dANaIdj->;{>$<%rTgit655zU71Vj?T&UV`u}x'
        b'e$<bw1mQ)&flDj4yMnOzj~1K@vcHC)4jjXpgSvv@v10#Sc=qn;s<>KVXaDZAfH?KoXZ%BN7Dfj7KIUS!hjfaEIrG2Ay&t{dc9+J!'
        b'e&iA1x(Rfm&WObn89(A)3>IJH_XW=5_5@zVS+a6^6%#UGl_inUA7w1bOkS~_=AT`fA|u=j%C+uNUE>Y?%YG~2_ga407H3eHXIiP`'
        b'mcsIL;+B@uHcPsTN>_Y_8R87!oRFeSbB!s>?>#T;aKF~(e*My=GiRD{e=lbc9Gxd^7Md5UtT>juYW3b!@Tc!Z7z~(+@GBx_S*diE'
        b'`sMmup|((-nJ-_zN@;1hVahAc&Aqen<v&=7Ui01{lRMp{Kblv41GEqs0_Nxoh)<q3Zk!`JKxZyRIY#v`8BETAMi|RHm;U{$7AEI<'
        b'sv=7Fgr89v{v9UMJq>@-{v8$s&Od>93zvYGZypcwQi+P?SmD39$B20WACHAzzFc!og61yt(UsL}4kik(1zXnnVeKi2C%S^LlK9yN'
        b'PFmLb+o<&Qt7N1i_njKAn}Y`|m7eP;XS4h!!BO+uck+JaH>vds^&KzK3vR6O?=TQ1qL);xU!^r=_4>ZyNJ+AhwPb9p33E|dj9Z$%'
        b'iY*kgg~@E;5|<^zBrj&DjI!I>7GalPW+}L#Q~O)qQzDL?l>u?uv$8znjm%<np>?%Zs7;aQ7Rj_lN|FGMlBvx^?vWa+<zZ`HvDczu'
        b'ENaFQ&sfqJOXgF=i^MZ9{)-sPLky*fIRwu$7={4uY0W7@it;mbTGb&c1(v5Jh+ozvE-ION_{MkrxbF*sp&#!I^F2%CDQ}q6c~ueO'
        b'X9yFW9rQddwh;b3T<rVeV;oCqa|kke*9ieBby3<5w}AQR3$%#5Tk~khkynz}9om<YkTc%qu1<}@eakW3yc-?oWoO=P#u-b3x+%!3'
        b'KUy^b$R3mWYPtGqjtuwh<**V;NC*-zEM}WbiEY`hQ{KR4Uy@<b{O8R{GHe3unZh>~pl_Sk59q%4dsTVIDlbag+=ovdpwgo2??fD_'
        b'iP}Bp_k`Vmfo2l(+)iZ!q5HwlT9Um5k0YYDrq<#<EtYc)e#K=1k^ms^4#WxI-T1B(xa0SD&PvD`-$OayIy^^(p0%Q!@o_vk3v!Nd'
        b'A}1_05;xAn7)nhhxl@#^;C;YDmTSRU6C~)q@U!~&iL5N$XCOyvuPVFclFWQ>Ezok+El4A@kI1x_YudG?onb}^u{Qzpi3zohBNvNT'
        b'ar`_xaOO;OC+JDPJIK8Mc9A+5Faqn0CpoPCMUIRUuK?*{E%A#^Y(In>pT!mxq$c3La6#-!$omqo*eu99zQ@S&?W*SwZ^y+~u%e~7'
        b'ZzXnPb;zzGA%#1+*u~-u4l7zc&QcGVHNgsTD)Zr8a*p=Z8k@G%d|}c>J;eIHwH>ShquTuGJ;sgm;uKG6Jm>tj6eWn8d#|@ERsKSX'
        b'-R&PqkyqE~_t%g_T|SfT6feQB_<i#a@7og_mYPsaX4&`ok$iqQobEKfjXsqsPu+(*{)KH<y%>8vb+&Z7Dkk<q>TKNiDQ7+mBK44>'
        b'ajyDVF7_p#jQ=V+42t{ASaJa>^AC;zny*jlp6F#%OBKX8;~R{<nR*HbjcDKFPyG}Zf5`Eq2I$o7_S?7nwR^oL>LH+#@swrM)#aPA'
        b'oyHh!QOb4|vq%Np5)Wa?CsJnzEeb<zyn_(19xQ-?hl!gpU6G%ZRMZ$}V2f4)#MsO?6A6Xv|ARVMc5SCbn=13VV~>R4zCU0JGZw!W'
        b'cO2q$tNokz)e#6Mm8>n6DHbkNTe#RK#Gg$;_tw=QZY;!L>>Nw59F!BM0B`bhRNGatAZjp{&Df%A(4?c9)1~x6Qwqgh$EzHclY;1Y'
        b'h11OiUOcAA>al}Tq>^_LK{_oc#k|g~(B?E776S2X!Q<jp&?13ae1+StdMbzK`wJW}$6SB&z&p%`UxOGtRg(*1u=30Q5`*F|c&@fS'
        b'IxPS#d%Y;$Q>y2M6wiY{mw~m+awltf$asNUSAYbxfJ0JtvFB%l5~%2r`(H?bieyy!TGw)?hwuX#pGu*w_RDrM?8?fT+$*J5Etz5s'
        b'w(k0NRnof8kAR$KVC#_FJ4!jTf+WiU8yU%bSbtEgtu5D0_PVm>_}=6gw`IF(9^+o0dIUEznC|3thKP(;;o?kAC-y@HB#&-eiq<~T'
        b'%M>R&P{41-jmUMRatwGUw|e;^e`bm!jVQXQ?(j4Q$HSa1s+WxBAOE1OEZ24QvRMx(zU}sBaj~W14O3(oOcvt~Zrz2{eSNXlH-cKB'
        b'Io<8vjn{Cal5_di)k%zH9H}-zsU*mMOGd{M)s;1X(N<k*?*D-K@UV7&x#F`g9N}Qsz(luy*t;dAJ-yiH=aLCDm=}6UO+|sYhs!}('
        b'Am+nCM9DdzB-Zf-hx%fJ2foj^&Tn;ZUQa7fl(*~N=_MnLzv7U3*gH%2X9QLKRoBu>rumj}AgSUXrmQef3oq)9BJ?$68pxRL^Xs05'
        b'058yKHfFho{qO_x_ah45NbJpxr*Pk`DSJ)t#!qoa|CIfmUfW(TF9xpV8e<j;NphkWmX`+NNN|*HZ*S|7UKX?=iYS#`HttT*R@cZ}'
        b'mSo-Ut|ReX3DWl-*+fd9E00PL?oXybX6$eD285<-p?q`ANS$2wQtu0OE)eCp9LBtfO*7y!V!(^N<PtV(18`RSItL9uCDzs{p#{ex'
        b'G}Cm?_kwyRvKBC^$GsQ+`c9I}dwgwE3i`@ed#1caTYBJx=b7Ht-}f>}*(Zr0e>@lans{Wg1zO*n?VCHrf`Dj5>oaQ1s%~Us#k20T'
        b'T`*hUz_vHwAf&82c)Mm5C|pN5c6cK$eg-?7iu<0zQjh%V2Fz2>lum!0RV`LrJo0Ez)xUV{*>y<XlmdSD=9FfF|D04YQSZs=P0xUi'
        b'dp7sF`HuVa7_X}07ZIsP;z4EZJC6AB)HGidOGAoa5<i6L9_`&ZZk&tM)4o?xiPh63bg8{NRbn-klf7LtKPPP$=(|5+IgyC!KVXY)'
        b'qWo5D(ZyY}k1YCh7ofVv*|U3*+$Hwzj1<pCwv*cmJvF|JZP$dcAD($98+Tmd>{M?_ajtlJ?jZg20cZZUPItQpEVIt7Ix!6E<BIFG'
        b'h!o~NDdD}q#)@&rPD~dHqE|6aihRK^HeEgJHJpu<tS)AzkC@cI={|zKsw73Lqs2Ng%(=$#fDTQS;J&w}V0;6kEB;_o*Ki$O&Kf3k'
        b'9~N#w-(r?JMmc*#Z|e`&p&#TN_QSiE3ESlwHsn~@fZHkaet56lsdQhfDf?oi8O5hS-^Z^wCPs6o^}QbN+{fE2%Ylfeq;1sl!3o_F'
        b'=u%Ko7B2ppW9FuVysSkkQlWYU^=<O{bl<+bP8L^$`7XiInglo=BO~2uH9oZe<2lmfwZzBoO4>F1m!88t<XrFPI4g}l>BJo|Q=WfZ'
        b'ze;7X(#)%tG&DJuXNu7aKhLG>WCTESc@PUFENQ+I9A<z2Ix;D<GhL8B&S5%R4|7ex5Sa-DxWmpFgFx2(uPSB_;11yw8Pgo%U#;kj'
        b'b_k|ekf~3umsl2|&VpFEIjry%MJkk=nADz7lF@~$6rGjlr2Z#R`EMps-!5LynHT6CDY|M|Bz}X#)J{bL)ESxt+=TchTB55IzWzyF'
        b'B{1o+&M<M`q^|8c;z!-}l7h#d68m<;T-3s1RR@a!mXif$q4+DnuJ*cZyo9Tf)%3^fMAkfG+a!iewHjoi6=Azll5z@=1@>z!rySW_'
        b'S5P(2+dWVrP*Z1vYFfvelRyP(<ODS0+lZx}#*I&5u)0Oz#tW0?_`|4L;ZN1T&Sc!&HW>~Jwr9(AX7f^C%_KCu4q14<7op+x>%tHX'
        b'&%xisoN;9L{TeNtK*MpKh8M5@M8p384GSIRlROFQR6v5b7+aTu`uQebc<av!KLLf)jXU^$u0tlN<2R^{b-dlV0b5sq+Stoi+w`+)'
        b'MyU1+$L8raYET=$LEUt$$JQN!mK+t6V1|-eV1s&|x(>B}s+xA4w?_@)Cnw3QX>O+gx<`EGNwk3SfQJCE$YBEfj0c;BB?9ar$77SQ'
        b'AWlQn0C`xv3=Bku41?JhOH4m_@Vd*w5Lr60Ve%?GQ)$0c0u9O1pT<{l{VFQKIMOGPFUIhs=G?D83+5?2O%XGbIs+OffO~?kW7_@9'
        b'<|V%5N%OZAyFcyr2A|%zIcAIdj(_o#J430Mz*?_%d*>P&RsLQ@V~X#kdx&je*QY!FLr+P8(J=?wgVqB$b$5D*tW-xNg3Y=Q8wOaK'
        b'BMiaLbx*?v0G8pHiD2UU<@^A9)Db+XE1jlL*A0+gibazQupU{0jQ)L(py$81|0xv7G~T<1xuA>+c&7X2e(jHYTxekQzB~7-6vkmR'
        b'=4AAAwM#(zV#n=!(Ei1qmL{dQAY1&(J<M{mhrk!+LeJ68OHlp0Q^}>`rT0E86w>t4PAhe;hm0^;m*$=AdG6~TTAjUxmeGaTG^}=X'
        b'5Pf`YlFHmB+I^`9y*IEhAQqrLX}3Nh4D24PP#MvcByXax(2#iE=z(8lldXPcMCS|Ycc#|GiRazJs5g5$D5j0h_FU{K8&_ve!7A>x'
        b'KIWyfwM{awHM>Oce$_s(&`Da$fM`7g79B~@A559t0_B2ot+G^C(ZdjZimh^mL2jioSn6Ts_*AYLoZd_@jdRV)vVVcY3(mKdN(0+a'
        b'yGprUE404F*;3>Hgskppk7aE)c*@#U$WsPjW}4jcyB_TVWp%DlyGp)3MV1RZ%qtEmz<qPE`lhMmmyA<)G3qxx44tRgDl9?aOAoK!'
        b'_X|cPP|Lw@T%dclr-ROGQ)Sc1b3Cpd<yqM)orTO)*_hj_rB&HV=vqOxuBa!6h7}Dl>jTc$f7k0Svp?L;zbjH)8p>PQ!>IGTg?Y^8'
        b'2Xs&Nl&BuxDJ=|%Xbc4eUUgn;Sr5H=PKWzx5`U$MF37geLN&z$V8hVac`JI*moV0B<8e-x(_>O)_Z5a&N<g13Nj)qr{PR@oUwoJE'
        b'A`_;t#|q2dLK$OOswkK1^gYfL7XE5NElJ(Ygf)H%Is*{xNVvzSvb77qy<MWS^th-c;C80V4xG^DKVP;@s}o)caC3pO?Kr1>M7sqV'
        b'*T2tDODx}aX`hHI8_!MAnka^)mgKIKnJkRevTR>*h)&((Qax-fc-UoGrc3WJQA@N75Fu3;bPx8BBCE=1Dll3tOYJwhpheb_ow_qb'
        b'7YV&dXA9CzmTXH`7htqnj7xWf=t2QkhP5EWWijezp&l>&1|4+psxs=|6L&`Y=1vkshVGLt-v0+t$Bhf`=|;Qq3l#qprftRC`>k#i'
        b'+A}Sh6lu-nkBU${jVxjPD^tlE#N~JMd|eE+)MPON1E6J-Wf|Dc_Vz9-wUo60jfgtdvdqziY}Du;XawdH8HO#mARgj$x4MCzlZ6j@'
        b'Ra*3d>1{+$5YVI5wfu~p(0jV>ZmTLgb(@?Z(shkLJ#vKHW2p?6yx5j2EW5>0nJuSfxlbx>TA_<dEBg<Kbqg=bC2w&c>mb=%0+M~F'
        b'`?)u}ew6GjyktN3es@5!VT?eykz`v^u2Lx=-&eK>K{JCen77OG-s^T27DZ+p3<5W(y1G<xI!wWa<*%ZTbtS1E4dM^}Y)Mt-rqyU^'
        b'6u$KsPQUezQf+&Ojx5|U6}v&a@UA&)2IcKe3r(#R5xACE@-Wrd&AjzazA0nDx2pJ!MY!(~Ot-(AAasObKJ8hNut%=*bc1v+wc?In'
        b'V3fO?F3?#Hbkp(KK|Q$7faSg2O@`%~Wab4TWVGc+Ys}WS-q~#ZHXb)Fz^u)Z&9ri5d9Je5Ttb2|w|Y}B^(xfRSmS9L+*s;Bw^Ah|'
        b'!@e+>sN_fS)z8nMUhXC%Xd0(GE`u_m{@e|7K^ZU8(n`hE;Jn{=)9S@lVdBfPZs5O9e!)?MCX8Zyl-kj)GjtL7!#|DBp}T3;B5=}u'
        b'9D~OyR*vdy-GO~3!tk);Jo?rlY{WQ<{3trxdi<~J`MC*22|T6hknZ^(3#U+)Zr@q%>2GpD%@$<){>qVI#?PSM;ZWRII|cf;?7EiM'
        b'z?8Y0ro}~cC`--jj5PlFF0B#Kw7fIa@%mlpyY5%r|L(^f4H&ITHc|89Lvir|OtZ=qDo*g@KG$84$JB3d#{+k_`*E=gBZzsr89$S^'
        b'XYYpLLFm5>#{?6aP~9Wlgdqrq#&rA-0n(_2pfcytbTVBmpi;U)U%L;9ycWG;LIv%mMHGc;2t3{LXg7_=!s=o+VRoWBHxhM|(saA1'
        b'd4wTdvxcSxgh5EDx)=SkI23rZT7f%W#b%G=;_oNCbgH@>W{UCAdjy_JiM!IQimghT4uZJ~+8-VFiY5sdw|NA}pPBi93hmBY)D2jm'
        b'ctHEXpc94+Dy>@ySqm^CdG_;amRdxL0l~(|XxeSi3A+=(PI?{N)rN~pG1~o$gf!gudkm^3Y>lHPyV6373SxC5Fy0xADi>4kPg|Ml'
        b'3IS9U-K|^&$}Aa#h8pim{TBCiU^ISgwsj_OCRU}%*Dwj?unykU-RjEg>Y|BElPH-~<kIb=NNKKtYV$<vpAZ2*;b}W9fJIBWN(l&8'
        b'KmR1KI;aG9v|-d&U39@h>OWnJ)M@nU8r*jYOMM&noq!cb3t92I@JEN>?_t!{E}gH74t<CTiz6en&<t>=rbQ(HVs(H18gwiArrDBA'
        b'UF=H3i?UR}si1M(ad0B<k6$AjAYyv-#Um4WE4l(4q|SAD-3_PMCQto4sX(#oO{{vaOp&;Z#WyG<*<hxa30-0ORP39+^a*q-E0n;4'
        b'h^!#vc4WrWY5_=|v6Q3Lgu;rEc;bRWi^NLJ)0j0-5F?C2@iSn{&r>x1M-xRCBs-o)a|H5-zDf)0ya19!h=d?1j%@&kdTHjgFoFnj'
        b'OmI|tS8gb;WJ5941>f)C`O>Yp!@=oZ?qXD_7;y<k-p2y+MYMbIzBb%f$(5+GsncBvyTHbsAc%)@-&SJEfo8G4GU5n4UxxXUr;^|I'
        b'1x+C4kKxAE6IAxs1hJ5RXN4H!Yn*^Ox%Emy|9Jhb2tx2U)IY-DzE;rX3$51#kTn_OXrtN+tsb9j^L4<=pL-T9`FY=d-Bz$XFn7eo'
        b'9D>wzt!8oGqZ4_qu3W2Z^<JqzZfcRx*Y^W(&ZJuU&MMsT`s4u-L8R*9zvk!WTr@ZLP6m}M(yi{IsQ)6)!A_7NUbg^f^S}5r+A0xk'
        b'rfUK+lwJ}CFnWoaTG|C;zpEgLz#k$*FzrCgQDyxL5l2#R;~yqX^wO#b<BOB<jJeA9C@YT6QtL9h@-}q=*~Y(fz&jJ)Ss)G2!JK$*'
        b'14!v|cxqh|w<XZWhxu_$yut)yjNzE^7aW%N%~y!v`(kD^Pvo_JJ<XA&+@e*h!*(os8Od}UwrIiXFkHNX%e(p2eaW25;On+wGkrlA'
        b'6Z(+pEe^@2>7g<|{ECG<%!8rD%=8c$fqo6^#E*b4`zengY=RV_b1P^;wyl&yX|MpN?K;y#J}syF`~NDpWu@HO%t28xINZ9kUrqbO'
        b'*Kx6$({=o>;_IRKQB>U6&ygb1cu-`rJW58N6P4XtzfBoZv~eZqrK~WVx=KBY3FaOQ!S-LMK8Q}-xh#+Fe(Nj3K;=dS##r7NA)Yfy'
        b'ef2duHMzkUjeJo>Cbrg-yG{$;Jt(0&?mZ<5*>2uGQ56MtmhRfuFuGYAsEMylG*&j2OKU;DPwVN<uNi!UdFxE-68woZhlNrX;m-r+'
        b'6XBp1b`?HHz5g{s2N$Vu<0`Bu1$S7mqOf(kqhB#9F?ydc0g`g^I&L&!x|gBP+WT@S*KG@Mq$S}xEbkeFLHqw$d-u4eu5@8|-x5Ny'
        b')g1x>5$)bPgiAzCc2v-6n*@xA+9t8!W!iZO2-@2mL@G{er%C8Uw0H*MbiCBQ6Jn`o%LwUAYwLIhutlq&hzN?H)Rwt)+KzRsmnh_Y'
        b')(+a4^PTUX@BMy1eqpb**M8Po&wB3b#sxu)=(&AY(#k<Zqe*og4*KYKqlWjc+TXp(KWtLtRS>@cB8}U7Rq%tzj0M5s=UYKoL6h_v'
        b'*7hic4k6fc)#gxwH6ofQ8R~LnOXt;wJrfGPW=d|1(iPsRz$o>NS4V=Q0p~*LXJNpj_js7j2A9D@Os%WB`V6`0mvIVX=E?~wBAX<*'
        b'nj@l;%?9*&kA|_~V&&dajWmu`CTfVO7?+0;AurmYZg~7k5&kLkuAH0-UgZjQ(=R6jm;z;H|3vpT=wx<8kwrj>XBmPo76tnDP}mTF'
        b'_ofH>+$4QBjPW2Oeb=>r8O?agd;Jb#ZqO|+5!Pej#TylXI&SS%z@GQxFjsJu=WS^Yj5s9?g$;RERuy-~c@Nxmzz~cOR^wfSUd@#U'
        b'bLd3J%F(oq)_2186<0x0fk{+E$OXx?MoFPj@A?@9^zHof6}_Hf!8l)!X8Veq87X@!pY8y$y>2fd{Rk^4Hl*d#YDfDwL!_;*s^C>U'
        b'-+qlP-dXVHSxMJY6B%GiDAxmOF)1|>*=zi%ujmGPZ?NrYwqfUpYl2$$7qw<KZE>buWgUR0ctv^T`3b}2N>AG=Qab15&E#TC!54Mh'
        b'@5sQ4w2Rg6MnT=3|4g!^{)Vt_Kn6|f4MO@KV|LBe4bXdSZl#Bi-n~Og=Gy-@^iWiIm)<q`LnA*JBPS8lfAIS&*3F6k5MV69O4UTi'
        b'Vk{+vkUn!awOsD~$z6aBcEswtwC_N$yy5I<Qm@yC@NW2FD4<ak=rFJ2E+CrcB{fA2U87G|bZoyfEC)BI<J&t1?5bV+Bdr=nuN3WP'
        b'SFNClb#X+;KFq_-1k#}6-zF5R3U}?arS4?Y8QwYT#b~vVJaTe0>1Ide9sX1pStM&P?%OLok%o{JV0rVZkrx49y<FoE--A1dEcGvO'
        b'9$&?`huFf3TXX5u{OFNSM;E;AT?cLDu3n)R`}oDqo-0XtJEAsK&r+;hxq=5e9$u+DuqPRC8*E#}V2LW}lWTq={@1`Sxd>BK0=9uH'
        b'J37PdZL8Kity+Ykm4DoaLk?cr8P}n@8(BYmB(Zaf_r(2ne?p+m<aQ0A#X4<QfYef7(vU<Jm~Cng#+`{!o6dgp3Tcjo@o|22rBF0L'
        b'?H^vDgAVQD)Hmh9Hiq7=Eu5fU)4{b|p%;}yyWhDIIB|<U`nF`#wn9bz$`wB?jgJ}rrLw)v1njfDhRnsR3=B!>u18eTXy^^Ri}a?a'
        b'&9r?7dL**p7i8~8yC%a+l-<?S#<+I4NEsG+NiM_2`&t*irTb?DJiwM}tbYNX>{NAJ9Hp(VN;hrgk^JRVl8GcS2f>zPi#0@0hM3s#'
        b'*?sHl@C`{k*&$xI!gDiAL3=I?b6c*^R*)z5|G2VX^{Y|<bUu!h%mLnqZ{SN1!@I^hjPT8_#BZQoHJjlrgULH?g*B2VNn#?4$u$xU'
        b'{C3<0J@V|8tQG2w1Eo6&>-z9W!{~Ct`}f-@;O(3#U5f+>H_KO?;B!9uVsw#HutrhH?wJYH-GNcgC$7-(yQQ@yt%a%RTq@rA=wKX3'
        b'mzo&sJ(73MM07}azYp_db!QA;oWL!=BJdfds%Zl8epE5^eI6G(^gwz<YybCX#;>iNP&s&RI_-x%(Xjy8UTG^Le#Evr+`=mk4g}|H'
        b'PCDdp&iYaAymZf=d4-o$t9$GM3b`1I4v!%T!-79*VpG_n!=otX!ZStOEEIF$#hA<CtB~X2vYH`BVEMxu5b`JxBYLdx3X1u-M?vR`'
        b'A1*ALhl+VPb0JHCW-a7VAjTPc1&ml1OW7jHZw4Xh;~t0SB5s~3UCC-tT~5Un{R5bSpWyB5p)PgL4CmNTmO4d6cpEV7e~!|#y)~%&'
        b'fjg;jgm(|>e7Q!#r$X<gd3U(6A%T~rsG>^V7|nP`>bVV)YfHmQGOA?zXhx3o7q>mYE1Q+TE8Gu5KiY^h?}3S6J$V}hb!s&s?YM3K'
        b'X2|*B;0noHn>A#Th-KpMXe5G(5T9f37$rs%DLyOjn271LnkKN6^Dw?DiJ>OOn|RNJPlt?}n2z{+EcrZ=hjI5#te5fH#UEM-Z_GV#'
        b'H;SXAq>L(z7*@+ii=(12srZ~Xin=%1SdU#ncUq{-c^dOlqj_1j`N<XL<?i4h;``8${j;GJ`0{N0Nh7{YgD+L#d5$89{n!w9bBL5!'
        b'R#-67f}8NA_EkgR652l=auh||KOAC|A%`SMWg#>c(rBU7FX46VL$+r_g-Tr^uPZd_9=_t<8{&y+YJuRc4%H6~sR+WRL+ibufQlf+'
        b'2U0~);sX^`yvp#~A^XlD6{*ljmT~8YSS9cf%W`rRX+r8+GMfedwMZEjoDQ8Pdv2sV44#Md#79Qx3sMylT~IR@ty}#S>L&E=Ai-4+'
        b'A&aJ14!YF-$00Cc(;H3{E4V5UkBhk@&@lz~(a_dnnf({g^O@lFf+uXkpWnnpIe0})Tt}yZJ3M5!46ZImJChWt8x>r|5F&zuL!?E*'
        b'Z5WE*C<6!7&@e=1%TOrpouP;;#dF!fpkQlq>xXEPBxZ4jLE#}+F@#kY_BP)WKqLN>ux24@bKr+oo+qqx;JMMR9TbiyqZPGtS8D|P'
        b'prcgxAnhn71V1hmtTHGEBX)~GPR*1O*7n<m<wIZzo+u%#$rv49Uc5N<rFr(;A@`~wL6SsDvcQh%%&xNzf#vCuOl26IfFIg0XGonJ'
        b'B^=iy;FV+)f#Gt49(ps~K5xi9bBJCHg?y5!D%te11MH^lNs7wK0wpQQCUes(RV5nP92gsT_MAjg6&h*hh7hPZ&}T8o>?kQ1U9h&J'
        b'>6V~bTyXqWL;h&eZ0n(0AOzp2Li^qFJ;#@cN5*Jm7%3rz<17eI1R+yHV(=)v9LCgl??x&DNh|#d<f>}OxfJ!a5M1)&+*K=t{f}kF'
        b'C9X6+C+yc{zDam3n6Q5~Jao*&gup=Nn`;eHR6PC%!kPnW?lQPC;z%I&>X>z#CzA}5hQN&LwAjZ6MMFf#{bSH@chIhZaZdlynEl(J'
        b'Vdjufq_ct(vfqJfNX1qf1z~?~W}MCN?cjnrX)9Lx2x|$E`Uk@M3oL07q`WaWq^zk}DZDv^(NgK_WAORYnQ;<f|I3+gb_nmkGk*>p'
        b'PfPXdstWZL&hA0M+9Ft+5!g55L{C^yNi)ABIv%-g_<WF-7G*a(dj^G++^CK7xxJS)(z!Mvq!&eu^!_cbbx>o`aruKN5K@|pDHFM)'
        b'gV0=+B|Q^F--R$*4cY8HA6D~Y);%y3YR3)hu3JeXsI9lK1=^J{M8}12T2%pY*nxk_`|qzLfM9QPHwOWUX#_im$%GQyZ+VpKi@5oq'
        b'1-AUX`3M7&o1Ko<n}HsPgegUd{QsLWs2%(_W$^6f|5+JS4?a`|pb2&rP2^4t@;nx4wD*}?T-D$LsThr$n@wb{lMvFc@Ioe}vKR_u'
        b';a4b7ZQ))S<cYQF0M2b5gkmaUnuf^4l;A->!eSt^=8~37u6)o?ir(6r2g&SdAOy(lM?eBZ*k9@m3-zyM!gxm!sUM(4@Iw7Biu@SD'
        b'8#N~U&NZK><3S0R`?0dx3ef64r_dQ=ZM<jLHCUf9m_+M8VBIT`98+(f$*ml;Zy0O`*quygQb!nvTDj!Q4t~kLUt+esr7)(~@lq{e'
        b'{T}apiRV46R>Eg5;9@V^mkd4-I8i*gpfje!a~G^S!`aJ`up(N9VDy5^UhjgYO0VETy}O9ZhG%bI*qR>(`BHGJw+Kb>jYZCxFx-wG'
        b'hufy7^pCQ&Eal*gFx<Sd*@!|;9!{{a)RsRC^XQ5f$k_4{j9K@C)C)g=%>%>Q`XIw`_$t6?7LyJx3v&3wj|1TX5b*n5V!nra6qRg3'
        b'VSutUrH@+(W9@hkg};F>9Y80d*#RxGM-AGHN*f}!$L+%dB3;dcq$x{j#|MF^pf3G`ss%6<Tof0+tj>L2G}5{9!^g@%q*ypG2=~G7'
        b'p#9F}&BT@)WxT%p!ED%ue_nQ^<~p1?HF45Aqd_jG-LDU{F&^g=?tuXqF#GUjdNMEhdwWxuHw%1RvWI(uw<mDFx*Q-r=D8eydR1+J'
        b';g#yLPn4}Z)6BC$An`-W$hnHVU9HY~o|`(D1=Z?#y#PKk7&AiA2tJxbNuT}!48&|04zB02XuZ!yW0Zn*OuonCjpg`3&<$wsucjW0'
        b'H(^G!19+W>(T?4>_}PwSKcIzwM(g!3*M2$b2SS>H1^BrQ(<R^}S+Cv#s>1YN3q{KcG?@3!9i+_`T^`qFc%$>f%Z~O1!}&^EfontK'
        b'WuaZKl29P09r(fdnIP;vpXr6q7C;6F^Z9ePS7wtGW=|BPYmrXLNmQR_%G;CBjR~7HQAGJ?;$tZ(B^V*ZFd>En8jWrE=lzUWspbc?'
        b'Sy}}Rv3?;M=Q?N6fK3|02o#}~8nE%%k-~?wBZbeyFdJQE6wqO%vbmHgD`mGFsVxHobr#g)5;JOD54Ou~VqEKhPP57nrxsQ+0LKG_'
        b'R;qMWGKG~$4xz(9DuIF)mOZO1T*tavsq**2KA^HrWmze+;b)gy0a`0%6O%w_8>|D6gXUaH8PiGShIN-)JJ{MnN?)oh>tqT$*>?N-'
        b'*4CS??PgkC*r{)ArP`fFXVK;Il-$(Yg!EO+{>J5&J(q2jO#O_@<)yhv^tipY@^ZwG0Ru;!_?<(VRCB>za+#E7MN|}N&2ml|u+0ta'
        b'`_k~lWggJWD|H$TK}0k`As-^iES3d}DT}jSww35Mg5ff6z?7`Bc|xvuU7<9@MCE~6)gw!CGWYY#4-8wm_VWFVWN+(Dbig=?7SBF3'
        b'BEg_6Hs>|4#$r4VY)3G>*c3Twe!>(8l{{i3@hAMBu!Z7!TlWma4w1FWMVu*kc&zyk$ZG&40dm?SN{t6f!g2VXIKMS(Sma(Y=W2w#'
        b'L1%zm5Y<L1umUi-L!8gGAyx4xD%li<v4UjTT%<NYE`Y!(6qy_b%}ydcf$pnAlIn3#9*{I?mG(=QKy5(2{oX)CbLbyb4Qj)d7y{ck'
        b'g8I~JM4>WdxHX_5vqa3w0JD$-XvMT46Sv0AT?PiRWrg&-4x>VRyWWQ9MaIGcPX9qYrh`0`VI;G0(B9zcy+20BBSzg?@8blt(Y3O^'
        b'Y%{xSYgEbc`x&#PMK?Wtc)5)A9sX5qB~zZumP?ZgqT~f6ZRj0ve5MCJT(g3d-~bn+62-by1P<0Q6PFmVi%X<N)F^pqylS8e)RqS+'
        b'C=G+gD0OU1o~b_6K%$|8UW1R!-5CfJXW4jo9_Kl0Pni4b0OVjIVOitC-1UJUw{QSco(fCF)wXnI4=0qL2v<Hc(f!E)DK(DA&a6i8'
        b'-3#K!I?jX*`v>T`pe4Y!UZo&Oql#oviEN{A{C+{fnDhjKv#;3w-hh!XXb1s8FzOgyXS5hJ7J>WqfP+}u87KXROhXtzHNzVf@rcHP'
        b'%EB`gQ5U~n_tpTnZ9ojM>X=v^X_>3CWLl%g(yGA6^4@=F)pXpv$^B_y6@jMdwG23h*8H1J>m`yj*whjKSD_&Vv?&_=un%r?6$4;7'
        b'>@&Kn1|9?j4J1^H9t7@1c)508F&SwVhMM(n?@I<8htGnd5eP(&f`#>N8AamUdT$hL!q6yE-Ki2QGlm{gB+`jv;PYE0_c3tC9Zumz'
        b'3CMlvv@r|=@gYru|DXXj_y&;1D$4ab#;~lY7YWPp)23&47Mdz*D)c@yms>DzpLy{>QcdvFoIqQw8^44$$w@K<Du*}EL?__N_+&L7'
        b'BW05*L8*2eeyuj5A2mo9anS?ED7Kvi1=o;7)g*SXH-%o@l5AR~T0-P%vW%-^mhkfg>6DuokL=r=VCv$ODKhmvoIic*7C%REl#Zi`'
        b'W^L6mf>T}!w3*U;!vrRcg0^dI+=NSw`Dx{1c&g^DdgnkA?Y?voZT8_ZZm*xmO&)OYPwe|_S$yT28K9hc_{Et2>vn#5kYCi@UE%lN'
        b'wBDvLPBIYS?KOuSx@qn))Hg?wojZMzmN|$7I$n|gw#>Gx>X~RCH)DpZHgzYP&uo2@kZ!`#RwqS6uWNZ`tB>fYz__tXjSf)aBiQ}2'
        b'LweBJL2jnsU*W?)4LB|Q>9HnR?SY-_=AC7G8K3j9a&E@`=(H%7jV+By=f1iW;IWd?dp^zrQpOLueZCqQGTba=V$7xVx}D$*!Z%RT'
        b'aOo1yFLH3{eDU1$bLy8Q9&Q%WW_qgm1Eq(v2#2rg=Yh~emTvIypZua-<>MYhrWK4$y3#d1HtSDZo6;n4Pq-A>V7w0@?%)?S&mEJv'
        b'H;ZG;W!V4g(#j$!cj8i7QF<Kr*(HIS0iI~Jid>{mNgz5jSeAoUpgDfc+X{B~&RVwOBf!OMO#eoeOJDKPPNKtr!XzFPCJNvO(_(~n'
        b'W?t4o-^i2q4|+hD08&AoWX(eoC7&cIm4x6bFM_{eBSIMdJV}z97%lhBrA9I$ERdRL3Aqnk6!#cM#0?T3Af>qfeTlTp<Mv(hpf=7^'
        b'$tVm5lb{4u5sgI^5mF7#y?Mzez9pAXRvuj?tziXj7NCMnq1ZW9;9pDM4Lh8VIh>YPCDM1oyz?<09tmrG81;kKkm_=b_haeCkzLZr'
        b'bfYw4VsNuSPqBKy_*EDK&{N1$dGvo61BW;U5BOvK$|7Vc3(EC8ii{z{_ydNuQE0gaONmx77$(j6XsUP12gvr!X9P|Fd_e}N!Yv!Y'
        b'FxHE&g~R{wJg|%(<Xm-$ma({?!y@MV=>d$#{3486jZ!%L8Y-`49q87SNB>nnMwBDcj9JKNjwnZfAe!3dLQxfhoo%0g$u@3hKW<lD'
        b'6x}MM8BJ+Q`|L~5(b|7kj;#KsTexJu-@ool!jU#_bsZ_2Z`WMH{Cj=c%mb5GwIp5)lw<-X3QkkNQQC?3ft?mys!s5)VR!8&yxmyc'
        b'&Hnm@mpthne>J1NV{m`p?@3#(ZWQPVJ<e?RxBY0-<jFZbTsA$W`Ix@Bxgv6OjDuUSuffMHSe9UqxwPvDAw7qEc!}t^j4c>hIgjx6'
        b'i*qeM5FKflU4Cg*TuKQtaqYMIp)UphlpXoP(U#S`V&^f5{m#XJHnV}cZ@+c%phR0KZTv!=hc#@zKko~}_ZJ%_g2uLLP1cIcxStrl'
        b'>K8Qg)J6ix(jnf92^1(qV=Glk`vjoX3|lp8|Hnm-GecPPzTr>(^<P|cXqKxN3BwYsCeeD~2HL%Q6w$lehJJ+rmbsUZp1?*PzYmSg'
        b'`~e+5Zn%08zz50qp@xs*v=<Xj)-|ruHcY7b8dXNVziRcWIAM`YSQ0sC1*B5IX|}&|(cO7bh?|7=Z{|-DkYi@l+o&yH>IKFI?h$7K'
        b'QrL3g`h$Vn@`nfRk}&+hUE1<e_k-6j`~W6UtC#{a3`J7G0JEW~IRO{~%zmB)=s<z~eE1k~gAJ8=4W4UPD{T&tc3EIM0}t^c`LW`n'
        b'B)%yO56GXN11(wz_89W(M3;Wt{o@|56<vClm_&wIdA}!On7w%sXwUWUwD(bwntQFE=b4%wK+eg!i<5)VSmSEYA@&^?d2WWmeX&Pt'
        b'<BMl4D^Go!kXB*+L9`-wSyAd#Lh8n7f_F~kGA?FW(j0<w3hzwfUb@Kh%9^6I7@jBLW&MVWJzXDx8wGNrTT|7p)3ZHnu<eDB@|c3W'
        b'q=xkSPtW#-zW=`v87zCV62w{O7ziLi3$%ul+1SVv(tuXdme#-SnuPnw#ddxkq6it*uyKO7ZLB`NzwzaiJcTcPo_cbZ$C+)N8*Y-6'
        b'?7in+0IV`keS`>bGkkKaN#b)ZMR&kJid*VYV7n5Ob!#uSa~ZXrY~7-Z?amC(lJ~U<_pK>mM3`}iBs<c>J-|{~Tc<v<b>ZS=xm%|a'
        b')*0cTHqUVZ#}uam60NB@RPvchnig*8yXQ?o^3oG|D?8=B*GEqgO`++u42oh$&NqCjvQ7<qF5o@d%y#YKpiCQ(C69cjvY+V>l&I<p'
        b'`rWtt(K$V_VT_J*<o!j^F!eqC!FLdIm0XfY=Y%msRDV{n`h1s<%h>ui0&)!Mi>r2~fORH>(K@;-eP~I*9>%5$`J5SIm{Ec0_u7ez'
        b'LP?f2J#4@)W|3Jdr1!$hJU|8BMfftG^fhQWT95bB7{i@@fRd&n%~WZO9JF<Y#3p*)yk=Gsy~=Tn07GeYz5ByH@jL;HH^&xKJ_F?<'
        b'<c<n*8H>wfx$pY}gsDV%PrV%z2ora$U$A5tzUa6Ax}PUAKsbPb1ysZ@Vpnc9aeoF$0yGw{&!X5gDpfTZc(+`PaFmIpfe!P`pVXu%'
        b'$(3-I`vWmEIY5{_A>c?xtsW-r7y8k{8eYXK*Za8nLd2sAGT`Qxy@HepcvQi|qbLwl$*`56Z(L}G1}PhTBx7T(7>J3aUic^c2XzAq'
        b'6f_QG01*Qa;QHnVMS$5|qB#ReM9L`VHSn7u2?WiiBHk<)nY|1N1mugAi@q2nBO$zU(HHZHx(0f=!QT)35aIVSQQd5)?2D+IGEv=Z'
        b'*xmn7-IP6G`4iV3=Os){Ohb~C`*pv-E%I=S#pPaBAD8RkmIy`j4KMe3imZah>MNS(D4ON|0gW6R6wl-$(ZVKgKUxGO3Gj1Eeoi7S'
        b'Q6lHu{h%*j>KBSgu)jPaMnQjn%(z7T9YJU$ur;o~f5c}b;{iU!6yP)eU+|g#@Aw>7=nwFjFXA(wjp%NK%>Ntpo!9@P`quRQoBGb_'
        b'|L^MCxges!4-|7P=KlIQ{k&pr2F>T$f~VI9PCezmdjXx%rgKm1kJymwiWFRCzk^8Pbo~yCOk75y=7jzp{8N(9w>{sFHScZoArf72'
        b'4@mx_^<2yJ{`yDyla>Wfr=2?F9zpQXi5;Q7$cY^zHt2jt=CcZp1F%!MH~<?B75$}1#ZB#}w>yYw90PfB_qTnb&d=Bo-@mIw=15K8'
        b'<o%8!Ra%t8pN2x!yHHqN`Zeb8Cqc4f21<evQ0hb5S?%)vy0N~rd_hv(&dsD1p7)2hd+2y!Nkx-F=o}kTxDM>p_gAGycW-At+D(8x'
        b'X&CEkPmjqWTTfE+z6V$6g;49D(r;wCQKV4aQ}0eaMtBEtPyH{p3WPO*O!_N$4&F^f>Jh@~!%?mCiAcPE1A*-5)dcr-U)J~Y2(Gq|'
        b'C-85|JzP#rg7kUP{$(H6-zWG_&gX>-xI=5&tXfU10%xkc2zL|_^8~=g?Q4YeBhqlO&*3lPHBX@a6_IG&d5p~Ax2%jIyobq>^q7Y$'
        b'?gQNMzV1Wtza&1UGqHoe2~H7B2X#~5IMlG@9*>r%FCqy=4^bxiP*c5!?}HpKiHVsZR}cK|n7sa6-^i2qK;)4`a<z=i)~{SIacHHE'
        b'Vtng*qrIii^Sf{sI#q6-WMnpjj*ju7!7()V1^up7JL_-s8TR)j(Vqkz#guzJ8glzPeOZ!~8<X6xTo6AqyxSM#Qyr?A0Y1gByU(#A'
        b'dE_o--wTBnZ+yi4R$rvhzP<oyGSv13vNH^;F9cQS*q4!(5ab9XrT&s^8R)Cu+t==obw7zJG5oUc;YlwI-_Qlyu^^9*dTAJ-x!3v('
        b'OD?qYOpmHCNazE+QX4yg`$eC?Wuy_2rIFHC$HetHD4J+<QCt4*5Tl8%HxO4vIKLWb)yP&O;|ch#S~Q-3@2bTTFQKS*H3KOyo+2S_'
        b'RDKp@M55Z_2bN~>17t9P=_8s3k&l4weP9}hr;LJB4RDWw<Uygxe5H$LKqCb~lCDt(n!<iaI@rK_;bxX<7dhXb&(tsL0}0Y93R9HS'
        b'UVvl|_c%NUxOt`-NT&F0RDDjLK40k<0WOoE&=$`W#O&N0MJJY(#X3%m+H_S8r5Xx=-(UMC!|q{yc6CZ7A+?V2<ey!87<BgobV1DT'
        b'FpW9<)6fi;6BGO?nK5X69G8rUS<kz&h*dFyGd_z?6CBP2!8w_CCI;J{ruS;I6w)c+gZWF*+(HmbHU32KKaJ*N;==YdeY_tB1Ak=7'
        b'J%h4uvqU(L^Vu2IaX&u}fH!Mb&1rG={rt<-|J-&yiEbj?F^KT!cv|9Lxzhn;(%pNE5H!o^Pj(d(9e5bswIcY-P(AhV@G?|ly*~y9'
        b'T)?krn5_u3y-*T&uVop~5ChNdF;U#basRwPlYX=$Z3^Fmmvc$0+a26gQ0G7I5!&^uH9R-Xy9?t}7t>Kf`xqU!BTD~E<Re$^RPgQJ'
        b'fbUtklki>}3*f7uza{Ak!_^BszRE$yqO}HtVCuz}a|!(M1V^#7yg16iO%}Ms)%-j`i!mL&WA@+n`tVP|qT(e}9g=BmI)j!8pSj?X'
        b'MDM$}FPK?0SrwH{O6DM!7@JVukMmJE^e>UkvN#9K5;_hZ9o$S5uZikYzk~(bm?lE|6yYFp)D1BwiV5iwtO48_E&&=MIFq1qhjR*Q'
        b'g>#xf<T#vDGmBq#Q+)w$n(GMbapsi-42EC!f?ICWgjftM5J2%SJ!Uv~0UY>%W)5kdrZVS^{MKN2<-ZqWFu4YwX1H;IWfN^iaaNKc'
        b'yc%@Mm7%0pMJ6*0x@jIU_G<=U(LnKxl0#I>a~JA=cA??>NzisQM!7`8+Y+A0$t+6bR`#m!M374ut~2@3huSR$?$HZ@q8TIaQY}wk'
        b's4u*r{ccjd=R%}|y#FMtbFC)k#r%lpl3DlAvcZ?fP&2$;XxZQC3(z{26vLO7!VH$^?GKBUKiyy=I{uE#T<&KVL@E9MM%Ra=OTwJK'
        b'HyFTpei?g|DOie&WVOY;vKN`*ZCiloN@NOq3&6pE#2da1ajP$sYcU`)An^9hS|G7)h{V$7{9Kc6?68la-LOV9aX1rCHQEKgfOzc1'
        b'F_pwXMhk&92HLNZ2yL1R*V<kn%^EV=*mG(N%8Z`o|AZyY$)v<2CLbZqQ%H#!o=J03z59Z82O<5*7*<}NXZWVK67<O;yu5yCCGcSW'
        b'7_XYt;FScmv!Q~KE%*HM*}*l2c^BH`7p`dxJ(}4q8!n&-;KkVs<xNDAr6H3{1$tjRrfpOH%bqX(LS)ZZ$zf$@qSSLkz(2L%pXxP~'
        b'zL^4H`ZVb}ih~JaGEmJtTV}*fK?=<eAI0kzU1$!n?S5?JN{CCk&?OJ@i|DC=`lTh;LRRV@7@FRXnTqC7SAhq82k~|q4oUEx(e!={'
        b'(UClc=E|WjGw`f>4!e-0DkpNYj5lJEc^-ytCOr*2Z#JD8{tFw}j}OT@HABP<Qs8oE$=2ue_Qu|Tf9;WcL5t!Q?ark=&gIvf%WgRH'
        b'8h!-=cd3Va;s%#@ja$~kEq{h~on$?SG1spc*Za!hYPS7%;ntIkzmxSeh0B_hu1?1PKHH!r-B)_+|JEA>H$y%zxPC^9@xnDu_c4A$'
        b'x4326g+|%A4|?0hSwqqsJ#vnKDgyg+kH`*8A-vy@mgnXUMm5$Siz<1I?tD4O%?xnzk{4-D04v{*yDHhTvYT6@V(U73K{<FPCzpW+'
        b'5Y-63I(h55G<QXB-Jg1e^%N)^SGkg(oE-Qa(jjH&jNs$~kPm5+CUV40aUb>uVv?o37+N*~B=@_puz$Aoy)atZ;6v+MQ;ku8*N%75'
        b'I{p1mqr3)q`LZ{FxFc<HDWAdnO`uG<pPdI2i6;_Dd4)=1A){xb1L$5kUz@5d$79RN)`IU)ZjP-V?gb8OkQ3alUV*oFo=5w1_MDIG'
        b'*Xa0Qv|NL0_bL6EtsXz_@MHQ_Rm>bE7?t+g^R`teoZxU~9Ec~Z2S>r6$s)MAUZLoTj)u|tQ@v$IaMBrQ1bDy=6ant9kZxC>zw6N8'
        b'BfnAl=d|j}ccPs#ubwX}qnJviejZaM8UY8ut9*0Ru(6kS<_H?QLxX`xa}+-ztsMmc@M3RTOewGC@mS%o3z^U6SP;0&NPWa#L{7s3'
        b'wv0ldziX_9DJy5UoCh2K`nb<z6#Xz1v#Wd%_pAId?l<m-{TTKe_qra0{VK(<U*&_aU*&_aAM(|*#v_05$^QpG?6Kbe?uW&l|2IEu'
        b'ZtuVPVfM`4h$}`)vIOn2)FMK!FTBC&&TZ*!!+YzW>z#+2hC^s*Z{ku5;4LDp7*5_&(F=NlG|w~zz*S%BPCGBoXwJ0F51B|gj8e-B'
        b'y;adhB*-K}mDzx?XfBa&W1zfyYNW6M71qeB@R^`sS_*ra1i8kXtdWRo!^}$=r5x0WI|da-6OxG`mXnkC6Do<hCBIi=o}$4G&<2c<'
        b'gN(;8IhvV_LWKbuKxR~Okfc5BTiVW?SDBNJ5!T<2jm#OBg&-G4rr)bclz#cGfX6xxyU^-%b1XOqNfL3Fs9I1aI09IGdarGq023Mp'
        b'@g|~Sgy;z0FEL0AkMwf2=YtvyL5rEBO$BJ)v){ISaGt$Hb&-%;vWk%YGYn>E4ox_mGZ#wAIsG$)_aC4MxII1KfABGTeHU;xnJVM;'
        b't)kP1crAJXNH4X8atC@y$=pENVh|;O;h-}QW4|7jV?i#@|5&U(&<aTQzfx7cWC4hn%$Qgx%%?2@Cjgz9edWCS*XP9vm-#+!fkUL?'
        b'bjDRi0U?9;i;Ub0K+85ni2|bKKL8mGiy0{OQp5p{q#oM9Vv6TxfdkCiC>|W(e4tsz2ASXh+kgxo^NTq^#bV}b@Qh-JD^c(a2pLEi'
        b'MMXrP8672?E<Pg<d7+0h+gil{VkdHF?QfiK<<SJaEs|W@(~4GnJT8Vg=b1iNwzi8Na@BdX=%bTiJ6Y~e=SB0V-M+q|p5TcE0cTEU'
        b'jQ7{~xhH#?$jBW}^}ElzpFnu&_|N-3E+=I&;oW<`#eBZrdcI-ZB=0WdI$1b$443D@ytYZ4*LHPN!Na4#_t%He#J1(|y>1>Y6)?dw'
        b'uz#o0R0b$ww^Tqzcct=$n;?=43#rypC1e!xY>|kyLK|8!1z0N-t#+45bQ^L|4^60hk45(7IY0<3fe%@mNsJlfj8BO}4)DGO5LbY}'
        b'0t5@Ne=SwG2PJEH*8JFc5C!PjPgww2hrm5xNph~~9i>^-<IpUESD5K*$TXR5o+!#`qDJhYZw9!io}{I8BF|ggZiJlobq4MEbX^*0'
        b'S%a-k>?}G+S_yQ7UzVkyDtyoq;PlqGZ?UK6IGlRv{cw+FF`d-iU2#m(L|LPe<JI_udX0F5Cw|X8?Yu#CKJ8BW{>~om(;jraN(@yA'
        b'F0lU_?I_i_pZ6E1CKA@iF%Ijo@K4lyI!vMcW&15q$F6TM4<E1o>zI$5&nwqkP!y+jm}(9Jf{epQSyMN)<qC|)FghAd=swB<0c{Dw'
        b'SfHy!kFvF8)RuA>3rLk6WnZ`f|6xRcd|^-ukFxB;u|RvffCMc-#DMT3AmSYKk&nwV9c3-x$fYPv;+3VA-=QE4P;ey4bB|g;6g!kC'
        b'7A^uY)l&R>VHCpIgCLj(dTNg%GPQ}H6mgH6gXiEwcs8X#0k-*%6x!^497Ou#AfjC^3JpB~;pTgs8K6FFz*OkuJ*ddU4pSgS+PQ_m'
        b'X*_54Z~~NUZKYV20!;Xvvn=9D8PF^q?y+{Kfp=z^S}Evqt%(BmOPQZuceICor1~zc@SXg$_D@yKwH1R)6i1qWTh)1~<ry?KzA04g'
        b'E=s**s{8G8H`3JV$0vG}>%}!;fbK1quJ2IRzQwq<v0IJ~?^8l<?OW`Y&8}@s_eYRoU$_fzTfIss5CqH~VVd7Wx72w+Hf&@3zeh!o'
        b'Tl^LSW>2jL6?46%4E`<*C84WOvh0Wwt<c#9s5e02!fi_5d*MipFc@IH**;d*{jvvaxLV|nXFwU#Hf7y2=fI?UP;8za%DmcxZV@@c'
        b'2JPz+iYH;yx4T>wZ_B~r149qYy${o9L}lLMZ_xQ5{_w+Y{+-=&x%oQ=sA|j6?kjBb5Cino+Qn{prMVL^cG(v8g?r7F45FcRZ1YP>'
        b'$Kk8C0;VjVMf-vC86X|gBDNN20)$^O)6UIA9vtxSvT-JNG=+O$ToIES%9bN0FI=Pqu@`w;#ATV6_t@S={0!!iIprMURe05iIQc{o'
        b'A<YWc=k+XT&kd#iTFFg5$MdhMJs6rCATZDe=nkpLM90i97jv%upYWEU-+(s_PO2k491uJCiP*^jf25P2KqvhVJNdHzVJAa=v6F$r'
        b'SD~N&QU*;F6|ey`OEliez~R^YIjD!Vpt_P-utZ%ipl}3q4+%VwQqPRbIp`{M>|sCcu{}t(y{j~T*A2;bv};W4<oinVq@Esb9whb0'
        b'5DLJXXc_HZ9^H)grr%_rtlAgrIeE=>cW2FS%>&(*<X3CZ#d~zaYSK>i(3E9SH7!|fbYw@bR)L3Z$^NRQArQbU*|F|(=TJ0&vSepi'
        b'RLPFtVYVE`p;1~^B=0Mssa0{7Y`vv;(vtHQiLB`GKMHdg%OaV%xtmUPBrgNCS973<o3W~($iH?~+_Q5Wy|_bSiYn0-CEMr{v{L!A'
        b'5ZJXv;0Ug-DlAYIsggY)mrK#96^<3?0CKnYoMY7_btM+`uWeF{oFEIXNm{O*3y`tebb03*AjAbXFbwM2HNpqmUZ6i|NR{t<**<U%'
        b'ozsqj8K+V6Yt|f-(4T0*VF*p6<t5)L?0dQcWQIdKby$KW$=$opMNT9B4f^kVzuS=#U-MbekJC{Bjhy|c3QE~`bO-!n4#~&m{!v>2'
        b'Wjjzc@(a;nKgHCP^U2F9%L(sq$I|A~==^i(+en!IhR3}2>vW!X_utXJ8l3y>ISnzJ8#u>eiIJs5EINk~dD|T`ZgvcR*QxT({J|P`'
        b'8{M~Ps-R_CW6gEeb9#M6d$cW+o<lD=ChPIziak3NyPoEEt$1Ykpz@ICPy^ZyB*%745JAaRa%zVH!<S+^&UYphM32%jY?>Yz3Z2Q0'
        b'<8KpOMfcC^Z}7R?taD4;LE>ZX{JGV2Jb^uXuAE~(@=WaEI6A5JAPc-N-W!9bS@87X66JI0Dm<FRWg7`>_;sbqOs9XbJ)JZwu=vDc'
        b'0wZzyxngW?;tDA|Dz;Z)+Qe+Mpn*>R-s5Dj*AxF7uf${_tSW@*Ll_alxDdvK%IXX08-La<;AVE)h>#0=9-(3h#)>%cnlL?Djjp6)'
        b'Ftq(Z%@EJiAzJ3eF-X(%>CLV*K;Zdf<e%g5W6??Usd}GNeZv`>ZH`%CRu-F88_jVnTj7rG7Eh#A-{4}i@t763vKUuw#N*<x5gm`C'
        b')~fIcj4g4vLFun|t;nNNuMysbU^devJ^`~Nx<|T)bCh}Y*?Ck@_Ay`wDxs6WNCgA|Q1$k2q58MUB)axvbQ5Q}U*`VyEL2$OA-uD|'
        b'pq`+?6)Y}Ct3>TCauF7Fjj)dA(~$2z)6Fs6d1ju^1=vsnnS;?u00@!MZ^IE3MAO$`aIOD^TukV?j$UtVMbBvI8Hb^*GYoAR-zj)B'
        b'%;L{W{}6^GeTu#){Sa;HT8dx<fhxS{&Mx$7JH6X_7@o@_8*=^>##V-)0+YCDM%o_6tRZh}IO_{iim6CUoKGaAXTlgB@^*%Kj>-C-'
        b'B+#4jTD#C2X=fPGSi5)&U!YBIamKm_5H6rQ4RxdiPkP~^D~Cx+bLFrtA9P#HfJQw{EvYLxKCx~8Sq&cR8N_>J@6frdt)hu~TefLi'
        b's-k*pK0BPNENau|eVCW6qOd84NCn2k=(Y}_!)Q<}XDPPuI+i#<(n|1pNOSDSRy~Qwic4v9hW74bxIkt=O{5tU%+s_pNyCP2I>(YN'
        b'=d%^sH4}LM+LD<QN>-!GDgzoNdx%kQk3v_5YLwis&aPZ5_wX_GigPr&s(am9xdl?PbMz}9J_Gz@bgWu#MZnJbbJ)ca@g;T+GzW!='
        b'5MtD8arY>qzmfYSjV|LtTl&t6>uY#r{pxNSsh^S=6X+OdkM(vK(>C3)4o1#<uKVd(S{9gmZr5{4AY;~5$W}A1J0_Q_&~x&U>DA5X'
        b'X6m$r>NJH>pH?NF`|QT-^Sd1qn>s&Hy+6+8N>15KSf9dZna@uu_8@T)JhUI3My<e{pLL_NVAbM^Ml`zkl<JzvAEx!Eq!Hf5ST=!a'
        b'NElz7r4o$<L7H(8U}&?TnLxW(jEP1wX{0bcCB_P$z*tS<5oIGsnxz^urZQ7Tv&3C~R`gYY)+w7VWQxgy5(bq8cfW8}T<j!O;TYNk'
        b'h36S@327mW77Q)Hr0~cB%8q5I{vby%Ok$%FAgj!n`x*2pkeyNdR1YvY1QT<wjJzPSBQRt05PS;(M5lu0Q$z%&HxHEwa^%0l%pHfR'
        b'flu?$r$-Ep9D-?yyugj(3zI4W6NjeK+4Z;2yiIP}woqZr%%9^NJ44D-ZF587s^OI3Dy1vva=q?SDKJt-X=I3hklZs|jx0mQG$GAW'
        b'EO2Ug>UASUnZ$rAaP<F#MDDEU!;4518yDp807oJ;CXS;Kbs1=#%Cj~hUZ*4xog!@uL)(vV(A5BkkN0)Lcwf;s^HG-`;4f+%e;V-x'
        b'AXa)fOj6PaDC_a?L$v(}D|F_+kHt9NZbn|<5642<g6==4J9NhFI~%x!Uz>ccC3vPsKA(Qw^c};?Y!>-Df{do~y1OacqaoY$kZozG'
        b'OTMYbpg45Ek&CH9HKSN;=)elOeR}tBNVz7gnuL+jsTeNbcjZ9uBr-QilgoNe-uHbzjQF4s3u$tb$XwPM3KuFv@LC1Wx5L5pY;b)N'
        b'I?W(*e}wl8x_~|I9B`NUg|nHZkI;)Y)SRKo7bS}Pl@5upc1HQy1k0!Q6{Q6o;w=EQwfq9EC|&0;c%t4}w`#sS<18sjwIzgV_SZ?e'
        b'hrQ^o2$c*I<I%}vPC_KC-$3XCYi9r)$7jO@x9)X(gX(vepRvh8>J_7Px6Z<cd#gc<L%Y#c8ra-6+?;#X5{p@!Tum|(8{%G94fn#?'
        b'CfvE|jDu(xSwQk2PJ6-BOG-AOAY2l+^{j>Ccp_s-9dDk-twEi8RZ8dZPSzF^q7xK3!^ujv&V|LAu*Ukpvk5*<v-lF4<!vcAOGc&o'
        b'6jM?1S6JQBGq&_lL<w8BVRhYS#iXvi&BpF?q3bU4&VYdTr6+ovGgRh`;b=@(ckuJNg=f&T2P!(<!_83P8A!354Qp`L*Ji`mJY70S'
        b'4vm=|KURkc-QYNkGU>%D<=LA%Z#cQ~6T<~h{otN{hK>R3h;uuH_fKJqGeuoRk<yZu|2R9okp3rUM5WFF<u|7*b(_ejNf@qENlPCd'
        b'+M|-Li!ePr>rzw%4cY)>_wvpZUj3VL|5`SKD)N`G>#DBjE2rcaIn#?c&f!d^B@QR=aB3YLX`r)bfajRnB0C#sGig^(bSuu*Q)k*`'
        b'@6-*Sp(Rjtk)OK3X%wZH)O5Y9E^6HdTIP9nMzGBWL+X0ZMar>tgM`<NrSJr_`$n5-`(gMY^RVrQ;a#vz4~2p{EOHn(VAJQE-tN=^'
        b'PTd-jhwuzQDfGyLRxeF&=X7XgXd(bAbp6WZkzuZU*7y1Sg5TVBhr2v!Gxue|n8Md=I}5Op5hucc+B=f50LPZ7^&5g`j^PJ!=#OKu'
        b'qU0Ds=Xw^)8~#RX|BG&W@5~J@HPqSeWJ`HM`ZVV5?h2$K6&JA2^Ve4R8!Jj<2`h)~ke4P$ZMmbb*88iOW6{<}fSy~dXKjj*byK({'
        b'=j@F(8}P91w?H%Ajp!VAr>4l6>}?8{if9M|8s4)W6W7M)x*FL{+h>86Uzs+%TiM>G-}^^|Aq7_ZTUX1$E=@EB5`iV3hrxxu!`DE6'
        b'3$G(fLu^3p5oU+n^$J^doS~=CljsSp_jZ~tS9PCd{`gJpA-#V;6L9j&rGHE`SDf*1sro(4_MF`0Ceq^6Zn>$?(U(;)baL&|opo<^'
        b'9ix2d$$)(zXFznjlc$#i+Y0HaTgK2GGU+EDRqQz-d1TkhBt*88O;}fb>luA(K2v+P^#;e&vesYi^f>w8>HF^0XM7y*$W^?5shwkQ'
        b'aN6n&AD80#RjbQgxb<Kn_i`5~51x;q?}6@j-$DbeeTB42K>44e-FYww>FC1lH0AZp%)Y<W{j94rKD|9%S-<?uu_z#rVH)UuddoLw'
        b'0_j4@CsI05tGi=!%`Vvem2@hgbmcmQBR!`6DzGTJ4{n)cWz<CbGhOwU&p5O(L4OqTW!7}jiuFGP{KT*nk*0Jl7SM{O%z7|ovI-A@'
        b'H?8r%%lQ2jHHV7OSF-xkXP~T;KLaf*N{J~bz3I>@>(kGG{UX6i>S_C;E~n77>W6^38$<)-!BBgbVKl$t_!;NV&L|x2xm~t(RSpg)'
        b'A<g4tX)B1){QtG#qcgxMFK;HJfKJmk%<cjn4Yb*|?`4B5474vbvD}ZNqhBiP%gQQ%LBty!fE$1<w!06WbhBNyG$e2~Ve&0^$~NoE'
        b'@)?`0LWQ#!lczGX1)J{fBhAyGyO!kSCMlR@%cT}4?~Lg(;;bztvOiRz{w07+E;<=5$hx53F9E4CJ-ykY<i<Mlc(bevq?Ro<vSsiw'
        b'rvjR|)RK}+Pp9LtkB&Ey024ldGQ&%hZN@WsW(HBXO~0Qdb7HkmhSdZ6c_^+B@0<>bv-;ZIVMBKpS_YRb2l2s^Hg*=vXWQr)@9Sf9'
        b'j5P?Xk@^>O&^aKVeoN|)*n`Ii?)ft{Z-_Jgy`4Ya^<nSrWc3xExN{aiwrl;%P;<j1<A=Hp0e{%`2X+TZ(?jyk-9G==uD#F9ka?rA'
        b'sP(%3MD6sw&3lyS1|x!0#E7C+p^C;yg;HE)E~5!LRw}`o=qa5pw>fy4wSE_l`jVc)>ka0D>~Is=L11XN&O7xZx5Mh^#zbfF0v?de'
        b'x3_ot{gg+mJ|^B$qD>3<u>%R{x@Ga+@e2JR=8s<owaK)KmeH|qlUv`KxZq{+0(f*(g1%x$^a1i_jchr2VCSF5>9QJx4|||WD`+E_'
        b'Br(JB&SR9IS=>aR1#Jl~v<A2kfTKGs+fvT7aA%q*ZDzROllvJ1){Eo!Q{8ML4ivA|A2g3I8m82F68DQ;K0gIyEhJF2Ms(A)u!?f0'
        b'ccG;;wVkEgla9$f8m9hdU6G|)B_>iG!rdH777UEJrHFm&$uoi`hMo>hK}8-Tr(QR_)#+Z@C1`Tbk!QfGqmv%o35iZp{z7a|U1_K9'
        b'5*~<d^h6)@SF?fW1HR~Y;i0ygt;_9lxhewDHqR0oWUOb2?ZKV9t2^tjcX`s+1NFd*1G|&m3%dfcy{UU8zRBm-{VmQ1b`+61d4fk~'
        b'b8Ta4t6S;GuJoOe`<I^Xth?6bTc7Bz=&bt!9&+o3;dhDnn^$)geiuKu>!@z1i<a+*4*C-|y%BpdI(47oI-1l*yBgA_UY~O4^d6d!'
        b'jz;Lx-P={)(^W0w^Kf+<_Tzm{^<7<C?s)QWcPG58NqBglvWJMOTu)e2;6YaZX;)ITClA~DG0~yJ>e{=yPbyD+d_<xCdvwa?;#<`#'
        b'6xD!;57YkR)W<yv37yvYc2GfeF7*)6K$P^-=IUZk9zjp<+;M78do)GQYyG(D6P}JfCZEnvKf3kfjCMjYWshr6*-l8iJK6T1;L^Kc'
        b'thBnBCipx;N+Lguh^7+&2)~Bl0$piDO^kTo5!660sTIK=lhe@%*wwx5?X-N#9)M!K7v6FM`s=+Bj@-M(z1c;RX@p?MmlMwre~jrC'
        b'l&rCJ*r;^YcF}}z{Hy1T=tV$-qjPpnRg)<R%hZ3RJSWFox+>4{uQGp==~3cazO>mWeKljNX1AO-nW*bIN=TU?^#LnRGU>%tQZBZ_'
        b'RSkbi7tc<;zEFnlXI(D$ej9#9Zv7@QCWZ}NU^C{D@6Ya@tuz^1-9W!arEvWIcBAFw{c2LZ3X9yz2TfbN^ScOrly;d+6}x4n>FMsZ'
        b'UAtwpEG2zm_ckzUTkC$>g$^XxR-KEkjTCPm+9B_Vg1(QxFZh4FrxVmK-;3M^3b1z&NzpX1bspWlTj^fXwYPe=tX908Z*D!-M2?K2'
        b'^MXvKn}vlHJLH`@T9|s>CzsO8Gvu{RRqJ%$4b&$s1HH1%-Q$dQe|8$N+`=y29OaW^rZn@EkAry_Z;q}vba95RJviM-Peul+nG(!0'
        b'i&<V?gt?EPkE-1l>q<91LOXiQ65cFrnbFnm$C-Lodp#`pv1Ql%nw{thb9LWsK}OLY^-j4Ulf1tXit=U&lwdgadbToe5t!yvjHb=z'
        b'a*M)Zp{MiUAQX&w{~qRL((7}P2&)lZnX5ON1@nZrjP&b}VKGYuvxL5x`Fo<{M7YRIzaLnR17YA3G6h096lM)(B>d*Mid0ykz9OoK'
        b'D9kboITNSwQ*t_f2rtAtrL_9GWxQ@4)tx=jl09j<F;aJD7+MI`*Iaugh1GCB;i1h?i?<_uJw^Ew9<Up^6VyhA4BI<F^VyyXp|w7$'
        b'M4O<q6@?gm9$0I7i;j`z*-Ao~Ij@k=F%p!?km4_uCtk=0Fpg~Wyo)vOX0}e201cHK3cIf$<fiDJK*H}kLcNAUfzfY?&O9;XfsIIr'
        b'nwLl3AiQ@Gw;=i$i6aI>X~leuba7EawaVp+ElprXo+N7yH5Q*-k#;CZqT7tQs7^ixEAZUo{bSN^L1wz~9Z|ef{VIt#Age-fvcrPX'
        b';#Bd@DHe{MuSHro8Ql5=T|OxRgEwJYo6GeQX$D6nzR1bAKSEm5{HN0aXH0-gG%eLXqd+mL7L@J&`1HYZt~c}^XPk#qEmzF1Zj^bP'
        b'ocj=Z+0MlbN!*Q{;^JFXz?r1WZ$y4V&^gszk8)3*8=~C)PI2B?9dJ&YpVdePosYQpM!rt!;ieXGdiU<}5(mG~r8N>CfA998j2`Zh'
        b'c5a%xP6YJD4EaLE#qR@LOpuFp??8FW<<BS@&jq=-E@FsuSEH;h`H-TCIwo;fJtz?QKrG>k0J``+0wsRve&yju#4*xcDW<3)NrQ2g'
        b'`=w5Cm)xJ#g!C1Rd$tq&3mY-M3(flqrbzi?4@R6CUnNkA3bz$?o-68%JkO8^xQWe=vhKovtKk_DrT;4eT8N)`;LE4EzEeEEL@h`x'
        b'?_fc0s>#R(xFliaM0b9txIg2OfKwI#G}y(D>I`!_@3dXxn3KS>LBKhuo~L{k9eN6CyG*AH#7`8O!eC0UhuFZ%i7K4oe5V*(t|G=m'
        b'JsmkH)&}+@IuOS?iyJ+y!6%AGg6N>|G5NzgklZIvL4^%tGi|yMR`j*{!wG!+#Fa%Bfs2QcvT&+ljZ&ATOIDE>(3f!dDuyQl1XFW}'
        b'#3x4JYtv?d1&d-Gm<~SH^9;Ed<5y0^<_<J|Vfr9sG&AnQr^E}zCJKIv=cXu(nK62x+00lSR01_P+8Es;-6|kGl>}qcTu@bzW1uS3'
        b'LcjR!TCBi$pWAgx1^pmG9MQ?(YoJ5iwo`gehkC}yx#OpolXM&t13siCa&Q@1{)Q(Y$H^SO?oBP=@mN&D@h~#i4F5O{U9hP_Q&M2K'
        b'v6SQ9*TXZU9aUkB4lWK7UOTXmW=f9xZ>PnkGXX9+=v2B#PDePRhl>q36N1jk0gefBO82$XqFQ)c(aufi;o^Y(g4|?}Q|oi4xG$d;'
        b'31172kVqr4W6|zjl;`e4zhKUf0~9|Z&8hCQ51^eqCjvuNi~~FQKLBfwv@s^=j3x0@gtVh5=is@ZGwuQCBp^HYM`Ep_I^a3(<hg@{'
        b'2!0w6An&K#hsD>;ksA27iG#9D+tNHRV0>!AG!Mt7CO`vK!ye`K_kwNA_BX(dk3@XHsb6?Kz^RT!jWmTpV5KG!(s#pC@}+?=_%;(U'
        b'$$&najgSj;ucUh>G&A6w0Lg}LW@_+6bX-%6&WOir@Ci_WRiQoT?(L`{kO_q$A0vTw6C=H3@inNIo`=0ex3FO-{+>jeevhUi+^0WB'
        b'efh=dy8h2?xgp!+5I9pNT<(^i2B#^qZ`~#ft&n2H1g4>|Yzb!S3z<F(nTA8A--k?r&<eA(*c_!Yt2AaR+blt$^|!(rDZZ1!_e=0>'
        b'0!Lx?`C|F@kf}Fh`XppJ7}A*KMsv(gvuwXPI@_#3N?~_+1&$TtsJseS8Sxn4l@(^X*gS!jF{Z@2g44FuA(Q0!O^kIAWw`C9ZL2~y'
        b'N<8b!h(Qi$4IJvvHZw*urZM9syTSl08)wvsxV!HZ#)QOxk+>JXBRuswW0Kclr!Q`>?FrT9=uSG1*c;8JuR`0t03c$Al+Z?i*6^QU'
        b'0AhPNbg|`ReUOU|a55;i(L71JBV3FoX_R%}oni~*wu2$t-Vn6h|K^&F_@uh@)74)vt3x}{G*PVnSvj^V1U&;#{@<)&o(&b|%h54l'
        b'60rlP!br4ahA=9$Bg%R_?0)xi%pS6>4;4O@=RR->jg8n->u2GM8^)VD68hJMt}sv3z79B?INs1Bb*P;qsGSWSXeSL#a({ZN%qmB?'
        b'Z46;ML;hc{v271Q``u%wm?hBA3D8g%G}MP03ZTXtnj?pXM5cYL4G$VB33a>;`nC-tDe}lu^}jepnkn}$5IH$>K7W<U{r$oEXYJr<'
        b'N3E5RQBkB>;(YA$XPxomDXIC(Q)HA(beeTEg#_?tGgVO(NfMEG|G^F7X+A)sq*>wS5ZoziL0BHCH|-CN^Z{$283UHlkx|t6m_CKA'
        b'KR`y|Dw3F93UWQK)XaTun;jCTwh}F=im0_R6)q`MhE!%r{92g?mlpCsiBcmjfoHS&b5<os<#9P_mXT3XJ#yzKYjBwnmoa>zUavC+'
        b'Lr}YW5o*oBb(WZk;8o_Z7RN+$)aN7~^&kX5bO^}b%xAXMSq{6(@|B8G_1p<$6k)`v-5;U3GE%OIijI0#VvM5nSR%{hu|d>Tl^N5%'
        b'5LUk|FKHvx^X0yniCg~a+Qax96MX~~2w<i?tj|LEVi-R>I2a%F=~=?dVI)qdaM>}mh#av1F|sbK)=77N6#p!W>LKp>BhmS?`&HEL'
        b'g1rD>BAqCLKyYho*8<QKHQ`OhND@0nAP`tXaTpoz%cb7>us8uqY4E6H1c(%INQee!xM1)1Q?I+%A)spA57zr(4U8X-siLBxB}ASE'
        b'mxx7C>sWDGsN|>N0^JW%<PbqQC=Er8xRfE*j8_UJ^<v49pM(pZyXi$IRC>5*GK%z^#IXc4_-OWy_Bf*(J_Hh=5ecw}1VH*k4&4AM'
        b'1S|t~F)~pV=?#nGJXk|PSpD@)z+Ipz?0)N{e-ERA5!=IpOaN4h0SzDniXlM2DvlBGxrj>big3Z#UrIlV_)MOdiN1q>M+;=$jRhZ^'
        b'BxiXX6Fr(mqy_U7MY~@<31U^e3VXhA9#37L;SQW^qfdF#^3WZ*;@&!V7+D^6CnBt&rA<0U?I38v3%GVa^?6YCvHFcs_peW$3xDoO'
        b'%cYaV8>$M{+^26$y*^^Y)$>O)<PFQ^BejZ>5``7)btjgNyQQCt#&z__+e9NyD@qz7{&hVz&s|tu0nWm+_|Lg{&TSin*opMyS|eLn'
        b'_)<9+D?BxEcrH40E=uxn0vBBD-IYKFrIQKi42(3BN8Cwt6UcSB+jLT#Op+g?$ZV`h(qIm&Kao{Chf9^iyOq@&_P)8t3=i<n{@l81'
        b'?vI-zU_~pj0wDU{KeE?Hn(;k#Xu=rBeX$e8ch6UIbfThq8;2<Jsfh(?@r`b@G{c>Y>N8CIoF*(JmilW2PvU|f*YkQb)yYy)3Z1f('
        b'jUA(!BqLdfULvjp5THb5CZ*@X;!CteW^TCP)NS$DVhxU~qDbIo&<_#y1}*X&9z$IA)I<`;VE`k&GltazA>aPoUA`3;liMbpY+MV7'
        b'{Zq7h`&}PJ(bH;M%)>|ZTZWpOsq614yFX_9N7=@;!5nJ$p_5NtYWZ6|x>lB={#x&^Ghb{O-lMOrrLON$b`LPMZ?nD}${jiZWNS-^'
        b'C?whV4vjCvzNpDHp9hkqZ8uKrK7`_=(U>nVK;q;sUp$(CM2ja#Rt&$@T|GfYlOV2qQ3=rIT0aFS6$M5FlVabssbTe+@2cx+asje>'
        b'-d}r?iS}ekkfNZDl3;W};$OTifR{S_b6<3{`q{5MoD@(1<LKe2y}Que<ubqqGG21A>J4b1?R$5j<s{KqBvZ?U3qr$IKk~h>dAQ-@'
        b'6BavBPA1S)`H3;XPn6BBa{m;K<g4UD3TU)pBk`hq@m>k7nL$pyZvWj0A#U&1;z@@76K$5y1x+3dCyLjZYfsi4I6+J3T+?ipo}#E8'
        b'Zd4u$po!_|<ZWgQ*X=QU%ptY$#LV{O83%7xn|&M^<cJfA3Utxod-eW&7POD=^I^-U_Y3}d&wTQvg^IOgXPA$jsJ!qBEqzt$Nfv5$'
        b'pTvPFBj+TbYmZgbmWv>`(c=orzWanvNqDr@+WizgWsee>kJ|sk*xSH0bzYC-H#avgBo|Ep0|IWz4S{H}18fDYT_sS!mu?U>qH8ya'
        b'2B~ZJRcfnsc1uDFk<txgt3Y+lO`C#LrU~*QFY=}VEv{-?+uC-cwo&W0mQ|}3f%`k>CbVw*e*XXO=abLP^Ln21oaa2}InR0Ca?#ib'
        b'lTkfco=7md2sZo_ze2AQkhGl9<uu8`Q+0t3XA)A+NV>z%HmUiyv*)RNqu|Kt<D3bps*i5jizr(R(#7c}_SKR8i=5LX^tnWCVgBY<'
        b'_w1`Ab1q=YzSvXri%pW+RL^nRky(>^M%FETPDamak^*Pc2w<j@U#WD@oVI)KP<5li+NgF2+=bI}hPZY?6A5MLB%C8tCHs<&!0n;y'
        b'6>Rnpqf=Phd8FKg=Ub2|S8O*2`8)Fn+YNLi)m_2FS_M9dF^h0&=eV`^)DGCSbDi2`z4G9@wV&J9PtUz1$LgOM0;B;LO&WDMAa2QE'
        b'IU^z>@U<XG6>dyO{gebkKn#Yd<+|%c;Fp4epA0fH_HHwifsceh9NwgchSf+aC6y}Q&LNaYiq=~hw6`)VDDjohnrx<Qs9R{Kh$=ny'
        b'_a@R3DVQr$#d3B^w(}r}X0*wv?b$NjeR9iB<$(w}J_d*OuJJ*&^@cNYdc{l;_O)fCTS%Ce3YZns1Ch7gb3`CkRBH+K5z6w5u+UzK'
        b'2TAqft(wjuql+*a;U_2{0qt|E&2r7vK{H94R*F=6rA3lKp-9PZl=wAmd`9tL>H7jkval#@Fx_0rTp$@T#^e;c6QhB34k~SpLqQ|A'
        b'YOTojdvvoqhnU0&AOBtl<KnRFjn5x^kTR3`w0zxq95c*@d|mV;O?oa0ioyp?3#S_rQy?iVSKS!r7a08i;up)V<LK&kQI@}l*=Ow4'
        b'hz6~U!ekJzgM;=&g^xF{vt>iT^13V{P!?7d>!EJD6Muv}?b=$k)a@cXlG~~iRFlxNb8@ciLCP&zXiikoa$vL(F=2Z5767-shg`zw'
        b'ewO*n&|*fB>m<wXA#@a=mwDN5NJvo~y-vr`B6Z6iG^-Ot>Vd(X-`It;l}WJ+^8q8<#vvvve_1<pZ71+ut)Tj#+Fm58%{*45dwQ}a'
        b'bFR!$&|dUlm}%@*oTIJg;#>-C_QZapZ8?@)yp*D4mQTZg27Z3S(<fi>jWSbHHn{UTG)p(NZeB`C%6;_BCLvJHBAoQ33%sulvab&Y'
        b'en*$%!_gYn?`E(;Y&qBjnx_XDvONiU-5D<Ve9oB=uh|SkbeJ=5+OT^Ox%;O>OkVh0V2#}ihx$Gmq+jiIyXCd6*E2^dm5q*3htg{A'
        b'wGXA(mk>#vAIz2U;|<!=BE~c+Lo{VDOw&B)Pf6LD&x~p24vl0fmon=FpzAK1N5bIyb_yZuOBf=muXU{_7F;|d1WhPKtG>xBldP9&'
        b'#s+crPR#Mf4-t#6{p;A^T={tyw`iIi>bceTHuu4v`+EC(<;lsPrx^&-F^U<UT!fFet8sJ@%bDbN`Ip>@%!Waxe-gA@fR%HVBVL-e'
        b'f9vQQ?z=1TJXXSL-TH{kzKp<L$Np)Mu5m4K%bCSlnIrcpm*V@eDGPej22ud%zV^BU)Kp!Q|E_kcZ9{&b=>BU>q^%iU^2SE@qA*%+'
        b'hZ#_eJo(FgH54tiF9meujlQLVobQ5p+l9&Rclexgf?m3M=5LZ);$B=`D{{&O_P0q|)-5|D`=^Y4h5qrAGSw;S{He1a+<*T+I?wJ`'
        b'@1Gg>)s+@W>yy-?rRCwo?hghB7u*=xuRMKfbXa+Dc=Rx`Seyg;$3L2y<l=G8dFuS9;_APZjdrFS=~kHTObjoj=b)`a?dUy4fg&QL'
        b'WjS}a_#NUgUTzc$&8~^H#&1MKoTv1i_ebARZ>$jYiv;eIAn-qxza)Q5en3v|qkp7&lrj&W-I#vwx^{I{objY!b$WDFxV(0xU0L}e'
        b'P<E4}ds@GYh->uU;JU+2bGf)${vP%I;q$b(_cvuDpQfC>pfEK}3_mbe4sBKN%}GLfG5D~@Gm2?%hG~k!?k(6e7`(<X`Tf<e;bOOX'
        b'POmVVkTbJ|C;|#<2k)s3Ccxt{gzE8$2S=aTB`w$#%9isl)EV)nDI$(>5zi<Rd20h<`DU&#xJihJ)#MD?T?B6%LL(pJ5)k?U-maTz'
        b'AB3#ISsTNjHp3yfb8hg>0mEs5JiCe-2C-}^6X>c1t~qLzZ_+k+GQUObxV>l&o(;Ll1%4vP*Qr&FgzmL4Izl}sq|cS#;P`ct%%dmY'
        b'PD?3M=Tl?(31g9<HKVpeDg;ZNL*o_B6f~yM_X4KfGIqp|yNo_N$!}sn>l)~p_JMIV-i$}2JHr-h#%7Ja6z2aY_n<WAc97556@#>#'
        b'9=3I1F5AyRV$fj=qzhse=oe%x$Xig@9cDQEH~L4PhAnE2f7(qFMR|kt&o}Mpmk^`Fiv7z+o>kWE15M6(>TF$I9AoO35Yq(l&1wJQ'
        b'-zzq6-ufiH`8Ru>6RT8I>FIYvp01qI(}zOtL*=f&>^ZbZpO;ano~PF1&8>Ppeq!(=h0k2+<wyaq$|l~k`Q`(3*Dn&|eiqkxAl&~s'
        b'M-(r^8<B4=BgG6+{EMrlr{6pizWFa@&(UYXU4JR--KJKhPwbm_wpQx@hU;(m+39EdUAAqDdI1+x{hiW=mv_|G7K;DDfqx==^PRHM'
        b'&0FQQD#;k#wlDqF+Pv}r#2hk7zEgd4dwX7yeDLhxiqrmYXyQzGakPA>@X7Gr-l*P<WoN{v-`Uqi`aj}oGs-{YOx(BoT2No9)r;Tf'
        b'2-Ea$_cfE{=egRLoO7Xlir@KZR16$5;nNUS5j(ANcAUd%y^kTK5VC9L)Y|3f|1sT_|6{sO{d6z@KViE+^xx%q?=H_&`ty*!DXcv#'
        b'>D7q#B~>4TzFWBqm#r!pDK%>}&fz>2Rh;oRnglt*r}uxKKCOMpp^r!O%1S$=x6ZM;8R3W=CX7POw<qYCOhg@wd$d%&Ymaq`;lGF1'
        b'Lz5tIcpc@aKhx*05i(IkM%d1a>N2G|<vr^>wPU7hp2BLQP(II7Cp)ZmMRH|*P591h5RO};v}&k<eo4auR3V}WHA6wa0;!Dre!x$M'
        b'y(CMULnQ54kv4}?y-SVER#r1sex){buiqI-z&HKN#6xKgVMWA`-SxfoVX{7_-z}BWa?eB4Z5K{}^wxuFI~%8?4k0a6>wD=Kbw(NL'
        b'@Nu>7(^16>4$z_V-&hZu|GZ1;jwH@@C`@tEeizw$TH$mFdSBhM^S$6qXmO*Wx>2p!?su;s8c4g0TI^7u;<l8^Jb1#CEIR8@q?csa'
        b'qv}?dWcK}!-z}5U%L4PK+auAsk4IqY@SX|Gv4Y4Td*>+KLh6az)}XaNi((+7S<1e7!glavXuX-pExFqF7(%k7O;??s08q}ue*=w?'
        b'hw#L0Mo2*$F<F#&6zNt_;4dma(I9fF>I|_$wRJ0uw2PN0=m?W^`eJ=qW}Y7iZ;v8;hwqH=cV6I0;+2Hz^KeE+C7G8p6k$Jn1tDe='
        b'n(`BFhMzg8DR&eBle8e7D?x2`xo#v~l)2m#<09!8m%hy9Rzefn8y<qZE;lC9i+oW;-@Se}DLvAfZAqNo)#!v2^}W_z3Yv7g1Xg$1'
        b'kxD#I;;O}yI`);&)*`F=hFV8CL{EHYl;RP?YW_GNlSeTso;JTaVKXCbps>}KBs&9mS^G-#rQCJJS(-X+B~Xu+F1D9h)m!nQK7B0R'
        b'pmr$c3X5wb)vr*rp;}u8bWp3aoedAUpqwdEK<~#sGI`QIlSnU#23ZfSwT8&ODrH=Xpc~so^AHdRU!S(QPB2V7%wd3u{kJjirz8-4'
        b'u2@y9_}AAbX|jEK>jPxYPl?6WDCf`w9bKJN23?8$$%({_C!H5b`%LMU>nAotgRYT|ysiA~Zznsdu=D=GDW%f#r2ON#sTWV~{2(oo'
        b'*j%fCi3Tb%wd$SCxNcsHmv}5T;JLPJrMgzJxK{m<)R{-E$#^_3ah9fdE<TmX#0cp~F(|?xe-|q7DJW3wzXXgAals?bg+gYIJ)U=N'
        b'vTOQJrXD}ZY|7E}ous3fP0KXBCutG0X{n|MLUT13m!}u1SK_0L!)a#|%Bt)g!z07W(|_q-PsDW|n+^kQ@jar{mXm3lmLR>LoU}Ix'
        b'{})qz%>$I7DYHxJ$U0QhFmIg^C$qK>2Aq*XdrTcI$2rkV>#;p^MfGtqy%2Zg%w~ZT;<D2QqKfYu3dz3IPhp0)tSYaV5d}MpTZ<fP'
        b't2t?{R9LMyObwGxt$p>gU(ho_in&+{*dZzQ0;9#*Zw@FMxX<VhCo_)?yq%UW8Y}1@h!hg}x-owER=X1t7kg3Buzfp#t2r=K3kXHT'
        b'*!O!eVc0gD7)f_h{2KCuQt{WJ`nj2zRgJdyPvCNki?Ew#x|vv*r+Eyw+~(LR+_#+6&nsMEVB&ITWC^KhT538$$Req5&;&v|JQZV1'
        b'LR@4vZFUh!uV@)9ne>Wi-J5Dlj!eIzaGsrse}tsN=-7%^a;w6Yte7=AS7c=39NN`2RFhbjEz^?WLXyU9WQtfJIc**}olwYx6rCbi'
        b'8r%j;kYhpv{RoLK8T98|<KM}lwNe^miI_+}i$W<2r6<I~Jo*tSJu^~D3#H+6rFil`?_HwqUAsPB{8!|C+oF?t=~Vp|oYY5-_iM}p'
        b'$>qif`5K{KXy_N5eFLOu??@wjt?;!yj+8wZsX8q-xCq0h_@o(fZ}Let`J`<lQZFx(CX=FmW}AJoo3u8l`(1k5Z!w2v{t0_Re4#;a'
        b'T+=wa!z7jHg}xI{oOMDc=pCt5&Z&h@ziX@UaLlLD3SXi=a`wF0+Sx0htIp1%BW8^zwZ39^eP?iONXih<Z!BhdXA5&a;F`j!q-zf~'
        b'zHw0gWVqGc>w03(rZ*18#X0(iVZO2z*XnhbIK393XdATpc}aC&m0!hrYbH-LFpji}ScPtct6>_9_Sy0EwSry7T}*Hf%FPq{j1XOH'
        b'*H7s6j*O%l5_H*6nC7b!4yGmz=%~>QRLm6Uhl2Y{Y*%3%hSYghrWXg|vbjKA;8}YFEhHmSKR>bYs>n_*-&PW9XJSC6+Vx6c*Af2Y'
        b'6q>cO!a(VDM$nSSlNha>h`6XZej<25E53X2(-Xm`7IF72ImYuaK{#I5l1c^$6BC>JWpvQq2z;VBe1eF%h!Z+KFCX3w;h?4hKB>n~'
        b'0Czg(RYd$Wv*QG4!7!yl1^ruYN<oL@^YKX+QXw>i2cc>W;Xp~dRtP;Qsb*Mn<V2)F3Sctk(J{eSF7YwiS)&TU9R7{f`2s<~8z=f*'
        b'PvqTC%bO_Mcl}V&_^M^i?i0&xe)JSR6;H3(V2o6Blg5?u!aeR2>NQ)9LdKXqqp;byA-3>!<A#~GPE2Z!q6>xwqA!yL&J!h~?K2*?'
        b'mFNoZe|Gm8Z$WGS<Lsv*dXN^=%Xc`@oEV-UA0`BI`ir8@7e(UiA!4q*FJ(uKy-$5GY)4H^*p8#sb-n$XsPmdg)dHsavvps}8?uS8'
        b')4sV0BaKfT%!WM9qKIIA+a)aD-ly2n4ml3WKYQu~9qZIY5b=wNM%Lxp>YGLYoC{&IT(7E~KO<bl>hottN(aYH^sOx=CrTwmX?9d;'
        b'f=V?gZ(l8xP$MrYE7^w1K1ctNPH25aM;9SG-TpSe^IB;e?B@;O3S0q;h_zMr3njvQ{g@(nS5FaP;|3ZexY-o%?2W`bdpm+TBBz>-'
        b'6c-Zi4bgUuQY%nYGLa;q+1{^K@@M^m_w*Zqe-R3E7nFnl38g%bI2avCMGGbTfty^iCYzSbm29ge%gYJPn*L{BcQVVLZLWCs=i4_V'
        b'$8M|4D?Kl8OJ;49J+$+dYg@{?jSAJ?>9)1~>(*^8?Nj7S$4q<qRp$9~VG=H}y@ch#>}uBl)DcCB5L$S1vD&<n#+z<*oV!SI@CG_v'
        b'T#@p`!7uW~V*rQFAyUR{+5M3`RY2^^i(z`{*6Db`A2}~G!uCx6l<bcT%KmwRh@kj~Ho>zGm+u&(XkoTeV%eEGJ|N7FD4Cb0CDT=8'
        b'wB`4jd;6hl%|0Q_R^+4-JHK<)rc}SGDBs1gN&UbAwelS`2g7nIIAL})fA@+oSHK@_lN5_0B?QbL*A-<h+m>^JD|&dqES9QN*Y|x#'
        b'`cHF3R|a6($eZtQ+L+_Vyh37ifXw+T7YP&=%n{>xtAc6$MHdHPXrl+{hoQiQ+X1XrELpfkL9T^HH2cTX2F4?E3Hd5hU?TPWK=6g@'
        b'X9$^w>jTWiI2lSkGcfgp@Kf`$6=_j44DU(rZdm+=TGz&D`Ujwqg`_mJx8_~~`#Gf$W>59=>~P2eeLMYgwNWD~$y{SB+>&u_O=)4@'
        b'<Ayb4Nm1cv3nDW9^|%?YZz_0eK>zUU`%%O`?0JbpSxxXua*>`eu1OGho=a5>AYW<62r@SHK`fiUlWI<6W(4xXjJZNm5GjbzhzEcO'
        b'&~6~(prVifniRJdkl3D@p*}p-F*TOw?Bk%a{#Q7ZHD^QnKM(Y~T@8(n-IW6k()O5xVGSU)kIg(dd)ES9rth{5u#N%!0>|u%wCNz9'
        b')r`hvx9h{eIcpT=8t7;2a>jor2+!>z0;j`lPYpQrq_afi$f%e}dVbIGu)dexs0ICIfZu%)#;@;%3-iJP2RYRoB5()NvQG}shq_5y'
        b'8CC)&V2G!Aps*q76=_X79hF`S@{*>Q5?NY_-0~(@6>GW8rT)3k@wuvSGHC`y%g|>2#ss6C2IzneRDPYG!)2QLYqG0%sZ~DESB9+i'
        b'^^8lVc0BdTQyDAw)g&@e)A@7C6_<qVD;u&sw*e6tA=LBM(?<2Yr}ouQ`jzPsA1;^e%3iS2wu49Q8y+q#UxeGb|Iml^dZmBom|gmJ'
        b'yMfU)+;psEAMW2}cI<fKj@2RRtx?(|riJE4#%WI3F*=TxRlil{YvK;bAbfM96893n#jUHw3y^}zf@5UrqkV4e{h;+(JG8}e(m$7Q'
        b'zI~I9r^7Ycf$C4n&Q@=AkfvkA`M0m1-CtJyky`bou+okeQi+?CRGm)FtEkiaw5e>&fbQWNsZaFNQg_z1)S|v!WQNvmkl@?#r0FS&'
        b'mWm?@g03sS$vNM)0pJ7S!_S?6`!)bog$YzwC*+P@Bn_a`@+AImxZ&H0Z@(Rvv4E_!yYnRFU*Ww<?#YVgzdK1uauywvUfXmQD^2cv'
        b'DkW4OGE|>i{dOUt${^65V(UiInKr>_*B3lJvF++*plBrq+udA!#)r0t`km4*_AhWW4Bz&C*-tM*bLJt8S9RR!CYyw|uhBzCl*3Hd'
        b'b}*PxQ&D*c?WD**pZ7VTh+2VNDllaT0#9?Qi-b+m$6o2P>lO4pykd=G{6~HK3QL6Q{H#o_m)+UVBt+1-a`c!?)fmsmDU-$P7zGTR'
        b'(JzVB6?^Pi)W(P?w~(-8Pc%t%LMf9lt4Rzwo|NQo-r6LwXyjEnOu~~8l5gG04B>X!R%SXgbQ5|59j2};t5$D4WX4BuMNk;~tNw0W'
        b'wkh6+>%8$Q&8^;z`^cPJLZ3#*LWpzd>u%CM^pEO}GV7c&^*w6HW-^WkF;jh`%{<r3`uYHnkLUflGF1nYETX0PYZY{KlQh464@|=G'
        b'%>d}E330n{PqRa?Tm;ei6=n7;f_4uFAY!fvA}Tgf#w;Q}!X#db^_xEd80)^37!ziJf<7W5OuoEe#Tb5rJih>(6OV8q^Tthb%}}q~'
        b'MKg?Wgdb07vDrXv;s4Eq8B~^p`Q}_ivgidsSeY#6$(Ae$)`gDQ3{(ySeGstP7m*l*s`+(46G6Bb#V3X|AXZd=H!e!f8r7%8%gO`5'
        b'fWgcXa|A%7<9LW(MZY^C%~B?`yv@<Fz&AJimpOtK^Jg`P+)HH6Jj`W|r0j?PW-V6OBd4Qx1y!0QFlNb&S?Z$K`mU6S?5YI&is?WI'
        b'T58X^V$n^Qq3&YL>W-vb4b<>8bHakEy%1Ej)SQqWj6$gR9FHOh(k!f16-QZ0!rWOxx3Jd3$>><iwwsm*xIjr*;7!i^Xdk<-PxqC~'
        b'v*9K!vy|M_otd<K+ly-}v2wGp#_azVbc5FU@j#8`VzgVlPPr^)P2#}A(t;;@<2M!F5A7l`%f0XRL7j0g?^D7-v(%lCic4$j$q&r9'
        b'#^%wHZDvxpNqEIfdRBhRs`_1S1&CkI|44DAY2*eYR7);B66l^(?VuPfWzdR@u9sKW;VYZ<Eu=q%FuQhd1n>PseJd%}gSQ&J3kiB}'
        b'(tI*!Ap{JqW7Y?bO`3L$<H~WMo-+#7v_ZW}VbVngIwl{1{uJRp%z0MbELmIXdR4E|r)_(g%z2E+ZNp_NyQ{VWyuSoT9XP~4A#C^e'
        b'+V!!jLQsoQ_})VVR)ndp{oU=d>NZGq&xXNt@ckPeW0)zH>z0{;IYxV-4P1;m2b2!8%egT&)$H1{F_six;Nlqndz{&|cVn!6<H9*+'
        b'*S?Lh@U2<b*h`ySIc4Q%xVM;`VYD6e-^@A9$r<q}Zc&1Nkb~J2=ppeh<Hi#h9&%1{v>SKt*<A+!OCU_eQBr&_c>h!pg{D?IYVoR+'
        b'9D;a@F}T8#?!%fHTtkbQ^`1r`fvIB@gqPT}Q?mbk+i&@1?wGN2%#wYRkwGiU7-76AO$t3ID;`=T+KeK>b8zw{nd-ExV5~RuLJuQK'
        b'E_JyK?~!I#%(fc5p1|p1_r;Lnbi(#dkNrc^E{%;YS!3IPz)d?SdZya8q1usRwW7^(=SS6e8>-qLjukDxz!7nb_<g9ZAJ4f%{lxD<'
        b'{c_&p@alu|zjAc;Vo3Zk#M$x@;Ks^7dt88yY0hn<C|SLD>*}beCUTb`u;`}dRF6ZTzf_ghB*mk0*_fPhjVH-S&o9Fa(22;Tm!W=w'
        b'DY=0Q4dFmXDppd`Xv@Il!>4!NR`aOt{1WZgwt2xauZk~myL~;**|DncZt?5w{!clTv(1<=ztp7!{)fRKa7tEium>sy0;uqQb^RU)'
        b'R*75u?@jW0iiPD;f7yGe()J@BFCqDeY&=c1l3-Xt5*4Z0)60-Vm0QEY{}(2P2vmLhzoR^B)PCAZlTMew>fGbZ5*1&Iwf(ej_d|VX'
        b'%_||8B?MC_)I8b4F!NCcZtAfMNmb!@F!q^l-?j@yDm|gIbJ#WOq_#Uf$N(3kf=0LWYjQiI@V?&5{uFVvE$OlAm#3GI0gu@73K!f{'
        b'Ph`&RO<mRFrfP~i!fBGpuCa8;aLW=wxV5|xzJ`Z{=|<f#na0vXpAO1mhN|1&4}zygLX$@AEPexkx4wtTu4A>mj8=iDhW8as>!T&K'
        b'$Y`LRB};RNQll`af)vZ}>48$<w^-8u3vdvnW+Iqi%c@>TZp^)A8{+G7dbm`pV5jx^T-Ff@k@Gbd#HwObl-s2Y9F}Po_qbgOK+69S'
        b'e?h6D#~4w!+A=ek?8+tuebLe+)1>#ruhpmdQD?QhHSXG^R?QLM{kLz)G${Ze9O6#lSykp|TiSa!uTpG#WwBe!FX{_yEl4~g)xKJm'
        b'%mA6(${_6eO;YH0-$-)0a9N(#)yp)q0F(rA!MO=!sXH{o$ShxNiNsNFRHB&y@g&ConVTZ7<k}_MOITB*%a-4$s2Vd;HMB43m0`Xu'
        b'@IbivUDEOoiCHBzx}>YcTJw2<S-etmIX0Ld@}zH?#`=4VT7}QG7@9$Mfpb%}rcIywBF-^y5O@pgoiEtKy|yD*4}UdB#Mf`Di`nwc'
        b'@zSI$)!=2@cRg;c!6&_j^xX&j=k!g`D#NU=mQ`D~ZYPJgJ5OJ)ez8myqZ+<tC&g6_^)b>?gSfm3>*zL!b?<PW#NwD4MbVLJEd`v-'
        b'o8-5XJ4%hY642eYjPyuKBy_ty_nKdT2f)S)p@HpDgsNnEshBWrOAb7a9PByG4KFRF2-B^xEq^+0%oda;El<Bfic2}q4srQrd>-1B'
        b'0E#xMq0jVs_Fs1c6xZB}x@P*c?vFBC_i=iMU61P+;;WGO(PR5+RJQixcKtn7AF`XU_K+d?gq|%0X>MmV)<%VDDTUf*VMT4aos^Ep'
        b'?8>yw##kpSuxqG&GL2jE1$0lq-sU-8&7a}3>oeWCU#J?cV_9cF6{rypadycydZzVY8N{0^3H#88;8yMU7rVUI^D?5U>KHW|#5sLf'
        b'{%+@Sx8z#Q>|L24dmNc|1GNk9s4A``%O4<;rSacw-nFM*4|)ZcTvJg;ic^Ss{R5zb$F56uRKz~vbWhq{f^7@P{1?>LY6|t^zfVmI'
        b'NV|J-TRT~vz{OSUf;MpHO3F3dqwN*333k`-5tx=()Lv270lA{D9<`Iy&IMC@YjR=<!Xz1k7<yL_Sos%R&{v}{J$sv8M#tj?W&6u|'
        b'YZW^`MO#cQdv>Z|)30wjwf5@WqTW*}JD)u}jLQYRL+XAbiI<)Ln4}W2{49qhuEDh#1BJ9BR29eN+nx<_ODQRV?yuU|4S?uq0JXU`'
        b'rJGFNPd{?WB|TfKER{<Jqo3HeC>m%H9S^jKz9+5|0!_J-Ial%8C8$~SI;iZvE4HtCe*4>seSa&BAV;>TOO2%e23BQcyTVjIe)hJ4'
        b'jvcMv<8o0uKNxLPZgwbK!8&|BwsYI&sTv_4LH-XaYD)p>LhCj~se$re;vkIHSAez)q3N5qE9gAyHg(Qz4zSuc4cHU3snYAl974PV'
        b'#+<#!flEqR%{JNeEi;b0U16n3B=)si9Koj(e~a@|<o^YnrH;du^=m}n@T5t`*(xw^V&#>PowK(mCFQ>1dHjYC$@;JwsWXgl8VLSa'
        b'?lOn}cF3-tV!g4uwddC7;q2eKmuD?s?!HLUFAW#sE4P@jB+?f~B)%O!_-ceNR{DXQN<$EFwN_iE|69&yAg1Qxws*SeFxJ!KEOhY4'
        b'BKfe>-7E_ON$S+n8-zJvI&t-;UZ(MOGfatkwg|N8esvO+6FMWB+1*|6N{>AuwF%cB@ShC+2Y2UHtv5grZgmQsX~sihX+=a}luPdS'
        b'2?WeiBCb(4%J~E&@3edkP9g8~e8rz-LA-1|iH3V_8l!E`_arimZD-HTw0PT&p2P^1ZCj6+B5c3yNwmvoM^Z)@1QeHEMI*88nVv-7'
        b'xAEWEp6=Nf@lXGa(7qlL_dIyICql4cfXt8J?I(gc5TWbhBSL%D%DbCLs0zP^5tg1I1vk3^<p*CW%dv^6dO_OXb{i8?Rl;cYS3Mx9'
        b'-6WBgkV-Uab!`)PsCjLVk*9+Q&&Gn2UDBg+Kq?ZF1ddKX_*A?j4O|U+PcsIxkMtN_JB>>TBN=AP?WwXPdu$K)7?%nP(~L93=@!YO'
        b'_Z#y-9tHi;7RmC5@ABt@|Kyb43I50BMxCN+)$$n-80X;AYy=phyYj4tJg?m4-v<7`UH%G4ue-~i1b)l+ew`Aaui~L2-gyLW!OIgs'
        b'jgTfx$WfRk6iEv7-T5<umbRZv)x9u{j%%<0;R5wYHFkOrxWS=Mga3w7pG#nQ6C)TPU|0{oeR0+(kQ#{Saq;w`LOB{Dg8!_b2NL5Z'
        b'6=);1QLXvzIIgl72t2y!A_AX;)!!$WHEKF4RFw&BbC27lvO~9pB7%M(crMQJ+C;akiM0K#8!vOX7$$G5KPvNnc^ra1#-O<DoUb^%'
        b'H?8so`hf;%&UNhXkC8=zF3sPL<L<FgLFNkr-GyLT|Dg7NZi~Q@R52o3%W)_z_`V{&ELf&kM6}+QZWqtWEldT-))%a9J>hc+J$r+='
        b'bYa1kb0J*(h)a72m&+ksgrE|>cAQ=o1T4N5<b9m*oe9&N>atz$hJGM#9GRm;bN2G8rM#u>pYWxnbOfP)m+u=;CMe6gKTfzh)a+Zw'
        b'Z3nvfbAiErQ*j*k6roXcj?aZhK|ED_I`+7252gcIH`R}7%nrtxMbsE~MLO4u8`7L4WpyZhr@sbC>~!J27@`ga6m`2{*Hcw*z4*GV'
        b'j4wzyYt)w|ML~o1K`r6alFlK)5r?u?SlQV`TE@7LOmX<=nY7&c>K<n%(L}bzMEW9PoUZNFoeI_4gx7xjjKK1Uh!H?nMLi*t$QkGO'
        b'efI1#$ItgEF7>6*c?$~8kV}fzY<b-F?Cy`0UkY|<=E~y#n4BdaE~cT)mbD)UZ#yih_z9WPtUfTUqt<z9+!6MO%qb<BC}%dXdtA0D'
        b'jC)DWZ{Om1O}#bsnJyroL7NtMX5!qhj(gV~cb!(dT|&!k4&+A0bz1IrZQ$(_PzPwl_q!0i(*oOuF8=7}{%hT&Z84I<`^fPoD)4CB'
        b'b23^*i-y~pDBJJ4r-Zb3+3_Zc?HkOax+v1D>0+~wJDF76g3hF}4<8RYKpZ=Z2;FZcY6PK}g?x;JQ0+qR=6W@FRRaP$L@mIfsYzVQ'
        b'r0RY>0pl4v|2P8>Ny0k^206mA68FiC7Asvlg7ZCooTw2t=-X%8&US^Egy8q$dTvoq%9@0p$$M!L9hLI%o`Xu)>%EH?Z#}4)Ehtq{'
        b'CB-{dnM_<U^GnT~E_PO^9Ni6Su8dyRB(kws&nIQ74%q=2KmeVSsz^8J%_fFB7kRu}L@#d=+oBNPkyXl6#qqh~O{<b#*#v>}F()lt'
        b'WL&Jp^XSEC2Q?90tO!dehki0z0h)nz#G!OE!l0wFvPrtDpf=M}%{dBcGCvusTG1ZUpsas2+S-5{U7bag?jt^`YU!@9xK+z)<F@5|'
        b'%()pt(WeH!&?SjnOZO~ea{k8AB69?_@qP)9r}(ej=nKkxz6|)9VU`7j6*q}>mE0$5t5!Hv+m+jD!o8n$pAoEkQ|)08Ox&vSuQ;Gz'
        b'FTNsgHM@S5?iABxc@$99$B_N5nN0%QM_9wh$R@!7LHvHZj2JKJ7Bo@zC4{a=&h#r(jpLg4JK4W<r!l-p)CK?9)7?QLx6hzs0|9=4'
        b'A#q6I8+z@?k*#fu$aQ!v1rb*p*O(KM8>uHc*`98LHWk>`KuW8&g45kE#f$Pt0^ET-90)UC?>2&ZM1dG?hya)67dLP?GgsZVYf~4$'
        b'f!aWWIS7OSEx)!qq<7c|g;$N|&AU0>cifcBNUiT=-wc)6V1$3uS{Oh`o#_S^Rq=gMZbl4F&tiTE4VD9AY=i>b?4IuWt0a7bQG9Yc'
        b'Bf*%L_?VKrWAfY>;pnb<5ARQ)h~VZ(-2?ov@|$izIW*pc@cVryYr7jiM60O#dlZ6r>C*o<ytZ@?UX{Z41Hj?e-FGK&lw$njeEj2l'
        b'{QA3bbnrO-s(XJ-gMIh<?tQZP!Mh&ldjj`iK{a;UW8D?IB7Y!wDPU&FyAh)KqV7-~cqJ`Z!$9&x`Dmz}mv*v0`_DQh{|Bi9vw4a<'
        b'jKSZd^gy@jYUtjHAXHBhrn2)nL8vhjWRr&w4>s<<XbC;2@pVhW#JSXNZ)*1$8OTW8n;d_gz#pjxW&1lc37xFG8zd8IVoWN3yb1z>'
        b'Y|Jl^1!a(PztlFb^9<!EoVu$5;!>kJ+4!kik%-4EWLGvOgopShj@g;=PSxim@N*z;BK2Qg*qx0W`z<;=1zbbKa4buA)AB$*$Nr-W'
        b'R0^JXLC0XF-O#6k>YgQr*Y&7wdqNP$sejOXRBMS~F4SEvcI8a%lga#NN3dK=)I{pLd~r)T_5&V)rNMH)>Z0YAB^>*ge=GMNUEh}*'
        b'Q1Inm?)v{Lx9f*;?Lwj^%|4`TA}eaAJ0jz1U|fCCQ5#v=9C)4!>9jD0rMV{4ow!XSb)dto{mF=oP@NW}L5rX1+D|r-y0D3J2fMs)'
        b'cb$>Z3j>uLKbi&W)z)E7SlBgx(H&fjN$o^QB|EgVK0>bU=sj}e1~Q8nk&1ggKurYki}M6U0<T_^&_?`z%_8C@l8KCYj!H61whwH6'
        b'>b}ie`wL#{D0;CgF(yXU{v$lo(@7L(kmc_Yj4qWo>dzVl7u(ncPPZ0AU2j+|ljC^Z{hM9j1&3WLNbXOnnXWN+p~}QGkaivNms?A2'
        b'Zc_)Ya}8ORm+u8Frg#o1evr7iaF%Kgl^DBx`#hRVie6O;@awu@Y;2eZ&Kx<BxHRhKQnEaQp!aR7`v{BQ-Gw*WqN}ot=Xc)rh8Zg`'
        b'Bc6m~U+4lqLRry`OQGA>t8U4*Kc%XdVX`tF{`z1F_GeQ`p9=n$M#e}shGV)Xx`rd*17VDAq00GngRt=p&k&5Ds<ko$wAhU>15X!<'
        b'*s`UoTLP+vJ*Z)*WD=+}F4ss2_0e9tZebG%Z3Di067V)f#Qm3D!RxKuS`h>K_tTvC0*B#i_&UjRzT@y-D*L^ri#JQPVwFUI7@6+I'
        b'9O@JOEru3!<-EfgNTTYCDSYrB8#)c@@;O=lM^1GKAE8v)`J!{N2z1Oxhu9HBD64B19=T}{f~WBf-DlXUnxrl#4+=Dz$QXy9+DSD;'
        b'R#)ut=~62jeMN-lujB0k+}Nv24N9q+$mF4lS_QOx=B3WcY<B_?Z2bmpw?y|IH-%TjJm^2*xeL{XEO2>B@3nk1es}1Ks-^#)E^oc+'
        b'3!+J=+j8&lCJ1X-e^;DaEBSA@1K@JGsKC4b26q6Nm!&-CdFB-%^NPDT0-M-!Zd~K<1iq1QfING&^M`ub4t0*atgLgu!~y7nhZ=dV'
        b'w)jD$b%xkzUN^bFG9cu5Zt+kcXx;;00h062MH#`K>-6LKkPw|cr+GSG?zHQIQ~a7pyDPb(R%vr$QPmFX_hlgs13g?RpAZXzEULzE'
        b'w3JK*W#Q@OU*2216z`I2U5jf&#j#}h5<=Ce#QwIFC|*eVm;R7pg{m<!#P-1^lwik(UahO69>LCHnnSQ}bWU}PC}g*WPSx{-fg)51'
        b'(CabE5X_477ylRi|D#Q&64Jp|@pO#e9X{18x?|(zg&a|nC4aUxi7q`gPRDJ2tIV}|Yt=^fKxcVB(2w2UshT~SxB#zWX6ri3@p{C>'
        b'9cyn^DihZ-iJS0J14Q=a&Kxn3Sh*aeM=Y7sHx(w}<wX@@56zD57dt^JqNB3Yk7sbu>F5;S;=?LB{Wo|=c_-drg{~Jm#iQKzti)Wh'
        b'{0JXq?<{W$j`uZDj);m{kv)M-ubJ-f4c~@tkTRfF`_!I>;J%a4Flt&lnRDldJl*6O;Z#1VfeLuIAI9K@h`>HdRY#fjP^t5eu_c|M'
        b'fj0sbkvEZunTtBV*Aq!pDBc(kstO^Mg$d?hm7T%y86f9HsJ3#M%&{h6&>GXggl6}$P8c@CH$(ShWRR^|GUsQ+@+w-6*JPv~!=uPE'
        b'j<I<mEZii8<NpC3jhh|ct6ha;@eDcYF%NZu&rcIZk}_t3+VyPJ3*HAh&j@H4gqJ8GiRwZ`gY8KHcxjPCS<!;)!-+alY=G4BR1eFc'
        b'h=5)KqPI@=Z`!bDFV?c)Vux9arZO>6LawvUDAILS7Q4kz`+2w{?}w=8bw%p`Evg`{6PylF%?x`{ghN+&zr85RK^lu@SnV@lR^cp)'
        b'wA!F2MnF;{DOhchVy&ik-mPQmN%ay+Bkx?w@Y?&lkZ#!05z@&@d9<M;i502}0(@@20=t`73T|EHIF3aJJHQQdKnzb5g4?tII=Ib#'
        b'wYY;b^8my|+$w)NN3j3s5I2VOOJ6(tua5uH=>s*_u|1p}-xJJ?(}%M0|3!8FQwJ*Uf9l{>d90kZEQ<ZOBT+w%{ix$+hLpX~kr+d='
        b'rI?_>4)HEecA#?-lRJ3;XFK-l33gM*f6oaVJm~cuQ))OuKFLGw=OOp<kbl8LE)7D~wN8Gow0Cseg6u0g{%cCHwF3r%yXO>vr?F=2'
        b'nvVa}gKdTFyBj;~`sG$DH5{|Mp@VJesFm%m?*LDI2iw@;+(hhtv%{n(c6&N(4IQ=8pxrj}(ROzN>Sl*x(L(9&K*O^3{+shuiILhg'
        b'UYCNt@?b}>)8G-Md79#^0BVu1cA$=euDu-)=fBRO`{fRhG3eOS;SZhj16^-?>?K*ZlwH<QrH7e*jO8{reBQRY-L9XnDuf9^$M^RD'
        b'`dnCF%T2C2STCQ8ME|!x`1$w;DZA_bsxezmd%Mh0ct&`{hwC`BbgndH*8%-=w!m^-_=wEtBFs^gAwj%umDO|~r~5|e+N9>~1GUF^'
        b'&C;|fj3x~#D%VH)=MyExrkj&uH9?HpmFnOmKT)XuVUn-0I42#NPdaJ@!;d#O+^5HH&QV~n?qdjs$-N{ld)c-)#;&3&(mM5m{fxf2'
        b'>XOrCrNwA|n15f;{BZqPH$^W89Bv>EBiYKLB^`4`YqOJH&V@kLu^>I3lg*|0o1sU`mFuPq4(md=xMO1WRYqaawMxsoP<V~<`{Ikm'
        b'U!ZLP1oFC8wM9cMWBj=EHEK|*v#n4Xe4$q0@ZQsLM!2+5_hTxK2|gtNwDZpH01;?;TdH}#jZNwZPW^4M=&++TQP6~^iXm+G8|^Tq'
        b'!k2DlQfzET^p_+%6PuFt9t+N|f^Di9Xk%4VV5A*vREI+fP}2B08M4>=$3l_S?ci`r^DVjK82;K1V0bv*HdZ_Z=jJi?$HxF2@CHvg'
        b'V}?C<m1`qXJ#FlrV<0QkYMebb@e{aA6yV(gG)@kO!N}1iW8KI2-L@#ogqf7CUM3V!-DpkKWsL_4P<KHgxAWNd9ge+%Ie7Nw%XzVl'
        b'{p=XP!s(MXq$LIo6CSlJSjMh@D<k0gzKp=4anG`;GS=T!#$WC#gC#Vtv@>MB%1&xFx3NPZdchZ0_$RN^c%hQ#l}V(5F+_uco@2BS'
        b'us{|21EJ{}q4{kay+hB0=t*cEYikl27!;_9duGx{b0f3qz2Ikk$2LYzZxVX0Uyo}9B?5yEAHz}g*T;g%i}s<zoQSM|k5Y&UjJ+=u'
        b'8#k}`^$NfY$tom@s*bTc+w;T_K*vEWVmKSor=!4GU~0>-<jy1g4-={SHbdk&$p$j;38(vv^L)T%((Oj-dDZ*V^4G1)FIKF(xp>{W'
        b'bw>Y>O9A#Dj+y-r;XNc0V$+6(#3L3ZAv?WkeY+p`sIF<lJBgk=1_>SFC(($2;|`5}bXY@<QWvo~SDia!an&}oX$p^_uA9i%et8UF'
        b'eJJf`QridO_5r|J_SEi=Y_==}`=M=Qn{vmNgSjK&#L(^$ny6u)3xhsaoHn2?zR$~3)Dt(Jsy=o`)-9yxSPo1=tv~a$;{{IiOJ^`X'
        b'P$RX>9Cw{Y!=Kwl>R!bp>=*69c1u;ZG1_>QGk|BJUgip>wKY*0F95N&$37@iZIs)-ZmU^slpdk;Dqg_LTXue1y(%UDS0YtQm=UUx'
        b'a|{QW)!@`c@@m7|?LiZ6&~!T_rsJGNGBnvD?!iD%55fpmeGHuKvWDDR7N$FV92#`zAs;pf!HIhE#dc)!J=ES3wD$4~ckVruG02EC'
        b'KkPytZ#y_LgjHo3-=L*h1lY%A`^&iMU!_*B>gD$U;W@>7k=+AtN-|$>_a+~EOx8r%_8^hj$u`&h?v#0%BW22k8T=iXy(z1DT^>BP'
        b'?h%c5W6DZQx&L+VkB@<;96e3KfN<Q^p@vc4X2$>={$b`5jm4y%Y;y~vEdJ|QWa%X6>udyu7gV;IMKQ&R)67B{d#Bx$NU&q=xOI>|'
        b'#+w7&TA};2(lUwna@&Pc_C`C5q3rc`-V9Jsm4|$TF=6c2?ZYwf0Uw{y5&7s?qFzGBx*RF)p~rM%2!Su^$FwZ)_v<BV%_?zHaRe>X'
        b'fhU%|)UJZEKg0Y%C?#3!SM93#0`{Nib7UpP$btNcdJ-D}Kxre{kJ=MeB>N%n73Q;n_Wfe^bM#rduOpFkKbma9OEVp>@2@G&AjR24'
        b'YaVX3D~=(>Sp@q@d$Ar36u7zi(sh{bv;KC;1|@nw<Gm-^qrV{80fcA}UQw+i*z-Ymvg(WQ=nW$FosgIP3uGk4^N7qJx0$1+R}_ob'
        b'VIC{$M^!oOY2Fz%eIEo5q1*UAzWJ17ksG3>*8`XnJQ!_$!^*&wJKnzbGctOP=kZAh%zUohtxd_Jpoe(7_;6hbhU0F+53XmdO^XyK'
        b't&atQUbya_LxFaH0GfjUESQj;)*h62@n7V|XcnDd+4kHR5~f#Z7U%;Vv$nk)*L2vL_VTgNKfhqk)?r5R+o84Uh*q_0t1%(f^XZ*)'
        b's&?<ISj0lhuXyz^AvJj06Z>tOAt5!musc6fkSb~gAfYKqEjj`p-9h)vP#}Ey`6C->3+Z#Rz$ME2$Mz>>O#<85Rsi`6jp_nn07ls$'
        b'dDM*8x%P>de_?!=G#ChjC^mWnS^jfDoI&$pi}Sp|9=2FgB7Rg-nhm|JG~!(PM)9MKZuCTNl(=1aywe%BF#U1yqf4B;C!#L*aq;q*'
        b'yr-%a7&7{@czKQ)y=L;1q*!WprGU?HLSWX~CB@=L=ksw%B@kf@MkHO4m|e?*S!PJni^a*UK~Kcqip!8}^;CX+)iY*STF{s5hksgZ'
        b'&K4jI1VLH^{x}{OL;_{H+NLG~4X=aC;=cpVsUY~*iKM!dcZb<dw1BgrBrt%X>~72t4$J-5pOm?^KLh>N`#}41NY&rA@^?bU2MDRI'
        b'?~Yv)5B)@Hdj>-nHP|!7bl7ig_M&)a(X7Cv#HpDDDe8}r<+ll^i*V)<-W_ddnHE42+vBbLg^=;M%9hX$us84l%yRFH_KjCbZxn{D'
        b'<HI7(NlIkicno-y576d%XSS<qD7$t^SA#bOBUS|??ACgbb+2foRyo?JtZr0WUl3Uv)t1&fAlYzcx*U^rQ;=Z^pJ9e{8-SJ~goi`r'
        b'S8SJgMHrBY0md29)fTyzY{%S-FeKL^^KxwvzW{w3!8eY+`}x#b`xOZI4g*qocw|hmUgo`t0dq0n7DQi1-|Qg5zpJY8j-p?Oe$%aF'
        b'eQ6>dMO)x~zs=-M-Uek~Ys0c<VZ8S$CXGdB#nUox0DaNu(|NwBs`Fk#e<b?h-_^ojCgNhPX)+?YKWUE$@5f(CZ23t`lYmJ|-PwYI'
        b'{oximmeIzci7B!zEh#i*IfqVkoDDhBJ|KOO(k6lBoe4}Nz@Sj#3~{=s6g;fI4R2%@re#9ZZ;G>I-hM>qYeXYM?0usxah?>vTGIPE'
        b'Mtq48X-S(8WqE&x{s8(@8Z#}g-swhO`wabFA4dH(nDpPvO-l+_%_FhkMl9H!6ppCM2p53ZcL$O8gpkjO?%IRt+?cK*Iuy81H6Xyy'
        b'Kk=daz!})XXM1(3&Qldk+W!<L+{-6S`j5zTRT&TFk9=(Uf5fg1X5Ga{uKxGPv?RIeT|TcpSOGb>JumV&{62&OEvI93mt}Mu2sODU'
        b'Afx3l(93lJ*@H4XregU*mS3*6mZ`0kYW`J8l~im8fScQ(3nG6(QDW$Ay7D{0u4YaOcKId|xB|~(e>WxtC(TVlaCyq^fHRE`5)#mZ'
        b'(HUm3-?<BKTl-O3#^~etkzx4<_ZUhI0`Z?Gy}xN4IjHPtY>>s(x@CkL_o9f$C%p-6iAkhai|zOXwqwrHsXZag>%UKm)Y9@Mp>8G2'
        b'H5VE8FSHz)cv3cedWh<#dIx%&M4oMvbH%ep7azq-$2<{}t~u)RJE8MEsGH{tpOmTAiUWrxOk*NYyYq#vwd%}gj+*)fr7(^DNgJrD'
        b'O+s+$p1FhS>(18TTs)26CuPzR?9;92RmDiwN8!Z#*;dsHgi%DOAZi;%4VU5q4#<tExdq;Ju>B}Zk=;55*=?b^%AL9PC_5uGe9@FW'
        b'lE~0jW}8-U!6XmLaH9t3Rl_a(oLSW<az?^@dtb)A8Cnokb&aNXC(nu7g0otfSlWJyefU9`(x$)sW0=wwVLmK<C~~A-dG<qPN5{qC'
        b'Q}Q?m9`12#@uEb_vdOdo3eT0(lrfT6eV;T#YtnLf$&FhpIJ;7b_qH`!19_8i+2UJM?=|HF>!JO=9{Qtfp!I*NhxYDz)ct?e<3j5X'
        b'^`QT~9zXd%)FbErR*$T^>j9PUTqO-I!YC8C=ZM#4o0f8(E97IilYz4RPfKtoL#4P|M$7CXLB+y*3oRxcckWQ@a0GmKe8q_G2qv8?'
        b'-jtp6@;yyrn{W!>ni;*7%F10I#vBk2g$+NtOTMgAtRRNs2WKr<RtuUBnhToMp883qpUN2p+)0B-keepui}7RSbb?-k64ESgwCX&Q'
        b'aSY%t&yH&>{}|Um(@5gb`j^P~x<~J%!5~mZd0%X8A}t+ZFlQN~G@mpx%&bE`JTn&tQ_r4e*4q00nk@S}q%r$kYiOg$J*}Y0f5nB2'
        b'Th4*ks;jr|TSy+6r%2;_<Q2}lwG}7VN5fQ&1kAExb)Qb)Sv<>oB=CR_DJVEY2ELv!)!oThU)9_YsoKPyA$>xDc#PA$*31@%ipsf+'
        b'xTlu2c+F6zZR=4y-1wWL?7CK8M1J6jiR2;sQo`<XS2Df`f{75gPs0pedBmsIZJW@%)Z8Qt)`5MxCA6L#vd0w>slRFQ{=60Xx9wLv'
        b'P<wOm@-f`zw6s<C)CA-VDUFtY%Z%?vY-<j_BAEJEi`UTVE+7!jBM8SQAlRR_de%+YUCBOyz>b?81HYQEpC|3o81Mb9FgNku*J{f;'
        b'diQGgBX<`7@OO>{wAb}(ACxhSQe~9Vb0AK?LMRi0pO)bfco<4e&5y}&>Yvbx7FP>6b@%eR*@6}`6VlC|2A3z9*TX_VZk-gImV0=q'
        b'%!KT(Lf(i#KY$h$9tJx*gb||^r9qiw(jEam?*O>b!=S^XvQW^BWV^4~&OEDXr@X>eMW32KfZ3ot(x|k}Y39{95~DX!-tm?*0z8u`'
        b'CC=Sx!T0i#X_~anLgt?>a0v7ef*U*+9}V?}BMzk%y5Rd0b`5Sn+$G=_0=)lhIfF&ugP4E|d#!~Qb_*5=bO%KZg7nyovrsVI%<oZ3'
        b'kIm_prEMbEOD&dq(YeoB+68n~6KNx`$OWW>tP$+XkVAlWs>ri=U7Xde7eE&ZY@c+HagJT2_*<@9#=hI4dtDUVOF)z7&bIuMJVSPq'
        b'bgZQbhRAbgz_0FC!{B*HcJA#^WE1ImOLp!Q@1x_I$Ur0Rtz(JQt3Eo-u3f3B5%E?!RjddNOFgJ5ISSnMPgFL7-=f6HXnUrn^=Mot'
        b'WL`PZj%F(h{A<|eqk$C@n$e@}O6b5VCfd<f7BEh*ok#CBItOJI+t`9v3u-A-gg~dJOdW(~$j82U7sDYx5BSoUWYr2O|47e4fy;HH'
        b'Yav>Q4z%FjgV&D&S2qbQ^Cp0!Rj(3!r;BT}q)mL!!3U0p3|>lsYK0K9{*ll63S=d55d8_{6;{2<XN6Acx%Y>>f0)Y4B!l)C;<TX6'
        b'yv-NC)S>_0_H1kRd3Ut%7iGlQY(BjBXl&|<8a{q&3tR1D-s02_g>z1pW<zsz9mOz_>uPZaB0cjmDWJnN-sb9RD!*0<iI_RKd!CNP'
        b'!<c(UW(#(I+#I|r2g}n43ZC=Plv|f;C{h>-^tpAUcs79|VjbnOQLaBlxeN5>BBi}3(peP27GVq8q{w{*&gMsCX3-UTMt*V1x^-I%'
        b'*7!`VMCs|<c9&pt$sSelwBn;Utv9<AxvivMPZTGRIgb!G?_160x2WEe7DtidhX`|@+Pk{BNgQ}W;?ym32)CG8st-_S4+?^t-ggO2'
        b'vz1#6K6{_KG<xsm&6FxVhP}T<TnzH<l14#CT`Gz&6h&StQs#Wf6=x&v#m_gg3lPmMKWZ+@Xu%V=Ns8i_b<P=k+a6zQ&%tAhrO_1o'
        b'$D^ySNX;-!OKDL(a|^}rCmd1y1-|}cc3E@h$0eS~PkfK`U*L-5%?*1!m&eY?yvZ#&G#)=nykRiAiH%T&cQ}wE<+v%uE+$klV|I;F'
        b'e3>iad<}2P8!exYd1top_5#ZU?rmkGTgveQ9ahy+eu*m)?llqS8GGxCRYl+U+~OM5MM5`%<xFqM;ot9Jr?r&hU6yQk3m#wN|KEdu'
        b'Pum^43oW0n_A*zUx<PohQ?Pl5;>b4jv%-p6vfRf#C+!yJh>4L3rIoc>Pg$)mT7|SUQcA>a!@C=n63(JHUr}rz2Bw#BK22<W`nzHe'
        b'*Ce6i>=1hB8@nbJuLO`1Bm0z)!QH2*tBYJh2x08ow#)%(EHfl_%=Y${kG<@<qtHB(jik5+EgD-=jsj{93Frb+6ys3E=wdDV*-?D9'
        b'Tsj^&H-;vWp=S7g_Nmu>Zwm06=j>Q8Wm56Xz`;AJg+FcBQFTrC&Y1VTqdWl%CU|obk^YR5J&TY^09TMMVuCkWcs>x8&XKz|;ljFc'
        b'#@^>->6XU|rXRJd#D$`ytEBh}5h%u2=e+$vaLXt7Z1t-p#zaBGjKDd)WoWG6_2x6OZV^N;#b|q?a{qQZ7R9|R@Q&W%9}C7>@-VjG'
        b'fENnN4Upok#O_00_v~mODW1yev;Dl8e*!YjmA}=Uxxqa<&R7%!F_$z-Z;5ZjN~wpGMy38pqoTJ_z4ITvC-EeTT@!gp6EWJZ-1(t('
        b'SaGCFedNe{>OUy0FRJYYdOFT(%RIs#7W5tdJ!Gr~IbI3vZuL>FKZ{(Qkeb@r#TNO_RUIAaRQ5U)M;z+&vyj<+vD9NyK&CBxh4UlQ'
        b'Ia9j&%P0u$kEPs)|JLiLjtt{*{N6%!?w8TF0-yWv*Vt!bDA!4a^?9ln3VKxC22o3WyI=JMqpBgQg39Nk?3$ST>Knr`s)Mu_l$L^K'
        b'pn@$6<<=!ljBWW*C|Na4Q2*t0pI}3i)bi;#(xp;ebr3{cev3Nr*KzO}wZz^Rh{30SYZQvpEl(p0uDRpW5<oy;vI~FzQT__bRlQa9'
        b'w8-dMBKcA=_}hrWNY@c6KVP&uPGWRD&hOY??uq^~3P24$9ck1GTwW@_AQ-(V7~PWeWkjKH@M+BJr1FiT)iWXT*L<WqOKfxzEYl1='
        b'Y+M~S?#2M=-$*!x)N*N|&~z%=`T|HKqibjWN=5tvx+Z@Y9*=hj_m)ufjNGea{%S?<3(7*_6W>*@Qdn21lcj5f`3?m=<CBctT40bL'
        b'LA`(tphhm&R##!!kr$MJEnWu4CpWGq>_UourJ{uzjxuIZ1r*}28W?OjVHAoS!m6itM<3niAjLUE2#JeyZGPRJf{3HeEKz=;!g;cn'
        b'meMn-3(KsChx^Z*i-){MXxAu=EK&VJnY~D17mB_wM3g5qQPVPi>@!eTOj~E{j`A92>r~GZK>Of|Z=SH=+anh?EM%qF=Q2-u4V1|A'
        b'MFvf=;TT}nr6sAz@;Cu4v;EV{bG^dN67^vs+n4B7Z51#&g;(HZPk7NxGJb^7MyePhwEj~h@VOJ`i$$DnE_P0kd>=Q9lQ<x`n2xVr'
        b')k}xv@846Mzg27n)&Fo05Ob<Rrjjf2T4xpoqOMSAKip$orC1{bk9-wWs@%`z35|c|^0O67gy116HZYmqBZjEGk_}|}5rQ2=*^?=5'
        b'rsE6=1iqL~Ax3$^eH)Z)A0Kzo>!zXt%f8`*H*R<^v(np;Z7Cn~b~N+yLy97xVWsYcvCO?b5DOGNCm_bKLX}%5^pv5fpxiFfBjN*v'
        b'X4jF-lit<kA|rK0C6exb?a1cMTY)8lGQ;+~&+BP^QU-m(w$;l&FH`WlX6PxBjng+5P|F{9bYcEmdkVHUyYqyrH`1lE?b|krm#;2;'
        b'n21{iW3QxGynG|?i7u8bzhHitFrE~csVh~jCBki&C6DHWLR<tmpbRvAYl&z}v@YwL0*kL()+7qNKF+>?HE+V}8A^l&WzDO_sRbL3'
        b'm}kfil@~4ZvcG7?kyAzOyF#*SnuGUdo55Qwch8XFcBrjmd`%@5MZrT}5ClfipN40!`OSQ2lEt`Xf!CIQ#3-RnEreNLQt$+n@SxE('
        b'-7LxP%WGa|QLI*xeT#hFjm<ze6aoLj6-nqV#+Y-_mPofG-}0L=??NB$uO)S(<2>ASi>hGZ5u+%kSQl=jWbFKAD06;uu!h?#GYkp&'
        b'?gWu%)0o%DH=O4m!F-uNZ_X7x;?_jy9v|~Q!bb(Jjq|OYyY>D{O1)8|G;1PvezEvxiu`Q#s7bl=!n$mQT@wMm#f#rl7b?M#`~t98'
        b'@d**T(Z{bH5Vtn`IFs-iT>>}tJWaVC-qS<{%wyj9!2-Sr7SQ$u=}+J?Zys?cL|&GWehrr>yWg{J%sZD)X1RpPa^krrQ8%T#@0*bq'
        b'l+Hdy<*tL$xK)7z;`;k9i+|4HVFdpjj@2}aZ*VBLaG`D{mwD?jaQQwcK!uk<Jo3#WGTnC~Tax!&Y;&YEMHo(aXEqapd-`IUg%q_r'
        b'ruiA-Uag$q-zn7@^!X)p-pbs)ad~0&FRM!R1vEvg{z+}Vyyv-TpG|ANG>zEyqjX4R))(Zhq$Mv&me5<I&2-ed=l4WDLI{@;2gB^S'
        b'z&!Pr$(&o0X6X2dUe<pE#_00vlh~pI<GUw((4wVb#J1RJn;TQsZA@`3-fCWg7m07V<?ELAyJ|Mqt0ApT=;aODv8sz>5ZEnklGwTr'
        b'<E~G!|1t;4-<LxFmC2ypBDpXn<-Q6hnUhQ;W!zhAAjKNurZFs$DNaoLAJqTj^%W7ni{B1O%GE@%@$Z^HA7;)A(hLvyZ*g|_WeiV%'
        b'tTD+$6={E26qD5cwB7w$g>yjj#^E%>(eke#(N%=6Au7_IvAe&la5iWT1VJ3eJ6JSzK~IeTb564_=$`2x;WRG?-Esa;InC~%dy)Sl'
        b'r};zB{f7SoPV-{W9q)gSvpEjW(c9S_l}ws}@So*0&j;fU`Ok2g|Hs$2fHiexjh<HyAsjUijJ#}fP6!0lP7<_4YiCHnfYi<aYDA~~'
        b'e~5x$ZGUU6+LpPK99sw$ZzZ%95bz`z31AecwQ8k<*i!1y8MW=Sb=s-b(pp<v$7y}w<J`4Rz|Ot@z4!ZC+}V${*WP>Wwbxo_@3lOU'
        b'ba?25$o`K=df(8ylJB~@{XA!!U!=8;>z|&D`-Kc8{|Ro%OOW&*&>NoIZ!-O4DONbM@%m*wmN4>l&&Q*njwrF5ny9xrQtuzA-oriS'
        b'`91%SdXMgB2uty+cjIy{hu=(`iQi(0eot}`>(0<w7QQ!8erjG1Bj+DJ?D^e(-zWIF=m(GfPbP-R@7bxl0%Gh5-Nw4)n68fhNMeij'
        b'lk(JYw@%n3EFlZ~lfS1)w|)DD{we(M*}6pE!-pqyq51pk+AVRXI6)D$QfU#UNF#obA<#py>k+?9>;jl7f>+Du7p<;HtpC+GmJLd)'
        b'%3rphPg?}SkIAd!D;Gudulm%9aST{-e`(MEQ6tjtJ^P`jKKZ<!?UXhR^9fV@M2|23Q0`-s`sCBAu7jk8-Vo;>nz%Ef-d}YQ7K|t6'
        b'nYL3A=SN2?P4!gOnadN-kW3cJ2clO7dYFuQv(GELA)2-O1H?Rwe%up2DJipSKY+EkYqRs*+*kLMFER&}u-Htz$+rctJ3Ck9lh3O<'
        b'A~Y#Yb9I)yc@w^df7~}dKEbMj!NIZm-^N$}^+cWRFbA=H|F<~+{i9|vVR9$e|9zkDQ=DIzH4P;4Y*cAs);NvSe>ef>veZ}AnSTQV'
        b'<-H^OKwgPAHEwZt;>T|G`erN|h=dV&Y*CGdFnK7*F@L;oofkJnJj_0}h#B{>RNp@V`(y<6v;RA6|LglqZVGv&N?)}0X5;}n$j&h7'
        b'+ndH+_||{X3$tF5fsar5nne?M@7Y&%JrIA&<TXJP5W4S5+@KyUKLvQf3SSQ4$D$B<FvNhQtRCy$X9_@7Q%@Hj$uVV6{&#zOGE71S'
        b'{=ZEi>SNmk{_7&^5ElRYIy^s7r)PYvzWDETo|DEIQt|Q4(m0{tzI~#}Pr18Pk)QnXX8#tL>CBar`_lPM&&dbV7lMK|@M6QdL#Wvx'
        b'@B&F;fQpPfcjY9gwfeazsKq2grGi7MW3Bt4o@ovhsfYX^XCUAvsf{Jw!Ni1P#>o@Wd&NGU<JtZDbs+s(MvB>@eRKOHzn4%}x-S4_'
        b'q5ZlpD7$r}>UwYfK9i){=o(e5Za+U`5j10a_oGcwPeJ-@6V4X&M)nB&Jeh%`eji&Dd8CK-z`T7YQGn*z(*B=**EZyt{qOnr+|B0)'
        b'cRuoI&0!_K_lvE3&0#seKhw>-Yvw9Fp8akvpwrvV@~U*>Wll977udhGfE=q)KagsT=KV`*)F}uQA4sfGKgb9CHNGEN%l=4ELw4Fe'
        b'%zcqBdIXv8FgA9d#WmOBGSmMO+4PAjlOt71hAxS0@<e8IB(t>o!ub342YT!0_HxBk+VZBj@wsC(EmtD34z}%!ys$*iX*Z*E7nj8i'
        b'#Be&(2K4L{*}HxYTZp)F%@oj$-zSntQ<u`2js@&-7Iloh{e<QCIbidd2V@pOZz+l?ycwQJt~c<eOy!8iQuLpsEJ{P<MPf6N_B{J('
        b'-1@qUnm!k=R5|t073&W=3CCQF=N@)HMgb>Sy-6N0EVKY4-_lUxRhm`%UFv4g4^8DtceRc$YDP6HDMr3&Q`CCHLT2i^7aDx(W~f>e'
        b'77Ln`>tJ)$qIyNtJr$~g`<0fQdo09z_WfUEWhgE7_snBGc6D))2CMp4)&iZqsMxMvUXWozg+<Gyo$w&RIJ~Nu^3|U>G-R@#G<b0x'
        b'n~urP^j_>CZDdwpOk*QFKZT_WaHJFv^C1mRY{aH{&h=#Vjzu0Cql;VLp*n$;2FvlY&Vyr)w?*du%Jt^k`&`^2Q@PINT2y^Zl>8WM'
        b'NQu+8Y-TLw#wqLvJxm;L$JoX&2mui~V^8ek?TYH_B6@K8I>8C5+%;dbZ|{TYqQ~!~nuHCbPf+vib<LjIFhfXGdU)La&Ve@iRu5N*'
        b'?(kV`c-cn)VRl_J`^PYkW4yh8!j8@m{sX95KMu7<PZRU)+Ie^Y$JwV*MXXED+m9OlO#HGZJYn{|eRd<S%TaOy>D-O;#<`q;yOX!*'
        b'+#BjXxw<%pEf3FKU-l(Ei<*9!vCwxUJM>)Ka8>3h3HJpsIBiHA>uFNX|NY3}q!-^%Gf6w&Q0w~yObQ?&2tW07skS!rC(gQGuqApo'
        b'dS&E7h3~zyLs!NBYgsfZyZfFjHw=VXlw85Odn`*%nMx>~L0PzDpZ0GwpIqVEf6e{847uHt%`1s`!dNh`X#bA|KnY7u6>jLU#GYEg'
        b'wG>6I)a*E~>`PV$ggC=bVqdZ<sW}LH&>m){TDW+IFcociPzJs5v8M`(WzZa{i(ZgfR3@tqK*7l4kN~sflxx9*h7F=cHqW)>RMo)}'
        b'=xD(_<OLh%1o?sZN*4S|Rwn)Di3`KLFa(*G7vURL^~^wOgMv*Ca~!X`5BXC%{-IBh!*tiojWK*F3!IqQk%3;P>2wr&tO9M0#fQU$'
        b'Z>ED2<{X_{PlbWGUzWJ^>HW7)PH^eInZU+XCNr`IZT~k;99$ngaXxxx^#G&r#bNw@al6-4PllnJhye&4cUGn6(q2pP^5B0(kKe(*'
        b'xfl70aDWt9EbIMxZ`C<pVl#BEiyXYaZ|0KuP3u*_kq1FyXhJ3?H2c4AUcEk+hng0O>lRBgki{9z;P0D9E2DuTxMW99w-ogWc}hm-'
        b')nE5Qk{56!DZ;TmAt_ca8cn=C8ck1}YukWiQyYoudoi!v=YJH1VgEJe^Z$N_m8cG5GZ)s(t(>XJv=WX+to#t+Xuy)lnv8knUV?re'
        b'WB3|NOnC*0QOFSV6bxg0016eHOKtp~9oTDz6*)}=)bgq;Ce9>q%IY{Q$&wnktj0nmsp+dCKYWfMt{RD<Es~wWCv@#-B!+6Rnz;|n'
        b'KaF5DfF_VI(*;R~ADek4wec0h+cHLdHDB*AAq(;R^Ncz(Zg7!0HIAVFA+qgzIWCvcFbZ9J!z=~zB={}zLFQkA#<&fu=_Ba1Fh>Vc'
        b'<A6Hef<}_`zc=Et#PJX0Unr2UBd!U}!wi^*F9DzGt$@!XoWB;q*aQg8;QX6W`ZJO9dl8I3iH4UDd8Ia^2txq@A6-ibda8Oc3NP>9'
        b'it0WMi5F4b17cYn!Ke?W6V)G!42r9PzIz6uP)8e~qv;m^xl9=DlhEKRXiyyz*(U(O=XEI*eNf~AaR6@UDU1umqcQtMwj4^=46T#E'
        b'{Aou7$GH#q0=rOpEu?i^AQ9oP1R8BcI5ddt^1UD)aP7zm;!qCc`_U9<LE<Q|4@=;inv4WX;A>d;>JrQnIGG8pUKQCz&=p_pf}C$_'
        b'ULzbn(UZHE|Ag?#rw`dtD5#vhyxyoao|j$&3Bm?OBj_8dy(0VIUPb{;GuO)uzbAy<)GP(P1r0n*7*-HM8dd#A$#vIk1Yf6@4Lt{H'
        b'b+DKaIEsD-^uGI~e4UI*5I9ry2GNtYmp2-<jh_Xi>)_B6MrH}RdK5VDaS`)yQgP^vWK~9Z#0kcR>T;1y+#AtSfNClThf8E-kbwt?'
        b'tg0&j8NGUCHK+<lBrtJ6MWKdjfX5_^{tnhGa}80wRAdzrG6t%;2;p4zUm!X%1cJX(aw|pd^%<XI;<g(b(A5#lBX;|YOX-`U=N2S*'
        b'9j{wf8Dm&Wz}CE)PQXt$;G6~h{@l%Rt8^?iG+*>wfvWM^&c8@=8#nZw=(*G_r4yyQ{ho_Z{+zaRgfk+3=P*UiIg4P(^bxcfOU-x?'
        b'wDTbYXy;Q?xM#{O#L&GMLzdOcOzBE#=O^hiB_%!SDfBN3%K8`VU^h~Bi3c1%i)iV6C>Bj>M#9WthODs+&ex>Aw#gFMmFat(J=AR>'
        b'4pe^!)h?jsdMp$6)xC%+GJQMPo(P=%4p7p=k#w8`l=QAhI^F?FdPgLk=l~^scO*UE0ZO_*lHTq3P-NR8=_JP~(Y&)eU2pL}JCCyv'
        b'*y!^zU}i&qhB<pRQe|)Tu*fz<(&6fNM0R^5y{~!@`COkrTm#c`9!ot$RL{YZtnh2-O)S;AxEzq*3rtdxYMoZj6V-b#=Ec-E2}cc9'
        b'?jq<{B{`cx7Kx!CR97;e)cC$*pMiB+1cc_eE|&KZjt(p-uEzHv`&2ilUheppSUyNNUI3W7RO_#JVJfnD?34IT2r{(@k%JgAkp$Rs'
        b'gd|7o9^E9<r7O_~tC`4jGW0t16+5%IMorLPi0q@0T1midu$f-ez8#y{2!+U|;fxe!IX)73|Cgw*H_<3*3&_$-5v)Fd^~n6|sM#J!'
        b'PMv=NS~}hn*<5K9dTI#y!!AEfID*)sI8-($vRU0ojx<v4PU>Wr3dD1P)46w3=x;YQ(4}&}fYLo))le}89Z5*<0_Zb&{|W$6-7B)c'
        b'>Soe;Zjrlw)O{ZXyRTE}MhAe7$p=MwJEx;N0bw_?_0$1`7tvUEi!9gO4}0<G=uCn`FQWC;yF`o+>_+3-4)Ak%|0wFK2GWVV|0~oN'
        b'Fs0aTCIJoRSAdmi$cMfW2BJ_sHzX3!n6`;*Ok}3+aSTf3{RrlZXrlSRQ3U6CktL)lNtMyO$Ory}aPvaVlL)szi0sWS3Bcj%XMygn'
        b'ck#q~402{Rv{Ag=sA4#`$CjiJLP}kl^52FD5`!Cl0oT%1uZ4COyEr0_UL$(G>8iic#Tg&=r2$)`Ha(*V#5J#8Low-4bM+0vQ7ZCr'
        b'%^epA`aeY`4?xh5itL#P1_|^Ek^Q)fQ@=X24Cy}KbVbfs_B7-b3jrl7-^Z)5sw*(#bfw6?4}A{P4~w1?UG<+$^vP12ZV*GcsFzI_'
        b'i0TC*W2_z(*}*Pg)5w7GAftAtZ>jzb;N0I8F{!|CKOyJ`L^o%H;c-g9)vK(2S7Z-#aolfpoQ$3=dV0G8#@}*rr-XLd+Utl^I5ZtP'
        b'-A_X^5w2ZbXo^!PM;fpIDa}%j6kq{eh*(lVmzDv!o$Zn+?s;lx0Qzs0>KQ0UlE^l98P_`!M7B}NOQRgqMD`UJwt}82vcAatOs`%j'
        b'vM)&$l4bN1k*(`ORMlTyDSEbc)nDia^myYUCP9}<ZEsXEF+ep;`u6Sy=+pm2H?t5{QP|l4NmxJ_BD2+fWXrY~6c3wyR>Ct4A?fzY'
        b'=q5C#r=kCU&_9pcNd0@lNp(z&r=@G$t;GEvjFE?2wK!636AB(W){oD%mBrm4acX1*W0W4TX>c6FAKQp2LhEl`WaKC`9mcEUn0TP7'
        b'h?~`s>*n$<CSLNRGy|(WuC?BtpGPBq9OjZPCU3&&{9BIiK&C)_kT!|~u~~)sNlkcF>H#YFtN%HE$Nhz{c}tiX>8HY^hwql|xzu%e'
        b'sp8nY<XUpMW}&{&(PjHX_z|XGhVIZkgQ`3TRZvEl^2|o#GXZVKGNf*{6n$dio`};$mQ5DTaoxy}si8V5Qp+}6+nW&i<?9x=M@*cH'
        b'Ddx!NQ!;a5S3sC#(Ua(ohbwF)>oUT`Fa9A+I_l^-=K6elruF{%gs!SS9+^FL$l#(hv6RlMt2$%iD8!_^DC&?YgIaq9ijhAYWFvb|'
        b'@(s>(`SuT6<nL|IKu!)p49<J6`bNa3w<Fw3b@}92OC>3%$cIu$IY~Zr4=E?ehqR;|Cm)*3&sbFdU>I2%A6w*!>GBz$sC$o@&KsW|'
        b'^uLYbzuvtw!d~e#nKoGL!>Q*b^DTO~P&R@uyZBF@7`E)cX+jPUhe6{&!RpX`#_OG7!u}CqkCpoj51D2wZ3$t|m!0-l%rslaP`UAP'
        b'yK!b#wka!@vJ@AWb;}LYWZET|#qiKCHXzSOol;2Z=^y~PP4&F6*<_+>)H$hE6)&u+QR{i(i5hiUL@(t9zD6zM1);`wiJcU7Hr!#S'
        b'gomz+DE+~0Ru&%mS!AQbPR(tW3=dra=_u@6e2c}ypf<ue>N(P>^y@4Yt1P9YrIeVfnu`bTzxK<!)G!e|dq?00_?77CNud3Yk`FKs'
        b'<b&2+N^t@oye%SnY$oX6VI7u4PIv;+Ll1&Pz8MnLzd_!DQxg`>FG6nf51_2yV@OU1xw-@rU8&9I+3rq`Gin33fx<z&BQPTl0v>|8'
        b';@ugXxxTZ9Q>E)kJ2sSpq;D28*LC*TRasly8aX4mFMF!6p|ijsh2+3iM?xK-==Se+BCj;_#ypi>fk7kipsrA3I>5!!PMElK%-7tM'
        b'?i-9n_eL8v(fFSOCRI8&sDpZEIjEX$^m3Yoc%uS~JAqoL(orK%GqkJad~2}$3^JQBT)NTwbeI2`uCm!O(3plqBi>_Cv8y`gaio1x'
        b'^_XaG+-t-m&eF`n-m`X9eg-6AL}WH@UeSrhHF*f_`bONmtg~mKDnDC8O)0^~q=9AF9_ZqBqYs9BEXCx*Za~Q;RMk12D!}5ibeu;D'
        b'SXO|B`};1*MneG#Fkyh*6hqaWp-)A#t&`K7+HsBmhG)cQaO2Y{`R_E(n<#tr-^*}%MAFmw!Inq94HGqo6ZySok;P9VS@DQ!Gv=Am'
        b'88FUuXkkhE@v_fFM2QKTI;;tZJQH$(Y=Ji-f=!s=pV1k){lg0fY7#1W;jNm4r+J~Prui!`ULW5%!wZtf*4mJKh`_vfPov5c+u7_5'
        b'4I^TU{8pmhpMc2i#e0kQq8tY0T=4uBEiwJG7^y}>CMid=2NY2KBjnZ-ccB}BlLGkq+o6e^xS_AbRO^f+Z;g6Isx`)0^t0z`C}7N^'
        b'zZ8=|9{XL=AtaRjRrFkj+*Q@c-x=@UTBEk5TGhPYiRNKg^n4o%9g^-ANoLKt$gC*|U7quyK-?n^8uNS!&D9{?dj0_kRW<TS?D-4|'
        b'OEATm-YcER@gH)T>iHP*N~NPB;``?4X)m8*m0is<md9m=2yZ}WckgYqa8&tI$lvS1EyU10Soum6TM|7sMIORZivM=7I3}e+p0fG<'
        b'$a`v@qf#~(T=m9VxagGP`wvzaLq((e?({1{q@n)$HU;SHOhabeeVNvKQyLlOwamsLqc5PwXdHuo2`sqvI`EJXN#7RD10l~?w}m_$'
        b'b$++kH}s8|vSkM2OVtq7Ux;WK&|Bw-AE;0fihvZlL*kh9Ojf$Pg|R&$5VxXSr#%<C9iK?C4u9;_x^O_Tyh0h^<Ykl7>yCs7W1y>D'
        b'icv8Ave6eJ=!hRc)*rHPPdHzboT>)zz;2s_VHWNw^x=-g?7}o*o-VifOWO+}j@!sg2UgxcNqRmvOA!p*(Vo6#r{MU`eEFSm-u^JC'
        b'gxCmgeOarKS$AuXQ`YA}Akr)-iltJgIxfGUTH!tGjr_6B=7+!En(;WnObh6-qIblS6y4RW8n34Af`Lq*6;=1FQ7;93m?gIyAE{gF'
        b'Tz?yNqUA+PtbFg{#wDN{GIUJFNxdpPtyn#aHW?dq>vaI701~N6CwE8t&aEN}KRR{b1r;}Z*&EBy>E87MZZyU$eUPpTSmj0(7wSP;'
        b'mkB2`KYY1vfm3s5XjIf@-vFJ-N-QK6u4L5JUq)mB*4G_5OSX6OM)|~f_9bR62t7>j`X@L6Kk9`u|BVooEy`nv4r}_NwS9sZ#yzgk'
        b'_zNWt+TV-z7pH%knZ9T($XxAjjJw^6$OZl6K~8mQbN8{$-MyQ;{m*nqgbL67AvjW7mY)o$($i0Jsz7@RoUI5%SKybkRf>0^I#tnq'
        b'?D6j2$GiQN-JVL+x;{0;r#<1c;=JT6fX~MINy811Q6PFa$*a=6C%vk^_7q>*Mg;Q6p)h$i8gq`_rX%rO04_6}dPsF@dH1p9-M!1Z'
        b'{foOjizU3$L%eZnT}3|`dF1V3e!;Wra+iujNG37;WZ(?(%e(cv@D_9*%kA#X?e_ns+w&U<-mMO3|5;}egPxFhV$sCG$w&sTjbjTm'
        b'f3i=N{^sR3RlIQ{g5CFbLb})Lym&hzw|$98^Ujdy)-;JASZtX2>yD)7Ecy)rWZ&EX)U7j7rmPLxx9P&abo3g#fwl{RI?r$iLIUq*'
        b'6nq@UFD(w*ao%7-k^VfCPc{tV6Y`ON1{9ae(q{sww_vy|OR5y4-2A^)Is#Na9*c6pa3RrM{K8ooHq8~o$ilM3rNL>J%Y#3sx|GUZ'
        b'9pGd*D?)-v2!0`Ey5xRYH+nsMMyz|=cDlnK?64=_TP58!|7Ta;s=d2)$rQ*?JcT_<xED9HEG^z$Hx+qa*-#hkLoX{kdU{Hb%Zydd'
        b'mv4{m_%TAadpg1d%<V`Mvvu^+_-sm32(#6W9tS&*+>vB1<Ug~_dFKx(@MNn(7#yfeW{5NjR43T2@**|0%sTFiQG;DBR&8B+b}9S`'
        b'S>T@)U56BJG*vqPMR_eV-&^4g#qDUmr{3S;OPk%YJS6XDYFXsRo2}al%+l(41T9V-l|~sYE4a_rGeq%F-8<nZK>bmLuw#Ic-^#Bj'
        b'cUIqlWgj@I<4Xx&DgGW_Hk5{ZI}GE_tv3?A^xwt)=vo#^M&Fk5zgHxB*K4Uwhwi<+S+#Z3*-h{#bU*yFuFDPBy>iz1!7bzc&vGL<'
        b'e~?vwBVv^l;)c@sP@$gr&azkY8QJ5qYT$$guS>2J|CFYEmhi0Wa2aQ}XhTFlavdWLz~Y&S2Jk)w!akD5A6L|^NnBdCmg<;ud{)GG'
        b'+^3E!5;hmSsnkA4M0{H^F{9s#481zxGb6rQ{jsrcwfZzbK*0hYS4af>J|#gLe-rgSiEgt8zZS>kMDuSu(rgwz>(t``mI9&yaZ$+E'
        b'jf^pbgTO*IXgN!vO@}!%+89mIU<)=i3tQ}8UTDRO7ms{o#jPvn;!aX@NX}K)YvfkEf+}7dlX-HBYU>M)a)wwPPdJh>Bxk%jnT-qa'
        b'#B`38fwthzY&iLp>e;2nsah^-eJmQ-vZ%`WH^YRdu4Cfykk`f}lvE6)uBJk73+=OoJ%fo|!Nlu-KpzL!bx4nP!cm?lP^x}WSJ%N%'
        b'bmE((4|R3CnHi#)XkR|I%(uWuOMcb<hAJh#jy^GdfRc4jF)~K0b8Z<~pmqI=epmbhNuLz45PdkhsnqiT64g5C#!_eg&CY20CsFs#'
        b'K;lS0;kh3bI4(+YSlKQ{emWWt%RinsWyI*M9FbJZRyoph4#f|gP@Q;lI5DwHH!?8r;+Dw!1K10<#D|Glilgb4bkccT=2fR`e(I`s'
        b'MoQi@SBqoJOxHo<BseCJWnZ0AVKvLU7@0A{$tkQWor^)yq@$taHDrNLs>zsK?){uSz6aSxXHnGzmJ*uEoQI<WL<EUmVD+>oZh%<D'
        b'9@)dhA~QWw98J0n)z?J!b*Wt{3KP!u?Xhr1bhy3?@;!Oij68Hnyo^{cNZj5G>7TBUHz7Apk;s8wS!4MUgx7vqnJ-Oy;?B@1z^?j+'
        b'IN@u`@XrY!;YK@in2AfBtMpvx#E2}nu6`ms2&2{+P0}~rtgH>dqKSp7;78)#uHqFl{~VT$wvnB1D(B(3uO@m`EqS&xoimR!j(##M'
        b'^L)}Nsn5=?=;@bDJ(TlJ=@rE(QJao?^JBbMtudQdglXhLHz8`I(qy(JmeZHSnQ!Md;W1r_n?M0e%o(IW_8EAqp{Hj<-JknLKHR40'
        b'`JWB$o(;|!cUtzY+dYsnZz`O?AMZhQb0X`2F7Phtc@y>Pf1`6yfuVO$3Sux9>&wLhxrC3xoXc<ca>=3d;=@tQJ-`g!r%?nQ&t(L`'
        b'x#H)59YYi*@rFkUqrHF}D_>6xIk2m|>7a|KwxKUcgU953$CxmcW*#N4&r*Cp&$}SS`smfXd!2EVl|87Boo^o^0Y*8GoKx_FR~h1<'
        b'5v_JgvHW0h9zT5bs_`;IhRWvRc9zI&{!Qp<=d*MeC=NZr2^eI3!c0RgX%}#G|7f=#cKLYjXbov$iH?ju<boF)O{OBwyO3qWaPyk;'
        b'#7(Oz^FR+jHIC7^J+{cbhLH*;KC8At>%B2QA2qX}0U$Oq7azTLEwkBcRpn+N>C<sdgt>fvk7Us(-x|+q_ehea(*N5|m|9OKDq$?z'
        b'{C{EOiL9Qnuq=4~4t-k0pw&iHhAB=sZiwS^2M35bjb-yX`th(VO;y$>KCBoyF~6w%=?B>PowmiDTqz1|l`?oAmrRwr?gO0Aq>_f~'
        b'*N*1*vAF3ta$*tu1}Jpz#gQ`mi4kUHmVV3h%ZV8%m?t-Q<Dli^7mq<3Q@gJ0yKCC!TgK-Pa&I%7<ErR=KE*1(nrBFfBZiW(#vJd<'
        b'<&`LY#KB6MY3?U?9KjE<lH(4CRg(8VJ6Qa9O2wL#%^w&({Q(%}7Ofs_Oe<cf>Ri?kRd^{_WVm<vQx<)c_V~5n=Xd%9-28LMnU3|5'
        b'7$YmnMl}xwp}41qLViY|DK&FRZUYJsllvM0`_6Lw!-Fe{>c5Jkg;(jnfDV<DQjv9a^W@@}t!zr3?O<{4Tp4{<OlkZL6RepN%e;Vm'
        b'qm786m-|W2OK5V3J`q8$h$DatT3;?^ixy*!4<SY3IGK%ApAt=`*_H*E<FAp@Y-|XW&qFF{klL+RW+{exL~|fm^bu~+>jSbRCK36o'
        b'>Xv-B{xkF_0c$9WtUT-n5~aG@6T5g}C8Oy$gfk>Cqz-Gmg~I9@dcO`q?Z;3Z$>vqDXF?u@v#LGF>1R8OF!moIZsly_%FpcVXQ8yG'
        b'(zdXF52ZDrKkewxYqmcIkyp&*C`13Xeue+zkY_0ZGdf3P%Y)9XlZuj`s9RdBXPyPoAZcv0R2;S4M9-+pif#tqxg(TN!MA=W<8K>Y'
        b'x=j+R!Z>LoNgF}hAc2kEb2a!bY-Y(}`=2mIQ5M8@tceqPDG(u<B#_#GN%kDo32*9>6hN1Sd}#fLMBh}b>gS%NroL(NK>_c1T^SH2'
        b'2YbY#WTSQzlN{IyJsX%LW^37gu`enCQe(k=P#iz<dfz^gN$TnODQQhGEP9>~6<26qCmUbUrePrZG(KIoyq}hQYZjN$H^j0zH_Hy+'
        b'Dbn97^Z?^|JVuIL;Lwg<kuEXGFd8&lKAA5PaQAANyIKY^<>hjfyIfaLjyzetFJsmiI>dhZeOc1H;2zO+8u!sz+hkFdGJcxey@l#a'
        b'ejWtXp4TW8k3={BOxbR+-V-XkzK6+dvW<R8HrhJgAckgQ>ysBU545bdC-YgGWLXXwmY9WY@(<*wvT}7j2XuCI^ZNZ?tjkf_i<+6F'
        b'MG2$3#6E7(lPmVDdrs-hmE{rqeyo0ND9fwd5$Eu%31#Kka;<-`Dff`XvVvG-snHN-CK1cJND_1HMUS9R&u@GH+hZfPh>5j34%-Rr'
        b'$wxw-xuJDAx`l)hh0zGmhesC>oc>;0Mu=M#W!KwSeaP;@*rh;Aw(W3Mc7VJYQY3CdFVh!d&oxz_5bgSVN&C3ZP~ypj5+a#?^xR3Z'
        b'W9EjKXylzMFY^80wjgvYJH*5w+wEWw`8WJc2nCtT#*U7$XLbiT^ctvefADby@&F_IA(FAWS%pkS29?t*nUM@?Z86ReD2Ol$?~{#r'
        b'P6o&K04gRiw|j$g_$J3G{d<Ca0d%{cj@UMB$94yjpF{6jlS4*Q*EPTi=8nGqjO4LNp-vJ3BqVz=PqB4D1dpHr-mON2r<xKvsqZfu'
        b'Hveco7339|g`8>fBBuc@A&(v5kaA>F${E$j2{_t^aAYnr22#}jL^c4&?TI^^bjXr7@!pRNaT9O<e1r~;J4T*asj|3e^GmyZ0)E%B'
        b'-qWb!30>q0Ai8;B*GcmUIFSUUA!O#~cPlYPfgafpQKlWujE0~{g5HSDRbr2A#2#SCNQtG0F#mCPK##_3B_bd?Eym;MOd<0=fZ6I-'
        b'+zonyKPLIt9#j+lPdh-kTZ%?`*AKHd@Q~%RVs!gyiLvk4%H4eedMJ!;qr;gQapG)W;zY7><V=SFnr8)pK&6ncGd3z^sCx%OmZT|-'
        b'gT_<|eOweTSa>Iq<sZ|)6jkqz#P3xSW0>KD=TL_ZOE>>9sKGH5LsoYYs_Aq;x%q(mc^f7_p~Dm~5YIEHRdGtE(;37Hvv&s!XtbRv'
        b'6S2)h9p0zvF8GXCY7=REN{ams(*I20aGnEbgq=@m*W5`{AoWbbn;Kh=&rde3qgK!U6*Cq3RwC@#meD+QUUF6zwJDYudIZZG%<3Hr'
        b'6V}tn!JA^@gMn>ZM=`ZbO*zYA(kOpT2NMIl(xVSbmQG?A2Xrq{p97BqEpfg9vN~Sh8Hgo%rw6fwGcY=j1C6Edi``IEU>NIENf-8|'
        b'nWLye*=`Lbix`ee&+bOCaPP;w>SAL-3AO1}xv8EiD5RFfb47AF5J=V6B}<j-mg<V~<i&xkfiXZta*~Q(NE4-}5GXy2O{vhKsN#v3'
        b'a*Ubkm;xd>R1AI(A_P>^p80X;eK<kUST!~xOcbA%LN`lb`e-7+;=$*yX>j6E1%{6~yT(WyD?Q(i(9NL&DbGP0SPCfboDJoUy)eW7'
        b'KUkxGybDV^@8(?urO?$wLw^(V0>ij81`4BhOYfIs0{$1v^rFtRffGdSvp5rD_{@l9=!J{{U>XUg^ah=-1a|niJ;|2RfpPi}b@W-Q'
        b'!rE|D<1W&lougWjaXAD26zV!oqJJ|J5-bVwn)8#*ZS5pEo6L_Q$qX`Ij_i1U6&cd93d;=0A|D;hu^ko?eqKK7Qt9q@1DwLi9l8uR'
        b'x{W%=Z6&oUZ`+s-3sqJ3FAHS?#8Nd;mSk<6#*p!2`u$KnJp-!Fn**w1%{P;u<lD)p*<^MU8I?h1%iVqYvk$0_WTaO^#UmMT)}(u('
        b'_Cpybz0hRqQckvHgf|AAb_Jv67A)x}7mb8*&lBx1txv9NXQpydaSR#5>E>*iMOw{ke>TmgOq|l9q6autL55PN*A@EOxk8#V{Mt!G'
        b'F>24bJzP$eadzzi?K#>)8LN1mUTI~y9OL&H&?<>8S*dKaY4^yC@l^+n1SnZ&Eh>&OmT*cFr-N#XMnD3U+e>lJ!w3nB;Wvz0yYdoj'
        b'4f=qHcmy0g3zlfpzek}Mu`nJ9?7HGR$61jRR;A6R&xw|3-KLdomT9GdX(dcjKP?<>Fs*GEcvCrWzY<0I%JBDaI+I0b$uT-FULX1_'
        b'vS&3!G_V^Ce+U#O6xaG**s}>5LZMWq!=^H%8446*#db`%xT34>?L5x%wwQZFA<TJ-#xZMA=DeSP-@3D?Wfc!#<QWY?_io$`EkVA)'
        b'{1?afWl4L)qhdh<bfduB&C9G*aZy3>%DNn$BMOQKmalJFW#mkj0ZAV*C$>lUIc#351$~>e6FRFsYSq8SeE_5HpL>cZEM+P|8?Zvp'
        b'o?=<CA!R8AWIX*c$hkSlzuY6D_RJj@g+2Mqp0iHXnx&VQ!k?2%RV$X2^!#Kgi<PKDq76hA?P)St07B?+doCfnrE39I%zgI4v#*&e'
        b'_7s!1$_j4>4wDuGU%Fs-Nrui+#)F7Ca@=3GXVHkRPv<#{+9c|^91H|d`X3^uef^sB4Z;5(dptj);nPygAdJ_S>*LJMJq+O^O<0q@'
        b'rb%ugt5P)tTeJsoCsK{q>wmk)7me)*{dm@>+R9z#RP_t@Y~@aJs`NA?q2+ID7vFY!^%I3s$wOQ-S3Pmocz&~o6YlurRdw;4+!Q%8'
        b'btgBl);&J-&ObFi<=E^!{m~m=yeFpVY^|!<3wxs(*;(BI{nom=R<2R5>(U9jpWrl>b3S?^mKdX85<gd%{=Vf?u0x~cNnP#*CC^Rj'
        b'h*Nml1H3#g#_R6h!mH`Ew+4=kzpdqqXgKMFX5AYa{7{A`e$U||i@Zv!p$7@fA~#_pdf3&OEk$tp4$M{g;_e~y)FctrSD{*av!_XE'
        b'YSMjr!B-5qnnupqg*l(Wtab~j+jL%UksGT{2*}NdQQJf@1lmlHb$EMZJLMT++`a!Jz$Ez+OCD5gpWonv(o21br6(n@J$oCfJ}@;&'
        b'yQ0gF-csZlt)Zy%uN&<~HAmpfT-}Ts1yn+FCv0E{5T4izL72c<(Jgb?uYydxk>CkjFb*(sUF{Y(;*wA|k<+<>n_^duGWPQzM^s7i'
        b'LC5{ZNF}L_F`kcuyu2zkj$l6uPJDYl1(mUuz8DVOsrO3Us{YTxljzeG4+5BOLrQT>??});5;U9?g>jw?YkfQjWxO048P?U<oSTs@'
        b'VYn$Wgy*dwFl$5vO}yO1Bw${BY8(jiW$n<Kio7v65DXC5NIrU%cvFP#%hf8+z919rm3xi+@J)BxmI(6)9s!zC#4cOd5wy!NEhV}H'
        b'?8)|Ei9^TBu$qHkdZS!6jF;oQ4d+v1YgMB+#BEecLR6S8YZ3+b1}voKZ3GjaxYhmg7N1R?qKNgp66}2?=#!h!4eTa8U|186KlH|7'
        b'Gc;7FJ=<W80d>eO@ea6OZrB#h+oDacA;)UK`qsZ&>^yTdvAp_=NZcqcCSv9{nKlS|lX**!Nr1BjI5tD-=54uqzriQ00@lKF_>S0E'
        b'poq+GC!1eu$EY)sn3ayH(#^O05;J^kqcRq#65YB`#sEp8`x#0C&eq1z+AG@|sDVzEPcA3(aGmrNXQ9=XC(qK2O~`Lvb)NNoO52VN'
        b'3c~}(S2FFUk*5Ys8*&>|J|kf<Dz?8&nKG!%CW21INI8B;jwA<c^k>nkwvfiC^YNZ%5J%DGM|)lmFwa}$iY#>PLE+G1);>vIidyq`'
        b'vn`lM=7PNRl`M_4JrG0=e?VXO7`5azMBQd2N{|!)_NwdO^bg0KjxRZcUqS&_mW$dWHwHCGsG&U4hZ^mX>x&egcTm#&ncsT8E<<tw'
        b'VpJQ|D3FZdKg9<X+GnpiP<(BWLs~-C(=99W)G+IP$@qjU0%sKp0FPPEX~~;;>M(H#xsIj3jqIa<&X<k@f7H3DlZRA%v~h6%wFsX$'
        b'G?!m!1i4AF-<3WSKruz9O<7Ol&Nn7|)h1zs=}8KfE9#=v_OgFkrMj@jf2=HUZfa?tT>d$t>S7T@xxo9>!Z>95L*Cu*#V`)q_bJAm'
        b'*7vFD+{a|o))2NW{-|#WIt7EaQIDm-dTg(!HpNf(ulLti`OhVk4jS?8pX$Oy6Fyo5U>otKxF$J}Ox6J%EY+Zql-A1dcM*=WOENgt'
        b'MivyV^q-qrl67hfL`7Hy<gxg7VzIjF0w<H3Oq5$<N>v|R-lPJGTnGGVfjmjEQ0A#b(;cP^Z{Qq_X;1&e5HuX_&;|4bK#BvSABxC1'
        b't>eVFt#2Xjx#CCWtvKj6C0%)1!0vWg_Pw}G;hx|(Qr&N)x>~8O`g2*NYM2OqD?Y9md6uEazXd#*6z~N7_GweH@|4cmGOwDK8&fYl'
        b'6t!|e)P)6JOMTz&?OtWMcd}=;pCshcBM{J&9?~u#?P~hnukOQSXL{!c>`?@I8L|rX3HXox?W%JgP9p_(TE$@iUbr++0DAheDYhKH'
        b'Jz1rtu8)hO)t`&l$kf6eyZfRDf8*}553Xv{ukymMJI9@s^;7QaF@~3aU@jVFkwd3JobHouC$C;}%5g~?AE#mX`rb93`~197S=Ts>'
        b'e=ZvjXyCamM6HZH9al2QVv#u-k2Z;6r{hY8#%+LJb<!jlFsLpkKT#GG{M2%(;3Hk6I!svEcd#ed{>+ia0#3<g8&Pu~&{E}ng<lIy'
        b'LXlxnZrR0SKM1Hx!-t~hgdh0pNpu=1s-7+wKaJ4m6I8)oiWy!PVL7y2H@s?%9Fs17bkpZ0-&TdYbv+yGWR-RmX*(kn{&u(XCddm2'
        b'w`mph`&3vq`i1EIz@krtt*|g|p`4-YdGfVCWi=_`^a>--y-5nsM}A4eM`y!>yE!;)`!LQp&Hun|V46aNIM90-y7H;Y43Z)=6ka-i'
        b'_d<<pWjvW34QixIO|SQ3>&kT+dz6NXauv}$g)_ONoz~dp>ozN$HIqQG&`Io&&cK*FcexHKVROzLnq9OK%W4N*iS(QokS5kC=qajT'
        b'&X|dq!A!-LeNa$9T`p4<k-Dl+w=Y$eEY&qyDyZ$RP$e#Ed%3de+maG0l3zhpJyTLaoh(;P{9b#bq>>u=<u~lTlC>1(xwyStRZy@B'
        b'@`|!`wR$Y>OvP)^4T+N*mA_YV>AfHL`BMCsw@v**L`lX17riQ|1u9eBR3S9bnNiJPK+RRJBN{ED^R@t*S$67djtXUD>umpOx35fK'
        b'sJZr8(j?YRE!jNqOopDKdyn{aEC{?Lz=vKuyHOVaR}bpuyfO5?s{LYbufJrCyK*rqZ;?;{QP_VG5a`Typ22PZArvH!VdzSe%66t5'
        b')1HB!I#oJmyJ%lYffgOg28CbPGk~R^L06st%8Lk!?PPnWgjTHM)5x7Pn_&3}w~$#;E2sNUw6Fb};ovpfd+in~rzAs}l!8RpoE)Tu'
        b'X+{@ZGr!#~<m=!dXB4h%yzJ2*v|A_f=`wAy!j~LZ6E8XW$;L@)nu}W0w35u0xw0ucm0-`t>_EcL>o4c2w&tA7QRQb?S6Vc5?#js)'
        b'*bOV?0in&)hh*Nuz3nrr^JHe3KbKBKx9KWzJE>q&N^*4eY(;5DyDf;+-Aal{F7I2l5T)%JiqXQnm*kl2*@RWbP({bj79=+mwzgZ2'
        b'Ur&=UYEv?b^M~ynW@v<+f^sRa+HvfhU;SLF7Ho6;fs}jf)J)`|X}2zrjnN;7K=CUb*TjVlwintN8hK^NNsjD0Pc6cgQH;JTdPsp$'
        b'@J8g!(vu)CM<TJPJyq@Xe?-Vhkr*PfaDE42tpBUPM=NR+imD?5il(OsK8AaqY_ET^oynJK!yoVXg$%Uka&n1E^Ps?yic~7bzW-(x'
        b'VknBT3Y;xzKlYDZ0T5OwYnR<V^Svwm=oz#5FT0quq7QIhwgmXE^8&`(9iG4Mf-`;`#Yft0OA%hRlw^KOo^~My5=M&2mu@uhG8;)2'
        b'q6h><8W|>CApN3|C{{P&%T<kBv89P!Zr<u4^RV9EfUaHyf)#031oc<7TW?Aa&5(@v>8^l4M<T|1=C!j~?fyBaN3H^y)Hp>lvv50y'
        b'?x}J4$?S^)liukI5Q-g&X^bM6kMo40stHA=u9Qr1i1DJTMl2wpyE=}@cjN#k(_X|qZ|ws1t!>0UQ4ibu2z0kd`ZrYcIT;L2#420u'
        b'N@u4c1S~{y=E|v&gk7LOIznlCGOAbhlNd1~GTE8LrNT0SlPOZkNmZ}G;ma*RUN{VeI7_y}5<~!GWhf)9ZPD#!41r%r+Md|u`Ve=~'
        b'SyAO^9bH6n>eo+4rkSZO@#;$dD3Fx1K#NSs{#yZ5Vo%0;F81{N6ucsOp4?U1AOwu}xM+zAg$=6{bfr&0lVy=6rK5oWjYaB@nl3?l'
        b'H0_57_^OR1UM1|x2uRn0r19>{iJ@UJlAiYU6tvJ}WFBdBDc*B3KvIi+a@-E5N~ivEvr1@kpG5A?+_0*4yMvU=>~gC2oq+#zz$H+X'
        b'uK=Nu_9;Q?sy5-Kqj!A0&AX)Q;#r_47RRth0+N|GS;tWk8a5va6qBj15RQ#lc^^?-izP*+W<FtKgsYaR+M>y6B&!fmJY0g^AF%ZW'
        b'hE`%J_HWVKjBG4KGO?Buw?G9lC2z4|!h=L<p%95WUyz}Sm_g9bB^2k!b?HhchjBTL9njbBF*b9T@wB!`iwvgAu#|JGU2vz)UV$EK'
        b'tisAqx7+<&a%BWvh}mZCV%Fr%Mi)}P+2s<5FyUGiUA9kjK6{U?E|5p1#>%*rSlM!zyOeVTdcN`k8e$&7HUv^%Cg{J3qi>1mf?xR+'
        b'V(8DJJ%Ht^QN(kQue|~G*+BKL&>Nwr10bU!T=SCC=roecA-Ehx+RJIXJyijA9V)3MA|qRNj-Zc;?4>sUUv_b@zh8U?`I~nf6*1>W'
        b'KLjsb71rpq`9A<k9HprGW*xfTseqP6Ids`fkO>!UaxLJr%xV|<K*xU87T}O|mQRWM18^y|<nRuDAeN;<$#j|@Ciqg62i!K2>0Q%^'
        b'?`TvSZeeVGz~)5AEhOj`>AfxgeFUKAcY$?X109E=(YK^miSh3PzGM|Im};VX(D#A1U44RX{QCgLL7xd6r$Wvrd)i0^CcVy{u@P$='
        b'lEi;5fTg}dv8KRsVkVJBA{QUe?^-r0v#Y1<Sf#Y3!$OoFn1{H%np(EX91xUcFN@AG%r4*y1Enbe+r0tlSV*E4l95`j{a=*ipiOEo'
        b'qK4LrdF!DTWUP)Q9F=0E%1j!LmFlaoR49ZT(DF2wEFj2(ABveMp#<Tq!=?1R*v2IA#<|Gi9>7LVi#t%EyX<tt55^)z2NB~DL6XEe'
        b';)v0cqUW|hO#B~we8Do}0rToM%LkEz_E)xtcUdS!rc43CLx$3lqcFta<|o?%dgQdo{GDHDr>tb>%jM@~h9<<wB3&B(EUtFNva4ZH'
        b'Q9Y={KCr9Phg?=nJBR4n{JGyqmiH}W=j^f*Nh7nF=k4|++sFRGytV*^y9|r4dHTzG&?wv|Ih8Ki9pLCE(|2tGHZd17qA*WU7m486'
        b'OANu~COKjyhkWNAk|=sX`RRk~aX*?j;47=rZ6EpzkNX)1q79iXepltok)ml|{RWY-VVqynB!<}@XbU7Gd^6V!n_u?_gaJ;E>AIB8'
        b'6<64pT^2$S><7}4TkHx$zev9=MgY0?-+VHmZF~jo$@Y(NJ7puI3SDngXUkP3F1Lopq$d<FdF_owwRpvPuM0E{5WbpJwQQw1-$v$O'
        b'y|4PosG=|q?5ynY&(5)H^e1Aexoz(}&?<e=#@x!^aw)(O6@cmGc9p5ieX>jSP*>m7lCIssCeg#RaTEp|Il_)p6D9{JtZ(WghEKnT'
        b'gyD2#o{aZ1sD1S?BICv*96_Cp#)N<=>S6#$`x>mvOCmeg3QNZD00<5I#5uZNqPInIH?OR#2-ZcS+aeL+=lY>Gw$fkQ6yfDuv?5g@'
        b'13|&?Eyx>&ZZuQDF6qLPM6YRPdKY`HH9&r|H-Qge<`O^J#=x&aBD2*H68%Tp5EDrpzpu!1b0rpF7{0`l-)Jw~qOTx%CWUi$xD=j~'
        b'trLWv>YD1g+~x~l0r@wKT&QgbBXhi=UEJhKW)ci1F;7by6Yt9-d~)P8O0tG2JiqqW7a$VxRbZJeDoJ5L##Mx8s_WP6{eCOKzSLHJ'
        b'Ji#Ks!Knzobk)$08E#(f4Y&Dw+sf>O#ZH(_{ty{#5&MXyy1%n~Tm9+41Jx1a*^xGm_(p3HVHcJ)i&8uXfNi*S)%;8wNJxETlTJs0'
        b'c%*$3W7}H&iQ`R6<NWp%Eak&rb3#_GC8_)XdM}HJR70hnBdT9QP7YrYhYBQe|0)h~qL;sbxlR|^x>odvbvh#Ce~E>gS{cIr5zb{N'
        b'aa2|mu<0dOKr@BgEv;#OY}wvR#uXgsc`l;*VT`>lM9$`@3-RMJKz#4|HoqurkKEF?CmS*dp0fGKf|^eW+J-%Zt`cwMNzepjg%RUX'
        b'^#dr3Lbk$lT`2tq!K<Ysuu?A&)dsBhKia~?=zRp*84~H|gDfmbZA!^Xl!Mtm5lGqMA_{{YP-J%$QF!ku0ee9&U3Em3?VKWtA}Lvs'
        b'eP;10&|ZsNN_4<i|2)3Yzlx6}gaWGSlgmq0?i}Q_E3zfE3Mw*-w%k^bOHq2Ur03{mOB(GuOc5$-BE0JxU7hMCuGVtb97fvZpp`QU'
        b'^dTEHN*U)BL*K!I!dj>i2Po1|?5x&zM-|0%3Y-Gel4)N>*}3Vk)nG?T+;6;ZV=J&h=)SWdg20d$?Zd)mkl;`}rpqo>dO0YCYnFz}'
        b'v|G=5=vJ3;QO8w+{-anVqoPKMp(@dpK(D4`)5?gUXGFVkQAI*lE;X=3Wv7j6uSW)KcNj0*Rq4sLmjq-~Paa;A*M$U53Zowv8FgAa'
        b'>lVx}paq&sRKFFW%TyO(_?sBv|LkT|2J~Mgq-uyEGgi1>fPHG0;fC5voB{)4s-B5qIr_^RRQai>3q#0N*KADS2qPjV19mxCWgckF'
        b'N0xgRne-5sZqSy?r<E5mF@4!d+BH!XM-C&GormzKHNP&s-f}KQS$8LY2MBY`uN?cZB~-~wIy)K5&qb;i%*3(3w)6>@;U9PGWD+wK'
        b'4KO<?@9VnR()2=J>MDcnn-*Y<Mad+JGIXc~8SSQ)FoYpb1o}6ARcDd7p2W65LCakA6B8>qwrJnJlXnDQM6LPC*4+{&`eI9}HjL(o'
        b'ustKH%aFux%(+5H18dmQY}?xEMF+MominerR&N(}#L?b7$rNMFaBjIh{w@DOK__gG4%A<K(^!R8!YHqcZW{N0Ge?NrI~O*1rnmlb'
        b'kK8;{@RFZhNF&3fm-|faBV?W#!n8`cMUTN+c+!O01Ud%8lJY&<TA<Zl1tYJWm!{Z8Hd;rP*XDOxtN$r(i*AfgZMx*?XqD8yyEufn'
        b'x)m@C^!pIuR}0KcucA@@MiYBlPWcFGM{Ar<F5?NAyVf-A0`qP(#ZDH|5<&^Ubwl%<3AcyF<7@K-R=3$B7aHYh@+K}a<}lHswjt#*'
        b'57gVbRV6D-1qB<vFN^ej7Ck=*#R9|VC%1ONLX2!pT*^~e&77~GK{6Z<jBH$20#5eLcdWS;F%C|}sNFA6(zQovZob>4(`~SljN+(f'
        b'ki-~yH7sYM_uWJHo^4cZZ902c)u=hr)E7;q?!0g)`s$4H-i3A6$l~a$uZVZ&!FFbs$+RI%7?bysPEN-Dx}`Ij=jQl7+Ep9Nb5``x'
        b'pR#?h%kG+k%<5WR<P-{RAJ+TVU4y$B&pl|~LsW}`HMLk{Ev`8nG(q2;(kS>pnb8dWQ)I}ASmZo1&}TMk(6JWBkUA^6Q9Au{m<)dM'
        b'9q7Zb9L@xB+~-FgfxKzGY_b!wX<wz=;#z#kYir`!K7ukG*Y*8b6%bCtVGTdI<hAdUQpPFN^Mqd@o{RBsZIQgKtF^^g#HBmWY3i(!'
        b'vvTjby1a;AIG9=KTs8Xc#>Mlzf*Qi~KCJl6!cK4Hh_9S>N;{jf`0-5Yf$GVa`KO(ne%4iPPJldQ_(ptGp<Q#^n+|GJ+_do<B!)uo'
        b'E>qV4qv?2^&{=e|NS#1|>J_n1N1|>^;a8>po<eKsGpbvbUv+6b&+a-4BAyXMJakn{GUEZuy*(apvtpO7U_;)PtYn>bH~wU2OX<2@'
        b'TvXdKpN4s)PpApgp1ziG$L0WBD`ObN=oQhaxZ_{F%cv-~ud@y9>=O<Q3agGB@a)@(-hd=OP-jQJ83@oz4)gonZuEuvuyG3<psVI^'
        b'`pL-SWU|%xT4cUZHL@bGGJcwCsxg~eWj21mt(wQ_X>L^przf~ozcOZUt4zjrZdInSfm?My+qu)e{|?99A8E-XNbIDdD7VcMM5uCt'
        b'8xSw(+rm5o*z*$h>gvCW#`8=9dI-c?cjXZ&IdAwgcl8s4La|+-JZ^;eLeS%O7A?My<6r>jf+GqF7O!1#%ZNNbI=+<N5ELfv%9EwO'
        b'9LwIbt8S$+8T3pxVOQEzMvd;`I2TWOGIrM{ABm<bG-n(6IN3@%pH*l-xzopCw&!*}nXs!okr?_trhRi#`3!<yfR#Uhe9wX$#8Zbi'
        b'T_A>*OAklC7Cpo+pMbmM72C^ouDptH)FXBMgvW{S+$>Ao!Ia)<^G;peNR{4ftDNde{?*8<rPte1ci<IMU8{ao_}tFAl~!4RlMF%B'
        b'F8^mcEvqb+WUCZT<N@tsEb<h}VwhQ{K~=7{rIC)mh=&w;^HO)tH0Cd~)FtQ5OUud2H&UB?lZ-j8)C40@QbLUoMp+Z?sX(*Zh%<2y'
        b'M~9IcfiPj{61C4>W@!2y$q~kvZ5AV@U3tYyYBg8TiBXCL!{Q-aJMW)XyZ`TPmR089!RuincwBr?;k@{x_osf49#^4H-TflAu0uD9'
        b';9>q#ZA^^ez;#Amqmh}37M^Tzn<&Qt5o!cOqIN6hKhcJQf%RTzqIYOC<{LX<9xY_c4owuJF<DKf?bL(Oj*u9R3I;{(nww0F|4(g0'
        b'7ZHxyS1<bep)v0H7LBHQPvkq3MTfq#YBWqD?D5gFz}f27^uFE(Oyx~+-2Oc%Fyp}sIJ6%AeQoH46M6+TSH%#cyT#N5I>Z`oipUEM'
        b'HSXU`Kz<{2p@!hF6yg-+JxK6+JV4@@`~**8+UvOO`(`Flx>z`akz<EG7#*OjdN}&RM49Rmz{%<v8||kYW8?dreQW34n{zE8&#C76'
        b'^UeGxctD=yOVfj(9}R3=k}v7;_?$1aF&c{<Ge6&kzDbkjeLG>FN|*a+_QPg7$DuImWb0=i*xqX9V?Wgv<2<LAf)`FfJnl*$_S1f3'
        b')8sf-Vr~fLx;9?A7!Vijd7`axSaN<c@m=~)%@)p~-GYL-A`e9*oZfB7@Lbl$$g^ha+!eaS;#Qg;zV3ddVO#V-lgeE?fF$27p#!zC'
        b'%P9kKsq?@#8S{$$?fJ_ZKkyervwp?<awfcS8=H8cmEni4x!W2})~dF92TpobFM7AWSUd0A^!Lten;bY{wLRSC|6SW$%DkxUJre#r'
        b'!px1Co5;j?4m6`x%Wj)L0zZ1u50B7n<jo7(+@LrSXV`<S?poWp(>Pn(<vdj_31}_U)S|b=<2-$C8&{zjzaOF7pdE~2w>0xyECP04'
        b'8*|Sg`EVS}Y$%bLG|)V-{U2LSZr^a~S8YhXc^G@QIj>%i(xHUmv`+cK`HIGGeQEUe2HTFKXvL6DT7fm9WGMcP1oUqpEjlIr*XWyU'
        b'H04h~Z5!js{Fo*=$7ztOcTL+NMaxc)rj1dP@)(~SC?s9iq+<wQ9!5UIq$$SjGL7*=-%9>WquZE@Mgo1BGwMBLn?JhkkbF>>-{+z|'
        b'^U;)$1mU%i_GprzYS)9H4y#<%iOjJJC37ssUTX#M=<fS(_UBe64eCIRqZfLwwuW5uM?C2WP@~K9T`Ng|aOMR#1gIyq7XJ^ejFq%g'
        b'00&(oT#f2=7J>E}0SVbOiq&`jG0ZI62@+!zNWQJO?M!Rw$E}{fwHlG`Q=vA-rM^m3@4$_elbDPQ<DiH=gO$Dcb0?+Ux{6C+R=b#f'
        b'h5y@~%w7+Mb}Bp4T0s>N7zq2->oL!?o$KXUQQr`b$FWop{~yDuF1TM&`s^4<PcDpZ_W#$;<pDsCw8bp{((`MCBTp)r)ODMc1^Htc'
        b'^b``0(cqJ{HR+3K2Gfsa8CDdo-N~dDEEs!6okd8hS1Zhp!c?##D>znmkG}J?$A`eA<Qt4sg`VT$N><8@ma0v<WU7SIxk$t>K(1d`'
        b'uGFRIKt^T*tr1(U3nqLQ65M<+#oISHo1CSuw6d?XenJ(~MuMC)CGE*H1N(9-X_IMi8A-@WKW)PBgo2c@rjMH5A#F7J=7tfjQko<t'
        b'YltbN4cFs1qt)RvnDlKlw)F!&F{!rRQ`@Ssk$Rh4LnsQ2W1iur#RNkVF&EU?xJ+ZC-jA-u^)})Uboo65{Z}kw(qxk*UHikVlwT8$'
        b'&#(ezf(hMyAm}ir$7LBfj>!}zb;4rXq|>Dg%%l=mNbdidU=9}JlQcMvKBmdW-j8afFVUYI%fPX0oX}+`GHh5DDXG0*V5a1RY@AY3'
        b'=;zQsFw8bK^o2Ou`t#5WA``XVjtw=4n5U?9vwZWkXXJr*WB*)zNFF$G>*SlN!wG%Ew`#P+kOlKPNLqa|r0QH9pkvA0Xp){1$Tg9<'
        b'a=;3cpW#a-#NI)Ob#5w9j0IBSfIK_D38W-Ijm|d$+L*wy_y9dMkb8fq+>5Mof!x`Fl=xapX9uGQl*b3k6Z~^qJqHj7&$CUPMZ8N{'
        b'%OQeEmmG-*ub?Z%z^S!XiX<k%Rw3=6Y^3}4UqkLCfan|ypF+E9DEIaaeD0jRP3yIczpc6E8+l)f+S7*M23%@KvA8V;IqnG!mEGVv'
        b'`yxRs_!KRZ;BId4<<6lCAfqs@wLlj6BuHTFnBK0?*eB5?;xp<D`{dM$$KV%c9t%+#+vE%zlWkKNw*6eNW~_oLp%F1Z1+(K)6(IMG'
        b'lQVE88&_<^)?kJNtY$2WU$MnLSt);PBbEc(gh>VZen!pIV9OAV8!mG$0_!}z4ulq1nQVj`^bsgk7@q$*P|6s7;5ttOH~<Qu=`Wz%'
        b'ge7ziGWTa;>7;#1rF!UolqYpn_)>EgpN|>G3SJm<bLr@^ELN}%jVZ^ZOvqBDYwS~`%(%`$Og4kjZdATifG!_S&Qh+>*eBD;B4DVu'
        b'PXQG5_Q^U^epdUK;cKpQuzI@mfhWarUIacj3F?w|#t|oao@&OFV+9psC7KmF+X^gp46qy0V4lbC=I2N9vvE8Nb!}dW%YewUw1~(*'
        b'J@yNYTgGYpe-ZXJU`-ua<M_?ZO-RC36TpZ8ySWzv0ih+>mXF$95;1&KyFfJpw!0)6M7r)OrNvsin;UFMB1m$Hkf7a7QmMeo3h9UV'
        b'!7k7)S_|*0{i4?HOYO3y)OIaJOY!6WW^ST(_uc3Je;%H2@7$R=XJ*cvIcH|hIY9!Saspb1RL<8jX^3bn%#zE1TI7q%>p5IgaF-^B'
        b'G3}A%yfOcd57g5Mxeln3l6!(j&XFAM%VGHaXME#BfbD>a`47T2fJuVLsnz$;MmEpab1=ESyh898BAo~059GQ?4i?7|h;wBKDf0Az'
        b'>T^Xof%z|e06@;6c`7UfgUb<soMU02_9+0z-N%n%kWC!Em=Eb_<WZzi_+><6ETCJ!sWSc<X5C>BJS2TnU`UOwS+K?}g{*WHQj;n@'
        b'lf_-IL>jiRf32V7BFis&|2T+bUj!h*0KDS^Edw+`O}hcqxG)qn2e8u|wD63thYvc?*mVog2AG3!Xe5Fze@?u-3Io&8kc>;;4BvT?'
        b'tBI^J;-CVMb%Kw8tX<CnbavMPrfFCuf*1AGK%q(opa5x4{)PlKAr;d*(?QOPwn2{((4I~x@N-2=s(0a0Io)#qDv`?UzOx}OPDhc%'
        b'&qd%DkB8T$;DS%(9<1k}fFa7QfOL_1HJYZBjeL9?ac`^fnH+WE$}hs>&~Q1D9EV1LUwFr#575w#GWt6AR$&o;e&k)IYMQ%Ru=NAb'
        b'0O(I64n<dS5G3rPJYEE-%+m*(<evvc<J5rv;glct&ko{XQTaSK3;{!h@SyY54g=Ybfw@`}z6N=9`b>no4>T-}ol;=j>c9}(k6ehs'
        b'*Mx0<QLOtyv<ek-Q3<|Go>O>XwGzKC{L(6o_}p*nYgQ+%TFpBzIJk4c;S5w8hfFQQmmL1HU_2F1JUqa`Gms@Yh{uP7<#@eLj}fc^'
        b'&%eQ4jUoJtT@L|t-`QV$?LZNdyc1rK-?@Zc*G13sA|G31FmTxmaHuxwwjl=JQYrBX+kpTGhdjr_UT#=eobCqfiS=3(1JCq>`%WUu'
        b'%aEh5R$4v=|1Fmp1dJ=Lktc{7X*@y>Sjs99{~(iu86UaEzjZ65>;4&bli9nQSmtgJ@rd^hkYxCseIboUDYzqxo<5))Zq$(I!*Kuj'
        b'svBC2@JKIXxxpy1u1T{QQnZ+j2MqT~upVe6o);kit1S@R9r-P(SfhD>OIabXQ6NjjbjOgEJ94;+=T>h91cZ{2f<%lLj63E0$c@7z'
        b'W^ySO^zJTC#EQtYlB2&XvWgv0A!iRP%dp}_?qD|SLm&%Yh8N1a>Y<RWP&R6Uk*(7s1;iS68Yz~h&qLd82y?0}77K#RL;0kay`$(n'
        b'@t-i`A<SQ010V-~4D!3SyCCEL9i+4*6ipjc9Lt3uH7rOL=DTev{}<-V{|Pf8*iJT-$d7@3a1Ut0e{UzKIORWJ5`SvL1vHsL7!Np<'
        b'^&vf`i%ol;(Eljy5S#W};;DOSyXPlYT(Op?vd5h;p1HEbOh!PTr}tum8P9Qv;semmSm3==Zs>Py=A(!|1#zx9;O!R!eXy5qF&&q9'
        b'9ktL)zEw>B3c;6}=oZ8#@#VPblr<rT2)|lmeD_8OA5)u|{H-(^^{qS*@S>Bazc-VMV2t$5>>kl?gTMcd3oe^{doE<FjEfZao@JAN'
        b'`%(JcXE3XP{?>7E&YLX1BZtFy*@JVqXmWH8S`to<&*6CBmER2>ksDvTQ*PLcfF!?{s|W;({wNKd?EQ~4P_*Od-Lyu7*)PZK4QM1N'
        b'FMSUo-(psd1L?*8)-B_&u7q4!Jp387jZHt*0=R#pU-}Ya_HjwCpn;c!qdi=J(2$l?YmMu#q;s^XqS5atZyWS3vik5F3rKG`_(XEF'
        b'Y(+p;*G<A$n}9xyCvUKZxA2v9fdS`Y@nk!A9^e@lL>M<;@vF7Ec4)83HR2Jvv$sL@y0{y6?Wpir_MYAKJNDo>&c0s@zJG>D%?Rz|'
        b'n!SQHR0-Wyh!p)du4EI5ZTK!F2@SS5xJ+^E#-+1F+?}ML=N#zR2;^Ql$9g1(*^H0OY3CTWzi1x^x3-~CK*difXp2s2$O4Uw!;=%E'
        b'<#;A6onlCgPD}A8y8lHibo)`n3uMI7+gc!?$T|jZ5P~+pR~WiPQypY>i1u41Rx}cfPw*Msi7@`{M!?Gf4~mSryMCyRxt!3xtR5j='
        b'gR{>Zftj4xlB(6zjkX?6f2P8wpgAZWjV#SUtUemu(>cs)cYDlUtKCcwrztOV36i2alayIq%A`!6*bOEF^=?~ePo386(T2|6K$CCX'
        b'qtT9=cb<E=9jAiNdPH@yHF&J;bhNFE4hY=|Cm;5DXICn>Oy8eTy@2wyvLPSV;p1UXFN;-%O-CQ8S((`|Em0k4#Y_E>=fkS`v=DFH'
        b'dZ*XvxGL3ao($VJ+8Yc-w>k^lX654!Xsx+G(KM4XB`v%)G7CG&9|vP{QW|&AC9HJ*R?4{c8;12yhGS!#$NDsS&g6ZwIGHC)f)1wB'
        b'gO0&E?jyMz47xHG%Zm537AfX|!t@-%M@;Rhn2j6iTWKT;$OUc}%`>AHJ2|cG&_TEH&F^8m0WF^Te&i;j82-M8J2KDS8GF7JbfaIX'
        b'Qhf8h--}Uous<E4^{k>5xA~Q8@XW))#ZAKNq?p>)>U+G+tQ12VOTk@=gFI$StC=)6?3BRRs`2cmMqK;9#TaGJ6V}WmM#nyxo*2D+'
        b'4VZsz?uAqt=xEd&Ey$ZfiRkuaSBdqlA=kL*hN*uMQSD$<iK4q{$EH3Z#O>N^?7l%}D;wlIoXT(Y;q7K6jEhP}oL^!HCswuk1pf&i'
        b'(84EQ(J1FhWoCJUM`DhPkmjRQR;!Qk1k0LH&KgakTTI4D8vR6it8d=(?=e;Z%+yxjHP5{;vfn{5LQ#9eS}nD*30GOA>(N$F&|2mD'
        b'+A|sre(uDjR3qwTtzdA-cymKdlCA|&jNW0GWc>Qk5**dSy@tscF#6J6w?P^xsoQlMPuE@#`rT=)G5hNMfPbM9T^yWbM)!>#&H&el'
        b'%=K{L7{j6e)s1v70@g%tTuTo+@&oLvN^&vvA{<*{Nh@BiOux%7aI4P1;K`GJx<!dw@j@#+7HL9R@dMHm;KEWaXMoego&10qt?uWv'
        b'E=M{x&fT5M0G#w04j{S7_n6Uc@cC(EOavz2dNzyM8*L)R0A1b8ZLmBHpdH)3??La#Hjkomd2J(2jO+))h?gv>N(b}>z+ak%OUYju'
        b'&@-dE0N|eQQbh;5)4favEyhu}xlL_?`GAfpd!HQ`)$dyYOVbH%8~wMaJaz;=-7ojc+1AipyzzN6x5#7@H!S_LV%?0?egp5vW#(0G'
        b';~#GE{}nusvQOUQ#f3lO%gM%Tcb{b)vv;3Glix8RUUIh&I^OzmA1GG;_dYN_^`kzZws`K^0~4D)_)>NUGu&D!;4Hg(m6SN3*V0=4'
        b'4R)^X+wWJh@xwN?dS8bk4jqmC>gM1{$)HCJqyd;v8cOz_#D<Ul&hcMAbzp&`fAMxpdOc!q7yRTey=&V8WKC&+kMk^x5o^StQBrNq'
        b'&y?=LXn_DPJS-IYmGF3Zt>{!ajUg$8JGSmWyi`Ufu7Gy;5!G8e`E;TRJp0l;2JpbY8#vwffJc)E!(+#+*Puw=L;l81N>aVtlSey3'
        b'ZC82%tmmwb?-?q=(<w-lVR#G}laQZ-9&~SClHPc0%Bm+hg3%MCfHN9UZQh?58S>GI=(YP}N;L_p7kLG0JZ3E~_TZDZUKYs@v^X5K'
        b'jqlLIZ+WNXj;~rK9JN=vYEE;=)6i0g%tdqoZeO?uhTgX6sk8gx=Cc0E#f_blWnlO$Q%u5eBt6WAgI>uyM~cB{fI>03F?D1Z!vBJa'
        b'$%QurR({gMqh8t1M(JqGCJT|6LSojv6FTK62KlCn6Mwp6XQJ+l+e&o?{W$UP{u(m*$g#$C;khe6s>wx2GMPFGOBcN%XU!oSHv{b>'
        b'7ty@Usqr#(5vXN^p<aa<q#_P=2tL&KxVX8_j`9Z?9EGb!50BJyj3>WKl%ZM$ST#nDGuC3|l0mnmo$eR*@H~2IKP>3hH?~g|$9(f;'
        b'@yIxP-EzNQC?EyAM$M9G)N(&ErOvpImobg<QxVn~xm=Eo8gN-oa=p}W)2b$uI2mp!RllG0x5gq%dzrR~KSIZ})Qd2gPEe&+syur3'
        b'vs(``RH}jokHm*AXgwJbv`a!qK48GwW*qoVIz20OaY_hm&E<^6sCF;3EEvEL@3b*+1J(;(OA=JzeM978P&FRjkpLDn>H3M1O4SJK'
        b'vi&Ix@VPZJmfg&n%i0%$_7K$M{vJ+%H99kL71R+IEr`ZT6OzJ#oB>p+prFx!E+(4yo6$XuXM8vI;{qUXP;c(P7oYbJE^~BiLlqAi'
        b'm;LD)b=qZCMzM#gejh>|*?-4Ip?JRwe|z^xVST3{pom9AXLD*yaPQ?k7u?1R)4YAN<gXK3Tz?PFGYUykXBBVN=j7BDd28Q%kRMuL'
        b'h<&a|4!;Nu>Z4x{aEx&`q_W#M^v~W9wRD1(Oms@xonD`bE5ss22szAw;av+b^BGPhd5O#6MRG6%NhZA<jTaGf3Zatz7XsEPg0?P5'
        b'{97;<0rYG5un+00-47NJja~p)84%>S90B+UJ(3C9A|w;XB`5j-w8(Iz+ZS1g#aQWgIF-tO_z5gP@W#-biTO{t#_#U%LyB<)&y`gx'
        b'_g5Ce;|6n_WW&@VmEPt1`~LK}h=HJOyqW7xjQ*bb4(3jnH=4OT-5ihRddOAoL=S3S<)OV%U~CezBvgVMI!1ChgApyDXQUYa@O511'
        b'Jx~v0qXHdg70>KLyn9=E1e2OuX70h!{B*9n@-?^W7cRg_(&ONfqZa7y<SLJ4B6Lpg<AAlX0bL3sIRBFIX3KRKk;$Llq89G=3p|ax'
        b'V2fB;idyReT1D{QJk+kC&dGHvxkpF>b+b2Zb+rtU<O-g%n90n};AvE30hEqa^KBq&1o3^_-K;;klQj;}Y(mV2*x+f2>f1IV-KF6o'
        b'2eAuY7_;2>b=$C)b8Y~J<5YhIG`AIb?lARqTRx^StYGaoRS)bZSA9W<T<Kmx@YYdAb)@D3^xvC-iQpyIN!Ob2d%ggTvkdh~Tj=5^'
        b'94o0SHn`A-X#9h=wBA~?5|Nf7As>UEwV0J*!B^wEckZlHqiujXk_4mg`Q8RNMniky_gi50)1dao(vY!IP|kU)t?!Zxs7i|eVN^qH'
        b'W-gk3CTgNZqI%smVU;*mnCyGFTuvld#3NbLA;|#RgK_i0+GiwZyy^96!N^AJTw(q92|8xxRex&J5Qy^?R{=L)QV^L>6vU~!+sqg`'
        b'Q7S2a!h9x*%R}IqoehY~&}Z^$q}bDD<{<}_)W<E(gFtXqbqeuiP}hRQ8h~=LF=j?r9un|CO+ds3HJIv6!LI-#<I)-F^eqz9Vo*1>'
        b'sZO`x%hKaio!Hm{9LB)nf6Kr#{h(gwLwYzJduPp(h4@mSy!3F)#S0bxVh*0Anp&(oE0sw-oXHuc@nXl;Ym>FJeJ+>J?NXd#oG-Km'
        b'Pe%(7=ksmg7ux*Rw)tw>%;AW$rVV0r)?~7oxPW}ZIovg{l_n2h0*L(t_c5U5DHhG(OW7-tCT}hO3nqliq<NMExJ0Ira#ckeS-h}>'
        b'i>jY+O}r#2`D@g~dI?e1R=$qQ<JiqW!b3r0J47?m>;=V!7PDf_7gd#tUtW_I;>POPzO63bHkYxFAsnv2;wSxRiXwg5f0XG+_$nYm'
        b'&J<o)T+vxR*>*FaSVNp?k)IUnJ`wo2s3Pnul8dS|Z4<1AUKCmji4jpyL*Z(W4(<$pDbSs`2$j_aT^jq_-GHruc0r;*qG>MY|E8jr'
        b'j~Tb1Gunf?mDWsni4Ra$SHy%{0w@3u{~j>*?KA)asFz!S7;k;6EBww_a!q=X)A7`7-@`87Bd*Cq3=!Sti)agw2n@YWLOM>z;OTKo'
        b'IEeu!!AXN_U+s_Vo~g*T0j?D?$<TEpz$46pD4;M<3)+Ab*H}Xc+n`Vp@_j@7&=QommVAj*SuL^Icjlb)R%<|r(t<t5%C5e9!2d4m'
        b'y%{=m?zWy0T9rWNHjNG%=cl!^EZ^x9xqSa>?eH)im!V8-JjPIp7I;@4QgP!jC1~+Yf%z)Nm*2Tx#^I<wYfYKU<VsgXsy}Ycd?J4x'
        b'F3519+5$xN_tyS&pa|0O#Zxq1SM_YAG`t3k%#s}BIp6l}wd&Cpv-f@)D{{1n+m@gsD-lZ6lJKyER<77_rnPRVz<0W}rfLOUjo@MU'
        b'Qp3otp0J9pmTe;6SgWBB=?OFI7t{Kvj^Ew%U8W7m%X-3q^k*g(>xWyx?1Ld?wFpf_Z40Z5#;wmfw#vh;Z)T#~x5#%KZLO%l40(wD'
        b'&DI_N)6&Bq2<xyjfQIn!$;;DVgaPTm!L@)n(8I2J`G}S8mYVfqYeLn-Gz?lFVbDi*JTYsKETp|0cv+=*A)sUZq1MEmDl=AOGR0T!'
        b'R0f99{9X~QMLK%s^M|bGHF|OWXJ)-bqmO{<)a%TZ<XF~cA&>>M2mt&agyrNGh=C@r;Um%qg$6EC0%){SQmqElDH0QxtGSq1y{EN$'
        b'Pn-Y|qkvpDl*32XgUgz9P}>Sgc5(KDT%I_R8?>6l!Q8{RtB}bH-%7LRCKIn2SIqk8mVq!l(zuIB*L<OJ(7x?0WSlr~2wqW|9Gt}k'
        b'BOfx=n<KSI`MLoP;Ie?#P5#ffx{E((&oP<LR>t-BaEwP7=sOzvE3Rmr2uPg2qEFc2HC|zOu=l9qmSI6r;*;v$VaZvKYC9b%Tm;R>'
        b';aO5DJsb-t(&08m3ORT0$dbd+a3U)s(V!Q96cNv#=#DI8*O4KF?OB1sJr96Ca+mP{u0!Ou8oV4ZGo&?egGljvW}8U0vX#hg1?wKX'
        b'AY4)ix((NGA<Mq^4*7Rds|Il1c=cAAN@>-^t2zZN|AyAKqm|GXiv_Gska<o1`CIA5+hDi`IB=*mc8V*&0Z+?Cj04}QQ)xV$iwTeK'
        b';Hr^;8rvp1CQB*dA;%UcP)k~iOK5yqi2~F;wg9>v^I}Ei66(nozht4QTU^vF_ZKe&glPPVk-j;H!{I_Z+GY}DFfK~p3oZcrmka<5'
        b's=0Gjx@a+Eb0zU>ik{$so|f{$xR?NdKKEA%Te=07w)~9=a8c?i{qAzMS2IzKU=InH0em_3{toCM?1ay!Yw69EXOWuxJ(L(SDI$T!'
        b'=UD}Q(g&n3<8zEO@Gl~a_I*La%ZJP1t^X51WX41x4yZ;HJ>N=YUjq~Y7I5V-o7DHwARS@~Z}>oJ&;n)P42dTXzBM=*nAT3+x!3cp'
        b'(@#DQM2sskGnsYpj4!=~`i6$Q?_=lg<JO%fkC;N~Q5$VoOIJO@Zo<F2AH2Zdsz;n>fpURdxrodB1&E(q<2<#$OXwT{YHS*9SmQhf'
        b'-`)mqi|MK~=SlcB1d1)DdiT2pI^hkP+~yHb1N+T}ZNWH+K16lWiKpj36P|lLUZ(!T{(S6UJaJ?{Ag#t>V!|1_E4Z@(R&(`%{Td9B'
        b'&T`ckokN>iO5#=OgZlwzHN+ztZZy7E^Y-l=e|^W#p;<bLFYDolMm|}h{*(qIpVKXtvm;M9_UpUp9&~`;p=QAHzF@YvX+M`M^z&Hj'
        b'`Lj$c9_(o2b6`}llo|d6v*TI|C=h1+DWl<`)Tooa1kc3~*5X_QXi^imCTA5-iV3+~mM(H7v3Sm?oF(KPGnKM_=$^GB8x{wkCe}&H'
        b'OQ=3495NoPMDupk4g(FUf)(dQVsPFBXJq7R1XiNh2YAW%iqB`kde)9wPBMybzVp3E5Acl-F>1s9%x8cOt9Cil-?|;E$bT?ame$b%'
        b'?brJN-Ei;GO@|H4sTniGAw)M$hciSsOYhLlxuBo(_4|W&u-1kCXVbwwUcyN)nL>$DXGqU~5Kw6(f}XwWV*;eT0Md$-C3jQd+SyKr'
        b'e0<fb;jLdAbOuchQjhKj$;nE%OX49`IUBNY;%VA^M$XPWr63g3m^LemxB{RFiP#EZnt@jRng*+NQ6#)%Ar5^BuIn3V^EihTq#)?U'
        b'yZLwhclgVG3_p&A{}_P3=Ev}f2q%pCqQrhwpHsXakeMh|82e4ig4jO*x$f{!Iisauje*i$!$9QlnZFDU)}H<udJcvQL1Marx)pPh'
        b'e=W2R=hQ)b9DY9#@>ZxPUXf%&-{1HvUjLxHzFzgc%j=!(UXjj4@B<kq`NU1Qt%CH;x_U_y$YSaqbaeZ{xOxxODt<aIy?6^OLuo3L'
        b'lB>NI(v^Su-`o3{3na^xCK8@L3KRQz#6MxxtVk|0W`U}1!yCPXNr?teL||RZLv`Wp!P<c28meyWUUi8lFycK>7u-91a9%27g7uIj'
        b'!Vm4^Pi~l|qW=x8dlj7wRRjit_6mtXM?)4Lj)DCS4gAvy)M&FnAkF7ce{uw4lVpqwh?nT#Wx5~vIH5XSs$R$4Miz1B6Em~S!%6^<'
        b'vN|1BQ>T)8+0jc&+O0sb?>__e`cECfm;umB2b?LT(?PdTU{b&%BA|AE4`ns>dL<IX=UziPC8loERTy1pQ0|@epXCHI-^J&XALY%I'
        b'*y}-?RljqAW<%PG16blMiLXgi^$vjQ0Q6Ncd6m_})lWH9olZZNV&+C2cCUQb%nB`?0_xWgd(aSoen5#s{Cgn&W-LX+jRLL6bH_Z!'
        b'W?m7=ML`orzGMbC9WnE|?i-d#2AN2gWUGL<Vwns15t=17JE*5zN!;*ch^c8dG4uY|Dd><NBg$M#lqz)rg>cR-Nc1eCqtU}2Aq-@*'
        b'igm(o%^ZPypUz@e?9KsUs^B^EPllJ4hFec(M-4A6JG^os^cA#M84dV&7k6Zaq2HOqQRsp8jz2-_XD)f#Z1}3290(al^D^@^-up5h'
        b'<Pq5}Kt1{_S3dtKtOvW9O+DgZIW7>ge&+Xzx$vr_Bj~~F$i*ZPj;5ERN!f|6W&TQpTZjfPu$PJw_w!0*XvX5No)UFtTfSzx9vb<c'
        b'A(RfB8#E8aBak?_k7D^QNT;!EIJEO@T(>m{-VbAXz0SVL5!F%`bZK0IYF8rH4Ublm=tw(qJ$;!f0;Wrc7X%+FBT)W>2vG)!c0`3#'
        b'rlWipQmH{LE=2W&6J&sfIMBbb)`Q^I#7s%00Ue={%9?kH6sH*#@EZ`^4P%Y9AeHnek?2%LB!DX05X)XRE*xq(fFx!<&IXaQw1CIu'
        b'm3~y)guqa8RwBl^GKoZ^?s#l!=t9lIsiZ$P*@_6x@)sgF4BR$iMG^w2<r9Wj1lU`o7ATpq`7qrMs*}YkVa+cA^`bd8lZ~E?THa;Y'
        b'NfuiLbG-y|p?ov+4!dfa6hYHa%Vxy#Yc_f&EX;?Y+kPDjG33L@YT8)Xky;aYjE;qE)4qVjcEZ>uCm7-z2Z`qM*CDFm=GZeVxR%&)'
        b'2=h-2@r8qoh=;*p)*vG~1WB>Nk*Gti52M;=5dZLJlY<N(c_{Ay$Z+ViE&$_KD@$PuEZ{M9B^#RWMPy|@47&CQhI-GT+U+2f8DLof'
        b'z^pK*_6!5oD|q{DWmOQ*l{;Ywm3<6xs9Ck$VJ6KW>xMa$|7V6Ip+Sap<{LoMi0Go_II|MAZDbDsrd-L6+b+O)vS9=28N$`<C-aC3'
        b'2cQM%iLaoU=bxg$1Xwu^5o~}#{6^{#HiF(r4MW(PJ1-FH*v!*Y(5dO~S^$h7lLNRDhX5)MgC&oDkRf~yD?DK${@?&|QfRbEZ+Ehl'
        b'4+z`?`c!a*RvmKiH^G>O;8m!-!4NGDGb&{5p$Vr$8DY835Y6C!0{K3%shR%-OyBEJYIK^L(4!_{bwKKX;SVO`r<Jnc1$Xcg2VP*v'
        b'I1{K&#0O;bA^;%be-1J#$Z4y{WWp>Tfbu&X)_{q^EEgE!S?~x~72+8<qz#u*{y4+G4Bmg^;G$_GTVQa``=+@fjBjLo87;Uwx!Zqs'
        b'91xdpWpiRC8Dil}9PL)X!Bd<6or7;{hCA4(;$_D20=qX|1`sc@mS{B$u>tg15wWJZvs76FO+?yZG)$1C*rA#SgOdR=g27dmz<^L%'
        b'hR`%CYv4jk$Xl#vjCJG{m^ZFj^{?h26>OP9Eh`}v;K@4w|BhraL`<`4D)g~#4%I#cKT2mtahc^ghWe_R6yTRi2&7phYNp95Vi^tB'
        b'Bpa$-&fqg<L6K^u!(<l2v}lz7d&Z)G@c!OxMvM3_F~oh%RzonVDH~@(v6BHk^5pD`B3z2|^5_DMh?AqMU(18;<pm9{hlp?YC2>o_'
        b'kSAvn_vfsfA%~f(B@+31lOD+V>m?QIP5r!{Fv<eE>r!^-;>lj7iyO2>TFaAb>%ma#=$phOU5buG06abh55xrBgeg&cDUNT$9i3_N'
        b'tu5Y4v9$H372V*zZy@Y3zlZaVgxb-}nr@ttjJ9)8Ay^-p_}cFnrGFbXa+4{2NNT*ng5CnN=`P;xTnxw?NY}x3WpO&H84YOJ%%h@2'
        b'*LqUKS$R!5gMmhdg|EM=kWhc7%gG7oSFj)5o(MObiV|9=b+E3+2wnHBBiTehtwfI)`cd$WdOX-ZCD|D0<goE#_#6Zo-2-(AWxC}W'
        b'^jt|Tg_&Y6A5Ncoat7xmM)8Q3=@Jsz(Lv{jZNpNrD;NCU6w14gwFs0Z-yGmR=Eu3z3$R!jnr;wfxDv=MaQ)$GgwQv96}q7nhq<Wx'
        b'VIFDr?QN*i4;?}!y=n={eiV{b4AwjHEv7_|fz|eUjeztfzNtX@yOGLOD4#~IKapA)hmLGU-dur>)FG9TDF1$hXrQZ5=nnPO*l~4#'
        b'@fg;_o!|qkAjhrTglZ2W*TJtHseI=Bj)PbI#eA=~HdZ4&yOem2mTwj(N>R%)WN#ndK51g4_6NBf6!A_^{_!ekSNDo4QNnXD7A79{'
        b'RG1YEv-!*qxX9F1?={tq=5M#PNc+<=W>GEN5)k;kksZ4kY5N19ihfwhx4)#fPt<<O8RG$v9i5;?gO}L?Slb0gn};AvX0g~|{%Qa_'
        b'R;GBK87)t#v8dtoQVxoTLmb}z;VF^SejB_iMM%Z8ymF9C#wrcP_>zp;<ghJ?1Dx3Gj%S&J7nQvJ)yWB<vn!v@hZ5P>-wueNN3#X<'
        b'sUltb9H{`MvIh7)ybi+;10vr;wDBU-XKeO8NKbyu@UsxaIQfHa*L+cjyyJIq-d%FI<RK7)e|$S~g@J(y5|?a)<rUAy0hXK7JMW99'
        b'6(2Hv>zaLWbjJsbB@#hYBu#o_({jZbE;W(4FP-F{+60?se406O5ulnpS<M_NgpH{|yzPMSGGzy!05~J^X&_=;*NE7y(|%O@5rd={'
        b'*qZ|0*u2fxK+ocZiY<(E`fE^&Y{~30PzR8u0e(Og=rA(U@+*LY$>YUGPyjF6xS5e=e+BXc2qc(C@iZfqO@medX|JCH^*CxDq+D-r'
        b'h4-Ym_eM@{Z$;o;IgInrH*Yz{#11c+MMwV5KyV$u1oi)um~H}?l4QZbbWkP0T`HUOr8QIkgw>2pF~lcLA%_~`FDy+AqIzSW`q6!4'
        b'<f0r>PCl_n3(sT{XHm;GhNY7TML8qwz6fxvK`}706-BesFd?3>We>{#Edyv#rYHsN{X57&qda8$bWJgWFS(Mn<^7+7vELjEa%3xX'
        b'%)w-kA*Ky6O<%2(Y~NurZ$KQ|XU!;Is{Ei~76mKT-afxK+V})${`(+ntN>KCefw-3kWbby!RW~VpNd!Iiek`b^N{o*EKbF9awrYg'
        b'csZaNtvZNw^yK4!xc>$+0SF*piU=<Nm6_UG>XJ}?CS&<IgXE*Jt73<9;_9`{Oss~#FSNH}Mmf?c9uTp7ZBBSwTOv0G7?7xHY684{'
        b'G~bM(VBPjP;77o9!53XWfP%iMTo{Pp`kI|cI1CG+I0`<Ym6>9Y;b0Z4&JIg-^swhPW*}2Q*L7qBP)E;d=kEI7Q`b6+ifZ$*O6*DX'
        b'@0?ZGXsh3Qh}zM_n#G>MPBrQqn+ypLH0tp1HP!Ga-|OzgfNoPUBBwSqv9_`J=m58(+eAIl6cnnJ7*`WtqH!rPoQp?=!f{^RBPp~x'
        b'w>W`%u{YmtYtOAx!UITlufVB9E75r3m(DZj!GqNHCbRN^#!>)p7pxwocI;y>8L^f<SE0D#T+ddc1l5pdl&rl0tViQ?qX|OsRp<lO'
        b'xz@=Z0V$Qst`Y?Rfc6%=JJFZr#2c+ZS);+|9pT_YhrG5SWr;J@8Ds4dUUf@s;dYzzr@^va(ZMs_6sMBcs^O~Qol5Rax{9ZM*m*TU'
        b'QVmy?<oHff*DX-;aDF(M#M?sR5J4sUl52?PY~^P1*kJSW2Y3K^eUwwl??JD$>t*bNRCdEHvU2mg8$4nw|FAo|fS-y{5A9<^aixlS'
        b'u#xKwn<2ZwBY_#B3ivtkaw_#+4j8wtAl)+06!=+tZG;rL8Y2|uFROSz#u4XJKY@j|lG^v#J5%2~lxPeY+^3jo#Iwxg8e9WpFH=(e'
        b'-E)px4jQb51<;iSLWMUuXB~d!+Ag7U&OukLHU8tyd0>ebx{?Hor-F;<s!=nB96Tep4sH{fjP(_!+L&D3)GhPyg*)#$!7Zqy0vRV{'
        b'?>oj#`4b+4FYp7#k&MwO=L?TudB8Z&>asIuFPU*<w0U%E&jQmQ>$UUDkxcsRg+~`S9;r`r)Q);g-Gkl(^*uuA4>x1Tn9-51VSIGU'
        b'Ri;P4Ua|x<e$^mJtCXM9Nh)4~CV4x~I;x>FiyTL-y+J+V0Q#^d9vK##nP`z%F(|tyA=W+Z)_?##b_)8{Gz++=`_Yj&r1#XIbzN_7'
        b'tw-_>CunUAV`E9H!-5sFwdU`!H}of`E7J;qUYYSoxLK*fBaiiS9z|2R)?KQ~Cb=9-vx?>HE#!*zgGsyEUFX(IND-zHqSeNUN=c!n'
        b'x(=w8Q8@_d(<G+kkYbHY3`;%8mWq>;<>Iv>=(I22rF(l8h)8g(Tn-?|xdnjw()#7+_DXtL^TQL?zGerc<-LWVJ!g8jW4wvaC01br'
        b'9c#5sTQ3OEj~<Bt?K_r<pF26IEC7vT&x_q2o$Xf89-Bh04olKT<zHjx)=0`EgX;zXx=rZW^*}<0amY#x3z3((>53GDpOcp6OiROX'
        b'{uUs5Jc<<m#<7iCqd+FgB%NW0qoE?!*$`NWly_ecp&y+@NAeNBh<oe=YSAK98vy(sp-tsc59`s(dLG1tk8BfJRc`eeVyakLy{L27'
        b'7t<*J5o9oT@LaCsZ0<y^<ibLv&>!&jo;ZOoMwaCu>wV+l=hn;1!U344xG@0G>0>Ydrf_v336Q^AZdL-=UV&qNR^xrW@aKLEIs8zO'
        b'vSA`il1+kgB#NGq$U$%90UW+8{(*3G!OJ+xhN<EtemaKC5#&N7pOejyKR+`OFHt}2z@^FY;j1*7*V7+Ipa;^J^_B_7kG>P|GJegO'
        b'W3u$|2M#`ZwL^j*EI-l1-Ea!^|Mhxrx5@jd$#GoXBN*esW<yBE&zU*UR=3)!idi2+T7YhfOLw;EzW7S}WssKTMYU>~gNTM(K325o'
        b'K@;gaB41%j=ORj_G=RAUx~&+k6!?Yw!z&)8g<%<48Qxb0S&Kn<%apyR1GhcOsU?kOWyHZMJO+u(K~DP8<Be%2#iLK>49>H$YnENL'
        b'x^?b(91YS}@vUa{jb>=V{{d>nl06z<ZJ|dag!jbU(Wknq1eMZ<`>p<P{^1Aj4}^#1J)-m;8ccgl4q*xr>c(COEV@MTQQikQ!o4`a'
        b'hj7q4a5`_?vHhnmH(&Kj+=4-~#LH4}x7GLeW_CvpfJ(EP{DL!p*%a~StyxE+&j?S`%f@ZP3((Wqi!UtT9)5JuAYcdHT2On)8wa4|'
        b'tXsQhMs9}cKie$tt?d+0?=;gsxE*-H+HN%q01wJ}U+&&@@XIMt<$ba_`{hOG7nu<=i?|Ix!zVfigUx{Tb++rOZ-wUEv1aI7x-I%A'
        b'6DuU0g2eWSPHW@EfCy>ao89dfak@PYM=fZb@^-55E>AtuJjSyMa(ZjoAQ|kvL5=U3JR17zNqi93_-f#DDtmSTIvKoJo&!0a&7-gE'
        b'IM}RyaW9$pVM+WZ`3mud$csQ|D|#Z0EJjE*YVaaq#tN!oudlUvfKMtnc3dX$m@!cgya6Ju#;onqXv}RV>YL;q@y)FPnK)H=_-RRh'
        b'@^IoOrymgxCtkuMj-BG93IVIZmy$r#mgXQyKIm~8mmjRB)tmw77CEM}s90T5QLE$qK)leLzIl@pl}23i`<@*E@}&Nm=Hm5x$%Jl='
        b'q5@!;7iq-NoK<N_oFqxu=Etduy}oVDKy;{4Zk!w^y=UbCFW}V^VaO?&yZy+=JCg$m{$m*lfrMA;9+B^~<1yQxiF#gwMC2eZ_|obC'
        b'9@|gVzZf1+BLEX25<}*w)i7R5{5(<GoNlZjNyP7~k)~gPt`UyHwNU@_W-{SrfC=%yUJa?wi`*T;htzX&wqw#IeCm<CzI=#N3FxrD'
        b'-NT88NDHy?_EWd;Xb8XG2POxe(!09_^xN|iJS^CA34Yjf39o>DYYKZ&uzfpLqecMY`1W1k33k|mduYBrM=ady_dSzt&=V=mN>pcn'
        b'_M-a4=3)Wpvd;mQq{5Kcf?7<B#*1i*5sey^$EAViFvEIEvezeX29yu_PVrYV;N<{R!O()fv%A|*74+MO@TS3c#aE8(Oumrt$wwJ+'
        b'7ZNVjJ-Q5E1{abSVfSsnRNouG0&30$*nuxDfL)j?C)8lw&;@=V1fUBIO4RSG)m`|?^2^XYmXtMkIJ9iQ_rj~(oaU4@0~|`$2oL_Q'
        b'*qyicT`4DS?W3zUl2zrz&3$Cmlk9IPaRdBrV1LVqdGPxSK#;h=K@Q?e<+l3NyM9Mg_Tn;12kUFx<@|h~RXAGJC4}>=N$7U#Y)qGX'
        b'guU}>MQL9Rj<#hkBz?~`1aR8-EFk`d<1y?Vtq=F%D6M=Zap_fB+0B~!vxgAWxqY<qh_ve#t^7O`U)>B!M?9RE8E*E~G(^Zk_kDb|'
        b'4H3y^-?K0dd54`OH)#b3;Rg>D)L-_Ql`oq}F+71Geh-rL@FMyF@L-_&!M6|jtW5=swwwyL9<%T-aX}lsjA*f&S8>ebS|C%IR{`<6'
        b'-9*8de%3TwWE0BXD?rIr9KvRYdF(KtTrlA!Ho<bIPy;sd?HxT~_*?vV4~j=L9OvNh&U8bToc1F0Dvq<xPJhgyg-5SjBTS}RM3Cb!'
        b'IfH;%Uo2;*aKZKLFMwKpC$5dUb>9FG(%E}n7@{iLo6bETeGSO#S)43MdNG!+7O718z??C}b(fG86}jSy^<s?yyne1BH<cJFN=U<<'
        b'#7&yGXG#o)(SK;-j_B4cAWZupaZ3UJdJolLX6feJnztE1W%>%cZ`(fTN!v}9By0o(49$Vq5TvK3tJ+V!>b7?#JAQ*1)Eq;ce@pfX'
        b'L)<HeA5O)kezF2mvBd|imPMvlTO2J>el_BeRPASv;bEB2@Z3u5WuTP;HaNgBsF99;GP>zoor(dD@d~p|q)P_R`1s+>ca3@yD7^<S'
        b'nj=c_r6#+0fNwh9VvZ;SY{k?q_HM1;DuIiwRT2BoE$)|b=~f9;_7Kf`Tn$z!#b&~DK~sE>?i;}LDRyHc;IW`BESm*9Bb(=L$74Vz'
        b'L44o!N#DV?;00EDv7)iaD!w^oAPr9mw&0Of$rs{2`RL*B-i`7=+@&oiQB$crKyE53!g^1MOVk1!#~1fLSzn?S?(GB96t=BV+r=Qe'
        b'Zw#JHs{ot`2h-H}_c?fi0?+vmv9x`4g(PQ{ya(-z*q6#Xw?`tK<mb2t&v_(;9(b$hz_9Sda3QC}^9%VwQ(FgbP%#K-D3~LBw9s>Q'
        b'7~~o*MB5LPF4ZXz|5nbwmEL`=q-<jjyCxU1zTox-yeCdrHPJ|+MpKHA@b(ADQ^+9;QD~PzA^3e;IafDHCM<HB{!?t)zfrT}b`!jG'
        b'_eCVCZAT_&89J==Q(k+wKd*F*+k*{oJHBHyVP%CNq0Fj3_nhRMTVg63tf+$`=eatG?^2U}eRUm>Iw$HR<tKI(4j*_b;Cia})Dy=g'
        b'(of|5@zNLKabAs=iOCIMr|V+inS`kT3Vn7cEanuNYP?9m%Z9f+eJmE$?m^TaHYG%&>JOSs9@thp+tw2W%g?<jsW>@!?xdvp<ixv@'
        b'vlrj>ygPdKY<qh_>N|u-g=5FnKu?hti2Nve_;qw70ijWD-f`3tkMyf^25Tn{Ncwu4+7FZ;AAamiKj+Ae@g(o);NW0w(FDBddvMv+'
        b'b_xE6ZVw**#b40C+3P1f?Vq|iHa#8=^$H<k)yF;`vpz2?*R7uDk~n|g)a~(mCqRA~B&-v@PGN7iyi3^E*(8lez^|V`&3Zny*$!RR'
        b'ACfChUL6p15>$nqy~a+XJZV|DALRp7`O5*SVF1+;B?7ybZFb*FO~IBQ*mWFW{~tJSpQzpb|AlkRJ)HBh*4(Ysw>?y8`+r4!S5sqD'
        b'-}3--F2wwy5au06A?7Md6~sKI&Mk?_&C5b9uQ2BlBo*Y~IZ~o3Z>l!HyH=aXgiNw>`8g##3I-qS?Ac{Ksmvs+mgh_GNU+++wJf^|'
        b')CtA^0AedI`alk;t$eDu2OC=m=xr3x+eS!l8{t_;%=(e-OiZ1&4$gP)|6Vv6Te$k%xH<Nv?%dtC2YAozT~Ii7ITzVAdU*{JzCJt`'
        b'57Yi8w2yLCBT1{3pUabM-veieUe&Y<PLdLD|I4U7p`0wCkxE{~`JdQuo<DVCNePhez?@HPmu_d3l3kEK3$-NH53~moMnFm3*dz3C'
        b'K9-E3K#FF!$Hyg7(Jiw~{KeEIzqh~K(rxueBQf3nQp7UDKt1g<fvrqZa{rS}D2^uXM=g1Xo@|1VIP;({xshC?gkO4frzEXTelAh6'
        b'o$WDaSko?Y;)3Mj$L?j)cNY8a-$*YwA<bSa6)py95x%I4lSG7j$on?}Np?)wBe3o8s6H<KQvHJ-Vud1e`c#p1N6#X+YP@(#eaaAs'
        b'5P$KN>I~6IPMneqU2QyZYIu3tX`taPM*_=LhfhM?Iw+y{bG&~XgksEJT6+H|$77^P$g%boTqr+Y-*x~Vg0{7zmUM&$6>defX$XD)'
        b'lj9N?y}3tV)`vl-VGc}wTrx!4K$f6!3tb|%?vPds;V1-qwRY%ljeu3`+P!;Lv*F3g=#9EpuylUuh88S*eTlXdu8k%9GX4o>bW;hx'
        b'oZrvD_l^8F!T$h?o$HYUP_&*KY;i{_Ij5gej~BaD)*afvfjsH_vJEZAVO3??E6nKU>HP8yEnV=voV_@e&fmD9#RK0rYX8CPo*{F='
        b'u#bEO<%Ml%iBwD+ZY<h}?F1{je0>@eGuQi+7CC{**UP01i>wVwequDL%|?_XQVpQi9)2)HmVJS>VW%Z4VfzjYHg0Di3_bU(#K6aj'
        b'8rW@!ljT;uvyr_dIqaP{dj?;+dwv{;*T|0hdQYUCJ1O>;KIt#rXcZjC6O_D!%*R1TNTWE^POBygF^{8kv>*p`XQ@E*)};C9tp+SY'
        b'^VST0Ca+)A!!>?QfaOzq;${$7c`4ij&;=Bka80UFJUhp~0>szWyvPL_Z(Cku47*eTX-uWJ;)--25O8IzWxWinU8*Oo!4wE>l}tO!'
        b'>}(r>b}al)*uA=SRvagnZ#*6GGxPE%@nxyFDYb=OUMe@$rs9s&7XR`MatC<yrnbnvwdC?L`B=-KycS-l=#;}-i|umgNH|Hp?CQ&C'
        b'4;r*)gLBm^DU+m?%Fn$dDPq^Na;tMS+h1in7mscT*<jG#6OR3+8V@2pecP<(dWgyE%!`;+<tD<aKe-vdmgnKPIc5*iaBR$(Y~9{l'
        b'YfjqO!vi@L;iOdsgPgGXZIehR5&)h8Z9YL|HV$>4wdOQqR&E4EiaO-5fZ*Q?jPBAk+=4Mg5X8O9;S%S0zUf=mc!txNeD**fDeYMH'
        b'eRPuQa8`6LJCO!NJp!v_j1P~E%5UNkBY$H80xVdw5hcw8*K(cdOb*0@g3IW5P;klrEqL}C+&sKnZt^w(%8gtP>C7_?pnqv)DU7wn'
        b'AK<c@@Q?08tEb_2bNq%zD;@z>us{pza&N<rHh+WlOf>WWF}-XIOY5!OJ=3@qu;Y+c9sE8Xg!2m=^1Ph4<%vtN|Adu~rehop#>-h@'
        b'8eN6+QhCd+=BKMZ+FQU?Jj6)P-tI&{`{&*ZBHplwgNJw2LAQmwZW*&+tRLB}{B&GYuqt2E#VvRuA2nmV!_nc^2t39Xr{FUFT!9(m'
        b'G>$7tJUnRy;7OAlm{w5FMtouMJGs{?kah|>QMdK*Qq=MQ5YWYVjN5G5i}hO598L_*F{{sEm9xtpU?H>+9s1MW_5*kfv@$yBgNtL='
        b';JI#i@n-_i=@FAZIrDJ1<g<nbKNq=he}z=WJNHMq|JM~EdBg_q+clcZ%H<8=65nqd%yAq#S)UM{;W#M|RO>rQ{BmOZ&qyvp)iub|'
        b'FfzJ*_m`oNVWsUI?|#qr+wS?^?zD5=Vkp<{p6l&TbDR{zfCyH%F7rF>Hw=PbIGlcd@+jdo%}T8|otqm#g@L7|jeZ#NtgMs|1JeYp'
        b'z<NnBSynnS#qNL9!Tzw`=?`tf|9^jwLiBDI3{~y5!?5Ye%e#+&{)vG7Lndb?hKtYV!rmZL4W~qM&>7nd!Ok$*Ou^nDmCF;uB~*4p'
        b'I+sH#H%Xu1$U$#ZZR$7$+RHXp4jTI{v-`W=*V5!C#X#u+O|@QwuE?Ry_u9Rg+{PBD`h;u-Rjc=!<DQX5Gk_hLThvnP?byhS2yx<T'
        b's5TL)G{990|2%`ffTM6LBU}j<Xmx6XFMF>%AXkhM>G5}!87=}S?IO?GF17MHlcB;<Y>pF{nlZDQGwC7lrGR<Drhe?BL=Doj_;7S7'
        b'9zJ+hJb1hXC?J98vfgenzTA7D#Ut@^5L#Iwoep=rET^j~tSzjr19y$W$pjRhz`=;=u`4nn1nK@SGa_Kv>K`MBHTWX-4xox*h~Jp#'
        b'9(vPoFUXB`CX4&z#wg}gp>N89M+cHChB*kt&F$;8$#soL(BP`qDmGWM(1Ye0&>tcUYKU~k4RAW7jBfr$I9Z7{j~rnF%8K3rac@_P'
        b'yB?@#KuPmRM#h-k^XD$6IbIgS=-cc(YOJBYx4Q+S!X!cCGt{(QDHuhw1k?|9Qh?|#a7ZtQ%txqyS%|Og>B^t@uG!NK2=Serton)3'
        b'@qLI_+~EU-D|AmFAwHl{ePA!(cFf)m@_~QYLwq1ckrCtrlXJHp6`iu@Yj7E010{FaK;s!}g!hEpyou8>d^^Yo4hpR4O47C>=^5B>'
        b'iXo7U71YB}(UadXmd}IdR_E+NpT2%M71aQ3K2Z_{9ZU|N54Std+DFM$;gKnOJTwIvJ}=L#SAKkOrU#{jFmHJG;g*GC+yM-hegLL4'
        b'W-BiM3Ju<&hpCJOq%QAX!&CR$55EyfHNy9&M5EoiX9nd+66A?bar8&+fM-{{DW^6y1dW*}1AH(-)8!44upS=egYQxjEA^KsBCjmQ'
        b'p?{n*tmF_<#w|fpV)@EpHrf!D6vqZz0bHU7a(Nzt^YO)AT??CiOZ$lBdnN>#&)VIqTI_34C3n=1-@s+mB!tq%RdO5CReSAOWS`aE'
        b'gHiJkXB=9f2k-Ot)!RW2Tw_zCan!4XAz4FX3ip~|yLVVvm#M!^D#s&|vV-N;qQrA{HjZ%?7<nXRCNYvv)Y_F`t?t3tVD-9eMzzhZ'
        b'eD7cY0O*BPfF+gf-H$A6<hfg*d*_%`u4U#9KR4Lf7}Xwu6^IAcs(b#MeFzYAE;9$qtGahQX|Izm%+bOKveKM{U<AP(#da_gwjYyI'
        b'!?12$H@4$(J06|XR&cl^FJ(uOoeV>ui&-Fn$63gPbucdb<94!gUE@E9wE*eHnlau0#)d!*DJg5=e$EJc+kPe75_7`d+$NGH!w7-Y'
        b'*APk%mwEyI?|wDB+b=>=erS^k2f}*z)IVV=CA0wLmaG(#%5|DbQHeI?`48(N7P4Vg>ty^Mj`7I_T_b(Tc2LcJSm2U<M}i$s0+>2j'
        b'Oo?Uoofj^h-g-fMf$1Y)w!LiI%5U$8wc`cQ%J~|T8U_t`*NU|7Fn4^rVAMZf3VNnSlSBk=H+xYUO=%D=QeMz$7z%A*k1DkYk|YY*'
        b'i1tHIM$&L>2)Fm()SD2B73~w)-JN5iPT@N-UEzK~ivKa8Ux?99bN!DAtm8HmOh}X#q%7HrN<Y8t?sN;K&)-fBzdQe?EcbkB_n?!P'
        b'm_}K8VM>U^Lg@iAj3klX*UWwr{ggk(D?F+AOw=gaed3Pqn*Z~?<Me;|{;s@}Ogm{-y!Yd8L!a0JUIv#Lhehg-ZK<NJc&RK*HEvUK'
        b'Z<Y`r*>>LmMA;4d$;!QS28{2AHg>jL5}iM98#-_Eod?BhsgJE}XHkEEIXk(#Z%|_}pEaHswpsJtHF%-JI-K-i0ctZ-Bk&8ppew4A'
        b'JGNk80rj@+j?JZ+MCikaY0n#=V*vHwXq!OzSa-+M1Rj0YpHL4<^xIB<2Y=~gB+ZtVD3HmM;u6p(>UCRRz(%}oGugzwuZiVWdBcG)'
        b'IJWRwY}%eT0*8^_e(~@jpvs&+aK&-Lm6q+wc;s_7tfi#gY7>R-E3tl7wh&gdyR!?u=lg?{nU%QCiulP8IfE4I_-IvU4OMsNb!v2{'
        b'pIk~kV+nbA2IbE9J6C`XrmA7j?4GmTkty9zq#I<Hgy(IxA)BqwZu8k~R0Hfq>!#7p^H$r?9$R07&GG}2|H|m0^A_8X$=3Ih4WQ_7'
        b'U2g0;UvC@QZR@MI0b#+k=W=7`dCE3aXX~SEK;-FsCdUqwerp?g#@6>+8&K)!vva%Wzz~F6O>;RZ!k}x|h7;lE>uf{Sw!S)>_J0{`'
        b'%V_`kXKh23w!UX=+E0L#_12MbTe|f<sS-0A!T{d@JbH45@sqN^u-G`mq?5AF*KU@dueJ@9+4`z&+W%o-)Jw@rtanAOF8gLM7UFKr'
        b'NEU(so+^T0x@vUEH-HZ1&50jfm;ZT=DGH$aq-`kQ*0<4S8DI{s(-@ZKe`oeGdHu5U8*D=wTi*to_83FW?_n!ms++$B7|y|5jUh%8'
        b'C;l*=bH2znlxgexxoxC}LCl62&}#=bYYefPIEnd{+j;$x^M$sdG+SSR&C<cB7rz9=D)@bwCN3iLnY`B`&ga^Ol(xQAHfXAEHZ0@+'
        b'03@(1a~6$rv;66X@L?|w9rq5eq<(-X;G^tY8g-3DXgD8UBcW#COHgHC<IJ0bMBK1Ka{hkX(EV_h`6M=KAv?zD;OA9Y`1xcAIN;*|'
        b'1urxot;2xFm>jN4Wod2dgTnKqZHTn>#o2tQjbb26LRQ4tSEQL-xDc0_y6VMtj&EX*cZE1DQ=T<^@4T+GCZAjK*Et;B@L)>Oq2cgu'
        b'DiY4K<;l=WA%3uk90t>MAxr|2tbD!Mn>$#PJE+-&g#4nofk39Tl}Sp^Cq9hw^APv*<%x;MQA;i|`cMyVM2(z!%gs&YwY6sUN4n$M'
        b'540Ui-M$=DyXja)!uF&=_X_aXdu*_CXbe4ZoO%Ivj&&%xE*Vg^eElH*8zz<K#@bqc(jVoHhoz;*G8Sz249b&WDfff?Z<*~U2Ybm)'
        b'R!%2S_8K0_aF;udUA}Uo?V(hM`Lc-~oRf_YeJ!*R9@SXb0Doc;VkO)v-8{c@NUj`g@9r9EuS;Iff1e?f1&I$!&W~A#-m?b0Py2eU'
        b'R1fUOsdB3%{C+#Ri=1e?JaHNP4JvmzP7lhz*#z)VcDH{6p2i<k%C=(fM12`Q0QWFnl`S|wU>zC)6+H)U&>>RMzu>s}j~)r00}mk@'
        b'y-*W}1<B=kUx9k-kTJmIJ97$M1r(0$T#+Y>sG{<u3#w*{?5>Jx*Op9Fa|AIAS8eSx5Lm^l^2whNkF~dDJmsw$#Mjb8;wf%t-^UUU'
        b'=T_Jl8erX->yoifHRXqd<kau+zMAIf7F($<^{Jf|t~dOL5pNeXv^>_Hl+!WjJ?pAC;X1Z*S>HA*kkI>Dz^{BuJAe0dP-5`JRd^(Y'
        b'1vzgFnh9aW$u!eRv2Nq{a$Q^k?-Mf-T~XvRt>0uO@XK+?V{=wtXJ47b#@WSu${RyFK4o<F8zd2J^$m!Mh6l?#DHR;%>O<@v60~(N'
        b'xqzl@)*}_y<@iE&4-B3Bnz`$H=X{NIsKzS(EEMB&@+R|PA+p@A6L8E&Z#T#UKyHV=%EZLo*bsWe{0ig$tDwOZ)n~MlUX*$tf+Sam'
        b'!be;nV=8hbF`o|o!uqu+=TkX^X#AdOmEAtS(ds?)#!#}=zZ&_PbMAfc2|8=J#<Z5-^v1uD?ng7|Fr_4EF&x))KPQ7e;`O?^7W2Oh'
        b'-X-Zo@%pDwGFg@-NgontamH)rqNcDhQQ)lDf3|9J6trseL=QLcSF8ge@W_zdNN`H@OG-%D6ju6Djb3WdN1Klx+3-_z<a?wlYQw|m'
        b'$Tg&7xT-`i0TS!#njyKLkUY;RlicFN4j$ldrM5a1r<t0w>zYJcmW1I;yjxmy+Uzn($xwV52VXQ51q$G6LDof+Z!@5dB`@<!&aU&e'
        b'wG?e>sVEbd=p&m%x`#3hM~`fgEh=?ZQ5D9)ieIWK)(;l_k~d+LRM*C=-x*d^giWlMJkKr9&Bt(ML8N9#T)nwUTkhH#hx5()sI4n@'
        b'&(Zp&>ToN*rWDJM+WXq>`7*smA7<9abYyVNL`(@037`uN`iQQfwSp4;;@#J2y|@Pyj+va1mk{C_Qr5k`L@&k*N`_KAk}}SC-3$R}'
        b'8{p59^<+QusR&eb(5^XpBySnYKZ@X(W|fq`7{Q}7`Y3p7x^rlNH|)hgofq^nMH;tjsI!lnfOFZaODpRGr7sY&4~=1(!$`&EH*zY)'
        b'nhqqdbs^~f{1v6fqTI{);+zla&z-|Atdi!hkme>1aKR)6)fsm(ps+NXqnt4ny5z~O#3)qjK!~tCK!~6TX=9frQe;YY<&c}mGUUTd'
        b'k_4~WuH92m&wdHP1^hjL>B2p<7{x#21|TUAG2_n}2yu1y;Q^FC#uyGGMXon0JYs(bf@|?5a1(|=wn_{`%B>ta)DMsSFoxpc#?D|z'
        b'=*s`K(^oaLWeLh3U^)X;efXNdP+Eta+Z6zf>+BO(a*UtKE7qq0FlHj6y1PnG6N|TQs@l=DV(T-zua~VdKOv%5E!jHsBG!a$<E;&|'
        b'8~~II_;J{P5F#22$E|B9rqWM@!*Lv!gE<b84!@ZNR(N_y>EQ$j@$-`LT>!Te*CB2o8x4B?_dyJ4LMEM_XGsgXs)Z4iq*Z-DfUBr|'
        b'!_g+zy@Sz21mJLO4`VTvfHG(zy1&oybQ(=8X|pJ+xS-uz)sJo6TI?qj1|l9*K0G9z;3I71t=0cq)u+2CSj&GATPqj=8o2)ua@dpY'
        b'CnAu#xLxfI$1JUnaAr36G8-H&82G!bRiHmmUy&>4PcjLZ69CR>cWueCR@6xf^C0;cUPZQme*cu&UV+tk1qS_MFj6&oPR&qsjUEBm'
        b'j6e6IaRBImrWu<dWq<~b{EgvnWSp{wirTccFj+z}%Kw<j+2yKeceNdZ(F)bO>vOd7k@uM0vz7}C(zF1clvfH+?QfX8baZ4JV;;Y$'
        b'{T1A&Czeie$0PGs8;GcnxnD+VHlYbpbYwO2?Sl<{4>kB6Y8XB=)^P?0i~{a(LEZ!H9=6t&Z8p3e4KMW`mrKhL|Iync3xiUrz(lDV'
        b'-dJIdLp~!L%zB<R^1PzKrZ*3XZ4xT3;g-n88RG-34NX!{zR4_a-#s3)zCrl<j}|V#S7*G)<)h4up7R6e(-5mxyw2S5L8<-^94321'
        b'I9P&$ua!k125$AotncWRH=ckHq4+n?NH5;}k2SKuSLWP?YT}W`)#NJ-xgJqkcFbFnHjxQJa#L8}Hx?*HvI=<jy1uV0Jv?d-zI0LD'
        b't1D&e%seFJa$@vHO&Gqk?{iC!z%yjlhg09M>R4aj|6010K(zS^zJ4uo4@qTMWpW0{h^O?RU-nTR=qJ@ZG}U)S7Vf$9!*UJ(bAXkS'
        b'sw8{*E?UM=0L@X)+H3q^xx~bHrp+Uh49P>JhA=ZB+8+N#NflB_{(AdG7g&nOx1t-C$*8w26`x9mS}gL*aud7g@D&c`MNw-u7Vth$'
        b')FG$F%uquhg!m%wT)mZ=qV5dOUo7YUYysl~<G=H_s>_Ne55j`oh_3oyX6_Q*_>J9Pq=qfK`m59M(kamI!Q2e53=BnY)pzKbZ6ZGr'
        b'1zm210aczSeU67GRhTdv1>}3UZ9DD@42h3(ZizmYe9apR3MEx$y-;Cbtj;U#;iVgrqb6RGxT%sMvHhh|f%%==_Dah%gY>IGy`a*U'
        b'MYv3A`+t0Wdt6gjw(!ZxlW?>NkBESJ5(osuP6%xUrrv=_5wvz7)d<XVhJYYYts%TIl$@Xt)ZPnd6{wv_qN%{hNMcpgGLr<QXki9W'
        b'>!Z>t7K>Ip79aHm=iB=PP<!w1`v-FNW9_xqUVA<EW9^A{w`o2wA&EdG^_|y_hp<ILuT<2fb^%g~QzU3ip<;+r$oII=M{opM)&LB{'
        b'+{TDCZ(x#onb7MdJA_)rNQy~Mw*Y&SXM7S9b3ew|YLAIYH=iNpCl|yl&m1x`%s>^YkW2il_xb&F%pIWJWU?s9Mw9Z^BiDZHa#PG|'
        b'JG@j6@0Y~Ng#5mx?R3_BAmJF=u}81fG{4d5busYrHy4gBI=VPiJ#3c_L(9@E<n_-w{?ALv#McBEl8ecDA@6d@WrJSD8;F2rDR7p3'
        b'&8JA`LZ)pY_e@)PoBf9o`<W4Yo4ungQ#*F`2fJf+b!TjAU@NVbanoy<)s9-y$*-SK@hJf=rDt;vVcc~`-%@AWla!eon0@i>%<5SP'
        b'QrcZVw@Tj~vzzVK034@#jb*!=-xvv)wd|Mqn(jA;0^FSe+%8TTZM-|O9j%Scx=9*hx3@v4+8;ETvqv&t0TA4(>PqmkZlF!a16~;l'
        b'W;X<2)}zGT3VX*fUV2I97b`|Q(fU`b(|_XE{e+kQb=#rcOWr8sC(`;kzz(`YDsMe8oGp(lH`Jar+ye-LANN=nNMs~nHV}kz71GZE'
        b'q!!1JJ@-j4Uwgiz<||F4S}5Xc^!!4RN+PN+?qXmJkt#&53SGo#XWCR@qlLIl7<Rn5C1U@v61}kwTj^`K1nfkoaN!tz!VQdHUrvMS'
        b'RZBE57=z8iK;j;B1dXeu*5Bw`fF5|YV>K9V5ttDxS{155vnpVuw{!@o1YsoJFE!oVqU+-s`*_MeH(lFK!B+l}*Fpv#Z*e@{V(Qvr'
        b'+xrf24BCJ<=0IKC$Qlzgr~<cTyO(_GPRURE=lqxx_NyoO0Q~V505T-6Hcc-K6$vH!v{&@PH$`c)Ynw&F5WP?&O5@dD773Twz6yh-'
        b'4IyoM)e?~~fcR!h$gL=DlW%HhZgko5OUG}X@rzr8IaQH*)tgRLh*K5nR7twrs!ss^F`?M3qs=Jm&tSrbn1xHyJNcj$(Et9~Pfoz-'
        b'a>7@4`OXnMc_#Q=;2vk+$B${Vi-6{9<F}a&X`RRQ0IKioNUmNb(fhvA=nLqqZ|0?h>Qy0z=A7u#<&r$ms!bJWXzRQ@cE%h!8z5;@'
        b'i2&I^@5Y6JfJl3yK@ab??W~E0!G`ogNzHM10q5>Mi=h00-bAbMMOo)blVuCQY=0wsSJ!@yA2VzRy}mlkzkCtC=F&b3;5?#QG_DFG'
        b'ehVi{6jvsU1lR-6<HE4i(5N(pP$Cn)sYsg*D5(%GxvSe5)qMBKPMI(yBu_`$0a2sL)V2}fqU7yc%9aD_Vr)N&jtpq>&5ahRLKUh='
        b'zc|p%aaG8Y*}|$V8`#<hpR(hj6E6%gw(abEb!%IC8y|Qqw%JJUeA_p4`w3ddaU38G=nAkKQiTBoT{ImMhJl85mD9fZNg4fv-!R}a'
        b'W5>>;OAf_1kr<b?k9;n}%IZT149c(I#SDzw!voEE0Z&UUv10}ua5;%4S_nVympe@LIXfkOdZGB44aCotazlMTTHe|2MzEns-+mnP'
        b'#6-q`z3@)Myt|<#JvXP$RrHFa(w+A1%og-C?UBcr*F{DbH|r7E*Cr7y_F!SYi)Az{bSnO4C%pn)xbTRm#2oA^*&6&?{$Sh|N8A>h'
        b'@h>LE76OIbEy>FXxEPU_;hv2Ljo{h#UQbDA`VCjCMYxbKXNw~eR5169lYLwJ4g)}4bn(SW*Dl(FRK}x-G0%(iT*?rD?>+s8+;tfd'
        b'<V}bU9-t2J^}xWOuKVEdZjJWGm8^F5N9@u;U?Uy%5_DD{eT_eeZ*kzDk+Y`nHWOE%j_fQhZ^KyoPiO}Hwm5u2);V}g&lZ3j-I-$!'
        b'pzV*$aEg3~!nl_&U+7$;8@4}+P!DGsTkM^V{#k7YYlWBiM4=9fVZK4w;@KH+*#I&d9UW~2Knh=O>ik=iqcvcl#D27y*Gn5_LZhTs'
        b'IC`5j2>YUy>mIkWApwKj-3KQ&JDzN|8Go+62$!c4=`DG=0mhaQ0Ik&%bPd`!0W@IWwxht?aPm@tNW^Ak{S2M9CoK_hO<VjvYVd50'
        b'NHf%Wf-y0{BRz>$aWG!$+4ydG`37_)cfH(TEs2T~Zqc;_;1ZtEEDa$DI~<(WSZpP*U7-rkdJJG1tXIx7^yD<v51o8g!Ppf^0}arD'
        b')nxgFR7Nurh{OOeF6w>upk?FZVp@ZdrgwNfc{0Xqsc!;ObLh)w{VdGA*4kvs`eD*wZ8Y`W8g}dFP~h*8?j?dyU{F>6L{6;@)660y'
        b'<{aKnp9=1ZxYi*=zA0-HJeR+<DK2T%NK%{~W2V-p5{;hAqTbN{QU+ucMG4@LUjX`A=_>$qOIc2xX}kf1!yCw8)n-S_X46_g)?Pvd'
        b'M|(w?dab=-?_^zeW_k9qBTU7~M@iY4fV))KN`=E`jGjun1YB2WJp(Ob`DXGx?)K&SGpm#dycQMEHbl{8Y7NwAkm?RH&6k<>Hd=Zf'
        b'Zi?Sr>o8{HEdjYI<7ZN0JuC$*lGfOkh%P4fc2+WqRX_3^qqj!1Ca2PJ`7@|zod>8J9LnX~6wtB0q7|vBL`sB0<(8vLPujU+b@S>}'
        b'&*WXYBm*zqAk{vo4M>e({gYItv2&Ihh-F7USkaiCW7q!DWU8KxAdSQ?O^n9+k|qT<*9@0kn)t1>6<<&Frpa3Cu>5P%J-gBREV`Xt'
        b'cNz!Q&ge4K;Hcm>n$jQHcmJ;IcCc=(U9)#mot?QA(noXh5%{^Hy83&lOyA?ey*^<71HC%+9@7TYzb{D)4{j@rG|(n-trFg|wPH-O'
        b'Lt=TdKyV8Y1#y#?ZC0Xie+jsZnjqiO8g+hb$?GWVcSxtHo#D6oDjiXtVRc&DVYEnPD9h=P0NmPH7CEV0&NP<edcH@^(F26v=JX4E'
        b'$E~UnhZGp8pa|s1(aEnbBigZ==7oMGYW011+QYc-aDy2&>hAAu_8l7({Au!{Bat>ihdkNN8eKyQqN!_8`iqmw#%F?zXPpjL%UdUH'
        b'!ddX`0XhPMJ!?=_&>WTog?qh7sgt;<ODf^j%n2d9H<vnfB|MN&v-`WTA;I4#5@{DlU;{R148$p!6y!aNzd?@K1hZkD`FY;x?@7U#'
        b'r}5A(f&Rp>YYyOYTx6sT1qvDh=ja1{E;RWm0=?6Ql{xHd-&I+!R+%1GIn4=K_uSVnul7XT4f?e{w!pb{TVnlE;Ze7>bGB|XaG=4g'
        b'Fx6~1E(-JxZ4w3gO7wWsNE2NVD8M}RfpgaQ6zasW@K)MF35xi{AbU-C8?TR&;i5nvKZCnSzjlsjtq<!ysR;Bn2hQz1+_+`nkNmpf'
        b'5#5$dg%KHA>kVvm{aOKNk;sNaZ9P{tjP^6y8RGBAHO*-Czev!oVy!@;SGYg{`xfI?-<Z-VfCp9_8of)d1j<HP&H@5~A%=ldl*gIa'
        b'%57C+^e%2|0JQdjL%}eg%(3j9#QZ)*jjj;FO<*eOY*ih)!rK?+fxd>FpZRz-2KX5;uNVXF-n6wzS33e6huQ!vE-?b*XzwR3t$jB!'
        b'GqGUa-9=p1<kVemz&CK+Y>YIf;aAdZLI#i<;`&MW%H}M%bkmIXypBLl*9Tz0pjcMA3Yet8;3aCSfK}QM!q)wS`)%HKsOA`29gJW;'
        b'wZJa(s-;aZ`hg`aUP@lMjLicnW3jLoAk{U~ExX7A)XI?WruVq;ISV}ynkpdCXHVBgyI5eFX6>AWfga>1X+r_8T=*RA876@sw29cg'
        b'`^*8J#3lGtM1mZkEYIX6C;(`ACO;uVp6QX5H7SXWjnIW$mvqO7@R08Ke@*e&b#f&)qdSHLpHaT{cGZxO;aFE?U0!8cS0z74ivQ&<'
        b'&tUW%BVlawRBKB2vZ5s^*2c5ILQktrIh3<M$xxsO_W0s0^WMp%cVms&nZPNiIXpL|rs<v{!v|_K%Plgc`%0T?yfS??FSR?znoFb*'
        b'SGKfRtLaEe2@KDP2)R0ZHJ;k-67M<Pgqu#M<ZV9;S~1)!Eh+Iqt0hSO=O2!pRcG^Z>y=7>fbs3~2mYbxe)Hm?-o2^Nt8o9R3y^p;'
        b'fZTpu(jEJtlIkY#_5d}~kKkFWClw-JeZZ`gEwv_qS<3ZP2XHe%h0~<+^0Q7AC}z=29^eA`wWhi2np@RHl_R*y%BeC1R%stty4)3+'
        b'ydG+YI>iLaDjzUXR5_;9>$&$*x>duVZvcPLLQYZ2y`*e=3ISAyqC4i%y|L@LP#ez!BgmwJJqWmb&A|gDzG(G%lA_N=AP*+uhkzN&'
        b'wK=>Ly`)0L9L=9JBm;1MhQ^}W<dk}iGiP_B+ON%+lx|$jOL`EKl$5SNwLozSPaRBg)Lu)CO{vG083xBxHLs^$P2u0Xo_dc3EMp@L'
        b'7=9x{tQM}YGn0nxP~Nw*YkzJ~@hlrB4L>&sdCFV2$5gHY!yL$H0H+N=w*JR&^~K~1uOClQUAmWgy&68&3A||luR(?A9^t^FqIw02'
        b'Q{b}lNEf){KXzVQ^9hjL@!yamLWc1;EDE4=hS~in^uKZ@1>8y2E)vm>re42!k9CktIcp&DR;Qj#xtDIRgCF-m*Yo1QP!V9Lstc&O'
        b'Nuwon2N%Aw>^?*L0E|WQN0q?APVDaN#<+8yqVe+)BJ9J2v$_+!ltcUd;Gw5Kz6~$P#KAdX*bB6dcdaSaVL($nfHSO6@eQIBS>m8V'
        b'<*8SB0Eiig;cUvGHIa+KsLhPlDljxm{lNn@&3@Ku{k6^di`N}{^(Ld<vd5iTU?2U01fCAXx7a+VV-*!Wa2C1i_@wI-uFv<8yUt9c'
        b'ph3(}K{F~IP?t%o3R2HXt|$MYGGwphEXEBvB<W5(n<U~T$5$pnw(YqEZ92o*4U9dO<vBs#{0*FJF+Zg{Bfx!55t^P;khgYy+pZp9'
        b'1^KUUTlX5HW*4)a1+kC^U~}$=Q_B+!AV9KKPOgND6<xGkn&s`u{W}Hn0KS2?EONFYz#}bgStl#^Z0)`HyQFJ}!g7;TmOstNoYnIq'
        b'Y(J-a&JF%xj^2@@x8~?gbM?d==qCj~j5Kr~9g8hJ+aU5!Tem)KT~xTrzcSsx`@)cP9-a>b(7?p{g50&02BzXEU5tna`h<c}qzG~y'
        b'DmjR4&Y{w?>y94DJsW?U%sEtY#GZS00|yYFM$r~t7U?8+EuS!)Er}eX)<R-|6F*nZPg1CS<tiT_`Z830DLZolfNJ;4zTvIR$V4$l'
        b'%qkpoIl~AHb(;PlnOmRh$O!c~M%0>Wt%8S~jGjligQF3Xg5w-G*TFp80E`w=k-<=YPrv4_9}1vZ-Swtmy>tJc#2>oHbAe5BiY7PG'
        b'Vpiix$`R0n^5e%g$EtR^Lgg)22`n2I0PS%65ik_x@L-P35!X)7Q1KNikI@Ya)&XO44RY-PanaNIfH2JiP}h!@0!__ILXef*o^xbQ'
        b'dG%$$;291aD7o$~mzq$9KGZwju1zM~_2WX{+E}$NU1tcW4c7~OMuc-~g#=4)6Z-XY%YYWqPPC&Um1l;^OMGuq**ref?bAMMNab%?'
        b'yI@G@e`TwlKF9Ht&|hTP4K#Z%-o=7^`#Vzk<Ug**Y0ZvEqPzkw33}6P&NsoQc-;b<Qwn}qvKM4H6M*V*M2==HFkEXm03YpiIwC1o'
        b'<(efKw8wU3Ug0{f6GM(jn}gcxiURO&g5RJwZvk0yQ!nyOsPD|__<UrK``~55ahWh}A#D5KCiFV$@I|9%ttaSQVnl*TU21QlYu@E1'
        b'F2(xVS;Q)c+7)K0Q|5d#XQ*sk?vzSKay>%=+L<nWvEmRVumn$T>CgBl#YuHpJ7VH-C1bL>!exi*`BG>xqP2sG4oevcm}Mo`Fxcx*'
        b'US>4V=S;90VuKqq@35LojRnKZS{hZh$tu1??&8vOVpEbaAN|rfxtXa2?R1+Hw<ImVJU?QntEzPB!tMKwukDZ;3%7^n>Qfuw-S3rL'
        b'>iRsiXRLdPAtS=02y%%w`VQI0ZJ}P-c|%AWxWUg*3FN9d3YAydPk@s!*3dqhb04YSk2HLSV7>~W_nP@=bu6MR7Rc!WrI#<TSmbg~'
        b'F2=-I>4o+q!DzJ|`651DeSb(Oa0<PE5zD?qr}iN4k{<!rB;$;~@}axHu;^zc0lj1EYQnUcaPI&6Xp%eBR3G0EpezxR65v;i3H(;4'
        b'm*DEvBg!H+95s3>+?taE&Q|6@j=TpT?kdNDLN2XASTSmKeaZ26@?(i>zaxeMP?H*fb#$@CE8J&rVY+Y;kCC4;jk}<Q25@R>IOAWZ'
        b'+yS4YUoD7SI4C7d8KCM{U2My;nX1?;uqq4$;{dIG{b+u5CVbvW=$*ifi8~yVbU&$M--S;+04e<9<nMCjLho&Ha+P<Fjr{Tx9Hd@h'
        b'48{|Vc)(rPO}BN#Eoh0l!;%}gz;@NG=I#FYj7{hr6T?XH>tr6wO!1a4os(L?x<i7>O0S!J`v)Tl#~YyjUDkg{^_NrIx0Z^@g=yMz'
        b'A90s4p>v}B9@>J9q?|oRaBdWn^duvQJOBZNbq3JoD$d2FV7#nyvB&B9OQzEf!8wNf<fFtvxg#zyIaWYm%yFS$MCb*kePV2Cc&ad!'
        b'pGt!S6R7}Wcvy~1e#BklJ70dr9}~nVtCC_0mFK=w^sY*ZuM*s6$7{)iB4DzC2@KRLoWNVP(5rMxyO?nPE?gjYzS+fqGdL7X<pelI'
        b'Ll%@?(;q;9YXZK?u7QjS?z85pxh(bu?cL6EjO)M@rtGK*kg%r>w(lKNRHarIDlc4+pIHTdE0<lM?ui1c3JwyRG;YPWQzZo$lXVWt'
        b'GQcMFIoav!Mz;41ey4L>*IB>UvG#zR98+0DsWW$Jj(6F3inxoL>y;Xa^_iUsdX*26s-<=jd@_V{Qp^dg#A^wH#GeJ;kGH*Lb40cS'
        b'edaUjvjF4^Zn0CCtj8p>k{$mhsdwN&PWI~nJ!@mrr{rY1?tU$w=+XfS*U}P&+6mYDU8#iF1p1}idRcFrEQt&ShP$E67UE&<y`m#x'
        b'1q+c5BDOQv{gbV=9i1Z`274o6G-U3MMB~LI@Jh?GSweCphqW5mZDAON5b<miz}Y681JF9^wXi|x1*R~V$l50?CU6Vg)Sp|v{N&H-'
        b'@}28;$F_=FU*FaQI4{E+-Tldk<`fQoG<eV6eFTmFiZnA92+GInvh5kG(SA1E&H~`GR!zeGrcHdrjW?6Xx}*Pa&j$G!OjdT#p&W~Q'
        b'cCH2PXI%K?GtflI8%DpG+>diCe%aOVTs1)}HLFH9DO7>VHCPTnJVS-&cy<95CCqS0fq?xAc40&qIPTyLGy3V&=pTmu&#v;>atF_L'
        b'QVqlK(-!o#g<&9*PW%&A$QGwKoe8d~A^v#+2#RL+gxGwQPOicek`)e~TqTqP>B^O#W7*?q&Qt0xraBInb^BoRha9Ets9ZH)rdp77'
        b'kbIB3>lQl<qnvu81;YN6iO~TBnJQ3zN*y$J9frz;f!OcfL#2P-QSF5w+x9PRW|Xp7UqQRY^2>asFR5p<vVDFue7TNu1E`wDqb)7F'
        b'k6&rLU@$cOq6dBm8?d+tv~*>;;mi7eYrEJ$jn#e$^hO#yfgJkOwRRDX=^i<v_>qGnLgA1Qcf6^ya&)HO>Y`|t2`&)*?Tpd8^HT;('
        b'9etr?K-@=~mG@?KF`Q6eSRy7DUdH_1qZ|Lq9QebIy7RmWu5uo(y$P>Nt%PCTIwn2^Uabe{rr9YKS59=X6?@4qq8pv2pDOFpcDB;2'
        b'cPht{FUC4>ok^&hU}in!wm7W|bWuYcZM>+FR;N08XBT_%VbpfvS!AqvFDX;`M<&Zu^Dz2;Z%+8%E7L#bOQY~{VE3qeM~vu@Bi-px'
        b'yZl+1%4b|P7Z^)fjpV1?UB29G-`~rG{$ZF*h0BEVDAG5mf@CTok+6wcZw_iu1;(EMGj`jdc1G5<`Jl%EsS##6D?5~D>kfl=8L!S)'
        b'E=M$(?y238^qw!sAtMb?BIa|*5CGPYN^A)QezW%M!Zyqg!=%wX<5xTE#zFvlNGMhw8e3SSJG2A1>sNZOv<=><blj-4{!nSsRT34@'
        b'WPi_%)l7a$kH1A~$7()Cfi5>Vb-JC(7B?3KNAo5$d&vWB250?WDs|;MDbii6wC<@i4OYVAL|G%;`hm(6XC3f5oftE9D0L(yR-wXE'
        b'k`*c;ApM#-oN!fTdJSJ13FzY`qXj41DrIL`_6QoFVNwK6(J%>^vy?$FuJV?_6E1Van<2-ZxiZbM&&nx|jb9CjHPDd`SfPFbo@#%<'
        b'%A+2>;j(gE_5clIVBY?Hn7i4LM9ha|R>ZEuycH@xvm<Bp^n5`Z&4x;mxPX`ynK2#d$cX@GNNt~RSvgKejtxv#RO~saJU*$Rty5m`'
        b'1oXB!azKmjlMC~{E=Mr$^fgt=^Ust5mf$+m@o}X!rSj)Bl_S*25mQ5@c#sR`EC2%mAD&P~KT*(@sR}C<=UMjEG<eutg)1BhkUkC`'
        b'9M4mLf0Cf?J3;Qs`^695unvkw<Ij>keWZ4DO*0H+m*L<!u*zZXNKYwcT4w!yVprS!aiIvbsSpN$#xMMp`NPNX-Pj-g%3Sj)$`T?f'
        b'S!I5BrDJ2IX=5c&BfvjQrDc5y+}|WHvRNx9lw1^JDpdaP&%ET^$_%*mI$zOKs!%P!76G=7zeFlT*oe?ODQ)MF(97|sO4FZRkdO)H'
        b'sFQ1Os*<5cg0XUkaz|>N8GFff-hWe#ewYp;CgRiyE;xWvI2POB2(tb{-5qc_FqE5efZP>I+y2Dh#JGU*_WQ89xPa8xr_XmekVoUd'
        b'Si8IPa82#3=|b=|rFnOWCm%YNRO*2R_~^qC5r0U;GeuY4eX>)04A4JjYKiILgwl7S(P<5?G>msN@pM~vHaY9R_%PkTZyjnKsWafM'
        b'gV2X`nXY;jCVmK<(Z}&WkeDCff^W#4@1c(d#?v+BMjI!tJkc}e)YB?mrapimKk4K0rhx5BOXQ2kr*S6`MF19iVAC=t)3w7rW#YJz'
        b'AbopY3|!2Je@wEAuFAVPV6Kn;70mUCWkreR0MEul3Nuabi9(Js@ar1!q$XSu;MGKH6sLHDM(dHvRzCQTEdnhw;EqOWc-Ae_(7orD'
        b'ux=A>z-znVd%Y=#fK#4a8;jMN!Qh%vsK<nl%5eja^~=;b<tgRzfYgh)E4d9$$@Y{MPR$PQRyR?Amjvz8z%{QVIFX>?{VC@oZqGv!'
        b'j0-Tj0o|Z0E>mHnHzsyP(~WKLI73adyVL0k;{NT#mCN#TbfB5i*W&4IeB)<$D*@?EWvA9>eMipRIY=Zb&^e=tA|sNK>6OvV5oOK_'
        b'xhKl>OzmEA7FJ-jvn^M_H2u1q4y{5iAdY-5xvVinJCe|y{O+bMdQu#o*bVok#z}Zb2lna;j3_N=e&UKijd{tJvJ&<u(xdhR5FRk7'
        b'RZZ4E4MaPqww}m@{3#0dGt}?5u|)^3P@8ZfPc$~=!*mfpMvf=aV(*k0&3H^39=q;CjM*xT5#iVpK!1Q*DnBF^5ITJQTjC*j^~CoJ'
        b'W%<KJ42%H=%^<FMEkA`R5B3#&JWG-3+0L+a$KY{?!3c{*6Ki&&@vkEo8vivMklk4@9uyvE2?FT71=|OW@6Yl8U7WjVF!4js#{m)O'
        b'X3rQo82O=t^Wne{KGH1#lM-}XykP=#_v@{XdX58FhHmy4H>G>dsN63O-lx2~69zM=<u`f{d7@jJ^lnH>Ncu2ef03Rvj0094o9nn&'
        b'0Z*Q=0H~~-iLZU1Eld-fdb)_q+E3~Oyc&I|Aa+!2ID@1icwSAEmbhQ8gKP{}ms|D`d&}Ti=1fmz+s|5gbrUHMzzAcR;^3q%4wq+Q'
        b'7(<@P2V}tUoeBF=_l6u&Wb)*h9s=|(=;zSh$$_{`(Az<e4*_9E0z4f96`*(2!2cNzeDj^2&E)#=>M9ahZ)54n_3|DaNv&D6qg{0I'
        b'D-+a`HrHJr=-b8Z?KB6@CH?{t0^g#w-i-!BXBTY%OeRC7Xzd*RT0z5FA2{p&dlJ-2V-u&!g<&7oUIV2=OpT=mgD~_%y^5y~^b4`-'
        b'ReXJ*zc2_Sc<2M?wbtuZp2Sc^hyz<9azwh=nGrJB^s`>Y5!=A{-%c~f3WmA;T$nN10aC6+n^j(zhtrY7vjP)Gr1Bm;Fabl@Stg&k'
        b'-em>e0JX*i`ZINul{R5qjw{RAU0nY@Fn=*mA`kZGJw}w(?2wH9aef6?@Pui0;#q$L*4Zn-F==O7GUs1O3qMo=SR;z|Xk={YqSM+@'
        b'VPbtax{jOUEcH(R9WyT?YCOsrDb8@dDa+u?M828~UP@J@O_AY~6fq*p@W$w}41p|T&LZmKDJUQd;7G$`7r&0OevgEIU!lsakf}Un'
        b'Mh?{Ij)W+F_+Klo4Oc_~dti8a=Loo19$Bj<{8lgF?rM8QkTx5S4#=jXti?!V?BKbID1Bt|h(j9H(9fbuXT?r{g1)oH9GKwhzyovt'
        b'<Px^=4e0du<z1EDmwvWmPukBF6^<_}tQ8feo{Fni?_1Ki>-Sa%BNu<(vtdN!ci|tie=e$U*ek3>6()NHu*!!rfJWx+`E*3&f8ihe'
        b'pFgN@oT#vFs4$(Vh^Jx&4rTZc3Hh+{JXkrq!g095npI&sTmdxKP{usa@r&2Ss(zR^`{zGbI65k<f2uHbRK#B+a|R;|77ILoPOZ2z'
        b'%W<H>no?mpPysJH00Y7)b!ncgHzthHxFBs5ilGs5CB5fw@J{@}128<ai)R7#M(assGiR6!*uv(J05UX8>}qBkqjy5lwgaxOCYaMB'
        b'_=z-Q+~MrN-wpn@!r@*q;z$@ci&N!C7lHD?Hcr@P1s^pN$}{xFeBxha=7X1NYQrfVMn1b;ZjNP{lhL_mVp5CE(?tMF3@~B>MyFta'
        b'p&YFyBWY3Q?bJS0cHkr1K@#Bd^qKPVBp6NzTf7;V3zOR%u2%mWp6yxRMs4*YZ(O5M#&57(6*Rh;G^@gJ1rDZwZ-ztdH0~MZo^inN'
        b'u%nv+yYD)KxH?zCUABX@-b`&Y4;hV4W8=V}&hF3w<0Q#~i}kQ9_Z4IF&Si5ig0yy)<u~&iEi1WAriO!)yFJkAC5TxVL_92ocC^@U'
        b'|1mVa5D^5<YCL5MtLUN|n|SGa`Nk&P<j{h@O{W@!{!Ql_g!3A*W<vlCC@TzU;3t`mYtx%xxh{GW4So;9?;&B3u@%R#R$=?B)BMxn'
        b'4XRgdszpwfbV&6Z;u37~+Mdz|;j33mcy%SXu>>!R&40CGNcbCR6RvK;okHoQ<R(>aeg$R|F6t|+H)_*2@!^>(0(%c*_tRj9m}T`@'
        b'8_AMpc*j;^3b6nw`vr*rPsSJRIYt6hmd!<b>}1ao_`8d~JA&qS2y^Q>PvSc*>V1dd;om4^h@Yg~hg{gf774@R4}ihQ4q0Ar)53Fv'
        b'gqC*=uY+5(pe>90#I7@sVZ%T|WMxe#pFFY&`So#-Pj<VbtgF!6VP;)<rp)`L!67lnzG_YuG+6|n-(mfY6l|u;#h7M460`GgiCb9y'
        b'IW6EwbsSHgg~jG+oyNM>^R1&X5x7|;#^$-k8u*kJ6{$=ck2FPDwAU9mpgmucP^pQ~>T{&_DZuDFkafyi-%*SYkP`oC0)Br>nPL#*'
        b'91_0Y1N3lwF$tu75p`~nvN>=lK+z}yD1}|e5#yPi!whOe0G*hzC0ymYAYTGwTBhQR{t?cT|7D-7ns^pHbdD|;&9e{FVzM)ViIP5y'
        b'JHoZbVf+r0D)P%SxVJqL-0W^X*d0%UW`xnWbLyT=gJ_=Xf(|ff@33O*h3n<(q8Q>2rtjgHMO=`Xh0PcE(gycy9s9M`{aTYy>vBxe'
        b'Z{W`j;n9sRoRe)a1AXQ;{|a~TQ?27ut@Tr_$x}=4VI`Mp$XZKIzyI!PL(BpifHqjKb?neucW6x<Ey0Avp%E~9uuki!(^~7buE$B{'
        b'JmSBwgCH)W=tiwirB4c?C##>5(>RPG5C^T+QKhw3X-(ssh`Z2AdU5}uU~;OjRQZW{puAe^DAQWYw5A)Ii0^-0K4)_3jH3&0%aeH!'
        b'?@X=Z1FiJ~t?BY6;sUJF*gfZ_`=Chc$kSTihj_1V+qIdKa@KHYP8phHD5&{-1x2-0lS*H9hHHZ|7j97AfyNc!hSUk=R%Xui#Iw13'
        b'6A!7_WeMHslnnxi2e>2Y6d*e2E{5W5OMBdrWt}&MjHuIyP)J(-G`Z_I4P)s8W-aUNce&hDMn)`ebnWEVX_GIH?@v@8WLih8)*7od'
        b'wQeFlgME;kogPnDxzQh~auTg0N^6bMn*O?p*i%l8k>t>vQby!isi*+n_aI#IG)OEZm7!>)dC0g2$j8frXB<!xN72O62{5OcXUqBT'
        b'$o7(pcg}J#&aOOi{ge1-B$SICCGa6Xksq)h%m=S5i?{-G8TA+_N0#9ubL4c<v&ac$+Osfh8!#mjh(K6A!;!9_{aJaQm3(89(`W$w'
        b'1_GJtw?ZY#Pz7WK0(>54&=x3rn0o#@s?t*6ngGiV5H`^v7Y5aTv?*~gwqX<SRzRT`10H*B6UIz`YX>~oL}`&GQ>wN0TGY>S6;Gz('
        b'XDuMB2S@~3011Hk{3isreu?h`918W8WydohKY(<Z)?HAxPz4pLK$%Kx@gohiTC>vkuJ$Q(s_LEznjiLj;W~Rp&7br0_HYNUZE{@O'
        b'WWBb@v~&{@3yCdPp}^ZRUdFdMpx>0`2P7lYxcP9lByCze$PD^gnxUbV&vW1|w=c_M;#poofcafC@lZlU>)ym}ED*X9X5dPgS!^)K'
        b'gR3?H;o%6}G;kRQg4b0|{Q0x5o2fmx^=GE`D`F9+iG#VfGl*Y`0X8XnuUIgV_4p=H9I|a6VS~dU*^Bx5i9+_mdKuk#wl^0OfoyBs'
        b'rs{_z@Ol)Uv)42V%=86<;}hvUxUHK5h{u^wUVaAfb9$n~jBRkQ#`<jGR_*yUhNB8k)Ni%oT~s@|#`m8+KaiBInYDhJhfRAnVQ$Ns'
        b'X!GtiSLrzj{&_4ek>dDk@Q_NV1l4Vh#ZO4#Q?t6)s6eC!PDfy@P9*hf>iL<9gYnTO31{j)s#IF2J-%IU6V2b=4cd5@bX`HNns-<5'
        b'TVPRGl1b(9Npr@0N)ExgA8xXKxXCO*h(g$NlXjCWbpELPr8k4ZOE$>^=C{)gn-dCS40?=Fi^?--mV2ZuV7{RsQKoCtw~FBHTv#>_'
        b'l!d46h`Ys9v;cTH`VRaVp1r9ptJKpkd)-m5Hy8S~bsR1@e!PW#%#--CjJk_lN*8>IwWGu}SlX|RP`dzhp@L>E@ixTHh9atWH`%@#'
        b'?1--d<J-<A;$bosI{#a@mE69|?M$K?CPmVv@aC3j`KB%g@fZTC;NA{Rpocw$sCAT4XFiQ_cFZTHX2;g$nm7Oi<HFd@8U`YmLt2+?'
        b'0u1tFvFj}aO#lKMGU5dM%=X0q*RqKa*bJaQbdHE13Jv)5GXlPZ@T>Y;5-Ia!4NvWn!KLN(Zf5vkgyjy|#WjgGVebsnoW?@Sj;Z(C'
        b'Q6NlzBxC(Ib#eQF&myiRiL~<fP&<yaa)4$IWf=GkGz6PpOW(lNpPtlxP<6GMXE*TmOBq2S7;w>z8<GwK$3|=*v3ItC&qDAC7cgtc'
        b'pyhOo0go$c$KeSe*LxhJWEbr{c$iffQw|$JZ{N}z|D%iJHP9H^M==Izoq;Ef<C%Ub2ZCh8NLw-JYC#{%$TE;r4H&Nh#k?^F{??9|'
        b'nK%mY#ut)&t338j`8H8MqYDMY(@W+DQLV6V_|oB>YSj<r*6+*PSwsUx<XbH3ckt`K;nx-4ei-2$nxUtthS;C^o)IxP+x67C{OMvU'
        b'z7I{$KpKpQC^H5iC+eMqkrdeYU#c``Y4#AlXc;3&GJD9xxC{wHu}CoqU<lAhi|Fy+kw6`~ni&1ZbQ5U&w<Pr(4?K@)eA8^C5x<8+'
        b'iOYa7z30rf<EF#q{dC}668FofQP~b-N!%))x+PAHGuG#dS9-OGx=BC!FEV_8c^4O(Pf@R(p7jB#2jqRi9&-n|eSi}{+G27h29aq`'
        b'IehWA8@I@3><iQGa+?zq*OMX<O>d+bMRtsfw^Ti^^FLJn|IAEUn6?$B0XSL2b2wXI8qmEUSzPhFO#n0Itlm^njyrMvTj{n_n7DM>'
        b'eu5b#<^AYahqLlsX(mLErte81J}S~nR&Br74ukS;&ugb;{g<0LW3FjEY-99&AZv)d#nUkn9EjOiCsNHKHbJt$1);5M#hJB=Jb&yh'
        b'MczDxaRbIsEH71@$-!pHm!~W87RZf-n74fSdPN@o)$*adxkJlyhStv4oLR3pS*pnsVZoZbfK<nZSsJ58K}T*MZW$DJlHn`M#~i~f'
        b'7<U6kgHI<_wbVed1m!@{5S0)gxC4Uulz2-Uj3v827V0giE*mFOf7KaFIP8pH1Z#|JFsgQce4nrufpR@hNLQr!(Q?w9L94z^*=ez_'
        b'mv_+<KnqtHNODBEO!SVNiAbXu%RCp3o`1T8dmvgbdIw|ZY8m>s5S@;3SHjnxw;5pwckzX%8@PRG?R3jGPv_mWipyJAM1K)=ZD}Iu'
        b'b6$%8KY@3wz%7@bvhGpyR)zwu>hm=5%YhAU`GSPY6U$jL8e>`JpP;C1fR)4D%HQMWc<w(k$3R!{%l+EcHHwLOMU<2^&=2IKdbZF3'
        b'pgvC_S=NOT4~nLi77+x-<RUVme^q^-MBWsIc;?cz_k|D3dd5lrI2d~a^jFY8GmV$ooWQ1^M}$KPn{!~)h~Sy=Hc?A|e<j1m${>S}'
        b'=22%IZ$}ekA)xb~PKwTZmbcTyer~Px*gHdxKp?JQL=vEST<>;YE|aaDFF3@4k+}BZqc<kEr@@1gS(heVDV9-ScQV5-6*?}J4F$Xt'
        b'e!gtr5@Tp7GB5xI4&&}H-}1Mo;nxd|I)+-p*9Yk3?PQDrhLg}|>i0y4_m)ZMeNN$nLb+%`B0c<cnJi-g^;ThTndwpy@in9g%Vmcr'
        b'pDdFwl^IM^cbVlVYb7_E%O7-<IUHp+bD+slMz}+Ifw^Ndl5ovP&oV~iea8n+lsS%pA|db;Eo7N$mOhle2#}-ZwONhwW<$;AEX!tA'
        b'2;j%j64nx~vU$R#m|QZ{z1^K?FPnKAeF>_k&k~`S&cKIV==}woi=n!Z9fSpzk<n-4c>3bwH0}7*oHiQ~;;&^>5oG}1T>G@FclP$T'
        b'U2@9QTQW>Dnt4EyMB7f&h~2QD(s$B83zbkYs(>D^FWatfp>JPK)R(y)zo1j&l9W^km-_k{2Tl>&%Bb))1`e=Ob$W4M%br@IX1Yyw'
        b'4s)PMT31)7BVu9PJ3<e0svk|qzNsv$cN9VW!FiioC&FP^9}cmptYIHQC2DU^Ckl(p>PsM#8BlCNodG7+qSR--rVM)rD5?7Vvgt&L'
        b'8?muWC*l!@igY5J*Z?y^+$e~~DR@*V(;o__zF}sIo9G~dxA8C;-Ubs}VPYf4^rtdo6VGhY8Jln_Oi%qE%Ba%Tw6eiRh43DJN?FJA'
        b'8l4=|>N5KY9{70-Hq*%+H~}+{aj9DCH`&{G(`8#Yj(5sntgUTR060{lHNI?kc89AN$NE;8X=&LE0M1l(4iQ^siY=RN#lW@xyAacM'
        b'xG2Lly;){`r;tkTFz~1(BC^bO@H+~`G-y|2!oulqleEk#Et{@o{Y}|4I9CH<WiWN&OQ~+A^@Uxp7+ooDt`tC3>RX=+7%-Q>Db`tl'
        b'y*fO*>lLSw4b%K!+8uNl#a_X*KnTJ#0afl5Y~CG^)-?+z@ynja(*cIkY*-regE{V0;a6QrQvg_0+JC)Rj5ZAue7L|8&)__*zf)>@'
        b'T1ug7bkWDH{-;tCt?=cftEHy<#V;qFD>Z%ntBSWuO#{<OE;>y6n;Iv>X?$igQikJj0mNlq6zaddiw$J`SL6mD4*SyjR{K}UvKP<0'
        b'+raXJiai>yi`*ftE8LS9v$aa6E8N~|2}W8O2QI^U;t)j6V#tg)7kjaUeWfreH|RawbNB}doLU)+>CagFc{{whBQnugw}7^W@tk0+'
        b'g}}uXXhttji{jZl%tM!L$5%`H<_Ja^=0F6@UEsoW(b`(XPEwi1km3)dh9cY`l^Ue(LTO|y_@5_hpaaEKsH?Su>gF9rfLf&KZ>3kV'
        b'1p5(C8!iX2#S0Kw;9`uMmzlA4@yt5V22>NYSb`=B%S9ovBIBOWppfv=SPYf*_=nI$EM@{NIB>3n6?_zB;fN?`u>m+X_HvCTdohN_'
        b'`$O!UMtEh04b(d@f}b!Ggxd?T?bMlhA0)vu2KQ2G7^Z^4Wzn$`I#E+<HI#1EZ!4)e!6B+kb$VS*G+QkK-qiiusO9fuYjPR?%E`v?'
        b'GB=6mil)#K39Ts{czU#L5v(ilfOc^y7z`mzWJKz8_p!M^z<z{El687JV&KO}GWTq0;lt=TZR8!UU@HTgHNFoCUczgiJ$is_<l}Mn'
        b'(55Cn>j(1kKU$c*?gpW~P1?%b(=uS(c_nSYX}{Z-+0MC?e^d3C$ik3E#F*-0{)*wApGfU^{56-|iFsj|^kkLYUicoWyu!jyRw=bC'
        b'gGc@50+9)=iAwEc-eC-5Ku=zR<Y;D4I~+i7X59qe&zh-&EnLf0xB+rTPxnjl-qULiSZtu%j8}&lVc79QTiYyq$t%tBfW`8YxIA;Q'
        b'EMW2C!>BM4bR6&v3Y_Fc-1ujtONSH^uM|ufY{wBxA{)Lko3)(1ojVgx$)ybX#s|Yn9bu*ZKbpcyiDl3Z7)@kvZypRObp)4&!AL&S'
        b'{^=oH=|LOBOC5owHe;{}FC~5pi|_FSkQ3P3+Xm;AI_8yzoq(DG8WDbQeUIQ3f-)}KR)r``sNf{SQcnVR%JP6T=HUtxP0&Wi*nQoA'
        b'7A(tS@;!Pr7Zk>m?(2oXNuVX|uBuD1Bdht+)tT_b^XPw*pK|+-1LK5cc}Qv>K&#Mr98Wrhx3ik~S>s?d(?soVS^q;OMcAuvy2j>B'
        b'H;fY;!Y3Y<P*0;vQ0*fyPjvsoT;zJ|cT9d!)+_4tXhAI%Xsg0ybKfqp-Y)4!i967f(3?<po<DKZ1;Btdw3C!>suS@j-J~}nQ?N|m'
        b'mRP@q^}c(d-ZwM#%*a$d{MYpcN~{C0-XN^E1Qo%Wp~8QaU_KHQzO-U6wV?jvi$%UrT(t>LmxM-Kjo^z+5MT)1HLk+HX`lkUj2n2u'
        b'Rt?_7)74Va?Q;A*xZYqoT4Fs4+vud$xL^y?@XiwLQ{bD`YhWxm>olTRB86u=-G!+r2O$g^Dk9$^mpx(HS7O}<VOd^)WpTm!kb?D>'
        b'8CbRd3s%v~u<A>!^$=FW3$Pkou->O&ZJUOrJvIZ2Hw7!>Wmq4USU-fYDqnzA>4KF)!781BRrbGN{r)9b#Ksc;#|BP2+R1Uf=3y`e'
        b'hX^1+Kfz`V^y4-YLgbcAd6AB{DcXN!H}D+GHTD_We-(e9qJ2t<H3j08`T}05F1%zEUWyqeF(EGz4A@s8FZc1S66;$KR{RXCl<;^L'
        b'tOc+nd{<XQEG;opkQzDDb`bSpZYP0tM12#l&$Rh>@+D$`HnEr6l$2N{u+5Mc@DFjdiBkBBW?&h0zsCP@{!6gDORU}ymf!_g0vD|R'
        b'z>>r(Gq4U;{u-|vFT+AhtSE#<hp@CyjenCGV;IWU7!NaJl4&I(r++(>xJ&_kS`2_1I1L9X4IHU7FjN8!0FSx|K3p$}gqTKofWrUE'
        b'pYf`|B%FR<$TU`L9V-UT0&%l=8tL%Zo5i++RM0gCtQ3B|*btE&$=3Zy*L}pOjc8{O$6<PJL<_wO9W9`{uy(;aS8P2;!8>0(EhuII'
        b'6(t-hHj9waVmiiIG`%)xI$dl%T@3noruex`=`HquV&F8+aOQ!k;81Aa)rPoghPUKH%B4yTyztNRr6QhAPw``F{4Zp1D75=(qduYo'
        b'Z_)HARWKJAN2Wdb#+ib-)zjx(i1uPQ4-7zv!ZB!kgrG5Xc)csSGPD{cy!!3=fQlephg(^Xr|OwLDYkw>^>GhG99|QIxW5hv#?F+9'
        b'+sSsuoXm)<)1>g@Vk}XD%1`<m(5rF$x&YqtgaedY;5EfUUX*~#`i!LB>_dRsW`Q4Y0KK$_q%O10t9mN#bONdn(UM-n1)kpFRmG~R'
        b'V(DwV^ekR_1g^a2Nj(_BBuXGg>|5}*98pkwHIu(JJBM|JHCR^cC@VIV7u!rLh$^VOpa=K~DOe68dlu13MeTI<4`|OqL~J5WnZ?%3'
        b';(j`@76L03VQ(9aj4x}@>L6rK8<AdY>-INruATrqciaH!=3{rwL!UW6pz&g4do(a9kCCOacDmpfj-`t%m4jbDaKxv{PDMLiJVcg)'
        b'e}Z)!@kLVGnXfF?Rr5+3J@Qu;*I$Q2W`Ku8VaM6<gO&eIvD(1Pm*uNnCN0Y^;!VLiPqfELLgHB(NY+_MJHeA*h^XQQ3b!VJoAyMr'
        b'3%iacUiAeMG`yQ+T_&@Rkt}Loe)J^i+Mu_bBjbljFoZony5iyhP88S}QQ_gi#r_;PduwSSLb-~jP%(%JH6V#_L9s#hd_u_JJGl>G'
        b'hBXjyIi2UgM<Y?aiP@KCNZ#%PemsBQ$AlGIG05|?W_bQJ!mXGR3ymn{m$5U0{LyL050mJsc$AB{rxf#)PWgya`gQ#{jO+Y>)Lxgm'
        b'q=;Mf43CZ%S;vbYkKThT2l9iYF-{r-B*-fI!=*A{!UP5Q2Std2Jl(TChCBOpBoqzeZQ!@KiDW$^v$m41y}_&<B<l%@$bl_3#fPSE'
        b'imcxhfj(R*dM@X#6j5^SFeC$UzGzxUhWsxbc|iS=oa-&J_Ci>vUx0Pm1<Opqa!$k2Uix2pt?4CL10sI3DEt&vK0tzQcVe?zGN@Rf'
        b'j>73!pr$wSgFM*TB95@DsD%oyU^-S5Bzu5yv*mY*V-N}9;Uc_E5B(On)^Zr)!XzrGmV8!3K$|7fM08NC7$h7Cn(YN`7rjWPtD=0('
        b'3>he|QBUblkkTNMX&*_c_3N24b_068)S#<xDuNNbYjt`Fvd5<-NBflc7^3PrH7|bTT6;RO6s?vb%5nGn9YrD&-M|)bxWfM_0wNlk'
        b'qN%VY1KavhQKL@_Wc}z`eXrL5+?eTz<K-KQsFeVF9AABc7vu8(p~6hyWWVtzRf9S`4kjhSBwOff+LJLSc$k-~oGtIQ=%$9#UIQ>#'
        b'IptMq=|CnWCB2sP+{=!1i>=6SM`I#jiYyl)UQ^GkKdTZ7(&Km(cq*(R)H{z|b1XzvL09heM7(2=I8%6fQH(G)BstoQ`2|O#>Z5o+'
        b'W0*~-im0H)8J9^@Y7ypvMXWo%A^Z<T{p=ji7J6hrE<Z~6Rd_3H11&066oe?9Sa?E_IRNQ9b2@)?Bds_83tw>&t(7hdKn%&!&LUj|'
        b'f9qas{^DpF3>v7ufOq^uM<h@Sz-Mq7Xe6d+@o_gv?27Dl4SyFIX)+^C_1hx(6>`}TG+u&ad#=G)?JRt66###U7W*5>7!2a^MgSl`'
        b'tf)7?lwHaW@|eA@0cFJ?K_ay0cZkRcBQ$3OzozZQ>%4%RbFCNY*S*%xaH`nEO<1`%-zH>9ufv^xj4Qqdq#BItgM@EWXM4a9Dofb#'
        b'ki@@8f={ib&MuNh>wC_S*#QaRSW!j*qGZuV(`m}(i0B~Tm(eVmITHbWhNL}d0{ym|VnNr9dv%xq_ML^zI(~%Ux@Zg9g7-@?kD!S8'
        b'!Ja;t2=feD<~2wbI><s3S!gqzARa+0NE!f76OMjGx}X{XHJ9@NVB<ajb=eHm2Za>Wcq@ruqG~(2h!y`&m&|w=my0nm0Zv^)Ql4U}'
        b't`<U8W(giKgjWiw(?!H*kQxS-wx`plk#qHL{Hs;`<89G~jyC>P`0nA>TFTCgiSbHr;>A!Zry&PMfxcMiiW2<s#;NsmD9a~i{8uKv'
        b'ifZ&Q^WoAIl@qp`z!H4Ui2VoEE`u<@dJ<MU!{E_~f~KMkQxnK#;D^7imOfvr6G@QpdX042YAgLe+U&~!a*VQwG$KSfhXj;Ui0C;U'
        b'38Jj`5zO-=c2ZT<!#LU!Hn7g5(n96EXR;nrW1O{kaZh-2p(X&iQsdZHh{3Sedkd*WavAU^&phd3XI(*UB1Zbxct5k9Vfl(&!d0d{'
        b'j`<wV`k7?8Vz5tde#I0jKW9Cx%1N%K=*$!}GKKm=YGa&uo1!xld+Yy8=XQG13+8oX^5u<5Q#7X&+9`@hZT!D%N`M0k&)NYWMSO#E'
        b'qza8+faI@*Xr!<OOm=d5Atg~4QdDPO-N7$KB_7dDSK&j(KzwyT!f&miaL{Ui${L8{<I@99AtT{vKaZIj0Qeah`^H9~f~S%qiB%MK'
        b'OoC5g$9iFGR7ieOAtqR}7`_gP&3RZw!`SL<9AdhQt})W^bvvH1gi(bC;HT0LNT`Tw7IK1hhc(RZ2j*2S4X|4b1P`-D8%YTLg}$pO'
        b'+d<AVcwlodhHlx87+qncNZI%bphC}^NRC`CLI5i~j7N2)IOg+EOv5<35}dsb9{4pe3$4t;eg?sU4QPKc?w10)OL@lKkWs3TXliM|'
        b'Fb(00mmvhdP{O(5boc=tft!N9usnekwsQ1<Px3gxCO?K=r1i7A=or^>mxTYaz9suv@Q3(I5{8WdKN?8kj|Ep(@zX>psOo-!)`p9D'
        b'>l!>%KNjQ@8zEg;Y8ORWknP2Y>UM$6h^C8ps(*g~Ox<+XoM4W=LkcGfdigdK!DdCD0Q2cGwY)fG=L3Sc;*zM4hgC~5j5LK2aY=#O'
        b'qr&eBo>Q7>`EPQ9d51a7>St)5rb0^JC~#4lDb|xO%`p|C^k6((`d`WaDgf2ZVno2DV;=CteF)9c>t|qg(j**%Pe0?u*{lcXUIc7C'
        b'F!0*wZffuFg*oe=fGw=?2nz0m7Ob^rW02k#GXzIQ+RR9h?3IUd9<~D54PovNMW}V?0~l!CX4C~K9#~)9ctr6ZYv;zGjGH3oV}B0j'
        b'j(1i8HIH4iW`9uQaV|JgX#H$sP{UWit3J|j3hT7)-&o_(W&Qg`k@G&r!8>;Vv(w+lS`G^D502!BoOksmr1}o&F9B`Wc<c~4@96g-'
        b'@i$5TG3yghRUaJrj(?+d*Tx#4Xokt)$RPh5*H`r=@@@AT8w#vl|5AV+Na{I9TI)bdW7Xf2{=L?n1u*U3q}B8R=xKF7iMhk$HDQt1'
        b'Hdy~OfF{9KWINHG9uiyl5d1$$hWUiKgUonfZUf}L^>^#y;K!<}|3QYOybUv0Uy#-|4QRIK7#Wu1YL<1Bw7y!PcV5EWbjNm7ADW_Z'
        b'h~A9s_P~Rqiu^f28lQ*yh58xtCP4CX0C|b>4<P60De@8-8y{x;hdBR1{1Xy8M5Jz9>~SqP!V}v8XtdblYvT7CgChorw2jr{BzBhI'
        b'ez4fXNvzqpSoQ_T53(I00zVKr|AW!-svWFbB;x-Fc3+4DM@IQ)5{UrV&fo~X|58k{*kkM4oZyHpfYLqRk^WW0(v6EL@&Ys#gRWgB'
        b'iTDDMb2R=o85UXNu`)Q)FKliY2c8-|NBVPukD;s~^34QHF4b36|C<bZ_iYZW-%k>m8d(1f8I}n_fwW$d_(3CbUIL?qNu;$qdb&w}'
        b'1Ez=X4M7@>1xL>FZz8_Y?6xh$nuySX-5vq{WxGA*2g&@1i<)>Q5|&DcLF%mFsM%pr#92*n6iVO)kY-`I#5|C555CR$0xbUm7p%E2'
        b'!TN3rme+Gwmnm4UOvA!nfE88{e26#bUf^&qFu51_`w`=malZNk@HduIpry{S9N7R36lOu_y9y?v{Fn;VFb)@Ba<~=n4$o=Q_!;Ha'
        b'u-nnm2QZ_QyMarcN&c49J~FmQ)vo;?R%n3Y6ip#Vh$XNAAXEOb;rafH3zspC<F>{$rt$xZ_&0@%jKXD9Lz!heV0q%YCe$F~Anp-B'
        b'&B_uGWfhG3anps-djO*>yQ|rBSF=ozdmHAa0JNwWA?HY=g~FIc_)TG=-7xJ-gl!5wF?+B_<M>Kr>d_GG6c&6~EV)}l={U^>N>7S^'
        b'fIt(tOSsg6^}m5HMj74EIF!(-$W^$@<)ss}4_wMCW5di|EAb5e7TPq_s|oK>MDEbY>B1{<u?IB?UhquKFTjwI8);diq<pE6xa(?{'
        b'NZv60rt%RzTKy{YBv^|OVvK_K7tNFhkwDREkH++#8m=IDK_xGd>LO^a^|Xc@sVl|wu?D0_qbN(CN|Z^Y_4ROlFp36U0a{%I@A*gl'
        b'HqDC#U3t&zZPENXW&H<r5mT^<e@^uP-!SD(ydbNA?s%y8d>FtpMQN;28lW+wHPosH3lyT>zkOYEbtk{s(8w|Umqy#EtL5!)^f0}y'
        b'v3|ATrHx3}CgB?zxJ2Z;VS3B#cEm&ZVQeA1emM!;G@(*6Oy4T%6hWJd2%uIE(dtq1h`bK-gGT|roeY0RGXQ<gP8n5(T5YAyCO8oB'
        b'_vDa>;S`~rXp6_dAVYkgY$cT3S0g<#P(&J27$iWe4<m|`&z7)`yoDO0p+P8k_gxu^VeBZA0-a?rVV<9|bvvq(3aZp)xN?qSc@b7y'
        b'(u(%HMKdUBt$I{aTi@4Xu<G8}A$S*&3Eh;LNyJ7-w)`N-F>GRBJ=|wpsKKD0DhrVsr+hVOq?~;n?P*4ut`Se*f?ngb@Q3-tHyeS2'
        b'0S{4xNUifVI%;Z|bEU2n*Y5Dlr<D)KxHT3oT*OXo-nu@lnC9hrFM+W#HNQ@|vtb4{z~^_=__GNk#N9NR-*_#GtLzDCK=HARUQN@r'
        b'(}N=_jCf-MwKxjO?WW3&=Wi>7PXNM`U7c)$2|Bys@OSuN!+Ko~f8Yc!{e9R-E=<h{2d*sqfD27IY~(OM`TKlrMUs-&u^JXih3P45'
        b'EGYfOPwm&~t9dWv#=o3<WIES|hEORT>5PGF{=jNpdKT3(yYX7@;F#lppW>wC>S}&zLs}Yao@wpLSF3lbOZXkxJYbW;qRefp;A?`e'
        b'e1G<Iss;_EQuGJ^sa7+LC4AlU8dQee&gjtcod>_O_wdwxFyk~+Qcq<OaqDq4qoaiOLLK=@Tp)VIU{&qgsEcq)oAg(&GSZvO#t&&!'
        b'm1`**>pqUHi?Cn4!BhVP81z2U#J?KH2bnjS(k6U)8#K(h#1J(EwfRH@{2?Lc-BlQ$8Hl6^9_B6GQniE=p8(^gQY=WwH=2liol5{v'
        b'EI{!k&-B6i8SZo?n#$msU{o>`Dal5cd~to43i5wd`=xpt@_(JOYQqfd@Xy!xWI>@E$yDJRL1)rkkO7&f?u2mTzart>>?em%fzyNA'
        b'bj_)nb;&_At)J$&r|(lUW?|s~U^wa=hKu1^h48n~b`Sv^uFIoH43lz%rr+m3=QhB4#%!K$H7!Z`oPFlZ@Y)>ebB5PkpEJBRm3!pn'
        b'-0JDv-a(4<?Dp^BoAv8W4q5*CC-zgkbQdqUn!4zKW#K5M@H;l}2Sf7*&hyfTVTntwR0>uG>Vlr0&ah|mjew0`L_zhR_14eT(@AF3'
        b'hicfE&WOpTb<C7y3%K7>87g<^SfoO}N}&O^1Cl%`!kMB00|5RjP<(llbhSRAA$_$OIDSd1W0NB6cO&?BSJMF3NnfY-GN?r-b~34!'
        b'#?b(8xfY(H*ztdc=M2ygq9>gM?spW?^CwbaLQ{#JKax}X!ZG&yNdxyW^x^Ww!TxVx0%->HQG<6aB!<=7nyF=D*OD;@0IJiyez%do'
        b'waMPZ|1yM4e6RksFZq1`b(i}8-hT!5!vw@daGV)_UJaBjTqoWD*@mc{u2Mgs208|(p55G9E8(<23O1sYO)#|#juO4<`il3dwTIZ}'
        b'tDmt%>iaXRpA<fW|5Q8vsW$yn{pS0`R%k}RwL=lwBSMY@pz%WZ&S$hibxaMH9J6)$Ah_Hr@L`1?Rs-!tT!+x2MU;&Z2Y=_V8U>N8'
        b'fm%Qm)$;e@N$-gCEM9#g#3ZGlZf0}~ped7yL9;=g$sq<|-6g=d+P;?ve~uyXD*Rpj3=(AO9NR;Y=3&6byK;VXT=EVzeDHU5BvTG>'
        b'I>ZRCgE&RYh_3ft^Nmg{fWH!$DP9uBz+3z@>VaT6^*~$lq4$$q&M1Sh!cr@_?ey&@2|m?2!?iv^%!XgAXCz$6enQ3f#<-Zzr`(vv'
        b's)qrzkGQ&8T&F8kHZmTH;_o)_O&itHCLQ%^s;<SY!Gs=Yrmp>a)h5@*j$ZX8av_GHk`|APvAxM<Fz^l|{RrN+H){p*DcAL2PQ!EG'
        b'7h_}I8`v>fu&wvlV9v9%(D(vsc=C~yRVt-gacXkS5j6e-Bw3*z$l&L#ZeiZl@Us%g`nT25HPmaYjZ8rZhe%XQOLTcTMDY}9Sj5FV'
        b'XmiTdQ1unHu)ENH`lyZ80-CfOqDk1LaRy*~P)61Q#5V>Jo1{~#@e2k*`E4@H{b~e1I#T_IstRU(h#C$rU0Ol|Bdm6fFufs=nf$6+'
        b'c6xI0Vc)Dvq+?>EKU|%91{YXbnaZ|@+VTHK+q=g#b!831=bYTb(Ix@H)iwzR1JxM_RuZZ+Bt-;TXMk!1yfg_WgaBTst(T#Fb3z9a'
        b'#CZ_g3e?VX5}OhkGXmNcwak;CQcK|(vG)!>!!S)RYFkRxs#VXo_c=lB%=>%a@B8EXC)s<Sz1P04z1G@$tu?$9K{Bt_WOt&kM)fFY'
        b';W*r=e9vF)w8$poDGqs`%!c3Ab_GTlQc)fU23su461DB4r93cIg^C_Q@8#dIn55l!(mwCf_^$$fe@i=b#aG6c?L_zTx7=$kzl{AV'
        b'%(a7G+`i9PE^hx5)wW$!yd8er$=?yPp0%ZP-*X(gY{5o=(nQ<Q*`m2AjVtLJI(}(@+5*s$LX<mu+nZQJza<QCvn2vzmp$T_iP#Q9'
        b'+}n(No6+UeA$zcEDO;{7>ZakHgl=Lp9FRQqe3(UgkS+gY^EnOZuY=&+UEfs@jEjv+3iwVH?0Eb9WM~gm;fdUxY)mF@+L;!xTD?St'
        b'{jQvySYv1Qmg4T-$~?1~hFSu@=uT}`u#wAN;uM^)esUw2yATW#LHhUY&5MMG_@g}_f1W+UXMq9%RuWV*A%0EQB)NOHB=6m<!W;@Q'
        b'bEgH?_VUZ;$B%3d9og(TvbmqkCu(ShA^>3*KUR4N9fK|#22tVx2&hPrn-w(ta67`=_%^%vqbi6oJNRuRC%cQ&ws-l0gl}A`yY-nB'
        b'$ROKjS{~r~x=@^NO~i&}NYZLN!7(87j@&6e-bi-rYg;R7eyI-nvDlAxKPd=sEia+_D><VTP;iu*cwHeucvCa@S%*_(^^3<{n?tV6'
        b'9ye(2PYkVzyTBI%|MmiNY;)yEMh+YLoz4mZ(xq%4ZSXy}cN+luA{&n_uE+of7x!ywJ%9MiNE_+<njff@!aeX&Sl{B!UJ@ss-c0*1'
        b'mR@Azql0XMs-~kI{Jz@FGFjfV7wzp7^>y0GPC!(#k%M9o1>tey=1%_EIscH?yoyh_aS1NW^)`~^w$YrRxAAaAr^-z`0YL@?y(FhQ'
        b'>w=$8{wd?j7EW*9@&zaVx>C@Q*7QAvxaW7O@)_P8PlQ+LJszTX^Ie|uZrT&GX(6O=ul^uX?%COw`=n^aOW5!i2+qM{jLREK$?4qO'
        b'ZEIMV;RQ{p2PuA1)Vf^yQTEH;Y}a0C0pjvV`Pto-^Q5n#I_>7I+ReH7jumgs)oC_w)i7af_<clA-dWMe$LEi7@Xx`aZN;#B9n$bQ'
        b'eszT;zTtyp4*WZfKeIw2Za7v-&RZc7lpdjK^!Qu3Ya06|H+e}u@eqw~N~E7jJSkv#6J2mXb1$)SSF)j=LjWz*)suG!A57M6-QLK>'
        b'zueL&b8p>>Z^obK;291HQaM<D5rV&1Xe!uB_^Z7hgnUipCY}>`P56K=zzcr_rf?!>3z;{40@Y!g{b+8F2=FC`(3R+roZT<yHQWxc'
        b'eIG#sI3cM&+8cx51<ftcf0;i9XB%=v0iJR*>LQw7!<rsPT&Ct8tf>%5+HQU4KdqcKo~xS_9u83h8|W_~{#RtP;TG;0%A0`f5WLe;'
        b'HrXvE{h8eotm#3dK(_@<@r(7T9L|=l%eTMum$SNotpULWPUpDgzp0LK>Bvo&z)`XsG@ax77&LwBg-wQ$C_tT-MyjyFDij_RFsv>b'
        b'SclS|Fd-cOU{mOWO`dl*^^@Ji|AI8_fUxZ(+B=Z>mSnHL!f^9WM_T?-=&=I;K0`eR#-w;l-t>OdGq`C7O43@+JJIJNV^aK~EWopz'
        b'p`@RE@8aeEjY`V%SLDA<Az-wdg7EqyydKrdxhvAK;kPNTiMyURe1Zz_eCtp!K<QZ1ThuVU*9(c^AF1YlV%#hwxrK;<U63aJklcz#'
        b'5g9Pz+FPCDPPE0iJk=HMbeVCRt8e;Qu{jZO7hMo~|BR9}Pt)+_7OTj-9x;QtSpnjGuWb4>#=Hs{V;7U#d=+e$&eOSR(k8a|;L`dR'
        b'LC4{pmetb@>Yb0^3xnHb^{bGEAB|NRfD@}0zI+~Vv&Cnib`H@BsVY@TfK!O6VhT#qVw5A)Ta`R8&Q0)(=lM;<73enAERUC_a$F^D'
        b'E{<`Vsd|!MUx7$pM~384gIv%GWhr}q<s7gFW9dD(0~Q9|A)iG(TQ}L*Oh2mGO&?H5!$feq2sEhID&tO2pr#o(68T?4T%W&%eou?f'
        b'siw(~u{pH;oKv&9GE&K0wF2>`ASB7jxWvj>#?DTR>D#bLHY5xGf_Ah@rZDbiGk?2@J}riAjMU{x*q{LnFLWkB!;^2jybq&LQMGte'
        b'sCbj-(M|o{J;V$=xz0*(fvckXz$R%m*IiD$N6!+5C%WQsfupOj&9SWm0}DI*BKkJpFTkTn&+;*$Mb8F#1np&ri|=UTOdb;NUA(EM'
        b')8Sd(@D-p>94^8SpESD#phaY)MaQb?(=Pu5%AJ%Srd}0FZ8rk^{7L%A`zsZB`{|pWeb-4W*rX_!m7gtyh2<%mBJ!?Q2s2Z@3CiSH'
        b'gaY<;{J~9l{Mk9}i_qXm@SPlR%H-a1w!IR}9rZdogSlTjGg`&dKb)DqF3WX$GyW)^eC$kyOWgIJju&K^qD{e5XYiOGwJ6U1iq+D3'
        b'@#~fs&PMA=bpNkF%80Awg|Aue=tFak&m)A@OmAvn3sfvkG(At@s}ym&j;1kaSsn2S{7kSm(XYGeAn9OxPUz<n6g;T5pNR6NBGA_^'
        b'EfyrM)HVE+?(*~9DA7a<dcLh2<fT`G>{sA-(>HbaoOCPXk+_+c>c-}zXVId^%&+SPnQ%EP^UJ#QEI*6b4$EhL4gse4F&rc6VS)?A'
        b'=lJ>bJBrP<j64z0&e$>xj|olGU0~rqc|#)QGH!rPSm1Z!uXXs+7Uv;Gsg+(*KTitLNh5XNpRR*xp3yojnocGE;R0*ub!Z5j;KB^4'
        b'iE-oa)P>%u^So2nPd-f;Xug7-KSd#rE3DC1n7MU&uxpBVMqKFhu&n7gK8JBLWw}J{5#D`k7RmR<efj1^JO_Ste?HkImTVE*OD6mF'
        b'z_pS*+CNl6`~j9q9<l7ETAlLO>+pD*Eo1c2n9~PSla+%QUK?O1DF`Rbp56ZK?3*8=s}4_q1YH3mH-;mJbF9&_I+j%e9TwBV>i*Xd'
        b'Je^nzgQFFxF^Z_XWgN&b?umSa{+?FV(F&lqd=nIWe7sV~{f=UMkH}xB!-Xo0XsM%hLOGdNs{pYK6_rmV60ADffwXEtqImpwb)nyZ'
        b'@htTGu8u%y1}Twvo)#%@ufs9z-ZX;vT^-HAc|$T{Ck(>C4m$99E_u`&+Eh2*Q$-$h5;tm@M+7SeF_>q|Z0603@YeD@Mc81F%#p!l'
        b'>+E+640zVph1S&pc;owNU|%r6z$mVSdDhQnUdIGP#O*408;E*IQnQs<15+1t;o~doLMuRjp5eYnApw*qrR%%Ma+0LugxAsI%s3^J'
        b'otF{+T}!7&-_^e-5r*y~(`E1ubt%0thOWM;nFnu-0Q!=3G`7jMjh=5Gx%#G-?;ZJ$R5eQLACPaa-Fv2%e(;0Pl1pUomRiLTC`;-P'
        b'IGh=zH>0gRBUD!_SHms+2`+QV8fF~*8Rr;996aQJr3Y}wZdu<^7<A)M4jlzUQA96HISW~ycj3<`QRGm@xlvg1-6;AYPn#lx{L_6J'
        b'It`a*b!Ld))b5qm(TP9fw355-zE>61?Y&<0vlrfSyl!u96|KHBD{f$PnOdu6b(@q%=<j9k?OOaIajUlJEOq}rNl>n(hRB2fwsbdf'
        b'n%@04YM0)mg(%4f?&>LBt^Ju&$}L3zTX%^VfcfR$)h6GF)X&sMT&n$9yA?LX_awmUpv+IipXf55|67^KTJ8*#^WZ0xtMADFUK_el'
        b'i_gO!2DtWrY8jmS4vpMCtqlO~_&kXMnu2aGzHE#IZ=i@!B;Wgy|G(7E-t+WcV)YKPJ!7@uJz(9$E1#gqODr<LPHtWLJE9q8OK$NM'
        b'QVi}sQycnAZ3o{K-zj%z5<|8492miqc6&OZYXRZ}%)i@19AqjV>OO}@fv6{vd^Ga^N4ga#BX0!%eUbl;+Sz-se;~>mRA!)7%|fJ&'
        b'sP1sBnnX(HBRYSrR$cs9qgH`u73#GTjlMO@Uq8u0h}U6JX%8p!K&>~FR{%~Qy-BP#NisWYnFyj46VKJsyDg7+X*SRhsd;<k|34!C'
        b'&(c(*85a_JXWN8i?yd!A_8)3#8H^#3Lu-Qoc9j9b91rV-5UW+v!eXK}w6=D9zm<H$OZuEdxQ4+e%b*4cv96YJ^1dnZUk?AnUsDC8'
        b'Qb29jPqL9Gl0Z9LHO%MVMzU2!{(nPPSqpzB(p3_?B2~i0?WqbBFCuI()wejJn=H4~W?E{q`(v2*obt-r76pytoqEtMCb2`(Tn?xf'
        b'h)0L6H!-@eOn)pNB9>;vr$FU~S_Ou*&R8zRw-ym5*euU`R?83qh^_EaG<<}0Ksf%J+R$%m`#mzxZ)yn-O_r>z^(qkQE<};e9hLY#'
        b'V~71%>u2KywV^za?^j&fdAKEo<yl@!6wxE_2ut}3mRw((`B<$~h>q)OLpdO4e$z!N(!N{S{Z|wuV(FmNBpUu6q9%ooe!GP7WwLE='
        b'D{w3gmEWofplM<PjZ9}k<R76o*rHk|i83SL`zVo1QHcCOxGU8(oOX<U9*y$7<VJ^M8-qBUOcfZ)d;;mR*>qwa1Umdbk+W*y6OdOU'
        b'9<@UGz$I4kdbTdM7J7|+0c`cRPeCo4*AuK29BV8FY6j<sFJbf<tDOUz!5Hy-Ey21gmJmUxYZ7r|o&$6@jZJ^|y+eT$jqU|=HXDvb'
        b'fdnqS8kpbD;nYZl&^GOVCJ@(abPv`zdPIcES~3p=WVuC-6_3DYAiAcSlBOCa+9XGG-_<x;g3XH|W2Pf&ih96L_p!}=7i$3F`3gXR'
        b';V#hXr*&V}02=2{HOy`C#mIk8&D{nSqIh1R7-tvibpKPM*2(lHOw<RDYH2h(yab>qFfrPaw5{O~Bxb?>`WTkA#$fq>rJ6>;c!c*Q'
        b'=-#VY(SiZ;w+ZTL!7Ju{30C_bxsz1*m&mLSC*t)QCm%6<0*7pn<&z<vvo*dyBt+~5EkR~=^E2P9!MQtFc&zNL;7V@q@_n?6&G1i@'
        b'?rqQ&%kG2)aeO~(kXzLym^bZBK?ga~3Mzbq0*tUbftIC$y83HqRbkrxdT-4T$$?e}_E|t82>2YcclUigHJ+XtW;pJ?iT2mXzGj7A'
        b'NZ^?{p4V$EFC@f)fUhRpn6SVc<vCc>JcWVZurnds%=dU}L}HoJnXm$cNf@>e32Q+9Kh}gD2{gXeNQhTz8iq0yqRg(E7H4x-j;FH*'
        b'Y>V*oaFU)+@a(TqJ`V{pKL-9YU#x+O@6W*muL2D>Bm`K>2KuuC{72d?Z>^yvk7d|ORz`}<Orr21aFeIlC9)P^!%4`sve?x4%v9BH'
        b'lCrF)raWym;q7!;Bz0hI>RF@J^@Y5#M%P$Fo2c+O;eP?U2|+yDYb?)zc7Y$yGc~?#2?2I^TY~55n()&J`Io`ItFO`3M@nsFN<r0o'
        b'#Iw1E_Td5&p=vxL-%{h*LSGUn5akvKa7zMFS3~PVe`(`*YHGrp5<K=Az&S!&bA8odj*M`Q(%~F=tTi&d%vTHgZmCP~Y^)KL$ig)V'
        b'^&z8Y16Ul&ngqMgn~wAg5$RggVo&g_s|i;p*kAJ}f<I41jj}r7ajW&sPfO2;^ruDJUph;yr8n6LuHh6%p@>N>#fIY$&*L?+K9<Fr'
        b';3=vJTR>et5PYJ>Vo3mB!W$Fd)&}9i8d*OpTnYN1+?e25Q6oFbQo@*}GQpEqBRj@YnqkbG0Bw3&qxk^7)r<{)Im`Pw6)_8U?Oj^a'
        b'oFmx#Xw9Tw+|$`1=uFwGt?A4f)exE*_hTwaS|z<!KwfKEI#ege<K5AOx&{}zQ$XUOtS?;Ry%{x=Dsg(JN|2V48ZS%Tkv4DIYU6{P'
        b'EG`^#>y9zvJ3IYCvkBS{lq+ivMW;PB3~{zRr6%n$sGnv+ToOFljk@%Ms9Wq(1DxrWr)3h!HM8^uLrZ1G*YrYRF*wEn@0jtV44eZ+'
        b'lR|`C-k6jHIG)CDrSlPANdm+7tcRL(*HV_q@fzk)=f@i%@5ig@Z4`I8@F=|H*_MY2_!Aq?Wr<Hfjk+9d04rxLViThq>3Wk+KJEfk'
        b'&e@HOd}#P4gEQ{Jy=G_NhG@7y*#EC^-~1We{(pgcE#;TGf7l~hMTg->V#3~=C2q;W1x}LxtP5b6?sl}3^*B^7I=FH6-3rcaxCO{F'
        b'F7YuOXYl_K{C|#{dCsn45&JjNoXVakX+Pc}`3l>A5}K2ItCREP32b;VvcufEz+Zo8yT5*?aO)YnU%$Nz8uanN6_3Z|e@pq*TiurH'
        b'iY>cDTaL)2Jv=Y=K%9N!<iQ{w)18H`<hBh2#~!%A%RL!%qn+}v#WN-r@ir~vKs)4LiLYnAp1vgK*LcE@S?H_WmhHQCYO$RXnwkv2'
        b'W@_{SuBw#y6Ww$S&|skbufxdj->I9w!sEZpLiccY?cB8^|9eVj*jTc9V<A>9Y5JaOeaF*f@9VUWafw$W{qCY~8Q!MGxPiHYg8W(8'
        b'xKD_LISAAbW^k{(-R||UKEW=36S8dVYqNXW?B`90Y(_RkN{Nh(G+!O%$0k57v<Z5K@wn|i0b=O66R|Z%G}#&Z3XHl3tRsBsj-0S-'
        b'Fqb4FCx}b3b1+b!<780waFAF6L6Qf9#4bCY0LBa#^eTd08$fIJHbqcjLoL5aoIPjcPus!BJk5*-pue|9LOA{~vH8Am-R#W<Jez9m'
        b'I=ekoWACfAf5XD(EIpCN4xfYeS%vJ9r|f{j=P)u(KZ~$1w<CvpT%3}Jt7sm?&nk}S1kz8K5*pqpj=X6~2#?*tSz7k2yokS1nt~9k'
        b'?QX145=k47xG+2!Ny<eIcp7ff_pixqJsIa-5ufOk^@t`r#k8rB<jAG5JZ7WpUS%CS<aa6~@f|p1s?uzbi*rR}QcLYxNkoQ#$0y(L'
        b'N0ec+)8MNSr#+e&u2i2&rZ46o4v*fOX@{mIqAd}Y2XeA~;Y!$-bSbok@XyNLS>;TpU7G(Lv+w*^JAg8)z>(1RkUjGFDFN0xTc?1j'
        b'leWcwE&>xO*!_29#{DpVWMC@ANKhe`r8^V~barmT58O?=OIP^jM$$kpG8EtoysUygGcmwMnee&zB79vx;Jr`S=oJTB1&K!&y7$Lw'
        b'k8vaD?m|JNw`e=YqCd5@v1OfN(j~h0flYt#9IFK1L_hn+0Q<b!(`~(%9h-$?>_q=9?`PHbGBQc>85^wAC6aZbKg%nBxSH1X$)V>^'
        b'K32`>){a&OFc%*xp-WZBy*G<a1rK0Tux}Q`i-^+@g=F-IGJ1k|G?~&ky9WQOI&D@CwGxxRU9G`zY?L)`nz8ZY`-zfvA^xX{w_x!e'
        b'g{F~voxaD0w(TLRuBwE0eMhPb*rROPd?VX(osy=r{o4jn;!lidwgc^Qxv>thO9K8S9dehV&Gocf(UIv=g9LSl&ZP(c`i>G;Dfln#'
        b'FuBa&-(2uQ{zbYjS-%X@bJr<_9J_0qQazw29F^qB;9CQt@%HLad$p&%dSMb#4Jmx04c2_9o>}+u=4ur-3W|aOF{n_6&h*!}?&=?k'
        b'A(~-Mm6KU#CPcJV7G8)1d&HzCC`v@aix5$!jQmXYDr*r7k7>C6@nS8`-kr6G{qc*d&*{bK@JYZ=i!&DMf?&O621U^bj;}}S@Q)8H'
        b'uWHAJvyky^)uAob{p8LjF(Bk@k^#Nl*ZqoU!0cCazal8tmzBB|_SNO3NqLGP5p)Mw#!BU&Ns6RA^(oPCm>Nh+jj|<u@nyewe0_Cj'
        b'J%Ci@DXS)a3A;JDTYLgq!v4Oz`tgBtOT;%%+7Dh&g5H;XHxjQ$4Lp29cs%{OU?AZ}&drnG|F-&gQQvQ?TmIvCg_AGFqmJ9(ikBYW'
        b'Wrrs!&dqtGy0LC<(rEj;BJMe=y$TzuVx6x-zK&CVO??&j3GZxn#{%e5GjnnE7{|q0#y=cC{;TSc7BuMj;m;_fFV+@3ECYospHM>!'
        b'SQF_<Swo}q7wr3D{E_NV2FTTtKTi1@2HEds6KXi-b;7gR(w5t~r)9-&$OxYqs^Sgb!r8+-#NYV%lhPKX|5QBj5X?FeLrAO3_|^RK'
        b'CO9nf7rZzzZ`#EwXSw&y-hD%VG%`aY)VX;^m|<u%#0qo4?;C;@DUhw&%B?Qr8DhD8m#P*P5$QI%eyN>1h~c9|6RcY<sMani%vV@B'
        b'rB-gnu^<!}P%z)2XUm(UC)oYNF~ltxm$Rzr_bMH*lm;+#+NNsWA`Y?7Oz%9~BP(9VvR_ZLEeHQqDe|)4=l_EOL<u-fNw`<w38(O|'
        b'^M7LQ?uTcnh8cKw3h#5VF_zbZz1>e-w(Y%a`-*=-fb*OG$nknO!vZMv>wZ`{lZH<BIJ*Co9CV3W_V`tkE#e-y1U#SE9(T3$SiYk#'
        b'Vv<~78fo&7UjKiy5ue&*uAuxQo1;;#!jcr}s)%ip=g_n@@^dyD7PN|u@}Nk9yo&aX*}#b}AaY@k`bKTUi0xHjuPX@3CKa4JE&get'
        b'Y`zX+SvtS`v~3xx!iGk#t0cP*rm^H9TUxZcxxI=<WIzDpf3e}Mv~WcW&uv$8$9Axlq8dh5JSw$UtJVYr)m3FxYr0B1)_~JnHeWt('
        b'x=iB79$ify76n&}4gu<<+b16Xvn}*zTR&;`{Mklqfy7kv$%Ic7AE!r+_t-*y@MUAub!rVbnPpI9n{;xwg8L;kAS_FCrQ33FfqOx9'
        b'_HkZ$T*al^tUAt~sLmA~D^_R)$s9bP>WwFx<|3aw^s&F<>;qpOzJw=y82~f|E`7(3;#^~=sI6_=<r`lH7Qf@q>>UjDz7cfP29GCx'
        b'Doo~7DY5)>RM`SIR<0<^u9lRm-Ms2Ju#u(5XS^e#{C6qj9hK<Zrr@4A9V>QINu8Z5ppg?${u>-nsgQPRu;Gb=7(u|L)h!W^@3e(>'
        b'+WI})JUeZ~64+1qcAJ-krT~c@OrAO8+iamNAkVY#y)Po)Y8ylYXc|gvwcW%0{Uj~4U@<fr!1Fb>y)`zxsFP2ORqeIg+HDB&sR^P='
        b'o9z%EkX}ONk9Y5}{%Vcz)!;mxhxAs+$aGonqcYtFo8c-#oHgw|YjU&OH=;B$4oeYROc}fC(ePU@V{3B$Zd@&sF2Cc8MZSu;&NgmB'
        b'jcZZzBi-~h-MJ5C)7NCvuLgS!y2&qexOD$As1h}KCTJWDev!;ET)rtie)D)t-*Vd_wm-=g^-&L}s{?So&03gmWMpLc<+srmCmy>%'
        b'gW{Y;{JpQ62%o7ZE9Vh6yE7)Ak90=8o0Ps8kNI&4rYDh{U!6-0<}Aiz7A!$=c5zlPH!BFA<b~%T!{;cZ%@)MxRcWyEBoeF$o?9LK'
        b'B9>#gdP6#VqdKZQsjD57gSTrVS&IZYi)pr(wsZH84RR9?(${&3HfIXbo&wM4)&b==6yY@OB}{HsXEfj^;%xMNCh=cZjl}VaGvk+;'
        b'8Cr*9cR!#$_Ge*We$rLx4}%E;ge)H4orO6`q_;l^NZc?ha)%heS|#D@)LlC>77@d{5g1)NRi$FNqSMpy=x#NNvszA`$YRRreyRfX'
        b'U#p@e;~>b$;b|efmQQ?NHOm9)zK8iPSJ4vjs?6`0tSU&XXjsITck?N;?kp27iXuL*iqPHvsJcgYgFSnQpB8`jT@JMTXt@Nf<e=dn'
        b'D9bPJkVSCq5Fb|2g!1|*Kp)6n2#%kt!jqd9qc~o?FBt3$o}Htb=V%3_N%K<B7XY-!pP_)!91!j8ck~{0SZ3e_6r}sEF*?enq$pbw'
        b'=T%_JhInX7nN9o!uISbrm4r(h+ks<svdYhI?ZM~JcZusPvwb4ofa!qWBn)@c<h@lctW^ca8&4#D3)2r_hKqOLQ-+%n8>YV7)PxX_'
        b'50;exU5D2rhfv=Qit+Tv$d$+{-|hQsXlK4!B^#3Y0m2Jkp>XzrbSRqk)yDf-W7r_u_X7nXTM8hJ<1-?(l}d)*{gGOREfP*#R9>Zg'
        b'`OsvLr4X4&A7kMU<B7@_QH6(ND1w64dD8(F?WtXwc!xezkfC%oSX~wm3ZM<o@>8B&Rlb||`BYcwajx_{uR7FEQpd%|(V38FDwJ`7'
        b'`$TI1v%H3^7aCePeVeP2M|^haN}*K9DHoO}Cgc5~_}x9k2*m59d2ywvs5CFW6kSxBmspA}EX_+Oi*Dr<#+F4_$CR_nScTD}oI+MX'
        b'N+~Ky$}3DM2vy`2hK8pom4v=Tr}4)UIaZ*@d1jK7vPJc##ib-QL-tOQ=b)3kL@M#y3%n;5f<^||;V#4=jA{>woTQ`0-B0!g_zUsG'
        b'lYk|E*$8jxgbQ(RXbZ6qMxei+E#6QD@gK9X40xT_IvW!~UqG(eSTW4`dl(xcWs$4|jGjkD?PxT9=k1xXxx4$lq4;)__Pj|mWy&E^'
        b'OtkMT?RmLoN}e;3?!@9h?wI4n61%lLCzjCTYEDa0NrtDXf|%j6@T?Ds?B}P@qeEz4KiYenv-<*6p?Muq$QL`&{uYJ8w3r)W*0moy'
        b'oahpEBp!(Gj6aa(7Pu5qF1NzBS~?79?@lcLCgqlJZ!&qkLz?g{N}&)+>)Gm|Tly4ada=0Zv2%;X0NX)MPMz_XY=tCBfBLZZbY8dw'
        b'zDAWD49ag<Nv}@U<CL$q0=80d<S+<(M{e~Tw3J9^*GRtt^A3q}KY*rKl{3hCupV10aF*JVFmGCaMiXE|q3Bi0d?pWXe72FD#x)PK'
        b'HOr-0d>l&);d2xul_pM$tSmfva1L1b&jYf{u#408i8Xmdxm*fX?Pqwku=?)G%7QD)tdBFJVypBKC#o96ocee$_m9Sd0ggB=SHdTX'
        b'R*zF5Hrixnv)GJER3W>9J4I=toBj?BiG55VdZk!#<W8<a1iiT`WTqmc!Xj2E<MoyVs7`vy2))KDWC}}su}`MeX-l*w-+zM*(%J?3'
        b'2i9i(Fqkxu2U^Gdkn+me(w1qBupsdOSk(t&v}}zjDobm!ES2V8rwVmo7i&xMA(HS~5}G1>uvfvFwXCl+q4#jYed(6U`_lbt_&OkL'
        b'K_hQzz)oBujo^b~$6{#n^EA}h2Q=cS#;^9(-B<R1^If^>zVG0Km$(%~gH@|`W227|A8ouxD+I9cFK6q?e8#FsK@4iFZ;RDSs>12g'
        b'0~N$pYg(dPn3kTFlU9^gk!DZZmDZBhb%>>6Y+$JL2kQL_m(Zo6RcDC}aO<=dfn9!sLLxSSZL9#xmO9BrXvbQ&sON-+L~h?2P>0Po'
        b'Us@-GTErvlox+`oJBxN!?6mLPwX<bs*Up}u7kA#Qw~OlS3EK4MgaFF}z7*Q~`-s{jJn*KWf~_fSWmQLOxj0KJ)#$5BM_JW+jX5bx'
        b'YliPD%nF{g=~nj3@y0i0-l1gWgYoKAB*4`~<J?IWl7ERpY^e}O8ef+=O-Oiz3UHMVNnI#+`ku{d;?7g>o}Lt~gmTJm&2J!=>zfAW'
        b'@`5fsAiY>=sPYmx+HTqXs79#S2LKPC<b-Yv13TOTo!U=~biCj~TLtbk&`MQjyk?vGg;AD!o9o3Sm;1$e(|%OiLV=>uplHPJLBt={'
        b'MQWw6L}HZ|amyq)_khy%$cheudAVee^SIX+9bcvdYp!%Y;);=4*zQ=Vja|+!GY8mFtIN&GzW|(Rkw^>b-+rx(4VqG_#3ng#ey%-5'
        b'Ux`j!1S2xY4&(7Ec7UytOk%WA0k=N?8>+k%{2&GM^QWox?52pF^Z+Y7g=iG(g@;dRB+2i(Qku2%lT>LbkE&?vCx8pl>yef$1q*jn'
        b'h>J^Q<yjG%F?|;-UeclDO354<oanAQ%BXm!0&V4M<J~N<G^1UZRx--hVlIVawHOSFB3HHzKv1QWXC*1pQn=sH`V{Q&X9$sF96EwJ'
        b'dPFYl@QzPZxM2Uh<jLdW69bAUJX?(qJlZ>;>wbkj(r-A4By|q|NV(#<SE;);Vbuymnnim_)2E;oc6@-PM5N2uG&)6Q^(P{E3$S{U'
        b'lAdPceB1o>`~V+MYPj7jO_}TvcfB|yz_SlToiD`KM~${5xxh-_o_sYBB~?<;2s~n*j~Y%u1rWCKP8?|Wjo6i3sq!c8b!rhif7TvL'
        b'!*#VD(d*GtJyx%0xfO1;TkkG)o89$;+yhelmUoCxd}pNPR8D;ygsSH^&DuL)HC%7_S__6vs{mVC->#2wPdUvGsLdkpP@eKioZ1{S'
        b'yZ0aOPj2-dp$Nh<YYUe^T<V6K-5tvszV1{9&}8kiZjQ4^;2lAoNA7@);L-<Bx7dlrICXqL>>S$aRm2Q{9lmgmt89$14-IBb4PhOc'
        b'at_5e+`ygBI$53k$6Z|JZq7B;PChrrYPi{~O{NQX2>aj5?RAMesu#|2oODbI?t{^<m^(ybaJ^5*8Ak4O%($kk0@OXzE|Dd<k~-T<'
        b'W$vknPB3WqXHgydb8zQbQL9a*XUz4<3oTGV27K>O69pElfUVWvvj+(35B=8$jc`Drc^d4nWx`0!0DCoD_nJlSDff)i%mU*UzCgjn'
        b'4)0H98g2vx*&QjGsZ#R!;;hQfnWBQyq4?}$iL|Rbj^%3HXoU;4syKx+G|Qa_4g#Du8%dv?q4@x<UZKoG@z4hhE5NnP!~v?Rhf_eL'
        b'&c~V-A&jp+-?wpwbU^_1^&s_fR6mplHvaZRE!6S+m^PXK{ny3mC9<eIeW^?@ktczFx#1=UkFm{UzYOhM<SZ_j%032_ZQ%9=d;SAT'
        b'k77mpqIPC4NQ0I00^H7!<zie%=<+TXVO8;*0G!KNDsxKYQQMP1NZxdXvc`xR6F}jQ<D`i<*9)5fb_C2(+q)5;DSwND_?#Sx_(-;V'
        b'7?*#6LKv4S(D%h<N}B#-{`Zu23R?UJV~~-ttwXIP)Tj{$d#Bo?-D^fSF5{nnS9I>t#<ty!)gebC^o%nRf8x_~yBja?M_o3Li)$vI'
        b'Ykres`gCK{Lx_Lo>=dba+Dkr99<Dqz?mdF`oZd6%n>oSV`-(5^`;tH3MfCW|!NvoBy1sXi{|#r19Y8H3)F5jN1=Hz!n_4F9UUC#q'
        b'z=g$K&@Xl8KWyVwN4-gnaP+-H@$SCxCvkPciJ}hFnzj&HuK<Vchad$k5tddBm9L;Hzc!?Q0s2;=gnn^9MFAS-=50+MyedV`^U!kv'
        b'*?H3g;ZWRp`2(#LULKaybEwZncuA@|p5x^q&0XgYJc8fa{T84lKt|%l4PXa-^1b22Pp-YNNB#qe-qU{>9r5y5&0XD3C>Fe$+4KPN'
        b'#BKoKtrxTUd93bN_PRoEL0I#eyP7_ZQP>E&q~m2#Pv@xC_74O1N0-O6d!v@$bRHs??iW8*d9?8I9?pZ&xNXapZD2pto6zc6N}rP('
        b'+?LV1jd3>_rba6ULZIs(P!XTy1?q;Q8H+_YZ+8|h-O?<}Xlit1Yy%r$`#!$@G?u%haeMSUdShz<R?uXPaXvc<_SVYTfnx(6iUp9-'
        b'P-xX43-sGJ6t_}nu-`GuW38!H+l-Zqsm%|V!3MXQOJzw}X7c%}ed9KD!<XBo7`Gn5xv(U3*!34!Ffpkf6wH3KdJ3!#%~bZA823Sh'
        b'u6_rNSF*%AvY~&MjGU8`Jmf$R&f-3WAO^!tGuSbp26@vLRFXCO<wN=3QJT=eR4OY+EsurXd^uWOcp%Ooj2)O71Eh)455l)JQ-FY&'
        b'(&(%yJT=%WS?W@m8UO<S^5MTzh*>dLO+KHoq*85)cOIeCBz$~bm4$IL5xTztj_+uk;j;%on@88+(uV8#X^1tB-dvWyPzK>OfFwa%'
        b'>1}2CbDZJkm3sLcz=J65NOzo=-h(G8L)Q;`Sh%z)5kcyQ^2S)uK^4!}Oc@eq28BZ~68-}qqr7M)E>(8Ly`5-A)q7a>_dgy`4e~)V'
        b'0vx9)@w_P^+!N=NC!Uul7)H2Wd2DJrHk^-u6ANA#XEe&P-x6+li{8J-C{R4BX_P{&d~Em+uv=<V%n+KXCaHcjLv2E}%;G6NAJV{e'
        b'ljsY9{RMy<E>8B#W11hu@(F0mt(TI1_IIs%rLgHa3IWT=Dr#uV2D7@0(#+J8&t<=b<!`4V1EuuD8H#Sxt71Om-v}N9uf`cp{L?Jw'
        b'07fiahIC8k(x|eBGE{(x;eJN}ieD<_z%hZRo#k1|Ff!>yAtT^(#~nVA)M($ge?WO}7}`w<mM%C9?O+%xuF=E5JY4rtQC54_@Yht5'
        b't7(R6xH&vd(c^!RYT8Rd->Du<`WP?wm>6g4%_4B99#^bK8?Nce=x1MGo0kicRu=%uwqWtXIpADm1F8yV8CvG5<wz<E8%{&|{#dC7'
        b'CyN&e?}}X}lorh?UM@3#hJlp}n5+79<h&QDU%(n;oj3-T?Q_D`n>f2r4QP^`vFmw^pXxoV9egW~w<A84x6pZ(-7I~q0c3%e6rYXN'
        b's2fhNh~{T6w(E~vU$Jj9=+9|ty>OT&UU#Tcd7Ry@;Ta0qp-JU&-*eGKEjTxuU;fk9pVsL=z_!O=O%oIspfR<aC-Ojt7~Ro4^^s{U'
        b'n*SB0LG|Qqty&}2>eVPe``CkOeN597)$sX>=$EW43@}*@V5c{INP$5@hu^14>MHZkQ%gKZ!HlQ6GL^lgAS;!frdK>rN<O#Z4R}%w'
        b'(VmO|+Vv4}20LmaQd5&{Gb>&efpJHnQOIY(%AvhaCT(2F<<3wdaC))9ifV{6?7DOIpM$9PRGwuGW$3vr>Vwx)mYtO0;w>|ZImzdX'
        b'tW}yflk%#LogQS5(U&|s;vjXd+)hdDcfbte!ltii8esry{T%@Md>mAijL>?TQqQj{4_9i`&Lh(uS<MOZeg*42Z}@j{^eWjIH_#3s'
        b'fd$--3ju0qhi#-2q!qWhw;2C}h_rG6s8(<0l{<YmsQ2mvJmn3_^l)Xv%{5CNnD&V)?B`w=8+(G2J>tiE`r<2n<*|E&htnT#DHldr'
        b'Ugf{sga!molepa^3Y(~QxhTro{_ZNLTnyNLvx4h1bEO83bNE)f3Ym6`yE@Lf#ci%2RMKpEmA_w_=zVv({oTV10LzmUC<tIM21Jei'
        b'py{?5aQwy|r>V?r>=Bud95yl>zu!_CYcorw$rY<`E>yviBYrbvMD0D{zfy)>e7_l>9%GL~X`@<42FwAT{iMYf*CYmT+ZBjYj!SnY'
        b'wjF|=vzfYmmPp-~Pxy7+0}EVczhXdOcO~^)j_SaU^E=}KCnV^Q06tXUmK;);hgT)#4Np=X3D97lJIO8Rj6cqY4Oc5L!%;+S7Jv;I'
        b'rcWlX0tNM0o`OC<T5ta2L-Y8D=DrWjOBWI!(bqA$G6|fXL!pKrekRz$=Zr<cQ|MW0w8s`wqY`_THq>;DN@YE)!5W%|P;oZsc?RN4'
        b'VO4doHPOR2sVOwN9~I4z)cFwL5`4QUaC(8fzn4aHZCPuiP#>^N((r}rk*bbZfbh!!4!R1>YWvFKz#mU(hyx4fGf?WvfCQBPZwi_y'
        b'BMpsJvBHubb45i}EY<}0O;&g{Wk{c4NUT+Gx$%6ZajMb)+b}fk=`uHkDCGX843Rq65hth)gSJFLTR)=!$KUi8g?Pa}e1m%8_iK`&'
        b'gTpe=G0-dSc?!1iL|N?cPZXFw%ziTeKj?ihhCyMX<+lK9DLkA5H_bw&{P*UGXZyCAy`)I_aO_Huj<)U^<b;2^vxr+btMe`Emkp6@'
        b'$Whe6LEqg!M2ZMI4E7Jj<E=!Md6v(BcUnUv+HjLFGdYuS!U#i;_T$OK`up<1yW~&S-IGaVTFiZwW_SZFfKt(k96XV@2>Dh}{t$n3'
        b'mp29R;mE8E5#(QMrnQOs*TQ$en7qua!bZWKB?4<1pe}4h{C6q^H}W>f5RHx(n?uEBPl>soY$X1+f!2;WFy&JCF*hrGlWN`NN^I5m'
        b'CCtn0KG-&BNfUtl^L_1vDwoZ4okIM~;fp0&&<v<G(FW5z*=9VxL)fZy37lt9H&!Tg1I|Gk(>b3hgL4=h58MB+IijrZgkRu!JVPB2'
        b'_NAIT(p^#A9kHEJMB6&%mGO?Xk+&*)q6SpmuUzj`0oH@|m(u$u8Sx+-)z);saFq6=>Jm0f*#2}d_x{9)o-SBumnnSyff3rlio{Gy'
        b'11=}xkApG(U>zMBEy7RJG+fkplo`-PQH0P;8}M7npSW^(A3j19!A3}T-PR^*IBCK~tjp%h$F%8(IPfmBgS}spUN9dp71|h_4VZUu'
        b'ifL3U_FYd?ad}{NREnk_D9wD3eLl?$8!B(B=CA1Zo5DhSO*7DAP2Y*4o^MPzMx27eR?{U@0e3+RHe3SV41Wug`U=-hg?5||H2^LI'
        b'mP|F$E6PwIsh2;LX<sM*yD2AIZF(qu`+D~FeLS$r^Wg*Rg@6?EhRO&&?1TJcQ@ePfOm<~KCnVtHADZa!c_<hz0~LJ;E5ehO3W+`I'
        b'Xy{V=PkTpA{b)sp;CN!Euw5R9CwJzw%i}wX+R?S0>Fx4)ZEfuKA|)<pFH-Gg8EFf<xPbI3CvIN;v|X=+($0<Ep%~&igm{Zx-oGAG'
        b'pOUS_xF1nGJ10o{j3GU`{2wT!^>3bjQ@dPBc8WYX>$*FK@Pwvssg7fv{b|Rb-DU*ZvOA-BBfuf}^xUzUexkrZ3A)z}Tb_)M9EFj&'
        b'Oyj|ESq{j+2Z;%|nLIC<h&t2k{RebP@QNw)ipg`p)KA(8Dclnp_2@yc{=c7Hb2_)F6iVZX4JP{Q#A6`5jtNU2yRFr0j%w9_xO8D_'
        b';@KV1`#Ta{5*SL^-y!lVq{7?%r(y^Ly?Bal(RsgxYqw;Z$;D~?#CZg5X`e`IX>9!pRu=v{CGEM>L?5tTGKL6Lz!!dYXc<tOn3jWM'
        b'X+?$UmMh?Bpx;JD@W}Amd;1gisoE5(HhHQ{{hmzXAM4>h*U#b{hI<YF2nD~NDQ{EIh6M5E+K8Gx$a8@+fsL;<h1Qxp1_0nJF%ALv'
        b'^-d3#o%3MDKBtGhKSw&C_G1c6dE)5k%vjVQn<z2STGzCOmt1FZdblcVLDzR<Y~pcK!~+n-jqD2?*uKY1p?s6)*8u$2#Bm7ztR5ir'
        b'?4{8a`@8`B(x|fl{KzTdSEl>$YNYI9Q%Gy_WPq|i5k3EhvJ3AkJH`fmN;QQRnmlq-zjrQi02b_^3u<LWji6w&Ha^#JY(kacI0mK3'
        b'e%QeiM+x~X6nbpG;f>L4h&F|iOr8e-s9z9n2x<onDm#k-mHqHm)a1f;@Vp-G_KpYr>I>YSERSt{#+EC)j*$mNga$6f(IORhmm-ZD'
        b'@zt~k8)QM)w~Qf<$#dP<@A)H9&kVf+4*f$F`xJ2K;}m?QpFg2LtGU1#IR&Uo;;Qj(8xi@G5s)Yf4|jjpx1#T5Qz14W1ULb{5-u4)'
        b'MGlB*<5^s|to$eu2O9#YXXqaj5E=@$SHZf#^4*EKCr2m#X<Uin*opy#?>9GGIn9ejnj$<Q$JKmn?yFcneB6lS<lzY`G}CReZFkQI'
        b'Hu2~N+D5ezoLx7^KQM+qFnT^PuKOFYZ2i5pN{ksBe)98)zZ&mLJ8J|fqsG}inmJ-zkWxgvYos5cW~g=Q_m?7BV&V);$WR9}GOhwL'
        b'uP2KL8R<ib2*Uqdrw*hxpO{CSgi#Rg&PrrtqM5fg<ft<;G9jNpyaB&9{RpTM;wTJeYAUi5KO)HwkRCC>in4SWZ8QF^d^-FsV95~T'
        b')CSsE!|WJ^r<uDce4x2qpga{D89m&;U_d<nM`P%ZM$aFO{Rc;gI}j&XOJj&vVP#9NCl56zzVApELA-}tD~%>PVEV*G&x^+NbOnY$'
        b'nY8l1Vx^zmnRbfPRnrQwVrT+z4zn=?%O%OZq-+)UpA>zMHkw12!T5R2h`h-tZ9#lPQYVR!s(noRk_Vx=K*BM*VxUgr^Tvgv8Vrw8'
        b'kSKhqexw{?935Yw6XE(a6Y(@HkCotj(%I<LiHK+DyN<2^s?en}A3d9lgDA0;Zh4oy)(8;FW*8YAaYbuNo3n(O%Z%>QG!{+Hdf54l'
        b'+|pw<`Vi#4d*ezYK3c%aG#l|K?<qF1r<|sJj9Rr@Q5bPi!pM*hU`uagYw_tuagHmq%-E9UWMTJgzv~r?`pMVE*eCkIoL+-K4hY9f'
        b'jG+>vrvz*&74d3>s5k?^$qS9$F=$Z=^Ja1o^OC`S6GHs9oJNRF54ub^fF9`Cn`aE=8Nr#x>)tQ1HqV1(OLYaU<%+_pC!571E*HOb'
        b'N7DA;YgAIRTR>=xlluX?;_#BMY5C+qM=G{}h_9e;TwkLf2Pw;GLARoEQEBBb>MMWQEIqc9OIydsZ{bnIO86Nf`MdshE^xl#rm`MN'
        b'jZVd{XKUndro_x($if={JM90@xj9`?o$UhT#{{<JhuK?isI`5YvCBlb%jp|qd@ghr1Zeh~v-<0Mz~)|{ik3$iJ3wgvfIu!ZLKe%Z'
        b'Vr0oq^4DGxS)hrYh8C0@@>@@}D7+Yo^rR?nQ4!fXTvJ<N1$CJG##1<3h3yfhp$$JSV!z79=S`8XEd;#vihY1|Etz?0a<RA~tBfUm'
        b'iLF*H%GNxVbZ}5W4mRF;<>DKlWn8zoQ~qh@*SZ-KhnNS)%O&oRf0Fr??t00DJ;Mu_pys3ejMp7rA@XAvH@lnl9BUCLDUUmABLoTx'
        b'u2Hgj8EKc{iq@_{mhXQkm36d!oimNsFw-POG+bWgnn9sA^%oa7W9&%`pp}<Lc)GEta15ZvjSwa7J@u5A%x!bao^5%wUw|SfQ>;<H'
        b'n64M6Z{Ovr=OYc_;_af+)L+&YAf*MUx&W42^AwG-#yEozWd21eN%3eWNH2lus%NEBKNfI#8|Q#p2U#EkKGgI#NL$0aw<zT=P?a$M'
        b'V|uPwzOSe{+PC;P)hhj{2f_Dgv4)%UoVui=nstr&KT&|JG)w3{Fc+&3jl-7@boC(o0~NWy`X>X+G74dJ-3QB+3PCk7pdPq495gz-'
        b'3n#MvSeCytaKi8Wdz+U0e{7TQGioK>zf)9e%tyNzSO7J<wn0GLTa=2;GcO}g$h`A^0pHqIJ+(*(2J#NXxy+_t`xM;t2=6Q0(a%1x'
        b'8&7L<$()Zt4X|r4Q~qTtLQmsM!AARC8MOX$-T4^md<^5xz7L^&WUQxsp`V~yWB;X3zn|?Bhi9Gx`lS2?Jv75$Xz0!~U1jD<c@DrB'
        b'ZNXD!i$ZvBQBI}6U_-$0LSe+ezyL)V7>r*fFh}qG3yc8UH$rvC@{&`SS2)noy-%j>2gDk@i1GDNE+0KqKhW))I|gBcRRv(fi+K3p'
        b'28J)su7NXPy#J+*mH_3PA7v<uv=NSY6lfwn;Lvqt#1|-2KJ@SH3;u7~=bvp~H|09>|GIs+5R8{A5z1e1;Ue}u+c`qzo0O{sN~7+P'
        b'H%$Ixlxr8jN%!;@aG~WW<;sCDnDhv4!-e5K%9$R^0KY%o(hJh#ex9a00@C6=qZ>ef?oaoDu}W9nZ3a{RFi1=OcevpmkUsCe)JU5x'
        b'hd}y+|5BeHq&@WWywF}+wQgsL<#oy_7k#C3qt5h{>m_h!(nt5b@_h$4cn)qDB9XA?XMVdackcQ4rR`#6zOvyQ<EtaHa|0d^ADOXa'
        b'ntilEJ7~Z7`ho%acqR62NOw8;$hCrLP_FF~tL;^GdZ&E%hI4M(2ZyI+L+d^*zc9YLeH<#s9pZP!M|{TZ!Q{W+kXjaV%@!+nZb;Qc'
        b'$(uGf&)#Y$5l7lS+P9cvL+XyJ^5-_Zx#K(e^WfWc?yOHxJo2u7@0xowpw!87VQ*{vk^||k_-i|UajmQ{RkI|uV5wJuTCx$pqV=K+'
        b'>*oumPm1ZNatYE;;&=5ead)%!1D{3;HHZ-;ya&mrA2Wutq|lOs@)0Q{s~G!CI6s4Sx;U{z*3vkk>WJ22@Y%?<opZ017p7`sQVV}c'
        b'tlj`9E_^rf<c9qx3*l+MZntj{a!6v>g%B$@(7IQ?CdBYL3+F@B*-zTS4};HA;hpfK2%|&PPj2(2!?clGzEuc(RSwf8Eom^V<tOD9'
        b'B>y|ApC#~;m{Ns!&6pwarvPU8jvD@g_W!kb!vV~NwVrjwr<N_gW{XPIB%~I|nR!m#p?-5mn&;sSR@XOpRFeSlOTrBZGrl0W7@;pd'
        b'@Fc%P`5OdKvmg(cH5j+3qzo?#sS8ii-8!!Az^|44@?IUd+Y_^)S^I-u;<F-je*s|2GxzHFC9DI$FN)x_L6(R2b7+fbXb(l8Aq+H2'
        b'<y~mX%``LsYY{RGVTJSIfw3fnlw4geRrAdXMEVhLheF!SE9DASypaw@=Uaf542fLEz=-b$7|Y=dq5%wWw;;TWt-<sx{xY;wftVH8'
        b'5J#}ICcq6o>maTfz)~y2*1ZSP0zBde11*_a^Wyvfru-V>x)BXF$Q@z{Kpa-`1bo^lLKx8%Qt@)dL8ky}Y4*A@oP|imeh>rHNYZMO'
        b'jzj4W!)r6|ljLXCx1Q(_w(jgmZ`CTlW@x4m;`y)j(iyPKrG8d{Lb{3t8(zv6C@)i&TR?XvsmqBjtm4=ZpOFPm<P>0o=n$I^VxLo^'
        b'6||K8>$~q82|&Bbd)7-Yu>$CE9XLJ)ba-+A^^HTHkTh})pvp_|Wlqr;caQ`6a}`8JcMbADIur&3P^jd4mf>TF&h>*V7yoDYhInZ`'
        b')VaBfpP_|^)}ut*dOV6&f1TAObYV|$9mT7PTyCt`8eB2J*&#{VzEkqHvTAV#e15|!?r|80WrPKey8d*qXt_P>iMgdDVm=ZyZWK*E'
        b'D>J-<7*2C>{;&kW=YrGeYc#wHaVipa*MEf?0IrI6n&X`2gc(H~Krndxw7c;(|NKxg^t=!dbfQWl(t+*~f}RQ7sInLdmmn@wI&c&2'
        b'Tx<MUa6ov?aa-P!O_>nOO5`gP&X-~+*?2l=KU(1>er;e>2VozFNE@^zPS_3iaMNrW-Tuh=(@vs*%gS{_OhT)HkFiJn8Sci>GQcm='
        b'YhFk{V}U#dyg^W)Z7Y@MT;g1p%;A6LT%p*jLmcE)uMTzUSPs7~*Y%83$If+Jb?P{|E}c`y)$4d|j#WeC4zCVdy3H{fY+lS6A~hh;'
        b'mkH*@_an5ZwhM2CtH}2yJnwswpV$pqpeRGcd&vKFZd7;Y=FaN>)7-Fm0MXr@8|9;*KgsvaO`_ABJflbiV}kRi-TS<XBse{)G3eCW'
        b'l8@{Wf|Nm?8wI%9qJdL$mYx~}%ncYs@DYHBOivb=9{SCJVn{VRKOe7-SUI5QVjDdd*w5yNNxKd6;R&?$f2TQV89y>tjDi?w%NTn>'
        b'4BN-d&;K9uGP(|I)$8}oOPHCLg*ZJgzSZ~Ur32HV%h+wj8}+0kXXk*VI4_6`aq0eS3@|Y#tUIx4NmW-|_FFL>3cosOC;i1tB0bif'
        b'3bUE@_9H8@GQC5^187Ch7@PPH2-t=?PdSRLEss>A^`rymn2$J&m7*>Ave9FPMjp=N#v(Xx_y(nX2y{GKKO{2TV0#shSa<2XlG;wO'
        b'?;)f^+-_csC$yWhXB3OUK`EH-+BblLJm2tc3(gM}k8yoz$a7#aAIUu?^Ccj@Bt*L4<{}<g><Nq_jy2&lE&$&FoI$ov3K666R8WH|'
        b'hKh|x9mQS;v5}t3zeVP9lAbrZ`Lp*fKbtGdH?wmEhoL~yuRz-ND9`nXNx$q|r#N?y($OjF9aElrLF{Oik!PP7(jjE<>W~ig>R9Ai'
        b'U7P<Iua4aY=abV8=FP8jbUbtJadEqj?`XT)t`j(QQH~B~l5u*H=YUBb(qT^BT)pmrUdP5Ea@woow(Ep?a`Wt5Z-H}Nx{iMPv{HCk'
        b'n2ghVaEdl@*gqsvC>~jgr>fB>a4_kr)puR_F#1m*?dICMCPpK8l?{4K{IK>Oeu4DSxBn8qxc2_{tgUK5l)QeQzg<WS-HM6m!bBb!'
        b'T%V0AUx@LNvhXK2BJqX7@Z=3;<K6djvbHNukE3CxIUx>j->;7GzMCN*TkYsUWj(Sdc3W=H4iyz-<$iT$-){}_Ck(yEy}d_uw07RK'
        b'OYArlB*`n@k&OQLG8`vSq(|J_BLhX(MdgEq;q)R6Gy64z9-V=ti}gCLkbW<DP&b(_?(t5;`3w>jWs?t!9d7T5{^^IsvQ7xl@p~PB'
        b'={%d!)^-KJbhyy=cQaag9G&8}9<WXvu!h~kA5+YESdOmen!a0We8IbA%QnZxpwXmju^MZ1N!IGjC%A6{l7d98Il(q^ta%gTst_W)'
        b'*7Nt(EsYtKvgQ*;Vrs4DpKBeBj^-0jNl$Y?b~WjE)5)3EA!;%=!>Mzc(2Tqx=^11Iy}%m-r?Ta5F*pzByvkXj<S=e|hUDm$k7dR;'
        b'WdW?S#PVrOM@iD^9P4uenkgP+LmAQ-oJ7;`+76TmuC`ZKX&wS+vw(Pqo@*|A6UEP$0N$0m9s$3@UsC{In%-V(w-G1TRt-!@U%K6Q'
        b'Vr_s!s4E!#zMR|ra-{f-jQGPUkWdXUuv`A7`uLkpZ1^1Xvf}Aoi;t48RUQ&o^f-Ek2;bU6I<V{bME@#Ue(&+F9U}355^<Lh0hr_}'
        b'k<RCIh-sr(<DKPg!DG3Hp@Dz$o{u{}zi;VkZ9FuP^)sjT3sy&54cKTCUMi&T(5kyBo~E_ZGhCu+?f47jH1J{o`2d96b`Np~zb|!l'
        b'Z>K1DzX#er@#-?P_h%{lR+Y!krX0v)(k_(u-cu9z+OPm$$wtT)nL&7IKsUw<VD1vj>6q|eV#?$l;-uB(a#u-PUa%|6pV=XQj=!GY'
        b'eFz)wr2<?q5Sv%i1Cigt@T=<}nhImHbdjEnDkX*VZMN@?=+>gBywSWuTGk2Xr4)`KAZ(ZX11WiOt;{TgiUKN*VTy;34q_u7Vin8)'
        b'but4eQL>7bw5EyEJcFEM>^)CfUl{7SY+b%~^de2D!C31>KS#MQ7H4TWS{}V&{ha=gDm)SG=YfCAL^NK2oBg~&{ut&qIZdLpt-khH'
        b'z)bo%bP|!a*S9y;&+&O;t*h4H4TYKS>cA(qr7c$e@Y?=Rh9AS@lz)gV2n}+lUl13$$O18uy0*wgyEEK!&yisPzv0U*5yyjmj^&@x'
        b'eyD0T6^%m|NeT~^ng?IZ;I)P5yJEn`(6as5wfFJzCS)Z``or8-XMx#}2d(Sq5Z&ChEB0|Tl6($==x`9`Y83PxgH8Y<s75`A;)y<G'
        b'tUe`y_xW6XG<W~!d~b@BU_rS0eO$xmr~-VNq7x~&DZFw-)F-njV)Z1_BtvFVp#X8F;46i#{((lCv2VCe794a&bGO?B1CPPmKUj9)'
        b'{R2tPQ+drvkP;>?S1=|U-tSM5w7wUB<{5}D>Fc>l2{Z(ii71}r-mCrZbnUYNO9tXcK|{g`vGkb_#^QVhJ@vlt?(yrT(Ok#!l;Ywm'
        b'*%mDSS4fF?RdJrok(W{yt$&jHMJ&HGMf621mM=zZN2Odg&M(8<7;)xFN1iA*_e$$3Z%XX&0|+wE2(2!HZgCN-FvEo%9x$K%C!Sy|'
        b'Y|PEwHoDPy_M)S(v2|lPh6{(60NN^=`vf~zAp@=FW`Uswqq<<@+=A%bo?yZIt$F$s5eyw2Xe38u=V>L&Nj74R=30e#0hav93e9q&'
        b'yJAJzuXRUO8S_Lqw>sMP7-%zSvAGg?XJeFA$k8hh!+gYB89VTPIVP>Su0NHxA_?q4Vn02m!b9&j#UP*&`7%&ySd1XH$E4hA1+3!Y'
        b'm}<aP8}owAFQKj{-6{D31SvZ>(0GA8#tp#7{a++La9{fyZZ=_nDkAfOU&MUe^bRwy&|h2%dsKsC!}E~VdY5@r1F&@>LOfm34A)u{'
        b'SZl;q5C&_FHr7FG0ufBDU^(}3r8{ncS@V*p<xY$f%<Wfm!6MoJ6+Oe&3i_qQAj|SO1->m3{_N{h_g0_pW(=dpH##LxFYjAl;m5*D'
        b'Vxe6fgeZ=zf~&Lgcs%Mjc3g5?p)Te2n-lb<yyN=grN_;9t9NJ}QSc<Z6j@o3=5)7%Kev~7qQcz|e}-ny?!KZ5fSxj9XXAizg6)#f'
        b'?NUeyO~pMr;$Oe1@B0>YYWfNB2-Nl;$vc-P4q*MKw-Jjg=>2;j5wudMO?<ECkYebxjZi#!-~HW88Nl_HySlZW7s`pGihJKZj&kN6'
        b'WH#PVPDI}y-%(D8?u&<SQyOz?G*^u1Vk^|<C52u*rqHZ5XRFO{9$CmC35|{qDF6Zne`>#EjD<gLxkULDV{CkP_#)+3;|u#qiSi;<'
        b'Xbv-ak|u<i*6?Hu7<yT$On$n|k7?|q(ST$x0DJqB^gKLYHQyDJ9}NX->UORnnytH5?j0&CRIAMi#1(ko5uTy^=pgEwh{0R6m{y^c'
        b'X!Y7str=h$I9(H^&_?!o?UdRqQG+cL1sEAyl<TAGH&yIbbpf0EB?VvnD!--<u@?yqBX`2z(D3k6mXBk!9L8?#C5m_l*46iExl$C%'
        b';Eq#t!iVMIxv`*sG)-K`(##)y5@$8_z~)N1*_E-H`~xfvyHv`>)3j*YOQOr#{1^lQ1POd>GtE;Up`;gYH~kUN6g&8u_}wly%7yD6'
        b'=amG@m+_>PcRF4lXexfc5+0Y60<hOGZX41uzh^s{6(kP@56w4p-5#Ezii_C?d;!5S!FmCAEdrov(B1zJd+#3C)RpalpPVFzkQ|jD'
        b'rbuWf=kO2^+YnR;Vue7%Lv0~S0H@w^VnJZE)6$2nwf81bLqOVMR7hw$4Z-kIs!$*JnhDfKr8pOysbj5ns54OOw7u49r}b9(t$h*@'
        b'-`cq|zk5Hw-#^Jd=j^@qT5IpU_FDVw?>^={ZUrZPBEdn*o6VQ3zS=Dz!1FsB-b|EN;ieeui}!JNI99e<zXC2pu}<{~?e<nzi}-w-'
        b'_++bDZ2vRA^|Z9P?>Q==)xP5Sre(1Qkipo91n-R^{K3qr4~ttU!vdsZhlJ?Z@*m)WblCOaV>q<LSqij`A<hkNqB36#PxW-F;c6wi'
        b'0{y7A{YO%)pF&HJA1HBR5%4YkQvHgy@*DjM*O$aA;a_v*-z;e+j*dUT|B^B|kPpxtewKQTI{;jQ6z9%;Nth(q%j%{$-U;oW-jA05'
        b'`;x4kvS$y;3^gdTBOLD}o^5rl+}9Gmhxkbd4UHG>9^Sf=n1c=kD$ak68@CsKu0Yeb;#l9GjAudBNBN-V@eovjrcE=j=FpWn&&Il*'
        b'UFmuyRJ;3cYBTa|^EjYiKInH+1&0($2Ctq<ILartKpde(f=M@3B}iN4b*^LK{4?RWBOKI}_2ZIruQlzX|K9WqwBO$rV|a#@hB!d1'
        b'Y;6Iy2HS?MG5b%t1F=6nB0-GUV$eH6mKAHvP*5oNphqX5l0Q<0r%>4+sOE5M%z2L{UYl^a)lq~!Yjcr7y?c<HwistKkUSOD8M-p|'
        b'*}u8I41G4or5%6Cl#60{2{Df=2Yan0R(<FBtO^^G>=qp0E*Anfy9D#`X~O13nx<u~Ia%_6tT$s$eXw4eQ@yF9dJ_e~#Xz07)i$6M'
        b'C)fsTVsc{brqGxta>&W@86EOCO267Q5HGHb9as%N=!}vXE>a+`SUp>CezjO0uQ!a#hr9Y%{a_StFq&r&<{Kk0Njl#w$+e2CL^{v>'
        b'Qty{;0fxc2^yg{!UR9GAR=yc`<5=EM?q&k4kI^K=NS>R($Vug)ynG|1%tPg&oW;KR#`4e!?m}?ZFJ>6sORx%~Nr$C>4>mFBsTlp5'
        b'j`iQ>Rj$#mqq5AdHh~Lzd7jI)Rt#5=)~|6@TRZem#MD_q%p{x3l_3U~6bx{Z*_DpN<8=QDyn3T6owoVgH@jNs#2w|EeWf;=zwz)v'
        b'@RE+3F%f%_Sb?YeC+<vh`bxn-s}8ac*I**{A~C~1oeq96%{e!(4E)}*Je@RW=tW!&<DRcNcs5^`LFXybRnnY+r^We-(%5)zZU|01'
        b'g2{7S`3mXu@CKezrJjn#Ye=3HoqejwC^JpLj_>fzD-*HgL^(BK7$R4gugg=Y4hF()MFy?i<dd!vrPick87g%kM()T^rE7FezY;CX'
        b'*OaEhOrHeJ{PFrz3#&I?*Ub6iEcOdA<fPh-q1hiV%v#uyl}qW@x(4#Zl{x4@%N$pZIBTJcgr>=Qdi7#LRlh6~I7wHbkJrR1LNKKw'
        b'Y@8?NPB*FF9`<5=H~1W%%Ypft^o7{b#+OC-)mj3eDZy%>#hTeykFVr-kZbesNZvGG0$eKy0+l>BiBbAIvzQE$nf>S!1EjC4ZgoVv'
        b'jo(E3NAl<;0WoF`y%~!OBu&Wt0rf~8^_y%jE)?7=GAx&egLyj5ncKwzZ2msnDV~ouVm*moRRT|^PU_P`YR~4a>XxPYfe#375&c10'
        b'BsVez;)4a?<YjB}@*NtxKFci26B`#0`3v$mE!>urw|9bEKqwy(syYXxfP~qP^p}}skPUn#8B5JG2R7r0?>D_4p7@dB36#Hu6Yp>4'
        b'?16EUE>`-Zmcn5|fG#77&A^rZ&HgBN1msTf=B7t;(=|_H8UC#M<jL=^q?_sB=OKUaIzyZ{zhX4M0_CT@`2!(8tyDCtNT44^eq@;H'
        b'&952FuVMR*n}dCnDq?$`RTF%;S{|T%o>!l>u=<G@yRswrgnR~-l;Rqg4$VH0f_`Gfakg+p)3OAcy``giPK>>YlDE1B62z?y@RQJr'
        b'jy<xu6!zfi)f?g!Llei7zYFf|pS3XfGey&{2pQHd$Ro!G_q4|?3_f+CX}NkPhWc=Zs)(0m)%>UuWn^fQ>;bQnS|P7*O-ItU82wtx'
        b'-t6+6QPb@Cd3}7-MmoXP2Mj!c7)Z)=4Qv)?wnC;#F9WZSuddpVu6joh9^jk(w_Mb3AG7l6_U%!0DjKEh)DL0UI|8r;FyItQRZ+u&'
        b'bj_D4>2#$=ULEkdP^;u^-_Rj{GX@Qt3fBPopw>VI`mu>$Cu=u^U0$;t49lFD>RL*!bPa4kh7(y&mksTwpH1o$Hpo}Y;#KL2@QEZm'
        b'u6xJon-=+o3B%GNOe3*c*kS?udC^nD#s0H#SGc%<cBO|Da|dW~DeZb%oTPT4-y)Z*NNi3i)lvI$VT3NC(_<rWQEF6b-h#%6v@BVG'
        b')}KfHWkJ@vF|xHCpsi}FYXE)x3Smsqu|DOSWR|97b(>_79o28f$fi(w+J!z^9RWX;w2Kx`v2moShGgyf&AA!RSFT-kp?nXn-i^&G'
        b'&TY=?I=Y~ve)+NbXU;S&b9}h>rAn2)I$)aUrxI6$L$)b-AW~dM4_G`u)5g_We{n9tWpPyhJ$c|=@nze<kMM(ZLc87>Cwpr{b)+mR'
        b'RcdxW0``AX4)HMBO!_!)dqjsGm=B|>Ew1YclC{?GlM&l39kTyIsvh{#HSinpIorUO@Z%xtdRr!|Lv&@SE|J*;0YJNb!Mr?2{qpYm'
        b'XO1;3(+>ochgmK4%e8OtsJh!L$x{DJ`KEAV)3VC7GGJ#L(vuzZ<Pb+i!A~pFlPtnztY0p(Zh(G6Ey@ks&y|H5od>uDw4Rxts|&{@'
        b'MGq7&a5OC|Z9TlY_yICdUzO5SGr9PS&cB~1?;CP$FLEt)$d(Jfpm8D_gMi$~VBHL7(9Shd*kSQ<f#jUO`@7-d72rj)d2xpwv)f-F'
        b'Cx1b6NZ+$Q)zvRlm&zm$W7Va8HPL>0w>&%;MYVlzxg_D(_IF&(+&a3h)f(HvZR6TFN5q4>hRv~7&SBIkC4u9HA_PMMpVvv~h7g`x'
        b'pRY`<vmUqcMLW0a11$B+w0S~9_JZv&<laK_g?(hcXz~1j5}Twr3}HvpuUd2TYdf+aXE|jzyI@FGR<eT=O}aUtrDa*x4W>z0mOcPl'
        b'LfgzU%vzB3yBNK*!|tTE?{y7q5$|ms*z5Um)IYO(Q$$D8vb`+P-yx#gfoP{#zfKRo+s*nBvdgoYH#D{IY|n!iY_D)tJYOW?<^3JR'
        b'(M%D9ZRTdt`s_<u)j=N2XeFx`Elm1#OqPZ!$Z_=*inFvXn9)4*=&L#TOT1@SWia{Al^9-GKN7`;Jv`h&<7c}3j&;c|*ah+rWNrAD'
        b';!ij~QiU*MdG_}yvqwr9c52x@lvRt&rM-cLQNtY}qh)!rZdn`GQ`Q;A^Twi`+^SjNwGOigF~e5v=vguiDA{DeP1CV>%l<#4$CBK*'
        b'jX@?~EMZ@#2t1{9w32T}nGW!@qT#u*W=m&$(O(AOZXLQCZvoQ3LJI)ss#C+JH?nC9n_kbR&#>t?*z^U-I(FT=5?yuBe(a-i&&4e7'
        b'v(=u<1ooL8T_|Y(sy}pu(B2HMvZRi&&tGO4(N%pH?_iG&?Vx8OY1yxv%rtOxOlTPsc9eg7Bh32i(AF35f{hM=F`H0wl*y!^Jb)uw'
        b'12L2$+vkj3udv$(KG)0p^}!R+`hNvgk$r}d9%F(oFu{YXupuFjrBbypf<tl@s?q%(91RoVsmk!UmPH~Q-vBPdx=7)w%kGg1BRP?%'
        b'!igNwYI@r+%~nXW70UYc<bNLJL6!XLs&u}Hszh}7RST}Gl07SHgAdwKf)>IYS894NW5}ddvvJ8JHCmDYpJ9FA6V+xv@E1nbByjI{'
        b'KqeC9#Udz8P9sV1k!)8`=5bHJ9Z!DG#xL~lVZ#+~*=uzT)?BfmWutKh%uAlF&oJo;$C63atbcN?3=4|9GP1D+^*MrlVH}lUUnJ9R'
        b'<T>nFhQY^CoK={hy^I|d_J?TeL$pu6Y6wFCVTLdxC?hH(AtN(mQATM-YsTJ;o{W<j=Q1v<O8r!&VpXZXs&t|%GdQEJJ1l{GkljK+'
        b'1$f^tMT)~GO^8<IDum0q?S?F}oZulpPBQrZRkRo1j;RwdY#L#~F{x>9i$jPl7d+eQ2eCr*@ufDQ1%2*gsu4Li(Yuz~cyK+{xa`7|'
        b'wX#Hf%4A#}iO~W~Xa92n?f0Z<sXtCk!7Kt!FyD9>?_cypZ&3fIk7pg|&YE^+4@HV1Il=Ev6RrB5e4zVCANiX@zYXX<^1DNG_}xd2'
        b'fN$1)<lRGaW^^BE$=&)$%~ae<O;J85gE&l7y?b@lFVAug5QiQfFAFms@QI4{#Nr1CU<W3(zYQ0O##zPDbfoXJalJbT2zaW3WU_*{'
        b'U#Jp^;=#$~V%kgJlTOpgVeO0GlWR>Uyyr!DwjzPHzP`3@X?Qn>UByCsOT)ezbKiFDzVqDh=pH8{<rhii$3*b0RGuJf#s(Wl{W&H@'
        b'Tl&aJ`h0YzVbzD4!=I8tSuLyWSubeAu1Y$SNxrn<YyPSqPxJG|XijM3b~Wc1g_ty<a{mPp)+z4$NW8bVeREFFzRUYMMA#m2yJI9R'
        b'+P8iC3%l0g#D`edZ*m6qiTCdB6xl@>S*PBQb=XUH2ga1o8aMBw-GQMU_Tt^vDED5pXJ@w+H+4c{B_!0lAo1MpKml5}Bh7>l7A<h|'
        b'(LNp_$7o+x{+2MBD?crpnm}yDuwa4yw9MUt84v$XuYVzNB~19`3E}nn9JI5x(k!qGu(aj4`%^4;IZm9$h%-P3Zm3UV>OW)QzP`wP'
        b'E6*3GZJ227u3}vMFjikSrfi>4EVV?02Ctp#XbG(}HHG;^1i0C)_*25T(W=PM2wq<3BAV|0DFP=aMGB_*uKH1J!tz4dg0JSRGRkuN'
        b');U{3gN;y{=0^meMfO~p8*RK+_J?M?)1M5R=G!9J6A0yBy180jL;!TcThv+Tt+NDJy7y9iPbv2=Z!SYb1hB!vElSPs*7f+$lJBum'
        b'`5wj0p{puiHQUX8>pJ&@23PKm;+avw@+e-k+4wYW<~4_cnLPYMv!F8&YN|A$l2RHRM6*wkAfVf>Cq->OpJac@7(Sa19sewIBHPRn'
        b'{ifQyKrLeP1bXw>lG$8;9LZ%(7JW1D2DCXTY!R3_1Lg%493lwjY9vqxD57$1_YqLUp(w8`Q=+_j0G2#@04<2r<FGS_`=C=JyE^b&'
        b'@wva9|3+N-4Lh>lwi*xjmG3>P22%!?Z~;BDJOP4u(|->)i^<ONAY2_aY^F3^Y)S-CHG}jeq{HY4?kwwS8^;umA$LAEj~@{#%IUL;'
        b'zb`DT|GnqS*?D|BAA6NPPy4OY<cH=)LjyzPJ0+U)C9CYZno)JP`0kmke&9axk{CAk`h1^^$%n-DMZ&(02UkVUU-f468{jZW%@Le('
        b'8dv{eI4{OZRq(;u^hJu5f~fEZ&y$nFeR0#2VbjCIWEdpfp~EKSFh&-lG&O8e50iXI62BN$XAhGzAgK->HvMv#d<>PFJghDno=Fij'
        b'v)MsyRxph!#-U-})-mstF~13G@@W=2nD-6aP^%iLMhCNv4kQ#^ek*hjN2Gscfg<xnh9wKxW7Ha3d|NVl&l#!BWcR8cBLx=bJ$0Q3'
        b'Q&5fb@W=(4E<Z*6Uky?7*GJAL@q`(xE-IMUY35Cud4pzZR7@(()Y43ok!iIsTNI3)W_HocZklPMnRc4lNi*-!%)4q1)YD>N916;T'
        b')DlZ`u__ha{i&87R#A?m5SPTCuc7R^F24-Eih470QdFvnc~eEbp*fCAA^FD88ljQ0uQMANyV?iqc7$5G{5n7|YIDz#!gmB!LBt}F'
        b'rvBohYz<@AQSZr$^g5`Si}m`u(?uWy=}Ui%le|?ws8ky15}JC~$TV1(t@C{?Og%fCu`;HG<mspusYypbgwdj7nxAa#pR<s(MrTBC'
        b'VW%t|v$dOQ*7Xi7-HQ{C3I>YArOS&6JAnZkgKzpcqBss_ry(0D-NCfOP3IeM6W3Ag4yH{axhy&NqfUrPOh4*2W2POL?qj@+&}eIa'
        b'i1u--FjAs^AA|ZyYZ-y*4)rbV#EGdQP#Y<fmb@cCfqZk>p}zC2;?^d}AuTc<>MP&#MRa=k1L&1{v`<qL?hX`{QMIDh6|I6kbP_RI'
        b'Ln?EmuYB>C<H>GE!7H2#A9KFu2c7Qu@BlZgdbnArV_F={RtNR2IvCkUow&5n6o{35jCV{43jS&CTfyd~(bJ{wZl>0<G^jR$Up8ej'
        b'Xlr)_FFM`0G^i}hY7DFED-u_(C_D6%*{8J7$ZV}3(5o@blV3NQU#(jjqzki_h1IPr(z$;sCP0}MYO8~J_jtwG>gob$3{tKBHBw6S'
        b'?lQH;^!6}njF+G>pe1%od`KwKU{axuWc1~bHr?UAr4Vm_A#_kJQ%gx9L`1Dyz?L8dH5-wFIu7^k1_fo*2IB5=kAh5nLa%~+SOuAg'
        b'+w14wht0y*hz{yqbPR}BHxFROkMZt^px`TWw+2@%o%V?I_%Wu|Q5@71$u~wISr0|>qBAVTK}Lw4S>4ouo&L!zC@loVK)*m)30=fw'
        b'G)bboYF#nX3+S;D>BUT}`o5re0f^ecybE2@y=WN2&QJ{l&xp?zoi7si6u~2%4<=m!TG3I>kfqz*cc}AI9ko@RJFK(o)em81&}oP>'
        b'RP%saT)GSjb^pGvbXhmmat6xvb~7!nk!P4@xOu4aliG)HQ^s&K4nec2LMRF+1JsWWlO|#u(zDK9T;_`{trbdb78no?42Ir30%9v@'
        b'8PrMb%ix(2S_y__3mCs(!bsH@fcwnUyQ7Dr2@71=WH7?ik;59QcK_yF$Amsw?CA1iA!P*WC+H*Fj=W=zd0&%zlP{d&oIC{$(S~Pm'
        b'dVY`2;~S=hP}{reUw}P&SGpv(K?np?Kp@mT88deI(I@aSIw<&uxoN?xb0cO-*BY5xl`bePgrI3w$16g3(J2aD5KX<UpnlVrBTn#G'
        b'Yp@@S@+0{&*$dDrYzaP;fCjw20Gk_l1)dcrIdqDiK8d3cMnmG{L>=?4f@z=`=W={Dz8EJ`eL&)1eikdUhN{<5wYh`1NrCO(vD7gh'
        b'7zg_n6&{c0`Mbd^JMw^s%4857BtF2+;9U5G^R@5EPkN3(psO8@7v=@2sCS7jj1@g)X@dwTfGLX#b4xL=><T())!J8Mvts>%e^~c?'
        b'@Y<!I0u!j9Oc%5w%qvh_7%zJDH4PN88u$Tm0ri)bD2aTDy9v8}iP7xp-#~kTSZRgflD|H*)FB#?$g~U_6^9iAHK#AJ9A#cQh^rsL'
        b'_CLMUF>WNg!h#W{cadK`tf<3G1vkqMzQ}d$o*TS+L}-mJDED^l?veVZc-$+qJ~qT%g0UrT-|oODVgZR!JBWjGwSUc6F>uUumu4JP'
        b'4l9J1YPA1?Ai~i`ocuo_hg^>O@7?48Iw0>fZ2t=${@D>2j|2M{3_ciwdr`ZcV%v>m#W?v{&+mc%Y0wQ(C%kX=eSjHuTftrUM=acp'
        b'{dipdRE&yww<Zj8|JqkBFChI%o?NvdE2{tmNy>3WA6K2kb*UQSG(<r<3Wi>7T+zSn|7)%z0N4dKqaxCw|Eic)4YS2P57RjEpamCs'
        b'+YBT>&iR@+dA!HXMw1T>qXS^wBACNK=2voCL?aq=Cjfa6`Zx|#f+Usaq0g$rj9dLZK9GAlW^v>}{yH!H3nw{W3s0Wx=|R*pIL^S~'
        b'2w{8>&9o|*Ev86TvCro=1dQ0VYm`hB23n#&VMqCzS7VddQNAR2O>RUgYv^>kprxTBV>a}<QSPyGKUn?EI8Xw5G}Wr0ws@_ca*|1i'
        b'{F&R9XA57`SsC+g@+X-(YKw+yrT!}`=D)L()P6_t)7&=x0iFRv%N$=-j$U8MhU><lz^->P``^xVP^}%*7Q>I|=J8A%?Q!X*T8~j%'
        b'+Q<Xr4Buw6rx6I$<GtM}`VU}S*MFL=pql5EfyWr<;6sFhyj!ZC-u535O_2l{uVLzSj1zn~_m@DAdStGJ+ER-PLF-_jSrRcvvsH+M'
        b'f^nod_=cWrBjd1mNZ9<ySQ1wt2eAH{@&1Gl1GSmn_Gj4(e)IgN)Mg{k_hUQ}+_!o<B}-#}nLhaLlWSy;t)}g`tVm|08dNFSIv`<R'
        b'Qto&HyuFUY9K##gtn=s4p5%dNJ&y~c0KH(&Cx{LKMpF&p_@gSSft)x^m=v-aCZDPf`p}-mLfL}VS+W<t>PAkE(~a83SYKUfa3C2S'
        b'?3+Lf<*+bLf`^ehxJxq);8Q~aq)-5V^_VO~Ml;)KYKwwuJ&tpzbD1h?OZ3OGP`QTb0Phu1?wA*l_5e;~f&aX)r>l*7055#mrz<wI'
        b'-<)mu(_CP@OP<*;&zvSihlaC~^d^u2DrS?BYS!49<dxaEfq3#O*&3<=*b%Mm3d`(YnT_@x8JSKCv&Y~@L}rWZQ8L4ScoflO`1fq~'
        b'Baf#=Z8+LYydPybLp52bJ?EYV=T4fh%YYE2Q^V|-CY&u=E(jL{cTLFbAD<}#uL5rGF+7vaMlqdGMBDm9mrrK@zp<4XO3;HL=xE%`'
        b'{(R4^0(46&<k3`<k1j#OR4aHB68UJQTLtQ`7SS|Qt%Ke!`9|U9XzWU`pSd--f+tj{FaqgWrNX2%=yn=^QBfj~W_HMCx{j~Ds-SkD'
        b'Kqc0tV48?&*t|m2ijU?#Aefg!KAc<2k*4Y#Nd?(@qa#bh;1<V1eYQSd44tAbJD+ofca(b?5Br=C9b?{$xwR7L%RYmCz>kq~=xG<k'
        b'Peh=njpr3*<}a-c*MX1a?mK1b>dol?C<C>WVOqB5>`zIO+67IbqBdpbbREp-Kj?W(v(0rGB!<B(RjEL76<V`T<U%#Mim%*%8J_n%'
        b'O>K&+r4>}eln}pFe~6<+Dyk{Xfvcay+&M7IHETY+s$rVl9Bkf_xLRDD492usq|j{pbC%YxAn64KvuU1W=_cNPrzR!60K-*x0#~Wy'
        b'qIVo$jVbILS*%NCp9U62_X*sNCoORfhIYh7MH;@#Dzh(fqjk#JJbg+BSo0(mm6hrmSSZfSIiDlWTHq4tG#|<}YAkNbCuk6NUsWBH'
        b'D;!FVBMurQAz{%X6r`y@GFp`a@#B1MuHrm9cc>h39bJBzQ|CP}m0mH)HxZ}R%FL;BH&^k2T&e;c(2leyN<lTrLP5{F!LTt6Lm?1k'
        b'*84mygpRDEww2~+m<I4%=`F*u2#9tuxk9F3wv*h&+-Y1Q9<@t7G<UU}mlP{&^q(YIKxn9KI(yL~MFPa84d98R`QQTx@3&c~25EeP'
        b'O<^yxz{q5p)d85wz7#4!=8I`iG0mkqpTP%B<AG?Cg4zZT<u<*AeKO=9CM$92+#GQ6)u=CO>_t!pwFn3g^^t*46$)Hoirb83<@=G`'
        b'xJk*2xkLUku%A;lha0K3B-*7CaH`fw&C(nr(?)>GV%^Br+lMVwn+n|djUPimn(!FduYy!#<r<dWb{*9L*05KiuH}LLM<!H~P;cOQ'
        b'Ce+*^Tpa^`T&{y0nNuTha6N7_*JW_n&potUjS%Wa{ReR0MPuCeoBj70_wB!X`oNvt_Xu1;y{E+Gb7GYK?p+w`BBTxBCK<MMdagq_'
        b'B93~^s4(CXoMfFLp?eL6-OPK#&Ad0`rW))T`?vFdy!-?A5%{8f!i;!XI)oE)@Xc~r-^{C8B-kBw8@BO(jcyeh%w2#asRgY*a=)F#'
        b'S?&?U{m@M@o@w&GRt^>Bet499mIIdk5r2{O6j8Sz*ccW0$iV)qqwQb>_KS0yQ9D4@QIV(}JTA$t`R9B1UlGDr*h6pPzk}@~zr3$L'
        b'4iTw4^uKj%6j~$$=fvoVLeJvFbZq}0m$LCU%Nq*lPyp_5<UvKPBTe%u=WEf)PkTPfU{6RMTz+*-7<zLY8hraWG~rqtIyx5aArd8;'
        b'&{EvpV^QLrkytcLvKeAg;Yd{G{?#o)QS~x!D2jUL3u9wAe@tC+=NQhp_^KiZb3cXs(_&G%{Gz+~t}&cHW_oHg7A0<!1IN^Hca|e8'
        b'`zpku5Cmd3#d09WO=85|e=G;SlzZkq#G<BY?0NusEf9q<cE>oh@Ug2m#G#@wap=v=&$#b4xVJcz<m)_cLXjVgEfQDH#?iXgSbG<L'
        b'2YZKF1Ugi_M;NcYOUb>~5Mb{-@uf$WrPu5Q3f1mn@8WS_U{RjZV=veOcajAd)Sbi=(UMh}8XUBjNxDp(%@`h+*<?nz;#*LRwaW<J'
        b'2Ny^Eu6F;%+-vqD0;eG|iMosZh`fqkL^#~Co93t+$IgxGcXzgpUfT{VMDpE&yBkNy2&U0vi`nHnHWYirK{;gIvJN|Dh-6>jGfo}l'
        b'><uz41Z(ObdGZ8s_rWuBF6X(QKraa(Kgl=br?Gj#F>@~G&*l@E_^k}CIu_f1(6j6}YH)$oJL^j_VsB0B|26j3wBp|Et!cT(+D?%i'
        b'9BXaCu-<HK-OD_7>Sx+p;$L8I)yjLYx8RhGwYLlJ)81ab;<2|kT3gfPI~uH8vh=gp{YXCP@1DrHUwiw_71l(V{%iQ3WN(R2hVQ}N'
        b'n*MVb%U(QR!|Z~HoLMv<*`ty1<^DP2Yv9WNdVeOI^=Cw5{Fz&=tuMRX+B$UGyA80uD=@&2Gx2}hpE-Et27l(B<+#n<@-OsfI<NdM'
        b'@n^C^WD**usd^t>FlgRLHG}s7E<qxpQ)L-d*=VhkeVuik<3oEEe@LG)wMNCfYk|qsH@pmu%z6Z7Vl!o>$Vdq(NHT5EC%w@7f{|*_'
        b't2aoVmW2EN(o$a?WK$h^x`-AK>FC|NigJiTVUCs;a^$j5Bju3CCez(=`Ak{Xf@C@!%UUAS)?A^x`^bs1B^wH4FG$Wz0w#UF#ML>N'
        b'>fqHxoKD45;AdoGr`D2|I7I+E)pHad$W`@!QK<fs8RdQq!_fQvdKJ?|Z^l&h7c-M(;eIU4462_kTrBF!oY#LoRg~JsJ-`QI2F*Nn'
        b'-Lc8hBbS;TshE*zk|_8Vs*MaR^To6;Vk*0D+;q<CeAPBiW*SLY?3|>U)#bi&w5nDc1!7pJ_6}-iHG<ewACVb>=1Db6vrWe|sRW#*'
        b'0X+2Xw5@CEy#8Zsy#`q(TEN`-J-IP%2kt&GOgxBLjy!E)95m%nQM=Frrb8~99u-RC7*f=9q@ScPj$9$jT9^#Ysa0Je{9sJf>%Ve<'
        b'77{X_t>&o?KFuyMIkuM2OaonCtvbm`<Ok83)W6W(OMs$@3k9nEV)cp-o>rlSD+gVF5!4bzk^CgurK6Cu14U=^P2<t}Npr8neF10t'
        b'DMzQ$lU(Spq%V3c>QAF}b?0&xgg4EXUB(8%!G6ys78BDzeGR~s>LgxWvp~huSeWfq)6whY?O@o+(4=%f71JSEgITEUmLs_5w#vSS'
        b'y}v`d(APq3Jwt6D$Z!Sw4h19<6n2cVcYNg6y&SVF=j`cxrMa<O*6o<?*%}hmYhm^jzDiiAJyk*Oqqw8~uV-Lxcu#fkyo0d=8^)7('
        b'H)VghdEM5|PU(uSkLIRDzGtEAuQX>&-kW;FH=`4>0YS*w?FjAZ@lY*%iKq%v@5NR1e+30(qAe*f=v1HJWju{!1rN$Q9J(^<%~nH&'
        b'FBw?5;*}jQZ?2dO|C@)(1?xamJD3N|L(|ox_Ye(xj*vuQ?#;Nd{-WNXM>MGp$z)KMy~9zUqTbw#s6|wIx5YqdX==q}74t^fNqlIH'
        b'FH4pk^Ec3S{)(mh##p*L!oNh{Wd;=+sjb!N_pVB3kw=xpt9Mo9EBB;ICj+W9Exk^aR70?!y2v#oNmR?w{s2&CkKZ1$BDiIDMpNUO'
        b'u`C&xPUm96NOeMcXmLyZUyni1^^VSc9+Uyxm3@YHQ1<kub#FEAmZr8ZoVzpvB(`TXl?1jH?GcphhHQ;%9t3{8JBfbp%tQR7Aby}p'
        b'Gm%nJXN3sqBwoC`{I4qDE}}_8*<s|BmPqLezHL&;?#QMgqtCh=4Pz(Hb8giC0#^SI<BIx=@)*7P6%LqKmA$Y$6nC%Sbp0`<|Bor&'
        b'H)JvB&4{*j0yT9mC@#{M^p7fvoE*_qvRg`{DsJD%Ve?TXrb*sP&@L=$6EZ@yfPK?|6FnRYwT-6U)KT_28tvYq-Y`<{g8+n0LNjk5'
        b'{)=?LzW{x95t05#k6vg|jm|Wd|Eru)(m*$uFA5#<SD1Eiz_&T%rzzo-JuOl^Eo@vJIHq+5QwVLsDqa0wf!oqjy8Ap-0P2SdRG;GO'
        b'ia|!h`ONsu6}~U;kj734+v%RdQBj*318{c+#=gF?NAg%51YFaBU>ytqyU7PbTfj6UTfkf&>ceIe+R_(w^%n~my^fXNLN$T4mqp47'
        b'vUt$BvS^v&1P%j9(#_D+Hef`ikwpe((vj~+G+2->Y=X#!AtSL4os-Yf*NxJ5>%-!J{;$y>qVx)C)A7H6cTgZJlLhnDLiAmi{0Ay_'
        b'Wi&RfxlRGGgf?m!&Gx0JNW}-|U-Jgt>pL>j8*M)3UDDKbbX?f)ln+$KDo2Ws4vxV`K!3$h95fa+Re{WZlM>JHNAD$3OE#I(pffe;'
        b'RVj@DvrC^Y*<IXZVSA>usKPg6a!J#WN$BY^NS+(^%!NgPJUWmES!X**6r?UlQn`W!Ljki)zrb!7cO^}YriZQ{cVXdZ+-Vd3ZDiDe'
        b'As9RAian#QsC`9dT0{qEyQC>2ur+m$AcGxsCh3?_S4a`s*8DMJ4kjLGx~NdN)l`I=7GT68tSUtmi{1gj+$qXIuLj#dSRJ*~NVS*v'
        b'>Zmut!a@%QwY&jTq>y~0>=S&*B!V8#c5U<$byNhuUj5)?Lc2%<9V5x?v5F3)%Mv|I@3JBn%<lzDQyL|+!Hz>cD_<&O-Ylcui1d}N'
        b'D4ARa1E$=ERV`2*qZdE1%o#vv&&|7L%-TqwXNwj9xnSRdrC`+JiH9&`XhF9gL)*d{TIuzMHp~whTJ55A&}Zgv!Ju_qZ)5j2BO5Er'
        b'TpIa4Yhz0$w-z1oE$Qq)Hg;?mbczV=<rL`1nMLgAYtsp^QabC`F<C{fn#ObTU&qKHAvtGZdsn7XPA`Gpt)ZI0Z-gfBDS8~5PC;$c'
        b'QQMS(3Z#qoOJfzxn+oa;n?MSwH=s8TtroHyGYNsWpBYC7&S8Bam(ZS^WvRbdy<YEWTA-daT`x;<K~3@*uB6zM#)-)q>P;iN|1(ms'
        b'D8yr+lz~#3wM_yKb)Osi@Zc4`Hfkp8$$?QIaarsFpbbM`7Uq)Eu3-L<e~f7zySMX@U;gA*b|^PDuAV$rJ3sQZK?;wBDk#<8(nKA~'
        b'xMreuM^0WzM*<nhHnbWyy?_|%`N(4_2QTuqnbTmnDqy&RX6)`|;8@z@VY+Bq7b-21#*zU;VFK`He9q#gd6;Lcs!BM<5)3*ns1ihL'
        b'Ts`U9z&PUkFW@i2QGc<OQc&-sHo&0`RMfVSHpuWFX@hk%YkaS%zUT1Z-}u^uP|$oG1#R1vpz2quJX4M0;IP4#!G1%82W87X#zFnM'
        b'DMHp`ZPI)=4BV#I<shVOJ`DbK^pFWbLx4OeYScUpg1irbn;1nAFi{5+LlYlyKZtChPRB78id2Qd8_eMu;73}<+Ow6ff;pV#0}+zu'
        b'6u$nMjC7|BH}3><SQZz)U+E9#aA$^dnor}JDNrfcm!6~U&xbM3#G5gxf?u**+0?jN=;;qVM@%P&9geit7^I)wI%>DlAM^y0jp&Kh'
        b'($H$3b<m+aV|J{f3P0g%Tg6CG>n&*NsGo8sSV3)7QQI}tdr2V+qH<v7)G+T!E(lB!82kQktC89s%+rUvhWsB@UmQlJ$nEzEvbsB!'
        b'&Y{(wsoL$CN3Pi%=P_tck)r;uz?wWq4-NzBa-f6bc)YWCr!@AtsEjG0?a%|2&d9)0`V~RsPUvUEso}95-*rSE_Iti$?<MtQjO2n~'
        b'3d;Fa%E&MvoENW~8+$%1{D_aflr<i4-a$Fxo@bggoJ>a_d<J*adJ)4w#I492Uh95`2M_U0JdE9!;H<L2tpmP>qo|C6YE)70(G!VP'
        b'-^s#xvXl)f<~`Fmq?dQmE3if#RlBqqH~sCR`>Tr<>Rq^$?pfM`s~^5(dgPLdYJf<Q^bhCZ>gRt_Z}^F(-t&GhetSBL(UE^3Gh9p`'
        b'Iq#Ff46W(xVfE;s6vH<teLMkM^+N^6%&EdFya(<>KAB3UXlf68i$~kBv=H315HmJEu3xC{TPt2<?lZ&BK%Q7W-L=RpS5WH*QxnXJ'
        b'<_!tcs~2?0=fq^?P+74qxYhDIxE1TD-q?}!R7~|HDr?v!k4sK456lr?{;s-~%Cfm2nJ_${6xVGS0WXsi2ZqJf8(oX>>IJLMUv%Yj'
        b'bUjJu7i`D~T6eBQoU}b4pVExS=C!3i`ln5kGmCpgy^kEldtXW1d6b(L#yN`js70wTc;=~>ZsKRAtECurg39B({LuErtIvNdUUb@Z'
        b'TKq}OQ31(UV_0eLi5Mw5Zs255|EhGI`=^sd#l(uRFS6I9&pnm(TF1)8SsJSEKVqKEarM0@&dPOVEp}z4x{e26ucp5IuxLeJt{5I='
        b'K4wCI_aB#T{xNf2*9+-+&$td6(;qJuXU<!cn(=REejogW1bx3MeP#SP(myT~9WoUu^n7RnosH9$W~fRZb5>4EnxSIMwP7~8803te'
        b'o%7SMAs*dwVp!OfVec8yU09)>*S;#<p2;2r^Y6Ub!tB@5PhF;7PETH$-hxw)p`Vx1oB0{w_!u5hp+ju=?vq$2|0_{5-!N6>`GCTU'
        b'$>_k5y=}PRVN^#8zxOgax6AMry06W=qW(RGKEC`Zy3}y7M8}j(xZ(p&86@3wS3owCzO+^$UD95Vei}c@ZzG)1{GlM+?ZRHpHXgdN'
        b'%ZwAh#a0%T5m@5T(g$$&UTkVCis7*Kh3T?mvaAo;@8LzVW!}e%vvuw(yTD?$Lo)hLrLj6LwxWiR#;*F2z_IAv<m44KoVwVuu7}#y'
        b'={h?`Gn`jASMW1kveS5X7v09SFr+TqPnSI*ER=8ULMO2N26Kr0I>cgErPywEIm8nN%m_5RMZA5l3;njbT&-dzI=$6gZ8qi;dD#_f'
        b'7R5S1x+B>Sr`Og!BHhp)ncn7$gtK)GJ_J-7gJPPqJ9@5szb>-X=J3T5zpM@7qA7N2tXqh+KjcvaH!PUn802Hkwj8;#t0EwRh+h*a'
        b'p~UG*ocePb$yMUS%UHf7FFX3gqFB&t`6eXg4{DHdkI~Ml-NdPk)!4CiGF_7`)@1u>vL}GBaOZk?E4uQtos;-x5Y;zt4TGnb=D2+^'
        b'o!GAoB-V-xa$Gu)I0qfCu~hu*OD^=wg8NHz^f|`-i+R~3u_!kB(7J^tw9kcO1btgk`$EEEpI>YJrKKyd{hPE%v5l=a2-O>m>J1wY'
        b'wT36)YBkm&9#8HSy;WU(v34)6R)NCDiR$2LS3d536tjrQU9aG#M9laYwr5gHm~DnRyK=Q!f{x^9otM#M<w;}pRvEb!=C(Gjt;_I7'
        b'^p41!?8qjqU2)c^d4D)XC{hJvta3UTqD(DW$ok}p)KKz$<z{lCatA2$pa+Lyw_mh8hPBKfLloI!u<zM^itGvSINKt?qQ8r?J*a?='
        b'voEbp5GhuUQKOL|3ppT-MeOGQwJF8bu`Ua!Efx}bSDo12;zGYR7sCI?>J^2&_-xIG!3pu<Fw8rKn*#>749Bmb>e7^W#6{1^>`PWt'
        b'g=r<8Gq?s_!w5Hfa5${XGkE_8v6J~}H)AJr(yn1A7o^<+JNa7L|7+OEr_z2tb}~Ed|Hn@L-@#74Ip<!mlWXVv-^Nb1ssF!?oph+s'
        b'yL>NpvT!2L5rrY}<WqClrTWbdW}C!}MHKfc+62zw%ao5AqU9+zUz*w+!ET|#D4tpYw>Cfkwb>kjR=ar^g?X|GARA3{X~xmvNQKaF'
        b'`}=x_ofCFu0z@)&#AKf{<LN-6_Kd(0Au(Khj0I#m=*dK!j!#GOw8yv|lmo3fU&SRsT&RRS)pI<!-nE{yJ<p;dKv~u0=b$!i-=SZ1'
        b'sqoYU2v*elMQ9f}<p_2t0ts1&Uy&t+w))f@<Fd7iYX8Dkd4jDHVX#u6{N6pz6BCY6Z=a#wxj_A<n`-dX9`-fvVBT{#A&RRmcCd(0'
        b'6_c9nd^CCUqa>a%YYZf`mS(Ip)8xSouz1j&WALE6M)9B;szrnLt~cC>2SqQ6LR=CW;Xom-in?ya+cy%ed24Q1^S*w~(lKcCMQfJ-'
        b'h5(^i*?JEmG^%I>5Neux10YoE1%x_B0HN$TueZj7e)-t#@SsUI;6cCPvUt#4hNF*O!-Ia!y&E1>dkqijz7Y?qR^Bfj^g&S>WxWv('
        b'IuGF;3vR?a4jS(V4{H4v<3Y8z#Dh9-!h@PF-5(zGW1&|;WALE2(a*DE@Sv<_h`<}rpbCTrwXzUTA7g}PkHB5<pdLUdUpI;!y&WFZ'
        b'c^w|qITjD<{3qc--?%qCC?UKh9@Kp!9u&jIAVS>{!y3xEe@*T+JQ~g7=~z7IlgAucx59%u^L_>%)cUW$gK9_dpiY`;^g@c%H{n68'
        b'2oD;28$9Tf-pvkKx7h5EF^UK6{u%pLtoOZdMcsUF`&RCP34L<xzLl(dz=YmG2ZQl9U_$S{f7N<l`&a)5F`;)5qcHksU_!0`Vod0h'
        b'WB0CPUB7olHhlkkSFHc@dsjv=p{CdFfC<$SpN(Kbt#`nL&c`&4C%u@^teY{RVdC3kLT8O&LJ8^ZF`+Xsi{nY}mf)<LF`;3iv6#@P'
        b'5lpD$7MM^P&84?Ng{oO|$D%r~jrD&vE_6Yn7Z+Nhig__*EG~3q%JsO=6)9d^=mUxUl0@%Y@8?r)i3|Nz$}MoA+V!hbytvQ?gbOvK'
        b'AkY0KTxcV>avof0OX7{VP%ZH2#f3H?TxeN}2TwH?7wTkjp^dk}g=Src3te~%T&Po(k~4w}o#(}c3Q|0KhP8D(gz_7M3*8A3f-@YS'
        b'rJ|g-gN0g<uhR(gtQQmt0ycoB0)4T;0{1<b&_<eZvY60Dkl@ys(89z!VnXvgn9#64al77|)z3{aXl5f!=$2XiTV{DMp}r}jn9v$8'
        b'CNv}kVM6H?4dn!OL~Fb3v-&To#$ZB|XOCh+FRQ$m&>vOTVM60(-vcJJa#nxEtWiwpm#XV9p~hMLpRko0{;Kj~LjQeM{~tZKK2`k_'
        b'F`*3}OsL6&33c8H6PkB3CUkHPL{<$qVnQ1{m{5}k6WVYiCNynUzj_u6`fOH>#e~+VsG7{2t~s;%=Xf5!qq-|56vGfIv?i`L1mQu&'
        b'3d%Vp#ES}b{}NM=L4~57ax5&=lynm;wC2{Z&?Oi-Q5Nfp{^NC^&;k!A^cmGZ4hn@p?SBXp>Kua!b$T(O&f8%^)gzct=j|||&g(Iu'
        b'&QVOL^CnEF^R}2!=k=IS=QT{I^CnEF^EynZ3SmMiv{etAvN`N#RH&N+`Z8Sy3O()xg*v^UQ0Ev>C}AA~3e}PXvC#txwdM}t#H~T0'
        b'x18)ec)!B8?+fo2d*431$?L%1#_t=8mz&RJQK9PHx5I?49hJq43C;Ri=w5p(Oz7rYVnS=NYwX`6CbYtf2{qjY6M6^LI!!+V6KcJ8'
        b'yv==LLKzR%w)Xb;);q{D_{z_g<zI&jeR3==H0wHC=-~37feXDC{(mkml)ecUYP};a^hqy{BI{-xMOeYl#)ZcJym*xGo=|j~GWUw3'
        b'xG5eT!BMd7dkY-Jo#N3auHH9}!un6bQFx+Jgtpq~Y0Hsl)E$RmcZo++uHHY6;(p`Ne*{Nyhgj4ZclGDSqW6da`3G>J)?491ZxaL}'
        b'lQ$T3|F}@=KN%Og(2EPrVIq^R!-ekj;6jm<J8nRQHmIlG*?JTPv#8JpHFb-5^!B*W`>^f6#J%D|8?M8JYS~!q5eL=a#f3J^VMCTi'
        b'9o6W?g*JF`q2Qf0Uc-epkbJ`*;yoBr4LrCtE)*GDx8gRqwL95c-#g<%?{*%X^*+yoBVN8IOz1PWS^IO}=h~nDUDy7?eq=Fg1^-N2'
        b't4_EVOlZtC%$odW%v$`N#c+PbV%8r1r`p<o6c>6YdpmF=F7#fPF7I^>_C9c-{5cwCC&Go|bC5k69bd6OV|@MLAH#)O|KGxe-qxSF'
        b'9WL}v{!I6k|26*1-Eg6I@@IBk`M>MWwB8>sH1_ALt>0-p-V-i#p;47{S6rx;#f3WW0T=4L6E3s?;X)fmaG?!94;R|-vvHvfEH3om'
        b'?Ecc3Be>88L+|W=5Et6O;zD;_!-X~&7RKKa7wVkdKW`?B3$2@VYg}jpO*N>fooErW;TkTq;XZJo;K(!}T&VMATxi4fxKMQ3Ad3ra'
        b'7{!GmX9tRo#f5%%3tXrc;X<7jaEz|Ug*J@Ag*wOJLbd-iT&QCd7h2%s!G-qS70kGN_T9jY>>iz8`cws}58MhDsvW_F7Tpgnl-+ux'
        b'^+9`Cnr?{;efsC&LJ?hO7E5>ijkr+L4Y<(R$VtDeE}e6|x_s@fx|H6NE}d$m%hKzCp-wL_bQZ#!+!`0^7{!IEd_1_&{JY{pzfZga'
        b'F4W<{h0X?cOzJz~LY-b*Xu~aWq2F<C)PFpy|CkY6=*ls;(3d$~kI(3Te1`W8*_K2!@=s2njwap*E|l#&3RH<Ha4asg<~m&H(VvM6'
        b'bvUD0{yF%~xX|gQ-8bPvgT}PZU<7L0?>KivhOSS%2D^G+9l-%xT;qj?u1mZnG}MQMhI&2@z@lFq9%Ses<)an8GzJ-3b6aGnPIo6{'
        b'C~sYai5SI&I=r~hU>|MNvm?0Bn!Dgay$T5Q(Vn{{E_7kyU2vg@z+ixn_VO59D472y5Ewy25jyN+96>`fMxmhzW1yi8*Px+e@QWU3'
        b'k;8)vodEJIxo=$P=(r0Lp>e0Zd{<oP<itDRLOr9dknqu#F1ijE+HkM9&|UY93w3yLp;rlQ(1J0z(1w2m7wQ<rh5krrTj&2wT<EBs'
        b'4ZFnRLW45yhzsqWbq8FihnDj^q1~H$FSyW#Yq-#wd%}f6SCq!u1PbO2=!yt)ckP=U#?gUuSYLRS(AFi6!G$)A!G+e0;6fj}JuXyr'
        b'97nd#OC7tRA3M*0zHfmItr?3Aef^f$P>+TRKLh^mf(<R6b$e{+OJlI14(BI?w&yx*=reb~hR*k3LmM(CSNKBL1*woSKfy=9p&khf'
        b'|43*n?*<Olc*=f^UxyEMcwmoxgm&dMd}v2(e|zjTe5iQVt?;1@_l6H;-Ju@f@80mCUX33Der|~m9Y5<n@SzQN!-pbU>93=9dyM4`'
        b'5K#dO5%pq?$0*BrfVek|XotWw<tB`1!YweOw=xuAy9sTk7a*FDa|?WEPr{VYoj2h_PY;jn{H`N<X9pp<d`TTNf)8!{Dr6KNT7U7n'
        b'8M5cY!EFS>hfYA~&_)kBw3IO{NbrC|iA@&~HndmAk}~<;IA3ffBnemDT*%W{g}y6v05_y2uo%&s_NvcLVE3voL>tZ92frm*xbb^*'
        b'pch8EVS|Nvk9}u721sgM+Kj7DUo?H@0g_r-AgSpWm)x>TC_ZzJKuJwSKbcHkC@I2%W^nSwItDjLQJp6^XT?8I2k@g@Cw67@+k-gz'
        b'B=INc^MBcDW5{F;lW1g=#)&?puQ5B#yxPKq8<_}mgN~VPWTK3AeNdj`!#pEH8=0^&=23q}=Ffy0CL#LAsKhhW><iSR9d`XuUeG>t'
        b'_}fqOg*E3exY33O?JFGk`>G3e)dpIuo+l{B1)vi>Eu$9@4r=B!p5aHO2RMmvlmCU%_Dq?i5;H~-+6b)hhrb*CrYzsUj}IUartwQQ'
        b'9f|@}!xxa|#7_r7^ywjb{l&PmDQRZ~q_qMk(AxTx;>gZFye(3FkeVh%pJM(D(I$Bre^5;%jN3ldr~0WD5O6&)Jtc#Sz6Nd9v!7&E'
        b'h48dbb5JIS9x@pnSb2bt{C!y)?tJnG^x@_tUezB-JTfF=flO8qxx@|r-UDYi=?gMK(o;x$%0_<=M=Oeb=i#2OJg>Uo`OfoVJUt~s'
        b'MUrU_oOl!yr4DQqANwGnZd%!g0d=)zyxCW3)|YmdCoKQk=L%^aH}|xD`^AENM!o)0&%Oe)al8FetGRjn_U#w#_KTM<Z{OznVZ7dT'
        b'>HPLfAiaK_%f3BkuUUUS2A*POvAtQ=GJftif9lw2_N_`sTX{sOmLosa#_=;ALq3DqS918O`ln$G1L3lqvcgPGO%S1Tb2>f@P<#+T'
        b'l2*|PZngblpZ;P`tG?CM*LSH}f2q&xvRB8{nf0!bYRs|<(cIX%`{Fu|4up!Mro`h_OW2J=P#@j>(-c%6YOi=)@&T&vC^3!n;9@zi'
        b'7~&1D;R;3)Ut98dMsj{OO+}viL$J`0tw2E5+TObUkCjJ-9rkm?Z!u+%GD;~_CdAiva^GH8JdvD;Ns_SG`Vy&f>a$I<!3$V?ElHGc'
        b'j}KzxL?uowQ)JP8k=bqxLs-rDY^r6ZT;(@qV}y!|pt_aC$&tL|F6CmbJk_rtRn{9oT)>I%(ZUC{OKGH{OeB_`oR{4-RnZ@%Xyc*9'
        b'4}T3a(NK=M(WxE{6~VMANq@*0$uDW|4OE}QsrQtT0`*xO`HB9=sEHT4cz&PDfVaXNPD{N!)cN+Yn9WKHHIZ>Dt7H8N7RVG^ISDk$'
        b'RZ;#5CeZDNrHdmt(R}dnHY+k!#mPxd7Z#L+HP)v&1Co*o9Nqp{KoXWxj|r0s?Cb5DWrhaCO^iiJ2F@4mT_A$t8Q3)()BmOtacr>1'
        b'qAhH%EBjwp8h*p3tCam!N`noh(TC0#iwrr4LYG<DZ&n&M#g6PuL#3-dxwijOW|+%nIvdk}Hl~Hi+9^wds#DRu<8_>7#*;kCJIyzw'
        b'pj1_+l@Zx&3>lEe1TRrB59G!^9P^yA?=f*^Y<CEDEQI5r{5z<LhFF$F4<^bXiF`)KJfMcLL<)?|1My;6h)ZN4xwd{~S6qvb-AYCB'
        b'lwBG9c}xwTQ`}Dq78RBBYZ$SS@pJPqYgYtA@?<ubOkQB?QZRlhMx6IKX(1=(Dqd_XBs3rXl>a%&E&e=w=Ho-^KvGcgZFqRhste@g'
        b'NJHdvwr_($brSbvEbsI1$0Ver<lFF^s8v6Zz7>Xw=YnYqJoCp$|HyC6hM~Yja<a`}dv2O9+$P3hU<=@OIz#$brb;(vz!O>I0+>YM'
        b'{^xn0uezxGHp7qsL^O;9eTcr;Q1aX~BCi%q&m=Mx?nw9TnRGr?tUDOcIcaIf`8J=h16WIY@8$k5)c5OK>nAA<$EJg(B5KX;*5@j4'
        b'@~@<S?GA)Vm&N)?zKe}u8vUP@$)@)y#KjEtfHHwDm`<U6swADZWDYe+3F<y<JYfNq%jMGz4<N0#B=5;46%g9`ESYqeI3a-+g?2Se'
        b'LTxUk=L;8$<T2E`A`^x&e5H2vmFDEmY_^4cP-%An*bj!JC4qc>QbAJI^u9uI_K)#UPif9!{)tIYQ&K8r;KX`s%Dxy+5@-jP&(nT~'
        b'`NzUIbT`Lv84Ysz5?N9*wJt|H{c4rk!SFg5zJ+=~Qo>^g-@KUqlksgl#91?1BRqZ%kAH6KhGN5z1Sj4E7P?Ym`ag?D-BodT*f6N@'
        b')+eRY4JP(GtMN?wb71`6Mx_rYpU5_xLV3Do#`O2c8~%jSRA2np!o9TYf=nCA?|LMr|0u}8>!A2&7%9yJ8~#(l?$4B-#*dD7Fb{Sx'
        b'L551tdgX%_DhM7l2H}L76LU1?=y>@td7I#Xui-V6p(f}Fq6n;DXrD$*wZ~h(T|^(oPxwo0WW6M&eOWxvzX0^#kN42OKm{KifBw%h'
        b'!~3Yh;&ulUP@3AoOj0qEJF}aUX*b7E;(5pVprJV4J5ZaGfl))F!oyED6<|CpKSoV5sxj1rhF`LL>|IuWS>A4rXWQ>Blov8WF2e%$'
        b'anD0KYVwpC+?{}RotO7lg7^U))THIOVLhv>zsdX8#sfFN3u_muMzpN{Wca`YgBe}swR<vTh9O=Ja}eR>Lc^oi`0UKqx#fmcp0c{f'
        b'FleNlTnl5QL|w<^{gK{ElOptnGR2rehDYMrebcx)+sk$RA$j|Q@risx$#wZ;tSp(B+83L~6RC7OELU=gc!7hVr(JvH{R`s_i$^$j'
        b'e>@C6o4<mZ7@4fhhM{{Vo`W`hreif+e@Y$SH(i`Sqiy20^)w}cF=r5!9M@n4k+Pa@EWSNGxpYZhc1f~Yh{ZprT`li&$ouDj1cJ`>'
        b'hE&B!Ph*8oe{MGKc<aON-(rUiC)RsM*-Z4r@O_*|Nte(+dMXVu%ovdga>A4Y8hZrYQKi6S6u0py^u!RQ@aAWm_=`Ap%WpWk!8XsI'
        b'(G6|ge4inI_jFEids>Y+kq^O;8bh$zcqVa^8oQ>V&on$tnxjd@)R8b=x}KHy3*%?whKX#;FO&EGN)GNAngWinWGlaO|AJ%wR&toI'
        b'em)c_rK!Lw9lbd=Di%gtgg9{t`V0!?7t!Swfo3$6pC~0Qj7WOS1r{3oT0bKtE;#7wF{>CqBO@kx@y|tc9Z$hn#Jz<gHPkq{O`niM'
        b'O51#FUHSdaT5Pru`ByB>_-|!T#mI78$3Fz~U+`2+0VF4J%v}YVlq|CgV)u%!EZSAlZ=w7o89WU&Ve6&F0NDZVQC^!*VH0+^{(#V)'
        b'fTm;TMy#`bv9Qg@`D-k{9@t89yWaMEm${n)=U#}W?9DLH!1LfhI_ymtT;ln{#=w9B!lMEx=fJF=&li&Xp~x8^c=6|u3J)<Sll)w3'
        b'Ftatznq6xOU|yeION`I!D(;u&NQ?5jV6w7vfDRcXiQp8c&MHEP$)}qo(S-9g%--m-_P4g!?Wu3?jVA0xu14*IU^m<??rNo5i%Pmo'
        b'JS<!t&_<ZM96iCUW@~>%mz~zPLKHQwxT{ej>a0IXAhsK@mU?r4W8k<0JpEzT_i!MG8rjrHZgYLo4%y%q?D$H&nCYw+6_Mk}t!+Lf'
        b'OxP04Y_NXYQeW|0)t&=f&+S15v~Q$*bccrvie<--^Q@mYD$`G$IKVqCAfJTiPl1s+AZ)H5Y=jOdMfxLovqABaRTr{oc_b6jj+$M`'
        b'%;uSy;`YQzQnNH1x?u%F@(B}W{kHd&;`YV9YV^Xh(SICxp|WnoaTscKd4o)n!|e#+z;rkdn<nht+pmj*>CkabJ?kp8QwXo)1G2jp'
        b'ALtc-)N0uA2=eWN58%+!8?cD>y!PVf%*mxWQd+O)<@ZM#7IQ1QW(%!`=6aFs0MC{jmNsnck+(e8Tz`OXWFB<Z!9YC9Jpet$`3}_9'
        b'oM8PH>}hW+JjVyE$hN*CMARX#g$V+VIzI>FA7QB8BJ1per`ua)y>*GU+Q9jZl3e#VtY#P1{CQ_rL8)wek?gDQ8z-xvTXowxEQPQN'
        b'>;MmX7qALNhk|%tCHNFmi8V_DClo(tbjLuX(>QrDTw8_a<ir|XI;NH*NVqlGn1Pw%FbgHn9T^52U)*0Sd9Je_H5c-L)zJ1ReSqKQ'
        b'6Sv8C@G)$$5XKJ=D|`(3`1VCIPs0|bf`ZKksky>n+B=LnC?Rx<u$d5~i$E#TaG+eRb6KCOZS?P~Kg~x)!jggZavUOgjO2Snff_-U'
        b'!c`zkOTE+N5hduWb3SJ$fnBt=FSYp>Gt#0GCQ+ixz}&uAq7@k)LZq`0So!4B(h8`D;9-fr;A9kp%XHntMgpr1{0_Ck;0)~TB~@$V'
        b'CJ{)Ouo>6^E;P+_w0~d8ct)r*7OEtW-H1@AFloHfS3yN>jg92GeX!&YW@@OYjCQJfX4NFO=nBEbDA!CK`0DLd62j+7L_2%7QX4*a'
        b'$S2!9V>vgTf0XEbpS>n=LIT?E)sUDZ2P^yV1MLIDi6;wIx!w^rZHiNWKYY~Z0Ab@8x=^39a=r@6<F3qc@UhyuK<51!ZMd0`hUr(k'
        b'^hV0~G&b1ngJP|@vCUlVqMwK_hS_?Ldd}niJNqSeh<m9WGueMDZs?d<y)8yx(NS5U*T>k+uKM{i?VZN$HdjpvR=;&7a*$hX^;>4P'
        b'n(ODx{Jd?Zy~SbQlI+?mw(oPbgp3}CW4F2L<JpH!^sr^3eT!>=y=~*JSI(T(TwT{;|6NR7UA2V*;(dF>)o;1lYi3rry0&*ZT9$18'
        b'&*b)vGwV0b+`ivfxo`WiWP6)q;2l)e-qz~cWJ5KZb7QjJ=IDp?#^mZcSN*z~_6mo-#bvKgu52|_%(OQr>nj}9mgE7OL;q&-UNe-e'
        b'HoN-j#I3eI8~hCH5%0CZoq@CB%5SEA)AyO9Z+CLvTX56$qxiDz+aUQ=+j*NqdID%%aQ;~Rj*Fc3#qT()mhU}1uwUG>Z{Q>NaqSbg'
        b'?jwVDP2-Sc&%W;ZnDYHTj`x1wY9_>(-4$@^?XF0LtH<FQOdj~X_+0P6SLml#Og?m|?iXDl?4vKnJaYAlU9B$iA(FIzwZV9J);V*<'
        b'^Ty_lmHSA+o&}$z*kUVIPvd&ebu!w|SJK`z^~6lLjKJ9&=z8w;*Xfq87CP*HhPsE54`S)Pd{o$<GP6EqW{17Va54sNW&~wKWe8QJ'
        b'+;oe1devF8Wgtatj?YYQ=AGJW5@6B6<XrG%<7cAs)6*^K)3uwgkV2CXix5Wg*i~RsicL(y=GOo6AP5L~r=h%(x+_Yc4ADqtWWwnB'
        b'58@{k@$=Fcett2t{ujVcrD4}KelilOzKgJ=PaIeyPFGZ>M(`rJN}gBd;uJEd<AZ>L)&(zBhL}bA>WfJ>v|6#qmSi?oXI)xk)@NO+'
        b'u13oQb><4u+<lS{dFdf(;mXd5ZMbxw^PA!MLbhVw%z6$~ywhMs6(3Id=zWiAcl3~k*@!{*+msiFXY=NU576SMkbHk>k!}eOwFEjN'
        b'?b3{On_$pXzZ;`BP|%@B5jmOl|IgdR(tYKTe}~cb#V}jdmow^zW^~wpZ+Hz=Rk8?Ty-czutudnX`Q<*Du|~V_7=axX91tEm+Si6x'
        b'aHK_r-wvBOaW!8k4*rl3=f<!tvGa-LJhDm6$C6C0%GJk!J(T;X5AgWSu(T*QeCV2<*UyWQ8D$Ww)tdRB2ioqpzGnuc>287EEM9-u'
        b'ljgY~EuLO$=1rvs%;Fj=1Y!C&_|d-l$km?yW5(NXeRb&DUy}Hg6Hk(nwE|zgA-O_G`l}~mdLyK!`MUj}PW|?a(|mhpK{EtHffuy-'
        b'7+Y1czIr;F=IPf!I)F{%P|)Wr0feM<ReFUGok<k!Ir9j7Fx>e^kIvqnQE!{kQJ-XxBb||f%0(5Ktc0NZ;*`A9+(u$CcQ!BUG1<#0'
        b'#i{0y(%jC8xy>BuzBatD&qHF}jQR>7vDoknM8eV&FtAg+ch59mQh@x13VbfTTk!+^LBPNYvFcy|xJE0DrB6q4D#Rs}I}Cis08FCg'
        b'{lGcu3z|GT;RHFLzgS>4_C0%XVBk{0H^!CbD05%mrIVlO2QHmEeI%w&hStQe(_;PWvJ)|LhbzXJ#dCYh=X^jf!@2`F5|S6;Yy2SK'
        b'HD7X^E)cu$0LN8il*uk$E;@M}TQ2_EM;0!N98U*wbPwS!+6a_O>0<FodhY+j-q*)9b>07;dy`y3a;Y~YL?l@64G#f?HUuAlstbVz'
        b'MD1d%pnPXXsDRqKIjhn-U6ZtifZ9UZ3PkOaSQKbkg+6GtY{+b?4mYKpZC&lGtIqb<cGh*RWlDaZa}yqXs@iqmeZQ~Y?;p6i_dI;g'
        b'=lPs_?)x}rRIx|?QJHx#Ic!GWj3y^n{W3|t8^C;%&fOjr*7>`ONm8XcFh9hf9HciXwv^jU6Qy%8&dj_6BAi~aJ~p8@Fjb;AaLWB*'
        b'^IV_a9V@XtoyJ>Yk%Rz#O_}JO3jF$&?JX_bogXtlWxiy7_9EB3#NN}LKA6&;J{@RHq^Sjx#S)t0b61G=VGE-m-xUGd&ji*=x&+Wq'
        b'`M$ui$#{;vWkQRnsO{2WQ5SyxQJ__{SmHPz;GG%BQ9qYEEG)>~Eib%VwPH~mh1Vs{RmiFm!FCQ3r(X&zm4MV}aeH`|_yAG8Y4p+2'
        b'6TOOwrGB>4`<|^0Q~8=i<($!0ob=VsxpVMfo95*LkKw9&XI{y?7oJb0clLJEl6S>OrAH^co_4l1yhS|2iD<pYQ$M4rIP)*9;Tt{~'
        b'zXC#L0o<P+j_-Xbt!gJ9F?I=>Uk;>Eyly%Tjk#dupDsGtBvbd`)k?R|o#8ulQTN-6yCsc+29;#Zg@(JtbTmHvZ-?$9jFJfTAhQr8'
        b'TnsFbynnn)0_wdz(Ca>WdIC->b&#{rk;#SgOB|`#lPWi@Mhk>AHA^s6v|EAEzqWxQA3e?&)_adlur0+yKAU$Sx9_(Ktg-_#a9E48'
        b'`@cMNSPhI4Gz#ZM)b0GzWc@OGuXS&?$%L0rcWTpNu9EGvYSVY_#C~z7lbzuL^*=EqFD?AdsRt=BatdeUS=leM)vPuhte7thx(S6@'
        b'CtCwNNelma!h4VjNk8ZJt10IMJ`SoIzlQ$Pbgh#~cTdQ6P8FYtR#>g2*2mM;9(lDoqJH`vNUX2Zc0i6pA^U+(V?Rm%d#cMrRHumR'
        b'x2EA|b@gfCJg*)$l=Wb1T)oQt=EVY0D%mbfcq!mfcP9&IU;4@kJJjRpPEThylIrzrz1D?YT=A=-<!@e4Ymo0y6kfP|&I?ajw%#a1'
        b'G+q3v(ER3w10vs{e`ud(H`1>!NhLkYyHS|Fo2|#CU-q(lS?<0G?B-Bgx;HMW;}CxIf)|QGLu@VU4+PT0Q^P~~8?7p@g)HiQiRTb|'
        b'bom7DvI(8rBsL0*CcSWiDT6WH+uS=5Pa%=**QwSFHj8-u@fqIfveRvW0@)U~lkjLuanQ{4>N8j*(Oa$cS>_r7xI5jPNzh5OLR;`u'
        b'R@rpJRH0vh+KKWVflR`8h|Mz7@+`xaDBbgiv*)(Woib-W<=NKV8U}ndJpcQ`Hi+GYhE}R2Z)b+A`IiAtMt4>iPxFk9b~53Uz*501'
        b'$y8}OwLscMBzzoLOFHux86PG}o!yH-Cosg{5+|PRZ;uY^b`sh1An}9$)<1RgbNs{!JV5AFY0$^SKJ2xnb}$n(Nw?WXPdEYrG6|zk'
        b'!F+$;&r^>oC#ZV@w%c(SE$SNx)#7zU`j~Yc*OI4lLdbD}3b)B>?QN~Vtpd=p>EM%hWPM2s!G`d4weG@TJy(w+$)H`wRjcDPEo!Yc'
        b'Z_95_CdpEgTSz3(dqA4NP@R{Koa`QlJ>y0a!@ku(K(-&am?Z99UY+$1n#4~qq9%?tbUVpeQx6LFJ(r=iGhKqMg6h;Mo&)Ub5ANHm'
        b'ee<!=`wCN!5)*8nVGp^}&Zu8Jv=fwMAyU6Uf^w%gxqoIH5VB1S*N{=Wp+?BQ#s-Hu$wt_HLa<)@Y)WlGYKzcdQJXDsWtRBmmIT}O'
        b'RJ;!JS%%u<si~*MHAn51$Tb)2v%~BjE8YU4N`XHyw9{^hZI!jow&iE=@4I3`t961dqP&LWb9la=b^&ygMd&QT;Vw4vUA&#4!(E*6'
        b'SZOhCiSOx?57%7CK1%=Lu&|40C!yC<7FC}m=DZ~~;c+r#&la@rw`pqybnVhGm^G=Y553kYMQg>Ly-d;Gfz)@Znj|g=$g1%UJj+Pk'
        b'Rn;Vf-{Tz*epR_{+!U&E3<<%rOpKO${=BS$`B8P1l61r&mzanZjd!jYF#Y5dO)n-)13m3@>?V42-@zmFv+w*ms_)=$-kC)89XyD!'
        b'p!yE}@|{WPeFs~M+sAMEl-ThDmFJh;G+p=RV;dekOZ2=Lc;^nOr`diutgRiaX3a$)K;?9N8mOS@)VM6No$h^`-=3u$k362zEh{$A'
        b'(#$MuOhs>eO*i{b1d8tdnqKGsQ(!n}Iw1m{;GOB`0>ggotd7UWJs~_SfGlhH{;A>n37-w#|Nih9ztCNc&-j^c7@zU~=&pg!I6vb*'
        b'hR=9c#&^eOOw0KH_>BL1@EJAZZw8-n?D+rP_>48W{}=HYEoiN<Ab!Kk1!2<(S~y*{R7i>N3&qjKY*auLz?}kOkz#$`bV7M%pfRrD'
        b'Rni!bd~(Y0oHf4|f5_iBXP#hp?#{cr&&`*)=bC;gDw(f(+BBP6(o{G1p&d)o@g%_J!*j9T7{_gBckW?fD`zW9!7rHPROj=L?rdW^'
        b'J=UFVtZxq0$Qi{5Pb+NC;u>2e@2Bj}g<m!Nba4N467Q`?s3~{;oWdsk-0mj9{J5=D!>hzrYPYOKa5%h)v%Q34cOzF2SC`j4J+46D'
        b'e!4)@Bq)8nyGB#A`@Hc$KrN?c3ibTP5E!T?c{IOk0{e22&a&CgZB|>hsG})^#cj4cU1oV^xn+}XA5&G9l2q`i*~e{}DYgBCpIdU9'
        b'Tf<wY_qN%&Ep$(^7>xZ7VLEQ}Ofq>+nYYf&131Q1&}8<+HD8wb7mk2$tTR~h)RuZ3266PLF%FIopBQC%b^%#tc}~r_aZFIDbtKx5'
        b'tNZPrisAxx&TZ9oE8~KAjg8rt<27dCz362_d(j(5;5FjSaa%gM&E+2kHpCdWg&Djbg*GHM+PP=5A?0`$y6KfWHih9WaPN^cwcIy>'
        b'7MJB_uWnlNRhgwpWtb|mTedD0+bs<)%P)iY$;&Nnnlf;1)#G-H+aN?AzMf8p)9%!nsqKFL@z&-0PyXons=cJKn!?%rFCGr_gdtmJ'
        b'y4~V&#EF2YgtrEG?8a@j`*>}z_~7R0qi~aSaXz2Lt9<VpW!pCf2~y^LV|WfZcA>$Y{@Fzu4BwcCXa&^?f^gFf_Hbl4a3p^hX<Qbj'
        b'nodi$hMin3YuhmdO(;aFyyXXuRK51s)cmSw(*K7LcH@0v%ei_CO(;FmCd1#ZJ<o4T+s7>TX;-iLjK<#&alh>G=^w$^c;snophdD('
        b'<g;uA{qT=PM{;F-z|L9zG3eAj#{2>4ONfm9=ZxCe>iqGOR4;d0>h0x`)f&p2Aj3gzhenv1zq~xs%ssuF+jJyPwtBAljf?X{=b?=s'
        b'nk`%B3o%9=t|2lc$bi+jLY|>K(!f1!<~Eh&8TMZ+fZTGcf!n$u{Mi1#>h-1Yi_SAH!^}zDh1rvr?QaYqESwb}nRgT-m!-*=huOqK'
        b'IAS)vMmkc$e4KlH;gt}Mm`@`h9I167J}GXEPvt+sIF7=0kw12bM~*=rbpnrgn9KasiK_iQmU>rtWJA&*kAgUtJdf-=k7_ZGoIxJd'
        b'2zlM+D}-2t%U{7Fr*O@e`hqzIOVa`gXeu=~(8)EOoFUtjcMh5Z+i5ajFh_V~-w$!*!{yvohdE&ISRJ>cPR_kH{A9Ik^}~k!N6vxf'
        b'uE3mxI&Om$KjdqC@TP*KjDb`^)i#p)Jtdt?EB$w2BQ<yyEr)!lL4v<5avOZeL7|ygs4o2M!R6ubEDV2fgX3DP(8V?A@dsWF#?(Nn'
        b'&<?*aj$?yADFEDleO1-Ah$9*J1Iz3zod9Fr;qM`Q+QPy<-vnUwNGuNwDOHRy@6tpt2vtH=vjnPwptA1*-2^!q-Y3iABV#YjD2jco'
        b'Dru6c+HR>gFN`dXqjd2+-z)iV)D}kSxTg)=CM>ZG-ES`z2#!paWlx<h&<DSH#Wh4w0~mjK1->*;2_iOpK<M(Uv{3f}X~@lXY=EfM'
        b'5GxE04MuF>>We=njXL!DtNGg)pb~#5mAy#tu$;#*?F^1_Mre#9z9A*s1*Z!FizE-nz#!j(LFV&=gu!J`F~%YwS$Bdo$3?Dj{CsZd'
        b'T>SCq%2-E!QWkbn^~>*%tV*PGar{_|6NRbk%=cr`&Ag740QDCz33$)<J&T2pD2#itAH$VIPzi>M>pX6_f5dS43dRl|0k|Q5(b^ZN'
        b'{B880!2H(Wry{((cvzdyBt{!gG(9L8%8Pg#(!EbEkBj6n2iE1ckknI%C%NqY$jXE;=soxiVS+IA?kj1&2!mcED4a#D!!%T$B^`I5'
        b'*NgIp^``78<XCily}>+f&Ipvb5%uHCX*0%LgEr8cA;JcEd2PBD33!`dEVNd{`704$Bg9BtA@4FqUc^-17vy8ZSso^2)yOe?yYAyL'
        b'lxqTIL%N@TrSAW$V<;`fx__fFfRJFUsYA4bDrHYwBmm<_=YzEW5cJ^B1l$jffrqfc0#Jccr-`Ux+6_>30{F`y3f>6XGj5i4JFgc7'
        b'i?P4FT92+EeUYH_(ezCkWNa0cmX^{AT2MOSsb$Mbf&1F3?$kd*THr_#V(DPpJxdzX(d!i>bUjmGyn$~jj|gN+mWqtyAg?LUZ@z6%'
        b'KA8eXNYB(DBXwl(o7?=PiTpUtWs&?hx3Ur6+(xRor**u43VlX<Bwm)1mPLjzL?Zdmg=NE^3x~>w3ahzilLfO#_RjQVx$%{2*)8?>'
        b')piT_Fx5l0;i$O=&0x0;XqfCUpkm~=zt^Ulsu{Ff?d3WTj1i+7`1=b3|5JFXo)g5O3feCf91DHfSiWT_Y$sd(fBxr;C6~vc3h6g*'
        b'iM)Q71qWaZp_T^6(JlxYarvLGq8}_UJ2OOo5KD9f{TVl+-**}PDLnn(rdK2NdjVzq{Nnc)bDNJ21Y@qT@82AAsXaFrbE%!zj=9ve'
        b'Vy^XynCrQA%yr#*%zgZNF;|Wpl{bi2uMd>PAnLw<Ps}YX{nB4?!*~T$E*Q4iE5`sacha|yAz|kL#9S)v-!+C6{)smca~-Kewi*h!'
        b'U@13<x6cjyr{gUh21coSKA>%4Ap56<4ikwp{-P>=AR*&4ioe}36B>udQ8jFqFb?3M;l#*%f8veu{ZpZQe-WSWPg^Vq`pa)m_ZJCt'
        b'Tmv1i&tPHrQ$#vTL;Y)Mx_3!)Zl>AuFdb&j&B7l|k0A|sZ27}u%lwwHwF~g*%4@-)UM8avV*{5nLPisBRz{fu-qU0S=a4s0txN${'
        b'qCb<g$efpL;F=PJV-E{yX}iF7A(j8YC*Msv=9AjCZXZmqi%EP!T52M{kkLd7sX64e954kAczgb~Q6n8N#sU0x|NBVD|N5W1Y5zO<'
        b'JNaM7hM@Ny(%tL$Ux)oV{@3=M=RA(@bIv2b;hd*@A@6^0b<QIS^0F#HWcI{=tN%4--Gu*zL}|$X-g&kEoqPlTJCFCjcl_J@?@i5l'
        b'=rCGAam20q;PRQg?{fSta6=zF@s@osbv$rG`vw}1K&ko-sV@Afc!QlcP(RFUHdSxCZKQ$vc~@2D(=K@+IEKZ<2xrwrHvb@GpAMWK'
        b'RbOeJ<`bkY0o!LrX$BMf&H9I89o5N`RgEsN&vM>AgX><C6EQYb`QVtGm)U3S6N|-<L>u=YzDgKW31VPfR%fV!aVL*y-H^W+?6Z2<'
        b'?eh82;8;SVpsYO6^bpZFKN|M2-(VS3w~`LXk1)yKYM()xFP_43sC|OMKr#)L9|!HTn%8Zf4A6XI<+t;+JO$gQf58>B#ax57<VnMX'
        b'UB^D1gSs8!B-kf)^_s-+KuSXP>0c1!W5dV6{AlDD1jsn)+sBY_JGM`M>Mf4pIy!#!7*<e|Za4-3?*H|QpbmgVX8(XsE9^nK7XiiZ'
        b'5}%2$NRJ|erg=LWQs>}`)|lXdEF<Zjc(ZhO@;b48vDiNpd#_!gWH3QmHi_Nx7UUOU_eTS{kX3*nridW5Fyv;@aaw-a)DTRf@)!eL'
        b'doU!D*@O6^P3GL}#PCEjHtYu7i;rrZ3<P3mla8jtwT(~JX;<_<1jXtypHj|IBr0Z_x#ue4DJmE5Zxd*%iBf%h>HRs<iH7~!(najD'
        b'hjI+LXqkg85)T;mAEA{&WG$so4kUzqgdtOOZwyQkLLn+2q4%rlrz$fP;L6JUTHPOsvfRIvdFx^-j6dM@$?zPa#X9ae{dC5U&{D}-'
        b'=|183qtC~+Q(a+p%MM!vewQlE@Ey|naxn&$%Bd8J%$%22`9!F<n0}^mBGDCQevv3Cp~LA|)4|7f(b{Tvnw|4?a@(vK-G{~afYa@^'
        b'#svO@Ew78)ZWa@DHLP+S##DD5BwQBnzQ3j%ePXE3KP3h6wu=7x6}0~f>3A>TP#_;r-KIOV(9C&C^%Dy3HVA<(7-Z?f9DP1fx{zJA'
        b'B4?SAEqePB%p+llI!jYbh0ee5{S_vY&}?bi@Q+|-_%312{foiUr1RhJ;+}(aO54<pUrRvlqZCdH;)NM_D68Y7&XAoZ(s>9o-<-jN'
        b'OzGA#t_d0{y?0L8yJQ)ay@68A1wPW6Wsfi$!p6@98JBq;FI~hGDJ3p$tEr~@Of+dsK(V*=`QktM;&|Y^<(K|Z82h8~3;Fn-Ugn#K'
        b'Q%i}SCDNw0?KSEi?w6h1W*@f&_;AY7+<eCX@Zl8KT=dDrP97I!&ujJr=Q=Hopv1mEk&SK8%z-_sruALbcf9anAf;yPA?L>tHG5o3'
        b'Bv5F3&FwwD`1APdeca}uKQt!~6cwi1`Ic(&>$zYvc1gCfQ3y@BeAzu1{O!q3?g{snrU-hBYOmYbG`42XYi(!Nhpj)+XKD2F&>p9T'
        b'8vT8F{6JCv_+X<}jAP%Ztj3M?_zHN`lqU|^Y9i<)Ra0$M&DiCZCta2&&eU9|t>$q9McJC=JPOn@49L=$c!u<A5a#6K?lVf#ACF=q'
        b'T)z0@Ubh=V7@$*JW9RRfgSWkRd*>qQ@<o#E)m*T#!{MNIeU|3(m;unaKHy;+=ktC9+-Q5T%zw^jX&gjSX&eHp+L=<B*6!jOF_Oxj'
        b'ii6>0i=<F)d-b>xKufsogs6d{L$PH%nM<5NB{tu@?lTI~ABSSY?Y?-ox3-q2uP;bnMAO*LN@-c8WV>UKJ~7A`NGxZtjDf_Ww$Yb?'
        b'X*B|=%m0k&TeJh{+oh`5=S;~@Zntxd7({1J-a)aUlBX|(q7#&HxpbgNA|FQ4X*6(+ptD&*9rxs7#UT8J9iz5jsE~ItW(y2?eHIml'
        b'hC#V-Tc@dkq9wQKcz_P=T~=@}nvX`8aa--&v!<dsB~ED2Zh2Pu_b_8T;w3b_d%NO;Sn+aSe64r&YNHhS4ly<I*4GxduFu%+hz*S!'
        b'+js(j2VGPv9&UaAIZ!><`(($gltrzt30huLRpcjiO_#UjO@{`yJJtn}KZ1>PAGV&pcu6Vw+9<<1u#Z_ls=Xi4!jx$S%M&_KEYk%j'
        b'ZWvOm{R#b-luIu8MHt&c8A%KxV(@LfVNJMj$<A$danD``PVp?>Cjql1)ie3cq;bauW9x<B?`Hh_(+kGWFJR2cCh+XEB2hpZs|Ot0'
        b'2GrcMp?zA7!r0o>nUn-M<7VuBEpAr|<&^U{gVia-!8oU2cibL)Hr#G8-j}rQHL<Fx!S@#4>p!<im?R4Bb8IIo1j04vDHXCSD0~8k'
        b'lWBb0elMjpt<bV7oQf^qG=9|365$j|oi##p0dguRG3pW~h)Jb;fcgT`O4O3qDBP0Lu!oVhc1n<Dv$$2La@Ht}6tXX5%y~xp{yg)3'
        b'W6j(1g>)tz)%0b}NAnf@9>v{nZTYADw|Uh(mc)!??3CjenoNGHMy`pboPVzoP$HC+n<`Egz+L$e$i*P`gMOtwnb;^y6DZ#lO%3x$'
        b'pu@s;vWByX)X-E5MTZx*wNfpF{<qyt$}Z}l?DT~|q1wqEkZovNy+T{nZLR9T)8nahfpRxBc|!ML0nqUkhYwm-K1^wy-Pu)-P&LZ6'
        b'qBMS=sc>W1T0&j<Fiq+zA2L*~HCHYxtNfY0a=E(lC+f;I>dF=B%Acz%SF0;msVg5bXx7>_Yjr}Ta%%No8j3%#SFY_<I1Yu?Z;PXA'
        b'-S`l1PX(i_5ZW~lWkzq8k9KJu@@|dG45!x{1gNkO!q2Y9Wsc7RotlSynuilU3n=$o@_!sKXjVZDRi2@8RY9~WLz*`|I!jD_9!Q-t'
        b'8N9<iXetTa&Z5dHSDyF$^pt0X&$EP1?({6}@jS_IX@{qMnzd#zQl03lT-)ba_|7w=v5F|}A|2z<%!2A?NSN9dXJ)3h;LDkC8JU_p'
        b'87?0}&;|UTgp5sLQ^eJ;kj93vDUHRMq_G^$%*3T1Lk?HikMO1cVW=pdc>v$N2hF?y|BXu#wLT2}Xm>T=nB8+fTsW%GkDS#}q~q~0'
        b'e<k`FN)-{sKbW)wF7&84ThZrP^bX&r-Ln`sYbL1GVY{BeM`#!CC5=BteVzxQfIksYE5guUq1q%=JWXl$EW<tC57i#Ry%Z3}2g6|O'
        b'o`><TSx{>=9`<;+vl4oz%EPD}0`q1_6u_p;aA|>AfItxWQ3~Uapngyk<!@tAQ2H<g<y093W3s|^npGf(F{%vzT_Uq)rG74Ju3Whx'
        b'iuz$#tkCZZ=uHzgMEPfgL1OaGGhySMpb8ENqNAuNg!D%yY#8g$3+odT#aqMqXY@M%ZHT_x5rO!Mj;UdFc`Q{Qz(19L{EH(itovRD'
        b'?oST0YgY8W+qdr=GZt+mA}d$S7tfD2d#t8B*0>H#^GzXXyd$hnv-0Fd*>UGNr_6rfNbNd%<x2nBzy^gw69%-V3W_r%(uuUvP`Q$N'
        b'H~>6&IJPWVY!rvlQP7U#9OC~Q@xCFm55eVZlpHHISFUk<5qv~_0gPGO9%lCFPxpx7h7X1iMTIKP6u}=_Wc(EB*Pl-^`&jtxs$3H*'
        b'GM+*C3rT8Xz^wVnWXLO1&<l>@ZMU7wkd?hdWKU`l;7?sqk9T*cx4Z8hVs-DHU68Tw49p^pV<BHR6#H;lJCx0A5%6alm1&m4OnOqR'
        b'J$TAX<xg~#%O|TvYR%8^qMllqYEXl<YL@9V%TI;?-djl5J4DI+RuRU^yngXeS+!=Bx)4$0@s`GqNFz{ORJ@G_DhxoygcgBOcon_P'
        b'L3%N{xS$ydPK2RFk0f@|FtK6KJ3rsN9=X7qlA_ii_Wlj&wS%)LL1{w&p9X*;NZuVu=mn~Hn*=Dyo(g0L1{oZp);&yZgzp^!7t7|U'
        b'MfNmZ?D-jsVjnA3XQ&du<&`bfrA1W6QM$BrJhiFj*G!k{bZTvx8gDRMf@e1^f)aHri6=r(d_e?0DIhH!sKuoX>ZLk$f>xKH8|H4Z'
        b'#Q#<RjRtK<MlVb%-WD;;+bd~3{Up%pkL76%4~>T!^DohfbMz3MVL&G@hig)5)~qt!nLb~V97DAP2I(Bs+AHWRU-$jeX$D=rSvo=f'
        b'H4@{af%?cK2h_1eCebza$~CUa)qebO<Lrne8e6g*ehUzt01efLCxLO&&F0G0^hEG)&N17g!zw?zm&efx`M<}({|!)x0{^#4)#R#N'
        b'1?5`CNZVS+Y>%NJ^y9sq!J^H!z=jydKSWTV;|ym{M)U@s80~Dc`XuPh+TT<pkj5{_iisq(P8ciETZI+ii{}yGm3k-AV_cOhJ@+!o'
        b'#`L0zv3AW*K!K}3FLKZeiPhVJj4TjP!prsdCxKa#r9uBtR_&97N*TvM{s{d3az<9Hy*fTaRbT*fTdKpx!>eP1I>fx7u{ndrRzQLY'
        b')YeWHV}3*NSrOPiL;N1960g<8>q6yw6~^C)W=d?YYw#I$lHM5VbJC?*(JHi$5va$In#{B{i|gvX)VxOe|B4^1SGR<p?3CFnZMN(<'
        b'od0NSQ0GIwPPlqL{_oSQND5aq;$7tS>EblXRU+6ZNTvK~=!J?wK4cE_p<RGEk#JvNs${8XqiB}M5r=(cwNDx<nI@#Z31DV?#WN#u'
        b'l4?;|h#6Op?J{;`lAXYg^;u%9N|+x@ugQ-@tu9eFi2F^Y2{%%+DE<I!n!=Y;sU8o40ryls+WeWINAoC*`As)zd=M)M$k>;RT)hM&'
        b'l8}OT&b0PGh;7>)+o$=tbnk1it#rjykx#QEv2d)<+XAh)Dy=;pai<3@YqQ#ZjJfX8SfRyJ-j*J(6*TZfc(By!&kw!XC1^e?@KydC'
        b'o<pe$2}%7><Y{Jmm-yx&p2AMe&)0miLp7&Iv&!A;()_%qa#ckZ(6uCSdYDVIQVP1h^5Qcuylj1{yUxo=U){BbtjxZ>T@3A?d{t&U'
        b'i1W^k5@@?O#{W~&o!u%tS0NjpaaiOa(BW_+uz>by9%_s^GbX7^0>lN`Q2xUJPz0RV60;%Jm?E;i)V(vEt9)t9mW7bbL%&5Ie@gWS'
        b'T7<R^+`$G(t8hb<vGS5%Dp0NzE)_%80);Z83&aiEVzo`(*%i=q_Jl04bvFdsmF3d|%C<}IC;H_$HG#sWjP8=Wl8UV8>0&V8CD?%d'
        b'b1u1tEbIs91!KdupuQ{;IEI68$e(2fmP!_o4s2uQhLDXxxiNz=q9FFM2JmUg;L{A)r{!PEry0PfHOWHD({A-*5-XJf>r{T67<7u?'
        b'3qS1ChLvg&*{h_!5&ASMZKo1LR%ZNKs0NFn43PqLB&nI8S+mG${Zg}=^nU>9HMTM_SeebD4(`o<PdI2_@DMJO#Hz<n=E({T_W6Rv'
        b'Lca#0dP68gX5uNxWu^r(D^CLJT0l}`c?JxcpnuGF9Dk<3?aB(j+3{neIt7-ZSqW06W4i?9cLvh1r`aOhlBm<HoV+KZOVUEw5<|K|'
        b'!Gxhq^GHgbssg4AWtETklLT0&<|Ffq0mxE4&oRErs;y$BGqb2fHSA}neVd<6hz38qAn0e!m;2c=-p@|Dwx6xMj-Q3lS?jpApRK%('
        b'pDh=HpDhb%z>+l=?3IrgOL@Tx%Yx2!(zu`+WPTWOv$hZM+)f#D3B=wiR?oxkRpm$u$EY!7)2TEO$bYFIRYcwKZN9Z!4AM7is+I<w'
        b'>s7uLGvFUQ0}>{w=9#bbt(DjDt$e5%_N@!9$%En8j?Yv`6Y@0R!&h|P*YS1sWSRz#a=HOKR`9BRC7xb_L|eqFE#OlR9R`=WJ6hES'
        b'&NR9eJjc%~GQpodm{>U4=iPakGo=%Q&h(Ub=b$GIxl!#)Y{Jvnj|QEn|B|4$5IiVQYRCTbaQKc!(lH60mm~1eP>0??OV3w6y1LEw'
        b'HD06jzL#)b^Jt5t&)ae;C9~7}YiN7VuGJ?Fk2(pn9w}}#Cd}vk_3Abtc+W1M6n%QU&ua~C^!Hk&O{@31*LR9h51(N``+eX-|31*C'
        b'c@(M^y>`jS0UfK{PVnFMkpF%V{I?zaH%zWpx-?Z67mv?)eMM=|iNCUIkEnPLNrj<y3j6U_WVT|CN0EZ&lqJV`FFse+qp1QXPSfDT'
        b'4`ZG-MxPlo8u|xrgPTqG`v5R}L&=6M#yub~Y+sB2YS&b4h&EpOXX#7b_Bn`_@9g08nUAUVD&vUay`y~b=-ghJZ3-81=`PJ9IG1{a'
        b'`r@Amv`hJn&>xN`q%gsR3BEKBOk347J$mw(<THv<!GU*)oBz)MQ2Bldl+z_4g8=FCtuS9Ly7yx582^g`n3lRTs0QNNzP;dT-`;$D'
        b'VA!r3F0<?F`8H9|w^awvJ-gDk6@YJ_&ga!3-*$DrI_%nbyS58bCAJ3>LZ01k71()`juxn+!K9PzFMbtt?bIRxpFlyrfKB@oHt5^S'
        b'1lKlhFzr-|GN2pz_U1za*tg?+eS~j!{A<4bCdZFm`z#73TaY|As-#U#DwVrQ3aPT{DPJzKW_54rsmzFhl%ieSMcIDE^4SLPXtE$1'
        b'loT{`YWQH5@_K71(TMZxVS|~*=>r3hW^9S6erg;ggKR&N4%a6?wo$;cD{%fE?vfyPgDV^ree<<7uDdtVKTbf4?YT(Rx#8`~y;4X&'
        b'>e-O4>NJl)R8eK5<moCOfv7?~O&~sL$8LCKtOzoB6J+i!Sw$;{Gj}Q%bg%mQx_7#B;Cs#8VP0Qbb8ET#5fWm`;rO8L)vh_OhM4j@'
        b'65I2L6h1ka!e{;Y^8CG!4d(C4B^Pnlz8HOL`fh{}vuZfR7)OSfox7|FzJbB~-Tyx!f5$O~f*6CZag6c*7YgO@<>@1G_@9&iat{BK'
        b'_#5T$<*AqF@b{6uB@lk_v>Wnw--`ov2iYB)Nh%rn<S1CNnH6{rvB4^@7eX+hB*1S7CChrPbuU<f&|okLmd5eqiBLR&Iz?HRjEM;K'
        b'fiFD)F{STXbAojcP~wMY1)|DeKpC7E{C3>n#6VelJTxshj1LTlSORwHN+HgSxqZk`fvX8m3<ReH8<uQ{btGVD3GfL=qi%1Mf`uM$'
        b'f<Kc#7U3}S$X{VDu(01e2f?%<7-Qx<rP{k?V&z_0ix8s*?Dg8VjT<&xRR-9szqnudhA^GD9byb##LSyFW_q}Et^s0<bN-n8=!7#-'
        b'qk_bAg_p0xw7ee!<>=aiaI+9;=UUAov_rHX;!7<ww~ET^NBpuQ6SQ{a!ci|2Rr3pDcxu3}<6WLVt{7Mv^s*!J$3^@)lZ*GW(_<g2'
        b'20xp0wV!Rc+|N1(=Mc3phrsJhAwN6l9IiEiP!_F*81q&fZ|BOG)pmaF5R5Pr5{Kpve;`H%7&GRfa?kRS;pK4%FL>UtSct=m(4iTT'
        b'GhdZAo?aM?ESKfXnM3~V*2kPFsI_N_uN7Mwt{Gc|ONH3!mxi3aQF+}slb;c@W%;>09A|_!MNoN_?n;O<)MZiTh4(^HX4K$xwz-T~'
        b'mJ+<+vv@2YRCYF5L0vmN;$7iS(BUrVAfsFLQvTkE4L+ErT)aIrO;KxBWvf9y)s?Gw6-^U4e)SC`ZK;c;^JsDLYhXPqQ&-v#z6Wy_'
        b'I(&9%oU8H|F0a+yz%M6PP1%A;k(k3#@sxxqwL2z~{_$vvWJi=4CwFR;x@X5T_-ygi<M{ub$XI}WR124mJ5X`<ZN4{t<MFKcY6(8B'
        b'$e)9J9?OnbNXHN0qM|sPG_r8<Fn%Wyhm6_4-(4T!cgCHX)kS-e&xiUvVox61SGn5P_UMj}(#<bC3YM_JX~r3+YA(=g*8Bqh{{@b1'
        b'KF#WLdt~19xIKG1H>1wV)!sYfJb8>?j^E{KR(r?Co$HeAY4f>}uW~hXLD%kTTSa{pfM;~uJ8cgb{~kb93m5uceAMwpz_%U2{H@c6'
        b'cDc>I_5ifwYeqmztc0&zWuAdldpj$u`ZN#C8!MeVf9&?CFjZ4i1V%vU9CUfu-{gn<O>Y}eZGHn!42$0Qq<UeB*$Y0fs-(F36`A=!'
        b'0NiA!2;nurDFf!pDtPF^4~v^fqk@Q~yZ19ipH6}76^QNRUAJAcX7%2lyAcR^fuwlh&kUNMY?+kLCtwhtv$Gug5cmt@J{<G&d7FTF'
        b'P<FOsKZMfdvER(djJ4+{k5fJE8nKpdJcz1&B=siZ*So1VMy`YZ9zQbn1|Jy@;eBI}d88od_XYgT33Si{9ZYHA^N%am>QAQ(4CWvC'
        b'{JRBsf>&$#cMBuv$+(;zyqtacVtwA=V!iquqR;@T*%j{=s;{+HZ!ScBFMh4y2$Ji_=ih}4u6|$RUC8NiSI|51UC4K$7i3a6{buPc'
        b'LH?Bp>AQu>_eBQY?{82#X7I$2)Equx4iUfx3E-19|GhXEOpT}>%s1k+)LayN<|w)P8NN08Bhr|Ga>~?Z%^J`v(5}^cLAmmu5jFo6'
        b'gWjC}9T|kwh47<vkkuoX<F6s-a(ZAm&%BavF5p`~pIW74s9JoN^R3}>zBxzmt+u9Bd?nu+uEn?MlKC+ZDS{l^@>Tw}!IuIK!R7fd'
        b'0aW672=H^ndjlQM*0@+_e)43Vt-vQu5*1o9inUL^Jog(CE#!WMGg^cD!TBno2st@vWcg6x`4aHNX%z2>bzZAMQ<Xg#oLHG=m3BgR'
        b'Nk(=>S>-Cf@q%6Rh%$)+U#}iRRhF3?Q8=&EtWZ7$`tV4FFqI}@E(xyYqyZvUfk35(NyOK9!ka0WFDTQjFen9?RKEJp{OS!(mXne4'
        b'IAQx77r}EgwPr<8*#Hm;jTQ<1x#mkl<s)j%BZHVWyWeUj)xXWtY}R&qthPK{t2cYic}FBtd#uTSQ45T%Z>b9(RSWL+9a^g{B-DaD'
        b'bs=gMK+;q2mvi^ZOmDEZX&evx1X+9Gk}k<%Vd-|(_6K}#u^{=a`G29w5N1$?fTYZ5!}57$y%XEXg#BO4j^T=*78OL|@y(8gYpOua'
        b'FCx#5f*(YIu8W{!np-Gy{Ft!Qx0w}G!)dWEUTGVJ8z0(hVRgpY@1=0Uadv9{S*aQdpIX>()?$o8lNYi2ms!@wHhaHNf^UexMy;UM'
        b'tb}S%r#0TUkb>Xz-6kgszZ>7ynpQX!TI~vDtFZB-hNQGEVLRFUS>T0izSY~*3jW*_AmML#s^a4i)4?`BOX*$=I8+EF38m^}q1k|v'
        b'6e@MHg0FKAH44E6-r&Kq!Y$bidu03`kI9?ERnAsnjlw~pZ`tJ0+c(^2AMUe-=pq;yTi!qo;eFcPWO=Ni!-D3IgV?R#AI{J_?A16!'
        b'Z?VHTLr2+b;0(>?{$n^p8Qgcr8A{;(KhDtq9-N_9*qgx_dY=8?jWc9p|6jxz$^k`bC%Xi_^J*0BV(4DKpKX5V3%dtAC0U~g`Z$r='
        b'vc=AA!JB?9n}@)6HaL?O6&X;wIN`o8IQuvk*Q99*Q*&FAA|bQjelbo5H=dF}J!g{L(ggEMZuN*lI<=*#)2G$#WA?n{^AM-?l$~o*'
        b'C-J^Nn)ky=O50Dz@pwK>5V0qh36rK5`2?L@6W(&V;F}jdfex-bWNYC#{*W!LVISk;>h`?6<{#yEQD)1t#(&@qRZ!j&ql>24IHtmt'
        b't8NV2)F<G(ls5c@@9$o|zkM)A(c<c_HBYAcxTjBX&z$Er^>CYmeV6}}@L8VqpX33T$wBC#dbP!M6=;y!Th|$c8&YTAwdPB84+a}D'
        b'Sn_y)q36`x=Bx084BTeDu3I@rRK_*h_c7Bc1NUT>au8Oi>|GKgo;-2paS7g}iubbyKkyIjQ^n++J{8yyLp>V;6w+5%gNQ;}yni?d'
        b'DdgWc0#YawLkdj`LJGOBfE4l*Xt`xG#uM6%KlRy+@r3q_yB?m<qa*Qzc8<e%LL84LbWeW>Pw2&Q!+1h7`)>kIXxbHcLYqh62{~5W'
        b'5}wffu;rZV+Bi8Au7#6hAI1~fd^31LuKxg@&@_J|R+wQpA-4m=32hz$C*;2)%*SmWU+D9oo5K?tb!&V&{nJ~(6LS6A@PynLPiQlb'
        b'C*&T9C*%&{32nX>p3vs2@PsyF>)OoY32nX_Pw3z<p3vsY@PsyBh9|W7GCZNpH^dWiT@O!a0{*@*^J;vF=6Sb>C*=C?z!RG0c>F3n'
        b'A=eGD4JP1kYcsF@wzj<RJK_ns{&RRj6TaiOwXW-bEOy10wT^W`8onJ*=vsQif0sJ(7V(5!|2aIN>y6=b(k<c%x&Hg{geHvqwl;Ib'
        b'2Yd-*ZyHZ%;?2@N65rq^zO4=63AJAzPe>!Q2Td1rEd9FJH`nt`r*HcXctWm!6P^%{CggwlI^V=UcD3EYz02{0oY%w?a%@7wWM7kt'
        b'E2!q%xgnm=b^ZM}1OHQait&U>FZ(wBR`ui4;8<=)mvfrmwQ$u)GH#8{StMT5{FkwWCXB!m${c|ul<?uLVF}$(4%fmGx>?;`KpFpb'
        b'@q3K7Z+%BBA=iI5mXQC^YsA}|!xD11ZZ+OMe*Jhmj3sp4c>C*H#1eA-o3VuaY1hRPx^BGf7=a};6m6-Pt4A>TCRsZ&*h25<Cc^D^'
        b'iM8e12maHs_9`r)dq|w^UmHv4dWLzr>DI7>T>lMNLc3Kwme7<Cme5p;B{Z5e;IUm3OX%vc1+jz@HryJPkn1L}UcNJy&@=<*9>x+n'
        b'9W#U_WDa5pxs4_sOXwFWei6e>3#pmpwHz?cny!l_bY1`Z^Fb`3ZU1Kf>sWtt{?}m(df%UKIg`I_2y4P&{XXV8-ye?9_54<O#Vz6p'
        b'-Ky{X9&v=O8$U{J5l6`NZ^IE{uZJUaegAvUt>Fl{{%tryF@rcle0KCLI6@OJUQFgSaD;LOafFWEG>%Xf#$R#WGLFz|*fz^~+vL~0'
        b'u7@M^Vh}|LY_poTO@1tnM~BAooiK!4-!q2Lb@`ckix@(#Tf^V^J~4!@H->Wd7BPfe|GgMO6GmVNjWo;Cid)1Ga{aer2u(5MPQ5XP'
        b'klUO)?ItjU+!#YhARodI@=v`r459t95Qb3RFouxfTQG#Od0&q)ghUuasDQx`20Vz+-=mK%9fJXVY?q=(APA}ED(@A#I4>RT3rDUO'
        b'3AdY;*6n_3tF*V6-duSXu`#SVJfYaFHuLa7ri|{xB1k}fJcfTM=A}jUaH2R`h*z1t`;JE+og3`p4@!K{SMde9p>h{#{Br<*w}10+'
        b'L5>hykUIz$^f(U}<lZ9U*{>bM3vv(Q1-W^=Aoq3ff~F1Q1-S?Dg4`qUf~H*`FX&kKFkVpnWq3i<C>|~-W(*G(^zqn(dxpV+nufrF'
        b'%5{TaLB}WE5G?3dABK$?1Pf|vyBsU1DTpJJHc(Wky9QR!v_Y((X}5wE#5el;grtF@{?uz>1<kw#te{|9<#7W=*-8I0R#4Ljte}M3'
        b'hp>XwH^K_q9erc0ApY%S^gz*}v6o>5xo-t4sA&XNP=aCzD=7L#SV48s--Z<wlySnSfg*|GN~|DvmT<8`$34Lx@ZwfwxbuK?gXKw`'
        b'1;36x^H>;^T0g;0VR@7d$-`eR0eOtl@dM4y1Rd9WtkiK^4cxP)Ide+#blj5$%d^V2Fj`O<h{)KzUGe82SWx}yM;ubT#xW8uNEI47'
        b'h6`#I@^C>V;m|rCuVB!ij;=qE9do0H(Sm+`4YVMhw!_V6KpFEj_6yg*3Yvcbp+U4DzWDy;OP7>|m-sa#HTPt%ix%J%&hms`c*U3#'
        b'{&`6$8MwxK{9labU(4(9OZAQf1NgiqV1#;12wo`nDd2^J#(REX3dI8qQQIz1%@_EeJigG`3&u|_VE^h4;tPpMqjkWsWe8u$f~FJm'
        b'Wn~u9b|3ERUE-|l0*5zhC46~l=v+C{E~nPKR|nBzw$UCp#%!5lw`AGnVRX2CcE0m5mnG3|Npfy0vrM&HQtTdU%sk&4^XwM2-IB1}'
        b'GA+`=Mq1)+^G5S$08Tl@O+C*|>-1O;3uE@;y=#|dNj80g;6^(cvo|6AZ)?tb3{R<L#+l-3Qal6)<l`o#32jqwBSB0f@3TtV#L!Rv'
        b'w_9n`jriT^L3mpoLY@?M==?=bfEH`AXxoX=wQ4(wXglj<LT8+E?~Q(8MaO%i_0O@k_i#H~+z|MMwqy8u!|{%{M#GP{_#YB}!yw+*'
        b'<{9l2+utSB;v~KeTg2$lKDX2TgJ+c68b)^soZ=HAds5bC)L~)o)AZPVJ)^sX6yCo^Liq}bm=;c_44&HQ<nUR3wtgkw)@LGoLSOkm'
        b'huV8=^k-D4z2Iqo{N6_XjLafAno6Vzx8$ukwMC>BBJ~^ue`x`&U?)7qpZRP9zKvchN=~0nED+GnS)wu_Bs6WC&WED~q&2`4{bnHb'
        b'kHwoLWx$+q<Ky|$5nn0ZB!u7N;~)GoznYsO%vX|BJ~EKV?D?}PkNMHMVg-)%WhAlO!>D`69P8-W>qi&;80DOgnq4z`*^}uf#D~N1'
        b'`I|MeZ*puBUeRQ&T=1Ul3k5#DclL!GTC$PcDoK;jv3-7gp5ip&(g^Smeg5CX!Vhto|6uTY=|2B2@r|-Fe{0qDA8qOvHrzFHSCg=1'
        b'wkA98-P!bQY`eDZPue4Gtmo6mHr#iXThm{8N7`9gU4xzdmHh<mcC$O|tj5>2JtevHm+6(+1RasGc*)i@Njn`p4|q*~8Gjbzi9m&f'
        b'Ih&rU&Lom=+bT*EzW<V+Mq5U)Cj1VFG#MVND=keE={I#35L=$xAdzM|i7YWCM5w6YZ}bkTD^N80Z*(=aH!wALHtgW}jLm-ygwELn'
        b'd0MfY4+~BRyU2tyBkr#rzTf=O;C+za9ix+TrV|?lbj>U=mR?fZs^wv5BUx9)6zv*FeYZL&z0o1*?XDh{-nwzT^c;CudUnsBtsp&T'
        b'wSqJnu=HX@<JG1grhC^#bvzygN++5wv(@s#;buwSm3beH>i9*}VUf*^32RLs6xW)-VF|4YiA=OK0`GhHHklO%Wj0}Eev|Mlr<s;_'
        b'maBVP%l-;W>;&!k(_<SJoK0^Z6_nXCyv(E^vt~P+FhXW0=#b2$L7BCW;$>zG$}A@+vo+_pl0lh;U0-HriLBdrnMIwWo2lOfik|r!'
        b'y$)n|h0My&j*yLfST?6e$}D2|e);JU_ctj|h@4`5_m}phO#XD~L7UA%di|Fh1zYCWJ%Rk)Qk|zZi(GSoKY|_7Ogb7nC&c?{?=EFB'
        b'!L~7;hIOukw%7-pM8o)n$EK5}$bPO<X;SyIgoN`c;U^+ytU{%mT13h=k*!UM<CXV$B?{MjJRLj4)43f=Ie|hIHVsv{b9=O;!-tFQ'
        b'tm|+)*L>q?)mm#AhX~oWDtGLT6kwVpf*iyXXLBiQh$JEuLu_@*`e&5jOWVl~o3gr9Q(q5%CD1fO#8CL77p8+feHwYX6^XG-V(OTp'
        b'Eo3K0v=Ge{;gF!+GPqhu@Thk9x?Dt<V){#oek1=)8I<&KsK-N;mk}mOzn<+M;>q&s^JM8DPZkUf@xEh?B4w?}_JGo%0G?C~@g$!s'
        b'8^M#=Llx4FwV;j#SMh`bp3DQDFhe}SI!KFy9Kq-E#<0~Z*L=geU+O$yi~VF*is9H^WItf1NvrEAeCD4wU-`U~O<}x7rAN)iE<w?H'
        b'WcTh$iL>3UL{h!g+L7XnUA~h)CE9AO=eNC@$bM9ZPtvnC*+XYdLoasdU~v~&ojmziG{L1Q+3`$;c(N@`31Jh`A#bV@iSZyc5_SC@'
        b'___|a4KY@&wW=AsU{P^ajGIQ15M!}CW0mz>P@Xj15dpGHsE>ue;-EzRk*JGEIEXwRMPiIBG3EA8_h7Msgc1q}P!Ieg;bR1{!tWJ>'
        b'GR5LE62T41L4lq=gMw0qe(Qqrv<*bnQ=xuiJN_1h`yGfH>K8mq7ty>A(W&R!WZi8H9qZ}s-YvszO&`{bVZJQcN>-<g=FUcKI*YhZ'
        b'qG0f>wL|@4z^c~PshLoopx@7${)l(rcL~Z9ht7t!AZ+u=M3$_18nT^=GNtr8#V|Q>`aH<m`k2SM0%R{Ih@t`^gH)*It)krmt|!W*'
        b'>(>(FSD~1MwV!wVCMq?$MzZsH*7jBu*gG`gz<b5@p8hy+34g%%nx7=%2&C-4s8<j29`7o}{U#J5+y1CDiBp^?j!k%ycz;O?ary~j'
        b'Lw}2`9RAfNRDGVRPL^=LjtbJNeF+ajZ6UIV@_ESiN)#|8NHQ%6Qd~4I5|o@Fcyb$MaRkAVs#QqNJsrhsKG2O3K^#8-BDp7{V044G'
        b'?}B=v=aZ1$+b_r=6C8wqAeAW*+`6bi)0we~!Dr=^Fa6x^;p|Hg*BIp(kH?G4KZeT}xhWvu&R6|J1Xge3FSCI!KuPrJ#h-WljOSXr'
        b')aKxsCh5oDEhH@ZoO>WjKoEA18gv2LW)Rq?5?Xi^bCCN*6zCF=2%5YKP2(PkGDaZoz9_6W2<T4raRd-?dNuBD%W+W8;8k{W+2^TA'
        b'H4^ULC_apEKaPSHLV9FDJVVjx4+XX|-2Ub41O@oC5e0=GO>((B6ERg$<qJOV_`#6y@8!o4)34|H2Xi}U*OnWlXG`^J*3`(bcZ&AS'
        b'i>gzzAVbX*g@-K#r=WG>`(VY|w^+^V5r>5*M7BA&DZd%$yeFze4V8Nhr!xu1J&3;3bVvF*HRCzUY6GHk@L-@qjpKZUjx^ql@CThp'
        b'|1sNpyFVJe*|eacG0i(Us$+5#6rz5Byc422CPqO~Y6>`vsE!Fy6_F&Bg}lj89oi@mIr3_vI+Ac{M+Wl7M|C9P(he>1Qc)cYF6~G|'
        b'UO`j`8D$)g-fWb6RZ$(PsAFR#-sq@~*eEIy`mb|#TOUuKa<Dpi?6JAX_2T}9q;WyxvvuPvqj>?5kV-%#_DZ8V=qUc|dGF_nj?WZ{'
        b'kzt8y*{61+0&!m|W=VFMwOt}ghW1579gT>xjlx{PXTEzcDLMue_*<}jVNplJqHJRPWZwnF(Qgzs5zjmDcit}*9sf`m3FQ4k(eb5X'
        b'<hkx0A1G{}DA+$S+P%zYBt2$V5<!R4(X?b|?NfD5cE`I?+i}G^NupitV;$2FD3>V?lrBZTvmcZk9`R9~$^`lRPQgCQ?AnS~54^_|'
        b'N8U{D>9y^6g0ZH_dS0}Hs!4m#sbyy(zuu`yKmVd#-D8_vJIcCVmNp7MQ=fCnjy)XcezF_Kg^k{?Q>C^&3hU<#{`&;$d(qAw??z+s'
        b'SKm9-(vFuEKyLa=@RwzKyZLVjp@B_q)SHdJuR`Z)WzycAE!{<H20XPdrMD>F&#b#sRNte(D6vgR;eIJDFI87>`x=_wp^j4bJX+@?'
        b'xK>3<5-25`!tyyBo6?O)9GdEq*pRQvaVgk%MmvF->=Vr*(*#q6wswWq&<&Pg%IME;3Dc@2j=P|4POC!mTvpC{_{&12{74Zz0TFOd'
        b'Dxhq>93LbydxOH1(C@z!<vgn>R2OCh8=0BMpLZ{`xfPR>#w+C#+rw}XIlDn&*l#z9`cXy-Qm5ej&Gt0hdc9U%8>*=_#MtT-dI4DE'
        b'IIEqhA;3+Q3i=s?M2k`wbqp&kDMb)g3Ss=#490f9!gPPXRc$qy`?<#yrJ{b*^8RIHVW~U@%A1HnD6HqJn5aS!ce6(T9$hIUIJ2TI'
        b'k6`1i$pp>^)G33$+=g-r6|)N!+J($k0g$SkG<WtK1)ImLCG!*L%7k!QRO~b1bQxK46r5gRqWU#Ylhh2tyHL@bPWZ>+U}-B;R3;_a'
        b'EQ-pO`99C4(&}_;Z8wCnQcnlgj#_VJV~)ooq!T=IyB!gTPOxPwsyE%?O;vE?72rOhMaLu}-#5x6=sz}Q7B@x#9*)ux=vZ>VB**dB'
        b'e+PkVEL4hyC&xZ6^o~_@k+wud(ES=UFeuv(6xB@<?BK{0Dh}V6rT{0Vby|zgqBR#-r}o$)RQ{xZ`g;JmEQ01Z!Ztn<Dtjj>Aewue'
        b'R+x>`G1fhg?X<3FOz+Lq*FN@o^s$e@XDGmUY|>C)$42LJ$%>RbQy$y95TO_&=1pQ0X`~3?yI)AKkBX#K%bMBV<2cd^VuF@Oy&dqz'
        b'Dk@X(`OTb4k*^+gZ1ES|XL3HRNuj<5dmOFE_leGo`PlfI0Cz^7qg3D&QLbQ648CBn7P3r<DIQ<v$iUB(ASMO+;35=^Iz=12z9`p5'
        b';xZ_`pVby-<e&mVuV#{o42X`}60I!8fxmS^miOcuM+8SG9(0-v{d$z5*Y|UW<oe2VkUi&@m-%gMJX>2~`$nEj&}4p#!gfJUN9MQC'
        b'1w={(_d9t?-gLO1^QHWxT~?bX5JIAXyu0O$R)V;gnjArnK>rft5F%Tb9QYPTh#<N!hLrlZ<t@ZcHIbV`6vzaGpe~P@&Utb;?<si('
        b'L3;97?}zd^1ksj<8QhPAG5WZYT(H3p<ZyjIM0-O&cU+F*N=%}ZocHB;+)9b5tiM!W$Q_eI{sPx%VIhowm8BqKf9U5C`SA7chp(Xv'
        b'ZEm4S*k2k|$mB_Kb5ILWSI7i=)(T1x5d#?p1Kc4C5!<hiD}<~liKsI$CPlwqUcz<Bfz?10$cWo32QdLBxjk}c4nr2!s^ui&cF7qe'
        b'LCQmxSLL;K)1-c6>ereJbHzxXAYs%JXm1fwm&kx@naG%ALNANKL@7!bCPq4!TPR;Pmj$u*-knn^H%;j0*2%%0YeAs0Tu6;%Kv>Ki'
        b'u#EX~eL{+fDP%2@`+1Q&neB>X&MmL@2`CC7P2()C5g3cGun7r!cMKAO&(U+U<otUb&IKjI)9dA6ZTLG<P2*VLIxCDp!~?6)7;Zft'
        b'8zV>oRv2eu{Yn3coF=QcO`knYZmmwwBw*qI_HMFvWIL^zm6lAouE&N1`qE_`YtAp@)A(ef)XAtlqfJg$tLD8l+i@%&v1}>tkz&B-'
        b'rO%RQ<Op-|0Ki{o5kNxvQaKwR18yPxL3z%DAk-K=n}UBnAV(aQ9D-?3d?7OTqkBuh@J+e>=?mp1;NtyQC(`ei%X0*#Iq<YF-698l'
        b'M0fXxe%>b^zShd2Jp2r{V<J;Z%VWT3^{@8ZB0~BrCj?;qOk`ntAhOO5_9O%m0X-lOkQ^kOZBFatbd$LMj64En+@E1z0fqd50J!F%'
        b'`JfFY=OpFid=_at9|@M0pA;b=gxrZpK`u&`Q}-cTmOMXc#q2Ek8nHEx0f%gxESD3)?UCu+Bsr)fh@txF+qenxoC&;0z&9xR88!xH'
        b'b0{V*7gEj`K`vo@5X*>5h8mJk4UIe}DOf|o*O08~AFLsP8vY+68z;wmIWm!t6E+`3v%kX5(G=A`J67)UjDxVpGKI6{a^!X6n~`#q'
        b'eF$zcf)ZAq0u<=&{X3FlIu8X-{!Z4x$Xzd@Lwk2i>z-zIjS=FM2I=$Dtqm*dp6;gCH;fn62&ia;W|MNTD`=02E18Ytrn@mw&?I<L'
        b'#DIkrGGvV2+K=nyb;ma4Cx-*05X6RXh}Rb);R>upFDS|RDiTG;fGvVimdg5BsL0~M#R(8@kY~!Vp72t2KiqVvk<A6J3}zZan6bel'
        b'Xq1*vIF#w%Ot-(dy0*7&17XeU#`<M-V{a-xl=DF(OrjBqdzt;SNO~%ZQjp$_6o;UBc@6<TfgO;*vpAWTK%P&h89W4f`>ijIM4s}H'
        b'kT)}4wmbqIGY|p+f)PTm0s+Ba5FSryXnoXH5t&RtK&pQul3N%F`V8h@oh-%k7YG&gZe^1g?3jBZ(gYSy_H$j4_4{D({Pk;*kQkWA'
        b'!r%pKD&%%YB1jT~*RPJaetGzs6{SFfcr@VQ5=yF*MJ!BX#fW<@vi^lgm|IjQi|eBz>l&>t3&OUV0bT*C8-mz2sMk3HwPh~njXW$o'
        b'X_OVJlgQ<kBDKXNO;B6RX3Ly1%j`8hv`~{OG4x)Vk*YUr)8}$#&SdAzs`w*nS?x--<zDtdNWQyiQT>=mEZ>qOQ+WTT9@NJb;Uq9E'
        b'iA3a~Qy$OB1X;}IDR&4ANHw>3$GdiJjtg!k$zqyPl4%jlsrtCNCmUq$t#RQ<E=H;<@Wps>;zMENM$&X!Ki;}$wja1y)%wSiD`l&H'
        b'Cdh||W~lo(Q*rz8lX<d}3uLD}=ge<hjQQMPnMXff@_A`q_bJQ#wGjqO@yUEyVGcw)gXdgf{l@SGVMZy+Sr}=4BLHf_GASqrYedeR'
        b'Nc@v10R=HELMQJIR+`}idpr~M`z{K6i_7v~J(eGpKaX;XA|W<nRU=a5IVCu4dw(DY42&qj28f$2adH3E!~F<1E<A)}G24~t(j8{c'
        b'xtO^p+hlFcyCr>GF})H+=yzH>YV&Z`?etpLcbCrXu8|;--fHUbOVIm9X)z4!<Xm81$$j%grg<E8^=S4*8Tc6nJwS_KZtO@z6p7A6'
        b';Wx7wCpLkWs`A>UeV)K6FQUgmw&M)%-Lpk(eWJT2eB&rQ1F~+!mlD<98BOits_`FeSKgVZ6eT7q9pOk??E*5J@F(FljpDkxg^&eH'
        b't2==Vrz~b~?RtFg-X?KHLj2KInJJ<leCn3kF6u}-3(Ns-lsBOuA7IqL0ozkD@URG``7n!5Mbd`$a2hXW_d$buWHBf9bnTW(+jctH'
        b'Q=I9qZD%(u!Vuz3Fkdln^XV~${TJsclz$xP<K}=K9nS}0$9%3TF1*KG1v9liZr;gfWT&_ycYE8fS|nXU6mzIuEYCyWiSVMxDNw89'
        b'vg04bNl``wQni7T>HOWrKF++O{V(o%`E;yBdBr<+8CM06v<Y)MnOD>#vdn)$**SnWkf^zPAyRaAcH1o_&FhivpbYYJQ)WLac;I9;'
        b'<U=K^P$qX&20X)oIx>Z6vRZ4bKF>MCxm|A(DDu$BM`T*AB&Kck>h%>!?M?<ebti`f7qHcCtIeujG-X)>>zykreU$|r6XcX6;PZ$6'
        b'3p!dF4n6Sk9t$851d#Hxl<`TVv;rFDUXnpRA<xHCMo6oUZNIb@c<bFMqa+x1s%>u^g)*c_-9x~@%ltyH7fl+eX*mU^m%_;n3Tc(f'
        b'x#>-GvQoCh0xY9R$5(+<-0U;c!q41pe&N@CJ^zkzb|OsSr=hZaCSXrW;!<*LxPwD*ZQo}~NrH??+5{2l*ujAfQ9&2!*Wqu(%VfTN'
        b'rX@?{6wEx~Ii7E&g&!*$fR3Ob(=X2jJyFn+;F<6|3(9vw`3Io93YXWkei~|z@ZSz~;eG~1NUOA*1VVV65ou)-xsfRIUpzDV)Y5RA'
        b'G9jQPgCwLCp)v-(jDb-1Ts)I_3L+ZN+y^wL4bprj`O`Q;At$1GS3;1H=MoO^^6GvFN5P+b_oSYU53bwTK4t1>%6L}~`3(42yr64y'
        b'E0e<TTG3n?3(_~FKwikrmf?v6SIC+01*0qEeken6{h{kw!`JV}b2DTR2ed>XgbO`W$nTTogfbiz*c2du<7C?S5^#uE$U<BS>`IPv'
        b'T0ZuGvsZJ-_6Ad*EgPh3GA>l_E}BlM_Y+n-Tl6koU2Fa!>XLY0XTY&mC`f8C+D&+W!`ONl{Mv<}%JCTsDYEL;JCAij@`R%uj=ec3'
        b'eHQ~+9n5^w<79d{PM#p5rf+2!eu)}7gx+AP!f+|+V`cSYFc;W4DY$&J3}T@^y)bye<QArnmZ1s#q3fs-*YXk9k)iAK+hjN+%qa|B'
        b'FbfOQBV>3U5WJR-xDFq2{W1e}krF2qNZW5p#~fn?g?dpT0%gb{s$1uRyN@Fv9V8%|*Jh-^#7CY(>O1@O+xl(4!0dooj;XMppT3~<'
        b'O^lo%5fwwn<7JsU(!saG^o&-p@sJW9f(U?LUPQr!QZX~9mdTXumU$O5`ZxxfP3CM%aC?}4I!JV4JTP~{b11HaftgVpK?Y}vrICfD'
        b'Od%rr@r<jq5at6$0%SnM1;xy-iOgbVA7Qk4%u+#q^IfycnEZs>ik}`!kETUz@l&%z$|&M6c|w4fd2K(&eHxzwJ^CS&{zGQFlJviX'
        b'xS9Cc(Sc_F2I}5{|2C7xe6;V^%+X&ne7)JY-aZX;^utlMS4P40_88LGjKKE!<>Q28H2Y-+FKj_g$2c^*6B^Rv6*5~cUo)CH+Bb?0'
        b'v+4O?QOwbNW|m}uly5tm39Y8_FK3UB;@7mMN*x-sPr@91W7KjFVbk&T!kDA`Mh(?Vy{umEP`xo|_EXS(-oAg1I=X8Vt+B=NmA@W!'
        b'^yT5o&HTOdqmH(Zvc(KHWO{|Qy*AhqUMS&L`92=iVP)vawwH$b!0&9o9^$HNuz^<MHJR-RzUh_B(UtrdZMFRGhnS-eF}471A+!eh'
        b'IDh}A%+a4Rwr@t<=k;vg1I*C}7~9`R+<%zAU&$P;WNe>}xWAmge?N2de#Z7!eBVhl%B%<2y7ySy1N^i5n4|YG8zozLPSp@iGFv%+'
        b'zl1qj!r1;aqAgxO_7yQlix}G<N8F#!-#0Ty&5Z32Bks@P@8825y@#<K#P|7C<9nD86__X17Pjs+*0zs-3LLW;@zaX1D4ye(eR~Jl'
        b'>StggFol^tl{r!+Tb;Lh<$<twM+dpi*X$S-;&Y3zGoG-u57s;OD&p3U;+JWsih>&&Cgq@wB<C2Vbum-J2j6MtAkIDt=G*CsOtzZ6'
        b'Gjvv!ZS5#4|8j<Z2R^F)7o)&i(vj7zq}nsMw}VqL{JZd@%SR>Wup1fcu63Qiv&Akxkh80mq&TFUC*4YSzbLXT9d+!V!g_{*1jf37'
        b'+0!HsN7lMhYYkifz$j}?P901IBn;C=)b%pm2iSu-afFa1B;70mSAqW${G=~On3QwG&ir5Y?mjMx>(B%K?Ci2EyMyivB5$^{tKfpz'
        b'E{h4f*4*wALO_#VG?l1Ld%*-lY}#7mO_P)~J4*tCVvCSlSz_8<5)z=HLCgzkxLq)zY8E4C5|gVfNhLAHB*a)XM40EC*<E~TdS9OB'
        b'`SbVvh`Td$=FFKhXU?26Z|iU8JKQyiO!xv_Ew|hwxNA9U)g@28t)ZEg8akzWXSa{17cRGz%&gtLkaR&AMk`+j6F!|uo0RP)EmM*?'
        b'@lTc$?x!r7DIdI=6^TXhfq$7<yC*JuiLS=RFoFD;&(>v`|1vYuZ82mC$7hn`Ozm8*S<yhRe0?Z4SxBVjO*2V{%v1Z=VzJdfRoiJY'
        b'TW99Xn@Q#(b(vK$U-`X39rH|*KIhQP22o-2=}FGiDM;t>-p*&+zq9SYOd)w@UdJqR%H>%!spf&1@@sv~KfGdWjQLM=NUtZ&Y-TW)'
        b'$=N;AyFWP`X+tybqo+pAFVB=a$+R90Upl7Sved|M#x7PkHG>qNTeZgz>J5B)43oH2F{)+MUrHG!cFZi_%A;Z`w9G<Pqzuq&C?{rI'
        b'zTYQ&{cCJOy5fGHF1BJ)ik2DQOp?=9mi#AQJFQs6cn1z!tlWE#&uq+MMn^pRkA2=alS`d{gM!mdgbwZvrM|RqMtw0!&sZ{3r>&tU'
        b'BloXLedVoN7%nxqH@JIMZ;Ed3?v&bOrLU+?+uTmC%F4?c%VxY;Orj%ZghXF8v&R~Ldg$|C&g7EcUZUXQCid>}g_2*&j^W}8Nn@ya'
        b')mt5;A$`W#TeMqC`T&gwq|%R=MytxFZQXAhyMdt>P2XD0(06JX7~iVsJGCljlJ)hjWyY>&>E+W%o>WXpJ$?<%u7%<Cr290NkY}9j'
        b'Wtr?&(oal^7XmcjIHNzm+U43rbCiVhnl*NFoW-K3{q2n2*(B#KN%c#M=h7<(J?RP(Vft56;zMMvdz8hd%-qO3)7(tYTt%xzQSqge'
        b'*urpP-E~}LaZKH;%l9$$n%a$R7o^bX^EYv#a!4hvqW4o@zW-sAWrXW#)j<|PSMdW$u+u^M{bQ+%%}~aWuWi|MMB9Q$y|LixZ8<h2'
        b'ReU8y?wd-F<V)Kp(zW@*(bY)%=lSx3ugRC2e;ZHMpR8irCCTeoAJ1yHe4@5$PsCWgLn>0}Ncy*G<$K5kX27CoG#g0p;B&lh`2ly^'
        b'm(o^k^YZ=f=MLTzSDgIY`xF+le(}1pjX}=Dt=n*Y^}|Z1lhf1~nX30W&HSbtIb)`i-o)8z)<65(<evF7B5%3Mw|wlJB)XfIlP!`-'
        b'kAv+NuUT)^(u0R}<7Dh7>hN7Em(xPpdvEgOs6Z0f#kP$}p?BLYB+1$#m36HgZn|DhY$YqlBpzfOOIr`x#uAw><=|H&-v#xI>3i*j'
        b'kr{!*Ga5Cj#MMlzm8p2)bYv$Z({f&)VLmX!t5iKFwkz9uPA}9RpJ?@KgmdxoHV&nXjY;&a$8(vAU8hU6QtMi#!x-HsUzxG<l^I_7'
        b'PCakFD*c($jeZ5E@z+(8p=deZMHgJ}Y}d54pN@>{V#odz-me2Jm&|EO>Z(1SO+R5vkEv~S)uj)pOXtP32KYWjXTVZkWG^pnd-0_C'
        b'sTr3#y^2)3Iq#LC9{*@Im$J7jMi`>W92i#g>>KS;x4m}q`1)2lt!G%F@AL@UXUHp2pJHyBF=xEwHJYDg&+zH{PA=4{Nr|%r*upQR'
        b'a5}eM&M)&joRt+e(-9rf{X}?}4o1r8LsxwN#TDN-UH+c)%Na#%)mOHs`0$*gj~X^V)x22e^DQndj_J)ht{c8@M*pT6flV`dTFt`0'
        b'(=fiQcH_NYk-efZ>+Djo+ovBF4RmNd8QS*a8S<Heb`6)1KI4NfrLdmPQhyiO)LY`^q;skovNB}ZMXbZP<@;4%m9+7~kK~0{8#X`c'
        b'Xx8OAn=hG~i;l+)|6oS{9Ww$e$+Fi7r8J1Mh%=G={JtFNE)wbeG}10r#TR5tamvDrk^R#_Rw{pALYL|RWu-~DnFbecton!?in*9B'
        b')#_aDohso*I=0<-drI!ubszRTFVTB4m(X$Jzcq-n*ZcfFLyJgOtg?vwx4Nk6@AP9;mrA&9Mz|soZl?<;d6)i$6lpg6<Fc)hWxo?$'
        b'_FTH`dC_HGpZ=}rvgdrwve#PE$p0%U)8wVEsGLI<KP$TUyy)UT4lkb64bJ7OmUBuj<yIxXw7O(*wQUjaG?ebkwzHZ_gFjc#EwbI!'
        b'bc4Fmc>I}u^^6{WwxE-1qj?<)S1!NGaAv(FKn|L#467CE5>xvp<4F+u9!mucRhG;DP@8ygQZ#tW$<`}2Cl*+WREbYpM6<(KS;WPX'
        b'f|~bRcCePQs;a))vX;(xil)(#(50rY9kn<bQ*)h-!WbQCRqR-iInSXeW;r(V#wBMnZ!>=oU%5Q9+Ns`g-Rec8lDdhETxotUUR+)r'
        b'llj<cjdi($HNP95IhV|kJNTy5|5p5xEnJH5E{*PCZQ`0afj`GreI>k3hlN+;t=7_fU0^8wL2JkSz-#fDvF+N-ys`fp>tmNa+r}!|'
        b'XQ$~%rdqPjc3XJ*W&PQOvBJyo?T*yW4hLz%3VUfpp><uc!f}p#TRWiVH237xxhvgV$}^=3PD`)b+nSsF59&)VsOoPcHO4{7YUUCj'
        b'W_20-I{L&5TlTXUo3)8wr!W2BT<I>8$I83rR`dL(`i&bLO*Y%6(%U{8ekQ*EnfSmHB(q-<o}|mHG^kHV{l6n4(ppJRs5M@0wIpWE'
        b'+%nL`Red#3t`-{UI5B5`d8MZGElsf|&=fDa@3|{eRhQ85{hz4Boc2{@HCA<TLLCj6_@O%Bp_%ijJRj?RIG*mPkG4Bn4=P$Km9zjp'
        b'BG*!b33L$$%7q8zkcIopJx}RFYdpEUv+xEjIaCP$E=PDDL$+_*KB>|yx{GpB#bpJ>Bx`O}556otU?}{nL`v#!Xs!*OmL4$Q8vB#j'
        b'!aZc?bZz2EDRC$gt7*v<YG{c13bIQ-Dt}u<cIE$+5?_A1D>nTlY48p*$HOcsl7nZ-H%lO9a9sXm3roZGVIP^u?pU^8se3NisSoWr'
        b'X3FR@rD@)Fs1tvvraNTDPz9H@?!*_O&aup@5tFRO@n%EmZ84kc{PcGe=w`PjWh-sr5>S~G9+7s{h(>F&IX~XkY2bZ&e+M1kTA6&{'
        b'$M5`-V+%i!y5di0YCe>>6!M+>#`#+m+>Fig{@X|bUW^;{sH%Q-*lHO4OwWHx=lv*-{C6s@s)zqnPd0()*K}kZ9VsT8t@2_-+6y2f'
        b'I+AO~!s|(&17H&?)Yh2%*EE%^@J+f2s=gw5te5vCW8l1QywTu)N-rj6`5ZUN^~XAsgGAyG%^!1ouHK(Zqjb_*#VY39#D&)|Qxv%H'
        b'F|<qdO1>~fw*qZ-S^S<X8q}dN|JN0BYv|mXoVTNMYid4|7~yj|m-=j^?j^fL(vw<SbG56z+VA5pIr+M#GpD#MU8=ENiXpB11a~Z*'
        b'WB4;Ja@Q+qoqfX9w#1X2`HWm<zK~i2Y^3d$-lK@LBLa-QTuo{|yPt6?(z_HlXzLSPi|=&5$8obsYKm0F%WoyM38#5d!*8#yRMaNN'
        b'<~^gbs%jhm)qRYkIjlM};2tKST{i`vWL?{<8(f=0=iDQlYi00Ow&dn&SIMTtHl}%bt&fephc*A1yL&FZ>uC5O*ME=;yw3IbR|zl3'
        b'bpfle7!{2HCTktprSI-w&Hu@9>Sl${&Bbkv<7=z8C;d`%=e6J8tMcj;mQ;nO&Ai#7J8K#E#`w2)t?%U1&CgnH_XG>d4m5odcOq_('
        b'KERP`<r@kz1&(c)U(GjcN<9&}XIu<=wpZ6bnELAv6H`CYaPgv0`}|v6{HgLD9W$vIjUihub)EV>(r|m%I{&E;Jx7A%Ah<AYSwT&o'
        b'6mBPQ?elvL!%uSkPjWqhn1GK9?`wy>2D6XbY-wgiBfV?N>(1-thJVZTH<4iK!oN!lsj^#g=>}KI{YCkyXVM%|x%{qeRcA9^({e^;'
        b'mW%9;mH~+`&^O1LYdKEIXX^7>H9AX`=&|srmRItBS=Ugv%TsOMTr<RWsW@Go*=G=bMUx<!d+1L%@~uUrQQvIft-%t@jafclEWa{H'
        b's@AO^%u>>_D8^>_erfescMZkybIo0($Yf>ENZwHhKcUg|uyQ2%%rS*%KAe7ImRLt)Xf~)nljJ(0OWF3BRCO`qHBw#E6pI0!$RyBD'
        b'f4g4zp_~*o$9A@NsKwYdWNx|KZClN8n!dPJ|Izz58}`S|-=R57s*Ekxq&efM;ufE|gd4mhkz;Pdoy_4onX-?S!uPo4-{ao<9_P8='
        b'c6v;>mAgmrp~Jm%AvdJxiV44nHGNWQb{|`Qs=QtC?Cj&hO{6Gp-puJdFE@32Ha(j-FENQ7c60r1QqUd>xH%!2rmagYq;Ve3)H=p='
        b'C`b)hIg8VlJ=9dYJ$~59^<PiI{!)F8?0g&jQ+L0t8@`U~&mrTg$l9l_yJyzn4@`QV_Wvu%!8!H;75TPtEwkZH#`Ce#8Z$qM8_weT'
        b'v&am;8+>14th02M%vs0nW`@g**$|zz;RDk>q^Z2ZFU^1PqhX%w{{{*F^x#`^JC0)mY23~^+z>0o(d5RipF#F<cFcE@`ws0a|NdmE'
        b'Wl2(P<1ubedf91CH}<=e+~SIVBj3`=H|^Mu$hWp9PjV^g^xN2ulU!EY56QO*@@?tZ9dzmwC%H8h^jkXlw!ZBLbZW~<?xA%0jV@?&'
        b'#Tq)5d}|q7P3LGn$#tgFZ)4j}M*H&oCQ@+(KG*F$s~b`Zf6>WlRd*@t2P&R8nVL(|*fdJRrvLtA%~#=im%D}2wGL>6|I*TWvAK@r'
        b'tloT0nzhatc|K@VCyeT@cs}U3PB?MJ@EAQaK+gkAN%B6F^R_OO&uM9WMhfK@AM#7@Bo&}aI6~*4oeaO+$vE?XtFHQtRS4;p9_-aL'
        b'CyCbG3SFpA+eNx!-g36Wc&fDXE0-mxK11qBMa{?Zb}+xDv#?AkU#Oyy2?O+h^G|d;TFeKv87T?oSG5^gGt7H*8H+XMe(k!Ythsmk'
        b'p2YM^(zbazbC1sN3qIQuv+V^P*>XEy(D_^4q-puA-9)-i{oT5SnrH24B$=!yvwF_>sMpXvVB1_r3djM?7E2AOGU$b-J-f+>W4d6E'
        b'?d3TNvZq++k%8u=j>{7KI{9F8e2w7KamkHEOvO1#_?_0%8T1BJerr=C-$;vEV01hGL+5V~j?FwpI)V-1zDuJn(y5R1(SM`MX`rpR'
        b'cGkRA=YRS|xyR0FY!<z%(ZIj(qCb=GZsfU?hRxNUhD|r<LI;G$bRMs*TjV`0)%C^ZpJ{V`8a~drJ-SFs{5y0ZWcToFRppS(BnRng'
        b'4@c@Q`G_Z6N2iW{tQ`GB)&K9h`M;ZULfP{)bIU~fh7Wd}e(yfgW76%sPdDKIxo{s1`3XDx6CDX~hj#G16fGBAlJ`bNxL3!;i5gK8'
        b'a>yrj+BNf2xK@oSl+t=5BU(u}=}ArDWO&=IC3}>xmc~au%Ojs<@+MxRv$7&N?1f0h#E=F#ne!5@_i|S2!aciKIoNU<!}7?Sw?#hx'
        b'm43RH>Z~d&8)_v7<|%EY@OoKQ=u|r^ETtjHXA%9hSlH71sS2kee;$*s(j<OgL1y_}-Z$0@F1gs9phK>Ym9AS=t^T`&C33+|akVxH'
        b'i|JR=NTTcGw(I29%P0-KJWEF!!j&<liCmhFGy$%s0Xt$s?~(xT(g1Rwgkky@=+>?$&2)u*spj?5C)9oFB}>~@eee_Q4()sCy5V%)'
        b'&UBLPZwa&HWp-A~88av7xH<i1U0*y|S94^Y_4LybBbvJR8$6-lXvnZR)Wvdhf*}K^6OzMIxf@oQxYX{~3?*`iHKFd1fy`^TG7j=7'
        b'Y31&x&@JZyTl1!rnP|SCwHIp0#Piy4Aayv(N>lfsp-hf$eTdezv_2TuhPTo0Xju1$+EuF1Ya~y1gjbus+CH>an9$0FzE9D`rXQC`'
        b'AM9QFuA8QC7*>5=;$A1&c8U&{o|fCy^^t5N$AD%PDQrtsVqB(nb=L8Vt@kjken$9!26)yuhs^gk`D>$%OI53wt#QrP(mJWbI!O2C'
        b'9#UVvt!;CEn3$q??=9`{TiTsN+JQi(@QNJ2f~hyAza^2hYzVJ^;SnkPjD>j*Sufg0t)vr#omx`Jdr4NTn_e&BRr<A0k^Y7hI!McM'
        b'cuGvoMM+MtmqeaaahRSXS{;sDZeY^7VM5}J(R+h?waa_8OY^s~obl!t>B)Qdi`w#+v`dS)SvS9=;9^QFeC+!(%{^Low>HZ<{{@xx'
        b'zQmFERn^a2#};146y0h5qqg$C!v%({dG&?nPAxyr^S+g-e=8&L!JqrJ85tTOlP>({PiRM!nntCnOOsvC>58868Ai&PkIcf#xbX9='
        b'=8>iG&4!P(jZ0@VDl;BTS)En9W~=s<-DNBJ(zdUxO3PBtnwwc<QO>KkTl~t*N{ceRextRLyOA`cGb__f9GmyJk~2A*$%_44(ANBo'
        b'tZTWbUB&j^R#G}b{-yqS^d-aky}`YPwa+Ery<kQ_(E9(-)BUF$|1;+9mSBl*q_K#z8r2`j=Zk7S3FlR_QMi{h(`tP)gr8_VxgO!)'
        b'wRycXn|NLotwY1-v`Ne4igViA?xoia#JJK2r0BU%x+x0`B_*3&H+pPh@aCpecZJsOSI}<KU5xooZD^KxEuG6rPe!#X7dO)$Ox&{E'
        b'nsec_v`t9D5478E*G4-MnQ<=HCN9Z*yS8*5V=krR>mtv*(o@S{(1&W%FGxF=YlrANYtAv8W`1*w@G8yo(Pl$SQ*&I%nJTI$q{z9}'
        b'ig89L)Y8izPmvTp+eB)O-f%j0lXR#f$8_Oew4}O`dv}bmMBC_(CExAjdk#&3Pb1j0T(bPF;<M;^eIb|h^=)-c(e&91R9y7@VtYQv'
        b'd9zaJS=#CI&CzFfGxC$quh3=~RT&nAJTAi<zpm#TmtS~EVmSLCDatEqBIouR2fSP=r)~H{wco$#%)5=xKhn}j2A<TONogI}K*n)r'
        b'w(6dJMeiLbBTa<v1^i1^wjq<>%6jOw<dW#2g2ofwhS4-chp+wI%4R>vv9->E?BeYXRy~hNtJ|JruXUQ&_0oHs)8cBKYVOPJN#C3^'
        b'o|e2l>H4(H?ag0sUfMKD>)4)@vEA__@Ba7B7yXqp)|{6b{f})=I!ESSLgv$Ff3&^#h<E?n=ZpHed{PN9js8csH^0c8B`p^6UEH4Z'
        b'Vy$yVqrYZ*QgWlec6-vX!7&oWueT?~H2Qy|9+NnG&3h7ODIATo!``8fRFjS+W0Y@=@|?STeUG!&f01EI;Y{{?#+$F;l=P-3@|})Q'
        b'c=Jgvc*%f<OtR;*gI~$VpS1jN-fWE?H+9VoqCVB4zI1gSk|V2<{AoOvV0gPGc?;x>jZ7mAE-z^+(5chmziyn>C?-YY5KXCKohiJ0'
        b'>qhau>GAA&YmBHQ6P44~J;;0}3#;;KRF~tU;W$xwnC=0Y$(MuEX;sZ0i(Y4;ElIwv`f?t%vP`2=!F0}Ld~+K%2e~xT=XizQC%?TV'
        b'#zMNXH!@e`XQXW#EkDgY^eTqMuShIrM&n2czoPD-`8Pl5Tg_sIGv<78%DUu?<|2-5JTUQ6adNxH+TQt;d=+4jWinQud}*~N<DQs|'
        b'2mg!AZ7s@J@y(Z3a2btp+^#$$$FYN7O4eqQcY_z`r;#BCAZxRgB|RH@-Du#*c?YStvLkum9XNm9N`_;id6Lf=z5At?9M{xs|I@x;'
        b'wO>8H>TG1)ugL?ig*k7vc$M_wep*IZRjtp|Z1g_GkYcm$qQ+`zH<2~%m}{NOC6PX`qbdBeG<06e)67+MLNxAwNTc!Vr+XWJ<Z0&b'
        b'uQTez&8@B4{dp~Fk8Kl;|Az6J$UcAV`b{q@@_FrgO%KzbWsQ{QYr|d}S2N2cWyHlb8%guu=V|aZMXmugv%N}A^K$as{l;S^&UpB_'
        b';0+qTy{Sui*hjuK*qefTgSHlZx3{Tb`aKA|cW$c4rEqbi5uTOF^N%mHgwvqe+`4&Jv$j{aOzigAeA;#GpG4EqPTKXgEi;>qTeYD&'
        b'(ZU%$jnxgFP2qw|ribXd<rzs!mb8C4<6!h!o!64mEP5@oJaxgv4zDG#A@}{-T`9K5+~gSIwIp-K7LoqAr6u6d@VPuW5Jd7rWXZn8'
        b'Uf#FF*2V#A{i=3NZBtA~93B6pW~-J|;a{^YnGNA>{?F>(>GBuZ9u`Z29NrljwpkPzChc=KX3RBY<ff2uoYMAwiH&FE<3_G+Z3#oZ'
        b'lLH4gSN)~LeGwUPUjEGx)=Kt;2S~LLsV(cm*BIN4&FtuA!(!39KY^afsFTm-agN%vv$>?>S!BqYxya*5$ViIKu&UOPHgHj$d|;^w'
        b'_d#eqHeC;1Q{L_%IdyHh5tYrR`eVMN`j6`3M2k+WBb%7<v4vkrb;jtiSTxpaoJpdQBvw;r5?QA)q;awiOKPsuG98b--70ED>vYHO'
        b's{Pk8kPxi{>{iF+d8|d(=Cx>Qo=ehWCFx22r|J1$gdr(q>x^~N>5C4Ns^N7@+OhjZrH`e>`G1=SJip01K!3f7OD0G3M*0ksW#F%*'
        b'0^eNSVCDUhXNb!gum9nyi9AP<tznUEk$c={7|k_sj>SDpvWsaCR9*Cow)P*>fr5Zv)VqrKR!c(hkBb$(mLhG>>wMAoxm$-6w!NNF'
        b'6;q$ZDV_Gn{pvUGx_7PrS2th3PFLW1!Oi96&0Fhw-0ku&8ub~*I}I(3Op1%C4eY<C>b$4M78Lb#xQ#4>ue;}FQ%u=ip0c~#cc=37'
        b'$F96$C0S~nqFF0inpb=G^K_Zry&iJh2tA}L=u;1VC{<0+1#{YH-9^@GNJZByk<8j_v1+?>4fcI5Ykqco_byN5Dzf}um4~;ILYC)D'
        b'v(0nU8_GpdW3w$9&owYgm&dlvW=n9YqWi9~KFMCG`1)e?zuYeWe4h;;UZeHjwe_TTppuIVdFPDNO9%N(s-?E^++ZY5@4%*iI<3CZ'
        b'>mS|hB?X|iQE@rMbUoJSA8lzQ2V8BfPtQ5IBGMf7uD$LCjl5iXQKE<;jp2*(zMAhpwltq~nc|pL^C}Z+Vi@l%^-I=x?|;N*Xkxo!'
        b'MwN`;!moI(Qn&7{>!*rTrJE+hX(#hN%+fh)w2VCKAia@Ro>?!?tnG{0@GO7j{AxP?yvY0^yH%Cg6SI|FsA*(La=Mg*N+z}QWuLb6'
        b'#i=^_n{b6QnI0`u`ovV|9-nGq9DSKmYIBc<IT6>T9MCd<ej=g%37wBq+KU-_$K46tJ1Tnbe`@E}xYFa3h3CR;eQr+p%E8!0X}V4z'
        b'N9Q{}+Mc9NZQ_(Q3T8o*SE=AkoUS#%+`n19XTW|7le(8nv2_M@yAzXQNP{~2$Q>utEVGp>WSHz@PwF=Jv@T-?;+WLkd1>0W)4o-@'
        b'WJ>;l>w!4M`=O^2|2SEj{dVf91wPL!!4IEPaH;oiQKyQV2U>4o20xej;uh-U{V7dTXBJs5My%Yg>S9+bRvT95oKW=9yHTtLu9ChC'
        b'C}v${j8&0&xewvW2$Dio87Wj>*LE?}+qxUf6E@ofZ(rZ-p0Ft=MqLvw<@)ZNiL%=!cz(T&nXr{j*fvb?G3#Ax*V}HK;5V&jZ0q^L'
        b'^=0!Xc;)&Ho7M--6WxXhM!&u+Z(^LC7^SZgcqsZ#2GULpu=Q)3z4YB7anb$GOUKcZYF1;WQZDo5%n<8T6dUL@se5(e9ZS9-UHZHv'
        b'wlIsaa>o=GjShDF_Xg24(c$kj6yHJ5taINu{C*QX;ArptBKWDnX3>v^uOMmrRA&~FFYjj=?av1-e!uNgJsn(c%<81!vq(@HE^ESP'
        b'y+yvPRk}hYUzAJYOg0~lqcL)oE~)BoHlIE`B6I^O!)nIv_b;ZGv6`*jw(s{mAMD<(x9z3#?6%5#7&-o#qL;GdK@vrHd78wbujGq?'
        b'#_k4r&K`Y(JZDd(vG9~6_czJ<zmg@cS@IQG{g;z6t=j!YksaS*5R(r2tV>B^cduy?kCOv~za^50-B&D|M%@#Mkz)(xc0{;69k)zu'
        b'+<&P#uGA?Pg2rS;izPhW)_AtzH#zij&2M6CmXR!L^nBtq$K&&MEhloTBYgl)bKZMCO+(ub^j@d}!{UOi%A1=b^+vnK)*NhUBwcmd'
        b'l_v8q@-StRBz=_@{$#!zl%#C>ospz@^iv^G^wD{iOrByG1!E)Qt>llV(;s0-G#bWn(}C~W$Y0H~F-u-2e?ju6pU=o#WIRv)^yF`K'
        b'7Q_76PUaxr@30^E?)S;xD)LuC{<7U%S$i2<rg3p)mE`Y~jVU|DGi95|au~X-zmgR23`v<>P3ol!WLU#6qMY^%(xc&Zc!d0skkV%f'
        b'3|H15kNZq|JUs2Y<nImn<1=}^zL2Cp(a%ftLr=n!)nr^G>@DOk?H75j1hd1nq&?5|=*~QsqbJX`iu{ds=DA+&%5$~fpXWOB9Qo5a'
        b'T&h3jxfVTi;Jb{TVGh5a=PG+Q&t?7Pf$x@)Y2sh=T(6LE^T_bMWIf5cFs@xOOP0P6v!t7RK0yAqk-v*1?u+~LTu%>^c}e~xk-yjG'
        b'hu=#>TDi(1?dv-S5){rHr`c(+mosDYr*72-I;1T-S7`@kDbnXp{X`r1LRv-!%L;fhW-NW`huT1^q~FPVvzQVxE=kcgZ^~c5=Ox63'
        b'qj4%6Ik&{wNas))WAl99<0&gLySg`RSH-wo-*<JF6&dV)kITO)kB+#@<u7YiGz2&0#l<u<+|>{)%l98yy38_gW^{?cW$_-&b&I5D'
        b'KiJYtnk!3lN9zoW?IcF?8`9`f11ZRz1z95f<#RFrdG*p<?rgqapVzBNwX}%3g3?8i`>z=8TPJ34Gr8kjYODVz!tW(|LhxU%9MwWc'
        b'xtB}JS4i}#wW@rDRFX?~WT(pgJ&CvdJNddw<;hi)t<;x<uVt&`QRPKs>LxPQpKFLta2H6+ZwklL+RBi4gnY?=c_xQu`FExKKhg<T'
        b'To!L8Rf)@|4_8UP@R-l9m)^Tx8u#f(uN*s^EA{6}he=fx87tT%c|wU#@4qtO713?Wq(OS)O7`mg;R=l2G0-08>eSmh<$DF<<muyk'
        b'^`n=k_r@LGs}EigUel)>@6?Zm=Ljz(?U5@|!p-1r<?f&vS}5o7t$oV0N4Ob7@pP11&f{2Vxh9-9Wc`<`rRhvlNgtkNYi=WX$|*@f'
        b'>*?2bshsYysmZ(+wq`NobaN>}4vixG{|#C$E5oF-@0)7%D^~a!TU%3)|1M#HB;W77^TJf%?^B#fuuAgHJ>5Uxg$(+&^VtsJ7mF2~'
        b'vP-dNrC^cclmF*telqjK%%PdIJd_KG@~9cyH&4tMn$b6tj9QZ`803*L-1Xe-Phw8Q45|BKX;>2-J*hpR9#Vf29`$8Fm_bK&Y!l+>'
        b'=f%MOZ6{*3#*Dw+6s&Ek-Kx#|PT$K-Dp9Ci{9>0vP|5LXg^4M8AB2f<xHC*_%|0m*oZ{;H6m6eQ?$8eZ=T!fnrUHMO>hXUrT%-Zd'
        b'Dwt2S+{4_xeM*{&kLWn=r;|!jtnUbq8l$5EFHUjFRob5ZB$BDla_91~k0vWsKhzE+k}OW>QjMLO^tbVODM~u6X!-ehdPh0Q*Ng=E'
        b'R`c`n?F)gnDOyvIEkdgbw^PwJHc4uUz*L_?t|i(|PWqpgqaf2nx2Iv#-IXyOvgbFH^(wk;n||@*nC|Yox^42V?IXLeyJ>3lDFfM!'
        b'7k83fc&RwrX;}W7sZNnQm!`bGT3vgcGPR&Z4Af7h?OUboQ;<cFs;S~Hll58>zv8)~oSLccw7WX*>`*Qca~_>?iFej1$9g2UcdA3x'
        b'u1xQda)hZ4WsYZxyY;M+8Hy(xQr^q`G(&P8nBr!T(WIo_8y@`x9bLQe2kuQ%Rj1^l>51(7IX|D`=q_8VbpLGXswwV!uNl7Qn&EYk'
        b';c7Zur`mp&Eqsh|ubo=%oQjryIUv6zhF=zAE8uhPn2NoNRd1ok)FS2b)l($}`tYK&r<Sh@&m`P76`fD6NdCN$t?@GM6;rP8SdBb3'
        b'ze~D$`1wc3uzT6m^eENx;who{>bRB{Mu)?5Ex+-qVO3SzRl%P<%c_6MxO2&(dAIV)s25IEeK1{lE}G)B^60Y27-1>R?QP$la(`Q1'
        b'r#RtT(bUJu5xW;$xi&?b9P5-VoD*{VaqjeJy29bFT-7-DH?N5-ZR+aj$=6Izyk@#-dipkLGXMF%%44sbCGOsHR}H$)PezAxR8w!0'
        b'&Afn-Z+fZP<O(+hmEoJ7E=@+8hT-9J)5AHROuFBjlxK2<8<WbM4=3GcuO4OoY?4#T*GJ5sOjdmnxl$4?EN@JbBk|yU65}2wso}5K'
        b'^sUU*!{o@D%NJHj?hsA(U;}CO$V=fKCCjNf66q@j-k;>+hO|BYnESWP61DS_5<|_TJKwS+Q+_Ze)wisZ-c@%=A}!a#NdGhN)@1s7'
        b'V^_Qz^vEQwTt_A&SA^-f@I~=$hbEt~#t4V#6!|hy;sa9p`IBwBDd8X;S96iJRl7e{cK4~geuc%)bX%+W9^Slfl62Xs#<mU6obkpn'
        b'9?zykhZGJ-JJsEF)m^Nomv4J)j4<z+w6IM5Kw$S|#hJ<ar9uyloYQe@#!{ztXy1Eba`=VG0sk*|zA!1gB&YR7`hWdIMb=b(=X=jj'
        b'4nIdGdkZf}^d`zb(rJk)iZ<(1;vVL`j>+LRGPQ2-GpX&fAgR2cy}X_R^A9#$Anm<uhRLP3Iu{o&UQBO#pj*?SwTbc_eAD^X%%+Jp'
        b'G03HovHRob>vOgQswO<0wqU2e-*+T@tS&Iz{K|~sjJNvdzZIDOR*%0b-L823DSGLuBlxO*SoIby7b*6A35Ut9Q^1dgmz%QKNe|`n'
        b'a^oV)jl23fUd6|ftNuC?e{iM2|FoxM70)HzOpcctE4ydqnpKCJ41(sZmPXG?y?geXbmKY6LR_Mr1f=&jJL!G8cACaw&Pa=GuG|N#'
        b'UzCwBXU@3DzMe}1(EAESleyvu>CDnJm<lgS*G&61nZ~Q5_hVl@aoeXO`T|9RsCR`|!4x@<%+Y>aYi2S%9qR~$+gA2_k|TW_lCP)a'
        b'Hjm8_<dSF@k)DLQDi6~3kLMbiSyxfeRuJS&^d_&|KuHO`+E)};|5#*KBEhRJ+8j2r1JS}y+R|KokDp$ufA9!>M^MQop=%_=q!Hd2'
        b'$(YLu!8hxSPF6H->mM=y=bI%Zs?skE^5w&9xfhq=-t%UIToYI-Gs0sIuQa%>9^>wL^V%_g{D(1rxOPnb^K}2pq)W3#VvG#r|53U!'
        b';MMb)<jO!EVUkDa<+`k71ux%3u8&0iG!qRKO+f9)HDhS?b4?iUo7aw6dGyLL_R8#VztU2f9PZ`j{9-zPjNvh(D-E`*$K?F%O|JOb'
        b'aX)^ODfowg>)yO_Osh4mYL~53U(y-AFE>pN_05Jzg1#xA7)Z1E^d+mqE1wpLru5C|Exyr+S6nlOW?d$|ylqwR{JBUi9v%*7Eysq}'
        b'vT&aiK9_A}OIzbgO6FylzMWXjWXxTfk-L8EW11IsYlhkOrfa2w&()XQ7EVcq%k3s#@+;?u^NWVDzPaJ*FmeFv;CU$$!2G8FYXW4}'
        b'd>TFu&>+cg9{!pjS%YIzhUs6QtInAF({;J^a#*9;M2d4l!&SkJa`4&eccn;}SQ^ImHDMCe!_hF(Q4*%)Yr@P@?~jJLK*MbKnlOp#'
        b'KS`1N+xEfH&|3KnPImYVXl1f`GFpd_>4Acg<L}Gcbb&u|?q`8Km=PVMKfP|e;?`|rbb@j4qI5Z)L&Kr7(HZs88KX1kBQs1)Z`U*S'
        b'@IuY=M)<3iYvR1o5vFUF{7o)DI_aB*S1kLuB@&n6a$J{Z4d1)fOv2f0s^hKlRhbO)kzrRZy)WG62-k@jw8E388O?1+`KzWGBj<qW'
        b'jlH3JqL~>jtl{`+Izo-%{a1b{HoOneGenX5>Q5;98;+LFWBPw{G|+JL{nsxFzd3sOzQ&L#r~asA;8N9K{R+`o)~gTcNS%6V%L-4('
        b'c0v^ls^oLbRwJLG&q^oZ<a-0@eQchia$TSQ>cy(pZ6yia1^OM=1*(qr_*KF$X#AWqa^aK=Hokgpd#|DY{-c5WkESgXenzLOFG$S5'
        b'zDwS0MdS069uGNk@eR%Te80lw<GV$@FD>8yh^Nuq7gPJfY}Z9sT8GOQWa3<&hHcp~X-|~+Y_7e*?jIOhR+1`c&5Hc=*`cGuWk>tV'
        b'ND4j+lpP)0%@k*6E;+EM>d@X>wj3WV(BC{qH~fR6{i{fTzmwf?pkj7WJ~xX=bun)S4j0gi9>w{4TIpq%{|KyF!_8~>4}RGlzBQX4'
        b'JD@2}Qime>$u}fyW$WJw6d&c52{#;#++?3=$+Y|OTL%&bM&f+hY~B4^RF=xw%fw}!wL3l~&6Y?zEcfVU%jM@$)4!7X9Y=S5>nNYk'
        b'2lsjQys%I^b~<{WN@7!n_xVfqeM<VSL1s9wmmT~q)8ps7{ztlZ-IwQJ)jZ?*%9YmXSv-9V)rot=Ajv9U&=*Xbo9AQIo0(u|kkQhY'
        b'0%t32qHS3RZJ4xHebJsmn={q)`cmmdWvY*^c5a|Kzadwj_{BGD4P`c`-u8tn?Ms_4xGdb15KYHd4aXntpFuKkFc5pR?J1_)Yv$tA'
        b'rzMZAjP$NNWYJ%Es)OAfhRvPwa_m{N6HO_{OjU1;PwHR(lWv$f+Rq&A3H+(>GwD?B{<)z)4o@EGpFGmzKQee)3OzS`=}7+s89G|{'
        b'q4d#`1K%20KYRX;tkI7Qr{Cw&ihe|sTu)nIn{A|>Q}?6LDVppZfrd_7bH2Yr-;p2tiEjAJk^VDBdIAp?z9o5I*KgTZ`zN;MyG+#~'
        b'@9UQiirs$+PCU8y*p~Lu6Z*GPbi?l->HixEJXig?wCulHPFx^mWb{b?U&yG8!a?a+(&57i4JY__lDOS;2B&WLog@8kk*U_f|CE|d'
        b'4Gjt1yZPOw<|J-G!|(K+zQzNW+LP<zx;y!f<n|;kxuJ#kC6REy)3@v()0}afQyw+isc-Z@@~qRs=;+&)xw!7#hR(h8x?9i4g4t(&'
        b'INWul|BoaiK2x_z4HK@kKQ!zO%0ahf>$*E_X-_mf5iC3_y<^RE)ZO6y@$BAwQU*v~919%Y%aiWG?)(-Dy|~vN5LeLW&{v42ssWEh'
        b'pOr1L@&jyjtkqO?ioOfZ6kNj7J(W||MC<3oBlEobE;d>f4SrSPX=eDzBmGYv>3Ql`fz3xM9%V+JzjWBAe>Zorv&h7ylip6TX@63k'
        b'k~7(s@Xn;$t6B9TM%0AbhqoQ+ZzNgu!@|#{Q%SL(#t;AINdHzc;zw$FPut<Y=<WVT4mX-7wQuj5ZJQ)}xJ}-}50gDymG*m=&t{W?'
        b'MGl8G^y=`YBmJ9bDXIAjnKSg%@Wvzk8)!MHc~|QGlc8mAaW2U_=e#{V`3q*>+-$S|c=r6JtkHiX6$6(*^W}v=)fdexyLZ_d_Ud=9'
        b'41LUe)5V+%jOW@e=G(rjcjkxshVMDje-BCA(!tjxrfQ#UhyJv0na`I*8XPUnb;<jas$Si4%yozU-RqX-k_7zQk^V9gdVS#@QVe20'
        b'V%6zP=*8hXj`Xh~V}CmMg2cE!B9+-Aqjdc~BsJL7bPYBt*I>V=HJB7!m0L77aqRQN7tYG-v3e1$hSK-+tXMGn_9k0CS&zs6FYB>v'
        b'$7x^HzHq9aT<oihb0k$AAOj?)8+y#!cO~1tB!$T)7p8`WZLR*~9zWl`+h*$wcDESz_-N0v(VjUwv}-v2NPj#nfrEm?IB7Y{t$Ou4'
        b'H;{&Q9@$6Yj`XX^#J|@(Bzf<d?a1enX=y7CkY+jA@tygd7Fw_R0=+95p5T2eB6Zpi+4^0f$LT#tZSP35+AKZ7xL)8(+W4_<Nq$0h'
        b'WZ%V8bE*b8UD>bn>z{f#!C-k+S!U6f2j7@~eGIAnx_j;$9aq)=b@<{)KTC?_9|B_|=|5mz&SM9^%XHq|oLIHrlc`@;%Zr|u9c=7J'
        b'bNk5gEBy~7^2CXYeaa25-YJCMpm(b(yJ9MaCAl~;p~2xZBmHMa=;r*GmamtGPmlDUBEvr=^$<h0BJVZNC)@C>E3Mrn2IUunZ_AEN'
        b'`~3!yZo{JMn=?omeSM_=^$}7=3+b=sg*t{0jP(C`gw|zmNySdzyzYNBY%ZYZ$8Xv=Z}#2WZH;%$zTKBK`ZL4&3bJiU&GvYp>VjC>'
        b'u-)eI>3yZ4kHXuw=%(>s*fwm^KX}u!UuTI`19fvq1EEv2CRH7!FB46&&Z#>2j)s1nBhK*zRrSvezcSL_M-pG7?v+TzE9xz;>*x2f'
        b'HFq$bPwdT{5Vw3ZZqav(!TI0N4L>!~{}c&2x3EjHCi8rP$II6xb3J6HTDxxecO(5zjL^ESO|s76=8@^$J^b!D?a5q{|9SoC&ensM'
        b'tSLS%X;5dT6eU-^>wj85UZD4M@~7u@B$Kv6;)>IvG4>Q&V__1XK0SVs?hxZ%^9k<43rQ|%Iy1*fW~xX0$z>!rPXsINMV3VM$B9Qj'
        b'?(Q>e-g}R{M`Y}IaqWWHcQ@vcJ>vGq7mVIYvXL`B@cr<M@a5YXHjql~`=N{UjcX$T>rIE(*~-@H*H);OZJwanmQ1p3Gs!`p#+qEU'
        b'pQrD?e8kgguI-u4lfzagA3aQ_?a0>p+iiR(*j;bv6zQXtk6Em<L#@NbBmKo>dwy29R?5s=?ey6jD`#78BK2;Xizy0_Oc)IrGH*J#'
        b'lI{s&pnauhGherIp|a+t@G}#dT4S7L;G)$iFMax6CvG5e|5oHa#`gS*hovq1o?W80+Os;JT{0uEj4bqCA?7fB=k?s_^EX|}w&~xD'
        b'DSe+A&L8Q|9|_zzLQg<sF=G{ye<`0nA$308dNASHT`}RCpX~e2*mm)xnKJeZsdcR?@u4YBRm`T}DfyoYb{L)Zj_{)&;d`{|7gv2%'
        b'@vF(`y|HY4O53){@HP8nub;8W&$pDGQu1}xr6T>2indEqdw!oXeUo&9c1LI1xFj0=?ZMWyiuAMLucD>HSi48jVF|x^!#0;b3&JU<'
        b'`vr}D1%0?b9C4D8Ea6OV&%TRYY{jQi7u$AT>QYvGOrq*+?=X&?Az%8G^lN*5+v9Zl-=l3Onjeahe#J;Y8t(C*OiyNxD@i>=n_TBe'
        b'+9K^z5;IN5DT)3+F4>;q+s33HYUwHrsnTDhEAddfaZP83u}eAjH?p)M3t5K_<IQvp$l^Yg2G4}s!f7E+NAK0YgH|nxjWIOBk4avP'
        b'l}S6_8@BD^D~hF6H@3Ye`B!?2?CG~i&BlgDgK~5woxx&q2<R~RlsjG!q(dd=T=Xr0o^31kf7A2WQ=Z4n9#0u<?97#a1}0oa>W_*y'
        b'rHbAPl~|D~)>X_I7gv(cm125c?-^(M;Fq*t;EY^Ht~XjN;oseOkFoR@a69M|U4s1$xrIL9xA*uNeSo*SZ?(I>CuF}NpL-h~^&33D'
        b'p2dp_f2*79&S@Oq!?zxs6nciqbpOXnf0xSMe`}wTdrs)0qlC`k%=gS4!}fB0=I3?8_Wng2+cTF&Y#C4pb{b?^?z;SsyA*BSiSTbk'
        b'wffI+uW-7~fH0FTw8wvedv4FpE~Vh3q1!4hmadP<nL1SNKD2n_FRo|Jj}I?ilz07g?#G9hDDCbuB!zbW1FrAQvb#Uw3urp+{xhyl'
        b'J|%a+ukYE%lGNt=&j>X%vXp|HGl$B*eQ5D@dDpYcy~8<=l7!kr32x7@rTjW`^>B_rzFcqdU*OFiOL?C8k>ULETuZsb{3{Z0k)?dG'
        b'#lK%~@vJC!ZXB4G?`Q1(KUcC{YT*}hcHDO7P|VUmpSmPBC|q}lj9F8Vcq6mS@{7iImby8%OJONs((jwN;+j6$lqW7k_T9*PXwF@@'
        b'>OC}LqZgv@u27D>8x2c}|6ilyNqHtkuHy46=X2fWb>+5N{7k7yK@O@FZ<878*Z0K;-y5EO*F;6}C9*L|nH;+meoSCGT>`_Y`c!G5'
        b'E=7KMtk6N%gmZY^thYa{F30Qty?41*Wcw6iQuz01#GmhU4s*smz1{iMuI^1|7I+pk9Up0Zp7AvN-QTWvuRKKh>x^h<XgEj8FMU%G'
        b'+3hR=%^<x8kt|C`m()X+^c#6eNzo;7tFBp4XtDL@^tNWL{9XjQuaR;k2y`y5|IgEb<sY`9>v%cL19Hs8Hrpny(pJ~xU`b$yi9UQo'
        b'y0nq|%LM*VqeVfol4NMDk8OMOV)Q;yfe~7V@_J_sGsFFg;edivCI3-zRHBi0DTHzwx6_cVw39g5G|^%5x|MzO#Wy7G$ot%dMtT16'
        b'!~I_z4t##N#~-LT9G!o8cz(P8*wqopX^YIiZQD@Eqn_H`Glowd?mu}rFiN86N)Jf`{xo`$Qz5u$B*g}9UjA}z5xc^zC`w3sY=v9t'
        b'G|LgGBHO(AKKV^uM-SI0lmF_p<iD$)y|XsPt~I%MRqUPVy4?D;sRiNRNLo-(Hg_P^QfBcwV{De-ElOL#oi59rWUj>gslmv306MS1'
        b'<stLVBJ&od%J1J_P;d+DjN#|WVXe|&<hcl2!{5FBN=qQ7))y}v8X`Sg`;j20v01CHJO-9C^5an}nNX*w;EKmd5hC@UGP=LeIQB>4'
        b'c<S&!#38QT_VUoqyf+$}^<C`C$r^GfY4p#kb<XVf9p33XJkrXfKPs;}x3K@Whj;$=aAEj40t=gzR>x`P?`FMzmdoemA1$EoBU;O)'
        b'bbHQmtS5^;$sOu2Z#kT0<y)#3#??Q_v6)Kq?+%fWq_x`_=un2w$(+i!*;J#Ra~alOop;Pmd_WV}erR2iTX^^|w^!7RXjI&OwSmbf'
        b'%6+NmmO#Uyb*nOj`^l#Lm`)={z%#bqrnLHOjctEZ&O<}CPx*G%s<obt+&?MYOM?EG1|=!I_i|9WL4*o2O<n}qHC`$FL=wslFOi3p'
        b'OZFF@lY}20=DtG*W6~To;}X3eBU~I;3qseB{CJ@2Mt8njk>Af3n~SuhXci^(DM&$@zBkWygr_yEpKhW{QnU;y6c4jjBd1$yF<C6%'
        b'*zhdBwtN;z@7jQRq4w?+Wrz*M%o!i>yL$W*-7y>GWyQX4o@Lbz#aKtkzBkhEA~Ot_^(VBQ+3m4w?&8<oY1IZF4_bR%HNiebV|k*t'
        b'Jb?shG$#(26BcS4c6#VB_gIM51LlOXg5c7Xn{#hft4~TaJwKu8(OO7)$`iOa&REje)Ic_$Hk3)zd<#cX(nTW`ekP|y{k}QDswIiA'
        b'whqPgsmO9pXj{$tHS^wmXoKZW*T$g#>EKW-X>SBZ%4Z3C=|bBRIo<v}UFuPerfI}Ht90T^k)%!UwHo;XlH@M+(v>9KL%FxIq@zK~'
        b'b&*B9i&Nd4w1`V>x7%K*9_Uw*={L8S9EO{3(>g5ecE^1rx0P~kTLQ83Q%HRzb*bd*dQ6ul{O+Itv+dU*VQVP7<$T+`<r?8%=t^*+'
        b'T!->?Ik)tZny#JA)_C2CR&AfcYLp94yU@E$x0y?R)<JJh?hcl1-=V5{r`D+xj?rUqhjO=xE>}G$KRXkyqv__#2p0{ne;uuDNqk<b'
        b'f{Zz{r%y{Oap4=$>AuKxk^cN{=%8rqVw;n^)>*xASJgM=e;Hbv!OTz8w9@iH$CmfL(HHYTX_sm=mLaXu2h`*<^q4h~B)co7@Vw;O'
        b'@cq#3OD^6Ld%I(XYePZk?zD>={rv3?MOv(wL7%(c@Mrm$M2eu;8$N85E}jstm&eiHJ~T}K_F?Isi<i??Oh<HH5DPb~49c78p@PEq'
        b'<m*UYV?0USy8Y>##=BhU^?SB$d!tU#&WZ-Bmc9q@*Kb%Xvl>Lc&Oo-<^!u^o-vBE88#7${M!)z*KzySoaBuq0C9g#>L^3UzOQrd;'
        b'hg56H9zoS0+Pu@pweaz9_s@mb<+8<IJ|K#8Hx!fl6!JlLp|(yH{XH{%Ki}iOjy4~@l8(15>*szzn#x~Eq0^$mqELB6gU54@CrOOf'
        b'okPkcBt-g`QsjPdTF<skNncyf4k_i>&PV$g@_w(8_xrY2q|4hfIzER)y!VRn{WrX^^M*G_bxT{_3z_NXzN7ayI>@GS?2?amp@R;x'
        b'K}3^%?yO!7Ju;g(jlY_90zzWrA17K`8mg<GyV%Y;w2oXdS=`8(Y-FuAUfzuKr<%P1b#055_6fw^=^wcar=^H2tLO#!fEYShM3<G2'
        b'KaVa;#c&B^S&z!gY9`BSXz?^WTK$T(og6QVwE6Q?B#2`pm*C3fof|Kw(m|4852*86v<_pRDzX~?e=INN>z8N!@0T~75j~j<tp`%c'
        b'GPYc`j4jo#RJOAxVnpqbN)*EnI9|1!Rq}Ff`tO!g&RnrSlQz{=?>PvGJ%60o(@6&Eo9W7kTJZsS=Oe4oE*IT}+EAxg!Pp!@Z-Bl?'
        b'X}Vw8ry_wXFFzAf&ZOSR#kg*3O1+7j)y`IG*JjKZRWq-oR2qjAYcrDjVo0*o%<*^I75=hKe!uF>9>>PmJ7-p%bmi)u8_UX7qzWr*'
        b'ZKBa-B=l91YPItEk{5Y0kFG#X`j3{h!m_*W6dmpMJ~dfvhSEn49;J)EYz@S!&&toJ8RJP8cmJsTc7(0dt%2|}U;(wf?}+(7VZHk='
        b'aqM~PB3jkU$H+6AMMcRf{`MrZnAoQkd&{1o8BG$bmh;h(Sl{B<#ih!Fq}OJ$%$?O^rEgy%HHe+og?TOWt%+Q!#i9$3oQ}El^rcFL'
        b'J)kKm4VKJpQj=qM>A|mRE?m*BdNR@`y7$mOw2AsF5ACcxbW1$hpU+*j@ApUceb1xrEBF2Axd@x>?~VQevbnZ5X`1u7iS6|6gUGWI'
        b';r&=(t|;ELOsJS!wUHLC@AXItaYaf<>mMgN3&_BZB6s1TdXxL6L+vbWxRL`#Q39EhMpg85Pk)-c#-Yx9MVf6<FrSo`c};R1c}1OZ'
        b'gEn-UmfIq^+^Xa;bl<XF-nUws$gY)Gsfr}$-(Q#O)tt;jeG1y-CczyhGM{5(7aQ3P!aG|M8A&RW8?@o-L=~-0!oP?6zuULlr}yo|'
        b'Q_%#hqzTAYISnKcafkBVa?gRRyM3-A->>+Zl=N7Y|K0xh|0ON<E7J1e(Elne?0=t@tB>{9R6(Q)-%_1OTAksg8^fD|^jDnb?3kQC'
        b'53PtKpx8jWXY%6zZ*>!GbJGTQuRbj~u=n+yFAimI-JYbOlXvbMO1qV`g}6u?n%)`ze`z0nc<}$;KFmG%|Dt_J>Xw1=mn<`eYlix3'
        b'hXS=jJ^s>)Pp0IPVyt}sKkY%&_Mb50;I{aK?fE_Z);htrt>RL&Q~3&Au2(@0C*#eAmgYt`J1QEo;~L#c(hwB2?)!!s`*|_RmqT_t'
        b'xl*>~rzO=kF0=~G+j!CK=}>q!^MSh$`b9m{Vc;A7-q6Aa?mWozoBTdKY3z{31Zi!y3!G6Xr)@sLImE?n-W+~>Gt}$1Hig#u+ua>B'
        b'ousQDel9FPpQ~4r-P$R%eJ=GW!)?lK;iRTzlccfjG@W)il~%32pLgb1EDC#P3@H@)owObdEw(85OqE<e$?>U3e8ocB8Ht{;pz%E%'
        b'jZZ~NGwHsNSc`K=tZv5;X_>kcBNa{lJldN%e$cDnGm<nJ)}#(4?d+zhij_r5YySKMCGFGE<)kGPPDI{;5oyz94E4_+3Yf`u**<n;'
        b'>VIt0eNFwj=ZgB%a`kh)aveStsl#Ir%5}K^ANs}$MWu1umIG@Z-I!tGQfr+G(&ftdhI~9EeXS?uzE)i5I{76ukuogg$%T;}imBB0'
        b'sVd*v@S)t-Qb+n)_qMZZ9&OeJPX^1xJDYctwte}m_sbJpmBG<Ch7|fIwL|JI<>{S`<q5*W2jsrito6Ab+S_V0C)}zj{9CxMP)Vzw'
        b'#I+f;`cX5bEvi24fIp3FnY9*1NTf*+zITA^@!4@VlU943(@Y9wu_0|P8RF*BonPIjaG2yHW4JC`m0+J2-s>an0$Sho_?i59I=RLx'
        b')vB+q@=7PBms!LLU(&R0vmfyK`8+4-nvmwS(rL&}%5y46w}>>TRq{zA+5tPhzMU=7dgmERlN6VaDT^XYE+Q?;{g29b98S>(3jZM;'
        b'ORr7G;uzX5BFV@ntNyl}4*fOh@cNI-L&qX1Ass5$)BHb8%e*Vo^7s{LA?1euyWRhp%|ed%_CO5psFsgY|LlAQsXLxIn5LB<7udNe'
        b'bk#Eo+~TVT4@L*GZy}{<YCnBf{BI9Fso<LL7xley%Y5_}K3y>U1j6+Dr|5|(-B=ub7M5GaX~#IGeg*lGQo)6vqi!=X^!2`erY%+u'
        b'vw+jKX=#`RTuQo@%+8W&WARM%UCdmHu#EPINLYIBXEFVrXjhOxq#q;POb3O+kbLT|iyiw?l6PAAZkcUUU;E5wbbll9WtepG&0R4W'
        b'xorBcr-bW5js7#d7<7r@SGG25sz@G8Ke#bHU+9bB>`;GpD3BexLq}gf-ZUj-gm`PvWihNXX>;Na&|4GfMNeImEyu0PW$Fx`T++MZ'
        b'J-K}J{vjbHM54Mp6GLaRuT7XU{!eC#rkyWRrdk-*Wh++N_-#yX;H@uoq@uA|c-~gV=hC}27?X?VxADa$64o;CO`APvE28gz<BOGv'
        b't+BE1Yi7TnJpcX0>bZ>lz<9B8wdtO@59adaZoS8)z989$rpMV|JLgc^_l?#meWs4NyL0(gH&4QRDv^*QL*sGr$#XInI&ZM|lVBr5'
        b'di%b^(K+jG^xf8R=kEK)Jud!lZkxw7NZ<cKW+O>rj4sYdjt?Y(BvBk2Kh7EB$>tfi7*Z{^BISkmwYpp~aAEBQn{5%jwZ(3*Sp=Rx'
        b'N9M38mD%j{8gZ6*dApjK@_#*8@`3VJrYv3m9SbkN?(U{fq<B?{{FUUJgSCD5g~Mpmn;aIK!Q`;pR3=BhjWan`*m#p;t<7w5Y_wTS'
        b'4zF#liNw0$U;gG~ZF;5CXfr6C7Mn`xwA(nPGvCH5ohxi+rE{&#qI7Pw%~d+R@$z$>oYHo(oaXafo<B(!EANYByvh|Gzli5^ZMN{F'
        b'a4()I(KG*}O|SJ2ymWF`chB?V$4o7OsYgN`cmL-0gw3sMTJ!!k=fZQ#B>(^b0000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        b'00000000000000000000000000001h|A##|5C8xG008oTZ3I<SRaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RTcK&KmY&$007AUwGmWRRaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaMx70|5X4001EW*G5oPRaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI40'
        b'RaI40RaI40RaI40RaI40RaI40RaI40RaI40RaI#Z4haAN000F2f9(nz000000000000000000000000000000000000000000000'
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
        b'00000000000000000000000000000000000000000000000000000263u5uJq5'
    )
    _firmware_identity = {'protocol': 1, 'firmware': 'CNC_FFST-S3-0.1.0', 'app_image_sha256': 'c5c1c2b6e4b3b0b2aff0d8139aa1fe7fcca9678f57148aa25aa237e31df7ac51', 'application_file_sha256': '9323e6e408f8e991a1a0b16c97861ea98fa33e4e3def202a343be041b9e36b0c'}
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
