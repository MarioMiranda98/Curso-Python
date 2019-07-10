#Bucle comun (recorre los elementos de la lista)
for i in [1, 2, 3] :
    print ("Hola", end=" ")
print("")

#Recorriendo String
for i in "Mario" :
    print (i, end="")
print ("")

#Verificando email
flag = False
contador = 0
email = input("Introduce una direccion de correo: ")

for i in email :
    if i == "@" or i == "." :
        contador += 1

if contador == 2 :
    print ("Email correcto")
else :
    print ("Email incorrecto")