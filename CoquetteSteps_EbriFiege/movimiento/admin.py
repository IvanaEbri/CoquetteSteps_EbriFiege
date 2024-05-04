from django.contrib import admin

# Register your models here.
@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ('usuario','feha', 'calzado','talle','cantidad','motivo','activo',)
    search_fields = ('usuario','fecha','calzado',)
    list_filter = ('usuario','fecha', 'calzado','talle','motivo','activo',)