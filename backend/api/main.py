from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse

import json
import pandas as pd
from datetime import date

import os
import sys

from api.utils import dpto_to_cod, mpio_to_cod, count
from api.schemas import Data

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    """
    I don't care that this is deprecated, the documentation is bullshit
    """

    global dataset
    global DATA_PATH
    global cods
    global courthouses

    current_path = os.getcwd()
    DATA_PATH = os.path.join(current_path, 'data')

    try:
        if not os.path.exists(DATA_PATH):
            raise RuntimeError('data_path does not exists')

        dataset = pd.read_csv(
            os.path.join(DATA_PATH, "processed", "dataset.csv")
        )
        dataset["FechaSolicitud"] = pd.to_datetime(dataset["FechaSolicitud"], format="%Y-%m-%d")

        with open(
            os.path.join(DATA_PATH, "processed", "dpts_cods_mpios.json"),
            mode="r",
            encoding="utf-8"
        ) as json_data:
            cods = json.load(json_data)

        with open(
            os.path.join(DATA_PATH, "processed", "depts_mpios.json"),
            mode="r",
            encoding="utf-8"
        ) as json_data:
            courthouses = json.load(json_data)

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

    cod_dpto = dpto_to_cod(name, cods)
    response = dataset.loc[dataset["COD_DPTO"] == cod_dpto]

    if not stream:
        total_items = len(response)
        start = (page - 1) * page_size
        end = start + page_size
        paginated_data = response.iloc[start:end]
        data = [row.to_dict() for _, row in paginated_data.iterrows()]
        for i in range(len(data)):
            data[i]["FechaSolicitud"] = data[i]["FechaSolicitud"].strftime('%Y-%m-%d')

        return {
            'total_items': total_items,
            'page': page,
            'page_size': page_size,
            'data': json.dumps(data)
        }

    async def event_generator():
        data = [row.to_dict() for _, row in response.iterrows()]
        for i in range(len(data)):
            data[i]["FechaSolicitud"] = data[i]["FechaSolicitud"].strftime('%Y-%m-%d')

        for row in data:
            yield json.dumps(row)

    return StreamingResponse(event_generator(), media_type="text/event-stream")


@app.get("/department")
def departments() -> list[str]:
    """
    Returns a list with all departments
    """
    return [x["department"] for x in courthouses]


@app.get("/courthouses")
def courthouses_department(department: str | None = None) -> list[str]:
    """
    Returns a list of courthouses. If department is None, then returns all
    courthouses, otherwise returns all courthouses in the given department
    """
    tmp = courthouses.copy()
    if department is not None:
        department = department.upper()
        tmp = [dic for dic in tmp if dic["department"] == department]

    out = []
    for dic in tmp:
        for courths in dic["municipalities"].values():
            if courths is None:
                continue
            out.extend([x["courthouse"] for x in courths])

    return out


@app.get("/data/courthouse-count")
def courthouse_count(
    courthouse: str,
    min_date: date = None,
    max_date: date = None
) -> Data:
    """
    Returns a count of requests in the given courthouse in an interval of time
    """
    subdf = dataset.loc[
        dataset["NomCasaJusticia"] == courthouse,
        ["FechaSolicitud", "IdSolicitud"]
    ].reset_index(drop=True)

    real_data = count(subdf, min_date, max_date)

    # Meanwhile returning this way
    return Data(real=real_data, predicted=None)


@app.get("/data/department-count")
def department_count(
        department: str,
        min_date: date = None,
        max_date: date = None
) -> Data:
    """
    Returns a count of requests in the given department in an interval of time
    """
    cod_dpto = dpto_to_cod(department, cods)
    subdf = dataset.loc[
        dataset["COD_DPTO"] == cod_dpto,
        ["FechaSolicitud", "IdSolicitud"]
    ].reset_index(drop=True)

    real_data = count(subdf, min_date, max_date)

    # Meanwhile returning this way
    return Data(real=real_data, predicted=None)


@app.get("/data/municipality-count")
def municipality_count(
    municipality: str,
    department: str,
    min_date: date = None,
    max_date: date = None
) -> Data:
    """
    Returns a count of requests in the given municipality in an interval of time
    """
    cod_dpto = dpto_to_cod(department, cods)
    cod_mpio = mpio_to_cod(municipality, department, cods)

    subdf = dataset.loc[
        (dataset["COD_DPTO"] == cod_dpto) & (dataset["COD_MPIO"] == cod_mpio),
        ["FechaSolicitud", "IdSolicitud"]
    ].reset_index(drop=True)

    real_data = count(subdf, min_date, max_date)

    # Meanwhile returning this way
    return Data(real=real_data, predicted=None)
