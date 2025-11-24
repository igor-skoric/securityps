from django.shortcuts import render, get_object_or_404
from .services_data import SERVICES, ACTIVITIES
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def test(request):
    context = {}
    return render(request, 'coming_soon.html', context)


def home(request):
    context = {
        "services": SERVICES,
        "extended_services": ACTIVITIES
    }
    return render(request, 'website/index.html', context)


def success(request):
    return render(request, "website/contact_success.html")


def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message = f"Od: {name} <{email}>\n\nPoruka:\n{message}"

            send_mail(
                subject="Nova poruka sa sajta",
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,  # koristi se iz settings.py
                recipient_list=[settings.EMAIL_HOST_USER],  # stiže na tvoj email
                fail_silently=False,
            )

            return render(request, "website/contact_success.html")

    return render(request, "website/contact.html", {"form": form})


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

    service = ACTIVITIES.get(pk)

    if not service:
        from django.http import Http404
        raise Http404("Service not found")

    context = {
        "service": service
    }
    return render(request, 'website/single_service_extended.html', context)


def activities(request):
    context = {
        "activities": ACTIVITIES
    }
    return render(request, 'website/activities.html', context)