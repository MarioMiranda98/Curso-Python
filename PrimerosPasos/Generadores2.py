def devuelveCiudades(*Ciudades) : # * indica que recibira n elementos en forma de tupla
    for elementos in Ciudades :
        #for subElemento in elementos :
        yield from elementos #Sirve para hacer como bucles for anidados

ciudadesDevueltas = devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print (next(ciudadesDevueltas))
print (next(ciudadesDevueltas))