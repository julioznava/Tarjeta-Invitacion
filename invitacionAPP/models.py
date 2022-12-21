from django.db import models

# Create your models here.

class Confirmacion(models.Model):
    confirmar = models.CharField(max_length=50, verbose_name='Confirmar')


class Nombre(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='', null=False, blank=False)

    def __str__(self):
        return self.nombre


