# URLs configuration for mainapp
# This file maps URLs to views
# When a user visits a URL, Django calls the corresponding view

# Importing path function
# NECESSARY: path is used to define URL patterns
from django.urls import path

# Importing views from the current app
# The dot means current directory
# views contains all our view functions
from . import views

# This is the URL patterns list
# It's a list of path objects
# Each path maps a URL to a view
# Pretty simple concept

# NECESSARY: URL patterns list - defines all routes for this app
urlpatterns = [
    # Home page URL
    # Empty string means root URL
    # It calls the home view
    path('', views.home, name='home'),
    
    # About page URL
    # 'about/' means /about/ in the browser
    # It calls the about view
    # The name parameter is for reverse URL lookup
    path('about/', views.about, name='about'),
    
    # Contact page URL
    # You get the pattern now, right?
    # URL -> view -> template
    path('contact/', views.contact, name='contact'),
    
    # API endpoint URL
    # This returns JSON data
    # Not HTML like the others
    # But same pattern applies
    path('api/data/', views.api_data, name='api_data'),
]

# End of URL configuration
# All routes are defined above
# Django will match URLs from top to bottom
# First match wins
