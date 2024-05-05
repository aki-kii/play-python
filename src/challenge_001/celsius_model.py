from pydantic import BaseModel, Field

ABSOLUTE_TEMPERATURE = -273.15
"""絶対零度の温度"""

ROUND_DECIMAL = 2
"""小数点以下の有効桁数"""


class CelsiusModel(BaseModel):
    """セルシウス温度のモデル"""

    temperature: float = Field(
        ...,
        ge=ABSOLUTE_TEMPERATURE,
    )
    """温度"""

    def to_fahrenheit(self) -> float:
        """ファーレンハイト温度に変換する

        Returns:
            float: ファーレンハイト温度
        """
        return round(self.temperature * 1.8 + 32, ROUND_DECIMAL)
