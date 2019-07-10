class Persona() : 
    def __init__(self, nombre, edad, lugarResidencia) :
        self.nombre = nombre
        self.edad = edad 
        self.lugarResidencia = lugarResidencia

    def descripcion(self) :
        print ("Nombre: " + str(self.nombre) + "\nEdad: " + str(self.edad) + "\nLugar de Residencia: " + str(self.lugarResidencia))

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre, edad, lugarResidencia) :
        super().__init__(nombre, edad, lugarResidencia)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self) :
        super().descripcion()
        print ("\nSalario: " + str(self.salario) + "\nAntiguedad: " + str(self.antiguedad))

Manuel = Empleado(1500, 15, "Manuel", 55, "Colombia")
Manuel.descripcion()

print (isinstance (Manuel, Persona))