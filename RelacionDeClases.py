class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

class Profesor:
    def __init__(self, nombre, edad, experiencia):
        self.nombre = nombre
        self.edad = edad
        self.experiencia = experiencia

class GrupoAsignatura:
    def __init__(self, nombre, horario, codigo, profesor):
        self.nombre = nombre
        self.horario = horario
        self.codigo = codigo
        self.profesor = profesor
        self.estudiante = []

    def Agregar_estudiante(self, estudiante):
        self.estudiante.append(estudiante)
        print("Estudiante agregado exitosamente")

    def Promedio(self):
        acumulador = 0
        for estudiante in self.estudiante:
            acumulador = acumulador + estudiante.nota
        promedio = acumulador / len(self.estudiante)
        return promedio
    
    def MostrarEstudiantes(self):
        return  "La cantidad de estudiantes es:" ,len(self.estudiante)
    
profesor = Profesor("Juan", 35, 5)
poo = GrupoAsignatura("Programación orientada a objetos", "M-V 10-12", "62", profesor)

esudiante1 = Estudiante("Esteban", 17, 5)
esudiante2 = Estudiante("Jorge", 20, 2.5)
esudiante3 = Estudiante("Luis", 21, 3)
esudiante4 = Estudiante("Jero", 18, 4)

poo.Agregar_estudiante(esudiante1)
poo.Agregar_estudiante(esudiante2)
poo.Agregar_estudiante(esudiante3)
poo.Agregar_estudiante(esudiante4)

print(poo.MostrarEstudiantes())
