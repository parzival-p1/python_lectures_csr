def memoria():  
    a = 8
    print("Direccion de memoria de a:", id(a))
    b = 8
    print("Direccion de memoria de b:", id(b))
    c = 8
    print("Direccion de memoria de c:", id(c))

def regresarMuchasCosas():
    x = 8
    y = 9
    z = 10
    return x, y, z

def muchasCosas():
    a, b, c = regresarMuchasCosas()

def palabrasReservadas():
    help("keywords")
    print(dir(__builtins__))

def rangos():
    for i in range(0, 4, -1): 
        print(i)

def slicing():
    lista = [22, 11, 9, 13, 17, 23, 51, 49, 3]
    lista1 = lista[] 