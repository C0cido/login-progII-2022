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
        alta = ttk.Toplevel(title="Alta de productos")
        alta.geometry("400x350")
        
        
        #variables
        varNombreProducto = ttk.StringVar(alta,"")
        varProveedor = ttk.StringVar(alta,"")
        varFechaCompra = ttk.StringVar(alta,"")
        varCantidad = ttk.StringVar(alta,"")
        varPrecio = ttk.StringVar(alta,"")

        def confirmarCompra():
            alta.focus()
            varFechaCompra.set(datetime.datetime.today())
            if len(varNombreProducto.get())>0 and  len(varProveedor.get())>0 and len(varFechaCompra.get())>0 and len(varCantidad.get())>0 and len(varPrecio.get())>0:
                if (varPrecio.get()).isdigit() and (varCantidad.get()).isdigit():
                    #registrar compra
                    lstCompra = fn.abrirArchivo("archivosJSON/compras.json")
                    nuevaCompra = {}
                    nuevaCompra["IDCompra"] = fn.maximo(lstCompra,"idCompra")
                    nuevaCompra["NombreProducto"] = (varNombreProducto.get()).upper()
                    nuevaCompra["cantProducto"] = int(varCantidad.get())
                    nuevaCompra["Precio"] = (float(varPrecio.get())).__round__(2)
                    nuevaCompra["NombreProveedor"] = varProveedor.get()
                    nuevaCompra["FechaCompra"] = varFechaCompra.get()
                    lstCompra.append(nuevaCompra)
                    with open("archivosJSON/compras.json","w") as compra:
                        json.dump(lstCompra,compra)

                    #dar alta producto en inventario
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
                    ms.showinfo("Operacion realizada","el registro de compra se realizado con existo")
                    for i in tblInventario.get_children():
                        tblInventario.delete(i)

                    actualizarTabla(tblInventario)
                    varCantidad.set("")
                    varFechaCompra.set("")
                    varNombreProducto.set("")
                    varPrecio.set("")
                    varProveedor.set("")
                else:
                    if ms.showerror("Error","La cantidad de productos o el precio solo puede ser numerica"):
                        alta.focus()
            else:   
                if ms.showerror("Error","La casillas no pueden estar vacias"):
                    alta.focus()

        #nombre proveedor
        ttk.Label(alta,text="Proveedor").place(x=20,y=20)
        entProv = ttk.Entry(alta,textvariable=varProveedor)
        entProv.place(x=150,y=20)
        entProv.focus()

        #nombre producto
        ttk.Label(alta,text="Producto").place(x=20,y=60)
        ttk.Entry(alta,textvariable=varNombreProducto).place(x=150,y=60)

        #cantidad producto
        ttk.Label(alta,text="Cant. Producto").place(x=20,y=100)
        ttk.Entry(alta,textvariable=varCantidad).place(x=150,y=100)

        #precio total
        ttk.Label(alta,text="Precio").place(x=20,y=140)
        ttk.Entry(alta,textvariable=varPrecio).place(x=150,y=140)

        #buton confirmar compra
        ttk.Button(alta,text="Confirmar",command=confirmarCompra).place(x=150,y=200)

def actualizarTabla(tbl):
    lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")
    for i in lstInventario:
        tbl.insert("",ttk.END,text=i["IDProducto"],values=(i["NombreProducto"],i["CantProducto"]))

#estructura del menu de compras
def menuCompras():
    menu = ttk.Window(themename="darkly")
    menu.geometry("850x500")
    menu.title("Sector compras")

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
    btnAlta = ttk.Button(menu,text="Alta de productos",command=altaProducto)
    btnAlta.place(x=650,y=120)

    menu.mainloop()
menuCompras()