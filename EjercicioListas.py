import random

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.numero = [random.randint(100, 999) for _ in range(5)]

lista_personas = []
print("Bienvenido a la rifa")

while True:
    print("Ingrese la opción deseada: ")
    print("1. Agregar persona")
    print("0. Salir")

    opcion = int(input())
    if opcion == 1:
        nombre = input("Ingrese el nombre de la persona: ")
        nueva_persona = Persona(nombre)
        print("Persona agregada exitosamente, sus números asignados son: ", nueva_persona.numero)
        lista_personas.append(nueva_persona)
    
    elif opcion == 0:
        print("Hasta luego")
        break

    else: 
        print("Opción no válida")
    