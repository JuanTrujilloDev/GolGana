# Generated by Django 3.2.6 on 2021-09-24 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0027_reserva_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancha',
            name='nombre',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Nombre'),
        ),
    ]
