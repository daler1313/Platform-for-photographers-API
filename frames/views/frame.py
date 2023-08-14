from django.shortcuts import render
from rest_framework import generics


from ..models import Frame
from ..serializer import FrameSerializer


# Create your views here.
class FrameList(generics.ListCreateAPIView):
  queryset = Frame.objects.all()
  serializer_class = FrameSerializer

class FrameDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Frame.objects.all()
  serializer_class = FrameSerializer