from django.urls.base import reverse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from .models import Cancha, Empresa, Reserva
from django.db.models import Q
from datetime import timedelta

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
                context['tittle'] = "Lista de empresas"
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

    def get_context_data(self, *args,  **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tittle'] = "Empresa: " + self.object.slug
        return context
    
    
class DetalleReserva(LoginRequiredMixin, DetailView):
    model = Reserva
    #Toca traer tambien los datos de la cancha.
    template_name = 'detalle-reserva.html'

    def get_context_data(self,  **kwargs):
        context =  super().get_context_data(**kwargs)
        context['hora_final'] = self.object.date + timedelta(hours=1)
        context['tittle'] = "Reserva #: " + str(self.object.pk)
        return context

    def get(self, request, *args, **kwargs):
        ##ESTA VISTA SOLO LA PUEDEN VER LOS DUEÑOS DE LA EMPRESA Y EL USUARIO CLIENTE
        objeto = self.get_object()
        try:
            usuario= objeto.persona.usuario
        except:
            usuario = None
        if request.user == usuario or objeto.cancha.empresa.encargado == request.user.perfilempresa :
            return super().get(request, *args, **kwargs)
        else:
            
            #return redirect(reverse('404'))
            return redirect(reverse('home-next'))


        




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










