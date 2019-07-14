from tkinter import *

root = Tk()
varOpcion = IntVar()
Label(root, text = "Genero:").pack()

def imprimir() :
    #print(varOpcion.get())
    if varOpcion.get() == 1 :
        etiqueta.config(text = "Masculino")
    elif varOpcion.get() == 2 :
        etiqueta.config(text = "Femenino")
    else :
        etiqueta.config(text = "Otras Opciones")

Radiobutton(root, text = "Masculino", variable = varOpcion, value = 1, command = imprimir).pack()
Radiobutton(root, text = "Femenino", variable = varOpcion, value = 2, command = imprimir).pack()
Radiobutton(root, text = "Otras Opciones", variable = varOpcion, value = 3, command = imprimir).pack()
etiqueta = Label(root)
etiqueta.pack()
root.mainloop()