from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PrevisaodoTempo
import requests


# get funcionando
class Climaview(APIView):
    def get_clima(self, cidade):
        chave_da_api = '8fb56de87ff0a40e6b526e4ed0c15dcb'  # chave da api
        # url
        url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_da_api}&units=metric'
        response = requests.get(url)
        dados = response.json()

        return dados
    # retorna os dados da api

    def get(self, request, city):
        dados = self.get_clima(city)
        temperatura = dados.get('main','').get('temp')
        temperaturaMaxima = dados.get('main','').get('temp_max')
        temperaturaMinima = dados.get('main','').get('temp_min')

        # cria um dicionario
        data = {
            'temperatura' : temperatura,
            'temperatura_maxima': temperaturaMaxima,
            'temperatura_minima': temperaturaMinima
        }

        return Response(data)
