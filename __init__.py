"""
ComfyUI-Hifar-Pack
==================
Hifar 自定义节点库的入口文件。

新增节点步骤：
1. 在 nodes/ 目录下新建 .py 文件，定义节点类。
2. 在本文件的 import 区域导入该类。
3. 将类名添加到 NODE_CLASS_MAPPINGS 和 NODE_DISPLAY_NAME_MAPPINGS。
"""

from .nodes.image_invert import ImageInvert
from .nodes.get_images_from_batch import GetImagesFromBatch

# ── 节点注册 ──────────────────────────────────────────────────────────────────
# key   : ComfyUI 内部唯一标识符（建议加前缀避免与其他插件冲突）
# value : 节点类
NODE_CLASS_MAPPINGS = {
    "HifarImageInvert": ImageInvert,
    "HifarGetImagesFromBatch": GetImagesFromBatch,
}

# key   : 与 NODE_CLASS_MAPPINGS 对应的 key
# value : 在 ComfyUI 节点菜单中显示的名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "HifarImageInvert": "Image Invert (Hifar)",
    "HifarGetImagesFromBatch": "Get Images From Batch (Hifar)",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
