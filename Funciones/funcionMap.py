class Empleados() :
    def __init__(self, nombre, cargo, salario) :
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self) :
        return "{} que trabaja como {}, que tiene salario de {} $".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [
    Empleados("Juan", "Director", 6700),
    Empleados("Ana", "Presidenta", 7500),
    Empleados("Antonio", "Administrativo", 2150),
    Empleados("Sara", "Secretaria", 2000),
    Empleados("Mario", "Botones", 1800)
]

def calculoComision(empleado) :
    if empleado.salario <= 3000 :
        empleado.salario = empleado.salario * 1.03
    return empleado

listaEmpleados = map(calculoComision, listaEmpleados)
for l in listaEmpleados :
    print(l)