
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

Osamu Watanabe

GitHub: [https://github.com/owsam](https://github.com/owsam)

---

# Repository description (short)

Use this in the GitHub "About" section:

**Blender addon to apply mirror as real geometry while preserving shape keys. Fixes Unity blendshape export issues.**

---


# Mirror to Real Mesh (Keep Shape Keys)

Blender用アドオン
Mirrorモディファイアを使用して作成されたメッシュを、**Shape Keyを保持したまま実メッシュとしてミラー化**します。

Blender標準仕様では、Shape Keyが存在するメッシュにMirrorモディファイアを適用することはできません。このアドオンは、Mirrorを使わずに同等の結果を生成することで、この制限を回避します。

Unityなどの外部ソフトへFBXエクスポートする際のBlendshape消失問題の解決に有効です。

---

# 特徴

* Shape Keyを完全保持
* Mirrorモディファイア不要
* ワンクリック実行
* Blender 3.6対応
* Unity互換FBX作成に最適

---

# 動作原理

以下の処理を自動で実行します：

1. Mirrorモディファイアを削除
2. メッシュを複製
3. Global Xで反転
4. 法線を修正
5. 元メッシュと結合
6. 中央頂点をMerge by Distanceで統合

これにより、Shape Keyを壊さずに完全な対称メッシュを生成します。

---

# インストール

1. このリポジトリをダウンロード

または

Code → Download ZIP

2. Blenderを開く

3. Edit → Preferences → Add-ons

4. Install をクリック

5. `mirror_to_real_with_shapekey.py` を選択

6. チェックをON

---

# 使い方

1. MirrorモディファイアとShape Keyを持つメッシュを選択

2. 3Dビューで

```
Nキー → Shapekey Tools → Apply Real Mirror
```

3. ボタンをクリック

完了です。

---

# 使用用途

* Unity用キャラクター作成
* FBX Blendshape保持
* VRChatアバター制作
* Shape Key付きモデルの最終化

---

# 注意事項

* X軸対称メッシュを前提としています
* 実行前にバックアップを推奨します

---

# 対応バージョン

Blender 3.6 以上

---

# ライセンス

MIT License

自由に使用・改変・配布可能

---

# 作者

Osamu Watanabe


