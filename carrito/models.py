from django.db import models
from django.db import transaction


class Carrito(models.Model):
    usuario = models.ForeignKey('usuario.Usuario',models.CASCADE, null=False, blank=False)
    calzado = models.ForeignKey('calzado.Calzado',models.CASCADE, null=False, blank=False)
    talle = models.IntegerField(null=False, blank=False)
    comprado = models.BooleanField(default=False, null=False, blank=False)
    activo = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return (f'{self.usuario.username}: {self.calzado.codigo} talle: {self.talle}')

    def compra_calzado (self):
        from movimiento.models import Movimiento

        if activo==True and comprado==False:
            try:
                with transaction.atomic():
                    #creo un registro en movimiento con los datos del producto en el carro
                    nuevo_registro = Movimiento.objects.create(
                        usuario = self.usuario,
                        calzado = self.calzado,
                        talle = self.talle,
                        cantidad = 1,
                        motivo = 1,
                        activo = True
                    )
                    self.comprado=True
                return True    
                #messages.success(request,f"Su compra del {self.calzado.nombre} en talle {self.talle} ha sido exitosa")
            except Exception as e:
                return False
                #messages.error(request, f"Hubo un error al procesar su compra, favor intente nuevamente")
        else:
            return False
            #messages.error(request, f"No se puede realizar la compra de un carrito invalido")


    def eliminacion_carro (self):
        self.activo= False