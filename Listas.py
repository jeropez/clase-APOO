# Crear lista
mi_lista = ["primer elemento", "segundo elemento", "tercer elemento"]
print(mi_lista)
print(mi_lista[0])
print(mi_lista[1])
print(mi_lista[2])

longitud = len(mi_lista)
print(longitud)

print(mi_lista[longitud - 1])
print(mi_lista[-1])

print(mi_lista[:2])

print(mi_lista[1:])

lista_ceros = [0] * 10
print(lista_ceros)

import random 
lista_random = []
for i in range(0, 10):
    lista_random.append(random.randint(0, 100))
print(lista_random)

lista_random2 = [random.randint(1, 100) for _ in range(10)]
print(lista_random2)

lista_ejemplo = [i for i in range(0,10)]
print(lista_ejemplo)

lista_ejemplo[2] = 1
lista_ejemplo[5] = 2
print(lista_ejemplo)

#Eliminar un elemento
# lista_ejemplo.remove(1)
# print(lista_ejemplo)

# #Eliminar una posicion
# del lista_ejemplo[2]
# print(lista_ejemplo)

lista_ejemplo = [elemento for elemento in lista_ejemplo if elemento != 1]
print(lista_ejemplo)

lista_ejemplo.reverse()
print(lista_ejemplo)

lista_ejemplo.sort()
print(lista_ejemplo)

lista_ejemplo.sort(reverse=True)
print(lista_ejemplo)

