# Generated by Django 5.0.6 on 2024-06-07 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_tablafruta_especie_alter_tablafruta_variedad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablafruta',
            old_name='variedad',
            new_name='variedad_fruta',
        ),
        migrations.RemoveField(
            model_name='tablafruta',
            name='especie',
        ),
        migrations.AddField(
            model_name='tablafruta',
            name='especie_fruta',
            field=models.ForeignKey(default='especie_fruta', on_delete=django.db.models.deletion.CASCADE, related_name='frutas_especie', to='core.tablaespecie'),
            preserve_default=False,
        ),
    ]
