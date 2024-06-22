from django.shortcuts import render
from django.views.generic import TemplateView
from usuario.views import NonClientActiveUserRequiredMixin
from .models import Movimiento

class VentasView (NonClientActiveUserRequiredMixin,TemplateView):
    template_name = "ventas.html"
    
    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        ventas = Movimiento.objects.filter(activo=True, motivo=1)
        total_ventas = 0
        for venta in ventas:
            total_ventas += venta.precio
        context['total_ventas'] = total_ventas
        context['ventas'] = ventas
        return context