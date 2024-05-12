from django.contrib import admin

from movimiento.models import Movimiento

# Register your models here.
@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ('usuario','fecha', 'calzado','talle','cantidad','motivo','activo',)
    search_fields = ('usuario','fecha','calzado',)
    list_filter = ('usuario','fecha', 'calzado','talle','motivo','activo',)