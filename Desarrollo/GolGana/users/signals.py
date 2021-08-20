
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import PerfilUsuario, TipoUsuario


@receiver(post_save, sender=User)
def newPerfil(sender, instance, created, **kwargs):
    
    if created:
        PerfilUsuario.objects.create(usuario=instance)

@receiver(post_save, sender=User) 
def guardarPerfil(sender, instance, **kwargs):
        tipo = TipoUsuario.objects.get(nombre="Cliente")
        instance.perfilusuario.tipo_usuario = tipo
        instance.perfilusuario.save()