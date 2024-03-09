from rest_framework.serializers import ModelSerializer
from clima import models



class PrevisaodoTempoSerializer(ModelSerializer):
    class Meta:
        model = models.PrevisaodoTempo
        fields = '__all__'
