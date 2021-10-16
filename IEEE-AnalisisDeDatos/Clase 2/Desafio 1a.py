    # Gráficar en el intervalo de [-1, 1] la función valor absoluto. Elegir una cantidad apropiada de puntos de acuerdo a su criterio.

    # Tip: Usar la funcion np.absolute de numpy.

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-1 , 1 , 50 )
plt.plot(X , np.absolute(X))
plt.show()