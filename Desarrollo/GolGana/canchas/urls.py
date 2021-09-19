from django.urls import path
from .views import ListaEmpresas

urlpatterns  = [

path('home/', ListaEmpresas.as_view(), name="home-next"),

]