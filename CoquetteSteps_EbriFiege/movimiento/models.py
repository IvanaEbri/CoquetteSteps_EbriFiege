from django.db import models

# Create your models here.
class Movimiento(models.Model):
    usuario = models.ForeignKey('usuario.Usuario',models.CASCADE, null=False, blank=False)
    fecha = models.DateTimeField(null=False, blank=False)
    calzado = models.ForeignKey('calzado.Calzado', models.CASCADE, null=False, blank=False)
    talle = models.IntegerField(max_length=2,null=False,choices=TALLE_CHOICE, default=TALLE_CHOICE[0][0])
    cantidad = models.IntegerField(max_length=3,null=False,blank=False, default=0)
    motivo = models.IntegerField(max_length=1,null=False,choices=MOTIVO_CHOICE,default=MOTIVO_CHOICE[0][0])
    activo = models.BooleanField(null=False, default=True)

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