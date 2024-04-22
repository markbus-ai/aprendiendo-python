import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("archivos_problemas_graficos/grafico_bigote_de_gato.py")
#creando el grafico
sns.barplot(x="categoria",y="valor", data=df)
#creando un punto en el momento de mas pedos


#mostrando el grafico|
plt.show()