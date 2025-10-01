from django.urls import path
from .views.api import registrar_placa

urlpatterns = [
    path('registrar_placa/', registrar_placa, name='registrar_placa'),
]
