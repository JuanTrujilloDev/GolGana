
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.core.validators import RegexValidator

#MODELO DEPARTAMENTOS
class Departamento(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre



#MODELO CIUDADES
class Ciudad(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete= models.CASCADE)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        nombre = self.nombre

        return nombre


def custom_upload_to(instance, filename):
    old_intance = PerfilCliente.objects.get(pk=instance.pk)
    return 'profiles/image/' + filename

class PerfilCliente(models.Model):
    DOC_CHOICES =(
    ("1", "CC"),
    ("2", "CE"),
    ("3", "TI"),
    ("4", "PA"),
)
    ##DATOS PERSONALES

    usuario = models.OneToOneField(User, on_delete= models.CASCADE)
    nombre = models.CharField(max_length=60, verbose_name= "Nombre Usuario")
    apellido = models.CharField(max_length=80, verbose_name="Apellido Usuario")
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to = custom_upload_to, default='profiles/image/default-profile.png')
    
    ##DATOS DE FACTURACION
    
    phone_regex = RegexValidator(regex='^(3)([0-9]){9}$', message = "Por favor escribe el numero en el formato aceptado sin código de área ej: 3123456789")
    telefono = models.CharField(validators=[phone_regex], max_length=10, verbose_name="Telefono")
    direccion = models.CharField(max_length= 70, verbose_name="Direccion")
    tipo_documento = models.CharField(max_length=300, choices = DOC_CHOICES)
    documento_regex = RegexValidator(regex='^[0-9]{10}$')
    documento = models.CharField(validators=[documento_regex],max_length=13, verbose_name="Numero de documento")
    departamento = models.ForeignKey(Departamento, on_delete= models.DO_NOTHING, null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete= models.DO_NOTHING, null=True, blank=True)



    def get_absolute_url(self):
        return reverse("user:edit-profile", kwargs={"slug": self.slug})


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.usuario)
        super(PerfilCliente, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        output_size = (300,300)
        img.thumbnail(output_size)
        img.save(self.image.path)

    def __str__(self) -> str:
        return self.usuario.username

## MODELO PERFIL EMPRESA
    #Datos del encargado.






    #Foreign Key --> Empresa.


##SE HARIA EN OTRA APP -> APP CANCHAS
#Modelo Empresa.
    #Datos de la empresa.



    #Direccion.
    #CIUDAD.
    #DEPARTAMENTO.
    #LATITUD a partir de la direccion con API de google.
    #LONGITUD 


#CANCHAS:

    #Empresa asociada.
    #Numero de jugadores.
    #Si es una cancha pequeña se debe poner a que cancha grande conforma
    #Imagen.




## APP MODERADOR
# MODELO PERFIL MODERADOR
    #DATOS DEL MODERADOR




