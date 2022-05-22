import ttkbootstrap as ttk
import json
from werkzeug.security import generate_password_hash
from tkinter import messagebox as ms
import funciones as fn

pantalla = ttk.Window(themename="darkly")
pantalla.title("Alta de usuarios")
pantalla.geometry("280x180")

#variables
varNombre = ttk.StringVar(pantalla,"")
varContra = ttk.StringVar(pantalla,"")

#funciones
def agregarEmpleado():
    lstEmpleado = fn.abrirArchivo("archivosJSON/empleados.json")
#completar la funcion para generar dos archivos json (1. para usuario y contraseña 2.para la informacion del empleado)

def agregarUsuario():
    lstUsuario = fn.abrirArchivo("archivosJSON/usuarios.json")
    if len(varContra.get()) > 0 and len(varNombre.get()) > 0: 
        nuevoUsuario = {}
        nuevoUsuario["Usuario"] = varNombre.get() 
        nuevoUsuario["Contra"] = generate_password_hash(varContra.get())
        lstUsuario.append(nuevoUsuario)
        with open("contra.json","w") as lst:
            json.dump(lstUsuario,lst)
        ms.showinfo("Alta existosa","Se ha agregado un nuevo usuario")
        varNombre.set("")
        varContra.set("")
        entNombre.focus()
    else:
        ms.showerror("Error","Si desea agregar usuarios... por favor ingrese su información")


#Nombre
ttk.Label(pantalla,text="Nombre").place(x=20,y=20)
entNombre = ttk.Entry(pantalla,textvariable=varNombre)
entNombre.place(x=120,y=20)
entNombre.focus()

#contra
ttk.Label(pantalla,text="Contra").place(x=20,y=60)
entContra = ttk.Entry(pantalla,textvariable=varContra)
entContra.place(x=120,y=60)

#buton cargar datos
btnCargar = ttk.Button(pantalla,command=agregarUsuario,text="Agregar Empleado")
btnCargar.place(x=70,y=100)

#Inciar
pantalla.mainloop()