from rest_framework import serializers
from apps.placas.models.monitor import Monitor

class MonitorSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Monitor
        fields = '__all__'