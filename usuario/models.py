from django.db import models

# Create your models here.
class Usuario(models.Model):
    user = models.CharField(null=False, unique=True, blank=False, max_length=15)
    password = models.CharField(null=False,blank=False, max_length=15)
    email = models.EmailField(unique=True, null=False,blank=False)
    cliente = models.BooleanField(null=False,default=True)
    activo = models.BooleanField(null=False, default=True)

    def __str__(self) -> str:
        return self.user