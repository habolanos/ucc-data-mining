from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Dividir datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Predecir valores
y_pred = model.predict(X_test)

# Evaluar rendimiento del modelo
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)