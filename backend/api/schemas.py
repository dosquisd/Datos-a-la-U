from pydantic import BaseModel


class RealData(BaseModel):
    date_request: str  # Format %Y-%m-%d
    real_value: int


class PredictedData(BaseModel):
    date_request: str  # Format %Y-%m-%d
    predicted_value: float | None = None


class Data(BaseModel):
    real: list[RealData]
    predicted: list[PredictedData] | None = None
