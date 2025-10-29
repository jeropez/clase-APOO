import os

class Vehiculo:
    def __init__(self, marca, modelo, valor):
        self.marca = marca
        self.modelo = modelo
        self.valor = float(valor)

    def mostrar_informacion(self):
        """Muestra la información del vehículo, incluyendo su impuesto."""
        impuesto = self.calcular_impuesto()
        print(f"{self.__class__.__name__}: {self.marca} {self.modelo} "
              f"- Valor: ${self.valor:.2f} - Impuesto anual: ${impuesto:.2f}")

    def __str__(self):
        """Formato para guardar en archivo."""
        return f"{self.__class__.__name__},{self.marca},{self.modelo},{self.valor}"

    @staticmethod
    def from_string(linea):
        """Crea el vehículo correcto a partir de una línea de texto."""
        tipo, marca, modelo, valor = linea.strip().split(",")
        valor = float(valor)

        if tipo == "Auto":
            return Auto(marca, modelo, valor)
        elif tipo == "Camion":
            return Camion(marca, modelo, valor)
        elif tipo == "Moto":
            return Moto(marca, modelo, valor)
        else:
            raise ValueError(f"Tipo de vehículo desconocido: {tipo}")


# ================================
# Subclases con sus propios impuestos
# ================================
class Auto(Vehiculo):
    def calcular_impuesto(self):
        return self.valor * 0.10


class Camion(Vehiculo):
    def calcular_impuesto(self):
        return self.valor * 0.15


class Moto(Vehiculo):
    def calcular_impuesto(self):
        return self.valor * 0.05


# ================================
# Clase GestorFlota
# ================================
class GestorFlota:
    def __init__(self, archivo="vehiculos.txt"):
        self.archivo = archivo
        self.vehiculos = self.cargar_vehiculos()

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        self.guardar_vehiculos()

    def guardar_vehiculos(self):
        """Guarda los vehículos en un archivo de texto."""
        with open(self.archivo, "w", encoding="utf-8") as f:
            for v in self.vehiculos:
                f.write(str(v) + "\n")

    def cargar_vehiculos(self):
        """Carga los vehículos desde el archivo si existe."""
        vehiculos = []
        if not os.path.exists(self.archivo):
            return vehiculos

        with open(self.archivo, "r", encoding="utf-8") as f:
            for linea in f:
                if linea.strip():
                    vehiculos.append(Vehiculo.from_string(linea))
        return vehiculos

    def resumen_general(self):
        print("\n--- RESUMEN DE VEHÍCULOS ---")
        total_impuestos = 0
        for v in self.vehiculos:
            v.mostrar_informacion()
            total_impuestos += v.calcular_impuesto()
        print(f"\nTOTAL IMPUESTOS: ${total_impuestos:.2f}")

# ================================
# Ejecución interactiva
# ================================
if __name__ == "__main__":
    gestor = GestorFlota()

    while True:
        print("\n=== MENÚ DE GESTIÓN DE FLOTA ===")
        print("1. Registrar Auto")
        print("2. Registrar Camión")
        print("3. Registrar Moto")
        print("4. Ver resumen")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion in ["1", "2", "3"]:
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            valor = float(input("Valor: "))

            if opcion == "1":
                vehiculo = Auto(marca, modelo, valor)
            elif opcion == "2":
                vehiculo = Camion(marca, modelo, valor)
            else:
                vehiculo = Moto(marca, modelo, valor)

            gestor.agregar_vehiculo(vehiculo)
            print("Vehículo registrado correctamente.")

        elif opcion == "4":
            gestor.resumen_general()

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida.")
