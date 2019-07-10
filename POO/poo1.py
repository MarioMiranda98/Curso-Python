class Coche() :
    def __init__ (self) : #Constructor
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 #__ (Dos guiones) es equivalente a protected
        self.__enMarcha = False

    def arrancar(self, arrancamos) : #Siempre colocar el self equivalente al this
        self.__enMarcha = arrancamos

        if self.__enMarcha == True :
            chequeo = self.__chequeoInterno()
            #print(chequeo)

        if (self.__enMarcha and chequeo) :
            return "El coche esta en marcha"
        elif (self.__enMarcha and chequeo == False) :
            return "Algo ha ido mal en el chequeo, no se puede arrancar"
        else :
            return "El coche esta parado"


    def estado(self) :
        print ("El coche tiene " + str(self.__ruedas) + " Un ancho de " + str(self.__anchoChasis) + " y un largo de " + str(self.__largoChasis))
       #Para acceder a esta variable protected hay que poner dos guiones antes de la llamada

    def __chequeoInterno(self) :
        print ("Realizando chequeo interno")
        self.gasolina = "Ok"
        self.aceite = "Ok"
        self.puertas = "Cerradas"

        if (self.gasolina == "Ok" and self.aceite =="Ok" and self.puertas == "Cerradas") :
            #print ("Todo bien")
            return True
        else :
            #print ("Algo mal")
            return False

miCoche = Coche()
#print ("El largo del coche es: " + str(miCoche.largoChasis))
#print ("El coche tiene " + str(miCoche.ruedas) + " ruedas")
print (miCoche.arrancar(True))
miCoche.estado()

print ("------------------A continuacion creamos el segundo objeto-------------------------")
miCoche2 = Coche()
#print ("El largo del coche es: " + str(miCoche2.largoChasis))
#print ("El coche tiene " + str(miCoche2.ruedas) + " ruedas")
print (miCoche2.arrancar(False))
#miCoche2.ruedas = 5
miCoche2.estado()