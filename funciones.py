import json

def abrirArchivo(archivo):
    try:
        with open(archivo):
            lst = json.load(archivo)
    except:
        lst = []
    return lst