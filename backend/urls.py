from django.urls import path

from backend import view_reservation
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reservation', view_reservation.reservation, name='reservation'),
    path('add_game', views.add_game, name='add_game')
]