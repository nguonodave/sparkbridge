from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.service_list, name="service_list"),
    path('create/', v.create, name='service_create'),
    path("<str:id>", v.index, name="index"),
]