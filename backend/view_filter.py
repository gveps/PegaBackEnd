from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

from backend.models import Game


def get_filter_game(request):
    if request.method == 'GET':

        # 0, 1, 2, 3, 4
        players = request.GET.get('players')
        # 60, 120, 0
        time = request.GET.get('time')
        # 0-non popular, 1-popular
        popularity = request.GET.get('popularity')

        if popularity is None or players is None or time is None:
            return JsonResponse({
                'players': players,
                'time': time,
                'popularity': popularity
            })

        games = Game.objects.all()

        result_game = []
        for game in games:
            if not (game.min_players >= players):
                continue

            if not (game.time <= time):
                continue

            result_game.append(game)

        if popularity == 1:
            top = Game.objects.order_by('-popularity')[:10]
        else:
            top = Game.objects.order_by('-popularity')[40:50]

        json_result = []
        for game in result_game:
            for g_top in top:
                if game.title == g_top.title:
                    json_game = {
                        'title': game.title,
                        'description': game.description,
                        'photo': game.photo,
                        'barcode': game.barcode,
                        'rate': game.rate,
                        'min_players': game.min_players,
                        'max_players': game.max_players,
                        'time': game.time
                    }
                    json_result.append(json_game)

        return JsonResponse(json_result, safe=False)
    else:
        return JsonResponse({'Response': 'use GET'})


def get_game_by_title(request):
    if request.method == 'GET':
        title = request.GET.get('title')

        if title is None:
            return JsonResponse({'title': title})

        game = Game.objects.filter(title=title)

        if len(game) < 1:
            return JsonResponse({"Game not exist": title})
        else:
            game = game.first()

        json_game = {
            'title': game.title,
            'description': game.description,
            'photo': game.photo,
            'barcode': game.barcode,
            'rate': game.rate,
            'min_players': game.min_players,
            'max_players': game.max_players,
            'time': game.time
        }
        return JsonResponse(json_game)
    else:
        return JsonResponse({'Response': 'use GET'})


def get_all_games(request):
    if request.method == 'GET':
        games = Game.objects.all()

        result = []
        for game in games:
            json = {
                'title': game.title,
                'description': game.description,
                'photo': game.photo,
                'barcode': game.barcode,
                'rate': game.rate,
                'min_players': game.min_players,
                'max_players': game.max_players,
                'time': game.time
            }
            result.append(json)
        print(result)
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({'Response': 'use GET'})
