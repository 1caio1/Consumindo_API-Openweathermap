from rest_framework import viewsets
from .serializers import PrevisaodoTempoSerializer
from ..models import PrevisaodoTempo
import requests
from rest_framework.response import Response
from rest_framework import status


class TempoViewset(viewsets.ModelViewSet):
    serializer_class = PrevisaodoTempoSerializer
    queryset = PrevisaodoTempo.objects.all()

    def create(self, request):
        cidade = request.data.get('cidade', '')
        chave_da_api = '8fb56de87ff0a40e6b526e4ed0c15dcb'  # chave da api
        # url
        url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_da_api}&units=metric'
        response = requests.get(url)
        dados = response.json()
        name = dados.get('name', '')
        temperatura = dados.get('temp', '')
        temperaturaMaxima = dados.get('temp_max',  '')
        temperaturaMinima = dados.get('temp_min', '')
        recebido = {
            'cidade': name,
            'temperatura': temperatura,
            'temperatura_maxima': temperaturaMaxima,
            'temperatura_minima': temperaturaMinima
        }
        serialize = PrevisaodoTempoSerializer(data=recebido)
        if serialize.is_valid():
            serialize.save()
            return response(serialize.data, status=status.HTTP_201_CREATED)
