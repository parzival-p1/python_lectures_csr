def suma():
    x = int(input("Dame el primer numero: "))
    y = int(input("Dame el segundo numero: "))
    result = x + y

    print(f"El resultado es: {result}")

def mayor():
    x = int(input("Dame un numero: "))
    y = int(input("Dame otro numero: "))

    if (x > y):
        print(f"Este es el mayor: {x}")
    else:
        print(f"Este es el mayor: {y}")

def negativo():
    x = int(input("Dame un numero: "))

    if (x < 0):
        print("Numero negativo")
    elif (x == 0):
        print("Es cero")
    else:
        print("Es positivo")

def pares():
    x = int(input("Dame el inicio: "))
    y = int(input("Dame el final: "))

    if (x % 2 != 0):
        x += 1
    for i in range(x, y + 1, 2):
        print(i)

def promedio():
    result = 0
    for i in range (5):
        x = int(input("Dame un numero: "))
        result += x
    prom = result / 5
    print("El resultado es:", prom)

# T A R E A
# 1. Hacer una func que calcule el facotrial de un numero con for
# n! = n * (n - 1)

def factorial(n=None):
    n = n * (n - 1)
    for i in range(n)

# 2. Hacer una func que muestre los numeros impares dado un rango con while
def evens():
    x = int(input("Introduce el primer rango de numeros ej. 1 - 10"))
    y = int(input("Introduce el segundo rango: "))

    if (x % 2 == 0):

    while x <  y:

# 3. Hacer una func que lea del usuario ap paterno, ap materno, nombre y me de las dos primeras
    # letras de cada una de ellas
#4. Hacer una func que lea un numero y me diga que mes conrresponde ese numero, 03 = marzo
#5. Hacer el binomio de newton, con for

