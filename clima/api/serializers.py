from rest_framework.serializers import ModelSerializer
from ..models import PrevisaodoTempo




class PrevisaodoTempoSerializer(ModelSerializer):
    class Meta:
        model = PrevisaodoTempo
        fields = ['id', 'cidade', 'temperatura', 'temperatura_maxima', 'temperatura_minima']
