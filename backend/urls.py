from django.urls import path

from backend import view_reservation, view_filter
from backend import viewStatistics
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_game', views.add_game, name='add_game'),
    path('imageTest', viewStatistics.my_image, name='imageTest'),
    path('calendar', viewStatistics.getReservations, name='calendar'),
    path('statistic', viewStatistics.tmp, name='statistics'),
    path('reservation', view_reservation.reservation, name='reservation'),
    path('get_game_by_title', view_filter.get_game_by_title, name='get_game_by_id'),
    path('get_all_games', view_filter.get_all_games, name='get_all_games'),
    path('get_filter_games', view_filter.get_filter_game, name='get_filter_games'),
    path('add_description', views.add_descriptions, name='add_descriptions'),
    path('import_csv', views.import_csv, name='import_csv')

    path('get_filter_games', view_filter.get_filter_game, name='get_filter_games'),
    path('reservation_id_game', view_reservation.reservation_id),
    path('filter_game', view_filter.filter_game)
]
