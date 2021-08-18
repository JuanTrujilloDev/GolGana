# Generated by Django 3.2.6 on 2021-08-18 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_tipousuario_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipousuario',
            options={'ordering': ['nombre'], 'verbose_name': 'Tipo Usuario', 'verbose_name_plural': 'Tipo Usuario'},
        ),
        migrations.AddField(
            model_name='perfilusuario',
            name='telefono',
            field=models.CharField(default='313', max_length=10, verbose_name='Numero telefonico'),
            preserve_default=False,
        ),
    ]