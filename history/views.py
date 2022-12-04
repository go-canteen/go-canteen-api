from django.shortcuts import render
from rest_framework import viewsets
from .models import History
from .serializers import HistorySerializer


class HistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows history to be viewed.
    """

    queryset = History.objects.all().order_by("-transaction_date")
    serializer_class = HistorySerializer