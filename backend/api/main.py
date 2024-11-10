from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import pandas as pd
import os
import uvicorn
import sys
import json

from datetime import date

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    """
    I don't care that this is deprecated, the documentation is bullshit
    """

    global dataset
    global DATA_PATH

    current_path = os.getcwd()
    DATA_PATH = os.path.join(current_path, 'data')

    try:
        if not os.path.exists(DATA_PATH):
            raise RuntimeError('data_path does not exists')

        dataset = pd.read_csv(
            os.path.join(DATA_PATH, "processed", "dataset.csv"))
    except Exception as e:
        sys.stderr.write(f'error during load ({startup_event.__name__}): {e}')
        sys.exit(1)


@app.get('/healthcheck')
def healthcheck():
    try:
        return {'len': len(dataset)}
    except NameError:
        raise HTTPException(status_code=500, detail="DataFrame no cargado")


@app.get('/data/by_department')
def by_department(
    name: str,
    page: int = 1,
    page_size: int = 1000,
    stream: bool = False
):
    if 'dataset' not in globals() or dataset.empty:
        raise HTTPException(status_code=500, detail="DataFrame not loaded")

    if not name:
        raise RuntimeError('?department_name is required')

    response = dataset[dataset['department'] == name]

    if not stream:
        total_items = len(response)
        start = (page - 1) * page_size
        end = start + page_size
        paginated_data = response.iloc[start:end]
        data = [row.to_dict() for _, row in paginated_data.iterrows()]

        return {
            'total_items': total_items,
            'page': page,
            'page_size': page_size,
            'data': json.dumps(data)
        }

    async def event_generator():
        data = [row.to_dict() for _, row in response.iterrows()]

        for row in data:
            yield json.dumps(row)

    return StreamingResponse(event_generator(), media_type="text/event-stream")


@app.get("/data/courthouse-count")
def courthouse_count(
    courthouse: str,
    min_date: date = None,
    max_date: date = None
) -> dict[str, list]:
    subdf = dataset.loc[
        dataset["NomCasaJusticia"] == courthouse,
        ["FechaSolicitud", "IdSolicitud"]
    ].reset_index(drop=True)

    subdf["FechaSolicitud"] = pd.to_datetime(subdf["FechaSolicitud"], format="%Y-%m-%d")
    subdf.index = subdf["IdSolicitud"]
    count_df = subdf.groupby(by="FechaSolicitud").count()
    count_df.rename(columns={"IdSolicitud": "Count"}, inplace=True)

    # Limit dates
    if min_date is not None:
        count_df = count_df.loc[count_df.index >= min_date.strftime("%Y-%m-%d")]
    if max_date is not None:
        count_df = count_df.loc[count_df.index <= max_date.strftime("%Y-%m-%d")]

    return {
        "FechaSolicitud": [ts.strftime('%Y-%m-%d') for ts in count_df.index],
        "Count": count_df["Count"].tolist()
    }


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
