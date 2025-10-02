from rest_framework import serializers
from apps.placas.models.conductor import Conductor

class ConductorSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Conductor
        fields = '__all__'