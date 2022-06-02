import json
import ttkbootstrap as ttk
from werkzeug.security import check_password_hash
from tkinter import messagebox as ms
import funciones as fn
import abriMenues as menu

pantalla = ttk.Window()
pantalla.title("Login de usuarios")
pantalla.geometry("400x300")

#Recordar contraseña
lstRecordar = fn.abrirArchivo("recordarme.json")
nombre= lstRecordar[0]["Usuario"]
guardar = lstRecordar[0]["Guardar"]


#variables
varNombre = ttk.StringVar(pantalla,nombre)
varContra = ttk.StringVar(pantalla,"")
varRecordar = ttk.BooleanVar(pantalla,guardar) 

#funciones
def recordar():
    if varRecordar.get():
        lstRecordar[0]["Usuario"]= varNombre.get()
        lstRecordar[0]["Guardar"] = True
    else:
        lstRecordar[0]["Usuario"]= ""
        lstRecordar[0]["Guardar"] = False
    with open("recordarme.json","w") as recordar:
        json.dump(lstRecordar,recordar)

def login():
    lstUsuario = fn.abrirArchivo("archivosJSON/usuarios.json")
    if len(varContra.get()) > 0 and len(varNombre.get()) > 0:
        encontrado = False 
        for i in lstUsuario:
            if i["Usuario"] == varNombre.get() and check_password_hash(i["Contra"],varContra.get()):
                encontrado = True
                idBuscar = i["IDUsuario"]
                break
        if encontrado:
            recordar()
            pantalla.destroy()
            menu.buscarEmpleado(idBuscar)            
        else:
            ms.showinfo("Usuario no encontrado","El usuario o la contraseña no son correctas")
    else:
        ms.showerror("Error","Ingrese la informacion necesaria")

#Nombre
ttk.Label(pantalla,text="Nombre").place(x=20,y=20)
entNombre = ttk.Entry(pantalla,textvariable=varNombre)
entNombre.place(x=150,y=20)
entNombre.focus()

#contra
ttk.Label(pantalla,text="Contra").place(x=20,y=80)
entContra = ttk.Entry(pantalla,textvariable=varContra)
entContra.place(x=150,y=80)

#Recordarme
ttk.Checkbutton(pantalla,text="Recordarme",variable=varRecordar,offvalue=False,onvalue=True).place(x=130,y=130)

#buton cargar datos
btnCargar = ttk.Button(pantalla,command=login,text="Loguear")
btnCargar.place(x=150,y=180)

#Inciar
pantalla.mainloop()