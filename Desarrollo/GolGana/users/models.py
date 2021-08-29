
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=15, verbose_name="Tipo Usuario")

    class Meta:
        verbose_name = "Tipo Usuario"
        verbose_name_plural = "Tipo Usuario"
        ordering = ["nombre"]

    def __str__(self) -> str:
        return self.nombre


def custom_upload_to(instance, filename):
    old_intance = PerfilUsuario.objects.get(pk=instance.pk)
    return 'profiles/image/' + filename

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete= models.CASCADE)
    nombre = models.CharField(max_length=60, verbose_name= "Nombre Usuario")
    apellido = models.CharField(max_length=80, verbose_name="Apellido Usuario")
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to = custom_upload_to)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete= models.SET_NULL, null=True, unique=False)
    telefono = models.CharField(max_length= 10 , verbose_name= "Numero telefonico")



    def get_absolute_url(self):
        return reverse("perfil-usuario", kwargs={"slug": self.slug})


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.usuario)
        super(PerfilUsuario, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.usuario.username

