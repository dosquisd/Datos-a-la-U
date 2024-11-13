from pydantic import BaseModel


class RealData(BaseModel):
    date_request: str  # Format %Y-%m-%d
    value: int


class PredictedData(BaseModel):
    date_request: str  # Format %Y-%m-%d
    value: float | None = None


class Data(BaseModel):
    real: list[RealData]
    predicted: list[PredictedData] | None = None
