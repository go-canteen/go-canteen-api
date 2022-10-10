# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from main.serializers import UserSerializer
from rest_framework import authentication, permissions
import logging
import jwt, datetime

logger = logging.getLogger(__name__)

class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
