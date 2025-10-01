from django.db import models
from .enums import tipo_licencia

class conductor(models.Model):
    id_conductor = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    identificacion = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)

    clase_licencia = models.CharField(
        max_length=2,
        choices=tipo_licencia.choices
    )
