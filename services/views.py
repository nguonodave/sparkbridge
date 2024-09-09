from django.shortcuts import render

def service_list(request):
    return render(request, 'services/services.html')

def index(request, id):
    return render(request, 'services/service.html')
