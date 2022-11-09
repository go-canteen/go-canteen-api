from rest_framework import routers
from .views import PenggunaViewSet

router = routers.DefaultRouter()
router.register(r"user", PenggunaViewSet)
