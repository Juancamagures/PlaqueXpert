from django.db import models
from .vehiculo import Vehiculo
from .jornada import Jornada
from .monitor import Monitor

class Movimientos(models.Model):

    id_movimiento = models.AutoField(primary_key=True) 
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name="movimiento")
    jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE,related_name="movimiento")
    monitor = models.ForeignKey(Monitor, on_delete=models.SET_NULL, null=True, blank=True,related_name="movimiento")
    hora_llegada = models.DateTimeField("Llegada", auto_now=False, auto_now_add=False)
    hora_salida = models.DateTimeField("Salida", auto_now=False, auto_now_add=True)
    punto = models.CharField(max_length=20,choices=[('entrada', 'Entrada'), ('salida', 'Salida')])

    class Meta:

        db_table="movimientos"
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
    
    def __str__ (self):
        return f"[{self.fecha}] {self.vehiculo}"