from django.shortcuts import render
from . models import Service

services = [
  {
    "id": 1,
    "name": "Web Development",
    "description": "Custom website design and development using modern technologies.",
    "price": "1200",
    "availability": "Available"
  },
  {
    "id": 2,
    "name": "Graphic Design",
    "description": "Creative design solutions including logos, brochures, and branding materials.",
    "price": "800",
    "availability": "Available"
  },
  {
    "id": 3,
    "name": "Digital Marketing",
    "description": "Strategies for increasing online presence through SEO, social media, and PPC campaigns.",
    "price": "1000",
    "availability": "Limited"
  },
  {
    "id": 4,
    "name": "Consulting",
    "description": "Expert advice on business strategy, operations, and growth.",
    "price": "1500",
    "availability": "Available"
  },
  {
    "id": 5,
    "name": "Technical Support",
    "description": "24/7 support for technical issues and troubleshooting.",
    "price": "500",
    "availability": "Available"
  }
]

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
