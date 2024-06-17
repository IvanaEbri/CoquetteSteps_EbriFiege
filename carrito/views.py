from django.shortcuts import render
from django.views.generic import TemplateView
from calzado.models import Calzado
from django.shortcuts import redirect
from django.urls import reverse
from categoria.models import Categoria
from usuario.models import Usuario
from carrito.models import Carrito
from usuario.views import ActiveClientLoginRequiredMixin


class Carrito_view(ActiveClientLoginRequiredMixin, TemplateView):
    template_name = "cart.html"
    
    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        total_carro = 0
        usuario_act = self.request.user
        carro = usuario_act.productos_carro()

        #total de compra
        for producto in carro:
            total_carro += producto.calzado.precio

        context["category"] = Categoria.objects.all()
        context["total_compra"] = total_carro
        context ["cant_prduct"] = usuario_act.carrito()
        context ["cart"] = carro
        return context

    