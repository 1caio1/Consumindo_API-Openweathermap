from django.db import models

#para criação do banco
class PrevisaodoTempo(models.Model):
    id = models.AutoField(primary_key=True)
    cidade = models.CharField( max_length=255, null=False, blank=True)
    temperatura = models.CharField(max_length=255, blank=True)
    temperatura_maxima = models.CharField(max_length=255, blank=True)
    temperatura_minima = models.CharField(max_length=255, blank=True)
    
    
