import bpy


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


def register_operator(idname, label, func):
    """Register bones.set/next/prev"""
    class Op(bpy.types.Operator):
        bl_idname = idname
        bl_label = label
        def execute(self, context):
            func()
            return {'FINISHED'}
    bpy.utils.register_class(Op)
    

def register_panel():
    """Show Bone Traversal side panel in 3D View"""
    class Panel(bpy.types.Panel):
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
    bpy.utils.register_class(Panel)


def main():
    register_operator('bones.set', 'Set Bones', set_bones)
    register_operator('bones.next', 'Next Bone', next_bone)
    register_operator('bones.prev', 'Prev Bone', prev_bone)
    register_panel()
    

if __name__ == '__main__':
    main()

