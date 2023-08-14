from django.urls import path
from .views import FrameList,FrameDetail


urlpatterns = [
    path("frame/", FrameList.as_view(), name="frame_list"),
    path("frame/<int:pk>/",FrameDetail.as_view(), name="frame_detail")
]
