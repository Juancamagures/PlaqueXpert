from rest_framework import serializers
from apps.placas.models.movimientos import Movimientos

class MovimientoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Movimientos
        fields = '__all__'
        read_only_fields = ['hora_llegada', 'hora_salida']