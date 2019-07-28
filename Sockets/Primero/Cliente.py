import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 9999)) #Para conectar el socket al servidor

while True :
    mensaje = str(input(">"))
    s.send(mensaje.encode('utf-8'))
    if mensaje == "Salir" :
        break
    else :
        recibido = s.recv(1024)
        print("Recibido: ", recibido)

print ("Adios")
s.close()