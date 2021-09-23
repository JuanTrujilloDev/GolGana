from django.db import models
from django.db.models.deletion import SET_NULL
from users.models import PerfilEmpresa, PerfilCliente
from users.models import Ciudad, Departamento
from PIL import Image
from django.core.validators import RegexValidator
from django.utils.text import slugify
from datetime import timedelta, date

# Create your models here.

##SE HARIA EN OTRA APP -> APP CANCHAS
#Modelo Empresa.
class Empresa (models.Model):
    #Datos de la empresa.


    nombre = models.CharField(max_length=40, verbose_name="Nombre", default="Nombre Empresa")
    encargado = models.OneToOneField(PerfilEmpresa, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length= 250, verbose_name="Descripcion")
    direccion = models.CharField(max_length=70, verbose_name="Direccion")
    phone_regex = RegexValidator(regex='^(3)([0-9]){9}$', message = "Por favor escribe el numero en el formato aceptado sin código de área ej: 3123456789")
    telefono = models.CharField(validators=[phone_regex], max_length=10, verbose_name="Telefono")
    ciudad = models.ForeignKey(Ciudad, null=True, on_delete=models.SET_NULL, verbose_name="Ciudad")
    departamento = models.ForeignKey(Departamento, null=True, on_delete=models.SET_NULL, verbose_name="Departamento")
    #LATITUD a partir de la direccion con API de google.
    latitud = models.CharField(max_length=50,  verbose_name="Latitud", blank=True, null=True)
    longitud = models.CharField(max_length=50,  verbose_name="Longitud", blank=True, null=True)
    
    #Hora inicial para crear canchas
    hora_inicio = models.TimeField(auto_now_add=False, auto_now=False, null=True)
    #Hora final para crear canchas
    hora_final = models.TimeField(auto_now_add=False, auto_now=False, null=True)


    image = models.ImageField(verbose_name="Imagen", upload_to="media/canchas/image", default="canchas/image/default-image.png")
    slug = models.SlugField(verbose_name="Slug", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.encargado.pk)+ "-" + slugify(self.nombre)
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        size = (600,300)
        thumb = img.resize(size)
        thumb.save(self.image.path)
    
    def __str__(self) -> str:
        id = str(self.pk)
        return str( id +"-"+ self.nombre)

    def get_jugadores(self):
        empresa = Empresa.objects.get(encargado = self.encargado)
        if Cancha.objects.filter(empresa=empresa):
            jugadores = Cancha.objects.filter(empresa = empresa).values_list('jugadores', flat=True).distinct().order_by('jugadores')
            return jugadores

    def get_reservas(self):
        empresa = Empresa.objects.get(encargado = self.encargado)
        reservas = Reserva.objects.filter(empresa = empresa, date__gte = date.today())
        if reservas:
            return reservas.order_by("date")
            

        

#CANCHAS:
class Cancha(models.Model):
    nombre = models.CharField(max_length=40, verbose_name="Nombre") #Cancha 5
    #Empresa asociada.
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    #Numero de jugadores.
    class NumJugadores(models.IntegerChoices):
        FUTBOL5 = 5, '5'
        FUTBOL6 = 6, '6',
        FUTBOL7 = 7, '7',
        FUTBOL8 = 8, '8',
        FUTBOL9 = 9, '9',
        FUTBOL10 = 10, '10',
        FUTBOL11 = 11, '11'

    jugadores = models.IntegerField( default=NumJugadores.FUTBOL5 , choices=NumJugadores.choices, verbose_name="Numero de jugadores")
    #Si es una cancha pequeña se debe poner a que cancha grande conforma
    cancha_conformada = models.ManyToManyField('self', verbose_name="Canchas que conforman cancha",  blank=True)
    #Imagen.
    image = models.ImageField(verbose_name="Imagen", upload_to="media/canchas/image", default="canchas/image/default-image.png")

    class Meta:
        ordering = ['nombre']

    def save(self, *args, **kwargs):
        super(Cancha, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        size = (600,300)
        thumb = img.resize(size)
        thumb.save(self.image.path)
    
    def __str__(self) -> str:
        return self.nombre

class Reserva(models.Model):
    #Empresa a cargo de la reserva
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null = True)
    #cancha
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE, null=True)
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

    estado = models.IntegerField(default = Estados.DISPONIBLE, choices = Estados.choices)
    precio = models.FloatField(verbose_name="Precio", default="0")


    def __str__(self):
        return 'Reserva #: ' + str(self.pk)

    def get_hora_final(self):
        return self.date + timedelta(hours=1)

