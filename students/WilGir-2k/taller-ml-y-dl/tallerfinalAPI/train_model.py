import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
import joblib

# Cargar los datos desde el archivo CSV
data = pd.read_csv('data.csv')

# Eliminar filas con valores faltantes si es necesario
data.dropna(inplace=True)

# Codificar las variables categóricas
data = pd.get_dummies(data, columns=['NOMBRE', 'ENVIO'])

# Dividir los datos en características (X) y etiquetas (y)
X = data.drop(columns=['CALIFICACION'])
y = data['CALIFICACION']

# Usar SimpleImputer para manejar valores faltantes en X
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Evaluar el modelo
score = model.score(X_test, y_test)
print("Score:", score)

# Guardar el modelo entrenado
joblib.dump(model, 'model.pkl')
