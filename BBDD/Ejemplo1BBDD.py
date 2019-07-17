import sqlite3

conexion = sqlite3.connect("PrimeraBase") #Creacion de la base de datos
cursor = conexion.cursor() #Creamos el cursor o puntero

#Crear la tabla
cursor.execute('CREATE TABLE IF NOT EXISTS PRODUCTOS (NOMBREARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))') #Para usar los querys

#Insertar registros
#cursor.execute("INSERT INTO PRODUCTOS VALUES ('Balon', 15, 'Deportes')") #Orden (Ejecucion)
#conexion.commit() #Confirmacion

#varios registros
variosProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria")
]

#cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
conexion.commit()

cursor.execute("SELECT * FROM PRODUCTOS")
recuperaProductos = cursor.fetchall() #Recuperar registros, convierte la variable en una lista [ ]
#print (recuperaProductos)

for productos in recuperaProductos :
    print ("Nombre producto: " + str(productos[0]) + " Seccion: " + str(productos[2]))

conexion.close()