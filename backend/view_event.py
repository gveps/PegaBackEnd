from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

from backend.models import Event


def add_event(request):
    if request.method == 'POST':

        id_reservation = request.POST.get('id_reservation')
        title = request.POST.get('title')

        if title is None or id_reservation is None:
            return JsonResponse({
                'id_reservation': id_reservation,
                'title': title
            })

        event = Event()
        event.id_reservation = id_reservation
        event.title = title

        event.save()

    else:
        return JsonResponse({'Response': 'use POST'})