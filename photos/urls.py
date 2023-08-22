from django.urls import path, include
from rest_framework import routers
from .views import PhotoViewSet,CategoryViewSet


router = routers.DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("photos", PhotoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
