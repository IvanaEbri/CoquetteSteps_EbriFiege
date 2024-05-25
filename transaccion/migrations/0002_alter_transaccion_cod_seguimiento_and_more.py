# Generated by Django 5.0.6 on 2024-05-25 01:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0002_alter_direccion_depto_alter_direccion_observaciones_and_more'),
        ('transaccion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='cod_seguimiento',
            field=models.CharField(default='179F33', max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='direccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='direccion.direccion'),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='fecha_pago',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
