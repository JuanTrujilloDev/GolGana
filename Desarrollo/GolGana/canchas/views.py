from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from .models import Cancha, Empresa, Reserva
from django.db.models import Q

# Create your views here.

class ListaEmpresas(LoginRequiredMixin, ListView):
    model = Empresa
    #template de la vista
    template_name = "canchas.html"
    paginate_by = 10
    ordering = "nombre"
    #Aca se listan las empresas 
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        if self.request.method == "GET":
            query = self.request.GET.get("q")
            if query:
                queryset = self.get_queryset()
                context['total'] = queryset.count()
                context['query'] = query
                return context
        return context

    def get_queryset(self):
        if self.request.method == "GET":
            query = self.request.GET.get("q")
            if query:
                queryset = Empresa.objects.filter((Q(nombre__icontains = query) | Q (ciudad__nombre__icontains = query)) | Q(cancha__jugadores = query))
                return queryset
        return super().get_queryset()
        
    
    


class DetalleEmpresa(LoginRequiredMixin, DetailView):
    model = Empresa
    template_name = 'detalle-canchas.html'
    #template de la vista
    #Aca se listan las canchas y sus horarios


class DetalleReserva(LoginRequiredMixin, DetailView):
    model = Reserva
    #Toca traer tambien los datos de la cancha.
    template_name = 'detalle-reserva.html'

    def get(self, request, *args, **kwargs):
        ##ESTA VISTA SOLO LA PUEDEN VER LOS DUEÑOS DE LA EMPRESA Y EL USUARIO CLIENTE
        return super().get(request, *args, **kwargs)




#VISTAS EXCLUSIVAS EMPRESA
class UpdateEmpresa(LoginRequiredMixin, UpdateView):
    model = Empresa
    #Actualizar datos de la empresa.


class UpdateCanchas(LoginRequiredMixin, UpdateView):
    model = Cancha
    #Aca se actualizan las canchas (Apartado del admin).

class UpdateReserva(LoginRequiredMixin, UpdateView):
    model = Reserva
    #Aca se actualizan las reservas (Para el admin)

class ListaReservaciones(LoginRequiredMixin, ListView):
    model = Reserva
    #Aca se verian las reservaciones que estan en proceso de confirmacion o confirmadas.






### VISTAS DE USUARIO CLIENTE
class MisReservas(LoginRequiredMixin, ListView):
    model = Reserva
    #Aca se traen las reservas que ha hecho el usuario.
    #Esto SOLO lo puede ver el usuario

class DetalleMisReservas(LoginRequiredMixin, DetailView):
    model = Reserva
    #Se ve el detalle de la reservacion
    #Solo lo puede ver el usuario cliente.

class VistaConfirmacion(LoginRequiredMixin, DetailView):
    model = Reserva
    #Aca se le diria al usuario que debe confirmar su reserva realizando el pago.
    #Se le da unas opciones de pago.

class ProcesoPago(LoginRequiredMixin, TemplateView):
    #Se agrega la API para realizar el pago (Puede ser una o varia vista dependiendo de las APIS que se usen).
    pass

class VistaReservaConfirmada(LoginRequiredMixin, DetailView):
    model = Reserva
    #Despues de confirmar el pago se le muestra que la reserva ya esta confirmada.










