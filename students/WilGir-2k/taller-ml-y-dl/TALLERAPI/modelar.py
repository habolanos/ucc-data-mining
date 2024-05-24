import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Cargar los datos
data = pd.read_csv('data3.csv', encoding='utf-8')

# Ver las primeras filas del dataframe
print(data.head())

# Eliminar columnas no necesarias
data = data.drop(columns=['ESTACION', 'TIEMPO', 'HORAMEDICION', 'ID'])

# Codificar las variables categóricas (si hay alguna que necesite codificación)
data = pd.get_dummies(data)

# Dividir los datos en características (X) y etiquetas (y)
X = data.drop('AIRETEMPERATURA', axis=1)
y = data['AIRETEMPERATURA']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Predicciones y evaluación del modelo
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Modelo creado:", mse)

# Guardar el modelo entrenado
joblib.dump(model, 'temperature_prediction_model.pkl')
