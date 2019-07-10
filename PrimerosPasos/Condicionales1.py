print ("Programa de evaluacion de notas de alumno")

notaAlumno = int(input("Introduce la nota del alumno: "))

def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion

print (evaluacion(notaAlumno))