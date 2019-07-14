from tkinter import *
from tkinter import messagebox #Para hacer modales

root = Tk()

#---------------------Construyendo el modal------------------------------------#
def infoAdicional() :
    messagebox.showinfo("Procesador de Mario", "Procesador de textos version 2019")

def avisoLicencia() :
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion() :
    #valor = messagebox.askquestion("Salir","Deseas Salir De la Aplicacion?")
    #if valor == "yes" :
    #    root.destroy()

    valor = messagebox.askokcancel("Salir", "Deseas Salir?")
    if valor :
        root.destroy()

def cerrarDocumento() :
    valor = messagebox.askretrycancel("Retry", "No es posible, documento bloqueado")
    if valor == False :
        root.destroy()

barraMenu = Menu(root)
root.config(menu = barraMenu, width = 300, height = 300)

archivoMenu = Menu(barraMenu, tearoff = 0)
archivoMenu.add_command(label = "Nuevo")
archivoMenu.add_command(label = "Guardar")
archivoMenu.add_command(label = "Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label = "Cerrar", command = cerrarDocumento)
archivoMenu.add_command(label = "Salir", command = salirAplicacion)

archivoEdicion = Menu(barraMenu, tearoff = 0)
archivoEdicion.add_command(label = "Copiar")
archivoEdicion.add_command(label = "Cortar")
archivoEdicion.add_command(label = "Pegar")

archivoHerramientas = Menu(barraMenu, tearoff = 0)
archivoHerramientas.add_command(label = "")

archivoAyuda = Menu(barraMenu, tearoff = 0)
archivoAyuda.add_command(label = "Licencia", command = avisoLicencia)
archivoAyuda.add_command(label = "Acerca de", command = infoAdicional)

barraMenu.add_cascade(label = "Archivo", menu = archivoMenu)
barraMenu.add_cascade(label = "Edicion", menu = archivoEdicion)
barraMenu.add_cascade(label = "Herramientas", menu = archivoHerramientas)
barraMenu.add_cascade(label = "Ayuda", menu = archivoAyuda)

root.mainloop()