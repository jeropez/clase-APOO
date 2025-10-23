import random

class Cuenta:
    def __init__(self, nombre_titular):
        self.nombre_titular = nombre_titular
        self.numero_cuenta = random.randint(10000, 99999)
        self.saldo = 0

    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
        return self.saldo
    
    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo = self.saldo - cantidad
            return self.saldo
        else:
            print("No hay dinero para retirar")
            return -1
        
    def consultar(self):
        return self.saldo
    
# Programa principal

lista_cuentas= []

print("Bienvenido al banco")

while True:
    print("Ingrese la opción deseada: ")
    print("1. Registrar cuenta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Consultar saldo")
    print("0. salir")

    opcion = int(input())
    if opcion == 1:
        nombre = input("Ingrese el nombre del titular: ")
        nueva_cuenta = Cuenta(nombre)
        lista_cuentas.append(nueva_cuenta)
        print("Cuenta creada exitosamente. Su número de cuenta es: ", nueva_cuenta.numero_cuenta)

    elif opcion == 2:
        numero_cuenta = int(input("Ingrese el número de cuenta: "))
        existe = False
        for cuenta in lista_cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                existe = True
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                nuevo_saldo = cuenta.depositar(cantidad)
        if existe == False:
            print("Cuenta no exisite")

    elif opcion == 3:
        numero_cuenta = int(input("Ingrese el número de cuenta: "))
        existe = False
        for cuenta in lista_cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                existe = True
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                nuevo_saldo = cuenta.retirar(cantidad)

                if nuevo_saldo >= 0:
                    print("Retiro exitoso. Su nuevo saldo es: ", nuevo_saldo)
        if existe == False: 
            print("Cuenta no existe")
   
    elif opcion == 4:
        numero_cuenta = int(input("Ingrese el número de cuenta: "))
        existe = False
        for cuenta in lista_cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                existe = True
                print("Su saldo es: ", cuenta.consultar())

    elif opcion == 0:
        print("Hasta luego")
        break
    
    else:
        print("Opción no válida")



