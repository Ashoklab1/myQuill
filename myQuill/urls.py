# myQuill/urls.py

from django.urls import path
from . import views # Import views from your myQuill app

app_name = 'myQuill' # Or 'posts' if you want to keep the namespace consistent with previous 'posts'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.new_post, name='new_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    # Add other URL patterns specific to your myQuill app here
]
