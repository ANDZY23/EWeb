from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *


def user(request):
    users = User.objects.all()
    return render(request, 'user/user.html', {'users':users})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user.html')
    else:
        form = UserForm()
    return render(request, 'user/add_user.html', {'form': form})

def delete_user(request, room_id):
    room = get_object_or_404(user, id=id)
    room.delete()
    return redirect('user')

def update_user(request, room_id):
    room = get_object_or_404(user, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('user')
    else:
        form = UserForm(instance=room)
    return render(request, 'user/update_user.html', {'form': form})



