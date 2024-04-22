#leyendo un archivo con open
archivo = open("archivos/test.txt")

#leer archivo completo
#archivo = archivo_sin_leer.read()

#leer lineas
#lineas = archivo_sin_leer.readlines()

linea = archivo.readline()
#cerrar archivo
archivo.close()
print(linea)