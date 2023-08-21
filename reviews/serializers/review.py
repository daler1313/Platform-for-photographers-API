from rest_framework import serializers
from ..models import Review
from users.serializers import UserSerializer
from photos.serializers import PhotoSerializer


class ReviewSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  photo = PhotoSerializer()
  class Meta:
    model = Review
    fields = ('id', "photo", "user", "rating", "comment", "created_at")


class ReviewCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = ("photo", "user", "rating", "comment", "created_at")


class ReviewEditSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = ("photo", "user", "rating", "comment", "created_at")
  
