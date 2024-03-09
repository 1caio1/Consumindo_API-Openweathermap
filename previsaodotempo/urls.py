from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clima.api import viewsets as TempoViewset

route = routers.DefaultRouter()
route.register(r'clima', TempoViewset.TempoViewset, basename="clima")

urlpatterns = [
    path('clima/', include('clima.urls')),
    path('', include(route.urls))

]
