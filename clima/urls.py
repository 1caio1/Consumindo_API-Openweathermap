from django.urls import path
from .views import Climaview

urlpatterns = [
    path('weather/<str:city>/', Climaview.as_view(), name='weather')
]
