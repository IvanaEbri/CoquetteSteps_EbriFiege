# Generated by Django 5.0.4 on 2024-06-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaccion', '0028_alter_transaccion_cod_seguimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='cod_seguimiento',
            field=models.CharField(default='4F607E', max_length=6, unique=True),
        ),
    ]