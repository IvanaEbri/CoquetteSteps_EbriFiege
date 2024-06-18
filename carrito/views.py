from django.shortcuts import render
from django.views.generic import TemplateView
from calzado.models import Calzado
from django.shortcuts import redirect
from django.urls import reverse
from categoria.models import Categoria
from usuario.models import Usuario
from carrito.models import Carrito
from usuario.views import ActiveClientLoginRequiredMixin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

class CarritoView(ActiveClientLoginRequiredMixin, TemplateView):
    template_name = "cart.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        total_carro = 0
        usuario_act = self.request.user
        carro = usuario_act.productos_carro()

        #total de compra
        for producto in carro:
            total_carro += producto.calzado.precio

        context["category"] = Categoria.objects.all()
        context["total_compra"] = total_carro
        context["cant_prduct"] = usuario_act.carrito()
        context["cart"] = carro
        return context

@csrf_exempt
def agregar_al_carrito(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        talle = data.get('talle')

        try:
            producto = Calzado.objects.get(id=product_id)
            usuario = request.user
            carrito_item, created = Carrito.objects.get_or_create(
                usuario=usuario,
                calzado=producto,
                talle=talle,
                comprado=False,
                activo=True
            )

            return JsonResponse({'success': True})
        except Calzado.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Producto no encontrado'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Método no permitido'})
