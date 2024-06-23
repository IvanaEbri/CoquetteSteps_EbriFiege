from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages
from .models import Lista_de_Deseos
from calzado.models import Calzado
from categoria.models import Categoria
from django.contrib.auth.decorators import login_required
import json

class ListaDeseosView(TemplateView):
    template_name = "wishlist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        deseos = Lista_de_Deseos.objects.filter(usuario=usuario, activo=True)

        context["category"] = Categoria.objects.all()
        context["cant_deseos"] = deseos.count()
        context["wishlist"] = deseos
        return context

@csrf_exempt
@login_required
def agregar_a_deseos(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')

        try:
            producto = Calzado.objects.get(id=product_id)
            usuario = request.user
            wishlist_item, created = Lista_de_Deseos.objects.get_or_create(
                usuario=usuario,
                calzado=producto,
                activo=True
            )

            if created:
                messages.success(request, 'Producto agregado a tu lista de deseos.')
            else:
                messages.info(request, 'Este producto ya está en tu lista de deseos.')

            deseos = Lista_de_Deseos.objects.filter(usuario=usuario, activo=True)
            cantidad_deseos = deseos.count()

            return JsonResponse({
                'success': True,
                'cant_deseos': cantidad_deseos
            })
        except Calzado.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Producto no encontrado'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Método no permitido'})

@csrf_exempt
@login_required
def eliminar_de_deseos(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item_id = data['item_id']
            usuario = request.user
            wishlist_item = Lista_de_Deseos.objects.get(id=item_id, usuario=usuario, activo=True)
            wishlist_item.activo = False
            wishlist_item.save()

            deseos = Lista_de_Deseos.objects.filter(usuario=usuario, activo=True)
            cantidad_deseos = deseos.count()

            return JsonResponse({
                'success': True,
                'cant_deseos': cantidad_deseos
            })
        except Lista_de_Deseos.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Producto no encontrado en la lista de deseos'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})
