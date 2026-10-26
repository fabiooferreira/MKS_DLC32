import bpy,json,sys,math
from pathlib import Path
from mathutils import Vector
p=Path(sys.argv[sys.argv.index('--')+1])
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
for i,item in enumerate(json.loads((p/'preview_mesh.json').read_text())):
 mesh=bpy.data.meshes.new('mesh'+str(i));mesh.from_pydata(item['vertices'],[],item['faces']);mesh.update()
 ob=bpy.data.objects.new('piece'+str(i),mesh);bpy.context.collection.objects.link(ob)
 mat=bpy.data.materials.new('material'+str(i));mat.diffuse_color=(*item['color'],1);mat.use_nodes=True
 bs=mat.node_tree.nodes.get('Principled BSDF');bs.inputs['Base Color'].default_value=(*item['color'],1)
 c=item['color'];metal=(c[2]>.5 and c[0]<.1) or c[0]>.6
 bs.inputs['Metallic'].default_value=.7 if metal else .05;bs.inputs['Roughness'].default_value=.32 if metal else .48
 ob.data.materials.append(mat)
# diffuse studio ground, in same millimetre coordinate system
bpy.ops.mesh.primitive_plane_add(size=200,location=(0,0,1.5));plane=bpy.context.object
m=bpy.data.materials.new('ground');m.diffuse_color=(.8,.83,.88,1);plane.data.materials.append(m)
def aim(ob,at):ob.rotation_euler=(Vector(at)-ob.location).to_track_quat('-Z','Y').to_euler()
bpy.ops.object.camera_add(location=(34,-46,37));camera=bpy.context.object;aim(camera,(0,0,12));camera.data.type='ORTHO';camera.data.ortho_scale=38;bpy.context.scene.camera=camera
for pos,power,size in [((0,-25,55),35000,35),((-35,10,30),25000,30),((25,30,45),35000,25)]:
 bpy.ops.object.light_add(type='AREA',location=pos);ob=bpy.context.object;ob.data.energy=power;ob.data.shape='DISK';ob.data.size=size;aim(ob,(0,0,10))
scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=96;scene.cycles.use_denoising=False
scene.world.color=(.35,.35,.35);scene.render.resolution_x=1200;scene.render.resolution_y=1200;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG';scene.render.filepath=str(p/'Previa_3D.png');scene.view_settings.view_transform='Standard'
bpy.ops.wm.save_as_mainfile(filepath=str(p/'TWOTREES_TMC2209_V20_Visual.blend'))
bpy.ops.render.render(write_still=True)
