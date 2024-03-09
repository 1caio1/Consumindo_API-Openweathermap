from django.db import models
#


class PrevisaodoTempo(models.Model):
    cidade = models.CharField(max_length=255)
    temperatura = models.FloatField()
    temperatura_maxima = models.FloatField()
    temperatura_minima = models.FloatField()
    umidade = models.FloatField()
