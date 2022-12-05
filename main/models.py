from django.db import models
import uuid

# Create your models here.
class Canteen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField(max_length=255, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    canteen = models.ForeignKey(Canteen, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField(max_length=255, blank=True, null=True)
    price = models.IntegerField()
    kelompok = models.CharField(max_length=255)

    def __str__(self):
        return self.name