import requests
import pandas as pd

# Definir los datos para la solicitud
data = {
    "DATE_OF_OCCURRENCE": "08/31/2023 07:00:00 PM",
    "BLOCK": "042XX W MARQUETTE RD",
    "IUCR": "0498",
    "LOCATION_DESCRIPTION": "APARTMENT",
    "ARREST": "Y",
    "DOMESTIC": "Y",
    "BEAT": 833,
    "WARD": 23
}

# Crear un DataFrame a partir de los datos
input_data = pd.DataFrame(data, index=[0])

# Realizar la solicitud POST
url = "http://localhost:8000/predict_crime/"
response = requests.post(url, json=input_data.to_dict(orient='records'))

# Verificar el estado de la respuesta
if response.status_code == 200:
    print("Solicitud exitosa:")
    print(response.json())
else:
    print("Error en la solicitud:")
    print(response.text)
