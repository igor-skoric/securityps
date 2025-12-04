from .services_data import SERVICES


def services_dropdown(request):

    return {
        "services_dropdown": SERVICES
    }
