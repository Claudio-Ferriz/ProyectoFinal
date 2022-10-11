from tabnanny import verbose
from django.db import models

# Create your models here.

class Autor(models.Model):
 
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30) 
    
    def __str__(self):
        return self.nombre


class Articulo(models.Model):

    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=1000)
    fecha = models.DateField(null = True)


class Seccion(models.Model):

    nombre = models.CharField(max_length=50)   
