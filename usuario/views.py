from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from categoria.models import Categoria
from usuario.models import Usuario


from usuario.forms import RegistrationForm


class CustomLoginView(LoginView):
    template_name = "login.html"

    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Categoria.objects.all()
        #print (context["category"])
        return context

    def form_invalid(self, form):
        """No es obligatorio sobreescribir este método, pero es útil para agregar mensajes de error personalizados."""
        messages.error(
            self.request, "Los datos ingresados son incorrectos. Por favor, inténtalo de nuevo."
        )  # Mensaje de error
        return super().form_invalid(form)

class CustomLogoutView(LogoutView):

    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Categoria.objects.all()
        usuario_act = self.request.user
        if usuario_act.is_authenticated:
            context ["cant_prduct"] = usuario_act.carrito
        return context

class ActiveClientLoginRequiredMixin(LoginRequiredMixin):
    #verifica si el usuario no esta autentificado o activo y lo lleva al login
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.activo:
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)

class NonClientActiveUserRequiredMixin(LoginRequiredMixin):

    #verifica si el usuario no esta autenticado, es un cliente (condicion True) o esta inactivo (cond False) lo deriva al home
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.cliente or not request.user.activo:
            return redirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)


class LogoutConfirmationView(LoginRequiredMixin, View):
    template_name = "logout.html"

    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Categoria.objects.all()
        usuario_act = self.request.user
        if usuario_act.is_authenticated:
            context ["cant_prduct"] = usuario_act.carrito
        return context

    def get(self, request, *args, **kwargs):
        """No es obligatorio sobreescribir este método, pero es útil para agregar mensajes de error personalizados."""
        return render(request, self.template_name)




class RegistrationView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    template_name = "register.html"

    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Categoria.objects.all()
        return context

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
                messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)