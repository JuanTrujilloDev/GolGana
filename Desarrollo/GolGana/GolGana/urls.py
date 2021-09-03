from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from users.urls import post_patterns
from .views import Home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(post_patterns)),
    path('', include('social_django.urls', namespace='social')),
    path('', Home.as_view(), name="home"),
]



if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)