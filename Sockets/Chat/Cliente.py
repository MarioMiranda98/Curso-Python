import socket 
import select
import errno
import sys

HEADERLENGHT = 10
IP = "127.0.0.1"
PUERTO = 1234

miNombreUsuario = input("Nombre de usuario: ")
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketCliente.connect((IP, PUERTO))
socketCliente.setblocking(False)

nombreUsuario = miNombreUsuario.encode('utf-8')
nombreUsuarioHeader = f"{len(nombreUsuario):<{HEADERLENGHT}}".encode('utf-8')
socketCliente.send(nombreUsuarioHeader + nombreUsuario)

while True :
    mensaje = input(f'{ miNombreUsuario } > ')
    if mensaje :
        mensaje = mensaje.encode('utf-8')
        mensajeHeader = f"{len(mensaje):<{HEADERLENGHT}}".encode('utf-8')
        socketCliente.send(mensajeHeader + mensaje)

    try :
        while True :
            nombreUsuarioHeader = socketCliente.recv(HEADERLENGHT)
            if not len(nombreUsuarioHeader) :
                print("Conexion cerrada por el servidor")
                sys.exit()
            nombreUsuarioLongitud = int(nombreUsuarioHeader.decode('utf-8').strip())
            nombreUsuario = socketCliente.recv(nombreUsuarioLongitud).decode('utf-8')
            mensajeHeader = socketCliente.recv(HEADERLENGHT)
            mensajeLongitud = int(mensajeHeader.decode('utf-8').strip())
            mensaje = socketCliente.recv(mensajeLongitud).decode('utf-8')
            print(f"{nombreUsuario} > {mensaje}")
    except IOError as e :
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK :
            print("Leyendo Error {}".format(str(e)))
            sys.exit()
        continue
    except Exception as e :
        print("Leyendo error {}".format(str(e)))
        sys.exit()
