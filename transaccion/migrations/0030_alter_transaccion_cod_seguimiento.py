# Generated by Django 5.0.4 on 2024-06-22 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaccion', '0029_alter_transaccion_cod_seguimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='cod_seguimiento',
            field=models.CharField(default='1CB33B', max_length=6, unique=True),
        ),
    ]
