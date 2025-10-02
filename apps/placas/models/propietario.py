from django.db import models 

class Propietario (models.Model):

    id_propietario = models.AutoField(primary_key=True)
    nombres = models.CharField("Nombres", max_length=100)
    apellidos = models.CharField("Apellidos",max_length=150)
    identificacion = models.CharField("Identificación",max_length=15)
    telefono = models.CharField("Teléfono",max_length=10)
    correo_electronico = models.CharField("Correo Electrónico",max_length=240)

    class Meta:

        db_table="propietario"
        verbose_name = 'Propietario'
        verbose_name_plural = 'Propietarios'
    
    def __str__ (self):
        return f"{self.nombres} {self.apellidos}"