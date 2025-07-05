    # C:\Users\ashok_wsg2ds5\my-pythonDjango1\config\views.py

from django.shortcuts import render

def home(request):
        # This view will render your home.html template
        return render(request, 'home.html')

def about(request):
        # This view will render your about.html template.
        # Make sure you have a templates/about.html file (even if it's just <h1>About Us</h1>)
        return render(request, 'about.html')
