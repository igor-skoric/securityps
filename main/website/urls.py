from django.urls import path, include
from .views import home, contact, services, single_service

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('services', services, name='services'),
    path('single_service/<int:pk>', single_service, name='single_service')
]
