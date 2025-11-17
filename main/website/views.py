from django.shortcuts import render, get_object_or_404
from .services_data import SERVICES


def test(request):
    context = {}
    return render(request, 'coming_soon.html', context)


def home(request):
    context = {
        "services": SERVICES
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