import pandas as pd
import numpy as np
import os

# pip install -U scikit-learn
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def printPandas(dataInput: pd.core.frame.DataFrame):
    # Mostrar las primeras filas
    print('--------------head------------')
    print(dataInput.head())

    # Obtener infromacion sobre los datos
    print('--------------info------------')
    print(dataInput.info())

    # Resumen estadistico de los datos
    print('--------------describe------------')
    print(dataInput.describe())
    

# Obtener ruta relativa del archivo
absolutepath = os.path.abspath(__file__)

# Obtener la ruta del directorio del archivo<
fileDirectory = os.path.dirname(absolutepath)

# Se obtiene la ruta del archivo a leer
pahtFile = fileDirectory +'/../../WilGir-2k/TallerPython3/Chicago_Public_Schools_-_Progress_Report_Cards__2011-2012__20240312.csv'

# Carga de datos
data = pd.read_csv(pahtFile)

## Creamos una nueva data donde solo utilice columnas numericas
# Seleccionar solo las columnas numéricas
data_numeric = data.select_dtypes(include=[np.number])
# printPandas(data_numeric)

## Manejo de valores faltantes
imputer = SimpleImputer(strategy='mean')
data_filled = imputer.fit_transform(data_numeric)

## Codificacion de variables categoricas
encoder = OneHotEncoder()
encoded_data = encoder.fit_transform(data[['Average Student Attendance']])

## Normalizacion/escalado de caracteristica
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data_numeric)
print(scaled_data)