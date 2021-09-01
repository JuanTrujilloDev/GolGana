
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse



def custom_upload_to(instance, filename):
    old_intance = PerfilCliente.objects.get(pk=instance.pk)
    return 'profiles/image/' + filename

class PerfilCliente(models.Model):

    ##DATOS PERSONALES

    usuario = models.OneToOneField(User, on_delete= models.CASCADE)
    nombre = models.CharField(max_length=60, verbose_name= "Nombre Usuario")
    apellido = models.CharField(max_length=80, verbose_name="Apellido Usuario")
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to = custom_upload_to)
    
    ##DATOS DE FACTURACION
    
    #regex
    telefono = models.CharField(max_length= 10 , verbose_name= "Numero telefonico")
    #direccion
    #documento
    #Departamento -> Foreign Key
    #ciudad -> Foreign Key



    def get_absolute_url(self):
        return reverse("perfil-usuario", kwargs={"slug": self.slug})


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.usuario)
        super(PerfilCliente, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.usuario.username

## MODELO PERFIL EMPRESA
    #Datos del encargado.






    #Foreign Key --> Empresa.


##SE HARIA EN OTRA APP -> APP CANCHAS
#Modelo Empresa.
    #Datos de la empresa.



    #Direccion.
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




#MODELO DEPARTAMENTOS




#MODELO CIUDADES