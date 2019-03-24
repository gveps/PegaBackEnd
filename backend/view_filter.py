import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from backend.models import Game, Reservation


def get_filter_game(request):
    if request.method == 'GET':

        # 0, 1, 2, 3, 4
        players = request.GET.get('players')
        # 60, 120, 1000
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

        print(len(games))

        result_game = []
        for game in games:
            if not game.time < int(time):
                continue
            print(f'{game.time} : {time}')
            print(f'players: {game.min_players} : {players}')
            if game.min_players < int(players):
                continue

            result_game.append(game)

        print(len(result_game))
        if int(popularity) == 1:
            top = Game.objects.order_by('-popularity')[0:50]
        else:
            top = Game.objects.order_by('-popularity')[50:120]

        json_result = []
        for game in result_game:
            for g_top in top:
                if game.title == g_top.title:
                    json_game = {
                        'id': game.id,
                        'title': game.title,
                        'description': game.description,
                        'barcode': game.barcode,
                        'rate': game.rate,
                        'min_players': game.min_players,
                        'max_players': game.max_players,
                        'time': game.time
                    }
                    json_result.append(json_game)
        print(len(json_result))

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
            'id': game.id,
            'title': game.title,
            'description': game.description,
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
            status = 0

            test = Reservation.objects.filter(data__range=[datetime.datetime.today().strftime('%Y-%m-%d'), (
                        datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%Y-%m-%d')], idgame=game.id)
            if len(test) > 0:
                status = 1

            test = Reservation.objects.filter(data__range=[datetime.datetime.today().strftime('%Y-%m-%d'), datetime.datetime.today().strftime('%Y-%m-%d')], idgame=game.id)
            if len(test) > 0:
                status = 2

            json = {
                'id': game.id,
                'title': game.title,
                'description': game.description,
                'barcode': game.barcode,
                'rate': game.rate,
                'min_players': game.min_players,
                'max_players': game.max_players,
                'time': game.time,
                'status': status
            }
            result.append(json)
        print(len(result))
        return JsonResponse(result[:15], safe=False)
    else:
        return JsonResponse({'Response': 'use GET'})
