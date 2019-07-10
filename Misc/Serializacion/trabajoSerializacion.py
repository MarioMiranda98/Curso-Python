import pickle

lista = ["Pedro", "Ana", "Maria", "Isabel"]
#Creando un fichero en modo binario
ficheroBinario = open("listaNombre", "wb")
pickle.dump(lista, ficheroBinario)
ficheroBinario.close()
del (ficheroBinario)

#Para recuperarlo
fichero = open("listaNombre", "rb")
listaLecutra = pickle.load(fichero)
print(listaLecutra)
fichero.close()