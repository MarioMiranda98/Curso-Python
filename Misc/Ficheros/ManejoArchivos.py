from io import open

#Para crear un archivo externo
#Modos:
#lectura -> r
#escritura -> w
#anexar -> a

archivoTexto = open("archivo.txt", "w")
frase = "Estupendo dia para estudiar Python \nel miercoles"
archivoTexto.write(frase)
archivoTexto.close()

#Para abrir un archivo y leer
#leer todo el archivo
archivoTexto = open("archivo.txt", "r")
texto = archivoTexto.read()
print (texto)
archivoTexto.close()

#leer linea a linea, guarda en una lista
archivoTexto = open("archivo.txt", "r")
lineasTexto = archivoTexto.readlines()
print (lineasTexto[0])
archivoTexto.close()

#abrir archivo para anexar
archivoTexto = open("archivo.txt", "a")
archivoTexto.write("\nsiempre es una buena ocasion para estudiar Python")
archivoTexto.close()

#Rebobinar el puntero
archivoTexto = open("archivo.txt", "r")
print (archivoTexto.read())
archivoTexto.seek(15) #Como un rewind variable, con read se puede igual pero read se dentendra hasta el caracter n
print (archivoTexto.read())
archivoTexto.close()