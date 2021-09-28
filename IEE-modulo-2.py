listaLetras = []
Palabra = input()
for x in Palabra:
    x = x.upper()
    if x not in listaLetras:
        listaLetras.append(x)        
# print(listaLetras)
intentosFallidos = 0
intentos = 0

while len(listaLetras) != 0 and intentosFallidos != 3:
    intentos += 1
    Adivina = input().upper()
    if Adivina in listaLetras:
        listaLetras.remove(Adivina)
    elif Adivina not in listaLetras:
        intentosFallidos += 1
print(intentos)