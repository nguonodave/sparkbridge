from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Service, RequestService
from . forms import CreateNewService, RequestServiceForm
from django.http import HttpResponseForbidden

# get all services from the database (order by latest first)
def service_list(request):
    services = Service.objects.all().order_by("-date")
    context = {
        "services" : services
    }
    return render(request, 'services/services.html', context)

# get individual service details when a service object is clicked
def index(request, id):
    service = Service.objects.get(id=id)
    context = {
        "service": service
    }
    return render(request, 'services/service.html', context)

# functionality for creating a service
@login_required(login_url='login_user')
def create(request):
    if not request.user.is_company:
            error_context = {
                'exclaim': 'Uh-oh!',
                'status': '403 Forbidden',
                'message': "This feature is a company-only zone. Check out our registration options."
            }
            return HttpResponseForbidden(render(request, "main/errors.html", error_context))

    # get the company parameter to customize field choices
    form = CreateNewService(company=request.user.company)

    if request.method == "POST":
        # print(request.POST)
        form = CreateNewService(request.POST, company=request.user.company)
        if form.is_valid():
            # extract data from the service creation form
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

    context = {
        "form": form
    }
    return render(request, "services/create.html", context)

# functionality for updating a service
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

# functionality for requesting a service
@login_required(login_url='login_user')
def request_service(request, id):
    service = Service.objects.get(id=id)
    form = RequestServiceForm()

    if request.method == "POST":
        form = RequestServiceForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            requested_service = RequestService(
                address = cd['address'],
                time = cd['time'],
                customer = request.user.customer,
                service = service,
                total_cost = service.price_hr * cd['time'],
            )
            requested_service.save()
            return redirect("customer_profile")
    else:
        if not request.user.is_customer:
            error_context = {
                'exclaim': 'Uh-oh!',
                'status': '403 Forbidden',
                'message': "This feature is a customer-only zone. Check out our registration options."
            }
            return HttpResponseForbidden(render(request, "main/errors.html", error_context))

    context = {
        'form': form,
    }
    return render(request, 'services/request_service.html', context)
