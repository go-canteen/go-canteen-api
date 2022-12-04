from rest_framework import routers
from .views import HistoryViewSet

router = routers.DefaultRouter()
router.register(r"history", HistoryViewSet)