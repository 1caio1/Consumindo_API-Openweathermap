from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import TempoViewset
from ..views import Climaview

router = DefaultRouter()
router.register(prefix="clima", viewset=TempoViewset)


urlpatterns = [
    path("api/", include(router.urls)),
    path('clima/<str:city>/', Climaview.as_view(), name='weather'),
]
