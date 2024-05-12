from django.contrib import admin

from calzado.models import Calzado

# Register your models here.
@admin.register(Calzado)
class CalzadoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre','tipo_calzado','foto_prod','descripcion','color','material','precio','activo',)
    search_fields = ('codigo','tipo_calzado__tipo','color','material','precio',)
    list_filter = ('tipo_calzado__categoria_nom','tipo_calzado__tipo','color','material','precio','activo',)