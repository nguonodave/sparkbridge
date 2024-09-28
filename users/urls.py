from django.urls import path
from . import views as v

urlpatterns = [
    path('register', v.register, name='register'),
    path('register/customer/', v.register_customer, name='register_customer'),
    path('register/company/', v.register_company, name='register_company'),
    path('login/', v.login_user, name='login_user'),
    path('customer/profile/', v.customer_profile, name='customer_profile'),
    path('company/<str:username>/', v.company_profile, name='company_profile'),
]
