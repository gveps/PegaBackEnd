import os

from django.http import HttpResponse, JsonResponse

from backend.models import Reservation, Game
from django.db.models import Count
import json

def tmp(request):
    # games = Game.objects.all()
    topReservations = Reservation.objects.values('idgame').annotate(total=Count('idgame')).order_by('-total')[:10]
    result = []

    for elem in topReservations:
        myGame = Game.objects.get(id=elem['idgame'])

        # image_file = open("backend/resources/game_photos/" + myGame.photo, "rb")
        # encoded_string = base64.b64encode(image_file.read())
        #
        # base64_string = encoded_string.decode('utf-8')

        dic = {"id": myGame.id, "Id_game": myGame.id_game, "Title": myGame.title, "Description": myGame.description, "Photo": myGame.photo, "Barcode": myGame.barcode, "Rate": myGame.rate, "Id_base_game": myGame.id_base_game, "Min_players": myGame.min_players, "Max_players": myGame.max_players, "Time": myGame.time}
        # image_file.close()
        result.append(dic)

    return JsonResponse(dic, safe=False)


def my_image(request):
    file_name = request.GET.get('filename', '')
    root, extention =  os.path.splitext(file_name)
    image_data = open("backend/resources/game_photos/" + file_name, "rb").read()
    return HttpResponse(image_data, content_type="image/" + extention)


def getReservations(request):
    data_start = request.GET.get('dataStart', '')
    data_end = request.GET.get('dataEnd', '')
    result = []
    test = Reservation.objects.filter(data__range=[data_start, data_end])
    for elem in test:
        # print(elem.Id_user)
        dic = {"Data": elem.data, "Id_user": elem.id_user.id, "Id_game": elem.idgame.id}
        result.append(dic)
    # print(dic)
    return JsonResponse(result, safe=False)
