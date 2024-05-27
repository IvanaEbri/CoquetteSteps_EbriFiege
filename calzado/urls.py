from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:category_filter>/', views.home_filter, name='home_filter'),
]
