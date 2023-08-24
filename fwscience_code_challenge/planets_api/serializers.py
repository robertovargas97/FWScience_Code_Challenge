from rest_framework import serializers

from .models import Planet


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = [
            "id",
            "name",
            "population",
            "terrains",
            "climates",
        ]

    terrains = serializers.ListField(
        child=serializers.CharField(required=False), required=False
    )
    climates = serializers.ListField(
        child=serializers.CharField(required=False), required=False
    )
