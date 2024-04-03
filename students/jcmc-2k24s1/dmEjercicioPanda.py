import pandas as pd 

# Cargar datos
data = pd.read_csv('./dataInput/CrimesMap.csv')

#mostrar las primeras filas 
print(data.head())

#obternet uinformacion
print(data.info())

print(data.describe())