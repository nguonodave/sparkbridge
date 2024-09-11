from django.shortcuts import render
from . models import Service

def service_list(request):
    services = Service.objects.all()
    context = {
        "services" : services
    }
    return render(request, 'services/services.html', context)

def index(request, id):
    service = Service.objects.get(id=id)
    context = {
        "service": service
    }
    return render(request, 'services/service.html', context)
