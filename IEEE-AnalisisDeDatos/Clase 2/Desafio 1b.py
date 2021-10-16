    # Gráficar en el intervalo de [-5, 5] una función gaussiana definida como:

    # f(x)=e−x2/2
    # es una campana de Gauss
    # Tip: Usar la funcion np.exp de numpy.

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-5 , 5 , 150 )
plt.plot( X , np.exp( -X**2/2) )
plt.show()