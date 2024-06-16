from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario
from django.db import IntegrityError, transaction

class UsuarioAdmin(BaseUserAdmin):
    model = Usuario
    list_display = ('username', 'email', 'cliente', 'activo')
    list_filter = ('cliente', 'activo', 'is_staff')

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Información personal', {
            'fields': ('first_name', 'last_name', 'email', 'cliente', 'activo')
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Fechas importantes', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Deshabilitar el campo cliente si el usuario es cliente y no es superusuario
        if obj and obj.cliente and not request.user.is_superuser:
            form.base_fields['cliente'].disabled = True
        return form

    def save_model(self, request, obj, form, change):
        # Verificar si se intenta cambiar el campo cliente
        if 'cliente' in form.changed_data:
            # Si es cliente y no es superusuario, no permitir el cambio
            if obj.cliente and not request.user.is_superuser:
                raise PermissionDenied("No se puede cambiar el estado de 'cliente' si el usuario es cliente.")
            # Si no tiene permiso, no permitir el cambio
            if not request.user.has_perm('usuario.change_cliente_activo') and not request.user.is_superuser:
                raise PermissionDenied("No tienes permiso para cambiar el estado de 'cliente'.")
        if 'activo' in form.changed_data and not request.user.has_perm('usuario.change_cliente_activo'):
            raise PermissionDenied("No tienes permiso para cambiar el estado de 'activo'.")
        try:
            with transaction.atomic():
                super().save_model(request, obj, form, change)
        except IntegrityError as e:
            self.message_user(request, f"Error al guardar: {e}", level='ERROR')

admin.site.register(Usuario, UsuarioAdmin)
