from django.db import models
from django.utils import timezone

TALLE_CHOICE=[
        (36,36),
        (37,37),
        (38,38),
        (39,39),
        (40,40),
    ]

MOTIVO_CHOICE=[
        (1,'VENTA'),
        (2,'STOCK'),
    ]
    
# Create your models here.
class Movimiento(models.Model):
    usuario = models.ForeignKey('usuario.Usuario',models.CASCADE, null=False, blank=False)
    fecha = models.DateTimeField(auto_now_add=True)
    calzado = models.ForeignKey('calzado.Calzado', models.CASCADE, null=False, blank=False)
    talle = models.IntegerField(null=False,choices=TALLE_CHOICE, default=TALLE_CHOICE[0][0])
    cantidad = models.IntegerField(null=False,blank=False, default=0)
    motivo = models.IntegerField(null=False,choices=MOTIVO_CHOICE,default=MOTIVO_CHOICE[0][0])
    activo = models.BooleanField(null=False, default=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Si es un nuevo registro
            # Establecer la fecha de creación solo si es una nueva instancia
            self.fecha_creacion = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return (f'{self.id}, {self.usuario.user}, {self.calzado.codigo}')

    def get_motivo(self):
        return dict(MOTIVO_CHOICE).get(self.motivo, "Desconocido")