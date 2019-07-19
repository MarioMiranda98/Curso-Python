import re

listaNombres = ['Ana Gomez', 'Maria Martin', 'Sandra Lopez', 'Santiago Martin', 'Sandra Fernandez']
print("Las anclas buscan todas las coincidencias dentro de una lista")
#^ todo lo que empieze con lo que se le indique
#$ para cada lo que termine
#[] el texto dentro de los corchetes se vuelve un patron de caracteres a buscar
#Dentro de los corchetes se pueden hacer variaciones
for elemento in listaNombres :
    if (re.findall("Martin$", elemento)) :
        print(elemento)