from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    #username y passwor se definen en AbstractUser
    email = models.EmailField(unique=True, null=False,blank=False)
    cliente = models.BooleanField(null=False,default=True)
    activo = models.BooleanField(null=False, default=True)

    def __str__(self) -> str:
        return self.username

    def save(self, *args, **kwargs):
        if self.pk is None:  # El objeto se está creando
            self.cliente = True
            self.activo = True
        super(Usuario, self).save(*args, **kwargs)

    class Meta:
        permissions = [
            ("change_cliente_activo", "Can change cliente and activo status"),
        ]