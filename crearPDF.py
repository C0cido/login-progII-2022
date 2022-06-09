import pdfkit
import jinja2
import funciones as fn


lstVentas = fn.abrirArchivo("archivosJSON/ventas.json")
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
    config = pdfkit.configuration(wkhtmltopdf = "C:\Program Files\wkhtmltopdf")
    rutaSalida = "C:/Users/Warnet1454/Documents/GitHub/login_integradorProg/archivosPDF/prueba.pdf"

    pdfkit.from_string(html,rutaSalida,css=rutaCss,options=option,configuration=config)
nombreProductos = ""
for i in lstVentas:
    if i["IDVenta"] == 0:
        for j in i["VentaRealizada"]:
            nombreProductos += j["Producto"] + " "
        info = {"IDVenta": i["IDVenta"],"FechaVenta":i["FechaVenta"],"Cliente":i["Cliente"],"MetodoPago":i["MetodoPago"],"Producto":nombreProductos,"TotalACobrar":i["TotalACobrar"]}
        break
rutaTemplate = "C:/Users/Warnet1454/Documents/GitHub/login_integradorProg/archivosPDF/template.html"
crearNuevoPdf(rutaTemplate,info)