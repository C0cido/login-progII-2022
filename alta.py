import ttkbootstrap as ttk
import json
import contra as encriptado
from tkinter import messagebox as ms

pantalla = ttk.Window(themename="darkly")
pantalla.title("Alta de usuarios")
pantalla.geometry("280x180")

#variables
varNombre = ttk.StringVar(pantalla,"")
varContra = ttk.StringVar(pantalla,"")

#funciones
def agregarUsuario():
    lstUsuario = []
    try:
        with open("contra.json") as lst:
            lstUsuario=json.load(lst)
    except:
        lstUsuario = []
    if len(varContra.get()) > 0 and len(varNombre.get()) > 0: 
        nuevoUsuario = {}
        nuevoUsuario["Usuario"] = varNombre.get() 
        contra = encriptado.f.encrypt(bytes(varContra.get(),"utf_8"))
        nuevoUsuario["Contra"] = contra.decode("utf_8")
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