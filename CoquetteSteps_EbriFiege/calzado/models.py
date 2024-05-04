from django.db import models


# Create your models here.
class Calzado(models.Model):
    codigo = models.CharField(max_length=10, null=False, unique=True, blank=False)
    nombre = models.CharField(max_length=50, null=False, unique=True, blank=False)
    tipo_calzado= models.ForeignKey('categoria.Tipo', on_delete=models.CASCADE, null=False, blank=False)
    foto_prod = models.ImageField(upload_to='calzado/',null=True)
    descripcion = models.TextField(null=False, blank=False)
    color= models.IntegerField(choices=COLOR_CHOICES, default=COLOR_CHOICES[0][0])
    material = models.IntegerField(choices=MATERIAL_CHOICES, default=MATERIAL_CHOICES[0][0])
    precio = models.DecimalField(decimal_places=2,null=False,blank=False, default=0.00)
    activo=models.BooleanField(null=False, default=True)

    def __str__(self) -> str:
        return self.nombre, self.precio

    COLOR_CHOICES=[
        (1,"Blanco"),
        (2,"Negro"),
        (3,"Marron")
        (4,"Beige"),
        (5,"Rojo"),
        (6,"Azul"),
        (7,"Amarillo"),
        (8,"Naranja"),
        (9,"Verde"),
        (10,"Violeta"),
        (11,"Gris"),
        (12,"Rosa"),
        (13,"Celeste")
        (14,"Crema"),
        (15,"Nude"),
        (16,"Plateado"),
        (17,"Dorado"),
        (18,"Multicolor"),
    ]

    MATERIAL_CHOICES=[
        (1,"Gamuza"),
        (2,"Cuero"),
        (3,"Cuero sintetico"),
        (4,"Charol"),
        (5,"Ecocuero"),
        (6,"Lona"),
        (7,"Algodon"),
        (8,"Corderito"),
        (9,"Engomado"),
        (10,"Gabardina"),
        (11,"PVC"),
    ]