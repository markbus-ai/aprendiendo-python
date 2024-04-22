def inversa (cadena):
    
    longitud  = -(len(cadena)-1)
    nueva_cadena = str()
    for n in range (longitud, 1):
        n = abs(n)
        nueva_cadena += cadena[n]
    print(nueva_cadena)
    
inversa('hola')

