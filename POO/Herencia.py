class Vehiculos() :
    def __init__(self, marca, modelo) :
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self) :
        self.enMarcha = True

    def acelerar(self) :
        self.acelera = True

    def frenar(self) :
        self.frena = True

    def estado(self) :
        print ("Marca: " + str(self.marca) + "\nModelo: " +str(self.modelo) + "\nEn Marcha: " + str(self.enMarcha) +
            "\nAcelerando: " + str(self.acelera) + "\nFrenado: " + str(self.frena))

class VehiculosElectricos(Vehiculos) :
    def __init__(self, marca, modelo) :
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self) :
        self.cargando = True 

class Furgoneta(Vehiculos) :
    def carga(self, cargar) :
        self.cargado = cargar
        if self.cargado :
            return "La furgoneta esta cargada"
        else :
            return "La furgoneta esta vacia"

class Moto(Vehiculos) : #Clase que hereda de vehiculos
    hcaballito = ""
    def caballito(self) :
        self.hcaballito = "Voy haciendo el caballito"
        print (self.hcaballito)
    #Sobreescribiendo el metodo estado
    def estado(self) :
        print ("Marca: " + str(self.marca) + "\nModelo: " +str(self.modelo) + "\nEn Marcha: " + str(self.enMarcha) +
                "\nAcelerando: " + str(self.acelera) + "\nFrenado: " + str(self.frena) + "\nCaballito: " + str(self.hcaballito))

class BicicletaElectrica(VehiculosElectricos, Vehiculos) :
    pass

miMoto = Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

miBicicleta = BicicletaElectrica("Orbea", "hj")