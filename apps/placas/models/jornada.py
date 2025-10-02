from django.db import models

class Jornada(models.Model):
    id_jornada= models.AutoField(primary_key=True)
    nombre= models.CharField("Jornada",max_length=50)
    inicio= models.TimeField ("Inicio")
    fin = models.TimeField ("Final")

    class Meta:
        db_table="jornada"
        verbose_name = 'Jornada'
        verbose_name_plural = 'Jornadas'
    
    def __str__ (self):
        return f"{self.nombre}"