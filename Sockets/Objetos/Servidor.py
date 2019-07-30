import socket
import pickle
from Objeto import Objeto

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9999))
s.listen(1)

obj = Objeto("Hola Perro Mundo", 15)
dobj = pickle.dumps(obj)
cliente, dir = s.accept()

cliente.send(dobj)
cliente.close()

