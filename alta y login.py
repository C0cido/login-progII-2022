import ttkbootstrap as ttk
import json
import probandoContra as encriptado

pantalla = ttk.Window()
pantalla.title("Probando")
pantalla.geometry("400x400")

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
    nuevoUsuario = {}
    nuevoUsuario["Usuario"] = varNombre.get() 
    contra = encriptado.f.encrypt(bytes(varContra.get(),"utf_8"))
    nuevoUsuario["Contra"] = contra.decode("utf_8")
    lstUsuario.append(nuevoUsuario)
    with open("contra.json","w") as lst:
        json.dump(lstUsuario,lst)

#Nombre
ttk.Label(pantalla,text="Nombre").place(x=20,y=20)
entNombre = ttk.Entry(pantalla,textvariable=varNombre)
entNombre.place(x=200,y=20)

#contra
ttk.Label(pantalla,text="Contra").place(x=20,y=60)
entContra = ttk.Entry(pantalla,textvariable=varContra)
entContra.place(x=200,y=60)

#buton cargar datos
btnCargar = ttk.Button(pantalla,command=agregarUsuario,text="Agregar Empleado")
btnCargar.place(x=100,y=100)

#Inciar
pantalla.mainloop()