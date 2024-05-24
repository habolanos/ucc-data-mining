curl -X 'POST' \
  'http://localhost:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
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
  "BATERIA": 119
}'


# uvicorn api:app --reload
