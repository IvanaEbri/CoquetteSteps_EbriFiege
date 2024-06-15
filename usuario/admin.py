from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario
from django.db import IntegrityError, transaction

class UsuarioAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')  # Campos requeridos para AbstractUser
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

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValidationError as e:
            self.message_user(request, f"Error al guardar: {e}", level='ERROR')
        try:
            with transaction.atomic():
                if 'cliente' in form.changed_data or 'activo' in form.changed_data:
                    if not request.user.has_perm('usuario.change_cliente_activo'):
                        raise PermissionDenied("No tienes permiso para cambiar el estado de 'cliente' y 'activo'.")
                super().save_model(request, obj, form, change)
        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            # Manejar el error según sea necesario

admin.site.register(Usuario, UsuarioAdmin)
