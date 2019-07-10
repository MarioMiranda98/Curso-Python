from tkinter import *

root = Tk()
miFrame = Frame(root, width = 1200, height = 600)
miFrame.pack()

cuadroTexto = Entry(miFrame)
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

root.mainloop()