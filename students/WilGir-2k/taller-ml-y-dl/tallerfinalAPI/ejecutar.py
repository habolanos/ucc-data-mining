import joblib
import pandas as pd

# Cargar el modelo entrenado
model = joblib.load('model.pkl')

# Datos de entrada para la predicción
input_data = {
    "NOMBRE": "Torre Gamer Amd Ryzen 5 00g +gb Ram +ssd 240 Radeon Pc",
    "PRECIONORMAL": 1900000,
    "PRECIODESCUENTO": 1539000,
    "DESCUENTO": 19,
    "ENVIO": "Envio gratis",
    "CALIFICACION": 4
}

# Crear un DataFrame con los datos de entrada
input_df = pd.DataFrame([input_data])

# Eliminar caracteres no numéricos y convertir a flotante
input_df['NOMBRE'] = input_df['NOMBRE'].str.replace(r'\D', '', regex=True).astype(float)

# Eliminar la columna 'ENVIO' si es categórica
if 'ENVIO' in input_df.columns:
    input_df.drop('ENVIO', axis=1, inplace=True)

# Realizar la predicción
prediction = model.predict(input_df)

print("Predicción de calificación:", prediction)