# Generated by Django 3.2.6 on 2021-08-18 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210818_1232'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipousuario',
            options={'ordering': ['nombre'], 'verbose_name': 'Tipo Usuario'},
        ),
    ]
