from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=30,null=False)

    def __str__(self) -> str:
        return self.categoria


class Tipo(models.Model):
    categoria_nom = models.ForeignKey("categoria.Categoria", on_delete=models.CASCADE, null=False, blank= False )
    tipo= models.CharField(max_length=30, null=False, blank=False)

    def __str__(self) -> str:
        return self.tipo