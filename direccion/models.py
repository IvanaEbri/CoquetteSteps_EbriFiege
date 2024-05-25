from django.db import models

PROVINCIA_CHOICE = [
        ('BUE', 'Buenos Aires'),
        ('CAT', 'Catamarca'),
        ('CHA', 'Chaco'),
        ('CHU', 'Chubut'),
        ('CBA', 'Córdoba'),
        ('COR', 'Corrientes'),
        ('ERI', 'Entre Ríos'),
        ('FOR', 'Formosa'),
        ('JUJ', 'Jujuy'),
        ('LP', 'La Pampa'),
        ('LR', 'La Rioja'),
        ('MZA', 'Mendoza'),
        ('MIS', 'Misiones'),
        ('NEU', 'Neuquén'),
        ('RNE', 'Río Negro'),
        ('SL', 'San Luis'),
        ('SC', 'Santa Cruz'),
        ('SF', 'Santa Fe'),
        ('SDE', 'Santiago del Estero'),
        ('TF', 'Tierra del Fuego'),
        ('TUC', 'Tucumán'),
        ('CF', 'Capital Federal'),
    ]
    
# Create your models here.
class Direccion(models.Model):
    usuario_dir = models.ForeignKey('usuario.Usuario',models.CASCADE, null=False, blank=False)
    provincia = models.CharField(max_length=3,choices=PROVINCIA_CHOICE, default=PROVINCIA_CHOICE[0][0], null=False )
    ciudad = models.CharField(max_length=100,null=False, blank=False)
    codigo_postal = models.CharField(max_length=8)
    calle = models.CharField(max_length=100,null=False, blank=False)
    altura = models.IntegerField( null=False, blank=False)
    depto = models.CharField(max_length=3,blank=True, null=True)
    piso = models.CharField(max_length=3,blank=True, null=True)
    observaciones = models.TextField(null=True, blank=True)
    activo = models.BooleanField(null=False, default=True)

    