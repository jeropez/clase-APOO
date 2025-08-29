"""Imagina que estás creando un programa para administrar una biblioteca personal.
Cada libro tiene la siguiente información:

Título

Autor

Año de publicación

Género

Se espera que el sistema permita:

Registrar nuevos libros en la biblioteca.

Listar todos los libros registrados.

Consultar si un libro ya existe en la biblioteca (por título).

Obtener el total de libros guardados.

Guía

Debes crear una clase para representar los libros.

Decide si la colección de libros se almacenará en una lista o en una tupla, y justifica tu decisión.

Implementa funciones o métodos que cumplan con los 4 puntos solicitados."""

class Libros:
    def __init__(self, titulo, autor, año, genero):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self. genero = genero

lista_libros = [] 

while True:
    print("1. Agregar nuevo libro")
    print("2. Mostrar libros registrados")
    print("3. Consultar existencia de un libro")
    print("4. Obtener el total de libros guardados")
    print("0. Salir")
    opcion = int(input("Ingresa la opción deseada: "))

    if opcion == 1:
        print("Ingrese el nombre del libro: ")
        titulo = input()
        print("Ingrese el autor del libro: ")
        autor = input()
        print("Ingrese el año de publicación del libro: ")
        año = input()
        print("Ingrese el genero del libro: ")
        genero = input()
        libro = Libros(titulo, autor, año, genero)
        lista_libros.append(libro)
        print("Libro agregado correctamente")

    elif opcion == 2:
        for libro in lista_libros:
            print("\n")
            print("Titulo: ", libro.titulo)
            print("Autor: ", libro.autor)
            print("Año de publicación: ", libro.año)
            print("Genero: ", libro.genero)
            print("\n")
    
    elif opcion == 3:
        busqueda = input("Que libro estas buscando: ")
        for libro in lista_libros:
            if busqueda == libro.titulo:
                print("Si existe")
            else: 
                print("No existe")

    elif opcion == 4:
        print("El total de libros en la biblioteca es: ", len(lista_libros))
    
    elif opcion == 0:
        print("Hasta luego.")
        break
    else:
        print("Opción no válida")

# Decidimos hacerlo con una lista ya que necesitabamos ir agregando los libros y la tupla no permitiria hacer esto ya que necesita valores predeterminados

# Hecho por: Isabella Quintero Gutierrez y Jerónimo Pérez Macías 
    

