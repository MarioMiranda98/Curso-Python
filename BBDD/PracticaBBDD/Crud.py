from tkinter import *
from tkinter import messagebox
import sqlite3

#-------------Funciones-------------#
def conexionBD() :
    miConexion = sqlite3.connect("Usuarios")
    cursor = miConexion.cursor()
    try :
        cursor.execute(''' 
            CREATE TABLE datosUsuarios(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBREUSUARIO VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR(50),
                COMENTARIOS VARCHAR(255)
            )
        ''')

        messagebox.showinfo("Base de datos", "Base de datos creada con exito")
    except :
        messagebox.showwarning("Advertencia", "La base de datos ya existe")
    finally :
        cursor.close()
        miConexion.close()

def salirAplicacion() :
    valor = messagebox.askquestion("Salir", "¿Deseas Salir de la Aplicacion?")

    if valor == "yes" :
        root.destroy()

def limpiarCampos() :
    miNombre.set("")
    miID.set("")
    miApellido.set("")
    miPass.set("")
    miDireccion.set("")
    textoComentario.delete("1.0", END)

def crear() :
    miConexion = sqlite3.connect("Usuarios")
    cursor = miConexion.cursor()
    try :
        cursor.execute("INSERT INTO datosUsuarios VALUES (NULL, ?, ? ,?, ?, ?)", (cuadroNombre.get(), cuadroPass.get(), cuadroApellido.get(), cuadroDireccion.get(), textoComentario.get("1.0", END)))
        miConexion.commit()
        messagebox.showinfo("Usuario", "Registro Agregado")
    except :
        messagebox.showwarning("Error", "No se pudo registrar")
    finally :
        cursor.close()
        miConexion.close()

def leer() :
    miConexion = sqlite3.connect("Usuarios")
    cursor = miConexion.cursor()
    try :
        cursor.execute("SELECT * FROM datosUsuarios WHERE ID = " + str(miID.get()))
        usuario = cursor.fetchall()

        for u in usuario :
            miID.set(u[0])
            miNombre.set(u[1])
            miPass.set(u[2])
            miApellido.set(u[3])
            miDireccion.set(u[4])
            textoComentario.insert("1.0", u[5])

        miConexion.commit()
    except :
        messagebox.showwarning("Error", "No se pudo conectar")
    finally :
        cursor.close()
        miConexion.close()

def actualizar() :
    miConexion = sqlite3.connect("Usuarios")
    cursor = miConexion.cursor()
    try :
        cursor.execute("UPDATE datosUsuarios SET NOMBREUSUARIO = ? , PASSWORD =  ? , APELLIDO = ?, DIRECCION = ?, COMENTARIOS = ? WHERE ID = '" + cuadroID.get() +"'", (cuadroNombre.get(), cuadroPass.get(), cuadroApellido.get(), cuadroDireccion.get(), textoComentario.get("1.0", END)))
        miConexion.commit()
        messagebox.showinfo("Usuario", "Actualizado")
    except :
        messagebox.showwarning("Error", "No se pudo actualizar")
    finally :
        cursor.close()
        miConexion.close()

def eliminar() :
    miConexion = sqlite3.connect("Usuarios")
    cursor = miConexion.cursor()
    try :
        cursor.execute("DELETE FROM datosUsuarios WHERE ID = " + cuadroID.get())
        miConexion.commit()
        messagebox.showinfo("Registro Borrado", "Exito")
    except :
        messagebox.showwarning("No se pudo eliminar")
    finally :
        cursor.close()
        miConexion.close()

#-----------Interfaz Gráfica---------#
root = Tk()

barraMenu = Menu(root)
root.config(menu = barraMenu, width = 300, height = 300)

bbddMenu = Menu(barraMenu, tearoff = 0)
bbddMenu.add_command(label = "Conectar", command = conexionBD)
bbddMenu.add_command(label = "Salir", command = salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff = 0)
borrarMenu.add_command(label = "Borrar Campos", command = limpiarCampos)

CRUDMenu = Menu(barraMenu, tearoff = 0)
CRUDMenu.add_command(label = "Create", command = crear)
CRUDMenu.add_command(label = "Read", command = leer)
CRUDMenu.add_command(label = "Update", command = actualizar)
CRUDMenu.add_command(label = "Delete", command = eliminar)

ayudaMenu = Menu(barraMenu, tearoff = 0)
ayudaMenu.add_command(label = "Ayuda")
ayudaMenu.add_command(label = "Acerca de")

barraMenu.add_cascade(label = "BBDD", menu = bbddMenu)
barraMenu.add_cascade(label = "Borrar", menu = borrarMenu)
barraMenu.add_cascade(label = "CRUD", menu = CRUDMenu)
barraMenu.add_cascade(label = "Ayuda", menu = ayudaMenu)

#---------------Comienzo de campos----------#

miFrame = Frame(root)
miFrame.pack()

miID = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()
miDireccion = StringVar()

cuadroID = Entry(miFrame, textvariable = miID)
cuadroID.grid(row = 0, column = 1, padx = 10, pady = 10)

cuadroNombre = Entry(miFrame, textvariable = miNombre)
cuadroNombre.grid(row = 1, column = 1, padx = 10, pady = 10)
cuadroNombre.config(fg = "red", justify = "right")

cuadroPass = Entry(miFrame, textvariable = miPass)
cuadroPass.grid(row = 2, column = 1, padx = 10, pady = 10)
cuadroPass.config(show = "?")

cuadroApellido = Entry(miFrame, textvariable = miApellido)
cuadroApellido.grid(row = 3, column = 1, padx = 10, pady = 10)

cuadroDireccion = Entry(miFrame, textvariable = miDireccion)
cuadroDireccion.grid(row = 4, column = 1, padx = 10, pady = 10)

textoComentario = Text(miFrame, width = 16, height = 5)
textoComentario.grid(row = 5, column = 1, padx = 10, pady = 10)
scroll = Scrollbar(miFrame, command = textoComentario.yview)
scroll.grid(row = 5, column = 2, sticky = "nsew")
textoComentario.config(yscrollcommand = scroll.set)

#-----------------Comenzando labels-------------#
Label(miFrame, text = "ID:").grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "e")
Label(miFrame, text = "Nombre:").grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "e")
Label(miFrame, text = "Password:").grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "e")
Label(miFrame, text = "Apellido").grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "e")
Label(miFrame, text = "Direccion:").grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "e")
Label(miFrame, text = "Comentario:").grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "e")

#----------------Comenzando los botones-----------#
miFrame2 = Frame()
miFrame2.pack()

botonCrear = Button(miFrame2, text = "Crear", command = crear)
botonCrear.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "e")

botonLeer = Button(miFrame2, text = "Leer", command = leer)
botonLeer.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "e")

botonActualizar = Button(miFrame2, text = "Actualizar", command = actualizar)
botonActualizar.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = "e")

botonBorrar = Button(miFrame2, text = "Borrar", command = eliminar)
botonBorrar.grid(row = 0, column = 3, padx = 10, pady = 10, sticky ="e")

root.mainloop()