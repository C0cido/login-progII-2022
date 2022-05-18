import ttkbootstrap as ttk
import json

usuarios = []
try:
    with open ("empleados.json") as lstEmpleados:
        usuarios = json.load(lstEmpleados)
except:
    pass

loginEmpleados = ttk.Window(themename="darkly")
loginEmpleados.title("Login para Empleados")
loginEmpleados.geometry("500x400")

ttk.Label(loginEmpleados, text="Nombre de Empleado").place(x=150, y=120)
ttk.Entry(loginEmpleados).place(x=150, y=160)
ttk.Label(loginEmpleados, text="Contraseña").place(x=150, y=200)
ttk.Entry(loginEmpleados).place(x=150, y=240)

loginEmpleados.mainloop()