# Generated by Django 5.0.6 on 2024-05-25 01:57

import calzado.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calzado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calzado',
            name='foto_prod',
            field=models.ImageField(null=True, upload_to=calzado.models.upload_to),
        ),
    ]
