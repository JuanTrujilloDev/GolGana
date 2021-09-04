# Generated by Django 3.2.6 on 2021-09-03 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_rename_ciudade_ciudad'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilcliente',
            name='ciudad',
            field=models.ForeignKey(default=5254, on_delete=django.db.models.deletion.CASCADE, to='users.ciudad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfilcliente',
            name='departamento',
            field=models.ForeignKey(default=151, on_delete=django.db.models.deletion.CASCADE, to='users.departamento'),
            preserve_default=False,
        ),
    ]
