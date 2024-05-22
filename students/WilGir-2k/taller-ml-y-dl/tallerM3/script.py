import requests

url = "http://localhost:8000/predict_crime/"
data = {
    "DATE OF OCCURRENCE": "08/31/2023 07:00:00 PM",
    "BLOCK": "042XX W MARQUETTE RD",
    "IUCR": "0498",
    "LOCATION DESCRIPTION": "APARTMENT",
    "ARREST": "Y",
    "DOMESTIC": "Y",
    "BEAT": 833,
    "WARD": 23
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.json())




curl -X 'POST' \
  'http://localhost:8000/predict_crime/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "DATE_OF_OCCURRENCE": "08/31/2023 07:00:00 PM",
    "BLOCK": "042XX W MARQUETTE RD",
    "IUCR": "0498",
    "LOCATION_DESCRIPTION": "APARTMENT",
    "ARREST": "Y",
    "DOMESTIC": "Y",
    "BEAT": 833,
    "WARD": 23
}'
