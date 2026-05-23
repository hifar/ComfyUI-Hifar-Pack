import torch


class GetImagesFromBatch:
    """
    从一个 IMAGE batch 中按索引取出指定图片，组成新的 batch 输出。
    支持负索引（-1 表示最后一张）。

    示例：
        indices = "0, 3, 4"  →  输出第 0、3、4 张图片组成的 batch（共 3 张）
        indices = "0, -1"    →  输出第 0 张和最后一张
    """

    CATEGORY = "Hifar/Image"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "indices": ("STRING", {
                    "default": "0",
                    "multiline": False,
                    "tooltip": "逗号分隔的索引，支持负索引，例如：0, 3, 4  或  0, -1",
                }),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("images",)
    FUNCTION = "get_images"

    def get_images(self, images: torch.Tensor, indices: str) -> tuple:
        """
        Parameters
        ----------
        images : torch.Tensor
            Shape: (B, H, W, C), dtype float32。
        indices : str
            逗号分隔的整数索引字符串，例如 "0, 3, 4"。

        Returns
        -------
        tuple[torch.Tensor]
            按指定顺序排列的子 batch，shape (N, H, W, C)。
        """
        batch_size = images.shape[0]

        # 解析索引字符串
        try:
            idx_list = [int(s.strip()) for s in indices.split(",") if s.strip() != ""]
        except ValueError as e:
            raise ValueError(f"[GetImagesFromBatch] indices 格式错误：{e}，请使用逗号分隔的整数，例如 '0, 3, 4'")

        if not idx_list:
            raise ValueError("[GetImagesFromBatch] indices 不能为空")

        # 范围校验（支持负索引转正）
        normalized = []
        for i in idx_list:
            pos = i if i >= 0 else batch_size + i
            if pos < 0 or pos >= batch_size:
                raise IndexError(
                    f"[GetImagesFromBatch] 索引 {i} 超出范围，当前 batch 共 {batch_size} 张图片"
                )
            normalized.append(pos)

        # 按索引取出并拼接
        selected = torch.stack([images[i] for i in normalized], dim=0)
        return (selected,)
