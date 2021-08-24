from django.contrib import admin
from django.urls import path, include
from users.urls import post_patterns
from .views import Home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(post_patterns)),
    path('', include('social_django.urls', namespace='social')),
    path('', Home.as_view(), name="home")
]
