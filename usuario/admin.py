from django.contrib import admin

from usuario.models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuaurioAdmin(admin.ModelAdmin):
    list_display = ('user', 'password','email','cliente','activo',)
    search_fields = ('user','email',)
    list_filter = ('activo',)