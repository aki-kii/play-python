from pydantic import BaseModel, Field

ABSOLUTE_TEMPERATURE = -459.67
"""絶対零度の温度"""

ROUND_DECIMAL = 2
"""小数点以下の有効桁数"""


class FahrenheitModel(BaseModel):
    """ファーレンハイト温度のモデル"""

    temperature: float = Field(
        ...,
        ge=ABSOLUTE_TEMPERATURE,
    )
    """温度"""

    def to_celsius(self) -> float:
        """セルシウス温度に変換する

        Returns:
            float: セルシウス温度
        """
        return round((self.temperature - 32) * 5 / 9, ROUND_DECIMAL)
