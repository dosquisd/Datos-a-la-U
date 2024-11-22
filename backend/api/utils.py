import numpy as np
import pandas as pd
from datetime import date, timedelta

from api.schemas import RealData, PredictedData


def dpto_to_cod(department: str, cods: dict) -> int:
    return int(cods[department]['code'])


def mpio_to_cod(municipality: str, department: str, cods: dict) -> int:
    return int(cods[department]['municipalities'][municipality])


def count(
    df: pd.DataFrame,
    min_date: date = None,
    max_date: date = None
) -> list[RealData]:
    df.index = df["IdSolicitud"]
    count_df = df.groupby(by="FechaSolicitud").count()
    count_df.rename(columns={"IdSolicitud": "Count"}, inplace=True)

    # Limit dates
    if min_date is not None:
        count_df = count_df.loc[count_df.index >= min_date.strftime("%Y-%m-%d")]
    if max_date is not None:
        count_df = count_df.loc[count_df.index <= max_date.strftime("%Y-%m-%d")]
    
    dts = [ts.strftime('%Y-%m-%d') for ts in count_df.index]
    values = count_df["Count"].tolist()

    return [RealData(date_request=dt, real_value=value) 
            for dt, value in zip(dts, values)]


def generate_random_timeserie(
    first_date: date,
    last_date: date | None = None,
    range_values: tuple[int, int] | None = None
) -> list[PredictedData]:
    """
    Generate a random timeseries. By default, if last_date is None,
    then timeserie is for a month
    """
    if last_date is None:
        last_date = first_date + timedelta(days=30)
    
    if range_values is None:
        range_values = (0, 100)

    dts = pd.date_range(
        start=first_date.strftime("%Y-%m-%d"),
        end=last_date.strftime("%Y-%m-%d"),
        freq="D"
    ).strftime("%Y-%m-%d")

    n = len(dts)
    values = np.random.randint(range_values[0], range_values[1] + 1, size=n)

    return [PredictedData(date_request=dt, predicted_value=value) 
            for dt, value in zip(dts, values)]
