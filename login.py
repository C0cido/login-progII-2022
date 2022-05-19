from base64 import encode
import ttkbootstrap as ttk
import json
import contra as encriptado
from tkinter import messagebox as ms

pantalla = ttk.Window(themename="darkly")
pantalla.title("Login de usuarios")
pantalla.geometry("280x180")

#variables
varNombre = ttk.StringVar(pantalla,"")
varContra = ttk.StringVar(pantalla,"") 

#funciones
def login():
    lstUsuario = []
    try:
        with open("contra.json") as lst:
            lstUsuario=json.load(lst)
    except:
        lstUsuario = []
    if len(varContra.get()) > 0 and len(varNombre.get()) > 0: 
        for i in lstUsuario:
            contra = (str.encode(i["Contra"]))
            print(encriptado.f.decrypt(contra))
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

#buton cargar datos
btnCargar = ttk.Button(pantalla,command=login,text="Loguear")
btnCargar.place(x=70,y=100)

#Inciar
pantalla.mainloop()