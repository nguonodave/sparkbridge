from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.home, name="home"),
    path('logout/', v.logout_user, name='logout_user'),
]