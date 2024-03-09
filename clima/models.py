from django.db import models


class PrevisaodoTempo(models.Model):
    cidade = models.CharField(primary_key= True, max_length=255, null=False)
    temperatura = models.FloatField(max_length=255)
    temperatura_maxima = models.FloatField(max_length=255)
    temperatura_minima = models.FloatField(max_length=255)
