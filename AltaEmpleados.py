import ttkbootstrap as ttk
import json
import tkinter.messagebox as msg

lstEmpleados = []
try:
    with open ("empleados.json") as empleados:
        lstEmpleados = json.load(empleados)
except:
    lstEmpleados = []

altaEmpleados = ttk.Window(themename="darkly")
altaEmpleados.title("Alta de Empleados")
altaEmpleados.geometry("500x700")

def fContID():
    try:
        with open ("empleados.json") as empleados:
            lstEmpleados = json.load(empleados)
    except:
        lstEmpleados = []
    max = 0
    try:
        for empleado in lstEmpleados:
            if empleado["IDEmpleado"] > max:
                max = empleado["IDEmpleado"]
    except:
        max = 0
    return max + 1

def fDNIenLista(DNI):
    existe = True
    try:
        with open ("empleados.json") as empleados:
            lstEmpleados = json.load(empleados)
    except:
        lstEmpleados = []
    for empleado in lstEmpleados:
        if DNI == empleado["DNI"]:
            existe = False
    return existe

    

def fRegistrarEmpleado():
    if fDNIenLista(varDNI.get()) and varNombre.get().isalpha and varApellido.get().isalpha and (str(varDNI.get()).isdigit and len(varDNI.get() == 8)) and ((str(varCUIL.get()).isdigit) and len(varCUIL.get()) == 11):
        nEmpleado = {}
        try:
            with open ("empleados.json") as archivo:
                lstEmpleados = json.load(archivo)
        except:
            lstEmpleados = []
        nEmpleado["IDEmpleado"] = fContID()
        nEmpleado["Nombre"] = varNombre.get() + " " + varApellido.get()
        nEmpleado["Contra"] = varContra.get()
        nEmpleado["DNI"] = varDNI.get()
        nEmpleado["CUIL"] = varCUIL.get()
        nEmpleado["Sector"] = cmbSector.get()
        lstEmpleados.append(nEmpleado)
        with open("empleados.json", "w") as empleados:
            json.dump(lstEmpleados, empleados)
    else:
        if (varNombre.get().isalpha == False) and (varApellido.get() == False):
            msg.showerror("Registro", "El nombre solo puede contener letras")
        elif str(varDNI.get()).isdigit == False:
            msg.showerror("Registro", "El DNI solo puede contener números")
        elif len(varDNI.get()) != 8:
            msg.showerror("Registro", "El DNI solo puede tener 8 números")
        elif str(varCUIL.get()).isdigit == False:
            pass

ttk.Label(altaEmpleados, text="Nombre:").place(x=150, y=100)
varNombre = ttk.StringVar()
ttk.Entry(altaEmpleados, textvariable=varNombre).place(x=150, y=140)
ttk.Label(altaEmpleados, text="Apellido:").place(x=150, y=180)
varApellido = ttk.StringVar()
ttk.Entry(altaEmpleados, textvariable=varNombre).place(x=150, y=220)
ttk.Label(altaEmpleados, text="Contraseña:").place(x=150, y=260)
varContra = ttk.StringVar()
ttk.Entry(altaEmpleados).place(x=150, y=300)
ttk.Label(altaEmpleados, text="DNI:").place(x=150, y=340)
varDNI = ttk.IntVar()
ttk.Entry(altaEmpleados).place(x=150, y=380)
ttk.Label(altaEmpleados, text="CUIL:").place(x=150, y=420)
varCUIL = ttk.IntVar()
ttk.Entry(altaEmpleados).place(x=150, y=460)
ttk.Label(altaEmpleados, text="Sector:").place(x=150, y=500)
#sectores: compras, ventas, stock
lstSectores = []
cmbSector = ttk.Combobox(altaEmpleados, values=lstSectores, state="readonly")
cmbSector.place(x=150, y=540)

altaEmpleados.mainloop()