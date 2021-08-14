from django.shortcuts import render
from django.contrib.auth.models import Group
from django.urls.base import reverse_lazy
from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView


class createUserView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'users/signup.html'

    def get_success_url(self):
        return reverse_lazy('user:signup')+'?ok'

    def form_valid(self, form):
        user = form.save(commit=False)
        group = Group.objects.get(name='UsuarioCliente')
        user.save() 
        user.groups.add(group)
        return super().form_valid(form)


            



