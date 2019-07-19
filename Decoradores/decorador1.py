#Los decoradores añaden funcionalidad extra a una funcion
#Se conforma de tres funciones A, B, C, recibe A como parametro B y devuelve C
def funcionDecoradora(funcionParametro) :
    def funcionInterior(*args, **kwargs) : #Aqui si la funcion recibe parametros
        #Acciones adicionales que decoran
        print("Vamos a realizar un calculo")
        funcionParametro(*args, **kwargs)
        #Mas acciones
        print("Se ha terminado el calculo")
    
    return funcionInterior

@funcionDecoradora
def suma(num1, num2, num3, num4) :
    print (num1 + num2 + num3 + num4)

@funcionDecoradora
def resta(num1, num2) :
    print (num1 - num2)
    
@funcionDecoradora
def potencia(base, exponente) :
    print(base ** exponente)

suma(7, 5, 8, 10)
resta(12, 10)
potencia(base = 5, exponente = 3)