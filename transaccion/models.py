from django.db import models

ENVIO_CHOICE=[
    (1,'Retiro en local'),
    (2,'Envio a sucursal'),
    (3,'Envio a domicilio'),
]

ESTADO_CHOICE=[
    (1,'Reservado'),
    (2,'Pagado'),
    (3,'Rechazado'),
    (4,'Cancelado'),
    (5,'En preparacion'),
    (6,'Despachado'),
    (7,'Entregado'),
]

# Create your models here.
class Transaccion(models.Model):
    usuario = models.ForeignKey('usuario.Usuario',models.CASCADE, null=False,blank=False)
    cod_seguimiento =models.CharField(max_length=6, null=False, blank=False, unique=True)
    movimientos =models.ManyToManyField ('movimiento.Movimiento', blank=False)
    monto_total = models.DecimalField(decimal_places=2,max_digits=10,null=False,blank=False)
    metodo_envio= models.IntegerField(null=False,choices=ENVIO_CHOICE,default=ENVIO_CHOICE[0][0])
    direccion= models.ForeignKey('direccion.Direccion',models.CASCADE,null=True)
    estado = models.IntegerField(null=False, blank=False,choices=ESTADO_CHOICE,default=ESTADO_CHOICE[0][0])
    fecha_creacion= models.DateTimeField(null=False,blank=False)
    fecha_pago= models.DateTimeField(null=True)
    fecha_actualizacion = models.DateTimeField(null=False,blank=False)

