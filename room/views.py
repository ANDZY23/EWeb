from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

def room(request):
    rooms = Room.objects.all()
    return render(request, 'room/room.html', {'rooms': rooms})

def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room')
    else:
        form = RoomForm()
    return render(request, 'room/add_room.html', {'form': form})

def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.delete()
    return redirect('room')

def update_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room')
    else:
        form = RoomForm(instance=room)
    return render(request, 'room/update_room.html', {'form': form})



