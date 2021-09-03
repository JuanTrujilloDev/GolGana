from django.contrib import admin
from .models import Ciudad, Departamento, PerfilCliente
# Register your models here.


admin.site.register(PerfilCliente)
admin.site.register(Departamento)
admin.site.register(Ciudad)