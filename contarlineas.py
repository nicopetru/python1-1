archivos = ["alto-leak.txt" , "alto-leak2.txt" , "alto-leak3.txt" ]

for line in archivos:
    count = 0
    file = open(line, "r")
    for linea in file:
        count += 1
    print(line,"tiene",count, "lineas") 
