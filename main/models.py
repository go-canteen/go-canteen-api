from django.db import models
import uuid


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


class CanteenBanner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    canteen = models.ForeignKey(Canteen, on_delete=models.CASCADE)
    image = models.URLField(max_length=255)
    is_active = models.BooleanField(default=True)
    on_click_url = models.URLField(max_length=255, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.canteen.name + ": " + str(self.id)
