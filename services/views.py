from django.shortcuts import render
from . models import Service
from . forms import CreateNewService

def service_list(request):
    services = Service.objects.all().order_by("-date")
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

def create(request):
    form = CreateNewService()
    context = {
        "form": form
    }
    return render(request, "services/create.html", context)
