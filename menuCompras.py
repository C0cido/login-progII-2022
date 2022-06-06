from faulthandler import disable
import json
import ttkbootstrap as ttk
import funciones as fn
from tkinter import messagebox as ms

lstCarrito = []

def datosCarrito(produc):
    global datos
    try:
        if datos.state() == "normal":
            datos.focus()
    except:
        datos = ttk.Toplevel(title="Formulario")
        datos.geometry("600x400")
        

        #variables
        varNombre = ttk.StringVar(datos,"")
        varCantidad = ttk.StringVar(datos,"0")
        varPrecio = ttk.StringVar(datos,"0")
        varNombre.set(produc)


        def confirmarDatos():
            if ((varCantidad.get()).isdigit() and (varPrecio.get()).isdigit() and int(varPrecio.get()) > 0 and int(varCantidad.get()) > 0):
                pass
            else:
                if ms.showerror("Error","La casillas no pueden estar vacias o los datos deben ser mayor a 0"):  datos.focus()
            
            #nombre producto
        ttk.Label(datos,text="Producto").place(x=20,y=20)
        ttk.Entry(datos,textvariable=varNombre,state="disable").place(x=210,y=20)

            #nombre desarrollador
        ttk.Label(datos,text="Cantidad").place(x=20,y=80)
        ttk.Entry(datos,textvariable=varCantidad).place(x=210,y=80)

            #combobox tipo producto
        ttk.Label(datos,text="Precio").place(x=20,y=140)
        ttk.Entry(datos,textvariable=varPrecio).place(x=210,y=140)


            #buton confirmar compra
        ttk.Button(datos,text="Confirmar",command=confirmarDatos).place(x=210,y=200)

def agregarCarrito():
    if  tblInventario.item(tblInventario.focus(), 'text') != "":
        if ms.askyesno("Atencion","¿Desea agregar el producto seleccionado?"):
            nombre = tblInventario.item(tblInventario.focus(),"values"[0])
            datosCarrito("jorge")
    else:
        ms.showerror("Error","Por favor seleccione un elemento de la tabla")

def eliminarCarrito():
    if  tblCarrito.item(tblCarrito.focus(), 'text') != "":
        if ms.askyesno("Atencion","¿Desea eliminar el producto seleccionado?"):
            for i in lstCarrito:
                if i["IDProducto"] == tblCarrito.item(tblCarrito.focus(), 'text'):
                    lstCarrito.remove(i)
            actualizarTablaCarrito()
    else:
        ms.showerror("Error","Por favor seleccione un elemento de la tabla")


def actualizarTablaCarrito():
    for i in tblCarrito.get_children():
        tblCarrito.delete(i)
    for i in lstCarrito:
        tblCarrito.insert("",ttk.END,text=i["IDProducto"],values=(i["Producto"],i["Precio"],i["Cantidad"]))

def actualizarTablaInventario():
    for i in tblInventario.get_children():
        tblInventario.delete(i)
    lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")
    for i in lstInventario:
        tblInventario.insert("",ttk.END,text=i["IDProducto"],values=(i["Producto"],i["Desarrollador"],i["Tipo"],i["Precio"],i["Cantidad"]))


def Deposito():
    menu = ttk.Window()
    menu.geometry("1200x500")
    menu.title("AMC Compras")

    #label saludando al empleado
    ttk.Label(menu,text="Bienvenido").place(x=20,y=20)
    ttk.Label(menu,text="Inventario actual").place(x=20,y=60)

    #estructura de tabla(mostrar el inventario)
    global tblInventario
    tblInventario = ttk.Treeview(menu,columns=("col1","col2","col3","col4"),selectmode="browse")
    tblInventario.column("#0", anchor=ttk.CENTER,width=50)
    tblInventario.column("col1", anchor=ttk.CENTER)
    tblInventario.column("col2", anchor=ttk.CENTER,width=150)
    tblInventario.column("col3", anchor=ttk.CENTER,width=70)
    tblInventario.column("col4", anchor=ttk.CENTER,width=100)
    tblInventario.heading("#0", anchor=ttk.CENTER, text="ID")
    tblInventario.heading("col1", anchor=ttk.CENTER, text="Producto")
    tblInventario.heading("col2", anchor=ttk.CENTER, text="Desarrollador")
    tblInventario.heading("col3", anchor=ttk.CENTER, text="Tipo")
    tblInventario.heading("col4", anchor=ttk.CENTER, text="Cantidad")
    tblInventario.place(x=20,y=120)
    actualizarTablaInventario()


    global tblCarrito
    tblCarrito = ttk.Treeview(menu,columns=("col1","col2","col3"),selectmode="browse")
    tblCarrito.column("#0", anchor=ttk.CENTER,width=50)
    tblCarrito.column("col1", anchor=ttk.CENTER)
    tblCarrito.column("col2", anchor=ttk.CENTER,width=100)
    tblCarrito.column("col3", anchor=ttk.CENTER,width=100)
    tblCarrito.heading("#0", anchor=ttk.CENTER, text="ID")
    tblCarrito.heading("col1", anchor=ttk.CENTER, text="Producto")
    tblCarrito.heading("col2", anchor=ttk.CENTER, text="Precio")
    tblCarrito.heading("col3", anchor=ttk.CENTER, text="Cantidad")
    tblCarrito.place(x=650,y=200)

    #Activar botones a traves de la seleccion del treeview

    #button alta producto
    btnAlta = ttk.Button(menu,text="Agregar Producto",command=agregarCarrito,width=20)
    btnAlta.place(x=700,y=120)

    #button modificar producto

    btnEliminar = ttk.Button(menu,text="Eliminar Producto",command=eliminarCarrito,width=20)
    btnEliminar.place(x=900,y=120)

    #destruirPantalla()

    menu.mainloop()
Deposito()