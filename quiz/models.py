from django.db import models
from django.core.files.storage import FileSystemStorage

photosPath = FileSystemStorage(location='/media/photos')

class Techniques(models.Model):
    name = models.CharField(max_length=200)
    belt_group = models.ForeignKey('Belt_group', on_delete=models.CASCADE)
    photo = models.ImageField(null=True)
    def __str__(self):
        return self.name

class Belt_group(models.Model):
    belt_color = models.CharField(max_length=200)
    def __str__(self):
        return self.belt_color
