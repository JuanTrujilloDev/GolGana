# Generated by Django 3.2.6 on 2021-09-19 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_groups'),
        ('canchas', '0009_alter_empresa_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancha',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='Slsug'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='encargado',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.perfilempresa'),
        ),
    ]