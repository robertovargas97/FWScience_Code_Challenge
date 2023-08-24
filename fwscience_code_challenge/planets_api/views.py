from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Planet
from .serializers import PlanetSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
