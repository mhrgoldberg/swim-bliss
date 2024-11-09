from rest_framework import serializers
from .models import Location
from django.contrib.gis.geos import Point
from typing import Dict, Optional, List


class LocationSerializer(serializers.ModelSerializer):
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ('id', 'name', 'description', 'coordinates', 'is_public', 'created_by')

    def get_coordinates(self, obj: Location) -> Optional[Dict[str, str | List[float]]]:
        if isinstance(obj.coordinates, Point):
            return {
                "type": "Point",
                "coordinates": [obj.coordinates.x, obj.coordinates.y]
            }
        return None
