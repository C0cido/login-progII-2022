import json
import ttkbootstrap as ttk
import funciones as fn
from tkinter import messagebox as ms
import datetime 


global lstCarrito
lstCarrito = []
 
def agregarCarrito():                                                                           #Función para crear TopLevel y agregar información en el carrito
    if  tblInventario.item(tblInventario.focus(), 'text') != "":                                #Pedir que seleccione un elemento de la tabla inventario
        if ms.askyesno("Atencion","¿Desea agregar el producto seleccionado?"):                  #Ventana si/no para agregar el producto seleccionado
            global datos                                                                        #Hace global el TopLevel datos
            try:
                if datos.state() == "normal":
                    datos.focus()                                                               #Si está abierto, la fokusea. Sino la crea
            except:
                datos = ttk.Toplevel(title="Formulario")
                datos.geometry("600x400")                                                       #Crear el TopLevel "datos" con su tamaño
                

                #variables
                global varNombre                                                                #Se hace global la variable varNombre
                varNombre = ttk.StringVar(datos,"")
                varCantidad = ttk.StringVar(datos,"0")
                varPrecio = ttk.StringVar(datos,"0")                                            #Se especifica los tipos de variable y se los usa en el toplevel "datos"

                lstInventario =fn.abrirArchivo("archivosJSON/inventario.json")                  #Crea un lista en la que carga la información del json de inventario a través de la fn "abrirArchivo"
                for i in lstInventario:                                                         #Recorre la lista de inventario
                    if i["IDProducto"]== tblInventario.item(tblInventario.focus(),"text"):      #La clave IDProducto debe ser igual al ID del elemento seleccionado de la tabla
                        varNombre.set(i["Producto"])                                            #Se carga el nombre del producto en la variable "varNombre"
                
                def confirmarDatos():                                                           #Función para validar los datos
                    if ((varCantidad.get()).isdigit() and (varPrecio.get()).isdigit() and int(varPrecio.get()) > 0 and int(varCantidad.get()) > 0):     #La cantidad y precio deben ser números mayores a 0.
                        nuevoProducto = {}
                        nuevoProducto["IDProducto"] = tblInventario.item(tblInventario.focus(),"text")
                        nuevoProducto["Producto"] = varNombre.get()
                        nuevoProducto["Cantidad"] = int(varCantidad.get())
                        nuevoProducto["Precio"] = float(varPrecio.get())                                                                                #Se crea el nuevo producto con sus claves
                        lstCarrito.append(nuevoProducto)                                                                                                #Se agrega el nuevo producto al carrito
                        actualizarTablaCarrito()                                                                                                        #Se actualiza la tabla
                        datos.destroy()                                                                                                                 #Se hace un destroy del TopLevel
                    else:
                        if ms.showerror("Error","La casillas no pueden estar vacias o los datos deben ser mayor a 0"):  datos.focus()                   #Si las casillas están vacías, dar un msg de aviso
                    
                    #nombre
                ttk.Label(datos,text="Nombre").place(x=20,y=20)
                ttk.Entry(datos,textvariable=varNombre,state="disable").place(x=210,y=20)  
                    #cantidad
                ttk.Label(datos,text="Cantidad Comprada").place(x=20,y=80)
                entCant=ttk.Entry(datos,textvariable=varCantidad)
                entCant.place(x=210,y=80)
                entCant.focus()


                    #precio
                ttk.Label(datos,text="Precio de Compra").place(x=20,y=140)
                ttk.Entry(datos,textvariable=varPrecio).place(x=210,y=140)

                    #buton confirmar compra
                ttk.Button(datos,text="Confirmar",command=confirmarDatos).place(x=210,y=200)
    else:
        ms.showerror("Error","Por favor seleccione un elemento de la tabla")                                                                            #Si no selecciona un elemento, avisar que debe seleccionar uno


def eliminarCarrito():                                                                                                                                  #Función para eliminar productos del carrito
    if  tblCarrito.item(tblCarrito.focus(), 'text') != "":                                                                                              #Primero, se debe seleccionar un producto del carrito
        if ms.askyesno("Atencion","¿Desea eliminar el producto seleccionado?"):                                                                         #Preguntar si/no para eliminar el producto del carrito
            for i in lstCarrito:
                if i["IDProducto"] == tblCarrito.item(tblCarrito.focus(), 'text'):
                    lstCarrito.remove(i)                                                                                                                #Recorrer el carrito y para remover el elemento por coincidencia de ID.
            actualizarTablaCarrito()
    else:
        ms.showerror("Error","Por favor seleccione un elemento de la tabla")                                                                            #Si no selecciona un elemento, avisar que debe seleccionar uno o varios.

