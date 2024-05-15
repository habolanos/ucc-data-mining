import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt



def printPandas(dataInput: pd.core.frame.DataFrame):
    
    print('--------------head------------')
    print(dataInput.head())

 
    print('--------------info------------')
    print(dataInput.info())

   
    print('--------------describe------------')
    print(dataInput.describe())
    


absolutepath = os.path.abspath(__file__)


fileDirectory = os.path.dirname(absolutepath)


pahtFile = fileDirectory +'/../dataInput/04.Chicago_Public_Schools_-_Progress_Report_Cards__2011-2012__20240312.csv'


data = pd.read_csv(pahtFile)
data_numeric = data.select_dtypes(include=[np.number])

correlation_matrix = data_numeric.corr()


plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de correlacion')
plt.show()