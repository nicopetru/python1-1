import pandas as pd

ArchivoDesafio = open("DatosIEEE.csv" , 'r')

df = pd.read_csv(ArchivoDesafio, index_col='Legajo')

def prome(columna):
    calcPromedio = sum(df[columna])/len(df[columna])
    return calcPromedio
    # print(df[columna])
    # print(len(df[columna]))

def sonNumeros(algo):
    for materia in algo.select_dtypes( include = 'int64').columns:
        print('El promedio de ' +str(materia) + ' fue: ' + str(prome(materia)))

# print(df['Quimica'])
# print(df.select_dtypes(include = 'int64').columns)
# print(sum(df['Quimica'])/len(df['Quimica']))
print(sonNumeros(df))