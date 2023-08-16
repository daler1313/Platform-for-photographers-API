from django.shortcuts import render
from rest_framework import viewsets


from ..models import Photographer
from ..serializers import PhotographerSerializer


class PhotographerViewSet(viewsets.ModelViewSet):
  queryset = Photographer.objects.all()
  serializer_class = PhotographerSerializer
