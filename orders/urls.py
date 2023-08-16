from django.urls import path, include
from rest_framework import routers
from .views import OrderDetailViewSet,OrderViewSet


router = routers.DefaultRouter()
router.register("order", OrderViewSet)
router.register("orderdetail", OrderDetailViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
