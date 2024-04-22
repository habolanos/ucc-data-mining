import pandas as pd 
import os
#cargar datos
data = pd.read_csv('./students/WilGir-2k/data/Crimes_Crimenes_Map.csv')

# mostrar las primeras filas 

print(data.head())

print (data.info())

print (data.describe())



