from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ...

class Movie(models.Model):
    name = models.CharField(max_length = 20)
    film_studio = models.CharField(max_length = 80)
    age_category = models.CharField(max_length = 5)
    year = models.CharField(max_length = 5)
    rating = models.CharField(max_length = 10)
    time = models.CharField(max_length = 5)

    class Meta:
        ...

class MovieShow(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.SET_DEFAULT, default = "uncommon movie")
    time = models.TimeField()

    class Meta:
        ...

class HallSeat(models.Model):
    hall = models.CharField(max_length = 50)
    seat = models.ForeignKey(MovieShow, on_delete=models.CASCADE)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)

    class Meta:
        ...

class Booking(models.Model):
    client = models.CharField(max_length = 1000)
    row = models.CharField(max_length = 50)
    seat = models.CharField(max_length = 50)
    price = models.CharField(max_length = 50)
    booking_time = models.DateField(auto_now_add=True)