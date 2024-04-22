#creando una funcion de 3 parametros
def frase (nombre, apellido, adjetivo):
    return (f'Hola {nombre} {apellido}, sos muy {adjetivo}')

#utilizando keyword arguments
frase_resultante = frase (adjetivo = "lindosm set-force-adoptable true", nombre = "Marcos", apellido ="Bustos")
print (frase_resultante)