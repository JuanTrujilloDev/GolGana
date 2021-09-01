from django.contrib.auth import views
from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView, PasswordChangeView
post_patterns = ([
    path('registro/', views.createUserView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('accounts/profile/', views.Profile.as_view(), name='profile'),
    path('accounts/email-update/', views.EmailUpdate.as_view(), name='email-update'),
    path('accounts/edit-profile/', views.ProfileUpdate.as_view(), name='edit-profile'),
    path('login/', views.CLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('accounts/password-change/', PasswordChangeView.as_view(success_url='/'), name="password-change"),
    path('social/success', views.socialSuccess, name="social-success")
], "user")
