# Blender Bone Traversal

I asked this on the blender stack exchange and decided to try building it myself:
https://blender.stackexchange.com/q/228008/70346

Sometimes you have a group of bones selected and you want to animate them or their bone constraints over time, but manually selecting each bone in order to set keyframes on position or constraints is tedious.

With this script, it makes it much easier to cycle between a subset of bones.

## Requirements
Blender 2.93+ (Tested in LTS)

## Installation
1. Download Latest Release
2. Edit > Preferences > Add-ons > Install > blender_bone_traversal.py
3. Observe "Bone Traversal" panel in 3D View

## Usage

1. Select an armature and switch to Pose Mode.
2. Select a subset of bones within the armature.
3. Open the "Bone Traversal" panel, and select "Set Bones" aka `bones.set`
4. Select Next or Prev to cycle through those bones (aka `bones.prev` or `bones.next`)
