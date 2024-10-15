from django.db import models

class Room(models.Model):

    room_name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)