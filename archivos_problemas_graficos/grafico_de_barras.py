import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("archivos_problemas_graficos/cofla_ingresos.csv")
#creando el grafico
sns.barplot(x="ingresos",y="fuente", data=df)
#creando un punto en el momento de mas pedos

#obteniendo el total 
total = df["ingresos"].sum()

print(total)


#mostrando el grafico|
plt.show()