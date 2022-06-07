import json
import ttkbootstrap as ttk
import funciones as fn
from tkinter import messagebox as ms
import datetime as time


global lstCarrito
lstCarrito = []

    
#fn crea top level que permite agregar la informacion ha agregar en el carrito 
def agregarCarrito():
    if  tblInventario.item(tblInventario.focus(), 'text') != "":
        if ms.askyesno("Atencion","¿Desea agregar el producto seleccionado?"):
            global datos
            try:
                if datos.state() == "normal":
                    datos.focus()
            except:
                datos = ttk.Toplevel(title="Formulario")
                datos.geometry("600x400")
                

                #variables
                global varNombre
                varNombre = ttk.StringVar(datos,"")
                varCantidad = ttk.StringVar(datos,"0")
                varPrecio = ttk.StringVar(datos,"0")

                lstInventario =fn.abrirArchivo("archivosJSON/inventario.json")
                for i in lstInventario:
                    if i["IDProducto"]== tblInventario.item(tblInventario.focus(),"text"):
                        varNombre.set(i["Producto"])
                        varPrecio.set(i["Precio"])
                        stockActual = i["Cantidad"]
                
                def confirmarDatos():
                    if ((varCantidad.get()).isdigit()  and int(varCantidad.get()) > 0 and stockActual >= int(varCantidad.get())):
                        nuevoProducto = {}
                        nuevoProducto["IDProducto"] = tblInventario.item(tblInventario.focus(),"text")
                        nuevoProducto["Producto"] = varNombre.get()
                        nuevoProducto["Cantidad"] = int(varCantidad.get())
                        nuevoProducto["Precio"] = float(varPrecio.get())
                        lstCarrito.append(nuevoProducto)
                        actualizarTablaCarrito()
                        datos.destroy()
                    else:
                        #especiicar los errores
                        if ms.showerror("Error","La casillas no pueden estar vacias o los datos deben ser mayor a 0"):  datos.focus()
                    
                    #nombre
                ttk.Label(datos,text="Nombre").place(x=20,y=20)
                ttk.Entry(datos,textvariable=varNombre,state="disable").place(x=210,y=20) 

                    #precio
                ttk.Label(datos,text="Precio").place(x=20,y=80)
                ttk.Entry(datos,textvariable=varPrecio,state="disable").place(x=210,y=80)

                    #cantidad
                ttk.Label(datos,text="Cantidad").place(x=20,y=140)
                entCant=ttk.Entry(datos,textvariable=varCantidad)
                entCant.place(x=210,y=140)
                entCant.focus()
                                
                    #buton confirmar compra
                ttk.Button(datos,text="Confirmar",command=confirmarDatos).place(x=210,y=200)
    else:
        ms.showerror("Error","Por favor seleccione un elemento de la tabla")

#fn permite eliminar producto en el carrito
def eliminarCarrito():
    if  tblCarrito.item(tblCarrito.focus(), 'text') != "":
        if ms.askyesno("Atencion","¿Desea eliminar el producto seleccionado?"):
            for i in lstCarrito:
                if i["IDProducto"] == tblCarrito.item(tblCarrito.focus(), 'text'):
                    lstCarrito.remove(i)
            actualizarTablaCarrito()
    else:
        ms.showerror("Error","Por favor seleccione un elemento de la tabla")

#actualiza tabla
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
        if i["Cantidad"] > 0:
            tblInventario.insert("",ttk.END,text=i["IDProducto"],values=(i["Producto"],i["Desarrollador"],i["Precio"],i["Cantidad"]))


#fn que permite confirmar la compra y actualiza los datos en los respectivos archivos
def confirmarComprar():
    if len(tblCarrito.get_children()) > 0:
        lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")
        lstVenta = fn.abrirArchivo("archivosJSON/ventas.json")
        lstCarrito = []
        nuevaVenta = {}
        #Cambiar ganancia y proveedor hacer con un entry...
        cliente = "Cualquiera"
        total = 0
        for i in tblCarrito.get_children():
            producto = {}
            producto["IDProducto"] = tblCarrito.item(i)["text"]
            producto["Producto"] = tblCarrito.item(i)["values"][0]
            producto["Precio"] = float(tblCarrito.item(i)["values"][1])
            producto["Cantidad"] = int(tblCarrito.item(i)["values"][2])
            total += (float(tblCarrito.item(i)["values"][1]) * int(tblCarrito.item(i)["values"][2]))
            for j in lstInventario:
                if int(tblCarrito.item(i)["text"])== j["IDProducto"]:
                    j["Cantidad"] -= tblCarrito.item(i)["values"][2]
                    j["Precio"] = float(tblCarrito.item(i)["values"][1])
                    with open("archivosJSON/inventario.json","w") as archivo:
                        json.dump(lstInventario,archivo)
            lstCarrito.append(producto)
        nuevaVenta["IDVenta"] = fn.maximo(lstVenta,"IDVenta")
        nuevaVenta["Cliente"] = cliente
        nuevaVenta["TotalACobrar"] = total
        nuevaVenta["VentaRealizada"] = lstCarrito
        nuevaVenta["FechaCompra"] = 2022
        lstVenta.append(nuevaVenta)
        with open("archivosJSON/ventas.json","w") as venta:
            json.dump(lstVenta,venta)
        lstCarrito.clear()
        for i in tblCarrito.get_children():
            tblCarrito.delete(i)
        actualizarTablaInventario()
    else:
        ms.showerror("Error","No hay producto en el carrito")
#fn que crea la ventana principal
def Ventas():
    menu = ttk.Window()
    menu.geometry("1200x500")
    menu.title("AMC Ventas")

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
    tblInventario.heading("col3", anchor=ttk.CENTER, text="Precio")
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
    tblCarrito.place(x=650,y=120)

    #button alta producto
    btnAlta = ttk.Button(menu,text="Agregar Producto",command=agregarCarrito,width=20)
    btnAlta.place(x=650,y=80)

    #button modificar producto
    btnEliminar = ttk.Button(menu,text="Eliminar Producto",command=eliminarCarrito,width=20)
    btnEliminar.place(x=880,y=80)

    #button confirmar comprar
    btnConfirmar =ttk.Button(menu,text="Confirmar",command=confirmarComprar,width=20)
    btnConfirmar.place(x=780,y=425)

    menu.mainloop()
Ventas()