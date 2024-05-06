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

# Carga de datos
data = pd.read_csv(pahtFile)
data_numeric = data.select_dtypes(include=[np.number])
# printPandas(data_numeric)

# Histograma de una variable
plt.hist(data['Safety Score'], bins=20)
plt.xlabel('Safety Score')
plt.ylabel('Frecuencia')
plt.title('Histograma de Safety Score')
plt.show()

# Diagrama de dispersion
plt.scatter(data['Average Student Attendance'],data['Average Teacher Attendance'])
plt.xlabel('Average Student Attendance')
plt.ylabel('Average Teacher Attendance')
plt.title('Diagrama de dispersion')
plt.show()