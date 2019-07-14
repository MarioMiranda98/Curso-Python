from tkinter import *

raiz = Tk()
miFrame = Frame()
miFrame.pack()
operacion = ""
resultado = 0
resetPantalla = False
#---------------Pantalla------------------#
numeroPantalla = StringVar()
pantalla = Entry(miFrame, textvariable = numeroPantalla)
pantalla.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 4)
pantalla.config(background = "black", fg = "#03f943", justify = "right")
#----------------Pulsaciones Teclado-------------#
def numeroPulsado(num) :
    global operacion
    global resetPantalla
    if resetPantalla != False :
        numeroPantalla.set(num)
        resetPantalla = False
    else :
        numeroPantalla.set(numeroPantalla.get() + num)

#----------------Funcion Suma-----------------------#
def suma(num) :
    global operacion
    global resultado
    global resetPantalla
    resultado += int(num)
    operacion = "suma"
    resetPantalla = True
    numeroPantalla.set(resultado)

#------------------Funcion Resta----------------#
num1 = 0
contadorResta = 0
def resta(num) :
    global num1
    global contadorResta
    global operacion
    global resultado
    global resetPantalla
    
    if contadorResta == 0 :
        num1 = int(num)
        resultado = num1
    else :
        if contadorResta == 1 :
            resultado = num1 - int(num)
        else :
            resultado = int(resultado) - int(num)    
        
        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contadorResta = contadorResta + 1
    operacion = "resta"
    resetPantalla = True

#------------------Funcion multiplicacion-------#
contadorMultiplicacion = 0

def multiplicacion(num) :
    global operacion
    global resultado
    global num1
    global contadorMultiplicacion
    global resetPantalla

    if contadorMultiplicacion == 0 :
        num1 = int(num)
        resultado = num1
    else :
        if contadorMultiplicacion == 1 :
            resultado = num1 * int(num)
        else :
            resultado = int(resultado) * int(num)

        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contadorMultiplicacion = contadorMultiplicacion + 1
    operacion = "multiplicacion"
    resetPantalla = True

#----------------Funcion Division---------------#
contadorDivision = 0
def division(num) :
    global operacion
    global resultado
    global num1
    global contadorDivision
    global resetPantalla

    if contadorDivision == 0 :
        num1 = float(num)
        resultado = num1
    else :
        if contadorDivision == 1:
            resultado = num1 / float(num)
        else :
            resultado = float(resultado) / float(num)
    
        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()
    
    contadorDivision = contadorDivision + 1
    operacion = "division"
    resetPantalla = True

#------------------Funcion Resultado------------#
def elResultado() :
    global resultado
    global operacion
    global contadorResta
    global contadorMultiplicacion
    global contadorDivision

    if operacion == "suma" :
        numeroPantalla.set(resultado + int(numeroPantalla.get()))
        resultado = 0
    elif operacion == "resta" :
        numeroPantalla.set(int(resultado) - int(numeroPantalla.get()))
        resultado = 0
        contadorResta = 0
    elif operacion == "multiplicacion" :
        numeroPantalla.set(int(resultado) * int (numeroPantalla.get()))
        resultado = 0
        contadorMultiplicacion = 0
    elif operacion == "division" :
        numeroPantalla.set(float(resultado) / float(numeroPantalla.get()))
        resultado = 0
        contadorDivision = 0
    
#------------Botones----------------#
#---------FIla 1--------------------#
boton7 = Button(miFrame, text = "7", width = 3, command = lambda:numeroPulsado("7"))
boton7.grid(row = 2, column = 1)
boton8 = Button(miFrame, text = "8", width = 3, command = lambda:numeroPulsado("8"))
boton8.grid(row = 2, column = 2)
boton9 = Button(miFrame, text = "9", width = 3, command = lambda:numeroPulsado("9"))
boton9.grid(row = 2, column = 3)
botonDividir = Button(miFrame, text = "/", width = 3, command = lambda:division(numeroPantalla.get()))
botonDividir.grid(row = 2, column = 4)
#-------------Fila 2 ----------------#
boton4 = Button(miFrame, text = "4", width = 3, command = lambda:numeroPulsado("4"))
boton4.grid(row = 3, column = 1)
boton5 = Button(miFrame, text = "5", width = 3, command = lambda:numeroPulsado("5"))
boton5.grid(row = 3, column = 2)
boton6 = Button(miFrame, text = "6", width = 3, command = lambda:numeroPulsado("6"))
boton6.grid(row = 3, column = 3) 
botonMultiplicar = Button(miFrame, text = "X", width = 3, command = lambda:multiplicacion(numeroPantalla.get()))
botonMultiplicar.grid(row = 3, column = 4)
#-------------Fila 3--------------#
boton1 = Button(miFrame, text = "1", width = 3, command = lambda:numeroPulsado("1"))
boton1.grid(row = 4, column = 1)
boton2 = Button(miFrame, text = "2", width = 3, command = lambda:numeroPulsado("2"))
boton2.grid(row = 4, column = 2)
boton3 = Button(miFrame, text = "3", width = 3, command = lambda:numeroPulsado("3"))
boton3.grid(row = 4, column = 3)
botonRestar = Button(miFrame, text = "-", width = 3, command = lambda:resta(numeroPantalla.get()))
botonRestar.grid(row = 4, column = 4)
#---------------Fila 4-----------------#
boton0 = Button(miFrame, text = "0", width = 3, command = lambda:numeroPulsado("0"))
boton0.grid(row = 5, column = 1)
botonComa = Button(miFrame, text = ",", width = 3, command = lambda:numeroPulsado(","))
botonComa.grid(row = 5, column = 2)
botonIgual = Button(miFrame, text = "=", width = 3, command = lambda:elResultado())
botonIgual.grid(row = 5, column = 3)
botonSumar = Button(miFrame, text = "+", width = 3, command = lambda:suma(numeroPantalla.get()))
botonSumar.grid(row = 5, column = 4)
#----------Correr esta app---------------#
raiz.mainloop()