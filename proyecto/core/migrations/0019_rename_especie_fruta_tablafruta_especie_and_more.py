# Generated by Django 5.0.6 on 2024-06-07 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_rename_especie_tablavariedad_especie_variedad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablafruta',
            old_name='especie_fruta',
            new_name='especie',
        ),
        migrations.RenameField(
            model_name='tablafruta',
            old_name='variedad_fruta',
            new_name='variedad',
        ),
        migrations.RenameField(
            model_name='tablavariedad',
            old_name='especie_variedad',
            new_name='especie',
        ),
    ]
