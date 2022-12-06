from rest_framework import routers


router = routers.DefaultRouter()

path('order/', CanteenList.as_view(), name='order'),
path('order/<uuid:pk>/', CanteenDetail.as_view(), name='order-detail'),
