from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pandas as pd

# Cargar datos
data = pd.read_csv('../../data/dataFromWeb-ciudades.csv')

# Manejo de valores faltantes
#imputer = SimpleImputer(strategy='mean')
#data_filled = imputer.fit_transform(data)

# Codificación de variables categóricas
#encoder = OneHotEncoder()
#encoded_data = encoder.fit_transform(data[['WARD']])

# Normalización/escalado de características
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
