from django.urls import path
from .views import DetalleReserva, ListaEmpresas, DetalleEmpresa

urlpatterns  = [

path('home/', ListaEmpresas.as_view(), name="home-next"),
path('detalle-cancha/<slug>', DetalleEmpresa.as_view(), name="detalle-cancha"),
path('detalle-reserva/<slug>', DetalleReserva.as_view(), name="detalle-reserva"),
]