from django.urls import path
from .views import DetalleReserva, ListaEmpresas, DetalleEmpresa,  VistaAuxReservacion, MisReservaciones, UpdateEmpresa, DeleteCanchas, CrearReserva, CrearCanchas

urlpatterns  = [

path('home/', ListaEmpresas.as_view(), name="home-next"),
path('detalle-cancha/<slug>', DetalleEmpresa.as_view(), name="detalle-cancha"),
path('detalle-reserva/<int:pk>', DetalleReserva.as_view(), name="detalle-reserva"),
path('accounts/cliente/lista-reservas/<slug:slug>', MisReservaciones.as_view(),  name="lista-reservas-cliente"),
path('confirmar-reserva/<int:pk>', VistaAuxReservacion.as_view(), name="vista-reservacion"),
path('update-empresa/<slug>', UpdateEmpresa.as_view(), name='update-empresa'),
path('eliminar-cancha/<int:pk>', DeleteCanchas.as_view(), name='eliminar-cancha'),
path('crear-reserva/', CrearReserva.as_view(), name='crear-reserva'),
path('crear-canchas/', CrearCanchas.as_view(), name='crear-canchas'),
]