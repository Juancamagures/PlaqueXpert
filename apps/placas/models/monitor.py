from django.db import models
from .enums import tipo_monitor_institucion

class Monitor(models.Model):
    monitor_id = models.AutoField(primary_key=True)
    nombres = models.CharField("Nombres",max_length=100)
    apellidos = models.CharField("Apellidos",max_length=150)
    identificacion = models.CharField("Identificación",max_length=15)
    tipo_monitor = models.CharField("Tipo",max_length=12,choices=tipo_monitor_institucion.choices, null=True,     blank=True,default=None)


    class Meta:
        db_table="monitor"
        verbose_name = 'monitor'
        verbose_name_plural = 'monitores'
    
    def __str__ (self):
        return f"{self.nombres} {self.apellidos}"