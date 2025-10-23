""" # Crear diccionario
agenda = {
    "Ana": "3145206147",      # La estructura es clave: valor
    "Bruno": "3106256734",
    "Carla": "3017778899",
}

# Mostrar el elemento de una clave
print("Teléfono de Bruno:", agenda["Bruno"])

# Agregar elemento a un diccionario
agenda["Juan"] = "3001112233"


# Buscar elementos en un diccionario
nombre = input("Ingrese el nombre del contacto: ")

if nombre in agenda:
    print("Teléfono de " + nombre, agenda[nombre])
else:
    print("No está")


# Eliminar un elemento del diccionario
# del agenda["Ana"]

# Mostar todos los valores del diccionario
print("Diccionario completo", agenda) """

estudiantes = {
    "Lucia": [4.5, 3.8, 4.2],
    "Mateo": [3.0, 3.5, 4.0, 4.2],
    "Sofia": [5.0, 4.8, 4.9]
    
}

promedios = {}

for nombre, notas in estudiantes.items():
    prom = sum(notas) / len(notas)
    promedios[nombre] = prom
    print(f"Promedio de {nombre}: {prom:.2f}")

print(promedios)

# Encontrar mejor promedio
mejor_estudiante = max(promedios, key=promedios.get)
print(mejor_estudiante, promedios[mejor_estudiante])