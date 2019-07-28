from django.http import HttpResponse

def saludo(request) :
    return HttpResponse("Hola mundo, primer pagina con Django")

def despedida(request) :
    return HttpResponse("Hasta Luego !!")