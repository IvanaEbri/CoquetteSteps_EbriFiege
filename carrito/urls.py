from django.urls import path
from .views import CarritoView, agregar_al_carrito, eliminar_del_carrito, CheckoutView

urlpatterns = [
    path('', CarritoView.as_view(), name='carrito'),
    path('agregar/', agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('checkout/', CheckoutView.as_view(), name='checkout_view'),
]