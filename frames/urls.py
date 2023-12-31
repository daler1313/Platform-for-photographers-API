from django.urls import path,include
from rest_framework import routers
from .views import FrameViewSet


router = routers.DefaultRouter()
router.register("frames", FrameViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
