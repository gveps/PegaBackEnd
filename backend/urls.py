from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_game', views.add_game,name='add_game')
]