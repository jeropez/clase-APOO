inventario = {
    "Cuaderno": 15,
    "Lápiz": 40,
    "Borrador": 0,
    "Marcador": 10,
    "Regla": 5, 
}

print("Bienvenido al programa")

while True:
    print("Elija la opción que desea realizar")
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Mostrar inventario")
    print("0. Salir")
    opcion = int(input())

    if opcion == 1:
        nombre_producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad que hay del producto: "))
        if nombre_producto in inventario:
            inventario[nombre_producto] += cantidad
        else:
            inventario[nombre_producto] = cantidad
        print("Inventario actualizado")
    
    elif opcion == 2:
        nombre_producto = input("Ingrese el nombre del producto que desea vender: ")
        if nombre_producto in inventario:
            cantidad = int(input("Ingrese la cantidad que va a vender del producto: "))
            if inventario[nombre_producto] >= cantidad:
                inventario[nombre_producto] -= cantidad
                print("Inventario actualizado")
            else: 
                print("No hay cantidad suficiente")
        else:
            print("Producto no existe")

    elif opcion == 3:
        print(inventario)

    elif opcion == 0:
        print("Hasta luego")
        break
    else:
        print("Opción no válida")


