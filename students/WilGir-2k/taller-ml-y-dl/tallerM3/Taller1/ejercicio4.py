import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer

# Cargar los datos
data = pd.read_csv('/mnt/c/Users/Willian_Steveen/ucc-repositorio/ucc-data-mining/data/chicago-Crimes-Map.csv')

# Imputador para reemplazar NaN con la media de las columnas en X
imputer_X = SimpleImputer(strategy='mean')

# Seleccionar variables para el modelo y aplicar imputación en X
X = data[['LATITUDE', 'WARD']]
X = imputer_X.fit_transform(X)

# Imputador para reemplazar NaN en y
imputer_y = SimpleImputer(strategy='mean')
y = data['LONGITUDE']
y = imputer_y.fit_transform(y.values.reshape(-1, 1)).ravel()

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Predecir valores para el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el rendimiento del modelo
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)
