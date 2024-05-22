import requests

# URL de tu API FastAPI
url = "http://127.0.0.1:8889/predict"

# Token de acceso obtenido después de la autenticación
token = "tu-token-de-acceso"

# Datos de ejemplo para enviar a la API
data = {
  "NOMBR _PC": "Torre Gamer Amd Ryzen 5 5600g +16gb Ram +ssd 240 Radeon 7 Pc",
  "PREC O_NORMAL": 1900000,
  "PRE IO_DESCUENTO": 1539000,
  "DESCUENTO": 19,
  "ENVIO": "Envio gratis"
}


# Enviar una solicitud POST a la API con el token de acceso
response = requests.post(url, json=data, headers={"Authorization": f"Bearer {token}"})

# Imprimir la respuesta
print(response.status_code)
print(response.json())

