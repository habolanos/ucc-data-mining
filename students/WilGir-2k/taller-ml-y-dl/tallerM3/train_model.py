import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def clean_and_train_model(data_path):
    # Cargar los datos
    data = pd.read_csv(data_path)

    # Preprocesamiento de datos
    data = data.drop(columns=['CASE#', 'FBI CD', 'X COORDINATE', 'Y COORDINATE', 'LATITUDE', 'LONGITUDE', 'LOCATION'])

    # Dividir los datos en lotes más pequeños
    batch_size = 10000
    num_batches = len(data) // batch_size

    # Modelo inicializado fuera del bucle para ser guardado después de completar el entrenamiento
    final_model = RandomForestClassifier()

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

        # Dividir los datos en conjunto de entrenamiento y conjunto de prueba
        X_train, X_test, y_train, y_test = train_test_split(X_batch, y_batch, test_size=0.2, random_state=42)

        # Entrenar el modelo en cada lote
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        # Hacer predicciones en el conjunto de prueba y calcular la precisión
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy for batch {batch_idx}: {accuracy}")

        # Actualizar el modelo final con el modelo entrenado en el lote actual
        final_model = model

    # Guardar el modelo final entrenado
    joblib.dump(final_model, 'crime_prediction_model.pkl')

    return final_model

# Limpieza de datos y entrenamiento del modelo
trained_model = clean_and_train_model("data2.csv")
