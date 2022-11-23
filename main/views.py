# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets
from main.models import Canteen
from main.serializers import CanteenSerializer, UserSerializer
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

import logging

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer

class CanteenList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        canteens = Canteen.objects.all()
        serializer = CanteenSerializer(canteens, many=True)
        return Response({"canteens": serializer.data})

    def post(self, request, format=None):
        serializer = CanteenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CanteenDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_object(self, pk):
        try:
            return Canteen.objects.get(pk=pk)
        except Canteen.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        canteen = self.get_object(pk)
        serializer = CanteenSerializer(canteen)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        canteen = self.get_object(pk)
        serializer = CanteenSerializer(canteen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)