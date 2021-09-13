from django.contrib.auth import views
from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView, PasswordChangeView

post_patterns = ([
    path('registro/', views.createUserView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('accounts/cliente/<slug:slug>/edit-profile/', views.ProfileUpdate.as_view(), name='edit-profile-cliente'),
    path('login/', views.CLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    ###AGREGAR QUE SI EL CORREO NO EXISTE NO DEJE ENVIAR PASSWORD RESET
    path('accounts/password-change/', PasswordChangeView.as_view(success_url='/'), name="password-change"),
    path('social/success', views.socialSuccess, name="social-success"),
    path('redirect/account', views.login_redirect, name="login_redirect"),
    path('json/load/cities', views.json_load, name="json-load-cities"),
], "user")

