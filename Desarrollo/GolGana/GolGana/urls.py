from django.contrib import admin
from django.urls import path, include
from users.urls import post_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include(post_patterns)),
    path('', include('social_django.urls', namespace='social')),
]
