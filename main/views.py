from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout

def home(request):
    return render(request, "main/home.html")

def logout_user(request):
    django_logout(request)
    return redirect('home')