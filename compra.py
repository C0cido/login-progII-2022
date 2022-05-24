import json
import ttkbootstrap as ttk
import funciones as fn

lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")

#estructura del menu de compras
def menuCompra():
    menuCompra = ttk.Window(themename="darkly")
    menuCompra.geometry("800x400")
    menuCompra.title("Sector deposito")
    ttk.Label(text="Bienvenido").place(x=20,y=20)
    tblInventario = ttk.Treeview(columns=("NombreProducto","StockProducto"))
    tblInventario.heading("#0", text="NombreProducto")
    tblInventario.heading("NombreProducto", text="NombreProducto")
    tblInventario.heading("StockProducto", text="StockProducto")
    tblInventario.place(x=20,y=60)





    menuCompra.mainloop()
menuCompra()