from django.urls import path
from . import views

urlpatterns = [
    #path('', views.Home.as_view(), name='home'),
    path('Category/<str:category_filter>/', views.Home_filter.as_view(), name='home_filter'),
]
