import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Paso 1: Cargar los datos
data = pd.read_csv('data.csv')

# Paso 2: Preprocesamiento de datos
# Eliminar columnas innecesarias o que no sean útiles para la predicción
data = data.drop(columns=['CASE#', 'FBI CD', 'X COORDINATE', 'Y COORDINATE', 'LATITUDE',
                         'LONGITUDE', 'LOCATION'])

# Dividir los datos en lotes más pequeños
batch_size = 10000
num_batches = len(data) // batch_size
for batch_idx in range(num_batches):
    batch_data = data.iloc[batch_idx * batch_size:(batch_idx + 1) * batch_size]
    
    # Guardar la columna "PRIMARY DESCRIPTION"
    y_batch = batch_data['PRIMARY DESCRIPTION']
    
    # Aplicar pd.get_dummies() a batch_data
    batch_data = pd.get_dummies(batch_data)
    
    # Concatenar la columna "PRIMARY DESCRIPTION" con el DataFrame resultante de pd.get_dummies()
    batch_data = pd.concat([batch_data, y_batch], axis=1)
    
    # Dividir los datos en características (X) y etiquetas (y) para cada lote
    X_batch = batch_data.drop(columns=['PRIMARY DESCRIPTION'])
    y_batch = batch_data['PRIMARY DESCRIPTION']
    
    # Entrenar y evaluar el modelo en cada lote
    X_train, X_test, y_train, y_test = train_test_split(X_batch, y_batch, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy for batch {batch_idx}: {accuracy}")

# Guardar el modelo entrenado
joblib.dump(model, 'crime_prediction_model.pkl')
