from rest_framework import serializers
from .models import PrevisaodoTempo


class PrevisaodoTempoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PrevisaodoTempo
        fields = ['temperatura', 'temperatura_maxima', 'temperatura_minima']

