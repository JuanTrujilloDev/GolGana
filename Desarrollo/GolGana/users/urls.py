from django.urls import path
from .views import createUserView, ProfileUpdate

post_patterns = ([
    path('registro/', createUserView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
], "user")
