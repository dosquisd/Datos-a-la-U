""""
Para evitar repetir continuamente algunas secciones de código, se crearán funciones en este
archivo, para luego importalas y aplicarlas.
"""

import numpy as np
import pandas as pd
from typing import Dict


# Función para la creación de subdatasets

def divide_dataframe(df: pd.DataFrame, column: str) -> Dict:
    """
    Esta función divide un datasets en función de los valores de una de sus columnas,
    para luego retornar un diccionaro que contiene dichos valores como claves y el resto
    de las columnas como valores.

    Si bien es una única línea de código, puede dificultar la legibilidad posterior de los
    notebooks, por lo que preferí utilizar una función que sea bastante más clara. Esto es, a
    la larga, más beneficioso para el equipo.
    """
    datasets: Dict[str, pd.DataFrame] = {str(valor): datos for valor, datos in df.groupby(column)}
    return datasets


# Función para comprobar que el dataframe mayor y los subdatasets tienen la misma cantidad de elementos

def compare_rows(df: pd.DataFrame, dfs: Dict) -> bool:

    dfRows = df.shape[0]
    dfsRows = 0

    for dataframe in dfs.values():
        dfsRows += dataframe.shape[0]

    print(f"({dfRows}, {dfsRows})")

    return True if dfRows == dfsRows else False
