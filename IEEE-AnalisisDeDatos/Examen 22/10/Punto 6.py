import pandas as pd

tabla = pd.read_excel('LigaArgentinapunto10.xlsx')

errores = tabla['Diferencia de Gol'] != (tabla['Goles convertidos'] - tabla['Goles recibidos'])

print(tabla['Error'].mask(errores, 'Si'))