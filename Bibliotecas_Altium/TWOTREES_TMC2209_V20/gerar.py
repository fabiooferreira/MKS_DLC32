from pathlib import Path
import cadquery as cq, xml.etree.ElementTree as E, csv, json
P=Path(__file__).parent
A=cq.Assembly(name='TWOTREES_TMC2209_V20_COM_DISSIPADOR')
parts=[]
def add(shape,name,color):
 A.add(shape,name=name,color=cq.Color(*color));parts.append((shape,color))
def block(x,y,z,w,d,h,name,color):
 shape=cq.Workplane('XY').box(w,d,h).translate((x,y,z+h/2));add(shape,name,color);return shape
black=(.04,.045,.055);gold=(.82,.62,.19);pcb=(.08,.085,.09);white=(.88,.88,.86)
# Coordinate system: carrier board top z=0; module sits in nominal 8.5 mm sockets.
board=cq.Workplane('XY').box(15.24,20.32,1.6).translate((0,0,9.3))
pins=[]
left=['EN_N','MS1','MS2','PDN','USART','CLK','STEP','DIR']
right=['VM','GND_POWER','M1B','M1A','M2A','M2B','VIO','GND_LOGIC']
for side,names in [(-1,left),(1,right)]:
 for i,name in enumerate(names):
  x=side*6.35;y=8.89-i*2.54;number=i+1 if side==-1 else i+9
  pins.append((number,name,x,y))
  board=board.cut(cq.Workplane('XY').circle(.5).extrude(4).translate((x,y,7.5)))
  block(x,y,2.6,.64,.64,9.2,'pin_'+str(number),gold)
  ring=cq.Workplane('XY').circle(.88).circle(.5).extrude(.035).translate((x,y,10.1));add(ring,'pad_'+str(number),gold)
  block(x,y,7.1,2.3,2.3,1.4,'header_spacer_'+str(number),(.65,.07,.16))
add(board,'PCB_15p24x20p32',pcb)
# Dimensions below are nominal visualization estimates, not a TWOTREES mechanical drawing.
block(0,-.5,10.1,8.81,10.19,.035,'thermal_copper',gold)
block(0,-.5,10.135,8.6,10,.18,'thermal_adhesive',(.55,.55,.56))
block(0,-.5,10.315,9,10.5,1,'heatsink_base',(.035,.16,.62))
for i in range(7):block(-3.9+i*1.3,-.5,11.315,.55,10.5,11,'heatsink_fin_'+str(i),(.035,.19,.72))
# underside IC and passives, realistic physical arrangement, approximate positions.
block(0,-.5,7.55,5,5,.9,'TMC2209_QFN_underside',black)
for i in range(12):
 x=-4 if i<6 else 4;y=-5+(i%6)*1.5
 block(x,y,7.9,1,.6,.6,'SMD_'+str(i),(.24,.22,.18))
block(3.2,7,10.1,2.7,2.7,1.2,'VREF_trimmer',(.18,.19,.21))
add(cq.Workplane('XY').circle(.85).extrude(.15).translate((3.2,7,11.3)),'trimmer_screw',(.72,.72,.73))
# Auxiliary pads shown visually only; not assigned carrier through-holes.
for i in range(2):add(cq.Workplane('XY').circle(.85).circle(.45).extrude(.04).translate((-3.8+i*2.54,8.89,10.1)),'auxiliary_pad_'+str(i),gold)
for label,pos in [('TWOTREES',(0,-7.4,10.14)),('TMC2209 V2.0',(0,-8.5,10.14)),('EN',(-5.0,8,10.14)),('VM',(5,8,10.14))]:
 try:add(cq.Workplane('XY').text(label,.8,.02,combine=True).translate(pos),'label_'+str(len(parts)),white)
 except Exception:pass
A.save(str(P/'TWOTREES_TMC2209_V20_Dissipador.step'))
# Separate socket model, same origin and coordinates.
S=cq.Assembly(name='SOQUETES_STEPSTICK_2X8')
for side in [-1,1]:
 body=cq.Workplane('XY').box(2.54,20.32,7).translate((side*6.35,0,3.5))
 for i in range(8):
  y=8.89-i*2.54
  body=body.cut(cq.Workplane('XY').rect(.85,.85).extrude(9).translate((side*6.35,y,0)))
  S.add(cq.Workplane('XY').box(.64,.64,3).translate((side*6.35,y,-1.5)),name=f'tail_{side}_{i}',color=cq.Color(*gold))
 S.add(body,name='socket_'+str(side),color=cq.Color(*black))
