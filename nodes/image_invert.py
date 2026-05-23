import torch


class ImageInvert:
    """
    图片反色节点：将输入图像的每个像素值取反 (1 - value)。
    支持 RGB / RGBA 图像，Alpha 通道保持不变。
    """

    CATEGORY = "Hifar/Image"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            },
            "optional": {
                "invert_alpha": ("BOOLEAN", {"default": False, "label_on": "Yes", "label_off": "No"}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "invert"

    def invert(self, image: torch.Tensor, invert_alpha: bool = False) -> tuple:
        """
        Parameters
        ----------
        image : torch.Tensor
            Shape: (B, H, W, C), dtype float32, 取值范围 [0.0, 1.0]。
            C 为 3 (RGB) 或 4 (RGBA)。
        invert_alpha : bool
            是否同时反转 Alpha 通道（仅对 RGBA 图像有效）。

        Returns
        -------
        tuple[torch.Tensor]
            反色后的图像，形状与输入相同。
        """
        result = image.clone()

        if result.shape[-1] == 4 and not invert_alpha:
            # RGBA：只反转 RGB，保留 Alpha
            result[..., :3] = 1.0 - result[..., :3]
        else:
            # RGB 全部反转，或 RGBA 且用户选择反转 Alpha
            result = 1.0 - result

        return (result,)
