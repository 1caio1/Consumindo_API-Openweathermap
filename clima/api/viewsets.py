from rest_framework import viewsets
from clima.api import serializers
from clima import models


class TempoViewset(viewsets.ModelViewSet):
    serializer_class = serializers.PrevisaodoTempoSerializer
    queryset = models.PrevisaodoTempo.objects.all()
