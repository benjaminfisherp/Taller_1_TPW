# Generated by Django 5.0.6 on 2024-06-07 15:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_tablaespecie_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablafruta',
            name='variedad',
            field=models.ForeignKey(default='variedad', on_delete=django.db.models.deletion.CASCADE, to='core.tablavariedad'),
            preserve_default=False,
        ),
    ]
