# Imprimir los números del 1 al 10, pero salir del bucle cuando se encuentre el número 5
numero = 1
while True:
    print(numero)
    if numero == 5:
        break
    numero += 1


# Imprimir los números pares del 1 al 10, pero omitir los números pares divisibles por 3
numero = 1
while numero <= 10:
    if numero % 2 == 0 and numero % 3 == 0:
        continue
    print(numero)
    numero += 1
