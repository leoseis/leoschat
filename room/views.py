from django.contrib.auth.decorators import login_required            # imprtinf a decorator
from django.shortcuts import render


from .models import Room

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html',{
        'rooms':rooms
    })



# Create your views here.
