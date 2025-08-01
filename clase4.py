class Estudiantes:
    def __init__(self, nombre, edad, nota1, nota2, nota3):
        self.nombre = nombre
        self.edad = edad
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def mostrarDatos(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Nota 1: ", self.nota1)
        print("Nota 2: ", self.nota2)
        print("Nota 3: ", self.nota3)

    def calcular_promedio(self):
        promedio = (self.nota1 + self.nota2 + self.nota3) / 3
        return promedio

print("Bienvenido a la gestión de estudiantes")
print("Ingrese el nombre del estudiante: ")
nombre = input()
print("Ingrese la edad del estudiante: ")
edad = input()
print("Ingrese la primera nota: ")
nota1 = float(input())
print("Ingrese la segunda nota: ")
nota2 = float(input())
print("Ingrese la tercera nota: ")
nota3 = float(input())

estudiante = Estudiantes(nombre, edad, nota1, nota2, nota3)

promedio_estudiante = estudiante.calcular_promedio()
print("El promedio de ", estudiante.nombre, "es", promedio_estudiante)


