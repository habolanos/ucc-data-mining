import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# importamos la data
data = pd.read_csv('./students/WilGir-2k/data/data.csv')

# Manejo de Valores faltantes
imputer = SimpleImputer(strategy='mean')
data_filled = imputer.fit_transform(data)

# Codificion de valiables categoricas
encoder = OneHotEncoder()
encoder_data = encoder.fit_transform(data[['categorical_column']])

# Normalizacion/escalado de caracteristicas
scaler = StandardScaler()
scaler_data = scaler.fit_transform(data)
# Imprimir el DataFrame resultante
print(data)