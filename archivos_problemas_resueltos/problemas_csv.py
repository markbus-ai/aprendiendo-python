import pandas as pd

df = pd.read_csv("archivos_problemas_resueltos/archivo.csv")

#convertimos una columna en string
#df['Edad'] = df['Edad'].astype(str)


df['Nombre'].replace('marcos','Marcos')
print(df['Nombre'])

#borra las filas con datos faltante
df = df.dropna()

#eliminando las filas repetidas
df = df.drop_duplicates()

#creando un csv con el data frame resultante(limpio)
df.to_csv("archivos_problemas_resueltos/archivo_limpios.csv")
