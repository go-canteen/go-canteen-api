from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


User = get_user_model


class Pengguna(AbstractUser):
    """
    This is the base model for the user.
    """

    first_name = None
    last_name = None
    display_name = models.CharField(max_length=64, blank=True, null=True)

    def get_full_name(self):
        return self.display_name.strip()

    def get_short_name(self):
        if self.display_name:
            return self.display_name.strip().split(" ")[0]
        return self.username

    def get_name(self):
        name = self.get_full_name()
        if name:
            return name
        else:
            return self.username

    def __str__(self) -> str:
        return f"{self.id} | {self.email}"
