from django.db import models
from .enums import tipo_licencia

class Conductor(models.Model):
    
    id_conductor = models.AutoField(primary_key=True)
    nombres = models.CharField("Nombres",max_length=150)
    apellidos = models.CharField("Apellidos",max_length=150)
    identificacion = models.CharField("Identificación",max_length=15)
    telefono = models.CharField("Teléfono",max_length=15)
    clase_licencia = models.CharField("Licencia",max_length=2, choices=tipo_licencia.choices)

    class Meta:

        db_table="conductor"
        verbose_name = 'Conductor'
        verbose_name_plural = 'Conductores'

    def __str__ (self):
        return f"{self.nombres} {self.apellidos}"

