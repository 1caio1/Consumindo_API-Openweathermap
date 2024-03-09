from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import TempoViewset

router = DefaultRouter()
router.register(prefix="clima", viewset=TempoViewset)


urlpatterns = [
    path("api/", include(router.urls))
]
