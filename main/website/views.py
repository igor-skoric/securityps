from django.shortcuts import render, get_object_or_404
from .services_data import SERVICES, SERVICES_EXTENDED


def test(request):
    context = {}
    return render(request, 'coming_soon.html', context)


def home(request):
    context = {
        "services": SERVICES,
        "extended_services": SERVICES_EXTENDED
    }
    return render(request, 'website/index.html', context)


def contact(request):
    context = {}
    return render(request, 'website/contact.html', context)


def services(request):
    context = {
        "services": SERVICES
    }
    return render(request, 'website/services.html', context)


def single_service(request, pk):
    service = SERVICES.get(pk)
    if not service:
        from django.http import Http404
        raise Http404("Service not found")

    context = {
        "service": service
    }
    return render(request, 'website/single_service.html', context)


def single_service_extended(request, pk):

    print(request)
    print(pk)
    service = SERVICES_EXTENDED.get(pk)

    if not service:
        from django.http import Http404
        raise Http404("Service not found")

    context = {
        "service": service
    }
    return render(request, 'website/single_service_extended.html', context)