import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Cargar datos
data = pd.read_csv('/mnt/c/Users/Willian_Steveen/ucc-repositorio/ucc-data-mining/data/chicago-Crimes-Map.csv')

# Manejo de valores faltantes
imputer = SimpleImputer(strategy='mean')
num_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[num_columns] = imputer.fit_transform(data[num_columns])

# Codificación de variables categóricas
encoder = OneHotEncoder()
encoded_data = pd.DataFrame(encoder.fit_transform(data[['PRIMARY DESCRIPTION']]).toarray(),
                            columns=encoder.get_feature_names_out(['PRIMARY DESCRIPTION']))

# Concatenar datos codificados de nuevo al DataFrame principal
data = pd.concat([data.drop(['PRIMARY DESCRIPTION'], axis=1), encoded_data], axis=1)

# Normalización/escalado de características
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data.select_dtypes(include=['float64', 'int64']))
scaled_data = pd.DataFrame(scaled_data, columns=data.select_dtypes(include=['float64', 'int64']).columns)

# Resultado
print(scaled_data.head())
