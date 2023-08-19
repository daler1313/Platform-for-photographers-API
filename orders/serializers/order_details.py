from rest_framework import serializers
from ..models import OrderDetail
from photos.serializers import PhotoSerializer
from frames.serializer import FrameSerializer
from .order import OrderSerializer

class OrderDetailSerializer(serializers.ModelSerializer):
  photo =PhotoSerializer()
  frame = FrameSerializer()
  order = OrderSerializer()
  class Meta:
    model = OrderDetail
    fields = ('id', "order", "photo", "frame", "quantity", "total_price")
