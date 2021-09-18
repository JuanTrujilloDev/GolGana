
from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver
from .models import PerfilCliente, PerfilEmpresa, PerfilModerador, User
from canchas.models import Empresa


##PERFIL POR FORMULARIO
@receiver(post_save, sender = User)
def agregarPerfil(instance, sender, created, **kwargs):
    grupo_cliente = Group.objects.get(name = "Cliente")
    grupo_empresa = Group.objects.get(name = "Empresa")
    grupo_moderador = Group.objects.get(name = "Moderador")
    


    if created:
        instance.groups = grupo_cliente
        PerfilCliente.objects.get_or_create(usuario = instance)
        instance.save()
    

    else:

        if instance.groups == grupo_cliente:
            if PerfilEmpresa.objects.filter(usuario = instance):
                perfil = PerfilEmpresa.objects.get(usuario = instance)
                perfil.delete()

            elif PerfilModerador.objects.filter(usuario = instance):
                perfil = PerfilModerador.objects.get(usuario = instance)
                perfil.delete()
            
            PerfilCliente.objects.get_or_create(usuario = instance)

        elif instance.groups == grupo_empresa:

            if PerfilCliente.objects.filter(usuario = instance):
                perfil = PerfilCliente.objects.get(usuario = instance)
                perfil.delete()

            elif PerfilModerador.objects.filter(usuario = instance):
                perfil = PerfilModerador.objects.get(usuario = instance)
                perfil.delete()
            
            perfil = PerfilEmpresa.objects.get_or_create(usuario = instance)[0]
            Empresa.objects.get_or_create(encargado = perfil)

        elif instance.groups == grupo_moderador:

            if PerfilCliente.objects.filter(usuario = instance):
                perfil = PerfilCliente.objects.get(usuario = instance)
                perfil.delete()

            elif PerfilEmpresa.objects.filter(usuario = instance):
                perfil = PerfilEmpresa.objects.get(usuario = instance)
                perfil.delete()
                
            
            PerfilModerador.objects.get_or_create(usuario = instance)

