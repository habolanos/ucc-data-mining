import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
data = pd.read_csv('data.csv')
# Mostrar las primeras filas de los datos
print(data.head())
# Descripción estadística de los datos numéricos
print(data.describe())
# Distribución de características categóricas
categorical_columns = ['PRIMARY DESCRIPTION','SECONDARY DESCRIPTION','LOCATION DESCRIPTION']
for col in categorical_columns:
 print(f"Distribución de {col}:")
 print(data[col].value_counts())
# Histograma de las características numéricas
data.hist(figsize=(10, 8))
plt.show()
# Mapa de calor de la correlación
corr_matrix = data.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()