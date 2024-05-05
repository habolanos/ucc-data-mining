from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
# Paso 1: Cargar el modelo entrenado
model = joblib.load('crime_prediction_model.pkl')
# Paso 2: Definir los modelos de datos para la entrada y salida de la API
class CrimePredictionInput(BaseModel):
 DATE_OF_OCCURRENCE: str
 BLOCK: str
 IUCR: str
 LOCATION_DESCRIPTION: str
 ARREST: str
 DOMESTIC: str
 BEAT: int
 WARD: int
class CrimePredictionOutput(BaseModel):
 PRIMARY_DESCRIPTION: str
# Paso 3: Inicializar la aplicación FastAPI
app = FastAPI()
# Paso 4: Definir el endpoint para hacer predicciones de crimen
@app.post('/students/WilGir-2k/taller-ml-y-dl/taller 1/')
async def predict_crime(data: CrimePredictionInput):
 # Convertir los datos de entrada en un DataFrame
 input_data = pd.DataFrame([data.dict()])
 # Preprocesar los datos de entrada
 input_data = pd.get_dummies(input_data)
 # Asegurarse de que todas las columnas necesarias estén presentes
 required_columns = set(X.columns)
 missing_columns = required_columns - set(input_data.columns)
 for column in missing_columns: input_data[column] = 0
 # Hacer la predicción
 prediction = model.predict(input_data)
 # Obtener la descripción primaria del crimen predicho
 primary_description = prediction[0]
 return CrimePredictionOutput(PRIMARY_DESCRIPTION=primary_description)