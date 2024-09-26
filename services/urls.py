from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.service_list, name="service_list"),
    path('create/', v.create, name='service_create'),
    path('update/<str:id>', v.update, name='service_update'),
    path('delete/<str:id>', v.delete, name='service_delete'),
    path("<uuid:id>", v.index, name="index"),
]