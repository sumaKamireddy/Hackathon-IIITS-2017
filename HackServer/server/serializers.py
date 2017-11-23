from rest_framework import serializers

from server import models


class LatLonSerializer(serializers.ModelSerializer):
        class Meta:
                model = models.LatLon
                fields = '__all__'

class SoilMoistureSerializer(serializers.ModelSerializer):
        class Meta:
                model = models.SoilMoisture
                fields = '__all__'
class WaterFlowSerializer(serializers.ModelSerializer):
        class Meta:
                model = models.WaterFlow
                fields = '__all__'
class WaterLevelSerializer(serializers.ModelSerializer):
        class Meta:
                model = models.WaterLevel
                fields = '__all__'
