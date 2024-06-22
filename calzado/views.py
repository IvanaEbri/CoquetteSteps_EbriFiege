from django.shortcuts import render, redirect
from categoria.models import Categoria, Tipo
from calzado.models import Calzado, COLOR_CHOICE, MATERIAL_CHOICE
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from usuario.models import Usuario
import random
from django.views.decorators.http import require_POST
import json
from .forms import CalzadoForm, DeleteForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from usuario.views import NonClientActiveUserRequiredMixin

class Home (TemplateView):
    template_name = "home_content.html"
    
    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Categoria.objects.all()
        shoes= list(Calzado.objects.all())
        context["star_product"]= random.sample(shoes, min(len(shoes), 5))
        usuario_act = self.request.user
        if usuario_act.is_authenticated:
            context ["cant_prduct"] = usuario_act.carrito_count()
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
        usuario_act = self.request.user
        if usuario_act.is_authenticated:
            context ["cant_prduct"] = usuario_act.carrito_count()
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
        usuario_act = self.request.user
        if usuario_act.is_authenticated:
            context ["cant_prduct"] = usuario_act.carrito_count()

        return context

    @require_POST
    def agregar_al_carro(request):
        data = json.loads(request.body)
        talle = data.get('talle')

        if self.request.user.is_authenticated:
            try:
                with transaction.atomic():
                #creo un registro en carro
                    nuevo_registro = Carrito.objects.create(
                            usuario = self.request.user,
                            calzado = self.request.producto,
                            talle = talle,
                            comprado = False,
                            activo = True
                        )
            except Exception as e:
                messages.error(request, f"Hubo un error al añadir al carrito, favor intente nuevamente")
        else:
            return redirect("login")

class ProductosView (NonClientActiveUserRequiredMixin,TemplateView):
    template_name = 'prod_admin.html'

    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoes'] = Calzado.objects.filter(activo=True)
        return context

class CrearCalzadoView(NonClientActiveUserRequiredMixin, CreateView):
    model = Calzado
    form_class = CalzadoForm
    template_name = 'prod_ne_admin.html'
    success_url = reverse_lazy('productos_admin') 

    def form_valid(self, form):
        # Procesar el formulario si es válido
        user = form.save(commit=False)
        # Podemos hacer algo
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # Agregar mensajes de error a la lista de mensajes
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{error}")
        return super().form_invalid(form)

class EditarCalzadoView(NonClientActiveUserRequiredMixin, UpdateView):
    model = Calzado
    form_class = CalzadoForm
    template_name = 'prod_ne_admin.html'
    success_url = reverse_lazy('productos_admin')

    def form_valid(self, form):
        # Procesar el formulario si es válido
        user = form.save(commit=False)
        # Podemos hacer algo
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # Agregar mensajes de error a la lista de mensajes
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{error}")
        return super().form_invalid(form)

class EliminarCalzadoView(NonClientActiveUserRequiredMixin,DeleteView):
    model = Calzado
    form_class = DeleteForm
    template_name = 'prod_del_admin.html'
    success_url = reverse_lazy('productos_admin')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.activo = False  # Cambiamos el atributo activo a False
        self.object.save()
        messages.success(request, 'El calzado se ha eliminado correctamente de forma lógica.')
        return super().delete(request, *args, **kwargs)