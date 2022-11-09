from rest_framework import mixins, viewsets
from .models import Pengguna
from .permissions import IsThemselfOrReadOnly
from .serializers import (
    MinimizedPenggunaSerializer,
    PenggunaSerializer,
)
from dj_rest_auth.views import UserDetailsView


class PenggunaViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Pengguna.objects.all().order_by("-date_joined")
    serializer_class = PenggunaSerializer
    permissions = [IsThemselfOrReadOnly]

    def list(self, request):
        self.serializer_class = MinimizedPenggunaSerializer
        return super().list(self, request)

    def retrieve(self, request, pk=None):
        if request.user.pk != int(pk):
            self.serializer_class = MinimizedPenggunaSerializer
        return super().retrieve(self, request, pk=pk)


class PenggunaDetailsView(UserDetailsView):
    serializer_class = PenggunaSerializer
