from django.db import models
from django.db.models.deletion import SET_NULL
from users.models import PerfilEmpresa
from users.models import Ciudad, Departamento
from PIL import Image
from django.core.validators import MaxValueValidator

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


    image = models.ImageField(verbose_name=True, upload_to="media\canchas\image", default="canchas\image\default-image.png")


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = self.image
        img = Image.open(img)
        size = (300,300)
        thumb = img.resize(size)
        thumb.save(self.image.path)
    
    def __str__(self) -> str:
        return self.nombre

#CANCHAS:
class Cancha(models.Model):
    nombre = models.CharField(max_length=40, verbose_name="Nombre") #Cancha 5
    #Empresa asociada.
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    #Numero de jugadores.
    jugadores = models.IntegerField(validators=[MaxValueValidator(11)], verbose_name="Numero de jugadores")
    #Si es una cancha pequeña se debe poner a que cancha grande conforma
    cancha_conformada = models.ForeignKey('self', verbose_name="Canchas que conforman cancha", on_delete=models.SET_NULL, null=True)
    #Imagen.
    image = models.ImageField(verbose_name="Imagen", upload_to="media\canchas\image", default="canchas\image\default-image.png")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = self.image
        img = Image.open(img)
        size = (300,300)
        thumb = img.resize(size)
        thumb.save(self.image.path)
    
    def __str__(self) -> str:
        return self.nombre

class Reservas(models.Model):
    #cancha
    #Hora
    #Persona que reservo
    #Estado -> Desocupada /  Ya esta activa /confirmando.
    pass
