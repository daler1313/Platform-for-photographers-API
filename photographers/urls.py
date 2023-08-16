from django.urls import path, include
from rest_framework import routers
from .views import PhotographerViewSet


router = routers.DefaultRouter()
router.register("photographer", PhotographerViewSet)

urlpatterns = [
    path("", include(router.urls)),
  ] 