from django.contrib import admin
from .models import Ciudad, Departamento, PerfilCliente, PerfilEmpresa, PerfilModerador, User
# Register your models here.


class CiudadAdmin(admin.ModelAdmin):
    model = Ciudad
    ordering = ('departamento', 'nombre')

class DepAdmin(admin.ModelAdmin):
    model = Departamento
    ordering = ['nombre']    


admin.site.register(PerfilCliente)
admin.site.register(PerfilEmpresa)
admin.site.register(PerfilModerador)
admin.site.register(User)
admin.site.register(Departamento, DepAdmin)
admin.site.register(Ciudad, CiudadAdmin)

