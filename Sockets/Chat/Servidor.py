import socket
import select #Para seleccionar conexiones

HEADERLENGHT = 10
IP = "127.0.0.1"
PUERTO = 1234

socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketServidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Nos permite reusar la direccion IP (setscokopt nos permite configurar el socket)
socketServidor.bind((IP, PUERTO))
socketServidor.listen()

listaSockets = [socketServidor]
clientes = {}

print(f"Escuchando conexiones en { IP } : { PUERTO }")

def recibeMensaje(socketCliente) :
    try :
        mensajeHeader = socketCliente.recv(HEADERLENGHT)
        if not len(mensajeHeader) :
            return False
        longitudMensaje = int(mensajeHeader.decode("utf-8").strip())
        return {"header" : mensajeHeader, "datos" : socketCliente.recv(longitudMensaje)} 
    except :
        return False 

while True :
    leerSockets, _, excepcionEnSockets = select.select(listaSockets, [], listaSockets)

    for socketNotificado in leerSockets :
        if socketNotificado == socketServidor :
            socketCliente, direccionCliente = socketServidor.accept()

            usuario = recibeMensaje(socketCliente)
            if usuario is False :
                continue
            listaSockets.append(socketCliente)
            clientes[socketCliente] = usuario
            print("Nueva conexion aceptada de {} : {} usuario: {}".format(direccionCliente[0], direccionCliente[1], usuario['datos'].decode('utf-8')))
        else :
            mensaje = recibeMensaje(socketNotificado)

            if mensaje is False :
                print("Cerrando conexion de {}".format(clientes[socketNotificado]['datos'].decode('utf-8')))
                listaSockets.remove(socketNotificado)
                del clientes[socketNotificado]
                continue

            usuario = clientes[socketNotificado]
            print(f"Mensaje recibido de { usuario['datos'].decode('utf-8') } : { mensaje['datos'].decode('utf-8') }")

            for socketCliente in clientes :
                if socketCliente != socketNotificado :
                    socketCliente.send(usuario['header'] + usuario['datos'] + mensaje['header'] + mensaje['datos'])
        
    for socketNotificado in excepcionEnSockets :
        listaSockets.remove(socketNotificado)
        del clientes[socketNotificado]