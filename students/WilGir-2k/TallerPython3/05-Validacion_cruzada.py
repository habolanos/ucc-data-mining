import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

# pip install -U scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

from sklearn.model_selection import cross_val_score


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

# Filtrar filas con valores NaN en 'Average Student Attendance' o 'Average Teacher Attendance'
data_clean = data.dropna(subset=['Average Student Attendance', 'Average Teacher Attendance'])

# Dividir datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data_clean[['Average Student Attendance']], data_clean['Average Teacher Attendance'], test_size=0.2, random_state=42)

# Imputar valores faltantes con la media
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

model = LinearRegression()
model.fit(X_train_imputed, y_train)

# Aplicar Validacion cruzada
scores = cross_val_score(model, data_clean[['Average Student Attendance']], data_clean['Average Teacher Attendance'], cv=5)
print('Cross-validated scores:', scores)
print('Mean score:', scores.mean())