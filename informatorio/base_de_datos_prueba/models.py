from django.db import models

# Create your models here.

class clientes(models.Model):
	nombre = models.CharField(max_length=30)
	direccion = models.CharField(max_length=50)
	telefono = models.IntegerField()
	email = models.EmailField()
	fecha_alta = models.DateField()


class vendedores(models.Model):
	nombre = models.CharField(max_length=30)
	direccion = models.CharField(max_length=50)
	telefono = models.IntegerField()
	email = models.EmailField()
	fecha_alta = models.DateField()
