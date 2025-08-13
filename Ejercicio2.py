class Producto: 
    def __init__(self, nombre, precio, cantidad, codigo):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.codigo = codigo
    
    def vender(self, cantidad_a_vender):
        if self.cantidad >= cantidad_a_vender:
            self.cantidad = self.cantidad - cantidad_a_vender
            print("Producto vendido exitosamente")
        else:
            print("No hay cantidad disponible")

lista_productos = []

print("Bienvenido a la tienda")
while True:
    print("Ingrese la opción deseada")
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Mostrar inventario")
    print("0. Salir")

    opcion = int(input())

    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))
        codigo = int(input("Ingrese el código: "))

        nuevo_producto = Producto(nombre, precio, cantidad, codigo)
        lista_productos.append(nuevo_producto)
        print("Producto agregado exitosamente")

    elif opcion == 2:
        codigo_producto = int(input("Ingrese el código del producto que quiere vender: "))
        existe = False
        for producto in lista_productos:
            if producto.codigo == codigo_producto:
                cantidad_venta = int(input("Cuánto de ese producto va a vender: "))
                producto.vender(cantidad_venta)
                existe = True
                break
        
        if existe == False:
            print("Este producto no existe")

    elif opcion == 3:
        for producto in lista_productos:
            print("Nombre: ", producto.nombre)
            print("Cantidad disponible: ", producto.cantidad)
            print("\n")

    elif opcion == 0:
        print("Hasta luego")
        break
    else:
        print("Opción no válida")
