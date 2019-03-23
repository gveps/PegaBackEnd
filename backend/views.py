from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from backend.models import Game


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def add_game(request):
    game = Game()
    game.id_game = 11
    game.id_entity = 13
    game.title = "Test Game"
    game.save()
    json={
        'result':'failure',
        'message':'Empty Request'
    }
    return JsonResponse(json)
