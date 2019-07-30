class Objeto() :
    def __init__(self, texto, numero):
        self.texto = texto
        self.numero = numero

    def __str__(self) :
        return f"El texto es { self.texto } con numero { self.numero }"