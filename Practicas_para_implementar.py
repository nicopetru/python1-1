list = ('ALL UPPER','all lower','mixed UPPER and lower',"","asd","123","123")

def mayusculas(x):
    if x.strip() == "": return True
    else:
        if x.isdigit() == True: return True
        else:
#            print("llego aca")
            return x.isupper()

def otraso(h):
    return h.upper() == h 


for y in list:
    print(y)
#    print(type(y))
    print(mayusculas(y))
    print(otraso(y))
