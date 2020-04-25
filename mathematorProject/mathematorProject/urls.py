"""
mathematorProject URL Configuration
"""
from django.urls import include, path

app_name='mathemator'

urlpatterns = [
    path('', include('mathematorApp.urls')),
]
