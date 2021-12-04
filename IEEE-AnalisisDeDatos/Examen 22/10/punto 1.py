import matplotlib.pyplot as plt
import numpy as np

mu = [0, 0]                          # Valores medios de x e y
cxy = [[1, 1], [1, 2]]               # Matriz de covarianza, [[Cxx, Cxy], [Cyx, Cyy]]
x, y = np.random.multivariate_normal(mu, cxy, 5000).T


mu2 = [0, 0]                          # Valores medios de x e y
cxy2 = [[1, 1], [1, 2]]               # Matriz de covarianza, [[Cxx, Cxy], [Cyx, Cyy]]
x2, y2 = np.random.multivariate_normal(mu2, cxy2, 5000).T

plt.subplot(1,2,1)
plt.title('Original')
plt.scatter(x, y, s=5, alpha=0.5)

plt.subplot(1,2,2)
plt.title('modificado')
plt.scatter(x2, y2, s=(10 * np.random.rand(5000))**2, alpha=0.5)
plt.show()