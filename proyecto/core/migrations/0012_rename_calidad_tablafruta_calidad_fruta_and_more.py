# Generated by Django 5.0.6 on 2024-06-07 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_tablavariedad_especie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablafruta',
            old_name='calidad',
            new_name='calidad_fruta',
        ),
        migrations.RenameField(
            model_name='tablafruta',
            old_name='codigo',
            new_name='codigo_fruta',
        ),
        migrations.RenameField(
            model_name='tablafruta',
            old_name='especie',
            new_name='especie_fruta',
        ),
        migrations.RenameField(
            model_name='tablafruta',
            old_name='variedad',
            new_name='variedad_fruta',
        ),
    ]