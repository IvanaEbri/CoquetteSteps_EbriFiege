from django.db import models
from django.utils import timezone
import uuid

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
    cod_seguimiento =models.CharField(max_length=6, null=False, blank=False, unique=True, default=uuid.uuid4().hex[:6].upper())
    movimientos =models.ManyToManyField ('movimiento.Movimiento', blank=False)
    monto_total = models.DecimalField(decimal_places=2,max_digits=10,null=False,blank=False)
    metodo_envio= models.IntegerField(null=False,choices=ENVIO_CHOICE,default=ENVIO_CHOICE[0][0])
    direccion= models.ForeignKey('direccion.Direccion',models.CASCADE,null=True,blank=True)
    estado = models.IntegerField(null=False, blank=False,choices=ESTADO_CHOICE,default=ESTADO_CHOICE[0][0])
    fecha_creacion= models.DateTimeField(auto_now_add=True)
    fecha_pago= models.DateTimeField(null=True,blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Si es un nuevo registro
            # Establecer la fecha de creación solo si es una nueva instancia
            self.fecha_creacion = timezone.now()

        

        if self.pk is not None: 
            # Si la instancia ya existe en la base de datos
            # Obtener la instancia existente desde la base de datos
            existing_instance = Transaccion.objects.get(pk=self.pk)
            # Comparar los movimientos actuales con los movimientos existentes en la base de datos
            if existing_instance.movimientos.all() != self.movimientos.all():
                # Si los movimientos han cambiado, lanzar una excepción
                raise ValueError("No se permiten modificaciones en los movimientos después de la creación.")
        super().save(*args, **kwargs)
        venta_movimientos = self.movimientos.filter(motivo='venta')
        if len(venta_movimientos) != len(self.movimientos.all()):
            raise ValueError("Solo se pueden asignar movimientos de tipo 'venta' a esta transacción.")

        super().save(*args, **kwargs)