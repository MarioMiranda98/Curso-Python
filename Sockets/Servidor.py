import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Creacion de un objeto tipo socket
s.bind(("", 9999))#Host y puerto
s.listen(1)#Para que el socket acepte conexiones 
sc, addr = s.accept() #Aceptamos la conexion devuelve una tupla

while True :
    recibido = sc.recv(1024) #Vamos a recibir 1024 bytes

    if recibido == "Salir" :
        break
    else :
        print ("Recibido:", recibido)

    respuesta = str(input(">"))
    sc.send(respuesta.encode('utf-8'))

print ("Adios")
sc.close()#Cerramos los sockets
s.close()
