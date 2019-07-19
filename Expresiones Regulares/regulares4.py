import re

nombre1 = "Jara Lopez"
nombre2 = "Antonio Gomez"
nombre3 = "Lara Lopez"

cadena1 = "Mario Miranda"
cadena2 = "5456545654"
cadena3 = "a55445566"

print("Match busca si hay concidencias al comienzo")
if re.match("Sandra", nombre3, re.IGNORECASE) :
    print ("Se ha encontrado el nombre")
else :
    print ("No lo hemos encontrado")

print("El comodin punto sirve para dar una letra cualquiera y luego el patron")
if re.match(".ara", nombre3, re.IGNORECASE) :
    print ("Se ha encontrado el nombre")
else :
    print ("No lo hemos encontrado")

print ("La barra invertida mas una d \d, si en la cadena el patron de busqueda la cadena comienza con un numero o no")
if re.match("\d", cadena2) :
    print("Hemos encontrado numero")
else : 
    print("No hemos encontrado numero")

print("La funcion search, busca en toda la cadena si se encuentra el patron")
if re.search("Lopez", nombre1, re.IGNORECASE) :
    print("Se ha encontrado el apellido")
else :
    print("No se ha encontrado")