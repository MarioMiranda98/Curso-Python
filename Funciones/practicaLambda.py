#Una funcion lambda es una funcion anonima
#Variable a guardar = lambda parametros : lo que se desea retornar
#los : siginifican return
areaTriangulo = lambda base, altura : ((base * altura) / 2)
print(areaTriangulo(8, 5))

alCubo = lambda numero : numero ** 3
print(alCubo(3))

destacarValor = lambda comision : "{} $".format(comision)
comisionAna = 15338
print(destacarValor(comisionAna))