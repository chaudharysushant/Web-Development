from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path('about', views.about, name='about'),
    path("service", views.service, name='service'),
    path('index', views.index, name='index'),
    path('contact', views.contact, name='contact'),
       
]