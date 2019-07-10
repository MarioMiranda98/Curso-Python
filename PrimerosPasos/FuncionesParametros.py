from random import randint, uniform, random
#import sys// Para scripts con distinta ruta
#sys.path.append('../')//especifimos la ruta del script, usamos la misma linea de código que abajo
#from Listas import prueba //Para scripts del mismo fichero

def suma(num1, num2, i):
	#num1 = 5;
	#num2 = 7;
	print ("La suma de", num1 ,"más", num2, "es", num1+num2)
	print ("Iteracion", i)

def main():
	for i in range (5):
		suma(int (random()*10+1), int (random()*20+1), i)
	print ("Fin del programa")

main()
#prueba()