print ("Verificacion de Acceso")

edadUsuario = int(input("Introduce tu edad: "))

if edadUsuario < 18: 
    print ("No puedes pasar")
elif edadUsuario > 18:
    print ("Puedes Pasar")
else: 
    print ("Nada")