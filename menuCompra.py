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
        varFechaLanzamiento = ttk.StringVar(alta,"")
        #funcion que permite agregar cantidad de productos a la lista compra y inventario, y si estan agregando alguno repetido, se lo suma a la lista de inventario
        def confirmarCompra():
            alta.focus()
            if len(varNombreProducto.get())>0 and  len(varFechaLanzamiento.get()) == 4  and cmbDesarrollador.get() != "" and cmbTipo.get() != "" and cmbCategoria.get() != "" :
                #dar alta producto en inventario o sumarlo
                lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")
                nuevoProducto = {}
                nuevoProducto["IDProducto"] = fn.maximo(lstInventario,"IDProducto")
                nuevoProducto["Producto"] = (varNombreProducto.get()).upper()
                nuevoProducto["Cantidad"] = 0
                nuevoProducto["Precio"] = 0
                nuevoProducto["Desarrollador"] = cmbDesarrollador.get()
                nuevoProducto["Tipo"] = cmbTipo.get()
                nuevoProducto["Categoria"] = cmbCategoria.get()
                lstInventario.append(nuevoProducto)
                with open("archivosJSON/inventario.json","w") as inventario:
                    json.dump(lstInventario,inventario)
                actualizarTabla(tblInventario)
                ms.showinfo("Operacion realizada","el registro de compra se realizado con existo")
                varNombreProducto.set("")
                varFechaLanzamiento.set("")
            else:   
                if ms.showerror("Error","La casillas no pueden estar vacias"):  alta.focus()

        #nombre producto
        ttk.Label(alta,text="Producto").place(x=20,y=20)
        ttk.Entry(alta,textvariable=varNombreProducto).place(x=210,y=20)

        #nombre desarrollador
        ttk.Label(alta,text="Desarrollador").place(x=20,y=80)
        cmbDesarrollador = ttk.Combobox(alta,state="readonly",values=("SONY","MICROSOFT","FROM_SOFTWARE","2K_INTERACTIVE","UBISOFT","VALVE","CAPCOM","RIOT GAMES","ELECTRONIC_ARTS"))
        cmbDesarrollador.place(x=210,y=80)

        #combobox tipo producto
        ttk.Label(alta,text="Tipo").place(x=20,y=140)
        cmbTipo =ttk.Combobox(alta,state="readonly",values=("Digital","Fisico"))
        cmbTipo.place(x=210,y=140)

        #combobox de categorias
        ttk.Label(alta,text="Categorias").place(x=20,y=200)
        cmbCategoria = ttk.Combobox(alta,state="readonly",values=("Terror","Deporte","Accion","FPS","RPG","Aventura"))
        cmbCategoria.place(x=210,y=200)

        #fecha lanzamiento producto
        ttk.Label(alta,text="Fecha de Lanzamiento").place(x=20,y=260)
        ttk.Entry(alta,textvariable=varFechaLanzamiento).place(x=210,y=260)


        #buton confirmar compra
        ttk.Button(alta,text="Confirmar",command=confirmarCompra).place(x=210,y=330)


def actualizarTabla(tbl):
    for i in tbl.get_children():
        tbl.delete(i)
    lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")
    for i in lstInventario:
        tbl.insert("",ttk.END,text=i["IDProducto"],values=(i["Producto"],i["CantProducto"]))

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
    tblInventario = ttk.Treeview(columns=("col1","col2","col3","col4"))
    tblInventario.column("#0", anchor=ttk.CENTER)
    tblInventario.column("col1", anchor=ttk.CENTER)
    tblInventario.column("col2", anchor=ttk.CENTER)
    tblInventario.heading("#0", anchor=ttk.CENTER, text="IDProducto")
    tblInventario.heading("col1", anchor=ttk.CENTER, text="Producto")
    tblInventario.heading("col2", anchor=ttk.CENTER, text="Desarrollador")
    tblInventario.place(x=20,y=120)
    actualizarTabla(tblInventario)

    #boton alta producto
    btnAlta = ttk.Button(menu,text="AGREGAR AL STOCK",command=altaProducto)
    btnAlta.place(x=645,y=120)

    menu.mainloop()
menuCompras()