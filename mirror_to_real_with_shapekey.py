bl_info = {
    "name": "Mirror to Real Mesh (Keep Shape Keys)",
    "author": "Osamu Watanabe",
    "version": (1, 1),
    "blender": (3, 6, 0),
    "location": "View3D > Sidebar > Shapekey Tools",
    "description": "Apply mirror manually while keeping shape keys",
    "category": "Object",
}

import bpy
import bmesh


# =========================
# Operator
# =========================

class OBJECT_OT_apply_real_mirror(bpy.types.Operator):

    bl_idname = "object.apply_real_mirror_keep_shapekey"
    bl_label = "Apply Real Mirror"
    bl_options = {'REGISTER', 'UNDO'}


    merge_distance: bpy.props.FloatProperty(
        name="Merge Distance",
        default=0.0001,
        min=0.0,
        precision=6
    )


    def execute(self, context):

        obj = context.active_object

        if obj is None or obj.type != 'MESH':
            self.report({'ERROR'}, "Mesh object required")
            return {'CANCELLED'}


        # Mirror modifier 削除
        for mod in obj.modifiers:
            if mod.type == 'MIRROR':
                obj.modifiers.remove(mod)


        # 複製
        bpy.ops.object.select_all(action='DESELECT')

        obj.select_set(True)
        context.view_layer.objects.active = obj

        bpy.ops.object.duplicate()

        mirror_obj = context.active_object


        # Global X ミラー
        mirror_obj.scale[0] *= -1

        bpy.ops.object.transform_apply(
            location=False,
            rotation=False,
            scale=True
        )


        # 法線修正
        bpy.ops.object.mode_set(mode='EDIT')

        bpy.ops.mesh.select_all(action='SELECT')

        bpy.ops.mesh.flip_normals()

        bpy.ops.mesh.normals_make_consistent(inside=False)

        bpy.ops.object.mode_set(mode='OBJECT')


        # Join
        bpy.ops.object.select_all(action='DESELECT')

        obj.select_set(True)
        mirror_obj.select_set(True)

        context.view_layer.objects.active = obj

        bpy.ops.object.join()


        # Merge
        bpy.ops.object.mode_set(mode='EDIT')

        bm = bmesh.from_edit_mesh(obj.data)

        bmesh.ops.remove_doubles(
            bm,
            verts=bm.verts,
            dist=self.merge_distance
        )

        bmesh.update_edit_mesh(obj.data)

        bpy.ops.object.mode_set(mode='OBJECT')


        self.report({'INFO'}, "Mirror applied successfully")

        return {'FINISHED'}



# =========================
# Sidebar Panel
# =========================

class VIEW3D_PT_shapekey_tools(bpy.types.Panel):

    bl_label = "Shapekey Tools"
    bl_idname = "VIEW3D_PT_shapekey_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Shapekey Tools"


    def draw(self, context):

        layout = self.layout

        layout.operator(
            "object.apply_real_mirror_keep_shapekey",
            icon='MOD_MIRROR'
        )



# =========================
# Register
# =========================

classes = (

    OBJECT_OT_apply_real_mirror,
    VIEW3D_PT_shapekey_tools,

)


def register():

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)



if __name__ == "__main__":
    register()