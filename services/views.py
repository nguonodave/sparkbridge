from django.shortcuts import render
from django.http import HttpResponse

def service_list(request):
    return HttpResponse("these are services")

def index(request, id):
    return HttpResponse("this is service" + " " + str(id))
