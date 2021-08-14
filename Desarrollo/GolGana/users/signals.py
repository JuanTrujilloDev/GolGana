from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import PerfilUsuario


@receiver(post_save, sender=User)
def new_perfil(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(usuario=instance)

@receiver(post_save, sender=User) 
def guardar_perfil(sender, instance, **kwargs):
        instance.perfilusuario.save()