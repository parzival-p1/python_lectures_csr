# Crear diccionario vacío
mi_diccionario = {}
# Agregar un par llave-valor
mi_diccionario["nombre"] = "Ana"
mi_diccionario["edad"] = 25
print(mi_diccionario)
# Resultado: {'nombre': 'Ana', 'edad': 25}

mi_diccionario = {"nombre": "Ana", "edad": 25}

# ciclar
mi_diccionario = {"nombre": "Ana", "edad": 25, "ciudad": "CDMX"}
for llave, valor in mi_diccionario.items():
    print(f"Llave: {llave}, Valor: {valor}")

# Eliminar un par
del mi_diccionario["edad"]
print(mi_diccionario)
# {'nombre': 'Ana', 'ciudad': 'CDMX'}

valor_eliminado = mi_diccionario.pop("ciudad")
print(valor_eliminado)   # CDMX
print(mi_diccionario)    # {'nombre': 'Ana'}
