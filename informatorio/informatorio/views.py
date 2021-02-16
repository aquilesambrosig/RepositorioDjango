
from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context
from django.shortcuts import render

import datetime



class Persona:
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido



def saludo(request):

	p1 = Persona('Aquiles', 'Kere')

	#nombre = 'Aquileskere'

	meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Setiembre', 'Octubre', 'Noviembre', 'Diciembre']

	fecha_actual = datetime.datetime.now()
	mes_nombre = meses[fecha_actual.month - 1]
	# template = loader.get_template('plantilla-saludo.html')
	context = {
	'nombre_persona':p1.nombre, 
	'apellido_persona': p1.apellido,
	'fecha_actual':fecha_actual, 
	'mes_nombre':mes_nombre,
	'meses':meses
	 }

	#documento = template.render(context, request)
	#return HttpResponse(documento)
	return render(request, "plantilla-saludo.html", context )


def mostrarhora(request):
	fecha_actual = datetime.datetime.now()
	documento = """<html>
	<body>
	<h2>
	Fecha y hora actuales %s
	</h2>
	</body>
	</html>
	""" %fecha_actual

	return HttpResponse(documento)

def calculaEdad(request, anio, edadActual):
	
	periodo = anio - 2021
	edadFutura = edadActual + periodo
	documento = """<html>
	<body>
	<h2>
	En el año %s tendras la edad de %s años
	</h2>
	</body>
	</html>
	""" %(anio, edadFutura)

	return HttpResponse(documento)


def cartas(request):
	fecha_actual = datetime.datetime.now()
	context = {'dameFecha': fecha_actual}
	return render(request, "cartas.html", context)
