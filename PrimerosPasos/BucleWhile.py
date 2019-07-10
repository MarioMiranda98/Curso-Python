import sys
import math

i = 1 
while i <= 10 :
    print ("Hola: " + str(i))
    i += 1

print ("Termino la ejecucion")

print ("Otras cosas")
edad = int(input("Edad: "))
while edad < 0 or edad > 100 :
    print ("Haz introducido una edad incorrecta")
    edad = int(input("Edad: "))

print ("Gracias por colaborar")
print ("Edad: " + str(edad))

print ("Otras cosas 2.0")
print ("Programa de calculo de raiz cuadrada")
numero = int(input("Introduce un numero: "))
intentos = 0
while numero < 0 and intentos < 2 :
    print ("No se puede encontrar una raiz negativa")
    intentos += 1
    numero = int(input("Numero: "))
    
if intentos == 2 :
    print ("Fin")
    sys.exit()
else :
    solucion = math.sqrt(numero)
    print ("La raiz cuadrada de " + str(numero) + " es: " + str(solucion))