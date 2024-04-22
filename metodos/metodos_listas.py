# Definición de una lista
mi_lista = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Imprimir la lista original
print("Lista original:", mi_lista)

# Método append() - agrega un elemento al final de la lista
mi_lista.append(8)
print("Lista después de append(8):", mi_lista)  # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5, 8]

# Método extend() - agrega los elementos de otra lista al final de la lista actual
mi_lista.extend([7, 9, 3])
print("Lista después de extend([7, 9, 3]):", mi_lista)  # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5, 8, 7, 9, 3]

# Método insert() - inserta un elemento en una posición específica
mi_lista.insert(0, 0)
print("Lista después de insert(0, 0):", mi_lista)  # Output: [0, 3, 1, 4, 1, 5, 9, 2, 6, 5, 8, 7, 9, 3]

# Método remove() - elimina la primera ocurrencia de un elemento específico
mi_lista.remove(5)
print("Lista después de remove(5):", mi_lista)  # Output: [0, 3, 1, 4, 1, 9, 2, 6, 5, 8, 7, 9, 3]

# Método pop() - elimina y devuelve el elemento en la posición dada (o el último si no se especifica)
elemento_eliminado = mi_lista.pop(2)
print("Elemento eliminado con pop(2):", elemento_eliminado)  # Output: 1
print("Lista después de pop(2):", mi_lista)  # Output: [0, 3, 4, 1, 9, 2, 6, 5, 8, 7, 9, 3]

# Método index() - devuelve el índice de la primera ocurrencia de un elemento
indice = mi_lista.index(9)
print("Índice de la primera ocurrencia de 9:", indice)  # Output: 4

# Método count() - cuenta la cantidad de ocurrencias de un elemento en la lista
ocurrencias_3 = mi_lista.count(3)
print("Cantidad de ocurrencias de 3:", ocurrencias_3)  # Output: 2

# Método sort() - ordena los elementos de la lista
mi_lista.sort()
print("Lista ordenada:", mi_lista)  # Output: [0, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 9]

# Método reverse() - invierte el orden de los elementos en la lista
mi_lista.reverse()
print("Lista invertida:", mi_lista)  # Output: [9, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 0]
