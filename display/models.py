from django.db import models
from room.models import Room

class Data(models.Model):

    label = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    room_name = models.ForeignKey(Room, on_delete=models.PROTECT, null=True)
    timestamp = models.DateTimeField(null=True, blank=True)
