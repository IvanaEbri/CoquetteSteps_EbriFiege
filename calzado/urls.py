from django.urls import path
from . import views

urlpatterns = [
    #path('', views.Home.as_view(), name='home'),
    path('admin/', views.ProductosView.as_view(), name='productos_admin'),
    path('Category/<str:category_filter>/', views.Home_filter.as_view(), name='home_filter'),
    path('Product/<str:product_code>/', views.Product.as_view(), name='producto'),
    path('admin/Shoes/new/', views.CrearCalzadoView.as_view(), name='crear_producto'),
    path('admin/Shoes/edit/<int:pk>/', views.EditarCalzadoView.as_view(), name='editar_producto'),
    path('admin/Shoes/delete/<int:pk>/', views.EliminarCalzadoView.as_view(), name='eliminar_producto'),

]
