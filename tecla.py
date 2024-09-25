import os

ev = 1

# current working directory
ruta_de_impresion =os.path.abspath(os.getcwd()) + "/album de fotos/carpeta " + str(ev)+ "/documento.pdf"


print(ruta_de_impresion)