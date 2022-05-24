
import json
import ttkbootstrap as ttk
import funciones as fn


def altaProducto():
    pass

def actualizarTabla(tbl):
    lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")
    for i in lstInventario:
        tbl.insert("",ttk.END,text=i["idProducto"],values=(i["nombreProducto"],i["stockProducto"]))

#estructura del menu de compras
def menuInventario():
    menu = ttk.Window(themename="darkly")
    menu.geometry("800x400")
    menu.title("Sector deposito")

    #label saludando al empleado
    ttk.Label(text="Bienvenido").place(x=20,y=20)

    #estructura de tabla(mostrar el inventario)
    tblInventario = ttk.Treeview(columns=("col1","col2"))
    tblInventario.column("#0", anchor=ttk.CENTER)
    tblInventario.column("col1", anchor=ttk.CENTER)
    tblInventario.column("col2", anchor=ttk.CENTER)
    tblInventario.heading("#0", anchor=ttk.CENTER, text="IdProducto")
    tblInventario.heading("col1", anchor=ttk.CENTER, text="NombreProducto")
    tblInventario.heading("col2", anchor=ttk.CENTER, text="StockProducto")
    tblInventario.place(x=20,y=60)
    actualizarTabla(tblInventario)

    #boton alta producto
    btnAlta = ttk.Button(menu,text="Alta Producto",command=altaProducto)
    btnAlta.place(x=650,y=60)

    menu.mainloop()
menuInventario()