from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Photo
from ..serializers import PhotoSerializer



class PhotoViewSet(viewsets.ModelViewSet):
  queryset = Photo.objects.all()
  serializer_class = PhotoSerializer
 

