from django.urls import path
from .views import createUserView
post_patterns = ([
    path('registro/', createUserView.as_view(), name="signup"),
], "user")
