from django.urls import path
from .views import CarritoView, agregar_al_carrito

urlpatterns = [
    path('', CarritoView.as_view(), name='carrito'),
    path('agregar/', agregar_al_carrito, name='agregar_al_carrito'),
]