import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.reshape.merge import merge_ordered

Amazon = pd.read_csv('AMZN.csv' , index_col='Date')
Google = pd.read_csv('GOOGLE.csv', index_col='Date')
tablaDeTrabajo = pd.merge(Amazon['Adj Close'], Google['Adj Close'], on='Date' , suffixes=('Amz', 'Goo'))
tablaDeTrabajo = tablaDeTrabajo.rename(columns={'Adj CloseAmz' : 'Amazon', 'Adj CloseGoo' : 'Google'})

# print(Amazon.head())
# print(Google.head())

print(tablaDeTrabajo.head())