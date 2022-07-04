from django.shortcuts import render
from FamiliaApp.models import Familiar
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
# Create your views here.


def familiares(request):
    familiares = Familiar(nombre='Daniel', apellido='Paredes', dni=3874846, fecha="1968-07-12")
    texto=f"<br>Familiar Agregado {familiares.nombre} {familiares.apellido} DNI: {familiares.dni} Fecha de Nacimiento: {familiares.fecha}</br>\n"
    familiares = Familiar(nombre='Myriam',apellido='Arrighi', dni=16840508, fecha="1965-09-20")
    texto+=f"<br>Familiar Agregado {familiares.nombre} {familiares.apellido} DNI: {familiares.dni} Fecha de Nacimiento: {familiares.fecha}</br>\n"
    familiares = Familiar(nombre='Santina',apellido='Molinari',dni=10180457, fecha="1945-06-20")
    texto+=f"<br>Familiar Agregado {familiares.nombre} {familiares.apellido} DNI: {familiares.dni} Fecha de Nacimiento: {familiares.fecha}</br>\n"
    familiares.save()

    html= open("E:/NuevoProyecto/ProyectoFamilia/FamiliaApp/templates/template.html")

    plantilla= Template(html.read())

    html.close()

    micontexto = Context(familiares)

    texto+=plantilla.render (micontexto)

    return HttpResponse (texto)