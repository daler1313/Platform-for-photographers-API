from django.urls import path, include
from rest_framework import routers
from .views import PhotoViewSet,CategoryViewSet


router = routers.DefaultRouter()
router.register("category", CategoryViewSet)
router.register("photo", PhotoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
