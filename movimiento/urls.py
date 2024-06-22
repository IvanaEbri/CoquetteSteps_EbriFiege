from django.urls import path
from . import views

urlpatterns = [
    path('', views.VentasView.as_view(), name='ventas'),
]