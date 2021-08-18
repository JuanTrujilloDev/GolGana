from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import PerfilUsuario
from django.contrib.auth.models import Group


@receiver(post_save, sender=User)
def new_perfil(sender, instance, created, **kwargs):
    ### -> PREGUNTAR PERFIL
    group = Group.objects.get(name='UsuarioCliente')
    instance.groups.add(group)
    
    if created:
        if(instance.groups.filter(name="UsuarioCliente")):
            PerfilUsuario.objects.create(usuario=instance)
        else:
            print("Error")

@receiver(post_save, sender=User) 
def guardar_perfil(sender, instance, **kwargs):
        instance.perfilusuario.save()