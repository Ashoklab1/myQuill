# C:\Users\ashok_wsg2ds5\my-pythonDjango1\users\urls.py

from django.urls import path
from . import views # Import views from your users app

app_name = 'users' # <--- This is the crucial line for defining the namespace!

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Add other URL patterns for your users app here if you have them
]
