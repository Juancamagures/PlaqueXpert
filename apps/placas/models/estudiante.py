from django.db import models
from .vehiculo import Vehiculo
from .jornada import Jornada
from .enums import grado

class Estudiante(models.Model):
    id_Estudiante = models.AutoField(primary_key=True)
    vehiculo = models.ForeignKey (Vehiculo, on_delete=models.CASCADE, related_name="estudiante")
    jornada = models. ForeignKey (Jornada, on_delete=models.CASCADE, related_name="estudiante")
    nombres = models.CharField ("Nombres",max_length=100)
    apellidos = models.CharField ("Apellidos",max_length=150)
    identificacion = models.CharField("Identificación",max_length=15)
    grado= models.CharField("Grado",max_length=10,choices=grado.choices)

def __str__(self): 
    return f"{self.nombres} ({self.grado})"