def actualizarTablaCarrito():                                                                                                                           #Función para actualizar el carrito
    for i in tblCarrito.get_children():
        tblCarrito.delete(i)                                                                                                                            #Se recorre el carrito y borra todos los productos de la tabla
    suma = 0                                                                                                                                            #Se inicia una variable "suma" en la cual se va a sumar el precio segun la cantidad de productos
    for i in lstCarrito:
        tblCarrito.insert("",ttk.END,text=i["IDProducto"],values=(i["Producto"],i["Precio"],i["Cantidad"]))                                             #Se actualiza el carrito insertando los productos con sus claves y se suman los precios
        suma += i["Precio"]
    varTotal.set(suma)                                                                                                                                  #Se asigna la el resultado de la suma a la variable varTotal

def actualizarTablaInventario():                                                                                                                        #Función para actualizar el inventario
    for i in tblInventario.get_children():                                                                                                              
        tblInventario.delete(i)                                                                                                                         #Se recorre el inventario y borra todos los productos de la tabla
    lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")                                                                                     #Se abre el archivo de inventario y se carga en la lista "lstInventario"
    for i in lstInventario:
        tblInventario.insert("",ttk.END,text=i["IDProducto"],values=(i["Producto"],i["Desarrollador"],i["Precio"],i["Cantidad"]))                       #Se recorre la lista y se inserta en la tabla los productos con sus claves y valores


def confirmarComprar():                                                                                                                                     #Función para validar la compra y actualizar los datos en los archivos
    if len(tblCarrito.get_children()) > 0 and cmbMetodoPago.get() != "" and cmbProveedor != "":                                                             #Se pide que el carrito no esté vacio, el método de pago y el proveedor
        if ms.askyesno("Atención","¿Desea confirmar la compra?"):                                                                                           #Se pregunta si/no para confirmar compra
            lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")                                                                                 #Se carga los datos del json de inventario en la lista de inventario
            lstCompra = fn.abrirArchivo("archivosJSON/compras.json")                                                                                        #Se carga los datos del json de compras en la lista de compras
            lstCarrito = []                                                                                                                                 #Se inicia lstCarrito como lista vacía por cada producto a comprar
            nuevaCompra = {}                                                                                                                                #Se inicia la nueva compra como diccionario vacío
            #Cambiar ganancia y proveedor hacer con un entry...
            for i in tblCarrito.get_children():
                producto = {}
                producto["IDProducto"] = tblCarrito.item(i)["text"]
                producto["Producto"] = tblCarrito.item(i)["values"][0]
                producto["Precio"] = (float(tblCarrito.item(i)["values"][1])).__round__(2)
                producto["Cantidad"] = int(tblCarrito.item(i)["values"][2])                                                                                 #Se recorre el carrito para agregar el producto a comprar con sus claves y valores
                for j in lstInventario:                                                                                                                     #Se recorre la lista de inventario
                    if int(tblCarrito.item(i)["text"])== j["IDProducto"]:                                                                                   #Si el ID del producto en el carrito coincide con el ID del producto en Inventario.
                        j["Cantidad"] += tblCarrito.item(i)["values"][2]                                                                                    
                        j["Precio"] = ((float(tblCarrito.item(i)["values"][1])/int(tblCarrito.item(i)["values"][2]))*(1+j["Ganancias"]/100)).__round__(2)   #Se suma las cantidades, se saca el precio unitario y el porcentaje de ganancia para guardar todo en el json de inventario 
                        with open("archivosJSON/inventario.json","w") as archivo:
                            json.dump(lstInventario,archivo)
                lstCarrito.append(producto)                                                                                                                 #Se carga el producto en el json de inventario y en el carrito
            nuevaCompra["IDCompra"] = fn.maximo(lstCompra,"IDCompra")
            nuevaCompra["Proveedor"] = cmbProveedor.get()
            nuevaCompra["TotalPagar"] = (float(varTotal.get())).__round__(2)
            nuevaCompra["MetodoPago"] = cmbMetodoPago.get()
            nuevaCompra["CompraRealizada"] = lstCarrito
            nuevaCompra["FechaCompra"] = datetime.datetime.strftime(datetime.datetime.now(),'%d/%m/%Y')
            lstCompra.append(nuevaCompra)                                                                                                                   #Se asigna valores a las claves de la nueva compra
            with open("archivosJSON/compras.json","w") as compra:
                json.dump(lstCompra,compra)                                                                                                                 #Se registra la nueva compra en el json de compras
            lstCarrito.clear()
            varBuscador.set("")
            cmbMetodoPago.set("")
            cmbProveedor.set("")
            varTotal.set("")                                                                                                                                #Se hace un clean de todo 
            for i in tblCarrito.get_children():
                tblCarrito.delete(i)
            actualizarTablaInventario()                                                                                                                     #Se limpia el TreeView del carrito
            ms.showinfo("Operacion Realizada","La compra se realizado con exito")
    else:
        if len(tblCarrito.get_children()) <= 0:                                                                                                             #Avisar que no hay productos en el carrito
            ms.showerror("Error","No hay producto en el carrito")
        elif cmbMetodoPago.get() == "" or cmbProveedor == "":                                                                                               #Avisar que no se seleccionó método de pago o proveedor
            ms.showerror("Error","El metodo de pago y el proveedor deben estar seleccionados")

