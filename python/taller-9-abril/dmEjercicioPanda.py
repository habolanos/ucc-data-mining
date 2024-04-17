import pandas as pd

# Cargar datos
data = pd.read_csv('../../data/chicago-Crimes-Map.csv')

# Mostrar las primeras filas
print("-----------------------HEAD-----------------------")
print(data.head())
print("-----------------------INFO-----------------------")
print(data.info())
print("-----------------------DESC-----------------------")
print(data.describe())