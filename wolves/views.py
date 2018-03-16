from django.shortcuts import render
from .models import *
from datetime import datetime


def index(request):
    return render(request, "wolves/home.html", {})


def room(request, room_name):
    try:
        room_object = Room.objects.get(name=room_name)
    except Room.DoesNotExist:
        room_object = Room(name=room_name, player_count=0, time_started=datetime.now())
        room_object.save()

    context = {'room_name': room_name,
               'player_count': room_object.player_count,
               'time_started': room_object.time_started,
               # 'players': [Player.objects.filter(room__name=room_name)],
               }

    if 'player' in request.POST:

        context['player_name'] = request.POST['player']

        player, created = Player.objects.get_or_create(
            name=request.POST['player'],
            room=room_object,
        )
        if created:
            room_object.player_count += 1
            room_object.save()
            context['player_count'] = room_object.player_count

        return render(request, "wolves/player_room.html", context)

    else:

        return render(request, "wolves/room.html", context)
