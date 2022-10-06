from rest_framework import routers
from views import CanteenList, CanteenDetail
from django.urls import include, path

router = routers.DefaultRouter()

urlpatterns = [
    path('canteens/', CanteenList.as_view()),
    path('canteens/<int:pk>/', CanteenDetail.as_view()),
    path('', include(router.urls))
]

