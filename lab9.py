import os
import bpy

bpy.ops.object.select_all(action = "DESELECT")

for obj in bpy.data.objects:    # for every object in the scene
    if obj.type == "MESH":      # check if object is a mesh
        obj.select_set(True)    # select object 
        
bpy.ops.object.delete()         # delete selected

path = "curuthers.obj"
bpy.ops.import_scene.obj(filepath = path)
obj = bpy.context.selected_objects[0]

bpy.context.view_layer.objects.active = obj
obj.name = "JoinedName"
obj.data.name = "JoinedData"
bpy.ops.object.join()

if not os.path.exists("export"):
    os.mkdir("export")

bpy.ops.export_scene.obj(
    filepath = "export/myfile.obj", 
    use_selection = True, 
    path_mode = "COPY"
    )
