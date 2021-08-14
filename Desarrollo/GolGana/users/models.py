from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class PerfilUsuario (models.Model):
    usuario = models.OneToOneField(User, on_delete= models.CASCADE)
    nombre = models.CharField(max_length=60, verbose_name= "Nombre Usuario")
    apellido = models.CharField(max_length=80, verbose_name="Apellido Usuario")
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to = 'usuario')    



    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.usuario)
        super(PerfilUsuario, self).save(*args, **kwargs)

    