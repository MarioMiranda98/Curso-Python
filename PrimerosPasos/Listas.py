miLista = ["Maria", "Pepe", "Martha", "Antonio"]

print ("Imprimir un elemento en concreto")
print (miLista[0])

print ("Imprimir toda la lista")
print (miLista)

print ("Acceder a los elementos 0 a n")
print (miLista[:2])

print("Acceder a los elementos k a n")
print (miLista[2:])

print ("Añadir a una persona a la lista al final")
miLista.append("Sandra")
print (miLista[:])

print ("Anadir un elemento en un posicion determinada")
miLista.insert(2, "Tom")
print (miLista[:])

print ("Añadir varios elementos al final")
miLista.extend(["Mario", "Alberto", "Miranda", "Sandoval"])
print (miLista[:])

print ("Obtener indice del elemento en la lista")
print (miLista.index("Maria"))

print ("Saber si existe un elemento (True/False)")
print ("Mario" in miLista)

print ("Para eliminar un elemento en concreto")
miLista.remove("Alberto")
print (miLista[:])

print ("Eliminar el último elemento de la lista")
miLista.pop()
print(miLista[:])

print ("Longitud de la lista")
print (len(miLista))

print ("Sumar listas (guardar en una tercera lista)")
miLista2 = [1, 2, 3, True]
miLista3 = miLista + miLista2
print (miLista3)

print ("Reeptir listas")
listaRepetir = [5, 6, 7, 8, False] * 3
print (listaRepetir)