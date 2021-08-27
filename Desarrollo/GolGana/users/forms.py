from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text=None, widget=forms.TextInput(attrs={'placeholder':'Digita tu correo electronico'}))
    username = forms.CharField(required=True, help_text=None, widget=forms.TextInput(attrs={'placeholder':'Digita tu usuario'}))
    password1 = forms.CharField(required=True, help_text=None, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'placeholder':'Digita una contraseña'}))
    password2 = forms.CharField(required=True, help_text=None, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder':'Confirma tu contraseña'}))
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    #verifica que el email no este registrado
    def clean_email(self):
        email_passed = self.cleaned_data.get("email")
        email_already_registered = User.objects.filter(email = email_passed).exists()
        user_is_active = User.objects.filter(email = email_passed, is_active = 1)
        if email_already_registered and user_is_active:
            #print('email_already_registered and user_is_active')
            raise forms.ValidationError("Email already registered.")
        elif email_already_registered:
            #print('email_already_registered')
            User.objects.filter(email = email_passed).delete()

        return email_passed

    
    #verifica que el usuario no este tomado
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("El username ya esta registrado")
        return username    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "form-control"


"""--------------Creo que esto sobra-------

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

---------------------------------------------"""

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)