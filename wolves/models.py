from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=20)
    player_count = models.IntegerField()
    time_started = models.DateTimeField()


class Player(models.Model):
    name = models.CharField(max_length=50)
    room = models.ForeignKey(Room, related_name='room', on_delete=models.CASCADE)
