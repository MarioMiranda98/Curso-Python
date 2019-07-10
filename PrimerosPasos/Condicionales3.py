salarioPresidente = int(input("Introduce Salario Presidente: "))
print ("Salario Presidente " + str(salarioPresidente))

salarioDirector = int(input("Introduce Salario Director: "))
print ("Salario Director " + str(salarioDirector))

salarioJefeArea = int(input("Introduce Salario Jefe de Area: "))
print ("Salario Jefe de Area " + str(salarioJefeArea))

salarioAdministrativo = int(input("Introduce Salario Administrativo: "))
print ("Salario  Administrativo " + str(salarioAdministrativo))

if salarioAdministrativo < salarioJefeArea < salarioDirector < salarioPresidente: #Se lee de izquierda a derecha si algo falla, se va directo al else, algo asi como en serie
	print ("Todo funciona de manera correcta")
else:
	print ("Some smells tricky :P")