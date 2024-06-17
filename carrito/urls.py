from django.urls import path
from . import views

urlpatterns = [
    path('', views.Carrito_view.as_view(), name='carrito'),
]
