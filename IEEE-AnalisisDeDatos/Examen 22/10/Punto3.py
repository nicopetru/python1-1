import pandas as pd

tabla = pd.read_excel('LigaArgentinapunto3.xlsx', index_col='Equipo')
dataFrame = tabla.to_dict('index')
# print(tabla.idxmax()['Goles recibidos'])  Da error
print(tabla['Goles recibidos'].idxmax())