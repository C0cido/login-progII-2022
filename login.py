import json
import ttkbootstrap as ttk
from werkzeug.security import check_password_hash
from tkinter import messagebox as ms
import funciones as fn

pantalla = ttk.Window(themename="darkly")
pantalla.title("Login de usuarios")
pantalla.geometry("280x180")

#Recordar contraseña
lstRecordar = fn.abrirArchivo("recordarme.json")
nombre= lstRecordar[0]["Usuario"]
contra = lstRecordar[0]["Contra"]
guardar = lstRecordar[0]["Guardar"]


#variables
varNombre = ttk.StringVar(pantalla,nombre)
varContra = ttk.StringVar(pantalla,contra)
varRecordar = ttk.BooleanVar(pantalla,guardar) 

#funciones
def recordar():
    if varRecordar.get() or guardar:
        lstRecordar[0]["Usuario"]= varNombre.get()
        lstRecordar[0]["Contra"]= varContra.get()
        lstRecordar[0]["Guardar"] = True
    else:
        lstRecordar[0]["Usuario"]= ""
        lstRecordar[0]["Contra"]= ""
    with open("recordarme.json","w") as recordar:
        json.dump(lstRecordar,recordar)

def login():
    lstUsuario = fn.abrirArchivo("archivosJSON/usuarios.json")
    if len(varContra.get()) > 0 and len(varNombre.get()) > 0:
        encontrado = False 
        for i in lstUsuario:
            if i["IDUsuario"] == varNombre.get() and check_password_hash(i["Contra"],varContra.get()):
                encontrado = True
                break
        if encontrado:
            recordar()
        else:
            ms.showinfo("Usuario no encontrado","El usuario o la contraseña no son correctas")
    else:
        ms.showerror("Error","Ingrese la informacion necesaria")

#Nombre
ttk.Label(pantalla,text="Nombre").place(x=20,y=20)
entNombre = ttk.Entry(pantalla,textvariable=varNombre)
entNombre.place(x=120,y=20)
entNombre.focus()

#contra
ttk.Label(pantalla,text="Contra").place(x=20,y=60)
entContra = ttk.Entry(pantalla,textvariable=varContra)
entContra.place(x=120,y=60)

#Recordarme
ttk.Checkbutton(pantalla,text="Recordarme",variable=varRecordar,offvalue=False,onvalue=True).place(x=100,y=100)

#buton cargar datos
btnCargar = ttk.Button(pantalla,command=login,text="Loguear")
btnCargar.place(x=108,y=140)

#Inciar
pantalla.mainloop()