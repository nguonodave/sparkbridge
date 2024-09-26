from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='login_user')
def create(request):
    form = CreateNewService(company=request.user.company)
    if request.method == "POST":
        # print(request.POST)
        form = CreateNewService(request.POST, company=request.user.company)
        if form.is_valid():
            cd = form.cleaned_data
            service = Service(
                name = cd["name"],
                description = cd["description"],
                price_hr = cd["price_hr"],
                field = cd["field"],
                company = request.user.company
            )
            service.save()
            return redirect("index", id=service.id)
    else:
        if not request.user.is_company:
            error_context = {
                'error': "Access denied! You are not allowed to access this page. You will be redirected to services page after 5 seconds."
            }
            return render(request, "services/create.html", error_context)

    context = {
        "form": form
    }
    return render(request, "services/create.html", context)

@login_required(login_url='login_user')
def update(request, id):
    service = Service.objects.get(id=id)
    form = CreateNewService(company=request.user.company)
    if request.method == "POST":
        form = CreateNewService(request.POST, company=request.user.company)
        if form.is_valid():
            cd = form.cleaned_data
            service.name = cd["name"]
            service.description = cd["description"]
            service.price_hr = cd["price_hr"]
            service.field = cd["field"]
            service.save()
            return redirect("index", id=service.id)
    else:
        form = CreateNewService(initial={
            'name': service.name,
            'description': service.description,
            'price_hr': service.price_hr,
            'field': service.field
        }, company=request.user.company)

    context = {
        "form": form
    }
    return render(request, "services/create.html", context)

@login_required(login_url='login_user')
def delete(request, id):
    service = Service.objects.get(id=id)
    if request.method == "POST":
        service.delete()
        return redirect("service_list")
    
def service_field(request, field):
    # search for the service present in the url
    field = field.replace('-', ' ').title()
    services = Service.objects.filter(field=field)
    return render(request, 'services/field.html', {'services': services, 'field': field})
