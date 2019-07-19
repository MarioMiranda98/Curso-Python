import re
#Rangos nos ayuda a buscar rangos de caracteres o numeros

lista = ['Ana', 'Pedro', 'Maria', 'Rosa', 'Celia', "Sandra"]

for elemento in lista :
    if re.findall('[o-t]$', elemento) :
        print (elemento)

ciudades = ['Ma1', 'Se1', 'Ma2', 'Ba1', 'Ma3', 'Va1', 'Va2', 'Ma4', 'Ma5', 'MaA', 'MaB', 'MaC']

#Para negar el rango se coloca primero en los corchetes antes de añadir el rango
for elemento in ciudades :
    if re.findall('Ma[0-3A-B]', elemento) :
        print (elemento)