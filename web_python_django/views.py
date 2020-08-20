from django.http import HttpResponse;
#podemos declarar una vista, con tan solo declarar una funcion en python.
import datetime

"""
Este metodo recibe un request como parametro: Es nuestra primera vista.
para que esta vista sea acesible, se tiene que realizar una configuración 
en el archivo urls.py, en el que agregaremos la ruta de nuestro hacia esta vista 
llamada saludo.
"""
def saludo(request):
    return HttpResponse("Hola, esta es nuestra primera vista")

def despedida(request):
    return HttpResponse("Hasta luego")


def dameFecha(requuest):
    fecha_actual=datetime.datetime.now()
    document= """ 
    <html>
    <head></head>
    <h2>
    Fecha y hora actuales: %s 
    </h2>
    <body></body>
    </html>""" % fecha_actual

    return HttpResponse(document);

def calulaEdad(response,agno,edad):
    #edadActual = 18
    periodo=agno-2020
    edadFutura=edad+periodo

    document = """ 
    <html>
    <head></head>
    <h2>
    En el año %s tendras % años
    </h2>
    <body></body>
    </html>""" %(agno,edadFutura)

    return HttpResponse(document);