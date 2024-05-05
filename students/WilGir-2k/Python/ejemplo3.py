import matplotlib.pyplot as plt

# Histograma de una variable
plt.hist(data['variable'], bins=20)
plt.xlabel('Variable')
plt.ylabel('Frecuencia')
plt.title('Histograma de variable')
plt.show()

# Diagrama de dispersion
plt.scatter(data['x'], data['y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Diagrama de dispersion')
plt.show()