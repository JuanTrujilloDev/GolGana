# Generated by Django 3.2.6 on 2021-09-20 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0016_alter_cancha_jugadores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancha',
            name='cancha_conformada',
        ),
        migrations.AddField(
            model_name='cancha',
            name='cancha_conformada',
            field=models.ManyToManyField(blank=True, null=True, related_name='_canchas_cancha_cancha_conformada_+', to='canchas.Cancha', verbose_name='Canchas que conforman cancha'),
        ),
    ]