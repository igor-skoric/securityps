from django.shortcuts import render, get_object_or_404
from .services_data import SERVICES, ACTIVITIES
from .forms import ContactForm, JobApplicationForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
import mimetypes


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
                recipient_list=['officesmartps@gmail.com', settings.EMAIL_HOST_USER],  # stiže na tvoj email
                fail_silently=False,
            )

            return render(request, "website/contact_success.html")

    return render(request, "website/contact.html", {"form": form})


def jobs(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()  # Sačuvaj u bazu

            # Slanje email-a sa fajlom
            email = EmailMessage(
                subject=f"ZAPOSLENJE sa sajta:  {application.name}",
                body=(
                    f"Ime i prezime: {application.name}\n"
                    f"Email: {application.email}\n"
                    f"Telefon: {application.phone}\n"
                    f"Godina rođenja: {application.birth_year}\n"
                    f"Poruka: {application.message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.DEFAULT_FROM_EMAIL, 'officesmartps@gmail.com'],  # zameni sa pravim email-om
            )

            if application.cv:
                application.cv.open()
                file_mime = mimetypes.guess_type(application.cv.name)[0] or "application/octet-stream"

                email.attach(
                    application.cv.name,
                    application.cv.read(),
                    file_mime
                )
                application.cv.close()

            # Pošalji email
            email.send(fail_silently=False)

            # Render uspeh stranice
            return render(request, "website/contact_success.html")

    else:
        form = JobApplicationForm()

    return render(request, "website/jobs.html", {"form": form})


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