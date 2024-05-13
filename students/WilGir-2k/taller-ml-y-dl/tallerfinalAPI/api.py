from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import Optional

# Definir el modelo de datos de entrada
class InputData(BaseModel):
    NOMBRE: str
    PRECIONORMAL: int
    PRECIODESCUENTO: int
    DESCUENTO: str
    ENVIO: str
    CALIFICACION: str

# Cargar el modelo entrenado
model = joblib.load('model.pkl')

# Crear la aplicación FastAPI
app = FastAPI()

# Definir el endpoint para hacer predicciones
@app.post("/predict/")
async def predict(data: InputData):
    try:
        # Convertir los datos de entrada en un DataFrame
        input_data = pd.DataFrame([data.dict()])

        # Realizar la predicción
        prediction = model.predict(input_data)

        # Devolver la predicción
        return {"DESCUENTO_PREDICHO": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
