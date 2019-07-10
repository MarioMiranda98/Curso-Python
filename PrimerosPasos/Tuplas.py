miTupla = ("Juan", 13, 1, 1995)#A diferencia de las listas las tuplas se declaran con parentesis

print ("Acceder a un elemento en concreto")
print (miTupla[0])

print ("Convertir una tupla a lista")
miLista = list(miTupla)
print (miLista)

print ("Convertir una lista a tupla")
miTupla = tuple(miLista)
print (miTupla)

print ("Buscar un elemento en la Tupla")
print ("Juan" in miTupla)

print ("Saber cuantos elementos determinandos hay en la tupla")
print (miTupla.count(13))

print ("Saber la longitud de una tupla")
print (len(miTupla))

print ("Tuplas unitarias")
tuplaUnitaria = ("Juan", )
print (len(tuplaUnitaria))

print ("Empaquetado de tupla")
tupla2 = "Juan", 1, 13, 1995
print (tupla2)

print ("Desempaquetado de tupla")
nombre, dia, mes, anio = tupla2
print (nombre)
print (dia)
print (anio)
print (mes)
