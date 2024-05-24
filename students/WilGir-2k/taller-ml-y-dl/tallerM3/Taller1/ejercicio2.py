import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('/mnt/c/Users/Willian_Steveen/ucc-repositorio/ucc-data-mining/data/chicago-Crimes-Map.csv')

# Seleccionar solo las columnas numéricas para la correlación
num_data = data.select_dtypes(include=['float64', 'int64'])

# Calcular la matriz de correlación
correlation_matrix = num_data.corr()

# Visualizar la matriz de correlación
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de correlación')

# Guardar la figura
plt.savefig('correlation_matrix.png')
plt.close()
