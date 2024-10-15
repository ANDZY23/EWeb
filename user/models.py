from django.db import models
import os
import uuid

#file path sa image
def get_upload_path(instance, filename):
    filename = f"{uuid.uuid4()}{os.path.splitext(filename)[1]}"
    return os.path.join('media/', filename)

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    contact_num=models.IntegerField()

    def __str__(self):
        return f"{self.name}"
    

