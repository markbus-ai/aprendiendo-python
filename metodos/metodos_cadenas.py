# Definición de una cadena de texto
cadena = "Hola, mundo!"

# Imprimir la cadena original
print("Cadena original:", cadena)

# Método upper() - convierte la cadena a mayúsculas
cadena_mayusculas = cadena.upper()
print("Mayúsculas:", cadena_mayusculas)  # Output: HOLA, MUNDO!

# Método lower() - convierte la cadena a minúsculas
cadena_minusculas = cadena.lower()
print("Minúsculas:", cadena_minusculas)  # Output: hola, mundo!

# Método capitalize() - convierte la primera letra de la cadena a mayúscula
cadena_capitalizada = cadena.capitalize()
print("Capitalizada:", cadena_capitalizada)  # Output: Hola, mundo!

# Método title() - convierte la primera letra de cada palabra a mayúscula
cadena_titulada = cadena.title()
print("Titulada:", cadena_titulada)  # Output: Hola, Mundo!

# Método count() - cuenta la cantidad de ocurrencias de una subcadena
ocurrencias_o = cadena.count("o")
print("Cantidad de 'o':", ocurrencias_o)  # Output: 2

# Método replace() - reemplaza todas las ocurrencias de una subcadena por otra
cadena_reemplazada = cadena.replace("mundo", "amigo")
print("Reemplazada:", cadena_reemplazada)  # Output: Hola, amigo!

# Método split() - divide la cadena en una lista de subcadenas utilizando un separador
palabras = cadena.split(", ")
print("Lista de palabras:", palabras)  # Output: ['Hola', 'mundo!']

# Método join() - une una lista de subcadenas en una sola cadena utilizando un separador
nueva_cadena = "-".join(palabras)
print("Cadena unida:", nueva_cadena)  # Output: Hola-mundo!
