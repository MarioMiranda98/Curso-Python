from tkinter import *

root = Tk()
root.title("Ejemplo")

playa = IntVar()
montaña = IntVar()
turismo = IntVar()

def opcionesViaje() :
    opcionEscogida = ""

    if playa.get() == 1 :
        opcionEscogida += "Playa\n"
    
    if montaña.get() == 1 :
        opcionEscogida += "Montaña\n"

    if turismo.get() == 1 :
        opcionEscogida += "Turismo Rural\n"

    texto.config(text = opcionEscogida)

foto = PhotoImage(file = "./imgs/red.png")
Label(root, image = foto).pack()
frame = Frame()
frame.pack()
Label(frame, text = "Elige destinos:", width = 50).pack()
Checkbutton(frame, text = "Playa", justify = "left", variable = playa, onvalue = 1, offvalue = 0, command = opcionesViaje).pack()
Checkbutton(frame, text = "Montaña", justify = "left", variable = montaña, onvalue = 1, offvalue = 0, command = opcionesViaje).pack()
Checkbutton(frame, text = "Turismo rural", justify = "left", variable = turismo, onvalue = 1, offvalue = 0, command = opcionesViaje).pack()

texto = Label(frame)
texto.pack()

root.mainloop()