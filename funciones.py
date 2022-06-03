import json

def abrirArchivo(archivo):
    try:
        with open(archivo) as archi:
            lst = json.load(archi)
    except:
        lst = []
    return lst

def maximo(lst,clave):
    max = -1
    try:
        for i in lst:
            if i[clave] > max:
                max = i[clave]
    except:
        max = -1
    return max + 1




            