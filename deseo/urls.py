from django.urls import path
from .views import ListaDeseosView, agregar_a_deseos, eliminar_de_deseos

urlpatterns = [
    path('', ListaDeseosView.as_view(), name='lista_deseos'),
    path('agregar/', agregar_a_deseos, name='agregar_a_deseos'),
    path('eliminar/', eliminar_de_deseos, name='eliminar_de_deseos'),
]
