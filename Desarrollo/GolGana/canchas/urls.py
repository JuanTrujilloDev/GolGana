from django.urls import path
from .views import ListaEmpresas, DetalleEmpresa

urlpatterns  = [

path('home/', ListaEmpresas.as_view(), name="home-next"),
path('detalle-cancha/<slug>', DetalleEmpresa.as_view(), name="detalle-cancha"),
]