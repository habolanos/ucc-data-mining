## Crear entorno vitual
python3 -m venv scrapy
## Activar entorno virtual
source scrapy/bin/activate
# Instalar lib
pip install scrapy
# Creamos carpeta
mkdri scrapy
cd scrapy/
# Creamos el proyecto
scrapy startproject festivos
cd festivos/
# Creamos myspider con la configuracion base
scrapy genspider myspider www.festivos.com.co/historico
# Corremos el spyder
scrapy crawl myspider
# Desactivamos el env
deactivate