# Generated by Django 5.0.6 on 2024-06-05 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablacliente',
            name='value',
        ),
        migrations.AddField(
            model_name='tablacliente',
            name='correo',
            field=models.CharField(default='default@example.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tablacliente',
            name='rut',
            field=models.CharField(default='default@example.com', max_length=100),
            preserve_default=False,
        ),
    ]