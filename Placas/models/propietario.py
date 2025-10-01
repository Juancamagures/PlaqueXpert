from django.db import models 

class propietario (models.Model):
    id_propietario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    identificacion = models.CharField(max_length=15)
    telefono = models.CharField(max_length=10)
    correo_electronico = models.CharField(max_length=240)
