from django.http import HttpResponse;
#podemos declarar una vista, con tan solo declarar una funcion en python.

"""
Este metodo recibe un request como parametro: Es nuestra primera vista.
para que esta vista sea acesible, se tiene que realizar una configuración 
en el archivo urls.py, en el que agregaremos la ruta de nuestro hacia esta vista 
llamada saludo.
"""
def saludo(request):
    return HttpResponse("Hola, esta es nuestra primera vista");

def despedida(request):
    return HttpResponse("Hasta luego");

