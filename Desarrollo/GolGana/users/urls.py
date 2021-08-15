from django.urls import path
from .views import createUserView, ProfileUpdate
from django.contrib.auth.views import LoginView

post_patterns = ([
    path('registro/', createUserView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('login/', LoginView.as_view(template_name = "login.html"), name="login")
], "user")
