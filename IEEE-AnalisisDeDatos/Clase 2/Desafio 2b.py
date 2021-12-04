from numpy.core.numeric import roll
import pandas as pd
import matplotlib.pyplot as plt

Amazon = pd.read_csv('AMZN.csv' , index_col='Date')
Google = pd.read_csv('GOOGLE.csv', index_col='Date')
tablaDeTrabajo = pd.merge(Amazon['Adj Close'], Google['Adj Close'], on='Date' , suffixes=('Amz', 'Goo'))
tablaDeTrabajo = tablaDeTrabajo.rename(columns={'Adj CloseAmz' : 'Amazon', 'Adj CloseGoo' : 'Google'})
tablaDeTrabajo['Promedio'] = (round( tablaDeTrabajo['Amazon'] / tablaDeTrabajo['Google'], ndigits=2))
tablaDeTrabajo.index = pd.to_datetime(tablaDeTrabajo.index)
# print(Amazon.head())
# print(Google.head())
# print(tablaDeTrabajo.index)
# print(tablaDeTrabajo.head())
# print(tablaDeTrabajo.loc[ (tablaDeTrabajo['Promedio'] == 1.00)])

plt.plot(tablaDeTrabajo.index , tablaDeTrabajo['Amazon'], 'r' , label = 'Amazon')
plt.plot(tablaDeTrabajo.index , tablaDeTrabajo['Google'], 'b' , label = 'Google')
plt.plot( tablaDeTrabajo.loc[ (tablaDeTrabajo['Promedio'] == 1.00)] , label = 'Cruces'  )
plt.legend()
plt.show()