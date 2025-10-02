from rest_framework import serializers
from apps.placas.models.vehiculo import Vehiculo
from apps.placas.serializers.propietario import PropietarioSerializers,Propietario
from apps.placas.serializers.conductor import ConductorSerializers, Conductor

class VehiculoSerializers(serializers.ModelSerializer):

    class Meta:
        model=Vehiculo
        fields = '__all__'
    
    propietario = serializers.PrimaryKeyRelatedField(
        queryset=Propietario.objects.all(),
        many=False,
        write_only=True)
    
    conductor = serializers.PrimaryKeyRelatedField(
        queryset=Conductor.objects.all(),
        many=False,
        write_only=True)
    
    propietario_detalle = PropietarioSerializers(source='propietario', read_only=True)
    conductor_detalle = ConductorSerializers(source='conductor', read_only=True)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['propietario'] = rep.pop('propietario_detalle')
        rep['conductor'] = rep.pop('conductor_detalle')
        return rep