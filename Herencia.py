# Existe una clase padre y las clases hijas
# Permite crear nuevas clases a partir de las clases existentes
# Las clases hijas heredan atributos y metodos de la clase padre
# Permite reutilizar el codigo y evitar duplicacion

# Usar herencia solo cuando haya una relacion es-un

# Ejemplo

""" class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print(f'{self.nombre} hace un sonido')

    def orinar(self):
        print(f'{self.nombre} esta orinando')

class Perro(Animal):
    def __init__(self, nombre, color_pelota):
        super().__init__(nombre)
        self.color_pelota = color_pelota

    def hacer_sonido(self):
        print(f'{self.nombre} hace guau guau')

    def salir_a_pasear(self):
        print(f'{self.nombre} esta paseando')

class Gato(Animal):
    def hacer_sonido(self):
        print(f'{self.nombre} hace miau miau')

animal1 = Perro('Mia')
animal1.hacer_sonido()
animal1.salir_a_pasear()
animal1.orinar()

animal2 = Gato('Simba')
animal2.hacer_sonido()
animal2.orinar()


print(isinstance(animal1, Perro))
print(isinstance(animal1, Animal))

print(issubclass(Gato, Animal)) """

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f'Mi nombre es {self.nombre} y tengo {self.edad}')

class Estudiante(Persona):

    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    def decir_carrera(self):
        print(f'Estoy estudiando {self.carrera}')

estudiante1 = Estudiante('Jero', '17', 'Computacion Cientifica')
estudiante1.presentarse()
estudiante1.decir_carrera()
