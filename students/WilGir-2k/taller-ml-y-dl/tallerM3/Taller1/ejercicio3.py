import pandas as pd
import matplotlib.pyplot as plt

# Configura Matplotlib para usar el backend 'Agg' para guardar archivos sin mostrar ventana
plt.switch_backend('agg')

# Cargar los datos
data = pd.read_csv('/mnt/c/Users/Willian_Steveen/ucc-repositorio/ucc-data-mining/data/chicago-Crimes-Map.csv')

# Visualización de datos: Histograma de Latitud
plt.hist(data['LATITUDE'], bins=20)  # Asegúrate de que 'LATITUDE' es el nombre correcto de la columna
plt.xlabel('Latitud')
plt.ylabel('Frecuencia')
plt.title('Histograma de Latitud')
plt.savefig('/mnt/c/Users/Willian_Steveen/ucc-repositorio/ucc-data-mining/students/WilGir-2k/taller-ml-y-dl/tallerM3/Taller1/latitud_histogram.png')
plt.close()  # Cierra la figura actual para evitar sobreposiciones

# Visualización de datos: Diagrama de dispersión entre Latitud y Longitud
plt.scatter(data['LATITUDE'], data['LONGITUDE'])  # Asegúrate de que 'LATITUDE' y 'LONGITUDE' son los nombres correctos de las columnas
plt.xlabel('Latitud')
plt.ylabel('Longitud')
plt.title('Diagrama de dispersión Latitud vs. Longitud')
plt.savefig('/mnt/c/Users/Willian_Steveen/ucc-repositorio/ucc-data-mining/students/WilGir-2k/taller-ml-y-dl/tallerM3/Taller1/latitud_longitud_dispersion.png')
plt.close()  # Cierra la figura

