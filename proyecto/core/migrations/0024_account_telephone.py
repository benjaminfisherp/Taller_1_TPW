# Generated by Django 5.0.6 on 2024-06-11 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='telephone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono'),
        ),
    ]