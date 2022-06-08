import json
import ttkbootstrap as ttk
import funciones as fn
from tkinter import messagebox as ms
from werkzeug.security import generate_password_hash

def verificarCUIT(DNI,CUIT):
    cont = 0
    total = 0
    try:
        for i in CUIT:
            if cont >=2 and cont <= 9:
                if  i == DNI[total]:
                    total+=1
            cont += 1
    except:
        total = 0
    return total


#crea top level, el cual permite agregar existencia de productos.
def altaEmpleado():
    global alta
    try:
        if alta.state() == "normal":
            alta.focus()
    except:
        alta = ttk.Toplevel(title="Alta")
        alta.geometry("600x400")
        
        #variables
        varNombre = ttk.StringVar(alta,"")
        varDNI = ttk.StringVar(alta,"")
        varCUIT = ttk.StringVar(alta,"")

            #funcion que permite agregar existencia de productos al inventario.
        def confirmarAlta():
                alta.focus()
                if len(varNombre.get())>0 and  len(varDNI.get()) == 8  and (varDNI.get()).isdigit() and len(varCUIT.get()) == 11 and (varCUIT.get()).isdigit() and cmbSector.get() != "" and verificarCUIT(varDNI.get(),varCUIT.get()) == 8 and (varNombre.get()).isalpha():
                    #dar alta producto en inventario o sumarlo
                    lstEmpleados = fn.abrirArchivo("archivosJSON/empleados.json")
                    lstUsuarios = fn.abrirArchivo("archivosJSON/usuarios.json")
                    if any((i["DNI"] == (varDNI.get())) for i in lstEmpleados):
                        ms.showerror("Atencion","Ha ingresado informacion de un empleado ya existente")
                    else:
                        nuevoEmpleado = {}
                        idVinculado = fn.maximo(lstEmpleados,"IDEmpleado")
                        nuevoEmpleado["IDEmpleado"] = idVinculado
                        nuevoEmpleado["Nombre"] = (varNombre.get()).upper()
                        nuevoEmpleado["DNI"] = varDNI.get()
                        nuevoEmpleado["CUIT"] = varCUIT.get()
                        nuevoEmpleado["Sector"] = cmbSector.get()
                        lstEmpleados.append(nuevoEmpleado)
                        with open("archivosJSON/empleados.json","w") as archivo:
                            json.dump(lstEmpleados,archivo)
                        nuevoUsuario = {}
                        nuevoUsuario["IDUsuario"] = idVinculado
                        nuevoUsuario["Usuario"] = (varNombre.get()).upper()
                        nuevoUsuario["Contra"] = generate_password_hash(varDNI.get())
                        nuevoUsuario["Inicio"] = False
                        lstUsuarios.append(nuevoUsuario)
                        with open("archivosJSON/usuarios.json","w") as archivo:
                            json.dump(lstUsuarios,archivo)
                        actualizarTabla(tblEmpleados)
                        ms.showinfo("Operacion realizada","El registro de alta de empleados se ha completado con exito")
                    alta.focus()
                    varNombre.set("")
                    varDNI.set("")
                    varCUIT.set("")
                    cmbSector.set("")
                else:   
                    if varNombre.get() == "" or varCUIT.get() == "" or varDNI.get()== ""  or cmbSector.get() == "":
                        ms.showerror("Error","La casillas no pueden estar vacias")
                    elif (varDNI.get()).isdigit() == False or (varCUIT.get()).isdigit() == False:
                        ms.showerror("Error","El DNI o el CUIT solo puede ser numerica")
                    elif verificarCUIT(varDNI.get(),varCUIT.get()) != 8:
                        ms.showerror("Error","El CUIT se ha ingresado incorrectamente")
                    elif (varNombre.get()).isalpha() == False:
                        ms.showerror("Error","El nombre solo puede ser alfabetico")
                    alta.focus()

            #nombre 
        ttk.Label(alta,text="Nombre").place(x=20,y=20)
        ttk.Entry(alta,textvariable=varNombre).place(x=210,y=20)

                #Dni
        ttk.Label(alta,text="DNI").place(x=20,y=80)
        ttk.Entry(alta,textvariable=varDNI).place(x=210,y=80)

                #cuil
        ttk.Label(alta,text="CUIT").place(x=20,y=140)
        ttk.Entry(alta,textvariable=varCUIT).place(x=210,y=140)

                #combobox sector
        ttk.Label(alta,text="Sector").place(x=20,y=200)
        cmbSector = ttk.Combobox(alta,state="readonly",values=("Compras","Ventas","Deposito","Empleados"))
        cmbSector.place(x=210,y=200)

            #buton confirmar compra
        ttk.Button(alta,text="Confirmar",command=confirmarAlta).place(x=210,y=330)

