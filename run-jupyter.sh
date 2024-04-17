NAME_CONTAINER=jupyter-ml
PATH_VOLUMEN=~/repos-ucc/ucc-data-mining/taller-ml-y-dl
PORT_EXTERNO=8888
docker container run -it --name $NAME_CONTAINER --rm -p $PORT_EXTERNO:8888 -v $PATH_VOLUMEN:/home/jovyan/work jupyter/base-notebook:lastest