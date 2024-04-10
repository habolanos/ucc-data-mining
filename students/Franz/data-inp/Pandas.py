import pandas as pd

#cargar datos
data= pd.read_csv('repos_ucc/ucc-data-mining/data-inp/chicagoCrimes-Map.csv')

#msotrar las primeras filas

print(data.head());
print(data.info());
print(data.describe());