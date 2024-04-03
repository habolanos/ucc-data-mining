import pandas as pd 

#cargar datos
data = pd.read_csv('./data/Crimes_Crimenes_Map.csv')

# mostrar las primeras filas 

print(data.head())

print (data.info())

print (data.describe())



