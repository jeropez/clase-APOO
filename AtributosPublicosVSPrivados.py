# Atributos públicos
class Persona:
    def __init__(self, nombre, cedula, ti):
        self.nombre = nombre # Atributos públicos
        self.__cedula = cedula # Atributos privados
        self.__ti = ti

    def obtener_documento(self):  # Encapsulación
        if self.__cedula is not None:
            return self.__cedula
        else:
            return self.__ti

persona1 = Persona("Juan", 1111, None)
persona2 = Persona("María", 2222, None)
niño1 = Persona("Isaac", None, 3333)

"""print(" ")

print("El nombre de la primera persona es: ", persona1.nombre)
print("El documento de la primera persona es: ", persona1.obtener_documento())

print(" ")

print("El nombre de la segunda persona es: ", persona2.nombre)
print("El documento de la segunda persona es: ", persona2.obtener_documento())

print(" ")

print("El nombre de la tecera persona es: ", niño1.nombre)
print("El documento de la tercera persona es: ", niño1.obtener_documento())

print(" ")"""


# Ejercicio

class Dispositivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = False

    def encender(self):
        self.estado = True
        print(self.nombre, ": encendido")

    def apagar(self):
        self.estado = False
        print(self.nombre, ": apagado")

class Espacio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__dispositivos = []

    def agregard(self, dispositivo):
        self.__dispositivos.append(dispositivo)
        print("Dispositivo agregado")
    
    def mostrard(self):
        for dispositivo in self.__dispositivos:
            print(dispositivo.nombre)

class Casa:
    def __init__(self, direccion):
        self.direccion = direccion
        self.__espacios = []

    def agregare(self, nombre):
        self.__espacios.append(Espacio(nombre))
        print("Espacio Agregado")

    def buscare(self, nombre):
        for espacio in self.__espacios:
            if espacio.nombre == nombre:
                return espacio
        return None
        
    def mostrare(self):
        for espacio in self.__espacios:
            print(espacio.nombre)

mi_casa = Casa("Calle 123")
mi_casa.agregare("Cocina")
mi_casa.agregare("Habitación")
mi_casa.agregare("Baño")

television = Dispositivo("Televisión")
mi_casa.buscare("Habitación").agregard(television)
mi_casa.buscare("Habitación").mostrard()