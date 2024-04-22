"""
1 Alumno es profesor
1 Alumno es asistente
(A)
Pedir la edad de los compañeros que
vinieron hoy a clase y ordenar
los datos de menor a mayor
(B)
El mayor es el profesor y el
menor es el asistente:
¿Quien es quien?
"""



def compañeros(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input("ingrese el nombre del alumno: ")
        edad = int(input("ingrese la edad del alumno: "))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    print(f"el profesor es {profesor} y el asistente es {asistente}")


print((compañeros(3)))