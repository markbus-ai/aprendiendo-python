def fibonacci_hasta(num):
    a = 0
    b = 1

    # Se recorren los números hasta el número máximo
    for _ in range(0,num):
        if a <= num:
            
    # Se muestra el primer número de Fibonacci
            print(a)

        # Se calcula el siguiente número de Fibonacci
            c = a + b

            # Se actualiza el valor de los dos primeros números
            a = b
            b = c
    

fibonacci_hasta(34)