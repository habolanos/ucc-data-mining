import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

# pip install -U scikit-learn

def printPandas(dataInput: pd.core.frame.DataFrame):
    # Mostrar las primeras filas
    print('--------------head------------')
    print(dataInput.head())

    # Obtener infromacion sobre los datos
    print('--------------info------------')
    print(dataInput.info())

    # Resumen estadistico de los datos
    print('--------------describe------------')
    print(dataInput.describe())
    

# Obtener ruta relativa del archivo
absolutepath = os.path.abspath(__file__)

# Obtener la ruta del directorio del archivo<
fileDirectory = os.path.dirname(absolutepath)

# Se obtiene la ruta del archivo a leer
pahtFile = fileDirectory +'/../../WilGir-2k/TallerPython3/Chicago_Public_Schools_-_Progress_Report_Cards__2011-2012__20240312.csv'


# Carga de datos
data = pd.read_csv(pahtFile)
data_numeric = data.select_dtypes(include=[np.number])
# printPandas(data_numeric)

# Histograma de una variable
plt.hist(data['Safety Score'], bins=20)
plt.xlabel('Safety Score')
plt.ylabel('Frecuencia')
plt.title('Histograma de Safety Score')
plt.show()

# Diagrama de dispersion
plt.scatter(data['Average Student Attendance'],data['Average Teacher Attendance'])
plt.xlabel('Average Student Attendance')
plt.ylabel('Average Teacher Attendance')
plt.title('Diagrama de dispersion')
plt.show()