from django.contrib import admin

# Register your models here.
@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cod_seguimiento','movimientos','monto_total','metodo_envio','direccion','estado','fecha_creacion','fecha_pago','fecha_actualizacion',)
    search_fields = ('usuario', 'cod_seguimiento','movimientos','estado','fecha_creacion','fecha_pago','fecha_actualizacion',)
    list_filter = ('usuario','metodo_envio','estado','fecha_creacion','fecha_pago',)