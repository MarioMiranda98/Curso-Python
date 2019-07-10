import os
import time
import sys
borrarPantalla = lambda : os.system("cls")

nombreUsuario = input("Introduce tu nombre de uduario: ")
print ("El nombre es: " + str(nombreUsuario))

print ("Para pasarlo a mayusculas")
print ("El nombre es: " + str(nombreUsuario.upper()))

print ("Pasarlo a minusculas")
print ("El nombre es: " + str(nombreUsuario.lower()))

print ("Poner la primera letra en mayuscula")
print ("El nombre es: " + str(nombreUsuario.capitalize()))

time.sleep(4)
borrarPantalla()
print ("Ejemplo mas elaborado")
edad = input("Introduce tu edad: ")
print (edad.isdigit())

if edad.isdigit() :
    edad = int(edad)
else :
    sys.exit()

if edad >= 18 :
    print ("Eres mayor de edad")
else :
    print ("Eres menor de edad")