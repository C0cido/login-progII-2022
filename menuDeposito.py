import json
import ttkbootstrap as ttk
import funciones as fn
from tkinter import messagebox as ms

#crea top level, el cual permite agregar existencia de productos.
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

        #funcion que permite agregar existencia de productos al inventario.
        def confirmarCompra():
            alta.focus()
            if len(varNombreProducto.get())>0 and  len(varFechaLanzamiento.get()) == 4  and cmbDesarrollador.get() != "" and cmbTipo.get() != "" and cmbCategoria.get() != "" :
                #dar alta producto en inventario o sumarlo
                lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")
                if any((i["Producto"] == (varNombreProducto.get()).upper() and i["Desarrollador"] == cmbDesarrollador.get() and i["Tipo"] == cmbTipo.get() ) for i in lstInventario):
                    ms.showerror("Atencion","Ha ingresado un producto ya existente")
                else:
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
                    ms.showinfo("Operacion realizada","El registro de alta de producto se ha completado con exito")
                alta.focus()
                varNombreProducto.set("")
                varFechaLanzamiento.set("")
                cmbCategoria.set("")
                cmbDesarrollador.set("")
                cmbTipo.set("")
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


#crea top level, el cual permite modificar datos de productos existentes.
def modificarProducto():
    global modificar
    try:
        if modificar.state() == "normal":
            modificar.focus()
    except:
        modificar = ttk.Toplevel(title="")
        modificar.geometry("600x400")
        
        #variables
        varNombreProducto = ttk.StringVar(modificar,"")
        varFechaLanzamiento = ttk.StringVar(modificar,"")

        #funcion que permite modificar productos existentes en el inventario.
        def confirmarModificacion():
            pass

        #nombre producto
        ttk.Label(modificar,text="Producto").place(x=20,y=20)
        ttk.Entry(modificar,textvariable=varNombreProducto).place(x=210,y=20)

        #nombre desarrollador
        ttk.Label(modificar,text="Desarrollador").place(x=20,y=80)
        cmbDesarrollador = ttk.Combobox(modificar,state="readonly",values=("SONY","MICROSOFT","FROM_SOFTWARE","2K_INTERACTIVE","UBISOFT","VALVE","CAPCOM","RIOT GAMES","ELECTRONIC_ARTS"))
        cmbDesarrollador.place(x=210,y=80)

        #combobox tipo producto
        ttk.Label(modificar,text="Tipo").place(x=20,y=140)
        cmbTipo =ttk.Combobox(modificar,state="readonly",values=("Digital","Fisico"))
        cmbTipo.place(x=210,y=140)

        #combobox de categorias
        ttk.Label(modificar,text="Categorias").place(x=20,y=200)
        cmbCategoria = ttk.Combobox(modificar,state="readonly",values=("Terror","Deporte","Accion","FPS","RPG","Aventura"))
        cmbCategoria.place(x=210,y=200)

        #fecha lanzamiento producto
        ttk.Label(modificar,text="Fecha de Lanzamiento").place(x=20,y=260)
        ttk.Entry(modificar,textvariable=varFechaLanzamiento).place(x=210,y=260)


        #buton confirmar compra
        ttk.Button(modificar,text="Confirmar",command=confirmarModificacion).place(x=210,y=330)

#permite eliminar producto seleccionado en el treeview
def eliminarProducto():
    if ms.askyesno("Atencion","¿Desea eliminar el producto seleccionado?"):
        lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")
        for i in lstInventario:
            if i["IDProducto"] == tblInventario.item(tblInventario.focus(), 'text'):
                lstInventario.remove(i)
            with open("archivosJSON/inventario.json","w") as archivo:
                json.dump(lstInventario,archivo)
        actualizarTabla(tblInventario)



#actualiza la tabla 
def actualizarTabla(tbl):
    for i in tbl.get_children():
        tbl.delete(i)
    lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")
    for i in lstInventario:
        tbl.insert("",ttk.END,text=i["IDProducto"],values=(i["Producto"],i["Desarrollador"],i["Tipo"],i["Precio"],i["Cantidad"]))

#estructura del menu de compras
def menuDeposito():
    menu = ttk.Window()
    menu.geometry("1060x400")
    menu.title("AMC STOCK")

    #label saludando al empleado
    ttk.Label(text="Bienvenido").place(x=20,y=20)
    ttk.Label(text="Inventario actual").place(x=20,y=60)

    #estructura de tabla(mostrar el inventario)
    global tblInventario
    tblInventario = ttk.Treeview(columns=("col1","col2","col3","col4","col5"),selectmode="browse")
    tblInventario.column("#0", anchor=ttk.CENTER,width=50)
    tblInventario.column("col1", anchor=ttk.CENTER)
    tblInventario.column("col2", anchor=ttk.CENTER)
    tblInventario.column("col3", anchor=ttk.CENTER)
    tblInventario.column("col4", anchor=ttk.CENTER,width=100)
    tblInventario.column("col5", anchor=ttk.CENTER,width=100)
    tblInventario.heading("#0", anchor=ttk.CENTER, text="ID")
    tblInventario.heading("col1", anchor=ttk.CENTER, text="Producto")
    tblInventario.heading("col2", anchor=ttk.CENTER, text="Desarrollador")
    tblInventario.heading("col3", anchor=ttk.CENTER, text="Tipo")
    tblInventario.heading("col4", anchor=ttk.CENTER, text="Precio")
    tblInventario.heading("col5", anchor=ttk.CENTER, text="Cantidad")
    tblInventario.place(x=20,y=120)
    actualizarTabla(tblInventario)

    #Activar botones a traves de la seleccion del treeview
    def activarBotones(event):
        btnEliminar["state"]=ttk.NORMAL
        btnModificar["state"]= ttk.NORMAL
    tblInventario.bind("<<TreeviewSelect>>",activarBotones)
    
    

    #button alta producto
    btnAlta = ttk.Button(menu,text="Alta Producto",command=altaProducto,width=20)
    btnAlta.place(x=900,y=120)

    #button modificar producto
    btnModificar = ttk.Button(menu,text="Modificar Producto",command=modificarProducto,width=20,state="disable")
    btnModificar.place(x=900,y=160)

    #button modificar producto
    btnEliminar = ttk.Button(menu,text="Eliminar Producto",command=eliminarProducto,width=20,state="disable")
    btnEliminar.place(x=900,y=200)

    menu.mainloop()
menuDeposito()