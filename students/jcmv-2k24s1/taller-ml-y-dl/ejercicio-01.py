import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
data = pd.read_csv('data.csv')

# Mostrar las primeras filas 
print(data.head())

# Descripcion estadistica de los datos numericos
print(data.describe())

print(data.info())

# Distribucion de caracteristicas categoria
categoria_columns = ['PRIMARY DESCRIPTION','SECONDARY DESCRIPTION','LOCATION DESCRIPTION']
for col in categoria_columns:
    print(f"Distribucion de {col}")
    print(data[col].value_counts())

# Histograma de las caractersticas numericas
data.hist(figsize=(10,8))
# plt.show()

