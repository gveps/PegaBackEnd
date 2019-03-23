from django.urls import path

from backend import viewStatistics
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_game', views.add_game, name='add_game'),
    path('imageTest', viewStatistics.my_image, name='imageTest'),
    path('calendar', viewStatistics.getReservations, name='calendar'),
    path('statistic', viewStatistics.tmp, name='statistics'),
    path('reservation', view_reservation.reservation, name='reservation'),

]
