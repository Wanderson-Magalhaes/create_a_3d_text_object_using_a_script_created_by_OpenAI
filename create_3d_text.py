import bpy

class Create3DTextPanel(bpy.types.Panel):
    bl_label = "Create 3D Text"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tools"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.prop(context.scene, "text_to_create")
        row = layout.row()
        row.operator("object.create_3d_text")

class Create3DTextOperator(bpy.types.Operator):
    bl_idname = "object.create_3d_text"
    bl_label = "Create 3D Text"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.text_add()
        context.active_object.data.body = context.scene.text_to_create
        return {'FINISHED'}

def register():
    bpy.utils.register_class(Create3DTextPanel)
    bpy.utils.register_class(Create3DTextOperator)
    bpy.types.Scene.text_to_create = bpy.props.StringProperty(name="Text", default="My Text")

def unregister():
    bpy.utils.unregister_class(Create3DTextPanel)
    bpy.utils.unregister_class(Create3DTextOperator)
    del bpy.types.Scene.text_to_create

if __name__ == "__main__":
    register()
