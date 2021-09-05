# Generated by Django 3.2.6 on 2021-09-02 22:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_perfilcliente_documento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.AlterField(
            model_name='perfilcliente',
            name='documento',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(regex='^[0-9]{13}$')], verbose_name='Numero de documento'),
        ),
        migrations.AlterField(
            model_name='perfilcliente',
            name='telefono',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Por favor escribe el numero en el formato aceptado sin código de área ej: 3123456789', regex='^(3)([0-9]){9}$')], verbose_name='Telefono'),
        ),
        migrations.CreateModel(
            name='Ciudade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.departamento')),
            ],
        ),
    ]