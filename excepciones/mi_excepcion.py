#creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"cometiste el siguiente error: {err}")

#lanzandola
raise MiExcepcion("que boludo")


#manejandola
try:
    
    raise MiExcepcion("que boludo")
except:
    print("como vas a cometer ese error")