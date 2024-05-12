from django.contrib import admin

from categoria.models import Categoria, Tipo

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria',)
    search_fields = ('categoria',)

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'get_categoria_name',)
    search_fields = ('tipo',)
    def get_categoria_name(self, obj):
        return obj.categoria.categoria  # Suponiendo que 'categoria' es una ForeignKey a otro modelo con un campo 'nombre'

    get_categoria_name.short_description = 'Categoría'  # Nombre personalizado para la columna

    # Definir el filtro por 'categoria' solo si 'categoria' es un campo en el modelo 'Tipo'
    if 'categoria' in [f.name for f in Tipo._meta.get_fields()]:
        list_filter = ('categoria',) 