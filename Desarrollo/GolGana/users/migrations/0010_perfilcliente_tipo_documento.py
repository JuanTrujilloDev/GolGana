# Generated by Django 3.2.6 on 2021-09-02 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_perfilcliente_documento'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilcliente',
            name='tipo_documento',
            field=models.CharField(choices=[('1', 'CC'), ('2', 'CE'), ('3', 'TI'), ('4', 'PA')], default='CC', max_length=300),
            preserve_default=False,
        ),
    ]