#crea top level, el cual permite modificar datos de productos existentes y que son seleccionado del treview.
def modificarEmpleado():
    if  tblEmpleados.item(tblEmpleados.focus(), 'text') != "":
        global modificar
        try:
            if modificar.state() == "normal":
                modificar.focus()
        except:
            modificar = ttk.Toplevel(title="Modificar")
            modificar.geometry("600x400")

        
            #variables
            global varNombre
            global varDNI
            global varCUIT
            global cmbSector
            varNombre = ttk.StringVar(modificar,"")
            varDNI = ttk.StringVar(modificar,"")
            varCUIT = ttk.StringVar(modificar,"")
                #funcion que permite modificar productos existentes en el inventario.
            def confirmarModificacion():
                if len(varNombre.get())>0 and  len(varDNI.get()) == 8  and (varDNI.get()).isdigit() and len(varCUIT.get()) == 11 and (varCUIT.get()).isdigit() and cmbSector.get() != "" and verificarCUIT(varDNI.get(),varCUIT.get())==8 and (varNombre.get()).isalpha():
                    if ms.askyesno("Atencion","¿Desea modificar el empleado seleccionado?"):
                        lstEmpleado = fn.abrirArchivo("archivosJSON/empleados.json")
                        for i in lstEmpleado:
                            if i["IDEmpleado"] == tblEmpleados.item(tblEmpleados.focus(), 'text'):
                                i["Nombre"] = (varNombre.get()).upper()
                                i["DNI"] = varDNI.get()
                                i["CUIT"] = varCUIT.get()
                                i["Sector"] = cmbSector.get()
                        with open("archivosJSON/empleados.json","w") as archivo:
                            json.dump(lstEmpleado,archivo)
                        actualizarTabla(tblEmpleados)  
                        modificar.destroy()                   
                else:
                    if varNombre.get() == "" or varCUIT.get() == "" or varDNI.get()== ""  or cmbSector.get() == "":
                        ms.showerror("Error","La casillas no pueden estar vacias")
                    elif (varDNI.get()).isdigit() == False or (varCUIT.get()).isdigit() == False:
                        ms.showerror("Error","El DNI o el CUIT solo puede ser numerica")
                    elif verificarCUIT(varDNI.get(),varCUIT.get()) != 8:
                        ms.showerror("Error","El CUIT se ha ingresado incorrectamente")
                    elif (varNombre.get()).isalpha() == False:
                        ms.showerror("Error","El nombre solo puede ser alfabetico")
                    modificar.focus()
                            
                #nombre 
            ttk.Label(modificar,text="Nombre").place(x=20,y=20)
            ttk.Entry(modificar,textvariable=varNombre).place(x=210,y=20)

                #Dni
            ttk.Label(modificar,text="DNI").place(x=20,y=80)
            ttk.Entry(modificar,textvariable=varDNI).place(x=210,y=80)

                #cuil
            ttk.Label(modificar,text="CUIT").place(x=20,y=140)
            ttk.Entry(modificar,textvariable=varCUIT).place(x=210,y=140)

                #combobox sector
            ttk.Label(modificar,text="Sector").place(x=20,y=200)
            cmbSector = ttk.Combobox(modificar,state="readonly",values=("Compras","Ventas","Deposito","Empleados"))
            cmbSector.place(x=210,y=200)


                #buton confirmar compra
            ttk.Button(modificar,text="Confirmar",command=confirmarModificacion).place(x=210,y=330)

            lstEmplleados = fn.abrirArchivo("archivosJSON/empleados.json")
            for i in lstEmplleados:
                if i["IDEmpleado"] == tblEmpleados.item(tblEmpleados.focus(), 'text'):
                    varNombre.set(i["Nombre"])
                    varDNI.set(i["DNI"])
                    varCUIT.set(i["CUIT"])
                    cmbSector.set(i["Sector"])
    else:
        ms.showerror("Error","Por favor seleccione un elemento de la tabla")
