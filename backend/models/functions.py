"""
Para evitar repetir continuamente algunas secciones de código, se crearán funciones en este
archivo, para luego importarlas y aplicarlas.
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


# Función para llenar los espacios vacíos en los días de un dataframe

def create_continuos_time_series(df: pd.DataFrame) -> pd.DataFrame:
    """
    Esta función crea un arreglo con una fila por cada día entre la primera y última fecha de un
    dataframe, sin tener en cuenta los días sábados y domingos (En los que no abren las casas de justicia)

    Dicho arreglo contiene un conteo de los casos abiertos por día, en lugar de una fila por cada caso abierto.

    Como entrada se recibe un dataframe basado en 'backend/data/processed/unified_data.csv',
    por lo que se espera tener la columna 'FechaSolicitud'.
    """

    # Luego creamos el dataframe con solo los días laborales
    continuos_days = pd.date_range(start=df['FechaSolicitud'].min(), end=df['FechaSolicitud'].max(), freq='B')
    df_continuous_days = pd.DataFrame({'FechaSolicitud': continuos_days})

    # Unificamos los dataframes
    fulled_df = pd.merge(df_continuous_days, df, on='FechaSolicitud', how='left')

    # Rellenamos los valores faltantes con ceros
    fulled_df.fillna(0, inplace=True)

    # Agrupamos por fechas
    final_df = fulled_df.groupby('FechaSolicitud').size().reset_index(name='CantidadCasos')

    """
    En este punto existe un problema, y es que al realizar la unión de los dataframes hay
    al menos una fila por cada día, así que el valor más bajo de "Cantidad Casos" es 1.
    
    Aún así, por la forma en la que se realiza el merge de los dataframes, este aumento en 1
    solo sucede en las filas que tenía df_continuous_days y no el df original.
    
    Buscaremos las fechas de final_df que no están en el df original y enviaremos su cantidad
    de casos a 0
    
    """
    final_df.loc[~final_df['FechaSolicitud'].isin(df['FechaSolicitud']), 'CantidadCasos'] = 0

    return final_df
