

class Empresa:
    def __init__(self, nombre):
          self.nombre = nombre
          self.vehiculos = []


    def registrar_vehiculo(self, vehiculo):
        self.marca = input('Ingrese la marca del vehiculo: ')
        self.placa = input('Ingrese la placa del vehiculo: ')
        self.valor = input('Ingrese el valor del vehiculo: ')
        vehiculo = Vehiculo(self.marca, self.placa, self.valor)
        self.vehiculos.append(vehiculo)
         
    def mostrar_vehiculos(self, vehiculo):
        for vehiculo in self.vehiculos:
             print(f'Marca: {self.marca}, Placa: {self.placa}, Valor: {self.valor}')

class Vehiculo:
        def __init__(self, marca, placa, valor):
            self.marca = marca
            self.placa = placa
            self.valor = float(valor)
        
        def mostrar_informacion(self):
           print(f'Marca: {self.marca}, Placa: {self.placa}, Valor: {self.valor}') 

empresa1 = Empresa('Empresa 1')
empresa1.registrar_vehiculo