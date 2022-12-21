from django.db import models

# Create your models here.

class Nombre(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Ingrese su nombre:')

    def __str__(self):
        return self.nombre

class Confirmacion(models.Model):
    confirmar = models.CharField(max_length=50, verbose_name='Escriba la palabra "si" (sin comillas para confirmar su asistencia!) ')