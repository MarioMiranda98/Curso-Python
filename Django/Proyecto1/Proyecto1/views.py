from django.http import HttpResponse
import datetime

def saludo(request) :
    return HttpResponse("<html><body><h1>Hola mundo, primer pagina con Django</h1></body></html>")

def despedida(request) :
    return HttpResponse("Hasta Luego !!")

def dameFecha(request) :
    fechaActual = datetime.datetime.now()
    return HttpResponse("<html><body><h1>Fecha y hora Actual: %s</h1></body></html>" %fechaActual)

def calculaEdad(request, anio, edadPersona) :
    edadActual = edadPersona
    periodo = anio - 2019
    edadFutura = edadActual + periodo
    documento = "<html><body><h2>En el año %s tendras %s años</h2></body></html>"%(anio, edadFutura)
    return HttpResponse(documento)
