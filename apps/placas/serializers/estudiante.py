from rest_framework import serializers
from apps.placas.models.estudiante import Estudiante

class EstudianteSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Estudiante
        fields = '__all__'