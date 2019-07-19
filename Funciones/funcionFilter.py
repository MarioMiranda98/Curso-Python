'''def numeroPar(num) :
    if num % 2 == 0 :
        return True'''

'''numeros = [17, 24, 7, 39, 8, 21, 92]
print(list(filter(lambda numeroPar : numeroPar % 2 == 0, numeros)))'''

class Empleados() :
    def __init__(self, nombre, cargo, salario) :
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self) :
        return "{} que trabaja como {}, que tiene salario de {} $".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [
    Empleados("Juan", "Director", 75000),
    Empleados("Ana", "Presidenta", 85000),
    Empleados("Antonio", "Administrativo", 25000),
    Empleados("Sara", "Secretaria", 27000),
    Empleados("Mario", "Botones", 21000)
]

salariosAltos = filter(lambda empleados : empleados.salario > 50000, listaEmpleados)

for s in salariosAltos :
    print(s)