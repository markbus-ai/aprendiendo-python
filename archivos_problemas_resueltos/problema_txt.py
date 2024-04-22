#2 listas una con con nombre otra con appelidos
nombres = ["lucas","marcos","juan","alondra"]
apellidos = ["rodriguez","bustos","fernandez","sanz"]

with open("archivos_problemas_resueltos/nombres_y_appellidos.txt","w") as arch:
    arch.writelines("los datos son: \n")
    for n,a in zip(nombres,apellidos):
        arch.writelines(f"Nombre: {n}\nApellido:{a}\n--------------\n")