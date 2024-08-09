from django.urls import path
from .views import RotaProtegida

urlpatterns = [
    path('protegido/', RotaProtegida.as_view(), name='rota_protegida'),
]