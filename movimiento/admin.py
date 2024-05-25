from django.contrib import admin

from movimiento.models import Movimiento

# Register your models here.
@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ('usuario','fecha', 'calzado','talle','cantidad','motivo','activo',)
    search_fields = ('usuario','fecha','calzado__nombre','calzado__codigo',)
    list_filter = ('usuario__user','fecha', 'calzado__nombre','talle','calzado__tipo_calzado__categoria_nom','calzado__tipo_calzado__tipo','motivo','activo',)