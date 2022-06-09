import pdfkit
import jinja2
import funciones as fn


lstVentas = fn.abrirArchivo("archivosJSON/ventas.json")

infoProductos = ""
producto1 = "-"
producto2 = "-"
producto3 = "-"
producto4 = "-"
producto5 = "-"
producto6 = "-"
producto7 = "-"
producto8 = "-"
producto9 = "-"
producto10 = "-"

cont = 1
for i in lstVentas:
    if i["IDVenta"] == 2:
        for j in i["VentaRealizada"]:
            if cont <= 10:
                infoProductos = j["Producto"] + "  |  $" + str(j["Precio"]) + "  |  " + str(j["Cantidad"]) + "  |  $" + str(j["Precio"]*j["Cantidad"])
                if cont == 1 and infoProductos:
                    producto1 = infoProductos
                elif cont == 2:
                    producto2 = infoProductos
                elif cont == 3:
                    producto3 = infoProductos
                elif cont == 4 :
                    producto4 = infoProductos
                elif cont == 5:
                    producto5 = infoProductos
                elif cont == 6:
                    producto6 = infoProductos
                elif cont == 7:
                    producto7 = infoProductos
                elif cont == 8:
                    producto8 = infoProductos
                elif cont == 9:
                    producto9 = infoProductos
                elif cont == 10:
                    producto10 = infoProductos
                
                cont += 1
        info = {"IDVenta": i["IDVenta"],"FechaVenta":i["FechaVenta"],"Cliente":i["Cliente"],"MetodoPago":i["MetodoPago"],"TotalACobrar":i["TotalACobrar"],"Producto1": producto1,"Producto2":producto2,"Producto3":producto3,"Producto4":producto4,"Producto5":producto5,"Producto6":producto6,"Producto7":producto7,"Producto8":producto8,"Producto9":producto9,"Producto10":producto10}
        break
rutaTemplate = "C:/Users/Warnet1454/Documents/GitHub/login_integradorProg/archivosPDF/template.html"

def crearNuevoPdf(rutaTemplate,info,rutaCss=""):
    nombreTemplate = rutaTemplate.split("/")[-1]
    rutaTemplate = rutaTemplate.replace(nombreTemplate,"")

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(rutaTemplate))
    template = env.get_template(nombreTemplate)
    html = template.render(info)
    option = {
        "page-size":"Letter",
        "encoding":"UTF-8"
    }
    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    rutaSalida = "C:/Users/Warnet1454/Documents/GitHub/login_integradorProg/archivosPDF/prueba.pdf"

    pdfkit.from_string(html,rutaSalida,css=rutaCss,options=option,configuration=config)

crearNuevoPdf(rutaTemplate,info)