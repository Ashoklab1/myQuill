# C:\Users\ashok_wsg2ds5\my-pythonDjango1\users\views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # CORRECTED: Changed 'posts:post_list' to 'myQuill:post_list'
            return redirect('myQuill:post_list')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # CORRECTED: Changed 'posts:post_list' to 'myQuill:post_list'
            return redirect(request.POST.get("next") or 'myQuill:post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
    # CORRECTED: Changed 'posts:post_list' to 'myQuill:post_list'
    return redirect('myQuill:post_list')
