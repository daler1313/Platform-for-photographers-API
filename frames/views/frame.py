from django.shortcuts import render
from rest_framework import viewsets


from ..models import Frame
from ..serializer import FrameSerializer


# Create your views here.
class FrameViewSet(viewsets.ModelViewSet):
  queryset = Frame.objects.all()
  serializer_class = FrameSerializer
