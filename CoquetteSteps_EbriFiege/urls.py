"""
URL configuration for CoquetteSteps_EbriFiege project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from calzado.views import Home
from usuario.views import HomeAdminView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',home,name='home'),
    path('Home/admin/', HomeAdminView.as_view(), name='home_admin'),
    path('Shoes/', include('calzado.urls')),
    path('User/', include('usuario.urls')),
    path('Cart/', include('carrito.urls')),
    path('Category/', include('categoria.urls')),
    path('', Home.as_view(), name='home'), #AL FINAL
]

