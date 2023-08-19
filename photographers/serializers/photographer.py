from rest_framework import serializers
from ..models import Photographer
from users.serializers import UserSerializer


class PhotographerSerializer(serializers.ModelSerializer):
  
  users = UserSerializer
  class Meta:
    model = Photographer
    fields = ('id', "users", "bio")