S.save(str(P/'Soquetes_2x8_12p70mm.step'))
A.add(S,name='SOQUETES_CARRIER')
A.save(str(P/'TWOTREES_TMC2209_V20_Completo.step'))
# EAGLE XML library, supported interchange via Altium EAGLE Importer.
r=E.Element('eagle',version='9.6.2');drawing=E.SubElement(r,'drawing');layers=E.SubElement(drawing,'layers')
for n,name,color in [(1,'Top',4),(16,'Bottom',1),(17,'Pads',2),(21,'tPlace',7),(25,'tNames',7),(27,'tValues',7),(51,'tDocu',7),(94,'Symbols',4),(95,'Names',7),(96,'Values',7)]:E.SubElement(layers,'layer',number=str(n),name=name,color=str(color),fill='1',visible='yes',active='yes')
lib=E.SubElement(drawing,'library');E.SubElement(lib,'description').text='TWOTREES TMC2209 V2.0 module; nominal StepStick socket. Import into Altium. Mechanical review required.'
packs=E.SubElement(lib,'packages');pkg=E.SubElement(packs,'package',name='TWOTREES_TMC2209_V20_SOCKET_2X8')
for num,name,x,y in pins:E.SubElement(pkg,'pad',name=str(num),x=str(x),y=str(y),drill='1.0',diameter='1.9',shape='square' if num==1 else 'round')
for x1,y1,x2,y2 in [(-7.62,-10.16,7.62,-10.16),(7.62,-10.16,7.62,10.16),(7.62,10.16,-7.62,10.16),(-7.62,10.16,-7.62,-10.16)]:E.SubElement(pkg,'wire',x1=str(x1),y1=str(y1),x2=str(x2),y2=str(y2),width='.15',layer='21')
for text,yy,layer in [('>NAME',11.5,'25'),('>VALUE',-12.8,'27')]:E.SubElement(pkg,'text',x='-7.62',y=str(yy),size='1',layer=layer).text=text
E.SubElement(pkg,'text',x='-5',y='8',size='.8',layer='21').text='EN'
E.SubElement(pkg,'text',x='3.6',y='8',size='.8',layer='21').text='VM'
syms=E.SubElement(lib,'symbols');sym=E.SubElement(syms,'symbol',name='TWOTREES_TMC2209_V20')
for x1,y1,x2,y2 in [(-12.7,-12.7,12.7,-12.7),(12.7,-12.7,12.7,12.7),(12.7,12.7,-12.7,12.7),(-12.7,12.7,-12.7,-12.7)]:E.SubElement(sym,'wire',x1=str(x1),y1=str(y1),x2=str(x2),y2=str(y2),width='.254',layer='94')
for num,name,x,y in pins:E.SubElement(sym,'pin',name=name,x=str(-17.78 if num<=8 else 17.78),y=str(y),length='middle',direction='pas' if name.startswith(('PDN','USART','GND')) or name=='CLK' else ('pwr' if name in ['VM','VIO'] else ('out' if name in ['M1A','M1B','M2A','M2B'] else 'in')),rot='R0' if num<=8 else 'R180')
E.SubElement(sym,'text',x='-12.7',y='15.24',size='1.27',layer='95').text='>NAME'
E.SubElement(sym,'text',x='-12.7',y='-15.24',size='1.27',layer='96').text='>VALUE'
devs=E.SubElement(lib,'devicesets');ds=E.SubElement(devs,'deviceset',name='TWOTREES_TMC2209_V20',prefix='U');g=E.SubElement(ds,'gates');E.SubElement(g,'gate',name='G$1',symbol='TWOTREES_TMC2209_V20',x='0',y='0');dev=E.SubElement(E.SubElement(ds,'devices'),'device',name='',package='TWOTREES_TMC2209_V20_SOCKET_2X8');conn=E.SubElement(dev,'connects')
for num,name,x,y in pins:E.SubElement(conn,'connect',gate='G$1',pin=name,pad=str(num))
E.SubElement(E.SubElement(dev,'technologies'),'technology',name='');E.indent(r);E.ElementTree(r).write(P/'TWOTREES_TMC2209_V20.lbr',encoding='utf-8',xml_declaration=True)
with (P/'pinagem.csv').open('w') as f:
 w=csv.writer(f,lineterminator='\n');w.writerow(['pad','sinal','x_mm','y_mm']);w.writerows(pins)
# Mesh intermediate for a physically lit Blender preview (STEP generation is independent).
import shutil,subprocess
meshes=[]
for shape,col in parts:
 for solid in shape.solids().vals():
  vs,fs=solid.tessellate(.08)
  meshes.append({'vertices':[[v.x,v.y,v.z] for v in vs],'faces':fs,'color':col})
(P/'preview_mesh.json').write_text(json.dumps(meshes))
if shutil.which('blender'):
 subprocess.run(['blender','-b','--python',str(P/'render_blender.py'),'--',str(P)],check=True)
print('Generated',len(pins),'pins;',len(parts),'colored components')
