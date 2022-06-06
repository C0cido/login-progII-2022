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
        alta = ttk.Toplevel(title="Alta")
        alta.geometry("600x400")
        
        #variables
        varNombreProducto = ttk.StringVar(alta,"")
        varFechaLanzamiento = ttk.StringVar(alta,"")

            #funcion que permite agregar existencia de productos al inventario.
        def confirmarAlta():
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
                        nuevoProducto["Desarrollador"] = cmbDesarrollador.get()
                        nuevoProducto["FechaLanzamiento"] = varFechaLanzamiento.get()
                        nuevoProducto["Tipo"] = cmbTipo.get()
                        nuevoProducto["Categoria"] = cmbCategoria.get()
                        nuevoProducto["Cantidad"] = 0
                        nuevoProducto["Precio"] = 0
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
        ttk.Button(alta,text="Confirmar",command=confirmarAlta).place(x=210,y=330)

#crea top level, el cual permite modificar datos de productos existentes y que son seleccionado del treview.
def modificarProducto():
    if  tblInventario.item(tblInventario.focus(), 'text') != "":
        global modificar
        try:
            if modificar.state() == "normal":
                modificar.focus()
        except:
            modificar = ttk.Toplevel(title="Modificar")
            modificar.geometry("600x400")

        
            #variables
            global varProducto
            global varFecha
            global cmbCategoria
            global cmbDesarrollador
            global cmbTipo
            varProducto = ttk.StringVar(modificar,"")
            varFecha = ttk.StringVar(modificar,"")

                #funcion que permite modificar productos existentes en el inventario.
            def confirmarModificacion():
                if len(varProducto.get())>0 and  len(varFecha.get()) == 4  and cmbDesarrollador.get() != "" and cmbTipo.get() != "" and cmbCategoria.get() != "" :
                    if ms.askyesno("Atencion","¿Desea modificar el producto seleccionado?"):
                        lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")
                        for i in lstInventario:
                            if i["IDProducto"] == tblInventario.item(tblInventario.focus(), 'text'):
                                i["Producto"] = (varProducto.get()).upper()
                                i["FechaLanzamiento"] = varFecha.get()
                                i["Categoria"] = cmbCategoria.get()
                                i["Desarrollador"] = cmbDesarrollador.get()
                                i["Tipo"] = cmbTipo.get()
                        with open("archivosJSON/inventario.json","w") as archivo:
                            json.dump(lstInventario,archivo)
                        actualizarTabla(tblInventario)  
                        modificar.destroy()                   
                else:
                    ms.showerror("Error","La casilla no pueden estar vacias")
                    modificar.focus()
                            
                #nombre producto
            ttk.Label(modificar,text="Producto").place(x=20,y=20)
            ttk.Entry(modificar,textvariable=varProducto).place(x=210,y=20)

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
            ttk.Entry(modificar,textvariable=varFecha).place(x=210,y=260)

                #buton confirmar compra
            ttk.Button(modificar,text="Confirmar",command=confirmarModificacion).place(x=210,y=330)

            lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")
            for i in lstInventario:
                if i["IDProducto"] == tblInventario.item(tblInventario.focus(), 'text'):
                    varProducto.set(i["Producto"])
                    varFecha.set(i["FechaLanzamiento"])
                    cmbCategoria.set(i["Categoria"])
                    cmbDesarrollador.set(i["Desarrollador"])
                    cmbTipo.set(i["Tipo"])
        else:
            ms.showerror("Error","Por favor seleccione un elemento de la tabla")
#permite eliminar producto seleccionado en el treeview
def eliminarProducto():
    if  tblInventario.item(tblInventario.focus(), 'text') != "":
        if ms.askyesno("Atencion","¿Desea eliminar el producto seleccionado?"):
            lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")
            for i in lstInventario:
                if i["IDProducto"] == tblInventario.item(tblInventario.focus(), 'text'):
                    lstInventario.remove(i)
            with open("archivosJSON/inventario.json","w") as archivo:
                json.dump(lstInventario,archivo) 
            actualizarTabla(tblInventario)
    else:
        ms.showerror("Error","Por favor seleccione un elemento de la tabla")

#actualiza la tabla 
def actualizarTabla(tbl):
    for i in tbl.get_children():
        tbl.delete(i)
    lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")
    for i in lstInventario:
        tbl.insert("",ttk.END,text=i["IDProducto"],values=(i["Producto"],i["Desarrollador"],i["Tipo"],i["Precio"],i["Cantidad"]))

#estructura del menu de compras
def Deposito():
    menu = ttk.Window()
    menu.geometry("1200x500")
    menu.title("AMC STOCK")

    #label saludando al empleado
    ttk.Label(menu,text="Bienvenido").place(x=20,y=20)
    ttk.Label(menu,text="Inventario actual").place(x=20,y=60)

    #estructura de tabla(mostrar el inventario)
    global tblInventario
    tblInventario = ttk.Treeview(menu,columns=("col1","col2","col3","col4","col5"),selectmode="browse")
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

    #button alta producto
    btnAlta = ttk.Button(menu,text="Alta Producto",command=altaProducto,width=20)
    btnAlta.place(x=900,y=120)

    #button modificar producto
    global btnModificar
    btnModificar = ttk.Button(menu,text="Modificar Producto",command=modificarProducto,width=20)
    btnModificar.place(x=900,y=160)

    #button modificar producto
    global btnEliminar
    btnEliminar = ttk.Button(menu,text="Eliminar Producto",command=eliminarProducto,width=20)
    btnEliminar.place(x=900,y=200)

    #destruirPantalla()

    menu.mainloop()
Deposito()
