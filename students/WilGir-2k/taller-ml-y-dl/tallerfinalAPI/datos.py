import pandas as pd

# Cargar los datos desde el archivo CSV
data = pd.read_csv('data.csv')

# Imprimir la información del DataFrame
print(data.info())
