from django.shortcuts import render
from categoria.models import Categoria
from calzado.models import Calzado
from django.shortcuts import redirect
import random

def home(request):
    category = Categoria.objects.all()
    shoes= list(Calzado.objects.all())
    star_product= random.sample(shoes, min(len(shoes), 5))
    return render(request,'home_content.html',{"category":category,"star_product":star_product})


def home_filter(request, category_filter):
    category = Categoria.objects.all()
    
    if category_filter!='all':
        product = Calzado.objects.filter(tipo_calzado__categoria_nom__categoria=category_filter)  
    else:
        product= Calzado.objects.all()
        category_filter= "Calzado"
    return render(request, 'product.html',{"category":category,"category_filter":category_filter,"product":product})
