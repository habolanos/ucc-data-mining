import requests

# URL de la API
url = 'http://127.0.0.1:8000/predict'

# Datos de entrada para la predicción
data = {
    "ESTACION": "63rd Street Weather Station",
    "TIEMPO": "1/01/2016 12:00:00 a. m.",
    "AIRETEMPERATURA": -28,
    "BULBOTEMPERATURA": -44,
    "HUMEDAD": 69,
    "INTECIDADLLUVIA": 0,
    "INTERVALOLLUVIA": 0,
    "LLUVIATOTAL": 67,
    "PRECICION": 0,
    "DIRECIONVIENTO": 255,
    "VELOCIDADVIENTO": 38,
    "VELOCIDADMAXIMA": 64,
    "BAROMETRICA": 10005,
    "RADIACIONSOLAR": 5,
    "RUMBO": 353,
    "BATERIA": 119,
    "HORAMEDICION": "1/01/2016 12:00:00 a. m.",
    "ID": "63rdStreetWeatherStation201601012400"
}

# Enviar la solicitud POST con los datos en el cuerpo
response = requests.post(url, json=data)

# Obtener la respuesta con la predicción
if response.status_code == 200:
    result = response.json()
    print('Predicción:', result)
else:
    print('Error al enviar la solicitud:', response.text)
