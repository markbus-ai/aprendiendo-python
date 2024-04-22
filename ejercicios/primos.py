def numeros_primos(n):
    for i in range(2,n-1):
        if i % n == 0: 
            return False
    return True
    

def primos_hasta(num):
    primos = []
    for i in range(2,num+1):
        resultado = numeros_primos(i)
        if resultado == True: primos.append(i)
    return primos


resultado = primos_hasta(13)
print(resultado)