from django.http import HttpResponse

from backend.models import Reservation, Game

def tmp(request):
    games = Game.objects.all()
    reservations = Reservation.objects.all()
    result = []
    tmp = {'title': 'a', 'count': 0}

    for ele in games:
        count = len(Reservation.objects.get(title=ele.title))
        tmp = {'title': ele.title, 'count': count}
        result.append(tmp)
    result.sort()
    print(result)
    return HttpResponse("Hello, statistics.")
