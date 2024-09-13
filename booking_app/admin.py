from django.contrib import admin
from .models import Client, Movie, MovieShow, HallSeat

admin.site.register(Client)
admin.site.register(Movie)
admin.site.register(MovieShow)
admin.site.register(HallSeat)
