# Generated by Django 5.0.4 on 2024-06-17 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_alter_usuario_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
