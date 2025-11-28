# Leer datos del usuario

def leer_datos():
    MAX = 10
    numeros = []
    i = 0
    while (i < MAX):
        num = int(input(f"Número {i + 1}: "))
        numeros.append(num)
        i += 1
    return numeros

# Imprimir la lista
def imprimir_lista(lista):
    print("Lista de números: ")
    for i in lista:
        print("Lei el numero:", i, "del usuario")
    # print(type(lista))
    
# Calcular la media
def media(lista):
    suma = 0
    for n in lista:
        suma += n
    return suma / len(lista)
"""
numeros = leer_datos()
imprimir_lista(numeros)
print("La media es:", media(numeros))"""

# Calcular la mediana
def mediana(lista):
    data = sorted(lista)
    index = len(lista) // 2 
    
    if len(lista) % 2 != 0:
        return data[index]
    else:
        return (data[index] + data[index - 1]) / 2

def moda(lista):
    element = lista[0]
    reps = lista.count(element)

    for n in lista:
        total = lista.count(n)
        if (reps < total):
            element = n
            reps = total
    return element

lista = [8,7,1,3,1,5,6,6,5,1,8,1,7]
print(moda(lista))

def isPalindrome(x: int) -> bool:
    palindrome = str(x)
    print(palindrome)
    fst = 0 
    lst = -1
    testpass = False

    while(palindrome[lst] == palindrome[fst] and fst < lst):
        testpass = True
        fst += 1
        lst -= 1
    if(fst >= lst and testpass):
        return True
    else:
        return False
print(isPalindrome(-121))

# terminar el programa
"""
hacer un programa que guarde una serie de alumnos con sus materias de la escuela 
y sus respectivas calificaciones. SOLO USAR DICCIONARIOS
dic: con materias
materias = { "ingles" : 70, "biologia" : 90 }
alumnos = { "Pedro" : materias }

    0. Menu
    1. Agregar un alumno
    2. Agregar materia
    3. Imprimir todos los alumnos con sus calificaiones
    4. Quiero borrar materia de un alumno
    5. Quiero poder actualizar la calificación de una materia
    6. Poder borrar un alumno
"""
