from pydantic import BaseModel, Field


class NaturalNumberModel(BaseModel):
    """100以下の自然数のモデル

    本来なら目的に沿った名前をつけたい所ですが、演習問題のため説明的な名前にしています。
    """

    number: int = Field(
        ...,
        ge=1,
        le=100,
    )
    """100以下の自然数"""

    def list_multiples(self) -> list[int]:
        """入力値に対する100以下の倍数をリスト化する

        Returns:
            list[int]:  100以下の倍数のリスト
        """
        # 100以下の倍数の個数
        multiple_size = 100 // self.number

        return [i * self.number for i in range(1, multiple_size + 1)]
