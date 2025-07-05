"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

# Import views from your main 'config' project for home/about pages
from . import views

urlpatterns = [
    # Static and Media file serving for local development (only needed in DEBUG=True)
    # In production on PythonAnywhere, these are handled by the web server config
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    path('admin/', admin.site.urls),

    # Your main project's home and about views
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Include URLs from your 'myQuill' app
    path('posts/', include('myQuill.urls')),

    # CORRECTED: Uncomment and include 'users.urls' with a namespace
    path('users/', include('users.urls')), # This will automatically use 'users' as the namespace if app_name is set in users/urls.py
]

# This line is for serving media files ONLY in DEBUG=True (local development)
# It's usually commented out or removed in production as handled by web server
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
