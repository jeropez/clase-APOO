import unittest
import os
from flota import Auto, Camion, Moto, GestorFlota

class TestVehiculos(unittest.TestCase):

    def test_calculo_impuestos(self):
        self.assertEqual(Auto("Toyota", "Corolla", 20000).calcular_impuesto(), 2000)
        self.assertEqual(Camion("Volvo", "FH16", 50000).calcular_impuesto(), 7500)
        self.assertEqual(Moto("Honda", "CBR", 10000).calcular_impuesto(), 500)

    def test_mostrar_informacion(self):
        moto = Moto("Yamaha", "MT-07", 12000)
        # Simplemente se llama para verificar que no arroje errores
        moto.mostrar_informacion()


class TestGestorFlota(unittest.TestCase):
    ARCHIVO_TEST = "vehiculos_test.txt"

    def setUp(self):
        if os.path.exists(self.ARCHIVO_TEST):
            os.remove(self.ARCHIVO_TEST)
        self.gestor = GestorFlota(self.ARCHIVO_TEST)

    def test_guardar_y_cargar(self):
        auto = Auto("Ford", "Focus", 18000)
        camion = Camion("Scania", "R500", 60000)
        moto = Moto("Suzuki", "GSX", 15000)

        self.gestor.agregar_vehiculo(auto)
        self.gestor.agregar_vehiculo(camion)
        self.gestor.agregar_vehiculo(moto)

        # Se carga una nueva instancia del gestor desde el archivo
        gestor2 = GestorFlota(self.ARCHIVO_TEST)

        self.assertEqual(len(gestor2.vehiculos), 3)
        self.assertIsInstance(gestor2.vehiculos[0], Auto)
        self.assertIsInstance(gestor2.vehiculos[1], Camion)
        self.assertIsInstance(gestor2.vehiculos[2], Moto)

    def tearDown(self):
        if os.path.exists(self.ARCHIVO_TEST):
            os.remove(self.ARCHIVO_TEST)

if __name__ == "__main__":
    unittest.main()