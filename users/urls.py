from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.register, name='register'),
    path('customer/', v.register_customer, name='register_customer'),
    path('company/', v.register_company, name='register_company'),
]
