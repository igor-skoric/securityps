from django.urls import path, include
from .views import home, contact, services, single_service, single_service_extended, test

urlpatterns = [
    path('', home, name='home'),
    path('test', test, name='test'),
    path('contact', contact, name='contact'),
    path('services', services, name='services'),
    path('single_service/<int:pk>', single_service, name='single_service'),
    path('activities/<int:pk>', single_service_extended, name='single_service_extended')
]
