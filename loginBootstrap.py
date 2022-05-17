import ttkbootstrap as ttk

pantalla = ttk.Window(themename="darkly")
pantalla.geometry("400x200")
ttk.Label(pantalla,text="Ingrese su datos").place(x=20,y=20)


pantalla.mainloop()