import pandas as pd
from datetime import date

from api.schemas import TimeSeries


def dpto_to_cod(department: str, cods: dict) -> int:
    return int(cods[department]['code'])


def mpio_to_cod(municipality: str, department: str, cods: dict) -> int:
    return int(cods[department]['municipalities'][municipality])


def count(
    df: pd.DataFrame,
    min_date: date = None,
    max_date: date = None
) -> TimeSeries:
    df.index = df["IdSolicitud"]
    count_df = df.groupby(by="FechaSolicitud").count()
    count_df.rename(columns={"IdSolicitud": "Count"}, inplace=True)

    # Limit dates
    if min_date is not None:
        count_df = count_df.loc[count_df.index >= min_date.strftime("%Y-%m-%d")]
    if max_date is not None:
        count_df = count_df.loc[count_df.index <= max_date.strftime("%Y-%m-%d")]

    return TimeSeries(
        FechaSolicitud=[ts.strftime('%Y-%m-%d') for ts in count_df.index],
        Count=count_df["Count"].tolist()
    )
