# Generated by Django 5.0.6 on 2024-06-07 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_tablafruta_especie_fruta_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablavariedad',
            old_name='especie',
            new_name='especie_variedad',
        ),
    ]