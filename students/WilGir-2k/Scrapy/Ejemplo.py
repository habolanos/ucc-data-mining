
import requests
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd

r = requests.get('https://listado.mercadolibre.com.co/computador-portatil-gamer-i7#D[A:computador%20portatil%20gamer%20i7]')
soup = BeautifulSoup(r.content, 'html.parser')

titulos = soup.find_all('h2', attrs={"class": "ui-search-item__title"})

titulos = [i.text for i in titulos]


precio = soup.find_all('span', attrs = {"class":"andes-money-amount__fraction"} )
precio = [i.text for i in precio]


df = pd.DataFrame({"titulo":titulos,"precios":precio})
df.to_csv('productos.csv')

