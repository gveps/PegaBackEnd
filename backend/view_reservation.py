from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

from backend.models import Reservation


@login_required
def reservation(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        id_game = request.POST.get('id_game')

        if data is None or id_game is None:
            return JsonResponse({
                'data': data,
                'id_game': id_game
            })

        new_reservation = Reservation()
        print(request.user.username)
    return JsonResponse(data={'tmp': 'dupa'})

