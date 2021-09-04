from django.contrib import admin
from .models import Ciudad, Departamento, PerfilCliente
# Register your models here.


class CiudadAdmin(admin.ModelAdmin):
    model = Ciudad
    ordering = ('departamento', 'nombre')

class DepAdmin(admin.ModelAdmin):
    model = Departamento
    ordering = ['nombre']    


admin.site.register(PerfilCliente)
admin.site.register(Departamento, DepAdmin)
admin.site.register(Ciudad, CiudadAdmin)

