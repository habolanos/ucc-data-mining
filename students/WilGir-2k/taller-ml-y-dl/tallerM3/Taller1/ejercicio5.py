import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error

# Cargar los datos
data = pd.read_csv('/mnt/c/Users/Willian_Steveen/ucc-repositorio/ucc-data-mining/data/chicago-Crimes-Map.csv')

# Imputadores para reemplazar NaN
imputer_X = SimpleImputer(strategy='mean')
imputer_y = SimpleImputer(strategy='mean')

# Seleccionar variables para el modelo
X = data[['LATITUDE', 'WARD']]
y = data['LONGITUDE']

# Aplicar la imputación
X = imputer_X.fit_transform(X)
y = imputer_y.fit_transform(y.values.reshape(-1, 1)).ravel()

# Inicializar el modelo de regresión lineal
model = LinearRegression()

# Aplicar validación cruzada
scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')  # Usamos el negativo del MSE

# Imprimir los resultados de la validación cruzada
print('Cross-validated scores:', -scores)  # Convertimos a positivo para interpretación
print('Mean score:', -scores.mean())
