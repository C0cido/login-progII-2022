import json

def abrirArchivo(archivo):
    try:
        with open(archivo) as archi:
            lst = json.load(archi)
    except:
        lst = []
    return lst