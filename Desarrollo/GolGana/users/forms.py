from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import ClearableFileInput
from .models import PerfilCliente
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible, ReCaptchaV2Checkbox

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text=None, widget=forms.TextInput(attrs={'placeholder':'Digita tu correo electronico'}))
    username = forms.CharField(required=True, help_text=None, widget=forms.TextInput(attrs={'placeholder':'Digita tu usuario'}))
    password1 = forms.CharField(required=True, help_text=None, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'placeholder':'Digita una contraseña', 'id':'password-field1'}))
    password2 = forms.CharField(required=True, help_text=None, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder':'Confirma tu contraseña', 'id':'password-field2'}))
    captcha = ReCaptchaField(required = True, widget= ReCaptchaV2Checkbox(attrs={'data-size':'normal', 'required':True}))
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "captcha")

    #verifica que el email no este registrado
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("El email ya esta registrado")
        return email

    
    #verifica que el usuario no este tomado
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("El username ya esta registrado")
        return username    
    
  

class LoginCaptcha(AuthenticationForm):
    captcha = ReCaptchaField(required = True, widget= ReCaptchaV2Checkbox(attrs={'data-size':'normal', 'required':True}))
    class Meta:
        model = User
        fields = ['username', 'password', 'captcha']
    


class ProfileUpdateForms(forms.ModelForm):
    class Meta:
        model = PerfilCliente
        fields = ['nombre', 'apellido', 'image', 'telefono', 'direccion', 'tipo_documento', 'documento']
    
    
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForms, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    





class EmailForms(forms.ModelForm):
    email = forms.EmailField(required=True) 

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email__iexact=email).exists():
                raise forms.ValidationError("El email ya esta registrado")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "form-control"



