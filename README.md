
# Mirror to Real Mesh (Keep Shape Keys)

Blender addon to convert a mesh that uses a Mirror modifier into real mirrored geometry **while preserving all Shape Keys**.

This solves Blender's limitation where modifiers cannot be applied to meshes that have Shape Keys, and prevents Blendshape loss when exporting to FBX for Unity, VRChat, or other engines.

---

# Why this addon exists

In Blender, you cannot apply the Mirror modifier if the mesh contains Shape Keys.

This creates a major problem when exporting to FBX:

* Mirror modifier is not exported as real geometry
* Blendshapes may break or disappear
* Unity cannot read them correctly

This addon fixes the problem by converting the mirrored side into real mesh geometry without destroying Shape Keys.

---

# Features

* Preserves all Shape Keys
* One-click operation
* No modifier application required
* Unity-compatible result
* VRChat-ready meshes
* Non-destructive workflow
* Works in Blender 3.6+

---

# How it works

The addon performs the following steps automatically:

1. Removes the Mirror modifier
2. Duplicates the mesh
3. Mirrors it using Global X scale
4. Fixes normals
5. Joins the original and mirrored mesh
6. Merges center vertices

Result:

A fully symmetrical real mesh with Shape Keys intact.

---

# Installation

1. Download the addon file:

```
mirror_to_real_with_shapekey.py
```

2. Open Blender

3. Go to:

```
Edit → Preferences → Add-ons
```

4. Click:

```
Install
```

5. Select the .py file

6. Enable the addon checkbox

---

# Usage

1. Select a mesh that has:

* Mirror modifier
* Shape Keys

2. Open the Sidebar:

```
Press N key
```

3. Go to:

```
Shapekey Tools tab
```

4. Click:

```
Apply Real Mirror
```

Done.

---

# Recommended use cases

* Unity character export
* Blendshape export
* VRChat avatars
* Game character pipelines
* Finalizing production meshes

---

# Before / After

Before:

* Mirror modifier
* Shape Keys
* Cannot apply modifier

After:

* No modifier
* Real mirrored geometry
* Shape Keys fully working
* Ready for FBX export

---

# Compatibility

Tested on:

Blender 3.6
Unity 2021+
Unity 2022+
VRChat SDK

Should work on newer Blender versions.

---

# Limitations

* Assumes symmetry on X axis
* Always creates real geometry
* Original mirror modifier will be removed

It is recommended to save a backup before use.

---

# License

MIT License

You are free to use, modify, and distribute.

---

# Contributing

Pull requests and suggestions are welcome.

---

# Author

Your Name

GitHub: [https://github.com/owsam](https://github.com/owsam)

---

# Repository description (short)

Use this in the GitHub "About" section:

**Blender addon to apply mirror as real geometry while preserving shape keys. Fixes Unity blendshape export issues.**

---

# Optional: Add this topic tags on GitHub

Recommended topics:

```
blender
blender-addon
unity
vrchat
blendshape
shapekey
fbx
3d
gamedev
```

