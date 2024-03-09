from rest_framework import serializers
from clima import models


class PrevisaodoTempoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrevisaodoTempo
        fields = '__all__'
