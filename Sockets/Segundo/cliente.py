import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9999))

while True : 
    mensajeCompleto = b''
    nuevoMensaje = True
    while True :
        mensaje = s.recv(16)
        if nuevoMensaje :
            print(f"Longitud del nuevo mensaje: {mensaje[:HEADERSIZE]}")
            longitudMensaje = int(mensaje[:HEADERSIZE])
            nuevoMensaje = False
        mensajeCompleto += mensaje

        if len(mensajeCompleto) - HEADERSIZE == longitudMensaje :
            print("Mensaje completo")
            print(mensajeCompleto[HEADERSIZE:])

            d = pickle.loads(mensajeCompleto[HEADERSIZE:])
            print(d)

            nuevoMensaje = True
            mensajeCompleto = b""

print(mensajeCompleto)

s.close()