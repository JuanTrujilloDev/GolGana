from django.contrib import admin
from .models import Cancha, Empresa, Reserva

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Cancha)
admin.site.register(Reserva)
