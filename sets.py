"""
Set is a collection of items. 
Set is a collection of unordered and un-indexed 
distinct elements. In Python set is used to store 
unique items, and it is possible to find the 
union, intersection, difference, symmetric 
difference, subset, super set and disjoint set 
among sets.
"""

# Creating a set

st = {}
st = set()

# Creating a set with initial items
st = {'item1', 'item2', 'item3', 'item4'}

frutas = {'manzana', 'pera', 'piña', 'mango'}

# len() para encontrar el largo de un set
print(len(frutas)) # 4

# Checar si un item existe en un set
print('mango' in frutas) # True

# Agregar un item a un set de manera aleatoria
st2 = {'item1', 'item2', 'item3', 'item4', 'item5'}
st2.add('item6')
print(st2) # {'item6', 'item1', 'item5', 'item4', 'item2', 'item3'}

# Agregar multiples items update()
verduras = {'apio', 'zanahoria', 'cebolla', 'hongos'}
verduras.update(['papa', 'tomate', 'espinca'])
print(verduras)

# Borrar items de un set remove()
verduras.remove('apio')
print(verduras)

# pop() borra de manera aleatoria
print(verduras.pop()) # se elimino zanahoria

# Eliminar los elementos del set clear()
verduras.clear()
print(verduras) # set()

# Elimna todo el set del
pet = {'perro', 'gato', 'conejo', 'tortuga'}
del pet

# Convertir una lista a un set
lista = ['item1', 'item2', 'item3', 'item4']
list_set = set(lista)
print(list_set)

# Unir dos sets union()
perros = {'pastor', 'bulldog', 'bullterry', 'chihuahua'}
gatos = {'siames', 'doncat', 'garfield'}
catdog = perros.union(gatos)
print(catdog) # {'doncat', 'chihuahua', 'siames', 'bulldog', 'pastor', 'garfield', 'bullterry'}

# update() puede hacer lo mismo
numero = {'1', '2', '3', '4', '5'}
letras = {'a', 'b', 'c', 'd', 'e'}
alphanum = numero.update(letras)

# Intersecciones retorna un set de elementos encontrados en dos sets
numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
pares = {2, 4, 6, 8, 10}
print(numeros.intersection(pares)) # {2, 4, 6, 8, 10

# Checar un subset y un super set
print(numeros.issubset(pares)) # False
print(numeros.issuperset(pares)) # True

# La diferencia entre dos sets, retorna la diferencia entre los dos
python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.difference(dragon)) # {'y', 't', 'p'}

# Encuentra la diferencia simetrica entre dos sets
# Retorna un set que contiene los elementos de ambos sets, excepto elementos que se repitan
symetric = python.symmetric_difference(dragon)
print(symetric) # {'y', 'g', 'd', 'a', 'r', 't', 'p'}

# Uniendo sets
disj = python.isdisjoint(dragon)
print(disj)
