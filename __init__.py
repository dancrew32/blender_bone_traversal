import bpy

bl_info = {
    "name": "Bone Traversal",
    "blender": (2, 93, 0),
    "category": "3D View",
}


def select_bones(bones, select=True):
    """Select a list of bones"""
    for bone in bones:
        bone.select = select
    
    
def set_bones():
    """Set a list of bones for bone traversal"""
    pose_bones = bpy.context.selected_pose_bones_from_active_object
    bones = [pose_bone.bone for pose_bone in pose_bones]
    select_bones(bones)
    bpy.props.cur_bones = bones
    bpy.props.cur_bone = None


def next_bone():
    """Select the next bone in the list of bones"""
    cur_bones = bpy.props.cur_bones
    if cur_bones is None:
        raise Exception('run bones.set first')
    cur_bones_len = len(cur_bones)
    cur_bone = getattr(bpy.props, 'cur_bone', None)
    if cur_bone is None:
        index = -1
    else:
        index = cur_bones.index(cur_bone)
    next_index = 0 if index + 1 == cur_bones_len else index + 1
    next_bone = cur_bones[next_index]
    select_bones(cur_bones, False)
    select_bones([next_bone])
    bpy.props.cur_bone = next_bone


def prev_bone():
    """Select the previous bone in the list of bones"""
    cur_bones = bpy.props.cur_bones
    if cur_bones is None:
        raise Exception('run bones.set first')
    cur_bones_len = len(cur_bones)
    cur_bone = getattr(bpy.props, 'cur_bone', None)
    if cur_bone is None:
        index = cur_bones_len - 1
    else:
        index = cur_bones.index(cur_bone)
    prev_index = cur_bones_len - 1 if index - 1 == -1 else index - 1 
    prev_bone = cur_bones[prev_index]
    select_bones(cur_bones, False)
    select_bones([prev_bone])
    bpy.props.cur_bone = prev_bone


class Panel(bpy.types.Panel):
    """Show Bone Traversal side panel in 3D View"""

    bl_idname = "BONE_TRAVERSAL_PT_PANEL"
    bl_label = "Bone Traversal"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Bone Traversal"

    @classmethod
    def poll(cls, context):
        return context.mode in {'POSE'}

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.operator("bones.set")
        row = box.row()
        row.operator("bones.prev")
        row.operator("bones.next")


class OpSetBones(bpy.types.Operator):
    bl_idname = 'bones.set'
    bl_label = 'Set Bones'

    def execute(self, context):
        set_bones()
        return {'FINISHED'}


class OpNextBone(bpy.types.Operator):
    bl_idname = 'bones.next'
    bl_label = 'Next Bone'

    def execute(self, context):
        next_bone()
        return {'FINISHED'}


class OpPrevBone(bpy.types.Operator):
    bl_idname = 'bones.prev'
    bl_label = 'Prev Bone'

    def execute(self, context):
        prev_bone()
        return {'FINISHED'}


def register():
    bpy.utils.register_class(OpSetBones)
    bpy.utils.register_class(OpNextBone)
    bpy.utils.register_class(OpPrevBone)
    bpy.utils.register_class(Panel)


def unregister():
    bpy.utils.unregister_class(OpSetBones)
    bpy.utils.unregister_class(OpNextBone)
    bpy.utils.unregister_class(OpPrevBone)
    bpy.utils.unregister_class(Panel)


if __name__ == "__main__":
    register()
