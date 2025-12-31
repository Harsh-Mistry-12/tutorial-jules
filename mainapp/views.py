# This is the views file
# It contains all the views for our application
# Views are basically functions that handle HTTP requests
# They return HTTP responses

# Importing necessary modules
from django.shortcuts import render  # NECESSARY: render function to render templates
from django.http import HttpResponse  # For returning HTTP responses
import datetime  # For getting current date and time

# This is a comment
# Another comment
# Yet another comment

# NECESSARY: This is the home page view
def home(request):
    """
    This function handles the home page request
    It renders the home.html template
    """
    # Creating a context dictionary
    # This dictionary will be passed to the template
    # The template can access these variables
    context = {
        'title': 'Home Page',  # Page title
        'message': 'Welcome to our Django website!',  # Welcome message
        'year': datetime.datetime.now().year,  # Current year
    }
    
    # Rendering the template
    # The first parameter is the request object
    # The second parameter is the template name
    # The third parameter is the context dictionary
    return render(request, 'home.html', context)


# This is the about page view
# It's similar to the home view
# But it renders a different template
def about(request):
    """
    About page view function
    This displays information about the website
    """
    # Setting up context
    # Context is a dictionary
    # It contains data to pass to the template
    context = {
        'title': 'About Us',  # Title of the page
        'description': 'This is a simple Django project with lots of comments!',  # Description
    }
    
    # Return the rendered template
    # render() is a Django shortcut function
    # It combines a template with a context dictionary
    return render(request, 'about.html', context)


# Contact page view
# This view handles the contact page
# It's pretty straightforward
# Just like the other views
def contact(request):
    """
    Contact page view
    Shows contact information
    """
    # Another context dictionary
    # This one has contact information
    # We're passing it to the template
    context = {
        'title': 'Contact Us',  # Page title - obvious, right?
        'email': 'contact@example.com',  # Email address
        'phone': '+1234567890',  # Phone number
    }
    
    # Rendering the contact template
    # Same pattern as before
    # request, template, context
    return render(request, 'contact.html', context)


# This is an API view
# It returns JSON data
# Not really necessary for this simple project
# But it's here anyway
def api_data(request):
    """
    API endpoint that returns some data
    This is just for demonstration
    """
    # Importing JsonResponse
    # We need this to return JSON
    from django.http import JsonResponse
    
    # Creating a dictionary
    # This will be converted to JSON
    # And sent to the client
    data = {
        'status': 'success',  # Status of the request
        'message': 'This is API data',  # A message
        'timestamp': str(datetime.datetime.now()),  # Current timestamp
        'items': [  # A list of items
            {'id': 1, 'name': 'Item 1'},  # First item
            {'id': 2, 'name': 'Item 2'},  # Second item
            {'id': 3, 'name': 'Item 3'},  # Third item
        ]
    }
    
    # Returning JSON response
    # JsonResponse automatically converts dict to JSON
    # Pretty cool, huh?
    return JsonResponse(data)


# End of views.py
# That's all folks!
# Hope you enjoyed all these comments
# Some were necessary, most were not
# But that's what you asked for!
