import socket
import pickle
from Objeto import Objeto

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9999))

obj = Objeto("", 0)
asd = s.recv(1024)
obj = pickle.loads(asd)

print(obj)

s.close()