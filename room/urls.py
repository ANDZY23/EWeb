from django.urls import path
from . import views

urlpatterns = [
    path('', views.room, name='room'),
    path('add_room/', views.add_room, name='add_room')
]