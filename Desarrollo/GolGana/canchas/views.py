from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from .models import Cancha, Empresa, Reserva

# Create your views here.

class ListaEmpresas(LoginRequiredMixin, ListView):
    model = Empresa
    #template de la vista
    template_name = "canchas.html"
    paginate_by = 10
    #Aca se listan las empresas 



class DetalleEmpresa(LoginRequiredMixin, DetailView):
    model = Empresa
    #template de la vista
    #Aca se listan las canchas y sus horarios


class DetalleReserva(LoginRequiredMixin, DetailView):
    model = Reserva
    #Toca traer tambien los datos de la cancha.




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










