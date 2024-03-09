from django.db import models



class PrevisaodoTempo(models.Model):
    temperatura = models.FloatField()
    temperatura_maxima = models.FloatField()
    temperatura_minima = models.FloatField()
    
    
    
    
    
