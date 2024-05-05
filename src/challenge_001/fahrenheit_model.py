from pydantic import BaseModel, Field


class FahrenheitModel(BaseModel):
    """ファーレンハイト温度のモデル"""

    temperature: float = Field(
        ...,
        gt=-459.67,
    )
