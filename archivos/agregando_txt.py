with open ("archivos/test.txt","a") as archivo:
    #agregando al archivo,  NO SOBREESCRIBE
    # archivo.write("que pasooo?")
    
    #agregando lineas con un bucle
    for i in range(5):
        archivo.write(f"line agregada {i+1}\n")