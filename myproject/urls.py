"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # NECESSARY: include is needed to include other URL configs

# URL patterns for the entire project
# This is the main URL configuration
# It includes URLs from other apps
urlpatterns = [
    # Admin site URL
    # This is Django's built-in admin interface
    # Very useful for managing data
    path('admin/', admin.site.urls),
    
    # Main app URLs
    # NECESSARY: This includes all URLs from mainapp
    # The empty string means these URLs are at the root
    path('', include('mainapp.urls')),
]
