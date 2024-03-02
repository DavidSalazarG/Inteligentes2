import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

meses = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
ventas = np.array([20,25,30,35,40,45,50,55,60,65,70,75])

media_meses = np.mean(meses)
media_ventas = np.mean(ventas)

std = np.std(meses)
var = np.var(meses)
cov = np.cov(meses, ventas)

print("media meses: {}, media ventas: {}, std: {}, var: {}, cov".format(media_meses,media_ventas,std,var,cov))
print(cov)

b1, b0 =np.polyfit(meses, ventas, 1)
plt.scatter(meses, ventas, color = "Blue", label = "Datos")
plt.plot(meses, b1*meses+b0, color = "Red", label = "Regresion")
plt.legend