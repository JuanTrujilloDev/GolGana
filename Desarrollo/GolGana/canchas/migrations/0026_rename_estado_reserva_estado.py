# Generated by Django 3.2.6 on 2021-09-22 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0025_reserva_empresa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='Estado',
            new_name='estado',
        ),
    ]