from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.CategoriasView.as_view(), name='categorias_admin'),
    path('admin/Category/new/', views.CrearCategoriaView.as_view(), name='crear_categoria'),
    path('admin/Category/edit/<int:pk>/', views.EditarCategoriaView.as_view(), name='editar_categoria'),
    path('admin/Category/delete/<int:pk>/', views.EliminarCategoriaView.as_view(), name='eliminar_categoria'),
    path('admin/Type/new/', views.CrearTipoView.as_view(), name='crear_tipo'),
    path('admin/Type/edit/<int:pk>/', views.EditarTipoView.as_view(), name='editar_tipo'),
    path('admin/Type/delete/<int:pk>/', views.EliminarTipoView.as_view(), name='eliminar_tipo'),
]
