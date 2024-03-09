from django.db import models


class PrevisaodoTempo(models.Model):
    id = models.AutoField(primary_key=True)
    cidade = models.CharField( max_length=255, null=False)
    temperatura = models.FloatField(max_length=255)
    temperatura_maxima = models.FloatField(max_length=255)
    temperatura_minima = models.FloatField(max_length=255)
