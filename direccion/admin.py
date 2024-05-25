from django.contrib import admin

from direccion.models import Direccion

# Register your models here.
@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('usuario_dir', 'provincia','ciudad','codigo_postal','calle','altura','depto','piso','observaciones','activo',)
    search_fields = ('usuario_dir','provincia','ciudad',)
    list_filter = ('provincia','ciudad','activo',)