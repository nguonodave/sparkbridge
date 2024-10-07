from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from services.models import Service
from django.db.models import Count

def home(request):
    # get a max of 8 most requested services with more than one request and display them in the home page
    most_requested_services = Service.objects.annotate(request_count=Count('requestservice')).filter(request_count__gt=0).order_by('-request_count')[:8]

    context = {
        'most_requested_services': most_requested_services,
    }
    return render(request, "main/home.html", context)

def logout_user(request):
    django_logout(request)
    return redirect('home')