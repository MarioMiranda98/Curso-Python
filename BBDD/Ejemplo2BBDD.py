import sqlite3

conexion = sqlite3.connect("Gestion Productos")
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS PRODUCTOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBREARTICULO VARCHAR(50) UNIQUE,
        PRECIO INTEGER,
        SECCION VARCHAR(20)
    )
''')

productos = [
    ("Pelota", 20, "Jugueteria"),
    ("Pantalon", 15, "Confeccion"),
    ("Destornillador", 25, "Ferreteria"),
    ("Jarron", 45, "Ceramica")
]

#cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL, ?, ?, ?)", productos)
#cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'Confeccion'")
#pro = cursor.fetchall()
#print(pro)
#cursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBREARTICULO = 'Pelota'")
cursor.execute("DELETE FROM PRODUCTOS WHERE ID = 2")
conexion.commit()
conexion.close()