from django.contrib.auth.models import User, Group
from rest_framework import serializers
from main.models import Order

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

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "merchant",
            "content",
            "date",
        )
        read_only_fields = ("id", "user" ,"merchant" , "content" , "date")