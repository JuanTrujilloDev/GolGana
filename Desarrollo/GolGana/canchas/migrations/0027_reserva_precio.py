# Generated by Django 3.2.6 on 2021-09-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0026_rename_estado_reserva_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='precio',
            field=models.FloatField(default='0', verbose_name='Precio'),
        ),
    ]