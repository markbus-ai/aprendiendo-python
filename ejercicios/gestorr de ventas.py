import os

'''
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero. 
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
'''

'''
file_name = "markbusking.txt"

with open(file_name, "w") as file:
    file.write("Markbusking\n")
    file.write("18\n")
    file.write("python")

with open(file_name, "r") as file:
    print(file.read())


os.remove(file_name)
'''
file_name = "markbusking_shop.txt"

open(file_name, "a")


while True:
    print("1.agregar producto")
    print("2.mostrar todos los productos")
    print("3.eliminar producto")
    print("4.consultar producto")
    print("5.calcular venta total")
    print("6.venta por producto")
    print("7.actualizar producto")
    print("8.salir")


    opcion = input("ingresa un numero de opcion:\n")

    if opcion == "1":
        print("ingrese el nombre del producto")
        name = input("nombre:")
        cantidad = input("cantidad vendida: ")
        precio = input("precio: ")
        with open(file_name, "w") as file:
            file.write(f"{name}, {cantidad}, {precio}\n")
            
    elif opcion == "2":
        with open(file_name, "r") as archivo:
            # Leer todas las líneas del archivo
            lineas = archivo.readlines()
            # Imprimir todas las líneas
            for linea in lineas:
                print(linea.strip())  # Eliminar el salto de línea final
    elif opcion == "3":
            name = input("Introduce el nombre: \n")
            
            with open(file_name,"r") as file:
                contenido = file.readlines()

            with open(file_name,"w") as file:
                for line in contenido:
                    if name != line.split(" | ")[0]:
                        file.write(line)
    elif opcion == "4":
        name = input("nombre:")
        cantidad = input("cantidad vendida: ")
        precio = input("precio: ")
        with open(file_name, "r") as file:
            lines = file.readlines
        with open(file_name, "w") as file:
            for line in file.readlines:
                if line.split(", ")[0] == name:
                        file.write("f {name}, {cantidad}, {precio}\n")
                else: file.write(line)
    elif opcion == "5":
            total = 0
            with open(file_name, "r") as file:
                componentes = line.split(", ")
                cantidad = int(componentes[1])
                precio = float(componentes[2])
                total += cantidad * precio
        
    elif opcion == "6":
        name = input("nombre:")
        total = 0
        with open(file_name, "r") as file:
            componentes = line.split(", ")
            if componentes[0] == name:
                cantidad = int(componentes[1])
                precio = float(componentes[2])
                total += cantidad * precio
        
    elif opcion == "7":
        name = input("nombre:")
        with open(file_name, "r") as file:
            for line in file.readlines:
                if line.split(", ")[0] == name:
                    print(line)
                else: print("no se encontro el producto")
                break
    
    elif opcion == "8":
        break
        
    else: print("ingrese un numero valido")
        













