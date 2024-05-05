import requests

url = "http://localhost:8000/predict/"
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

response = requests.post(url, json=data)
print(response.json())
