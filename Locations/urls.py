from django import views
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/',login, name="login"),
    path('registre/',registre, name="registre"),
    path('visitez/',visitez, name="visitez"),
    path('visite/',visite, name="visite"),
    path('vise/',vise, name="vise"),


]
