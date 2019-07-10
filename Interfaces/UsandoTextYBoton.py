from tkinter import *

root = Tk()
miFrame = Frame(root, width = 1200, height = 600)
miFrame.pack()

miNombre = StringVar()

cuadroTexto = Entry(miFrame, textvariable = miNombre)
cuadroTexto.grid(row = 0, column = 1, pady = 10, padx = 5)
nombreLabel = Label(miFrame, text = "Nombre:")
nombreLabel.grid(row = 0, column = 0, sticky = "e", pady = 10, padx = 5)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row = 1, column = 1, pady = 10, padx = 5)
apellidoLabel = Label(miFrame, text = "Apellido:")
apellidoLabel.grid(row = 1, column = 0, sticky = "e", pady = 10, padx = 5)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row = 2, column = 1, pady = 10, padx = 5)
direccionLabel = Label(miFrame, text = "Direccion:")
direccionLabel.grid(row = 2, column = 0, sticky = "e", pady = 10, padx = 5)

cuadroPassword = Entry(miFrame) 
cuadroPassword.grid(row = 3, column = 1 , pady = 10, padx = 5)
cuadroPassword.config(show = "*", fg = "blue", justify = "center")
passwordLabel = Label(miFrame, text = "Pass")
passwordLabel.grid(row = 3, column = 0, pady = 10, padx = 5)

comentariosLabel = Label(miFrame, text = "Comentarios")
comentariosLabel.grid(row = 4, column= 0, pady = 10, padx = 5)
textoComentario = Text(miFrame, width = 15, height = 5)
textoComentario.grid(row = 4, column = 1, pady = 10, padx = 5)
scrollVertical = Scrollbar(miFrame, command = textoComentario.yview)
scrollVertical.grid(row = 4, column = 2, sticky = "nsew")
textoComentario.config(yscrollcommand = scrollVertical.set)

def codigoBoton() :
    miNombre.set("Mario")

botonEnvio = Button(root, text = "Enviar", command = codigoBoton)
botonEnvio.pack()

root.mainloop()