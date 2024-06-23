from django.conf import settings
from django.db import models
from calzado.models import Calzado

class Lista_de_Deseos(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    calzado = models.ForeignKey(Calzado, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.calzado.nombre}'
