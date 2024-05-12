from django.contrib import admin

from categoria.models import Categoria, Tipo

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria',)
    search_fields = ('categoria',)

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'categoria_nom',)
    search_fields = ('tipo',)
    def get_categoria_name(self, obj):
        return obj.categoria.categoria  # Suponiendo que 'categoria' es una ForeignKey a otro modelo con un campo 'nombre'

    get_categoria_name.short_description = 'Categoría'  # Nombre personalizado para la columna

    list_filter = ('categoria_nom__categoria',)