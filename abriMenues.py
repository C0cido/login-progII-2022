import json
from menuCompra import menuCompras
from funciones import abrirArchivo

def buscarEmpleado(id):
    encontrado = False
    lstEmpleado = abrirArchivo("archivosJSON/empleados.json")
    for i in lstEmpleado:
        if i["IDUsuario"] == id:
            if i["Sector"] == "Compras":
                menuCompras()