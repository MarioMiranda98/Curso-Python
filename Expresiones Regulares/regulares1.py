import re

cadena = "Vamos a aprender expresiones regulares en python, python es un lenguaje de sintaxis sencilla"

print("Metodo search, hacer la busqueda de un string donde coincida")
print(re.search("aprender", cadena)) #Si esta devuelve un objeto, si no devuelve none

if re.search("aprender", cadena) is not None :
    print ("Se ha encontrado el texto")
else :
    print ("No se ha encontrado el texto")

texto = re.search("aprender", cadena)

print("start devuelve el inicio del caracter de la palabra (posicion)")
print(texto.start())

print("el metodo end devuelve el caracter final de la palabra (posicion)")
print(texto.end())

print ("El metodo span devuelve en una tupla el caracter donde comienza la palabra encontrada y el caracter final (posicion)")
print(texto.span())

print("El metodo findall devuelve una lista con todas las apariciones de lo buscado")
print(re.findall("python", cadena))