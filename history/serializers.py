from rest_framework import serializers
from .models import History


class HistorySerializer(serializers.ModelSerializer):

    def get_username(self, obj):
        return obj.user.username

    name = serializers.SerializerMethodField("get_username")

    class Meta:
        model = History
        fields = (
            "transaction_date",
            "user",
            "name",
        )
        read_only_fields = ("transaction_date",)
