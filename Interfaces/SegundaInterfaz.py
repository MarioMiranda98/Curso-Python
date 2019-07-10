from tkinter import *

#primero construir la raiz 
raiz = Tk()
raiz.title("Ventana de prueba") #Asignar titulo
raiz.resizable(0, 0) #Evitar que sea redimensionable 
#raiz.iconbitmap("Ruta") //Para poner otro icono
#raiz.geometry("650x350") #Para dar medidas
raiz.config(bg = "blue") #Para cambiar el fondo
miFrame = Frame() #Construccion de frame
miFrame.pack(fill = "both") #Frame empaquetado
miFrame.config(bg = "red")
miFrame.config(width = 650, height = 350)#Siempre darle tamaño al frame
miFrame.config(relief = "sunken")#Poner un borde
miFrame.config(bd = 8)
miFrame.config(cursor = "pirate")
raiz.mainloop() #Bucle infinito 
