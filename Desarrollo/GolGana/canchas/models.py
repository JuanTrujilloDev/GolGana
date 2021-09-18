from django.db import models
from django.db.models.deletion import SET_NULL
from users.models import PerfilEmpresa, PerfilCliente
from users.models import Ciudad, Departamento
from PIL import Image
from django.core.validators import MaxValueValidator
from django.utils.text import slugify

# Create your models here.

##SE HARIA EN OTRA APP -> APP CANCHAS
#Modelo Empresa.
class Empresa (models.Model):
    #Datos de la empresa.


    nombre = models.CharField(max_length=40, verbose_name="Nombre", default="Nombre Empresa")
    encargado = models.ForeignKey(PerfilEmpresa, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=70, verbose_name="Direccion")
    ciudad = models.ForeignKey(Ciudad, null=True, on_delete=models.SET_NULL, verbose_name="Ciudad")
    departamento = models.ForeignKey(Departamento, null=True, on_delete=models.SET_NULL, verbose_name="Departamento")
    #LATITUD a partir de la direccion con API de google.
    latitud = models.CharField(max_length=50,  verbose_name="Latitud", blank=True, null=True)
    longitud = models.CharField(max_length=50,  verbose_name="Longitud", blank=True, null=True)
    
    #Hora inicial para crear canchas
    hora_inicio = models.TimeField(auto_now_add=False, auto_now=False, null=True)
    #Hora final para crear canchas
    hora_final = models.TimeField(auto_now_add=False, auto_now=False, null=True)


    image = models.ImageField(verbose_name=True, upload_to="media\canchas\image", default="canchas\image\default-image.png")
    slug = models.SlugField(verbose_name="Slug", unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pk)+ "-" + slugify(self.nombre)
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
    cancha_conformada = models.ForeignKey('self', verbose_name="Canchas que conforman cancha", on_delete=models.SET_NULL, null=True, blank=True)
    #Imagen.
    image = models.ImageField(verbose_name="Imagen", upload_to="media\canchas\image", default="canchas\image\default-image.png")
    slug = models.SlugField(verbose_name="Slug", unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.empresa.nombre) +"-" + slugify(self.pk)+ "-" + slugify(self.nombre)
        super().save(*args, **kwargs)
        img = self.image
        img = Image.open(img)
        size = (300,300)
        thumb = img.resize(size)
        thumb.save(self.image.path)
    
    def __str__(self) -> str:
        return self.nombre

class Reserva(models.Model):
    #cancha
    cancha = models.ForeignKey(Cancha, on_delete=models.SET_NULL, null=True)
    #Hora y dia
    date = models.DateTimeField(verbose_name= "Fecha y Hora", null=True, auto_now_add=False, auto_now=False)
    #Persona que reservo
    persona = models.ForeignKey(PerfilCliente, on_delete=models.CASCADE, null=True, blank=True)
    #Estado -> Desocupada /  Ya esta activa /confirmando.

    class Estados(models.IntegerChoices):
        DISPONIBLE = 0, 'Disponible'
        POR_CONFIRMAR = 1, 'En confirmacion'
        CONFIRMADA = 2, 'Confirmada'
        CANCELADA = 3, 'Cancelada'
        FINALIZADA = 4, 'Finalizada'

    Estado = models.IntegerField(default = Estados.DISPONIBLE, choices = Estados.choices)

    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = "r"+ slugify(self.pk)
        return super().save(*args, **kwargs)

    def __str__(self):
        return 'Reserva #: ' + str(self.pk)
