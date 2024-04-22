#slicing
cadena = "0123456789"
print(cadena[0:0])














import pandas as pd

#usando read_csv para leer el archivo csv
df = pd.read_csv("archivos/archivo.csv")
df2 = pd.read_csv("archivos/archivo.csv")

#mostrando solo la columna nombres
#obteniendo los datos de la columna nombre
nombres =df["nombre"]

#ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")

#ordeandolo de forma descendente
df_orden_descendente = df.sort_values("edad", ascending=False)

#concatenando los data frames
df_conca = pd.concat([df,df2])

#accediendo a la primeras 3 filas con head()
primeras_filas = df.head (3)
#accediendo a las últimas 3 filas con tail()
ultimas_filas = df.tail(3)
#accediendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape

#obteniendo data estadistica del data frame
df_info = df.describe()

#accediendo a un elem especifico del df
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a un elem especifico del df
elemento_especifico_loc = df.iloc[2,2]

#accediendo a todos los appelidos con iloc
apellidos = df.iloc[:,1]

#accediendo a las filas con mayor de 30
mayor_que_30 = df.iloc[df["edad"]>30,:]
