from django.db import models
from .enums import tipo_monitor_institucion

class monitor(models.Model):
    monitor_id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    identificacion = models.CharField(max_length=15)
    tipo_monitor = models.CharField(
        max_length=12,
        choices=tipo_monitor_institucion.choices,
        null=True,     
        blank=True,
        default=None
    )

