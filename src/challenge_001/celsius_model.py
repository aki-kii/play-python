from pydantic import BaseModel, Field


class CelsiusModel(BaseModel):
    """セルシウス温度のモデル"""

    temperature: float = Field(
        ...,
        gt=-273.15,
    )

    def to_fahrenheit(self) -> float:
        fahrenheit = self.temperature * 1.8 + 32
        return fahrenheit
