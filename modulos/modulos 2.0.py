#si el modulo estuviera dentro de una carpeta en la misma ruta:
#import funciones_buenas.saludar as m_saludar
import sys

sys.path.append("home/marcos/Escritorio/curso/curso de python/funciones_buenas")
import saludo as modulo_saludo
print(modulo_saludo.saludar ("Dalto")) 
