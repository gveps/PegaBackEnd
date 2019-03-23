from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    id_game = models.IntegerField()
    id_entity = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    photo = models.CharField(max_length=50, null=True)
    barcode = models.CharField(max_length=43, default=None, null=True)
    rate = models.FloatField(default=5.0)
    id_base_game = models.IntegerField(default=None, null=True)


class Malfunction(models.Model):
    id_game_entity = models.ForeignKey(Game, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    data = models.DateField()
    solved = models.BooleanField(default=False)


class Reservation(models.Model):
    data = models.DateField()
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id_game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    returned = models.BooleanField(default=False)


class CategoryType(models.Model):
    name = models.CharField(max_length=50)


class GameCategory(models.Model):
    id_category = models.ForeignKey(CategoryType, on_delete=models.CASCADE)
    id_game = models.ForeignKey(Game, on_delete=models.CASCADE)
