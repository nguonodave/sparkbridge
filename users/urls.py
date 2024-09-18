from django.urls import path
from . import views as v

urlpatterns = [
    path('customer/', v.register_customer, name='register_customer'),
]