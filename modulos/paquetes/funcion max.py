def maximo(a,b,c):
    if c < a > b :
        return a
    elif b > c:
        return b
    else:
        return c

# print(maximo(8,9,7))


def Vocal(L):
    if L == "a" or L == "A":
        print(f"{L} es una vocal")
    elif L == "e" or L == "E":
        print(f"{L} es una vocal")
    elif L == "i" or L == "I":
        print(f"{L} es una vocal")
    elif L == "o" or L == "O":
        print(f"{L} es una vocal")
    elif L == "u" or L == "U":
        print(f"{L} es una vocal")
    else: print(f"{L} no es una vocal")


# print(Vocal("A"))

def sum(lista):
    resultado = 0
    for n in lista:
        resultado = resultado + (n)
        
    print (resultado)



#sum([1,2,-1])


def multi(lista):
    resultado = lista[0]
    for n in lista:
        resultado *= n
        
    print (resultado)


multi([1,2,3])
