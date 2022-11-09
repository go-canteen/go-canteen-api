from rest_framework import serializers
from .models import Pengguna
from django.utils.translation import gettext_lazy as _


class MinimizedPenggunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengguna
        fields = ["id", "display_name"]


class PenggunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengguna
        fields = [
            "id",
            "email",
            "display_name",
        ]
