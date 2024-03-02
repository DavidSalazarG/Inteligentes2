import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

dias = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1) #reshape transpone el arreglo en una columna
altura_planta = np.array([2,5,9,15,23,34,45,55,67,80])
caracteristicas = PolynomialFeatures(degree=2)
polinomio_dias = caracteristicas.fit_transform(dias)
modelo = LinearRegression()
modelo.fit(polinomio_dias, altura_planta)

#Se genera este umbral de incertidumbre para poder calcular el valor de la metrica, 
#por cuanto porcentaje el modelo es preciso o no
dias_pred = np.linspace(0, 10, 100).reshape(-1,1)

#polinomio para los datos de dias_pred
polinomio_dias_pred = caracteristicas.fit_transform(dias_pred)

#ahora se debe predecir con el modelo anteriormente construido
modelo.predict(polinomio_dias_pred, altura_planta)

altura_pred = modelo.predict(polinomio_dias_pred, altura_planta)
#ahora se grafíca
plt.scatter(dias, altura_planta, color = "Blue", label = "Días")
plt.plot(polinomio_dias_pred, al)