#permite eliminar producto seleccionado en el treeview
def eliminarEmpleado():
    if  tblEmpleados.item(tblEmpleados.focus(), 'text') != "":
        if ms.askyesno("Atencion","¿Desea eliminar el empleado seleccionado?"):
            lstEmpleados = fn.abrirArchivo("archivosJSON/empleados.json")
            lstUsuario = fn.abrirArchivo("archivosJSON/usuarios.json")
            for i in lstEmpleados:
                if i["IDEmpleado"] == tblEmpleados.item(tblEmpleados.focus(), 'text'):
                    lstEmpleados.remove(i)
            for i in lstUsuario:
                if i["IDUsuario"] == tblEmpleados.item(tblEmpleados.focus(), 'text'):
                    lstUsuario.remove(i)
            with open("archivosJSON/usuarios.json","w") as archivoUsuarios:
                json.dump(lstUsuario,archivoUsuarios) 
            with open("archivosJSON/empleados.json","w") as archivo:
                json.dump(lstEmpleados,archivo) 
            actualizarTabla(tblEmpleados)
    else:
        ms.showerror("Error","Por favor seleccione un elemento de la tabla")

#actualiza la tabla 
def actualizarTabla(tbl):
    for i in tbl.get_children():
        tbl.delete(i)
    lstInventario = fn.abrirArchivo("archivosJSON/empleados.json")
    for i in lstInventario:
        tbl.insert("",ttk.END,text=i["IDEmpleado"],values=(i["Nombre"],i["DNI"],i["CUIT"],i["Sector"]))

#estructura del menu de compras
def Empleados():
    menu = ttk.Window()
    menu.geometry("1200x500")
    menu.title("AMC EMPLEADOS")

    #label saludando al empleado
    ttk.Label(menu,text="Bienvenido").place(x=20,y=20)
    ttk.Label(menu,text="Lista empleados actual").place(x=20,y=60)

    #estructura de tabla(mostrar el inventario)
    global tblEmpleados
    tblEmpleados = ttk.Treeview(menu,columns=("col1","col2","col3","col4"),selectmode="browse")
    tblEmpleados.column("#0", anchor=ttk.CENTER,width=50)
    tblEmpleados.column("col1", anchor=ttk.CENTER)
    tblEmpleados.column("col2", anchor=ttk.CENTER)
    tblEmpleados.column("col3", anchor=ttk.CENTER)
    tblEmpleados.column("col4", anchor=ttk.CENTER,width=100)
    tblEmpleados.heading("#0", anchor=ttk.CENTER, text="ID")
    tblEmpleados.heading("col1", anchor=ttk.CENTER, text="Empleado")
    tblEmpleados.heading("col2", anchor=ttk.CENTER, text="DNI")
    tblEmpleados.heading("col3", anchor=ttk.CENTER, text="CUIT")
    tblEmpleados.heading("col4", anchor=ttk.CENTER, text="Sector")
    tblEmpleados.place(x=20,y=120)
    actualizarTabla(tblEmpleados)

    #Activar botones a traves de la seleccion del treeview

    #button alta 
    btnAlta = ttk.Button(menu,text="Alta Empleado",command=altaEmpleado,width=20)
    btnAlta.place(x=900,y=120)

    #button modificar 
    btnModificar = ttk.Button(menu,text="Modificar Empleado",command=modificarEmpleado,width=20)
    btnModificar.place(x=900,y=160)

    #button modificar 
    btnEliminar = ttk.Button(menu,text="Eliminar Empleado",command=eliminarEmpleado,width=20)
    btnEliminar.place(x=900,y=200)


    menu.mainloop()
Empleados()