from django.contrib import admin

from backend.models import Game, Malfunction, Reservation, CategoryType, GameCategory, Event, EventUser

admin.site.register(Game)
admin.site.register(Malfunction)
admin.site.register(Reservation)
admin.site.register(CategoryType)
admin.site.register(GameCategory)
admin.site.register(Event)
admin.site.register(EventUser)