#fn que crea la ventana principal
def Compras(menu):
    menu.geometry("1200x700")
    menu.title("AMC Compras")

    global varTotal
    varTotal = ttk.StringVar(menu,"0")
    global varBuscador
    varBuscador = ttk.StringVar(menu,"")

    #label saludando al empleado
    ttk.Label(menu,text="Bienvenido").place(x=20,y=0)
    ttk.Label(menu,text="Inventario actual").place(x=20,y=40)

    #funcion para el buscador
    def buscadorNombre(event):                                                                                                                  #Función para buscar nombre de producto
        lstInventario = fn.abrirArchivo("archivosJSON/inventario.json")                                                                         #Se abre el json de inventario
        if varBuscador.get() != "":                                                                                                             #Se debe escribir en el buscador
            for i in tblInventario.get_children():
                tblInventario.delete(i)                                                                                                         #Borrar todos los productos
            for i in lstInventario:
                if (varBuscador.get()).upper() in i["Producto"]:
                    tblInventario.insert("",ttk.END,text=i["IDProducto"],values=(i["Producto"],i["Desarrollador"],i["Precio"],i["Cantidad"]))   #Mostrar solo el producto que coincida o incluya en el nombre lo escrito en el buscador
        else:
            for i in tblInventario.get_children():
                tblInventario.delete(i)
            for i in lstInventario:
                tblInventario.insert("",ttk.END,text=i["IDProducto"],values=(i["Producto"],i["Desarrollador"],i["Precio"],i["Cantidad"]))       #Si no se escribe nada en el buscador, se muestra todo el listado de productos

    #buscador
    entBuscador = ttk.Entry(menu,textvariable=varBuscador,width=50)
    entBuscador.place(x=20,y=80)
    entBuscador.insert(0,"Realize una busqueda por nombre de producto")
    entBuscador.bind('<FocusIn>',lambda event: entBuscador.delete(0,"end") if varBuscador.get() == "Realize una busqueda por nombre de producto" else None)
    entBuscador.bind('<FocusOut>',lambda event: entBuscador.insert(0,"Realize una busqueda por nombre de producto") if varBuscador.get() == "" else None)
    entBuscador.bind('<KeyRelease>',buscadorNombre)


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
    tblInventario.heading("col3", anchor=ttk.CENTER, text="Precio U.")
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

    #cmb metodo de pago
    ttk.Label(menu,text="Metodo Pago").place(x=650,y=480)
    global cmbMetodoPago
    cmbMetodoPago = ttk.Combobox(menu,state="readonly",values=("Efectivo","Credito","Debito"))
    cmbMetodoPago.place(x=780,y=480)


    #cmb proveedor
    ttk.Label(menu,text="Proveedor").place(x=650,y=540)
    global cmbProveedor
    cmbProveedor = ttk.Combobox(menu,state="readonly",values=(fn.abrirArchivo("archivosJSON/proveedor.json")))
    cmbProveedor.place(x=780,y=540)

    #entry total
    ttk.Label(menu,text="Total a Pagar").place(x=650,y=600)
    ttk.Entry(menu,textvariable=varTotal,state="disable",width=22).place(x=780,y=600)

    #button confirmar comprar
    btnConfirmar =ttk.Button(menu,text="Confirmar",command=confirmarComprar,width=20)
    btnConfirmar.place(x=780,y=640)

    menu.mainloop()
