from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Location
from .serializers import LocationSerializer
from typing import Type


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class: Type[LocationSerializer] = LocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
