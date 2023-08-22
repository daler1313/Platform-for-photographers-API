from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Photo
from ..serializers import PhotoSerializer,PhotoEditSerializer,PhotoCreateSerializer



class PhotoViewSet(viewsets.ModelViewSet):
  queryset = Photo.objects.all()
  permission_classes = [IsAuthenticated]

  def get_serializer_class(self):
      if self.action == 'create':
          return PhotoCreateSerializer
      elif self.action == 'update' or self.action == 'partial_update':
          return PhotoEditSerializer
      return PhotoSerializer

  def update(self, request, *args, **kwargs):
      instance = self.get_object()
      if instance.photographer.users == self.request.user:
          serializer = PhotoEditSerializer(
          instance, data=request.data, partial=True)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return Response(serializer.data)
      return Response("Вы не имеете доступа к обновлению", status=status.HTTP_403_FORBIDDEN)

  def destroy(self, request, *args, **kwargs):
      instance = self.get_object()
      if instance.photographer.users == self.request.user:
          instance.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
      return Response("Вы не имеете доступа к удалению", status=status.HTTP_403_FORBIDDEN)
 

