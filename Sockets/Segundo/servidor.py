import socket
import time
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9999))
s.listen(5)

while True :
    clientSocket, direccion = s.accept()
    print(f"Conexion de la { direccion } ha sido establecida")

    d = {1 : "Oye", 2 : "Ahi!"}
    mensaje = pickle.dumps(d)
    mensaje = bytes(f"{len(mensaje):<{HEADERSIZE}}",  "utf-8") + mensaje

    clientSocket.send(mensaje)
