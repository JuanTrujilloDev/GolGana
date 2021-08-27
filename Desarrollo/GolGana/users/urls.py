from django.urls import path
from .views import CLoginView, createUserView, ProfileUpdate, activate
from django.contrib.auth.views import LoginView, LogoutView
post_patterns = ([
    path('registro/', createUserView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/',activate, name='activate'),
    path('accounts/profile/', ProfileUpdate.as_view(), name='profile'),
    path('login/', CLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout")
], "user")
