# Backend

## Estructura

```bash
.
├── api  # Desarrollo de la API
│   ├── main.py
│   └── utils.py
├── data  # Datos utilizados
│   ├── depts_municipalities_cods.ipynb
│   ├── directorio_casas_de_justicia.ipynb
│   ├── merge_dataset.ipynb
│   ├── procesos_casas_de_justicia.ipynb
│   ├── processed  # Datos después de ser tratados
│   │   ├── cods_dptos_mpios.json
│   │   ├── dataset.csv
│   │   ├── depts_mpios.json
│   │   ├── directorio_casas_de_justicia.csv
│   │   ├── dpts_cods_mpios.json
│   │   ├── Procesos_casas_de_justicia.csv
│   │   ├── unified_data.csv
│   │   └── vulnrb.csv
│   ├── raw  # Datos descargados directamente de fuentes oficiales
│   │   ├── Caracterizaci_n_de_Personas_en_Casas_de_Justicia_20241103.csv
│   │   ├── Directorio_de_Casas_de_Justicia_y_Centros_de_Convivencia_Ciudadana._20241103.csv
│   │   ├── Procesos_en_Casas_de_Justicia_20241103.csv
│   │   ├── Tabla-Códigos-Dane.pdf
│   │   ├── VULNRB_IPMxMZ.cpg
│   │   ├── VULNRB_IPMxMZ.dbf
│   │   ├── VULNRB_IPMxMZ.prj
│   │   ├── VULNRB_IPMxMZ.shp
│   │   ├── VULNRB_IPMxMZ.shx
│   │   └── VULNRB_IPMxMZ.zip
│   ├── README.md
│   └── vulnrb.ipynb
├── models  # Modelos de IA
│   ├── departments_lstm.ipynb
│   └── functions.py
├── README.md
└── requirements.txt  # Lista de requerimientos necesarios para ejecutar backend
```

## API

Dentro de [api](./api/) es donde se encuentra desarrollada la API con la cual se comunica el Frontend con todos los datos. Para la creación de la API se utilizó el framework de FastAPI, debido a la sencillez que provee, además de la vasta documentación existente.

### Ejecutar API

Para poder ejecutar la API se deben ejecutar los siguientes comandos desde consola

```bash
$cd backend
backend$python3 -m venv .venv  # [Opcional] Crear entorno virtual
backend$pip install -r requirements.txt
backend$uvicorn api.app:app
```

Demás configuraciones extras, como el puerto, host, reload, se pueden agregar sin problemas, teniendo en cuenta la documentación de uvicorn.

## Data

Dentro de [data](./data/) se podrán encontrar dos carpetas llamadas: [raw](./data/raw/), es donde están los datos descargados por las fuentes oficiales; [processed](./data/processed/), es donde están los datos procesados a raíz de los datos crudos; además de diferentes notebooks donde se encontrará el código que se utilizó para tratar los datos.

Como extra, en el README dentro de [data](./data/) ([aquí](./data/README.md)), están los links directos de donde se extrayeron todos los datos.

## Models

Dentro de [models](./models/) están los modelos de IA que se desarrollaron, además de los notebooks y funciones necesarias para su desarrollo
