from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import widgets
from .models import PerfilUsuario
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text=None)
    username = forms.CharField(required=True, help_text=None)
    password1 = forms.CharField(required=True, help_text=None, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    password2 = forms.CharField(required=True, help_text=None, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya esta registrado")
        return email



class EmailForms(forms.ModelForm):
    email = forms.EmailField(required=True) 

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya esta registrado")
        return email

