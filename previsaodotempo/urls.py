from django.contrib import admin
from django.urls import path, include




#caminhos
urlpatterns = [
    path('', include('clima.api.urls')),
    path('admin/', admin.site.urls)

]
