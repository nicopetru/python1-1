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
# print(df)
sorted = df.sort_values([ 'Puntos', 'Goles a favor'] , ascending = False) #ordena de mayor a menor con ascending y segun los strings de la lista del principio
# print(sorted)
print(f"El campeon es: {sorted.index[0]}  y el ultimo es: {sorted.index[-1]}" )