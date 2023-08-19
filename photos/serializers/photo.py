from rest_framework import serializers
from ..models import Photo
from photographers.serializers import PhotographerSerializer


class PhotoSerializer(serializers.ModelSerializer):
  photographer =  PhotographerSerializer()


  class Meta:
    model = Photo
    fields = ('id', "photographer", "title", "description","image", "category", "created_at", "price")
