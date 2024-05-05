import seaborn as sns
import matplotlib.pyplot as plt

# Calcular matriz de correlación
correlation_matzix = data.corr()

# Visualizar matriz de correlación
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matzix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de correlacion')
plt.show()