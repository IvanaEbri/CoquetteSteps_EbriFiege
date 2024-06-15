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