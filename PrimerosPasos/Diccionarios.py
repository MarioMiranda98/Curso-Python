miDiccionario = {"Alemania" : "Berlin", "Francia" : "Paris", "Reino Unido" : "Londres", "Espania" : "Madrid"}#Los diccionarios van entre llaves

print ("Acceder a un elemento concreto")
print (miDiccionario["Francia"])

print ("Imprimir un diccionario entero")
print (miDiccionario)

print ("Añadir un elemento")
miDiccionario["Italia"] = "Lisboa"
print (miDiccionario)

print ("Sobreescribir el valor a un clave")
miDiccionario["Italia"] = "Roma"
print (miDiccionario)

print ("Elimiar pareja clave : valor")
del miDiccionario["Reino Unido"]
print (miDiccionario)

print ("Probando...")
miDiccionario2 = {"Alemania" : "Berlin", 23 : "Jordan", "Mosqueteros" : 3}
print (miDiccionario2)

print ("Asignar una lista a un diccionario")
miLista = ["Francia", "Reino Unido", "Espania"]
miDiccionario3 = {miLista[0] : "Paris", miLista[1] : "Londres", miLista[2] : "Madrid"}
print (miDiccionario3)

print ("Diccionario Almacene una lista")
miDiccionario4 = {23 : "Jordan", "Nombre" : "Michael", "Equipo" : "Chicago", "Anillos" : [1991, 1992, 1993, 1996, 1997, 1998]}
print (miDiccionario4)

print ("Guardar un diccionario en otro diccionario")
miDiccionario5 = {23 : "Jordan", "Nombre" : "Michael", "Equipo" : "Chicago", "Anillos" : {"Temporadas" : [1991, 1992, 1993, 1996, 1997, 1998]}}
print (miDiccionario5)
print (miDiccionario5["Anillos"])

print ("Devolver las claves del diccionario")
print (miDiccionario.keys())

print ("Imprimir los valores de los diccionarios")
print (miDiccionario.values())

print ("Longitud del diccionario")
print (len(miDiccionario))