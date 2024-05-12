from django.contrib import admin

from transaccion.models import Transaccion
# Register your models here.
@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('get_usuario_user', 'cod_seguimiento','display_movimientos','monto_total','metodo_envio','direccion','estado','fecha_creacion','fecha_pago','fecha_actualizacion',)
    search_fields = ('get_usuario_user', 'cod_seguimiento','display_movimientos','estado','fecha_creacion','fecha_pago','fecha_actualizacion',)
    #list_filter = ('usuario','metodo_envio','estado','fecha_creacion','fecha_pago',)

    def display_movimientos(self, obj):
        return ', '.join([movimiento.__str__() for movimiento in obj.movimientos.all()])

    display_movimientos.short_description = 'Movimientos'

    def get_usuario_user(self, obj):
        return obj.usuario.user  # Suponiendo que 'categoria' es una ForeignKey a otro modelo con un campo 'nombre'

    get_usuario_user.short_description = 'Usuario'  # Nombre personalizado para la columna

    # Definir el filtro por 'categoria' solo si 'categoria' es un campo en el modelo 'Tipo'
    if 'usuario' in [f.name for f in Transaccion._meta.get_fields()]:
        list_filter = ('usuario','metodo_envio','estado','fecha_creacion','fecha_pago',) 