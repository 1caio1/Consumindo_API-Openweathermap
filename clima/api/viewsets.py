from rest_framework import viewsets
from .serializers import PrevisaodoTempoSerializer
from ..models import PrevisaodoTempo
import requests
from rest_framework.response import Response



class TempoViewset(viewsets.ModelViewSet):
    serializer_class = PrevisaodoTempoSerializer
    queryset = PrevisaodoTempo.objects.all()

#funcao create 
    def create(self, request):
        cidade = request.data.get('cidade', '')
        chave_da_api = '8fb56de87ff0a40e6b526e4ed0c15dcb' # chave da api
        # url
        url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_da_api}&units=metric'
      
        respostas = requests.get(url)
        dados = respostas.json()
        #dados captados para api
        name = dados.get('name', '')
        temperatura = dados.get('main', '').get('temp')
        temperaturaMaxima = dados.get('main', '').get('temp_max')
        temperaturaMinima = dados.get('main', '').get('temp_min')
        
        #referenciando json
        recebido = {
            'cidade': f'{name}',
            'temperatura': f'{temperatura}',
            'temperatura_maxima': f'{temperaturaMaxima}',
            'temperatura_minima': f'{temperaturaMinima}',
        }
        
        serialize = PrevisaodoTempoSerializer(data=recebido)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
