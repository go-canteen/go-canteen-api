from rest_framework import routers
from main.views import CanteenList, CanteenDetail
from django.urls import include, path

router = routers.DefaultRouter()

urlpatterns = [
    path('canteens/', CanteenList.as_view(), name='canteens'),
    path('canteens/<uuid:pk>/', CanteenDetail.as_view(), name='canteen-detail'),
    path('', include(router.urls))
]

