from django.db import models
from .vehiculo import vehiculo
from .jornada import jornada
from .enums import grado

class estudiante(models.Model):
    id_Estudiante = models.AutoField(primary_key=True)
    vehiculo = models.ForeignKey (vehiculo, on_delete=models.CASCADE)
    jornada = models. ForeignKey (jornada, on_delete=models.CASCADE)
    nombres = models.CharField (max_length=100)
    apellidos = models.CharField (max_length=150)
    identificacion = models.CharField(max_length=15)
    grado= models.CharField(
        max_length=10,
        choices=grado.choices
    )

def __str__(self): 
    return f"{self.nombres} ({self.grado})"
