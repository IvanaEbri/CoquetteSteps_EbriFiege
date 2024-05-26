from django.db import models

COLOR_CHOICE=[
        (1,"Blanco"),
        (2,"Negro"),
        (3,"Marron"),
        (4,"Beige"),
        (5,"Rojo"),
        (6,"Azul"),
        (7,"Amarillo"),
        (8,"Naranja"),
        (9,"Verde"),
        (10,"Violeta"),
        (11,"Gris"),
        (12,"Rosa"),
        (13,"Celeste"),
        (14,"Crema"),
        (15,"Nude"),
        (16,"Plateado"),
        (17,"Dorado"),
        (18,"Multicolor"),
        (19,"Tostado"),
        (20,"Bordó"),
    ]

MATERIAL_CHOICE=[
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
def upload_to(instance, filename):
    # Obtener la información necesaria de la instancia de Calzado
    categoria = instance.tipo_calzado.categoria_nom.categoria
    tipo = instance.tipo_calzado.tipo
    codigo = instance.codigo

    # Definir la ruta de almacenamiento para la imagen
    return f'calzado/{categoria}/{tipo}/{codigo}/{filename}'

# Create your models here.
class Calzado(models.Model):
    codigo = models.CharField(max_length=10, null=False, unique=True, blank=False)
    nombre = models.CharField(max_length=50, null=False, unique=True, blank=False)
    tipo_calzado= models.ForeignKey('categoria.Tipo', on_delete=models.CASCADE, null=False, blank=False)
    foto_prod = models.ImageField(upload_to=upload_to,null=True)
    descripcion = models.TextField(null=False, blank=False)
    color= models.IntegerField(choices=COLOR_CHOICE, default=COLOR_CHOICE[0][0])
    material = models.IntegerField(choices=MATERIAL_CHOICE, default=MATERIAL_CHOICE[0][0])
    precio = models.DecimalField(decimal_places=2,max_digits=12,null=False,blank=False, default=0.00)
    activo=models.BooleanField(null=False, default=True)

    def save(self, *args, **kwargs):
        # Antes de guardar el código se convierte en el nombre del archivo si es nuevo
        if not self.pk:  # Si es un nuevo registro
            self.foto_prod.name = f'{self.codigo}.jpg'  # Asignar el nombre del archivo basado en el código
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return (f'{self.codigo}: {self.nombre}')

    

