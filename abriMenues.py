from menuDeposito import menuDeposito
from funciones import abrirArchivo

def buscarEmpleado(id):
    lstEmpleado = abrirArchivo("archivosJSON/empleados.json")
    for i in lstEmpleado:
        if i["IDUsuario"] == id:
            if i["Sector"] == "Compras":
                menuDeposito()