from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

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

    description = request.GET.get("description", "")
    photo = request.GET.get("photo")
    game = Game()
    game.title = title
    game.description = description
    game.photo = photo
    game.save()
    valid_json = {
        'result': 'success',
        'message': 'Game added to the system'
    }

    return JsonResponse(valid_json)


def add_extension(request):
    title = request.GET.get("title")
    if title is None or title == "":
        error_json = {
            'result': 'failure',
            'message': 'Invalid Name'
        }
        return JsonResponse(error_json)
    if len(title) > 50:
        error_json = {
            'result': 'failure',
            'message': 'Too long title'
        }
        return JsonResponse(error_json)

    description = request.GET.get("description", "")
    photo = request.GET.get("photo")
    game = Game()
    game.title = title
    game.description = description
    game.photo = photo
    game.save()
    valid_json = {
        'result': 'success',
        'message': 'Game added to the system'
    }

    return JsonResponse(valid_json)
