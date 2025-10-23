class Empleado:
    def __init__(self, nombre, documento, edad):
        self.__nombre = nombre
        self.__documento = documento
        self.__edad = edad

    def mostrar_datos(self):
        return {'Nombre: ' : self.__nombre, 'Documento: ' : self.__documento, 'Edad: ' : self.__edad}
    

class Desarrollador(Empleado):
    def __init__(self, nombre, documento, edad, tipo):
        super().__init__(nombre, documento, edad)
        self.__tipo = tipo
    
    def mostrar_datos(self):
       datos = super().mostrar_datos()
       datos['Tipo'] = self.__tipo
       return datos
    

class Gerente(Empleado):
    def __init__(self, nombre, documento, edad, area):
        super().__init__(nombre, documento, edad)
        self.__area = area
        self.__empleados_a_cargo = []

    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos['Area'] = self.__area
        return datos
    def mostrar_empleados_a_cargo(self):
        for empleado in self.__empleados_a_cargo:
            print(empleado.mostrar_datos())
    def asignar_empleado(self, empleado):
        self.__empleados_a_cargo.append(empleado)


empleado1 = Gerente('Isaac', 2222, 5, 'Desarrollo')

empleado2 = Desarrollador('Juan', 1111, 30, 'Backend')
empleado3 = Empleado('Carlos', 3333, 20)

empleado1.asignar_empleado(empleado2)
empleado1.asignar_empleado(empleado3)


