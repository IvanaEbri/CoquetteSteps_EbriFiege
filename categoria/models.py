from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(unique=True, max_length=30,null=False)

    def __str__(self) -> str:
        return self.categoria


class Tipo(models.Model):
    categoria_nom = models.ForeignKey("categoria.Categoria", on_delete=models.CASCADE, null=False, blank= False )
    tipo= models.CharField(unique=True, max_length=30, null=False, blank=False)

    def __str__(self) -> str:
        return self.tipo
    
    class Meta:
        unique_together = ('categoria_nom', 'tipo')

# @receiver(pre_delete, sender=Categoria)
# def prevent_category_deletion(sender, instance, **kwargs):
#     if Tipo.objects.filter(categoria_nom=instance).exists():
#         raise ValidationError("No se puede eliminar esta categoría porque tiene tipos asociados.")