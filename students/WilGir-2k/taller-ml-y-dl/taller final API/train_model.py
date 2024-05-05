import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor  # Importa RandomForestRegressor en lugar de RandomForestClassifier
from sklearn.impute import SimpleImputer
import joblib

# Cargar los datos desde el archivo CSV
data = pd.read_csv('data.csv')

# Eliminar filas con valores faltantes si es necesario
data.dropna(inplace=True)

# Eliminar el "%" y otros caracteres no numéricos de la columna 'DESCUENTO'
data['DESCUENTO'] = data['DESCUENTO'].str.replace(r'\D', '', regex=True)

# Convertir la columna 'DESCUENTO' a tipo flotante
data['DESCUENTO'] = data['DESCUENTO'].astype(float)

# Convertir la calificación a un valor numérico
data['CALIFICACION'] = data['CALIFICACION'].str.extract(r'(\d+\.\d+)')
data['CALIFICACION'] = data['CALIFICACION'].astype(float)

# Codificar las variables categóricas si es necesario
data = pd.get_dummies(data)

# Dividir los datos en características (X) y etiquetas (y)
X = data.drop(columns=['CALIFICACION'])
y = data['CALIFICACION']

# Usar SimpleImputer para manejar valores faltantes en y
imputer = SimpleImputer(strategy='mean')
y = imputer.fit_transform(y.values.reshape(-1, 1)).ravel()

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model = RandomForestRegressor()  # Cambia a RandomForestRegressor
model.fit(X_train, y_train)

# Evaluar el modelo
score = model.score(X_test, y_test)
print("Score:", score)

# Guardar el modelo entrenado
joblib.dump(model, 'model.pkl')

