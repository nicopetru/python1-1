tabla = open("Tabla1.csv", "r")
import pandas as pd

# Equipo,Puntos,Goles a favor,Goles en contra
# Equipo A,30,65,10
# Equipo B,25,45,15
# Equipo C,27,60,20
# Equipo D,17,30,60
# Equipo E,19,25,30
# Equipo F,23,45,20

df = pd.read_csv(tabla , index_col = "Equipo")

for team in df.index:
    DiferenciaDeGol = df.loc[team , 'Goles a favor'] - df.loc[team , 'Goles en contra']
    print('La diferencia de gol de ' +team +' es: '+ str(DiferenciaDeGol))

# print(type(df.loc['Equipo B', 'Puntos']))
# print(type(df.index.name))
# print(df.loc())
# print(df.index[1])