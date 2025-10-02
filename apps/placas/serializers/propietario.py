from rest_framework import serializers
from apps.placas.models.propietario import Propietario

class PropietarioSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Propietario
        fields = '__all__'