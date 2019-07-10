import sys

def andor():
	print ("Programa de becas año 2017")

	distanciaEscuela = int(input("Introduce la distancia a la escuela en km: "))
	print (distanciaEscuela)

	numeroHermanos = int(input("Introduce el numero de hermanos en el centro "))
	print (numeroHermanos)

	salarioFamiliar = int(input("Introduce salario anual bruto: "))
	print (salarioFamiliar)

	if distanciaEscuela > 40 and numeroHermanos > 2 or salarioFamiliar <= 20000:
		print ("Tienes derecho a beca")
	else:
		print ("No tienes derecho a beca")

def conin():
	print ("Asignaturas Optativas Anio 2017")
	Asignaturas = {1 : "Informatica Gráfica", 2 : "Pruebas Gráficas", 3 : "Usabilidad y Accesibilidad"}
	for i in range (0, 3):
		print ("Materia:", i+1, "Nombre:", Asignaturas[i+1])
	eleccion = int(input("Escoge la asignatura a escoger: "))
	if eleccion in (1, 2, 3) or eleccion > 0:
		print ("La asignatura elegida es", Asignaturas[eleccion])
	else:
		print ("No existe la asignatura")


def main():
	print("Introduce que quieres ver 1.- And & Or 2.-In 3.-Salir")
	eleccion = int(input())
	if eleccion == 1:
		andor()
	elif eleccion == 2:
		conin()
	else:	
		sys.exit()

main()