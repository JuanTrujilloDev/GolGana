from django.db import models
from django.db.models.deletion import SET_NULL
from users.models import PerfilEmpresa
from users.models import Ciudad, Departamento
from PIL import Image

# Create your models here.

##SE HARIA EN OTRA APP -> APP CANCHAS
#Modelo Empresa.
class Empresa (models.Model):
    #Datos de la empresa.


    nombre = models.CharField(max_length=40, verbose_name="Nombre")
    encargado = models.ForeignKey(PerfilEmpresa, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=70, verbose_name="Direccion")
    ciudad = models.ForeignKey(Ciudad, null=True, on_delete=models.SET_NULL, verbose_name="Ciudad")
    departamento = models.ForeignKey(Departamento, null=True, on_delete=models.SET_NULL, verbose_name="Departamento")
    #LATITUD a partir de la direccion con API de google.
    latitud = models.CharField(max_length=50, null=True, verbose_name="Latitud")
    longitud = models.CharField(max_length=50, null=True, verbose_name="Longitud")
    #Hora inicial para crear canchas
    hora_inicio = models.TimeField(auto_now_add=False, auto_now=False, null=True)
    #Hora final para crear canchas
    hora_final = models.TimeField(auto_now_add=False, auto_now=False, null=True)
    image = models.ImageField(verbose_name=True, upload_to="media\canchas\image", default="default-image.png")


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = self.image
        img = Image.open(img)
        size = (300,300)
        thumb = img.resize(size)
        thumb.save(self.image.path)

#CANCHAS:

    #Empresa asociada.
    #Numero de jugadores.
    #Si es una cancha pequeña se debe poner a que cancha grande conforma
    #Imagen.