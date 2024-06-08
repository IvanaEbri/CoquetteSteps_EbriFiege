from django.shortcuts import render
from categoria.models import Categoria
from calzado.models import Calzado
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView
import random

class Home (TemplateView):
    template_name = "home_content.html"
    
    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Categoria.objects.all()
        shoes= list(Calzado.objects.all())
        context["star_product"]= random.sample(shoes, min(len(shoes), 5))
        print(context)
        return context

# def home(request):
#     category = Categoria.objects.all()
#     shoes= list(Calzado.objects.all())
#     star_product= random.sample(shoes, min(len(shoes), 5))
#     return render(request,'home_content.html',{"category":category,"star_product":star_product})


class Home_filter (TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = kwargs.get('category_filter')
        
        context['category'] = Categoria.objects.all()

        if cat!='all':
            context['product'] = Calzado.objects.filter(tipo_calzado__categoria_nom__categoria=cat)  
        else:
            context['product']= Calzado.objects.all()
            context['category_filter']= "Calzado"

        return context


# def home_filter(request, category_filter):
#     category = Categoria.objects.all()
    
#     #kwargs.get('category_filter')

#     if category_filter!='all':
#         product = Calzado.objects.filter(tipo_calzado__categoria_nom__categoria=category_filter)  
#     else:
#         product= Calzado.objects.all()
#         category_filter= "Calzado"
#     return render(request, 'product.html',{"category":category,"category_filter":category_filter,"product":product})

class Product(TemplateView):
    template_name='product_one.html'

    def dispatch(self, request, *args, **kwargs):
        cod = kwargs.get('product_code')
        producto = Calzado.objects.filter(codigo=cod).first()

        if producto is None or not producto.nombre:
            return redirect("home")
        
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cod = kwargs.get('product_code')
        producto = Calzado.objects.filter(codigo=cod).first()

        context['category'] = Categoria.objects.all()
        context['product'] = producto
        context['product_color'] = producto.get_color_display() 
        context['product_material'] = producto.get_material_display() 
        context['size']= [35,36,37,38,39,40]

        return context