import json
import ttkbootstrap as ttk

#estructura del menu de compras
def abrirCompra():
    menuCompra = ttk.Window(themename="darkly")
    menuCompra.geometry("400x400")
    menuCompra.title("Sector compras")
    tabControl=ttk.Notebook(menuCompra)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab1,text="tab1")
    tabControl.add(tab2,text="tab2")
    tabControl.pack(expand = 1, fill ="both")
    ttk.Label(tab1,text="Bienvenido").place(x=20,y=20)





    menuCompra.mainloop()
abrirCompra()