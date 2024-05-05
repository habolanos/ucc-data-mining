from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import Optional
from fastapi.security import OAuth2PasswordBearer

# Cargar el modelo entrenado
model = joblib.load('model.pkl')

# Definir la estructura de los datos de entrada
class InputData(BaseModel):
    NOMBRE_PC: str
    PRECIO_NORMAL: int
    PRECIO_DESCUENTO: int
    DESCUENTO: float
    ENVIO: str

# Crear la aplicación FastAPI
app = FastAPI()

# Secret key para firmar los tokens de acceso
SECRET_KEY = "your-secret-key"

# Generador de tokens de acceso
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Función para verificar la validez del token de acceso
def verify_token(token: str = Depends(oauth2_scheme)):
    # Aquí podrías implementar la lógica para verificar la validez del token
    # Por ejemplo, decodificar el token y verificar su firma
    # Si el token no es válido, puedes levantar una excepción HTTPException
    # Si el token es válido, puedes devolver los detalles del usuario
    return {"token": token}

# Definir la ruta para realizar predicciones (requiere autenticación)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
@app.post("/predict")
async def predict(data: InputData, token_data: dict = Depends(verify_token)):
    # Convertir los datos de entrada en un DataFrame
    input_data = pd.DataFrame([data.dict()])

    # Realizar la predicción
    prediction = model.predict(input_data)

    # Devolver la predicción
    return {"prediction": prediction[0]}
