from django.db import models
from .vehiculo import vehiculo
from .jornada import jornada
from .monitor import monitor

class movimientos(models.Model):
    id_movimiento = models.AutoField(primary_key=True) 
    vehiculo = models.ForeignKey(vehiculo, on_delete=models.CASCADE)
    jornada = models.ForeignKey(jornada, on_delete=models.CASCADE)
    monitor = models.ForeignKey(
        monitor,
        on_delete=models.SET_NULL,  
        null=True,                  
        blank=True
    )
    fecha = models.DateField()
    hora_llegada = models.TimeField()
    hora_salida = models.TimeField()
    punto = models.CharField(
        max_length=20,
        choices=[('entrada', 'Entrada'), ('salida', 'Salida')]
    )