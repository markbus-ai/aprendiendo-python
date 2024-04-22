import re

texto = '''1. hola alito como estas
            esta es la segunda linea de texto
            y esta la tercera'''

#busqueda simple
resultado = re.findall("alito",texto)

#\d -> busca digitos numericos del 0-9
resultado = re.findall(r"\d",texto)

#\D -> busca TODO MENOS digitos numericos del 0-9
resultado = re.findall(r"\D",texto)

#\w -> busca caracteres alfanumericos
resultado = re.findall(r"\w",texto)

#\W -> busca TODO MENOScaracteres alfanumericos
resultado = re.findall(r"\W",texto)

#\s -> busca espacios en blanco 
resultado = re.findall(r"\s",texto)

#\S -> busca TODO MENOS espacios en blanco 
resultado = re.findall(r"\S",texto)

#. busca TODO MENOS salto en linea
resultado = re.findall(r".",texto)

#\n busca salto en linea
resultado = re.findall(r"\n",texto)

#\ cancela todos los caracteres especiales que vengan despues del \
resultado = re.findall(r"\.",texto)

#armando una cadena que busque un numero seguido de un punto y un espacio en blanco
resultado = re.findall(r"\d\.\s",texto)

#^--> busca el comienzo busca de una linea
#flags=re.M activa buscar en multi lineas
resultado = re.findall(r"\^1.",texto, flags=re.M)

#$ busca el final de una linea
resultado = re.findall(r"$",texto)

#{n,m} busca  al menos n y como maximo m cantidad de veces el valor de la izquierda
resultado = re.findall(r"\d{3}",texto)

# | --> busca una cosa o otra
resultado = re.findall(r"\d{3}|Hola",texto)

print(resultado)
