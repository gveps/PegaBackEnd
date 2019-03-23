from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.db.models import Max
from backend.models import Game


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def add_game(request):
    title = request.GET.get("title")
    if title is None or title == "":
        error_json = {
            'result': 'failure',
            'message': 'Invalid Name'
        }
        return JsonResponse(data=error_json)
    if len(title) > 50:
        error_json = {
            'result': 'failure',
            'message': 'Too long title'
        }
        return JsonResponse(data=error_json)

    same_titles = Game.objects.filter(title=title)
    if len(same_titles) > 0:
        same_game = same_titles.first()
        id_game = same_game.id_game
    else:
        maxi = Game.objects.latest('id_game')
        id_game = maxi.id_game+1

    base_game_title=request.GET.get('base_game_title')
    id_base_game=None
    if base_game_title is not None:
        base_games = Game.objects.filter(title=base_game_title)
        if len(base_games)>0:
            base_game=base_games.first()
            id_base_game=base_game.id_game
        else:
            id_base_game=None

    description = request.GET.get("description", "")
    photo = request.GET.get("photo")
    game = Game()
    game.title = title
    game.description = description
    game.photo = photo
    game.id_game = id_game
    game.id_base_game=id_base_game
    game.save()

    valid_json = {
        'result': 'success',
        'message': 'Game added to the system'
    }

    return JsonResponse(valid_json)
