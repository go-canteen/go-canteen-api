from rest_framework import routers
from main.views import OrderList, OrderDetail
from django.urls import include, path

router = routers.DefaultRouter()

path('order/', OrderList.as_view(), name='order'),
path('order/<uuid:pk>/', OrderDetail.as_view(), name='order-detail'),
