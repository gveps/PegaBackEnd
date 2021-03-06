from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    id_game = models.IntegerField(auto_created=True)
    # id_entity = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    photo = models.CharField(max_length=50, null=True)
    barcode = models.CharField(max_length=43, default=None, null=True, blank=True)
    rate = models.FloatField(default=5.0)
    id_base_game = models.IntegerField(default=None, null=True, blank=True)
    min_players = models.IntegerField(default=1)
    max_players = models.IntegerField(default=None, null=True)
    time = models.IntegerField(default=None, null=True)
    popularity=models.IntegerField(default=0, null=True)

    def __str__(self):
        return f'title: {self.title} id: {self.id}'


class Malfunction(models.Model):
    idgameentity = models.ForeignKey(Game, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    data = models.DateField()
    solved = models.BooleanField(default=False)


class Reservation(models.Model):
    data = models.DateField()
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    idgame = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    returned = models.BooleanField(default=False)


class CategoryType(models.Model):
    name = models.CharField(max_length=50)


class GameCategory(models.Model):
    id_category = models.ForeignKey(CategoryType, on_delete=models.CASCADE)
    idgame = models.ForeignKey(Game, on_delete=models.CASCADE)


class Event(models.Model):
    title = models.CharField(max_length=50)
    id_reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)


class EventUser(models.Model):
    id_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

