"""Generate the review schematic PDF. Requires reportlab; no KiCad/netlist claims.
The drawings are functional electrical proposals, not a released manufacturing schematic.
"""
from pathlib import Path
import csv
import json
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A3, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'artifacts/CNC_FFST_S3_Carrier_Proposta_R4.pdf'
PAGE_W, PAGE_H = landscape(A3)
MM = 72 / 25.4
INK = colors.HexColor('#162b3d')
BLUE = colors.HexColor('#166697')
GREEN = colors.HexColor('#23745c')
GRAY = colors.HexColor('#e9eef2')
RED = colors.HexColor('#a24029')
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
pdfmetrics.registerFont(TTFont('D', str(FONT_DIR / 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('DB', str(FONT_DIR / 'DejaVuSans-Bold.ttf')))

# Development-board header positions are intentionally not assigned before inspection.
PINS = [
 ('X_STEP',4,'out','STEP direto / RMT canal 0'), ('Y_STEP',5,'out','STEP direto / RMT canal 1'),
 ('Z_STEP',6,'out','STEP direto / RMT canal 2'), ('A_STEP',7,'out','STEP direto / RMT canal 3'),
 ('X_DIR',8,'out','DIR direto'), ('Y_DIR',9,'out','DIR direto'),
 ('Z_DIR',10,'out','DIR direto'), ('A_DIR',11,'out','DIR direto'),
 ('DRV_EN_REQ_N',12,'out','ENABLE comum, ativo baixo; pull-up 10k'),
 ('PWM_REQ',13,'out','PWM GPIO 3V3 antes do conversor TTL 5V; pull-down 100k'),
 ('LIMIT_X',1,'in','Entrada condicionada; contato NC'), ('LIMIT_Y',2,'in','Entrada condicionada; contato NC'),
 ('LIMIT_Z',14,'in','Entrada condicionada; contato NC'), ('LIMIT_A',15,'in','Entrada condicionada; contato NC'),
 ('PROBE',16,'in','Entrada condicionada; contato NO com GND'),
 ('ESTOP_ACTIVE',17,'in','Monitor de emergência; ativo alto'),
 ('DRV_FAULT_RESERVA',18,'reserved','Não conectado aos FAULT nesta R2'),
 ('USB_D_MINUS',19,'onboard','Reservado à USB nativa da DevKit'), ('USB_D_PLUS',20,'onboard','Reservado à USB nativa da DevKit'),
 ('GPIO21_RESERVA',21,'reserved','Reserva, sem circuito nesta revisão'),
 ('TOOL_ARM',42,'out','Habilitação lógica auxiliar; pull-down 100k'),
 ('FEED_HOLD',39,'in','Contato NO, condicionado'), ('CYCLE_START',40,'in','Contato NO, condicionado'),
 ('SAFETY_DOOR_RESERVA',41,'reserved','Reserva para intertravamento'),
 ('GPIO38_RESERVA',38,'reserved','Possível LED RGB integrado; não usar'), ('UART_TX',43,'onboard','Reservado ao USB/serial integrado'),
 ('UART_RX',44,'onboard','Reservado ao USB/serial integrado'), ('STATUS_RESERVA',47,'reserved','LED comum opcional'),
 ('GPIO48_RESERVA',48,'reserved','Possível LED RGB integrado; não usar')]
assert len({p[1] for p in PINS}) == len(PINS)
assert not {0,3,45,46,35,36,37,38,48,19,20,43,44}.intersection(p[1] for p in PINS if p[2] in ('in','out'))
assert all(gpio < 32 for _, gpio, _, _ in PINS[:10])

C = canvas.Canvas(str(OUT), pagesize=(PAGE_W, PAGE_H))
C.setTitle('CNC_FFST S3 — Proposta de esquema elétrico R4')
C.setAuthor('Projeto CNC_FFST')
C.setSubject('Placa-base para ESP32-S3 N16R8 dual USB encaixável e quatro DRV8825')

def txt(x,y,s,size=9,bold=False,color=INK):
    C.setFillColor(color); C.setFont('DB' if bold else 'D',size)
    C.drawString(x*MM,PAGE_H-y*MM,str(s))

def line(x1,y1,x2,y2,color=INK,width=.8):
    C.setStrokeColor(color); C.setLineWidth(width)
    C.line(x1*MM,PAGE_H-y1*MM,x2*MM,PAGE_H-y2*MM)

def box(x,y,w,h,title=None,fill=None):
    C.setStrokeColor(INK); C.setLineWidth(.8)
    C.setFillColor(fill or colors.white)
    C.rect(x*MM,PAGE_H-(y+h)*MM,w*MM,h*MM,fill=bool(fill),stroke=1)
    if title:txt(x+3,y+5,title,10,True)

def note(x,y,w,text,size=9,color=INK):
    lines=simpleSplit(text,'D',size,w*MM)
    for i,s in enumerate(lines):txt(x,y+i*4,s,size,color=color)
    return y+4*len(lines)

def node(x,y):
    C.setFillColor(INK);C.circle(x*MM,PAGE_H-y*MM,.65*MM,fill=1,stroke=0)

def ground(x,y):
    line(x,y,x,y+3)
    for dy,half in [(3,2.4),(4,1.6),(5,.7)]:line(x-half,y+dy,x+half,y+dy)

def res(x1,y,x2,label):
    mid=(x1+x2)/2
    line(x1,y,mid-4,y);box(mid-4,y-1.3,8,2.6);line(mid+4,y,x2,y)
    txt(mid-10,y-3,label,8)

def cap(x,y,label):
    line(x,y,x,y+3);line(x-2,y+3,x+2,y+3);line(x-2,y+4.4,x+2,y+4.4)
    line(x,y+4.4,x,y+8);ground(x,y+8);txt(x+3,y+4,label,8)

def input_pin(x,y,label,span=14):
    txt(x-span-33,y-1,label,8,color=BLUE);line(x-span,y,x,y)

def output_pin(x,y,label,span=14):
    line(x,y,x+span,y);txt(x+span+1,y+1,label,8,color=BLUE)

def gate(x,y,kind,ref,a,b,out):
    box(x,y,32,21,ref)
    txt(x+7,y+13,kind,11,True)
    line(x-9,y+8,x,y+8);txt(x-43,y+7,a,8,color=BLUE)
    line(x-9,y+16,x,y+16);txt(x-43,y+15,b,8,color=BLUE)
    line(x+32,y+12,x+43,y+12);txt(x+44,y+13,out,8,color=BLUE)

def header(page,title):
    txt(12,13,'CNC_FFST S3',20,True)
    txt(92,13,title,15,True)
    line(12,18,408,18,BLUE,1.3)
    txt(12,25,'R4 — PROPOSTA PARA REVISÃO | NÃO LIBERADA PARA FABRICAÇÃO',10,True,RED)
    txt(12,31,'22/10/2026 • Placa-base para DevKit ESP32-S3 N16R8 dual USB • X/Y/Z/A • DRV8825 • 24 V',9)
    line(12,280,408,280,BLUE)
    txt(12,286,'Pontos com [PENDENTE] exigem dimensionamento/validação. Rótulos iguais representam a mesma rede.',8)
    txt(360,286,f'Folha {page} / 9',9,True)

def end():C.showPage()

# 1 — carrier connections; no physical connector position is invented.
header(1,'ESP32 encaixável e distribuição dos GPIOs')
box(55,49,106,156,'U1 — DEVKIT ESP32-S3 N16R8',GRAY)
txt(61,62,'Encaixe em duas barras de soquetes',9)
txt(61,70,'USB e regulador na própria DevKit',8.5)
left=[('3V3_DK','3V3'),('GND comum','GND'),('LIMIT_X','GPIO1'),('LIMIT_Y','GPIO2'),
      ('LIMIT_Z','GPIO14'),('LIMIT_A','GPIO15'),('PROBE','GPIO16'),
      ('ESTOP_ACTIVE','GPIO17'),('FEED_HOLD','GPIO39'),('CYCLE_START','GPIO40')]
for i,(name,pin) in enumerate(left):
    y=83+i*10.5
    line(49,y,55,y);txt(15,y-1,name,8,color=BLUE);txt(57,y+1,pin,7)
right=[('X_STEP',4),('Y_STEP',5),('Z_STEP',6),('A_STEP',7),
       ('X_DIR',8),('Y_DIR',9),('Z_DIR',10),('A_DIR',11),
       ('DRV_EN_REQ_N',12),('PWM_REQ',13),('TOOL_ARM',42)]
for i,(name,gpio) in enumerate(right):
    y=84+i*10
    txt(139,y+1,f'IO{gpio}',7);line(161,y,169,y);txt(171,y+1,name,8,color=BLUE)
box(242,44,166,177,'Conexões propostas: usar a marcação GPIO')
for i,(signal,gpio,kind,detail) in enumerate([p for p in PINS if p[2]!='reserved']):
    y=57+i*6.5
    txt(246,y,signal,8);txt(307,y,f'GPIO{gpio}',8,True)
    txt(349,y,{'out':'saída carrier','in':'entrada carrier','onboard':'USB da DevKit'}[kind],8)
note(15,221,210,'Placa de desenvolvimento N16R8: 16 MB flash / 8 MB PSRAM. O anúncio não pôde ser acessado. A posição física, quantidade de pinos e distância entre fileiras precisam ser conferidas na unidade real antes do footprint.',9,color=RED)
note(15,245,210,'Não usar GPIO35/36/37 (PSRAM octal), GPIO0/3/45/46 (straps), GPIO19/20 (USB nativa), GPIO43/44 (USB/serial) ou GPIO38/48 (possível RGB integrado). Sem LED endereçável usando RMT.',9)
note(242,230,165,'STEP/DIR/ENABLE continuam diretos. Os quatro STEP usam os quatro canais RMT TX internos. TOOL_ARM foi movido para GPIO42 para evitar o RGB de algumas variantes. Não é um ENABLE separado dos drivers.',9)
note(242,252,165,'Só conectar aos pinos que tiverem essas marcações na placa real. Não confundir número GPIO com posição do conector. Firmware 0.1.3 compilado; mapa elétrico R2 preservado. Validação física pendente.',9,color=RED)
end()

# 2 — complete functional socket connections, not a physical top view.
header(2,'Soquetes dos quatro módulos DRV8825')

def driver(x,y,axis,ref):
    box(x,y,190,95,f'{ref} — DRV8825 encaixável • eixo {axis}')
    bx=x+66;by=y+17
    box(bx,by,56,64,f'SOQUETE {axis}',GRAY)
    ins=[('9  /EN','DRV_EN_N'),('15 STEP',axis+'_STEP'),('16 DIR',axis+'_DIR'),
         ('13 /RESET','DRV_WAKE'),('14 /SLEEP','DRV_WAKE'),('10 M0',axis+'_M0'),
         ('11 M1',axis+'_M1'),('12 M2',axis+'_M2')]
    outs=[('8 VMOT','VMOT_24V'),('1 GND','GND'),('7 GND','GND'),('4 A1',axis+'_A1'),
          ('3 A2',axis+'_A2'),('5 B1',axis+'_B1'),('6 B2',axis+'_B2'),('2 /FAULT','TP_'+axis+'_FAULT')]
    for i,(pin,net) in enumerate(ins):
        yy=by+12+i*6.2
        txt(bx+2,yy+1,pin,7.3);line(bx-10,yy,bx,yy);txt(x+3,yy-1,net,8,color=BLUE)
    for i,(pin,net) in enumerate(outs):
        yy=by+12+i*6.2
        txt(bx+35,yy+1,pin,7.3);line(bx+56,yy,bx+66,yy);txt(bx+67,yy+1,net,7.7,color=BLUE)
    txt(x+3,y+88,'STEP/DIR: série 33 Ω opcional + pull-down 100k no lado do módulo.',8)
    txt(x+3,y+93,'VMOT: 100 µF / 50 V + 100 nF locais. Saída motor: A1/A2/B1/B2.',8)
for x,y,a,ref in [(12,41,'X','A1'),(216,41,'Y','A2'),(12,144,'Z','A3'),(216,144,'A','A4')]:driver(x,y,a,ref)
note(14,247,191,'Microstep por eixo: três jumpers ligam M0/M1/M2 a 3V3; pull-down 100k para cada entrada. Tabela DRV8825: 000=1; 100=1/2; 010=1/4; 110=1/8; 001=1/16; 101/011/111=1/32 (ordem M0,M1,M2).',8)
note(216,247,191,'A numeração é a convenção do símbolo KiCad Pololu_Breakout_DRV8825, não uma vista física de inserção. Confirmar o módulo real, orientação de VMOT/GND e espaçamento dos soquetes antes do layout. /FAULT fica separado em TP por eixo.',8,color=RED)
end()

# 3 — prototype powered through development board USB, separate 24V motors.
header(3,'Placa-base: 24 V nos drivers, USB na ESP32')
box(15,47,50,26,'J1 — ENTRADA')
txt(19,61,'24 V DC / GND',10)
line(65,60,88,60)
box(88,47,49,26,'F1 + proteção')
txt(91,61,'inversão [PENDENTE]',8)
line(137,60,164,60);txt(141,56,'VMOT_24V',9,True,BLUE)
node(155,60);line(155,60,155,86)
box(139,86,49,25,'TVS [PENDENTE]');ground(163,111)
line(164,60,221,60);txt(174,55,'para quatro soquetes',9)
cap(207,60,'470 µF / 50 V')
box(15,135,203,63,'U1 — DEVKIT ENCAIXADA')
txt(20,149,'USB da DevKit → regulador integrado → 3V3_DK.',9)
line(218,153,230,153);txt(177,147,'3V3_DK',8,True,BLUE)
cap(225,153,'10 µF')
txt(20,160,'3V3_DK alimenta somente a lógica da placa-base.',9)
txt(20,171,'GND da DevKit ligado ao GND da alimentação dos drivers.',9)
txt(20,182,'Nenhuma conexão entre 24 V e 5V/VBUS/3V3 da DevKit.',9,True,RED)
txt(20,191,'3V3 = 3V3_DK: mesma rede, originada na DevKit. 100 nF por CI.',8)
ground(110,198)
box(15,216,203,36,'U_SUP + buffer de DRV_WAKE [PENDENTE]')
txt(20,230,'Monitorar 3V3_DK; /RESET e /SLEEP dos módulos altos só com lógica válida.',8)
txt(20,240,'Não alterar o circuito EN/RESET existente na DevKit nesta proposta.',8.5)
box(243,47,161,74,'Usar os conectores USB da própria DevKit')
txt(248,62,'Sem USB, CH340 ou CP2102 adicional na placa-base.',8.5)
txt(248,72,'USB nativa: reservar GPIO19 e GPIO20.',9)
txt(248,82,'USB/serial integrado: reservar GPIO43 e GPIO44.',9)
txt(248,92,'Escolher a porta de comunicação de acordo com o firmware.',8)
txt(248,103,'Duas USBs: não assumir que os circuitos de alimentação',8)
txt(248,111,'sejam iguais entre clones; conferir a placa real.',8)
box(243,137,161,58,'Alimentação dos primeiros testes')
txt(248,152,'ESP32: alimentada pela sua própria USB.',9,True)
txt(248,162,'Motores: fonte de 24 V separada, com proteção.',9,True)
txt(248,172,'GND comum, com retornos de potência separados da lógica.',8)
txt(248,182,'R4: buck 24 V → 5V_LOGIC separado, ver folha 9.',8.5)
box(243,211,161,41,'BOOT / RESET / manutenção')
txt(248,226,'Aproveitar os botões e a USB da DevKit.',9)
txt(248,235,'Não ligar outro TX externo aos pinos ocupados pelo USB/serial.',8)
txt(248,244,'Deixar acesso físico aos conectores e botões após o encaixe.',8)
note(16,261,388,'Fusível, proteção de inversão, TVS e supervisor ainda dependem de seleção/cálculo. Manter VMOT abaixo de 45 V, incluindo transientes e margem. A placa-base não deve alimentar a USB do computador. Operação futura sem cabo USB exigirá outra revisão de alimentação, após conferir o circuito da DevKit.',8.5,color=RED)
end()

# 4 — sensor conditioning, electrical circuit with dry contact terminal.
header(4,'Limites, sonda e comandos de painel')

def sensor(x,y,signal,gpio,nc=False,probe=False):
    box(x,y,190,61,f'{signal} → GPIO{gpio}')
    txt(x+5,y+14,'3V3',8,color=BLUE)
    line(x+19,y+16,x+19,y+23);box(x+17.7,y+23,2.6,8)
    txt(x+23,y+28,'4,7k',8);line(x+19,y+31,x+19,y+37);node(x+19,y+37)
    line(x+6,y+37,x+19,y+37);txt(x+3,y+34,'J: sinal',8)
    res(x+19,y+37,x+68,'1k')
    node(x+68,y+37);cap(x+68,y+37,'1 nF' if probe else '10 nF')
    line(x+68,y+37,x+110,y+37)
    # Schmitt inverter with output bubble.
    C.setStrokeColor(INK);C.setFillColor(colors.white)
    p=C.beginPath();p.moveTo((x+110)*MM,PAGE_H-(y+31)*MM);p.lineTo((x+110)*MM,PAGE_H-(y+43)*MM);p.lineTo((x+123)*MM,PAGE_H-(y+37)*MM);p.close()
    C.drawPath(p,stroke=1,fill=0)
    C.circle((x+124.5)*MM,PAGE_H-(y+37)*MM,1.5*MM,stroke=1,fill=0)
    line(x+126,y+37,x+138,y+37);txt(x+139,y+38,signal,8,color=BLUE)
    txt(x+110,y+27,'74LVC14A / 3V3',7.5)
    txt(x+5,y+56,'J: retorno GND; contato '+('NC' if nc else 'NO')+'. Sem 5 V ou 24 V nesta entrada.',8)
for args in [(12,43,'LIMIT_X',1,True,False),(216,43,'LIMIT_Y',2,True,False),
             (12,111,'LIMIT_Z',14,True,False),(216,111,'LIMIT_A',15,True,False),
             (12,179,'PROBE',16,False,True),(216,179,'FEED_HOLD',39,False,False)]:sensor(*args)
note(15,250,187,'CYCLE_START → GPIO40 usa o mesmo circuito de FEED_HOLD, com contato NO. Limites NC: cabo rompido deve gerar limite. Polaridades e pulls internos: folha 7. Circuito completo de CYCLE_START: folha 6.',8.5)
note(216,250,190,'Reservar proteção ESD na entrada dos conectores; MPN a selecionar. A sonda é contato elétrico com GND: validar a referência elétrica da ferramenta/PCB antes da ligação. Histerese e filtro não substituem ensaios de ruído e repetibilidade.',8.5,color=RED)
end()

# 5 — independent EStop gate and tool selector.
header(5,'ENABLE comum, emergência e seleção de ferramenta')
box(15,45,177,54,'J_ESTOP — contato auxiliar NC')
txt(20,59,'Contato NC entre ESTOP_LOOP e GND; pull-up 4,7k a 3V3.',8.5)
txt(20,68,'Série 1k + 10 nF → inversor Schmitt → SAFETY_OK.',8.5)
txt(20,77,'Outro inversor → ESTOP_ACTIVE (GPIO17).',8.5)
txt(20,86,'Normal: SAFETY_OK=1; acionado/cabo rompido: SAFETY_OK=0.',8)
box(219,45,185,54,'Seleção e emergência: circuito de potência externo')
txt(224,60,'A chave seleciona a alimentação: laser OU spindle.',9)
txt(224,69,'A emergência interrompe a energia das ferramentas.',8.5)
txt(224,78,'Não há chave seletora no caminho do sinal PWM.',8.5)
txt(224,87,'Tensões, contatos e proteções dependem das cargas reais.',8.5)
gate(65,113,'OR','U_EN','DRV_EN_REQ_N','ESTOP_ACTIVE','DRV_EN_N')
txt(15,148,'GPIO12: pull-up 10k → 3V3. DRV_EN_N → /EN dos quatro módulos.',9)
txt(15,157,'DRV_EN_N = 1: todos desabilitados. = 0: todos habilitados.',9)
txt(15,166,'DRV_WAKE baixo mantém os módulos em reset/sleep se a lógica não estiver válida.',8.5)
gate(261,113,'AND','U_PWM1','PWM_REQ','TOOL_ARM','PWM_ARMED')
txt(219,148,'GPIO13 e GPIO42 com pull-down 100k.',9)
gate(65,187,'AND','U_PWM2','PWM_ARMED','SAFETY_OK','PWM_OUT')
txt(15,221,'PWM_OUT = PWM_REQ AND TOOL_ARM AND SAFETY_OK.',9,True)
txt(15,230,'Portas lógicas em 3V3; 100 nF por CI. Estado inativo do PWM: baixo.',8.5)
box(243,176,160,62,'PWM comum: conversão para 5 V na folha 8')
line(248,200,273,200);txt(247,195,'PWM_5V',8,color=BLUE)
node(273,200);line(273,190,273,211)
line(273,190,322,190);txt(324,191,'TTL_LASER',8,color=BLUE)
line(273,211,322,211);txt(324,212,'GATE_SPINDLE',8,color=BLUE)
txt(248,225,'PWM_OUT=3V3 → conversor → PWM_5V compartilhado.',8)
txt(248,233,'Chave externa atua somente na alimentação das ferramentas.',8)
note(15,247,190,'PWM_5V controla TTL do laser e MOSFET do spindle (folhas 8/9). A chave comuta alimentação; laser recebe +24V_LASER. Trocar com M5/S0 e movimento parado. A posição da chave não é lida pelo firmware. Validar se a entrada PWM do módulo desligado permite sinal sem causar retroalimentação; condicionamento ainda pendente.',8.3)
note(219,247,184,'Lógica funcional proposta, sem certificação de segurança. Autenticação implementada; UART/USB 0.1.3 compilados. Perfil protegido opcional 0.2.3 exige chaves do proprietário e teste físico. O bloqueio físico de energia não depende de o ESP32 executar o firmware.',8.5,color=RED)
end()
# 6 — explicit second panel input, not merely a repeated-circuit note.
header(6,'Botões de painel: Pausar e Retomar')
sensor(15,46,'FEED_HOLD',39,False,False)
sensor(219,46,'CYCLE_START',40,False,False)
note(18,121,184,'PAUSAR: contato normalmente aberto (NO) entre J:sinal e GND. Solto: J=3,3 V e GPIO39=0. Pressionado: J=0 V e GPIO39=1. O inversor 74LVC14A muda a polaridade; pull-up externo de 4,7k está no lado do contato.',10)
note(222,121,179,'RETOMAR: contato normalmente aberto (NO) entre J:sinal e GND. Solto: J=3,3 V e GPIO40=0. Pressionado: J=0 V e GPIO40=1. Repetir filtro, inversor e desacoplamento; não unir GPIO39 e GPIO40.',10)
box(15,161,389,40,'Pausas do firmware e conferência no Python são diferentes')
note(19,174,380,'Feed Hold pausa o movimento pelo grblHAL; Cycle Start retoma quando permitido pelo estado da controladora. Na Pausa para Conferência de Posicionamento e Ajuste Fino gerenciada pelo Python, o botão físico não substitui Retornar na interface. Fechar a caixa não continua o arquivo.',10)
box(15,213,389,43,'Ligação e limites elétricos')
note(19,227,380,'Circuitos em 3,3 V, GND comum e 100 nF de desacoplamento por CI. Nunca aplicar 5 V ou 24 V ao GPIO. Não ligar o contato direto ao GPIO presumindo acionamento em zero: este BIN espera o condicionamento com inversores. Pull-ups internos não substituem resistores externos, filtros ou emergência física.',10,color=RED)
end()

# 7 — exact firmware defaults, distinct from external contact-side resistors.
header(7,'Entradas: polaridade e pulls internos do firmware')
note(15,42,388,'Referência: CNC_FFST-S3 UART/USB 0.1.3, mapa Carrier R2 (documentação R4), fonte e190011. Valores padrão do BIN, antes de alterações salvas no GRBL. 0 = nível baixo/GND; 1 = nível alto/3,3 V. A coluna GPIO se refere à saída do condicionador, não ao contato no conector.',10)
cols=[15,70,91,125,159,202,250,291,404]
labels=['Entrada','GPIO','Inativo','Ativo','Pull-up interno','Pull-down','Contato J','Acionamento no J']
for a,b,label in zip(cols,cols[1:],labels):
    box(a,64,b-a,12,fill=GRAY);txt(a+2,72,label,8,True)
entries=[('Limite X',1,'1','0','SIM','NÃO','NC','Abre / cabo rompe'),('Limite Y',2,'1','0','SIM','NÃO','NC','Abre / cabo rompe'),('Limite Z',14,'1','0','SIM','NÃO','NC','Abre / cabo rompe'),('Limite A',15,'1','0','SIM','NÃO','NC','Abre / cabo rompe'),('Sonda',16,'0','1','SIM','NÃO','NO','Fecha para GND'),('Emergência',17,'0','1','SIM','NÃO','NC','Abre / cabo rompe'),('Pausar',39,'0','1','SIM','NÃO','NO','Fecha para GND'),('Retomar',40,'0','1','SIM','NÃO','NO','Fecha para GND')]
for i,row in enumerate(entries):
    y=76+i*10
    for a,b,value in zip(cols,cols[1:],row):
        box(a,y,b-a,10);txt(a+2,y+6.5,value,8.5)
note(15,164,388,'TODAS as oito entradas acima têm pull-up interno habilitado e pull-down interno desabilitado no padrão do programa. Pull-up não define a polaridade ativa: sonda, emergência e botões são ativos em 1 mesmo tendo pull-up. Sem o condicionador, deixar esses GPIOs abertos pode indicar entrada acionada.',10,color=RED)
note(15,187,388,'Resistores EXTERNOS do esquema: 4,7k a 3V3 no lado dos contatos; filtros série 1k + capacitor e inversor 74LVC14A. Limites/sonda/botões usam um inversor; a emergência usa dois até GPIO17. Esses resistores não são os pulls internos configurados pelo software.',9)
note(15,207,388,'Configuração padrão: $5=15 (inversão de limites XYZA), $6=0 (sonda), $14=0 (controles); $17=0, $18=0 e $19=0 mantêm os pull-ups de controles, limites e sonda. São valores de referência, NÃO instruções para sobrescrever a configuração da máquina. Leia $$ para conferir os valores atuais.',9)
note(15,228,388,'Fontes verificadas: boards/my_machine_map.h, platformio.ini, grbl/config.h, grbl/ioports.c e driver.c (gpio_config para ESP32-S3). O PDF não lê a flash da sua placa. Alterações persistentes de inversão/pulls mudam o comportamento; valide entradas com ferramentas sem potência antes de mover.',9)
note(15,248,388,'GPIO18 (fault), GPIO21 e GPIO41 (porta de segurança) são reservas SEM função de entrada mapeada neste BIN; não há pull/polaridade funcional garantidos para essas reservas. USB19/20, UART43/44, PSRAM e boot não são entradas de comando disponíveis. Emergência física deve cortar energia independentemente do software.',9,color=RED)
end()
# 8 — the MKS-style translator, after the existing 3V3 safety gates.
header(8,'TTL 5 V: conversor e conector do laser 24 V')
note(15,42,389,'Topologia inspirada na MKS DLC32 V2.1_003, folha MOSFET (7/9). Aqui o sinal já passa por TOOL_ARM e SAFETY_OK antes da conversão. O positivo do laser é 24 V comutado pela seleção/emergência, não 5 V. Pinagem dos conectores abaixo é a proposta CNC_FFST, não a ordem de qualquer laser comercial.',9)
box(112,75,111,75,'U_TTL — SN74LVC1T45DCK')
txt(119,92,'6 VCCB = 3V3_DK',10);txt(119,103,'1 VCCA = 5V_LOGIC',10)
txt(119,114,'4 B = entrada 3V3',10);txt(119,125,'3 A = saída 5 V',10)
txt(119,136,'5 DIR = GND (B → A)',10);txt(119,145,'2 GND = GND comum',9)
line(23,114,112,114);txt(23,108,'PWM_OUT (folha 5)',9,True,BLUE)
node(81,114);line(81,114,81,130);box(79.5,130,3,10);txt(65,145,'100k',8);ground(81,140)
line(223,125,271,125);txt(230,119,'PWM_5V',10,True,BLUE)
node(255,125);line(255,125,255,156);txt(259,155,'→ folha 9: R_GATE → Q_SP',9)
res(271,125,319,'220 Ω');line(319,125,344,125)
box(344,85,60,61,'J_LASER — 3 pinos')
txt(348,102,'1  +24V_LASER',9,True);txt(348,113,'2  GND',9);txt(348,126,'3  TTL 5 V',9,True)
node(330,125);line(330,125,330,146);box(328.5,146,3,10);txt(312,160,'10k',8);ground(330,156)
line(340,99,344,99);txt(275,94,'+24V_LASER: folha 9',9,True,RED)
line(340,99,340,102);line(340,102,344,102)
line(340,113,344,113);ground(340,113)
note(15,175,187,'Alimentação U_TTL: 100 nF + 1 µF entre VCCA e GND; outros 100 nF + 1 µF entre VCCB e GND, próximos ao CI. Usar o encapsulamento DCK e conferir o datasheet antes do layout. DIR aterrado seleciona B → A: 3,3 V para 5 V, sem inversão.',9)
note(219,175,184,'Baixo = laser desligado; alto/PWM 5 V = comando ativo, se esse for o padrão do módulo. O resistor série limita correntes de falha, mas NÃO garante ausência de alimentação parasita com o laser sem 24 V. Conferir a entrada TTL do laser real antes de ligar.',9,color=RED)
box(15,215,389,48,'O que muda e o que permanece')
note(19,228,380,'GPIO13 continua PWM 3,3 V e GPIO42 continua TOOL_ARM: não há mudança de pinagem ou BIN. Só a etapa externa passa a gerar 5 V. R39/pull-down equivalente mantém B baixo sem comando; 10k mantém TTL baixo se a saída ficar em alta impedância. Não ligar PWM_5V, +24V_LASER ou 5V_LOGIC a um GPIO. GND do laser deve ser GND fixo, nunca o dreno chaveado do spindle.',9)
end()

# 9 — motor low-side switch and independent positive-side tool selection.
header(9,'Spindle MOSFET e seleção de potência 24 V')
box(15,42,389,52,'Alimentação positiva: seleção independente do PWM')
txt(20,57,'24V_TOOL → F_TOOL → K_ESTOP (contato de potência) → chave LASER / 0 / SPINDLE',10,True)
txt(20,69,'Saída LASER → F_LASER → +24V_LASER (J_LASER pino 1).',10)
txt(20,81,'Saída SPINDLE → F_SP → +24V_SP (J_SP pino 1). GND da fonte permanece comum.',10)
box(15,105,224,105,'Q_SP — MOSFET N, chaveamento no negativo')
line(162,123,219,123);txt(166,119,'+24V_SP',9,True,RED)
box(193,123,29,29,'M_SP');txt(197,142,'DC 24 V',8)
line(207,152,207,165);line(155,165,207,165);txt(160,161,'SP_MINUS',8,True)
# Abstract MOSFET: gate isolated from the drain/source channel.
line(155,165,155,176);line(155,176,155,192);line(151,176,151,192)
line(143,184,151,184);line(155,192,155,199);ground(155,199)
txt(161,180,'D',8);txt(161,196,'S',8);txt(141,180,'G',8)
res(33,184,112,'47 Ω');line(112,184,143,184);txt(22,175,'PWM_5V',9,True,BLUE)
node(127,184);line(127,184,127,192);box(125.5,192,3,8);txt(107,202,'100k',8);ground(127,200)
# Flyback diode parallel with the motor, cathode positive.
line(179,123,179,132);line(175,132,183,132);txt(163,130,'K',7)
pth=C.beginPath();pth.moveTo(175*MM,PAGE_H-141*MM);pth.lineTo(183*MM,PAGE_H-141*MM);pth.lineTo(179*MM,PAGE_H-132*MM);pth.close();C.drawPath(pth,stroke=1,fill=0)
line(179,141,179,165);node(179,165);txt(164,149,'A',7);txt(164,156,'D_FREE',7)
box(249,105,155,43,'J_SP — 2 pinos')
txt(254,121,'1 = +24V_SP selecionado',9,True)
txt(254,132,'2 = SP_MINUS (dreno de Q_SP)',9,True)
txt(254,142,'Motor entre 1 e 2; pino 2 NÃO é GND fixo.',8)
note(249,160,155,'Q_SP: selecionar MOSFET com RDS(on) especificado a VGS=4,5 V e VDS de pelo menos 60 V, com margem para transientes. Corrente, Qg, dissipador, fusível, TVS e D_FREE dependem do spindle real. D_FREE: cátodo no positivo; ânodo no dreno. Validar driver de gate se a carga de gate/frequência exigir.',8.5,color=RED)
box(15,220,389,43,'U_5V — conversor buck separado para a lógica TTL')
note(19,232,380,'24 V protegido → buck 24/5 V → 5V_LOGIC → VCCA de U_TTL. Selecionar módulo/CI para a faixa real da fonte e transientes (entrada nominal máxima ≥36 V, conforme dimensionamento). Incluir desacoplamento conforme datasheet. 5V_LOGIC NÃO se conecta ao VBUS/5V da DevKit: a ESP32 segue alimentada pela própria USB. Retornos de motor e laser separados do retorno lógico até a fonte.',8.8)
note(15,271,389,'Potência ainda não dimensionada: sem corrente/tipo do spindle, este estágio NÃO está liberado para fabricação. É para motor DC com escovas, não saída de VFD ou motor AC. Chave deve abrir antes de fechar; emergência atua fisicamente em K_ESTOP. Trocar somente parado com M5/S0.',8,color=RED)
end()
C.save()

with (ROOT/'hardware/pinagem_carrier_r4.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f,lineterminator='\n');w.writerow(['sinal','gpio','tipo','observacao','posicao_fisica'])
    for signal,gpio,kind,detail in PINS:w.writerow([signal,gpio,kind,detail,'CONFERIR NA DEVKIT REAL'])
write={'revision':'R4','status':'PROPOSTA_CARRIER_NAO_FABRICAR',
       'development_board':'ESP32-S3 N16R8 dual USB, modelo exato a conferir',
       'board_removable':True,'development_board_power':'USB da propria DevKit',
       'carrier_has_usb_connector':False,'carrier_has_usb_serial_bridge':False,
       'flash_mb':16,'psram_mb':8,'header_positions_verified':False,
       'listing_url':'https://www.mercadolivre.com.br/p/MLB2069410538',
       'axes':list('XYZA'),'driver':'DRV8825 StepStick 2x8, validar modulo real',
       'common_enable':True,'motor_supply_v':24,'pwm_gpio_v':3.3,'pwm_output_v':5,'laser_supply_v':24,'ttl_translator':'SN74LVC1T45DCK, DIR=0 B->A','spindle_power_stage':'N-MOS low-side, brushed DC24V; parts/rating pending',
       'pwm_permanently_connected_to':['laser','spindle'],
       'tool_selection':'chave externa na alimentacao; nao no PWM',
       'firmware_driver_commit':'0b2d3e1bb7da3b0ae0e03490b71275374eb84c67',
       'core_submodule_commit':'4ec1ae44b857a70d2f9298344feac4b43ed0eb6b',
       'manufacturing_released':False,'firmware_built':True,'firmware_version':'0.1.3','electrical_pinmap_revision':'R2','inputs_default_pull':'UP','inputs_default_pulldown':False,'inputs_active_low':[1,2,14,15],'inputs_active_high':[16,17,39,40],
       'pending':['Foto/pinout e medidas da DevKit real: numero de pinos, espacamento e botoes/USB',
                  'Protecao da entrada de 24V, supervisor e conectores com MPNs e calculos',
                  'Entrada PWM dos modulos sem alimentacao: impedancia e retroalimentacao',
                  'Confirmacao dos GPIOs expostos, do RGB e da alimentacao USB do modelo real',
                  'Validacao fisica de firmware, autenticacao e protecao/atualizacao criptografada na S3',
                  'ERC/DRC de projeto EDA, layout e validacao eletrica/termica/EMC/seguranca']}
(ROOT/'hardware/proposta_carrier_r4.json').write_text(json.dumps(write,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(OUT)
