from django.shortcuts import render
from django.urls.base import reverse_lazy
from .forms import UserCreationFormWithEmail
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class createUserView(generic.CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/sign-up.html'

    def get_success_url(self):
        return reverse_lazy('login')+'?register'


   


    

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(generic.TemplateView):
    success_url = reverse_lazy('user:profile')
    template_name = 'registration/profile_form.html'

       



