from django.db import models

class jornada(models.Model):
    id_jornada= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=50)
    inicio= models.TimeField ()
    fin = models.TimeField ()