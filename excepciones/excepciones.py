#creando una funcion de suma
def suma():
    #iniciando bucle
    while True:
        #pidiendo valores a sumar
        a = input("numero 1: ")
        b = input ("numero 2: ")
        #intentando sumarlos
        try:
            resultado = int(a) + int(b)
        except:
            #si no se puede por un error mostrar esto
            print("te pedi un numero")
        else:
            #si todo salio bien terminamos el bucle
            break
        #esto se ejecuta siempre sin importar nada
        finally:
            print("esto se ejecuta siempre")
    #devolvemos el resultado
    return resultado


print(suma())