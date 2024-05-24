from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Cargar el modelo entrenado
model = joblib.load('temperature_prediction_model.pkl')

# Definir los modelos de datos para la entrada y salida de la API
class TemperaturePredictionInput(BaseModel):
    BULBOTEMPERATURA: float
    HUMEDAD: int
    INTECIDADLLUVIA: float
    INTERVALOLLUVIA: float
    LLUVIATOTAL: float
    PRECICION: float
    DIRECIONVIENTO: int
    VELOCIDADVIENTO: int
    VELOCIDADMAXIMA: int
    BAROMETRICA: int
    RADIACIONSOLAR: int
    RUMBO: int
    BATERIA: int

class TemperaturePredictionOutput(BaseModel):
    AIRETEMPERATURA: float
    

# Inicializar la aplicación FastAPI
app = FastAPI()

# Definir el endpoint para hacer predicciones de temperatura
@app.post('/predict/', response_model=TemperaturePredictionOutput)
async def predict_temperature(data: TemperaturePredictionInput):
    # Convertir los datos de entrada en un DataFrame
    input_data = pd.DataFrame([data.dict()])
    
    # Preprocesar los datos de entrada, si es necesario agregar dummy variables
    input_data = pd.get_dummies(input_data)
    
    # Asegurarse de que todas las columnas necesarias estén presentes
    required_columns = model.feature_names_in_
    for column in required_columns:
        if column not in input_data.columns:
            input_data[column] = 0

    # Hacer la predicción
    prediction = model.predict(input_data)

    # Obtener la temperatura del aire predicha
    aire_temperatura = prediction[0]
    
    return TemperaturePredictionOutput(AIRETEMPERATURA=aire_temperatura)
