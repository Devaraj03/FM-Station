from rest_framework import serializers
from .models import Station

class StationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'