from django.db import models
from .propietario import Propietario
from .conductor import Conductor
import uuid

class Vehiculo (models.Model): 
    
    #id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False, unique= True)
    id_vehiculo = models.AutoField(primary_key=True)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name="vehiculo") 
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE,related_name="vehiculo")
    placa = models.CharField("Placa",max_length=6, unique=True)
    marca = models.CharField("Marca", max_length=50)
    modelo = models.CharField("Modelo",max_length=50)
    color = models.CharField("Color",max_length=50)
    cupos = models.IntegerField("Cupos", default=0)
    nickname = models.CharField ("Nickname",max_length=15 , unique=True)

    class Meta:

        db_table="vehiculo"
        ordering=["placa"]
        verbose_name = 'vehículo'
        verbose_name_plural = 'Vehículos'
        get_latest_by= 'placa'
    
    def save(self, *args, **kwargs):
        self.placa = self.placa.upper()
        super().save(*args, **kwargs)


    def __str__ (self):
        return f"{self.placa}"

"""
    db_table:Nombre personalizado de la tabla en la base de datos.
    ordering: Lista de campos por los que se ordenarán los resultados por defecto.
    verbose_name: Nombre legible en singular para el modelo.
    verbose_name_plural: Nombre legible en plural para el modelo.
    unique_together: Define combinaciones de campos que deben ser únicas.
    index_together: Define combinaciones de campos que deben ser indexadas juntas.
    permissions: Lista de permisos personalizados.
    default_related_name:Nombre por defecto para relaciones inversas.
    get_latest_by: Campo usado por Model.objects.latest().
    abstract: Si es True, el modelo es abstracto (no se crea tabla).
    managed: Si es False, Django no gestionará la tabla (útil para tablas existentes).
    app_label: Especifica a qué aplicación pertenece el modelo (cuando está fuera de una app).
    default_permissions: Lista de permisos que Django crea automáticamente (add, change, etc.).

    2. Métodos de la clase Meta:
        Puedes sobrescribirla para agregar lógica antes o después de guardar un objeto.
        Ejemplo:
        def save(self, *args, **kwargs):
            self.nombre = self.nombre.upper()
            super().save(*args, **kwargs)

        Sobrescribe esta función si necesitas lógica personalizada al eliminar un objeto.
        Ejemplo:
        def delete(self, *args, **kwargs):
            print(f"Eliminando {self.nombre}")
            super().delete(*args, **kwargs)

        Permite validar el modelo antes de guardarlo. Se usa junto con formularios o full_clean().
            from django.core.exceptions import ValidationError

        def clean(self):
            if self.precio < 0:
            raise ValidationError("El precio no puede ser negativo.")

        Valida todos los campos del modelo, incluyendo clean() y validaciones de campo.
            producto.full_clean()
"""
