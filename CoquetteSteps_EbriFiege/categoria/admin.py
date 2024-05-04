from django.contrib import admin

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria',)
    search_fields = ('categoria',)

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'categoria',)
    search_fields = ('tipo',)
    list_filter = ('categoria',)