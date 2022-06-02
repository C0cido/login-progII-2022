import ttkbootstrap as ttk
import json

tabla = ttk.Window()
tabla.title("Tabla de Empleados")
tabla.geometry("800x600")

tvEmpleados = ttk.Treeview()
tvEmpleados['columns']=('Rank', 'Name', 'Badge')
tvEmpleados.column('#0', width=0, stretch="NO")
tvEmpleados.column('ID', anchor="center", width=80)
tvEmpleados.column('Nombre', anchor="center", width=80)
tvEmpleados.column('DNI', anchor="center", width=80)
tvEmpleados.column('CUIL', anchor="center", width=80)
tvEmpleados.column('Sector', anchor="center", width=80)

tvEmpleados.heading('#0', text='', anchor="center")
tvEmpleados.heading('ID', text='ID', anchor="center")
tvEmpleados.heading('Nombre', text='Nombre', anchor="center")
tvEmpleados.heading('DNI', text='DNI', anchor="center")
tvEmpleados.heading('CUIL', text='CUIL', anchor="center")
tvEmpleados.heading('Sector', text='Sector', anchor="center")

tvEmpleados.pack()


tabla.mainloop()