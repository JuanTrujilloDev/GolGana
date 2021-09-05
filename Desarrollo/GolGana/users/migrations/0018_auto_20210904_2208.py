# Generated by Django 3.2.6 on 2021-09-05 03:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210904_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilcliente',
            name='ciudad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.ciudad'),
        ),
        migrations.AlterField(
            model_name='perfilcliente',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.departamento'),
        ),
        migrations.AlterField(
            model_name='perfilcliente',
            name='documento',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(regex='^[0-9]{10}$')], verbose_name='Numero de documento'),
        ),
    ]