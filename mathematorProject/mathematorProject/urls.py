"""
mathematorProject URL Configuration
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

app_name='mathemator'

urlpatterns = [
    path('', include('mathematorApp.urls')),
    path('admin/', admin.site.urls),
]
