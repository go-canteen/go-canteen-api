from django.contrib.auth.models import User, Group
from rest_framework import serializers

from main.models import Canteen


class UserSerializer(serializers.HyperlinkedModelSerializer):
    token = serializers.CharField(source="auth_token.key", read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "token",
        )
        read_only_fields = ("id", "token", "groups")

class CanteenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canteen
        fields = (
            "id",
            "name",
            "address",
            "description",
            "image",
            "date_joined",
            "date_updated"
        )
        read_only_fields = ("id", "date_joined")
