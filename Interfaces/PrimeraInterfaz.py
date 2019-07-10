from tkinter import *

#primero construir la raiz (frame)
raiz = Tk()
raiz.title("Ventana de prueba") #Asignar titulo
raiz.resizable(0, 0) #Evitar que sea redimensionable 
#raiz.iconbitmap("Ruta") //Para poner otro icono
raiz.geometry("650x350") #Para dar medidas
raiz.config(bg = "blue") #Para cambiar el fondo
raiz.mainloop() #Bucle infinito 