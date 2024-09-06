from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.service_list, name="service_list"),
    path("<int:id>", v.index, name="index"),
]