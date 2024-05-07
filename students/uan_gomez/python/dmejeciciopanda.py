import pandas as pd
import os

# Obtener ruta relativa del archivo
absolutepath = os.path.abspath(__file__)

# Obtener la ruta del directorio del archivo<
fileDirectory = os.path.dirname(absolutepath)

# Se obtiene la ruta del archivo a leer
pahtFile = fileDirectory +'/../dataInput/CrimesMap.csv'
# Carga de datos
data = pd.read_csv(pahtFile)

# Mostrar las primeras filas
print(data.head())

# Obtener infromacion sobre los datos
print(data.info())

# Resumen estadistico de los datos
print(data.describe())