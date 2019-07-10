from setuptools import setup

setup(#Datos del paquete a distribuir
    name = "paqueteCalculos", #nombre del paquete
    version = "1.0", #version del paquete
    description = "Paquete de redondeo y potencia", #Descripcion del paquete
    author = "Mario", #Autor
    #opcionales
    #author_email
    #url
    packages = ["Misc.Paquetes.calculos", "Misc.Paquetes.calculos.redondeo_Potencia"] #Ruta del paquete a distribuir [Ruta paquete principal, Ruta paquete a distribuir]
)