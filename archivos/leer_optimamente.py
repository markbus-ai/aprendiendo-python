#leyendo un archivo de forma correcta con with open y cambiandole el nombre a archivo
with open ("archivos/test.txt") as archivo:
    #leyendo el archivo
    print(archivo.read())
#se cierra automaticamente