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

class CarritoView(TemplateView):
    template_name = "cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario_act = self.request.user
        carro = usuario_act.productos_carro()

        total_carro = sum(item.calzado.precio for item in carro)

        context["category"] = Categoria.objects.all()
        context["total_compra"] = total_carro
        context["cant_prduct"] = carro.count()  # Cantidad de productos en el carrito
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
            
            # Calcular el total y la cantidad de productos en el carrito
            carro = usuario.productos_carro()
            total_carro = sum(item.calzado.precio for item in carro)
            cantidad_productos = carro.count()

            return JsonResponse({
                'success': True,
                'cant_prduct': cantidad_productos,
                'total_compra': total_carro
            })
        except Calzado.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Producto no encontrado'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Método no permitido'})

@csrf_exempt
def eliminar_del_carrito(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item_id = data['item_id']
            usuario = request.user
            carrito_item = Carrito.objects.get(id=item_id, usuario=usuario, activo=True)
            carrito_item.delete()

            # Calcular el total y la cantidad de productos en el carrito
            carro = usuario.productos_carro()
            total_carro = sum(item.calzado.precio for item in carro)
            cantidad_productos = carro.count()

            return JsonResponse({
                'success': True,
                'cant_prduct': cantidad_productos,
                'total_compra': total_carro
            })
        except Carrito.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Producto no encontrado en el carrito'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})
