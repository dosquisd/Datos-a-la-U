from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import pandas as pd
import os
import uvicorn
import sys
import json

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    """
    I don't care that this is deprecated, the documentation is bullshit
    """

    global proceso_casas_justicia
    global DATA_PATH

    current_path = os.getcwd()
    DATA_PATH = os.path.join(current_path, 'data')

    try:
        if not os.path.exists(DATA_PATH):
            raise RuntimeError('data_path does not exists')

        proceso_casas_justicia = pd.read_csv(
            os.path.join(DATA_PATH, "processed", "Procesos_casas_de_justicia.csv"))
    except Exception as e:
        sys.stderr.write(f'error during load ({startup_event.__name__}): {e}')
        sys.exit(1)


@app.get('/healthcheck')
def healthcheck():
    try:
        return {'len': len(proceso_casas_justicia)}
    except NameError:
        raise HTTPException(status_code=500, detail="DataFrame no cargado")


@app.get('/data/by_department')
def by_department(
    name: str,
    page: int = 1,
    page_size: int = 1000,
    stream: bool = False
):
    if 'proceso_casas_justicia' not in globals() or proceso_casas_justicia.empty:
        raise HTTPException(status_code=500, detail="DataFrame not loaded")

    if not name:
        raise RuntimeError('?department_name is required')

    response = proceso_casas_justicia[proceso_casas_justicia['department'] == name]

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


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
