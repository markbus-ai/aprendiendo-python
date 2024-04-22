with open ("archivos/test.txt","w") as archivo:
    #sobre escribiendo el archivo
    #archivo.write("que pasooo?")
    
    #escribieno 2 lineas con writelines
    archivo.writelines(["que pasooo?\n","ahhh,con razon"])
    archivo.writelines(["que pasooo?\n","ahhh,con razon"])