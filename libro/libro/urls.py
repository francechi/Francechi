from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    re_path(r'^', include('apps.home.urls')),
    re_path(r'^', include('apps.biblioteca.urls')),
    re_path('admin/', admin.site.urls),
]
