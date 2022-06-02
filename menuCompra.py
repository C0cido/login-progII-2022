import json
import ttkbootstrap as ttk
import funciones as fn
from tkinter import messagebox as ms
import datetime

#crea top level, el cual permite agregar, modificar, eliminar productos
def altaProducto():
    global alta
    try:
        if alta.state() == "normal":
            alta.focus()
    except:
        alta = ttk.Toplevel(title="")
        alta.geometry("600x400")
        
        #variables
        varNombreProducto = ttk.StringVar(alta,"")
        varProveedor = ttk.StringVar(alta,"")
        varCantidad = ttk.StringVar(alta,"")
        varPrecio = ttk.StringVar(alta,"")

        #funcion que permite agregar cantidad de productos a la lista compra y inventario, y si estan agregando alguno repetido, se lo suma a la lista de inventario
        def confirmarCompra():
            alta.focus()
            if len(varNombreProducto.get())>0 and  len(varProveedor.get())>0  and len(varCantidad.get())>0 and len(varPrecio.get())>0:
                if (varPrecio.get()).isdigit() and (varCantidad.get()).isdigit():
                    #registrar compra
                    lstCompra = fn.abrirArchivo("archivosJSON/compras.json")
                    nuevaCompra = {}
                    nuevaCompra["IDCompra"] = fn.maximo(lstCompra,"idCompra")
                    nuevaCompra["NombreProducto"] = (varNombreProducto.get()).upper()
                    nuevaCompra["cantProducto"] = int(varCantidad.get())
                    nuevaCompra["Precio"] = (float(varPrecio.get())).__round__(2)
                    nuevaCompra["NombreProveedor"] = varProveedor.get()
                    nuevaCompra["FechaCompra"] = str(datetime.datetime.today())
                    lstCompra.append(nuevaCompra)
                    with open("archivosJSON/compras.json","w") as compra:
                        json.dump(lstCompra,compra)

                    #dar alta producto en inventario o sumarlo
                    lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")
                    repetido = False
                    for i in lstInventario:
                        if i["NombreProducto"] == (varNombreProducto.get()).upper():
                            repetido = True
                            i["CantProducto"] += int(varCantidad.get())
                    if repetido == False:
                        nuevoProducto = {}
                        nuevoProducto["IDProducto"] = fn.maximo(lstInventario,"IDProducto")
                        nuevoProducto["NombreProducto"] = (varNombreProducto.get()).upper()
                        nuevoProducto["CantProducto"] = int(varCantidad.get())
                        lstInventario.append(nuevoProducto)
                    with open("archivosJSON/inventario.json","w") as inventario:
                        json.dump(lstInventario,inventario)
                    actualizarTabla(tblInventario)
                    ms.showinfo("Operacion realizada","el registro de compra se realizado con existo")
                    varCantidad.set("")
                    varNombreProducto.set("")
                    varPrecio.set("")
                    varProveedor.set("")
                else:
                    if ms.showerror("Error","La cantidad de productos o el precio solo puede ser numerica"):    alta.focus()
            else:   
                if ms.showerror("Error","La casillas no pueden estar vacias"):  alta.focus()

        #nombre proveedor
        ttk.Label(alta,text="Proveedor").place(x=20,y=20)
        ttk.Combobox(alta,values=("SONY","MICROSOFT","FROM_SOFTWARE","2K_INTERACTIVE","UBISOFT","VALVE","CAPCOM","RIOT GAMES","ELECTRONIC_ARTS")).place(x=210,y=20)

        #nombre producto
        ttk.Label(alta,text="Producto").place(x=20,y=80)
        ttk.Entry(alta,textvariable=varNombreProducto).place(x=210,y=80)

        #cantidad producto
        ttk.Label(alta,text="Fecha de Lanzamiento").place(x=20,y=140)
        ttk.Entry(alta,textvariable=varCantidad).place(x=210,y=140)

        #combobox tipo
        ttk.Label(alta,text="Tipo").place(x=20,y=220)
        ttk.Combobox(alta,values=("Digital","Fisico")).place(x=210,y=220)

        #combobox de categorias
        ttk.Label(alta,text="Categorias").place(x=20,y=280)
        ttk.Combobox(alta,values=("Terror","Deporte","Accion","FPS","RPG","Aventura")).place(x=210,y=280)

        #buton confirmar compra
        ttk.Button(alta,text="Confirmar",command=confirmarCompra).place(x=210,y=333)


def actualizarTabla(tbl):
    for i in tbl.get_children():
                        tbl.delete(i)
    lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")
    for i in lstInventario:
        tbl.insert("",ttk.END,text=i["IDProducto"],values=(i["NombreProducto"],i["CantProducto"]))

#estructura del menu de compras
def menuCompras():
    try:
        menu = ttk.Window()
    except:
        menu = ttk.Window()
    menu.geometry("850x500")
    menu.title("AMC STOCK")

    #label saludando al empleado
    ttk.Label(text="Bienvenido").place(x=20,y=20)
    ttk.Label(text="Inventario actual").place(x=20,y=60)

    #estructura de tabla(mostrar el inventario)
    global tblInventario
    tblInventario = ttk.Treeview(columns=("col1","col2"))
    tblInventario.column("#0", anchor=ttk.CENTER)
    tblInventario.column("col1", anchor=ttk.CENTER)
    tblInventario.column("col2", anchor=ttk.CENTER)
    tblInventario.heading("#0", anchor=ttk.CENTER, text="IDProducto")
    tblInventario.heading("col1", anchor=ttk.CENTER, text="NombreProducto")
    tblInventario.heading("col2", anchor=ttk.CENTER, text="StockProducto")
    tblInventario.place(x=20,y=120)
    actualizarTabla(tblInventario)

    #boton alta producto
    btnAlta = ttk.Button(menu,text="AGREGAR AL STOCK",command=altaProducto)
    btnAlta.place(x=650,y=120)

    menu.mainloop()
menuCompras()