# Generated by Django 3.2.6 on 2021-09-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0008_empresa_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='descripcion',
            field=models.TextField(max_length=120, verbose_name='Descripcion'),
        ),
    ]