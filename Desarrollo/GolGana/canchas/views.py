from .forms import UpdateEmpresaForm, CrearReserva, CrearCancha
from django.views.generic.edit import CreateView, DeleteView
from users.models import PerfilEmpresa, PerfilCliente, User
from django.urls.base import reverse, reverse_lazy
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

    def get(self, request, *args, **kwargs):
        try:
            perfil = Empresa.objects.get(nombre= self.get_object().nombre)
        except:
            perfil = None
        if self.request.user.groups.name != 'Cliente' and self.request.user != perfil.encargado.usuario:
            return redirect(reverse('home-next'))
        return super().get(request, *args, **kwargs)
    
    
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
        usuario = PerfilCliente.objects.filter(usuario = request.user).first()
        empresario = PerfilEmpresa.objects.filter(usuario = request.user).first()

        if usuario or empresario:
            if (objeto.persona != None and objeto.persona == usuario) or (empresario == objeto.empresa.encargado) or (objeto.persona == None):
                return super().get(request, *args, **kwargs)    
        return(redirect('home-next'))


class VistaAuxReservacion(LoginRequiredMixin, DetailView):
     model = Reserva  

     def get(self, request, *args, **kwargs):
        try: 
            usuario = PerfilCliente.objects.filter(usuario = request.user).first()
        except:
            usuario = None
        if usuario == None:
            return redirect('detalle-reserva', pk = self.get_object().pk) 
        else:
            reserva = Reserva.objects.filter(pk = self.get_object().pk ,persona = usuario).first()
            if reserva:
                if reserva.usuario == usuario:
                    return redirect('detalle-reserva', pk = self.get_object().pk) 
                return redirect('home-next')
            objeto = self.get_object()
            objeto.persona = request.user.perfilcliente
            objeto.estado = 1
            objeto.save()
            return redirect('detalle-reserva', pk = self.get_object().pk) 


#actualizar las canchas
#crear canchas
#lista de reservas
#crear reservas
#actuaizar reservas

#VISTAS EXCLUSIVAS EMPRESA
class UpdateEmpresa(LoginRequiredMixin, UpdateView):
    model = Empresa
    template_name = "update-empresa.html"
    form_class = UpdateEmpresaForm
    #Actualizar datos de la empresa.
    #Aca se veria las Lista de canchas.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            empresa = Empresa.objects.get(encargado = self.request.user.perfilempresa)
        except:
            empresa = None
        context['canchas'] = Cancha.objects.filter(empresa = empresa)
        return context

    def get(self, request, *args, **kwargs):
        try:
            perfil = PerfilEmpresa.objects.get(usuario = request.user)
        except:
            perfil = None
        if perfil:
            return super().get(request, *args, **kwargs)
        return(redirect('home-next'))
    
    

#-------Crear, Actualizar, Eliminar, Listar canchas-----------

class UpdateCanchas(LoginRequiredMixin, UpdateView):
    model = Cancha
    #Aca se actualizan las canchas (Apartado del admin).

class DeleteCanchas(LoginRequiredMixin, DeleteView):
    model = Cancha
    template_name = "eliminar-cancha.html"
    
    def get_success_url(self):
        return reverse_lazy('home-next')

class CrearCanchas(LoginRequiredMixin, CreateView):
    model = Cancha
    form_class = CrearCancha
    template_name = "crear-canchas.html"

    def get_success_url(self):
        return reverse_lazy('home-next')

    def form_valid(self, form):
        cancha = form.save()
        usuario = User.objects.get(username = self.request.user.perfilempresa)
        perfilempresa = PerfilEmpresa.objects.get(usuario = usuario)
        empresa = Empresa.objects.get(encargado = perfilempresa)
        cancha.empresa = empresa
        cancha.save()
        return super().form_valid(form)
class CrearReserva(LoginRequiredMixin, CreateView):
    model = Reserva
    template_name = "crear-reservas.html"
    form_class = CrearReserva

    def get_success_url(self):
        return reverse_lazy('home-next')

    def form_valid(self, form):
        reserva = form.save()
        usuario = User.objects.get(username = self.request.user.perfilempresa)
        perfilempresa = PerfilEmpresa.objects.get(usuario = usuario)
        empresa = Empresa.objects.get(encargado = perfilempresa)
        reserva.empresa = empresa
        reserva.save()
        return super().form_valid(form)

class UpdateReserva(LoginRequiredMixin, UpdateView):
    model = Reserva
    #Aca se actualizan las reservas (Para el admin)

class ListaReservas(LoginRequiredMixin, ListView):
    model = Reserva

#------------------------------------------------------





### VISTAS DE USUARIO CLIENTE

class MisReservaciones(LoginRequiredMixin, DetailView):
    model = PerfilCliente
    template_name = "lista_reserva.html"
    
    def get(self, request, *args, **kwargs):
        if self.request.user != self.get_object().usuario:
            return redirect(reverse('home-view'))
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        perfil = self.get_object()
        if self.request.user == self.get_object().usuario:
            context['reservas'] = Reserva.objects.filter(persona = perfil).order_by('date')
        return context

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










