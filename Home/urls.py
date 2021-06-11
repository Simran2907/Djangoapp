from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
      path("",views.index, name= 'Home'),
      path("about",views.about, name= 'about'),
      path("service",views.service, name= 'service'),
      path("contact",views.contact, name = 'contact')


]