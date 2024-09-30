from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from services.models import Service
from django.db.models import Count

def home(request):
    most_requested_services = Service.objects.annotate(request_count=Count('requestservice')).filter(request_count__gt=0).order_by('-request_count')

    context = {
        'most_requested_services': most_requested_services,
    }
    return render(request, "main/home.html", context)

def logout_user(request):
    django_logout(request)
    return redirect('home')