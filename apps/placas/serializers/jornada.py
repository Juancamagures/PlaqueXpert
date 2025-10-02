from rest_framework import serializers
from apps.placas.models.jornada import Jornada

class JornadaSerializers(serializers.ModelSerializer):

    class Meta:
        model=Jornada
        fields = '__all__'