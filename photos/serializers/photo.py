from rest_framework import serializers
from ..models import Photo


class PhotoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Photo
    fields = ('id', "photographer", "title", "description","image", "category", "created_at", "price")
