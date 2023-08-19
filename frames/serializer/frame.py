from rest_framework import serializers
from ..models import Frame
from photographers.serializers import PhotographerSerializer

class FrameSerializer(serializers.ModelSerializer):
  photographer = PhotographerSerializer()
  class Meta:
    model = Frame
    fields = ('id',"frame","size","photographer","price")