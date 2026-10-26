from pathlib import Path
import csv,json,xml.etree.ElementTree as E
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import ezdxf
p=Path(__file__).parent;rows=list(csv.DictReader((p/'pinagem.csv').open()))
doc=ezdxf.new();doc.units=4;ms=doc.modelspace()
for layer in ['CONTORNO','FUROS','PADS','NOMES']:doc.layers.new(layer)
ms.add_lwpolyline([(-7.62,-10.16),(7.62,-10.16),(7.62,10.16),(-7.62,10.16)],close=True,dxfattribs={'layer':'CONTORNO'})
for r in rows:
 x,y=float(r['x_mm']),float(r['y_mm']);ms.add_circle((x,y),.5,dxfattribs={'layer':'FUROS'});ms.add_circle((x,y),.95,dxfattribs={'layer':'PADS'})
 ms.add_text(r['pad']+' '+r['sinal'],dxfattribs={'height':.65,'insert':(x+1.2,y),'layer':'NOMES'})
doc.saveas(p/'Footprint_mecanico.dxf')
c=canvas.Canvas(str(p/'Footprint_1para1.pdf'))
c.setFont('Helvetica-Bold',14);c.drawString(35,800,'TWOTREES TMC2209 V2.0 - Gabarito NOMINAL / escala 1:1')
c.setFont('Helvetica',10)
for i,t in enumerate(['Imprimir em TAMANHO REAL (100%), sem ajustar a pagina.','Medidas estimadas: conferir no modulo antes de fabricar.','Vista superior; EN/VM na extremidade superior.','A numeracao dos pads e propria desta biblioteca.']):c.drawString(35,775-i*16,t)
ox,oy=105*mm,190*mm
c.rect(ox-7.62*mm,oy-10.16*mm,15.24*mm,20.32*mm)
for r in rows:
 x,y=float(r['x_mm']),float(r['y_mm']);c.circle(ox+x*mm,oy+y*mm,.5*mm);c.circle(ox+x*mm,oy+y*mm,.95*mm)
 c.drawString(ox+(x+1.3)*mm if x>0 else ox+(x-27)*mm,oy+y*mm-3,r['pad']+' '+r['sinal'])
c.line(40*mm,120*mm,90*mm,120*mm);c.drawString(40*mm,115*mm,'Barra de controle: 50 mm')
c.drawString(35,70,'Furos e folgas devem ser conferidos para os soquetes selecionados. Nao liberado para fabricacao.')
c.save()
(p/'dimensoes.json').write_text(json.dumps({'module':'TWOTREES TMC2209 V2.0','release':'A_ESTUDO','physical_measurement':False,'altium_tested':False,'row_pitch_mm':12.7,'pin_pitch_mm':2.54,'pcb_estimated_mm':[15.24,20.32,1.6],'socket_body_estimated_mm':7,'module_pcb_bottom_z_mm':8.5,'sink_estimated_mm':[9,10.5,12],'carrier_drill_proposed_mm':1,'carrier_pad_proposed_mm':1.9,'nominal_height_mm':22.315},indent=2))
xml=E.parse(p/'TWOTREES_TMC2209_V20.lbr');pads=xml.findall('.//package/pad');pins=xml.findall('.//symbol/pin');connections=xml.findall('.//connect')
assert len(pads)==len(pins)==len(connections)==16
assert {v.get('name') for v in pads}=={str(i) for i in range(1,17)}
assert len({(v.get('x'),v.get('y')) for v in pads})==16
for conn in connections:
 row=next(r for r in rows if r['pad']==conn.get('pad'));assert row['sinal']==conn.get('pin')
assert next(r['sinal'] for r in rows if r['pad']=='15')=='VIO'
assert next(r['sinal'] for r in rows if r['pad']=='5')=='USART'
print('PASS: 16 unique pads, symbol-to-pad mapping, VIO and USART as photographed; DXF and 1:1 PDF generated.')
