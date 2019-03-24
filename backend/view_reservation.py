from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

from backend.models import Reservation, Game


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
        new_reservation.data = data
        new_reservation.id_user = request.user
        new_reservation.idgame = Game.objects.get(id=id_game)

        new_reservation.save()

        return JsonResponse({'Reservation': 'done'})
    else:
        return JsonResponse({'Reservation': 'failed, use POST'})


def reservation_id(request):
    if request.method == 'GET':
        id_game = request.GET.get('id_game')

        if id_game is None:
            return JsonResponse({
                'id_game': id_game
            })
        result = []
        test = Reservation.objects.filter(idgame=id_game)
        for elem in test:
            dic = {"data": elem.data, "id_user": elem.id_user.id, "id_game": elem.idgame.id}
            result.append(dic)
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({'Response': 'use GET'})
