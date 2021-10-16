import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.tools.datetimes import to_datetime

tabla = pd.read_csv('BTC.csv' )
tabla.index = pd.to_datetime(tabla['Date'])


y = tabla['Adj Close']
x = tabla.index
maximo = y.max()   #Adj Close =  19497.4
# print(maximo)
plt.plot( x ,y )
plt.plot( x[ y == maximo] , maximo , 'r*' , label = 'Maximo')
plt.xticks(rotation=90)
plt.title('Bitcoin')
plt.legend() #Para que muestre las etiquetas
plt.show()
# print(tabla['Date'])

print(tabla.tail(20))