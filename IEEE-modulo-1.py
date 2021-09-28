def lothar(n):
  # Solucion
    contar = 0
    while n != 1:
        
        print("hola")
        if n % 2 == 1:
            n = n * 3 + 1
            contar += 1
            print("chau")
        elif n % 2 == 0:
            n = n / 2
            contar += 1
            print("chau 1")
    return contar 

n = int(input())

print( lothar(n) )