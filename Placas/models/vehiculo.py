from django.db import models
from .propietario import propietario
from .conductor import conductor

class vehiculo (models.Model): 
    id_vehiculo = models.AutoField(primary_key=True)
    propietario = models.ForeignKey(propietario, on_delete=models.CASCADE) 
    conductor = models.ForeignKey(conductor, on_delete=models.CASCADE)
    placa = models.CharField(max_length=6, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    cupos = models.IntegerField
    nickname = models.CharField (max_length=15 , unique=True)

    def __str__ (self):
        return f"{self.placa} - {self.marca} {self.marca}"

