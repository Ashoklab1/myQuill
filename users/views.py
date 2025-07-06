# my-pythonDjango1/users/views.py

from django.shortcuts import render, redirect
# Import your custom forms
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login, logout

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) # Use custom form
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('myQuill:post_list')
    else:
        form = CustomUserCreationForm() # Use custom form
    return render(request, 'users/register.html', {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST) # Use custom form
        if form.is_valid():
            login(request, form.get_user())
            return redirect(request.POST.get("next") or 'myQuill:post_list')
    else:
        form = CustomAuthenticationForm() # Use custom form
    return render(request, 'users/login.html', {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect('myQuill:post_list')