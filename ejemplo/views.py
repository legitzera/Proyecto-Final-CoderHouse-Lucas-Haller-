from django.template import Template, Context, loader
from django.http import HttpResponse

import datetime
import random
from miapp.models import *

def saludar (request):
    return HttpResponse("Este es el mensaje de saludo")

def parametro (request, nombre):
    respuesta = f"Este es el mensaje de saludo con parametro: {nombre}"
    return HttpResponse (respuesta)

def html_hoy (request):
    hoy = datetime.datetime.now()
    respuesta = f"""
    <html>
    <h1> Ejemplo con HTML </h1>
    <h2> h2 es para algo mas chico </h2>
    <h3> ejemplo de hoy es: {hoy} </h3>
    </html>
    """
    return HttpResponse (respuesta) 

def ejemplo_template(request):
    miHtml = open("C:/Users/Usuario/Desktop/Programmer/PAG 1/ejemplo/ejemplo/plantillas/ejemplo.html")
    plantilla = Template(miHtml.read())
    miHtml.close ()
    contexto = Context()
    respuesta = plantilla.render(contexto)
    return HttpResponse(respuesta)

def ejemploMejor(request):
    hoy = datetime.datetime.now()
    nombre = "legit"
    apellido = "zera"
    notas = [4,5,6,7,8,9]
    contexto = {"nombre" : nombre, "apellido" : apellido, "hoy" : hoy, "notas" : notas}
    plantilla = loader.get_template("ejemplomejor.html")
    respuesta = plantilla.render(contexto)
    return HttpResponse(respuesta)

def nuevo_curso(request):
    iComision = random.randint(20000,30000)
    sNombre = "Python " + str(iComision)
    curso = Curso(nombre=sNombre, comision=iComision)
    curso.save()
    respuesta = f"<html><h1>El curso nuevo es {sNombre} : {iComision}</h1></html>"
    return HttpResponse(respuesta)


