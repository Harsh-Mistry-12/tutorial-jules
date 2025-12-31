# mainapp/views.py
import datetime
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    """Renders the home page."""
    context = {
        'title': 'Home Page',
        'message': 'Welcome to our Django website!',
        'year': datetime.datetime.now().year,
    }
    return render(request, 'home.html', context)

def about(request):
    """Renders the about page."""
    context = {
        'title': 'About Us',
        'description': 'This is a simple Django project with lots of comments!',
    }
    return render(request, 'about.html', context)

def contact(request):
    """Renders the contact page."""
    context = {
        'title': 'Contact Us',
        'email': 'contact@example.com',
        'phone': '+1234567890',
    }
    return render(request, 'contact.html', context)

def api_data(request):
    """Returns a JSON response with sample data."""
    data = {
        'status': 'success',
        'message': 'This is API data',
        'timestamp': str(datetime.datetime.now()),
        'items': [
            {'id': 1, 'name': 'Item 1'},
            {'id': 2, 'name': 'Item 2'},
            {'id': 3, 'name': 'Item 3'},
        ]
    }
    return JsonResponse(data)
