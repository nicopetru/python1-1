import pandas as pd

tabla = pd.read_excel('LigaArgentinapunto2.xlsx')

ahora = tabla.dropna(subset=['Puntaje', 'Diferencia de Gol'])
print(ahora)