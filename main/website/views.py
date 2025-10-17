from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, 'website/index.html', context)


def contact(request):
    context = {}
    return render(request, 'website/contact.html', context)


def services(request):

    context = {}
    return render(request, 'website/services.html', context)


def single_service(request, pk):

    context = {}
    return render(request, 'website/single_service.html', context)