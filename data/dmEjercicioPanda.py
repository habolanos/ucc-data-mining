import pandas as pd

#carga de datos
data=pd.read_csv('/mnt/c/ucc-repos/ucc-data-mining/data/Crimes_-_Map.csv')

#mostrar las primeras filas
print(data.head())

# obtener informacion sobre los datos 
print(data.info())

print(data.describe())