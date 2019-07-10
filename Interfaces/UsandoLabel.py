from tkinter import *

root = Tk()
miFrame = Frame(root, width = 500, height = 400)
miFrame.pack()
#miLabel = Label(miFrame, text = "Hola mundo")
#miLabel.place(x = 100, y = 100)#Como setLocation en java
#Para elementos que no cambiara su ejecucion
Label(miFrame, text = "Hola mundo", fg = "blue", font = ("Courier New", 18)).place(x = 100, y = 200)
miImagen = PhotoImage(file = "./imgs/red.png")
Label(miFrame, image = miImagen).place(x = 100, y = 50)
root.mainloop()