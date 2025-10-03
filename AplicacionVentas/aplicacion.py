from modelos import Producto, Cliente
from pedido import Factura
from Descuentos import DescuentoVIP, DescuentoVolumen, SinDescuento
from impuestos import IVA, Excentos

cliente = Cliente(123, 'Juan', False)
producto1 = Producto(567, 'Arepas', 'alimentos', 2000)
producto2 = Producto(949, 'Suscripcion Netflix', 'servicios', 25000)
producto3 = Producto(111, 'Computador', 'tecnologia', 2500000)

mifactura = Factura(cliente)

mifactura.agregar_linea(producto2, 10)
descuento_a_aplicar = DescuentoVolumen()
impuesto_a_aplicar = IVA()

print(mifactura.calcular_total(descuento_a_aplicar, impuesto_a_aplicar))