from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from users.models import User
from ..models import Review
from ..serializers import ReviewSerializer,ReviewEditSerializer,ReviewCreateSerializer


class ReviewViewSet(viewsets.ModelViewSet):
  queryset = Review.objects.all()
  permission_classes = [IsAuthenticated]

  def get_serializer_class(self):
      if self.action == 'create':
            return ReviewCreateSerializer
      elif self.action == 'update' or self.action == 'partial_update':
            return ReviewEditSerializer
      return ReviewSerializer


  def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != self.request.user:
            return Response("Вы не имеете доступа к обновлению", status=status.HTTP_403_FORBIDDEN)
        serializer = ReviewEditSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
  def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != self.request.user:
            return Response("Вы не имеете доступа к удалению", status=status.HTTP_403_FORBIDDEN)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
