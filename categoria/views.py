from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Categoria, Tipo
from calzado.models import Calzado
from .forms import CategoriaForm, TipoForm, DeleteForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class CategoriasView (TemplateView):
    template_name = 'cat_admin.html'

    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Categoria.objects.all()
        context['type'] = Tipo.objects.all()
        return context

class CrearCategoriaView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'cat_ne_admin.html'
    success_url = reverse_lazy('categorias_admin') 

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

class EditarCategoriaView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'cat_ne_admin.html'
    success_url = reverse_lazy('categorias_admin')

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

class EliminarCategoriaView(DeleteView):
    model = Categoria
    form_class = DeleteForm
    template_name = 'cat_del_admin.html'
    success_url = reverse_lazy('categorias_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = DeleteForm(request.POST)
        if form.is_valid():
            confirm_delete = form.cleaned_data.get('confirm_delete')
            if confirm_delete:
                if Tipo.objects.filter(categoria_nom=self.object).exists():
                    messages.error(request,'No puedes eliminar esta categoria porque contiene Tipos.')
                else:
                    return super().post(request, *args, **kwargs)
            else:
                messages.error(request, 'Debes confirmar la eliminación.')
        else:
            # Agregar errores del formulario a los mensajes
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = DeleteForm()
        return context


class CrearTipoView(CreateView):
    model = Tipo
    form_class = TipoForm
    template_name = 'cat_ne_admin.html'
    success_url = reverse_lazy('categorias_admin') 

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

class EditarTipoView(UpdateView):
    model = Tipo
    form_class = TipoForm
    template_name = 'cat_ne_admin.html'
    success_url = reverse_lazy('categorias_admin')

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

class EliminarTipoView(DeleteView):
    model = Tipo
    form_class = DeleteForm
    template_name = 'type_del_admin.html'
    success_url = reverse_lazy('categorias_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = DeleteForm(request.POST)
        if form.is_valid():
            confirm_delete = form.cleaned_data.get('confirm_delete')
            if confirm_delete:
                if Calzado.objects.filter(tipo_calzado=self.object).exists():
                    messages.error(request,'No puedes eliminar este tipo porque contiene Calzados.')
                else:
                    return super().post(request, *args, **kwargs)
            else:
                messages.error(request, 'Debes confirmar la eliminación.')
        else:
            # Agregar errores del formulario a los mensajes
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = DeleteForm()
        return context