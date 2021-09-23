from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls.base import reverse_lazy, reverse
from .forms import  LoginCaptcha, UserCreationFormWithEmail, EmailForms, ProfileAdminUpdateForms
from django.views import generic
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import Group
from .models import PerfilEmpresa, User
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from .forms import ProfileUpdateForms
from .models import PerfilCliente, Departamento, Ciudad
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.decorators import user_passes_test
import json
from django.templatetags import static
import requests



UserModel = get_user_model()
#Funcion vista de activacion de cuenta
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # Redirect user to login
        messages.success(request, 'Email confirmado correctamente, ahora puedes ingresar.')
        return HttpResponseRedirect(reverse('user:login'))
    else:
        return HttpResponse('Activation link is invalid!')




class createUserView(generic.CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/sign-up.html'
    redirect_authenticated_user = True
    model = User
    
    """ def get_success_url(self):
        return reverse_lazy('user:login')
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated: return super().dispatch(request, *args, **kwargs)
        return redirect('user:login')
        

    def form_valid(self, form):
        # Gguarda el usurio en la base de datos pero con is_active = False
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        # Send confirmation email
        current_site = get_current_site(self.request)
        subject = 'Activate Your ' + current_site.domain + ' Account'
        message = render_to_string('registration/email_confirmation.html',
        {
        "domain": current_site.domain,
        "user": user,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": default_token_generator.make_token(user),},
        )
        to_email = form.cleaned_data.get('email')
        send_mail(subject, message, 'golganaco@gmail.com', [to_email])
        
        messages.success(self.request, 'Porfavor confirma tu email antes de ingresar.')
        return HttpResponseRedirect(reverse('user:login'))  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = "Registro - GolGana"
        return context   

class CLoginView(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True
    authentication_form = LoginCaptcha

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = "Login - GolGana"
        return context 
    

class ProfileClienteUpdate(LoginRequiredMixin, generic.UpdateView):
    form_class = ProfileUpdateForms
    template_name = 'registration/edit_profile.html'
    model = PerfilCliente

    ###SE CAMBIO EL GET OBJECT PORQUE TRAIA SIEMPRE AL REQUEST USER OBJECT 
    # Y NO DEBE SER ASI POR EL SLUG!!!!
    def get_success_url(self):
        return reverse_lazy('user:edit-profile-cliente', kwargs={'slug': self.get_object().slug})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['email'] = EmailForms(self.request.POST, instance = self.request.user)
        else: 
            context['email'] = EmailForms(instance = self.request.user)
        context["tittle"] = "Actualizacion de perfil"
        return context


    ##SE REDIRECCIONA SI EL USUARIO NO ES DUEÑO DEL PERFIL Y QUIERE EDITARLO
    ## O SI NO ES CLIENTE
    def get(self, request, *args, **kwargs):
        object = self.get_object()
        ##REDIRIGIR A ACCESO DENEGADO!!
        grupo = Group.objects.filter(name="Cliente").first()
        if request.user == object.usuario :
            if object == request.user.perfilcliente and request.user.groups == grupo:
                return super().get(self, request, *args, **kwargs)
        return redirect(reverse('home'))
        
    
    def form_valid(self, form):
        context = self.get_context_data()
        with transaction.atomic():
            self.object = form.save()
            if context['email'].is_valid():
                context['email'].save()
        return super(ProfileClienteUpdate, self).form_valid(form)

@login_required(login_url="/login")
def socialSuccess(request):
    defaultgroup = Group.objects.get(name = 'Cliente')
    user = request.user
    user.groups = defaultgroup

    return redirect('user:login')

@login_required
def login_redirect(request):
    perfil = PerfilCliente.objects.get(usuario = request.user)
    return redirect(perfil.get_absolute_url())

'''###JSON IMPORT
@user_passes_test(lambda u: u.is_superuser)
def json_load(request):
    url = 'http://raw.githubusercontent.com/marcovega/colombia-json/master/colombia.json'
    file = json.loads(requests.get(url).text)
    for lines in file:
        departamento = Departamento.objects.create(nombre = lines['departamento'])
        for x in lines['ciudades']:
            ciudad = Ciudad.objects.create(nombre= x, departamento = departamento)
    return redirect('home')'''

@user_passes_test(lambda u: u.is_superuser)
def json_load(request):
    data = requests.get('https://raw.githubusercontent.com/marcovega/colombia-json/master/colombia.min.json')
    my_dict = data.json()   
    for i in my_dict[0:32]:
        departamento = Departamento.objects.create(nombre = i['departamento'])
        for j in range(0, len(i['ciudades'])):Ciudad.objects.create(departamento = departamento, nombre = i['ciudades'][j])
    return redirect('home')

## ACTUALIZAR CONTRASEÑA VIEW


## VISTA ACTUALIZAR DATOS EMPRESARIO

class PerfilEmpresaUpdate(LoginRequiredMixin, generic.UpdateView):
    form_class = ProfileAdminUpdateForms
    model = PerfilEmpresa
    template_name = "registration/edit_profile.html"

        ###SE CAMBIO EL GET OBJECT PORQUE TRAIA SIEMPRE AL REQUEST USER OBJECT 
    # Y NO DEBE SER ASI POR EL SLUG!!!!
    def get_success_url(self):
        return reverse_lazy('user:edit-profile-empresa', kwargs={'slug': self.get_object().slug})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['email'] = EmailForms(self.request.POST, instance = self.request.user)
        else: 
            context['email'] = EmailForms(instance = self.request.user)
        context["tittle"] = "Actualizacion de perfil"
        return context


    ##SE REDIRECCIONA SI EL USUARIO NO ES DUEÑO DEL PERFIL Y QUIERE EDITARLO
    ## O SI NO ES CLIENTE
    def get(self, request, *args, **kwargs):
        object = self.get_object()
        ##REDIRIGIR A ACCESO DENEGADO!!
        grupo = Group.objects.filter(name="Empresa").first()
        if request.user == object.usuario :
            if object == request.user.perfilempresa and request.user.groups == grupo:
                return super().get(self, request, *args, **kwargs)
        return redirect(reverse('home'))
        
    
    def form_valid(self, form):
        context = self.get_context_data()
        with transaction.atomic():
            self.object = form.save()
            if context['email'].is_valid():
                context['email'].save()
        return super(PerfilEmpresaUpdate, self).form_valid(form)






       



