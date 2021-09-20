from django.contrib import admin
from .models import Cancha, Empresa, Reserva
from django.db import models
from django.forms.widgets import CheckboxSelectMultiple

# Register your models here.
class CanchaAdmin(admin.ModelAdmin):
     formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
admin.site.register(Empresa)
admin.site.register(Cancha, CanchaAdmin)
admin.site.register(Reserva)
