from pydantic import BaseModel


class TimeSeriesModels(BaseModel):
    date: str  # Format %Y-%m-%d
    real: int
    predicted: float


class TimeSeries(BaseModel):
    FechaSolicitud: list[str]  # Fechas en formato %Y-%m-%d
    Count: list[int]