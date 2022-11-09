from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsThemselfOrReadOnly(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return request.method in SAFE_METHODS or obj == user
