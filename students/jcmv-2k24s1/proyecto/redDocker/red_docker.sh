# Crear la red
docker network create my_network

# Agregar contenedores a la red
docker network connect my_network jupyter-ml-proyecto
docker network connect my_network postgres-dm

# Validar contenedores en la red
docker network inspect my_network

