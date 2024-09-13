from django.shortcuts import render, redirect
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
    form = CreateNewService(choices=Service.choices)
    if request.method == "POST":
        # print(request.POST)
        form = CreateNewService(request.POST, choices=Service.choices)
        if form.is_valid():
            cd = form.cleaned_data
            service = Service(
                name = cd["name"],
                description = cd["description"],
                price_hr = cd["price_hr"],
                field = cd["field"],
            )
            service.save()
            return redirect("index", id=service.id)

    context = {
        "form": form
    }
    return render(request, "services/create.html", context)
