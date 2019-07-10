print ("Instruccion Continue")
for letra in "Python" :
    if letra == "h" : 
        continue #Ignora el resto del bucle y manda a la otra iteracion
    print ("Imprimiendo la letra: " + str(letra))

print ("Pequeña Aplicacion")
contador = 0
nombre = "Pildoras Informaticas"

for i in nombre :
    if i == " " :
        continue
    contador += 1
print ("Las letras del nombre: " + str(nombre) + " son: " + str(contador))

#print ("Probando Pass")
#while True :
  #pass

print ("Probando else")
email = input("Introduce tu email porfavor: ")

for i in email : 
    if i == '@' :
        arroba = True
        break
else : #Sirve para algo cuando termina el bucle entra en accion, depende del uso
    arroba = False
print (arroba)