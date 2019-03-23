from django.urls import path

from backend import view_reservation
from backend import viewStatistics
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_game', views.add_game, name='add_game'),
    path('statistic', viewStatistics.tmp, name='statistics')
    path('reservation', view_reservation.reservation, name='reservation'),
]