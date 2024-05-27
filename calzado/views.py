from django.shortcuts import render
from categoria.models import Categoria
from calzado.models import Calzado
from django.shortcuts import redirect

def home(request):
    #category = Categoria.objects.all()
    #return render(request, 'home.html',{"category":category})
    return redirect('home_filter',category_filter='all')


def home_filter(request, category_filter):
    category = Categoria.objects.all()
    
    if category_filter!='all':
        product = Calzado.objects.filter(tipo_calzado__categoria_nom__categoria=category_filter)  
    else:
        product= Calzado.objects.all()
        category_filter= "Calzado"
    return render(request, 'product.html',{"category":category,"category_filter":category_filter,"product":product})
