from django.db import models
import os

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
        if not self.pk:  # Nuevo objeto
            self.foto_prod.name = upload_to(self, self.foto_prod.name)
        else:  # Actualización de un objeto existente
            try:
                calzado_antiguo = Calzado.objects.get(pk=self.pk)
                if (calzado_antiguo.codigo != self.codigo or 
                    calzado_antiguo.tipo_calzado.categoria_nom.categoria != self.tipo_calzado.categoria_nom.categoria):
                    # Borrar la imagen antigua si existe
                    if calzado_antiguo.foto_prod:
                        calzado_antiguo.foto_prod.delete(save=False)
            except Calzado.DoesNotExist:
                pass  # Manejar el caso donde no se encuentra el objeto antiguo
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.activo = False  # Marcamos el objeto como inactivo en lugar de borrarlo
        self.save()
        
    def get_color_display(self):
        return dict(COLOR_CHOICE).get(self.color, "Desconocido")

    def get_material_display(self):
        return dict(MATERIAL_CHOICE).get(self.material, "Desconocido")

    def __str__(self) -> str:
        return (f'{self.codigo}: {self.nombre}')

    

