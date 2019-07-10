def generaPares(limite) :#Funcion normal
    num = 1
    miLista = []
    while num < limite :
        miLista.append(num*2)
        num += 1
    
    return miLista

print ("Usando funcion normal")
print (generaPares(10))

print ("Usando generadores")
def generarPares(limite) :#Generador
    num = 1
    while num < limite :
        yield num*2#Genera objeto iterable
        num += 1

damePares = generarPares(10)

#for i in damePares :
#    print (i)

print ("Usando Next")
print (next(damePares))
print (next(damePares))
print (next(damePares))