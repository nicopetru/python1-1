
capital = input("cuanta plata tenes: ")
tasa = input("A q tasa: ")
tiempo = input("Cuantos años la dejas: ")

total = int(capital) *((1+int(tasa)/100)**int(tiempo))

print(total)

