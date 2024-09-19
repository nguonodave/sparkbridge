from django.urls import path
from . import views as v

urlpatterns = [
    path('register', v.register, name='register'),
    path('register/customer/', v.register_customer, name='register_customer'),
    path('register/company/', v.register_company, name='register_company'),
    path('login/', v.login_user, name='login_user'),
    path('logout/', v.logout_user, name='logout_user'),
]
