
    
def inversa(cadena):
    longitud  = -(len(cadena)-1)  # Obtiene el índice negativo para el último caracter
    nueva_cadena = str()
    for n in range (longitud, 1):
        n = abs(n)
        nueva_cadena += cadena[n]
    return nueva_cadena  # Devuelve la cadena invertida



def ISpalindromo(cadena):
    nueva_cadena = inversa(cadena)
    if cadena == nueva_cadena:
        return True



def superposicion(l1,l2):
    for n in (l1):
        for i in (l2):
            if n == i:
                return True

l1 = [1,2,3]
l2 = [2,4,5]
print(superposicion(l1,l2))


def generar_n_char(n,c):
    i = str(n * c)
    return i

print(generar_n_char(5,"x"))

def histograma(lista1):
    for n in lista1:
        i = n * "*"
        print(f"{i}\n")
histograma([1,2,3])