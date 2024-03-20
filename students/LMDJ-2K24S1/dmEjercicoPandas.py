import pandas as pd

# cargar datos
data = pd.read_csv('./dataInput/Chicago_crimenes_map.csv')

# mostrsr las primeras filas
print(data.head())

print(data.info())

print (data.describe())


